"""Reference solutions for Project 08 (spoilers!). Each entry: exercise name -> (keys, explanation).

See one with:  python3 check.py --show N      Watch it typed:  python3 check.py --watch N
"""
SOLUTIONS = {
    "replace-last-word": ("A<C-w>np<Esc>jA<C-w>pd<Esc>jA<C-w>plt",
        "A puts you at the end of the line, and Ctrl-w deletes the word before the cursor, so "
        "A<C-w> is \"retype the last word\" in two keys. $ciw does the same in four. . can't help here, "
        "because each line needs a different alias."),
    "comment-leader": ("jo<C-u>int fd = open_dev();",
        "o on a comment line starts the new line with the comment leader \"// \", because C sets "
        "formatoptions to continue comments. Ctrl-u deletes everything before the cursor on the line, and in "
        "C the indent comes back by itself. Ctrl-w works too here: it deletes the \"// \" as one word "
        "and keeps the indent. Opening the line with O from the next line doesn't help, since that line is "
        "a comment too."),
    "indent-as-you-type": ("jA,<C-t><Esc>j.j.",
        "A, adds the comma, and Ctrl-t adds one shiftwidth of indent to the line, wherever the cursor is. "
        "Since the indent happened inside the insert, it's part of the change, so . repeats both the comma "
        "and the indent. With >> instead, . would only repeat whichever of the two you did last. Ctrl-d "
        "removes a shiftwidth the same way."),
    "one-normal-command": ("jfsi(<C-o>t/)",
        "fs jumps to sum and i( opens the parenthesis. Ctrl-o runs one Normal-mode command, here t/ (to "
        "just before the /), and returns to Insert mode at the new spot, so ) goes right after extra. "
        "<Esc>t/i) does the same with one more key: Ctrl-o saves the key that gets you back into Insert "
        "mode."),
    "do-the-math": ("j$s<C-r>=1920*1080*4<CR>",
        "$s replaces the 0. Ctrl-r = opens a prompt for an expression, and <CR> inserts its value, "
        "8294400. Any Vim expression works there: arithmetic, but also things like strlen(\"text\"). "
        "If you already know the answer, typing it is shorter, but the point is that you don't need "
        "to know it."),
    "complete-names": ("oin<C-n>();<CR>re<C-n>();",
        "o opens a line in the method, already indented. in<C-n> completes initializeConnectionPool, the "
        "only word in the file that starts with \"in\", and re<C-n> completes registerShutdownHooks. Ctrl-n "
        "searches forward through the file for words starting with what you typed (and then other open "
        "buffers), Ctrl-p backward. Typing ( ends the completion, so the <CR> after it is an ordinary "
        "new line."),
    "complete-line": ("o<CR>in<C-x><C-l><BS> {<CR>return 0;<CR>}",
        "o<CR> leaves a blank line and starts another. in<C-x><C-l> searches backward for a line that "
        "starts with \"in\" and inserts all of it: the prototype. <BS> removes the ;, and the rest is "
        "typed, with C's automatic indent placing return 0; and the closing }. If the first match isn't "
        "the line you want, Ctrl-p and Ctrl-n step through the others."),
    "literal-tab": ("GoJava<C-v><Tab>Gosling<C-v><Tab>1995",
        "With expandtab on, Tab inserts spaces. Ctrl-v inserts the next key literally, so Ctrl-v Tab is a "
        "real tab character. The same trick inserts any control character, and Ctrl-v u followed by hex "
        "digits inserts any Unicode character, like Ctrl-v u2192 for an arrow. :set noexpandtab would "
        "also work, for 10 more keys."),
    "draw-a-box": ("O<C-k>dr<C-k>dl<Esc>jo<C-k>ur<C-k>ul<Esc>8i<C-k>hh<Esc>kk.",
        "Ctrl-k plus two characters types a digraph: dr is ┌ (lines going down and right), dl is ┐, ur "
        "is └, ul is ┘ and hh is ─. Type the four corners first, then 8i<C-k>hh<Esc> fills one row with "
        "eight ─ in front of the corner, and . repeats that, count included, on the other row. "
        "r<C-k>hh works in Normal mode too, since r takes digraphs."),
    "word-under-cursor": (":%s/attempts/<C-r><C-w><CR>",
        "On the command line, Ctrl-r Ctrl-w inserts the word under the cursor, here retryCount, so you never "
        "type the new name. Ctrl-r Ctrl-a inserts the WORD instead, and Ctrl-r followed by a register name "
        "inserts that register. For the search side, * is often better, since it adds the word boundaries "
        "for you."),
    "repeat-ex-command": ("4:s/print/log.debug<CR>9j@:",
        "4: fills in the range .,.+3, which covers load(). After the :s, the cursor is on the last line it "
        "changed (line 4), and save() starts 9 lines down. @: repeats the last command line exactly as typed, "
        "so the range .,.+3 now means save(). & repeats only the substitute on one line, and :&& would "
        "need the range again."),
    "command-window": ("q:kfEcwWARN<Esc>;.<CR>",
        "q: opens the command-line window: your history, one command per line, as ordinary text. The "
        "cursor starts on the empty line at the bottom, so k goes up to the old :s. fE and cwWARN<Esc> "
        "change the first ERROR, ; and . find and change the second, and <CR> runs the line under the "
        "cursor. While typing a command, Ctrl-f opens the same window."),
    "review-thumbs-cli": ([
        ("j2faxp", "step 1: the second a on the line is the one in thumbanils, and xp swaps it with the n."),
        ("3j1920<C-a>j1080<C-a>", "step 2: adding a number to itself doubles it."),
        ("+f0C<C-r>=3840*2160*4<CR><Esc>", "steps 3 and 4 together: C replaces the 0 and the comment, and "
                                           "Ctrl-r = works out 33177600."),
        ("6j$Fxr<C-k>*X", "step 5: from the end, Fx finds the x of WIDTHxHEIGHT (not the one in 320x240), "
                          "and r takes a digraph: Ctrl-k *X is ×."),
        ("+f\"i\"-v\", <Esc>", "step 6."),
        ("fuxp", "step 7: the next u is the one in store_ture."),
        ("6+wiint(<C-o>w)<C-o>Wint(<C-o>$)<Esc>", "step 8, typed around the names in one insert: Ctrl-o w hops "
                                                  "over width to the comma, Ctrl-o W to height, and Ctrl-o $ "
                                                  "to the end of the line."),
        ("4+wi0 < <Esc>", "step 10 for the width..."),
        ("A and <C-a>he<C-p> <= MAX_H<C-p><Esc>", "...then step 9, with step 10 for the height: in Insert "
                                                  "mode, Ctrl-a types the text you inserted last, \"0 < \", "
                                                  "again. he<C-p> and MAX_H<C-p> complete height and "
                                                  "MAX_HEIGHT from the words in the file."),
        ("4j$i, 1<Esc>", "step 11."),
        ("^*cwratio<Esc>n.n.", "step 12: * jumps to the next factor, cw renames it, and n. does the other two "
                               "(n wraps around to the first one)."),
    ], "Top to bottom. The Insert-mode keys earn their place where you'd otherwise leave Insert mode or "
       "type a lot: Ctrl-r = for the arithmetic, Ctrl-o to type around a word, Ctrl-a to repeat the last "
       "insert, Ctrl-p to complete long names. Measured: typing int( and ) with <Esc>, e, W and A costs 2 "
       "more than Ctrl-o; typing \"0 < \" twice costs 3 more than Ctrl-a; typing MAX_HEIGHT and height in "
       "full costs 7 more than completing them."),
    "review-changelog": ([
        ("q:kflcwtally<CR>", "step 12, first, while the old :s is still the newest command in the history. "
                             "q: opens the history as text, k goes up to the :s, fl finds the l of ledger, and "
                             "cw changes it. <CR> runs the line, even from Insert mode."),
        ("3GA<C-w>2024-06-14<Esc>", "step 1: A<C-w> retypes the last word."),
        ("3jA`<C-o>B`<Esc>", "step 2: A` closes the backticks, Ctrl-o B jumps back to the start of Ctrl+K, "
                             "and ` opens them, all in one insert."),
        ("jfer<C-k>e'fir<C-k>i'", "step 3: r takes a digraph: e' is é and i' is í."),
        ("jA<C-w>theme<Esc>", "step 4."),
        ("vip:sor<CR>", "step 5: the paragraph includes ### Added, but # sorts before -, so it stays on top."),
        ("11Gfxr<C-k>*X", "step 6: *X is ×."),
        ("+fFi<C-k>DG<Esc>fC.", "step 7: DG is the degree sign, and . types it again before the C."),
        ("2+$Xp", "step 8: Xp swaps the last two characters, so 02 becomes 20."),
        ("3jddp", "step 9."),
        (":g/^- /s/$/.<CR>", "step 11, before the backport, so that the copy comes with its period. :g leaves "
                             "the cursor on the last entry."),
        ("o- Cr<C-x><C-l><C-p>", "step 10: Ctrl-x Ctrl-l completes a whole line from the ones that start the "
                                 "same way. The first match is the startup crash just above, and Ctrl-p goes on "
                                 "to the resize crash. It's the last edit, so its <Esc> is free."),
    ], "Edit the old command instead of retyping it, and do it before any other Ex command pushes it down "
       "the history. Digraphs type the accents and symbols, r takes them too, and the backported entry is "
       "completed, not typed. Measured: retyping the :s costs about 60 more than q:, and $ciw instead of "
       "A<C-w> costs 2 more each time."),
}
