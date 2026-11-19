# Project 06 · Macros: record once, replay a thousand times

> **Stage 6 · Macros** · about 3 hours · 13 exercises

## What you'll learn

`.` repeats one change. A **macro** repeats anything: a whole sequence of motions, edits and searches,
recorded once and stored in a register. Record yourself turning one line of CSV into code, and you can
convert the other 500 lines with five keys: `499@a`.

```
  qa                 start recording into register a
  I("<Esc>f,s", <Esc>A),<Esc>j     edit one line, move to the next
  q                  stop recording
  14@a               play it 14 more times
```

The skill isn't the recording, it's writing a macro that works on **every** line, not just the one
you recorded it on. In these exercises, keys typed by a playing macro don't count, only the keys you
type yourself. So the pars reward automation: a good macro plus a count beats any amount of careful
hand editing.

## The keys you need

### Recording and playing

| Keys | Does |
|---|---|
| `qa` | start recording into register `a` (any of `a`–`z`). The bottom line shows `recording @a`. |
| `q` | stop recording |
| `@a` | play the macro in register `a` |
| `Q` | play the macro you *recorded* last (Neovim only), in one key |
| `@@` | play the macro you *played* last, again |
| `14Q` `14@a` | play it 14 times (`@@` and `Q` take a count too) |
| `u` | undo a whole macro run in one step, even `14Q` |

`Q` and `@@` are not the same. `Q` always plays the register you recorded into last; `@@` repeats
whichever register you played last. Record macro `a`, then macro `b`: now `Q` plays `b`, so to play
`a` you type `@a`, and after that `@@` plays `a` again while `Q` still plays `b`. Most of the time you
record one macro and play it straight away, and then `Q` is the shortest way: `qa … q`, then `Q` or
`14Q`. `Q` plays what the register holds now, so it also picks up keys added with `qA` (below). It
doesn't help with a macro you only yanked into a register (`"ay$`): nothing was recorded, so play
that one with `@a`.

A good habit: record on the first line, test with `Q` on the second, look at the result, and only
then use a count.

### Writing a macro that works on every line

A macro replays your exact keys, so `5l` means "five characters right" on every line, whether or not
that's where the comma is. Make each part of the macro adapt to the line:

1. **Start from a known position.** Begin with `0`, `^` or `$`, or a search like `/printf<CR>` that
   jumps to the next target. Then it doesn't matter where the last run left the cursor.
2. **Move by meaning.** Use `f,`, `t)`, `$`, `b`, `e`, `%` and text objects. Avoid `l`, `h` and
   counted `w`: a type like `Map<String, Integer>` is six words, `int` is one.
3. **Prefer `I` and `A`** to "move, then `i`". They work on any line length.
4. **End by moving to the next target:** `j`, `+`, or a search. Then the next `@a` starts in the right
   place.

### When a macro stops

If any key in a macro fails (an `f,` that finds no comma, `j` on the last line, a search with no match,
`Ctrl-a` on a line with no number), the macro stops right there. With a count, the remaining runs are
cancelled too. That's a feature: `99@a` is a safe way to say "until it fails", **as long as the macro
fails before it changes anything.** Put the motion that can fail first: a macro starting with `0f=`
does nothing at all on a line without `=`. A macro starting with `I{ ` changes the line before
anything can fail, so overshooting the count mangles the next line.

### Recursive macros

A macro can call itself: end it with `@a`, and it repeats until something fails.

```
qaq                          empty register a (record nothing into it)
qa0f=a"<Esc>A",<Esc>j@aq     record one row, move down, call a, stop recording
Q                            run it (or @a): it keeps going until 0f= fails
```

Clear the register first. While you record, the `@a` inside runs whatever `a` held before. If `a` is
empty it does nothing, which is what you want. If `a` holds an old macro, that old macro runs in the
middle of your recording. (Every attempt in this course starts with empty registers, but in your own
Neovim, registers survive restarts.)

A big count does the same job: `99@a` also stops at the first failure. Recursion's advantage is that
you never count, and the macro is a complete "do the rest of the file" command you can rerun.

### Running a macro over lines: `:normal`

