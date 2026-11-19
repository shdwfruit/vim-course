# Project 10 · Advanced: real files, many edits, fewest keys

> **Stage 10 · Putting it together** · about 5–8 hours · 17 exercises

## What you'll learn

There are no new keys in this project. Every exercise is a real file (a Java service, a C module, a
Python script, a SQL schema, a Bash deploy script, a README, a docker-compose file, an ASCII diagram)
with **10 to 14 edits** to make, written the way they reach you at work: review comments, a migration
ticket, a merge conflict, compiler and linter output.

What's new is **planning**. In Projects 00–09 each exercise had one trick. Here every edit has three or
four reasonable tools, and the choices affect each other:

- **Which tool for each edit:** a search and `cw`, a text object, `.`, a macro, one `:s` or `:g`.
- **Which edits are secretly the same:** two steps that look different but can be done by one command.
- **What order to do them in:** every command leaves the cursor somewhere, and a good order makes the
  next edit start right where the last one ended.
- **What text you can reuse:** what you just deleted, yanked or typed is still in a register, and
  completion can type the rest of a long name.

Par is the shortest solution the course's authors found, and then a second golfer tried to beat it.
Pars run from 66 to 182 keys. Expect to be well over par on your first try. That's normal: solve
it first, then go for par.

## How these exercises work

They work like every other exercise, with two additions:

- **The list of edits.** check.py prints the numbered list before Neovim opens, and **F1** shows it
  inside Neovim as a checklist, with notes on the commands that help underneath (F1 doesn't count as a
  key). The target window on the right shows the result, with every difference highlighted.
- **The course's solution comes in steps.** When you reach par, check.py shows the reference
  solution split into stretches, each with its key count and which edits it makes, so you can compare
  your plan with it stretch by stretch. `python3 check.py --show N` shows the same thing any time.

Testing an idea doesn't need Neovim:

```bash
python3 check.py 4 --try ':%s/old/new/g<CR>'   # replay these keys on exercise 4: count and result
```

## How to plan a long edit

1. **Read the whole list before you touch anything.** Sort the edits into ones that repeat (the same
   change in several places) and ones that happen once.
2. **Look for one command that does several edits.** A `:s` with `\|` or a group can fix two
   different-looking steps at once. One `:g/pattern/norm ...` can do the same edit on every matching
   line. A rename usually takes one `*` and one `:%s//new/g`.
3. **Choose the order by where the cursor lands.** `:s` over a range ends on the last line it
   changed, `:g` on the last match, `dd` on the line below. Editing bottom-up keeps the line numbers
   above you stable. Doing a whole-file command first is good when it leaves you next to a local edit.
4. **Move by meaning.** A short search (`/Ar<CR>`) beats counting lines, unless the relative line
   number is right there in the margin. `*`, `%`, `}` and `f`/`t` with `;` cover most of the rest.
5. **Reuse text.** What you just deleted is in `"` and `-`, what you yanked is in `0`, what you typed
   last is in `.`. `Ctrl-r` puts any of them into Insert mode or the command line. `Ctrl-n` and
   `Ctrl-p` complete a name that's already in the file, and `Ctrl-x Ctrl-l` a whole line.
6. **Make it repeatable.** If you'll make an edit twice, make it with something `.` repeats: `ciw`,
   `A;`, `cgn`. Three times or more, consider a macro (`Q` replays the last one).
7. **End in Insert mode if you can.** Keys after your last change are free, so the final `<Esc>` costs
   nothing. Make the edit that ends in typing the last one.

### Neovim details that matter here

- **`|` after `:s`:** `:s/a/b|s/c/d` fails, because without the closing `/` the `|` becomes part of the
  replacement. Write `:s/a/b/|s/c/d`.
- **Columns:** `G`, `12G`, `j` and `k` keep the cursor's column, so the motion after them starts from
  wherever the last edit left the cursor. `I`, `A`, `^`, `+` and `-` don't depend on it.
- **`Ctrl-a`** only finds numbers at or after the cursor on the line.
- **Completion in Insert mode** follows smartcase: `M` then `Ctrl-p` only offers words starting with a
  capital M.
- **`.` after a `Ctrl-r` insert** reads the register again, so `ciW"<C-r>-"` then `.` quotes each new
  WORD with its own text.
