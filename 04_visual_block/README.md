# Project 04 · Visual and block mode: rectangles, columns and ASCII art

> **Stage 4 · Visual and block mode** · about 2–3 hours · 14 exercises

## What you'll learn

So far every command has been "verb, then noun": `d` then `w`. Visual mode turns that around. You
**select first, see exactly what you've got, then act on it**. There are three kinds of selection:

```
 v  characters                 V  whole lines                Ctrl-v  a rectangle (block)

 int width  = 640;             int width  = 640;             int width  = 640;
            ^^^^^^             ^^^^^^^^^^^^^^^^^                 ^^^^^
 int height = 480;             int height = 480;             int height = 480;
 ^^^^^^^^^^^^                  ^^^^^^^^^^^^^^^^^                 ^^^^^
 int depth  = 32;              int depth  = 32;              int depth  = 32;
```

`v` and `V` mostly do what an operator + motion already does. **Block mode is the new power**: it
selects a column, which no motion or text object can name. With it you can add `- ` to twenty lines
at once, delete a column of pasted line numbers, change every `public` in a column to `private`, or
cut a picture out of some ASCII art and move it somewhere else.

## The keys you need

### The three Visual modes

| Key | Selects | Example |
|---|---|---|
| `v` | characters, from where you started to the cursor | `v3e` selects three words |
| `V` | whole lines | `Vj` selects this line and the next |
| `Ctrl-v` | a rectangle: these columns, on these lines | `Ctrl-v 3j` selects one column on four lines |

- **Any motion or text object grows the selection:** `vip` (the paragraph), `vi"`, `V}`, `Ctrl-v G`.
- **Press a different Visual key to switch modes** and keep the selection. Press the same key again,
  or `<Esc>`, to leave Visual mode.
- **Then press an operator** and it acts on the selection: `d c y > < = gq gc !`, and more below.

### What you can do to a selection

| Key | Does | Key | Does |
|---|---|---|---|
| `d` or `x` | delete | `U` | uppercase (not undo!) |
| `c` | change: delete, then insert | `u` | lowercase (not undo!) |
| `y` | yank (copy) | `~` | toggle case |
| `r{c}` | replace every selected character with `{c}` | `J` / `gJ` | join the selected lines |
| `>` / `<` | shift right / left | `3>` | shift three levels (in Normal mode, `3>>` means three *lines*) |
| `:` | an Ex command on the selected lines | `!` | filter the selected lines through a shell command |

`gU`, `gu` and `g~` work too, but in Visual mode `U`, `u` and `~` are the same thing in one key.

### Moving the ends: `o`, `O` and `gv`

| Key | Does |
|---|---|
| `o` | jump to the other end of the selection, so you can grow or shrink *that* end |
| `O` | in block mode: jump to the other corner on the same line (to move the left edge instead of the right) |
| `gv` | select the last selection again, in the same mode |

Say you're in the middle of a function and press `V}` to select down to its end. Now you see that
you also need the two lines above where you started: `o` moves the cursor to the top of the
selection, and `2k` grows it upwards. No need to start over.

`gv` is for doing a second thing to the same text. Most commands end Visual mode, but Vim remembers
the corners (in the marks `'<` and `'>`), so `gv` brings the selection back. For example, yank a
block with `y`, then `gv` and `r<Space>` blank it out.

### Block mode: `Ctrl-v`

A block is a rectangle: from the column where you started to the cursor's column, on every line in
between. These are the commands that make it worth learning:

| Keys | Does | Example |
|---|---|---|
| `I{text}<Esc>` | insert in front of the block, on every line | bullets: `Ctrl-v 3j I- <Esc>` |
| `A{text}<Esc>` | append after the block, on every line, padding short lines with spaces | a box's right edge |
| `$A{text}<Esc>` | `$` makes the right edge ragged, so `A` appends at each line's own end | semicolons |
| `c{text}<Esc>` | replace the block with `{text}` on every line | `public` → `private` |
| `r{c}` | fill the block with one character | `r#`, or `r` and a space to erase |
| `d` | delete the rectangle; text to its right moves left | strip line numbers |
| `y`, then `P` | copy the rectangle, then put it as a rectangle with its corner at the cursor | move part of a drawing |
| `>` | push the text from the block's left edge to the right by `'shiftwidth'` | open up a gap in a table |

Things to know:

