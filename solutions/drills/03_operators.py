"""Reference solutions for Project 03's drills (spoilers!). Each entry: drill -> (keys, explanation).

See one with:  python3 check.py drill case --show 3      Watch it typed:  python3 check.py drill case --watch 3
"""
SOLUTIONS = {
    # ---------- gU gu g~ ~ ----------
    "case-1": ("gUe",
        "gU is the uppercase operator and e moves to the end of the word, which is inclusive, so gUe "
        "uppercases all of default_timeout (_ is a word character). gUw also works in 3 keys, and gUiw in "
        "4. gUU would uppercase the comment too."),
    "case-2": ("guu",
        "Doubled operators work on the whole line, like dd, so guu lowercases line 2. gu$ is a tie. The # "
        "has no case, so it stays."),
    "case-3": ("g~~",
        "g~~ flips the case of every letter on the line: lowercase becomes uppercase and the other way "
        "round, which is exactly what undoes Caps Lock. The digits and periods pass through. g~$ is a tie."),
    "case-4": ("2w~",
        "2w moves two words forward, onto the s of shoppingCart. ~ flips that one character and moves the "
        "cursor right. gUl would also work, in one more key."),
    "case-5": ("3~",
        "~ with a count flips that many characters, starting at the cursor: t, m and l become T, M and L. "
        "gUe would uppercase the whole rest of the word, Parser included."),
    "case-6": ("gUi{",
        "i{ is the inside of the braces, and when the cursor isn't inside any, it finds the next pair on "
        "the line. So gUi{ from column 1 uppercases \" low, normal, high \" and leaves Priority alone. "
        "gUa{ is a tie, since braces have no case."),
    "case-7": ("gUeff.fw.",
        "gUe uppercases select. ff jumps to the f of from (the first f on the line) and . repeats \"gU to "
        "the end of the word\" there. fw and . do the same for where. 4w. and 2w. instead of ff. and fw. "
        "are the same length."),
    "case-8": ("gUip",
        "ip is the paragraph around the cursor: the five comment lines between the blank lines. gUip "
        "uppercases them, and /* and */ have no letters to change. {gU} is a tie, and gUj would miss the "
        "first line of the warning."),
    "case-9": ("wlgu$",
        "w moves onto the G of GETTING and l onto the E after it. gu$ lowercases from there to the end of "
        "the line. guuw~ is a tie: lowercase everything, then flip the g back."),
    "case-10": ("fr2~;.",
        "fr jumps to the r of HttpUrl, the first r on the line. 2~ flips r and l to R and L and moves the "
        "cursor past them. ; repeats fr and finds the r in the second HttpUrl, and . repeats 2~ with its "
        "count. fU would also find the names, but then you'd need l before each 2~."),
    "case-11": ("gUiw",
        "iw is the whole word under the cursor, from anywhere inside it, and _ is a word character, so gUiw "
        "uppercases all of base_url. gUe from the u would leave base_ alone. bgUe is a tie: b goes back to "
        "the start of the word first."),
    "case-12": ('gui"',
        'i" is the text inside the quotes, and from column 1 it finds the string further along the line. gu '
        "lowercases it, and @ and the dots have no case. Wgu$ is a tie: W lands on the =, and gu$ lowercases "
        "from there to the end of the line."),
    "case-13": ("guG",
        "G is a line-wise motion to the last line, so guG lowercases every line from here to the end of the "
        "file. The keys and braces are already lowercase or have no case, so only True and False change. "
        "Fixing them one at a time, with jw~ and j., costs more."),
    "case-14": ("wgU$",
        "w moves from id to integer, and gU$ uppercases from there to the end of the line. The comma has no "
        "case. gUU would uppercase id as well."),
    "case-15": ("fM2~",
        "f is case-sensitive, so fM jumps straight to the M of XML (there's no other capital M on the line). "
        "2~ flips the M and the L. fMgue does the same in 5 keys: gu to the end of the word."),
    "case-16": ("2WgUej.j.",
        "2W jumps over the date and the time to info. gUe uppercases to the end of the word, and leaves the "
        "cursor at its start. The levels line up, so j lands on warn and . repeats gUe, then j. does error. "
        "gUw is the same length as gUe here, and gUiw is a key longer."),
    "case-17": ("w~w.3w.w.",
        "w moves onto the a, ~ flips it and steps right, and w and . do the same for tour. 3w skips of and the "
        "and lands on vim, where . flips the v, and w. does grammar. Pressing ~ instead of . is the same "
        "length: . shines when the command it repeats is longer."),
    "case-18": ("gue*.",
        "gue lowercases MAX_SIZE, because the cursor is on its first letter and _ is part of the word. Now "
        "the word under the cursor is max_size, and * searches for it as a whole word. * ignores 'smartcase' "
        "and uses 'ignorecase', so it matches MAX_SIZE on the next line. . repeats gue there. guiw instead of "
        "gue is a key longer."),
    "case-19": ('gui"3W.3W.',
        'gui" lowercases RED, the first string on the line, and leaves the cursor inside it. 3W jumps three '
        'WORDs to the opening quote of "GREEN", and . repeats gui" there: with the cursor on a quote, Vim '
        "works out which string it opens. 3W. again does BLUE. 4w is the same length as 3W. Lowercasing more "
        "at once would lowercase Red, Green and Blue too."),
    "case-20": ("guufu~",
        "guu lowercases the whole line, tags and text, which fixes the four tags in 3 keys. That also turns "
        "Use into use, so fu finds that u (the first one on the line) and ~ makes it a capital again. guu3w~ "
        "and guu3l~ are ties. Flipping the tag letters one by one, with l~ fB. ;. fP., takes 10 keys."),

    # ---------- = == ----------
    "equal-1": ("==",
        "== re-indents the current line by the filetype's rules. In C, a line inside a function's braces "
        "gets one level, 4 spaces. >> would add 4 to the 2 that are there and give 6."),
    "equal-2": ("=ip",
        "ip is the paragraph around the cursor, which is the whole sum() function. = works out each line's "
        "indentation from C's rules, so 2, 4 and 6 spaces become 4, 8 and 12. =ap is a tie. > and < can't "
        "do this, since they add or remove the same amount on every line."),
    "equal-3": ("=%",
        "% jumps from the { to its matching }, so =% re-indents every line from the for line down to the "
        "loop's closing brace, nested if included. =i{ would leave the closing } of the for loop out, and "
        "=a{ is one key longer."),
    "equal-4": ("gg=G",
        "gg goes to the first line and =G re-indents from there to the last one: the whole file. It's a "
        "good habit after pasting in C or Java. =G alone, from inside main(), would miss square()."),
    "equal-5": ("=j",
        "=j re-indents this line and the next. Python's rules indent the line after a line ending in a "
        "colon one level deeper, so the if goes to 8 and continue to 12. That's about all = knows about "
        "Python: it leaves most other lines alone. >j would add 4 to both and give 10 and 14. =ip also "
        "works here, in 3 keys."),
    "equal-6": ("=i{",
        "i{ is the inside of the braces around the cursor, the four lines of the loop body, and = re-indents "
        "them relative to the for line. =ip would also re-indent the hand-aligned \"name\", \"count\" line "
        "to Java's continuation indent. Here k=3j is one key longer."),
    "equal-7": ("=i{",
        "The cursor is inside the switch, so i{ is the lines between its braces. Java's rules indent case "
        "labels one level in from switch and the statements under them one more. =ap is also 3 keys here, "
        "because the whole class is one paragraph and everything else is already right."),
    "equal-8": ("ddkkP==",
        "dd cuts the line, and the cursor lands on the method's closing brace. kk goes up to the if's "
        "closing brace, and P puts the line above it, still at its old indentation. == re-indents it two "
        "levels deeper in one go, where >> would need a . as well. dd3kp is a tie."),
    "equal-9": ("=j8j.",
        "=j fixes area()'s two body lines and leaves the cursor on the first of them. 8j goes down to "
        "perimeter()'s first body line (the relative line numbers show the 8), and . repeats =j. gg=G "
        "would also re-indent the second line of SIDES, which is lined up by hand."),
    "equal-10": ("dapP=G",
        "At the end of a file, ap takes the paragraph plus the blank line before it, so dap cuts the blank "
        "line and norm(). The cursor lands on the class's }, and P puts the lines above it. P leaves the "
        "cursor on the first pasted line, the blank one, so =G re-indents from there to the end of the file: "
        "the method gets 4 and 8 spaces and the class's } goes back to column 1."),
    "equal-11": ("3==",
        "A count before == re-indents that many lines, starting with this one, like 3dd. C's rules give the "
        "if one level, the return under it (an if without braces) one more, and the printf goes back to one "
        "level, since only one line belongs to the if. =2j is a tie."),
    "equal-12": ("=G",
        "G is a line-wise motion to the last line, so =G re-indents from find()'s first line to the end of "
        "the file. C's rules indent each statement under a braceless for or if one level deeper. =ip is a "
        "key longer, and gg=G would also move \"beta\" to C's continuation indent."),
    "equal-13": ("=}",
        "} moves to the blank line after the function, and with an operator it becomes line-wise, so =} "
        "re-indents from line 1 down to there. Lua's rules indent after then and function and dedent at end. "
        "=ip is a key longer, and =G would also re-indent the table's two-space line."),
    "equal-14": ("=gg",
        "gg is a motion like any other, and = makes it line-wise, so =gg re-indents every line from the "
        "first one down to the cursor's. Motions work backwards too: you don't have to go to the top first. "
        "gg=4j is two keys longer, and gg=G would also re-indent the \"green\" line."),
    "equal-15": ("=ip",
        "ip is the paragraph around the cursor: the five lines of the loop. Neovim's shell rules indent "
        "after do and then and dedent at fi and done. =} or =G from the gzip line would miss the if line "
        "above, and k=} is a tie."),
    "equal-16": ("=2}",
        "2} moves to the second blank line, after hi(), so =2} re-indents both functions from line 1 in one "
        "go. =9j is a tie (the relative line numbers show the 9), and =2ap is a key longer. gg=G would move "
        "the hand-aligned second line of LIMITS."),
    "equal-17": ("=2i{",
        "i{ is the inside of the innermost braces, the if's, so =i{ would only fix go(). With a count, 2i{ is "
        "the inside of the braces one level out, run()'s body: start(), the whole if, and stop(). =ip would "
        "also re-indent \"build\", since the class is one paragraph."),
    "equal-18": ("4j=i{",
        "4j goes down from the if to the first line inside the else (the relative line numbers show the 4). "
        "There, i{ is the inside of the else's braces, and = re-indents the three lines. 4j=2j is a tie. =i{ "
        "from the if's line would re-indent the whole method body, the hand-aligned - o.coupon() line too."),
    "equal-19": ("yy5jP=j",
        "yy copies the guard, 5j goes down to load(), and P puts the copy above it, at its own indentation, "
        "with the cursor on it. =j re-indents the copy and load(), which goes from 8 spaces to 4. yy5jPj<< "
        "is a key longer."),
    "equal-20": ("$=%",
        "$ moves onto the { at the end of the switch line, and % jumps from there to the matching }. So =% "
        "re-indents the switch's lines: case labels one level in from switch, and the returns one more. "
        "From the s, % would find the ( of switch (c) first. j=6j is a key longer, and =i{ would also "
        "re-indent the hand-aligned \" color\" line."),

    # ---------- gc gcc ----------
    "comment-1": ("gcc",
        "gcc comments out the current line using Java's 'commentstring', // %s. The marker goes at the "
        "line's indentation. Typing it with I// takes 4 keys."),
    "comment-2": ("gcc",
        "Markdown's 'commentstring' is <!-- %s -->, an HTML comment, so gcc wraps the line in <!-- and -->. "
        "The rendered page won't show it."),
    "comment-3": ("gcj",
        "gcj toggles this line and the next. Both are already comments, so gc uncomments them and removes "
        "the space after the // too. On one line at a time, ^3x and j. would take 5 keys."),
    "comment-4": ("3gcc",
        "A count before gcc toggles that many lines, starting with the current one. gc2j is a tie. Lua's "
        "comment marker is --, and Neovim knows that from the filetype."),
    "comment-5": ("gcip",
        "ip is the paragraph around the cursor: the five lines of deploy(), between the blank lines. gc "
        "puts the # at the indentation of the least-indented line, column 1 here, so the body keeps its "
        "four spaces after the #. {gc} would also comment the blank line above."),
    "comment-6": ("gci{",
        "i{ is the lines inside the braces. From column 1 the cursor isn't inside any braces yet, so it "
        "finds the { further along the line. gc comments the three body lines and leaves the function "
        "itself alone. jgc2j would take 5 keys."),
    "comment-7": ("gccj.",
        "gcc on a comment line uncomments it. j goes down a line and . repeats gcc, which comments that one. "
        "gcj would comment both lines, because they aren't all comments to begin with."),
    "comment-8": ("gcgc",
        "After an operator, gc is a text object: the block of comment lines around the cursor. So gc + gc "
        "toggles exactly the three commented lines, and since they're all comments, it uncomments them. "
        "kgc2j would do the same in 5 keys."),
    "comment-9": ("dgc",
        "d with the gc text object deletes the comment block around the cursor: all five // lines, and "
        "nothing else, from anywhere inside the block. Here 2kd4j would take 5 keys."),
    "comment-10": ("gc}}j.",
        "gc} comments from here to the end of the paragraph, lines 1 and 2, and the cursor stays on line 1. "
        "} jumps to the blank line and j to the second function, where . repeats gc}: those lines are all "
        "comments, so it uncomments them. gcip}j. also works in 7 keys."),
    "comment-11": ("3gcc",
        "3gcc toggles three lines from the cursor down: redis: and its two settings. The # goes at the "
        "indentation of the least-indented line, redis:'s, so the settings keep their extra two spaces after "
        "the # and the nesting is still readable. gc2j is a tie."),
    "comment-12": ("Ggcc",
        "G jumps to the last line, and gcc comments it with SQL's marker, --. gcG from line 1 would comment "
        "the whole query, and 4jgcc is a key longer."),
    "comment-13": ("gcj",
        "gcj comments this line and the next. CSS has no line comments, so its 'commentstring' is /* %s */ "
        "and gc wraps each line in its own /* and */. 2gcc is a key longer."),
    "comment-14": ("gc2at",
        "at is a tag and everything in it. The cursor is inside the <a>, so at alone would be just that one "
        "link, on one line. 2at is the tag one level out, the <nav>, and gc comments every line it touches, "
        "each wrapped in <!-- and --> at the <nav>'s indentation. kgc3j is a tie."),
    "comment-15": ("gcG",
        "G is a motion to the last line, so gcG comments every line from the cursor to the end of the file. "
        "The shell's marker is #. 3gcc is a key longer, and you'd have to count the lines."),
    "comment-16": ("jgcc2j.3j.",
        "j goes to the first console.log and gcc comments it. 2j and 3j reach the other two (the relative "
        "line numbers show the counts), and . repeats gcc on each. A search is longer here: /log<CR> takes 5 "
        "keys, and after gcc adds the // the cursor sits before the match, so n finds the same line again."),
    "comment-17": ("gca{",
        "a{ is the braces and everything between them. It starts at the { on the if line and ends at the }, "
        "and gc works on whole lines, so gca{ comments the if line, the body and the closing brace. gci{ "
        "would leave the if and the } as they are, and kgc3j is a key longer."),
    "comment-18": ("gcj}dG",
        "gcj uncomments the old function, since both its lines are comments. The cursor stays on line 1, so "
        "} jumps to the blank line, and dG deletes from there to the last line: the blank line and the new "
        "greet(). Gdap and then gck also works, a key longer."),
    "comment-19": ("gcgc=2j",
        "gcgc uncomments the comment block around the cursor, all three lines, and leaves the cursor on the "
        "first. The text stays at column 1 (gc only removes the markers), so =2j re-indents the three lines by "
        "Java's rules. gc2j instead of gcgc is the same length, and so is =2j first, then gcgc: = indents "
        "comment lines too, and uncommenting keeps their indentation."),
    "comment-20": ("yyPgccj30<C-a>",
        "yyP puts a copy of the line above it and leaves the cursor on the copy. gcc comments the copy with "
        "TOML's #. j goes back down to the real setting, and 30 Ctrl-a turns 30 into 60. yyp, then "
        "commenting the line above, costs a k more."),

    # ---------- Ctrl-a Ctrl-x ----------
    "increment-1": ("<C-a>",
        "Ctrl-a adds 1 to the first number at or after the cursor, so from column 1 it finds 8080 and "
        "makes it 8081. The cursor ends on the number's last digit."),
    "increment-2": ("<C-x>",
        "Ctrl-x subtracts 1 from the first number at or after the cursor: 10 becomes 9. Typing it would "
        "mean changing two characters into one."),
    "increment-3": ("256<C-a>",
        "A count tells Ctrl-a how much to add: 256 + 256 = 512. Retyping takes longer: f2 then R512 is "
        "6 keys."),
    "increment-4": ("5<C-x>",
        "5 Ctrl-x subtracts 5, and Vim is happy to go below zero: 2 - 5 = -3, and it adds the minus sign "
        "for you. The comment has no digits, so it isn't touched."),
    "increment-5": ("w<C-a>",
        "Digits inside a name count as a number, so Ctrl-a from column 1 would turn uint8_t into uint9_t. w "
        "moves to max_retries, past the type, and Ctrl-a finds the 9. 9 + 1 is 10."),
    "increment-6": ("G2<C-a>",
        "G goes to the last line. Ctrl-a reads 0x02 as hex and keeps it in hex, so adding 2 gives 0x04. G$r4 "
        "is one key longer."),
    "increment-7": ("$<C-x>",
        "$ goes to the 9 at the end. Vim sees the - before 29 as a minus sign, so the number is -29, and "
        "the next day needs -30: that's Ctrl-x, not Ctrl-a. Ctrl-a would give 2026-10-28. "
        ":set nrformats+=unsigned makes Vim ignore minus signs, if you edit a lot of dates."),
    "increment-8": ("2<C-a>l.",
        "2 Ctrl-a turns the first 8 into 10 and leaves the cursor on its last digit. l steps onto the ], so "
        "the first number after the cursor is the second 8, and . adds 2 to it. Without the l, . would add "
        "2 to the 10 again."),
    "increment-9": ("f.<C-a>l2<C-x>",
        "Vim has no decimal numbers, so 1.4.2 is three numbers. f. lands on the first dot, and Ctrl-a "
        "changes the next number, 4, into 5. l steps onto the second dot, and 2 Ctrl-x takes the 2 down to "
        "0. ; instead of l (repeat f. to land on the second dot) is a tie. f4r5f2r0 would take 8 keys."),
    "increment-10": ("<C-x>f=x",
        "Ctrl-x finds the first number on the line, the 1 in i = 1, and makes it 0. The cursor stays there, "
        "so f= jumps to the = of <=, and x deletes it. f1r0 instead of Ctrl-x is 3 keys longer."),
    "increment-11": ("2<C-a>",
        "2 Ctrl-a adds 2 to the first number at or after the cursor, the 3, so the cursor doesn't have to "
        "move first. $r5 is a key longer."),
    "increment-12": ("2W8<C-a>",
        "2W jumps over margin: and 8px onto 16px, and 8 Ctrl-a makes it 24. The px after the digits doesn't "
        "matter. f18<C-a> is a tie: f1 lands on the 1 of 16."),
    "increment-13": ("<C-x>",
        "Vim sees -1, a negative number, in i-1. Ctrl-x subtracts 1 from it, which gives -2, exactly what's "
        "needed. Ctrl-a would go toward zero and give arr[i0]."),
    "increment-14": ("<C-a>j.",
        "Ctrl-a finds the first number on the line, the step's 3, and makes it 4. The 3 in python3 comes later, "
        "so it's safe. j moves down, and . adds 1 to that line's 4."),
    "increment-15": ("<C-x>w.",
        "Ctrl-x turns the first 3 into 2 and leaves the cursor on it. w steps past it (the next word is the >), "
        "so . finds the 3 of </h3>. Without the w, . would subtract from the 2 again. e instead of w is a tie."),
    "increment-16": ("15<C-a>w30<C-a>",
        "15 Ctrl-a adds 15 to the first number on the line, LIMIT's 10, and the cursor stays on its last "
        "digit. w moves to OFFSET, and 30 Ctrl-a turns 20 into 50. A bare . would add 15 again, the last "
        "count. 30. is a tie: a count before . replaces the old one."),
    "increment-17": ("<C-a>l15<C-x>",
        "Ctrl-a finds 09 and adds 1. Neovim doesn't read numbers with a leading 0 as octal, and it keeps the "
        "two digits, so 09 becomes 10. The cursor is on the 0, so l steps onto the colon, and 15 Ctrl-x takes "
        "30 down to 15. Typing the time over with R takes 7 keys."),
    "increment-18": ("<C-a>l9<C-x>l.",
        "Ctrl-a turns the 2 into 3. l steps onto the dot, and 9 Ctrl-x takes the next number, the middle 9, "
        "to 0. l steps onto the second dot, and . repeats 9 Ctrl-x on the last 9. <C-a>lR.0.0 also works, "
        "a key longer."),
    "increment-19": ("1000<C-a>j.j.",
        "1000 Ctrl-a finds the first number on the line, the host port 8080 (the - before it is followed by a "
        "space, so it isn't a minus sign), and makes it 9080. The cursor ends on the last digit, and j keeps "
        "the column, landing inside 8443. Ctrl-a works on the number under the cursor even from its middle, so "
        ". adds 1000 to 8443 and then to 5432. + instead of j is a tie."),
    "increment-20": ("<C-a>G.k.",
        "Ctrl-a makes the first 63 into 64 and leaves the cursor on the 4. G goes to the last line and keeps "
        "the column ('startofline' is off), which on line 3 is just before the 63, so . finds it. The cursor "
        "is now on that 64's last digit, and k goes up to line 2 in the same column, right on its 63, so . "
        "changes that one too. Going down in order costs more: j lands before the 0 on line 2, so you'd need "
        "jf6. and then +., 7 keys."),

    # ---------- g? ----------
    "rot13-1": ("g??",
        "g?? rot13s the whole line, and since rot13 is its own inverse, that decodes it. g?$ is a tie."),
    "rot13-2": ("3Wg?$",
        "3W moves three WORDs forward, from Great to the. g?$ rot13s from there to the end of the line. "
        "The period isn't a letter, so it stays. $g?T: also works in 5 keys: back from the end to just "
        "after the colon."),
    "rot13-3": ("jg??2j.",
        "j goes to the first answer and g?? decodes the whole line, including the N: that becomes A:. 2j "
        "goes down to the second answer and . repeats g??. jj. would be the same length."),
    "rot13-4": ('g?i"',
        'i" is the text inside the quotes, and from column 1 it finds the string further along the line. g? '
        "rot13s it, which decodes it, and the code around it isn't touched. g?? would scramble const and "
        "answer too."),
    "rot13-5": ("g?ip",
        "ip is the paragraph around the cursor, the three encoded lines between the blank lines. g?ip decodes "
        "all of them at once, wherever the cursor is in the paragraph. g?ap is a tie, since blank lines have "
        "no letters."),
    "rot13-6": ("Wg?e2w.",
        "W jumps over Winners: to Ana, and g?e encodes it to the end of the word: Nan. The cursor stays on "
        "its first letter, so 2w skips and and lands on Raj, where . repeats g?e. g?iw is a key longer than "
        "g?e, and g?$ would also encode and."),

    # ---------- gq gw ----------
    "gq-1": ("gqip",
        "ip is the whole paragraph around the cursor, including the line above it. gq joins its lines and "
        "breaks them again at the last space that fits in 50 columns. gq} from here would leave the first "
        "line out. gwip does the same and leaves the cursor where it was."),
    "gq-2": ("gqq",
        "gqq rewraps the current line. In Markdown, \"- \" is in 'comments' as a list item, so gq indents "
        "the new lines by two spaces to line up with the text. gww is a tie, and gqj would also work: each "
        "bullet is wrapped on its own."),
    "gq-3": ("gw2j",
        "gw2j rewraps the three comment text lines and keeps the * leader on every new line, because \"*\" "
        "is a comment leader in Java's 'comments'. gq2j does the same here. In your own config they can "
        "differ: when a language server like jdtls is attached, gq asks it to format, while gw always does "
        "this plain rewrap. gqip would go wrong: with no blank lines around the comment, the paragraph is "
        "the whole class."),
    "gq-4": ("gqgc",
        "After an operator, gc is a text object: the block of comment lines around the cursor, lines 2 to 4 "
        "here. gq rewraps them to 60 columns and keeps the # leader on each new line. gwgc is a tie, and "
        "kgq2j is a key longer. gqip would pull import time and the def line into the rewrap."),
    "gq-5": ("gqG",
        "gq rewraps every line from here to the last one, and keeps the blank line between the paragraphs: "
        "each paragraph is joined and broken on its own. gq} would only do the first paragraph, and "
        "gqip}jgqip is much longer."),
    "gq-6": ("gqq3j.",
        "gqq breaks the first comment into two lines with // on each, and leaves the cursor on the last line "
        "it made. From there the second comment is 3 lines down (the relative line numbers show it, after the "
        "rewrap), and . repeats gqq on it. gqG would join the code lines into the comments' paragraphs."),

    # ---------- ! !! ----------
    "filter-1": ("!!bc<CR>",
        "!! puts :.! on the command line, so the current line becomes the input of the command you type. "
        "bc is the shell's calculator: it reads 2^32 - 1 (^ is a power in bc) and prints 4294967295, which "
        "replaces the line. Retyping the answer would take 11 keys, even if you knew it."),
    "filter-2": ("!i[sort -u<CR>",
        "i[ is the lines inside the square brackets, and from column 1 it finds the [ further along the "
        "line. ! sends them through sort -u, which sorts and drops repeated lines. Plain sort plus deleting "
        "the two extra lines with dd takes at least 13 keys. Project 07's :sort u does the same without the "
        "shell."),
    "filter-3": ("!ipsort|uniq -c|sort -rn<CR>",
        "!ip sends the ten codes into a pipeline. sort puts equal codes next to each other, uniq -c turns "
        "each run into one line with a count in front, and sort -rn sorts by that count, highest first. The "
        "counts are all different, so the order doesn't depend on anything else. Each command does one "
        "small thing, and | connects them."),
    "filter-4": ("!Gsort<CR>",
        "!G puts :.,$! on the command line, from this line to the last, and sort sorts those lines. The "
        "comment on line 1 is outside the range, so it stays on top. !}sort<CR> is a tie, since } at the end "
        "of the file goes to the last line."),
    "filter-5": ("!i{sort<CR>",
        "i{ is the lines inside the braces, and from column 1 it finds the { further along the line. ! sends "
        "them through sort, and since they all have the same indentation, they come back ordered by property "
        "name. !ip would also sort the .btn { and } lines into the list."),
    "filter-6": ("!ipsort<CR>G.",
        "!ipsort<CR> sorts the first group, the paragraph around the cursor. G goes to the last line, inside "
        "the second group, and . repeats the whole filter, sort included, on that paragraph. }j. instead of "
        "G. is a key longer. !Gsort from line 1 would sort the blank line to the top and mix the groups."),

    # ---------- gJ ----------
    "gjoin-1": ("gJ",
        "gJ joins the next line onto this one without adding a space, so the URL comes back whole. J would "
        "put a space after the /. Jx is a tie: J leaves the cursor on the space it added, and x deletes it."),
    "gjoin-2": ("jgJ",
        "j goes to the face, and gJ joins the next line exactly as it is, leading space included: \"( o.o\" "
        "plus \" )\". J would remove that space and add none before the ), giving \"( o.o)\"."),
    "gjoin-3": ("j4gJ",
        "j goes to the line with the opening quote, and 4gJ joins four lines, that one and the next three, "
        "adding nothing. 4J would put a space at each of the three joins."),
    "gjoin-4": ("gJ",
        "gJ joins the next line onto this one exactly as it is, so the five spaces at its start stay and the "
        "bar keeps its width. J would remove them and put one space in their place: [##### ] 50%."),
    "gjoin-5": ("gJj.j.",
        "gJ joins =localhost onto HOST with nothing in between. The lines below move up, so j lands on PORT, "
        "and . repeats gJ, and j. once more does USER. J would give HOST =localhost. + instead of j is a tie."),
    "gjoin-6": ("3gJj.",
        "3gJ joins the first piece with the two lines under it, adding nothing, so the first key comes back "
        "whole. j goes down to the second key's first piece, and . repeats 3gJ with its count. gJgJ for each "
        "key takes 9 keys."),
}
