"""Drills for Project 06: short problems that practice one command at a time.
Play them with:  python3 check.py drill      (the reference solutions are in ../solutions/drills/)"""
from trainer import Drills, text

drills = Drills(__file__)

ESC = "\x1b"  # a literal <Esc>, as it appears when a macro is pasted into a file (shown as ^[)
CTRL_R = "\x12"  # a literal Ctrl-r (shown as ^R)

# ---------- q @ ----------

macro = drills.command(
    "macro", "q{r}  @{r}", "record and play a macro",
    """q followed by a letter starts recording everything you type into that register (the bottom line
    shows "recording @a"), and q again stops. @a plays those keys back exactly as if you typed them
    again, and Q plays the macro you recorded last in a single key. A macro replays keys, not
    intentions: 5l moves five characters on every line, whether or not that's where the comma is. So
    start from a known spot (I, A, 0, ^ or $), move with f, t, w, b or a search, and end by moving to
    the next line (j or +) so the next run starts in the right place. If any key fails (an f that finds
    nothing, j on the last line), the macro stops right there.""",
    examples=[("qa", "start recording into register a"), ("q", "stop recording"), ("@a", "play macro a"),
              ("Q", "play the macro you recorded last"), ("qaA;<Esc>jq", "record: add a semicolon, move down"),
              ("2Q", "play it twice")],
)
macro.add(
    title="Two Markdown links", par=17, ext="md",
    task="Turn both lines into Markdown links like [neovim](https://neovim.io).",
    start=text("""
        neovim https://neovim.io
        lua https://www.lua.org/manual/5.1/
    """),
    target=text("""
        [neovim](https://neovim.io)
        [lua](https://www.lua.org/manual/5.1/)
    """),
    hint="Record line 1 with qa ... q: I[ adds the bracket, f<Space> finds the space, s]( replaces it, "
         "and A) closes the link. End the recording with j, then Q plays the macro you just recorded on line 2.",
    uses=["insert", "f", "c"],
)
macro.add(
    title="Bracket the log level", par=15, ext="log",
    task="Drop the date and time from both log lines and put the level in brackets: [WARN] disk at 91%",
    start=text("""
        2026-10-21 09:14:07 WARN disk at 91%
        2026-10-21 09:15:32 ERROR backup failed
    """),
    target=text("""
        [WARN] disk at 91%
        [ERROR] backup failed
    """),
    hint="d2W deletes the date and time. I[ opens the bracket, and e jumps to the end of the level, "
         "whatever its length, so a] closes it. End with + and play the macro on line 2 with Q.",
    uses=["d", "count", "bigword", "insert", "word", "plus"],
)
macro.add(
    title="Parenthesize the defines", par=14, ext="c",
    task="Wrap each value in parentheses, so the macros are safe inside bigger expressions: "
         "#define BUF_SIZE (4 * 1024)",
    start=text("""
        #define BUF_SIZE 4 * 1024
        #define TIMEOUT_MS 30 * 1000
        #define LAST_INDEX COUNT - 1
    """),
    target=text("""
        #define BUF_SIZE (4 * 1024)
        #define TIMEOUT_MS (30 * 1000)
        #define LAST_INDEX (COUNT - 1)
    """),
    hint="The names have different lengths and the values contain spaces, so neither l nor $b finds the "
         "value. 2W does: it's always the third WORD. Then A) closes it and + moves on. 2Q does the "
         "other two lines.",
    uses=["bigword", "count", "insert", "plus"],
)
macro.add(
    title="Keyword arguments", par=15, ext="py",
    task='Someone used dict-literal syntax inside dict(...). Turn each entry into a keyword argument: '
         'host="localhost",',
    start=text("""
        DEFAULTS = dict(
            "host": "localhost",
            "port": 8080,
            "debug": False,
            "log_file": "/var/log/app.log",
        )
    """),
    target=text("""
        DEFAULTS = dict(
            host="localhost",
            port=8080,
            debug=False,
            log_file="/var/log/app.log",
        )
    """),
    hint="+ lands on the opening quote of a key. x deletes it, f\" finds the closing one, and cf<Space> "
         "changes the quote, colon and space into =. End with + and play the macro three times.",
    uses=["plus", "x", "f", "c", "count"],
)
macro.add(
    title="Final constants", par=20, ext="py", cursor=(3, 1),
    task="Make these module constants: uppercase each name and mark it Final, like "
         "MAX_RETRIES: Final = 3. The cursor starts on max_retries.",
    start=text("""
        from typing import Final

        max_retries = 3
        timeout = 30.0
        base_url = "https://api.example.com"
        user_agent = "vimcourse/1.0"
    """),
    target=text("""
        from typing import Final

        MAX_RETRIES: Final = 3
        TIMEOUT: Final = 30.0
        BASE_URL: Final = "https://api.example.com"
        USER_AGENT: Final = "vimcourse/1.0"
    """),
    hint="gUiw uppercases the name, however long it is, and e jumps to its end, so a: Final types the "
         "annotation in the right place. End with + and use a count for the other three lines.",
    uses=["case", "iw", "word", "insert", "plus", "count"],
)
macro.add(
    title="Rows to tuples", par=26, ext="py",
    task='Turn each CSV row into a tuple of strings: ("ada", "lovelace", "ada@ex.io"),',
    start=text("""
        USERS = [
            ada,lovelace,ada@ex.io
            alan,turing,alan@ex.io
            grace,hopper,grace@ex.io
            linus,torvalds,linus@ex.io
        ]
    """),
    target=text("""
        USERS = [
            ("ada", "lovelace", "ada@ex.io"),
            ("alan", "turing", "alan@ex.io"),
            ("grace", "hopper", "grace@ex.io"),
            ("linus", "torvalds", "linus@ex.io"),
        ]
    """),
    hint='A macro can use ; and . too. Fix the first comma with f,s", "<Esc>, then ; finds the second '
         'comma and . repeats the change. I(" and A"), finish the row, + moves on.',
    uses=["insert", "f", "c", "semicolon", "dot", "plus", "count"],
)
macro.add(
    title="Find the next malloc", par=19, ext="c",
    task="Use calloc so the memory starts zeroed: malloc(x) becomes calloc(1, x).",
    start=text("""
        struct node *head = malloc(sizeof(struct node));
        if (!head) return NULL;
        int *counts = malloc(64 * sizeof(int));
        char *name = malloc(strlen(src) + 1);
        if (!name) goto fail;
        double *weights = malloc(n * sizeof(double));
    """),
    target=text("""
        struct node *head = calloc(1, sizeof(struct node));
        if (!head) return NULL;
        int *counts = calloc(1, 64 * sizeof(int));
        char *name = calloc(1, strlen(src) + 1);
        if (!name) goto fail;
        double *weights = calloc(1, n * sizeof(double));
    """),
    hint="The mallocs aren't on neighboring lines, so start the macro with a search: /mal<CR> lands on "
         "the next one wherever you are. Then rc, and f( a1, <Esc>. A count plays it for the other three.",
    uses=["search", "r", "f", "insert", "count"],
)
macro.add(
    title="Name every color", par=24, ext="c",
    task='Turn the list into a table of names using designated initializers: [RED] = "RED",',
    start=text("""
        static const char *color_names[] = {
            RED,
            GREEN,
            BLUE,
            ALPHA_MASK,
        };
    """),
    target=text("""
        static const char *color_names[] = {
            [RED] = "RED",
            [GREEN] = "GREEN",
            [BLUE] = "BLUE",
            [ALPHA_MASK] = "ALPHA_MASK",
        };
    """),
    hint="The name appears twice, so yank it first with yiw. I[ opens the bracket, e jumps to the end of "
         "the name, and a] = \"<C-r>0\" types the rest, with Ctrl-r 0 inserting the yank.",
    uses=["plus", "y", "iw", "insert", "word", "ctrl-r", "count"],
)
macro.add(
    title="Headings with a hash", par=17, ext="md",
    task="Turn the underlined headings into ## headings, and delete the ------- lines.",
    start=text("""
        Install
        -------
        Run the installer for your platform.

        Usage
        -----
        - open a file
        - save it

        Credits
        -------
        Made by Rick.
    """),
    target=text("""
        ## Install
        Run the installer for your platform.

        ## Usage
        - open a file
        - save it

        ## Credits
        Made by Rick.
    """),
    hint="Let the macro find each underline with /--<CR> (a single - would also find the list items). "
         "dd deletes it, k goes up to the heading, and I## adds the hashes. 2Q does the other two.",
    uses=["search", "dd", "insert", "count"],
)
macro.add(
    title="Generate the getters", par=47, ext="java", cursor=(2, 1),
    task="Replace each field with a getter, like public String getName() { return name; }. "
         "The cursor starts on the first field.",
    start=text("""
        class User {
            String name;
            int age;
            List<String> tags;
        }
    """),
    target=text("""
        class User {
            public String getName() { return name; }
            public int getAge() { return age; }
            public List<String> getTags() { return tags; }
        }
    """),
    hint="The types have different shapes, so find the name from the end: $b. Yank it with yiw, type "
         "get in front with iget<Esc>, then l~ capitalizes the name. $s replaces the ; with the body, "
         "and Ctrl-r 0 puts the lowercase name back.",
    uses=["insert", "line", "word", "y", "iw", "case", "c", "ctrl-r", "plus", "count"],
)
macro.add(
    title="Front matter to a table", par=19, ext="md",
    task="Turn each key: value line into a table row: | name | garden |",
    start=text("""
        name: garden
        version: 2.4.1
        license: MIT
    """),
    target=text("""
        | name | garden |
        | version | 2.4.1 |
        | license | MIT |
    """),
    hint="Record line 1: I| adds the first bar, E reaches the colon at the end of the key, and s | "
         "replaces it. A | closes the row. End with j, and a count plays the macro on the other two lines.",
    uses=["insert", "bigword", "c", "count"],
)
macro.add(
    title="Defines to an enum", par=19, ext="c",
    task="Turn the #define constants into enum entries, indented by 4: LOG_DEBUG = 10,",
    start=text("""
        enum log_level {
        #define LOG_DEBUG 10
        #define LOG_INFO 20
        #define LOG_WARN 30
        #define LOG_ERROR 40
        };
    """),
    target=text("""
        enum log_level {
            LOG_DEBUG = 10,
            LOG_INFO = 20,
            LOG_WARN = 30,
            LOG_ERROR = 40,
        };
    """),
    hint="dW deletes #define and its space. e and a = put the equals sign after the name, whatever its "
         "length, A, adds the comma, and >> indents. End with + (first non-blank of the next line, which "
         "is column 1 there) and play it three more times.",
    uses=["d", "bigword", "word", "insert", "indent", "plus", "count"],
)
macro.add(
    title="require to import", par=29, ext="js",
    task="Turn each CommonJS require into an ES import: const fs = require(\"fs\"); becomes "
         "import fs from \"fs\";",
    start=text("""
        const fs = require("fs");
        const path = require("path");
        const express = require("express");
        const { promisify } = require("util");
    """),
    target=text("""
        import fs from "fs";
        import path from "path";
        import express from "express";
        import { promisify } from "util";
    """),
    hint="Three edits per line: cw turns const into import, f= and cf( turn = require( into from, and f)x "
         "drops the ). f= finds the = after a { } name as well as after a plain one. End with +.",
    uses=["c", "word", "f", "x", "insert", "plus", "count"],
)
macro.add(
    title="Links with anchors", par=36, ext="html", setup=["setlocal indentexpr="],
    task="Turn each item into a link to its section: <li><a href=\"#pricing\">Pricing</a></li>. The anchor "
         "is the label in lowercase.",
    start=text("""
        <ul class="nav">
          <li>Pricing</li>
          <li>Docs</li>
          <li>Blog</li>
          <li>Support</li>
        </ul>
    """),
    target=text("""
        <ul class="nav">
          <li><a href="#pricing">Pricing</a></li>
          <li><a href="#docs">Docs</a></li>
          <li><a href="#blog">Blog</a></li>
          <li><a href="#support">Support</a></li>
        </ul>
    """),
    hint="cit deletes the label into the unnamed register, so Ctrl-r \" can type it twice while you write "
         "the <a> tag. Then F# goes back to the anchor and gue lowercases it. A macro replays Ctrl-r \" as "
         "keys, so each run types its own label.",
    uses=["tag", "c", "ctrl-r", "f", "case", "word", "plus", "count"],
)
macro.add(
    title="Shorter log lines", par=20, ext="log",
    task="Shorten each logfmt line: ts=09:14:07 level=warn msg=\"disk at 91%\" becomes "
         "09:14:07 WARN disk at 91%",
    start=text("""
        ts=09:14:07 level=warn msg="disk at 91%"
        ts=09:15:32 level=error msg="backup failed"
        ts=09:16:02 level=info msg="retrying"
        ts=09:17:44 level=warn msg="disk at 95%"
    """),
    target=text("""
        09:14:07 WARN disk at 91%
        09:15:32 ERROR backup failed
        09:16:02 INFO retrying
        09:17:44 WARN disk at 95%
    """),
    hint="ts= and msg=\" are the same on every line, so a count of x deletes them. The levels differ: df= "
         "deletes level=, and gUe uppercases what's left. W gets from field to field, and $x drops the "
         "last quote. End with +.",
    uses=["x", "count", "d", "f", "bigword", "case", "word", "line", "plus"],
)
macro.add(
    title="A bar per day", par=16,
    task="Replace each number with that many # signs: mon 3 becomes mon ###.",
    start=text("""
        mon 3
        tue 7
        wed 5
        thu 2
        fri 6
    """),
    target=text("""
        mon ###
        tue #######
        wed #####
        thu ##
        fri ######
    """),
    hint="Any register can be played as keys, so if register 0 holds 7, @0 types 7, a count. In the "
         "macro: $ and yiw yank the number, x deletes it, and @0 followed by a#<Esc> appends that many #.",
    uses=["line", "y", "iw", "x", "count", "insert", "plus", "edit-macro"],
)
macro.add(
    title="Settings to environment variables", par=27, ext="toml",
    task="These [server] settings move to environment variables: host = \"0.0.0.0\" becomes "
         "SERVER_HOST=0.0.0.0",
    start=text("""
        host = "0.0.0.0"
        port = "8080"
        log_level = "info"
        data_dir = "/var/lib/garden"
    """),
    target=text("""
        SERVER_HOST=0.0.0.0
        SERVER_PORT=8080
        SERVER_LOG_LEVEL=info
        SERVER_DATA_DIR=/var/lib/garden
    """),
    hint="gUiw uppercases the key, and ISERVER_ adds the prefix. From the space after the key, 4s "
         "changes the four characters = \" into =, and $x drops the last quote. End with +.",
    uses=["case", "iw", "insert", "f", "c", "x", "line", "plus", "count"],
)
macro.add(
    title="Fluent assertions", par=47, ext="java",
    task="Move the tests to AssertJ: assertEquals(42, total); becomes assertThat(total).isEqualTo(42); "
         "The expected value comes first in assertEquals and last in the new form.",
    start=text("""
        assertEquals(42, total);
        assertEquals("ada", user.name());
        assertEquals(3, cart.size());
        assertEquals(true, cart.isPaid());
        assertEquals(1999, cart.totalCents());
    """),
    target=text("""
        assertThat(total).isEqualTo(42);
        assertThat(user.name()).isEqualTo("ada");
        assertThat(cart.size()).isEqualTo(3);
        assertThat(cart.isPaid()).isEqualTo(true);
        assertThat(cart.totalCents()).isEqualTo(1999);
    """),
    hint="cw renames the method. Cut the expected value into a named register with \"adt, (the later x "
         "would replace the unnamed one), and delete the comma and space. $F) finds the last ), and "
         "a.isEqualTo( with Ctrl-r a puts the value back at the end. End with +.",
    uses=["c", "word", "d", "t", "named", "x", "line", "f", "insert", "ctrl-r", "plus", "count"],
)
macro.add(
    title="Check every fopen", par=36, ext="c",
    task="After each fopen line, add a check that uses its variable: if (!in) return -1; for "
         "FILE *in = fopen(...);",
    start=text("""
        int copy(const char *src, const char *dst) {
            FILE *in = fopen(src, "rb");
            char buf[4096];
            FILE *out = fopen(dst, "wb");
            size_t n;
            FILE *log = fopen("copy.log", "a");
            while ((n = fread(buf, 1, sizeof buf, in)) > 0)
                fwrite(buf, 1, n, out);
            return 0;
        }
    """),
    target=text("""
        int copy(const char *src, const char *dst) {
            FILE *in = fopen(src, "rb");
            if (!in) return -1;
            char buf[4096];
            FILE *out = fopen(dst, "wb");
            if (!out) return -1;
            size_t n;
            FILE *log = fopen("copy.log", "a");
            if (!log) return -1;
            while ((n = fread(buf, 1, sizeof buf, in)) > 0)
                fwrite(buf, 1, n, out);
            return 0;
        }
    """),
    hint="The fopen lines aren't next to each other, so start the macro with a search for fopen. The "
         "variable is two words back (the = is a word of its own): yank it, and o types the check with "
         "Ctrl-r 0.",
    uses=["search", "line", "f", "y", "iw", "o", "ctrl-r", "count"],
)
macro.add(
    title="Two lines become one link", par=23, ext="md",
    task="Turn each name/url pair into one Markdown list item: - [Garden](https://garden.dev)",
    start=text("""
        - name: Garden
          url: https://garden.dev
        - name: Docs
          url: https://docs.garden.dev
        - name: Blog
          url: https://blog.garden.dev
        - name: Status
          url: https://status.garden.dev
    """),
    target=text("""
        - [Garden](https://garden.dev)
        - [Docs](https://docs.garden.dev)
        - [Blog](https://blog.garden.dev)
        - [Status](https://status.garden.dev)
    """),
    hint="6s replaces name: and its space with [, and ea]( closes the bracket. Then J joins the url line "
         "on and leaves the cursor at the join, right where 2dW deletes the space and url: . A) closes "
         "the link and + moves to the next pair.",
    uses=["c", "count", "word", "insert", "join", "d", "bigword", "plus"],
)

