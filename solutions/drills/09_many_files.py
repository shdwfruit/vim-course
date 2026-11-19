"""Reference solutions for Project 09's drills (spoilers!). Each entry: drill -> (keys, explanation).

See one with:  python3 check.py drill edit --show 3      Watch it typed:  python3 check.py drill edit --watch 3
"""
SOLUTIONS = {
    # ---------- :e Ctrl-^ ----------
    "edit-1": (":e r<Tab><CR>jf.<C-a>",
        ":e r<Tab> completes requirements.txt, the only file starting with r, and Enter opens it. j goes down to "
        "the requests line, f. lands on the dot before 31, and Ctrl-a adds 1 to the first number after the cursor. "
        "From the start of the line, Ctrl-a would change the 2 instead. (:e r* also works: a pattern that matches "
        "just one file opens it.)"),
    "edit-2": (":e s<Tab>p<Tab><CR>5jdd",
        ":e s<Tab> completes the folder name src/, and p<Tab> completes parser.c inside it. The printf is on line "
        "6, five lines below where the file opens, so 5jdd deletes it (6Gdd is the same length). "
        ":e s<Tab><Tab><Tab> gets there too: the second Tab goes into src/ and shows lexer.c, the third parser.c."),
    "edit-3": (":e **/P<Tab><CR>2jf)iCents",
        "** stands for any number of folders, so **/P<Tab> completes the one file whose name starts with P, "
        "src/main/java/shop/model/Product.java. 2j goes to the record line, f) to the parenthesis after price, and "
        "i types Cents in front of it. Tabbing down one folder at a time would take many more keys."),
    "edit-4": (":e d<Tab><CR>3jyj<C-^>p",
        ":e d<Tab> opens dev.ini at its first line, 3j reaches log_format, and yj yanks it and the line below. "
        "Ctrl-^ returns to prod.ini with the cursor still on port = 80, and p puts the two lines under it. Once "
        "dev.ini is open, Ctrl-x Ctrl-l could also complete the lines one by one, but that takes at least a key more here."),
    "edit-5": (":e p<Tab><CR>5jyi\"<C-^>vep",
        "In pyproject.toml, 5j reaches the Documentation line, and yi\" yanks the text inside the first quotes on "
        "it, even though the cursor starts before them. Ctrl-^ returns to README.md with the cursor on TODO, ve "
        "selects the word, and p replaces it with the URL. ciw followed by Ctrl-r 0 also works, in two more keys "
        "(Ctrl-r \" would type TODO, because ciw just put it in the unnamed register)."),
    "edit-6": (":e t<Tab><CR>3jyap<C-^>P",
        ":e t<Tab> completes the first match, test_cart.py (cart sorts before checkout). 3j reaches def make_cart, "
        "and yap yanks the function with the two blank lines after it. Ctrl-^ returns to test_checkout.py, still "
        "on the def line, and P puts the lines above it."),
    "edit-7": ("eaing<Esc>:e p<Tab><CR>/n(<CR>.",
        "e moves to the n at the end of warn, and a appends ing. In parse.py, /n( lands on the n of warn, the "
        "first n( in the file, and . repeats the append there: the dot command doesn't care which file you're "
        "in. 8jt( reaches the same n in the same number of keys."),
    "edit-8": ("dd:e d<Tab><CR>GVp<C-^>p",
        "dd cuts the login line. In done.md, G goes to the dark mode line, V selects it, and p replaces it with "
        "the login line, putting the replaced line in the unnamed register. Ctrl-^ returns to todo.md, where the "
        "cursor is on the last line after the dd, and p puts dark mode below it. Gp then kdd also works, in two "
        "more keys."),
    "edit-9": ("}dap:e t<Tab><CR>p<C-^>dap:e d<Tab><CR>p",
        "} jumps to the first blank line, and dap from there deletes the two blank lines and slugify. In text.py, "
        "p puts them below the import. Ctrl-^ returns to utils.py, where the cursor is on the next pair of blank "
        "lines, so dap takes parse_date the same way, and p puts it in dates.py."),
    "edit-10": (":e S<Tab><CR>5jyy<C-^>P<C-^>2jy2j<C-^>jp",
        "In Square.java, 5j reaches the first @Override and yy yanks it. Ctrl-^ returns to Circle's area line, "
        "and P puts it above. The second Ctrl-^ goes back to Square, still on that @Override, so 2j reaches the "
        "blank line and y2j yanks it with the toString lines. The third Ctrl-^ lands on Circle's new @Override, "
        "and j then p put the block below area."),
    "edit-11": (":e c<Tab><Tab><CR>GA<C-w>false",
        "Two files start with c. The first Tab fills in config.dev.toml, the first in alphabetical order, and the "
        "second Tab moves on to config.prod.toml. G goes to the debug line, and A<C-w>false swaps the last word. "
        "Typing :e config.p<Tab> costs more than the second Tab."),
    "edit-12": ("yj:e b<Tab><CR>P:e d<Tab><CR>P",
        "yj yanks the #! line and the set line. The register keeps them from file to file, so in each empty "
        "script P puts them above its only, empty line, which is left at the end, where it doesn't count."),
    "edit-13": ("<C-^>3jfDcwWARN",
        "Ctrl-^ switches to the alternate file, config.h, in one key, with the cursor where you left it, on line "
        "1. 3j reaches the LOG_LEVEL line, fD the D of DEBUG, and cw changes the rest of the word. :e c<Tab><CR> "
        "would take five keys more."),
    "edit-14": ("*cwRETRY_LIMIT<Esc>:e c<Tab><CR>n.n.",
        "* searches for \\<MAX_RETRIES\\>; there's no other one in this file, so the cursor stays put. cw renames "
        "it. In client.py (the first match for c in alphabetical order) the search pattern and the last change "
        "are both still there: n finds each use and . renames it. A :%s there would cost more than n.n."),
    "edit-15": (":%s/cta/primary<CR>:e s<Tab><CR>g&",
        ":%s/cta/primary renames both classes in index.html (one per line, so no g). In style.css, @: would run "
        "the last command line again, and that's the :e. g& repeats the last substitute on every line instead, "
        "with the same flags. : and Ctrl-p twice to recall the :s is two keys more."),
    "edit-16": ("yG:e .e<Tab><Tab><CR>P:%s/=.*/=<CR>",
        "yG yanks every line from the cursor to the end. .env comes before .env.example, so it takes a second "
        "Tab. In the empty file P puts the lines above its empty line, and :%s/=.*/= removes everything after "
        "each =, keeping the = itself. Typing :e .env.<Tab> instead is two keys longer."),
    "edit-17": (":e s<Tab><CR>3jyy<C-^>3jP5j.",
        "In sync.py the @retry line is line 4: 3jyy yanks it. Ctrl-^ goes back to api.py at line 1, 3j reaches "
        "the first def, and P puts the line above it. That pushes the second def to line 9, five down, where . "
        "repeats the P. Once sync.py is open, O@<C-x><C-l> on each def completes the line from it too, in the "
        "same number of keys."),
    "edit-18": ("4j4dd:e d<Tab>i<Tab><CR>Vpx",
        "4j reaches ## Install, and 4dd cuts it with its blank line, the pip line and the blank line after it, "
        "which leaves README.md with one blank line before ## Usage. d<Tab> completes the docs/ folder and i<Tab> "
        "install.md in it. Vp replaces the TODO line with the four lines (the blank one at the end doesn't "
        "count), and x deletes one # of the heading, where p left the cursor."),
    "edit-19": (":e k<Tab><CR>G$yiW<C-^>2jWvep:e c<Tab><CR>Gf8yiw<C-^>jviwp",
        "In k8s.yaml the image is the last WORD of the last line: G$ gets there and yiW yanks it, slashes, colon "
        "and all. Ctrl-^ goes back to line 1 of the runbook, 2jW reaches the first TODO, and vep replaces it. In "
        "compose.yml, G and f8 reach the port, and yiw yanks just 8080. Ctrl-^ goes back to where you left the "
        "runbook, at the end of the image line, so j lands on the second TODO's last letter and viwp replaces it."),
    "edit-20": ("2jci\"1.5.0<Esc>:e a<Tab><Tab><CR>.:e C<Tab><CR>2jwcw<C-a>",
        "ci\" replaces the version inside its quotes, from anywhere on the line. a<Tab> completes the acme/ "
        "folder, and the second Tab goes into it, to its only file, __init__.py. There . repeats the ci\" on "
        "line 1. In CHANGELOG.md the heading isn't quoted, so cw changes Unreleased, and Ctrl-a types your last "
        "insert, 1.5.0, again. A :vimgrep for the old version would also find the 1.4.2 heading, which stays."),
    # ---------- :ls :b :bn :bp ----------
    "buffers-1": (":b v<CR>Gfhcwlist",
        ":b v switches to views.py. (v also appears in the folder name vim-course, so every buffer matches it "
        "somewhere; Neovim then takes the only name that starts with v.) G goes to the last line, keeping the "
        "first column, fh finds the h of home, and cw changes home to list. :e v<Tab><CR> is a key longer."),
    "buffers-2": ("dd:b c<CR>p",
        "dd cuts the line, and :b c switches to client.py, the only buffer whose name starts with c. In a buffer "
        "you haven't visited yet the cursor starts on line 1, so p puts the line right below import os."),
    "buffers-3": (":b au<CR>G$ciwFalse",
        ":b test matches three buffers, but au only appears in test_auth.py (th works too). G goes to the last "
        "line, $ to the e of True, and ciw replaces the word with False."),
    "buffers-4": (":b q<CR>Gk$x:b u<CR>4jf>r<lt>",
        ":b q finds queue.c, the only name with a q. Gk reaches the return line, $ the second ;, and x deletes it. "
        ":b u finds util.h: u is also in /Users, so every buffer matches somewhere, and Neovim falls back to the "
        "one name that starts with u. 4j reaches the MIN line, f> the >, and r< flips it."),
    "buffers-5": ("]bGf8r9]b/po<CR>xp",
        "]b goes to the next buffer in :ls order, 02-install.md. G reaches the last line, f8 the 8, and r9 "
        "replaces it. Another ]b goes to 03-usage.md, where /po lands on the p of stpo and xp swaps the two "
        "letters. :bn does the same as ]b in more keys."),
    "buffers-6": ("[b/xt<CR>ie<Esc>[b2j<C-x>",
        "From the first buffer, [b wraps around to the last one, Token.java (]B goes there too). /xt lands on the "
        "x of txt, and ie makes it text. Another [b goes back to Parser.java, where 2j reaches pos and Ctrl-x "
        "subtracts 1 from the next number on the line."),
    "buffers-7": ("A3<Esc>]b.]b.",
        "A3 appends to the first line of backup.py. ]b goes to cleanup.py with the cursor on line 1, and . "
        "appends the 3 there too; once more for report.py. :bufdo norm A3 does the same in 15 keys."),
    "buffers-8": (":ls<CR>5<C-^>t]rx",
        ":ls shows that 2024-03-06.md is buffer 5 (number 2 is the task window, which isn't listed). At the Press "
        "ENTER prompt, 5 Ctrl-^ switches straight to buffer 5, like :b5. t] stops on the space inside the "
        "brackets, and rx replaces it. :b 06 would go to buffer 6, a different note. :b 6. ties with this, and so "
        "does ]b three times, if you guess where the note is."),
    "buffers-9": ("{dap:b n<CR>Gp{dap<C-^>Gp",
        "{ goes up to the blank line above connect, and dap takes both blank lines and the function. In net.py, G "
        "and p put it at the end. The cursor is then on the first blank line you just put, and { goes up to the "
        "blank line above parse_args, so dap takes that function the same way. Ctrl-^ returns to cli.py, and Gp "
        "puts it at the end."),
    "buffers-10": (":b ca<CR>G-$x:b g<CR>G-cwboolean<Esc>:b st<CR>G-$i0",
        "ca appears only in Cart.java's path, g only in PaymentGateway's, and st only in StripeClient's. In each "
        "file, G goes to the closing brace and - to the first non-blank of the line above. Then $x deletes the "
        "extra ;, cw replaces void, and $i0 puts a 0 before the ;. StripeClient goes last, so its Esc is free."),
    "buffers-11": (":b pi<CR><C-a>",
        "Both index.ts buffers match index, but :b also checks the folders in each name, and only src/api/index.ts "
        "has pi in it (app has an a and a p, but not together). Ctrl-a adds 1 to the first number on line 1, the "
        "1 of v1."),
    "buffers-12": ("]bfsxp2]bfgxp",
        "]b goes to install.md, where fs and xp swap the s and the n. 2]b goes two buffers on, past config.md, "
        "to usage.md, where fg and xp swap the g and the a. Going the other way round with [b and counts is a "
        "key longer."),
    "buffers-13": (":b q<CR>2j$i NOT NULL",
        "No other buffer name has a q, so :b q finds schema.sql (the piece can come from the extension). 2j "
        "reaches the email line, and $i types in front of the comma. f,i instead of $i is a key longer."),
    "buffers-14": (":b it<CR>3jf(lcwlong<Esc>:b ro<CR>3j2f/is",
        "Every name contains Order, so pick two letters from the part after it: it is only in Repository, ro "
        "only in Controller. In OrderRepository, f(l reaches int and cw changes it. In OrderController, 2f/ "
        "reaches the slash after order, and is puts the s in front of it."),
    "buffers-15": (":b b/v<CR>Gf\"aweb/",
        "views matches both views.py buffers and web both web/ buffers, but b/v, the end of web, the slash and the "
        "start of views, matches only web/views.py. G goes to the render line, f\" to the opening quote, and a "
        "types web/ after it. :e w<Tab>v<Tab><CR> is a key longer."),
    "buffers-16": (":b db<CR>G180<C-a>:b ew<CR>G$hil<Esc>:b cl<CR>G$Fuxp",
        "db, ew and cl each appear in one path only (vi and ur would also match the folders the course is in). "
        "Each fix is on the last line: 180 Ctrl-a turns 20 into 200, in Normal mode, so no <Esc> is needed "
        "before the next :b; $hi types in front of the closing quote; $Fu finds the u of ture and xp swaps it "
        "with the r."),
    "buffers-17": ("A3<Esc>]b.2]b.]b.",
        "A3 fixes backup.py. ]b goes to cleanup.py, where the cursor starts on line 1, and . repeats the A3. 2]b "
        "skips report.py, which already ends in python3, and . fixes sync.py; ]b. does upload.py. :bufdo "
        "s/n$/n3/e would leave report.py alone too, but it's four keys longer."),
    "buffers-18": (":b a<CR>2jdd<C-^>p:b d<CR>4jdd<C-^>p",
        "a and d are in the folders around the course, so every buffer matches them somewhere, and :b falls back "
        "to the one name that starts with each: app.py, db.py. dd cuts each TODO line, and Ctrl-^ goes straight "
        "back to TODO.md, the buffer you came from, where p puts it below the cursor: the first one below the "
        "heading, the second below the first."),
    "buffers-19": ("Ofrom __future__ import annotations<Esc>:b sc<CR>.:b rv<CR>.",
        "O opens a line above line 1 for the import. schemas.py and services.py both start with s, so :b needs "
        "a piece only one of them has: sc and rv. In a buffer you haven't visited yet the cursor starts on line "
        "1, so . opens the same line there. Ctrl-x Ctrl-l in each would cost more than ."),
    "buffers-20": ("}dap:b t<CR>Gp<C-^>dap:b d<CR>Gp",
        "} goes to the blank lines above slugify, and dap takes them with the function. :b t and :b d go to the "
        "only names starting with t and d (both letters are in the folders around the course too). G and p put "
        "each function at the end. Ctrl-^ goes back to utils.py with the cursor where you left it, on the blank "
        "lines above parse_date, so dap takes that one the same way."),
    # ---------- Ctrl-w ----------
    "windows-1": ("fmxp<C-w>lG$i!",
        "fm lands on the m of nmae, and xp swaps it with the a. Ctrl-w l moves to the test on the right, G goes "
        "to the last line, $ to its closing quote, and i! types the ! before it."),
    "windows-2": ("yy<C-w>lP",
        "yy yanks the import, Ctrl-w l moves to api.py, where the cursor is on line 1, and P puts the line above "
        "it. In real life you'd make this layout yourself with :vs api.py."),
    "windows-3": ("<C-w>j}dap<C-w>kGp",
        "Ctrl-w j moves down to scratch.sql. } jumps to the blank line, and dap deletes it with the query below it. "
        "Ctrl-w k goes back up (Ctrl-w p would too), G goes to the last line, and p puts the blank line and the "
        "query after it."),
    "windows-4": ("y}<C-w>lp",
        "y} yanks up to the blank line. Because it starts at the beginning of a line and ends at the start of "
        "another, it takes whole lines: the four lines of the logo. Ctrl-w l moves to cli.py, and p puts them "
        "below the BANNER line."),
    "windows-5": ("jf_x<C-w>l/_<CR>.",
        "jf_ reaches the underscore in user_name, and x deletes it. Ctrl-w l moves to schema.sql, /_ finds its "
        "first underscore, in user_name, and . repeats the x. :windo %s/r_n/rn/ would work too, in more keys."),
    "windows-6": ("dd<C-w>lGVp<C-w>hP",
        "dd cuts ads.example.net. On the right, G goes to pypi.org, and Vp replaces that line with the cut one, "
        "putting pypi.org in the register. Ctrl-w h goes back, where the cursor is on the line that followed "
        "ads.example.net, and P puts pypi.org above it."),
    "windows-7": ("<C-w>lA/<Esc>jx<C-w>l0r\\jr<Space>",
        "Ctrl-w l moves to frame2.txt. A/ adds the raised arm at the end of line 1, and after Esc the cursor is on "
        "it, so j lands right on the old \\ and x deletes it. Another Ctrl-w l moves to frame3.txt, where the "
        "cursor starts on the o: 0r\\ puts the arm at the start of line 1, and j then r and a space blank out the "
        "/ below it. Ctrl-w w moves the same way here."),
    "windows-8": ("<C-w>lG$<C-w>jG$yiW<C-w>pP",
        "Ctrl-w l moves to test_app.py, and G$ puts the cursor on the closing quote. Ctrl-w j goes down to "
        "fixtures.yml, where G$ reaches the end of the address and yiW yanks the whole WORD. Ctrl-w p goes back to "
        "the window you came from, and P puts the address before the quote. From the bottom window, Ctrl-w k "
        "would go to whichever top window is above the cursor's column."),
    "windows-9": ("Gf1cE1.5.0<Esc><C-w>b.<C-w>h/U<CR>.",
        "Gf1 reaches 1.4.2 in the README, and cE changes it, to the end of the WORD. Ctrl-w b jumps to VERSION, "
        "bottom right, and . repeats the change on its 1.4.2. Ctrl-w h goes to CHANGELOG.md, /U finds Unreleased "
        "(a capital letter makes the search match case), and . changes that WORD too. Ctrl-w j from the README "
        "would go to whichever bottom window is below the cursor, which depends on your terminal's width."),
    "windows-10": ("<C-w>b2jdd<C-w>kjp<C-w>h4jf1cwS<C-n><C-n>",
        "Ctrl-w b goes to test_stack.c, bottom right, and 2jdd cuts the #define. Ctrl-w k goes up to stack.h, and "
        "jp puts it below #define STACK_H. Ctrl-w h goes back to stack.c, where 4jf1 reaches the 16 and cw "
        "starts replacing it. After a capital S, Ctrl-n offers only capitalized words from the open files: "
        "STACK_H first, STACK_CAP on the second press. Typing STACK_CAP in full takes six more keys."),
    "windows-11": ("/in<CR>cwsize_t<Esc><C-w>ln.",
        "/in skips the int at the very start of the line (the search starts after the cursor) and lands on int "
        "len. cw makes it size_t. The search pattern is shared by every window, so after Ctrl-w l, n finds the "
        "same int in buf.c, and . repeats the change. :windo s/int l/size_t l is seven keys longer."),
    "windows-12": ("*cwdebug<Esc><C-w>jn.n.n.",
        "* searches for the whole word verbose (the README has no other, so the cursor stays put), and cw changes "
        "it. Ctrl-w j goes down to cli.py, where each n finds the next verbose, the flag, args.verbose and the "
        "message, and . renames it."),
    "windows-13": ("GoLOG_LEVEL=info<Esc><C-w>lG.<C-w>lG.",
        "Go adds the line at the end of dev.env. Ctrl-w l moves one window right (Ctrl-w w does the same here), G "
        "goes to that file's last line, and . repeats the o with its text. :windo norm Go... is three keys longer, "
        "and it would complain in the task window."),
    "windows-14": ("<C-w>l3j$yiw<C-w>pvp",
        "In fixtures.json, 3j reaches the total line, $ the end of 4599, and yiw yanks it. Ctrl-w p goes back to "
        "the window you came from (Ctrl-w h ties), where the cursor is still on the 0: v selects that one "
        "character and p replaces it."),
    "windows-15": ("<C-w>l0<C-v>3j$y<C-w>hjP",
        "In a window that opens a file for the first time, the cursor starts on the first non-blank, so 0 goes to "
        "column 0 first. Ctrl-v 3j$ selects all four lines to their ends, and y yanks them as a block. In "
        "scene.txt, j goes to the house's second line, and P puts the block in front of it, one piece per line, "
        "each padded to the width of the widest so the house stays straight."),
    "windows-16": ("*<C-w>ln{yap<C-w>hGp",
        "* searches for formatPrice. The search is the same in every window, so in utils.js n jumps to the "
        "definition. { goes up to the blank line above it, and yap from a blank line takes the blank line with "
        "the paragraph after it. Back in app.js, Gp puts both at the end."),
    "windows-17": ("<C-w>byE<C-w>h2jwvEp<C-w>k2jf1vE\"0p",
        "Ctrl-w b goes to VERSION, bottom right, and yE yanks 2.0.0. Ctrl-w h goes to the changelog, 2jw reaches "
        "Unreleased, and vEp replaces it. That p put Unreleased into the unnamed register, but \"0 still holds "
        "the yank: Ctrl-w k goes up to the README, 2jf1 reaches 1.9.4, and vE\"0p replaces it. Doing the README "
        "first, with Ctrl-w p from VERSION and then Ctrl-w j, ties."),
    "windows-18": ("<C-w>lj$yiW<C-w>p$viwp<C-w>pj$yiW<C-w>pj$viwp",
        "In inventory.ini, j$ reaches the end of the host line and yiW yanks the address, dots included. Ctrl-w p "
        "goes back, and $viwp replaces TODO, a word on its own after the =. Each window keeps its cursor, so the "
        "second round trip is the same with a j in each window."),
    "windows-19": ("dd<C-w>jGP<C-w>kdd<C-w>bGP",
        "dd cuts the /login line, Ctrl-w j goes down to auth.py, and G then P puts it above the closing ]. Ctrl-w "
        "k goes back up to web.py, where the cursor is now on /v1/health: dd cuts it, and Ctrl-w b goes straight "
        "to the bottom window, api.py, two windows down, for the same GP."),
    "windows-20": ("<C-w>j:g/^fe/d A<CR>:%d<CR><C-w>k2j\"apGp:%s/^\\w*: /- /<CR>",
        "In commits.txt, :g/^fe/d A deletes every feat: line and appends each one to register a, in order. The "
        "fix: lines are all that's left, and :%d deletes them into the unnamed register (ggdG ties). Up in "
        "RELEASE.md, 2j\"ap puts the features below ## Added, and Gp the fixes below ## Fixed. Then one :s turns "
        "the word and colon at the start of each line into a dash; the headings start with #, which \\w doesn't "
        "match."),
    # ---------- gf ----------
    "gf-1": ("gf3j2<C-a>",
        "gf opens config.h, found in main.c's folder. 3j reaches the MAX_RETRIES line, and 2 Ctrl-a adds 2 to "
        "its number. :e c<Tab><CR> opens it too, in four more keys."),
    "gf-2": ("jddkwgfp",
        "jdd cuts the TAX_RATE line. k goes back to the import, and w puts the cursor on shop.cart, where gf "
        "opens shop/cart.py: the Python filetype plugin turns the dot into a slash and adds .py. The cursor "
        "starts on line 1 there, so p puts the line below the import. Cut first: gf can't take anything with it."),
    "gf-3": ("gfwcwon<Esc><C-^>4k512<C-a>",
        "gf opens conf.d/gzip.conf, w moves to off, and cw changes it to on. Ctrl-^ returns to the include line "
        "in nginx.conf (Ctrl-o would too, since you made no jumps in gzip.conf), 4k reaches worker_connections, "
        "and 512 Ctrl-a doubles the number. Editing nginx.conf first, then 4j and gf, takes the same keys."),
    "gf-4": ("fcgf/no<CR>cwunderline",
        "gf takes the file name under the cursor, so first fc puts the cursor on the c of css (stylesheet has no "
        "c). gf opens css/site.css, /no finds none (nothing on line 1 has no in it), and cw replaces it. :e with "
        "Tab completion would take four keys more than fcgf."),
    "gf-5": ("2jf82<C-a>f(lgf2jf8.",
        "2jf8 reaches the 8 of 3.8, and 2 Ctrl-a makes it 10. f(l puts the cursor on the link's path, and gf "
        "opens docs/setup.md. There 2jf8 finds the other 8, and . repeats the 2 Ctrl-a. Doing the setup guide "
        "first and coming back with Ctrl-^ is a key longer."),
    "gf-6": ("3Wgf363<C-a><C-^>WgffDcwINFO",
        "3W walks the SRC line to src/net.c, and gf opens it. 363 Ctrl-a adds 363 to the first number on the line: "
        "8080 becomes 8443. Ctrl-^ goes back to the Makefile with the cursor still on src/net.c, W moves to "
        "src/log.c, and gf opens that one, where fD and cw turn DEBUG into INFO. :e with Tab completion costs more "
        "than 3Wgf each time."),
    # ---------- :args :argdo ----------
    "argdo-1": (":argdo $d<CR>",
        ":argdo runs :$d in each of the three files: the range $ means the last line, and :d deletes it. "
        "README.md is in the buffer list but not in the argument list, so it's safe; :bufdo $d would delete "
        "its last line too. :argdo norm Gdd does the same in six more keys."),
    "argdo-2": (":args s<Tab>*|argdo norm oset -euo pipefail<CR>",
        "s<Tab> completes scripts/, so :args scripts/* puts just the three scripts in the list (and opens the "
        "first). | ends :args, and :argdo then runs :normal in each file: o opens a line below line 1 and types "
        "the text. install.sh isn't in the list, so it doesn't change. Enter and a new :argdo would cost a key "
        "more than |."),
    "argdo-3": (":args s<Tab><Tab>m<Tab>*|argdo s/;/.model;/<CR>",
        "s<Tab> completes src/, the next Tab goes inside it to src/shop/, and m<Tab> completes model/, so :args "
        "gets just Order.java and Product.java. In each, :s works on the cursor's line, line 1, and puts .model "
        "before the ;. :args **/model/* picks the same files in four more keys, and works however deep the "
        "folder is."),
    "argdo-4": (":args **/*.md|argdo %s/ttp:/ttps:/ge<CR>",
        "**/*.md picks the Markdown files here and in docs/, but not build.cmd or src/server.py. :argdo runs the "
        ":s in each, and e keeps faq.md, which has no link, from stopping it. ttp: is enough of a pattern: ftp: "
        "has only one t, and the https: link already has its s. **/*d would also take in build.cmd."),
    "argdo-5": (":argdo g/\\*$/norm A  # noqa: F403<CR>",
        ":argdo runs the :g in each Python file in the list. The star imports are the only lines that end in a "
        "star (\\* in the pattern), and :norm A appends the comment to each one. :bufdo would reach notes.txt "
        "too, and typing import \\* in the pattern is six keys longer."),
    "argdo-6": (":args s<Tab>*|argdo norm gg=G<CR>",
        "s<Tab> completes src/, and src/* is just the two C files. :args opens the first, and :argdo runs gg=G in "
        "each: gg goes to the top and =G re-indents to the end, with C's 4-space indent. Adding .c to the glob "
        "costs two keys and changes nothing here."),
    # ---------- :bufdo :windo ----------
    "bufdo-1": ("$*:bufdo %s//REDIS_URL/g<CR>",
        "$ puts the cursor on REDIS_HOST at the end of line 1, and * searches for it as a whole word. :bufdo runs "
        "the substitution in worker.py, cache.py and settings.py, and the empty pattern reuses the search, so "
        "DB_HOST stays, and so does the unopened legacy file. g covers settings.py's line, which has the name "
        "twice. Typing the name out, %s/REDIS_HOST/REDIS_URL/g, takes eight more keys."),
    "bufdo-2": ("jw*:windo %s//button_ok/<CR>",
        "jw puts the cursor on the quote before btn_ok, and * searches for the next word as a whole word. :windo "
        "runs the substitution in both visible windows. It also visits the task window and fails there, which "
        "doesn't matter. fr.json isn't in a window, so it keeps its key; :bufdo would have changed it too."),
    "bufdo-3": (":bufdo %s/list_add/list_push/e|%s/list_del/list_pop/<CR>",
        ":bufdo runs both substitutions in each of the three buffers. main.c has no list_add, so without e the "
        "first :s would fail there and skip the second, and main.c would keep list_del. Every buffer has a "
        "list_del, so the second :s needs no flag. The full names keep map_add safe; vendor/list_compat.c isn't "
        "open, so it's safe anyway."),
    "bufdo-4": (":bufdo norm oset -euo pipefail<CR>",
        "In each buffer the cursor is on line 1, the #! line, so :norm o opens the line below it and types the "
        "text. With six scripts that's three keys shorter than typing it once and then ]b. five times."),
    "bufdo-5": (":bufdo g/e.log/d<CR>",
        ":bufdo runs the :g in every listed buffer, and :g/pattern/d deletes each matching line. e.log (the . "
        "matches any character) is in console.log but not in console.error, store.load or dialog, and \\.log "
        "works too. scripts/debug.js isn't in the buffer list, so it keeps its log."),
    "bufdo-6": (":bufdo %s/\\s*$<CR>",
        "\\s*$ matches the whitespace at the end of every line, or nothing on a line that has none, so the :s never "
        "fails, even in README.md, and needs no e flag. A :s with no replacement deletes what it matches. \\s "
        "catches the tab as well; a plain space would leave it. The usual %s/\\s\\+$//e is four keys longer."),
    # ---------- :vimgrep :cnext ----------
    "vimgrep-1": (":vim /retries=/ **/*.py<CR><C-a>]q.]q.",
        ":vimgrep finds the three lines and puts the cursor on the first match, where Ctrl-a adds 1 to the next "
        "number on the line. ]q goes to the next match, and . repeats the Ctrl-a. The match in mail.py is on the "
        "def line, before its attempts=retries. :cdo norm with Ctrl-v Ctrl-a would also work, in more keys."),
    "vimgrep-2": (":vim /print(/ *.py<CR>cwlog.debug<Esc>]q]q.]q.",
        "The first match is the args print in cli.py: cw replaces print with log.debug. ]q goes to the "
        "order-number print, which stays, so another ]q skips it, and . repeats the change in orders.py, then in "
        "payments.py. :cdo can't skip a match; stepping through by hand lets you decide at each one."),
    "vimgrep-3": ("*:vim // *.c<CR>cwrx_buf<Esc>]q.]q]q.]q.]q.",
        "* searches for \\<buf\\>, and :vim // fills the quickfix list with every line that has it, http.c's "
        "first. cw renames the first buf, then ]q and . do the rest, with one extra ]q to skip the log message. "
        ":cdo s//rx_buf/ would rename the buf in the message too."),
    "vimgrep-4": (":vim /t=/g *<CR>5<C-a>]q.]q.",
        "Every timeout ends in t=, and nothing else here does. The g flag gives each match its own quickfix entry, "
        "so the line with two gets two. :vimgrep puts the cursor on the first, 5 Ctrl-a adds 5 to the number "
        "after it, and ]q and . do the other two. Spelling out timeout= costs six keys more."),
    "vimgrep-5": (":vim /ol\\w*(/ **<CR>3snew<Esc>3]q.",
        "The ( keeps app.py's import line out of the list, and ol\\w*( is enough to find old_api( calls. 3s "
        "replaces the three letters of old. The two calls in compat/legacy.py come next, so 3]q skips them "
        "and lands in worker.py, where . repeats the 3s. :cdo can't skip anything."),
    "vimgrep-6": (":vim /TO/ **<CR>CSpeichern<Esc>]qCGuardar<Esc>]qCEnregistrer",
        "TO is enough to find the three TODOs (the titles have t's, but no to). :vimgrep goes through the files "
        "in order, de, es, fr, and puts the cursor on each TODO in turn. It's the last word on its line, so C "
        "replaces it; each word is different, so ]q and a new C each time."),
    # ---------- :cdo :cfdo ----------
    "cdo-1": ("*:vim // **/*.py<CR>:cdo s//get_user/<CR>",
        "* searches for \\<fetch_user\\>, so fetch_users and test_fetch_user don't match. :vim // fills the quickfix "
        "list from that search in every .py file, and :cdo runs s//get_user/ on each matching line, reusing the "
        "pattern once more. No line has two calls, so it needs no g flag."),
    "cdo-2": (":vim /sleep(/ *.py<CR>:cfdo norm ggOimport time<CR>",
        "sleep( matches the calls but not the word sleeps in config.py's comment. poller.py has two matches, so "
        ":cdo would add two imports there; :cfdo runs once per file. The cursor starts on the file's first match, "
        "so gg goes to the top before O opens a line above it."),
    "cdo-3": (":vim /print / *.py<CR>:cdo norm f r(A)<CR>",
        "At each match the cursor is on the p of print. f and a space find the space after it, r( turns that "
        "space into a parenthesis, and A) adds the closing one at the end of the line. A :cdo s with a group "
        "would also work, in more keys."),
    "cdo-4": (":vim /r(/ *<CR>:cdo s/)/, exc_info=True)<CR>",
        "r( is in log.error( and nowhere else, so the list has just the two error calls. :cdo runs the :s on each "
        "of those lines: each has a single ), and the new argument goes in front of it. :cdo norm $i, "
        "exc_info=True does the same with Normal keys, two keys longer."),
    "cdo-5": (":vim /^i/ *<CR>:cfdo %s/req\\w*/httpx/g<CR>",
        "Only the two modules have a line starting with i: their import. :cfdo runs once in each file in the "
        "list, and %s there covers the whole file, so the import and every call change together; :cdo would "
        "only change the import lines. req\\w* is requests and nothing else. README.md and notes.py never get "
        "into the list."),
    "cdo-6": (":vim /t(/ **<CR>:cdo norm gcc<CR>",
        "t( only appears in breakpoint(), so :vimgrep lists the three calls and not the docs. At each, :cdo norm "
        "gcc comments out the line with Python's # and keeps its indent. Commenting doesn't add or remove lines, "
        "so every entry still points at the right line."),
}
