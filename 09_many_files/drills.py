"""Drills for Project 09: short problems that practice one command at a time.
Play them with:  python3 check.py drill      (the reference solutions are in ../solutions/drills/)

Most drills here have several files, so there's no target window: the task says what to change in which file.
"""
from trainer import Drills, text

drills = Drills(__file__)


def badd(*names):
    """Setup: open more files as buffers (listed, but not shown)."""
    return [f"badd {n}" for n in names]


WINBAR = "lua vim.wo.winbar = ' %#Comment#%f%*'"  # the new window shows its file name at the top


def vsplit(name):
    """Setup: show NAME in a window on the right. keepalt: Ctrl-^ can't jump between the two files."""
    return [f"keepalt rightbelow vsplit {name}", WINBAR, "wincmd p"]


def split(name):
    """Setup: show NAME in a window below."""
    return [f"keepalt rightbelow split {name}", WINBAR, "wincmd p"]


# ---------- :e Ctrl-^ ----------

edit = drills.command(
    "edit", ":e {file}  Ctrl-^", "open a file, and switch back",
    """:e {file} opens a file in the current window. The name is relative to the folder Neovim started in, and
    Tab completes it: :e r<Tab> fills in requirements.txt when that's the only name starting with r (if several
    match, each Tab shows the next one). Folder names complete too, and ** stands for any folders, so
    :e **/Prod<Tab> finds Product.java wherever it is. Ctrl-^ switches to the alternate file, the one this window
    showed just before, with the cursor where you left it; press it again to come back. The file you leave stays
    open as a hidden buffer, unsaved changes and all, so you can save everything at the end with :wa.""",
    examples=[(":e r<Tab>", "complete a file name, then Enter opens it"), (":e src/p<Tab>", "complete inside a folder"),
              (":e **/Prod<Tab>", "find Product.java in any folder"),
              ("Ctrl-^", "back to the previous file, again to return"), (":e #", "the same as Ctrl-^")],
)
edit.add(
    title="Open a second file", par=10,
    task="Bump requests to the next minor version: in requirements.txt, change requests==2.31.0 to "
         "requests==2.32.0. You start in app.py.",
    files={
        "app.py": (text('''
            import requests

            resp = requests.get("https://api.github.com/zen", timeout=5)
            print(resp.text)
        '''),) * 2,
        "requirements.txt": (text('''
            certifi==2024.8.30
            requests==2.31.0
            urllib3==2.2.3
        '''), text('''
            certifi==2024.8.30
            requests==2.32.0
            urllib3==2.2.3
        ''')),
    },
    open="app.py",
    hint=":e opens a file, and after its first letter Tab completes the name. In the file, f. puts the cursor on "
         "the dot before 31, and Ctrl-a adds 1 to the next number on the line.",
    uses=["increment", "f"],
)
edit.add(
    title="A file inside a folder", par=12,
    task="Remove the debugging printf line from src/parser.c. You start in the Makefile.",
    files={
        "Makefile": (text('''
            CFLAGS = -Wall -O2
            SRC = $(wildcard src/*.c)

            calc: $(SRC)
            \t$(CC) $(CFLAGS) -o $@ $(SRC)
        '''),) * 2,
        "src/lexer.c": (text('''
            #include <ctype.h>

            int is_operator(char c)
            {
                return c == '+' || c == '-' || c == '*' || c == '/';
            }
        '''),) * 2,
        "src/parser.c": (text('''
            #include <stdio.h>
            #include <stdlib.h>

            int parse_number(const char *s)
            {
                printf("parse_number: %s\\n", s);
                return atoi(s);
            }
        '''), text('''
            #include <stdio.h>
            #include <stdlib.h>

            int parse_number(const char *s)
            {
                return atoi(s);
            }
        ''')),
    },
    open="Makefile",
    hint="Tab completes folder names too: :e s<Tab> fills in src/, then type p and Tab again for parser.c. In the "
         "file, a counted j reaches the printf line.",
    uses=["dd", "count"],
)
edit.add(
    title="Find it in any folder", par=19,
    task="Rename the price component of the Product record to priceCents. Product.java is somewhere under src/. "
         "You start in build.gradle.",
    files={
        "build.gradle": (text('''
            plugins {
                id 'application'
            }

            application {
                mainClass = 'shop.App'
            }
        '''),) * 2,
        "src/main/java/shop/App.java": (text('''
            package shop;

            import shop.model.Product;

            public class App {
                public static void main(String[] args) {
                    System.out.println(new Product("Tea", 450));
                }
            }
        '''),) * 2,
        "src/main/java/shop/model/Product.java": (text('''
            package shop.model;

            public record Product(String name, int price) {
            }
        '''), text('''
            package shop.model;

            public record Product(String name, int priceCents) {
            }
        ''')),
    },
    open="build.gradle",
    hint="** in a file name stands for any folders, so :e **/P<Tab> finds Product.java wherever it is. In the "
         "file, f) and i put the new letters just before the closing parenthesis.",
    uses=["f", "insert", "count"],
)
edit.add(
    title="Copy lines from another file", par=12,
    task="prod.ini is missing the two log_ lines that dev.ini has. Copy them into prod.ini, below port = 80. "
         "Your cursor starts on that line.",
    files={
        "prod.ini": (text('''
            [server]
            host = 0.0.0.0
            port = 80

            [database]
            url = postgres://db.internal/shop
        '''), text('''
            [server]
            host = 0.0.0.0
            port = 80
            log_format = %(asctime)s %(levelname)s %(name)s: %(message)s
            log_datefmt = %Y-%m-%d %H:%M:%S

            [database]
            url = postgres://db.internal/shop
        ''')),
        "dev.ini": (text('''
            [server]
            host = 127.0.0.1
            port = 8000
            log_format = %(asctime)s %(levelname)s %(name)s: %(message)s
            log_datefmt = %Y-%m-%d %H:%M:%S

            [database]
            url = postgres://localhost/shop_dev
        '''),) * 2,
    },
    open="prod.ini", cursor=(3, 1),
    hint="Open dev.ini with :e and yank the two lines (yj takes this line and the next). Ctrl-^ jumps back to "
         "prod.ini with the cursor where you left it, so p puts them right below.",
    uses=["y", "p", "count"],
)
edit.add(
    title="Paste over a placeholder", par=15,
    task="Replace TODO in README.md with the documentation URL from pyproject.toml (without its quotes). Your "
         "cursor starts on TODO.",
    files={
        "README.md": (text('''
            # acme-widgets

            Small widgets for terminal apps.

            Documentation: TODO
        '''), text('''
            # acme-widgets

            Small widgets for terminal apps.

            Documentation: https://acme-widgets.readthedocs.io/en/latest/
        ''')),
        "pyproject.toml": (text('''
            [project]
            name = "acme-widgets"
            version = "0.4.2"

            [project.urls]
            Documentation = "https://acme-widgets.readthedocs.io/en/latest/"
            Source = "https://github.com/acme/widgets"
        '''),) * 2,
    },
    open="README.md", cursor=(5, 16),
    hint="In pyproject.toml, yi\" yanks the first quoted text on the line, even from the start of the line. "
         "Ctrl-^ takes you back to TODO, and in Visual mode p replaces the selection with what you yanked.",
    uses=["y", "quote", "visual", "p", "count"],
)
edit.add(
    title="Borrow a test helper", par=13,
    task="test_checkout.py calls make_cart, which only test_cart.py defines. Copy the make_cart function, with "
         "the two blank lines after it, into test_checkout.py above test_checkout_clears_cart. Your cursor starts "
         "on that def line.",
    files={
        "test_checkout.py": (text('''
            from shop.cart import Cart
            from shop.checkout import checkout


            def test_checkout_clears_cart():
                cart = make_cart()
                checkout(cart)
                assert cart.items == []
        '''), text('''
            from shop.cart import Cart
            from shop.checkout import checkout


            def make_cart():
                cart = Cart()
                cart.add("tea", 450, qty=2)
                return cart


            def test_checkout_clears_cart():
                cart = make_cart()
                checkout(cart)
                assert cart.items == []
        ''')),
        "test_cart.py": (text('''
            from shop.cart import Cart


            def make_cart():
                cart = Cart()
                cart.add("tea", 450, qty=2)
                return cart


            def test_total():
                assert make_cart().total() == 900
        '''),) * 2,
    },
    open="test_checkout.py", cursor=(5, 1),
    hint=":e t<Tab> completes the first name that starts with t. On the def line, yap yanks the function and "
         "the blank lines after it. Ctrl-^ goes back, and P puts the lines above the cursor.",
    uses=["y", "ip", "p", "count"],
)
edit.add(
    title="Same fix in the other file", par=17,
    task="logging.warn is deprecated. Change it to logging.warning in both fetch.py and parse.py (once in each). "
         "Your cursor starts on warn in fetch.py.",
    files={
        "fetch.py": (text('''
            import logging

            import requests


            def fetch(url):
                resp = requests.get(url, timeout=5)
                if resp.status_code != 200:
                    logging.warn("GET %s returned %d", url, resp.status_code)
                return resp
        '''), text('''
            import logging

            import requests


            def fetch(url):
                resp = requests.get(url, timeout=5)
                if resp.status_code != 200:
                    logging.warning("GET %s returned %d", url, resp.status_code)
                return resp
        ''')),
        "parse.py": (text('''
            import json
            import logging


            def parse(text):
                try:
                    return json.loads(text)
                except json.JSONDecodeError:
                    logging.warn("not JSON: %r", text[:40])
                    return None
        '''), text('''
            import json
            import logging


            def parse(text):
                try:
                    return json.loads(text)
                except json.JSONDecodeError:
                    logging.warning("not JSON: %r", text[:40])
                    return None
        ''')),
    },
    open="fetch.py", cursor=(9, 17),
    hint="Append ing after the n of warn, then open parse.py. The dot command still remembers that change in "
         "the new file: put the cursor on the n of warn there (a search for n( gets you there) and press .",
    uses=["insert", "word", "dot", "search"],
)
edit.add(
    title="Swap items between lists", par=13,
    task="You finished \"fix the login timeout\": move that line from todo.md to the end of done.md. And \"add dark "
         "mode\" was reverted: it goes back to the end of todo.md, so its line in done.md is the one the login line "
         "replaces. Your cursor starts on the login line.",
    files={
        "todo.md": (text('''
            # To do

            - write the README
            - fix the login timeout
            - add CSV export
        '''), text('''
            # To do

            - write the README
            - add CSV export
            - add dark mode
        ''')),
        "done.md": (text('''
            # Done

            - set up CI
            - add dark mode
        '''), text('''
            # Done

            - set up CI
            - fix the login timeout
        ''')),
    },
    open="todo.md", cursor=(4, 1),
    hint="Cut the login line with dd and open done.md. There, V selects the dark mode line and p replaces it, and "
         "the replaced line goes into the register in its place. Ctrl-^ goes back to todo.md, onto its last line.",
    uses=["dd", "visual-line", "p", "gg"],
)
edit.add(
    title="Split a module in two", par=22,
    task="Move slugify from utils.py into text.py, and parse_date into dates.py: each goes below the file's "
         "import, with two blank lines between, as in utils.py. utils.py keeps just its two imports.",
    files={
        "utils.py": (text('''
            import re
            from datetime import datetime


            def slugify(title):
                return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


            def parse_date(s):
                return datetime.strptime(s, "%Y-%m-%d").date()
        '''), text('''
            import re
            from datetime import datetime
        ''')),
        "text.py": (text('''
            import re
        '''), text('''
            import re


            def slugify(title):
                return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        ''')),
        "dates.py": (text('''
            from datetime import datetime
        '''), text('''
            from datetime import datetime


            def parse_date(s):
                return datetime.strptime(s, "%Y-%m-%d").date()
        ''')),
    },
    open="utils.py",
    hint="From a blank line, dap deletes the blank lines and the function after them, exactly what each new file "
         "needs below its import. Ctrl-^ brings you back to utils.py for the second function.",
    uses=["ip", "paragraph", "p"],
)
edit.add(
    title="There and back again", par=21,
    task="Make Circle.java match Square.java's style: put an @Override line above Circle's area method, and copy "
         "Square's toString method (with its @Override line and the blank line above them) to the end of Circle, "
         "after area. Your cursor starts on Circle's area method.",
    files={
        "Circle.java": (text('''
            public class Circle implements Shape {
                private final double r;

                public Circle(double r) { this.r = r; }

                public double area() { return Math.PI * r * r; }
            }
        '''), text('''
            public class Circle implements Shape {
                private final double r;

                public Circle(double r) { this.r = r; }

                @Override
                public double area() { return Math.PI * r * r; }

                @Override
                public String toString() { return getClass().getSimpleName() + " with area " + area(); }
            }
        ''')),
        "Square.java": (text('''
            public class Square implements Shape {
                private final double side;

                public Square(double side) { this.side = side; }

                @Override
                public double area() { return side * side; }

                @Override
                public String toString() { return getClass().getSimpleName() + " with area " + area(); }
            }
        '''),) * 2,
    },
    open="Circle.java", cursor=(6, 5),
    hint="Two trips to Square.java: one to yank the @Override line, one for the last three lines. Ctrl-^ goes "
         "back and forth, and each file keeps its cursor where you left it.",
    uses=["y", "p", "count"],
)
edit.add(
    title="The second match", par=15,
    task="Production must not run in debug mode: in config.prod.toml, change debug = true to debug = false. Leave "
         "config.dev.toml alone. You start in app.py.",
    files={
        "app.py": (text('''
            import tomllib

            with open("config.prod.toml", "rb") as f:
                CONFIG = tomllib.load(f)
        '''),) * 2,
        "config.dev.toml": (text('''
            [server]
            host = "127.0.0.1"
            port = 8000
            debug = true
        '''),) * 2,
        "config.prod.toml": (text('''
            [server]
            host = "0.0.0.0"
            port = 8080
            debug = true
        '''), text('''
            [server]
            host = "0.0.0.0"
            port = 8080
            debug = false
        ''')),
    },
    open="app.py",
    hint="Both config files start with c. The first Tab fills in the first one, config.dev.toml, and a second Tab "
         "moves on to the next. In the file, debug is on the last line.",
    uses=["gg", "insert", "ctrl-w"],
)
edit.add(
    title="One header, two new scripts", par=16,
    task="build.sh and deploy.sh are new and still empty. Give each one the same first two lines as lib.sh: the "
         "#! line and set -euo pipefail. You start at the top of lib.sh.",
    files={
        "lib.sh": (text('''
            #!/usr/bin/env bash
            set -euo pipefail

            log() { printf '%s\\n' "$*" >&2; }
        '''),) * 2,
        "build.sh": ("", text('''
            #!/usr/bin/env bash
            set -euo pipefail
        ''')),
        "deploy.sh": ("", text('''
            #!/usr/bin/env bash
            set -euo pipefail
        ''')),
    },
    open="lib.sh",
    hint="Yank the lines once: the register is still full in the next file, and in the one after that. In an "
         "empty file, P puts the lines above the empty line.",
    uses=["y", "count", "p"],
)
edit.add(
    title="Where you just were", par=11,
    task="You opened main.c from config.h a moment ago, so config.h is the alternate file. In config.h, the log "
         "level should be LOG_WARN, not LOG_DEBUG.",
    files={
        "main.c": (text('''
            #include "config.h"

            int main(void)
            {
                log_init(LOG_LEVEL);
                return run(BUF_SIZE);
            }
        '''),) * 2,
        "config.h": (text('''
            #ifndef CONFIG_H
            #define CONFIG_H

            #define LOG_LEVEL LOG_DEBUG
            #define BUF_SIZE 4096

            #endif
        '''), text('''
            #ifndef CONFIG_H
            #define CONFIG_H

            #define LOG_LEVEL LOG_WARN
            #define BUF_SIZE 4096

            #endif
        ''')),
    },
    open="main.c", setup=["edit config.h", "edit #"],
    hint="Ctrl-^ goes straight to the alternate file, no name needed. The cursor is where you left it there: on "
         "line 1.",
    uses=["count", "f", "c"],
)
edit.add(
    title="The search comes along", par=25,
    task="Rename MAX_RETRIES to RETRY_LIMIT, here in constants.py and everywhere in client.py. You start on its "
         "definition.",
    files={
        "constants.py": (text('''
            MAX_RETRIES = 3
            TIMEOUT_SECONDS = 10
        '''), text('''
            RETRY_LIMIT = 3
            TIMEOUT_SECONDS = 10
        ''')),
        "client.py": (text('''
            from constants import MAX_RETRIES, TIMEOUT_SECONDS


            def fetch(url):
                for attempt in range(MAX_RETRIES):
                    resp = get(url, timeout=TIMEOUT_SECONDS)
                    if resp.ok:
                        return resp
        '''), text('''
            from constants import RETRY_LIMIT, TIMEOUT_SECONDS


            def fetch(url):
                for attempt in range(RETRY_LIMIT):
                    resp = get(url, timeout=TIMEOUT_SECONDS)
                    if resp.ok:
                        return resp
        ''')),
    },
    open="constants.py",
    hint="* searches for the word under the cursor. The search and the last change both stay with you when you "
         "open another file, so there n finds the next one and . renames it.",
    uses=["star", "c", "search", "dot"],
)
edit.add(
    title="The same :s over there", par=24,
    task="Rename the btn-cta class to btn-primary, both in index.html (you're here) and in style.css.",
    files={
        "index.html": (text('''
            <form>
                <button class="btn-cta">Save</button>
                <a class="btn-cta" href="/cancel">Cancel</a>
            </form>
        '''), text('''
            <form>
                <button class="btn-primary">Save</button>
                <a class="btn-primary" href="/cancel">Cancel</a>
            </form>
        ''')),
        "style.css": (text('''
            .btn-cta {
                background: #2563eb;
                color: white;
            }
        '''), text('''
            .btn-primary {
                background: #2563eb;
                color: white;
            }
        ''')),
    },
    open="index.html",
    hint="Do it here with :%s. In style.css, @: would repeat the :e you used to get there, but g& repeats the last "
         ":s on every line.",
    uses=["subst", "range", "amp"],
)
edit.add(
    title="An example file", par=21,
    task=".env holds real secrets. Fill the empty .env.example with the same lines, but with nothing after each =. "
         "You start at the top of .env.",
    files={
        ".env": (text('''
            DATABASE_URL=postgres://ada:hunter2@db.internal/shop
            REDIS_URL=redis://cache.internal:6379/0
            SECRET_KEY=8f3c9b1e7a
        '''),) * 2,
        ".env.example": ("", text('''
            DATABASE_URL=
            REDIS_URL=
            SECRET_KEY=
        ''')),
    },
    open=".env",
    hint="Yank the whole file, open the other one (two Tabs: .env comes first), put the lines there, and then one "
         ":s clears everything after the = on every line.",
    uses=["y", "gg", "p", "subst", "range"],
)
edit.add(
    title="One line, two places", par=17,
    task="Both functions in api.py should retry the way sync.py's sync_all() does: copy its @retry line from "
         "sync.py to above each def in api.py. You start at the top of api.py.",
    files={
        "api.py": (text('''
            import requests


            def fetch_user(uid):
                return requests.get(f"/users/{uid}")


            def fetch_order(oid):
                return requests.get(f"/orders/{oid}")
        '''), text('''
            import requests


            @retry(attempts=5, backoff=1.5, on=(TimeoutError,))
            def fetch_user(uid):
                return requests.get(f"/users/{uid}")


            @retry(attempts=5, backoff=1.5, on=(TimeoutError,))
            def fetch_order(oid):
                return requests.get(f"/orders/{oid}")
        ''')),
        "sync.py": (text('''
            from resilience import retry


            @retry(attempts=5, backoff=1.5, on=(TimeoutError,))
            def sync_all():
                return [sync(job) for job in pending()]
        '''),) * 2,
    },
    open="api.py",
    hint="Yank the line in sync.py and Ctrl-^ back. P puts it above the first def, and . puts it again above the "
         "second one.",
    uses=["y", "p", "count", "dot"],
)
edit.add(
    title="Fill in the placeholder", par=16,
    task="Move the Install section out of README.md into docs/install.md: the heading, its blank line and the pip "
         "line replace the TODO there, with the heading one level up (# Install). README.md keeps one blank line "
         "between its intro and ## Usage. You start at the top of README.md.",
    files={
        "README.md": (text('''
            # acme

            Small widgets for terminal apps.

            ## Install

            pip install acme-widgets

            ## Usage

            Run acme --help.
        '''), text('''
            # acme

            Small widgets for terminal apps.

            ## Usage

            Run acme --help.
        ''')),
        "docs/install.md": ("TODO", text('''
            # Install

            pip install acme-widgets
        ''')),
    },
    open="README.md",
    hint="4dd from the heading takes the section and the blank line after it. In docs/install.md, V selects the "
         "TODO line and p replaces it with those lines; then x deletes one #.",
    uses=["dd", "count", "visual-line", "p", "x"],
)
edit.add(
    title="Two values, two files", par=36,
    task="Fill in the runbook from the deployment files: the Image TODO is the image from k8s.yaml, and the Port "
         "TODO is the host port from compose.yml (the 8080 in \"8080:80\"). You start at the top of runbook.md.",
    files={
        "runbook.md": (text('''
            # Deploying web

            Image: TODO
            Port: TODO
        '''), text('''
            # Deploying web

            Image: ghcr.io/acme/web:1.8.2
            Port: 8080
        ''')),
        "k8s.yaml": (text('''
            apiVersion: apps/v1
            kind: Deployment
            spec:
              template:
                spec:
                  containers:
                    - name: web
                      image: ghcr.io/acme/web:1.8.2
        '''),) * 2,
        "compose.yml": (text('''
            services:
              web:
                image: ghcr.io/acme/web:1.8.2
                ports: ["8080:80"]
        '''),) * 2,
    },
    open="runbook.md",
    hint="Yank each value with a text object (the image is one WORD), come back with Ctrl-^, and replace the TODO "
         "with ve and p. Ctrl-^ brings you back to the TODO you left.",
    uses=["gg", "y", "iw-big", "visual", "p", "f"],
)
edit.add(
    title="Release in three files", par=31,
    task="Release 1.5.0: the version in pyproject.toml (you're here) and in acme/__init__.py becomes \"1.5.0\", and "
         "the Unreleased heading in CHANGELOG.md becomes 1.5.0.",
    files={
        "pyproject.toml": (text('''
            [project]
            name = "acme"
            version = "1.4.2"
        '''), text('''
            [project]
            name = "acme"
            version = "1.5.0"
        ''')),
        "acme/__init__.py": (text('''
            __version__ = "1.4.2"
        '''), text('''
            __version__ = "1.5.0"
        ''')),
        "CHANGELOG.md": (text('''
            # Changelog

            ## Unreleased

            - Add the Spinner widget.

            ## 1.4.2

            - Fix the progress bar on narrow terminals.
        '''), text('''
            # Changelog

            ## 1.5.0

            - Add the Spinner widget.

            ## 1.4.2

            - Fix the progress bar on narrow terminals.
        ''')),
    },
    open="pyproject.toml",
    hint="ci\" works from anywhere on the line, so . repeats it in __init__.py, where the version is on line 1. In "
         "the changelog, the heading isn't quoted, but Ctrl-a in Insert mode types 1.5.0 again.",
    uses=["count", "quote", "dot", "word", "c", "ctrl-a-insert"],
)

