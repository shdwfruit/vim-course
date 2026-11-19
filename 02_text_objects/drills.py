"""Drills for Project 02: short problems that practice one command at a time.
Play them with:  python3 check.py drill      (the reference solutions are in ../solutions/drills/)"""
from trainer import Drills, text

drills = Drills(__file__)

# ---------- iw aw ----------

iw = drills.command(
    "iw", "iw  aw", "a word",
    """iw is the word under the cursor, and aw is the word plus the white space after it, or the white space
    before it when there's none after (say, before a period or a closing quote). A word is a run of letters,
    digits and underscores, or a run of other punctuation, just like for w. On white space, iw is the whole run
    of white space, and aw is that plus the next word. Where in the word the cursor is doesn't matter, and a
    count takes more words. Rule of thumb: delete with aw, so the spacing stays right, and change with iw.""",
    examples=[("ciw", "change the word under the cursor"), ("daw", "delete the word and its space"),
              ("yiw", "copy the word"), ("gUiw", "uppercase the word"), ("d3aw", "delete three words"),
              ("ciw<Space>", "squeeze white space down to one space")],
)
iw.add(
    title="Rename from the middle", par=7, ext="java", cursor=(1, 7),
    task="Rename count to size. The cursor is in the middle of count.",
    start="int count = items.size();",
    target="int size = items.size();",
    hint="ciw changes the word under the cursor, wherever in the word you are, and leaves you in Insert mode "
         "to type the new one.",
    uses=["c"],
)
iw.add(
    title="Drop the last word", par=3, ext="txt", cursor=(1, 26),
    task='Shorten the commit message to "Fix typo in the README." The cursor is on file.',
    start="Fix typo in the README file.",
    target="Fix typo in the README.",
    hint="aw is a word plus the white space after it. When a period comes right after the word, it takes "
         "the space before the word instead, so daw leaves no stray space.",
    uses=["d"],
)
iw.add(
    title="Squeeze the spaces", par=4, ext="py", cursor=(1, 13),
    task="This line was aligned with a longer setting that has since been deleted. Squeeze the gap before "
         "the = down to a single space. The cursor is in the gap.",
    start="retries            = 3",
    target="retries = 3",
    hint="On white space, iw is the whole run of white space. Change it and type one space.",
    uses=["c"],
)
iw.add(
    title="Close the gap", par=3, ext="py", cursor=(1, 19),
    task="Remove the spaces between compute and its opening parenthesis. The cursor is in the gap.",
    start="result = compute    (x, y)",
    target="result = compute(x, y)",
    hint="diw on white space deletes the whole run of white space, wherever in it the cursor is.",
    uses=["d"],
)
iw.add(
    title="Copy a word and its space", par=5, ext="java", cursor=(1, 10),
    task="Make reset() static too: copy static from line 1. The cursor is on static.",
    start=text("""
        public static int count() {
        public void reset() {
    """),
    target=text("""
        public static int count() {
        public static void reset() {
    """),
    hint="yaw copies the word and the space after it. void is right below static, and P puts text before "
         "the cursor.",
    uses=["y", "p"],
)
iw.add(
    title="Swap two words", par=5, ext="java", cursor=(1, 10),
    task="Java style puts static before final. Swap the two words. The cursor is on final.",
    start="public final static int MAX = 10;",
    target="public static final int MAX = 10;",
    hint="daw deletes final with its space. Then move past static and put it back in front of int with P.",
    uses=["d", "word", "p"],
)
iw.add(
    title="Delete three words", par=4, ext="java", cursor=(1, 46),
    task='Shorten the message to "Cannot read the file". The cursor is on for.',
    start='throw new IOException("Cannot read the file for some reason");',
    target='throw new IOException("Cannot read the file");',
    hint="A count in front of aw takes that many words. With no space after the last one, aw takes the "
         "space before the first one instead.",
    uses=["d", "count"],
)
iw.add(
    title="Shout two constants", par=6, ext="c", cursor=(1, 22),
    task="Constants are written in UPPER_CASE. Uppercase max_users and idle_timeout. The cursor is on "
         "max_users.",
    start=text("""
        static const int max_users = 64;
        const int idle_timeout = 30;
    """),
    target=text("""
        static const int MAX_USERS = 64;
        const int IDLE_TIMEOUT = 30;
    """),
    hint="gU (Project 03) uppercases whatever you give it, so gUiw uppercases the word. j then lands in "
         "the middle of idle_timeout, and . repeats the whole command.",
    uses=["case", "dot"],
)
iw.add(
    title="Same change, two words", par=10, ext="java", cursor=(1, 7),
    task="Raise both log calls to the info level: change debug and trace to info. The cursor is on debug.",
    start=text("""
        log.debug("Loaded " + rows.size() + " rows");
        log.trace("Cache hit rate: " + rate);
    """),
    target=text("""
        log.info("Loaded " + rows.size() + " rows");
        log.info("Cache hit rate: " + rate);
    """),
    hint="Change the word with ciw. On the next line, j lands in the middle of trace, and . repeats the "
         "change: ciw doesn't care where in the word you are.",
    uses=["c", "dot"],
)
iw.add(
    title="Tighten the instructions", par=6, ext="md", cursor=(1, 24),
    task="Delete afterwards and immediately, along with the space before each. The cursor is on "
         "afterwards.",
    start="Restart the server afterwards. Then clear the cache immediately.",
    target="Restart the server. Then clear the cache.",
    hint="daw on a word just before a period takes the space in front of it. $h puts the cursor inside "
         "the last word, and . repeats the daw there.",
    uses=["d", "line", "dot"],
)
iw.add(
    title="A word with digits in it", par=7, ext="css", cursor=(2, 14),
    task="Use rem for the margin: change 120px to 2rem. The cursor is on the 2 of 120px.",
    start=text("""
        .hero {
            margin: 120px auto;
        }
    """),
    target=text("""
        .hero {
            margin: 2rem auto;
        }
    """),
    hint="A word is a run of letters, digits and underscores, so 120px is one word, and ciw changes all of it "
         "from the middle.",
    uses=["c"],
)
iw.add(
    title="A doubled word", par=3, ext="txt", cursor=(1, 17),
    task="The commit message says when twice. Delete one of them. The cursor is on the h of the second when.",
    start="Fix crash when when the cache is empty",
    target="Fix crash when the cache is empty",
    hint="aw is the word and the space after it, so deleting it leaves one space between the words around it.",
    uses=["d"],
)
iw.add(
    title="Fill in the template", par=7, ext="js", cursor=(1, 9),
    task="Log the number of attempts: put retries between the empty braces on line 2. The cursor is in the "
         "middle of retries.",
    start=text("""
        const retries = 3;
        console.log(`attempts: ${}`);
    """),
    target=text("""
        const retries = 3;
        console.log(`attempts: ${retries}`);
    """),
    hint="yiw copies the word under the cursor and moves to its start. Then put it in front of the } on line 2.",
    uses=["y", "f", "p"],
)
iw.add(
    title="is not, not not is", par=6, ext="py", cursor=(1, 5),
    task='Python reads better with "is not": move not so that the line reads if user is not None:. The cursor '
         "is on the o of not.",
    start=text("""
        if not user is None:
            login(user)
    """),
    target=text("""
        if user is not None:
            login(user)
    """),
    hint="daw takes not and its space with it. Then move two words on and put it back.",
    uses=["d", "count", "word", "p"],
)
iw.add(
    title="An arrow is a word too", par=4, ext="txt", cursor=(1, 22),
    task="The pipeline has no test stage anymore. Delete test and the arrow after it. The cursor is on the e "
         "of test.",
    start="start --> build --> test --> deploy",
    target="start --> build --> deploy",
    hint="A run of punctuation like --> is a word of its own. A count in front of aw takes that many words.",
    uses=["d", "count"],
)
iw.add(
    title="Fill in an assignment", par=8, ext="java", cursor=(1, 21),
    task="Finish the constructor line: assign width to this.width, as in the target. The cursor is on the d "
         "of width.",
    start=text("""
        private final int width;
        this. = ;
    """),
    target=text("""
        private final int width;
        this.width = width;
    """),
    hint="Yank the word once and put it in both places. After P the cursor is on the last character it put, "
         "and the dot is behind it.",
    uses=["y", "p", "f"],
)
iw.add(
    title="Three timestamps", par=12, ext="ts", cursor=(3, 18),
    task="The three timestamps should be Date objects: change their type from number to Date, but leave id "
         "alone. The cursor is on the m of the first one.",
    start=text("""
        interface Session {
            id: number;
            createdAt: number;
            updatedAt: number;
            expiresAt: number;
        }
    """),
    target=text("""
        interface Session {
            id: number;
            createdAt: Date;
            updatedAt: Date;
            expiresAt: Date;
        }
    """),
    hint="ciw works from anywhere in the word, and after the change j lands in the middle of the next number. "
         ". repeats the change there.",
    uses=["c", "dot"],
)
iw.add(
    title="No spaces around =", par=5, ext="sh", cursor=(1, 10),
    task="In a shell script, an assignment can't have spaces around the =. Delete both gaps. The cursor is in "
         "the first one.",
    start=text("""
        GREETING   =   "hello"
        echo "$GREETING"
    """),
    target=text("""
        GREETING="hello"
        echo "$GREETING"
    """),
    hint="On white space, iw is the whole gap. Once it's gone, the next gap is one character away, and . "
         "repeats.",
    uses=["d", "dot"],
)
iw.add(
    title="Always needed", par=6, ext="md", cursor=(1, 21),
    task='Both steps are always needed now: delete " if needed" from both lines. The cursor is on if.',
    start=text("""
        Restart the service if needed.
        Reload the configs if needed.
    """),
    target=text("""
        Restart the service.
        Reload the configs.
    """),
    hint="A count in front of aw takes that many words, and with a period after the last one, the space "
         "before the first goes too. Then see where j lands.",
    uses=["d", "count", "dot"],
)
iw.add(
    title="Two more synchronized methods", par=8, ext="java", cursor=(1, 12),
    task="Make get() and clear() synchronized too, like put(). The cursor is on the h of synchronized.",
    start=text("""
        public synchronized void put(K k, V v) { map.put(k, v); }
        public V get(K k) { return map.get(k); }
        public void clear() { map.clear(); }
    """),
    target=text("""
        public synchronized void put(K k, V v) { map.put(k, v); }
        public synchronized V get(K k) { return map.get(k); }
        public synchronized void clear() { map.clear(); }
    """),
    hint="yaw copies the word with the space after it. . repeats a put, once you've got to the right place.",
    uses=["y", "p", "plus", "word", "dot"],
)

