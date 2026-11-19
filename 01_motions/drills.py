"""Drills for Project 01: short problems that practice one command at a time.
Play them with:  python3 check.py drill      (the reference solutions are in ../solutions/drills/)"""
from trainer import Drills, text

drills = Drills(__file__)

# ---------- W B E ----------

bigword = drills.command(
    "bigword", "W  B  E", "move by WORDs (anything between spaces)",
    """A WORD is a run of anything that isn't a space: in "x = cfg.get('port')" the WORDs are x, = and
    cfg.get('port'). W jumps to the start of the next WORD, B back to the start of this (or the previous)
    WORD, and E to the end of this (or the next) WORD. Small words (w b e) stop at every run of
    punctuation, so in paths, URLs, dotted names and flags like -O2 the capital versions take far fewer
    presses. After an operator, W and B are exclusive and E is inclusive: dW deletes the WORD and the
    space after it, dE stops at the WORD's last character, and yE copies a WORD without the space.""",
    examples=[("W", "next WORD"), ("3W", "three WORDs on"), ("B", "back to this WORD's start"),
              ("E", "end of this WORD"), ("dW", "delete a WORD and its space"), ("cB", "change back to the WORD's start")],
)
bigword.add(
    title="Drop the output flag", par=3, ext="sh",
    task="Print the response instead of saving it: remove -o users.json from the end of the line.",
    start="curl https://my-api.example.com/v1/users?page=2 -o users.json",
    target="curl https://my-api.example.com/v1/users?page=2",
    hint="The URL is a single WORD, so W hops over it in one press. 2W lands on -o, and D deletes to the end "
         "of the line.",
    uses=["count", "d"],
)
bigword.add(
    title="One more folder", par=8, ext="sh", cursor=(1, 39),
    task="Also back up ~/src: add ~/src (and a space) just before ~/photos. The cursor starts at the end of "
         "the line.",
    start="tar -czf backup.tar.gz ~/docs ~/photos",
    target="tar -czf backup.tar.gz ~/docs ~/src ~/photos",
    hint="B jumps back to the start of the WORD the cursor is in, which is the ~ of ~/photos. Insert there "
         "with i.",
    uses=["insert"],
)
bigword.add(
    title="Compare with the backup", par=7, ext="sh",
    task="Diff against the backup copy: add .bak to the end of the first file name, so it reads "
         "./notes/old-notes.txt.bak.",
    start="diff ./notes/old-notes.txt ./notes/new-notes.txt",
    target="diff ./notes/old-notes.txt.bak ./notes/new-notes.txt",
    hint="E jumps to the end of a WORD. From diff, the first E stays in diff and the second reaches the end "
         "of the first path. Then append with a.",
    uses=["count", "insert"],
)
bigword.add(
    title="No optimizing", par=4, ext="sh",
    task="Build without optimization: delete the -O2 flag and the space after it.",
    start="gcc -Wall -Wextra -O2 -g main.c -o main",
    target="gcc -Wall -Wextra -g main.c -o main",
    hint="Every flag is one WORD. 3W reaches -O2, and dW deletes a WORD plus the space after it. (dw would "
         "only take the -, which is a word of its own.)",
    uses=["count", "d"],
)
bigword.add(
    title="Another branch", par=13, ext="sh",
    task="Create the branch fix/login instead of feature/login-form.",
    start="git checkout -b feature/login-form origin/main",
    target="git checkout -b fix/login origin/main",
    hint="3W lands on the branch name. cW changes the whole WORD, slashes and dashes included, and leaves "
         "the space before origin/main alone.",
    uses=["count", "c"],
)
bigword.add(
    title="Same host twice", par=4, ext="sh", cursor=(1, 11),
    task="Log in to the host you just pinged: copy api.staging.example.com to the end of line 2, after the "
         "@. The cursor starts on the a of api.",
    start=text("""
        ping -c 3 api.staging.example.com > /dev/null
        ssh deploy@
    """),
    target=text("""
        ping -c 3 api.staging.example.com > /dev/null
        ssh deploy@api.staging.example.com
    """),
    hint="yE copies from the cursor to the end of the WORD, without the space after it (yW would take the "
         "space too). Go down a line; j lands on the @, and p puts the copy after it.",
    uses=["y", "p"],
)
bigword.add(
    title="Fewer configure options", par=5, ext="sh",
    task="Drop the two options --enable-debug and --with-x (and the spaces after them).",
    start="./configure --prefix=$HOME/.local --enable-debug --with-x CFLAGS=-O2",
    target="./configure --prefix=$HOME/.local CFLAGS=-O2",
    hint="2W gets you to --enable-debug. A count works after d too: d2W deletes two WORDs.",
    uses=["count", "d"],
)
bigword.add(
    title="Replace the expression", par=6, ext="java", cursor=(1, 51),
    task="name already holds the cleaned-up name. Replace everything after = with name, keeping the "
         "semicolon. The cursor starts on the ;.",
    start="String label = item.getName().trim().toLowerCase();",
    target="String label = name;",
    hint="The whole call chain, semicolon included, is one WORD, and B goes back to its start. cB changes "
         "from there up to the cursor, but not the ; under it.",
    uses=["c"],
)
bigword.add(
    title="Remove two flags", par=6, ext="sh",
    task="Stop debugging: remove -g and -O0 (and the space after each).",
    start="cc -Wall -g main.c -O0 util.c -o app",
    target="cc -Wall main.c util.c -o app",
    hint="2W reaches -g and dW deletes it. W skips to the next WORD, which is -O0, and . repeats the delete.",
    uses=["count", "d", "dot"],
)
bigword.add(
    title="A debug build", par=14, ext="sh",
    task="Make a debug build: name the output build/app-debug and add -g at the end of the line.",
    start="gcc -O2 -o build/app src/main.c",
    target="gcc -O2 -o build/app-debug src/main.c -g",
    hint="4E reaches the end of build/app (count the WORDs: gcc, -O2, -o, build/app). Append -debug with a, "
         "then A adds -g at the end of the line.",
    uses=["count", "insert"],
)

bigword.add(
    title="Drop the logger name", par=3, ext="log", cursor=(1, 38),
    task="Shorten the line for the bug report: delete the logger name cache.redis.pool: and the space after "
         "it. The cursor starts on the p of pool.",
    start="2026-11-05 10:22:01 WARN cache.redis.pool: retrying connection (attempt 3 of 5)",
    target="2026-11-05 10:22:01 WARN retrying connection (attempt 3 of 5)",
    hint="The logger name, dots and colon included, is one WORD. B goes back to its start from anywhere "
         "inside it, and dW deletes it with its space.",
    uses=["d"],
)
bigword.add(
    title="This year's table", par=8, ext="sql",
    task="Query this year's table: change analytics.events to analytics.events_2026.",
    start="SELECT user_id, count(*) FROM analytics.events WHERE day = '2026-11-04' GROUP BY user_id;",
    target="SELECT user_id, count(*) FROM analytics.events_2026 WHERE day = '2026-11-04' GROUP BY user_id;",
    hint="Count the WORDs: SELECT, user_id, count(*), FROM, analytics.events. A count before E jumps to the "
         "end of the fifth one, and a appends after it.",
    uses=["count", "insert"],
)
bigword.add(
    title="One e too many", par=3, ext="sh",
    task="Fix the typo in the folder name: vim-coursee should be vim-course.",
    start="cd ~/school/vim-coursee && python3 progress.py",
    target="cd ~/school/vim-course && python3 progress.py",
    hint="The extra e is the last character of the path, which is the second WORD. A count before E lands "
         "right on it.",
    uses=["count", "x"],
)
bigword.add(
    title="Leave the crate out", par=4, ext="toml",
    task='Remove "crates/legacy-api", (and the space after it) from the workspace members.',
    start=text("""
        [workspace]
        members = ["crates/core", "crates/cli", "crates/legacy-api", "crates/web"]
    """),
    target=text("""
        [workspace]
        members = ["crates/core", "crates/cli", "crates/web"]
    """),
    hint="W doesn't stop at the end of a line: from [workspace], count the WORDs on into line 2 (members, =, "
         "and the two crates before it). Then dW.",
    uses=["count", "d"],
)
bigword.add(
    title="Default dpi", par=4, ext="py", cursor=(1, 69),
    task="Use the default dpi and background: delete dpi=300, transparent=True, (up to bbox_inches). The "
         "cursor starts on the last ).",
    start='plt.savefig("out.png", dpi=300, transparent=True, bbox_inches="tight")',
    target='plt.savefig("out.png", bbox_inches="tight")',
    hint="B goes back to the start of the last WORD, bbox_inches=. d2B deletes the two WORDs before it, and "
         "since B is exclusive, the b under the cursor stays.",
    uses=["count", "d"],
)
bigword.add(
    title="Quote the variables", par=10, ext="sh",
    task='Quote both arguments so paths with spaces work: the line should read mv "$1" "$BACKUP_DIR/$1.old".',
    start="mv $1 $BACKUP_DIR/$1.old",
    target='mv "$1" "$BACKUP_DIR/$1.old"',
    hint="Insert one opening quote with i, then W and . put the next one. The closing quote of $1 goes "
         "just before the space, one character to the left, and the last one goes at the end of the line.",
    uses=["insert", "dot"],
)
bigword.add(
    title="Install it the same way", par=8, ext="dockerfile",
    task="Install git the same way as curl: line 2 should read RUN apt-get install -y "
         "--no-install-recommends git.",
    start=text("""
        RUN apt-get update && apt-get install -y --no-install-recommends curl
        RUN apt-get install git
    """),
    target=text("""
        RUN apt-get update && apt-get install -y --no-install-recommends curl
        RUN apt-get install -y --no-install-recommends git
    """),
    hint="6W reaches -y, and y2W copies both flags with the spaces after them. Line 2 is shorter, so j lands "
         "at its end, in git; B goes back to the g, and P puts the flags in front.",
    uses=["count", "y", "p"],
)
bigword.add(
    title="Compressed logs", par=11, ext="sh",
    task="The old logs are compressed now: add .gz to each of the three file names.",
    start="zcat access.log.1 access.log.2 access.log.3 | grep -c POST",
    target="zcat access.log.1.gz access.log.2.gz access.log.3.gz | grep -c POST",
    hint="2E lands on the end of the first name, and a types .gz. From there, E goes to the end of the next "
         "WORD, and . appends .gz again.",
    uses=["count", "insert", "dot"],
)
bigword.add(
    title="Restore, don't overwrite", par=6, ext="sh",
    task="You meant to restore the backup, not overwrite it: swap the two paths, so the line reads "
         "cp backups/app-2026-11-04.db app.db.",
    start="cp app.db backups/app-2026-11-04.db",
    target="cp backups/app-2026-11-04.db app.db",
    hint="Cut app.db together with the space in front of it, so it can go back after the other path with "
         "its space. From the space after cp, dE deletes up to the end of the next WORD. Then $ and p.",
    uses=["d", "line", "p"],
)
bigword.add(
    title="A release build", par=7, ext="mk",
    task="Build without debug info: remove -g (and the space after it) from both lines.",
    start=text("""
        CFLAGS = -O2 -g -Wall
        LDFLAGS = -g -lm
    """),
    target=text("""
        CFLAGS = -O2 -Wall
        LDFLAGS = -lm
    """),
    hint="3W reaches the first -g and dW deletes it. j lands on -lm, one WORD past the second -g, so B "
         "steps back onto it and . repeats the delete.",
    uses=["count", "d", "dot"],
)

# ---------- 0 ^ $ ----------

line = drills.command(
    "line", "0  ^  $", "line start, first non-blank, line end",
    """0 jumps to column 1, ^ to the first character that isn't a space (where the code starts on an
    indented line), and $ to the last character of the line. After an operator, 0 and ^ are exclusive
    backward motions, so d0 and c^ never include the character under the cursor, and d0 takes the
    indentation while c^ keeps it. $ is inclusive: d$ (the same as D) deletes through the last character.
    $ takes a count: 2$ is the end of the next line, so 2D deletes to there. $ then i inserts before the
    last character, which is how you add to the end of a list or call. (In Neovim, Y is y$.)""",
    examples=[("^", "where the code starts"), ("$", "last character"), ("0", "column 1"),
              ("d0", "delete back to column 1"), ("c^", "change back to the indent, keeping it"),
              ("$i", "insert before the last character")],
)
line.add(
    title="Add to the list", par=6, ext="py",
    task="Add 11 to the end of the list.",
    start="primes = [2, 3, 5, 7]",
    target="primes = [2, 3, 5, 7, 11]",
    hint="$ goes to the last character, the ]. i inserts before it.",
    uses=["insert"],
)
line.add(
    title="A bigger type", par=7, ext="java", cursor=(1, 33),
    task="The result can overflow: change int to long. The cursor starts at the end of the line.",
    start="    int count = items.size() * 2;",
    target="    long count = items.size() * 2;",
    hint="^ jumps to the first non-blank character, the i of int. Then cw changes the word.",
    uses=["c"],
)
line.add(
    title="Close the box", par=3, ext="txt", cursor=(2, 11),
    task="The left wall of the box is missing: put a | in column 1 of line 2. The cursor starts at the end "
         "of line 2.",
    start=text("""
        +---------+
           hello  |
        +---------+
    """),
    target=text("""
        +---------+
        |  hello  |
        +---------+
    """),
    hint="^ would stop on the h. 0 goes all the way to column 1, where r can replace the space.",
    uses=["r"],
)
line.add(
    title="Paste without the prompt", par=2, ext="sh", cursor=(1, 7),
    task="This was copied from a terminal. Delete the indentation and the $ prompt, so the line starts "
         "with pip. The cursor starts on the p of pip.",
    start="    $ pip install neovim",
    target="pip install neovim",
    hint="Everything before the cursor goes, spaces included. d0 deletes back to column 1.",
    uses=["d"],
)
line.add(
    title="Drop the assignment", par=2, ext="py", cursor=(2, 14),
    task="The result is never used. Delete result = but keep the indentation. The cursor starts on the p "
         "of process.",
    start=text("""
        def run(items):
            result = process(items)
    """),
    target=text("""
        def run(items):
            process(items)
    """),
    hint="^ is the first non-blank, and d^ deletes back to it, leaving the indentation and the character "
         "under the cursor alone.",
    uses=["d"],
)
line.add(
    title="Print it instead", par=7, ext="py", cursor=(2, 17),
    task="Swap the logger call for a plain print, keeping the indentation and the arguments. The cursor "
         "starts on the (.",
    start=text("""
        if key not in cache:
            logger.debug("cache miss for %s", key)
    """),
    target=text("""
        if key not in cache:
            print("cache miss for %s", key)
    """),
    hint="Everything to replace lies between the first non-blank and the cursor. c^ changes exactly that "
         "and keeps the indent.",
    uses=["c"],
)
line.add(
    title="$ takes a count", par=2, ext="txt", cursor=(1, 27),
    task="Delete the second sentence, Bring your laptop and charger. It runs from the cursor (on the B) to "
         "the end of line 2.",
    start=text("""
        The meeting is on Monday. Bring your
        laptop and charger.
        Lunch is provided.
    """),
    target=text("""
        The meeting is on Monday.
        Lunch is provided.
    """),
    hint="2$ is the end of the next line, so d2$ deletes from the cursor to there. D is short for d$, and it "
         "takes the count too.",
    uses=["d", "count"],
)
line.add(
    title="Drop the last argument", par=4, ext="py",
    task="Stop marking the notification urgent: remove , urgent=True.",
    start="notify(user, message, urgent=True)",
    target="notify(user, message)",
    hint="Start from the end: $ lands on the ). dF, deletes back to the last comma and leaves the ) the "
         "cursor is on.",
    uses=["d", "f"],
)
line.add(
    title="Fix the last word", par=10, ext="txt",
    task="Change platform to machine, keeping the period.",
    start="The tests pass on every platform.",
    target="The tests pass on every machine.",
    hint="$ goes to the period. cb changes back to the start of the word, without the period under the "
         "cursor.",
    uses=["c", "word"],
)
line.add(
    title="Return it instead", par=12, ext="py", cursor=(2, 42),
    task="Return the total instead of printing it: the line should read return compute_total(orders, "
         "tax_rate), indented as before. The cursor starts on the last ).",
    start=text("""
        def total(orders, tax_rate):
            print(compute_total(orders, tax_rate))
    """),
    target=text("""
        def total(orders, tax_rate):
            return compute_total(orders, tax_rate)
    """),
    hint="You're already on the ) that has to go, so delete it first. Then ^ jumps to print, and cf( "
         "changes print( in one go.",
    uses=["x", "c", "f"],
)

