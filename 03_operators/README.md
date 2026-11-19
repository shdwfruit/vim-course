# Project 03 · More operators: case, indent, format, filter, comment

> **Stage 3 · More operators** · about 2–3 hours · 14 exercises

## What you'll learn

You already know three operators (`d`, `c`, `y`), plus `>` and `<`. This project adds nine more. The
good news: **every new operator works with every motion and text object you already know.** You
don't learn `gUiw`, `=ap` or `gcip` as separate commands. You learn `gU`, `=` and `gc`, and the rest
is grammar you have from Projects 00–02.

```
     operator          noun                     sentence
     gU  uppercase     iw   inner word          gUiw      MAX_SIZE
     =   reindent      ap   a paragraph         =ap       fix a pasted method
     gc  comment       j    this line + next    gcj       hide two debug lines
     !   filter        ip   inner paragraph     !ip sort  sort the imports
     gq  rewrap        gc   the comment block   gqgc      tidy a long comment
```

Learn one new operator and you get a few dozen new commands for free. `.` repeats every one of them.

## The keys you need

### Case: `gU` `gu` `g~` `~` and `g?`

| Keys | Does | Example |
|---|---|---|
| `gU{motion}` | uppercase | `gUiw`: `max_size` → `MAX_SIZE` |
| `gu{motion}` | lowercase | `gu$`: lowercase to the end of the line |
| `g~{motion}` | toggle (flip) case | `g~j`: fix two lines typed with Caps Lock on |
| `g?{motion}` | rot13: shift each letter 13 places | `g?i"`: decode the string |
| `~` | toggle the character under the cursor and move right | `3~` toggles three characters |

**Doubled means "this line",** like `dd`: `gUU` (or `gUgU`), `guu`, `g~~`, `g??`.

A few details:

- **Text objects work from anywhere in the thing.** With the cursor in the middle of `max_retries`,
  `gUiw` uppercases the whole word, but `gUe` only uppercases from the cursor to the end of it.
- **`~` is not an operator.** It takes a count, not a motion: `5~` flips five characters. (The
  `'tildeop'` option turns it into one, but it's off by default and in this course.)
- **Only letters have case.** Digits, `_` and punctuation pass through `gU`, `gu`, `g~` and `g?`
  unchanged. That's why `g~` on `# nEVER` gives `# Never`.
- **rot13 is its own inverse.** Doing `g?` twice gives the original text back. It's not encryption,
  just a way to hide spoilers in plain sight.

### Indent: `>` `<` and `=`

`>` and `<` shift lines right or left by `'shiftwidth'` (4 spaces here). They're always line-wise:
any motion or text object becomes "the lines it touches."

| Keys | Shifts |
|---|---|
| `>>` / `<<` | this line |
| `>ip` / `<ip` | the paragraph around the cursor (lines between blank lines) |
| `>i{` | the lines inside the `{ }` block around the cursor |
| `>G` / `>}` | from here to the end of the file / of the paragraph |

**A count is a count of lines, not of levels.** `3>>` shifts three lines by one level each. To
shift further, press `.` once per extra level. Empty lines are never shifted, so `>ip` and `>ap`
give the same result.

`=` is different: instead of shifting, it **recomputes** each line's indentation from the language's
rules, so it fixes indentation that's random, not just off by one level.

| Keys | Reindents |
|---|---|
| `==` | this line |
| `=ap` | the paragraph around the cursor, such as one whole function |
| `=i{` | the inside of the innermost `{ }` block around the cursor |
| `gg=G` | the whole file |
| `P=']` | paste above, then reindent what you just pasted (`']` is a mark at its last line) |

Which rules `=` uses depends on the filetype:

- **C** uses `'cindent'`, Vim's built-in C indenter. It understands braces, `case` labels, and
  statements continued on the next line.
- **Java** uses `GetJavaIndent()`, which is cindent with a few Java tweaks.
- **Python** uses `python#GetIndent()`, and it can't do much. In Python the indentation *is* the
  structure, so Vim can't know where a block should end. In this Neovim, `=` indents the line after
  a line ending in `:` by one level, dedents the line after `return`, `pass`, `raise`, `break` or
  `continue` if it's indented deeper than that, and **leaves every other line's indentation alone.**
  So on a function that's one level too deep, `=ip` does nothing. **In Python, move blocks with `>`
  and `<`.**

Gotchas:

- `=i{` reindents only the inside of the *innermost* braces, relative to the line with the `{`. If
  that line is wrong too, widen the object: `=2i{`, `=ap`, or `gg=G`.
- `>%` from column 1 of `if (x) {` shifts just one line: `%` finds the `(` first and jumps to its
  `)`. Use `>i{`, or put the cursor on the `{` first.

### Rewrapping text: `gq` and `gw`

`gq{motion}` re-breaks lines so they fill up to `'textwidth'` columns, joining short lines and
splitting long ones. `gw{motion}` does the same but puts the cursor back where it was.

| Keys | Rewraps |
|---|---|
| `gqip` / `gwip` | the paragraph |
| `gqq` | this line |
| `gqgc` | the comment block around the cursor (`gc` is a text object, see below) |
| `gqj` | this line and the next |

- **Set `'textwidth'` first.** `:setlocal textwidth=72` sets it for the current file. If it's 0 (the
  default), `gq` uses the window width, up to 79 columns. Exercise 10 sets it to 50 for you.
