"""Drills for Project 00: short problems that practice one command at a time.
Play them with:  python3 check.py drill      (the reference solutions are in ../solutions/drills/)"""
from trainer import Drills, text

drills = Drills(__file__)

# ---------- i a I A ----------

insert = drills.command(
    "insert", "i  a  I  A", "start typing: before, after, at the line's start or end",
    """i starts Insert mode just before the cursor and a just after it, so a is how you add to the end of
    a word. I starts at the line's first non-blank character (after the indentation, not in column 1) and
    A at the very end of the line. Type your text, then press <Esc> to go back to Normal mode: everything
    from i to <Esc> is one change, so u undoes it and . repeats it. With a count, the text is typed that
    many times when you press <Esc>: 3a-<Esc> adds ---.""",
    examples=[("ithe <Esc>", "type 'the ' before the cursor"), ("as<Esc>", "add an s after the cursor"),
              ("A;<Esc>", "add ; at the end of the line"), ("I// <Esc>", "type // before the first non-blank"),
              ("3a-<Esc>", "add three dashes")],
)
insert.add(
    title="Fill in a word", par=8, ext="txt", cursor=(1, 25),
    task='Add the missing word: the sentence should end "back to Normal mode." The cursor is on the m of '
         '"mode".',
    start="Press Esc to go back to mode.",
    target="Press Esc to go back to Normal mode.",
    hint='i inserts before the cursor, so type "Normal " (with the space) right where you are.',
)
insert.add(
    title="Make it plural", par=2, ext="sh", cursor=(1, 18),
    task='The folder is called node_modules. Add the missing s. The cursor is on the last letter of '
         '"node_module".',
    start="rm -rf node_module dist",
    target="rm -rf node_modules dist",
    hint="i would put the s before the e. a appends just after the cursor.",
)
insert.add(
    title="End the statement", par=2, ext="java",
    task="Add the missing semicolon at the end of the line.",
    start="int area = width * height",
    target="int area = width * height;",
    hint="A jumps to the end of the line and starts Insert mode there, all in one key.",
)
insert.add(
    title="Make it final", par=7, ext="java", cursor=(2, 15),
    task='Make MAX a constant: put "final " in front of "int", keeping the indentation. The cursor is on '
         "the 10.",
    start=text("""
        class Limits {
            int MAX = 10;
        }
    """),
    target=text("""
        class Limits {
            final int MAX = 10;
        }
    """),
    hint="I inserts before the first non-blank character of the line, so the indentation stays put.",
)
insert.add(
    title="Close the list", par=3, ext="py",
    task="The list never ends. Add a ] at the end of line 2.",
    start=text("""
        names = ["ada", "grace",
                 "linus"
        print(names)
    """),
    target=text("""
        names = ["ada", "grace",
                 "linus"]
        print(names)
    """),
    hint="Go down a line, then A appends at the end of it.",
)
insert.add(
    title="Compare, don't assign", par=4, ext="c",
    task="The condition assigns 0 to count instead of comparing. Make the = a ==.",
    start="if (count = 0) {",
    target="if (count == 0) {",
    hint="Jump onto the = with f, then a adds a character just after it.",
    uses=["f"],
)
insert.add(
    title="Return the result", par=9, ext="c",
    task="The function computes w * h but never returns it. Add \"return \" in front of it on line 2.",
    start=text("""
        int area(int w, int h) {
            w * h;
        }
    """),
    target=text("""
        int area(int w, int h) {
            return w * h;
        }
    """),
    hint="Go down a line. You don't need to find the w first: I starts typing before the first non-blank.",
)
insert.add(
    title="Quote a value", par=5, ext="toml", cursor=(2, 8),
    task="TOML strings need quotes: make the name \"Ada\". The cursor is on the A.",
    start=text("""
        [user]
        name = Ada
        email = "ada@example.com"
    """),
    target=text("""
        [user]
        name = "Ada"
        email = "ada@example.com"
    """),
    hint="Two small inserts: i for the quote before the cursor, then <Esc> and A for the one at the end.",
)
insert.add(
    title="Python 3 print", par=6, ext="py",
    task='Turn the Python 2 print statement into a call: print("Hello, world").',
    start='print "Hello, world"',
    target='print("Hello, world")',
    hint="The space after print should become a (: jump onto it with f and replace it with r. Then A adds "
         "the ) at the end.",
    uses=["f", "r"],
)
insert.add(
    title="Wrap it in print", par=10, ext="py", cursor=(2, 9),
    task="Print the sum instead of throwing it away: line 2 should be print(x + y), still indented. The "
         "cursor is on the y.",
    start=text("""
        def show(x, y):
            x + y
    """),
    target=text("""
        def show(x, y):
            print(x + y)
    """),
    hint="I types after the indentation, A at the end of the line. Use one for print( and the other for ).",
)
insert.add(
    title="Make the parents too", par=5, ext="sh",
    task="mkdir fails when build/ doesn't exist yet. Add the -p flag: mkdir -p build/output.",
    start="mkdir build/output",
    target="mkdir -p build/output",
    hint="Get to the start of the next word, then type the flag and its space in front of it.",
    uses=["word"],
)
insert.add(
    title="A heading, from the middle", par=4, ext="md", cursor=(1, 4),
    task='Make the line a level-two heading: "## Configuration". The cursor is on the f.',
    start="Configuration",
    target="## Configuration",
    hint="You don't need to go back to the start of the line first: one key starts typing there.",
)
insert.add(
    title="Pin the image", par=6, ext="yaml", cursor=(3, 5),
    task="Pin the web image to a version: it should be nginx:1.27. The cursor is on image.",
    start=text("""
        services:
          web:
            image: nginx
            ports:
              - "8080:80"
    """),
    target=text("""
        services:
          web:
            image: nginx:1.27
            ports:
              - "8080:80"
    """),
    hint="The tag goes at the very end of the line, wherever the cursor is on it.",
)
insert.add(
    title="Make it an f-string", par=4, ext="py",
    task='The braces print literally. Make the string an f-string: print(f"total: {total}").',
    start='print("total: {total}")',
    target='print(f"total: {total}")',
    hint="Jump to the opening quote with f, then type the f in front of it.",
    uses=["f"],
)
insert.add(
    title="Bold the warning", par=10, ext="md",
    task='Make "required" bold: This step is **required**.',
    start="This step is required.",
    target="This step is **required**.",
    hint="Two inserts: ** in front of the r (the first r on the line), then ** after the end of the word. "
         "e gets you there.",
    uses=["f"],
)
insert.add(
    title="Finish the printf", par=8, ext="c",
    task='End the output with a newline and the statement with a semicolon: printf("%d\\n", n);',
    start='printf("%d", n)',
    target='printf("%d\\n", n);',
    hint="The \\n goes right after the d, the first d on the line. The semicolon goes at the end: that's A's "
         "job.",
    uses=["f"],
)
insert.add(
    title="Comment out a rule", par=9, ext="css", cursor=(2, 5),
    task="CSS only has /* */ comments. Comment out the color line: /* color: red; */, keeping its "
         "indentation. The cursor is on color.",
    start=text("""
        .button {
            color: red;
            padding: 4px;
        }
    """),
    target=text("""
        .button {
            /* color: red; */
            padding: 4px;
        }
    """),
    hint="One insert after the indentation, one at the end of the line, with an <Esc> between them.",
)
insert.add(
    title="Run them as root", par=10, ext="sh",
    task='Both commands need root: put "sudo " in front of lines 2 and 3.',
    start=text("""
        #!/bin/sh
        apt-get update
        apt-get install -y git
    """),
    target=text("""
        #!/bin/sh
        sudo apt-get update
        sudo apt-get install -y git
    """),
    hint="Do line 2 with I, then let . repeat it on line 3. I, not i: . repeats the I too, so it types at "
         "the start of the line wherever the cursor is.",
    uses=["dot"],
)
insert.add(
    title="Top of the box", par=7, ext="txt",
    task="The box's top border is just a +. Make it +----------+ (ten dashes), like the bottom one.",
    start=text("""
        +
        |  menu    |
        +----------+
    """),
    target=text("""
        +----------+
        |  menu    |
        +----------+
    """),
    hint="A count on a, then one more append for the corner.",
    uses=["count"],
)
insert.add(
    title="Make it a link", par=22, ext="html",
    task='Turn the menu item into a link: <li><a href="/">Home</a></li>.',
    start="<li>Home</li>",
    target='<li><a href="/">Home</a></li>',
    hint='Type the opening tag in front of Home with i. After <Esc> the cursor is on the >, and e jumps to the '
         "end of Home, where a adds the closing tag.",
    uses=["f", "word"],
)


# ---------- o O ----------

o = drills.command(
    "o", "o  O", "open a new line below or above",
    """o opens a new line below the cursor's line and O opens one above it, and both start Insert mode on
    it, wherever the cursor was on the line. The new line is indented for you to match the code around
    it: in C and Java it's one level deeper after a line ending in {, and in Python after a line ending in
    a colon. In C, Java and shell files, o or O on a comment line starts the new line with the comment
    marker (// or #) already typed. With a count, 3o types your text on three new lines when you press
    <Esc>.""",
    examples=[("ofoo<Esc>", "new line below, type foo"), ("Ofoo<Esc>", "new line above, type foo"),
              ("o<Esc>", "add a blank line below"), ("3o-<Esc>", "three new lines of -")],
)
o.add(
    title="Add an item", par=8, ext="md", cursor=(4, 1),
    task='Add "- bread" to the end of the list. The cursor is on milk.',
    start=text("""
        # Groceries

        - eggs
        - milk
    """),
    target=text("""
        # Groceries

        - eggs
        - milk
        - bread
    """),
    hint="o opens a new line below the cursor's line and puts you in Insert mode on it.",
)
o.add(
    title="Annotate the method", par=10, ext="java", cursor=(2, 5),
    task="Add an @Override line above the method, indented like it. The cursor is on the method's first "
         "line.",
    start=text("""
        class Dog extends Animal {
            public String sound() {
                return "Woof";
            }
        }
    """),
    target=text("""
        class Dog extends Animal {
            @Override
            public String sound() {
                return "Woof";
            }
        }
    """),
    hint="O opens a line above the cursor's line, and Neovim indents it for you.",
)
o.add(
    title="Open the body", par=10, ext="c",
    task="Give main a body: add the line \"return 0;\" between the braces.",
    start=text("""
        int main(void) {
        }
    """),
    target=text("""
        int main(void) {
            return 0;
        }
    """),
    hint="o on the first line. The new line comes already indented, because the line above ends in {.",
)
o.add(
    title="After the colon", par=13, ext="py",
    task="Write the body of square: \"return n * n\", indented under the def.",
    start="def square(n):",
    target=text("""
        def square(n):
            return n * n
    """),
    hint="o opens the line below. After a line ending in a colon, Python's indent rules add the 4 spaces "
         "for you.",
)
o.add(
    title="Above the return", par=13, ext="py", cursor=(2, 5),
    task='Add the line "assert items" just before the return, indented like it. The cursor is on the '
         "return.",
    start=text("""
        def total(items):
            return sum(items)
    """),
    target=text("""
        def total(items):
            assert items
            return sum(items)
    """),
    hint="The cursor is already on the return line, so open a line above it with O.",
)
o.add(
    title="Continue the comment", par=20, ext="c",
    task='Add a second comment line below the first one: "// s must not be NULL."',
    start=text("""
        // Returns the length of s.
        int length(const char *s);
    """),
    target=text("""
        // Returns the length of s.
        // s must not be NULL.
        int length(const char *s);
    """),
    hint="In a C file, o on a comment line types the // for you. Just type the words.",
)
o.add(
    title="Three empty rows", par=13, ext="txt",
    task="Give the box three rows of |        | (8 spaces between the bars) between its top and bottom.",
    start=text("""
        +--------+
        +--------+
    """),
    target=text("""
        +--------+
        |        |
        |        |
        |        |
        +--------+
    """),
    hint="Type the row once after o and let a count do the rest: 3o repeats the line when you press <Esc>.",
    uses=["count"],
)
o.add(
    title="A shebang line", par=12, ext="sh", cursor=(3, 1),
    task="Make the script start with the line #!/bin/sh, above everything else. The cursor is on the last "
         "line.",
    start=text("""
        set -e
        make clean
        make all
    """),
    target=text("""
        #!/bin/sh
        set -e
        make clean
        make all
    """),
    hint="gg goes to the first line, and O opens a line above it.",
    uses=["gg"],
)
o.add(
    title="Before and after", par=20, ext="c", cursor=(2, 5),
    task='Add the line "init();" above run(); and the line "return 0;" below it. The cursor is on run.',
    start=text("""
        int main(void) {
            run();
        }
    """),
    target=text("""
        int main(void) {
            init();
            run();
            return 0;
        }
    """),
    hint="O for the line above, <Esc>, then j and o for the line below the run() call.",
)
o.add(
    title="Raise the roof", par=10, ext="txt",
    task="Put a roof on the house: add the two lines \" /\\\" and \"/  \\\" above it.",
    start=text("""
        |  |
        |__|
    """),
    target=text("""
         /\\
        /  \\
        |  |
        |__|
    """),
    hint="Build it bottom-up: O for the lower roof line, <Esc>, then O again for the peak above it. (If "
         "you press <CR> instead, the new line copies the space in front of the peak.)",
)
o.add(
    title="Room under the heading", par=1, ext="md",
    task="Add a blank line between the heading and the paragraph.",
    start=text("""
        # Changelog
        All notable changes are listed here.
    """),
    target=text("""
        # Changelog

        All notable changes are listed here.
    """),
    hint="The blank line goes below the cursor's line. Opening a line is already the whole change.",
)
o.add(
    title="Stop on errors", par=7, ext="sh",
    task='Add the line "set -e" right below the shebang line.',
    start=text("""
        #!/bin/bash
        echo "deploying"
        ./deploy.sh
    """),
    target=text("""
        #!/bin/bash
        set -e
        echo "deploying"
        ./deploy.sh
    """),
    hint="The cursor is on the shebang line, so open a line below it.",
)
o.add(
    title="No fall-through", par=7, ext="js", cursor=(3, 9),
    task='The "stop" case falls through into "go". Add a break; below halt();. The cursor is on halt.',
    start=text("""
        switch (cmd) {
            case "stop":
                halt();
            case "go":
                run();
        }
    """),
    target=text("""
        switch (cmd) {
            case "stop":
                halt();
                break;
            case "go":
                run();
        }
    """),
    hint="o opens the new line with the same indentation as halt();, so you only type the statement.",
)
o.add(
    title="The missing brace", par=2, ext="java", cursor=(3, 9),
    task="run() never ends. Add its closing brace on a line of its own, indented like void run(). The "
         "cursor is on go.",
    start=text("""
        class Main {
            void run() {
                go();
        }
    """),
    target=text("""
        class Main {
            void run() {
                go();
            }
        }
    """),
    hint="o starts the line at go()'s indentation, but Java's indent rules move a } you type back a level.",
)
o.add(
    title="One more branch", par=6, ext="yaml", cursor=(4, 9),
    task="Run the workflow on pushes to dev too: add a \"- dev\" item below \"- main\". The cursor is on "
         "main.",
    start=text("""
        on:
          push:
            branches:
              - main
    """),
    target=text("""
        on:
          push:
            branches:
              - main
              - dev
    """),
    hint="The new line keeps the indentation of the line you open it from.",
)
o.add(
    title="Or else", par=14, ext="py", cursor=(2, 5),
    task="Add an else branch that calls retry(): an else: line under the if, and retry() indented under it. "
         "The cursor is on send.",
    start=text("""
        if ok:
            send()
    """),
    target=text("""
        if ok:
            send()
        else:
            retry()
    """),
    hint="Open a line below send() and type else: there. Python's indent rules move else back out to the "
         "if's level as you type it, and Enter after the colon indents the next line.",
)
o.add(
    title="Three empty boxes", par=8, ext="md",
    task='Add three empty checkboxes under the heading, "- [ ]" on each line.',
    start="## Todo",
    target=text("""
        ## Todo
        - [ ]
        - [ ]
        - [ ]
    """),
    hint="Type one checkbox and let a count make the other two when you press <Esc>.",
    uses=["count"],
)
o.add(
    title="A body for reset", par=15, ext="c",
    task="Give the function a body in this file's style, braces on their own lines: {, then count = 0; "
         "indented, then }.",
    start="void reset(void)",
    target=text("""
        void reset(void)
        {
            count = 0;
        }
    """),
    hint="One o and three lines typed with Enter between them. After the { the next line is indented for "
         "you, and a } you type moves back out by itself.",
)
o.add(
    title="Space the statements", par=4, ext="sql",
    task="Put a blank line after each of the first two statements.",
    start=text("""
        CREATE TABLE users (id INT);
        CREATE TABLE posts (id INT);
        CREATE TABLE tags (id INT);
    """),
    target=text("""
        CREATE TABLE users (id INT);

        CREATE TABLE posts (id INT);

        CREATE TABLE tags (id INT);
    """),
    hint="o<Esc> adds a blank line, and leaves the cursor on it. Go down to the next statement and repeat "
         "the change.",
    uses=["dot"],
)
o.add(
    title="Two fields", par=12, ext="c",
    task="Give the struct two fields, int x; and int y;, each on its own line.",
    start=text("""
        struct point {
        };
    """),
    target=text("""
        struct point {
            int x;
            int y;
        };
    """),
    hint="The two lines differ by one letter. A count on o types the line twice; then fix the letter on the "
         "second one.",
    uses=["count", "r"],
)


# ---------- x X ----------