# ---------- @@ {N}@ ----------

replay = drills.command(
    "replay", "@@  Q  {N}@{r}", "play a macro again, or N times",
    """Q plays the macro you recorded last, and @@ the macro you played last: after recording a and then b,
    Q always plays b, while @a followed by @@ plays a twice. Both take a count, as @a does: 9Q plays the
    macro nine times in a row, the way to go when it moves on to its next target itself. If any key
    fails (an f that finds nothing, j or + on the last line, a search with no match), that run stops and
    the rest of the count is cancelled, so 99Q means "until it fails", which is safe as long as the
    macro fails before it changes anything. u undoes a whole counted run in one step.""",
    examples=[("Q", "play the macro recorded last"), ("@@", "play the macro played last, again"),
              ("9Q", "play it nine times"), ("99Q", "play it until a key fails"),
              ("j3@@", "skip a line, then the last played macro three times")],
)
replay.add(
    title="Check off three tasks", par=22, ext="md",
    task="You finished write the parser, add tests and fix the CI cache. Check those three boxes and "
         "strike their text through: - [x] ~~add tests~~",
    start=text("""
        - [ ] write the parser
        - [ ] add tests
        - [ ] update the README
        - [ ] tag a release
        - [ ] fix the CI cache
        - [ ] email the reviewers
    """),
    target=text("""
        - [x] ~~write the parser~~
        - [x] ~~add tests~~
        - [ ] update the README
        - [ ] tag a release
        - [x] ~~fix the CI cache~~
        - [ ] email the reviewers
    """),
    hint="Record the first task, ending with +. Q plays it on the second. Then 2+ skips two tasks, "
         "and Q again does the fifth.",
    uses=["macro", "f", "r", "bigword", "insert", "plus"],
)
replay.add(
    title="Two kinds of rows", par=34, ext="py",
    task='Turn each row into a keyword argument. Text values get quotes (host="localhost",), numbers '
         "don't (port=8080,). Leave the comment as it is.",
    start=text("""
        SETTINGS = dict(
            host,localhost
            port,8080
            user,admin
            # logging
            log_level,info
            log_file,/var/log/app.log
            timeout,30
            retries,3
        )
    """),
    target=text("""
        SETTINGS = dict(
            host="localhost",
            port=8080,
            user="admin",
            # logging
            log_level="info",
            log_file="/var/log/app.log",
            timeout=30,
            retries=3,
        )
    """),
    hint="You need two macros: record a on host (quotes) and b on port (no quotes), both ending with +. "
         "Now Q plays b, the one recorded last, so play a with @a. After stepping over the comment, @@ "
         "repeats the macro you played last (a), and a count works on it too. Q does the numbers.",
    uses=["macro", "plus", "f", "c", "r", "insert", "count"],
)
replay.add(
    title="Ten rows, one count", par=18, ext="js",
    task='Turn every row into an object property: py: "Python",',
    start=text("""
        const LANGUAGES = {
            py,Python
            java,Java
            c,C
            h,C
            rs,Rust
            js,JavaScript
            ts,TypeScript
            md,Markdown
            sh,Shell
            lua,Lua
        };
    """),
    target=text("""
        const LANGUAGES = {
            py: "Python",
            java: "Java",
            c: "C",
            h: "C",
            rs: "Rust",
            js: "JavaScript",
            ts: "TypeScript",
            md: "Markdown",
            sh: "Shell",
            lua: "Lua",
        };
    """),
    hint="Record the first row, ending with + so the macro sets up the next one. Then a count plays it "
         "for the other nine: 9Q is two keys, nine separate Qs would be nine.",
    uses=["macro", "plus", "f", "c", "insert"],
)
replay.add(
    title="Don't count, run until done", par=25, ext="java",
    task='Turn every row into a pair of strings: {"fr", "Paris"},',
    start=text("""
        String[][] CAPITALS = {
            fr,Paris
            de,Berlin
            it,Rome
            es,Madrid
            pt,Lisbon
            nl,Amsterdam
            be,Brussels
            at,Vienna
            ch,Bern
            se,Stockholm
            no,Oslo
            fi,Helsinki
        };
    """),
    target=text("""
        String[][] CAPITALS = {
            {"fr", "Paris"},
            {"de", "Berlin"},
            {"it", "Rome"},
            {"es", "Madrid"},
            {"pt", "Lisbon"},
            {"nl", "Amsterdam"},
            {"be", "Brussels"},
            {"at", "Vienna"},
            {"ch", "Bern"},
            {"se", "Stockholm"},
            {"no", "Oslo"},
            {"fi", "Helsinki"},
        };
    """),
    hint="Make the macro fail before it changes anything: start it with f, (the }; line has no comma). "
         "Then 99Q runs it until it reaches that line, and stops.",
    uses=["macro", "plus", "f", "c", "insert"],
)
replay.add(
    title="To the end of the log", par=16, ext="log",
    task="Shorten every log line: [2026-10-21 09:14:07] INFO: server started becomes "
         "09:14:07 INFO server started",
    start=text("""
        [2026-10-21 09:14:07] INFO: server started
        [2026-10-21 09:14:09] INFO: listening on :8080
        [2026-10-21 09:15:32] WARN: slow request: /api/users
        [2026-10-21 09:15:40] INFO: cache warmed
        [2026-10-21 09:16:02] ERROR: database timeout
        [2026-10-21 09:16:03] INFO: retrying
        [2026-10-21 09:16:05] INFO: database connected
        [2026-10-21 09:17:44] WARN: disk at 91%
        [2026-10-21 09:18:10] INFO: backup started
        [2026-10-21 09:21:37] INFO: backup done
        [2026-10-21 09:22:00] INFO: shutting down
    """),
    target=text("""
        09:14:07 INFO server started
        09:14:09 INFO listening on :8080
        09:15:32 WARN slow request: /api/users
        09:15:40 INFO cache warmed
        09:16:02 ERROR database timeout
        09:16:03 INFO retrying
        09:16:05 INFO database connected
        09:17:44 WARN disk at 91%
        09:18:10 INFO backup started
        09:21:37 INFO backup done
        09:22:00 INFO shutting down
    """),
    hint="df<Space> deletes the date, f]x the bracket, and f:x the colon after the level. End with +: "
         "on the last line + fails, so 99Q stops by itself at the end of the file.",
    uses=["macro", "d", "f", "x", "plus", "count"],
)
replay.add(
    title="Sign every TODO", par=22, ext="py",
    task="Put your name on every TODO: # TODO(rick): retry on timeout",
    start=text("""
        def connect(host, port):
            # TODO retry on timeout
            sock = socket.create_connection((host, port))
            # TODO make the timeout configurable
            sock.settimeout(5)
            return sock


        def send(sock, data):
            # TODO compress large payloads
            sock.sendall(data)
            # TODO log the byte count
    """),
    target=text("""
        def connect(host, port):
            # TODO(rick): retry on timeout
            sock = socket.create_connection((host, port))
            # TODO(rick): make the timeout configurable
            sock.settimeout(5)
            return sock


        def send(sock, data):
            # TODO(rick): compress large payloads
            sock.sendall(data)
            # TODO(rick): log the byte count
    """),
    hint="Start the macro with a search for /TODO<Space><CR>, so each run finds the next one. e and "
         "a(rick): sign it. A count plays it for the other three.",
    uses=["macro", "search", "word", "insert"],
)
replay.add(
    title="Skip the commented row", par=20, ext="lua",
    task="Turn every row into a field like alice = 92, but leave the commented-out row as it is.",
    start=text("""
        local scores = {
            alice,92
            bob,85
            carol,78
            -- mallory,99
            dave,64
            erin,88
            frank,71
            grace,95
        }
    """),
    target=text("""
        local scores = {
            alice = 92,
            bob = 85,
            carol = 78,
            -- mallory,99
            dave = 64,
            erin = 88,
            frank = 71,
            grace = 95,
        }
    """),
    hint="Record the first row ending with +, and a count does the next two. The macro would happily "
         "convert the comment too, so step over it with +, then 4Q plays the macro four more times.",
    uses=["macro", "plus", "f", "c", "insert", "count"],
)
replay.add(
    title="Build the staircase", par=13,
    task="Extend the staircase to eight steps. Each step is the one above it, two spaces further right.",
    start=text("""
        _
         |_
    """),
    target=text("""
        _
         |_
           |_
             |_
               |_
                 |_
                   |_
                     |_
    """),
    hint="Record on the second row: yyp copies it, and I<Space><Space> indents the copy. The cursor ends "
         "on the new step, so each replay copies the step the last one made. Six more steps: 5Q.",
    uses=["macro", "y", "p", "insert"],
)
replay.add(
    title="Count runs, not lines", par=10, ext="yaml",
    task="Join each key with the value on the line below it: name: Ada Lovelace",
    start=text("""
        name
        Ada Lovelace
        born
        1815
        field
        mathematics
        known for
        the first published algorithm
    """),
    target=text("""
        name: Ada Lovelace
        born: 1815
        field: mathematics
        known for: the first published algorithm
    """),
    hint="A:<Esc>J adds the colon and joins the value on (J puts a space between). + moves to the next "
         "key. Each run eats two lines, so the count is the number of pairs left, not lines.",
    uses=["macro", "insert", "join", "plus", "count"],
)
replay.add(
    title="Three lines per contact", par=18, ext="csv",
    task="Turn each contact into one CSV row: Ada Lovelace,ada@ex.io,+44 20 7946 0001 "
         "(no blank lines between the rows).",
    start=text("""
        Ada Lovelace
        ada@ex.io
        +44 20 7946 0001

        Alan Turing
        alan@ex.io
        +44 20 7946 0002

        Grace Hopper
        grace@ex.io
        +1 212 555 0100

        Linus Torvalds
        linus@ex.io
        +1 503 555 0199
    """),
    target=text("""
        Ada Lovelace,ada@ex.io,+44 20 7946 0001
        Alan Turing,alan@ex.io,+44 20 7946 0002
        Grace Hopper,grace@ex.io,+1 212 555 0100
        Linus Torvalds,linus@ex.io,+1 503 555 0199
    """),
    hint="A,<Esc>gJ adds a comma and joins the next line without a space. Do that twice, then jdd "
         "deletes the blank line and leaves you on the next contact. Each run handles one contact.",
    uses=["macro", "insert", "gjoin", "dd", "count"],
)
replay.add(
    title="Export them all", par=23, ext="sh",
    task="Export every setting, with its value quoted: export DB_HOST=\"localhost\"",
    start=text("""
        DB_HOST=localhost
        DB_PORT=5432
        DB_USER=garden
        DB_NAME=garden_prod
        CACHE_URL=redis://localhost:6379
        LOG_LEVEL=info
        SENTRY_DSN=https://key@sentry.example/12
        FEATURE_FLAGS=beta,dark-mode
    """),
    target=text("""
        export DB_HOST="localhost"
        export DB_PORT="5432"
        export DB_USER="garden"
        export DB_NAME="garden_prod"
        export CACHE_URL="redis://localhost:6379"
        export LOG_LEVEL="info"
        export SENTRY_DSN="https://key@sentry.example/12"
        export FEATURE_FLAGS="beta,dark-mode"
    """),
    hint="Record line 1: Iexport , then f= and a\" open the quote, and A\" closes it. End with j. Seven lines "
         "are left, so a count of 7 plays it on all of them in two keys.",
    uses=["macro", "insert", "f", "count"],
)
replay.add(
    title="Grow the tree", par=14,
    task="Grow the tree to five rows. Each row is the one above it, one space further left and two stars "
         "wider.",
    start="    *",
    target=text("""
            *
           ***
          *****
         *******
        *********
    """),
    hint="yyp copies the row, 0x deletes one of its leading spaces, and A** widens it. The cursor ends on "
         "the new row, so the next run copies that one. Count the rows still to make, not the ones you "
         "have.",
    uses=["macro", "y", "p", "line", "x", "insert", "count"],
)
replay.add(
    title="Links and plain names", par=37, ext="md",
    task="Rows with a URL become links: - [garden](https://garden.dev). Rows without one become bold: "
         "- **roadmap**.",
    start=text("""
        - garden https://garden.dev
        - docs https://docs.garden.dev
        - roadmap
        - blog https://blog.garden.dev
        - changelog
        - faq
        - status https://status.garden.dev
    """),
    target=text("""
        - [garden](https://garden.dev)
        - [docs](https://docs.garden.dev)
        - **roadmap**
        - [blog](https://blog.garden.dev)
        - **changelog**
        - **faq**
        - [status](https://status.garden.dev)
    """),
    hint="Two macros, both ending with +: a for a link row, b for a bold one. Q plays the one you recorded "
         "last, so once b exists, link rows need @a.",
    uses=["macro", "word", "insert", "f", "c", "plus", "count"],
)
replay.add(
    title="Some rows are done", par=27, ext="c",
    task="Finish the command table: add,cmd_add becomes { \"add\", cmd_add },. The rows already in braces "
         "stay as they are.",
    start=text("""
        static const struct cmd cmds[] = {
            { "help", cmd_help },
            add,cmd_add
            rm,cmd_rm
            { "ls", cmd_ls },
            mv,cmd_mv
            cp,cmd_cp
            cat,cmd_cat
            { "quit", cmd_quit },
        };
    """),
    target=text("""
        static const struct cmd cmds[] = {
            { "help", cmd_help },
            { "add", cmd_add },
            { "rm", cmd_rm },
            { "ls", cmd_ls },
            { "mv", cmd_mv },
            { "cp", cmd_cp },
            { "cat", cmd_cat },
            { "quit", cmd_quit },
        };
    """),
    hint="Record on add, ending with +, and Q does rm. The macro wouldn't fail on a finished row (it has a "
         "comma too), so step over { \"ls\" ... } with +, then a count does the next three.",
    uses=["macro", "insert", "f", "c", "plus", "count"],
)
replay.add(
    title="Stop at the blank line", par=20, ext="md",
    task="Bold every glossary term: buffer,a file loaded into memory becomes **buffer**: a file loaded "
         "into memory. The CSV in the code block below must stay as it is.",
    start=text("""
        ## Glossary
        buffer,a file loaded into memory
        window,a view on a buffer
        tab,a collection of windows
        register,a named clipboard
        macro,keys saved in a register
        mark,a saved position
        jump,a position you can go back to
        count,a number in front of a command
        motion,a command that moves the cursor
        operator,a command that works on a motion
        textobject,a thing like a word or a paragraph

        ```csv
        term,uses
        buffer,12
        ```
    """),
    target=text("""
        ## Glossary
        **buffer**: a file loaded into memory
        **window**: a view on a buffer
        **tab**: a collection of windows
        **register**: a named clipboard
        **macro**: keys saved in a register
        **mark**: a saved position
        **jump**: a position you can go back to
        **count**: a number in front of a command
        **motion**: a command that moves the cursor
        **operator**: a command that works on a motion
        **textobject**: a thing like a word or a paragraph

        ```csv
        term,uses
        buffer,12
        ```
    """),
    hint="Start the macro with f,: on the blank line it fails before changing anything, so 99Q stops "
         "there and never reaches the CSV, and you don't have to count the terms. Then s**: replaces the "
         "comma and I** opens the bold. End with +.",
    uses=["macro", "f", "c", "insert", "plus", "count"],
)
replay.add(
    title="One row, three lines", par=40, ext="yaml",
    task="Turn each CSV row into a YAML list item with three keys (name, role, team), indented as in the "
         "target.",
    start=text("""
        ada,dev,core
        grace,lead,compilers
        linus,ops,kernel
        ken,dev,unix
    """),
    target=text("""
        - name: ada
          role: dev
          team: core
        - name: grace
          role: lead
          team: compilers
        - name: linus
          role: ops
          team: kernel
        - name: ken
          role: dev
          team: unix
    """),
    hint="I- name:  starts the item. f, and s with Enter replace each comma with a line break, and you type "
         "the next key there: with two spaces for role, while team gets them from the line above "
         "(autoindent). + then lands on the next row, however many lines the run made, so the count is "
         "the rows left.",
    uses=["macro", "insert", "f", "c", "plus", "count"],
)
replay.add(
    title="Every other line", par=15, ext="md",
    task="Make every question bold: **Q: How do I install it?** The answers stay as they are.",
    start=text("""
        Q: How do I install it?
        A: pip install garden
        Q: Where is the config?
        A: ~/.config/garden/config.toml
        Q: Does it run on Windows?
        A: Yes, in WSL.
        Q: Can I change the colors?
        A: Set theme in the config.
    """),
    target=text("""
        **Q: How do I install it?**
        A: pip install garden
        **Q: Where is the config?**
        A: ~/.config/garden/config.toml
        **Q: Does it run on Windows?**
        A: Yes, in WSL.
        **Q: Can I change the colors?**
        A: Set theme in the config.
    """),
    hint="I** and A** bold the question, and 2j skips the answer to land on the next question. A count "
         "does the other three.",
    uses=["macro", "insert", "count"],
)
replay.add(
    title="Added and removed", par=43, ext="md",
    task="Label each changelog entry: + new plugin API becomes - **Added:** new plugin API, and "
         "- old config format becomes - **Removed:** old config format.",
    start=text("""
        + new plugin API
        + faster startup
        - old config format
        - the legacy importer
        + dark mode
        + a --dry-run flag
        + Windows builds
    """),
    target=text("""
        - **Added:** new plugin API
        - **Added:** faster startup
        - **Removed:** old config format
        - **Removed:** the legacy importer
        - **Added:** dark mode
        - **Added:** a --dry-run flag
        - **Added:** Windows builds
    """),
    hint="Two macros: a for a + line and b for a - line, both ending with +. Q plays b, the one you "
         "recorded last, so for the last group of + lines, play a by name, with a count.",
    uses=["macro", "r", "insert", "plus", "count"],
)
replay.add(
    title="Move first, then edit", par=14, ext="py",
    task="Port the prints to Python 3: print \"done\" becomes print(\"done\"). Line 1 is already done, and "
         "leave the bare print on the last line for later.",
    start=text("""
        print("loading")
        print "parsed", len(rows), "rows"
        print "skipped", skipped
        print "writing", out_path
        print "done"
        print "elapsed", time.time() - start
        print "workers", workers
        print "retries", retries
        print "cache hits", hits
        print "cache misses", misses
        print "bye"
        print
    """),
    target=text("""
        print("loading")
        print("parsed", len(rows), "rows")
        print("skipped", skipped)
        print("writing", out_path)
        print("done")
        print("elapsed", time.time() - start)
        print("workers", workers)
        print("retries", retries)
        print("cache hits", hits)
        print("cache misses", misses)
        print("bye")
        print
    """),
    hint="Make the macro start with + and then edit: f<Space> and r( open the call, A) closes it. The "
         "bare print has no space, so f<Space> fails there before anything changes, and 99Q stops by "
         "itself: no counting.",
    uses=["macro", "plus", "f", "r", "insert", "count"],
)
replay.add(
    title="Routes from a table", par=31, ext="js",
    task="Turn every row into a route: get,/users,listUsers becomes router.get(\"/users\", listUsers);",
    start=text("""
        get,/users,listUsers
        post,/users,createUser
        get,/users/:id,getUser
        put,/users/:id,updateUser
        delete,/users/:id,deleteUser
        get,/health,health
    """),
    target=text("""
        router.get("/users", listUsers);
        router.post("/users", createUser);
        router.get("/users/:id", getUser);
        router.put("/users/:id", updateUser);
        router.delete("/users/:id", deleteUser);
        router.get("/health", health);
    """),
    hint="One macro does a row: Irouter. adds the prefix, f,s(\" and ;s\", replace the two commas, and "
         "A); finishes the call. End with + and count the rows left.",
    uses=["macro", "insert", "f", "c", "semicolon", "plus", "count"],
)