- **It knows about comments.** In a Python or C file, rewrapping `# ...` or `// ...` lines keeps the
  comment leader at the start of every new line. (`'comments'` lists the leaders, and the `q` flag
  in `'formatoptions'` allows `gq` on them.)
- **Don't point it at code.** `gq` treats code lines as text, so `gqip` on a function can join two
  statements into one line. Give it exactly the lines you mean, such as `gqgc` or `gq2j`.
- **`gq` vs `gw` in your own config.** When a language server is attached, Neovim sets
  `'formatexpr'` so that `gq` asks the server to format. `gw` never does: it always uses Vim's own
  line-wrapping. If `gq` ever does something surprising in real code, try `gw`.

### Filtering through the shell: `!`

`!{motion}` sends the lines to a shell command's input and replaces them with its output. After the
motion, Vim puts a range on the command line for you (`!ip` on a 5-line paragraph gives
`:.,.+4!`), and you type the command and `<CR>`.

| Keys | Does |
|---|---|
| `!ipsort<CR>` | sort the paragraph |
| `!!rev<CR>` | `!!` filters just this line (`3!!sort<CR>` sorts this line and the next two) |
| `!Gsort<CR>` | from here to the end of the file |
| `u` | undo, like any other change |

These commands all ship with macOS, and each behaves as described (checked on this Mac):

| Command | Does | Watch out |
|---|---|---|
| `sort` | sorts lines as text | `10` sorts before `9` |
| `sort -n` | sorts by number: `9 10 100` | |
| `sort -r`, `sort -rn` | reverse order (highest first) | |
| `sort -u` | sorts and removes duplicates | |
| `sort -f` | ignores upper/lowercase | without it, case order depends on your locale |
| `uniq` | removes repeated lines | only *adjacent* repeats, so sort first (or use `sort -u`) |
| `uniq -c` | counts repeats | |
| `tr a-z A-Z` | translates characters | `gU` does this one without the shell |
| `tr -s ' '` | squeezes runs of spaces into one | |
| `tr -d ' '` | deletes every space | |
| `rev` | reverses each line: `stressed` → `desserts` | |
| `column -t` | lines up whitespace-separated columns, two spaces apart | splits on *every* space |
| `column -s, -t` | the same for comma-separated values | |

**`%`, `#` and `!` are special on Vim's command line**: `%` means the current file's name. So
`!!echo 50%` prints `50` followed by the file name. Write `\%` for a literal percent sign.

The filter operator is how Vim gets every feature it doesn't have: any program that reads lines and
writes lines becomes an operator, and it works with all your motions.

### Comments: `gc` (built into Neovim)

| Keys | Does |
|---|---|
| `gcc` | toggle a comment on this line (`3gcc`: three lines) |
| `gc{motion}` | toggle comments on the lines it covers: `gcj`, `gcip`, `gcG` |
| `gcgc` | uncomment the comment block around the cursor |
| `dgc`, `gqgc`, `ygc` | after any operator, `gc` is a text object: "the block of commented lines here" |