x = drills.command(
    "x", "x  X", "delete a character",
    """x deletes the character under the cursor, and X deletes the one just before it. A count deletes
    that many: 5x deletes five characters going right (or up to the end of the line, if there are fewer),
    and 3X deletes three going left. Neither one ever joins lines. The deleted text is saved like any
    delete, so p can put it back: xp swaps the character under the cursor with the next one.""",
    examples=[("x", "delete the character under the cursor"), ("X", "delete the character before the cursor"),
              ("5x", "delete five characters"), ("3X", "delete three characters to the left"),
              ("xp", "swap two characters")],
)
x.add(
    title="A doubled letter", par=3, ext="txt",
    task='Fix the spelling: "Tuesdday" should be "Tuesday".',
    start="The meeting is on Tuesdday at 10.",
    target="The meeting is on Tuesday at 10.",
    hint="Jump onto either d with fd, then x deletes the character under the cursor.",
    uses=["f"],
)
x.add(
    title="Space before the colon", par=2, ext="py",
    task="Remove the space before the colon.",
    start="def area(w, h) :",
    target="def area(w, h):",
    hint="$ jumps to the colon at the end of the line. X deletes the character just before the cursor.",
    uses=["line"],
)
x.add(
    title="Too excited", par=4, ext="py",
    task='Leave just one exclamation mark: print("Done!").',
    start='print("Done!!!!")',
    target='print("Done!")',
    hint="Jump to the first ! with f!, then give x a count: 3x deletes three characters.",
    uses=["f", "count"],
)
x.add(
    title="Not equal", par=4, ext="c",
    task="The operator is backwards: =! should be !=.",
    start="if (a =! b) {",
    target="if (a != b) {",
    hint="Two characters in the wrong order: put the cursor on the first one, delete it with x, and put it "
         "back after its neighbor with p.",
    uses=["f", "p"],
)
x.add(
    title="Digits only", par=5, ext="py",
    task='Remove both dashes so the number reads "5558675309".',
    start='phone = "555-867-5309"',
    target='phone = "5558675309"',
    hint="f- and x delete the first dash. Then ; repeats the jump to the next dash.",
    uses=["f", "semicolon"],
)
x.add(
    title="Drop the suffix", par=3, ext="py",
    task='Remove "-beta" from the version string.',
    start='version = "1.4.2-beta"',
    target='version = "1.4.2"',
    hint="From the closing quote ($ gets you there), X with a count deletes that many characters to the left.",
    uses=["line", "count"],
)
x.add(
    title="Square up the box", par=5, ext="txt",
    task="Line 3 sticks out. Remove three spaces so its right edge lines up with the others.",
    start=text("""
        +--------+
        | Save   |
        | Load      |
        | Quit   |
        +--------+
    """),
    target=text("""
        +--------+
        | Save   |
        | Load   |
        | Quit   |
        +--------+
    """),
    hint="Go down two lines and jump to the end with $. 3X deletes the three spaces before the |.",
    uses=["line", "count"],
)
x.add(
    title="Uncomment two lines", par=5, ext="java",
    task="Someone commented out the two log calls with // in the first column. Remove the // from both lines.",
    start=text("""
        void save() {
        //    log("saving");
        //    log(path);
            write(path);
        }
    """),
    target=text("""
        void save() {
            log("saving");
            log(path);
            write(path);
        }
    """),
    hint="2x deletes both slashes. j goes down a line in the same column, and . repeats the 2x.",
    uses=["count", "dot"],
)
x.add(
    title="Unwrap the condition", par=4, ext="py",
    task="Python doesn't need the parentheses here. Remove both of them.",
    start="if (count > 0):",
    target="if count > 0:",
    hint="w jumps onto the ( (punctuation counts as a word). After x, $ goes to the colon, and X deletes the ) "
         "before it.",
    uses=["word", "line"],
)
x.add(
    title="Inside the quotes", par=3, ext="txt",
    task="Move the period inside the closing quote.",
    start='She said "see you tomorrow".',
    target='She said "see you tomorrow."',
    hint="x deletes the period and leaves the cursor on the quote. P puts the period back before the cursor.",
    uses=["line", "p"],
)
x.add(
    title="No dollar on the left", par=1, ext="sh",
    task="In shell you don't write $ when you assign to a variable. Remove it.",
    start=text("""
        $NAME="ada"
        echo "hi, $NAME"
    """),
    target=text("""
        NAME="ada"
        echo "hi, $NAME"
    """),
    hint="The cursor is already on the $.",
)
x.add(
    title="Trailing comma", par=3, ext="json", cursor=(3, 3),
    task="JSON doesn't allow a comma after the last item. Remove the one on line 3. The cursor is on its "
         "first quote.",
    start=text("""
        {
          "name": "app",
          "version": "1.0.0",
        }
    """),
    target=text("""
        {
          "name": "app",
          "version": "1.0.0"
        }
    """),
    hint="There's only one comma on the line: find it, then delete the character under the cursor.",
    uses=["f"],
)
x.add(
    title="Drop the v", par=3, ext="yaml",
    task="The version should be a bare number: version: 1.2.0.",
    start="version: v1.2.0",
    target="version: 1.2.0",
    hint="fv looks for the next v after the cursor, so it skips the one you're on.",
    uses=["f"],
)
x.add(
    title="Short hex", par=4, ext="css",
    task="Use the short form of white: color: #fff;.",
    start="color: #ffffff;",
    target="color: #fff;",
    hint="Land on the first f of the color, then delete three characters in one go.",
    uses=["f", "count"],
)
x.add(
    title="Swap a typo", par=4, ext="js",
    task='Fix the keyword: "fucntion" should be "function".',
    start="fucntion add(a, b) {",
    target="function add(a, b) {",
    hint="Two letters in the wrong order: cut the first one and put it back after its neighbor.",
    uses=["f", "p"],
)
x.add(
    title="Hug the brackets", par=6, ext="py",
    task="Remove the spaces just inside the brackets: nums = [1, 2, 3].",
    start="nums = [ 1, 2, 3 ]",
    target="nums = [1, 2, 3]",
    hint="X deletes the character before the cursor, so land on the 1 and on the ], not on the spaces.",
    uses=["f"],
)
x.add(
    title="Sticky keys", par=5, ext="txt",
    task='Fix the commit message: "Add a unit test."',
    start="Addd a unit testt.",
    target="Add a unit test.",
    hint="Any of the d's can go, and one is right next to the cursor. For the t, the period is easier to "
         "find than the letter: delete the character before it.",
    uses=["f"],
)
x.add(
    title="Not done after all", par=6, ext="md",
    task="Remove the strikethrough: both pairs of ~~ around the item.",
    start="- ~~Write the tests~~",
    target="- Write the tests",
    hint="2x deletes a pair. ; finds the next ~, and . deletes another pair.",
    uses=["f", "count", "semicolon", "dot"],
)
x.add(
    title="Python 2 strings", par=7, ext="py",
    task='Remove the u prefixes, Python 3 doesn\'t need them: names = ["ada", "bob", "cy"].',
    start='names = [u"ada", u"bob", u"cy"]',
    target='names = ["ada", "bob", "cy"]',
    hint="The first u on the line is a prefix. Delete it, then ; and . for the others.",
    uses=["f", "semicolon", "dot"],
)
x.add(
    title="Numbers, not strings", par=11, ext="json", cursor=(2, 3),
    task='Take the quotes off both values: "port": 8080 and "debug": true. The cursor is on line 2\'s '
         "first quote.",
    start=text("""
        {
          "port": "8080",
          "debug": "true"
        }
    """),
    target=text("""
        {
          "port": 8080,
          "debug": true
        }
    """),
    hint='Get to the quote before 8080 with a counted f". After x, ; repeats the f" to the next quote. It '
         "still works after you move to line 3, and , goes the other way.",
    uses=["f", "count", "semicolon"],
)


# ---------- r ----------

r = drills.command(
    "r", "r{c}", "replace one character",
    """r followed by a character replaces the character under the cursor with it, and leaves you in Normal
    mode, so there's no <Esc> to press. With a count, 3r- replaces three characters with three dashes (if
    fewer than three are left on the line, nothing happens), and the cursor ends on the last one. r<CR>
    replaces the character with a line break, splitting the line. Like Enter in Insert mode, it indents
    the new line and drops any spaces that would start it, and 5r<CR> replaces five characters with a
    single line break.""",
    examples=[("rx", "replace the character with x"), ("r+", "turn a - into a +"), ("3r-", "replace three characters with ---"),
              ("f;r,", "make the next ; a comma"), ("r<CR>", "split the line here")],
)
r.add(
    title="Check the box", par=4, ext="md",
    task="Mark the task as done: put an x between the brackets.",
    start="- [ ] Write the tests",
    target="- [x] Write the tests",
    hint="The space between the brackets is three characters to the right: 3l gets there. Then r replaces it.",
    uses=["count"],
)
r.add(
    title="Wrong separator", par=4, ext="csv",
    task="One field is separated with a semicolon. Make it a comma like the rest.",
    start="id,name;email,city",
    target="id,name,email,city",
    hint="f; finds the semicolon, and r, replaces it with a comma.",
    uses=["f"],
)
r.add(
    title="Fill the gap", par=5, ext="txt",
    task="The box's top border has a gap. Replace the three spaces with dashes.",
    start=text("""
        +--   --+
        |  OK   |
        +-------+
    """),
    target=text("""
        +-------+
        |  OK   |
        +-------+
    """),
    hint="f followed by a space lands on the first space. A count on r replaces that many characters: 3r-.",
    uses=["f", "count"],
)
r.add(
    title="Or, not and", par=5, ext="java",
    task="The check should pass for admins or owners: change && to ||.",
    start="if (isAdmin && isOwner) {",
    target="if (isAdmin || isOwner) {",
    hint="Jump to the first & with f&, then replace two characters at once with 2r|.",
    uses=["f", "count"],
)
r.add(
    title="Mask the card number", par=6, ext="py",
    task="Replace the first twelve digits with * so only the last four show.",
    start='card = "4111222233334444"',
    target='card = "************4444"',
    hint="f4 finds the first digit. With a count, r replaces that many characters: 12r*.",
    uses=["f", "count"],
)
r.add(
    title="Slashes to dashes", par=6, ext="py",
    task='Write the date with dashes: "2026-10-29".',
    start='date = "2026/10/29"',
    target='date = "2026-10-29"',
    hint="Fix the first slash with f/ and r-. Then ; jumps to the next slash and . repeats the r-.",
    uses=["f", "semicolon", "dot"],
)
r.add(
    title="Star eyes", par=7, ext="txt",
    task="Give the face star eyes: both o's on line 2 become *.",
    start=text(r"""
         .-------.
         | o   o |
         |   ^   |
         | \___/ |
         '-------'
    """),
    target=text(r"""
         .-------.
         | *   * |
         |   ^   |
         | \___/ |
         '-------'
    """),
    hint="Go down to line 2, find the first o with fo and replace it with r*. Then ; finds the next o and . "
         "repeats the r*.",
    uses=["f", "semicolon", "dot"],
)
r.add(
    title="One item per line", par=5, ext="txt",
    task="Put each item on its own line, without the commas.",
    start="milk, eggs, bread",
    target=text("""
        milk
        eggs
        bread
    """),
    hint="w jumps onto the comma (punctuation is a word of its own). r<CR> replaces it with a line break, and "
         "the space after it disappears by itself. Then w and . do the second comma.",
    uses=["word", "dot"],
)
r.add(
    title="One statement per line", par=7, ext="py",
    task="Split the three statements onto lines of their own, without the semicolons.",
    start=text("""
        def reset(self):
            self.x = 0; self.y = 0; self.z = 0
    """),
    target=text("""
        def reset(self):
            self.x = 0
            self.y = 0
            self.z = 0
    """),
    hint="On line 2, f; finds a semicolon and r<CR> turns it into a line break. The new line is indented to "
         "match. Then ; and . do the next one.",
    uses=["f", "semicolon", "dot"],
)
r.add(
    title="Progress bar", par=9, ext="txt",
    task="Update the progress bar to 80%: eight # and two dots, and the number 80.",
    start="[#####.....] 50%",
    target="[########..] 80%",
    hint="f. finds the first dot, and 3r# turns three dots into #. Then f5 and r8 fix the number.",
    uses=["f", "count"],
)
r.add(
    title="Executable for the owner", par=3, ext="sh",
    task="Let the owner run the script: change the mode from 644 to 744.",
    start="chmod 644 deploy.sh",
    target="chmod 744 deploy.sh",
    hint="Only the first digit changes. Get to the next word, then replace one character.",
    uses=["word"],
)
r.add(
    title="Letter O, digit 0", par=4, ext="java",
    task="Someone typed a capital O instead of a zero: the limit should be 10.",
    start="int limit = 1O;",
    target="int limit = 10;",
    hint="f is case-sensitive, so fO finds the capital O. Then replace it.",
    uses=["f"],
)
r.add(
    title="Follow the pointer", par=4, ext="c",
    task="C uses -> to reach through a pointer: make it node = node->next;.",
    start="node = node=>next;",
    target="node = node->next;",
    hint="f= would stop on the first =, the assignment. t> stops just before the >, on the = you want.",
    uses=["t"],
)
r.add(
    title="A bigger heading", par=4, ext="md",
    task="Make Install a top-level heading: underline it with = instead of -.",
    start=text("""
        Install
        -------
    """),
    target=text("""
        Install
        =======
    """),
    hint="Go down, then a count on r replaces the whole run of dashes at once.",
    uses=["count"],
)
r.add(
    title="Not the same", par=4, ext="js",
    task="The test is backwards: === should be !==.",
    start="if (a === b) {",
    target="if (a !== b) {",
    hint="Only the first = changes. Land on it, then replace it.",
    uses=["f"],
)
r.add(
    title="Number the steps", par=6, ext="md",
    task="Number the steps 1, 2 and 3.",
    start=text("""
        1. Clone the repo
        1. Build it
        1. Run the tests
    """),
    target=text("""
        1. Clone the repo
        2. Build it
        3. Run the tests
    """),
    hint="j keeps the column, so after each r you're right above the next number.",
)
r.add(
    title="SQL strings", par=6, ext="sql",
    task="SQL strings take single quotes: make it name = 'ada'.",
    start="SELECT * FROM users WHERE name = \"ada\";",
    target="SELECT * FROM users WHERE name = 'ada';",
    hint="Fix the first quote with f and r. ; finds the second one, and . repeats the r.",
    uses=["f", "semicolon", "dot"],
)
r.add(
    title="One command per line", par=5, ext="sh",
    task='Split the line in two: "make" on line 1 and "make test" on line 2, without the &&.',
    start="make && make test",
    target=text("""
        make
        make test
    """),
    hint='r<CR> replaces with a line break, and with a count it replaces that many characters with a single '
         'one. " && " is four characters.',
    uses=["f", "count"],
)
r.add(
    title="Bump the version", par=8, ext="toml",
    task="Release the next minor version: 1.4.9 becomes 1.5.0.",
    start='version = "1.4.9"',
    target='version = "1.5.0"',
    hint="Two digits change. Fix the 4, then move two characters right to the 9.",
    uses=["f"],
)
r.add(
    title="Star corners", par=10, ext="txt",
    task="Make all four corners of the box * instead of +.",
    start=text("""
        +----+
        |    |
        +----+
    """),
    target=text("""
        *----*
        |    |
        *----*
    """),
    hint="r* on the first corner, then f+ and . for the next. 2j keeps the column, and , repeats the f+ "
         "backward.",
    uses=["f", "semicolon", "dot", "count"],
)


# ---------- w b e ----------

word = drills.command(
    "word", "w  b  e", "move by words",
    """w moves to the start of the next word, b back to the start of this word or the previous one, and e
    to the end of this word or the next one. A word is a run of letters, digits and underscores, or a run
    of other non-blank characters, so w stops at punctuation: user.name is three words. After an
    operator, w and b leave out the character they land on and e includes it: dw deletes a word and the
    space after it, de leaves the space, and cw is a special case: like ce, it stops at the end of the
    word. dw on the last word of a line stops at the end of the line, while w on its own goes on to the
    next line.""",
    examples=[("w", "next word"), ("3b", "back three words"), ("e", "end of the word"),
              ("dw", "delete a word and the space after it"), ("de", "delete to the end of the word"),
              ("cw", "change to the end of the word (like ce)")],
)
word.add(
    title="Lowercase the name", par=3, ext="java",
    task="Java variables start with a lowercase letter: make Name name.",
    start='String Name = "Ada";',
    target='String name = "Ada";',
    hint="w hops to the start of the next word. Then replace one character.",
    uses=["r"],
)
word.add(
    title="Capitalize a heading", par=3, ext="md", cursor=(1, 15),
    task='Capitalize the heading: "Installation". The cursor is on the last letter.',
    start="## installation",
    target="## Installation",
    hint="b goes back to the start of the word the cursor is in.",
    uses=["r"],
)
word.add(
    title="The right package", par=3, ext="py", cursor=(1, 8),
    task="The package is called pandas. Add the missing s. The cursor is on the p.",
    start="import panda as pd",
    target="import pandas as pd",
    hint="e jumps to the end of the word, and a appends after the cursor.",
    uses=["insert"],
)
word.add(
    title="Say it once", par=3, ext="txt",
    task='Delete the doubled "the".',
    start="Press the the Esc key to leave Insert mode.",
    target="Press the Esc key to leave Insert mode.",
    hint="Move to the next word, then dw deletes a word together with the space after it.",
    uses=["d"],
)
word.add(
    title="Rename a variable", par=6, ext="c",
    task="Rename total_count to sum.",
    start="int total_count = 0;",
    target="int sum = 0;",
    hint="Underscores are part of a word, so total_count is one word. cw changes it and keeps the space "
         "after it.",
    uses=["c"],
)
word.add(
    title="Trim the name", par=2, ext="py", cursor=(1, 8),
    task="Rename timeout_from_config to timeout. The cursor is on the first underscore.",
    start='timeout_from_config = load("timeout")',
    target='timeout = load("timeout")',
    hint="de deletes to the end of the word and leaves the space. dw would take the space too.",
    uses=["d"],
)
word.add(
    title="Stop at the dot", par=10, ext="java", cursor=(1, 14),
    task="Read the email from account instead of currentUser. The cursor is on the =.",
    start="String email = currentUser.email;",
    target="String email = account.email;",
    hint="w lands on currentUser. A word ends at punctuation, so cw changes only up to the dot.",
    uses=["c"],
)
word.add(
    title="Lower the log level", par=6, ext="py", cursor=(1, 14),
    task="Log at the info level instead of debug. The cursor is on the (.",
    start='logging.debug("saved %s", name)',
    target='logging.info("saved %s", name)',
    hint="Backward motions leave out the character the cursor starts on. So cb changes back to the start "
         "of debug and keeps the (.",
    uses=["c"],
)
word.add(
    title="Fewer words", par=7, ext="txt", cursor=(1, 11),
    task='Replace "a huge number of" with "many". The cursor is on the a.',
    start="There are a huge number of bugs.",
    target="There are many bugs.",
    hint="Counts work on motions: c4w changes four words, and like cw it stops at the end of the last one.",
    uses=["c", "count"],
)
word.add(
    title="Swap two words", par=4, ext="java",
    task='Java style puts public before final. Swap them: "public final void run()".',
    start="final public void run() {",
    target="public final void run() {",
    hint="dw cuts final and its space. Then move to the next word and put it in front with P.",
    uses=["d", "p"],
)
word.add(
    title="Subtract instead", par=4, ext="c",
    task="diff should be a - b, not a + b.",
    start="int diff = a + b;",
    target="int diff = a - b;",
    hint="The + is a word of its own, four words along. A count on w gets there.",
    uses=["count", "r"],
)
word.add(
    title="Not async", par=4, ext="ts",
    task='load doesn\'t await anything. Remove "async ".',
    start="export default async function load() {",
    target="export default function load() {",
    hint="async is two words along. dw deletes it with the space after it.",
    uses=["count", "d"],
)
word.add(
    title="A pointer", par=3, ext="c",
    task="name should be a pointer: char *name = \"ada\";.",
    start='char name = "ada";',
    target='char *name = "ada";',
    hint="The * goes right in front of name, which is the next word.",
    uses=["insert"],
)
word.add(
    title="Rename from the end", par=10, ext="js", cursor=(1, 19),
    task="Rename maxRetryCount to retries. The cursor is on its last letter.",
    start="const maxRetryCount = 5;",
    target="const retries = 5;",
    hint="camelCase is still one word. b goes back to its start, and cw changes it.",
    uses=["c"],
)
word.add(
    title="Drop the label", par=4, ext="py",
    task='Remove "TODO(ada): " from the comment, so it reads "# retries are capped at 5".',
    start="# TODO(ada): retries are capped at 5",
    target="# retries are capped at 5",
    hint="Go to TODO. The punctuation runs ( and ): are words too, so the label is four words, and a count "
         "on dw deletes them and the space after them.",
    uses=["count", "d"],
)
word.add(
    title="Say it shorter", par=10, ext="md", cursor=(1, 45),
    task='Replace "you open a pull request" with "pushing": "Run the tests before pushing." The cursor is on '
         "the period.",
    start="Run the tests before you open a pull request.",
    target="Run the tests before pushing.",
    hint="c works with b, and a backward motion leaves out the character under the cursor, so the period "
         "survives. Count the words you want gone.",
    uses=["count", "c"],
)
word.add(
    title="Fewer steps", par=9, ext="py", cursor=(1, 16),
    task="Call fetch() on self directly: self.table.rows() becomes self.fetch(). The cursor is on the first "
         "dot.",
    start="for row in self.table.rows():",
    target="for row in self.fetch():",
    hint="table, the dot and rows are three words. c3w changes them and stops before the (.",
    uses=["count", "c"],
)
word.add(
    title="Short names", par=10, ext="java",
    task="Rename width to w and height to h.",
    start="int width = 0, height = 0;",
    target="int w = 0, h = 0;",
    hint="cw for the first name. From there, height is four words along: =, 0 and the comma are words too.",
    uses=["c", "count"],
)
word.add(
    title="No type annotations", par=8, ext="ts",
    task="Strip the three \": number\" annotations: function add(a, b) {.",
    start="function add(a: number, b: number): number {",
    target="function add(a, b) {",
    hint='From a colon, de deletes the colon, the space and number: the colon is a word on its own, so e '
         "goes on to the end of the next one. ; and . do the other two.",
    uses=["f", "d", "semicolon", "dot"],
)
word.add(
    title="A private field", par=22, ext="java",
    task="Make the constant an ordinary private field in camelCase: private int maxSize = 10;.",
    start="public static final int MAX_SIZE = 10;",
    target="private int maxSize = 10;",
    hint="c3w replaces the first three words in one change. Then two words along, cw renames MAX_SIZE "
         "(underscores are part of a word).",
    uses=["c", "count"],
)


