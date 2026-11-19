"""The full-screen maps play.py draws when the terminal has room: the course as an ocean of islands, one
per project, and each project as an island whose trail runs through its exercises, with its drills at a
training camp below. This file draws and reads keys; play.py decides what each key does.

    course_map(worlds, at)     -> (key, project), ("resize", project), or None if the screen is too small
    project_map(course, spot)  -> (key, value), ("resize", value), or None if the screen is too small
"""
import math
import random
import select
import shutil
import sys
import termios
import textwrap
import time
import tty

import trainer


# ---------- the terminal ----------

def size():
    s = shutil.get_terminal_size((100, 30))
    return s.columns, s.lines


def out(s):
    sys.stdout.write(s)
    sys.stdout.flush()


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
    """The whole screen as cells: a character, a foreground and a background color (xterm's 256), bold."""

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.cells = [[(" ", 252, 0, False)] * w for _ in range(h)]

    def put(self, x, y, text, fg=None, bg=None, bold=False):
        """Write text at x, y. fg or bg None keeps the color already there."""
        if 0 <= y < self.h:
            row = self.cells[y]
            for i, ch in enumerate(text, x):
                if 0 <= i < self.w:
                    _, f, b, _ = row[i]
                    row[i] = (ch, f if fg is None else fg, b if bg is None else bg, bold)

    def copy(self):
        c = Canvas.__new__(Canvas)
        c.w, c.h, c.cells = self.w, self.h, [row[:] for row in self.cells]
        return c

    def render(self):
        parts, last = ["\033[H"], None
        for y, row in enumerate(self.cells):
            if y:
                parts.append("\n")
            for ch, f, b, bold in row:
                if (f, b, bold) != last:
                    parts.append(f"\033[{1 if bold else 22};38;5;{f};48;5;{b}m")
                    last = (f, b, bold)
                parts.append(ch)
        return "".join(parts) + "\033[0m"


# ---------- looks ----------

# Each project's island: its land, coast and sea (with the color of its waves), the trail once it's walked,
# and the scenery scattered over it as (character, color).
THEMES = [
    dict(land=71, coast=186, sea=25, wave=39, trail=230,  # 00 meadow
         deco=[("♣", 22), ("♣", 28), ("*", 224), ("*", 218), ('"', 65)]),
    dict(land=29, coast=143, sea=24, wave=31, trail=223,  # 01 pine forest
         deco=[("♠", 22), ("♠", 23), ("♣", 22), ("'", 65)]),
    dict(land=179, coast=222, sea=30, wave=44, trail=231,  # 02 dunes
         deco=[("ψ", 28), ("∩", 137), (".", 137), ("°", 137)]),
    dict(land=254, coast=252, sea=67, wave=153, trail=60,  # 03 snowfield
         deco=[("▲", 23), ("▲", 29), ("*", 153), (".", 248)]),
    dict(land=173, coast=180, sea=31, wave=80, trail=230,  # 04 canyon
         deco=[("∩", 130), ("▲", 94), (".", 131), ("ψ", 64)]),
    dict(land=65, coast=101, sea=23, wave=29, trail=187,  # 05 marsh
         deco=[("♣", 58), ("¥", 64), ("~", 30), ("*", 143)]),
    dict(land=239, coast=236, sea=124, wave=208, trail=214,  # 06 volcano, in a lava sea
         deco=[("▲", 52), ("▲", 88), ("∴", 244), ("*", 202)]),
    dict(land=60, coast=238, sea=17, wave=62, trail=189,  # 07 crystal caverns
         deco=[("◆", 51), ("◆", 213), ("◆", 147), (".", 103)]),
    dict(land=255, coast=253, sea=39, wave=117, trail=67,  # 08 cloud kingdom
         deco=[("~", 153), ("°", 117), ("+", 189), (".", 250)]),
    dict(land=60, coast=59, sea=17, wave=25, trail=229,  # 09 twilight town
         deco=[("⌂", 223), ("⌂", 216), ("♣", 23), (".", 146)]),
    dict(land=240, coast=237, sea=52, wave=160, trail=220,  # 10 the fortress
         deco=[("Π", 250), ("Π", 246), ("^", 243), (".", 236)]),
]
OCEAN = dict(sea=25, wave=39)  # around the islands on the course map
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


