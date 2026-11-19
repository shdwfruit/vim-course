"""The whole course from one place:  python3 play.py

The course as a map of islands, one per project. Walk to one and go in: its trail runs through its exercises,
and its training camp holds the drills. Pick one and play: the same menu as check.py runs it, and q there
brings you back. Progress and stats are the ones check.py keeps. On a small terminal the map becomes a list.

    h l (or ← →) walk    j k (or ↑ ↓) up and down    g G first / last    Enter go in / play
    r read the project's lesson    p practice    t your stats    q back (on the course map: quit)
"""
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

COURSE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(COURSE_DIR / "common"))
import mapview  # noqa: E402
import trainer  # noqa: E402
from mapview import read_key, size  # noqa: E402
from trainer import bold, cyan, dim, yellow  # noqa: E402

# What a key does, on the full-screen maps (where h and l walk) and on the lists (where they open and go back)
MAP_KEYS = {"enter": "open", "q": "back", "esc": "back", "backspace": "back", "p": "practice", "r": "lesson",
            "t": "stats"}
LIST_KEYS = dict(MAP_KEYS, l="open", right="open", h="back", left="back")


def out(s):
    sys.stdout.write(s)
    sys.stdout.flush()


def screen_on():
    """The alternate screen, like Neovim's: no cursor, and long lines cut at the edge instead of wrapping."""
    out("\033[?1049h\033[?25l\033[?7l")


def screen_off():
    out("\033[?7h\033[?25h\033[?1049l")