# ---------- :norm @ ----------

norm_macro = drills.command(
    "norm-macro", ":norm @{r}", "run a macro on every line of a range",
    """:normal runs Normal-mode keys once for each line of a range, starting in column 1 of each line, so
    :%norm @a plays macro a on every line and the macro needs no 0 or j (:%norm Q plays the macro you
    recorded last). Unlike a count, a failure only skips that line, so a macro that fails before it
    changes anything works as a filter. The range can be line numbers (:5,12norm @a), the Visual
    selection (press : in Visual mode and '<,'> is typed for you), or :g/pat/norm @a for the lines
    matching a pattern; :g marks its lines first, so use it when the macro adds or deletes lines.
    Careful: the line you recorded on is in the range too, so the macro must fail there, or the range
    must leave it out.""",
    examples=[(":%norm @a", "macro a on every line"), (":%norm Q", "the last recorded macro on every line"),
              (":5,12norm @a", "on lines 5 to 12"),
              ("vip:norm @a", "on the lines of this paragraph"), (":g/TODO/norm @a", "on every line with TODO")],
)
norm_macro.add(
    title="Only the complete rows", par=36, ext="txt",
    task="Turn each contact into a mutt alias: alias ada Ada Lovelace <ada@ex.io>. The rows without an "
         "email address stay exactly as they are, so you can fix them by hand.",
    start=text("""
        ada,Ada,Lovelace,ada@ex.io
        alan,Alan,Turing,alan@ex.io
        grace,Grace,Hopper
        linus,Linus,Torvalds,linus@ex.io
        ken,Ken,Thompson
        barbara,Barbara,Liskov,liskov@ex.io
        dennis,Dennis,Ritchie
        bjarne,Bjarne,Stroustrup,bjarne@ex.io
    """),
    target=text("""
        alias ada Ada Lovelace <ada@ex.io>
        alias alan Alan Turing <alan@ex.io>
        grace,Grace,Hopper
        alias linus Linus Torvalds <linus@ex.io>
        ken,Ken,Thompson
        alias barbara Barbara Liskov <liskov@ex.io>
        dennis,Dennis,Ritchie
        alias bjarne Bjarne Stroustrup <bjarne@ex.io>
    """),
    hint="Start the macro with 3f, so it fails on a row with only two commas before changing anything "
         "(and on a converted row, which has none). Then :%norm Q runs it on every line and skips the "
         "rows where it fails. A count would stop for good at grace.",
    uses=["count", "f", "c", "insert", "r", "semicolon", "dot"],
)
norm_macro.add(
    title="Points with three coordinates", par=38, ext="py",
    task="Turn each 3D point into a Vec3: spawn = Vec3(12, 0, -4). Rows with only two coordinates are "
         "bad data: leave them alone.",
    start=text("""
        origin,0,0,0
        spawn,12,0,-4
        door,3,1
        camera,0,8,-15
        light,5,10
        exit,40,0,22
    """),
    target=text("""
        origin = Vec3(0, 0, 0)
        spawn = Vec3(12, 0, -4)
        door,3,1
        camera = Vec3(0, 8, -15)
        light,5,10
        exit = Vec3(40, 0, 22)
    """),
    hint="3f, is only a test here: it fails on a row with fewer than three commas, and on a finished "
         "row (it has two). Then 0f, starts over at the first comma: s = Vec3(, then f,a<Space> and ;. "
         "space out the other two commas, and A) closes the call. Run it with :%norm Q.",
    uses=["count", "f", "line", "c", "insert", "semicolon", "dot"],
)
norm_macro.add(
    title="A half-finished hosts file", par=30, ext="conf",
    task="Someone started converting this list into hosts-file lines like 10.0.0.11 web1 # web. Finish "
         "the job. Rows without a role, the comments and the finished lines stay as they are.",
    start=text("""
        # production
        10.0.0.11 web1 # web
        web2,10.0.0.12,web
        db1,10.0.0.21
        cache1,10.0.0.31,redis

        # staging
        web1,10.1.0.11,web
        10.1.0.21 db1 # postgres
        queue1,10.1.0.41
        mail1,10.1.0.51,smtp
    """),
    target=text("""
        # production
        10.0.0.11 web1 # web
        10.0.0.12 web2 # web
        db1,10.0.0.21
        10.0.0.31 cache1 # redis

        # staging
        10.1.0.11 web1 # web
        10.1.0.21 db1 # postgres
        queue1,10.1.0.41
        10.1.0.51 mail1 # smtp
    """),
    hint="Record on web2. 2f, finds the second comma, and fails on a row with only one (and on finished "
         "lines, which have none). s # <Esc> replaces it. , goes back to the first comma: r<Space> turns "
         "it into a space, then wdW cuts the address and 0P puts it at the start. Finish with :%norm Q.",
    uses=["count", "f", "c", "semicolon", "r", "word", "d", "bigword", "line", "p"],
)
norm_macro.add(
    title="Only this season", par=34, ext="md", cursor=(3, 1),
    task="Turn the complete 2026 rows into Markdown table rows: | ajax | 3 | 1 | 0 |. Leave the rows "
         "with a missing number, and all of 2025, as they are. The cursor starts on the first 2026 row.",
    start=text("""
        ## 2026

        ajax,3,1,0
        benfica,2,2
        celtic,1,3,0
        dortmund,0,4
        everton,2,1,1
        feyenoord,3,0,1

        ## 2025

        ajax,2,2,0
        benfica,4,0,0
    """),
    target=text("""
        ## 2026

        | ajax | 3 | 1 | 0 |
        benfica,2,2
        | celtic | 1 | 3 | 0 |
        dortmund,0,4
        | everton | 2 | 1 | 1 |
        | feyenoord | 3 | 0 | 1 |

        ## 2025

        ajax,2,2,0
        benfica,4,0,0
    """),
    hint="Record on ajax, starting with 3f, so the macro fails on short rows and finished ones. Then vip "
         "selects this paragraph, and : in Visual mode types :'<,'> for you: norm Q<CR> runs the macro on "
         "just those lines.",
    uses=["visual", "ip", "count", "f", "c", "semicolon", "dot", "insert"],
)
norm_macro.add(
    title="Inside one enum", par=36, ext="c", cursor=(2, 1),
    task="In enum color only, turn each complete row into RED = 0xff0000, /* primary */. Rows without a "
         "group, and enum legacy_color, stay as they are. The cursor starts on RED.",
    start=text("""
        enum color {
            RED,0xff0000,primary
            GREEN,0x00ff00,primary
            TEAL,0x008080
            BLUE,0x0000ff,primary
            ORANGE,0xffa500,secondary
        };

        enum legacy_color {
            MAROON,0x800000,web
            NAVY,0x000080,web
        };
    """),
    target=text("""
        enum color {
            RED = 0xff0000, /* primary */
            GREEN = 0x00ff00, /* primary */
            TEAL,0x008080
            BLUE = 0x0000ff, /* primary */
            ORANGE = 0xffa500, /* secondary */
        };

        enum legacy_color {
            MAROON,0x800000,web
            NAVY,0x000080,web
        };
    """),
    hint="2f, fails on TEAL and on finished rows (they have one comma). a /* and A */ add the comment, "
         "then F, and ; reach the first comma for s = . vi{ selects the inside of this enum, and :norm Q "
         "runs the macro on those lines.",
    uses=["visual", "brace", "count", "f", "insert", "semicolon", "c"],
)
norm_macro.add(
    title="Just the prod hosts", par=42, ext="py",
    task='Turn the prod rows into Host("web1", "10.0.0.11", "web"),. The row without a role stays as it '
         'is, and so does the dev list.',
    start=text("""
        HOSTS = {
            "prod": [
                web1,10.0.0.11,web
                db1,10.0.0.21
                cache1,10.0.0.31,redis
                web2,10.0.0.12,web
            ],
            "dev": [
                web1,10.1.0.11,web
                db1,10.1.0.21,postgres
            ],
        }
    """),
    target=text("""
        HOSTS = {
            "prod": [
                Host("web1", "10.0.0.11", "web"),
                db1,10.0.0.21
                Host("cache1", "10.0.0.31", "redis"),
                Host("web2", "10.0.0.12", "web"),
            ],
            "dev": [
                web1,10.1.0.11,web
                db1,10.1.0.21,postgres
            ],
        }
    """),
    hint="Record on web1, starting with 2f, so db1 fails. A finished row still has two commas, so leave "
         "line 3 out of the range: :4,6norm Q runs the macro on lines 4 to 6 only. (With relative line "
         "numbers, line 4 is 1 below line 3 and line 6 is 3 below.)",
    uses=["range", "count", "f", "c", "semicolon", "dot", "insert"],
)
norm_macro.add(
    title="Prints to logging", par=41, ext="py",
    task='Replace every debug print with a logging call: print("loaded", n) becomes '
         'log.debug("loaded %s", n).',
    start=text("""
        def load(path):
            print("loading", path)
            with open(path) as f:
                rows = f.readlines()
                print("read", len(rows))
            data = parse(rows)
            if not data:
                print("empty file", path)
            return data
    """),
    target=text("""
        def load(path):
            log.debug("loading %s", path)
            with open(path) as f:
                rows = f.readlines()
                log.debug("read %s", len(rows))
            data = parse(rows)
            if not data:
                log.debug("empty file %s", path)
            return data
    """),
    hint="Record on the first print: ^ (:g starts each line in column 1, before the indent), cw to type "
         "log.debug over print, then 2f\" and i %s. Then :g/print/norm Q runs it on every line with a "
         "print. The finished line doesn't match any more, so it's left alone.",
    uses=["global", "line", "c", "count", "f", "insert"],
)
norm_macro.add(
    title="Alerts from the errors", par=39, ext="csv",
    task="Turn the complete ERROR rows into alerts: !! 09:14:09 db: timeout. Leave the ERROR row with "
         "no message, and every other row, as they are.",
    start=text("""
        time,level,component,message
        09:14:07,INFO,web,started
        09:14:09,ERROR,db,timeout
        09:15:32,WARN,web,slow request
        09:15:40,ERROR,cache
        09:16:02,ERROR,db,connection refused
        09:16:03,INFO,db,retrying
        09:17:44,ERROR,disk,full
    """),
    target=text("""
        time,level,component,message
        09:14:07,INFO,web,started
        !! 09:14:09 db: timeout
        09:15:32,WARN,web,slow request
        09:15:40,ERROR,cache
        !! 09:16:02 db: connection refused
        09:16:03,INFO,db,retrying
        !! 09:17:44 disk: full
    """),
    hint="The rows to change match a pattern (ERROR) and a filter (three commas). Let :g pick the "
         "ERROR lines and let 3f, at the start of the macro skip the short one. From the third comma: "
         "s: <Esc>, then , goes back to the second, dF, deletes ,ERROR and r<Space> fixes the comma.",
    uses=["global", "count", "f", "c", "semicolon", "d", "r", "insert"],
)
norm_macro.add(
    title="Bold the glossary terms", par=28, ext="md",
    task="Turn each list item into a bold term: - buffer: a file... becomes **buffer**: a file... "
         "Every other line stays as it is.",
    start=text("""
        # Glossary

        Words you'll meet in this course.

        - buffer: a file loaded into memory
        - window: a view on a buffer

        Modes:

        - normal: where keys are commands
        - insert: where keys type text
        - visual: where keys select text
    """),
    target=text("""
        # Glossary

        Words you'll meet in this course.

        **buffer**: a file loaded into memory
        **window**: a view on a buffer

        Modes:

        **normal**: where keys are commands
        **insert**: where keys type text
        **visual**: where keys select text
    """),
    hint="Record on the first item: 2x deletes the dash and space, i** opens the bold, and f: with . "
         "closes it. The other lines would be mangled by that macro, so let :g/^- /norm Q pick the list "
         "items. The finished item no longer starts with -, so it's skipped.",
    uses=["global", "count", "x", "insert", "f", "dot"],
)
norm_macro.add(
    title="Teams in YAML", par=42, ext="yaml",
    task="Turn each complete row into a YAML mapping: ada: {role: dev, team: core}. Rows without a team, "
         "comments and blank lines stay as they are.",
    start=text("""
        # core
        ada,dev,core
        grace,lead
        barbara,dev,core

        # infra
        linus,ops,infra
        ken,dev
        dennis,dev,infra
        bjarne,ops,infra
    """),
    target=text("""
        # core
        ada: {role: dev, team: core}
        grace,lead
        barbara: {role: dev, team: core}

        # infra
        linus: {role: ops, team: infra}
        ken,dev
        dennis: {role: dev, team: infra}
        bjarne: {role: ops, team: infra}
    """),
    hint="2f, makes the macro fail first on short rows, comments and finished rows (they have one "
         "comma). Then , goes back to the first comma and ; forward to the second again. Record on ada "
         "and run :%norm Q.",
    uses=["count", "f", "semicolon", "c", "insert"],
)
norm_macro.add(
    title="Only the complete log rows", par=30, ext="log",
    task="Turn each complete row (five fields) into 09:14:07 web-03 ERROR: db timeout. Rows with missing "
         "fields stay exactly as they are.",
    start=text("""
        2026-11-05,09:14:07,web-03,ERROR,db timeout
        2026-11-05,09:14:09,web-01,INFO
        2026-11-05,09:15:32,web-03,WARN,slow request
        2026-11-05,09:15:40,web-02,INFO,cache warmed
        2026-11-05,09:16:02
        2026-11-05,09:16:03,db-01,INFO,retrying
        2026-11-05,09:17:44,db-01,ERROR
        2026-11-05,09:18:10,web-02,INFO,backup started
        2026-11-05,09:19:00,web-02
        2026-11-05,09:21:37,web-02,INFO,backup done
        2026-11-05,09:22:00,web-01,WARN
        2026-11-05,09:22:05,web-01,INFO,shutting down
    """),
    target=text("""
        09:14:07 web-03 ERROR: db timeout
        2026-11-05,09:14:09,web-01,INFO
        09:15:32 web-03 WARN: slow request
        09:15:40 web-02 INFO: cache warmed
        2026-11-05,09:16:02
        09:16:03 db-01 INFO: retrying
        2026-11-05,09:17:44,db-01,ERROR
        09:18:10 web-02 INFO: backup started
        2026-11-05,09:19:00,web-02
        09:21:37 web-02 INFO: backup done
        2026-11-05,09:22:00,web-01,WARN
        09:22:05 web-01 INFO: shutting down
    """),
    hint="Start the macro with 4f,: it fails on a row with fewer than four commas before changing anything "
         "(and on a finished row, which has none). s: replaces that comma, 0df, deletes the date, and f,r "
         "and ;r turn the other two commas into spaces. :%norm Q runs it on every line and skips the rest.",
    uses=["count", "f", "c", "line", "d", "r", "semicolon"],
)
norm_macro.add(
    title="Priced items only", par=29,
    task="Reformat each row that has all four fields (sku;item;qty;price): A-100;mug;12;4.50 becomes "
         "A-100 mug x12 = 4.50. Rows with missing fields, and the comments, stay as they are.",
    start=text("""
        # warehouse export: sku, item, qty, price
        A-100;mug;12;4.50
        A-101;teapot;3
        A-102;saucer;40;1.20
        # discontinued
        A-104;tray;6;12.00
        A-105;kettle
        A-106;cup;24;3.75
        A-107;lid
        A-108;jar;2;0.95
        # returns
        A-109;plate;1;6.20
    """),
    target=text("""
        # warehouse export: sku, item, qty, price
        A-100 mug x12 = 4.50
        A-101;teapot;3
        A-102 saucer x40 = 1.20
        # discontinued
        A-104 tray x6 = 12.00
        A-105;kettle
        A-106 cup x24 = 3.75
        A-107;lid
        A-108 jar x2 = 0.95
        # returns
        A-109 plate x1 = 6.20
    """),
    hint="3f; is the test and the first move: it fails on rows with fewer than three semicolons. s = "
         "replaces that one, and , (the f; backward) reaches the one before it for s x, then the first one "
         "for r<Space>. :%norm Q does the rest.",
    uses=["count", "f", "c", "semicolon", "r"],
)
norm_macro.add(
    title="Rows inside the table body", par=57, ext="html", setup=["setlocal indentexpr="], cursor=(6, 1),
    task="Turn each complete row in <tbody> (five fields) into a table row: "
         "<tr><td>ada</td><td>dev</td><td>core</td><td>2019</td><td>yes</td></tr>. Short rows stay, and "
         "so does the raw data in <pre>. The cursor starts on the first row.",
    start=text("""
        <table>
          <thead>
            <tr><th>name</th><th>role</th><th>team</th><th>since</th><th>remote</th></tr>
          </thead>
          <tbody>
            ada,dev,core,2019,yes
            grace,lead,compilers,2016
            linus,ops,kernel,2021,no
            ken,dev,unix,2017,yes
            barbara,dev
            dennis,dev,unix,2018,no
            bjarne,dev,cpp
            margaret,lead,apollo,2015,yes
            alan,research
            edsger,research,algol,2020,no
            frances,research,ptran,2012,yes
            niklaus,dev,pascal
            john,research,lisp,2011,no
            tony,research
            radia,ops,stp,2022,yes
          </tbody>
        </table>
        <pre>
        ada,dev,core,2019,yes
        linus,ops,kernel,2021,no
        </pre>
    """),
    target=text("""
        <table>
          <thead>
            <tr><th>name</th><th>role</th><th>team</th><th>since</th><th>remote</th></tr>
          </thead>
          <tbody>
            <tr><td>ada</td><td>dev</td><td>core</td><td>2019</td><td>yes</td></tr>
            grace,lead,compilers,2016
            <tr><td>linus</td><td>ops</td><td>kernel</td><td>2021</td><td>no</td></tr>
            <tr><td>ken</td><td>dev</td><td>unix</td><td>2017</td><td>yes</td></tr>
            barbara,dev
            <tr><td>dennis</td><td>dev</td><td>unix</td><td>2018</td><td>no</td></tr>
            bjarne,dev,cpp
            <tr><td>margaret</td><td>lead</td><td>apollo</td><td>2015</td><td>yes</td></tr>
            alan,research
            <tr><td>edsger</td><td>research</td><td>algol</td><td>2020</td><td>no</td></tr>
            <tr><td>frances</td><td>research</td><td>ptran</td><td>2012</td><td>yes</td></tr>
            niklaus,dev,pascal
            <tr><td>john</td><td>research</td><td>lisp</td><td>2011</td><td>no</td></tr>
            tony,research
            <tr><td>radia</td><td>ops</td><td>stp</td><td>2022</td><td>yes</td></tr>
          </tbody>
        </table>
        <pre>
        ada,dev,core,2019,yes
        linus,ops,kernel,2021,no
        </pre>
    """),
    hint="4f, fails on short rows (and on tags and finished rows). From the last comma, s</td><td>, and "
         ", with . for the others going backwards; I and A add the ends. Then, on a row still in plain "
         "text, vit selects everything inside <tbody>, and : with norm Q runs the macro on just those "
         "lines, so <pre> stays raw.",
    uses=["count", "f", "c", "semicolon", "dot", "insert", "visual", "tag"],
)
norm_macro.add(
    title="One upstream block", par=44, ext="conf",
    task="In upstream production only, turn each complete host:port:weight:zone row into a server line: "
         "server web1:8080 weight=3; # eu. Incomplete rows, and the staging block, stay as they are.",
    start=text("""
        upstream production {
            web1:8080:3:eu
            web2:8080
            web3:8080:1:us
            api1:9000:5:eu
            api2:9000
            db1:5432:1:eu
            cache1:6379:2
            cache2:6379:2:us
            queue1:5672
            queue2:5672:1:eu
            search1:9200:2:us
            mail1:25
            mail2:25:1:eu
            cron1:22
            vpn1:1194:1:us
        }
        upstream staging {
            web1:8080:1:eu
            api1:9000:1:eu
        }
    """),
    target=text("""
        upstream production {
            server web1:8080 weight=3; # eu
            web2:8080
            server web3:8080 weight=1; # us
            server api1:9000 weight=5; # eu
            api2:9000
            server db1:5432 weight=1; # eu
            cache1:6379:2
            server cache2:6379 weight=2; # us
            queue1:5672
            server queue2:5672 weight=1; # eu
            server search1:9200 weight=2; # us
            mail1:25
            server mail2:25 weight=1; # eu
            cron1:22
            server vpn1:1194 weight=1; # us
        }
        upstream staging {
            web1:8080:1:eu
            api1:9000:1:eu
        }
    """),
    hint="3f: fails on incomplete rows, and on finished ones (they keep one colon). From the last colon, "
         "s; #  adds the comment, , goes back to the colon before it for s weight=, and Iserver  adds the "
         "keyword. vi{ selects the inside of the production block, and :norm Q runs the macro there.",
    uses=["count", "f", "c", "semicolon", "insert", "visual", "brace"],
)
norm_macro.add(
    title="Inventory from addresses", par=39, ext="ini",
    task="Rows that start with an IPv4 address become Ansible inventory lines: 10.0.0.11 web1 becomes "
         "web1 ansible_host=10.0.0.11. Rows that start with a DNS name, and the group headers, stay.",
    start=text("""
        [web]
        10.0.0.11 web1
        web2.prod.internal web2
        172.16.4.20 web3
        10.0.0.14 web4
        [db]
        db1.prod.internal db1
        10.0.1.21 db2
        db3.prod.internal db3
        192.168.7.5 db4
        [cache]
        cache.internal cache1
        10.0.2.31 cache2
        cache3.internal cache3
        10.0.2.33 cache4
    """),
    target=text("""
        [web]
        web1 ansible_host=10.0.0.11
        web2.prod.internal web2
        web3 ansible_host=172.16.4.20
        web4 ansible_host=10.0.0.14
        [db]
        db1.prod.internal db1
        db2 ansible_host=10.0.1.21
        db3.prod.internal db3
        db4 ansible_host=192.168.7.5
        [cache]
        cache.internal cache1
        cache2 ansible_host=10.0.2.31
        cache3.internal cache3
        cache4 ansible_host=10.0.2.33
    """),
    hint="An IPv4 address has three dots and none of the DNS names here do, so 3f. is the test. Then 0dW "
         "cuts the address and its space, and A ansible_host= with Ctrl-r \" puts it back at the end "
         "(its trailing space doesn't count). A finished line still has three dots, so leave the line you "
         "recorded on out of the range: :3,$norm Q.",
    uses=["count", "f", "line", "d", "bigword", "insert", "ctrl-r", "range"],
)
norm_macro.add(
    title="Seed only this release", par=39, ext="sql", cursor=(3, 1),
    task="Turn the complete rows of the first block into SQL tuples: ('2.4.0', '2026-11-05', 'fern', "
         "'stable'),. Rows with a missing field, and the second block (an older release), stay as they "
         "are. The cursor starts on the first row.",
    start=text("""
        -- 2.4 series
        INSERT INTO releases VALUES
        2.4.0,2026-11-05,fern,stable
        2.4.1,2026-11-19,fern
        2.4.2,2026-12-03,fern,stable
        2.4.3,2026-12-17,fern
        2.4.4,2027-01-07,fern,beta
        2.4.5,2027-01-21,fern
        2.4.6,2027-02-04,fern,stable
        2.4.7,2027-02-18,fern,stable
        2.4.8,2027-03-04,fern
        2.4.9,2027-03-18,fern,beta
        2.4.10,2027-04-01,fern
        2.4.11,2027-04-15,fern,stable

        -- 2.3 series, already imported
        2.3.9,2026-10-22,daisy,stable
    """),
    target=text("""
        -- 2.4 series
        INSERT INTO releases VALUES
        ('2.4.0', '2026-11-05', 'fern', 'stable'),
        2.4.1,2026-11-19,fern
        ('2.4.2', '2026-12-03', 'fern', 'stable'),
        2.4.3,2026-12-17,fern
        ('2.4.4', '2027-01-07', 'fern', 'beta'),
        2.4.5,2027-01-21,fern
        ('2.4.6', '2027-02-04', 'fern', 'stable'),
        ('2.4.7', '2027-02-18', 'fern', 'stable'),
        2.4.8,2027-03-04,fern
        ('2.4.9', '2027-03-18', 'fern', 'beta'),
        2.4.10,2027-04-01,fern
        ('2.4.11', '2027-04-15', 'fern', 'stable'),

        -- 2.3 series, already imported
        2.3.9,2026-10-22,daisy,stable
    """),
    hint="3f, fails on short rows. Then go back to the first comma (0f,): s', '<Esc>, and ; with . do "
         "the other two going forwards (backwards, , would find the comma you just typed). I(' and A'), "
         "finish the tuple. A finished tuple has commas too, so select from the next line to the end of "
         "the block (jV}), and : with norm Q runs the macro on just those lines.",
    uses=["count", "f", "c", "line", "semicolon", "dot", "insert", "visual-line", "paragraph"],
)
norm_macro.add(
    title="Status codes to an enum", par=35, ext="java",
    task="Turn each complete row (name|code|message|retryable) into an enum constant: "
         "NOT_FOUND(404, \"Not Found\", false),. Rows without the retryable field, and the comments, "
         "stay as they are.",
    start=text("""
        enum Status {
            // 2xx
            OK|200|OK|false
            CREATED|201|Created
            // 4xx
            BAD_REQUEST|400|Bad Request|false
            NOT_FOUND|404|Not Found|false
            CONFLICT|409|Conflict
            TOO_MANY|429|Too Many Requests|true
            // 5xx
            INTERNAL|500|Internal Server Error|false
            BAD_GATEWAY|502|Bad Gateway
            UNAVAILABLE|503|Service Unavailable|true
            TIMEOUT|504|Gateway Timeout|true
        }
    """),
    target=text("""
        enum Status {
            // 2xx
            OK(200, "OK", false),
            CREATED|201|Created
            // 4xx
            BAD_REQUEST(400, "Bad Request", false),
            NOT_FOUND(404, "Not Found", false),
            CONFLICT|409|Conflict
            TOO_MANY(429, "Too Many Requests", true),
            // 5xx
            INTERNAL(500, "Internal Server Error", false),
            BAD_GATEWAY|502|Bad Gateway
            UNAVAILABLE(503, "Service Unavailable", true),
            TIMEOUT(504, "Gateway Timeout", true),
        }
    """),
    hint="3f| fails on rows with fewer than three pipes. From the last pipe, work backwards with , (the "
         "f| again): s\", , then s, \", then r( on the first one. A), closes it. :%norm Q does every line.",
    uses=["count", "f", "c", "semicolon", "r", "insert"],
)
norm_macro.add(
    title="Flags from a table", par=79, ext="py",
    task="Turn each complete row (flag|type|default|help) into an argparse call: "
         "parser.add_argument(\"--retries\", type=int, default=3, help=\"retry this many times\"). "
         "Rows with a missing field, and the comments, stay.",
    start=text("""
        # flag|type|default|help, filled in by hand
        --retries|int|3|retry this many times
        --timeout|float|2.5
        --workers|int|4|parallel jobs
        # network
        --host|str|localhost|bind address
        --port|int|8080|listen port
        --proxy|str
        # output
        --format|str|text|text or json
        --color|str|auto
        --verbose|int|0|more output
    """),
    target=text("""
        # flag|type|default|help, filled in by hand
        parser.add_argument("--retries", type=int, default=3, help="retry this many times")
        --timeout|float|2.5
        parser.add_argument("--workers", type=int, default=4, help="parallel jobs")
        # network
        parser.add_argument("--host", type=str, default=localhost, help="bind address")
        parser.add_argument("--port", type=int, default=8080, help="listen port")
        --proxy|str
        # output
        parser.add_argument("--format", type=str, default=text, help="text or json")
        --color|str|auto
        parser.add_argument("--verbose", type=int, default=0, help="more output")
    """),
    hint="3f| is the test, and the comment on line 1 is the one line it would wrongly pass, so start the "
         "range at line 2. From the last pipe, go backwards with ,: s, help=\", s, default=, s\", type=. "
         "Then Iparser.add_argument(\" and A\"). :2,$norm Q runs it.",
    uses=["count", "f", "c", "semicolon", "insert", "range"],
)
norm_macro.add(
    title="Fields with a comment", par=32, ext="py", cursor=(4, 1),
    task="Turn each complete row (name;type;default;comment) into an annotated field: "
         "retries: int = 3  # attempts before giving up. Rows without a comment stay as they are, so you "
         "can write one. The cursor starts on retries.",
    start=text("""
        @dataclass
        class Settings:
            # name, type, default, comment
            retries;int;3;attempts before giving up
            timeout;float;2.5
            host;str;"0.0.0.0";bind address
            port;int;8080;listen port
            workers;int;4
            debug;bool;False;log every request
            db_url;str;""
            pool_size;int;10;connections per worker
            cache_ttl;int;300
            log_level;str;"info";one of debug, info, warn
            metrics;bool;True
            region;str;"eu-west-1";where to deploy
    """),
    target=text("""
        @dataclass
        class Settings:
            # name, type, default, comment
            retries: int = 3  # attempts before giving up
            timeout;float;2.5
            host: str = "0.0.0.0"  # bind address
            port: int = 8080  # listen port
            workers;int;4
            debug: bool = False  # log every request
            db_url;str;""
            pool_size: int = 10  # connections per worker
            cache_ttl;int;300
            log_level: str = "info"  # one of debug, info, warn
            metrics;bool;True
            region: str = "eu-west-1"  # where to deploy
    """),
    hint="3f; fails on rows with fewer than three semicolons. Work backwards from it with , (none of the "
         "text you type has a ;): s  # , then s = , then s: . A finished field has no semicolons, so "
         ":%norm Q can run on every line.",
    uses=["count", "f", "c", "semicolon"],
)
norm_macro.add(
    title="Two kinds of rows, two passes", par=60,
    task="Turn every row into Mon 09:00-09:15 (A1) Standup. Rows without a room have one semicolon "
         "fewer: they get (TBD) as their room.",
    start=text("""
        Mon;09:00;09:15;A1;Standup
        Mon;10:00;11:30;Planning
        Mon;14:00;15:00;B2;Hiring sync
        Mon;16:00;16:30;Budget
        Tue;09:00;09:15;A1;Standup
        Tue;11:00;12:00;A1;Pairing
        Tue;13:00;14:00;Design review
        Wed;09:00;09:15;A1;Standup
        Wed;10:00;10:45;Vendor call
        Wed;15:00;16:00;A1;1:1 with Ada
        Wed;16:30;17:00;Docs
        Thu;09:00;09:15;A1;Standup
        Thu;11:00;12:00;Demo prep
        Thu;14:00;15:30;B2;Demo
        Thu;16:00;16:30;B2;Q&A
        Fri;09:00;09:15;Standup
        Fri;11:00;12:00;A1;Planning
        Fri;14:00;15:00;Retro
    """),
    target=text("""
        Mon 09:00-09:15 (A1) Standup
        Mon 10:00-11:30 (TBD) Planning
        Mon 14:00-15:00 (B2) Hiring sync
        Mon 16:00-16:30 (TBD) Budget
        Tue 09:00-09:15 (A1) Standup
        Tue 11:00-12:00 (A1) Pairing
        Tue 13:00-14:00 (TBD) Design review
        Wed 09:00-09:15 (A1) Standup
        Wed 10:00-10:45 (TBD) Vendor call
        Wed 15:00-16:00 (A1) 1:1 with Ada
        Wed 16:30-17:00 (TBD) Docs
        Thu 09:00-09:15 (A1) Standup
        Thu 11:00-12:00 (TBD) Demo prep
        Thu 14:00-15:30 (B2) Demo
        Thu 16:00-16:30 (B2) Q&A
        Fri 09:00-09:15 (TBD) Standup
        Fri 11:00-12:00 (A1) Planning
        Fri 14:00-15:00 (TBD) Retro
    """),
    hint="Two macros, two :%norm runs, and the order matters. 4f; only passes rows with a room, so do "
         "those first: work backwards with , (s) , s ( and two r). After that, only the rows without a "
         "room have semicolons left, and a second macro that starts with 3f; can't touch a finished row.",
    uses=["count", "f", "c", "semicolon", "r", "macro"],
)

