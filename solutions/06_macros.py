"""Reference solutions for Project 06 (spoilers!). Each entry: exercise name -> (keys, explanation).

See one with:  python3 check.py --show N      Watch it typed:  python3 check.py --watch N
"""
SOLUTIONS = {
    "first-macro": ("+qaf r(A)<Esc>q2+Q+Q",
        "+ moves to the first print. qa starts recording into register a. f<Space> jumps to the space "
        "after print, r( turns it into a paren, and A) closes the call. q stops recording. 2+ moves to "
        "the next print and Q plays the macro you just recorded; on the last print, Q plays it again. (@a "
        "and then @@ do the same in 2 more keys.) Ending the macro with a search (/pr<CR>) and then 2Q "
        "takes 17 keys, and saves you the moving by hand. That's exercise 6."),
    "count-rows": ("jqaI{ \"<Esc>f,s\", <Esc>A },<Esc>jq14Q",
        "Record the first row: I{ \" opens the brace, f, finds the comma, s\", replaces it with the closing "
        "quote and a space, and A }, closes the row. The last key, j, moves to the next row, so each "
        "replay sets up the next one, and 14Q plays it 14 times (14@a is one key more). Count exactly "
        "here: a 15th run would start with I{ \" on the }; line, which can't fail, and mangle it."),
    "grow-tree": ("qayyp0xA**<Esc>q6Q",
        "yyp copies the row below itself and puts the cursor on the copy. 0x deletes one leading space "
        "and A** adds two stars. The cursor ends on the new row, so each replay copies the row the last "
        "one made, and the trunk gets pushed down as the tree grows. 6Q makes the other six rows."),
    "gpio-numbering": ("jqayyp<C-a>$4<C-a>q6Q",
        "j goes to the PIN0 line. yyp copies it, and Ctrl-a adds 1 to the first number at or after the "
        "cursor: the 0 in PIN0. $ jumps to the end and 4 Ctrl-a adds 4 to 0x00. Ctrl-a knows hex, so 0x0c "
        "plus 4 is 0x10. 6Q replays it six times, each run copying the line the last one made. Copying "
        "the line 7 times and using g Ctrl-a on two columns (Project 04) takes about 20 keys."),
    "robust-fields": ("jqa$byiwSthis.<C-r>0 = <C-r>0;<Esc>jq4Q",
        "$b finds the field name on any line: jump to the end, then back one word, whatever the type "
        "looks like. yiw yanks it, and S replaces the whole line but keeps its indent. this.<C-r>0 = "
        "<C-r>0; types the assignment with the yank twice. (Ctrl-r \" would insert the line S just "
        "deleted.) A macro that counts words, like ^d2w, falls apart on List<String> and Map<String, "
        "Integer>, because <, > and the comma count as words of their own."),
    "search-ifdef": ("qa/pri<CR>O#ifdef DEBUG<Esc>jo#endif<Esc>q2Q",
        "The macro starts with /pri<CR>, so wherever it starts, it jumps to the next printf. O opens a "
        "line above (C indenting moves a typed # to column 1), and jo opens one below the printf. The "
        "cursor ends on the #endif, so the next run's search finds the next printf, and 2Q wraps the "
        "other two. :g/pri/norm with the same keys takes 36, because an <Esc> on the command line has to "
        "be typed as Ctrl-v <Esc>."),
    "recursive-dict": ("jqaqqa0f=a\"<Esc>A\",<Esc>j@aqQ",
        "qaq records nothing into a, which empties it. Then record the first row: 0f= finds the =, a\" "
        "opens the quote, A\", closes it, j moves down, and @a calls the macro. While you're recording, a "
        "is still empty, so that @a does nothing. The final Q (the macro you just recorded; @a works too) "
        "runs it for real: each run starts the next, until 0f= fails on the closing paren and everything "
        "stops before changing anything. A count (5Q, or 99Q) also stops at the first failure and is 3 or "
        "4 keys shorter here; recursion saves you counting. Registers start empty in these exercises, but "
        "always qaq in your own Neovim."),
    "edit-macro": ("fF~0y$dd5@0",
        "Read the macro: I inserts cfg.put(\", then F, searches backward for a comma, but the comma is "
        "ahead of the cursor, so the macro would stop there. fF jumps to the F and ~ makes it f. 0y$ "
        "yanks the line without its line break into the yank register, and dd deletes it (deletes never "
        "touch \"0). Any register can be played, so 5@0 converts all five rows. (Q can't play it: Q plays "
        "the macro you last recorded, and this one was only yanked.) You'd normally keep a macro in a "
        "letter: 0\"ay$, then @a. Don't yank it with yy: the line break becomes part of the macro and acts "
        "like an extra j, so every other row gets skipped."),
    "normal-table": ("qa3f,s | <Esc>F,.;.I| <Esc>A |<Esc>q:%norm Q<CR>",
        "The macro starts with 3f,, which needs three commas, so on a short row it fails before changing "
        "anything. From the third comma it works backward: s | <Esc> replaces it, F, and . do the second, "
        "; and . the first. I| and A | add the outer bars. :%norm Q then runs the macro you just recorded "
        "on every line (:%norm @a is one key more), starting at column 1. Where it fails (the short rows, "
        "and rows already converted, which have no commas left), it just skips that line. A count would "
        "stop for good at grace. A search for three commas inside the macro (/,.*,.*,<CR>) and a count "
        "also work, in a key fewer."),
    "append-macro": ("qajIPerson(\"<Esc>f,s\", <Esc>A),<Esc>q2QjQqAhi, admin=True<Esc>q2Q",
        "This macro starts by moving (j) and then converts the row, so it doesn't end with a move. That "
        "matters for qA. Record it from the people = [ line and replay it twice with 2Q. j steps over the "
        "# admins comment, and Q converts linus. Now qA records more keys onto the end of a: h steps onto "
        "the ), and i, admin=True<Esc> adds the argument. 2Q runs the longer macro on ken and dennis "
        "(after qA, Q plays a with the added keys). Recording a second macro from scratch would mean "
        "typing the conversion again: about 20 more keys."),
    "enum-finale": ("jqa^yegUef,s(\"<C-r>0\", <Esc>A),<Esc>jq14Q",
        "^ puts the cursor on the name, whatever column j left it in. ye yanks the name, and gUe "
        "uppercases it in place. f, finds the comma, and s(\"<C-r>0\", replaces it with the paren and the "
        "lowercase name from the yank register. A), closes the constant and j moves on. 14Q does the "
        "other fourteen rows. A single :s with groups and \\U (Project 07) does it in about 40 keys, and "
        "it's harder to get right on the first try."),
    "review-error-table": ([
        ("4jyyp3fdcwbool<Esc>", "step 1: yyp copies the <stddef.h> line below itself. The third d on the line is "
                                "the one that starts def, and cw changes def to bool."),
        ("2j<C-a>", "step 2: Ctrl-a finds the first number at or after the cursor, the 3."),
        ("6jFAXp", "step 3: the cursor lands past the end of the short ERR_PRASE line, so FA searches back "
                   "for the A. X deletes the R before it and p puts it back after the A: Project 00's swap, "
                   "done from the other side."),
        ("3joERR_TLS,<Esc>", "step 4: o opens a line under ERR_AUTH, already indented."),
        ("yi{}jjp", "step 5 starts with a copy: yi{ yanks the lines between the enum's braces and leaves the "
                    "cursor on the first one. } goes to the blank line after the enum, jj to the table's "
                    "first line, and p puts the eight codes inside the table."),
        ("kwywf*p", "step 6: const is already on that line. yw yanks it with its space, and f*p puts it "
                    "after the *."),
        ("jqa^4s\"<Esc>gueea\"<Esc>jq7Q", "step 5 again: record one line. ^4s\" replaces ERR_ with the opening "
                                          "quote, gue lowercases from the quote to the end of the name, ea\" "
                                          "closes the string, and j moves to the next line, so 7Q does the "
                                          "other seven."),
        ("2+2wcwbool<Esc>", "step 7: + goes to the start of a line, wherever the macro left the cursor."),
        ("2j$FRcwIO<Esc>", "step 8: from the ; at the end, FR finds the R of REFUSED, and cw changes the rest "
                           "of the word. ERR_ stays."),
        ("3+<C-v>jIextern <Esc>", "step 9: a Visual block down the first column of the two lines, and I types "
                                  "extern on both."),
        ("flibuf<Esc>", "step 10: the first l on the line is the one in len."),
        ("F(ly2e", "step 11: yank enum netd_err from netd_strerror()'s parameters..."),
        ("jfiviwp", "...and put it over int: fi finds it, viw selects it and p replaces it."),
        ("jgcc", "step 12: gcc comments out the line. Neovim treats .h files as C++, so it uses //."),
    ], "Top to bottom, fixing the enum before it's copied, so the table gets ERR_PARSE and ERR_TLS for free. "
       "The eight names differ only in the code, so they're one recorded line and a count, not eight lines "
       "of typing. And text that's already in the file is reused: const and enum netd_err are yanked and "
       "put. Measured: f*aconst <Esc> costs 4 more than yanking it, and typing enum netd_err 6 more."),
    "review-seed-data": ([
        ("jgUeG.6G", "step 1: gUe uppercases begin, and . does the same to commit, on the last line. 6G goes "
                     "to user 2's row."),
        ("fmxp", "step 2: fm finds the m of exmaple, and xp swaps it with the a."),
        ("$r,", "half of step 4: user 2 won't be the last row any more, so its ; becomes a comma before it "
                "gets copied."),
        ("qayyp<C-a>f'<C-a>q5Q", "step 3, the counter macro: yyp copies the row, Ctrl-a adds 1 to the first "
                                 "number on it (the id), f' moves into the email, and the next Ctrl-a turns "
                                 "02 into 03, keeping the zero. 5Q makes users 4 to 8."),
        ("$r;", "the rest of step 4: the last row ends the statement."),
        ("2+Y", "Copy the products statement's first line for step 10. In Neovim, Y copies to the end of "
                "the line, here all of it."),
        ("2+f,50<C-a>", "step 5: Ctrl-a changes the first number at or after the cursor, so start after "
                        "SKU-1002, on the first comma. A count adds that much."),
        ("+gUi'", "step 6: i' finds the first quoted string on the line even when the cursor is before it."),
        ("fda'<Esc>", "step 7: double the quote after Kid."),
        ("2+$d/;<CR>", "step 9: from the comma at the end of the desk lamp's row, d/; deletes up to the ; at "
                       "the end of the next line: the comma, the line break and all of SKU-1006's row."),
        ("F,500<C-x>", "step 8: back to the comma before the price, and Ctrl-x takes 500 off."),
        ("2jV\"0p", "step 10: V\"0p puts the yanked line over the comment. The delete went into the unnamed "
                    "register, but \"0 still holds the yank."),
        ("2wct)tags (name<Esc>", "...and ct) changes products (sku, name, price_cents into tags (name."),
        ("jqa>>I('<Esc>A'),<Esc>jq5Q", "step 11, a second macro: >> indents, I(' and A'), wrap the tag, and j "
                                       "moves on. 5Q does the other five."),
        ("k$r;", "step 12."),
    ], "Fix user 2 before copying it, so the copies come out right. A macro that copies a row and bumps "
       "both numbers with Ctrl-a writes the new users, and a second macro turns the tags into rows. Counts "
       "on Ctrl-a and Ctrl-x do the arithmetic. Measured: typing the tags statement's first line costs 10 "
       "more than putting the products line over the comment and changing it (and SQL's indenting moves "
       "it while you type); $r;jdd costs 3 more than d/; for SKU-1006; Visual-block inserts for the tags "
       "cost 4 more than the macro."),
}
