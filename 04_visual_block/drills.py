"""Drills for Project 04: short problems that practice one command at a time.
Play them with:  python3 check.py drill      (the reference solutions are in ../solutions/drills/)"""
from trainer import Drills, text

drills = Drills(__file__)

# ---------- v ----------

visual = drills.command(
    "visual", "v", "select characters",
    """v starts selecting characters at the cursor. Every motion or text object now moves one end of the
    selection, and both ends are included: vt) stops just before the ), and v$ even takes the line break (so
    v$d joins two lines). Press an operator (d, c, y, >, gU, ...) and it acts on exactly what's highlighted.
    Visual mode also has keys of its own: r{c} replaces every selected character with {c}, U, u and ~ change
    the case, and p replaces the selection with what you yanked and puts the replaced text in the register (P
    does the same but keeps the register as it was). v again, or <Esc>, stops selecting.""",
    examples=[("viw", "select the word"), ('vi"r*', "mask a string with *"), ("veU", "uppercase to the end of the word"),
              ("viwp", "replace a word with the yanked text"), ("v%", "select to the matching bracket"),
              ("v$", "to the end of the line, line break included")],
)
visual.add(
    title="Mask the password", par=5, ext="py", cursor=(2, 1),
    task="Hide the password before you share this file: replace every character between the quotes on line 2 "
         "with a *. The cursor starts on line 2.",
    start=text("""
        DB_USER = "admin"
        DB_PASSWORD = "tr0ub4dor&3"
    """),
    target=text("""
        DB_USER = "admin"
        DB_PASSWORD = "***********"
    """),
    hint='vi" selects the text inside the quotes, and finds the string even when the cursor is in front of it. '
         "In Visual mode, r* replaces every selected character with a *.",
    uses=["quote", "r"],
)
visual.add(
    title="Shout the macro name", par=3, ext="c", cursor=(2, 9),
    task="Macro names are written in capitals. Uppercase max_clients. The cursor is on its first letter.",
    start=text("""
        #define BUFFER_SIZE 4096
        #define max_clients 64
    """),
    target=text("""
        #define BUFFER_SIZE 4096
        #define MAX_CLIENTS 64
    """),
    hint="v starts a selection, e stretches it to the end of the word, and U uppercases whatever is selected.",
    uses=["word", "case"],
)
visual.add(
    title="Stop shouting", par=6, ext="txt",
    task="Caps Lock was on for four words. Lowercase them so the line says \"back up the database\".",
    start="Always BACK UP THE DATABASE before an upgrade.",
    target="Always back up the database before an upgrade.",
    hint="Jump to the B with f. Then v and a counted e select through the end of the fourth word, and u "
         "lowercases everything selected.",
    uses=["f", "count", "word", "case"],
)
visual.add(
    title="Use the constant", par=7, ext="java", cursor=(1, 18),
    task="Replace the 3 in the loop condition with the constant MAX_RETRIES. The cursor is on MAX_RETRIES.",
    start=text("""
        static final int MAX_RETRIES = 3;
        for (int attempt = 0; attempt < 3; attempt++) {
            connect();
        }
    """),
    target=text("""
        static final int MAX_RETRIES = 3;
        for (int attempt = 0; attempt < MAX_RETRIES; attempt++) {
            connect();
        }
    """),
    hint="Yank the name first. Then go to the 3: v on its own selects one character, and p replaces the "
         "selection with what you yanked.",
    uses=["y", "word", "f"],
)
visual.add(
    title="Copy the arguments", par=8, ext="java",
    task="Fill the same rectangle that you draw: give fillRect the same arguments as drawRect.",
    start=text("""
        g.drawRect(x + 10, y + 10, width - 20, 40);
        g.fillRect(0, 0, 0, 0);
    """),
    target=text("""
        g.drawRect(x + 10, y + 10, width - 20, 40);
        g.fillRect(x + 10, y + 10, width - 20, 40);
    """),
    hint="yi( yanks the arguments of drawRect. On the next line, vi( selects the arguments of fillRect, and p "
         "replaces them.",
    uses=["paren", "y"],
)
visual.add(
    title="Finish the download", par=9, ext="txt",
    task="The download is done. Fill the bar with # and change 0% to 100%.",
    start="Loading [              ] 0%",
    target="Loading [##############] 100%",
    hint="vi[ selects the inside of the square brackets, and r# fills every selected character. Then Ctrl-a "
         "with a count adds that much to the next number on the line.",
    uses=["bracket", "r", "increment", "count"],
)
visual.add(
    title="Swap the arguments", par=9, ext="java", cursor=(3, 14),
    task="JUnit's assertEquals takes the expected value first. Swap the two arguments. The cursor is on actual.",
    start=text("""
        String expected = "8080";
        String actual = config.get("port");
        assertEquals(actual, expected);
    """),
    target=text("""
        String expected = "8080";
        String actual = config.get("port");
        assertEquals(expected, actual);
    """),
    hint="Delete actual with de. Then select expected with ve and press p: actual goes in, and the word it "
         "replaced goes into the register. Put that in the gap after the (.",
    uses=["d", "word", "f", "p"],
)
visual.add(
    title="Reuse the variable", par=7, ext="py",
    task="Don't compute it twice: replace the math.sqrt(...) call on line 2 with distance.",
    start=text("""
        distance = math.sqrt(dx * dx + dy * dy)
        if math.sqrt(dx * dx + dy * dy) > radius:
            bounce()
    """),
    target=text("""
        distance = math.sqrt(dx * dx + dy * dy)
        if distance > radius:
            bounce()
    """),
    hint="Yank distance. On line 2, with the cursor on the m of math, v% selects from there through the "
         "matching parenthesis (% looks ahead for the first bracket on the line). Then p.",
    uses=["y", "word", "percent"],
)
visual.add(
    title="Swap the dimensions", par=10, ext="c",
    task="The rows should come from the height and the columns from the width. Swap width and height.",
    start=text("""
        int rows = config.width;
        int cols = config.height;
    """),
    target=text("""
        int rows = config.height;
        int cols = config.width;
    """),
    hint="Delete width with de. On the line below, select height with ve and press p: width goes in, and "
         "height goes into the register. Go back up and put it.",
    uses=["count", "word", "d", "p"],
)
visual.add(
    title="Point the mirrors", par=13, ext="toml",
    task="The old mirrors are gone. Give both mirrors the primary URL.",
    start=text("""
        primary = "https://pkg.example.com/simple"
        mirror1 = "https://old.example.net/pypi"
        mirror2 = "https://old.example.org/pypi"
    """),
    target=text("""
        primary = "https://pkg.example.com/simple"
        mirror1 = "https://pkg.example.com/simple"
        mirror2 = "https://pkg.example.com/simple"
    """),
    hint='Yank the URL with yi". On each mirror, vi" selects the old URL. P replaces it and, unlike p, keeps the '
         "register as it is, so you can put the same text twice.",
    uses=["quote", "y"],
)
visual.add(
    title="Mask the token", par=6, ext="env",
    task="Hide the token before you paste this into a ticket: replace every character after the = with a *.",
    start="API_TOKEN=ghp_8f3k2LmQ9xT7wR",
    target="API_TOKEN=******************",
    hint="Go to the end of the line, then v and T= stretch the selection back to just after the =. r* "
         "replaces every selected character, however many there are.",
    uses=["line", "t", "r"],
)
visual.add(
    title="Point the replica at the primary", par=6, ext="txt",
    task="The replica moved onto the primary's machine. Give line 2 the same address as line 1.",
    start=text("""
        10.0.0.5     db-primary
        10.0.12.177  db-replica
    """),
    target=text("""
        10.0.0.5     db-primary
        10.0.0.5  db-replica
    """),
    hint="An address is one WORD, so yE yanks it. On line 2, vE selects the old address, and p replaces it.",
    uses=["y", "bigword"],
)
visual.add(
    title="Same hosts for the tests", par=8, ext="js",
    task="The tests should use the dev hosts: replace what's inside testHosts' brackets with what's inside "
         "devHosts'.",
    start=text("""
        const devHosts = ["localhost", "127.0.0.1"];
        const testHosts = ["ci.internal"];
    """),
    target=text("""
        const devHosts = ["localhost", "127.0.0.1"];
        const testHosts = ["localhost", "127.0.0.1"];
    """),
    hint="yi[ yanks the inside of the brackets, and finds them further along the line. On line 2, vi[ "
         "selects the inside of the other brackets, and p replaces it.",
    uses=["bracket", "y"],
)
visual.add(
    title="Redact the key", par=5, ext="html", cursor=(1, 26),
    task="Replace every character of the key inside the <code> tag with a *, keeping the tags. The cursor is "
         "on the 3 in the key.",
    start="<p>Your key is <code>sk-12345abcde</code>.</p>",
    target="<p>Your key is <code>*************</code>.</p>",
    hint="it is the inside of the tag around the cursor, and vit selects it. Then r* fills it.",
    uses=["tag", "r"],
)
visual.add(
    title="Pass the whole config", par=7, ext="py",
    task="Replace the two lines of keyword arguments to start() with the variable config, so the call reads "
         "start(config).",
    start=text("""
        config = load()
        start(debug=True,
              port=8080)
    """),
    target=text("""
        config = load()
        start(config)
    """),
    hint="Yank config with ye. On line 2, vi( selects everything inside the parentheses, across both lines, "
         "and p replaces all of it with the one word.",
    uses=["y", "word", "paren"],
)
visual.add(
    title="The table's separator row", par=12, ext="md",
    task="Add the separator row under the header: a copy of the header line with every character between "
         "the | turned into a -, so it reads |------|------|.",
    start=text("""
        | Name | Role |
        | Ana  | dev  |
    """),
    target=text("""
        | Name | Role |
        |------|------|
        | Ana  | dev  |
    """),
    hint="yyp makes the copy. vt| from the first space selects up to the next |, and r- fills it. Both cells "
         "are 6 wide, so 7l lands at the start of the second, and . repeats a Visual change on the same "
         "number of characters at the cursor.",
    uses=["y", "p", "t", "r", "dot"],
)
visual.add(
    title="Classified", par=8, ext="txt",
    task="Black out everything inside the quotes, which run over two lines: every character between them "
         "becomes a #. The line break stays.",
    start=text("""
        She said "the launch code is
        0000, tell nobody" and left.
    """),
    target=text("""
        She said "##################
        #################" and left.
    """),
    hint="i\" only works within one line, so build the selection yourself: start just inside the first quote "
         "(the quote is a word of its own, so a counted w gets there), go down a line, and stop just before "
         "the closing quote with t. r# replaces every character but the line break.",
    uses=["word", "count", "t", "r"],
)
visual.add(
    title="Roll back the release", par=8, ext="sh",
    task="Point CURRENT at the same release as BASE: replace its date with 2026-11-05, BASE's date.",
    start=text("""
        BASE=/opt/app/releases/2026-11-05
        CURRENT=/opt/app/releases/2026-10-01
    """),
    target=text("""
        BASE=/opt/app/releases/2026-11-05
        CURRENT=/opt/app/releases/2026-11-05
    """),
    hint="f2 finds the date (there's no 2 before it), and y$ yanks it to the end of the line. Both dates "
         "start with the word 2026, so * takes you to the other one. Select it with vE, and p.",
    uses=["f", "y", "line", "star", "bigword"],
)
visual.add(
    title="Two passwords, one length", par=7, ext="ini",
    task="Replace every character inside the quotes with a *, on both lines.",
    start=text("""
        db_pass  = "hunter22"
        api_pass = "letmein!"
    """),
    target=text("""
        db_pass  = "********"
        api_pass = "********"
    """),
    hint="vi\" and r* mask the first one. Both passwords are 8 characters and start in the same column, and . "
         "repeats a Visual change on the same number of characters at the cursor.",
    uses=["quote", "r", "dot"],
)
visual.add(
    title="Fill in the template", par=8, ext="txt",
    task="Replace the blank ____ on line 2 with the name on line 1.",
    start=text("""
        Name: Ada Lovelace
        Hello, ____! Welcome aboard.
    """),
    target=text("""
        Name: Ada Lovelace
        Hello, Ada Lovelace! Welcome aboard.
    """),
    hint="W gets to the name, and y$ yanks the rest of the line. On line 2, select the blank with v and e "
         "(underscores are word characters) and p.",
    uses=["bigword", "y", "line", "word"],
)