line.add(
    title="Money, not a number", par=9, ext="ts",
    task="Prices are Money objects now: change the return type from number to Money.",
    start=text("""
        function total(items: Item[]): number {
            return items.reduce((sum, item) => sum.add(item.price), Money.zero());
        }
    """),
    target=text("""
        function total(items: Item[]): Money {
            return items.reduce((sum, item) => sum.add(item.price), Money.zero());
        }
    """),
    hint="The return type is the last word before the {, which is the line's last character. $ gets you to "
         "the end, and b steps back one word.",
    uses=["word", "c"],
)
line.add(
    title="Uncomment the print", par=3, ext="py", cursor=(3, 20),
    task="Turn the commented-out print back on: delete the # and the space after it, keeping the "
         "indentation. The cursor starts at the end of line 3.",
    start=text("""
        def parse(rows):
            for row in rows:
                # print(row)
                yield row.split(",")
    """),
    target=text("""
        def parse(rows):
            for row in rows:
                print(row)
                yield row.split(",")
    """),
    hint="^ jumps to the first non-blank character, the #. From there, dw deletes the # and the space "
         "after it.",
    uses=["d", "word"],
)
line.add(
    title="A plain prompt", par=4, ext="md", cursor=(2, 26),
    task="Show a plain $ prompt in the README: replace everything before python3 with $ and a space. The "
         "cursor starts on the p of python3.",
    start=text("""
        ```
        rick@laptop vim-course % python3 check.py drill W
        ```
    """),
    target=text("""
        ```
        $ python3 check.py drill W
        ```
    """),
    hint="Everything to replace lies between column 1 and the cursor. c0 changes exactly that, and the "
         "p under the cursor stays.",
    uses=["c"],
)
line.add(
    title="Clear the placeholder", par=4, ext="py",
    task='The message will be filled in later: empty the string, so the line reads msg = "".',
    start='msg = "Something went wrong, please try again later."',
    target='msg = ""',
    hint="$ lands on the closing quote. A backward motion with d never takes the character under the "
         "cursor, so delete back till the other quote with T\".",
    uses=["d", "t"],
)
line.add(
    title="Bump the patch version", par=4, ext="c",
    task="Release the bug-fix version: change 1.4.1 to 1.4.2.",
    start='#define APP_VERSION "1.4.1"',
    target='#define APP_VERSION "1.4.2"',
    hint="The digit to change is the second-to-last character of the line. $ goes to the last one, the "
         "quote.",
    uses=["r"],
)
line.add(
    title="Rewrite the rest", par=16, ext="txt", cursor=(1, 40),
    task="Shorten the commit message: replace everything from used to struggling. with now backs off., so "
         "line 1 reads Fix the retry loop in fetch_page(): it now backs off. and Closes #142. stays on "
         "line 2. The cursor starts on the u of used.",
    start=text("""
        Fix the retry loop in fetch_page(): it used to
        sleep for one second every time, which hammered
        the server when it was already struggling.
        Closes #142.
    """),
    target=text("""
        Fix the retry loop in fetch_page(): it now backs off.
        Closes #142.
    """),
    hint="$ takes a count, and so does C (which is c$): with a count of 3, it changes from the cursor to "
         "the end of the third line.",
    uses=["c", "count"],
)
line.add(
    title="Return it", par=13, ext="js", cursor=(2, 17),
    task="Return the user instead of logging it: line 2 should read return user; (indented as before). The "
         "cursor starts on the u of user.",
    start=text("""
        function current() {
            console.log(user)
        }
    """),
    target=text("""
        function current() {
            return user;
        }
    """),
    hint="c^ changes console.log( (from the first non-blank up to the cursor) and keeps the indent. Then $ "
         "reaches the ), and r turns it into a semicolon.",
    uses=["c", "r"],
)
line.add(
    title="The comment moves down", par=7, ext="py",
    task="The comment is about tax, not the total: move it (with its two spaces) to the end of line 2.",
    start=text("""
        total = price * qty  # before discounts
        tax = total * TAX_RATE
        total += tax
    """),
    target=text("""
        total = price * qty
        tax = total * TAX_RATE  # before discounts
        total += tax
    """),
    hint="Cut from the first of the two spaces to the end of the line: t# stops on the space before the #, "
         "and h steps onto the other one. Then go down, and $ gets you to the end for p.",
    uses=["t", "d", "p"],
)
line.add(
    title="Quote the snippet", par=10, ext="md",
    task="Quote the code in your review comment: put > and a space at the very start of each of the three "
         "lines, before the indentation.",
    start=text("""
        def add(a, b):
            \"\"\"Return the sum.\"\"\"
            return a + b
    """),
    target=text("""
        > def add(a, b):
        >     \"\"\"Return the sum.\"\"\"
        >     return a + b
    """),
    hint="Type > and a space with i on line 1. On the indented lines, . inserts at the cursor, so go to "
         "column 1 first with 0 (I and ^ would stop after the indentation).",
    uses=["insert", "dot"],
)
line.add(
    title="Close the box", par=8, ext="txt", cursor=(3, 11),
    task="Fix the box's walls: line 2 needs a | in column 1 and line 3 needs a space and a | at the end. "
         "The cursor starts at the end of line 3.",
    start=text("""
        +-----------+
          install   |
        | configure
        +-----------+
    """),
    target=text("""
        +-----------+
        | install   |
        | configure |
        +-----------+
    """),
    hint="A adds to the end of line 3. Then k goes up a line, where 0 reaches column 1 (^ would stop on "
         "the i), and r puts the wall in.",
    uses=["insert", "r"],
)

# ---------- gg G {N}G ----------

gg = drills.command(
    "gg", "gg  G  {N}G", "first line, last line, line N",
    """gg goes to the first line of the file, G to the last, and a count in front of either goes to that
    line: 42G (or 42gg) is line 42, handy when a compiler reports an error there. :42 and Enter does the
    same. In Neovim they keep the cursor's column when they can (Vim would go to the first non-blank). As
    nouns they're line-wise: dG deletes from this line to the end of the file, ygg copies from here to the
    top, >G indents to the end, and they always act on whole lines wherever the cursor is on the line.""",
    examples=[("gg", "first line"), ("G", "last line"), ("8G", "line 8"), ("dG", "delete to the end of the file"),
              ("yGP", "duplicate from here to the end"), ("dgg", "delete up to the top")],
)
gg.add(
    title="Call main", par=8, ext="py",
    task="Add the missing main() call, indented, on a new line at the end of the file.",
    start=text("""
        import sys


        def main():
            print(sys.argv[1:])


        if __name__ == "__main__":
    """),
    target=text("""
        import sys


        def main():
            print(sys.argv[1:])


        if __name__ == "__main__":
            main()
    """),
    hint="G jumps to the last line, and o opens a new line below it. Neovim indents it for you after the "
         "colon.",
    uses=["o"],
)
gg.add(
    title="Add the shebang", par=14, ext="sh", cursor=(7, 1),
    task="Add #!/bin/bash as a new first line. The cursor starts on the last line.",
    start=text("""
        set -euo pipefail

        SRC=./src
        OUT=./build

        mkdir -p "$OUT"
        cp -r "$SRC"/* "$OUT"
    """),
    target=text("""
        #!/bin/bash
        set -euo pipefail

        SRC=./src
        OUT=./build

        mkdir -p "$OUT"
        cp -r "$SRC"/* "$OUT"
    """),
    hint="gg jumps to the first line, and O opens a new line above it.",
    uses=["o"],
)
gg.add(
    title="Fix line 8", par=4, ext="c",
    task="The compiler says: main.c:8:26: error: expected ';' before 'return'. Fix line 8.",
    start=text("""
        #include <stdio.h>

        int main(void) {
            int total = 0;
            for (int i = 1; i <= 10; i++) {
                total += i;
            }
            printf("%d\\n", total)
            return 0;
        }
    """),
    target=text("""
        #include <stdio.h>

        int main(void) {
            int total = 0;
            for (int i = 1; i <= 10; i++) {
                total += i;
            }
            printf("%d\\n", total);
            return 0;
        }
    """),
    hint="8G goes straight to line 8. Then append the semicolon at the end of the line.",
    uses=["count", "insert"],
)
gg.add(
    title="Book the seat below", par=4, ext="txt", cursor=(2, 12),
    task="Also book the seat in the same column on row 5: put an x in it. The cursor starts on the x in row 2.",
    start=text("""
        Row 1: [ ][ ][ ][ ][ ]
        Row 2: [ ][x][ ][ ][ ]
        Row 3: [ ][ ][ ][ ][ ]
        Row 4: [ ][ ][ ][ ][ ]
        Row 5: [ ][ ][ ][ ][ ]
    """),
    target=text("""
        Row 1: [ ][ ][ ][ ][ ]
        Row 2: [ ][x][ ][ ][ ]
        Row 3: [ ][ ][ ][ ][ ]
        Row 4: [ ][ ][ ][ ][ ]
        Row 5: [ ][x][ ][ ][ ]
    """),
    hint="5G goes to line 5, and in Neovim it keeps the cursor's column. Then replace the space with rx.",
    uses=["count", "r"],
)
gg.add(
    title="Drop the test code", par=2, ext="py", cursor=(5, 1),
    task="Delete the quick tests: everything from the cursor's line (the first print) to the end of the file.",
    start=text("""
        def slugify(title):
            return title.lower().replace(" ", "-")


        print(slugify("Hello World"))
        print(slugify("Vim Rocks"))

        print("tests done")
    """),
    target=text("""
        def slugify(title):
            return title.lower().replace(" ", "-")
    """),
    hint="G is the last line, and dG deletes whole lines from here to there. d} would stop at the blank line.",
    uses=["d"],
)
gg.add(
    title="Remove the banner", par=3, ext="ini", cursor=(3, 1),
    task="Delete the three-line banner at the top. The cursor starts on its last line.",
    start=text("""
        # ==================================
        # Generated by setup.py. Do not edit.
        # ==================================
        [server]
        port = 8080
        host = 0.0.0.0
    """),
    target=text("""
        [server]
        port = 8080
        host = 0.0.0.0
    """),
    hint="gg is a motion to the first line, so dgg deletes every line from the top down to this one.",
    uses=["d"],
)
gg.add(
    title="Repeat the chorus", par=3, ext="txt", cursor=(3, 1),
    task="Sing the chorus twice: repeat the blank line and the two Merrily lines below the song. The cursor "
         "starts on the blank line.",
    start=text("""
        Row, row, row your boat,
        gently down the stream.

        Merrily, merrily, merrily, merrily,
        life is but a dream.
    """),
    target=text("""
        Row, row, row your boat,
        gently down the stream.

        Merrily, merrily, merrily, merrily,
        life is but a dream.

        Merrily, merrily, merrily, merrily,
        life is but a dream.
    """),
    hint="yG copies whole lines from here to the end. The copy starts with a blank line, so P (above) puts "
         "it in the right place without moving first.",
    uses=["y", "p"],
)
gg.add(
    title="Indent the body", par=2, ext="py", cursor=(4, 1),
    task="The body of main() lost its indentation. Indent every line from the cursor to the end of the file "
         "by one level.",
    start=text("""
        import sys

        def main():
        args = sys.argv[1:]
        for arg in args:
            print(arg)
    """),
    target=text("""
        import sys

        def main():
            args = sys.argv[1:]
            for arg in args:
                print(arg)
    """),
    hint="> is an operator that shifts lines right, and G is a motion to the last line.",
    uses=["indent"],
)
gg.add(
    title="Simplify the body", par=10, ext="py", cursor=(2, 1),
    task="Replace the whole body of legacy_total() with return 0, indented.",
    start=text("""
        def legacy_total():
            a = compute_a()
            b = compute_b()
            return a + b
    """),
    target=text("""
        def legacy_total():
            return 0
    """),
    hint="cG changes whole lines from here to the end of the file. Like cc, it keeps the first line's "
         "indentation.",
    uses=["c"],
)
gg.add(
    title="Includes go first", par=5, ext="c", cursor=(7, 1),
    task="Move #include <string.h> from the bottom of the file to just below #include <stdio.h>.",
    start=text("""
        #include <stdio.h>

        int main(void) {
            printf("%zu\\n", strlen("vim"));
            return 0;
        }
        #include <string.h>
    """),
    target=text("""
        #include <stdio.h>
        #include <string.h>

        int main(void) {
            printf("%zu\\n", strlen("vim"));
            return 0;
        }
    """),
    hint="dd cuts the line. gg goes to the first line, and p puts the cut line below it.",
    uses=["dd", "p"],
)

