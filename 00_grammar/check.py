"""Exercises for Project 00. Run:  python3 check.py   (python3 check.py 3 plays exercise 3)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "common"))
from trainer import Course, text  # noqa: E402

course = Course("Project 00 · The grammar: verbs, counts, and the dot", __file__,
                done_message="On to 01_motions, where you'll learn to get anywhere in a few keys.")

course.add(
    name="delete-words", title="Delete three words", par=5, ext="py",
    task="Delete \"very very very \" so the comment reads \"This is a long comment\".",
    start='# This is a very very very long comment',
    target='# This is a long comment',
    hint="Jump to the first \"very\" with f, then delete with d + a count + w.",
    uses=["d", "count", "word", "f"],
)
course.add(
    name="fix-operator", title="Fix the operator", par=5, ext="c",
    task="The function subtracts instead of adding. Change the - to a +.",
    start=text("""
        int add(int a, int b) {
            return a - b;
        }
    """),
    target=text("""
        int add(int a, int b) {
            return a + b;
        }
    """),
    hint="Move down a line, jump to the - with f, then replace that one character with r.",
    uses=["r", "f"],
)
course.add(
    name="swap-letters", title="Swap two letters", par=4, ext="py",
    task="Fix the typo: \"teh\" should be \"the\".",
    start='print("Fix teh typo")',
    target='print("Fix the typo")',
    hint="Two letters in the wrong order: delete one and put it back after its neighbor (x, then p).",
    uses=["x", "p", "f"],
)
course.add(
    name="move-line", title="Move a line down", par=3, ext="py",
    task="The steps are out of order. Move step_two() below step_one().",
    start=text("""
        step_two()
        step_one()
        step_three()
    """),
    target=text("""
        step_one()
        step_two()
        step_three()
    """),
    hint="Deleting a line also cuts it. Paste it back with p and it goes below the cursor's line.",
    uses=["dd", "p"],
)
course.add(
    name="change-to-end", title="Change the rest of the line", par=4, ext="py",
    task="Replace everything after \"retries = \" with 3.",
    start='retries = int(os.environ["RETRIES"])',
    target='retries = 3',
    hint="Move to the start of \"int\" with a counted w, then C changes from the cursor to the end of the line.",
    uses=["c", "word", "count"],
)
course.add(
    name="delete-to-char", title="Delete up to a character", par=6, ext="java",
    task="Remove the debug label so the line prints only the value.",
    start='System.out.println("Debug: value=" + value);',
    target='System.out.println(value);',
    hint="Jump to the opening quote, then delete up to (not including) a character with dt. "
         "There are two v's in the way, and t takes a count too.",
    uses=["d", "t", "count", "f"],
)
course.add(
    name="append-semicolons", title="Add the missing semicolons", par=7, ext="java",
    task="Add a semicolon to the end of all three lines.",
    start=text("""
        int width = 10
        int height = 20
        int area = width * height
    """),
    target=text("""
        int width = 10;
        int height = 20;
        int area = width * height;
    """),
    hint="A appends at the end of the line. After the first one, . repeats the whole change.",
    uses=["insert", "dot"],
)
course.add(
    name="indent-body", title="Indent the function body", par=3, ext="py",
    task="The two print lines should be indented inside the function.",
    start=text("""
        def greet(name):
        print("Hello")
        print(name)
    """),
    target=text("""
        def greet(name):
            print("Hello")
            print(name)
    """),
    hint="> is an operator like d. Give it a motion that covers this line and the next.",
    uses=["indent"],
)
course.add(
    name="join-array", title="Join an array onto one line", par=2, ext="c",
    task="Put the whole array literal on one line.",
    start=text("""
        int nums[] = {
            1,
            2,
            3
        };
    """),
    target='int nums[] = { 1, 2, 3 };',
    hint="J joins the next line onto this one (and tidies the spaces). It takes a count.",
    uses=["join", "count"],
)
course.add(
    name="space-after-commas", title="Space after every comma", par=11, ext="py",
    task="Add a space after each comma.",
    start='values = [1,2,3,4,5]',
    target='values = [1, 2, 3, 4, 5]',
    hint="Make the first change with f, and a. Then ; repeats the f-jump and . repeats the change.",
    uses=["f", "insert", "semicolon", "dot"],
)
course.add(
    name="underline-heading", title="Underline a heading", par=6, ext="md",
    task="Underline the heading with exactly 7 equals signs on a new line below it.",
    start='Results',
    target=text("""
        Results
        =======
    """),
    hint="A count works on inserts too: 3ix<Esc> types xxx. Open a new line first.",
    uses=["o", "count", "insert"],
)

course.add(
    name="review-wordcount", title="Review · Fix a word-count script", par=64, ext="py",
    task="Review: everything in this project at once. This script counts the words in a file, or would if "
         "it ran. Fix it, top to bottom. Par uses only what Project 00 teaches.",
    steps=[
        "Put import os above import sys.",
        "parse_args() is missing the colon at the end of its def line.",
        "The script takes exactly one argument: test len(argv) != 2.",
        "Indent the print into the if.",
        "The usage message should say PATH, not FILE.",
        "Exit with status 2, the usual one for a usage error.",
        "Delete the TODO comment, and the two spaces before it.",
        "Rename count_words to n_words.",
        "Delete the DEBUG print.",
        "len( is missing its closing parenthesis.",
        "main() calls count_words too: rename it there.",
        "Fix the typo paht.",
        "Join the print call onto one line.",
    ],
    start=text("""
        import sys
        import os

        def parse_args(argv)
            if len(argv) < 2:
            print("usage: wc.py FILE")
                sys.exit(1)
            return argv[1]  # TODO: check it exists

        def count_words(path):
            print("DEBUG: counting", path)
            with open(path) as f:
                text = f.read()
            return len(text.split()

        def main():
            path = parse_args(sys.argv)
            total = count_words(paht)
            print(path,
                  total,
                  "words")

        main()
    """),
    target=text("""
        import os
        import sys

        def parse_args(argv):
            if len(argv) != 2:
                print("usage: wc.py PATH")
                sys.exit(2)
            return argv[1]

        def n_words(path):
            with open(path) as f:
                text = f.read()
            return len(text.split())

        def main():
            path = parse_args(sys.argv)
            total = n_words(path)
            print(path, total, "words")

        main()
    """),
    hint="A, I, o and O start typing in the right place without moving there first, and r and R type over "
         "what's there. ct_ changes a name up to its underscore. . repeats only your last change, so do the "
         "second rename right after the first.",
    uses=["dd", "p", "insert", "c", "t", "indent", "replace-mode", "r", "dot", "join"],
)
course.add(
    name="review-readme", title="Review · Tidy a README", par=64, ext="md",
    task="Review: Project 00 on prose. The README of a small command-line tool renders badly: Markdown wants "
         "blank lines under headings, and shows lines indented four spaces as code. Fix it, top to bottom. "
         "Par uses only what Project 00 teaches.",
    steps=[
        "Add a blank line under the title.",
        "Join the description onto one line.",
        "Fix the typo in the Instal heading.",
        "Indent the pip command four spaces, so it shows as code.",
        "Add a blank line under ## Usage.",
        "Add todo list --all right below todo list (copy the line).",
        "The command is todo done, not todo remove.",
        "Indent the four usage commands.",
        "Delete (new in 1.2), and the space before it.",
        "Indent the three options.",
        "Line up the descriptions in one column, three spaces after the longest option, --color WHEN.",
    ],
    start=text("""
        # todo-cli
        A tiny todo list for the
        command line.

        ## Instal

        pip install todo-cli

        ## Usage
        todo add "buy milk"
        todo list
        todo remove 1

        ## Options

        --file PATH  where the list is kept (default: todo.txt)
        --quiet  print nothing but errors (new in 1.2)
        --color WHEN  always, never or auto
    """),
    target=text("""
        # todo-cli

        A tiny todo list for the command line.

        ## Install

            pip install todo-cli

        ## Usage

            todo add "buy milk"
            todo list
            todo list --all
            todo done 1

        ## Options

            --file PATH    where the list is kept (default: todo.txt)
            --quiet        print nothing but errors
            --color WHEN   always, never or auto
    """),
    hint="> takes a motion like any other operator, so one > can indent several lines. A count works on "
         "inserts: 3i<Space><Esc> types three spaces. And a count before . replaces the count of the change "
         "it repeats.",
    uses=["o", "join", "insert", "indent", "y", "c", "t", "d", "count", "dot"],
)

course.run()
