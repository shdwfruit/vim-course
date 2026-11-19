"""Exercises for Project 09. Run:  python3 check.py   (python3 check.py 3 plays exercise 3)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "common"))
from trainer import Course, text  # noqa: E402

course = Course("Project 09 · Many files: buffers, windows, and project-wide changes", __file__,
                done_message="On to 10_advanced, where every exercise is a real file with 10 to 14 edits to plan.")


def setup(*commands):
    """Extra Ex commands to run before the exercise starts (open more buffers, split windows, ...)."""
    return list(commands)


course.add(
    name="move-a-method", title="Move a method to another file", par=13,
    task="Someone put the start method in Config.java. Move it into Main.java, below main, with one blank line "
         "between the two methods. Afterwards Config.java holds just its two constants.",
    files={
        "Main.java": (text('''
            public class Main {
                public static void main(String[] args) {
                    start(Config.HOST, Config.PORT);
                }
            }
        '''), text('''
            public class Main {
                public static void main(String[] args) {
                    start(Config.HOST, Config.PORT);
                }

                static void start(String host, int port) {
                    System.out.println("Serving on " + host + ":" + port);
                }
            }
        ''')),
        "Config.java": (text('''
            public class Config {
                static final String HOST = "127.0.0.1";
                static final int PORT = 8000;

                static void start(String host, int port) {
                    System.out.println("Serving on " + host + ":" + port);
                }
            }
        '''), text('''
            public class Config {
                static final String HOST = "127.0.0.1";
                static final int PORT = 8000;
            }
        ''')),
    },
    open="Main.java", setup=setup(),
    hint="Open Config.java with :e (Tab completes the name). } jumps to the blank line above the method. Delete "
         "it and the method with d and a counted j (the relative line numbers show the count). Then Ctrl-^ "
         "jumps straight back to Main.java.",
    uses=["edit", "paragraph", "d", "count", "p"],
)
course.add(
    name="buffers-by-name", title="Jump to a buffer by name", par=42,
    task="Five files of this Java project are open as buffers. Fix one typo in each of three of them: \"retrun\" "
         "in ProductRepository.java, \"pubilc\" in ProductController.java, and \"priceCnets\" in Order.java.",
    files={
        "src/main/java/shop/App.java": (text('''
            package shop;

            import shop.web.ProductController;

            public class App {
                public static void main(String[] args) {
                    new ProductController().list();
                }
            }
        '''),) * 2,
        "src/main/java/shop/model/Product.java": (text('''
            package shop.model;

            public record Product(String name, int priceCents) {
            }
        '''),) * 2,
        "src/main/java/shop/model/Order.java": (text('''
            package shop.model;

            import java.util.List;

            public record Order(List<Product> items) {
                public int totalCents() {
                    return items.stream().mapToInt(Product::priceCnets).sum();
                }
            }
        '''), text('''
            package shop.model;

            import java.util.List;

            public record Order(List<Product> items) {
                public int totalCents() {
                    return items.stream().mapToInt(Product::priceCents).sum();
                }
            }
        ''')),
        "src/main/java/shop/model/ProductRepository.java": (text('''
            package shop.model;

            import java.util.List;

            public class ProductRepository {
                public List<Product> findAll() {
                    retrun List.of(new Product("Tea", 450));
                }
            }
        '''), text('''
            package shop.model;

            import java.util.List;

            public class ProductRepository {
                public List<Product> findAll() {
                    return List.of(new Product("Tea", 450));
                }
            }
        ''')),
        "src/main/java/shop/web/ProductController.java": (text('''
            package shop.web;

            import shop.model.ProductRepository;

            public class ProductController {
                private final ProductRepository repo = new ProductRepository();

                pubilc void list() {
                    repo.findAll().forEach(System.out::println);
                }
            }
        '''), text('''
            package shop.web;

            import shop.model.ProductRepository;

            public class ProductController {
                private final ProductRepository repo = new ProductRepository();

                public void list() {
                    repo.findAll().forEach(System.out::println);
                }
            }
        ''')),
    },
    open="src/main/java/shop/App.java",
    setup=setup("badd src/main/java/shop/model/Product.java", "badd src/main/java/shop/model/Order.java",
           "badd src/main/java/shop/web/ProductController.java",
           "badd src/main/java/shop/model/ProductRepository.java"),
    hint=":b takes any unique piece of a buffer's name, like :b Repo. \"Product\" alone matches three buffers, "
         "so Vim refuses (E93). Inside each file, search for two letters of the typo and swap them with xp.",
    uses=["buffers", "search", "x", "p"],
)
course.add(
    name="side-by-side", title="Header and source side by side", par=23,
    task="point.c is on the left and point.h on the right. Move the struct point definition (and the blank line "
         "above it) from point.c into point.h, just below the #define line. Then add a declaration of midpoint "
         "to point.h, on the line after distance's: the same text as midpoint's first line in point.c, with "
         "\" {\" replaced by \";\".",
    files={
        "point.c": (text('''
            #include <math.h>
            #include "point.h"

            struct point {
                double x;
                double y;
            };

            double distance(struct point a, struct point b) {
                double dx = a.x - b.x, dy = a.y - b.y;
                return sqrt(dx * dx + dy * dy);
            }

            struct point midpoint(struct point a, struct point b) {
                struct point m = { (a.x + b.x) / 2, (a.y + b.y) / 2 };
                return m;
            }
        '''), text('''
            #include <math.h>
            #include "point.h"

            double distance(struct point a, struct point b) {
                double dx = a.x - b.x, dy = a.y - b.y;
                return sqrt(dx * dx + dy * dy);
            }

            struct point midpoint(struct point a, struct point b) {
                struct point m = { (a.x + b.x) / 2, (a.y + b.y) / 2 };
                return m;
            }
        ''')),
        "point.h": (text('''
            #ifndef POINT_H
            #define POINT_H

            double distance(struct point a, struct point b);

            #endif
        '''), text('''
            #ifndef POINT_H
            #define POINT_H

            struct point {
                double x;
                double y;
            };

            double distance(struct point a, struct point b);
            struct point midpoint(struct point a, struct point b);

            #endif
        ''')),
    },
    open="point.c",
    setup=setup("rightbelow vsplit point.h", "lua vim.wo.winbar = ' %#Comment#%f%*'", "wincmd p"),
    hint="Ctrl-w l and Ctrl-w h move between the two windows, and each window keeps its own cursor. "
         "Paragraph motions do most of the aiming: } jumps to the next blank line, and dap from a blank line "
         "takes it plus the paragraph after it.",
    uses=["windows", "paragraph", "ip", "y", "p", "count", "line", "x", "r"],
)
course.add(
    name="follow-the-include", title="Follow an include and come back", par=9,
    task="The header util/strbuf.h defines a private helper, sb_room, that doesn't belong in a header. Move the "
         "whole function into util/strbuf.c, below the #include lines and above sb_append, with one blank line "
         "on each side. Your cursor starts on the name of the included header.",
    files={
        "util/strbuf.c": (text('''
            #include <stdlib.h>
            #include <string.h>
            #include "strbuf.h"

            void sb_append(struct strbuf *sb, const char *s) {
                size_t n = strlen(s);
                if (sb_room(sb) < n + 1) {
                    sb->cap = sb->len + n + 1;
                    sb->buf = realloc(sb->buf, sb->cap);
                }
                memcpy(sb->buf + sb->len, s, n + 1);
                sb->len += n;
            }
        '''), text('''
            #include <stdlib.h>
            #include <string.h>
            #include "strbuf.h"

            static size_t sb_room(const struct strbuf *sb) {
                return sb->cap - sb->len;
            }

            void sb_append(struct strbuf *sb, const char *s) {
                size_t n = strlen(s);
                if (sb_room(sb) < n + 1) {
                    sb->cap = sb->len + n + 1;
                    sb->buf = realloc(sb->buf, sb->cap);
                }
                memcpy(sb->buf + sb->len, s, n + 1);
                sb->len += n;
            }
        ''')),
        "util/strbuf.h": (text('''
            #ifndef STRBUF_H
            #define STRBUF_H

            #include <stddef.h>

            struct strbuf {
                char *buf;
                size_t len;
                size_t cap;
            };

            static size_t sb_room(const struct strbuf *sb) {
                return sb->cap - sb->len;
            }

            void sb_append(struct strbuf *sb, const char *s);

            #endif
        '''), text('''
            #ifndef STRBUF_H
            #define STRBUF_H

            #include <stddef.h>

            struct strbuf {
                char *buf;
                size_t len;
                size_t cap;
            };

            void sb_append(struct strbuf *sb, const char *s);

            #endif
        ''')),
    },
    open="util/strbuf.c", cursor=(3, 11), setup=setup(),
    hint="gf opens the file whose name is under the cursor. Cut the function with a paragraph motion, then "
         "go back with Ctrl-^ (or Ctrl-o, but count your jumps) and put it below the include line.",
    uses=["gf", "paragraph", "ip", "edit", "p", "count"],
)
course.add(
    name="replace-include-guards", title="Run one command in every header", par=45,
    task="Replace the include guard in every header file, in src/ and src/util/, with #pragma once: delete the "
         "#ifndef and #endif lines, and turn the #define line into #pragma once. Leave the .c files alone "
         "(list.c has an #ifndef block of its own).",
    files={
        "src/main.c": (text('''
            #include "list.h"
            #include "map.h"

            int main(void) {
                struct list *l = list_new();
                struct map *m = map_new();
                return list_len(l) + map_len(m);
            }
        '''),) * 2,
        "src/list.c": (text('''
            #include <stdlib.h>
            #include "list.h"
            #include "util/str.h"

            #ifndef NDEBUG
            #include <stdio.h>
            #endif

            struct list { int len; };
        '''),) * 2,
        "src/list.h": (text('''
            #ifndef LIST_H
            #define LIST_H

            struct list;

            struct list *list_new(void);
            int list_len(const struct list *l);

            #endif
        '''), text('''
            #pragma once

            struct list;

            struct list *list_new(void);
            int list_len(const struct list *l);
        ''')),
        "src/map.h": (text('''
            #ifndef MAP_H
            #define MAP_H

            struct map;

            struct map *map_new(void);
            int map_len(const struct map *m);

            #endif
        '''), text('''
            #pragma once

            struct map;

            struct map *map_new(void);
            int map_len(const struct map *m);
        ''')),
        "src/util/str.h": (text('''
            #ifndef UTIL_STR_H
            #define UTIL_STR_H

            char *str_dup(const char *s);

            #endif
        '''), text('''
            #pragma once

            char *str_dup(const char *s);
        ''')),
    },
    open="src/main.c", setup=setup(),
    hint="Put just the headers in the argument list with :args and a ** glob. Then :argdo runs one :normal "
         "command in each of them: go to the last line and delete it, go to the top and change two lines.",
    uses=["argdo", "normal", "gg", "dd", "c"],
)
course.add(
    name="open-buffers", title="Change every open buffer", par=60,
    task="In the three open buffers (app.py, pricing.py and cart.py), rename round_price to round_cents and "
         "with_tax to add_tax. Leave legacy/report.py alone: it isn't open, and it has its own functions with "
         "those names.",
    files={
        "app.py": (text('''
            from pricing import with_tax

            print(with_tax(1999), with_tax(500))
        '''), text('''
            from pricing import add_tax

            print(add_tax(1999), add_tax(500))
        ''')),
        "pricing.py": (text('''
            def round_price(amount):
                return round(amount, 2)


            def with_tax(amount, rate=0.08):
                return round_price(amount) + round_price(amount * rate)
        '''), text('''
            def round_cents(amount):
                return round(amount, 2)


            def add_tax(amount, rate=0.08):
                return round_cents(amount) + round_cents(amount * rate)
        ''')),
        "cart.py": (text('''
            from pricing import round_price


            class Cart:
                def __init__(self):
                    self.items = []

                def add(self, name, unit_price):
                    self.items.append((name, round_price(unit_price)))
        '''), text('''
            from pricing import round_cents


            class Cart:
                def __init__(self):
                    self.items = []

                def add(self, name, unit_price):
                    self.items.append((name, round_cents(unit_price)))
        ''')),
        "legacy/report.py": (text('''
            def round_price(amount):
                return int(amount * 100) / 100


            def with_tax(amount):
                return round_price(amount * 1.1)


            print(with_tax(3.14159))
        '''),) * 2,
    },
    open="app.py", setup=setup("badd pricing.py", "badd cart.py"),
    hint=":bufdo runs a command in every listed buffer, and | puts a second command after the first. A :s "
         "that finds nothing is an error, and an error skips the rest of the line in that buffer. app.py has no "
         "round_price. The e flag turns that error off.",
    uses=["bufdo", "subst", "range"],
)
course.add(
    name="rename-everywhere", title="Rename a function in every file", par=39,
    task="Rename the function stack_size to stack_len everywhere it appears, in all four files (the header, both "
         ".c files and the test). stack_size_max keeps its name. Your cursor starts on a stack_size call.",
    files={
        "main.c": (text('''
            #include <stdio.h>
            #include "stack.h"

            int main(void) {
                struct stack s = {0};
                stack_push(&s, 1);
                stack_push(&s, 2);
                int n = stack_size(&s);
                printf("%d of %d\\n", n, stack_size_max());
                return 0;
            }
        '''), text('''
            #include <stdio.h>
            #include "stack.h"

            int main(void) {
                struct stack s = {0};
                stack_push(&s, 1);
                stack_push(&s, 2);
                int n = stack_len(&s);
                printf("%d of %d\\n", n, stack_size_max());
                return 0;
            }
        ''')),
        "stack.h": (text('''
            #pragma once

            #define STACK_CAP 16

            struct stack {
                int items[STACK_CAP];
                int top;
            };

            void stack_push(struct stack *s, int x);
            int stack_size(const struct stack *s);
            int stack_size_max(void);
        '''), text('''
            #pragma once

            #define STACK_CAP 16

            struct stack {
                int items[STACK_CAP];
                int top;
            };

            void stack_push(struct stack *s, int x);
            int stack_len(const struct stack *s);
            int stack_size_max(void);
        ''')),
        "stack.c": (text('''
            #include "stack.h"

            void stack_push(struct stack *s, int x) {
                if (stack_size(s) < stack_size_max())
                    s->items[s->top++] = x;
            }

            int stack_size(const struct stack *s) {
                return s->top;
            }

            int stack_size_max(void) {
                return STACK_CAP;
            }
        '''), text('''
            #include "stack.h"

            void stack_push(struct stack *s, int x) {
                if (stack_len(s) < stack_size_max())
                    s->items[s->top++] = x;
            }

            int stack_len(const struct stack *s) {
                return s->top;
            }

            int stack_size_max(void) {
                return STACK_CAP;
            }
        ''')),
        "tests/test_stack.c": (text('''
            #include <assert.h>
            #include "../stack.h"

            int main(void) {
                struct stack s = {0};
                stack_push(&s, 7);
                assert(stack_size(&s) == 1 && stack_size(&s) <= stack_size_max());
                return 0;
            }
        '''), text('''
            #include <assert.h>
            #include "../stack.h"

            int main(void) {
                struct stack s = {0};
                stack_push(&s, 7);
                assert(stack_len(&s) == 1 && stack_len(&s) <= stack_size_max());
                return 0;
            }
        ''')),
    },
    open="main.c", cursor=(8, 13), setup=setup(),
    hint="* searches for the word under the cursor, as a whole word. An empty pattern, //, reuses the last "
         "search: once in :vimgrep to fill the quickfix list, and again in the :s that :cdo runs at each match. "
         "One line in the test calls stack_size twice.",
    uses=["vimgrep", "cdo", "star", "subst"],
)
course.add(
    name="match-case", title="Rename without touching the class", par=40,
    task="Rename the variable and parameter order to purchase in every file. The class Order, the class "
         "OrderService and the field orders keep their names. Your cursor starts on an order variable.",
    files={
        "Main.java": (text('''
            import shop.Order;
            import shop.OrderService;

            public class Main {
                public static void main(String[] args) {
                    Order order = new Order(3);
                    new OrderService().submit(order);
                    System.out.println(order + " x" + order.quantity());
                }
            }
        '''), text('''
            import shop.Order;
            import shop.OrderService;

            public class Main {
                public static void main(String[] args) {
                    Order purchase = new Order(3);
                    new OrderService().submit(purchase);
                    System.out.println(purchase + " x" + purchase.quantity());
                }
            }
        ''')),
        "shop/Order.java": (text('''
            package shop;

            public record Order(int quantity) {
            }
        '''),) * 2,
        "shop/OrderService.java": (text('''
            package shop;

            import java.util.ArrayList;
            import java.util.List;

            public class OrderService {
                private final List<Order> orders = new ArrayList<>();

                public void submit(Order order) {
                    if (order.quantity() > 0) {
                        orders.add(order);
                    }
                }
            }
        '''), text('''
            package shop;

            import java.util.ArrayList;
            import java.util.List;

            public class OrderService {
                private final List<Order> orders = new ArrayList<>();

                public void submit(Order purchase) {
                    if (purchase.quantity() > 0) {
                        orders.add(purchase);
                    }
                }
            }
        ''')),
    },
    open="Main.java", cursor=(6, 15), setup=setup(),
    hint="Same tools as the last exercise, with a catch: \\<order\\> is all lowercase, so it ignores case and "
         "also matches Order, both in :vimgrep and in :s//. The I flag makes :s match case.",
    uses=["vimgrep", "cdo", "star", "subst", "subst-flags"],
)
course.add(
    name="step-through-matches", title="Step through the matches", par=52,
    task="Every call to connect() should take its host from the config. Replace the first argument of each "
         "call with cfg.host, in all files. Don't change the definition of connect in db.py, or the call to "
         "disconnect().",
    files={
        "app.py": (text('''
            from config import cfg
            from db import connect, disconnect

            conn = connect("localhost", 5432)
            print(conn.query("SELECT 1"))
            disconnect(conn, force=True)
        '''), text('''
            from config import cfg
            from db import connect, disconnect

            conn = connect(cfg.host, 5432)
            print(conn.query("SELECT 1"))
            disconnect(conn, force=True)
        ''')),
        "db.py": (text('''
            import socket


            def connect(host, port):
                return socket.create_connection((host, port))


            def disconnect(conn, force=False):
                conn.close()
        '''),) * 2,
        "jobs/backup.py": (text('''
            import os

            from config import cfg
            from db import connect

            src = connect("10.0.0.7", 5432)
            dst = connect(os.environ["BACKUP_HOST"], 5433)
        '''), text('''
            import os

            from config import cfg
            from db import connect

            src = connect(cfg.host, 5432)
            dst = connect(cfg.host, 5433)
        ''')),
        "jobs/report.py": (text('''
            from config import cfg
            from db import connect

            HOST = "db.internal"
            print(connect(HOST, 5432).query("SELECT count(*) FROM orders"))
        '''), text('''
            from config import cfg
            from db import connect

            HOST = "db.internal"
            print(connect(cfg.host, 5432).query("SELECT count(*) FROM orders"))
        ''')),
    },
    open="app.py", setup=setup(),
    hint="End the :vimgrep pattern with \\zs so each match starts on the first argument, and start it with \\< "
         "so disconnect( doesn't match. Make the first change with ct, then ]q goes to the next match and . "
         "repeats it. At the match you want to keep, just ]q again.",
    uses=["vimgrep", "c", "t", "dot"],
)
course.add(
    name="import-once", title="Once per file, not once per match", par=50,
    task="Add import json as the first line of every module that calls a json function (app.py, store.py and "
         "api/handlers.py), exactly once per file. pricing.py only mentions JSON in a comment: leave it alone.",
    files={
        "app.py": (text('''
            import os

            from store import load_cart, save_cart


            def main():
                cart = load_cart(os.environ.get("CART", "cart.json"))
                print(json.dumps(cart, indent=2))
                save_cart(cart)
                print(json.dumps({"saved": True}))
        '''), text('''
            import json
            import os

            from store import load_cart, save_cart


            def main():
                cart = load_cart(os.environ.get("CART", "cart.json"))
                print(json.dumps(cart, indent=2))
                save_cart(cart)
                print(json.dumps({"saved": True}))
        ''')),
        "store.py": (text('''
            from pathlib import Path


            def load_cart(path):
                return json.loads(Path(path).read_text())


            def save_cart(cart, path="cart.json"):
                Path(path).write_text(json.dumps(cart))
        '''), text('''
            import json
            from pathlib import Path


            def load_cart(path):
                return json.loads(Path(path).read_text())


            def save_cart(cart, path="cart.json"):
                Path(path).write_text(json.dumps(cart))
        ''')),
        "pricing.py": (text('''
            # Prices are whole cents. Never store floats in JSON.


            def with_tax(cents, rate=8):
                return cents + cents * rate // 100
        '''),) * 2,
        "api/handlers.py": (text('''
            from store import load_cart


            def get_cart(request):
                return json.dumps(load_cart(request.path))
        '''), text('''
            import json
            from store import load_cart


            def get_cart(request):
                return json.dumps(load_cart(request.path))
        ''')),
    },
    open="app.py", setup=setup(),
    hint=":cdo runs once per match, so a file with two matches would get two imports. :cfdo runs once per "
         "file. And json\\. is all lowercase, so it ignores case and matches \"JSON.\" too. \\C fixes that.",
    uses=["vimgrep", "cdo", "normal", "gg", "o"],
)
course.add(
    name="add-a-parameter", title="Add a parameter everywhere", par=74,
    task="Give log a Level parameter: in Logger.java and ConsoleLogger.java, change log(String msg) to "
         "log(Level level, String msg), and at every call pass Level.INFO as the new first argument, like "
         "logger.log(Level.INFO, \"ready\").",
    files={
        "App.java": (text('''
            import net.Server;

            public class App {
                private final Logger logger = new ConsoleLogger();

                void run() {
                    logger.log("starting");
                    new Server(logger).listen(8080);
                    logger.log("ready");
                }
            }
        '''), text('''
            import net.Server;

            public class App {
                private final Logger logger = new ConsoleLogger();

                void run() {
                    logger.log(Level.INFO, "starting");
                    new Server(logger).listen(8080);
                    logger.log(Level.INFO, "ready");
                }
            }
        ''')),
        "Level.java": (text('''
            public enum Level { INFO, WARN, ERROR }
        '''),) * 2,
        "Logger.java": (text('''
            public interface Logger {
                void log(String msg);
            }
        '''), text('''
            public interface Logger {
                void log(Level level, String msg);
            }
        ''')),
        "ConsoleLogger.java": (text('''
            public class ConsoleLogger implements Logger {
                @Override
                public void log(String msg) {
                    System.err.println(msg);
                }
            }
        '''), text('''
            public class ConsoleLogger implements Logger {
                @Override
                public void log(Level level, String msg) {
                    System.err.println(msg);
                }
            }
        ''')),
        "net/Server.java": (text('''
            package net;

            public class Server {
                private final Logger logger;

                public Server(Logger logger) {
                    this.logger = logger;
                }

                public void listen(int port) {
                    logger.log("listening on " + port);
                    logger.log("accepting connections");
                }
            }
        '''), text('''
            package net;

            public class Server {
                private final Logger logger;

                public Server(Logger logger) {
                    this.logger = logger;
                }

                public void listen(int port) {
                    logger.log(Level.INFO, "listening on " + port);
                    logger.log(Level.INFO, "accepting connections");
                }
            }
        ''')),
    },
    open="App.java", setup=setup(),
    hint="One :vimgrep for every log( call and declaration. Then one :cdo can run two substitutions at each "
         "match, joined with |: one for lines where ( is followed by a quote, one for lines where it's "
         "followed by String. Give the first one the e flag, as in exercise 6.",
    uses=["vimgrep", "cdo", "subst"],
)
course.add(
    name="review-release", title="Review · Cut a release", par=174,
    task=("Review of the whole course: cut release 1.5.0 of tally, a small Python CLI. pyproject.toml is open, and "
          "README.md, CHANGELOG.md, src/tally/__init__.py and src/tally/cli.py are open as buffers. "
          "tests/test_cli.py and docs/usage.md aren't open yet. CHANGELOG.md's old 1.4.2 entry and its \"drop "
          "Python 3.8\" bullet stay as they are."),
    steps=[
        "pyproject.toml: version 1.5.0.",
        "pyproject.toml: Python 3.8 is no longer supported: requires-python = \">=3.9\".",
        "pyproject.toml: require click>=8.1.",
        "pyproject.toml: add \"rich>=13.0\", on its own line below click.",
        "src/tally/__init__.py: __version__ = \"1.5.0\".",
        "tests/test_cli.py: the expected --version output says 1.5.0.",
        "cli.py: version_option() takes __version__ instead of a hard-coded string...",
        "...imported with from tally import __version__, on a line above the count_file import.",
        "cli.py: delete the breakpoint() left in main().",
        "cli.py: --json's help in the style of -c's: \"Print counts as JSON.\"",
        "README.md: Needs Python 3.9 or newer.",
        "README.md: pip install tally==1.5.0.",
        "docs/usage.md: the --version example prints 1.5.0.",
        "docs/usage.md: a row for --json between -c and --version, with the help text from step 10.",
        ("CHANGELOG.md: the four Unreleased bullets are now 1.5.0: give them a ## 1.5.0 - 2026-11-04 heading, with "
         "a blank line above it. ## Unreleased stays at the top, empty."),
        "CHANGELOG.md: each of those bullets starts with a capital letter...",
        "...and ends with a period.",
    ],
    files={
        "pyproject.toml": (text('''
            [project]
            name = "tally"
            version = "1.4.2"
            description = "Count lines, words and bytes"
            readme = "README.md"
            requires-python = ">=3.8"
            dependencies = [
                "click>=8.0",
            ]

            [project.scripts]
            tally = "tally.cli:main"
        '''), text('''
            [project]
            name = "tally"
            version = "1.5.0"
            description = "Count lines, words and bytes"
            readme = "README.md"
            requires-python = ">=3.9"
            dependencies = [
                "click>=8.1",
                "rich>=13.0",
            ]

            [project.scripts]
            tally = "tally.cli:main"
        ''')),
        "src/tally/__init__.py": (text('''
            """Count lines, words and bytes."""

            __version__ = "1.4.2"
        '''), text('''
            """Count lines, words and bytes."""

            __version__ = "1.5.0"
        ''')),
        "src/tally/cli.py": (text('''
            import json

            import click

            from tally.count import count_file


            @click.command()
            @click.version_option("1.4.2")
            @click.option("-c", "--bytes", "show_bytes", is_flag=True, help="Print byte counts.")
            @click.option("--json", "as_json", is_flag=True, help="print the counts as json")
            @click.argument("paths", nargs=-1, type=click.Path(exists=True))
            def main(show_bytes, as_json, paths):
                counts = [count_file(p) for p in paths]
                breakpoint()
                if as_json:
                    click.echo(json.dumps([c._asdict() for c in counts]))
                    return
                for path, c in zip(paths, counts):
                    fields = [c.lines, c.words] + ([c.bytes] if show_bytes else [])
                    click.echo(" ".join(map(str, fields)) + " " + path)
        '''), text('''
            import json

            import click

            from tally import __version__
            from tally.count import count_file


            @click.command()
            @click.version_option(__version__)
            @click.option("-c", "--bytes", "show_bytes", is_flag=True, help="Print byte counts.")
            @click.option("--json", "as_json", is_flag=True, help="Print counts as JSON.")
            @click.argument("paths", nargs=-1, type=click.Path(exists=True))
            def main(show_bytes, as_json, paths):
                counts = [count_file(p) for p in paths]
                if as_json:
                    click.echo(json.dumps([c._asdict() for c in counts]))
                    return
                for path, c in zip(paths, counts):
                    fields = [c.lines, c.words] + ([c.bytes] if show_bytes else [])
                    click.echo(" ".join(map(str, fields)) + " " + path)
        ''')),
        "tests/test_cli.py": (text('''
            from click.testing import CliRunner

            from tally.cli import main


            def test_version():
                result = CliRunner().invoke(main, ["--version"])
                assert result.output == "main, version 1.4.2\\n"
        '''), text('''
            from click.testing import CliRunner

            from tally.cli import main


            def test_version():
                result = CliRunner().invoke(main, ["--version"])
                assert result.output == "main, version 1.5.0\\n"
        ''')),
        "README.md": (text('''
            # tally

            Count lines, words and bytes, like wc, but with JSON output.
            Needs Python 3.8 or newer:

                pip install tally==1.4.2

            See docs/usage.md for every option.
        '''), text('''
            # tally

            Count lines, words and bytes, like wc, but with JSON output.
            Needs Python 3.9 or newer:

                pip install tally==1.5.0

            See docs/usage.md for every option.
        ''')),
        "docs/usage.md": (text('''
            # Usage

                $ tally --version
                main, version 1.4.2

            | Option | Does |
            |---|---|
            | `-c`, `--bytes` | Print byte counts. |
            | `--version` | Show the version and exit. |
        '''), text('''
            # Usage

                $ tally --version
                main, version 1.5.0

            | Option | Does |
            |---|---|
            | `-c`, `--bytes` | Print byte counts. |
            | `--json` | Print counts as JSON. |
            | `--version` | Show the version and exit. |
        ''')),
        "CHANGELOG.md": (text('''
            # Changelog

            ## Unreleased

            - add --json, to print the counts as JSON
            - count bytes with -c
            - fix the crash on empty files
            - drop Python 3.8

            ## 1.4.2 - 2026-08-30

            - Fix files without a trailing newline.
        '''), text('''
            # Changelog

            ## Unreleased

            ## 1.5.0 - 2026-11-04

            - Add --json, to print the counts as JSON.
            - Count bytes with -c.
            - Fix the crash on empty files.
            - Drop Python 3.8.

            ## 1.4.2 - 2026-08-30

            - Fix files without a trailing newline.
        ''')),
    },
    open="pyproject.toml",
    setup=setup("badd src/tally/__init__.py", "badd src/tally/cli.py", "badd CHANGELOG.md", "badd README.md"),
    hint=("Seven lines mention 1.4.2. One :vimgrep finds them all, and its list doubles as a route through the "
          "files, but entry 1 is CHANGELOG.md's old heading: :2,$cdo skips it. (:vimgrep doesn't set the search "
          "pattern, so the :s needs its own.) [q and ]q step through the list. A Visual block capitalizes the four "
          "bullets at once, and in cli.py, __ and Ctrl-n complete __version__ from __init__.py."),
    uses=["vimgrep", "cdo", "increment", "block-insert", "visual-ends", "case", "paren", "quote", "complete",
          "readonly", "yank0", "iw"],
)
course.add(
    name="review-rename-command", title="Review · Rename a command", par=129,
    task=("Review of the whole course: in this small C to-do app, the done command becomes finish. src/main.c is "
          "open; src/commands.h, src/commands.c and README.md aren't yet. Only the command is renamed: the help "
          "text \"mark task N as done\" and README.md's \"When you're done\" keep their done."),
    steps=[
        "main.c: in the table, the done command is now called finish, and its function cmd_finish...",
        "...commands.h: its prototype too...",
        "...commands.c: the function...",
        "...and its error message (\"finish: expected...\").",
        "README.md: the example runs todo finish 1.",
        "main.c: sort the table by command name, so usage lists them alphabetically.",
        "commands.h: sort the prototypes the same way.",
        "commands.c: and the functions: cmd_list moves to the end of the file, with a blank line above it.",
        "main.c: usage() pads the names to 8 characters: %-8s.",
        "main.c: an unknown command prints the usage too, after its message, as a missing one does.",
        "README.md: end with a ## Commands section: a blank line, the heading, a blank line...",
        "...and a bullet per command from main.c's table, in its order: - `add`: add a task",
    ],
    files={
        "src/main.c": (text('''
            #include <stdio.h>
            #include <string.h>

            #include "commands.h"

            static const struct command COMMANDS[] = {
                {"list", cmd_list, "list the open tasks"},
                {"add", cmd_add, "add a task"},
                {"done", cmd_done, "mark task N as done"},
            };

            #define NUM_COMMANDS 3

            static void usage(FILE *out) {
                fprintf(out, "usage: todo COMMAND [ARGS]\\n");
                for (int i = 0; i < NUM_COMMANDS; i++)
                    fprintf(out, "  %-6s %s\\n", COMMANDS[i].name, COMMANDS[i].help);
            }

            int main(int argc, char **argv) {
                if (argc < 2) {
                    usage(stderr);
                    return 2;
                }
                for (int i = 0; i < NUM_COMMANDS; i++)
                    if (strcmp(argv[1], COMMANDS[i].name) == 0)
                        return COMMANDS[i].run(argc - 2, argv + 2);
                fprintf(stderr, "todo: unknown command '%s'\\n", argv[1]);
                return 2;
            }
        '''), text('''
            #include <stdio.h>
            #include <string.h>

            #include "commands.h"

            static const struct command COMMANDS[] = {
                {"add", cmd_add, "add a task"},
                {"finish", cmd_finish, "mark task N as done"},
                {"list", cmd_list, "list the open tasks"},
            };

            #define NUM_COMMANDS 3

            static void usage(FILE *out) {
                fprintf(out, "usage: todo COMMAND [ARGS]\\n");
                for (int i = 0; i < NUM_COMMANDS; i++)
                    fprintf(out, "  %-8s %s\\n", COMMANDS[i].name, COMMANDS[i].help);
            }

            int main(int argc, char **argv) {
                if (argc < 2) {
                    usage(stderr);
                    return 2;
                }
                for (int i = 0; i < NUM_COMMANDS; i++)
                    if (strcmp(argv[1], COMMANDS[i].name) == 0)
                        return COMMANDS[i].run(argc - 2, argv + 2);
                fprintf(stderr, "todo: unknown command '%s'\\n", argv[1]);
                usage(stderr);
                return 2;
            }
        ''')),
        "src/commands.h": (text('''
            #ifndef COMMANDS_H
            #define COMMANDS_H

            struct command {
                const char *name;
                int (*run)(int argc, char **argv);
                const char *help;
            };

            int cmd_list(int argc, char **argv);
            int cmd_add(int argc, char **argv);
            int cmd_done(int argc, char **argv);

            #endif
        '''), text('''
            #ifndef COMMANDS_H
            #define COMMANDS_H

            struct command {
                const char *name;
                int (*run)(int argc, char **argv);
                const char *help;
            };

            int cmd_add(int argc, char **argv);
            int cmd_finish(int argc, char **argv);
            int cmd_list(int argc, char **argv);

            #endif
        ''')),
        "src/commands.c": (text('''
            #include <stdio.h>
            #include <stdlib.h>

            #include "commands.h"
            #include "store.h"

            int cmd_list(int argc, char **argv) {
                (void)argv;
                if (argc != 0) {
                    fprintf(stderr, "list: takes no arguments\\n");
                    return 2;
                }
                return store_print(stdout);
            }

            int cmd_add(int argc, char **argv) {
                if (argc != 1) {
                    fprintf(stderr, "add: expected 1 argument, got %d\\n", argc);
                    return 2;
                }
                return store_append(argv[0]);
            }

            int cmd_done(int argc, char **argv) {
                if (argc != 1) {
                    fprintf(stderr, "done: expected 1 argument, got %d\\n", argc);
                    return 2;
                }
                return store_remove(atoi(argv[0]));
            }
        '''), text('''
            #include <stdio.h>
            #include <stdlib.h>

            #include "commands.h"
            #include "store.h"

            int cmd_add(int argc, char **argv) {
                if (argc != 1) {
                    fprintf(stderr, "add: expected 1 argument, got %d\\n", argc);
                    return 2;
                }
                return store_append(argv[0]);
            }

            int cmd_finish(int argc, char **argv) {
                if (argc != 1) {
                    fprintf(stderr, "finish: expected 1 argument, got %d\\n", argc);
                    return 2;
                }
                return store_remove(atoi(argv[0]));
            }

            int cmd_list(int argc, char **argv) {
                (void)argv;
                if (argc != 0) {
                    fprintf(stderr, "list: takes no arguments\\n");
                    return 2;
                }
                return store_print(stdout);
            }
        ''')),
        "README.md": (text('''
            # todo

            A to-do list for your terminal. When you're done with a task, it's gone.

                todo add "water the plants"
                todo list
                todo done 1
        '''), text('''
            # todo

            A to-do list for your terminal. When you're done with a task, it's gone.

                todo add "water the plants"
                todo list
                todo finish 1

            ## Commands

            - `add`: add a task
            - `finish`: mark task N as done
            - `list`: list the open tasks
        ''')),
    },
    open="src/main.c",
    setup=setup(),
    hint=(":vimgrep done ** lists every line with a done, README.md's sentence first: :2,$cdo skips it. Without "
          "the g flag :s changes the first done on a line, so on main.c's table line & changes the second "
          "(cmd_done) and leaves the help alone. Ctrl-a and Ctrl-x read the - in %-6s as a minus sign. A macro "
          "turns each table line into a bullet."),
    uses=["vimgrep", "cdo", "amp", "sort", "increment", "line-complete", "paragraph", "ip", "yank0", "macro",
          "replay", "f"],
)

course.run()
