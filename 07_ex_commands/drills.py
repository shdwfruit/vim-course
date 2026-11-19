"""Drills for Project 07: short problems that practice one command at a time.
Play them with:  python3 check.py drill      (the reference solutions are in ../solutions/drills/)"""
from trainer import Drills, text

drills = Drills(__file__)

# Completion (Ctrl-n, Ctrl-x Ctrl-l) only searches your own file, as in the exercises (see check.py).
OWN_FILE_ONLY = ["setlocal complete=."]

# ---------- :s ----------

subst = drills.command(
    "subst", ":s/old/new/", "substitute",
    """:s/old/new/ replaces the first match of the pattern old on the cursor line with new. Add the g flag
    (:s/old/new/g) to replace every match on the line, and put a range in front to cover more lines:
    :%s/old/new/g does the whole file. The pattern is a regular expression, so . * [ ~ ^ $ and \\ are
    special (\\. is a literal dot), and \\< \\> match the start and end of a word. An empty pattern
    (:s//new/) reuses your last search, so * then :%s//new/g renames the word under the cursor. In the
    replacement, & is the whole match and \\r is a line break. The closing / is optional, leaving out the
    replacement deletes the match, and another separator like # can stand in for the / (:s#/usr#/opt#).""",
    examples=[(":s/a/b/", "first a on this line"), (":s/a/b/g", "every a on this line"),
              (":%s/a/b/g", "every a in the file"), ("*:%s//b/g", "the word under the cursor, everywhere"),
              (":%s/\\d\\+/&px/g", "& is the match: 12 becomes 12px"), (":s#/usr#/opt#", "# as the separator")],
)
subst.add(
    title="Underscores, not dashes", par=9, ext="csv", setup=OWN_FILE_ONLY,
    task="The database wants snake_case column names. Change every - in this header to _.",
    start="user-id,first-name,last-name,birth-date,home-city",
    target="user_id,first_name,last_name,birth_date,home_city",
    hint=":s/-/_/ works on the cursor line, but only on the first match. The g flag at the end changes every "
         "match on the line.",
)
subst.add(
    title="INI to YAML", par=9, ext="yaml", setup=OWN_FILE_ONLY,
    task="Turn the first = on each line into a colon and a space. The = inside the URL stays.",
    start=text("""
        name=shop
        host=db.local
        url=postgres://db/shop?ssl=true
        timeout=30
    """),
    target=text("""
        name: shop
        host: db.local
        url: postgres://db/shop?ssl=true
        timeout: 30
    """),
    hint="The range % runs :s on every line. Without the g flag, :s changes only the first match on each "
         "line, which is exactly what you want here.",
    uses=["range"],
)
subst.add(
    title="Double quotes everywhere", par=10, ext="py", setup=OWN_FILE_ONLY,
    task="The style guide says double quotes. Change every ' in the file to \".",
    start=text("""
        name = 'Ada'
        langs = ['C', 'Java', 'Python']
        print('Hello, ' + name)
    """),
    target=text("""
        name = "Ada"
        langs = ["C", "Java", "Python"]
        print("Hello, " + name)
    """),
    hint="% for every line, and the g flag for every match on each line: :%s/'/\"/g.",
    uses=["range"],
)
subst.add(
    title="Rename the loop variable", par=12, ext="java", cursor=(2, 14), setup=OWN_FILE_ONLY,
    task="The cursor is on the loop variable c. Rename it to col everywhere. cols must not change.",
    start=text("""
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                grid[r][c] = r * cols + c;
            }
        }
    """),
    target=text("""
        for (int r = 0; r < rows; r++) {
            for (int col = 0; col < cols; col++) {
                grid[r][col] = r * cols + col;
            }
        }
    """),
    hint="* searches for the whole word under the cursor (\\<c\\>), and :s with an empty pattern reuses the "
         "last search. Some lines have c more than once.",
    uses=["star", "range"],
)
subst.add(
    title="Only at the start of a word", par=16, ext="java", setup=OWN_FILE_ONLY,
    task="Rename the getters: getName becomes fetchName, and so on. Widget and budget contain \"get\" "
         "too, and must not change.",
    start=text("""
        String n = user.getName();
        int a = user.getAge();
        Widget w = cart.getWidget();
        double b = budget.getTotal();
    """),
    target=text("""
        String n = user.fetchName();
        int a = user.fetchAge();
        Widget w = cart.fetchWidget();
        double b = budget.fetchTotal();
    """),
    hint="\\< in a pattern matches only at the start of a word, so \\<get skips the get inside Widget and "
         "budget. Each line has one getter.",
    uses=["range"],
)
subst.add(
    title="Headers into lib/", par=12, ext="c", setup=OWN_FILE_ONLY,
    task="The project's own headers moved into lib/. Change \"util.h\" to \"lib/util.h\" and so on. The "
         "<system> headers stay.",
    start=text("""
        #include <stdio.h>
        #include "util.h"
        #include <string.h>
        #include "parse.h"
        #include "net.h"
    """),
    target=text("""
        #include <stdio.h>
        #include "lib/util.h"
        #include <string.h>
        #include "lib/parse.h"
        #include "lib/net.h"
    """),
    hint="Replace the first \" on each line with \"lib/. The replacement has a slash in it, so either write "
         "it as \\/ or use another separator: :%s#a#b# works just like :%s/a/b/.",
    uses=["range"],
)
subst.add(
    title="Add the units", par=15, ext="css", setup=OWN_FILE_ONLY,
    task="CSS needs units: put px after every number.",
    start=text("""
        .card {
            margin: 8 16;
            padding: 4;
            border-radius: 6;
        }
    """),
    target=text("""
        .card {
            margin: 8px 16px;
            padding: 4px;
            border-radius: 6px;
        }
    """),
    hint="\\d\\+ matches a number (one or more digits). In the replacement, & is the whole match, so &px "
         "writes the number back with px after it. Line 2 has two numbers.",
    uses=["range"],
)
subst.add(
    title="Drop the semicolons", par=7, ext="py", setup=OWN_FILE_ONLY,
    task="Someone wrote this Python with Java habits. Delete the ; at the end of each line. The ; inside "
         "the string stays.",
    start=text("""
        total = 0;
        for x in xs:
            total += x;
        print("sum: %d; n: %d" % (total, len(xs)));
    """),
    target=text("""
        total = 0
        for x in xs:
            total += x
        print("sum: %d; n: %d" % (total, len(xs)))
    """),
    hint="$ at the end of a pattern means \"at the end of the line\", so ;$ only matches a final semicolon. "
         "To delete a match, leave the replacement empty. You can even leave out the slashes after it.",
    uses=["range"],
)
subst.add(
    title="One directory per line", par=10, ext="txt", setup=OWN_FILE_ONLY,
    task="This is a $PATH. Split it into one directory per line: every : becomes a line break.",
    start="/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin",
    target=text("""
        /opt/homebrew/bin
        /opt/homebrew/sbin
        /usr/local/bin
        /usr/bin
        /bin
        /usr/sbin
        /sbin
    """),
    hint="In the replacement, \\r is a line break. (\\n would insert a null byte instead, shown as ^@.)",
)
subst.add(
    title="Rename and requote", par=23, ext="py", setup=OWN_FILE_ONLY,
    task="Two cleanups: rename the variable c to config (the c inside other words stays), and switch every "
         "' to \".",
    start=text("""
        c = load('app.toml')
        port = c['port']
        host = c.get('host', 'localhost')
        print('listening on', host, port, c)
    """),
    target=text("""
        config = load("app.toml")
        port = config["port"]
        host = config.get("host", "localhost")
        print("listening on", host, port, config)
    """),
    hint="Two :s commands. For the rename, the cursor is already on c: * searches for it as a whole word, "
         "and :%s//config reuses that search. Then :%s/'/\"/g for the quotes.",
    uses=["star", "range"],
)
subst.add(
    title="Forward slashes", par=11, ext="ini", setup=OWN_FILE_ONLY,
    task="The build now runs on Linux too. Change every \\ in these Windows paths to /.",
    start=text("""
        [paths]
        source = C:\\Users\\ada\\code\\shop\\src
        build = C:\\Users\\ada\\code\\shop\\build\\out
        logs = D:\\logs\\shop
    """),
    target=text("""
        [paths]
        source = C:/Users/ada/code/shop/src
        build = C:/Users/ada/code/shop/build/out
        logs = D:/logs/shop
    """),
    hint="A backslash is special in a pattern, so a literal one is written \\\\. The replacement is a /, so "
         "a separator other than / saves escaping that one too.",
    uses=["range"],
)
subst.add(
    title="Columns to CSV", par=12, ext="txt", setup=OWN_FILE_ONLY,
    task="This ps output lines its columns up with runs of spaces. Make it CSV: each run of spaces becomes "
         "one comma.",
    start=text("""
        PID   USER   %CPU  %MEM  COMMAND
        412   ada    12.0  1.4   nvim
        1088  root   0.3   0.1   sshd
        2231  ada    48.5  9.8   python3
        77    _www   0.0   0.2   httpd
    """),
    target=text("""
        PID,USER,%CPU,%MEM,COMMAND
        412,ada,12.0,1.4,nvim
        1088,root,0.3,0.1,sshd
        2231,ada,48.5,9.8,python3
        77,_www,0.0,0.2,httpd
    """),
    hint="\\+ after a character means one or more of it, so a space followed by \\+ matches a whole run of "
         "spaces. Each line has four runs.",
    uses=["range"],
)
subst.add(
    title="Drop the trailing comments", par=10, ext="js", setup=OWN_FILE_ONLY,
    task="Delete every // comment and the space before it. The // in the URL and the / that divides are "
         "code, and stay.",
    start=text("""
        const API = "https://api.example.com"; // base url
        let total = 0; // running sum
        for (let i = 0; i < prices.length; i++) total += prices[i];
        const avg = total / prices.length; // mean price
        if (avg > 100) { // expensive
            alert("Big spender!");
        } // end if
    """),
    target=text("""
        const API = "https://api.example.com";
        let total = 0;
        for (let i = 0; i < prices.length; i++) total += prices[i];
        const avg = total / prices.length;
        if (avg > 100) {
            alert("Big spender!");
        }
    """),
    hint=".* matches everything to the end of the line, and an empty replacement deletes the match. What comes "
         "just before each comment's // but not before the URL's? With # as the separator, the slashes need "
         "no backslashes.",
    uses=["range"],
)
subst.add(
    title="Quote the keys", par=13, ext="js", setup=OWN_FILE_ONLY,
    task="This object is going into a JSON file, and JSON wants its keys in double quotes: name: becomes "
         "\"name\":.",
    start=text("""
        {
          name: "shop",
          version: "1.4.2",
          private: true,
          main: "index.js",
          dev_port: 8080
        }
    """),
    target=text("""
        {
          "name": "shop",
          "version": "1.4.2",
          "private": true,
          "main": "index.js",
          "dev_port": 8080
        }
    """),
    hint="The key is the first word on each line, and \\w\\+ matches a word (one or more word characters). & in "
         "the replacement puts the match back, so it can go between two quotes.",
    uses=["range"],
)
subst.add(
    title="Just the messages", par=9, ext="log", setup=OWN_FILE_ONLY,
    task="Delete the timestamp and the [worker] tag from every line, and the space after them, so only the "
         "messages are left.",
    start=text("""
        2026-03-14T09:14:02Z [web-1] GET /health 200
        2026-03-14T09:14:05Z [worker-12] job 4411 done
        2026-03-14T09:14:09Z [api] POST /orders 201
        2026-03-14T09:15:30Z [web-1] GET /cart 500
    """),
    target=text("""
        GET /health 200
        job 4411 done
        POST /orders 201
        GET /cart 500
    """),
    hint=".* matches as much as it can, so .* followed by more text runs to the last place that text appears "
         "on the line. Here that's the ] and the space after it.",
    uses=["range"],
)
subst.add(
    title="Strict equality", par=17, ext="js", setup=OWN_FILE_ONLY,
    task="The linter wants === instead of ==. Change every == to ===. The === and !== that are already "
         "there must not change.",
    start=text("""
        if (user.role == "admin") grant(user);
        if (count == 0 || items == null) return;
        const same = a === b;
        const differs = a !== b;
        while (next == undefined) next = read();
        assert(sum(xs) == 10 && max(xs) == 4);
        return mode == "dark" ? dark : light;
    """),
    target=text("""
        if (user.role === "admin") grant(user);
        if (count === 0 || items === null) return;
        const same = a === b;
        const differs = a !== b;
        while (next === undefined) next = read();
        assert(sum(xs) === 10 && max(xs) === 4);
        return mode === "dark" ? dark : light;
    """),
    hint="== alone also matches inside === and !==. What's on both sides of every == that has to change? "
         "Some lines have two.",
    uses=["range"],
)
subst.add(
    title="Strip the tags", par=15, ext="html", setup=OWN_FILE_ONLY,
    task="Make this plain text: delete every HTML tag, opening and closing, and keep the text between them.",
    start=text("""
        <h1>Welcome</h1>
        <p>Read <a href="/docs">the docs</a> first.</p>
        <p>It's <b>free</b> and <em>open</em>.</p>
    """),
    target=text("""
        Welcome
        Read the docs first.
        It's free and open.
    """),
    hint="<.*> would run from the first < to the last > on the line. [^>] matches any character except >, "
         "so < then any number of those then > is exactly one tag.",
    uses=["range"],
)
subst.add(
    title="European prices", par=18, ext="csv", setup=OWN_FILE_ONLY,
    task="These prices are written the European way, 1.299,00. Make them 1299.00: drop the dots that group "
         "the thousands, then make the decimal comma a dot.",
    start=text("""
        item;price
        laptop;1.299,00
        mouse;24,90
        server;12.450,50
        budget;1.000.000,00
    """),
    target=text("""
        item;price
        laptop;1299.00
        mouse;24.90
        server;12450.50
        budget;1000000.00
    """),
    hint="Two :s commands, and the order matters: once the commas are dots, you can't tell them from the "
         "thousands dots. A dot in a pattern is \\.. Each line has at most one comma.",
    uses=["range"],
)
subst.add(
    title="One import per line", par=12, ext="py", setup=OWN_FILE_ONLY,
    task="PEP 8 wants one import per line: split this into five import lines, in the same order.",
    start="import os, sys, json, re, shutil",
    target=text("""
        import os
        import sys
        import json
        import re
        import shutil
    """),
    hint="\\r in the replacement breaks the line, and each new line needs import in front. The cursor is on "
         "import, so Ctrl-r Ctrl-w can type it for you. Look at what's left after the comma: the space is "
         "already there.",
    uses=["ctrl-r-ctrl-w"],
)
subst.add(
    title="It lives in config now", par=17, ext="js", cursor=(4, 18), setup=OWN_FILE_ONLY,
    task="BASE_URL moved onto the config object: every BASE_URL becomes config.BASE_URL. ADMIN_BASE_URL "
         "is a different constant and stays. The cursor is on the first BASE_URL.",
    start=text("""
        import config from "./config.js";

        export function get(path) {
            return fetch(BASE_URL + path);
        }

        export function post(path, body) {
            log(`POST ${BASE_URL}${path}`);
            return fetch(BASE_URL + path, { method: "POST", body });
        }

        const admin = ADMIN_BASE_URL + "/admin";
        export const ping = () => fetch(BASE_URL + "/ping").then(() => BASE_URL);
    """),
    target=text("""
        import config from "./config.js";

        export function get(path) {
            return fetch(config.BASE_URL + path);
        }

        export function post(path, body) {
            log(`POST ${config.BASE_URL}${path}`);
            return fetch(config.BASE_URL + path, { method: "POST", body });
        }

        const admin = ADMIN_BASE_URL + "/admin";
        export const ping = () => fetch(config.BASE_URL + "/ping").then(() => config.BASE_URL);
    """),
    hint="* searches for the whole word under the cursor, so it skips ADMIN_BASE_URL, and :s with an empty "
         "pattern reuses it. In the replacement, & is the match itself, so there's no need to type it again.",
    uses=["star", "range"],
)