# ---------- :ls :b :bn :bp ----------

buffers = drills.command(
    "buffers", ":ls  :b {name}  :bn  :bp", "switch between open buffers",
    """A buffer is a file Neovim has open; it stays in the buffer list until you quit, and :ls shows the list with
    numbers (% the current buffer, # the alternate, + unsaved changes). :b {piece} switches to the buffer whose
    name contains that piece anywhere, as long as only one does: :b Gate finds src/PaymentGateway.java, and on
    E93 (more than one match) you add letters or press Tab to cycle. The piece is also checked against the folders
    in each full path, so one that's in them, like se in /Users, matches every buffer, and then only a name that
    starts or ends with it counts. :b 3 or 3 Ctrl-^ switches by number, and :bn and :bp (]b and [b) step through
    the list in :ls order, wrapping around at the ends.""",
    examples=[(":b Repo", "the buffer with Repo in its name"), (":b 3", "buffer number 3"),
              ("3 Ctrl-^", "also buffer 3"), ("]b  [b", "next / previous buffer"), (":ls", "list the buffers")],
)
buffers.add(
    title="Switch by name", par=14,
    task="Four files are open as buffers: app.py, models.py, urls.py and views.py. In views.py, article_list "
         "renders the wrong template: change \"home.html\" to \"list.html\".",
    files={
        "app.py": (text('''
            from django.core.wsgi import get_wsgi_application

            application = get_wsgi_application()
        '''),) * 2,
        "models.py": (text('''
            from django.db import models


            class Article(models.Model):
                title = models.CharField(max_length=200)
        '''),) * 2,
        "urls.py": (text('''
            from django.urls import path

            from . import views

            urlpatterns = [path("", views.article_list)]
        '''),) * 2,
        "views.py": (text('''
            from django.shortcuts import render


            def article_list(request):
                return render(request, "home.html")
        '''), text('''
            from django.shortcuts import render


            def article_list(request):
                return render(request, "list.html")
        ''')),
    },
    open="app.py", setup=badd("urls.py", "views.py", "models.py"),
    hint=":b takes any piece of a buffer's name, and one letter is enough when no other name has it: v. In "
         "views.py the template is on the last line.",
    uses=["gg", "f", "c"],
)
buffers.add(
    title="Move a line to another buffer", par=8,
    task="app.py imports requests but doesn't use it, and client.py uses requests without importing it. Move the "
         "import requests line from app.py to client.py, below import os. client.py, models.py and utils.py are "
         "open as buffers. Your cursor starts on the import.",
    files={
        "app.py": (text('''
            import json
            import requests

            from models import User

            print(json.dumps({"ok": True}))
        '''), text('''
            import json

            from models import User

            print(json.dumps({"ok": True}))
        ''')),
        "client.py": (text('''
            import os


            def fetch_user(user_id):
                url = os.environ["API"] + f"/users/{user_id}"
                return requests.get(url, timeout=5).json()
        '''), text('''
            import os
            import requests


            def fetch_user(user_id):
                url = os.environ["API"] + f"/users/{user_id}"
                return requests.get(url, timeout=5).json()
        ''')),
        "models.py": (text('''
            from dataclasses import dataclass


            @dataclass
            class User:
                name: str
        '''),) * 2,
        "utils.py": (text('''
            def chunks(items, n):
                return [items[i:i + n] for i in range(0, len(items), n)]
        '''),) * 2,
    },
    open="app.py", cursor=(2, 1), setup=badd("utils.py", "client.py", "models.py"),
    hint="dd cuts the line, :b c switches to client.py (no other buffer name starts with c), and p puts the line "
         "below the cursor.",
    uses=["dd", "p"],
)
buffers.add(
    title="A piece from the middle", par=16,
    task="conftest.py is open, and so are test_api.py, test_auth.py and test_models.py. In test_auth.py, the "
         "test should check that a wrong password is rejected: change is True to is False.",
    files={
        "conftest.py": (text('''
            import pytest


            @pytest.fixture
            def client():
                from app import create_app
                return create_app().test_client()
        '''),) * 2,
        "test_api.py": (text('''
            def test_health(client):
                assert client.get("/health").status_code == 200
        '''),) * 2,
        "test_auth.py": (text('''
            from app import login


            def test_login_rejects_bad_password():
                assert login("ada", "wrong") is True
        '''), text('''
            from app import login


            def test_login_rejects_bad_password():
                assert login("ada", "wrong") is False
        ''')),
        "test_models.py": (text('''
            from app.models import User


            def test_user_name():
                assert User("ada").name == "ada"
        '''),) * 2,
    },
    open="conftest.py", setup=badd("test_models.py", "test_auth.py", "test_api.py"),
    hint="Every test file starts with test_, so :b test matches three buffers (E93). Use a piece only test_auth.py "
         "has: two letters of auth are enough. True is the last word in the file.",
    uses=["gg", "line", "iw", "c"],
)
buffers.add(
    title="Two buffers, two fixes", par=20,
    task="main.c is open, and so are queue.c, stack.c and util.h. In queue.c, delete the extra ; at the end of the "
         "return line. In util.h, the MIN macro compares the wrong way: change its > to <.",
    files={
        "main.c": (text('''
            #include <stdio.h>
            #include "queue.h"

            int main(void)
            {
                struct queue q = {0};
                printf("%d\\n", queue_len(&q));
                return 0;
            }
        '''),) * 2,
        "queue.c": (text('''
            #include "util.h"

            int queue_len(const struct queue *q)
            {
                return q->tail - q->head;;
            }
        '''), text('''
            #include "util.h"

            int queue_len(const struct queue *q)
            {
                return q->tail - q->head;
            }
        ''')),
        "stack.c": (text('''
            #include "util.h"

            int stack_len(const struct stack *s)
            {
                return s->top;
            }
        '''),) * 2,
        "util.h": (text('''
            #ifndef UTIL_H
            #define UTIL_H

            #define MAX(a, b) ((a) > (b) ? (a) : (b))
            #define MIN(a, b) ((a) > (b) ? (a) : (b))

            #endif
        '''), text('''
            #ifndef UTIL_H
            #define UTIL_H

            #define MAX(a, b) ((a) > (b) ? (a) : (b))
            #define MIN(a, b) ((a) < (b) ? (a) : (b))

            #endif
        ''')),
    },
    open="main.c", setup=badd("util.h", "stack.c", "queue.c"),
    hint=":b q and :b u each match just one buffer. In queue.c the return line is the second to last, and in "
         "util.h, f> on the MIN line finds the >.",
    uses=["gg", "line", "x", "f", "r", "count"],
)
buffers.add(
    title="The next buffer", par=15,
    task="Three chapters are open as buffers, in this order: 01-intro.md (you're here), 02-install.md and "
         "03-usage.md. In 02-install.md, the minimum version should be Python 3.9, not 3.8. In 03-usage.md, fix "
         "the typo stpo (it should be stop).",
    files={
        "01-intro.md": (text('''
            # Introduction

            acme-widgets draws spinners and progress bars in the terminal.
        '''),) * 2,
        "02-install.md": (text('''
            # Installation

            Install it with pip install acme-widgets.
            Python 3.8 or newer is required.
        '''), text('''
            # Installation

            Install it with pip install acme-widgets.
            Python 3.9 or newer is required.
        ''')),
        "03-usage.md": (text('''
            # Usage

            Call spinner.start() before the work and spinner.stpo() after it.
        '''), text('''
            # Usage

            Call spinner.start() before the work and spinner.stop() after it.
        ''')),
    },
    open="01-intro.md", setup=badd("02-install.md", "03-usage.md"),
    hint="]b goes to the next buffer in the list, the one :bn would. In each file, jump to the line, then r or xp "
         "makes the fix.",
    uses=["gg", "f", "r", "search", "x", "p"],
)
buffers.add(
    title="Around the end", par=14,
    task="Four classes are open as buffers, in this order: Main.java (you're here), Lexer.java, Parser.java and "
         "Token.java. In Token.java, rename the component txt to text. In Parser.java, pos should start at 0.",
    files={
        "Main.java": (text('''
            public class Main {
                public static void main(String[] args) {
                    System.out.println(new Parser(new Lexer(args[0]).tokens()).parse());
                }
            }
        '''),) * 2,
        "Lexer.java": (text('''
            public class Lexer {
                private final String src;

                public Lexer(String src) { this.src = src; }
            }
        '''),) * 2,
        "Parser.java": (text('''
            public class Parser {
                private final java.util.List<Token> tokens;
                private int pos = 1;
            }
        '''), text('''
            public class Parser {
                private final java.util.List<Token> tokens;
                private int pos = 0;
            }
        ''')),
        "Token.java": (text('''
            public record Token(Kind kind, String txt) {
                enum Kind { NUMBER, PLUS, MINUS, LPAREN, RPAREN }
            }
        '''), text('''
            public record Token(Kind kind, String text) {
                enum Kind { NUMBER, PLUS, MINUS, LPAREN, RPAREN }
            }
        ''')),
    },
    open="Main.java", setup=badd("Lexer.java", "Parser.java", "Token.java"),
    hint="[b goes to the previous buffer, and from the first one it wraps around to the last. Ctrl-x subtracts 1 "
         "from the next number on the line.",
    uses=["search", "insert", "increment", "count"],
)
buffers.add(
    title="Same fix, every buffer", par=9,
    task="Three scripts are open as buffers: backup.py (you're here), cleanup.py and report.py. Their first "
         "lines still ask for python: make each one end in python3.",
    files={
        "backup.py": (text('''
            #!/usr/bin/env python
            import shutil

            shutil.copytree("data", "backup/data", dirs_exist_ok=True)
        '''), text('''
            #!/usr/bin/env python3
            import shutil

            shutil.copytree("data", "backup/data", dirs_exist_ok=True)
        ''')),
        "cleanup.py": (text('''
            #!/usr/bin/env python
            import pathlib

            for p in pathlib.Path("tmp").glob("*.log"):
                p.unlink()
        '''), text('''
            #!/usr/bin/env python3
            import pathlib

            for p in pathlib.Path("tmp").glob("*.log"):
                p.unlink()
        ''')),
        "report.py": (text('''
            #!/usr/bin/env python
            import csv
            import sys

            rows = list(csv.reader(open(sys.argv[1])))
            print(len(rows), "rows")
        '''), text('''
            #!/usr/bin/env python3
            import csv
            import sys

            rows = list(csv.reader(open(sys.argv[1])))
            print(len(rows), "rows")
        ''')),
    },
    open="backup.py", setup=badd("cleanup.py", "report.py"),
    hint="Make the change once with A, then ]b visits the next buffer, where the cursor starts on line 1, and . "
         "repeats the change.",
    uses=["insert", "dot"],
)
buffers.add(
    title="Look up the number", par=10,
    task="index.md and five daily notes are open as buffers, in the order you opened them, which isn't date "
         "order. In the notes for March 6 (2024-03-06.md), tick the first item: change [ ] to [x].",
    files={
        "index.md": (text('''
            # Notes

            One file per day, named by date.
        '''),) * 2,
        "2024-03-04.md": ("- [x] plan the sprint",) * 2,
        "2024-03-05.md": ("- [x] review the parser PR",) * 2,
        "2024-03-06.md": (text('''
            - [ ] fix the flaky upload test
            - [x] standup
        '''), text('''
            - [x] fix the flaky upload test
            - [x] standup
        ''')),
        "2024-03-07.md": ("- [ ] write the release notes",) * 2,
        "2024-03-08.md": ("- [ ] release 1.5",) * 2,
    },
    open="index.md",
    setup=badd("2024-03-08.md", "2024-03-05.md", "2024-03-06.md", "2024-03-04.md", "2024-03-07.md"),
    hint=":b 06 would go to buffer number 6, not to the file with 06 in its name. :ls shows each buffer's number, "
         "and N Ctrl-^ (or :b N) jumps to buffer N. You can type it straight at the Press ENTER prompt.",
    uses=["edit", "t", "r"],
)
buffers.add(
    title="Swap two functions", par=18,
    task="connect is in cli.py but belongs in net.py, and parse_args is in net.py but belongs in cli.py. Move "
         "each one to the end of the other file, with the two blank lines above it. cli.py, models.py and net.py "
         "are open as buffers. Your cursor starts on def connect.",
    files={
        "cli.py": (text('''
            import argparse
            import socket


            def connect(host, port):
                return socket.create_connection((host, port), timeout=5)


            def main():
                print("usage: cli HOST PORT")
        '''), text('''
            import argparse
            import socket


            def main():
                print("usage: cli HOST PORT")


            def parse_args(argv):
                p = argparse.ArgumentParser()
                p.add_argument("host")
                return p.parse_args(argv)
        ''')),
        "models.py": (text('''
            from dataclasses import dataclass


            @dataclass
            class Host:
                name: str
                port: int
        '''),) * 2,
        "net.py": (text('''
            import argparse
            import socket


            def parse_args(argv):
                p = argparse.ArgumentParser()
                p.add_argument("host")
                return p.parse_args(argv)
        '''), text('''
            import argparse
            import socket


            def connect(host, port):
                return socket.create_connection((host, port), timeout=5)
        ''')),
    },
    open="cli.py", cursor=(5, 1), setup=badd("models.py", "net.py"),
    hint="{ goes up to the blank line above the function, and dap from there takes the blank lines and the "
         "function. In net.py, G and p put it at the end. Then { and dap again for parse_args, and Ctrl-^ takes "
         "you back to cli.py.",
    uses=["paragraph", "ip", "gg", "p", "edit"],
)
buffers.add(
    title="Three fixes in a Java tree", par=38,
    task="App.java is open, and so are Cart.java, PaymentGateway.java and StripeClient.java, deep in "
         "src/main/java/shop/. Fix one thing in each: in Cart.java, delete the doubled ; at the end of the items "
         "line; in PaymentGateway.java, charge returns boolean, not void; in StripeClient.java, the timeout is 30 "
         "seconds, not 3.",
    files={
        "src/main/java/shop/App.java": (text('''
            package shop;

            public class App {
                public static void main(String[] args) {
                    System.out.println("shop is running");
                }
            }
        '''),) * 2,
        "src/main/java/shop/cart/Cart.java": (text('''
            package shop.cart;

            public class Cart {
                private java.util.List<String> items = new java.util.ArrayList<>();;
            }
        '''), text('''
            package shop.cart;

            public class Cart {
                private java.util.List<String> items = new java.util.ArrayList<>();
            }
        ''')),
        "src/main/java/shop/payment/PaymentGateway.java": (text('''
            package shop.payment;

            public interface PaymentGateway {
                void charge(String customer, long cents);
            }
        '''), text('''
            package shop.payment;

            public interface PaymentGateway {
                boolean charge(String customer, long cents);
            }
        ''')),
        "src/main/java/shop/payment/StripeClient.java": (text('''
            package shop.payment;

            public class StripeClient {
                static final int TIMEOUT_SECONDS = 3;
            }
        '''), text('''
            package shop.payment;

            public class StripeClient {
                static final int TIMEOUT_SECONDS = 30;
            }
        ''')),
    },
    open="src/main/java/shop/App.java",
    setup=badd("src/main/java/shop/payment/StripeClient.java", "src/main/java/shop/cart/Cart.java",
               "src/main/java/shop/payment/PaymentGateway.java"),
    hint="In each :b, use a short piece that only one buffer's path has: ca for Cart, g for Gateway, st for "
         "Stripe. Each fix is on the last line but one, and G- gets there: - goes to the first non-blank of the "
         "line above.",
    uses=["gg", "plus", "line", "x", "c", "insert"],
)
buffers.add(
    title="A piece of the folder", par=7,
    task="Two index.ts files are open as buffers, src/api/index.ts and src/ui/index.ts, and you're in src/app.ts. "
         "In the API one, the base URL should be /api/v2, not /api/v1.",
    files={
        "src/app.ts": (text('''
            import { BASE_URL } from "./api";
            import { Button } from "./ui";

            console.log(BASE_URL, Button);
        '''),) * 2,
        "src/api/index.ts": (text('''
            export const BASE_URL = "/api/v1";
            export const TIMEOUT_MS = 5000;
        '''), text('''
            export const BASE_URL = "/api/v2";
            export const TIMEOUT_MS = 5000;
        ''')),
        "src/ui/index.ts": (text('''
            export { Button } from "./Button";
            export { Modal } from "./Modal";
        '''),) * 2,
    },
    open="src/app.ts", setup=badd("src/ui/index.ts", "src/api/index.ts"),
    hint="The file names are the same, but :b looks at the folders too: a piece of api that app.ts doesn't have is "
         "enough. Then Ctrl-a adds 1 to the first number on the line.",
    uses=["increment"],
)
buffers.add(
    title="Two buffers on", par=13,
    task="Six chapters are open as buffers, in this order: intro.md (you're here), install.md, config.md, usage.md, "
         "api.md and faq.md. Fix the heading typos in install.md (Isntall) and usage.md (Usgae).",
    files={
        "intro.md": (text('''
            # Introduction

            acme draws spinners and progress bars.
        '''),) * 2,
        "install.md": (text('''
            # Isntall

            pip install acme
        '''), text('''
            # Install

            pip install acme
        ''')),
        "config.md": ("# Configuration",) * 2,
        "usage.md": (text('''
            # Usgae

            Call spinner.start() before the work.
        '''), text('''
            # Usage

            Call spinner.start() before the work.
        ''')),
        "api.md": ("# API",) * 2,
        "faq.md": ("# FAQ",) * 2,
    },
    open="intro.md", setup=badd("install.md", "config.md", "usage.md", "api.md", "faq.md"),
    hint="]b goes to the next buffer, and with a count it goes that many on: from install.md, 2]b skips config.md. "
         "xp swaps two letters.",
    uses=["count", "f", "x", "p"],
)
buffers.add(
    title="By its extension", par=18,
    task="models.py, views.py, README.md and schema.sql are open as buffers, and you're in models.py. In schema.sql, "
         "the email column must not be empty: make it email TEXT NOT NULL,",
    files={
        "models.py": (text('''
            from dataclasses import dataclass


            @dataclass
            class User:
                email: str
                name: str
        '''),) * 2,
        "views.py": (text('''
            def show(user):
                return f"{user.name} <{user.email}>"
        '''),) * 2,
        "README.md": ("# users",) * 2,
        "schema.sql": (text('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                email TEXT,
                name TEXT
            );
        '''), text('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                email TEXT NOT NULL,
                name TEXT
            );
        ''')),
    },
    open="models.py", setup=badd("README.md", "schema.sql", "views.py"),
    hint="The piece can come from anywhere in the name, extension included, and only one name here has a q.",
    uses=["count", "line", "insert"],
)
buffers.add(
    title="The middle of a long name", par=31,
    task="OrderService.java is open, and so are OrderRepository.java, OrderController.java and Order.java. In "
         "OrderRepository, find takes a long id, not an int. In OrderController, the path is /orders/{id}, not "
         "/order/{id}.",
    files={
        "src/main/java/shop/OrderService.java": (text('''
            package shop;

            class OrderService {
                private final OrderRepository repo;

                Order find(long id) { return repo.find(id); }
            }
        '''),) * 2,
        "src/main/java/shop/OrderRepository.java": (text('''
            package shop;

            interface OrderRepository {
                Order find(int id);
            }
        '''), text('''
            package shop;

            interface OrderRepository {
                Order find(long id);
            }
        ''')),
        "src/main/java/shop/OrderController.java": (text('''
            package shop;

            class OrderController {
                @GetMapping("/order/{id}")
                Order show(@PathVariable long id) { return service.find(id); }
            }
        '''), text('''
            package shop;

            class OrderController {
                @GetMapping("/orders/{id}")
                Order show(@PathVariable long id) { return service.find(id); }
            }
        ''')),
        "src/main/java/shop/Order.java": (text('''
            package shop;

            record Order(long id, long cents) {
            }
        '''),) * 2,
    },
    open="src/main/java/shop/OrderService.java",
    setup=badd("src/main/java/shop/OrderController.java", "src/main/java/shop/Order.java",
               "src/main/java/shop/OrderRepository.java"),
    hint="Every name starts with Order, so use two letters from the part that's different: only Repository has "
         "it in it, only Controller has ro.",
    uses=["count", "f", "c", "insert"],
)
buffers.add(
    title="Across the slash", par=15,
    task="Four views and urls files are open, in api/ and in web/, and you're in settings.py. In web/views.py, the "
         "template is web/home.html: put web/ in front of home.html.",
    files={
        "settings.py": ("INSTALLED_APPS = [\"api\", \"web\"]",) * 2,
        "api/views.py": (text('''
            from django.http import JsonResponse


            def home(request):
                return JsonResponse({"ok": True})
        '''),) * 2,
        "api/urls.py": ("urlpatterns = []",) * 2,
        "web/views.py": (text('''
            from django.shortcuts import render


            def home(request):
                return render(request, "home.html")
        '''), text('''
            from django.shortcuts import render


            def home(request):
                return render(request, "web/home.html")
        ''')),
        "web/urls.py": ("urlpatterns = []",) * 2,
    },
    open="settings.py", setup=badd("web/urls.py", "api/views.py", "web/views.py", "api/urls.py"),
    hint="views and web each match two buffers. The piece can run across the slash: the end of web, the slash "
         "and the start of views.",
    uses=["gg", "f", "insert"],
)
buffers.add(
    title="Three buffers, three fixes", par=35,
    task="pkg/__init__.py is open, and so are pkg/cli.py, pkg/db/models.py, pkg/web/urls.py and pkg/web/views.py. "
         "In models.py, titles may be 200 characters long, not 20. In views.py, the template is list.html, not "
         "list.htm. In cli.py, fix the typo store_ture.",
    files={
        "pkg/__init__.py": ("__version__ = \"0.1.0\"",) * 2,
        "pkg/cli.py": (text('''
            import argparse


            def main():
                p = argparse.ArgumentParser(prog="pkg")
                p.add_argument("--verbose", action="store_ture")
        '''), text('''
            import argparse


            def main():
                p = argparse.ArgumentParser(prog="pkg")
                p.add_argument("--verbose", action="store_true")
        ''')),
        "pkg/db/models.py": (text('''
            from django.db import models


            class Article(models.Model):
                title = models.CharField(max_length=20)
        '''), text('''
            from django.db import models


            class Article(models.Model):
                title = models.CharField(max_length=200)
        ''')),
        "pkg/web/urls.py": ("urlpatterns = []",) * 2,
        "pkg/web/views.py": (text('''
            from django.shortcuts import render


            def article_list(request):
                return render(request, "list.htm")
        '''), text('''
            from django.shortcuts import render


            def article_list(request):
                return render(request, "list.html")
        ''')),
    },
    open="pkg/__init__.py",
    setup=badd("pkg/web/views.py", "pkg/cli.py", "pkg/web/urls.py", "pkg/db/models.py"),
    hint="Find two letters only one path has: db for models.py, ew for views.py (vi and ur also appear in the "
         "folders around the course), cl for cli.py. Each fix is on the last line.",
    uses=["gg", "count", "increment", "line", "insert", "x", "p"],
)
buffers.add(
    title="Skip the one that's done", par=13,
    task="Five scripts are open, in this order: backup.py (you're here), cleanup.py, report.py, sync.py and "
         "upload.py. Their first lines should end in python3. report.py already does: leave it alone.",
    files={
        "backup.py": ("#!/usr/bin/env python\nimport shutil", "#!/usr/bin/env python3\nimport shutil"),
        "cleanup.py": ("#!/usr/bin/env python\nimport pathlib", "#!/usr/bin/env python3\nimport pathlib"),
        "report.py": ("#!/usr/bin/env python3\nimport csv",) * 2,
        "sync.py": ("#!/usr/bin/env python\nimport rsync", "#!/usr/bin/env python3\nimport rsync"),
        "upload.py": ("#!/usr/bin/env python\nimport boto3", "#!/usr/bin/env python3\nimport boto3"),
    },
    open="backup.py", setup=badd("cleanup.py", "report.py", "sync.py", "upload.py"),
    hint="Make the change once, then ]b and . for each script. 2]b jumps over report.py.",
    uses=["insert", "dot", "count"],
)
buffers.add(
    title="Collect the TODOs", par=22,
    task="TODO.md is open, and so are app.py and db.py. Move the TODO comment line out of each of them into "
         "TODO.md, below the heading: app.py's first, then db.py's.",
    files={
        "TODO.md": ("# TODO", text('''
            # TODO
            # TODO: retry on timeout
            # TODO: add an index on email
        ''')),
        "app.py": (text('''
            import requests

            # TODO: retry on timeout
            resp = requests.get("https://api.acme.dev/health", timeout=5)
        '''), text('''
            import requests

            resp = requests.get("https://api.acme.dev/health", timeout=5)
        ''')),
        "db.py": (text('''
            import sqlite3

            conn = sqlite3.connect("shop.db")

            # TODO: add an index on email
            conn.execute("CREATE TABLE IF NOT EXISTS users (email TEXT)")
        '''), text('''
            import sqlite3

            conn = sqlite3.connect("shop.db")

            conn.execute("CREATE TABLE IF NOT EXISTS users (email TEXT)")
        ''')),
    },
    open="TODO.md", setup=badd("db.py", "app.py"),
    hint="After :b, Ctrl-^ goes straight back to TODO.md, the buffer you came from. a and d are in the folder "
         "names around the course, but only one buffer's name starts with each.",
    uses=["count", "dd", "edit", "p"],
)
buffers.add(
    title="Repeat it in two others", par=50,
    task="models.py (you're here), schemas.py, services.py, urls.py and views.py are open as buffers. Give models.py, "
         "schemas.py and services.py a new first line: from __future__ import annotations",
    files={
        "models.py": ("class User:\n    name: str", "from __future__ import annotations\nclass User:\n    name: str"),
        "schemas.py": ("class UserSchema:\n    fields = (\"name\",)",
                       "from __future__ import annotations\nclass UserSchema:\n    fields = (\"name\",)"),
        "services.py": ("def create_user(name):\n    return User(name)",
                        "from __future__ import annotations\ndef create_user(name):\n    return User(name)"),
        "urls.py": ("urlpatterns = []",) * 2,
        "views.py": ("def index(request):\n    return None",) * 2,
    },
    open="models.py", setup=badd("views.py", "services.py", "urls.py", "schemas.py"),
    hint="Type the line once with O. In a buffer you haven't visited yet the cursor starts on line 1, so after :b, "
         ". does it there too. sc and rv pick the two other buffers.",
    uses=["o", "dot"],
)
buffers.add(
    title="Split a module three ways", par=22,
    task="utils.py keeps only chunks. slugify goes to the end of text.py and parse_date to the end of dates.py, each "
         "with the two blank lines above it. All three files are open as buffers, and you're at the top of utils.py.",
    files={
        "utils.py": (text('''
            import re
            from datetime import datetime


            def slugify(title):
                return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


            def parse_date(s):
                return datetime.strptime(s, "%Y-%m-%d").date()


            def chunks(items, n):
                return [items[i:i + n] for i in range(0, len(items), n)]
        '''), text('''
            import re
            from datetime import datetime


            def chunks(items, n):
                return [items[i:i + n] for i in range(0, len(items), n)]
        ''')),
        "text.py": (text('''
            import re


            def title_case(s):
                return s.title()
        '''), text('''
            import re


            def title_case(s):
                return s.title()


            def slugify(title):
                return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        ''')),
        "dates.py": (text('''
            from datetime import datetime
        '''), text('''
            from datetime import datetime


            def parse_date(s):
                return datetime.strptime(s, "%Y-%m-%d").date()
        ''')),
    },
    open="utils.py", setup=badd("dates.py", "text.py"),
    hint="From a blank line, dap takes the blank lines and the function after them. G and p put them at the end of "
         "the other buffer, and Ctrl-^ brings you back to utils.py right where the next function starts.",
    uses=["paragraph", "ip", "gg", "p", "edit"],
)