gg.add(
    title="Call it at the end", par=4, ext="py",
    task="main() is called before it's defined: move the first line to the end of the file.",
    start=text("""
        main()
        import sys


        def main():
            print(sys.argv)
    """),
    target=text("""
        import sys


        def main():
            print(sys.argv)
        main()
    """),
    hint="dd cuts the line. G jumps to the last line, however far down it is, and p puts the cut line "
         "below it.",
    uses=["dd", "p"],
)
gg.add(
    title="Dedent the paste", par=2, ext="py",
    task="This snippet was pasted one level too deep. Shift every line left by one level.",
    start=("    import json\n"
           "\n"
           "    def load(path):\n"
           "        with open(path) as f:\n"
           "            return json.load(f)"),
    target=text("""
        import json

        def load(path):
            with open(path) as f:
                return json.load(f)
    """),
    hint="< is an operator that shifts lines left, and G is a motion to the last line.",
    uses=["indent"],
)
gg.add(
    title="The box needs a bottom", par=4, ext="txt",
    task="The board is missing its bottom edge: put a copy of the top border below the last line.",
    start=text("""
        +----------+
        | backlog  |
        | doing    |
        | done     |
    """),
    target=text("""
        +----------+
        | backlog  |
        | doing    |
        | done     |
        +----------+
    """),
    hint="yy copies the border line you're on. G jumps to the last line, and p puts the copy below it.",
    uses=["y", "p"],
)
gg.add(
    title="One title line", par=3, ext="md", cursor=(8, 1),
    task="The title got split over two lines: join lines 1 and 2 into one. The cursor starts on the last "
         "line.",
    start=text("""
        # Getting started with
        the course

        Install Neovim first.

        Then clone the course and run check.py.

        Ask in the chat if you get stuck.
    """),
    target=text("""
        # Getting started with the course

        Install Neovim first.

        Then clone the course and run check.py.

        Ask in the chat if you get stuck.
    """),
    hint="gg jumps to the first line from anywhere. J joins the next line onto it, with a space.",
    uses=["join"],
)
gg.add(
    title="Copy the fixture", par=5, ext="js", cursor=(4, 1),
    task="Start a second test fixture: put a copy of the four lines that define user at the end of the "
         "file. The cursor starts on the }; that closes it.",
    start=text("""
        const user = {
          id: 1,
          name: "Ada",
        };

        test("greets the user", () => {
          expect(greet(user)).toBe("Hello, Ada");
        });
    """),
    target=text("""
        const user = {
          id: 1,
          name: "Ada",
        };

        test("greets the user", () => {
          expect(greet(user)).toBe("Hello, Ada");
        });
        const user = {
          id: 1,
          name: "Ada",
        };
    """),
    hint="gg is a motion too: ygg copies every line from the top down to this one. G and p put them at the "
         "end.",
    uses=["y", "p"],
)
gg.add(
    title="All or nothing", par=19, ext="sql", cursor=(4, 1), setup=["setlocal indentexpr="],
    task="Run the transfer as one transaction: add BEGIN; as a new first line and COMMIT; as a new last "
         "line. The cursor starts on line 4.",
    start=text("""
        UPDATE accounts SET balance = balance - 100 WHERE id = 1;
        UPDATE accounts SET balance = balance + 100 WHERE id = 2;

        INSERT INTO transfers (from_id, to_id, amount) VALUES (1, 2, 100);
        UPDATE stats SET transfers = transfers + 1;

        DELETE FROM pending WHERE id = 7;
    """),
    target=text("""
        BEGIN;
        UPDATE accounts SET balance = balance - 100 WHERE id = 1;
        UPDATE accounts SET balance = balance + 100 WHERE id = 2;

        INSERT INTO transfers (from_id, to_id, amount) VALUES (1, 2, 100);
        UPDATE stats SET transfers = transfers + 1;

        DELETE FROM pending WHERE id = 7;
        COMMIT;
    """),
    hint="gg then O opens a line above the first one. G then o opens one below the last.",
    uses=["o"],
)
gg.add(
    title="One more web server", par=9, ext="txt",
    task="Add web-03 at 10.0.0.13: a new last line just like web-02's, with both 2s turned into 3s.",
    start=text("""
        127.0.0.1    localhost
        10.0.0.11    web-01
        10.0.0.12    web-02
    """),
    target=text("""
        127.0.0.1    localhost
        10.0.0.11    web-01
        10.0.0.12    web-02
        10.0.0.13    web-03
    """),
    hint="G and yyp duplicate the last line. The copy's first 2 is the end of the address, one WORD, and "
         "the other is the last character of the line, where . can repeat the r.",
    uses=["y", "p", "bigword", "r", "line", "dot"],
)
gg.add(
    title="Wrap it in a function", par=16, ext="py",
    task="Turn the script into a function: add def main(): as a new first line and indent every line "
         "below it one level.",
    start=text("""
        args = sys.argv[1:]
        for arg in args:
            print(arg)
    """),
    target=text("""
        def main():
            args = sys.argv[1:]
            for arg in args:
                print(arg)
    """),
    hint="O opens a line above the first one. Then go down a line: >G shifts every line from there to the "
         "end of the file.",
    uses=["o", "indent"],
)
gg.add(
    title="Two missing semicolons", par=8, ext="c",
    task="gcc says: main.c:4: error: expected ';' and main.c:8: error: expected ';'. Fix both lines.",
    start=text("""
        #include <stdio.h>

        int main(void) {
            int n = 10
            for (int i = 0; i < n; i++) {
                printf("%d\\n", i);
            }
            printf("done\\n")
            return 0;
        }
    """),
    target=text("""
        #include <stdio.h>

        int main(void) {
            int n = 10;
            for (int i = 0; i < n; i++) {
                printf("%d\\n", i);
            }
            printf("done\\n");
            return 0;
        }
    """),
    hint="4G goes to line 4 and A; fixes it. 8G goes to the other line, and . repeats the A; there.",
    uses=["count", "insert", "dot"],
)
gg.add(
    title="Shebang first, exit last", par=10, ext="sh",
    task="The first and last lines are swapped: #!/bin/bash belongs at the top and exit 0 at the bottom.",
    start=text("""
        exit 0
        set -euo pipefail

        ./build.sh
        ./test.sh

        #!/bin/bash
    """),
    target=text("""
        #!/bin/bash
        set -euo pipefail

        ./build.sh
        ./test.sh

        exit 0
    """),
    hint="dd the exit line and put it below the last line with G and p. The shebang is now the line just "
         "above; cut it too and put it above the first line with gg and P.",
    uses=["dd", "p"],
)

# ---------- % ----------

percent = drills.command(
    "percent", "%", "jump to the matching bracket",
    """On a bracket, % jumps to its partner: ( and ), [ and ], { and }, across lines if needed, skipping
    any pairs nested in between. If the cursor isn't on a bracket, % first looks forward on the line for
    one and jumps to that one's partner, so from the start of a line % often lands on the end of its first
    call. It's inclusive: d%, c% and y% take both brackets and everything between. In C files it also pairs
    /* with */ and #if or #ifdef with #else and #endif. With a count, 50% means "halfway through the file"
    instead.""",
    examples=[("%", "to the partner bracket"), ("d%", "delete a bracketed group"), ("c%", "change it"),
              ("y%", "copy it"), ("%x", "delete the partner bracket"), ("%O", "open a line above the closing brace")],
)
percent.add(
    title="It can throw", par=21, ext="java", cursor=(4, 1),
    task="Declare that save() throws IOException: add throws IOException just before the { on line 1. The "
         "cursor starts on the closing }.",
    start=text("""
        void save(Path path) {
            Files.writeString(path, render());
            log("saved " + path);
        }
    """),
    target=text("""
        void save(Path path) throws IOException {
            Files.writeString(path, render());
            log("saved " + path);
        }
    """),
    hint="% jumps from the } to the { that opens the block, however long the method is. Then insert before it.",
    uses=["insert"],
)
percent.add(
    title="Strip the input", par=10, ext="py",
    task="Add .strip() right after the input(...) call.",
    start='name = input("Name: ") or "anon"',
    target='name = input("Name: ").strip() or "anon"',
    hint="The cursor isn't on a bracket, so % looks ahead on the line for the first one, the ( of input(, and "
         "jumps to its partner. Then append after it with a.",
    uses=["insert"],
)
percent.add(
    title="Skip the aside", par=4, ext="txt",
    task="Delete the part in parentheses and one of the spaces around it.",
    start="The build (which takes ten minutes) runs every night.",
    target="The build runs every night.",
    hint="% from the start of the line lands on the ). d% deletes back to the ( and both brackets go. Then "
         "one space is left over.",
    uses=["d", "x"],
)
percent.add(
    title="Nested pairs", par=8, ext="java",
    task="total already holds the sum. Replace (sum(a) + sum(b)), parentheses included, with total.",
    start="double avg = (sum(a) + sum(b)) / 2.0;",
    target="double avg = total / 2.0;",
    hint="% finds the first ( on the line and jumps to its partner, skipping the pairs inside. c% then changes "
         "back to the (, both ends included.",
    uses=["c"],
)
percent.add(
    title="Erase what you drew", par=5, ext="c",
    task="Give wipe the same arguments as draw, parentheses included: wipe(x, y, width, height);.",
    start=text("""
        draw(x, y, width, height);
        wipe;
    """),
    target=text("""
        draw(x, y, width, height);
        wipe(x, y, width, height);
    """),
    hint="% gets you to the ), and y% copies the whole group. The cursor ends on the (, right above the ; of "
         "line 2. P puts the copy before the cursor.",
    uses=["y", "p"],
)
percent.add(
    title="Return before the brace", par=11, ext="c", cursor=(1, 16),
    task="Add return 0; as the last line of main(). The cursor starts on the {.",
    start=text("""
        int main(void) {
            init();
            run();
        }

        static void init(void) {
        }
    """),
    target=text("""
        int main(void) {
            init();
            run();
            return 0;
        }

        static void init(void) {
        }
    """),
    hint="% jumps from the { to the } that closes main(). O opens a line above it, already indented.",
    uses=["o"],
)
percent.add(
    title="Drop the else branch", par=3, ext="java", cursor=(3, 1),
    task="The else branch is never needed: delete else and its block, leaving the } that closes the if. The "
         "cursor starts on that }.",
    start=text("""
        if (cached) {
            return cache.get(key);
        } else {
            return load(key);
        }
    """),
    target=text("""
        if (cached) {
            return cache.get(key);
        }
    """),
    hint="Step onto else first. From there % looks ahead for the { and jumps to its }, two lines down, so d% "
         "deletes the whole branch.",
    uses=["word", "d"],
)
percent.add(
    title="Label the endif", par=14, ext="c",
    task="Label the #endif: it should read #endif /* DEBUG */.",
    start=text("""
        #ifdef DEBUG
            log_state(state);
            dump(buf, len);
        #endif
            send(buf, len);
    """),
    target=text("""
        #ifdef DEBUG
            log_state(state);
            dump(buf, len);
        #endif /* DEBUG */
            send(buf, len);
    """),
    hint="In C files % also jumps between #if/#ifdef, #else and #endif. Then append at the end of the line.",
    uses=["insert"],
)
percent.add(
    title="Extra parentheses", par=5, ext="java",
    task="Remove the parentheses around width * height.",
    start="    return (width * height);",
    target="    return width * height;",
    hint="% from the indentation finds the ( and lands on the ). Delete it, then go back to the ( with F( and "
         "delete that too.",
    uses=["x", "f"],
)
percent.add(
    title="Negate the condition", par=9, ext="java",
    task="Negate the whole condition: the line should read if (!(user.isAdmin() && !locked)) {.",
    start="if (user.isAdmin() && !locked) {",
    target="if (!(user.isAdmin() && !locked)) {",
    hint="Insert !( after the first (. The ( you just typed now pairs with the old closing ), so % jumps "
         "there, and a adds the second ).",
    uses=["f", "insert"],
)

percent.add(
    title="Pass it on", par=10, ext="js", cursor=(4, 1),
    task="The handler should pass errors on: give it a third parameter, so line 1 reads "
         "app.get(\"/users\", (req, res, next) => {. The cursor starts on the closing }.",
    start=text("""
        app.get("/users", (req, res) => {
          const users = db.all();
          res.json(users);
        });
    """),
    target=text("""
        app.get("/users", (req, res, next) => {
          const users = db.all();
          res.json(users);
        });
    """),
    hint="% jumps from the } to the { that opens the function, at the end of line 1. From there F) finds "
         "the ) after res.",
    uses=["f", "insert"],
)
percent.add(
    title="Drop the comment", par=4, ext="c", cursor=(2, 1),
    task="Delete the two-line comment after int port = 8080;, so that line ends with the semicolon and the "
         "comment's second line is gone too. The cursor starts on line 2.",
    start=text("""
        int main(void) {
            int port = 8080; /* default port,
                                see config.h */
            start_server(port);
            return 0;
        }
    """),
    target=text("""
        int main(void) {
            int port = 8080;
            start_server(port);
            return 0;
        }
    """),
    hint="In C files % also pairs /* with */, across lines. Get onto the / of /* and delete to its partner.",
    uses=["f", "d"],
)
percent.add(
    title="Add a row", par=10, ext="py",
    task="Add a third row, [5, 6], to the matrix.",
    start="matrix = [[1, 2], [3, 4]]  # rows",
    target="matrix = [[1, 2], [3, 4], [5, 6]]  # rows",
    hint="% from the start of the line finds the first [, the outer one, and jumps to the ] that closes it, "
         "skipping the rows inside. Insert before it.",
    uses=["insert"],
)
percent.add(
    title="Empty the queue", par=5, ext="py",
    task="Start with an empty queue: line 1 should read QUEUE = [] and the three items should go.",
    start=text("""
        QUEUE = [
            "build",
            "test",
            "deploy",
        ]
        run(QUEUE)
    """),
    target=text("""
        QUEUE = []
        run(QUEUE)
    """),
    hint="% finds the [ at the end of line 1 and jumps to its ] three lines down. c% changes everything "
         "from there back to the [, both brackets included, so type them again.",
    uses=["c"],
)
percent.add(
    title="No default options", par=4, ext="js",
    task="Drop the default value: line 1 should read function connect(opts) {.",
    start=text("""
        function connect(opts = { retries: 3, timeout: 500 }) {
          return open(opts);
        }
    """),
    target=text("""
        function connect(opts) {
          return open(opts);
        }
    """),
    hint="From a character that isn't a bracket, % looks ahead for one and jumps to its partner, so d% "
         "from the space before = deletes everything up to the } of the object. t= stops on that space.",
    uses=["f", "d"],
)
percent.add(
    title="A shorter arrow", par=9, ext="ts",
    task="Use the short form of the arrow function: the line should read "
         "const doubled = items.map((x) => x * 2);.",
    start="const doubled = items.map((x) => { return x * 2; });",
    target="const doubled = items.map((x) => x * 2);",
    hint="Get onto the { of the body. c% changes the whole block, braces included, and you type the "
         "expression instead.",
    uses=["f", "c"],
)
percent.add(
    title="Show the condition", par=7, ext="java",
    task="Put the failed condition, (amount <= 0) with its parentheses, at the end of the message, so it "
         "reads \"rejected: amount must be positive (amount <= 0)\".",
    start=text("""
        if (amount <= 0) {
            throw new IllegalArgumentException("rejected: amount must be positive ");
        }
        charge(card, amount);
    """),
    target=text("""
        if (amount <= 0) {
            throw new IllegalArgumentException("rejected: amount must be positive (amount <= 0)");
        }
        charge(card, amount);
    """),
    hint="% from the start of line 1 lands on the ) of the condition, and y% copies the group back to its "
         "(. Go down, stop on the closing quote with t), and put the copy before it.",
    uses=["y", "t", "p"],
)
percent.add(
    title="Hard-code the average", par=8, ext="sql",
    task="Replace the whole subquery, parentheses included, with 100, so line 4 reads WHERE total > 100.",
    start=text("""
        -- big spenders
        SELECT name, email, country, total
        FROM orders
        WHERE total > (
            SELECT avg(total)
            FROM orders
            WHERE created_at > now() - interval '30 days'
        )
        ORDER BY total DESC;
    """),
    target=text("""
        -- big spenders
        SELECT name, email, country, total
        FROM orders
        WHERE total > 100
        ORDER BY total DESC;
    """),
    hint="Get onto the ( at the end of line 4. c% changes from there to its ), four lines down, skipping "
         "the pairs inside, and joins what's left.",
    uses=["gg", "line", "c"],
)
percent.add(
    title="Round the result", par=16, ext="py",
    task="Round the result before comparing: the line should read "
         "assert round(compute(load(path), opts), 2) == expected.",
    start="assert compute(load(path), opts) == expected",
    target="assert round(compute(load(path), opts), 2) == expected",
    hint="Type round( before compute. Then step onto compute: % jumps to the ) that closes its call, past "
         "the one that closes load(path), and that's where , 2) goes.",
    uses=["word", "insert"],
)
percent.add(
    title="Run it at least once", par=11, ext="c",
    task="Turn the loop into a do-while: line 1 should read do { and the closing } should read "
         "} while (running);.",
    start=text("""
        while (running) {
            poll_events();
            render();
        }
        shutdown();
    """),
    target=text("""
        do {
            poll_events();
            render();
        } while (running);
        shutdown();
    """),
    hint="c% from the w changes while (running) (the motion goes to the ) of the first pair on the line) "
         "and keeps the old text to put back later. % then jumps from the { to the }. Type the space and the "
         "semicolon after it, and put the condition before the semicolon.",
    uses=["c", "insert", "p"],
)