# ---------- i" a" i' a' ----------

quote = drills.command(
    "quote", "i\"  a\"  i'  a'", "inside or around quotes",
    """i" is the text inside a double-quoted string, and a" is the string with its quotes. i' a' and i` a` do
    the same for single quotes and backticks. They work from anywhere in the string, and from before it: if
    the cursor isn't in a string, Vim uses the next one on the line (never a later line). a" also takes the
    white space after the closing quote, or before the opening one if there's none after. Escaped quotes
    like \\" are skipped. With the cursor off a quote, Vim pairs the nearest quote before it with the nearest
    one after it, so with the cursor on the gap between two strings, ci" changes the gap.""",
    examples=[('ci"', "change inside the string"), ('di"', "empty the string"),
              ('da"', "delete the string, its quotes and a space"), ("ci'", "change inside single quotes"),
              ('ya"', "copy the string with its quotes"), ('gUi"', "uppercase the string")],
)
quote.add(
    title="Change a greeting", par=11, ext="java", cursor=(1, 27),
    task='Change the greeting to "Hi there". The cursor is on world.',
    start='String greeting = "Hello, world";',
    target='String greeting = "Hi there";',
    hint='ci" changes everything inside the quotes around the cursor. Where in the string you are doesn\'t '
         "matter.",
    uses=["c"],
)
quote.add(
    title="A single-quoted message", par=20, ext="py", cursor=(1, 13),
    task="Change the message to 'Permission denied'. The cursor is on not.",
    start="msg = 'File not found'",
    target="msg = 'Permission denied'",
    hint="Single-quoted strings have their own object: i'.",
    uses=["c"],
)
quote.add(
    title="From the start of the line", par=12, ext="java",
    task='Change the message to "Bad width". The cursor is at the start of the line.',
    start='throw new IllegalArgumentException("Width must be positive");',
    target='throw new IllegalArgumentException("Bad width");',
    hint='You don\'t have to move into the string first. When the cursor is before a string, ci" looks '
         "ahead along the line for it.",
    uses=["c"],
)
quote.add(
    title="Delete a quoted file name", par=3, ext="sh", cursor=(1, 21),
    task='Copy only the first file: delete "Old Notes.txt" and the space after it. The cursor is on Old.',
    start='cp "My Notes.txt" "Old Notes.txt" backup/',
    target='cp "My Notes.txt" backup/',
    hint='a" is the string with its quotes, and like aw it takes the white space after it too.',
    uses=["d"],
)
quote.add(
    title="Copy a key with its quotes", par=5, ext="java",
    task='Read the same setting back: put "timeout", quotes and all, between the parentheses on line 2.',
    start=text("""
        settings.put("timeout", 30);
        settings.get();
    """),
    target=text("""
        settings.put("timeout", 30);
        settings.get("timeout");
    """),
    hint='ya" copies the string with its quotes, and leaves the cursor on the opening quote. The ) on '
         "line 2 is right below it.",
    uses=["y", "p"],
)
quote.add(
    title="Shout two strings", par=6, ext="py",
    task="Python's logging levels are written in capitals. Uppercase both strings.",
    start=text("""
        log_level = "warning"
        fallback_level = "error"
    """),
    target=text("""
        log_level = "WARNING"
        fallback_level = "ERROR"
    """),
    hint='gU (Project 03) uppercases whatever you give it, and i" is the inside of the next string. Then '
         "j and . repeat it on line 2.",
    uses=["case", "dot"],
)
quote.add(
    title="Skip the escaped quotes", par=8, ext="java", cursor=(1, 21),
    task='Replace the whole message with "Hello". The cursor is on hi, between escaped quotes.',
    start='String msg = "Say \\"hi\\" to everyone";',
    target='String msg = "Hello";',
    hint='Vim skips quotes with a backslash in front, so ci" sees one string, from the first quote to the '
         "last.",
    uses=["c"],
)
quote.add(
    title="Point at the same URL", par=8, ext="py",
    task="Point url at the production server: give it the same string as PROD_URL.",
    start=text("""
        PROD_URL = "https://api.example.com/v2"
        url = "http://localhost:8000"
    """),
    target=text("""
        PROD_URL = "https://api.example.com/v2"
        url = "https://api.example.com/v2"
    """),
    hint='Yank inside the first string. On line 2, select inside the string with vi" (Visual mode is '
         "Project 04), and p puts the yanked text over the selection.",
    uses=["y", "visual", "p"],
)
quote.add(
    title="Empty the secrets", par=7, ext="py",
    task="Before you commit this file, empty all three strings.",
    start=text("""
        DB_USER = "admin"
        DB_PASSWORD = "s3cr3t!"
        API_KEY = "sk-29f8a7c1"
    """),
    target=text("""
        DB_USER = ""
        DB_PASSWORD = ""
        API_KEY = ""
    """),
    hint='di" empties a string from inside it or from before it. j and . do the same on the next line.',
    uses=["d", "dot"],
)
quote.add(
    title="Mind the gap", par=21, ext="java", cursor=(1, 15),
    task='Change "Ada Lovelace" to "Margaret Hamilton". The cursor is on the comma between the two '
         "strings.",
    start='map.put("name", "Ada Lovelace");',
    target='map.put("name", "Margaret Hamilton");',
    hint='On the comma, ci" would change the gap between the strings: Vim pairs the nearest quote on each '
         "side of the cursor. Step onto the second string first.",
    uses=["word", "c"],
)
quote.add(
    title="Inline code", par=13, ext="md",
    task="The project uses make now: change the inline code to make check.",
    start="Run `npm test` before you push.",
    target="Run `make check` before you push.",
    hint="Backticks have a quote object of their own, i`, and like i\" it looks ahead along the line.",
    uses=["c"],
)
quote.add(
    title="A single-quoted value", par=10, ext="sql",
    task="Change the country in the query to Germany.",
    start="SELECT name FROM customers WHERE country = 'Netherlands';",
    target="SELECT name FROM customers WHERE country = 'Germany';",
    hint="SQL strings use single quotes. With no quote before the cursor, i' looks ahead for the first string.",
    uses=["c"],
)
quote.add(
    title="Replace a string with a constant", par=12, ext="js",
    task="Use the USERS_URL constant instead of the URL: replace the first string, quotes included.",
    start='const res = await fetch("https://api.example.com/users", { method: "POST" });',
    target='const res = await fetch(USERS_URL, { method: "POST" });',
    hint='a" is the string with its quotes. It only takes white space along when there\'s some right next to '
         "the string.",
    uses=["c"],
)
quote.add(
    title="A new sed script", par=5, ext="sh",
    task="Make the command delete the first line of notes.txt instead: change the sed script to 1d.",
    start="sed -i 's/foo/bar/' notes.txt",
    target="sed -i '1d' notes.txt",
    hint="The script is a single-quoted string, and ci' finds it by looking ahead.",
    uses=["c"],
)
quote.add(
    title="Back to NULL", par=8, ext="sql",
    task="The string 'none' should be a real NULL: replace it, quotes included, with NULL.",
    start="UPDATE users SET nickname = 'none' WHERE id = 42;",
    target="UPDATE users SET nickname = NULL WHERE id = 42;",
    hint="a' takes the space after the closing quote with it. Type the space back, or give i' a count of 2: "
         "that's the quotes without any white space.",
    uses=["c", "count"],
)
quote.add(
    title="A default value", par=9, ext="py",
    task="Pass the default region to get() as a second argument, as in the target.",
    start=text("""
        DEFAULT_REGION = 'eu-west-1'
        region = os.environ.get('AWS_REGION')
        print(f"Using {region}")
    """),
    target=text("""
        DEFAULT_REGION = 'eu-west-1'
        region = os.environ.get('AWS_REGION', 'eu-west-1')
        print(f"Using {region}")
    """),
    hint="At the end of a line, a' takes the space before the opening quote instead. That's half of the \", \" "
         "you need.",
    uses=["y", "line", "insert", "p"],
)
quote.add(
    title="From the closing quote", par=16, ext="py",
    task="Change the help text to destination.",
    start='parser.add_argument("-o", "--output", help="output file")',
    target='parser.add_argument("-o", "--output", help="destination")',
    hint='With quotes before the cursor, Vim uses the nearest ones on each side, so from help= it would change '
         "the gap. On a quote, though, it counts the quotes before it to tell an opening one from a closing one.",
    uses=["line", "c"],
)
quote.add(
    title="Two attributes from one", par=9, ext="html",
    task="Give the input the same id and name as the label's for.",
    start=text("""
        <label for="username">Username</label>
        <input id="" name="">
    """),
    target=text("""
        <label for="username">Username</label>
        <input id="username" name="username">
    """),
    hint='yi" copies the value and moves to its start. P puts it in front of the cursor, and . repeats a put.',
    uses=["y", "p", "line", "dot"],
)
quote.add(
    title="Move the text", par=7, ext="js",
    task="The text is in the wrong string. Move Welcome back from subtitle into title.",
    start=text("""
        const title = "";
        const subtitle = "Welcome back";
    """),
    target=text("""
        const title = "Welcome back";
        const subtitle = "";
    """),
    hint='di" deletes the text into the register, ready to put somewhere else.',
    uses=["d", "p"],
)
quote.add(
    title="Clear three strings", par=7, ext="py",
    task="Reset all three values to empty strings.",
    start='name, email, phone = "Ada", "ada@example.com", "555-0100"',
    target='name, email, phone = "", "", ""',
    hint='di" empties the first string by looking ahead. After that, W jumps to the opening quote of the next '
         "one, and on a quote, . knows which string you mean.",
    uses=["d", "bigword", "dot"],
)

# ---------- i( a( ----------

