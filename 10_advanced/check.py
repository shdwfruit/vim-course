"""Exercises for Project 10. Run:  python3 check.py   (python3 check.py 3 plays exercise 3)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "common"))
from trainer import Course, text  # noqa: E402

course = Course("Project 10 · Advanced: real files, many edits, fewest keys", __file__,
                done_message="You've finished the course. See \"After the course\" in ../ROADMAP.md for what to "
                             "learn next.")

course.add(
    name="merge-conflicts",
    title="Resolve a merge",
    par=66,
    ext="py",
    task="git merge feature-branch stopped with four conflicts in orders.py. Resolve them as decided "
         "below, then fix what the merge broke. No conflict marker may survive.",
    steps=[
        "Imports hunk: keep both sides, HEAD's lines first.",
        "Then delete the second import os.",
        "And sort the import lines alphabetically.",
        "Loader hunk: keep feature-branch's side, the read_orders() version.",
        "export(): open the file with encoding=\"utf-8\" too, after newline=\"\", as read_orders() does.",
        "export() hunk: keep feature-branch's csv.writer line.",
        "main() still calls load_orders(), which feature-branch renamed: call read_orders().",
        "main() hunk: keep HEAD's two logging lines, then feature-branch's total line.",
        "Wrap that total in round(..., 2), as HEAD's line did.",
        "export() now defaults to \"orders.csv\": drop that argument from the last line.",
    ],
    start=text("""
        import json
        <<<<<<< HEAD
        import os
        import logging
        =======
        import os
        import csv
        >>>>>>> feature-branch


        <<<<<<< HEAD
        def load_orders(path):
            with open(path) as f:
        =======
        def read_orders(path):
            with open(path, encoding="utf-8") as f:
        >>>>>>> feature-branch
                return json.load(f)


        def export(orders, path="orders.csv"):
            with open(path, "w", newline="") as f:
        <<<<<<< HEAD
                json.dump(orders, f)
        =======
                csv.writer(f).writerows(o.values() for o in orders)
        >>>>>>> feature-branch


        def main():
            orders = load_orders(os.environ["ORDERS"])
        <<<<<<< HEAD
            log = logging.getLogger(__name__)
            log.info("loaded %d orders", len(orders))
            total = round(sum(o["price"] for o in orders), 2)
        =======
            print("loaded", len(orders), "orders")
            total = sum(o["price"] * o["qty"] for o in orders)
        >>>>>>> feature-branch
            export(orders, "orders.csv")
            log.info("total: %.2f", total)
    """),
    target=text("""
        import csv
        import json
        import logging
        import os


        def read_orders(path):
            with open(path, encoding="utf-8") as f:
                return json.load(f)


        def export(orders, path="orders.csv"):
            with open(path, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerows(o.values() for o in orders)


        def main():
            orders = read_orders(os.environ["ORDERS"])
            log = logging.getLogger(__name__)
            log.info("loaded %d orders", len(orders))
            total = round(sum(o["price"] * o["qty"] for o in orders), 2)
            export(orders)
            log.info("total: %.2f", total)
    """),
    hint=":sort u sorts and drops duplicates, and after it | can chain a :g that deletes every conflict marker "
         "in the file at once. Then only the unwanted sides are left: work bottom-up, and yank what you need "
         "from the other side instead of typing it.",
    uses=["sort", "global", "dd", "count", "y", "p", "replace-mode", "f"],
)

course.add(
    name="compose-config", title="Review a docker-compose file", par=83, ext="yml",
    task="docker-compose.yml needs a round of fixes before the next deploy. Apply the review, top to "
         "bottom.",
    steps=[
        "Delete the obsolete version: line and the blank line under it.",
        "Bump nginx to 1.27.",
        "Make web's filesystem read-only: read_only: true.",
        "Rename the api service to backend, and both references to it in web. build: ./api stays.",
        "Turn DEBUG off.",
        "YAML reads PYTHON_VERSION: 3.10 as the number 3.1: quote the value.",
        "YAML 1.1 reads BACKUP_AT: 08:00 as a number of minutes: quote that value too.",
        "Publish backend on host port 5001 (macOS AirPlay already listens on 5000).",
        "Bump postgres to 16.",
        "POSTGRES_USER and POSTGRES_PASSWORD belong under environment: indent them one level.",
        "Add POSTGRES_DB: app right below POSTGRES_USER (copy that line).",
        "In cache, put image: before command:.",
        "Bump redis to 7.4.",
    ],
    start=text("""
        version: "3.8"

        services:
          web:
            image: nginx:1.25
            ports:
              - "8080:80"
            environment:
              UPSTREAM: http://api:5000
            read_only: false
            depends_on:
              - api

          api:
            build: ./api
            environment:
              DEBUG: true
              PYTHON_VERSION: 3.10
              BACKUP_AT: 08:00
              DATABASE_URL: postgres://app:secret@db/app
            ports:
              - "5000:5000"
            depends_on:
              - db

          db:
            image: postgres:14
            environment:
            POSTGRES_USER: app
            POSTGRES_PASSWORD: secret
            volumes:
              - pgdata:/var/lib/postgresql/data

          cache:
            command: redis-server --appendonly yes
            image: redis:7.0

        volumes:
          pgdata:
    """),
    target=text("""
        services:
          web:
            image: nginx:1.27
            ports:
              - "8080:80"
            environment:
              UPSTREAM: http://backend:5000
            read_only: true
            depends_on:
              - backend

          backend:
            build: ./api
            environment:
              DEBUG: false
              PYTHON_VERSION: "3.10"
              BACKUP_AT: "08:00"
              DATABASE_URL: postgres://app:secret@db/app
            ports:
              - "5001:5000"
            depends_on:
              - db

          db:
            image: postgres:16
            environment:
              POSTGRES_USER: app
              POSTGRES_DB: app
              POSTGRES_PASSWORD: secret
            volumes:
              - pgdata:/var/lib/postgresql/data

          cache:
            image: redis:7.4
            command: redis-server --appendonly yes

        volumes:
          pgdata:
    """),
    hint="ciw then . renames the references one by one and leaves ./api alone. ciW\"<C-r>-\" quotes a "
         "value, and . quotes the next one: the Ctrl-r - is replayed with the new deletion. true and false "
         "just trade places, and p in Visual mode swaps the text it replaces into the register. Ctrl-a "
         "takes counts, and looks for the number at or after the cursor.",
    uses=["increment", "dot", "iw", "visual", "ctrl-r", "small-delete", "indent", "dd", "p"],
)

course.add(
    name="ascii-architecture",
    title="Redraw the architecture",
    par=101,
    ext="txt",
    task="The checkout architecture changed. Bring the ASCII diagram up to date without breaking its "
         "columns: every box and arrow that doesn't change must stay exactly where it is.",
    steps=[
        "Bump the revision in the top right corner to rev 3.",
        "Make the ==== underline as long as the title.",
        "The cache box is gone: erase it and its arrow (the cdn box doesn't move).",
        "The top border of the cdn box ends one column early. Move its right + over by one.",
        "We replaced the CDN with our own proxy: relabel cdn to edge, in the same box.",
        "gRPC labels the wrong link. Move it down to the gap under the gateway-to-orders arrow, same columns.",
        "The gateway calls auth, not the other way round: flip that arrow to <----.",
        "orders was rewritten: widen its box by four columns, on the right side.",
        "Label it orders (v2), centred: |  orders (v2)  |.",
        "Relabel mysql to postgres in the same box: | postgres  |.",
        "Add a replica box under postgres: a copy of its arrow and box, with a dotted arrow (:) and |  replica  |.",
    ],
    start=text("""
        Checkout request path                                 rev 2
        ===============

                          +------------+
                          |  browser   |
                          +------------+
                                |
                                | https
                                v
        +-----------+     +-----------+           +-----------+
        |   cache   |<----|    cdn     |--------->|  assets   |
        +-----------+     +------------+   gRPC   +-----------+
                                |
                                v
        +-----------+     +------------+          +-----------+
        |   auth    |---->|  gateway   |--------->|  orders   |
        +-----------+     +------------+          +-----------+
                                                        |
                                                        v
                                                  +-----------+
                                                  |   mysql   |
                                                  +-----------+

        Legend:  --->  request      :  async replication
        Owner:   team-checkout (#checkout-oncall)
    """),
    target=text("""
        Checkout request path                                 rev 3
        =====================

                          +------------+
                          |  browser   |
                          +------------+
                                |
                                | https
                                v
                          +------------+          +-----------+
                          |    edge    |--------->|  assets   |
                          +------------+          +-----------+
                                |
                                v
        +-----------+     +------------+          +---------------+
        |   auth    |<----|  gateway   |--------->|  orders (v2)  |
        +-----------+     +------------+   gRPC   +---------------+
                                                        |
                                                        v
                                                  +-----------+
                                                  | postgres  |
                                                  +-----------+
                                                        :
                                                        v
                                                  +-----------+
                                                  |  replica  |
                                                  +-----------+

        Legend:  --->  request      :  async replication
        Owner:   team-checkout (#checkout-oncall)
    """),
    hint="R types over characters without moving the rest of the line, Visual block r<Space> erases a "
         "rectangle, and a one-column block yank pasted with a count widens a box. Compare whole lines "
         "too: some lines you need already exist elsewhere, and Vp leaves the line it replaced in the "
         "register.",
    uses=["increment", "count", "block-edit", "r", "replace-mode", "visual-line", "y", "p", "paragraph"],
)

course.add(
    name="c-prototypes",
    title="Declare before use",
    par=106,
    ext="c",
    task="vec.c doesn't compile: main() calls functions that are only defined further down. "
         "Fix that, and apply the rest of the review.",
    steps=[
        "struct vec fits on one line: join it.",
        "Above main, add prototypes for the four vec_ functions: each definition line plus ;, in file order.",
        "main: a and b never change. Make them const.",
        "main: vec_dot and vec_len return double. Print them with %g, not %d.",
        "main: rename d to delta.",
        "vec_sub was copied from an add: make it subtract, in both components.",
        "vec_dot: the last term multiplies a.y by itself. It should be a.y * b.y.",
        "vec_print: x and y are doubles too. %g, not %d.",
        "The helpers sq and round2 are used before they're defined: move both up between main and vec_sub.",
        "Make sq and round2 static: they're private to this file.",
        "Rename the vec_ prefix to vector_ on every function, prototype and call (struct vec keeps its name).",
    ],
    start=text("""
        #include <math.h>
        #include <stdio.h>

        struct vec {
            double x, y;
        };

        int main(void)
        {
            struct vec a = {3, 4}, b = {1, 2};
            struct vec d = vec_sub(a, b);
            printf("%d %d\\n", vec_dot(a, b), vec_len(d));
            vec_print(d);
        }

        struct vec vec_sub(struct vec a, struct vec b)
        {
            return (struct vec){a.x + b.x, a.y + b.y};
        }

        double vec_dot(struct vec a, struct vec b)
        {
            return a.x * b.x + a.y * a.y;
        }

        double vec_len(struct vec v)
        {
            return sqrt(sq(v.x) + sq(v.y));
        }

        void vec_print(struct vec v)
        {
            printf("(%d, %d)\\n", round2(v.x), round2(v.y));
        }

        double sq(double x) { return x * x; }
        double round2(double x) { return round(x * 100) / 100; }
    """),
    target=text("""
        #include <math.h>
        #include <stdio.h>

        struct vec { double x, y; };

        struct vec vector_sub(struct vec a, struct vec b);
        double vector_dot(struct vec a, struct vec b);
        double vector_len(struct vec v);
        void vector_print(struct vec v);

        int main(void)
        {
            const struct vec a = {3, 4}, b = {1, 2};
            struct vec delta = vector_sub(a, b);
            printf("%g %g\\n", vector_dot(a, b), vector_len(delta));
            vector_print(delta);
        }

        static double sq(double x) { return x * x; }
        static double round2(double x) { return round(x * 100) / 100; }

        struct vec vector_sub(struct vec a, struct vec b)
        {
            return (struct vec){a.x - b.x, a.y - b.y};
        }

        double vector_dot(struct vec a, struct vec b)
        {
            return a.x * b.x + a.y * b.y;
        }

        double vector_len(struct vec v)
        {
            return sqrt(sq(v.x) + sq(v.y));
        }

        void vector_print(struct vec v)
        {
            printf("(%g, %g)\\n", round2(v.x), round2(v.y));
        }
    """),
    hint="One :g can build all four prototypes: what do the four definition lines end with that main "
         "and the calls don't? Copy each one below the '[ mark (the start of the last change) so they stay in "
         "order, and save the renames for the end, chained with | on one command line.",
    uses=["join", "global", "copy-move", "marks", "subst", "dot", "paragraph", "ip", "count"],
)

course.add(
    name="readme-cleanup", title="Tidy a README", par=110, ext="md",
    task="README.md grew by copy and paste. Apply the docs reviewer's notes, top to bottom.",
    steps=[
        "Typo in the tagline: form should be from.",
        "Only the title keeps a single #: every other heading becomes ##.",
        "Install should come first: move the whole Install section (heading to blank line) above Usage.",
        "Turn the indented example into a fenced code block: a ```sh line above it, ``` below, no indent.",
        "Number the install steps 1, 2, 3.",
        "Format every make command as code: `make`, `make install` and `make test`.",
        "Align the Styles table: widen the first column so the double row fits.",
        "Options: use - bullets instead of *.",
        "Options: put each option and its argument in backticks, like `--pad N`.",
        "The link's text and URL are swapped: it should read [the guide](CONTRIBUTING.md).",
        "Typo on the last line: beofre should be before.",
    ],
    start=text("""
        # boxdraw

        Draw ASCII boxes around text, straight form your shell.

        # Usage

        Pipe any text into boxdraw and pick a style:

            echo "hello" | boxdraw --style round

        # Install

        1. Clone the repository.
        1. Run make.
        1. Run make install.

        # Styles

        | style | corner | edge |
        |-------|--------|------|
        | plain | +      | -    |
        | round | .      | -    |
        | double | #      | =    |

        # Options

        * --style NAME: pick a style (default: plain)
        * --pad N: blank columns between text and edge
        * --width N: wrap lines longer than N columns

        # Contributing

        Read [CONTRIBUTING.md](the guide) and run make test
        beofre you open a pull request.
    """),
    target=text("""
        # boxdraw

        Draw ASCII boxes around text, straight from your shell.

        ## Install

        1. Clone the repository.
        2. Run `make`.
        3. Run `make install`.

        ## Usage

        Pipe any text into boxdraw and pick a style:

        ```sh
        echo "hello" | boxdraw --style round
        ```

        ## Styles

        | style  | corner | edge |
        |--------|--------|------|
        | plain  | +      | -    |
        | round  | .      | -    |
        | double | #      | =    |

        ## Options

        - `--style NAME`: pick a style (default: plain)
        - `--pad N`: blank columns between text and edge
        - `--width N`: wrap lines longer than N columns

        ## Contributing

        Read [the guide](CONTRIBUTING.md) and run `make test`
        before you open a pull request.
    """),
    hint="Three of the steps are one command each: a range that starts at the cursor skips the title, a "
         "short pattern that only the make commands contain catches all three, and one :g with :normal "
         "(Ctrl-o works inside it) does both Options steps. g Ctrl-a numbers the list, and a one-column "
         "Visual block, yanked and put back, doubles a column of the table.",
    uses=["search", "subst", "range", "global", "normal", "ctrl-o", "block-edit", "g-ctrl-a", "bracket",
          "ctrl-a-insert"],
)

course.add(
    name="strbuf-bugs",
    title="Fix what ASan found",
    par=113,
    ext="c",
    task="A code review and an AddressSanitizer run of the tests found these bugs in strbuf.c. "
         "Fix them all.",
    steps=[
        "sb_new: heap-buffer-overflow. malloc(sb->len) leaves no room for the NUL: allocate sb->len + 1.",
        "sb_new: the NULL check after that malloc tests s. It must test sb->buf.",
        "sb_new: leak. On that error path, free(sb) before returning NULL (add braces).",
        "sb_new: replace strcpy with memcpy(sb->buf, s, sb->len + 1).",
        "sb_new: -Wreturn-type, it falls off the end. Add return sb; as its last line.",
        "sb_cstr only reads sb: make the parameter const struct strbuf *sb.",
        "sb_cstr: sizeof(char *) is the size of a pointer. It should be sizeof(char).",
        "sb_cstr: replace strcpy with memcpy(out, sb->buf, sb->len + 1).",
        "sb_print only reads sb too: make its parameter const as well.",
        "sb_print: off by one, the loop prints the NUL too. It should run while i < sb->len.",
        "sb_print: -Wformat, sb->len is a size_t. Print it with %zu, not %d.",
        "sb_free: leak. Free sb->buf first: add free(sb->buf); above free(sb);.",
        "Move sb_free() up so it sits right below sb_new(), with one blank line between functions.",
    ],
    start=text("""
        #include "strbuf.h"
        #include <stdio.h>
        #include <stdlib.h>
        #include <string.h>

        struct strbuf *sb_new(const char *s)
        {
            struct strbuf *sb = malloc(sizeof *sb);
            if (sb == NULL)
                return NULL;
            sb->len = strlen(s);
            sb->buf = malloc(sb->len);
            if (s == NULL)
                return NULL;
            strcpy(sb->buf, s);
        }

        char *sb_cstr(struct strbuf *sb)
        {
            char *out = malloc((sb->len + 1) * sizeof(char *));
            if (out != NULL)
                strcpy(out, sb->buf);
            return out;
        }

        void sb_print(struct strbuf *sb)
        {
            for (size_t i = 0; i <= sb->len; i++)
                printf("%02x ", sb->buf[i]);
            printf("(%d bytes)\\n", sb->len);
        }

        void sb_free(struct strbuf *sb)
        {
            free(sb);
        }
    """),
    target=text("""
        #include "strbuf.h"
        #include <stdio.h>
        #include <stdlib.h>
        #include <string.h>

        struct strbuf *sb_new(const char *s)
        {
            struct strbuf *sb = malloc(sizeof *sb);
            if (sb == NULL)
                return NULL;
            sb->len = strlen(s);
            sb->buf = malloc(sb->len + 1);
            if (sb->buf == NULL) {
                free(sb);
                return NULL;
            }
            memcpy(sb->buf, s, sb->len + 1);
            return sb;
        }

        void sb_free(struct strbuf *sb)
        {
            free(sb->buf);
            free(sb);
        }

        char *sb_cstr(const struct strbuf *sb)
        {
            char *out = malloc((sb->len + 1) * sizeof(char));
            if (out != NULL)
                memcpy(out, sb->buf, sb->len + 1);
            return out;
        }

        void sb_print(const struct strbuf *sb)
        {
            for (size_t i = 0; i < sb->len; i++)
                printf("%02x ", sb->buf[i]);
            printf("(%zu bytes)\\n", sb->len);
        }
    """),
    hint="Begin at the bottom with sb_free: dap and P move it, and the ->buf you type there is still in "
         "the . register when you fix the NULL check. Yank sb->len + 1 once and record the first strcpy "
         "fix as a macro for the second. Ctrl-x Ctrl-l completes the whole free(sb); line.",
    uses=["ip", "paragraph", "ctrl-r", "paren", "line-complete", "complete", "macro", "replay", "replace-mode", "dot"],
)

course.add(
    name="modern-java",
    title="Modernize an old class",
    par=123,
    ext="java",
    cursor=(3, 1),
    task="Inventory.java was written for Java 6. Bring it up to Java 21, one review comment at a time.",
    steps=[
        "KINDS: build the list with List.of(...) instead of Arrays.asList(...).",
        "items: use the diamond operator, new ArrayList<>().",
        "stock: use the diamond too, and join the declaration onto one line.",
        "label(): turn the switch into an expression, starting return switch (kind) {.",
        "label(): one arrow line per case, like case \"cd\" -> \"Music\"; and default -> \"Other\";.",
        "label(): close the switch expression with };.",
        "inStock(): return stock.getOrDefault(name, 0); instead of the ?: expression.",
        "report(): declare sb with var.",
        "report(): loop with for (Item item : items) and delete the items.get(i) line.",
        "equals() and hashCode() override Object's methods: put @Override above each.",
        "equals(): use pattern matching, o instanceof Inventory other, and delete the cast line.",
    ],
    start=text("""
        import java.util.*;

        public class Inventory {
            static final List<String> KINDS = Arrays.asList("cd", "lp");
            private final List<Item> items = new ArrayList<Item>();
            private final Map<String, Integer> stock =
                    new HashMap<String, Integer>();

            static String label(String kind) {
                switch (kind) {
                    case "cd":
                        return "Music";
                    case "lp":
                        return "Vinyl";
                    default:
                        return "Other";
                }
            }

            int inStock(String name) {
                return stock.containsKey(name) ? stock.get(name) : 0;
            }

            String report() {
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < items.size(); i++) {
                    Item item = items.get(i);
                    sb.append(label(item.kind())).append('\\n');
                }
                return sb.toString();
            }

            public boolean equals(Object o) {
                if (o instanceof Inventory) {
                    Inventory other = (Inventory) o;
                    return items.equals(other.items);
                }
                return false;
            }

            public int hashCode() { return items.hashCode(); }
        }
    """),
    target=text("""
        import java.util.*;

        public class Inventory {
            static final List<String> KINDS = List.of("cd", "lp");
            private final List<Item> items = new ArrayList<>();
            private final Map<String, Integer> stock = new HashMap<>();

            static String label(String kind) {
                return switch (kind) {
                    case "cd" -> "Music";
                    case "lp" -> "Vinyl";
                    default -> "Other";
                };
            }

            int inStock(String name) {
                return stock.getOrDefault(name, 0);
            }

            String report() {
                var sb = new StringBuilder();
                for (Item item : items) {
                    sb.append(label(item.kind())).append('\\n');
                }
                return sb.toString();
            }

            @Override
            public boolean equals(Object o) {
                if (o instanceof Inventory other) {
                    return items.equals(other.items);
                }
                return false;
            }

            @Override
            public int hashCode() { return items.hashCode(); }
        }
    """),
    hint="di< and . handle both diamonds, a short macro (J, then change the colon and the return) turns each "
         "case into an arrow, and O@Override plus . covers both overrides. Deleted text lands in a register: "
         "reuse the return the cases lose, and yank most of the new loop header from the line you delete.",
    uses=["angle", "dot", "macro", "replay", "join", "plus", "complete", "paren", "visual", "p"],
)

course.add(
    name="py2-to-py3", title="Port a script to Python 3", par=137, ext="py",
    task="chart.py still runs on Python 2. Port it to Python 3: the steps are what 2to3 and a reviewer "
         "flagged, top to bottom.",
    steps=[
        "Shebang: run it with python3.",
        "Replace the cPickle try/except with a plain import pickle, sorted above import sys.",
        "except ValueError, e: becomes except ValueError as e:.",
        "Turn every print statement into a print() call (the bare print becomes print()).",
        "In parse(), not hits.has_key(url) becomes url not in hits.",
        "In chart(), replace the keys()/sort() pair with one line: urls = sorted(hits).",
        "top == None becomes top is None.",
        "hits.itervalues() becomes hits.values().",
        "xrange becomes range.",
        "The bar length must stay an int: use // for the division.",
        "Print the bar with an f-string: f\"{urls[i]:20} {bar}\".",
        "<> becomes !=.",
        "raw_input becomes input.",
    ],
    start=text("""
        #!/usr/bin/env python
        import sys
        try:
            import cPickle as pickle
        except ImportError:
            import pickle


        def parse(path):
            hits = {}
            for line in open(path):
                try:
                    url, ms = line.split()[6], int(line.split()[-1])
                except ValueError, e:
                    print "skipping line:", e
                    continue
                if not hits.has_key(url) or hits[url] < ms:
                    hits[url] = ms
            return hits


        def chart(hits, width, top=None):
            urls = hits.keys()
            urls.sort()
            if top == None:
                top = max(hits.itervalues())
            print "scale:", top, "ms"
            for i in xrange(len(urls)):
                bar = "#" * (hits[urls[i]] * width / top)
                print "%-20s %s" % (urls[i], bar)
            print


        if __name__ == "__main__":
            if len(sys.argv) <> 2:
                sys.exit("usage: chart.py LOGFILE")
            hits = parse(sys.argv[1])
            pickle.dump(hits, open("hits.pkl", "wb"))
            print "saved", len(hits), "URLs to hits.pkl"
            chart(hits, int(raw_input("Width? ")))
    """),
    target=text("""
        #!/usr/bin/env python3
        import pickle
        import sys


        def parse(path):
            hits = {}
            for line in open(path):
                try:
                    url, ms = line.split()[6], int(line.split()[-1])
                except ValueError as e:
                    print("skipping line:", e)
                    continue
                if url not in hits or hits[url] < ms:
                    hits[url] = ms
            return hits


        def chart(hits, width, top=None):
            urls = sorted(hits)
            if top is None:
                top = max(hits.values())
            print("scale:", top, "ms")
            for i in range(len(urls)):
                bar = "#" * (hits[urls[i]] * width // top)
                print(f"{urls[i]:20} {bar}")
            print()


        if __name__ == "__main__":
            if len(sys.argv) != 2:
                sys.exit("usage: chart.py LOGFILE")
            hits = parse(sys.argv[1])
            pickle.dump(hits, open("hits.pkl", "wb"))
            print("saved", len(hits), "URLs to hits.pkl")
            chart(hits, int(input("Width? ")))
    """),
    hint="| chains Ex commands on one line (a :g has to come last), and :3,5d|<|m1 does the imports. "
         "Only the print statements contain a quote followed by s, so one :g with :normal converts three of "
         "them and leaves you at the bottom: working upward, the jumps land on the right columns. Ctrl-n and "
         "Ctrl-p complete url, hits, sort, urls and bar, even in Replace mode.",
    uses=["global", "normal", "copy-move", "complete", "replace-mode", "ctrl-o", "count", "bigword"],
)

course.add(
    name="globals-to-struct",
    title="Globals into a struct",
    par=136,
    ext="c",
    task="bar.c draws a text progress bar. Its five settings are loose globals: gather them into one "
         "struct, then apply the rest of the review.",
    steps=[
        "Wrap the five globals in struct config { ... } cfg; with the members indented one level.",
        "In the struct, merge char fill; and char empty; into one line: char fill, empty;",
        "Every use of a former global becomes a field: cfg.width, cfg.fill, cfg.empty, cfg.label, cfg.quiet.",
        "Rename set_defaults() to config_init(), definition and call.",
        "config_init: the bar should be 60 wide by default, not 40.",
        "config_init: empty cells should be '-', not '.'.",
        "config_init: the default label is \"loading\", not \"progress\".",
        "draw: check quiet first. Move the if (cfg.quiet) return; above int filled.",
        "draw: right-align the percentage in three columns: %3d%% instead of %d%%.",
        "main: draw in 20 steps instead of 10 (both 10s become 20).",
        "Make config_init() and draw() static: nothing outside this file calls them.",
    ],
    start=text("""
        #include <stdio.h>
        #include <stdlib.h>

        int width;
        char fill;
        char empty;
        const char *label;
        int quiet;

        void set_defaults(void)
        {
            width = 40;
            fill = '#';
            empty = '.';
            label = "progress";
        }

        void draw(int done, int total)
        {
            int filled = done * width / total;
            if (quiet)
                return;
            printf("%s [", label);
            for (int i = 0; i < width; i++)
                putchar(i < filled ? fill : empty);
            printf("] %d%%\\n", done * 100 / total);
        }

        int main(int argc, char **argv)
        {
            set_defaults();
            if (argc > 1)
                label = argv[1];
            if (argc > 2)
                width = atoi(argv[2]);
            for (int i = 0; i <= 10; i++)
                draw(i, 10);
        }
    """),
    target=text("""
        #include <stdio.h>
        #include <stdlib.h>

        struct config {
            int width;
            char fill, empty;
            const char *label;
            int quiet;
        } cfg;

        static void config_init(void)
        {
            cfg.width = 60;
            cfg.fill = '#';
            cfg.empty = '-';
            cfg.label = "loading";
        }

        static void draw(int done, int total)
        {
            if (cfg.quiet)
                return;
            int filled = done * cfg.width / total;
            printf("%s [", cfg.label);
            for (int i = 0; i < cfg.width; i++)
                putchar(i < filled ? cfg.fill : cfg.empty);
            printf("] %3d%%\\n", done * 100 / total);
        }

        int main(int argc, char **argv)
        {
            config_init();
            if (argc > 1)
                cfg.label = argv[1];
            if (argc > 2)
                cfg.width = atoi(argv[2]);
            for (int i = 0; i <= 20; i++)
                draw(i, 20);
        }
    """),
    hint="Wrap the struct first. Then one :s from its closing line to the end adds every cfg.: it's "
         "enough to match the first letter of each name, but mind filled. Ctrl-a with a count finds the "
         "next number on the line by itself, and * with cgn and . renames set_defaults.",
    uses=["join", "indent", "subst", "very-magic", "range", "increment", "star", "complete", "dot", "dd"],
)

course.add(
    name="unittest-to-pytest", title="Move a test module to pytest", par=139, ext="py",
    task="The team switched to pytest. Convert test_cart.py: module-level test functions that take a "
         "cart fixture, and plain assert statements.",
    steps=[
        "Import pytest instead of unittest.",
        "Replace the class TestCart line with @pytest.fixture, so setUp turns into a module-level fixture.",
        "setUp(self) becomes cart(), and it returns the new Cart instead of assigning self.cart.",
        "Dedent everything that was inside the class by one level.",
        "Every test takes the fixture: (self) becomes (cart), and self.cart becomes cart everywhere.",
        "self.assertEqual(a, b) becomes assert a == b.",
        "self.assertIsNone(x) becomes assert x is None.",
        "self.assertIn(a, b) becomes assert a in b.",
        "self.assertTrue(x) becomes assert x.",
        "with self.assertRaises(E): becomes with pytest.raises(E):.",
        "Separate the top-level functions with two blank lines, as black would.",
        "Delete the if __name__ == \"__main__\": block at the bottom.",
    ],
    start=text("""
        import unittest

        from shop.cart import Cart, OutOfStock


        class TestCart(unittest.TestCase):
            def setUp(self):
                self.cart = Cart(stock={"apple": 3, "pear": 2})

            def test_starts_empty(self):
                self.assertEqual(len(self.cart), 0)
                self.assertIsNone(self.cart.last_added)

            def test_add(self):
                self.cart.add("apple", 2)
                self.assertEqual(self.cart.count("apple"), 2)
                self.assertIn("apple", self.cart)
                self.assertEqual(self.cart.last_added, "apple")

            def test_items_are_sorted(self):
                self.cart.add("pear", 1)
                self.cart.add("apple", 1)
                self.assertEqual(self.cart.items(), ["apple", "pear"])

            def test_total(self):
                self.cart.add("apple", 3)
                self.assertEqual(self.cart.total(), 1.5)
                self.assertTrue(self.cart.has_items())

            def test_out_of_stock(self):
                with self.assertRaises(OutOfStock):
                    self.cart.add("pear", 5)


        if __name__ == "__main__":
            unittest.main()
    """),
    target=text("""
        import pytest

        from shop.cart import Cart, OutOfStock


        @pytest.fixture
        def cart():
            return Cart(stock={"apple": 3, "pear": 2})


        def test_starts_empty(cart):
            assert len(cart) == 0
            assert cart.last_added is None


        def test_add(cart):
            cart.add("apple", 2)
            assert cart.count("apple") == 2
            assert "apple" in cart
            assert cart.last_added == "apple"


        def test_items_are_sorted(cart):
            cart.add("pear", 1)
            cart.add("apple", 1)
            assert cart.items() == ["apple", "pear"]


        def test_total(cart):
            cart.add("apple", 3)
            assert cart.total() == 1.5
            assert cart.has_items()


        def test_out_of_stock(cart):
            with pytest.raises(OutOfStock):
                cart.add("pear", 5)
    """),
    hint="Strip self. everywhere with one :s, and the only self left are the parameters; | puts both "
         ":s on one line. After that every assertion line starts with assert, so one :g with :normal can "
         "rewrite them all the same way (drop the last paren, the method name and its paren, turn the first "
         "comma into ==), and the odd ones need only a touch. <G dedents to the end, and a :g on the def test "
         "lines can copy the blank line above each one.",
    uses=["subst", "global", "normal", "replace-mode", "complete", "indent", "copy-move", "bigword"],
)

course.add(
    name="harden-bash",
    title="Make ShellCheck happy",
    par=149,
    ext="sh",
    task="deploy.sh works on your machine, but ShellCheck and a reviewer flagged it. Harden it.",
    steps=[
        "Add set -euo pipefail on its own line, right after the shebang.",
        "Mark the three constants APP, SRC and LOG readonly: readonly APP=shop, and so on.",
        "SC2006: VERSION uses backticks. Use $(...) instead.",
        "log: msg leaks into the global scope. Declare it with local.",
        "log: SC2086, quote \"$LOG\".",
        "die: error messages belong on stderr. Add >&2 at the end of the echo.",
        "deploy_to is indented with two spaces. Re-indent its body to four, like the other functions.",
        "deploy_to: HOST isn't an environment variable. Make it local, and lowercase (host) in the whole function.",
        "deploy_to logs \"deployed\" before anything has run: move the log line to the end of the function.",
        "deploy_to: SC2086, quote rsync's arguments \"$SRC/\" and \"$host:/srv/$APP/\", and ssh's \"$host\".",
        "SC2292: use [[ ]] instead of [ ] in the argument check.",
        "SC2046: quote both expansions on the cd line: cd \"$(dirname \"$0\")\".",
        "SC2164: cd can fail. Add || exit 1 to that line.",
        "SC2068 and SC2086: quote \"$@\" in the for loop, and \"$h\" in the call.",
    ],
    start=text("""
        #!/bin/bash
        # Deploy the current build to one or more web servers.

        APP=shop
        SRC=dist
        LOG=/var/log/deploy.log
        VERSION=`git describe --tags`

        log() {
            msg=$1
            echo "$(date +%T) $msg" >> $LOG
        }

        die() {
            echo "error: $1"
            exit 1
        }

        deploy_to() {
          HOST=$1
          log "deployed $VERSION to $HOST"
          rsync -az $SRC/ $HOST:/srv/$APP/ || die "rsync failed"
          ssh $HOST "systemctl restart $APP" || die "restart failed"
        }

        if [ $# -eq 0 ]; then
            die "usage: $0 HOST..."
        fi
        cd $(dirname $0)
        for h in $@; do
            deploy_to $h
        done
        log "deployed $VERSION to $# hosts"
    """),
    target=text("""
        #!/bin/bash
        set -euo pipefail
        # Deploy the current build to one or more web servers.

        readonly APP=shop
        readonly SRC=dist
        readonly LOG=/var/log/deploy.log
        VERSION=$(git describe --tags)

        log() {
            local msg=$1
            echo "$(date +%T) $msg" >> "$LOG"
        }

        die() {
            echo "error: $1" >&2
            exit 1
        }

        deploy_to() {
            local host=$1
            rsync -az "$SRC/" "$host:/srv/$APP/" || die "rsync failed"
            ssh "$host" "systemctl restart $APP" || die "restart failed"
            log "deployed $VERSION to $host"
        }

        if [[ $# -eq 0 ]]; then
            die "usage: $0 HOST..."
        fi
        cd "$(dirname "$0")" || exit 1
        for h in "$@"; do
            deploy_to "$h"
        done
        log "deployed $VERSION to $# hosts"
    """),
    hint="ciW\"<C-r>-\"<Esc> quotes a whole WORD, and . repeats it on other WORDs because Ctrl-r - "
         "reads the register again each time. One :s over the four lines of deploy_to lowercases HOST "
         "(\\L&). Finish each . chain before you start the next.",
    uses=["insert", "dot", "range", "replace-case", "iw-big", "ctrl-r", "small-delete", "bracket", "complete", "bigword"],
)

course.add(
    name="training-loop", title="Fix a training script", par=141, ext="py",
    task="A reviewer went through train.py and left comments, top to bottom. Apply them all.",
    steps=[
        "Lower the learning rate: LR = 3e-4.",
        "Train for 50 epochs.",
        "Double the batch size to 64.",
        "Shuffle the training data, not the validation data: move , shuffle=True to train_dl's line.",
        "Rename train_dl and val_dl to train_loader and val_loader.",
        "Rename opt to optimizer.",
        "Call model.train() at the start of each epoch, before total = 0.",
        "zero_grad() has to run before the forward pass: move it to the top of the batch loop.",
        "loss.item is a method: call it.",
        "Comment out the debug print of loss.shape.",
        "Call model.eval() before correct = 0.",
        "Run the validation for loop inside with torch.no_grad(): (correct = 0 stays above it).",
        "The validation loop has the same .item bug: call it there too.",
        "Build the checkpoint path with an f-string: f\"convnet-{EPOCHS}.pt\".",
    ],
    start=text("""
        import torch
        from torch import nn
        from torch.utils.data import DataLoader

        from data import load_digits
        from model import ConvNet

        LR = 0.01
        EPOCHS = 10
        BATCH_SIZE = 32

        train_set, val_set = load_digits()
        train_dl = DataLoader(train_set, BATCH_SIZE)
        val_dl = DataLoader(val_set, BATCH_SIZE, shuffle=True)

        model = ConvNet()
        opt = torch.optim.Adam(model.parameters(), lr=LR)
        loss_fn = nn.CrossEntropyLoss()

        for epoch in range(EPOCHS):
            total = 0
            for x, y in train_dl:
                loss = loss_fn(model(x), y)
                loss.backward()
                opt.zero_grad()
                opt.step()
                total += loss.item
                print(loss.shape)

            correct = 0
            for x, y in val_dl:
                pred = model(x).argmax(dim=1)
                correct += (pred == y).sum().item
            print(epoch, total, correct / len(val_set))

        path = "convnet-%d.pt" % EPOCHS
        torch.save(model.state_dict(), path)
    """),
    target=text("""
        import torch
        from torch import nn
        from torch.utils.data import DataLoader

        from data import load_digits
        from model import ConvNet

        LR = 3e-4
        EPOCHS = 50
        BATCH_SIZE = 64

        train_set, val_set = load_digits()
        train_loader = DataLoader(train_set, BATCH_SIZE, shuffle=True)
        val_loader = DataLoader(val_set, BATCH_SIZE)

        model = ConvNet()
        optimizer = torch.optim.Adam(model.parameters(), lr=LR)
        loss_fn = nn.CrossEntropyLoss()

        for epoch in range(EPOCHS):
            model.train()
            total = 0
            for x, y in train_loader:
                optimizer.zero_grad()
                loss = loss_fn(model(x), y)
                loss.backward()
                optimizer.step()
                total += loss.item()
                # print(loss.shape)

            model.eval()
            correct = 0
            with torch.no_grad():
                for x, y in val_loader:
                    pred = model(x).argmax(dim=1)
                    correct += (pred == y).sum().item()
            print(epoch, total, correct / len(val_set))

        path = f"convnet-{EPOCHS}.pt"
        torch.save(model.state_dict(), path)
    """),
    hint="Ctrl-a takes a count. * on opt then :%s//&imizer renames it without retyping it (& is the "
         "match), * also jumps you to zero_grad(), and | chains the Ex commands. Both .item lines end the "
         "line, so A() and . fix them. Indent the validation loop before you add the with line: O copies "
         "the indent and Ctrl-d removes one level.",
    uses=["increment", "search", "star", "copy-move", "subst", "comment", "dot", "complete", "ctrl-o",
          "indent"],
)

course.add(
    name="sql-migration",
    title="Rework a schema for a migration",
    par=174,
    ext="sql",
    task="Ticket SHOP-42: schema v2. Apply the migration checklist to schema.sql.",
    steps=[
        "The header: this is version 2 of the schema.",
        "Uppercase the lowercase SQL keywords: create table (line 2), and create index ... on (near the end).",
        "Every CREATE TABLE becomes CREATE TABLE IF NOT EXISTS.",
        "Rename the table customer to customers, in its REFERENCES too (customer_id and the index name stay).",
        "VARCHAR(255) columns become TEXT.",
        "name, email, title and price are NOT NULL (right after the type).",
        "customer and orders: add updated_at TIMESTAMP as a new last column.",
        "orders references product, so move the whole product table (and its blank line) above orders.",
        "product: delete the trailing comma after the stock column.",
        "Seed data: the comment -- id,title,price becomes INSERT INTO product (id, title, price) VALUES",
        "Each seed row becomes a tuple like (1, 'Widget', 2.50), indented 4 spaces, with the title quoted.",
        "End the last tuple with ; instead of ,.",
    ],
    start=text("""
        -- Shop schema, v1
        create table customer (
            id INTEGER PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255) UNIQUE,
            created_at TIMESTAMP
        );

        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER REFERENCES customer(id),
            product_id INTEGER REFERENCES product(id),
            quantity INTEGER DEFAULT 1,
            created_at TIMESTAMP
        );

        CREATE TABLE product (
            id INTEGER PRIMARY KEY,
            title VARCHAR(255),
            price NUMERIC(10, 2),
            stock INTEGER DEFAULT 0,
        );

        create index orders_by_customer on orders (customer_id);

        -- seed data for product:
        -- id,title,price
        -- 1,Widget,2.50
        -- 2,Gadget,10.00
        -- 3,Doohickey,7.25
        -- 4,Sprocket,0.99
        -- 5,Gizmo,15.00
        -- 6,Flange,3.75
    """),
    target=text("""
        -- Shop schema, v2
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP,
            updated_at TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            price NUMERIC(10, 2) NOT NULL,
            stock INTEGER DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER REFERENCES customers(id),
            product_id INTEGER REFERENCES product(id),
            quantity INTEGER DEFAULT 1,
            created_at TIMESTAMP,
            updated_at TIMESTAMP
        );

        CREATE INDEX orders_by_customer ON orders (customer_id);

        -- seed data for product:
        INSERT INTO product (id, title, price) VALUES
            (1, 'Widget', 2.50),
            (2, 'Gadget', 10.00),
            (3, 'Doohickey', 7.25),
            (4, 'Sprocket', 0.99),
            (5, 'Gizmo', 15.00),
            (6, 'Flange', 3.75);
    """),
    hint="VARCHAR(255) to TEXT and NOT NULL is one :s, and price can borrow its NOT NULL with a yank. A new "
         "column is a copy of created_at with three letters typed over, so record it once for both tables. "
         "The six seed rows have the same shape, so record one and replay it; Ctrl-t and Ctrl-o let the "
         "macro stay in Insert mode.",
    uses=["increment", "case", "star", "subst", "y", "paragraph", "replace-mode", "macro", "replay", "ctrl-t"],
)

course.add(
    name="review-userservice",
    title="Apply a code review",
    par=179,
    ext="java",
    task="A teammate reviewed UserService.java. Apply every comment.",
    steps=[
        "Also import java.util.List, on its own line below the ArrayList import.",
        "Add private static final int MAX_USERS = 500; above the fields, and use it for both 500s.",
        "Make the fields repo and m private final.",
        "Rename the field m to mailer everywhere (the constructor parameter too).",
        "findActive() and register() implement UserLookup: put @Override above each.",
        "findActive() should return List<User>, and declare its local list as List<User> too.",
        "In findActive(), rename the local list out to active.",
        "Delete both System.out.println debug lines.",
        "Strings need equals: write u.getStatus().equals(\"ACTIVE\") instead of ==.",
        "Fix the typo usres in the exception message.",
        "Swap welcome()'s parameters to (User u, String text), and fix its call in register().",
        "Move spaceLeft() above welcome(): the private helper goes last.",
    ],
    start=text("""
        import java.util.ArrayList;

        public class UserService implements UserLookup {
            UserRepository repo;
            Mailer m;

            public UserService(UserRepository repo, Mailer m) {
                this.repo = repo;
                this.m = m;
            }

            public ArrayList<User> findActive() {
                ArrayList<User> out = new ArrayList<>();
                for (User u : repo.findAll()) {
                    System.out.println("checking " + u);
                    if (u.getStatus() == "ACTIVE") {
                        out.add(u);
                    }
                }
                return out;
            }

            public void register(User u) {
                if (repo.count() >= 500) {
                    throw new IllegalStateException("Too many usres");
                }
                System.out.println("saving " + u);
                repo.save(u);
                welcome("Welcome aboard!", u);
            }

            private void welcome(String text, User u) {
                m.send(u.getEmail(), text);
            }

            public int spaceLeft() { return 500 - repo.count(); }
        }
    """),
    target=text("""
        import java.util.ArrayList;
        import java.util.List;

        public class UserService implements UserLookup {
            private static final int MAX_USERS = 500;
            private final UserRepository repo;
            private final Mailer mailer;

            public UserService(UserRepository repo, Mailer mailer) {
                this.repo = repo;
                this.mailer = mailer;
            }

            @Override
            public List<User> findActive() {
                List<User> active = new ArrayList<>();
                for (User u : repo.findAll()) {
                    if (u.getStatus().equals("ACTIVE")) {
                        active.add(u);
                    }
                }
                return active;
            }

            @Override
            public void register(User u) {
                if (repo.count() >= MAX_USERS) {
                    throw new IllegalStateException("Too many users");
                }
                repo.save(u);
                welcome(u, "Welcome aboard!");
            }

            public int spaceLeft() { return MAX_USERS - repo.count(); }

            private void welcome(User u, String text) {
                mailer.send(u.getEmail(), text);
            }
        }
    """),
    hint="The List import and both List types are 5x on ArrayList, so * and . finish them, and :s leaves the "
         "cursor on the last line it changed, often right where the next edit is. Both welcome() argument "
         "lists swap with the same keys: record the swap once. Type private final once (pr completes): . "
         "repeats it, and Ctrl-a in Insert mode types it again for the constant.",
    uses=["star", "dot", "paragraph", "global", "subst", "macro", "replay", "ctrl-r", "complete", "ctrl-a-insert"],
)

course.add(
    name="junit5-migration",
    title="Migrate a test class to JUnit 5",
    par=182,
    ext="java",
    task="Ticket: move CartTest.java from JUnit 4 to JUnit 5. The checklist below is in file order.",
    steps=[
        "Point every import at JUnit 5: org.junit. becomes org.junit.jupiter.api.",
        "Assert's import becomes import static org.junit.jupiter.api.Assertions.*; put it first, then a blank line.",
        "@Before and @After become @BeforeEach and @AfterEach (imports too).",
        "@Ignore becomes @Disabled (import too). Keep the reason.",
        "JUnit 5 doesn't need public: drop it from the class and from every method.",
        "Drop the JUnit 3 style test prefix: testAddsItems() becomes addsItems(), and so on.",
        "Call the assertions through the static import: delete every Assert. prefix.",
        "JUnit 5 takes the message last: assertX(\"msg\", a, b) becomes assertX(a, b, \"msg\").",
        "addsItems(): two apples at 150 each cost 300, so expect a total of 300.",
        "rejectsNegativeQuantity(): drop (expected = ...) from its @Test.",
        "Wrap its body: assertThrows(IllegalArgumentException.class, then Enter and () -> cart.add(...));",
    ],
    start=text("""
        import org.junit.After;
        import org.junit.Assert;
        import org.junit.Before;
        import org.junit.Ignore;
        import org.junit.Test;

        public class CartTest {
            private Cart cart;

            @Before
            public void setUp() {
                cart = new Cart();
            }

            @After
            public void tearDown() {
                cart.clear();
            }

            @Test
            public void testAddsItems() {
                cart.add("apple", 2);
                Assert.assertFalse("empty", cart.isEmpty());
                Assert.assertEquals("count", 2, cart.size());
                Assert.assertEquals("total", 150, cart.total());
            }

            @Test(expected = IllegalArgumentException.class)
            public void testRejectsNegativeQuantity() {
                cart.add("pear", -1);
            }

            @Ignore("discount codes are not implemented yet")
            @Test
            public void testStartsWithNoDiscount() {
                Assert.assertEquals(0, cart.discount());
            }
        }
    """),
    target=text("""
        import static org.junit.jupiter.api.Assertions.*;

        import org.junit.jupiter.api.AfterEach;
        import org.junit.jupiter.api.BeforeEach;
        import org.junit.jupiter.api.Disabled;
        import org.junit.jupiter.api.Test;

        class CartTest {
            private Cart cart;

            @BeforeEach
            void setUp() {
                cart = new Cart();
            }

            @AfterEach
            void tearDown() {
                cart.clear();
            }

            @Test
            void addsItems() {
                cart.add("apple", 2);
                assertFalse(cart.isEmpty(), "empty");
                assertEquals(2, cart.size(), "count");
                assertEquals(300, cart.total(), "total");
            }

            @Test
            void rejectsNegativeQuantity() {
                assertThrows(IllegalArgumentException.class,
                        () -> cart.add("pear", -1));
            }

            @Disabled("discount codes are not implemented yet")
            @Test
            void startsWithNoDiscount() {
                assertEquals(0, cart.discount());
            }
        }
    """),
    hint="Dropping public, the test prefix and Assert. are all deletions: one :s with \\v alternatives (and \\l) "
         "does the three, with the shortest patterns while the new static import doesn't exist yet. The "
         "imports line up, so one Visual-block insert fixes every package. The messages and the expected "
         "exception never need retyping: cut or yank them, and paste with Ctrl-r while typing.",
    uses=["subst", "very-magic", "replace-case", "macro", "replay", "increment", "ctrl-r", "ctrl-o", "copy-move",
          "block-insert"],
)

course.add(
    name="review-menu-page", title="Review · Update a café's menu page", par=164, ext="html",
    task=("Review of the whole course: Bean There's menu page needs a round of updates before the new prices go "
          "up. Work down the page."),
    steps=[
        "The title: Menu · Bean There. (The dot is the digraph .M: Ctrl-k . M.)",
        "The nav: they're not hiring any more, so delete the Jobs link.",
        "The nav: the Contact link reads Find us.",
        "The heading: Our Menu.",
        "Espresso goes up 20 cents, to 2.70.",
        "Coffee: sort the list.",
        "Pastries: each line becomes a list item like the coffee ones.",
        "Every price: in <strong> instead of <b>...",
        "...after a € (Ctrl-k E u): <strong>€2.80</strong>.",
        "Delete the TODO comment...",
        "...and do what it says: loading=\"lazy\" on both images, after the src.",
        "The footer: © (Ctrl-k C o) instead of (c).",
        "The footer: 2026.",
        "The footer: 7am–6pm, with an en dash (Ctrl-k - N) and no spaces around it.",
    ],
    start=text("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Menu</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <nav>
                <a href="/">Home</a>
                <a href="/menu.html">Menu</a>
                <a href="/jobs.html">Jobs</a>
                <a href="/contact.html">Contact</a>
            </nav>

            <h1>our menu</h1>

            <h2>Coffee</h2>
            <ul>
                <li>Latte <b>3.50</b></li>
                <li>Espresso <b>2.50</b></li>
                <li>Cappuccino <b>3.20</b></li>
                <li>Americano <b>2.80</b></li>
            </ul>

            <h2>Pastries</h2>
            <ul>
                Croissant 2.20
                Pain au chocolat 2.60
                Muffin 2.90
            </ul>

            <!-- TODO: lazy-load the photos -->
            <img src="beans.jpg">
            <img src="counter.jpg">

            <footer>
                <p>(c) 2025 Bean There. Open 7am - 6pm.</p>
            </footer>
        </body>
        </html>
    """),
    target=text("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Menu · Bean There</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <nav>
                <a href="/">Home</a>
                <a href="/menu.html">Menu</a>
                <a href="/contact.html">Find us</a>
            </nav>

            <h1>Our Menu</h1>

            <h2>Coffee</h2>
            <ul>
                <li>Americano <strong>€2.80</strong></li>
                <li>Cappuccino <strong>€3.20</strong></li>
                <li>Espresso <strong>€2.70</strong></li>
                <li>Latte <strong>€3.50</strong></li>
            </ul>

            <h2>Pastries</h2>
            <ul>
                <li>Croissant <strong>€2.20</strong></li>
                <li>Pain au chocolat <strong>€2.60</strong></li>
                <li>Muffin <strong>€2.90</strong></li>
            </ul>

            <img src="beans.jpg" loading="lazy">
            <img src="counter.jpg" loading="lazy">

            <footer>
                <p>© 2026 Bean There. Open 7am–6pm.</p>
            </footer>
        </body>
        </html>
    """),
    hint=("Ctrl-k types a character from two letters, in Insert mode and on the command line. Ctrl-n completes "
          "Bean and There from the footer. A macro can turn the pastries into list items with <b> like the "
          "coffees, so that one :s (with | and a second :s) then changes all seven prices at once."),
    uses=["digraph", "complete", "tag", "case", "increment", "sort", "range", "macro", "replay", "subst", "dot",
          "dd"],
)

course.add(
    name="review-package-json", title="Review · Clean up a package.json", par=147,
    task=("Review of the whole course: trail-map's package.json before its 2.0 release. Keep it valid JSON: in "
          "each block, every entry but the last ends with a comma."),
    steps=[
        "npm rejects capital letters in a name: trail-map.",
        "Version 2.0.0.",
        "private: true, so it can't be published by accident.",
        "scripts: start is now called dev.",
        "scripts: test runs vitest run.",
        "scripts: a new last script, \"lint\": \"eslint .\".",
        "eslint is a dev tool: move it to devDependencies.",
        "dependencies: delete lodash, which nothing imports...",
        "...and jest, which vitest replaces.",
        "react: 18.3.1.",
        "Sort dependencies and devDependencies alphabetically.",
        "devDependencies: add \"vitest\": \"1.6.0\".",
        "Pin every version: drop the ^.",
        "files: on one line, [\"dist\", \"README.md\"].",
        "engines: node >=20.",
    ],
    files={"package.json": (text("""
        {
            "name": "Trail-Map",
            "version": "1.9.4",
            "private": false,
            "scripts": {
                "start": "vite",
                "build": "vite build",
                "test": "jest"
            },
            "dependencies": {
                "react": "^18.2.0",
                "leaflet": "^1.9.4",
                "eslint": "^8.57.0",
                "lodash": "^4.17.21",
                "jest": "^29.7.0",
                "date-fns": "^3.6.0",
                "axios": "^1.6.8"
            },
            "devDependencies": {
                "vite": "^5.2.0"
            },
            "files": [
                "dist",
                "README.md"
            ],
            "engines": {
                "node": ">=16"
            }
        }
    """), text("""
        {
            "name": "trail-map",
            "version": "2.0.0",
            "private": true,
            "scripts": {
                "dev": "vite",
                "build": "vite build",
                "test": "vitest run",
                "lint": "eslint ."
            },
            "dependencies": {
                "axios": "1.6.8",
                "date-fns": "3.6.0",
                "leaflet": "1.9.4",
                "react": "18.3.1"
            },
            "devDependencies": {
                "eslint": "8.57.0",
                "vite": "5.2.0",
                "vitest": "1.6.0"
            },
            "files": ["dist", "README.md"],
            "engines": {
                "node": ">=20"
            }
        }
    """))},
    hint=("gu$ lowercases to the end of the line, and quotes and commas have no case. Two deletes in a row push "
          "the first into register 2. Sorting moves the comma-less last line to the top, so two commas need fixing "
          "afterwards. Ctrl-a with a count does the version arithmetic."),
    uses=["case", "increment", "replace-mode", "quote", "brace", "numbered", "sort", "subst", "join", "complete",
          "dd", "p"],
)

course.run()
