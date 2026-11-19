"""Exercises for Project 02. Run:  python3 check.py   (python3 check.py 3 plays exercise 3)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "common"))
from trainer import Course, text  # noqa: E402

course = Course("Project 02 · Text objects: act on the thing you're in", __file__,
                done_message="On to 03_operators, where every text object meets new verbs like = gU and gq.")

course.add(
    name="drop-word", title="Delete a word and its space", par=3, ext="py",
    task="Shorten the log message to \"Download finished\". The cursor is in the middle of successfully.",
    start='log.info("Download finished successfully")',
    target='log.info("Download finished")',
    cursor=(1, 33),
    hint="\"a word\" takes its surrounding space with it. When there's no space after the word, it takes "
         "the space before. Where in the word the cursor is doesn't matter.",
    uses=["iw", "d"],
)
course.add(
    name="drop-sentence", title="Delete a sentence", par=3, ext="md",
    task="Delete the second sentence, the one that starts with \"It started\".",
    start=text("""
        Neovim is a fork of Vim. It started in 2014
        and is written mostly in C and Lua. It adds a
        built-in terminal and an LSP client.
    """),
    target=text("""
        Neovim is a fork of Vim. It adds a
        built-in terminal and an LSP client.
    """),
    cursor=(2, 8),
    hint="A sentence is a text object, even when it spans lines. The \"around\" version takes the space "
         "after it too.",
    uses=["sentence", "d"],
)
course.add(
    name="drop-notes", title="Delete a paragraph", par=3, ext="py",
    task="Delete the scratch notes at the top, and the blank line after them.",
    start=text("""
        # scratch notes, delete before submitting:
        # try a heap instead of sorting
        # check the empty list case

        import heapq

        def top_k(xs, k):
            return heapq.nlargest(k, xs)
    """),
    target=text("""
        import heapq

        def top_k(xs, k):
            return heapq.nlargest(k, xs)
    """),
    cursor=(2, 3),
    hint="The notes are a paragraph: lines between blank lines. \"around\" a paragraph includes the "
         "blank lines after it.",
    uses=["ip", "d"],
)
course.add(
    name="change-prompt", title="Change a string", par=9, ext="py",
    task="Change the prompt to \"Name: \" (keep the space after the colon).",
    start='name = input("Enter your name: ")',
    target='name = input("Name: ")',
    hint="Change inside the quotes. You don't need to move first: when the cursor is before a string, "
         "the quote objects look ahead along the line for it.",
    uses=["quote", "c"],
)
course.add(
    name="change-host", title="Change a string from the middle", par=12, ext="py",
    task="Point the config at localhost: change 'db.internal' to 'localhost'. The cursor is on internal.",
    start="DB = {'host': 'db.internal', 'port': 5432}",
    target="DB = {'host': 'localhost', 'port': 5432}",
    cursor=(1, 21),
    hint="Single quotes have their own object. From inside the string, it doesn't matter how far you "
         "are from either quote.",
    uses=["quote", "c"],
)
course.add(
    name="shout-title", title="Uppercase a string", par=4, ext="java",
    task="Make the title string all capitals.",
    start=text("""
        class Game {
            static final String TITLE = "space invaders";
        }
    """),
    target=text("""
        class Game {
            static final String TITLE = "SPACE INVADERS";
        }
    """),
    cursor=(2, 1),
    hint="gU is an operator: it uppercases whatever you give it. Give it the inside of the quotes.",
    uses=["quote", "case"],
)
course.add(
    name="last-item", title="Change an index", par=5, ext="py",
    task="Use Python's negative indexing: change the index so the line reads last = scores[-1].",
    start='last = scores[len(scores) - 1]',
    target='last = scores[-1]',
    hint="Square brackets have a text object too, and like the others it looks ahead for the next "
         "[ when you're not inside one. The parentheses inside don't confuse it.",
    uses=["bracket", "c"],
)
course.add(
    name="copy-args", title="Copy the arguments", par=6, ext="py",
    task="Give scatter() the same arguments as plot().",
    start=text("""
        plot(xs, ys, color="red")
        scatter()
    """),
    target=text("""
        plot(xs, ys, color="red")
        scatter(xs, ys, color="red")
    """),
    hint="Yank inside the parentheses, wherever the cursor is on the line. Then put the text before "
         "the ) of scatter().",
    uses=["paren", "y", "line", "p"],
)
course.add(
    name="type-args", title="Change a generic type", par=6, ext="java",
    task="Change the list's element type to Row, so the line starts with List<Row>.",
    start='List<Map<String, Integer>> rows = load();',
    target='List<Row> rows = load();',
    hint="< and > form a pair with its own text object, and it counts nesting like ( and ) do.",
    uses=["angle", "c"],
)
course.add(
    name="outer-args", title="Change the outer arguments", par=10, ext="c",
    task="dx and dy are never negative anymore. Change max's arguments to plain dx, dy. The cursor is "
         "on dx.",
    start=text("""
        if (max(abs(dx), abs(dy)) <= range) {
            attack();
        }
    """),
    target=text("""
        if (max(dx, dy) <= range) {
            attack();
        }
    """),
    cursor=(1, 13),
    hint="The cursor is inside abs( ), which is inside max( ). A count on a bracket object reaches "
         "out that many levels.",
    uses=["nested", "paren", "c"],
)
course.add(
    name="stub-body", title="Replace a method body", par=10, ext="java",
    task="Replace the whole body of reset() with a single // TODO comment.",
    start=text("""
        void reset() {
            count = 0;
            total = 0;
            log("reset");
        }
    """),
    target=text("""
        void reset() {
            // TODO
        }
    """),
    cursor=(3, 5),
    hint="Change inside the braces. When the braces are on their own lines, the lines between are "
         "replaced and you start typing on a fresh, indented line.",
    uses=["brace", "c"],
)
course.add(
    name="paragraph-text", title="Change the text of a tag", par=16, ext="html",
    task="Replace the paragraph's text, bold part included, with: Start here.",
    start=text("""
        <div class="card">
          <h2>Welcome</h2>
          <p>Read the <b>full</b> guide first.</p>
        </div>
    """),
    target=text("""
        <div class="card">
          <h2>Welcome</h2>
          <p>Start here.</p>
        </div>
    """),
    hint="Get onto the paragraph's line. The inner tag object is everything between <p> and </p>, "
         "nested tags included, so ct< can't do this one.",
    uses=["tag", "c"],
)

course.add(
    name="review-signup", title="Review · Fix a sign-up form", par=70, ext="html",
    task="Review: Projects 00 to 02 together. This sign-up form needs a few fixes before launch. Par uses "
         "only what Projects 00 to 02 teach.",
    steps=[
        "A form that creates accounts must post: method=\"post\".",
        "Remove the <em> tags from the heading, but keep the word.",
        "Ask for the name first: move its label and input, with their blank line, up above the email ones.",
        "The label says Email, not E-mail.",
        "The email input is type=\"email\".",
        "The password input is type=\"password\".",
        "Delete the hint's middle sentence (Mix letters and numbers.).",
        "check() only takes the form: drop the false argument.",
    ],
    start=text("""
        <form action="/signup" method="get">
          <h2>Create an <em>account</em></h2>

          <label for="email">E-mail</label>
          <input id="email" type="text" name="email">

          <label for="pw">Password</label>
          <input id="pw" type="text" name="pw">

          <label for="name">Name</label>
          <input id="name" type="text" name="name">

          <p class="hint">Use at least 8 characters. Mix letters and numbers. Spaces are fine.</p>
          <button type="submit" onclick="check(this.form, false)">Sign up</button>
        </form>
    """),
    target=text("""
        <form action="/signup" method="post">
          <h2>Create an account</h2>

          <label for="name">Name</label>
          <input id="name" type="text" name="name">

          <label for="email">Email</label>
          <input id="email" type="email" name="email">

          <label for="pw">Password</label>
          <input id="pw" type="password" name="pw">

          <p class="hint">Use at least 8 characters. Spaces are fine.</p>
          <button type="submit" onclick="check(this.form)">Sign up</button>
        </form>
    """),
    hint="a< is a whole <...> tag, brackets included. ap is a block of lines plus the blank line after it. as "
         "is a sentence plus its space. And with smartcase, a search with a capital letter in it only finds "
         "capitals.",
    uses=["angle", "ip", "quote", "sentence", "search", "paragraph", "dot", "t", "x", "c"],
)
course.add(
    name="review-report", title="Review · Tidy a report script", par=65, ext="py",
    task="Review: Projects 00 to 02 together. This script prints a sales report from a CSV file. Bring it "
         "in line with the new data. Par uses only what Projects 00 to 02 teach.",
    steps=[
        "The report's title is now \"Q3\".",
        "Prices are in euros: \"EUR\".",
        "Delete the debug entry.",
        "The files are UTF-8: encoding=\"utf-8\".",
        "Nobody passes strict: delete it, and its comma.",
        "Move total() up, above render(), keeping two blank lines between the functions.",
        "float() ignores spaces around a number, but the filter should treat a cell of spaces as empty: move "
        ".strip() from the float() call to the end of the filter.",
        "Print the title as it is: no .upper().",
        "Print every row, the first one too: drop the [1:].",
    ],
    start=text("""
        DEFAULTS = {
            "title": "Monthly report",
            "currency": "USD",
            "rows": 50,
            "debug": True,
        }


        def load(path, encoding="latin-1", strict=False):
            with open(path, encoding=encoding) as f:
                return [line.split(",") for line in f]


        def render(rows, title):
            print("=" * 40)
            print(title.upper())
            for r in rows[1:]:
                print(r[0], r[2])
            print("Total:", total(rows))


        def total(rows, column=2):
            return sum(float(r[column].strip()) for r in rows if r[column])
    """),
    target=text("""
        DEFAULTS = {
            "title": "Q3",
            "currency": "EUR",
            "rows": 50,
        }


        def load(path, encoding="utf-8"):
            with open(path, encoding=encoding) as f:
                return [line.split(",") for line in f]


        def total(rows, column=2):
            return sum(float(r[column]) for r in rows if r[column].strip())


        def render(rows, title):
            print("=" * 40)
            print(title)
            for r in rows:
                print(r[0], r[2])
            print("Total:", total(rows))
    """),
    hint="i\" looks ahead along the line for the next string. At the end of a file, ap takes the blank lines "
         "above the paragraph instead of below. df) deletes through the next ), and what you delete can be "
         "put back somewhere else.",
    uses=["quote", "bracket", "ip", "replace-mode", "f", "d", "p", "dot", "line", "dd"],
)

course.run()