- **What you type in `I`, `A` or `c` appears on the first line only, until `<Esc>`.** Then Vim
  copies it to the other lines. If you leave Insert mode with `Ctrl-c`, the copy doesn't happen.
- **`I` skips lines that are too short to reach the block's left edge.** A block in column 1 reaches
  every line, even blank ones: `Ctrl-v }` goes down to the blank line after a paragraph, and `I- `
  puts a `- ` on it too. `A` without `$` does the opposite: it pads short lines with spaces.
- **`G` keeps your column**, because `'startofline'` is off in Neovim. So `Ctrl-v G` selects the
  current column from here to the end of the file.
- **Text objects switch modes.** `Ctrl-v ip` becomes a line-wise selection. Use motions in block mode.
- **`.` repeats a block change on a block of the same size, at the cursor.** After
  `Ctrl-v 3j I| <Esc>`, moving to another column and pressing `.` inserts `| ` there on four lines.

### Past the end of the line: `'virtualedit'`

Normally the cursor can't go past the last character of a line. So `30|` stops at the end of a
short line, and you can't stretch a block out to a column that's past the end of the text. (`N|` is
the motion "go to column N".) The `'virtualedit'` option removes that limit:

| Setting | The cursor can go past the end of the line… |
|---|---|
| `:set virtualedit=` (the default) | never |
| `:set virtualedit=block` | in block mode only. Many people put this in their config. |
| `:set virtualedit=all` | everywhere, also in Normal mode. Your `:Art` command sets this. |

