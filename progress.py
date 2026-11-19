"""Your progress in every project.  Run from the course folder:  python3 progress.py"""
import os
import runpy
import sys
from pathlib import Path

COURSE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(COURSE_DIR / "common"))
os.environ["VIMCOURSE_COLLECT"] = "1"
import trainer  # noqa: E402

for check in sorted(COURSE_DIR.glob("[0-9][0-9]_*/check.py")):
    runpy.run_path(str(check))

print(trainer.bold("Neovim course") + trainer.dim("   exercises, then drills (practice one command at a time)") + "\n")
total_solved = total_par = total = drills_done = drills_total = 0
widest = max(len(c.exercises) for c in trainer.COLLECTED)
next_up = reached = None
for course in trainer.COLLECTED:
    progress = course._progress()
    n = len(course.exercises)
    solved = sum(1 for ex in course.exercises if course._entry(ex, progress).get("solved"))
    at_par = sum(1 for ex in course.exercises
                 if course._entry(ex, progress).get("solved") and course._entry(ex, progress).get("best", 10 ** 9) <= ex.par)
    total, total_solved, total_par = total + n, total_solved + solved, total_par + at_par
    bar = "".join(trainer.yellow("★") if i < at_par else trainer.green("✓") if i < solved else trainer.dim("·")
                  for i in range(n)) + " " * (widest - n)
    drills = course.drills()
    done = sum(1 for ex in drills if course._entry(ex, progress).get("solved"))
    drills_done, drills_total = drills_done + done, drills_total + len(drills)
    drill_note = f"   drills {done:>3}/{len(drills)}" if drills else ""
    name = course.project_dir.name
    print(f"  {name:<20} {bar}  {solved:>2}/{n} solved, {at_par:>2} at par{drill_note}")
    if next_up is None and solved < n:
        next_up = name
    if progress and drills:
        reached = name  # the furthest project you've played that has drills
print()
print(f"{total_solved}/{total} exercises solved · {total_par} at par · {drills_done}/{drills_total} drills solved")
if next_up:
    print(f"Next up: cd {next_up} && python3 check.py next      (python3 check.py drill for that project's drills)")
if reached:
    print(f"Mixed drills from everything up to {reached}:  cd {reached} && python3 check.py practice")
print("Your stats (favorite keys, combos, habits):  python3 stats.py")
print("Everything from one screen (no cd needed):  python3 play.py")
