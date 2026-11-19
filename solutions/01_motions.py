"""Reference solutions for Project 01 (spoilers!). Each entry: exercise name -> (keys, explanation).

See one with:  python3 check.py --show N      Watch it typed:  python3 check.py --watch N
"""
SOLUTIONS = {
    "drop-argument": ("3WdW",
        "Each argument is one WORD (letters and punctuation up to a space), so 3W lands on linewidth "
        "and dW deletes that WORD plus the space after it. With small words you'd need 10w to get "
        "there, because every run of punctuation, like ( or , or =\", counts as a word too."),
    "return-it": ("c^return ",
        "^ is the first non-blank character of the line, so c^ changes everything from there up to "
        "(not including) the cursor. The indentation stays, and so does the string under the cursor. "
        "d0 or c0 would also eat the indentation. ^c3Wreturn works too, one key longer."),
    "drop-sort": ("F.dF.",
        "F. jumps back to the dot before toList. From there, dF. deletes back to the previous dot. "
        "Backward motions are exclusive: the character under the cursor is never included, so the "
        "dot of .toList() survives and exactly \".sorted()\" goes. 2F.dt. also works, in 6 keys."),
    "match-bracket": ("$c%sd",
        "$ lands on the last closing parenthesis, and % jumps to the ( that matches it, skipping the "
        "pair inside stdev(xs). As a motion, % is inclusive, so c% changes both parentheses and "
        "everything between. Without % you'd be counting parentheses: 3f(Csd is one key longer."),
    "double-pattern": ("yGP",
        "yG yanks from the current line to the last line, which here is the whole file, line-wise. "
        "P puts line-wise text above the cursor's line, so the copy lands on top and the pattern is "
        "twice as tall. yGGp does the same in one more key."),
    "move-main": ("}d}Gp",
        "} jumps to the blank line under the #include. d} from a blank line deletes up to the next "
        "blank line, and because the motion starts and ends in column 1 it becomes line-wise: the "
        "blank line and all of main() go into the register. G goes to the last line and p puts them "
        "below it, blank line first. jd4jGp also works, one key longer, if you count the lines right."),
    "delete-to-word": ("fxd/m<CR>",
        "fx moves to the first x. d/m<CR> deletes from there up to (not including) the next m, "
        "joining the three lines into one. The only m in the way is the one in map, so one letter "
        "is a long enough pattern. A search is the motion to reach for when the target is lines "
        "away and you'd rather not count."),
    "delete-back": ("d?,<CR>",
        "?, searches backward for a comma, and d?,<CR> deletes from the comma up to the cursor. The "
        "motion is exclusive, so the period under the cursor stays and becomes the end of the first "
        "sentence. f, F, t and T can't do this, because they never leave the current line."),
    "rename-variable": ("*cwsize<Esc>n.n.",
        "* searches forward for \\<tmp\\>, the whole word, so it skips tmpdir and lands on line 4. "
        "cw changes that tmp. n goes to the next match and . repeats the change, and the second n "
        "wraps around to the tmp you started on. There's no need to go back first. (*cgnsize<Esc>.. "
        "is one key shorter: gn selects the next match, so . does the n for you.)"),
    "fetch-and-return": ("/f<CR>yE<C-o>p",
        "/f<CR> jumps to the next f, which is the start of formatSummaryLine. yE yanks to the end of "
        "the WORD, parentheses included. A search is a jump, so Ctrl-o goes back to the exact spot "
        "you searched from, and p puts the name after the (. `` works too, one key longer. In "
        "Project 08, Insert-mode completion (Ctrl-n) types long names for you."),

    "review-inventory": ([
        ("ddp", "step 1."),
        ("jjwifinal <Esc>", "step 2: w hops over public to class."),
        ("j.", "step 3: j keeps the column, which is on List, and . types final  again."),
        ("2fnyt)", "for step 8, while the cursor is here: the second n on the line starts new, and yt) yanks "
                   "new ArrayList<>( up to the ). A yank isn't a change, so . still types final ."),
        ("j4B.", "step 3 for limit: j lands on the ; at the end of the shorter line, and four WORDs back is int."),
        ("G2kFiP", "step 8: G and 2k reach all()'s return, Fi goes back to items, and P puts new ArrayList<>( "
                   "in front of it."),
        ("$i)<Esc>", "$ then i) closes the call before the ;."),
        ("/m)<CR>", "step 6: the first m) after the cursor is in item) in add(). The search wraps around past "
                    "the end of the file."),
        ("*cwname<Esc>", "* searches for the whole word item, so items never matches, and jumps to the next one. "
                         "cw renames it."),
        ("n.n.n.n.", "n and . for the other four, the one in the message included. The last n wraps around to "
                     "the parameter itself."),
        ("/><CR>a=<Esc>", "step 7: the next > is the one in the size check."),
        ("2T(yt ", "for step 4: 2T( goes back to just after the second ( behind the cursor, the start of "
                   "items.size(), and yt<Space> yanks it."),
        ("?n;<CR>Plx", "step 4: ?n; finds count()'s return n;. P puts items.size() before the n, and lx deletes "
                       "the n."),
        ("kd3k", "then the four lines that count go."),
        ("{d}", "step 5: { goes up to the blank line above count(). From there d} cuts that line and the "
                "method, line-wise."),
        ("}}P", "two } reach the blank line after remove(), and P puts count() above it, blank line first."),
    ], "The edits are spread out, so the motions do the work: searches and G to get near, a WORD count or F "
       "to land on the exact spot, and { and } to step over whole methods. Both bits of code the edits need, "
       "new ArrayList<>( and items.size(), are already in the file: yank each where it is and put it where it "
       "goes before anything else is deleted. Measured: yanking new ArrayList<>( at the end instead, with "
       "?w A and coming back with Ctrl-o, costs 2 more; typing items.size() over the n costs 5 more."),
    "review-ring": ([
        ("ddp", "step 2 first: dd cuts stdlib.h and p puts it below stdio.h..."),
        ("jdd", "step 1: ...which leaves string.h right below, to delete."),
        ("jf1R64<Esc>", "step 3: R types 64 over 16."),
        ("/((r<CR>", "step 4: the search lands on the second of the three (, the one that opens the extra pair."),
        ("%x``x", "% jumps to its partner after CAP, and x deletes it. `` jumps back to where the % started "
                  "(Ctrl-o can't, because the jump list keeps only one place per line), and x deletes the (."),
        ("kIstatic <Esc>", "step 5: I types at the start of the line."),
        ("}j.", "step 6: } jumps to the blank line after ring_push(), and . types static  again."),
        ("/2<CR>cwCAP<Esc>", "step 7: there's no other 2 between here and the 20."),
        ("3jdd4kp", "step 8: dd cuts int v; and p puts it below r."),
        ("/\\\\<CR>xr ", "step 9: a backslash is special in a search, so \\\\ finds a real one. x deletes it, and "
                       "r<Space> turns the n into a space."),
        ("joputchar('\\n');", "step 10, last, so its <Esc> is free. o on the loop's } opens an indented line "
                              "below it."),
    ], "Top to bottom, except for the includes: sorting them first leaves string.h right where the cursor is. "
       "% finds a parenthesis's partner however deep it's nested, and `` gets back to the exact spot. Both "
       "statics are one I and a ., with } to step from one function to the next. Measured: deleting string.h "
       "first and then sorting with gg costs 3 more; /20 instead of /2 costs 1 more."),
}