# ---------- ranges ----------

rng = drills.command(
    "range", ":5,9  :.,+3  :%", "ranges: which lines a command touches",
    """A range in front of an Ex command says which lines it works on. % is every line, . the cursor line,
    $ the last line, a number is that line, and 5,9 is lines 5 to 9. +N and -N count from the cursor, so
    .,+3 (or just ,+3) is this line and the three below it, and .,$ is from here to the end. Two shortcuts
    type a range for you: a count before : (4: becomes :.,.+3, and relative line numbers show you the
    count), and : in Visual mode (it becomes :'<,'>, the selected lines). Lines in the range that don't
    match a :s pattern are simply skipped. With no range, most commands work on the cursor line only;
    :g, :v and :sort are the exceptions, and default to the whole file.""",
    examples=[(":2,4s/a/b/g", "lines 2 to 4"), ("4:s/a/b/g", "4: becomes :.,.+3"),
              (":,$s/a/b/g", "from here to the end"), ("vip:s/a/b/g", "the selected paragraph"),
              (":3,5t.", "copy lines 3-5 below the cursor"), (":-2d", "delete the line two above")],
)
rng.add(
    title="Only lines 2 to 4", par=17, ext="java", cursor=(6, 1), setup=OWN_FILE_ONLY,
    task="add(), sub() and mul() can overflow. Change every int on lines 2 to 4 to long. sign() keeps "
         "its ints. The cursor starts on the last line.",
    start=text("""
        class Calc {
            static int add(int a, int b) { return a + b; }
            static int sub(int a, int b) { return a - b; }
            static int mul(int a, int b) { return a * b; }
            static int sign(int a) { return Integer.signum(a); }
        }
    """),
    target=text("""
        class Calc {
            static long add(long a, long b) { return a + b; }
            static long sub(long a, long b) { return a - b; }
            static long mul(long a, long b) { return a * b; }
            static int sign(int a) { return Integer.signum(a); }
        }
    """),
    hint="Put the line numbers in front of s: :2,4s/int/long/g. Each line has three ints, so you need g.",
    uses=["subst"],
)
rng.add(
    title="A count before the colon", par=10, ext="py", setup=OWN_FILE_ONLY,
    task="Switch greet() to double quotes. legacy_greet() must keep its single quotes.",
    start=text("""
        def greet(name):
            print('Hello, ' + name)
            print('Welcome back!')
            log('greeted ' + name)

        def legacy_greet(name):
            print('Hello, ' + name)
    """),
    target=text("""
        def greet(name):
            print("Hello, " + name)
            print("Welcome back!")
            log("greeted " + name)

        def legacy_greet(name):
            print('Hello, ' + name)
    """),
    hint="Typing 4 before : fills in :.,.+3, the cursor line and the three below it. The def line has no "
         "quotes, but that's fine: :s skips lines where the pattern doesn't match.",
    uses=["subst"],
)
rng.add(
    title="From here to the end", par=12, ext="txt", cursor=(4, 1), setup=OWN_FILE_ONLY,
    task="Make it rain harder: from the cursor line (line 4, the first row of rain) to the end, every . "
         "becomes '. The dots in the cloud stay.",
    start=text("""
           .--.
         .(    ).
        (___.__)__)
          .  .  .
         .  .  .
          .  .  .
         .  .  .
          .  .  .
         .  .  .
          .  .  .
         .  .  .
          .  .  .
         .  .  .
    """),
    target=text("""
           .--.
         .(    ).
        (___.__)__)
          '  '  '
         '  '  '
          '  '  '
         '  '  '
          '  '  '
         '  '  '
          '  '  '
         '  '  '
          '  '  '
         '  '  '
    """),
    hint=".,$ means from the cursor line to the last line, and the . is optional: :,$s/.../.../g. "
         "A plain . in a pattern matches any character, so write \\. for a dot.",
    uses=["subst"],
)
rng.add(
    title="Inside the braces", par=12, ext="py", cursor=(6, 5), setup=OWN_FILE_ONLY,
    task="COLORS is going into a JSON file, so inside its braces every ' becomes \". TITLE keeps its "
         "single quotes. The cursor starts inside the braces, on line 6.",
    start=text("""
        TITLE = 'Paint'
        COLORS = {
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'white': (255, 255, 255),
            'black': (0, 0, 0),
        }
    """),
    target=text("""
        TITLE = 'Paint'
        COLORS = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "white": (255, 255, 255),
            "black": (0, 0, 0),
        }
    """),
    hint="vi{ selects everything inside the braces. Press : and Neovim types :'<,'> for you, the selected "
         "lines.",
    uses=["subst", "visual", "brace"],
)
rng.add(
    title="Reuse the setup lines", par=7, ext="py", cursor=(7, 1), setup=OWN_FILE_ONLY,
    task="test_sub() needs the same three setup lines as test_add(). Copy lines 2 to 4 to just below the "
         "cursor line, def test_sub() on line 7.",
    start=text("""
        def test_add():
            calc = Calculator()
            calc.clear()
            calc.mode = "exact"
            assert calc.add(2, 2) == 4

        def test_sub():
            assert calc.sub(5, 3) == 2
    """),
    target=text("""
        def test_add():
            calc = Calculator()
            calc.clear()
            calc.mode = "exact"
            assert calc.add(2, 2) == 4

        def test_sub():
            calc = Calculator()
            calc.clear()
            calc.mode = "exact"
            assert calc.sub(5, 3) == 2
    """),
    hint=":t copies lines, and the address after it says where to: . is below the cursor line. Give it the "
         "range of lines to copy in front.",
    uses=["copy-move"],
)
rng.add(
    title="Install comes first", par=7, ext="md", setup=OWN_FILE_ONLY,
    task="Move the Install section (the blank line above it, its heading and its command) up so it comes "
         "before Usage.",
    start=text("""
        # tinyhttp

        ## Usage
        tinyhttp serve ./public

        ## Install
        brew install tinyhttp

        ## License
        MIT
    """),
    target=text("""
        # tinyhttp

        ## Install
        brew install tinyhttp

        ## Usage
        tinyhttp serve ./public

        ## License
        MIT
    """),
    hint=":m moves lines, and like :t it takes a range in front and an address after it: the line to put "
         "them below. Lines 5 to 7 belong just below line 1.",
    uses=["copy-move"],
)
rng.add(
    title="Port four prints", par=16, ext="py", setup=OWN_FILE_ONLY,
    task="Port lines 3 to 6 to Python 3: print \"x\" becomes print(\"x\").",
    start=text("""
        import sys

        print "usage: wc.py FILE"
        print "counts lines, words and bytes"
        print "FILE can be - for stdin"
        print "version 1.0"
        sys.exit(2)
    """),
    target=text("""
        import sys

        print("usage: wc.py FILE")
        print("counts lines, words and bytes")
        print("FILE can be - for stdin")
        print("version 1.0")
        sys.exit(2)
    """),
    hint=":normal runs Normal-mode keys on every line of its range. On one line you'd type f r(A): replace "
         "the first space with ( and append ). Give :norm the range 3,6.",
    uses=["normal", "f", "r", "insert"],
)
rng.add(
    title="Sort just the imports", par=6, ext="py", setup=OWN_FILE_ONLY,
    task="Sort the four import lines alphabetically. Leave the rest of the file alone.",
    start=text("""
        import sys
        import json
        import re
        import os

        def main():
            print(os.getcwd(), sys.argv)
    """),
    target=text("""
        import json
        import os
        import re
        import sys

        def main():
            print(os.getcwd(), sys.argv)
    """),
    hint=":sort with no range sorts the whole file, which would scramble main(). A count before : gives it "
         "just the lines you want.",
    uses=["sort"],
)
rng.add(
    title="Make it a list", par=13, ext="md", cursor=(5, 1), setup=OWN_FILE_ONLY,
    task="Turn the indented outline (lines 3 to 7) into a Markdown list: put \"- \" before the text on "
         "each line, after its indentation. The cursor starts on line 5.",
    start=text("""
        # Trip

        packing
          clothes
          charger
        tickets
          passport

        Leave at 8.
    """),
    target=text("""
        # Trip

        - packing
          - clothes
          - charger
        - tickets
          - passport

        Leave at 8.
    """),
    hint="vip selects the paragraph the cursor is in, and : turns it into the range '<,'>. Then :norm I- "
         "inserts \"- \" at the first non-blank of every selected line.",
    uses=["visual-line", "ip", "normal", "insert"],
)
rng.add(
    title="Two functions, one fix", par=16, ext="c", setup=OWN_FILE_ONLY,
    task="reset() and respawn() take a pointer, so p.field must become p->field in them. reset_copy() "
         "works on a copy of the struct on purpose, and stays as it is.",
    start=text("""
        void reset(struct player *p) {
            p.score = p.lives = 0;
            p.x = p.y = 0;
        }

        void reset_copy(struct player p) {
            p.score = p.lives = 0;
            p.x = p.y = 0;
            save(p);
        }

        void respawn(struct player *p) {
            p.x = p.y = 0;
            p.lives = 3;
        }
    """),
    target=text("""
        void reset(struct player *p) {
            p->score = p->lives = 0;
            p->x = p->y = 0;
        }

        void reset_copy(struct player p) {
            p.score = p.lives = 0;
            p.x = p.y = 0;
            save(p);
        }

        void respawn(struct player *p) {
            p->x = p->y = 0;
            p->lives = 3;
        }
    """),
    hint="Fix reset() with a count before : (a dot is \\. in a pattern). Then go down to respawn() and "
         "repeat the same substitute there: & repeats the last :s, and a count in front of it gives it a "
         "range, just like a count before :.",
    uses=["subst", "amp"],
)
rng.add(
    title="Light up the tree", par=12, ext="c", cursor=(13, 5), setup=OWN_FILE_ONLY,
    task="Hang lights on the tree: in tree[] only, every o becomes @. The owl and the snowman keep their "
         "eyes. The cursor is in the middle of the tree.",
    start=text("""
        static const char *owl[] = {
            " ,_, ",
            "(o,o)",
            "(   )",
            " - - ",
        };
        static const char *tree[] = {
            "     *     ",
            "     ^     ",
            "    o^o    ",
            "   ^^o^^   ",
            "  o^^^^^o  ",
            "     ^     ",
            "    ^o^    ",
            "   o^^^o   ",
            "  ^^o^o^^  ",
            " o^^^^^^^o ",
            "    |||    ",
        };
        static const char *snowman[] = {
            "  _===_  ",
            "  (o.o)  ",
            " ( : : ) ",
            "(___:___)",
        };
    """),
    target=text("""
        static const char *owl[] = {
            " ,_, ",
            "(o,o)",
            "(   )",
            " - - ",
        };
        static const char *tree[] = {
            "     *     ",
            "     ^     ",
            "    @^@    ",
            "   ^^@^^   ",
            "  @^^^^^@  ",
            "     ^     ",
            "    ^@^    ",
            "   @^^^@   ",
            "  ^^@^@^^  ",
            " @^^^^^^^@ ",
            "    |||    ",
        };
        static const char *snowman[] = {
            "  _===_  ",
            "  (o.o)  ",
            " ( : : ) ",
            "(___:___)",
        };
    """),
    hint="Eleven rows is a lot to count. vi{ selects the lines inside the braces around the cursor, and : "
         "turns the selection into a range. Some rows have two lights.",
    uses=["subst", "visual", "brace"],
)
rng.add(
    title="Staging is not production", par=19, ext="yaml", setup=OWN_FILE_ONLY,
    task="The staging block was copied from production. In staging (lines 7 to 11), change every prod to "
         "staging. Production stays as it is.",
    start=text("""
        production:
          api: https://api.prod.example.com
          auth: https://auth.prod.example.com
          cdn: https://cdn.prod.example.com
          db: postgres://db.prod.example.com/shop

        staging:
          api: https://api.prod.example.com
          auth: https://auth.prod.example.com
          cdn: https://cdn.prod.example.com
          db: postgres://db.prod.example.com/shop
    """),
    target=text("""
        production:
          api: https://api.prod.example.com
          auth: https://auth.prod.example.com
          cdn: https://cdn.prod.example.com
          db: postgres://db.prod.example.com/shop

        staging:
          api: https://api.staging.example.com
          auth: https://auth.staging.example.com
          cdn: https://cdn.staging.example.com
          db: postgres://db.staging.example.com/shop
    """),
    hint="The block to change runs to the end of the file, and $ in a range is the last line. Each line has "
         "one prod.",
    uses=["subst"],
)
rng.add(
    title="Urgent goes first", par=5, ext="md", cursor=(4, 1), setup=OWN_FILE_ONLY,
    task="Move the three URGENT items to the top of the list, in the same order. The cursor is on the first "
         "of them, line 4.",
    start=text("""
        - [ ] write the changelog
        - [ ] update the screenshots
        - [ ] answer the issue about Windows
        - [ ] URGENT fix the login crash
        - [ ] URGENT rotate the leaked key
        - [ ] URGENT restore the backups
        - [ ] someday: learn Rust
    """),
    target=text("""
        - [ ] URGENT fix the login crash
        - [ ] URGENT rotate the leaked key
        - [ ] URGENT restore the backups
        - [ ] write the changelog
        - [ ] update the screenshots
        - [ ] answer the issue about Windows
        - [ ] someday: learn Rust
    """),
    hint=":m0 moves a line to the top. A count before : gives it more lines to move, all in one go.",
    uses=["copy-move"],
)
rng.add(
    title="Lines above the cursor", par=11, ext="sh", cursor=(9, 1), setup=OWN_FILE_ONLY,
    task="The smoke tests must use https: change http:// to https:// on the four production curl lines, 4 "
         "to 7. BASE on line 2 is the local server and stays http. The cursor is on the last line.",
    start=text("""
        #!/bin/sh
        BASE=http://localhost:8080
        # smoke tests against production
        curl -fsS http://shop.example.com/health
        curl -fsS http://shop.example.com/api/v1/ping
        curl -fsS -X POST http://shop.example.com/api/v1/echo -d hi
        curl -fsS http://cdn.example.com/logo.png -o /dev/null
        # and against the local server
        curl -fsS "$BASE/health"
    """),
    target=text("""
        #!/bin/sh
        BASE=http://localhost:8080
        # smoke tests against production
        curl -fsS https://shop.example.com/health
        curl -fsS https://shop.example.com/api/v1/ping
        curl -fsS -X POST https://shop.example.com/api/v1/echo -d hi
        curl -fsS https://cdn.example.com/logo.png -o /dev/null
        # and against the local server
        curl -fsS "$BASE/health"
    """),
    hint="The relative numbers say how far up line 4 is. Go there, and a count before : covers the four "
         "lines. Look at where the first colon on each of them is.",
    uses=["subst"],
)
rng.add(
    title="Sort under the header", par=8, ext="csv", setup=OWN_FILE_ONLY,
    task="Sort the users by name. The header stays on line 1.",
    start=text("""
        name,email,joined
        linus,linus@example.com,2021
        ada,ada@example.com,2019
        grace,grace@example.com,2020
        ken,ken@example.com,2023
        barbara,barbara@example.com,2022
        dennis,dennis@example.com,2019
        margaret,margaret@example.com,2024
        alan,alan@example.com,2018
    """),
    target=text("""
        name,email,joined
        ada,ada@example.com,2019
        alan,alan@example.com,2018
        barbara,barbara@example.com,2022
        dennis,dennis@example.com,2019
        grace,grace@example.com,2020
        ken,ken@example.com,2023
        linus,linus@example.com,2021
        margaret,margaret@example.com,2024
    """),
    hint="A plain :sort would put name after margaret. Give it a range from line 2 to the last line.",
    uses=["sort"],
)
rng.add(
    title="A test block from the dev block", par=17, ext="yaml", setup=OWN_FILE_ONLY,
    task="Add a test block below the dev block: the same four lines, with test in place of every dev.",
    start=text("""
        dev:
          url: http://dev.local:8080
          db: shop_dev
          user: dev
    """),
    target=text("""
        dev:
          url: http://dev.local:8080
          db: shop_dev
          user: dev
        test:
          url: http://test.local:8080
          db: shop_test
          user: test
    """),
    hint="Copy the block to the end first. A linewise put leaves the cursor on the first line it put, so a "
         "count before : from there covers the copy and nothing else.",
    uses=["subst", "y", "gg", "p"],
)
rng.add(
    title="Real NULLs", par=18, ext="sql", setup=OWN_FILE_ONLY,
    task="In the first INSERT, the string 'NULL' should be a real NULL, without quotes. In the second "
         "INSERT, 'NULL' is somebody's actual name, and stays.",
    start=text("""
        INSERT INTO users (id, name, email, phone) VALUES
            (1, 'ada', 'ada@example.com', 'NULL'),
            (2, 'alan', 'NULL', 'NULL'),
            (3, 'grace', 'grace@example.com', '555-0100'),
            (4, 'linus', 'NULL', 'NULL');
        -- yes, really
        INSERT INTO users (id, name, email, phone) VALUES
            (5, 'NULL', 'mr.null@example.com', '555-0199');
    """),
    target=text("""
        INSERT INTO users (id, name, email, phone) VALUES
            (1, 'ada', 'ada@example.com', NULL),
            (2, 'alan', NULL, NULL),
            (3, 'grace', 'grace@example.com', '555-0100'),
            (4, 'linus', NULL, NULL);
        -- yes, really
        INSERT INTO users (id, name, email, phone) VALUES
            (5, 'NULL', 'mr.null@example.com', '555-0199');
    """),
    hint="A count before : covers the first INSERT, and the lines without a match are skipped. Two rows "
         "have two NULLs.",
    uses=["subst"],
)
rng.add(
    title="Drop the commented-out settings", par=11, ext="js", cursor=(9, 5), setup=OWN_FILE_ONLY,
    task="Inside the config object, delete every line that's a // comment. The comments outside the braces "
         "stay. The cursor is inside the object, on line 9.",
    start=text("""
        // defaults, see docs/config.md
        const config = {
            port: 8080,
            // port: 3000,
            host: "0.0.0.0",
            // host: "localhost",
            root: "./public",
            logLevel: "info",
            // logLevel: "debug",
            cache: true,
            // cache: false,
            retries: 3,
            // retries: 0,
            timeout: 30,
        };
        export default config; // the tests import it too
        export function load(path) {
            // TODO: validate the file
            return { ...config, ...read(path) };
        }
    """),
    target=text("""
        // defaults, see docs/config.md
        const config = {
            port: 8080,
            host: "0.0.0.0",
            root: "./public",
            logLevel: "info",
            cache: true,
            retries: 3,
            timeout: 30,
        };
        export default config; // the tests import it too
        export function load(path) {
            // TODO: validate the file
            return { ...config, ...read(path) };
        }
    """),
    hint=":g takes a range like any other Ex command, and vi{ followed by : gives it the lines inside the "
         "braces. ./public has a slash too, so the pattern needs both of them.",
    uses=["global", "visual", "brace"],
)
rng.add(
    title="Quote the names", par=16, ext="sql", setup=OWN_FILE_ONLY,
    task="The city names and country codes are strings: quote every word in the four rows, as in "
         "(1, 'Paris', 'FR', 2102650). Line 1 and the comment stay as they are.",
    start=text("""
        INSERT INTO cities (id, name, country, population) VALUES
            (1, Paris, FR, 2102650),
            (2, Berlin, DE, 3850809),
            (3, Madrid, ES, 3332035),
            (4, Rome, IT, 2746984);
        -- source: national statistics offices, 2024
    """),
    target=text("""
        INSERT INTO cities (id, name, country, population) VALUES
            (1, 'Paris', 'FR', 2102650),
            (2, 'Berlin', 'DE', 3850809),
            (3, 'Madrid', 'ES', 3332035),
            (4, 'Rome', 'IT', 2746984);
        -- source: national statistics offices, 2024
    """),
    hint="\\a\\+ matches a run of letters, and digits aren't letters. & puts the match back between quotes. "
         "Go down to the first row and give :s a count for the four of them.",
    uses=["subst"],
)
rng.add(
    title="Tidy the Unreleased section", par=16, ext="md", setup=OWN_FILE_ONLY,
    task="In the Unreleased section only (lines 4 to 8): sort the entries, so the Adds, Fixes and Removes "
         "are together, and change the * bullets to -. The 1.2.0 section stays as it is.",
    start=text("""
        # Changelog

        ## Unreleased
        * Fix the crash on empty input
        * Add --json output
        * Remove the deprecated --raw flag
        * Add shell completions
        * Fix a typo in --help

        ## 1.2.0
        * Add the init command
        * Fix Windows paths
    """),
    target=text("""
        # Changelog

        ## Unreleased
        - Add --json output
        - Add shell completions
        - Fix a typo in --help
        - Fix the crash on empty input
        - Remove the deprecated --raw flag

        ## 1.2.0
        * Add the init command
        * Fix Windows paths
    """),
    hint="Two Ex commands with the same five lines as their range. Go to line 4 first, and a count before "
         ": does the rest. :sort leaves the cursor on the first line it sorted.",
    uses=["sort", "subst", "gg"],
)

