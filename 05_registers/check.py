"""Exercises for Project 05. Run:  python3 check.py   (python3 check.py 3 plays exercise 3)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "common"))
from trainer import Course, text  # noqa: E402

course = Course("Project 05 · Registers: many clipboards, and math while you type", __file__,
                done_message="On to 06_macros, where you'll record keys once and replay them a thousand times.")

course.add(
    name="black-hole", title="Delete without losing your cut", par=9, ext="c",
    task="The return ended up at the top. Move it to the end of the function, "
         "and delete the debug printf.",
    start=text(r"""
        int sum(const int *a, int n) {
            return t;
            int t = 0;
            printf("n=%d\n", n);
            for (int i = 0; i < n; i++) t += a[i];
        }
    """),
    target=text(r"""
        int sum(const int *a, int n) {
            int t = 0;
            for (int i = 0; i < n; i++) t += a[i];
            return t;
        }
    """),
    hint="Cut the return line first. Then delete the printf into the black hole register (\"_), "
         "so the unnamed register still holds the return line when you paste.",
    uses=["blackhole", "dd", "p"],
)
course.add(
    name="swap-args", title="Swap the arguments", par=15, ext="java",
    task="JUnit wants assertEquals(expected, actual). Swap the two arguments.",
    start='assertEquals(cart.total(), 4200);',
    target='assertEquals(4200, cart.total());',
    hint="Cut the first argument. In Visual mode, p replaces the selection and puts the replaced "
         "text in the unnamed register, so selecting 4200 and pressing p hands you 4200 to paste.",
    uses=["visual", "p", "iw", "d", "t", "f", "word", "line"],
)
course.add(
    name="yank-register", title="Paste the yank, not the delete", par=15, ext="java",
    task="Replace each System.out.println with LOG.info, like the call on line 2.",
    start=text("""
        void run(Path path) {
            LOG.info("starting import");
            System.out.println("reading " + path);
            System.out.println("parsed " + path);
            System.out.println("done");
        }
    """),
    target=text("""
        void run(Path path) {
            LOG.info("starting import");
            LOG.info("reading " + path);
            LOG.info("parsed " + path);
            LOG.info("done");
        }
    """),
    hint="Yank LOG.info once. A change like ct( puts the deleted text in the unnamed register, "
         "but your yank is still in register 0: insert it with Ctrl-r 0. Then . repeats the change.",
    uses=["yank0", "ctrl-r", "c", "y", "t", "dot", "plus"],
)
course.add(
    name="reverse-close", title="Free in reverse order", par=9, ext="c",
    task="Clean up in the reverse order of creation: free(buf) first, then fclose(out), "
         "then fclose(in).",
    start=text("""
        FILE *in = fopen(src, "r");
        FILE *out = fopen(dst, "w");
        char *buf = malloc(4096);
        copy(in, out, buf);
        fclose(in);
        fclose(out);
        free(buf);
    """),
    target=text("""
        FILE *in = fopen(src, "r");
        FILE *out = fopen(dst, "w");
        char *buf = malloc(4096);
        copy(in, out, buf);
        free(buf);
        fclose(out);
        fclose(in);
    """),
    hint="Delete the first two cleanup lines with dd and . (they land in registers 1 and 2). "
         "\"1p puts back the newest one, and . after a numbered put moves on to the next register.",
    uses=["numbered", "dd", "dot", "count"],
)
course.add(
    name="collect-imports", title="Collect the imports", par=14, ext="py",
    task="Move every import to the top of the file, below import os, keeping their order.",
    start=text("""
        import os

        def load(path):
            with open(path) as f:
                return json.load(f)
        import json

        def stamp():
            return time.time()
        import time

        def home():
            return Path(os.environ["HOME"])
        from pathlib import Path
    """),
    target=text("""
        import os
        import json
        import time
        from pathlib import Path

        def load(path):
            with open(path) as f:
                return json.load(f)

        def stamp():
            return time.time()

        def home():
            return Path(os.environ["HOME"])
    """),
    hint="An uppercase register name appends: \"Add adds the line to register a. Find the next "
         "import with * or n, and . repeats the delete, still appending. Paste them all at once at the end.",
    uses=["append", "named", "star", "search", "dd", "dot", "gg", "p"],
)
course.add(
    name="class-name", title="Match the file name", par=9,
    task="Java wants a public class to live in a file of the same name. This file is "
         "Inventory.java: rename the class to match.",
    files={"Inventory.java": (
        text("""
            public class Main {
                private int[] stock = new int[10];

                public int count(int id) {
                    return stock[id];
                }
            }
        """),
        text("""
            public class Inventory {
                private int[] stock = new int[10];

                public int count(int id) {
                    return stock[id];
                }
            }
        """),
    )},
    hint="Vim already knows the file name: it's in the read-only register %. Put it in, then "
         "delete the leftover \".javaMain\".",
    uses=["readonly", "p", "word", "f", "d", "bigword"],
)
course.add(
    name="wrap-in-float", title="Wrap each argument", par=19, ext="py",
    task="sys.argv holds strings. Wrap each sys.argv[...] in float(...).",
    start=text("""
        import sys
        width = sys.argv[1]
        height = sys.argv[2]
        depth = sys.argv[3]
        print(width * height * depth)
    """),
    target=text("""
        import sys
        width = float(sys.argv[1])
        height = float(sys.argv[2])
        depth = float(sys.argv[3])
        print(width * height * depth)
    """),
    hint="Change the WORD and type float(, then Ctrl-r - to put back what you just deleted. "
         "Ctrl-r - is special: . re-reads the register, so it wraps whatever the repeat deletes.",
    uses=["small-delete", "ctrl-r", "c", "iw-big", "dot", "line"],
)
course.add(
    name="keep-old-name", title="Rename, but keep the old name", par=22, ext="py",
    task="Rename fetch_user to get_user, and add the line fetch_user = get_user at the end "
         "(after a blank line) so old callers keep working.",
    start=text("""
        def fetch_user(user_id):
            return db.get(user_id)
    """),
    target=text("""
        def get_user(user_id):
            return db.get(user_id)

        fetch_user = get_user
    """),
    hint="One cw leaves you two registers: \" holds the word you deleted, and . holds the text you "
         "typed. Insert both with Ctrl-r instead of typing the names again.",
    uses=["ctrl-r", "readonly", "c", "word", "gg", "o"],
)
course.add(
    name="rename-param", title="Rename from the command line", par=15, ext="py",
    task="The parameter is now called measurements. Rename every lst in the body to match.",
    start=text("""
        def normalize(measurements):
            lo, hi = min(lst), max(lst)
            span = hi - lo
            return [(x - lo) / span for x in lst]
    """),
    target=text("""
        def normalize(measurements):
            lo, hi = min(measurements), max(measurements)
            span = hi - lo
            return [(x - lo) / span for x in measurements]
    """),
    hint="Put the cursor on measurements and start a :%s. On the command line, Ctrl-r Ctrl-w "
         "inserts the word under the cursor, so you never type the long name.",
    uses=["ctrl-r-ctrl-w", "subst", "range", "word", "count"],
)
course.add(
    name="constants", title="Let Vim do the math", par=29, ext="java",
    task="Fill in each constant with the value of the formula in the comment above it. "
         "They're longs, so end each number with L.",
    start=text("""
        class Units {
            // 1024 * 1024 * 1024 * 1024
            static final long TERABYTE = ;
            // 1000 * 60 * 60 * 24 * 365
            static final long MS_PER_YEAR = ;
        }
    """),
    target=text("""
        class Units {
            // 1024 * 1024 * 1024 * 1024
            static final long TERABYTE = 1099511627776L;
            // 1000 * 60 * 60 * 24 * 365
            static final long MS_PER_YEAR = 31536000000L;
        }
    """),
    hint="Yank a formula, then in Insert mode press Ctrl-r = to open the expression prompt. "
         "Ctrl-r works there too: Ctrl-r 0 drops the yanked formula in, and Enter inserts the result.",
    uses=["expr", "yank0", "ctrl-r", "y", "f", "line", "insert", "word"],
)

course.add(
    name="review-weather-script", title="Review · Tidy a weather script", par=92,
    task="weather.py works, but its constants are scattered and main() calls fetch() wrong. Tidy it, top to "
         "bottom. This one reviews Projects 00 to 05: par uses only what they teach.",
    steps=[
        "The docstring lost the file name in front of its colon: put it back.",
        "Raise TIMEOUT to 30.",
        "The API moved to v2: change the 1 in BASE_URL's path.",
        "Move the BASE_URL line up under TIMEOUT, and delete the two extra blank lines it leaves, so "
        "functions stay two blank lines apart.",
        "Rename week_range to temp_range, in its def and in main().",
        "Rename the loop variable day to d, both times (data[\"days\"] stays).",
        "Delete the debug print.",
        "Round both temperatures: round(min(temps)), round(max(temps)).",
        "Move the UNITS line up under BASE_URL, again with the two extra blank lines.",
        "main() passes fetch() its arguments the wrong way round, and units isn't defined there: make it "
        "fetch(city, UNITS).",
    ],
    files={"weather.py": (
        text("""
            \"\"\": fetch a forecast and print the week's range of temperatures.\"\"\"
            import json
            import urllib.request

            TIMEOUT = 10


            def fetch(city, units):
                url = BASE_URL + "?q=" + city + "&units=" + units
                with urllib.request.urlopen(url, timeout=TIMEOUT) as r:
                    return json.load(r)


            BASE_URL = "https://api.example.com/v1/forecast"


            def week_range(data):
                temps = [day["temp"] for day in data["days"]]
                print("debug:", temps)
                return min(temps), max(temps)


            UNITS = "metric"


            def main(argv):
                city = argv[1]
                lo, hi = week_range(fetch(units, city))
                print(f"{city}: {lo} to {hi}")
        """),
        text("""
            \"\"\"weather.py: fetch a forecast and print the week's range of temperatures.\"\"\"
            import json
            import urllib.request

            TIMEOUT = 30
            BASE_URL = "https://api.example.com/v2/forecast"
            UNITS = "metric"


            def fetch(city, units):
                url = BASE_URL + "?q=" + city + "&units=" + units
                with urllib.request.urlopen(url, timeout=TIMEOUT) as r:
                    return json.load(r)


            def temp_range(data):
                temps = [d["temp"] for d in data["days"]]
                return round(min(temps)), round(max(temps))


            def main(argv):
                city = argv[1]
                lo, hi = temp_range(fetch(city, UNITS))
                print(f"{city}: {lo} to {hi}")
        """),
    )},
    hint="The file name is in the % register. A named register holds the BASE_URL line while you work, and "
         "the capital letter appends UNITS to it, so one put brings both up. Ctrl-r - plus . wraps both "
         "calls in round(). In main(), gU, then dt, and a Visual p swap the arguments.",
    uses=["readonly", "named", "append", "small-delete", "ctrl-r", "star", "replace-mode", "case", "visual",
          "increment"],
)
course.add(
    name="review-upload-config", title="Review · Fix an upload config", par=83,
    task="Someone wrote this config with arithmetic in it, and YAML doesn't do arithmetic. Fix that and the "
         "rest of the review. This one reviews Projects 00 to 05: par uses only what they teach.",
    steps=[
        "The comment lost the file name in front of its colon: put it back.",
        "Bump the image to 2.7.2.",
        "replicas isn't a limit: move it to the top level, in place of debug: true, which goes.",
        "Scale to 4 replicas.",
        "Replace max_body_bytes's formula with its value.",
        "And memory_bytes's.",
        "keep_ms and sweep_every_ms got each other's formulas: swap them.",
        "Replace both retention formulas with their values.",
        "UPLOAD_MAX_BYTES must match max_body_bytes: give it the same value.",
        "Production logs at info, not debug.",
    ],
    files={"uploads.yaml": (
        text("""
            # : upload service, production
            service: uploads
            image: registry.example.com/uploads:2.7.1
            debug: true

            limits:
              max_body_bytes: 25 * 1024 * 1024
              memory_bytes: 6 * 1024 * 1024 * 1024
              replicas: 2

            retention:
              keep_ms: 6 * 60 * 60 * 1000
              sweep_every_ms: 30 * 24 * 60 * 60 * 1000

            env:
              UPLOAD_MAX_BYTES:
              LOG_LEVEL: debug
        """),
        text("""
            # uploads.yaml: upload service, production
            service: uploads
            image: registry.example.com/uploads:2.7.2
            replicas: 4

            limits:
              max_body_bytes: 26214400
              memory_bytes: 6442450944

            retention:
              keep_ms: 2592000000
              sweep_every_ms: 21600000

            env:
              UPLOAD_MAX_BYTES: 26214400
              LOG_LEVEL: info
        """),
    )},
    hint="C cuts a formula into the small delete register, and in Insert mode Ctrl-r = then Ctrl-r - "
         "evaluates it. For the swap, keep one formula in a named register and evaluate each where the other "
         "was. Yank the first value right after you make it, and Ctrl-r 0 puts it in the env at the end.",
    uses=["expr", "small-delete", "named", "ctrl-r", "yank0", "readonly", "visual-line", "increment", "indent",
          "iw-big"],
)

course.run()