`:normal {keys}` runs Normal-mode keys from the command line, once for each line in a range, with the
cursor starting in column 1 of each line:

| Command | Runs macro `a` on |
|---|---|
| `:%normal @a` | every line in the file |
| `:5,12normal @a` | lines 5 to 12 |
| `:'<,'>normal @a` | the lines of the Visual selection (press `:` in Visual mode and `'<,'>` is typed for you) |
| `:g/printf/normal @a` | every line containing `printf` |

Two differences from a count. First, the macro doesn't need to start with `0` or end with `j`, because
`:normal` puts the cursor on each line for you. Second, **a failure only skips that line**, and
`:normal` carries on with the next one. That makes "fail first" a filter: rows the macro fails on are
left alone.

**Gotcha:** if the macro adds or deletes lines, `:5,12normal` still visits lines 5, 6, 7 … by number,
so it lands on the lines the macro just made. `:g` marks the matching lines first and then visits
them, wherever they move, so use `:g` for macros that change the number of lines.

`Q` works here too: `:%norm Q` plays the macro you recorded last on every line.

`:normal` also takes keys directly, without a macro: `:%norm A;` adds a semicolon to every line. An
unfinished Insert is ended for you, but an `<Esc>` in the middle has to be typed as `Ctrl-v <Esc>`.

### Changing a macro

**Append with `qA`.** Recording into `A` (uppercase) adds keys to the end of macro `a`, just like `"A`
appends to a register. The new keys run after the old last key, so if the macro ends with `j`, the
added keys will run on the next line. Record macros that *start* with the move (`j`, then edit) when you
expect to extend them.

**Edit it as text.** A macro is just text in a register, so you can paste it, fix it and yank it back:

```
"ap      paste macro a on an empty line: I("^[f,s", ^[A),^[j
         ^[ is <Esc>, ^M is <Enter>, ^R is Ctrl-r
...      fix it with normal edits
0"ay$    yank the line back into a, without the line break
dd       delete the line
```

Use `0"ay$`, not `"ayy`: a line-wise yank keeps the line break, and when the macro plays, that line
break moves the cursor down a line like an extra `j`. You can also set a macro directly:
`:let @a = "A;\<Esc>j"` (in double quotes, `\<Esc>` means the Esc key).

**Any register is a macro.** `@0` plays your last yank, and `@:` repeats your last `:` command
(Project 08). Macros live in the same registers as yanked text, so `"ayy` overwrites macro `a`. Keep
macros and clipboards in different letters.

### Numbering with `Ctrl-a`

`Ctrl-a` adds 1 to the number at or after the cursor, and `Ctrl-x` subtracts 1. With a count, `5 Ctrl-a`
adds 5. It understands hex (`0x0c` becomes `0x10`). Inside a macro it's a counter:

```
qayyp<C-a>q     on item_1: copy the line, add 1 to its first number (item_2)
9@a             nine more copies: item_3 ... item_11
```

Each run copies the line the last run made, so the numbers climb.

### Registers inside a macro

A macro replays keys, not results. `Ctrl-r 0` in a macro inserts whatever is in `"0` *when it plays*,
so a macro can yank something from each line and paste it elsewhere on the same line: `yiw`, then later
`Ctrl-r 0`. Use `Ctrl-r 0` rather than `Ctrl-r "` if the macro deletes anything in between (Project 05).

## Your exercises

| # | Exercise | What it teaches |
|---|---|---|
| 1 | Record once, replay | `qa` … `q`, then `Q` (or `@a` and `@@`) |
| 2 | Fifteen rows at once | ending with `j`, and a count: `14Q` |
| 3 | Grow the tree | macros that make new lines |
| 4 | Number the pins | `Ctrl-a` inside a macro |
| 5 | Any line, any shape | robust macros: `$`, `b` and `S` instead of counting words |
| 6 | Let the macro find its target | starting a macro with a search |
| 7 | A macro that calls itself | recursive macros, and `qaq` |
| 8 | Fix a macro as text | reading and editing a macro, and playing any register |
| 9 | Skip the rows that don't fit | `:%normal @a`, and "fail first" as a filter |
| 10 | Add a step to the macro | appending with `qA` |
| 11 | CSV to Java | everything together: yank, `gU` and `Ctrl-r 0` in one macro |
| 12 | Review · Name every error code | 00–06 mixed: `yi{` and a macro with a count, `gu`, `Ctrl-a`, a block `I` |
| 13 | Review · Seed the test database | 00–06 mixed: a counter macro, `gUi'`, `d/;`, `V"0p` |