def choose(header, rows, at, footer):
    """Draw header, rows with a cursor on row `at`, and footer(value of that row); j k / ↑ ↓ move, g G jump.
    rows are (text, value) pairs, value None for a heading. Returns (key, value, at) for any other key."""
    picks = [i for i, (_, value) in enumerate(rows) if value is not None]
    at = at if at in picks else picks[0]
    while True:
        foot = footer(rows[at][1])
        room = max(3, shutil.get_terminal_size((100, 30)).lines - len(header) - len(foot))
        top = min(max(0, at - room // 2), max(0, len(rows) - room))
        body = [(cyan("  ▸ ") if i == at else "    ") + text for i, (text, _) in enumerate(rows)]
        if len(rows) > room:
            foot = [dim(f"    ({top + 1}-{min(len(rows), top + room)} of {len(rows)} lines)")] + foot[1:]
        out("\033[H\033[2J" + "\n".join(header + body[top:top + room] + foot))
        shown = size()
        key, i = read_key(0.5), picks.index(at)
        if key is None:
            if size() != shown:
                return "resize", rows[at][1], at  # maybe big enough for the map now
            continue
        if key in ("up", "k", "down", "j", "g", "G"):
            at = {"up": picks[max(0, i - 1)], "k": picks[max(0, i - 1)], "g": picks[0], "G": picks[-1],
                  "down": picks[min(len(picks) - 1, i + 1)], "j": picks[min(len(picks) - 1, i + 1)]}[key]
        elif key:
            return key, rows[at][1], at


def short(course):
    """ "Project 02 · Text objects: act on the thing you're in" -> "Text objects" """
    return course.title.split(" · ", 1)[-1].split(": ")[0]


def counts(course, progress):
    """(exercises solved, at par, drills solved)"""
    entries = [course._entry(ex, progress) for ex in course.exercises]
    solved = sum(1 for e in entries if e.get("solved"))
    at_par = sum(1 for e, ex in zip(entries, course.exercises) if e.get("solved") and e["best"] <= ex.par)
    drills = sum(1 for ex in course.drills() if course._entry(ex, progress).get("solved"))
    return solved, at_par, drills


def lines_of(s, n, indent="  "):
    """The first n wrapped lines of s, … if there's more."""
    width = max(30, shutil.get_terminal_size((100, 30)).columns - len(indent) - 2)
    lines = textwrap.wrap(" ".join(s.split()), width)
    return [indent + ln for ln in lines[:n - 1]] + ([indent + lines[n - 1] + ("…" if len(lines) > n else "")]
                                                    if len(lines) >= n else [])


# ---------- the map ----------

def map_screen(worlds, at):
    tw, bw = max(len(short(c)) for c in worlds), max(len(c.exercises) for c in worlds)
    rows, done, total, drills_done, drills_total = [], 0, 0, 0, 0
    for c in worlds:
        progress = c._progress()
        solved, at_par, drilled = counts(c, progress)
        drills = len(c.drills())
        complete = at_par == len(c.exercises) and drilled == drills
        marks = "".join(c._mark(ex, progress) for ex in c.exercises) + " " * (bw - len(c.exercises))
        flag = yellow("⚑") if complete else " "
        text = f"{c.project_dir.name[:2]} {flag} {short(c).ljust(tw)}  {marks}  {solved:>2}/{len(c.exercises):<2}"
        rows.append((text + (dim(f"  drills {drilled:>3}/{drills}") if drills else ""), c))
        done, total, drills_done, drills_total = done + solved, total + len(c.exercises), \
            drills_done + drilled, drills_total + drills
    header = [bold("  Neovim course") + dim(f"   {done}/{total} exercises · {drills_done:,}/{drills_total:,} drills"),
              dim("  ★ at par  ✓ solved  ✗ tried  ○ not yet  A-F boss grade  ⚑ all of it at par"), ""]

    def footer(c):
        ex = c._first_open(c.exercises)
        e = c._entry(ex)
        nxt = (f"next: {ex.number}. {ex.title}" if not e.get("solved") else
               f"next: get {ex.number}. {ex.title} to par" if e["best"] > ex.par else "every exercise at par")
        return ["", *lines_of(c.title.split(" · ", 1)[-1], 1), "  " + nxt, "",
                dim("  j k move   Enter open   r lesson   p practice   t stats   q quit")]
    return choose(header, rows, at, footer)


# ---------- a project ----------

def world_rows(course):
    progress, rows = course._progress(), [(bold("Exercises"), None)]
    width = max(len(ex.title) for ex in course.exercises)
    for ex in course.exercises:
        best = course._entry(ex, progress).get("best")
        detail = f"best {best} · par {ex.par}" if best is not None else f"par {ex.par}"
        rows.append((f"{course._mark(ex, progress)} {ex.number:>2}. {ex.title.ljust(width)}   {dim(detail)}", ex))
    cmds = course.drill_commands()
    if cmds:
        rows += [("", None), (bold("Drills") + dim("   one command at a time"), None)]
        kw, mw = max(len(c.keys) for c in cmds), max(len(c.drills) for c in cmds)
        for c in cmds:
            marks = "".join(course._mark(ex, progress) for ex in c.drills) + " " * (mw - len(c.drills))
            solved = sum(1 for ex in c.drills if course._entry(ex, progress).get("solved"))
            rows.append((f"{cyan(c.keys.ljust(kw))}   {marks}  {solved:>2}/{len(c.drills):<2}  {dim(c.name)}", c))
    rows += [("", None), (bold("Practice") + dim("   random drills from this project and every one before it"),
                          "practice")]
    return rows


def list_project(course, spot):
    """The project as a list, for small terminals: (key, value of the row picked)."""
    rows = world_rows(course)
    at = next((i for i, (_, v) in enumerate(rows) if v is spot), 1)
    progress = course._progress()
    solved, at_par, drilled = counts(course, progress)
    drills = len(course.drills())
    header = [bold(f"  {course.project_dir.name[:2]} · {course.title.split(' · ', 1)[-1]}"),
              dim(f"  {solved}/{len(course.exercises)} exercises solved · {at_par} at par"
                  + (f" · {drilled}/{drills} drills" if drills else "")), ""]

    def footer(value):
        if value == "practice":
            about = "Drills picked at random, as many as you like. The ones you've missed or solved over " \
                    "par come up more often, and so do ones you haven't played for a while."
        elif isinstance(value, trainer.Command):
            ex = course._first_open(value.drills)
            about = f"{value.keys}: {value.name}. Enter plays drill {ex.number}, " \
                    f"the first one you haven't solved (or got to par)."
        else:
            about = value.task
        return ["", *lines_of(about, 2), "",
                dim("  j k move   Enter play   r lesson   p practice   t stats   h back to the map")]
    key, value, _ = choose(header, rows, at, footer)
    return key, value


def ask(full, small):
    """An action and what it's for, from the full-screen map if it fits, else from the list."""
    while True:
        got = full()
        key, value = got if got else small()
        action = (MAP_KEYS if got else LIST_KEYS).get(key)
        if action:
            return action, value


def world_screen(course, spots):
    """Play the exercises and drills of one project. Returns the project to show on the map: where the
    last game ended, since → in the game menu walks on into the next project. spots holds where you were
    standing in each project (an exercise, a drill's command, or "practice")."""
    while True:
        spot = spots.get(course) or course._first_open(course.exercises)
        spot = spot.command or spot if isinstance(spot, trainer.Exercise) else spot
        action, value = ask(lambda: mapview.project_map(course, spot), lambda: list_project(course, spot))
        spots[course] = value
        if action == "back":
            return course
        if action == "stats":
            stats()
        elif action == "lesson":
            lesson(course)
        elif action == "practice" or action == "open" and value == "practice":
            game(course.practice)
        elif action == "open":
            ended = game(course.play, value if isinstance(value, trainer.Exercise) else course._first_open(value.drills))
            if ended:
                course, spots[ended[0]] = ended  # maybe another project: → in the game walks on into it


def game(run, *args):
    """Leave the map for check.py's own screens (and Neovim), and come back when q is pressed there."""
    screen_off()
    out("\033[H\033[2J")
    try:
        return run(*args)
    except (KeyboardInterrupt, EOFError):
        print()
        return None
    finally:
        screen_on()


def stats():
    screen_off()
    out("\033[H\033[2J")
    subprocess.run([sys.executable, str(COURSE_DIR / "stats.py")])
    out(dim("\n  Any key for the map "))
    read_key()
    screen_on()


def lesson(course):
    """The project's README, read-only in Neovim (your own config). q closes it."""
    screen_off()
    subprocess.run(["nvim", "-M", "-c", "nnoremap <buffer> q <cmd>quit<CR>", str(course.project_dir / "README.md")])
    screen_on()


def last_played(worlds):
    """(project, exercise or drill) you finished most recently, from the times progress keeps."""
    latest, found = 0, None
    for c in worlds:
        progress = c._progress()
        for ex in c.exercises + c.drills():
            t = c._entry(ex, progress).get("last", 0)
            if t > latest:
                latest, found = t, (c, ex)
    return found


def main():
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        sys.exit("play.py needs a terminal: run it as  python3 play.py")
    trainer.LAUNCHED = True
    dirs = sorted(p.parent for p in COURSE_DIR.glob("[0-9][0-9]_*/check.py"))
    worlds = [c for c in map(trainer._course_for, dirs) if c]
    course, spot = last_played(worlds) or (worlds[0], None)
    spots = {course: spot} if spot else {}
    screen_on()
    try:
        while True:
            at = worlds.index(course)
            action, course = ask(lambda: mapview.course_map(worlds, at), lambda: map_screen(worlds, at)[:2])
            if action == "back":
                break
            if action == "stats":
                stats()
            elif action == "practice":
                game(course.practice)
            elif action == "lesson":
                lesson(course)
            elif action == "open":
                course = world_screen(course, spots)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        screen_off()
    print(dim("Back in with:  ") + "cd " + str(COURSE_DIR).replace(str(Path.home()), "~") + " && python3 play.py")


if __name__ == "__main__":
    main()