paren = drills.command(
    "paren", "i(  a(", "inside or around parentheses",
    """i( is everything inside the parentheses around the cursor, and a( adds the parentheses themselves (but
    never the white space around them). i) and ib, and a) and ab, are the same objects. The cursor can be
    anywhere between the parentheses or on either one, and nested pairs inside are skipped, so the ) is
    always the matching one. When the cursor isn't inside any pair, they look ahead for the next (, even on
    later lines. When ( ends its line and ) starts its own, i( is the whole lines between them.""",
    examples=[("ci(", "change the arguments"), ("di(", "empty the parentheses"),
              ("ca(", "change them, parentheses included"), ("yi(", "copy the arguments"),
              (">i(", "indent the lines inside"), ("vi(", "select inside them")],
)
paren.add(
    title="Change the arguments", par=17, ext="java", cursor=(1, 18),
    task="Change the arguments to x1, y1, x2, y2. The cursor is on width.",
    start="drawLine(0, 0, width, height);",
    target="drawLine(x1, y1, x2, y2);",
    hint="ci( changes everything inside the parentheses around the cursor.",
    uses=["c"],
)
paren.add(
    title="Empty the call", par=3, ext="py",
    task="Remove the argument, so ArgumentParser() is called with none.",
    start='parser = argparse.ArgumentParser(description="Resize images")',
    target="parser = argparse.ArgumentParser()",
    hint="di( deletes inside the parentheses. When the cursor isn't inside a pair, it looks ahead for the "
         "next (.",
    uses=["d"],
)
paren.add(
    title="Name the subtotal", par=11, ext="py", cursor=(1, 19),
    task="Replace (price * qty), parentheses included, with subtotal. The cursor is on qty.",
    start="total = (price * qty) * (1 + tax)",
    target="total = subtotal * (1 + tax)",
    hint="a( is the parentheses and everything in them.",
    uses=["c"],
)
paren.add(
    title="Copy the outer arguments", par=5, ext="py", cursor=(1, 30),
    task="Give price_for() the same arguments as rect_area(). The cursor is on height.",
    start=text("""
        area = rect_area(width(box), height(box))
        cost = price_for()
    """),
    target=text("""
        area = rect_area(width(box), height(box))
        cost = price_for(width(box), height(box))
    """),
    hint="The cursor is inside rect_area( ), but not inside height( ). yi( copies the arguments, nested "
         "parentheses and all, and moves to the start of them. Look at what's right below.",
    uses=["y", "p"],
)
paren.add(
    title="Look ahead to the next line", par=3, ext="c",
    task="Call init_window() with no arguments. The cursor is on the comment line above it.",
    start=text("""
        /* Use the default window settings. */
        init_window(800, 600, "Untitled", FULLSCREEN);
    """),
    target=text("""
        /* Use the default window settings. */
        init_window();
    """),
    hint="Unlike the quote objects, the bracket objects keep looking for the next ( on later lines.",
    uses=["d"],
)
paren.add(
    title="Past the first )", par=10, ext="java", cursor=(1, 21),
    task="Log the summary variable instead: replace everything inside log.info( ) with summary. The "
         "cursor is on format.",
    start='log.info(String.format("%d items", list.size()));',
    target="log.info(summary);",
    hint="ci( uses the pair around the cursor, and counts the nested pairs to find the ) that really "
         "matches.",
    uses=["c"],
)
paren.add(
    title="Indent the arguments", par=3, ext="py", cursor=(3, 1),
    task="Indent the three arguments by one level. The cursor is on json=payload.",
    start=text("""
        response = requests.post(
        url,
        json=payload,
        timeout=10,
        )
    """),
    target=text("""
        response = requests.post(
            url,
            json=payload,
            timeout=10,
        )
    """),
    hint="When ( ends its line and ) starts its own, i( is the whole lines in between. > shifts them right.",
    uses=["indent"],
)
paren.add(
    title="Clear every call", par=7, ext="py",
    task="Call all three functions with no arguments.",
    start=text("""
        setup(verbose=True)
        run(debug=True, workers=4)
        teardown(force=True)
    """),
    target=text("""
        setup()
        run()
        teardown()
    """),
    hint="di( empties the parentheses, looking ahead when the cursor isn't inside a pair. j and . repeat it "
         "on each line.",
    uses=["d", "dot"],
)
paren.add(
    title="Put over the arguments", par=8, ext="py",
    task="Draw the padded rectangle: give draw_rect() the four values from bounds.",
    start=text("""
        bounds = (x + pad, y + pad, w - 2 * pad, h - 2 * pad)
        draw_rect(0, 0, w, h)
    """),
    target=text("""
        bounds = (x + pad, y + pad, w - 2 * pad, h - 2 * pad)
        draw_rect(x + pad, y + pad, w - 2 * pad, h - 2 * pad)
    """),
    hint="Yank inside the first parentheses. On line 2, select inside draw_rect's with vi( (Visual mode "
         "is Project 04), and p puts the yanked text over the selection.",
    uses=["y", "visual", "p"],
)
paren.add(
    title="Copy, then adjust", par=8, ext="java",
    task="Give end the same arguments as start, but with 25 instead of 20.",
    start=text("""
        Point start = new Point(margin + 10, margin + 20);
        Point end = new Point();
    """),
    target=text("""
        Point start = new Point(margin + 10, margin + 20);
        Point end = new Point(margin + 10, margin + 25);
    """),
    hint="Yank inside start's parentheses and put the text inside end's. After P, the cursor is on the "
         "last character it put, which is the digit to fix.",
    uses=["y", "p", "r"],
)
paren.add(
    title="Drop a cast", par=3, ext="c",
    task="strlen() already returns a size_t: delete the cast, parentheses and all.",
    start="size_t n = (size_t)strlen(name);",
    target="size_t n = strlen(name);",
    hint="a( is the parentheses and what's in them. The cursor doesn't have to be inside: the bracket objects "
         "look ahead.",
    uses=["d"],
)
paren.add(
    title="Relabel an arrow", par=6, ext="txt",
    task="The web server talks to the API over plain TCP now. Change the first arrow's label to TCP.",
    start="[web] --(HTTP)--> [api] --(SQL)--> [db]",
    target="[web] --(TCP)--> [api] --(SQL)--> [db]",
    hint="Parentheses in ASCII art are parentheses all the same, and i( looks ahead for the first pair.",
    uses=["c"],
)
paren.add(
    title="Command substitution", par=9, ext="sh",
    task="Use id -un instead of whoami, which some minimal systems don't have.",
    start=text("""
        user=$(whoami)
        echo "Hello, $user"
    """),
    target=text("""
        user=$(id -un)
        echo "Hello, $user"
    """),
    hint="$( ) is a pair of parentheses like any other.",
    uses=["c"],
)
paren.add(
    title="Count every row", par=4, ext="sql",
    task="Count every visit, not just the distinct users: make it COUNT(*).",
    start="SELECT COUNT(DISTINCT user_id) FROM visits;",
    target="SELECT COUNT(*) FROM visits;",
    hint="Change inside the parentheses. They're the first pair on the line.",
    uses=["c"],
)
paren.add(
    title="Dedent the arguments", par=4, ext="py", cursor=(4, 1),
    task="The arguments are indented two levels too deep. Shift them left twice. The cursor is on the action "
         "line.",
    start=text("""
        def main():
            parser.add_argument(
                        "--verbose",
                        action="store_true",
                        help="print more",
            )
    """),
    target=text("""
        def main():
            parser.add_argument(
                "--verbose",
                action="store_true",
                help="print more",
            )
    """),
    hint="When ( ends its line and ) starts its own, i( is the whole lines in between. < shifts lines left, "
         "and . does it again.",
    uses=["indent", "dot"],
)
paren.add(
    title="Reuse a subquery", par=5, ext="sql",
    task="Finish the DELETE: it needs the same subquery as the SELECT, parentheses included.",
    start=text("""
        SELECT * FROM orders WHERE customer_id IN (SELECT id FROM vip);
        DELETE FROM coupons WHERE customer_id IN ;
    """),
    target=text("""
        SELECT * FROM orders WHERE customer_id IN (SELECT id FROM vip);
        DELETE FROM coupons WHERE customer_id IN (SELECT id FROM vip);
    """),
    hint="ya( copies the parentheses with what's in them, and leaves the cursor on the (. Line 2 is shorter "
         "than that.",
    uses=["y", "line", "p"],
)
paren.add(
    title="Pass null to every setter", par=12, ext="java",
    task="To test the validation, call all three setters with null.",
    start=text("""
        user.setName(input.name());
        user.setEmail(input.email());
        user.setPhone(input.phone());
    """),
    target=text("""
        user.setName(null);
        user.setEmail(null);
        user.setPhone(null);
    """),
    hint="ci( skips the nested pair of parentheses to find the ) that matches. After the first change, j lands "
         "inside the next setter's call.",
    uses=["c", "dot"],
)
paren.add(
    title="Same arguments, twice", par=7, ext="py",
    task="Pass rows and schema to transform() and save() too.",
    start=text("""
        validate(rows, schema)
        transform()
        save()
    """),
    target=text("""
        validate(rows, schema)
        transform(rows, schema)
        save(rows, schema)
    """),
    hint="yi( leaves the cursor at the start of what it copied. Look at what j lands on in each line: p puts "
         "after the cursor, P before it.",
    uses=["y", "p"],
)
paren.add(
    title="Name the parts", par=16, ext="py",
    task="Both factors have names now. Replace the first, parentheses included, with gross, and the second "
         "with rate.",
    start="total = (price + shipping) * (1 - discount)",
    target="total = gross * rate",
    hint="a( is the parentheses and what's in them. Outside every pair it looks ahead, so after the first "
         "change you don't need to move.",
    uses=["c"],
)
paren.add(
    title="Replace a list of values", par=11, ext="sql",
    task="Only show closed tickets: replace the three statuses with 'closed', on a line of its own.",
    start=text("""
        SELECT * FROM tickets
        WHERE status IN (
            'new',
            'open',
            'reopened'
        );
    """),
    target=text("""
        SELECT * FROM tickets
        WHERE status IN (
            'closed'
        );
    """),
    hint="The bracket objects look ahead onto later lines. When ( ends its line and ) starts its own, ci( "
         "replaces the lines between them with one fresh line.",
    uses=["c"],
)

# ---------- i{ a{ ----------

