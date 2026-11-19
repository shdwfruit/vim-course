# Project 02 · Text objects: act on the thing you're in

> **Stage 2 · Text objects** · about 2 hours · 14 exercises

## What you'll learn

A motion says "from here to there." A **text object** says "this thing": the word, the string, the
parentheses, the block, the tag, the sentence or the paragraph the cursor is in. You use one after an
operator, in the noun slot:

```
  operator  i/a  object
     c       i     "      → change inside the quotes
     d       a     w      → delete a word, and the space next to it
     y       i     (      → copy everything inside the parentheses
     gU      i     w      → uppercase this word
```

The best part: **it doesn't matter where in the thing the cursor is.** `ci"` works the same at the
start, the middle or the end of the string, and often from before it. You stop aiming and just say
what you want to change.

## The keys you need

### Inner and around

Every text object comes in two sizes. `i` is **inner**: just the thing, or just what's between the
delimiters. `a` is **a**, or **around**: the thing plus its delimiters, or plus the white space next
to it.

With the cursor on the `t` of `there`:

```
print("hi there", x)

  iw   there                  the word
  aw    there                 the word and a space (here the space before, see below)
  i"   hi there               inside the quotes
  a"   "hi there"             the quotes too
  i(   "hi there", x          inside the parentheses
  a(   ("hi there", x)        the parentheses too
```

Text objects only exist after an operator (`d c y gU >` ...) or in Visual mode. On their own, `i` and
`a` still start Insert mode.

### Words and WORDS: iw aw iW aW

| Object | Is |
|---|---|
| `iw` | the word under the cursor. On white space, it's the run of white space. |
| `aw` | the word plus the white space after it. If there's none after it, the white space before it. |
| `iW` / `aW` | the same for a WORD (anything between spaces, like `a.b(c)`) |

The "before" rule is what makes `daw` tidy. Deleting the last word before a closing quote, `daw` takes
the space in front of it, so you don't end up with `"Download finished "`.

Rule of thumb: **delete with `aw`, change with `iw`.** `daw` removes a word and keeps the spacing
right. `ciw` keeps the spaces, which is what you want when you're about to type a replacement.

Two more tricks: `ciw<Space>` on a run of spaces squeezes it down to one space, and counts work, so
`d3aw` deletes three words.

### Sentences and paragraphs: is as ip ap

| Object | Is |
|---|---|
| `is` / `as` | a sentence / plus the white space after it |
| `ip` / `ap` | a paragraph / plus the blank lines after it |

A **sentence** ends at `.`, `!` or `?` followed by a space, a tab or the end of the line. It can span
several lines. `das` deletes it and the space after it. `dis` leaves the spaces behind, so you'd get
two spaces between the sentences around it.

A **paragraph** is a block of lines between blank lines, and these objects always work on whole lines.

- `ap` includes the blank lines after the paragraph. For the last paragraph in a file, which has none
  after it, `ap` takes the blank lines before it instead.
- On a blank line, `ip` is the run of blank lines, and `ap` is those plus the paragraph after them.
- Here a line of only spaces *does* count as blank, unlike for the `}` motion.

In code, a paragraph is usually a function or a block. `dap` deletes a function from anywhere inside
it, and `yap` copies one. In Project 03 you'll use `=ip` to reindent one and `!ip sort` to sort one.

### Quotes: i" a" i' a' i` a`

| Object | Is |
|---|---|
| `i"` / `a"` | inside a double-quoted string / with the quotes |
| `i'` / `a'` | the same for single quotes (Python strings, C chars) |
| `` i` `` / `` a` `` | the same for backticks (Markdown code, shell, JavaScript) |

- **Inside the string, the position doesn't matter.** `ci"` from the middle changes the whole contents.
- **Before a string, they look ahead.** If the cursor isn't in a string, Vim uses the next string on
  the line. So `ci"` works from the start of `name = input("Enter: ")`.
- **Only on the current line.** A string on the next line isn't found.
- **`a"` includes white space,** like `aw`: the space after the closing quote, or if there's none, the
  space before the opening one. `2i"` is the quotes without any white space.
- **Escaped quotes are skipped,** so `"a \"quoted\" word"` is one string.

Two traps:

- **Between two strings, the gap looks like a string.** In `put("name", "Ada")` with the cursor on the
  comma, `ci"` changes `, `. Vim pairs up the quotes from the start of the line, and the comma sits
  between quote 2 and quote 3. Move into the string you mean first.
- **No string, no change.** If there's no string on the line, `ci"` fails and you stay in Normal mode,
  so whatever you type next runs as commands. Press `u` to undo the damage.

### Brackets: i( i{ i[ i<

| Object | Also written | Is |
|---|---|---|
| `i(` / `a(` | `i)` `ib` / `a)` `ab` | inside the parentheses / with the parentheses |
| `i{` / `a{` | `i}` `iB` / `a}` `aB` | inside the braces / with the braces |
| `i[` / `a[` | `i]` / `a]` | inside the square brackets / with them |
| `i<` / `a<` | `i>` / `a>` | inside the angle brackets / with them |

- **Anywhere inside, or on either bracket.** The object is the innermost pair around the cursor. Nested
  pairs inside it are counted properly, so `ci[` on `scores[len(scores) - 1]` changes the whole index.
- **A count reaches outward.** In `max(abs(dx), abs(dy))` with the cursor on `dx`, `i(` is `dx`, and
  `2i(` is `abs(dx), abs(dy)`.
- **Not inside a pair? It looks ahead,** for the next opening bracket after the cursor. Unlike quotes,
  it keeps looking on later lines, so if there's no `(` on this line, `ci(` will happily change one ten
  lines down.
- **`a(` adds only the brackets,** never the white space around them.
- **Blocks on their own lines are line-wise.** When `{` ends its line and `}` starts its own, `di{`
  deletes the lines between and leaves both braces where they are. `ci{` gives you a fresh, correctly
  indented line to type on. That's how you empty or replace a function body in one go.
- **`i<` is for generics and HTML:** `ci<` turns `List<Map<String, Integer>>` into `List<Row>`. It
  doesn't understand Java, though. A less-than sign earlier on the line, like `if (n < max)`, confuses
  the look-ahead. Move inside the brackets first.

**`ci(` or `ct)`?** `ct)` only works from the start of the contents, and stops at the first `)`, even
a nested one. `ci(` works from anywhere inside and finds the right `)`.

### Tags: it at

| Object | Is |
|---|---|
| `it` | everything between an HTML/XML tag and its closing tag |
| `at` | the whole element, tags included |

- **Nested tags are included.** In `<p>Read the <b>full</b> guide.</p>`, `cit` on `Read` changes the
  whole text, bold part and all. `ct<` would stop at `<b>`.
- **On a tag counts as inside it:** with the cursor on `<b>`, `dat` deletes `<b>full</b>`.
- **In the indentation,** Vim starts from the first character after it, so the first tag on the line.
- **It doesn't look ahead.** Outside every tag, `dit` does nothing.
- Case is ignored, and tags without a closing tag, like `<br>`, are skipped.

### Objects work with every operator

| You want to | Keys |
|---|---|
| change a word from its middle | `ciw` |
| delete a word and keep the spacing right | `daw` |
| copy a function's arguments | `yi(` |
| uppercase a word, or a whole string | `gUiw`, `gUi"` |
| delete a whole function | `dap` |
| empty a function body | `di{` |
| indent a block's contents | `>i{` |
| select the inside of a string, to see it | `vi"` (Visual mode is Project 04) |

And `.` repeats them as objects. After `ci"one<Esc>`, moving to another line and pressing `.` changes
*that* line's string to `one`, wherever on the line you are.

In Visual mode, objects can grow: `va(` selects the parentheses around the cursor, and pressing `a(`
again selects the next pair out.

## Your exercises