# ---------- f F ----------

f = drills.command(
    "f", "f{c}  F{c}", "find a character on the line",
    """f followed by any character jumps forward to the next place that character appears on the current
    line, and puts the cursor on it. F does the same backward. They never leave the line (use / to search
    the whole file), and they start looking just past the cursor, so fv from a v finds the next v. A
    count finds the Nth one. Used after an operator, f includes the character it lands on (dfx deletes
    through the x), while F stops just short of where the cursor was.""",
    examples=[("fv", "next v"), ("3f,", "third comma"), ("F(", "back to the ("), ("dfx", "delete through the next x"),
              ("cf)", "change through the next )"), ("dF/", "delete back to the last /")],
)
f.add(
    title="Multiply instead", par=4, ext="py",
    task="The area should be width times height. Change the + to a *.",
    start="area = width + height",
    target="area = width * height",
    hint="f+ puts the cursor on the +, and r* replaces that one character.",
)
f.add(
    title="One bracket too many", par=3, ext="c",
    task="Delete one of the two closing parentheses.",
    start='printf("%d\\n", count));',
    target='printf("%d\\n", count);',
    hint="Jump onto a ) with f), then delete the character under the cursor.",
    uses=["x"],
)
f.add(
    title="A missing letter", par=4, ext="txt",
    task='Fix the spelling: "belive" should be "believe".',
    start="I can't belive it worked the first time.",
    target="I can't believe it worked the first time.",
    hint="The missing e goes just before the v, and there's only one v on the line. i inserts before the cursor.",
    uses=["insert"],
)
f.add(
    title="Make it wink", par=6, ext="txt",
    task="Turn the right eye (the second o on line 2) into a -.",
    start=text("""
        +-----+
        | o o |
        |  ^  |
        | --- |
        +-----+
    """),
    target=text("""
        +-----+
        | o - |
        |  ^  |
        | --- |
        +-----+
    """),
    hint="Go down a line first. A count in front of f finds the Nth match: 2fo is the second o.",
    uses=["count", "r"],
)
f.add(
    title="Double plus", par=4, ext="c", cursor=(1, 28),
    task="The loop should count with i++. Fix the increment. The cursor starts at the end of the line.",
    start="for (int i = 0; i < n; i+) {",
    target="for (int i = 0; i < n; i++) {",
    hint="F searches backward: F+ lands on the lonely +. Then append another one after it.",
    uses=["insert"],
)
f.add(
    title="Back to the folder", par=3, ext="py", cursor=(1, 34),
    task="Drop the file name so the path points at the folder: delete /python3.12. The cursor is on the "
         "closing quote.",
    start='path = "/usr/local/bin/python3.12"',
    target='path = "/usr/local/bin"',
    hint="d works with F. A backward motion leaves out the character the cursor started on, so the quote "
         "survives.",
    uses=["d"],
)
f.add(
    title="Skip a lookup", par=5, ext="java",
    task='Read the host straight from config: remove .get("db").',
    start='String host = config.get("db").get("host");',
    target='String host = config.get("host");',
    hint="Jump to the first dot, then delete through the first ) with df).",
    uses=["d"],
)
f.add(
    title="Change a call", par=11, ext="java",
    task="Replace Math.max(left, right) with Math.abs(x).",
    start="double d = Math.max(left, right) * scale;",
    target="double d = Math.abs(x) * scale;",
    hint='The first lowercase m on the line is the start of "max" (f is case-sensitive). From there, cf) '
         "changes everything through the closing parenthesis.",
    uses=["c"],
)
f.add(
    title="Drop a column", par=6, ext="csv",
    task="Remove the birthdate column from this CSV header, along with one of its commas.",
    start="id,name,email,birthdate,city",
    target="id,name,email,city",
    hint="Land on the comma just after birthdate with a counted f, then delete back to the previous comma "
         "with dF,.",
    uses=["count", "d"],
)
f.add(
    title="Same greeting", par=9, ext="java",
    task='Give farewell the same value as greeting: line 2 should end with = "Hi";.',
    start=text("""
        String greeting = "Hi";
        String farewell;
    """),
    target=text("""
        String greeting = "Hi";
        String farewell = "Hi";
    """),
    hint='Get onto the space before = (it\'s the second space on the line), then yank through the second " '
         "with y2f\". Go down to the ; and put the text in front of it with P.",
    uses=["count", "y", "p"],
)
f.add(
    title="Skip two", par=4, ext="py",
    task="tail should skip the first two items: items[2:].",
    start="tail = items[1:]",
    target="tail = items[2:]",
    hint="There's only one 1 on the line. Jump onto it and replace it.",
    uses=["r"],
)
f.add(
    title="Trim the PATH", par=3, ext="sh", cursor=(1, 33),
    task='Remove ":/opt/old/bin" from the end of the line. The cursor is on the last letter.',
    start="export PATH=/usr/bin:/opt/old/bin",
    target="export PATH=/usr/bin",
    hint="F searches backward for the colon. Then delete from there to the end of the line.",
    uses=["d"],
)
f.add(
    title="Misspelled document", par=4, ext="js",
    task='Fix the typo: "documnet" should be "document".',
    start="const root = documnet.body;",
    target="const root = document.body;",
    hint="const has an n too, so aim for the e instead: the first e on the line. The n just before it is "
         "the letter to move.",
    uses=["x", "p"],
)
f.add(
    title="Drop a query parameter", par=5, ext="js",
    task='Remove "per_page=50&" from the URL.',
    start='const url = "/search?q=vim&per_page=50&sort=new";',
    target='const url = "/search?q=vim&sort=new";',
    hint="The first p on the line starts per_page. From there, df& deletes through the next &.",
    uses=["d"],
)
f.add(
    title="Backward to the word", par=9, ext="java", cursor=(1, 27),
    task='Print "Saved" instead of "Done". The cursor is at the end of the line.',
    start='System.out.println("Done");',
    target='System.out.println("Saved");',
    hint="F goes backward: FD lands on the D. Then cw changes the word, up to the quote.",
    uses=["c"],
)
f.add(
    title="A lighter image", par=8, ext="html",
    task="Use the WebP version of the logo: logo.webp.",
    start='<img src="logo.png" alt="Logo">',
    target='<img src="logo.webp" alt="Logo">',
    hint="The first p on the line is the start of png. cw changes it and stops at the quote.",
    uses=["c"],
)
f.add(
    title="Crop to the same size", par=7, ext="py",
    task="Pass the same size to crop: line 2 should be crop(img, (640, 480)).",
    start=text("""
        resize(img, (640, 480))
        crop(img)
    """),
    target=text("""
        resize(img, (640, 480))
        crop(img, (640, 480))
    """),
    hint="From the comma, yf) copies through the first ), the end of the tuple. Line 2 is shorter, so j "
         "lands on its last character, the ). P puts the copy before it.",
    uses=["y", "p"],
)
f.add(
    title="No casts", par=8, ext="c",
    task="Remove both casts: int n = a + b;.",
    start="int n = (long)a + (unsigned)b;",
    target="int n = a + b;",
    hint="df) deletes a whole cast, however long, and . repeats it. But df) is an f of its own, so ; "
         "would look for another ), not a (.",
    uses=["d", "semicolon", "dot"],
)
f.add(
    title="Attribute access", par=9, ext="py",
    task='The row is an object now, not a dict: print(row.name).',
    start='print(row["name"])',
    target="print(row.name)",
    hint='Turn the [ into a dot and delete the quote after it. "] is a word of its own, so the next word '
         "is the rest to delete.",
    uses=["r", "x", "word", "count"],
)
f.add(
    title="Quote the value", par=9, ext="sql",
    task="ada is a string: make it 'ada'.",
    start="INSERT INTO users (id, name) VALUES (1, ada);",
    target="INSERT INTO users (id, name) VALUES (1, 'ada');",
    hint="The first lowercase a is in name, so a count gets you to ada. After the first quote, e reaches the "
         "end of the word.",
    uses=["count", "insert", "word"],
)


# ---------- t T ----------

t = drills.command(
    "t", "t{c}  T{c}", "move till a character",
    """t followed by a character moves forward to just before the next place that character appears on
    the line, and T moves backward to just after it. They're f and F stopping one short: t stops before,
    f lands on. That makes them ideal after an operator: dt) deletes up to the ) and keeps it, and ct"
    changes everything up to a closing quote. Like F, a backward T never includes the character the
    cursor started on. A count finds the Nth match: 2t, stops before the second comma.""",
    examples=[("t,", "just before the next comma"), ("T(", "just after the previous ("),
              ("dt)", "delete up to the )"), ('ct"', "change up to the next quote"),
              ("yt,", "copy up to the comma"), ("d2t,", "delete up to the second comma")],
)
t.add(
    title="Point the progress bar", par=4, ext="txt",
    task="Turn the last = of the bar into a >, so the bar ends in an arrow.",
    start="[==========-----] 66%",
    target="[=========>-----] 66%",
    hint="The last = is just before the first -, which is exactly where t- stops. Then replace it with r.",
    uses=["r"],
)
t.add(
    title="Just the path", par=3, ext="py", cursor=(1, 15),
    task="Drop the extra arguments so the call is just open(path). The cursor is on the comma after path.",
    start=text("""
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
    """),
    target=text("""
        with open(path) as f:
            data = f.read()
    """),
    hint="dt) deletes everything up to the closing parenthesis and leaves the parenthesis itself.",
    uses=["d"],
)
t.add(
    title="Read from args", par=12, ext="py", cursor=(1, 12),
    task='Take the port from args instead: replace os.environ["PORT"] with args.port. The cursor is on os.',
    start='port = int(os.environ["PORT"]) + 1',
    target="port = int(args.port) + 1",
    hint="ct) changes everything up to the ), so the closing parenthesis of int(...) survives.",
    uses=["c"],
)
t.add(
    title="A shorter message", par=12, ext="java", cursor=(1, 75),
    task='Replace the message with "Disk full". The cursor is on the closing quote.',
    start='throw new IOException("Something went wrong, please try again in a minute.");',
    target='throw new IOException("Disk full");',
    hint="T searches backward and stops just after the opening quote. cT\" changes from there up to the "
         "cursor, and leaves the quote under the cursor alone.",
    uses=["c"],
)
t.add(
    title="Same prefix, new key", par=5, ext="py",
    task="Line 2 should set config.database.port, like line 1 sets config.database.host.",
    start=text("""
        config.database.host = "localhost"
        port = 5432
    """),
    target=text("""
        config.database.host = "localhost"
        config.database.port = 5432
    """),
    hint="Copy everything before host with yt and the first letter of host. Then go down and put it in "
         "front of port with P.",
    uses=["y", "p"],
)
t.add(
    title="Keep the slash", par=3, ext="c", cursor=(1, 44),
    task="Point LOG_PATH at the folder: delete access.log, but keep the slash before it. The cursor is on "
         "the closing quote.",
    start='#define LOG_PATH "/var/log/nginx/access.log"',
    target='#define LOG_PATH "/var/log/nginx/"',
    hint="dT/ deletes back to just after the last /. (dF/ would delete the slash too.)",
    uses=["d"],
)
t.add(
    title="Drop two columns", par=8, ext="csv", cursor=(1, 4),
    task="Remove the name and city columns from every row. The cursor is on the first comma.",
    start=text("""
        key,name,city,email
        ada,Ada Lovelace,London,ada@example.com
        gmh,Grace Hopper,New York,grace@example.com
    """),
    target=text("""
        key,email
        ada,ada@example.com
        gmh,grace@example.com
    """),
    hint="d2t, deletes up to just before the second comma after the cursor. j moves straight down to the "
         "next row's first comma, and . repeats the whole d2t,.",
    uses=["count", "d", "dot"],
)
t.add(
    title="Strip the file names", par=7, ext="log", cursor=(1, 6),
    task="Remove the file names, so each line starts with \"DEBUG:\". The cursor is on the first space.",
    start=text("""
        DEBUG main.c: started
        DEBUG net/socket.c: connected
        DEBUG ui.c: ready
    """),
    target=text("""
        DEBUG: started
        DEBUG: connected
        DEBUG: ready
    """),
    hint="dt: deletes up to the colon however long the file name is, so j. repeats it on the next line.",
    uses=["d", "dot"],
)
t.add(
    title="A new greeting", par=7, ext="txt",
    task='Reuse the email for Ada: change "Dr. Grace Hopper" to "Ada".',
    start="Hi Dr. Grace Hopper, thanks for the talk.",
    target="Hi Ada, thanks for the talk.",
    hint="w gets you to Dr. Then ct, changes everything up to the comma.",
    uses=["word", "c"],
)
t.add(
    title="Change the password", par=12, ext="env",
    task="Change the password in the URL (between admin: and @) to hunter2.",
    start="DATABASE_URL=postgres://admin:p4ss-w0rd!@localhost:5432/app",
    target="DATABASE_URL=postgres://admin:hunter2@localhost:5432/app",
    hint="There's only one @ on the line, so f@ gets you to the end of the password. From there cT: "
         "changes back to just after the colon.",
    uses=["f", "c"],
)
t.add(
    title="Production settings", par=9, ext="json",
    task='Change the environment to "prod".',
    start='"env": "staging-eu-1",',
    target='"env": "prod",',
    hint="The first s on the line starts the value. ct\" changes everything up to the closing quote, dashes "
         "and all.",
    uses=["f", "c"],
)
t.add(
    title="Drop the separator", par=5, ext="py",
    task='join should take just items: remove the sep parameter and its comma.',
    start='def join(items, sep=", "):',
    target="def join(items):",
    hint="Start on the comma after items. dt) deletes everything up to the ), whatever is in the way.",
    uses=["f", "d"],
)
t.add(
    title="Right-align the columns", par=6, ext="md", cursor=(2, 1),
    task="Right-align both columns: the separator row should be |-----:|-----:|. The cursor is at the start "
         "of the row.",
    start=text("""
        | Item | Cost |
        |------|------|
        | Tea  |    3 |
    """),
    target=text("""
        | Item | Cost |
        |-----:|-----:|
        | Tea  |    3 |
    """),
    hint="t| lands on the last dash of a column. After an r, ; skips the | right next to the cursor and "
         "stops before the following one.",
    uses=["r", "semicolon", "dot"],
)
t.add(
    title="Just the file name", par=3, ext="c", cursor=(1, 25),
    task='Include config.h directly: #include "config.h". The cursor is on the c of config.',
    start='#include "../../include/config.h"',
    target='#include "config.h"',
    hint="dT\" deletes back to just after the opening quote, and keeps the character under the cursor.",
    uses=["d"],
)
t.add(
    title="Call a helper", par=11, ext="py",
    task="Use the helper instead: value = lookup(key).",
    start="value = self.cache.get(key)",
    target="value = lookup(key)",
    hint="ct( changes everything up to the (, dots and all.",
    uses=["f", "c"],
)
t.add(
    title="Plain text, no link", par=7, ext="md",
    task="Keep the words but drop the link: See the guide for details.",
    start="See [the guide](https://example.com/guide) for details.",
    target="See the guide for details.",
    hint="Delete the [ first. Then from the ], dt and a space deletes the rest of the link, up to the space "
         "before for.",
    uses=["word", "x", "f", "d"],
)
t.add(
    title="Same compose file", par=5, ext="sh",
    task="Line 2 should run logs with the same compose file: docker compose -f docker-compose.prod.yml logs.",
    start=text("""
        docker compose -f docker-compose.prod.yml up -d
        logs
    """),
    target=text("""
        docker compose -f docker-compose.prod.yml up -d
        docker compose -f docker-compose.prod.yml logs
    """),
    hint="The first u on line 1 is the one in up, so ytu copies everything before it, the space included. "
         "Then put it in front of logs.",
    uses=["y", "p"],
)
t.add(
    title="No annotations", par=9, ext="py",
    task="Remove the type annotations: x = 0, y = 0.5 and z = [].",
    start=text("""
        x: int = 0
        y: float = 0.5
        z: list[int] = []
    """),
    target=text("""
        x = 0
        y = 0.5
        z = []
    """),
    hint="From a colon, the type ends just before the second space, so d2t and a space deletes it, however "
         "long it is. That's why . works on the other lines.",
    uses=["f", "d", "count", "dot"],
)
t.add(
    title="Log, don't print", par=15, ext="java", cursor=(2, 5),
    task="Use the logger: both System.out.println calls become log.info. The cursor is on the first "
         "System.",
    start=text("""
        void run() {
            System.out.println("start");
            work();
            System.out.println("done");
        }
    """),
    target=text("""
        void run() {
            log.info("start");
            work();
            log.info("done");
        }
    """),
    hint="ct( changes the whole dotted name up to the (. Then get to the second System and press . : "
         "2j and FS work, but counting words is shorter, since (\" and \"); are words too.",
    uses=["c", "count", "word", "dot"],
)
t.add(
    title="Reset the state", par=16, ext="js", cursor=(2, 3),
    task="Set all three values to null. The cursor is on user.",
    start=text("""
        const state = {
          user: currentUser,
          token: session.token,
          theme: prefs.theme,
        };
    """),
    target=text("""
        const state = {
          user: null,
          token: null,
          theme: null,
        };
    """),
    hint="ct, changes a value up to its comma, whatever its length, so . works on every line. After j, b "
         "gets you back to the start of the value.",
    uses=["word", "c", "dot"],
)