brace = drills.command(
    "brace", "i{  a{", "inside or around braces",
    """i{ is everything inside the curly braces around the cursor, and a{ includes the braces. i} and iB, and
    a} and aB, are the same objects. Like i( they work from anywhere inside or on a brace, skip nested pairs,
    and look ahead for the next { when the cursor isn't inside one. When { ends its line and } starts its
    own, as in most C and Java code, i{ is the whole lines between them: di{ empties a function body and
    leaves both braces in place, and ci{ replaces the body with one fresh, indented line.""",
    examples=[("ci{", "replace a block's contents"), ("di{", "empty a function body"),
              ("ca{", "replace a block, braces included"), ("yi{", "copy a body"), (">i{", "indent a body"),
              ("=i{", "re-indent a body")],
)
brace.add(
    title="Reset an array", par=4, ext="c", cursor=(1, 21),
    task="Start the scores from scratch: make the initializer {0}. The cursor is on 85.",
    start="int scores[] = {90, 85, 77};",
    target="int scores[] = {0};",
    hint="ci{ changes everything inside the braces around the cursor.",
    uses=["c"],
)
brace.add(
    title="Empty a function", par=3, ext="c", cursor=(3, 5),
    task="Empty the body of debug_dump(), keeping both braces. The cursor is on the middle printf.",
    start=text("""
        void debug_dump(void) {
            printf("count=%d\\n", count);
            printf("total=%d\\n", total);
            printf("avg=%f\\n", avg);
        }
    """),
    target=text("""
        void debug_dump(void) {
        }
    """),
    hint="When { ends its line and } starts its own, i{ is the whole lines between them.",
    uses=["d"],
)
brace.add(
    title="Rewrite a function body", par=27, ext="c", cursor=(3, 5),
    task="Clear the struct in one go: replace the three assignments in reset() with a single memset() "
         "call, as in the target. The cursor is on the middle assignment.",
    start=text("""
        void reset(struct counter *c) {
            c->hits = 0;
            c->misses = 0;
            c->total = 0;
        }
    """),
    target=text("""
        void reset(struct counter *c) {
            memset(c, 0, sizeof *c);
        }
    """),
    hint="ci{ on a block whose braces are on their own lines replaces the lines between them, and starts "
         "you on a fresh, indented line.",
    uses=["c"],
)
brace.add(
    title="Replace an initializer", par=13, ext="java", cursor=(1, 23),
    task="Java fills a new array with zeros anyway: replace {0, 0, 0, 0}, braces included, with new int[4]. "
         "The cursor is on the third 0.",
    start="int[] counts = {0, 0, 0, 0};",
    target="int[] counts = new int[4];",
    hint="a{ is the braces and everything inside them.",
    uses=["c"],
)
brace.add(
    title="Indent a pasted body", par=3, ext="java", cursor=(3, 1),
    task="The body of run() lost its indentation. Indent its three lines by one level. The cursor is on "
         "sync();.",
    start=text("""
        public void run() {
        connect();
        sync();
        disconnect();
        }
    """),
    target=text("""
        public void run() {
            connect();
            sync();
            disconnect();
        }
    """),
    hint="i{ on a block with its braces on their own lines is the whole lines between them. > shifts lines "
         "right.",
    uses=["indent"],
)
brace.add(
    title="Copy a body", par=5, ext="java", cursor=(3, 9),
    task="Give saveAs() the same three-line body as save(). The cursor is on write();.",
    start=text("""
        void save() {
            validate();
            write();
            notifyListeners();
        }
        void saveAs() {
        }
    """),
    target=text("""
        void save() {
            validate();
            write();
            notifyListeners();
        }
        void saveAs() {
            validate();
            write();
            notifyListeners();
        }
    """),
    hint="yi{ copies the lines between the braces. The last line of the file is saveAs()'s closing brace, "
         "and P puts lines above the cursor's line.",
    uses=["y", "gg", "p"],
)
brace.add(
    title="Reset the colors", par=15, ext="c",
    task="Reset all three colors to black: {0, 0, 0}.",
    start=text("""
        struct color bg = {30, 30, 46};
        struct color fg = {205, 214, 244};
        struct color accent = {137, 180, 250};
    """),
    target=text("""
        struct color bg = {0, 0, 0};
        struct color fg = {0, 0, 0};
        struct color accent = {0, 0, 0};
    """),
    hint="ci{ looks ahead for the next { when the cursor isn't inside one. After the first change, j and . "
         "repeat it.",
    uses=["c", "dot"],
)
brace.add(
    title="Pass the dict inline", par=6, ext="py",
    task="Pass the default style inline: put the whole dict, braces included, right after style=.",
    start=text("""
        DEFAULT_STYLE = {"color": "red", "bold": True}
        title = Label(root, text="Report", style=)
    """),
    target=text("""
        DEFAULT_STYLE = {"color": "red", "bold": True}
        title = Label(root, text="Report", style={"color": "red", "bold": True})
    """),
    hint="ya{ copies the braces and everything in them. Then put it before the last ) on line 2.",
    uses=["y", "line", "p"],
)
brace.add(
    title="Fix a messy body", par=3, ext="c", cursor=(4, 1),
    task="The indentation of clamp()'s body is a mess. Re-indent it. The cursor is on the line of the "
         "second if.",
    start=text("""
        int clamp(int x, int lo, int hi) {
              if (x < lo)
          return lo;
                if (x > hi)
                    return hi;
            return x;
        }
    """),
    target=text("""
        int clamp(int x, int lo, int hi) {
            if (x < lo)
                return lo;
            if (x > hi)
                return hi;
            return x;
        }
    """),
    hint="= (Project 03) re-indents lines by the language's rules. Give it the inside of the braces.",
    uses=["equal"],
)
brace.add(
    title="Move the setup code", par=6, ext="java", cursor=(7, 9),
    task="Move the three assignments from init() into the constructor Game(), leaving init() empty. The "
         "cursor is on lives = 3;.",
    start=text("""
        class Game {
            Game() {
            }

            void init() {
                score = 0;
                lives = 3;
                level = 1;
            }
        }
    """),
    target=text("""
        class Game {
            Game() {
                score = 0;
                lives = 3;
                level = 1;
            }

            void init() {
            }
        }
    """),
    hint="di{ deletes the body as whole lines, and P puts deleted lines back above the cursor. After di{ "
         "the cursor is on init()'s closing brace: count up to Game()'s.",
    uses=["d", "count", "p"],
)
brace.add(
    title="No options", par=3, ext="js",
    task="Start with no options: empty the object.",
    start="const opts = { verbose: true, retries: 3 };",
    target="const opts = {};",
    hint="di{ empties the braces, the spaces inside them too, and looks ahead for the first {.",
    uses=["d"],
)
brace.add(
    title="A LaTeX heading", par=18, ext="tex",
    task="Rename the section to Getting started.",
    start=text("""
        \\section{Intro}
        This chapter covers the basics.
    """),
    target=text("""
        \\section{Getting started}
        This chapter covers the basics.
    """),
    hint="LaTeX arguments are in curly braces, and i{ looks ahead for the first pair.",
    uses=["c"],
)
brace.add(
    title="A shell variable", par=10, ext="sh",
    task="Name the archive after the RELEASE variable instead of NAME.",
    start="tar -czf ${NAME}.tar.gz src/",
    target="tar -czf ${RELEASE}.tar.gz src/",
    hint="${NAME} has braces, and ci{ finds them by looking ahead.",
    uses=["c"],
)
brace.add(
    title="Copy the declarations", par=5, ext="css",
    task=".panel should look like .card: give it the same declarations.",
    start=text("""
        .card { padding: 1rem; border-radius: 8px; }
        .panel {}
    """),
    target=text("""
        .card { padding: 1rem; border-radius: 8px; }
        .panel { padding: 1rem; border-radius: 8px; }
    """),
    hint="yi{ copies what's between the braces, spaces included, and moves to its start. Look at what's right "
         "below.",
    uses=["y", "p"],
)
brace.add(
    title="Just the version", par=6, ext="toml",
    task='Drop the extra features: replace the inline table, braces included, with just the version string "1".',
    start='tokio = { version = "1", features = ["full"] }  # async runtime',
    target='tokio = "1"  # async runtime',
    hint="a{ is the braces and everything inside them.",
    uses=["c"],
)
brace.add(
    title="Swap the branches", par=10, ext="java", cursor=(6, 5),
    task="The branches are the wrong way round: a cache hit should count a hit and return the cached value. "
         "Swap the two bodies. The cursor is in the else branch.",
    start=text("""
        if (cache.has(key)) {
            misses++;
            return load(key);
        } else {
            hits++;
            log("hit");
            return cache.get(key);
        }
    """),
    target=text("""
        if (cache.has(key)) {
            hits++;
            log("hit");
            return cache.get(key);
        } else {
            misses++;
            return load(key);
        }
    """),
    hint="di{ deletes a body as whole lines, from any line of it, and p puts lines below the cursor. With no "
         "blank lines in the way, { jumps all the way to the first line.",
    uses=["d", "paragraph", "p", "count"],
)
brace.add(
    title="Same body for both callbacks", par=15, ext="js", cursor=(3, 5),
    task="Replace the body of both callbacks with a single track(); call. The cursor is on connect();.",
    start=text("""
        onOpen(() => {
            log("open");
            connect();
            render();
        });
        onClose(() => {
            log("close");
            disconnect();
            render();
        });
    """),
    target=text("""
        onOpen(() => {
            track();
        });
        onClose(() => {
            track();
        });
    """),
    hint="ci{ replaces a body of whole lines with one fresh, indented line, from any line inside it. . repeats "
         "it from anywhere in the next body.",
    uses=["c", "count", "dot"],
)
brace.add(
    title="A red copy of a button", par=12, ext="css", cursor=(3, 5),
    task=".btn-danger should look like .btn-primary, only red: copy the three declarations into it and change "
         "blue to red. The cursor is on the background line.",
    start=text("""
        .btn-primary {
            color: white;
            background: blue;
            border: none;
        }
        .btn-danger {
        }
    """),
    target=text("""
        .btn-primary {
            color: white;
            background: blue;
            border: none;
        }
        .btn-danger {
            color: white;
            background: red;
            border: none;
        }
    """),
    hint="yi{ copies the body as whole lines. The last line of the file is .btn-danger's closing brace, and P "
         "puts lines above the cursor.",
    uses=["y", "gg", "p", "bigword", "c"],
)
brace.add(
    title="Close an endpoint", par=14, ext="conf", cursor=(5, 9),
    task="Close the /api endpoint: replace everything in its location block with return 404;. The cursor is "
         "on the proxy_set_header line.",
    start=text("""
        server {
            listen 80;
            location /api {
                proxy_pass http://api:3000;
                proxy_set_header Host $host;
                proxy_read_timeout 30s;
            }
        }
    """),
    target=text("""
        server {
            listen 80;
            location /api {
                return 404;
            }
        }
    """),
    hint="The innermost braces around the cursor are the location block's. ci{ replaces the lines between "
         "them and keeps the indentation.",
    uses=["c"],
)
brace.add(
    title="Flatten the config", par=9, ext="js", cursor=(4, 9),
    task="Move host, port and tls up a level, straight into config, and remove the server wrapper. The cursor "
         "is on port.",
    start=text("""
        const config = {
            server: {
                host: "0.0.0.0",
                port: 8080,
                tls: false,
            },
        };
    """),
    target=text("""
        const config = {
            host: "0.0.0.0",
            port: 8080,
            tls: false,
        };
    """),
    hint="< shifts lines left, and i{ gives it the lines between server's braces. Then delete the two wrapper "
         "lines: . repeats a dd.",
    uses=["indent", "dd", "count", "dot"],
)

