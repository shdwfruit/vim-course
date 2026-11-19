"""Reference solutions for Project 02's drills (spoilers!). Each entry: drill -> (keys, explanation).

See one with:  python3 check.py drill iw --show 3      Watch it typed:  python3 check.py drill iw --watch 3
"""
SOLUTIONS = {
    # ---------- iw aw ----------
    "iw-1": ("ciwsize",
        "ciw deletes the whole word count, from any position in it, and starts Insert mode, so you type "
        "size. bcwsize ties at 7 keys, but only after you've noticed you aren't at the start of the "
        "word: ciw doesn't care."),
    "iw-2": ("daw",
        "daw deletes \"a word\". A period follows file, not a space, so aw takes the space before it "
        "instead, and README ends up right next to the period. bdw would leave \"README .\", and bXdw takes "
        "4 keys. $5X ties, if you count the characters: it deletes the 5 before the period."),
    "iw-3": ("ciw ",
        "With the cursor on white space, iw is the whole run of white space around it, so ciw deletes all "
        "twelve spaces, and you type one. dw from the middle would only delete the spaces after the "
        "cursor. w11X ties, but only if you count the spaces exactly."),
    "iw-4": ("diw",
        "iw on white space is the whole run, so diw removes all four spaces at once, wherever in them the "
        "cursor is. dw would only delete from the cursor on, leaving the spaces before it behind. w4X ties, "
        "but you have to count the spaces first."),
    "iw-5": ("yawjP",
        "yaw yanks \"static \" with the space after it, and moves the cursor to the start of the word. j "
        "lands on the v of void, right below, and P puts the text in front of it. bywjP ties: yw takes the "
        "space too, but only from the start of the word."),
    "iw-6": ("dawwP",
        "daw deletes \"final \" with its space and leaves the cursor on static. w moves on to int, and P "
        "puts \"final \" back in front of it. bdwwP ties."),
    "iw-7": ("d3aw",
        "d3aw deletes three words: for some reason. A closing quote follows reason, so instead of the "
        "white space after it, aw takes the space before for, and file ends up next to the quote. F dt\" "
        "does the same in 5 keys."),
    "iw-8": ("gUiwj.",
        "gUiw uppercases the word under the cursor and leaves the cursor at its start. j lands in the "
        "middle of idle_timeout, and . repeats gUiw there. With bgUw, the repeat would need another b "
        "first: bgUwjb. is 7 keys."),
    "iw-9": ("ciwinfo<Esc>j.",
        "ciwinfo<Esc> changes debug to info. j lands in the middle of trace, and . repeats the ciw with the "
        "same text, which works from anywhere in the word. With cw you'd need a b before each change: "
        "bcwinfo<Esc>jb. is 11 keys. A Visual block (Project 04) over both words ties at 10, since they "
        "start in the same column."),
    "iw-10": ("daw$h.",
        "daw deletes afterwards with the space before it, because a period follows. $h puts the cursor on "
        "the y of immediately, and . deletes that word the same way. Deleting with counted X instead "
        "needs a different count for each word: f.11X$12X is 9 keys."),
    "iw-11": ("ciw2rem",
        "Digits and letters together make one word, so iw is all of 120px, and ciw replaces it from the 2 in "
        "the middle. bcw2rem ties at 7, and so does Xlcwrem: X deletes the 1, l steps past the 2, and cw "
        "changes 0px. cw from the 2 alone would leave the 1 behind."),
    "iw-12": ("daw",
        "daw deletes the second when and the space after it, from anywhere in the word, so one space is left "
        "between the words around it. bdw ties: b goes back to the start of the word, and dw deletes the word "
        "and its space. diw would leave two spaces behind."),
    "iw-13": ("yiwjf}P",
        "yiw yanks retries from the middle of it and moves to its start. j goes down to line 2, f} finds the "
        "closing brace, and P puts the word in front of it. yiwjf{p ties, and so does starting with bye. "
        "Typing it, jf}iretries, takes 11 keys."),
    "iw-14": ("daw2wP",
        "daw deletes not with the space after it, leaving the cursor on user. 2w moves past user and is to "
        "None, and P puts \"not \" in front of it, space included. bdw2wP ties, and so do dawWWP and dawfNP."),
    "iw-15": ("d2aw",
        "A run of punctuation like --> is a word of its own, so 2aw is test and its space plus --> and its "
        "space. d2aw deletes all of that from the middle of test. daw. ties, and so do bd2W and bdtd."),
    "iw-16": ("yiwjPF.p",
        "yiw yanks width and moves to its start. Line 2 is shorter, so j lands on its last character, the ;, "
        "and P puts width in front of it. That leaves the cursor on the h, so F. jumps back to the dot, and p "
        "puts width again after it. byejPF.p ties. Typing both copies takes 17 keys."),
    "iw-17": ("ciwDate<Esc>j.j.",
        "ciwDate<Esc> changes the number on line 3 from its middle. The cursor ends on the e of Date, so j "
        "lands on the b of the number below, in the middle of the word, and . repeats the ciw there. j. does "
        "the last one. With cw you'd need a b before each repeat: bcwDate<Esc>jb.jb. is 14 keys. A search "
        "with * finds id's number too, which costs an extra n: 13 keys."),
    "iw-18": ("diwl.",
        "On white space, iw is the whole run of it, so diw deletes the first gap wherever the cursor is in it, "
        "and leaves the cursor on the =. l steps into the second gap, and . deletes that one too. c3iw= ties: "
        "with a count, the white space counts as a word, so 3iw is gap, = and gap, and you type the = back."),
    "iw-19": ("d2awj.",
        "2aw is if and needed, and since a period follows needed, aw takes the space before if instead of a "
        "space after needed. So d2aw leaves the period right after service, with the cursor on it. j lands on "
        "the if of line 2, in the same column, and . repeats d2aw there. daw. also cleans line 1, but line 2 "
        "then needs j.. as well: 7 keys."),
    "iw-20": ("yawjP+w.",
        "yaw yanks \"synchronized \" with its space and moves to the start of the word. j lands on the V of "
        "line 2, and P puts the copy in front of it. + goes to the start of line 3, w to void, and . repeats "
        "the put. bywjP+w. ties: yw takes the space too, once you're at the start of the word."),

    # ---------- i" a" i' a' ----------
    "quote-1": ("ci\"Hi there",
        "ci\" deletes Hello, world, from any position inside the string, and leaves you typing between the "
        "quotes. T\"ct\" does the same in two more keys."),
    "quote-2": ("ci'Permission denied",
        "ci' works like ci\", for single quotes: it changes the whole string from anywhere inside it. ciw "
        "would only change not, and T'ct' is two keys longer."),
    "quote-3": ("ci\"Bad width",
        "The cursor isn't in a string, so ci\" uses the next one on the line. fWct\"Bad width also works, "
        "two keys longer. The quote objects only search the current line, never the lines below."),
    "quote-4": ("da\"",
        "da\" deletes the quotes, the text between them and the space after the closing quote, so backup/ "
        "moves up with one space in front. With motions you'd go back to the quote first: F\"dtb is 5 "
        "keys. daW can't do it, because the file name has a space in it."),
    "quote-5": ("ya\"jP",
        "ya\" finds the string by looking ahead, yanks it with its quotes and moves to the opening quote. "
        "The ) of get() is right below, so j lands on it, and P puts the string in front of it. f\"yf\"jP "
        "takes two keys more."),
    "quote-6": ("gUi\"j.",
        "gUi\" uppercases the inside of the first string on the line, found by looking ahead. j moves to "
        "line 2, and . repeats the whole command: wherever the cursor lands, i\" finds that line's string. "
        "f\"gU$ also uppercases a string, but repeating it needs another f\": 9 keys in all."),
    "quote-7": ("ci\"Hello",
        "The \\\" quotes are escaped, so they don't end the string: i\" is everything between the first and "
        "the last quote. T\" and t\" stop at the escaped quotes, so they can't do this in one go."),
    "quote-8": ("yi\"jvi\"p",
        "yi\" yanks the URL. j lands inside the second string, vi\" selects its contents, and p replaces "
        "the selection with what you yanked. di\"P wouldn't work: deleting puts the old URL in the "
        "register, so P would put that one back."),
    "quote-9": ("di\"j.j.",
        "di\" deletes the inside of the first string on the line. j goes down, and . repeats di\", which "
        "finds that line's string whether the cursor lands before it or inside it."),
    "quote-10": ("wci\"Margaret Hamilton",
        "Vim pairs the quotes from the start of the line, so on the comma the gap , between the strings "
        "looks like a string too, and ci\" would change it. w moves onto the opening quote of \"Ada "
        "Lovelace\", and from there ci\" changes the right string. fAct\"Margaret Hamilton is one key longer."),
    "quote-11": ("ci`make check",
        "ci` changes everything between the backticks, and there are none before the cursor, so it finds them "
        "by looking ahead. 2wc2emake check is two keys longer: 2w gets to npm, and c2e changes two words."),
    "quote-12": ("ci'Germany",
        "There's no single quote before the cursor, so ci' looks ahead and changes the first string on the "
        "line. fNcwGermany is one key longer: Netherlands holds the line's first capital N."),
    "quote-13": ("ca\"USERS_URL",
        "ca\" finds the first string by looking ahead and changes it, quotes included. A comma follows the "
        "closing quote and a parenthesis comes before the opening one, so there's no white space for a\" to "
        "take. f\"cWUSERS_URL, is two keys longer: cW eats the comma, so you type it back."),
    "quote-14": ("ci'1d",
        "ci' looks ahead to the quoted script and replaces everything inside it, slashes and all. "
        "f'lct'1d takes 8 keys."),
    "quote-15": ("c2i'NULL",
        "With a count of 2, i' is the string with its quotes but without any white space, so c2i' replaces "
        "'none' and you type NULL. ca'NULL followed by a space ties: a' takes the space after the closing "
        "quote too, so you type it back. So does f'cWNULL, since the string is a WORD of its own."),
    "quote-16": ("ya'j$i,<Esc>p",
        "ya' finds the string on line 1 by looking ahead. Nothing follows it, so a' takes the space in front "
        "of it instead: \" 'eu-west-1'\". j$ goes to the ) at the end of line 2, i,<Esc> types the comma in "
        "front of it, and p puts the string, space first, after the comma. Typing the argument out takes 16 "
        "keys."),
    "quote-17": ("$hci\"destination",
        "$ goes to the ) and h onto the closing quote of the help text. On a quote, Vim counts the quotes "
        "before it, five here, so it knows this one closes a string, and ci\" changes that string. From help=, "
        "ci\" would change the gap between \"--output\" and the help text. $hcT\"destination ties, and 5f\" "
        "to the opening quote is one key longer."),
    "quote-18": ("yi\"jhP$h.",
        "yi\" looks ahead to for=\"username\", yanks the value and moves to its u. j lands on the space after "
        "id=\"\", h steps onto its closing quote, and P puts username in front of it. $ goes to the >, h onto "
        "the closing quote of name, and . puts it again. yi\"jhP$hP ties: the repeat costs the same as P."),
    "quote-19": ("jdi\"khP",
        "j goes to line 2, and di\" deletes Welcome back, found by looking ahead, into the register. That "
        "leaves the cursor on the closing quote. Line 1 is shorter, so k lands on the ; at its end, h steps "
        "onto the closing quote, and P puts the text in front of it. Typing it into title and then emptying "
        "subtitle takes 20 keys."),
    "quote-20": ("di\"W.W.",
        "di\" looks ahead and empties \"Ada\", leaving the cursor on its closing quote. W jumps to the next "
        "WORD, which starts with the opening quote of the email, and . empties it: on an opening quote, i\" "
        "is the string it opens. W. does the last one. f\" instead of the first W works too, with ; for the "
        "second jump: 8 keys."),

    # ---------- i( a( ----------
    "paren-1": ("ci(x1, y1, x2, y2",
        "ci( deletes everything between the parentheses, wherever in them the cursor is, and leaves you in "
        "Insert mode. T(ct) is two keys longer."),
    "paren-2": ("di(",
        "The cursor isn't inside parentheses, so di( uses the next pair it finds and empties it. With "
        "motions, $dT( is one key longer: $ lands on the ), and dT( deletes back to just after the (."),
    "paren-3": ("ca(subtotal",
        "ca( changes the parentheses around the cursor along with everything inside them. F(c%subtotal is "
        "one key longer."),
    "paren-4": ("yi(jP",
        "The cursor is inside rect_area( ) but not inside height( ), whose ( comes later, so yi( yanks "
        "rect_area's arguments, nested parentheses and all, and moves to the start of them. Right below "
        "that is the ) of price_for(), so j lands on it, and P puts the text before it. yi(j$P is one key "
        "longer."),
    "paren-5": ("di(",
        "There are no parentheses on line 1, so di( looks ahead and finds the next ( on line 2. jdi( works "
        "too, one key longer. Careful in real code: it will just as happily find a ( ten lines down."),
    "paren-6": ("ci(summary",
        "The cursor is inside info( ) but not inside format( ), so i( is everything between info's "
        "parentheses. It skips over the nested pairs to find the matching ). ct) would stop at the first "
        "), the one after size(. Without i(, the shortest way is T(Csummary);, two keys longer."),
    "paren-7": (">i(",
        "( is the last character of line 1 and ) the first of line 5, so i( covers lines 2 to 4 as whole "
        "lines, and > shifts them right by one shiftwidth. k>2j does the same in 4 keys. >ip would shift "
        "lines 1 and 5 too."),
    "paren-8": ("di(j.j.",
        "di( empties the first call. After each j, the cursor is either inside the next call's parentheses "
        "or before them, and . works from both, so j.j. finishes the job."),
    "paren-9": ("yi(jvi(p",
        "yi( yanks the four values, looking ahead from the start of the line. j lands inside draw_rect( ), "
        "vi( selects what's there, and p replaces the selection with the yanked text. di(P would put back "
        "the text you just deleted, since deleting fills the register too."),
    "paren-10": ("yi(jhPr5",
        "yi( yanks margin + 10, margin + 20. Line 2 is shorter, so j stops on its ;, and h steps onto the "
        "). P puts the text in front of it and leaves the cursor on its last character, the 0 of 20, so "
        "r5 makes it 25. Typing it all yourself would take 27 keys."),
    "paren-11": ("da(",
        "da( finds the first ( on the line by looking ahead and deletes the pair and everything in it, so "
        "(size_t) goes and strlen moves up next to the space. f(d% is one key longer: % jumps to the matching "
        ")."),
    "paren-12": ("ci(TCP",
        "ci( finds the first ( on the line and changes what's inside it, HTTP. fHcwTCP is one key longer, and "
        "fHRTCP<Esc>x two."),
    "paren-13": ("ci(id -un",
        "ci( looks ahead to the $( ) and changes the command inside it. fwcwid -un is one key longer: whoami "
        "holds the line's first w."),
    "paren-14": ("ci(*",
        "ci( looks ahead to COUNT's parentheses and replaces DISTINCT user_id with *. fDc2w* takes 6 keys, "
        "and f(lct)* 7."),
    "paren-15": ("<lt>i(.",
        "( ends line 2 and ) starts line 6, so i( is the three argument lines. <i( shifts them left by one "
        "shiftwidth, from any of them, and . shifts them once more. k<2j. is one key longer, and <ip would "
        "shift the def and parser lines too."),
    "paren-16": ("ya(jP",
        "ya( looks ahead to the subquery, yanks it with its parentheses and moves to the (. Line 2 is shorter "
        "than that, so j lands on its last character, the ;, and P puts the copy in front of it. f(y%jP is "
        "one key longer, and typing it takes 23 keys."),
    "paren-17": ("ci(null<Esc>j.j.",
        "ci( looks ahead to setName( and finds its matching ), past the nested name(). After <Esc> the cursor "
        "is on the last l of null, and j lands on line 2 between setEmail's parentheses, but not inside "
        "email()'s, so . changes the right pair. The same goes for line 3. ct) would stop at the first ), "
        "the one after name(."),
    "paren-18": ("yi(jpjP",
        "yi( yanks rows, schema and moves to the r. Right below it is the ( of transform(), so j lands on it "
        "and p puts the arguments after it. That leaves the cursor on the last a of schema, and j goes down "
        "to save(), which is shorter, so it lands on the ). P puts the arguments in front of it. . would "
        "repeat p, not P, and put them after the )."),
    "paren-19": ("ca(gross<Esc>ca(rate",
        "ca( looks ahead to the first pair and replaces it, parentheses included, with gross. After <Esc> the "
        "cursor is on the s of gross, outside every pair, so the next ca( looks ahead too and finds "
        "(1 - discount). Moving there with f( first costs two more keys."),
    "paren-20": ("ci('closed'",
        "There's no ( on line 1, so ci( looks ahead and finds the one at the end of line 2. That pair spans "
        "whole lines, so ci( replaces the three status lines with one empty, indented line, and you type "
        "'closed'. 2jc2j'closed' is two keys longer."),

    # ---------- i{ a{ ----------
    "brace-1": ("ci{0",
        "ci{ deletes 90, 85, 77 from anywhere between the braces and leaves you typing inside them. T{ct}0 "
        "is two keys longer."),
    "brace-2": ("di{",
        "di{ deletes the three lines between the braces, from anywhere in the body, and leaves both braces "
        "on their lines. kd2j does the same in 4 keys."),
    "brace-3": ("ci{memset(c, 0, sizeof *c);",
        "ci{ deletes the three lines of the body and opens one empty line, indented to match, so you can "
        "type the new body straight away. kc2j does the same in one more key."),
    "brace-4": ("ca{new int[4]",
        "ca{ changes the braces and everything in them, from anywhere inside. F{c%new int[4] and "
        "F{Cnew int[4]; are one key longer."),
    "brace-5": (">i{",
        ">i{ shifts the lines between the braces right by one shiftwidth, 4 spaces here. k>2j does the "
        "same in 4 keys, and =i{ (Project 03) would also fix it, in 3."),
    "brace-6": ("yi{GP",
        "yi{ yanks the body of save() as whole lines. G jumps to the last line, the } of saveAs(), and P "
        "puts the lines above it. ky2jGP is one key longer."),
    "brace-7": ("ci{0, 0, 0<Esc>j.j.",
        "ci{ finds the braces on line 1 by looking ahead and changes what's inside them. After each j the "
        "cursor lands between the next line's braces, so . repeats the change there. A substitute from "
        "Project 07 beats it: :%s/\\d\\+/0/g<CR> turns every number in the file into 0 in 13 keys, which "
        "works here because the colors are the only numbers."),
    "brace-8": ("ya{j$P",
        "ya{ looks ahead for the first {, yanks the whole dict with its braces, and moves the cursor to the "
        "{. j$ goes to the end of line 2, and P puts the dict in front of the closing parenthesis. Since "
        "the dict ends the line, f{Yj$P ties: Y yanks to the end of the line."),
    "brace-9": ("=i{",
        "= is the re-indent operator from Project 03, and i{ gives it the lines between the braces. C's "
        "indent rules know that a line after an if without braces goes one level deeper. =ip ties here, "
        "since the whole function is one paragraph. > and < can't do it: each line is off by a different "
        "amount."),
    "brace-10": ("di{3kP",
        "di{ deletes the three lines of init()'s body into the register and leaves the cursor on the } "
        "below them. 3k goes up to the } of Game(), and P puts the lines above it. Both bodies are indented "
        "the same, so the indentation is already right."),
    "brace-11": ("di{",
        "di{ finds the { by looking ahead and deletes everything up to the }, the spaces inside the braces "
        "too. f{ldt} takes 6 keys."),
    "brace-12": ("ci{Getting started",
        "ci{ looks ahead to the braces of \\section and changes Intro. fIcwGetting started is one key longer."),
    "brace-13": ("ci{RELEASE",
        "ci{ looks ahead to the braces of ${NAME} and changes the name inside them. fNcwRELEASE is one key "
        "longer."),
    "brace-14": ("yi{jp",
        "yi{ yanks \" padding: 1rem; border-radius: 8px; \", spaces and all, and moves to its first character, "
        "the space after .card's {. Right below it is the { of .panel {}, so j lands on it, and p puts the "
        "declarations after it."),
    "brace-15": ("ca{\"1\"",
        "ca{ looks ahead to the inline table and replaces it, braces and all, so you type the short form "
        "\"1\". The comment after it stays where it is. f{C\"1\" is the same length, but C would delete the "
        "comment too."),
    "brace-16": ("di{{p3jdjp",
        "di{ deletes the three lines of the else body into the register, from its middle line, and leaves the "
        "cursor on the closing }. There are no blank lines above, so { goes all the way to line 1, and p puts "
        "the hit lines below the if. The old if body is now three lines further down: 3j gets to it, and dj "
        "deletes both of its lines, which leaves the cursor on } else {. p puts them below it. kd2j instead "
        "of di{ is one key longer, and so is gg instead of {."),
    "brace-17": ("ci{track();<Esc>3j.",
        "ci{ replaces the three lines of the first body with one indented line, where you type track();. The "
        "cursor stays on that line, and 3j lands in the second body, on its log line, where . does the same "
        "change. kc2j instead of ci{ is one key longer, and its . would only work from the top line of a "
        "body."),
    "brace-18": ("yi{GPjWcwred",
        "yi{ yanks the three declarations as whole lines. G goes to the last line, the } of .btn-danger, and "
        "P puts them above it, leaving the cursor on color: white;. j moves down to the background line, W "
        "jumps to blue;, and cw changes blue to red, leaving the ; alone. Doing the change last means the "
        "<Esc> is free. ky2j instead of yi{ is one key longer."),
    "brace-19": ("ci{return 404;",
        "The innermost braces around the cursor are the location block's, so ci{ replaces the three proxy "
        "lines with one line, indented like them, and you type the new directive. kc2j is one key longer."),
    "brace-20": ("<lt>i{kdd3j.",
        "<i{ shifts the three lines inside server's braces left one level and leaves the cursor on the first "
        "of them. k goes up to server: {, and dd deletes it. The lines below move up, so 3j lands on the "
        "line of the old closing brace, and . deletes it too. k<2j instead of <i{ is one key longer."),

    # ---------- i[ a[ ----------
    "bracket-1": ("ci[pos",
        "ci[ deletes index + offset from anywhere between the brackets and leaves you typing. T[ct] is two "
        "keys longer."),
    "bracket-2": ("di[",
        "The cursor is before the list, so di[ finds the next [ on its own and deletes everything up to "
        "the matching ]. $dT[ is one key longer."),
    "bracket-3": ("da[",
        "da[ deletes the brackets around the cursor and everything in them. F[d% does the same in 4 keys."),
    "bracket-4": ("ya[jp",
        "ya[ yanks [i + 1] by looking ahead along the line, and leaves the cursor on the [. Line 2 is "
        "shorter than that, so j lands on its last character, the s of ys, and p puts the brackets after "
        "it. f[Yjp ties, since the index ends the line and Y yanks to the end of it."),
    "bracket-5": ("ci[0",
        "ci[ looks ahead to the first [, then finds its partner: it skips the nested pair, so everything "
        "from indices to the inner ] is replaced. ct] would stop at the first ]. f[lC0] is 6 keys."),
    "bracket-6": ("ci[user guide",
        "ci[ finds the first [ on the line and changes the link text between the brackets. fdcwuser guide "
        "is one key longer."),
    "bracket-7": ("di[",
        "di[ deletes the three entries as whole lines, from anywhere in the list, and leaves both brackets "
        "on their lines. kd2j does the same in 4 keys."),
    "bracket-8": ("ci[LEN<Esc>j.j.",
        "ci[ looks ahead to the [ on line 2 and changes the size. After <Esc> the cursor is on the N of "
        "LEN, so j lands inside the next line's brackets (on line 4, on the ] itself, which counts as "
        "inside), and . repeats the change. With cw you'd have to get to the start of each number first."),
    "bracket-9": ("yi[j$P",
        "yi[ yanks the three items without the brackets. j$ goes to the end of line 2, the ] of the empty "
        "list, and P puts the items in front of it."),
    "bracket-10": ("ci[the setup guide<Esc>ci(docs/setup.md",
        "ci[ changes the link text, found by looking ahead from the start of the line. After <Esc> the "
        "cursor is just before the ], so ci( looks ahead again and lands in the link target. ftc2w would "
        "change this page too, but it's 2 keys longer than ci[."),
    "bracket-11": ("ci[-20:",
        "ci[ looks ahead to the brackets and changes :10 to -20:. f:C-20:] is one key longer, since C deletes "
        "the ] too and you type it back."),
    "bracket-12": ("ci[cfg(test)",
        "ci[ finds the [ right after the # and changes allow(dead_code), parentheses and all: only the square "
        "brackets matter to i[. lC[cfg(test)] is one key longer."),
    "bracket-13": ("ya[jP",
        "ya[ looks ahead to the list, yanks it with its brackets and moves to the [. Line 2 is shorter than "
        "that, so j lands on its last character, the ], and P puts the list in front of it. f[Yj$P is one key "
        "longer."),
    "bracket-14": ("ca[.get(key)",
        "ca[ looks ahead to [key] and replaces it, brackets and all, with the method call. Keeping key and "
        "swapping the brackets instead, f]r)F[r(i.get, is one key longer."),
    "bracket-15": ("ci[\"*\",",
        "[ ends line 1 and ] starts line 5, so ci[ replaces the three entry lines with one empty line, "
        "indented like them, and you type the new entry. kc2j is one key longer."),
    "bracket-16": ("$hci[size",
        "From the start of the line, ci[ would look ahead to the empty [] of int[] and type size into it. $ "
        "goes to the ; and h onto the ], and on a bracket, i[ is that pair. f[;ci[size is one key longer, and "
        "so is 4fnct]size, which needs the fourth n on the line."),
    "bracket-17": ("ci[v2.1<Esc>j.",
        "ci[ finds the first [ on the line and changes the link text. After <Esc> the cursor is on the 1 of "
        "v2.1, and j lands inside the link text below it, so . changes that one too. With cw you'd have to get "
        "back to the start of download on line 2: fdcwv2.1<Esc>jb. is 12 keys."),
    "bracket-18": ("da[.",
        "da[ looks ahead and deletes [\"response\"], brackets and all. That leaves the cursor on the [ of "
        "[\"payload\"], which counts as inside that pair, and . deletes it the same way. f[d2t[ is two keys "
        "longer."),
    "bracket-19": ("di[j$i, <Esc>p",
        "di[ looks ahead and deletes both items, leaving [] behind and the items in the register. j$ goes to "
        "the ] at the end of line 2, i, <Esc> types the separator in front of it, and p puts the items after "
        "the space. Putting first, with j$P, would leave the comma and space to squeeze in between the two "
        "strings."),
    "bracket-20": ("ca[.at(-1)<Esc>.",
        "ca[ looks ahead to the brackets and replaces them, index and all, with .at(-1). After <Esc> the "
        "cursor is on the ), outside every pair of square brackets, and there's no [ left on line 1, so . "
        "looks ahead onto line 2 and makes the same change there. You don't even need the j. f[C.at(-1);<Esc> "
        "also does line 1, but C has to retype the ;, and its repeat needs the cursor back on the [."),

    # ---------- ip ap ----------
    "ip-1": ("dap",
        "dap deletes the three lines of the paragraph and the blank line after it, so the headings end up "
        "one blank line apart. dip would leave two blank lines between them. kd3j is one key longer."),
    "ip-2": ("cipFeature complete.",
        "cip replaces the paragraph's three lines with one empty line and starts Insert mode there. The "
        "blank lines around it stay. cap would swallow the blank line after it, and kc2j is one key longer."),
    "ip-3": ("yapP",
        "yap yanks the function and the blank line after it, as whole lines, and moves the cursor to the "
        "def line. P puts the copy above it. ky2jP is one key longer."),
    "ip-4": (">ip",
        ">ip shifts every line of the paragraph right by one shiftwidth, 4 spaces. k>2j is one key longer."),
    "ip-5": ("dap}p",
        "dap deletes both lines and the blank line after them, leaving the cursor on import os. } jumps to "
        "the blank line after sys, and p puts the group below it, where its own blank line now separates "
        "it from main(). Deleting with k3dd is one key longer."),
    "ip-6": ("d2ap",
        "d2ap deletes two paragraphs, each with the blank line after it, from anywhere in the first one. "
        "dap. also works, in the same 4 keys. Counting lines, 2k7dd is one key longer."),
    "ip-7": ("cip",
        "On a blank line, ip is all the blank lines around it, so cip replaces all five with one empty "
        "line and starts Insert mode. There's nothing to type, and the <Esc> after it is free. dip would "
        "delete all five, and dipO takes 4 keys."),
    "ip-8": ("gcip",
        "gc is the comment operator from Project 03, and ip gives it the three lines of the paragraph, "
        "from wherever the cursor is in it. kgc2j is one key longer."),
    "ip-9": ("gUip",
        "gUip uppercases every line of the paragraph around the cursor. gUap ties, since the blank lines "
        "it adds have nothing to uppercase. kgU2j is one key longer."),
    "ip-10": ("yap}pj$r2kbcwbeta",
        "yap yanks the section and its blank line, and moves the cursor to [server.alpha]. } jumps to the "
        "blank line after it, and p puts the copy below, with the cursor on its first line. j$r2 turns the "
        "1 at the end of the next line into a 2. Then k goes back up to the ] and b to alpha, and cwbeta "
        "renames it. Doing the rename last means the <Esc> after it is free. With Ctrl-a (Project 03) "
        "instead of r2, it's 16 keys."),
    "ip-11": ("dip",
        "On a blank line, ip is all the blank lines around it, so dip deletes the three of them, wherever in "
        "the run the cursor is. k3dd is one key longer."),
    "ip-12": (">ip.",
        ">ip shifts every line of the drawing right by 4 columns, and . does it again for the other 4. {>}. "
        "ties: { goes up to the top of the drawing, and > with } shifts everything down to its end."),
    "ip-13": ("dap",
        "dap deletes the three lines of the debug service and the blank line after it, so web and db end up "
        "one blank line apart. {d} ties: { goes up to the blank line above, and d} deletes from there to the "
        "next one. k3dd is one key longer."),
    "ip-14": ("cipmake all",
        "cip deletes the three npm lines, keeps the blank lines on both sides, and leaves you on an empty line "
        "to type make all. kc2j is one key longer."),
    "ip-15": ("dap",
        "The lines around the prints hold only spaces, and the paragraph objects treat those as blank, so ap "
        "is the two prints and the line after them. dap deletes all three from the second print. { and } "
        "walk past lines of spaces, so {d} would delete far more, and k3dd is one key longer."),
    "ip-16": ("dap2j.",
        "dap deletes the first block and its blank line, leaving the cursor on import json. 2j lands on the "
        "second TODO comment, and . deletes that block the same way. With counted dd you'd have to start on "
        "each block's first line: k3dd2j. is one key longer."),
    "ip-17": ("yapGp/2<CR>r3",
        "The second block is the last paragraph in the file, so yap yanks it together with the blank line in "
        "front of it. G goes to the last line, and p puts the copy below it, blank line first, so the blocks "
        "stay apart. The cursor is on that blank line, and the next 2 after it is the last digit of the new "
        "address, so /2<CR> jumps right to it and r3 changes it. 2j$hr3 is one key longer."),
    "ip-18": ("dap3kP",
        "dap deletes parse() and the blank line after it, which leaves the cursor on main(). 3k goes up to "
        "def save, and P puts the function and its blank line above it. dap2{p and dap{{p tie: two { jumps "
        "reach the blank line above save(), and p puts the lines below it."),
    "ip-19": ("cipTBD.<Esc>5j.",
        "cip replaces the first placeholder's three lines with one, where you type TBD.. The cursor stays on "
        "it, and 5j lands in the middle of the second placeholder, where . does the same. kc2j instead of cip "
        "is one key longer, since its . then needs the paragraph's top line."),
    "ip-20": ("cip<Esc>}.",
        "cip on the first gap replaces all four blank lines with one empty line, and <Esc> leaves Insert "
        "mode. } jumps to the next blank line, the first of the second gap, and . does the same to its three. "
        "Deleting with counts, 3dd}2dd, is one key longer."),

    # ---------- iW aW ----------
    "iw-big-1": ("ciW\"$API_URL\"",
        "ciW changes the whole URL, since a WORD runs from one space to the next. ciw would only change "
        "example. BcW ties, but needs you to spot where the WORD starts."),
    "iw-big-2": ("daWfp.",
        "daW deletes -g with its dash and the space after it. fp lands inside -pedantic, and . deletes "
        "that WORD the same way, from the middle. BdW2W. ties: dW from the start of -g, then 2W to the "
        "start of -pedantic, where . repeats it."),
    "iw-big-3": ("yaWjp",
        "yaW yanks the path together with the space in front of it: there's no white space after the last "
        "WORD on a line, so aW takes the white space before it. j lands on the m of vim, the last "
        "character of the shorter line, and p puts the text after it. F Yjp ties: F<Space> goes back to "
        "the space, and Y yanks from there to the end of the line."),
    "iw-big-4": ("daW",
        "name, is one WORD, comma included, and aW adds the space after it, so daW leaves self, age. daw would "
        "only take name and leave two commas behind. bdW ties."),
    "iw-big-5": ("daW0wP",
        "daW deletes \"-avz \", dash and space included, from the middle of the flag. 0w goes to src/, and P "
        "puts the flag in front of it, its space now separating it from src/. BdW0wP ties, and so does "
        "daWFsP."),
    "iw-big-6": ("d2aW",
        "[10/Oct/2024:13:55:36 and +0000] are two WORDs, so 2aW is both of them with the spaces after them, "
        "and d2aW deletes them from the middle of the date. Bd2W and daW. tie, and F[dt\" is one key longer."),

    # ---------- is as ----------
    "sentence-1": ("das",
        "das deletes the sentence and the space after it, so the sentences around it stay one space apart. "
        "dis would leave two spaces. Without sentence objects you'd go back to its start first: FYdf.x is "
        "6 keys."),
    "sentence-2": ("cisIt is small.",
        "cis deletes the sentence, period included, but leaves the spaces around it, and you type the new "
        "one in its place. cas would take the space after it, which you'd then have to type again. "
        "FTct.It is small keeps the period but is one key longer."),
    "sentence-3": ("das0P",
        "das deletes the sentence and the space after it into the register. 0 goes to the start of the "
        "line, and P puts it there, its space now separating it from the first sentence."),
    "sentence-4": ("d2as",
        "A sentence ends at a period followed by a space, so Vim sees \"Pick a fast hash, e.g.\" and "
        "\"xxHash.\" as two sentences. d2as deletes both, with the space after the second. das. ties. das "
        "alone would leave xxHash. behind, and FPdtA is one key longer."),
    "sentence-5": ("yasGP",
        "yas yanks \"Back up your data first. \", space included, and moves to the start of the sentence. G "
        "goes to line 3, the last line, in the same column, and P puts the sentence in front of Run. 0ytTGP "
        "is one key longer: ytT yanks up to the T of Then."),
    "sentence-6": ("fNdasj.",
        "fN finds the first Note, and das deletes that sentence with the space after it, leaving the cursor "
        "on Then. j lands on the t of that in line 2, inside the other note, and . deletes it the same way. "
        "dtT would do line 1 in as many keys, but its repeat fails on line 2, which has no T to stop at."),

    # ---------- it at ----------
    "tag-1": ("cit${junit.version}",
        "cit changes what's between <version> and </version>. In the indentation, Vim starts from the "
        "first tag on the line. f4ct< does the same in 2 more keys."),
    "tag-2": ("c2itDocumentation",
        "it alone would be full, the inside of <em>. 2it goes out one level, to everything inside <a>, "
        "and the nested <em> goes with it. 2F>cit also works, two keys longer: on a tag counts as inside "
        "it."),
    "tag-3": ("datX",
        "dat deletes the whole <small> element from inside it, and leaves the cursor on the < of </h1>, "
        "just after the space. X deletes that space. F d2f> does it all in 6 keys."),
    "tag-4": ("catshipped",
        "at is the innermost element around the cursor, <span class=\"ok\">done</span>, tags and all, so cat "
        "replaces it with what you type. cit would keep the span tags, and F<c2f>shipped is three keys "
        "longer."),
    "tag-5": ("dit",
        "On the <div> tag, it is everything inside the div: the line break, the <p> line and the line break "
        "before </div>. it is never line-wise, so dit leaves the two tags side by side on one line. jddkJx "
        "takes 6 keys."),
    "tag-6": ("citn/a<Esc>j.j.",
        "In the indentation, Vim starts from the first tag on the line, so cit changes TODO. After <Esc> the "
        "cursor is on the a of n/a, and j lands in the next cell, on its text or on its closing tag, which "
        "both count as inside. . repeats cit there, and j. does the last cell. ct< would need to start "
        "right after each <td>."),

    # ---------- i< a< ----------
    "angle-1": ("di<lt>",
        "di< deletes everything between the angle brackets around the cursor, whatever its position. "
        "T<dt> does the same in 5 keys."),
    "angle-2": ("ya<lt>jP",
        "ya< finds the first < on the line, yanks up to the > that matches it, the outer one, and moves "
        "the cursor to the <. j lands on the space after Map on line 3, and P puts the type in front of "
        "it. f<y2f>jP is three keys longer."),
    "angle-3": ("ci<lt>lovelace@example.org",
        "ci< finds the first < on the line and changes everything up to the >, the whole address. $cT< "
        "is one key longer, and f<lct> three."),
    "angle-4": ("ci<lt>&str",
        "ci< looks ahead to Vec<String> and changes the type argument. fScw&str is one key longer."),
    "angle-5": ("fSdi<lt>",
        "From the start of the line, di< looks ahead to the < of n < 10, finds no pair, and does nothing. fS "
        "jumps into String, inside the real brackets, and di< deletes everything up to the matching >, the "
        "nested List<Integer> included. fSd2t> is one key longer."),
    "angle-6": ("ya<lt>f(P",
        "ya< looks ahead to Map<string, User[]>, yanks the brackets with what's in them, and moves to the <. "
        "f( finds the ( of Map(), and P puts the copy in front of it. f<yf>f(P is two keys longer."),

    # ---------- 2i( 2i{ ----------
    "nested-1": ("c2i(key",
        "The innermost pair around the cursor belongs to normalize( ), so i( would change name.trim(). "
        "2i( goes out one level, to the inside of contains( ). 2F(ci(key is two keys longer, and ci( from "
        "the start of the line would pick the if's parentheses."),
    "nested-2": ("c2i{// TODO",
        "From inside the loop, i{ is the loop's body, and 2i{ the method's. Its braces are on their own "
        "lines, so c2i{ replaces lines 2 to 6 with one indented line. Counting lines, 2kc4j is one key "
        "longer."),
    "nested-3": ("c3i(unique",
        "i( is the inside of set( ), 2i( of sorted( ), and 3i( of join( ). So c3i( replaces "
        "sorted(set(names)) in one go. 3F(ci(unique is two keys longer."),
    "nested-4": ("d2i[",
        "The cursor is inside [0, 1], which is inside the outer list, so 2i[ is everything in the outer "
        "brackets, and d2i[ deletes it. From the start of the line, di[ would find [\"grid\"] first, and "
        "$hdi[ is one key longer: $ lands on the ;, and h onto the outer ]."),
    "nested-5": ("c2i<lt>T[]",
        "The innermost angle brackets around the cursor are Map's, so i< would be string, T. 2i< is the pair "
        "around that, Promise's, and c2i< replaces Map<string, T> with T[]. 2F<ci<T[] is two keys longer, "
        "and ci< from the start of the line would change the <T> after load."),
    "nested-6": ("c2i(input<Esc>j.",
        "2i( goes one pair out from read( ), to the inside of parse( ), so c2i(input replaces "
        "read(\"a.json\"). After <Esc> the cursor is on the t of input, and j lands on the ( of read( on line "
        "2, which counts as inside read( ). So . with its count of 2 reaches parse( ) again. "
        "2F(ci(input<Esc>jF(. is four keys longer."),
}