## Run it

```bash
python3 check.py          # see the exercises and your progress
python3 check.py next     # play the first one you haven't solved
python3 check.py 4        # play exercise 4
python3 check.py --watch 4   # stuck after three tries? watch the reference solution
```

See "How an exercise works" in [`../ROADMAP.md`](../ROADMAP.md) for the scoring rules. Only the keys
you type count, so `14@a` costs four keys however much the macro does.

## Drills

Drills are short extra problems that practice one macro skill at a time, on Java, C, Python, CSV, logs,
Markdown and a bit of ASCII art: recording a macro that works on every line, replaying it, running it with
`:norm`, and fixing or extending it. `python3 check.py drill` lists them, `python3 check.py drill replay`
plays the drills for one command, and `python3 check.py drill replay --show 2` reveals a solution. Before
each one, check.py explains the commands you'll need, and F1 inside Neovim shows the same notes. As in the
exercises, recording keys count (`q`, the letter and the closing `q`), and registers start empty.

| Keys | Does | Drills |
|---|---|---|
| `q{r}` `@{r}` | record and play a macro | 20 |
| `@@` `Q` `{N}@{r}` | play a macro again, or N times | 20 |
| `:norm @{r}` | run a macro on every line of a range | 20 |
| `qaq … @aq` | a macro that calls itself | 6 |
| `qA` | add keys to the end of a macro | 6 |
| `"ap … "ay$` | edit a macro as text | 6 |
| `yyp Ctrl-a` | macros that count | 6 |

## Stretch goals

1. **The roadmap test.** Make a CSV file with 30 rows (or grab one from a class), and turn it into 30
   lines of Java, C or Python with one macro. Time yourself, then do it again tomorrow.
2. **Read your macros.** After exercise 5, paste macro `a` with `"ap` and read it. Can you predict what
   each key does on the `List<String>` line?
3. **Break it on purpose.** In exercise 2, run `16@a` instead of `14@a` and look at the `};` line.
   Then rewrite the macro so it fails before changing anything, and `99@a` is safe.
4. **Beat par on exercise 9** with a search inside the macro instead of `:normal`. Which version
   would you trust on a 5000-line file?
5. **Use a macro for real.** The next time you write the same kind of line three times in your own
   code (getters, test cases, switch cases), stop and record a macro instead.

## Check your understanding

- Why is `0f,` a safer start for a macro than `f,`?
- A macro ends with `j`. You append `A;<Esc>` to it with `qA`. Which line gets the semicolon?
- Why does `99@a` sometimes ruin the line after your data, and how do you write a macro so it never
  does?
- What's the difference between `14@a` and `:%normal @a` when the macro fails on line 6?
- You paste a macro with `"ap`, fix it, and yank it back with `"ayy`. What goes wrong when you play it?
- During `qa … @a q`, what does the `@a` do, and why must you run `qaq` first?

## Cheat sheet

```
Record    qa ... q          Play  @a   last recorded  Q   last played  @@   count  14Q  14@a   Undo  u
Robust    start with 0 ^ $ or /pat<CR>    move with f t $ b e %    end with j + or /pat<CR>
Stops     at the first failing key (and cancels the rest of a count): make it fail first
Recurse   qaq  then  qa ... @aq  then  Q or @a      (or just 99Q)
Ranges    :%norm @a   :%norm Q   :5,12norm @a   :'<,'>norm @a   :g/pat/norm @a   (a failure skips a line)
Append    qA ... q          Edit  "ap  fix  0"ay$  dd       Set  :let @a = "A;\<Esc>j"
Counters  yyp Ctrl-a        Ctrl-a / Ctrl-x add / subtract (hex too)     Any register  @0  @:
```