# ---------- ; , ----------

semicolon = drills.command(
    "semicolon", ";  ,", "repeat the last f, t, F or T",
    """; repeats your last f, t, F or T in the same direction, and , repeats it in the opposite
    direction: after F( (backward), ; keeps going backward and , goes forward. After a t, ; skips to
    just before the next match instead of staying stuck in front of the one it already found. They work
    after an operator too (after f., d; deletes through the next period), and with . they make a rhythm:
    ; to the next place, . to make the same change there.""",
    examples=[(";", "next match, same direction"), (",", "next match, the other way"),
              ("f,;;", "the third comma"), ("d;", "delete to the next match"),
              (";.", "go to the next one and repeat the change")],
)
semicolon.add(
    title="Fix the time", par=6, ext="toml",
    task="Times use colons: make the alarm 07:30:00.",
    start='alarm = "07-30-00"',
    target='alarm = "07:30:00"',
    hint="Fix the first dash with f- and r:. Then ; jumps to the next dash and . repeats the r:.",
    uses=["f", "r", "dot"],
)
semicolon.add(
    title="Minus, minus", par=6, ext="c", cursor=(1, 30),
    task="Change the last two + signs to -, so it prints a + b - c - d. The cursor is at the end of the line.",
    start='printf("%d\\n", a + b + c + d);',
    target='printf("%d\\n", a + b - c - d);',
    hint="F+ finds the last + going backward. After an F, ; keeps going backward.",
    uses=["f", "r", "dot"],
)
semicolon.add(
    title="Back with a comma", par=6, ext="sh", cursor=(1, 12),
    task="Use underscores in the file name: report_2024_final.pdf. The cursor is on the 0 of 2024.",
    start="cp report-2024-final.pdf backup/",
    target="cp report_2024_final.pdf backup/",
    hint="Fix the dash after 2024 with f- and r_. Then , repeats the f- the other way, back to the dash "
         "before 2024, and . repeats the r_.",
    uses=["f", "r", "dot"],
)
semicolon.add(
    title="Zero the first three", par=8, ext="c",
    task="Set the first three pins to 0 and leave the last one alone: {0, 0, 0, 9}.",
    start="int pins[] = {3, 7, 5, 9};",
    target="int pins[] = {0, 0, 0, 9};",
    hint="t, stops on the number before the first comma. After r0, the cursor is still right before that "
         "comma, and ; is smart enough to skip it and go to the next one.",
    uses=["t", "r", "dot"],
)
semicolon.add(
    title="Drop a sentence", par=5, ext="txt",
    task="Delete the middle sentence, so the text reads \"Neovim is a text editor. You can extend it with "
         "Lua.\"",
    start="Neovim is a text editor. It was forked from Vim in 2014. You can extend it with Lua.",
    target="Neovim is a text editor. You can extend it with Lua.",
    hint="f. finds the end of the first sentence. Step onto the space after it, then d; deletes through "
         "the next period: ; works as the motion for an operator.",
    uses=["f", "d"],
)
semicolon.add(
    title="Tidy the commas", par=7, ext="java",
    task="Remove the space before each comma: {1, 2, 3, 4}.",
    start="int[] values = {1 , 2 , 3 , 4};",
    target="int[] values = {1, 2, 3, 4};",
    hint="t, stops on the space before a comma, and x deletes it. Then ; and . for the next ones.",
    uses=["t", "x", "dot"],
)
semicolon.add(
    title="Add type hints", par=14, ext="py",
    task="All three parameters are ints: make the line def area(w: int, h: int, d: int):.",
    start=text("""
        def area(w, h, d):
            return w * h * d
    """),
    target=text("""
        def area(w: int, h: int, d: int):
            return w * h * d
    """),
    hint="t, lands on w, and a types \": int\" after it. ; skips the comma right after the cursor and "
         "finds the next one, and . types \": int\" again. The last parameter ends at ), not a comma.",
    uses=["t", "insert", "dot"],
)
semicolon.add(
    title="Space the operators", par=11, ext="c",
    task="Put a space on both sides of every +: a + b + c + d.",
    start="int total = a+b+c+d;",
    target="int total = a + b + c + d;",
    hint="f+ and then s replaces the + with \" + \". After <Esc>, ; finds the next + and . repeats the s.",
    uses=["f", "c", "dot"],
)
semicolon.add(
    title="CSV to table", par=16, ext="md", cursor=(3, 1),
    task="Turn line 3 into a Markdown table row like the header: | Ada | Lovelace | 1815 |. The cursor is "
         "on line 3.",
    start=text("""
        | First | Last | Born |
        |-------|------|------|
        Ada,Lovelace,1815
    """),
    target=text("""
        | First | Last | Born |
        |-------|------|------|
        | Ada | Lovelace | 1815 |
    """),
    hint="I and A add the outer bars. For the commas, f, then s turns one into \" | \", and ; . does the "
         "next.",
    uses=["insert", "f", "c", "dot"],
)
semicolon.add(
    title="Slashes to dots", par=8, ext="py", cursor=(1, 19),
    task="Write the path as a module name: src.app.models.user. The cursor is on models.",
    start='module = "src/app/models/user"',
    target='module = "src.app.models.user"',
    hint="Start with F/ and r., then ; keeps going left. When the left side is done, , turns around and "
         "finds the slash after models.",
    uses=["f", "r", "dot"],
)
semicolon.add(
    title="No code spans", par=9, ext="md",
    task="Remove all four backticks: Run make, then make test.",
    start="Run `make`, then `make test`.",
    target="Run make, then make test.",
    hint="Find the first backtick and delete it. Then ; jumps to the next one and . deletes it again.",
    uses=["f", "x", "dot"],
)
semicolon.add(
    title="Colons in the time", par=7, ext="txt",
    task="The time part should use colons: 2026-01-05T10:30:00.",
    start="2026-01-05T10-30-00",
    target="2026-01-05T10:30:00",
    hint="The first dash to change is the third dash on the line. Fix it, then ; and . for the last one.",
    uses=["f", "count", "r", "dot"],
)
semicolon.add(
    title="Escape the dots", par=7, ext="py", cursor=(1, 23),
    task='In a regex an unescaped dot matches anything. Escape both: "www\\.example\\.com". The cursor is on '
         "the first w.",
    start='pattern = re.compile("www.example.com")',
    target='pattern = re.compile("www\\.example\\.com")',
    hint="t. stops just before a dot, and a\\ adds the backslash there. After a t, ; skips the dot right "
         "next to the cursor and stops before the next one.",
    uses=["t", "insert", "dot"],
)
semicolon.add(
    title="JSON wants double quotes", par=10, ext="json",
    task="Make it valid JSON: {\"name\": \"ada\"}.",
    start="{'name': 'ada'}",
    target='{"name": "ada"}',
    hint="Four quotes, one change each: f' and r\" for the first, then ; . three times.",
    uses=["f", "r", "dot"],
)
semicolon.add(
    title="First two fields", par=4, ext="csv",
    task="Keep only the first two fields, the date and the email.",
    start="2026-01-05,ada@example.com,login,ok,203",
    target="2026-01-05,ada@example.com",
    hint="f, finds the first comma and ; the second. From there, D deletes to the end of the line.",
    uses=["f", "d"],
)
semicolon.add(
    title="Drop the middle name", par=5, ext="py",
    task='Remove "bob" from the list: ["ada", "cy"].',
    start='names = ["ada", "bob", "cy"]',
    target='names = ["ada", "cy"]',
    hint='From the space after the first comma, d; deletes through the next comma: ; is a motion like any '
         "other.",
    uses=["f", "d"],
)
semicolon.add(
    title="Markdown, not text", par=11, ext="sh",
    task="Copy the Markdown files instead: cp a.md b.md c.md dest/.",
    start="cp a.txt b.txt c.txt dest/",
    target="cp a.md b.md c.md dest/",
    hint="ft lands on the first txt, and cw changes it. ; finds the next t, which is the start of the next "
         "txt, and . repeats the change.",
    uses=["f", "c", "dot"],
)
semicolon.add(
    title="Decimal points", par=7, ext="txt",
    task="Use decimal points instead of commas: 3.50 and 0.35.",
    start=text("""
        price: 3,50
        tax: 0,35
    """),
    target=text("""
        price: 3.50
        tax: 0.35
    """),
    hint="j keeps the column when it can, and here it lands past the comma on line 2. ; would look further "
         "right, so , turns around.",
    uses=["f", "r", "dot"],
)
semicolon.add(
    title="Escape the inner quotes", par=8, ext="py",
    task='Escape the quotes around hi: msg = "say \\"hi\\" now".',
    start='msg = "say "hi" now"',
    target='msg = "say \\"hi\\" now"',
    hint="Do the later quote first. Then , searches backward for the earlier one, and the backslash you "
         "typed isn't in the way.",
    uses=["f", "count", "insert", "dot"],
)
semicolon.add(
    title="Windows path", par=11, ext="java",
    task='Java needs doubled backslashes: "C:\\\\Users\\\\ada\\\\Documents\\\\notes.txt".',
    start='String path = "C:\\Users\\ada\\Documents\\notes.txt";',
    target='String path = "C:\\\\Users\\\\ada\\\\Documents\\\\notes.txt";',
    hint="f\\ and a\\ double the first one and leave the cursor on the new one, past the old one, so ; "
         "finds the next backslash, not the same one again.",
    uses=["f", "insert", "dot"],
)


# ---------- counts ----------

count = drills.command(
    "count", "{N}", "counts: do it N times",
    """Type a number before a command to do it that many times: 3w moves three words, 5x deletes five
    characters, 4dd deletes four lines, and 4J joins four lines into one. On an operator the count can go
    before it or before the motion: 3dw and d3w both delete three words (and 2d3w deletes six). On an
    insert, the text you type is repeated when you press <Esc>: 10i-<Esc> types ten dashes. With
    relativenumber on, the number beside each line is the count to use with j or k.""",
    examples=[("3w", "three words forward"), ("5x", "delete five characters"), ("d3w", "delete three words"),
              ("4dd", "delete four lines"), ("10i-<Esc>", "type ten dashes"), ("2f,", "the second comma")],
)
count.add(
    title="Calm down", par=2, ext="py", cursor=(1, 13),
    task="One exclamation mark is enough. The cursor is on the second one.",
    start='print("Done!!!!")',
    target='print("Done!")',
    hint="x deletes the character under the cursor, and 3x deletes three.",
    uses=["x"],
)
count.add(
    title="Five lines down", par=4, ext="c",
    task="Add the missing semicolon on line 6.",
    start=text("""
        int main(void) {
            int width = 8;
            int height = 5;
            int area = width * height;
            int perimeter = 2 * (width + height);
            printf("area: %d\\n", area)
            printf("perimeter: %d\\n", perimeter);
            return 0;
        }
    """),
    target=text("""
        int main(void) {
            int width = 8;
            int height = 5;
            int area = width * height;
            int perimeter = 2 * (width + height);
            printf("area: %d\\n", area);
            printf("perimeter: %d\\n", perimeter);
            return 0;
        }
    """),
    hint="With relative line numbers, the number next to line 6 is how far down it is: use it as a count "
         "on j. Then A.",
    uses=["insert"],
)
count.add(
    title="Fill the bar", par=7, ext="txt",
    task="Fill the progress bar with ten # signs: [##########].",
    start="Progress: [] 100%",
    target="Progress: [##########] 100%",
    hint="Get onto the [ with f, then a count on an insert types the text that many times: 10a#<Esc>.",
    uses=["f", "insert"],
)
count.add(
    title="Three words at once", par=3, ext="sh", cursor=(1, 8),
    task="Only tmp needs removing: delete build, dist and logs. The cursor is on build.",
    start="rm -rf build dist logs tmp",
    target="rm -rf tmp",
    hint="d3w deletes three words, spaces included. 3dw is the same thing.",
    uses=["d", "word"],
)
count.add(
    title="Delete four lines", par=3, ext="py", cursor=(2, 1),
    task="Remove the four print lines. The cursor is on the first one.",
    start=text("""
        def total(prices):
            print("start")
            print(prices)
            print(len(prices))
            print("summing")
            return sum(prices)
    """),
    target=text("""
        def total(prices):
            return sum(prices)
    """),
    hint="dd deletes a line, and a count in front deletes that many.",
    uses=["dd"],
)
count.add(
    title="One long line", par=2, ext="txt",
    task="Join the four lines into a single line.",
    start=text("""
        Neovim is a fork of Vim
        that focuses on extensibility
        and usability. It adds Lua
        and a built-in terminal.
    """),
    target="Neovim is a fork of Vim that focuses on extensibility and usability. It adds Lua and a built-in "
           "terminal.",
    hint="J joins two lines. With a count, it joins that many lines.",
    uses=["join"],
)
count.add(
    title="Build the wall", par=5, ext="txt",
    task="Make the wall three courses high: lines 1 and 2, three times over.",
    start=text("""
        _|___|___|___
        ___|___|___|_
    """),
    target=text("""
        _|___|___|___
        ___|___|___|_
        _|___|___|___
        ___|___|___|_
        _|___|___|___
        ___|___|___|_
    """),
    hint="yj copies both lines. Go to the second line, then a count on p puts them that many times.",
    uses=["y", "p"],
)
count.add(
    title="The second i", par=5, ext="txt",
    task='Fix the spelling: "reciept" should be "receipt".',
    start="I received your reciept.",
    target="I received your receipt.",
    hint='The i to swap is the second lowercase i on the line (the first is in "received"). 2fi finds it, '
         "and xp swaps it with the e after it.",
    uses=["f", "x", "p"],
)
count.add(
    title="Indent three lines", par=3, ext="py", cursor=(2, 1),
    task="Indent the three lines of the function body. The cursor is on the first one.",
    start=text("""
        def greet(name):
        message = "Hi, " + name
        print(message)
        return message
    """),
    target=text("""
        def greet(name):
            message = "Hi, " + name
            print(message)
            return message
    """),
    hint=">> indents one line, and a count in front indents that many.",
    uses=["indent"],
)
count.add(
    title="Four zeros", par=8, ext="c",
    task="Spell out all four zeros: {0, 0, 0, 0}.",
    start="int a[4] = {0};",
    target="int a[4] = {0, 0, 0, 0};",
    hint='Get onto the 0 with f. Then type ", 0" once with a count of 3 in front of a.',
    uses=["f", "insert"],
)
count.add(
    title="Delete from the bottom", par=3, ext="sh", cursor=(6, 1),
    task="Remove the whole if block, from if to fi. The cursor is on the fi.",
    start=text("""
        #!/bin/sh
        make
        if [ -n "$DEBUG" ]; then
            echo "debug build"
            ls -l build/
        fi
    """),
    target=text("""
        #!/bin/sh
        make
    """),
    hint="d with k deletes upward, whole lines. The relative line numbers show how far up the if is.",
    uses=["d", "dd"],
)
count.add(
    title="Close every call", par=4, ext="js",
    task="Close all three calls: foo(bar(baz(1))).",
    start="foo(bar(baz(1",
    target="foo(bar(baz(1)))",
    hint="A count works on A too: the text you append is typed that many times when you press <Esc>.",
    uses=["insert"],
)
count.add(
    title="Out of the loop", par=3, ext="py", cursor=(3, 1),
    task="The last five lines belong outside the loop: unindent them one level. The cursor is on the first "
         "of them.",
    start=text("""
        for item in items:
            check(item)
            total = sum(items)
            mean = total / len(items)
            print(total)
            print(mean)
            report(total, mean)
    """),
    target=text("""
        for item in items:
            check(item)
        total = sum(items)
        mean = total / len(items)
        print(total)
        print(mean)
        report(total, mean)
    """),
    hint="<< shifts a line left, and a count in front shifts that many lines, starting at the cursor.",
    uses=["indent"],
)
count.add(
    title="Eight digits", par=6, ext="py",
    task='Pad the order number with zeros to eight digits: "00000042".',
    start='order_id = "42"',
    target='order_id = "00000042"',
    hint="Six zeros go in front of the 4. A count on i types the 0 that many times.",
    uses=["f", "insert"],
)
count.add(
    title="The separator row", par=10, ext="md",
    task="Line 2 is empty. Make it the separator row for the table: |---|---|---|.",
    start=text("""
        | Name | Age | City |

        | Ada  | 36  | London |
    """),
    target=text("""
        | Name | Age | City |
        |---|---|---|
        | Ada  | 36  | London |
    """),
    hint="The row is |--- three times and then a closing |. Type the repeating part once with a count.",
    uses=["insert"],
)
count.add(
    title="Seventy percent", par=9, ext="txt",
    task="Fill the bar to 70%: seven # and then three dots, [#######...].",
    start="loading [] 70%",
    target="loading [#######...] 70%",
    hint="[] is a word of its own, so w gets you onto the [. Then two counted appends, one after the other. "
         "Each one's <Esc> is what types the copies.",
    uses=["word", "insert"],
)
count.add(
    title="Remove two users", par=8, ext="yaml",
    task="Remove ada's entry (2 lines) and cy's entry (3 lines).",
    start=text("""
        users:
          - name: ada
            role: admin
          - name: bob
            role: dev
          - name: cy
            role: dev
            shell: zsh
    """),
    target=text("""
        users:
          - name: bob
            role: dev
    """),
    hint="2dd deletes ada. Then on cy's first line, a count in front of . replaces the 2 with a new count.",
    uses=["dd", "dot"],
)
count.add(
    title="Two missing semicolons", par=7, ext="c",
    task="Lines 2 and 5 are missing their semicolons.",
    start=text("""
        int main(void) {
            int a = 1
            int b = 2;
            int c = 3;
            printf("%d\\n", a + b + c)
            return 0;
        }
    """),
    target=text("""
        int main(void) {
            int a = 1;
            int b = 2;
            int c = 3;
            printf("%d\\n", a + b + c);
            return 0;
        }
    """),
    hint="A; on line 2. The relative line numbers then show how far down line 5 is, and . repeats the A;.",
    uses=["insert", "dot"],
)
count.add(
    title="A grid of boxes", par=7, ext="txt",
    task="Make a 3 by 3 grid: three rows of [ ][ ][ ].",
    start="[ ]",
    target=text("""
        [ ][ ][ ]
        [ ][ ][ ]
        [ ][ ][ ]
    """),
    hint="Y copies the [ ], and a count on P puts it twice in front of the cursor. Then do the same with "
         "the whole row.",
    uses=["y", "p"],
)
count.add(
    title="Draw a box", par=19, ext="txt",
    task="Turn the + into a box eight characters wide inside: +--------+, then |        |, then "
         "+--------+.",
    start="+",
    target=text("""
        +--------+
        |        |
        +--------+
    """),
    hint="Counted appends draw each line in a few keys. The bottom border is a copy of the top one, and O "
         "opens the middle line above it.",
    uses=["insert", "y", "p", "o"],
)


# ---------- d D ----------