# ---------- V ----------

visual_line = drills.command(
    "visual-line", "V", "select whole lines",
    """V selects whole lines: the cursor's line, and every line a motion (j, k, G, }, /pattern, ...) moves over.
    An operator then works on all of them: d, y, c, > and <, =, gc, J. The Visual-only keys work too: U, u
    and ~ change the case of the lines, r{c} turns every character on them into {c}, Ctrl-a adds to the first
    number on each line, and p replaces the lines with what you yanked (P does too, but keeps the register as
    it was). Press V again, or <Esc>, to stop selecting.""",
    examples=[("VU", "uppercase the line"), ("Vjd", "delete this line and the next"),
              ("yypVr=", "underline a heading"), ("Vp", "replace the line with the yanked one"),
              ("VG10 Ctrl-a", "add 10 to a number on every line"), ("V/end<CR>", "down to the line with end")],
)
visual_line.add(
    title="Shout the warning", par=2, ext="txt", cursor=(2, 1),
    task="Make line 2 stand out: uppercase all of it. The cursor is on line 2.",
    start=text("""
        Release checklist
        warning: run the migrations first!
        1. Tag the commit
    """),
    target=text("""
        Release checklist
        WARNING: RUN THE MIGRATIONS FIRST!
        1. Tag the commit
    """),
    hint="V selects the whole line, and U uppercases the selection.",
    uses=["case"],
)
visual_line.add(
    title="Redact the key", par=5, ext="pem",
    task="Before you paste this into a bug report, replace every character of the two key lines (2 and 3) "
         "with an X.",
    start=text("""
        -----BEGIN PRIVATE KEY-----
        MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcw
        ggSjAgEAAoIBAQC7VJTUt9Us8cKjMzEfYyjiWA4R
        -----END PRIVATE KEY-----
    """),
    target=text("""
        -----BEGIN PRIVATE KEY-----
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        -----END PRIVATE KEY-----
    """),
    hint="V and j select the two lines. r in Visual mode replaces every selected character, however long each "
         "line is.",
    uses=["r"],
)
visual_line.add(
    title="Underline the heading", par=6, ext="md",
    task="Make the first line a Markdown heading the old-fashioned way: underline it with = signs, one under "
         "each character.",
    start=text("""
        Release notes
        Fixed the crash on startup.
    """),
    target=text("""
        Release notes
        =============
        Fixed the crash on startup.
    """),
    hint="Copy the line with yyp. Then V selects the copy, and r= replaces every character on it.",
    uses=["y", "p", "r"],
)
visual_line.add(
    title="Same URL as production", par=7, ext="env",
    task="Staging should use the production database for now. Replace line 4 with a copy of line 2.",
    start=text("""
        # production
        DATABASE_URL=postgres://db.prod.internal:5432/shop
        # staging
        DATABASE_URL=postgres://localhost/shop_old
    """),
    target=text("""
        # production
        DATABASE_URL=postgres://db.prod.internal:5432/shop
        # staging
        DATABASE_URL=postgres://db.prod.internal:5432/shop
    """),
    hint="Yank line 2 with yy. On line 4, V selects the line and p replaces it with the yanked one.",
    uses=["y"],
)
visual_line.add(
    title="Bump the test ports", par=5, ext="txt", cursor=(2, 1),
    task="The test servers clash with the dev servers. Add 10 to every port. The cursor is on line 2.",
    start=text("""
        # test servers
        web   8080
        api   8081
        admin 8082
        docs  8083
    """),
    target=text("""
        # test servers
        web   8090
        api   8091
        admin 8092
        docs  8093
    """),
    hint="Select the four lines with V and G. In Visual mode, Ctrl-a adds to the first number on every "
         "selected line, and a count says how much.",
    uses=["increment", "count", "gg"],
)
visual_line.add(
    title="Copy the settings over", par=7, ext="ini",
    task="The tests should use the dev database. Replace the test host and port with the dev ones.",
    start=text("""
        [dev]
        host = localhost
        port = 5432

        [test]
        host = 10.0.0.7
        port = 6543
    """),
    target=text("""
        [dev]
        host = localhost
        port = 5432

        [test]
        host = localhost
        port = 5432
    """),
    hint="Yank the two dev lines with yj. G goes to the last line, Vk selects it and the line above, and p "
         "replaces both.",
    uses=["y", "gg"],
)
visual_line.add(
    title="Reverse the statements", par=7, ext="py",
    task="These three statements are upside down. Put them in order: price first, then total, then print.",
    start=text("""
        print(total)
        total = price * qty
        price = float(input())
    """),
    target=text("""
        price = float(input())
        total = price * qty
        print(total)
    """),
    hint="Delete the first line. On the last line, Vp puts it there, and the line it replaced goes into the "
         "register. Put that at the top.",
    uses=["dd", "p"],
)
visual_line.add(
    title="Fix the loggers", par=11, ext="py",
    task="save() and delete() set up log wrongly. Replace their log = lines with the one from load().",
    start=text("""
        def load(path):
            log = logging.getLogger(__name__)
            log.info("loading %s", path)

        def save(path):
            log = print
            log.info("saving %s", path)

        def delete(path):
            log = None
            log.info("deleting %s", path)
    """),
    target=text("""
        def load(path):
            log = logging.getLogger(__name__)
            log.info("loading %s", path)

        def save(path):
            log = logging.getLogger(__name__)
            log.info("saving %s", path)

        def delete(path):
            log = logging.getLogger(__name__)
            log.info("deleting %s", path)
    """),
    hint="Yank line 2. On each wrong line, VP replaces it. P in Visual mode keeps the register, so the second "
         "put still has the right line.",
    uses=["y", "count"],
)
visual_line.add(
    title="Caps Lock, twice", par=5, ext="txt", cursor=(2, 1),
    task="Lines 2 and 4 were typed with Caps Lock on. Flip the case of both. The cursor is on line 2.",
    start=text("""
        Changelog
        tHIS RELEASE FIXES THE CRASH.
        Thanks to everyone who tested it.
        iT ALSO ADDS DARK MODE.
    """),
    target=text("""
        Changelog
        This release fixes the crash.
        Thanks to everyone who tested it.
        It also adds dark mode.
    """),
    hint="V~ flips the case of the whole line. . repeats a Visual command on the same number of lines, at the "
         "cursor.",
    uses=["case", "dot"],
)
visual_line.add(
    title="Comment banner", par=10, ext="py", cursor=(3, 1),
    task="Make the comment on line 3 a banner: a row of # above it and below it, each as long as the comment. "
         "The cursor is on line 3.",
    start=text("""
        import os

        # Data loading
        def load():
            return os.listdir(".")
    """),
    target=text("""
        import os

        ##############
        # Data loading
        ##############
        def load():
            return os.listdir(".")
    """),
    hint="yyP copies the line above itself, and Vr# turns the copy into a row of #. Then yank that row and put "
         "it below the comment.",
    uses=["y", "p", "r"],
)
visual_line.add(
    title="Fix the stack trace", par=4, ext="log", cursor=(2, 1),
    task="Two lines were added at the top of app.js, so every line number in this trace is now 2 higher. "
         "Add 2 to each one. The cursor is on line 2.",
    start=text("""
        TypeError: cannot read properties of undefined
            at render (app.js:42)
            at update (app.js:17)
            at main (app.js:9)
    """),
    target=text("""
        TypeError: cannot read properties of undefined
            at render (app.js:44)
            at update (app.js:19)
            at main (app.js:11)
    """),
    hint="Select from here to the last line with V and G. Ctrl-a with a count adds to the first number on "
         "every selected line, wherever it is.",
    uses=["increment", "count", "gg"],
)
visual_line.add(
    title="Double borders", par=5, ext="txt",
    task="Make the top and bottom borders of the box double lines: every character on lines 1 and 3 "
         "becomes a =.",
    start=text("""
        +------------+
        | build: ok  |
        +------------+
    """),
    target=text("""
        ==============
        | build: ok  |
        ==============
    """),
    hint="Vr= turns every character on the line into a =, without counting. G goes to the last line, and . "
         "repeats a Visual command on the same number of lines at the cursor.",
    uses=["r", "gg", "dot"],
)
visual_line.add(
    title="Three levels back", par=3, ext="py", cursor=(4, 1),
    task="The return line is indented 16 spaces, but it belongs to the function: 4 spaces. Fix it. The "
         "cursor is on it.",
    start=text("""
        def report(rows):
            for row in rows:
                print(row)
                        return len(rows)
    """),
    target=text("""
        def report(rows):
            for row in rows:
                print(row)
            return len(rows)
    """),
    hint="In Visual mode, a count before < shifts the lines that many levels. (In Normal mode, 3<< would "
         "shift three lines by one level. And == leaves a Python line like this one alone.)",
    uses=["indent", "count"],
)
visual_line.add(
    title="Fill in the empty function", par=5, ext="py", cursor=(3, 1),
    task="close() only has a TODO. Replace that line with a copy of line 3, so it does nothing for now, "
         "like open(). The cursor is on line 3.",
    start=text("""
        class Port:
            def open(self):
                pass
            def close(self):
                # TODO
    """),
    target=text("""
        class Port:
            def open(self):
                pass
            def close(self):
                pass
    """),
    hint="Yank line 3, go down to the TODO (it's the last line), and replace it with V and p.",
    uses=["y", "gg"],
)
visual_line.add(
    title="Lowercase SQL", par=2, ext="sql",
    task="This team writes its SQL in lowercase. Lowercase the whole statement.",
    start="SELECT NAME, EMAIL FROM USERS WHERE ID = 7;",
    target="select name, email from users where id = 7;",
    hint="V selects the line and u lowercases the selection. (u is undo only in Normal mode.)",
    uses=["case"],
)
visual_line.add(
    title="Release headings", par=4, ext="md",
    task="Uppercase both release headings (lines 1 and 4), so they stand out in the plain-text changelog.",
    start=text("""
        version 2.1 (stable)
        - Faster startup.
        - Fewer crashes.
        version 2.0 (beta)
        - New drills.
    """),
    target=text("""
        VERSION 2.1 (STABLE)
        - Faster startup.
        - Fewer crashes.
        VERSION 2.0 (BETA)
        - New drills.
    """),
    hint="VU uppercases a whole line, a key shorter than gUU. * finds the next use of the word under the "
         "cursor, which is on the other heading, and . repeats VU on one line there.",
    uses=["case", "star", "dot"],
)
visual_line.add(
    title="Build, test, deploy", par=9, ext="yaml", cursor=(2, 1),
    task="The pipeline runs its steps in the wrong order. Swap the first step (deploy, lines 2 and 3) with "
         "the last one (build, lines 6 and 7). The cursor is on line 2.",
    start=text("""
        steps:
          - name: deploy
            run: ./deploy.sh
          - name: test
            run: make test
          - name: build
            run: make
    """),
    target=text("""
        steps:
          - name: build
            run: make
          - name: test
            run: make test
          - name: deploy
            run: ./deploy.sh
    """),
    hint="dj cuts the deploy step. The build step is now the last two lines: select them with V, and press p. "
         "Deploy goes in, and the build lines go into the register. Then put them below line 1.",
    uses=["d", "count", "p", "gg"],
)
visual_line.add(
    title="Staging, ten ports up", par=11, ext="ini",
    task="Give [staging] a copy of the three dev settings, with every port 10 higher.",
    start=text("""
        [dev]
        web = 8080
        api = 8081
        db  = 5432

        [staging]
    """),
    target=text("""
        [dev]
        web = 8080
        api = 8081
        db  = 5432

        [staging]
        web = 8090
        api = 8091
        db  = 5442
    """),
    hint="Yank the three settings, go to the last line and put them below it. The cursor is then on the "
         "first copy: V and G select the copies, and 10 Ctrl-a adds 10 to the number on each.",
    uses=["y", "count", "gg", "p", "increment"],
)
visual_line.add(
    title="Sign the email", par=6, ext="txt",
    task="Replace the SIGNATURE placeholder on the last line with the three signature lines at the top.",
    start=text("""
        Best,
        Rick Xie
        Platform team

        Hi Ana, the demo moved to Friday.
        SIGNATURE
    """),
    target=text("""
        Best,
        Rick Xie
        Platform team

        Hi Ana, the demo moved to Friday.
        Best,
        Rick Xie
        Platform team
    """),
    hint="Yank the three lines with y and a counted j. On the placeholder, V selects it and p replaces it with "
         "all three.",
    uses=["y", "count", "gg"],
)
visual_line.add(
    title="Lift the overlays", par=9, ext="css",
    task="Add 100 to the z-index of .modal, .overlay, .toast and .tooltip. Leave .nav and .footer alone.",
    start=text("""
        .modal   { z-index: 10; }
        .overlay { z-index: 9; }
        .nav     { z-index: 5; }
        .footer  { z-index: 1; }
        .toast   { z-index: 20; }
        .tooltip { z-index: 19; }
    """),
    target=text("""
        .modal   { z-index: 110; }
        .overlay { z-index: 109; }
        .nav     { z-index: 5; }
        .footer  { z-index: 1; }
        .toast   { z-index: 120; }
        .tooltip { z-index: 119; }
    """),
    hint="Vj and 100 Ctrl-a do the first two. Go down to .toast, and . repeats the Visual Ctrl-a, count and "
         "all, on two lines there.",
    uses=["count", "increment", "dot"],
)