# ---------- i[ a[ ----------

bracket = drills.command(
    "bracket", "i[  a[", "inside or around square brackets",
    """i[ is everything inside the square brackets around the cursor, and a[ includes the brackets. i] and a]
    are the same objects. Like the other bracket objects they work from anywhere inside or on a bracket,
    skip nested pairs, and look ahead for the next [ (even on a later line) when the cursor isn't inside
    one. When [ ends its line and ] starts its own, i[ is the whole lines between them. Reach for them for
    array indexes, slices, Python lists and Markdown link text.""",
    examples=[("ci[", "change the index"), ("di[", "empty the list"), ("da[", "delete the index, brackets too"),
              ("ya[", "copy the index with its brackets"), ("yi[", "copy the list's items")],
)
bracket.add(
    title="Change an index", par=6, ext="java", cursor=(1, 28),
    task="Index data with pos instead. The cursor is on offset.",
    start="int value = data[index + offset];",
    target="int value = data[pos];",
    hint="ci[ changes everything inside the square brackets around the cursor.",
    uses=["c"],
)
bracket.add(
    title="Empty a list", par=3, ext="py",
    task="Empty the queue.",
    start="queue = [job1, job2, job3]",
    target="queue = []",
    hint="di[ looks ahead for the next [ when the cursor isn't inside a pair.",
    uses=["d"],
)
bracket.add(
    title="Flatten a lookup", par=3, ext="py", cursor=(1, 22),
    task='The config is flat now: remove ["network"] from the lookup. The cursor is on network.',
    start='timeout = config["network"]["timeout"]',
    target='timeout = config["timeout"]',
    hint="a[ is the square brackets and everything between them.",
    uses=["d"],
)
bracket.add(
    title="Index the other list", par=5, ext="py",
    task="Give ys the same index as xs: line 2 should read next_y = ys[i + 1].",
    start=text("""
        next_x = xs[i + 1]
        next_y = ys
    """),
    target=text("""
        next_x = xs[i + 1]
        next_y = ys[i + 1]
    """),
    hint="ya[ copies the index with its brackets and leaves the cursor on the [. Line 2 is shorter, so j "
         "stops on its last character.",
    uses=["y", "p"],
)
bracket.add(
    title="Brackets inside brackets", par=4, ext="py",
    task="Use the first color in the palette: change the index to 0.",
    start="color = palette[indices[k]]",
    target="color = palette[0]",
    hint="ci[ counts nested brackets, so it ends at the ] that matches, not at the first one.",
    uses=["c"],
)
bracket.add(
    title="Rename a link", par=13, ext="md",
    task="Change the link text from docs to user guide.",
    start="See the [docs](https://example.com/docs) for details.",
    target="See the [user guide](https://example.com/docs) for details.",
    hint="In Markdown, a link's text is in square brackets, and ci[ finds them by looking ahead.",
    uses=["c"],
)
bracket.add(
    title="Empty a multi-line list", par=3, ext="py", cursor=(3, 5),
    task='Disable every plugin: delete all three entries, keeping the brackets on their lines. The cursor '
         'is on "cache".',
    start=text("""
        PLUGINS = [
            "auth",
            "cache",
            "metrics",
        ]
    """),
    target=text("""
        PLUGINS = [
        ]
    """),
    hint="When [ ends its line and ] starts its own, i[ is the whole lines between them.",
    uses=["d"],
)
bracket.add(
    title="One constant for all sizes", par=11, ext="c", cursor=(2, 1),
    task="Use the LEN constant for all three array sizes. The cursor is at the start of line 2.",
    start=text("""
        struct user {
            char name[32];
            char mail[128];
            char city[16];
        };
    """),
    target=text("""
        struct user {
            char name[LEN];
            char mail[LEN];
            char city[LEN];
        };
    """),
    hint="Change the first size with ci[, then j and . for the others. The cursor counts as inside when "
         "it's on a bracket.",
    uses=["c", "dot"],
)
bracket.add(
    title="Inline the list", par=6, ext="py",
    task="Check against the same three formats: put them inside the empty brackets on line 2.",
    start=text("""
        allowed = ["png", "jpg", "gif"]
        ok = ext in []
    """),
    target=text("""
        allowed = ["png", "jpg", "gif"]
        ok = ext in ["png", "jpg", "gif"]
    """),
    hint="yi[ copies the items without the brackets. Then put them before the ] at the end of line 2.",
    uses=["y", "line", "p"],
)
bracket.add(
    title="Fix a Markdown link", par=35, ext="md",
    task='Change the link text to "the setup guide" and the link target to docs/setup.md.',
    start="See [this page](wiki/Setup) for details.",
    target="See [the setup guide](docs/setup.md) for details.",
    hint="The text is in square brackets and the target in parentheses. Both objects look ahead along the "
         "line.",
    uses=["c", "paren"],
)
bracket.add(
    title="The last twenty lines", par=7, ext="py",
    task="Keep the last 20 lines instead of the first 10: change the slice to -20:.",
    start="recent = lines[:10]",
    target="recent = lines[-20:]",
    hint="A slice is in square brackets, and ci[ looks ahead for them.",
    uses=["c"],
)
bracket.add(
    title="A test-only helper", par=12, ext="rs",
    task="The helper is only used by tests: change the attribute to #[cfg(test)].",
    start=text("""
        #[allow(dead_code)]
        fn make_fixture() -> User {
    """),
    target=text("""
        #[cfg(test)]
        fn make_fixture() -> User {
    """),
    hint="Rust attributes are in square brackets, and i[ looks ahead for the first [.",
    uses=["c"],
)
bracket.add(
    title="Select the columns", par=5, ext="py",
    task="Select those columns from the DataFrame: put the whole list, brackets included, inside df[].",
    start=text("""
        COLUMNS = ["id", "name", "email"]
        df = df[]
    """),
    target=text("""
        COLUMNS = ["id", "name", "email"]
        df = df[["id", "name", "email"]]
    """),
    hint="ya[ copies the list with its brackets, and leaves the cursor on the [. Line 2 is short.",
    uses=["y", "p"],
)
bracket.add(
    title="A safe lookup", par=12, ext="py",
    task="cache[key] raises KeyError when the key is missing. Use cache.get(key) instead.",
    start=text("""
        if cache[key]:
            hit()
    """),
    target=text("""
        if cache.get(key):
            hit()
    """),
    hint="a[ is the brackets and what's between them. Replace them with the method call.",
    uses=["c"],
)
bracket.add(
    title="Allow any host", par=7, ext="js", cursor=(3, 5),
    task='Allow every host: replace the three entries with a single "*", entry. The cursor is on "127.0.0.1".',
    start=text("""
        const hosts = [
            "localhost",
            "127.0.0.1",
            "staging.example.com",
        ];
    """),
    target=text("""
        const hosts = [
            "*",
        ];
    """),
    hint="When [ ends its line and ] starts its own, i[ is the whole lines between them, and changing them "
         "leaves one fresh, indented line.",
    uses=["c"],
)
bracket.add(
    title="The [] trap", par=9, ext="java",
    task="Allocate size elements: change n * 2 to size.",
    start="int[] buf = new int[n * 2];",
    target="int[] buf = new int[size];",
    hint="From the start of the line, the first [ is the empty pair in int[]. Get onto the brackets you mean "
         "first: on a bracket counts as inside.",
    uses=["line", "c"],
)
bracket.add(
    title="A version in the table", par=10, ext="md",
    task="Show the version instead of download in both links: v2.1.",
    start=text("""
        | Linux | [download](linux.tar.gz) |
        | macOS | [download](mac.dmg) |
    """),
    target=text("""
        | Linux | [v2.1](linux.tar.gz) |
        | macOS | [v2.1](mac.dmg) |
    """),
    hint="ci[ looks ahead to the link text. Then see where j lands.",
    uses=["c", "dot"],
)
bracket.add(
    title="Two levels at once", par=4, ext="py",
    task='The API returns the user at the top level now: remove ["response"]["payload"] from the lookup.',
    start='user = data["response"]["payload"]["user"]',
    target='user = data["user"]',
    hint="a[ is one pair of brackets with what's in them. After the delete, the cursor is on the next [, and "
         "on a bracket counts as inside.",
    uses=["d", "dot"],
)
bracket.add(
    title="Move the done items", par=10, ext="py",
    task="Both tasks are finished: move them from todo to the end of done.",
    start=text("""
        todo = ["write tests", "update docs"]
        done = ["fix bug"]
        save(todo, done)
    """),
    target=text("""
        todo = []
        done = ["fix bug", "write tests", "update docs"]
        save(todo, done)
    """),
    hint="di[ deletes the items into the register. On line 2, type the comma and space they need first, then "
         "put them after it.",
    uses=["d", "line", "insert", "p"],
)
bracket.add(
    title="The last item, twice", par=12, ext="js",
    task="Modern JavaScript has .at(-1) for the last item. Use it in both lines: items.at(-1) and parts.at(-1).",
    start=text("""
        const last = items[items.length - 1];
        const tail = parts[parts.length - 1];
    """),
    target=text("""
        const last = items.at(-1);
        const tail = parts.at(-1);
    """),
    hint="a[ is the brackets and the index between them. When the cursor isn't inside a pair, it looks ahead "
         "for the next [, even on a later line.",
    uses=["c", "dot"],
)

