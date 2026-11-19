"""Reference solutions for Project 07 (spoilers!). Each entry: exercise name -> (keys, explanation).

See one with:  python3 check.py --show N      Watch it typed:  python3 check.py --watch N
"""
SOLUTIONS = {
    "space-after-commas": (":%s/,/, /g<CR>",
        "% is the range \"every line\", s/,/, / replaces a comma with a comma and a space, and the g flag "
        "does every comma on the line instead of only the first. Every key on the command line counts, "
        "including the <CR>. Compare Project 00's exercise 10: the same edit on one line took 11 keys "
        "with f, ; and ., and this does a whole file in 11."),
    "rename-in-function": ("6:s/total/sum_sq<CR>",
        "Typing a count before : fills in a range for you: 6: becomes :.,.+5, the cursor line and the "
        "five below it, which is exactly variance(). The closing / is optional when there are no flags. "
        ":,+5s/total/sum_sq (the . is implied) and vip:s/total/sum_sq do the same thing in a few more "
        "keys. A range is what keeps mean() and report() safe."),
    "match-case": (":%s/log/logger/I<CR>",
        "With ignorecase and smartcase on, an all-lowercase pattern ignores case, so plain "
        ":%s/log/logger/ turns the type Log into logger on line 2. The I flag makes this one "
        ":s case-sensitive. Putting \\C anywhere in the pattern (:%s/\\Clog/logger) is the same "
        "length and does the same. An uppercase letter in the pattern would also do it, through smartcase."),
    "star-rename": ("*:%s//len<CR>",
        "* searches for the word under the cursor as a whole word, \\<n\\>, so it can't match the n in "
        "int, mean or return. An empty pattern in :s means \"the last search pattern\", so :%s//len "
        "renames every match without retyping it. Typed out, :%s/\\<n\\>/len is 4 keys longer. Note that "
        "* ignores smartcase: if the file also had a variable N, it would match too."),
    "backtick-calls": (r":%s/\w\+()/`&`/g<CR>",
        "\\w\\+ is one or more word characters, followed by a literal (). In the replacement, & is "
        "the whole match (\\0 means the same thing), so `&` wraps it in backticks. You can shave a key "
        "with \\w*(), since a run of zero word characters never comes before () here. In very magic "
        "mode, ( and ) would start a group, so this one is easier without \\v."),
    "swap-names": (r":%s/\v(.*), (.*)/\2 \1<CR>",
        "\\v turns on very magic, so ( ) are groups without backslashes. The first (.*) grabs everything "
        "before \", \" and the second grabs the rest. In the replacement, \\2 \\1 writes them back in the "
        "other order with a space between. Without \\v you'd type \\(.*\\), \\(.*\\), two keys longer. "
        ".* is greedy, so with two commas on a line the first group would take everything up to the last one."),
    "snake-to-camel": (r":%s/\v_(.)/\u\1/g<CR>",
        "The pattern matches an underscore plus the next character, and captures that character as \\1. "
        "The replacement drops the underscore and writes \\u\\1: \\u uppercases the next character "
        "only. The g flag matters on the last line, which has several names. \\U uppercases everything "
        "that follows until \\e or \\E, and \\l and \\L do the same for lowercase."),
    "double-sizes": (r":%s/\d\+/\=submatch(0)*2/g<CR>",
        "A replacement that starts with \\= is evaluated as an expression for each match. submatch(0) is "
        "the matched text as a string, and multiplying it turns it into a number. The g flag catches every "
        "number on a line. Doing this with Ctrl-a would need a different count for each of the 11 numbers."),
    "keep-errors": (":v/ERROR/d<CR>",
        ":v (short for :vglobal, the same as :g!) runs a command on every line that does NOT match. So "
        "\"delete every line without ERROR\" keeps exactly the errors. The INFO line that says \"no errors\" "
        "goes too: ERROR has capitals, so smartcase makes the pattern case-sensitive. :g/ERROR/d would do "
        "the opposite. (:v/ER/d<CR> beats par by 3, because only the ERROR lines contain a capital ER. "
        "Shortening patterns like that is fair game, but check that the short one can't match too much.)"),
    "python3-prints": (":g/print/norm f r(A)<CR>",
        ":g puts the cursor at the start of each matching line, and :norm (short for :normal) types the "
        "rest of the command there as Normal-mode keys: f<Space> jumps to the first space, r( replaces "
        "it with (, and A) appends ). :normal finishes Insert mode by itself, so no <Esc> is needed. "
        "It works here because every print starts its line. :%s/\\vprint (.*)/print(\\1) also works, "
        "in 6 more keys."),
    "sort-scores": (":sor!n/,/<CR>",
        "Written out, this is :sort! n /,/. ! sorts in reverse (highest first). n sorts by the first number "
        "on the line, and /,/ tells :sort to skip past the first comma, so that first number is the score "
        "instead of the id. :sor is the shortest abbreviation, and the spaces are optional. Without n, "
        "\"9\" would sort above \"88\", because text sorts character by character."),
    "mirror-art": ("4:g/^/t5<CR>",
        "4: makes the range .,.+3, the top four lines. :g/^/ matches every line in it, and t5 copies "
        "each one to just below line 5, the middle. :g handles the lines in order, so each copy pushes "
        "the earlier ones down: the line copied last (line 4) ends up first. That's the same reason "
        ":g/^/m0 reverses a whole file."),
    "review-backup-script": ([
        ("A3<Esc>", "step 1."),
        ("4jdd", "step 2."),
        ("vip:sor<CR>", "step 3: vip selects the imports, and : on a Visual selection starts the command line "
                        "with its range."),
        ("5jfvRsrv<Esc>", "step 4: srv is as long as var, so Replace mode types over it."),
        ("2j7<C-a>", "step 5."),
        ("4jf-x;.", "step 6: x deletes one dash, ; finds the other and . deletes it too."),
        (":%s/src/source<CR>", "step 7: no line has src twice, so there's no need for g. And no other word in "
                               "the file contains src: SOURCES doesn't, even ignoring case."),
        (":g/DEBUG/d<CR>", "step 8."),
        (":%s/print/log.info<CR>", "step 9."),
        (":%s/\" %/\",<CR>", "step 10: in every message the closing quote is followed by \" %\", so replacing "
                             "that with \",\" makes the value an argument."),
        (":+7m+4<CR>", "step 11: the last :s left the cursor on the pruning line, so prune() is 7 lines down "
                       "and the logging line it goes under is 4 down. Ex addresses can count from the cursor."),
        (":g/^$/t.<CR>", "step 12: :t. copies a line below itself, and :g/^$/ does it to every blank line. "
                         ":g marks the lines before it runs, so the new blank lines aren't copied again."),
    ], "The Normal-mode fixes first, top to bottom, then one Ex command per step for the ones that touch "
       "several lines: :sort, :s, :g with :d, :m and :t. Measured: :%s/\\<src\\>/source/g, the careful "
       "rename, costs 6 more; moving prune() with G3k:m-3 costs 1 more than counting from the cursor. "
       ":g/^def\\|^if/norm O would miss the blank lines after the docstring and after the imports."),
    "review-orders-csv": ([
        ("dd", "step 1."),
        ("fccwname<Esc>", "step 9: the header is the cursor's line now, and its first c starts customer."),
        ("$F;i_cents<Esc>", "step 8."),
        ("+<C-v>Gr5", "step 10: all the ids are 100x, so a Visual block down the first column and r5 turns "
                      "every 1 into a 5 at once."),
        ("3j4f;a-<Esc>", "step 11: the refunded order is three rows down, and its amount comes after the "
                         "fourth ;."),
        (":%s/;/,/g<CR>", "step 2."),
        (":g/test/d<CR>", "step 3."),
        (":%s#\\v(..)/(..)/(....)#\\3-\\2-\\1<CR>", "step 4: with # as the separator the slashes need no "
                                                  "backslash, and very magic groups don't either. \\3-\\2-\\1 "
                                                  "puts the year, month and day back in ISO order."),
        (":sor/-/<CR>", "step 5: :sort with a pattern sorts on what comes after the match. The first - in "
                        "each row is in its date, so the rows sort by month and day (every order is from "
                        "2024), and the header, which has no -, stays on top."),
        (":%s/,\\a\\a,/\\U&<CR>", "step 6: the countries are the only two-letter fields, and \\U uppercases "
                                 "the match."),
        (":%s/\\.<CR>", "step 7: every amount has two decimals, so dropping the dot gives cents. With an "
                        "empty replacement, the slashes after the pattern can go."),
        ("2k4f,50<C-a>", "step 12: :s left the cursor on the last row, and Linus is two rows up. From the "
                         "comma before his amount, Ctrl-a adds 50 to it."),
    ], "The header and the fixed-width edits first, while the ids still line up in a column, then one Ex "
       "command for each change that touches every row. Measured: \\=submatch(0)+4000 on the ids costs more "
       "than a block r5; :2,$sor/,/ sorts the same in 3 more keys; doing Linus's 50 cents before the cents "
       "step doesn't work, since Ctrl-a would change the 8 of 8.99."),
}