# ---------- Ctrl-w ----------

windows = drills.command(
    "windows", "Ctrl-w s v h j k l c o", "split windows and move between them",
    """A window is a view of a buffer, and each one keeps its own cursor. Ctrl-w s splits the current window one
    above the other and Ctrl-w v side by side (:sp {file} and :vs {file} also open a file in the new one).
    Ctrl-w h, j, k and l move to the window on the left, below, above or right, Ctrl-w w to the next one, Ctrl-w p
    back to the previous one and Ctrl-w b to the bottom-right one. Ctrl-w c closes a window and Ctrl-w o all the
    others, without closing their buffers. In these exercises Ctrl-w w also stops at the task window at the top,
    and closing your first window submits.""",
    examples=[("Ctrl-w v", "split side by side"), ("Ctrl-w l", "the window on the right"),
              ("Ctrl-w j", "the window below"), ("Ctrl-w p", "back to the previous window"),
              (":vs file.h", "open a file in a split"), ("Ctrl-w o", "close all the other windows")],
)
windows.add(
    title="Fix both sides", par=10,
    task="greet.py is on the left and its test on the right. In greet.py, fix the parameter name nmae (it should "
         "be name). In test_greet.py, add the missing ! to the expected string, so it reads \"Hello, Ada!\".",
    files={
        "greet.py": (text('''
            def greet(nmae):
                return f"Hello, {name}!"
        '''), text('''
            def greet(name):
                return f"Hello, {name}!"
        ''')),
        "test_greet.py": (text('''
            from greet import greet


            def test_greet():
                assert greet("Ada") == "Hello, Ada"
        '''), text('''
            from greet import greet


            def test_greet():
                assert greet("Ada") == "Hello, Ada!"
        ''')),
    },
    open="greet.py", setup=vsplit("test_greet.py"),
    hint="xp swaps two letters. Ctrl-w l moves to the window on the right, where G and $ reach the closing quote, "
         "and i types in front of it.",
    uses=["x", "p", "f", "gg", "line", "insert"],
)
windows.add(
    title="Copy into the other window", par=5,
    task="api.py, on the right, uses JsonResponse without importing it. Copy the import line from views.py (on "
         "the left, where your cursor is) to the top of api.py, above its other import.",
    files={
        "views.py": (text('''
            from django.http import JsonResponse
            from django.shortcuts import get_object_or_404

            from .models import Article


            def article(request, pk):
                a = get_object_or_404(Article, pk=pk)
                return JsonResponse({"title": a.title})
        '''),) * 2,
        "api.py": (text('''
            from django.views.decorators.http import require_GET


            @require_GET
            def health(request):
                return JsonResponse({"ok": True})
        '''), text('''
            from django.http import JsonResponse
            from django.views.decorators.http import require_GET


            @require_GET
            def health(request):
                return JsonResponse({"ok": True})
        ''')),
    },
    open="views.py", setup=vsplit("api.py"),
    hint="yy yanks the line, Ctrl-w l moves to the right window, and P puts the line above the cursor.",
    uses=["y", "p"],
)
windows.add(
    title="Move it up from below", par=10,
    task="queries.sql is on top and scratch.sql below it. The recent_orders query in scratch.sql is ready: move it, "
         "with the blank line above it, to the end of queries.sql. The EXPLAIN note stays in scratch.sql.",
    files={
        "queries.sql": (text('''
            -- name: active_users
            SELECT id, email FROM users WHERE active;
        '''), text('''
            -- name: active_users
            SELECT id, email FROM users WHERE active;

            -- name: recent_orders
            SELECT id, total FROM orders
            WHERE created_at > now() - interval '7 days';
        ''')),
        "scratch.sql": (text('''
            -- is the index used?
            EXPLAIN SELECT * FROM orders WHERE created_at > now();

            -- name: recent_orders
            SELECT id, total FROM orders
            WHERE created_at > now() - interval '7 days';
        '''), text('''
            -- is the index used?
            EXPLAIN SELECT * FROM orders WHERE created_at > now();
        ''')),
    },
    open="queries.sql", setup=split("scratch.sql"),
    hint="Ctrl-w j moves to the window below. } jumps to the blank line, and dap from there cuts it with the query "
         "after it. Ctrl-w k goes back up, and G then p puts the query at the end.",
    uses=["paragraph", "ip", "gg", "p"],
)
windows.add(
    title="Copy a block across", par=5,
    task="Put the logo from banner.txt (left) into cli.py (right), between the two lines of triple quotes. Only "
         "the four lines of the logo: not the blank line or the version line under it.",
    files={
        "banner.txt": (text(r'''
              __ _  ___ _ __ ___   ___
             / _` |/ __| '_ ` _ \ / _ \
            | (_| | (__| | | | | |  __/
             \__,_|\___|_| |_| |_|\___|

            acme 1.4 - terminal widgets
        '''),) * 2,
        "cli.py": (text('''
            BANNER = r"""
            """


            def main():
                print(BANNER)
        '''), text(r'''
            BANNER = r"""
              __ _  ___ _ __ ___   ___
             / _` |/ __| '_ ` _ \ / _ \
            | (_| | (__| | | | | |  __/
             \__,_|\___|_| |_| |_|\___|
            """


            def main():
                print(BANNER)
        ''')),
    },
    open="banner.txt", setup=vsplit("cli.py"),
    hint="y} yanks down to the blank line: all four lines of the logo. Ctrl-w l, then p puts them below the "
         "cursor's line.",
    uses=["y", "paragraph", "p"],
)
windows.add(
    title="Rename in both windows", par=10,
    task="Rename the user_name column to username, in models.py (left) and in schema.sql (right).",
    files={
        "models.py": (text('''
            class User(Model):
                user_name = CharField(max_length=40)
                email = CharField(max_length=120)
        '''), text('''
            class User(Model):
                username = CharField(max_length=40)
                email = CharField(max_length=120)
        ''')),
        "schema.sql": (text('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                user_name TEXT NOT NULL,
                email TEXT NOT NULL
            );
        '''), text('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            );
        ''')),
    },
    open="models.py", setup=vsplit("schema.sql"),
    hint="Delete the underscore in models.py with x. In the right window, search for _ and press . to repeat "
         "the x.",
    uses=["f", "x", "search", "dot"],
)
windows.add(
    title="Swap two lines", par=10,
    task="ads.example.net belongs in the blocklist, and pypi.org in the allowlist. Swap them: pypi.org takes the "
         "place of ads.example.net in allowlist.txt (left), and ads.example.net takes the place of pypi.org in "
         "blocklist.txt (right). Your cursor starts on ads.example.net.",
    files={
        "allowlist.txt": (text('''
            docs.python.org
            github.com
            ads.example.net
            stackoverflow.com
        '''), text('''
            docs.python.org
            github.com
            pypi.org
            stackoverflow.com
        ''')),
        "blocklist.txt": (text('''
            tracker.example.com
            doubleclick.net
            pypi.org
        '''), text('''
            tracker.example.com
            doubleclick.net
            ads.example.net
        ''')),
    },
    open="allowlist.txt", cursor=(3, 1), setup=vsplit("blocklist.txt"),
    hint="dd cuts the line. On the right, V selects pypi.org's line and p replaces it, and the line it replaced "
         "goes into the register. Back on the left, P puts it above the cursor.",
    uses=["dd", "visual-line", "p", "gg"],
)
windows.add(
    title="Three frames in a row", par=15,
    task="Three frames of a waving stick figure, left to right. frame1.txt is already correct. In frame2.txt, raise his "
         "right arm: the \\ on line 2 moves up to the end of line 1, as /. In frame3.txt, raise the other arm "
         "too: the / at the start of line 2 becomes a \\ at the start of line 1.",
    files={
        "frame1.txt": (text(r'''
             o
            /|\
            / \
        '''),) * 2,
        "frame2.txt": (text(r'''
             o
            /|\
            / \
        '''), text(r'''
             o/
            /|
            / \
        ''')),
        "frame3.txt": (text(r'''
             o/
            /|
            / \
        '''), text(r'''
            \o/
             |
            / \
        ''')),
    },
    open="frame1.txt",
    setup=["keepalt rightbelow vsplit frame3.txt", WINBAR, "keepalt leftabove vsplit frame2.txt", WINBAR,
           "wincmd h"],
    hint="Ctrl-w l (or Ctrl-w w) moves one window to the right. In frame2.txt, A types at the end of line 1, and "
         "j lands on the old arm, ready for x. In frame3.txt the cursor starts on the o: 0 goes to the start of the "
         "line, and r replaces one character without leaving Normal mode.",
    uses=["insert", "x", "line", "r"],
)
windows.add(
    title="Back with Ctrl-w p", par=14,
    task="app.py is top left, test_app.py top right, and fixtures.yml along the bottom. In test_app.py, fill in "
         "the empty string with Ada's email address from fixtures.yml.",
    files={
        "app.py": (text('''
            def load_user(data):
                return User(**data)
        '''),) * 2,
        "test_app.py": (text('''
            from app import load_user


            def test_load_user(fixtures):
                user = load_user(fixtures["ada"])
                assert user.email == ""
        '''), text('''
            from app import load_user


            def test_load_user(fixtures):
                user = load_user(fixtures["ada"])
                assert user.email == "ada.lovelace@example.org"
        ''')),
        "fixtures.yml": (text('''
            ada:
              name: Ada Lovelace
              email: ada.lovelace@example.org
        '''),) * 2,
    },
    open="app.py",
    setup=["keepalt rightbelow vsplit test_app.py", WINBAR, "keepalt botright split fixtures.yml", WINBAR,
           "2wincmd w"],
    hint="Put the cursor on the closing quote in test_app.py first. Ctrl-w j goes down to fixtures.yml, where the "
         "address is the last WORD of the last line: yiW yanks it. Ctrl-w p goes back to the window you came from, "
         "and P puts it before the quote.",
    uses=["gg", "line", "iw-big", "y", "p"],
)
windows.add(
    title="Bottom right, then left", par=20,
    task="Release 1.5.0: README.md is on top, CHANGELOG.md bottom left and VERSION bottom right. Change 1.4.2 to "
         "1.5.0 in the README's install line and in VERSION, and the Unreleased heading in CHANGELOG.md to 1.5.0.",
    files={
        "README.md": (text('''
            # acme

            Install it with pip install acme==1.4.2 and run acme --help.
        '''), text('''
            # acme

            Install it with pip install acme==1.5.0 and run acme --help.
        ''')),
        "CHANGELOG.md": (text('''
            # Changelog

            ## Unreleased

            - Add the Spinner widget.
        '''), text('''
            # Changelog

            ## 1.5.0

            - Add the Spinner widget.
        ''')),
        "VERSION": ("1.4.2", "1.5.0"),
    },
    open="README.md",
    setup=["keepalt botright split CHANGELOG.md", WINBAR, "keepalt rightbelow vsplit VERSION", WINBAR,
           "2wincmd w"],
    hint="cE changes to the end of a WORD, so it can replace 1.4.2 and Unreleased alike, and . repeats it. "
         "Ctrl-w b goes to the bottom-right window, and Ctrl-w h from there to its left.",
    uses=["gg", "f", "c", "bigword", "dot", "search"],
)
windows.add(
    title="Header, source and test", par=21,
    task="stack.c is on the left, stack.h top right and test_stack.c bottom right. Move the #define STACK_CAP line "
         "from test_stack.c into stack.h, just below #define STACK_H. Then in stack.c, the push check should use it: "
         "change 16 to STACK_CAP.",
    files={
        "stack.c": (text('''
            #include "stack.h"

            void stack_push(struct stack *s, int x)
            {
                if (s->top < 16)
                    s->items[s->top++] = x;
            }
        '''), text('''
            #include "stack.h"

            void stack_push(struct stack *s, int x)
            {
                if (s->top < STACK_CAP)
                    s->items[s->top++] = x;
            }
        ''')),
        "stack.h": (text('''
            #ifndef STACK_H
            #define STACK_H

            struct stack {
                int items[STACK_CAP];
                int top;
            };

            #endif
        '''), text('''
            #ifndef STACK_H
            #define STACK_H
            #define STACK_CAP 16

            struct stack {
                int items[STACK_CAP];
                int top;
            };

            #endif
        ''')),
        "test_stack.c": (text('''
            #include <assert.h>
            #include "stack.h"
            #define STACK_CAP 16

            int main(void)
            {
                struct stack s = {0};
                stack_push(&s, 1);
                assert(s.top == 1);
                return 0;
            }
        '''), text('''
            #include <assert.h>
            #include "stack.h"

            int main(void)
            {
                struct stack s = {0};
                stack_push(&s, 1);
                assert(s.top == 1);
                return 0;
            }
        ''')),
    },
    open="stack.c",
    setup=["keepalt rightbelow vsplit stack.h", WINBAR, "keepalt rightbelow split test_stack.c", WINBAR,
           "2wincmd w"],
    hint="Ctrl-w b goes straight to the bottom-right window. Cut the #define there, then Ctrl-w k goes up to "
         "stack.h. Back in stack.c (Ctrl-w h), don't type all of STACK_CAP: after S, Ctrl-n offers the capitalized "
         "words from the other windows' files, STACK_H first.",
    uses=["dd", "p", "count", "f", "c", "complete"],
)
windows.add(
    title="The search goes across", par=17,
    task="buf.h is on the left and buf.c on the right. The length parameter should be size_t len, not int len, in "
         "both. You start at the top of buf.h.",
    files={
        "buf.h": (text('''
            int buf_append(struct buf *b, const char *s, int len);
            void buf_free(struct buf *b);
        '''), text('''
            int buf_append(struct buf *b, const char *s, size_t len);
            void buf_free(struct buf *b);
        ''')),
        "buf.c": (text('''
            int buf_append(struct buf *b, const char *s, int len)
            {
                memcpy(b->data + b->used, s, len);
                b->used += len;
                return 0;
            }
        '''), text('''
            int buf_append(struct buf *b, const char *s, size_t len)
            {
                memcpy(b->data + b->used, s, len);
                b->used += len;
                return 0;
            }
        ''')),
    },
    open="buf.h", setup=vsplit("buf.c"),
    hint="Search for the int you want, change it with cw, and move right with Ctrl-w l. The search is the same in "
         "every window, so n finds the same spot there, and . repeats the change.",
    uses=["search", "c", "dot"],
)
windows.add(
    title="Down to the code", par=17,
    task="The --verbose flag is now called --debug: rename it in README.md (top) and in cli.py (below), everywhere. "
         "The cursor starts on verbose in the README.",
    files={
        "README.md": (text('''
            # acme

            Run acme --verbose to see each request.
        '''), text('''
            # acme

            Run acme --debug to see each request.
        ''')),
        "cli.py": (text('''
            import argparse

            p = argparse.ArgumentParser()
            p.add_argument("--verbose", action="store_true")
            args = p.parse_args()
            if args.verbose:
                print("verbose mode")
        '''), text('''
            import argparse

            p = argparse.ArgumentParser()
            p.add_argument("--debug", action="store_true")
            args = p.parse_args()
            if args.debug:
                print("debug mode")
        ''')),
    },
    open="README.md", cursor=(3, 12), setup=split("cli.py"),
    hint="* searches for the word under the cursor. After cw, Ctrl-w j goes down to cli.py, where n and . do each "
         "of the others.",
    uses=["star", "c", "search", "dot"],
)
windows.add(
    title="Three files in a row", par=25,
    task="dev.env, staging.env and prod.env are side by side, left to right, and you're in dev.env. Add the line "
         "LOG_LEVEL=info at the end of each.",
    files={
        "dev.env": ("APP_ENV=dev\nDB_HOST=localhost", "APP_ENV=dev\nDB_HOST=localhost\nLOG_LEVEL=info"),
        "staging.env": ("APP_ENV=staging\nDB_HOST=db.staging.internal\nCACHE=on",
                        "APP_ENV=staging\nDB_HOST=db.staging.internal\nCACHE=on\nLOG_LEVEL=info"),
        "prod.env": ("APP_ENV=prod\nDB_HOST=db.prod.internal",
                     "APP_ENV=prod\nDB_HOST=db.prod.internal\nLOG_LEVEL=info"),
    },
    open="dev.env",
    setup=["keepalt rightbelow vsplit prod.env", WINBAR, "keepalt leftabove vsplit staging.env", WINBAR,
           "wincmd h"],
    hint="Go and o add the line once. Ctrl-w l moves one window to the right, where G and . add it again: the "
         "dot doesn't care which window you're in.",
    uses=["gg", "o", "dot"],
)
windows.add(
    title="The real number", par=12,
    task="test_orders.py is on the left and fixtures.json on the right. The test should expect the fixture's "
         "total: replace the 0 with 4599. The cursor starts on the 0.",
    files={
        "test_orders.py": (text('''
            def test_order_total(load_fixture):
                order = load_fixture("order_8812")
                assert order.total == 0
        '''), text('''
            def test_order_total(load_fixture):
                order = load_fixture("order_8812")
                assert order.total == 4599
        ''')),
        "fixtures.json": (text('''
            {
              "order_8812": {
                "items": 3,
                "total": 4599
              }
            }
        '''),) * 2,
    },
    open="test_orders.py", cursor=(3, 27), setup=vsplit("fixtures.json"),
    hint="Yank the number in the right window, and Ctrl-w p takes you back. v selects the 0 alone, and p "
         "replaces it.",
    uses=["count", "line", "iw", "y", "visual", "p"],
)
windows.add(
    title="Plant the tree", par=12,
    task="Put the tree from tree.txt (right) to the left of the house in scene.txt (left), as a block: its four "
         "lines go in front of the house's last four lines.",
    files={
        "scene.txt": ("  /\\\n /  \\\n/____\\\n|  []|\n|____|",
                      "  /\\\n   ^   /  \\\n  ^^^ /____\\\n ^^^^^|  []|\n   |  |____|"),
        "tree.txt": ("   ^\n  ^^^\n ^^^^^\n   |",) * 2,
    },
    open="scene.txt", setup=vsplit("tree.txt"),
    hint="In tree.txt, the cursor starts on the first non-blank: 0 first, then Ctrl-v and $ select a block down to "
         "the end of every line. Back in scene.txt, P puts a block in front of the cursor on each line, padded to "
         "the same width.",
    uses=["block-edit", "count", "line", "p"],
)
windows.add(
    title="Find it over there", par=12,
    task="app.js (left) should get its own copy of formatPrice: copy the function from utils.js (right), with the "
         "blank line above it, to the end of app.js. The cursor starts on the formatPrice call.",
    files={
        "app.js": (text('''
            import { render } from "./ui.js";

            render(formatPrice(cart.total));
        '''), text('''
            import { render } from "./ui.js";

            render(formatPrice(cart.total));

            function formatPrice(cents) {
                return (cents / 100).toFixed(2) + " EUR";
            }
        ''')),
        "utils.js": (text('''
            export function slugify(s) {
                return s.toLowerCase().replace(/\\W+/g, "-");
            }

            function formatPrice(cents) {
                return (cents / 100).toFixed(2) + " EUR";
            }

            export function clamp(x, lo, hi) {
                return Math.min(hi, Math.max(lo, x));
            }
        '''),) * 2,
    },
    open="app.js", cursor=(3, 8), setup=vsplit("utils.js"),
    hint="* searches for formatPrice, and the search works in the other window too: n there jumps to the "
         "definition. { goes up to the blank line, and yap takes it with the function.",
    uses=["star", "search", "paragraph", "y", "ip", "gg", "p"],
)
windows.add(
    title="Round the grid", par=23,
    task="Four windows: README.md top left (you're here), docs.md top right, CHANGELOG.md bottom left and VERSION "
         "bottom right. Put VERSION's number in the README's install line (instead of 1.9.4) and in the changelog "
         "(instead of Unreleased).",
    files={
        "README.md": (text('''
            # acme

            pip install acme==1.9.4
        '''), text('''
            # acme

            pip install acme==2.0.0
        ''')),
        "docs.md": ("# Docs\n\nSee the README.",) * 2,
        "CHANGELOG.md": (text('''
            # Changelog

            ## Unreleased

            - Drop Python 3.8.
        '''), text('''
            # Changelog

            ## 2.0.0

            - Drop Python 3.8.
        ''')),
        "VERSION": ("2.0.0",) * 2,
    },
    open="README.md",
    setup=["keepalt rightbelow vsplit docs.md", WINBAR, "keepalt rightbelow split VERSION", WINBAR, "wincmd h",
           "keepalt rightbelow split CHANGELOG.md", WINBAR, "wincmd k"],
    hint="Ctrl-w b goes to the bottom-right window. After a p over a selection, the unnamed register holds the "
         "text you replaced, but \"0 still has your yank.",
    uses=["bigword", "y", "visual", "p", "yank0", "count", "word", "f"],
)
windows.add(
    title="Back and forth", par=29,
    task="deploy.sh (left) needs the host and port from inventory.ini (right): replace each TODO with the value "
         "after its = there. The cursor starts on HOST's line.",
    files={
        "deploy.sh": (text('''
            #!/bin/sh
            HOST=TODO
            PORT=TODO
            rsync -e "ssh -p $PORT" -a dist/ "deploy@$HOST:/srv/app/"
        '''), text('''
            #!/bin/sh
            HOST=10.0.3.17
            PORT=2222
            rsync -e "ssh -p $PORT" -a dist/ "deploy@$HOST:/srv/app/"
        ''')),
        "inventory.ini": (text('''
            [web]
            host = 10.0.3.17
            port = 2222
        '''),) * 2,
    },
    open="deploy.sh", cursor=(2, 1), setup=vsplit("inventory.ini"),
    hint="Each window keeps its own cursor, so after the first round trip, j moves to the next line in each. The "
         "host is a WORD (dots and all), TODO a word.",
    uses=["line", "iw-big", "iw", "y", "visual", "p"],
)
windows.add(
    title="Top, middle, bottom", par=14,
    task="Three route files are stacked: web.py (top, you're here), auth.py and api.py. The /login route belongs "
         "in auth.py, at its end, and /v1/health in api.py, at its end. The cursor starts on the /login line.",
    files={
        "web.py": (text('''
            routes = [
                ("/", home),
                ("/login", login),
                ("/v1/health", health),
            ]
        '''), text('''
            routes = [
                ("/", home),
            ]
        ''')),
        "auth.py": (text('''
            routes = [
                ("/logout", logout),
            ]
        '''), text('''
            routes = [
                ("/logout", logout),
                ("/login", login),
            ]
        ''')),
        "api.py": (text('''
            routes = [
                ("/v1/orders", orders),
            ]
        '''), text('''
            routes = [
                ("/v1/orders", orders),
                ("/v1/health", health),
            ]
        ''')),
    },
    open="web.py", cursor=(3, 1),
    setup=["keepalt rightbelow split api.py", WINBAR, "keepalt leftabove split auth.py", WINBAR, "wincmd k"],
    hint="Ctrl-w b goes straight to the bottom window, Ctrl-w k up one. In each target, the route goes above the "
         "closing ], so G and P.",
    uses=["dd", "gg", "p"],
)
windows.add(
    title="Release notes from the log", par=41,
    task="RELEASE.md is on top and commits.txt below. Move the feat: lines under ## Added and the fix: lines under "
         "## Fixed, in their order, as list items: feat: color themes becomes - color themes. commits.txt ends up "
         "empty.",
    files={
        "RELEASE.md": (text('''
            # 1.5.0

            ## Added

            ## Fixed
        '''), text('''
            # 1.5.0

            ## Added
            - spinner widget
            - color themes

            ## Fixed
            - progress bar on narrow terminals
            - crash on empty input
        ''')),
        "commits.txt": (text('''
            feat: spinner widget
            fix: progress bar on narrow terminals
            feat: color themes
            fix: crash on empty input
        '''), ""),
    },
    open="RELEASE.md", setup=split("commits.txt"),
    hint=":g/pat/d A appends each deleted line to register a. What's left is the fix: lines, and one more delete "
         "takes them. In RELEASE.md, one :s turns every \"word: \" at the start of a line into \"- \".",
    uses=["global", "append", "named", "gg", "p", "subst", "range"],
)

