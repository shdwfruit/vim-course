# Project 00 · The grammar: verbs, counts, and the dot

> **Stage 0 · The grammar** · about 1–2 hours · 13 exercises

## What you'll learn

Vim commands aren't a list of shortcuts to memorize. They're **sentences** with a small grammar:

```
  [count]  operator  [count]  motion
           verb               noun
     2       d          3        w        → delete 6 words
```

Learn ten verbs and twenty nouns and you know two hundred commands, because every verb works with every
noun. Then one key, `.`, repeats the last sentence. This project is the foundation for everything
after it, so even if some of it is familiar, do every exercise: par is often lower than you'd guess.

## The keys you need

### Verbs (operators)

An operator does nothing until you tell it *what* to act on.

| Operator | Does | Example |
|---|---|---|
| `d` | delete (and save the text so you can paste it) | `dw` deletes to the start of the next word |
| `c` | change: delete, then start Insert mode | `cw` changes the rest of the word |
| `y` | yank (copy) | `y$` copies to the end of the line |
| `>` / `<` | indent / unindent lines | `>j` indents this line and the next |

Project 03 adds `=`, `gu`, `gU`, `gq`, `!` and `gc`. They follow exactly the same grammar.

**Double an operator to act on the whole line:** `dd` deletes the line, `cc` changes it, `yy` copies it,
`>>` indents it. With a count, `3dd` deletes three lines.

### Nouns (motions)

Every motion moves the cursor on its own, and also works as the noun after an operator.

| Motion | Moves to | Motion | Moves to |
|---|---|---|---|
| `w` / `b` | start of next / previous word | `0` | first column |
| `e` | end of the word | `^` | first non-blank character |
| `W` `B` `E` | the same, by WORD (anything between spaces) | `$` | end of the line |
| `f{c}` / `F{c}` | onto the next / previous `{c}` on the line | `j` / `k` | down / up a line |
| `t{c}` / `T{c}` | just before / just after the next / previous `{c}` | `gg` / `G` | first / last line |
| `;` / `,` | repeat the last `f t F T` forward / backward | `{N}G` | line N |

A **word** is letters, digits and underscores, or a run of punctuation: `os.environ["X"]` is six words
(`os`, `.`, `environ`, `["`, `X`, `"]`). A **WORD** is anything between spaces: the same text is one WORD.

**Where a motion stops matters for operators.** `dw` deletes up to the start of the next word, so it
takes the space with it. `de` deletes to the end of this word and leaves the space. `dt)` deletes up to
the `)`, and `df)` deletes the `)` too. `j` and `k` are *line-wise*: `dj` deletes two whole lines,
however far along the line the cursor is.

### Counts

A count repeats a motion or a whole command. Counts multiply: `2d3w` deletes six words.

| Keys | Does |
|---|---|
| `3w` | move three words forward |
| `d3w` or `3dw` | delete three words |
| `2f,` | jump to the second comma |
| `5J` | join five lines |
| `3ix<Esc>` | insert `xxx`: counts work on inserts too, and the repeat happens when you press `<Esc>` |

With `relativenumber` on, the number next to each line is exactly the count you need for `j` or `k`.

### Shortcuts for common sentences

These single keys are abbreviations. Each one is still a change that `.` can repeat.

| Key | Same as | Does |
|---|---|---|
| `x` | `dl` | delete the character under the cursor |
| `X` | `dh` | delete the character before the cursor |
| `s` | `cl` | change one character |
| `S` | `cc` | change the whole line |
| `D` | `d$` | delete to the end of the line |
| `C` | `c$` | change to the end of the line |
| `Y` | `y$` | copy to the end of the line (in Neovim; in Vim, `Y` copies the whole line) |

### Inserting and replacing

| Key | Starts Insert mode | Key | Does |
|---|---|---|---|
| `i` / `a` | before / after the cursor | `r{c}` | replace one character with `{c}`, and stay in Normal mode |
| `I` / `A` | at the start / end of the line | `R` | Replace mode: overwrite as you type |
| `o` / `O` | on a new line below / above | `J` | join the next line onto this one, with one space |

### Putting, undoing

`p` puts (pastes) after the cursor and `P` before it. What you deleted or yanked line-wise (`dd`, `yy`)
goes on a new line below (`p`) or above (`P`), so **`ddp` swaps two lines** and **`xp` swaps two
characters**. `u` undoes, `Ctrl-r` redoes.

### The dot command

`.` repeats the last **change**: everything from the operator to the end of the text you typed. Motions
aren't changes, so `.` never repeats a motion, only the edit.

That suggests a rhythm called **the dot formula: one key to move, one key to repeat.**

```
A;<Esc>   add a semicolon to this line (one change)
j.        down a line, add another
j.        and another
```

`A;<Esc>` beats `$a;<Esc>` here. Both add the semicolon, but `A` includes "go to the end of the line" in
the change, so `.` repeats it correctly on lines of any length.

