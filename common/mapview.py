"""The full-screen maps play.py draws when the terminal has room: the course as a sea of islands, one per
project, and each project as an island you pick a level on. The maps are painted in pixels, two to a
character cell (scenery.py has the sprites, the terrain and the weather); text goes on top in whole cells.
This file draws and reads keys; play.py decides what each key does.

    course_map(worlds, at)     -> (key, project), ("resize", project), or None if the screen is too small
    project_map(course, spot)  -> (key, value), ("resize", value), or None if the screen is too small
"""
import io
import json
import math
import os
import random
import re
import select
import shutil
import sys
import termios
import textwrap
import time
import tty
from pathlib import Path

import scenery
import trainer
from scenery import FLAG, LANDMARKS, MARKERS, THEMES, blob, curve


# ---------- the terminal ----------

def size():
    s = shutil.get_terminal_size((100, 30))
    return s.columns, s.lines


def out(s):
    sys.__stdout__.write(s)  # the real terminal, even while a trainer method's printing is being captured
    sys.__stdout__.flush()


def read_key(timeout=None):
    """A key, named the way trainer._read_key names them, or None if `timeout` seconds pass first."""
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    tty.setcbreak(fd, termios.TCSANOW)
    try:
        if timeout is not None and not select.select([fd], [], [], timeout)[0]:
            return None
        return trainer._read_key(fd)
    finally:
        termios.tcsetattr(fd, termios.TCSANOW, old)


class Canvas:
    """The screen as pixels, two to a character cell (one above the other, drawn with ▀), with text on
    top: a cell that holds text (a character, foreground, background, bold) hides its two pixels."""

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.px = [[0] * w for _ in range(2 * h)]
        self.cells = [[None] * w for _ in range(h)]

    def dot(self, x, y, color):
        if 0 <= x < self.w and 0 <= y < 2 * self.h:
            self.px[y][x] = color

    def shade(self, x, y, name):
        """Recolor a pixel through one of scenery's tables: "grey" for fog, "dark" for shadow."""
        if 0 <= x < self.w and 0 <= y < 2 * self.h:
            self.px[y][x] = scenery.table(name)[self.px[y][x]]

    def put(self, x, y, text, fg=None, bg=None, bold=False):
        """Write text at cell x, y. fg or bg None keeps the color already there (for bg: the pixel's)."""
        if 0 <= y < self.h:
            row = self.cells[y]
            for i, ch in enumerate(text, x):
                if 0 <= i < self.w:
                    _, f, b, _ = row[i] or (None, 252, self.px[2 * y + 1][i], False)
                    row[i] = (ch, f if fg is None else fg, b if bg is None else bg, bold)

    def crop(self, x, w):
        """A copy of the columns from x, w wide: what the screen shows of a picture wider than it."""
        c = Canvas.__new__(Canvas)
        c.w, c.h = w, self.h
        c.px, c.cells = [row[x:x + w] for row in self.px], [row[x:x + w] for row in self.cells]
        return c

    def render(self):
        parts, last = ["\033[H"], None
        for y, row in enumerate(self.cells):
            if y:
                parts.append("\n")
            upper, lower = self.px[2 * y], self.px[2 * y + 1]
            for x, cell in enumerate(row):
                ch, f, b, bold = cell or ((" ", b2, b2, False) if (b2 := lower[x]) == upper[x] else
                                          ("▀", upper[x], lower[x], False))
                if (f, b, bold) != last:
                    parts.append(f"\033[{1 if bold else 22};38;5;{f};48;5;{b}m")
                    last = (f, b, bold)
                parts.append(ch)
        return "".join(parts) + "\033[0m"


