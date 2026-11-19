"""Exercises for Project 06. Run:  python3 check.py   (python3 check.py 3 plays exercise 3)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "common"))
from trainer import Course, text  # noqa: E402

course = Course("Project 06 · Macros: record once, replay a thousand times", __file__,
                done_message="On to 07_ex_commands, where one line of :s or :g transforms a whole file.")

ESC = "\x1b"  # a literal <Esc>, as it appears when a macro is pasted into a file (shown as ^[)

course.add(
    name="first-macro", title="Record once, replay", par=16, ext="py",
    task="This is Python 2. Turn each print statement into a print(...) call.",
    start=text("""
        def greet(name):
            print "Hello,", name
            if name == "Rick":
                print "Welcome back!"
            print "Goodbye"
    """),
    target=text("""
        def greet(name):
            print("Hello,", name)
            if name == "Rick":
                print("Welcome back!")
            print("Goodbye")
    """),
    hint="Fix the first print while recording with qa ... q. Then move to the next print and play "
         "it back with Q, which plays the macro you recorded last (@a, then @@, work too).",
    uses=["macro", "replay", "plus", "f", "r", "insert", "count"],
)
course.add(
    name="count-rows", title="Fifteen rows at once", par=25, ext="c",
    task="Turn every name,score row into a struct initializer like { \"alice\", 92 },",
    start=text("""
        struct score scores[] = {
            alice,92
            bob,85
            carol,78
            dave,64
            erin,88
            frank,71
            grace,95
            heidi,59
            ivan,83
            judy,90
            mallory,47
            niaj,76
            olivia,99
            peggy,68
            rupert,80
        };
    """),
    target=text("""
        struct score scores[] = {
            { "alice", 92 },
            { "bob", 85 },
            { "carol", 78 },
            { "dave", 64 },
            { "erin", 88 },
            { "frank", 71 },
            { "grace", 95 },
            { "heidi", 59 },
            { "ivan", 83 },
            { "judy", 90 },
            { "mallory", 47 },
            { "niaj", 76 },
            { "olivia", 99 },
            { "peggy", 68 },
            { "rupert", 80 },
        };
    """),
    hint="Record the first row, and finish the macro by moving down a line with j. Then a count "
         "plays it that many times: 14Q.",
    uses=["macro", "replay", "insert", "f", "c"],
)
course.add(
    name="grow-tree", title="Grow the tree", par=14,
    task="Grow the tree: each row is a copy of the one above, one space further left and two stars "
         "wider, down to a base of 15 stars. The trunk stays at the bottom.",
    start="       *\n      |||",
    target=text("""
               *
              ***
             *****
            *******
           *********
          ***********
         *************
        ***************
              |||
    """),
    hint="A macro can make new lines: copy the row with yyp, then remove one leading space and add "
         "two stars. Each replay starts from the row the last one made.",
    uses=["macro", "replay", "y", "p", "line", "x", "insert"],
)
course.add(
    name="gpio-numbering", title="Number the pins", par=13, ext="c",
    task="Define pins 0 to 7. Each pin's register is 4 bytes after the previous one.",
    start=text("""
        /* GPIO register offsets */
        #define GPIO_PIN0 0x00
    """),
    target=text("""
        /* GPIO register offsets */
        #define GPIO_PIN0 0x00
        #define GPIO_PIN1 0x04
        #define GPIO_PIN2 0x08
        #define GPIO_PIN3 0x0c
        #define GPIO_PIN4 0x10
        #define GPIO_PIN5 0x14
        #define GPIO_PIN6 0x18
        #define GPIO_PIN7 0x1c
    """),
    hint="Copy the line, then Ctrl-a adds 1 to the first number at or after the cursor, and 4 Ctrl-a "
         "adds 4. Ctrl-a understands hex. Record that once and replay it six times.",
    uses=["counter", "increment", "macro", "replay", "y", "p", "line"],
)
course.add(
    name="robust-fields", title="Any line, any shape", par=27, ext="java",
    task="These fields were pasted into the constructor. Turn each line into an assignment like "
         "this.name = name;",
    start=text("""
        User(/* ... */) {
            private final String name;
            private final int age;
            private final List<String> tags;
            private final Map<String, Integer> scores;
            private final int[] history;
        }
    """),
    target=text("""
        User(/* ... */) {
            this.name = name;
            this.age = age;
            this.tags = tags;
            this.scores = scores;
            this.history = history;
        }
    """),
    hint="Don't count words: the types have different shapes. The name is always the last word "
         "before the semicolon ($b finds it). Yank it, then S replaces the whole line, and Ctrl-r 0 "
         "inserts the yank.",
    uses=["macro", "replay", "line", "word", "y", "iw", "c", "ctrl-r"],
)
course.add(
    name="search-ifdef", title="Let the macro find its target", par=33, ext="c",
    task="Wrap every printf in #ifdef DEBUG ... #endif, each on its own lines.",
    start=text(r"""
        int parse(const char *s) {
            int n = 0;
            printf("parsing %s\n", s);
            while (*s) {
                n = n * 10 + (*s++ - '0');
                printf("n = %d\n", n);
            }
            printf("done: %d\n", n);
            return n;
        }
    """),
    target=text(r"""
        int parse(const char *s) {
            int n = 0;
        #ifdef DEBUG
            printf("parsing %s\n", s);
        #endif
            while (*s) {
                n = n * 10 + (*s++ - '0');
        #ifdef DEBUG
                printf("n = %d\n", n);
        #endif
            }
        #ifdef DEBUG
            printf("done: %d\n", n);
        #endif
            return n;
        }
    """),
    hint="The printfs aren't on neighboring lines, so start the macro with a search (/pri) that "
         "jumps to the next one. Then O and o open lines above and below. C indenting moves # to "
         "column 1 for you.",
    uses=["macro", "search", "o", "replay"],
)
course.add(
    name="recursive-dict", title="A macro that calls itself", par=21, ext="py",
    task="Environment settings are strings. Quote each value and end each line with a comma, "
         "like host=\"localhost\",",
    start=text("""
        DEFAULTS = dict(
            host=localhost
            port=8080
            user=admin
            timeout=30
            retries=3
            log_level=info
        )
    """),
    target=text("""
        DEFAULTS = dict(
            host="localhost",
            port="8080",
            user="admin",
            timeout="30",
            retries="3",
            log_level="info",
        )
    """),
    hint="Clear register a with qaq. Record the first row, ending with j and then @a (which does "
         "nothing yet, because a is empty). Then Q runs it until a motion fails: start with 0f= so "
         "it fails on the closing paren, before changing anything.",
    uses=["recursive", "macro", "line", "f", "insert"],
)
course.add(
    name="edit-macro", title="Fix a macro as text", par=11, ext="java",
    task="Line 1 is a macro a teammate pasted into the file (^[ is <Esc>). It has one wrong key. "
         "Fix it, delete line 1, and run the macro on every row.",
    start=text(f"""
        Icfg.put("{ESC}F,s", {ESC}A);{ESC}j
        width,800
        height,600
        depth,32
        fps,60
        vsync,1
    """),
    target=text("""
        cfg.put("width", 800);
        cfg.put("height", 600);
        cfg.put("depth", 32);
        cfg.put("fps", 60);
        cfg.put("vsync", 1);
    """),
    hint="F, searches backward, but at that point the comma is ahead of the cursor. Fix the "
         "letter, then yank the line with y$ (not yy, or the line break joins the macro). Any "
         "register can be played: @0 plays the yank register.",
    uses=["edit-macro", "f", "case", "line", "y", "dd", "yank0", "replay"],
)
course.add(
    name="normal-table", title="Skip the rows that don't fit", par=33, ext="md",
    task="Turn the CSV into Markdown table rows like | ada | dev | core | ada@ex.io |. Two rows have "
         "no email: leave those exactly as they are, so you notice and fix them by hand.",
    start=text("""
        name,role,team,email
        ---,---,---,---
        ada,dev,core,ada@ex.io
        alan,dev,infra,alan@ex.io
        grace,lead,core
        linus,ops,infra,linus@ex.io
        ken,dev,core
        dennis,dev,infra,dmr@ex.io
    """),
    target=text("""
        | name | role | team | email |
        | --- | --- | --- | --- |
        | ada | dev | core | ada@ex.io |
        | alan | dev | infra | alan@ex.io |
        grace,lead,core
        | linus | ops | infra | linus@ex.io |
        ken,dev,core
        | dennis | dev | infra | dmr@ex.io |
    """),
    hint="A count stops at the first row where the macro fails. :%norm Q runs the macro on every "
         "line and just skips the ones where it fails. So make it fail on short rows first: 3f, "
         "needs three commas.",
    uses=["norm-macro", "macro", "count", "f", "c", "dot", "semicolon", "insert"],
)
course.add(
    name="append-macro", title="Add a step to the macro", par=49, ext="py",
    task="Turn each name,age row into Person(\"name\", age),. The rows under # admins also get "
         "admin=True as a last argument.",
    start=text("""
        people = [
            ada,36
            alan,41
            grace,85
            # admins
            linus,54
            ken,80
            dennis,70
        ]
    """),
    target=text("""
        people = [
            Person("ada", 36),
            Person("alan", 41),
            Person("grace", 85),
            # admins
            Person("linus", 54, admin=True),
            Person("ken", 80, admin=True),
            Person("dennis", 70, admin=True),
        ]
    """),
    hint="Record a macro that starts by moving down (j) and then converts the row. On the first "
         "admin row, qA appends to the macro: the keys you type now are added to the end of a.",
    uses=["append-macro", "macro", "replay", "insert", "f", "c"],
)
course.add(
    name="enum-finale", title="CSV to Java", par=29, ext="java",
    task="Turn every row into an enum constant: apple,50 becomes APPLE(\"apple\", 50),",
    start=text("""
        enum Fruit {
            apple,50
            banana,25
            cherry,300
            date,180
            fig,90
            grape,120
            kiwi,45
            lemon,30
            lime,25
            mango,150
            melon,400
            peach,80
            pear,70
            plum,60
            quince,110
            ;
            Fruit(String label, int cents) { /* ... */ }
        }
    """),
    target=text("""
        enum Fruit {
            APPLE("apple", 50),
            BANANA("banana", 25),
            CHERRY("cherry", 300),
            DATE("date", 180),
            FIG("fig", 90),
            GRAPE("grape", 120),
            KIWI("kiwi", 45),
            LEMON("lemon", 30),
            LIME("lime", 25),
            MANGO("mango", 150),
            MELON("melon", 400),
            PEACH("peach", 80),
            PEAR("pear", 70),
            PLUM("plum", 60),
            QUINCE("quince", 110),
            ;
            Fruit(String label, int cents) { /* ... */ }
        }
    """),
    hint="The name appears twice: yank it first, uppercase it with gU, and use Ctrl-r 0 for the "
         "lowercase copy. Start the macro with ^ so it works wherever j left the cursor.",
    uses=["macro", "replay", "line", "y", "word", "case", "f", "c", "ctrl-r", "insert"],
)

course.add(
    name="review-error-table", title="Review · Name every error code", par=127, ext="h",
    task="errors.h is getting a table of names for its error codes, and a round of cleanups on the way. "
         "This reviews Projects 00 to 06: par uses nothing from later projects.",
    steps=[
        "Include <stdbool.h> too, on the line below <stddef.h>.",
        "This is version 4 of the codes: bump NETD_ERR_VERSION.",
        "ERR_PRASE is a typo: make it ERR_PARSE.",
        "Add ERR_TLS at the end of the enum.",
        "Fill netd_err_names with the codes' names, one per line, in the enum's order: \"ok\", \"nomem\" "
        "and so on. Each name is the code in lowercase, without ERR_.",
        "The table itself is constant too: make it const char *const.",
        "netd_retryable() returns a bool, not an int.",
        "A refused connection won't come back by retrying, but an I/O error might: test for ERR_IO "
        "instead of ERR_REFUSED.",
        "Put extern in front of the first two prototypes.",
        "Rename netd_strerror()'s len parameter to buflen.",
        "netd_errname() takes an enum netd_err e, like the others, not an int e.",
        "netd_perror() is deprecated: comment its prototype out.",
    ],
    start=text("""
        /* errors.h: error codes for netd */
        #ifndef NETD_ERRORS_H
        #define NETD_ERRORS_H

        #include <stddef.h>

        #define NETD_ERR_VERSION 3

        enum netd_err {
            ERR_OK,
            ERR_NOMEM,
            ERR_IO,
            ERR_PRASE,
            ERR_TIMEOUT,
            ERR_REFUSED,
            ERR_AUTH,
        };

        /* netd_err_names[e] is the name of code e */
        static const char *netd_err_names[] = {
        };

        static inline int netd_retryable(enum netd_err e)
        {
            return e == ERR_TIMEOUT || e == ERR_REFUSED;
        }

        int netd_strerror(enum netd_err e, char *buf, size_t len);
        const char *netd_errname(int e);
        int netd_perror(const char *prefix, enum netd_err e);

        #endif
    """),
    target=text("""
        /* errors.h: error codes for netd */
        #ifndef NETD_ERRORS_H
        #define NETD_ERRORS_H

        #include <stddef.h>
        #include <stdbool.h>

        #define NETD_ERR_VERSION 4

        enum netd_err {
            ERR_OK,
            ERR_NOMEM,
            ERR_IO,
            ERR_PARSE,
            ERR_TIMEOUT,
            ERR_REFUSED,
            ERR_AUTH,
            ERR_TLS,
        };

        /* netd_err_names[e] is the name of code e */
        static const char *const netd_err_names[] = {
            "ok",
            "nomem",
            "io",
            "parse",
            "timeout",
            "refused",
            "auth",
            "tls",
        };

        static inline bool netd_retryable(enum netd_err e)
        {
            return e == ERR_TIMEOUT || e == ERR_IO;
        }

        extern int netd_strerror(enum netd_err e, char *buf, size_t buflen);
        extern const char *netd_errname(enum netd_err e);
        // int netd_perror(const char *prefix, enum netd_err e);

        #endif
    """),
    hint="Fix the enum first, then copy its lines into the table with a text object. Record the change "
         "for one line and replay it with a count. Text that's already in the file, like const or enum "
         "netd_err, is cheaper to yank and put than to type.",
    uses=["macro", "replay", "brace", "y", "p", "case", "increment", "block-insert", "comment", "x"],
)

course.add(
    name="review-seed-data", title="Review · Seed the test database", par=107, ext="sql",
    task="seed.sql fills a test database before the integration tests run. Add the missing rows and "
         "apply the fixes below. This reviews Projects 00 to 06: par uses nothing from later projects.",
    steps=[
        "begin and commit in uppercase, like the other keywords.",
        "Fix the typo in user 2's email: example.com.",
        "Add users 3 to 8 below user 2: the same row, with the next id and the next number in the email.",
        "Only the last user row ends the statement with ;. The others end with a comma.",
        "The USB-C cable costs 50 cents more now: 1250.",
        "sku-1003 in uppercase, like the other SKUs.",
        "SQL escapes a quote inside a string by doubling it: 'Kid''s tablet'.",
        "The desk lamp is on sale: 500 cents off.",
        "SKU-1006 is discontinued: delete its row, so that the statement ends after SKU-1005.",
        "Replace the tags comment with the statement's first line: INSERT INTO tags (name) VALUES",
        "Turn each tag into an indented row: ('keyboards'), and so on.",
        "The last tag row ends the statement with ; instead of a comma.",
    ],
    start=text("""
        -- seed.sql: fixtures for the integration tests
        begin;

        INSERT INTO users (id, email, role) VALUES
            (1, 'user01@example.com', 'admin'),
            (2, 'user02@exmaple.com', 'member');

        INSERT INTO products (sku, name, price_cents) VALUES
            ('SKU-1001', 'Mechanical keyboard', 8900),
            ('SKU-1002', 'USB-C cable', 1200),
            ('sku-1003', 'Kid's tablet', 12900),
            ('SKU-1004', '27" monitor', 32900),
            ('SKU-1005', 'Desk lamp', 3400),
            ('SKU-1006', 'Laptop stand', 4500);

        -- tags, pasted from the product sheet
        keyboards
        cables
        tablets
        monitors
        lighting
        office

        commit;
    """),
    target=text("""
        -- seed.sql: fixtures for the integration tests
        BEGIN;

        INSERT INTO users (id, email, role) VALUES
            (1, 'user01@example.com', 'admin'),
            (2, 'user02@example.com', 'member'),
            (3, 'user03@example.com', 'member'),
            (4, 'user04@example.com', 'member'),
            (5, 'user05@example.com', 'member'),
            (6, 'user06@example.com', 'member'),
            (7, 'user07@example.com', 'member'),
            (8, 'user08@example.com', 'member');

        INSERT INTO products (sku, name, price_cents) VALUES
            ('SKU-1001', 'Mechanical keyboard', 8900),
            ('SKU-1002', 'USB-C cable', 1250),
            ('SKU-1003', 'Kid''s tablet', 12900),
            ('SKU-1004', '27" monitor', 32900),
            ('SKU-1005', 'Desk lamp', 2900);

        INSERT INTO tags (name) VALUES
            ('keyboards'),
            ('cables'),
            ('tablets'),
            ('monitors'),
            ('lighting'),
            ('office');

        COMMIT;
    """),
    hint="Fix user 2 before you copy it. A macro that copies a row and bumps both numbers with Ctrl-a "
         "makes the rest. Ctrl-a and Ctrl-x take a count, and change the first number at or after the "
         "cursor. A second macro turns the tags into rows.",
    setup=["setlocal indentexpr="],  # SQL's indent rules would push a typed INSERT line in by 4 spaces
    uses=["counter", "macro", "replay", "increment", "case", "quote", "visual-line", "yank0", "indent", "r"],
)

course.run()