# ---------- { } ----------

paragraph = drills.command(
    "paragraph", "{  }", "back or forward to a blank line",
    """} jumps forward to the next empty line and { back to the previous one. In code, blank lines usually
    separate functions and blocks, so these hop from one to the next. A line with spaces on it doesn't
    count as empty. As nouns they're exclusive, but when you start at the beginning of a line (or on a
    blank line) they act on whole lines: d} from a blank line deletes it and the block after it, and >}
    from a block's first line indents the block. From the middle of a line, d} deletes to the end of the
    paragraph. At the end of the file there's no next blank line, so use dG there.""",
    examples=[("}", "next blank line"), ("{", "previous blank line"), ("d}", "delete a block (from the blank above it)"),
              ("y}", "copy a block"), (">}", "indent to the next blank line"), ("d2}", "delete two blocks")],
)
paragraph.add(
    title="One more import", par=13, ext="py",
    task="Add import json at the end of the import block.",
    start=text("""
        import os
        import re
        import sys
        import time

        def main():
            print(time.time())
    """),
    target=text("""
        import os
        import re
        import sys
        import time
        import json

        def main():
            print(time.time())
    """),
    hint="} jumps to the blank line after the imports. O opens a new line above it.",
    uses=["o"],
)
paragraph.add(
    title="Cache it", par=12, ext="py", cursor=(7, 5),
    task="Put the decorator @lru_cache on its own line just above def fib(n):. The cursor starts on the last "
         "line.",
    start=text("""
        from functools import lru_cache


        def fib(n):
            if n < 2:
                return n
            return fib(n - 1) + fib(n - 2)
    """),
    target=text("""
        from functools import lru_cache


        @lru_cache
        def fib(n):
            if n < 2:
                return n
            return fib(n - 1) + fib(n - 2)
    """),
    hint="{ jumps back to the blank line just above the function. o opens a line below it.",
    uses=["o"],
)
paragraph.add(
    title="Remove a function", par=3, ext="c",
    task="Delete the unused() function and one of the blank lines next to it.",
    start=text("""
        int add(int a, int b) {
            return a + b;
        }

        int unused(int x) {
            return x * 2;
        }

        int sub(int a, int b) {
            return a - b;
        }
    """),
    target=text("""
        int add(int a, int b) {
            return a + b;
        }

        int sub(int a, int b) {
            return a - b;
        }
    """),
    hint="} gets you to the blank line above unused(). From a blank line, d} deletes whole lines: the blank "
         "line and the block after it, up to the next blank line.",
    uses=["d"],
)
paragraph.add(
    title="Ship it again", par=4, ext="txt", cursor=(3, 1),
    task="Repeat the chorus (with a blank line before it) after the last verse. The cursor starts on the "
         "blank line above the chorus.",
    start=text("""
        We wrote the code at night,
        the tests were green and bright.

        Ship it, ship it,
        push it to main.

        The pager rang at three,
        the logs were blamed on me.
    """),
    target=text("""
        We wrote the code at night,
        the tests were green and bright.

        Ship it, ship it,
        push it to main.

        The pager rang at three,
        the logs were blamed on me.

        Ship it, ship it,
        push it to main.
    """),
    hint="From a blank line, y} copies that blank line and the block below it. G goes to the last line, and p "
         "puts the lines below it.",
    uses=["y", "gg", "p"],
)
paragraph.add(
    title="Constructor first", par=5, ext="java",
    task="Move length() (and the blank line above it) below the constructor, so Point(int x, int y) comes "
         "first.",
    start=text("""
        class Point {
            int x, y;

            double length() {
                return Math.sqrt(x * x + y * y);
            }

            Point(int x, int y) {
                this.x = x;
                this.y = y;
            }
        }
    """),
    target=text("""
        class Point {
            int x, y;

            Point(int x, int y) {
                this.x = x;
                this.y = y;
            }

            double length() {
                return Math.sqrt(x * x + y * y);
            }
        }
    """),
    hint="} lands on the blank line above length(), and d} cuts it with the method. Then go to the class's "
         "closing } on the last line and put the lines above it with P.",
    uses=["d", "gg", "p"],
)
paragraph.add(
    title="Indent the block", par=2, ext="py", cursor=(2, 1),
    task="The three lines after the if should only run when verbose is set. Indent them one level.",
    start=text("""
        if args.verbose:
        print("Loading", path)
        data = load(path)
        print("Loaded", len(data), "rows")

        save(data)
    """),
    target=text("""
        if args.verbose:
            print("Loading", path)
            data = load(path)
            print("Loaded", len(data), "rows")

        save(data)
    """),
    hint="> shifts lines right, and } is a motion to the blank line. From the start of a line, >} shifts "
         "every line of the block.",
    uses=["indent"],
)
paragraph.add(
    title="Write the section", par=19, ext="md", cursor=(3, 1),
    task="Replace the three-line TODO note with a single line: Run make install.",
    start=text("""
        ## Install

        TODO: write this section.
        Mention brew and apt.
        And the Windows zip.

        ## Usage
    """),
    target=text("""
        ## Install

        Run make install.

        ## Usage
    """),
    hint="c} from the start of a line changes whole lines up to the blank line, and leaves you typing on one "
         "line.",
    uses=["c"],
)
paragraph.add(
    title="Cut the rest", par=2, ext="txt", cursor=(1, 24),
    task="Keep only the first sentence of the paragraph: delete from I fixed to the end of the paragraph "
         "(not the blank line or the signature). The cursor starts on the I.",
    start=text("""
        Thanks for the review. I fixed the typo and
        renamed the helper. Let me know if anything
        else needs work.

        -- Rick
    """),
    target=text("""
        Thanks for the review.

        -- Rick
    """),
    hint="From the middle of a line, d} deletes up to the end of the paragraph and leaves the blank line "
         "alone.",
    uses=["d"],
)
paragraph.add(
    title="Two old functions", par=4, ext="py",
    task="Delete old_a() and old_b(), with one blank line each, so keep() and also_keep() are left with one "
         "blank line between them.",
    start=text("""
        def keep():
            return 1

        def old_a():
            return 2

        def old_b():
            return 3

        def also_keep():
            return 4
    """),
    target=text("""
        def keep():
            return 1

        def also_keep():
            return 4
    """),
    hint="Go to the blank line under keep() with }. Counts work with }: d2} deletes up to the second blank "
         "line from here.",
    uses=["d", "count"],
)
paragraph.add(
    title="Helper first", par=5, ext="c", cursor=(9, 5),
    task="Move greet() (with a blank line) above main(), so the file reads: include, blank, greet(), blank, "
         "main(). The cursor starts inside greet().",
    start=text("""
        #include <stdio.h>

        int main(void) {
            greet("Rick");
            return 0;
        }

        void greet(const char *name) {
            printf("Hello, %s\\n", name);
        }
    """),
    target=text("""
        #include <stdio.h>

        void greet(const char *name) {
            printf("Hello, %s\\n", name);
        }

        int main(void) {
            greet("Rick");
            return 0;
        }
    """),
    hint="{ jumps back to the blank line above greet(). greet() is the last block, so cut it to the end of "
         "the file with dG. Another { reaches the blank line under the include, and P puts the lines above it.",
    uses=["gg", "d", "p"],
)

paragraph.add(
    title="Only two hosts", par=2, ext="yaml", cursor=(4, 1),
    task="Retire the old servers: delete the three -old hosts, from the cursor's line to the end of the list. "
         "Keep the blank line and port.",
    start=text("""
        hosts:
          - web-01
          - web-02
          - web-03-old
          - web-04-old
          - web-05-old

        port: 8080
    """),
    target=text("""
        hosts:
          - web-01
          - web-02

        port: 8080
    """),
    hint="From the start of a line, d} deletes whole lines up to the blank line, which stays.",
    uses=["d"],
)
paragraph.add(
    title="Dedent the block", par=2, ext="py", cursor=(3, 1),
    task="The if around these three lines was removed: shift lines 3 to 5 left by one level. The cursor "
         "starts on line 3.",
    start=text("""
        def main():
            config = load()
                print("loaded", config)
                validate(config)
                apply(config)

            run(config)
    """),
    target=text("""
        def main():
            config = load()
            print("loaded", config)
            validate(config)
            apply(config)

            run(config)
    """),
    hint="< is an operator that shifts lines left, and } is a motion to the next blank line.",
    uses=["indent"],
)
paragraph.add(
    title="Not this function", par=3, ext="py", cursor=(6, 5),
    task="Delete the whole legacy_total() function and one of the blank lines next to it. The cursor starts "
         "inside it.",
    start=text("""
        def total(items):
            return sum(i.price for i in items)

        def legacy_total(items):
            result = 0
            for i in items:
                result += i.price
            return result

        def count(items):
            return len(items)
    """),
    target=text("""
        def total(items):
            return sum(i.price for i in items)

        def count(items):
            return len(items)
    """),
    hint="{ jumps back to the blank line above the function. From a blank line, d} deletes it and the "
         "block below.",
    uses=["d"],
)
paragraph.add(
    title="From below", par=2, ext="sql", cursor=(5, 1),
    task="Keep the tables: delete the two DROP TABLE lines and the blank line above them. The cursor starts "
         "on the blank line below them.",
    start=text("""
        CREATE TABLE users (id int);

        DROP TABLE users;
        DROP TABLE sessions;

        CREATE TABLE logs (id int);
    """),
    target=text("""
        CREATE TABLE users (id int);

        CREATE TABLE logs (id int);
    """),
    hint="{ works with d too. From a blank line, d{ deletes back up to the previous blank line, that one "
         "included, and leaves the line you're on.",
    uses=["d"],
)
paragraph.add(
    title="Sorted imports", par=4, ext="py", cursor=(5, 1),
    task="Keep the imports sorted: move import argparse (the cursor's line) to the top of the import block.",
    start=text("""
        \"\"\"Sync users from the API.\"\"\"

        import json
        import sys
        import argparse

        API = "https://api.example.com"
    """),
    target=text("""
        \"\"\"Sync users from the API.\"\"\"

        import argparse
        import json
        import sys

        API = "https://api.example.com"
    """),
    hint="dd cuts the line. { jumps back to the blank line above the block, and p puts the line just below "
         "it.",
    uses=["dd", "p"],
)
paragraph.add(
    title="Into the with block", par=4, ext="py",
    task="Everything up to print(header) belongs inside the with block: indent lines 2 to 6 one level.",
    start=text("""
        with open(path) as f:
        data = f.read()
        rows = data.splitlines()

        header = rows[0]
        body = rows[1:]

        print(header)
    """),
    target=text("""
        with open(path) as f:
            data = f.read()
            rows = data.splitlines()

            header = rows[0]
            body = rows[1:]

        print(header)
    """),
    hint="Go down to line 2. } takes a count: >2} shifts every line up to the second blank line from there. "
         "Blank lines don't get indented.",
    uses=["indent", "count"],
)
paragraph.add(
    title="Fence the code", par=11, ext="md", cursor=(5, 1),
    task="Put the commands in a code block: add a line with ``` above them and another below them. The "
         "cursor starts on the third command.",
    start=text("""
        Before you push, run:

        python3 check.py --solution
        python3 check.py drill
        python3 progress.py
        git status
        git push

        Then open a pull request.
    """),
    target=text("""
        Before you push, run:

        ```
        python3 check.py --solution
        python3 check.py drill
        python3 progress.py
        git status
        git push
        ```

        Then open a pull request.
    """),
    hint="{ jumps to the blank line above the commands, where o opens a line for the first fence. } then "
         "jumps to the blank line below them, and O opens a line above it.",
    uses=["o"],
)
paragraph.add(
    title="Two debug blocks", par=5, ext="py",
    task="Remove both groups of debug prints, each with the blank line above it.",
    start=text("""
        def run(job):
            prepare(job)

            print("DEBUG", job)
            print("DEBUG", job.args)

            execute(job)

            print("DEBUG", job.result)

            return job.result
    """),
    target=text("""
        def run(job):
            prepare(job)

            execute(job)

            return job.result
    """),
    hint="} gets to the blank line above the first group, and d} deletes it with the group. That leaves "
         "you on a blank line; } jumps to the next one, and . repeats the delete.",
    uses=["d", "dot"],
)
paragraph.add(
    title="Install comes first", par=6, ext="md",
    task="Readers need to install before they can use it: move the Usage section (its heading, its text and "
         "the blank line above it) to the end of the file.",
    start=text("""
        # acme-cli

        ## Usage

        Run acme sync to pull the latest data.

        ## Install

        Run pip install acme-cli.
    """),
    target=text("""
        # acme-cli

        ## Install

        Run pip install acme-cli.

        ## Usage

        Run acme sync to pull the latest data.
    """),
    hint="The heading and its text are two paragraphs. From the blank line above ## Usage, d2} cuts both, "
         "with the blank lines in front of them. Then G and p.",
    uses=["d", "count", "gg", "p"],
)
paragraph.add(
    title="A replica section", par=16, ext="ini",
    task="Add a [replica] section with the same settings as [database] at the end of the file, with a "
         "blank line before it.",
    start=text("""
        [server]
        host = 0.0.0.0
        port = 8080

        [database]
        host = db.internal
        port = 5432

        [logging]
        level = info
    """),
    target=text("""
        [server]
        host = 0.0.0.0
        port = 8080

        [database]
        host = db.internal
        port = 5432

        [logging]
        level = info

        [replica]
        host = db.internal
        port = 5432
    """),
    hint="} goes to the blank line above [database], and y} copies it with the section. G and p put the "
         "copy at the end, leaving you on its blank line. Then rename database.",
    uses=["y", "gg", "p", "c"],
)

