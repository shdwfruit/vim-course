# Project 08 · Insert and command-line mode: fix it without leaving

> **Stage 8 · Insert and command-line mode** · about 2 hours · 14 exercises

## What you'll learn

Insert mode isn't only for typing characters. It has a small toolkit of `Ctrl` keys: delete the last
word, fix the indent, run one Normal command, insert a register or a calculated value, complete a long
name or a whole line, and type characters that aren't on your keyboard. The command line (after `:`
and `/`) has the same keys, plus two ways to reuse what you typed before.

The idea is simple. **When you're already typing, fix it without leaving.** `Ctrl-w` and retyping a
word beats `<Esc>`, `b`, `cw`. And `Ctrl-n` beats typing `initializeConnectionPool` by hand.

Most of these keys work in both Insert mode and on the command line, so you learn them once.

## The keys you need

### Deleting while you type

| Key | Deletes |
|---|---|
| `Ctrl-h` | the character before the cursor (the same as Backspace) |
| `Ctrl-w` | the word before the cursor |
| `Ctrl-u` | everything before the cursor on this line, back to the indent (again: the indent too) |

They can delete text that was there before you started inserting, so **`A` then `Ctrl-w`** means
"retype the last word of the line": two keys, where `$ciw` takes four. If you've typed something, they
stop once at the point where you started inserting; press again to keep going. In Neovim, `Ctrl-w`
and `Ctrl-u` start a new undo step, so if you delete too much, `<Esc>u` brings it back.

**A common use: the comment leader.** In C, Java and similar languages, `o` on a `//` comment line
starts the new line with `// ` already typed, because the language settings ask Vim to continue
comments. When you wanted code, delete it without leaving Insert mode. `Ctrl-u` deletes everything
before the cursor back to the indent, so the `// ` goes and the indent stays (a second `Ctrl-u` would
take the indent too). `Ctrl-w` also deletes just the `// ` here.

### Indenting while you type

| Key | Does |
|---|---|
| `Ctrl-t` | add one `shiftwidth` of indent to the current line |
| `Ctrl-d` | remove one `shiftwidth` |
| `0 Ctrl-d` | remove all the indent (type `0`, then `Ctrl-d`) |

They work **from anywhere in the line**: the cursor can be at the end, after what you typed. `<Tab>`
only indents at the start of a line; in the middle it just inserts spaces there. And because the indent
change is part of the insert, **`.` repeats it** together with the text. `A,<C-t><Esc>` adds a comma
and indents, and `j.` does both on the next line.

### One Normal command: `Ctrl-o`

`Ctrl-o` runs one Normal-mode command, then puts you back in Insert mode.

| Keys | Does |
|---|---|
| `Ctrl-o t/` | jump to just before the next `/`, and keep typing there |
| `Ctrl-o $` / `Ctrl-o 0` | jump to the end / start of the line |
| `Ctrl-o D` | delete from the cursor to the end of the line |
| `Ctrl-o dw` | delete the next word |
| `Ctrl-o zz` | scroll so the cursor line is in the middle of the screen |

Compared with `<Esc>`, a motion and `i`, `Ctrl-o` saves the key that gets you back into Insert mode.
It also doesn't move the cursor one character to the left the way `<Esc>` does.

### Inserting registers and values: `Ctrl-r`

`Ctrl-r` followed by a register name inserts that register, right where you're typing.

| Keys | Inserts |
|---|---|
| `Ctrl-r "` | the last thing you yanked or deleted |
| `Ctrl-r 0` | the last thing you yanked |
| `Ctrl-r a` | register `a` |
| `Ctrl-r /` | the last search pattern |
| `Ctrl-r :` | the last command line |
| `Ctrl-r =` | the value of an expression you type, then `<CR>` |
| `Ctrl-a` | the text you typed in your previous Insert session (`Ctrl-@` does the same and leaves Insert mode) |

**`Ctrl-r =` is a calculator.** `Ctrl-r =` `37*41` `<CR>` inserts `1517`. Any Vim expression works:

| Expression | Inserts | Expression | Inserts |
|---|---|---|---|
| `7*24*3600` | `604800` | `0x1F` | `31` |
| `10/4` | `2` (whole numbers divide to a whole number) | `10/4.0` | `2.5` |
| `printf('%x', 255)` | `ff` | `repeat('-', 5)` | `-----` |
| `strftime('%Y-%m-%d')` | today's date | `line('.')` | the line number |

