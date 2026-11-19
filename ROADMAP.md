# Neovim Roadmap: from hjkl to editing at the speed of thought

This is a path from "I can get around in Vim" to "I can make any edit in a handful of keys." It has ten
stages, numbered 0 to 9. Each one teaches **a group of keys** in its README, then gives you **exercises
where you make real edits** to Java, C, Python and ASCII art while the course counts your keystrokes. A
final stage, 10, puts it all together: real files with 10 to 14 edits each, done in as few keys as you can.
Each exercise has a *par*, the key count of a good solution, like a golf hole.

**Time:** about 4–6 weeks at 20–30 minutes a day. Vim skill is muscle memory, and muscle memory is
built by short daily practice, not weekend marathons. Using each new command in your real work matters
more than finishing fast.

---

## How to use this course

The easy way in is one command from the course folder:

```bash
cd vim-course
python3 play.py               # the whole course from one screen: pick a project, then an exercise or drill
```

It opens a map of the projects with your marks. `j`/`k` (or the arrows) move, `Enter` opens a project
and then plays the exercise or drill you pick, `r` reads the project's lesson (this folder's README) in
Neovim, `p` starts mixed practice, `t` shows your stats, and `h` or `q` goes back a screen. In a game,
the menu's `q` brings you back to the list instead of quitting. Your progress and stats are the same ones
the commands below keep: use whichever you like.

```bash
cd vim-course
python3 progress.py           # your progress in every project
python3 stats.py              # your stats: completion, favorite keys, combos and motions, habits
cd 00_grammar
python3 check.py              # your progress in this project, and what's next
python3 check.py next         # play the first exercise you haven't solved
python3 check.py 3            # play exercise 3
python3 check.py drill        # this project's drills: short problems, one command at a time
python3 check.py drill f      # play the drills for f
python3 check.py practice     # endless mixed drills from this project and every one before it
python3 check.py explain f    # what a command does (works from any project)
```

You need Neovim (`brew install neovim`) and Python 3. Nothing else.

For every project:

1. **Read the project's `README.md`,** especially "The keys you need." Open any file in Neovim and try
   each command as you read about it.
2. **Drill the commands that are new to you** with `python3 check.py drill`. Each common command has ten
   short drills and each rarer one has three, in different languages and paired with other commands.
3. **Play the exercises in order** with `python3 check.py next`. Solve each one any way you can first.
   Before each one, check.py explains every command it needs.
4. **Then go for par.** When you're over par, the hint after your attempt points at the trick.
5. **Stuck after three tries?** Watch the reference solution being typed with `python3 check.py --watch N`,
   or read it with an explanation using `python3 check.py --show N`. Then close it and do it yourself.
6. **Do at least one stretch goal,** and **answer "Check your understanding"** without looking anything up.
7. **Use it for real.** Pick one new command a day and force it into your actual coding. That's how a
   command moves from "I know it exists" to "my fingers do it."

**Review exercises.** Every project ends with two bigger exercises titled "Review · …", each a list of
edits to one realistic file (several files in Project 09). They mix the project's own commands with
everything from the projects before it, and their par uses nothing from later projects, so in 00 they're
more of the basics and by 09 they sweep the whole course. They're there to keep older commands in your
fingers: play them after the project's other exercises, and come back to them a few days later.

---

## How an exercise works

`python3 check.py N` shows you the task and explains the commands you'll need. Then it opens Neovim
with three windows:

```
 4/11 · Move a line down              F1 help · F5 restart · F7/F9 back/next · ZZ submit
 The steps are out of order. Move step_two() below step_one().
 ─────────────────────────────────────┬────────────────────────────────────────
 your file          keys 0 · par 3    │ target: make your file match this
 step_two()                           │ step_one()
 step_one()                           │ step_two()
 step_three()                         │ step_three()
```

Edit the file on the left until it matches the target on the right. Differences are highlighted as you
go. Then quit any way you like (`ZZ`, `:wq`, even `:q!`) and check.py grades your result.

- **What counts:** every key you press, up to your last change to the text. Saving, quitting, and
  moving around afterwards are free. `<Esc>`, `<CR>` and `Ctrl-v` each count as one key.