# ---------- :g ----------

glob = drills.command(
    "global", ":g/pat/cmd", "run a command on every matching line",
    """:g/pat/cmd runs the Ex command cmd on every line that contains a match for pat. With no range it
    covers the whole file. It works in two passes: first it marks every matching line, then it runs the
    command on each marked line in turn, top to bottom, with the cursor on that line. The command is often
    d (delete), s (substitute; an empty pattern reuses pat), t or m (copy or move), or normal (keys). A
    range after the pattern is relative to each matching line: :g/start/,/end/d deletes from every start
    line to the next end. :g/^/m0 reverses the file, because each line in turn moves to the top.""",
    examples=[(":g/TODO/d", "delete every line with TODO"), (":g/ada/s/ ]/x]", "substitute on matching lines"),
              (":g/pat/norm A;", "Normal keys on matching lines"), (":g/TODO/t$", "copy them to the end"),
              (":g/^/m0", "reverse the file"), (":g/#if/,/#end/d", "delete from each #if to its #end")],
)
glob.add(
    title="Remove the debugger", par=9, ext="py", setup=OWN_FILE_ONLY,
    task="Delete every line that mentions pdb, the import included.",
    start=text("""
        import json
        import pdb

        def update(db, rows, page_size):
            pdb.set_trace()
            for row in rows:
                pdb.set_trace()
                db.save(json.dumps(row))
            pdb.set_trace()
            db.commit()
    """),
    target=text("""
        import json

        def update(db, rows, page_size):
            for row in rows:
                db.save(json.dumps(row))
            db.commit()
    """),
    hint=":g/pattern/d deletes every line that matches the pattern.",
)
glob.add(
    title="Strip the comments", par=8, ext="conf", setup=OWN_FILE_ONLY,
    task="Delete the comment lines (the ones starting with #). The colors keep their # signs.",
    start=text("""
        # server
        port = 8080
        host = 0.0.0.0
        # colors: hex, with the leading #
        accent = #ff8800
        background = #1e1e2e
        # off, info or debug
        log_level = info
        # seconds
        timeout = 30
    """),
    target=text("""
        port = 8080
        host = 0.0.0.0
        accent = #ff8800
        background = #1e1e2e
        log_level = info
        timeout = 30
    """),
    hint="A bare # would also match the color lines. ^ anchors a pattern to the start of the line.",
)
glob.add(
    title="Tick off Ada's tasks", par=15, ext="md", setup=OWN_FILE_ONLY,
    task="Ada finished her tasks: on every line ending in @ada, change [ ] to [x].",
    start=text("""
        - [ ] write the parser @ada
        - [ ] read the spec @alan
        - [ ] fix the tokenizer @ada
        - [ ] update the docs @grace
        - [ ] add a lexer test @linda
        - [ ] release 1.0 @ada
    """),
    target=text("""
        - [x] write the parser @ada
        - [ ] read the spec @alan
        - [x] fix the tokenizer @ada
        - [ ] update the docs @grace
        - [ ] add a lexer test @linda
        - [x] release 1.0 @ada
    """),
    hint="The command after :g/pattern/ can be any Ex command, :s included: :g/ada/s/old/new/ substitutes "
         "only on Ada's lines. The space before ] is what has to change.",
    uses=["subst"],
)
glob.add(
    title="Python 3 exceptions", par=20, ext="py", setup=OWN_FILE_ONLY,
    task="Port the Python 2 raise statements: raise ValueError, \"msg\" becomes raise ValueError(\"msg\").",
    start=text("""
        def ship(order, stock):
            if order.is_empty():
                raise ValueError, "empty order"
            for sku, qty in order.items:
                if qty > stock.get(sku, 0):
                    raise KeyError, "out of stock: " + sku
            try:
                order.charge(use_credit=False)
            except PaymentError:
                raise RuntimeError, "payment failed"
            log("paid, tracking", order.id, "on the way")
            return order
    """),
    target=text("""
        def ship(order, stock):
            if order.is_empty():
                raise ValueError("empty order")
            for sku, qty in order.items:
                if qty > stock.get(sku, 0):
                    raise KeyError("out of stock: " + sku)
            try:
                order.charge(use_credit=False)
            except PaymentError:
                raise RuntimeError("payment failed")
            log("paid, tracking", order.id, "on the way")
            return order
    """),
    hint="On one raise line you'd type f,xr(A): find the comma, delete it, replace the space with (, append ). "
         ":g/pattern/norm runs those keys on every matching line, starting at the beginning of each.",
    uses=["normal", "f", "x", "r", "insert"],
)
glob.add(
    title="Newest first", par=8, ext="txt", setup=OWN_FILE_ONLY,
    task="This is git log --reverse: oldest commit first. Reverse the lines so the newest comes first.",
    start=text("""
        a1f3c2e initial commit
        9b0e7d1 add the parser
        4c2d8f0 fix an off-by-one in the lexer
        e7a1b9c add tests
        0d5f3a2 release 1.0
    """),
    target=text("""
        0d5f3a2 release 1.0
        e7a1b9c add tests
        4c2d8f0 fix an off-by-one in the lexer
        9b0e7d1 add the parser
        a1f3c2e initial commit
    """),
    hint="^ matches every line. :m0 moves a line to the top, and :g handles the lines from the top down. "
         "What happens if each line in turn moves to the top?",
    uses=["copy-move"],
)
glob.add(
    title="Collect the TODOs", par=11, ext="txt", setup=OWN_FILE_ONLY,
    task="Copy every TODO line to the end of the notes, keeping their order, so they can go into the "
         "tracker. The originals stay where they are.",
    start=text("""
        ## Standup, Tuesday
        DONE   ODOO import script
        TODO   fix the flaky test
        TODAY  demo for the PROTO team
        TODO   update the docs
        UNDO   the bad migration
        TODO   book a room
    """),
    target=text("""
        ## Standup, Tuesday
        DONE   ODOO import script
        TODO   fix the flaky test
        TODAY  demo for the PROTO team
        TODO   update the docs
        UNDO   the bad migration
        TODO   book a room
        TODO   fix the flaky test
        TODO   update the docs
        TODO   book a room
    """),
    hint=":t copies a line, and $ means after the last line. :g runs :t$ on each matching line from the top "
         "down, so the copies keep their order.",
    uses=["copy-move"],
)
glob.add(
    title="Done goes last", par=9, ext="txt", setup=OWN_FILE_ONLY,
    task="In this todo.txt, finished tasks start with x. Move them to the bottom, in the same order.",
    start=text("""
        x buy milk
        fix the leaky tap
        x renew passport
        book flights
        x pay rent
        email the landlord
    """),
    target=text("""
        fix the leaky tap
        book flights
        email the landlord
        x buy milk
        x renew passport
        x pay rent
    """),
    hint="x alone also matches \"fix\": anchor it with ^. :m$ moves a line to the end, and since :g goes from "
         "the top down, the moved lines stay in order.",
    uses=["copy-move"],
)
glob.add(
    title="Delete the debug blocks", par=12, ext="c", setup=OWN_FILE_ONLY,
    task="Delete every #ifdef DEBUG block, from the #ifdef line through its #endif. The blocks have "
         "different lengths.",
    start=text("""
        #include <assert.h>
        #include <stdio.h>

        int sum(const int *a, int n) {
            int s = 0;
        #ifdef DEBUG
            fprintf(stderr, "sum of %d items\\n", n);
        #endif /* DEBUG */
            for (int i = 0; i < n; i++) {
        #ifdef DEBUG
                assert(a[i] >= 0);
                fprintf(stderr, "a[%d] = %d\\n", i, a[i]);
        #endif /* DEBUG */
                s += a[i];
            }
        #ifdef DEBUG
            fprintf(stderr, "total %d\\n", s);
        #endif /* DEBUG */
            return s;
        }
    """),
    target=text("""
        #include <assert.h>
        #include <stdio.h>

        int sum(const int *a, int n) {
            int s = 0;
            for (int i = 0; i < n; i++) {
                s += a[i];
            }
            return s;
        }
    """),
    hint="The command after :g/pattern/ can have its own range, counted from each matching line: "
         ",/pat2/d deletes from that line to the next line matching pat2. The first pattern must not match "
         "the #include lines.",
    uses=["range"],
)
glob.add(
    title="Twice as tall", par=8, ext="txt", setup=OWN_FILE_ONLY,
    task="Stretch the heart to twice its height: every line appears twice in a row.",
    start=text("""
         ## ##
        #######
         #####
          ###
           #
    """),
    target=text("""
         ## ##
         ## ##
        #######
        #######
         #####
         #####
          ###
          ###
           #
           #
    """),
    hint=":t. copies the cursor line to just below itself. :g/^/ runs a command on every line.",
    uses=["copy-move"],
)
glob.add(
    title="Reverse just the teardown", par=9, ext="py", cursor=(8, 1), setup=OWN_FILE_ONLY,
    task="Teardown must undo the setup in reverse order. Reverse lines 8 to 11 (the cursor is on the first "
         "of them) and leave setup() alone.",
    start=text("""
        def setup():
            db.connect()
            cache.start()
            queue.open()
            server.listen()

        def teardown():
            db.close()
            cache.stop()
            queue.close()
            server.shutdown()
    """),
    target=text("""
        def setup():
            db.connect()
            cache.start()
            queue.open()
            server.listen()

        def teardown():
            server.shutdown()
            queue.close()
            cache.stop()
            db.close()
    """),
    hint=":g/^/m0 reverses a whole file. Give :g a range (a count before : works) and move each line to "
         "just below line 7 instead of to the top.",
    uses=["range", "copy-move"],
)
glob.add(
    title="No more HTML comments", par=8, ext="md", setup=OWN_FILE_ONLY,
    task="This README was converted from HTML, and the old comments came along. Delete every <!-- --> "
         "comment line.",
    start=text("""
        <!-- generated by html2md -->
        # tinyhttp
        <!-- badges -->
        A tiny, dependency-free web server. Fast!
        <!-- TODO: screenshot -->

        ## Install
        brew install tinyhttp
        <!-- end install -->

        ## Usage
        tinyhttp serve ./public --port 8080
        <!-- see docs/flags.md -->
        - serves static files
        - press <kbd>Ctrl-C</kbd> to stop
    """),
    target=text("""
        # tinyhttp
        A tiny, dependency-free web server. Fast!

        ## Install
        brew install tinyhttp

        ## Usage
        tinyhttp serve ./public --port 8080
        - serves static files
        - press <kbd>Ctrl-C</kbd> to stop
    """),
    hint=":g/pattern/d deletes the matching lines. Every comment starts with <!, and the ! in Fast! is why "
         "the < matters.",
)
glob.add(
    title="Labels and values", par=7, ext="txt", setup=OWN_FILE_ONLY,
    task="The export put every value on the line below its label. Join each pair: Name: on its own line, "
         "then Ada Lovelace, becomes Name: Ada Lovelace.",
    start=text("""
        Name:
        Ada Lovelace
        Born:
        10 December 1815
        Known for:
        the first published program
        Web:
        https://en.wikipedia.org/wiki/Ada_Lovelace
        Languages:
        English, French
    """),
    target=text("""
        Name: Ada Lovelace
        Born: 10 December 1815
        Known for: the first published program
        Web: https://en.wikipedia.org/wiki/Ada_Lovelace
        Languages: English, French
    """),
    hint="The command after :g/pattern/ can be :j, which joins a line with the next one and puts a space "
         "between them, like J. Every label has a colon. What happens to a value line that has one too?",
)
glob.add(
    title="Comments above, not below", par=8, ext="sh", setup=OWN_FILE_ONLY,
    task="In this .env file each comment describes the setting above it. The team wants them above: move "
         "every comment line up one, above its setting.",
    start=text("""
        PORT=8080
        # the port the web server listens on
        WORKERS=4
        # one per CPU core
        ACCENT=#ff8800
        # brand orange, for the header
        LOG_LEVEL=info
        # off, info or debug
    """),
    target=text("""
        # the port the web server listens on
        PORT=8080
        # one per CPU core
        WORKERS=4
        # brand orange, for the header
        ACCENT=#ff8800
        # off, info or debug
        LOG_LEVEL=info
    """),
    hint="Moving each comment up one is the same as moving each setting down one, below its comment. :m+ "
         "moves a line below the next one. Which character do only the settings have?",
    uses=["copy-move"],
)
glob.add(
    title="Braces on the same line", par=8, ext="java", setup=OWN_FILE_ONLY,
    task="The style guide changed: an opening brace goes at the end of the line before it, not on a line of "
         "its own. Fix every {.",
    start=text("""
        public class App
        {
            public static void main(String[] args)
            {
                if (args.length == 0)
                {
                    usage();
                }
                for (String a : args)
                {
                    run(a);
                }
            }
        }
    """),
    target=text("""
        public class App {
            public static void main(String[] args) {
                if (args.length == 0) {
                    usage();
                }
                for (String a : args) {
                    run(a);
                }
            }
        }
    """),
    hint="Like J, :j joins a line with the next one, drops the next one's indentation and puts a space in "
         "between. Give it the range - (the line above), and run it from every { line.",
    uses=["range"],
)
glob.add(
    title="Subtitles to a transcript", par=9, ext="srt", setup=OWN_FILE_ONLY,
    task="Turn the subtitles into a transcript: delete every cue number and every timing line. Keep the "
         "text, and the blank lines between cues.",
    start=text("""
        1
        00:00:01,000 --> 00:00:03,500
        Where are we?

        2
        00:00:04,000 --> 00:00:06,000
        3 days from the coast.

        3
        00:00:06,500 --> 00:00:09,000
        Then we walk.
    """),
    target=text("""
        Where are we?

        3 days from the coast.

        Then we walk.
    """),
    hint="Each cue number sits on the line just above a timing line. The command after :g/pattern/ can have "
         "a range relative to the matching line, like -,. for the line above and this one.",
    uses=["range"],
)
glob.add(
    title="Delete the skipped tests", par=10, ext="py", setup=OWN_FILE_ONLY,
    task="Nobody is going to fix the skipped tests. Delete each one: its @pytest.mark.skip line, the "
         "function, and the two blank lines after it.",
    start=text("""
        import pytest


        @pytest.mark.skip
        def test_upload():
            client.upload("big.zip")
            assert client.ok


        def test_login():
            assert login("ada", "pw")


        @pytest.mark.skip
        def test_refund():
            order.refund()
            assert order.refunded


        def test_disk_full():
            assert not disk.full()
    """),
    target=text("""
        import pytest


        def test_login():
            assert login("ada", "pw")


        def test_disk_full():
            assert not disk.full()
    """),
    hint="Every skipped test is six lines long, counting the blank lines after it. A range like ,+5 after "
         ":g/pattern/ starts at each matching line.",
    uses=["range"],
)
glob.add(
    title="Comment out the prints", par=15, ext="lua", setup=OWN_FILE_ONLY,
    task="Comment out every line that calls print. Leave the rest of the config as it is.",
    start=text("""
        local opts = { number = true, relativenumber = true }
        print("loading options")
        for k, v in pairs(opts) do
            vim.opt[k] = v
            print("set", k, v)
        end
        print(vim.inspect(opts))
        vim.keymap.set("n", "<leader>w", "<cmd>write<cr>")
        print("keymaps done")
        vim.cmd.colorscheme("catppuccin")
        print("colors done")
        vim.opt.clipboard = "unnamedplus"
        print("all done")
    """),
    target=text("""
        local opts = { number = true, relativenumber = true }
        -- print("loading options")
        for k, v in pairs(opts) do
            vim.opt[k] = v
            -- print("set", k, v)
        end
        -- print(vim.inspect(opts))
        vim.keymap.set("n", "<leader>w", "<cmd>write<cr>")
        -- print("keymaps done")
        vim.cmd.colorscheme("catppuccin")
        -- print("colors done")
        vim.opt.clipboard = "unnamedplus"
        -- print("all done")
    """),
    hint="gcc comments out one line. :g/pattern/norm runs Normal-mode keys on every matching line, and "
         ":normal uses mappings, so gcc works there.",
    uses=["normal", "comment"],
)
glob.add(
    title="A line for the translators", par=15, ext="yaml", setup=OWN_FILE_ONLY,
    task="Under every en: line, add a fr: line for the translators to fill in: a copy of the en line, with "
         "fr in place of en.",
    start=text("""
        greeting:
          en: Hello
        welcome:
          en: Good evening
        farewell:
          en: Goodbye
        thanks:
          en: Thank you
    """),
    target=text("""
        greeting:
          en: Hello
          fr: Hello
        welcome:
          en: Good evening
          fr: Good evening
        farewell:
          en: Goodbye
          fr: Goodbye
        thanks:
          en: Thank you
          fr: Thank you
    """),
    hint="The command after :g/pattern/ can be several commands joined with |, and they run one after "
         "another on each matching line. :t. leaves the cursor on the copy. :g sets the search pattern, so "
         "an empty :s pattern means the same one.",
    uses=["copy-move", "subst"],
)
glob.add(
    title="Action items", par=23, ext="md", setup=OWN_FILE_ONLY,
    task="Collect the TODOs at the end, under ## Action items: each one becomes a line like - [ ] write the "
         "docs, in the order they appear. The notes themselves stay as they are.",
    start=text("""
        # Standup, 3 March

        DONE: the parser, the lexer and the REPL.
        Ada: TODO: write the docs
        Alan: TODAY: fixing the flaky test.
        Grace: TODO: ask ops for a VM
        Linus: reviewed the lexer: looks good.
        Ken: TODO: book a room for Friday

        ## Action items
    """),
    target=text("""
        # Standup, 3 March

        DONE: the parser, the lexer and the REPL.
        Ada: TODO: write the docs
        Alan: TODAY: fixing the flaky test.
        Grace: TODO: ask ops for a VM
        Linus: reviewed the lexer: looks good.
        Ken: TODO: book a room for Friday

        ## Action items
        - [ ] write the docs
        - [ ] ask ops for a VM
        - [ ] book a room for Friday
    """),
    hint=":t$ copies a line to the end and leaves the cursor on the copy, so a :s after a | changes the "
         "copy. .* is greedy, so .*: runs to the last colon on the line.",
    uses=["copy-move", "subst"],
)
glob.add(
    title="The down migration", par=27, ext="sql", setup=OWN_FILE_ONLY,
    task="Write the down migration: under -- down, a DROP TABLE for every table, in reverse order (items "
         "first), as in DROP TABLE items;.",
    start=text("""
        CREATE TABLE users (id INT PRIMARY KEY, email TEXT);
        CREATE TABLE orders (id INT PRIMARY KEY, user_id INT);
        CREATE TABLE items (id INT PRIMARY KEY, order_id INT);
        -- down
    """),
    target=text("""
        CREATE TABLE users (id INT PRIMARY KEY, email TEXT);
        CREATE TABLE orders (id INT PRIMARY KEY, user_id INT);
        CREATE TABLE items (id INT PRIMARY KEY, order_id INT);
        -- down
        DROP TABLE items;
        DROP TABLE orders;
        DROP TABLE users;
    """),
    hint="Copying each CREATE line to just below -- down (line 4) reverses them, as each copy lands above "
         "the ones before it. Then fix the copy where :t left the cursor: :normal can follow the :t after a "
         "|, with Ctrl-v <Esc> to leave Insert mode in the middle.",
    uses=["copy-move", "normal", "c", "word", "t", "literal"],
)