Project 05 covered registers in depth. `Ctrl-r` is how you use them without leaving Insert mode.

### Completion: `Ctrl-n`, `Ctrl-p`, `Ctrl-x Ctrl-l`

Type the start of a word and press **`Ctrl-n`**: Vim finishes it with a word that's already in the file.
It searches forward from the cursor (and around the end of the file), then other windows and buffers.
**`Ctrl-p`** searches backward first, so it finds the nearest match above. Press either again to step
through the other matches; a menu shows them when there's more than one.

| Keys | Completes |
|---|---|
| `Ctrl-n` / `Ctrl-p` | the word before the cursor: next / previous match |
| `Ctrl-x Ctrl-l` | the whole line: a line that starts with what you've typed (indent ignored) |
| `Ctrl-x Ctrl-f` | a file name |
| `Ctrl-y` | accept the match in the menu and stop completing |
| `Ctrl-e` | cancel: go back to what you typed |

Completion is the reason long names don't slow you down: `in` `Ctrl-n` can type
`initializeConnectionPool`. Two letters are usually enough. If the first match is wrong, press `Ctrl-n`
again or type one more letter. With `ignorecase` on, case is ignored here too, so `st` `Ctrl-n` can
complete `String`.

`Ctrl-x Ctrl-l` searches backward for a matching line and inserts all of it. Then you keep typing to
change what's different, like the `;` that becomes ` {` when you turn a C prototype into a function.
`Ctrl-p` and `Ctrl-n` step to older and newer matching lines.

The `complete` option decides where `Ctrl-n` looks. In these exercises it's set to your own file only,
so completion can't copy text out of the target window.

### Special characters: `Ctrl-v` and `Ctrl-k`

**`Ctrl-v` inserts the next key literally.** With `expandtab` on, `<Tab>` types spaces, but
`Ctrl-v <Tab>` is a real tab character, which TSV files need. (Makefiles need them too, but Neovim
already turns `expandtab` off in those.) `Ctrl-v` also takes a character code:

| Keys | Inserts |
|---|---|
| `Ctrl-v <Tab>` | a real tab |
| `Ctrl-v 065` | the character with decimal code 65: `A` |
| `Ctrl-v u2192` | Unicode U+2192: `→` (`u` then 4 hex digits) |
| `Ctrl-v U0001F600` | code points above FFFF (`U` then up to 8 hex digits) |

**`Ctrl-k` and two characters type a digraph**, an easy-to-remember name for a special character.
The names follow patterns: an accent goes after its letter (`'` acute, `!` grave, `>` circumflex,
`:` umlaut), `*` after a letter makes it Greek, and a box-drawing piece is named after the directions
its lines go (`d`own, `u`p, `l`eft, `r`ight, `h`orizontal, `v`ertical).

| Digraph | Gives | Digraph | Gives | Digraph | Gives |
|---|---|---|---|---|---|
| `->` `<-` | → ← | `e'` `e!` `e>` | é è ê | `hh` `vv` | ─ │ |
| `-!` `-v` | ↑ ↓ | `a:` `o:` `u:` | ä ö ü | `dr` `dl` | ┌ ┐ |
| `*X` `+-` | × ± | `n?` `c,` `ss` | ñ ç ß | `ur` `ul` | └ ┘ |
| `!=` `=<` `>=` | ≠ ≤ ≥ | `a*` `l*` `p*` | α λ π | `vr` `vl` | ├ ┤ |
| `DG` `00` `Eu` | ° ∞ € | `OK` `XX` | ✓ ✗ | `dh` `uh` `vh` | ┬ ┴ ┼ |

`:digraphs` lists them all, and `:help digraphs-default` explains the naming. `ga` in Normal mode shows the
code of the character under the cursor. Digraphs also work after `r`, `f` and `t`: `r` `Ctrl-k` `hh`
replaces a character with `─`.

With box-drawing digraphs plus counts (`8i` `Ctrl-k` `hh` `<Esc>` types eight `─`) and `.`, ASCII
art gets fast.

### The command line has the same keys, and more

