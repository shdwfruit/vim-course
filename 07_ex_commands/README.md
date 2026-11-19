# Project 07 · Ex commands and :s: change every line that matches

> **Stage 7 · Ex commands and substitution** · about 3–4 hours · 14 exercises

## What you'll learn

Normal mode edits what's under the cursor. **Ex commands**, the ones you type after `:`, edit **lines**:
a range of them, or every line that matches a pattern. Almost every one has the same shape:

```
  :[range] command [arguments]
     %        s     /,/, /g        → on every line, replace each "," with ", "
    .,$       d                    → delete from this line to the end of the file
     4:       g     /^/t5          → on 4 lines from the cursor down, copy each one below line 5
```

Once you can say *which lines* (the range) and *what to do* (the command), one line of Ex does what
would take a macro. The star of the project is `:s`, the substitute command, with regular expressions,
groups, case changes and even arithmetic in the replacement. Then `:g` runs any command on every
matching line, and `:t`, `:m` and `:sort` move lines around.

Every key you type on the command line counts, including the final `<CR>`. `:s/a/b/<CR>` is 8 keys.

## The keys you need

### Ranges: which lines

A range goes right after the `:`. With no range, most commands act on the cursor line (`:sort`, `:g`
and `:v` are the exceptions: they default to the whole file).

| Range | Lines | Range | Lines |
|---|---|---|---|
| (none) | the cursor line | `%` | every line (same as `1,$`) |
| `.` | the cursor line | `5` | line 5 |
| `$` | the last line | `3,8` | lines 3 to 8 |
| `.,$` or `,$` | from here to the end | `.,+3` or `,+3` | this line and the 3 below it |
| `-2` | two lines above the cursor | `'a,'b` | from mark `a` to mark `b` |
| `'<,'>` | the last Visual selection | `/start/;/end/` | from the next line matching `start` to the first `end` after it |

Two shortcuts fill in a range for you:

- **A count before `:`** becomes a range. `4:` turns into `:.,.+3`: the cursor line and the three
  below it. With relative line numbers on, the count you need is right there in the margin, plus one.
- **`:` in Visual mode** fills in `:'<,'>`. Select a paragraph with `vip`, press `:`, and the command
  acts on just those lines.

A leading `.` is optional: `:,+3` means `:.,+3`. A pattern address searches forward from the line
*after* the cursor, wrapping around the end of the file. Separate two pattern addresses with `;`, not
`,`: in `:/def b/;/return/s/x/y/` the search for `return` starts at `def b`, while with a comma it
starts back at the cursor and might find a `return` above `def b`.

### `:s`: substitute

```
:[range]s/pattern/replacement/[flags]
```

| Command | Does |
|---|---|
| `:s/old/new/` | replace the first `old` on the cursor line |
| `:s/old/new/g` | replace every `old` on the cursor line |
| `:%s/old/new/g` | every `old` in the file |
| `:%s/old/new` | the closing `/` is optional when there are no flags |
| `:s#/usr/local#/opt#` | any punctuation can be the separator, handy when the text has slashes |
| `:%s//new/g` | an **empty pattern** reuses the last search |

The empty pattern is the trick to remember. Search first (with `/` or `*`, and watch the highlights
to check you got the right matches), then `:%s//new/g` replaces exactly what you saw. `*` searches
for the whole word under the cursor, as `\<word\>`, so it never matches inside a longer word.

**Flags** go after the last `/`:

| Flag | Does |
|---|---|
| `g` | every match on the line, not just the first |
| `i` / `I` | ignore case / match case exactly, for this command only |
| `c` | confirm each change (`y` yes, `n` no, `a` all, `q` quit) |
| `n` | don't change anything, just count the matches |
| `&` | keep the flags of the previous `:s` (must come first: `:s/a/b/&`) |

### Case: `ignorecase` and `smartcase`

The course config has `ignorecase` and `smartcase` on, just like your own config. That means
**an all-lowercase pattern ignores case**, and a pattern with any capital letter matches case exactly.
This applies to `/`, `?`, `:s` and `:g`.

| Pattern | Matches | Why |
|---|---|---|
| `log` | `log`, `Log`, `LOG` | all lowercase, so case is ignored |
| `Log` | only `Log` | has a capital, so smartcase makes it exact |
| `\Clog` | only `log` | `\C` anywhere in a pattern: match case |
| `\cLog` | `log`, `Log`, `LOG` | `\c` anywhere in a pattern: ignore case |

The `I` and `i` flags do the same as `\C` and `\c`, for one `:s`. **Gotcha:** `*` and `#` don't use
smartcase. They ignore case whenever `ignorecase` is on, so `*` on `log` also finds `Log`.