# ---------- ip ap ----------

ip = drills.command(
    "ip", "ip  ap", "a paragraph",
    """ip is the paragraph around the cursor: its lines between blank lines. ap adds the blank lines after it
    (for the last paragraph in the file, the ones before it). Both always work on whole lines, from any line
    of the paragraph, and a line of only spaces counts as blank. On a blank line, ip is the whole run of
    blank lines, and ap is that plus the next paragraph. In code a paragraph is often a whole function or
    block, so dap deletes one and yap copies one, blank line included.""",
    examples=[("dap", "delete the paragraph and the blank line after it"), ("cip", "rewrite the paragraph"),
              ("yap", "copy the paragraph"), (">ip", "indent the paragraph"), ("d2ap", "delete two paragraphs"),
              ("gUip", "uppercase the paragraph")],
)
ip.add(
    title="Delete a draft paragraph", par=3, ext="md", cursor=(4, 1),
    task="Delete the draft paragraph and the blank line after it. The cursor is in the middle of it.",
    start=text("""
        # Notes

        Draft: this section is out of date
        and will be rewritten after the
        next release.

        ## Install
    """),
    target=text("""
        # Notes

        ## Install
    """),
    hint="ap is a paragraph plus the blank lines after it, as whole lines.",
    uses=["d"],
)
ip.add(
    title="Rewrite a paragraph", par=20, ext="md", cursor=(4, 1),
    task="Replace the whole status paragraph with one line: Feature complete. The cursor is in the middle "
         "of it.",
    start=text("""
        ## Status

        The parser handles most of the
        grammar, but error messages are
        still rough and slow.

        ## Usage
    """),
    target=text("""
        ## Status

        Feature complete.

        ## Usage
    """),
    hint="cip deletes the paragraph's lines, without the blank lines around it, and leaves you on a fresh "
         "line to type.",
    uses=["c"],
)
ip.add(
    title="Duplicate a test", par=4, ext="py", cursor=(2, 5),
    task="Duplicate test_empty(), blank line included, so you can turn the copy into a new test. The "
         "cursor is on its assert line.",
    start=text("""
        def test_empty():
            assert parse("") == []

        def test_single():
            assert parse("a") == ["a"]
    """),
    target=text("""
        def test_empty():
            assert parse("") == []

        def test_empty():
            assert parse("") == []

        def test_single():
            assert parse("a") == ["a"]
    """),
    hint="yap copies the paragraph and the blank line after it, and moves the cursor to its first line. P "
         "puts lines above the cursor.",
    uses=["y", "p"],
)
ip.add(
    title="Make a code block", par=3, ext="md", cursor=(4, 1),
    task="Turn the three commands into a Markdown code block by indenting them four spaces. The cursor is "
         "on mypy src.",
    start=text("""
        Run the checks with:

        ruff check .
        mypy src
        pytest -q

        Then open the report.
    """),
    target=text("""
        Run the checks with:

            ruff check .
            mypy src
            pytest -q

        Then open the report.
    """),
    hint="> shifts lines right, and ip gives it every line of the paragraph.",
    uses=["indent"],
)
ip.add(
    title="Move an import group", par=5, ext="py", cursor=(2, 1),
    task="Standard-library imports go first: move the numpy and pandas group below the os and sys group. "
         "The cursor is on import pandas.",
    start=text("""
        import numpy as np
        import pandas as pd

        import os
        import sys

        def main():
            pass
    """),
    target=text("""
        import os
        import sys

        import numpy as np
        import pandas as pd

        def main():
            pass
    """),
    hint="dap deletes the group and the blank line after it. } jumps to the next blank line, and p puts "
         "lines below the cursor.",
    uses=["d", "paragraph", "p"],
)
ip.add(
    title="Delete two paragraphs", par=4, ext="py", cursor=(5, 1),
    task="Delete the debug flags and the fake users: both paragraphs, with the blank lines after them. The "
         "cursor is on VERBOSE = True.",
    start=text("""
        import json

        # TODO: remove before release
        DEBUG = True
        VERBOSE = True

        USERS = ["alice", "bob"]
        ADMINS = ["root"]

        def main():
            pass
    """),
    target=text("""
        import json

        def main():
            pass
    """),
    hint="A count in front of ap takes that many paragraphs.",
    uses=["d", "count"],
)
ip.add(
    title="Squeeze the blank lines", par=3, ext="py", cursor=(4, 1),
    task="A deleted function left five blank lines behind. Squeeze them down to one. The cursor is on the "
         "middle one.",
    start="import os\n\n\n\n\n\ndef main():\n    pass",
    target="import os\n\ndef main():\n    pass",
    hint="On a blank line, ip is the whole run of blank lines. Changing it leaves one empty line to type "
         "on, and you can just press <Esc>.",
    uses=["c"],
)
ip.add(
    title="Comment out a block", par=4, ext="py", cursor=(5, 1),
    task="Comment out the three debug lines at the bottom. The cursor is on dump(state).",
    start=text("""
        def main():
            run()

        print("debug: start")
        dump(state)
        print("debug: end")
    """),
    target=text("""
        def main():
            run()

        # print("debug: start")
        # dump(state)
        # print("debug: end")
    """),
    hint="gc (Project 03) comments lines out. Give it the paragraph.",
    uses=["comment"],
)
ip.add(
    title="The legal part in capitals", par=4, ext="txt", cursor=(5, 1),
    task="License disclaimers are traditionally in capitals. Uppercase the whole second paragraph. The "
         "cursor is in its middle.",
    start=text("""
        Permission is hereby granted, free of
        charge, to any person obtaining a copy.

        The software is provided "as is",
        without warranty of any kind, express
        or implied.
    """),
    target=text("""
        Permission is hereby granted, free of
        charge, to any person obtaining a copy.

        THE SOFTWARE IS PROVIDED "AS IS",
        WITHOUT WARRANTY OF ANY KIND, EXPRESS
        OR IMPLIED.
    """),
    hint="gU (Project 03) uppercases whatever you give it, and ip is the paragraph.",
    uses=["case"],
)
ip.add(
    title="Add a second server", par=17, ext="ini", cursor=(2, 1),
    task="Add a [server.beta] section after alpha, with the same settings except host = 10.0.0.2. The "
         "cursor is on alpha's host line.",
    start=text("""
        [server.alpha]
        host = 10.0.0.1
        port = 8080

        [logging]
        level = info
    """),
    target=text("""
        [server.alpha]
        host = 10.0.0.1
        port = 8080

        [server.beta]
        host = 10.0.0.2
        port = 8080

        [logging]
        level = info
    """),
    hint="Copy the section with yap, blank line included, and put it below the blank line after it. Then "
         "fix the last digit of the address, and change alpha to beta last, so the <Esc> is free.",
    uses=["y", "paragraph", "p", "line", "r", "word", "c"],
)
ip.add(
    title="Close the gap in a list", par=3, ext="md", cursor=(4, 1),
    task="The blank lines split the shopping list in two. Delete them all. The cursor is on the middle one.",
    start="- apples\n- pears\n\n\n\n- plums\n- figs",
    target="- apples\n- pears\n- plums\n- figs",
    hint="On a blank line, ip is the whole run of blank lines.",
    uses=["d"],
)
ip.add(
    title="Move the rocket", par=4, ext="txt", cursor=(3, 1),
    task="Move the rocket eight columns to the right. The cursor is in the middle of it.",
    start="\n".join(["    /\\", "   /  \\", "  |    |", "  |____|", "   /  \\"]),
    target="\n".join(["            /\\", "           /  \\", "          |    |", "          |____|",
                      "           /  \\"]),
    hint="> shifts lines by one shiftwidth, 4 columns, and ip gives it the whole drawing. . does it again.",
    uses=["indent", "dot"],
)
ip.add(
    title="Drop a service", par=3, ext="yaml", cursor=(6, 5),
    task="Remove the debug service, and the blank line after it. The cursor is on its image line.",
    start=text("""
        services:
          web:
            image: nginx

          debug:
            image: busybox
            command: sleep 3600

          db:
            image: postgres
    """),
    target=text("""
        services:
          web:
            image: nginx

          db:
            image: postgres
    """),
    hint="ap is a block of lines and the blank line after it, from any line of the block.",
    uses=["d"],
)
ip.add(
    title="One target for the build", par=11, ext="sh", cursor=(5, 1),
    task="The Makefile runs all three steps now: replace them with one line, make all. The cursor is on npm "
         "run lint.",
    start=text("""
        #!/bin/sh
        set -e

        npm ci
        npm run lint
        npm run build

        echo done
    """),
    target=text("""
        #!/bin/sh
        set -e

        make all

        echo done
    """),
    hint="cip replaces the paragraph's lines with one fresh line, and leaves the blank lines around it alone.",
    uses=["c"],
)
ip.add(
    title="Blank lines full of spaces", par=3, ext="py", cursor=(5, 5),
    task='Delete the two debug prints and the line after them. The "blank" lines here hold four spaces each. '
         "The cursor is on the second print.",
    start='def main():\n    config = load()\n    \n    print("debug:", config)\n    print("env:", os.environ)\n'
          '    \n    run(config)',
    target='def main():\n    config = load()\n\n    run(config)',
    hint="For the paragraph objects, a line of only spaces counts as blank, even though { and } walk right "
         "past it.",
    uses=["d"],
)
ip.add(
    title="Two TODO blocks", par=6, ext="py", cursor=(3, 1),
    task="Delete both TODO blocks, each with the blank line after it. The cursor is on VERBOSE = True.",
    start=text("""
        # TODO: remove before release
        DEBUG = True
        VERBOSE = True

        import json

        # TODO: remove before release
        USERS = ["alice", "bob"]

        def main():
            pass
    """),
    target=text("""
        import json

        def main():
            pass
    """),
    hint="dap works from any line of the block, and . repeats it from any line of the next one.",
    uses=["d", "count", "dot"],
)
ip.add(
    title="A third server", par=10, ext="toml", cursor=(6, 1),
    task="Add a third server at 10.0.0.3: copy the last [[servers]] block to the end of the file and change "
         "its address. The cursor is on the second block's host line.",
    start=text("""
        [[servers]]
        host = "10.0.0.1"
        port = 8080

        [[servers]]
        host = "10.0.0.2"
        port = 8080
    """),
    target=text("""
        [[servers]]
        host = "10.0.0.1"
        port = 8080

        [[servers]]
        host = "10.0.0.2"
        port = 8080

        [[servers]]
        host = "10.0.0.3"
        port = 8080
    """),
    hint="For the last paragraph in a file, ap takes the blank line before it instead of after. That's just "
         "what a copy at the end needs.",
    uses=["y", "gg", "p", "search", "r"],
)
ip.add(
    title="Move a function up", par=6, ext="py", cursor=(8, 5),
    task="Put parse() before save(), keeping one blank line between the functions. The cursor is in parse().",
    start=text("""
        def load(path):
            return open(path).read()

        def save(path, data):
            open(path, "w").write(data)

        def parse(text):
            return text.split()

        main()
    """),
    target=text("""
        def load(path):
            return open(path).read()

        def parse(text):
            return text.split()

        def save(path, data):
            open(path, "w").write(data)

        main()
    """),
    hint="dap deletes the function with the blank line after it. Then go up to save() and put it back above.",
    uses=["d", "count", "p"],
)
ip.add(
    title="Placeholders", par=11, ext="md", cursor=(4, 1),
    task="Both sections still hold the lorem ipsum placeholder. Replace each paragraph with the line TBD. "
         "The cursor is in the first one.",
    start=text("""
        ## Install

        Lorem ipsum dolor sit
        amet, consectetur
        adipiscing elit.

        ## Usage

        Lorem ipsum dolor sit
        amet, consectetur
        adipiscing elit.
    """),
    target=text("""
        ## Install

        TBD.

        ## Usage

        TBD.
    """),
    hint="cip replaces a paragraph with one line and keeps the blank lines. . repeats it from any line of the "
         "next paragraph.",
    uses=["c", "count", "dot"],
)
ip.add(
    title="Squeeze two gaps", par=6, ext="py", cursor=(3, 1),
    task="Too many blank lines: leave just one after import os, and one between a() and b(). The cursor is in "
         "the first gap.",
    start="import os\n\n\n\n\ndef a():\n    pass\n\n\n\ndef b():\n    pass",
    target="import os\n\ndef a():\n    pass\n\ndef b():\n    pass",
    hint="On a blank line, ip is the whole run of blank lines, and changing it leaves one empty line. } jumps "
         "to the next blank line.",
    uses=["c", "paragraph", "dot"],
)