d = drills.command(
    "d", "d{motion}  D", "delete",
    """d is the delete operator: d followed by a motion deletes the text the motion moves over, and saves
    it so p can put it back. dw deletes to the start of the next word, so it takes the space after the
    word, while de stops at the end of the word and leaves the space. f, t and e include the character
    they land on: df) deletes the ), and dt), which lands just before the ), stops short of it. Backward
    motions (db, dF, dT, d0) never delete the character under the cursor. D is short for d$: delete to
    the end of the line. A count can go on either side: d3w and 3dw both delete three words.""",
    examples=[("dw", "delete to the next word"), ("de", "delete to the end of the word"), ("dt)", "delete up to the )"),
              ("df,", "delete through the comma"), ("D", "delete to the end of the line"),
              ("d0", "delete back to the start of the line")],
)
d.add(
    title="Said it twice", par=4, ext="txt",
    task='Delete one of the two "completely"s.',
    start="The update is completely completely free.",
    target="The update is completely free.",
    hint='Jump to the first "completely" with fc. dw deletes the word and the space after it.',
    uses=["f", "word"],
)
d.add(
    title="Drop the comment", par=3, ext="java",
    task='Delete the comment at the end of the line, so it ends with "return total;".',
    start="return total; // TODO: double-check rounding",
    target="return total;",
    hint="f/ jumps to the comment. D deletes from the cursor to the end of the line.",
    uses=["f"],
)
d.add(
    title="Drop the last parameter", par=4, ext="py",
    task="Remove the timeout_seconds parameter and its comma.",
    start="def fetch(url, timeout_seconds):",
    target="def fetch(url):",
    hint="Start on the comma (f,). From there, e goes to the end of the next word, so de deletes the comma, "
         "the space and the whole name.",
    uses=["f", "word"],
)
d.add(
    title="Skip a getter", par=5, ext="java",
    task="Call getName() on user directly: remove .getProfile().",
    start="String name = user.getProfile().getName();",
    target="String name = user.getName();",
    hint="Start on the first dot. dt. deletes up to, but not including, the next dot.",
    uses=["f", "t"],
)
d.add(
    title="Cut the aside", par=5, ext="txt",
    task='Remove ", which was moved twice," so the sentence reads "The meeting is now on Friday."',
    start="The meeting, which was moved twice, is now on Friday.",
    target="The meeting is now on Friday.",
    hint="Put the cursor on the first comma. df, deletes through the next comma, both commas included.",
    uses=["f"],
)
d.add(
    title="Two words back", par=3, ext="java", cursor=(1, 22),
    task='Make LIMIT an ordinary field: delete "static final ". The cursor starts on int.',
    start="private static final int LIMIT = 100;",
    target="private int LIMIT = 100;",
    hint="db deletes back to the start of the previous word, and d2b two words back. A backward delete leaves "
         "the cursor's own character alone, so int survives.",
    uses=["count", "word"],
)
d.add(
    title="Lose the prompt", par=2, ext="sh", cursor=(1, 21),
    task="You pasted a command along with the shell prompt in front of it. The cursor is on the m of make: "
         "delete everything before it.",
    start="rick@mbp ~/school $ make test",
    target="make test",
    hint="d0 deletes from the start of the line up to the cursor, and keeps the character under the cursor.",
    uses=["line"],
)
d.add(
    title="Shorten the chain", par=5, ext="py",
    task='Read the timeout straight from self: delete "config.settings.".',
    start="x = self.config.settings.timeout",
    target="x = self.timeout",
    hint='Dots are words too, so "config.settings." is four words. Jump to config with fc, then d4w.',
    uses=["f", "count", "word"],
)
d.add(
    title="Simplify the condition", par=4, ext="py",
    task='Delete " and not done" so the line reads "if count > 0:".',
    start="if count > 0 and not done:",
    target="if count > 0:",
    hint="From the colon at the end ($), dT0 deletes back to just after the 0. T is the backward version of t.",
    uses=["line", "t"],
)
d.add(
    title="Not static, no throws", par=7, ext="java",
    task='Remove "static " and "throws Exception " from the method header.',
    start="public static void run(String[] args) throws Exception {",
    target="public void run(String[] args) {",
    hint="w and then dw take care of static. Then from the { at the end ($), d2b deletes the two words before it.",
    uses=["word", "line", "count"],
)
d.add(
    title="Nothing to await", par=4, ext="js",
    task='parse isn\'t async. Remove "await ".',
    start="const data = await parse(text);",
    target="const data = parse(text);",
    hint="data has two a's, so count words instead: await is three words along. dw deletes it with its "
         "space.",
    uses=["word", "count"],
)
d.add(
    title="No verbose flag", par=3, ext="py", cursor=(1, 28),
    task="Remove the verbose parameter and its comma. The cursor is on the ).",
    start="def run(self, verbose=False):",
    target="def run(self):",
    hint="dF, deletes back through the comma, and a backward delete leaves the cursor's ) alone.",
    uses=["f"],
)
d.add(
    title="Say it plainly", par=5, ext="md",
    task='Remove "probably maybe ": We should use Neovim for this.',
    start="We should probably maybe use Neovim for this.",
    target="We should use Neovim for this.",
    hint="Two words in, two words to delete. A count works on w after d.",
    uses=["count", "word"],
)
d.add(
    title="Same tab", par=5, ext="html",
    task='Open the link in the same tab: remove target="_blank" and the space before it.',
    start='<a href="/docs" target="_blank">Docs</a>',
    target='<a href="/docs">Docs</a>',
    hint="The first t on the line starts target, so t followed by t stops on the space just before it. dt> "
         "deletes from there up to the >.",
    uses=["t"],
)
d.add(
    title="No comments", par=5, ext="toml",
    task="Remove the comments at the ends of both lines.",
    start=text("""
        port = 8080      # default
        host = "0.0.0.0" # all interfaces
    """),
    target=text("""
        port = 8080
        host = "0.0.0.0"
    """),
    hint="f# and D delete the first one. The comments start in the same column, so j and . do the second.",
    uses=["f", "dot"],
)
d.add(
    title="Drop the NULL check", par=5, ext="c",
    task="Simplify the condition to if (p->ok) {.",
    start="if (p != NULL && p->ok) {",
    target="if (p->ok) {",
    hint="From the first p, t looks for the next p, so dtp deletes everything up to the second one.",
    uses=["f", "t"],
)
d.add(
    title="Up to the next line", par=4, ext="c",
    task="Delete the comment at the end of line 1 and the whole comment line under it.",
    start=text("""
        int x = 5; // was 3 before
        // see the changelog
        int y = 6;
    """),
    target=text("""
        int x = 5;
        int y = 6;
    """),
    hint="D takes a count: 2D deletes to the end of this line and the whole next line.",
    uses=["f", "count"],
)
d.add(
    title="Two folders up", par=4, ext="sh", cursor=(1, 48),
    task="Go to the releases folder itself: delete /2026.01.05-1200/assets. The cursor is on the last "
         "letter.",
    start="cd /srv/app-v2.1/releases/2026.01.05-1200/assets",
    target="cd /srv/app-v2.1/releases",
    hint="A count on F goes back to the second slash, and D deletes from there to the end of the line.",
    uses=["f", "count"],
)
d.add(
    title="Blank the secrets", par=7, ext="sh",
    task='Empty both values, keeping the quotes: API_KEY="" and DB_PASS="".',
    start=text("""
        API_KEY="abc123"
        DB_PASS="hunter2!"
    """),
    target=text("""
        API_KEY=""
        DB_PASS=""
    """),
    hint="Get inside the first quotes (=\" is a word of its own), then dt\" deletes up to the closing one. The "
         "names are the same length, so j lands inside the second value, and . deletes it however long it is.",
    uses=["word", "count", "t", "dot"],
)
d.add(
    title="A plain method", par=15, ext="java",
    task="Simplify the header to public void run(String name, int n) {: remove static synchronized, both "
         "finals and the throws clause.",
    start="public static synchronized void run(final String name, final int n) throws IOException {",
    target="public void run(String name, int n) {",
    hint="d2w for static synchronized. f finds each final, and ; with . deletes the second one. Then count "
         "words to throws (the ) is one) and delete two.",
    uses=["word", "count", "f", "semicolon", "dot"],
)


# ---------- dd ----------

dd = drills.command(
    "dd", "dd", "delete whole lines",
    """dd deletes the whole line the cursor is on, wherever the cursor is on it, and 3dd deletes three lines
    starting there. d with a motion that moves up or down deletes whole lines too: dj deletes this line
    and the next, dk this line and the one above, dG everything to the end of the file. Deleted lines are
    saved as lines, so p puts them back as whole lines below the cursor's line and P above it: ddp swaps
    a line with the next one. After dd the cursor is on the line that took the deleted one's place, or
    the line above if you deleted the last line, so moving a line up is ddkP, but just ddP from the
    last line.""",
    examples=[("dd", "delete this line"), ("3dd", "delete three lines"), ("dj", "delete this line and the next"),
              ("dk", "delete this line and the one above"), ("dG", "delete to the end of the file"),
              ("ddp", "swap this line with the next")],
)
dd.add(
    title="Remove the debug line", par=3, ext="py",
    task="Delete the print line.",
    start=text("""
        def add(a, b):
            print("debug")
            return a + b
    """),
    target=text("""
        def add(a, b):
            return a + b
    """),
    hint="Go down a line with j, then dd deletes the whole line, wherever the cursor is on it.",
)
dd.add(
    title="Three stale comments", par=4, ext="sh",
    task="Delete the three comment lines under the first line.",
    start=text("""
        #!/bin/sh
        # old build steps:
        # make clean
        # make all
        make release
    """),
    target=text("""
        #!/bin/sh
        make release
    """),
    hint="A count in front of dd deletes that many lines, starting with the cursor's line.",
    uses=["count"],
)
dd.add(
    title="Remove an empty loop", par=2, ext="java", cursor=(2, 10),
    task="The loop does nothing. Delete it: the for line and its closing brace. The cursor starts in the "
         "middle of line 2.",
    start=text("""
        int total = 0;
        for (int i = 0; i < n; i++) {
        }
        return total;
    """),
    target=text("""
        int total = 0;
        return total;
    """),
    hint="j moves between lines, so dj deletes this line and the next one, whole, wherever the cursor is.",
)
dd.add(
    title="Remove an empty if", par=2, ext="c", cursor=(3, 5),
    task="The if block is empty. Delete its two lines. The cursor starts on the closing brace.",
    start=text("""
        int main(void) {
            if (verbose) {
            }
            run();
            return 0;
        }
    """),
    target=text("""
        int main(void) {
            run();
            return 0;
        }
    """),
    hint="dk deletes this line and the one above it.",
)
dd.add(
    title="Header first", par=3, ext="csv",
    task="The header row ended up second. Move it to the top.",
    start=text("""
        alice,30,Paris
        name,age,city
        bob,25,Rome
    """),
    target=text("""
        name,age,city
        alice,30,Paris
        bob,25,Rome
    """),
    hint="Delete the first line, which moves the header up to line 1, then put the line back below it with p.",
    uses=["p"],
)
dd.add(
    title="Config comes first", par=5, ext="java", cursor=(4, 5),
    task="loadConfig() must run before connect(). Move it up two lines. The cursor starts on it.",
    start=text("""
        void start() {
            connect();
            authenticate();
            loadConfig();
            serve();
        }
    """),
    target=text("""
        void start() {
            loadConfig();
            connect();
            authenticate();
            serve();
        }
    """),
    hint="dd cuts the line, and the cursor lands on the line that took its place. Go up two lines and put it "
         "above that one with P.",
    uses=["count", "p"],
)
dd.add(
    title="Quiet the log", par=7, ext="txt",
    task="Delete the three DEBUG lines.",
    start=text("""
        INFO start
        DEBUG tick
        INFO step 1
        DEBUG tick
        INFO step 2
        DEBUG tick
        INFO done
    """),
    target=text("""
        INFO start
        INFO step 1
        INFO step 2
        INFO done
    """),
    hint="jdd deletes the first one and leaves the cursor on the INFO line after it. From there it's j and . "
         "for each of the others.",
    uses=["dot"],
)
dd.add(
    title="Helper before main", par=5, ext="c",
    task="In C, a function should be defined before it's used. Move main (lines 1 to 3) below helper.",
    start=text("""
        int main(void) {
            return helper();
        }
        int helper(void) {
            return 42;
        }
    """),
    target=text("""
        int helper(void) {
            return 42;
        }
        int main(void) {
            return helper();
        }
    """),
    hint="3dd cuts main's three lines. G goes to the last line, and p puts them below it.",
    uses=["count", "gg", "p"],
)
dd.add(
    title="Up from the bottom", par=3, ext="py", cursor=(3, 1),
    task="greeting is used before it's set. Move the last line up one, above the print. The cursor starts "
         "on the last line.",
    start=text("""
        name = input()
        print(greeting)
        greeting = "Hi, " + name
    """),
    target=text("""
        name = input()
        greeting = "Hi, " + name
        print(greeting)
    """),
    hint="After dd on the last line, the cursor lands on the line above. P puts a line above the cursor's line.",
    uses=["p"],
)
dd.add(
    title="Tidy the list", par=7, ext="md",
    task='Delete the "(old)" item, then swap the last two items so "Review PR" comes before "Ship release".',
    start=text("""
        ## Today
        - Write tests
        - (old) Email Bob
        - Ship release
        - Review PR
    """),
    target=text("""
        ## Today
        - Write tests
        - Review PR
        - Ship release
    """),
    hint="After dd, the cursor is on the line that moved up into the gap, which is the next line you want to "
         "move. ddp swaps a line with the one below it.",
    uses=["count", "p"],
)
dd.add(
    title="Obsolete version", par=2, ext="yaml",
    task="Compose files don't need the version line any more. Delete line 1.",
    start=text("""
        version: "3.8"
        services:
          web:
            image: nginx
    """),
    target=text("""
        services:
          web:
            image: nginx
    """),
    hint="The cursor is already on the line.",
)
dd.add(
    title="Unused imports", par=3, ext="java",
    task="Lines 2 and 3 import classes nobody uses. Delete them.",
    start=text("""
        import java.util.List;
        import java.util.Map;
        import java.util.Set;
        import java.io.File;
    """),
    target=text("""
        import java.util.List;
        import java.io.File;
    """),
    hint="Go down to line 2. d with j deletes that line and the next.",
)
dd.add(
    title="Fix the build first", par=3, ext="md",
    task='"Fix the build" should come first. Move it above "Write docs" and its sub-item.',
    start=text("""
        - Write docs
          - API page
        - Fix the build
    """),
    target=text("""
        - Fix the build
        - Write docs
          - API page
    """),
    hint="Or think of it the other way: move the two-line item below Fix the build. dj cuts both lines.",
    uses=["p"],
)
dd.add(
    title="No docstring", par=4, ext="py",
    task="Delete the three lines of the docstring.",
    start=text("""
        def area(r):
            \"\"\"
            Area of a circle.
            \"\"\"
            return 3.14159 * r * r
    """),
    target=text("""
        def area(r):
            return 3.14159 * r * r
    """),
    hint="Go down to the first quotes. d2j deletes that line and the two below it.",
    uses=["count"],
)
dd.add(
    title="Struct first", par=4, ext="c", cursor=(2, 1),
    task="The prototype uses struct point, so the struct has to come first. Move the four struct lines to "
         "the top. The cursor is on struct.",
    start=text("""
        void print_point(struct point p);
        struct point {
            int x;
            int y;
        };
    """),
    target=text("""
        struct point {
            int x;
            int y;
        };
        void print_point(struct point p);
    """),
    hint="d3j cuts the four lines. Deleting the end of the file leaves the cursor on line 1, and P puts the "
         "lines above it.",
    uses=["count", "p"],
)
dd.add(
    title="Around the write", par=5, ext="py", cursor=(3, 5),
    task="Delete the print lines above and below db.write. The cursor is on db.write.",
    start=text("""
        def save(doc):
            print("before")
            db.write(doc)
            print("after")
            return True
    """),
    target=text("""
        def save(doc):
            db.write(doc)
            return True
    """),
    hint="Go up and delete the first one. The cursor lands on db.write again, so the second print is one "
         "line down, and . deletes it.",
    uses=["dot"],
)
dd.add(
    title="Install before usage", par=5, ext="md",
    task="Move the Usage section (lines 1 and 2) below the Install section.",
    start=text("""
        ## Usage
        Run todo add.
        ## Install
        pip install todo
        Needs Python 3.
    """),
    target=text("""
        ## Install
        pip install todo
        Needs Python 3.
        ## Usage
        Run todo add.
    """),
    hint="dj cuts both lines of Usage, and the cursor lands on ## Install. Go to the section's last line "
         "and put them below it.",
    uses=["count", "p"],
)
dd.add(
    title="No try needed", par=7, ext="py",
    task="Remove the try/except: keep only run(), not indented.",
    start=text("""
        try:
            run()
        except Exception:
            pass
    """),
    target="run()",
    hint="dd deletes try: and leaves the cursor on run(), which << unindents. Then the two except lines go "
         "with one dj.",
    uses=["indent"],
)
dd.add(
    title="Sort by id", par=9, ext="csv", cursor=(2, 1),
    task="Sort the rows by id, 1 to 4, under the header. The cursor is on the first row.",
    start=text("""
        id,name
        3,cy
        1,ada
        4,di
        2,bo
    """),
    target=text("""
        id,name
        1,ada
        2,bo
        3,cy
        4,di
    """),
    hint="ddp puts 3 after 1. Then 2 has to move up two lines: after dd on the last line, the cursor is "
         "already one line up.",
    uses=["p", "count"],
)
dd.add(
    title="First and last", par=11, ext="md",
    task="Deploy and Commit are swapped. Put Commit first and Deploy last.",
    start=text("""
        - Deploy
        - Build
        - Test
        - Commit
    """),
    target=text("""
        - Commit
        - Build
        - Test
        - Deploy
    """),
    hint="Move Deploy to the end first. Then Commit is one line above the cursor: cut it, and put it above "
         "the first line.",
    uses=["count", "p"],
)


# ---------- c C cc s S ----------