# ---------- :normal ----------

norm = drills.command(
    "normal", ":normal {keys}", "Normal-mode keys on many lines",
    """:normal (short: :norm) types the rest of the line as Normal-mode keys. With a range it runs once per
    line, with the cursor at the start (column 1) of each, so :%norm A; appends a ; to every line. If the
    keys leave Insert mode or a command unfinished, :normal ends it as if you pressed <Esc>, so an insert
    at the end needs no <Esc>. A key that would act on the command line itself, like <Esc> or Ctrl-a,
    goes in with Ctrl-v first: Ctrl-v <Esc> shows as ^[. If the keys fail on a line, :normal skips the
    rest of that line and carries on with the next. It uses your mappings (gcc works); :normal! ignores
    them.""",
    examples=[(":%norm A;", "append ; to every line"), (":5,9norm I// ", "insert at each first non-blank"),
              (":%norm f r(A)", "several edits per line"), (":g/x/norm gcc", "toggle a comment on matching lines"),
              (":%norm Ctrl-v Ctrl-a", "Ctrl-v puts a Ctrl-a in the keys"), ("vip:norm .", "repeat the last change on each line")],
)
norm.add(
    title="Capitalize the names", par=11, ext="txt", setup=OWN_FILE_ONLY,
    task="Capitalize every first and last name in both teams.",
    start=text("""
        ada lovelace
        grace hopper

        alan turing
        linus torvalds
        barbara liskov
    """),
    target=text("""
        Ada Lovelace
        Grace Hopper

        Alan Turing
        Linus Torvalds
        Barbara Liskov
    """),
    hint="On one line you'd type ~w~. :%norm types the same keys on every line. On the blank line ~ fails, "
         "and :normal just goes on to the next line.",
    uses=["case", "word"],
)
norm.add(
    title="Python 3 prints", par=14, ext="py", cursor=(3, 1), setup=OWN_FILE_ONLY,
    task="Port the prints to Python 3: print \"x\" becomes print(\"x\"). The cursor starts on line 3.",
    start=text("""
        print "Usage: wc.py [-l] FILE"
        print "Counts lines, words and bytes."
        print "Options:"
        print "  -l  only count lines"
        print "  -h  show this help"
    """),
    target=text("""
        print("Usage: wc.py [-l] FILE")
        print("Counts lines, words and bytes.")
        print("Options:")
        print("  -l  only count lines")
        print("  -h  show this help")
    """),
    hint="f<Space> finds the first space, r( replaces it, and A) appends. :%norm runs those keys on every "
         "line, wherever the cursor is.",
    uses=["f", "r", "insert"],
)
norm.add(
    title="Redact the log", par=21, ext="log", cursor=(3, 1), setup=OWN_FILE_ONLY,
    task="Before sharing the log, replace each message (everything after the level) with [redacted]. The "
         "cursor starts on line 3.",
    start=text("""
        09:14:02 INFO server started on :8080
        09:14:05 ERROR could not open config.yml
        09:16:40 WARN disk 91% full
        09:17:02 ERROR connection refused (db)
        09:17:30 INFO retrying in 5 s
    """),
    target=text("""
        09:14:02 INFO [redacted]
        09:14:05 ERROR [redacted]
        09:16:40 WARN [redacted]
        09:17:02 ERROR [redacted]
        09:17:30 INFO [redacted]
    """),
    hint="From the start of a line, 2W skips the time and the level. C changes to the end of the line. "
         ":normal ends Insert mode for you.",
    uses=["count", "bigword", "c"],
)
norm.add(
    title="Five bonus points", par=12, ext="csv", setup=OWN_FILE_ONLY,
    task="Everyone gets 5 bonus points: add 5 to the score, the last number on each player's line "
         "(name,level,score).",
    start=text("""
        # team red
        ada,3,88
        grace,12,95
        # team blue
        alan,7,100
        linus,10,72
    """),
    target=text("""
        # team red
        ada,3,93
        grace,12,100
        # team blue
        alan,7,105
        linus,10,77
    """),
    hint="On one line: $5 Ctrl-a. On the command line, Ctrl-a means something else, so type Ctrl-v first to "
         "put a real Ctrl-a into the keys. The comment lines have no number, so Ctrl-a fails there and "
         ":normal moves on.",
    uses=["line", "count", "increment", "literal"],
)
norm.add(
    title="Mask the secrets", par=14, ext="sh", cursor=(3, 1), setup=OWN_FILE_ONLY,
    task="Replace every secret value (the first quoted string on each line) with ***. The quoted words in "
         "the comments stay. The cursor starts on line 3.",
    start=text("""
        DB_PASSWORD="hunter2"  # rotated "monthly"
        API_KEY="sk-live-123"
        SMTP_PASS="p@ss"  # from "vault"
        SESSION_SECRET="xyz"
        WEBHOOK_TOKEN="t0k3n"  # see "docs"
    """),
    target=text("""
        DB_PASSWORD="***"  # rotated "monthly"
        API_KEY="***"
        SMTP_PASS="***"  # from "vault"
        SESSION_SECRET="***"
        WEBHOOK_TOKEN="***"  # see "docs"
    """),
    hint="ci\" works even from before the first quote: it changes the first quoted string on the line. "
         "Run it on every line with :%norm.",
    uses=["c", "quote"],
)
norm.add(
    title="From exports to .env", par=18, ext="sh", cursor=(3, 1), setup=OWN_FILE_ONLY,
    task="Turn the shell exports into a .env file: drop export, and put the value after = in double "
         "quotes. The cursor starts on line 3.",
    start=text("""
        export EDITOR=nvim
        export PAGER=less -R
        export LANG=en_US.UTF-8
        export PROJECT_ROOT=~/code/shop
        export GREETING=hello world
    """),
    target=text("""
        EDITOR="nvim"
        PAGER="less -R"
        LANG="en_US.UTF-8"
        PROJECT_ROOT="~/code/shop"
        GREETING="hello world"
    """),
    hint="On one line: dw, then f=a\" and <Esc>, then A\". In :normal, an <Esc> in the middle goes in as "
         "Ctrl-v <Esc>; the one at the very end isn't needed.",
    uses=["d", "word", "f", "insert", "literal"],
)
norm.add(
    title="Swap dev and prod", par=11, ext="py", cursor=(3, 1), setup=OWN_FILE_ONLY,
    task="Toggle every line: the commented-out dev settings become active, and the active prod settings "
         "get commented out. The cursor starts on line 3.",
    start=text("""
        # DB_URL = "sqlite:///dev.db"
        DB_URL = "postgres://db.prod/shop"
        # DEBUG = True
        DEBUG = False
        # CACHE_URL = None
        CACHE_URL = "redis://cache.prod:6379"
    """),
    target=text("""
        DB_URL = "sqlite:///dev.db"
        # DB_URL = "postgres://db.prod/shop"
        DEBUG = True
        # DEBUG = False
        CACHE_URL = None
        # CACHE_URL = "redis://cache.prod:6379"
    """),
    hint="gcc toggles the comment on one line. gc over several lines treats them as a group (it would comment "
         "them all), but :%norm gcc toggles each line on its own.",
    uses=["comment"],
)
norm.add(
    title="Unwrap the str() calls", par=15, ext="py", cursor=(3, 1), setup=OWN_FILE_ONLY,
    task="Drop the str( ) wrapper on every line: total = str(sum(prices)) becomes total = sum(prices). The "
         "cursor starts on line 3.",
    start=text("""
        total = str(sum(prices))
        label = str(item.name)
        count = str(len(items))
        ratio = str(round(done / todo, 2))
        when = str(datetime.now())
    """),
    target=text("""
        total = sum(prices)
        label = item.name
        count = len(items)
        ratio = round(done / todo, 2)
        when = datetime.now()
    """),
    hint="2W jumps to str(, df( deletes through the first (, and the matching ) is the last character on "
         "the line.",
    uses=["count", "bigword", "d", "f", "line", "x"],
)
norm.add(
    title="Keys without quotes", par=16, ext="py", cursor=(3, 5), setup=OWN_FILE_ONLY,
    task="Finish the switch to dict(...): on lines 2 to 5, 'host': 'db.local', becomes host='db.local',. "
         "The cursor starts on line 3.",
    start=text("""
        settings = dict(
            'host': 'db.local',
            'port': 5432,
            'user': 'ada',
            'timeout': 30,
        )
    """),
    target=text("""
        settings = dict(
            host='db.local',
            port=5432,
            user='ada',
            timeout=30,
        )
    """),
    hint="On one line: ^x deletes the opening quote, f' finds the closing one, and 3s= replaces the quote, "
         "colon and space with =. A count before : gives :norm its range.",
    uses=["range", "line", "x", "f", "c", "count"],
)
norm.add(
    title="Inventory to CSV", par=21, ext="csv", cursor=(3, 1), setup=OWN_FILE_ONLY,
    task="Make each line CSV: code,quantity,\"description\". The description can contain spaces, so it gets "
         "double quotes. The cursor starts on line 3.",
    start=text("""
        A12 3 blue widget
        B07 10 red sprocket
        C33 1 large gear box
        D02 25 spring
        E19 4 small brass hinge
    """),
    target=text("""
        A12,3,"blue widget"
        B07,10,"red sprocket"
        C33,1,"large gear box"
        D02,25,"spring"
        E19,4,"small brass hinge"
    """),
    hint="f<Space>r, fixes the first space and ;r, the second (; repeats the f). Then a\", an <Esc> (typed "
         "as Ctrl-v <Esc> on the command line), and A\".",
    uses=["f", "r", "semicolon", "insert", "literal"],
)
norm.add(
    title="A blank translation", par=11, ext="xml", setup=OWN_FILE_ONLY,
    task="This is the start of the French strings file, copied from the English one. Empty every string, "
         "and keep the tags, their names and the comments.",
    start=text("""
        <string name="app_name">Shop</string>
        <!-- account -->
        <string name="login">Log in</string>
        <string name="logout">Log out</string>
        <!-- cart -->
        <string name="cart_empty">Your cart is empty</string>
        <string name="checkout">Check out</string>
        <string name="thanks">Thanks for your order!</string>
    """),
    target=text("""
        <string name="app_name"></string>
        <!-- account -->
        <string name="login"></string>
        <string name="logout"></string>
        <!-- cart -->
        <string name="cart_empty"></string>
        <string name="checkout"></string>
        <string name="thanks"></string>
    """),
    hint="dit deletes the text inside a tag, and from the start of the line it finds the tag on its own. "
         ":%norm runs it on every line, and where it fails, on the comments, :normal just goes on to the next "
         "line.",
    uses=["d", "tag"],
)
norm.add(
    title="Shout the keys", par=11, ext="sh", cursor=(3, 1), setup=OWN_FILE_ONLY,
    task="Environment variables are written in capitals. Uppercase every key, the part before the =, and "
         "leave the values alone. The cursor starts on line 3.",
    start=text("""
        db_host=localhost
        db_port=5432
        api_key=sk-test-123
        log_level=info
        cache_ttl=300
    """),
    target=text("""
        DB_HOST=localhost
        DB_PORT=5432
        API_KEY=sk-test-123
        LOG_LEVEL=info
        CACHE_TTL=300
    """),
    hint="gU takes a motion, and _ is part of a word, so from the start of a line one short motion covers the "
         "whole key.",
    uses=["case", "word"],
)
norm.add(
    title="Empty the lists", par=11, ext="json", cursor=(3, 3), setup=OWN_FILE_ONLY,
    task="A new season starts: empty every list, and keep the keys and the brackets. The cursor starts "
         "on line 3.",
    start=text("""
        {
          "admins": ["ada", "grace"],
          "banned": ["troll42"],
          "invited": ["alan", "linus", "ken"],
          "muted": ["spammer", "bot7"]
        }
    """),
    target=text("""
        {
          "admins": [],
          "banned": [],
          "invited": [],
          "muted": []
        }
    """),
    hint="di[ deletes what's inside square brackets, and finds them even from the start of the line. On the "
         "lines without any, it fails, and :normal goes on.",
    uses=["d", "bracket"],
)
norm.add(
    title="Read the answers", par=13, ext="txt", setup=OWN_FILE_ONLY,
    task="The answers after each | are in ROT13, so you can't read them by accident. Decode all of them. "
         "The riddles stay as they are.",
    start=text("""
        Riddles, week 12

        What has keys but can't open locks? | N cvnab
        What gets wetter the more it dries? | N gbjry

        What has a neck but no head? | N obggyr
        What can you catch but not throw? | N pbyq
    """),
    target=text("""
        Riddles, week 12

        What has keys but can't open locks? | A piano
        What gets wetter the more it dries? | A towel

        What has a neck but no head? | A bottle
        What can you catch but not throw? | A cold
    """),
    hint="g? ROT13s over a motion, and doing it twice undoes it. Find the | and decode to the end of the "
         "line. Inside :normal a | is just another key.",
    uses=["f", "rot13", "line"],
)
norm.add(
    title="Just one underscore", par=12, ext="js", setup=OWN_FILE_ONLY,
    task="Make each variable camelCase: user_name becomes userName. Each name with an underscore has just "
         "one, and the _ in the URL stays.",
    start=text("""
        let user_name = "ada";
        let max_retries = 3;
        const api_url = "https://example.com/api_v2";
        let count = 0;
        let is_admin = false;
        const page_size = 50;
    """),
    target=text("""
        let userName = "ada";
        let maxRetries = 3;
        const apiUrl = "https://example.com/api_v2";
        let count = 0;
        let isAdmin = false;
        const pageSize = 50;
    """),
    hint="On one line: find the _, delete it, and switch the case of the letter that slides under the "
         "cursor. That's three Normal-mode commands.",
    uses=["f", "x", "case"],
)
norm.add(
    title="Patch releases", par=13, ext="json", setup=OWN_FILE_ONLY,
    task="Every package has a security fix out: bump the last number of each version by one, so "
         "4.18.2 becomes 4.18.3.",
    start=text("""
        {
          "dependencies": {
            "express": "4.18.2",
            "lodash": "4.17.21",
            "pg": "8.11.3",
            "zod": "3.22.4"
          },
          "devDependencies": {
            "eslint": "8.56.0",
            "vitest": "1.2.1"
          }
        }
    """),
    target=text("""
        {
          "dependencies": {
            "express": "4.18.3",
            "lodash": "4.17.22",
            "pg": "8.11.4",
            "zod": "3.22.5"
          },
          "devDependencies": {
            "eslint": "8.56.1",
            "vitest": "1.2.2"
          }
        }
    """),
    hint="Ctrl-a adds to the first number at or after the cursor, so get past the first two parts of the "
         "version first: 2f. lands on the second dot. Type Ctrl-v before the Ctrl-a on the command line.",
    uses=["count", "f", "increment", "literal"],
)
norm.add(
    title="Country codes in capitals", par=14, ext="csv", setup=OWN_FILE_ONLY,
    task="The country code is the third field. Write every code in capitals: gb becomes GB. Dennis's "
         "record has no city or country yet.",
    start=text("""
        ada,london,gb,1815
        grace,new york,us,1906
        linus,helsinki,fi,1969
        dennis,1941
        margaret,paoli,us,1936
        ken,new orleans,us,1943
    """),
    target=text("""
        ada,london,GB,1815
        grace,new york,US,1906
        linus,helsinki,FI,1969
        dennis,1941
        margaret,paoli,US,1936
        ken,new orleans,US,1943
    """),
    hint="2f, lands on the comma before the code. From a comma, e goes to the end of the next word, so gUe "
         "uppercases the comma and the code.",
    uses=["count", "f", "case", "word"],
)
norm.add(
    title="CAPS LOCK", par=11, ext="txt", cursor=(3, 1), setup=OWN_FILE_ONLY,
    task="Caps Lock was on for the first word of every line: tHE should be The. Fix the first words. The "
         "cursor starts on line 3.",
    start=text("""
        tHE meeting moved to 3pm.
        pLEASE bring the slides.
        lUNCH is on the team.
        sEE you there!
    """),
    target=text("""
        The meeting moved to 3pm.
        Please bring the slides.
        Lunch is on the team.
        See you there!
    """),
    hint="g~ switches the case of everything a motion covers. From the start of the line, which motion "
         "covers exactly the first word?",
    uses=["case", "word"],
)
norm.add(
    title="From require to import", par=31, ext="js", cursor=(3, 1), setup=OWN_FILE_ONLY,
    task="Move to ES modules: const fs = require('fs'); becomes import fs from 'fs';. The cursor starts "
         "on line 3.",
    start=text("""
        const fs = require('fs');
        const path = require('path');
        const express = require('express');

        const db = require('./db');
        const log = require('./log');
    """),
    target=text("""
        import fs from 'fs';
        import path from 'path';
        import express from 'express';

        import db from './db';
        import log from './log';
    """),
    hint="Three edits per line: const becomes import, \"= require(\" becomes \"from \", and the ) goes. Each "
         "<Esc> in the middle costs a Ctrl-v, so do the edit at the start of the line last: its insert "
         "needs no <Esc> at all. % jumps to the bracket matching the first one on the line.",
    uses=["percent", "x", "f", "c", "line", "word", "literal"],
)
norm.add(
    title="Two seconds later", par=19, ext="srt", setup=OWN_FILE_ONLY,
    task="The subtitles show up two seconds early. Add 2 to the seconds of both times on every timing "
         "line: 00:00:01,000 becomes 00:00:03,000. The cue numbers stay.",
    start=text("""
        1
        00:00:01,000 --> 00:00:03,500
        Where are we?

        2
        00:00:04,000 --> 00:00:06,000
        Three days from the coast.

        3
        00:00:06,500 --> 00:00:09,000
        Then we walk.

        4
        00:00:12,250 --> 00:00:15,000
        Then we swim.
    """),
    target=text("""
        1
        00:00:03,000 --> 00:00:05,500
        Where are we?

        2
        00:00:06,000 --> 00:00:08,000
        Three days from the coast.

        3
        00:00:08,500 --> 00:00:11,000
        Then we walk.

        4
        00:00:14,250 --> 00:00:17,000
        Then we swim.
    """),
    hint="The seconds come after the second colon of each time. 2f: gets there, 2 Ctrl-a adds 2 to the "
         "number after it, and ; repeats the f (it takes a count too). On a line with no colons, f: fails "
         "and :normal skips the rest of that line.",
    uses=["count", "f", "semicolon", "increment", "literal"],
)