# ---------- qaq … @aq ----------

recursive = drills.command(
    "recursive", "qaq … @aq", "a macro that calls itself",
    """A macro can call itself: record it with @a as its last key, and every run starts the next one until
    some key fails (an f that finds nothing, j on the last line, a search with no match left). Empty the
    register first with qaq (record nothing into it): while you record, the @a at the end runs whatever a
    already holds, and only an empty register does nothing. The macro has to fail before it changes
    anything on the line where it should stop. 99@a does the same job without recursion; the recursive
    version is a complete "do the rest" command that needs no count.""",
    examples=[("qaq", "empty register a"), ("qa…j@aq", "record a macro that ends by calling itself"),
              ("@a", "run it until something fails")],
    level="complex",
)
recursive.add(
    title="Until the closing brace", par=28, ext="c",
    task="Turn each status into a named constant: HTTP_OK = 200,",
    start=text("""
        enum http_status {
            OK=200
            CREATED=201
            NO_CONTENT=204
            NOT_FOUND=404
            SERVER_ERROR=500
        };
    """),
    target=text("""
        enum http_status {
            HTTP_OK = 200,
            HTTP_CREATED = 201,
            HTTP_NO_CONTENT = 204,
            HTTP_NOT_FOUND = 404,
            HTTP_SERVER_ERROR = 500,
        };
    """),
    hint="Clear register a with qaq. Record on OK, starting with f= so the macro fails on the }; line "
         "before changing anything, and end with + and @a. Then Q (or @a) runs it until f= fails.",
    uses=["macro", "plus", "f", "c", "insert"],
)
recursive.add(
    title="Until no function is left", par=42, ext="js",
    task="Turn each function declaration into an arrow function: const add = (a, b) => {",
    start=text("""
        function add(a, b) {
            return a + b;
        }

        function scale(v, k) {
            return v.map(x => x * k);
        }

        function clamp(x, lo, hi) {
            return Math.min(Math.max(x, lo), hi);
        }
    """),
    target=text("""
        const add = (a, b) => {
            return a + b;
        }

        const scale = (v, k) => {
            return v.map(x => x * k);
        }

        const clamp = (x, lo, hi) => {
            return Math.min(Math.max(x, lo), hi);
        }
    """),
    hint="Start the macro with a search for /function<Space><CR>. A converted line doesn't match any "
         "more, so once all three are done the search fails and the recursion stops, even though "
         "searches wrap around the end of the file.",
    uses=["macro", "search", "c", "word", "insert", "f"],
)
recursive.add(
    title="Unwrap every paragraph", par=15, ext="txt",
    task="Each paragraph was hard-wrapped. Join each one into a single line.",
    start=text("""
        Macros replay keys, not intentions,
        so a macro has to work on every line,
        not just the one you recorded it on.

        Start from a known position
        and move by meaning.

        End by moving to the next target,
        so the next run starts in the right place,
        and make it fail before it changes anything.
    """),
    target=text("""
        Macros replay keys, not intentions, so a macro has to work on every line, not just the one you recorded it on.

        Start from a known position and move by meaning.

        End by moving to the next target, so the next run starts in the right place, and make it fail before it changes anything.
    """),
    hint="vipJ joins the paragraph, however many lines it has. } then goes to the blank line after it "
         "and j to the next paragraph. On the last one there's no line left for j, so the recursion "
         "stops there.",
    uses=["macro", "visual", "ip", "join", "paragraph"],
)
recursive.add(
    title="One field per line", par=18, ext="yaml",
    task="This logfmt line is hard to read. Put each field on its own line as key: value, like "
         "level: error.",
    start="ts=2026-11-06T10:22:01Z level=error svc=billing route=/v1/charge status=502 user=4821 took=1532ms",
    target=text("""
        ts: 2026-11-06T10:22:01Z
        level: error
        svc: billing
        route: /v1/charge
        status: 502
        user: 4821
        took: 1532ms
    """),
    hint="The macro never leaves the line it splits: w (or f=) reaches the =, s: <Esc> fixes it, and "
         "f<Space> with r<CR> breaks the line after the field, so the cursor lands at the start of the "
         "rest. On the last field f<Space> finds nothing, and the recursion stops.",
    uses=["macro", "word", "c", "f", "r"],
)
recursive.add(
    title="Every debug block, any length", par=16, ext="java",
    task="Delete every if (log.isDebugEnabled()) { ... } block, braces and all. The blocks have "
         "different lengths; everything else stays.",
    start=text("""
        public Report build(List<Order> orders) {
            if (log.isDebugEnabled()) {
                log.debug("building report for {} orders", orders.size());
            }
            Report report = new Report();
            for (Order order : orders) {
                if (log.isDebugEnabled()) {
                    log.debug("order {}", order.id());
                    log.debug("lines {}", order.lines());
                }
                report.add(order);
                if (log.isDebugEnabled()) {
                    log.debug("running total {}", report.total());
                }
            }
            if (log.isDebugEnabled()) {
                log.debug("closing after {} ms", timer.elapsed());
                log.debug(report.summary());
            }
            report.close();
            if (log.isDebugEnabled()) {
                log.debug("closed");
            }
            return report;
        }
    """),
    target=text("""
        public Report build(List<Order> orders) {
            Report report = new Report();
            for (Order order : orders) {
                report.add(order);
            }
            report.close();
            return report;
        }
    """),
    hint="Search for the block (smartcase makes /D match only a capital D), $ reaches its {, and V% "
         "selects every line down to the matching }, however many there are. When no block is left, "
         "the search fails and the recursion stops.",
    uses=["macro", "search", "line", "visual-line", "percent", "d"],
)
recursive.add(
    title="Unwrap until the return", par=17, ext="py",
    task='The row now comes from a typed reader. Remove each conversion call, so int(row["id"]) '
         'becomes row["id"].',
    start=text("""
        def to_user(row):
            user_id = int(row["id"])
            name = str(row["name"])
            score = float(row["score"])
            active = bool(row["active"])
            tags = list(row["tags"])
            joined = date(row["joined"])
            return user_id, name, score, active, tags, joined
    """),
    target=text("""
        def to_user(row):
            user_id = row["id"]
            name = row["name"]
            score = row["score"]
            active = row["active"]
            tags = row["tags"]
            joined = row["joined"]
            return user_id, name, score, active, tags, joined
    """),
    hint="Start each run with + and f(: the return line has no (, so the recursion stops there before "
         "touching it. x deletes the (, db the function name in front of it, and $x the ) at the end.",
    uses=["macro", "plus", "f", "x", "d", "word", "line"],
)