`gc` uses the filetype's `'commentstring'`. In this Neovim:

| Filetype | `'commentstring'` | `gcc` gives |
|---|---|---|
| C, Java | `// %s` | `// return 0;` |
| Python | `# %s` | `# return 0` |
| Lua | `-- %s` | `-- x = 1` |
| Markdown, HTML | `<!-- %s -->` | `<!-- Some text -->` |
| plain text | (empty) | nothing: "Option 'commentstring' is empty." |

How the toggle decides: **if every line in the range is a comment, `gc` uncomments them all.
Otherwise it comments them all,** so lines that were already comments get a second `//`. That's
why toggling a mix of commented and uncommented lines in one go rarely does what you want. The
comment marker goes at the indentation of the least-indented line, so a block's inner indentation
is kept.

To comment in a file type with no `'commentstring'`, set one: `:setlocal commentstring=#\ %s`.

### Joining: `J` and `gJ`

| Keys | Joins | Example |
|---|---|---|
| `J` | the next line onto this one, with one space | `{2, 3,` + `    7}` → `{2, 3, 7}` |
| `gJ` | exactly as is, with nothing added or removed | `"9f86` + `c27e"` → `"9f86c27e"` |
| `4J` / `4gJ` | four lines into one | |

`J` removes the next line's leading spaces and puts a single space at the join, with two exceptions:
no space before a `)`, and no extra space if the line already ends in one. In a comment, `J` also
removes the second line's comment marker: `# first` + `# second` → `# first second`. `gJ` adds and
removes nothing, so the next line's indentation stays in the middle of the joined line.

`J` takes a count but not a motion, so it isn't an operator. (In Project 04 you'll use it on a
Visual selection.)

### Numbers: `Ctrl-a` and `Ctrl-x`

`Ctrl-a` adds its count (default 1) to **the first number at or after the cursor** on the line, and
`Ctrl-x` subtracts. You don't need to move to the number first. The cursor ends on its last digit.

| Keys | On `port = 8080` |
|---|---|
| `Ctrl-a` | `port = 8081` |
| `10 Ctrl-a` | `port = 8090` |
| `80 Ctrl-x` | `port = 8000` |
| `.` | repeats the last one, with the same count |

