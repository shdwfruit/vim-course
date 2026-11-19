# Project 09 · Many files: buffers, windows, and project-wide changes

> **Stage 9 · Many files** · about 2–3 hours · 13 exercises

## What you'll learn

Every project so far had one file. Real code doesn't: a C function lives in a `.h` and a `.c` file and is
called from five others. This project teaches you to work across files without leaving Neovim:

- **Getting around:** open a file, jump back, switch between open files by name, and follow an
  `#include` or `import` straight to the file it names.
- **Seeing two files at once:** split the screen into windows and move between them.
- **Changing many files with one command:** pick a set of files (by glob, by what's open, or by what a
  search found), then run a command in every one of them.

The big idea is the last one. `:vimgrep` searches the whole project and collects every match in the
**quickfix list**. `:cdo` then runs a command at every match. Together they're a project-wide find and
replace with the full power of `:s`, `:normal` and the dot command.

**How these exercises look:** most exercises here have several files, so there's no target window. The
task at the top describes the change exactly, and you edit until the files match it. Neovim starts in the
project's folder, so `:e Config.java`, `:args *.c` and `:vimgrep /x/ **/*.py` all work. Your result is
read from your buffers, saved or not. Quitting the window you started in submits your answer. That
includes `Ctrl-w o` from another window, because it closes your first one. F5 also clears the quickfix
list, the argument list and your command history, closes the files and windows you opened, and puts
the windows back the way they started (reopening any you closed, with every cursor where it began).

## The keys you need

### Buffers, windows and tabs

Three words that are easy to mix up:

| Thing | Is | Think of it as |
|---|---|---|
| **buffer** | a file loaded into memory | the file |
| **window** | a view onto a buffer | a pane on the screen |
| **tab page** | a set of windows | a layout |

Closing a window doesn't close its buffer. Neovim's `hidden` option is on, so you can also switch away from
a buffer with unsaved changes: it stays open, marked `+` in `:ls`, until you save it or quit.

### Opening files and switching buffers

| Keys | Does |
|---|---|
| `:e {file}` | edit a file. The path is relative to the current folder. `Tab` completes names: `:e C<Tab>` |
| `Ctrl-^` | jump to the alternate file, the one you were in before. `:e #` is the same |
| `:ls` | list the buffers: `%` current, `#` alternate, `+` changed. With several, you get a Press ENTER prompt |
| `:b {part}` | switch to the buffer whose name contains `{part}`: `:b Repo` for `ProductRepository.java` |
| `:b {N}` or `N Ctrl-^` | switch to buffer number N (the numbers `:ls` shows) |
| `:bn` / `:bp` | next / previous buffer. Neovim maps these to `]b` / `[b`, and the first / last to `[B` / `]B` |
| `:bd` | delete a buffer: take it out of the list |
| `:wa` / `:qa` / `:wqa` | write all changed buffers / quit all / both |

`:b` is the one to make a habit. You don't need the path, only a piece of the name that no other buffer has.
If the piece matches several buffers, Vim refuses with "E93: More than one match". Add a letter or press
`Tab` to cycle through the matches. On macOS the match ignores case.

### Windows

| Keys | Does |
|---|---|
| `Ctrl-w s` / `:sp {file}` | split the window in two, one above the other |
| `Ctrl-w v` / `:vs {file}` | split side by side |
| `Ctrl-w h` `j` `k` `l` | move to the window on the left, below, above, right |
| `Ctrl-w w` / `Ctrl-w p` | move to the next window / back to the previous one |
| `Ctrl-w c` | close this window. The buffer stays open |
| `Ctrl-w q` | quit this window, like `:q` |
| `Ctrl-w o` | close every other window ("only") |
| `Ctrl-w =` | make the windows the same size |

Each window has its own cursor, so you can keep your place in two files at once. In these exercises the task
text sits in a window at the top, and `Ctrl-w w` stops there too. `Ctrl-w h j k l` and `Ctrl-w p` go
straight to the window you mean.

**Tabs** hold different window layouts: `:tabnew`, `:tabe {file}`, `gt` / `gT` to switch, `:tabclose`.
They're not one-tab-per-file like in other editors. You won't need them in this project.

### Following a file name: gf

| Keys | Does |
|---|---|
| `gf` | go to the file whose name is under the cursor |
| `Ctrl-w f` | the same, in a new split |
| `Ctrl-o` / `Ctrl-i` | back / forward through the jump list, across files |