# ---------- / ? n N ----------

search = drills.command(
    "search", "/  ?  n  N", "search forward or backward",
    """/text and Enter jumps forward to the next match of text, anywhere in the file, and ?text and Enter
    jumps backward. n repeats the search in the same direction, N in the opposite one (so after ?, n keeps
    going up), and both wrap around the ends of the file. With smartcase on, an all-lowercase pattern
    ignores case and any capital makes it exact. Some characters are special: . matches anything, so
    search for \\. to find a dot. As nouns, searches are exclusive and work across lines: d/map<CR>
    deletes up to map, and dn up to the next match.""",
    examples=[("/port<CR>", "next port"), ("?def<CR>", "previous def"), ("n", "next match"),
              ("N", "match in the other direction"), ("d/x<CR>", "delete up to the next x, lines away"),
              ("/\\.<CR>", "next literal dot")],
)
search.add(
    title="Turn off debug", par=11, ext="py",
    task="Set DEBUG to False.",
    start=text("""
        # settings.py
        import os

        BASE_DIR = os.path.dirname(__file__)
        SECRET_KEY = os.environ["SECRET_KEY"]
        DEBUG = True
        ALLOWED_HOSTS = ["localhost"]
    """),
    target=text("""
        # settings.py
        import os

        BASE_DIR = os.path.dirname(__file__)
        SECRET_KEY = os.environ["SECRET_KEY"]
        DEBUG = False
        ALLOWED_HOSTS = ["localhost"]
    """),
    hint="Search for the word you want to change: /Tr and Enter is enough (a capital makes the search "
         "match case exactly). Then cw.",
    uses=["c"],
)
search.add(
    title="A spelling slip", par=5, ext="txt", cursor=(3, 42),
    task='Fix the spelling of "untill" on line 1. The cursor starts at the end of the message.',
    start=text("""
        Hi all, the release is delayed untill Monday, sadly,
        because the build server is down and the
        tests keep failing. Sorry for the trouble.
    """),
    target=text("""
        Hi all, the release is delayed until Monday, sadly,
        because the build server is down and the
        tests keep failing. Sorry for the trouble.
    """),
    hint="? searches backward. The doubled l is rare, so ?ll and Enter lands on it, and x removes one.",
    uses=["x"],
)
search.add(
    title="The second N/A", par=20, ext="csv",
    task="Bob's email is bob@example.com: replace the second N/A in the file (on bob's line) with it.",
    start=text("""
        name,phone,email
        alice,N/A,alice@example.com
        bob,555-0101,N/A
        carol,N/A,carol@example.com
    """),
    target=text("""
        name,phone,email
        alice,N/A,alice@example.com
        bob,555-0101,bob@example.com
        carol,N/A,carol@example.com
    """),
    hint="/N and Enter finds the first N/A (the capital makes it skip name). n goes on to the next match, "
         "and C changes to the end of the line.",
    uses=["c"],
)
search.add(
    title="Done with that one", par=3, ext="py", cursor=(4, 9),
    setup=["let @/ = 'TODO'"],
    task="You've been searching for TODO (it's still your last search). The first TODO is done: delete "
         "\"TODO: \" from line 2, so it's a plain comment. The cursor starts on line 4.",
    start=text("""
        def parse(path):
            # TODO: handle missing files
            with open(path) as f:
                rows = f.readlines()
            # TODO: skip the header row
            return [r.split(",") for r in rows]
    """),
    target=text("""
        def parse(path):
            # handle missing files
            with open(path) as f:
                rows = f.readlines()
            # TODO: skip the header row
            return [r.split(",") for r in rows]
    """),
    hint="The last search was forward, so n would go down to line 5. N goes the other way, up to line 2. "
         "TODO: is one WORD, so dW deletes it and its space.",
    uses=["d", "bigword"],
)
search.add(
    title="Fewer columns", par=4, ext="sql", cursor=(1, 12),
    task="Select only id and created_at: delete from name up to created_at, across the lines. The cursor "
         "starts on the n of name.",
    start=text("""
        SELECT id, name, email,
               phone, address,
               created_at
        FROM users
    """),
    target=text("""
        SELECT id, created_at
        FROM users
    """),
    hint="d takes a search as its motion: d/c and Enter deletes up to the next c, which is the start of "
         "created_at, joining the lines.",
    uses=["d"],
)
search.add(
    title="Say it shorter", par=20, ext="txt", cursor=(1, 12),
    task="Make it read: The parser streams the file, which is slow. The cursor starts on reads.",
    start=text("""
        The parser reads the whole file into
        memory before it starts, which is slow.
    """),
    target="The parser streams the file, which is slow.",
    hint="c works with a search too. c/, and Enter changes everything up to the comma on the next line.",
    uses=["c"],
)
search.add(
    title="A literal dot", par=5, ext="txt", cursor=(1, 28),
    task="Shorten it to: Version 2.0 ships next week. Thanks to everyone! The cursor starts on the comma "
         "after week.",
    start=text("""
        Version 2.0 ships next week, along with
        the new docs, the installer, and a few
        other small things. Thanks to everyone!
    """),
    target="Version 2.0 ships next week. Thanks to everyone!",
    hint="Delete up to the period after things. In a pattern . means any character, so search for \\. "
         "instead: d/\\. and Enter.",
    uses=["d"],
)
search.add(
    title="Drop the u", par=9, ext="txt",
    task="Use American spelling: change colour to color everywhere (three times).",
    start=text("""
        Set the colour of the border.
        The default colour is grey.
        Background colours are not supported.
    """),
    target=text("""
        Set the color of the border.
        The default color is grey.
        Background colors are not supported.
    """),
    hint="Search for ur (u alone would also find default), delete the u with x, then n and . for each "
         "remaining match.",
    uses=["x", "dot"],
)
search.add(
    title="Skip one", par=13, ext="py",
    task="Change 80 to 100 on lines 1 and 4. Leave OLD_WIDTH alone.",
    start=text("""
        WIDTH = 80
        # keep the old width for the legacy report
        OLD_WIDTH = 80
        MARGIN = 80 // 10
    """),
    target=text("""
        WIDTH = 100
        # keep the old width for the legacy report
        OLD_WIDTH = 80
        MARGIN = 100 // 10
    """),
    hint="/80 and Enter, then cw100. n moves to the next match without changing it, so nn skips "
         "OLD_WIDTH, and . repeats the change.",
    uses=["c", "dot"],
)
search.add(
    title="Fewer arguments", par=5, ext="py", cursor=(2, 1),
    task="Use the default timeout and source address: line 2 should end with port)) and lines 3 and 4 "
         "should go.",
    start=text("""
        def connect(host, port):
            sock = socket.create_connection((host, port),
                                            timeout=10,
                                            source_address=None)
            return sock
    """),
    target=text("""
        def connect(host, port):
            sock = socket.create_connection((host, port))
            return sock
    """),
    hint="$ takes you to the comma at the end of line 2. From there, d/) and Enter deletes everything up "
         "to the ) after None, joining the lines.",
    uses=["line", "d"],
)

search.add(
    title="Scale it up", par=5, ext="yaml",
    task="Scale the deployment up: set replicas to 4.",
    start=text("""
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: api
          namespace: shop
          labels:
            app: api
            team: payments
          annotations:
            owner: rick
        spec:
          replicas: 2
          selector:
            matchLabels:
              app: api
    """),
    target=text("""
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: api
          namespace: shop
          labels:
            app: api
            team: payments
          annotations:
            owner: rick
        spec:
          replicas: 4
          selector:
            matchLabels:
              app: api
    """),
    hint="Search for the thing you want to change. There's only one 2 in the file, so /2 and Enter lands "
         "right on it.",
    uses=["r"],
)
search.add(
    title="A shorter timeout", par=6, ext="py", cursor=(10, 1),
    task="Make the default timeout 10 seconds instead of 30. The cursor starts on the last line.",
    start=text("""
        def connect(host, port=5432, timeout=30, retries=3):
            sock = open_socket(host, port)
            sock.settimeout(timeout)
            for attempt in range(retries):
                if sock.ping():
                    return sock
            raise ConnectionError(host)


        conn = connect("db.internal")
    """),
    target=text("""
        def connect(host, port=5432, timeout=10, retries=3):
            sock = open_socket(host, port)
            sock.settimeout(timeout)
            for attempt in range(retries):
                if sock.ping():
                    return sock
            raise ConnectionError(host)


        conn = connect("db.internal")
    """),
    hint="? searches backward, up the file. Only one place has a 3 followed by a 0, and only the 3 has to "
         "change.",
    uses=["r"],
)
search.add(
    title="Tick the last box", par=6, ext="md",
    task="Publishing is done: tick the last unchecked box (publish to PyPI) by putting an x in it.",
    start=text("""
        # Release checklist

        - [x] bump the version
        - [x] update the changelog
        - [ ] run the full test suite
        - [x] tag the commit
        - [ ] build the wheels
        - [x] upload to the test index
        - [x] smoke-test the install
        - [x] write the announcement
        - [ ] publish to PyPI
        - [x] close the milestone
        - [x] thank the contributors
        - [x] start the next milestone
    """),
    target=text("""
        # Release checklist

        - [x] bump the version
        - [x] update the changelog
        - [ ] run the full test suite
        - [x] tag the commit
        - [ ] build the wheels
        - [x] upload to the test index
        - [x] smoke-test the install
        - [x] write the announcement
        - [x] publish to PyPI
        - [x] close the milestone
        - [x] thank the contributors
        - [x] start the next milestone
    """),
    hint="An open box has a space before its ]. Searches wrap around the ends of the file: from line 1, ? "
         "goes backward, around the top, and meets the last match first.",
    uses=["r"],
)
search.add(
    title="The second column", par=8, ext="py",
    task="Use the second column: change both row[0] to row[1]. Leave the 100 alone.",
    start=text("""
        for row in rows[100:]:
            name = row[0]
            if row[0] in seen:
                continue
            emit(name)
    """),
    target=text("""
        for row in rows[100:]:
            name = row[1]
            if row[1] in seen:
                continue
            emit(name)
    """),
    hint="Search for 0] (a ] on its own is just a ], but [0] would mean \"any of the characters 0\"). Then "
         "r, and n and . for the other one.",
    uses=["r", "dot"],
)
search.add(
    title="Two typos, going up", par=9, ext="md", cursor=(7, 1),
    task="Fix both misspellings of accommodate (accomodate, with one m). The cursor starts on the last "
         "line.",
    start=text("""
        # Venue

        The hall can accomodate 120 people.

        The hotel next door can accomodate the speakers.

        Lunch is served at noon.
    """),
    target=text("""
        # Venue

        The hall can accommodate 120 people.

        The hotel next door can accommodate the speakers.

        Lunch is served at noon.
    """),
    hint="?mo and Enter finds the closest accomodate above you. Typing one more m there is a change . can "
         "repeat, and after ?, n keeps going up.",
    uses=["insert", "dot"],
)
search.add(
    title="Not the cache", par=8, ext="js", cursor=(6, 1),
    task="Lower the two request timeouts on lines 4 and 7 to 3000, but leave API_TIMEOUT and CACHE_TTL at "
         "5000. The cursor starts on line 6.",
    start=text("""
        const API_TIMEOUT = 5000;

        function load(url) {
          return fetch(url, { timeout: 5000 });
        }

        retry(job, { tries: 3, timeout: 5000 });

        const CACHE_TTL = 5000;
    """),
    target=text("""
        const API_TIMEOUT = 5000;

        function load(url) {
          return fetch(url, { timeout: 3000 });
        }

        retry(job, { tries: 3, timeout: 3000 });

        const CACHE_TTL = 5000;
    """),
    hint="/50 and Enter finds line 7. n would go on to CACHE_TTL, but N goes back the other way, to line 4, "
         "and . repeats the r there.",
    uses=["r", "dot"],
)
search.add(
    title="The first and the last", par=13, ext="py",
    task="Log less: change the first DEBUG and the last one to INFO, but keep the middle one (the parser "
         "module stays at DEBUG).",
    start=text("""
        logging.basicConfig(level="DEBUG")
        log = logging.getLogger("app")

        parser_log = logging.getLogger("app.parser")
        parser_log.setLevel("DEBUG")

        handler = logging.FileHandler("app.log")
        handler.setLevel("DEBUG")
        log.addHandler(handler)
    """),
    target=text("""
        logging.basicConfig(level="INFO")
        log = logging.getLogger("app")

        parser_log = logging.getLogger("app.parser")
        parser_log.setLevel("DEBUG")

        handler = logging.FileHandler("app.log")
        handler.setLevel("INFO")
        log.addHandler(handler)
    """),
    hint="/DE and Enter lands on the first DEBUG; change it with cw. N searches the other way, so from the "
         "first match it wraps around the top of the file to the last one, where . repeats the change.",
    uses=["c", "dot"],
)
search.add(
    title="Logs, not catalogs", par=15, ext="sh",
    task="The logs are plain text now: change each .log to .txt (three of them). Don't touch catalog.",
    start=text("""
        ./export.sh --catalog ./data/catalog.db > export.log
        gzip -9 ./tmp/worker.log
        tail -n 50 /var/log/app/app.log
    """),
    target=text("""
        ./export.sh --catalog ./data/catalog.db > export.txt
        gzip -9 ./tmp/worker.txt
        tail -n 50 /var/log/app/app.txt
    """),
    hint="A plain . in a pattern matches any character, so search for \\.l to find a real dot followed by "
         "an l. R types over .log, and n and . repeat it.",
    uses=["replace-mode", "dot"],
)
search.add(
    title="No more levels", par=12, ext="py",
    task="log() picks its level by itself now: remove , DEBUG from the three log calls. Leave the comma in "
         "\"dry run, nothing to do\" alone.",
    start=text("""
        log("starting", DEBUG)
        config = load()
        log("loaded %s" % config.name, DEBUG)
        if config.dry_run:
            log("dry run, nothing to do", DEBUG)
            sys.exit(0)
        run(config)
    """),
    target=text("""
        log("starting")
        config = load()
        log("loaded %s" % config.name)
        if config.dry_run:
            log("dry run, nothing to do")
            sys.exit(0)
        run(config)
    """),
    hint="Search for a comma, a space and a capital D: the capital makes the search match case exactly, so "
         "\", nothing\" doesn't count. dt) deletes up to the ), and n and . do the rest.",
    uses=["d", "t", "dot"],
)
search.add(
    title="Only the constant", par=18, ext="py",
    task="Rename the constant API to BASE_URL everywhere (three places), but leave the variable api and the "
         "api in the URL alone.",
    start=text("""
        API = "https://api.example.com"
        api = connect(API)
        log("api ready", API)
    """),
    target=text("""
        BASE_URL = "https://api.example.com"
        api = connect(BASE_URL)
        log("api ready", BASE_URL)
    """),
    hint="* won't do: it ignores smartcase, so it also stops on api. Change the first one with cw, then "
         "search for AP: with a capital in the pattern it matches case exactly. . and n. do the other two.",
    uses=["c", "dot"],
)