On the command line (after `:`, `/` or `?`), `Ctrl-w`, `Ctrl-u`, `Ctrl-h`, `Ctrl-r {register}`,
`Ctrl-r =`, `Ctrl-v` and `Ctrl-k` all work as in Insert mode. A few keys are command-line only:

| Keys | Does |
|---|---|
| `Ctrl-r Ctrl-w` | insert the word under the cursor |
| `Ctrl-r Ctrl-a` | insert the WORD under the cursor (everything between spaces) |
| `Ctrl-r Ctrl-l` | insert the whole line under the cursor |
| `Ctrl-b` / `Ctrl-e` | jump to the start / end of the command line |
| `Ctrl-p` / `Ctrl-n` | recall the previous / next command from history |
| `Ctrl-f` | open the command-line window (below) with what you've typed so far |

`Ctrl-r Ctrl-w` is great in the replacement half of `:s`: with the cursor on the new name,
`:%s/oldName/` `Ctrl-r Ctrl-w` `<CR>` renames without typing the new name.

**Gotcha:** text from `Ctrl-r` goes into a pattern as is, so a `.`, `*` or `[` in it becomes regex.
Start the pattern with `\V` ("very nomagic") to match it literally: `:%s/\V` `Ctrl-r "` `/p/` replaces
a yanked `a[i].x` with `p`.

### The command-line window: `q:`

**`q:`** opens a window with your command history, one command per line, as ordinary text. Move and
edit with any Normal or Insert mode keys, then press **`<CR>`** to run the line under the cursor. The
cursor starts on the empty last line, so `k` takes you to your most recent command.

This is the way to rerun a long command with a change in the middle. On the command line you can only
edit comfortably at the end, but in the window, `fE` `cw` and `.` work like anywhere else. Leave
without running anything with `:q`, or press `Ctrl-c` to put the line under the cursor back on the
command line. `q/` does the same for your search history.

### Repeating commands: `@:`, `&`, `g&`