### Patterns, and very magic `\v`

Vim's regular expressions need a backslash in front of many special characters. Start a pattern with
`\v` ("very magic") and they work without one, like in Python or Java:

| Meaning | Normal Vim | Very magic | Meaning | Either mode |
|---|---|---|---|---|
| group | `\(…\)` | `(…)` | any character | `.` |
| one or more | `\+` | `+` | zero or more | `*` |
| zero or one | `\=` or `\?` | `=` or `?` | start / end of line | `^` `$` |
| 2 to 3 times | `\{2,3}` | `{2,3}` | digit / not a digit | `\d` `\D` |
| as few as possible | `\{-}` | `{-}` | word character `[0-9A-Za-z_]` / letter | `\w` `\a` |
| word start / end | `\<` `\>` | `<` `>` | whitespace / not | `\s` `\S` |

"This or that" is `\|` normally and a bare bar in very magic: `\v(get|set)Name` matches `getName`
and `setName`.

So `:%s/\(.*\), \(.*\)/\2 \1/` and `:%s/\v(.*), (.*)/\2 \1/` are the same command. The catch: in
very magic mode a *literal* `(`, `)`, `+`, `=`, `?`, `{`, `@`, `<`, `>` or bar needs a backslash
instead (`\v\(bar\)` matches the text `(bar)`, and an email needs `\@`). Use whichever mode needs
fewer backslashes.

`.*` is **greedy**: it grabs as much as it can. On `say "hi" and "bye"`, `".*"` matches from the first
quote to the last one. The lazy version, `\v".{-}"` (or `".\{-}"` without `\v`), matches just `"hi"`.

`\zs` and `\ze` set where the match **starts** and **ends**, so you can match context without
replacing it. `:s/width: \zs\d\+/20/` changes the number and keeps `width: `.

### The replacement

| In the replacement | Inserts |
|---|---|
| `&` or `\0` | the whole match |
| `\1` … `\9` | what group 1 … 9 matched (groups are numbered by their opening parenthesis) |
| `\u` / `\l` | the next character in uppercase / lowercase |
| `\U` / `\L` | everything after it in uppercase / lowercase, until `\e` or `\E` |
| `\r` | a line break (splits the line) |
| `\t` | a tab |
| `~` | the replacement from the previous `:s` |

Examples: `:s/\w\+/"&"/g` quotes every word. `:s/\v(\w+) (\w+)/\2 \1/` swaps the first two words.
`:s/\v_(.)/\u\1/g` turns `user_name` into `userName`. `:s/\w\+/\u&/g` capitalizes every word.

**Gotcha:** in the replacement, `\n` is *not* a line break. It inserts a null byte (shown as `^@`).
Use `\r`. (In the *pattern*, `\n` does match a line break.)

### Expressions: `\=`

If the replacement starts with `\=`, the rest is a Vim expression, evaluated for every match.

| Replacement | Does |
|---|---|
| `\=submatch(0) * 2` | doubles the matched number. `submatch(0)` is the whole match, `submatch(1)` group 1 |
| `\=line('.')` | the line number |
| `\=line('.') . '. '` | `1. `, `2. `, …: `.` joins strings |
| `\=printf('%04d', submatch(0))` | pads the number to four digits: `7` becomes `0007` |

`submatch()` gives you text, and Vim turns text into a number when you do arithmetic on it. So
`:%s/\d\+/\=submatch(0)*2/g` doubles every number in the file.

### `:g` and `:v`: run a command on every matching line

```
:[range]g/pattern/command        on every line that matches
:[range]v/pattern/command        on every line that doesn't
```

| Command | Does |
|---|---|
| `:g/TODO/d` | delete every line containing TODO |
| `:v/ERROR/d` | delete every line *without* ERROR: keep only the errors |
| `:g/^\s*$/d` | delete blank (and whitespace-only) lines |
| `:g/TODO/t$` | copy every TODO line to the end of the file |
| `:g/pat/s/a/b/g` | substitute only on lines that contain `pat` |
| `:g/pat/normal A;` | run Normal-mode keys on every matching line |
| `:g/^/m0` | reverse the file |

`:v` is short for `:vglobal`, the same as `:g!`. `:g` works in two passes: first it marks every
matching line, then it runs the command on each marked line in order, top to bottom, with the cursor
at the start of that line. That's why `:g/^/m0` reverses a file: line 1 moves to the top, then line 2
moves above it, then line 3 above that, and so on.

**Gotcha:** `:g/pat/d` puts the deleted lines in the unnamed register, so `p` afterwards pastes the
last one. Use `:g/pat/d _` (the black hole register) to keep your register.

