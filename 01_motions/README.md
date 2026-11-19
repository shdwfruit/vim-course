# Project 01 · Motions: get anywhere in a few keys

> **Stage 1 · Motions** · about 2–3 hours · 12 exercises

## What you'll learn

Project 00 gave you a handful of motions. This project gives you the rest, so you can **move by
meaning**: to the next comma, the matching bracket, the next blank line, the next use of this name,
the place you just came from. Counting characters with `l` and lines with `j` is the slow way.

And every motion you learn here is also a **noun**. Anything that moves the cursor can follow an
operator, and the operator acts on the text the cursor would pass over:

```
  operator   motion
     d       /map<CR>    → delete from here up to "map", even three lines down
     c       %           → change from this bracket to its partner
     y       G           → copy from this line to the end of the file
     d       }           → delete to the next blank line
```

So each new motion adds a whole row of new commands. That's the big idea of this project.

## The keys you need

### Words and WORDS

| Key | Moves to | Key | Moves to |
|---|---|---|---|
| `w` | start of the next word | `W` | start of the next WORD |
| `b` | start of this (or the previous) word | `B` | start of this (or the previous) WORD |
| `e` | end of this (or the next) word | `E` | end of this (or the next) WORD |
| `ge` | end of the previous word | `gE` | end of the previous WORD |

A **word** is a run of letters, digits and underscores, *or* a run of other punctuation. A **WORD** is
anything between spaces. In `a.b(c) d`, `w` stops on `.`, `b`, `(`, `c`, `)` and then `d`. `W` jumps
straight from `a` to `d`.

Use WORDs when the code is dense with punctuation: `color="red",` is one WORD but four words. An empty
line also counts as a word, so `w` stops on it.

Two things to know when you use them after an operator:

- **`dw` and `dW` stop at the end of a line.** If the last word the motion passes over is the last
  word on its line, the delete ends right there and the next line isn't pulled up. So you can't use
  `d5W` to delete up to a word at the start of a later line. Use a search for that (below).
- **`ge` is inclusive and `b` isn't** (more on that next). From the `t` of `three` in `one two three`,
  `db` deletes `two `, but `dge` deletes `o t`.

### Inclusive or exclusive: does the motion take the last character?

When an operator uses a motion, the text from the cursor to where the motion lands is affected. The
only question is whether the character at the far end is included.

| Kind | Motions | Example |
|---|---|---|
| **inclusive**: the far end is included | `e E ge gE f t $ %` | `df)` deletes the `)` too |
| **exclusive**: the far end is left alone | `w W b B F T 0 ^ / ? { }` and `` `a `` | `dt)` stops before the `)` |
| **line-wise**: whole lines | `j k G gg` and `'a` | `dG` deletes this line to the last line |

The rule worth remembering: **a backward motion never includes the character under the cursor.**
`dF.` deletes back to the previous `.` and keeps the character you're on. `db` keeps it too. That's
often exactly what you want, as exercise 3 shows.

One more rule, which makes `d}` useful: if an exclusive motion starts at or before the first
non-blank of a line and ends in column 1, the operator works on **whole lines** instead. So `d}` from
the start of a line deletes whole lines up to the next blank line.

### Line positions

| Key | Moves to | With an operator |
|---|---|---|
| `0` | column 1 | `d0` deletes back to column 1, indentation included |
| `^` | the first non-blank character | `c^` changes back to the indentation and keeps it |
| `$` | the end of the line | `d$` (or `D`) deletes to the end of the line |

`c^` is the one people forget: "replace everything on this line before the cursor, but keep the
indent." Exercise 2 uses it.

### Characters on the line: f t F T ; ,

You know `f` and `t` from Project 00. Here's the full set:

| Key | Moves to |
|---|---|
| `f{c}` / `F{c}` | onto the next / previous `{c}` on the line |
| `t{c}` / `T{c}` | just before the next `{c}` / just after the previous `{c}` |
| `;` | the last `f t F T` again, in the same direction |
| `,` | the last `f t F T` again, in the opposite direction |

- **Counts work:** `3f,` jumps to the third comma, `2F.` to the second dot back.
- **`,` reverses.** After `f,`, the `,` key goes back to the previous comma. After `F.`, `;` keeps going
  backward and `,` goes forward. Use it when `;` overshoots.
- **`;` after `t` moves on.** After `t,` the cursor sits just before a comma. Pressing `;` doesn't get
  stuck there: it jumps to just before the *next* comma.
