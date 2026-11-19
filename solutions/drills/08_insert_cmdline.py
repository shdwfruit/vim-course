"""Reference solutions for Project 08's drills (spoilers!). Each entry: drill -> (keys, explanation).

See one with:  python3 check.py drill ctrl-w --show 3      Watch it typed:  python3 check.py drill ctrl-w --watch 3
"""
SOLUTIONS = {
    # ---------- Ctrl-w Ctrl-u Ctrl-h ----------
    "ctrl-w-1": ("A<C-w>nvim",
        "A starts Insert mode at the end of the line, and Ctrl-w deletes nano. It stops at the =, which isn't "
        "a word character. $ciw does the same, but needs four keys before the typing instead of two."),
    "ctrl-w-2": ("A<C-w>email",
        "Ctrl-w deletes back to the start of the word, and the dot isn't part of it, so only name goes. A "
        "second Ctrl-w would delete the dot, and a third user."),
    "ctrl-w-3": ("jo<C-w>hugo --minify",
        "o on a comment line starts the new line with \"# \", because the shell's settings continue comments. "
        "Ctrl-w skips the space and deletes the #, which leaves an empty line to type on. O on the next line "
        "would continue that comment too. Ctrl-u works the same here."),
    "ctrl-w-4": ("A<C-w><C-w><C-h>, scipy",
        "The first Ctrl-w deletes np, the second skips the space and deletes as, and Ctrl-h deletes the space "
        "that's left after numpy. 2f C (or eelC) followed by the same typing is also 11 keys."),
    "ctrl-w-5": ("jA<C-w>true<Esc>j.j.",
        "A<C-w>true is one insert, so . repeats the whole thing: append, delete the last word, type true. "
        "It works on lines of any length, because A always goes to the end. $ciwtrue<Esc> with j. needs two "
        "more keys."),
    "ctrl-w-6": ("A<C-w>alpine<CR>RUN apk add gcc",
        "Ctrl-w deletes slim and stops at the -. Since you're still in Insert mode, <CR> and the next line "
        "follow straight on. fsCalpine<Esc>o and the same line is two keys longer."),
    "ctrl-w-7": ("Go<C-u>- Usage",
        "o copies the indent of the line above, 8 spaces here. On a line that's only indent, Ctrl-u deletes "
        "all of it, where Ctrl-d would take two presses (and 0 Ctrl-d two keys). Ctrl-w also clears it in one."),
    "ctrl-w-8": ("jjo<C-u>[server]<CR>port = 8080<CR>E<C-p>",
        "o starts the line with the cat line's 8 spaces of indent, and Ctrl-u wipes them in one key. The next "
        "lines copy the indent of the line before them, which is now none, so they start at column 0 too. "
        "EOF is already on the cat line, so E and Ctrl-p complete it (typing it is one key more)."),
    "ctrl-w-9": ("A<C-h> {<CR>p->used = 0;<CR>}",
        "A then Ctrl-h deletes the ; and leaves you typing in its place. C's indenting puts the body one level "
        "in and moves the } back out as you type it. $s does the same as A<C-h>, in the same two keys."),
    "ctrl-w-10": ("jA<C-w>D<C-p><Esc>j.",
        "A<C-w> deletes the 10, and D<C-p> completes DEFAULT_TIMEOUT from line 1, the only word starting with "
        "a D. The completed text is part of the insert, so j. repeats it all on the next line. "
        "Yanking the name and using Ctrl-r 0 takes three keys more."),
    "ctrl-w-11": ("GA<C-w>id_ed25519",
        "G goes to the last line and A to its end. id_rsa is one word, since an underscore is a word character, "
        "but the / before it isn't, so Ctrl-w deletes just id_rsa. $ciw or $bC before the typing costs two keys "
        "more."),
    "ctrl-w-12": ("A<C-w> to web1\"",
        "The three dots and the closing quote are all non-word characters, so one Ctrl-w deletes the whole run "
        "and stops at the g of Deploying. Then you type the rest, quote included. f.C does the same deleting in "
        "one key more."),
    "ctrl-w-13": ("O<C-h>!/bin/sh",
        "O on a comment line starts the new line with the shell's comment leader, \"# \". Ctrl-h deletes just "
        "the space, so the # stays and you type the rest of #!/bin/sh after it. O<C-w> and typing the # again "
        "is one key longer."),
    "ctrl-w-14": ("A<C-w>changeme<Esc>j.j.",
        "A<C-w>changeme deletes the value, however long it is, and types the new one, all in one insert. j. "
        "repeats that on each line below, since A always starts at the end. :%s/=.*/=changeme is three keys "
        "longer."),
    "ctrl-w-15": ("Go<C-u>---",
        "o under the image line starts with its six spaces of indent. Ctrl-u deletes the whole indent in one "
        "key; Ctrl-d or Backspace would take three presses (shiftwidth is 2 in YAML). Go<Esc>i--- also works, "
        "since Esc removes an indent you didn't type into, but costs a key more."),
    "ctrl-w-16": ("A early<CR><C-w>validate(o<C-p>);",
        "A appends to the comment, and Enter continues it on the new line, which starts with \"// \" at the "
        "comment's indent. Ctrl-w deletes the // and leaves the indent (Ctrl-u does the same here). o<C-p> "
        "completes order, the nearest word above starting with o. <Esc>o in place of <CR> is a key more."),
    "ctrl-w-17": ("A<C-w>Role<CR>email: s<C-p>",
        "Ctrl-w deletes string, Role goes in its place, and Enter opens the next line at the same indent. s<C-p> "
        "completes string from the line above. fsC instead of A<C-w> is a key more."),
    "ctrl-w-18": ("A<C-w>inactive<C-o>2F,<C-w>manager",
        "A<C-w> swaps active for inactive. Still in Insert mode, Ctrl-o 2F, jumps back two commas, to the one "
        "right after engineer, and the typing goes in front of it, so Ctrl-w deletes engineer. Doing the role "
        "first (3f,i<C-w> or 3f,cb, then <C-o>$ or <Esc>A for the status) is a key longer: getting around "
        "costs A plus Ctrl-o 2F, here, five keys, against six for 3f,i plus Ctrl-o $."),
    "ctrl-w-19": ("jjo<C-w>assert_held(&q->l<C-p>);<Esc>6j.",
        "o on the comment line starts the new line with \"// \", and Ctrl-w deletes it, keeping the indent. "
        "l<C-p> completes lock from the comment. The whole insert, Ctrl-w included, is one change, so after 6j "
        "reaches the second comment, . adds the same line below it. Ctrl-u in place of Ctrl-w ties."),
    "ctrl-w-20": ("Go<C-u><CR><CR>if __name__ == \"__main__\":<CR>m<C-p>(s<C-p>.a<C-p>)",
        "o starts the line with print's eight spaces of indent, and Ctrl-u deletes them all. The two Enters "
        "leave two blank lines, and the line after them starts at column 0 as well. After the colon, Python "
        "indents the next line by 4. m, s and a with Ctrl-p complete main, sys and argv. Go<CR><CR> first and "
        "Ctrl-u on the third line ties: Python gives that line print's indent again, but one Ctrl-u clears it."),

    # ---------- Ctrl-n Ctrl-p ----------
    "complete-1": ("$im<C-n>",
        "$ goes to the ;, and i inserts in front of it. One letter is enough when only one word starts with "
        "it: Ctrl-n puts maxConnectionsPerHost in at once. The <Esc> afterwards is free."),
    "complete-2": ("cwi<C-p>",
        "cw replaces TBD. i matches Internationalization because ignorecase is on, and Ctrl-p searches "
        "upward, so the heading comes first. Ctrl-n would search forward and find is first."),
    "complete-3": ("$iu<C-p>",
        "Ctrl-p searches backward, so the nearest match above comes first: user_cache, on line 2. Ctrl-n "
        "searches forward and wraps around to the top, so it would find user_count first and need a second "
        "press."),
    "complete-4": ("f)ig<C-p><C-p>()",
        "f)i puts you between the parentheses. g matches all three getters; Ctrl-p finds getUserPhone first "
        "(the nearest above) and the second Ctrl-p steps to getUserEmail. From the other end, Ctrl-n Ctrl-n "
        "would reach it too, through getUserName."),
    "complete-5": ("wcwrel<C-n>",
        "w moves onto free and cw replaces it. With re, release_buffer is the third match in either direction, "
        "but rel matches nothing else, so one more letter saves a key over two more presses. (r and three "
        "Ctrl-p is the same length.)"),
    "complete-6": ("f(iC<C-p><lt>>",
        "f( lands on the (, and i types in front of it. A lowercase c would match class first (the nearest "
        "above), but smartcase makes a capital letter match case exactly, and ConcurrentHashMap is the only "
        "word starting with C. co<C-p> works too, a key longer."),
    "complete-7": ("A c->r<C-n> <lt> c->m<C-n>;",
        "Completion works after -> like anywhere else. For r, Ctrl-p would find return, the nearest match "
        "before the cursor, on this very line; Ctrl-n searches forward, wraps around and finds retry_count on "
        "line 1 first. m matches only max_retries."),
    "complete-8": ("A u<C-p> * q<C-p> * (1 - d<C-p>)",
        "Each parameter is one letter and Ctrl-p. d also matches def, but searching backward from the end of "
        "line 1, discount_rate comes first. After a completion, typing a space or a ) simply carries on with "
        "the insert; there's nothing to confirm."),
    "complete-9": ("j$i, encoding=D<C-p><Esc>j.j.",
        "$i inserts in front of the ), and D<C-p> completes DEFAULT_ENCODING (a capital D matches it alone). "
        "The completed word is part of the insert, so . types all of it again. After the first line, the "
        "cursor sits far to the right, so j lands on the ) at the end of each shorter line below."),
    "complete-10": ("or<C-p> s<C-p>().add(sh<C-p>).subtract(d<C-p>);",
        "o opens a line inside total(), already indented. return, subtotalBeforeTax, shippingCost and "
        "discountAmount are all in the file, so a letter or two and Ctrl-p type each one: s finds "
        "subtotalBeforeTax first, but by the time you want shippingCost, subtotalBeforeTax is nearer, so that "
        "one needs sh. subtract isn't in the file, so it's typed in full."),
    "complete-11": ("$i$D<C-n>",
        "$i inserts in front of the closing quote. The $ isn't a word character, so completion works on the D "
        "after it. A capital D makes the match exact, but Deploying matches too, and Ctrl-p, looking back, finds "
        "it first. Ctrl-n searches forward, wraps around to line 1 and finds DEPLOY_ENVIRONMENT. DE<C-p> is a "
        "key longer."),
    "complete-12": ("f)i-<C-p>",
        "f)i puts you between the parentheses. CSS counts - as a word character, so a single - is enough to "
        "start a word, and completion fills in the whole --color-primary-dark: it's the nearest match above. "
        "Typing -- first changes nothing but costs a key."),
    "complete-13": ("A w<C-p> * h<C-p>",
        "Ctrl-p looks back from the cursor first, and width and height are right there on the same line, so "
        "each takes a letter and one Ctrl-p."),
    "complete-14": ("cwD<C-p>",
        "cw replaces TBD. Nothing above the cursor starts with a capital D, so Ctrl-p wraps around to the end of "
        "the file and searches upward from there: Dragonfly, the last word, comes first. Ctrl-n searches down and "
        "finds Details first, so it needs Dr<C-n>, a key more."),
    "complete-15": ("f\"ab<C-p>-a<C-p>",
        "f\"a puts you inside the empty quotes. In HTML - isn't a word character, so billing-address is two "
        "words: complete billing, type the -, complete address. Backward from here, Ctrl-p wraps around to the "
        "end of line 2 and finds the lowercase words there first; Ctrl-n would find the label's Billing, with a "
        "capital B."),
    "complete-16": ("w<C-v>3jIo<C-p>.<Esc>",
        "w moves from SELECT to product_id on the next line. Ctrl-v 3j makes a block down the four columns, and "
        "I types in front of it. o<C-p> wraps around backward to the last word in the file, order_items, and "
        "<Esc> copies the whole insert, completion and dot, to every line of the block. wIo<C-p>.<Esc> and j. on "
        "the other three lines is three keys longer."),
    "complete-17": ("A m<C-p><C-h> in m<C-n>:",
        "m<C-p> completes migrations, the only m word in the file, and Ctrl-h deletes its s. For the plural, "
        "Ctrl-p would now find the migration you just made, the nearest match back; Ctrl-n searches forward, "
        "wraps around and finds migrations on line 1. m<C-p>s or m<C-p><C-p> is a key longer."),
    "complete-18": ("$ir<C-n>(&o<C-p>)",
        "$i inserts in front of the ;. The functions are defined after main, so Ctrl-n, searching forward, meets "
        "run_tests before any other word starting with r. Ctrl-p would find return on this very line. For opts "
        "it's the other way round: Ctrl-p finds it on the line just above. ru<C-p> would wrap around to "
        "run_benchmark, the last function, and need a second press."),
    "complete-19": ("*<C-v>3j$A D<C-p>;<Esc>",
        "* on const jumps to the next const, at the start of line 3 (jj works too, a key longer). Ctrl-v 3j "
        "selects the four lines, and $ makes the block reach the end of each one, however long. A appends there: "
        "D<C-p> completes DEFAULT_REQUEST_TIMEOUT_MS (a capital D matches it alone), and <Esc> adds the same "
        "text to the other lines. A on one line, then j. on each of the others, is two keys longer."),
    "complete-20": ("GA (s<C-n>.su<C-n> - s<C-n>.di<C-n>) * (1 + s<C-n>.t<C-n>)",
        "From the end of the file, Ctrl-n wraps around to the top and searches down, so it meets the names on the "
        "__init__ line first: s gives self, t gives tax_rate. su is needed for subtotal (s alone is self) and di "
        "for discount (d alone is def). Ctrl-p looks back instead, through the words you've just typed and the "
        "def total(self) line, so it needs se, ta and di: three keys more. d<C-n><C-n> ties with di<C-n>."),

    # ---------- Ctrl-o ----------
    "ctrl-o-1": ("wi`<C-o>tf`",
        "wi` opens the code span. Ctrl-o tf runs one Normal-mode motion, to just before the f of first, and "
        "puts you back in Insert mode there, right after install. <Esc>eea` takes a key more."),
    "ctrl-o-2": ("ea.info<C-o>$;",
        "ea appends after log, and Ctrl-o $ moves to the end of the line without leaving Insert mode, so the "
        "; goes after the ). <Esc>A; is exactly as long: for the end of a line, Ctrl-o $ and <Esc>A are a "
        "tie."),
    "ctrl-o-3": ("jf,a\"<C-o>t1\"",
        "a\" opens the quote after the first comma. Ctrl-o t1 jumps to the comma just before 1815, and the "
        "closing quote goes in front of it. The same with <Esc> needs t1i\" or 3ea\": one key more."),
    "ctrl-o-4": ("A)<C-o>Fpround(",
        "Start at the end: A) closes the call. Ctrl-o Fp searches backward to the p of price and leaves you "
        "typing in front of it. Opening first (fpiround(, then <Esc>A) or Ctrl-o $) is one key longer."),
    "ctrl-o-5": ("fvimin(<C-o>f))",
        "fv lands on value, and imin( opens the inner call. Ctrl-o f) jumps to the ) and leaves you just "
        "before it, where the second ) goes. With <Esc> it's f)i), one key more."),
    "ctrl-o-6": ("f(i(!<C-o>%)",
        "f( lands on the condition's opening parenthesis, and i(! types in front of it, so the cursor is still "
        "on it. Ctrl-o % jumps to its partner, and the extra ) goes there. Typing a(! after the ( instead "
        "would leave % with the wrong parenthesis."),
    "ctrl-o-7": ("wiDISTINCT <C-o>2wactive_",
        "After DISTINCT and a space you're in front of name. Ctrl-o 2w moves two words on, to users, and "
        "active_ goes in front of it. Ctrl-o fu is the same length. With <Esc> you'd need 3wi: a key more."),
    "ctrl-o-8": ("jf_RName<C-o>;Age ",
        "R types over the blanks, so the table keeps its width. Ctrl-o works in Replace mode too: ; repeats "
        "the f_ from before and drops you back into Replace mode at the second cell, where \"Age \" covers "
        "the four blanks."),
    "ctrl-o-9": ("jfti<lt>a href=\"/guide\"><C-o>tf<lt>/a>",
        "ft lands on the t of the, and i types the opening tag in front of it. Ctrl-o tf jumps to the space "
        "before first, and the closing tag goes in front of it. With <Esc> you'd need eea: one key more."),
    "ctrl-o-10": ("fea.strip()<C-o>fcstr(<C-o>$)",
        "fe lands on the e of name, and a appends .strip(). Ctrl-o fc jumps to count, where str( goes, and "
        "Ctrl-o $ to the end of the line for the closing ). All three edits are one stay in Insert mode."),
    "ctrl-o-11": ("A;<C-o>Bawait ",
        "A; adds the semicolon. Ctrl-o B moves back to the start of the WORD response.json(); and leaves you in "
        "Insert mode in front of it, where await and a space go. With <Esc>Bi it's a key more, and so is typing "
        "await first and then <Esc>A;."),
    "ctrl-o-12": ("ea<lt>String, Integer><C-o>f(<lt>>",
        "ea appends right after Map. Ctrl-o f( jumps to the parenthesis after HashMap, and the typing carries on in "
        "front of it, so <> lands between HashMap and (. <Esc>f(i<> is one key longer."),
    "ctrl-o-13": ("f)i, role<C-o>;, 'admin'",
        "f)i puts the new column in front of the first ). Ctrl-o ; repeats the f) from where the typing is, so it "
        "finds the next ), after 'Ada', and the value goes in front of it. After <Esc> the cursor would step back "
        "onto role, and ; would find the first ) again: you'd need ;; and i, two keys more."),
    "ctrl-o-14": ("4wRPASSED<C-o>f042",
        "The top border is one long word of punctuation, so 4w goes through |, build and : to FAILED. R types "
        "PASSED over it, keeping the width. Ctrl-o f0 jumps to the 0 and puts you back in Replace mode, where 42 "
        "covers the 0 and one space, so the right border stays put. <Esc>f0R42 is a key more."),
    "ctrl-o-15": ("fsaS<C-o>fh--fail ",
        "fs lands on the s of -s, and a appends the S. The URL starts with the only h on the line, so Ctrl-o fh "
        "puts the typing right in front of it. Ctrl-o 3W gets there in the same number of keys; with <Esc> it's "
        "one more."),
    "ctrl-o-16": ("/ =<CR>i: number<C-o>n: string<C-o>n: boolean",
        "/ = finds the space before the = on line 1, and i types the annotation in front of it. Ctrl-o n jumps to "
        "the next match, on the next line, and puts you back in Insert mode there: no <Esc> and no i, two keys "
        "saved each time. 2ea on each line, with <Esc>+ in between, is four keys longer."),
    "ctrl-o-17": ("$biMath.round(<C-o>%)",
        "$ lands on the ( at the end of line 1, b goes back to sum, and i types Math.round( in front of it. The "
        "cursor is then on the s, not on a bracket, so Ctrl-o % looks ahead on the line for one, finds sum's ( "
        "and jumps to its partner two lines down. The second ) goes in front of it. <Esc>l%a) instead is two keys "
        "longer, and 3w ties with $b."),
    "ctrl-o-18": ("$i=t<C-p><C-o>F,=p<C-p><C-o>;=h<C-p>",
        "Working right to left, each name is the nearest word behind the cursor, so a letter and Ctrl-p type it. "
        "$i starts in front of the ). Ctrl-o F, goes back to the comma after port, and Ctrl-o ; repeats the F, "
        "back to the comma after host. Going left to right (f,i, Ctrl-o ; and Ctrl-o f)) costs a key more."),
    "ctrl-o-19": ("f%ic<C-n>=<C-o>f\\ total=%d<C-o>f), t<C-p>",
        "f%i starts in front of the %. count is further along the line, so c and Ctrl-n, searching forward, type "
        "it. Ctrl-o f\\ jumps to the backslash of \\n, where the second label goes, and Ctrl-o f) to the end of the "
        "arguments, where total is now behind you, for t and Ctrl-p. Each Ctrl-o saves a key over <Esc> and i, "
        "and the completions six more over typing the names."),
    "ctrl-o-20": ("f,i: string<C-o>;: number<C-o>f): n<C-p><C-o>l: Socket",
        "f,i starts in front of the first comma, right after host. Ctrl-o ; repeats the f, to the next comma, "
        "Ctrl-o f) goes to the ), and n<C-p> completes the number you typed a moment ago. Ctrl-o l steps over the "
        ") so that : Socket goes after it (Ctrl-o a does the same). Working right to left costs more: no number "
        "would be behind you yet for the second one, and n<C-p> would find net on line 2."),

    # ---------- Ctrl-t Ctrl-d ----------
    "ctrl-t-1": ("Go<C-d>log.info(\"done\")",
        "o starts the new line at the loop body's indent, 8 spaces. Ctrl-d removes one shiftwidth, which puts "
        "it back in the function. Backspace does the same in the indent here, since smarttab is on; Ctrl-u "
        "would remove all of it."),
    "ctrl-t-2": ("jI- <C-t><Esc>j.j.",
        "I types the \"- \" at the start of the line, and Ctrl-t indents the line from wherever the cursor "
        "is. Both are part of one insert, so j. does both on each line. >2j and I- <Esc>j.j. is two keys "
        "longer, and so is a block insert of \"    - \"."),
    "ctrl-t-3": ("o- Install<CR><C-t>- macOS<CR>- Linux<CR><C-d>- Usage",
        "Each <CR> starts the new line with the previous line's indent. Ctrl-t goes in a level for macOS, "
        "Linux keeps that indent by itself, and Ctrl-d comes back out for Usage. At the start of a line, "
        "Tab and Backspace would do the same (smarttab is on); Ctrl-t and Ctrl-d also work after you've typed "
        "the text."),
    "ctrl-t-4": ("3jA * r<C-p><C-t>",
        "A appends the factor, with r<C-p> completing rate from line 1. Ctrl-t then adds a shiftwidth of indent "
        "to the whole line, from wherever the cursor is. Indenting first with >> is a key longer, since >> and A "
        "are two commands."),
    "ctrl-t-5": ("GA<C-w><C-w>None<C-d>",
        "Two Ctrl-w delete the 1 and the - (they're different kinds of character), and you type None. Ctrl-d "
        "then takes the line out one level, to the loop's own indent. G<< and the same edit is a key longer; "
        "f-C in place of A<C-w><C-w> ties."),
    "ctrl-t-6": ("6Wa<CR><C-t><Esc>f r<CR>Ei,<CR><C-d>",
        "6W walks the WORDs from the top to the [ (Gf[ is a key more). After it, Enter starts a line with no "
        "indent and Ctrl-t gives it one level. r<CR> turns the space after the first comma into a line break, and "
        "the new line keeps that indent. E jumps to the end of the WORD \"rich\"], the ]. i, adds the last comma, "
        "Enter puts the ] on a line of its own at the same indent, and Ctrl-d takes it back out. At the very "
        "start of a line, Tab and Backspace do the same as Ctrl-t and Ctrl-d here."),

    # ---------- Ctrl-x Ctrl-l ----------
    "line-complete-1": ("O@<C-x><C-l>",
        "O opens a line above the def at the top level. The @retry line is the only one that starts with @, "
        "so @ and Ctrl-x Ctrl-l complete all of it. :1t- copies it too, in five keys."),
    "line-complete-2": ("Go<CR>i<C-x><C-l><C-p><C-h> {<CR>b->cap = n;<CR>return 0;<CR>}",
        "Go<CR> leaves a blank line. Both prototypes start with i, and Ctrl-x Ctrl-l finds the nearer one, "
        "buffer_len, first; Ctrl-p steps to buffer_init. Ctrl-h deletes the ;, and C's indenting places the "
        "body and the }. With nothing typed, Ctrl-x Ctrl-l would offer the comment first and need another "
        "Ctrl-p: the same length. Copying the line with :3t$ costs two keys more."),
    "line-complete-3": ("Gowith pytest.raises(ValueError):<CR>p<C-x><C-l><C-x><C-l><C-w><C-w>\")",
        "After the with line, Python indents the next line by 8. p and Ctrl-x Ctrl-l complete the parser "
        "line at that indent (no other line starts with p), and a second Ctrl-x Ctrl-l adds the line that "
        "followed it. Two Ctrl-w delete \") and the 2, and \") closes the string again. Yanking the two lines "
        "first, then p, >j and f2x, is a key longer."),
    "line-complete-4": ("oW<C-x><C-l>",
        "o opens the line below the second FROM. The first query's WHERE line is the only line starting with W, "
        "so W and Ctrl-x Ctrl-l complete all of it. :2t. copies it too, a key longer, and you need to know its "
        "line number."),
    "line-complete-5": ("Goc<C-x><C-l><C-p><CR>a<C-x><C-l><C-w>0",
        "Go opens test_empty's body, indented. Both cart lines start with c: Ctrl-x Ctrl-l offers the nearer one, "
        "cart.add, first, and Ctrl-p steps up to cart = Cart(...). Enter, then a and Ctrl-x Ctrl-l complete the "
        "only line starting with a, the assert, and Ctrl-w swaps its 450 for 0. :8t$|10t$ and then A<C-w>0 is a "
        "key longer."),
    "line-complete-6": ("jos<C-x><C-l><C-p>;<CR>s<C-x><C-l><C-p>;<CR>",
        "jo opens a line below the blank one. Nothing above starts with s, so Ctrl-x Ctrl-l wraps around to the "
        "end of the file and searches up from there: send_response comes first, and Ctrl-p steps to "
        "parse_request. On the next line your new prototype is the nearest s line, so one Ctrl-p reaches "
        "send_response's header. The last Enter leaves the blank line before main. Copying the headers with :t "
        "and adding the semicolons takes at least four keys more."),

    # ---------- Ctrl-k ----------
    "digraph-1": ("fer<C-k>e'$r<C-k>e:",
        "r takes a digraph as its character: r Ctrl-k e' replaces the e with é. $ jumps to the last e, and "
        "e: is e with an umlaut, ë."),
    "digraph-2": ("fCi<C-k>DG<Esc>$.F-2s<C-k>->",
        "fC lands on the first C, and Ctrl-k DG inserts ° before it. The line ends in the other C, so $. "
        "inserts the second °. F- goes back to the arrow, and 2s replaces both its characters with the "
        "digraph ->, a real →."),
    "digraph-3": ("ji<C-k>vr<C-k>hh<C-k>hh <Esc>+.0r<C-k>ur",
        "vr is ├ (lines going vertical and right) and hh is ─. + goes to the start of the next line and . "
        "types the same prefix there, then 0r<C-k>ur turns its first piece into └ (up and right). Typing the "
        "second prefix out would take five keys more."),
    "digraph-4": ("f<lt>2s<C-k>=<lt><Esc>;.f!2s<C-k>!=",
        "f< lands on the first <=, and 2s replaces both its characters with the digraph =<, a real ≤. ; repeats "
        "the f< to the next one, and . does the same 2s there. f! and 2s with != make the ≠. :s/<=/≤/g for the "
        "two ≤ is two keys longer than f<, 2s and ;. together."),
    "digraph-5": ("fcr<C-k>c,fur<C-k>u:far<C-k>a?",
        "Each letter is one f and one r with a digraph: c, is ç, u: is ü and a? is ã (a~ works too). After the "
        "ü, the next a on the line is the one in Sao, so a plain fa gets there."),
    "digraph-6": ("O<C-k>dr<C-k>dl<Esc>jo<C-k>ur<C-k>ul<Esc>8i<C-k>hh<Esc>2k.",
        "Type the four corners first: ┌┐ (dr, dl) above and └┘ (ur, ul) below. After <Esc> you're on the ┘, and "
        "8i types eight ─ (hh) in front of it. 2k goes up to the top line, where the cursor ends up on the ┐, "
        "and . types the eight ─ in front of that too. Filling the top line first and copying it down with yyjp, "
        "then fixing both corners, is a key longer."),

    # ---------- Ctrl-v ----------
    "literal-1": ("A<C-v><Tab>typing<Esc>jA<C-v><Tab>static<Esc>j.",
        "With expandtab on, Tab types spaces, but Ctrl-v Tab inserts a real tab character. The second line's "
        "insert is the same as the third's, so j. repeats it, tab included."),
    "literal-2": ("O<C-v>u2554<C-v>u2557<Esc>7i<C-v>u2550<Esc>",
        "Double-line box pieces have no digraphs, so Ctrl-v u and the hex code types them: 2554 is ╔ and "
        "2557 is ╗. After <Esc> the cursor is on the ╗, and 7i types seven ═ (2550) in front of it. The last "
        "<Esc> counts this time: it's what adds the other six."),
    "literal-3": (":%s/=/<C-v>u2550/g<CR>",
        "Ctrl-v works on the command line too, so Ctrl-v u2550 puts a ═ in the replacement. One :s covers all "
        "four underlines. jVr with Ctrl-v u2550, then 4j. for each of the others, is three keys longer."),
    "literal-4": ("f r<C-v><Tab>;.",
        "f and a space find the first gap. With expandtab on, r and Tab would give spaces, but r Ctrl-v Tab puts "
        "in a real tab. ; finds the next space and . repeats the r. :s/ /\\t/g is three keys longer."),
    "literal-5": ("i<C-v><Esc><Esc>6w.",
        "Ctrl-v Esc inserts an Escape character, and the second Esc leaves Insert mode. 6w steps over ^[[, 1, ;, "
        "32mWelcome, to and web1 to the other [, and . inserts another Escape in front of it (2f[ or $F[ is a "
        "key more)."),
    "literal-6": ("r<C-v>u256d$r<C-v>u256eGr<C-v>u256f0r<C-v>u2570",
        "These corners have no digraphs, but after r, Ctrl-v u and four hex digits type any character: 256d is ╭ "
        "and 256e ╮. G keeps the column, so from the top-right corner it lands on the bottom-right one, for ╯ "
        "(256f), and 0 goes to the start of the line for ╰ (2570)."),

    # ---------- q: ----------
    "cmdwin-1": ("q:kf6r0<CR>",
        "q: opens your command history as text, with the cursor on an empty line at the bottom, so k reaches "
        "the :s. f6r0 turns 16.0 into 10.0, and <CR> runs the edited line in your file. On the command line "
        "itself you'd have to arrow your way to the 16."),
    "cmdwin-2": (":%s/#222/var(--text-strong)/<CR>q:kf23r8fscwmuted<Esc><CR>",
        "The first :s has to be typed. The second differs only in the middle, so q: and k bring it back as "
        "text: f2 and 3r8 make the color #888, fs and cwmuted change the variable's name, and <CR> runs it. "
        "Retyping the whole command would cost nine keys more."),
    "cmdwin-3": ("q:3kfocwerr<Esc><CR>",
        "In the q: window the newest command is at the bottom, so 3k goes up to the third one back. fo lands "
        "on out (System has no o), cwerr changes it, and <CR> runs it."),
    "cmdwin-4": ("q:kf\"r';.<CR>",
        "q:k puts your last command in front of you as text. f\" lands on the first double quote and r' turns it "
        "into a single one; ; finds the next \" and . repeats the r'. <CR> runs the edited command. :<C-f> opens "
        "the same window from the command line, in the same number of keys; retyping the :s takes eleven more."),
    "cmdwin-5": ("q:kfEiNot<Esc>f=r!<CR>",
        "The E of Equals is the only capital E in the command, so fE gets there and iNot makes it NotEquals. f= "
        "finds the first = of == and r! makes it !=. <CR> runs it on the whole file, as before. Typing the new "
        ":s out would take over thirty keys more."),
    "cmdwin-6": ("q:kfhxp<CR>",
        "The command's only h is the one in Lenght, so fh lands on it, and xp swaps it with the t after it. "
        "<CR> runs the fixed command. A new, shorter :%s/Length(/Size(/g still takes twelve keys more."),

    # ---------- @: ----------
    "at-colon-1": (":ce40<CR>G@:",
        ":ce40 (short for :center 40) centers the cursor line. G goes to the last line, and @: runs the same "
        "command line again. :1ce40|6ce40 is four keys longer, and a :g pattern that matches only these two "
        "lines longer still."),
    "at-colon-2": ("2:s/float/double/g<CR>8j@:",
        "2: fills in the range .,.+1, the first two lines of area(). The :s leaves the cursor on line 2, and "
        "8j reaches perimeter(). @: repeats the command with its relative range, measured from there. & would "
        "repeat the :s on just one line."),
    "at-colon-3": ("j:ri50<CR>3j@:G@@",
        ":ri50 (short for :right 50) right-aligns the line. 3j and @: do the next name, and once you've used "
        "@:, @@ repeats it in one key less; G reaches the last name. Typing :2ri50|5ri50|8ri50 is five keys "
        "longer."),
    "at-colon-4": (":s/ \\+/ /g<CR>6j@:",
        ":s/ \\+/ /g replaces every run of spaces on line 1 with a single space; single spaces stay as they are. "
        "6j reaches the second comment, and @: runs the same command line again, g flag included. & would drop "
        "the g and fix only the first run, :&& is two keys longer than @:, and :g/^\\//s/ \\+/ /g two longer "
        "than the whole solution. :%s would squeeze the aligned fields too."),
    "at-colon-5": (":s/-/=/g<CR>2j@:",
        ":s/-/=/g doubles the top border of both boxes, and 2j and @: do the same on line 3. A range from 1 to 3 "
        "would turn the arrow into ==>, and :g/^+/s/-/=/g, which picks the right lines, is a key longer."),
    "at-colon-6": ("2j2:le4<CR>3j@:",
        "2j reaches apples, and 2: types :.,.+1, so :le4 (short for :left 4) sets the indent of apples and pears "
        "to exactly 4. The cursor stays on apples, so 3j reaches leeks, and @: runs the command with the same "
        "relative range there. >> can't do this, since the indents are all different. :3,7v/^-/le4 is a key "
        "longer, and :g/^ /le4 would flatten baby carrots too."),

    # ---------- Ctrl-a (Insert) ----------
    "ctrl-a-insert-1": ("A build/release<Esc>A && cd<C-a>",
        "The first insert types \" build/release\". In the second, Ctrl-a types it again, leading space "
        "included, so the line ends with cd build/release. Ctrl-r . does the same in one key more."),
    "ctrl-a-insert-2": ("jf;imaxConnections<Esc>jjF).othis.<C-a> = <C-a>;",
        "Type the name once in front of the ;. j j and F) reach the parameter list, and . inserts it there. "
        "o opens the constructor's body, and Ctrl-a types maxConnections twice, since . repeated it and it's "
        "still the last insert. Completing it with m<C-p> costs one key more each time."),
    "ctrl-a-insert-3": ("A CONFIG_PARSER_H<Esc>j.GA /*<C-a> */",
        "A types the name on #ifndef, and j. repeats that on #define. The #endif needs it inside a comment, "
        "which . can't do, but Ctrl-a types \" CONFIG_PARSER_H\" again, space included. Completing the name "
        "with C and Ctrl-p takes two keys more, counting the space you'd type yourself."),
    "ctrl-a-insert-4": ("jA chunk<Esc>A = 0;<C-a> <lt><C-a>_count;<C-a>++) {",
        "The first insert is \" chunk\", leading space included. In the second, each Ctrl-a types \" chunk\" "
        "again, so the spaces come out right, and chunk_count is Ctrl-a followed by _count. Doing it in one "
        "insert with c and Ctrl-p costs five keys more: by the third chunk, Ctrl-p finds chunk_count first."),
    "ctrl-a-insert-5": ("jjA[^cache-bench]<Esc>Go<CR><C-a>: Measured on a 2023 laptop.",
        "The first insert is just the marker, so Ctrl-a in the second one, at the end of the file, types "
        "[^cache-bench] again. Go<CR> opens a line after ## Notes and leaves it blank. Yanking the marker with "
        "ya[ and using Ctrl-r 0 instead is four keys longer."),
    "ctrl-a-insert-6": ("A v2.4.0-rc1<Esc>A -m \"Release<C-a>\" && g<C-p> push origin<C-a>",
        "The first insert is \" v2.4.0-rc1\" with its leading space. In the second, Ctrl-a types it after "
        "Release, inside the quotes, and again at the end. g<C-p> completes git from the start of the line. "
        "Completion can't help with the tag itself: it's made of several words."),

    # ---------- Ctrl-b Ctrl-e Ctrl-p Ctrl-n ----------
    "cmdline-keys-1": ("j2:s/\\v(.*) (.*)/\\2, \\1 (staff)/<CR>3j:<C-p><C-w><C-w>guest)/<CR>",
        "2: fills in .,.+1, so the :s rewrites both staff lines. After it, the cursor is on Alan Turing, and 3j "
        "reaches the guests. : and Ctrl-p bring back the whole command, range and all. Ctrl-w deletes )/ and "
        "then staff, and you type the new tag. Reusing the pattern with :.,+1s//...(guest)/ is twelve keys "
        "longer."),
    "cmdline-keys-2": (":ri40<CR>:<C-p><C-b>8,$<CR>",
        ":ri40 right-aligns line 1. : and Ctrl-p bring the command back, Ctrl-b jumps to its start, and 8,$ "
        "(line 8 to the last line) is all you type. Typing :8,$ri40 out is two keys longer. Typing the range "
        "first and inserting the last command line with Ctrl-r : is a tie."),
    "cmdline-keys-3": (":<C-p><C-p><C-p><C-b>5,7<C-e><C-w><C-w>poetry]/<CR>",
        "Each Ctrl-p goes one command further back, so the third brings back the :s. Ctrl-b jumps to its start "
        "for the range, and Ctrl-e back to the end, where Ctrl-w deletes ]/ and then novel. Typing :s/ and "
        "then Up recalls it too, since Up only matches commands starting with what you've typed. The q: "
        "window takes two keys more, and retyping the :s far more."),
    "cmdline-keys-4": (":<C-p><C-b>g/\"h/<CR>",
        ": and Ctrl-p bring back :normal A  # noqa: E501, Ctrl-b jumps to its start, and g/\"h/ in front makes it "
        "a :g that runs the :normal on every line with a quote followed by an h: only the two URL lines. Typing "
        "the whole :g out is eighteen keys more."),
    "cmdline-keys-5": (":<C-p><C-b>%<C-e>g<CR>",
        "Ctrl-p brings back the :s, Ctrl-b goes to its start for the %, and Ctrl-e back to the end for the g "
        "flag, which changes add's three ints, not just the first. The \\< and \\> keep printInt as it is. "
        "Typing :%s/\\<int\\>/long/g out is twelve keys more."),
    "cmdline-keys-6": ("/<C-p><C-p><CR>:%s//load_user<CR>",
        "In the search prompt Ctrl-p recalls searches, so the second one brings back \\v<(get|fetch)_user> and "
        "<CR> runs it. The empty pattern in :s reuses it; each line has at most one match, so no g. q/2k<CR> "
        "gets the search back too, a key longer. Rewriting the pattern yourself costs far more, because "
        "get_users and forget_user mustn't match."),
}