- **★ par:** solved in par keys or fewer. **✓ solved:** right result, more keys. Both count as solved,
  and you can replay any exercise to improve your best.
- **At or under par, you see the course's solution** and its explanation next to your keys, so you can
  compare. Over par, it stays hidden (you get a hint instead) until you find the shorter way or ask for it:
  `s` in the menu shows it, and `w` watches it typed.
- **After every try, the coach looks for shorter ways to do what you did.** It replays your keys and,
  for each stretch where you only moved the cursor, searches for the fewest keys that land in exactly the
  same place; for edits made one right after another (`xxxx`, `dwdw`), it looks for one command that
  leaves the same text there (`4x`, `d2w`, `ct,`). It only suggests commands from your project and the
  ones before it, and it checks every suggestion by replaying your keys with it before showing it. It
  keeps your edits where you made them, so it won't find a whole different plan (that's what par and
  the course's solution are for), but it shows where your moves were longer than they had to be.
- **F1** shows or hides notes on the commands this exercise uses, in a window over the top right. It
  doesn't count as a key, and you can keep typing while it's open.
- **F5** starts the exercise over. It resets the count and the text, and everything an earlier attempt
  could reuse: undo history, registers, marks, searches, command history, and what `.`, `&`, `;` and
  `@:` would repeat. Windows you split or closed go back to how they started.
- **F7 and F9** leave for the previous and next exercise, and **F8** goes back to the menu (below).
  None of them grades your try. Quitting without changing anything (`:q`) doesn't count as a try either.
- **Project 10's exercises list their edits.** check.py prints the numbered list before Neovim opens,
  and F1 shows it inside Neovim as a checklist.
- **Project 09's exercises have several files** and no target window. The task says exactly what to
  change, and Neovim starts in a folder containing just those files.
- **Arrow keys and the mouse** count like any other key, and check.py will gently call them out.
- **A fixed setup:** exercises run with `common/init.lua` instead of your own config, so your results
  and the pars never change. It matches your settings: 4-space indents, `ignorecase` + `smartcase`,
  relative line numbers. Nothing (registers, history) carries over between attempts.

### Getting around

check.py shows a menu before Neovim opens and after every try. It takes one key, no Enter needed:

| Key | Does |
|---|---|
| `Enter` | start the exercise; after a try, the next one if you solved it, else try again |
| `→` or `n` | the next exercise (from a project's last one, on into the next project) |
| `←` or `p` | the previous one (from a project's first, back into the previous project) |
| `↑` / `↓` | the previous / next project, at the first exercise you haven't solved. In drills: the previous / next command |
| a number, then `Enter` | that exercise (in drills, that drill of the current command) |
| `l` | list them all with your marks, and pick one (in drills, pick a command) |
| `r` | try this one again |
| `s` | show the course's solution, with why it works |
| `w` | watch Neovim type the course's solution (`ZZ` closes it), then try it yourself |
| `q` or `Ctrl-C` | quit, printing the command that brings you right back (`cd … && python3 check.py 4`). From `play.py`: back to its list |

So there's no need to quit and type `python3 check.py 7`: press `7` and `Enter`, or `F9` inside Neovim to
skip ahead.

Other commands:

```bash
python3 check.py --watch 3    # watch the reference solution being typed (add --speed 0.5 to slow it down)
python3 check.py --show 3     # read the reference solution with an explanation
python3 check.py --solution   # replay every reference solution, to check the project works at all
python3 check.py explain      # every command in the course, one line each
python3 check.py 3 --try 'dd' # replay keys of your own on exercise 3: the count, and whether it's right
```

## Drills

Exercises mix several commands. Drills practice **one command at a time**: twenty short problems for each
command you'll use all the time (`f`, `p`, `ci(`, `:s`, ...) and six for each rarer, more complex one
(`R`, `g?`, recursive macros, `:cdo`, ...). Each set starts with the command on its own and then pairs it
with others, in Java, C, Python, prose and ASCII art. Every project has its own drills for the commands it
introduces, about 1,400 in all.

```bash
python3 check.py drill            # the list, with your progress (★ at par, ✓ solved, ✗ tried, ○ not yet)
python3 check.py drill f          # play the drills for f, from the first one you haven't solved
python3 check.py drill 3          # the third command in the list
python3 check.py drill f 4        # just drill 4
python3 check.py drill f --show 4 # its solution, explained (--watch 4 to see it typed)
```

**Mixed practice.** `python3 check.py practice` plays random drills from the project you run it in and
every project before it, for as long as you like: in 03_operators, that's 00 to 03. The ones you haven't
solved yet, or solved over par, come up more often, and so do the ones you haven't played for a while, so
old commands keep coming back before you forget them. `←` and `→` step back and forth through the ones
you've had, and `q` stops.

Drills are scored exactly like exercises. When you finish one, Enter takes you to the next, and after the
last drill for a command, on to the next command. `←` and `→` step through drills, `↑` and `↓` jump to the
previous or next command, a number and `Enter` picks a drill of this command, and `l` lists the commands. The first drill for a command explains it in full. F1
brings the explanation back inside Neovim.

---

## The map

| Stage | You learn | Keys | You'll be able to |
|---|---|---|---|
| 0 | **The grammar** | `d c y > ` + motions, counts, `.` | read and write commands as sentences: verb + count + noun |
| 1 | **Motions** | `f t ; , w e b % { } * # / ? n` marks, jumps | get anywhere on the screen in 2–4 keys |
| 2 | **Text objects** | `iw aw i" a( i{ it ip` … | change "the thing the cursor is inside" without aiming |
| 3 | **More operators** | `= gu gU g~ gq gw ! gc J Ctrl-a` | reindent, recase, rewrap, comment, and filter text through shell commands |
| 4 | **Visual and block mode** | `v V Ctrl-v o gv I A $A r g Ctrl-a` | edit columns and rectangles, number lists, draw ASCII art |
| 5 | **Registers** | `"a "A "0 "_ "1 Ctrl-r Ctrl-r=` | keep several clipboards, paste the right thing, do math while typing |
| 6 | **Macros** | `qa @a @@ 10@a :normal` recursive macros | automate any repetitive edit |
| 7 | **Ex commands and `:s`** | ranges, `:s` with `\v` groups `\U` `\=`, `:g :v :t :m :sort :normal` | transform a whole file with one line |
| 8 | **Insert and command-line mode** | `Ctrl-w Ctrl-u Ctrl-o Ctrl-r Ctrl-a Ctrl-n Ctrl-x Ctrl-l Ctrl-k q: @:` | fix things without leaving Insert mode, and reuse commands |
| 9 | **Many files** | buffers, windows, `:args :argdo :vimgrep :cdo` | make a change across a whole project |
| 10 | **Putting it together** | everything above, planned | make 10–14 edits to a real file in close to the fewest keys |

---

## The stages

### Stage 0 · The grammar (about 1–2 hours) → Project 00

- **Keys:** operators `d c y > <`; motions `w b e 0 ^ $ f t`; counts; doubled operators (`dd cc yy >>`);
  the shortcuts `x X s S D C Y`; inserting with `i a I A o O`; `r`; `p P`; `J`; `u Ctrl-r`; `.` and `;`.
- **The big idea:** Vim commands are sentences. Learn ten verbs and twenty nouns and you know two
  hundred commands. `.` repeats the last sentence.
- **Ready when** you can explain why `A;<Esc>` followed by `j.` works on lines of different lengths.

### Stage 1 · Motions (about 2–3 hours) → Project 01

- **Keys:** words vs WORDS (`w W e E b B ge`); line positions `0 ^ $`; `f t F T ; ,`; `%` for brackets;
  paragraphs `{ }`; `gg G` and `:42`; search `/ ? n N`; `* #` for the word under the cursor; marks
  (`ma`, `'a`, `` `a ``); the jump list (`Ctrl-o`, `Ctrl-i`) and the change list (`` `. ``, `gi`).
- **The big idea:** move by meaning (the next comma, the matching bracket, the next use of this name),
  not by counting characters. Every motion is also a noun for `d`, `c` and `y`.
- **Ready when** you can delete from the cursor to the next occurrence of a word anywhere in the file
  in one command.

### Stage 2 · Text objects (about 2 hours) → Project 02

- **Keys:** `iw aw iW aW`, `is as`, `ip ap`, `i" a" i' a' i` a``, `i( a( ib`, `i{ a{ iB`, `i[ a[`,
  `i< a<`, `it at`.
- **The big idea:** "inner" and "around" objects let you act on the thing the cursor is *in*, wherever
  in it the cursor is. `ci"` doesn't care whether you're at the start, middle or end of the string.
- **Ready when** you can explain when to use `daw` instead of `diw`, and `ci(` instead of `ct)`.

### Stage 3 · More operators (about 2–3 hours) → Project 03

- **Keys:** `>` `<` `=` (reindent); `gu gU g~ ~` (case); `gq gw` (rewrap to `textwidth`); `!` (filter
  through a shell command, such as `!ip sort`); `gc` (comment, built into Neovim); `J gJ`;
  `Ctrl-a Ctrl-x` (increment numbers); `g?` (rot13, for fun).
- **The big idea:** every new operator multiplies with every motion and text object you already know.
  `gUiw`, `=ap`, `gcip`, `!ip sort` need no new learning once you have the grammar.
- **Ready when** you can sort the lines of a paragraph and reindent a function without leaving Normal mode.

### Stage 4 · Visual and block mode (about 2–3 hours) → Project 04

- **Keys:** `v V Ctrl-v`; `o` to swap ends; `gv` to reselect; block `I A $A c r`; `>` on selections;
  `g Ctrl-a` for sequences; `:'<,'>`.
- **The big idea:** use Visual mode when you can't name the text with a motion, and block mode for
  columns. Prefer operators + motions when you *can* name it, because `.` repeats those better.
- **Ready when** you can add a column of text to 20 lines at once and draw a box in ASCII art.

### Stage 5 · Registers (about 2 hours) → Project 05

- **Keys:** named registers `"a`–`"z` and appending `"A`; the yank register `"0`; the black hole `"_`;
  the numbered delete history `"1`–`"9`; `".` `"%` `":` `"/`; `Ctrl-r {reg}` in Insert and
  command-line mode; the expression register `Ctrl-r =`.
- **The big idea:** Vim has dozens of clipboards. Knowing which one holds what fixes the classic
  "I yanked, then deleted, and now `p` pastes the wrong thing" problem.
- **Ready when** you can explain what `"0p` does that `p` doesn't.

### Stage 6 · Macros (about 3 hours) → Project 06

- **Keys:** `qa … q`, `@a`, `@@`, `10@a`, recursive macros, `:normal @a` on a range, appending with `qA`,
  editing a macro as text.
- **The big idea:** a macro is a recorded sequence of keys. Write it so it works on *any* line (start
  with `0` or a search, end by moving to the next target) and you can run it a thousand times.
- **Ready when** you can turn 30 lines of CSV into 30 lines of Java code with one recorded macro.

### Stage 7 · Ex commands and substitution (about 3–4 hours) → Project 07

- **Keys:** ranges (`.`, `$`, `%`, `'<,'>`, `/start/,/end/`, `+3`); `:s` with flags; very magic `\v`;
  groups and back-references; case changes `\u \U \l \L`; expressions `\=`; `:g` and `:v`; `:normal`;
  `:t` and `:m`; `:sort`.
- **The big idea:** Normal mode edits what's under the cursor; Ex commands edit *every line that
  matches*. `:g/TODO/d` and `:%s/\v(\w+), (\w+)/\2 \1/` do in one line what would take a macro.
- **Ready when** you can swap the order of two comma-separated fields on every line with one `:s`.

### Stage 8 · Insert and command-line mode (about 2 hours) → Project 08

- **Keys:** Insert mode `Ctrl-w Ctrl-u Ctrl-t Ctrl-d Ctrl-o Ctrl-r Ctrl-a Ctrl-n Ctrl-p Ctrl-x Ctrl-l
  Ctrl-v Ctrl-k`; command line `Ctrl-r Ctrl-w`, `q:`, `@:`.
- **The big idea:** Insert mode has its own small toolkit. Fixing a typo with `Ctrl-w` is faster than
  `<Esc>`, `b`, `cw`, and completion saves typing long names.
- **Ready when** you can insert the result of `37 * 41` without a calculator.

### Stage 9 · Many files (about 2–3 hours) → Project 09

- **Keys:** buffers (`:ls :b :bn Ctrl-^`), windows (`Ctrl-w s v w c o`), the argument list (`:args
  :argdo`), `:bufdo`, the quickfix list (`:vimgrep :cnext :cdo :cfdo`).
- **The big idea:** `:vimgrep` finds every match across the project, and `:cdo` runs a command at each
  one. That's a project-wide find-and-replace with full Vim power.
- **Ready when** you can rename a function in every file of a project and save them all, in two commands.

### Stage 10 · Putting it together (about 5–8 hours) → Project 10

- **Keys:** nothing new. Fifteen real files (a merge conflict, a code review, a JUnit migration, a
  ShellCheck report, a schema migration, an ASCII diagram, ...) with 10 to 14 edits each, and pars from
  66 to 182 keys.
- **The big idea:** planning. Pick the tool for each edit, spot the edits one command can do together,
  and choose the order so each command leaves the cursor where the next edit starts. Reuse text that's
  already in a register or the file instead of typing it.
- **Ready when** you can read a list of review comments and see, before touching a key, which ones are
  one `:s`, which are one `.` chain, and what order to do them in.

---

## After the course: where to go next

- **Language servers (LSP).** Neovim has an LSP client built in. Set up `clangd` (C), `basedpyright`
  (Python) and `jdtls` (Java) for go-to-definition, rename, and inline errors. Then learn the default
  keys: `grn` (rename), `gra` (code action), `grr` (references), `K` (hover), `]d` (next diagnostic).
- **Make it yours with Lua.** Write your own mappings, commands and autocommands, like the `:Art`
  command in your config. Start with `:help lua-guide`.
- **Plugins worth knowing.** A fuzzy finder (`fzf-lua` or `telescope.nvim`), surround editing
  (`mini.surround` or `nvim-surround`), and Tree-sitter text objects (`nvim-treesitter-textobjects`)
  extend everything you learned in Stages 1–3. Neovim 0.12 installs plugins with `vim.pack.add()`.
- **Golf.** VimGolf (vimgolf.com) is the same "fewest keystrokes" game as this course, with thousands
  of challenges and other people's solutions to learn from.

---

## Resources (free unless noted)

- **`:Tutor`** inside Neovim: a 30-minute interactive tutorial of the basics. Good for a refresher.
- **`:help`**: Vim's documentation is excellent and searchable. `:help usr_toc` is the user manual,
  `:help d`, `:help text-objects` and `:help :s` jump to any topic, and `Ctrl-]` follows links.
- ***Practical Vim*, 2nd edition, by Drew Neil** (paid): the best book on Vim's editing language. Project 00's
  "dot formula" comes from it.
- **Vimcasts** (vimcasts.org): free screencasts by the same author.
- ***Learn Vim (the Smart Way)*** by Igor Irianto (github.com/iggredible/Learn-Vim): a free book that
  covers everything here in more depth.
- **kickstart.nvim** (github.com/nvim-lua/kickstart.nvim): a small, heavily commented Neovim config
  to read when you're ready to set up LSP and plugins.

---

## Habits that separate fluent Vim users from people who just know the keys

1. **Think in sentences.** Say the edit to yourself ("change inside the quotes") and type the sentence
   (`ci"`). If you can't say it, you're about to hold down `l`.
2. **Make changes repeatable.** Prefer edits that `.` can repeat: `A;` over `$a;`, `ciw` over `bcw`.
   One key to move, one key to repeat, is the fastest editing there is.
3. **Move by meaning, not by counting.** Search, `f`/`t`, `%`, `*` and text objects beat `jjjjlllll`.
   If you're pressing the same motion key four times, there's a better motion.
4. **Automate on the third repetition.** Once: do it. Twice: notice it. Three times: `.`, a macro, or `:s`.
5. **Live in Normal mode.** Insert mode is for typing new text, briefly. Get out with `<Esc>` the moment
   you're done typing.
6. **Read `:help` for anything you use daily.** Almost every command has an option or variant you
   don't know yet.