# ---------- :t :m ----------

cm = drills.command(
    "copy-move", ":t  :m", "copy and move lines",
    """:t (short for :copy) copies lines and :m (:move) moves them. The address after the command says
    below which line they go: :t. duplicates the cursor line, :t$ copies it to the end, and 0 means
    above the first line, so :m0 moves it to the top. Both take a range in front (:5,8t$ copies lines
    5 to 8 to the end), and numbers can be relative to the cursor (:-3t. copies the line three up to
    just below the cursor). The cursor doesn't have to go anywhere first, and it ends on the last line
    copied or moved. Several Ex commands can share one command line, separated by | (:3t$|1t$).""",
    examples=[(":t.", "duplicate this line"), (":m0", "move this line to the top"), (":t$", "copy it to the end"),
              (":2t.", "copy line 2 below the cursor"), (":5,8t0", "copy lines 5-8 to the top"),
              (":m-2", "move this line up one")],
)
cm.add(
    title="Plain imports first", par=4, ext="py", cursor=(5, 1), setup=OWN_FILE_ONLY,
    task="import argparse belongs at the very top. The cursor is on it (line 5): move it there.",
    start=text("""
        import json
        import os

        from pathlib import Path
        import argparse
    """),
    target=text("""
        import argparse
        import json
        import os

        from pathlib import Path
    """),
    hint=":m moves the cursor line below the line you name, and 0 means \"above line 1\".",
)
cm.add(
    title="Close the box", par=4, ext="txt", cursor=(4, 1), setup=OWN_FILE_ONLY,
    task="The box has no top. Put a copy of its bottom border (the cursor line) above line 1.",
    start=text("""
        | ascii is |
        | art made |
        | of text  |
        +----------+
    """),
    target=text("""
        +----------+
        | ascii is |
        | art made |
        | of text  |
        +----------+
    """),
    hint=":t copies the cursor line; the address after it says where, and 0 is above line 1.",
)
cm.add(
    title="Borrow a line", par=5, ext="java", cursor=(7, 5), setup=OWN_FILE_ONLY,
    task="PaymentService needs the same clock as OrderService. Copy line 2 to just below the cursor line "
         "(line 7, in PaymentService).",
    start=text("""
        class OrderService {
            private final Clock clock = Clock.systemUTC();
            private final Repo repo;
        }

        class PaymentService {
            private final Repo repo;
        }
    """),
    target=text("""
        class OrderService {
            private final Clock clock = Clock.systemUTC();
            private final Repo repo;
        }

        class PaymentService {
            private final Repo repo;
            private final Clock clock = Clock.systemUTC();
        }
    """),
    hint="Put the line to copy in front of t and the place after it: . is the cursor line.",
)
cm.add(
    title="Decorate another one", par=4, ext="py", cursor=(3, 1), setup=OWN_FILE_ONLY,
    task="settings() needs @login_required too. Copy the cursor line (the decorator on line 3) to just "
         "above def settings.",
    start=text("""
        from auth import login_required

        @login_required
        def profile(request):
            return render(request, "profile.html")

        def settings(request):
            return render(request, "settings.html")
    """),
    target=text("""
        from auth import login_required

        @login_required
        def profile(request):
            return render(request, "profile.html")

        @login_required
        def settings(request):
            return render(request, "settings.html")
    """),
    hint="With no range, :t copies the cursor line. The address after it is the line the copy goes below.",
)
cm.add(
    title="Install after testing", par=4, ext="sh", cursor=(2, 1), setup=OWN_FILE_ONLY,
    task="make install should only run after the tests pass. Move the cursor line (make install, line 2) "
         "to just below make test.",
    start=text("""
        git pull
        make install
        ./configure
        make
        make test
        echo "deployed"
    """),
    target=text("""
        git pull
        ./configure
        make
        make test
        make install
        echo "deployed"
    """),
    hint=":m moves the cursor line below the line whose number you give it.",
)
cm.add(
    title="Duplicate the sample rows", par=7, ext="csv", cursor=(5, 1), setup=OWN_FILE_ONLY,
    task="To test duplicate handling, copy rows 2 to 4 to the end of the file.",
    start=text("""
        id,name,role
        1,ada,admin
        2,alan,user
        3,grace,user
        4,linus,user
    """),
    target=text("""
        id,name,role
        1,ada,admin
        2,alan,user
        3,grace,user
        4,linus,user
        1,ada,admin
        2,alan,user
        3,grace,user
    """),
    hint="Give :t a range: :2,4t followed by the line to put them below.",
    uses=["range"],
)
cm.add(
    title="main() goes first", par=7, ext="java", setup=OWN_FILE_ONLY,
    task="Move main() (lines 6 to 8) and the blank line after it to the top of the class, just below "
         "class App {.",
    start=text("""
        class App {
            void run() {
                start();
            }

            public static void main(String[] args) {
                new App().run();
            }

            void stop() {
                halt();
            }
        }
    """),
    target=text("""
        class App {
            public static void main(String[] args) {
                new App().run();
            }

            void run() {
                start();
            }

            void stop() {
                halt();
            }
        }
    """),
    hint=":m takes a range too. Lines 6 to 9 should go below line 1.",
    uses=["range"],
)
cm.add(
    title="Copy, then recolor", par=15, ext="css", cursor=(7, 5), setup=OWN_FILE_ONLY,
    task="The danger button needs a background too: copy line 3 below the cursor line (line 7), then "
         "change the copy's color to #d20f39.",
    start=text("""
        .button {
            color: #ffffff;
            background: #1e66f5;
        }

        .button-danger {
            color: #ffffff;
        }
    """),
    target=text("""
        .button {
            color: #ffffff;
            background: #1e66f5;
        }

        .button-danger {
            color: #ffffff;
            background: #d20f39;
        }
    """),
    hint=":3t. copies line 3 below the cursor and leaves the cursor on the copy, ready to edit. f1 finds "
         "the start of the color, and cw changes it.",
    uses=["f", "c", "word"],
)
cm.add(
    title="Swap two steps", par=10, ext="sh", setup=OWN_FILE_ONLY,
    task="The migration must run while the service is stopped: swap lines 2 and 5.",
    start=text("""
        git pull
        ./migrate.sh
        npm ci
        npm run build
        systemctl stop shop
        systemctl start shop
    """),
    target=text("""
        git pull
        systemctl stop shop
        npm ci
        npm run build
        ./migrate.sh
        systemctl start shop
    """),
    hint="Two :m commands. Moving line 2 below line 5 shifts the lines in between up by one, so the stop "
         "line is then line 4.",
)
cm.add(
    title="Make a playlist", par=13, ext="md", setup=OWN_FILE_ONLY,
    task="Copy yesterday, imagine and wonderwall, in that order, to the end, under ## Playlist.",
    start=text("""
        ## Library
        bohemian rhapsody
        imagine
        hotel california
        yesterday
        wonderwall

        ## Playlist
    """),
    target=text("""
        ## Library
        bohemian rhapsody
        imagine
        hotel california
        yesterday
        wonderwall

        ## Playlist
        yesterday
        imagine
        wonderwall
    """),
    hint=":5t$ copies line 5 to the end, and each copy goes after the previous one. A | lets you put several "
         "commands on one command line.",
)
cm.add(
    title="The shebang goes first", par=5, ext="py", setup=OWN_FILE_ONLY,
    task="The #! line only works as the very first line of a script. Move it (line 6) to the top.",
    start=text("""
        \"\"\"Rename photos by the date they were taken.\"\"\"

        import sys
        from pathlib import Path

        #!/usr/bin/env python3
        def main():
            for p in map(Path, sys.argv[1:]):
                rename(p)
    """),
    target=text("""
        #!/usr/bin/env python3
        \"\"\"Rename photos by the date they were taken.\"\"\"

        import sys
        from pathlib import Path

        def main():
            for p in map(Path, sys.argv[1:]):
                rename(p)
    """),
    hint=":m moves a line, and a number in front says which one, so the cursor doesn't have to go there. 0 "
         "is above line 1.",
)
cm.add(
    title="The same filter", par=5, ext="sql", cursor=(8, 1), setup=OWN_FILE_ONLY,
    task="The orders query must skip deleted rows too. Copy line 3 to just above the cursor line, the "
         "ORDER BY on line 8.",
    start=text("""
        SELECT id, email
        FROM users
        WHERE deleted_at IS NULL
        ORDER BY email;

        SELECT id, total
        FROM orders
        ORDER BY total DESC;
    """),
    target=text("""
        SELECT id, email
        FROM users
        WHERE deleted_at IS NULL
        ORDER BY email;

        SELECT id, total
        FROM orders
        WHERE deleted_at IS NULL
        ORDER BY total DESC;
    """),
    hint=":t puts the copy below the line you name. Above the cursor line is below the line before it, and "
         "- on its own means the line above.",
)
cm.add(
    title="Five lines up", par=6, ext="js", cursor=(17, 5), setup=OWN_FILE_ONLY,
    task="The orders route must not be cached either. Copy the res.set line from the users route (line "
         "12) to just below the cursor line, line 17.",
    start=text("""
        import express from "express";
        import { db } from "./db.js";

        const app = express();

        app.get("/health", (req, res) => {
            res.send("ok");
        });

        app.get("/users/:id", async (req, res) => {
            const user = await db.users.find(req.params.id);
            res.set("Cache-Control", "no-store");
            res.json(user);
        });

        app.get("/orders/:id", async (req, res) => {
            const order = await db.orders.find(req.params.id);
            res.json(order);
        });
    """),
    target=text("""
        import express from "express";
        import { db } from "./db.js";

        const app = express();

        app.get("/health", (req, res) => {
            res.send("ok");
        });

        app.get("/users/:id", async (req, res) => {
            const user = await db.users.find(req.params.id);
            res.set("Cache-Control", "no-store");
            res.json(user);
        });

        app.get("/orders/:id", async (req, res) => {
            const order = await db.orders.find(req.params.id);
            res.set("Cache-Control", "no-store");
            res.json(order);
        });
    """),
    hint="The relative number next to the res.set line says how far up it is, and an address can count from "
         "the cursor: -5 is five lines up.",
)
cm.add(
    title="An import at the bottom", par=5, ext="py", setup=OWN_FILE_ONLY,
    task="Someone added import re at the end of the file. Move it to just below import json, line 3.",
    start=text("""
        import argparse
        import csv
        import json
        import sys

        def main():
            args = parse(sys.argv)
            for row in csv.reader(open(args.file)):
                print(json.dumps(clean(row)))
        import re
    """),
    target=text("""
        import argparse
        import csv
        import json
        import re
        import sys

        def main():
            args = parse(sys.argv)
            for row in csv.reader(open(args.file)):
                print(json.dumps(clean(row)))
    """),
    hint="$ is the last line, as a line to move as well as an address to move to.",
)
cm.add(
    title="A quick start on top", par=7, ext="md", setup=OWN_FILE_ONLY,
    task="Copy the three install commands (lines 6 to 8) to the very top of the README, as a quick start. "
         "The originals stay where they are.",
    start=text("""
        # tinyhttp

        A tiny web server for static sites.

        ## Install
        brew tap ada/tools
        brew install tinyhttp
        tinyhttp --version

        ## Usage
        tinyhttp serve ./public
    """),
    target=text("""
        brew tap ada/tools
        brew install tinyhttp
        tinyhttp --version
        # tinyhttp

        A tiny web server for static sites.

        ## Install
        brew tap ada/tools
        brew install tinyhttp
        tinyhttp --version

        ## Usage
        tinyhttp serve ./public
    """),
    hint=":t takes a range in front, like :m, and 0 is above line 1.",
    uses=["range"],
)
cm.add(
    title="Two stray fields", par=11, ext="java", cursor=(4, 5), setup=OWN_FILE_ONLY,
    task="Two fields were declared at the bottom of the class. Move them, first email (line 14) then "
         "createdAt (line 17), up below the cursor line, line 4, with the other fields.",
    start=text("""
        public class User {
            private final long id;
            private final String name;
            private boolean admin;

            public User(long id, String name) {
                this.id = id;
                this.name = name;
            }

            public String name() {
                return name;
            }
            private String email;

            public boolean isAdmin() { return admin; }
            private Instant createdAt;
        }
    """),
    target=text("""
        public class User {
            private final long id;
            private final String name;
            private boolean admin;
            private String email;
            private Instant createdAt;

            public User(long id, String name) {
                this.id = id;
                this.name = name;
            }

            public String name() {
                return name;
            }

            public boolean isAdmin() { return admin; }
        }
    """),
    hint=":14m. moves line 14 to below the cursor line, and the cursor goes with it, so the next :m. puts "
         "its line below that one. Moving a line up doesn't change the numbers of the lines below where it "
         "was. | joins two commands.",
    uses=["range"],
)
cm.add(
    title="A lighter deploy", par=9, ext="sh", cursor=(8, 1), setup=OWN_FILE_ONLY,
    task="Staging only needs two of the production steps: copy git pull (line 2), then systemctl restart "
         "shop (line 5), into deploy_staging, in that order. The cursor is on its first line.",
    start=text("""
        deploy_prod() {
            git pull
            npm ci
            ./migrate.sh
            systemctl restart shop
        }

        deploy_staging() {
        }
    """),
    target=text("""
        deploy_prod() {
            git pull
            npm ci
            ./migrate.sh
            systemctl restart shop
        }

        deploy_staging() {
            git pull
            systemctl restart shop
        }
    """),
    hint=":t. copies a line below the cursor line, and then the cursor is on the copy. So a second :t. puts "
         "its line below the first one.",
)
cm.add(
    title="Another port", par=10, ext="yaml", cursor=(9, 7), setup=OWN_FILE_ONLY,
    task="The sidecar listens on 9090. Copy the containerPort line from the web container (line 6) below "
         "the cursor line, and make the copy's port 9090.",
    start=text("""
        spec:
          containers:
            - name: web
              image: shop:1.4
              ports:
                - containerPort: 8080
            - name: metrics
              image: prom/statsd-exporter
              ports:
    """),
    target=text("""
        spec:
          containers:
            - name: web
              image: shop:1.4
              ports:
                - containerPort: 8080
            - name: metrics
              image: prom/statsd-exporter
              ports:
                - containerPort: 9090
    """),
    hint="After :6t. the cursor is on the copy. Ctrl-a adds to the first number at or after the cursor, and "
         "it takes a count: what do you add to 8080 to get 9090?",
    uses=["increment", "count"],
)
cm.add(
    title="In the right order", par=8, ext="dockerfile", setup=OWN_FILE_ONLY,
    task="Put the Dockerfile in a working order: FROM, WORKDIR, COPY, RUN, then CMD.",
    start=text("""
        CMD ["node", "server.js"]
        FROM node:20
        COPY . .
        WORKDIR /app
        RUN npm ci
    """),
    target=text("""
        FROM node:20
        WORKDIR /app
        COPY . .
        RUN npm ci
        CMD ["node", "server.js"]
    """),
    hint="Two moves do it: CMD to the end, then WORKDIR up. After the first one the line numbers change. With "
         "no line number in front, :m moves the cursor line.",
)
cm.add(
    title="Questions and answers", par=13, ext="md", setup=OWN_FILE_ONLY,
    task="The flash cards came out as all the questions, then all the answers. Put each answer right after "
         "its question.",
    start=text("""
        Q: What does :t do?
        Q: What does :m0 do?
        Q: What is $ in a range?
        Q: What does :g/^/m0 do?
        A: copies lines
        A: moves a line to the top
        A: the last line
        A: reverses the file
    """),
    target=text("""
        Q: What does :t do?
        A: copies lines
        Q: What does :m0 do?
        A: moves a line to the top
        Q: What is $ in a range?
        A: the last line
        Q: What does :g/^/m0 do?
        A: reverses the file
    """),
    hint="Three :m commands joined with |. Each move changes the order of the lines between, so work out "
         "where the next answer is after the one before. The last answer is already in place.",
)