It understands `0x` hex (`0xfe` → `0xff`, and it keeps the letters' case) and `0b` binary
(`0b0111` → `0b1000`). Gotchas:

- **A `-` in front makes it negative.** On `arr[i-1]`, `Ctrl-a` gives `arr[i0]`: Vim saw `-1` and
  added 1. `:set nrformats+=unsigned` makes it ignore minus signs (`arr[i-2]`).
- **Digits inside names count.** On `v2 = x1 + 9`, `Ctrl-a` from column 1 turns `v2` into `v3`.
- **No octal in Neovim.** `007` becomes `008`. In Vim, whose `'nrformats'` includes octal, `007`
  becomes `010`, a classic surprise.

### Repeating it all with `.`

`.` repeats the whole sentence: operator, motion or text object, and count. After `gUiw`, `.` on
another word uppercases that word. After `gcj`, `.` toggles the next two lines. After `10 Ctrl-a`,
`.` adds 10 again. The dot formula from Project 00 (one key to move, one key to repeat) works with
every operator in this project.

## Your exercises

| # | Exercise | What it teaches |
|---|---|---|
| 1 | Caps Lock was on | `g~` with a line-wise motion |
| 2 | CONSTANT_CASE | `gU` + a text object, then `.` |
| 3 | camelCase a method name | `~` on single characters |
| 4 | Decode the secret | `g?` + a quote text object |
| 5 | Dedent a function | `<` + a paragraph, and why `=` can't do it in Python |
| 6 | Reindent a method | `=` + the right-sized text object |
| 7 | Toggle comments | `gc` + a motion, then `.` to toggle back |
| 8 | J and gJ | joining with and without a space |
| 9 | Bump the ports | `Ctrl-a` with a count, on a number later on the line |
| 10 | Rewrap a comment | `gq` on exactly the comment lines |
| 11 | Sort the imports | `!` + a paragraph + `sort` |
| 12 | Line up a table | `!` + `column -t` |
| 13 | Review · Clean up a logger | 00–03 mixed: `!ip` sort, `gU` + `*` + `Ctrl-o`, `Ctrl-x` + `.`, `gq`, `=i{` |
| 14 | Review · Finish a backup script | 00–03 mixed: `gUU`, `dap`, `~`, `gJ`, `<j`, `gcc`, `gqq` |

## Run it

```bash
python3 check.py          # see the exercises and your progress
python3 check.py next     # play the first one you haven't solved
python3 check.py 6        # play exercise 6
python3 check.py --watch 6   # stuck after three tries? watch the reference solution
```

See "How an exercise works" in [`../ROADMAP.md`](../ROADMAP.md) for the scoring rules.

## Drills

Drills are short extra problems that practice one command at a time, in different files and pairings,
from its simplest form to small realistic edits. `python3 check.py drill` lists them,
`python3 check.py drill gq` plays the drills for one command, and `python3 check.py drill gq --show 2`
reveals a solution. Before each one, check.py explains the commands you'll need, and F1 inside Neovim
shows the same notes.

| Keys | Does | Drills |
|---|---|---|
| `gU` `gu` `g~` `~` | change case | 20 |
| `=` `==` | re-indent by the language's rules | 20 |
| `gc` `gcc` | comment or uncomment lines | 20 |
| `Ctrl-a` `Ctrl-x` | add to or subtract from a number | 20 |
| `g?` | ROT13-encode text | 6 |
| `gq` `gw` | rewrap text to the text width | 6 |
| `!{motion}` `!!` | run lines through a shell command | 6 |
| `gJ` | join lines without adding spaces | 6 |

## Stretch goals

1. **Beat par on exercise 9.** Peek at Project 04: select the three lines with `V`, then one
   `Ctrl-a` with a count changes all of them.
2. **The leaderboard.** Type five lines like `42 ada`, `7 linus`, `128 grace`. Sort them highest
   score first. Try `!ipsort -r` before `!ipsort -rn`, and explain the difference.
3. **Mirror some ASCII art.** Draw a small shape with `/`, `\`, `(` and `<`, then try `!iprev`. The
   slashes now lean the wrong way. Fix it with
   `!iprev | tr '/\\()<>' '\\/)(><'` (inside Vim you need `\\` for each backslash).
4. **Clean up a real file.** Open a C or Java file you wrote this semester and run `gg=G`. Did
   anything change? Then find a long comment and rewrap it with `gwgc`.
5. **Make your own filter.** Any program that reads lines and writes lines works with `!`. Write a
   five-line Python script that numbers its input lines, and run `!ip python3 number.py`.

## Check your understanding

- Why does `=ip` fix a method with messy indentation in Java, but do nothing to an over-indented
  function in Python?
- With the cursor in the middle of `buffer_size`, what's the difference between `gUiw` and `gUe`?
- `3>>` doesn't indent a line three levels. What does it do, and how *do* you indent three levels?
- You run `gc3j` on two commented lines followed by two uncommented ones. What happens, and why?
- What does `Ctrl-a` do on `arr[i-1]`, and how would you stop it?
- `sort` puts `100` before `9`. Why, and which flag fixes it?
- `gqip` broke a line of code in two. Which text object or motion should you have used?

## Cheat sheet

```
Case       gU up   gu down   g~ toggle   g? rot13   ~ one char (takes a count)   gUU guu g~~ g?? = line
Indent     > <  shift by shiftwidth  (>> << >ip >i{ >G)   count = lines, not levels; . shifts again
Reindent   =  language rules  (== =ap =i{ gg=G P='])      Python: use > and < instead
Rewrap     gq{motion} to textwidth (gqip gqq gqgc)        gw = same, cursor stays, never uses LSP
Filter     !{motion}cmd<CR>   !!cmd = this line           sort -n -r -u -f  uniq  tr  rev  column -t
Comment    gcc  gc{motion}  gcip   gc as an object: gcgc dgc gqgc     all commented → uncomment
Join       J  one space, no indent     gJ  exactly as is     4J = four lines
Numbers    Ctrl-a / Ctrl-x  first number at or after cursor   10 Ctrl-a = +10   . repeats   watch -1
```