| Keys | Repeats |
|---|---|
| `@:` | the last command line, exactly as typed; `@@` repeats it again, and `3@:` three times |
| `&` | the last `:s`, on the cursor line (in Neovim with the same flags; it's mapped to `:&&`) |
| `g&` | the last `:s` on every line, with the same flags |
| `:&&` / `:&` | the last `:s` on the cursor line with / without its flags; takes a range |

`@:` repeats the range as typed too, and a relative range is measured from the cursor again. So after
`4:s/print/log/` (which became `:.,.+3s/print/log/`), moving down and pressing `@:` fixes the next four
lines. `.` doesn't repeat command-line commands at all, which is what `@:` is for.

## Your exercises

| # | Exercise | What it teaches |
|---|---|---|
| 1 | Replace the last word | `A` and `Ctrl-w` |
| 2 | Code after a comment | `Ctrl-u` to wipe the comment leader |
| 3 | Indent as you type | `Ctrl-t`, and why `.` repeats it |
| 4 | One Normal command | `Ctrl-o` |
| 5 | Do the math | `Ctrl-r =` as a calculator |
| 6 | Complete long names | `Ctrl-n` and `Ctrl-p` |
| 7 | Complete a whole line | `Ctrl-x Ctrl-l` |
| 8 | A real tab | `Ctrl-v` to insert a key literally |
| 9 | Draw a box | `Ctrl-k` digraphs, with counts and `.` |
| 10 | The word under the cursor | `Ctrl-r Ctrl-w` on the command line |
| 11 | Repeat an Ex command | `@:`, and relative ranges |
| 12 | Edit an old command | the command-line window, `q:` |
| 13 | Review · Finish the thumbnail tool | 00–08 mixed: `Ctrl-r =`, `r` with a digraph, `Ctrl-o`, `Ctrl-a` and `Ctrl-p` while typing |
| 14 | Review · Release notes | 00–08 mixed: `q:`, `A<C-w>`, digraphs, `Ctrl-x Ctrl-l`, `:g` |

## Run it

```bash
python3 check.py          # see the exercises and your progress
python3 check.py next     # play the first one you haven't solved
python3 check.py 4        # play exercise 4
python3 check.py --watch 4   # stuck after three tries? watch the reference solution
```

See "How an exercise works" in [`../ROADMAP.md`](../ROADMAP.md) for the scoring rules.

## Drills

Drills are short problems that practice one command at a time: 20 for each everyday command and 6 for each
rarer one, in Java, C, Python, shell, Markdown, CSS and plain text. `python3 check.py drill` lists them,
`python3 check.py drill 3` (or `drill ctrl-o`) plays one command's drills, and
`python3 check.py drill ctrl-o --show 4` reveals the solution to one. Each drill lists the commands it uses
before it starts, and F1 inside Neovim shows the same notes.

| Keys | What they do | Drills |
|---|---|---|
| `Ctrl-w` `Ctrl-u` `Ctrl-h` | delete while typing | 20 |
| `Ctrl-n` `Ctrl-p` | complete a word | 20 |
| `Ctrl-o {cmd}` | one Normal command without leaving Insert | 20 |
| `Ctrl-t` `Ctrl-d` | indent or unindent while typing | 6 |
| `Ctrl-x Ctrl-l` | complete a whole line | 6 |
| `Ctrl-k {a}{b}` | type special characters | 6 |
| `Ctrl-v {key}` | type a key literally | 6 |
| `q:` | edit command lines in a window | 6 |
| `@:` | repeat the last Ex command | 6 |
| `Ctrl-a` (Insert) | type the last insert again | 6 |
| `Ctrl-b` `Ctrl-e` `Ctrl-p` `Ctrl-n` | edit and recall command lines | 6 |

## Stretch goals

1. **The calculator, for real.** Insert the result of `37 * 41` without a calculator. Then insert
   today's date with `Ctrl-r =` and `strftime()`.
2. **`Ctrl-a`.** Type a long variable name in one insert. Leave Insert mode, move somewhere else, and
   start a different insert (`o`, `A`, `ci(`) that needs the same name: `Ctrl-a` types it again.
3. **A table in box-drawing characters.** Draw a 2×2 grid with `┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘`. Find the
   digraphs in the table above, or look up others with `:digraphs`.
4. **Search history.** Do three different searches, then open `q/`, edit the first one and run it.
5. **Use it for real.** Next time you notice a typo while typing, fix it with `Ctrl-w` instead of
   `<Esc>`. Next time `o` continues a comment you didn't want, use `Ctrl-w`.

## Check your understanding

- `Ctrl-w`, `Ctrl-u` and `Ctrl-h` all delete backward. How much does each one delete?
- After `A,<C-t><Esc>`, `j.` adds a comma *and* indents. After `A,<Esc>>>`, what does `j.` do, and why?
- When is `Ctrl-o` + a motion one key shorter than `<Esc>` + a motion + `i`? When is it the same?
- What does `Ctrl-r =` `10/4` `<CR>` insert, and how do you get `2.5` instead?
- You yank `arr[0].x` and run `:%s/<C-r>"/y/g`. Why might it not change `arr[0].x`, and what fixes it?
- `@:`, `&` and `.` all repeat something. What does each one repeat?

## Cheat sheet

```
Delete      Ctrl-h char   Ctrl-w word   Ctrl-u to start of line      (also on the command line)
Indent      Ctrl-t more   Ctrl-d less   0 Ctrl-d none                 part of the insert, so . repeats it
Normal      Ctrl-o {cmd}  one Normal command, then back to Insert: Ctrl-o t/   Ctrl-o D   Ctrl-o zz
Registers   Ctrl-r "  0  a  /  :  .     Ctrl-r = expression <CR>      Ctrl-a last insert again
Complete    Ctrl-n next word   Ctrl-p previous   Ctrl-x Ctrl-l line   Ctrl-x Ctrl-f file   Ctrl-y accept  Ctrl-e cancel
Literal     Ctrl-v <Tab> real tab   Ctrl-v u2192 →   Ctrl-v 065 A
Digraphs    Ctrl-k ->  →   e' é   hh ─  vv │  dr ┌  dl ┐  ur └  ul ┘  vh ┼      :digraphs   ga
Cmdline     Ctrl-r Ctrl-w word   Ctrl-r Ctrl-a WORD   Ctrl-r Ctrl-l line   Ctrl-b/Ctrl-e start/end   Ctrl-p/Ctrl-n history
Window      q: commands   q/ searches   Ctrl-f from the command line   <CR> runs the line   :q leaves
Repeat      @: last command line   @@ again   & last :s here (keeps flags)   g& last :s everywhere
```