# ---------- :v ----------

vg = drills.command(
    "vglobal", ":v/pat/cmd", "run a command on every line that doesn't match",
    """:v (short for :vglobal, the same as :g!) is the opposite of :g: it runs the command on every line
    that does NOT match the pattern. :v/pat/d keeps only the lines that match, and :v/./d deletes the
    empty lines, since . matches any character and an empty line has none. Like :g, it covers the whole
    file unless you give it a range, and it marks the lines first, then runs the command on each, top to
    bottom.""",
    examples=[(":v/ERROR/d", "keep only the ERROR lines"), (":v/./d", "delete the empty lines"),
              (":v/=/m$", "move lines without = to the end"), (":g!/pat/d", "the same as :v/pat/d")],
    level="complex",
)
vg.add(
    title="Just the signatures", par=9, ext="py", setup=OWN_FILE_ONLY,
    task="Make an outline of the module: keep only the def lines and delete everything else.",
    start=text("""
        import math
        debug = False

        def area(r):
            return round(math.pi * r ** 2, 2)

        def half(x):
            # rounds toward zero, as before
            return int(x / 2) if x else 0

        def describe(r):
            if area(r):
                print(f"radius {r}: area {area(r)}")
    """),
    target=text("""
        def area(r):
        def half(x):
        def describe(r):
    """),
    hint=":v/pattern/d deletes every line that doesn't match the pattern, so the matching ones are all "
         "that's left.",
)
vg.add(
    title="Close the gaps", par=7, ext="md", setup=OWN_FILE_ONLY,
    task="Delete the empty lines between the items.",
    start=text("""
        - milk

        - eggs

        - flour

        - butter

        - sugar
    """),
    target=text("""
        - milk
        - eggs
        - flour
        - butter
        - sugar
    """),
    hint="In a pattern, . matches any one character. Which lines don't contain any character at all?",
)
vg.add(
    title="Pinned versions first", par=8, ext="txt", setup=OWN_FILE_ONLY,
    task="In this requirements file, move every package without a pinned version (no ==) to the bottom, "
         "keeping the order within each group.",
    start=text("""
        requests==2.31.0
        flask
        numpy==1.26.4
        pytest
        rich==13.7.1
        black
    """),
    target=text("""
        requests==2.31.0
        numpy==1.26.4
        rich==13.7.1
        flask
        pytest
        black
    """),
    hint=":m$ moves a line to the end. :v runs it on the lines that don't match, from the top down, so they "
         "keep their order.",
    uses=["copy-move"],
)
vg.add(
    title="Just the outline", par=8, ext="md", setup=OWN_FILE_ONLY,
    task="Turn the notes into an outline: keep only the heading lines, the ones that start with #.",
    start=text("""
        # Release 1.4
        Ship it on Friday if the tests are green.

        ## Fixes
        The crash from issue #12 is gone.
        Windows paths work again (#31, #40).

        ## New
        A --json flag for every command.
        ### Docs
        The man page is generated now.
    """),
    target=text("""
        # Release 1.4
        ## Fixes
        ## New
        ### Docs
    """),
    hint=":v/pattern/d deletes every line that doesn't match. Some of the other lines have a # too, but not "
         "at the start.",
)
vg.add(
    title="One blank line is enough", par=12, ext="py", setup=OWN_FILE_ONLY,
    task="Wherever there are several blank lines in a row, keep just one. The single blank lines stay.",
    start=text("""
        import os


        def load(path):
            return open(path).read()



        def save(path, text):

            with open(path, "w") as f:
                f.write(text)


        def main():
            save("out.txt", load("in.txt"))
    """),
    target=text("""
        import os

        def load(path):
            return open(path).read()

        def save(path, text):

            with open(path, "w") as f:
                f.write(text)

        def main():
            save("out.txt", load("in.txt"))
    """),
    hint="On each blank line, join it with the blank lines after it: the range ,/./- runs from there to the "
         "line before the next non-blank one, and :j on a range of one line does nothing. :v/./ finds the "
         "blank lines.",
    uses=["range"],
)
vg.add(
    title="Turn it all off", par=13, ext="sh", setup=OWN_FILE_ONLY,
    task="Disable this .bashrc snippet for a while: comment out every line with \"# \" in front. The lines "
         "that are already comments stay as they are.",
    start=text("""
        # aliases
        alias ll='ls -lh'
        alias gs='git status'
        # prompt
        export PS1='\\w $ '
        [ -f ~/.local.sh ] && . ~/.local.sh
        echo "ready" # say hi
    """),
    target=text("""
        # aliases
        # alias ll='ls -lh'
        # alias gs='git status'
        # prompt
        # export PS1='\\w $ '
        # [ -f ~/.local.sh ] && . ~/.local.sh
        # echo "ready" # say hi
    """),
    hint="Like :g, :v can run any Ex command on its lines, :s included, and :s/^/x/ puts x at the start of "
         "the line. The comment at the end of the echo line is why the :v pattern needs a ^.",
    uses=["subst"],
)

# ---------- very magic ----------