def line(a, b):
    """The cells on the straight line from a to b, leaving out both ends."""
    (x0, y0), (x1, y1) = a, b
    dx, dy, sx, sy = abs(x1 - x0), -abs(y1 - y0), 1 if x1 > x0 else -1, 1 if y1 > y0 else -1
    err, cells = dx + dy, []
    while (x0, y0) != (x1, y1):
        e2 = 2 * err  # both steps test the error from before either one
        if e2 >= dy:
            err, x0 = err + dy, x0 + sx
        if e2 <= dx:
            err, y0 = err + dx, y0 + sy
        cells.append((x0, y0))
    return cells[:-1]


def route(a, b, half):
    """The cells from tile a to tile b further right: along a's row to halfway, up or down to b's row, then
    along it."""
    (x1, y1), (x2, y2) = a, b
    mid, step = (x1 + x2) // 2, 1 if y2 > y1 else -1
    return ([(x, y1) for x in range(x1 + half + 1, mid + 1)] + [(mid, y) for y in range(y1 + step, y2 + step, step)
            if y1 != y2] + [(x, y2) for x in range(mid + 1, x2 - half)])


def blob(cx, cy, rx, ry, rng):
    """The cells of one island: an ellipse whose edge swells and dips with a few random waves, so no two
    islands have the same coast."""
    waves = [(rng.choice((2, 3, 4, 5, 6)), rng.uniform(0.05, 0.13), rng.uniform(0, 2 * math.pi)) for _ in range(3)]
    cells = set()
    for y in range(int(cy - ry * 1.4) - 1, int(cy + ry * 1.4) + 2):
        for x in range(int(cx - rx * 1.4) - 1, int(cx + rx * 1.4) + 2):
            dx, dy = (x - cx) / rx, (y - cy) / ry
            if math.hypot(dx, dy) < 1 + sum(a * math.sin(k * math.atan2(dy, dx) + p) for k, a, p in waves):
                cells.add((x, y))
    return cells


# ---------- a map ----------