c = drills.command(
    "c", "c{motion}  C  cc  s  S", "change: delete, then type",
    """c works like d, then puts you in Insert mode to type the replacement. The whole thing is one change,
    so . repeats it, typed text and all. cw is a special case: on a word it changes only to the end of
    the word, like ce, so the space after the word survives. C changes to the end of the line (like c$),
    cc or S the whole line, and s just the character under the cursor (3s changes three). cc and S keep
    the line's indentation, so you only type the new text.""",
    examples=[("cw", "change to the end of the word"), ("ct)", "change up to the )"), ("C", "change to the end of the line"),
              ("cc", "change the whole line (S does the same)"), ("3s", "change three characters"),
              ("c2w", "change two words")],
)
c.add(
    title="Rename a variable", par=8, ext="java",
    task="Rename count to total.",
    start="int count = 0;",
    target="int total = 0;",
    hint="w moves to count. cw changes to the end of the word (the space after it stays) and leaves you typing.",
    uses=["word"],
)
c.add(
    title="Quieter logs", par=7, ext="py",
    task="Change the log level from DEBUG to INFO.",
    start="level = logging.DEBUG",
    target="level = logging.INFO",
    hint="fD finds DEBUG. C changes from the cursor to the end of the line.",
    uses=["f"],
)
c.add(
    title="Break, don't continue", par=8, ext="java",
    task="Replace continue; with break; and keep the indentation.",
    start=text("""
        if (done) {
            continue;
        }
    """),
    target=text("""
        if (done) {
            break;
        }
    """),
    hint="S (or cc) replaces the whole line's text but keeps its indentation, so you only type the new "
         "statement.",
)
c.add(
    title="Fetch, not get", par=9, ext="py",
    task="Rename the method from get_name to fetch_name.",
    start="name = user.get_name()",
    target="name = user.fetch_name()",
    hint="The underscore is part of the word, so cw would change all of get_name. 3s changes just the three "
         "characters of get.",
    uses=["f", "count"],
)
c.add(
    title="Simplify the condition", par=10, ext="java",
    task="Replace the whole condition inside the parentheses with ready.",
    start="if (count > 0 && !done) {",
    target="if (ready) {",
    hint="2w lands on count. ct) changes everything up to, but not including, the ).",
    uses=["count", "word", "t"],
)
c.add(
    title="Rename everywhere", par=15, ext="java",
    task="Rename cnt to count on all three lines.",
    start=text("""
        int cnt = 0;
        cnt += step;
        return cnt;
    """),
    target=text("""
        int count = 0;
        count += step;
        return count;
    """),
    hint="Make the first change with cw. Then move to each other cnt (0 goes to the start of a line) and "
         "press . to repeat the change, typed text and all.",
    uses=["word", "dot", "line"],
)
c.add(
    title="Stub it out", par=7, ext="py",
    task="Replace the three lines of the if body with a single pass.",
    start=text("""
        if ready:
            x = 1
            y = 2
            z = 3
    """),
    target=text("""
        if ready:
            pass
    """),
    hint="A count on S (or cc) changes that many lines into one, keeping the first one's indentation.",
    uses=["count"],
)
c.add(
    title="New signature", par=17, ext="java",
    task="Change the return type to long and the method name to getTotal.",
    start="public int getCount() {",
    target="public long getTotal() {",
    hint="cw on int, then <Esc>. Only the Count part of the name needs to change: jump to its C and cw again.",
    uses=["word", "f"],
)
c.add(
    title="Skip, twice", par=16, ext="c",
    task="Replace both printf lines with continue; at the same indentation.",
    start=text(r"""
        for (int i = 0; i < n; i++) {
            if (skip[i]) {
                printf("skip %d\n", i);
            }
            if (bad[i]) {
                printf("bad %d\n", i);
            }
        }
    """),
    target=text("""
        for (int i = 0; i < n; i++) {
            if (skip[i]) {
                continue;
            }
            if (bad[i]) {
                continue;
            }
        }
    """),
    hint="S replaces a line and keeps its indentation. After the first one, 3j gets to the other printf and . "
         "repeats the whole change.",
    uses=["count", "dot"],
)
c.add(
    title="Return, don't print", par=13, ext="py",
    task="Make the function return total instead of printing it.",
    start=text("""
        def report(total):
            print("total:", total)
    """),
    target=text("""
        def report(total):
            return total
    """),
    hint='print("total:", has no spaces in it, so it\'s one WORD: cW changes it and keeps the space before '
         "total. Then delete the ) at the end.",
    uses=["word", "bigword", "line", "x"],
)
c.add(
    title="A fixed port", par=8, ext="js",
    task="Hard-code the port: const port = 8080;.",
    start="const port = process.env.PORT || 3000;",
    target="const port = 8080;",
    hint="Get to process with a counted w. C changes from there to the end of the line, so retype the ;.",
    uses=["word", "count"],
)
c.add(
    title="Power, not xor", par=5, ext="py",
    task="In Python, ^ is xor. Square y with ** instead: x = y ** 2.",
    start="x = y ^ 2",
    target="x = y ** 2",
    hint="s replaces one character with whatever you type, even two characters.",
    uses=["f"],
)
c.add(
    title="A shorter timeout", par=4, ext="sh",
    task="Give make 5 seconds instead of 30.",
    start="timeout 30 make",
    target="timeout 5 make",
    hint="cw on a number changes just the number.",
    uses=["word"],
)
c.add(
    title="Use puts", par=8, ext="c",
    task="puts adds the newline itself: puts(name);.",
    start='printf("%s\\n", name);',
    target="puts(name);",
    hint="cf and a space changes everything through the first space, the one after the comma.",
    uses=["f"],
)
c.add(
    title="Sum, not total", par=9, ext="py", cursor=(2, 5),
    task="Rename total to sum on line 2. The cursor is on the first total.",
    start=text("""
        for item in items:
            total = total + item
    """),
    target=text("""
        for item in items:
            sum = sum + item
    """),
    hint="cw for the first one. f finds the second total's t, and . repeats the change.",
    uses=["f", "dot"],
)
c.add(
    title="Ids, not names", par=9, ext="js",
    task="Use the id instead of the name: const userId = req.userId;.",
    start="const userName = req.userName;",
    target="const userId = req.userId;",
    hint="ce changes from the cursor to the end of the word, so from the N it changes just Name. fN, ; and "
         ". do the other one.",
    uses=["f", "word", "semicolon", "dot"],
)
c.add(
    title="Python booleans", par=10, ext="py",
    task="Python spells && as and: if a and b and c:.",
    start="if a && b && c:",
    target="if a and b and c:",
    hint="&& is a word of its own, so cw changes both &'s. ; finds the next & and . changes it too.",
    uses=["f", "word", "semicolon", "dot"],
)
c.add(
    title="Return the condition", par=12, ext="py",
    task="The if/else is the same as returning ok: replace the four lines with return ok.",
    start=text("""
        def ready(self):
            if ok:
                return True
            else:
                return False
    """),
    target=text("""
        def ready(self):
            return ok
    """),
    hint="A count on S replaces that many lines with one empty line, at the first one's indentation.",
    uses=["count"],
)
c.add(
    title="Rename the flag", par=16, ext="json",
    task='Rename the key to "verbose" and set it to 1.',
    start='"debug": false,',
    target='"verbose": 1,',
    hint="Two cw's: one for the key (step inside the quote first) and one for the value.",
    uses=["f", "word"],
)
c.add(
    title="A clearer index", par=14, ext="py",
    task="Rename the loop variable i to idx in all three places.",
    start=text("""
        for i in range(len(items)):
            print(i, items[i])
    """),
    target=text("""
        for idx in range(len(items)):
            print(idx, items[idx])
    """),
    hint="cw on i, then . for the others. j lands on the i of print, so fi finds the next one. For the last "
         "one, count words: the comma, items and [ are words too.",
    uses=["word", "f", "dot", "count"],
)


# ---------- y yy Y ----------

y = drills.command(
    "y", "y{motion}  yy  Y", "yank (copy)",
    """y copies (yanks) the text a motion moves over without changing anything, and p or P then puts the
    copy somewhere. yy copies the whole line, and 3yy three lines. In Neovim, Y copies from the cursor to
    the end of the line, like y$ (in Vim, Y copies the whole line, like yy). Mind where the motion stops:
    yw copies a word and the space after it, ye just the word. A yank never moves the cursor forward, but
    after a backward one like yb or yk, the cursor is at the start of what you copied.""",
    examples=[("yy", "copy the line"), ("3yy", "copy three lines"), ("yw", "copy to the next word"),
              ("ye", "copy to the end of the word"), ("Y", "copy to the end of the line"),
              ("yt,", "copy up to the comma")],
)
y.add(
    title="Close the box", par=4, ext="txt",
    task="Add a bottom border: a copy of the top line, below line 2.",
    start=text("""
        +------+
        | data |
    """),
    target=text("""
        +------+
        | data |
        +------+
    """),
    hint="yy copies the line. Go down and put it below with p.",
    uses=["p"],
)
y.add(
    title="Use the constant", par=6, ext="py",
    task="Use the constant as the default: timeout=DEFAULT_TIMEOUT_SECONDS.",
    start=text("""
        DEFAULT_TIMEOUT_SECONDS = 30
        def fetch(url, timeout=):
    """),
    target=text("""
        DEFAULT_TIMEOUT_SECONDS = 30
        def fetch(url, timeout=DEFAULT_TIMEOUT_SECONDS):
    """),
    hint="ye copies to the end of the word (yw would take the space too). Then go down, find the ) and put "
         "the name before it with P.",
    uses=["word", "f", "p"],
)
y.add(
    title="Same destination", par=5, ext="py",
    task='Send the second message to stderr too: line 2 should end with , file=sys.stderr).',
    start=text("""
        print("start", file=sys.stderr)
        print("done"
    """),
    target=text("""
        print("start", file=sys.stderr)
        print("done", file=sys.stderr)
    """),
    hint="In Neovim, Y copies from the cursor to the end of the line, like y$. Start on the comma, then put "
         "the copy at the end of line 2 with p.",
    uses=["f", "p"],
)
y.add(
    title="Copy two words", par=9, ext="py",
    task='Fill in the city: line 2 should read label = "Welcome to New York!".',
    start=text("""
        city = "New York"
        label = "Welcome to !"
    """),
    target=text("""
        city = "New York"
        label = "Welcome to New York!"
    """),
    hint="From the N, y2e copies two words: New York. Then go down, find the ! and put the copy before it "
         "with P.",
    uses=["f", "count", "word", "p"],
)
y.add(
    title="Copy an argument", par=6, ext="py",
    task="Pass x=10 to the second call too: draw(x=10, y=40).",
    start=text("""
        draw(x=10, y=20)
        draw(y=40)
    """),
    target=text("""
        draw(x=10, y=20)
        draw(x=10, y=40)
    """),
    hint='"x=10," has no spaces, so it\'s one WORD, and yW copies it with the space after it. j keeps the '
         "column, which lands on the y of line 2. P puts the copy before it.",
    uses=["f", "bigword", "p"],
)
y.add(
    title="One more test", par=10, ext="py",
    task="Add a second assert below the first one, for square(3) == 9.",
    start="assert square(2) == 4",
    target=text("""
        assert square(2) == 4
        assert square(3) == 9
    """),
    hint="yyp duplicates the line, and the cursor lands on the copy. Then fix the two numbers with r.",
    uses=["p", "f", "r", "line"],
)
y.add(
    title="Reuse an expression", par=7, ext="py",
    task="Print what the if checks: line 2 should be print(len(items)).",
    start=text("""
        if len(items) > 0:
            print()
    """),
    target=text("""
        if len(items) > 0:
            print(len(items))
    """),
    hint="w jumps to len. yf) copies through the first ), so the whole call. Then go to the ) on line 2 and "
         "put the copy before it.",
    uses=["word", "f", "line", "p"],
)
y.add(
    title="Add a prototype", par=6, ext="c",
    task="Add a prototype above the function: a copy of its first line ending with a semicolon, then a "
         "blank line.",
    start=text("""
        int clamp(int v, int lo, int hi)
        {
            return v < lo ? lo : v > hi ? hi : v;
        }
    """),
    target=text("""
        int clamp(int v, int lo, int hi);

        int clamp(int v, int lo, int hi)
        {
            return v < lo ? lo : v > hi ? hi : v;
        }
    """),
    hint="yy and P put a copy of the line above it, with the cursor on the copy. A appends at the end of the "
         "line, and Enter makes the blank line.",
    uses=["p", "insert"],
)
y.add(
    title="Add a table row", par=9, ext="md",
    task="Add a row for Bo, also an Engineer, below Ana's. Keep the columns lined up.",
    start=text("""
        | Name | Role     |
        |------|----------|
        | Ana  | Engineer |
    """),
    target=text("""
        | Name | Role     |
        |------|----------|
        | Ana  | Engineer |
        | Bo   | Engineer |
    """),
    hint='Copy Ana\'s row with yyp, then overwrite the name. R types over characters, so "Bo" and a space '
         'replace "Ana" and the columns stay put.',
    uses=["gg", "p", "word", "replace-mode"],
)
y.add(
    title="Same link twice", par=10, ext="md",
    task="The second FAQ link is empty. Give it the same URL as the first.",
    start=text("""
        Questions? See the [FAQ](https://example.com/faq).
        Still stuck? The [FAQ]() covers that too.
    """),
    target=text("""
        Questions? See the [FAQ](https://example.com/faq).
        Still stuck? The [FAQ](https://example.com/faq) covers that too.
    """),
    hint="Get just inside the first ( and yt) copies the URL up to the ). On line 2, F( goes back to the empty "
         "() and p puts the URL after the (.",
    uses=["f", "t", "p"],
)
y.add(
    title="One more item", par=3, ext="html", cursor=(2, 5),
    task="Add a second, identical list item below the first. The cursor is on it.",
    start=text("""
        <ul>
            <li>Item</li>
        </ul>
    """),
    target=text("""
        <ul>
            <li>Item</li>
            <li>Item</li>
        </ul>
    """),
    hint="yy copies the line, indentation and all, and p puts it below.",
    uses=["p"],
)
y.add(
    title="Another import", par=9, ext="py",
    task="Add import json below import os.",
    start="import os",
    target=text("""
        import os
        import json
    """),
    hint="Duplicate the line, then change everything after import on the copy.",
    uses=["p", "word", "c"],
)
y.add(
    title="Unsigned too", par=4, ext="c",
    task="b should be unsigned too: unsigned int b;.",
    start=text("""
        unsigned int a;
        int b;
    """),
    target=text("""
        unsigned int a;
        unsigned int b;
    """),
    hint="yw copies the word and the space after it. Line 2 starts in the same column.",
    uses=["word", "p"],
)
y.add(
    title="Same key for scp", par=6, ext="sh",
    task="scp needs the same key option: line 2 should be scp -i ~/.ssh/key.pem app.tar.gz.",
    start=text("""
        ssh -i ~/.ssh/key.pem ubuntu@10.0.0.5
        scp app.tar.gz
    """),
    target=text("""
        ssh -i ~/.ssh/key.pem ubuntu@10.0.0.5
        scp -i ~/.ssh/key.pem app.tar.gz
    """),
    hint="From the -, copy up to the u of ubuntu, space included. scp and ssh are the same length, so j lands "
         "on the a of app.",
    uses=["word", "t", "p"],
)
y.add(
    title="Same columns", par=6, ext="sql",
    task="Select the same columns from admins: SELECT id, name FROM admins;.",
    start=text("""
        SELECT id, name FROM users;
        SELECT FROM admins;
    """),
    target=text("""
        SELECT id, name FROM users;
        SELECT id, name FROM admins;
    """),
    hint='"id, name " is three words: id, the comma and name, with the space after it. j lands on FROM.',
    uses=["word", "count", "p"],
)
y.add(
    title="The other dimension", par=9, ext="py",
    task="Line 2 should be height = image.size[1] * scale.",
    start=text("""
        width = image.size[0] * scale
        height
    """),
    target=text("""
        width = image.size[0] * scale
        height = image.size[1] * scale
    """),
    hint="From the space after width, Y copies the whole right-hand side, = included. Put it after height, "
         "then fix the index.",
    uses=["f", "p", "r"],
)
y.add(
    title="Override them all", par=9, ext="java",
    task="Put an @Override line above b() and c() too.",
    start=text("""
        class Shape {
            @Override
            void a() {}
            void b() {}
            void c() {}
        }
    """),
    target=text("""
        class Shape {
            @Override
            void a() {}
            @Override
            void b() {}
            @Override
            void c() {}
        }
    """),
    hint="Copy the @Override line once. P puts it above a line, and . repeats the P.",
    uses=["count", "p", "dot"],
)
y.add(
    title="A second service", par=13, ext="yaml",
    task="Add a worker entry below web, with the same port: - name: worker, then port: 80.",
    start=text("""
        - name: web
          port: 80
    """),
    target=text("""
        - name: web
          port: 80
        - name: worker
          port: 80
    """),
    hint="yj copies both lines of the entry. Put them below it, then change the name on the copy.",
    uses=["p", "word", "count", "c"],
)
y.add(
    title="Fully qualified", par=10, ext="py", cursor=(1, 11),
    task="Formatter and Filter live in logging too: lines 2 and 3 should use logging.Formatter and "
         "logging.Filter. The cursor is on logging.",
    start=text("""
        handler = logging.StreamHandler()
        formatter = Formatter("%(asctime)s %(message)s")
        filt = Filter("app")
    """),
    target=text("""
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s %(message)s")
        filt = logging.Filter("app")
    """),
    hint='"logging." is two words, logging and the dot. Copy them and put them in front of Formatter. . '
         "repeats a put, so on line 3 you only need to get to the F.",
    uses=["word", "count", "f", "p", "dot"],
)
y.add(
    title="Fill in the prototype", par=7, ext="c", cursor=(2, 1),
    task="Give the prototype the same parameters as the definition: int clamp(int v, int lo, int hi);. The "
         "cursor is on the definition.",
    start=text("""
        int clamp();
        int clamp(int v, int lo, int hi)
        {
            return v < lo ? lo : v > hi ? hi : v;
        }
    """),
    target=text("""
        int clamp(int v, int lo, int hi);
        int clamp(int v, int lo, int hi)
        {
            return v < lo ? lo : v > hi ? hi : v;
        }
    """),
    hint="Copy what's inside the parentheses with yt). Both lines start with int clamp(, so k lands right on "
         "the empty ()'s ).",
    uses=["f", "t", "p"],
)


# ---------- p P ----------

