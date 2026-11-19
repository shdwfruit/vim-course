"""Reference solutions for Project 07's drills (spoilers!). Each entry: drill -> (keys, explanation).

See one with:  python3 check.py drill subst --show 3      Watch it typed:  python3 check.py drill subst --watch 3
"""
SOLUTIONS = {
    # ---------- :s ----------
    "subst-1": (":s/-/_/g<CR>",
        ":s works on the cursor line. The pattern - and the replacement _ are single characters, and the g "
        "flag changes all five dashes instead of only the first. f-r_ and then ;. for each of the other "
        "four would take 12 keys."),
    "subst-2": (":%s/=/: <CR>",
        "% is the range \"every line\". Without the g flag, :s replaces only the first = on each line, so "
        "the ssl=true inside the URL survives. The closing / is optional when there are no flags, and the "
        "trailing space in the replacement is typed like any other character."),
    "subst-3": (":%s/'/\"/g<CR>",
        "Every line, every match: % in front, g at the end. ' and \" aren't special in a pattern, so no "
        "backslashes are needed."),
    "subst-4": ("*:%s//col/g<CR>",
        "* searches for the word under the cursor as a whole word, \\<c\\>, so it can't match the c in cols. "
        "An empty pattern in :s means the last search, so :%s//col/g replaces exactly what * found. The g "
        "flag matters: lines 2 and 3 have c more than once. Typing :%s/\\<c\\>/col/g instead is 4 keys "
        "longer."),
    "subst-5": (":%s/\\<get/fetch<CR>",
        "\\< matches only at the start of a word, so \\<get finds getName but not the get inside Widget or "
        "budget. Each line has one getter, so no g flag. :%s/\\.get/.fetch also works, one key longer, but "
        "an unescaped .get would match dget in Widget, because . matches any character."),
    "subst-6": (":%s#\"#\"lib/<CR>",
        "Any punctuation can separate the parts of :s, and with # the / in lib/ needs no backslash. The "
        "pattern \" matches the first quote on each line, the opening one, and only the project headers "
        "have quotes. With / as the separator it's :%s/\"/\"lib\\/, one key longer. :%s#\"#&lib/ is the "
        "same length: & is the matched quote."),
    "subst-7": (":%s/\\d\\+/&px/g<CR>",
        "\\d is a digit and \\+ means one or more, so \\d\\+ matches a whole number. In the replacement, & is "
        "the whole match, so &px puts the number back followed by px. g catches both numbers on the margin "
        "line. \\d\\> (a digit at the end of a word) would work too, at the same length."),
    "subst-8": (":%s/;$<CR>",
        "$ anchors the pattern to the end of the line, so the ; inside the string (followed by more text) "
        "doesn't match. With nothing after the pattern, the replacement is empty and the match is deleted: "
        ":%s/;$// does the same in two more keys."),
    "subst-9": (":s/:/\\r/g<CR>",
        "In the replacement, \\r breaks the line. The g flag splits at all six colons. In a pattern \\n "
        "matches a line break, but in a replacement it inserts a null byte, so \\r is the one to remember "
        "here. f:r<CR> then ;. for each colon also works, but takes 14 keys."),
    "subst-10": ("*:%s//config<CR>:%s/'/\"/g<CR>",
        "The cursor starts on c, so * searches for \\<c\\> (and moves on to the next c, which doesn't "
        "matter). :%s//config reuses that search; there's one c per line, so no g. The second :s switches "
        "the quotes, with g since most lines have several. :%s/\\<c\\>/config would be 4 keys longer than "
        "*:%s//config."),
    "subst-11": (":%s#\\\\#/#g<CR>",
        "In a pattern a backslash starts something special, so a literal one is \\\\. With # as the "
        "separator the / in the replacement needs no backslash: :%s/\\\\/\\//g is one key longer. \\W (any "
        "non-word character) is no shorter, and would also hit the [ ] = and :."),
    "subst-12": (":%s/ \\+/,/g<CR>",
        "\" \\+\" is one or more spaces, so each run of them becomes a single comma, however long it is, and "
        "g gets all four runs on each line. \"  *\" (two spaces and a star) is the same length. A single "
        "space and * would also match nothing at all, between any two characters, and put commas "
        "everywhere."),
    "subst-13": (":%s# //.*<CR>",
        "Every comment has a space before its //, and the URL's // doesn't, so \" //.*\" matches from that "
        "space to the end of the line, and the empty replacement deletes it. # as the separator saves "
        "escaping the slashes: :%s/ \\/\\/.*/ is two keys longer. \" /.*\" would cut line 4 at the division, "
        "and \"// .*\" (the space after the slashes instead) ties."),
    "subst-14": (":%s/\\w\\+/\"&\"<CR>",
        "On each line, the first match of \\w\\+ is the key, and \"&\" writes it back between quotes. Without "
        "g, the values that are words (shop, true) stay as they are, and the { and } lines have no match at "
        "all. \\w* would match the empty string before the indentation, and \\a\\+ would stop at the _ in "
        "dev_port."),
    "subst-15": (":%s/.*] <CR>",
        ".* is greedy: it takes as much of the line as it can while the rest of the pattern still matches, "
        "so \".*] \" runs to the last \"] \" on the line, the end of the tag. The tags have different widths, "
        "so a Visual block can't take them out. :%norm 2dW deletes the same two WORDs, two keys longer."),
    "subst-16": (":%s/ == / === /g<CR>",
        "With a space on each side, the pattern can't match inside === or !==: in those, the == is touching "
        "another = or a !. g gets the second == on lines 2 and 6. :%s/ ==\\ze /&=/g ties. Searching for "
        "\" == \" and fixing each one with a= and n. takes 21 keys for the seven of them."),
    "subst-17": (":%s/<lt>[^>]*>//g<CR>",
        "[^>] is any character except >, so <[^>]*> matches one tag, attributes and all, and can't run on "
        "past its >. The empty replacement deletes it, and g gets every tag on the line. The lazy "
        "<.\\{-}> (as few characters as possible) is the same length. The greedy <.*> would swallow "
        "everything from the first < to the last >."),
    "subst-18": (":%s/\\.//g<CR>:%s/,/.<CR>",
        "The dots go first: \\. is a literal dot, and g matters because 1.000.000 has three. Then the one "
        "comma on each line becomes a dot, so no g. The other way round, the decimal points would be "
        "deleted along with the thousands dots. :%s/\\.<CR> with g&g& for the second and third dots is a "
        "key longer than the g flag."),
    "subst-19": (":s/,/\\r<C-r><C-w>/g<CR>",
        "\\r breaks the line at each comma, and Ctrl-r Ctrl-w types the word under the cursor, import, "
        "right after the break. The space that followed each comma is still there, so the new lines read "
        "import sys and so on. Typing :s/,/\\rimport/g is four keys longer, and replacing \", \" with "
        "\"\\rimport \" longer still."),
    "subst-20": ("*:%s//config.&/g<CR>",
        "* searches for \\<BASE_URL\\>, and _ is a word character, so ADMIN_BASE_URL doesn't match. The "
        "empty pattern reuses that search, and & puts the matched BASE_URL back after config.; the last "
        "line has two, hence g. :%s/\\<B/config.&/g also works (every word starting with a capital B is a "
        "BASE_URL), two keys longer."),

    # ---------- ranges ----------
    "range-1": (":2,4s/int/long/g<CR>",
        "2,4 is lines 2 to 4, and the g flag gets all three ints on each line. Lines 1, 5 and 6 are outside "
        "the range, so sign() and Integer keep their int. 4k3:s/int/long/g is a tie: go up to line 2, and "
        "let a count of 3 type :.,.+2 for you."),
    "range-2": ("4:s/'/\"/g<CR>",
        "From line 1, 4: types :.,.+3 for you: the def line and the three below it. The def line has no "
        "quotes, but a :s with a range just skips lines where the pattern doesn't match (it complains only "
        "if no line matches). :%s would also change legacy_greet()."),
    "range-3": (":,$s/\\./'/g<CR>",
        ".,$ is from the cursor line to the last one, and the . can be left out. The pattern needs \\. "
        "because a bare . matches any character, spaces included. Ten lines is where this starts to pay off: "
        "10:s/\\./'/g and VG:s/\\./'/g (select to the end, then :) are the same length, and on a shorter "
        "stretch a count before : is shorter."),
    "range-4": ("vi{:s/'/\"/g<CR>",
        "vi{ selects the lines inside the braces, and : in Visual mode types :'<,'> for you. The command "
        "then runs on just those lines. A count works too (3k5:s/'/\"/g, the same length), but vi{ needs "
        "no counting, which helps most when the block is long."),
    "range-5": (":2,4t.<CR>",
        ":t copies lines (it's short for :copy). 2,4 is what to copy and . says where: below the cursor "
        "line. The cursor never moves, so there's no going there and coming back: 2Gy2j''p does the same "
        "in 8 keys."),
    "range-6": (":5,7m1<CR>",
        ":m moves lines. Lines 5 to 7 are the blank line, ## Install and its command, and m1 puts them "
        "just below line 1. Moving the blank line along with the section keeps every section separated. "
        "5Gdap''p does it in 8 keys."),
    "range-7": (":3,6norm f r(A)<CR>",
        ":3,6norm runs the keys on lines 3 to 6, starting at the beginning of each: f<Space> finds the first "
        "space, r( replaces it, and A) appends. :normal ends Insert mode by itself. jj4:norm f r(A) ties, "
        "and so does a macro recorded on line 3 and played three more times."),
    "range-8": ("4:sor<CR>",
        ":sort with no range sorts the whole file, so it needs one here. From line 1, 4: makes it "
        ":.,.+3, the four imports. :sor is the shortest form of :sort. vip:sor and !ipsort<CR> work too, "
        "two keys longer."),
    "range-9": ("vip:norm I- <CR>",
        "vip selects the paragraph around the cursor, lines 3 to 7, and : turns that into :'<,'>. :norm I- "
        "inserts \"- \" before the first non-blank of each line, so the indentation stays in front. "
        "{j5:norm I- ties. A count that took in the blank line above would give it a stray \"- \"."),
    "range-10": ("3:s/\\./->/g<CR>9j3&",
        "3: covers lines 1 to 3, and :s/\\./->/g changes every dot there (line 1 has none, which is fine). "
        "The cursor ends on line 3. 9j goes to line 12, where respawn() starts, and 3& repeats the last "
        ":s, flags included, on that line and the next two: a count before & works like a count before :. "
        "reset_copy() in the middle has the very same lines, so no :g pattern could tell them apart."),
    "range-11": ("vi{:s/o/@/g<CR>",
        "vi{ selects the eleven rows inside tree[]'s braces (the lines with the braces themselves stay out, "
        "since each brace ends or starts its line), and : makes that :'<,'>. g gets the rows with two "
        "lights. Counting instead, 5k11:s/o/@/g, is a key longer. No short pattern tells the tree's o from "
        "the owl's and the snowman's: :g/\\^/s/o/@/g, on the lines with a ^, takes 14."),
    "range-12": (":8,$s/prod/staging<CR>",
        "8,$ is from line 8 to the last line, the four staging hosts. Each line has one prod, so no g. "
        "}:,$s/prod/staging ties: } jumps to the blank line above staging, and ,$ runs from there to the "
        "end (the blank line and staging: have no prod, so they're skipped)."),
    "range-13": ("3:m0<CR>",
        "3: becomes :.,.+2, the three URGENT lines, and m0 moves them, in order, above line 1. d2j{P ties: "
        "delete the three lines, { goes up to line 1 (there's no blank line on the way), and P puts them "
        "above it."),
    "range-14": ("5k4:s/:/s:<CR>",
        "The relative number of line 4 is 5, so 5k gets there and 4: covers lines 4 to 7. On each of them "
        "the first colon is the one in http:, so :s/:/s: turns it into https:. :4,7s/:/s: ties, and "
        ":s/p:/ps: reads better at two keys more."),
    "range-15": (":2,$sor<CR>",
        "2,$ is everything but the header. j:,$sor, jVG:sor and j!Gsort all tie at 8 keys. A plain :sor "
        "would put name after margaret, and :sor n keeps the header on top (a line without a number sorts "
        "first) but sorts the users by the year they joined."),
    "range-16": ("yGGp4:s/dev/test<CR>",
        "yG yanks the whole block from line 1, G goes to its last line, and p puts the copy below it, with "
        "the cursor on the copy's first line. From there 4: is exactly the copy, so :s changes only it; each "
        "line has one dev. :%t$ copies the block in 5 keys, but leaves the cursor on the last line, so "
        "the count needs a 3k first."),
    "range-17": ("5:s/'NULL'/NULL/g<CR>",
        "From line 1, 5: covers the first INSERT, header line included (it has no 'NULL', so it's skipped). "
        "The quotes are part of the pattern and not of the replacement, so they go. Lines 2 and 4 have two "
        "each, hence g. With % the name on the last line would lose its quotes too."),
    "range-18": ("vi{:g#//#d<CR>",
        ":g takes a range like any Ex command. vi{ selects the lines inside the braces, : makes it "
        ":'<,'>g, and #//# matches the commented lines (# as the separator, so the slashes need no "
        "backslash). A single / would also hit ./public. Counting the twelve lines takes a key more, and "
        "no pattern alone works: the TODO in load() is an indented comment too."),
    "range-19": ("j4:s/\\a\\+/'&'/g<CR>",
        "j goes to the first row and 4: covers the four rows. \\a\\+ is a run of letters, so it finds the "
        "city and the country but not the numbers, and '&' puts each one back between quotes; g does both "
        "on each line. :2,5s is a key longer than j4:, and \\w\\+ would quote the numbers too."),
    "range-20": ("4G5:sor<CR>5:s/*/-<CR>",
        "4G goes to the first entry and 5: makes :sort work on the five entries only. :sort leaves the "
        "cursor on the first line it sorted, so the same 5: is the right range again for :s. A * at the "
        "start of a pattern is a literal star. 3j ties with 4G. Doing :s first leaves the cursor on line 8, "
        "and vip:sor from there takes two keys more."),

    # ---------- :g ----------
    "global-1": (":g/pdb/d<CR>",
        ":g/pdb/ marks every line containing pdb, the import included, and d deletes each of them. pdb is "
        "already the shortest pattern that works: pd is in update and db is in db.save."),
    "global-2": (":g/^#/d<CR>",
        "^ anchors the pattern to the start of the line, so the colors, whose # comes later, survive. "
        ":g/# /d also works here at the same length, since every comment has a space after its #."),
    "global-3": (":g/ada/s/ ]/x]<CR>",
        ":g/ada/ picks Ada's lines and runs :s on each. The pattern \" ]\" is the space inside the "
        "brackets plus the ] after it (] alone isn't special), so it can't hit the space after the dash. "
        "Without :g you'd need :%s/ \\ze].*ada/x, which is longer."),
    "global-4": (":g/rai/norm f,xr(A)<CR>",
        "On each matching line, :norm starts at column 1: f, finds the comma, x deletes it, r( turns the "
        "space into (, and A) appends. rai is as short as a pattern gets that only matches the raise lines; "
        ":g/raise/ reads better and costs 2 more keys. A macro (/rai<CR>, record f,xr(A)<Esc>n, play it "
        "twice) ties."),
    "global-5": (":g/^/m0<CR>",
        "^ matches every line. :g goes from the top down, and each line in turn moves to the top, above "
        "the ones moved before it, so the order comes out reversed. :sort! would sort by hash instead, "
        "which isn't the same order."),
    "global-6": (":g/TODO/t$<CR>",
        "Every TODO line is copied to the end in turn. :g marks the lines before it starts copying, so the "
        "copies (which also contain TODO) aren't copied again, and they keep their order. Nothing shorter "
        "than TODO picks out exactly these lines: TODAY, ODOO and UNDO see to that."),
    "global-7": (":g/^x/m$<CR>",
        "^x matches lines that start with x (fix has an x too, but not at the start). Each one moves to "
        "the end in turn, and since :g goes from the top down, they keep their order."),
    "global-8": (":g/fd/,/#/d<CR>",
        "fd only appears in #ifdef. For each #ifdef line, ,/#/ is the range from that line to the next "
        "line containing a #, which is its #endif, and d deletes the whole block. The blocks are 3 and 4 "
        "lines long, so a fixed count wouldn't do. :g/#ifdef/,/#endif/d says the same thing in full."),
    "global-9": (":g/^/t.<CR>",
        "t. copies a line to just below itself. :g only visits the lines it marked at the start, so the "
        "new copies aren't copied again."),
    "global-10": ("4:g/^/m7<CR>",
        "4: gives :g the range :.,.+3, lines 8 to 11. Each line in turn moves to just below line 7, above "
        "the ones moved before it, which reverses the block. :8,11g/^/m7 is the same command without "
        "the count, 3 keys longer."),
    "global-11": (":g/<lt>!/d<CR>",
        "Every comment starts with <!, and nothing else has those two characters together: a bare < is "
        "in <kbd>, a - is in dependency-free and the list, a ! is in Fast!. :g/!-/d and :g/->/d tie."),
    "global-12": (":g/:/j<CR>",
        ":j joins a line with the next one, with one space in between, as J does. :g marks every line with "
        "a colon, the URL included, but by the time it gets to the URL, the URL has already been joined "
        "onto Web: and is gone, so it's skipped. :g/:$/j says \"ends with a colon\" exactly, one key "
        "longer, and :%norm J takes 9."),
    "global-13": (":g/=/m+<CR>",
        "Moving every comment up one is the same as moving every setting down one: :m+ puts a line below "
        "the next one, so each setting lands below its comment. Only the settings have an =. The direct "
        "way, :g/^#/m-2, takes 10 keys; it needs the ^ because of the # in the color."),
    "global-14": (":g/{/-j<CR>",
        "On every line with a {, :-j joins the line above with it: - is the range (one line up), and :j "
        "joins it with the next line, dropping the indentation and putting one space in between. :g marks "
        "the lines first, so the joins don't confuse it. :%s/\\n *{/ { does the same in 13 keys."),
    "global-15": (":g/>/-,d<CR>",
        "Only the timing lines have a >, and -,d deletes the line above (the cue number) through the "
        "timing line itself: - is .-1, and the . after the comma can be left out. :g/:/-,d ties. "
        ":g/^\\d/d would also delete \"3 days from the coast.\", and :v/\\a/d the blank lines."),
    "global-16": (":g/@/,+5d<CR>",
        ",+5 is the matching line and the five after it: the decorator, the three lines of the function "
        "and the two blank lines. Only the skipped tests have a decorator, so @ is enough of a pattern; "
        ":g/skip/,+5d reads better and takes 3 more keys. The blocks are all the same length, so a fixed "
        "count works."),
    "global-17": (":g/pr/norm gcc<CR>",
        "gcc comments a line with Lua's --, and :normal uses mappings, so it works inside :g. pr is the "
        "shortest pattern only the print lines have; :g/print/ reads better at 3 keys more. Searching for "
        "pr, gcc, then n. for each of the others goes wrong: after gcc, n finds the same print again, "
        "now three columns to the right, and . uncomments it."),
    "global-18": (":g/en/t.|s//fr<CR>",
        "| puts a second command in :g's command, and both run on each en line: :t. copies it below "
        "itself and leaves the cursor on the copy, and :s changes the copy. :g sets the search pattern, "
        "so :s// means en again, and the first en on the line is the key (\"Good evening\" has one later "
        "on). Nothing else has an en."),
    "global-19": (":g/O:/t$|s/.*: /- [ ] <CR>",
        "On each TODO line, :t$ copies it to the end, below the earlier copies, so they stay in order, and "
        ":s on the copy replaces everything up to the last \": \" (.* is greedy) with \"- [ ] \". With a "
        "capital in it, smartcase makes O: match case exactly, and only TODO: has it: TODAY and DONE rule "
        "out the shorter ones. :g/TODO/ reads better at 2 more keys."),
    "global-20": (":g/(/t4|norm 0cwDROP<C-v><Esc>t(C;<CR>",
        "Only the CREATE lines have a (. Each one in turn is copied to just below line 4, above the copies "
        "before it, so they come out in reverse. :normal then fixes the copy: 0 goes to the start (the "
        "cursor keeps the column it had after the last copy), cw changes CREATE to DROP, Ctrl-v <Esc> "
        "ends that insert, t( stops just before the (, and C; replaces the column list with a semicolon."),

    # ---------- :normal ----------
    "normal-1": (":%norm ~w~<CR>",
        ":%norm runs ~w~ on every line from its first column: ~ capitalizes the first letter (and steps "
        "right), w jumps to the last name, and ~ capitalizes it. On the blank line ~ fails and :normal "
        "moves on. A macro would stop at the blank line and need a restart."),
    "normal-2": (":%norm f r(A)<CR>",
        "f<Space> finds the space after print, r( replaces it, and A) appends. :%norm covers every line, "
        "so the cursor starting on line 3 doesn't matter, and :normal leaves Insert mode for you. "
        ":%s/ \\(.*\\)/(\\1) does it in 3 more keys."),
    "normal-3": (":%norm 2WC[redacted]<CR>",
        "From column 1, 2W skips two WORDs (the time and the level), and C replaces the rest of the line. "
        "The levels have different lengths, so the messages don't line up for a Visual block. "
        ":%s/\\u \\zs.*/[redacted] is 3 keys longer."),
    "normal-4": (":%norm $5<C-v><C-a><CR>",
        "$ goes to the last character, the score's last digit, and 5 Ctrl-a adds 5 to the number there. "
        "On the command line Ctrl-a would insert something else, so Ctrl-v comes first to type it as a "
        "key. On the comment lines there's no number, Ctrl-a fails, and :normal goes on to the next line."),
    "normal-5": (":%norm ci\"***<CR>",
        "When the cursor is before the first quote, ci\" changes the first quoted string on the line, so "
        "it works from column 1. :normal ends the insert. The greedy :%s/\".*\"/\"***\" would swallow the "
        "comments too."),
    "normal-6": (":%norm dwf=a\"<C-v><Esc>A\"<CR>",
        "dw deletes export and its space. f= finds the =, a\" inserts a quote after it, and the Ctrl-v "
        "<Esc> (it shows as ^[) leaves Insert mode in the middle of the keys. A\" adds the closing quote; "
        "that insert needs no <Esc>. A macro (after { to get to line 1) ties."),
    "normal-7": (":%norm gcc<CR>",
        "gcc toggles one line: it comments a plain line and uncomments a commented one. gc on a whole "
        "range would comment every line (some aren't commented yet), but :%norm runs gcc on each line on "
        "its own. :normal uses mappings, which gcc needs; :normal! wouldn't find it. A macro (after { "
        "to get to line 1) ties."),
    "normal-8": (":%norm 2Wdf($x<CR>",
        "2W lands on str(, df( deletes through the first (, and $x deletes the last character, the "
        "matching ). :%s/str(\\|)$//g does both deletions in one :s, one key longer: \\| means \"or\"."),
    "normal-9": ("k4:norm ^xf'3s=<CR>",
        "k goes to line 2 and 4: makes the range lines 2 to 5. On each, ^ goes to the first non-blank "
        "(:normal starts in column 1, in the indentation), x deletes the opening quote, f' finds the "
        "closing one, and 3s= replaces the quote, colon and space with =. :2,5norm and vi(:norm work "
        "too, one key longer. A macro ties."),
    "normal-10": (":%norm f r,;r,a\"<C-v><Esc>A\"<CR>",
        "f<Space>r, turns the first space into a comma, and ; repeats the f to reach the second. a\" "
        "opens the quote, Ctrl-v <Esc> leaves Insert mode, and A\" closes it. A macro (after { to get to "
        "line 1) ties; :%s with three groups is far longer."),
    "normal-11": (":%norm dit<CR>",
        "In Neovim, dit finds the first tag on the line even from column 1, and deletes what's inside it. "
        "On the comment lines there's no tag, dit fails, and :normal goes on with the next line. A macro "
        "would stop at the first comment."),
    "normal-12": (":%norm gUe<CR>",
        "e goes to the end of the word, and _ is a word character while = isn't, so gUe uppercases the "
        "whole key and stops there. :%s/\\w*/\\U& is a key longer. A macro ({ to get to line 1, then "
        "qqgUejq4@q) ties."),
    "normal-13": (":%norm di[<CR>",
        "di[ deletes what's inside the brackets, and Neovim finds them from the start of the line. On the "
        "{ line it reaches the list on the next line, which is fine, and on the } line it fails. "
        ":%s/\\[.*]/[] is two keys longer. A macro ({ then qqdi[jq4@q) ties."),
    "normal-14": (":%norm f|g?$<CR>",
        "f| finds the bar and g?$ ROT13s from there to the end of the line; the bar and the spaces don't "
        "change. On the title and the blank lines f| fails, :normal moves on, and a macro would stop. "
        "$g?F| looks the same, but F| leaves out the last character."),
    "normal-15": (":%norm f_x~<CR>",
        "f_ finds the first underscore, the one in the name, x deletes it, and ~ switches the case of the "
        "letter that moved under the cursor. On let count there's no _, so the line is skipped, where a "
        "macro would stop. :%s/_\\(.\\)/\\u\\1 is four keys longer."),
    "normal-16": (":%norm 2f.<C-v><C-a><CR>",
        "2f. lands on the second dot, and Ctrl-a adds 1 to the first number after the cursor: the patch "
        "number. On the lines with fewer than two dots, 2f. fails and nothing happens. A Visual Ctrl-a "
        "would bump the first number on each line, the major version."),
    "normal-17": (":%norm 2f,gUe<CR>",
        "2f, lands on the comma before the code. A comma counts as a word of its own, so from it e jumps "
        "to the end of the code, and gUe uppercases both (a comma has no case). Dennis's line has only "
        "one comma, so 2f, fails there, and a macro would stop. :%s/,\\a\\a,/\\U& is a key longer."),
    "normal-18": (":%norm g~e<CR>",
        "g~ switches case over a motion, and e is the end of the first word, so tHE becomes The. "
        ":%s/\\a*/\\u\\L& (capitalize, the rest in lowercase) is three keys longer. A macro ({ then "
        "qqg~ejq3@q) ties."),
    "normal-19": (":%norm %xF=cf(from <C-v><Esc>0cwimport<CR>",
        "% jumps from the start of the line to the ) that matches the first (, and x deletes it. F= goes "
        "back to the =, and cf( changes \"= require(\" to \"from \". Ctrl-v <Esc> ends that insert, and "
        "0cwimport replaces const last, since an insert at the very end needs no <Esc>. On the blank line "
        "% fails, where a macro would stop. f) instead of % is a key longer."),
    "normal-20": (":%norm 2f:2<C-v><C-a>2;2<C-v><C-a><CR>",
        "2f: lands on the colon before the seconds of the first time, and 2 Ctrl-a adds 2 to the number "
        "after it, keeping its leading zero. 2; repeats the f: twice more, to the colon before the second "
        "time's seconds, and 2 Ctrl-a again. The cue numbers, the text and the blank lines have no colon, "
        "so 2f: fails there and they stay as they are."),

    # ---------- :t :m ----------
    "copy-move-1": (":m0<CR>",
        ":m moves the cursor line, and 0 is the address above line 1. ddggP does the same in 5 keys."),
    "copy-move-2": (":t0<CR>",
        ":t0 copies the cursor line above line 1. yy{P ties: with no blank line above, { goes straight to "
        "line 1."),
    "copy-move-3": (":2t.<CR>",
        ":2t. copies line 2 to below the cursor line, without the cursor going anywhere. With relative "
        "numbers on, :-5t. is the same, one key longer. 5kyy5jp takes 7."),
    "copy-move-4": (":t6<CR>",
        "With no range, :t copies the cursor line; 6 means below line 6, the blank line above def "
        "settings. yy3jp takes 5 keys."),
    "copy-move-5": (":m5<CR>",
        ":m5 moves the cursor line to just below line 5, make test. dd2jp takes 5 keys: after the dd, "
        "everything below has moved up one line."),
    "copy-move-6": (":2,4t$<CR>",
        "2,4 is the range to copy, and $ puts the copies after the last line. 2Gy2jGp is the same length."),
    "copy-move-7": (":6,9m1<CR>",
        "Lines 6 to 9 are main() and the blank line after it, and m1 puts them below line 1. 6Gdap''p "
        "takes 8 keys."),
    "copy-move-8": (":3t.<CR>f1cwd20f39",
        ":3t. copies line 3 to below the cursor line and leaves the cursor on the copy. f1 finds the 1 "
        "that starts the color, and cw replaces 1e66f5. Yanking line 3 and coming back to put it costs "
        "two more keys than :3t."),
    "copy-move-9": (":2m5<CR>:4m1<CR>",
        ":2m5 moves migrate below line 5. Lines 3 to 5 shift up one, so the stop line is now line 4, and "
        ":4m1 moves it below line 1. Doing it in Normal mode takes 13 keys or so."),
    "copy-move-10": (":5t$|3t$|6t$<CR>",
        "| separates Ex commands on one command line, so this is three :t$ in a row: line 5 (yesterday), "
        "then line 3 (imagine), then line 6 (wonderwall), each copied after the last line, so they come "
        "out in that order. As three separate commands it's 15 keys."),
    "copy-move-11": (":6m0<CR>",
        "The 6 in front is the line to move, and 0 is above line 1, so the cursor never goes to line 6. "
        "5jddggP takes 7 keys, and { can't stand in for gg here, because of the blank lines on the way up."),
    "copy-move-12": (":3t-<CR>",
        "- on its own is the line above the cursor, so :3t- copies line 3 below line 7, which is just above "
        "the cursor line. :3t7 ties. Going up for it and coming back, 5kyyGP, takes 6."),
    "copy-move-13": (":-5t.<CR>",
        "-5 counts from the cursor: the line five up, which the relative numbers show. . puts the copy below "
        "the cursor line. :12t. is the same length, and 5kyy5jp takes 7."),
    "copy-move-14": (":$m3<CR>",
        "$ is the last line, so :$m3 moves import re below line 3, import json. Gdd3Gp does it in 6."),
    "copy-move-15": (":6,8t0<CR>",
        "6,8 is the three commands and t0 copies them above line 1. 6Gy2jggP takes 8, and so does "
        "5jy2j''P ('' jumps back to where 5j started)."),
    "copy-move-16": (":14m.|17m.<CR>",
        ":14m. moves email below the cursor line, and the cursor goes along to it, line 5. Moving a line up "
        "only renumbers the lines it passed, so createdAt is still line 17, and :17m. puts it below email. "
        "In Normal mode, 14Gdd''p twice (with 17G the second time) takes 16."),
    "copy-move-17": (":2t.|5t.<CR>",
        "After :2t. the cursor is on the copy of git pull, so :5t. puts systemctl restart shop below it, "
        "in order. The copies land below line 5, so line 5 is still line 5. Fetching each one in Normal mode "
        "and coming back takes 14."),
    "copy-move-18": (":6t.<CR>1010<C-a>",
        ":6t. copies the port line below the cursor line and leaves the cursor on the copy. Ctrl-a finds "
        "8080, the first number on the line, and adds the count, 1010. cw over the number and typing 9090 "
        "is three keys longer than the count."),
    "copy-move-19": (":m$|3m1<CR>",
        "With no line number, :m$ moves the cursor line, CMD, to the end. That leaves FROM, COPY, WORKDIR, "
        "RUN, CMD, so WORKDIR is line 3 now, and :3m1 puts it below FROM. ddGp, then 2kddkP, takes 10."),
    "copy-move-20": (":5m1|6m3|7m5<CR>",
        ":5m1 puts the first answer below the first question. That pushes the other questions down one, so "
        "the second answer, still line 6, goes below line 3, and the third, still line 7, below line 5. The "
        "last answer ends up after the last question by itself. Every move shifts the lines between, so no "
        "single :g pattern can do it, and in Normal mode it takes about 20 keys."),

    # ---------- :v ----------
    "vglobal-1": (":v/def/d<CR>",
        ":v runs d on every line that doesn't contain def, blank lines included, so only the three "
        "signatures are left. def is already the shortest pattern: debug, round and \"if area(r):\" rule "
        "out the shorter ones."),
    "vglobal-2": (":v/./d<CR>",
        ". matches any character, so the lines without a match are exactly the empty ones. :g/^$/d does "
        "the same in one more key. (Here :v/-/d would also do, at the same length.)"),
    "vglobal-3": (":v/=/m$<CR>",
        "Only the pinned lines contain an =. :v moves every other line to the end, from the top down, so "
        "flask, pytest and black keep their order. :g/=/m0 would move the pinned ones up instead, but in "
        "reverse order."),
    "vglobal-4": (":v/^#/d<CR>",
        "^# matches the lines that start with #, and :v deletes all the others, blank lines included. The ^ "
        "matters: issue #12 and (#31, #40) have a # further along. :g!/^#/d is the same command, a key "
        "longer."),
    "vglobal-5": (":v/./,/./-j<CR>",
        ":v/./ visits the empty lines. On each, ,/./- is the range from there to the line before the next "
        "non-empty one, and :j joins those blank lines into one. On a single blank line that range is one "
        "line, and :j on one line does nothing. The blank lines that got joined away are skipped. "
        ":%s/^\\n\\+/\\r does it in 13."),
    "vglobal-6": (":v/^#/s/^/# <CR>",
        ":v/^#/ runs the :s on every line that doesn't start with #, and :s/^/# / puts \"# \" in front (the "
        "closing / can go, even with a space before it). Without the ^ in the :v pattern, the echo line, "
        "with its comment at the end, would be skipped. :%s/^[^#]/# & is a key longer; gc on the whole "
        "file would comment the comments a second time."),

    # ---------- very magic ----------
    "very-magic-1": (":%s/\\v(\\d+), (\\d+)/\\2, \\1<CR>",
        "With \\v, (\\d+) is a group of one or more digits, no backslashes on ( ) or +. The replacement "
        "writes group 2, a comma and space, then group 1. Without \\v the pattern is "
        "\\(\\d\\+\\), \\(\\d\\+\\), four keys longer."),
    "very-magic-2": (":%s#\\v(..)/(..)/(\\d+)#\\3-\\2-\\1<CR>",
        "# is the separator, so the slashes in the date need no backslash. Day and month are always two "
        "characters, so (..) catches them; the year is (\\d+), which stops at the comma. \\3-\\2-\\1 puts "
        "them back in the other order. (\\d+) three times reads better and is two keys longer."),
    "very-magic-3": (":%s#\\v\\[(.*)]\\((.*)\\)#<a href=\"\\2\">\\1</a><CR>",
        "In very magic mode [ ( ) are special, so the literal ones get a backslash; a ] on its own is "
        "literal anyway. Group 1 is the link text and group 2 the url; there's one link per line, so the "
        "greedy .* is safe. # as the separator saves escaping the / in </a>. Here the plain-magic version "
        "\\[\\(.*\\)](\\(.*\\)) happens to be the same length: with many literal brackets, very magic stops "
        "paying off."),
    "very-magic-4": (":%s/\\v(.*): (.*)/\\2: \\1<CR>",
        "Each line has one \": \", so the greedy first group stops there and the second takes the rest, "
        "spaces and accents included. \\2: \\1 writes them back the other way round. Without \\v it's "
        "\\(.*\\): \\(.*\\), two keys longer."),
    "very-magic-5": (":%s/\\v,(...)(...)/,(\\1) \\2-<CR>",
        "The comma anchors the match at the start of the number; each (...) is three characters, the area "
        "code and the next three digits. The replacement puts the comma back, the area code in parentheses "
        "(plain text there) and a dash; the last four digits are outside the match and stay. Without \\v "
        "the groups cost two more keys. ,\\zs.../(&) and then a second :s for the dash takes 30."),
    "very-magic-6": (":%s/\\v(.*) - (.*) - (.*)/\\2 (\\3), by \\1<CR>",
        "Three groups around the two \" - \". Each line has exactly two, so the greedy groups can't run past "
        "them, and the commas in Gödel, Escher, Bach are no problem. The parentheses in the replacement are "
        "plain text in either mode. Without \\v the three groups need six backslashes, so that "
        "version is 4 keys longer, even counting the \\v."),

    # ---------- case in the replacement ----------
    "replace-case-1": (":%s/\\<./\\u&/g<CR>",
        "\\< is the start of a word, so \\<. is the first character of every word (# isn't a word "
        "character, so the heading marks are skipped). \\u& writes it back in uppercase. :%s/ \\a/\\U&/g "
        "ties: a space and a letter, uppercased (the space doesn't care)."),
    "replace-case-2": (":%s/\\v\"(.*)\"/\\U\\1\\e(&)<CR>",
        "Group 1 is the text between the quotes. \\U\\1\\e writes it in capitals, then \\e ends the "
        "uppercasing so the rest of the replacement is copied as is: ( and & (the whole match, \"red\") "
        "and ). Lines 1 and 6 have no quotes and are skipped."),
    "replace-case-3": (":%s/\\u/_\\l&/g<CR>",
        "In a pattern, \\u is any uppercase letter, and it ignores ignorecase. Each one is replaced with an "
        "underscore followed by the same letter in lowercase (\\l&). There are no capitals anywhere else, so "
        "nothing else changes."),
    "replace-case-4": (":%s/\\u\\u\\+/\\L&/g<CR>",
        "In a pattern \\u is an uppercase letter, whatever ignorecase says, so \\u\\u\\+ is a run of two or "
        "more: the keywords, but not the A of 'Ada'. \\L& writes the match in lowercase, and g gets every "
        "keyword on the line. \\u\\+\\> (capitals up to the end of a word) ties."),
    "replace-case-5": (":%s/\\w*/\\u\\L&/g<CR>",
        "\\L lowercases everything after it in the replacement, and the \\u before it still makes the first "
        "character uppercase, so each word comes out capitalized. \\w* can also match nothing, at the "
        "spaces, but an empty match is replaced with nothing, so it does no harm and saves the backslash of "
        "\\w\\+. guG and then :%s/\\<./\\u&/g takes 17."),
    "replace-case-6": (":%s/\\v(.*) (.*)/\\U\\2\\e, \\1<CR>",
        "The greedy first group runs to the last space, so group 2 is the last name even when there's a "
        "middle name. \\U\\2 writes it in capitals and \\e stops the uppercasing, so \", \" and the first "
        "names come out as they are. Without \\v it's two keys longer."),

    # ---------- \= ----------
    "expr-replace-1": (":%s/\\d\\+/\\=submatch(0)*60/g<CR>",
        "\\= makes the replacement an expression, evaluated for each number: submatch(0) is the matched "
        "text, and *60 turns it into a number and multiplies it. g gets both numbers on each line. Typing "
        "the eight new numbers by hand, or using Ctrl-a with a count for each, takes far more keys."),
    "expr-replace-2": (":%s/LINE/\\=line('.')<CR>",
        "line('.') is the number of the line being substituted, so each LINE becomes its own line number. "
        "By hand, /LINE then cw2<Esc>, n, cw4<Esc>... takes about 29 keys."),
    "expr-replace-3": (":%s/\\d\\+/\\=printf('0x%02X',submatch(0))/g<CR>",
        "printf() formats the matched number: %X is uppercase hexadecimal and %02X pads it to two digits, "
        "which matters for 10 (0x0A). The 0x is plain text in the format. submatch(0) is text, but printf "
        "converts it to a number for %X. msg[] has no digits, so it's left alone."),
    "expr-replace-4": (":%s/\\d.*/\\=eval(submatch(0))<CR>",
        "\\d.* runs from the first digit to the end of the line, the whole expression, since the names have "
        "no digits. eval() works out text as a Vim expression, so 60*60*24 becomes 86400, and a plain 3 "
        "stays 3. Working each one out with Ctrl-r = in Insert mode takes far more keys."),
    "expr-replace-5": (":%s/0x\\w*/\\=submatch(0)+0/g<CR>",
        "When Vim turns text into a number it reads 0x as hexadecimal, so submatch(0)+0 is the value, and "
        "the result is written in decimal. g gets the three flags. 0\\w* would also match the 080 in 8080 "
        "and turn the port into 880; the x keeps the pattern to the hex numbers."),
    "expr-replace-6": (":%s#\\d\\+F#\\=(submatch(0)-32)*5/9.'C'<CR>",
        "The expression has a /, so # separates the parts of :s. submatch(0) is 50F, and as a number that's "
        "50, so (50-32)*5/9 is 10, and . 'C' adds the unit. The arithmetic is whole numbers, which is why "
        "these temperatures come out even. \\S\\+F ties; ..F would cut 104F down to 04F."),

    # ---------- :sort ----------
    "sort-1": (":sor u<CR>",
        "u drops repeated lines after sorting. The order is by character code: * comes before ., and . "
        "before letters. The space before u is needed: :soru isn't a command."),
    "sort-2": (":sor!n<CR>",
        "n compares the first number on each line as a number, and ! reverses, so the biggest comes first. "
        "Without n, 940 would come before 5120, because 9 sorts after 5."),
    "sort-3": (":sor / /<CR>",
        "The pattern is a single space. :sort skips past the first match on each line and compares what's "
        "left, the last names. Lines where the pattern doesn't match would sort first, but every line has "
        "a space."),
    "sort-4": (":sor i<CR>",
        "i compares the lines as if they were all lowercase. Without it, every capital sorts before every "
        "lowercase letter, so Brewfile would come before bin. The dot sorts before the letters either way. "
        "!Gsort -f does the same through the shell, three keys longer."),
    "sort-5": (":sor /.*\\./<CR>",
        ":sort compares what comes after the match, and .*\\. is greedy, so it runs to the last dot: the "
        "keys are c, gz, h and md. Lines with the same key stay in their old order. :sor /\\./ would sort "
        "by what follows the first dot, so archive.tar.gz would go last, as tar.gz."),
    "sort-6": ("j5:sor n/#/<CR>",
        "j and 5: give :sort the five entries. With n and a /pattern/, it sorts by the first number after "
        "the match, the pull request number. Plain n would use the first number on the line, the 2 in "
        "\"fix 2 typos\". vip:sor n/#/ also works (the heading has no number, so it stays first), a key "
        "longer."),

    # ---------- & g& :&& ----------
    "amp-1": (":s/\\./*/g<CR>jj&jj&",
        ":s/\\./*/g stars row 1. & repeats the last substitute on the cursor line, and in Neovim it keeps "
        "the g flag, so jj& and jj& do rows 3 and 5 completely. The rows are identical, so no pattern "
        "could pick out just the odd ones."),
    "amp-2": (":%s/,/-<CR>g&",
        ":%s/,/- replaces the first comma on every line. g& runs the same substitute on every line again, "
        "and now the first comma is the one after the month. @: (repeat the last Ex command, Project 08) "
        "ties."),
    "amp-3": (":s/\\v\\((.*), (.*)\\)/(\\2, \\1)<CR>jj&jj&",
        "\\( and \\) are literal parentheses in very magic mode. The greedy (.*) runs to the last \", \" "
        "before the last ), so items.size() stays in one piece. After line 1, & repeats the substitute "
        "on lines 3 and 5. :%s/.../c with y n y n y would take 2 more keys, and a :g pattern that tells "
        "the wrong lines apart would be longer still."),
    "amp-4": (":%s/\\d\\zs\\d\\{3}\\>/,&<CR>g&g&",
        "\\d\\{3}\\> is the last three digits of a number, and \\d\\zs in front means there must be a digit "
        "before them, without making it part of the match. Each pass puts one comma before the last group "
        "that doesn't have one yet: 2147483647 needs three. g& repeats the substitute on every line; once "
        "a number is done, nothing matches in it. Doing it in one pass, with \\v\\d\\zs\\ze(\\d{3})+>, takes 28."),
    "amp-5": ("*:%s//accountId/g<CR>/uid<CR>g&",
        "* and :%s// rename userId. /uid then makes uid the last search pattern, and g& is :%s//~/&: the "
        "last search pattern, the last replacement, and the same g flag. :%s/userId\\|uid/accountId/g "
        "takes 28, and a second :%s/uid/~/g after the first one, 30."),
    "amp-6": (":%s/\\v<lt>(\\w+) \\1>/\\1/g<CR>g&",
        "(\\w+) \\1 is a word, a space, and the same word again; the < and > make them whole words, so \"the "
        "theory\" doesn't match. The first pass turns very very very into very very, since the third very "
        "is part of no pair any more, and g& makes it one. \\v<lt>(\\w+)( \\1>)+ gets runs of any length in "
        "one pass, one key longer."),

    # ---------- flags ----------
    "subst-flags-1": (":%s/max/best/gI<CR>",
        "With ignorecase and smartcase, the lowercase pattern max also matches MAX. The I flag makes this "
        ":s match case exactly, and g gets both maxes on line 4. :%s/\\Cmax/best/g is the same length."),
    "subst-flags-2": (":%s/,/;/gc<CR>yyna",
        "c asks about each comma in turn. On line 1: y, y, then n for the comma inside the quotes. Then a "
        "says yes to all the rest. :%s/,/;/g and fixing the quoted comma afterwards takes 17."),
    "subst-flags-3": ("*:%s//user_id/I<CR>",
        "* searches for \\<id\\>, but * always ignores case, so the search also finds ID. :s//user_id/ "
        "reuses that pattern, and I makes it case-sensitive again. Each line has one id, so no g. Typed "
        "out, :%s/\\<id\\>/user_id/I is 5 keys longer."),
    "subst-flags-4": ("g*:%s//work/gI<CR>",
        "g* searches for tmp without the word boundaries of *, so tmpfile matches too, and like * it "
        "ignores case, so TMPDIR would as well. The I flag makes this :s match case exactly. Typing "
        ":%s/tmp/work/gI is a key longer than g* and the empty pattern."),
    "subst-flags-5": (":%s/Vim/Neovim/gc<CR>ynyyna",
        "c asks about each Vim in turn: y for line 3, n for Bram on line 4, y and y for lines 5 and 6, n "
        "for the Amiga line, then a for all the rest. The two history lines share nothing a short pattern "
        "could find: :v/Br\\|Am/s/Vim/Neovim/g takes 25. Searching and repeating sNeov with . takes 27."),
    "subst-flags-6": ("*:%s//orderId/gc<CR>nynya",
        "* searches for \\<id\\>, ignoring case, so the first match is the ID in X-Request-ID: n. Then the "
        "parameter: y. On line 3 the key comes first, n, then the value, y, and a does the rest. "
        "*:%s//orderId/gcI with ynya ties: I skips the header for you. A pattern that leaves out the key, "
        ":%s/\\<id\\>:\\@!/orderId/gI, takes 26."),
}