# ---------- Ctrl-v I A $A ----------

block_insert = drills.command(
    "block-insert", "Ctrl-v  I  A  $A", "type on many lines at once",
    """Ctrl-v selects a rectangle (a block): from the column where you started to the cursor's column, on every
    line in between. I types in front of it and A after it, on every line. What you type shows on the first
    line only, and Vim copies it to the others when you press <Esc>. I skips lines too short to reach the
    block's left edge (a block in column 1 reaches every line, even blank ones), while A pads short lines with
    spaces. Press $ to make the right edge ragged, so that $A appends at each line's own end.""",
    examples=[("Ctrl-v 3j I- <Esc>", "bullets on four lines"), ("Ctrl-v 3j $A;<Esc>", "a ; at the end of four lines"),
              ("Ctrl-v G I> <Esc>", "quote every line"), ("Ctrl-v 2j A|<Esc>", "a | after the block, padding short lines"),
              (".", "the same block insert again, at the cursor")],
)
block_insert.add(
    title="Make it a checklist", par=11, ext="md", cursor=(3, 1),
    task="Turn the four steps into a Markdown task list: put \"- [ ] \" in front of each one. The cursor is on "
         "the first step.",
    start=text("""
        ## Before release

        run the tests
        bump the version
        update the changelog
        tag the commit

        Ship it on Friday.
    """),
    target=text("""
        ## Before release

        - [ ] run the tests
        - [ ] bump the version
        - [ ] update the changelog
        - [ ] tag the commit

        Ship it on Friday.
    """),
    hint="Ctrl-v and 3j select a block one column wide on the four lines. I types in front of the block, and "
         "what you type appears on the other lines when you press <Esc>.",
)
block_insert.add(
    title="Star the comment", par=8, ext="c", cursor=(2, 1),
    task="Give the four text lines of this comment the usual \" * \" in front (space, star, space). The cursor "
         "is on line 2.",
    start=text("""
        /*
        Parses the config file at path.
        Returns 0 on success, or -1 if
        the file is missing or unreadable.
        Never frees path.
         */
        int parse_config(const char *path);
    """),
    target=text("""
        /*
         * Parses the config file at path.
         * Returns 0 on success, or -1 if
         * the file is missing or unreadable.
         * Never frees path.
         */
        int parse_config(const char *path);
    """),
    hint="Select the first column of the four lines with Ctrl-v, and I types the text in front of all of them.",
)
block_insert.add(
    title="Continue the command", par=8, ext="sh",
    task="Every line of this command except the last needs a space and a backslash at its end, so that the "
         "shell reads it all as one command.",
    start=text("""
        docker run
          --rm
          -p 8080:80
          -v "$PWD":/usr/share/nginx/html
          nginx:alpine
    """),
    target=text("""
        docker run \\
          --rm \\
          -p 8080:80 \\
          -v "$PWD":/usr/share/nginx/html \\
          nginx:alpine
    """),
    hint="In block mode, $ stretches the block to the end of every line, however long it is. Then A appends "
         "after each line's end.",
)
block_insert.add(
    title="Quote the whole email", par=6, ext="txt",
    task="Quote Ana's email in your reply: put \"> \" at the start of every line, the blank ones too.",
    start=text("""
        Hi Rick,

        The demo moved to Friday.
        Can you send the slides?

        Thanks,
        Ana
    """),
    target=text("""
        > Hi Rick,
        >
        > The demo moved to Friday.
        > Can you send the slides?
        >
        > Thanks,
        > Ana
    """),
    hint="A block in the first column reaches every line, even empty ones. G goes to the last line and keeps "
         "the column.",
    uses=["gg"],
)
block_insert.add(
    title="Prefix with self.", par=10, ext="py", cursor=(2, 5),
    task="These should be attributes: put self. in front of width, height and area. The cursor is on width.",
    start=text("""
        def __init__(self, w, h):
            width = w
            height = h

            area = w * h
    """),
    target=text("""
        def __init__(self, w, h):
            self.width = w
            self.height = h

            self.area = w * h
    """),
    hint="Make a one-column block from width down to area. I skips lines that are too short to reach the "
         "block, so the blank line stays blank.",
)
block_insert.add(
    title="Make the fields final", par=11, ext="java", cursor=(2, 13),
    task="Make the three fields final: put final (and a space) between private and the type. The cursor is on "
         "String.",
    start=text("""
        class Config {
            private String host;
            private int    port;
            private long   timeoutMillis;
        }
    """),
    target=text("""
        class Config {
            private final String host;
            private final int    port;
            private final long   timeoutMillis;
        }
    """),
    hint="The types start in the same column on every line. A block there, and I puts final in front of all "
         "three.",
)
block_insert.add(
    title="Add the seconds", par=9, ext="log",
    task="Add :00 seconds to every time, so that 09:15 becomes 09:15:00.",
    start=text("""
        09:15 boot
        09:20 login as rick
        11:05 logout
    """),
    target=text("""
        09:15:00 boot
        09:20:00 login as rick
        11:05:00 logout
    """),
    hint="Select the times as a block. E jumps to the end of a WORD, so it treats 11:05 as one. A appends after "
         "the block's right edge on every line.",
    uses=["bigword"],
)
block_insert.add(
    title="Hex prefixes", par=12, ext="c", cursor=(2, 5),
    task="Write the bytes as C hex literals: put 0x in front of each one. The cursor is on the first byte.",
    start=text("""
        uint8_t key[] = {
            ff, 00, a5, 3c,
            10, 7f, 80, e1,
        };
    """),
    target=text("""
        uint8_t key[] = {
            0xff, 0x00, 0xa5, 0x3c,
            0x10, 0x7f, 0x80, 0xe1,
        };
    """),
    hint="Block-insert 0x on both lines once. Then . repeats a block insert at the cursor, on the same number "
         "of lines: W to the next byte, then .",
    uses=["bigword", "dot"],
)
block_insert.add(
    title="Namespace the functions", par=9, ext="c", cursor=(1, 6),
    task="Avoid clashing with the C library: rename the three functions to vfs_open, vfs_read and vfs_close. "
         "The cursor is on open.",
    start=text("""
        int  open(const char *path);
        int  read(int fd, char *buf, int n);
        void close(int fd);
    """),
    target=text("""
        int  vfs_open(const char *path);
        int  vfs_read(int fd, char *buf, int n);
        void vfs_close(int fd);
    """),
    hint="The names start in the same column, so a block there and I can prefix all three.",
)
block_insert.add(
    title="Pipe the table", par=17, ext="md",
    task="Make this a Markdown table: \"| \" at the start of every line and in front of the second column, and "
         "\" |\" at the end of every line.",
    start=text("""
        Keys   Action
        ----   ------
        dd     delete a line
        yy     yank a line
        p      put after
    """),
    target=text("""
        | Keys   | Action |
        | ----   | ------ |
        | dd     | delete a line |
        | yy     | yank a line |
        | p      | put after |
    """),
    hint="Block-insert \"| \" in the first column. 2W gets to the second column, and . repeats the block "
         "insert there. gv selects the first block again, and $A adds the ends.",
    uses=["bigword", "count", "dot", "visual-ends"],
)
block_insert.add(
    title="Make them local", par=11, ext="lua",
    task="These globals should be locals: put local (and a space) in front of all three lines.",
    start=text("""
        width = 80
        height = 24
        title = "nvim"
    """),
    target=text("""
        local width = 80
        local height = 24
        local title = "nvim"
    """),
    hint="Ctrl-v 2j selects the first column of the three lines, and I types in front of the block on every "
         "line when you press <Esc>.",
    uses=["count"],
)
block_insert.add(
    title="Qualify the columns", par=7, ext="sql", cursor=(2, 5),
    task="The query will join another table soon, so qualify the three column names with the alias: u.id, "
         "u.name, u.email. The cursor is on id.",
    start=text("""
        SELECT
            id,
            name,
            email
        FROM users u;
    """),
    target=text("""
        SELECT
            u.id,
            u.name,
            u.email
        FROM users u;
    """),
    hint="The names start in the same column, so a one-column block there and I put the prefix on all three.",
    uses=["count"],
)
block_insert.add(
    title="Commas for the array", par=7, ext="js", cursor=(2, 5),
    task="The array items are missing their commas. Put a comma at the end of each of the three item lines. "
         "The cursor is on \"red\".",
    start=text("""
        const COLORS = [
            "red"
            "green"
            "blue"
        ];
    """),
    target=text("""
        const COLORS = [
            "red",
            "green",
            "blue",
        ];
    """),
    hint="The lines have different lengths. $ in block mode makes the block reach each line's own end, and A "
         "appends there.",
    uses=["count"],
)
block_insert.add(
    title="Two-space YAML", par=7, ext="yaml", cursor=(2, 1),
    task="These three settings belong under env:, which this file indents by 2 spaces. Put two spaces in "
         "front of lines 2 to 4. The cursor is on line 2.",
    start=text("""
        env:
        DEBUG: "1"
        LOG_LEVEL: info
        PORT: "8080"
    """),
    target=text("""
        env:
          DEBUG: "1"
          LOG_LEVEL: info
          PORT: "8080"
    """),
    hint="> shifts by 'shiftwidth', 4 spaces here. A block insert types exactly the two spaces you want.",
    uses=["count"],
)
block_insert.add(
    title="Colons after the keys", par=7, ext="txt",
    task="Make this a key: value list: put a colon right after each key (host, port, user).",
    start=text("""
        host    localhost
        port    5432
        user    admin
    """),
    target=text("""
        host:    localhost
        port:    5432
        user:    admin
    """),
    hint="The keys all end in column 4. Get there with e, make a block down the three lines, and A appends "
         "right after the block, in the middle of each line.",
    uses=["word", "count"],
)
block_insert.add(
    title="Pad the track numbers", par=7, ext="txt",
    task="Give tracks 1 to 9 a leading zero (Track 01 ... Track 09) so that they sort properly. Track 10 is "
         "already fine.",
    start=text("""
        Track 1  intro
        Track 2  dawn
        Track 3  rain
        Track 4  wind
        Track 5  stone
        Track 6  river
        Track 7  smoke
        Track 8  ember
        Track 9  dusk
        Track 10  outro
    """),
    target=text("""
        Track 01  intro
        Track 02  dawn
        Track 03  rain
        Track 04  wind
        Track 05  stone
        Track 06  river
        Track 07  smoke
        Track 08  ember
        Track 09  dusk
        Track 10  outro
    """),
    hint="w gets to the number. A block down to Track 9 (the relative line numbers show how far), and I0 puts "
         "a 0 in front of each number.",
    uses=["word", "count"],
)
block_insert.add(
    title="A bash array", par=12, ext="sh", cursor=(2, 1),
    task="Quote every file name in the array: \"main.c\" and so on. The cursor is on main.c.",
    start=text("""
        FILES=(
        main.c
        util.c
        parse.c
        )
    """),
    target=text("""
        FILES=(
        "main.c"
        "util.c"
        "parse.c"
        )
    """),
    hint="Block-insert the opening quotes with I. gv selects the same block again, and $ and A add the closing "
         "quotes at each line's own end.",
    uses=["count", "visual-ends"],
)
block_insert.add(
    title="Export both groups", par=15, ext="sh",
    task="Put export (and a space) in front of the four variables, but not in front of the comments.",
    start=text("""
        # database
        DB_HOST=localhost
        DB_PORT=5432
        # cache
        REDIS_HOST=localhost
        REDIS_PORT=6379
    """),
    target=text("""
        # database
        export DB_HOST=localhost
        export DB_PORT=5432
        # cache
        export REDIS_HOST=localhost
        export REDIS_PORT=6379
    """),
    hint="Block-insert export on the first two variables. . repeats a block insert at the cursor on a block "
         "of the same size, so go down to the other two and press it.",
    uses=["count", "dot"],
)
block_insert.add(
    title="Semicolons in two rules", par=8, ext="css", cursor=(2, 5),
    task="Every declaration is missing its semicolon. Add one at the end of each of the four declaration "
         "lines. The cursor is on the first one.",
    start=text("""
        .a {
            color: red
            margin: 0
        }
        .b {
            color: blue
            padding: 4px
        }
    """),
    target=text("""
        .a {
            color: red;
            margin: 0;
        }
        .b {
            color: blue;
            padding: 4px;
        }
    """),
    hint="$A; on a two-line block does the first rule. . repeats the block append on two lines at the "
         "cursor, $ included, so get to the other rule's color line (* finds the next color) and press it.",
    uses=["count", "star", "dot"],
)
block_insert.add(
    title="Long options", par=10, ext="txt",
    task="Turn the options into long options: put -- in front of each of the four words in the two option "
         "columns.",
    start=text("""
        git log oneline graph
        git log stat    patch
    """),
    target=text("""
        git log --oneline --graph
        git log --stat    --patch
    """),
    hint="Block-insert -- in front of the first column of options (2w gets there). The second column lines "
         "up too, so W and . do it there.",
    uses=["word", "count", "bigword", "dot"],
)