`gf` looks for the file in the folders listed in the `path` option. By default that's `.,,`: first the
folder of the current file, then the current folder. So `#include "strbuf.h"` in `util/strbuf.c` finds
`util/strbuf.h`, and `#include "util/strbuf.h"` in `main.c` finds it too.

- **C:** put the cursor on the file name, or on the space or quote before it. `gf` searches forward on the
  line for a name. On `#include` itself it fails ("E447: Can't find file "#include" in path"), because `#`
  counts as a file-name character.
- **Java:** on `util.Strings` in `import util.Strings;`, `gf` opens `util/Strings.java`. The Java filetype
  plugin turns the dots into slashes and adds `.java`.
- **Python:** on `shop.cart` in `import shop.cart` or `from shop.cart import total`, `gf` opens
  `shop/cart.py`, and on `config` in `from config import HOST` it opens `config.py`. But in
  `from shop import cart`, `gf` on `cart` fails, because it doesn't know `cart` lives in `shop/`.

**`Ctrl-o` vs `Ctrl-^`.** Both take you back, but `Ctrl-o` retraces every jump, including jumps inside a
file. `G`, `gg`, `/`, `n`, `*`, `%`, `{` and `}` are jumps. `j`, `k` and `w` aren't, even with a count. So
after `gf` and a search, the first `Ctrl-o` goes back to where the search started, and only the second one
leaves the file. `Ctrl-^` goes straight to the other file.

### The argument list: :args and :argdo

The argument list holds the files you started Neovim with, as in `nvim *.c`. You can replace it any time,
and it's the way to say "these files, picked by name."

| Keys | Does |
|---|---|
| `:args {files}` | set the argument list and open the first file. Globs work: `*.c`, `src/*.h`, `**/*.java` |
| `:args` | show the list. The current file is in `[brackets]` |
| `:next` / `:prev` | next / previous file. Neovim maps these to `]a` / `[a`, and the first / last to `[A` / `]A` |
| `:argdo {cmd}` | run `{cmd}` in every file in the argument list |

`**` matches any number of folders, including none, so `**/*.h` finds `list.h` and `src/util/str.h`. It
skips hidden folders like `.git`.

### :bufdo and :windo

| Keys | Does |
|---|---|
| `:bufdo {cmd}` | run `{cmd}` in every buffer in the buffer list (the files `:ls` shows) |
| `:windo {cmd}` | run `{cmd}` in every window on the screen |

Use `:bufdo` when the files you want are the ones you already have open. `:windo` is handy with splits,
for example `:windo diffthis` to compare two windows. In these exercises it also visits the task window,
which can't be changed. You'll see an E21 error for it, but the other windows still get the command.

### Rules for every "do" command

`:argdo`, `:bufdo`, `:windo`, `:cdo` and `:cfdo` all follow the same rules:

- **They take the rest of the line, `|` included.** `:bufdo %s/a/b/ge | %s/c/d/ge` runs both substitutions
  in every buffer. (`:g` and `:normal` work this way too.)
- **A `:s` that finds nothing is an error** ("E486: Pattern not found"). The loop still moves on to the
  next file, but the error skips the rest of that line in that file, so `| %s/c/d/` never runs there. Give
  every `:s` inside a loop the `e` flag, which turns that error off.
- **Changed files are left open, unsaved.** Save them all with `:wa` when you're done, or add `| update`
  to save each one as you go (`:update` only writes a file that changed). In these exercises `:wa` after
  your last change is free, but `| update` costs keys, because you type it before the Enter that makes the
  change.
- **`:normal` runs Normal-mode keys** in each file: `:argdo norm ggO// header`. It ends Insert mode for you.
  The cursor starts wherever you last left that file (line 1 if you haven't visited it), so start with a
  motion like `gg` or `G`.
- **Expect a Press ENTER prompt at the end.** The loops print a message for each file or match they visit
  (`:cdo` prints "(3 of 5)" and the line). That's normal. Press `Enter`, or type your next command straight
  away.

### The quickfix list: :vimgrep, :cnext, :cdo

| Keys | Does |
|---|---|
| `:vim /pat/ {files}` | `:vimgrep`: put every line that matches in the quickfix list, and jump to the first |
| `:vim /pat/g {files}` | one entry for every match, not every line |
| `:vim /pat/j {files}` | don't jump to the first match |
| `:vim // {files}` | reuse your last search pattern, from `/`, `*` or `#` |
| `:copen` / `:cclose` | open / close the quickfix window. `Enter` on an entry jumps to it |
| `:cnext` / `:cprev` | next / previous entry. Neovim maps these to `]q` / `[q`, and the first / last to `[Q` / `]Q` |
| `:cdo {cmd}` | run `{cmd}` at every entry, with the cursor on the match |
| `:cfdo {cmd}` | run `{cmd}` once in every file in the list |

The project-wide rename, in two commands (plus a save):

```
*                         search for the word under the cursor, as a whole word
:vim // **/*.java         every match in the project goes into the quickfix list
:cdo s//fetchUser/g       at each match, substitute using the same pattern
:wa                       save every changed file
```

The empty patterns `//` reuse the last search, so you only type the pattern once. Note that `:vimgrep`
doesn't set the search pattern itself: after `:vim /getUser/ **`, a `:s//x/` fails with "E35: No previous
regular expression". Search first, then `:vim //`.

**`:cdo` or `:cfdo`?** `:cdo` runs once per entry, which is what you want for `:s` on the matching line.
`:cfdo` runs once per file, which is what you want for anything that should happen once in each file,
like adding an import (`:cdo` would add it once per match), or a `%s` over the whole file.

**`:cnext` and `.` instead of `:cdo`.** When some matches need a different change, or none at all, step
through them yourself: make the first change, then `]q` to the next match and `.` to repeat it, or `]q`
again to skip it.

**Patterns that help:**

| Pattern | Means |
|---|---|
| `\<` `\>` | start / end of a word. `\<connect(` doesn't match `disconnect(`. `*` adds these for you |
| `\zs` | start the match here. `connect(\zs` puts each quickfix entry, and so the cursor, on the first argument |
| `\C` | match case, anywhere in the pattern. (`\c` ignores case) |

### Case: 'ignorecase', 'smartcase' and \C

Your setup has `ignorecase` and `smartcase` on: a pattern in all lowercase ignores case, and a pattern with
a capital letter matches case. Two things catch people out:

- **An all-lowercase pattern always ignores case.** `\<order\>` matches the class `Order` too.
- **`smartcase` only applies to patterns you type.** `*`, `#` and `:vimgrep` ignore it, so `*` on `getUser`
  and `:vim /getUser/ **` both match `GETUSER`. `:s//new/` reuses the last pattern the way it was made, so
  after `*` it ignores case as well. After a typed `/getUser`, it doesn't.

When case matters, say so. Put `\C` in the pattern (`/\C\<order\>`, `:vim /\Cjson\./ **/*.py`), or give `:s` the
`I` flag (`:s//purchase/gI`), which matches case for that substitution.

### :grep and ripgrep (optional)

`:vimgrep` uses Vim's own regular expressions and loads every file into Neovim to search it. That's fine
for a small project and slow for a big one. `:grep {args}` runs an outside search program instead, and
loads its results into the same quickfix list, so `:cnext`, `:cdo` and `:cfdo` work the same way.

If ripgrep is installed (`brew install ripgrep`), Neovim's `:grep` uses it automatically
(`rg --vimgrep -uu`): `:grep -w getUser` searches the whole project for the whole word, including hidden
and git-ignored files. Without ripgrep, `:grep` runs plain `grep`: `:grep -rw getUser .` does the same
thing. Either way the pattern is that program's syntax, not Vim's, so `:s//` can't reuse it. Retype it in
the `:s`.

## Your exercises

| # | Exercise | What it teaches |
|---|---|---|
| 1 | Move a method to another file | `:e` with `Tab`, and `Ctrl-^` back |
| 2 | Jump to a buffer by name | `:b` with a piece of the name |
| 3 | Header and source side by side | moving between windows with `Ctrl-w h` and `l` |
| 4 | Follow an include and come back | `gf`, and `Ctrl-^` vs `Ctrl-o` |
| 5 | Run one command in every header | `:args` with `**`, `:argdo` and `:normal` |
| 6 | Change every open buffer | `:bufdo`, `\|` and the `e` flag |
| 7 | Rename a function in every file | `*`, `:vimgrep //` and `:cdo s//` |
| 8 | Rename without touching the class | lowercase patterns ignore case, and the `I` flag |
| 9 | Step through the matches | `\<` and `\zs` in the pattern, then `]q` and `.` |
| 10 | Once per file, not once per match | `:cfdo` vs `:cdo`, and `\C` in `:vimgrep` |
| 11 | Add a parameter everywhere | two substitutions in one `:cdo` |
| 12 | Review · Cut a release | the whole course so far: a ranged `:cdo`, Visual block, `Ctrl-n` across buffers |
| 13 | Review · Rename a command | the whole course so far: `:cdo` without `g` and then `&`, `:sort`, a macro |

## Run it

```bash
python3 check.py          # see the exercises and your progress
python3 check.py next     # play the first one you haven't solved
python3 check.py 7        # play exercise 7
python3 check.py --watch 7   # stuck after three tries? watch the reference solution
```

See "How an exercise works" in [`../ROADMAP.md`](../ROADMAP.md) for the scoring rules. In this project, also
remember that keys you type on the command line count, up to the Enter that makes your last change, and
saving with `:wa` afterwards is free. `--show` writes keys in Vim's notation: `<CR>` is Enter, `<C-w>` is
Ctrl-w, and `<lt>` is a typed `<`.

## Drills

Drills are short extra problems that practice one command at a time, with two to six small files each, in
Java, C, Python, shell, SQL, config files, Markdown and ASCII art. Like the exercises, most have no target
window: the task says what to change in which file. `python3 check.py drill` lists them,
`python3 check.py drill buffers` plays the drills for one command, and `python3 check.py drill buffers --show 2`
reveals a solution. Before each one, check.py explains the commands you'll need, and F1 inside Neovim shows the
same notes.

| Keys | Does | Drills |
|---|---|---|
| `:e {file}` `Ctrl-^` | open a file, and switch back | 20 |
| `:ls` `:b {name}` `:bn` `:bp` | switch between open buffers | 20 |
| `Ctrl-w` `s` `v` `h` `j` `k` `l` `c` `o` | split windows and move between them | 20 |
| `gf` | open the file under the cursor | 6 |
| `:args` `:argdo` | run a command on a list of files | 6 |
| `:bufdo` `:windo` | run a command in every buffer or window | 6 |
| `:vimgrep` `:cnext` `]q` | search many files, step through matches | 6 |
| `:cdo` `:cfdo` | run a command on every match | 6 |

## Stretch goals

1. **Beat par by one.** `|` joins two commands on one line, and it's one key shorter than `<CR>:`. Try
   `:args **/*.h | argdo ...` in exercise 5, and `:vim // **/*.[ch] | cdo ...` in exercise 7.
2. **The other way.** Solve exercise 8 with `\C` instead of the `I` flag: search again with `/\C`
   followed by `Ctrl-r /`, then use `//` as before. Run `:copen` after the `:vimgrep` both ways. Which list
   is cleaner?
3. **Look before you leap.** In exercise 7, run `:copen` after `:vimgrep`, check every entry, then run
   `:cdo`. Do this every time you use it for real.
4. **Use it on your own code.** In one of your Java, C or Python projects, rename something with `*`,
   `:vim //`, `:cdo s//new/g` and `:wa`. Check the result with `git diff`.
5. **The location list.** Every window can have its own quickfix-style list: `:lvimgrep`, `:lopen`,
   `:lnext` (`]l`), `:ldo`, `:lfdo`. Redo exercise 7 with it.
6. **Install ripgrep** and redo exercise 7 with `:grep -w stack_size` instead of `:vimgrep`.

## Check your understanding

- What's the difference between a buffer and a window? What happens to a buffer when you close its
  window?
- After `:vim /pat/ **/*.c`, why does `:cdo s//new/g` fail with E35, when the same `:cdo` after
  `*` and `:vim // **/*.c` works?
- When does `:cdo` do the wrong thing where `:cfdo` is right? And when is `:cdo` right and
  `:cfdo s/a/b/` (without `%`) wrong?
- In `:bufdo %s/a/b/g | %s/c/d/g`, why can the second substitution be skipped in some files? How does
  `e` fix it?
- `Ctrl-o` and `Ctrl-^` both take you back. When do they take you to different places?
- Why can `:vim /getUser/ **/*.java` match `GETUSER`, even with `smartcase` on?

## Cheat sheet

```
Buffers     :e {file}  Ctrl-^  :ls  :b {part}  :b N  :bn :bp (]b [b)  :bd  :wa :qa :wqa
Windows     Ctrl-w s v (:sp :vs {file})   Ctrl-w h j k l w p   Ctrl-w c q o =
Files       gf  Ctrl-w f   Ctrl-o Ctrl-i (jump list)   'path' = .,, (this file's folder, then cwd)
Arg list    :args {glob}  :args  :next :prev (]a [a)  :argdo {cmd}       ** = any depth
Loops       :argdo :bufdo :windo :cdo :cfdo {cmd}   take | too   :s///ge   :wa or | update
Quickfix    :vim /pat/[gj] {files}  :vim // (last search)  :copen  :cnext :cprev (]q [q)  :cdo  :cfdo
Patterns    \< \> word edges   \zs match starts here   \C match case   :s///I match case
```