# ---------- * # ----------

star = drills.command(
    "star", "*  #", "search for the word under the cursor",
    """* searches forward for the word under the cursor, and # searches backward. They match whole words
    only (the pattern is \\<word\\>), so * on tmp skips tmpdir. Afterwards n and N repeat the search as
    usual, wrapping around the file. One surprise: they use ignorecase but not smartcase, so * on vim
    also stops at Vim and VIM. Search first, then change: * then cw then n and . renames a variable one
    use at a time. (g* and g# also match inside longer words.)""",
    examples=[("*", "next use of this word"), ("#", "previous use"), ("*cwnew<Esc>", "jump and rename one"),
              ("n.", "next one, same change"), ("d*", "delete up to the next use")],
)
star.add(
    title="Remove the call", par=3, ext="c", cursor=(1, 6),
    task="Delete the line that calls debug_dump() inside main(). The cursor starts on the function's name.",
    start=text("""
        void debug_dump(void) {
            printf("state: %d\\n", state);
        }

        int main(void) {
            init();
            debug_dump();
            run();
        }
    """),
    target=text("""
        void debug_dump(void) {
            printf("state: %d\\n", state);
        }

        int main(void) {
            init();
            run();
        }
    """),
    hint="* jumps to the next place the word under the cursor appears. Then delete the line.",
    uses=["dd"],
)
star.add(
    title="Not the logger", par=9, ext="py",
    task="Pass config to make_logger instead of log: change the argument on line 2.",
    start=text("""
        log = open_log()
        logger = make_logger(log)
        logger.info("started")
    """),
    target=text("""
        log = open_log()
        logger = make_logger(config)
        logger.info("started")
    """),
    hint="* searches for log as a whole word, so it skips logger and make_logger and lands on the argument. "
         "Then cw.",
    uses=["c"],
)
star.add(
    title="Inline the helper", par=10, ext="c", cursor=(6, 20),
    task="Mark clamp() as inline: its definition should start with static inline int. The cursor starts on "
         "the call in main().",
    start=text("""
        static int clamp(int x, int lo, int hi) {
            return x < lo ? lo : x > hi ? hi : x;
        }

        int main(void) {
            printf("%d\\n", clamp(42, 0, 10));
        }
    """),
    target=text("""
        static inline int clamp(int x, int lo, int hi) {
            return x < lo ? lo : x > hi ? hi : x;
        }

        int main(void) {
            printf("%d\\n", clamp(42, 0, 10));
        }
    """),
    hint="# searches backward for the word under the cursor, straight to the definition. b steps back to int, "
         "and i inserts before it.",
    uses=["word", "insert"],
)
star.add(
    title="Around to the top", par=4, ext="py", cursor=(6, 29),
    task="Allow 5 retries instead of 3. The cursor starts on the last RETRIES.",
    start=text("""
        RETRIES = 3

        def fetch(url):
            for attempt in range(RETRIES):
                if get(url):
                    print("tries:", RETRIES)
    """),
    target=text("""
        RETRIES = 5

        def fetch(url):
            for attempt in range(RETRIES):
                if get(url):
                    print("tries:", RETRIES)
    """),
    hint="This is the last RETRIES in the file, so * wraps around to the first one, on line 1. Then $ and r.",
    uses=["line", "r"],
)
star.add(
    title="A clearer name", par=13, ext="c", cursor=(1, 5),
    task="Rename the variable n to count everywhere (three places). The cursor starts on the first n.",
    start=text("""
        int n = read_count();
        int *buf = malloc(n * sizeof(int));
        for (int i = 0; i < n; i++)
    """),
    target=text("""
        int count = read_count();
        int *buf = malloc(count * sizeof(int));
        for (int i = 0; i < count; i++)
    """),
    hint="* jumps to the next n as a whole word, skipping the n's inside int and read_count. Change it with "
         "cw, then n. for each remaining one. The search wraps back to line 1.",
    uses=["c", "dot", "search"],
)
star.add(
    title="Rename going up", par=12, ext="java", cursor=(2, 22),
    task="Rename ratio to aspect in both places. The cursor starts on the ratio in line 2.",
    start=text("""
        double ratio = width / height;
        label.setText(format(ratio));
    """),
    target=text("""
        double aspect = width / height;
        label.setText(format(aspect));
    """),
    hint="Search before you change: once you've changed it, the word under the cursor isn't ratio any more. "
         "# goes back to line 1. After #, n keeps going backward and wraps around to line 2.",
    uses=["c", "dot", "search"],
)
star.add(
    title="Any case", par=14, ext="txt", cursor=(1, 15),
    task="Replace every vim, capitalized or not, with Neovim (three places). The cursor starts on the first "
         "vim.",
    start=text("""
        I switched to vim last year.
        Vim is fast, and vim motions are everywhere.
    """),
    target=text("""
        I switched to Neovim last year.
        Neovim is fast, and Neovim motions are everywhere.
    """),
    hint="* ignores smartcase: on vim it also finds Vim. Search, change with cw, then n. twice.",
    uses=["c", "dot", "search"],
)
star.add(
    title="Up to the retry", par=2, ext="py",
    task="The first attempt is no longer needed: delete lines 1 to 3, so the file starts with the second "
         "connect().",
    start=text("""
        connect()
        send(header)
        send(body)
        connect()
        send(header)
        send(body)
        close()
    """),
    target=text("""
        connect()
        send(header)
        send(body)
        close()
    """),
    hint="* is a motion like any search, so d* deletes up to the next connect. Starting in column 1 and "
         "ending in column 1, it deletes whole lines.",
    uses=["d"],
)
star.add(
    title="Not in the message", par=13, ext="py",
    task="Rename the variable data to rows, but leave the word data in the printed message alone.",
    start=text("""
        data = load()
        clean(data)
        print("data saved")
        save(data)
    """),
    target=text("""
        rows = load()
        clean(rows)
        print("data saved")
        save(rows)
    """),
    hint="* finds data inside the string too (it's a whole word there). Use n without . to skip that one.",
    uses=["c", "search", "dot"],
)
star.add(
    title="Rename the field", par=12, ext="java", cursor=(1, 13),
    task="Rename the field count to size everywhere it's used, but don't touch the method name getCount.",
    start=text("""
        private int count;
        int getCount() { return count; }
        void reset() { count = 0; }
    """),
    target=text("""
        private int size;
        int getCount() { return size; }
        void reset() { size = 0; }
    """),
    hint="* matches whole words only, so the Count inside getCount isn't a match. Then cw, and n. for the rest.",
    uses=["c", "search", "dot"],
)

star.add(
    title="A long total", par=8, ext="java", cursor=(7, 27),
    task="The total can overflow an int: change total()'s return type to long. The cursor starts on the "
         "call in summary().",
    start=text("""
        public class Cart {
            private int total() {
                return items.stream().mapToInt(Item::price).sum();
            }

            public String summary() {
                return "Sum: " + total();
            }
        }
    """),
    target=text("""
        public class Cart {
            private long total() {
                return items.stream().mapToInt(Item::price).sum();
            }

            public String summary() {
                return "Sum: " + total();
            }
        }
    """),
    hint="# searches backward for the word under the cursor and lands on the definition. The type is the "
         "word before it.",
    uses=["word", "c"],
)
star.add(
    title="One more try", par=7, ext="py", cursor=(2, 1),
    task="Try once more than the retry count: make it range(retries + 1). The cursor starts at the start of "
         "line 2, in the indentation.",
    start=text("""
        def fetch(url):
            retries = 3
            delay = 1.0
            for attempt in range(retries):
                if try_get(url):
                    return True
                sleep(delay)
            return False
    """),
    target=text("""
        def fetch(url):
            retries = 3
            delay = 1.0
            for attempt in range(retries + 1):
                if try_get(url):
                    return True
                sleep(delay)
            return False
    """),
    hint="When the cursor isn't on a word, * uses the first word after it on the line, here retries. So * "
         "takes you straight to range(retries. Then append after the word's end.",
    uses=["word", "insert"],
)
star.add(
    title="Add a field", par=8, ext="c", cursor=(5, 1),
    task="Points are 3D now: add the field int z; on its own line, after int x, y;. The cursor starts on "
         "the Point at the start of line 5.",
    start=text("""
        typedef struct {
            int x, y;
        } Point;

        Point add(Point a, Point b) {
            return (Point){a.x + b.x, a.y + b.y};
        }
    """),
    target=text("""
        typedef struct {
            int x, y;
            int z;
        } Point;

        Point add(Point a, Point b) {
            return (Point){a.x + b.x, a.y + b.y};
        }
    """),
    hint="# jumps back to the previous Point, the one that closes the struct. O opens a line above it, "
         "indented for you.",
    uses=["o"],
)
star.add(
    title="Numbers are words too", par=10, ext="yaml", cursor=(4, 10),
    task="The app listens on 3000 inside the container now: change the container port (after the colon) "
         "and PORT to 3000. The host port stays 8080. The cursor starts on the first 8080.",
    start=text("""
        services:
          web:
            ports:
              - "8080:8080"
            environment:
              PORT: 8080
    """),
    target=text("""
        services:
          web:
            ports:
              - "8080:3000"
            environment:
              PORT: 3000
    """),
    hint="A number is a word, so * finds the next 8080 as a whole word: the one after the colon. Change "
         "it, then n and . for PORT.",
    uses=["c", "search", "dot"],
)
star.add(
    title="The other way round", par=4, ext="py",
    task="can_add() has its comparison backwards: make it len(cart) < MAX_ITEMS.",
    start=text("""
        MAX_ITEMS = 10

        def add(cart, item):
            if len(cart) >= MAX_ITEMS:
                raise ValueError("cart is full")
            cart.append(item)

        def can_add(cart):
            return len(cart) > MAX_ITEMS

        def clear(cart):
            cart.clear()
    """),
    target=text("""
        MAX_ITEMS = 10

        def add(cart, item):
            if len(cart) >= MAX_ITEMS:
                raise ValueError("cart is full")
            cart.append(item)

        def can_add(cart):
            return len(cart) < MAX_ITEMS

        def clear(cart):
            cart.clear()
    """),
    hint="* would find the next MAX_ITEMS, in add(). # goes backward, and from the first one in the file "
         "it wraps around to the last one, in can_add(). The > is the word just before it.",
    uses=["word", "r"],
)
star.add(
    title="Only in area()", par=11, ext="py", cursor=(1, 10),
    task="In area() only, rename w to width (two places). perimeter() keeps its w. The cursor starts on "
         "the w in area's parameters.",
    start=text("""
        def area(w, h):
            return w * h

        def perimeter(w, h):
            return 2 * (w + h)
    """),
    target=text("""
        def area(width, h):
            return width * h

        def perimeter(w, h):
            return 2 * (w + h)
    """),
    hint="Search before you change: * goes to the w on line 2. Change it, then N goes back up to the first "
         "w (n would go on to perimeter's), and . repeats the change.",
    uses=["c", "search", "dot"],
)
star.add(
    title="Rename the alias", par=14, ext="sql",
    task="Rename the alias spent to revenue, in both places.",
    start=text("""
        SELECT customer_id AS cid, sum(total) AS spent
        FROM orders
        GROUP BY cid
        HAVING sum(total) > 100
        ORDER BY spent DESC;
    """),
    target=text("""
        SELECT customer_id AS cid, sum(total) AS revenue
        FROM orders
        GROUP BY cid
        HAVING sum(total) > 100
        ORDER BY revenue DESC;
    """),
    hint="$ puts the cursor on the last letter of spent, and * works from anywhere in a word. It finds the "
         "spent on the last line; change it there, then n wraps around to line 1 for the .",
    uses=["line", "c", "search", "dot"],
)
star.add(
    title="Not OUT_DIR", par=14, ext="sh",
    task="Rename the variable OUT to DIST everywhere (four places), but leave OUT_DIR alone.",
    start=text("""
        OUT=dist
        OUT_DIR=/tmp/logs
        mkdir -p "$OUT"
        cp -r public/* "$OUT/"
        echo "built into $OUT, logs in $OUT_DIR"
    """),
    target=text("""
        DIST=dist
        OUT_DIR=/tmp/logs
        mkdir -p "$DIST"
        cp -r public/* "$DIST/"
        echo "built into $DIST, logs in $OUT_DIR"
    """),
    hint="* matches whole words, and the $ isn't part of the word, so it stops at every $OUT but never in "
         "OUT_DIR. Change the first one it finds, then n. until you're back on line 1.",
    uses=["c", "search", "dot"],
)
star.add(
    title="Strip the dumps", par=7, ext="py", cursor=(2, 5),
    task="Remove the three dump(...) lines. The cursor starts on the first one.",
    start=text("""
        def handle(req):
            dump(req)
            user = auth(req)
            if not user:
                dump(req.headers)
                return deny()
            result = run(user, req)
            dump(result)
            return result
    """),
    target=text("""
        def handle(req):
            user = auth(req)
            if not user:
                return deny()
            result = run(user, req)
            return result
    """),
    hint="Search first: once you've deleted this line, there's no dump under the cursor. * goes to the "
         "next one; dd it, then n and . for the others (n wraps around to the first).",
    uses=["dd", "search", "dot"],
)
star.add(
    title="It's an attribute", par=14, ext="py", cursor=(3, 9),
    task="count is the object's attribute: make it self.count in the four places it's used as a variable, "
         "but not in the message \"count is now\". The cursor starts on the first count.",
    start=text("""
        class Counter:
            def bump(self, step):
                count = count + step
                log("count is now", count)
                return count
    """),
    target=text("""
        class Counter:
            def bump(self, step):
                self.count = self.count + step
                log("count is now", self.count)
                return self.count
    """),
    hint="Type self. in front of the first count. The cursor is then on the dot, and * there uses the next "
         "word, count, and jumps to the count after it, where . types self. again. Each . leaves you on a "
         "dot like that, so keep going with * (n would find the count right after the dot). Skip the one "
         "in the message with n.",
    uses=["insert", "search", "dot"],
)