def waves(c, frame, cam, y0, y1, colors):
    """Short wave crests that come and go and drift over the water in pixel rows y0 to y1.
    colors: {a sea's color: its wave's}."""
    for py in range(y0, y1):
        row = c.px[py]
        for k in range(18):  # 18 crests in every 512 pixels of a row
            if scenery.rand(k, py, frame // 8) > 0.45:
                x = (int(scenery.rand(k, py, 3) * 512) + frame // 3 - cam) % 512
                for x in (x, x + 1):
                    if x < c.w and row[x] in colors:
                        row[x] = colors[row[x]]


def to_cells(pixels):
    """The character cells a path of pixels runs through, in order."""
    cells = []
    for x, y in pixels:
        if not cells or cells[-1] != (x, y // 2):
            cells.append((x, y // 2))
    return cells


def block(cells_x, cells_y):
    """The pixels of a block of character cells."""
    return {(x, 2 * y + half) for x in cells_x for y in cells_y for half in (0, 1)}


# ---------- looks ----------

OCEAN = 25, 39  # the open sea on the course map, and its waves
TILE = {"par": ("★", 16, 220), "solved": ("✓", 16, 41), "tried": ("✗", 231, 160), "new": ("·", 238, 250),
        "started": ("•", 231, 31)}
MARK = {"par": ("★", 220), "solved": ("✓", 41), "tried": ("✗", 160), "new": ("○", 244)}
GRADE_TILE = {"A": (16, 220), "B": (16, 41), "C": (16, 44), "D": (16, 208), "F": (231, 196)}  # bosses, once solved
CAMP = {"par": (16, 220), "solved": (16, 41), "started": (231, 31), "new": (252, 240), "practice": (231, 97)}
PANEL, TEXT, FAINT, HERO = 235, 252, 244, 226  # the bars, their text, and you (a black @ on yellow)


def status(course, ex, progress):
    """"par", "solved", "tried" or "new" for one exercise or drill."""
    e = course._entry(ex, progress)
    if e.get("solved"):
        return "par" if e["best"] <= ex.par else "solved"
    return "tried" if e.get("attempts") else "new"


def badge(course, ex, progress):
    """(symbol, foreground, background) for an exercise's tile: its grade if it's a solved boss."""
    st = status(course, ex, progress)
    if ex.boss and st in ("par", "solved"):
        g = trainer.grade(course._entry(ex, progress)["best"], ex.par)
        return (g, *GRADE_TILE[g])
    return TILE[st]


def mark(course, ex, progress):
    """(symbol, color) for a list of marks."""
    sym, fg, bg = badge(course, ex, progress)
    return (sym, bg) if ex.boss and sym in GRADE_TILE else MARK[status(course, ex, progress)]


def group_status(states):
    """One status for many: "par" if all at par, "solved" if all solved, "started" if any, else "new"."""
    if all(s == "par" for s in states):
        return "par"
    if all(s in ("par", "solved") for s in states):
        return "solved"
    return "started" if any(s != "new" for s in states) else "new"


def short(course):
    """ "Project 02 · Text objects: act on the thing you're in" -> "Text objects" """
    return course.title.split(" · ", 1)[-1].split(": ")[0]


def wrap(text, width, n):
    lines = textwrap.wrap(" ".join(text.split()), max(20, width))
    return lines[:n - 1] + [lines[n - 1] + ("…" if len(lines) > n else "")] if len(lines) >= n else lines


# ---------- layout ----------

def serpentine(n, left, top, width, height, pitch_x, pitch_y):
    """n points along rows that run left to right, then right to left, and so on: each in the middle of its
    own cell of a grid over the box. None if the cells would be narrower than pitch_x or shorter than pitch_y."""
    max_cols, max_rows = max(1, width // pitch_x), max(1, height // pitch_y)
    cols = min(max_cols, max(2, round((n * width / 2 / max(1, height)) ** 0.5)))  # cells are twice as tall as wide
    rows = -(-n // cols)
    if rows > max_rows:
        rows = -(-n // max_cols)
    cols = -(-n // rows)  # as few empty places in the last row as this many rows allows
    if rows > max_rows or cols > max_cols:
        return None
    xs = [left + int((i + 0.5) * width / cols) for i in range(cols)]
    ys = [top + int((r + 0.5) * height / rows) for r in range(rows)]
    return [(xs[c if r % 2 == 0 else cols - 1 - c], ys[r]) for r, c in (divmod(i, cols) for i in range(n))]


# ---------- a map ----------

class Board:
    """One full-screen map: the picture (sea, islands, roads, tiles), what moves over it (waves, lights,
    weather), the places you can stand, the paths between them, and the bars at the top and bottom."""

    def __init__(self, w, h, top, keys, describe, width=None):
        self.w, self.h, self.pic = w, h, Canvas(max(w, width or w), h)  # wider than the screen: it scrolls
        self.items = []  # (value, where you stand, the point used to find what's above or below it,
        #                  (first column, last column, row) of its tile, which gets arrows when you're on it)
        self.trails = {}  # i -> the cells you walk from item i to item i + 1
        self.top, self.keys, self.describe = top, keys, describe  # top: (left, right[, right when short of room])
        self.strip = None  # [(symbol, color)] per item, shown in the top bar with you on it
        self.linear = False  # items in one line: j and k go on and back like l and h
        self.seas = {}  # {a sea's color: its wave's}
        self.lights = []  # (x, y, colors): pixels that blink
        self.weather = []  # (kind, x0, y0, x1, y1, seed): an island's weather, over those pixels
        self.gulls = 0
        self.rows = (2, 2 * (h - 5))  # the pixel rows the map is in

    def animate(self, c, frame, cam):
        """Everything that moves, onto c: the part of the picture from column cam on."""
        waves(c, frame, cam, *self.rows, self.seas)
        for kind, x0, y0, x1, y1, seed in self.weather:
            if x1 > cam and x0 < cam + c.w:
                scenery.ambient(c, kind, frame, x0 - cam, y0, x1 - cam, y1, seed)
        for x, y, colors in self.lights:
            c.dot(x - cam, y, colors[(frame // 2 + x + y) % len(colors)])
        for k in range(self.gulls):  # gulls cross the sea
            x = int(scenery.rand(k, 1, 7) * self.pic.w + frame * (0.8 + 0.3 * k)) % self.pic.w - cam
            y = 2 + int(scenery.rand(k, 2, 7) * (self.h - 9)) + (frame // 8 + k) % 2
            if 0 <= x < c.w and c.cells[y][x] is None:
                c.put(x, y, "v" if (frame + k) % 6 < 3 else "-", 231)

    def tile(self, x, y, text, style):
        """A rounded tile centered on x: ▐ text ▌ in the style's colors."""
        _, fg, bg = style
        self.pic.put(x - 2, y, "▐", bg)
        self.pic.put(x - 1, y, text, fg, bg, bold=True)
        self.pic.put(x + 2, y, "▌", bg)

    def hero(self, c, x, y, frame, moving):
        """You: a badge that blinks yellow and white."""
        glow = HERO if moving or frame // 3 % 2 == 0 else 231
        c.put(x - 1, y, "▐", glow)
        c.put(x, y, "@", 16, glow, bold=True)
        c.put(x + 1, y, "▌", glow)

    def draw(self, frame, at, walker=None, extra=None):
        w, h = self.w, self.h
        value, spot, _, (left_x, right_x, box_y) = self.items[at]
        hx, hy = walker or spot
        cam = max(0, min(hx - w // 2, self.pic.w - w))  # the camera keeps you in the middle
        c = self.pic.crop(cam, w)
        self.animate(c, frame, cam)
        if extra:
            extra(c, cam)
        if not walker:  # arrows either side of the tile you're on
            c.put(left_x - 1 - cam, box_y, "▶", HERO, bold=True)
            c.put(right_x + 1 - cam, box_y, "◀", HERO, bold=True)
        self.hero(c, hx - cam, hy, frame, walker)
        if cam > 0:
            c.put(0, (h - 4) // 2, "◀", 231, bold=True)  # more map that way
        if cam + w < self.pic.w:
            c.put(w - 1, (h - 4) // 2, "▶", 231, bold=True)
        for y in (0, *range(h - 5, h)):
            c.put(0, y, " " * w, TEXT, PANEL)
        left, right = self.top[:2]
        strip = 2 * len(self.strip) + 3 if self.strip else 0
        if len(self.top) > 2 and len(left) + strip + len(right) + 4 > w:
            right = self.top[2]
        c.put(w - len(right) - 1, 0, right, TEXT, PANEL)
        c.put(1, 0, left[:max(0, w - len(right) - 4)], 220, PANEL, bold=True)
        if self.strip and len(left) + strip + len(right) + 4 <= w:
            for i, (sym, fg) in enumerate(self.strip):
                c.put(len(left) + 4 + 2 * i, 0, "@" if i == at else sym, HERO if i == at else fg, PANEL, bold=True)
        title, info, lines = self.describe(value)
        c.put(w - len(info) - 2, h - 5, info, TEXT, PANEL)
        c.put(2, h - 5, title[:max(0, w - len(info) - 6)], 230, PANEL, bold=True)
        for i, line in enumerate(lines[:3]):
            x = 2
            for text, fg in ([(line, TEXT)] if isinstance(line, str) else line):
                c.put(x, h - 4 + i, text, fg, PANEL)
                x += len(text)
        c.put(2, h - 1, self.keys[:w - 3], FAINT, PANEL)
        return c.render()

    def step(self, at, key):
        """Where a movement key takes you from item at, or None if key isn't a movement key."""
        last = len(self.items) - 1
        if key in ("l", "right", "w") or self.linear and key in ("j", "down"):
            return min(last, at + 1)
        if key in ("h", "left", "b") or self.linear and key in ("k", "up"):
            return max(0, at - 1)
        if key in ("g", "0"):
            return 0
        if key in ("G", "$"):
            return last
        return None

    def walk(self, a, b, frame):
        """Walk the path from item a to item b, if they're next to each other on it."""
        cells = self.trails.get(min(a, b)) if abs(a - b) == 1 else None
        if cells:
            path = cells if b > a else cells[::-1]
            for i, cell in enumerate(path[::max(1, len(path) // (24 if self.pic.w > self.w else 12))]):
                out(self.draw(frame + i // 3, a, walker=cell))
                time.sleep(0.015)

    def arrive(self, at, frame):
        """Called when you come to rest on an item."""


def run(board, at):
    """Show the board and walk around it until a key that isn't a move. Returns (key, at), or ("resize", at)
    when the terminal changes size."""
    shown, frame = size(), 0
    board.arrive(at, frame)
    while True:
        out(board.draw(frame, at))
        key = read_key(0.2)
        if key is None:
            frame += 1
            if size() != shown:
                return "resize", at
            continue
        to = board.step(at, key)
        if to is None:
            if key:
                return key, at
        elif to != at:
            board.walk(at, to, frame)
            at = to
            board.arrive(at, frame)


# ---------- the course: one island per project ----------

def celebrated(add=None):
    """The islands whose fireworks you've already seen (add one to remember it)."""
    path = Path(os.environ.get("VIMCOURSE_STATE") or trainer.COURSE_DIR) / ".celebrated.json"
    try:
        seen = set(json.loads(path.read_text()))
    except (OSError, ValueError):
        seen = set()
    if add and add not in seen:
        seen.add(add)
        try:
            path.write_text(json.dumps(sorted(seen)) + "\n")
        except OSError:
            pass
    return seen


def course_board(worlds, w, h):
    """The projects as islands in a line, left to right, each its own shape and country: the map scrolls
    with you. An island you haven't started lies in grey fog."""
    top, bottom = 1, h - 5
    if w < 64 or bottom - top < 12:
        return None
    gap = max(46, min(76, int(w / 2.3)))  # columns from one island to the next: two or three on screen
    width, mid = gap * len(worlds), (top + bottom) // 2
    ry = max(4.0, min(12.0, (bottom - top) * 0.37))  # in cells
    swing = max(0, (bottom - top) // 2 - int(ry * 1.2) - 1)  # how far up or down an island can sit
    pts = [(gap * i + gap // 2, round(mid + swing * math.sin(i * 2.1 + 0.4))) for i in range(len(worlds))]

    progress = {c: c._progress() for c in worlds}
    states = {c: [status(c, ex, progress[c]) for ex in c.exercises] for c in worlds}
    drills = {c: [status(c, ex, progress[c]) for ex in c.drills()] for c in worlds}

    def world_state(c):
        s = group_status(states[c])
        return "complete" if s == "par" and all(d in ("par", "solved") for d in drills[c]) else s

    def describe(c):
        ex_states, n = states[c], len(c.exercises)
        solved = sum(s in ("par", "solved") for s in ex_states)
        at_par, drilled = ex_states.count("par"), sum(d in ("par", "solved") for d in drills[c])
        ex = c._first_open(c.exercises)
        nxt = (f"Next up: {ex.number}. {ex.title}" if status(c, ex, progress[c]) in ("new", "tried") else
               f"Next: get {ex.number}. {ex.title} to par" if status(c, ex, progress[c]) == "solved" else
               "Every exercise at par" + (" and every drill solved." if world_state(c) == "complete" else "."))
        info = f"{solved}/{n} solved · {at_par} at par" + (f" · drills {drilled}/{len(drills[c])}" if drills[c] else "")
        marks = [("Exercises  ", FAINT)] + [mark(c, ex, progress[c]) for ex in c.exercises]
        return (f"WORLD {c.project_dir.name[:2]} · {short(c).upper()}", info,
                [c.title.split(" · ", 1)[-1], marks, nxt])

    total = sum(len(c.exercises) for c in worlds)
    solved = sum(s in ("par", "solved") for c in worlds for s in states[c])
    at_par = sum(states[c].count("par") for c in worlds)
    drilled, drill_total = sum(d in ("par", "solved") for c in worlds for d in drills[c]), sum(map(len, drills.values()))
    bar = ("◆ NEOVIM ISLANDS",
           f"★ {at_par} at par   ✓ {solved}/{total} exercises   » {drilled:,}/{drill_total:,} drills",
           f"★{at_par} ✓{solved}/{total} »{drilled}/{drill_total}")
    board = Board(w, h, bar, "h l sail  g G first / last  Enter go ashore  r lesson  p practice  t stats  q quit",
                  describe, width=width)
    board.linear, board.seas, board.gulls = True, {OCEAN[0]: OCEAN[1]}, 3
    pic = board.pic
    for row in pic.px:
        row[:] = [OCEAN[0]] * pic.w

    # the sea routes, bowing one way then the other
    routes = [curve((a[0] + 3, 2 * a[1]), (b[0] - 3, 2 * b[1]), 0.16 if i % 2 else -0.16)
              for i, (a, b) in enumerate(zip(pts, pts[1:]))]
    on_route = {p for r in routes for p in r}
    room = gap - 6  # for each project's name under its tile
    style = {"complete": TILE["par"], "par": TILE["solved"], "solved": TILE["solved"], "started": TILE["started"],
             "new": TILE["new"]}
    board.strip, board.done, taken = [], {}, set()
    for i, ((x, y), c) in enumerate(zip(pts, worlds)):
        number = int(c.project_dir.name[:2])
        theme, r = THEMES[number % len(THEMES)], random.Random(number * 7919)  # the same island every time
        land = blob(x, 2 * y, gap * r.uniform(0.32, 0.39), 2 * ry * r.uniform(0.85, 1.05), r)
        for _ in range(r.randint(0, 2)):  # an islet or two off the coast
            angle, far = r.uniform(0, 2 * math.pi), r.uniform(1.25, 1.45)
            land |= blob(x + math.cos(angle) * gap * 0.36 * far, 2 * y + math.sin(angle) * 2 * ry * far,
                         r.uniform(2, 4), r.uniform(1.5, 3), r)
        land |= block(range(x - 4, x + 5), range(y - 1, y + 2))  # room for the tile, its name and you
        land = {p for p in land if 2 * top <= p[1] < 2 * bottom and 0 <= p[0] < width} - taken
        taken |= land
        name = short(c) if len(short(c)) <= room else short(c)[:room - 1] + "…"
        label_x = x - len(name) // 2 - 1
        clear = block(range(x - 3, x + 4), (y - 1, y)) | block(range(label_x, label_x + len(name) + 2), (y + 1,))
        clear |= {(px + dx, py + dy) for px, py in on_route & land for dx in (-1, 0, 1) for dy in (-1, 0, 1)}
        sight = LANDMARKS[theme["landmark"]]
        spot = scenery.landmark_spot(land, sight, clear)
        if not spot:  # a small island: its landmark at half the size
            sight = sight.small()
            spot = scenery.landmark_spot(land, sight, clear)
        lights, box = scenery.paint_island(pic, land, theme, number, r, clear, [], spot, mark=sight)

        state = world_state(c)
        untouched = state == "new" and all(d == "new" for d in drills[c])
        xs, ys = [p[0] for p in land], [p[1] for p in land]
        x0, y0, x1, y1 = min(xs) - 3, max(2 * top, min(ys) - 2), max(xs) + 4, min(2 * bottom, max(ys) + 3)
        if untouched:  # not started: grey, in fog
            for py in range(y0, y1):
                for px in range(max(0, x0), min(width, x1)):
                    if pic.px[py][px] != OCEAN[0]:
                        pic.shade(px, py, "grey")
        else:
            board.lights += lights
            board.weather += [(kind, x0, y0, x1, y1, number) for kind in theme["ambient"]]
        cleared = state in ("complete", "par", "solved")
        if cleared and box:  # every exercise solved: a flag on its landmark, gold when it's all at par
            FLAG.stamp(pic, box[0] + box[2] // 2, box[1] - 4, swap=dict(F=220 if state != "solved" else 41))
        board.done[i] = (cleared, c.project_dir.name, x, 2 * y - 6)

        sym = "★" if state == "complete" else style[state][0]
        board.tile(x, y, sym + c.project_dir.name[:2], style[state])
        pic.put(label_x, y + 1, f" {name} ", 255, 236)
        board.items.append((c, (x, y - 1), (x, y), (x - 2, x + 2, y)))
        board.strip.append((sym, style[state][2]))
    for i, pixels in enumerate(routes):  # sailed routes are solid, the rest dashed
        sailed = world_state(worlds[i]) in ("complete", "par", "solved")
        for k, (px, py) in enumerate(pixels):
            if sailed or k % 4 < 2:
                pic.dot(px, py, 230 if sailed else 252)
        board.trails[i] = to_cells(pixels)

    def arrive(at, frame):  # fireworks, the first time you stand on an island with every exercise solved
        cleared, name, x, y = board.done[at]
        if cleared and name not in celebrated():
            for step in range(36):
                out(board.draw(frame + step, at, extra=lambda c, cam: scenery.fireworks(c, step, x - cam, y, at)))
                time.sleep(0.07)
            celebrated(add=name)
    board.arrive = arrive
    return board


def course_map(worlds, at):
    board = course_board(worlds, *size())
    if board is None:
        return None
    key, at = run(board, at)
    return key, worlds[at]


# ---------- one project: pick a level ----------

class Stage(Board):
    """One project: its island, with a winding road through its levels to the training camp at the end.
    The level you're on has its name and task in a box above it, and its details and a PLAY button on the
    right. menu: when the camp is open, (its commands and "practice", the one chosen)."""

    menu = None
    sheet = None  # a level's briefing or result, open over the map: (title, lines, first line shown, keys)

    def draw(self, frame, at, walker=None, extra=None):
        c = self.pic.crop(0, self.w)
        self.animate(c, frame, 0)
        value, spot, (x, y), _ = self.items[at]
        if not walker and not self.menu and not self.sheet:
            self.draw_popup(c, at, x, y)
        self.hero(c, *(walker or spot), frame, walker)
        if self.menu:
            value = self.menu[0][self.menu[1]]
            self.draw_menu(c)
        self.draw_panel(c, value, frame)
        if self.sheet:
            self.draw_sheet(c)
        return c.render()

    def sheet_room(self):
        """(columns, lines) of text a sheet holds."""
        return min(self.w - 8, 96), self.h - 7

    def draw_sheet(self, c):
        title, lines, first, keys = self.sheet
        width, room = self.sheet_room()
        left, top = (self.w - width - 4) // 2, 2
        c.put(left, top, "╔" + "═" * (width + 2) + "╗", 220, PANEL, bold=True)
        c.put(left + 2, top, f" {title} ", 16, 220, bold=True)
        for i in range(room):
            y = top + 1 + i
            c.put(left, y, "║" + " " * (width + 2) + "║", 220, PANEL, bold=True)
            x = left + 2
            for text, fg, bold in (lines[first + i] if first + i < len(lines) else ()):
                c.put(x, y, text[:max(0, left + 2 + width - x)], fg, PANEL, bold=bold)
                x += len(text)
        more = f" {first + 1}-{min(len(lines), first + room)} of {len(lines)} " if len(lines) > room else ""
        c.put(left, top + room + 1, "╟" + "─" * (width + 2) + "╢", 220, PANEL, bold=True)
        c.put(left + width + 2 - len(more), top + room + 1, more, FAINT, PANEL)
        c.put(left, top + room + 2, "║" + " " * (width + 2) + "║", 220, PANEL, bold=True)
        c.put(left + 2, top + room + 2, keys[:width], TEXT, PANEL)
        c.put(left, top + room + 3, "╚" + "═" * (width + 2) + "╝", 220, PANEL, bold=True)

    def draw_popup(self, c, at, x, y):
        """A box over the level you're on: its name, par and best, what to do, and which keys lead on."""
        title, facts, body = self.blurb(self.items[at][0])
        width = max(24, min(44, self.w - self.panel_w - 4))
        ways = "   ".join(f"{key} {word}" for to, word in ((at + 1, "on"), (at - 1, "back"))
                          if 0 <= to < len(self.items)
                          for key in [dict(right="l →", left="h ←", down="j ↓", up="k ↑")[self.heading(at, to)]])
        lines = [(title[:width], 231, True), (facts[:width], 223, False)]
        lines += [(text, TEXT, False) for text in wrap(body, width, 3)] + [(ways, FAINT, False)]
        width = max(len(text) for text, _, _ in lines)
        top = y - 3 - len(lines) - 1  # above you if there's room, else under the level
        if top < self.map_top:
            top = y + 1
        left = max(0, min(self.w - self.panel_w - width - 4, x - width // 2 - 2))
        c.put(left, top, "╭" + "─" * (width + 2) + "╮", 220, PANEL)
        for i, (text, fg, bold) in enumerate(lines, 1):
            c.put(left, top + i, "│ " + text.ljust(width) + " │", 220, PANEL)
            c.put(left + 2, top + i, text, fg, PANEL, bold=bold)
        c.put(left, top + len(lines) + 1, "╰" + "─" * (width + 2) + "╯", 220, PANEL)

    def draw_menu(self, c):
        """The training camp, open: its commands with your marks, and practice."""
        rows, sel = self.menu
        keys = max(len(label) for label, *_ in self.camp)
        width = min(self.w - self.panel_w - 4, keys + 36)
        room = max(3, self.map_bottom - self.map_top - 6)
        first = max(0, min(sel - room // 2, len(rows) - room))
        left, top = max(1, (self.w - self.panel_w - width) // 2 - 1), self.map_top + 1
        c.put(left, top, "╔" + "═" * width + "╗", 220, PANEL, bold=True)
        c.put(left + 2, top, " TRAINING CAMP ", 16, 220, bold=True)
        for i, (label, marks, count, style) in enumerate(self.camp[first:first + room], first):
            y = top + 1 + i - first
            c.put(left, y, "║" + " " * width + "║", 220, PANEL, bold=True)
            c.put(left + 2, y, f" {label.ljust(keys)} ", *(style if i != sel else (16, HERO)), bold=True)
            px = left + keys + 6
            for sym, color in marks:
                c.put(px, y, sym, color, PANEL)
                px += 1
            c.put(left + width - len(count) - 1, y, count, TEXT if i == sel else FAINT, PANEL)
            if i == sel:
                c.put(left + 1, y, "▶", HERO, PANEL, bold=True)
        y = top + 1 + min(room, len(rows))
        c.put(left, y, "║" + " j k choose   Enter play   q close".ljust(width)[:width] + "║", 220, PANEL)
        c.put(left + 1, y, " j k choose   Enter play   q close"[:width], FAINT, PANEL)
        c.put(left, y + 1, "╚" + "═" * width + "╝", 220, PANEL, bold=True)

    def draw_panel(self, c, value, frame):
        """The chosen level's (or drill's) details, and the button that plays it."""
        x0, top, bottom = self.w - self.panel_w, self.map_top, self.map_bottom
        width = self.panel_w - 4
        for y in range(top, bottom):
            c.put(x0, y, " " * self.panel_w, TEXT, PANEL)
        c.put(x0, top, "╭" + "─" * (self.panel_w - 2) + "╮", 240, PANEL)
        for y in range(top + 1, bottom - 1):
            c.put(x0, y, "│", 240, PANEL)
            c.put(x0 + self.panel_w - 1, y, "│", 240, PANEL)
        c.put(x0, bottom - 1, "╰" + "─" * (self.panel_w - 2) + "╯", 240, PANEL)
        head, title, stats, body, button = self.details(value)
        y = top + 1
        c.put(x0 + 2, y, head[:width], 223, PANEL, bold=True)
        for line in wrap(title, width, 2):
            y += 1
            c.put(x0 + 2, y, line, 231, PANEL, bold=True)
        y += 1
        for segments in stats:
            y += 1
            x = x0 + 2
            for text, fg in ([(segments, TEXT)] if isinstance(segments, str) else segments):
                c.put(x, y, text[:max(0, x0 + 2 + width - x)], fg, PANEL)
                x += len(text)
        room = bottom - 5 - (y + 2)  # lines left above the button
        if room > 0:
            for i, line in enumerate(wrap(body, width, room)):
                c.put(x0 + 2, y + 2 + i, line, FAINT, PANEL)
        green = 34 if frame // 3 % 2 == 0 else 40  # the button breathes
        bx, bw = x0 + 2, self.panel_w - 4
        c.put(bx, bottom - 4, "▄" * bw, green, PANEL)
        c.put(bx, bottom - 3, f"▶ {button}   Enter".center(bw), 231, green, bold=True)
        c.put(bx, bottom - 2, "▀" * bw, green, PANEL)

    def heading(self, a, b):
        """Which way the road runs from stop a to stop b: "right", "left", "down" or "up"."""
        (x1, y1), (x2, y2) = self.items[a][2], self.items[b][2]
        if abs(x2 - x1) >= 2 * abs(y2 - y1):  # a cell is twice as tall as it is wide
            return "right" if x2 > x1 else "left"
        return "down" if y2 > y1 else "up"

    def step(self, at, key):
        """You follow the road: a key moves you only if the road to the next stop, or back to the last one,
        runs that way. (w and b go on and back whichever way it runs.)"""
        last = len(self.items) - 1
        if key in ("g", "0"):
            return 0
        if key in ("G", "$"):
            return last
        if key in ("w", "b"):
            return max(0, min(last, at + (1 if key == "w" else -1)))
        way = dict(l="right", right="right", h="left", left="left", j="down", down="down", k="up", up="up").get(key)
        if not way:
            return None
        return next((to for to in (at + 1, at - 1) if 0 <= to <= last and self.heading(at, to) == way), at)


def project_board(course, w, h):
    number = int(course.project_dir.name[:2])
    theme, rng, progress = THEMES[number % len(THEMES)], random.Random(number), course._progress()
    levels, n = course.exercises, len(course.exercises)
    panel_w = max(26, min(36, w // 3))
    map_top, map_bottom, map_w = 1, h - 1, w - panel_w
    if w < 72 or map_bottom - map_top < 12:
        return None
    stops = n + 1  # the levels, then the training camp
    # each level's marker is two cells tall, with you standing above it: (x, y) is its lower middle cell
    pts = serpentine(stops, 4, map_top + 3, map_w - 10, map_bottom - map_top - 4, 9, 4)
    if pts:
        pts = [(x + rng.randint(-2, 2), y + rng.choice((-1, 0, 0, 1))) for x, y in pts]  # not quite a grid
    else:  # a small screen: rows closer together, so no room to wobble up and down
        pts = serpentine(stops, 4, map_top + 2, map_w - 10, map_bottom - map_top - 2, 8, 3)
        if not pts:
            return None
        pts = [(x + rng.randint(-1, 1), y) for x, y in pts]
    states = [status(course, ex, progress) for ex in levels]

    commands = course.drill_commands()
    drill_states = [status(course, ex, progress) for ex in course.drills()]
    drilled = sum(s in ("par", "solved") for s in drill_states)

    def blurb(value):  # for the box over the stop you're on: (name, facts, what to do)
        if value == "camp":
            return ("Training camp", f"{drilled}/{len(drill_states)} drills solved" if commands else "practice",
                    "Drills, one command at a time, and mixed practice. Enter opens it.")
        e = course._entry(value, progress)
        facts = f"par {value.par}" + (f" · best {e['best']}" if e.get("best") is not None else "")
        if value.boss:
            facts += " · boss" + (f", grade {badge(course, value, progress)[0]}" if e.get("solved") else "")
        return f"{value.number}. {value.title.removeprefix('Review · ')}", facts, value.task

    def details(value):
        if value == "camp":
            return ("TRAINING CAMP", "Drills and practice",
                    [f"{drilled}/{len(drill_states)} drills solved", f"{drill_states.count('par')} at par"],
                    "Short problems that practice one command at a time, and mixed practice from every "
                    "island so far.", "OPEN")
        if value == "practice":
            return ("PRACTICE", "Random drills", [f"from 00 to {course.project_dir.name[:2]}"],
                    "Drills from this world and every one before it, picked at random, as many as you like. The "
                    "ones you've missed or solved over par come up more often, and so do the ones you haven't "
                    "played for a while.", "PRACTICE")
        if isinstance(value, trainer.Command):
            its = [status(course, ex, progress) for ex in value.drills]
            ex = course._first_open(value.drills)
            solved = sum(s in ("par", "solved") for s in its)
            marks = [MARK[s] for s in its]
            return (f"TRAINING · {' '.join(value.keys.split())}", value.name,
                    [f"{solved}/{len(value.drills)} solved", f"{its.count('par')} at par", marks[:10], marks[10:]],
                    f"Next: drill {ex.number}, {ex.title}.", f"DRILL {ex.number}")
        e, st = course._entry(value, progress), status(course, value, progress)
        sym, _, color = badge(course, value, progress)
        word = {"par": "at par", "solved": "solved", "tried": "not solved yet", "new": "not tried yet"}[st]
        stats = [[(MARK[st][0] + " ", MARK[st][1]), (word, TEXT)],
                 f"par {value.par}" + (f"   best {e['best']}" if e.get("best") is not None else "")]
        if value.boss:
            stats.append([("grade ", FAINT), (sym, color)] if st in ("par", "solved") else
                         [("graded A to F once solved", FAINT)])
        return (f"LEVEL {value.number}" + (" · BOSS" if value.boss else ""), value.title.removeprefix("Review · "),
                stats, value.task, "PLAY")

    left = f"◆ WORLD {course.project_dir.name[:2]} · {short(course).upper()}"
    right = f"★ {states.count('par')}/{n} at par" + (
        f"   » drills {sum(s in ('par', 'solved') for s in drill_states)}/{len(drill_states)}" if drill_states else "")
    board = Stage(w, h, (left, right), "h j k l follow the road  Enter play  r lesson  p practice  t stats  q back",
                  None)
    board.n, board.panel_w, board.map_top, board.map_bottom, board.details = n, panel_w, map_top, map_bottom, details
    board.blurb = blurb
    board.rows, board.seas = (2 * map_top, 2 * map_bottom), {theme["sea"]: theme["wave"]}
    pic = board.pic
    for py in range(*board.rows):
        pic.px[py][:map_w] = [theme["sea"]] * map_w

    # the island: big enough for every level, with a winding road from each to the next
    inside = {(x, y) for x in range(1, map_w - 1) for y in range(board.rows[0] + 1, board.rows[1] - 1)}
    roads = [curve((a[0], 2 * a[1]), (b[0], 2 * b[1]), rng.uniform(0.2, 0.4) * rng.choice((-1, 1)))
             for a, b in zip(pts, pts[1:])]
    roads = [[p for p in road if p in inside] for road in roads]
    land = blob(map_w / 2, map_top + map_bottom, map_w / 2 - 2, map_bottom - map_top - 1.4, rng)
    clear = set()
    for x, y in pts:  # every level on dry land, with room for you above it and its number beside it
        land |= block(range(x - 4, x + 7), range(y - 2, y + 1))
        clear |= block(range(x - 3, x + 6), (y - 1, y)) | block(range(x - 1, x + 2), (y - 2,))
    for road in roads:
        land |= {(x + dx, y + dy) for x, y in road for dx in (-2, -1, 0, 1, 2) for dy in (-2, -1, 0, 1, 2)}
    land &= inside
    on_road = {p for road in roads for p in road}
    big = 2 if map_w >= 96 and map_bottom - map_top >= 26 else 1  # room for a landmark twice the size
    sight = LANDMARKS[theme["landmark"]]
    spot = scenery.landmark_spot(land, sight, clear | on_road, big)
    if not spot and big == 2:
        big, spot = 1, scenery.landmark_spot(land, sight, clear | on_road)
    walked = [states[i] in ("par", "solved") for i in range(n)]
    lights, box = scenery.paint_island(pic, land, theme, number, rng, clear, list(zip(roads, walked)), spot, big)

    # fog: the country around a level stays grey until you've reached it (solved the one before it)
    reached = [i == 0 or states[i] != "new" or states[i - 1] in ("par", "solved") for i in range(n)]
    reached.append(states[-1] in ("par", "solved") or any(s != "new" for s in drill_states))  # the camp
    centers, fogged = [(x, 2 * y) for x, y in pts], set()
    if not all(reached):
        for py in range(*board.rows):
            for px in range(map_w):
                if pic.px[py][px] != theme["sea"]:
                    nearest = min(range(stops), key=lambda i: (centers[i][0] - px) ** 2 + (centers[i][1] - py) ** 2)
                    if not reached[nearest]:
                        pic.shade(px, py, "grey")
                        fogged.add((px, py))
    board.lights = [light for light in lights if light[:2] not in fogged]
    if any(s != "new" for s in states + drill_states):  # an island you haven't started has no weather yet
        board.weather = [(kind, 0, board.rows[0], map_w, board.rows[1], number) for kind in theme["ambient"]]
    if box and all(s in ("par", "solved") for s in states):  # all solved: a flag on the landmark
        FLAG.stamp(pic, box[0] + box[2] // 2, box[1] - 4, swap=dict(F=220 if all(s == "par" for s in states) else 41))

    for y in (0, h - 1):  # the bars
        pic.put(0, y, " " * w, TEXT, PANEL)
    pic.put(w - len(right) - 1, 0, right, TEXT, PANEL)
    pic.put(1, 0, left[:max(0, w - len(right) - 4)], 220, PANEL, bold=True)
    pic.put(2, h - 1, board.keys[:w - 3], FAINT, PANEL)
    for i, ((x, y), ex, st) in enumerate(zip(pts, levels, states)):
        sym, _, color = badge(course, ex, progress)
        shape = MARKERS["skull" if ex.boss and theme["name"] == "fortress" else "boss" if ex.boss else "level"]
        shape.stamp(pic, x - 2, 2 * y - 2, swap=dict(C=color if st != "new" else 250 if reached[i] else 244))
        if st in ("par", "solved"):  # a flag planted on a solved level: gold at par
            FLAG.stamp(pic, x - 5, 2 * y - 4, swap=dict(F=220 if st == "par" else 41))
        pic.put(x + 3, y, f"{ex.number}", 255, 236)
        board.items.append((ex, (x, y - 2), (x, y), None))
    x, y = pts[-1]  # the training camp, at the end of the road
    scenery.CAMP.stamp(pic, x - 2, 2 * y - 2)
    pic.put(x + 3, y, "camp", 255, 236)
    board.items.append(("camp", (x, y - 2), (x, y), None))
    board.rows_of_camp, board.camp = [], []
    for value in [*commands, "practice"]:
        if value == "practice":
            board.camp.append(("∞ practice", [], "", CAMP["practice"]))
        else:
            sts = [status(course, ex, progress) for ex in value.drills]
            board.camp.append((" ".join(value.keys.split()), [MARK[s] for s in sts],
                               f"{sum(s in ('par', 'solved') for s in sts)}/{len(sts)}", CAMP[group_status(sts)]))
        board.rows_of_camp.append(value)
    board.trails = {i: to_cells(road) for i, road in enumerate(roads)}
    return board


# ---------- playing a level without leaving the map ----------

SCREEN = "\033[?1049h\033[?25l\033[?7l"  # back to the map's screen after Neovim (the same as play.py's)
INK = {"31": 203, "32": 41, "33": 220, "36": 80}  # the trainer's colors, as the map's


def captured(fn, *args, width):
    """Run one of the trainer's printing methods and take what it prints: (what it returned, the text as
    lines of (text, color, bold) pieces, wrapped for `width` columns)."""
    printed, columns, stdout = io.StringIO(), trainer._columns, sys.stdout
    trainer._columns, sys.stdout = (lambda: width + 2), printed
    try:
        result = fn(*args)
    finally:
        trainer._columns, sys.stdout = columns, stdout
    lines, fg, bold = [], TEXT, False
    for raw in printed.getvalue().strip("\n").split("\n"):
        pieces = []
        for part in re.split(r"(\033\[[0-9;]*m)", raw.split("\r")[-1]):
            if part.startswith("\033["):
                for code in part[2:-1].split(";"):
                    fg, bold = (TEXT, False) if code in ("", "0") else (fg, True) if code == "1" else \
                        (FAINT, bold) if code == "2" else (INK.get(code, fg), bold)
            elif part:
                pieces.append((part, fg, bold))
        lines.append(pieces)
    return result, lines


def read_sheet(board, at):
    """Show the board's sheet until a key that isn't scrolling, and return it (None: the screen changed size)."""
    shown, frame = size(), 0
    while True:
        title, lines, first, keys = board.sheet
        out(board.draw(frame, at))
        key = read_key(0.2)
        frame += 1
        if key is None:
            if size() != shown:
                return None
            continue
        room = board.sheet_room()[1]
        move = dict(j=1, down=1, k=-1, up=-1, d=room // 2, u=-(room // 2), g=-len(lines), G=len(lines)).get(key)
        if key == " ":
            move = room - 1
        if move is None:
            return key
        board.sheet = (title, lines, max(0, min(len(lines) - room, first + move)), keys)


def session(board, at, course, ex):
    """A level, start to finish, in sheets over the map: its briefing, then Neovim, then how it went.
    Returns "next" or "prev" if you're moving on, else None."""
    width = board.sheet_room()[0]
    name = ex.command.label(ex) if ex.command else f"LEVEL {ex.number}" + (" · BOSS" if ex.boss else "")
    answer = "   s solution   w watch it" if course._solution(ex) else ""
    _, lines = captured(course._intro, ex, width=width)
    board.sheet, outcome = (name, lines, 0, "Enter start   j k scroll" + answer + "   q back"), None

    def grading():  # Neovim has just closed: straight back to the map while the try is graded
        board.sheet = (name, [[("Grading…", FAINT, False)]], 0, "")
        out(SCREEN + board.draw(0, at))
    try:
        while True:
            key = read_sheet(board, at)
            if key in (None, "q", "esc", "backspace"):
                return None
            title, lines, first, keys = board.sheet
            if key == "s" and answer:
                _, more = captured(course._reveal, ex, width=width)
                board.sheet = (title, lines + [[]] + more, max(0, len(lines) + 1 + len(more) - board.sheet_room()[1]), keys)
            elif key == "w" and answer:
                captured(course._watch_it, ex, width=width)
                out(SCREEN)
            elif key == "enter" and outcome == "solved":
                return "next"
            elif key in ("enter", "r"):
                trainer.AFTER_PLAY = grading
                try:
                    outcome, lines = captured(course._attempt, ex, width=width)
                finally:
                    trainer.AFTER_PLAY = None
                out(SCREEN)
                if outcome in ("prev", "next"):  # F7 or F9 in Neovim
                    return outcome
                go = "Enter next   r retry" if outcome == "solved" else "Enter retry"
                board.sheet = (name + " · " + {"solved": "SOLVED", "unsolved": "NOT YET"}.get(outcome, "NOT PLAYED"),
                               lines, 0, go + "   j k scroll" + answer + "   q back to the map")
    finally:
        board.sheet = None


def project_map(course, spot):
    """Walk around one project, starting on spot (an exercise, "camp", or a drill command to have the camp
    open on). Levels and drills are played here, in sheets over the map; anything else is play.py's:
    returns (key, value)."""
    board = project_board(course, *size())
    if board is None:
        return None
    rows = board.rows_of_camp
    in_camp = spot in rows  # back from a drill: the camp is still open, on that command
    at = board.n if in_camp else next((i for i, item in enumerate(board.items) if item[0] is spot), 0)

    def play(ex):  # a level or drill, then the island again as it is now
        nonlocal board
        outcome = session(board, at, course, ex)
        board = project_board(course, *size())
        return outcome

    while True:
        if not in_camp:
            key, at = run(board, at)
            value = board.items[at][0]
            if key != "enter":
                return key, value
            if value != "camp":
                outcome = play(value)
                if board is None:
                    return "resize", value
                to = at + (1 if outcome == "next" else -1 if outcome == "prev" else 0)
                if to != at and 0 <= to < len(board.items):  # solved (or F7, F9): walk on
                    board.walk(at, to, 0)
                    at = to
                continue
        board.menu, frame, shown, picked = (rows, rows.index(spot) if spot in rows else 0), 0, size(), None
        while board.menu:  # the camp's list: j k choose, Enter play, q close
            out(board.draw(frame, at))
            key, sel = read_key(0.2), board.menu[1]
            frame += 1
            if key is None and size() != shown:
                return "resize", rows[sel]
            if key in ("j", "down", "k", "up", "g", "G"):
                sel = dict(j=sel + 1, down=sel + 1, k=sel - 1, up=sel - 1, g=0, G=len(rows) - 1)[key]
                board.menu = (rows, max(0, min(len(rows) - 1, sel)))
            elif key == "enter":
                picked, board.menu = rows[sel], None
            elif key in ("q", "esc", "h", "left", "backspace"):
                board.menu = None
        in_camp = spot = None
        if picked == "practice":
            return "enter", picked
        if picked:  # drills of one command, one after another for as long as you solve them
            ex = course._first_open(picked.drills)
            while ex:
                outcome = play(ex)
                if board is None:
                    return "resize", picked
                i = picked.drills.index(ex) + (1 if outcome == "next" else -1 if outcome == "prev" else len(picked.drills))
                ex = picked.drills[i] if 0 <= i < len(picked.drills) else None
            rows, in_camp, spot = board.rows_of_camp, True, picked