- **They're all motions,** so they all work after operators: `dF.`, `cT"`, `y2t,`. Even `d;` works:
  after `f,`, `d;` deletes through the next comma.
- They never leave the current line. For anything farther away, search.

### Brackets: %

`%` jumps from a bracket to its partner: `(` and `)`, `[` and `]`, `{` and `}`. It counts nesting, so
from the last `)` in `(x - mean(xs)) / (stdev(xs) + 1e-9)` it skips `stdev(xs)` and lands on the `(`
that opens the group.

- **You don't have to be on a bracket.** If the cursor isn't on one, `%` looks forward on the line for
  the first bracket and jumps to *its* partner.
- **It's inclusive,** so `d%` and `c%` include both brackets.
- **In C it knows more pairs:** `/*` and `*/`, and `#if`, `#else`, `#endif`. Neovim also loads the
  matchit plugin, which makes `%` jump between an HTML tag like `<div>` and its `</div>`.
- **With a count it means a percentage:** `50%` goes to the line halfway through the file.

### Paragraphs: { }

`}` jumps forward to the next empty line, and `{` jumps back to the previous one. In code, blank lines
usually separate functions or blocks, so these hop from one to the next.

- **Empty means empty.** A line containing only spaces is *not* a paragraph boundary, so `}` goes
  straight past it.
- **As nouns they're line-wise** when you start at the beginning of a line (the rule above): `d}` from a
  blank line deletes that blank line and the whole block after it. `y}` copies them.
- **At the end of the file** there's no next blank line, so `}` goes to the end of the last line and
  `d}`/`y}` work character by character. Use `dG`/`yG` there instead.

### Lines: gg, G, :N

| Keys | Goes to |
|---|---|
| `gg` | the first line |
| `G` | the last line |
| `42G` or `42gg` or `:42<CR>` | line 42 |

Compilers report errors by line number (`main.c:42:5: error: ...`), and `42G` takes you straight there.
With relative numbers on, the current line still shows its real number.

- **In Neovim these keep the column.** Neovim turns the `startofline` option off, so `gg` from column 20
  lands in column 20 of line 1 (or at the end of the line, if it's shorter). In Vim they go to the
  first non-blank. Add `0` or `^` if you need the start of the line.
- **As nouns they're line-wise:** `dG` deletes from this line to the end of the file, `ygg` copies from
  here to the top, and `yG` from line 1 copies the whole file.

### Search: / ? n N

| Keys | Does |
|---|---|
| `/text<CR>` | search forward for `text` |
| `?text<CR>` | search backward |
| `n` / `N` | next match in the same / opposite direction as the last search |
| `/<CR>` | search forward again for the last pattern |

- **Searches wrap around** the end (or start) of the file, so `n` eventually comes back to where you
  started.
- **Case: `ignorecase` and `smartcase` are on.** A pattern in all lowercase ignores case: `/the` finds
  `the`, `The` and `THE`. A pattern with any capital letter matches case exactly: `/The` finds only
  `The`. Capitals are rare, so `?U<CR>` is often a one-letter way back to a word starting with U.
- **Make the pattern only as long as it needs to be.** It just has to reach the right spot first.
  `/m<CR>` is fine if the next `m` is the one you want.
- **Some characters are special** in a pattern: `.` matches any character, and `*`, `[`, `~`, `^`, `$`
  and `\` also mean something. To find a literal dot, search for `\.`.
- **Matches stay highlighted.** `Ctrl-l` clears the highlighting until your next search. `<Esc>`
  cancels a search you're typing.

**Search is the most powerful noun.** `d/map<CR>` deletes from the cursor up to (not including) the
next `map`, however many lines away it is. `c?if<CR>` changes back to the previous `if`. `y/}<CR>`
copies up to the next `}`. `dn` deletes up to the next match of the last search. Like `F`, a backward
search excludes the character under the cursor.

### The word under the cursor: * #

| Key | Does |
|---|---|
| `*` | search forward for the word under the cursor |
| `#` | search backward for it |
| `g*` / `g#` | the same, but also match it inside longer words |

`*` searches for the **whole word**: on `tmp`, it finds `tmp` but skips `tmpdir`. `g*` would stop at
`tmpdir` too. After `*`, `n` and `N` continue the search as usual.

