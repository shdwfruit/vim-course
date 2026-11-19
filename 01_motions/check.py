"""Exercises for Project 01. Run:  python3 check.py   (python3 check.py 3 plays exercise 3)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "common"))
from trainer import Course, text  # noqa: E402

course = Course("Project 01 · Motions: get anywhere in a few keys", __file__,
                done_message="On to 02_text_objects, where you'll act on the thing the cursor is in.")

course.add(
    name="drop-argument", title="Drop an argument", par=4, ext="py",
    task="Remove the linewidth=2 argument (and the space after it).",
    start='plot(x, y, color="red", linewidth=2, label="data")',
    target='plot(x, y, color="red", label="data")',
    hint="Punctuation splits a line into lots of small words, but W hops a whole space-separated WORD "
         "at a time. Count the WORDs to linewidth, then delete one WORD.",
    uses=["bigword", "count", "d"],
)
course.add(
    name="return-it", title="Change back to the indent", par=9, ext="java",
    task="The method forgets to return its result. Turn the assignment into a return statement and keep "
         "the indentation. The cursor starts on the opening quote.",
    start=text("""
        String describe(int total) {
            String label = "Total: " + total;
        }
    """),
    target=text("""
        String describe(int total) {
            return "Total: " + total;
        }
    """),
    cursor=(2, 20),
    hint="Everything you want to replace is between the first non-blank character and the cursor. "
         "c works with a backward motion too, and ^ is a motion.",
    uses=["line", "c"],
)
course.add(
    name="drop-sort", title="Delete backward", par=5, ext="java",
    task="Return the names in their original order: remove the .sorted() call. The cursor starts at "
         "the end of the line.",
    start=text("""
        List<String> copy(List<String> names) {
            return names.stream().sorted().toList();
        }
    """),
    target=text("""
        List<String> copy(List<String> names) {
            return names.stream().toList();
        }
    """),
    cursor=(2, 44),
    hint="F jumps backward to a character. A backward motion never includes the character the cursor "
         "is on, so deleting backward from one dot to the previous dot removes exactly one call.",
    uses=["f", "d"],
)
course.add(
    name="match-bracket", title="Replace a bracketed group", par=5, ext="py",
    task="sd already holds the denominator. On line 2, replace the whole denominator, parentheses "
         "included, with sd.",
    start=text("""
        sd = stdev(xs) + 1e-9
        z = (x - mean(xs)) / (stdev(xs) + 1e-9)
    """),
    target=text("""
        sd = stdev(xs) + 1e-9
        z = (x - mean(xs)) / sd
    """),
    cursor=(2, 1),
    hint="The line ends on the closing parenthesis you want. % jumps from a bracket to its partner, "
         "and like any motion it can follow c.",
    uses=["percent", "line", "c"],
)
course.add(
    name="double-pattern", title="Repeat the whole pattern", par=3, ext="txt",
    task="Make the pattern twice as tall by repeating all six of its lines.",
    start=text(r"""
          /\    /\    /\
         /  \  /  \  /  \
        /    \/    \/    \
        \    /\    /\    /
         \  /  \  /  \  /
          \/    \/    \/
    """),
    target=text(r"""
          /\    /\    /\
         /  \  /  \  /  \
        /    \/    \/    \
        \    /\    /\    /
         \  /  \  /  \  /
          \/    \/    \/
          /\    /\    /\
         /  \  /  \  /  \
        /    \/    \/    \
        \    /\    /\    /
         \  /  \  /  \  /
          \/    \/    \/
    """),
    hint="G is a motion to the last line, so y + G copies every line from here to the end. "
         "Then put it back on the other side of the cursor's line.",
    uses=["gg", "y", "p"],
)
course.add(
    name="move-main", title="Move a function down", par=5, ext="c",
    task="main() calls square() before it's declared. Move main() (and the blank line above it) to the "
         "end of the file, so square() comes first.",
    start=text("""
        #include <stdio.h>

        int main(void) {
            printf("%d\\n", square(7));
            return 0;
        }

        int square(int x) {
            return x * x;
        }
    """),
    target=text("""
        #include <stdio.h>

        int square(int x) {
            return x * x;
        }

        int main(void) {
            printf("%d\\n", square(7));
            return 0;
        }
    """),
    hint="} jumps to the next blank line. From that blank line, d + } cuts the blank line and the "
         "paragraph below it in one go. Then put it after the last line.",
    uses=["paragraph", "d", "gg", "p"],
)
course.add(
    name="delete-to-word", title="Delete up to a word", par=6, ext="c",
    task="The bounds checks moved into a helper. Delete them, from the first x up to map, so the "
         "condition is only the wall check.",
    start=text("""
        if (x >= 0 && y >= 0 &&
            x < W && y < H &&
            map[y][x] != WALL) {
            move(x, y);
        }
    """),
    target=text("""
        if (map[y][x] != WALL) {
            move(x, y);
        }
    """),
    hint="A search is a motion, so d can take one: d, then /, a pattern and Enter deletes up to the "
         "match, across lines. The pattern only needs to be long enough to be unique.",
    uses=["search", "f", "d"],
)
course.add(
    name="delete-back", title="Delete back to a comma", par=4, ext="md",
    task="Shorten the first sentence to \"Install the package with pip.\" The cursor starts on the "
         "period after GitHub.",
    start=text("""
        Install the package with pip, or clone the repo
        and run make install if you want the latest
        version from GitHub. Then run the tests.
    """),
    target='Install the package with pip. Then run the tests.',
    cursor=(3, 20),
    hint="? searches backward, and d can use it as a motion. There's only one comma before the cursor, "
         "and a backward motion leaves the cursor's own character alone.",
    uses=["search", "d"],
)
course.add(
    name="rename-variable", title="Rename a variable", par=12, ext="py",
    task="Rename the variable tmp to size everywhere it appears. Leave tmpdir alone. The cursor starts "
         "on the first tmp.",
    start=text("""
        def total_size(tmpdir):
            tmp = 0
            for name in os.listdir(tmpdir):
                tmp += os.path.getsize(name)
            return tmp
    """),
    target=text("""
        def total_size(tmpdir):
            size = 0
            for name in os.listdir(tmpdir):
                size += os.path.getsize(name)
            return size
    """),
    cursor=(2, 5),
    hint="* searches for the whole word under the cursor, so it skips tmpdir. Change one match, then "
         "n goes to the next match and . repeats the change. The search wraps around the end of the file.",
    uses=["star", "c", "search", "dot"],
)
course.add(
    name="fetch-and-return", title="Fetch and come back", par=7, ext="java",
    task="Put a call to formatSummaryLine() inside the empty println(), borrowing the long name "
         "from its definition below. The cursor starts on the (.",
    start=text("""
        class Report {
            void print() {
                System.out.println();
            }

            String formatSummaryLine() {
                return rows.size() + " rows";
            }
        }
    """),
    target=text("""
        class Report {
            void print() {
                System.out.println(formatSummaryLine());
            }

            String formatSummaryLine() {
                return rows.size() + " rows";
            }
        }
    """),
    cursor=(3, 27),
    hint="Search for the definition (one letter is enough), yank the WORD, then Ctrl-o jumps back to "
         "exactly where you searched from. Put the text after the cursor.",
    uses=["jumps", "search", "bigword", "y", "p"],
)

course.add(
    name="review-inventory", title="Review · Tidy a Java class", par=85, ext="java",
    task="Review: Projects 00 and 01 together. This class works, but needs a round of fixes before code "
         "review. The edits are spread over the whole file, so get to them with searches and jumps rather "
         "than lots of j. Par uses only what Projects 00 and 01 teach.",
    steps=[
        "Sort the imports: ArrayList goes first.",
        "Nothing extends Inventory: make the class final.",
        "Neither field is ever reassigned: make both final too.",
        "count() counts by hand: its whole body should be return items.size();",
        "Then move count() down, below remove().",
        "In add(), rename the parameter item to name, everywhere it appears (the message too, but not items).",
        "The list is full once it holds limit items: test >= limit.",
        "all() hands out the list itself: return a copy, new ArrayList<>(items).",
    ],
    start=text("""
        import java.util.List;
        import java.util.ArrayList;

        public class Inventory {
            private List<String> items = new ArrayList<>();
            private int limit = 100;

            public int count() {
                int n = 0;
                for (String s : items) {
                    n++;
                }
                return n;
            }

            public void add(String item) {
                if (item == null || item.isEmpty()) {
                    throw new IllegalArgumentException("empty item");
                }
                if (items.size() > limit) {
                    throw new IllegalStateException("full");
                }
                items.add(item);
            }

            public String remove(int index) {
                return items.remove(index);
            }

            public List<String> all() {
                return items;
            }
        }
    """),
    target=text("""
        import java.util.ArrayList;
        import java.util.List;

        public final class Inventory {
            private final List<String> items = new ArrayList<>();
            private final int limit = 100;

            public void add(String name) {
                if (name == null || name.isEmpty()) {
                    throw new IllegalArgumentException("empty name");
                }
                if (items.size() >= limit) {
                    throw new IllegalStateException("full");
                }
                items.add(name);
            }

            public String remove(int index) {
                return items.remove(index);
            }

            public int count() {
                return items.size();
            }

            public List<String> all() {
                return new ArrayList<>(items);
            }
        }
    """),
    hint="* finds the next whole word under the cursor, so items never matches item, and n then . renames the "
         "rest. The code two of the edits need is already in the file: yank it where it is. From a blank "
         "line, d} cuts a whole method.",
    uses=["star", "search", "gg", "bigword", "line", "paragraph", "y", "p", "dot", "t"],
)
course.add(
    name="review-ring", title="Review · Clean up a ring buffer", par=75, ext="c",
    task="Review: Projects 00 and 01 together. ring.c is a fixed-size queue that compiles, but a review "
         "turned up ten things to fix. Par uses only what Projects 00 and 01 teach.",
    steps=[
        "string.h isn't used: delete its #include.",
        "Sort the two that are left: stdio.h goes first.",
        "Make the buffer hold 64 values.",
        "ring_push()'s if has one pair of parentheses too many, the one around (r->tail + 1) % CAP: remove it.",
        "Nothing outside this file calls ring_push(): make it static.",
        "Same for ring_pop().",
        "main() should push CAP values, not 20.",
        "Declare v at the top of main(), right under r.",
        "Print the values on one line, a space after each: \"%d \".",
        "Then end that line: add putchar('\\n'); after the while loop.",
    ],
    start=text("""
        #include <stdlib.h>
        #include <stdio.h>
        #include <string.h>

        #define CAP 16

        struct ring {
            int data[CAP];
            int head;
            int tail;
        };

        int ring_push(struct ring *r, int value) {
            if (((r->tail + 1) % CAP) == r->head) {
                return -1;
            }
            r->data[r->tail] = value;
            r->tail = (r->tail + 1) % CAP;
            return 0;
        }

        int ring_pop(struct ring *r, int *out) {
            if (r->head == r->tail) {
                return -1;
            }
            *out = r->data[r->head];
            r->head = (r->head + 1) % CAP;
            return 0;
        }

        int main(void) {
            struct ring r = {0};
            for (int i = 0; i < 20; i++) {
                ring_push(&r, i);
            }
            int v;
            while (ring_pop(&r, &v) == 0) {
                printf("%d\\n", v);
            }
            return 0;
        }
    """),
    target=text("""
        #include <stdio.h>
        #include <stdlib.h>

        #define CAP 64

        struct ring {
            int data[CAP];
            int head;
            int tail;
        };

        static int ring_push(struct ring *r, int value) {
            if ((r->tail + 1) % CAP == r->head) {
                return -1;
            }
            r->data[r->tail] = value;
            r->tail = (r->tail + 1) % CAP;
            return 0;
        }

        static int ring_pop(struct ring *r, int *out) {
            if (r->head == r->tail) {
                return -1;
            }
            *out = r->data[r->head];
            r->head = (r->head + 1) % CAP;
            return 0;
        }

        int main(void) {
            struct ring r = {0};
            int v;
            for (int i = 0; i < CAP; i++) {
                ring_push(&r, i);
            }
            while (ring_pop(&r, &v) == 0) {
                printf("%d ", v);
            }
            putchar('\\n');
            return 0;
        }
    """),
    hint="% jumps to a parenthesis's partner, and `` jumps back to exactly where you were before it (Ctrl-o "
         "keeps only one place per line, so it can't). } gets from one function to the next, and a search "
         "for a single character is often all it takes to get somewhere.",
    uses=["percent", "marks", "search", "paragraph", "dd", "p", "replace-mode", "insert", "dot", "r"],
)

course.run()
