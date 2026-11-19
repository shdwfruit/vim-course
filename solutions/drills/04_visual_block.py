"""Reference solutions for Project 04's drills (spoilers!). Each entry: drill -> (keys, explanation).

See one with:  python3 check.py drill visual --show 3      Watch it typed:  python3 check.py drill visual --watch 3
"""
SOLUTIONS = {
    # ---------- v ----------
    "visual-1": ('vi"r*',
        'vi" selects the text inside the quotes. Like the text object after an operator, it looks ahead on the '
        "line for a string when the cursor isn't in one. r* replaces every selected character with a *, so you "
        "get eleven stars without counting them. The count version, ft11r*, is a key longer."),
    "visual-2": ("veU",
        "v starts selecting, e moves to the end of max_clients (the underscores are part of the word), and U "
        "uppercases the selection. gUe is just as short: in Visual mode, U, u and ~ are the one-key versions of "
        "gU, gu and g~. Prefer the operator if you want to repeat it with ., because . repeats a Visual change "
        "on the same number of characters, not on the same word."),
    "visual-3": ("fBv4eu",
        "fB lands on the B of BACK (f is case-sensitive, and there's no capital B before it). v4e selects "
        "through the end of DATABASE, and u lowercases everything selected. gu4e is the same length."),
    "visual-4": ("yejf3vp",
        "ye yanks MAX_RETRIES. j goes down a line in the same column, and f3 finds the 3. v selects that one "
        "character, and p replaces it with the yanked text. Typing the name after s would take 13 keys: a yank "
        "and a Visual p don't care how long the name is."),
    "visual-5": ("yi(jvi(p",
        "yi( yanks everything inside the parentheses (from the start of the line, i( looks ahead for them) and "
        "leaves the cursor at the start of what it yanked. j moves into fillRect's parentheses, vi( selects its "
        "arguments, and p puts the yanked ones in their place. Copying the line with yyjVp and then fixing the "
        "name is longer."),
    "visual-6": ("vi[r#100<C-a>",
        "vi[ selects the 14 spaces inside the brackets, and r# turns each one into a #. That leaves the cursor at "
        "the start of the bar, so 100 Ctrl-a adds 100 to the next number on the line, the 0. (f0i10 is the same "
        "length.) Filling by count, f[l14r#, is two keys longer, and you'd have to count the cells."),
    "visual-7": ("dewvepF(p",
        "de deletes actual into the register and leaves the cursor on the comma. w moves to expected, and vep "
        "replaces it with actual. A Visual p puts the text it replaced into the register, so now the register "
        "holds expected. F( goes back to the parenthesis, and p puts expected after it. Retyping both names "
        "takes twice as many keys."),
    "visual-8": ("yejwv%p",
        "ye yanks distance. j and w put the cursor on math in line 2. In Visual mode, % finds the next "
        "parenthesis on the line and jumps to its match, so v% selects the whole call, and p replaces it with "
        "distance. c%distance works too, but typing the name costs more than yanking it."),
    "visual-9": ("5wdejvepkP",
        "5w gets to width, and de deletes it. j lands on the h of height, because the two lines line up. vep "
        "puts width over height and leaves height in the register. k goes back to line 1, where the cursor "
        "ends up on the ; because the line got shorter, and P puts height in front of it."),
    "visual-10": ('yi"jvi"Pjvi"P',
        'yi" yanks the URL and leaves the cursor inside it. j moves into the next string, vi" selects it, and P '
        "replaces it. With p, the register would now hold the old mirror's URL, and the next put would paste "
        "that. P leaves the register alone, so the second vi\"P puts the primary URL again. . doesn't help "
        "here: repeating a Visual put only deletes."),
    "visual-11": ("$vT=r*",
        "$ goes to the last character of the token. v starts selecting there, and T= stretches the selection "
        "back to just after the =. r* turns every selected character into a *, without counting them. "
        "f=lv$r* is a key longer, and so is the count version, f=l18r*, which needs counting too."),
    "visual-12": ("yEjvEp",
        "An IP address is one WORD (dots aren't spaces), so yE yanks 10.0.0.5 from column 1. j goes to "
        "line 2, still in column 1, vE selects the old address, and p puts the new one in its place. The "
        "new address is shorter, so the name moves left. yiW and viW work too, a key longer each."),
    "visual-13": ("yi[jvi[p",
        "yi[ yanks the inside of devHosts' brackets (from column 1, i[ finds them further along the line). j "
        "goes to line 2, vi[ selects the inside of testHosts' brackets, and p replaces it. Copying the line "
        "with yyjVp and fixing the name takes more."),
    "visual-14": ("vitr*",
        "it is the inside of the tag around the cursor, the <code> element's text, so vit selects the whole "
        "key from its middle. r* turns each character into a *, and the tags stay. With a count you'd go "
        "back to the start first: F>l13r* is 7 keys, and you have to count."),
    "visual-15": ("yejvi(p",
        "ye yanks config. j goes to the start of line 2, and vi( looks ahead for the parenthesis and selects "
        "everything inside it, across both lines, line break included. p replaces all of that with config. "
        "With an operator, ci( would make you type the name: 10 keys."),
    "visual-16": ("yyplvt|r-7l.",
        "yyp copies the header line below itself. l moves onto the space after the first |, vt| selects up "
        "to just before the next |, and r- turns those 6 characters into dashes. The cursor is back on the "
        "first dash, and 7l jumps over the 6 dashes and the middle | to the start of the second cell. . "
        "repeats the Visual r- on 6 characters from there, which is exactly that cell. f|l instead of 7l is "
        "a key longer. yypVr- and then putting the three | back with r takes 16 keys."),
    "visual-17": ('3wvjt"r#',
        "3w lands just inside the opening quote: the quote is a word of its own, and the is the third word. "
        "v starts the selection, j takes it down to line 2 (a charwise selection runs from the start "
        "position, along the line break, to the cursor), and t\" stops it just before the closing quote. r# "
        "replaces every selected character with a #, and leaves the line break alone. f\"l instead of 3w is "
        "a key longer. i\" can't do this, because quotes only pair up within a line."),
    "visual-18": ("f2y$*vEp",
        "f2 lands on the date (there's no 2 earlier on the line), and y$ yanks it to the end of the line. "
        "The cursor is on 2026, a word of its own, and * jumps to the next 2026, the start of CURRENT's "
        "date. vE selects the date (it's the end of the WORD), and p puts BASE's date there. jf2 instead of "
        "* is 2 keys longer, and typing the date over with cE takes 15."),
    "visual-19": ('vi"r*j.',
        'vi" selects hunter22 and r* turns it into stars, leaving the cursor at the start of the selection. '
        "The values line up, so j lands on the first letter of letmein!, and . repeats the Visual r* on the "
        "same number of characters, 8, from the cursor. Both passwords are 8 long, so that's exactly the "
        "second one. With different lengths you'd need vi\"r* again."),
    "visual-20": ("Wy$jwvep",
        "W jumps over Name: to Ada, and y$ yanks Ada Lovelace. j goes to line 2 in the same column, which is "
        "the space before the blank, and w moves onto the blank. ve selects it (_ is a word character, so e "
        "stops at the last _ before the !), and p replaces it with the name."),

    # ---------- V ----------
    "visual-line-1": ("VU",
        "V selects the line and U uppercases it. gUU does the same in 3 keys."),
    "visual-line-2": ("jVjrX",
        "j goes to the first key line, Vj selects it and the next, and rX replaces every character on both "
        "with an X. The lines have different lengths, which is why 36rX followed by . doesn't work: the count "
        "is wrong for the second line."),
    "visual-line-3": ("yypVr=",
        "yyp puts a copy of the line below it and moves the cursor there. Vr= turns every character on the "
        "copy into a =, so the underline is exactly as long as the heading. yyp13r= also works, but it's a key "
        "longer and you have to count."),
    "visual-line-4": ("jyy2jVp",
        "jyy yanks line 2, 2j goes to line 4, and Vp replaces that line with the yanked one. Without Visual "
        "mode, dd would overwrite the yank, so you'd have to delete first and yank after: 3jddkyyjp, 9 keys."),
    "visual-line-5": ("VG10<C-a>",
        "VG selects from here to the last line. 10 Ctrl-a adds 10 to the first number on each selected line. "
        "In Normal mode you'd need 10 Ctrl-a and then j. three times, 9 keys."),
    "visual-line-6": ("jyjGVkp",
        "jyj yanks lines 2 and 3. G jumps to the last line, Vk selects the test host and port, and p replaces "
        "them with the yanked lines. Putting first and deleting after, jyjGpkdk, is a key longer."),
    "visual-line-7": ("ddjVpkP",
        "dd deletes the print line, and the cursor lands on the total line. j goes to the price line, and Vp "
        "replaces it with the print line, which puts the price line in the register. k and P put it above the "
        "total line. Swapping with dd and p alone takes about 9 keys."),
    "visual-line-8": ("jyy4jVP4jVP",
        "jyy yanks the right line. 4j goes to save's log line, and VP replaces it. With p, the line it replaced "
        "(log = print) would go into the register, and the second put would paste that. P leaves the register "
        "as it was, so 4jVP fixes delete's line too."),
    "visual-line-9": ("V~2j.",
        "V~ flips every letter on the line. 2j goes to line 4, and . repeats the Visual ~ on one line there. "
        "g~~2j. also works, a key longer."),
    "visual-line-10": ("yyPVr#yyjp",
        "yyP puts a copy of the comment above it, with the cursor on the copy. Vr# turns every character into "
        "a #. yy yanks that row, j moves down to the comment, and p puts the row below it. 14r# instead of Vr# "
        "costs a key more."),
    "visual-line-11": ("VG2<C-a>",
        "VG selects from line 2 to the last line. In Visual mode, Ctrl-a adds to the first number on every "
        "selected line, and the count says how much, so all three line numbers go up by 2. app.js has no "
        "digits, so the first number is the line number. In Normal mode it takes 2 Ctrl-a and then j. twice "
        "(6 keys)."),
    "visual-line-12": ("Vr=G.",
        "Vr= turns every character on line 1 into a =, corners included, without counting the 14 "
        "characters. G goes to the last line, and . repeats the Visual r= on one line there. 14r= and G. "
        "would be a key longer, and you'd have to count."),
    "visual-line-13": ("V3<lt>",
        "In Visual mode, a count before < is a number of levels, so V3< shifts the line left three times by "
        "4 spaces: 16 becomes 4. In Normal mode, 3<< would shift three lines one level each, so you'd need "
        "<<.. (4 keys). == doesn't help: Python's rules leave the indentation of a line like this alone."),
    "visual-line-14": ("yyGVp",
        "yy yanks line 3. G jumps to the last line, the TODO, and Vp replaces it with the yanked line, "
        "indentation included. Without Visual mode it's yyGpkdd, 7 keys, since dd first would overwrite the "
        "yank."),
    "visual-line-15": ("Vu",
        "V selects the line and u lowercases it. In Visual mode u doesn't undo: it's the one-key version of "
        "gu. guu does the same in 3 keys."),
    "visual-line-16": ("VU*.",
        "VU uppercases line 1. The cursor is still on its first word, and * searches for that word, "
        "VERSION, and with 'ignorecase' it finds version on line 4. . repeats the Visual U on one line "
        "there. 3j instead of * is a key longer, and gUU*. is a key longer too."),
    "visual-line-17": ("djGVkpggp",
        "dj cuts the deploy step's two lines. G goes to the last line, and Vk selects it and the line above, "
        "the build step. p puts deploy there, and the build lines it replaced go into the register. gg goes "
        "to line 1, and p puts the build step below it. Moving the steps with dd and p alone takes more."),
    "visual-line-18": ("jy2jGpVG10<C-a>",
        "j and y2j yank the three dev settings. G goes to the last line, [staging], and p puts the copies "
        "below it with the cursor on the first one. VG selects the copies, and 10 Ctrl-a adds 10 to the "
        "first number on each line: the ports."),
    "visual-line-19": ("y2jGVp",
        "y2j yanks the three signature lines. G goes to the placeholder, and Vp replaces that one line with "
        "all three. Putting first and deleting after, y2jGpkdd, is 2 keys longer, and dd first would "
        "overwrite the yank."),
    "visual-line-20": ("Vj100<C-a>4j.",
        "Vj selects .modal and .overlay, and 100 Ctrl-a adds 100 to the first number on each, the z-index "
        "(the class names have no digits). The cursor goes back to the top of the selection, so 4j reaches "
        ".toast, and . repeats the Visual Ctrl-a on two lines, with the same count. In Normal mode it would "
        "be 100 Ctrl-a and then j. 3j. j., 11 keys."),

    # ---------- Ctrl-v I A $A ----------
    "block-insert-1": ("<C-v>3jI- [ ] <Esc>",
        "Ctrl-v 3j selects the first column of the four steps. I inserts in front of the block. You only see "
        "\"- [ ] \" on the first line until <Esc>, which copies it to the other three. Typing it once and "
        "repeating it with j. takes 14 keys."),
    "block-insert-2": ("<C-v>3jI * <Esc>",
        "A block in the first column of lines 2 to 5, then I * <Esc>. gc can't do this: it would add C comment "
        "markers, not stars. I * <Esc>j.j.j. takes 11 keys."),
    "block-insert-3": ("<C-v>3j$A \\<Esc>",
        "Ctrl-v 3j selects lines 1 to 4, and $ makes the block reach the end of each one. A then appends \" \\\" "
        "after each line's own end. Without the $, A would add the text after the block's right edge and pad "
        "the shorter lines with spaces up to it. A \\<Esc>j.j.j. takes 10 keys."),
    "block-insert-4": ("<C-v>GI> <Esc>",
        "Ctrl-v G selects column 1 on every line. The block starts in column 1, so even the blank lines are "
        "long enough to reach it, and I puts \"> \" on them too (the grader ignores the trailing space). A "
        "block that starts further right skips lines that are too short."),
    "block-insert-5": ("<C-v>3jIself.<Esc>",
        "The block starts in column 5, on width, and goes down to the area line. The blank line is too short to "
        "reach column 5, so I skips it, which is just what you want here. Iself.<Esc>j.jj. takes 12 keys."),
    "block-insert-6": ("<C-v>2jIfinal <Esc>",
        "The types line up in column 13, so a one-column block there marks the spot on all three lines, and I "
        "types \"final \" in front of it. The dot formula is clumsy here: after the first insert the cursor isn't "
        "on the next line's type, so every line needs +w. (14 keys)."),
    "block-insert-7": ("<C-v>2jEA:00<Esc>",
        "Ctrl-v 2j goes down the first column, and E moves to the end of 11:05, so the block is exactly the "
        "time column. A types after its right edge, which is in the middle of each line here, not at the end. "
        "Ea:00<Esc> and then +E. on each other line takes 12 keys."),
    "block-insert-8": ("<C-v>jI0x<Esc>W.W.W.",
        "Ctrl-v j I0x<Esc> prefixes the first byte on both lines and leaves the cursor at the top of the block. "
        "W jumps to the next byte, and . repeats the block insert there, two lines tall. Three W. pairs do the "
        "rest: 12 keys for eight bytes."),
    "block-insert-9": ("<C-v>2jIvfs_<Esc>",
        "The return types are padded so that the names line up, and a block in that column lets I prefix all "
        "three at once. The dot formula needs +w before each . (12 keys)."),
    "block-insert-10": ("<C-v>4jI| <Esc>2W.gv$A |<Esc>",
        "Ctrl-v 4jI| <Esc> starts every line with \"| \". 2W jumps two WORDs to the Action column, and . "
        "inserts \"| \" there on the same five lines. gv brings back the first block, $ stretches it to each "
        "line's end, and A |<Esc> closes every row. Selecting again with Ctrl-v 4j$ instead of gv$ costs a key "
        "more."),
    "block-insert-11": ("<C-v>2jIlocal <Esc>",
        "Ctrl-v 2j selects the first column of the three lines, and I types \"local \" in front of the block. "
        "It shows on the first line only until <Esc>, which copies it to the other two. Ilocal <Esc>j.j. "
        "takes 12 keys."),
    "block-insert-12": ("<C-v>2jIu.<Esc>",
        "The three names start in column 5, under the cursor. Ctrl-v 2j makes a one-column block there, and "
        "Iu.<Esc> puts the alias in front of each name. Iu.<Esc>j.j. is a key longer, and the gap grows with "
        "every extra line."),
    "block-insert-13": ("<C-v>2j$A,<Esc>",
        "Ctrl-v 2j selects the three item lines, and $ makes the block reach the end of each one, however "
        "long. A, then appends a comma after each line's own end. A,<Esc>j.j. takes 7 keys too: the dot "
        "formula ties when there are only three lines."),
    "block-insert-14": ("<C-v>2jI  <Esc>",
        "> would shift by 'shiftwidth', 4 spaces, which is too far for this file. A block insert types "
        "exactly what you give it: Ctrl-v 2j selects the first column of lines 2 to 4, and I followed by two "
        "spaces and <Esc> indents all three by 2."),
    "block-insert-15": ("e<C-v>2jA:<Esc>",
        "e moves to the t of host, the end of the key, which is column 4 on every line. Ctrl-v 2j makes a "
        "one-column block there, and A types the colon right after it, in the middle of each line. The "
        "values move one column right, together. With ea:<Esc> you'd need a motion back to the key's end and "
        "a . on each other line."),
    "block-insert-16": ("w<C-v>8jI0<Esc>",
        "w moves onto the 1. Ctrl-v 8j runs the block down to Track 9 (the relative line numbers show the "
        "8), and I0<Esc> puts a 0 in front of each number. Track 10 is outside the block. With the dot "
        "formula you'd need j. eight times."),
    "block-insert-17": ('<C-v>2jI"<Esc>gv$A"<Esc>',
        'Ctrl-v 2j I"<Esc> opens a quote in front of the three names. gv selects the same block again, $ '
        'stretches it to each line\'s end, and A"<Esc> closes the quotes. Doing $A" first and then gvI" is '
        "the same length. Selecting again with Ctrl-v 2j instead of gv costs a key more."),
    "block-insert-18": ("j<C-v>jIexport <Esc>3j.",
        "j skips the comment, and Ctrl-v j I export <Esc> puts the prefix on the two database lines. The "
        "cursor goes back to the top of the block, so 3j reaches REDIS_HOST, and . repeats the block insert "
        "on a block of the same size, two lines. A block over all five lines would put export in front of "
        "# cache too."),
    "block-insert-19": ("<C-v>j$A;<Esc>*.",
        "Ctrl-v j$ selects the first rule's two declarations to their ends, and A;<Esc> appends the "
        "semicolons. The cursor is back on color, and * jumps to the next color, the second rule's first "
        "declaration. . repeats the block append there, on two lines, with the ragged $ edge too, so each ; "
        "lands at its own line's end. 4j instead of * is a key longer."),
    "block-insert-20": ("2w<C-v>jI--<Esc>W.",
        "2w moves onto oneline. Ctrl-v j makes a one-column block on the two lines, and I--<Esc> puts -- in "
        "front of oneline and stat. The cursor is back at the top of the block, W jumps to graph, which lines "
        "up with patch, and . repeats the block insert there."),

    # ---------- Ctrl-v c r d y ----------
    "block-edit-1": ("<C-v>3jrx",
        "Ctrl-v 3j selects the space inside each box, one column on four lines, and rx turns them all into x. "
        "rxj.j.j. takes 8 keys."),
    "block-edit-2": ("<C-v>Gld",
        "Ctrl-v G selects column 1 on every line (G keeps the column), l makes the block two columns wide to "
        "take the space too, and d deletes the rectangle. 2xj.j.j. takes 8 keys."),
    "block-edit-3": ("l<C-v>2jecDONE<Esc>",
        "l moves onto the T, Ctrl-v 2j selects that column on the three lines, and e stretches the block to "
        "the end of TODO. c deletes the block and starts inserting on the first line, and <Esc> copies DONE to "
        "the others. lciwDONE<Esc>j.j. takes 13 keys."),
    "block-edit-4": ("<C-v>GU",
        "Ctrl-v G selects the first letter of every line from here to the end, and U uppercases the block. "
        "~+.+.+. takes 7 keys."),
    "block-edit-5": ("<C-v>2jEr<Space>",
        "Ctrl-v 2j goes down the first column. On the last line, E jumps to the end of the WORD (___.__)__), "
        "the widest part of the cloud. r and a space replace every character in the block with a space, so "
        "nothing to its right moves. With 12r and a space you'd also need j0. for each of the other two lines "
        "(10 keys)."),
    "block-edit-6": ("w<C-v>GEld",
        "w moves to the date column. Ctrl-v G runs the block down to the last line, keeping the column, and E "
        "stretches it to the end of that line's date (a date is a single WORD). l takes the space after it "
        "too, and d deletes the rectangle, so the city column slides left. wdWj.j.j.j. takes 11 keys."),
    "block-edit-7": ("W<C-v>G>",
        "W jumps to localhost, the start of the names column. Ctrl-v G makes a one-column block from there to "
        "the last line, and > pushes everything from the block's left edge one shiftwidth (4 spaces) to the "
        "right. The addresses don't move. Block-inserting four spaces would take 9 keys."),
    "block-edit-8": ("<C-v>3j$c0,<Esc>",
        "Ctrl-v 3j$ selects from the column of the values to the end of each line, however long. c deletes all "
        "of that and types 0, on every line. cw0<Esc>j.j.j. takes 10 keys."),
    "block-edit-9": ("<C-v>3jt|d$P",
        "Ctrl-v 3j covers the four rows, and t| stretches the block to the column before the second |. d cuts "
        "out \"| Country   \" and the rest of that column, leaving \"| Code |\". $ goes to the closing |, and "
        "P puts the block in front of it as a rectangle, on all four lines at once."),
    "block-edit-10": ("f+<C-v>Gt+y$PjwRWednesday",
        "f+ moves to the + where the Tuesday column starts. Ctrl-v G goes down to the last line in that "
        "column, t+ stretches the block to just before the next +, and y copies the column. $ goes to the "
        "last character of line 1, and P puts the block in front of it on all six lines, so the table grows by "
        "a column. jw lands on the new Tuesday, and RWednesday types over it and over two of the spaces after "
        "it, so the cell keeps its width."),
    "block-edit-11": ("<C-v>2jeclong<Esc>",
        "Ctrl-v 2j selects column 1 on the three lines, and e stretches the block to the end of int. c deletes "
        "the block and types long on the first line, and <Esc> copies it to the others. cwlong<Esc> and then "
        "+.+. takes 11 keys, and the gap grows with every line."),
    "block-edit-12": ("<C-v>2jr|",
        "The cursor is on the space in column 7, and Ctrl-v 2j makes a one-column block of it down the three "
        "lines. r| replaces every character in the block, so the column of spaces becomes a line. r|j.j. is a "
        "key longer."),
    "block-edit-13": ("f;l<C-v>3j$d",
        "f; and l put the cursor just after the semicolon, where the comments' spaces start, in the same "
        "column on all four lines. Ctrl-v 3j covers the lines, $ makes the block reach each line's end, "
        "however long the comment, and d deletes it. With D you'd have to put the cursor back after the ; on "
        "every line: f;lD and then j and . don't line up, since D leaves the cursor on the ;."),
    "block-edit-14": ("l<C-v>j$y$p",
        "l moves to column 2, and Ctrl-v j$ selects from there to the end of both lines. y copies the block and "
        "puts the cursor back at its top-left corner. $ goes to the end of line 1, and p puts the block after "
        "it, as a rectangle, on both lines: the fence doubles."),
    "block-edit-15": ("<C-v>2jeu",
        "Ctrl-v 2j runs down the first column, and e stretches the block to the end of 0x1F, so the block is "
        "exactly the four-character codes. u lowercases what's selected: the F, the F and the A (x and the "
        "digits have no case to change). The names are outside the block. guiw then j. on each line takes 8."),
    "block-edit-16": ("<C-v>2j5ldWP",
        "Ctrl-v 2j5l selects the level column and the space after it (6 wide, since ERROR is the longest "
        "level), and d cuts it. Every line now starts with its time, W jumps over it to the message, and P "
        "puts the block in front of the cursor on all three lines. E wouldn't do for the width: it would stop "
        "at the end of INFO on the last line."),
    "block-edit-17": ("w<C-v>jUw.",
        "w moves onto the l of lima, Ctrl-v j makes a one-column block on the two cities' first letters, and U "
        "uppercases them. The cursor is back at the top of the block, w jumps to peru, which lines up with "
        "india, and . repeats the block U on a block of the same size there. W instead of w is a tie."),
    "block-edit-18": ("jl<C-v>j5lr.",
        "j and l move onto the first space inside the box. Ctrl-v j5l selects the 2-by-6 inside, and r. fills "
        "it with dots, leaving the edges alone. jt| instead of j5l is the same length, and avoids counting."),
    "block-edit-19": ("2w<C-v>2j3ly6l<C-v>2j3lp",
        "2w lands on the window's top-left corner: the whole top border is one word, so the first w goes to "
        "the | on line 2 and the second to the window. Ctrl-v 2j3l selects the 3-by-4 window, and y copies "
        "it and brings the cursor back to the corner, in column 4. 6l moves to column 10, Ctrl-v 2j3l "
        "selects a block of spaces of the same size, and p replaces it with the window. P would insert the "
        "window and push the wall out of line, and typing the three rows with R takes about 27 keys. P over "
        "the selection is a tie."),
    "block-edit-20": ("<C-v>2j3ld$p",
        "Ctrl-v 2j3l selects the first four columns, 001| and the others, and d cuts them out. The lines are "
        "all the same length, so $ goes to the last | on line 1, and p puts the block after it, on all three "
        "lines. If the lines had different lengths, the block would land in line 1's last column on every "
        "line."),

    # ---------- o O gv ----------
    "visual-ends-1": ("<C-v>2j2EA]<Esc>gvI[<Esc>",
        "Ctrl-v 2j2E selects the date and time column, and A]<Esc> adds a ] after it on every line. gv selects "
        "the same block again, and I[<Esc> adds the [ in front. Doing the [ first is awkward: it pushes the text "
        "right by one, so the block that gv brings back would end one column short."),
    "visual-ends-2": ("<C-v>5j19lr#gvkhojlr<Space>",
        "Ctrl-v 5j19l selects the 6-by-20 rectangle (past the line ends, thanks to virtualedit=all), and r# "
        "fills it. gv selects it again with the cursor back in the bottom-right corner. kh moves that corner in "
        "by one, o jumps to the top-left corner, jl moves it in by one, and r and a space empty the inside. "
        "Selecting the inside from scratch is a key longer, and so is drawing the four sides with r and ."),
    "visual-ends-3": ("<C-v>2jEygvr<Space>j20|P",
        "Ctrl-v 2j goes down the first column, and E stretches the block to the end of the moon's bottom line, "
        "so y yanks the moon as a 3-by-4 block. gv selects it again, and r and a space blank it out without "
        "moving the stars, which d would not do. j goes down a line, 20| jumps to column 20 (past the end of "
        "the line, because virtualedit=all), and P puts the block with its top-left corner there."),
    "visual-ends-4": ('2w<C-v>2jlUgvA"<Esc>gvI"<Esc>',
        "2w lands on the m of ma (the comma is a word of its own). Ctrl-v 2jl selects the 2-by-3 block of "
        "codes, and U uppercases it. gv brings the same block back, and A\"<Esc> closes the quotes after it "
        "on every line. gv again (the block is still the codes' columns) and I\"<Esc> opens them. Doing I\" "
        "first would push the codes right, and the next gv would end one column short. Selecting the block "
        "again from scratch costs more each time."),
    "visual-ends-5": ('yi"jT_vepgvU',
        "yi\" yanks authentication. j goes to line 2, where the cursor ends up on the 1 at the end, and T_ "
        "goes back to just after the _, on XXX. ve selects XXX and p puts the string over it. After a Visual "
        "p, gv selects the text that was put, so U uppercases exactly that. gUiw would also do it, a key "
        "longer, and typing the long name with cw takes 20 keys."),
    "visual-ends-6": ("<C-v>2jly$h<C-v>2jlpgvU",
        "Ctrl-v 2jl selects the codes in column 1, and y copies them. $h moves to the first x on line 1, and "
        "Ctrl-v 2jl selects the xx block. p replaces it with the codes, and gv selects the block you just "
        "put, so U uppercases the copies only. 3W instead of $h is a tie. Uppercasing first would change "
        "column 1 too."),

    # ---------- g Ctrl-a ----------
    "g-ctrl-a-1": ("<C-v>GI0. <Esc>gvg<C-a>",
        "Ctrl-v G I0. <Esc> writes \"0. \" in front of every step. gv selects that block again, and g Ctrl-a "
        "turns the zeros into 1, 2, 3, 4. Starting from 1. would give 2 to 5, because g Ctrl-a adds 1 even on "
        "the first line. VG instead of gv works too, in the same number of keys."),
    "g-ctrl-a-2": ("f0<C-v>2jg<C-a>",
        "f0 jumps to the 0 of guest0. Ctrl-v 2j makes a one-column block of the three zeros, and g Ctrl-a counts "
        "them up: 1, 2, 3. Only numbers inside the block change, so the ids are safe."),
    "g-ctrl-a-3": ("jVG4g<C-a>",
        "j skips REG_CTRL, which stays at 0. VG selects the other three lines, and 4 g Ctrl-a adds 4 to the "
        "first, 8 to the second and 12 to the third. Vim sees that these are hex numbers, so 12 comes out as "
        "0x0c."),
    "g-ctrl-a-4": ("VGg<C-a>",
        "VG selects the four server lines. g Ctrl-a adds 1 to the first number on the first line, 2 on the "
        "second, and so on, so the four web0s become web1 to web4. Plain Ctrl-a in Visual mode would make "
        "them all web1."),
    "g-ctrl-a-5": ("jVG10g<C-x>",
        "j skips .modal, which keeps 100. VG selects the other three, and 10 g Ctrl-x subtracts 10 from the "
        "first, 20 from the second and 30 from the third: 90, 80, 70. The class names have no digits, so the "
        "first number on each line is the z-index."),
    "g-ctrl-a-6": ("3l<C-v>2jl15g<C-a>",
        "3l puts the cursor on the minutes of the second talk. Ctrl-v 2jl makes a block over both digits of "
        "the minutes on lines 2 to 4, and 15 g Ctrl-a adds 15, 30 and 45. Neovim keeps the two digits. 2w "
        "or f0 instead of 3l is a tie. A one-column block would only see the first 0, so it would add to "
        "that digit alone, and V would change the hours."),

    # ---------- :'<,'> ----------
    "visual-ex-1": ("Va{:s/cfg./opts-><CR>",
        "Va{ selects the lines of the whole function, from the line with its { to the line with its }. : "
        "starts the command line with :'<,'>, so s/cfg./opts-> only changes those lines. (The . in the pattern "
        "matches any character, which is fine here; \\. would match only a dot.) :2,6s/... is the same length "
        "if you read the line numbers. Changing one with R and repeating it with n. takes at least 20 keys, "
        "and you have to step over the cfg in dump()."),
    "visual-ex-2": ("vip:norm W~<CR>",
        "vip selects the five entries, and : gives you :'<,'>. :norm (short for :normal) types its keys on "
        "every selected line, starting at the beginning of the line: W jumps over the type and its colon, and ~ "
        "flips the first letter. Doing it with W~ and then W. on each other line takes at least 14 keys, and "
        "vip:s/ ./\\U& (Project 07) takes 13."),
    "visual-ex-3": ("jVG:sor!n<CR>",
        "j skips the heading, and VG selects the scores. : gives you :'<,'>, and sor!n (short for sort! n) "
        "sorts those lines by the first number on each, biggest first. The shell's sort -rn would sort these by "
        "name, because the names come first on the line."),
    "visual-ex-4": ("V2j:ri30<CR>",
        "V2j selects the three address lines, and : starts the command line with :'<,'>. :ri30 (short for "
        ":right 30) adds spaces in front of each line until it ends in column 30. Vip is a tie with V2j. "
        "Typing the spaces by hand means counting them for every line."),
    "visual-ex-5": ("vip:sor u<CR>",
        "vip selects the tag paragraph, and : gives you :'<,'>. :sor u (short for :sort u) sorts the lines "
        "and keeps only the first of each run of equal lines, so each tag appears once. The headings are "
        "outside the range. !ipsort -u<CR> does the same through the shell, a key longer."),
    "visual-ex-6": ("VG:norm gUe<CR>",
        "VG selects the eight route lines, and : gives you :'<,'>. :norm gUe types gUe at the start of every "
        "selected line, which uppercases the method there, however long it is. A block can't do this, since "
        "the methods have different lengths, and gUe with j. on each line takes 17 keys. gUiw instead of gUe "
        "is a key longer."),

    # ---------- virtualedit N| ----------
    "virtualedit-1": ("<C-v>3j39|A\\<Esc>",
        "Ctrl-v 3j selects lines 1 to 4, and 39| stretches the block to column 39. That's past the end of every "
        "line, which only works because virtualedit=block is set. A appends after the block's right edge and "
        "pads each line with spaces up to it, so every \\ lands in column 40. With $ instead of 39|, each \\ "
        "would go right after its own line."),
    "virtualedit-2": ("14|<C-v>3jr|A>",
        "14| jumps to column 14, which is in empty space on every line, since virtualedit=all. Ctrl-v 3j makes "
        "a one-column block down to the last line, and r| draws the pole, filling the gap before it with "
        "spaces. A> appends the flag at the end of the top line, right after the pole."),
    "virtualedit-3": ("<C-v>3jEy10|P",
        "Ctrl-v 3j goes down the first column, and E stretches the block to the end of the bottom line, the "
        "widest, so y yanks the house as a 4-by-6 block. 10| jumps to column 10, past the end of the top line, "
        "and P puts the block with its top-left corner there. Every line is padded with spaces up to column 10 "
        "first."),
    "virtualedit-4": ("15|<C-v>2jrY",
        "15| jumps to column 15, the flag, on line 1. Ctrl-v 2j makes a one-column block there down the three "
        "records, and rY sets every flag. In a fixed-width file the spec gives you column numbers, and N| "
        "uses them directly. 2fN is a tie here (the N of ANA comes first), but it depends on the data."),
    "virtualedit-5": ("j20|i<lt>-- port 80<Esc>",
        "j goes to line 2, and 20| jumps to column 20, past the end of the line, which works because "
        "virtualedit=all is set. i inserts the label right there, and Neovim fills the gap before it with "
        "spaces. R is a tie. Without virtualedit you'd type A and nine spaces first."),
    "virtualedit-6": ("27|<C-v>j$d",
        "27| jumps to column 27, the space after the seventh byte. Ctrl-v j takes the block down to line 2, "
        "$ makes it reach the end of both lines, and d deletes it. The short last line isn't in the block. "
        "27|D, then jl. is a tie, and 7El instead of 27| would need you to count the bytes. No virtualedit "
        "is needed, since both lines are long enough."),
}
