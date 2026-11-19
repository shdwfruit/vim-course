"""Reference solutions for Project 00's drills (spoilers!). Each entry: drill -> (keys, explanation).

See one with:  python3 check.py drill f --show 3      Watch it typed:  python3 check.py drill f --watch 3
"""
SOLUTIONS = {
    # ---------- i a I A ----------
    "insert-1": ("iNormal ",
        "i starts Insert mode just before the m, so typing \"Normal \" (with its space) slots the word in "
        "front of \"mode\". The <Esc> afterwards is free."),
    "insert-2": ("as",
        "a appends after the character under the cursor, the last e of node_module. i would put the s "
        "before the e."),
    "insert-3": ("A;",
        "A means \"go to the end of the line and append\", in one key. $a; does the same in three."),
    "insert-4": ("Ifinal ",
        "I starts typing at the first non-blank character, the i of int, so the indentation stays in "
        "front. ^ifinal (^ jumps to the first non-blank) is one key more."),
    "insert-5": ("jA]",
        "j moves down to line 2, and A appends at its end, wherever the cursor was on the line."),
    "insert-6": ("f=a=",
        "f= lands on the =, and a= appends a second one right after it. f=i= works just as well, since "
        "the two characters are the same."),
    "insert-7": ("jIreturn ",
        "j goes down to line 2, and I starts typing before the w, after the indentation, wherever the "
        "cursor is on the line. <CR> (the first non-blank of the next line) followed by i ties."),
    "insert-8": ("i\"<Esc>A\"",
        "i\" puts the opening quote before the A, and <Esc> ends that insert. A\" adds the closing one at "
        "the end of the line. C\"Ada\" works too, but retyping the name costs a key more."),
    "insert-9": ("f r(A)",
        "f<Space> lands on the space after print, and r( turns it into a parenthesis without leaving "
        "Normal mode. A) closes the call at the end of the line. elr(A) ties."),
    "insert-10": ("Iprint(<Esc>A)",
        "I starts typing after the indentation, so print( goes in front of x. <Esc> ends that insert, and "
        "A) closes the call. Doing A) first and Iprint( second is the same 10 keys."),
    "insert-11": ("wi-p ",
        "w hops from mkdir to build, and i types \"-p \" in front of it, the space included. ea -p (append "
        "after the end of mkdir) ties."),
    "insert-12": ("I## ",
        "I starts typing at the first non-blank of the line, wherever the cursor is, so you don't have to "
        "go back to the C first. bi## is a key more."),
    "insert-13": ("A:1.27",
        "A appends at the end of the line, wherever the cursor is on it, so it lands right after nginx."),
    "insert-14": ("f\"if",
        "f\" lands on the opening quote, and i types the f in front of it. f(af ties: a appends after "
        "the parenthesis."),
    "insert-15": ("fri**<Esc>ea**",
        "fr lands on the r of required, the first r on the line, and i** puts the stars in front of it. "
        "<Esc> leaves the cursor on the second star, and e jumps to the end of the next word, the d of "
        "required, where a** appends the closing stars. f.i** for the second pair is a key more."),
    "insert-16": ("fda\\n<Esc>A;",
        "fd lands on the d of %d, and a\\n appends the newline escape after it. <Esc>, then A; adds the "
        "semicolon at the end. t,i\\n (insert before the quote just before the comma) ties."),
    "insert-17": ("I/* <Esc>A */",
        "I types after the indentation, so the comment starts where color did. <Esc> ends that insert, and "
        "A */ closes the comment at the end of the line. Retyping the whole line with S costs twice as "
        "much."),
    "insert-18": ("jIsudo <Esc>j.",
        "j goes to line 2 and Isudo <Esc> types in front of apt-get. . repeats the whole insert, I "
        "included, so j. puts sudo at the start of line 3 too. With i, . would type it at the cursor's "
        "column, in the middle of the line."),
    "insert-19": ("10a-<Esc>a+",
        "10a-<Esc> appends a dash and repeats it ten times when you press <Esc>, which leaves the cursor on "
        "the last dash. a+ adds the corner after it. 11a-<Esc>r+ ties: one dash too many, then r turns the "
        "last one into the +."),
    "insert-20": ("fHi<lt>a href=\"/\"><Esc>ea<lt>/a>",
        "fH lands on Home, and i types the opening tag in front of it. <Esc> leaves the cursor on the > just "
        "typed, and e jumps to the end of the next word, the e of Home. a</a> appends the closing tag. "
        "Doing the closing tag first (f<lt>i</a><Esc>FHi...) takes a key more."),

    # ---------- o O ----------
    "o-1": ("o- bread",
        "o opens a new line below milk and starts Insert mode on it, so you just type the item. Copying "
        "the line with yyp and changing the word costs more."),
    "o-2": ("O@Override",
        "O opens a line above the method, and Java's indent rules give it the method's indentation."),
    "o-3": ("oreturn 0;",
        "o opens a line below the {. Because that line ends in {, the new one starts a level deeper, so "
        "you don't type the 4 spaces."),
    "o-4": ("oreturn n * n",
        "o opens the line below the def. Python's indent rules see the colon at the end of the line above "
        "and indent the new line by 4 spaces."),
    "o-5": ("Oassert items",
        "The cursor is already on the return line, so O opens the new line right above it, with the same "
        "indentation."),
    "o-6": ("os must not be NULL.",
        "In C, o on a // comment line starts the new line with \"// \" already typed, so you only type "
        "the words. A<CR> continues the comment too, but costs a key more."),
    "o-7": ("3o|        |<Esc>",
        "3o opens a line, and when you press <Esc> it types the same text on two more new lines. That "
        "<Esc> counts, because it's what adds them. o|        |<Esc>.. is one key more."),
    "o-8": ("ggO#!/bin/sh",
        "gg jumps to the first line, and O opens a new line above it, which becomes the first line of "
        "the file."),
    "o-9": ("Oinit();<Esc>joreturn 0;",
        "O opens a line above run(); and <Esc> ends that insert. The cursor is on the new line, so j "
        "goes back down to run(); and o opens the line below it. Both new lines get run()'s "
        "indentation. Doing the bottom one first (oreturn 0;<Esc>kOinit();) is also 20 keys."),
    "o-10": ("O/  \\<Esc>O /\\",
        "The first O opens a line above the walls for \"/  \\\". The second O, from that new line, opens "
        "one above it for the peak. If you type both lines in one go, <CR> copies the peak's leading space "
        "onto the second line, and deleting it with <BS> makes that the same 10 keys."),
    "o-11": ("o",
        "o opens an empty line below the heading. That's the whole change, so the <Esc> after it is free. "
        "jO, opening it above the paragraph, is a key more."),
    "o-12": ("oset -e",
        "o opens a line below the shebang, and you type the command. The #! line isn't a comment as far "
        "as o is concerned (a shell comment needs a space after the #), so no # is added."),
    "o-13": ("obreak;",
        "o opens a line below halt(); with the same indentation, and you type break;. jObreak; (open it "
        "above the next case) is a key more."),
    "o-14": ("o}",
        "o opens a line at go()'s indentation. As soon as you type }, Java's indent rules shift the line "
        "back one level, to line up with void run()."),
    "o-15": ("o- dev",
        "o opens a line below - main with the same indentation, so you type just \"- dev\"."),
    "o-16": ("oelse:<CR>retry()",
        "o opens a line indented like send(). As you type else:, Python's indent rules move it back out "
        "to the if's level. <CR> after the colon indents the next line one level, where retry() goes."),
    "o-17": ("3o- [ ]<Esc>",
        "3o opens a line and types \"- [ ]\" there; when you press <Esc>, the count adds two more lines "
        "with the same text. That <Esc> counts, because it's what adds them. o- [ ]<Esc>.. is a key more."),
    "o-18": ("o{<CR>count = 0;<CR>}",
        "o opens a line below the signature for the {. Because that line ends in {, <CR> indents the next "
        "one a level, for count = 0;. After the last <CR>, the } you type moves back out to the first "
        "column. o{<CR>}<Esc>Ocount = 0; costs a key more."),
    "o-19": ("o<Esc>j.",
        "o<Esc> adds a blank line below the first statement and leaves the cursor on it. j moves to the "
        "posts statement, and . opens a blank line below it too. o<Esc>jo ties: the second o is already "
        "the change, so its <Esc> would be free."),
    "o-20": ("2oint x;<Esc>hry",
        "2o types int x; on a new line, indented because the line above ends in {, and <Esc> types it "
        "once more on another line. The cursor is on the second ;, so h steps back onto the x and ry "
        "makes it a y. Typing both lines (oint x;<CR>int y;) takes 14."),

    # ---------- x X ----------
    "x-1": ("fdx",
        "fd lands on the first d of \"Tuesdday\". Either d would do, since they're the same letter. x "
        "deletes it."),
    "x-2": ("$X",
        "$ jumps to the last character, the colon. X deletes the character before the cursor, the space, "
        "and the colon slides left. $hx works too, but X saves the h."),
    "x-3": ("f!3x",
        "f! lands on the first exclamation mark, and 3x deletes it and the next two, leaving the last one. "
        "x.. would take a key more."),
    "x-4": ("f=xp",
        "f= lands on the =. x deletes it, which leaves the cursor on the !, and p puts the = back after it. "
        "f!Xp is just as short: X deletes the = from the other side."),
    "x-5": ("f-x;x",
        "f- jumps to the first dash and x deletes it. ; repeats the last f, landing on the second dash, and "
        "x deletes that one too. ;. would work as well, since . repeats the x."),
    "x-6": ("$5X",
        "$ lands on the closing quote. 5X deletes the five characters before it, \"-beta\", and the quote "
        "stays. f-5x is one key longer."),
    "x-7": ("2j$3X",
        "2j goes down to line 3 and $ to its last character, the |. 3X deletes the three spaces before it, "
        "and the | moves back into line."),
    "x-8": ("j2xj.",
        "j moves down to the first column of line 2, where 2x deletes the //. j goes down again, still in "
        "the first column, and . repeats the 2x. (Project 04's Ctrl-v can select both pairs of slashes at "
        "once, which also takes 5 keys.)"),
    "x-9": ("wx$X",
        "w moves from \"if\" to the next word, which is the ( on its own. x deletes it. $ jumps to the colon "
        "at the end, and X deletes the ) just before it. Using x for both would cost a key more: wxf)x."),
    "x-10": ("$xP",
        "$ jumps to the period. x deletes it, and since it was the last character, the cursor moves back "
        "onto the quote. P puts the period before the quote. $Xp works too: X deletes the quote, and p puts "
        "it after the period."),
    "x-11": ("x",
        "The cursor starts on the $, and x deletes the character under the cursor. The $NAME on line 2 "
        "stays: reading a variable does need the $."),
    "x-12": ("f,x",
        "f, jumps to the only comma on line 3, and x deletes it."),
    "x-13": ("fvx",
        "f starts looking just past the cursor, so fv skips the v of version under the cursor and lands on "
        "the v of v1.2.0. x deletes it. ww gets there too (version, :, then v1), also in 2 keys."),
    "x-14": ("ff3x",
        "ff (f, then the letter f) lands on the first f after the #, and 3x deletes it and the next two. "
        "f;3X ties: from the semicolon, X deletes three to the left."),
    "x-15": ("fcxp",
        "fc lands on the c, and x cuts it, leaving the cursor on the n. p puts the c back after the n: "
        "fu-n-c-tion. fnXp ties: X cuts the c from the other side."),
    "x-16": ("f1Xf]X",
        "f1 lands on the 1, and X deletes the space just before it. f] lands on the closing bracket, and X "
        "deletes the space before that too. Using x for both (f[lx and then f]hx) costs more."),
    "x-17": ("lxf.X",
        "Deleting any one of the three d's leaves \"Add\", so l steps onto the first one and x deletes it. "
        "f. finds the period, and X deletes the extra t just before it. fdx for the d is a key more."),
    "x-18": ("f~2x;.",
        "f~ lands on the first ~, and 2x deletes the pair. ; repeats the f~ to the closing pair, and . "
        "repeats the 2x, count and all."),
    "x-19": ("fux;.;.",
        "The first u on the line is the prefix of \"ada\" (names has none), so fu lands on it and x deletes "
        "it. ; jumps to the next u and . deletes it, and ;. once more for the last one."),
    "x-20": ("2f\"x;xj;x,x",
        "2f\" lands on the quote before 8080 and x deletes it. ; repeats the f\" to the quote after 8080, "
        "and x deletes that one. j moves down to the u of true, where ; still repeats f\": it finds the "
        "closing quote, and after x, , goes back the other way to the opening one. f8Xf,X also clears line 2 "
        "in 6 keys, but then ; repeats f, instead of f\", and line 3 costs a key more."),

    # ---------- r ----------
    "r-1": ("3lrx",
        "3l moves three characters right, onto the space between the brackets, and rx replaces it with an "
        "x. (wl gets there too: w hops to the [.) sx would tie here, since the <Esc> after it is free, but "
        "r leaves you in Normal mode, which matters as soon as there's more to do."),
    "r-2": ("f;r,",
        "f; jumps to the semicolon and r, turns it into a comma. You're still in Normal mode afterwards."),
    "r-3": ("f 3r-",
        "f followed by a space jumps to the first space of the gap. 3r- replaces it and the next two with "
        "dashes, and the cursor ends on the last one. Typing over the gap with R--- would take a key more."),
    "r-4": ("f&2r|",
        "f& lands on the first ampersand, and 2r| replaces it and the next character with |. R|| (Replace "
        "mode, the last command in these drills) ties at 5 keys."),
    "r-5": ("f412r*",
        "f4 lands on the first digit, the first 4 on the line. 12r* replaces twelve characters with "
        "asterisks in one go. If the count were more than the characters left on the line, r would do "
        "nothing at all."),
    "r-6": ("f/r-;.",
        "f/ jumps to the first slash and r- replaces it. ; repeats the f/ jump, and . repeats the "
        "replacement. This ; . pair repeats any one-character fix along a line."),
    "r-7": ("jfor*;.",
        "j goes down to the eyes, fo finds the left one, and r* replaces it. ; jumps to the next o, and . "
        "replaces that one too."),
    "r-8": ("wr<CR>w.",
        "w moves from \"milk\" to the comma, since punctuation is a word of its own. r<CR> replaces the "
        "comma with a line break, and like Enter in Insert mode it drops the space that would start the new "
        "line. The cursor is at the start of line 2, so w finds the next comma and . splits again."),
    "r-9": ("jf;r<CR>;.",
        "j goes down to the long line and f; finds the first semicolon. r<CR> replaces it with a line break; "
        "the new line gets the same indentation, without the space that followed the semicolon. ; finds the "
        "next semicolon, on the new line, and . splits there too."),
    "r-10": ("f.3r#f5r8",
        "f. jumps to the first dot and 3r# fills three more cells. The cursor is on the last # it wrote, so "
        "f5 finds the 5 of 50, and r8 makes it 80. Project 03's Ctrl-a, which adds to a number, beats par by "
        "one: f.3r# and then 30 Ctrl-a turns the 50 into 80."),
    "r-11": ("wr7",
        "w hops from chmod to 644, and r7 replaces the 6. You stay in Normal mode, so there's nothing to "
        "finish. f6r7 is a key more."),
    "r-12": ("fOr0",
        "fO finds the capital O (f is always case-sensitive, whatever ignorecase says), and r0 replaces it "
        "with a zero."),
    "r-13": ("t>r-",
        "t> stops just before the >, which is the = of the typo. f= would land on the first =, the "
        "assignment, and you'd need 2f= or a ; to go on. r- replaces it."),
    "r-14": ("j7r=",
        "j goes down to the dashes, and 7r= replaces all seven with = in one go. The count has to match: "
        "if fewer than seven characters were left, r would do nothing."),
    "r-15": ("f=r!",
        "f= lands on the first of the three =, and r! replaces it, which turns === into !==."),
    "r-16": ("jr2jr3",
        "j goes down to the second 1 and r2 replaces it. j keeps the column, so the cursor is on the third "
        "1, and r3 fixes it."),
    "r-17": ("f\"r';.",
        "f\" finds the first double quote and r' replaces it. ; finds the next double quote, and . "
        "repeats the r'."),
    "r-18": ("f 4r<CR>",
        "f<Space> lands on the space after make. 4r<CR> replaces the four characters \" && \" with a single "
        "line break, so make test starts line 2. f&3r<CR> ties: it leaves a trailing space on line 1, "
        "which doesn't count."),
    "r-19": ("f4r5llr0",
        "f4 lands on the 4 and r5 replaces it. ll steps over the dot to the 9, and r0 replaces that. "
        "f4r5f9r0 ties."),
    "r-20": ("r*f+.2j.,.",
        "r* replaces the corner under the cursor. f+ finds the top right one, and . repeats the r*. 2j "
        "goes straight down to the bottom right corner, and . again. , repeats the f+ backward, to the "
        "bottom left corner, and . makes the last one."),

    # ---------- w b e ----------
    "word-1": ("wrn",
        "w hops from String to the start of the next word, Name, and rn replaces the N. fN gets there "
        "too, but costs a key more."),
    "word-2": ("brI",
        "From the middle or the end of a word, b goes back to its start. rI capitalizes it."),
    "word-3": ("eas",
        "e jumps to the end of the word, the a of panda, and as appends the s after it."),
    "word-4": ("wdw",
        "w moves to the first \"the\", and dw deletes it together with the space after it, so the "
        "spacing comes out right. (w4x is the same length, if you count the letters.)"),
    "word-5": ("wcwsum",
        "w moves to total_count, which is a single word because underscores count as letters. cw "
        "changes to the end of the word and keeps the space after it, just like ce."),
    "word-6": ("de",
        "de deletes from the cursor through the end of the word, so _from_config goes and the space "
        "before = stays. dw would delete that space too."),
    "word-7": ("wcwaccount",
        "w goes to currentUser. A word ends where punctuation starts, so cw changes only currentUser "
        "and leaves .email alone."),
    "word-8": ("cbinfo",
        "cb changes back to the start of debug. A backward motion leaves out the character under the "
        "cursor, so the ( survives. bcwinfo is a key more."),
    "word-9": ("c4wmany",
        "c4w changes four words: a, huge, number and of. Like cw, it stops at the end of the last word, "
        "so the space before bugs stays. (16smany ties, but you'd have to count the letters.)"),
    "word-10": ("dwwP",
        "dw cuts \"final \" with its space and leaves the cursor on public. w moves on to void, and P "
        "puts \"final \" in front of it."),
    "word-11": ("4wr-",
        "int, diff, = and a come first, so 4w lands on the +, a one-character word. r- replaces it. f+r- "
        "ties."),
    "word-12": ("2wdw",
        "2w hops over export and default to async, and dw deletes it along with the space after it. "
        "f is no help here: the first a on the line is in default."),
    "word-13": ("wi*",
        "w moves from char to name, and i types the * in front of it."),
    "word-14": ("bcwretries",
        "b goes back to the start of the word the cursor is in: maxRetryCount is one word, capitals and all. "
        "cw changes it and keeps the space after it. Fmcwretries is a key more."),
    "word-15": ("wd4w",
        "w moves from the # to TODO. The label is four words, TODO, (, ada and ):, since a run of "
        "punctuation is a word, and d4w deletes them along with the space after the last one. dtr (up to "
        "the r of retries) ties, and so does 11x, if you count the characters."),
    "word-16": ("c5bpushing",
        "c5b changes back five words, you open a pull request. Like every backward motion, it leaves the "
        "character under the cursor alone, so the period stays. 5bCpushing. is a key more, since C takes "
        "the period too and you have to type it back."),
    "word-17": ("wc3wfetch",
        "w moves from the dot to table. c3w changes table, the dot and rows, and like cw it stops at the end "
        "of the last word, so the () stays. lct(fetch ties, and so does 10s, if you count the characters."),
    "word-18": ("wcww<Esc>4wcwh",
        "w and cw change width to w. From that w, the words are =, 0, the comma, and then height, so 4w "
        "gets there, and cwh renames it. fhcwh for the second one costs a key more."),
    "word-19": ("f:de;.;.",
        "f: lands on the first colon. It's a word on its own, so e goes on to the end of number, and de "
        "deletes \": number\" and leaves the comma. ; repeats the f: and . the de, for b and then for the "
        "return type."),
    "word-20": ("c3wprivate<Esc>wwcwmaxSize",
        "c3w changes public static final into private in one go. After <Esc>, ww hops over int to MAX_SIZE, "
        "and cw renames it: underscores are part of a word. c5w and typing \"private int maxSize\" ties at "
        "22, and cw for public plus d2w for static final costs more."),

    # ---------- f F ----------
    "f-1": ("f+r*",
        "f+ jumps to the plus sign. r* replaces the character under the cursor and leaves you in Normal "
        "mode."),
    "f-2": ("f)x",
        "f) stops on the first closing parenthesis. Either one would do, since both are the same "
        "character. x deletes it."),
    "f-3": ("fvie",
        "fv lands on the v of \"belive\". i inserts before the cursor, so typing e gives \"believe\". "
        "The <Esc> afterwards is free."),
    "f-4": ("j2for-",
        "j goes down to the eyes. fo would stop on the left eye, and 2fo goes on to the second o. r- "
        "replaces it. (fo;r- is also 6 keys: ; repeats the last f.)"),
    "f-5": ("F+a+",
        "F+ searches backward from the end of the line and lands on the +. a appends after it, so "
        "typing + makes i++."),
    "f-6": ("dF/",
        "dF/ deletes from the last / up to the cursor. A backward motion like F never includes the "
        "character the cursor started on, so the closing quote stays. 11X ties, if you count the "
        "characters."),
    "f-7": ("f.df)",
        "f. lands on the dot before get(\"db\"). df) deletes through the first ), which is the end of "
        ".get(\"db\"). f is inclusive: the character it finds is deleted too."),
    "f-8": ("fmcf)abs(x)",
        "f is case-sensitive, so fm skips the capital M of Math and lands on the m of max. cf) deletes "
        "through the ) and leaves you in Insert mode to type abs(x). 16sabs(x) ties, if you count the "
        "characters first."),
    "f-9": ("4f,dF,",
        "4f, lands on the fourth comma, just after birthdate. dF, deletes back to the previous comma: the "
        "comma before birthdate and birthdate itself go, and the comma under the cursor stays. "
        "(3f,dt, ties: from the comma before birthdate, delete up to the next one. So does 4f,10X.)"),
    "f-10": ("2f y2f\"jP",
        "2f<Space> lands on the second space, just before =. y2f\" yanks through the second quote: "
        "' = \"Hi\"'. j keeps your column when it can, or goes to the end of a shorter line, so it lands "
        "on the ; of line 2. P puts the text before it."),
    "f-11": ("f1r2",
        "f1 jumps onto the only 1 on the line, and r2 replaces it."),
    "f-12": ("F:D",
        "F: searches backward from the cursor and lands on the colon before /opt. D deletes from there to "
        "the end of the line, the cursor's own letter included. dF: would leave that last n behind."),
    "f-13": ("feXp",
        "fn would stop on the n of const, but the first e on the line is the one in documnet, so fe lands "
        "right after the n to move. X cuts the n and leaves the cursor on the e, and p puts the n back after "
        "it. 2fnxp is a key more."),
    "f-14": ("fpdf&",
        "fp lands on the p of per_page, the first p on the line. df& deletes from there through the next &, "
        "so q=vim& now runs straight into sort=new. fp12x ties, if you count the characters."),
    "f-15": ("FDcwSaved",
        "FD searches backward and lands on the D of Done. cw changes the word up to the closing quote, and "
        "you type Saved. F\"cT\"Saved, changing back from the closing quote, is a key more."),
    "f-16": ("fpcwwebp",
        "fp lands on the p of png, and cw changes the word up to the closing quote. f.lcwwebp is a key "
        "more."),
    "f-17": ("f,yf)jP",
        "f, lands on the comma after img, and yf) yanks through the first ), the one that closes the tuple: "
        "\", (640, 480)\". j can't keep the column on the shorter line 2, so it lands on its last character, "
        "the ), and P puts the copy before it."),
    "f-18": ("f(df)f(.",
        "f( lands on the first cast's (, and df) deletes through its ), whatever is inside. df) counts as "
        "an f of its own, so ; would now look for a ), not a (: f( again finds the second cast, and . "
        "deletes it the same way. Counting characters (f(6xf(10x) costs a key more, since the casts are "
        "different lengths."),
    "f-19": ("f[r.lxw2x",
        "f[ lands on the bracket and r. turns it into the dot. l steps onto the quote and x deletes it, "
        "which leaves the cursor on name. The \"] after it is a run of punctuation, a word of its own, so w "
        "jumps onto it and 2x deletes it. f\"2x instead of w2x is a key more."),
    "f-20": ("2fai'<Esc>ea'",
        "The first lowercase a is in name, so 2fa lands on the first a of ada, and i' puts the opening quote "
        "before it. <Esc> leaves the cursor on that quote, and e jumps to the end of ada, where a' appends "
        "the closing one. Finding the ) with f) instead of e costs a key more."),

    # ---------- t T ----------
    "t-1": ("t-r>",
        "t- stops just before the first dash, which is the last =. r> replaces it. f- would land on the "
        "dash itself, one too far."),
    "t-2": ("dt)",
        "dt) deletes from the cursor up to, but not including, the next ). The ) stays to close open(. "
        "Counting words doesn't work here, because the \" and the ) form a single word."),
    "t-3": ("ct)args.port",
        "ct) changes from os up to the ) that closes int(, and leaves that ) alone. cf) would change it "
        "too, and you'd have to retype it. (18sargs.port ties, if you count the characters.)"),
    "t-4": ("cT\"Disk full",
        "cT\" changes backward to just after the opening quote. A backward motion never includes the "
        "character the cursor started on, so the closing quote stays too."),
    "t-5": ("ythjP",
        "yth copies from the cursor up to, not including, the h of host: \"config.database.\". j moves "
        "down to the p of port, and P puts the copy in front of it. y4w ties, but you have to count the "
        "dots as words."),
    "t-6": ("dT/",
        "dT/ deletes backward to just after the last slash and leaves the closing quote under the cursor. "
        "dF/ would delete the slash as well. d3b ties: access, . and log are three words."),
    "t-7": ("d2t,j.j.",
        "d2t, deletes from the first comma up to just before the second comma after it, which removes "
        ",name,city. j moves straight down to the next row's first comma, and . repeats d2t, however "
        "long the fields are."),
    "t-8": ("dt:j.j.",
        "dt: deletes from the space up to the colon. The file names have different lengths, but . "
        "repeats \"up to the colon\", not a number of characters, so j. works on every line."),
    "t-9": ("wct,Ada",
        "w moves to Dr, and ct, changes everything up to the comma. c4w ties: Dr, ., Grace and Hopper "
        "are four words."),
    "t-10": ("f@cT:hunter2",
        "There's only one @, so f@ gets you to the end of the password. cT: changes back to just after "
        "the colon, and leaves the @ under the cursor alone."),
    "t-11": ("fsct\"prod",
        "fs lands on the s of staging, the first s on the line, and ct\" changes everything up to the "
        "closing quote, which stays. cw would stop at the first dash. c5w ties (staging, -, eu, - and 1 "
        "are five words), and so does 12s, if you count the characters."),
    "t-12": ("f,dt)",
        "f, lands on the comma after items, and dt) deletes everything up to the closing parenthesis, the "
        "quoted \", \" included. f,10x ties, if you count the characters."),
    "t-13": ("t|r:;.",
        "t| stops on the last dash of the first column, and r: replaces it. The cursor is now right before "
        "a |, so ; skips that one and stops before the next, on the last dash of the second column, and . "
        "repeats the r:."),
    "t-14": ("dT\"",
        "dT\" deletes back to just after the opening quote. A backward motion never includes the character "
        "the cursor started on, so config.h stays whole."),
    "t-15": ("fsct(lookup",
        "fs lands on self, and ct( changes everything up to the (: self.cache.get. c5w ties, since the dots "
        "are words of their own."),
    "t-16": ("wxf]dt ",
        "w hops from See to the [, a word of its own, and x deletes it. f] lands on the closing bracket, and "
        "dt<Space> deletes from there up to the space before for, the whole URL with it. df) ties."),
    "t-17": ("ytujP",
        "ytu yanks from the cursor up to, not including, the u of up: the whole command and the -f option, "
        "with the space after them. j moves down onto logs, and P puts the copy in front of it."),
    "t-18": ("ld2t j.j.",
        "l steps onto the colon. The annotation runs up to just before the second space, so d2t<Space> "
        "deletes \": int\" and keeps the space before =. The colons are all in column 2, so j. repeats it "
        "on each line, and it still works for float and list[int]. de would leave [int] behind, and "
        "counted x can't be repeated, because the types have different lengths."),
    "t-19": ("ct(log.info<Esc>6w.",
        "ct( changes System.out.println up to the (, and you type log.info. From the o at the end of info, "
        "the words are (\", start, \");, work, (); and then System, so 6w lands on it, and . repeats the "
        "change there. 2jFS. gets there too, in two keys more: after 2j the cursor is inside the name, "
        "three columns right of the S. c5w ties with ct(, since the dots are words too."),
    "t-20": ("wwct,null<Esc>jb.jb.",
        "ww hops over the colon to currentUser, and ct,null changes the value up to its comma. After <Esc> "
        "the cursor is at the end of null, so j lands inside the next value and b goes back to its start, "
        "where . repeats the ct,. The same jb. does the last line."),

    # ---------- ; , ----------
    "semicolon-1": ("f-r:;.",
        "f- finds the first dash and r: replaces it. ; repeats the f- to find the next dash, and . "
        "repeats the r:."),
    "semicolon-2": ("F+r-;.",
        "F+ searches backward from the end and lands on the last +, and r- changes it. After an F, ; "
        "searches backward too, so it finds the + before it, and . repeats the r-."),
    "semicolon-3": ("f-r_,.",
        "f- finds the dash after 2024, and r_ replaces it. , repeats the last f- in the opposite "
        "direction, so it lands on the dash before 2024, and . repeats the r_. F-r_,. works too: then "
        "the , goes forward."),
    "semicolon-4": ("t,r0;.;.",
        "t, lands on the 3, just before the first comma, and r0 replaces it. The cursor is still right "
        "in front of that comma, so ; skips it and stops before the next one, on the 7. . repeats the "
        "r0, and ;. once more does the 5."),
    "semicolon-5": ("f.ld;",
        "f. finds the period at the end of the first sentence, and l steps onto the space after it. d; "
        "deletes up to and including the next period, because ; repeats f., and f includes what it "
        "finds. tIdf. ties."),
    "semicolon-6": ("t,x;.;.",
        "t, stops on the space before the first comma, and x deletes it. Now the cursor is on that "
        "comma, so ; finds the next one and stops on the space before it, and . repeats the x."),
    "semicolon-7": ("t,a: int<Esc>;.t).",
        "t, lands on w and a: int<Esc> types after it. The cursor ends up right before the comma, and ; "
        "skips that comma and stops on h, where . types \": int\" again. The last parameter is followed "
        "by ) instead of a comma, so t). handles it."),
    "semicolon-8": ("f+s + <Esc>;.;.",
        "f+ lands on the first +, and s + <Esc> replaces it with \" + \". ; finds the next +, and . "
        "repeats the s. The ; . rhythm does the rest."),
    "semicolon-9": ("I| <Esc>f,s | <Esc>;.A |",
        "I| <Esc> adds the bar at the start. f, finds the first comma and s | <Esc> turns it into "
        "\" | \". ;. does the same to the second comma, and A | adds the bar at the end."),
    "semicolon-10": ("F/r.;.,.",
        "F/ finds the slash before models and r. replaces it. ; repeats F/ backward, to the slash after "
        "src. , repeats it the other way, forward, to the slash after models, and . replaces each one."),
    "semicolon-11": ("f`x;.;.;.",
        "f` finds the first backtick and x deletes it. ; repeats the f` to the next backtick, and . repeats "
        "the x. Three more ;. pairs do the rest."),
    "semicolon-12": ("3f-r:;.",
        "3f- skips the two dashes in the date and lands on the one after 10, and r: replaces it. ; repeats "
        "the f- to the last dash, and . repeats the r:."),
    "semicolon-13": ("t.a\\<Esc>;.",
        "t. stops on the last w, just before the first dot, and a\\ appends the backslash after it. After "
        "<Esc> the cursor is on that backslash, right next to the dot. ; is smart enough to skip a match "
        "right next to the cursor, so it stops before the second dot, and . adds another backslash. With f. "
        "and i\\, ; would land on the dot you just escaped."),
    "semicolon-14": ("f'r\";.;.;.",
        "f' finds the first single quote and r\" replaces it. ; finds each of the other three in turn, and "
        ". repeats the r\"."),
    "semicolon-15": ("f,;D",
        "f, lands on the first comma and ; on the second. D deletes from there to the end of the line, the "
        "comma included. 2f,D ties, and so does 11wD, if you count the dashes, the @ and the dot as words."),
    "semicolon-16": ("f,ld;",
        "f, lands on the comma after \"ada\", and l steps onto the space. d; deletes through the next comma, "
        "because ; repeats the f, and f includes what it finds: ' \"bob\",' goes, and \"cy\" moves up. "
        "f,ldf, would be a key more."),
    "semicolon-17": ("ftcwmd<Esc>;.;.",
        "ft lands on the t of the first txt, and cw changes the word to md. ; finds the next t, the start of "
        "b.txt's extension, and . repeats the cw, and ;. once more for c.txt. 3s instead of cw ties."),
    "semicolon-18": ("f,r.j,.",
        "f, finds the comma on line 1 and r. replaces it. Line 2 is shorter, so j lands on its last "
        "character, past the comma. ; searches to the right and would find nothing, but , repeats the f, "
        "backward, and . repeats the r.."),
    "semicolon-19": ("3f\"i\\<Esc>,.",
        "3f\" lands on the quote after hi, and i\\ puts a backslash in front of it. , repeats the f\" "
        "backward, to the quote before hi, and . escapes that one too. Going left to right takes a key "
        "more: after the first i\\, ; would land on the quote you just escaped, so you'd need 2; to skip it."),
    "semicolon-20": ("f\\a\\<Esc>;.;.;.",
        "f\\ lands on the first backslash, and a\\ adds another after it. <Esc> leaves the cursor on the new "
        "one, so f\\ has nothing left at this spot: ; finds the next original backslash, and . doubles it. "
        "With i\\, the cursor would stay in front of the old one, and ; would find it again."),

    # ---------- counts ----------
    "count-1": ("3x",
        "x deletes the character under the cursor, and 3x deletes three, starting there. x.. does the "
        "same in three keys."),
    "count-2": ("5jA;",
        "With relativenumber on, the line you want is labeled 5, so 5j goes straight there. A; adds "
        "the semicolon. 6GA; (6G goes to line 6) ties."),
    "count-3": ("f[10a#<Esc>",
        "f[ lands on the [. 10a#<Esc> appends #, and when you press <Esc> it repeats that until there are "
        "ten. The <Esc> counts, because it's what types the other nine."),
    "count-4": ("d3w",
        "d3w deletes three words, each with the space after it, so tmp moves right up to -rf. 3dw does "
        "exactly the same."),
    "count-5": ("4dd",
        "4dd deletes the cursor's line and the three below it. d3j (this line and three down) ties."),
    "count-6": ("4J",
        "4J joins four lines into one. J puts a single space between the joined lines, so the sentence "
        "reads naturally. JJJ does it in three keys."),
    "count-7": ("yjj2p",
        "yj copies the cursor's line and the one below. j moves to line 2, and 2p puts the two lines "
        "below it twice."),
    "count-8": ("2fixp",
        "2fi skips the i in received and lands on the i of reciept. xp swaps it with the e after it. "
        "fi;xp ties: ; repeats the fi."),
    "count-9": ("3>>",
        "3>> indents three lines, starting at the cursor's. >2j (this line and two below) ties."),
    "count-10": ("f03a, 0<Esc>",
        "f0 lands on the 0. 3a, 0<Esc> appends \", 0\", and <Esc> repeats it to make three. f}3i, 0<Esc> "
        "ties."),
    "count-11": ("d3k",
        "The if line is three lines up, so d3k deletes the fi line and the three above it. 3k4dd gets there "
        "too, in a key more."),
    "count-12": ("3A)<Esc>",
        "3A) appends a ), and when you press <Esc> it appends two more. That <Esc> counts, because it's "
        "what types them. A))) is the same length."),
    "count-13": ("5<lt><lt>",
        "5<< shifts five lines left one level, starting with the cursor's line. The count is lines, not "
        "levels. <4j ties."),
    "count-14": ("f46i0<Esc>",
        "f4 lands on the 4, and 6i0<Esc> types six zeros in front of it. The <Esc> counts, since it's "
        "what types the other five."),
    "count-15": ("j3a|---<Esc>a|",
        "j goes to the empty line. 3a|---<Esc> types |--- three times, and a| adds the closing bar after "
        "the last dash. Typing the whole row costs 14."),
    "count-16": ("w7a#<Esc>3a.<Esc>",
        "[] is a word of its own, so w lands on the [ (f[ is a key more). 7a#<Esc> appends seven #, leaving the cursor on the last one, so 3a.<Esc> "
        "appends the three dots right after them. Both <Esc>s count."),
    "count-17": ("j2dd2j3.",
        "j and 2dd delete ada's two lines, and the cursor lands on bob's entry. 2j goes down to cy's, and "
        "3. repeats the dd with a new count, three lines. jdj and 2jd2j tie."),
    "count-18": ("jA;<Esc>3j.",
        "jA; fixes line 2. Line 5 is then three lines down (the relative numbers say 3), so 3j goes there "
        "and . repeats the A;."),
    "count-19": ("Y2Pyy2p",
        "Y copies \"[ ]\" from the cursor to the end of the line, and 2P puts it twice in front of the "
        "cursor, making the row. (2p would put the copies after the [, inside the box.) yy copies the row, "
        "and 2p puts it twice below."),
    "count-20": ("8a-<Esc>a+<Esc>yypO|<Esc>8a <Esc>a|",
        "8a-<Esc> draws the eight dashes after the +, and a+ adds the corner. yyp copies that line below it "
        "as the bottom border. O opens a line above the bottom border, where | and then 8a <Esc> and a| "
        "draw the middle."),

    # ---------- d D ----------
    "d-1": ("fcdw",
        "fc lands on the first \"completely\". dw deletes up to the start of the next word, so the word and "
        "its space go together. Deleting either copy gives the same text, and 3wdw is the same length."),
    "d-2": ("f/D",
        "f/ lands on the first slash, and D (short for d$) deletes everything from there to the end of the "
        "line. The space left before it doesn't matter, since spaces at the end of a line are ignored. C "
        "would tie, because its <Esc> is free, but it leaves you in Insert mode."),
    "d-3": ("f,de",
        "f, lands on the comma. The comma is a one-character word, so e moves on to the end of the next "
        "word, and de deletes \", timeout_seconds\" and keeps the ). dw would only delete \", \", because it "
        "stops at the start of the next word. dt) works too but is a key longer."),
    "d-4": ("f.dt.",
        "f. lands on the dot after user. t. stops just before the next dot, so dt. deletes "
        "\".getProfile()\" and leaves that dot for .getName(). That's the difference between f and t: f "
        "lands on the character, t stops one short of it."),
    "d-5": ("f,df,",
        "f, jumps to the first comma. df, deletes from there through the next comma, both commas included, "
        "and the space before \"is\" becomes the space after \"meeting\"."),
    "d-6": ("d2b",
        "2b would move back two words, to the s of static. d2b deletes from there up to the cursor, but not "
        "the character under it: a backward motion never includes where you started, so int survives. 2db "
        "is the same."),
    "d-7": ("d0",
        "0 is the first column, and d0 deletes from there up to, but not including, the cursor, so \"make "
        "test\" stays whole. From the start of the line, d3W would do the same in 3 keys."),
    "d-8": ("fcd4w",
        "fc lands on config. Punctuation counts as a word of its own, so \"config\", \".\", \"settings\" and "
        "\".\" are four words, and d4w deletes them all. 4dw is the same, and fcd2f. ties too."),
    "d-9": ("$dT0",
        "$ jumps to the colon. T0 would move back to just after the 0, and like every backward motion, dT0 "
        "leaves the cursor's own character alone, so the colon stays and \" and not done\" goes."),
    "d-10": ("wdw$d2b",
        "w moves to static, and dw deletes it with its space. $ jumps to the {, and d2b deletes back two "
        "words: \"throws Exception \", including the space before the brace. The brace stays, because a "
        "backward delete never includes the cursor's character."),
    "d-11": ("3wdw",
        "const, data and = come first, so 3w lands on await, and dw deletes the word and the space after it. "
        "fa would stop in data, which has two a's of its own."),
    "d-12": ("dF,",
        "dF, deletes back to the comma, and like every backward motion it leaves the character under the "
        "cursor alone, so the ) stays. F,dt) gets the same result in two keys more."),
    "d-13": ("2wd2w",
        "2w hops over We and should to probably. d2w deletes two words, each with its space. fpd2w ties."),
    "d-14": ("ttdt>",
        "The first t on the line is the start of target, so tt (t, then the letter t) stops on the space "
        "just before it. dt> deletes from there up to the >. 2f<Space> gets to the same space in a key "
        "more."),
    "d-15": ("f#Dj.",
        "f# lands on the first comment and D deletes it, which leaves the cursor on the space just before "
        "where the # was. The comments start in the same column, so j lands just before the second one, "
        "and . deletes to the end of that line too."),
    "d-16": ("fpdtp",
        "fp lands on the first p, and dtp deletes up to the next p, which f and t look for starting just "
        "past the cursor: \"p != NULL && \" goes. fpd4w ties: p, !=, NULL and && are four words."),
    "d-17": ("f/2D",
        "f/ lands on the comment, and 2D deletes to the end of this line and the whole next line too. The "
        "space left before the comment doesn't count, since trailing spaces are ignored. f/Djdd takes 6."),
    "d-18": ("2F/D",
        "2F/ goes back to the second slash before the cursor, the one before 2026.01.05-1200, and D deletes "
        "from there to the end of the line. 10bD ties, if you count all ten words back: the dots, the dash "
        "and the slashes are words too."),
    "d-19": ("2wdt\"j.",
        "2w hops over API_KEY and =\" (a run of punctuation is one word) to abc123, and dt\" deletes up to "
        "the closing quote. API_KEY and DB_PASS have the same length, so j lands on the h of hunter2!, and . "
        "deletes up to its closing quote, even though the value is longer. A counted x couldn't do that."),
    "d-20": ("wd2wffdw;.3wd2w",
        "w and d2w delete static synchronized. ff lands on the first final and dw deletes it with its "
        "space, and ; with . does the second. That leaves the cursor on int: int, n and ) are three words, "
        "so 3w reaches throws, and d2w deletes it and IOException with its space."),

    # ---------- dd ----------
    "dd-1": ("jdd",
        "j moves to line 2 and dd deletes it. It doesn't matter where on the line the cursor is."),
    "dd-2": ("j3dd",
        "j moves to the first comment and 3dd deletes it and the two lines below. jd2j is the same length: "
        "d with j deletes whole lines too."),
    "dd-3": ("dj",
        "dj deletes the cursor's line and the one below it. Because j moves between lines, d deletes whole "
        "lines, not from the cursor's column. 2dd does the same in 3 keys."),
    "dd-4": ("dk",
        "k moves between lines like j, so dk deletes the cursor's line and the line above it. k2dd would "
        "take 4 keys."),
    "dd-5": ("ddp",
        "dd cuts the first line, so the header moves up to line 1, with the cursor on it. p puts the cut "
        "line below the cursor's line. ddp swaps a line with the one below it."),
    "dd-6": ("dd2kP",
        "dd cuts the line and leaves the cursor on serve(), the line that took its place. 2k goes up to "
        "connect(), and P puts the line above it. Moving the other two lines down instead (2k2ddp) takes 6."),
    "dd-7": ("jddj.j.",
        "j and dd delete the first DEBUG line, and the cursor lands on the INFO line after it. j steps onto "
        "the next DEBUG line and . deletes it, and the same again for the last one. Project 07's "
        ":g/DEBUG/d deletes every matching line in one command."),
    "dd-8": ("3ddGp",
        "3dd cuts the three lines of main, and the cursor lands on helper's first line. G jumps to the last "
        "line, and p puts the cut lines below it. d2j would cut the same three lines with the same number "
        "of keys."),
    "dd-9": ("ddP",
        "dd on the last line leaves the cursor on the new last line, print(greeting), and P puts the cut "
        "line above it. In the middle of a file, dd leaves the cursor on the line below instead, so there "
        "moving a line up takes ddkP."),
    "dd-10": ("2jddddp",
        "2j goes to the (old) line and dd deletes it, which leaves the cursor on \"Ship release\". ddp then "
        "swaps that line with the one below it."),
    "dd-11": ("dd",
        "dd deletes the line the cursor is on, and the rest of the file moves up."),
    "dd-12": ("jdj",
        "j moves to line 2, and dj deletes it and the line below. j2dd is a key more."),
    "dd-13": ("djp",
        "dj cuts Write docs and its sub-item, and the cursor lands on Fix the build. p puts the two lines "
        "below it. Moving Fix the build up instead (2jddkP) takes twice as many."),
    "dd-14": ("jd2j",
        "j moves to the opening quotes, and d2j deletes that line and the two below it, whole, wherever the "
        "cursor is. j3dd ties."),
    "dd-15": ("d3jP",
        "d3j cuts the four struct lines. Nothing is left below them, so the cursor ends on line 1, the "
        "prototype, and P puts the struct above it. Moving the prototype down instead (dd3jp) is a key "
        "more."),
    "dd-16": ("kddj.",
        "k goes up to the first print and dd deletes it. The cursor lands on db.write, which took its place, "
        "so j reaches the second print and . deletes it too."),
    "dd-17": ("dj2jp",
        "dj cuts the two Usage lines, and the cursor lands on ## Install. 2j goes down to the section's last "
        "line, and p puts Usage below it."),
    "dd-18": ("dd<lt><lt>jdj",
        "dd deletes try: and leaves the cursor on run(), and << unindents it. j goes down to except, and dj "
        "deletes it and pass."),
    "dd-19": ("ddp2jddkP",
        "dd cuts 3,cy, and p puts it below 1,ada. The cursor is on the 3, so 2j reaches 2,bo on the last "
        "line. dd cuts it, which leaves the cursor on the line above, 4,di. k goes up to 3,cy, and P puts "
        "2,bo above it."),
    "dd-20": ("dd2jpkdd2kP",
        "dd cuts Deploy, 2j goes down to Commit, and p puts Deploy below it, at the end. k goes back up to "
        "Commit and dd cuts it. That leaves the cursor on Deploy, now line 3, so 2k goes up to Build and P "
        "puts Commit above it."),

    # ---------- c C cc s S ----------
    "c-1": ("wcwtotal",
        "w jumps to count, and cw deletes it and starts Insert mode. On a word, cw only goes to the end of "
        "the word, like ce, so the space before = survives. The <Esc> at the end is free."),
    "c-2": ("fDCINFO",
        "fD lands on DEBUG, and C deletes to the end of the line and starts Insert mode, so you type INFO. "
        "cw would work too, but it's one key longer."),
    "c-3": ("jSbreak;",
        "j moves to line 2, and S clears it and starts Insert mode while keeping its 4-space indentation, "
        "so you just type break;. cc does exactly the same in one more key, and so does jwcwbreak."),
    "c-4": ("fg3sfetch",
        "fg lands on the g of get. 3s deletes three characters and starts Insert mode, so you type fetch. "
        "ct_ works too but costs a key more, and cw would take the whole name, since underscores are part of "
        "words. A sneaky tie: get and fetch share \"et\", so rf and then appending ch after the t (fgrfftach) "
        "is also 9 keys."),
    "c-5": ("2wct)ready",
        "2w skips \"if\" and \"(\" and lands on count. ct) deletes up to the closing parenthesis and leaves "
        "you in Insert mode to type ready. c6w ties, if you count the six words (! is one), and C would delete "
        "the ) and { too, so you'd have to type them back."),
    "c-6": ("wcwcount<Esc>j0.jw.",
        "wcwcount<Esc> renames the first one. j0 goes to the start of line 2, and . repeats the whole change "
        "there. From the end of that count, j lands on the r of return, w on cnt, and . renames it too. "
        "Project 01's + (start of the next line) would save a key, and Project 07's :%s/cnt/count/g does "
        "it in one command, but in 17 keys."),
    "c-7": ("j3Spass",
        "j moves into the body. 3S replaces the three lines with a single empty line, still indented, and "
        "you type pass. 3cc does the same with one more key."),
    "c-8": ("wcwlong<Esc>fCcwTotal",
        "w and cw replace int with long, and <Esc> ends that change. fC jumps to the C of Count, and cw "
        "changes Count to Total. Doing it all in one change also takes 17 keys: wc2w and then typing "
        "\"long getTotal\"."),
    "c-9": ("2jScontinue;<Esc>3j.",
        "2j goes to the first printf, and S replaces it with continue; at the same indentation. 3j goes down "
        "to the second printf, and . repeats the change, typed text included."),
    "c-10": ("jwcWreturn<Esc>$x",
        "j and w get to print. A WORD is anything between spaces, and like cw, cW stops at the end of it, so "
        "cWreturn turns print(\"total:\", into return and keeps the space. $x deletes the leftover ). "
        "Retyping the line with S takes 14."),
    "c-11": ("3wC8080;",
        "const, port and = come first, so 3w lands on process. C deletes from there to the end of the line "
        "and starts Insert mode, so you type 8080 and the ; that C took with it. 3wct;8080 is a key more."),
    "c-12": ("f^s**",
        "f^ lands on the ^, and s deletes it and starts Insert mode, where you type two stars in its place. "
        "f^r*a* ties."),
    "c-13": ("wcw5",
        "w moves to 30, and cw changes the number to the end of the word, so the space before make stays. "
        "w2s5 ties."),
    "c-14": ("cf puts(",
        "cf<Space> changes everything from the cursor through the first space, printf(\"%s\\n\", and its "
        "space, so name and the rest stay. You type puts( in front of name. 15s ties, if you count the "
        "characters."),
    "c-15": ("cwsum<Esc>ft.",
        "cw changes the first total to sum. ft finds the next t, the start of the second total, and . "
        "repeats the change, typed text and all. 2w. ties."),
    "c-16": ("fNceId<Esc>;.",
        "fN lands on the N of userName. ce changes to the end of the word, so only Name goes, and you type "
        "Id. ; repeats the fN to the second userName, and . repeats the ce."),
    "c-17": ("f&cwand<Esc>;.",
        "f& lands on the first &. && is a run of punctuation, one word, so cw changes both characters and "
        "you type and. ; finds the next &, and . changes that && too. 2s instead of cw ties."),
    "c-18": ("j4Sreturn ok",
        "j moves to the if line. 4S replaces it and the three lines below with one empty line, keeping the "
        "if's indentation, so you only type return ok. 4cc does the same in a key more."),
    "c-19": ("lcwverbose<Esc>ffcw1",
        "l steps inside the first quote, and cw changes debug up to the closing quote. After <Esc>, ff finds "
        "the f of false (verbose has none), and cw changes it to 1. 5s1 ties with cw1."),
    "c-20": ("wcwidx<Esc>jfi.4w.",
        "w moves to i and cw changes it to idx. The cursor ends on the x, so j lands on the i of print, and "
        "fi finds the next i, the one after the (, where . changes it. From the end of that idx, the comma, "
        "items and [ are three words, so 4w reaches the last i, and . again. f[l. is a key more."),

    # ---------- y yy Y ----------
    "y-1": ("yyjp",
        "yy copies the top line. j moves to line 2, and p puts the copied line below it. Whole lines always "
        "go on a new line of their own, never inside a line."),
    "y-2": ("yejf)P",
        "ye copies the name without the space after it. j goes down, f) finds the closing parenthesis, and "
        "P puts the name before it. With yw you'd copy the space too, and it would end up inside the "
        "parentheses."),
    "y-3": ("f,Yjp",
        "f, lands on the comma, and Y copies from there to the end of the line. (In Neovim Y is y$; in Vim "
        "it copies the whole line.) Line 2 is shorter, so j lands on its last character, and p puts the "
        "copy after it. j$p would be the safe version."),
    "y-4": ("fNy2ejf!P",
        "fN lands on New, and y2e copies to the end of the second word, \"New York\", without the closing "
        "quote. j goes down, f! finds the exclamation mark, and P puts the copy in front of it. yt\" and y2w "
        "copy the same text with the same number of keys."),
    "y-5": ("fxyWjP",
        "fx lands on the x. yW copies the WORD \"x=10,\" together with the space after it, which is exactly "
        "what goes in front of y=40. j moves straight down onto the y on line 2, and P puts the copy before "
        "it."),
    "y-6": ("yypf2r3$r9",
        "yy copies the line, and p puts the copy below with the cursor at its start. f2 finds the 2 and r3 "
        "replaces it; $ jumps to the 4 at the end, and r9 replaces that."),
    "y-7": ("wyf)j$P",
        "w moves to len, and yf) copies \"len(items)\": f includes the character it lands on, so the ) comes "
        "too. j goes down, $ to the closing parenthesis, and P puts the copy before it."),
    "y-8": ("yyPA;<CR>",
        "yy copies the first line, and P puts the copy above it, leaving the cursor on the copy. A; adds the "
        "semicolon at the end, and <CR> opens the blank line below it. The final <Esc> is free."),
    "y-9": ("GyypwRBo ",
        "G jumps to Ana's row, and yyp duplicates it, leaving the cursor at the start of the copy. w moves "
        "to Ana, and R overwrites it with \"Bo \" (Bo and a space), so the | after it doesn't move. cw and "
        "then \"Bo \" also works, but costs one key more."),
    "y-10": ("f(lyt)jF(p",
        "f( and l put the cursor on the h of https, and yt) copies up to the closing parenthesis. j goes down "
        "to line 2 and lands a little past the empty (), so F( goes back to the opening parenthesis, and p "
        "puts the URL after it. Project 02's yi( copies what's inside the parentheses from anywhere in them."),
    "y-11": ("yyp",
        "yy copies the whole line, its indentation included, and p puts the copy on a new line below it."),
    "y-12": ("yypwCjson",
        "yyp duplicates the line and leaves the cursor at the start of the copy. w moves to os, and C changes "
        "it to the end of the line. Typing the line with o costs 12."),
    "y-13": ("ywjP",
        "yw copies \"unsigned \" with its space. j moves straight down to the i of int on line 2, and P puts "
        "the copy in front of it."),
    "y-14": ("wytujP",
        "w hops from ssh to -i, and ytu copies up to the u of ubuntu: \"-i ~/.ssh/key.pem \", with its space. "
        "ssh and scp are the same length, so j lands on the a of app, and P puts the option in front of it."),
    "y-15": ("wy3wjP",
        "w moves to id, and y3w copies three words, id, the comma and name, with the space after name. j "
        "keeps the column and lands on the F of FROM, and P puts the copy in front of it. wytFjP ties."),
    "y-16": ("f YjpF0r1",
        "f<Space> lands on the space after width, and Y copies from there to the end of the line. j can't keep "
        "the column on the short line 2, so it lands on the t of height, and p puts the copy after it. F0 "
        "goes back to the 0 and r1 fixes the index."),
    "y-17": ("jyy2jP2j.",
        "j and yy copy the @Override line. 2j goes down to void b(), and P puts the copy above it, with the "
        "cursor on the new line. 2j goes down to void c(), and . repeats the P."),
    "y-18": ("yjjp3wCworker",
        "yj copies both lines of the web entry. j goes to the second line, and p puts the copy below it, with "
        "the cursor at the start of the new entry. The dash, name and the colon are three words, so 3w "
        "reaches web, and C changes it to the end of the line. Typing the two lines with o costs nearly twice "
        "as much."),
    "y-19": ("y2wjwPjFF.",
        "y2w copies logging and the dot. j lands on the = of line 2, w hops to Formatter, and P puts the copy "
        "in front of it, leaving the cursor on the dot, past Filter's F on line 3. So j and FF go back to "
        "that F, and . repeats the P."),
    "y-20": ("fiyt)kP",
        "fi finds the next i, the int inside the parentheses (clamp has no i), and yt) copies up to the ). "
        "Both lines start with int clamp(, so k lands on the ) of the empty (), and P puts the parameters in "
        "front of it. 3w instead of fi ties."),

    # ---------- p P ----------
    "p-1": ("ddGp",
        "dd cuts the first line. G jumps to the last line, and p puts the cut line below it: whole lines "
        "always go on a new line of their own."),
    "p-2": ("wdwwP",
        "w moves to like, and dw cuts it along with its space. The cursor is now on really, so w hops to "
        "pizza, and P puts \"like \" before it. The space travels with the word, so the spacing comes out "
        "right."),
    "p-3": ("jyy2p",
        "j moves to the row and yy copies it. 2p puts two copies below it. The indentation comes along, "
        "since the whole line is copied."),
    "p-4": ("f,xF\"p",
        "f, lands on the comma, and x cuts it. F\" searches backward for the closing quote of the format "
        "string, and p puts the comma right after it."),
    "p-5": ("fSywf<lt>p",
        "fS lands on String, and yw copies it (the word ends at the >). f< jumps to the next <, the empty "
        "pair, and p puts String after it. Typing String yourself would take 10 keys."),
    "p-6": ("jlY$2p",
        "j and l put the cursor on the first dash, and Y copies \"------|\" to the end of the line. $ goes "
        "to the last |, and 2p puts two copies after it."),
    "p-7": ("jyy4jP",
        "j and yy copy the @staticmethod line, indentation included. 4j goes down to def render, and P puts "
        "the copy above it. p would put it below the def, where it doesn't belong."),
    "p-8": ("ddjp",
        "dd cuts make install, and the cursor lands on ./configure. j goes down to make, and p puts the cut "
        "line below it."),
    "p-9": ("f#DO<Esc>p",
        "f# and D cut the comment. Text cut from inside a line goes back inside a line, so O<Esc> first makes "
        "an empty line above, and p puts the comment on it. The spaces left at the end of line 2 don't "
        "matter."),
    "p-10": ("2ddpddp",
        "2dd cuts sys and os, leaving json alone on line 1, and p puts them back below it: json, sys, os. The "
        "cursor is on sys, so ddp swaps it with os. Project 07's :sort does it in 5 keys (:sor<CR>)."),
    "p-11": ("f;xp",
        "f; lands on the semicolon and x cuts it, leaving the cursor on the ). p puts the ; after it: the "
        "same xp that swaps two letters."),
    "p-12": ("dwA <Esc>p",
        "dw cuts \"Lovelace \" with its space, which leaves Ada. A <Esc> adds a space at the end of the line, "
        "and p puts Lovelace after it. The space that came with the cut ends up at the end of the line, where "
        "it doesn't count."),
    "p-13": ("f yt>jP",
        "f<Space> lands on the space after div, and yt> copies up to the >: ' class=\"card\"'. j lands on "
        "the > of the shorter line 2, and P puts the copy in front of it."),
    "p-14": ("t xf1p",
        "t<Space> stops just before the first space on the line, on the second ), and x cuts it. f1 finds "
        "the 1 at the end, and p puts the ) after it. 2f) gets to the same ) in a key more."),
    "p-15": ("3f Djep",
        "3f<Space> lands on the first of the two spaces before the #, and D cuts \"  # seconds\". The cursor "
        "goes back to the ), column 10, so j lands on the space before 30, e on the 0 at its end, and p puts "
        "the comment after it."),
    "p-16": ("2jyy2jp2j.",
        "2j and yy copy the --- line. 2j goes down to text two, and p puts the copy below it, with the cursor "
        "on the new line. 2j reaches text three, and . repeats the put."),
    "p-17": ("dd2kp",
        "dd cuts import sys, and since it was the last line, the cursor lands on the line above, pass. 2k "
        "goes up to import os, and p puts the line below it."),
    "p-18": ("3ddjp",
        "3dd cuts Old and its two sub-items, and the cursor lands on New. j goes down to Newer, and p puts the "
        "three lines below it."),
    "p-19": ("d2wfuP",
        "d2w cuts sort and the |, each with the space after it. fu finds the u of uniq (grep error has none), "
        "and P puts \"sort | \" in front of it."),
    "p-20": ("f:yt,fbpfc.",
        "f: lands on the colon after a, and yt, copies \": float\" up to the comma. fb finds b, and p puts the "
        "copy after it. fc finds c (float has none), and . repeats the put."),

    # ---------- . ----------
    "dot-1": ("A \\<Esc>j.j.",
        "A \\<Esc> appends a space and a backslash at the end of line 1. . repeats the A as well as the "
        "text, so j. adds them to the end of the next line, however long it is."),
    "dot-2": ("rX2j.2j.",
        "rX marks the top dot. 2j goes two lines straight down, staying in the same column, and . "
        "repeats the rX."),
    "dot-3": ("dwj.",
        "dw deletes static and its space. j moves down a line and . deletes the next static. (7xj. ties, "
        "if you count the letters.)"),
    "dot-4": ("jddj.",
        "j goes to the first printf and dd deletes it. The lines below move up, so the second printf is "
        "one line down, and . deletes it too."),
    "dot-5": (">>.",
        ">> indents the line by 4 spaces, and . does it again. >>>> works too, but it's a key more."),
    "dot-6": ("3ea,<Esc>e.",
        "3e jumps to the end of the third word, eggs, and a,<Esc> appends the comma. From the comma, e "
        "jumps to the end of milk, and . appends another one. 3t a,<Esc>;. is a key more."),
    "dot-7": ("O@staticmethod<Esc>4j.",
        "O@staticmethod<Esc> opens a line above def add and types the decorator. The second def is now "
        "four lines down, and . repeats the whole O with its text. Copying the line with yy and putting "
        "it with P costs two keys more."),
    "dot-8": ("dd2j3.",
        "dd deletes import pdb. 2j goes down to pdb.set_trace(). dd's count was one, and 3. replaces it "
        "with three, so it deletes that line and the two below."),
    "dot-9": ("fcct;0<Esc>j.j.",
        "fc lands on the c of computeA, and ct;0<Esc> changes everything up to the semicolon into 0. That "
        "leaves the cursor on the 0, in the column where compute starts on every line, so j. repeats the "
        "change on the next line. C0;<Esc> would leave the cursor on the ;, one column too far right for "
        "j. to work."),
    "dot-10": ("jIprivate <Esc>j.j.",
        "jIprivate <Esc> types the word after the indentation of the first field, and j. repeats it on "
        "each of the others. (A visual block, from Project 04, ties at 15 keys.)"),
    "dot-11": ("A<BS><Esc>j.j.",
        "A goes to the end of the line and <BS> deletes the semicolon before the cursor. That's one change, "
        "and . repeats the A as well as the <BS>, so j. works on lines of any length."),
    "dot-12": ("I# <Esc>j.",
        "I# <Esc> types \"# \" after the indentation. j goes down, and . repeats the I, so the # goes in after "
        "that line's deeper indentation, not at the cursor's column."),
    "dot-13": ("cwaddr<Esc>2jb.",
        "cw changes host to addr. The cursor ends on the r, the fourth column, so 2j lands on the t of the "
        "other host, and b goes back to its start. . repeats the change, typed text and all."),
    "dot-14": ("jxj.j.",
        "j moves down to the first body line, still in the first column, and x deletes one space. The cursor "
        "stays in column 1, so j. deletes one space from each of the other lines. 3<< would remove four, not "
        "one."),
    "dot-15": ("cwlong<Esc>fi.;.",
        "cw changes the first int to long. fi finds the next i, the int inside the parentheses, and . "
        "changes it too. ; repeats the fi to the last int, and . again."),
    "dot-16": ("fpdwjl.",
        "fp lands on the p of px (margin has no p), and dw deletes px up to the semicolon, which leaves the "
        "cursor on the ;. j lands on the 0 of line 2, l on its px, and . deletes it. 2x instead of dw ties."),
    "dot-17": ("3wifinal <Esc>fS.",
        "3w hops over void, save and ( to int, and ifinal <Esc> types in front of it. fS finds String, and . "
        "types \"final \" in front of it too."),
    "dot-18": ("I\"<Esc>j.j.A\",<Esc>k.k.",
        ". repeats only your last change, so the quotes before the names come first: I\"<Esc> on ada, then j. "
        "twice. Then A\",<Esc> ends the last line, and k. twice ends the other two. Mixing them line by line "
        "would mean typing every change."),
    "dot-19": ("I#<Esc>2j2.",
        "I#<Esc> adds a # in front of ## Setup. 2j goes down to # Usage, and 2. repeats the I with a count of "
        "2, which types ## instead of #."),
    "dot-20": ("wcwresponse<Esc>jFr.f,w.",
        "w and cw rename the first res. The cursor ends on the e of response, so j lands on the t of throw, "
        "and Fr goes back to the r of res, where . renames it. f, finds the comma after \"failed\", w hops to "
        "res, and . again."),

    # ---------- > < >> << ----------
    "indent-1": ("j>>",
        "j moves to the print line, and >> shifts it right by one shiftwidth, 4 spaces here. Like dd, >> is "
        "an operator doubled to act on the whole line."),
    "indent-2": ("2j<lt><lt>",
        "2j goes down to line 3, and << shifts it left by 4 spaces. It doesn't matter where on the line the "
        "cursor is."),
    "indent-3": ("j3>>",
        "j moves to the first statement, and 3>> shifts it and the two lines below one level right. The count "
        "is lines, not levels. j>2j is the same length."),
    "indent-4": (">k",
        ">k shifts the cursor's line and the one above it, the same lines dk would delete. k2>> would take 4 "
        "keys."),
    "indent-5": ("j>}",
        "j moves to setup(), and } would move to the next blank line, so >} shifts setup(), run() and "
        "cleanup(). Blank lines are never indented. j3>> works too, with one more key."),
    "indent-6": ("G>>.",
        "G jumps to the last line, and >> indents it one level. . repeats the shift for the second level. "
        ">>>> also works, but . is a key shorter."),
    "indent-7": ("j4>>2j>>",
        "j and 4>> indent the four lines between the class's braces. The cursor stays on line 2, so 2j goes to "
        "count++; and >> gives it its second level. Project 03's = re-indents code by the language's rules: "
        "=G from the top fixes the whole class in 2 keys."),
    "indent-8": ("dd<lt>G",
        "dd deletes the if line and leaves the cursor on x = load(). G moves to the last line, so <G shifts "
        "all three lines left. 3<< or <2j would cost one more key."),
    "indent-9": ("j>j3j.",
        "j moves to Apple, and >j indents Apple and Banana. The cursor stays on Apple, so 3j reaches Carrot, "
        "and . repeats >j on Carrot and Leek."),
    "indent-10": ("joif debug:<Esc>j>>",
        "j moves to print(\"start\"), and o opens a line below it, already indented 4 spaces, where you type "
        "if debug:. Then <Esc>, j, and >> shift the print one level further in."),
    "indent-11": ("4j<lt><lt>",
        "4j goes down to the return, and << shifts it left one level, out of the loop. It doesn't matter "
        "where on the line the cursor is."),
    "indent-12": (">2k",
        "2k would move up two lines, so >2k shifts the cursor's line and the two above it. 2k3>> gets there "
        "too, in two keys more."),
    "indent-13": ("2j>>",
        "2j goes down to the if, and >> shifts it one level right."),
    "indent-14": ("j3<lt><lt>",
        "j goes to the first line of the body, and 3<< shifts it and the next two lines left by four spaces. "
        "<2j ties with 3<<."),
    "indent-15": ("j<lt><lt>..",
        "j goes down to the return, and << takes off one level. . repeats the shift, twice, leaving one "
        "level."),
    "indent-16": ("dd<lt>j2jdd",
        "dd deletes the { and leaves the cursor on int a. <j shifts that line and the next one left. The "
        "cursor stays on int a, so 2j reaches the } and dd deletes it."),
    "indent-17": ("j4>>2j>j",
        "j and 4>> shift port, tls, cert and key right by two spaces, the shiftwidth for YAML here. The "
        "cursor stays on port, so 2j reaches cert, and >j shifts cert and key once more."),
    "indent-18": ("2j>>2j.",
        "2j goes down to the first return, and >> shifts it. 2j reaches the second, and . repeats the >>."),
    "indent-19": ("j3>>4i <Esc>",
        "j and 3>> shift the three lines, but smartindent makes > skip a line whose first character is #, "
        "so the comment doesn't move. The cursor is still at its start, and 4i <Esc> types the four spaces. "
        "(Project 03's = re-indents by the language's rules instead.)"),
    "indent-20": ("j6>>2j3>>j>>",
        "j and 6>> shift everything between the outer <ul> lines one level. The cursor stays on Home, so 2j "
        "reaches the inner <ul>, and 3>> shifts it, Team and the inner </ul> once more. j goes down to Team "
        "for its third level."),

    # ---------- J ----------
    "join-1": ("J",
        "J joins line 2 onto line 1 and puts one space between them."),
    "join-2": ("3J",
        "3J joins three lines into one. J throws away the leading spaces of each line it pulls up and puts a "
        "single space in their place, which is the spacing you want after a comma."),
    "join-3": ("jJ",
        "j moves to the start( line, and J pulls the next line up. Normally J puts a space between the "
        "lines, but not when the next line starts with ), so you get start(config);."),
    "join-4": ("Jx",
        "J joins the lines and puts a space between them, with the cursor on that space. x deletes it. "
        "Project 03's gJ joins without adding the space, also in 2 keys."),
    "join-5": ("Ji,",
        "J joins the lines and leaves the cursor on the space it put in. i, inserts the comma before that "
        "space. A,<Esc>J also works, with one more key."),
    "join-6": ("kJ",
        "k goes up to the first comment line, and J joins the next one onto it. In code, J also removes the "
        "comment marker (# or //) from the line it joins, so you get a single comment."),
    "join-7": ("Jj.j.",
        "J joins Engineer onto Ana's line and drops its indentation. The joined line is line 1, so j moves to "
        "Bo Chen and . joins again, and the same once more for Cy Park."),
    "join-8": ("JF\"5x",
        "J pulls the second line up and leaves the cursor on the space before \"shipped.\". F\" jumps back to "
        "the quote that ended the first string, and 5x deletes it along with the space, the backslash, the "
        "space and the opening quote of the second string."),
    "join-9": ("J3j.",
        "J joins the { onto the first function's line. That line is now line 1, so 3j reaches the second "
        "function's first line, and . joins its brace too."),
    "join-10": ("Jx3JX",
        "J joins host onto the first line, and x deletes the space J added after the (. 3J joins the next "
        "two lines: a space before port, none before the ), and the cursor ends on the ). X deletes the comma "
        "just before it."),
    "join-11": ("J",
        "J joins the lines, and in Markdown it treats a list dash like a comment marker: it removes the - of "
        "the line it joins, just as it removes # or // in code."),
    "join-12": ("4J",
        "4J joins the four lines into one, removes the indentation of each line it pulls up, and puts one "
        "space at each join."),
    "join-13": ("J2X",
        "J joins the lines but keeps the backslash, and leaves the cursor on the space it added after it. 2X "
        "deletes the backslash and the space before it. JXx ties."),
    "join-14": ("2jJ",
        "2j goes down to the closing brace, and J pulls the else line up after it with one space between."),
    "join-15": ("Ji +",
        "J joins tax onto the first line, with the cursor on the space between price and tax. i + types a "
        "space and the + before that space, which gives price + tax. Ja+ <Esc> ties."),
    "join-16": ("Jr,Jr,",
        "J joins 36 onto ada, with the cursor on the space between them, and r, turns it into a comma. J and "
        "r, again for london. . would only repeat the r, so each join is typed out."),
    "join-17": ("3JI[<Esc>A]",
        "3J joins the three lines, putting one space after each comma. I[<Esc> adds the opening bracket at the "
        "start of the line, and A] the closing one at the end."),
    "join-18": ("Ji:<Esc>jJi:",
        "J joins ada onto name and leaves the cursor on the space between them, and i: types the colon "
        "before it. j moves to age, and the same J and i: do the second pair. The last <Esc> is free."),
    "join-19": ("JF r<CR>",
        "J joins the lines and leaves the cursor on the space between the and lazy. F<Space> goes back to the "
        "space before the, and r<CR> turns it into a line break."),
    "join-20": ("3J2F r<CR>",
        "3J makes one line and leaves the cursor on the space where usability. was joined. Going back, the "
        "first space is before and and the second before extensibility, so 2F<Space> lands there and r<CR> "
        "breaks the line."),

    # ---------- R ----------
    "replace-mode-1": ("GWRcarol",
        "G jumps to the last row, and W jumps over the date (one WORD, since it has no spaces) to bob. R "
        "overwrites: c, a and r replace bob, and o and l replace two of the spaces, so logout doesn't move. "
        "cw would push logout to the right."),
    "replace-mode-2": ("jfiRrunning",
        "j and fi land on idle. R overwrites one character per key, so running covers idle and three of the "
        "spaces, and the | stays put. cw would push the border out, and you'd have to delete three spaces."),
    "replace-mode-3": ("f6R5-12-31<Esc>jF6.",
        "f6 lands on the 6 of 2026, and R types 5-12-31 over the rest of the date. <Esc> ends the change, j "
        "goes down to line 2, and F6 goes back to its 6, where . repeats the overwrite. cW would also work, "
        "with one key more."),
    "replace-mode-4": ("jwROPEN  ",
        "j goes down to the sign's line, and w hops from the | to CLOSED. R overwrites one character per key: "
        "OPEN covers CLOS, and the two spaces cover ED, so the | stays where it was. cw would shrink the "
        "frame."),
    "replace-mode-5": ("wR12.0",
        "w hops from nginx to the 2 of 2.5. R types 12.0 over 2.5 and the first space after it, so 120M stays in "
        "its column. Inserting a 1 instead would push it right."),
    "replace-mode-6": ("wROK  <Esc>jb.",
        "w hops from the 1 to the first TODO, and R types OK and two spaces over it. <Esc> leaves the cursor on the "
        "last space typed, the fourth column of the word, so j lands on the last O of the next TODO, and b "
        "goes back to its T. . repeats the whole overwrite. cw would need the same two spaces typed, plus a "
        "key."),
}