class Board:
    """One full-screen map: the picture that doesn't move (sea, land, scenery, trails, tiles), the places you
    can stand, the trails between them, and the bars at the top and bottom."""

    def __init__(self, w, h, top, keys, describe, width=None):
        self.w, self.h, self.pic = w, h, Canvas(max(w, width or w), h)  # wider than the screen: it scrolls
        self.sea = {}  # column -> [(y, wave color, sea color)]: the cells that get waves
        self.items = []  # (value, where you stand, the point used to find what's above or below it,
        #                  (first column, last column, row) of its tile, which gets arrows when you're on it)
        self.trails = {}  # i -> the cells you walk from item i to item i + 1
        self.top, self.keys, self.describe = top, keys, describe  # top: (left, right[, right when short of room])
        self.strip = None  # [(symbol, color)] per item, shown in the top bar with you on it
        self.linear = False  # items in one line: j and k go on and back like l and h

    def paint(self, land, top, bottom, theme_at, sea, rng, reserved):
        """Sea, land with its coast, and scenery on the land that nothing else needs."""
        for y in range(top, bottom):
            for x in range(self.pic.w):
                if (x, y) not in land:
                    self.pic.put(x, y, " ", sea["wave"], sea["sea"])
                    if (x, y) not in reserved:  # trails over the water stay calm
                        self.sea.setdefault(x, []).append((y, sea["wave"], sea["sea"]))
                    continue
                t = theme_at(x, y)
                coast = any(p not in land for p in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))
                self.pic.put(x, y, " ", 252, t["coast"] if coast else t["land"])
                if not coast and (x, y) not in reserved and rng.random() < 0.09:
                    ch, fg = rng.choice(t["deco"])
                    self.pic.put(x, y, ch, fg)

    def tile(self, x, y, text, style):
        """A rounded tile centered on x: ▐ text ▌ in the style's colors."""
        _, fg, bg = style
        self.pic.put(x - 2, y, "▐", bg)
        self.pic.put(x - 1, y, text, fg, bg, bold=True)
        self.pic.put(x + 2, y, "▌", bg)

    def draw(self, frame, at, walker=None):
        w, h = self.w, self.h
        value, spot, _, (left_x, right_x, box_y) = self.items[at]
        hx, hy = walker or spot
        cam = max(0, min(hx - w // 2, self.pic.w - w))  # the camera keeps you in the middle
        c = Canvas.__new__(Canvas)
        c.w, c.h, c.cells = w, h, [row[cam:cam + w] for row in self.pic.cells]
        for x in range(cam, cam + w):  # waves drift a little each frame
            for y, wave, sea in self.sea.get(x, ()):
                if (x + 3 * y - frame) % 13 == 0 or (x - 2 * y + frame) % 23 == 0:
                    c.put(x - cam, y, "~", wave, sea)
        if not walker:  # arrows either side of the tile you're on
            c.put(left_x - 1 - cam, box_y, "▶", HERO, bold=True)
            c.put(right_x + 1 - cam, box_y, "◀", HERO, bold=True)
        glow = HERO if frame % 2 == 0 or walker else 231  # you: a badge that blinks yellow and white
        c.put(hx - cam - 1, hy, "▐", glow)
        c.put(hx - cam, hy, "@", 16, glow, bold=True)
        c.put(hx - cam + 1, hy, "▌", glow)
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
        if key in ("j", "down", "k", "up"):
            x0, y0 = self.items[at][2]
            below = key in ("j", "down")
            near = [(abs(y - y0), abs(x - x0), i) for i, (_, _, (x, y), _) in enumerate(self.items)
                    if (y > y0 if below else y < y0)]
            return min(near)[2] if near else at
        return None

    def walk(self, a, b, frame):
        """Walk the trail from item a to item b, if they're next to each other on it."""
        cells = self.trails.get(min(a, b)) if abs(a - b) == 1 else None
        if cells:
            path = cells if b > a else cells[::-1]
            for cell in path[::max(1, len(path) // (24 if self.pic.w > self.w else 10))]:  # scrolling: smoother
                out(self.draw(frame, a, walker=cell))
                time.sleep(0.015)


def run(board, at):
    """Show the board and walk around it until a key that isn't a move. Returns (key, at), or ("resize", at)
    when the terminal changes size."""
    shown, frame = size(), 0
    while True:
        out(board.draw(frame, at))
        key = read_key(0.45)
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


# ---------- the course: one island per project ----------

def course_board(worlds, w, h):
    """The projects as islands in a line, left to right, each a different shape: the map scrolls with you."""
    top, bottom = 1, h - 5
    if w < 64 or bottom - top < 12:
        return None
    gap = max(40, min(70, int(w / 2.6)))  # columns from one island to the next: two or three on screen
    width, mid = gap * len(worlds), (top + bottom) // 2
    ry = max(3.0, min(9.0, (bottom - top) * 0.28))
    swing = max(0, (bottom - top) // 2 - int(ry * 1.15) - 3)  # how far up or down an island can sit
    pts = [(gap * i + gap // 2, round(mid + swing * math.sin(i * 2.1 + 0.4))) for i in range(len(worlds))]
    land, owner = set(), {}
    for i, ((x, y), c) in enumerate(zip(pts, worlds)):
        r = random.Random(int(c.project_dir.name[:2]) * 7919)  # the same shape every time
        cells = blob(x, y, gap * r.uniform(0.24, 0.31), ry * r.uniform(0.75, 1.05), r)
        for _ in range(r.randint(0, 2)):  # an islet or two off the coast
            angle, far = r.uniform(0, 2 * math.pi), r.uniform(1.25, 1.45)
            cells |= blob(x + math.cos(angle) * gap * 0.28 * far, y + math.sin(angle) * ry * far,
                          r.uniform(1.5, 3.5), r.uniform(0.8, 1.5), r)
        cells |= {(x + dx, y + dy) for dx in range(-3, 4) for dy in (-1, 0, 1)}  # room for the tile and you
        for cell in cells:
            if top <= cell[1] < bottom and cell not in owner:
                land.add(cell)
                owner[cell] = i

    room = gap - 6  # for each project's name under its tile
    reserved, trails, labels = set(), {}, []
    for i, ((x, y), c) in enumerate(zip(pts, worlds)):
        name = short(c) if len(short(c)) <= room else short(c)[:room - 1] + "…"
        labels.append((x - len(name) // 2 - 1, y + 1, f" {name} "))
        reserved |= {(x + d, y) for d in range(-2, 3)} | {(x + d, y - 1) for d in (-1, 0, 1)}
        reserved |= {(labels[-1][0] + d, y + 1) for d in range(len(name) + 2)}
    for i in range(len(pts) - 1):
        trails[i] = route(pts[i], pts[i + 1], 2)
        reserved |= set(trails[i])

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
    top = ("◆ NEOVIM ISLANDS",
           f"★ {at_par} at par   ✓ {solved}/{total} exercises   » {drilled:,}/{drill_total:,} drills",
           f"★{at_par} ✓{solved}/{total} »{drilled}/{drill_total}")
    board = Board(w, h, top, "h l sail  g G first / last  Enter go ashore  r lesson  p practice  t stats  q quit",
                  describe, width=width)
    board.linear = True
    board.paint(land, top=1, bottom=bottom, sea=OCEAN, rng=random.Random(2026), reserved=reserved,
                theme_at=lambda x, y: THEMES[int(worlds[owner[x, y]].project_dir.name[:2]) % len(THEMES)])
    for i, cells in trails.items():
        done = world_state(worlds[i]) in ("complete", "par", "solved")
        for x, y in cells:
            board.pic.put(x, y, "·", 230 if done else 245, bold=done)
    style = {"complete": TILE["par"], "par": TILE["solved"], "solved": TILE["solved"], "started": TILE["started"],
             "new": TILE["new"]}
    board.strip = []
    for (x, y), c, (lx, ly, label) in zip(pts, worlds, labels):
        state = world_state(c)
        sym = "★" if state == "complete" else style[state][0]
        board.tile(x, y, sym + c.project_dir.name[:2], style[state])
        board.pic.put(lx, ly, label, 255, 236)
        if state == "complete":
            board.pic.put(x, y - 1, "⚑", 220, bold=True)
        board.items.append((c, (x, y - 1), (x, y), (x - 2, x + 2, y)))
        board.strip.append((sym, style[state][2]))
    board.trails = trails
    return board


def course_map(worlds, at):
    board = course_board(worlds, *size())
    if board is None:
        return None
    key, at = run(board, at)
    return key, worlds[at]


# ---------- one project: pick a level ----------

class Stage(Board):
    """One project as a stage select: a row of level cards along the top with the chosen one in the middle,
    the island below with a dotted route through its levels, the chosen level's details and a PLAY button on
    the right, and the training camp's drills in a row along the bottom."""

    def draw(self, frame, at, walker=None):
        w, h, n = self.w, self.h, self.n
        c = self.pic.copy()
        for x, column in self.sea.items():
            for y, wave, sea in column:
                if (x + 3 * y - frame) % 13 == 0 or (x - 2 * y + frame) % 23 == 0:
                    c.put(x, y, "~", wave, sea)
        if at < n:
            self.last_level = at
        self.draw_cards(c, self.last_level, at < n)
        chip = self.draw_camp(c, at - n if at >= n else None)
        glow = HERO if frame % 2 == 0 or walker else 231  # you: a badge that blinks yellow and white
        hx, hy = walker or (self.items[at][1] if at < n else chip)
        c.put(hx - 1, hy, "▐", glow)
        c.put(hx, hy, "@", 16, glow, bold=True)
        c.put(hx + 1, hy, "▌", glow)
        self.draw_panel(c, self.items[at][0], frame)
        return c.render()

    def draw_cards(self, c, sel, focused):
        """The level cards, the chosen one in the middle; the ones that don't fit run off the edges."""
        cw, top = self.card_w, 1
        mid = (self.w - cw) // 2
        for i, (title, detail, (sym, color), boss) in enumerate(self.cards):
            x = mid + (i - sel) * (cw + 1)
            if x + cw <= 0 or x >= self.w:
                continue
            chosen = i == sel
            fg, bg, edge = (16, 230, 220 if focused else 250) if chosen else (250, 237, 243)
            h_, v, corners = ("═", "║", "╔╗╚╝") if chosen else ("─", "│", "┌┐└┘")
            c.put(x, top, corners[0] + h_ * (cw - 2) + corners[1], edge, PANEL, bold=chosen)
            for r, text in ((1, title), (2, detail)):
                c.put(x, top + r, v, edge, PANEL, bold=chosen)
                c.put(x + 1, top + r, f" {text}"[:cw - 2].ljust(cw - 2), fg, bg, bold=chosen and r == 1)
                c.put(x + cw - 1, top + r, v, edge, PANEL, bold=chosen)
            c.put(x, top + 3, corners[2] + h_ * (cw - 2) + corners[3], edge, PANEL, bold=chosen)
            if boss:
                c.put(x + 2, top, " BOSS ", 231, 124, bold=True)
            c.put(x + cw - 4, top, f" {sym} ", 16 if color != 244 else 252, color, bold=True)
        if sel > 0:
            c.put(0, top + 1, "◀", HERO, PANEL, bold=True)
        if sel < self.n - 1:
            c.put(self.w - 1, top + 1, "▶", HERO, PANEL, bold=True)

    def draw_camp(self, c, sel):
        """The drills along the bottom, scrolled to keep the chosen one in view. Returns where you'd stand."""
        y, room = self.h - 2, self.w - 14
        total = self.chips[-1][0] + len(self.chips[-1][1]) + 2
        focus = self.chips[sel][0] if sel is not None else 0
        shift = 0 if total <= room else max(0, min(focus - room // 2, total - room))
        c.put(0, y, " " * self.w, TEXT, 236)
        c.put(1, y, "TRAINING", 223, 236, bold=True)
        for i, (x, label, value, style) in enumerate(self.chips):
            x = 12 + x - shift
            if 11 <= x and x + len(label) + 2 <= self.w - 1:
                c.put(x, y, f" {label} ", *style, bold=True)
                if i == sel:
                    c.put(x + len(label) + 2, y, "◀", HERO, 236, bold=True)
        if shift:
            c.put(10, y, "◀", 231, 236)
        if total - shift > room:
            c.put(self.w - 1, y, "▶", 231, 236)
        return (12 + self.chips[sel][0] - shift - 1, y) if sel is not None else None

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
        green = 34 if frame % 2 == 0 else 40  # the button breathes
        bx, bw = x0 + 2, self.panel_w - 4
        c.put(bx, bottom - 4, "▄" * bw, green, PANEL)
        c.put(bx, bottom - 3, f"▶ {button}   Enter".center(bw), 231, green, bold=True)
        c.put(bx, bottom - 2, "▀" * bw, green, PANEL)

    def step(self, at, key):
        n, last = self.n, len(self.items) - 1
        if key in ("l", "right", "w"):
            return min(n - 1 if at < n else last, at + 1)
        if key in ("h", "left", "b"):
            return max(0 if at < n else n, at - 1)
        if key in ("g", "0"):
            return 0 if at < n else n
        if key in ("G", "$"):
            return n - 1 if at < n else last
        if key in ("j", "down"):
            return self.last_chip if at < n else at
        if key in ("k", "up"):
            if at >= n:
                self.last_chip = at
                return self.last_level
            return at
        return None


def project_board(course, w, h):
    number = int(course.project_dir.name[:2])
    theme, rng, progress = THEMES[number % len(THEMES)], random.Random(number), course._progress()
    levels, n = course.exercises, len(course.exercises)
    panel_w = max(26, min(36, w // 3))
    map_top, map_bottom, map_w = 5, h - 3, w - panel_w
    if w < 72 or map_bottom - map_top < 9:
        return None
    pts = serpentine(n, 4, map_top + 2, map_w - 10, map_bottom - map_top - 4, 8, 4)
    if pts:
        pts = [(x + rng.randint(-2, 2), y + rng.choice((-1, 0, 0, 1))) for x, y in pts]  # not quite a grid
    else:  # a small screen: rows closer together, so no room to wobble up and down
        pts = serpentine(n, 4, map_top + 2, map_w - 10, map_bottom - map_top - 3, 7, 3)
        if not pts:
            return None
        pts = [(x + rng.randint(-1, 1), y) for x, y in pts]
    states = [status(course, ex, progress) for ex in levels]

    land = blob(map_w / 2, (map_top + map_bottom) / 2, map_w / 2 - 2, (map_bottom - map_top) / 2 - 0.6, rng)
    for x, y in pts:  # every level on dry land, with room for you above it and its number beside it
        land |= {(x + dx, y + dy) for dx in range(-2, 5) for dy in (-1, 0, 1)}
    land = {(x, y) for x, y in land if 0 <= x < map_w and map_top <= y < map_bottom}
    trails, reserved = {}, set()
    for i in range(n - 1):
        trails[i] = line(pts[i], pts[i + 1])
        reserved |= set(trails[i])
    for x, y in pts:
        reserved |= {(x + dx, y) for dx in range(0, 4)} | {(x + dx, y - 1) for dx in (-1, 0, 1)}

    def details(value):
        if value == "practice":
            return ("PRACTICE", "Random drills", [f"from 00 to {course.project_dir.name[:2]}"],
                    "Drills from this world and every one before it, picked at random, as many as you like. The "
                    "ones you've missed or solved over par come up more often, and so do the ones you haven't "
                    "played for a while.", "PRACTICE")
        if isinstance(value, trainer.Command):
            drill_states = [status(course, ex, progress) for ex in value.drills]
            ex = course._first_open(value.drills)
            solved = sum(s in ("par", "solved") for s in drill_states)
            marks = [MARK[s] for s in drill_states]
            return (f"TRAINING · {' '.join(value.keys.split())}", value.name,
                    [f"{solved}/{len(value.drills)} solved", f"{drill_states.count('par')} at par", marks[:10], marks[10:]],
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
    drill_states = [status(course, ex, progress) for ex in course.drills()]
    right = f"★ {states.count('par')}/{n} at par" + (
        f"   » drills {sum(s in ('par', 'solved') for s in drill_states)}/{len(drill_states)}" if drill_states else "")
    board = Stage(w, h, (left, right), "h l choose  j k levels / training  Enter play  r lesson  p practice  "
                  "t stats  q back", None)
    board.n, board.panel_w, board.map_top, board.map_bottom, board.details = n, panel_w, map_top, map_bottom, details
    board.paint(land, map_top, map_bottom, lambda x, y: theme, theme, rng, reserved)
    for y in (0, map_top - 1, *range(1, map_top - 1), h - 1):  # the bars and the strip behind the cards
        board.pic.put(0, y, " " * w, TEXT, PANEL)
    board.pic.put(w - len(right) - 1, 0, right, TEXT, PANEL)
    board.pic.put(1, 0, left[:max(0, w - len(right) - 4)], 220, PANEL, bold=True)
    board.pic.put(2, h - 1, board.keys[:w - 3], FAINT, PANEL)
    for i, cells in trails.items():  # walked routes are solid dots, the rest every other dot
        done = states[i] in ("par", "solved")
        for k, (x, y) in enumerate(cells):
            if done or k % 2 == 0:
                board.pic.put(x, y, "·", theme["trail"], bold=done)
    board.cards = []
    for (x, y), ex, st in zip(pts, levels, states):
        sym, _, color = badge(course, ex, progress)
        board.pic.put(x, y, "◆" if ex.boss else "●", color if st != "new" else 252, bold=True)
        board.pic.put(x + 1, y, f"{ex.number}", 255, 236)
        e = course._entry(ex, progress)
        detail = (f"best {e['best']} · par {ex.par}" if e.get("best") is not None else f"par {ex.par}")
        board.cards.append((f"{ex.number}. {ex.title.removeprefix('Review · ')}", detail, (sym, color), ex.boss))
        board.items.append((ex, (x, y - 1), (x, y), None))
    board.card_w = max(20, min(30, (w - 8) // 4))
    board.chips, x = [], 0
    for label, value in [(" ".join(c.keys.split()), c) for c in course.drill_commands()] + [("∞ practice", "practice")]:
        st = "practice" if value == "practice" else group_status([status(course, ex, progress) for ex in value.drills])
        board.chips.append((x, label, value, CAMP[st]))
        board.items.append((value, None, None, None))
        x += len(label) + 4
    board.last_level, board.last_chip = 0, n
    board.trails = trails
    return board


def project_map(course, spot):
    """Walk around one project, starting on spot (an exercise, a drill command, or "practice")."""
    board = project_board(course, *size())
    if board is None:
        return None
    at = next((i for i, item in enumerate(board.items) if item[0] is spot), 0)
    if at >= board.n:
        board.last_chip = at
    key, at = run(board, at)
    return key, board.items[at][0]