# ---------- iW aW ----------

iw_big = drills.command(
    "iw-big", "iW  aW", "a WORD",
    """iW and aW are iw and aw for a WORD: everything between white space, punctuation included. So a URL, a
    path like ~/.config/nvim/init.lua, a flag like -Wextra or a chain like user.getName() is one WORD, where
    it would be many words. aW takes the white space after the WORD, or before it when there's none after,
    just like aw. As with every object, the cursor can be anywhere in the WORD.""",
    examples=[("ciW", "change the whole WORD"), ("daW", "delete a flag or a path and its space"),
              ("yiW", "copy a path or a URL"), ("yaW", "copy it with a space")],
    level="complex",
)
iw_big.add(
    title="Replace a URL", par=13, ext="sh", cursor=(1, 21),
    task='Use the variable instead of the hard-coded URL: replace the URL with "$API_URL", quotes included. '
         "The cursor is in the middle of the URL.",
    start="curl -s https://api.example.com/v1/users | jq .",
    target='curl -s "$API_URL" | jq .',
    hint="iW is a WORD: everything between spaces, so the whole URL, slashes and dots included. ciw would "
         "only change one piece of it.",
    uses=["c"],
)
iw_big.add(
    title="Drop two flags", par=6, ext="sh", cursor=(1, 10),
    task="Build without debug info and pedantic warnings: delete -g and -pedantic. The cursor is on the g "
         "of -g.",
    start="gcc -O2 -g -Wall -Wextra -pedantic -o app main.c",
    target="gcc -O2 -Wall -Wextra -o app main.c",
    hint="aW is a WORD and the space after it, so daW removes a flag, dash included. For the second one, "
         "land anywhere in it and repeat with .",
    uses=["d", "f", "dot"],
)
iw_big.add(
    title="Open the copy", par=5, ext="sh", cursor=(1, 33),
    task="Open the file you just copied: line 2 should be vim, a space, and the destination path. The "
         "cursor is in the destination path.",
    start=text("""
        cp config.example.yml ~/.config/app/config.yml
        vim
    """),
    target=text("""
        cp config.example.yml ~/.config/app/config.yml
        vim ~/.config/app/config.yml
    """),
    hint="The path is the last WORD on the line, so aW takes the space before it instead of after it. "
         "That's the space you need after vim.",
    uses=["y", "p"],
)
iw_big.add(
    title="A parameter and its comma", par=3, ext="py", cursor=(1, 22),
    task="The class doesn't use name anymore: delete the parameter, its comma and the space after it. The "
         "cursor is on the m of name.",
    start=text("""
        def __init__(self, name, age):
            self.age = age
    """),
    target=text("""
        def __init__(self, age):
            self.age = age
    """),
    hint="A WORD runs from white space to white space, so the comma is part of it, and aW adds the space "
         "after it.",
    uses=["d"],
)
iw_big.add(
    title="Options first", par=6, ext="sh", cursor=(1, 22),
    task="Put -avz first, right after rsync, where it's easier to see. The cursor is on the v of -avz.",
    start="rsync src/ backup/ -avz --delete",
    target="rsync -avz src/ backup/ --delete",
    hint="daW deletes the flag, dash included, with the space after it. Put it back in front of src/.",
    uses=["d", "line", "word", "p"],
)
iw_big.add(
    title="Drop the timestamp", par=4, ext="log", cursor=(1, 20),
    task="Strip the timestamp, brackets and time zone included, before you share the log line. The cursor is "
         "in the date.",
    start='127.0.0.1 - - [10/Oct/2024:13:55:36 +0000] "GET /health HTTP/1.1" 200 2',
    target='127.0.0.1 - - "GET /health HTTP/1.1" 200 2',
    hint="The timestamp is two WORDs, because of the space before the time zone. A count works with aW too.",
    uses=["d", "count"],
)

# ---------- is as ----------

sentence = drills.command(
    "sentence", "is  as", "a sentence",
    """is is the sentence under the cursor, and as adds the white space after it (or before it, for the last
    sentence of a paragraph). A sentence ends at a . ! or ? followed by a space, a tab or the end of the
    line, so it can span several lines. das deletes a sentence and keeps the spacing right, while dis leaves
    the spaces on both sides behind. Abbreviations fool it: the period in "e.g. " ends a sentence too.""",
    examples=[("das", "delete the sentence"), ("cis", "rewrite the sentence"), ("yas", "copy the sentence"),
              ("das0P", "move a sentence to the start of the line")],
    level="complex",
)
sentence.add(
    title="Drop a sentence", par=3, ext="md", cursor=(1, 37),
    task='Delete the middle sentence, the one that starts with "You may". The cursor is on need.',
    start="Run make to build the app. You may need to run it twice. Then start it with ./app.",
    target="Run make to build the app. Then start it with ./app.",
    hint="as is a sentence and the space after it.",
    uses=["d"],
)
sentence.add(
    title="Rewrite a sentence", par=15, ext="md", cursor=(1, 51),
    task="Replace the middle sentence with: It is small. The cursor is on weekend.",
    start="This tool is fast. Two students wrote it over a weekend. It is free.",
    target="This tool is fast. It is small. It is free.",
    hint="is is the sentence alone, period included but without the space after it, which is what you "
         "want before you type a new one.",
    uses=["c"],
)
sentence.add(
    title="Lead with the warning", par=5, ext="md", cursor=(1, 60),
    task='Move the sentence "Never run it on a Friday." to the start of the line. The cursor is on Friday.',
    start="Run ./deploy.sh from the project root. Never run it on a Friday. It takes about ten minutes.",
    target="Never run it on a Friday. Run ./deploy.sh from the project root. It takes about ten minutes.",
    hint="das deletes the sentence with the space after it, which is exactly what it needs in front of "
         "another sentence.",
    uses=["d", "line", "p"],
)
sentence.add(
    title="Fooled by e.g.", par=4, ext="md", cursor=(1, 25),
    task="Delete the middle sentence, the one that starts with Pick. The cursor is on fast.",
    start="Hashing matters. Pick a fast hash, e.g. xxHash. Avoid MD5 for passwords.",
    target="Hashing matters. Avoid MD5 for passwords.",
    hint="To Vim, the period in e.g. ends a sentence, so the one you want to delete counts as two.",
    uses=["d", "count"],
)
sentence.add(
    title="Repeat the warning", par=5, ext="md", cursor=(1, 14),
    task="The cleanup tool needs a backup too: copy the first sentence, with its space, to the start of line 3. "
         "The cursor is on data.",
    start=text("""
        Back up your data first. Then run the update.

        Run the cleanup tool.
    """),
    target=text("""
        Back up your data first. Then run the update.

        Back up your data first. Run the cleanup tool.
    """),
    hint="as is a sentence and the space after it, which is just what it needs in front of another sentence.",
    uses=["y", "gg", "p"],
)
sentence.add(
    title="Two notes out", par=7, ext="txt",
    task="The notes are moving to a box of their own. Delete both sentences that start with Note.",
    start=text("""
        Run the installer. Note that it needs root. Then reboot.
        Open the app. Note that it is slow at first. Log in.
    """),
    target=text("""
        Run the installer. Then reboot.
        Open the app. Log in.
    """),
    hint="das works from anywhere in the sentence. After the first one, look at where j lands.",
    uses=["f", "d", "dot"],
)

# ---------- it at ----------