- **Inside `:g`**, the `'[` mark moves to each line you change or copy, so `:g/pat/t'[` copies the
  matching lines in their original order.

## Your exercises

| # | Exercise | File | What makes it short (spoilers, lightly) | Par |
|---|---|---|---|---|
| 1 | Resolve a merge | Python | merge conflicts: `:sort u`, one `:g` for every marker, counted deletes | 66 |
| 2 | Review a docker-compose file | YAML | `ciw` + `.` renames, `ciW"<C-r>-"` + `.` quotes, `Ctrl-a` with counts | 83 |
| 3 | Redraw the architecture | ASCII art | `R`, Visual block, whole-line `Vp` swaps | 101 |
| 4 | Declare before use | C | prototypes with one `:g` and `:t'[`, renames chained with `\|` | 106 |
| 5 | Tidy a README | Markdown | `:g` with `:normal`, `g Ctrl-a`, a block yank to align a table | 110 |
| 6 | Fix what ASan found | C | a recorded fix replayed with `Q`, `Ctrl-x Ctrl-l`, the `.` register | 113 |
| 7 | Modernize an old class | Java | `di<` + `.`, a macro for switch cases, reusing deleted text | 123 |
| 8 | Port a script to Python 3 | Python | `:g/pat/norm`, completion in Replace mode, working bottom-up | 137 |
| 9 | Globals into a struct | C | one `:s` with `\v` alternatives, `cgn` + `.`, `Ctrl-a` with counts | 136 |
| 10 | Move a test module to pytest | Python | two `:s` then one `:g` that rewrites every assert | 139 |
| 11 | Make ShellCheck happy | Bash | `.` chains, `\L&` in `:s`, `=ip`, `ca[` | 149 |
| 12 | Fix a training script | Python | `*` then `:%s//&imizer`, `:m`, `A()` + `.`, indenting a block | 141 |
| 13 | Rework a schema for a migration | SQL | `~` with a count, a macro that stays in Insert mode, `dap` moves | 174 |
| 14 | Apply a code review | Java | `*` + `.`, one recorded swap replayed with `Q`, `Ctrl-a` in Insert mode | 179 |
| 15 | Migrate a test class to JUnit 5 | Java | Visual-block insert, one `:s` for three steps, `Ctrl-r` pastes | 182 |
| 16 | Review · Update a café's menu page | HTML | digraphs, `cit`, a macro, then one `:s` with `\|` for every price | 164 |
| 17 | Review · Clean up a package.json | JSON | `gu$`, `R`, numbered registers, `:sort` and its commas, `4J` | 147 |

## Run it

```bash
cd 10_advanced
python3 check.py              # your progress, and what's next
python3 check.py next         # play the first exercise you haven't solved
python3 check.py 3            # play exercise 3
python3 check.py 3 --try 'keys'  # replay keys on exercise 3 and see the count
python3 check.py --watch 3    # watch the reference solution being typed
python3 check.py --show 3     # read the reference solution, step by step
```

## Drills

This project has no drills of its own: every command it uses was drilled in Projects 00–09. When an
exercise's notes mention a command you're rusty on, drill it in its own project. `python3 check.py
explain ID` works from any folder and tells you which project it's in.

## Stretch goals

1. **Beat a par.** The pars are the best solutions found, not proven minimums. If you beat one, look at
   which edits you merged or reordered that the reference didn't.
2. **Solve one in two different styles:** once with only Normal-mode commands and `.`, once leaning on
   `:s`, `:g` and `:normal`. Which was shorter? Which was faster to think of?
3. **Bring your own file.** Take a real review of your own code with ten or more comments. Write down
   the edits, plan an order, and count your keys.
4. **VimGolf** (vimgolf.com) is this same game with thousands of challenges and other people's solutions.

## Check your understanding

- You need to rename a variable in a whole file and fix a typo on the line below its declaration. Which
  do you do first, and why?
- Why might `:%s/x/y/g` followed by `kdd` be shorter than doing those edits the other way round?
- What's in registers `"`, `0`, `-` and `.` after you `yiw`, then `dw`, then type `foo` and press
  `<Esc>`?
- When is a macro shorter than `:g/pat/norm ...`, and when is it the other way round?
- Why is the final `<Esc>` of a solution free, and how can you use that when you plan the order?
