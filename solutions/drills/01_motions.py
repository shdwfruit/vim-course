"""Reference solutions for Project 01's drills (spoilers!). Each entry: drill -> (keys, explanation).

See one with:  python3 check.py drill W --show 3      Watch it typed:  python3 check.py drill W --watch 3
"""
SOLUTIONS = {
    # ---------- W B E ----------
    "bigword-1": ("2WD",
        "The whole URL is one WORD, so 2W goes from curl to -o in two hops. D deletes to the end of the "
        "line. The space left at the end doesn't matter (trailing spaces are ignored). With w you'd stop on "
        "every :, /, . and ? in the URL."),
    "bigword-2": ("Bi~/src <Esc>",
        "B goes back to the start of the WORD under the cursor, the ~ of ~/photos. b would stop on the s "
        "of photos, because / splits small words. i then types ~/src and a space in front of it."),
    "bigword-3": ("2Ea.bak",
        "From the d of diff, E goes to the end of diff and 2E to the end of the first path, the t of .txt. "
        "a appends after it. WEa.bak works too. With e you'd stop at the end of ., /, notes, /, old, - and "
        "so on."),
    "bigword-4": ("3WdW",
        "3W hops over -Wall and -Wextra to -O2. dW deletes the WORD and the space after it. dw would only "
        "delete the -, because - is punctuation and O2 is letters: two separate words."),
    "bigword-5": ("3WcWfix/login",
        "3W lands on feature/login-form. cW changes to the end of the WORD (like cw, it doesn't take the "
        "space after it), and you type fix/login. ffcW reaches it just as fast, since that's the first f."),
    "bigword-6": ("yEjp",
        "yE copies from the a to the end of the WORD: api.staging.example.com, without a space. j goes "
        "down to line 2; it's shorter, so the cursor lands on its last character, the @. p puts the host "
        "after it. yW would have copied the space after the WORD too."),
    "bigword-7": ("2Wd2W",
        "2W reaches --enable-debug, and d2W deletes two WORDs with their spaces, up to CFLAGS. With small "
        "words you'd be counting dashes and equals signs."),
    "bigword-8": ("cBname",
        "The cursor is on the ; at the end of item.getName().trim().toLowerCase();, all one WORD. B would "
        "go back to the i of item, and since a backward motion leaves out the character under the cursor, "
        "cB changes everything but the ;. Then type name. cT<Space> does the same in one more key."),
    "bigword-9": ("2WdWW.",
        "2W reaches -g and dW deletes it with its space, leaving the cursor on main.c. W hops to -O0, and . "
        "repeats dW there. f-;dW;. also works, one key longer."),
    "bigword-10": ("4Ea-debug<Esc>A -g",
        "E stops at the ends of gcc, -O2, -o and then build/app, so 4E lands on the p of app. a types "
        "-debug after it. Then A appends -g at the end of the line. The final <Esc> is free."),
    "bigword-11": ("BdW",
        "The cursor is inside cache.redis.pool:, one WORD. B goes back to its start, the c of cache, and dW "
        "deletes the WORD and the space after it. b would stop at the p of pool, since the dots split small "
        "words. dB then dW costs a key more."),
    "bigword-12": ("5Ea_2026",
        "E stops at the end of SELECT, user_id,, count(*), FROM and then analytics.events, so 5E lands on "
        "its last s. a appends _2026. 3fs gets there too, one key longer, since user_id and analytics have "
        "s's of their own."),
    "bigword-13": ("2Ex",
        "E from the c goes to the end of cd, and 2E to the end of the next WORD, the path: the last e of "
        "coursee. x deletes it. 2t<Space> also lands there, one key longer."),
    "bigword-14": ("5WdW",
        "W carries on into the next line: members, =, [\"crates/core\",, \"crates/cli\", and then "
        "\"crates/legacy-api\", is the fifth WORD. dW deletes it with its space. j4WdW is one key longer."),
    "bigword-15": ("Bd2B",
        "B from the ) goes back to the b of bbox_inches=\"tight\"). d2B deletes back over two WORDs, "
        "transparent=True, and dpi=300, with their spaces, and leaves the b. 3Bd2W also works, one key "
        "longer."),
    "bigword-16": ("Wi\"<Esc>W.h.A\"",
        "W reaches $1 and i\" types the first quote. W hops to $BACKUP_DIR/$1.old and . types another quote "
        "in front of it. h steps back onto the space, and . puts the quote that closes $1 before it. A\" "
        "adds the last one. Typing the closing quote of $1 with a or E-then-a\" breaks the . chain and costs "
        "a few keys more."),
    "bigword-17": ("6Wy2WjBP",
        "6W hops over RUN, apt-get, update, &&, apt-get and install to -y. y2W copies -y and "
        "--no-install-recommends with the spaces after them. Line 2 is shorter than that column, so j lands "
        "on its last character, in git. B goes back to the g, and P puts the flags in front of it. $By2B "
        "copies the same text from the other end, and ties."),
    "bigword-18": ("2Ea.gz<Esc>E.E.",
        "2E lands on the 1 at the end of access.log.1, and a types .gz. The cursor is on the z, the end "
        "of that WORD now, so E goes to the end of access.log.2, where . appends .gz again, and the same "
        "for access.log.3. 2t<Space> with ; instead of E is a key longer."),
    "bigword-19": ("EldE$p",
        "E jumps to the end of cp, and l onto the space after it. From a space, E goes to the end of the "
        "next WORD, so dE deletes \" app.db\", space first. $ and p put it after the other path, space "
        "included. f<Space>dE$p ties. dW from app.db would take the space after it instead, which ends up "
        "in the wrong place."),
    "bigword-20": ("3WdWjB.",
        "3W hops over CFLAGS and = and -O2 to -g, and dW deletes it with its space, leaving the cursor on "
        "-Wall. j goes down to the same column, the - of -lm. B steps back to the start of -g, and . "
        "repeats dW. /-g<CR>dWn. is a key longer."),
}
SOLUTIONS.update({
    # ---------- 0 ^ $ ----------
    "line-1": ("$i, 11",
        "$ lands on the ], and i inserts in front of it. A would put the cursor after the ], so you'd need "
        "a backspace and to type the ] again."),
    "line-2": ("^cwlong",
        "^ jumps from the end of the line to the i of int, skipping the indentation. cw changes int to "
        "long. 0 would land on the first space instead."),
    "line-3": ("0r|",
        "The line starts with spaces, so ^ would stop on the h. 0 always goes to column 1, and r| replaces "
        "the space there."),
    "line-4": ("d0",
        "d0 deletes from column 1 up to the cursor. 0 is a backward motion, so it's exclusive: the p under "
        "the cursor stays. d^ would have kept the indentation."),
    "line-5": ("d^",
        "d^ deletes back to the first non-blank character, the r of result, and stops there: the "
        "indentation and the p under the cursor stay."),
    "line-6": ("c^print",
        "c^ deletes logger.debug (everything from the first non-blank up to the cursor) and starts Insert "
        "mode with the indentation and the ( untouched. ^c3wprint also works, but logger.debug is three "
        "words, so it costs two more keys."),
    "line-7": ("2D",
        "D is d$, and with a count it goes on to the end of a later line: 2D deletes from the B to the end "
        "of line 2, laptop and charger included. d2$ does the same in one more key."),
    "line-8": ("$dF,",
        "$ jumps to the closing parenthesis. dF, deletes back to the last comma: a backward motion never "
        "includes the character under the cursor, so the ) survives. From the start, 2f,dt) takes 6 keys."),
    "line-9": ("$cbmachine",
        "$ lands on the period. cb changes back to the start of platform, and since a backward motion "
        "leaves out the cursor's character, the period stays."),
    "line-10": ("x^cf(return ",
        "x deletes the last ) while the cursor is already on it. ^ jumps to the p of print, and cf( "
        "changes print( into return and a space. The final <Esc> is free. Doing $x at the end instead "
        "would cost two more keys."),
    "line-11": ("$bcwMoney",
        "$ jumps to the { at the end of line 1, and b steps back to the start of number. cw changes it to "
        "Money. 2f: then w gets there too, in two more keys. (When the new word has as many letters as "
        "the old one, R types over it a key cheaper than cw.)"),
    "line-12": ("^dw",
        "^ jumps back from the end of the line to the #, the first non-blank character. # is a word of its "
        "own, so dw deletes it and the space after it, and the indentation stays. ^2x and ^dW tie."),
    "line-13": ("c0$ ",
        "c0 deletes from column 1 up to the cursor (0 is exclusive, so the p stays) and starts Insert mode, "
        "where you type $ and a space. F%d0 and then r$ would take six keys."),
    "line-14": ("$dT\"",
        "$ lands on the closing quote. dT\" deletes back till just after the opening quote, and since it's "
        "a backward motion, the closing quote under the cursor stays. f\"lD and then a\" takes six keys."),
    "line-15": ("$hr2",
        "$ goes to the closing quote at the end of the line, h back onto the last 1, and r2 replaces it. "
        "f1 would stop at the first 1 of the version, so 2f1r2 is a key longer."),
    "line-16": ("3Cnow backs off.",
        "C is c$, and a count carries it to the end of a later line: 3C deletes from used to the end of "
        "line 3, joining what's left of line 1 with Closes #142. below it, and starts Insert mode. c3$ "
        "does the same in one more key, and c/\\.<CR> stops before the period, so you'd retype less but "
        "spend more on the search."),
    "line-17": ("c^return <Esc>$r;",
        "c^ deletes console.log( (from the first non-blank up to the cursor, which stays) and you type "
        "return and a space. After <Esc>, $ jumps to the ) at the end, and r; turns it into a semicolon. "
        "A<BS>; instead of $r; ties."),
    "line-18": ("t#hDj$p",
        "t# stops on the space just before the #, and h steps onto the first of the two spaces. D cuts "
        "them and the comment. j goes down to line 2, $ to its end, and p puts the comment after the last "
        "character. 5f<Space> reaches the same space and ties; typing the comment again would take far more "
        "keys."),
    "line-19": ("i> <Esc>j0.j0.",
        "i types > and a space at the start of line 1. j goes down (to column 2), 0 back to column 1, and "
        ". inserts the same two characters there, before the indentation. The same again for line 3. I or "
        "^ then . would put the > after the indentation, inside the code."),
    "line-20": ("A |<Esc>k0r|",
        "A types a space and the | at the end of line 3. k goes up to line 2, 0 to column 1 (^ would stop "
        "on the i of install), and r| replaces the space there. k0r| first and then jA | ties."),
})
SOLUTIONS.update({
    # ---------- gg G {N}G ----------
    "gg-1": ("Gomain()",
        "G jumps to the last line, and o opens a line below it. Neovim's Python indenting adds four spaces "
        "after the colon, so you only type main(). 7jo works too, if you count the lines first."),
    "gg-2": ("ggO#!/bin/bash",
        "gg jumps to the first line, and O opens a new line above it for the shebang. 6kO ties, but gg "
        "needs no counting, however long the script is."),
    "gg-3": ("8GA;",
        "8G goes straight to line 8, the number in the error message. A appends the semicolon. :8<CR> gets "
        "there too, in one more key. 7j ties with 8G here, but only because you started on line 1."),
    "gg-4": ("5Grx",
        "5G goes to row 5, and since Neovim keeps the column, the cursor lands right below the x. rx books "
        "the seat. 3jrx ties. (In Vim, 5G would go to the first non-blank, the R.)"),
    "gg-5": ("dG",
        "dG deletes whole lines from the cursor's line to the last line. d} would stop at the blank line "
        "before print(\"tests done\"), and 4dd needs you to count the lines."),
    "gg-6": ("dgg",
        "gg is line-wise, so dgg deletes every line from the first one down to the cursor's line, all of "
        "the banner. d2k ties, but dgg needs no counting."),
    "gg-7": ("yGP",
        "yG copies the blank line and the chorus, from the cursor's line to the end. P puts line-wise text "
        "above the cursor's line, so the copy goes in front of the blank line and the song ends with the "
        "chorus twice. yGGp also works, one key longer."),
    "gg-8": (">G",
        ">G shifts every line from here to the end of the file right by one shiftwidth (four spaces). The "
        "print line keeps its extra level. 3>> and >2j both take three keys."),
    "gg-9": ("cGreturn 0",
        "cG deletes the three body lines and starts Insert mode on a single line, keeping the indentation of "
        "the first one, so you only type return 0. c2j does the same in one more key."),
    "gg-10": ("ddggp",
        "dd cuts the include line. gg jumps to the first line, and p puts the cut line below it. dd5kp "
        "ties, and :m1<CR> (Project 07) moves the line in five keys too."),
    "gg-11": ("ddGp",
        "dd cuts main() and leaves the cursor on the next line. G jumps to the last line, and p puts the "
        "cut line below it. 4jp after dd also works, one key longer, once you've counted the lines."),
    "gg-12": ("<G",
        "<G shifts every line from here to the end of the file left by one shiftwidth (four spaces), so "
        "the nested lines keep their extra levels. 5<< and <4j both take three keys."),
    "gg-13": ("yyGp",
        "yy copies the top border. G jumps to the last line, and p puts the copy below it. yy3jp is a key "
        "longer and needs counting."),
    "gg-14": ("ggJ",
        "gg jumps to line 1 from the bottom, and J joins line 2 onto it with one space. 7kJ ties, once "
        "you've read the relative line number; { would stop at each blank line on the way up."),
    "gg-15": ("yggGp",
        "gg is a line-wise motion, so ygg copies the four lines from the top down to the cursor's line. G "
        "goes to the last line, and p puts the copy below it. y3kGp ties, if you count the lines."),
    "gg-16": ("ggOBEGIN;<Esc>GoCOMMIT;",
        "gg jumps to line 1 and O opens a line above it for BEGIN;. G jumps to the last line, and o opens "
        "one below it for COMMIT;. { would stop at the blank line, and 3kO and 4jo need counting and cost a "
        "key more each."),
    "gg-17": ("GyypEr3$.",
        "G jumps to web-02's line and yyp puts a copy below it, with the cursor at its start. The address "
        "is one WORD, so E lands on its last character, the 2, and r3 replaces it. $ jumps to the other 2 "
        "at the end of the line, and . repeats r3 there. f2 instead of E is a key longer."),
    "gg-18": ("Odef main():<Esc>j>G",
        "O opens a line above the first one, where you type def main():. After <Esc>, j goes down to the "
        "old first line, and >G shifts it and every line after it right by one level. >GggOdef main(): "
        "ties: O starts the line indented, but Python's indenting moves it back to column 1 when you type "
        "the colon."),
    "gg-19": ("4GA;<Esc>8G.",
        "4G goes to line 4, the first line in the error list, and A; appends the semicolon. 8G goes to "
        "line 8, and . repeats the whole A;. 3jA;<Esc>4j. ties, but you'd have to work out the distances; "
        "with the line numbers from the compiler, G needs no arithmetic."),
    "gg-20": ("ddGpkddggP",
        "dd cuts exit 0, and G and p put it below the last line. The shebang is now just above it, so k "
        "and dd cut it, and gg and P put it above the first line. ddGPjddggP ties. Moving the shebang "
        "first (GddggPjddGp) takes a key more."),
})
SOLUTIONS.update({
    # ---------- % ----------
    "percent-1": ("%ithrows IOException ",
        "% jumps from the closing } to the { that opens the method, at the end of line 1. i inserts "
        "throws IOException and a space before it. gg$i also gets there, in two more keys, but % works "
        "the same way from the bottom of any block."),
    "percent-2": ("%a.strip()",
        "The cursor is on the n of name, not a bracket, so % searches forward on the line, finds the ( of "
        "input( and jumps to the ) that matches it. a appends .strip() after it. f)a.strip() is one key "
        "longer."),
    "percent-3": ("%d%x",
        "% looks ahead to the ( and lands on the matching ). d% deletes from there back to the (, both "
        "brackets included, which leaves two spaces in a row, and x deletes one of them."),
    "percent-4": ("%c%total",
        "% finds the first ( on the line and jumps to its partner, the ) after sum(b), skipping the two "
        "pairs nested inside. c% changes from there back to the (, inclusive, and you type total. "
        "f(c%total is one key longer."),
    "percent-5": ("%y%jP",
        "% lands on the ) of draw. y% copies (x, y, width, height) and leaves the cursor on the (, in "
        "column 5. j goes straight down to the ; of wipe; and P puts the copy before it."),
    "percent-6": ("%Oreturn 0;",
        "% jumps from the { of main() to its closing }. O opens a line above it, and Neovim's C indenting "
        "gives it four spaces. jjo also works but costs a key more, and % works however long the function is."),
    "percent-7": ("wd%",
        "w moves onto else. It isn't a bracket, so % looks ahead on the line, finds the { and jumps to its "
        "partner on line 5. d% deletes from else through that }, across the lines, and the space left at "
        "the end of line 3 doesn't count."),
    "percent-8": ("%A /* DEBUG */",
        "In C files, % pairs #ifdef with #endif, so it jumps there from line 1. A appends the comment. "
        "3jA costs a key more, and % finds the right #endif however long the block is."),
    "percent-9": ("%xF(x",
        "% looks ahead from the indentation to the ( and jumps to the ). x deletes it, then F( goes back to "
        "the ( and x deletes that. Deleting the ( first wouldn't work as well: with only a ) left, % has "
        "nothing to match."),
    "percent-10": ("f(a!(<Esc>%a)",
        "f( and a!( insert !( after the first (. After <Esc> the cursor is on the ( you typed. % counts "
        "forward from it, past the pair in isAdmin(), and lands on the old ), so a) can add the second "
        "closing parenthesis right after it."),
    "percent-11": ("%F)i, next",
        "% jumps from the } to the { at the end of line 1, however long the function is. F) goes back to "
        "the ) after res, and i types , next before it. From the top, ggf)i, next is a key longer."),
    "percent-12": ("f/d%",
        "f/ lands on the / of /*. In C files % pairs /* with */, so d% deletes the whole comment, across "
        "the line break: the rest of line 3 joins line 2, which leaves only a space after the semicolon "
        "(trailing spaces don't count). f/D and jdd takes six keys."),
    "percent-13": ("%i, [5, 6]",
        "The cursor isn't on a bracket, so % searches forward on the line, finds the outer [ and jumps to "
        "the ] that closes it, skipping the pairs inside. i inserts the new row before it. f];; reaches "
        "the same ] in three more keys, and $ would land at the end of the comment."),
    "percent-14": ("%c%[]",
        "% finds the [ at the end of line 1 and jumps to its partner on line 5. c% changes from there back "
        "to the [, both brackets and the three items included, and you type [] again. The rest of line 5 "
        "is empty, so the lines join."),
    "percent-15": ("t=d%",
        "t= stops on the space after opts. It's not a bracket, so % looks ahead, finds the { and jumps to "
        "its }. d% deletes from the space through that }, leaving opts) {. f=hd% and 2f<Space>d% take a "
        "key more."),
    "percent-16": ("f{c%x * 2",
        "f{ lands on the brace that opens the body. c% changes from it to the matching }, braces included, "
        "and you type the expression. $hhc% gets there with one more key."),
    "percent-17": ("%y%jt)P",
        "% from the i finds the ( of the condition and jumps to its ). y% copies (amount <= 0) back to the "
        "( and leaves the cursor there. j goes down to line 2, t) stops on the closing quote, just before "
        "the first ), and P puts the copy in front of it. 11W reaches the quote too, and ties; f\";P is a "
        "key longer."),
    "percent-18": ("3j$c%100",
        "3j and $ reach the ( at the end of line 4. c% changes from it through the ) four lines down, "
        "skipping the pair in avg(total), and you type 100. The text after the ) is empty, so line 8 joins "
        "line 4. /(<CR> instead of 3j$ ties."),
    "percent-19": ("wiround(<Esc>l%a, 2)",
        "w moves onto compute and i types round( before it. After <Esc> the cursor is on that (, which has "
        "no partner yet; l steps onto compute, and from there % finds its ( and jumps to the matching ), "
        "past the one that closes load(path). a adds , 2) after it. Doing the end first doesn't save "
        "anything: Ctrl-o can't take you back to the w, because Neovim keeps one jump per line."),
    "percent-20": ("c%do<Esc>%a ;<Esc>P",
        "From the w, % looks ahead to the ( and goes to its ), so c% changes while (running) into do, and "
        "keeps the old text in the register. From the o, % finds the { and jumps to the closing }. a types "
        "a space and a semicolon, and P puts while (running) in front of the semicolon. 3j would reach "
        "the } in a key more."),
})
SOLUTIONS.update({
    # ---------- { } ----------
    "paragraph-1": ("}Oimport json",
        "} jumps to the blank line after the four imports. O opens a new line above it, at the end of the "
        "block. 3jo does the same in one more key, once you've counted the lines."),
    "paragraph-2": ("{o@lru_cache",
        "{ jumps back to the blank line just above def fib(n):. o opens a line below it, right where the "
        "decorator goes. 3kO is one key longer."),
    "paragraph-3": ("}d}",
        "} jumps to the blank line after add(). From a blank line, d} becomes line-wise: it deletes that "
        "blank line and the whole unused() function, stopping before the next blank line."),
    "paragraph-4": ("y}Gp",
        "y} from the blank line copies it and the chorus below, as whole lines. G jumps to the last line, "
        "and p puts the copy below it: a blank line, then the chorus. y2jGp is one key longer."),
    "paragraph-5": ("}d}GP",
        "} lands on the blank line above length(). d} cuts the blank line and the method. G goes to the "
        "closing } of the class, and P puts the cut lines above it, blank line first."),
    "paragraph-6": (">}",
        ">} from the start of a line shifts every line up to the blank line, which itself is left out. "
        "3>> and >2j do the same in three keys."),
    "paragraph-7": ("c}Run make install.",
        "From the start of a line, c} is line-wise: it deletes the three TODO lines (but not the blank line "
        "after them) and leaves you typing on one empty line. c2j does the same in one more key."),
    "paragraph-8": ("d}",
        "From the middle of a line, d} deletes from the cursor through the end of the paragraph (else "
        "needs work. included) and leaves the blank line alone. The space left after review. doesn't count."),
    "paragraph-9": ("}d2}",
        "} jumps to the blank line under keep(). d2} deletes from there up to the second blank line ahead, "
        "line-wise: both old functions and the blank lines above them."),
    "paragraph-10": ("{dG{P",
        "{ jumps back to the blank line above greet(). greet() is the last block, so } would only reach the "
        "end of the file; dG cuts the blank line and the function instead. The next { lands on the blank "
        "line under the include, and P puts the cut lines above it."),
    "paragraph-11": ("d}",
        "From the start of a line, d} deletes whole lines from here up to the blank line, so the three old "
        "hosts go and the blank line and port stay. 3dd does the same in one more key."),
    "paragraph-12": ("<}",
        "<} shifts every line from here to the blank line left by one shiftwidth. 3<< and <2j take three "
        "keys."),
    "paragraph-13": ("{d}",
        "{ jumps back to the blank line above legacy_total(), wherever you are inside it. From a blank line "
        "d} deletes that line and the whole function, up to the next blank line. Counting lines with k "
        "and dd costs more."),
    "paragraph-14": ("d{",
        "{ from a blank line goes back to the previous blank line. As a motion it's exclusive and ends in "
        "column 1 here, so d{ deletes whole lines from that blank line down to the line above the cursor: "
        "the blank line and both DROP lines. d2k (the two DROPs and the blank line you're on) leaves the "
        "same text, in one more key."),
    "paragraph-15": ("dd{p",
        "dd cuts import argparse and leaves you on the blank line below the block. { from a blank line "
        "jumps back to the previous one, above the imports, and p puts the line just below it. ddkkP and "
        "dd2kP take a key more."),
    "paragraph-16": ("j>2}",
        "j goes down to line 2. With a count, } goes to the second blank line from here, so >2} shifts "
        "both blocks and the blank line between them (> leaves empty lines alone). j>4j and j5>> tie, "
        "if you count the lines."),
    "paragraph-17": ("{o```<Esc>}O```",
        "{ jumps to the blank line above the commands, and o opens a line below it for the first ```. "
        "After <Esc>, } jumps to the blank line below the commands, and O opens a line above it for the "
        "second. Going down first (}O```<Esc>{o```) ties. 2kO would need counting, and costs more."),
    "paragraph-18": ("}d}}.",
        "} jumps to the blank line above the first debug group, and d} deletes that line and the group. "
        "The cursor is left on the blank line above execute(job); } jumps to the next blank line, above "
        "the last print, and . repeats d}."),
    "paragraph-19": ("}d2}Gp",
        "} jumps to the blank line above ## Usage. d2} deletes up to the second blank line ahead, line-wise: "
        "the blank line, the heading, the blank line after it and the text. G goes to the last line and p "
        "puts the four lines below it, blank line first. j4ddGp ties, if you count."),
    "paragraph-20": ("}y}Gpjlcwreplica",
        "} jumps to the blank line above [database], and y} copies it and the section. G goes to the last "
        "line, and p puts the copy below it, with the cursor on its blank line. j and l get onto the d of "
        "database, and cw changes the word to replica. jw instead of jl ties."),
})
SOLUTIONS.update({
    # ---------- / ? n N ----------
    "search-1": ("/Tr<CR>cwFalse",
        "/Tr<CR> jumps to True. The capital T makes the search match case exactly, though tr would work "
        "here as well. cw changes the word. 5jfT ties if you count the lines, but the search needs no "
        "counting."),
    "search-2": ("?ll<CR>x",
        "?ll<CR> searches backward for a doubled l, and the first one it meets is in untill. x deletes "
        "one l. 2kFl;x also works, one key longer, because sadly has an l after it."),
    "search-3": ("/N<CR>nCbob@example.com",
        "/N<CR> lands on alice's N/A: with a capital in the pattern, the n of name doesn't count. n goes "
        "on to bob's N/A, and C replaces it to the end of the line."),
    "search-4": ("NdW",
        "Your last search was /TODO, forward, so n would find line 5. N searches in the opposite "
        "direction and lands on the TODO on line 2. dW deletes TODO: and the space after it. ?<CR> "
        "(search backward for the last pattern) is one key longer than N."),
    "search-5": ("d/c<CR>",
        "d/c<CR> deletes from name up to (not including) the next c, which is the first letter of "
        "created_at. The search crosses lines, so the three lines become one."),
    "search-6": ("c/,<CR>streams the file",
        "c/,<CR> deletes from reads up to the comma on line 2 (not including it), joining the two lines, "
        "and leaves you in Insert mode to type the new words."),
    "search-7": ("d/\\.<CR>",
        "In a pattern . matches any character, so d/.<CR> would delete only the comma. \\. matches a real "
        "dot, and the first one after the cursor ends things. d deletes up to it (not including it), so "
        "that period ends the new sentence."),
    "search-8": ("/ur<CR>xn.n.",
        "/ur<CR> lands on the u of the first colour. x deletes it. n jumps to the next ur and . repeats the "
        "x, twice. Searching for u alone would stop at default. (:%s/our/or/g in Project 07 does it in one "
        "command.)"),
    "search-9": ("/80<CR>cw100<Esc>nn.",
        "/80<CR> finds the 80 on line 1 and cw100 changes it. The first n lands on OLD_WIDTH's 80 and "
        "leaves it alone; the second reaches line 4, where . repeats the change. 2wcw100<Esc>3jF8. ties."),
    "search-10": ("$d/)<CR>",
        "$ jumps to the comma at the end of line 2. d/)<CR> deletes from it up to the next ), which is "
        "the one after None two lines down, so the extra arguments and line breaks all go."),
    "search-11": ("/2<CR>r4",
        "There's only one 2 in the file, so /2<CR> lands right on it, eleven lines down, and r4 replaces "
        "it. 11j$r4 is a key longer, and you'd have to count the lines."),
    "search-12": ("?30<CR>r1",
        "?30<CR> searches up from the last line and stops on the 3 of timeout=30. r1 turns it into 10. "
        "/30<CR> also works here, since it wraps around the end of the file. ggf3;r1 is a key longer (the "
        "first 3 on line 1 is in 5432)."),
    "search-13": ("? ]<CR>rx",
        "An open box is the only place with a space before a ], and a ] on its own is just a ] in a "
        "pattern. A backward search from line 1 wraps around the top of the file, so ? ]<CR> meets the "
        "last open box first and lands on its space. rx ticks it. /<Space>]<CR>nn takes two more keys, "
        "and G3k3lrx one more."),
    "search-14": ("/0]<CR>r1n.",
        "/0]<CR> finds the 0 in the first row[0]: a ] on its own is just a ]. (/[0] would be a character "
        "class, matching any 0, like the ones in 100.) r1 replaces it, and n. does the other one."),
    "search-15": ("?mo<CR>im<Esc>n.",
        "?mo<CR> searches up from the last line to the mo of the second accomodate. im<Esc> types the "
        "missing m in front of it. After a ? search, n keeps going up, to the first accomodate, and . "
        "types another m there."),
    "search-16": ("/50<CR>r3N.",
        "/50<CR> searches down from line 6 to the 5000 on line 7, and r3 makes it 3000. n would go on to "
        "CACHE_TTL, but N searches the other way, up to line 4, where . repeats the r3."),
    "search-17": ("/DE<CR>cwINFO<Esc>N.",
        "/DE<CR> lands on the DEBUG on line 1 and cw changes it to INFO. N searches backward from there, "
        "wraps around the top of the file and finds the last DEBUG, on line 8, where . repeats the change. "
        "n would have stopped at the parser's DEBUG first."),
    "search-18": ("/\\.l<CR>R.txt<Esc>n.n.",
        "In a pattern . matches any character, so \\. is a real dot: /\\.l<CR> finds .log and skips "
        "catalog (and the other dots, in ./ and .db). R types .txt over .log, and since every match starts "
        "on the dot, n. repeats it on each of the other two."),
    "search-19": ("/, D<CR>dt)n.n.",
        "With a capital in the pattern, /, D<CR> matches case exactly, so the comma in \"dry run, nothing\" "
        "doesn't match. It lands on the comma before DEBUG, and dt) deletes up to the ). n. repeats that "
        "on the other two log calls."),
    "search-20": ("cwBASE_URL<Esc>/AP<CR>.n.",
        "cw renames the first API, under the cursor. /AP<CR> has a capital, so it matches case exactly and "
        "skips api and the api in the URL. It lands on the API on line 2, . repeats the rename, and n. does "
        "line 3. * on API would also stop at every api, because * ignores smartcase."),
})
SOLUTIONS.update({
    # ---------- * # ----------
    "star-1": ("*dd",
        "* searches for debug_dump as a whole word and lands on the call in main(). dd deletes the line. "
        "6jdd works too, one key longer, if you count the lines."),
    "star-2": ("*cwconfig",
        "* searches for \\<log\\>, so logger and make_logger don't match, and the first hit is the argument "
        "on line 2. cw changes it to config."),
    "star-3": ("#biinline ",
        "# searches backward for clamp and lands on its definition. b steps back to int, and i types "
        "inline and a space before it. gg^wi is two keys longer than #b."),
    "star-4": ("*$r5",
        "There's no RETRIES after the cursor, so * wraps around to the top of the file, line 1. # would "
        "stop at the one on line 4 first. $ goes to the 3, and r5 replaces it."),
    "star-5": ("*cwcount<Esc>n.n.",
        "* jumps to the n on line 2; whole-word matching skips the n's inside int and read_count. cwcount "
        "renames it, n. does line 3, and the next n. wraps around to line 1. (*cgncount<Esc>.. is one key "
        "shorter: see :help gn, from this project's stretch goals.)"),
    "star-6": ("#cwaspect<Esc>n.",
        "# searches backward for \\<ratio\\> and lands on line 1. cw renames it. After #, n keeps going "
        "backward, wraps around the top of the file and finds the ratio on line 2, where . repeats the "
        "change. Changing line 2 first wouldn't work: the word under the cursor would be aspect by then."),
    "star-7": ("*cwNeovim<Esc>n.n.",
        "* ignores smartcase, so from vim it finds Vim at the start of line 2. cwNeovim changes it. n. "
        "changes the vim later on line 2, and the last n. wraps around to line 1. A typed search /vim "
        "would match all three as well, but costs more keys."),
    "star-8": ("d*",
        "* jumps to the next connect, and as a motion it's exclusive. It starts and ends in column 1, so "
        "d* deletes whole lines: the first three. 3dd does the same in one more key."),
    "star-9": ("*cwrows<Esc>nn.n.",
        "* lands on the data in clean(data), and cwrows changes it. The first n stops on the data in the "
        "message (a whole word there too), so press n again to skip it, then . on save(data). The last "
        "n. wraps around to line 1."),
    "star-10": ("*cwsize<Esc>n.n.",
        "* finds the count in return count; but not getCount, because there count isn't a whole word. cw "
        "renames it, n. does reset(), and the last n. wraps around to the field on line 1."),
    "star-11": ("#bcwlong",
        "# searches backward for total as a whole word and lands on its definition on line 2. b steps "
        "back to int, and cw changes it to long. (If the message said \"Total: \", # would stop there "
        "first: * and # ignore smartcase.)"),
    "star-12": ("*ea + 1",
        "The cursor is in the indentation, not on a word, so * uses the first word after it on the line, "
        "retries, and jumps to the next one, inside range(). e goes to its end and a types + 1. 2j$hi + 1 "
        "takes two more keys."),
    "star-13": ("#Oint z;",
        "# searches backward for Point and lands on the one in } Point;. O opens a line above it, and C "
        "indenting gives it four spaces, so you type int z;. 2kO is a key longer, and { would stop at the "
        "blank line."),
    "star-14": ("*cw3000<Esc>n.",
        "Numbers are words too, so * on the first 8080 finds the next whole 8080, the container port after "
        "the colon. cw changes it to 3000, and n. does the same for PORT. Changing the first one would be "
        "wrong: that's the host port."),
    "star-15": ("#br<",
        "* would stop at the MAX_ITEMS in add(). # searches backward, wraps around the top of the file and "
        "lands on the last MAX_ITEMS, in can_add(). The > is a word of its own, so b steps back onto it, "
        "and r< flips it. F> instead of b is a key longer, and 8jf>r< two."),
    "star-16": ("*cwwidth<Esc>N.",
        "* jumps from area's parameter to the w on line 2 (whole-word matching skips the w inside "
        "the words around it), and cw renames it. n would go on to perimeter(), but N goes back to the w on "
        "line 1, where . repeats the change. Renaming line 1 first would leave no w under the cursor."),
    "star-17": ("$*cwrevenue<Esc>n.",
        "$ lands on the t at the end of spent, and * uses the word the cursor is in, so it finds the spent "
        "on the last line. cw renames it, and n wraps around to the alias on line 1, where . repeats the "
        "change. Searching with /sp<CR> costs two more keys."),
    "star-18": ("*cwDIST<Esc>n.n.n.",
        "* on OUT searches for it as a whole word. $ isn't part of a word, so every $OUT matches, but "
        "OUT_DIR doesn't. It lands on line 3, cw renames it, and n. does line 4 and the $OUT on line 5. The "
        "last n. wraps around to line 1."),
    "star-19": ("*ddn.n.",
        "* jumps to the next dump, inside the if, and dd deletes the line. n finds dump(result) and . "
        "repeats dd; the last n wraps around to the first dump. Deleting the first line first would leave "
        "no dump under the cursor; ddjj.jj. takes a key more."),
    "star-20": ("iself.<Esc>*.*n.*.",
        "i types self. before the first count. After <Esc> the cursor is on the dot, which isn't part of "
        "a word, so * uses the next word on the line, count, and jumps to the count after it, where . types "
        "self. again. That leaves the cursor on a dot just before the count it fixed, where n would find "
        "the same count again; * from the dot goes on to the next one instead, the count in the message. "
        "n skips it, and . fixes the one after. *. does the last one, on line 5."),
})
SOLUTIONS.update({
    # ---------- ge gE ----------
    "ge-1": ("dgE",
        "The previous WORD is ys, with its comma, so gE lands on that comma. ge is inclusive, so dgE "
        "deletes from the comma through the e under the cursor and keeps the ). dF, would leave the e "
        "behind (backward motions don't take the cursor's character), so dF,x costs a key more."),
    "ge-2": ("gex",
        "From the end of tests, b would only go back to the t of tests. ge goes to the end of the previous "
        "word, the last e of thee, and x deletes it. 2Fex and bhhx both take four keys."),
    "ge-3": ("gEx",
        "gE skips back over the whole path ~/backup/notes/ and stops on the last character of the previous "
        "WORD, the stray /. x deletes it. F/ would stop at each slash in the path first: 3F/x is a key "
        "longer."),
    "ge-4": ("dgE",
        "From the opening quote of line 4, the end of the previous WORD is the closing quote at the end of "
        "line 3: gE crosses the line break. As a motion it's inclusive, so dgE deletes that quote, the line "
        "break, the indentation and the quote under the cursor, joining the two pieces. dge does the same "
        "here. b and B would go back to the start of .\" or download.\" and take the period too, and kJ "
        "leaves both quotes and a space between them to clean up: kJXxx is two keys longer."),
    "ge-5": ("d2gE",
        "Each column and its comma is one WORD (email, and phone,), so from the e of phone, gE lands on the "
        "comma after email and 2gE on the comma after name. d2gE deletes from there through the e, which "
        "leaves id, name, created_at. d3ge ties: ge counts the comma between email and phone as a word of "
        "its own. Deleting backward with d2F, leaves the e behind, so d2F,x is a key longer."),
    "ge-6": ("gEr,",
        "order.id. is one WORD and the cursor is in the next one, so gE goes straight to its last character, "
        "the stray period, and r, replaces it. F. would find the period in order.total first, so 2F.r, is a "
        "key longer, and so is 3ger, (ge also stops at the end of order and at the dot in order.total)."),
})
SOLUTIONS.update({
    # ---------- Ctrl-o Ctrl-i ----------
    "jumps-1": ("DG0ye<C-o>p",
        "D deletes width. G is a jump, so Neovim remembers where you were; 0ye copies BANNER_WIDTH from the "
        "last line. Ctrl-o jumps back to that exact spot, and p puts the name after the space. (Project 08's "
        "Insert-mode completion can type the name for you too.)"),
    "jumps-2": ("d%*f(y%<C-o>p",
        "d% deletes the empty (), leaving the cursor on the e of fetch_page. * jumps to the next "
        "fetch_page, in the def. f( and y% copy (url, timeout=10). Ctrl-o returns to the e, and p puts the "
        "parameter list right after it."),
    "jumps-3": ("D5Gf\"yE<C-o>p<Tab>d2k",
        "D deletes None. 5G jumps to the old line, f\" and yE copy the quoted path, and Ctrl-o goes back "
        "to line 1, where p puts it. Now Tab (Ctrl-i) goes forward in the jump list, back to the old line. "
        "d2k deletes it, the comment and the blank line above. Deleting first would lose the path, and "
        "deleting after the copy would replace it in the register. 4j would also get back down, one key "
        "longer than Tab."),
    "jumps-4": ("%r]<C-o>r[",
        "% jumps from the { to its partner on line 15, and r] replaces it. % is a jump, so Ctrl-o goes "
        "straight back to the {, where r[ finishes the job. Replacing the { first would break the pair, and "
        "then reaching the } takes 15G, 10j or /}<CR>: a key longer. `` instead of Ctrl-o is a key longer "
        "too."),
    "jumps-5": ("D22GplD<C-o>p",
        "D cuts the staging URL and leaves the cursor on the space before it. 22G jumps to the other URL's "
        "line, and since the column stays put, the cursor is on the space there too: p puts the cut URL "
        "right after it, then l and D cut the old one. Ctrl-o goes back to line 12, where you jumped from, "
        "and p puts it. `` instead of Ctrl-o is a key longer; 12G or 10k (or 10j and 10k instead of both "
        "jumps) are two longer."),
    "jumps-6": ("#dd<C-o>p",
        "# searches backward for the word under the cursor, import, and wraps around past the top of the "
        "file, so it lands on the last import: the stray one. dd cuts the line, and Ctrl-o jumps back to "
        "line 1, where p puts it below. gg or '' instead of Ctrl-o is a key longer, and so is 3* instead of "
        "# (the third import after this one) or 10G."),
})
SOLUTIONS.update({
    # ---------- `. g; gi ----------
    "changes-1": ("iprices<Esc>?la<CR>xpgi, tax",
        "i types prices before the ). <Esc>, then ?la<CR> searches back to the l of totla, and xp swaps "
        "it with the a. gi jumps back to where you stopped typing, right after prices, already in Insert "
        "mode, so you just carry on with , tax. (A golfer would fix the typo first and come back with "
        "Ctrl-o and i, two keys shorter; gi is for when you're already mid-sentence.)"),
    "changes-2": ("dwj0yw`.P",
        "dw deletes TODO and its space. j0 goes to the start of line 2, and yw copies API_BASE with the "
        "space after it. `. jumps back to where the delete happened, and P puts the name there. Deleting "
        "after the copy would have replaced it in the register. 2G and Ctrl-o instead of j and `. ties."),
    "changes-3": ("D/DE<CR>nyeg;p",
        "D deletes TODO. /DE<CR> finds DEFAULT_RETRY_COUNT, and n the next match, DEFAULT_TIMEOUT_SECONDS; "
        "ye copies it. That was two jumps, so Ctrl-o would need pressing twice, but g; goes straight to the "
        "last change, at the end of line 1. p puts the name after the space. (6GWye<C-o>p is shorter "
        "here, if you count lines.)"),
    "changes-4": ("de$ByE`.P",
        "de deletes TODO but not the spaces after it, so the comment stays where it was. $ and B get to the "
        "image name, the line's last WORD, and yE copies it. `. jumps back to where TODO was, and P puts the "
        "name there. 3W or fr instead of $B tie. Getting back without `. (2T: then p, or ^ f and a space, "
        "then p) is a key longer, and a search to the name is a jump on the same line, which Ctrl-o can't "
        "undo: it keeps only one place per line."),
    "changes-5": ("de-rsye2g;P",
        "de deletes TBD, and - goes up to where line 10 starts, right on the S. rs makes it lowercase and "
        "ye copies subtotal. That fix was a change too, so g; would only take you back to it; 2g; skips it "
        "and lands where TBD was, and P puts the name there. Every other way is at least a key longer: "
        "fixing the name before deleting TBD, jumping up with 10G^ or ?Su<CR> so that Ctrl-o can bring you "
        "back, or walking back with j and 2t- (or 11W and l)."),
    "changes-6": ("de-wye`.P",
        "de deletes TODO and leaves the cursor on the comma. - goes up a line to where the code starts, w "
        "moves to customerRepository and ye copies it. `. takes you back to the comma, and P puts the name "
        "before it. Walking back with j and f( then p is a key longer, and jumping up with 11G (or a search "
        "like ? c<CR>) so that Ctrl-o can bring you back is two longer."),
    # ---------- m ' ` ----------
    "marks-1": ("maG0ye`aP",
        "ma marks the spot. G goes to the last line and 0ye copies WELCOME_SUBJECT. `a jumps back to the "
        "exact column you marked, the ), and P puts the name before it. In a file this short, G is a jump, "
        "so Ctrl-o would bring you back too, and save the ma; a mark keeps working however many jumps and "
        "edits you make in between."),
    "marks-2": ("ma$%d'a",
        "ma marks the if line. $ and % jump to the closing } of the block. d'a deletes whole lines from "
        "there back to the marked line. Here d3j is shorter, because you can count four lines at a glance; "
        "with a block of 40 lines, the mark (or % and d'' for the line you jumped from) saves counting."),
    "marks-3": ("ma$%y'aGp",
        "ma marks the first line, $% jumps to the closing }, and y'a copies the five lines from the mark to "
        "there. G goes to the last line and p puts the copy below it. y4jGp is shorter in a file this "
        "small; the mark approach works the same however long the function is."),
    "marks-4": ("/ru<CR>xp>''.",
        "/ru<CR> lands on the misplaced r of retrun, and xp swaps it with the u. The search was a jump, so "
        "Neovim remembers line 12 as where you came from: '' as a motion is a line-wise trip back there, and "
        ">'' indents lines 12 to 23. That leaves the cursor on line 12 with '' pointing at line 23, so . "
        "indents the same lines again. Indenting first with >11j. and fixing the typo last is a key "
        "longer; fixing first and then Ctrl-o and >11j. is two longer. >} would stop at the blank line in "
        "the middle."),
    "marks-5": ("/ks<CR>xpy''P",
        "/ks<CR> lands on the k of deks, and xp makes it desk. The search was a jump from line 4, so y'' "
        "copies every line from here back to line 4, and leaves the cursor there. P puts the copy above, "
        "which gives the same text as putting it below. y13k instead of y'' is a key longer, copying first "
        "means fixing deks twice, and y} would stop at the blank line inside the order."),
    "marks-6": ("/dn<CR>xpd''Gp",
        "/dn<CR> jumps to the d of adn, and xp makes it and. You jumped there from line 4, so d'' cuts lines "
        "4 to 14, from the blank line through the end of the section. G goes to the last line and p puts "
        "them below it. d10k instead of d'' is a key longer, and so is cutting first with d10j and fixing "
        "the typo after the move (with the n of find in the way, tn won't reach it). d} would stop at the "
        "first blank line."),
})