# ---------- ge gE ----------

ge = drills.command(
    "ge", "ge  gE", "back to the end of the previous word",
    """ge moves backward to the last character of the previous word, and gE to the last character of the
    previous WORD (anything between spaces). They're the backward twins of e and E, and they're handiest
    when the cursor is in the middle of a word: b would only go to the start of the current one. As
    motions they're inclusive, so dge and dgE delete both ends: the end of the previous word and the
    character under the cursor. From the last letter of an argument, dgE deletes it along with the comma
    before it.""",
    examples=[("ge", "end of the previous word"), ("gE", "end of the previous WORD"),
              ("gex", "delete the previous word's last letter"), ("dgE", "delete back through the previous WORD's end"),
              ("gea", "append to the previous word")],
    level="complex",
)
ge.add(
    title="Drop the strict flag", par=3, ext="py", cursor=(1, 23),
    task="Remove the last argument and its comma, so the call reads zip(xs, ys). The cursor starts on the e "
         "of True.",
    start="zip(xs, ys, strict=True)",
    target="zip(xs, ys)",
    hint="gE goes back to the end of the previous WORD, which is the comma after ys. It's inclusive, so dgE "
         "deletes from that comma through the e under the cursor.",
    uses=["d"],
)
ge.add(
    title="One letter too many", par=3, ext="txt", cursor=(1, 21),
    task='Fix "thee" to "the". The cursor starts at the end of tests.',
    start="We ran all thee tests again.",
    target="We ran all the tests again.",
    hint="ge jumps back to the last letter of the previous word, wherever you are in the current one. Then "
         "delete it.",
    uses=["x"],
)
ge.add(
    title="A stray slash", par=3, ext="sh", cursor=(1, 25),
    task="Delete the / right after notes.txt. The cursor starts on the o of the second notes.",
    start="cp notes.txt/ ~/backup/notes/",
    target="cp notes.txt ~/backup/notes/",
    hint="The slash is the last character of the previous WORD, and gE goes straight there. (ge would stop "
         "at the end of each small word inside the path.)",
    uses=["x"],
)
ge.add(
    title="One string, not two", par=3, ext="py", cursor=(4, 10),
    task="Join the two pieces of the help text into one string, so line 3 reads help=\"Retries after a "
         "failed download. Use 0 to fail at once.\",. The cursor starts on the opening quote of line 4.",
    start=text("""
        parser.add_argument(
            "--retries", type=int, default=3,
            help="Retries after a failed download."
                 " Use 0 to fail at once.",
        )
    """),
    target=text("""
        parser.add_argument(
            "--retries", type=int, default=3,
            help="Retries after a failed download. Use 0 to fail at once.",
        )
    """),
    hint="gE crosses line breaks too: from here, the end of the previous WORD is the closing quote at the end "
         "of line 3. It's inclusive, so dgE deletes both quotes and everything between them.",
    uses=["d"],
)
ge.add(
    title="Drop two columns", par=4, ext="sql", cursor=(1, 29),
    task="The report no longer needs email and phone: line 1 should read SELECT id, name, created_at. The "
         "cursor starts on the e at the end of phone.",
    start=text("""
        SELECT id, name, email, phone, created_at
        FROM customers
        WHERE active = 1
        ORDER BY created_at DESC;
    """),
    target=text("""
        SELECT id, name, created_at
        FROM customers
        WHERE active = 1
        ORDER BY created_at DESC;
    """),
    hint="Each column and its comma is one WORD, so 2gE goes back two WORD ends, to the comma after name. "
         "d2gE deletes from that comma through the e under the cursor.",
    uses=["count", "d"],
)
ge.add(
    title="A comma, not a period", par=4, ext="js", cursor=(3, 43),
    task="The log shows one value instead of two: the period after order.id should be a comma, so line 3 "
         "reads console.log(\"paid\", order.id, order.total);. The cursor starts on the l at the end of total.",
    start=text("""
        async function markPaid(order) {
          await db.orders.update(order.id, { status: "paid" });
          console.log("paid", order.id. order.total);
        }
    """),
    target=text("""
        async function markPaid(order) {
          await db.orders.update(order.id, { status: "paid" });
          console.log("paid", order.id, order.total);
        }
    """),
    hint="order.id. is one WORD, and its last character is the stray period. gE lands on it in one move, "
         "and r replaces it.",
    uses=["r"],
)

# ---------- m ' ` ----------

marks = drills.command(
    "marks", "m{a}  '{a}  `{a}", "set a mark and jump back to it",
    """ma sets mark a at the cursor (any letter a to z works). Later, `a (backtick) jumps back to that exact
    spot and 'a (apostrophe) to the first non-blank of its line, however you moved away. As nouns, 'a is
    line-wise and `a is exclusive: d'a deletes whole lines from here to the mark's line, and y`a copies
    from the mark up to the cursor. Marks move with their text when lines are added or deleted above them.
    Neovim also keeps marks for you: '' or `` is where you were before your latest jump.""",
    examples=[("ma", "set mark a"), ("`a", "back to the exact spot"), ("'a", "back to the line"),
              ("d'a", "delete lines from here to the mark"), ("y'a", "copy lines from here to the mark"),
              ("``", "back to before the last jump")],
    level="complex",
)
marks.add(
    title="Mark the spot", par=9, ext="py", cursor=(2, 22),
    task="Pass WELCOME_SUBJECT as the second argument: line 2 should read send(user.email, WELCOME_SUBJECT). "
         "The cursor starts on the ).",
    start=text("""
        def notify(user):
            send(user.email, )


        WELCOME_SUBJECT = "Welcome to the course!"
    """),
    target=text("""
        def notify(user):
            send(user.email, WELCOME_SUBJECT)


        WELCOME_SUBJECT = "Welcome to the course!"
    """),
    hint="Set a mark here with ma. G and 0 take you to the constant, and ye copies its name. `a jumps back to "
         "the exact spot you marked, and P puts the name before the ).",
    uses=["gg", "line", "y", "p"],
)
marks.add(
    title="Delete to the mark", par=7, ext="c", cursor=(2, 5),
    task="Remove the whole debug block, from if (s->debug) { to its closing }. The cursor starts on the if.",
    start=text("""
        void step(State *s) {
            if (s->debug) {
                dump(s);
                log_state(s);
            }
            advance(s);
        }
    """),
    target=text("""
        void step(State *s) {
            advance(s);
        }
    """),
    hint="Mark the first line with ma. $% jumps to the } that closes the block, however long it is. d'a then "
         "deletes whole lines from there back to the mark's line.",
    uses=["line", "percent", "d"],
)
marks.add(
    title="Copy a function", par=9, ext="c",
    task="Put a copy of clamp() (all five lines) at the end of the file, as a starting point for a float "
         "version.",
    start=text("""
        int clamp(int x, int lo, int hi) {
            if (x < lo) return lo;
            if (x > hi) return hi;
            return x;
        }
        int main(void) {
            return clamp(5, 0, 3);
        }
    """),
    target=text("""
        int clamp(int x, int lo, int hi) {
            if (x < lo) return lo;
            if (x > hi) return hi;
            return x;
        }
        int main(void) {
            return clamp(5, 0, 3);
        }
        int clamp(int x, int lo, int hi) {
            if (x < lo) return lo;
            if (x > hi) return hi;
            return x;
        }
    """),
    hint="ma marks the first line. $% finds the closing brace, and y'a copies every line from there back to "
         "the mark. G and p put the copy below the last line.",
    uses=["line", "percent", "y", "gg", "p"],
)
marks.add(
    title="Pasted flush left", par=10, ext="py", cursor=(12, 1),
    task="The body of load() was pasted without its indentation. Indent lines 12 to 23 by two levels (8 "
         "spaces), so they're inside the method again, and fix the typo retrun on line 23. The cursor starts "
         "on line 12.",
    start=text("""
        import csv
        import logging

        log = logging.getLogger(__name__)


        class UserImporter:
            def __init__(self, path):
                self.path = path

            def load(self):
        seen = set()
        users = []
        with open(self.path, newline="") as f:
            for row in csv.DictReader(f):
                email = row["email"].strip().lower()
                if email in seen:
                    log.warning("duplicate user %s", email)
                    continue

                seen.add(email)
                users.append(User(row["name"], email))
        retrun users

            def count(self):
                return len(self.load())
    """),
    target=text("""
        import csv
        import logging

        log = logging.getLogger(__name__)


        class UserImporter:
            def __init__(self, path):
                self.path = path

            def load(self):
                seen = set()
                users = []
                with open(self.path, newline="") as f:
                    for row in csv.DictReader(f):
                        email = row["email"].strip().lower()
                        if email in seen:
                            log.warning("duplicate user %s", email)
                            continue

                        seen.add(email)
                        users.append(User(row["name"], email))
                return users

            def count(self):
                return len(self.load())
    """),
    hint="Fix the typo first: /ru and Enter jumps onto it and xp swaps two letters. That search was a jump, "
         "so '' is now a motion back to line 12, and >'' indents every line in between. . does it again, "
         "and '' still covers the same lines.",
    uses=["search", "x", "p", "indent", "dot"],
)
marks.add(
    title="The same order twice", par=10, ext="yaml", cursor=(4, 3),
    task="The test needs order 1042 in the file twice. Fix the typo deks (desk) on its last line, line 17, "
         "then duplicate the whole order, lines 4 to 17, so the two copies sit one after the other. The "
         "cursor starts on the - of line 4.",
    start=text("""
        # Orders for test_import_skips_duplicates: the importer must keep only one
        # copy of an order that appears twice.
        orders:
          - id: 1042
            customer: ada@example.com
            placed_at: 2026-10-30T09:14:00Z
            currency: EUR
            items:
              - sku: KB-101
                qty: 1
                price: 89.00

              - sku: MS-220
                qty: 2
                price: 24.50
            shipping: standard
            notes: leave at the front deks
          - id: 1043
            customer: grace@example.com
            placed_at: 2026-10-30T11:02:00Z
            currency: USD
            items:
              - sku: HD-310
                qty: 1
                price: 129.00
            shipping: express
            notes: ""
    """),
    target=text("""
        # Orders for test_import_skips_duplicates: the importer must keep only one
        # copy of an order that appears twice.
        orders:
          - id: 1042
            customer: ada@example.com
            placed_at: 2026-10-30T09:14:00Z
            currency: EUR
            items:
              - sku: KB-101
                qty: 1
                price: 89.00

              - sku: MS-220
                qty: 2
                price: 24.50
            shipping: standard
            notes: leave at the front desk
          - id: 1042
            customer: ada@example.com
            placed_at: 2026-10-30T09:14:00Z
            currency: EUR
            items:
              - sku: KB-101
                qty: 1
                price: 89.00

              - sku: MS-220
                qty: 2
                price: 24.50
            shipping: standard
            notes: leave at the front desk
          - id: 1043
            customer: grace@example.com
            placed_at: 2026-10-30T11:02:00Z
            currency: USD
            items:
              - sku: HD-310
                qty: 1
                price: 129.00
            shipping: express
            notes: ""
    """),
    hint="Fix first, so both copies get it: /ks and Enter, then xp. You jumped there from line 4, so y'' "
         "copies every line from here back to line 4, and leaves the cursor on line 4. P puts the copy above "
         "it.",
    uses=["search", "x", "y", "p"],
)
marks.add(
    title="Troubleshooting goes last", par=11, ext="md", cursor=(4, 1),
    task="Move the Troubleshooting section (lines 4 to 14: the blank line above the heading, down to its last "
         "line) to the end of the file, and fix the typo adn on its last line. The cursor starts on the blank "
         "line 4.",
    start=text("""
        # fastq-trim

        Trim adapters and low-quality ends from FASTQ files, fast.

        ## Troubleshooting

        **"No adapters found"**: pass the adapter sequence with `--adapter`.

        **Slow on large files**: use `--threads` to match your CPU count.
        The default is a single thread.

        **Empty output**: check that the input isn't gzipped twice. `--input`
        takes `.fastq` and `.fastq.gz`, but not `.gz.gz`. Run with `--verbose`
        to find out which reads were dropped adn why.

        ## Install

            pip install fastq-trim

        ## Usage

            fastq-trim --adapter AGATCGGAAGAGC reads.fastq.gz -o trimmed.fastq.gz
    """),
    target=text("""
        # fastq-trim

        Trim adapters and low-quality ends from FASTQ files, fast.

        ## Install

            pip install fastq-trim

        ## Usage

            fastq-trim --adapter AGATCGGAAGAGC reads.fastq.gz -o trimmed.fastq.gz

        ## Troubleshooting

        **"No adapters found"**: pass the adapter sequence with `--adapter`.

        **Slow on large files**: use `--threads` to match your CPU count.
        The default is a single thread.

        **Empty output**: check that the input isn't gzipped twice. `--input`
        takes `.fastq` and `.fastq.gz`, but not `.gz.gz`. Run with `--verbose`
        to find out which reads were dropped and why.
    """),
    hint="/dn and Enter jumps to the typo, and xp fixes it. You jumped there from line 4, so d'' cuts every "
         "line from here back to line 4. G and p put them below the last line.",
    uses=["search", "x", "p", "d", "gg"],
)

# ---------- Ctrl-o Ctrl-i ----------

