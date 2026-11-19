"""
Runs the exercises and drills. Shared by every project's check.py. You never need to edit (or read) this.

From inside a project folder:
    python3 check.py              your progress in this project, and what's next
    python3 check.py 3            play exercise 3 (or "next" for the first one you haven't solved)
    python3 check.py -k quote     only list exercises whose name contains "quote"
    python3 check.py --show 3     reveal the reference solution for exercise 3, explained (spoilers!)
    python3 check.py --watch 3    watch the reference solution being typed, slowly (spoilers!)
    python3 check.py --solution   replay every reference solution to check the project works

    python3 check.py drill        the drills: short problems that practice one command at a time
    python3 check.py drill f      play the drills for f, starting with the first one you haven't solved
    python3 check.py drill f 4    play drill 4 for f (python3 check.py drill 3 is the 3rd command listed)
    python3 check.py drill f --show 4     reveal its solution (--watch 4 watches it typed)
    python3 check.py drill --solution     replay every drill's reference solution

    python3 check.py explain f    what a command does, from anywhere in the course
    python3 check.py explain      every command the course teaches, one line each

Before Neovim opens and after each try there's a menu, one key each: Enter (start, or the next one after a
solve), → / ← (next / previous, on across projects), ↑ / ↓ (previous / next project, or command for drills),
a number + Enter (go to it), l (list), r (retry), s (the course's solution), w (watch it typed), q (quit,
printing the command that brings you back). Inside Neovim, F7 / F9 leave for the previous / next one and F8
for the menu, without grading.

    python3 check.py practice     endless mixed drills from this project and every one before it

From the course folder, python3 progress.py shows your progress in every project, and python3 play.py
runs the whole course from one screen (it plays each exercise through the same menu).
"""
import argparse
import importlib.util
import json
import os
import random
import re
import runpy
import select
import shutil
import socket
import subprocess
import sys
import tempfile
import termios
import textwrap
import time
import tty
from pathlib import Path

COURSE_DIR = Path(__file__).resolve().parent.parent
COMMON = COURSE_DIR / "common"

_COLOR = sys.stdout.isatty()


def _style(code, text):
    return f"\033[{code}m{text}\033[0m" if _COLOR else text


def green(t): return _style("32", t)
def red(t): return _style("31", t)
def yellow(t): return _style("33", t)
def cyan(t): return _style("36", t)
def dim(t): return _style("2", t)
def bold(t): return _style("1", t)


COLLECTED = []  # filled instead of running when progress.py loads every project


def text(s):
    """Dedent a triple-quoted block and drop its first and last newline. Used to write exercises."""
    return textwrap.dedent(s).strip("\n")


def _columns():
    """The terminal's width (Neovim runs in the same terminal, so this sizes the F1 notes too)."""
    return shutil.get_terminal_size((100, 40)).columns


def _wrap(s, indent="  "):
    """Wrap each line of s as its own paragraph. A line starting with "• " gets a hanging indent."""
    out = []
    width = max(40, min(96, _columns() - 2))
    for para in s.split("\n"):
        rest = indent + "  " if para.startswith("• ") else indent
        out.append(textwrap.fill(para, width=width, initial_indent=indent, subsequent_indent=rest) if para else "")
    return "\n".join(out)


def _print_keys(label, keys, note=""):
    """'  your keys:     ' and the keys, wrapped under themselves when they're long."""
    pad = 2 + len(label)
    width = max(30, min(110, _columns() - 2) - pad)
    if len(keys) > 12 * width:
        keys = keys[:6 * width] + " … " + keys[-6 * width:]
    chunks = [keys[i:i + width] for i in range(0, len(keys), width)] or [""]
    if note and len(chunks[-1]) + len(note) > width:
        chunks.append("")
    chunks[-1] += note
    print(dim("  " + label) + chunks[0])
    for chunk in chunks[1:]:
        print(" " * pad + chunk)


_ARROWS = {b"[A": "up", b"OA": "up", b"[B": "down", b"OB": "down",
           b"[C": "right", b"OC": "right", b"[D": "left", b"OD": "left"}


def _read_key(fd):
    """One keypress from a terminal in cbreak mode: a character, or "enter", "backspace", "esc", "up",
    "down", "left" or "right". Ctrl-C raises KeyboardInterrupt and Ctrl-D EOFError, like input()."""
    ch = os.read(fd, 1)
    if ch == b"\x1b":  # Esc on its own, or the start of an arrow key's escape sequence
        seq = b""
        while len(seq) < 8 and select.select([fd], [], [], 0.03)[0]:
            seq += os.read(fd, 1)
            if len(seq) >= 2 and (seq[-1:].isalpha() or seq.endswith(b"~")):
                break
        return _ARROWS.get(seq, "esc" if not seq else "")
    if ch in (b"\r", b"\n"):
        return "enter"
    if ch in (b"\x7f", b"\x08"):
        return "backspace"
    if ch == b"\x03":
        raise KeyboardInterrupt
    if ch in (b"\x04", b""):
        raise EOFError
    return ch.decode(errors="replace")


def _ask_key(prompt):
    """Show prompt and return the key pressed, as _read_key names it, without waiting for Enter. Digits
    make a number, returned as an int when Enter confirms it. Without a terminal, reads a line instead."""
    if not sys.stdin.isatty():
        answer = input(prompt).strip()
        if answer.isdigit():
            return int(answer)
        return {"": "enter", "[": "up", "]": "down"}.get(answer, answer.lower()[:1])
    print(prompt, end="", flush=True)
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    tty.setcbreak(fd, termios.TCSANOW)  # keys arrive one at a time, unechoed; TCSANOW keeps any typed ahead
    try:
        number = ""
        while True:
            key = _read_key(fd)
            if len(key) == 1 and key.isdigit():
                number += key
                print(key, end="", flush=True)
                continue
            if number:
                if key == "enter":
                    print()
                    return int(number)
                erase = 1 if key == "backspace" else len(number)  # anything else drops the number
                number = number[:-erase]
                print("\b \b" * erase, end="", flush=True)
                continue
            if key in ("", "esc", "backspace"):
                continue
            print()
            return key
    finally:
        termios.tcsetattr(fd, termios.TCSANOW, old)


_SPECIAL = (r"(?:[CSMAD]-)*(?:Esc|CR|Enter|Return|Tab|BS|Space|lt|Bar|Bslash|Del|Up|Down|Left|Right|Home|End"
            r"|PageUp|PageDown|Insert|NL|Nul|F\d\d?)|(?:[CSMAD]-)+[^\s>]")
_KEY_RE = re.compile(r"<(?:" + _SPECIAL + r")>|.", re.IGNORECASE)


def split_keys(keys):
    """'ci"x<Esc>' -> ['c', 'i', '"', 'x', '<Esc>']. A literal '<' becomes '<lt>'."""
    return ["<lt>" if k == "<" else k for k in _KEY_RE.findall(keys)]


def pretty(keys):
    """Keys for people to read: <lt> is just the < key."""
    return keys.replace("<lt>", "<")


def _pack(obj):
    """Just enough MessagePack to send RPC notifications to Neovim: small ints, strings, lists."""
    if isinstance(obj, int):
        return bytes([obj]) if 0 <= obj < 128 else b"\xce" + obj.to_bytes(4, "big")
    if isinstance(obj, str):
        data = obj.encode()
        n = len(data)
        head = bytes([0xa0 | n]) if n < 32 else b"\xd9" + bytes([n]) if n < 256 else b"\xda" + n.to_bytes(2, "big")
        return head + data
    if isinstance(obj, list):
        return (bytes([0x90 | len(obj)]) if len(obj) < 16 else b"\xdc" + len(obj).to_bytes(2, "big")) + b"".join(map(_pack, obj))
    raise TypeError(obj)


