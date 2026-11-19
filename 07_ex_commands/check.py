"""Exercises for Project 07. Run:  python3 check.py   (python3 check.py 3 plays exercise 3)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "common"))
from trainer import Course, text  # noqa: E402

# Completion (Ctrl-n, Ctrl-x Ctrl-l) normally also searches other windows, which would let you copy
# lines straight out of the target. In these exercises it only searches your own file.
OWN_FILE_ONLY = ["setlocal complete=."]

course = Course("Project 07 · Ex commands and :s: change every line that matches", __file__,
                done_message="On to 08_insert_cmdline, where you'll fix things without leaving Insert mode.")

course.add(
    name="space-after-commas", title="Space after every comma", par=11, setup=OWN_FILE_ONLY, ext="py",
    task="Add a space after every comma in the file.",
    start=text("""
        primes = [2,3,5,7,11]
        origin = (0,0)
        print(primes,origin)
    """),
    target=text("""
        primes = [2, 3, 5, 7, 11]
        origin = (0, 0)
        print(primes, origin)
    """),
    hint="One :s can cover the whole file if you give it the range %. Without the g flag it only "
         "changes the first match on each line.",
    uses=["subst", "range"],
)
course.add(
    name="rename-in-function", title="Rename inside one function", par=17, setup=OWN_FILE_ONLY, ext="py",
    task="In variance(), total is really a sum of squares. Rename it to sum_sq there, "
         "and leave mean() and report() alone.",
    cursor=(8, 1),
    start=text("""
        def mean(xs):
            total = 0
            for x in xs:
                total += x
            return total / len(xs)


        def variance(xs):
            m = mean(xs)
            total = 0
            for x in xs:
                total += (x - m) ** 2
            return total / len(xs)


        def report(xs):
            total = sum(xs)
            print("total:", total, "mean:", mean(xs))
    """),
    target=text("""
        def mean(xs):
            total = 0
            for x in xs:
                total += x
            return total / len(xs)


        def variance(xs):
            m = mean(xs)
            sum_sq = 0
            for x in xs:
                sum_sq += (x - m) ** 2
            return sum_sq / len(xs)


        def report(xs):
            total = sum(xs)
            print("total:", total, "mean:", mean(xs))
    """),
    hint="Give :s a range that covers only variance(). The relative line numbers tell you how many lines "
         "that is, and a count typed before : turns into a range for you.",
    uses=["range", "subst"],
)
course.add(
    name="match-case", title="Mind the case", par=17, setup=OWN_FILE_ONLY, ext="java",
    task="Rename the variable log to logger. The type Log, LogFactory and getLog must not change.",
    start=text("""
        class App {
            Log log = LogFactory.getLog(App.class);

            void run() {
                log.info("starting");
                log.debug("config loaded");
                log.info("done");
            }
        }
    """),
    target=text("""
        class App {
            Log logger = LogFactory.getLog(App.class);

            void run() {
                logger.info("starting");
                logger.debug("config loaded");
                logger.info("done");
            }
        }
    """),
    hint="ignorecase is on, so a lowercase pattern also matches Log. :s has a flag that makes one command "
         "case-sensitive again (or put \\C in the pattern).",
    uses=["subst-flags", "subst", "range"],
)
course.add(
    name="star-rename", title="Rename the word under the cursor", par=10, setup=OWN_FILE_ONLY, ext="c",
    task="The cursor is on the parameter n. Rename it to len everywhere it's used.",
    cursor=(1, 31),
    start=text("""
        double mean(const int *a, int n) {
            if (n == 0)
                return 0;
            long sum = 0;
            for (int i = 0; i < n; i++)
                sum += a[i];
            return (double) sum / n;
        }
    """),
    target=text("""
        double mean(const int *a, int len) {
            if (len == 0)
                return 0;
            long sum = 0;
            for (int i = 0; i < len; i++)
                sum += a[i];
            return (double) sum / len;
        }
    """),
    hint="The pattern n alone would also hit mean, int and return. * searches for the whole word under "
         "the cursor, and :s with an empty pattern reuses the last search.",
    uses=["star", "subst", "range"],
)
course.add(
    name="backtick-calls", title="Wrap every call in backticks", par=17, setup=OWN_FILE_ONLY, ext="md",
    task="Format every function call as inline code: put a backtick on each side of name().",
    start=text("""
        ## Usage

        Call init() once, then run().
        Call cleanup() when you're done.
        If run() fails, call reset() first.
    """),
    target=text("""
        ## Usage

        Call `init()` once, then `run()`.
        Call `cleanup()` when you're done.
        If `run()` fails, call `reset()` first.
    """),
    hint="In the replacement, & stands for the whole match. Match a word followed by (), and replace it "
         "with itself wrapped in backticks.",
    uses=["subst", "range"],
)
course.add(
    name="swap-names", title="Swap two fields", par=23, setup=OWN_FILE_ONLY, ext="txt",
    task="Turn each \"Last, First\" line into \"First Last\".",
    start=text("""
        Lovelace, Ada
        Turing, Alan
        Hopper, Grace
        Ritchie, Dennis
        Liskov, Barbara
    """),
    target=text("""
        Ada Lovelace
        Alan Turing
        Grace Hopper
        Dennis Ritchie
        Barbara Liskov
    """),
    hint="Capture each name in a group, then write them back as \\2 \\1. Very magic (\\v at the start of "
         "the pattern) lets you write the groups as ( ) without backslashes.",
    uses=["very-magic", "subst", "range"],
)
course.add(
    name="snake-to-camel", title="snake_case to camelCase", par=18, setup=OWN_FILE_ONLY, ext="java",
    task="These names came from Python. Convert them to Java's camelCase: max_retry_count becomes "
         "maxRetryCount.",
    start=text("""
        int max_retry_count = 3;
        String user_name = "ada";
        boolean is_logged_in = false;
        if (is_logged_in) retry(user_name, max_retry_count);
    """),
    target=text("""
        int maxRetryCount = 3;
        String userName = "ada";
        boolean isLoggedIn = false;
        if (isLoggedIn) retry(userName, maxRetryCount);
    """),
    hint="Match an underscore and the character after it, and replace both with just that character, "
         "uppercased. In the replacement, \\u uppercases the next character.",
    uses=["replace-case", "very-magic", "subst", "range"],
)
course.add(
    name="double-sizes", title="Double every number", par=27, setup=OWN_FILE_ONLY, ext="c",
    task="Make the UI twice as big for a high-DPI screen: double every number in the file.",
    start=text("""
        /* button sizes, in pixels */
        int widths[]  = {12, 40, 8, 16, 24};
        int heights[] = {6, 20, 4, 8, 12};
        int padding   = 3;
    """),
    target=text("""
        /* button sizes, in pixels */
        int widths[]  = {24, 80, 16, 32, 48};
        int heights[] = {12, 40, 8, 16, 24};
        int padding   = 6;
    """),
    hint="A replacement that starts with \\= is an expression, and submatch(0) is the whole match. "
         "Expressions can do arithmetic.",
    uses=["expr-replace", "subst", "range"],
)
course.add(
    name="keep-errors", title="Keep only the errors", par=11, setup=OWN_FILE_ONLY, ext="log",
    task="Keep only the ERROR lines. Delete everything else.",
    start=text("""
        09:14:02 INFO  server started on :8080
        09:14:05 ERROR could not open config.yml
        09:15:11 INFO  no errors in the last hour
        09:16:40 WARN  disk 91% full
        09:17:02 ERROR connection refused (db)
        09:17:30 INFO  retrying in 5 s
    """),
    target=text("""
        09:14:05 ERROR could not open config.yml
        09:17:02 ERROR connection refused (db)
    """),
    hint=":g/pattern/d deletes the lines that match. Its twin, :v, runs the command on the lines that "
         "don't match.",
    uses=["vglobal"],
)
course.add(
    name="python3-prints", title="Port print to Python 3", par=21, setup=OWN_FILE_ONLY, ext="py",
    task="Port the Python 2 print statements to Python 3: print \"x\", y becomes print(\"x\", y).",
    start=text("""
        import os, sys

        src, dst = sys.argv[1], sys.argv[2]
        print "Copying", src, "to", dst
        files = os.listdir(src)
        count = len(files)
        print "Found", count, "files"
        os.system("cp -r %s %s" % (src, dst))
        print "Done"
    """),
    target=text("""
        import os, sys

        src, dst = sys.argv[1], sys.argv[2]
        print("Copying", src, "to", dst)
        files = os.listdir(src)
        count = len(files)
        print("Found", count, "files")
        os.system("cp -r %s %s" % (src, dst))
        print("Done")
    """),
    hint="On one line you'd jump to the first space, replace it with (, and append ). "
         ":g/pattern/normal runs exactly those keys on every matching line.",
    uses=["global", "normal", "f", "r", "insert"],
)
course.add(
    name="sort-scores", title="Sort by the last column", par=10, setup=OWN_FILE_ONLY, ext="csv",
    task="Sort the scoreboard (id,name,score) by score, highest first.",
    start=text("""
        1042,ada,88
        1007,alan,95
        1123,grace,72
        1088,linus,100
        1015,dennis,9
        1061,barbara,91
    """),
    target=text("""
        1088,linus,100
        1007,alan,95
        1061,barbara,91
        1042,ada,88
        1123,grace,72
        1015,dennis,9
    """),
    hint="n sorts by the first number on each line, ! reverses the order, and a /pattern/ makes :sort skip "
         "past the match first. Ex commands can be abbreviated, and the spaces between flags are optional.",
    uses=["sort"],
)
course.add(
    name="mirror-art", title="Mirror the picture", par=9, setup=OWN_FILE_ONLY, ext="txt",
    task="Finish the diamond: below the middle line, add the top four lines again in reverse order.",
    start=text("""
            *
           *+*
          *+o+*
         *+o#o+*
        *+o#@#o+*
    """),
    target=text("""
            *
           *+*
          *+o+*
         *+o#o+*
        *+o#@#o+*
         *+o#o+*
          *+o+*
           *+*
            *
    """),
    hint=":t copies a line, and :g runs a command on each matching line, one at a time, top to bottom. "
         "If each of the top four lines is copied to just below the middle line in turn, what order do the "
         "copies end up in?",
    uses=["global", "copy-move", "range"],
)

course.add(
    name="review-backup-script", title="Review · Ship the backup script", par=107, setup=OWN_FILE_ONLY,
    ext="py",
    task="backup.py worked on someone's laptop. Get it ready to run every night on the server. This "
         "reviews Projects 00 to 07: par uses nothing from later projects.",
    steps=[
        "Run it with python3.",
        "Nothing uses sys: delete its import.",
        "Sort the other imports.",
        "/var/www moved to /srv/www.",
        "Keep two weeks of backups: KEEP = 14.",
        "Name the folders like the old backups, without dashes: %Y%m%d.",
        "Rename src to source, in backup() and in main(). SOURCES stays.",
        "Delete the lines marked # DEBUG.",
        "Log instead of printing: every print( becomes log.info(.",
        "Let logging do the formatting: pass the value as an argument instead of using %, as in "
        "log.info(\"pruning %s\", day).",
        "Free space before copying: main() calls prune() first.",
        "PEP 8 wants two blank lines around top-level code: wherever there's one blank line, make it two.",
    ],
    start=text("""
        #!/usr/bin/env python
        """ + '"""Nightly backup: copy each source into a dated folder, and keep the newest few."""' + """

        import time
        import sys
        import shutil
        import logging
        import os

        SOURCES = ["/etc", "/home", "/var/www"]
        DEST = "/mnt/backup"
        KEEP = 7
        log = logging.getLogger("backup")

        def stamp():
            return time.strftime("%Y-%m-%d")

        def backup(src):
            print("backing up %s" % src)
            dst = os.path.join(DEST, stamp(), os.path.basename(src))
            print("copying to %s" % dst)  # DEBUG
            shutil.copytree(src, dst)
            return dst

        def prune():
            days = sorted(os.listdir(DEST))
            print("found %d days" % len(days))  # DEBUG
            for day in days[:-KEEP]:
                print("pruning %s" % day)
                shutil.rmtree(os.path.join(DEST, day))

        def main():
            logging.basicConfig(level=logging.INFO)
            for src in SOURCES:
                backup(src)
            prune()

        if __name__ == "__main__":
            main()
    """),
    target=text("""
        #!/usr/bin/env python3
        """ + '"""Nightly backup: copy each source into a dated folder, and keep the newest few."""' + """


        import logging
        import os
        import shutil
        import time


        SOURCES = ["/etc", "/home", "/srv/www"]
        DEST = "/mnt/backup"
        KEEP = 14
        log = logging.getLogger("backup")


        def stamp():
            return time.strftime("%Y%m%d")


        def backup(source):
            log.info("backing up %s", source)
            dst = os.path.join(DEST, stamp(), os.path.basename(source))
            shutil.copytree(source, dst)
            return dst


        def prune():
            days = sorted(os.listdir(DEST))
            for day in days[:-KEEP]:
                log.info("pruning %s", day)
                shutil.rmtree(os.path.join(DEST, day))


        def main():
            logging.basicConfig(level=logging.INFO)
            prune()
            for source in SOURCES:
                backup(source)


        if __name__ == "__main__":
            main()
    """),
    hint="Each :s or :g covers the whole file in one go, so do the rest by hand first and the Ex commands "
         "where they're shortest. * picks up the word under the cursor, whole words only, and an empty "
         ":s pattern reuses it. :t. copies a line below itself.",
    uses=["subst", "global", "sort", "copy-move", "star", "range", "insert", "increment", "dd", "x"],
)

course.add(
    name="review-orders-csv", title="Review · Import the old orders", par=125, setup=OWN_FILE_ONLY,
    ext="csv",
    task="orders.csv comes from the old shop. Make it fit the new shop's importer. This reviews Projects "
         "00 to 07: par uses nothing from later projects.",
    steps=[
        "Delete the comment on line 1.",
        "Commas instead of semicolons.",
        "Delete the test orders.",
        "Dates in ISO format: 03/02/2024 (day/month/year) becomes 2024-02-03.",
        "Sort the orders by date, under the header.",
        "Country codes in uppercase.",
        "Amounts in cents: 19.90 becomes 1990.",
        "The header calls that column amount_cents.",
        "And it calls the customer column name.",
        "The new shop's order ids start at 5001: 1001 becomes 5001, 1002 becomes 5002, and so on.",
        "A refund counts against the total: make the refunded order's amount negative.",
        "Linus Torvalds was charged in the wrong currency: his amount is 50 cents more.",
    ],
    start=text("""
        # orders exported from the old shop, March 2024
        order_id;date;customer;country;amount;status
        1001;03/02/2024;Ada Lovelace;GB;19.90;paid
        1002;05/02/2024;Test User;GB;1.00;test
        1003;11/02/2024;Grace Hopper;us;120.00;paid
        1004;09/02/2024;Alan Turing;GB;45.50;refunded
        1005;14/02/2024;Linus Torvalds;fi;8.99;paid
        1006;12/02/2024;Test User;de;1.00;test
        1007;20/02/2024;Margaret Hamilton;US;300.00;paid
        1008;18/02/2024;Dennis Ritchie;us;12.00;paid
    """),
    target=text("""
        order_id,date,name,country,amount_cents,status
        5001,2024-02-03,Ada Lovelace,GB,1990,paid
        5004,2024-02-09,Alan Turing,GB,-4550,refunded
        5003,2024-02-11,Grace Hopper,US,12000,paid
        5005,2024-02-14,Linus Torvalds,FI,949,paid
        5008,2024-02-18,Dennis Ritchie,US,1200,paid
        5007,2024-02-20,Margaret Hamilton,US,30000,paid
    """),
    hint="Very magic groups put the date's parts back in any order. :sort with a /pattern/ sorts on what "
         "comes after the match, and \\U uppercases the replacement. Ctrl-a takes a count, in a Visual "
         "block too.",
    uses=["subst", "very-magic", "global", "sort", "replace-case", "range", "block-edit", "increment",
          "iw", "dd"],
)

course.run()