With it, `Ctrl-v` + `A` pads every line out to the column you picked, `P` can put a block in empty
space, and `r` can fill a rectangle where there was no text at all, which is how you draw a box
from nothing. Your `:Art` also sets `nolist` (so tabs and line ends aren't drawn as symbols) and
`nowrap` (so long lines don't wrap and bend your columns). Exercises 11 and 12 set `virtualedit`
for you.

### Numbers: `Ctrl-a` and `g Ctrl-a`

| Keys | On every selected line |
|---|---|
| `Ctrl-a` / `Ctrl-x` | add / subtract 1 (or the count) to the first number |
| `g Ctrl-a` | add 1 on the first line, 2 on the second, 3 on the third… |
| `4 g Ctrl-a` | add 4, 8, 12…: `0x00 0x00 0x00 0x00` becomes `0x00 0x04 0x08 0x0c` if you leave the first line out |

The classic use is numbering a list: write `0.` on every line, then `VG g Ctrl-a` turns them into
`1.`, `2.`, `3.`. In block mode, only numbers inside the block's columns count, so you can pick
which number on the line changes.

### Ex commands on a selection: `:'<,'>`

Press `:` in Visual mode and Vim starts the command line with `:'<,'>`, "from the first selected
line to the last". Whatever you type runs on those lines only:

```
:'<,'>sort               sort the selected lines
:'<,'>s/old/new/g        replace only in the selection (Project 07)
:'<,'>center 30          center each line in 30 columns; also :'<,'>right 30 and :'<,'>left
:'<,'>normal A;          run Normal-mode keys on each line (Projects 06 and 07)
```

The range is always whole lines, even from `v` or `Ctrl-v`. And `!` in Visual mode works like
`!{motion}` from Project 03: `vip!sort<CR>` is the same as `!ipsort<CR>`.

### When Visual mode is the right tool

Prefer **operator + motion** whenever you can name the text. It's shorter (no `v` to press), and
`.` repeats the *meaning* of the command, not its size:

```
gUi"   then  .   on another string   →  uppercases the whole new string
vi"U   then  .   on another string   →  uppercases as many characters as the first string had
```

Use **Visual mode** when:

1. **It's a column or a rectangle.** Nothing else can name it. This is block mode's job.
2. **There's no single motion for it,** or you want to see the text before a big change.
3. **You want to do two things to the same text.** `gv` reselects it for free.
4. **The command only exists in Visual mode:** `g Ctrl-a`, block `I` and `A`, `J` on a paragraph you
   didn't count.

## Your exercises

| # | Exercise | What it teaches |
|---|---|---|
| 1 | Make a bulleted list | block `I` |
| 2 | Semicolons on ragged lines | block `$A` |
| 3 | Delete a column | block `d`, and `G` keeping the column |
| 4 | Charge the battery | block `r` |
| 5 | Uppercase a column | `U` on a block |
| 6 | Count up the indexes | `V` and `g Ctrl-a` |
| 7 | Change a column | block `c` |
| 8 | Make a pipe table | block `I`, then `.` in another column |
| 9 | Quote a list | `gv` to reuse a block, `I` then `$A` |
| 10 | Center a banner | `:'<,'>` with an Ex command |
| 11 | Close the box | block `A` with `virtualedit=block` |
| 12 | Move the sun | block `y`, `gv`, `r`, `P` with `virtualedit=all` |
| 13 | Review · Make a value class | 00–04 mixed: `*` + `n` + `.`, block `c`, `I` and `d`, `gv` + `U`, `O` + `.` |
| 14 | Review · Lay out release notes | 00–04 mixed: `:ce`, `:ri`, `yyp` + `Vr=`, `gq`, `g Ctrl-a` then `gv` + `I`, `R` |

## Run it

```bash
python3 check.py          # see the exercises and your progress
python3 check.py next     # play the first one you haven't solved
python3 check.py 8        # play exercise 8
python3 check.py --watch 8   # stuck after three tries? watch the reference solution
```

See "How an exercise works" in [`../ROADMAP.md`](../ROADMAP.md) for the scoring rules.

## Drills

Drills are short practice problems, each about one command, in different files and pairings: 20 for each
common command and 6 for each rarer one. They're graded like the exercises. `python3 check.py drill` lists
them with your progress, `python3 check.py drill block-insert` plays one command's drills (`drill I` works
too), and `python3 check.py drill block-insert --show 3` reveals a reference solution. Press F1 inside Neovim
for notes on the commands a drill uses.

| Keys | What they do | Drills |
|---|---|---|
| `v` | select characters | 20 |
| `V` | select whole lines | 20 |
| `Ctrl-v` `I` `A` `$A` | type on many lines at once | 20 |
| `Ctrl-v` `c` `r` `d` `y` | change, fill, delete or copy a rectangle | 20 |
| `o` `O` `gv` | move the other end, or reselect | 6 |
| `g Ctrl-a` | number lines 1, 2, 3… | 6 |
| `:'<,'>` | run an Ex command on the selected lines | 6 |
| `virtualedit` `{N}\|` | edit past line ends, jump to column N | 6 |

## Stretch goals

1. **Set it for real.** Add `vim.opt.virtualedit = "block"` to your own `init.lua`. Your `:Art`
   command still switches to `all` when you're drawing.
2. **Draw a box from nothing.** Open an empty buffer, run `:Art`, and draw a 20×5 box using only
   block `r`: one block for each side, then the four `+` corners. Then put a title inside it.
3. **Practise `o` and `O`.** Select a block in the middle of some lines, then use `o` and `O` to
   visit all four corners, and grow the block in each direction.
4. **BASIC line numbers.** Write `0 PRINT "HI"` on 10 lines and turn the numbers into 10, 20, 30, …,
   100 with a single counted `g Ctrl-a`. (Hint: the first line has to change too.)
5. **Combine projects.** Take a whitespace-separated table, line it up with Project 03's
   `!ipcolumn -t`, then turn it into a pipe table with block `I` and `.`.

## Check your understanding

- After `vi"U`, why doesn't `.` on a longer string uppercase all of it, when `.` after `gUi"` does?
- What's the difference between `A` and `$A` on a block over lines of different lengths?
- Why did `Ctrl-v }` + `I- ` put a `- ` on the blank line below the list?
- When does `gv` save keys, compared with selecting the same block again?
- In ASCII art, why is block `r` and a space often better than block `d`?
- What can you do with `virtualedit=block` that you can't do without it?
- You press `:` with a block selected in the middle of three lines. Which text does `:'<,'>sort` sort?

## Cheat sheet

```
Modes      v chars   V lines   Ctrl-v block      same key or <Esc> leaves   other key switches
Ends       o other end   O other corner (block)   gv reselect last   '< '> first/last line
Act        d x c y r{c} > < = J gJ   U u ~ (case)   : → :'<,'>   ! filter   gc comment   gq wrap
Block      I{text}<Esc> before   A{text}<Esc> after (pads)   $A at each line end   c replace
           r{c} fill   d delete (text moves left)   y + P paste a rectangle   . repeats at cursor
Numbers    Ctrl-a / Ctrl-x every line   g Ctrl-a 1,2,3…   4 g Ctrl-a 4,8,12…
Past EOL   :set virtualedit=block (block mode)   =all (everywhere, like :Art)   N| column N
Rule       can you name it with a motion? use operator + motion. a column? use Ctrl-v.
```