# ---------- Ctrl-v c r d y ----------

block_edit = drills.command(
    "block-edit", "Ctrl-v  c  r  d  y", "change, fill, delete or copy a rectangle",
    """With a block selected (Ctrl-v and a motion), c deletes it and types your text on every line, r{c} fills
    it with {c}, d or x deletes it (the text on its right moves left), and y copies it. A yanked block stays
    a rectangle: P puts it with its top-left corner at the cursor (p just after the cursor), pushing the text
    there to the right, and p over another block selection replaces that block. U, u and ~ change the case of
    the block, and > pushes everything from the block's left edge one indent to the right. $ makes the right
    edge ragged, reaching each line's end.""",
    examples=[("Ctrl-v 2j e cnew<Esc>", "replace a word-wide column"), ("Ctrl-v j5l r#", "fill 2 rows of 6 with #"),
              ("Ctrl-v G l d", "delete the first two columns"), ("Ctrl-v 3j y ... P", "copy a rectangle, put it at the cursor"),
              ("Ctrl-v G U", "uppercase a column"), ("Ctrl-v G >", "push a column to the right")],
)
block_edit.add(
    title="Tick every box", par=5, ext="md", cursor=(1, 4),
    task="Everything is done: put an x in all four boxes. The cursor is inside the first box.",
    start=text("""
        - [ ] write the tests
        - [ ] fix the login bug
        - [ ] update the docs
        - [ ] tag v2.0
    """),
    target=text("""
        - [x] write the tests
        - [x] fix the login bug
        - [x] update the docs
        - [x] tag v2.0
    """),
    hint="Select the column of spaces inside the boxes with Ctrl-v. Then rx replaces every character in the "
         "block with an x.",
)
block_edit.add(
    title="Strip the prompts", par=4, ext="sh",
    task="You copied these commands from a tutorial, prompts and all. Delete the \"$ \" at the start of every "
         "line so you can run them as a script.",
    start=text("""
        $ git clone https://github.com/rick/vim-course
        $ cd vim-course
        $ python3 check.py
        $ python3 check.py drill
    """),
    target=text("""
        git clone https://github.com/rick/vim-course
        cd vim-course
        python3 check.py
        python3 check.py drill
    """),
    hint="Ctrl-v and G select the first column down to the last line. l widens the block to two columns, and "
         "d deletes it.",
    uses=["gg"],
)
block_edit.add(
    title="Mark them done", par=11, ext="txt",
    task="Change all three TODO tags to DONE.",
    start=text("""
        [TODO] write the tests
        [TODO] fix the login bug
        [TODO] update the docs
    """),
    target=text("""
        [DONE] write the tests
        [DONE] fix the login bug
        [DONE] update the docs
    """),
    hint="Move into the brackets and select the TODO column as a block (e goes to the end of the word). c "
         "deletes the block, and the word you type goes on every line when you press <Esc>.",
    uses=["word"],
)
block_edit.add(
    title="Capitalize the names", par=3, ext="csv", cursor=(2, 1),
    task="Capitalize the first letter of every name, but not the header. The cursor is on line 2.",
    start=text("""
        name,city,role
        ana,lima,admin
        raj,pune,dev
        mei,oslo,qa
        zoe,rome,dev
    """),
    target=text("""
        name,city,role
        Ana,lima,admin
        Raj,pune,dev
        Mei,oslo,qa
        Zoe,rome,dev
    """),
    hint="A one-column block from here to the last line, then U uppercases it.",
    uses=["case", "gg"],
)
block_edit.add(
    title="Erase the cloud", par=6, ext="txt",
    task="The sky cleared: erase the cloud on the left. The sun must stay where it is.",
    # Written line by line: text() would remove the leading spaces the lines have in common.
    start="\n".join([
        "    .--.             \\ | /",
        " .-(    ).           - O -",
        " (___.__)__)         / | \\",
    ]),
    target="\n".join([
        "                     \\ | /",
        "                     - O -",
        "                     / | \\",
    ]),
    hint="d would pull the sun to the left. Select the cloud as a block, and r followed by a space overwrites "
         "it with spaces. On the last line, E reaches the cloud's right edge.",
    uses=["bigword"],
)
block_edit.add(
    title="Drop the date column", par=6, ext="txt",
    task="Delete the date column, and the space after it, so that the city column moves into its place.",
    start=text("""
        user date       city
        ana  2024-01-31 Lima
        raj  2023-11-02 Pune
        mei  2025-06-15 Oslo
        zoe  2022-09-08 Rome
    """),
    target=text("""
        user city
        ana  Lima
        raj  Pune
        mei  Oslo
        zoe  Rome
    """),
    hint="w jumps to the date column. Ctrl-v G selects down to the last line in that column, E widens the "
         "block to the end of the date (a date is one WORD), l takes the space too, and d deletes the block.",
    uses=["word", "gg", "bigword"],
)
block_edit.add(
    title="Widen the gap", par=4, ext="txt",
    task="You're about to add some longer IPv6 addresses. Push the host names four columns to the right, and "
         "keep them lined up.",
    start=text("""
        127.0.0.1 localhost
        10.0.0.5  db
        10.0.0.6  cache
    """),
    target=text("""
        127.0.0.1     localhost
        10.0.0.5      db
        10.0.0.6      cache
    """),
    hint="In block mode, > shifts the text from the block's left edge to the right by one indent (4 spaces "
         "here) and leaves the text left of the block alone.",
    uses=["bigword", "gg", "indent"],
)
block_edit.add(
    title="Zero the counters", par=8, ext="c", cursor=(2, 16),
    task="Start the test from zero: set all four counters to 0. The cursor is on 1532.",
    start=text("""
        static struct stats expected = {
            .hits    = 1532,
            .misses  = 87,
            .errors  = 4,
            .retries = 12,
        };
    """),
    target=text("""
        static struct stats expected = {
            .hits    = 0,
            .misses  = 0,
            .errors  = 0,
            .retries = 0,
        };
    """),
    hint="A block that starts at the values and has a ragged right edge ($) covers each value and its comma. "
         "c replaces all of it with what you type.",
)
block_edit.add(
    title="Swap the columns", par=8, ext="md",
    task="Put the Code column first.",
    start=text("""
        | Country   | Code |
        |-----------|------|
        | Peru      | PE   |
        | India     | IN   |
    """),
    target=text("""
        | Code | Country   |
        |------|-----------|
        | PE   | Peru      |
        | IN   | India     |
    """),
    hint="Delete the Country column as a block, from the first | to just before the second (t| stops there). "
         "Then $ goes to the last |, and P puts the block in front of it.",
    uses=["t", "line", "p"],
)
block_edit.add(
    title="Add a Wednesday", par=21, ext="txt",
    task="Wednesday's plan is the same as Tuesday's. Add a Wednesday column to the right of Tuesday: a copy "
         "of the Tuesday column, with its heading changed.",
    start=text("""
        +-----------+-----------+
        | Monday    | Tuesday   |
        +-----------+-----------+
        | gym       | run       |
        | swim      | gym       |
        +-----------+-----------+
    """),
    target=text("""
        +-----------+-----------+-----------+
        | Monday    | Tuesday   | Wednesday |
        +-----------+-----------+-----------+
        | gym       | run       | run       |
        | swim      | gym       | gym       |
        +-----------+-----------+-----------+
    """),
    hint="Yank the Tuesday column as a block, from the + where it starts to just before the next + (t+). $ "
         "and P put it in front of the last column of + and |. Then type the new heading over the old one "
         "with R.",
    uses=["f", "gg", "t", "line", "p", "replace-mode"],
)
block_edit.add(
    title="Wider counters", par=10, ext="c",
    task="The counters can overflow an int. Change the type on all three lines from int to long.",
    start=text("""
        int count;
        int total;
        int max;
    """),
    target=text("""
        long count;
        long total;
        long max;
    """),
    hint="Ctrl-v 2j and e select the int column as a block. c deletes it, and what you type goes on every "
         "line when you press <Esc>.",
    uses=["count", "word"],
)
block_edit.add(
    title="Draw the divider", par=5, ext="txt", cursor=(1, 7),
    task="Draw a | down the column of spaces between the two columns, on all three lines. The cursor is on "
         "the space in line 1, column 7.",
    start=text("""
        name   role
        ana    dev
        raj    admin
    """),
    target=text("""
        name  |role
        ana   |dev
        raj   |admin
    """),
    hint="A one-column block down the three lines, and r| replaces each character in it.",
    uses=["count"],
)
block_edit.add(
    title="Drop the trailing comments", par=8, ext="c",
    task="Delete the // comments at the end of the four lines, and the two spaces before them.",
    start=text("""
        int a = 1;  // first
        int b = 2;  // second
        int c = 3;  // third
        int d = 4;  // fourth
    """),
    target=text("""
        int a = 1;
        int b = 2;
        int c = 3;
        int d = 4;
    """),
    hint="The comments start in the same column. Start the block just after the ;, go down three lines, and "
         "$ makes it reach the end of every line, however long. Then d.",
    uses=["f", "count", "line"],
)
block_edit.add(
    title="A longer fence", par=7, ext="txt",
    task="Make the fence twice as long: repeat everything after the first column at the end of both lines.",
    start=text("""
        +--+--+
        |  |  |
    """),
    target=text("""
        +--+--+--+--+
        |  |  |  |  |
    """),
    hint="Yank a block from column 2 to the end of both lines. $ goes to the end, and p puts the block after "
         "the cursor, on both lines at once.",
    uses=["line", "p"],
)
block_edit.add(
    title="Lowercase hex", par=5, ext="txt",
    task="Write the hex codes in lowercase (0x1f, 0x7f, 0x0a). The names stay in capitals.",
    start=text("""
        0x1F  US
        0x7F  DEL
        0x0A  LF
    """),
    target=text("""
        0x1f  US
        0x7f  DEL
        0x0a  LF
    """),
    hint="A block over the codes (e reaches the end of the first one), and u lowercases the block only.",
    uses=["word", "count", "case"],
)
block_edit.add(
    title="Time first", par=8, ext="log",
    task="Put the time before the level on every line: 10:01 ERROR disk full.",
    start=text("""
        ERROR 10:01 disk full
        WARN  10:02 slow query
        INFO  10:05 backup done
    """),
    target=text("""
        10:01 ERROR disk full
        10:02 WARN  slow query
        10:05 INFO  backup done
    """),
    hint="Cut the level column, with the space after it, as a block. Then W jumps over the time, and P puts "
         "the block in front of the cursor on all three lines.",
    uses=["count", "bigword", "p"],
)
block_edit.add(
    title="Capital cities and countries", par=6, ext="txt",
    task="Capitalize the first letter of each city and each country: Lima Peru, Pune India.",
    start=text("""
        ana    lima    peru
        raj    pune    india
    """),
    target=text("""
        ana    Lima    Peru
        raj    Pune    India
    """),
    hint="A one-column block on the first letters of the cities, and U. The country column lines up too, and "
         ". repeats a block change on a block of the same size at the cursor.",
    uses=["word", "case", "dot"],
)
block_edit.add(
    title="Shade the box", par=8, ext="txt",
    task="Fill the inside of the box with dots, without touching its edges.",
    start=text("""
        +------+
        |      |
        |      |
        +------+
    """),
    target=text("""
        +------+
        |......|
        |......|
        +------+
    """),
    hint="Start the block on the first space inside the box, take it down a line and across to the last "
         "space, and r. fills it.",
    uses=["count"],
)
block_edit.add(
    title="A second window", par=16, ext="txt",
    task="Copy the window (the 3-line, 4-column block) into the empty space on its right, with its left edge "
         "in column 10.",
    start=text("""
        +------------------+
        |  .--.            |
        |  |[]|            |
        |  '--'            |
        +------------------+
    """),
    target=text("""
        +------------------+
        |  .--.  .--.      |
        |  |[]|  |[]|      |
        |  '--'  '--'      |
        +------------------+
    """),
    hint="Yank the window as a block. P would push the wall to the right, so select a block of spaces the "
         "same size where it goes, and p replaces it.",
    uses=["f", "count", "p"],
)
block_edit.add(
    title="Id to the end", par=8, ext="txt",
    task="This export ends every field with a |. Move the id field (001| and so on) from the start of each "
         "line to the end.",
    start=text("""
        001|ana|lima|
        002|raj|pune|
        003|mei|oslo|
    """),
    target=text("""
        ana|lima|001|
        raj|pune|002|
        mei|oslo|003|
    """),
    hint="Cut the first four columns as a block. The lines are all the same length, so $ and p put the block "
         "after the last | on every line.",
    uses=["count", "line", "p"],
)

