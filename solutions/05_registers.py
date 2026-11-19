"""Reference solutions for Project 05 (spoilers!). Each entry: exercise name -> (keys, explanation).

See one with:  python3 check.py --show N      Watch it typed:  python3 check.py --watch N
"""
SOLUTIONS = {
    "black-hole": ('jddj"_ddp',
        "jdd cuts the return line into the unnamed register. j moves to the printf, and \"_dd deletes it "
        "into the black hole, so the unnamed register still holds the return. p puts it below the loop. "
        "Without the \"_, p would paste the printf back. Plain dd followed by \"2p also takes 9 keys: the "
        "second line-wise delete pushed the return line down to register 2."),
    "swap-args": ("f(ldt,wviwp0f(p",
        "f(l lands on cart, and dt, cuts cart.total(). w moves to 4200, and viwp replaces it with the cut "
        "text. Visual p also puts the text it replaced into the unnamed register, so now you're holding "
        "4200. 0f( goes back to the first paren (F( would stop at the one in total() and p puts 4200 "
        "after it. Neovim's Visual P is the opposite: it replaces without touching any register, which is "
        "what you want when you paste the same text over several things."),
    "yank-register": ("+yt(+ct(<C-r>0<Esc>+.+.",
        "+ moves to the first non-blank of the next line, and yt( yanks LOG.info into registers \" and 0. "
        "On the next line, ct( deletes System.out.println, which puts that in the unnamed register. That's "
        "why Ctrl-r \" would type System.out.println right back. Ctrl-r 0 inserts the yank instead. Then "
        "+. repeats the whole change on each line. Typing LOG.info costs 3 more keys, and the longer the "
        "text, the bigger the gap."),
    "reverse-close": ('4jdd."1p.',
        "4j goes to fclose(in). dd deletes it, and . deletes fclose(out) too. Each line-wise delete "
        "shifts the history, so now \"1 holds fclose(out) and \"2 holds fclose(in), and the cursor is on "
        "free(buf). \"1p puts fclose(out) below it, and . after a numbered put moves on to the next "
        "register, \"2. When you don't remember which number holds what, \"1p and then u. (undo, repeat "
        "with the next register) steps back through the history one delete at a time."),
    "collect-imports": ('*"Addn.n.gg"ap',
        "* on import searches for that whole word and jumps to the next one, import json. \"Add deletes "
        "the line and appends it to register a. n finds the next import, and . repeats the delete, still "
        "appending to a. gg\"ap puts all three at once, in the order you collected them. With a "
        "lowercase \"add, each . would overwrite a, and you'd end up with only the last import. Registers "
        "start empty in these exercises; in your own Neovim, clear one first with qaq before appending."),
    "class-name": ('2w"%PF.dE',
        "2w jumps to Main. \"%P puts the file name, Inventory.java, before the cursor and leaves the cursor "
        "on its last letter. F. goes back to the dot, and dE deletes the rest of that WORD, .javaMain. "
        "Project 08 teaches Ctrl-w in Insert mode, which gives an 8-key version: cw, Ctrl-r %, then Ctrl-w "
        "twice to delete \"java\" and the dot."),
    "wrap-in-float": ("j$ciWfloat(<C-r>-)<Esc>j.j.",
        "j$ puts the cursor on the end of sys.argv[1]. ciW deletes that WORD, a small delete, so it lands "
        "in \"-. Type float(, Ctrl-r - to put the WORD back, and ). The repeat is the trick: for Ctrl-r -, "
        ". reads the register again instead of retyping the old text, so each j. wraps whatever its own "
        "ciW just deleted. Ctrl-r \" looks the same on the first line, but . would type sys.argv[1] on every "
        "line. j lands inside the next WORD because each next line is shorter than the one you just grew."),
    "keep-old-name": ('wcwget_user<Esc>Go<CR><C-r>" = <C-r>.',
        "w cw get_user renames the function. That one change fills two registers: \" (and -) hold "
        "fetch_user, the word cw deleted, and . holds get_user, the text you typed. Go opens a line at the "
        "end (Python's indent rules drop the indent after a return), <CR> leaves it blank, and the two "
        "Ctrl-r's type the names for you. Ctrl-r - works as well as Ctrl-r \" here. If you had deleted a "
        "line in between, \" would hold that line, but - would still hold fetch_user."),
    "rename-param": ("3w:%s/lst/<C-r><C-w>/g<CR>",
        "3w puts the cursor on measurements. On the command line, Ctrl-r Ctrl-w inserts the word under the "
        "cursor, so the command becomes :%s/lst/measurements/g without typing the long name. % means "
        "every line, and g means every match on a line (line 2 has two). Project 07 covers :s in depth. "
        "The register lesson is that Ctrl-r works on the command line just as in Insert mode: Ctrl-r 0 "
        "would insert a yanked name the same way."),
    "constants": ("jf1y$j$i<C-r>=<C-r>0<CR>L<Esc>j^wy$j$i<C-r>=<C-r>0<CR>L",
        "jf1 lands on the first 1024, and y$ yanks the formula. j$i starts inserting before the semicolon. "
        "Ctrl-r = opens the expression prompt, which is a command line, so Ctrl-r 0 types the yanked "
        "formula into it. Enter evaluates it and inserts 1099511627776. Type L, <Esc>, and do the same "
        "again: j^w is the start of the next formula. Typing the 13-digit answer would cost more keys, "
        "and you'd need a calculator. For short math, type the expression itself: Ctrl-r =60*60*24 Enter."),
    "review-weather-script": ([
        ("3l\"%P", "step 1: \"%P puts the file name, weather.py, in front of the colon."),
        ("4j20<C-a>", "step 2: 20 Ctrl-a adds 20 to the 10."),
        ("9j<C-a>", "step 3: the only number on the BASE_URL line is the 1 in v1."),
        ("\"add2dd", "step 4: \"add cuts the line into register a, where it waits until the end. 2dd takes two "
                     "of the four blank lines left around it."),
        ("w*Rtemp<Esc>n.", "step 5: * jumps to the call in main(). week and temp are both four letters, so R "
                           "types over them, and n (wrapping around to the def) then . does the other."),
        ("jfd*cwd<Esc>N.", "step 6: * finds the second day as a whole word, so days doesn't match. cw renames "
                           "it, and N goes back to the first one for the repeat."),
        ("jdd", "step 7."),
        ("bcf)round(<C-r>-)<Esc>", "step 8: cf) cuts min(temps), a small delete, and Ctrl-r - puts it back "
                                      "inside round(...)."),
        ("W.", "step 8: . replays Ctrl-r - by reading the register again, and it holds max(temps) now."),
        ("3j\"Add2dd", "step 9: \"A appends the line to register a instead of replacing it."),
        ("2jfugUiw", "step 10: gUiw turns units into UNITS..."),
        ("dt,wviwpF(p", "step 10: ...dt, cuts it, viwp puts it over city (and city goes into the register), "
                        "and F(p puts city in front."),
        ("5G\"ap", "steps 4 and 9: \"ap puts both lines from register a under TIMEOUT."),
    ], "Register a carries the two constant lines down the file and brings them back up in one put at the "
       "end, so the cursor only goes down the file once. The small delete register does the wrapping, and "
       "the unnamed register does the swap through a Visual p."),
    "review-upload-config": ([
        ("2l\"%P", "step 1: the file name goes in front of the colon."),
        ("2j$<C-a>", "step 2: $ puts the cursor on the last 1, so Ctrl-a bumps the patch number."),
        ("6jdd5kVp", "step 3: dd cuts replicas, and Vp puts it over the debug line, which is gone without "
                     "needing a delete of its own."),
        ("<lt><lt>2<C-a>", "steps 3 and 4: << drops replicas to the top level, and 2 Ctrl-a makes it 4."),
        ("3jWC<C-r>=<C-r>-<CR><Esc>", "step 5: C cuts the formula into the small delete register. Ctrl-r = "
                                      "opens the expression prompt, Ctrl-r - types the formula into it, and "
                                      "Enter inserts 26214400."),
        ("yiW", "step 9, early: yank the value now, so \"0 still has it at the end."),
        ("+WC<C-r>=<C-r>-<CR><Esc>", "step 6, the same way. (. would put 26214400 again: it repeats the "
                                     "text that was inserted, not the formula.)"),
        ("3+W\"aD", "step 7: cut keep_ms's formula into register a..."),
        ("+WC<C-r>=<C-r>a<CR><Esc>", "steps 7 and 8: ...and evaluate it in sweep_every_ms's place. Now the "
                                     "small delete register holds sweep's old formula..."),
        ("k$a<C-r>=<C-r>-<CR><Esc>", "...which goes into keep_ms, evaluated."),
        ("4jA <C-r>0<Esc>", "step 9: Ctrl-r 0 inserts the yank from step 5."),
        ("j$ciwinfo<Esc>", "step 10, last because it ends in Insert mode."),
    ], "Every formula becomes C, then Ctrl-r = and Ctrl-r - in the expression prompt, which costs less than "
       "typing numbers this long. The swap needs no swapping at all: keep one formula in a named register "
       "and evaluate each one where the other was."),
}
