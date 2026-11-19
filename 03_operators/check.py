"""Exercises for Project 03. Run:  python3 check.py   (python3 check.py 3 plays exercise 3)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "common"))
from trainer import Course, text  # noqa: E402

course = Course("Project 03 · More operators: case, indent, format, filter, comment", __file__,
                done_message="On to 04_visual_block, where you'll edit columns and rectangles and draw ASCII art.")

course.add(
    name="caps-lock", title="Caps Lock was on", par=3, ext="py",
    task="Caps Lock was on while you typed the two comment lines. Flip the case of every letter in them.",
    start=text("""
        # nEVER TRUST USER INPUT.
        # vALIDATE IT, THEN PARSE IT.
        def parse(raw):
            return json.loads(raw)
    """),
    target=text("""
        # Never trust user input.
        # Validate it, then parse it.
        def parse(raw):
            return json.loads(raw)
    """),
    hint="g~ is an operator that flips case. Give it a motion that covers this line and the next.",
    uses=["case"],
)
course.add(
    name="shout-constants", title="CONSTANT_CASE", par=8, ext="java",
    task="Java constants are written in CONSTANT_CASE. Uppercase the three constant names.",
    start=text("""
        public class Config {
            static final int max_retries = 3;
            static final int timeout_ms = 500;
            static final int buffer_size = 4096;
        }
    """),
    target=text("""
        public class Config {
            static final int MAX_RETRIES = 3;
            static final int TIMEOUT_MS = 500;
            static final int BUFFER_SIZE = 4096;
        }
    """),
    cursor=(2, 26),
    hint="gU + a text object uppercases a whole word from anywhere inside it. The names line up, "
         "so after the first one, j and . do the rest.",
    uses=["case", "iw", "dot"],
)
course.add(
    name="camel-case", title="camelCase a method name", par=6, ext="java",
    task="Rename the method to camelCase: getuserid should be getUserId.",
    start='int getuserid() { return userId; }',
    target='int getUserId() { return userId; }',
    hint="~ flips the case of the one character under the cursor. Jump to each letter with f.",
    uses=["case", "f"],
)
course.add(
    name="secret-message", title="Decode the secret", par=4, ext="py",
    task="The string is rot13-encoded. Decode the text inside the quotes, and only that: print must stay print.",
    start='print("Gur pnxr vf n yvr")',
    target='print("The cake is a lie")',
    hint="g? is the rot13 operator. Give it the text object for \"inside the quotes\": it finds the "
         "string even when the cursor is before it.",
    uses=["rot13", "quote"],
)
course.add(
    name="dedent-function", title="Dedent a function", par=3, ext="py",
    task="distance() was copied out of a class, so it's indented one level too deep. Make it a top-level function.",
    start=text("""
        import math


            def distance(p, q):
                dx = p[0] - q[0]
                dy = p[1] - q[1]
                return math.hypot(dx, dy)


        print(distance((0, 0), (3, 4)))
    """),
    target=text("""
        import math


        def distance(p, q):
            dx = p[0] - q[0]
            dy = p[1] - q[1]
            return math.hypot(dx, dy)


        print(distance((0, 0), (3, 4)))
    """),
    cursor=(6, 9),
    hint="< shifts lines one level left. The function is a paragraph (blank lines around it), so "
         "give < the paragraph text object. (= can't do this in Python. Try it and see.)",
    uses=["indent", "ip"],
)
course.add(
    name="reindent-method", title="Reindent a method", par=3, ext="java",
    task="The body of max() was pasted with broken indentation. Reindent it.",
    start=text("""
        public class Stats {
            static int sum(int a, int b) {
                return a + b;
            }

            static int max(int[] xs) {
        int best = xs[0];
              for (int x : xs) {
          if (x > best) {
        best = x;
                }
                    }
            return best;
            }
        }
    """),
    target=text("""
        public class Stats {
            static int sum(int a, int b) {
                return a + b;
            }

            static int max(int[] xs) {
                int best = xs[0];
                for (int x : xs) {
                    if (x > best) {
                        best = x;
                    }
                }
                return best;
            }
        }
    """),
    cursor=(9, 1),
    hint="= reindents lines with Java's indent rules. Give it a text object that covers the whole method. "
         "i{ only covers the innermost block around the cursor, and that isn't enough.",
    uses=["equal", "ip"],
)
course.add(
    name="toggle-comments", title="Toggle comments", par=6, ext="c",
    task="Comment out the two debug printf lines, and uncomment the two lines below them.",
    start=text(r"""
        int main(void) {
            int n = read_count();
            printf("debug: n=%d\n", n);
            printf("debug: start\n");
            // run(n);
            // report(n);
            return 0;
        }
    """),
    target=text(r"""
        int main(void) {
            int n = read_count();
            // printf("debug: n=%d\n", n);
            // printf("debug: start\n");
            run(n);
            report(n);
            return 0;
        }
    """),
    cursor=(3, 5),
    hint="gc + a motion toggles comments on those lines. Then . repeats the same toggle further down, "
         "and toggling lines that are already commented uncomments them.",
    uses=["comment", "count", "dot"],
)
course.add(
    name="join-lines", title="J and gJ", par=4, ext="c",
    task="Put each statement on one line. The array needs its usual space after the comma. The hash "
         "string was split in the middle and must not get a space.",
    start=text("""
        int primes[] = {2, 3, 5,
                        7, 11};
        char *hash = "9f86d081
        884c7d65";
    """),
    target=text("""
        int primes[] = {2, 3, 5, 7, 11};
        char *hash = "9f86d081884c7d65";
    """),
    hint="J joins with one space and removes the next line's indent. gJ joins the lines exactly as "
         "they are, adding nothing.",
    uses=["join", "gjoin"],
)
course.add(
    name="bump-ports", title="Bump the ports", par=7, ext="c",
    task="Move every port up by 10: 8080 becomes 8090, and so on.",
    start=text("""
        #define WEB_PORT 8080
        #define API_PORT 8081
        #define DNS_PORT 8053
    """),
    target=text("""
        #define WEB_PORT 8090
        #define API_PORT 8091
        #define DNS_PORT 8063
    """),
    hint="Ctrl-a adds to the first number at or after the cursor, so you don't need to move to it. "
         "A count adds that much, and . repeats it with the same count.",
    uses=["increment", "count", "dot"],
)
course.add(
    name="rewrap-comment", title="Rewrap a comment", par=4, ext="py",
    task="The comment got ragged after some edits. Rewrap it to fill lines up to the textwidth "
         "(set to 50 for this exercise), without touching the code.",
    start=text("""
        def knn(points, query, k):
            # Return the k points that are nearest to the query,
            # measured by
            # Euclidean distance, closest first. Ties go to the lower index.
            dists = distances(points, query)
            return argsort(dists)[:k]
    """),
    target=text("""
        def knn(points, query, k):
            # Return the k points that are nearest to the
            # query, measured by Euclidean distance,
            # closest first. Ties go to the lower index.
            dists = distances(points, query)
            return argsort(dists)[:k]
    """),
    cursor=(2, 5),
    setup=["setlocal textwidth=50"],
    hint="gq + a motion rewraps lines to 'textwidth' and keeps the # on each line. Cover only the "
         "three comment lines: ip would rewrap the code below them too.",
    uses=["gq", "count"],
)
course.add(
    name="sort-imports", title="Sort the imports", par=8, ext="java",
    task="Sort the import lines alphabetically.",
    start=text("""
        package app;

        import java.util.Map;
        import java.io.IOException;
        import java.util.ArrayList;
        import java.io.File;
        import java.util.List;

        public class App {}
    """),
    target=text("""
        package app;

        import java.io.File;
        import java.io.IOException;
        import java.util.ArrayList;
        import java.util.List;
        import java.util.Map;

        public class App {}
    """),
    cursor=(5, 1),
    hint="! + a motion sends lines through a shell command and puts its output in their place. "
         "The imports are a paragraph, and the shell command you want is sort.",
    uses=["filter", "ip"],
)
course.add(
    name="align-table", title="Line up a table", par=13, ext="txt",
    task="Line the table up into neat columns, two spaces after the widest entry in each column.",
    start=text("""
        Big-O cheat sheet

        structure access search insert
        array O(1) O(n) O(n)
        linked_list O(n) O(n) O(1)
        hash_table - O(1) O(1)
        bst O(log_n) O(log_n) O(log_n)
    """),
    target=text("""
        Big-O cheat sheet

        structure    access    search    insert
        array        O(1)      O(n)      O(n)
        linked_list  O(n)      O(n)      O(1)
        hash_table   -         O(1)      O(1)
        bst          O(log_n)  O(log_n)  O(log_n)
    """),
    cursor=(5, 1),
    hint="The shell command column -t lines up whitespace-separated columns. Filter the paragraph "
         "through it with !.",
    uses=["filter", "ip"],
)

course.add(
    name="review-logger", title="Review · Clean up a logger", par=67, ext="c",
    task="A logger needs a round of fixes before it can be merged. Apply the review, top to bottom. This one "
         "reviews Projects 00 to 03: par uses only what they teach.",
    steps=[
        "Sort the #include lines alphabetically.",
        "Macros are CONSTANT_CASE: uppercase log_version and log_buf_size, and the use of log_buf_size in "
        "log_line().",
        "Bump LOG_VERSION to 4.",
        "Double LOG_BUF_SIZE to 512.",
        "Delete the TODO comment and the debug variable under it, and the blank line after them.",
        "Rewrap the comment above log_line() to the textwidth (72 for this one).",
        "Join the fprintf() call onto one line.",
        "Comment out the debug printf().",
        "Reindent the body of log_line() by C's rules.",
        "Level numbers start at 0 now: 1, 2 and 3 become 0, 1 and 2.",
        "Lowercase the three level names.",
        "An unknown level returns \"unknown\" instead of \"?\".",
    ],
    start=text(r"""
        #include <time.h>
        #include <stdio.h>
        #include <string.h>
        #include <stdarg.h>

        #define log_version 3
        #define log_buf_size 256

        // TODO: remove before release
        static int debug = 1;

        /* Writes one line to out, prefixed with the time. Lines longer than the buffer are cut short. */
        void log_line(FILE *out, const char *fmt, ...)
        {
        char buf[log_buf_size];
        va_list args;
            va_start(args, fmt);
                vsnprintf(buf, sizeof buf, fmt, args);
            va_end(args);
          fprintf(out, "%ld %s\n",
                  (long)time(NULL), buf);
            printf("debug: wrote %zu bytes\n", strlen(buf));
        }

        const char *level_name(int level)
        {
            switch (level) {
            case 1: return "ERROR";
            case 2: return "WARN";
            case 3: return "INFO";
            }
            return "?";
        }
    """),
    target=text(r"""
        #include <stdarg.h>
        #include <stdio.h>
        #include <string.h>
        #include <time.h>

        #define LOG_VERSION 4
        #define LOG_BUF_SIZE 512

        /* Writes one line to out, prefixed with the time. Lines longer than the
         * buffer are cut short. */
        void log_line(FILE *out, const char *fmt, ...)
        {
            char buf[LOG_BUF_SIZE];
            va_list args;
            va_start(args, fmt);
            vsnprintf(buf, sizeof buf, fmt, args);
            va_end(args);
            fprintf(out, "%ld %s\n", (long)time(NULL), buf);
            // printf("debug: wrote %zu bytes\n", strlen(buf));
        }

        const char *level_name(int level)
        {
            switch (level) {
            case 0: return "error";
            case 1: return "warn";
            case 2: return "info";
            }
            return "unknown";
        }
    """),
    setup=["setlocal textwidth=72"],
    hint="The includes are a paragraph for ! and sort. After the first gU, * finds the macro's other use and "
         "Ctrl-o brings you back. Ctrl-x and . count the levels down, and the level lines have no other "
         "capitals, so gu with a line-wise motion is enough.",
    uses=["filter", "case", "star", "jumps", "increment", "dd", "gq", "join", "comment", "equal"],
)
course.add(
    name="review-backup-script", title="Review · Finish a backup script", par=57, ext="py",
    task="backup.py works, mostly. Finish it before it goes into cron. This one reviews Projects 00 to 03: "
         "par uses only what they teach.",
    steps=[
        "import sys was only for old_main(): delete it. Then sort the imports.",
        "Keep 7 backups instead of 5.",
        "compress_level is a constant: CONSTANT_CASE it, and lower it to 6.",
        "Delete old_main() and the blank lines after it.",
        "Python's class is datetime.date, with a lowercase d.",
        "A bad paste split isoformat() over two lines. Join it back, without adding a space.",
        "Dedent the stamp and name lines to match the rest of main().",
        "Comment out the DEBUG print.",
        "Make zip archives instead of gztar.",
        "Rewrap the long comment to the textwidth (72 for this one).",
        "Join prune()'s arguments onto one line.",
    ],
    start=text("""
        #!/usr/bin/env python3
        \"\"\"backup.py: copy a folder to a dated archive, keeping the newest few.\"\"\"
        import sys
        import shutil
        import os
        import argparse
        import datetime

        KEEP = 5
        compress_level = 9


        def parse_args():
            p = argparse.ArgumentParser(description="Back up a folder.")
            p.add_argument("source")
            p.add_argument("--dest", default="~/backups")
            p.add_argument("--keep", type=int, default=KEEP)
            return p.parse_args()


        def old_main():
            os.system("tar czf backup.tgz " + sys.argv[1])


        def main():
            args = parse_args()
                stamp = datetime.Date.today().iso
        format()
                name = os.path.join(args.dest, "backup-" + stamp)
            print("DEBUG", args)
            shutil.make_archive(name, "gztar", args.source)
            # Delete the oldest archives, so that only the newest args.keep of them are left in the destination folder.
            prune(args.dest,
                  args.keep)


        if __name__ == "__main__":
            main()
    """),
    target=text("""
        #!/usr/bin/env python3
        \"\"\"backup.py: copy a folder to a dated archive, keeping the newest few.\"\"\"
        import argparse
        import datetime
        import os
        import shutil

        KEEP = 7
        COMPRESS_LEVEL = 6


        def parse_args():
            p = argparse.ArgumentParser(description="Back up a folder.")
            p.add_argument("source")
            p.add_argument("--dest", default="~/backups")
            p.add_argument("--keep", type=int, default=KEEP)
            return p.parse_args()


        def main():
            args = parse_args()
            stamp = datetime.date.today().isoformat()
            name = os.path.join(args.dest, "backup-" + stamp)
            # print("DEBUG", args)
            shutil.make_archive(name, "zip", args.source)
            # Delete the oldest archives, so that only the newest args.keep of
            # them are left in the destination folder.
            prune(args.dest, args.keep)


        if __name__ == "__main__":
            main()
    """),
    setup=["setlocal textwidth=72"],
    hint="Deleting sys first leaves four imports to sort. gUU uppercases a whole line, and Ctrl-x with a "
         "count finds the number after the cursor. dap takes a function and the blank lines after it. gJ "
         "joins without a space. ci\" ends in Insert mode, so save it for last.",
    uses=["dd", "filter", "increment", "case", "ip", "gjoin", "indent", "comment", "gq", "quote"],
)

course.run()
