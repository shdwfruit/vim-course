"""Your stats: how far you are, the keys and commands you use most, and your habits.
Run from the course folder:  python3 stats.py

Completion comes from each project's .progress.json. Everything about keys comes from .history.jsonl,
where check.py writes down every try (from November 2026 on: tries before that only kept their scores).
"""
import json
import os
import re
import runpy
import sys
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

COURSE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(COURSE_DIR / "common"))
os.environ["VIMCOURSE_COLLECT"] = "1"
import trainer  # noqa: E402
from trainer import bold, cyan, dim, green, yellow  # noqa: E402

for check in sorted(COURSE_DIR.glob("[0-9][0-9]_*/check.py")):
    runpy.run_path(str(check))
COURSES = trainer.COLLECTED

WIDTH = max(60, min(100, trainer._columns() - 2))

# ---------- splitting keys into commands (the way common/coach.lua does) ----------

NORMAL = {"n", "no", "nov", "noV", "no\x16"}  # Normal and operator-pending
VISUAL = {"v", "V", "\x16"}
TAKES_ONE = {"f", "F", "t", "T", "r", "m", "`", "'", "@", "g", "z", "Z", "[", "]", "<C-W>"}
PLACEHOLDER = {"f": "{c}", "F": "{c}", "t": "{c}", "T": "{c}", "r": "{c}", "m": "{a}", "`": "{a}", "'": "{a}",
               "@": "{r}", "q": "{r}"}  # the character after these varies, so it's left out of the name
MOTIONS = {"h", "j", "k", "l", "w", "b", "e", "W", "B", "E", "0", "^", "$", "G", "gg", "+", "-", "_", "{", "}",
           "(", ")", "%", "*", "#", "n", "N", "f{c}", "F{c}", "t{c}", "T{c}", ";", ",", "/", "?", "H", "M", "L", "|",
           "`{a}", "'{a}", "ge", "gE", "Ctrl-o", "Ctrl-i", "Enter", "Backspace", "Space", "←", "→", "↑", "↓"}
OPERATORS = {"d", "c", "y", ">", "<", "=", "!", "gU", "gu", "g~", "g?", "gq", "gw", "gc"}
TYPED = {"<SPACE>", "<LT>", "<BAR>", "<BSLASH>"}  # in Insert mode these are text, like letters
NAMES = {"<ESC>": "Esc", "<CR>": "Enter", "<SPACE>": "Space", "<LT>": "<", "<BS>": "Backspace", "<TAB>": "Tab",
         "<BAR>": "|", "<BSLASH>": "\\", "<LEFT>": "←", "<RIGHT>": "→", "<UP>": "↑", "<DOWN>": "↓", "<DEL>": "Del"}


def key_name(k):
    """<C-V> -> Ctrl-v, <Esc> -> Esc, <lt> -> <."""
    if not (k.startswith("<") and k.endswith(">") and len(k) > 2):
        return k
    up = k.upper()
    if up in NAMES:
        return NAMES[up]
    m = re.fullmatch(r"<C-(.+)>", k, re.I)
    if m:
        return "Ctrl-" + (key_name(f"<{m.group(1)}>") if len(m.group(1)) > 1 else m.group(1).lower())
    return k[1:-1]


def mode_kind(m):
    if m in NORMAL:
        return "Normal"
    if m in VISUAL or m.startswith("v") or m.startswith("V"):
        return "Visual"
    if m.startswith("i") or m.startswith("R") or m == "niI":
        return "Insert"
    if m.startswith("c"):
        return "Command line"
    return "Normal"


