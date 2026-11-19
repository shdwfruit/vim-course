"""Reference solutions for Project 09 (spoilers!). Each entry: exercise name -> (keys, explanation).

See one with:  python3 check.py --show N      Watch it typed:  python3 check.py --watch N
"""
SOLUTIONS = {
    "move-a-method": (":e C<Tab><CR>}d3j<C-^>}P",
        ":e C<Tab> completes Config.java, the only file starting with C. } jumps to the blank line above "
        "start, and d3j deletes that line and the three below it. dap would also take the class's closing "
        "brace, because no blank line separates it from the method. Ctrl-^ jumps back to the alternate file. "
        "With no blank lines in Main.java, } goes to the last line, and P puts the method above the closing "
        "brace. Ctrl-o wouldn't work here: } was a jump, so Ctrl-o first takes you back to the top of "
        "Config.java."),
    "buffers-by-name": (":b Repo<CR>/ru<CR>xp:b Contr<CR>/il<CR>xp:b Ord<CR>/ne<CR>xp",
        ":b accepts any piece of a buffer's name, as long as only one buffer matches. :b Product would fail "
        "with E93, because three buffers match. Tab after :b cycles through the matches if you're unsure. In "
        "each file, a two-letter search lands on the first letter of the swapped pair, and xp swaps them. "
        "If you know the buffer numbers (:ls shows them), :b 4 or 4 Ctrl-^ is shorter still, and ]b steps "
        "through the list."),
    "side-by-side": ("}dap<C-w>ljp<C-w>h}jyy<C-w>l2}P$xr;",
        "} jumps to the blank line above the struct, and dap from there deletes that blank line plus the "
        "struct. In the header, jp puts it below the #define line. Back in point.c the cursor is where you "
        "left it, so }j reaches midpoint's first line. In the header, 2} lands on the blank line above "
        "#endif, P puts the copy above it, and $xr; turns the trailing \" {\" into \";\". Ctrl-w w would also "
        "stop at the task window at the top, so Ctrl-w h and l are more reliable here."),
    "follow-the-include": ("gf3}dap<C-^>p",
        "gf opens strbuf.h. It searches 'path', which starts with the directory of the current file, so the "
        "include resolves without typing util/. 3} lands on the blank line above sb_room, and dap takes that "
        "blank line plus the function. Ctrl-^ returns to strbuf.c with the cursor still on the include line, "
        "and p puts the lines below it. Ctrl-o needs two presses here, because 3} was a jump too. With 10j "
        "instead of 3}, one Ctrl-o is enough."),
    "replace-include-guards": (":args **/*.h<CR>:argdo norm Gddggcj#pragma once<CR>",
        ":args **/*.h replaces the argument list with every header in this folder and below, and opens the "
        "first one. :argdo then runs the :normal command in each: G and dd delete #endif, gg goes to the top, "
        "and cj changes the #ifndef and #define lines into one line of new text. :normal ends Insert mode for "
        "you. A :vimgrep for #ifndef would also have found list.c, which is why you pick the files by name "
        "here."),
    "open-buffers": (":bufdo %s/round_price/round_cents/ge|%s/with_tax/add_tax/ge<CR>",
        ":bufdo runs the whole line, both :s commands, in each listed buffer. legacy/report.py isn't listed, "
        "so it's safe. app.py has no round_price: without e, that first :s fails there, and an error skips the "
        "rest of the line, so app.py would keep with_tax. The second e only keeps cart.py's \"Pattern not "
        "found\" quiet. The changed buffers stay open and unsaved. :wa saves them all, and it's free because "
        "it comes after your last change."),
    "rename-everywhere": ("*:vim // **/*.[ch]<CR>:cdo s//stack_len/g<CR>",
        "* searches for \\<stack_size\\>, a whole-word pattern, so stack_size_max doesn't match. :vim // "
        "reuses the last search pattern in every .c and .h file, and fills the quickfix list with one entry "
        "per matching line. :cdo s//stack_len/g reuses it once more on each of those lines. g covers the test "
        "line that calls it twice. In real life you'd finish with :wa, or add | update to the :cdo command."),
    "match-case": ("*:vim // **/*.java<CR>:cdo s//purchase/geI<CR>",
        "* searches for \\<order\\>. It's all lowercase, so it ignores case: the quickfix list also holds lines "
        "that only mention the class Order, and plain :cdo s//purchase/g renames the class. ('smartcase' can't "
        "help, because it needs a capital letter, and * and :vimgrep ignore it anyway.) The I flag makes :s "
        "match case, so those lines don't change, and e keeps them quiet. For a clean list instead, search "
        "again with /\\C<C-r>/<CR> before :vim // (Ctrl-r / types the last search)."),
    "step-through-matches": (":vim /\\<lt>connect(\\zs/ **/*.py<CR>ct,cfg.host<Esc>]q]q.]q.]q.",
        "\\< stops disconnect( from matching, and \\zs makes each match start on the first argument. Without the "
        "j flag, :vimgrep also jumps to the first match. ct,cfg.host<Esc> replaces the argument, ]q (Neovim's "
        "built-in :cnext) moves to the next match, and . repeats the change. The second match is the def line "
        "in db.py, so you skip it with another ]q. :cdo norm ct,cfg.host would change the def too. Stepping "
        "by hand lets you decide at each match."),
    "import-once": (":vim /\\Cjson\\./ **/*.py<CR>:cfdo norm ggOimport json<CR>",
        "json\\. is all lowercase, so it ignores case and would also match \"JSON.\" in pricing.py's comment. \\C makes "
        "it match case. "
        ":cfdo runs once per file in the quickfix list. :cdo would run once per match and give app.py and "
        "store.py two imports each. :cfdo leaves the cursor on the file's first match, so gg goes to the top "
        "before O opens a line above it. :cfdo 0put ='import json' does the same thing."),
    "add-a-parameter": (":vim /\\<lt>log(/ **/*.java<CR>:cdo s/(\"/(Level.INFO, \"/e|s/(S/(Level level, S/e<CR>",
        "One :vimgrep collects the two declarations and the four calls. :cdo treats everything after it, | "
        "included, as its command, so both substitutions run at every match. On a call line the ( is followed "
        "by a quote, and on a declaration line by String. The first e is the one that matters: on a "
        "declaration line the first :s finds nothing, and without e that error would skip the second :s. The "
        "pattern (S has a capital letter, so 'smartcase' makes it match case."),
    "review-release": ([
        ("5jf8<C-a>", "step 2. From the start of the line Ctrl-a would find the 3 first, so f8 goes to the 8."),
        ("2jF0<C-a>", "step 3. The click line is shorter than the cursor's column, so j leaves the cursor on its "
                      "last character, and F0 looks back for the 0."),
        ('o"rich>=13.0",<Esc>', "step 4. o keeps the indent of the line above."),
        (":vim 4.2 **<CR>", "every 1.4.2 in the project: steps 1, 5, 6, 12 and 13, cli.py's (which step 7 replaces "
                            "anyway) and CHANGELOG.md's old heading. A pattern that starts with a letter or a digit "
                            "needs no slashes. :vimgrep jumps to the first match, that old heading, and CHANGELOG.md "
                            "is the next file to work on anyway."),
        ("7ko<CR>## 1.5.0 - 2026-11-04<Esc>", "step 15: instead of renaming Unreleased and typing another above it, "
                                              "keep it and open the new heading below it, after a blank line."),
        ("2+w<C-v>3j~", "step 16: a block over the first letters of the four bullets, and ~ capitalizes them all."),
        ("gv$A.<Esc>", "step 17: gv selects the same block again, and after $, A appends at the end of every line, "
                       "however long it is."),
        (":2,$cdo s/4.2/5.0<CR>", "the version everywhere but entry 1, the old heading. :vimgrep doesn't set the "
                                  "last search pattern, so s//5.0 would fail: give the pattern again. :cdo ends on "
                                  "the last entry, in tests/test_cli.py."),
        ("2[q", "back two entries, to cli.py's version_option line."),
        ("ci(__<C-n><Esc>", "step 7. Ctrl-n completes __version__: :cdo loaded __init__.py, and it's the only word "
                            "starting with __ in any buffer."),
        ("4-yyPf.dt $bC<C-r>.<Esc>", "step 8: copy the import line above itself, delete .count, and change count_file "
                                     "to the . register, the text you inserted last: __version__."),
        ("7j$2b4~i.<Esc>4bdawb~", "step 10, right to left: 4~ uppercases json and moves past it, i. adds the "
                                  "period, daw deletes \"the \" with its space, and ~ capitalizes print."),
        ('yi"', "yank the new help text for step 14. A yank also goes to register 0, which deletes never touch."),
        ("4jdd", "step 9."),
        ("[q2kF8<C-a>", "step 11: [q goes to README.md's entry, and the Python version is two lines up."),
        ("2[q4jo| `--json` | <C-r>0 |<Esc>", "step 14: docs/usage.md is entry 2. Ctrl-r 0 puts the help text "
                                             "yanked in cli.py."),
    ], "Seven files, so plan the trip. Do pyproject.toml first, since it's open. Then one :vimgrep for 1.4.2 lands "
       "in CHANGELOG.md, the next stop, and its list is the route for the rest: one :cdo changes the version in "
       "five files and leaves you at the end of the list, and [q walks back through cli.py, README.md and "
       "docs/usage.md. Measured: yanking __version__ from __init__.py on the way (and putting it with Ctrl-r 0) "
       "costs 4 more than completing it; f.dt $ciw instead of f.dt $bC costs 1 more; gf on docs/usage.md in "
       "README.md instead of 2[q costs 1 more."),
    "review-rename-command": ([
        (":vim done **<CR>", "six lines in four files. The first is README.md's \"When you're done\", which stays, "
                             "and :vimgrep jumps there."),
        (":2,$cdo s/done/finish<CR>", "steps 1 to 5, nearly: every entry but the first. Without g, :s changes the "
                                      "first done on a line, which is right on every line but main.c's table "
                                      "entry, where cmd_done comes second. :cdo ends on the last entry, commands.h's "
                                      "prototype."),
        (":-2,sor<CR>", "step 7: the three prototypes are this line and the two above it."),
        ("[q&", "back to main.c's table line. & repeats the last :s on this line, and now its first done is "
                "cmd_done's. The help text's comes after it, so it stays."),
        (":-2,sor<CR>3yy", "step 6. :sort leaves the cursor on the first line, so 3yy yanks the sorted table for the "
                           "README section. (vi{ would pick the braces of the entry the cursor is on, not the "
                           "table's.)"),
        ("10j2<C-x>", "step 9. Ctrl-a and Ctrl-x read the - in %-6s as a minus sign: -6 minus 2 is -8. 2 Ctrl-a "
                      "would make it -4."),
        ("G-Ous<C-x><C-l><Esc>", "step 10: Ctrl-x Ctrl-l completes the whole line usage(stderr); from the one further "
                                 "up, with this line's indent."),
        ("[q3{dapGp", "step 8, in commands.c: three { reach the blank line above cmd_list, and dap from a blank "
                      "line takes it and the function below it. Put at the end, the blank line goes between "
                      "cmd_finish and cmd_list."),
        (":cr<CR>Go<CR>## Commands<CR><Esc>\"0p", "step 11: :cr (:crewind) goes back to the first entry, in "
                                                   "README.md. \"0p puts the table yanked in main.c: dap only "
                                                   "changed the unnamed register and register 1."),
        ("qq0cf\"- `<Esc>f\"cf\"`: <Esc>f\"Djq2@q", "step 12: the macro turns one table line into a bullet. cf\" "
                                                   "replaces the indent and {\" with - `, the next cf\" replaces "
                                                   "\", cmd_add, \" with `: and D deletes \"},. j moves on, and 2@q "
                                                   "does the other two lines."),
    ], "Renaming is a job for :vimgrep and :cdo, but two of the six lines with a done keep it, and one line has "
       "two that change. The list's order (README.md, commands.c, main.c, commands.h) sets the route: :cdo ends in "
       "commands.h, [q walks back through main.c and commands.c, and :cr returns to README.md for the new section, "
       "built from a copy of the sorted table. Measured: yanking it into register a and putting it with \"ap costs "
       "2 more than letting register 0 keep it."),
}