# ---------- qA ----------

append_macro = drills.command(
    "append-macro", "qA", "add keys to the end of a macro",
    """Recording into an uppercase register adds to the end of the lowercase one: qA … q appends keys to
    macro a, just like "Ayy appends to register a. The new keys run after the old last key, so if the
    macro ends with j, the added keys run on the next line. Macros that start with the move (j or +,
    then the edit) are the easy ones to extend. It's the tool for a group of lines that needs one more
    step than the rest.""",
    examples=[("qAA;<Esc>q", "add \"append a semicolon\" to macro a"), ("qAjq", "add a move down to macro a"),
              ("2@a", "play the longer macro")],
    level="complex",
)
append_macro.add(
    title="Inputs get one more field", par=40, ext="c",
    task='Turn each row into an initializer like { "led", 13 },. The rows under /* inputs */ also get '
         'INPUT: { "button", 2, INPUT },',
    start=text("""
        static const struct pin pins[] = {
            led,13
            buzzer,8
            /* inputs */
            button,2
            sensor,7
            door,4
        };
    """),
    target=text("""
        static const struct pin pins[] = {
            { "led", 13 },
            { "buzzer", 8 },
            /* inputs */
            { "button", 2, INPUT },
            { "sensor", 7, INPUT },
            { "door", 4, INPUT },
        };
    """),
    hint="Record a macro that starts with + and then converts the row. After the first input row, qA "
         "adds keys to it: F<Space> finds the space before }, and i, INPUT adds the field. The longer "
         "macro does the other two.",
    uses=["macro", "plus", "insert", "f", "c", "count"],
)
append_macro.add(
    title="Mark the known bugs", par=46, ext="py",
    task='Turn each row into a test case like Case("add", 1, 2),. The rows under # known bugs also get '
         '.xfail(): Case("div", 1, 0).xfail(),',
    start=text("""
        CASES = [
            add,1,2
            sub,5,3
            mul,4,6
            # known bugs
            div,1,0
            mod,7,0
            pow,0,-1
        ]
    """),
    target=text("""
        CASES = [
            Case("add", 1, 2),
            Case("sub", 5, 3),
            Case("mul", 4, 6),
            # known bugs
            Case("div", 1, 0).xfail(),
            Case("mod", 7, 0).xfail(),
            Case("pow", 0, -1).xfail(),
        ]
    """),
    hint="Start the macro with +, so keys added later run on the same row. After div, qA appends "
         "i.xfail()<Esc>: the cursor is on the last comma, so i puts the call right before it.",
    uses=["macro", "plus", "insert", "f", "c", "semicolon", "count"],
)
append_macro.add(
    title="Titles for the icons", par=35, ext="md",
    task='Turn each row into a Markdown image: ![home](img/home.png). The icons also get a title: '
         '![save](img/save.png "icon")',
    start=text("""
        ## Screenshots
        home,img/home.png
        editor,img/editor.png
        settings,img/settings.png
        ## Icons
        save,img/save.png
        open,img/open.png
        undo,img/undo.png
        redo,img/redo.png
    """),
    target=text("""
        ## Screenshots
        ![home](img/home.png)
        ![editor](img/editor.png)
        ![settings](img/settings.png)
        ## Icons
        ![save](img/save.png "icon")
        ![open](img/open.png "icon")
        ![undo](img/undo.png "icon")
        ![redo](img/redo.png "icon")
    """),
    hint="Record from the heading with a macro that starts with +. Skip the ## Icons line with + "
         "before playing it on save. Then qA appends i \"icon\"<Esc>, which lands before the ) "
         "because A) left the cursor on it.",
    uses=["macro", "plus", "insert", "f", "c", "count"],
)
append_macro.add(
    title="Owned by the app user", par=43, ext="sh",
    task="Turn each path into mkdir -p /var/cache/app. Each path under # owned by the app user also "
         "gets a second line below it: chown app:app /var/log/app",
    start=text("""
        # scratch space
        /var/cache/app
        /var/tmp/app
        # owned by the app user
        /var/log/app
        /var/lib/app
        /srv/app/uploads
        /srv/app/exports
    """),
    target=text("""
        # scratch space
        mkdir -p /var/cache/app
        mkdir -p /var/tmp/app
        # owned by the app user
        mkdir -p /var/log/app
        chown app:app /var/log/app
        mkdir -p /var/lib/app
        chown app:app /var/lib/app
        mkdir -p /srv/app/uploads
        chown app:app /srv/app/uploads
        mkdir -p /srv/app/exports
        chown app:app /srv/app/exports
    """),
    hint="Record the mkdir step with a macro that starts with +. On /var/log/app, qA adds the chown "
         "line: W reaches the path, Y yanks it, and o opens the line where Ctrl-r \" types it again. "
         "The next run's + starts from that new line, so it lands on the next path.",
    uses=["macro", "plus", "insert", "bigword", "y", "o", "ctrl-r", "count"],
)
append_macro.add(
    title="Help from the next line", par=55, ext="py",
    task='Turn each option into parser.add_argument("--verbose"). Each option under # with help text '
         'takes the line below it as its help: parser.add_argument("--output", help="where to write '
         'the report")',
    start=text("""
        parser = argparse.ArgumentParser(prog="report")
        --verbose
        --dry-run
        # with help text
        --output
        where to write the report
        --format
        csv, json or html
        --since
        only count commits after this date
        args = parser.parse_args()
    """),
    target=text("""
        parser = argparse.ArgumentParser(prog="report")
        parser.add_argument("--verbose")
        parser.add_argument("--dry-run")
        # with help text
        parser.add_argument("--output", help="where to write the report")
        parser.add_argument("--format", help="csv, json or html")
        parser.add_argument("--since", help="only count commits after this date")
        args = parser.parse_args()
    """),
    hint="Record the plain conversion with a macro that starts with +. On --output, qA adds the join: "
         "x drops the ), J pulls the help line up (the cursor lands on the space it added), s, help=\" "
         "replaces that space, and A\") closes the call. The help line is gone, so the next + finds "
         "the next option.",
    uses=["macro", "plus", "insert", "x", "join", "c", "count"],
)
append_macro.add(
    title="Remote calls return promises", par=35, ext="ts",
    task="Turn each row into a method signature like count(): number;. The rows under // remote also "
         "wrap their type in a Promise: fetchUsers(): Promise<User[]>;",
    start=text("""
        interface UserStore {
            count number
            current User
            // remote
            fetchUsers User[]
            fetchRoles string[]
            fetchSettings Settings
            fetchAvatar Blob
        }
    """),
    target=text("""
        interface UserStore {
            count(): number;
            current(): User;
            // remote
            fetchUsers(): Promise<User[]>;
            fetchRoles(): Promise<string[]>;
            fetchSettings(): Promise<Settings>;
            fetchAvatar(): Promise<Blob>;
        }
    """),
    hint="Record the signature with a macro that starts with + (ea(): after the name, A; at the end). "
         "On fetchUsers, qA adds the wrapper: A; left the cursor on the ;, so i> closes it right "
         "there, and B goes back to the start of the type for iPromise<.",
    uses=["macro", "plus", "word", "insert", "bigword", "count"],
)