# ---------- o O gv ----------

visual_ends = drills.command(
    "visual-ends", "o  O  gv", "move the other end, or reselect",
    """In Visual mode, o jumps to the other end of the selection, so the next motion moves that end instead:
    Vip, then o and k, adds the line above the paragraph. In block mode, O jumps to the other corner on the
    same line, to move the left edge instead of the right. gv, in Normal mode, selects the last selection again,
    in the same mode and with the cursor at the same end, so you can do a second thing to the same text
    without selecting it again. After a Visual p, gv selects the text you put.""",
    examples=[("o", "jump to the other end"), ("O", "the other corner on this line (block mode)"),
              ("gv", "select the last selection again"), ("Vipok", "the paragraph and the line above it"),
              ("y gv r<Space>", "copy a block, then blank it out")],
    level="complex",
)
visual_ends.add(
    title="Bracket the timestamps", par=13, ext="log",
    task="Put each timestamp (the date and the time) in square brackets.",
    start=text("""
        2026-10-29 09:15 boot
        2026-10-29 09:20 login as rick
        2026-10-29 11:05 logout
    """),
    target=text("""
        [2026-10-29 09:15] boot
        [2026-10-29 09:20] login as rick
        [2026-10-29 11:05] logout
    """),
    hint="Select the timestamps as a block (2E reaches the end of the time), and A] closes the brackets. gv "
         "selects the same block again, so I[ can open them.",
    uses=["block-insert", "bigword", "count"],
)
visual_ends.add(
    title="Hollow out the frame", par=17, ext="txt", setup=["setlocal virtualedit=all"],
    task="Draw a frame of # starting in the top-left corner: 6 lines tall, 20 columns wide, and empty inside. "
         "virtualedit=all is set, like your :Art command, so the cursor can go anywhere.",
    start="\n" * 5,
    target=text("""
        ####################
        #                  #
        #                  #
        #                  #
        #                  #
        ####################
    """),
    hint="Fill the whole 6-by-20 rectangle with # first. gv selects it again, with the cursor in the bottom-right "
         "corner: move that corner in by one, o jumps to the top-left corner, move it in too, then erase the "
         "inside with r and a space.",
    uses=["block-edit", "virtualedit", "count"],
)
visual_ends.add(
    title="Move the moon", par=14, ext="txt", setup=["setlocal virtualedit=all"],
    task="Move the moon (the 3-line, 4-column block at the top left) one line down, with its left edge in "
         "column 20. The stars must not move. virtualedit=all is set.",
    start=text(r"""
         _.       *    .
        (  \   .     *
         `-'      *

        ~~~~~~~~~~~~~~~~~~~~~~~~
    """),
    # Written line by line: no line of the target starts in column 1, so text() would dedent it.
    target="\n".join([
        "          *    .",
        "       .     *      _.",
        "          *        (  \\",
        "                    `-'",
        "~~~~~~~~~~~~~~~~~~~~~~~~",
    ]),
    hint="Yank the moon as a block (on its last line, E reaches its right edge). gv selects it again, so that "
         "r and a space can blank it out without moving the stars. Then go down a line, 20| to column 20, and P.",
    uses=["block-edit", "bigword", "virtualedit"],
)
visual_ends.add(
    title="Quote the state codes", par=17, ext="csv",
    task="Clean up the state column for the import: make each code uppercase and put it in double quotes, "
         "so ma becomes \"MA\".",
    start=text("""
        boston,ma,617
        austin,tx,512
        denver,co,303
    """),
    target=text("""
        boston,"MA",617
        austin,"TX",512
        denver,"CO",303
    """),
    hint="The codes line up, so select them as a block (2w gets to the first one: the comma is a word of its "
         "own) and U them. gv brings the same block back for A\", and once more for I\".",
    uses=["block-edit", "block-insert", "word", "count"],
)
visual_ends.add(
    title="Name the macro", par=12, ext="c",
    task="Replace XXX in the macro name with the string on line 1, in capitals: TARGET_AUTHENTICATION.",
    start=text("""
        const char *target = "authentication";
        #define TARGET_XXX 1
    """),
    target=text("""
        const char *target = "authentication";
        #define TARGET_AUTHENTICATION 1
    """),
    hint="Yank the string with yi\". On line 2, T_ gets back onto XXX, and ve and p put the string over it. "
         "After a Visual p, gv selects the text you just put, so U can uppercase it.",
    uses=["visual", "quote", "y", "f", "word", "case"],
)
visual_ends.add(
    title="Codes in capitals", par=15, ext="txt",
    task="Fill the last column (the xx) with each row's country code from column 1, in capitals: US, GB, DE. "
         "Column 1 stays lowercase.",
    start=text("""
        us  United States  xx
        gb  United Kingdom xx
        de  Germany        xx
    """),
    target=text("""
        us  United States  US
        gb  United Kingdom GB
        de  Germany        DE
    """),
    hint="Yank the codes as a block. $h gets onto the first x, a block over the xx column and p put the "
         "codes over it. gv selects what you just put, and U uppercases it.",
    uses=["block-edit", "line", "count", "case"],
)

