"""Reference solutions for Project 05's drills (spoilers!). Each entry: drill -> (keys, explanation).

See one with:  python3 check.py drill named --show 3      Watch it typed:  python3 check.py drill named --watch 3
"""
SOLUTIONS = {
    # ---------- "a … "z ----------
    "named-1": ('"ap',
        "\"ap puts register a after the cursor. Because the register holds a whole line, it goes in below "
        "the current line, no matter where the cursor is in it. Typing the import would take 23 keys."),
    "named-2": ('2f<"bP',
        "2f< jumps to the second <, the one after new. Register b holds part of a line, so \"bP puts "
        "HashMap into the line, just before the cursor. $F<\"bP and f<;\"bP are also 6 keys."),
    "named-3": ('"aPj"apG.',
        "\"aP puts the border above the title. j moves to the title, and \"ap puts one below it. . repeats "
        "the last change, and for a put that includes the register, so G. puts register a after the last "
        "line."),
    "named-4": ('"a2p',
        "\"a2p puts register a twice. It holds two whole lines, so each copy goes in below the cursor's "
        "line as a separator and an empty row. The count can go first too: 2\"ap."),
    "named-5": ('2j"aP3j.j"bp4k.',
        "2j goes to the first trace and \"aP puts #ifdef DEBUG above it. 3j reaches the second trace, and "
        ". repeats \"aP there. j\"bp puts #endif below it, and 4k. goes back to the first trace and repeats "
        "that. Grouping the puts by register lets . do half the work."),
    "named-6": ('ci"<C-r>a<Esc>j.',
        "ci\" deletes the first URL inside its quotes, and Ctrl-r a types register a in its place. After "
        "<Esc>, j moves to the next line (still inside the quotes) and . repeats the whole change. In "
        "Visual mode, vi\"\"ap would replace one URL in 6 keys, but it can't be repeated with ."),
    "named-7": ('"ayiwjyiwolimits = (<C-r>a, <C-r>0)',
        "\"ayiw yanks MAX_CONNECTIONS into register a. jyiw yanks the second name the normal way, into "
        "\"\" and \"0. o opens the new line, and Ctrl-r a and Ctrl-r 0 type the names as you build it. With "
        "only one register, you'd have to leave Insert mode and go back for the second name (30 keys). Project 08's "
        "Ctrl-n completion would type the names in fewer keys."),
    "named-8": ('W"ay$jwy$o[<C-r>"](<C-r>a)',
        "W jumps to the URL and \"ay$ yanks it into register a. jw lands on ASCII, and y$ yanks the title "
        "into \"\". o opens the new line, where Ctrl-r \" and Ctrl-r a type the two parts around the "
        "brackets. Without register a, you'd type the line in two trips (21 keys)."),
    "named-9": ('W"ay$jwy$oSigned-off-by: <C-r>a <lt><C-r>">',
        "W jumps to Ada and \"ay$ yanks the name into register a. jw lands on the address, and y$ yanks it "
        "into \"\". o opens the new line, and the two Ctrl-r's type the name and the address. With one "
        "register you'd have to leave Insert mode, go back for the address and append it (34 keys)."),
    "named-10": ('"ayiwjyiwolog.debug("<C-r>a=%s <C-r>0=%s", <C-r>a, <C-r>0)',
        "\"ayiw yanks user_id into register a and jyiw yanks retries into \"0. o opens the new line, and "
        "every name in it is a Ctrl-r: two keys instead of seven. Typing the whole line takes 53 keys, and "
        "yanking only user_id takes 47. "
        "Project 08's Ctrl-n completion would also save keys here."),
    "named-11": ('"ap5j.',
        "\"ap puts the saved line below line 1, as the first line of parse, and leaves the cursor on it. 5j "
        "goes down to function render(tree) {, and . repeats the put with the same register, below that "
        "line. }j. also takes 6 keys. Typing it with odebugger;<Esc> takes 11 keys each time."),
    "named-12": ('2j$"aPj.j.',
        "2j goes to user_id and $ to the comma at the end of the line. \"aP puts the register before the "
        "cursor, so NOT NULL lands just before the comma, and the cursor ends on the last L. That's past "
        "the end of the next line, so j lands on its last character, the comma, and . repeats the put with "
        "register a. It works once more for placed_at. (j$. on each line is a key longer.) Typing i NOT "
        "NULL<Esc> once and repeating it takes 18."),
    "named-13": ('/C<CR>cw<C-r>a<Esc>n.n.',
        "/C<CR> finds the first CHANGEME: the pattern has a capital letter, so smartcase makes it match "
        "case, and no other capital C is in the file. cw changes the word (the / after it ends it), and "
        "Ctrl-r a types the host name. n finds the next CHANGEME and . repeats the change, register and "
        "all. ciw is one key longer, and moving there with +fC costs more than n."),
    "named-14": ('2w"ayejyeofloat t = <C-r>a(<C-r>0(0));',
        "2w reaches clamp_temperature, and \"aye yanks it into register a: from the start of a word, e is "
        "its end. j lands on read_sensor_channel (both lines start with static float), and ye yanks it "
        "the normal way, into \"0. o opens the new line, and Ctrl-r a and Ctrl-r 0 type the two names. "
        "\"ayiw and yiw are 2 keys longer; yanking up to the ( with yf( ties. Typing both names takes 23 "
        "keys more."),
    "named-15": ('Gdk"ap',
        "G goes to pass, and dk deletes it and the line above, the TODO comment. The cursor is then on "
        "def area(shape):, and \"ap puts the three saved lines below it. Visual mode ties: GVk\"ap "
        "replaces the selected lines with the register."),
    "named-16": ('/0<CR><C-v>2jE"ap',
        "/0<CR> finds the first 0 in the file, the start of core's version. Ctrl-v 2j E selects the three "
        "old versions as a block (E reaches the end of 0.9.0). Register a holds part of a line, and putting "
        "that over a block puts it on every line of the block, so \"ap replaces all three. 2jf0 to get there "
        "is a key longer. ciW<C-r>a<Esc> with j. j. takes 13 keys, and a block c that types 1.0.0 takes 14."),
    "named-17": ("8w<C-v>3jI<C-r>a<Esc>",
        "8w lands on the > of the first <button> (jf> is a key longer). All four buttons start the same "
        "way, so the four > are in one column: Ctrl-v 3j selects them, and I inserts before the block. "
        "Ctrl-r a types the register into the first line, and <Esc> copies it to the other three. A block A "
        "after the n ties. jf>\"aP, then +;. on each other line, takes 15 keys."),
    "named-18": ('jw"aye+"bye+ye6wC<C-r>a(<C-r>b=3, <C-r>0=0.5)',
        "jw lands on RetryPolicy, and \"aye yanks it into a. + goes to max_attempts, yanked into b with "
        "\"bye, and +ye yanks backoff_seconds into \"0. 6w reaches None (G2W is a key longer) and C replaces "
        "it: Ctrl-r a, Ctrl-r b and Ctrl-r 0 type the names around the parts you type. Each Ctrl-r saves 5 "
        "or more keys over typing the name, and yiw instead of ye costs 3 more."),
    "named-19": ('jl<C-v>2j7ld"ap7l.',
        "Register a is a block, so \"ap inserts it on three lines at once and pushes the rest of each "
        "line to the right. Make room first: jl goes into the wall, and Ctrl-v 2j 7l d deletes 8 columns "
        "of spaces from lines 2 to 4. \"ap puts the window after the cursor, in column 3, and leaves the "
        "cursor at its top-left corner. 7l moves to the last space before the second spot, and . repeats "
        "the put. Selecting each spot and replacing it (Ctrl-v 2j3l\"ap) takes 21 keys."),
    "named-20": ('"ap2j.2j.j"bp4k.4k.',
        "Group the puts by register, so . does most of them. \"ap puts ```sh below line 1, above pip. 2j "
        "goes to Then create a config:, and . puts ```sh below it; 2j. does the same above garden serve. "
        "j moves onto garden serve and \"bp puts ``` below it. 4k goes up to garden init, . closes that "
        "block, and 4k. closes the pip one. Alternating \"ap and \"bp for each command takes more keys."),
    # ---------- "0 ----------
    "yank0-1": ('yyjdd"0p',
        "yy yanks the border into registers \" and 0. jdd deletes the TODO line, which replaces the unnamed "
        "register, so p would put \"| TODO |\" back. \"0p still has the border and puts it below the results "
        "line. Here you could also reorder (jddkyyjp, or yyGp2Gdd, both 8 keys), but when the delete has to "
        "come first, \"0 is how you get the yank back."),
    "yank0-2": ("wyiwjciw<C-r>0<Esc>+.",
        "wyiw yanks Mississippi. j lands inside Misisipi, and ciw deletes it, which fills the unnamed "
        "register with the misspelling. Ctrl-r 0 types the yank instead. + goes to the first word of the "
        "next line and . repeats the change. Typing the 11 letters would cost more than Ctrl-r 0's two keys."),
    "yank0-3": ("wyiwj$bciw<C-r>0<Esc>j$b.",
        "wyiw yanks monthlyRate. j$b lands on rate at the end of line 2, and ciw plus Ctrl-r 0 replaces it "
        "with the yank. j$b. does the same on line 3. Neovim's Visual P (which replaces without touching "
        "the registers) works too, but viwP on each line costs one key more than a single change and a ."),
    "yank0-4": ('yi"jci"<C-r>0<Esc>j.',
        "yi\" yanks eu-west-1. On line 2, ci\" deletes us-east-2 into the unnamed register, and Ctrl-r 0 "
        "types the yank. j moves down (still on the line, where ci\" finds the quotes) and . repeats it. "
        "Visual vi\"P on each line takes one key more."),
    "yank0-5": ("yi(jci(<C-r>0<Esc>j.",
        "yi( yanks the arguments of plot. j moves down, and ci( deletes the scatter arguments (here it "
        "works from just before the parentheses too). Ctrl-r 0 types the yanked arguments, and j. repeats "
        "the change on fill_between."),
    "yank0-6": ("j2Wy$jBC<C-r>0<Esc>jB.",
        "j2W reaches the cache path and y$ yanks it. j lands inside /tmp/logs, B goes back to its first "
        "character, and C deletes to the end of the line and types register 0 with Ctrl-r 0. jB. does the "
        "same to the tmp line. C deleted /tmp/logs into the unnamed register, so Ctrl-r \" would have typed "
        "that back."),
    "yank0-7": ("yf jcf(<C-r>0<Esc>+.",
        "yf<Space> yanks fprintf(stderr, through the space after the comma. j moves to line 2, and cf( "
        "changes printf( into the yank with Ctrl-r 0. + jumps to the first character of line 3, where . "
        "repeats it. Visual vf(P per line would take one key more."),
    "yank0-8": ("wyt_jct_<C-r>0<Esc>+w.",
        "w moves to particle_init and yt_ yanks particle, everything up to the underscore. j lands on pt_ "
        "in the next line, ct_ changes pt, and Ctrl-r 0 types particle. +w gets to pt_draw, and . repeats "
        "it. Typing particle twice would cost one key more, and more for a longer name."),
    "yank0-9": ("2Wy$dd$bciw<C-r>0<Esc>j$b.",
        "2W reaches settings.get and y$ yanks the expression. dd deletes line 1, so the unnamed register "
        "now holds that whole line, but register 0 still has the expression. $b lands on timeout, ciw and "
        "Ctrl-r 0 inline it, and j$b. does the second one. Doing the replacements first and the dd last "
        "takes 21 keys."),
    "yank0-10": ("3wyiw2jf3ciw<C-r>0<Esc>jF3.ggF0vp",
        "3wyiw yanks TIMEOUT_SECONDS. 2jf3 reaches the first 3600, and ciw with Ctrl-r 0 replaces it. jF3. "
        "does the second. Each change put the 3600 it deleted into the unnamed register, so it's there for "
        "the last step: gg goes up (keeping the column), F0 finds the 0, and vp replaces it with 3600. "
        "Register 0 holds the yank, and \"\" holds what you last deleted, so you get both."),
    "yank0-11": ("wye/any<CR>cw<C-r>0<Esc>n.n.",
        "w moves to UserRecord and ye yanks it (from the start of a word, e reaches its end). /any<CR> "
        "finds the first any, and cw deletes it into the unnamed register, so Ctrl-r 0 is the one that "
        "types UserRecord. n finds the next any and . repeats the change, twice. /ny<CR> with ciw ties. "
        "Visual P on each one (viwP) takes 23 keys."),
    "yank0-12": ("ya{jca{<C-r>0<Esc>+.+.",
        "ya{ yanks fg's initializer, braces included: a{ finds the next pair of braces on the line, so "
        "there's no need to move onto it. j goes to bg, ca{ replaces its { 0 }, and Ctrl-r 0 types the yank "
        "(ca{ just put { 0 } in the unnamed register). + goes to the start of the next line and . repeats "
        "the change, twice. Visual P with va{P on each line takes 18 keys."),
    "yank0-13": ("jyit4jcit<C-r>0<Esc>4j.",
        "jyit yanks 5.11.3, the text inside <junit.version>, and leaves the cursor at its start. 4j lands "
        "on the closing tag of the first <version> line, and cit works from there: it deletes 5.10.0 "
        "into the unnamed register, and Ctrl-r 0 types the yank. The second <version> is 4 lines further "
        "down, so 4j. does it. vitP on each one takes 16 keys."),
    "yank0-14": ("f'y$/?<CR>s<C-r>0<Esc>n.n.n.",
        "f' goes to the opening quote and y$ yanks 'acme-industries' with both quotes. /?<CR> finds the "
        "first placeholder (? is an ordinary character in a / search), s deletes it into the unnamed "
        "register, and Ctrl-r 0 types the yank. n. does each of the other three. With only one character "
        "to replace, vP (Visual P keeps the registers) is close: nvP for each takes 18 keys."),
    "yank0-15": ("yi<+ci<<C-r>0<Esc>+.+.",
        "yi< yanks OrderLine. Like i(, i< finds the next pair of angle brackets on the line, so it works "
        "from column 1. + goes to the start of line 2, where ci< deletes the ? and Ctrl-r 0 types the yank. "
        "+. does each of the other lines. Visual P (vi<P) on each line takes 18 keys."),
    "yank0-16": ("9wy$jciw<C-r>0<Esc>j.j.",
        "9w reaches eu-west-1 (the commas are words of their own), and y$ yanks it. j lands inside TBD on "
        "the next line, and ciw replaces it with Ctrl-r 0. After the change the cursor is at the end of the "
        "new region, past the end of the shorter next line, so j puts it on that line's last letter, inside "
        "TBD again, and . repeats. j$T, to get to the region is 2 keys longer, and viwP on each line takes "
        "19."),
    "yank0-17": ("3wyt;/le<CR>c2t.<C-r>0<Esc>n.n.",
        "3w reaches garden (the dots are words of their own), and yt; yanks garden.core.model. /le<CR> "
        "finds legacy, and c2t. changes up to just before the second dot after it, which is "
        "legacy.util. Ctrl-r 0 types the yank, and n. does the other two imports. The import lines don't "
        "line up (static), so a block can't do them at once."),
    "yank0-18": ("+y$/pa<CR>S<C-r>0<Esc>n.",
        "+ goes to the first non-blank of line 2, and y$ yanks the logger line without its indentation. "
        "/pa<CR> finds the first pass. S clears the line but keeps its indent (and puts the old text in "
        "the unnamed register), and Ctrl-r 0 types the yank. n. does the second one. Ctrl-r \" would type "
        "the pass line back, and doubles its indent."),
    "yank0-19": ("$yiW+cW<C-r>0<Esc>+.+.",
        "$ goes to the end of line 1 and yiW yanks <redacted>. + goes to the start of the next line, and "
        "cW changes the address, which is one WORD, dots and all. That fills the unnamed register with "
        "the address, so Ctrl-r 0 types the yank. +. does the other two lines. cE works the same, and "
        "vEP on each line takes 16."),
    "yank0-20": ("WyEci(<C-r>0<Esc>j.GA <C-r>0",
        "W jumps to the URL and yE yanks it. ci( finds the next parentheses even on a later line, so from "
        "line 1 it replaces the first TODO with Ctrl-r 0, and j. does the second link. Both changes put "
        "TODO in the unnamed register, so at the bottom, GA appends a space and Ctrl-r 0 types the URL. "
        "Filling in the reference first, with Ctrl-r \", takes 19."),
    # ---------- "_ ----------
    "blackhole-1": ('jddj"_ddp',
        "jdd cuts the return into the unnamed register. j moves to the print, and \"_dd deletes it into "
        "the black hole, leaving the cursor on check(xs). p puts the return below it. With a plain dd, the "
        "print would replace the return in the unnamed register; jdd jdd \"2p also takes 9 keys."),
    "blackhole-2": ('yy2j"_ddp',
        "yy yanks the --- line. 2j reaches the draft line, and \"_dd deletes it without touching the "
        "unnamed register. The cursor lands on the date, and p puts the --- below it. dd and \"0p tie, and "
        "so does putting first and deleting after (yy3jp2kdd)."),
    "blackhole-3": ('ddf/"_Djp',
        "dd cuts the return. f/ jumps to the comment, and \"_D deletes to the end of the line into the "
        "black hole. jp puts the return below log(result). The two spaces left at the end of the line "
        "don't count. A plain D and then j\"1p also takes 9 keys: D is a small delete, so it doesn't touch "
        "register 1."),
    "blackhole-4": ('dd"_ddj.p',
        "dd cuts free(buf). \"_dd deletes the first puts, and j. repeats that delete, black hole and all, "
        "on the second one. The cursor ends on fclose(in), and p puts free(buf) below it. With plain dd, "
        "dd j. leaves free(buf) in register 3, so \"3p ties at 9 keys."),
    "blackhole-5": ('dd"_3ddp',
        "dd cuts cleanup(). \"_3dd deletes the three commented lines into the black hole, and the cursor "
        "lands on save(). p puts cleanup() below it. A plain 3dd ties too, with \"2p: one delete of three "
        "lines is one entry in the history."),
    "blackhole-6": ('dd"_djjp',
        "dd cuts main(). d with the motion j deletes two whole lines, the current one and the one below, "
        "and \"_ sends them to the black hole. The cursor is on def main(), so jp puts the call after "
        "run(). dd dj j\"2p also takes 8 keys."),
    "blackhole-7": ('dd$"_xjp',
        "dd cuts the return, and the cursor lands on line 2. $ goes to the last ), and \"_x deletes it "
        "without saving it. jp puts the return below validate(result). x on its own doesn't touch "
        "register 1, so dd$xj\"1p is also 8 keys."),
    "blackhole-8": ('dd"_dwjp',
        "dd cuts exit 0, and the cursor lands on sudo. \"_dw deletes the word and its space into the "
        "black hole. jp puts exit 0 below echo. Putting first and deleting after (ddjpggdw) is also 8 "
        "keys."),
    "blackhole-9": ('dd"_dapp',
        "dd cuts garden --help, and the cursor lands on the Old notes heading. \"_dap deletes that "
        "paragraph and the blank line after it into the black hole. The cursor is on ## Usage, and p puts "
        "the cut line below it. dd dap \"2p ties: a paragraph is a delete of whole lines, so it pushes the "
        "first cut down to register 2."),
    "blackhole-10": ('$byiwj"_ddfAviwp',
        "$b lands on LinkedList, and yiw yanks it. j\"_dd deletes the ArrayList import into the black hole, "
        "so the unnamed register still holds LinkedList. fA reaches ArrayList, and viwp replaces it. A "
        "plain dd with viw\"0p ties at 16 keys."),
    "blackhole-11": ('dd"_ddGp',
        "dd cuts the trap line, and the cursor lands on the echo. \"_dd deletes it into the black hole, so "
        "the unnamed register still holds the trap. G goes to the closing brace and p puts the trap below "
        "it. Deleting the echo first (jddkddGp) ties, and so does dd dd G\"2p."),
    "blackhole-12": ('dd%"_dF,jp',
        "dd cuts free(buf). % jumps from the start of the fread line to the ) that closes its first "
        "bracket, and \"_dF, deletes backward to the comma before it (F is exclusive of the cursor, so the ) "
        "stays), into the black hole. jp puts free(buf) below fclose(fp). dF, is a small delete, so a plain "
        "dF, and j\"1p ties, and so does fixing the call first (j%dF,kddjp)."),
    "blackhole-13": ('wdw"_dw0P',
        "w moves to public, and dw cuts it with its space into the unnamed register, leaving the cursor "
        "on final. \"_dw deletes final and its space without touching any register, so 0P puts public "
        "back at the start of the line. With a plain dw, \"\" and \"- would both hold final, and neither "
        "is a numbered register. Deleting final first (2wdwbdw0P) ties."),
    "blackhole-14": ('jddG"_dkp',
        "jdd cuts the trailer. G goes to the last comment line, and dk deletes it and the line above; "
        "\"_ sends them to the black hole. The cursor lands on the blank line after the body, and p puts "
        "the trailer below it. A plain dk and \"2p ties (two lines deleted in one go are one entry in "
        "the history)."),
    "blackhole-15": ('jdd"_ditjp',
        "jdd cuts the script line, and the cursor lands on the paragraph. \"_dit empties the tag into the "
        "black hole (dit works from the <p of the tag). jp puts the script line below <main>. dit and "
        "j\"1p ties, and so does emptying the paragraph first (2jditkddjp)."),
    "blackhole-16": ('+dd"_cwlet<Esc>jp',
        "+ goes to the return's first character, and dd cuts the line; the cursor keeps its column, on "
        "const. \"_cwlet changes const without putting it in the unnamed register. jp puts the return "
        "below the loop. cw and j\"1p ties (cw is a small change, so \"1 keeps the return), and so does "
        "fixing const first (2+cwlet<Esc>-ddjp)."),
    "blackhole-17": ('ddf,"_d%jp',
        "dd cuts the close call. f, goes to the comma after sql. % from there jumps to the match of the "
        "next bracket on the line, the }, so \"_d% deletes , { timeout: 0, retries: 99 } into the black "
        "hole. jp puts the close call below render(rows). A plain d% goes into \"1 (it's one of the "
        "motions that always do), so the cut line would be in \"2: ddf,d%j\"2p ties."),
    "blackhole-18": ('dd"_4xj.p',
        "dd cuts print(total), and the cursor lands at the start of the first prompt. \"_4x deletes >>> "
        "and its space into the black hole, and j. repeats it on the next line, register and all. p puts "
        "the print below. dd 4x j. \"1p ties: x never touches \"1. A Visual block delete takes 2 keys "
        "more."),
    "blackhole-19": ('dd"_di(jp',
        "dd cuts run(). di( finds the parentheses on the line even with the cursor in column 1, so \"_di( "
        "empties them without touching the unnamed register. jp puts run() below configure(app). "
        "dddi(j\"1p ties, and so does emptying the call first (jdi(kddjp)."),
    "blackhole-20": ('ddw*"_ciwsubtotal<Esc>n.n.Gp',
        "dd cuts the return, and w moves to sum. * jumps to its next use, and \"_ciwsubtotal renames it "
        "without touching the unnamed register. n. renames the third one, and n. once more wraps around "
        "to the first: . remembers the black hole too. Gp puts the return at the end. A plain ciw and "
        "G\"1p ties, and so does moving the return first (ddGp, then gg and the renames)."),
    # ---------- Ctrl-r ----------
    "ctrl-r-1": ('yiwoprint(<C-r>")',
        "yiw yanks total_revenue. o opens a new line, and after print( Ctrl-r \" types the yank. The ) "
        "finishes it. Pasting with p instead means leaving Insert mode and coming back for the ) (14 keys)."),
    "ctrl-r-2": ('y$j$i`<C-r>"`',
        "y$ yanks the whole command. j$ goes to the period on line 2, and i inserts before it: a backtick, "
        "Ctrl-r \" for the command, and the closing backtick, all without leaving Insert mode."),
    "ctrl-r-3": ("yiwjf)i=<C-r>0, timeout=30",
        "yiw yanks DEFAULT_PORT. jf) lands on the closing parenthesis of line 2, and i inserts before it: "
        "=, Ctrl-r 0 for the name (Ctrl-r \" is the same here), then , timeout=30. Leaving Insert mode to "
        "paste with p and coming back costs one key more."),
    "ctrl-r-4": ("ciwmax_items<Esc>A  # was <C-r>-",
        "ciw deletes limit, which goes into both \"\" and \"- (it's a small delete), and you type max_items. "
        "A appends at the end of the line, and Ctrl-r - types the deleted name back into the comment. "
        "Ctrl-r \" works the same. Typing limit again takes 3 more keys, and yanking it first takes 3 more "
        "too."),
    "ctrl-r-5": ("wCTerminal Garden<Esc>jF]i<C-r>.",
        "wC changes TITLE to the end of the line, and you type Terminal Garden. jF] goes back to the ] on "
        "line 2, and i plus Ctrl-r . types what you just typed. . would repeat the whole C, not just the "
        "text, so it can't do this. \".P in Normal mode is the same length."),
    "ctrl-r-6": ("2wyiwjfbciwaccount.<C-r>0()",
        "2wyiw yanks getBalance. jfb lands on balance in line 2. ciw deletes it, which fills \"\" with "
        "balance, so after typing account., Ctrl-r 0 is the one that types getBalance. () finishes the "
        "call. Visual p and typing around it takes 26 keys or more."),
    "ctrl-r-7": ('Wy$:%s/TBD/<C-r>"/<CR>',
        "W jumps to ask and y$ yanks the default. On the command line, Ctrl-r \" types it as the "
        "replacement, so the command is :%s/TBD/ask in #garden-ops/. Each line has one TBD, so no g is "
        "needed. Changing each TBD with ciw and Ctrl-r 0 plus . takes 17 keys. Ctrl-r Ctrl-a (a later drill "
        "in this project) can't help here, because the text has spaces."),
    "ctrl-r-8": ('yitF>i id="<C-r>""',
        "yit yanks pricing and moves the cursor to its start. F> goes back to the > of <h2>, and i "
        "inserts before it: a space, id=\", Ctrl-r \" for the yank, and the closing quote. Typing pricing "
        "would cost 2 keys more."),
    "ctrl-r-9": ('yiwomkdir -p "$<C-r>"" && cd "$<C-r>""',
        "yiw yanks BACKUP_DIR, and o opens the new line. Each \"$ is followed by Ctrl-r \" (the register "
        "name is the \" key) and then a closing quote you type. A register can be inserted as often as "
        "you like. Typing the whole line takes 43 keys."),
    "ctrl-r-10": ('4wyiwoprintf("<C-r>"=%d\\n", cfg.<C-r>");',
        "4w reaches max_connections and yiw yanks it. o opens the new line, and the printf is typed with "
        "Ctrl-r \" in both places the name goes. Each Ctrl-r saves 13 keys over typing the name."),
    "ctrl-r-11": ('wyeoconsole.log("<C-r>"", <C-r>");',
        "w moves to sessionTimeoutMs and ye yanks it (from the start of a word, e is its end). o opens the "
        "new line, and Ctrl-r \" types the name inside the quotes and again as the value. Typing the whole "
        "line takes 51 keys."),
    "ctrl-r-12": ('yeGotrap <C-r>" EXIT',
        "ye yanks cleanup_temp_files from the start of line 1. G goes to the closing brace, o opens a line "
        "below it, and Ctrl-r \" types the name between trap and EXIT. Typing the name takes 14 keys more."),
    "ctrl-r-13": ('j$yiWolabels:<CR>app: <C-r>"',
        "j$ goes to the end of the name line, and yiW yanks payments-worker as one WORD (yiw would stop at "
        "the dash). o opens a line at the same indent; after labels:, Enter opens the next one two spaces "
        "deeper (YAML's indent rules see the colon), and Ctrl-r \" types the name after app: ."),
    "ctrl-r-14": ('wyeotype <C-r>"List = <C-r>"[];',
        "w moves to PaymentIntent and ye yanks it. o opens the new line, and Ctrl-r \" types the name twice: "
        "once with List typed after it, once with [] after it. Typing both names takes 18 keys more."),
    "ctrl-r-15": ('$byejothis.<C-r>" = <C-r>";',
        "$b lands on retryPolicy at the end of line 1, and ye yanks it. j goes to the constructor line, and "
        "o opens a line inside it, indented by Java's rules. this., Ctrl-r \", =, Ctrl-r \" and ; build the "
        "assignment. 2wye would yank RetryPolicy, the type, with its capital R."),
    "ctrl-r-16": ('Wyeo#define <C-r>"<Esc>Go<CR>#endif /* <C-r>" */',
        "W jumps to GARDEN_CONFIG_H (w would stop on ifndef, after the #), and ye yanks it. o opens line 2, "
        "where Ctrl-r \" types the name after #define. G and o<CR> open a blank line and the last line at "
        "the end, and Ctrl-r \" types the name again in the comment: the register keeps it until the next "
        "yank or delete. Copying the line with yyp and changing ifndef costs a key more."),
    "ctrl-r-17": ('O#include "<C-r>%<BS>h"',
        "O opens a line above line 1. Ctrl-r % types the file name, garden_sync.c, and Backspace deletes "
        "the c so you can type h and the closing quote. Typing the whole name takes 9 keys more."),
    "ctrl-r-18": ('2w"aye2wyeoCREATE INDEX <C-r>a_<C-r>"_idx ON <C-r>a (<C-r>");',
        "2w reaches order_items, and \"aye yanks it into register a. 2w steps over the ( to order_id, and ye "
        "yanks it the normal way. o opens the new line, and the index name is built from Ctrl-r a, _, "
        "Ctrl-r \" and _idx; the table and the column come back after ON. With only the unnamed register "
        "you'd have to type one of the names twice, or leave Insert mode to fetch it. The setup turns off "
        "SQL's indent rules, which would indent the line as you type."),
    "ctrl-r-19": ('6wDO<C-r>"<Esc>7wDO<C-r>"<Esc>7wDO<C-r>"',
        "6w reaches the first //, and D cuts the comment. O opens a line above the field, indented like it, "
        "and Ctrl-r \" types the comment there. From the end of that comment, 7w reaches the next // (2+; "
        "with an f/ is a key longer), and the same keys move it. . can't do the second one: it repeats only "
        "the last change, the O, not the D before it. O<Esc>p would put the comment in column 1: a new line "
        "that you leave empty loses its indent."),
    "ctrl-r-20": ('4wyej$i ?: <C-r>"<Esc>j.j.',
        "4w reaches DEFAULT_STATE_DIR (the * is a word of its own) and ye yanks it. j$ goes to the ; on "
        "line 2, and i inserts before it: ?:, a space, and Ctrl-r \". After <Esc> the cursor is on the R it "
        "just typed, past the end of the shorter next line, so j lands on that line's ;. . repeats the "
        "insert there, and j. does the last line."),
    # ---------- "A … "Z ----------
    "append-1": ('/AC<CR>"Addn.n.G"ap',
        "/AC finds the first ACTION line (the capitals make the search match case). \"Add cuts it onto the "
        "end of register a, which starts empty here. n finds the next one and . repeats the cut, still "
        "appending. G\"ap puts all three, in order, below the last line. Moving them one at a time takes 18 "
        "keys; Project 07's :g/ACTION/m$ is shorter still."),
    "append-2": ('"ayi"j"Ayi"j"Ayi"j"aP',
        "\"ayi\" yanks the base URL into register a, and each j\"Ayi\" appends the next string. All three are "
        "within a line, so they're joined with nothing in between. j lands on the second quote of line 4, "
        "and \"aP puts the whole URL before it. Copying the parts one by one takes 22 keys."),
    "append-3": ('fg"AdaWfD.jA <C-r>a',
        "fg lands on -g, and \"AdaW cuts it and the space after it onto register a. fD reaches -DDEBUG, and . "
        "repeats the appending cut, so register a holds \"-g -DDEBUG \". jA goes to the end of line 2, and "
        "after a space, Ctrl-r a types both flags. The trailing space doesn't count."),
    "append-4": ('/E<CR>"Ayyn"Ayyn"AyyG"ap',
        "/E<CR> finds the first ERROR line: the pattern has a capital, so smartcase makes it match case, "
        "and only ERROR has a capital E. \"Ayy appends the line to register a (empty in a drill; in your own "
        "Neovim, qaq first). A yank isn't a change, so . can't repeat it: n\"Ayy does each of the others. "
        "G\"ap puts all three below -- errors --. j\"Ayy2j\"Ayy2j\"Ayy ties here, but the search doesn't care "
        "how far apart the lines are."),
    "append-5": ('/(d<CR>"Adapn.G"ap',
        "/(d<CR> finds the first (deprecated) heading (searching for dep would also find ## Deprecated). "
        "\"Adap cuts the section and the blank line after it onto the end of register a, and n. does the "
        "same to the second one: . remembers the uppercase register, so it keeps appending. G goes to the "
        "blank line after ## Deprecated, and \"ap puts both sections there, in order."),
    "append-6": ('2j"ay)2j"Ay)G"Ay)ggA <C-r>a',
        "2j goes to the first paragraph, and \"ay) yanks up to the start of the next sentence, so the first "
        "sentence comes with the space after it. 2j\"Ay) and G\"Ay) append the first sentences of the other "
        "two paragraphs (G is the last line, a key shorter than 2j). The trailing spaces join the "
        "sentences. ggA appends a space to TL;DR:, and Ctrl-r a types all three. Fetching and pasting each "
        "sentence on its own means going back and forth three times."),
    # ---------- "1 … "9 ----------
    "numbered-1": ('jdd..."1p...',
        "jdd deletes the first DROP, and ... deletes the other three. Each delete pushes the earlier ones "
        "down, so orders is in \"1, carts in \"2, users in \"3 and accounts in \"4. The cursor is on the "
        "comment now, and \"1p puts orders below it. . after a numbered put uses the next number, so ... "
        "puts carts, users and accounts."),
    "numbered-2": ('jddddj."3p',
        "jdd cuts cleanup(), and dd deletes the first print, which lands the cursor on run(). j. deletes "
        "the second print. Three line deletes later, cleanup() is in register 3, and \"3p puts it below "
        "run(). Deleting the prints into the black hole (jdd\"_ddj.p) also takes 10 keys."),
    "numbered-3": (')d)wdwA <C-r>1',
        ") jumps to Each, and d) deletes up to the next sentence. That's within the line, but deletes with "
        "the ) motion always go into register 1 (and \"-). w moves to the first are, and dw deletes it, "
        "which replaces \"\" and \"-, but not \"1. A appends a space and Ctrl-r 1 types the sentence back. "
        "With Ctrl-r \" you'd get \"are \"."),
    "numbered-4": ('j"2pk"4P',
        "Four deletes ago is \"4: the most recent one, log.info(\"done\"), is in \"1, audit(event) in \"2, "
        "print(event) in \"3 and the metrics line in \"4. j goes to validate(event), and \"2p puts "
        "audit(event) below it. k goes back up, and \"4P puts the metrics line above validate. Browsing with "
        "\"1p and u. would find them too, but knowing the numbers is shorter."),
    "numbered-5": ('/xp<CR>ddn.n.2G"1P..',
        "/xp<CR> finds the first export (exec has no xp in it). dd deletes it, and n. twice deletes the "
        "other two, so GARDEN_PORT is in \"1, GARDEN_ENV in \"2 and GARDEN_HOME in \"3. 2G goes to the echo "
        "line. \"1P puts GARDEN_PORT above it, and each . puts the next older delete above the line it just "
        "put, so GARDEN_ENV and then GARDEN_HOME land on top, in the original order. (\"1p.. on the #! line "
        "would put them in reverse.) Cutting into \"A and putting once ties."),
    "numbered-6": ('jdd.j.."2p.',
        "jdd deletes the first print, and . deletes conn.close() right after it. j goes to log.flush(), . "
        "deletes it, and . deletes the second print. The cursor is on report(rows), and the history is: \"1 "
        "the second print, \"2 log.flush(), \"3 conn.close(). \"2p puts the flush below report, and . after a "
        "numbered put uses the next number, so it puts \"3, the close, below that. Keeping the two lines in "
        "named registers or sending the prints to the black hole costs more keys."),
    # ---------- "- ----------
    "small-delete-1": ('wdwjdd"-P',
        "w moves to final, and dw cuts it with its space: a small delete, so it's in \"- as well as \"\". "
        "jdd deletes the TODO, which replaces \"\" but leaves \"- alone, and keeps the cursor's column, on "
        "void. \"-P puts final before it. \"_dd and P, or putting first and deleting after, also take 9 "
        "keys."),
    "small-delete-2": ("$bciwMath.round(<C-r>-)<Esc>j$b.j$b.",
        "$b lands on price, and ciw deletes it into \"-. Type Math.round(, Ctrl-r - for the deleted word, "
        "and ). The magic is in the repeat: for Ctrl-r -, . reads the register again, so j$b. wraps "
        "shipping, not price. Ctrl-r \" looks the same the first time, but . would type price on every "
        "line."),
    "small-delete-3": ("wcwget_user<Esc>2jddo<CR><C-r>- = <C-r>.",
        "wcw renames the function. That fills \"\" and \"- with fetch_user, and \". with get_user. 2jdd "
        "deletes the comment, which replaces \"\" with the comment line, but \"- still holds fetch_user. o "
        "and <CR> open the new lines (Python's indent rules drop the indent after a return), and Ctrl-r - "
        "and Ctrl-r . type the two names. Adding the alias before deleting the comment takes 26 keys."),
    "small-delete-4": ("3wciwCOALESCE(<C-r>-, 0)<Esc>w.w.",
        "3w reaches discount, and ciw deletes it into \"-. Type COALESCE(, Ctrl-r - for the column, and , "
        "0). After <Esc> the cursor is on the ), and w jumps over ), to tax (the ) and the comma are one "
        "word). . repeats the change, and Ctrl-r - types what that ciw just deleted, tax, not discount. w. "
        "does shipping. With Ctrl-r \" the repeats would type discount every time."),
    "small-delete-5": ('f;dF jddf;"-P',
        "f; goes to the ; after !important, and dF<Space> deletes back to the space before it (F doesn't "
        "take the cursor's character), so \" !important\" is cut into \"- and \"\". jdd deletes the comment, "
        "which replaces \"\" but not \"-, and leaves the cursor on the .btn-primary line. f; reaches its ;, "
        "and \"-P puts the cut text before it. Deleting the comment first and using P ties."),
    "small-delete-6": ('WciW"<C-r>-"<Esc>W.j.}.',
        "W moves to $SRC_DIR/config.toml, and ciW changes the whole WORD: type a quote, Ctrl-r - (the "
        "argument you just deleted) and a quote. W. quotes $DEST_DIR/. After the change the cursor is on "
        "the closing quote, past the end of the shorter line 2, so j lands on its last character, inside "
        "$CACHE_DIR, and . quotes it. } goes to the end of the file (there's no blank line), inside the "
        "last argument, for the last . (j$. is a key longer). With Ctrl-r \" instead, every . would type "
        "$SRC_DIR/config.toml."),
    # ---------- Ctrl-r = ----------
    "expr-1": ("f2C<C-r>=<C-r>-<CR><Esc>jF=wC<C-r>=<C-r>-<CR>",
        "f2 lands on the formula, and C deletes it into \"- and starts Insert mode. Ctrl-r = opens the "
        "expression prompt, Ctrl-r - types the formula into it, and Enter inserts 26214400. jF=w reaches "
        "the second formula, and the same keys do it. Typing the numbers takes 24 keys, and you'd have to "
        "work them out first."),
    "expr-2": ("f0ciw<C-r>=<C-r>-<CR><Esc>f0ciw<C-r>=<C-r>-<CR>",
        "f0 lands on 0x1E90FF, and ciw deletes it into \"-. In the Ctrl-r = prompt, Ctrl-r - types it back, "
        "and Enter inserts 2003199: Vim reads 0x numbers as hex. The cursor ends on the last digit, so f0 "
        "skips the zeros behind it and finds the next hex number, and the same keys convert it. . can't help: it repeats the result, "
        "2003199, not the calculation."),
    "expr-3": ('wy$j$"=<C-r>0<CR>P',
        "wy$ yanks the formula. j$ goes to the ; on line 2. \"= starts a put from the expression register: "
        "Ctrl-r 0 types the formula at its prompt, Enter evaluates it, and P puts 86400000000000 before the "
        "cursor. In Insert mode, i<C-r>=<C-r>0<CR> is the same length."),
    "expr-4": ("ci[<C-r>=<C-r>-<CR><Esc>+ci[<C-r>=<C-r>-<CR>",
        "ci[ finds the brackets on line 1 from column 1, and deletes 1920 * 1080 * 4 into \"-. Ctrl-r = "
        "opens the prompt, Ctrl-r - types the formula, and Enter inserts 8294400. + goes to the start of "
        "line 2 and the same keys give 2073600. . can't help: it would repeat 8294400, not the calculation. "
        "Typing the two numbers takes 4 keys more."),
    "expr-5": ("9wC<C-r>=<C-r>-<CR><Esc>3wC<C-r>=<C-r>-<CR>",
        "9w lands on the 5 right after MAX_UPLOAD_BYTES= (the # . : and = are words of their own), and C "
        "deletes 50*1024*1024 into \"-. Ctrl-r = and Ctrl-r - type it into the prompt, and Enter inserts "
        "52428800. From its last digit, 3w reaches the 7 on the next line, and the same keys give 604800. "
        "f=l to get past each = is a key or two longer."),
    "expr-6": ("f(C<C-r>=<C-r>-<CR>  /* <C-r>- */<Esc>+;C<C-r>=<C-r>-<CR>  /* <C-r>- */",
        "f( goes to the formula and C deletes it into \"-. Ctrl-r = Ctrl-r - <CR> inserts its value, "
        "67108864. The register still holds the formula, so after typing two spaces and /*, a plain Ctrl-r "
        "- types it again as text. + goes to the next line and ; repeats the f(, and the same keys do "
        "LOG_BYTES. Typing the numbers instead takes 3 or 4 keys more per line."),
    # ---------- ". "% ": "/ ----------
    "readonly-1": ('Gf3l"%p',
        "G goes to the last line, f3 to the 3 of python3, and l onto the first of the two spaces. \"%p "
        "puts the file name after it. In Insert mode, Ctrl-r % does the same."),
    "readonly-2": ('j2WciWmath.pi<Esc>2jF*h".P',
        "j2W lands on 3.14, and ciW replaces it with math.pi, which also fills register . with math.pi. "
        "2j goes down to the circumference line (the cursor ends up past the gap), F*h steps back onto the "
        "second space of the gap, and \".P puts math.pi before it. . would repeat the ciW and swallow both "
        "spaces. i<C-r>. instead of \".P is the same length."),
    "readonly-3": ("Vj:center 40<CR>3jVj:<C-r>:<CR>",
        "Vj selects lines 1 and 2, and : in Visual mode types the range '<,'> for you, so :center 40 runs "
        "on them. The cursor is back on line 1, and 3jVj selects the credits. This time, after :, Ctrl-r : "
        "types the last command line, range included, so it reads :'<,'>'<,'>center 40. When a command "
        "gets more line numbers than it needs, Vim uses the last ones, so that works. Project 08's @: "
        "(Vj<Esc>@:) is a key shorter."),
    "readonly-4": ('}"%P',
        "} jumps to the next blank line, and there isn't one, so it goes to the end of the file: the "
        "closing quote of the empty string. \"%P puts the file name before it. Neovim opened the file as "
        ".github/workflows/lint.yml, so that's what register % holds. In Insert mode, Ctrl-r % does the "
        "same. G$ to get there is a key longer."),
    "readonly-5": ("Vj:center 30<CR>GA <C-r>:",
        "Vj selects the first two lines, and : types '<,'> for you, so center 30 runs on them. Register : "
        "now holds the whole command line, '<,'>center 30. GA appends to the last line, and after a space, "
        "Ctrl-r : types it. Typing '<,'>center 30 again takes 12 keys more."),
    "readonly-6": ("5wcwonComplete<Esc>oif (!<C-r>.) <C-r>. = noop;",
        "5w reaches cb, and cw renames it to onComplete, which also fills register . with onComplete. o "
        "opens the first line of the body, indented, and Ctrl-r . types the new name twice in it. You're "
        "inside a new insert, but . still holds the previous one until you leave Insert mode. Yanking the "
        "name and using Ctrl-r 0 takes 3 keys more, and typing it twice takes 16."),
    # ---------- Ctrl-r Ctrl-w ----------
    "ctrl-r-ctrl-w-1": ("w:%s/tries/<C-r><C-w><CR>",
        "w puts the cursor on maxAttempts. :%s/tries/ starts a substitute on every line, and Ctrl-r Ctrl-w "
        "types maxAttempts as the replacement. Each line has one tries, so no g is needed, and when there "
        "are no flags you can leave off the last /. Project 07 covers :s."),
    "ctrl-r-ctrl-w-2": ("2W:2,$s/<C-r><C-a>/timeout<CR>",
        "2W lands on config.timeout_seconds. :2,$s substitutes from line 2 to the end, leaving line 1 "
        "alone, and Ctrl-r Ctrl-a types the whole WORD as the pattern. (Its dot matches any character, "
        "which is fine here.) Typing the name instead would take 18 keys more."),
    "ctrl-r-ctrl-w-3": ("3W:%s/OWNER/<C-r><C-a><CR>",
        "3W lands on the address. :%s/OWNER/ and Ctrl-r Ctrl-a types help-desk@garden.dev as the "
        "replacement. Ctrl-r Ctrl-w would only type help, because - ends a word. OWNER is all capitals, so "
        "smartcase makes the search match case and it can't hit other words."),
    "ctrl-r-ctrl-w-4": (":%!grep <C-r><C-a><CR>",
        ":%!grep runs every line through grep, which keeps the lines that match. The cursor is on "
        "req-7f3a91, and Ctrl-r Ctrl-a types the whole WORD, dash included (Ctrl-r Ctrl-w would stop at "
        "req). The other ids share most of their characters, so the shortest part of this one that's "
        "unique, f3a9, takes 2 keys more to type. Deleting the five other lines by hand takes more still."),
    "ctrl-r-ctrl-w-5": ("$bi<C-r>=<C-r><C-w><CR> /* <Esc>A */<Esc>4wi<C-r>=<C-r><C-w><CR> /* <Esc>A */",
        "$b goes to the start of 0x20000000. i inserts before it, and the Ctrl-r = prompt is a command "
        "line, so Ctrl-r Ctrl-w types the word under the cursor, the hex number, and Enter inserts its "
        "value, 536870912. Type /* and a space, and the old number is still there to become the comment: A "
        "*/ closes it. 4w reaches the next hex number, and the same keys convert it. ciw with Ctrl-r - in "
        "the prompt and again in the comment takes 2 keys more per line, and typing the decimals takes "
        "more."),
    "ctrl-r-ctrl-w-6": ("/<C-r><C-a><CR>d2f.n.n.n.",
        "The cursor is on this.state.count, and / followed by Ctrl-r Ctrl-a searches for that whole WORD "
        "(its dots match any character, which is fine here). * would search for \\<count\\>, which also finds "
        "{ count: and this.props.count. The search lands on the next one, d2f. deletes this.state. up to "
        "the second dot, and n. does the others; the last n wraps around to line 2. Going to each one by "
        "hand takes 18 keys."),
}