# ---------- gf ----------

gf = drills.command(
    "gf", "gf", "open the file under the cursor",
    """gf opens the file whose name is under the cursor. If the cursor isn't on a name, it uses the next one on
    the line, but # counts as part of a name, so on #include itself it tries to open "#include". It looks in the
    folders in 'path': by default the current file's folder, then the folder Neovim started in. Filetype plugins
    help: in Java, gf on util.Strings in an import opens util/Strings.java, and in Python gf on shop.cart opens
    shop/cart.py. gf is a jump, so Ctrl-o comes back (after any jumps you made in the new file), and Ctrl-^
    comes straight back.""",
    examples=[("gf", "open the file under the cursor"), ("Ctrl-^", "straight back"),
              ("Ctrl-o", "back through the jump list"), ("Ctrl-w f", "open it in a split")],
    level="complex",
)
gf.add(
    title="Follow an include", par=6,
    task="The cursor is on the name of the included header. In config.h, the retry limit should be 5, not 3.",
    files={
        "main.c": (text('''
            #include <stdio.h>
            #include "config.h"

            int main(void)
            {
                for (int i = 0; i < MAX_RETRIES; i++)
                    puts("retrying");
                return 0;
            }
        '''),) * 2,
        "config.h": (text('''
            #ifndef CONFIG_H
            #define CONFIG_H

            #define MAX_RETRIES 3
            #define TIMEOUT_MS 2500

            #endif
        '''), text('''
            #ifndef CONFIG_H
            #define CONFIG_H

            #define MAX_RETRIES 5
            #define TIMEOUT_MS 2500

            #endif
        ''')),
    },
    open="main.c", cursor=(2, 11),
    hint="gf opens config.h. The MAX_RETRIES line is three lines down, and 2 Ctrl-a adds 2 to its number.",
    uses=["count", "increment"],
)
gf.add(
    title="Move a constant to its module", par=8,
    task="TAX_RATE is defined in app.py but belongs in shop/cart.py, which uses it. Move the line to shop/cart.py, "
         "below the import there, and leave app.py's import line alone. Your cursor starts on the import of "
         "shop.cart.",
    files={
        "app.py": (text('''
            from shop.cart import total
            TAX_RATE = 0.08

            print(total([450, 1200]))
        '''), text('''
            from shop.cart import total

            print(total([450, 1200]))
        ''')),
        "shop/cart.py": (text('''
            import math


            def total(prices):
                return math.ceil(sum(prices) * (1 + TAX_RATE))
        '''), text('''
            import math
            TAX_RATE = 0.08


            def total(prices):
                return math.ceil(sum(prices) * (1 + TAX_RATE))
        ''')),
    },
    open="app.py", cursor=(1, 1),
    hint="Cut the TAX_RATE line first. Then go back up to the import, put the cursor on shop.cart, and gf opens "
         "shop/cart.py: the Python plugin turns the dot into a slash and adds .py.",
    uses=["dd", "word", "p"],
)
gf.add(
    title="Follow a path in a config", par=15,
    task="In nginx.conf, the cursor is on an include line. In the included file, conf.d/gzip.conf, turn gzip on "
         "(off becomes on). Then, back in nginx.conf, change worker_connections from 512 to 1024.",
    files={
        "nginx.conf": (text('''
            worker_processes auto;

            events {
                worker_connections 512;
            }

            http {
                include conf.d/gzip.conf;
                server {
                    listen 80;
                }
            }
        '''), text('''
            worker_processes auto;

            events {
                worker_connections 1024;
            }

            http {
                include conf.d/gzip.conf;
                server {
                    listen 80;
                }
            }
        ''')),
        "conf.d/gzip.conf": (text('''
            gzip off;
            gzip_types text/css application/json;
        '''), text('''
            gzip on;
            gzip_types text/css application/json;
        ''')),
    },
    open="nginx.conf", cursor=(8, 13),
    hint="gf follows the path under the cursor. In gzip.conf, cw changes off. Ctrl-^ (or Ctrl-o) takes you back "
         "to the include line, and 512 is four lines up, where 512 Ctrl-a doubles it.",
    uses=["word", "c", "edit", "count", "increment"],
)
gf.add(
    title="Follow the stylesheet", par=19,
    task="Links should be underlined: in the stylesheet index.html links to, text-decoration: none becomes "
         "underline. The cursor starts on the link line.",
    files={
        "index.html": (text('''
            <!doctype html>
            <html>
            <head>
                <link rel="stylesheet" href="css/site.css">
            </head>
            <body>
                <a href="/docs">Docs</a>
            </body>
            </html>
        '''),) * 2,
        "css/site.css": (text('''
            body { font-family: sans-serif; }
            a { text-decoration: none; }
        '''), text('''
            body { font-family: sans-serif; }
            a { text-decoration: underline; }
        ''')),
    },
    open="index.html", cursor=(4, 1),
    hint="gf needs the cursor on the path itself: on the line, the first c is the c of css. In the stylesheet, a "
         "search for no finds none.",
    uses=["f", "search", "c"],
)
gf.add(
    title="A link in the README", par=16,
    task="The minimum is now Python 3.10: change 3.8 to 3.10 in README.md (you're here) and in the setup guide it "
         "links to, docs/setup.md.",
    files={
        "README.md": (text('''
            # acme

            Needs Python 3.8 or newer. See the [setup guide](docs/setup.md).
        '''), text('''
            # acme

            Needs Python 3.10 or newer. See the [setup guide](docs/setup.md).
        ''')),
        "docs/setup.md": (text('''
            # Setup

            Install Python 3.8 or newer, then run pip install acme.
        '''), text('''
            # Setup

            Install Python 3.10 or newer, then run pip install acme.
        ''')),
    },
    open="README.md",
    hint="2 Ctrl-a turns the 8 into 10. A Markdown link's path works with gf once the cursor is on it, and in the "
         "new file . repeats the 2 Ctrl-a.",
    uses=["count", "f", "increment", "dot"],
)
gf.add(
    title="From the source list", par=20,
    task="In the files the Makefile lists: src/net.c should listen on port 8443 instead of 8080, and src/log.c "
         "should log at LOG_INFO instead of LOG_DEBUG. You start at the top of the Makefile.",
    files={
        "Makefile": (text('''
            SRC = src/main.c src/net.c src/log.c

            app: $(SRC)
            \t$(CC) -o app $(SRC)
        '''),) * 2,
        "src/main.c": ("int main(void) { return serve(); }",) * 2,
        "src/net.c": ("static int port = 8080;", "static int port = 8443;"),
        "src/log.c": ("static int level = LOG_DEBUG;", "static int level = LOG_INFO;"),
    },
    open="Makefile",
    hint="W moves from path to path on the SRC line, and gf opens the one under the cursor. Ctrl-^ comes straight "
         "back to the Makefile, still on that path. 8443 is 363 more than 8080.",
    uses=["bigword", "count", "increment", "edit", "f", "c"],
)