`;` is the dot command for `f`/`t`: it repeats the last character jump. Combined: `f,` jumps to a comma,
`a <Esc>` adds a space after it, then `;.;.;.` does the next three commas.

### Getting help

`:help {key}` explains any command: `:help w`, `:help J`, `:help .`. Inside help, `Ctrl-]` follows a link
and `Ctrl-o` comes back. `:help motion.txt` lists every motion.

## Your exercises

| # | Exercise | What it teaches |
|---|---|---|
| 1 | Delete three words | `f`, and a count on an operator |
| 2 | Fix the operator | `r`: replace a character without entering Insert mode |
| 3 | Swap two letters | `xp`, the swap idiom |
| 4 | Move a line down | `ddp`, and how line-wise puts work |
| 5 | Change the rest of the line | counted `w`, and `C` |
| 6 | Delete up to a character | `dt` with a count |
| 7 | Add the missing semicolons | `A` and the dot formula |
| 8 | Indent the function body | an operator with a line-wise motion |
| 9 | Join an array onto one line | `J` with a count |
| 10 | Space after every comma | `f`, `;` and `.` together |
| 11 | Underline a heading | counts on inserts |
| 12 | Review · Fix a word-count script | all of Project 00 in 13 edits: `A`, `R`, `ct_` + `.`, `xp`, `3J` |
| 13 | Review · Tidy a README | all of Project 00 on prose: `>` with a motion, counted inserts, `.` with a new count |

## Run it

```bash
python3 check.py          # see the exercises and your progress
python3 check.py next     # play the first one you haven't solved
python3 check.py 4        # play exercise 4
python3 check.py --watch 4   # stuck after three tries? watch the reference solution
```

See "How an exercise works" in [`../ROADMAP.md`](../ROADMAP.md) for the scoring rules.

## Drills

Drills are short extra problems that practice one command at a time, in different files and pairings,
from its simplest form to small realistic edits. This project has the most: everything else in the course
is built from these keys. `python3 check.py drill` lists them, `python3 check.py drill f` plays the
drills for one command, and `python3 check.py drill f --show 2` reveals a solution. Before each one,
check.py explains the commands you'll need, and F1 inside Neovim shows the same notes.

A good order is the one listed: typing and moving first, then the verbs. If a command in an exercise is
new to you, do its drills first.

| Keys | Does | Drills |
|---|---|---|
| `i` `a` `I` `A` | start typing: before, after, at the line's start or end | 20 |
| `o` `O` | open a new line below or above | 20 |
| `x` `X` | delete a character | 20 |
| `r{c}` | replace one character | 20 |
| `w` `b` `e` | move by words | 20 |
| `f{c}` `F{c}` | find a character on the line | 20 |
| `t{c}` `T{c}` | move till a character | 20 |
| `;` `,` | repeat the last f, t, F or T | 20 |
| `{N}` | counts: do it N times | 20 |
| `d{motion}` `D` | delete | 20 |
| `dd` | delete whole lines | 20 |
| `c{motion}` `C` `cc` `s` `S` | change: delete, then type | 20 |
| `y{motion}` `yy` `Y` | yank (copy) | 20 |
| `p` `P` | put (paste) | 20 |
| `.` | repeat the last change | 20 |
| `>` `<` `>>` `<<` | shift lines right or left | 20 |
| `J` | join lines | 20 |
| `R` | Replace mode: type over text | 6 |

## Stretch goals

1. **Two ways.** For each exercise, find a second solution that's within one key of par. For example,
   exercise 11 has two different 6-key solutions.
2. **Beat par on exercise 10.** It's possible with an Ex command you'll meet in Project 07. Try
   `:help :s` and see if you can find it now.
3. **Feel the difference.** In any file, try `dw`, `de` and `db` on the same word, then `dt)` vs `df)`.
   Predict the result before each one.
4. **Use `.` for real.** In your next coding session, use `.` at least ten times. Each time you make the
   same change twice, ask whether the first one could have been repeatable.

## Check your understanding

- `dw` and `de` both delete "one word." When do they give different results, and why?
- Why does `A;<Esc>` + `j.` work on lines of different lengths, when `$a;<Esc>` + `j.` doesn't?
- What does `3.` do right after `dw`?
- `cw` is a famous special case: it acts like `ce`, not like `dw` followed by Insert mode. Try it on a
  word followed by a space. Why do you think Vim behaves this way? (`:help cw`)
- `xp` swaps two characters and `ddp` swaps two lines. Why is it the same idea both times?

## Cheat sheet

```
Operators   d delete   c change   y yank   > indent   < unindent        doubled (dd cc yy >>) = whole line
Motions     w b e  W B E  0 ^ $  f F t T ; ,  j k  gg G {N}G
Shortcuts   x=dl  X=dh  s=cl  S=cc  D=d$  C=c$  Y=y$
Insert      i a  I A  o O        Replace   r{c}  R        Join  J
Put/undo    p P   u  Ctrl-r      Repeat    .  (last change)   ;  (last f/t)
```