# ---------- "ap "ay$ ----------

edit_macro = drills.command(
    "edit-macro", "\"ap … \"ay$", "edit a macro as text",
    """A macro is plain text in a register, so you can edit it like text: "ap pastes macro a after the
    cursor (on a blank line, or make one with o<Esc>), with special keys shown as ^[ (Esc), ^M (Enter)
    and ^R (Ctrl-r). Fix it with normal edits, yank it back without the line break with 0"ay$, and
    delete the line. Don't use "ayy: the line break becomes part of the macro and acts like an extra j.
    Any register can be played (@0 plays the last yank), but a macro that calls @a, or that yanks while
    :norm runs it, needs a letter of its own. You can also set a macro directly: :let @a = "A;\<Esc>j".""",
    examples=[("o<Esc>\"ap", "paste macro a on a new line"), ("0\"ay$", "yank the line back into a"),
              (":let @a = \"A;\\<Esc>j\"", "set macro a directly"), ("@0", "play the yank register as a macro")],
    level="complex",
)
edit_macro.add(
    title="A recursive macro with a typo", par=13, ext="sh",
    task="Line 1 is a recursive macro a teammate left in the file (^[ is <Esc>). It has one wrong key. "
         "Fix it, delete line 1, and use it to turn every setting into export HOST=\"localhost\".",
    start=text(f"""
        0F=a"{ESC}A"{ESC}Iexport {ESC}j@a
        HOST=localhost
        PORT=8080
        USER=admin
        LOG_LEVEL=info
        CACHE_DIR=/tmp/cache
        TIMEOUT=30
    """),
    target=text("""
        export HOST="localhost"
        export PORT="8080"
        export USER="admin"
        export LOG_LEVEL="info"
        export CACHE_DIR="/tmp/cache"
        export TIMEOUT="30"
    """),
    hint="F= searches backward from column 1, so it fails at once: it should be f=. The macro ends by "
         "calling @a, so it has to live in register a: yank it with 0\"ay$ (not yy), delete the line, "
         "and @a runs it to the last line.",
    uses=["f", "r", "line", "named", "y", "dd", "macro"],
)
edit_macro.add(
    title="Same macro, other mode", par=60, ext="c",
    task="Turn each row into a pinMode call with the name as a comment: pinMode(13, OUTPUT); // led. "
         "The rows after the blank line are inputs: they use INPUT instead of OUTPUT.",
    start=text("""
        void setup() {
            led,13
            buzzer,8
            relay,7

            button,2
            sensor,10
            door,4
            window,12
            smoke,5
        }
    """),
    target=text("""
        void setup() {
            pinMode(13, OUTPUT); // led
            pinMode(8, OUTPUT); // buzzer
            pinMode(7, OUTPUT); // relay

            pinMode(2, INPUT); // button
            pinMode(10, INPUT); // sensor
            pinMode(4, INPUT); // door
            pinMode(12, INPUT); // window
            pinMode(5, INPUT); // smoke
        }
    """),
    hint="Record the outputs with a macro that starts with + (f,lD cuts the number, and Ctrl-r \" puts "
         "it back inside pinMode(...)). For the inputs, don't record it again: on the blank line, \"ap "
         "pastes the macro as text. Change OUTPUT to INPUT, yank it back with 0\"ay$, and D empties "
         "the line again.",
    uses=["plus", "f", "d", "insert", "ctrl-r", "line", "x", "named", "p", "c", "y", "count"],
)
edit_macro.add(
    title="Accessors for every field", par=21, ext="java",
    task="Line 1 is a macro (^[ is <Esc>, ^R is Ctrl-r) that turns a field into an accessor, but one key "
         "is wrong. Fix it, delete line 1, and turn every field into public String name() { return "
         "name; }. Comments and blank lines stay.",
    start=text(f"""
        f;byiwApublic {ESC}$s() {{ return {CTRL_R}0; }}{ESC}
        class User {{
            // identity
            String name;
            long id;

            // contact
            String email;
            List<String> phones;
        }}
    """),
    target=text("""
        class User {
            // identity
            public String name() { return name; }
            public long id() { return id; }

            // contact
            public String email() { return email; }
            public List<String> phones() { return phones; }
        }
    """),
    hint="Apublic would type at the end of the line: it should be Ipublic. The fields are spread out, "
         "so run the macro with :%norm @a (f; makes it skip lines without a semicolon). It yanks a "
         "word itself, so it can't stay in the yank register: put it in a with 0\"ay$.",
    uses=["f", "r", "line", "named", "y", "dd", "norm-macro"],
)
edit_macro.add(
    title="Yesterday's macro, today's file", par=18, ext="sql",
    setup=["setlocal indentexpr=",
           r'''let @a = "IINSERT INTO users VALUES ('\<Esc>f,s', '\<Esc>A');\<Esc>+@a"'''],
    task="Register a still holds yesterday's macro for users.csv (^[ is <Esc>): "
         "IINSERT INTO users VALUES ('^[f,s', '^[A');^[+@a. Today's export separates the fields with "
         "semicolons. Fix the macro and turn every row into INSERT INTO users VALUES ('ada', "
         "'ada@example.com');",
    start=text("""
        -- users from crm_export.csv (semicolon-separated)

        ada;ada@example.com
        alan;alan@example.com
        grace;grace@example.com
        linus;linus@example.com
        margaret;margaret@example.com
        dennis;dennis@example.com
        barbara;barbara@example.com
    """),
    target=text("""
        -- users from crm_export.csv (semicolon-separated)

        INSERT INTO users VALUES ('ada', 'ada@example.com');
        INSERT INTO users VALUES ('alan', 'alan@example.com');
        INSERT INTO users VALUES ('grace', 'grace@example.com');
        INSERT INTO users VALUES ('linus', 'linus@example.com');
        INSERT INTO users VALUES ('margaret', 'margaret@example.com');
        INSERT INTO users VALUES ('dennis', 'dennis@example.com');
        INSERT INTO users VALUES ('barbara', 'barbara@example.com');
    """),
    hint="Paste the macro on the blank line with \"ap. Its first comma is the one after f (the other "
         "is inside ', '), so 2F, reaches it and r; fixes it. The macro calls @a, so yank it back into "
         "a with 0\"ay$, and D empties the line again.",
    uses=["named", "p", "f", "r", "line", "y", "d", "macro"],
)
edit_macro.add(
    title="The macro in the comment", par=14, ext="py",
    task="The comment on line 1 records the macro that builds the list (^[ is <Esc>), but it stops "
         "after one row. Fix it in the comment (the comment stays), then use it to turn every row "
         "into (\"eur\", \"Euro\"),",
    start=text(f"""
        # built from currencies.csv with macro a: f,s", "{ESC}I    ("{ESC}A"),{ESC}j@a
        CURRENCIES = [
        eur,Euro
        usd,US Dollar
        gbp,Pound Sterling
        jpy,Yen
        chf,Swiss Franc
        cad,Canadian Dollar
        ]
    """),
    target=text(f"""
        # built from currencies.csv with macro a: f,s", "{ESC}I    ("{ESC}A"),{ESC}+@a
        CURRENCIES = [
            ("eur", "Euro"),
            ("usd", "US Dollar"),
            ("gbp", "Pound Sterling"),
            ("jpy", "Yen"),
            ("chf", "Swiss Franc"),
            ("cad", "Canadian Dollar"),
        ]
    """),
    hint="After A\"), the cursor is at the end of a long line, and j keeps that column: on the next, "
         "shorter row it lands past the comma, so f, fails. + goes to the start of the line instead. "
         "Then yank just the macro with \"ay$ from its first key (3B gets there), and play it from "
         "the start of the eur row.",
    uses=["f", "r", "bigword", "named", "y", "line", "plus", "macro"],
)
edit_macro.add(
    title="One more column", par=22, ext="md",
    setup=[r'let @a = "f,s | \<Esc>I| \<Esc>A |\<Esc>+@a"'],
    task="Register a holds the macro that built last week's two-column table (^[ is <Esc>): "
         "f,s | ^[I| ^[A |^[+@a. This table has three columns. Fix the macro and turn every row into "
         "| qa | Normal | start recording into register a |",
    start=text("""
        | Keys | Mode | What it does |
        |---|---|---|
        qa,Normal,start recording into register a
        q,Recording,stop recording
        @a,Normal,play register a
        @@,Normal,play the register played last
        Q,Normal,play the register recorded last
        qA,Normal,record more keys onto register a
        "ap,Normal,paste register a as text
    """),
    target=text("""
        | Keys | Mode | What it does |
        |---|---|---|
        | qa | Normal | start recording into register a |
        | q | Recording | stop recording |
        | @a | Normal | play register a |
        | @@ | Normal | play the register played last |
        | Q | Normal | play the register recorded last |
        | qA | Normal | record more keys onto register a |
        | "ap | Normal | paste register a as text |
    """),
    hint="qA can't help: keys added after @a never run, because the recursion ends by failing. Paste "
         "the macro on a new line, and insert ;. after the first ^[: ; finds the second comma and . "
         "repeats s | on it. Yank it back into a with 0\"ay$ (it calls @a), and dd the line.",
    uses=["o", "named", "p", "f", "insert", "semicolon", "dot", "line", "y", "dd", "macro"],
)

