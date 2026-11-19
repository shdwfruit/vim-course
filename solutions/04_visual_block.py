"""Reference solutions for Project 04 (spoilers!). Each entry: exercise name -> (keys, explanation).

See one with:  python3 check.py --show N      Watch it typed:  python3 check.py --watch N
"""
SOLUTIONS = {
    "bullet-list": ("<C-v>3jI- <Esc>",
        "<C-v>3j selects a block one column wide and four lines tall. I starts inserting in front of the "
        "block, but you only see it on the first line until <Esc>, which copies \"- \" to the other lines. "
        "<C-v>} looks shorter but goes down to the blank line, and the blank line gets a \"- \" too. "
        "The dot formula, I- <Esc>j.j.j., takes 10 keys."),
    "ragged-semicolons": ("<C-v>3j$A;<Esc>",
        "Pressing $ in block mode stretches the block to the end of every line, so the right edge is "
        "ragged. A then appends after each line's own end. Without $, A would append at the block's right "
        "column and pad the shorter lines with spaces. A;<Esc>j.j.j. also works, in 9 keys."),
    "strip-line-numbers": ("<C-v>G3ld",
        "<C-v>G selects column 1 from here to the last line: G keeps the cursor's column, because "
        "'startofline' is off in Neovim. 3l widens the block to four columns, \"1 | \", and d deletes "
        "only the rectangle. Line 2 is shorter than the block, which is fine: d takes what's there. "
        "<C-v>GEld also works in 5 keys."),
    "charge-battery": ("<C-v>j5lr#",
        "The cursor starts on the first empty cell. <C-v>j5l selects a block two rows tall and six "
        "columns wide, and r# replaces every character in it with #. Visual r doesn't need an <Esc>. "
        "Without a block, 6r# fills one row but leaves the cursor on the last # it wrote, so the second "
        "row needs 6r#j5h. (7 keys). The block doesn't care where the cursor ends up."),
    "hex-digits": ("<C-v>2j$U",
        "The block starts on the first hex digit, so 0x stays outside it. $ takes every line to its end, "
        "commas included, but U leaves characters without case alone. <C-v>2jeU also works: e moves to "
        "the end of the word on the last line, and all three numbers are the same width. gUiw would "
        "uppercase the x too."),
    "index-sequence": ("jVGg<C-a>",
        "j moves to the email line and VG selects from there to the end. g<C-a> adds 1 to the first "
        "number on the first selected line, 2 on the second, 3 on the third. Plain <C-a> would add 1 to "
        "all of them. To number a list from scratch, write every line as 0 and use VGg<C-a>, or make "
        "steps of 4 with 4g<C-a>."),
    "change-column": ("<C-v>2jecprivate<Esc>",
        "<C-v>2j selects the first column of the three public's, and e stretches the block to the end of "
        "the word. c deletes the block and inserts on the first line, and <Esc> copies \"private\" to the "
        "other two. The dot formula has trouble here: after cwprivate<Esc>, the cursor is in the wrong "
        "place for j., so you'd need cwprivate<Esc>+.+. (14 keys)."),
    "pipe-table": ("w<C-v>GI| <Esc>2w.",
        "w jumps to the year column. <C-v>GI| <Esc> inserts \"| \" in front of it on all four lines. 2w "
        "moves to the typed column on the first line, and . repeats the block insert there, with the "
        "same height. That's the dot formula with a block: one key to move, one key to repeat."),
    "quote-words": ("<C-v>3jI\"<Esc>gv$A\",<Esc>",
        "<C-v>3jI\"<Esc> puts the opening quote in front of every name. gv reselects the block you just "
        "used, and $ turns it into a ragged block that reaches each line's end. A\",<Esc> appends the "
        "closing quote and comma. Typing <C-v>3j again instead of gv works too, one key longer. You can "
        "also do it in the other order: <C-v>3j$A\",<Esc>gvI\"<Esc>."),
    "center-title": ("vip:ce30<CR>",
        "vip selects the banner, which is a paragraph. Pressing : in Visual mode starts the command line "
        "with :'<,'>, the range of selected lines. :ce30 is short for :center 30 (the space is optional), "
        "which centers each line in 30 columns. The rules are already 30 wide, so they don't move. :2,4ce30 "
        "is the same length. :right 30 and :left would right- or left-align instead."),
    "box-edge": ("<C-v>2j19|A|<Esc>",
        "<C-v>2j selects the three middle lines. 19| moves to column 19, which is past the end of every "
        "line: that's only possible because virtualedit=block is set. A types after the block's right "
        "edge, and Vim pads each short line with spaces up to it, so the | lands in column 20 under the "
        "+. With $ instead of 19|, each | would go right after its own line's text."),
    "move-sun": ("<C-v>2j4lygvr<Space>30|P",
        "<C-v>2j4ly yanks the sun as a 3-by-5 block. gv reselects it, and r<Space> blanks it out without "
        "moving anything else, which d would not do. 30| jumps to column 30 (possible past the end of "
        "the line because virtualedit=all), and P puts the block with its top-left corner at the cursor. "
        "Pasting first and blanking after also works: <C-v>2j4ly30|Pgvr<Space>."),
    "review-value-class": ([
        ("4jWifinal <Esc>", "step 1: W hops to class, and final goes in front of it."),
        ("fP*", "step 2: * searches for Point as a whole word, so it skips nothing and stops at the constructor."),
        ("iGeo<Esc>", "step 2: the new name only adds to the front, so the insert can go at the start of the "
                      "word, which is where n leaves the cursor..."),
        ("n.n.n.n.", "step 2: ...and n then . renames the other four: scale()'s return type, new Point, the "
                     "text in toString(), and, wrapping around, the class line. GeoPoint no longer matches "
                     "\\<Point\\>, so each one is only changed once."),
        ("+<C-v>2jecprivate final<Esc>", "step 3: + lands on the first public. A block over the three "
                                          "publics, then c types private final on all of them."),
        ("5+<C-v>2jIthis.<Esc>", "step 4: block I puts this. in front of the three assignments."),
        ("5jf_<C-v>2jd", "step 5: the underscores line up, so a one-column block deletes all three..."),
        ("gvU", "step 5: ...and gv selects the same block again, which now holds x, y and z. U uppercases them."),
        ("5jfza * k<Esc>", "step 6: z only appears once on the line."),
        ("4jF(r[$F)r]", "step 7: F( searches back to the (, r swaps it for [, and $F) finds the last ) on the "
                        "line, the one inside the quotes."),
        ("kO@Override<Esc>", "step 8: O opens a line above the method's."),
        ("5j.", "step 9: . repeats the whole O@Override<Esc>."),
        ("2jf)i, z<Esc>", "step 10, last because it ends in Insert mode."),
    ], "Down the file once. The rename is an insert at the front of each match, which n and . repeat, and "
       "the three column edits are three blocks. The bracket fix comes before the @Override lines, so . "
       "still remembers O@Override when it's needed for hashCode()."),
    "review-release-notes": ([
        (":ce60<CR>", "step 1: :ce is :center, and 60 is the width."),
        ("j:ri60<CR>", "step 2: :ri is :right."),
        ("jjyypVr=", "step 3: yyp copies the heading, and Vr= turns every character of the copy into =."),
        ("jgqq", "step 4: gqq rewraps the paragraph's one long line to 'textwidth'."),
        ("jjyypVr=", "step 3 again, for Fixes."),
        ("j<C-v>2jg<C-a>", "step 5: in block mode, g Ctrl-a only changes numbers inside the block. It adds 1, "
                           "2 and 3."),
        ("gvI  <Esc>", "step 6: gv reselects the same block, and I types two spaces in front of it."),
        ("jfsRll<Esc>", "step 7: push and pull only differ in their last two letters, so R types over them."),
        ("3jyypVr=", "step 3 again, for Platforms."),
        ("j3w<C-v>4j$d", "step 9: tested is the last column, so a block from its first letter to $ deletes "
                         "it on all five lines. The spaces left at the ends don't count."),
        ("gUU", "step 8: gUU uppercases the header line."),
        ("4jyypwRarm64 ", "step 10, last because it ends in Replace mode: arm64 and a space are exactly as "
                          "wide as x86_64, so R keeps the columns lined up."),
    ], "Top to bottom. The Ex commands that align lines have short names (:ce, :ri), yyp Vr= is the classic "
       "underline, and the fix list is one block for g Ctrl-a and the same block again, via gv, for I."),
}