class _Typist:
    """Types keys into a running Neovim through its RPC socket, the same way a terminal UI does."""

    def __init__(self, path, proc):
        deadline = time.time() + 10
        while True:
            try:
                self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                self.sock.connect(path)
                return
            except OSError:
                self.sock.close()
                if time.time() > deadline or proc.poll() is not None:
                    raise RuntimeError("couldn't connect to Neovim")
                time.sleep(0.02)

    def input(self, keys):
        self.sock.sendall(_pack([2, "nvim_input", [keys]]))

    def type(self, keys, delay):
        for k in split_keys(keys):
            self.input(k)
            time.sleep(delay * (4 if k == "<CR>" else 1))

    def close(self):
        self.sock.close()


class Exercise:
    def __init__(self, name, title, task, par, start=None, target=None, ext="txt", cursor=(1, 1),
                 hint=None, setup=(), exact=False, files=None, open=None, uses=(), steps=()):
        self.name, self.title, self.task, self.par = name, title, task, par
        self.steps = list(steps)  # for long exercises: the edits, one per item (printed, and in F1)
        self.cursor, self.hint, self.setup, self.exact = tuple(cursor), hint, list(setup), exact
        self.uses = list(uses)  # ids of the commands it practices, explained before it starts
        if files is None:
            files = {f"{name}.{ext}": (start, target)}
        self.files = {fname: (s.split("\n"), t.split("\n")) for fname, (s, t) in files.items()}
        self.open = open or next(iter(self.files))
        self.multi = len(self.files) > 1
        self.command = None  # for a drill: the Command it belongs to
        self.number = None  # exercise number, or the drill's number within its command
        self.workname = name


def _norm(lines, exact):
    lines = list(lines) if exact else [ln.rstrip() for ln in lines]
    while lines and lines[-1] == "":
        lines.pop()
    return lines


# ---------- commands and drills ----------
# Each project's drills.py describes the commands it teaches (what they do, with examples) and gives the
# common ones 20 drills and the rarer, more complex ones 6. Every exercise and drill lists the commands it
# uses, and their descriptions are shown before it starts (and inside Neovim with F1).

DRILL_SIZES = {"common": 20, "complex": 6}
_ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9-]*$")


class Command:
    """One command (or a small family of related keys) the course teaches."""

    def __init__(self, id, keys, name, about, examples=(), level="common"):
        if not _ID_RE.match(id):
            raise ValueError(f"command id {id!r}: use letters, digits and dashes only")
        if level not in (None, *DRILL_SIZES):
            raise ValueError(f"command {id!r}: level must be 'common', 'complex' or None")
        self.id, self.keys, self.name, self.about = id, keys, name, " ".join(about.split())
        self.examples, self.level = list(examples), level
        self.drills = []
        self.project = None

    def add(self, **kwargs):
        """Add a drill. Takes the same arguments as course.add(...), minus name (drills are numbered)."""
        n = len(self.drills) + 1
        ex = Exercise(name=f"{self.id}-{n}", **kwargs)
        if self.id not in ex.uses:
            ex.uses.insert(0, self.id)
        ex.command, ex.number, ex.workname = self, n, f"drill-{self.id}-{n}"
        self.drills.append(ex)
        return ex

    def label(self, ex):
        return f"{self.keys} · drill {ex.number}/{len(self.drills)}"

    def rundown(self, full=True, width=88):
        """(heading, body lines) in plain text."""
        head = f"{self.keys}   {self.name}"
        if not full:
            return head, []
        body = textwrap.wrap(self.about, width)
        line = ""
        for keys, meaning in self.examples:
            item = f"{keys}  {meaning}"
            if line and len(line) + 5 + len(item) > width:
                body.append(line)
                line = item
            else:
                line = f"{line}     {item}" if line else item
        if line:
            body.append(line)
        return head, body


class Drills:
    """The commands a project teaches, made at the top of its drills.py:  drills = Drills(__file__)"""

    def __init__(self, drills_file):
        self.project_dir = Path(drills_file).resolve().parent
        self.commands = []

    def command(self, id, keys, name, about, examples=(), level="common"):
        """Describe a command. level "common" gets 20 drills, "complex" 6, None none (glossary only)."""
        cmd = Command(id, keys, name, about, examples, level)
        cmd.project = self.project_dir.name
        self.commands.append(cmd)
        return cmd


_PROJECT_COMMANDS = {}
_GLOSSARY = None