# ---------- :args :argdo ----------

argdo = drills.command(
    "argdo", ":args  :argdo", "run a command on a list of files",
    """The argument list is a list of files you pick by name: the ones you started Neovim with, until you set it.
    :args {files} replaces it and opens the first one; globs work, and ** matches any folders, so :args **/*.h
    picks every header. :argdo {cmd} then runs an Ex command in each file in the list, for example
    :argdo %s/old/new/ge or :argdo norm Gdd. Like the other do commands it takes the rest of the line, | included,
    and leaves the changed files open but unsaved: :wa saves them all. :args alone shows the list, and ]a and [a
    step through it.""",
    examples=[(":args *.py", "the Python files here"), (":args **/*.h", "every header, in any folder"),
              (":argdo %s/a/b/ge", "substitute in each file"), (":argdo norm Gdd", "Normal keys in each file"),
              (":args", "show the list")],
    level="complex",
)
argdo.add(
    title="Every file in the list", par=10,
    task="The argument list holds three modules: app.py (you're here), db.py and jobs.py. Each ends with a "
         "leftover debug print: delete that last line in all three. README.md is open too, and must not change.",
    files={
        "app.py": (text('''
            from db import connect

            conn = connect()
            print("DEBUG app loaded")
        '''), text('''
            from db import connect

            conn = connect()
        ''')),
        "db.py": (text('''
            import sqlite3


            def connect():
                return sqlite3.connect("shop.db")
            print("DEBUG db loaded")
        '''), text('''
            import sqlite3


            def connect():
                return sqlite3.connect("shop.db")
        ''')),
        "jobs.py": (text('''
            from db import connect


            def nightly():
                connect().execute("VACUUM")
            print("DEBUG jobs loaded")
        '''), text('''
            from db import connect


            def nightly():
                connect().execute("VACUUM")
        ''')),
        "README.md": (text('''
            # shop

            Run python app.py to start.
        '''),) * 2,
    },
    open="app.py", setup=["args app.py db.py jobs.py", "badd README.md"],
    hint=":argdo runs an Ex command in every file in the argument list. $ is the last line as a range, and d "
         "deletes it. (:bufdo would also reach README.md.)",
    uses=["range"],
)
argdo.add(
    title="Pick files with a glob", par=40,
    task="Every script in scripts/ should stop at the first error: add the line set -euo pipefail right below the "
         "#! line of each one. install.sh, in the top folder, is for users' machines: leave it alone.",
    files={
        "install.sh": (text('''
            #!/bin/sh
            curl -fsSL https://example.com/acme.tar.gz | tar -xz -C /usr/local
        '''),) * 2,
        "scripts/build.sh": (text('''
            #!/bin/bash
            npm ci
            npm run build
        '''), text('''
            #!/bin/bash
            set -euo pipefail
            npm ci
            npm run build
        ''')),
        "scripts/deploy.sh": (text('''
            #!/bin/bash
            rsync -az dist/ deploy@web1:/srv/app/
        '''), text('''
            #!/bin/bash
            set -euo pipefail
            rsync -az dist/ deploy@web1:/srv/app/
        ''')),
        "scripts/test.sh": (text('''
            #!/bin/bash
            npm test -- --coverage
        '''), text('''
            #!/bin/bash
            set -euo pipefail
            npm test -- --coverage
        ''')),
    },
    open="install.sh",
    hint=":args scripts/* puts just those files in the list (Tab completes scripts/ after the s), and | runs "
         ":argdo after it on the same line. :normal o opens a line below line 1, where the cursor starts in each "
         "file.",
    uses=["normal", "o"],
)
argdo.add(
    title="A package moves", par=32,
    task="Order.java and Product.java were moved from src/shop/ into src/shop/model/. Change their package line "
         "from package shop; to package shop.model;. App.java and Cart.java stay in package shop.",
    files={
        "src/shop/App.java": (text('''
            package shop;

            public class App {
                public static void main(String[] args) {
                    System.out.println(new Cart());
                }
            }
        '''),) * 2,
        "src/shop/Cart.java": (text('''
            package shop;

            public class Cart {
            }
        '''),) * 2,
        "src/shop/model/Order.java": (text('''
            package shop;

            public record Order(String id, long cents) {
            }
        '''), text('''
            package shop.model;

            public record Order(String id, long cents) {
            }
        ''')),
        "src/shop/model/Product.java": (text('''
            package shop;

            public record Product(String name, long cents) {
            }
        '''), text('''
            package shop.model;

            public record Product(String name, long cents) {
            }
        ''')),
    },
    open="src/shop/App.java",
    hint=":args src/shop/model/* picks the two files, and Tab completes each folder name: s<Tab><Tab>m<Tab>. "
         "The package line is line 1, where the cursor starts in each file, so :argdo s/;/.model;/ needs no "
         "range.",
    uses=["subst"],
)
argdo.add(
    title="Only the Markdown files", par=37,
    task="The site moved to HTTPS: in every Markdown file, here and in docs/, http: becomes https:. build.cmd and "
         "src/server.py keep their http: URLs, and the ftp:// mirror stays as it is.",
    files={
        "README.md": (text('''
            # acme

            Docs: http://acme.dev/docs
            Blog: http://acme.dev/blog
            Code: https://github.com/acme/acme
            Mirror: ftp://mirror.acme.dev/acme
        '''), text('''
            # acme

            Docs: https://acme.dev/docs
            Blog: https://acme.dev/blog
            Code: https://github.com/acme/acme
            Mirror: ftp://mirror.acme.dev/acme
        ''')),
        "docs/install.md": (text('''
            # Install

            Download it from http://acme.dev/download.
        '''), text('''
            # Install

            Download it from https://acme.dev/download.
        ''')),
        "docs/faq.md": (text('''
            # FAQ

            Ask in the forum.
        '''),) * 2,
        "src/server.py": ('print("serving on http://localhost:8000")',) * 2,
        "build.cmd": ("curl -L -o deps.zip http://mirror.internal/deps.zip",) * 2,
    },
    open="README.md",
    hint=":args **/*.md picks the Markdown files in every folder, the top one included. faq.md has no link, and "
         "a :s that finds nothing is an error, so give it the e flag.",
    uses=["subst", "range"],
)
argdo.add(
    title="A :g in every file", par=34,
    task="Mark the star imports for the linter: the argument list holds the three Python files, and in each, every "
         "line with import * gets   # noqa: F403 at its end. notes.txt is open too, and stays as it is.",
    files={
        "app.py": (text('''
            from os.path import *
            import sys

            print(join(sys.argv[1], "out"))
        '''), text('''
            from os.path import *  # noqa: F403
            import sys

            print(join(sys.argv[1], "out"))
        ''')),
        "shapes.py": (text('''
            from math import *
            from fractions import *

            area = pi * Fraction(3, 2) ** 2
        '''), text('''
            from math import *  # noqa: F403
            from fractions import *  # noqa: F403

            area = pi * Fraction(3, 2) ** 2
        ''')),
        "clean.py": (text('''
            import os

            os.remove("out.txt")
        '''),) * 2,
        "notes.txt": ("Avoid import * in new code.",) * 2,
    },
    open="app.py", setup=["args app.py shapes.py clean.py", "badd notes.txt"],
    hint=":argdo can run any Ex command in each file, :g included: :g/pattern/norm A... appends to every matching "
         "line. Only the star imports end in a *, and in a pattern a star needs a backslash.",
    uses=["global", "normal"],
)
argdo.add(
    title="Re-indent them all", par=26,
    task="The C files in src/ were written with 2-space indents. Re-indent all of each with = so they use 4. "
         "include/acme.h is fine as it is.",
    files={
        "src/main.c": (text('''
            int main(void)
            {
              if (init() != 0)
                return 1;
              return run();
            }
        '''), text('''
            int main(void)
            {
                if (init() != 0)
                    return 1;
                return run();
            }
        ''')),
        "src/util.c": (text('''
            int clamp(int x, int lo, int hi)
            {
              if (x < lo)
                return lo;
              return x > hi ? hi : x;
            }
        '''), text('''
            int clamp(int x, int lo, int hi)
            {
                if (x < lo)
                    return lo;
                return x > hi ? hi : x;
            }
        ''')),
        "include/acme.h": (text('''
            #ifndef ACME_H
            #define ACME_H
            int run(void);
            #endif
        '''),) * 2,
    },
    open="include/acme.h",
    hint=":args with a glob picks the files. gg=G re-indents a whole file, and :argdo norm runs those keys in each.",
    uses=["normal", "equal", "gg"],
)