def split(keys, modes):
    """Keys as commands: a command starts at a key that arrives in Normal mode with nothing pending."""
    cmds, cur, expect, recording = [], [], "command", False
    for i, (k, m) in enumerate(zip(keys, modes)):
        if m == "n":
            if expect == "command" and cur:
                cmds.append(cur)
                cur = []
            u = k.upper() if k.startswith("<") else k
            if expect == "char":
                expect = "command"
            elif expect == "register":
                expect = "more"
            elif re.fullmatch(r"[1-9]", k) or (k == "0" and expect == "more" and keys[i - 1].isdigit()):
                expect = "more"
            elif k == '"':
                expect = "register"
            elif k == "q":
                expect = "command" if recording else "char"
                recording = not recording
            elif u in TAKES_ONE:
                expect = "char"
            else:
                expect = "command"
        else:
            expect = "command"
        cur.append((k, m))
    if cur:
        cmds.append(cur)
    return cmds


def describe(cmd):
    """What a command was, with counts, registers' names and typed text left out: d3w is dw, fx is f{c},
    ciwfoo<Esc> is ciw, :%s/a/b/g is :s, vjjd is v…d. Returns (name, kind, operator, text object)."""
    keys = [k for k, _ in cmd]
    modes = [m for _, m in cmd]
    first = keys[0]
    if first == ":" and len(keys) > 1:
        line = "".join("" if k.upper() == "<CR>" else key_name(k) for k in keys[1:])
        word = re.match(r"[\s%.$,'<>0-9+\-]*([A-Za-z]+|&&|&|!|<|>)?", line).group(1) or ""
        return ":" + word, "ex", None, None
    if first in ("/", "?"):
        return first, "motion", None, None
    if first.upper() in ("V", "<C-V>") and len(keys) > 1 and any(m in VISUAL for m in modes[1:]):
        last = max(i for i, m in enumerate(modes) if m in VISUAL)
        return f"{key_name(first)}…{key_name(keys[last])}", "visual", None, None
    name, op, obj, i, counting = "", None, None, 0, False
    while i < len(keys) and modes[i] in NORMAL:
        k, pending = keys[i], modes[i].startswith("no")
        if re.fullmatch(r"[1-9]", k) or (k == "0" and counting):
            counting, i = True, i + 1
            continue
        counting = False
        if pending and op is None:
            op = name.replace('"{r}', "")  # the keys before operator-pending mode: d, c, gU...
        if k == '"' and not pending and i + 1 < len(keys):
            name, i = name + '"{r}', i + 2
        elif pending and k in ("i", "a") and i + 1 < len(keys):
            obj = k + key_name(keys[i + 1])
            name, i = name + obj, i + 2
        elif k in PLACEHOLDER and i + 1 < len(keys):
            name, i = name + key_name(k) + PLACEHOLDER[k], i + 2
        else:
            name, i = name + key_name(k), i + 1
    bare = name.replace('"{r}', "")
    if any(mode_kind(m) == "Insert" for m in modes[i:]):  # (r's character arrives in Replace mode: not this)
        kind = "insert"
    elif bare in MOTIONS:
        kind = "motion"
    else:
        kind = "edit"
    return name or key_name(first), kind, op, obj


# ---------- reading it all ----------

def load():
    tries, progress = [], {}
    for course in COURSES:
        progress[course] = course._progress()
        try:
            lines = course.history_path.read_text().splitlines()
        except OSError:
            continue
        for line in lines:
            try:
                t = json.loads(line)
            except ValueError:
                continue
            t["project"] = course.project_dir.name
            tries.append(t)
    tries.sort(key=lambda t: t["time"])
    return tries, progress


# ---------- drawing ----------