One surprise: `*` and `#` use `ignorecase` but ignore `smartcase`, so `*` on `tmp` also matches `TMP`.

`*` is the dot formula's best friend. Change one occurrence, then `n.` changes the next one, and `n`
(skip) leaves one alone:

```
*            search for this name
cwsize<Esc>  change it
n.           next match, change it again
n.           and again (wrapping around the file if needed)
```

### Marks

A **mark** is a bookmark for a position in the file.

| Keys | Does |
|---|---|
| `ma` | set mark `a` at the cursor (any letter `a`–`z`) |
| `'a` | jump to the *line* of mark `a`, on its first non-blank |
| `` `a `` | jump to the *exact position* of mark `a` |
| `d'a`, `y'a`, `>'a` | act on whole lines, from this line to mark `a`'s line |
| `` d`a ``, `` y`a `` | act on characters, from the cursor to the mark (exclusive) |

Lowercase marks belong to one file. Uppercase marks (`mA`) work across files: `'A` opens the file the
mark is in. Marks move with their text when you add or delete lines above them. `:marks` lists them.

Vim also sets some marks for you:

| Mark | Is |
|---|---|
| ``` `` ``` or `''` | where you were before your latest jump. Press it again to go back. |
| `` `. `` | where you made the last change |
| `` `^ `` | where you last left Insert mode |
| `` `[ `` and `` `] `` | the start and end of the text you last changed, yanked or put |

Marks pay off in long files: mark the top of a function with `ma`, find its end with `%` or a search,
then `y'a` copies the whole thing, however long it is. The exercise files are short enough that a
count usually wins, so there's no exercise for named marks. Use them in your own code instead (see the
stretch goals). F5 clears all marks when it restarts an exercise.

### The jump list: Ctrl-o and Ctrl-i

Some motions are **jumps**: `G`, `gg`, `/`, `?`, `n`, `N`, `*`, `#`, `%`, `{`, `}`, and jumping to a
mark. Before each jump, Vim saves where you were in the window's **jump list**.

| Key | Does |
|---|---|
| `Ctrl-o` | go back to where you were before the last jump (older) |
| `Ctrl-i` or `Tab` | go forward again (newer) |

Small moves like `j`, `w` and `f` aren't jumps, and neither is `:42<CR>`, so they don't add entries.
`:jumps` shows the list.

This gives you a cheap round trip: jump somewhere to grab something, then `Ctrl-o` drops you back
exactly where you were, column included. That's exercise 10. (In Insert mode, `Ctrl-o` does something
different. Project 08 covers it.)

### The change list: `. g; gi

Vim also remembers where you made changes.

| Keys | Does |
|---|---|
| `` `. `` | jump to the last change |
| `g;` / `g,` | go to older / newer positions in the change list |
| `gi` | go back into Insert mode where you last left it |

`gi` is handy when you stop typing to look something up: go read the other function, then `gi` puts
you back in Insert mode at the exact spot, even if you made another change in between. `` `. `` would
take you to that later change instead.

### Every motion is a noun

Here's a sample of what you can now say, all with operators you already know:

| You want to | Keys |
|---|---|
| delete to the next blank line | `d}` |
| change a bracketed group, brackets included | `c%` (from either bracket) |
| delete back to the previous dot, keeping the one you're on | `dF.` |
| change back to the indentation | `c^` |
| copy from here to the end of the file | `yG` |
| delete up to the next `return`, lines away | `d/return<CR>` |
| delete up to the next match of the last search | `dn` |
| indent to the next blank line | `>}` |
| copy the WORD under the cursor (from its start) | `yE` |
| delete whole lines from here to mark `a` | `d'a` |

## Your exercises

| # | Exercise | What it teaches |
|---|---|---|
| 1 | Drop an argument | `W` vs `w`, and `dW` |
| 2 | Change back to the indent | `c^`: a backward motion that keeps indentation |
| 3 | Delete backward | `F`, and why backward motions don't take the cursor's character |
| 4 | Replace a bracketed group | `%` as a motion and as a noun |
| 5 | Repeat the whole pattern | `G` as a line-wise noun: `yG` |
| 6 | Move a function down | `}` to get there and `d}` to cut a block |
| 7 | Delete up to a word | search as a noun, across lines |
| 8 | Delete back to a comma | backward search as a noun |
| 9 | Rename a variable | `*`, `n` and `.` |
| 10 | Fetch and come back | the jump list: `Ctrl-o` |
| 11 | Review · Tidy a Java class | 00 and 01 mixed: `*` with `n.`, yanking code where it is, `d}` to move a method |
| 12 | Review · Clean up a ring buffer | 00 and 01 mixed: `%` and ``` `` ```, `}` between functions, one-character searches |

