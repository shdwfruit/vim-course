# Project 05 · Registers: many clipboards, and math while you type

> **Stage 5 · Registers** · about 2 hours · 12 exercises

## What you'll learn

Vim doesn't have one clipboard. It has dozens, called **registers**, and every yank and delete quietly
fills some of them:

```
  yy, yiw ...        ──>  ""  (unnamed: what p pastes)  +  "0  (the last yank)
  dd, cc, dj ...     ──>  ""  +  "1 ──> "2 ──> ... ──> "9  (delete history)
  dw, x, ciw ...     ──>  ""  +  "-  (the last small delete)
  "ayy, "add ...     ──>  ""  +  "a  (only when you ask for it)
```

That picture explains the most common Vim surprise: you yank a line, delete another one, press `p`,
and get the deleted line. The yank isn't lost, it's in `"0`. This project teaches you which register
holds what, how to paste from registers in Insert mode and on the command line, and how to use the
expression register as a calculator without leaving the file.

## The keys you need

### Using a register

Put `"` and a register name in front of any yank, delete or put:

| Keys | Does |
|---|---|
| `"ayy` | yank the line into register `a` |
| `"ap` / `"aP` | put register `a` after / before the cursor |
| `"bdiw` | delete the word into register `b` |
| `"a3p` or `3"ap` | put register `a` three times |
| `:reg` | show what's in every register (`:reg a0` shows just `a` and `0`). Press Enter to close it. |

In Insert mode and on the command line, `Ctrl-r {register}` inserts a register. More on that below.

### The unnamed register `""`

Every `d`, `c`, `s`, `x` and `y` fills the unnamed register, even when you also name a register
(`"ayy` fills both `a` and `""`). Plain `p` and `P` paste from it. That's all "copy and paste" is in Vim:
whatever you last yanked *or deleted* is what `p` pastes.

Visual mode has two puts, and the difference matters:

| Keys | Does |
|---|---|
| `p` in Visual mode | replace the selection, and put the **replaced text** into `""` |
| `P` in Visual mode | replace the selection and leave every register alone (Neovim) |

Visual `p` gives you a swap for free: cut one thing, select another, `p`, and you're now holding the
other thing, ready to paste where the first one was. Visual `P` is for pasting the same text over
several selections in a row.

### Named registers `"a`–`"z`, and appending with `"A`–`"Z`

Vim fills the 26 named registers **only when you say so**, so they're safe places to park text while you
edit. A lowercase name replaces the contents. An uppercase name **appends**:

```
"ayy     register a = this line
j"Ayy    register a = this line + the next one (both lines, in order)
G"ap     put both lines at the end of the file
```

If both parts are within a line, appending joins them with nothing in between (`"ayiw` on `foo`, then
`"Ayiw` on `bar` gives `foobar`). If either part is line-wise, the result is line-wise.

`.` remembers the register too, so `"Add` followed by `n.` `n.` appends three lines. Before appending
to a register that might already hold something, clear it: `qaq` (record an empty macro into `a`, the
fastest way) or `:let @a = ''`.

### The yank register `"0`

`"0` holds the text of your **last yank**, and deletes never touch it. That's the fix for the classic
problem:

```
yiw          yank a word: it's in "" and "0
ciw          change another word: now "" holds the word you just deleted
Ctrl-r "     types the deleted word back. Not what you wanted.
Ctrl-r 0     types the yanked word. That's the one.
```

The same goes for Normal mode: after `yy` and `dd`, `p` pastes the deleted line and `"0p` pastes the
yanked one. Only plain yanks go into `"0`: `"ayy` fills `a` and `""` but leaves `"0` alone.

### The black hole `"_`

Anything deleted into `"_` is gone, and no register changes. Use it when you're holding something you
still need: `"_dd` deletes a line without touching `""`, so `p` still pastes what you cut or yanked
before. It's also handy with `c`: `"_ciw` changes a word without saving it anywhere.

### The delete history `"1`–`"9`

`"1` holds the most recent delete or change of **a line or more** (`dd`, `cc`, `dj`, `dap`, `3dd` …).
Each new one shifts the history down: `"1` moves to `"2`, `"2` to `"3`, and `"9` falls off the end. So the
last nine big deletes are always there.

| Keys | Does |
|---|---|
| `"1p` | put the most recent delete |
| `"3p` | put the delete from three deletes ago |
| `"1p` then `.` `.` | put `"1`, then `"2`, then `"3`: after a numbered put, `.` uses the next number |
| `"1p` then `u.` `u.` | browse: put `"1`; wrong one? undo and put `"2`; still wrong? undo and put `"3` |

**Gotcha:** deletes within a line (`dw`, `x`, `D`, `diw`) don't enter the history. They go to `"-`
instead. The exception is a delete with one of the motions `%` `(` `)` `` ` `` `/` `?` `n` `N` `{` `}`:
`d/foo` always goes into `"1`, even inside a line.

