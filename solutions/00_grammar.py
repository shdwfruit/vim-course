"""Reference solutions for Project 00 (spoilers!). Each entry: exercise name -> (keys, explanation).

See one with:  python3 check.py --show N      Watch it typed:  python3 check.py --watch N
"""
SOLUTIONS = {
    "delete-words": ("fvd3w",
        "fv jumps to the first v on the line. d3w deletes three words, and each word takes its "
        "trailing space with it, so the spacing comes out right. 3dw does the same thing."),
    "fix-operator": ("jf-r+",
        "j moves down a line, f- jumps to the minus, and r+ replaces that one character. r leaves you "
        "in Normal mode, so there's no <Esc> to press."),
    "swap-letters": ("fexp",
        "fe lands on the e of \"teh\". x deletes it into the unnamed register, and p puts it back after "
        "the cursor, which is now on the h. \"xp\" is the classic swap-two-characters idiom."),
    "move-line": ("ddp",
        "dd cuts the whole line. p puts a line-wise register below the current line, so the line moves "
        "down by one. ddkP moves a line up."),
    "change-to-end": ("2wC3<Esc>",
        "2w hops over \"retries\" and \"=\" to land on \"int\". C is short for c$: change to the end of "
        "the line. The final <Esc> is free, because keys after your last change don't count."),
    "delete-to-char": ("f\"d2tv",
        "f\" jumps to the opening quote. dtv would stop at the v in \"value=\", so d2tv deletes up to "
        "just before the second v. Counts work on f, t, F and T. (f\"18x is a key shorter, but only if "
        "you count all 18 characters first, which is slow and easy to get wrong.)"),
    "append-semicolons": ("A;<Esc>j.j.",
        "A; appends the semicolon, and <Esc> finishes the change. Then j moves down and . repeats "
        "\"append a semicolon at the end of the line\", wherever the cursor is on that line."),
    "indent-body": ("j>j",
        "> is an operator. With the motion j it covers the current line and the one below, so >j "
        "indents both. 2>> does the same in one more key."),
    "join-array": ("5J",
        "5J joins five lines into one. J removes the indentation of each joined line and puts a single "
        "space between them, which is exactly the spacing we want."),
    "space-after-commas": ("f,a <Esc>;.;.;.",
        "f, jumps to the first comma and a<Space><Esc> appends a space after it. Then ; repeats the "
        "last f-jump and . repeats the last change. This \"; .\" rhythm is worth practicing until it's "
        "automatic. (Project 07 shows :s/,/, /g, which beats par here.)"),
    "underline-heading": ("o<Esc>7i=<Esc>",
        "o opens a new line and <Esc> returns to Normal mode. 7i=<Esc> inserts = seven times: the "
        "repetition happens when you press <Esc>, so that one counts. yypVr= (copy the line, then "
        "replace every character with =) is also 6 keys and always matches the heading's length."),

    "review-wordcount": ([
        ("ddp", "step 1: dd cuts import sys and p puts it back below import os."),
        ("jjA:<Esc>", "step 2: A appends at the end of the line, wherever the cursor is on it."),
        ("jF<lt>s!=<Esc>", "step 3: j keeps the column, which is past the < on the shorter line, so F goes back "
                           "to it. s replaces one character with what you type."),
        ("j>>", "step 4."),
        ("fFRPATH<Esc>", "step 5: PATH is as long as FILE, so Replace mode types over it, a key less than cw."),
        ("jhr2", "step 6: j lands on the ) at the end of the shorter line, and h steps back onto the 1."),
        ("jlD", "step 7: j keeps the column, which is the ] here. l steps onto the first space, and D deletes "
                "to the end of the line."),
        ("jjFcct_n<Esc>", "step 8: Fc goes back to the start of count_words, and ct_ changes up to the "
                          "underscore, so _words stays."),
        ("8jfc.", "step 11, straight away: . repeats only the most recent change, so the call is renamed "
                  "before anything else changes. The DEBUG line is still there, so main()'s call is 8 lines down."),
        ("fhxp", "step 12: the only h on the line is the one in paht. xp swaps it with the t."),
        ("7kdd", "step 9: back up to the DEBUG line."),
        ("2jA)<Esc>", "step 10."),
        ("5j3J", "step 13: 3J joins three lines into one, dropping the indentation and putting one space at "
                 "each join."),
    ], "Top to bottom, one short edit at a time, with one detour for the rename: . repeats only your last "
       "change, so the second count_words is renamed right after the first, before the DEBUG line and the "
       "parenthesis. Several edits ride on j keeping the column: after A, R or D the cursor is near the end "
       "of its line, and the next edit is near the end of the next line. Measured: going strictly top to "
       "bottom and typing ct_n again at the call ties at 64 (4jXp fixes the typo from the end of the line); "
       "cw instead of R for PATH costs 1 more."),
    "review-readme": ([
        ("o<Esc>", "step 1: o opens a line below the title, and <Esc> leaves it empty."),
        ("jJ", "step 2: J joins the next line on, with one space between."),
        ("jjAl<Esc>", "step 3."),
        ("jj>>", "step 4: Markdown files use a shiftwidth of 4, so >> indents exactly four spaces."),
        ("jjo<Esc>", "step 5."),
        ("jjyypA --all<Esc>", "step 6: yyp copies the line below itself, and A adds the flag to the copy."),
        ("jbcwdone<Esc>", "step 7: j keeps the column, which lands on the 1, so b goes back to remove."),
        (">3k", "step 8: > with the motion 3k indents this line and the three above it."),
        ("8jt(D", "step 9: t( stops on the space before the (, so D deletes it too."),
        ("4b6i <Esc>", "step 11, starting with --quiet, which needs the most: 4b goes back to print, and "
                       "6i<Space><Esc> types six spaces."),
        ("kb2.", "--file PATH needs two more. A count before . replaces the count of the change it repeats, "
                 "so 2. types two spaces before where."),
        ("jj1.", "and --color WHEN needs one, which 1. types."),
        (">2k", "step 10, last: one > indents all three options, and indenting them together keeps them lined up."),
    ], "Top to bottom, letting counts do the repeating: > with a motion indents a block in one go, a count on "
       "i types several spaces at once, and when the same insert comes up again in a different size, . takes "
       "a new count. Measured: lining the options up after indenting them costs 2 more, because > leaves the "
       "cursor where it was, far from where the spaces go."),
}