vm = drills.command(
    "very-magic", "\\v  ( )  \\1", "very magic patterns and groups",
    """Start a pattern with \\v ("very magic") and ( ) | + ? = { } < > become special without a backslash,
    as in most other regex flavors: \\v(\\d+)-(\\d+) instead of \\(\\d\\+\\)-\\(\\d\\+\\). Parentheses make a
    group, and in the replacement \\1 to \\9 put back what each group matched, numbered by their opening
    parenthesis (\\0 or & is the whole match). The catch is that a literal ( ) { < > = ? + @ or | then
    needs a backslash: \\v\\(x\\) matches the text (x). Use whichever mode needs fewer backslashes.""",
    examples=[(":%s/\\v(\\w+) (\\w+)/\\2 \\1", "swap the first two words"), ("\\v(get|set)Name", "| means or"),
              ("\\v\\d{4}", "exactly four digits"), ("\\v\".{-}\"", "{-} is as few as possible"),
              ("\\v\\(x\\)", "literal parentheses")],
    level="complex",
)
vm.add(
    title="Columns before rows", par=26, ext="java", setup=OWN_FILE_ONLY,
    task="The grid API changed from (row, col) to (col, row). Swap the two numbers in every call.",
    start=text("""
        grid.set(3, 14);
        grid.set(12, 7);
        grid.clear(0, 9);
        grid.set(21, 5);
    """),
    target=text("""
        grid.set(14, 3);
        grid.set(7, 12);
        grid.clear(9, 0);
        grid.set(5, 21);
    """),
    hint="Capture each number in a group with (\\d+), then write them back as \\2, \\1. \\v at the start of "
         "the pattern saves the backslashes on ( ) and +.",
    uses=["subst", "range"],
)
vm.add(
    title="Dates to ISO", par=31, ext="csv", setup=OWN_FILE_ONLY,
    task="Rewrite each day/month/year date as year-month-day: 14/03/2026 becomes 2026-03-14.",
    start=text("""
        14/03/2026,deploy web
        02/04/2026,rollback api
        28/04/2026,deploy api
    """),
    target=text("""
        2026-03-14,deploy web
        2026-04-02,rollback api
        2026-04-28,deploy api
    """),
    hint="Three groups, written back as \\3-\\2-\\1. The pattern has slashes in it, so use another separator "
         "for :s, like #. Day and month are always two characters.",
    uses=["subst", "range"],
)
vm.add(
    title="Markdown links to HTML", par=42, ext="md", setup=OWN_FILE_ONLY,
    task="Turn each Markdown link [text](url) into <a href=\"url\">text</a>.",
    start=text("""
        Read [the guide](guide.html) first.
        Then try [the tutorial](tutorial.html).
        Stuck? Ask on [the forum](https://forum.example.com).
    """),
    target=text("""
        Read <a href="guide.html">the guide</a> first.
        Then try <a href="tutorial.html">the tutorial</a>.
        Stuck? Ask on <a href="https://forum.example.com">the forum</a>.
    """),
    hint="Two groups: the text between [ and ], and the url between ( and ). In very magic mode the "
         "literal [ ( ) need a backslash (a ] on its own is fine). The replacement has slashes, so use # "
         "as the separator.",
    uses=["subst", "range"],
)
vm.add(
    title="French to English", par=24, ext="txt", setup=OWN_FILE_ONLY,
    task="Flip the word list so it can be looked up the other way: english: french becomes french: english.",
    start=text("""
        cat: chat
        dog: chien
        good morning: bonjour
        thank you: merci
        see you soon: à bientôt
    """),
    target=text("""
        chat: cat
        chien: dog
        bonjour: good morning
        merci: thank you
        à bientôt: see you soon
    """),
    hint="Two groups, one on each side of \": \", written back the other way round. Some sides have spaces, "
         "so .* is the thing to capture.",
    uses=["subst", "range"],
)
vm.add(
    title="Readable phone numbers", par=28, ext="csv", setup=OWN_FILE_ONLY,
    task="Format the ten-digit phone numbers: 5551234567 becomes (555) 123-4567.",
    start=text("""
        ada,5551234567
        grace,5559876543
        alan,5550142200
        barbara,5553330199
    """),
    target=text("""
        ada,(555) 123-4567
        grace,(555) 987-6543
        alan,(555) 014-2200
        barbara,(555) 333-0199
    """),
    hint="Capture the first three digits and the next three in two groups, starting from the comma. The last "
         "four don't need a group: they can stay where they are. Parentheses in the replacement are just "
         "text.",
    uses=["subst", "range"],
)
vm.add(
    title="The reading list", par=40, ext="txt", setup=OWN_FILE_ONLY,
    task="Rewrite each Author - Title - Year line as Title (Year), by Author.",
    start=text("""
        Mary Shelley - Frankenstein - 1818
        Ursula K. Le Guin - The Dispossessed - 1974
        Douglas Hofstadter - Gödel, Escher, Bach - 1979
        Ted Chiang - Exhalation - 2019
    """),
    target=text("""
        Frankenstein (1818), by Mary Shelley
        The Dispossessed (1974), by Ursula K. Le Guin
        Gödel, Escher, Bach (1979), by Douglas Hofstadter
        Exhalation (2019), by Ted Chiang
    """),
    hint="Three groups, separated by \" - \". Without \\v that's three pairs of \\( \\); with it, the "
         "parentheses in the pattern need no backslashes, and the ones in the replacement are plain text "
         "anyway.",
    uses=["subst", "range"],
)

# ---------- case in the replacement ----------

rc = drills.command(
    "replace-case", "\\u  \\U  \\l  \\L  \\e", "change case in the replacement",
    """In the replacement of :s, \\u makes the next character uppercase and \\l lowercase. \\U makes
    everything after it uppercase, and \\L lowercase, until \\e or \\E (or the end of the replacement).
    They work on whatever follows them: typed text, & or a group like \\1. So :s/\\w\\+/\\u&/g capitalizes
    every word, and :s/\\v_(.)/\\u\\1/g turns snake_case into camelCase. (In a pattern, \\u means something
    else: any uppercase letter.)""",
    examples=[(":s/\\w\\+/\\u&/g", "capitalize every word"), (":s/\\v_(.)/\\u\\1/g", "snake_case to camelCase"),
              (":s/\\u/_\\l&/g", "camelCase to snake_case"), (":s/.*/\\U&", "the whole line in capitals"),
              ("\\U\\1\\e\\2", "only group 1 in capitals")],
    level="complex",
)
rc.add(
    title="Capitalize the headings", par=14, ext="md", setup=OWN_FILE_ONLY,
    task="Capitalize every word in the headings.",
    start=text("""
        # getting started
        ## install the tools
        ## write your first plugin
        # going further
    """),
    target=text("""
        # Getting Started
        ## Install The Tools
        ## Write Your First Plugin
        # Going Further
    """),
    hint="\\< matches the start of a word, so \\<. is a word's first character. In the replacement, \\u& is "
         "that character in uppercase.",
    uses=["subst", "range"],
)
rc.add(
    title="Strings to enum constants", par=23, ext="java", setup=OWN_FILE_ONLY,
    task="Turn each string into an enum constant that keeps the string: \"red\", becomes RED(\"red\"),.",
    start=text("""
        enum Color {
            "red",
            "green",
            "blue",
            "black";
        }
    """),
    target=text("""
        enum Color {
            RED("red"),
            GREEN("green"),
            BLUE("blue"),
            BLACK("black");
        }
    """),
    hint="Capture the text between the quotes. In the replacement, \\U\\1\\e writes it in capitals and \\e "
         "stops the uppercasing, so & (the whole match, quotes included) comes out unchanged.",
    uses=["very-magic", "subst", "range"],
)
rc.add(
    title="camelCase to snake_case", par=14, ext="py", setup=OWN_FILE_ONLY,
    task="These names came from Java. Convert them to Python's snake_case: getUserName becomes "
         "get_user_name.",
    start=text("""
        def getUserName(userId):
            userRecord = fetchRecord(userId)
            return userRecord.fullName
    """),
    target=text("""
        def get_user_name(user_id):
            user_record = fetch_record(user_id)
            return user_record.full_name
    """),
    hint="In a pattern, \\u matches any uppercase letter (ignorecase doesn't change that). Replace it with _ "
         "and the same letter in lowercase: \\l&.",
    uses=["subst", "range"],
)
rc.add(
    title="Quiet keywords", par=17, ext="sql", setup=OWN_FILE_ONLY,
    task="The team writes SQL keywords in lowercase. Lowercase every word written in capitals. The names in "
         "the strings ('Ada', 'London') keep their capital.",
    start=text("""
        SELECT name, city FROM users
        WHERE name = 'Ada' OR city = 'London'
        ORDER BY name DESC
        LIMIT 10;
    """),
    target=text("""
        select name, city from users
        where name = 'Ada' or city = 'London'
        order by name desc
        limit 10;
    """),
    hint="In a pattern, \\u is an uppercase letter, so two of them in a row only match a word in capitals. "
         "\\L in the replacement lowercases everything after it.",
    uses=["subst", "range"],
)
rc.add(
    title="Names, properly", par=16, ext="txt", setup=OWN_FILE_ONLY,
    task="The guest list was typed with Caps Lock on and off. Write every name with a capital first letter "
         "and the rest in lowercase.",
    start=text("""
        ADA LOVELACE
        grace hopper
        aLAN tURING
        Barbara LISKOV
        ken THOMPSON
    """),
    target=text("""
        Ada Lovelace
        Grace Hopper
        Alan Turing
        Barbara Liskov
        Ken Thompson
    """),
    hint="\\L lowercases the rest of the replacement, and \\u in front of it still uppercases the first "
         "character. Match each word, and put it back with both.",
    uses=["subst", "range"],
)
rc.add(
    title="Surnames first", par=27, ext="txt", setup=OWN_FILE_ONLY,
    task="For the badges, write the last name first, in capitals, then a comma and the first names: Grace "
         "Brewster Hopper becomes HOPPER, Grace Brewster.",
    start=text("""
        Ada Lovelace
        Grace Brewster Hopper
        Alan Turing
        Barbara Liskov
    """),
    target=text("""
        LOVELACE, Ada
        HOPPER, Grace Brewster
        TURING, Alan
        LISKOV, Barbara
    """),
    hint="Two groups: everything up to the last space, and the last name. Greedy .* takes the first group as "
         "far as it can. \\U\\2\\e writes the last name in capitals and stops there.",
    uses=["very-magic", "subst", "range"],
)

# ---------- \= ----------

ex = drills.command(
    "expr-replace", "\\=", "compute the replacement",
    """When the replacement of :s starts with \\=, the rest is a Vim expression, worked out again for every
    match, and its result is the replacement. submatch(0) is the whole match (submatch(1) is group 1), as
    text; arithmetic turns it into a number, so \\=submatch(0)*2 doubles it. line('.') is the line number
    of the match, . joins strings ('#' . line('.')), and printf() formats: printf('%03d', n) pads to
    three digits, printf('%X', n) writes hexadecimal.""",
    examples=[(":%s/\\d\\+/\\=submatch(0)*2/g", "double every number"), (":%s/^/\\=line('.') . ' '/",
              "number the lines"), ("\\=printf('%03d', submatch(0))", "7 becomes 007"),
              ("\\=submatch(1) . submatch(1)", "group 1, twice")],
    level="complex",
)
ex.add(
    title="Minutes to seconds", par=28, ext="csv", setup=OWN_FILE_ONLY,
    task="The scheduler now reads seconds, not minutes. Multiply every number by 60.",
    start=text("""
        task,min_wait,max_wait
        backup,5,30
        sync,1,10
        report,15,45
        cleanup,2,20
    """),
    target=text("""
        task,min_wait,max_wait
        backup,300,1800
        sync,60,600
        report,900,2700
        cleanup,120,1200
    """),
    hint="\\d\\+ matches each number. A replacement that starts with \\= is an expression, and submatch(0) is "
         "the matched number.",
    uses=["subst", "range"],
)
ex.add(
    title="Where am I?", par=21, ext="py", setup=OWN_FILE_ONLY,
    task="Make each debug print say which line it's on: replace each LINE with that line's number.",
    start=text("""
        def load(path):
            print("reached LINE")
            with open(path) as f:
                print("reached LINE")
                text = f.read()
            print("reached LINE")
            rows = text.splitlines()
            print("reached LINE")
            header = rows.pop(0)
            print("reached LINE")
            return header, rows
    """),
    target=text("""
        def load(path):
            print("reached 2")
            with open(path) as f:
                print("reached 4")
                text = f.read()
            print("reached 6")
            rows = text.splitlines()
            print("reached 8")
            header = rows.pop(0)
            print("reached 10")
            return header, rows
    """),
    hint="line('.') is the number of the line being substituted. Put it after \\= in the replacement.",
    uses=["subst", "range"],
)
ex.add(
    title="Bytes in hex", par=42, ext="c", setup=OWN_FILE_ONLY,
    task="Write every byte in hexadecimal, two digits with a 0x in front: 72 becomes 0x48, and 10 "
         "becomes 0x0A.",
    start=text("""
        char msg[] = {72, 101, 108, 108, 111, 44, 32,
                      87, 111, 114, 108, 100, 33, 10};
    """),
    target=text("""
        char msg[] = {0x48, 0x65, 0x6C, 0x6C, 0x6F, 0x2C, 0x20,
                      0x57, 0x6F, 0x72, 0x6C, 0x64, 0x21, 0x0A};
    """),
    hint="printf() formats a number: %X is uppercase hexadecimal, and %02X pads it to two digits. Use it "
         "after \\= with submatch(0).",
    uses=["subst", "range"],
)
ex.add(
    title="Do the arithmetic", par=29, ext="ini", setup=OWN_FILE_ONLY,
    task="The new config reader doesn't do arithmetic. Replace each value with what it works out to: "
         "60*60*24 becomes 86400.",
    start=text("""
        [limits]
        session = 60*60*24
        upload = 1024*1024*8
        cache = 60*15
        retries = 3
        backoff = 250*4
    """),
    target=text("""
        [limits]
        session = 86400
        upload = 8388608
        cache = 900
        retries = 3
        backoff = 1000
    """),
    hint="eval() works out an expression written as text, so \\=eval(submatch(0)) replaces a match with its "
         "value. Each value runs from its first digit to the end of the line, and the names have no digits.",
    uses=["subst", "range"],
)
ex.add(
    title="JSON has no hex", par=28, ext="json", setup=OWN_FILE_ONLY,
    task="JSON doesn't allow hexadecimal numbers. Write every 0x number in decimal: 0xFF becomes 255.",
    start=text("""
        {
          "mask": 0xFF,
          "color": 0x1E66F5,
          "flags": [0x01, 0x04, 0x10],
          "port": 8080
        }
    """),
    target=text("""
        {
          "mask": 255,
          "color": 1992437,
          "flags": [1, 4, 16],
          "port": 8080
        }
    """),
    hint="When Vim turns text into a number, it reads a 0x in front as hexadecimal. Adding 0 is enough to "
         "make it a number, and the number comes out in decimal. One line has three.",
    uses=["subst", "range"],
)
ex.add(
    title="In Celsius, please", par=37, ext="txt", setup=OWN_FILE_ONLY,
    task="Convert every temperature to Celsius: (F - 32) * 5 / 9, so 50F becomes 10C. They all come out "
         "even.",
    start=text("""
        Anchorage  5F    snow
        London     50F   rain
        Rome       68F   sunny
        Cairo      95F   sunny
        Phoenix    104F  heat warning
    """),
    target=text("""
        Anchorage  -15C    snow
        London     10C   rain
        Rome       20C   sunny
        Cairo      35C   sunny
        Phoenix    40C  heat warning
    """),
    hint="Text that starts with digits becomes the number they make, so submatch(0) of 50F works in "
         "arithmetic as 50. . joins strings, for the C. The expression has a / in it, so use another "
         "separator for :s, like #.",
    uses=["subst", "range"],
)

# ---------- :sort ----------