### The small delete register `"-`

`"-` holds the last delete that was smaller than a line, as long as you didn't name a register. So
after `ciw`, the word you replaced is in `"-` (and in `""`). Line-wise deletes don't touch `"-`, so it
survives a `dd`.

`Ctrl-r -` has a special power in Insert mode: when you repeat the change with `.`, it inserts the
register's *current* contents instead of the text it inserted the first time. That makes "wrap this
thing" repeatable:

```
ciWint(Ctrl-r -)<Esc>     on x.size:  int(x.size)
.                         on y.size:  int(y.size), not int(x.size)
```

Every other register repeats as the literal text that was inserted, so `Ctrl-r "` in the same change
would type `x.size` again on every line.

### Read-only registers `".` `"%` `":` `"/`

Vim fills these for you, and you can paste them like any other register (`".p`, `Ctrl-r %`):

| Register | Holds | Example use |
|---|---|---|
| `".` | the last text you typed in Insert mode | type a name once, insert it again with `Ctrl-r .` |
| `"%` | the current file's name | `"%p` puts `Inventory.java` |
| `":` | the last command line | `":p` pastes it; `@:` runs it again (Project 08) |
| `"/` | the last search pattern | after `*` on `count`, it holds `\<count\>` |

### `Ctrl-r` in Insert mode and on the command line

`Ctrl-r {register}` inserts a register without leaving Insert mode. It works on the `:` and `/` command
lines too.

| Keys | Inserts |
|---|---|
| `Ctrl-r a` | register `a` (any register name works: `0`, `"`, `-`, `.`, `%` …) |
| `Ctrl-r Ctrl-w` | on the command line: the word under the cursor |
| `Ctrl-r Ctrl-a` | on the command line: the WORD under the cursor |

`:%s/<C-r><C-w>/total/g` renames the word under the cursor without typing it. It works for the new
name too: with the cursor on it, `:%s/tmp/<C-r><C-w>/g`, or with it yanked, `:%s/tmp/<C-r>0/g`.

**How the text goes in.** Named and numbered registers (`a`–`z`, `0`–`9`) are inserted literally, like
`p`. The others (`"`, `-`, `.`, `%` …) are inserted as if you typed them, so auto-indent applies. For
a single word that's the same thing. For whole lines of indented code it can double the indentation,
so use `p`, or `Ctrl-r Ctrl-o {register}`, which inserts literally without auto-indent.

### The expression register `"=`: a calculator

`Ctrl-r =` in Insert mode opens a prompt at the bottom. Type an expression, press Enter, and the result
is inserted:

| You type | Inserts | Note |
|---|---|---|
| `Ctrl-r =60*60*24<CR>` | `86400` | |
| `Ctrl-r =7/2<CR>` | `3` | whole numbers give whole-number division |
| `Ctrl-r =7/2.0<CR>` | `3.5` | use a decimal point to get decimals |
| `Ctrl-r =10%3<CR>` | `1` | remainder |
| `Ctrl-r =0xff<CR>` | `255` | hex (`0x`) and binary (`0b`) work too |
| `Ctrl-r =@a*@b<CR>` | `840` | if `a` holds 120 and `b` holds 7: registers are `@a`, `@b` … |
| `Ctrl-r =printf("%.2f", 19.99*3)<CR>` | `59.97` | format the result |

The prompt is a command line, so `Ctrl-r` works inside it: yank a formula like `1024 * 1024`, then
`Ctrl-r =` `Ctrl-r 0` `<CR>` inserts its value. In Normal mode, `"=` picks the expression register for
a put: `"=6*7<CR>p` puts `42` after the cursor.

**Repeating.** `.` after an Insert-mode `Ctrl-r =` repeats the *result* it inserted. `.` after a
Normal-mode `"=…p` evaluates the expression *again*, which matters when it uses registers or
functions like `line('.')`.

### The system clipboard `"+`

`"+` is your Mac's clipboard (on macOS, `"*` is the same one). `"+yy` copies a line so you can paste it
in your browser, and `"+p` pastes what you copied there. Some people `:set clipboard=unnamedplus` so
every yank and delete goes to the system clipboard. It's convenient, but then deleting a line also
replaces whatever you copied in another app. The exercises run with clean registers and never use the
clipboard.

## Your exercises