p = drills.command(
    "p", "p  P", "put (paste)",
    """p puts (pastes) the text you last deleted or yanked after the cursor, and P puts it before. Whole
    lines (from dd, yy or dj) go on new lines: below the cursor's line for p, above it for P. Anything
    else goes inside the line. A count puts several copies: 3p. After a put the cursor is on the last
    character put, or, for whole lines, on the first non-blank of the first new line. Every delete (x, d, c, s)
    replaces what p will put, so put before you delete anything else.""",
    examples=[("p", "put after the cursor, or below the line"), ("P", "put before the cursor, or above the line"),
              ("3p", "put three copies"), ("xp", "swap two characters"), ("ddp", "swap two lines"),
              ("yyp", "duplicate a line")],
)
p.add(
    title="Conclusion last", par=4, ext="md",
    task="Move the first item to the end of the list.",
    start=text("""
        - Conclusion
        - Introduction
        - Methods
        - Results
    """),
    target=text("""
        - Introduction
        - Methods
        - Results
        - Conclusion
    """),
    hint="dd cuts the line. G jumps to the last line, and p puts the line below it.",
    uses=["dd", "gg"],
)
p.add(
    title="Word order", par=5, ext="txt",
    task='Move "really" in front of "like": "I really like pizza."',
    start="I like really pizza.",
    target="I really like pizza.",
    hint='dw cuts "like " with its space, which leaves the cursor on "really". Hop to the next word and put '
         "the cut text in front of it with P.",
    uses=["d", "word"],
)
p.add(
    title="Rows of zeros", par=5, ext="py",
    task="Make the grid three rows tall: add two more copies of the [0, 0, 0] row.",
    start=text("""
        grid = [
            [0, 0, 0],
        ]
    """),
    target=text("""
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
    """),
    hint="yy copies the row, and a count on p puts it that many times.",
    uses=["y", "count"],
)
p.add(
    title="Misplaced comma", par=6, ext="c",
    task="The comma is in the wrong place. Move it to right after the format string.",
    start='printf("%d\\n" count,);',
    target='printf("%d\\n", count);',
    hint='x cuts the comma (x saves what it deletes, like d). F" jumps back to the closing quote, and p puts '
         "the comma after it.",
    uses=["x", "f"],
)
p.add(
    title="Spell out the type", par=7, ext="java",
    task="Fill in the empty <> with String: new ArrayList<String>().",
    start="List<String> names = new ArrayList<>();",
    target="List<String> names = new ArrayList<String>();",
    hint="fS and yw copy String. f< finds the next <, and p puts the copy after the cursor.",
    uses=["f", "y", "word"],
)
p.add(
    title="Finish the separator", par=6, ext="md",
    task="The separator row only covers the first column. Extend it to all three: |------|------|------|",
    start=text("""
        | Name | Team | City |
        |------|
        | Ana  | Red  | Oslo |
    """),
    target=text("""
        | Name | Team | City |
        |------|------|------|
        | Ana  | Red  | Oslo |
    """),
    hint='Copy one column\'s worth, "------|": from the first -, Y copies to the end of the line. Then $ and '
         "2p add two copies at the end.",
    uses=["y", "line", "count"],
)
p.add(
    title="Another static method", par=6, ext="py",
    task="render should be a static method too: put a copy of @staticmethod above it.",
    start=text("""
        class Parser:
            @staticmethod
            def parse(text):
                return text.split()

            def render(items):
                return " ".join(items)
    """),
    target=text("""
        class Parser:
            @staticmethod
            def parse(text):
                return text.split()

            @staticmethod
            def render(items):
                return " ".join(items)
    """),
    hint="yy copies the decorator line. Go down to the def render line (the relative line numbers show how "
         "far) and P puts the copy above it.",
    uses=["y", "count"],
)
p.add(
    title="Install last", par=4, ext="sh",
    task="Put the steps in order: ./configure, then make, then make install.",
    start=text("""
        make install
        ./configure
        make
    """),
    target=text("""
        ./configure
        make
        make install
    """),
    hint="dd cuts the first line and leaves the cursor on ./configure. Go down one more line and put it below.",
    uses=["dd"],
)
p.add(
    title="Comment on its own line", par=6, ext="py",
    task="Move the comment to a line of its own, above the code.",
    start="total = price * qty  # in cents",
    target=text("""
        # in cents
        total = price * qty
    """),
    hint="D cuts from the # to the end of the line. Text cut from inside a line goes back inside a line, so "
         "open an empty line above with O first, then put it there.",
    uses=["f", "d", "o"],
)
p.add(
    title="Sort the imports", par=7, ext="py",
    task="Sort the imports alphabetically: json, os, sys.",
    start=text("""
        import sys
        import os
        import json
    """),
    target=text("""
        import json
        import os
        import sys
    """),
    hint="Think in moves: cut the first two lines and put them below json, then swap the two that are still "
         "out of order.",
    uses=["dd", "count"],
)
p.add(
    title="Semicolon outside", par=4, ext="js",
    task='The semicolon ended up inside the call: console.log("done");.',
    start='console.log("done";)',
    target='console.log("done");',
    hint="Cut the ; with x. The cursor lands on the ), and p puts the ; after it.",
    uses=["f", "x"],
)
p.add(
    title="First name first", par=6, ext="txt",
    task="Write the name first name first: Ada Lovelace.",
    start="Lovelace Ada",
    target="Ada Lovelace",
    hint="dw cuts Lovelace and its space. Add a space at the end of the line and put the word after it.",
    uses=["d", "word", "insert"],
)
p.add(
    title="The same class", par=7, ext="html",
    task='Give the second div the same class: <div class="card">.',
    start=text("""
        <div class="card">
        <div>
    """),
    target=text("""
        <div class="card">
        <div class="card">
    """),
    hint="From the space after div, copy up to the >. On line 2, j lands right on the >, and P puts the "
         "copy before it.",
    uses=["f", "y", "t"],
)
p.add(
    title="Add inside the call", par=6, ext="py",
    task="The + 1 should be inside print: print(len(self.cache.items) + 1).",
    start="print(len(self.cache.items)) + 1",
    target="print(len(self.cache.items) + 1)",
    hint="The ) to move is the one just before the first space on the line. Cut it with x, then put it after "
         "the 1.",
    uses=["t", "f", "x"],
)
p.add(
    title="Comment on the right line", par=7, ext="py",
    task="The comment belongs to timeout: move \"  # seconds\" (two spaces and all) to the end of line 2.",
    start=text("""
        x = load()  # seconds
        timeout = 30
    """),
    target=text("""
        x = load()
        timeout = 30  # seconds
    """),
    hint="The comment starts at the third space on the line: 3f and a space gets there, and D cuts to the "
         "end. D leaves the cursor on the ), and j lands just before 30, so e gets you to its end.",
    uses=["f", "count", "d", "word"],
)
p.add(
    title="More separators", par=10, ext="md",
    task="Put a --- line after each section, like the one after One.",
    start=text("""
        ## One
        text one
        ---
        ## Two
        text two
        ## Three
        text three
    """),
    target=text("""
        ## One
        text one
        ---
        ## Two
        text two
        ---
        ## Three
        text three
        ---
    """),
    hint="yy the ---, and p it below text two. . repeats a put too.",
    uses=["y", "count", "dot"],
)
p.add(
    title="Imports at the top", par=5, ext="py", cursor=(4, 1),
    task="Move import sys up, below import os. The cursor is on it.",
    start=text("""
        import os
        def main():
            pass
        import sys
    """),
    target=text("""
        import os
        import sys
        def main():
            pass
    """),
    hint="dd on the last line leaves the cursor on the line above. From there, go up to import os and put "
         "the line below it.",
    uses=["dd", "count"],
)
p.add(
    title="Old goes last", par=5, ext="md",
    task="Move the Old item, with its two sub-items, to the end of the list.",
    start=text("""
        - Old
          - a
          - b
        - New
        - Newer
    """),
    target=text("""
        - New
        - Newer
        - Old
          - a
          - b
    """),
    hint="3dd cuts the three lines, and the cursor lands on New. One line down, p puts them below Newer.",
    uses=["dd", "count"],
)
p.add(
    title="Filter, then sort", par=6, ext="sh",
    task="grep first: grep error | sort | uniq.",
    start="sort | grep error | uniq",
    target="grep error | sort | uniq",
    hint='"sort | " is two words, the | included. Cut them, and put them in front of uniq.',
    uses=["d", "count", "word", "f"],
)
p.add(
    title="Floats all round", par=11, ext="py",
    task="Annotate b and c like a: def mix(a: float, b: float, c: float):.",
    start="def mix(a: float, b, c):",
    target="def mix(a: float, b: float, c: float):",
    hint='Copy ": float" once, with yt, from the colon. Put it after b, and . repeats the put after c.',
    uses=["f", "y", "t", "dot"],
)


# ---------- . ----------

dot = drills.command(
    "dot", ".", "repeat the last change",
    """. repeats your last change: an operator with its motion (like dw or dt,), a command like x, dd,
    >> or p, or an insert together with the text you typed (A;<Esc>, cwnew<Esc>, ofoo<Esc>). Moving
    isn't a change, so you can move with any keys you like and then press . to make the same change
    there: one key to move, one key to repeat. A count replaces the original one: after 2dd, 3. deletes
    three lines.""",
    examples=[(".", "repeat the last change"), ("A;<Esc>j.", "add ; to this line and the next"),
              ("dwj.", "delete a word here and on the next line"), ("cwnew<Esc>w.", "change this word and the next"),
              ("dd3.", "delete a line, then three more")],
)
dot.add(
    title="Continue the command", par=8, ext="sh",
    task="Make this one long command: end lines 1 to 3 with a space and a backslash.",
    start=text("""
        docker run
          -p 8080:80
          -v data:/data
          nginx
    """),
    target=text("""
        docker run \\
          -p 8080:80 \\
          -v data:/data \\
          nginx
    """),
    hint="A, then type a space and \\, then <Esc>. On the next line, . does all of that again.",
    uses=["insert"],
)
dot.add(
    title="X wins", par=8, ext="txt", cursor=(1, 6),
    task="Put an X on all three dots of the middle column. The cursor is on the top one.",
    start=text("""
         . | . | .
        ---+---+---
         . | . | .
        ---+---+---
         . | . | .
    """),
    target=text("""
         . | X | .
        ---+---+---
         . | X | .
        ---+---+---
         . | X | .
    """),
    hint="rX changes the first one. 2j moves straight down two lines, and . repeats the rX.",
    uses=["r", "count"],
)
dot.add(
    title="Not static", par=4, ext="c",
    task="Remove \"static \" from both declarations.",
    start=text("""
        static int add(int a, int b);
        static int sub(int a, int b);
    """),
    target=text("""
        int add(int a, int b);
        int sub(int a, int b);
    """),
    hint="dw deletes the first static and its space. j moves down, and . deletes the next one.",
    uses=["d", "word"],
)
dot.add(
    title="Two debug prints", par=5, ext="c",
    task="Remove the two printf lines.",
    start=text("""
        int load(const char *path) {
            printf("loading\\n");
            int fd = open(path, O_RDONLY);
            printf("done\\n");
            return fd;
        }
    """),
    target=text("""
        int load(const char *path) {
            int fd = open(path, O_RDONLY);
            return fd;
        }
    """),
    hint="dd the first one. The lines below move up, so the second printf is now just one line further "
         "down.",
    uses=["dd"],
)
dot.add(
    title="Two levels deeper", par=3, ext="py", cursor=(3, 1),
    task="print(cell) belongs inside both loops: indent it by two levels (8 spaces). The cursor is on it.",
    start=text("""
        for row in grid:
            for cell in row:
        print(cell)
    """),
    target=text("""
        for row in grid:
            for cell in row:
                print(cell)
    """),
    hint=">> indents the line once, and . does it again.",
    uses=["indent"],
)
dot.add(
    title="Add the commas", par=7, ext="txt",
    task='Separate the first three items with commas: "We need eggs, milk, bread and butter."',
    start="We need eggs milk bread and butter.",
    target="We need eggs, milk, bread and butter.",
    hint="A counted e gets you to the end of eggs, and a,<Esc> adds the comma. Then e moves to the end of "
         "the next word and . adds another.",
    uses=["word", "insert", "count"],
)
dot.add(
    title="Decorate both methods", par=18, ext="py", cursor=(2, 5),
    task="Put @staticmethod above both methods, indented like the def lines. The cursor is on the first "
         "def.",
    start=text("""
        class MathUtils:
            def add(a, b):
                return a + b

            def sub(a, b):
                return a - b
    """),
    target=text("""
        class MathUtils:
            @staticmethod
            def add(a, b):
                return a + b

            @staticmethod
            def sub(a, b):
                return a - b
    """),
    hint="O@staticmethod<Esc> for the first one. . repeats the O and the text, so go to the second def and "
         "press it.",
    uses=["o", "count"],
)
dot.add(
    title="Remove the debugging", par=6, ext="py", cursor=(2, 1),
    task="Remove import pdb and the three debugging lines at the start of main. The cursor is on the "
         "import.",
    start=text("""
        import os
        import pdb

        def main():
            pdb.set_trace()
            print("debug 1")
            print("debug 2")
            run()
    """),
    target=text("""
        import os

        def main():
            run()
    """),
    hint="dd the import. After moving to pdb.set_trace(), a count on . replaces dd's count of one, so 3. "
         "deletes three lines.",
    uses=["dd", "count"],
)
dot.add(
    title="Reset to zero", par=11, ext="java",
    task="Initialize all three variables to 0 instead of calling the compute methods.",
    start=text("""
        int a = computeA();
        int b = computeB();
        int c = computeC();
    """),
    target=text("""
        int a = 0;
        int b = 0;
        int c = 0;
    """),
    hint="fc gets you to compute on line 1, and ct; changes up to the semicolon. j stays in the same column, "
         "so if the cursor ends up where compute started, j. does the next line.",
    uses=["f", "c", "t"],
)
dot.add(
    title="Make the fields private", par=15, ext="java",
    task="Add \"private \" in front of all three fields.",
    start=text("""
        class User {
            String name;
            int age;
            String email;
        }
    """),
    target=text("""
        class User {
            private String name;
            private int age;
            private String email;
        }
    """),
    hint="I types before the first non-blank, after the indentation. Do the first field, then j. twice.",
    uses=["insert"],
)
dot.add(
    title="No semicolons in Python", par=7, ext="py",
    task="Remove the semicolon at the end of all three lines.",
    start=text("""
        x = 10;
        name = "ada";
        items = [];
    """),
    target=text("""
        x = 10
        name = "ada"
        items = []
    """),
    hint="A, then <BS> in Insert mode, deletes the last character of a line wherever it is, and . repeats "
         "the whole thing.",
    uses=["insert"],
)
dot.add(
    title="Comment out the ports", par=6, ext="yaml", cursor=(3, 5),
    task="Comment out both ports lines, keeping their indentation. The cursor is on the first one.",
    start=text("""
        services:
          web:
            ports:
              - "80:80"
            image: nginx
    """),
    target=text("""
        services:
          web:
            # ports:
              # - "80:80"
            image: nginx
    """),
    hint="I types after the indentation. . repeats the I too, so the # lands after the next line's "
         "indentation, however deep.",
    uses=["insert"],
)
dot.add(
    title="Shorter keys", par=11, ext="toml", cursor=(2, 1),
    task="Rename host to addr in both sections. The cursor is on the first host.",
    start=text("""
        [server]
        host = "0.0.0.0"
        [client]
        host = "localhost"
    """),
    target=text("""
        [server]
        addr = "0.0.0.0"
        [client]
        addr = "localhost"
    """),
    hint="cw for the first one. The cursor ends on the r of addr, so after 2j it's inside the other host: b "
         "goes back to its start for the .",
    uses=["c", "count", "word"],
)
dot.add(
    title="One space too many", par=6, ext="py",
    task="The body is indented five spaces instead of four. Remove one space from each of the three lines.",
    start=text("""
        def area(w, h):
             a = w * h
             print(a)
             return a
    """),
    target=text("""
        def area(w, h):
            a = w * h
            print(a)
            return a
    """),
    hint="x in the first column, then j and . for the others. x leaves the cursor in column 1.",
    uses=["x"],
)
dot.add(
    title="Long everywhere", par=12, ext="c",
    task="Use long for the return type and both parameters: long add(long a, long b).",
    start="int add(int a, int b)",
    target="long add(long a, long b)",
    hint="cw for the first int. fi finds the next one, and . repeats the change. ; finds the last.",
    uses=["c", "f", "semicolon"],
)
dot.add(
    title="No units on zero", par=7, ext="css",
    task="0 needs no unit: make both values 0;.",
    start=text("""
        margin: 0px;
        padding: 0px;
    """),
    target=text("""
        margin: 0;
        padding: 0;
    """),
    hint="fp and dw delete the first px. After that the cursor is on the ;, and j lands on line 2's 0, right "
         "in front of px.",
    uses=["f", "d", "word"],
)
dot.add(
    title="Final parameters", par=13, ext="java",
    task="Make both parameters final: void save(final int id, final String name).",
    start="void save(int id, String name)",
    target="void save(final int id, final String name)",
    hint='i "final " in front of int, then find String and press . there. A counted w gets you to int.',
    uses=["word", "count", "insert", "f"],
)
dot.add(
    title="Quote the names", par=15, ext="py", cursor=(2, 5),
    task='Turn the bare names into strings, each with a comma: "ada", "grace", "linus",. The cursor is on '
         "ada.",
    start=text("""
        names = [
            ada
            grace
            linus
        ]
    """),
    target=text("""
        names = [
            "ada",
            "grace",
            "linus",
        ]
    """),
    hint=". repeats only the last change, so do the opening quotes on every line first, then the endings on "
         "every line.",
    uses=["insert"],
)
dot.add(
    title="Level three", par=7, ext="md",
    task="Make both headings level three: ### Setup and ### Usage.",
    start=text("""
        ## Setup
        text
        # Usage
        text
    """),
    target=text("""
        ### Setup
        text
        ### Usage
        text
    """),
    hint="I# adds one #. On the Usage line, a count in front of . replaces the insert's count, so 2. types "
         "two.",
    uses=["insert", "count"],
)
dot.add(
    title="Spell it out", par=20, ext="js",
    task="Rename res to response in all three places.",
    start=text("""
        const res = await fetch(url, { method: "GET" });
        if (!res.ok) throw new HttpError("failed", res.status);
    """),
    target=text("""
        const response = await fetch(url, { method: "GET" });
        if (!response.ok) throw new HttpError("failed", response.status);
    """),
    hint="cw for the first one. After j, F finds the r of the second res behind the cursor. For the third, "
         "find the comma in front of it.",
    uses=["word", "c", "f"],
)


# ---------- > < >> << ----------