| # | Exercise | What it teaches |
|---|---|---|
| 1 | Delete a word and its space | `daw`, and which space it takes |
| 2 | Delete a sentence | `das` across lines |
| 3 | Delete a paragraph | `dap` vs `dip` |
| 4 | Change a string | `ci"` looking ahead from before the string |
| 5 | Change a string from the middle | `ci'`, from anywhere inside |
| 6 | Uppercase a string | objects with another operator: `gUi"` |
| 7 | Change an index | `ci[` with nested brackets inside |
| 8 | Copy the arguments | `yi(` and putting inside empty brackets |
| 9 | Change a generic type | `ci<` on nested Java generics |
| 10 | Change the outer arguments | a count on an object: `c2i(` |
| 11 | Replace a method body | `ci{` on a multi-line block |
| 12 | Change the text of a tag | `cit` with nested tags |
| 13 | Review · Fix a sign-up form | 00 to 02 mixed: `da<` + `.`, `dap` to move a block, `ci"`, `das`, smartcase searches |
| 14 | Review · Tidy a report script | 00 to 02 mixed: `ci"` looking ahead, `dap` at the end of a file, `df)` + `.`, `da[` |

## Run it

```bash
python3 check.py          # see the exercises and your progress
python3 check.py next     # play the first one you haven't solved
python3 check.py 4        # play exercise 4
python3 check.py --watch 4   # stuck after three tries? watch the reference solution
```

See "How an exercise works" in [`../ROADMAP.md`](../ROADMAP.md) for the scoring rules.

## Drills

Drills are short extra problems that practice one text object at a time, paired with different operators
(`d c y p v gU > = .`) in Java, C, Python, Markdown, HTML and shell, from the simplest form to small
realistic edits. `python3 check.py drill` lists them, `python3 check.py drill quote` plays the drills for
one object, and `python3 check.py drill quote --show 2` reveals a solution. Before each one, check.py
explains the commands you'll need, and F1 inside Neovim shows the same notes.

| Keys | Does | Drills |
|---|---|---|
| `iw` `aw` | a word | 20 |
| `i"` `a"` `i'` `a'` | inside or around quotes | 20 |
| `i(` `a(` | inside or around parentheses | 20 |
| `i{` `a{` | inside or around braces | 20 |
| `i[` `a[` | inside or around square brackets | 20 |
| `ip` `ap` | a paragraph | 20 |
| `iW` `aW` | a WORD | 6 |
| `is` `as` | a sentence | 6 |
| `it` `at` | inside or around an HTML/XML tag | 6 |
| `i<` `a<` | inside or around angle brackets | 6 |
| `2i(` `2i{` | counts reach the enclosing pair | 6 |

## Stretch goals

1. **Motions vs objects.** Solve exercises 4, 7 and 12 again using only motions (`f t / %`). How many
   more keys do they take? Which one can't be done with `t` at all?
2. **Spring the trap.** In exercise 5, press F5, then `F:` to land on the colon before the string, and
   try `ci'`. Explain what changed and why.
3. **Grow a selection.** In a nested expression like `f(a, g(b, h(c)))`, put the cursor on `c` and
   press `va(`, then `a(` a few more times. Then try `vip` and `vi{` in a real file.
4. **Objects for real.** For one day, every time you change a string, an argument list or a word, use
   an object. Count how often `ci"`, `ci(` and `ciw` come up.
5. **More objects.** Plugins in your own config can add more. `nvim-treesitter-textobjects` can give
   you objects for functions and classes, and `mini.ai` adds function arguments and more. Read their
   READMEs and decide which objects you'd use daily.

## Check your understanding

- When should you use `daw` instead of `diw`? When is `diw` the right one?
- When is `ci(` better than `ct)`? Is `ct)` ever better?
- `ci"` and `ci(` both look ahead when the cursor isn't inside. How far does each one look?
- In exercise 3, what would `dip` have left behind, and why does `dap` get it right?
- `aw` usually takes the space after the word. When does it take the space before instead?
- You typed `ci"one<Esc>` on one line. On another line, with the cursor at the start, you press `.`.
  What happens?

## Cheat sheet

```
i = inner (just the thing)          a = around (plus delimiters or white space)
Words       iw aw  iW aW         aw takes the space after, or before if there's none after
Text        is as (sentence)     ip ap (paragraph, line-wise; ap includes the blank lines after)
Quotes      i" a"  i' a'  i` a`  current line only; looks ahead; a" adds white space
Brackets    i( a( = ib ab   i{ a{ = iB aB   i[ a[   i< a<   counts reach out: 2i(
            not inside one: looks ahead to the next opening bracket, even on later lines
Tags        it at                includes nested tags; no look-ahead
Use with    c d y gU gu > =  v (select)   and . repeats the object
```