so = drills.command(
    "sort", ":sort", "sort lines",
    """:sort sorts lines, by default the whole file (give it a range, like vip:sort, for part of it). It
    compares text character by character, so 100 comes before 9; the n flag sorts by the first number on
    each line instead. ! reverses the order, u drops duplicate lines, and i ignores case. With a
    /pattern/, it sorts by what comes after the first match on each line (add r to sort by the match
    itself). Flags combine: :sort! n is biggest number first. The short form is :sor.""",
    examples=[(":sort", "alphabetically"), (":sort u", "and drop duplicates"), (":sort! n", "biggest number first"),
              (":sort / /", "by what follows the first space"), ("vip:sort", "just this paragraph")],
    level="complex",
)
so.add(
    title="Tidy the .gitignore", par=7, ext="txt", setup=OWN_FILE_ONLY,
    task="Sort the .gitignore and drop the duplicate lines.",
    start=text("""
        node_modules/
        dist/
        .env
        dist/
        coverage/
        .env
        *.log
    """),
    target=text("""
        *.log
        .env
        coverage/
        dist/
        node_modules/
    """),
    hint=":sort takes flags after it, and one of them removes duplicates.",
)
so.add(
    title="Biggest first", par=7, ext="txt", setup=OWN_FILE_ONLY,
    task="This is du output (size in KB, then the folder). Sort it from the biggest to the smallest.",
    start=text("""
        12  README.md
        5120  node_modules
        88  src
        940  dist
        4  .gitignore
    """),
    target=text("""
        5120  node_modules
        940  dist
        88  src
        12  README.md
        4  .gitignore
    """),
    hint="Without n, text sorting would put 940 before 5120. ! reverses, and :sor is short for :sort.",
)
so.add(
    title="By last name", par=9, ext="txt", setup=OWN_FILE_ONLY,
    task="Sort the speakers by last name.",
    start=text("""
        ada lovelace
        alan turing
        grace hopper
        linus torvalds
        barbara liskov
    """),
    target=text("""
        grace hopper
        barbara liskov
        ada lovelace
        linus torvalds
        alan turing
    """),
    hint="With a /pattern/, :sort compares what comes after the first match on each line. Here the "
         "pattern is a single space.",
)
so.add(
    title="Case doesn't count", par=7, ext="txt", setup=OWN_FILE_ONLY,
    task="Sort the file list alphabetically, ignoring case: bin comes before Brewfile.",
    start=text("""
        Brewfile
        .bashrc
        README.md
        Makefile
        .gitignore
        docs
        src
        LICENSE
        bin
    """),
    target=text("""
        .bashrc
        .gitignore
        bin
        Brewfile
        docs
        LICENSE
        Makefile
        README.md
        src
    """),
    hint="Without a flag, every capital sorts before every lowercase letter. One flag makes :sort ignore "
         "case.",
)
so.add(
    title="Grouped by extension", par=12, ext="txt", setup=OWN_FILE_ONLY,
    task="Sort the files by extension, the part after the last dot. Files with the same extension keep the "
         "order they have now.",
    start=text("""
        parser.c
        README.md
        lexer.h
        archive.tar.gz
        lexer.c
        notes.md
        parser.h
        main.c
    """),
    target=text("""
        parser.c
        lexer.c
        main.c
        archive.tar.gz
        lexer.h
        parser.h
        README.md
        notes.md
    """),
    hint="With a /pattern/, :sort compares what comes after the match. .* is greedy, so .*\\. runs to the "
         "last dot. :sort keeps lines that compare equal in their old order.",
)
so.add(
    title="In the order they were merged", par=12, ext="md", setup=OWN_FILE_ONLY,
    task="Sort the Unreleased entries (lines 2 to 6) by pull request number, smallest first. The 1.3.0 "
         "section stays as it is.",
    start=text("""
        ## Unreleased
        - fix 2 typos in the docs (#88)
        - add --json output (#112)
        - speed up the parser (#97)
        - remove the 3 deprecated flags (#64)
        - support 4-space tabs (#101)

        ## 1.3.0
        - add the init command (#51)
        - fix Windows paths (#47)
    """),
    target=text("""
        ## Unreleased
        - remove the 3 deprecated flags (#64)
        - fix 2 typos in the docs (#88)
        - speed up the parser (#97)
        - support 4-space tabs (#101)
        - add --json output (#112)

        ## 1.3.0
        - add the init command (#51)
        - fix Windows paths (#47)
    """),
    hint="n sorts by the first number on each line, which here would be the 2 or the 3. With a /pattern/ as "
         "well, it's the first number after the match. Give :sort a range for the five entries.",
    uses=["range"],
)

# ---------- & g& :&& ----------

amp = drills.command(
    "amp", "&  g&  :&&", "repeat the last substitute",
    """& repeats the last :s on the cursor line. In Neovim it keeps the flags too (& is a mapping for
    :&&), so a substitute with g stays global; in plain Vim, & and :& drop them. A count gives it a range
    (3& covers this line and the next two), and g& repeats it on every line with the same flags. g& is
    short for :%s//~/&, so it uses your last search pattern: search for something else in between and
    g& looks for that instead. @: (Project 08) repeats any Ex command.""",
    examples=[("&", "again on this line"), ("j&", "again on the next line"), ("3&", "on three lines"),
              ("g&", "again on every line"), (":5,9&&", "on lines 5 to 9, same flags")],
    level="complex",
)
amp.add(
    title="Stripes", par=16, ext="txt", setup=OWN_FILE_ONLY,
    task="Turn every dot on rows 1, 3 and 5 into a *. Rows 2 and 4 stay dotted.",
    start=text("""
        .  .  .  .  .
        .  .  .  .  .
        .  .  .  .  .
        .  .  .  .  .
        .  .  .  .  .
    """),
    target=text("""
        *  *  *  *  *
        .  .  .  .  .
        *  *  *  *  *
        .  .  .  .  .
        *  *  *  *  *
    """),
    hint="Fix row 1 with :s (a dot is \\. in a pattern, and you need g). Then go down two rows: & repeats "
         "the last substitute, g flag included.",
    uses=["subst"],
)
amp.add(
    title="Dashes in the dates", par=10, ext="csv", setup=OWN_FILE_ONLY,
    task="The date got split into three fields. Join it back with dashes: 2026,03,14,deploy web becomes "
         "2026-03-14,deploy web.",
    start=text("""
        2026,03,14,deploy web
        2026,03,15,rollback web
        2026,04,02,deploy api
    """),
    target=text("""
        2026-03-14,deploy web
        2026-03-15,rollback web
        2026-04-02,deploy api
    """),
    hint="Without the g flag, :%s/,/-/ changes the first comma on each line. Doing that once more on every "
         "line changes the second one: that's what g& does.",
    uses=["subst", "range"],
)
amp.add(
    title="Wrong way round", par=35, ext="java", setup=OWN_FILE_ONLY,
    task="assertEquals takes (expected, actual). Lines 1, 3 and 5 have them the wrong way round: swap the "
         "two arguments there. Lines 2 and 4 are already right.",
    start=text("""
        assertEquals(total, 10);
        assertEquals(4, count);
        assertEquals(name, "ada");
        assertEquals("ok", status);
        assertEquals(items.size(), 3);
    """),
    target=text("""
        assertEquals(10, total);
        assertEquals(4, count);
        assertEquals("ada", name);
        assertEquals("ok", status);
        assertEquals(3, items.size());
    """),
    hint="Write the swap once for line 1: capture what's between ( and the last \", \", and what's after it "
         "up to the last ). Then & repeats it on any line you move to.",
    uses=["subst", "very-magic"],
)
amp.add(
    title="Thousands separators", par=25, ext="txt", setup=OWN_FILE_ONLY,
    task="Make the big numbers readable: a comma between every group of three digits, from the right, so "
         "2147483647 becomes 2,147,483,647. Numbers under 1000 stay as they are.",
    start=text("""
        Page views   2147483647
        Revenue      1234567
        Costs        987654
        Users        48210
        Countries    12
    """),
    target=text("""
        Page views   2,147,483,647
        Revenue      1,234,567
        Costs        987,654
        Users        48,210
        Countries    12
    """),
    hint="One :s can put a comma before the last three digits of every number: three digits at the end of a "
         "word, with a digit before them (\\zs starts the match after it). The next comma goes before the "
         "next three, so run the same substitute again with g&, as often as it takes.",
    uses=["subst", "range"],
)
amp.add(
    title="One name for one thing", par=25, ext="js", cursor=(1, 20), setup=OWN_FILE_ONLY,
    task="userId and uid are the same thing. Rename both to accountId everywhere. The cursor is on the "
         "first userId.",
    start=text("""
        function getOrders(userId) {
            return db.orders.where({ userId });
        }

        function getInvoices(uid) {
            return db.invoices.where({ userId: uid });
        }

        function getCart(uid) {
            return carts.get(uid);
        }
    """),
    target=text("""
        function getOrders(accountId) {
            return db.orders.where({ accountId });
        }

        function getInvoices(accountId) {
            return db.invoices.where({ accountId: accountId });
        }

        function getCart(accountId) {
            return carts.get(accountId);
        }
    """),
    hint="g& repeats the last substitute on every line, with the last search pattern, not the last :s "
         "pattern. So after the first rename, a search for the second name is all g& needs.",
    uses=["subst", "star", "search", "range"],
)
amp.add(
    title="Stutter", par=24, ext="txt", setup=OWN_FILE_ONLY,
    task="Proofreading: a word typed twice or three times in a row becomes one. \"the theory\" is fine.",
    start=text("""
        We went to the the station early.
        It is is very very very cold today.
        Bring your your coat and and gloves.
        That was the theory, at least.
    """),
    target=text("""
        We went to the station early.
        It is very cold today.
        Bring your coat and gloves.
        That was the theory, at least.
    """),
    hint="In a pattern, \\1 matches the same text again that group 1 matched, so (\\w+) \\1 is a word twice. "
         "End it at the end of a word. Three in a row take two goes: g& is the second.",
    uses=["subst", "very-magic", "range"],
)

# ---------- flags ----------

fl = drills.command(
    "subst-flags", ":s///i  I  c  n", "substitute flags: case, confirm, count",
    """Flags go after the last / of :s, and combine (gc, gI). I matches case exactly and i ignores case,
    for this one :s, whatever ignorecase and smartcase say; \\C and \\c in the pattern do the same. That
    matters with an empty pattern from * or #, which ignore smartcase. c asks before each change: y
    yes, n no, a all the rest, l this one and stop, q stop. n changes nothing and just reports how many
    matches there are. & (first) keeps the flags of the previous :s.""",
    examples=[(":%s/max/best/gI", "max but not MAX"), ("*:%s//new/gI", "the word under the cursor, exact case"),
              (":%s/,/;/gc", "ask before each change"), (":%s/TODO//gn", "count the matches")],
    level="complex",
)
fl.add(
    title="max, not MAX", par=16, ext="c", setup=OWN_FILE_ONLY,
    task="Rename the variable max to best. The macro MAX stays as it is.",
    start=text("""
        #define MAX 100
        int max = 0;
        for (int i = 0; i < MAX; i++)
            if (a[i] > max) max = a[i];
        printf("%d of %d\\n", max, MAX);
    """),
    target=text("""
        #define MAX 100
        int best = 0;
        for (int i = 0; i < MAX; i++)
            if (a[i] > best) best = a[i];
        printf("%d of %d\\n", best, MAX);
    """),
    hint="ignorecase is on, and an all-lowercase pattern ignores case, so max also matches MAX. The I flag "
         "makes this :s match case exactly. Line 4 has max twice.",
    uses=["subst", "range"],
)
fl.add(
    title="Semicolons, but not in quotes", par=15, ext="csv", setup=OWN_FILE_ONLY,
    task="Switch the separators from , to ;. The comma inside the quoted field is part of the text and "
         "stays.",
    start=text("""
        ada,london,"tea,no sugar"
        alan,wilmslow,coffee
        grace,arlington,water
        linus,helsinki,coffee
    """),
    target=text("""
        ada;london;"tea,no sugar"
        alan;wilmslow;coffee
        grace;arlington;water
        linus;helsinki;coffee
    """),
    hint="The c flag asks before every change. y says yes and n no, and a says yes to all the rest.",
    uses=["subst", "range"],
)
fl.add(
    title="id, not ID", par=16, ext="py", cursor=(2, 10), setup=OWN_FILE_ONLY,
    task="The cursor is on the parameter id. Rename it to user_id everywhere. The constant ID and the word "
         "valid stay as they are.",
    start=text("""
        ID = 7
        def find(id):
            if id == ID:
                return users[id]
            return lookup(id, valid=True)
    """),
    target=text("""
        ID = 7
        def find(user_id):
            if user_id == ID:
                return users[user_id]
            return lookup(user_id, valid=True)
    """),
    hint="* searches for the whole word under the cursor, but it ignores smartcase, so it also finds ID. "
         ":s//new/ reuses that search, and the I flag makes it match case exactly.",
    uses=["star", "subst", "range"],
)
fl.add(
    title="tmp, but not TMPDIR", par=15, ext="sh", setup=OWN_FILE_ONLY,
    task="Rename tmp to work, inside longer names too (tmpfile becomes workfile). The environment variable "
         "TMPDIR stays as it is.",
    start=text("""
        tmp=$(mktemp -d)
        tmpfile="$tmp/out.txt"
        export TMPDIR="$tmp"
        trap 'rm -rf "$tmp"' EXIT
        make build > "$tmpfile"
        cp "$tmpfile" "$TMPDIR/build.log"
    """),
    target=text("""
        work=$(mktemp -d)
        workfile="$work/out.txt"
        export TMPDIR="$work"
        trap 'rm -rf "$work"' EXIT
        make build > "$workfile"
        cp "$workfile" "$TMPDIR/build.log"
    """),
    hint="* would skip tmpfile, but g* also matches inside longer words. Like *, it ignores case, so the I "
         "flag has to put case back.",
    uses=["star", "subst", "range"],
)
fl.add(
    title="Vim, mostly Neovim", par=24, ext="md", setup=OWN_FILE_ONLY,
    task="The team moved to Neovim: change Vim to Neovim, except on the two lines about Vim's history "
         "(lines 4 and 7).",
    start=text("""
        # Editor setup

        Vim is the editor we use for everything here.
        Bram Moolenaar wrote Vim and kept it going for decades.
        Install Vim with brew, then copy the config below.
        Open Vim and run :checkhealth once.
        Vim started out as a clone of vi on the Amiga.
        Our team's Vim config lives in ~/.config/nvim.
        Restart Vim after you change it.
        If Vim feels slow, see the FAQ.
        Plugins for Vim go in the pack folder.
        Ask in #editors if Vim gives you trouble.
    """),
    target=text("""
        # Editor setup

        Neovim is the editor we use for everything here.
        Bram Moolenaar wrote Vim and kept it going for decades.
        Install Neovim with brew, then copy the config below.
        Open Neovim and run :checkhealth once.
        Vim started out as a clone of vi on the Amiga.
        Our team's Neovim config lives in ~/.config/nvim.
        Restart Neovim after you change it.
        If Neovim feels slow, see the FAQ.
        Plugins for Neovim go in the pack folder.
        Ask in #editors if Neovim gives you trouble.
    """),
    hint="The c flag asks before each change: y for yes, n for no, and a for yes to all the rest. After "
         "line 7, every one is a yes.",
    uses=["subst", "range"],
)
fl.add(
    title="Not the key, not the header", par=22, ext="js", cursor=(2, 23), setup=OWN_FILE_ONLY,
    task="Rename the parameter id to orderId everywhere it's used. The id: key in the JSON body and the "
         "ID in the header name stay. The cursor is on the parameter.",
    start=text("""
        const HEADER = "X-Request-ID";
        async function cancel(id) {
            const body = JSON.stringify({ id: id, reason: "user" });
            log(`cancelling ${id}`);
            await fetch(`/orders/${id}/cancel`, { method: "POST", body });
            return id;
        }
    """),
    target=text("""
        const HEADER = "X-Request-ID";
        async function cancel(orderId) {
            const body = JSON.stringify({ id: orderId, reason: "user" });
            log(`cancelling ${orderId}`);
            await fetch(`/orders/${orderId}/cancel`, { method: "POST", body });
            return orderId;
        }
    """),
    hint="* finds every whole-word id, but also the ID in the header (it ignores case) and the key. With the "
         "c flag you say n to those two and y to the rest; a says yes to everything after.",
    uses=["star", "subst", "range"],
)