## Run it

```bash
python3 check.py          # see the exercises and your progress
python3 check.py next     # play the first one you haven't solved
python3 check.py 4        # play exercise 4
python3 check.py --watch 4   # stuck after three tries? watch the reference solution
```

See "How an exercise works" in [`../ROADMAP.md`](../ROADMAP.md) for the scoring rules.

## Drills

Drills are short problems that practice one command at a time, in different files and pairings: 20 for
each everyday command and 6 for each rarer one. Before each one starts, check.py lists the commands it
uses, and F1 inside Neovim shows those notes again.

```bash
python3 check.py drill             # every command and your drill progress
python3 check.py drill W           # the drills for W B E (a key or an id like bigword works)
python3 check.py drill W --show 3  # the reference solution for drill 3, explained
```

| Keys | What they do | Drills |
|---|---|---|
| `W B E` | move by WORDs (anything between spaces) | 20 |
| `0 ^ $` | line start, first non-blank, line end | 20 |
| `gg G {N}G` | first line, last line, line N | 20 |
| `%` | jump to the matching bracket | 20 |
| `{ }` | back or forward to a blank line | 20 |
| `/ ? n N` | search forward or backward | 20 |
| `* #` | search for the word under the cursor | 20 |
| `ge gE` | back to the end of the previous word | 6 |
| `` m{a} '{a} `{a} `` | set a mark and jump back to it | 6 |
| `Ctrl-o Ctrl-i` | back and forward through your jumps | 6 |
| ``` `. g; gi ``` | back to your last change or insert | 6 |

## Stretch goals

1. **Beat par on exercise 9.** Read `:help gn`. There's a way to make `.` find the next match by
   itself, which saves a key.
2. **Marks for real.** Open a long file of your own (100+ lines). Put `ma` on the first line of a
   function, find its last line with `%` or a search, and copy the function with `y'a`. Then scroll
   far away and come back with `` `a ``.
3. **Search offsets.** Read `:help search-offset`. What does `d/foo/e<CR>` delete that `d/foo<CR>`
   doesn't? Try it on a line of your own.
4. **Jump instead of scrolling.** For one coding session, use `*` to find the next use of a name, `%`
   to hop between braces, `42G` for compiler errors, and `Ctrl-o` to come back. Don't scroll at all.
5. **Try the failure.** In exercise 7, try `d16W` instead of a search. Explain what happens.

## Check your understanding

- `dF.` from a dot deletes back to the previous dot, but keeps the dot you're on. Why? Name two other
  motions that behave the same way.
- What's the difference between `'a` and `` `a ``? Between `d'a` and `` d`a ``?
- With `smartcase` on, what does `/the` match? `/The`? And `*` with the cursor on `The`?
- You press `G`, then `:5<CR>`, then `Ctrl-o`. Where does the cursor end up, and why not on line 5?
- `/tmp` and `*` on `tmp` both search for `tmp`. Which one stops at `tmpdir`, and why?
- `}` is an exclusive, character-wise motion. So why does `d}` from the blank line in exercise 6 delete
  whole lines?

## Cheat sheet

```
Words       w b e ge (words)     W B E gE (WORDS: anything between spaces)
Line        0 column 1    ^ first non-blank    $ end
Characters  f F t T {c}    ; repeat    , repeat backward          (counts work: 3f,)
Brackets    %  partner of ( [ { /* #if       50% = halfway through the file
Paragraphs  { }  previous / next empty line
Lines       gg first   G last   42G or :42 line 42             (Neovim keeps the column)
Search      /pat ?pat   n N   /<CR> again      * # whole word under cursor   g* g# partial
Marks       ma   'a line   `a exact    `` '' before last jump   `. last change   `[ `] last change/yank
Jumps       Ctrl-o back   Ctrl-i/Tab forward   (G gg / ? n N * # % { } and marks are jumps)
Changes     `. last change   g; g, older/newer   gi insert where you left off
Exclusive   w W b B F T 0 ^ / ? { } `a      Inclusive  e E ge f t $ %      Line-wise  j k G gg 'a
```
