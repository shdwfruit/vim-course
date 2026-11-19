"""Reference solutions for Project 06's drills (spoilers!). Each entry: drill -> (keys, explanation).

See one with:  python3 check.py drill macro --show 3      Watch it typed:  python3 check.py drill macro --watch 3
"""
SOLUTIONS = {
    # ---------- q @ ----------
    "macro-1": ("qaI[<Esc>f s](<Esc>A)<Esc>jqQ",
        "qa starts recording. I[ opens the bracket at the start of the line, f<Space> finds the space "
        "after the name, s]( replaces it, and A) closes the link at the end, however long the URL is. "
        "j moves down and q stops recording. Q plays the macro you recorded last, here on line 2; @a "
        "does the same in one more key. (Recording without the j and typing jQ afterwards costs the "
        "same.)"),
    "macro-2": ("qad2WI[<Esc>ea]<Esc>+qQ",
        "d2W deletes two WORDs: the date and the time with their spaces. I[ opens the bracket, and e "
        "jumps from it to the end of the level, so a] closes it after WARN or ERROR alike. + moves to "
        "the next line, and Q (or @a) does the same there. Doing line 2 by hand, even with ., takes 4 "
        "more keys."),
    "macro-3": ("qa2Wi(<Esc>A)<Esc>+q2Q",
        "2W jumps two WORDs, past #define and the name, onto the value, whatever their lengths. i( "
        "opens the paren and A) closes it at the end of the line, + moves on, and 2Q (or 2@a) does "
        "the other two lines. A count of l, or $b (the values contain spaces), would break on the "
        "other lines."),
    "macro-4": ("+qaxf\"cf =<Esc>+q3Q",
        "+ moves to the first entry's opening quote. x deletes it, f\" finds the quote after the key, "
        "and cf<Space> changes the quote, colon and space into =. + moves to the next entry and 3Q "
        "(or 3@a) converts the other three. f\" makes it work for keys of any length: log_file as well "
        "as host."),
    "macro-5": ("qagUiwea: Final<Esc>+q3Q",
        "gUiw uppercases the whole name and leaves the cursor at its start, e jumps to its last "
        "letter, and a: Final types the annotation after it. + moves on and 3Q does the other three. "
        "Doing gUiw on every line with . first and the annotations second takes about 30 keys."),
    "macro-6": ("jqaI(\"<Esc>f,s\", \"<Esc>;.A\"),<Esc>+q3Q",
        "j goes to the first row. I(\" opens the tuple, f, finds the first comma and s\", \" replaces "
        "it. ; repeats the f, to reach the second comma and . repeats the s there. A\"), closes the "
        "row and + moves on. 3Q converts the other three rows."),
    "macro-7": ("qa/mal<CR>rcf(a1, <Esc>q3Q",
        "The macro starts with a search, so it always begins on the next malloc, wherever the last "
        "run left the cursor. rc turns malloc into calloc, and f( a1, adds the first argument. 3Q "
        "finds and fixes the other three. Doing it by hand with n and . takes about 32 keys."),
    "macro-8": ("+qayiwI[<Esc>ea] = \"<C-r>0\"<Esc>+q3Q",
        "+ goes to RED. yiw yanks the name, I[ opens the bracket, and e jumps to the end of the name "
        "(an underscore is part of a word, so ALPHA_MASK is one word). a] = \"<C-r>0\" types the rest, "
        "with Ctrl-r 0 inserting the yanked name. The comma was already there. 3Q does the other "
        "rows."),
    "macro-9": ("qa/--<CR>ddkI## <Esc>q2Q",
        "/--<CR> finds the next underline (a single - would also stop on the list items). dd deletes "
        "it, which leaves the cursor on the line below, so k goes back up to the heading and I## adds "
        "the hashes. 2Q does the other two. :g/--/norm ddkI## (Project 07) takes 18 keys."),
    "macro-10": ("qaIpublic <Esc>$byiwiget<Esc>l~$s() { return <C-r>0; }<Esc>+q2Q",
        "Ipublic adds the modifier. $b finds the name from the end of the line, which works for "
        "List<String> as well as int, and yiw yanks it. iget<Esc> types get in front, l steps onto "
        "the name and ~ capitalizes its first letter. $s replaces the ; with the method body, Ctrl-r "
        "0 inserting the lowercase name. + moves on, and 2Q writes the other two getters."),
    "macro-11": ("qaI| <Esc>Es |<Esc>A |<Esc>jq2Q",
        "I| adds the first bar. From the space after it, E jumps to the end of the key, the colon, and s | "
        "replaces it (the space after the colon stays). A | closes the row and j moves down. 2Q plays the "
        "macro on version and license. Visual block can add the outer bars, but the colons are in different "
        "columns: that way takes 24 keys."),
    "macro-12": ("+qadWea =<Esc>A,<Esc>>>+q3Q",
        "+ goes to the first #define. dW deletes #define and its space, e jumps to the end of the name and "
        "a = adds the equals sign, A, the comma, and >> indents the line by 4. + moves to the next line's "
        "first non-blank, its #, and 3Q does the other three. Ending with j would keep the cursor at the "
        "end of the line, where dW goes wrong on the next run."),
    "macro-13": ("qacwimport<Esc>f=cf(from <Esc>f)x+q3Q",
        "cw turns const into import. f= finds the =, and cf( changes = require( into from and a space. f)x "
        "deletes the closing parenthesis, and + moves on. 3Q converts the other three, the { promisify } "
        "one too: f= skips over the braces. Doing each kind of edit down the file with . takes about 50 "
        "keys."),
    "macro-14": ('+qacit<a href="#<C-r>""><C-r>"</a><Esc>F#gue+q3Q',
        "+ goes to the first <li>. cit deletes the label into the unnamed register, and the <a> tag is "
        "typed around it, with Ctrl-r \" typing the label for the anchor and again for the link text. F# "
        "goes back to the #, and gue lowercases from there to the end of the anchor. + moves on, and 3Q "
        "does the other items: the macro replays the keys Ctrl-r \", so each run types the label it just "
        "deleted. The setup turns off HTML's indent rules, which would re-indent the line as you type the "
        "tag."),
    "macro-15": ("qa3xWdf=gUeW5x$x+q3Q",
        "3x deletes ts=, the same three characters on every line. W jumps to level=..., df= deletes up to "
        "its =, and gUe uppercases the level that's left. W goes to msg=\", and 5x deletes those five "
        "characters, the same on every line again. $x drops the closing quote, and + moves on. 3Q does the "
        "rest. df= in place of 3x, and df\" in place of 5x, cost a key each."),
    "macro-16": ("qa$yiwx@0a#<Esc>+q4Q",
        "$ goes to the number and yiw yanks it into \"0. x deletes it. @0 plays register 0 as keys, so it "
        "types 3 as if you'd pressed it: a count for the next command, and a#<Esc> appends three #. + moves "
        "on, and 4Q draws the other bars, each with its own number. Typing $x3a#<Esc> on each line takes 34 "
        "keys."),
    "macro-17": ("qagUiwISERVER_<Esc>f 4s=<Esc>$x+q3Q",
        "gUiw uppercases the key (iw takes the underscores too), and ISERVER_ adds the prefix. f<Space> "
        "goes to the space after the key, and 4s replaces the four characters  = \" with =. $x deletes the "
        "closing quote, and + moves on. 3Q converts the other three. cf\"= instead of 4s= is a key longer."),
    "macro-18": ('qacwassertThat<Esc>2l"adt,2x$F)a.isEqualTo(<C-r>a)<Esc>+q4Q',
        "cw renames assertEquals. 2l steps past the ( onto the expected value, and \"adt, cuts it into "
        "register a: the 2x that deletes the comma and space next would replace the unnamed register. $F) "
        "finds the last ), the one that closes assertThat(, and a.isEqualTo( Ctrl-r a ) puts the value back "
        "at the end. + moves on, and 4Q does the other four, whatever the expressions look like. Retyping "
        "one line costs about 34 keys."),
    "macro-19": ("qa/fop<CR>2byiwoif (!<C-r>0) return -1;<Esc>q2Q",
        "The fopen lines are spread out, so the macro starts with /fop<CR>, which finds the next one from "
        "wherever the cursor is. 2b goes back two words, over the = to the variable, and yiw yanks it. o "
        "opens a line below, indented like the fopen, and the check is typed with Ctrl-r 0 for the name. "
        "The cursor ends on the new line, so the next search finds the next fopen, and 2Q does the other "
        "two."),
    "macro-20": ("qaw6s[<Esc>ea](<Esc>J2dWA)<Esc>+q3Q",
        "w moves to name:, and 6s replaces name: and its space with [. e jumps to the end of the name, and "
        "a]( closes the bracket. J joins the url line on with one space and leaves the cursor on that "
        "space, so 2dW deletes it and url: . A) closes the link, and + moves to the next pair. 3Q does the "
        "other three. dWi[ in place of 6s[ is a key longer."),

    # ---------- @@ Q {N}@ ----------
    "replay-1": ("qaf[lrxWi~~<Esc>A~~<Esc>+qQ2+Q",
        "Record on the first task: f[l steps into the box and rx checks it. W jumps to the text, i~~ "
        "and A~~ strike it through, and + moves to the next task. Q plays the macro you just recorded "
        "on add tests and leaves you on update the README. 2+ skips two tasks, and Q again does fix "
        "the CI cache. With @a and @@ instead of the two Qs it takes 2 more keys."),
    "replay-2": ("+qaf,s=\"<Esc>A\",<Esc>+qqbf,r=A,<Esc>+q@a+2@@2Q",
        "+ goes to host. Macro a quotes a text value: f,s=\" replaces the comma, A\", closes the quote, "
        "+ moves on. Macro b does a number on port: f,r= and A, (no quotes). b was recorded last, so "
        "Q would play b; user needs a, so play it with @a. + steps over the comment, and 2@@ plays "
        "the macro you played last (a) on log_level and log_file. Then 2Q plays b, the one you "
        "recorded last, on timeout and retries."),
    "replay-3": ("+qaf,s: \"<Esc>A\",<Esc>+q9Q",
        "+ moves to the first row. f,s: \" replaces the comma, A\", closes the value, and + moves to "
        "the next row, so the macro is ready to run again. 9Q plays it nine times in one go (9@a is "
        "one key more). Nine separate Qs would cost 9 keys."),
    "replay-4": ("+qaf,s\", \"<Esc>I{\"<Esc>A\"},<Esc>+q99Q",
        "The macro starts with f,, which fails on the }; line before anything changes. s\", \" replaces "
        "the comma, I{\" and A\"}, wrap the row, and + moves on. 99Q runs it until f, fails on }; and "
        "cancels the rest of the count. Counting the rows (11Q) costs the same 3 keys, but 99Q saves "
        "you the counting. A macro that started with I{\" would mangle the }; line instead."),
    "replay-5": ("qadf f]xf:x+q99Q",
        "df<Space> deletes [2026-10-21 and its space, f]x deletes the bracket after the time, and f:x "
        "the colon after the level (the time's colons are behind the cursor by then). + moves on. On "
        "the last line + fails after the edits, which ends the run, and the rest of 99Q is cancelled. "
        "10Q is also 3 keys."),
    "replay-6": ("qa/TODO <CR>ea(rick):<Esc>q3Q",
        "The search finds the next TODO wherever you are, e goes to its last letter and a(rick): "
        "signs it. A signed TODO no longer matches \"TODO \" with the space, so each run finds a new "
        "one. 3Q signs the other three. (Searching for TODO alone would find the first one again "
        "after wrapping around.) /TODO<Space><CR> plus ne. for each of the others takes 26 keys, "
        "against 22."),
    "replay-7": ("+qaf,s = <Esc>A,<Esc>+q2Q+4Q",
        "Record on alice: f,s = <Esc> replaces the comma, A, ends the field, and + moves on. 2Q does "
        "bob and carol and stops on the comment. The comment has a comma too, so the macro wouldn't "
        "fail there: step over it with +, then 4Q plays it four times for dave to grace (4@@ or 4@a "
        "would cost one key more). A search like /,<CR> in the macro would land on the comment as "
        "well."),
    "replay-8": ("jqayypI  <Esc>q5Q",
        "j goes to the first step. yyp copies it below and puts the cursor on the copy, and "
        "I<Space><Space> indents the copy by two. The cursor stays on the new step, so the next run "
        "copies that one. 5Q adds the other five steps."),
    "replay-9": ("qaA:<Esc>J+q3Q",
        "A: adds the colon, J joins the value on with one space, and + moves to the next key. Each "
        "run turns two lines into one, so there are 3 runs left, not 6 lines. On the last pair, + "
        "fails, which doesn't matter: everything is done."),
    "replay-10": ("qaA,<Esc>gJA,<Esc>gJjddq3Q",
        "A,<Esc> adds a comma and gJ joins the email on without a space. A,<Esc>gJ again does the "
        "phone number. j goes to the blank line and dd deletes it, leaving the cursor on the next "
        "contact. 3Q does the other three; on the last one j fails at the end of the file, after the "
        "joins."),
    "replay-11": ('qaIexport <Esc>f=a"<Esc>A"<Esc>jq7Q',
        "Record on line 1: Iexport  adds the keyword, f= finds the equals sign and a\" opens the quote after "
        "it, A\" closes it at the end of the line, and j moves down. Seven lines are left, and 7Q plays the "
        "macro seven times. Block insert can add export to every line at once, but the = signs are in "
        "different columns: that way takes about 44 keys."),
    "replay-12": ("qayyp0xA**<Esc>q3Q",
        "yyp copies the row below and leaves the cursor on the copy. 0x deletes one of its leading spaces, "
        "and A** adds two stars. The next run copies the row this one made, so the tree grows. You have two "
        "rows after recording, so 3Q makes the last three: count runs still to do, not rows. Typing each "
        "row takes about 36 keys."),
    "replay-13": ("qawi[<Esc>f s](<Esc>A)<Esc>+qQqbwi**<Esc>A**<Esc>+q@a2Q@a",
        "Macro a makes a link: w moves to the name, i[ opens the bracket, f<Space> finds the space before "
        "the URL and s]( replaces it, A) closes, + moves on. Q does docs. On roadmap, record b: i** and A** "
        "bold the name. Now Q plays b, the one recorded last, so blog needs @a. 2Q plays b on changelog and "
        "faq, and @a does status (@@ would play b now, the macro played last)."),
    "replay-14": ('2+qaI{ "<Esc>f,s", <Esc>A },<Esc>+qQ+3Q',
        "2+ goes to add. Record the row: I{ \" opens it, f, finds the comma and s\",  replaces it, A }, "
        "closes the row, and + moves on. Q does rm. The ls row is already done, and the macro wouldn't fail "
        "on it (it has a comma), so + steps over it. 3Q does mv, cp and cat."),
    "replay-15": ("jqaf,s**: <Esc>I**<Esc>+q99Q",
        "j goes to buffer. The macro starts with f, so it fails on a line without a comma before changing "
        "anything: s**:  replaces the comma, I** opens the bold, and + moves on. 99Q runs it until it "
        "reaches the blank line, where f, fails and the count is cancelled, so the CSV below is never "
        "touched. Counting the ten terms left (10Q) costs the same 3 keys."),
    "replay-16": ("qaI- name: <Esc>f,s<CR>  role: <Esc>f,s<CR>team: <Esc>+q3Q",
        "I- name:  starts the item. f, finds the first comma, and s<CR> replaces it with a line break; type "
        "two spaces and role: there. f, then s<CR> again for the team: this time the new line gets the two "
        "spaces from the line above (autoindent), so type just team: . + lands on the next row, and 3Q does "
        "the other three: each run turns one line into three, so count the rows left."),
    "replay-17": ("qaI**<Esc>A**<Esc>2jq3Q",
        "I** and A** put the question in bold, and 2j skips the answer to land on the next question. 3Q "
        "does the other three. With . you'd need two passes, one for each end of the line (about 28 keys)."),
    "replay-18": ("qar-a **Added:**<Esc>+qQqba **Removed:**<Esc>+qQ3@a",
        "Record a on the first + line: r- turns the + into a dash, a **Added:** inserts the label after it, "
        "and + moves on. Q does faster startup. Record b on the first - line: it only needs a **Removed:**. "
        "Q plays b, the macro recorded last, on the legacy importer. For the last three lines you need a "
        "again, and 3@a plays it three times (@a and 2@@ also work, in 2 keys more)."),
    "replay-19": ("qa+f r(A)<Esc>q99Q",
        "Line 1 is already done, so the macro starts with the move: + goes to the next line, f<Space> finds "
        "the space after print, r( replaces it, and A) closes the call. Each run then begins by moving to "
        "its line. The bare print on the last line has no space, so f<Space> fails there before any edit, "
        "and 99Q stops by itself. 10Q, the exact count, is the same 3 keys."),
    "replay-20": ('qaIrouter.<Esc>f,s("<Esc>;s", <Esc>A);<Esc>+q5Q',
        "Irouter. adds the prefix. f, finds the first comma and s(\" replaces it, ; finds the second and s\", "
        "replaces that one, and A); closes the call. + moves on, and 5Q does the other five rows. On the "
        "last one + fails, but only after the edits."),

    # ---------- :norm @ ----------
    "norm-macro-1": ("qa3f,s <lt><Esc>A><Esc>F,r ;.Ialias <Esc>q:%norm Q<CR>",
        "3f, jumps to the third comma, so on grace's row (two commas) the macro fails before it "
        "changes anything. s <lt> replaces that comma with \" <\" and A> closes the email. F,r<Space> "
        "turns the second comma into a space, and ; with . does the first. Ialias adds the keyword. "
        ":%norm Q runs the macro you just recorded on every line (:%norm @a is one key more): the "
        "short rows fail and are skipped, and so does ada's row, which has no commas left. A count "
        "would stop for good at grace. A search for three commas (/,.*,.*,<CR>) inside the macro plus 4Q also takes 36 keys, but you'd have to count the rows."),
    "norm-macro-2": ("qa3f,0f,s = Vec3(<Esc>f,a <Esc>;.A)<Esc>q:%norm Q<CR>",
        "3f, is just a test: it fails on door and light (two commas) and on a finished row. 0f, goes "
        "back to the first comma, s = Vec3( replaces it, f,a<Space> spaces out the next comma and ;. "
        "the last one. A) closes the call. :%norm Q runs it on every line and skips the ones where "
        "3f, fails. Working backward from the third comma is harder than it looks: , would find the "
        "comma right behind the space you just typed. A search for three commas inside the macro plus "
        "3Q is a few keys shorter, but you'd have to count."),
    "norm-macro-3": ("2jqa2f,s # <Esc>,r wdW0Pq:%norm Q<CR>",
        "2j goes to web2. 2f, needs two commas, so the macro fails on db1, queue1, the comments and "
        "the finished lines. s # <Esc> replaces the second comma, , goes back to the first one and "
        "r<Space> turns it into a space. w moves onto the address, dW cuts it with its space, and 0P "
        "puts it at the start of the line. :%norm Q does the rest, wherever the rows are. A search "
        "(/,.*,<CR>) inside the macro plus 3Q is shorter, but you'd need the right pattern and the "
        "right count."),
    "norm-macro-4": ("qa3f,s | <Esc>,.,.I| <Esc>A |<Esc>qvip:norm Q<CR>",
        "Record on ajax: 3f, (fails on short rows and finished ones), s | <Esc> replaces the third "
        "comma, and , with . does the second and the first (, repeats the f, backward). I| and A | "
        "add the outer bars. vip selects the 2026 paragraph and : types :'<,'> for you, so norm Q<CR> "
        "runs the macro on those lines only; ajax is skipped there, since it has no commas left. "
        ":%norm would convert 2025 as well. A search for three commas inside the macro plus 3Q is a "
        "few keys shorter."),
    "norm-macro-5": ("qa2f,a /* <Esc>A */<Esc>F,;s = <Esc>qvi{:norm Q<CR>",
        "Record on RED: 2f, fails on TEAL and on finished rows. a /* <Esc> and A */<Esc> add the "
        "comment, then F, goes back to the second comma and ; to the first, where s = <Esc> turns it "
        "into \" = \". vi{ selects the inside of enum color, and :norm Q<CR> runs the macro on just "
        "those lines. A search (/,.*,<CR>) inside the macro plus 3Q is shorter here, because the rows "
        "to skip are easy to describe; the Visual range is the robust way when they aren't."),
    "norm-macro-6": ("2jqa2f,F,s\", \"<Esc>,.IHost(\"<Esc>A\"),<Esc>q:4,6norm Q<CR>",
        "2j goes to web1. 2f, fails on db1. F, goes back to the first comma, s\", \" replaces it, and , "
        "(the F, repeated forward) with . does the second one. IHost(\" and A\"), wrap the row. A "
        "finished row still has two commas, so the range must leave line 3 out: :4,6norm Q runs the "
        "macro on lines 4 to 6, and the dev list stays as it is. A search inside the macro plus a "
        "count is a few keys shorter."),
    "norm-macro-7": ("jqa^cwlog.debug<Esc>2f\"i %s<Esc>q:g/print/norm Q<CR>",
        "j goes to the first print. :g starts the cursor in column 1, before the indent, so the macro "
        "starts with ^. cw types log.debug over print, 2f\" finds the closing quote and i %s adds the "
        "placeholder. :g/print/norm Q runs it on every line containing print, at any indent; the "
        "finished line doesn't match any more. Here a search inside the macro (/pri<CR>) plus 2Q is "
        "shorter: :g pays off in long files, where you'd rather not count."),
    "norm-macro-8": ("2jqa3f,s: <Esc>,dF,r I!! <Esc>q:g/ERROR/norm Q<CR>",
        "2j goes to the first ERROR row. 3f, fails on the short ERROR row (two commas). s: <Esc> "
        "replaces the third comma, , goes back to the second, dF, deletes ,ERROR up to it, and "
        "r<Space> turns that comma into a space. I!! marks the alert. :g/ERROR/norm Q runs the macro "
        "on the ERROR lines only, and the short one is skipped. The INFO and WARN rows have three "
        "commas too, so :%norm would convert them. A search for ERROR rows with enough commas plus a "
        "count is a few keys shorter, if you can write that pattern."),
    "norm-macro-9": ("4jqa2xi**<Esc>f:.q:g/^- /norm Q<CR>",
        "4j goes to the first item. 2x deletes \"- \", i** opens the bold, and f: with . closes it "
        "before the colon. :g/^- /norm Q runs the macro on each line starting with a dash. The "
        "finished item doesn't match any more, and the other lines are never touched (the macro would "
        "mangle them, since 2x can't fail). A search for ^- inside the macro plus 4Q is shorter here; "
        ":g needs no count."),
    "norm-macro-10": ("jqa2f,,s: {role: <Esc>;s, team: <Esc>A}<Esc>q:%norm Q<CR>",
        "j goes to ada. 2f, fails on grace, ken, the comments and the blank lines, and on finished "
        "rows (one comma). , goes back to the first comma, where s: {role: replaces it. ; finds the "
        "second comma again (; repeats the f, forward) and s, team: replaces it, and A} closes the "
        "mapping. :%norm Q does every line. A search inside the macro plus a count is shorter here, "
        "but you'd need the right pattern (/,.*,) and the right count."),
    "norm-macro-11": ("qa4f,s: <Esc>0df,f,r ;r q:%norm Q<CR>",
        "4f, jumps to the fourth comma, so on a row with fewer fields the macro fails before it changes "
        "anything (and on a finished row, which has no commas left). s:  replaces that comma, 0df, deletes "
        "the date and its comma, and f,r<Space> and ;r<Space> turn the other two commas into spaces. :%norm "
        "Q runs it on every line and skips the short rows. The complete rows come in six separate groups, "
        "so playing the macro with counts and stepping over the short rows takes 33 keys, and a search for "
        "four commas inside the macro costs more still."),
    "norm-macro-12": ("jqa3f;s = <Esc>,s x<Esc>,r q:%norm Q<CR>",
        "j goes to the first row. 3f; is both the test and the first move: it fails on rows with fewer than "
        "three semicolons, and on the comments. s =  replaces the last semicolon, , (the f; again, "
        "backwards) reaches the one before it for s x, and , once more gets the first, which r<Space> turns "
        "into a space. :%norm Q does the rest; a finished row has no semicolons, so it's skipped too. "
        "Counting and stepping over the six gaps by hand takes 2 keys more. A search for three semicolons "
        "(/;.*;.*;<CR>) inside the macro plus 5Q ties."),
    "norm-macro-13": ("qa4f,s</td><td><Esc>,.,.,.I<tr><td><Esc>A</td></tr><Esc>qjvit:norm Q<CR>",
        "4f, fails on rows with fewer than five fields, and on the tags. From the last comma, s</td><td> "
        "replaces it, and , with . repeats that on the three commas before it (no comma is typed, so , "
        "finds the old ones). I<tr><td> and A</td></tr> add the ends. j moves to a row that's still plain "
        "text, right inside <tbody>, where vit selects everything inside that tag; : types the range for "
        "you, and norm Q runs the macro on those lines only, so <pre> keeps its raw rows. On ada's "
        "converted row, vit would only select inside <tr>. Counts with + to step over the short rows take 3 "
        "keys more, and a search pattern for four commas costs more than vit."),
    "norm-macro-14": ("jqa3f:s; # <Esc>,s weight=<Esc>Iserver <Esc>qvi{:norm Q<CR>",
        "j goes to web1. 3f: fails on incomplete rows, and on finished ones, which keep only one colon. "
        "From the last colon, s; #  turns it into the end of the directive and the comment, , goes back to "
        "the colon before it for s weight=, and Iserver  adds the keyword. vi{ selects the inside of the "
        "production block, and :norm Q runs the macro on those lines, so staging stays as it is. Playing it "
        "with counts and + takes 4 keys more: the complete rows come in seven groups."),
    "norm-macro-15": ('jqa3f.0dWA ansible_host=<C-r>"<Esc>q:3,$norm Q<CR>',
        "j goes to web1. An IPv4 address has three dots and the DNS names here have at most two, so 3f. "
        "fails on those rows and on the group headers. 0dW cuts the address and the space after it, and A "
        "ansible_host= with Ctrl-r \" puts it back at the end (the trailing space doesn't count). A finished "
        "line still has three dots, so the range has to leave line 2 out: :3,$norm Q runs the macro from "
        "line 3 to the end. Counts and + take 3 keys more."),
    "norm-macro-16": ("qa3f,0f,s', '<Esc>;.;.I('<Esc>A'),<Esc>qjV}:norm Q<CR>",
        "3f, is the test: it fails on rows with fewer than four fields. 0f, goes back to the first comma, "
        "s', '<Esc> replaces it, and ; with . does the next two: forwards, because the text you typed has a "
        "comma in it, and , would find that one. I(' and A'), finish the tuple. A finished tuple still has "
        "commas, so jV} selects from the next line to the blank line at the end of the block, and : with "
        "norm Q runs the macro there; the 2.3 block below is never touched. Counts and + take a key more, "
        "and a search with a count ties."),
    "norm-macro-17": ('2jqa3f|s", <Esc>,s, "<Esc>,r(A),<Esc>q:%norm Q<CR>',
        "2j goes to OK. 3f| fails on rows with fewer than four fields, and on the comments and braces. From "
        "the last pipe, s\",  ends the message string, , (the f| backwards) reaches the pipe before it for "
        "s, \", and , again the first pipe, which r( turns into the opening parenthesis. A), closes the "
        "constant. :%norm Q does every line, finished ones included: they have no pipes. Counts and + would "
        "take 4 keys more."),
    "norm-macro-18": ('jqa3f|s, help="<Esc>,s, default=<Esc>,s", type=<Esc>Iparser.add_argument("<Esc>A")<Esc>q:2,$norm Q<CR>',
        "j goes to --retries. 3f| fails on short rows and on the # network and # output comments, but the "
        "comment on line 1 has three pipes too, so the range starts at line 2: :2,$norm Q. From the last "
        "pipe, s, help=\" replaces it, , goes back a pipe for s, default=, and again for s\", type=. "
        "Iparser.add_argument(\" and A\") wrap the call. The text you type has no pipes, so , always finds "
        "the next old one. Typing even one call takes about 60 keys; counts and + to step over the gaps "
        "tie."),
    "norm-macro-19": ("qa3f;s  # <Esc>,s = <Esc>,s: <Esc>q:%norm Q<CR>",
        "The cursor starts on retries. 3f; fails on rows with fewer than three semicolons, and the header "
        "comment uses commas. From the last semicolon, s  #  starts the comment, , (the f; backwards) "
        "reaches the one before it for s = , and the first one becomes : . A finished field has no "
        "semicolons, so :%norm Q can run on every line, the one you recorded on included. Counts and + take "
        "3 keys more, and a search for three semicolons inside the macro takes 1 more."),
    "norm-macro-20": ("qa4f;s) <Esc>,s (<Esc>,r-,r q:%norm Q<CR>qb3f;s (TBD) <Esc>,r-,r q:%norm Q<CR>",
        "Macro a handles a row with a room: 4f; fails on anything with fewer than four semicolons, then "
        "working backwards s)  closes the room, s ( opens it, r- joins the two times and r<Space> separates "
        "the day. :%norm Q converts every row that has a room. Now only the rows without one still have "
        "semicolons, so macro b can start with 3f; without any risk to the finished rows: s (TBD)  fills in "
        "the room, and r- and r<Space> do the rest. A second :%norm Q (Q plays b now) finishes the file. "
        "Going down the file once, playing @a and Q by turns, takes 67 keys."),

    # ---------- qaq … @aq ----------
    "recursive-1": ("+qaqqaf=s = <Esc>IHTTP_<Esc>A,<Esc>+@aqQ",
        "+ goes to OK. qaq records nothing into a, which empties it. Then record the row: f= finds "
        "the =, s = <Esc> spaces it out, IHTTP_ adds the prefix, A, the comma, and + moves on. The @a "
        "at the end does nothing while you record (a is empty), and the final Q (the macro you just "
        "recorded; @a works too) runs the whole chain until f= fails on the }; line, before changing "
        "it. In a drill registers start empty, so qaq isn't strictly needed, and 4Q (or 99Q) instead "
        "of the recursion is a few keys shorter. A Q inside the macro instead of @a works too and "
        "saves a key, but then the macro calls whatever you recorded last, so it breaks as soon as "
        "you record another one; in your own Neovim, always clear the register first."),
    "recursive-2": ("qaqqa/function <CR>cwconst<Esc>wea = <Esc>f{i=> <Esc>@aqQ",
        "qaq empties a. The macro searches for the next \"function \" (with the space), cw types const "
        "over it, w and e reach the end of the name where a = adds the equals sign, and f{ with i=> "
        "adds the arrow. Then it calls itself with @a, and the final Q starts the chain. The cursor "
        "starts on the first function, so the first search finds scale, then clamp, then wraps around "
        "to add. After that no \"function \" is left, the search fails, and the recursion stops. 2Q in "
        "place of the recursion is shorter here, but you'd have to count the functions."),
    "recursive-3": ("qaqqavipJ}j@aqQ",
        "vip selects the paragraph however many lines it has, and J joins them. } goes to the blank "
        "line after it, j to the start of the next paragraph, and @a starts over; the final Q starts "
        "the first run. On the last paragraph } goes to the end of the file and j fails, which ends "
        "the recursion after the last join. qavipJ}jq2Q does the same in 11 keys when you know there "
        "are three paragraphs."),
    "recursive-4": ("qaqqaws: <Esc>f r<CR>@aqQ",
        "qaq empties a. Then record on the first field: w jumps from the start of the line to the = "
        "(punctuation is a word of its own, and every key here is one word), s: <Esc> turns it into "
        "\": \", f<Space> finds the space before the next field, and r<CR> replaces that space with a "
        "line break. That leaves the cursor at the start of the new line, right where the next run "
        "should begin, so the macro needs no other move. @a calls the still-empty register, q stops, "
        "and Q starts the chain. On the last field, took=1532ms, s: still runs but f<Space> finds "
        "nothing, and the recursion ends. f= in place of w costs one key more and doesn't care how the "
        "keys look. Without a macro, each field needs two different changes, so ; and . can't share "
        "the work and it takes about twice as many keys. qa…q6Q instead of the recursion is 4 keys "
        "shorter here (99Q, 3), since registers start empty and you can count the seven fields."),
    "recursive-5": ("qaqqa/D<CR>$V%d@aqQ",
        "qaq empties a. The macro searches with /D<CR>: a capital letter makes the search "
        "case-sensitive (smartcase), and the only capital D in the method is in isDebugEnabled. $ goes "
        "to the { at the end of that line, V starts a linewise selection, and % jumps to the matching "
        "}, so the selection covers the whole block whether it holds one statement or two; d deletes "
        "it. @a calls the macro again, and the final Q starts the chain. When the last block is gone "
        "the search fails (it wraps around the end of the file, but there's nothing left to find) and "
        "the recursion stops. . can't do this: it repeats d on the same number of lines, and the "
        "blocks alternate between 3 and 4 lines, so by hand every block costs n and a fresh d2j or "
        "d3j, 22 keys in all. qa/D<CR>$V%dq4Q is 4 keys shorter when you count the five blocks."),
    "recursive-6": ("qaqqa+f(xdb$x@aqQ",
        "qaq empties a. Record from the def line: + moves to the first assignment and f( finds the "
        "call's parenthesis. x deletes it, which glues the name to its argument (introw[...]), so db "
        "deletes back to the start of that word: just int. $x deletes the ) at the end of the line. "
        "@a calls the macro again, and Q starts the chain. The return line has no (, so f( fails "
        "there before anything changes, and the recursion stops. % looks like the natural way to "
        "find the closing ), but in this setup % comes from the matchit plugin, which doesn't fail on "
        "a line without brackets, so it wouldn't stop the recursion (it would delete the r of "
        "return). yi( with BD\"0p also works (i( finds the parentheses ahead of the cursor) and "
        "stops on the return line too, but it's a key longer. qa…q5Q is 4 keys shorter when you count "
        "the six assignments."),

    # ---------- qA ----------
    "append-macro-1": ("qa+I{ \"<Esc>f,s\", <Esc>A },<Esc>qQ+QqAF i, INPUT<Esc>q2Q",
        "The macro starts with +, so qa+ … q is recorded from the first line: + moves to led, I{ \" "
        "and f,s\", <Esc> and A }, convert it. Q does buzzer. + steps over the comment and Q does "
        "button. Now qA records onto the end of a: F<Space> finds the space before }, and i, INPUT "
        "adds the field to button. 2Q runs the longer macro on sensor and door: after qA, Q plays a "
        "with the added keys. Recording a second macro from scratch, or adding , INPUT to each input "
        "with ., takes more keys."),
    "append-macro-2": ("qa+ICase(\"<Esc>f,s\", <Esc>;a <Esc>A),<Esc>q2Q+QqAi.xfail()<Esc>q2Q",
        "qa+ … q records the conversion on add: + moves down, ICase(\" opens the call, f,s\", replaces "
        "the first comma, ; with a<Space> spaces out the second, and A), closes it. 2Q does sub and "
        "mul, + skips the comment and Q does div. qA then adds i.xfail()<Esc> to the macro and runs "
        "it on div right away: A), left the cursor on the last comma, so i puts .xfail() before it. "
        "2Q does mod and pow."),
    "append-macro-3": ("qa+I![<Esc>f,s](<Esc>A)<Esc>q2Q+QqAi \"icon\"<Esc>q3Q",
        "Record from the heading: + moves to home, I![ and f,s]( turn it into a link, A) closes it. "
        "2Q does editor and settings. + skips ## Icons and Q converts save. qAi \"icon\"<Esc>q appends "
        "the title step and runs it on save at once: the cursor is on the ) that A) typed, so i puts "
        "the title before it. 3Q does the other three icons."),
    "append-macro-4": ("qa+Imkdir -p <Esc>qQ+QqAWYochown app:app <C-r>\"<Esc>q3Q",
        "Record from the comment: + moves to /var/cache/app and Imkdir -p <Esc> adds the command. Q "
        "does /var/tmp/app, + steps over the second comment and Q does /var/log/app. Now qA records "
        "onto the end of a: the cursor is on the space after -p, so W reaches the path and Y yanks it "
        "(Y is y$), o opens a line below, and chown app:app Ctrl-r \" types the path again. 3Q does "
        "the other three paths: each run's + starts from the chown line the run before added, so it "
        "lands on the next path. yypc2Wchown app:app<Esc> in place of WYo… costs the same 20 keys. "
        "Converting everything first and adding the chown lines afterwards takes more: . can't repeat "
        "them, because . after Ctrl-r types the old path again, and a block insert for mkdir would "
        "also hit the comment between the groups."),
    "append-macro-5": ("qa+Iparser.add_argument(\"<Esc>A\")<Esc>qQ+QqAxJs, help=\"<Esc>A\")<Esc>q2Q",
        "Record from the parser line: + moves to --verbose, Iparser.add_argument(\" opens the call and "
        "A\") closes it. Q does --dry-run, + steps over the comment and Q does --output. qA then adds "
        "the help step and runs it on --output: x deletes the ), J joins the help line with one "
        "space and leaves the cursor on that space, s, help=\" replaces it, and A\") closes the "
        "string and the call. 2Q does --format and --since: the help line was joined away, so each "
        "run's + lands on the next option. Pulling the help in with J then h2s for the ) and the "
        "space is a key longer. Recording a second macro would mean typing parser.add_argument(\" "
        "again, and . can't repeat a change made of several edits."),
    "append-macro-6": ("qa+ea():<Esc>A;<Esc>qQ+QqAi><Esc>BiPromise<lt><Esc>q3Q",
        "Record from the interface line: + moves to count, e reaches the end of the name and a(): "
        "adds the parentheses, A; ends the line. Q does current, + steps over // remote and Q does "
        "fetchUsers. qA then appends the wrapper and runs it at once: A; left the cursor on the ;, so "
        "i> closes the Promise right there, and B goes back to the start of the type (User[]> is one "
        "WORD) for iPromise<. 3Q does the other three. Typing iPromise< first and then f;i> is a key "
        "longer. Leaving the ; out of the macro (qA can add >; for the remote rows) and giving the "
        "first two rows theirs with a block $A afterwards takes 41 keys."),

    # ---------- "ap "ay$ ----------
    "edit-macro-1": ("fFrf0\"ay$dd@a",
        "Read the macro: 0F= searches backward from column 1, so it fails at once. fF jumps to the F "
        "and rf makes it f=. The macro ends by calling @a, so it only works from register a: 0\"ay$ "
        "yanks the line without its line break (with \"ayy, the line break would play as an extra j "
        "and skip every other row). dd deletes the line, and @a runs the macro, which keeps calling "
        "itself until j fails on the last row. Q can't start it: Q plays the macro you last recorded, "
        "and this one was yanked, not recorded. Played from the yank register instead, the @a inside "
        "would call an empty register and stop after one row."),
    "edit-macro-2": ("qa+f,lDIpinMode(<C-r>\", OUTPUT); // <Esc>$xq2Qj\"apFOcwINPUT<Esc>0\"ay$D5Q",
        "Record the outputs: + moves to led, f,l moves onto the number and D cuts it, IpinMode( types "
        "the call, Ctrl-r \" puts the number back, and the rest of the line plus $x (deleting the "
        "comma) finish it. 2Q does buzzer and relay. Then j goes to the blank line and \"ap pastes the "
        "macro as text, leaving the cursor at its end, so FO finds OUTPUT and cw changes it to INPUT. "
        "0\"ay$ yanks the fixed macro back into a and D empties the line again. 5Q does the inputs: Q "
        "plays register a, the one you recorded last, with whatever it holds now. Recording a second "
        "macro would cost about 35 keys, and running the OUTPUT macro on the inputs and fixing each "
        "line afterwards takes 7 more than this. The pasted text may show <80><fd>5 right after f,: "
        "that's a do-nothing key that got recorded while f waited for its character. Leave it in; "
        "it's ignored when the macro plays."),
    "edit-macro-3": ("fArI0\"ay$dd:%norm @a<CR>",
        "Read the macro: f; finds the semicolon (so lines without one are skipped), b and yiw yank "
        "the name, and then Apublic would type at the end of the line. fA finds that A and rI makes "
        "it Ipublic. :%norm runs the macro again for every line, and the macro yanks a word each "
        "time, so it can't be played from the yank register: 0\"ay$ puts it in a. dd deletes line 1, "
        "and :%norm @a turns every field into an accessor. (:%norm Q wouldn't work: nothing was "
        "recorded.) The comments, blank lines and the class lines have no semicolon, so f; fails and "
        "they're skipped."),
    "edit-macro-4": ("j\"ap2F,r;0\"ay$D+@a",
        "j goes to the blank line, and \"ap pastes the macro there as text, with the cursor on its last "
        "key. Read it: I types the start of the statement, f, finds the separator and s', ' replaces "
        "it, A'); closes the row, and +@a moves on and calls itself. It has two commas, the one after "
        "f and the one inside ', ', so 2F, jumps back over both to the first, and r; turns f, into f;. "
        "The macro calls @a, so the fixed version has to be in register a: 0\"ay$ yanks the line "
        "without its line break (\"ayy would add one, which plays as an extra j and skips every other "
        "row). D empties the line again, + goes to ada, and @a runs the macro, which calls itself "
        "until + fails on the last row. 0f,r; is the same length as 2F,r;. Changing each ; in the "
        "data to a comma instead (f;r, and then +;. on every row) takes 29 keys, and recording the "
        "macro again about 50."),
    "edit-macro-5": ("fjr+3B\"ay$2+@a",
        "Read the macro in the comment: f, finds the comma, s\", \" splits the fields, I    (\" and "
        "A\"), wrap the row, and j@a moves down and calls itself. But A\"), leaves the cursor at the "
        "end of a long line, and j keeps that column: the next row is shorter, so the cursor lands "
        "past its comma, f, fails, and the recursion stops after one row. + goes to the start of the "
        "next line instead. fj finds the j (it's the only one on the line) and r+ fixes it in the "
        "comment. 3B goes back three WORDs to the macro's first key (^[ isn't a space, so "
        "(\"^[A\"),^[+@a is a single WORD), and \"ay$ yanks from there to the end of the line: just "
        "the macro, into register a, where its @a can find it. 2+ goes to the start of the eur row "
        "(3G would keep the cursor's column, because Neovim leaves 'startofline' off, so f, would "
        "start past the comma), and @a converts every row until f, fails on the ] line. F:w in place "
        "of 3B is a key longer, and recording a new macro would cost about twice as much."),
    "edit-macro-6": ("O<Esc>\"apFIi;.<Esc>0\"ay$dd2j@a",
        "qA can't add the missing step: it appends keys after the @a, and those never run, because "
        "the recursion ends by failing. So edit the macro as text: O<Esc> opens an empty line above "
        "the table, and \"ap pastes the macro there with the cursor on its last key. FI jumps back to "
        "the I (the only capital I in it), and i;.<Esc> puts two keys right after the first ^[: ; "
        "repeats f, to find the second comma, and . repeats s | on it. The macro calls @a, so "
        "0\"ay$ yanks it back into a, and dd deletes the line. 2j goes down to the first row (dd "
        "left the cursor in the first column) and @a runs the macro, which calls itself until + "
        "fails on the last row. Changing the macro's last a to 0 and playing it from the yank "
        "register costs a key more. Recording a new macro, even with a count instead of the "
        "recursion, takes 25 keys, and running the old one and then fixing the third column row by "
        "row takes 32."),

    # ---------- yyp Ctrl-a ----------
    "counter-1": ("qayyp<C-a>f\"<C-a>q4Q",
        "yyp copies the line and puts the cursor at its start, so Ctrl-a bumps the first number, the "
        "1 in b1. The cursor is now on that number; f\" moves past it to the label, and Ctrl-a bumps "
        "the 1 in \"Button 1\". 4Q makes buttons 3 to 6, each copying the line the run before made. "
        "With g Ctrl-a (Project 04) you'd need two separate selections, one for each column of "
        "numbers."),
    "counter-2": ("qayyp<C-a>$1024<C-a>q3Q",
        "yyp copies the line and Ctrl-a turns TIMER0 into TIMER1. $ jumps to the end of the hex "
        "number and 1024 Ctrl-a adds 1024, which is 0x400 (a count is always decimal, but Ctrl-a "
        "keeps the number in hex). 3Q makes TIMER2 to TIMER4: 0x40000c00 plus 0x400 rolls over to "
        "0x40001000."),
    "counter-3": ("/step<CR>ea 1<Esc>qayiwnea <C-r>0<Esc><C-a>q3Q",
        "/step<CR> finds the first comment, and ea 1 numbers it by hand. Then record: yiw yanks the "
        "number under the cursor, n finds the next step, ea <C-r>0 types the same number after it, "
        "and Ctrl-a makes it one higher. The cursor ends on that number, ready for the next run, and "
        "3Q numbers the last three. g Ctrl-a can't do this: it would also bump 16, 0 and 1 in the "
        "code."),
    "counter-4": ("qayyp$<C-x>F.<C-a>q4Q",
        "yyp copies the line. The host name comes first: $ jumps to its number, and Ctrl-x, not "
        "Ctrl-a, makes it node-2. The - right before the 1 reads as a minus sign, so the number is -1: "
        "Ctrl-a would give 0 (node0), while Ctrl-x takes 1 away and gives -2. F. then goes back to the "
        "last dot of the IP, and Ctrl-a finds the number after it and makes 11 into 12. 4Q makes "
        "node-3 to node-6, each from the line the run before made. A plain Ctrl-a right after yyp "
        "would bump the 10 at the start of the IP. Copying the line five times and bumping two "
        "Visual block columns with g Ctrl-a (a block that starts after the - counts the number as "
        "positive) takes 17 keys."),
    "counter-5": ("Gqaykjp<C-a>j<C-a>W10<C-a>q3Q",
        "G goes to the assert line, where the macro starts, so each run ends where the next begins. "
        "yk yanks it and the def line above (the cursor moves up to the def), j comes back down, and "
        "p puts the two-line copy below. The cursor is now at the start of the new def line, and "
        "Ctrl-a bumps test_level_1. j keeps the column, which on the assert line is inside "
        "assertEqual, so Ctrl-a there finds score(1) and makes it 2. W jumps to the 10) after it, and "
        "10 Ctrl-a adds 10. 3Q makes levels 3 to 5. g Ctrl-a can't help here: in a selection that "
        "covers both kinds of line it would bump every line by a different amount, and the copies "
        "need two lines each."),
    "counter-6": ("qayyp<C-a>f(7<C-a>;7<C-a>q4Q",
        "yyp copies the line, and Ctrl-a bumps the first number on it: the 01 in events_w01, which "
        "becomes 02 (Ctrl-a keeps the leading zero). f( reaches the opening ( of the first bound and "
        "7 Ctrl-a adds a week to the number after it. ; repeats the f( to reach the second bound, and "
        "7 Ctrl-a moves that one too. 4Q makes weeks 3 to 6, each starting from the line the run "
        "before made, so 8 and 15 become 15 and 22, and so on. Bumping three Visual block columns with "
        "g Ctrl-a and 7g Ctrl-a takes more than 25 keys, and a block over just the 0 of 01 would only "
        "change that digit (w11)."),
}