# ---------- g Ctrl-a ----------

g_ctrl_a = drills.command(
    "g-ctrl-a", "g Ctrl-a", "number lines 1, 2, 3…",
    """In Visual mode, Ctrl-a adds 1 to the first number on every selected line. g Ctrl-a adds more on each line:
    1 on the first, 2 on the second, 3 on the third. So write 0 on every line, select them, and g Ctrl-a
    numbers them 1, 2, 3. A count sets the step (4 g Ctrl-a adds 4, 8, 12), g Ctrl-x counts down instead, and
    in block mode only numbers inside the block's columns change. Hex numbers like 0x0f stay hex.""",
    examples=[("VG g Ctrl-a", "add 1, 2, 3 ... down to the last line"), ("4 g Ctrl-a", "add 4, 8, 12 ..."),
              ("g Ctrl-x", "subtract 1, 2, 3 ..."), ("Ctrl-v 2j g Ctrl-a", "only the numbers in the block's columns")],
    level="complex",
)
g_ctrl_a.add(
    title="Number the steps", par=11, ext="md", cursor=(2, 1),
    task="Number the four steps 1. to 4. The cursor is on the first step.",
    start=text("""
        ## Setup
        clone the repo
        install Neovim
        run check.py
        pick a project
    """),
    target=text("""
        ## Setup
        1. clone the repo
        2. install Neovim
        3. run check.py
        4. pick a project
    """),
    hint="Put \"0. \" in front of every step with a block insert. Then gv selects that block again, and "
         "g Ctrl-a adds 1 to the first line's number, 2 to the second's, and so on.",
    uses=["block-insert", "visual-ends", "gg"],
)
g_ctrl_a.add(
    title="Number the guests", par=7, ext="sql",
    task="Give each test user a name of its own: guest1, guest2, guest3. The ids must stay as they are.",
    start=text("""
        INSERT INTO users VALUES (1, 'guest0');
        INSERT INTO users VALUES (2, 'guest0');
        INSERT INTO users VALUES (3, 'guest0');
    """),
    target=text("""
        INSERT INTO users VALUES (1, 'guest1');
        INSERT INTO users VALUES (2, 'guest2');
        INSERT INTO users VALUES (3, 'guest3');
    """),
    hint="With V, g Ctrl-a would change the ids, the first number on each line. In block mode only the "
         "numbers inside the block count, so make a one-column block on the zeros.",
    uses=["f"],
)
g_ctrl_a.add(
    title="Step by four", par=6, ext="c",
    task="The registers are 4 bytes apart. Make the offsets 0x00, 0x04, 0x08 and 0x0c.",
    start=text("""
        #define REG_CTRL   0x00
        #define REG_STATUS 0x00
        #define REG_DATA   0x00
        #define REG_IRQ    0x00
    """),
    target=text("""
        #define REG_CTRL   0x00
        #define REG_STATUS 0x04
        #define REG_DATA   0x08
        #define REG_IRQ    0x0c
    """),
    hint="REG_CTRL stays at 0x00, so leave it out of the selection. A count before g Ctrl-a sets the step: "
         "4, 8, 12 (which is 0x0c).",
    uses=["count", "visual-line", "gg"],
)
g_ctrl_a.add(
    title="Number the servers", par=4, ext="yaml", cursor=(2, 1),
    task="Give each server its own name: web1, web2, web3, web4. The cursor is on the first one.",
    start=text("""
        servers:
          - name: web0
          - name: web0
          - name: web0
          - name: web0
    """),
    target=text("""
        servers:
          - name: web1
          - name: web2
          - name: web3
          - name: web4
    """),
    hint="Select the four lines with V and G. g Ctrl-a adds 1 to the first number on the first line, 2 on "
         "the second, and so on.",
    uses=["visual-line", "gg"],
)
g_ctrl_a.add(
    title="Stack the layers", par=7, ext="css",
    task="Each layer should sit 10 below the one above it: keep 100 for .modal and make the others 90, 80 "
         "and 70.",
    start=text("""
        .modal   { z-index: 100; }
        .drawer  { z-index: 100; }
        .header  { z-index: 100; }
        .tooltip { z-index: 100; }
    """),
    target=text("""
        .modal   { z-index: 100; }
        .drawer  { z-index: 90; }
        .header  { z-index: 80; }
        .tooltip { z-index: 70; }
    """),
    hint="g Ctrl-x counts down instead of up, and a count sets the step. Leave .modal out of the selection.",
    uses=["visual-line", "gg", "count"],
)
g_ctrl_a.add(
    title="Every fifteen minutes", par=10, ext="txt", cursor=(2, 1),
    task="The talks start every 15 minutes: make the times 09:00, 09:15, 09:30 and 09:45. The hours stay 09. "
         "The cursor is on line 2.",
    start=text("""
        09:00 welcome
        09:00 keynote
        09:00 demo
        09:00 questions
    """),
    target=text("""
        09:00 welcome
        09:15 keynote
        09:30 demo
        09:45 questions
    """),
    hint="With V, g Ctrl-a would change the hours, the first number on each line. A block over the minutes "
         "of lines 2 to 4 keeps it to them. Make the block both digits wide, and give g Ctrl-a a count of 15.",
    uses=["count"],
)