### `:normal`: Normal-mode keys, from the command line

`:normal` (short: `:norm`) types its argument as Normal-mode keys. On a range, it runs once per line,
starting at the first column of each.

| Command | Does |
|---|---|
| `:%norm A;` | append `;` to every line |
| `:'<,'>norm @q` | run macro `q` on every selected line (Project 06) |
| `:g/print/norm f r(A)` | on each `print` line: replace the first space with `(` and append `)` |

If the keys leave a command unfinished, `:normal` finishes it as if you pressed `<Esc>`, so an Insert
at the end needs no `<Esc>`. To put a special key *in the middle*, type `Ctrl-v` first: `Ctrl-v <Esc>`
shows up as `^[`. `:normal` uses your mappings; `:normal!` ignores them. Nothing can follow it on the
line: a `|` becomes part of the keys.

### `:t` and `:m`: copy and move lines

`:t` (also `:copy`) copies lines, and `:m` (`:move`) moves them. The address after them says
*below which line* the lines go. `0` means "above line 1".

| Command | Does | Normal-mode equivalent |
|---|---|---|
| `:t.` | duplicate the cursor line | `yyp` |
| `:t0` / `:t$` | copy this line to the top / bottom | `yyggP` / `yyGp` |
| `:m0` / `:m$` | move this line to the top / bottom | `ddggP` / `ddGp` |
| `:m+1` | move this line down one | `ddp` |
| `:m-2` | move this line up one | `ddkP` |
| `:5,8t$` | copy lines 5–8 to the end | |
| `:-7t.` | copy the line 7 above the cursor to below it | |

The best part is that **the cursor doesn't have to go there**. With relative numbers on, `:-7t.`
grabs a line you can see without leaving your spot.

### `:sort`

| Command | Sorts |
|---|---|
| `:sort` | the whole file (it's the default range), alphabetically |
| `:sort!` | in reverse |
| `:sort u` | and drops duplicate lines |
| `:sort i` | ignoring case |
| `:sort n` | by the first number on each line, so `9` comes before `10` |
| `:sort /pat/` | by the text *after* the first match of `pat` |
| `:sort /pat/ r` | by the text the pattern matches |
| `vip:sort` | just this paragraph |

Without `n`, sorting compares text character by character, so `100` sorts before `9`. Flags combine:
`:sort! n /,/` sorts by the first number after the first comma, highest first. For `:sort`'s
pattern, `ignorecase` applies but `smartcase` doesn't.

### Abbreviations, and repeating

Most Ex commands have a short form (`:help` shows it with brackets, like `:s[ubstitute]` and
`:sor[t]`), and the space between a command and its flags is optional. You'll see these in the
reference solutions:

| Short | Long | Short | Long |
|---|---|---|---|
| `:s` | `:substitute` | `:t` | `:copy` |
| `:g` / `:v` | `:global` / `:vglobal` | `:m` | `:move` |
| `:norm` | `:normal` | `:sor` | `:sort` |
| `:d` | `:delete` | `:sor!n/,/` | `:sort! n /,/` |

To repeat a substitute: **`&`** repeats the last `:s` on the cursor line. In Neovim it keeps the flags
(`&` is mapped to `:&&`); in plain Vim `&` drops them, and `:&` drops them in both. **`g&`** repeats it
on every line, with the same flags. **`@:`** repeats the last Ex command of any kind. Project 08 has
more on those.

## Your exercises

| # | Exercise | What it teaches |
|---|---|---|
| 1 | Space after every comma | `:s` with the `%` range and the `g` flag |
| 2 | Rename inside one function | a range of lines, and a count before `:` |
| 3 | Mind the case | how `ignorecase` affects `:s`, and the `I` flag |
| 4 | Rename the word under the cursor | `*`, then `:s` with an empty pattern |
| 5 | Wrap every call in backticks | `&`: the whole match, in the replacement |
| 6 | Swap two fields | very magic `\v`, groups and `\2 \1` |
| 7 | snake_case to camelCase | `\u` in the replacement |
| 8 | Double every number | `\=` expressions and `submatch()` |
| 9 | Keep only the errors | `:v/pattern/d` |
| 10 | Port print to Python 3 | `:g/pattern/normal` |
| 11 | Sort by the last column | `:sort` with `!`, `n` and a pattern |
| 12 | Mirror the picture | `:g` with `:t`, and why `:g` reverses things |
| 13 | Review · Ship the backup script | 00–07 mixed: `:sort`, `:g` with `:d` and `:t`, `:m` counting from the cursor |
| 14 | Review · Import the old orders | 00–07 mixed: `\v` groups, `:sort /pat/`, `\U&`, a block `r` |

## Run it

```bash
python3 check.py          # see the exercises and your progress
python3 check.py next     # play the first one you haven't solved
python3 check.py 4        # play exercise 4
python3 check.py --watch 4   # stuck after three tries? watch the reference solution
```

See "How an exercise works" in [`../ROADMAP.md`](../ROADMAP.md) for the scoring rules.

## Drills

Drills are short problems that practice one command at a time: 20 for each everyday command and 6 for
each rarer one, scored like the exercises. `python3 check.py drill` lists them,
`python3 check.py drill global` plays the next `:g` drill (or `drill global 4` for drill 4), and
`python3 check.py drill global --show 4` explains a reference solution. Before each one, check.py
lists the commands it uses, and F1 inside Neovim shows the same notes.

| Keys | What they do | Drills |
|---|---|---|
| `:s/old/new/` | substitute | 20 |
| `:5,9`  `:.,+3`  `:%` | ranges: which lines a command touches | 20 |
| `:g/pat/cmd` | run a command on every matching line | 20 |
| `:normal {keys}` | Normal-mode keys on many lines | 20 |
| `:t`  `:m` | copy and move lines | 20 |
| `:v/pat/cmd` | run a command on every line that doesn't match | 6 |
| `\v`  `( )`  `\1` | very magic patterns and groups | 6 |
| `\u`  `\U`  `\l`  `\L`  `\e` | change case in the replacement | 6 |
| `\=` | compute the replacement | 6 |
| `:sort` | sort lines | 6 |
| `&`  `g&`  `:&&` | repeat the last substitute | 6 |
| `:s///i`  `I`  `c`  `n` | substitute flags: case, confirm, count | 6 |

## Stretch goals

1. **Beat Project 00.** Go back to exercise 10 of Project 00 (space after every comma) and solve it with
   `:s`. How many keys under its par of 11 can you get?
2. **Number a list.** Take a few lines of text and turn them into a numbered list with one `:s` and
   `\=line('.')`. Then make it start at 1 even when the list doesn't start on line 1. (Hint: `line("'<")`
   is the first line of the last Visual selection.)
