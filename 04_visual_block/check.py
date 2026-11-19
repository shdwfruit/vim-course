"""Exercises for Project 04. Run:  python3 check.py   (python3 check.py 3 plays exercise 3)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "common"))
from trainer import Course, text  # noqa: E402

course = Course("Project 04 · Visual and block mode: rectangles, columns and ASCII art", __file__,
                done_message="On to 05_registers, where you'll learn which of Vim's many clipboards "
                             "holds what.")

course.add(
    name="bullet-list", title="Make a bulleted list", par=7, ext="md",
    task="Turn the four items into a Markdown bulleted list: put \"- \" in front of each one.",
    start=text("""
        # Groceries

        eggs
        milk
        bread
        butter

        Buy before Friday.
    """),
    target=text("""
        # Groceries

        - eggs
        - milk
        - bread
        - butter

        Buy before Friday.
    """),
    cursor=(3, 1),
    hint="Ctrl-v starts a block selection. Make it one column wide and four lines tall, then I types "
         "in front of the block, and <Esc> copies what you typed to every line.",
    uses=["block-insert"],
)
course.add(
    name="ragged-semicolons", title="Semicolons on ragged lines", par=7, ext="java",
    task="Add the missing semicolon to the end of each of the four statements.",
    start=text("""
        void setup() {
            int width = 640
            int height = 480
            String title = "Pong"
            boolean running = true
        }
    """),
    target=text("""
        void setup() {
            int width = 640;
            int height = 480;
            String title = "Pong";
            boolean running = true;
        }
    """),
    cursor=(2, 5),
    hint="The lines have different lengths. In block mode, $ stretches the block to the end of every "
         "line, however long, and then A appends after each end.",
    uses=["block-insert"],
)
course.add(
    name="strip-line-numbers", title="Delete a column", par=5, ext="c",
    task="You copied this from a website and the line numbers came along. Delete the numbers and "
         "the \" | \" after them.",
    start=text("""
        1 | #include <stdio.h>
        2 |
        3 | int main(void) {
        4 |     puts("hello");
        5 |     return 0;
        6 | }
    """),
    target=text("""
        #include <stdio.h>

        int main(void) {
            puts("hello");
            return 0;
        }
    """),
    hint="Select the rectangle of line numbers with Ctrl-v, then d deletes just that rectangle. "
         "G goes to the last line and keeps your column.",
    uses=["block-edit", "gg"],
)
course.add(
    name="charge-battery", title="Charge the battery", par=6, ext="txt",
    task="Charge the battery to 80%: fill the next six cells of both rows with #.",
    start=text("""
        +----------+
        |##        |=
        |##        |=
        +----------+
    """),
    target=text("""
        +----------+
        |########  |=
        |########  |=
        +----------+
    """),
    cursor=(2, 4),
    hint="r works on a block too: it replaces every character in the rectangle with the one you type.",
    uses=["block-edit"],
)
course.add(
    name="hex-digits", title="Uppercase a column", par=5, ext="c",
    task="Uppercase the hex digits in the palette, but keep each 0x lowercase.",
    start=text("""
        uint32_t palette[] = {
            0xff8800,
            0x00aaff,
            0xc0ffee,
        };
    """),
    target=text("""
        uint32_t palette[] = {
            0xFF8800,
            0x00AAFF,
            0xC0FFEE,
        };
    """),
    cursor=(2, 7),
    hint="U uppercases whatever is selected. Select a block that starts just after the 0x and covers "
         "the digits on all three lines.",
    uses=["block-edit", "case"],
)
course.add(
    name="index-sequence", title="Count up the indexes", par=5, ext="java",
    task="Each line should read the next field: parts[0], parts[1], parts[2], parts[3].",
    start=text("""
        String[] parts = line.split(",");
        String name  = parts[0];
        String email = parts[0];
        String city  = parts[0];
        String zip   = parts[0];
    """),
    target=text("""
        String[] parts = line.split(",");
        String name  = parts[0];
        String email = parts[1];
        String city  = parts[2];
        String zip   = parts[3];
    """),
    cursor=(2, 1),
    hint="In Visual mode, g Ctrl-a adds 1 to the first number on the first selected line, 2 on the "
         "next, and so on. Leave the line that stays parts[0] out of the selection.",
    uses=["g-ctrl-a", "visual-line", "gg"],
)
course.add(
    name="change-column", title="Change a column", par=13, ext="java",
    task="Fields should be private. Change public to private on all three fields.",
    start=text("""
        class Point {
            public int x;
            public int y;
            public String label;
        }
    """),
    target=text("""
        class Point {
            private int x;
            private int y;
            private String label;
        }
    """),
    cursor=(2, 5),
    hint="Select the column of \"public\" as a block, then c deletes it and starts Insert mode. Type the "
         "new word once: <Esc> copies it to every line.",
    uses=["block-edit", "word"],
)
course.add(
    name="pipe-table", title="Make a pipe table", par=10, ext="txt",
    task="Turn this into a pipe table: put \"| \" in front of the second and third columns on every row.",
    start=text("""
        name   year typed
        C      1972 static
        Python 1991 dynamic
        Java   1995 static
    """),
    target=text("""
        name   | year | typed
        C      | 1972 | static
        Python | 1991 | dynamic
        Java   | 1995 | static
    """),
    hint="Block-insert \"| \" in front of the year column. Then move to the next column: . repeats a "
         "block insert at the cursor, on the same number of lines.",
    uses=["block-insert", "word", "gg", "dot"],
)
course.add(
    name="quote-words", title="Quote a list", par=13, ext="py",
    task="Turn the bare names into a list of strings: \"java\", \"c\" and so on, each followed by a comma.",
    start=text("""
        LANGS = [
            java
            c
            python
            rust
        ]
    """),
    target=text("""
        LANGS = [
            "java",
            "c",
            "python",
            "rust",
        ]
    """),
    cursor=(2, 5),
    hint="Add the opening quotes with a block I. Then gv selects the same block again, $ stretches it "
         "to each line's end, and A appends there.",
    uses=["block-insert", "visual-ends"],
)
course.add(
    name="center-title", title="Center a banner", par=9, ext="txt",
    task="Center the three title lines between the 30-character rules of = signs. Leave the last line alone.",
    start=text("""
        ==============================
        Project 04
        Visual and block mode
        rectangles and art
        ==============================

        Read the README first.
    """),
    target=text("""
        ==============================
                  Project 04
            Visual and block mode
              rectangles and art
        ==============================

        Read the README first.
    """),
    cursor=(3, 1),
    hint="Select the banner with a text object, then press :. Vim types '<,'> for you, so the Ex command "
         "only runs on the selected lines. The command you want is :center (see :help :center).",
    uses=["visual-ex", "center", "visual", "ip"],
)
course.add(
    name="box-edge", title="Close the box", par=9, ext="txt",
    task="Add the missing right side of the box: a | on each of the three middle lines, right under the "
         "+ corners. For this exercise virtualedit=block is set, so a block can reach past the end of a line.",
    start=text("""
        +------------------+
        | Project 04
        | Visual mode
        | Block mode
        +------------------+
    """),
    target=text("""
        +------------------+
        | Project 04       |
        | Visual mode      |
        | Block mode       |
        +------------------+
    """),
    cursor=(2, 1),
    setup=["setlocal virtualedit=block"],
    hint="Make a block over the three middle lines that reaches the column just left of the corners "
         "(N| jumps to column N). A appends after the block and pads short lines with spaces.",
    uses=["virtualedit", "block-insert"],
)
course.add(
    name="move-sun", title="Move the sun", par=14, ext="txt",
    task="Move the sun (the 3-line, 5-column block at the top left) so its left edge is in column 30, "
         "right of the cloud. The cloud must not move. virtualedit=all is set, like your :Art command.",
    start=text(r"""
        \ | /         .--.
        - O -      .-(    ).
        / | \     (___.__)__)

             /\
            /  \  /\
           /    \/  \
    """),
    # Written line by line: no line of the target starts in column 1, so text() would dedent it.
    target="\n".join([
        "              .--.           \\ | /",
        "           .-(    ).         - O -",
        "          (___.__)__)        / | \\",
        "",
        "     /\\",
        "    /  \\  /\\",
        "   /    \\/  \\",
    ]),
    setup=["setlocal virtualedit=all"],
    hint="d would pull the cloud left. Yank the sun as a block instead, then gv reselects it so r and a "
         "space can blank it out. 30| jumps to column 30, and P puts a block at the cursor.",
    uses=["block-edit", "visual-ends", "virtualedit"],
)

course.add(
    name="review-value-class", title="Review · Make a value class", par=114, ext="java",
    task="Point is about to become an immutable value class, and the review found a few bugs on the way. "
         "Apply it, top to bottom. This one reviews Projects 00 to 04: par uses only what they teach.",
    steps=[
        "Make the class final.",
        "Rename the class to GeoPoint everywhere: the class line, the constructor, scale(), and the text "
        "in toString().",
        "Make the three fields private final.",
        "The constructor assigns each parameter to itself: put this. in front of the three assignments.",
        "Java getters are camelCase: getX(), getY() and getZ().",
        "scale() forgot to scale z.",
        "toString() should print square brackets, GeoPoint[1.0, 2.0, 3.0], the way a record does.",
        "toString() overrides Object's: put @Override on the line above it.",
        "So does hashCode().",
        "hashCode() forgot z too.",
    ],
    start=text("""
        package geo;

        import java.util.Objects;

        public class Point {
            public double x;
            public double y;
            public double z;

            public Point(double x, double y, double z) {
                x = x;
                y = y;
                z = z;
            }

            public double get_x() { return x; }
            public double get_y() { return y; }
            public double get_z() { return z; }

            public Point scale(double k) {
                return new Point(x * k, y * k, z);
            }

            public String toString() {
                return "Point(" + x + ", " + y + ", " + z + ")";
            }

            public int hashCode() {
                return Objects.hash(x, y);
            }
        }
    """),
    target=text("""
        package geo;

        import java.util.Objects;

        public final class GeoPoint {
            private final double x;
            private final double y;
            private final double z;

            public GeoPoint(double x, double y, double z) {
                this.x = x;
                this.y = y;
                this.z = z;
            }

            public double getX() { return x; }
            public double getY() { return y; }
            public double getZ() { return z; }

            public GeoPoint scale(double k) {
                return new GeoPoint(x * k, y * k, z * k);
            }

            @Override
            public String toString() {
                return "GeoPoint[" + x + ", " + y + ", " + z + "]";
            }

            @Override
            public int hashCode() {
                return Objects.hash(x, y, z);
            }
        }
    """),
    hint="* finds the next Point as a whole word, and an insert in front of the word repeats with n and . "
         "everywhere else. The fields, the assignments and the getters line up, so each is one block: c, I, "
         "and d then gv. One O@Override, then . puts the second.",
    uses=["star", "dot", "block-edit", "block-insert", "visual-ends", "visual", "plus", "f", "o", "r"],
)
course.add(
    name="review-release-notes", title="Review · Lay out release notes", par=84, ext="txt",
    task="The release notes for tern 2.4 go out as a plain-text email, 60 columns wide. Lay them out. This "
         "one reviews Projects 00 to 04: par uses only what they teach.",
    steps=[
        "Center the title in 60 columns.",
        "Right-align the date, so it ends in column 60.",
        "Underline each of the three headings with = signs, exactly as long as the heading.",
        "Rewrap the What's new paragraph to the textwidth (60 for this one).",
        "Number the fixes 1 to 3.",
        "Indent the three fixes by two spaces.",
        "The second fix was in tern pull, not tern push.",
        "Uppercase the table's header row.",
        "Delete the tested column.",
        "Windows on arm64 is in beta too: add its row at the bottom.",
    ],
    start=text("""
        Release notes for tern 2.4
        May 2026

        What's new
        tern sync now resumes an interrupted upload instead of starting over, and it shows a progress bar while it works.

        Fixes
        0. tern init no longer overwrites an existing config
        0. tern push reports the right file count
        0. tern log --since accepts dates like 2026-05-01

        Platforms
        os        arch    status    tested
        Linux     x86_64  stable    yes
        Linux     arm64   stable    yes
        macOS     arm64   stable    yes
        Windows   x86_64  beta      no
    """),
    target=text("""
                         Release notes for tern 2.4
                                                            May 2026

        What's new
        ==========
        tern sync now resumes an interrupted upload instead of
        starting over, and it shows a progress bar while it works.

        Fixes
        =====
          1. tern init no longer overwrites an existing config
          2. tern pull reports the right file count
          3. tern log --since accepts dates like 2026-05-01

        Platforms
        =========
        OS        ARCH    STATUS
        Linux     x86_64  stable
        Linux     arm64   stable
        macOS     arm64   stable
        Windows   x86_64  beta
        Windows   arm64   beta
    """),
    setup=["setlocal textwidth=60"],
    hint=":ce and :ri take the width as a number. yyp then Vr= underlines a line with exactly as many = signs. "
         "A block over the 0s, then g Ctrl-a, numbers them, and gv gets that block back for I. The tested "
         "column is the right edge, so a block with $ deletes it.",
    uses=["center", "visual-line", "gq", "g-ctrl-a", "visual-ends", "block-insert", "replace-mode",
          "block-edit", "case", "y"],
)

course.run()