tag = drills.command(
    "tag", "it  at", "inside or around an HTML/XML tag",
    """it is everything between an HTML or XML tag and its closing tag, and at is the whole element, tags
    included. Nested tags are part of the content, so cit on a paragraph also replaces a <b>...</b> inside
    it. With the cursor on a tag, you're inside that element, and in the indentation Vim starts from the
    first tag on the line. A count reaches out to an enclosing element: 2it. Unlike brackets, there's no
    look-ahead: outside every element, dit does nothing. And it's never line-wise: dit on an element spread
    over several lines leaves its two tags side by side.""",
    examples=[("cit", "change the text inside the tag"), ("dit", "empty the element"),
              ("dat", "delete the element"), ("yat", "copy the element"),
              ("c2it", "change the enclosing element's text")],
    level="complex",
)
tag.add(
    title="Use a version property", par=19, ext="xml", cursor=(4, 1),
    task="Replace the version 4.13.2 with ${junit.version}. The cursor is at the start of the version line.",
    start=text("""
        <dependency>
          <groupId>junit</groupId>
          <artifactId>junit</artifactId>
          <version>4.13.2</version>
        </dependency>
    """),
    target=text("""
        <dependency>
          <groupId>junit</groupId>
          <artifactId>junit</artifactId>
          <version>${junit.version}</version>
        </dependency>
    """),
    hint="it is everything between a tag and its closing tag. In the indentation, Vim uses the first tag "
         "on the line.",
    uses=["c"],
)
tag.add(
    title="Change a link's text", par=17, ext="html", cursor=(1, 31),
    task="Change the link's whole text, emphasis included, to Documentation. The cursor is on full.",
    start='<a href="/docs">Read the <em>full</em> docs</a>',
    target='<a href="/docs">Documentation</a>',
    hint="The cursor is inside <em>, which is inside <a>. A count reaches out to the enclosing element.",
    uses=["count", "c"],
)
tag.add(
    title="Remove an element", par=4, ext="html", cursor=(1, 28),
    task="The release is out: delete the <small>(draft)</small> element and the space before it. The "
         "cursor is on draft.",
    start="<h1>Release notes <small>(draft)</small></h1>",
    target="<h1>Release notes</h1>",
    hint="at is the whole element, tags included, but unlike aw it never takes white space. X deletes the "
         "character before the cursor.",
    uses=["d", "x"],
)
tag.add(
    title="Replace the whole element", par=10, ext="html", cursor=(1, 30),
    task="The status is plain text now: replace the whole <span> element, tags included, with shipped. The "
         "cursor is on done.",
    start='<p>Status: <span class="ok">done</span></p>',
    target="<p>Status: shipped</p>",
    hint="at is the element with its tags, and the cursor can be anywhere inside it.",
    uses=["c"],
)
tag.add(
    title="Empty the ad", par=3, ext="html",
    task='Empty the ad container, so that its tags end up side by side: <div class="ad"></div>.',
    start=text("""
        <div class="ad">
          <p>Buy now!</p>
        </div>
    """),
    target='<div class="ad"></div>',
    hint="With the cursor on a tag, you're inside that element. it is never line-wise, so deleting it joins "
         "the two tags.",
    uses=["d"],
)
tag.add(
    title="No data yet", par=11, ext="html", cursor=(2, 1),
    task="These cells have no data yet. Make all three say n/a. The cursor is at the start of the first td "
         "line.",
    start=text("""
        <tr>
          <td>TODO</td>
          <td>TBD</td>
          <td>??</td>
        </tr>
    """),
    target=text("""
        <tr>
          <td>n/a</td>
          <td>n/a</td>
          <td>n/a</td>
        </tr>
    """),
    hint="cit works from anywhere in the element or on its tags. After the change, j lands inside the next "
         "cell.",
    uses=["c", "dot"],
)

# ---------- i< a< ----------

angle = drills.command(
    "angle", "i<  a<", "inside or around angle brackets",
    """i< is everything inside the angle brackets around the cursor, and a< includes them. i> and a> are the
    same objects. They count nesting, so in List<Map<String, Integer>> from the first <, i< is
    Map<String, Integer>, and like the other bracket objects they look ahead when the cursor isn't inside a
    pair. Use them for Java generics, HTML tags and email addresses. They don't understand code, though: a
    less-than sign earlier on the line, as in if (n < max), confuses the look-ahead, so move inside the
    brackets first.""",
    examples=[("ci<", "change the type arguments"), ("di<", "empty them, for new HashMap<>()"),
              ("ya<", "copy them with the brackets"), ("ci>", "the same as ci<")],
    level="complex",
)
angle.add(
    title="Use the diamond", par=3, ext="java", cursor=(1, 53),
    task="Java can infer the type arguments after new: empty the second <String, Integer> so it reads "
         "HashMap<>(). The cursor is on the second Integer.",
    start="Map<String, Integer> counts = new HashMap<String, Integer>();",
    target="Map<String, Integer> counts = new HashMap<>();",
    hint="i< is everything inside the angle brackets around the cursor.",
    uses=["d"],
)
angle.add(
    title="Copy a generic type", par=5, ext="java", cursor=(2, 1),
    task="Give lookup() the full return type: copy <String, List<Integer>> to just after its Map. The "
         "cursor is at the start of line 2.",
    start=text("""
        class Index {
            Map<String, List<Integer>> byWord = new HashMap<>();
            Map lookup() { return byWord; }
        }
    """),
    target=text("""
        class Index {
            Map<String, List<Integer>> byWord = new HashMap<>();
            Map<String, List<Integer>> lookup() { return byWord; }
        }
    """),
    hint="ya< copies the angle brackets and everything in them, nested pairs included, looking ahead from "
         "the cursor. It leaves the cursor on the <, right above the space after Map on line 3.",
    uses=["y", "p"],
)
angle.add(
    title="Update an email address", par=23, ext="txt",
    task="Ada's address changed: make it lovelace@example.org.",
    start="Signed-off-by: Ada Lovelace <ada@old-mail.com>",
    target="Signed-off-by: Ada Lovelace <lovelace@example.org>",
    hint="Angle brackets have their own object, and like the other bracket objects it looks ahead when the "
         "cursor isn't inside a pair.",
    uses=["c"],
)
angle.add(
    title="A borrowed string type", par=7, ext="rs",
    task="The names are borrowed now: change the vector's element type to &str.",
    start="let names: Vec<String> = Vec::new();",
    target="let names: Vec<&str> = Vec::new();",
    hint="i< is everything between the angle brackets, found by looking ahead.",
    uses=["c"],
)
angle.add(
    title="The less-than trap", par=5, ext="java",
    task="Use the diamond: empty the type arguments of new HashMap<...>.",
    start="if (n < 10) cache = new HashMap<String, List<Integer>>();",
    target="if (n < 10) cache = new HashMap<>();",
    hint="The < in n < 10 comes first, and i< can't tell it from a bracket. Move inside the type arguments "
         "first.",
    uses=["f", "d"],
)
angle.add(
    title="Spell out the type", par=6, ext="ts",
    task="Give new Map() the same type arguments as the declaration, angle brackets included.",
    start="const cache: Map<string, User[]> = new Map();",
    target="const cache: Map<string, User[]> = new Map<string, User[]>();",
    hint="ya< copies the angle brackets and what's in them, and leaves the cursor on the <. The ( of Map() "
         "comes after it.",
    uses=["y", "f", "p"],
)

# ---------- 2i( 2i{ ----------

nested = drills.command(
    "nested", "2i(  2i{", "counts reach the enclosing pair",
    """A count on a bracket object reaches outward. i( is the inside of the innermost parentheses around the
    cursor, 2i( is the pair around that, 3i( the next one out, and the same goes for a( and for i{ a{ i[ i<.
    It saves you moving out of an inner call or block first: in max(abs(dx), abs(dy)) with the cursor on
    dx, c2i( changes everything inside max( ). If there aren't that many pairs around the cursor, the
    command fails and nothing changes.""",
    examples=[("c2i(", "change the outer call's arguments"), ("c2i{", "replace the enclosing block's body"),
              ("c3i(", "three pairs out"), ("v2a(", "select the outer pair")],
    level="complex",
)
nested.add(
    title="Reach the outer call", par=7, ext="java", cursor=(1, 35),
    task="Look up key directly: replace everything inside contains( ) with key. The cursor is on trim.",
    start="if (list.contains(normalize(name.trim()))) {",
    target="if (list.contains(key)) {",
    hint="i( would be the inside of normalize( ). A count reaches out: 2i( is the pair around that one.",
    uses=["c"],
)
nested.add(
    title="Replace the whole body", par=11, ext="java", cursor=(4, 9),
    task="Replace the whole body of tick() with // TODO. The cursor is inside the for loop.",
    start=text("""
        void tick() {
            for (Enemy e : enemies) {
                e.move();
                e.draw();
            }
            score++;
        }
    """),
    target=text("""
        void tick() {
            // TODO
        }
    """),
    hint="i{ would be the loop's body. 2i{ is the block around it: the whole method body.",
    uses=["c"],
)
nested.add(
    title="Three levels out", par=10, ext="py", cursor=(1, 29),
    task="unique already holds the sorted names: pass it to join() instead. The cursor is on names.",
    start='print(", ".join(sorted(set(names))))',
    target='print(", ".join(unique))',
    hint="names is three pairs of parentheses deep inside join( ): set, sorted, then join. Count outward.",
    uses=["c"],
)
nested.add(
    title="Reset the grid", par=4, ext="js", cursor=(1, 30),
    task="Clear the grid: empty the outer list. The cursor is on the last 1.",
    start='state["grid"] = [[1, 0], [0, 1]];',
    target='state["grid"] = [];',
    hint="i[ is the pair right around the cursor. A count reaches out to the pair around that one.",
    uses=["d"],
)
nested.add(
    title="Out of the inner type", par=7, ext="ts", cursor=(1, 38),
    task="load() resolves to a plain list now: make the return type Promise<T[]>. The cursor is on the g of "
         "string.",
    start="function load<T>(): Promise<Map<string, T>> {",
    target="function load<T>(): Promise<T[]> {",
    hint="i< is the inside of Map<...>, the innermost pair around the cursor. Count outward to Promise's.",
    uses=["c"],
)
nested.add(
    title="Two calls, one level out", par=12, ext="java", cursor=(1, 36),
    task="Both tests should parse the same input: replace everything inside parse( ) with input, in both "
         "lines. The cursor is on a.json.",
    start=text("""
        assertEquals(expected, parse(read("a.json")));
        assertEquals(expected, parse(read("b.json")));
    """),
    target=text("""
        assertEquals(expected, parse(input));
        assertEquals(expected, parse(input));
    """),
    hint="The innermost pair around the cursor is read( ). parse( ) is one out, and . repeats a counted "
         "change, count and all.",
    uses=["c", "dot"],
)
