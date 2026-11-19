"""Reference solutions for Project 10 (spoilers!). Each entry: exercise name -> (steps, overview), where
steps is a list of (keys, what they do) in the order typed. The solution is the keys joined together.

See one with:  python3 check.py --show N      Watch it typed:  python3 check.py --watch N
"""
SOLUTIONS = {
    "merge-conflicts": ([
        (":,8sor u|g/^[<=>]/d<CR>", "steps 1, 2 and 3, and every marker in the file: sorting lines 1 to 8 "
                                    "keeps both sides, u drops the duplicate import os, and the :g chained "
                                    "after | deletes all twelve <<<<<<<, ======= and >>>>>>> lines. It leaves "
                                    "the cursor on the export() call near the bottom (where the last "
                                    "marker was), so work bottom-up from there."),
        ("$dF,", "step 10: from the closing ), dF, deletes back through the comma."),
        ("kf*y2W", "steps 8 and 9 the other way round: instead of wrapping feature-branch's sum in "
                   "round(..., 2), yank its '* o[\"qty\"] ' (two WORDs and the space after)..."),
        ("2kffP", "...and put it in front of the for in HEAD's line."),
        ("jdj", "step 8: the print and feature-branch's total, the two lines left from feature-branch's side."),
        ("4-flRre<Esc>", "step 7: read is as long as load and only the first two letters differ, so Replace "
                         "mode types re over lo."),
        ("5-dd", "step 6: HEAD's json.dump line."),
        ("9k2dd", "step 4: HEAD's two loader lines."),
        ("jf,yt)", "step 5: yank ', encoding=\"utf-8\"' from read_orders(). Yanking after the deletes keeps "
                   "it in the unnamed register..."),
        ("5jf)P", "...so P puts it before the ) after newline=\"\"."),
    ], "Resolving a conflict is deleting lines. :sort u resolves the import hunk, the duplicate and the order "
       "at once, and a :g chained after it wipes every marker in one go, so what is left is only the "
       "unwanted sides: two lines, one, and two, each a short counted delete. Going bottom-up from where :g "
       "leaves the cursor keeps the line numbers above stable. Measured: the previous reference (71) let "
       "counted dd's take the markers with the sides (3dd after the sort, 4dd, j3dd, jdd and the like), "
       "which costs 5 more; deleting markers with a separate :g/^[<=>]/d at the end costs 1 more than "
       "chaining it; wrapping feature-branch's total in round(..., 2) instead of yanking the qty costs 10 "
       "more; yanking the encoding before the deletes forces \"0P, 2 more."),
    "compose-config": ([
        ("dj", "step 1: d with j deletes both lines."),
        ("2j$2<C-a>", "step 2: $ puts the cursor on 25, so Ctrl-a doesn't add to the 1."),
        ("5jdiw", "steps 3 and 5 just swap true and false. The column lands inside false, and diw cuts it."),
        ("7jviwp", "step 5: viwp puts false over true, and true, the text it replaced, goes into the register."),
        ("7kp", "step 3: back on read_only's line, p puts true after the space."),
        ("kfaciwbackend<Esc>", "step 4: fa finds the a of api in the URL."),
        ("3j.2+.", "step 4: . repeats ciw on the other two references. ./api is never touched."),
        ('4jWciW"<C-r>-"<Esc>', "step 6: ciW cuts 3.10 into the small-delete register, and Ctrl-r - puts it "
                                "back between the quotes."),
        ("j.", "step 7: . replays the Ctrl-r -, which now holds 08:00."),
        ("3+<C-a>", "step 8: + lands on the dash, and Ctrl-a finds the first number after it."),
        ("5+2<C-a>", "step 9."),
        ("8jddp", "step 12: ddp swaps two lines."),
        ("k$4<C-a>", "step 13."),
        ("6k>jyypfUcwDB", "steps 10 and 11, last so the final <Esc> is free. >j indents both lines (YAML's "
                          "shiftwidth is 2), then yyp copies the user line and cw changes USER to DB."),
    ], "Straight down the file, one edit after another, letting . do the repeats, with the db environment "
       "kept for last because it ends in Insert mode. true and false trade places, so the deleted false is "
       "put over true and comes back as true. Measured: the previous reference came to 89 (ciwtrue and "
       "Rfalse, and the db lines before cache). t Ctrl-n can complete true (ciwt<C-n> saves 2) but then "
       "false has to be typed; the swap saves 5. A :s rename has to skip ./api and http://api, and costs "
       "more than ciw + .; :,+s/\\S*$/\"&\" quotes both values in 14 keys against 12 for ciW and .; bumping "
       "redis before moving the line ties at 9."),
    "ascii-architecture": ([
        ("<C-a>", "step 1. Ctrl-a finds the first number on the line, the 2."),
        ("j6A=<Esc>", "step 2. A count before A types the six missing = at once."),
        ("8+<C-v>j2t|r ",
         "step 3 starts. + lands on the cache box's corner. The block covers the top two lines of the box "
         "and the arrow (t| twice stops just before the cdn box), and r<Space> blanks them without moving "
         "anything. The bottom line is left alone on purpose: it's about to be replaced whole."),
        ("f+;R-+<Esc>",
         "step 4. The second + on the line is the short corner, and R types over it and the space after it. "
         "This line is now finished, and here's the key observation: the line under the edge box must be "
         "exactly the same (same corners, same assets border)..."),
        ("yy", "...so yank it."),
        ("jbRedge<Esc>",
         "step 5. The cursor lands on the box's right border, b goes back to cdn, and R overwrites it."),
        ("jVp",
         "end of step 3: Vp replaces the old bottom line, cache border, gRPC and all, with the copy. A put "
         "in Visual mode leaves the text it replaced in the unnamed register, so you're now holding that "
         "old line."),
        ("4jhr-4hr<lt>",
         "step 7. Vp left the cursor on the corner of the edge box, which is in the column of the gateway "
         "box's left border. One column left is the > of the arrow, four more is its first -."),
        ("jVp",
         "step 6. Look at the line you're holding: a box border at column 1, the gateway-wide border at "
         "column 19, gRPC in the gap, then a border under assets. That's exactly what the line under the "
         "auth row should become, so Vp swaps it in: gRPC moves down without being erased or retyped."),
        ("$h<C-v>2ky4p",
         "step 8. Yank a one-column slice of the orders box (-, space, -) and paste it four times. This time "
         "the cursor starts on the bottom line, so the block goes up."),
        ("j3hR (v2)<Esc>", "step 9."),
        ("5jT|R postgres<Esc>", "step 10. T| stops just inside the box's left border."),
        ("3k5yy}P",
         "step 11 starts: copy the arrow and the box, and put them above the blank line before the legend..."),
        ("r:", "...dot the arrow..."),
        ("3jbR replica", "...and relabel the copy."),
    ], "R, r and Visual block are the ASCII-art tools: they change characters in place, so nothing to their "
       "right moves. The big saving is to compare whole lines, not just characters: once the edge box's top "
       "border is fixed, its bottom border is a copy of it, and the old line it replaces (gRPC included) is "
       "exactly the new line under the auth row. Two Vp do steps 3 and 6 together, because Visual p hands "
       "you the line it overwrote. Measured alternatives: the previous reference blanked gRPC with vEr<Space> "
       "and retyped it with R five lines down (110). Swapping the two lines with :12m17|-m11 takes 107, and "
       "copying the line under auth over both edge-box borders with three Vp takes 105. Fixing the arrow "
       "after widening orders (0f>r-4hr<) takes 102, and copying the mysql box before relabelling it ties "
       "at 101. :-3,+t+ instead of 5yy}P takes 3 more, and widening with $R----+ and . plus one R on the "
       "label row takes 6 more."),
    "c-prototypes": ([
        ("3j3Jo<Esc>",
         "step 1. 3J joins the three lines of struct vec with one space at each join. Then o<Esc> adds the "
         "blank line the prototype block needs. That change also moves the '[ mark (the start of the last "
         "change) to the new line, and the :g below copies to '[."),
        (":g/ .)$/t'[|s/$/;<CR>",
         "step 2. The four definition lines are the only lines that end in a space, one character and ) "
         "(vec b) or vec v)): main ends in (void), and the calls end in ;. For each one, "
         ":t'[ copies it below the '[ mark and s/$/; adds the semicolon. That :s is a change too, so '[ "
         "moves to the new prototype and the next copy lands under it, in order. With a plain line number "
         "(t5) the prototypes would come out reversed."),
        ("4jIconst <Esc>", "step 3."),
        ("8jf+r-;.", "step 6. r- on the first +, then ; finds the next + and . repeats r-."),
        ("5j$Farb", "step 7. The a that's wrong is the last one on the line."),
        ("GIstatic <Esc>k.", "step 10, on the two helpers at the bottom."),
        ("dap4{P",
         "step 9. dap takes the helpers and the blank line above them. Four { reach the blank line after "
         "main, and P puts the helpers above it."),
        (r":%s/%d/%g/g|%s/_/tor_/g|%s/\<lt>d\>/delta<CR>",
         "steps 4, 8, 11 and 5 on one command line. %d to %g covers main and vec_print together. Every _ in "
         "the file belongs to a vec_ name, so _ to tor_ renames them all, prototypes included. The %d fix "
         "must come before \\<d\\>, which also matches the d of %d. A :s without a closing / would take a "
         "following | as part of its replacement, so the delta rename goes last."),
    ], "Join the struct, then let one :g build the prototypes. The puzzle is the address after t: '[ follows "
       "the last change, so each copy lands under the one before and the order comes out right, and o<Esc> "
       "both adds the missing blank line and puts '[ there to start. Leave the renames for one command line "
       "at the end. Measured alternatives: the previous reference matched the definitions with _.*)$ (an _, "
       "and ) at the end), one key longer at 107. With that pattern, copying above main with t/^i/- took "
       "109, copying to $ and moving the block with :-3,m5 took 112, and doing the renames first (still "
       "with '[) took 109."),
    "readme-cleanup": ([
        ("/or<CR>xp", "step 1: the first 'or' is in form; xp swaps the o and the r."),
        (":,$s/^#/##<CR>", "step 2: the range :,$ starts at the cursor (line 3), so the title is out of "
                           "reach."),
        (":%s/ma[^.]*/`&`<CR>", "step 6: ma only occurs in make (NAME has 'am', not 'ma'). [^.]* runs up to "
                                "a period or the end of the line, so make install and make test come along, "
                                "and & is the whole match."),
        ("f[di[lvi(pF[p", "step 10: di[ cuts CONTRIBUTING.md and leaves the cursor on the ], so l is enough "
                          "to reach the (. vi(p puts the cut text in place of 'the guide' (and puts 'the "
                          "guide' in the register), and F[p puts that back in the brackets."),
        ("+foxp", "step 11: + goes to the first non-blank of the next line."),
        (":g/*/norm r-la`<C-o>f:`<CR>", "steps 8 and 9: a * at the start of a pattern is literal. r- swaps the "
                                        "bullet, la` adds the opening backtick, and Ctrl-o f: jumps to the colon "
                                        "without leaving Insert mode, where the closing one goes."),
        ("10k5h<C-v>3jyP", "step 7: 10k5h lands on the space before the header's second |. Down that column "
                           "there's a space, a dash, a space and a space: on each row exactly the character it "
                           "needs one more of. Ctrl-v 3j y copies that one-column block and P puts it back in "
                           "front of itself, doubling every character in it."),
        ("5kVjg<C-a>", "step 5: g Ctrl-a adds 1 on the first selected line, 2 on the second."),
        ("9k6dd5jp", "step 3, the other way round: moving Usage (six lines) below Install puts Install first "
                     "just the same, and leaves the cursor on Usage, four lines above the example."),
        ("4j<<O```sh<Esc>jo<C-a><C-w>", "step 4: dedent first, so O and o open unindented lines. In Insert mode "
                                        "Ctrl-a types the previous insert again (```sh) and Ctrl-w deletes the sh. "
                                        "Ending in Insert mode makes the final <Esc> free."),
    ], "Three of the steps are one command each from anywhere, so they're placed where they leave the cursor "
       "next to the following edit, and the section move goes just before the fence, which ends in Insert mode. "
       "Measured: the previous reference came to 117: f( instead of l in the link, a block insert of a space plus jr- for the table (14 "
       "keys with the jump, against 10 for the yank and put), o``` for the closing fence, and Install moved up "
       "with 2j6dd8kP as the last edit. Moving Install up here instead (3k6dd6kP) costs 1 more, since the "
       "example is then 10 lines down. :%s/\\v^. (.{-}):/- "
       "`\\1`: does the bullets and backticks in 25 keys against 20 for the :g; :%s/\\vmake( \\w+)?/`&` is 22 "
       "against 16."),
    "strbuf-bugs": ([
        ("GkyyPf)i->b<C-n><Esc>",
         "step 12, done first. G and k reach free(sb);, yyP copies it above itself, and f) i types ->buf "
         "in front of the ). Ctrl-n completes b to buf. Your ->buf also stays in the . register (the "
         "last text you inserted), and step 2 needs it."),
        ("dap{{P",
         "step 13. At the end of the file, dap takes sb_free plus the blank line above it. Two { land on "
         "the blank line under sb_new, and P puts the function above that line: one blank line on each side."),
        ("4kfsab<C-r>.<Esc>",
         "step 2. P left the cursor on that blank line, so 4k is the if line and fs is its s. Type b, then "
         "Ctrl-r . types ->buf back from the . register: s becomes sb->buf."),
        ("kf)i + 1<Esc>yi(",
         "step 1. Then yi( copies sb->len + 1 into register 0. Later deletes can't overwrite register 0, "
         "so it's safe there until the memcpy calls."),
        ("jA {<CR>fr<C-x><C-l><Esc>jo}<Esc>",
         "step 3. Ctrl-x Ctrl-l completes a whole line: fr finds free(sb); in sb_free and keeps this "
         "line's indent. C indenting moves the } back to four spaces as you type it."),
        ("jqqRmem<Esc>f)i, <C-r>0<Esc>q",
         "step 4, recorded as macro q because sb_cstr needs exactly the same change. R types mem over "
         "str, and Ctrl-r 0 types the length you yanked."),
        ("or<C-n> sb;<Esc>",
         "step 5. return is the only word in the file that starts with r, so Ctrl-n completes it."),
        ("9jaco<C-n> <Esc>8jF(.",
         "steps 6 and 9. The ; of return sb; is in the same column as the ( of sb_cstr, nine lines down. "
         "co Ctrl-n is const. sb_print's ( is in that column too, but the insert moved the cursor, so F( "
         "goes back to it before . repeats the insert."),
        ("4-Q",
         "step 8. - is like k but lands on the first non-blank character, so 4- puts the cursor on the "
         "s of sb_cstr's strcpy, the same spot where you started recording. Q replays the macro you "
         "recorded last."),
        ("kkf*Xx",
         "step 7. The macro ended on the 1, and on the line two up, the next * after that column is the "
         "one in char *. X deletes the space before it and x the * itself."),
        ("8jF=x",
         "step 10. The loop line is shorter, so the cursor lands at its end, and F= finds the = of <=."),
        ("jjFdszu",
         "step 11. Fd goes back to the d of %d, and s swaps it for zu."),
    ], "Work from the bottom up, starting with sb_free. Its fix leaves ->buf in the . register for step 2, "
       "and once it has moved, every other edit happens in one pass down the file. The two strcpy fixes are "
       "the same change, so the first one is recorded as a macro, and the length comes from a yank instead of "
       "being typed twice. Completion does a lot of the typing: Ctrl-n for buf, return and const, and Ctrl-x "
       "Ctrl-l for a whole line. Measured alternatives: 4k^Q instead of 4-Q takes 114, going top-down and "
       "moving sb_free last takes 117, and one :%s for both strcpy lines instead of the macro takes 123."),
    "modern-java": ([
        ("jfA9xea.of<Esc>", "step 1: 9x deletes \"Arrays.as\" leaving List(, and ea types .of after it."),
        ("jdi<", "step 2: di< looks ahead on the line for the next <...>, which here is <Item> after "
                 "ArrayList (the cursor is already past List<Item>)."),
        ("2+.kJ", "step 3: 2+ lands on the first non-blank of the HashMap line, . repeats di<, and kJ joins "
                  "it onto the declaration."),
        ("4jqqJXce -><Esc>+q", "step 5, recorded on the first case: J pulls the return line up (the cursor "
                               "lands on the space it inserts), X deletes the colon, and ce changes "
                               "\" return\" into \" ->\". + lands on the next case."),
        ("2Q", "step 5: the other two cases. The last run ends on the closing brace."),
        ("A;<Esc>", "step 6."),
        ("4-hP", "step 4: the macro's ce left \" return\" (space first) in the unnamed register. 4- is on "
                 "the s of switch, h on the last space of the indent, and P puts it there, so the space "
                 "ends up between return and switch."),
        ("/co<CR>CgetOrDefault(n<C-p>, 0);<Esc>", "step 7: C retypes the rest of the line; n Ctrl-p "
                                                   "completes name from the line above."),
        ("4+cwvar<Esc>", "step 8."),
        ("2+yt.kvi(pF=r:jdd", "step 9: yt. yanks \"Item item = items\", almost the whole new loop header. "
                              "k keeps the column, which is the for's (, vi(p swaps the old loop control for "
                              "the yank, F=r: turns = into :, and jdd deletes the get(i) line."),
        ("6jf)i ot<C-n><Esc>+dd", "step 11: name the variable in the instanceof (ot Ctrl-n completes other "
                                  "from the cast line, so do it before deleting that line), then delete the "
                                  "cast line."),
        ("2kO@Override<Esc>8j.", "step 10: once above equals(), then . above hashCode()."),
    ], "Most of this is repeats in disguise: di< then . for both diamonds, a three-run macro for the cases, "
       "O@Override then . for both overrides. The rest are short local edits, where the trick is to reuse "
       "text already in the file: the return the macro deletes, the loop variable and the list on the line "
       "you are about to delete, name and other through completion. Measured: the previous reference (130) "
       "recorded $s -><Esc>Jwdwj and replayed it with 2@q (2 more in all, even though its \"return \" "
       "pastes with a 3-key 4-P), yanked \"Item item \" and typed \": items\" (4 more), and deleted the cast "
       "line first, so other had to be typed (1 more); the cases as one multi-line :s, "
       ":%s/:\\n *\\w*/ ->, leave no return in a register; ite Ctrl-p completes item, not items."),
    "py2-to-py3": ([
        ("A3<Esc>", "step 1: A appends at the end of the shebang."),
        (':3,5d|<|m1|g/"s/norm t"r(A)<CR>', "steps 2 and 4 on one command line: | separates Ex commands, which "
                                           "saves a <CR> and a colon each time. :3,5d deletes try:, the cPickle "
                                           "import and except:, and leaves the cursor on the indented import "
                                           "pickle; :< dedents it and :m1 moves it below line 1, above import "
                                           "sys. The :g comes last because it takes the rest of the line as its "
                                           "command. Only the print statements contain a quote followed by s "
                                           "(\"skipping, \"scale, \"saved). On each, :normal runs t\" (to the space "
                                           "before the quote), r( and A). The %-20s print is skipped: step 11 "
                                           "retypes that line anyway. :g leaves the cursor on the last print, so "
                                           "the rest goes bottom-up."),
        ("jFr4x", "step 13: Fr searches backward from the end of the line, and the first r it meets is the "
                  "one in raw_input; 4x deletes raw_."),
        ("5klR!=<Esc>", "step 12: 5k keeps the column, which is the space just before <>; l steps onto it and "
                        "R types != over both characters."),
        ("4kA()<Esc>", "step 4 again: the bare print, which the :g pattern skipped."),
        ('kf C(f"{u<C-p>[i]:20} {b<C-p>}")<Esc>', "step 11 (and step 4 for this print): k lands inside print, "
                                                  "f<Space> finds the space after it, and C retypes the rest of "
                                                  "the line, parenthesis included. u Ctrl-p and b Ctrl-p complete "
                                                  "urls and bar from the line above."),
        ("kf/a/<Esc>", "step 10: a second slash after the first."),
        ("kFxx", "step 9."),
        ("2kfv4X", "step 8: fv finds the v of itervalues, and 4X deletes the four characters before it, iter."),
        ("kBBRis<Esc>", "step 7: the column is past the end of if top == None:, so the cursor sits on the "
                        "colon; two Bs reach ==, and R types is over it."),
        ("2kbRs<C-n>ed(h<C-n>)<Esc>jdd", "step 6: 2k and b land on hits. R types sorted(hits) over "
                                         "hits.keys(), and Ctrl-n works in Replace mode too: s Ctrl-n completes "
                                         "sort from the line below (so sorted is s, Ctrl-n, e, d) and h Ctrl-n "
                                         "completes hits. jdd deletes urls.sort()."),
        ("7-wiu<C-n> <C-o>win h<C-n><C-o>dE<Esc>", "step 5 in one Insert session: 7- and w reach not. u Ctrl-n "
                                                   "completes url, Ctrl-o w hops to hits.has_key(url), in h "
                                                   "Ctrl-n types in hits, and Ctrl-o dE deletes the old WORD "
                                                   "hits.has_key(url). The cursor ends on the s of hits."),
        ("3ks as", "step 3: from the s of hits, 3k lands exactly on the comma, and s replaces it with ' as'. "
                   "The final <Esc> is free."),
    ], "Fix the shebang, then one command line does the imports and the print statements. :g leaves the cursor "
       "at the bottom, so everything else is done going up, where the line numbers above you never shift and "
       "several relative jumps land on the right column for free. Measured: the same edits top-down (as e, "
       "has_key, sorted and so on, with Ctrl-o j reaching the bare print from the f-string, then :g, raw_input "
       "and <>) tie at 137. The previous reference came to 142: jj3dd<<kddp for the imports, a separate "
       ":g/t \"/... that also caught the %-20s print, Csorted(h<C-n>), and c2W for has_key (16 keys against 15 "
       "here). :%s/\\v<x|raw_|iter fixes xrange, raw_input and itervalues in one command of 19 keys, but the "
       "three local edits cost 15 with their jumps."),
    "globals-to-struct": ([
        ("4jJhc6l,<Esc>",
         "step 2 first. J joins char empty; onto char fill; and leaves the cursor on the joining space, "
         "so h c6l replaces \"; char\" with a comma."),
        (">ip", "step 1 starts here: indent the member lines, one paragraph..."),
        ("Ostruct config {<Esc>", "...open a line above them..."),
        ("}O} cfg;<Esc>",
         "...and one below: } jumps to the blank line after the members, and O opens a line above it. C "
         "indenting puts the } back in column 1."),
        (r":,$s/\v<lt>[weql]|fill>/cfg.&/g<CR>",
         "step 3. The range starts on the cursor line (} cfg;), so the declarations above are left alone. "
         "Matching the first letter is enough: width, empty, quiet and label are the only words starting "
         "with w, e, q or l, and the replacement puts cfg. in front of that letter. fill> (fill at the end "
         "of a word) skips the local filled. The g flag catches both uses in the putchar line."),
        ("jf110<C-a>+.",
         "step 10. f1 gets past the 0 in i = 0, and 10 Ctrl-a turns 10 into 20. On the next line Ctrl-a "
         "finds the 10 by itself, so + then . repeats it."),
        ("6-*Ncgnco<C-n>_init<Esc>.",
         "step 4. * searches for set_defaults and N comes back to the call. cgn changes that match (co "
         "Ctrl-n completes config from struct config), and . changes the next one, the definition, which "
         "leaves the cursor up there."),
        ("Istatic <Esc>8j.", "step 11."),
        ("6k20<C-a>jjr-jcwloading<Esc>",
         "steps 5 to 7. Ctrl-a finds the 40 on its own. It leaves the cursor in the column of the '.' two "
         "lines down, and on the line below that the same column is the p of progress, so cw replaces just "
         "the word and leaves the quotes alone (ci\" works too, one key more)."),
        ("5jddjp", "step 8. Move int filled down past the two quiet lines."),
        ("4jf%a3", "step 9."),
    ], "Build the struct first, so the :s that adds cfg. can start on its closing line and leave the members "
       "alone. Matching only the first letter of each name keeps that :s short, and fill> is how it spares "
       "filled. The :s leaves the cursor in main(), so fix main there, and let the rename's . carry you back "
       "up to config_init for the rest. Measured alternatives: the previous reference used ci\" for the label "
       "and took 137. Renaming set_defaults with cw and /se . takes 1 more, doing draw before "
       "the defaults takes 1 more, and spelling out all five names (\\v<(width|fill|...)>) takes 19 more."),
    "unittest-to-pytest": ([
        ("w4spy<Esc>", "step 1: 4s replaces unit with py."),
        (":%s/self\\.//g|%s/self/cart<CR>", "step 5 on one command line. The first :s removes self. from "
                                            "self.cart and from every assertion, 23 places (g for the lines that "
                                            "have two). After it the only self left are the parameters, so the "
                                            "second renames them, setUp(self) too, which turns out to be handy. | "
                                            "saves a <CR> and a colon; it works here because the first :s ends "
                                            "with /g (a :s without its closing / takes the | into its "
                                            "replacement)."),
        (":g/  a/norm $x^6ldt(r f,s ==<CR>", "steps 6 and 9, and most of 7 and 8. Two spaces then a is true "
                                              "only of the lines that start with assert (with assertRaises has "
                                              "a single space). On each line, $x drops the closing paren, ^6l "
                                              "lands on the letter after assert, dt( deletes Equal, In, True or "
                                              "IsNone, r<Space> turns the ( into a space, and f,s == replaces the "
                                              "first comma, never the one inside [\"apple\", \"pear\"]. On the True "
                                              "and IsNone lines f, fails, which just ends :normal there."),
        ("16kA is None<Esc>", "step 7: the :g already made it assert cart.last_added."),
        ("5j2bRin<Esc>", "step 8: the :g turned the comma into ==; R types in over it."),
        ("9-Rreturn<Esc>", "step 3: 9- goes to the first non-blank 9 lines up, and return is exactly as long "
                           "as cart =."),
        ("kdbxep", "step 3: the column lands on the ( after setUp. db deletes setUp, x cuts the (, e moves to "
                   "the end of cart and p puts the ( back: cart():"),
        ("kS@p<C-p>.fixture<Esc>", "step 2: S retypes the class line; p Ctrl-p completes pytest, the nearest "
                                   "word above that starts with p."),
        ("<G", "step 4: dedents every line from here to the end of the file."),
        (":g/ t/-t-<CR>", "step 11: with the class line gone, only the def test_ lines contain a space and a "
                          "t. On each, :-t- copies the line above (a blank line) to just below itself, so every "
                          "test gets its second blank line, and the blank lines around the imports are never "
                          "touched."),
        ("Gdk", "step 12: the last two lines. Blank lines at the end of the file don't count."),
        ("3-WcfRpy<C-p>.r", "step 10, last so the final <Esc> is free: 3- goes to with, W to assertRaises, cfR "
                            "deletes up to the R, and py Ctrl-p completes pytest."),
    ], "Two lines of Ex commands do most of the work: strip self. and rename the parameters, then one :g that "
       "rewrites every assert line the same way. Then the odd ones out going up, the structure from the top, "
       "and the one edit that ends in Insert mode last. Measured: the previous reference came to 143 "
       "(separate :%s commands, py<C-p>, :,$g/^$/t. at 11 keys against 10 for :g/ t/-t-, and assertRaises "
       "edited before IsNone instead of last). A :s with groups for assertEqual and assertIn, "
       ":%s/\\v[EI]\\w+.(\\S+),(.*)./ \\1 ==\\2 (35 keys), plus . to repeat cf( on True and IsNone, came to "
       "162. :%s/\\vself(.cart)?/cart/g renames both kinds of self in 26 keys, one fewer than the two :s "
       "here, but only once every self.assert is gone, and making the :g delete self. too costs 2 more."),
    "harden-bash": ([
        ("oset -euo pipefail<Esc>", "step 1."),
        ("3jIreadonly <Esc>j.j.", "step 2. I types at the start of the line and . repeats it."),
        ("js$(<Esc>$r)",
         "step 3. readonly plus its space is 9 characters, and so is VERSION=, so the cursor is right on the "
         "backtick. s swaps it for $(, and $r) fixes the other end."),
        ("3jIlocal <Esc>10j.", "step 4, and with . the local half of step 8."),
        (r"4:s/HOST/\L&<CR>",
         "the rest of step 8. 4: makes the range the four lines of the function, so the HOST in the usage "
         "message stays, and \\L lowercases what & puts back."),
        ("WciW\"<C-r>-\"<Esc>k.W.",
         "step 10. ciW deletes the WORD $host into the small-delete register -, and Ctrl-r - types it back "
         "between the quotes. . replays the Ctrl-r - as well, so it quotes whatever WORD it just deleted: "
         "$SRC/ straight above (the two-space indent shifts both lines alike), then $host:/srv/$APP/."),
        ("11k$.", "step 5, with the same ."),
        ("20j$.", "and $h in the loop, half of step 14."),
        ("kF$i\"<Esc>f;.", "the rest of step 14, with a new . : a \" before $@ and another before ;."),
        ("kl.$.0W.", "step 12 with the same \" insert: before $0, before ) and before $(..."),
        ("A\" || ex<C-n> 1<Esc>",
         "...and step 13 adds the closing quote too. The exit in die() is the only word in the file that "
         "starts with ex, so Ctrl-n finishes it."),
        ("3-ca[[<C-r>-]<Esc>",
         "step 11. 3- lands at the start of the if line, and ca[ looks ahead along the line for the [ by "
         "itself. It deletes the whole test, brackets included, into the small-delete register. Type [, "
         "Ctrl-r - puts [ $# -eq 0 ] back, and ] closes the outer pair."),
        ("5kddjp",
         "step 9. dd takes the log line, which leaves the cursor on rsync, so j p puts it below ssh. It "
         "waits until here because dd and p would have replaced what . repeats."),
        ("=ip", "step 7. = re-indents the paragraph with the shell indent rules: four spaces inside { }."),
        ("4kA >&2", "step 6."),
    ], "Most of this file is quoting, so plan the . chains. ciW\"<C-r>-\" quotes any whole WORD and . repeats "
       "it, because Ctrl-r - reads the register again each time; i\" handles the expansions that aren't "
       "whole WORDs. A chain only lasts until the next different change, and that sets the order: the "
       "local and quoting chains first, the line move and the re-indent (which don't need .) last. "
       "Measured alternatives: the previous reference typed exit in full and added the brackets with "
       "F]i]<C-o>F[[<Esc> (Ctrl-o F[ jumps back to the [ without leaving Insert mode), 151 in all. "
       "Bottom-up took 159 with those, and finishing on the cd line instead tied at 151."),
    "training-loop": ([
        ("/0<CR>R3e-4<Esc>", "step 1: the first 0 in the file is the one in 0.01, and 3e-4 is as long as "
                             "0.01, so R types over it."),
        ("j40<C-a>", "step 2: Ctrl-a with a count adds 40 to the next number on the line."),
        ("j32<C-a>", "step 3."),
        ("4j$dF,k$P", "step 4: from the closing paren, dF, deletes back to the comma, ', shuffle=True'; "
                      "k$P puts it before train_dl's closing paren."),
        ("4+*:m-3|%s//&imizer/|%s/dl/loader<CR>", "steps 8, 6 and 5. 4+ lands on opt at the start of its line, "
                                                  "and * searches for \\<opt\\> (not optim), jumping to "
                                                  "opt.zero_grad(). Then one command line: :m-3 moves that line "
                                                  "to the top of the batch loop; in %s//&imizer the empty pattern "
                                                  "is the * search and & is the matched opt; dl only occurs in "
                                                  "the two names. Each | replaces a <CR> and a colon, but a :s "
                                                  "followed by | needs its closing / (without it the | becomes "
                                                  "part of the replacement), so only the first one saves a key. "
                                                  "The cursor ends on the validation loop."),
        (">2jO<C-d>with tor<C-n>.no_grad():<Esc>", "step 12: indent the loop first. O copies its indent and "
                                                   "Ctrl-d takes one level back off. tor Ctrl-n completes torch "
                                                   "(t Ctrl-n would find total first)."),
        ("kOm<C-n>.eval()<Esc>", "step 11: m Ctrl-n completes model."),
        ("5jA()<Esc>", "step 13."),
        ("8k.", "step 9: . repeats A() on the training loop's .item."),
        ("jgcc", "step 10."),
        ("7kOm<C-n>.train()<Esc>", "step 7: O above total = 0 copies its indent."),
        ('/%<CR>C{E<C-n>}.pt"<C-o>F"f', "step 14: the first % below is the one in %d. C retypes from there, E "
                                        "Ctrl-n completes EPOCHS, and Ctrl-o F\" jumps back to the opening "
                                        "quote to insert the f without leaving Insert mode."),
    ], "Down to the data loaders, then one command line for the move and both renames, which leaves the cursor "
       "in the validation loop. The rest of the loop body goes there and back up: the two .item fixes have to be "
       "A() and . in a row, so the validation one comes after the with and eval() lines. Measured: the previous "
       "reference came to 146, mostly top to bottom (7j2W to reach 0.01, :m-3 and the two :s on separate "
       "lines, 8jf% to reach %d). :%s/m$/&() fixes both .item lines in one command, but in this order the "
       "whole comes to 144; inserting the with line before indenting (Owith ...<Esc>j>2j) costs 1 more, "
       "because eval() is then two lines up instead of one."),
    "sql-migration": ([
        ("<C-a>", "step 1: Ctrl-a finds the 1 in v1 on its own."),
        ("+12~", "step 2, line 2: ~ with a count flips the case of 12 characters, exactly \"create table\"."),
        ("w*eas<Esc>ne.", "step 4: * searches \\<customer\\>, a whole word, so customer_id and "
                          "orders_by_customer can't match. It jumps to REFERENCES customer(id); add the s, "
                          "then n wraps back to line 2 for e."),
        (":%s/LE/& IF NOT EXISTS<CR>", "step 3: LE has capitals, so smartcase matches only TABLE."),
        (":%s/V.*)/TEXT NOT NULL<CR>", "steps 5 and 6 together: every VARCHAR(255) column is also one that "
                                       "must be NOT NULL. V.*) runs to the last ) on the line, which is "
                                       "always VARCHAR's. :s ends on the title line."),
        ("$y2F j$P", "step 6, price: from the comma, y2F<Space> yanks back to the second space, \" NOT NULL\", "
                     "and $P puts it before price's comma."),
        ("j$x", "step 9."),
        ("dap2{p", "step 8: dap takes the table and its blank line, 2{ climbs to the blank line above "
                   "orders, p puts it below."),
        ("3kqqyypRupd<Esc>kA,<Esc>q", "step 7, recorded on customer's created_at: yyp copies the column, "
                                      "Rupd types over cre (created and updated differ only there), and "
                                      "kA, gives the old last column its comma."),
        ("16jQ", "step 7: the same in orders."),
        ("4+12~2w2~", "step 2, the index line: create index is 12 characters too, and 2~ flips on."),
        ("3+3sINSERT INTO p<C-p> (<Esc>f,a <Esc>;.A) VALUES<Esc>", "step 10: 3s replaces \"-- \", p Ctrl-p "
                                                                   "completes product from the comment "
                                                                   "above, and a space after each comma is a "
                                                                   ". repeat."),
        ("+qq3s<C-t>(<C-o>2w '<C-o>w'<C-o>l <C-o>$),<Esc>+q", "step 11, recorded on the first row: 3s swaps "
            "\"-- \" for (, Ctrl-t indents the line without leaving Insert mode, and Ctrl-o w hops word by "
            "word (1 , Widget , 2) so the quotes and spaces go in the right places. + ends on the next row, "
            "ready for the replay."),
        ("5Q", "step 11: the other five rows. On the last one the final + has nowhere to go, so the replay "
               "stops there with the cursor on the comma it just typed..."),
        ("r;", "...step 12."),
    ], "Two pairs of steps collapse: VARCHAR -> TEXT plus NOT NULL is one :s (and price borrows its NOT NULL "
       "with a yank), and the customer rename is * plus one appended s and a dot. Both new columns are a "
       "copy of created_at with three letters typed over, so a five-command macro adds them. The seed rows "
       "are a macro too: Ctrl-t and Ctrl-o w keep it in Insert mode almost the whole way. Measured: the "
       "previous reference (181) uppercased with gUww. (1 more each time), typed the new column as "
       "A,<CR>updated_at T<C-p> and repeated it with . (2 more), and replayed with 5@q and $r; (2 more); "
       r"one :s with three groups, :%s/\v-- (.),(\w+),(.*)/    (\1, '\2', \3),, is the obvious tool for "
       "the rows but costs 15 more than the macro; typing \" NOT NULL\" for price costs 5 more; doing the "
       "rows before the header ties (the header's <Esc> becomes free, the trip back costs 1)."),
    "review-userservice": ([
        ("yypfA5x", "step 1: yyp copies the ArrayList import, fA5x deletes \"Array\" so the copy imports List."),
        ("k*.n.", "step 6: k lands on the A of line 1's ArrayList (same column). * jumps to the next whole-word "
                  "ArrayList, the return type, and . repeats 5x there. n. does the local list."),
        ("kO@Override<Esc>", "step 5, first half: @Override above findActive()."),
        ("}j.", "step 5, second half: } jumps to the blank line before register(), j steps onto it, and . "
                "repeats the O@Override."),
        ("/res<CR>xp", "step 10: the search lands on the r of usres, and xp swaps r and e."),
        (":g/Sy/d<CR>", "step 8: Sy has a capital, so smartcase makes it match only System. With println gone, "
                        "private is also the only word left that starts with pr (that pays off in step 3)."),
        (":%s/500/MAX_USERS<CR>", "step 2, first half: both uses at once. Doing it before the constant exists "
                                  "keeps that 500 safe, and :s leaves the cursor on spaceLeft(), the last line "
                                  "it changed."),
        ("dk{P", "step 12: dk cuts spaceLeft() with the blank line above it, { jumps back to the blank line "
                 "above welcome(), and P puts both there."),
        ('/St<CR>qqd2Wf)i, <C-r>"<BS><BS><Esc>q', "step 11, the signature, recorded in q: d2W cuts \"String "
                                                  "text, \" (two WORDs and the space), f) goes to the closing "
                                                  "paren, and in front of it you type \", \" and Ctrl-r \" "
                                                  "pastes the cut; two <BS> drop its trailing \", \"."),
        ("+*:%s//mailer/g|%s/out/active<CR>", "steps 4 and 7: + is on the m of m.send, so * searches \\<m\\>, "
                                              "and an empty pattern reuses it. After a flag, | chains the next "
                                              ":s for free. out is safe to replace now that System.out is "
                                              "gone."),
        ('/"W<CR>Q', "step 11, the call: the search lands on the quote that starts \"Welcome aboard!\", the "
                     "first argument, and Q replays the swap: d2W takes the string and its comma, and it goes "
                     "back in after u."),
        ("? =<CR>4s.equals(<C-o>f))<Esc>", "step 9: ? = finds the space before ==, 4s replaces \" == \", and "
                                           "Ctrl-o f) hops to the if's ) to type the extra one."),
        ("6GIpr<C-n> final <Esc>k.", "step 3: pr Ctrl-n completes private. Once on mailer, then . on repo."),
        ("O<C-a>int M<C-p> = 500;<C-o>Ffstatic ", "step 2, second half: Ctrl-a retypes the last insert, "
                                                  "\"private final \" (the completed word included). M Ctrl-p "
                                                  "completes MAX_USERS, and Ctrl-o Ff jumps back to slip "
                                                  "static in."),
    ], "The order is built around repeats and landing spots. The List import and the List types are the same "
       "5x, so * and . finish them; @Override is one O and one dot. The 500 substitution has to run before "
       "the constant is typed, and it drops you on spaceLeft(), ready to move it. Both welcome() argument "
       "lists swap with the same keys, so the signature is recorded and the call is a Q. private final is "
       "typed once (with completion) and pays three times: . for the second field, Ctrl-a for the "
       "constant. Measured: the previous reference (186) swapped both argument lists with one "
       r":%s/\v\((.*), (.*u)/(\2, \1, 3 more than the macro, and typed private in full, 4 more; the same "
       "edits as separate commands, top to bottom, cost 199; /Ar<CR> instead of k* costs 2 more."),
    "junit5-migration": ([
        (r":%s/\v\a+c |A\l+\.|test(.)/\l\1/g|%s/[AB][ef]\w*/&Each<CR>",
         "steps 5, 6 and 7, then step 3. Each alternative is deleted; only test(.) captures something, the "
         "letter after test, and \\l lowercases it. The capital A makes the pattern case-sensitive, so "
         "CartTest and @Test are safe. Running it first keeps the short pattern safe: \\a+c<Space> would "
         "also eat the \"static \" and A\\l+\\. the \"Assertions.\" of the import you write at the end. "
         "After the g flag, | chains a second :s: [AB][ef] matches Before and After (and nothing else "
         "here), in the imports and the annotations. It ends on @AfterEach."),
        ('7jqq+f"dWt;i, <C-r>"<BS><BS><Esc>q', "step 8, recorded on the first assertion: dW cuts the message "
                                                 "with its comma and space, t; stops on the last ), and "
                                                 "Ctrl-r \" pastes the message back after a new comma; two "
                                                 "<BS> drop the copied \", \"."),
        ("2Q", "step 8: the other two assertions. Each run starts with + so it ends on the line it fixed."),
        ("0150<C-a>", "step 9: 0 goes back to the start of the line (Ctrl-a only looks right of the cursor), "
                      "then Ctrl-a with a count adds 150."),
        ("3jByt)F(D", "step 10: 3j keeps the column of 300, which is inside IllegalArgumentException; B backs "
                      "up to its start and yt) yanks the class into register 0. F(D then cuts "
                      "\"(expected = ...)\" from @Test."),
        ("2jIassertThrows(<C-r>0,<CR>() -> <C-o>f;)<Esc>", "step 11: Ctrl-r 0 pastes the class while typing, "
                                                           "Enter gets the continuation indent for free, and "
                                                           "Ctrl-o f; puts the closing ) before the "
                                                           "semicolon."),
        ("/Ig<CR>cwDisabled<Esc>n.", "step 4: two places, so cw and . beat a :s by 2. n wraps to the import, "
                                     "and leaves you on line 4, near the imports that are still to do."),
        (":2m0<CR>b<C-v>4jIjupiter.api.<Esc>", "steps 2 and 1: :2m0 puts the Assert import first, b backs up "
                                               "to the A of Assert, the column where every import's class "
                                               "name starts, and one Visual-block insert fixes all five "
                                               "packages."),
        ("Bistatic <Esc>A<BS>ions.*;<CR>", "step 2: B jumps back to org for the static, A<BS> replaces the "
                                           ";, and Enter opens the blank line. It is the last edit, so its "
                                           "<Esc> is free."),
    ], "Three steps that look different (drop public, drop the test prefix, drop Assert.) are all deletions, "
       "so one :s with alternatives does them, with \\l fixing the letter after test; the Each :s rides "
       "along after a |. The imports are a column job for Ctrl-v, and the three messages are a three-line "
       "macro. Text is never retyped when it can be cut and pasted: the messages and the expected exception "
       "both travel through a register. Ending on the static import makes its last <Esc> free. Measured: "
       "the previous reference (188) did the imports first, which forces the longer pu\\w+<Space> and "
       "Assert\\. (3 more), ran the Each :s on its own (1 more) and replayed with 2@q (1 more); moving the "
       r'messages with :%s/\v(".*"), (.*\(.)/\2, \1 costs 5 more than the macro; :%s/Ig\w*/Disabled costs '
       "2 more than cw and .; cutting the class with f(dtID and pasting it with Ctrl-r \" <BS>, ties."),
    "review-menu-page": ([
        ("4jfua <C-k>.M Be<C-n> Th<C-n><Esc>", "step 1: Ctrl-k .M types the middle dot, and Ctrl-n completes Bean "
                                              "and There from the footer: no other words start with those "
                                              "letters."),
        ("7jddcitFind us<Esc>", "steps 2 and 3: dd deletes the Jobs link and leaves the cursor on the Contact link, "
                                "where cit changes the text between the tags."),
        ("3+fo~w~", "step 4: + goes to the first non-blank, so fo finds the o of our. (3j would keep the column of "
                    "the last edit, past the end of this line.)"),
        ("5jf520<C-a>", "step 5: a count adds 20 to the 50."),
        (":-,+2sor<CR>", "step 6: from the Espresso line, the coffees are the line above it to the two below it."),
        ("8jqqI<lt>li><Esc>$F a<lt>b><Esc>A<lt>/b><lt>/li><Esc>jq2@q",
         "step 7: record the change on the Croissant line, with the price in <b> like the coffees for now, and "
         "2@q replays it on the other two."),
        (":%s/<lt>b>/&<C-k>Eu/|%s/b>/strong>/g<CR>",
         "steps 8 and 9 for all seven prices: the first :s puts a € after every <b>, and the one after | turns "
         "<b> and </b> into strong tags, since both end in b>. The / before | matters: without it the first "
         "replacement runs on to the next /."),
        ('3jdd$i loading="lazy"<Esc>j$.', "steps 10 and 11: $ lands on the > of the tag, and . inserts the same "
                                          "text before the next image's >."),
        ("3+f(3s<C-k>Co<Esc><C-a>f-h3s<C-k>-N<Esc>",
         "steps 12, 13 and 14: 3s replaces the three characters of (c), Ctrl-a finds the year after it, and the "
         "second 3s replaces \" - \" with the dash. The last <Esc> is free."),
    ], "Down the page one section at a time. The pastries get <b> from the macro rather than <strong>€, so that "
       "one :s afterwards treats all seven prices the same way. Digraphs work wherever you type text, so the € "
       "goes into that :s on the command line. Measured: typing Bean There instead of completing it costs 3 "
       "more."),
    "review-package-json": ([
        ("jfTgu$", "step 1: gu$ lowercases from the T to the end of the line. The M goes too, and the quotes and "
                   "the comma have no case."),
        ("j<C-a>lR.0.0<Esc>", "step 2: Ctrl-a finds the 1, and Replace mode types .0.0 over .9.4."),
        ("j$bcwtrue<Esc>", "step 3."),
        ('2+ci"dev<Esc>', "step 4: + puts the cursor on the line's first quote, so ci\" takes the first string."),
        ("2+$bsvit<Esc>$i run<Esc>", "step 5: jest and vitest end the same way, so s replaces just the j."),
        ('A,<CR>"lint": "es<C-n> ."<Esc>', "step 6: the test line needs a comma now. Ctrl-n completes eslint "
                                            "from the dependencies below."),
        ("5jdd2dd", "steps 7, 8 and 9: dd deletes eslint into register 1, and 2dd deletes lodash and jest into "
                    "register 1, which shifts eslint to register 2."),
        ("2-f.<C-a>2l<C-a>", "step 10: - goes to the first non-blank, and f. to the dot after 18, so Ctrl-a "
                             "finds the 2. (From the column of the last edit, f. would find nothing.)"),
        ("vi{:sor<CR>A,<Esc>3j$x", "step 11 for dependencies: vi{ selects the lines inside the braces. After "
                                   "sorting, axios, the old last line, is first and has no comma, and react is "
                                   "last with one."),
        ('3j"2PjA,<CR>"vitest": "1.6.0"<Esc>', "steps 7 and 12, and 11 for devDependencies: \"2P puts eslint "
                                               "above vite, already in order, and vitest goes last."),
        ("2j4JxF[lx", "step 14: 4J joins the four lines with a space at each join. The cursor stays at the last "
                      "one, before ], so x deletes it, and F[lx deletes the one after [."),
        ("2j4<C-a>", "step 15: 16 plus 4."),
        (":%s/\\^/<CR>", "step 13, last: one ^ per line, so no g. The ^ needs a backslash, or it means the start of "
                        "the line."),
    ], "Mostly small edits, so the work is picking the cheapest keys for each, top to bottom: case and Ctrl-a for "
       "the strings and numbers, the numbered registers to carry eslint down without naming a register, one sort "
       "and two comma fixes per block, and one :s at the end for every ^."),
}