jumps = drills.command(
    "jumps", "Ctrl-o  Ctrl-i", "back and forward through your jumps",
    """Some motions are jumps: G, gg, {N}G, / and ?, n and N, * and #, %, { and }, and jumping to a mark.
    Before each one, Neovim saves where you were in the jump list. Ctrl-o goes back to the previous saved
    place (to the exact column) and Ctrl-i, which is the same key as Tab, goes forward again. So you can
    jump away to copy or check something and come straight back. Small moves like j, w and f aren't
    jumps and don't count, and neither is :42.""",
    examples=[("Ctrl-o", "back to where you jumped from"), ("Ctrl-i", "forward again"), ("Tab", "the same key as Ctrl-i"),
              ("Gye Ctrl-o p", "fetch a word from the end and come back"), ("2 Ctrl-o", "two jumps back")],
    level="complex",
)
jumps.add(
    title="Fetch from the bottom", par=7, ext="py", cursor=(2, 18),
    task="Use the constant from the last line instead of width: line 2 should end with * BANNER_WIDTH. The "
         "cursor starts on width.",
    start=text("""
        def banner(title):
            line = "=" * width
            return f"{line}\\n{title}\\n{line}"


        BANNER_WIDTH = 72
    """),
    target=text("""
        def banner(title):
            line = "=" * BANNER_WIDTH
            return f"{line}\\n{title}\\n{line}"


        BANNER_WIDTH = 72
    """),
    hint="Delete width first (D). G is a jump to the last line, where 0ye copies the name. Ctrl-o jumps back "
         "to exactly where you were, and p puts the name there.",
    uses=["d", "gg", "line", "y", "p"],
)
jumps.add(
    title="Borrow the signature", par=9, ext="py", cursor=(2, 22),
    task="Call fetch_page with the same arguments as its definition: line 2 should read "
         "page = fetch_page(url, timeout=10). The cursor starts on the (.",
    start=text("""
        def main():
            page = fetch_page()
            print(page)


        def fetch_page(url, timeout=10):
            return http.get(url, timeout=timeout)
    """),
    target=text("""
        def main():
            page = fetch_page(url, timeout=10)
            print(page)


        def fetch_page(url, timeout=10):
            return http.get(url, timeout=timeout)
    """),
    hint="Delete the empty () with d%. * jumps to the definition, and y% copies its whole parameter list from "
         "the (. Ctrl-o brings you back, and p puts the copy after the name.",
    uses=["percent", "star", "f", "y", "p"],
)
jumps.add(
    title="There and back again", par=13, ext="py", cursor=(1, 12),
    task="Set TLS_CERT to the path in OLD_CERT_PATH (quotes included), then delete the deprecated comment and "
         "OLD_CERT_PATH, with the blank line above them. The cursor starts on None.",
    start=text("""
        TLS_CERT = None
        TLS_KEY = "/etc/ssl/private/api.key"

        # deprecated: remove once TLS_CERT is set
        OLD_CERT_PATH = "/etc/ssl/certs/api.example.com.pem"

        TIMEOUT = 30
    """),
    target=text("""
        TLS_CERT = "/etc/ssl/certs/api.example.com.pem"
        TLS_KEY = "/etc/ssl/private/api.key"

        TIMEOUT = 30
    """),
    hint="You can't delete the old lines before you've copied the path, and deleting would replace what you "
         "copied. So: D, then 5G to the old line, f\" and yE to copy the path, Ctrl-o back, p. Then Tab (which "
         "is Ctrl-i) jumps forward to the old line again, and d2k deletes it with the two lines above.",
    uses=["d", "gg", "f", "bigword", "y", "p"],
)
jumps.add(
    title="Keep them in order", par=6, ext="py", cursor=(5, 16),
    task="The upload form lists these types in this order, but a set has no order. Make UPLOAD_TYPES a list: "
         "change its { to [ and its } to ]. The cursor starts on the {.",
    start=text("""
        import mimetypes
        from pathlib import Path

        # Shown on the upload form in this order.
        UPLOAD_TYPES = {
            "image/png",
            "image/jpeg",
            "image/webp",
            "image/gif",
            "application/pdf",
            "text/plain",
            "text/csv",
            "application/zip",
            "application/json",
        }
        MAX_UPLOAD_BYTES = 10 * 1024 * 1024


        def is_allowed(path: Path) -> bool:
            kind, _ = mimetypes.guess_type(path.name)
            return kind in UPLOAD_TYPES
    """),
    target=text("""
        import mimetypes
        from pathlib import Path

        # Shown on the upload form in this order.
        UPLOAD_TYPES = [
            "image/png",
            "image/jpeg",
            "image/webp",
            "image/gif",
            "application/pdf",
            "text/plain",
            "text/csv",
            "application/zip",
            "application/json",
        ]
        MAX_UPLOAD_BYTES = 10 * 1024 * 1024


        def is_allowed(path: Path) -> bool:
            kind, _ = mimetypes.guess_type(path.name)
            return kind in UPLOAD_TYPES
    """),
    hint="% only finds the partner while both braces still match, so do the closing one first: % jumps "
         "there and r] replaces it. % is a jump, so Ctrl-o goes straight back to the {.",
    uses=["percent", "r"],
)
jumps.add(
    title="Crossed wires", par=9, ext="yaml", cursor=(12, 17),
    task="The two database URLs got swapped: production should use db-prod and staging db-staging. Swap the "
         "two URLs (everything after database_url: ). The cursor starts on the p of postgres in line 12.",
    start=text("""
        # Deploy settings, one block per environment.
        # Secrets (passwords, tokens) come from the vault, not from this file.

        defaults: &defaults
          timeout_seconds: 30
          retries: 3
          log_format: json

        production:
          <<: *defaults
          api_url: https://api.example.com/v2
          database_url: postgres://app@db-staging.internal:5432/shop
          cache_url: redis://cache-prod.internal:6379/0
          queue_url: amqp://mq-prod.internal:5672
          log_level: warn
          workers: 8
          replicas: 4

        staging:
          <<: *defaults
          api_url: https://api.staging.example.com/v2
          database_url: postgres://app@db-prod.internal:5432/shop
          cache_url: redis://cache-staging.internal:6379/0
          queue_url: amqp://mq-staging.internal:5672
          log_level: debug
          workers: 2
          replicas: 1
    """),
    target=text("""
        # Deploy settings, one block per environment.
        # Secrets (passwords, tokens) come from the vault, not from this file.

        defaults: &defaults
          timeout_seconds: 30
          retries: 3
          log_format: json

        production:
          <<: *defaults
          api_url: https://api.example.com/v2
          database_url: postgres://app@db-prod.internal:5432/shop
          cache_url: redis://cache-prod.internal:6379/0
          queue_url: amqp://mq-prod.internal:5672
          log_level: warn
          workers: 8
          replicas: 4

        staging:
          <<: *defaults
          api_url: https://api.staging.example.com/v2
          database_url: postgres://app@db-staging.internal:5432/shop
          cache_url: redis://cache-staging.internal:6379/0
          queue_url: amqp://mq-staging.internal:5672
          log_level: debug
          workers: 2
          replicas: 1
    """),
    hint="D cuts this URL. 22G is a jump to the other one (the column stays put), where p puts the cut URL "
         "in front of it; l and D cut the old one. Ctrl-o brings you back to line 12, and p puts it there.",
    uses=["d", "gg", "p"],
)
jumps.add(
    title="A stray import", par=5, ext="js",
    task="Someone added an import halfway down the file. Move it up into the imports: it goes right below the "
         "first line, so they stay sorted.",
    start=text("""
        import express from "express";
        import helmet from "helmet";
        import morgan from "morgan";

        const app = express();
        app.use(helmet());
        app.use(morgan("tiny"));
        app.use(express.json());

        import { rateLimit } from "express-rate-limit";
        app.use(rateLimit({ windowMs: 60_000, limit: 100 }));

        app.get("/health", (req, res) => res.json({ ok: true }));
        app.get("/version", (req, res) => res.json({ version: process.env.APP_VERSION }));

        app.listen(process.env.PORT ?? 3000);
    """),
    target=text("""
        import express from "express";
        import { rateLimit } from "express-rate-limit";
        import helmet from "helmet";
        import morgan from "morgan";

        const app = express();
        app.use(helmet());
        app.use(morgan("tiny"));
        app.use(express.json());

        app.use(rateLimit({ windowMs: 60_000, limit: 100 }));

        app.get("/health", (req, res) => res.json({ ok: true }));
        app.get("/version", (req, res) => res.json({ version: process.env.APP_VERSION }));

        app.listen(process.env.PORT ?? 3000);
    """),
    hint="# searches backward for the word under the cursor, and wraps around past the top: from the first "
         "import, it lands on the last one in the file, the stray one. dd cuts it, Ctrl-o jumps back to line 1, "
         "and p puts the line below it.",
    uses=["star", "dd", "p"],
)

# ---------- `. g; gi ----------

changes = drills.command(
    "changes", "`.  g;  gi", "back to your last change or insert",
    """Neovim remembers where you change text. `. (backtick, dot) jumps to the spot of the last change,
    and g; steps back through older changes one at a time (g, goes forward again; the first g; goes to
    the newest change). gi goes back into Insert mode exactly where you last left it, so you can stop
    typing, fix something elsewhere, and carry on. Unlike Ctrl-o, they don't care how you moved away:
    j, w and f work as well as searches.""",
    examples=[("`.", "where you last changed text"), ("g;", "back one change"), ("2g;", "back two changes"),
              ("g,", "forward one change"), ("gi", "carry on typing where you stopped")],
    level="complex",
)
changes.add(
    title="Back to typing", par=21, ext="py", cursor=(4, 23),
    task="Fix the typo in the function's name (totla) and make line 4 read grand = compute_total(prices, "
         "tax). The cursor starts on the ) of line 4.",
    start=text("""
        def compute_totla(items):
            return sum(items)

        grand = compute_total()
    """),
    target=text("""
        def compute_total(items):
            return sum(items)

        grand = compute_total(prices, tax)
    """),
    hint="Start typing prices, then (as if you'd just noticed the typo) press <Esc>, search back with ?la and "
         "swap the two letters with xp. gi puts you back in Insert mode right after prices.",
    uses=["insert", "search", "x", "p"],
)
changes.add(
    title="Fill the placeholder", par=9, ext="py", cursor=(1, 7),
    task="Replace TODO with the name API_BASE from line 2, so line 1 reads URL = API_BASE + "
         "\"/v2/users\". The cursor starts on TODO.",
    start=text("""
        URL = TODO + "/v2/users"
        API_BASE = "https://api.example.com"
    """),
    target=text("""
        URL = API_BASE + "/v2/users"
        API_BASE = "https://api.example.com"
    """),
    hint="Delete TODO and its space with dw first (deleting later would replace what you copy). Go down, copy "
         "API_BASE and its space with yw from column 1, then `. jumps back to where you deleted. P puts it there.",
    uses=["d", "line", "y", "p"],
)
changes.add(
    title="Where was I?", par=11, ext="py", cursor=(1, 11),
    task="Replace TODO with the timeout's old config name, DEFAULT_TIMEOUT_SECONDS (the second name in the "
         "comments). The cursor starts on TODO.",
    start=text("""
        TIMEOUT = TODO
        RETRIES = 3

        # old config names:
        # retries: DEFAULT_RETRY_COUNT
        # timeout: DEFAULT_TIMEOUT_SECONDS
    """),
    target=text("""
        TIMEOUT = DEFAULT_TIMEOUT_SECONDS
        RETRIES = 3

        # old config names:
        # retries: DEFAULT_RETRY_COUNT
        # timeout: DEFAULT_TIMEOUT_SECONDS
    """),
    hint="D deletes TODO. /DE and Enter finds the first name, n the second; ye copies it. You made two jumps, "
         "so one Ctrl-o wouldn't get you home, but g; goes straight back to your last change. Then p.",
    uses=["d", "search", "y", "p"],
)
changes.add(
    title="Use the pinned image", par=9, ext="yaml", cursor=(3, 12),
    task="Replace TODO with the image named in the comment, registry.example.com/payments/api:1.14.2, and "
         "keep the comment. The cursor starts on TODO.",
    start=text("""
        services:
          api:
            image: TODO  # pin: registry.example.com/payments/api:1.14.2
            ports:
              - "8080:8080"
            environment:
              DATABASE_URL: postgres://app@db:5432/payments
          db:
            image: postgres:16
    """),
    target=text("""
        services:
          api:
            image: registry.example.com/payments/api:1.14.2  # pin: registry.example.com/payments/api:1.14.2
            ports:
              - "8080:8080"
            environment:
              DATABASE_URL: postgres://app@db:5432/payments
          db:
            image: postgres:16
    """),
    hint="de deletes TODO first (deleting later would replace what you copy). $ and B get to the image name, "
         "the last WORD, and yE copies it. `. jumps back to where you deleted, and P puts the name there.",
    uses=["d", "line", "bigword", "y", "p"],
)
changes.add(
    title="Fix it, then use it", par=11, ext="py", cursor=(11, 49),
    task="Line 10 should define subtotal (lowercase s), and line 11 should use it in place of TBD. The cursor "
         "starts on TBD.",
    start=text("""
        from decimal import Decimal

        DISCOUNTS = {"WELCOME10": Decimal("0.10"), "VIP": Decimal("0.20")}


        def checkout(cart):
            if not cart.items:
                raise ValueError("cart is empty")

            Subtotal = cart.items_total() + cart.fees
            total = max(0, (1 - DISCOUNTS[cart.code]) * TBD - cart.gift_card_balance)
            return total.quantize(Decimal("0.01"))


        def receipt_line(cart):
            return f"{len(cart.items)} items, {checkout(cart)} EUR"
    """),
    target=text("""
        from decimal import Decimal

        DISCOUNTS = {"WELCOME10": Decimal("0.10"), "VIP": Decimal("0.20")}


        def checkout(cart):
            if not cart.items:
                raise ValueError("cart is empty")

            subtotal = cart.items_total() + cart.fees
            total = max(0, (1 - DISCOUNTS[cart.code]) * subtotal - cart.gift_card_balance)
            return total.quantize(Decimal("0.01"))


        def receipt_line(cart):
            return f"{len(cart.items)} items, {checkout(cart)} EUR"
    """),
    hint="de deletes TBD. - goes up to the S, rs fixes it, and ye copies the fixed name. That fix was a change "
         "too, so g; would stop there first: 2g; goes back two changes, to where TBD was, and P puts the name "
         "there.",
    uses=["d", "plus", "r", "y", "count", "p"],
)
changes.add(
    title="Wire it up", par=9, ext="java", cursor=(12, 54),
    task="Pass the repository from line 11 into the OrderService: line 12 should read OrderService "
         "orderService = new OrderService(customerRepository, clock);. The cursor starts on TODO.",
    start=text("""
        package shop.app;

        import java.time.Clock;
        import javax.sql.DataSource;

        public final class App {
            public static void main(String[] args) {
                DataSource dataSource = Database.connect(System.getenv("DATABASE_URL"));
                Clock clock = Clock.systemUTC();

                CustomerRepository customerRepository = new JdbcCustomerRepository(dataSource);
                OrderService orderService = new OrderService(TODO, clock);
                orderService.start();
            }
        }
    """),
    target=text("""
        package shop.app;

        import java.time.Clock;
        import javax.sql.DataSource;

        public final class App {
            public static void main(String[] args) {
                DataSource dataSource = Database.connect(System.getenv("DATABASE_URL"));
                Clock clock = Clock.systemUTC();

                CustomerRepository customerRepository = new JdbcCustomerRepository(dataSource);
                OrderService orderService = new OrderService(customerRepository, clock);
                orderService.start();
            }
        }
    """),
    hint="de deletes TODO. - goes up a line to where the code starts, w to the variable, and ye copies it. "
         "`. takes you back to the spot you deleted, and P puts the name before the comma.",
    uses=["d", "plus", "word", "y", "p"],
)

# ---------- + - (glossary only) ----------

drills.command(
    "plus", "+  -", "first non-blank of the next or previous line",
    """+ (or Enter) moves down one line and - up one line, landing on the first non-blank character instead
    of keeping the column like j and k do. With a count, 3+ goes three lines down. As nouns they're
    line-wise, like j and k: d+ deletes this line and the next.""",
    examples=[("+", "next line, where the code starts"), ("-", "previous line, where the code starts"),
              ("3+", "three lines down"), ("d-", "delete this line and the one above")],
    level=None,
)
