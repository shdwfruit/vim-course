"""Reference solutions for Project 03 (spoilers!). Each entry: exercise name -> (keys, explanation).

See one with:  python3 check.py --show N      Watch it typed:  python3 check.py --watch N
"""
SOLUTIONS = {
    "caps-lock": ("g~j",
        "g~ is the toggle-case operator and j is a line-wise motion, so g~j flips every letter on this "
        "line and the next. The # signs and punctuation have no case, so they don't change. g~ip would "
        "also flip the def line, because there's no blank line between the comment and the code."),
    "shout-constants": ("gUiwj.j.",
        "gUiw uppercases the whole word under the cursor, from anywhere inside it. Underscores are word "
        "characters, so max_retries is one word. An operator leaves the cursor at the start of the text it "
        "changed, and all three names start in the same column, so j lands on the next name and . repeats "
        "gUiw there. gUe would only work from the first letter of the word."),
    "camel-case": ("fu~fi~",
        "fu jumps to the u of \"userid\" and ~ flips it to U, then moves one character right. fi jumps to "
        "the i of \"id\" and ~ flips that too. ~ with a count flips several characters: 3~ would flip "
        "\"use\". (Careful with f: on a line starting with \"public\", fu would stop at the u in public.)"),
    "secret-message": ("g?i\"",
        "g? is the rot13 operator: it shifts each letter 13 places through the alphabet, so doing it twice "
        "gives the original back. i\" is \"inside the quotes\", and quote text objects search forward on "
        "the line when the cursor isn't in a string, so it works from column 1. g?? would rot13 the whole "
        "line and turn print into cevag. Digits and punctuation are left alone."),
    "dedent-function": ("<lt>ip",
        "< shifts lines left by one shiftwidth, and ip is the paragraph around the cursor: the four lines "
        "between the blank lines. Try =ip first: it changes nothing, because in Python the indentation IS "
        "the structure, so Vim can't work out that this def should be at the top level. In Python, use > "
        "and < to move blocks. <ap gives the same result, since < leaves empty lines alone."),
    "reindent-method": ("=ap",
        "= reindents lines using the filetype's rules (here GetJavaIndent(), which builds on cindent). ap "
        "is the paragraph around the cursor: the whole max() method plus the class's closing brace, which "
        "is already right. =i{ only reindents the inside of the innermost braces, the for loop, relative to "
        "the for line, which is itself wrong. =2i{ also works, in one more key. gg=G reindents the whole "
        "file, which is a good habit in C and Java."),
    "toggle-comments": ("gcj2j.",
        "gc is Neovim's built-in comment operator, and gcj toggles this line and the next. It uses the "
        "filetype's 'commentstring', here \"// %s\". The cursor stays on line 3, so 2j moves to the "
        "commented lines and . repeats gcj there. Both lines are already comments, so the toggle "
        "uncomments them. gc4j would do the wrong thing: when any line in the range isn't a comment, gc "
        "comments all of them, and the commented ones get a second //."),
    "join-lines": ("JjgJ",
        "J joins the next line, removes its leading spaces and puts one space at the join, which is right "
        "for the array. After J the cursor sits at the join, so j moves to the hash line. gJ joins without "
        "adding or removing anything, which is right for the split string. 3gJ joins three lines at once. "
        "Note that gJ also keeps the next line's indentation, if it has any."),
    "bump-ports": ("10<C-a>j.j.",
        "Ctrl-a adds its count to the first number at or after the cursor, so from column 1 it finds 8080. "
        "After Ctrl-a the cursor is on the last digit of the number, and the numbers line up, so j lands "
        "on the next number and . repeats \"add 10\". Project 04's Visual mode beats par: Vjj10<C-a> "
        "adds 10 to every selected line in 6 keys. If the numbers didn't line up, + (first non-blank of "
        "the next line) would work as well as j."),
    "rewrap-comment": ("gq2j",
        "gq is the format operator: it joins and re-breaks lines to fit 'textwidth'. Because # is in "
        "'comments' and 'formatoptions' has q, it keeps the # on every new line. 2j covers exactly the "
        "three comment lines. gqgc also works in 4 keys: gc after an operator is the text object for the "
        "comment block around the cursor. gqip would also rewrap the two code lines and break the return "
        "statement. gw does the same as gq but leaves the cursor where it was."),
    "sort-imports": ("!ipsort<CR>",
        "! is the filter operator. !ip puts :.,.+4! on the command line, and you type the command: "
        "sort<CR>. Vim sends the five lines to sort's input and replaces them with its output. From the "
        "first import line, !}sort<CR> is one key shorter: } is exclusive, and when it ends in column 1 "
        "Vim makes the motion line-wise and stops before the blank line. Ex has its own :sort too, which "
        "you'll meet in Project 07."),
    "align-table": ("!ipcolumn -t<CR>",
        "column -t reads whitespace-separated columns and pads each one to its widest entry plus two "
        "spaces. !ip sends the table's five lines through it. This only works because every cell is one "
        "word: column would split \"linked list\" into two cells. column -s, -t splits on commas instead, "
        "which aligns a small CSV file."),
    "review-logger": ([
        ("!ipsort<CR>", "step 1: the includes are the first paragraph, so !ip sends them through sort."),
        ("5jWgUe", "step 2: W skips #define in one hop (w would stop at the d after the #), and gUe uppercases "
                   "to the end of the name."),
        ("j.", "step 2: the names start in the same column, so j lands on log_buf_size and . repeats gUe."),
        ("*.", "step 2: * searches for the word under the cursor. 'ignorecase' is on, so LOG_BUF_SIZE finds "
               "log_buf_size in log_line(), and . uppercases it."),
        ("<C-o>256<C-a>", "step 4: * was a jump, so Ctrl-o goes straight back. 256 Ctrl-a adds 256 to the first "
                          "number after the cursor."),
        ("k<C-a>", "step 3: on the line above, the cursor's column is past the name, and Ctrl-a finds the 3."),
        ("3j3dd", "step 5: the TODO, the variable and the blank line."),
        ("gqq", "step 6: gq knows C comments: it rewraps the line and starts the new one with ' * '."),
        ("8jJ", "step 7: J joins the next line and drops its indent, leaving one space after the comma."),
        ("jgcc", "step 8: gcc comments out one line, with // in C."),
        ("=i{", "step 9: = with the inside of the braces reindents the whole body, the commented line too."),
        ("}4j<C-x>j.j.", "step 10: } and 4j to the first case. Ctrl-x finds the number after the cursor, and . "
                         "repeats it on the next two lines."),
        ("gu2k", "step 11: lowercasing the three whole lines only changes the names: case and return are "
                 "already lowercase."),
        ("4jci\"unknown<Esc>", "step 12, last because it ends in Insert mode: ci\" changes inside the quotes "
                               "even from the start of the line."),
    ], "Straight down the file, letting . repeat gU and Ctrl-x, and * plus Ctrl-o fetch the one change that's "
       "far away. The two numbers are done on the way back from the jump, bottom one first, because the "
       "cursor lands in the right place for both. gu2k beats gui\" and . (7 keys) because nothing else on "
       "those lines has a capital."),
    "review-backup-script": ([
        ("2jdd", "step 1: delete import sys first..."),
        ("!3jsort<CR>", "step 1: ...so the four imports left are the cursor's line and 3 more. (!ip would "
                        "sort the shebang and the docstring too: there's no blank line above the imports.)"),
        ("5j2<C-a>", "step 2: Ctrl-a with a count adds 2."),
        ("jgUU3<C-x>", "step 3: gUU uppercases the whole line (= and 9 have no case), and 3 Ctrl-x takes 3 "
                       "from the number after the cursor."),
        ("11jdap", "step 4: dap deletes the function and both blank lines after it."),
        ("jjfD~", "step 5: ~ flips the one character under the cursor."),
        ("gJ", "step 6: gJ joins the lines exactly as they are, with no space."),
        ("<lt>j", "step 7: < shifts this line and the next one level left."),
        ("2jgcc", "step 8: gcc uses # in Python."),
        ("jjgqq", "step 10: gqq rewraps the comment and starts the new line with # at the same indent."),
        ("jJ", "step 11: gq leaves the cursor on the last line it wrote, so j is on prune(."),
        ("3kci\"zip<Esc>", "step 9, last because it ends in Insert mode."),
    ], "Top to bottom, with the one Insert-mode change saved for the end so its <Esc> is free. Each edit is "
       "one operator and the smallest motion that covers it: dd and !3j on the imports, gUU on a whole line, "
       "dap for a function, <j for two lines, gqq and gcc for one."),
}