indent = drills.command(
    "indent", ">  <  >>  <<", "shift lines right or left",
    """> shifts lines right by one indent (the shiftwidth, 4 spaces here) and < shifts them left. They're
    operators that always work on whole lines: >> shifts the current line, 3>> shifts three lines one
    level (not one line three levels), and >j, >k or >} shift the lines the motion covers. To go another
    level, press . to repeat. Blank lines are left alone, and with smartindent on (as here) > also skips
    lines whose first character is #, like a Python comment in the first column.""",
    examples=[(">>", "indent this line"), ("<<", "unindent this line"), ("3>>", "indent three lines"),
              (">j", "indent this line and the next"), (">}", "indent to the end of the paragraph"),
              (">>.", "indent two levels")],
)
indent.add(
    title="Into the function", par=3, ext="py",
    task="Indent the print line so it's inside the function.",
    start=text("""
        def hello():
        print("hi")
    """),
    target=text("""
        def hello():
            print("hi")
    """),
    hint="Go down a line. >> shifts the line right by one indent.",
)
indent.add(
    title="One level too deep", par=4, ext="java",
    task="int y is indented one level too far. Line it up with int x.",
    start=text("""
        public class Point {
            int x;
                int y;
        }
    """),
    target=text("""
        public class Point {
            int x;
            int y;
        }
    """),
    hint="<< shifts a line left by one indent.",
    uses=["count"],
)
indent.add(
    title="Indent the body", par=4, ext="c",
    task="Indent the three statements inside main.",
    start=text(r"""
        int main(void) {
        printf("a\n");
        printf("b\n");
        return 0;
        }
    """),
    target=text(r"""
        int main(void) {
            printf("a\n");
            printf("b\n");
            return 0;
        }
    """),
    hint="A count on >> shifts that many lines, starting with the cursor's line: 3>> shifts three lines one "
         "level.",
    uses=["count"],
)
indent.add(
    title="Into the if", par=2, ext="py", cursor=(4, 5),
    task="The last two lines belong inside the if. Indent them one more level. The cursor starts on the last "
         "line.",
    start=text("""
        for line in lines:
            if line:
            print(line)
            count += 1
    """),
    target=text("""
        for line in lines:
            if line:
                print(line)
                count += 1
    """),
    hint="> is an operator like d, and k covers this line and the one above.",
)
indent.add(
    title="Indent a paragraph", par=3, ext="py",
    task="Indent the three calls so they're inside main().",
    start=text("""
        def main():
        setup()
        run()
        cleanup()

        main()
    """),
    target=text("""
        def main():
            setup()
            run()
            cleanup()

        main()
    """),
    hint="} moves to the next blank line. >} shifts every line from the cursor to there (the blank line itself "
         "stays empty).",
    uses=["paragraph"],
)
indent.add(
    title="Two levels deep", par=4, ext="py",
    task="print(cell) belongs inside the inner loop: indent it two levels (8 spaces).",
    start=text("""
        for row in grid:
            for cell in row:
        print(cell)
    """),
    target=text("""
        for row in grid:
            for cell in row:
                print(cell)
    """),
    hint="G jumps to the last line. >> shifts it once, and . shifts it again.",
    uses=["gg", "dot"],
)
indent.add(
    title="Fix the class", par=8, ext="java",
    task="Indent the class: the field and the method one level, the method's body two levels.",
    start=text("""
        class Counter {
        private int count;
        public void add() {
        count++;
        }
        }
    """),
    target=text("""
        class Counter {
            private int count;
            public void add() {
                count++;
            }
        }
    """),
    hint="4>> shifts lines 2 to 5 one level. Then count++; needs one more: go down to it and >> again.",
    uses=["count"],
)
indent.add(
    title="Drop the if", par=4, ext="py",
    task="The if True: is pointless. Delete that line and unindent the three lines under it.",
    start=text("""
        if True:
            x = load()
            y = parse(x)
            save(y)
    """),
    target=text("""
        x = load()
        y = parse(x)
        save(y)
    """),
    hint="dd deletes the if line. < is an operator too: <G shifts every line from the cursor to the end of "
         "the file.",
    uses=["dd", "gg"],
)
indent.add(
    title="Nest the list", par=6, ext="md",
    task="Nest the items under their headings: indent Apple, Banana, Carrot and Leek one level.",
    start=text("""
        - Fruit
        - Apple
        - Banana
        - Vegetables
        - Carrot
        - Leek
    """),
    target=text("""
        - Fruit
            - Apple
            - Banana
        - Vegetables
            - Carrot
            - Leek
    """),
    hint=">j indents two lines. Move down to the next pair and press . to do it again.",
    uses=["count", "dot"],
)
indent.add(
    title="Wrap it in an if", par=15, ext="py",
    task='Only print the state when debugging: add "if debug:" above that line and indent the print under it.',
    start=text("""
        def run():
            print("start")
            print("state:", state)
            work()
    """),
    target=text("""
        def run():
            print("start")
            if debug:
                print("state:", state)
            work()
    """),
    hint="o opens a new line below, with the same indentation. After typing the if, go down to the print and "
         "shift it with >>.",
    uses=["o"],
)
indent.add(
    title="Return after the loop", par=4, ext="py",
    task="The return runs on the first pass of the loop. Unindent it so it runs after the loop.",
    start=text("""
        def total(xs):
            t = 0
            for x in xs:
                t += x
                return t
    """),
    target=text("""
        def total(xs):
            t = 0
            for x in xs:
                t += x
            return t
    """),
    hint="The relative line numbers say how far down the return is. << shifts it left one level.",
    uses=["count"],
)
indent.add(
    title="Inside the with", par=3, ext="py", cursor=(4, 1),
    task="The three lines under the with belong inside it. Indent them. The cursor is on the last one.",
    start=text("""
        with open(path) as f:
        data = f.read()
        rows = data.split()
        print(rows)
    """),
    target=text("""
        with open(path) as f:
            data = f.read()
            rows = data.split()
            print(rows)
    """),
    hint="> takes any line motion, upward ones too: 2k covers this line and the two above.",
    uses=["count"],
)
indent.add(
    title="Inside the loop", par=4, ext="c",
    task="The if belongs inside the for loop: indent it one more level.",
    start=text("""
        int main(void) {
            for (;;) {
            if (done) break;
            }
        }
    """),
    target=text("""
        int main(void) {
            for (;;) {
                if (done) break;
            }
        }
    """),
    hint="Go down to the if and shift it right.",
    uses=["count"],
)
indent.add(
    title="Too deep", par=4, ext="py",
    task="The body is indented eight spaces. Make it four.",
    start=text("""
        def area(w, h):
                a = w * h
                print(a)
                return a
    """),
    target=text("""
        def area(w, h):
            a = w * h
            print(a)
            return a
    """),
    hint="A count on << shifts that many lines one level left.",
    uses=["count"],
)
indent.add(
    title="Way too deep", par=5, ext="py",
    task="The return is three levels too deep. Indent it just one level, under the def.",
    start=text("""
        def answer():
                        return 42
    """),
    target=text("""
        def answer():
            return 42
    """),
    hint="<< takes off one level, and . takes off another.",
    uses=["dot"],
)
indent.add(
    title="No extra block", par=8, ext="c",
    task="The braces around the two declarations do nothing. Delete both brace lines and unindent the two "
         "lines.",
    start=text("""
        {
            int a = 1;
            int b = 2;
        }
        int c = a + b;
    """),
    target=text("""
        int a = 1;
        int b = 2;
        int c = a + b;
    """),
    hint="dd the {, which leaves the cursor on the first declaration. <j shifts it and the next line left. "
         "The } is then two lines down.",
    uses=["dd", "count"],
)
indent.add(
    title="Nested settings", par=8, ext="yaml",
    task="Nest the settings: port and tls under server (two spaces), cert and key under tls (four).",
    start=text("""
        server:
        port: 80
        tls:
        cert: a.pem
        key: a.key
    """),
    target=text("""
        server:
          port: 80
          tls:
            cert: a.pem
            key: a.key
    """),
    hint="YAML files use two-space indents here. Shift all four lines once, then the last two once more.",
    uses=["count"],
)
indent.add(
    title="Bodies of the branches", par=7, ext="py",
    task="Indent the two return lines under their if and else.",
    start=text("""
        def sign(x):
            if x > 0:
            return 1
            else:
            return -1
    """),
    target=text("""
        def sign(x):
            if x > 0:
                return 1
            else:
                return -1
    """),
    hint=">> the first one, then go down to the other and repeat it with .",
    uses=["count", "dot"],
)
indent.add(
    title="The comment too", par=8, ext="py",
    task="Indent all three lines of main's body, the comment included.",
    start=text("""
        def main():
        # read the config
        cfg = load()
        run(cfg)
    """),
    target=text("""
        def main():
            # read the config
            cfg = load()
            run(cfg)
    """),
    hint="Try 3>> and look at the comment: with smartindent on, > skips lines that start with # in the "
         "first column. Type its four spaces instead, with a counted insert.",
    uses=["count", "insert"],
)
indent.add(
    title="Nested lists", par=12, ext="html",
    task="Indent the HTML to show the nesting: each level four spaces deeper than the one around it.",
    start=text("""
        <ul>
        <li>Home</li>
        <li>About
        <ul>
        <li>Team</li>
        </ul>
        </li>
        </ul>
    """),
    target=text("""
        <ul>
            <li>Home</li>
            <li>About
                <ul>
                    <li>Team</li>
                </ul>
            </li>
        </ul>
    """),
    hint="Work from the outside in: shift everything between the outer <ul> lines once, then the inner list "
         "once more, then Team once more.",
    uses=["count"],
)


# ---------- J ----------

join = drills.command(
    "join", "J", "join lines",
    """J joins the next line onto the end of this one: it removes the next line's indentation and puts one
    space between them. It adds no space if the next line starts with ), or if this line already ends
    with a space. A count joins that many lines, so 3J makes three lines one (2J is the same as J). In
    code, J also drops the comment marker (# or //) of the line it joins, so two comment lines become one
    comment. The cursor ends where the lines meet, ready for an x or an i.""",
    examples=[("J", "join the next line onto this one"), ("3J", "join three lines"), ("Jx", "join without a space"),
              ("Ji,", "join, then add a comma"), ("kJ", "join this line onto the one above")],
)
join.add(
    title="One sentence", par=1, ext="md",
    task="Join the two lines into one sentence.",
    start=text("""
        Remember to back up
        the database first.
    """),
    target="Remember to back up the database first.",
    hint="J joins the next line onto this one, with a space between them.",
)
join.add(
    title="One call, one line", par=2, ext="py",
    task="Put the call on a single line.",
    start=text("""
        result = compute(alpha,
                         beta,
                         gamma)
    """),
    target="result = compute(alpha, beta, gamma)",
    hint="J with a count joins that many lines. It removes each joined line's indentation and adds one space.",
    uses=["count"],
)
join.add(
    title="Close the call", par=2, ext="java",
    task="Move the stray ); up onto the end of line 2.",
    start=text("""
        if (ready) {
            start(config
            );
        }
    """),
    target=text("""
        if (ready) {
            start(config);
        }
    """),
    hint="Go down a line and press J. It doesn't add a space before a line that starts with ).",
)
join.add(
    title="Mend the URL", par=2, ext="py",
    task="The URL got split across two lines. Join them with no space in between.",
    start=text("""
        url = "https://example.com/api/
        v2/users"
    """),
    target='url = "https://example.com/api/v2/users"',
    hint="J leaves the cursor on the space it added, so x deletes it.",
    uses=["x"],
)
join.add(
    title="The missing comma", par=3, ext="py",
    task='The list is missing a comma, so Python glues "green" and "blue" together. Join the lines and add '
         'the comma: ["red", "green", "blue"].',
    start=text("""
        colors = ["red", "green"
                  "blue"]
    """),
    target='colors = ["red", "green", "blue"]',
    hint='After J the cursor is on the space between "green" and "blue". i inserts before the cursor.',
    uses=["insert"],
)
join.add(
    title="One comment", par=2, ext="py", cursor=(3, 5),
    task="Merge the two comment lines into one comment. The cursor starts on the second one.",
    start=text("""
        def total(cart):
            # Sum of all item prices,
            # including tax.
            return sum(cart)
    """),
    target=text("""
        def total(cart):
            # Sum of all item prices, including tax.
            return sum(cart)
    """),
    hint="J joins the line below onto the cursor's line, so start on the first comment. In code, J also "
         "removes the second line's #.",
)
join.add(
    title="Name and role", par=5, ext="txt",
    task="Join each person's role onto the line with their name.",
    start=text("""
        Ana Lima
            Engineer
        Bo Chen
            Designer
        Cy Park
            Manager
    """),
    target=text("""
        Ana Lima Engineer
        Bo Chen Designer
        Cy Park Manager
    """),
    hint="J does the first pair and leaves you on that line. j moves to the next name, and . repeats the J.",
    uses=["dot"],
)
join.add(
    title="Merge the strings", par=5, ext="py",
    task='Make it one string on one line: message = "Your order has been shipped."',
    start=text(r"""
        message = "Your order has been " \
            "shipped."
    """),
    target='message = "Your order has been shipped."',
    hint='J first. Then the five characters between "been " and shipped (quote, space, backslash, space, '
         'quote) have to go: F" jumps back to the first of them, and 5x deletes five characters.',
    uses=["f", "x", "count"],
)
join.add(
    title="Braces on the same line", par=4, ext="c",
    task="Move each opening brace up to the end of its function's first line.",
    start=text("""
        void start(void)
        {
            run();
        }
        void stop(void)
        {
            halt();
        }
    """),
    target=text("""
        void start(void) {
            run();
        }
        void stop(void) {
            halt();
        }
    """),
    hint="J pulls the { up. The second function's first line is then three lines down, and . repeats the J.",
    uses=["count", "dot"],
)
join.add(
    title="One-line signature", par=5, ext="py",
    task="Put the signature on one line: def connect(host, port):",
    start=text("""
        def connect(
            host,
            port,
        ):
    """),
    target="def connect(host, port):",
    hint="J and then x join host on without a space. 3J joins the rest; it adds no space before the ), and "
         "leaves the cursor on it, so X deletes the comma before it.",
    uses=["x", "count"],
)
join.add(
    title="One bullet", par=1, ext="md",
    task="Merge the two bullets into one: - Install Neovim and its plugins.",
    start=text("""
        - Install Neovim
        - and its plugins
    """),
    target="- Install Neovim and its plugins",
    hint="In Markdown a list dash counts like a comment marker, so J drops the second one.",
)
join.add(
    title="One query, one line", par=2, ext="sql",
    task="Put the whole query on one line.",
    start=text("""
        SELECT id,
               name,
               email
        FROM users;
    """),
    target="SELECT id, name, email FROM users;",
    hint="A count on J joins that many lines, and each joined line loses its indentation.",
    uses=["count"],
)
join.add(
    title="No continuation", par=3, ext="sh",
    task="Make it one line without the backslash: docker run -p 80:80 nginx.",
    start=text(r"""
        docker run \
          -p 80:80 nginx
    """),
    target="docker run -p 80:80 nginx",
    hint="J leaves the backslash in, and puts the cursor on the space it added after it. X deletes backward.",
    uses=["x", "count"],
)
join.add(
    title="Cuddle the else", par=3, ext="js",
    task="Put the else on the same line as the closing brace: } else {.",
    start=text("""
        if (ok) {
            save();
        }
        else {
            retry();
        }
    """),
    target=text("""
        if (ok) {
            save();
        } else {
            retry();
        }
    """),
    hint="Go to the } line and join the else line onto it.",
    uses=["count"],
)
join.add(
    title="Add the tax", par=4, ext="py",
    task="Make it one expression: total = price + tax.",
    start=text("""
        total = price
        tax
    """),
    target="total = price + tax",
    hint="J puts the cursor on the space between price and tax. Type the + and its own space there.",
    uses=["insert"],
)
join.add(
    title="Comma-separated", par=6, ext="csv",
    task="Make the three values one CSV row: ada,36,london.",
    start=text("""
        ada
        36
        london
    """),
    target="ada,36,london",
    hint="After J the cursor is on the space it added, and r turns it into a comma. Twice.",
    uses=["r"],
)
join.add(
    title="A list on one line", par=7, ext="py",
    task="Make the names a list on one line: [ada, bob, cy].",
    start=text("""
        ada,
        bob,
        cy
    """),
    target="[ada, bob, cy]",
    hint="3J does the joining, spaces included. Then I and A add the brackets.",
    uses=["count", "insert"],
)
join.add(
    title="Key, value", par=8, ext="yaml",
    task="Join each key with its value as YAML: name: ada and age: 36.",
    start=text("""
        name
        ada
        age
        36
    """),
    target=text("""
        name: ada
        age: 36
    """),
    hint="J leaves the cursor on the space it added, so i: types the colon before it. . would only repeat the "
         "insert, so do the second pair the same way.",
    uses=["insert"],
)
join.add(
    title="Rewrap two lines", par=5, ext="txt",
    task='Move "the" down to the second line: line 1 should end with "over".',
    start=text("""
        The quick brown fox jumps over the
        lazy dog.
    """),
    target=text("""
        The quick brown fox jumps over
        the lazy dog.
    """),
    hint="Join the lines, then break them again one space further back: r<CR> turns a space into a line "
         "break.",
    uses=["f", "r"],
)
join.add(
    title="Rewrap a paragraph", par=7, ext="md",
    task='Rewrap the paragraph into two lines, the first ending with "focuses on".',
    start=text("""
        Neovim is a fork of Vim that
        focuses on extensibility and
        usability.
    """),
    target=text("""
        Neovim is a fork of Vim that focuses on
        extensibility and usability.
    """),
    hint="3J makes one line and leaves the cursor at the last place it joined. From there, the line break "
         "goes two spaces back.",
    uses=["count", "f", "r"],
)


# ---------- R ----------

replace_mode = drills.command(
    "replace-mode", "R", "Replace mode: type over text",
    """R starts Replace mode: each character you type overwrites the one under the cursor instead of
    pushing the rest of the line along, so the text after it stays in its column. <BS> steps back and
    restores the character you overwrote. Past the end of the line, typing just adds characters. <Esc>
    goes back to Normal mode, and . repeats the whole overwrite somewhere else. It's made for fixed-width
    text: columns, dates, ASCII art.""",
    examples=[("Rcarol<Esc>", "overwrite five characters with carol"), ("<BS>", "in Replace mode: put back the last character"),
              (".", "overwrite the same way again"), ("R-->", "draw an arrow over the text")],
    level="complex",
)
replace_mode.add(
    title="Fixed-width column", par=8, ext="txt",
    task="In the last row, the user should be carol. Keep the columns lined up.",
    start=text("""
        DATE        USER    ACTION
        2026-01-15  alice   login
        2026-01-15  bob     logout
    """),
    target=text("""
        DATE        USER    ACTION
        2026-01-15  alice   login
        2026-01-15  carol   logout
    """),
    hint="G goes to the last line and W jumps to the user. R types over characters instead of inserting, so "
         "carol covers bob and two of the spaces after it.",
    uses=["gg", "bigword"],
)
replace_mode.add(
    title="Busy now", par=11, ext="txt",
    task="Change the status from idle to running, and keep the box's right edge where it is.",
    start=text("""
        +-----------------+
        | Status: idle    |
        | Jobs:   0       |
        +-----------------+
    """),
    target=text("""
        +-----------------+
        | Status: running |
        | Jobs:   0       |
        +-----------------+
    """),
    hint="fi finds idle on line 2. In Replace mode, running types over idle and three of the spaces after it.",
    uses=["f"],
)
replace_mode.add(
    title="Wrong date", par=15, ext="txt",
    task="Both entries have the wrong date: change 2026-01-15 to 2025-12-31 on both lines.",
    start=text("""
        2026-01-15 09:30 deploy started
        2026-01-15 09:42 deploy finished
    """),
    target=text("""
        2025-12-31 09:30 deploy started
        2025-12-31 09:42 deploy finished
    """),
    hint="Only the part from the 6 on changes. Overwrite it with R, then go down, back to the 6, and . "
         "repeats the overwrite.",
    uses=["f", "dot"],
)
replace_mode.add(
    title="Open for business", par=9, ext="txt",
    task="Change the sign to OPEN, and keep its frame the same size: | OPEN   |.",
    start=text("""
        +--------+
        | CLOSED |
        +--------+
    """),
    target=text("""
        +--------+
        | OPEN   |
        +--------+
    """),
    hint="OPEN is two letters shorter than CLOSED, so type two spaces after it to cover the rest.",
    uses=["word"],
)
replace_mode.add(
    title="Busy server", par=6, ext="txt", cursor=(2, 1),
    task="nginx's CPU is now 12.0. Keep the MEM column where it is. The cursor is on nginx.",
    start=text("""
        NAME    CPU   MEM
        nginx   2.5   120M
        redis   0.3   64M
    """),
    target=text("""
        NAME    CPU   MEM
        nginx   12.0  120M
        redis   0.3   64M
    """),
    hint="12.0 is one character longer than 2.5. In Replace mode, the extra character covers one of the "
         "spaces instead of pushing 120M along.",
    uses=["word"],
)
replace_mode.add(
    title="Done with both", par=10, ext="txt", cursor=(2, 1),
    task="Mark tasks 1 and 2 as OK, keeping the TASK column lined up. The cursor is on the 1.",
    start=text("""
        ID  STATUS  TASK
        1   TODO    write
        2   TODO    test
        3   WIP     ship
    """),
    target=text("""
        ID  STATUS  TASK
        1   OK      write
        2   OK      test
        3   WIP     ship
    """),
    hint="R and OK with two spaces covers TODO. After <Esc> the cursor is on the last space you typed, so "
         "after j, b goes back to the start of the next TODO for the .",
    uses=["word", "dot"],
)