# ---------- :'<,'> ----------

visual_ex = drills.command(
    "visual-ex", ":'<,'>", "run an Ex command on the selected lines",
    """Press : in any Visual mode and Vim starts the command line with :'<,'> for you: the range from the first
    selected line ('<) to the last ('>). The command you type after it runs on those lines only, and always on
    whole lines, even from v or Ctrl-v. Handy ones: :sort (n sorts by number, ! reverses), :s/old/new/g
    (Project 07), :normal {keys} to type Normal-mode keys on every line (Projects 06 and 07), and :center,
    :right and :left. The marks stay set afterwards, so gv: gets you the same range again.""",
    examples=[("vip:sort<CR>", "sort a paragraph"), (":'<,'>s/a/b/g", "replace only in the selection"),
              (":'<,'>norm A;", "type A; on every selected line"), (":'<,'>sort! n", "by number, biggest first"),
              ("gv:", "the last selection's lines, again")],
    level="complex",
)
visual_ex.add(
    title="Follow the rename", par=18, ext="c", cursor=(3, 5),
    task="apply() now takes a pointer called opts. Change every cfg. in apply() to opts->, but leave dump() "
         "alone. The cursor is inside apply().",
    start=text("""
        void apply(struct config *opts) {
            set_width(cfg.width);
            set_height(cfg.height);
            set_title(cfg.title);
            set_fps(cfg.fps);
            set_vsync(cfg.vsync);
        }

        void dump(struct config cfg) {
            printf("%d\\n", cfg.width);
        }
    """),
    target=text("""
        void apply(struct config *opts) {
            set_width(opts->width);
            set_height(opts->height);
            set_title(opts->title);
            set_fps(opts->fps);
            set_vsync(opts->vsync);
        }

        void dump(struct config cfg) {
            printf("%d\\n", cfg.width);
        }
    """),
    hint="Va{ selects the whole function, from the line with its { to the line with its }. Press :, and the "
         ":s command you type only touches those lines.",
    uses=["subst", "brace"],
)
visual_ex.add(
    title="Capitalize the summaries", par=12, ext="md", cursor=(5, 1),
    task="Capitalize the first word after the colon in each 0.4.0 entry (fix: Handle empty input). Leave "
         "0.3.0 alone. The cursor is on the docs entry.",
    start=text("""
        ## 0.4.0

        fix: handle empty input
        feat: add dark mode
        docs: explain the drills
        refactor: split the parser
        test: cover the edge cases

        ## 0.3.0

        feat: first release
    """),
    target=text("""
        ## 0.4.0

        fix: Handle empty input
        feat: Add dark mode
        docs: Explain the drills
        refactor: Split the parser
        test: Cover the edge cases

        ## 0.3.0

        feat: first release
    """),
    hint="The words start in different columns, so a block won't do. Select the paragraph and run :normal on "
         "it: the keys you give it are typed at the start of every selected line. W gets to the word, and ~ "
         "flips the case of one letter.",
    uses=["normal", "ip", "bigword", "case"],
)
visual_ex.add(
    title="Rank the high scores", par=10, ext="txt",
    task="Sort the scores from highest to lowest. The heading stays on top.",
    start=text("""
        HIGH SCORES
        ana    120
        raj    340
        mei     95
        zoe    210
    """),
    target=text("""
        HIGH SCORES
        raj    340
        zoe    210
        ana    120
        mei     95
    """),
    hint="Select the score lines (not the heading) and press :. :sort n sorts by the first number on each "
         "line, and :sort! sorts in reverse.",
    uses=["sort", "visual-line", "gg"],
)
visual_ex.add(
    title="The sender's address", par=9, ext="txt",
    task="Right-align the three lines of the sender's address so that they end in column 30, like a letter. "
         "Leave the greeting alone.",
    start=text("""
        Rick Xie
        12 Main Street
        Lima

        Dear Ana,
    """),
    target="\n".join([
        "                      Rick Xie",
        "                12 Main Street",
        "                          Lima",
        "",
        "Dear Ana,",
    ]),
    hint="Select the three lines and press :. :right 30 (or :ri30 for short) moves each line right until it "
         "ends in column 30.",
    uses=["center", "count"],
)
visual_ex.add(
    title="Sort the tags", par=10, ext="txt", cursor=(4, 1),
    task="Sort the tags in the middle paragraph alphabetically and remove the repeats, so each tag appears "
         "once. The cursor is inside the paragraph.",
    start=text("""
        # Tags for the post

        vim
        neovim
        editors
        vim
        macros
        neovim

        # Notes
        Publish on Friday.
    """),
    target=text("""
        # Tags for the post

        editors
        macros
        neovim
        vim

        # Notes
        Publish on Friday.
    """),
    hint="vip selects the paragraph. Press :, and :sort with the u flag (:sor u for short) sorts the lines "
         "and keeps only the first of each run of equal ones.",
    uses=["sort", "ip"],
)
visual_ex.add(
    title="Shout the methods", par=12, ext="txt", cursor=(2, 1),
    task="Uppercase the HTTP method at the start of each route line (GET, POST, ...). The methods have "
         "different lengths, and the paths stay as they are. The cursor is on the first route.",
    start=text("""
        # routes
        get /users
        post /users
        get /users/:id
        put /users/:id
        patch /users/:id
        delete /users/:id
        get /health
        post /login
    """),
    target=text("""
        # routes
        GET /users
        POST /users
        GET /users/:id
        PUT /users/:id
        PATCH /users/:id
        DELETE /users/:id
        GET /health
        POST /login
    """),
    hint="A block can't follow words of different lengths. Select the route lines and run :normal on them: "
         "its keys are typed at the start of every selected line, and gUe uppercases the first word.",
    uses=["normal", "visual-line", "gg", "case", "word"],
)