# ---------- yyp Ctrl-a ----------

counter = drills.command(
    "counter", "yyp Ctrl-a", "macros that count",
    """Ctrl-a adds 1 to the number at or after the cursor on the line, and Ctrl-x subtracts 1. With a count
    it adds that much: 4 Ctrl-a adds 4. It understands hex (0x0c plus 4 is 0x10) and keeps leading zeros
    (007 becomes 008), but a - right before a number makes it negative. Inside a macro it's a counter:
    yyp copies the line and Ctrl-a bumps its number, and since the next run copies the line the last run
    made, the numbers climb. After Ctrl-a the cursor is on the number it changed, so move past it before
    bumping a second number on the same line.""",
    examples=[("yyp Ctrl-a", "copy the line, add 1 to its first number"), ("4 Ctrl-a", "add 4"),
              ("Ctrl-x", "subtract 1"), ("$ Ctrl-a", "bump the number at the end of the line")],
    level="complex",
)
counter.add(
    title="Six numbered buttons", par=12, ext="java",
    task="Make buttons 1 to 6: each line is a copy of the one above with both numbers one higher.",
    start='JButton b1 = new JButton("Button 1");',
    target=text("""
        JButton b1 = new JButton("Button 1");
        JButton b2 = new JButton("Button 2");
        JButton b3 = new JButton("Button 3");
        JButton b4 = new JButton("Button 4");
        JButton b5 = new JButton("Button 5");
        JButton b6 = new JButton("Button 6");
    """),
    hint="yyp copies the line and Ctrl-a bumps the first number (b1). f\" moves past it to the label, "
         "and a second Ctrl-a bumps that one. Record it and replay it four times.",
    uses=["y", "p", "increment", "f", "macro", "count"],
)
counter.add(
    title="Timers 0x400 apart", par=15, ext="c",
    task="Add TIMER1 to TIMER4. Each timer's registers start 0x400 bytes (1024) after the previous one's.",
    start="#define TIMER0_BASE 0x40000000",
    target=text("""
        #define TIMER0_BASE 0x40000000
        #define TIMER1_BASE 0x40000400
        #define TIMER2_BASE 0x40000800
        #define TIMER3_BASE 0x40000c00
        #define TIMER4_BASE 0x40001000
    """),
    hint="Copy the line and bump TIMER0 with Ctrl-a. A count is always decimal, so 1024 Ctrl-a adds "
         "0x400 to the hex number at the end ($ gets you there). Record that and replay it three times.",
    uses=["y", "p", "increment", "line", "macro", "count"],
)
counter.add(
    title="Number the steps", par=27, ext="c",
    task="Number the step comments 1 to 5: /* step 1 */, /* step 2 */, ... Every other number in the "
         "code stays as it is.",
    start=text("""
        int main(int argc, char **argv) {
            /* step */
            Config cfg = load_config(argc, argv);
            /* step */
            if (cfg.workers > 16)
                cfg.workers = 16;
            /* step */
            Pool *pool = pool_new(cfg.workers, 0);
            /* step */
            for (int i = 1; i < argc; i++)
                pool_add(pool, argv[i]);
            /* step */
            return pool_wait(pool) ? 0 : 1;
        }
    """),
    target=text("""
        int main(int argc, char **argv) {
            /* step 1 */
            Config cfg = load_config(argc, argv);
            /* step 2 */
            if (cfg.workers > 16)
                cfg.workers = 16;
            /* step 3 */
            Pool *pool = pool_new(cfg.workers, 0);
            /* step 4 */
            for (int i = 1; i < argc; i++)
                pool_add(pool, argv[i]);
            /* step 5 */
            return pool_wait(pool) ? 0 : 1;
        }
    """),
    hint="Number the first step by hand (/step<CR> then ea 1). Then record: yiw yanks the number, n "
         "finds the next step, ea <C-r>0 types the same number, and Ctrl-a makes it one higher. "
         "g Ctrl-a would bump the other numbers in the code too.",
    uses=["search", "word", "insert", "y", "iw", "ctrl-r", "increment", "macro", "count"],
)
counter.add(
    title="Ctrl-x counts up", par=13, ext="txt",
    task="Add hosts node-2 to node-6, each on the next IP address: 10.0.1.12 node-2, and so on.",
    start="10.0.1.11   node-1",
    target=text("""
        10.0.1.11   node-1
        10.0.1.12   node-2
        10.0.1.13   node-3
        10.0.1.14   node-4
        10.0.1.15   node-5
        10.0.1.16   node-6
    """),
    hint="The - in node-1 reads as a minus sign, so Ctrl-a would turn -1 into 0 (node0). Ctrl-x takes 1 "
         "from -1, which gives node-2. $ gets to it, and F. goes back to the last part of the IP for "
         "Ctrl-a. Record that after yyp and replay it four times.",
    uses=["y", "p", "line", "f", "increment", "macro", "count"],
)
counter.add(
    title="Two lines per copy", par=17, ext="py",
    task="Add test_level_2 to test_level_5. Each test checks that score(n) is n * 10, like "
         "self.assertEqual(score(2), 20).",
    start=text("""
        class TestScore(unittest.TestCase):
            def test_level_1(self):
                self.assertEqual(score(1), 10)
    """),
    target=text("""
        class TestScore(unittest.TestCase):
            def test_level_1(self):
                self.assertEqual(score(1), 10)
            def test_level_2(self):
                self.assertEqual(score(2), 20)
            def test_level_3(self):
                self.assertEqual(score(3), 30)
            def test_level_4(self):
                self.assertEqual(score(4), 40)
            def test_level_5(self):
                self.assertEqual(score(5), 50)
    """),
    hint="Record on the assert line, so every run ends where the next one starts: yk yanks both lines "
         "of the test, and jp puts the copy below. Ctrl-a bumps the name; j and Ctrl-a bump score(...), "
         "and W with 10 Ctrl-a the expected value.",
    uses=["gg", "y", "p", "increment", "bigword", "macro", "count"],
)
counter.add(
    title="A partition per week", par=16, ext="sql",
    task="Add the partitions for weeks 2 to 6. Each one starts where the one before ends and covers 7 "
         "days: CREATE TABLE events_w02 PARTITION OF events FOR VALUES FROM (8) TO (15);",
    start="CREATE TABLE events_w01 PARTITION OF events FOR VALUES FROM (1) TO (8);",
    target=text("""
        CREATE TABLE events_w01 PARTITION OF events FOR VALUES FROM (1) TO (8);
        CREATE TABLE events_w02 PARTITION OF events FOR VALUES FROM (8) TO (15);
        CREATE TABLE events_w03 PARTITION OF events FOR VALUES FROM (15) TO (22);
        CREATE TABLE events_w04 PARTITION OF events FOR VALUES FROM (22) TO (29);
        CREATE TABLE events_w05 PARTITION OF events FOR VALUES FROM (29) TO (36);
        CREATE TABLE events_w06 PARTITION OF events FOR VALUES FROM (36) TO (43);
    """),
    hint="After yyp, Ctrl-a bumps w01 and keeps its leading zero. f( reaches the first bound and 7 "
         "Ctrl-a adds a week; ; repeats the f( for the second bound.",
    uses=["y", "p", "increment", "f", "semicolon", "count", "macro"],
)