def _project_commands(project_dir, strict=True):
    """The commands (with their drills) from a project's drills*.py files, in order."""
    project_dir = Path(project_dir).resolve()
    if project_dir not in _PROJECT_COMMANDS:
        commands = []
        for path in sorted(project_dir.glob("drills*.py")):
            try:
                spec = importlib.util.spec_from_file_location(f"vimcourse_{project_dir.name}_{path.stem}", path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
            except Exception as e:
                if strict:
                    raise
                print(dim(f"(couldn't read {project_dir.name}/{path.name}: {e})"), file=sys.stderr)
                continue
            for value in vars(module).values():
                if isinstance(value, Drills):
                    commands += value.commands
        _PROJECT_COMMANDS[project_dir] = commands
    return _PROJECT_COMMANDS[project_dir]


def glossary():
    """Every command in the course, by id."""
    global _GLOSSARY
    if _GLOSSARY is None:
        _GLOSSARY, seen = {}, {}
        for project in sorted(COURSE_DIR.glob("[0-9][0-9]_*/")):
            for cmd in _project_commands(project, strict=False):
                other = seen.get(cmd.id.lower())
                if other:
                    print(red(f"command {cmd.id!r} is described twice: in {other.project} and {cmd.project}"),
                          file=sys.stderr)
                    continue
                seen[cmd.id.lower()] = _GLOSSARY[cmd.id] = cmd
    return _GLOSSARY


def _match_command(which, commands):
    """Commands matching WHICH: by id, else by one of their keys (W, F, ., I), else by id in any case."""
    which = str(which)
    exact = [c for c in commands if c.id == which]
    if exact:
        return exact
    by_key = [c for c in commands if which in {k.split("{")[0] for k in c.keys.split()} | set(c.keys.split())]
    return by_key or [c for c in commands if c.id.lower() == which.lower()]


def _steps_text(ex, width):
    """An exercise's list of edits, numbered, with a hanging indent."""
    lines = []
    for i, step in enumerate(ex.steps, 1):
        lines += textwrap.wrap(step, width, initial_indent=f"{i:>2}. ", subsequent_indent="    ")
    return lines


def _rundown_text(ex):
    """Plain-text notes on the commands an exercise uses, for the F1 window inside Neovim. An exercise
    with a list of edits shows that first."""
    lines = []
    if ex.steps:
        width = max(30, min(88, _columns() - 12))
        lines += [f"The {len(ex.steps)} edits"] + ["  " + ln for ln in _steps_text(ex, width - 2)]
        if ex.uses:
            lines += ["", "Commands that help"]
    first = True
    for cid in ex.uses:
        cmd = glossary().get(cid)
        if not cmd:
            continue
        head, body = cmd.rundown(full=True, width=max(30, min(88, _columns() - 12)))
        lines += ([""] if lines and not (first and ex.steps) else []) + [head] + ["    " + b for b in body]
        first = False
    return lines


_COURSES = {}  # project folder -> its Course, so play can carry on into the next project


def _course_for(project_dir):
    """The Course in another project's check.py, loaded without running it (None if it won't load)."""
    if project_dir not in _COURSES:
        before, collecting = len(COLLECTED), os.environ.get("VIMCOURSE_COLLECT")
        os.environ["VIMCOURSE_COLLECT"] = "1"
        try:
            runpy.run_path(str(project_dir / "check.py"))
        except Exception as e:
            print(dim(f"  (couldn't load {project_dir.name}/check.py: {e})"))
        finally:
            if collecting is None:
                del os.environ["VIMCOURSE_COLLECT"]
        _COURSES[project_dir] = COLLECTED[-1] if len(COLLECTED) > before else None
    return _COURSES[project_dir]


def _neighbor(course, step, drills):
    """The nearest project after (step 1) or before (step -1) this one with exercises (or drills)."""
    dirs = sorted(p.parent for p in COURSE_DIR.glob("[0-9][0-9]_*/check.py"))
    i = dirs.index(course.project_dir) + step
    while 0 <= i < len(dirs):
        other = _course_for(dirs[i])
        if other and other._items(drills):
            return other
        i += step
    return None


class _Practice:
    """Mixed practice: random drills from one project and every project before it. The ones you haven't
    solved, or solved over par, come up more often, and so do the ones you haven't played for a while."""

    def __init__(self, origin):
        dirs = sorted(p.parent for p in COURSE_DIR.glob("[0-9][0-9]_*/check.py"))
        mine = dirs[:dirs.index(origin.project_dir) + 1]
        courses = [origin if d == origin.project_dir else _course_for(d) for d in mine]
        self.origin, self.courses = origin, [c for c in courses if c and c.drills()]
        self.history, self.pos, self.upcoming = [], -1, None  # the (course, drill) pairs played, and where you are

    @staticmethod
    def _weight(course, ex, progress, now):
        e = course._entry(ex, progress)
        if not e.get("attempts"):
            return 6.0  # never tried
        base = 1.0 if e.get("solved") and e["best"] <= ex.par else 3.0 if e.get("solved") else 6.0
        days = (now - e["last"]) / 86400 if "last" in e else 28  # played before progress kept dates
        return base * min(max(days / 7, 0.1), 4)

    def _pick(self):
        now, recent = time.time(), {id(ex) for _, ex in self.history[-15:]}
        here = self.history[self.pos][1].command if self.history else None
        pool, weights = [], []
        for course in self.courses:
            progress = course._progress()
            for ex in course.drills():
                if id(ex) not in recent and ex.command is not here:  # no repeats, and a new command each time
                    pool.append((course, ex))
                    weights.append(self._weight(course, ex, progress, now))
        return random.choices(pool, weights)[0] if pool else None

    def step(self, step):
        """Where → (step 1) or ← (step -1) leads: back and forth through what you've played, then a new pick."""
        if step < 0:
            return self.history[self.pos - 1] if self.pos > 0 else None
        if self.pos + 1 < len(self.history):
            return self.history[self.pos + 1]
        if self.upcoming is None:
            self.upcoming = self._pick()
        return self.upcoming

    def moved(self, to):
        """Play went to `to`, a (course, drill) pair."""
        for i in (self.pos + 1, self.pos - 1):
            if 0 <= i < len(self.history) and self.history[i] == to:
                self.pos = i
                return
        self.history.append(to)
        self.pos, self.upcoming = len(self.history) - 1, None


_PRACTICE = None  # the _Practice in progress, when check.py practice is running
LAUNCHED = False  # set by play.py: q in the menu goes back to its lists, so there's no cd command to print


class Course:
    """A project: a list of exercises added with course.add(...), run with course.run()."""

    def __init__(self, title, check_file, done_message=""):
        self.title = title
        self.done_message = done_message
        self.project_dir = Path(check_file).resolve().parent
        state = os.environ.get("VIMCOURSE_STATE")  # for testing the course: keep .work and progress elsewhere
        home = Path(state) / self.project_dir.name if state else self.project_dir
        self.work = home / ".work"
        self.progress_path = home / ".progress.json"
        self.history_path = home / ".history.jsonl"  # every try, one JSON line each, for stats.py
        self.solutions_path = COURSE_DIR / "solutions" / f"{self.project_dir.name}.py"
        self.exercises = []
        self._shown = set()  # commands whose full description was already printed this session

    def add(self, **kwargs):
        ex = Exercise(**kwargs)
        ex.number = len(self.exercises) + 1
        ex.workname = f"{ex.number:02d}-{ex.name}"
        self.exercises.append(ex)

    # ---------- drills ----------

    def drill_commands(self):
        """This project's commands that have drills, in order."""
        return [c for c in _project_commands(self.project_dir) if c.level]

    def drills(self):
        return [ex for c in self.drill_commands() for ex in c.drills]

    def _find_command(self, which):
        cmds = self.drill_commands()
        if not cmds:
            sys.exit("This project has no drills of its own: the commands it uses are drilled in the earlier projects.")
        if str(which).isdigit() and 1 <= int(which) <= len(cmds):
            return cmds[int(which) - 1]
        found = _match_command(which, cmds)
        if len(found) == 1:
            return found[0]
        if found:
            sys.exit(f"{which!r} could be: " + ", ".join(f"{c.id} ({c.keys})" for c in found))
        owners = [c for c in _match_command(which, glossary().values()) if c.level]
        if owners:
            o = owners[0]
            sys.exit(f"The drills for {o.keys} are in {o.project}:  cd ../{o.project} && python3 check.py drill {o.id}")
        ids = ", ".join(c.id for c in cmds)
        sys.exit(f"No drills for {which!r} here. Use a number (1-{len(cmds)}) or one of: {ids}")

    def _first_open(self, items):
        """The first item not solved yet, else the first not at par, else the first."""
        for ex in items:
            if not self._entry(ex).get("solved"):
                return ex
        for ex in items:
            if self._entry(ex).get("best", 10 ** 9) > ex.par:
                return ex
        return items[0]

    def _find_drill(self, which=None, number=None):
        if which in (None, "next"):
            items = self.drills()
            if not items:
                sys.exit("This project has no drills of its own: the commands it uses are drilled in the earlier projects.")
            return self._first_open(items)
        cmd = self._find_command(which)
        if number is None:
            return self._first_open(cmd.drills)
        if str(number).isdigit() and 1 <= int(number) <= len(cmd.drills):
            return cmd.drills[int(number) - 1]
        sys.exit(f"{cmd.id} has {len(cmd.drills)} drills: use a number from 1 to {len(cmd.drills)}.")

    # ---------- bookkeeping ----------

    def _progress(self):
        try:
            return json.loads(self.progress_path.read_text())
        except (OSError, ValueError):
            return {}

    def _save_progress(self, progress):
        self.progress_path.parent.mkdir(parents=True, exist_ok=True)
        self.progress_path.write_text(json.dumps(progress, indent=2) + "\n")

    def _entry(self, ex, progress=None):
        progress = self._progress() if progress is None else progress
        bucket = progress.get("drills", {}) if ex.command else progress
        return bucket.get(ex.name, {})

    def _solutions(self, drills=False):
        if not drills:
            paths = [self.solutions_path]
        else:
            paths = sorted((COURSE_DIR / "solutions" / "drills").glob(f"{self.project_dir.name}*.py"))
        sols = {}
        for path in paths:
            if not path.exists():
                continue
            spec = importlib.util.spec_from_file_location(f"solutions_{path.stem}", path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            for name, (keys, why) in module.SOLUTIONS.items():
                if not isinstance(keys, str):  # a list of (keys, what they do): join them, list them in why
                    steps = [f"• {pretty(k)}   ({len(split_keys(k))})  {note}" for k, note in keys]
                    keys = "".join(k for k, _ in keys)
                    why = why + "\n\nStep by step (keys in each step):\n" + "\n".join(steps)
                sols[name] = (keys, why)
        return sols

    def _solution(self, ex):
        return self._solutions(drills=bool(ex.command)).get(ex.name)

    def _find(self, which):
        if which == "next":
            return self._first_open(self.exercises)
        if str(which).isdigit() and 1 <= int(which) <= len(self.exercises):
            return self.exercises[int(which) - 1]
        for ex in self.exercises:
            if ex.name == which:
                return ex
        names = ", ".join(f"{i}" for i in range(1, len(self.exercises) + 1))
        sys.exit(f"No exercise called {which!r}. Use a number ({names}) or 'next'.")

    def _label(self, ex):
        return ex.command.label(ex) if ex.command else f"{ex.number}/{len(self.exercises)}"

    # ---------- getting around: next, back, another command or project ----------

    def _items(self, drills):
        return self.drills() if drills else self.exercises

    def _step(self, ex, step):
        """(course, exercise) one place after (step 1) or before (step -1) ex, on into the next or previous
        project at either end. Drills step through drills. None past the very first or last. In practice,
        the next drill is a random pick."""
        if _PRACTICE and ex.command:
            return _PRACTICE.step(step)
        items = self._items(bool(ex.command))
        i = items.index(ex) + step
        if 0 <= i < len(items):
            return self, items[i]
        other = _neighbor(self, step, bool(ex.command))
        return (other, other._items(bool(ex.command))[0 if step > 0 else -1]) if other else None

    def _jump(self, ex, step):
        """(course, exercise): the first one you haven't solved in the next or previous project, or for a
        drill, in the next or previous command. None if there's nothing that way."""
        if ex.command:
            cmds = self.drill_commands()
            i = cmds.index(ex.command) + step
            if 0 <= i < len(cmds):
                return self, self._first_open(cmds[i].drills)
            other = _neighbor(self, step, True)
            return (other, other._first_open(other.drill_commands()[0 if step > 0 else -1].drills)) if other else None
        other = _neighbor(self, step, False)
        return (other, other._first_open(other.exercises)) if other else None

    def _where(self, ex, to):
        """A few words on where `to` (a (course, exercise) pair) is, if that isn't where ex is."""
        course, other = to
        if course is not self:
            return f" ({course.project_dir.name})"
        if ex.command and other.command is not ex.command:
            return f" ({other.command.keys} drills)"
        return ""

    def _list(self, ex):
        """Print every exercise (or, for a drill, every command) with your marks, and ask where to go."""
        progress = self._progress()
        print()
        if ex.command:
            cmds = self.drill_commands()
            kw, mw = max(len(c.keys) for c in cmds), max(len(c.drills) for c in cmds)
            for i, c in enumerate(cmds, 1):
                here = cyan("▸") if c is ex.command else " "
                marks = "".join(self._mark(d, progress) for d in c.drills)
                print(f"  {here}{i:>2}. {c.keys.ljust(kw)}   {marks}" + " " * (mw - len(c.drills)) + dim(f"   {c.name}"))
            question = f"  Which command? (1-{len(cmds)} or its keys, Enter to stay) "
        else:
            width = max(len(e.title) for e in self.exercises)
            for e in self.exercises:
                here = cyan("▸") if e is ex else " "
                best = self._entry(e, progress).get("best")
                detail = f"best {best} · par {e.par}" if best is not None else f"par {e.par}"
                print(f"  {here}{self._mark(e, progress)} {e.number:>2}. {e.title.ljust(width)}   {dim(detail)}")
            question = f"  Which one? (1-{len(self.exercises)}, Enter to stay) "
        print(dim("  ★ at par  ✓ solved  ✗ tried  ○ not yet"))
        try:
            answer = input(question).strip()
        except (KeyboardInterrupt, EOFError):
            print()
            return None
        if not answer:
            return None
        if not ex.command:
            if answer.isdigit() and 1 <= int(answer) <= len(self.exercises):
                return self, self.exercises[int(answer) - 1]
        else:
            found = [cmds[int(answer) - 1]] if answer.isdigit() and 1 <= int(answer) <= len(cmds) \
                else _match_command(answer, cmds)
            if len(found) == 1:
                return self, self._first_open(found[0].drills)
        print(dim(f"  No {answer!r} here."))
        return None

    def _goto(self, ex, choice):
        """Where choice (from _prompt) leads: a (course, exercise) pair, or None (with a note) to stay."""
        if choice in ("next", "prev"):
            to = self._step(ex, 1 if choice == "next" else -1)
            if not to:
                print(dim("  That's the last one in the course." if choice == "next" else "  That's the very first one."))
            return to
        if choice in ("up", "down"):
            to = self._jump(ex, 1 if choice == "down" else -1)
            if not to:
                what = "command" if ex.command else "project"
                print(dim(f"  There's no {'next' if choice == 'down' else 'earlier'} {what}."))
            return to
        if choice == "list":
            return self._list(ex)
        n = choice  # a number: this project's exercise n, or this command's drill n
        items = ex.command.drills if ex.command else self.exercises
        if 1 <= n <= len(items):
            return self, items[n - 1]
        print(dim(f"  Pick a number from 1 to {len(items)}."))
        return None

    def _prompt(self, ex, after):
        """Ask what's next, one key, no Enter needed. after is "intro", "left", "solved" or "unsolved".
        Returns "start", "next", "prev", "up", "down", "list", "solution", "watch", a number, or "quit"."""
        nxt, prev = self._step(ex, 1), self._step(ex, -1)
        enter = "next" if after == "solved" and nxt else "retry" if after in ("solved", "unsolved") else "start"
        n = len(ex.command.drills if ex.command else self.exercises)
        options = [f"[Enter] {enter}" + (self._where(ex, nxt) if enter == "next" else "")]
        if enter == "next":
            options.append("r retry")
        if prev:
            options.append("← back" + self._where(ex, prev))
        if nxt and enter != "next":
            options.append("→ next" + self._where(ex, nxt))
        sol = self._solution(ex)
        options += ["↑↓ other command" if ex.command else "↑↓ other project",
                    f"1-{n}⏎ {'drill' if ex.command else 'exercise'} N", "l list"]
        options += ["s solution", "w watch it"] if sol else []
        options.append("q back" if LAUNCHED else "q quit")
        line = "   ".join(options)
        width = max(40, min(110, _columns() - 4))
        lines = textwrap.wrap(line, width, break_on_hyphens=False) if len(line) > width else [line]
        for part in lines[:-1]:
            print(dim("  " + part))
        keys = {"enter": enter, "r": "start", "right": "next", "n": "next", "left": "prev", "p": "prev",
                "up": "up", "[": "up", "down": "down", "]": "down", "l": "list", "q": "quit"}
        if sol:
            keys.update(s="solution", w="watch")
        while True:
            try:
                key = _ask_key(dim("  " + lines[-1]) + " ")
            except (KeyboardInterrupt, EOFError):
                print()
                return "quit"
            if isinstance(key, int):
                return key
            choice = keys.get(key)
            if choice == "retry":
                return "start"
            if choice:
                return choice

    # ---------- running Neovim ----------

    def _prepare(self, ex):
        """Write fresh copies of the exercise files and return (workdir, files for the session)."""
        workdir = self.work / ex.workname
        if workdir.exists():
            shutil.rmtree(workdir)
        workdir.mkdir(parents=True)
        files = []
        for fname, (start, target) in ex.files.items():
            path = workdir / fname
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join(start) + "\n")
            entry = {"path": str(path), "start": start}
            if not ex.multi:
                entry["target"] = target  # shown in a scratch buffer: no file on disk to :read the answer from
            files.append(entry)
        return workdir, files

    def _nvim(self, ex, mode, keys="", delay=0.005, analyze=None):
        """Run one exercise in Neovim. mode is "play" (you type), "replay" (headless, check.py types
        the reference solution), or "watch" (check.py types it slowly while you watch). analyze (with a
        replay) asks common/coach.lua for shorter ways to do what the keys did."""
        if not shutil.which("nvim"):
            sys.exit("Neovim isn't installed. Install it with:  brew install neovim")
        workdir, files = self._prepare(ex)
        rundir = Path(tempfile.mkdtemp(prefix=".run-", dir=self.work))  # its own, so replays can run side by side
        try:
            return self._run_nvim(ex, mode, keys, delay, workdir, files, rundir, analyze)
        finally:
            shutil.rmtree(rundir, ignore_errors=True)

    def _run_nvim(self, ex, mode, keys, delay, workdir, files, rundir, analyze=None):
        result = rundir / "result.json"
        session = {
            "mode": mode, "title": ex.title, "label": self._label(ex), "par": ex.par,
            "task": ex.task.split("\n") + ([f"F1 lists the {len(ex.steps)} edits (it doesn't count as a key)."] if ex.steps else []),
            "files": files, "open": list(ex.files).index(ex.open) + 1,
            "cursor": list(ex.cursor), "setup": ex.setup, "result": str(result),
            "help": _rundown_text(ex) if mode == "play" else [],
            "help_title": " the edits, and commands that help " if ex.steps else " the commands for this one ",
        }
        if analyze:
            session["analyze"] = analyze
        session_path = rundir / "session.json"
        session_path.write_text(json.dumps(session))
        env = dict(os.environ, VIMCOURSE_SESSION=str(session_path))
        cmd = ["nvim", "-u", str(COMMON / "init.lua"), "-i", "NONE",
               "-c", "luafile " + str(COMMON / "session.lua").replace(" ", r"\ "), str(workdir / ex.open)]
        if mode == "play":
            subprocess.run(cmd, cwd=workdir, env=env)
        else:
            sockdir = tempfile.mkdtemp(prefix="vimcourse-", dir="/tmp")
            sock = os.path.join(sockdir, "nvim.sock")
            cmd[1:1] = ["--listen", sock]
            if mode == "replay":
                cmd.insert(1, "--headless")
                proc = subprocess.Popen(cmd, cwd=workdir, env=env, stdin=subprocess.DEVNULL,
                                        stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            else:
                proc = subprocess.Popen(cmd, cwd=workdir, env=env)
            try:
                typist = _Typist(sock, proc)
                time.sleep(0.05 if mode == "replay" else 1.0)
                try:
                    typist.type(keys, delay)
                    time.sleep(0.1)
                    typist.input("<Cmd>lua VimCourse.finish()<CR>")
                except OSError:
                    if proc.wait(timeout=5) is None:  # the keys themselves quit Neovim (ZZ, :wq): that's fine
                        raise
                typist.close()
                proc.wait(timeout=None if mode == "watch" else 20)
            except (RuntimeError, subprocess.TimeoutExpired, OSError) as e:
                proc.kill()
                proc.wait()
                return None, f"Neovim got stuck ({e}). Is it waiting at a prompt?"
            finally:
                shutil.rmtree(sockdir, ignore_errors=True)
            if mode == "watch":
                return None, None
        if not result.exists():
            return None, "No result was recorded. Did Neovim close unexpectedly?"
        return json.loads(result.read_text()), None

    # ---------- grading ----------

    def _grade(self, ex, result):
        """Return (solved, message lines)."""
        problems = []
        for (fname, (start, target)), got in zip(ex.files.items(), result["files"]):
            want, have = _norm(target, ex.exact), _norm(got, ex.exact)
            if want == have:
                continue
            where = f"{fname}, " if ex.multi else ""
            if have == _norm(start, ex.exact):
                problems.append(f"{where}nothing changed: it's still the starting text.")
                continue
            for i in range(max(len(want), len(have))):
                w = want[i] if i < len(want) else None
                h = have[i] if i < len(have) else None
                if w != h:
                    problems.append(f"{where}line {i + 1} should be:  " + (repr(w) if w is not None else "(no line: the file should end before here)"))
                    problems.append(" " * len(f"{where}line {i + 1} ") + "but it is:  " + (repr(h) if h is not None else "(missing)"))
                    break
        return not problems, problems

    @staticmethod
    def _tips(keys):
        notes = []
        arrows = sum(k in ("<Up>", "<Down>", "<Left>", "<Right>", "<Home>", "<End>", "<PageUp>", "<PageDown>",
                           "<S-Up>", "<S-Down>", "<S-Left>", "<S-Right>", "<C-Left>", "<C-Right>") for k in keys)
        if arrows:
            notes.append(f"You used arrow keys (or Home/End/Page keys) {arrows} times. Every exercise here is "
                         "faster with motions, and your hands stay on the home row.")
        mouse = sum("Mouse" in k for k in keys)
        if mouse:
            notes.append(f"You clicked the mouse {mouse} times. Try a search (/text) or f/t to jump instead.")
        run_key, run_len, best_key, best_len = None, 0, None, 0
        for k in keys:
            run_len = run_len + 1 if k == run_key else 1
            run_key = k
            if run_len > best_len:
                best_key, best_len = k, run_len
        if best_len >= 4:
            n, k = best_len, best_key
            tips = {
                "j": f"`{n}j` does that in 2 keys (relative line numbers show the count), or jump with `/`, `}}` or `G`.",
                "k": f"`{n}k` does that in 2 keys (relative line numbers show the count), or jump with `?`, `{{` or `gg`.",
                "l": "`f{char}` / `t{char}` jump straight to a character on the line, and `w`/`e` move by words.",
                "h": "`F{char}` / `T{char}` jump back to a character on the line, and `b` moves back by words.",
                "w": f"`{n}w` moves {n} words at once, and `f{{char}}` often lands closer still.",
                "b": f"`{n}b` moves back {n} words at once.",
                "e": f"`{n}e` moves {n} word-ends at once.",
                "x": "`dw`, `dt{char}` or a count like `5x` deletes a run of characters in one go.",
                ".": f"`.` is great, but if you're repeating it {n} times, a count, a macro or `:s` may be shorter.",
                "<BS>": "In Insert mode, `Ctrl-w` deletes the word before the cursor and `Ctrl-u` the whole line. "
                        "Better still, use `c` + a motion to replace text in one go.",
            }
            if k in tips:
                notes.append(f"You pressed `{k}` {n} times in a row. " + tips[k])
        return notes

    def _record(self, ex, solved, count):
        progress = self._progress()
        bucket = progress.setdefault("drills", {}) if ex.command else progress
        entry = bucket.setdefault(ex.name, {"solved": False, "best": None, "attempts": 0})
        entry["attempts"] += 1
        entry["last"] = int(time.time())  # for practice: what you haven't played for a while comes up more
        new_best = False
        if solved:
            entry["solved"] = True
            if entry["best"] is None or count < entry["best"]:
                entry["best"], new_best = count, True
        self._save_progress(progress)
        return entry, new_best

    def _mark(self, ex, progress):
        p = self._entry(ex, progress)
        if p.get("solved"):
            return yellow("★") if p.get("best") is not None and p["best"] <= ex.par else green("✓")
        return red("✗") if p.get("attempts") else dim("○")

    def _print_commands(self, ex):
        """Explain the commands an exercise uses. A drill's own command is explained in full the first time;
        everything else in full for exercises, and in one line (F1 has the rest) for drills."""
        cmds = [glossary()[c] for c in ex.uses if c in glossary()]
        if not cmds:
            return
        print()
        if ex.command:
            print(dim("  Commands  (F1 inside Neovim shows what they do)"))
        elif ex.steps:
            print(dim("  Commands that help  (F1 inside Neovim explains each)"))
        else:
            print(dim("  The commands you'll need  (F1 inside Neovim shows this again)"))
        for cmd in cmds:
            full = (not ex.command and not ex.steps) or (cmd is ex.command and cmd.id not in self._shown)
            head, body = cmd.rundown(full=full, width=max(30, min(88, _columns() - 8)))
            keys, _, name = head.partition("   ")
            print("  " + bold(cyan(keys)) + "   " + name)
            for line in body:
                print("      " + line)
            if full:
                self._shown.add(cmd.id)

    # ---------- commands ----------

    def status(self, k=None):
        progress = self._progress()
        print(bold(self.title) + "\n")
        solved = at_par = 0
        width = max(len(ex.title) for ex in self.exercises)
        for i, ex in enumerate(self.exercises, 1):
            if k and k.lower() not in ex.name.lower():
                continue
            p = self._entry(ex, progress)
            if p.get("solved"):
                solved += 1
                best = p.get("best")
                at_par += best is not None and best <= ex.par
                detail = f"best {best} keys · par {ex.par}" + (yellow("  under par!") if best < ex.par else "")
            elif p.get("attempts"):
                detail = f"not solved yet · par {ex.par}"
            else:
                detail = dim(f"par {ex.par}")
            print(f"  {self._mark(ex, progress)} {i:>2}. {ex.title.ljust(width)}   {detail}")
        total = len(self.exercises)
        print()
        print(f"{solved}/{total} solved · {at_par} at par")
        if solved == total and at_par == total:
            print(green(bold("Every exercise solved at par.")) + (" " + self.done_message if self.done_message else ""))
        else:
            ex = self._first_open(self.exercises)
            verb = "Next up" if not self._entry(ex, progress).get("solved") else "Next: get to par on"
            print(f"{verb}: {bold(f'{ex.number}. {ex.title}')}   →  python3 check.py {ex.number}")
        if self.drill_commands() and not k:
            print()
            self.drill_status(short=True)

    def drill_status(self, short=False):
        progress = self._progress()
        cmds = self.drill_commands()
        if not cmds:
            print("This project has no drills of its own: the commands it uses are drilled in the earlier projects.")
            return
        if not short:
            print(bold(self.title) + "\n")
        print(bold("Drills") + dim("   short problems that practice one command each:  python3 check.py drill N"))
        kw = max(len(c.keys) for c in cmds)
        nw = max(len(c.name) for c in cmds)
        mw = max(len(c.drills) for c in cmds)
        done = total = 0
        for i, c in enumerate(cmds, 1):
            marks = "".join(self._mark(ex, progress) for ex in c.drills)
            solved = sum(1 for ex in c.drills if self._entry(ex, progress).get("solved"))
            done, total = done + solved, total + len(c.drills)
            print(f"  {i:>2}. {c.keys.ljust(kw)}   {c.name.ljust(nw)}   {marks}" + " " * (mw - len(c.drills))
                  + dim(f"  {solved}/{len(c.drills)}"))
        print()
        print(f"{done}/{total} drills solved" + dim("   ★ at par  ✓ solved  ✗ tried  ○ not yet"))
        if done < total:
            ex = self._find_drill()
            print(f"Next drill: {bold(ex.command.label(ex))}   →  python3 check.py drill {ex.command.id}")
        print(dim("Mixed drills from this project and every one before it:  python3 check.py practice"))

    def explain(self, which=None):
        g = glossary()
        if which is None:
            print(bold("Every command in the course") + dim("   python3 check.py explain ID shows one in full") + "\n")
            project = None
            kw = min(30, max(len(c.keys) for c in g.values()))
            for cmd in g.values():
                if cmd.project != project:
                    print(("\n" if project else "") + bold(cmd.project))
                    project = cmd.project
                drills = dim(f"  {len(cmd.drills)} drills") if cmd.drills else ""
                print(f"  {cmd.id:<14} {cyan(cmd.keys.ljust(kw))}   {cmd.name}{drills}")
            return
        matches = _match_command(which, g.values()) or [c for c in g.values() if which.lower() in c.name.lower()]
        if not matches:
            sys.exit(f"No command {which!r}. python3 check.py explain lists them all.")
        if len(matches) > 1:
            print(f"{which!r} could be: " + ", ".join(f"{c.id} ({c.keys})" for c in matches))
            return
        cmd = matches[0]
        head, body = cmd.rundown(width=max(30, min(88, _columns() - 8)))
        keys, _, name = head.partition("   ")
        print("\n  " + bold(cyan(keys)) + "   " + name)
        for line in body:
            print("      " + line)
        if cmd.drills:
            here = cmd.project == self.project_dir.name
            where = f"python3 check.py drill {cmd.id}" if here else \
                f"cd ../{cmd.project} && python3 check.py drill {cmd.id}"
            print(dim(f"\n  {len(cmd.drills)} drills:  {where}"))
        print()

    def play(self, ex):
        """Show an exercise (or drill), open Neovim, grade what you did, then go on, back, or anywhere.
        Returns the (course, exercise) you were on when you quit."""
        course, after = self, "intro"
        while True:
            if after == "intro":
                course._intro(ex)
            choice = course._prompt(ex, after)
            if choice == "quit":
                if not LAUNCHED:
                    course._print_resume(ex, after)
                return course, ex
            if choice in ("solution", "watch"):
                course._reveal(ex) if choice == "solution" else course._watch_it(ex)
                after = "left" if after == "intro" else after
                continue
            if choice == "start":
                after = course._attempt(ex)
                if after is None:
                    return course, ex
                if after not in ("prev", "next"):
                    continue
                choice = after  # F7 or F9 in Neovim
                after = "left"
            to = course._goto(ex, choice)
            if to:
                if _PRACTICE:
                    _PRACTICE.moved(to)
                elif to[0] is not course:
                    title = to[0].title
                    print("\n" + bold(cyan(f"━━ {title} " + "━" * max(3, 72 - len(title)))))
                    if not LAUNCHED:  # play.py opens the lesson with r on its world screen
                        print(dim(f"  Its README: {to[0].project_dir.name}/README.md"))
                (course, ex), after = to, "intro"
            elif after == "intro":
                after = "left"  # stayed put: just ask again, without printing it all again

    def _print_resume(self, ex, after):
        """On the way out: the command that brings you back here (to the next one, if you just solved this)."""
        course, here = self, ex
        if _PRACTICE:  # practice picks its drills as it goes, so the way back in is practice itself
            course, what = _PRACTICE.origin, "practice"
        else:
            if after == "solved" and self._step(ex, 1):
                course, here = self._step(ex, 1)
            what = f"drill {here.command.id} {here.number}" if here.command else str(here.number)
        folder = course.project_dir.resolve()
        try:
            folder = "~/" + str(folder.relative_to(Path.home()))
        except ValueError:
            pass
        print(dim("  To pick up where you left off:"))
        print(f"    cd {folder} && python3 check.py {what}\n")

    def _intro(self, ex):
        """The task, its edits, the commands that help, and how the session works."""
        print()
        if _PRACTICE:
            print(dim(f"Practice · drill {_PRACTICE.pos + 1} this session · from {self.project_dir.name}"))
        if ex.command:
            if ex.command.id not in self._shown:
                print(bold(cyan(f"── {ex.command.keys} drills " + "─" * max(0, 60 - len(ex.command.keys)))))
            print(bold(f"{ex.command.label(ex)} · {ex.title}") + dim(f"   (par {ex.par} keys)"))
        else:
            print(bold(f"Exercise {ex.number}/{len(self.exercises)} · {ex.title}") + dim(f"   (par {ex.par} keys)"))
        print(_wrap(ex.task))
        if ex.steps:
            print()
            for line in _steps_text(ex, max(40, min(96, _columns() - 2)) - 2):
                print("  " + line)
        self._print_commands(ex)
        if ex.multi:
            how = (f"This one has {len(ex.files)} files ({', '.join(ex.files)}) and no target window: the task "
                   "above says what to change. Neovim starts in a folder with just these files. Quit when you're "
                   "done (:wqa saves everything).")
        else:
            how = ("Your file opens on the left and the target on the right. Edit until they match, then quit "
                   "any way you like (ZZ saves and quits).")
        print("\n" + dim(_wrap(how + " Only keys up to your last edit count. F5 starts over. F7 and F9 go to "
                                "the previous and next one, and F8 back to this menu, without grading.")))
        print()

    def _attempt(self, ex):
        """Open Neovim on ex, then grade and record what you did. Returns "solved" or "unsolved"; "left"
        if you pressed F8 or quit without changing anything (that isn't a try); "prev" or "next" for F7
        and F9; None if Neovim failed."""
        began = time.time()
        result, error = self._nvim(ex, "play")
        if error:
            print(red("  " + error))
            return None
        print()
        seconds = round(time.time() - began, 1)
        leave = result.get("leave")
        if leave:
            if leave == "menu":
                print(dim("  Left without grading."))
            return {"menu": "left"}.get(leave, leave)
        starts = [_norm(start, ex.exact) for start, _ in ex.files.values()]
        if [_norm(got, ex.exact) for got in result["files"]] == starts:
            print(dim("  You quit without changing anything, so that doesn't count as a try."))
            return "left"
        solved, problems = self._grade(ex, result)
        count, keys = result["count"], result["keys"]
        entry, new_best = self._record(ex, solved, count)
        if solved:
            if count < ex.par:
                print(yellow(bold(f"  ★ Solved in {count} keys. Par is {ex.par}: you beat it!")))
            elif count == ex.par:
                print(yellow(bold(f"  ★ Solved in {count} keys. That's par.")))
            else:
                print(green(bold(f"  ✓ Solved in {count} keys.")) + f" Par is {ex.par}. Can you find the shorter way?")
            if new_best and entry["attempts"] > 1:
                print(green("    New personal best."))
        else:
            print(red(bold("  ✗ Not quite.")))
            for line in problems:
                print("    " + line)
        if keys:
            counted, free = pretty("".join(keys[:count])), pretty("".join(keys[count:]))
            _print_keys("your keys:     ", counted, dim(f"   (then {free}, free)") if free and len(free) < 30 else "")
        if solved and count <= ex.par:
            self._print_reference(ex, keys[:count])
        saved = self._coach(ex, keys[:count], result["files"])
        self._log_try(ex, result, solved, began, seconds, saved)
        notes = self._tips(keys[:count])
        if notes or (ex.hint and (not solved or count > ex.par)):
            print()
        if ex.hint and (not solved or count > ex.par):
            print(_wrap(dim("hint: ") + ex.hint, "  "))
        for note in notes:
            print(_wrap(cyan("tip: ") + note, "  "))
        print()
        return "solved" if solved else "unsolved"

    def _reveal(self, ex):
        """The course's solution and why it works, from the menu (s)."""
        keys, why = self._solution(ex)
        print()
        _print_keys("course's keys: ", pretty(keys), dim(f"   ({len(split_keys(keys))} keys, par {ex.par})"))
        print(dim(_wrap(why, "      ")))
        print()

    def _watch_it(self, ex):
        """Type the course's solution in Neovim while you watch, from the menu (w). Long ones go faster."""
        keys = self._solution(ex)[0]
        print(dim("  Neovim types the course's solution while you watch. ZZ closes it when it's done."))
        self.watch(ex, max(1.0, len(split_keys(keys)) / 60))
        print()

    def practice(self):
        """Random drills from this project and every one before it, until you quit."""
        global _PRACTICE
        _PRACTICE = _Practice(self)
        if not _PRACTICE.courses:
            sys.exit("There are no drills to practice yet.")
        first = _PRACTICE.step(1)
        _PRACTICE.moved(first)
        span = _PRACTICE.courses[0].project_dir.name
        if len(_PRACTICE.courses) > 1:
            span += f" to {_PRACTICE.courses[-1].project_dir.name}"
        print(bold("Practice") + dim(f"   random drills from {span}, as many as you like. The ones you've missed or "
                                     "solved over par come up more often, and so do ones you haven't played for a while."))
        try:
            return first[0].play(first[1])
        finally:
            _PRACTICE = None  # so play.py can go on to ordinary exercises afterwards

    def _coach(self, ex, keys, files):
        """After a try: shorter ways to make the same moves and edits, found by common/coach.lua using only
        the commands taught up to this project. Each is checked by replaying your keys with it."""
        if ex.multi or len(keys) < 2 or any("Mouse" in k for k in keys):
            return 0
        tty = sys.stdout.isatty()
        if tty:
            print(dim("  looking for shorter paths…"), end="\r", flush=True)
        try:
            return self._coach_run(ex, keys, files, tty)
        except Exception:  # the coach is a bonus: never let it get in the way of a try
            return 0
        finally:
            if tty:
                print(" " * 30, end="\r", flush=True)

    def _coach_run(self, ex, keys, files, tty):
        level = int(self.project_dir.name[:2]) if self.project_dir.name[:2].isdigit() else 99
        spent = len(keys)
        keys = list(keys) + ["<Esc>"]  # your free <Esc> at the end: the coach needs Normal mode to work in
        result, error = self._nvim(ex, "replay", keys="".join(keys),
                                   analyze={"coach": str(COMMON / "coach.lua"), "level": level, "budget": 2500})
        found = (result or {}).get("coach")
        if error or not isinstance(found, list) or not found:
            return 0
        # Put every suggestion in your keys and replay them: show the lot only if the text comes out the
        # same. (If it doesn't, the moves alone usually still do.)
        for subset in (found, [f for f in found if f["kind"] == "move"]):
            if not subset:
                continue
            better = list(keys)
            for f in sorted(subset, key=lambda f: -f["from"]):
                better[f["from"] - 1:f["to"] - 1] = split_keys(f["better"])
            check, error = self._nvim(ex, "replay", keys="".join(better))
            if check and not error and [_norm(x, ex.exact) for x in check["files"]] == [_norm(x, ex.exact) for x in files]:
                if tty:
                    print(" " * 30, end="\r")
                self._print_coach(subset, spent, check["count"])
                return spent - check["count"]
        return 0

    @staticmethod
    def _print_coach(found, before, after):
        print("\n" + dim("  shorter ways to make your own moves and edits (same places, same text):"))
        for f in found[:8]:
            yours = pretty(f["yours"])
            better = bold(pretty(f["better"])) if f["better"] else dim("nothing")
            if not f["better"] and not f.get("note"):
                f["note"] = "you end up where you started"
            note = f"saves {f['saves']}" + (f" · {f['note']}" if f.get("note") else "")
            print(f"    line {f['line']:<3} {f['kind']}:  {yours}  →  {better}   " + dim(note))
        if len(found) > 8:
            print(dim(f"    … and {len(found) - 8} more"))
        print(dim(f"    with {'all of these' if len(found) > 1 else 'that'}: {after} keys instead of {before}"))

    def _log_try(self, ex, result, solved, began, seconds, saved):
        """One line in .history.jsonl for stats.py: what you typed (and in which mode), and how it went."""
        entry = {"time": int(began), "seconds": seconds, "name": ex.name, "drill": ex.command.id if ex.command else None,
                 "practice": bool(_PRACTICE), "par": ex.par, "count": result["count"], "solved": solved,
                 "keys": result["keys"], "modes": result.get("modes", []), "coach_saves": saved or 0}
        try:
            self.history_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.history_path, "a") as f:
                f.write(json.dumps(entry) + "\n")
        except OSError:
            pass

    def _print_reference(self, ex, yours):
        """After a solve at or under par: the course's own solution, to compare with yours."""
        sol = self._solution(ex)
        if not sol:
            return
        ref, why = sol

        def norm(tokens):  # Neovim logs a space as <Space> and Ctrl-r as <C-R>
            return [" " if t.lower() == "<space>" else t.lower() if len(t) > 1 else t for t in tokens]

        same = len(yours) == ex.par and norm(yours) == norm(split_keys(ref))[:ex.par]
        if same:
            print(dim("  course's keys: ") + "the same as yours")
        else:
            _print_keys("course's keys: ", pretty(ref), dim(f"   ({ex.par} keys)"))
        print(dim(_wrap(why, "      ")))

    def _confirm_spoiler(self, ex):
        if sys.stdin.isatty() and not self._entry(ex).get("solved"):
            what = f"{ex.command.id} drill {ex.number}" if ex.command else f"exercise {ex.number}"
            try:
                answer = input(f"You haven't solved {what} yet. Show the solution anyway? [y/N] ")
            except (KeyboardInterrupt, EOFError):
                print()
                return False
            return answer.strip().lower() == "y"
        return True

    def show(self, ex):
        sol = self._solution(ex)
        if not sol:
            sys.exit("No reference solution for that one yet.")
        keys, why = sol
        if not self._confirm_spoiler(ex):
            return
        print()
        name = ex.command.label(ex) if ex.command else f"Exercise {ex.number}"
        print(bold(f"{name} · {ex.title}") + dim(f"   (par {ex.par})"))
        print(_wrap(ex.task))
        print()
        print("  " + bold(pretty(keys)) + dim(f"   ({len(split_keys(keys))} keys)"))
        print()
        print(_wrap(why))
        again = f"drill {ex.command.id} --watch {ex.number}" if ex.command else f"--watch {ex.number}"
        print(dim(f"\n  Watch it typed out:  python3 check.py {again}"))

    def watch(self, ex, speed):
        sol = self._solution(ex)
        if not sol:
            sys.exit("No reference solution for that one yet.")
        self._nvim(ex, "watch", keys=sol[0], delay=0.35 / speed)

    def try_keys(self, ex, keys):
        """Replay any keys on an exercise and grade them (for testing a solution without typing it)."""
        result, error = self._nvim(ex, "replay", keys=keys)
        if error:
            sys.exit(red(error))
        solved, problems = self._grade(ex, result)
        count = result["count"]
        verdict = (yellow(f"★ {count} keys, par {ex.par}") if solved and count <= ex.par
                   else green(f"✓ {count} keys, par {ex.par}") if solved else red(f"✗ not solved ({count} keys)"))
        print("  " + verdict)
        for line in problems:
            print("    " + line)
        _print_keys("keys typed:    ", pretty("".join(result["keys"])))
        self._coach(ex, result["keys"][:count], result["files"])

    def _verify(self, items, sols):
        """Replay reference solutions; print one line each. Returns the number of problems."""
        bad = 0
        g = glossary()
        for ex in items:
            label = f"{ex.command.id}-{ex.number}" if ex.command else f"{ex.number:>2}. {ex.name}"
            unknown = [c for c in ex.uses if c not in g]
            if ex.name not in sols:
                bad += 1
                print(f"  {red('?')} {label}: no reference solution")
                continue
            result, error = self._nvim(ex, "replay", keys=sols[ex.name][0])
            if error:
                bad += 1
                print(f"  {red('✗')} {label}: {error}")
                continue
            solved, problems = self._grade(ex, result)
            count = result["count"]
            warn = yellow(f"   unknown command ids in uses: {', '.join(unknown)}") if unknown else ""
            if solved and count == ex.par:
                print(f"  {green('✓')} {label}  {dim(f'{count} keys = par')}{warn}")
            else:
                bad += 1
                why = "; ".join(problems) if not solved else f"took {count} keys but par is {ex.par}"
                print(f"  {red('✗')} {label}: {why}{warn}")
                print(dim(f"        keys typed: {pretty(''.join(result['keys']))}"))
        return bad

    def verify(self, which=None, drills=None, number=None):
        """drills=None: the exercises (and every drill too, if which is None). drills=True: every drill,
        drills=ID: that command's drills (or just drill NUMBER)."""
        bad = 0
        if drills is None:
            print(bold(self.title) + dim("   [replaying the reference solutions]") + "\n")
            items = [ex for ex in self.exercises if not which or which in (str(ex.number), ex.name)]
            bad += self._verify(items, self._solutions())
        if drills is not None or (which is None and self.drill_commands()):
            cmds = self.drill_commands() if drills in (None, True) else [self._find_command(drills)]
            sols = self._solutions(drills=True)
            for cmd in cmds:
                want = DRILL_SIZES[cmd.level]
                size = "" if len(cmd.drills) == want else red(f"   has {len(cmd.drills)} drills, but a {cmd.level} command should have {want}")
                print("\n" + bold(f"{cmd.keys}") + dim(f"   {cmd.name} · {cmd.level}") + size)
                bad += bool(size) and number is None
                items = cmd.drills if number is None else [self._find_drill(cmd.id, number)]
                bad += self._verify(items, sols)
        print()
        print(green(bold("All reference solutions work.")) if not bad else red(bold(f"{bad} problem(s).")))
        sys.exit(1 if bad else 0)

    def run(self):
        if os.environ.get("VIMCOURSE_COLLECT"):
            COLLECTED.append(self)
            return
        _COURSES[self.project_dir] = self
        parser = argparse.ArgumentParser(description=self.title, usage="python3 check.py [N | next | drill [COMMAND [N]] | practice | explain [COMMAND]] [options]")
        parser.add_argument("what", nargs="*", help="exercise number or name, or 'next'; drill [COMMAND [N]]; explain [COMMAND]")
        parser.add_argument("-k", metavar="TEXT", help="only list exercises whose name contains TEXT")
        parser.add_argument("--show", metavar="N", help="reveal the reference solution for exercise (or drill) N")
        parser.add_argument("--watch", metavar="N", help="watch the reference solution for exercise (or drill) N being typed")
        parser.add_argument("--speed", type=float, default=1.0, help="replay speed for --watch (2 = twice as fast)")
        parser.add_argument("--solution", action="store_true", help="replay every reference solution (or just these)")
        parser.add_argument("--try", dest="try_keys", metavar="KEYS",
                            help="replay KEYS on exercise N (or drill COMMAND N) and grade them, e.g. --try ':%%s/a/b<CR>'")
        args = parser.parse_args()
        what = args.what
        if what and what[0] in ("drill", "drills"):
            rest = what[1:]
            if args.solution:
                self.verify(drills=rest[0] if rest else True, number=rest[1] if len(rest) > 1 else None)
            elif args.try_keys is not None:
                if len(rest) < 2:
                    sys.exit("Which drill? For example:  python3 check.py drill f 3 --try 'fxx'")
                self.try_keys(self._find_drill(rest[0], rest[1]), args.try_keys)
            elif args.show or args.watch:
                if not rest:
                    sys.exit("Which command? For example:  python3 check.py drill f --show 3")
                ex = self._find_drill(rest[0], args.show or args.watch)
                self.show(ex) if args.show else self.watch(ex, args.speed)
            elif rest:
                self.play(self._find_drill(rest[0], rest[1] if len(rest) > 1 else None))
            else:
                self.drill_status()
        elif what and what[0] == "practice":
            self.practice()
        elif what and what[0] == "explain":
            self.explain(what[1] if len(what) > 1 else None)
        elif args.try_keys is not None:
            if not what:
                sys.exit("Which exercise? For example:  python3 check.py 3 --try ':%s/a/b<CR>'")
            self.try_keys(self._find(what[0]), args.try_keys)
        elif args.solution:
            self.verify(what[0] if what else None)
        elif args.show:
            self.show(self._find(args.show))
        elif args.watch:
            self.watch(self._find(args.watch), args.speed)
        elif what:
            self.play(self._find(what[0]))
        else:
            self.status(args.k)