# ---------- :bufdo :windo ----------

bufdo = drills.command(
    "bufdo", ":bufdo  :windo", "run a command in every buffer or window",
    """:bufdo {cmd} runs an Ex command in every buffer in the buffer list (the files :ls shows), and :windo {cmd}
    in every window on the screen. Like the other do commands they take the rest of the line, | included, so
    :bufdo %s/a/b/ge | %s/c/d/ge runs both substitutions everywhere. A :s that finds nothing is an error, which
    skips the rest of that line in that buffer, so give each :s the e flag. Changed buffers stay open and
    unsaved: :wa saves them all. In these exercises :windo also visits the task window, which can't be changed,
    and reports an error there.""",
    examples=[(":bufdo %s/a/b/ge", "substitute in every buffer"), (":windo %s/a/b/ge", "in every window"),
              (":bufdo norm A;", "Normal keys in every buffer"), (":wa", "save every changed buffer")],
    level="complex",
)
bufdo.add(
    title="Every open buffer", par=25,
    task="The Redis setting was renamed: in the three open buffers (worker.py, cache.py and settings.py), change "
         "REDIS_HOST to REDIS_URL. DB_HOST keeps its name, and legacy/old_worker.py isn't open and must keep its "
         "REDIS_HOST.",
    files={
        "worker.py": (text('''
            from settings import REDIS_HOST

            queue = Queue(REDIS_HOST)
        '''), text('''
            from settings import REDIS_URL

            queue = Queue(REDIS_URL)
        ''')),
        "cache.py": (text('''
            import redis

            from settings import REDIS_HOST

            client = redis.from_url(REDIS_HOST)
        '''), text('''
            import redis

            from settings import REDIS_URL

            client = redis.from_url(REDIS_URL)
        ''')),
        "settings.py": (text('''
            import os

            DB_HOST = os.environ.get("DB_HOST", "localhost")
            REDIS_HOST = os.environ.get("REDIS_HOST", "redis://localhost:6379/0")
        '''), text('''
            import os

            DB_HOST = os.environ.get("DB_HOST", "localhost")
            REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
        ''')),
        "legacy/old_worker.py": (text('''
            REDIS_HOST = "localhost"
        '''),) * 2,
    },
    open="worker.py", setup=badd("cache.py", "settings.py"),
    hint="Put the cursor on REDIS_HOST and press *: then :bufdo %s//REDIS_URL/g reuses that whole-word search in "
         "each listed buffer, and DB_HOST doesn't match. The g flag changes both names on settings.py's line.",
    uses=["star", "line", "subst", "range"],
)
bufdo.add(
    title="Only what's on screen", par=25,
    task="en.json and de.json are side by side, and fr.json is open but hidden (another team translates it). In the "
         "two visible files only, rename the key \"btn_ok\" to \"button_ok\".",
    files={
        "en.json": (text('''
            {
              "btn_ok": "OK",
              "btn_cancel": "Cancel"
            }
        '''), text('''
            {
              "button_ok": "OK",
              "btn_cancel": "Cancel"
            }
        ''')),
        "de.json": (text('''
            {
              "btn_ok": "OK",
              "btn_cancel": "Abbrechen"
            }
        '''), text('''
            {
              "button_ok": "OK",
              "btn_cancel": "Abbrechen"
            }
        ''')),
        "fr.json": (text('''
            {
              "btn_ok": "OK",
              "btn_cancel": "Annuler"
            }
        '''),) * 2,
    },
    open="en.json", setup=badd("fr.json") + vsplit("de.json"),
    hint="* on btn_ok, then :windo %s//button_ok/ runs the substitution in each window, so the hidden fr.json is "
         "safe (:bufdo would change it). :windo also visits the task window and complains there: that's fine.",
    uses=["star", "word", "subst", "range"],
)
bufdo.add(
    title="Two renames in every buffer", par=53,
    task="In the three open buffers (main.c, list.c and list.h), rename list_add to list_push and list_del to "
         "list_pop. map_add keeps its name, and vendor/list_compat.c isn't open and must not change.",
    files={
        "main.c": (text('''
            #include "list.h"

            int main(void)
            {
                struct list *l = list_new();
                map_add(env, "list", l);
                return list_del(l) == 0 ? 0 : 1;
            }
        '''), text('''
            #include "list.h"

            int main(void)
            {
                struct list *l = list_new();
                map_add(env, "list", l);
                return list_pop(l) == 0 ? 0 : 1;
            }
        ''')),
        "list.c": (text('''
            #include "list.h"

            void list_add(struct list *l, int x) { l->items[l->len++] = x; }
            int list_del(struct list *l) { return l->items[--l->len]; }
        '''), text('''
            #include "list.h"

            void list_push(struct list *l, int x) { l->items[l->len++] = x; }
            int list_pop(struct list *l) { return l->items[--l->len]; }
        ''')),
        "list.h": (text('''
            struct list *list_new(void);
            void list_add(struct list *l, int x);
            int list_del(struct list *l);
            int list_len(const struct list *l);
        '''), text('''
            struct list *list_new(void);
            void list_push(struct list *l, int x);
            int list_pop(struct list *l);
            int list_len(const struct list *l);
        ''')),
        "vendor/list_compat.c": (text('''
            #define list_add(l, x) list_append(l, x)
            #define list_del(l) list_remove_last(l)
        '''),) * 2,
    },
    open="main.c", setup=badd("list.c", "list.h"),
    hint="Join two substitutions with |. main.c has no list_add, so the first :s fails there, and that error "
         "skips the rest of the line. The e flag on the first :s turns the error off.",
    uses=["subst", "range"],
)
bufdo.add(
    title="Six scripts at once", par=31,
    task="Six scripts are open as buffers, build.sh (you're here) and five more. Each needs the line "
         "set -euo pipefail right below its #! line.",
    files={name: (f"#!/bin/bash\n{body}", f"#!/bin/bash\nset -euo pipefail\n{body}") for name, body in [
        ("build.sh", "npm ci\nnpm run build"),
        ("clean.sh", "rm -rf dist node_modules"),
        ("deploy.sh", "rsync -az dist/ deploy@web1:/srv/app/"),
        ("lint.sh", "npx eslint src"),
        ("release.sh", "git tag \"v$1\" && git push --tags"),
        ("test.sh", "npm test -- --coverage"),
    ]},
    open="build.sh", setup=badd("deploy.sh", "test.sh", "clean.sh", "release.sh", "lint.sh"),
    hint=":bufdo norm runs Normal keys in each buffer, where the cursor is still on line 1. With six files, that's "
         "shorter than ]b and . for each one.",
    uses=["normal", "o"],
)
bufdo.add(
    title="Debug lines out", par=17,
    task="Delete the console.log lines from the three open buffers (app.js, api.js and ui.js). Keep console.error, "
         "and scripts/debug.js isn't open: its logs stay.",
    files={
        "app.js": (text('''
            import { store } from "./store.js";

            console.log("booting");
            store.load();
            dialog("Welcome!");
        '''), text('''
            import { store } from "./store.js";

            store.load();
            dialog("Welcome!");
        ''')),
        "api.js": (text('''
            export async function getJSON(url) {
                const resp = await fetch(url);
                console.log("GET", url, resp.status);
                if (!resp.ok) console.error("failed:", url);
                return resp.json();
            }
        '''), text('''
            export async function getJSON(url) {
                const resp = await fetch(url);
                if (!resp.ok) console.error("failed:", url);
                return resp.json();
            }
        ''')),
        "ui.js": (text('''
            export function render(items) {
                console.log("render", items.length);
                return items.map((i) => `<li>${i}</li>`).join("");
            }
        '''), text('''
            export function render(items) {
                return items.map((i) => `<li>${i}</li>`).join("");
            }
        ''')),
        "scripts/debug.js": ('console.log(process.versions);',) * 2,
    },
    open="app.js", setup=badd("ui.js", "api.js"),
    hint=":bufdo runs any Ex command in each buffer, so :g/pattern/d deletes every matching line in all of them. "
         "The pattern only has to tell console.log from console.error, store.load and dialog.",
    uses=["global"],
)
bufdo.add(
    title="Invisible spaces", par=15, exact=True,
    task="Strip the trailing whitespace (spaces, and one tab) from the ends of the lines in all three open buffers: "
         "server.py, routes.py and README.md. You can't see it, but it's there.",
    files={
        "server.py": ("from routes import app  \n\napp.run(port=8000)   ",
                      "from routes import app\n\napp.run(port=8000)"),
        "routes.py": ("from flask import Flask\t\n\napp = Flask(__name__) ",
                      "from flask import Flask\n\napp = Flask(__name__)"),
        "README.md": ("# Server\n\nRun python server.py.",) * 2,
    },
    open="server.py", setup=badd("routes.py", "README.md"),
    hint="\\s matches a space or a tab. Every line ends somewhere, so a pattern that can also match nothing at "
         "the end never fails, even in README.md, which has no trailing whitespace.",
    uses=["subst", "range"],
)

