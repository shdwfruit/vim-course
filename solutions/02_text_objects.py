"""Reference solutions for Project 02 (spoilers!). Each entry: exercise name -> (keys, explanation).

See one with:  python3 check.py --show N      Watch it typed:  python3 check.py --watch N
"""
SOLUTIONS = {
    "drop-word": ("daw",
        "daw deletes \"a word\": the word plus the white space after it, or, when there isn't any (here "
        "the closing quote follows), the white space before it. So the space before successfully goes "
        "too. bdw would leave a stray space inside the quotes, and bXdw takes one key more."),
    "drop-sentence": ("das",
        "das deletes \"a sentence\" plus the space after it, so \"It adds a\" moves up neatly after "
        "\"Vim.\". A sentence ends at . ! or ? followed by a space or the end of the line, so it can span "
        "lines. dis would leave two spaces. The sentence motions ( and ) do the same here as (d)."),
    "drop-notes": ("dap",
        "dap deletes \"a paragraph\": the lines up to the next blank line, plus the blank lines after "
        "it. It works line-wise from any line of the paragraph. dip would leave the blank line at the "
        "top of the file. kd3j works too, one key longer."),
    "change-prompt": ("ci\"Name: ",
        "The cursor starts at the beginning of the line, before the string. When you're not inside a "
        "string, ci\" looks forward along the line for the next one, so there's no need to move first. "
        "The fastest way without it, fEct\"Name: , is two keys longer."),
    "change-host": ("ci'localhost",
        "ci' changes everything between the single quotes around the cursor, so it doesn't matter that "
        "the cursor is in the middle of the string. Without it you'd go back first: T'ct' takes two "
        "more keys. Careful with a cursor between two strings, such as on the colon: Vim pairs the "
        "quotes from the start of the line, and the text between strings looks like a string too."),
    "shout-title": ("gUi\"",
        "gU is the uppercase operator from Project 03, and i\" is the inside of the next string. Like "
        "every object, it works after any operator. f\"gU$ also works here, in 5 keys, because gU leaves "
        "the quote and the semicolon alone."),
    "last-item": ("ci[-1",
        "ci[ looks ahead for the next [ (the cursor isn't inside one), then changes everything up to its "
        "partner ]. It counts nesting and isn't fooled by the parentheses in between. f[lct]-1 is three "
        "keys longer."),
    "copy-args": ("yi(j$P",
        "yi( yanks inside the first parentheses on the line, without moving there first. j moves down, "
        "$ lands on the ) of scatter(), and P puts the text before the cursor, inside the parentheses. "
        "yi(jf)P works too, one key longer."),
    "type-args": ("ci<lt>Row",
        "ci< finds the first < on the line and changes everything inside it, up to the > that matches "
        "it, so the nested Map<String, Integer> goes in one go. f<lc2t>Row also works, in 10 keys."),
    "outer-args": ("c2i(dx, dy",
        "i( alone would be the inside of abs( ), the innermost pair around the cursor. With a count, "
        "2i( goes out one more level, to the inside of max( ). 2F(ci( reaches the same place in two "
        "more keys. Starting from 0, ci( would pick the if's parentheses instead."),
    "stub-body": ("ci{// TODO",
        "ci{ changes everything between the braces. When { ends its line and } starts its own, the "
        "inner part is whole lines, so the braces stay on their lines and Insert mode starts on an "
        "empty line indented to match. kc2j does the same change in one more key."),
    "paragraph-text": ("jjcitStart here.",
        "jj moves down to the <p> line, still in the indentation. cit changes the inside of the tag "
        "you're in. From the indentation, Vim starts at the first tag on the line, so that's the <p>. "
        "The inner part includes the nested <b>full</b>, which is why ct< can't do this."),

    "review-signup": ([
        ("2fgcwpost<Esc>", "step 1: the first g on the line is in signup, so 2fg."),
        ("/<lt>e<CR>da<lt>", "step 2: a< is the whole <em>, angle brackets included."),
        ("f<lt>.", "f< reaches </em>, and . deletes it too."),
        ("/N<CR>dap", "step 3: with smartcase, a capital N matches only a capital, so /N finds Name. dap takes "
                      "the label, the input and the blank line after them."),
        ("3{p", "three { back is the blank line above the email label, and p puts the block below it."),
        ("/-<CR>x", "step 4."),
        ('/x<CR>ci"email<Esc>', "step 5: the first x is in text. From inside a string, ci\" changes all of it."),
        ('nci"password<Esc>', "step 6: n finds the next x, in the password input's text."),
        ("/M<CR>das", "step 7: das deletes the sentence and the space after it."),
        ("jf,dt)", "step 8: dt) deletes from the comma up to the )."),
    ], "Each edit is a search and a text object. A search for one letter that only appears where you're going "
       "is often the shortest motion, and with ignorecase and smartcase a capital letter narrows it down. "
       "ap moves the label and input with their blank line, so the spacing comes out right. Measured: /xt "
       "instead of /x and /me\" instead of /N each cost more; typing the heading again with cit costs far "
       "more than deleting the two tags."),
    "review-report": ([
        ('jfMci"Q3<Esc>', "step 1: inside the string, ci\" replaces all of it."),
        ("jfUREUR<Esc>", "step 2: EUR is as long as USD, so R types over it."),
        ("jjdd", "step 3."),
        ('3jci"utf-8<Esc>', "step 4: from the start of the line, ci\" looks ahead for the first string, "
                            "\"latin-1\"."),
        ("f,dt)", "step 5: from the comma after it, dt) deletes up to the )."),
        ("Gdap", "step 6: at the end of the file, ap takes the blank lines above total() instead of below."),
        ("{kkp", "{ is the blank line above render(), and two lines up is the end of load(). p puts the blank "
                 "lines and total() below it."),
        ("8jf.df)", "step 8 first: df) deletes .upper(), through its )."),
        ("5kf..", "step 7: back in total(), . deletes .strip() the same way..."),
        ("$P", "...and P puts it back before the last ), at the end of the filter."),
        ("6jhda[", "step 9: j lands on the : after ], h steps onto the ], and da[ deletes [1:] with its "
                   "brackets."),
    ], "Top to bottom, except for one swap: .upper() and .strip() both go with df), so .upper() goes first, "
       "and . does .strip(), which then goes back in at the end of the filter. Moving a function is one dap "
       "and a p: at the end of a file ap takes the blank lines above, so the block brings its own spacing. "
       "Measured: doing .strip() first costs 2 more, because . would then put instead of delete."),
}