# ---------- virtualedit N| ----------

virtualedit = drills.command(
    "virtualedit", "virtualedit  {N}|", "edit past line ends, jump to column N",
    """N| moves the cursor to column N of the line (| alone goes to column 1). Normally the cursor can't go past
    the last character, so on a short line 30| stops at the end. The 'virtualedit' option (ve for short)
    lifts that limit: :set ve=block in block mode only, :set ve=all everywhere, and :set ve= is back to
    normal. Past the end of a line, typing, r, A and P fill the gap with spaces, which is how you line things
    up in a column and draw in empty space. Your :Art command sets ve=all.""",
    examples=[("30|", "column 30"), (":set ve=all", "go anywhere, like :Art"), (":set ve=block", "only in block mode"),
              (":set ve=", "back to normal"), ("Ctrl-v 3j 39| A\\<Esc>", "a \\ in column 40 on four lines")],
    level="complex",
)
virtualedit.add(
    title="Line up the backslashes", par=9, ext="c", setup=["setlocal virtualedit=block"],
    task="Finish the macro: put a backslash in column 40 of lines 1 to 4, all lined up. virtualedit=block is "
         "set for this one.",
    start=text("""
        #define SWAP(a, b) do {
            int tmp_ = (a);
            (a) = (b);
            (b) = tmp_;
        } while (0)
    """),
    target=text("""
        #define SWAP(a, b) do {                \\
            int tmp_ = (a);                    \\
            (a) = (b);                         \\
            (b) = tmp_;                        \\
        } while (0)
    """),
    hint="Make a block over lines 1 to 4 that reaches column 39 (39| goes there, past the end of the line, "
         "thanks to virtualedit=block). A appends after the block's right edge and pads every line with spaces "
         "up to it.",
    uses=["block-insert"],
)
virtualedit.add(
    title="Raise the flag", par=10, ext="txt", setup=["setlocal virtualedit=all"],
    task="Plant a flagpole next to the tree: a | in column 14 on all four lines, and a > flag just right of "
         "the top one. virtualedit=all is set, like your :Art command.",
    # Written line by line: text() would remove the leading spaces the lines have in common.
    start="\n".join([
        "    *",
        "   ***",
        "  *****",
        "    |",
    ]),
    target="\n".join([
        "    *        |>",
        "   ***       |",
        "  *****      |",
        "    |        |",
    ]),
    hint="14| jumps to column 14, even past the end of the line. A block from there down three lines, and r| "
         "draws the whole pole. A then appends the flag at the end of the top line.",
    uses=["block-edit", "insert"],
)
virtualedit.add(
    title="Build another house", par=9, ext="txt", setup=["setlocal virtualedit=all"],
    task="Build a second house to the right of the first: an exact copy, with its left edge in column 10. "
         "virtualedit=all is set.",
    start=text(r"""
          /\
         /  \
        /____\
        |_[]_|
    """),
    target=text(r"""
          /\       /\
         /  \     /  \
        /____\   /____\
        |_[]_|   |_[]_|
    """),
    hint="Yank the house as a block (E on the bottom line reaches its right edge). 10| goes to column 10, past "
         "the end of the short top line, and P puts the block there.",
    uses=["block-edit", "bigword"],
)
virtualedit.add(
    title="Flip the flags", par=8, ext="txt",
    task="In this fixed-width bank file, column 15 is the paid flag. Set it to Y on all three records.",
    start=text("""
        00412ANA  0042N2026-11-01
        00413RAJ  0107N2026-11-02
        00414MEI  0009N2026-11-03
    """),
    target=text("""
        00412ANA  0042Y2026-11-01
        00413RAJ  0107Y2026-11-02
        00414MEI  0009Y2026-11-03
    """),
    hint="15| jumps straight to column 15, with no counting of words. A block from there down the three "
         "lines, and rY.",
    uses=["block-edit", "count"],
)
virtualedit.add(
    title="Label the box", par=16, ext="txt", setup=["setlocal virtualedit=all"],
    task="Write the label <-- port 80 on line 2, starting in column 20, out in the empty space to the right "
         "of the box. virtualedit=all is set.",
    start=text("""
        +--------+
        |  web   |
        +--------+
    """),
    target=text("""
        +--------+
        |  web   |         <-- port 80
        +--------+
    """),
    hint="With virtualedit=all, 20| goes to column 20 even past the end of the line, and text you insert "
         "there gets spaces in front of it to fill the gap.",
    uses=["insert"],
)
virtualedit.add(
    title="Trim the hex dump", par=7, ext="txt",
    task="Trim the hex dump to the offset and the first seven bytes: delete everything from column 27 on, "
         "on every line. The short last line stays as it is.",
    start=text("""
        0000: 48 65 6c 6c 6f 20 57 6f 72 6c 64 0a
        0010: 49 74 20 77 6f 72 6b 73 21 0a
        0020: 0a
    """),
    target=text("""
        0000: 48 65 6c 6c 6f 20 57
        0010: 49 74 20 77 6f 72 6b
        0020: 0a
    """),
    hint="27| goes to column 27. A block from there down one line, with $ to reach the end of both lines, "
         "and d.",
    uses=["block-edit", "line"],
)

# ---------- :center :right :left (glossary only) ----------

drills.command(
    "center", ":center  :right  :left", "center or align lines",
    """:center N centers each line of the range in a width of N columns, :right N moves each line right until it
    ends in column N, and :left N sets each line's indent to N spaces (0 if you leave N out). Without N, the
    width is 'textwidth', or 80 if that's 0. They work on whole lines, so give them a range, usually :'<,'>
    from Visual mode. Short forms: :ce, :ri and :le.""",
    examples=[(":'<,'>center 40", "center in 40 columns"), (":ce30", "short for :center 30"),
              (":'<,'>right 72", "make the lines end in column 72"), (":'<,'>left", "remove the indent")],
    level=None,
)