# ---------- :vimgrep :cnext ----------

vimgrep = drills.command(
    "vimgrep", ":vimgrep  :cnext  ]q", "search many files, step through matches",
    """:vimgrep /pattern/ {files} (:vim for short) searches the files and puts every matching line in the
    quickfix list, then jumps to the first match with the cursor on it. :cnext (]q) goes to the next match and
    :cprev ([q) to the previous one, opening each file as needed; with a count, 2]q goes two matches on. :vim //
    {files} reuses your last search pattern, from / or *, but :vimgrep doesn't set the search pattern itself. Add
    g after the pattern (/pat/g) for one entry per match instead of per line, and :copen shows the whole list.""",
    examples=[(":vim /TODO/ **/*.py", "every TODO in the Python files"), ("]q  [q", "next / previous match"),
              ("2]q", "two matches on"), (":vim // **/*.c", "reuse the last search"), (":copen", "show the list")],
    level="complex",
)
vimgrep.add(
    title="Visit each match", par=31,
    task="Every place that sets retries= should allow one more retry than it does now. They're in Python files "
         "in this folder and below.",
    files={
        "client.py": (text('''
            import requests


            def get(url):
                return http_get(url, retries=3)
        '''), text('''
            import requests


            def get(url):
                return http_get(url, retries=4)
        ''')),
        "jobs/sync.py": (text('''
            from client import get

            SYNC = dict(url="https://api.example.com/sync", retries=5)
        '''), text('''
            from client import get

            SYNC = dict(url="https://api.example.com/sync", retries=6)
        ''')),
        "jobs/mail.py": (text('''
            def send(msg, retries=1):
                return smtp_send(msg, attempts=retries)
        '''), text('''
            def send(msg, retries=2):
                return smtp_send(msg, attempts=retries)
        ''')),
    },
    open="client.py",
    hint=":vimgrep jumps to the first match with the cursor on it, and Ctrl-a adds 1 to the next number on the "
         "line. ]q goes to the next match and . repeats the Ctrl-a.",
    uses=["increment", "dot"],
)
vimgrep.add(
    title="Skip the one that's fine", par=39,
    task="Replace the debug print( calls with log.debug( in every Python file, except the one in cli.py that "
         "tells the user their order number: that one stays a print.",
    files={
        "cli.py": (text('''
            import logging

            from orders import place

            log = logging.getLogger(__name__)


            def main(argv):
                print("args:", argv)
                order = place(argv[1], int(argv[2]))
                print("Placed order", order.id)
        '''), text('''
            import logging

            from orders import place

            log = logging.getLogger(__name__)


            def main(argv):
                log.debug("args:", argv)
                order = place(argv[1], int(argv[2]))
                print("Placed order", order.id)
        ''')),
        "orders.py": (text('''
            import logging

            log = logging.getLogger(__name__)


            def place(item, qty):
                print("placing", item, qty)
                return Order(item, qty)
        '''), text('''
            import logging

            log = logging.getLogger(__name__)


            def place(item, qty):
                log.debug("placing", item, qty)
                return Order(item, qty)
        ''')),
        "payments.py": (text('''
            import logging

            log = logging.getLogger(__name__)


            def charge(order):
                print("charging", order.id)
        '''), text('''
            import logging

            log = logging.getLogger(__name__)


            def charge(order):
                log.debug("charging", order.id)
        ''')),
    },
    open="orders.py",
    hint=":vim /print(/ *.py puts the cursor on the first match, in cli.py. Change it with cw, then ]q goes to "
         "the next match: skip the order-number one with another ]q, and . repeats the change at the others.",
    uses=["c", "word", "dot"],
)
vimgrep.add(
    title="Reuse the search", par=36,
    task="Rename the variable buf to rx_buf in http.c and net.c. The log message in http.c says \"no buf\": that "
         "text stays as it is. Your cursor starts on a buf in net.c.",
    files={
        "http.c": (text('''
            int http_status(const char *buf)
            {
                if (!buf)
                    log_msg("http: no buf");
                return atoi(buf + 9);
            }
        '''), text('''
            int http_status(const char *rx_buf)
            {
                if (!rx_buf)
                    log_msg("http: no buf");
                return atoi(rx_buf + 9);
            }
        ''')),
        "net.c": (text('''
            #include "net.h"

            int net_read(int fd)
            {
                char buf[512];
                return recv(fd, buf, 512, 0);
            }
        '''), text('''
            #include "net.h"

            int net_read(int fd)
            {
                char rx_buf[512];
                return recv(fd, rx_buf, 512, 0);
            }
        ''')),
    },
    open="net.c", cursor=(5, 10),
    hint="* searches for the whole word buf, and :vim // reuses that search. Change the first match with cw, then "
         "]q and . at each of the others, except the one in the log message, which you skip with ]q.",
    uses=["star", "c", "word", "dot"],
)
vimgrep.add(
    title="Two on one line", par=21,
    task="Give every timeout five more seconds: timeout=5 becomes timeout=10, and so on. There are three, in "
         "the files in this folder, two of them on the same line.",
    files={
        "config.py": (text('''
            CONNECT = dict(timeout=5, read_timeout=30)
            RETRIES = 3
        '''), text('''
            CONNECT = dict(timeout=10, read_timeout=35)
            RETRIES = 3
        ''')),
        "worker.py": (text('''
            from config import CONNECT


            def poll(url):
                return get(url, timeout=12, **CONNECT)
        '''), text('''
            from config import CONNECT


            def poll(url):
                return get(url, timeout=17, **CONNECT)
        ''')),
    },
    open="worker.py",
    hint="Add g after the pattern for one quickfix entry per match instead of one per line. Each entry puts the "
         "cursor on its match, where 5 Ctrl-a adds 5 to the number after it.",
    uses=["count", "increment", "dot"],
)
vimgrep.add(
    title="Jump over two", par=27,
    task="Replace old_api( with new_api( everywhere, except in compat/legacy.py, which has to keep calling the "
         "old one.",
    files={
        "app.py": ("from api import old_api, new_api\n\nprint(old_api(1))",
                   "from api import old_api, new_api\n\nprint(new_api(1))"),
        "compat/legacy.py": ("def fetch(i):\n    return old_api(i)\n\n\ndef fetch_all():\n    return [old_api(i) for i in range(3)]",) * 2,
        "worker.py": ("def run():\n    old_api(42)", "def run():\n    new_api(42)"),
    },
    open="app.py",
    hint="A count works on ]q too: 3]q goes three matches on, over both of legacy.py's. 3s replaces just the "
         "three letters of old, and . repeats it.",
    uses=["c", "count", "dot"],
)
vimgrep.add(
    title="A different word each time", par=49,
    task="Each locale file has a TODO where the Save label goes: Speichern in de.yml, Guardar in es.yml and "
         "Enregistrer in fr.yml.",
    files={
        "app.yml": ("name: acme\nlocales: [de, es, fr]",) * 2,
        "locales/de.yml": ("de:\n  title: Titel\n  save: TODO", "de:\n  title: Titel\n  save: Speichern"),
        "locales/es.yml": ("es:\n  title: Título\n  save: TODO", "es:\n  title: Título\n  save: Guardar"),
        "locales/fr.yml": ("fr:\n  title: Titre\n  save: TODO", "fr:\n  title: Titre\n  save: Enregistrer"),
    },
    open="app.yml",
    hint=":vimgrep finds the three TODOs, in the order of the file names. Each needs its own word, so there's no . "
         "to repeat: ]q takes you to the next one, and C replaces the TODO at the end of the line.",
    uses=["c"],
)