| # | Exercise | What it teaches |
|---|---|---|
| 1 | Delete without losing your cut | the black hole register `"_` |
| 2 | Swap the arguments | Visual `p` swaps through the unnamed register |
| 3 | Paste the yank, not the delete | the yank register `"0`, and `Ctrl-r 0` |
| 4 | Free in reverse order | the delete history `"1`–`"9`, and `.` after `"1p` |
| 5 | Collect the imports | appending to a named register with `"A` |
| 6 | Match the file name | the read-only `"%` register |
| 7 | Wrap each argument | the small delete register, and repeating `Ctrl-r -` |
| 8 | Rename, but keep the old name | `""` and `".` in Insert mode |
| 9 | Rename from the command line | `Ctrl-r Ctrl-w` on the command line |
| 10 | Let Vim do the math | the expression register `Ctrl-r =` |
| 11 | Review · Tidy a weather script | 00–05 mixed: `"%`, `"a` then `"A` to carry two lines, `Ctrl-r -` + `.`, `R` + `*` + `n.`, `viwp` |
| 12 | Review · Fix an upload config | 00–05 mixed: `C` + `Ctrl-r =` + `Ctrl-r -`, a swap through `"a`, `Ctrl-r 0`, `Vp` |

## Run it

```bash
python3 check.py          # see the exercises and your progress
python3 check.py next     # play the first one you haven't solved
python3 check.py 4        # play exercise 4
python3 check.py --watch 4   # stuck after three tries? watch the reference solution
```

See "How an exercise works" in [`../ROADMAP.md`](../ROADMAP.md) for the scoring rules.

## Drills

Drills are short extra problems that practice one register at a time, in different files and pairings,
from its simplest form to small realistic edits. `python3 check.py drill` lists them,
`python3 check.py drill named` plays the drills for one command, and `python3 check.py drill named --show 2`
reveals a solution. Before each one, check.py explains the commands you'll need, and F1 inside Neovim
shows the same notes. Registers start empty in every drill, unless the task says one already holds
something.

| Keys | Does | Drills |
|---|---|---|
| `"a` … `"z` | named registers | 20 |
| `"0` | the yank register | 20 |
| `"_` | the black hole register | 20 |
| `Ctrl-r {r}` | insert a register while typing | 20 |
| `"A` … `"Z` | append to a named register | 6 |
| `"1` … `"9` | the delete history | 6 |
| `"-` | the small delete register | 6 |
| `Ctrl-r =` `"=` | the expression register: a calculator | 6 |
| `".` `"%` `":` `"/` | read-only registers | 6 |
| `Ctrl-r Ctrl-w` `Ctrl-r Ctrl-a` | the word under the cursor, on the command line | 6 |

## Stretch goals

1. **Read the registers.** In any file, make a few yanks and deletes (`yy`, `dd`, `dw`, `x`, `"ayiw`),
   then run `:reg`. Predict what's in `""`, `"0`, `"1`, `"-` and `"a` before you look.
2. **Browse the history.** Delete five lines one at a time with `dd`. Bring back the third one using
   `"1p` and `u.`, without counting.
3. **Beat par on exercise 6.** There's an 8-key solution using an Insert-mode key from Project 08.
   Try `:help i_CTRL-W`.
4. **Retire your calculator.** For the next week, every time you need a number in code, compute it
   with `Ctrl-r =`. Try `printf("%x", 255)` to get hex.
5. **Use the clipboard.** Copy a function to your browser with `"+yap` (or `"+y` in Visual mode), and
   paste a snippet from the browser with `"+p`. Then decide whether you want `clipboard=unnamedplus`.

## Check your understanding

- What does `"0p` do that `p` doesn't? When do they paste the same thing?
- You type `yiw` on `alpha`, then `ciw` on `beta` and type `gamma`. What's in `""`, `"0`, `"-` and `".`?
- Why doesn't `dw` show up in `"1`? Where does it go instead?
- Why does `"add` followed by `n.` `n.` leave only one line in register `a`, while `"Add` keeps all
  three?
- In a change you'll repeat with `.`, what's the difference between `Ctrl-r "` and `Ctrl-r -`?
- After `"=@a*2<CR>p`, you yank a different number into `a` and press `.`. What gets pasted?

## Cheat sheet

```
Use one      "{r}y  "{r}d  "{r}p    Insert/cmdline  Ctrl-r {r}    List  :reg    Clear  qaq
Unnamed ""   every d c s x y        Visual p swaps it      Visual P leaves it alone
Yank    "0   last plain yank        Black hole  "_d  "_c   (saves nothing)
Named   "a-"z  only when asked      "A-"Z append (and . keeps appending)
History "1-"9  deletes of a line+  "1p..  puts "1 "2 "3     "1pu.u.  browses them
Small   "-   deletes inside a line  Ctrl-r - re-reads the register on .
Read    ".  last insert   "%  file name   ":  last command line   "/  last search
Cmdline Ctrl-r Ctrl-w  word under cursor    Ctrl-r Ctrl-a  WORD under cursor
Math    Ctrl-r =6*7<CR> (Insert)   "=6*7<CR>p (Normal)   7/2.0  10%3  0xff  @a*@b
System  "+y  "+p   (the macOS clipboard)
```