3. **Reverse a file** with `:g/^/m0`. Then reverse just one block: if it's lines 10–14,
   `:10,14g/^/m9` does it. Why 9? What goes wrong with `m10`?
4. **Clean up for real.** In your own code, delete every line with a debug print in one `:g`, remove
   trailing whitespace with `:%s/\s\+$//e` (what does the `e` do?), and sort an import block with
   `vip:sort u`.
5. **Count things.** How many times does `return` appear in a file you're working on? Find out with
   `:%s/return//gn` without changing anything.

## Check your understanding

- `:s/a/b/` on the line `banana` gives `bbnana`. What does `:s/a/b/g` give? And `:%s/a/b/` on a file
  where every line is `banana`?
- After `*` on the variable `n`, why doesn't `:%s//len/g` touch the `n` in `int`? What would plain
  `:%s/n/len/g` do?
- You run `:%s/error/warning/g` on a log with lines like `ERROR: disk full`. What happens, and what are
  two ways to make it only change lowercase `error`?
- Why does `:g/^/m0` reverse the file? What would `:g/^/m$` do?
- In the replacement, what is the difference between `\r` and `\n`? Between `\u` and `\U`?
- What does `4:` put on the command line, and where does the range end if the cursor is on line 10?

## Cheat sheet

```
Ranges      %  .  $  5  3,8  .,$  ,+3  -2  'a,'b  '<,'>  /start/;/end/     4: → :.,.+3   Visual : → :'<,'>
:s          :s/pat/rep/   g every  i/I case  c confirm  n count  & keep flags    :%s//rep/g = last search
Case        lowercase pattern ignores case, any capital matches exactly     \c ignore  \C exact   (* ignores smartcase)
\v          ( ) + = ? | {n,m} {-} < >  without backslashes                  \d \w \s \a   \zs \ze
Replace     & \0 whole   \1-\9 groups   \u \l next char   \U \L … \e   \r newline   \t tab   ~ previous
Expr        \=submatch(0)*2   \=line('.')   \=printf('%03d', submatch(1))
:g :v       :g/pat/d   :v/pat/d   :g/pat/normal keys   :g/pat/s//new/g   :g/^/m0 reverse
Lines       :t. dup   :t0 :t$   :m0 :m$   :m+1 :m-2   :5,8t$   :-7t.
:sort       ! reverse  u unique  i case  n number  /pat/ after match  /pat/ r on match
Repeat      & last :s on this line (keeps flags in Neovim)   g& on every line   @: last Ex command
```