# ---------- :cdo :cfdo ----------

cdo = drills.command(
    "cdo", ":cdo  :cfdo", "run a command on every match",
    """:cdo {cmd} runs an Ex command at every entry in the quickfix list, with the cursor on that line, and :cfdo
    {cmd} runs it once in each file in the list. After * and :vim // **/*.c, :cdo s//new/g renames at every
    match, because the empty pattern reuses the search. Use :cfdo for things that should happen once per file,
    like adding an import or a %s over the whole file. Both take the rest of the line, | included, and leave the
    changed files unsaved; they often end at a Press ENTER prompt.""",
    examples=[(":cdo s//new/g", "substitute at every match"), (":cdo norm A;", "Normal keys at every match"),
              (":cfdo %s/a/b/ge", "once in each file"), (":cfdo norm ggOimport os", "add a line to each file")],
    level="complex",
)
cdo.add(
    title="Rename everywhere", par=35,
    task="Rename the function fetch_user to get_user everywhere it appears, in all the Python files. "
         "fetch_users (with an s) keeps its name. Your cursor starts on a fetch_user call.",
    files={
        "app.py": (text('''
            from users import fetch_user, fetch_users

            print(fetch_user(1), len(fetch_users()))
        '''), text('''
            from users import get_user, fetch_users

            print(get_user(1), len(fetch_users()))
        ''')),
        "users.py": (text('''
            def fetch_users():
                return [fetch_user(i) for i in range(3)]


            def fetch_user(user_id):
                return {"id": user_id}
        '''), text('''
            def fetch_users():
                return [get_user(i) for i in range(3)]


            def get_user(user_id):
                return {"id": user_id}
        ''')),
        "tests/test_users.py": (text('''
            from users import fetch_user


            def test_fetch_user():
                assert fetch_user(7)["id"] == 7
        '''), text('''
            from users import get_user


            def test_fetch_user():
                assert get_user(7)["id"] == 7
        ''')),
    },
    open="app.py", cursor=(3, 7),
    hint="* searches for the whole word, so fetch_users doesn't match. :vim // reuses it in every .py file, and "
         ":cdo s//get_user/ reuses it once more on each matching line. The test's name test_fetch_user isn't the "
         "whole word fetch_user, so it stays.",
    uses=["star", "subst"],
)
cdo.add(
    title="Once per file", par=45,
    task="Every module that calls time.sleep needs import time as its first line, once per file. They're the "
         "Python files in this folder; config.py only mentions sleep in a comment and stays as it is.",
    files={
        "poller.py": (text('''
            def poll(check):
                while not check():
                    time.sleep(1)
                time.sleep(0.5)
        '''), text('''
            import time
            def poll(check):
                while not check():
                    time.sleep(1)
                time.sleep(0.5)
        ''')),
        "retry.py": (text('''
            def retry(fn, tries=3):
                for i in range(tries):
                    try:
                        return fn()
                    except OSError:
                        time.sleep(2 ** i)
        '''), text('''
            import time
            def retry(fn, tries=3):
                for i in range(tries):
                    try:
                        return fn()
                    except OSError:
                        time.sleep(2 ** i)
        ''')),
        "config.py": (text('''
            # How long the poller sleeps between checks, in seconds.
            POLL_INTERVAL = 1
        '''),) * 2,
    },
    open="poller.py",
    hint="Search for sleep( rather than sleep, so the word sleeps in config.py's comment doesn't match. Then :cfdo "
         "runs once per file: :cdo would add two imports to poller.py. :cfdo leaves the cursor on the file's first "
         "match, so go to the top before O.",
    uses=["normal", "gg", "o"],
)
cdo.add(
    title="Python 2 prints", par=36,
    task="Turn every Python 2 print statement into a Python 3 call, in all the .py files here: print \"x\" becomes "
         "print(\"x\"). Each one is a whole line on its own.",
    files={
        "hello.py": (text('''
            name = "world"
            print "hello", name
        '''), text('''
            name = "world"
            print("hello", name)
        ''')),
        "report.py": (text('''
            def report(rows):
                print "rows:", len(rows)
                for r in rows:
                    print r
        '''), text('''
            def report(rows):
                print("rows:", len(rows))
                for r in rows:
                    print(r)
        ''')),
    },
    open="hello.py",
    hint=":vim /print / finds each statement. At every match, :cdo norm can make the edit with Normal keys: f "
         "and a space find the space after print, r( replaces it, and A) adds the closing parenthesis.",
    uses=["normal", "f", "r", "insert"],
)
cdo.add(
    title="One more argument", par=38,
    task="Log the tracebacks too: every log.error( call in the Python files gets , exc_info=True as its last "
         "argument. log.warning stays as it is.",
    files={
        "app.py": (text('''
            def handle(req):
                try:
                    return route(req)
                except KeyError:
                    log.warning("no route for %s", req.path)
                except Exception as e:
                    log.error("handler failed: %s", e)
        '''), text('''
            def handle(req):
                try:
                    return route(req)
                except KeyError:
                    log.warning("no route for %s", req.path)
                except Exception as e:
                    log.error("handler failed: %s", e, exc_info=True)
        ''')),
        "db.py": (text('''
            def connect(url):
                try:
                    return engine.connect(url)
                except OSError:
                    log.error("cannot reach %s", url)
                    raise
        '''), text('''
            def connect(url):
                try:
                    return engine.connect(url)
                except OSError:
                    log.error("cannot reach %s", url, exc_info=True)
                    raise
        ''')),
    },
    open="app.py",
    hint=":cdo runs a command on each line in the quickfix list. Each of these lines has one ), and a :s that puts "
         "the new argument in front of it does the job.",
    uses=["subst"],
)
cdo.add(
    title="Whole files that match", par=36,
    task="Switch from requests to httpx in the modules that import requests: there, every requests becomes httpx. "
         "README.md and notes.py only mention requests, and stay as they are.",
    files={
        "client.py": (text('''
            import requests

            def get_user(uid):
                return requests.get(f"/users/{uid}").json()

            def ping():
                return requests.head("/health").ok
        '''), text('''
            import httpx

            def get_user(uid):
                return httpx.get(f"/users/{uid}").json()

            def ping():
                return httpx.head("/health").ok
        ''')),
        "sync.py": (text('''
            import requests

            def push(batch):
                requests.post("/sync", json=batch)
        '''), text('''
            import httpx

            def push(batch):
                httpx.post("/sync", json=batch)
        ''')),
        "notes.py": ("# TODO: count the requests per minute\nLIMIT = 600",) * 2,
        "README.md": ("Uses requests for HTTP.",) * 2,
    },
    open="README.md",
    hint="Search for the import line, so only the files that import requests are in the list. :cfdo then runs "
         "once in each of them, and a %s there changes every line of the file, not just the matching one.",
    uses=["subst", "range"],
)
cdo.add(
    title="Comment them out", par=27,
    task="Comment out every breakpoint() call in the Python files, wherever it is. The docs only talk about "
         "breakpoints and stay as they are.",
    files={
        "app.py": ("def main():\n    breakpoint()\n    serve()", "def main():\n    # breakpoint()\n    serve()"),
        "models/user.py": ("class User:\n    def save(self):\n        breakpoint()\n        db.save(self)",
                           "class User:\n    def save(self):\n        # breakpoint()\n        db.save(self)"),
        "tests/test_user.py": ("def test_save():\n    breakpoint()\n    User().save()",
                               "def test_save():\n    # breakpoint()\n    User().save()"),
        "docs.md": ("Remove your breakpoints before you push.",) * 2,
    },
    open="app.py",
    hint="gcc comments out a line with the file type's comment leader, and :cdo norm gcc does it at every match, "
         "keeping each line's indent.",
    uses=["normal", "comment"],
)
