"""Exercises for Project 08. Run:  python3 check.py   (python3 check.py 3 plays exercise 3)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "common"))
from trainer import Course, text  # noqa: E402

# Completion (Ctrl-n, Ctrl-x Ctrl-l) normally also searches other windows, which would let you copy
# lines straight out of the target. In these exercises it only searches your own file.
OWN_FILE_ONLY = ["setlocal complete=."]

course = Course("Project 08 · Insert and command-line mode: fix it without leaving", __file__,
                done_message="On to 09_many_files, where one command changes a whole project.")

course.add(
    name="replace-last-word", title="Replace the last word", par=17, setup=OWN_FILE_ONLY, ext="py",
    task="Use the usual short aliases: numpy as np, pandas as pd, and matplotlib.pyplot as plt.",
    start=text("""
        import numpy as numpy
        import pandas as pandas
        import matplotlib.pyplot as pyplot
    """),
    target=text("""
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
    """),
    hint="Each alias is the last word on its line. In Insert mode, Ctrl-w deletes the word before the "
         "cursor, so you can append, delete and retype in one go.",
    uses=["ctrl-w", "insert"],
)
course.add(
    name="comment-leader", title="Code after a comment", par=23, setup=OWN_FILE_ONLY, ext="c",
    task="Add the line int fd = open_dev(); right below the comment \"open the device\".",
    start=text("""
        void run(void) {
            // open the device
            // then read its config
            load_config(fd);
        }
    """),
    target=text("""
        void run(void) {
            // open the device
            int fd = open_dev();
            // then read its config
            load_config(fd);
        }
    """),
    hint="A new line next to a comment starts with the comment leader \"// \". Ctrl-u (or Ctrl-w) "
         "wipes it without leaving Insert mode.",
    uses=["ctrl-w", "o"],
)
course.add(
    name="indent-as-you-type", title="Indent as you type", par=9, setup=OWN_FILE_ONLY, ext="c",
    task="Indent the three strings and put a comma after each one. (Without the commas, C glues them "
         "into one string.)",
    start=text("""
        const char *colors[] = {
        "red"
        "green"
        "blue"
        };
    """),
    target=text("""
        const char *colors[] = {
            "red",
            "green",
            "blue",
        };
    """),
    hint="Ctrl-t indents the current line from anywhere in it, without leaving Insert mode. Because it's "
         "part of the insert, . repeats it along with the text.",
    uses=["ctrl-t", "insert", "dot"],
)
course.add(
    name="one-normal-command", title="One Normal command", par=9, setup=OWN_FILE_ONLY, ext="java",
    task="Fix the precedence bug: the function should divide the sum of sum and extra by count.",
    start=text("""
        int average(int sum, int extra, int count) {
            return sum + extra / count;
        }
    """),
    target=text("""
        int average(int sum, int extra, int count) {
            return (sum + extra) / count;
        }
    """),
    hint="After typing the (, Ctrl-o runs one Normal-mode command, like a motion, and drops you back "
         "into Insert mode wherever it lands.",
    uses=["ctrl-o", "f", "t", "insert"],
)
course.add(
    name="do-the-math", title="Do the math", par=17, setup=OWN_FILE_ONLY, ext="c",
    task="FRAME_BYTES should be the size of one frame: 1920 x 1080 pixels at 4 bytes each. Replace the "
         "0 with that number.",
    start=text("""
        /* one 1920x1080 frame, 4 bytes per pixel */
        #define FRAME_BYTES 0

        static unsigned char framebuffer[FRAME_BYTES];
    """),
    target=text("""
        /* one 1920x1080 frame, 4 bytes per pixel */
        #define FRAME_BYTES 8294400

        static unsigned char framebuffer[FRAME_BYTES];
    """),
    hint="No calculator needed: in Insert mode, Ctrl-r = asks for an expression and inserts its value.",
    uses=["expr", "line", "c"],
)
course.add(
    name="complete-names", title="Complete long names", par=14, setup=OWN_FILE_ONLY, ext="java",
    task="Make start() call initializeConnectionPool() and then registerShutdownHooks(), one per line.",
    cursor=(5, 1),
    start=text("""
        class Server {
            void registerShutdownHooks() { }
            void initializeConnectionPool() { }

            void start() {
            }
        }
    """),
    target=text("""
        class Server {
            void registerShutdownHooks() { }
            void initializeConnectionPool() { }

            void start() {
                initializeConnectionPool();
                registerShutdownHooks();
            }
        }
    """),
    hint="Type the first two letters of a name and press Ctrl-n (or Ctrl-p): Vim completes it from the "
         "words already in the file.",
    uses=["complete", "o"],
)
course.add(
    name="complete-line", title="Complete a whole line", par=21, setup=OWN_FILE_ONLY, ext="c",
    task="Implement parse_config at the end of the file: its header line is the prototype with { instead "
         "of ;, the body is return 0;, and a blank line separates it from usage().",
    cursor=(7, 1),
    start=text("""
        #include <stdio.h>

        int parse_config(const char *path, int *out);

        static void usage(void) {
            puts("usage: app CONFIG");
        }
    """),
    target=text("""
        #include <stdio.h>

        int parse_config(const char *path, int *out);

        static void usage(void) {
            puts("usage: app CONFIG");
        }

        int parse_config(const char *path, int *out) {
            return 0;
        }
    """),
    hint="Ctrl-x Ctrl-l completes a whole line: type the start of a line that exists somewhere above, and "
         "Vim fills in the rest. Then keep typing.",
    uses=["line-complete", "o"],
)
course.add(
    name="literal-tab", title="A real tab", par=21, setup=OWN_FILE_ONLY, ext="tsv",
    task="Add a row for Java, created by Gosling in 1995. In this TSV file the fields are separated by "
         "real tab characters, but expandtab is on, so Tab types spaces.",
    start=text("""
        language\tcreator\tyear
        C\tRitchie\t1972
        Python\tvan Rossum\t1991
    """),
    target=text("""
        language\tcreator\tyear
        C\tRitchie\t1972
        Python\tvan Rossum\t1991
        Java\tGosling\t1995
    """),
    hint="Ctrl-v in Insert mode inserts the next key literally, so Ctrl-v Tab is a real tab whatever "
         "expandtab says.",
    uses=["literal", "gg", "o"],
)
course.add(
    name="draw-a-box", title="Draw a box", par=26, setup=OWN_FILE_ONLY, ext="txt",
    task="Draw a box around the label with box-drawing characters: corners and 8 horizontal lines on the "
         "top and bottom.",
    start="│ NEOVIM │",
    target=text("""
        ┌────────┐
        │ NEOVIM │
        └────────┘
    """),
    hint="Ctrl-k types a digraph: two letters for one special character. Box pieces are named after where "
         "their lines go: hh is ─, and dr is the corner with lines going down and right. A count before "
         "an insert, and ., save the rest.",
    uses=["digraph", "o", "count", "dot"],
)
course.add(
    name="word-under-cursor", title="The word under the cursor", par=16, setup=OWN_FILE_ONLY, ext="java",
    task="The field was renamed to retryCount, but the methods still say attempts. Update them. "
         "(The cursor starts on the new name.)",
    cursor=(2, 17),
    start=text("""
        class Retry {
            private int retryCount;

            void reset() { attempts = 0; }
            void bump() { attempts++; }
            boolean done() { return attempts >= 3; }
            int left() { return 3 - attempts; }
            String show() { return "tries: " + attempts; }
        }
    """),
    target=text("""
        class Retry {
            private int retryCount;

            void reset() { retryCount = 0; }
            void bump() { retryCount++; }
            boolean done() { return retryCount >= 3; }
            int left() { return 3 - retryCount; }
            String show() { return "tries: " + retryCount; }
        }
    """),
    hint="On the command line, Ctrl-r Ctrl-w inserts the word under the cursor. It works in the "
         "replacement part of :s too.",
    uses=["ctrl-r-ctrl-w", "subst", "range"],
)
course.add(
    name="repeat-ex-command", title="Repeat an Ex command", par=24, setup=OWN_FILE_ONLY, ext="py",
    task="Change the prints in load() and save() to log.debug. show() prints real output, so leave its "
         "prints alone.",
    start=text("""
        def load(path):
            print("loading", path)
            data = read(path)
            print("loaded", len(data))
            return data


        def show(data):
            print("rows:", len(data))
            print("first:", data[0])


        def save(data, path):
            print("saving", path)
            write(path, data)
            print("saved")
    """),
    target=text("""
        def load(path):
            log.debug("loading", path)
            data = read(path)
            log.debug("loaded", len(data))
            return data


        def show(data):
            print("rows:", len(data))
            print("first:", data[0])


        def save(data, path):
            log.debug("saving", path)
            write(path, data)
            log.debug("saved")
    """),
    hint="Fix load() with one :s on a range relative to the cursor. Then move to save(): @: repeats the "
         "last Ex command, and a relative range is measured from wherever the cursor is now.",
    uses=["at-colon", "subst", "range"],
)
course.add(
    name="command-window", title="Edit an old command", par=15, ext="log",
    task="The ERROR lines were already reformatted as \"[ERROR] time message\" by a :s that's in your "
         "command history. Do the same to the WARN lines.",
    setup=OWN_FILE_ONLY + [r"call histadd(':', '%s/\v^(\S+) ERROR +/[ERROR] \1 /')"],
    start=text("""
        [ERROR] 09:14:05 could not open config.yml
        09:15:11 INFO  cache warmed
        09:16:40 WARN  disk 91% full
        [ERROR] 09:17:02 connection refused
        09:18:30 WARN  slow query (2.3 s)
    """),
    target=text("""
        [ERROR] 09:14:05 could not open config.yml
        09:15:11 INFO  cache warmed
        [WARN] 09:16:40 disk 91% full
        [ERROR] 09:17:02 connection refused
        [WARN] 09:18:30 slow query (2.3 s)
    """),
    hint="Retyping that :s is a lot of keys. The command-line window shows your history as ordinary text: "
         "edit the old command with Normal-mode keys and press <CR> to run it.",
    uses=["cmdwin", "f", "c", "semicolon", "dot"],
)

course.add(
    name="review-thumbs-cli", title="Review · Finish the thumbnail tool", par=135, setup=OWN_FILE_ONLY,
    ext="py",
    task="thumbs.py makes thumbnails for a folder of images. Finish it. This reviews Projects 00 to 08: "
         "par uses nothing from later projects.",
    steps=[
        "Fix the typo in the docstring.",
        "Allow 4K images: MAX_WIDTH 3840 and MAX_HEIGHT 2160.",
        "FRAME_BYTES is the size of one frame at that size, 4 bytes per pixel. Replace the 0 with the "
        "number.",
        "The name says it all: delete the comment after it.",
        "Show a real multiplication sign in the --size help: WIDTH×HEIGHT.",
        "--verbose can also be written -v: add \"-v\" as the first name.",
        "Fix the typo in store_true.",
        "parse_size() returns numbers: int(width), int(height).",
        "fits() checks the height too: width <= MAX_WIDTH and height <= MAX_HEIGHT.",
        "And nothing fits with a size of 0: 0 < width <= MAX_WIDTH, and the same for the height.",
        "scale() never makes an image bigger: add 1 as the last value min() picks from.",
        "Rename factor to ratio in scale().",
    ],
    start=text("""
        #!/usr/bin/env python3
        """ + '"""thumbs: make thumbanils for a folder of images."""' + """
        import argparse

        MAX_WIDTH = 1920
        MAX_HEIGHT = 1080
        FRAME_BYTES = 0  # one RGBA frame at the largest size


        def parse_args():
            parser = argparse.ArgumentParser(description="Make thumbnails.")
            parser.add_argument("folder")
            parser.add_argument("--size", default="320x240", help="largest thumbnail, WIDTHxHEIGHT")
            parser.add_argument("--verbose", action="store_ture")
            return parser.parse_args()


        def parse_size(text):
            width, height = text.split("x")
            return width, height


        def fits(width, height):
            return width <= MAX_WIDTH


        def scale(width, height, max_width, max_height):
            factor = min(max_width / width, max_height / height)
            return round(width * factor), round(height * factor)
    """),
    target=text("""
        #!/usr/bin/env python3
        """ + '"""thumbs: make thumbnails for a folder of images."""' + """
        import argparse

        MAX_WIDTH = 3840
        MAX_HEIGHT = 2160
        FRAME_BYTES = 33177600


        def parse_args():
            parser = argparse.ArgumentParser(description="Make thumbnails.")
            parser.add_argument("folder")
            parser.add_argument("--size", default="320x240", help="largest thumbnail, WIDTH×HEIGHT")
            parser.add_argument("-v", "--verbose", action="store_true")
            return parser.parse_args()


        def parse_size(text):
            width, height = text.split("x")
            return int(width), int(height)


        def fits(width, height):
            return 0 < width <= MAX_WIDTH and 0 < height <= MAX_HEIGHT


        def scale(width, height, max_width, max_height):
            ratio = min(max_width / width, max_height / height, 1)
            return round(width * ratio), round(height * ratio)
    """),
    hint="Ctrl-r = works out the frame size for you, and Ctrl-k types the × (and r takes a digraph too). "
         "Ctrl-n and Ctrl-p complete names already in the file. Ctrl-o runs one Normal command and drops "
         "you back in Insert mode, handy for typing around a word.",
    uses=["expr", "digraph", "complete", "ctrl-o", "increment", "insert", "star", "dot", "f"],
)

course.add(
    name="review-changelog", title="Review · Release notes", par=117, ext="md",
    task="CHANGELOG.md needs to be ready for today's 2.4.0 release. Last release, you turned the issue "
         "numbers into links with a :s that's still in your command history, but the repository has been "
         "renamed from acme/ledger to acme/tally since. This reviews Projects 00 to 08: par uses nothing "
         "from later projects.",
    setup=OWN_FILE_ONLY + [r"call histadd(':', '%s/(#\(\d\+\))/([#\1](https:\/\/github.com\/acme\/ledger\/issues\/\1))/')"],
    steps=[
        "2.4.0 is out today: its date is 2024-06-14.",
        "Put the shortcut in backticks, as code: `Ctrl+K`.",
        "Spell José García with its accents.",
        "The app calls it Dark theme, not Dark mode.",
        "Sort the Added entries alphabetically.",
        "0×0 with a real multiplication sign.",
        "Temperatures are in °F and °C.",
        "2.3.1 came out on May 20: fix its date.",
        "The startup crash was the bigger fix in 2.3.1: list it first.",
        "The resize crash fix was backported to 2.3.1: add the same entry at the end of 2.3.1's list.",
        "Every entry ends with a period.",
        "Link the issue numbers as last release, to the renamed repository.",
    ],
    start=text("""
        # Changelog

        ## 2.4.0 - unreleased

        ### Added
        - Shortcut for search: Ctrl+K
        - Export to CSV, thanks to Jose Garcia
        - Dark mode

        ### Fixed
        - Crash when the window is resized to 0x0 (#412)
        - Temperatures shown in F when the locale uses C (#398)

        ## 2.3.1 - 2024-05-02

        ### Fixed
        - Login fails when the password contains a space (#377)
        - Crash on startup without a network (#381)
    """),
    target=text("""
        # Changelog

        ## 2.4.0 - 2024-06-14

        ### Added
        - Dark theme.
        - Export to CSV, thanks to José García.
        - Shortcut for search: `Ctrl+K`.

        ### Fixed
        - Crash when the window is resized to 0×0 ([#412](https://github.com/acme/tally/issues/412)).
        - Temperatures shown in °F when the locale uses °C ([#398](https://github.com/acme/tally/issues/398)).

        ## 2.3.1 - 2024-05-20

        ### Fixed
        - Crash on startup without a network ([#381](https://github.com/acme/tally/issues/381)).
        - Login fails when the password contains a space ([#377](https://github.com/acme/tally/issues/377)).
        - Crash when the window is resized to 0×0 ([#412](https://github.com/acme/tally/issues/412)).
    """),
    hint="Ctrl-k types the special characters, and r takes a digraph too. Ctrl-x Ctrl-l copies the "
         "backported line as you type it. One :g adds every period. And instead of retyping the long :s, "
         "open your history with q:, fix the repository's name and run it again.",
    uses=["cmdwin", "digraph", "ctrl-w", "ctrl-o", "line-complete", "global", "sort", "r", "dd", "p"],
)

course.run()