def bar(frac, width=24, color=green):
    frac = max(0.0, min(1.0, frac))
    full = int(frac * width * 8)
    blocks = "█" * (full // 8) + ("▏▎▍▌▋▊▉"[full % 8 - 1] if full % 8 else "")
    return color(blocks) + dim("·" * (width - len(blocks)))


def heading(text):
    print("\n" + bold(cyan(text)) + " " + dim("─" * max(3, WIDTH - len(text) - 1)))


def pct(a, b):
    return f"{100 * a / b:.0f}%" if b else "–"


def ranked(counter, n, total=None, fmt=lambda k: k):
    """'w 120 (18%) · j 98 (15%) ...' as aligned rows with bars."""
    items = counter.most_common(n)
    if not items:
        return
    top = items[0][1]
    total = total or sum(counter.values())
    kw = max(len(fmt(k)) for k, _ in items)
    for k, v in items:
        print(f"    {fmt(k).ljust(kw)}  {bar(v / top, 20, yellow)}  {v:>5}" + dim(f"  {pct(v, total)}"))


def completion(progress):
    heading("Completion")
    rows = []
    ex_total = ex_solved = ex_par = dr_total = dr_solved = dr_par = rev_total = rev_solved = 0
    for course in COURSES:
        p = progress[course]
        exs = course.exercises
        s = [e for e in exs if course._entry(e, p).get("solved")]
        a = [e for e in s if (course._entry(e, p).get("best") or 10 ** 9) <= e.par]
        drills = course.drills()
        ds = [d for d in drills if course._entry(d, p).get("solved")]
        da = [d for d in ds if (course._entry(d, p).get("best") or 10 ** 9) <= d.par]
        reviews = [e for e in exs if e.title.startswith("Review")]
        rev_total += len(reviews)
        rev_solved += sum(1 for e in reviews if e in s)
        ex_total, ex_solved, ex_par = ex_total + len(exs), ex_solved + len(s), ex_par + len(a)
        dr_total, dr_solved, dr_par = dr_total + len(drills), dr_solved + len(ds), dr_par + len(da)
        rows.append((course.project_dir.name, len(exs), len(s), len(drills), len(ds)))
    print(f"  {bold('Course')}    {bar(ex_solved / ex_total, 30)}  {bold(pct(ex_solved, ex_total)):>4}"
          + dim(f"   {ex_solved}/{ex_total} exercises solved, {ex_par} at par"))
    print(f"  {bold('Practice')}  {bar(dr_solved / dr_total, 30, cyan)}  {bold(pct(dr_solved, dr_total)):>4}"
          + dim(f"   {dr_solved}/{dr_total} drills solved, {dr_par} at par"))
    print(f"  {bold('Reviews')}   {bar(rev_solved / rev_total if rev_total else 0, 30, yellow)}  "
          f"{bold(pct(rev_solved, rev_total)):>4}" + dim(f"   {rev_solved}/{rev_total} review exercises"))
    print()
    print(dim(f"    {'project':<18} {'exercises':<22} drills"))
    for name, n, s, dn, ds in rows:
        drills = (bar(ds / dn, 14, cyan) + dim(f" {ds:>3}/{dn}")) if dn else dim("  (no drills of its own)")
        print(f"    {name:<18} {bar(s / n, 14)}{dim(f' {s:>2}/{n}')}   {drills}")


def all_time(progress):
    heading("All time")
    tries = beat = stubborn_n = 0
    stubborn = None
    unsolved_tried = 0
    for course in COURSES:
        p = progress[course]
        for ex in course.exercises + course.drills():
            e = course._entry(ex, p)
            n = e.get("attempts", 0)
            tries += n
            if e.get("solved") and e.get("best") is not None and e["best"] < ex.par:
                beat += 1
            if n and not e.get("solved"):
                unsolved_tried += 1
            if n > stubborn_n:
                label = course._label(ex) + " · " + ex.title
                stubborn, stubborn_n = (course.project_dir.name, label, e.get("solved")), n
    print(f"  {bold(str(tries))} tries in all · beat the course's par {bold(str(beat))} times"
          + (f" · {unsolved_tried} tried but not solved yet" if unsolved_tried else ""))
    if stubborn:
        project, label, solved = stubborn
        print(dim(f"  most tries on one: {label} ({project}), {stubborn_n} tries"
                  + ("" if solved else ", not solved yet")))


def keys_and_commands(tries):
    heading("Your keys" + (f" · {len(tries)} {'try' if len(tries) == 1 else 'tries'} recorded since {datetime.fromtimestamp(tries[0]['time']):%b %-d}"
                           if tries else ""))
    if not tries:
        print(dim("  Nothing recorded yet. From now on check.py writes down the keys of every try, so play a few"))
        print(dim("  exercises or drills and come back: this is where your favorite keys, combos and motions show up."))
        return
    pressed, typed, by_mode = Counter(), 0, Counter()
    commands, motions, operators, objects, inserts, ex_cmds, pairs = (Counter() for _ in range(7))
    runs = arrows = undos = dots = counted = motion_total = escs = 0
    for t in tries:
        keys, modes = t["keys"], t.get("modes") or []
        if len(modes) != len(keys):
            modes = ["n"] * len(keys)
        for k, m in zip(keys, modes):
            kind = mode_kind(m)
            by_mode[kind] += 1
            if kind in ("Insert", "Command line") and (not k.startswith("<") or k.upper() in TYPED):
                typed += 1
            else:
                pressed[key_name(k)] += 1
            arrows += key_name(k) in ("←", "→", "↑", "↓")
            escs += k.upper() == "<ESC>"
        prev, streak_key, streak = None, None, 0
        for c in split(keys, modes):
            name, kind, op, obj = describe(c)
            bare = name.replace('"{r}', "")
            commands[name] += 1
            if kind == "motion":
                motions[bare] += 1
                motion_total += 1
                counted += bool(re.fullmatch(r"[1-9]", c[0][0]))
                if bare in ("j", "k", "h", "l", "w", "b") and len(c) == 1:
                    streak = streak + 1 if bare == streak_key else 1
                    streak_key = bare
                    runs += streak == 4
                else:
                    streak_key, streak = None, 0
            else:
                streak_key, streak = None, 0
            if kind == "ex":
                ex_cmds[name] += 1
            if kind == "insert":
                inserts[bare] += 1
            if op:
                operators[op] += 1
            if obj:
                objects[obj] += 1
            undos += bare == "u"
            dots += bare == "."
            if prev and not (prev[1] == "motion" and kind == "motion"):
                pairs[f"{prev[0]}  then  {name}"] += 1
            prev = (name, kind)

    total_keys = sum(len(t["keys"]) for t in tries)
    print(f"  {bold(str(total_keys))} keys pressed: {sum(pressed.values())} commands and control keys, "
          f"{typed} characters typed into text and command lines")
    split_modes = " · ".join(f"{k} {pct(v, sum(by_mode.values()))}" for k, v in by_mode.most_common())
    print(dim(f"  where your keys went: {split_modes}"))

    print("\n  " + bold("Most pressed keys") + dim("   (not counting text you typed)"))
    ranked(pressed, 10, fmt=lambda k: k)
    print("\n  " + bold("Most used commands") + dim("   (counts and typed text left out: d3w is dw, fx is f{c})"))
    ranked(commands, 10)
    print("\n  " + bold("Favorite combos") + dim("   (two commands in a row)"))
    ranked(Counter({k: v for k, v in pairs.items() if v > 1}) or pairs, 6)

    heading("Favorites")
    def fav(label, counter):
        if counter:
            k, v = counter.most_common(1)[0]
            rest = ", ".join(f"{a} {b}" for a, b in counter.most_common(4)[1:])
            print(f"  {label:<18} {bold(k)}{' ' * max(1, 10 - len(k))}"
                  + dim(f"{v} times, {pct(v, sum(counter.values()))}" + (f" · then {rest}" if rest else "")))
    fav("motion", motions)
    fav("operator", operators)
    fav("text object", objects)
    fav("way into Insert", inserts)
    fav("Ex command", ex_cmds)

    heading("Habits")
    print(f"  counts on motions   {bold(pct(counted, motion_total))}" + dim(f"  of your {motion_total} moves had one (3j, 2w...)"))
    print(f"  the dot command     {bold(str(dots))}" + dim(" times: . repeats your last change for one key"))
    print(f"  undo                {bold(str(undos))}" + dim(" times"))
    print(f"  Esc                 {bold(str(escs))}" + dim(" times"))
    print(f"  long runs           {bold(str(runs))}" + dim(" times you pressed j, k, h, l, w or b four or more times in a row"
                                                         " (a count or f/t/search is shorter)"))
    if arrows:
        print(f"  arrow keys          {bold(str(arrows))}" + dim(" times (hjkl are right under your fingers)"))
    saves = sum(t.get("coach_saves") or 0 for t in tries)
    if saves:
        print(f"  coach               {bold(str(saves))}" + dim(" keys it found you could have saved on your own moves and edits"))


def efficiency(tries):
    if not tries:
        return
    heading("Scores and time")
    solved = [t for t in tries if t["solved"]]
    at_par = [t for t in solved if t["count"] <= t["par"]]
    over = [t["count"] - t["par"] for t in solved if t["count"] > t["par"]]
    print(f"  solved {bold(pct(len(solved), len(tries)))} of your tries, at or under par {bold(pct(len(at_par), len(tries)))}"
          + (dim(f" · over par by {sum(over) / len(over):.1f} keys on average when you were") if over else ""))
    best_streak = streak = 0
    for t in tries:
        streak = streak + 1 if t["solved"] and t["count"] <= t["par"] else 0
        best_streak = max(best_streak, streak)
    print(f"  longest run of tries at par: {bold(str(best_streak))}")
    first, best = {}, {}
    for t in tries:
        if t["solved"]:
            key = (t["project"], t["name"])
            first.setdefault(key, t["count"])
            best[key] = min(best.get(key, 10 ** 9), t["count"])
    gains = sorted(((first[k] - best[k], k) for k in first if first[k] > best[k]), reverse=True)
    if gains:
        gain, (project, name) = gains[0]
        print(f"  biggest improvement: {bold(name)} ({project}), from {first[(project, name)]} keys to "
              f"{best[(project, name)]}" + dim(f" · {len(gains)} you've solved in fewer keys than the first time"))
    drilled = Counter(t["drill"] for t in tries if t.get("drill"))
    if drilled:
        cmd, n = drilled.most_common(1)[0]
        print(dim(f"  most drilled command: {trainer.glossary()[cmd].keys if cmd in trainer.glossary() else cmd} ({n} tries)"))
    practice = sum(1 for t in tries if t.get("practice"))
    drills = sum(1 for t in tries if t.get("drill"))
    print(dim(f"  {drills} drill tries ({practice} in practice mode) and {len(tries) - drills} exercise tries"))
    seconds = sum(t.get("seconds") or 0 for t in tries)
    days = {datetime.fromtimestamp(t["time"]).date() for t in tries}
    d = datetime.now().date()
    if d not in days:
        d -= timedelta(days=1)  # nothing yet today: the streak is alive if you played yesterday
    streak_days = 0
    while d in days:
        streak_days, d = streak_days + 1, d - timedelta(days=1)
    hours = Counter(datetime.fromtimestamp(t["time"]).hour for t in tries)
    hour = hours.most_common(1)[0][0]
    per_day = Counter(datetime.fromtimestamp(t["time"]).date() for t in tries)
    busiest, busiest_n = per_day.most_common(1)[0]
    print(f"  {bold(f'{seconds / 3600:.1f} h')} in Neovim · {bold(str(len(days)))} days active · "
          f"current streak {bold(str(streak_days))} day{'s' if streak_days != 1 else ''}")
    print(dim(f"  busiest day {busiest:%a %b %-d} ({busiest_n} tries) · you play most around {hour:02d}:00"))


def main():
    tries, progress = load()
    print(bold("Neovim course · stats") + dim(f"   {datetime.now():%a %b %-d, %H:%M}"))
    completion(progress)
    all_time(progress)
    keys_and_commands(tries)
    efficiency(tries)
    print()


if __name__ == "__main__":
    main()
