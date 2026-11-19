"""Drills for Project 08: short problems that practice one command at a time.
Play them with:  python3 check.py drill      (the reference solutions are in ../solutions/drills/)"""
from trainer import Drills, text

drills = Drills(__file__)

# Completion (Ctrl-n, Ctrl-x Ctrl-l) could otherwise look in other buffers. In the drills, as in the
# exercises, it only searches your own file.
OWN_FILE_ONLY = ["setlocal complete=."]
# The q: window is a buffer of its own, so there completion would still search your file. Setting the option
# globally keeps completion inside whichever buffer you're typing in.
OWN_BUFFER_ONLY = ["set complete=."]

# ---------- Ctrl-w Ctrl-u Ctrl-h ----------

ctrl_w = drills.command(
    "ctrl-w", "Ctrl-w  Ctrl-u  Ctrl-h", "delete while typing",
    """In Insert mode, Ctrl-w deletes the word before the cursor, Ctrl-u everything before the cursor on
    the line, and Ctrl-h one character (it's the same as Backspace). Ctrl-w first skips spaces, then deletes
    either a run of letters, digits and underscores or a run of other characters, so at the end of user.name
    it deletes name, then the dot. Ctrl-u keeps the line's indent (press it again to delete that too), and
    on an empty, auto-indented line Ctrl-u and Ctrl-w remove the whole indent. They can delete text that was
    there before you started typing, so A then Ctrl-w retypes the last word of a line, but they stop once at
    the spot where the insert began: press again to keep going. All three work on the command line too.""",
    examples=[("A Ctrl-w", "retype the line's last word"), ("Ctrl-w", "delete the word before the cursor"),
              ("Ctrl-u", "delete back to the indent"), ("Ctrl-h", "delete one character"),
              ("o Ctrl-w", "drop the comment leader o added")],
)
ctrl_w.add(
    title="Switch the editor", par=6, ext="sh", setup=OWN_FILE_ONLY,
    task="Make nvim the editor instead of nano.",
    start="export EDITOR=nano",
    target="export EDITOR=nvim",
    hint="A starts typing at the end of the line, and Ctrl-w deletes the word before the cursor. The = isn't "
         "part of a word, so it stays.",
    uses=["insert"],
)
ctrl_w.add(
    title="Stop at the dot", par=7, ext="py", setup=OWN_FILE_ONLY,
    task="Send to the user's email, not their name: change user.name to user.email.",
    start="recipient = user.name",
    target="recipient = user.email",
    hint="A dot isn't part of a word, so from the end of user.name, Ctrl-w deletes just name.",
    uses=["insert"],
)
ctrl_w.add(
    title="Code below a comment", par=16, ext="sh", setup=OWN_FILE_ONLY,
    task="Add the command hugo --minify on a new line right below \"# build the site\".",
    start=text("""
        #!/bin/sh
        # build the site
        # then publish it
        rsync -a public/ web:/srv/site
    """),
    target=text("""
        #!/bin/sh
        # build the site
        hugo --minify
        # then publish it
        rsync -a public/ web:/srv/site
    """),
    hint="o on a comment line starts the new line with \"# \" already typed. Ctrl-w deletes it in one go: it "
         "skips the space, then deletes the #.",
    uses=["o"],
)
ctrl_w.add(
    title="Two words back", par=11, ext="py", setup=OWN_FILE_ONLY,
    task="Import scipy too, and drop the alias: the line should read import numpy, scipy.",
    start="import numpy as np",
    target="import numpy, scipy",
    hint="Ctrl-w twice deletes np and as, but leaves the space after numpy. Ctrl-h deletes that one "
         "character, and the rest is typing.",
    uses=["insert"],
)
ctrl_w.add(
    title="Turn the features on", par=12, ext="ini", setup=OWN_FILE_ONLY,
    task="Set all three features to true.",
    start=text("""
        [features]
        dark_mode = false
        beta_search = false
        new_editor = false
    """),
    target=text("""
        [features]
        dark_mode = true
        beta_search = true
        new_editor = true
    """),
    hint="A, Ctrl-w and the new word are all one insert, so . repeats the whole thing, even on lines of "
         "different lengths.",
    uses=["insert", "dot"],
)
ctrl_w.add(
    title="A smaller base image", par=24, ext="dockerfile", setup=OWN_FILE_ONLY,
    task="Switch the image from python:3.12-slim to python:3.12-alpine, and add a second line: "
         "RUN apk add gcc",
    start="FROM python:3.12-slim",
    target=text("""
        FROM python:3.12-alpine
        RUN apk add gcc
    """),
    hint="Ctrl-w from the end of the line deletes slim and stops at the -. You're still in Insert mode "
         "afterwards, so keep typing, new line included.",
    uses=["insert"],
)
ctrl_w.add(
    title="Back to the top level", par=10, ext="md", setup=OWN_FILE_ONLY,
    task="Add a top-level item \"- Usage\" at the end of the list, with no indent.",
    start=text("""
        - Setup
            - install Neovim
                - check the version
    """),
    target=text("""
        - Setup
            - install Neovim
                - check the version
        - Usage
    """),
    hint="o copies the indent of the line above (8 spaces here). On a line that's only indent, Ctrl-u deletes "
         "all of it in one key.",
    uses=["gg", "o"],
)
ctrl_w.add(
    title="A here-document", par=27, ext="sh", setup=OWN_FILE_ONLY,
    task="Fill in the here-document after cat: the lines [server] and port = 8080, then EOF. All three must "
         "start at column 0, or the shell won't find the EOF.",
    start=text("""
        write_config() {
            if [ ! -f app.ini ]; then
                cat > app.ini <<EOF
            fi
        }
    """),
    target=text("""
        write_config() {
            if [ ! -f app.ini ]; then
                cat > app.ini <<EOF
        [server]
        port = 8080
        EOF
            fi
        }
    """),
    hint="The new line starts with the cat line's indent. Ctrl-u wipes it, and the lines after it follow the "
         "new indent: none.",
    uses=["o", "complete"],
)
ctrl_w.add(
    title="Prototype to function", par=19, ext="c", setup=OWN_FILE_ONLY,
    task="Turn the prototype into a definition: replace the ; with \" {\", then a body line p->used = 0; "
         "and a closing }.",
    start="void reset(struct pool *p);",
    target=text("""
        void reset(struct pool *p) {
            p->used = 0;
        }
    """),
    hint="A then Ctrl-h deletes the ; and leaves you typing right there. C's indenting places the body and "
         "the }.",
    uses=["insert"],
)
ctrl_w.add(
    title="Use the constant", par=8, ext="py", setup=OWN_FILE_ONLY,
    task="Both timeouts should use DEFAULT_TIMEOUT instead of a number.",
    start=text("""
        DEFAULT_TIMEOUT = 30
        connect_timeout = 10
        read_timeout = 15
    """),
    target=text("""
        DEFAULT_TIMEOUT = 30
        connect_timeout = DEFAULT_TIMEOUT
        read_timeout = DEFAULT_TIMEOUT
    """),
    hint="A and Ctrl-w delete the number. Instead of typing the long name, type D and press Ctrl-p to "
         "complete it from line 1. Then . repeats it all on the next line.",
    uses=["insert", "complete", "dot"],
)
ctrl_w.add(
    title="A newer key", par=13, ext="conf", setup=OWN_FILE_ONLY,
    task="Switch to the newer SSH key: the IdentityFile line should end in ~/.ssh/id_ed25519.",
    start=text("""
        Host web1
            HostName 10.0.0.12
            User deploy
            IdentityFile ~/.ssh/id_rsa
    """),
    target=text("""
        Host web1
            HostName 10.0.0.12
            User deploy
            IdentityFile ~/.ssh/id_ed25519
    """),
    hint="An underscore is part of a word, but a slash isn't: from the end of the line, Ctrl-w deletes id_rsa "
         "and stops at the /.",
    uses=["gg", "insert"],
)
ctrl_w.add(
    title="Dots and a quote", par=11, ext="sh", setup=OWN_FILE_ONLY,
    task="Finish the message: it should say \"Deploying to web1\" instead of \"Deploying...\".",
    start='echo "Deploying..."',
    target='echo "Deploying to web1"',
    hint="Ctrl-w deletes either a run of letters and digits or a run of other characters. The three dots and the "
         "closing quote are one run.",
    uses=["insert"],
)
ctrl_w.add(
    title="Keep the #", par=10, ext="sh", setup=OWN_FILE_ONLY,
    task="The script has no #! line. Add #!/bin/sh as a new first line, above the comment.",
    start=text("""
        # deploy.sh: build the site and upload it
        set -e
        hugo --minify
        rsync -a public/ web1:/srv/www/
    """),
    target=text("""
        #!/bin/sh
        # deploy.sh: build the site and upload it
        set -e
        hugo --minify
        rsync -a public/ web1:/srv/www/
    """),
    hint="O on a comment line starts the new line with \"# \". You want the # but not the space after it, and "
         "Ctrl-h deletes one character.",
    uses=["o"],
)
ctrl_w.add(
    title="Scrub the secrets", par=15, ext="env", setup=OWN_FILE_ONLY,
    task="This is going into the repository as an example file: replace each secret value with changeme.",
    start=text("""
        DB_PASSWORD=hunter2
        API_TOKEN=a1b2c3d4
        SESSION_SECRET=letmein
    """),
    target=text("""
        DB_PASSWORD=changeme
        API_TOKEN=changeme
        SESSION_SECRET=changeme
    """),
    hint="A, Ctrl-w and the new word are one insert, so . repeats it on the next line, whatever the length of "
         "the value there.",
    uses=["insert", "dot"],
)
ctrl_w.add(
    title="A second document", par=6, ext="yaml", setup=OWN_FILE_ONLY,
    task="A Service is going into this manifest next. Start its document: add a line --- at the end, at column 0.",
    start=text("""
        apiVersion: v1
        kind: Pod
        metadata:
          name: web
        spec:
          containers:
            - name: nginx
              image: nginx:1.27
    """),
    target=text("""
        apiVersion: v1
        kind: Pod
        metadata:
          name: web
        spec:
          containers:
            - name: nginx
              image: nginx:1.27
        ---
    """),
    hint="o copies the last line's indent, three levels of it. Ctrl-u deletes all of it in one key, where Ctrl-d "
         "or Backspace would take three.",
    uses=["gg", "o"],
)
ctrl_w.add(
    title="Enter continues it too", par=22, ext="java", setup=OWN_FILE_ONLY, cursor=(2, 1),
    task="End the comment with the word early, and below it add the line validate(order); The cursor starts on "
         "the comment.",
    start=text("""
        void save(Order order) {
            // reject bad input
            repository.save(order);
        }
    """),
    target=text("""
        void save(Order order) {
            // reject bad input early
            validate(order);
            repository.save(order);
        }
    """),
    hint="Enter in the middle of an insert continues a comment just as o does, so the new line starts with "
         "\"// \". Ctrl-w removes it and keeps the indent. order is already in the file.",
    uses=["insert", "complete"],
)
ctrl_w.add(
    title="A type and a new property", par=16, ext="ts", setup=OWN_FILE_ONLY, cursor=(3, 1),
    task="role should have the type Role, and below it add a property email: string. The cursor starts on "
         "role's line.",
    start=text("""
        interface User {
            id: string
            role: string
        }
    """),
    target=text("""
        interface User {
            id: string
            role: Role
            email: string
        }
    """),
    hint="Ctrl-w swaps the last word, and Enter carries on with a new line at the same indent. string is still on "
         "the line above, so s and Ctrl-p type it.",
    uses=["insert", "complete"],
)
ctrl_w.add(
    title="Two fields at the end", par=22, ext="csv", setup=OWN_FILE_ONLY, cursor=(2, 1),
    task="Ada was promoted and is on leave: her role becomes manager and her status inactive. The cursor starts on "
         "her row.",
    start=text("""
        id,name,role,email,status
        42,Ada Lovelace,engineer,ada@example.com,active
    """),
    target=text("""
        id,name,role,email,status
        42,Ada Lovelace,manager,ada@example.com,inactive
    """),
    hint="Change the status with A and Ctrl-w. Still in Insert mode, Ctrl-o 2F, jumps back to the comma right "
         "after the role, and Ctrl-w deletes the role in front of it.",
    uses=["insert", "ctrl-o", "f", "count"],
)
ctrl_w.add(
    title="The same line under each comment", par=28, ext="c", setup=OWN_FILE_ONLY,
    task="Both functions say the caller holds the lock, so check it: below each of the two comments, add the line "
         "assert_held(&q->lock);",
    start=text("""
        void push(struct queue *q, int x)
        {
            // caller holds q->lock
            q->items[q->len++] = x;
        }

        int pop(struct queue *q)
        {
            // caller holds q->lock
            return q->items[--q->len];
        }
    """),
    target=text("""
        void push(struct queue *q, int x)
        {
            // caller holds q->lock
            assert_held(&q->lock);
            q->items[q->len++] = x;
        }

        int pop(struct queue *q)
        {
            // caller holds q->lock
            assert_held(&q->lock);
            return q->items[--q->len];
        }
    """),
    hint="o continues the comment and Ctrl-w takes the leader away again. It's all one insert, Ctrl-w included, "
         "so . adds the same line below the other comment.",
    uses=["o", "complete", "dot", "count"],
)
ctrl_w.add(
    title="The main guard", par=41, ext="py", setup=OWN_FILE_ONLY,
    task="Make the script runnable: at the end, after two blank lines, add if __name__ == \"__main__\": and, "
         "inside it, the line main(sys.argv).",
    start=text("""
        import sys


        def main(argv):
            for path in argv[1:]:
                print(path)
    """),
    target=text("""
        import sys


        def main(argv):
            for path in argv[1:]:
                print(path)


        if __name__ == "__main__":
            main(sys.argv)
    """),
    hint="Python keeps the last line's indent for a new line, even after blank lines. Ctrl-u deletes all of it "
         "once. main, sys and argv are all in the file already.",
    uses=["gg", "o", "complete"],
)

# ---------- Ctrl-n Ctrl-p ----------

complete = drills.command(
    "complete", "Ctrl-n  Ctrl-p", "complete a word",
    """In Insert mode, Ctrl-n completes the word you've started with the next word in the file that begins
    the same way, and Ctrl-p with the previous one. Ctrl-n searches forward from the cursor and wraps around
    from the end of the file to the top; Ctrl-p searches backward, so it finds the nearest match above first.
    The first press puts a match in right away, and pressing again steps through the others (a menu lists
    them). Just keep typing to accept it, or press Ctrl-y to accept and close the menu, Ctrl-e to go back to
    what you typed. With ignorecase and smartcase on (as here), lowercase letters match either case, but a
    capital letter makes the match exact. In these exercises it only looks in your own file.""",
    examples=[("ma Ctrl-n", "complete, say, maxRetries"), ("us Ctrl-p", "the nearest match above"),
              ("Ctrl-p Ctrl-p", "the match after that"), ("Ctrl-y", "accept the match"),
              ("Ctrl-e", "back to what you typed")],
)
complete.add(
    title="One long name", par=4, ext="java", setup=OWN_FILE_ONLY, cursor=(2, 1),
    task="Set limit to maxConnectionsPerHost. The cursor starts on line 2.",
    start=text("""
        int maxConnectionsPerHost = 8;
        int limit = ;
    """),
    target=text("""
        int maxConnectionsPerHost = 8;
        int limit = maxConnectionsPerHost;
    """),
    hint="Get in front of the ;, type m and press Ctrl-n: no other word in the file starts with an m.",
    uses=["line", "insert"],
)
complete.add(
    title="From the heading", par=4, ext="md", setup=OWN_FILE_ONLY, cursor=(3, 1),
    task="Replace TBD with the word from the heading, Internationalization. The cursor starts on TBD.",
    start=text("""
        ## Internationalization

        TBD is handled by the i18n module.
    """),
    target=text("""
        ## Internationalization

        Internationalization is handled by the i18n module.
    """),
    hint="cw replaces the word. With ignorecase, a lowercase i matches the capital I, and Ctrl-p looks upward "
         "first, toward the heading.",
    uses=["c"],
)
complete.add(
    title="The nearest one above", par=4, ext="py", setup=OWN_FILE_ONLY, cursor=(4, 1),
    task="Print the cache: put user_cache inside print(). The cursor starts on the last line.",
    start=text("""
        user_count = len(users)
        user_cache = {}

        print()
    """),
    target=text("""
        user_count = len(users)
        user_cache = {}

        print(user_cache)
    """),
    hint="Ctrl-n searches forward and wraps around to the top, so it finds user_count first. Ctrl-p searches "
         "backward: the nearest match above comes first.",
    uses=["line", "insert"],
)
complete.add(
    title="The middle one", par=8, ext="java", setup=OWN_FILE_ONLY, cursor=(6, 1),
    task="Print the email: the println() call should get getUserEmail() as its argument. The cursor starts "
         "on line 6.",
    start=text("""
        String getUserName() { return name; }
        String getUserEmail() { return email; }
        String getUserPhone() { return phone; }

        void printContact() {
            System.out.println();
        }
    """),
    target=text("""
        String getUserName() { return name; }
        String getUserEmail() { return email; }
        String getUserPhone() { return phone; }

        void printContact() {
            System.out.println(getUserEmail());
        }
    """),
    hint="g matches all three getters. Pressing Ctrl-p again steps to the next match, so the second press "
         "gives you the middle one.",
    uses=["f", "insert"],
)
complete.add(
    title="One more letter", par=7, ext="c", setup=OWN_FILE_ONLY, cursor=(8, 1),
    task="shutdown() should call release_buffer(buf) instead of free(buf). The cursor starts on line 8.",
    start=text("""
        void read_header(FILE *f);
        void reset_parser(void);
        void release_buffer(char *buf);
        void resize_table(int n);
        void retry_send(void);

        void shutdown(char *buf) {
            free(buf);
        }
    """),
    target=text("""
        void read_header(FILE *f);
        void reset_parser(void);
        void release_buffer(char *buf);
        void resize_table(int n);
        void retry_send(void);

        void shutdown(char *buf) {
            release_buffer(buf);
        }
    """),
    hint="re matches five names, and release_buffer is third whichever way you search. Typing one more letter, "
         "rel, leaves just one.",
    uses=["word", "c"],
)
complete.add(
    title="A capital narrows it", par=7, ext="java", setup=OWN_FILE_ONLY, cursor=(5, 1),
    task="Create a ConcurrentHashMap: new () should become new ConcurrentHashMap<>(). The cursor starts on "
         "line 5.",
    start=text("""
        import java.util.Map;
        import java.util.concurrent.ConcurrentHashMap;

        class Registry {
            private final Map<String, Handler> handlers = new ();
        }
    """),
    target=text("""
        import java.util.Map;
        import java.util.concurrent.ConcurrentHashMap;

        class Registry {
            private final Map<String, Handler> handlers = new ConcurrentHashMap<>();
        }
    """),
    hint="Lowercase c would match class and concurrent too. With smartcase, a capital letter makes completion "
         "match case exactly, and only one word starts with a capital C.",
    uses=["f", "insert"],
)
complete.add(
    title="After the arrow", par=16, ext="c", setup=OWN_FILE_ONLY, cursor=(4, 1),
    task="Finish the return statement: return c->retry_count < c->max_retries; The cursor starts on line 4.",
    start=text("""
        struct conn { int retry_count; int max_retries; };

        int should_retry(struct conn *c) {
            return
        }
    """),
    target=text("""
        struct conn { int retry_count; int max_retries; };

        int should_retry(struct conn *c) {
            return c->retry_count < c->max_retries;
        }
    """),
    hint="Completion works after -> too. Ctrl-p would find return first, since it's the nearest word before "
         "the cursor that starts with r. Ctrl-n wraps around to line 1 first.",
    uses=["insert"],
)
complete.add(
    title="Three names in one line", par=20, ext="py", setup=OWN_FILE_ONLY, cursor=(2, 1),
    task="Finish the return line: return unit_price * quantity_ordered * (1 - discount_rate). The cursor "
         "starts on line 2.",
    start=text("""
        def invoice_total(unit_price, quantity_ordered, discount_rate):
            return
    """),
    target=text("""
        def invoice_total(unit_price, quantity_ordered, discount_rate):
            return unit_price * quantity_ordered * (1 - discount_rate)
    """),
    hint="One letter and Ctrl-p for each parameter. Typing a space or a ) after a completed word just carries "
         "on: there's nothing to accept.",
    uses=["insert"],
)
complete.add(
    title="Complete, then repeat", par=21, ext="py", setup=OWN_FILE_ONLY,
    task="Pass encoding=DEFAULT_ENCODING to all three open() calls, after their first argument.",
    start=text("""
        DEFAULT_ENCODING = "utf-8"
        src = open(config_path)
        dst = open(output_path)
        log = open(log_path)
    """),
    target=text("""
        DEFAULT_ENCODING = "utf-8"
        src = open(config_path, encoding=DEFAULT_ENCODING)
        dst = open(output_path, encoding=DEFAULT_ENCODING)
        log = open(log_path, encoding=DEFAULT_ENCODING)
    """),
    hint="The completed word becomes part of the insert, so . types it again. After the first line, j lands "
         "on the ) of each shorter line below.",
    uses=["line", "insert", "dot"],
)
complete.add(
    title="Write the method", par=31, ext="java", setup=OWN_FILE_ONLY, cursor=(9, 1),
    task="Give total() a body: return subtotalBeforeTax().add(shippingCost).subtract(discountAmount); The "
         "cursor starts on total()'s line.",
    start=text("""
        class Cart {
            private BigDecimal shippingCost;
            private BigDecimal discountAmount;

            BigDecimal subtotalBeforeTax() {
                return BigDecimal.ZERO;
            }

            BigDecimal total() {
            }
        }
    """),
    target=text("""
        class Cart {
            private BigDecimal shippingCost;
            private BigDecimal discountAmount;

            BigDecimal subtotalBeforeTax() {
                return BigDecimal.ZERO;
            }

            BigDecimal total() {
                return subtotalBeforeTax().add(shippingCost).subtract(discountAmount);
            }
        }
    """),
    hint="Every name that's already in the file can be completed, return included. subtract isn't, so that "
         "one you type.",
    uses=["o"],
)
complete.add(
    title="Forward, round the end", par=5, ext="sh", setup=OWN_FILE_ONLY, cursor=(2, 1),
    task="Print the environment's name: the message should end in $DEPLOY_ENVIRONMENT, inside the quotes. The "
         "cursor starts on line 2.",
    start=text('''
        DEPLOY_ENVIRONMENT=staging
        echo "Deploying to "
    '''),
    target=text('''
        DEPLOY_ENVIRONMENT=staging
        echo "Deploying to $DEPLOY_ENVIRONMENT"
    '''),
    hint="The $ isn't part of a word, so the D after it starts one. A capital D also matches Deploying on this "
         "line, which Ctrl-p meets first. Ctrl-n searches forward and wraps around to line 1.",
    uses=["line", "insert"],
)
complete.add(
    title="Dashes are part of it", par=5, ext="css", setup=OWN_FILE_ONLY, cursor=(7, 1),
    task="Hovering should use the dark color: put --color-primary-dark inside var(). The cursor starts on line 7.",
    start=text("""
        :root {
            --color-primary: #2563eb;
            --color-primary-dark: #1d4ed8;
        }

        .btn:hover {
            background: var();
        }
    """),
    target=text("""
        :root {
            --color-primary: #2563eb;
            --color-primary-dark: #1d4ed8;
        }

        .btn:hover {
            background: var(--color-primary-dark);
        }
    """),
    hint="In CSS a dash counts as part of a word, so one completion fills in all of --color-primary-dark, dashes "
         "included. Ctrl-p finds the nearest match above first.",
    uses=["f", "insert"],
)
complete.add(
    title="From the same line", par=9, ext="js", setup=OWN_FILE_ONLY,
    task="Finish the arrow function: it should return width * height.",
    start="const area = (width, height) =>",
    target="const area = (width, height) => width * height",
    hint="Ctrl-p looks back from the cursor, and the nearest words are on this very line.",
    uses=["insert"],
)
complete.add(
    title="Backward wraps too", par=4, ext="md", setup=OWN_FILE_ONLY, cursor=(3, 28),
    task="Fill in the blank: the cache was replaced with Dragonfly. The cursor starts on TBD.",
    start=text("""
        ## Summary

        We replaced the cache with TBD and cut p99 latency in half.

        ## Details

        Memcached was slow to warm up, so we moved to Dragonfly.
    """),
    target=text("""
        ## Summary

        We replaced the cache with Dragonfly and cut p99 latency in half.

        ## Details

        Memcached was slow to warm up, so we moved to Dragonfly.
    """),
    hint="Nothing above the cursor starts with a capital D, so Ctrl-p wraps around to the end of the file and "
         "searches up from there. Ctrl-n would meet Details first.",
    uses=["c"],
)
complete.add(
    title="A dash splits it", par=8, ext="html", setup=OWN_FILE_ONLY,
    task="Connect the label to its input: for=\"\" should be for=\"billing-address\".",
    start=text('''
        <label for="">Billing address</label>
        <input id="billing-address" name="billing-address">
    '''),
    target=text('''
        <label for="billing-address">Billing address</label>
        <input id="billing-address" name="billing-address">
    '''),
    hint="In HTML a dash isn't part of a word, so complete billing, type the dash, then complete address. Ctrl-n "
         "would find the label's own Billing first.",
    uses=["f", "insert"],
)
complete.add(
    title="Complete in a block", par=9, ext="sql", setup=OWN_FILE_ONLY,
    task="Qualify the columns with their table: product_id becomes order_items.product_id, and the same for all "
         "four.",
    start=text("""
        SELECT
            product_id,
            quantity,
            unit_price,
            discount
        FROM order_items
    """),
    target=text("""
        SELECT
            order_items.product_id,
            order_items.quantity,
            order_items.unit_price,
            order_items.discount
        FROM order_items
    """),
    hint="A block insert (Ctrl-v, then I) types on every line of the block at once, and completion works while "
         "you type its first line. Going back from line 2, o and Ctrl-p wrap around to the last word in the file.",
    uses=["block-insert", "word", "count"],
)
complete.add(
    title="One letter too many", par=12, ext="py", setup=OWN_FILE_ONLY, cursor=(2, 1),
    task="Finish the loop header: for migration in migrations: The cursor starts on line 2.",
    start=text("""
        def apply_all(migrations):
            for
    """),
    target=text("""
        def apply_all(migrations):
            for migration in migrations:
    """),
    hint="Only the plural is in the file. Complete it and Ctrl-h deletes the s. For the second name, Ctrl-p would "
         "find the singular you just made, but Ctrl-n searches forward and wraps around to line 1.",
    uses=["insert", "ctrl-w"],
)
complete.add(
    title="Down the file", par=9, ext="c", setup=OWN_FILE_ONLY, cursor=(4, 1),
    task="main() should return run_tests(&opts). The cursor starts on the return line.",
    start=text("""
        int main(int argc, char **argv)
        {
            struct options opts = parse_options(argc, argv);
            return ;
        }

        static int run_tests(const struct options *o) { return test_all(o->filter); }
        static int run_benchmark(const struct options *o) { return bench(o->iterations); }
    """),
    target=text("""
        int main(int argc, char **argv)
        {
            struct options opts = parse_options(argc, argv);
            return run_tests(&opts);
        }

        static int run_tests(const struct options *o) { return test_all(o->filter); }
        static int run_benchmark(const struct options *o) { return bench(o->iterations); }
    """),
    hint="The functions come after main, so Ctrl-n, searching forward, meets run_tests first. Backward, Ctrl-p "
         "would find return on this line. opts is the other way: just above.",
    uses=["line", "insert"],
)
complete.add(
    title="Complete at every end", par=11, ext="js", setup=OWN_FILE_ONLY,
    task="Give all four timeouts the default: each line should end in = DEFAULT_REQUEST_TIMEOUT_MS;",
    start=text("""
        const DEFAULT_REQUEST_TIMEOUT_MS = 5000;

        const fetchTimeout =
        const uploadTimeout =
        const syncTimeout =
        const pingTimeout =
    """),
    target=text("""
        const DEFAULT_REQUEST_TIMEOUT_MS = 5000;

        const fetchTimeout = DEFAULT_REQUEST_TIMEOUT_MS;
        const uploadTimeout = DEFAULT_REQUEST_TIMEOUT_MS;
        const syncTimeout = DEFAULT_REQUEST_TIMEOUT_MS;
        const pingTimeout = DEFAULT_REQUEST_TIMEOUT_MS;
    """),
    hint="The lines end at different columns, but a block with $ appends at the end of each one. Complete the "
         "name on the first line, and Esc copies the whole insert to the rest.",
    uses=["block-insert", "count"],
)
complete.add(
    title="Forward is closer", par=34, ext="py", setup=OWN_FILE_ONLY,
    task="Give total() its formula: return (self.subtotal - self.discount) * (1 + self.tax_rate)",
    start=text("""
        class Invoice:
            def __init__(self, subtotal, tax_rate, discount):
                self.subtotal = subtotal
                self.tax_rate = tax_rate
                self.discount = discount

            def total(self):
                return
    """),
    target=text("""
        class Invoice:
            def __init__(self, subtotal, tax_rate, discount):
                self.subtotal = subtotal
                self.tax_rate = tax_rate
                self.discount = discount

            def total(self):
                return (self.subtotal - self.discount) * (1 + self.tax_rate)
    """),
    hint="Ctrl-p looks back from the cursor, so it keeps finding the words you've just typed, and def and total "
         "above. Ctrl-n goes forward from the end, wraps around to the top, and meets the __init__ line first.",
    uses=["gg", "insert"],
)

# ---------- Ctrl-o ----------

ctrl_o = drills.command(
    "ctrl-o", "Ctrl-o {cmd}", "one Normal command without leaving Insert",
    """In Insert mode, Ctrl-o runs one Normal-mode command, then puts you back in Insert mode wherever that
    command left the cursor. Typing carries on just before the character the command landed on: after
    Ctrl-o f) you type in front of the ), and after Ctrl-o $ you type after the last character. Compared with
    <Esc>, a command and i, it saves the key that gets you back into Insert mode, and it's handy for commands
    that don't touch the text at all, like Ctrl-o zz to scroll. It works in Replace mode too. . only repeats
    what you typed after the last Ctrl-o.""",
    examples=[("Ctrl-o $", "carry on at the end of the line"), ("Ctrl-o f)", "carry on just before the next )"),
              ("Ctrl-o Fp", "back to just before the last p"), ("Ctrl-o %", "to the matching bracket"),
              ("Ctrl-o D", "delete to the end of the line"), ("Ctrl-o zz", "scroll, and keep typing")],
)
ctrl_o.add(
    title="Inline code", par=7, ext="md", setup=OWN_FILE_ONLY,
    task="Mark npm install as code: put a backtick before npm and one after install.",
    start="Run npm install first.",
    target="Run `npm install` first.",
    hint="After the first backtick, Ctrl-o runs one motion and drops you back into Insert mode. tf stops just "
         "before the f of first, which is right after install.",
    uses=["word", "insert", "t"],
)
ctrl_o.add(
    title="Then the end", par=10, ext="java", setup=OWN_FILE_ONLY, cursor=(2, 1),
    task="Call log.info instead of log, and end the statement with a ;. The cursor starts on line 2.",
    start=text("""
        void start() {
            log("server started")
        }
    """),
    target=text("""
        void start() {
            log.info("server started");
        }
    """),
    hint="Type .info after log, then Ctrl-o $ takes you to the end of the line, still in Insert mode.",
    uses=["word", "insert", "line"],
)
ctrl_o.add(
    title="Quote a field", par=9, ext="csv", setup=OWN_FILE_ONLY,
    task="The name contains a comma, so CSV needs it in double quotes: \"Lovelace, Ada\".",
    start=text("""
        id,name,born
        7,Lovelace, Ada,1815
    """),
    target=text("""
        id,name,born
        7,"Lovelace, Ada",1815
    """),
    hint="Open the quote after the first comma. The closing one goes just before the comma that comes right "
         "before 1815: one t motion away.",
    uses=["f", "insert", "t"],
)
ctrl_o.add(
    title="Close first, open later", par=11, ext="py", setup=OWN_FILE_ONLY,
    task="Round the result: total = round(price * qty)",
    start="total = price * qty",
    target="total = round(price * qty)",
    hint="The ) goes at the end, so start with A. Then Ctrl-o and a backward F motion take you back to price, "
         "and you type round( there.",
    uses=["insert", "f"],
)
ctrl_o.add(
    title="Clamp it", par=11, ext="py", setup=OWN_FILE_ONLY,
    task="Fix the clamp: y = max(lo, min(value, hi)) * scale",
    start="y = max(lo, value, hi) * scale",
    target="y = max(lo, min(value, hi)) * scale",
    hint="Type min( in front of value. Ctrl-o f) then puts you just before the ), where the second ) goes.",
    uses=["f", "insert"],
)
ctrl_o.add(
    title="Negate the condition", par=8, ext="java", setup=OWN_FILE_ONLY,
    task="Negate the whole condition: if (!(queue.isEmpty() || closed)) {",
    start=text("""
        if (queue.isEmpty() || closed) {
            return;
        }
    """),
    target=text("""
        if (!(queue.isEmpty() || closed)) {
            return;
        }
    """),
    hint="Insert (! in front of the condition's opening parenthesis, so the cursor is still on it. Ctrl-o % "
         "then jumps to its partner, and you type the second ) there.",
    uses=["f", "insert", "percent"],
)
ctrl_o.add(
    title="Two spots in a query", par=21, ext="sql", setup=OWN_FILE_ONLY,
    task="Make the query SELECT DISTINCT name FROM active_users;",
    start="SELECT name FROM users;",
    target="SELECT DISTINCT name FROM active_users;",
    hint="After typing DISTINCT and a space, the cursor is in front of name. Ctrl-o 2w jumps two words on, to "
         "users.",
    uses=["word", "insert", "count"],
)
ctrl_o.add(
    title="Fill in the table", par=14, ext="txt", setup=OWN_FILE_ONLY,
    task="Overwrite the blanks: Name in the first cell and Age in the second, keeping the table's width.",
    start=text("""
        +------+------+
        | ____ | ____ |
        +------+------+
    """),
    target=text("""
        +------+------+
        | Name | Age  |
        +------+------+
    """),
    hint="R types over the blanks. Ctrl-o works in Replace mode too, and ; repeats the f_ you used to get to "
         "the first cell.",
    uses=["f", "replace-mode", "semicolon"],
)
ctrl_o.add(
    title="Make it a link", par=28, ext="html", setup=OWN_FILE_ONLY,
    task="Turn \"the docs\" into a link: <a href=\"/guide\">the docs</a>",
    start=text("""
        <ul>
            <li>Read the docs first</li>
        </ul>
    """),
    target=text("""
        <ul>
            <li>Read <a href="/guide">the docs</a> first</li>
        </ul>
    """),
    hint="Type the opening tag in front of the. The closing tag goes right before the space in front of first, "
         "and Ctrl-o tf gets you there.",
    uses=["f", "insert", "t"],
)
ctrl_o.add(
    title="Three edits, one insert", par=21, ext="py", setup=OWN_FILE_ONLY,
    task="Strip the name and convert count to a string: msg = name.strip() + \": \" + str(count)",
    start='msg = name + ": " + count',
    target='msg = name.strip() + ": " + str(count)',
    hint="Append after the e of name, then Ctrl-o fc and Ctrl-o $ take you to the other two spots without "
         "leaving Insert mode.",
    uses=["f", "insert", "line"],
)
ctrl_o.add(
    title="Back one WORD", par=10, ext="js", setup=OWN_FILE_ONLY,
    task="json() returns a promise: make the line const data = await response.json(); with the semicolon.",
    start="const data = response.json()",
    target="const data = await response.json();",
    hint="Add the ; with A first. Then Ctrl-o B takes you back to the start of the WORD response.json(); and "
         "you're still in Insert mode to type await there.",
    uses=["insert", "bigword"],
)
ctrl_o.add(
    title="Generics, twice", par=24, ext="java", setup=OWN_FILE_ONLY,
    task="Add the type parameters: Map<String, Integer> counts = new HashMap<>();",
    start="Map counts = new HashMap();",
    target="Map<String, Integer> counts = new HashMap<>();",
    hint="Append the first <...> right after Map, then Ctrl-o f( jumps to the parenthesis, and the <> goes in "
         "front of it.",
    uses=["word", "insert", "f"],
)
ctrl_o.add(
    title="Column and value", par=20, ext="sql", setup=OWN_FILE_ONLY,
    task="Insert a role too: INSERT INTO users (name, role) VALUES ('Ada', 'admin');",
    start="INSERT INTO users (name) VALUES ('Ada');",
    target="INSERT INTO users (name, role) VALUES ('Ada', 'admin');",
    hint="f) gets you to the first spot. ; repeats that f), even from inside Insert mode with Ctrl-o, and finds "
         "the next ) along.",
    uses=["f", "insert", "semicolon"],
)
ctrl_o.add(
    title="Keep the border", par=14, ext="txt", setup=OWN_FILE_ONLY,
    task="The build is fixed: overwrite FAILED with PASSED and the 0 tests with 42, without moving the right border.",
    start=text("""
        +--------------------------+
        | build: FAILED  tests: 0  |
        +--------------------------+
    """),
    target=text("""
        +--------------------------+
        | build: PASSED  tests: 42 |
        +--------------------------+
    """),
    hint="R types over the text, so the box keeps its width. In Replace mode, Ctrl-o f0 jumps to the 0 and drops "
         "you back into Replace mode there.",
    uses=["word", "count", "f", "replace-mode"],
)
ctrl_o.add(
    title="Two flags", par=14, ext="sh", setup=OWN_FILE_ONLY,
    task="Make curl show errors and fail on them: -s becomes -sS, and --fail goes right before the URL.",
    start="curl -s -o status.json https://api.acme.dev/v1/status",
    target="curl -sS -o status.json --fail https://api.acme.dev/v1/status",
    hint="Append the S after the s first. The URL starts with the only h on the line, so Ctrl-o fh lands right "
         "where --fail goes.",
    uses=["f", "insert"],
)
ctrl_o.add(
    title="The next match", par=34, ext="ts", setup=OWN_FILE_ONLY,
    task="Add type annotations: count: number, label: string and done: boolean, each before its =.",
    start=text("""
        let count = 0
        let label = "items"
        let done = false
    """),
    target=text("""
        let count: number = 0
        let label: string = "items"
        let done: boolean = false
    """),
    hint="Each annotation goes just before \" =\". Search for that once, and from inside Insert mode Ctrl-o n "
         "takes you to the next one.",
    uses=["search", "insert"],
)
ctrl_o.add(
    title="Lines away", par=17, ext="js", setup=OWN_FILE_ONLY,
    task="Round the total: it should be Math.round(sum(...)), with the second ) at the start of the last line.",
    start=text("""
        const total = sum(
            cart.items.map((item) => item.price * item.qty),
        );
    """),
    target=text("""
        const total = Math.round(sum(
            cart.items.map((item) => item.price * item.qty),
        ));
    """),
    hint="Type Math.round( in front of sum. The cursor is then on the s, and % from there finds the next bracket "
         "on the line and jumps to its partner, two lines down.",
    uses=["line", "word", "insert", "percent"],
)
ctrl_o.add(
    title="Name every argument", par=16, ext="py", setup=OWN_FILE_ONLY,
    task="Pass the arguments by name: client = connect(host=host, port=port, timeout=timeout)",
    start="client = connect(host, port, timeout)",
    target="client = connect(host=host, port=port, timeout=timeout)",
    hint="Start at the end, in front of the ). Each name is the word just before you, so a letter and Ctrl-p "
         "type it. Ctrl-o F, goes back a comma, and Ctrl-o ; another.",
    uses=["line", "insert", "f", "semicolon", "complete"],
)
ctrl_o.add(
    title="Format and arguments", par=25, ext="c", setup=OWN_FILE_ONLY,
    task="Print both numbers with labels: printf(\"count=%d total=%d\\n\", count, total);",
    start='printf("%d\\n", count);',
    target='printf("count=%d total=%d\\n", count, total);',
    hint="Three spots: before the %, before the \\n and before the ). count is already further along the line, "
         "so Ctrl-n completes it, and by the end, total is behind you for Ctrl-p.",
    uses=["f", "insert", "complete"],
)
ctrl_o.add(
    title="Four types in one go", par=38, ext="ts", setup=OWN_FILE_ONLY,
    task="Type the function: function connect(host: string, port: number, timeout: number): Socket {",
    start=text("""
        function connect(host, port, timeout) {
            return net.connect(host, port);
        }
    """),
    target=text("""
        function connect(host: string, port: number, timeout: number): Socket {
            return net.connect(host, port);
        }
    """),
    hint="Work from left to right in one insert: f, for the first spot, then Ctrl-o ; and Ctrl-o f) for the "
         "next two, and the second number completes from the first. Ctrl-o l steps over the ).",
    uses=["f", "insert", "semicolon", "complete"],
)

# ---------- Ctrl-t Ctrl-d ----------

ctrl_t = drills.command(
    "ctrl-t", "Ctrl-t  Ctrl-d", "indent or unindent while typing",
    """In Insert mode, Ctrl-t adds one shiftwidth of indent (4 spaces here) to the current line and Ctrl-d
    removes one, wherever the cursor is in the line, and your typing carries on where it was. Type 0 and
    then Ctrl-d to remove all the indent. Because the indent change is part of the insert, . repeats it along
    with the text. In the indent at the start of a line, Tab and Backspace do the same here (smarttab is on),
    but only there.""",
    examples=[("Ctrl-t", "one level more"), ("Ctrl-d", "one level less"), ("0 Ctrl-d", "no indent at all"),
              ("A, Ctrl-t", "add a comma and indent"), ("o Ctrl-d", "new line, one level out")],
    level="complex",
)
ctrl_t.add(
    title="After the loop", par=19, ext="py", setup=OWN_FILE_ONLY,
    task="After the loop, inside the function, add the line log.info(\"done\").",
    start=text("""
        def drain(queue):
            while queue:
                item = queue.pop()
                handle(item)
    """),
    target=text("""
        def drain(queue):
            while queue:
                item = queue.pop()
                handle(item)
            log.info("done")
    """),
    hint="o starts the new line at the loop body's indent. Ctrl-d takes it back one level (Ctrl-u would take "
         "away all of it).",
    uses=["gg", "o"],
)
ctrl_t.add(
    title="Nest the list", par=10, ext="md", setup=OWN_FILE_ONLY,
    task="Turn apples, pears and plums into list items nested under Fruit: \"    - apples\" and so on.",
    start=text("""
        - Fruit
        apples
        pears
        plums
        - Vegetables
    """),
    target=text("""
        - Fruit
            - apples
            - pears
            - plums
        - Vegetables
    """),
    hint="I types the \"- \", and Ctrl-t indents the line from where you are. Both are one insert, so . does "
         "both on the next line.",
    uses=["insert", "dot"],
)
ctrl_t.add(
    title="An outline in one go", par=36, ext="md", setup=OWN_FILE_ONLY,
    task="Below the heading, write the outline: - Install, with - macOS and - Linux nested under it, then "
         "- Usage at the top level again.",
    start="## Plan",
    target=text("""
        ## Plan
        - Install
            - macOS
            - Linux
        - Usage
    """),
    hint="Each <CR> keeps the indent of the line before. Ctrl-t steps in a level for the nested items, and "
         "Ctrl-d steps back out.",
    uses=["o"],
)
ctrl_t.add(
    title="Indent from the end", par=9, ext="py", setup=OWN_FILE_ONLY,
    task="The tax line belongs inside the if, and it should apply the rate: total += order.tax * rate, one level "
         "deeper.",
    start=text("""
        def charge(order, rate):
            total = order.subtotal
            if order.taxable:
            total += order.tax
            return total
    """),
    target=text("""
        def charge(order, rate):
            total = order.subtotal
            if order.taxable:
                total += order.tax * rate
            return total
    """),
    hint="You're typing at the end of the line anyway, and Ctrl-t indents it from there, without leaving Insert "
         "mode. rate is already in the file.",
    uses=["count", "insert", "complete"],
)
ctrl_t.add(
    title="Out of the loop", par=9, ext="py", setup=OWN_FILE_ONLY,
    task="find() gives up too early: the last line belongs after the loop, one level out, and it should return "
         "None instead of -1.",
    start=text("""
        def find(items, target):
            for i, item in enumerate(items):
                if item == target:
                    return i
                return -1
    """),
    target=text("""
        def find(items, target):
            for i, item in enumerate(items):
                if item == target:
                    return i
            return None
    """),
    hint="Retype the end of the line, and before you leave Insert mode, Ctrl-d takes the line out one level.",
    uses=["gg", "insert", "ctrl-w"],
)
ctrl_t.add(
    title="One per line", par=15, ext="toml", setup=OWN_FILE_ONLY,
    task="Spread the dependencies out, one per line and indented, with a comma after each and the ] on a line of "
         "its own.",
    start=text("""
        [project]
        name = "acme"
        dependencies = ["requests", "rich"]
    """),
    target=text("""
        [project]
        name = "acme"
        dependencies = [
            "requests",
            "rich",
        ]
    """),
    hint="A new line keeps the indent of the line before it. Ctrl-t indents the first item, the second follows "
         "along, and Ctrl-d brings the ] back out.",
    uses=["bigword", "count", "insert", "f", "r"],
)

# ---------- Ctrl-x Ctrl-l ----------

line_complete = drills.command(
    "line-complete", "Ctrl-x Ctrl-l", "complete a whole line",
    """In Insert mode, Ctrl-x Ctrl-l completes a whole line: type the start of a line that's somewhere else
    in the file (never mind its indent) and Vim fills in the rest. Your line keeps its own indent. It
    searches backward, so the nearest matching line above comes first; Ctrl-p (or Ctrl-l again) steps to the
    ones further back, Ctrl-n forward again. Press Ctrl-x Ctrl-l again right after a match and it adds the
    line that came after that match, so you can copy several lines in a row. Then keep typing to change what's
    different.""",
    examples=[("in Ctrl-x Ctrl-l", "the nearest line that starts with in"), ("Ctrl-p", "a matching line further up"),
              ("Ctrl-x Ctrl-l Ctrl-x Ctrl-l", "that line and the one after it")],
    level="complex",
)
line_complete.add(
    title="The same decorator", par=4, ext="py", setup=OWN_FILE_ONLY, cursor=(6, 1),
    task="Retry fetch_order() the same way as fetch_user(): give it the same @retry line. The cursor starts "
         "on its def line.",
    start=text("""
        @retry(attempts=3, backoff=2.0)
        def fetch_user(uid):
            return api.get(f"/users/{uid}")


        def fetch_order(oid):
            return api.get(f"/orders/{oid}")
    """),
    target=text("""
        @retry(attempts=3, backoff=2.0)
        def fetch_user(uid):
            return api.get(f"/users/{uid}")


        @retry(attempts=3, backoff=2.0)
        def fetch_order(oid):
            return api.get(f"/orders/{oid}")
    """),
    hint="Open a line above and type just the @. It's the only line that starts that way, so Ctrl-x Ctrl-l "
         "finds it.",
    uses=["o"],
)
line_complete.add(
    title="The older prototype", par=34, ext="c", setup=OWN_FILE_ONLY,
    task="Implement buffer_init at the end of the file: after a blank line, its prototype with { instead of ;, "
         "then the body b->cap = n; and return 0;, then }.",
    start=text("""
        #include "buffer.h"

        int buffer_init(struct buffer *b, size_t n);
        int buffer_len(const struct buffer *b);
        /* implementations */
    """),
    target=text("""
        #include "buffer.h"

        int buffer_init(struct buffer *b, size_t n);
        int buffer_len(const struct buffer *b);
        /* implementations */

        int buffer_init(struct buffer *b, size_t n) {
            b->cap = n;
            return 0;
        }
    """),
    hint="Both prototypes start with i, and buffer_len is the nearer one. Ctrl-p steps to the next match up. "
         "Then Ctrl-h deletes the ; and you keep typing.",
    uses=["gg", "o", "ctrl-w"],
)
line_complete.add(
    title="Two lines into a block", par=43, ext="py", setup=OWN_FILE_ONLY,
    task="Write test_incomplete()'s body: with pytest.raises(ValueError): and, inside it, the two lines from "
         "test_parse(), but parsing \"1 + \" instead of \"1 + 2\".",
    start=text("""
        def test_parse():
            parser = Parser(strict=True)
            tree = parser.parse("1 + 2")
            assert tree.value == 3


        def test_incomplete():
    """),
    target=text("""
        def test_parse():
            parser = Parser(strict=True)
            tree = parser.parse("1 + 2")
            assert tree.value == 3


        def test_incomplete():
            with pytest.raises(ValueError):
                parser = Parser(strict=True)
                tree = parser.parse("1 + ")
    """),
    hint="Line completion keeps the indent you're at, here the with block's. A second Ctrl-x Ctrl-l adds the "
         "line that followed. Then Ctrl-w fixes the end.",
    uses=["gg", "o", "ctrl-w"],
)
line_complete.add(
    title="The same filter", par=4, ext="sql", setup=OWN_FILE_ONLY, cursor=(4, 1),
    task="The second query should count the same orders: give it the first query's WHERE line, below its FROM. "
         "The cursor starts on that line.",
    start=text("""
        SELECT count(*) FROM orders
        WHERE status = 'paid' AND created_at >= '2024-01-01';

        SELECT sum(total) FROM orders
    """),
    target=text("""
        SELECT count(*) FROM orders
        WHERE status = 'paid' AND created_at >= '2024-01-01';

        SELECT sum(total) FROM orders
        WHERE status = 'paid' AND created_at >= '2024-01-01';
    """),
    hint="Only one line in the file starts with W, so on a new line, W and Ctrl-x Ctrl-l type all of it.",
    uses=["o"],
)
line_complete.add(
    title="Setup from the other test", par=12, ext="py", setup=OWN_FILE_ONLY,
    task="test_empty() needs the same cart as test_total(), then an assert that its total is 0: write its body as "
         "the cart = line from test_total() and assert cart.total() == 0.",
    start=text('''
        import pytest

        from shop.cart import Cart


        def test_total():
            """One item, priced in euros."""
            cart = Cart(currency="EUR")
            cart.add("tea", 450)
            assert cart.total() == 450


        def test_empty():
    '''),
    target=text('''
        import pytest

        from shop.cart import Cart


        def test_total():
            """One item, priced in euros."""
            cart = Cart(currency="EUR")
            cart.add("tea", 450)
            assert cart.total() == 450


        def test_empty():
            cart = Cart(currency="EUR")
            assert cart.total() == 0
    '''),
    hint="Both cart lines start with c, and the nearest one up is cart.add: Ctrl-p steps to the one before it. "
         "The assert is a whole line too, with only its number to change.",
    uses=["gg", "o", "ctrl-w"],
)
# When a line completion ends, C indenting re-indents the line while it's still a header without its ;, and
# takes it for an old-style (K&R) definition. The drill turns that off: nothing else in it is indented.
line_complete.add(
    title="Prototypes from below", par=14, ext="c", setup=OWN_FILE_ONLY + ["setlocal nocindent"],
    task="main() uses two functions that are defined after it. Declare them above main, below the #include and its "
         "blank line: each one's first line, ending in ; instead, in the order they're defined, with a blank line "
         "before main.",
    start=text("""
        #include <stdio.h>

        int main(void)
        {
            char buf[512];
            int fd = accept_client();
            if (parse_request(buf, read(fd, buf, sizeof buf)))
                return 1;
            return 0;
        }

        static int parse_request(char *buf, size_t len)
        {
            return len > 4 && buf[0] == 'G';
        }

        static void send_response(int fd, int status)
        {
            dprintf(fd, "HTTP/1.1 %d\\r\\n\\r\\n", status);
        }
    """),
    target=text("""
        #include <stdio.h>

        static int parse_request(char *buf, size_t len);
        static void send_response(int fd, int status);

        int main(void)
        {
            char buf[512];
            int fd = accept_client();
            if (parse_request(buf, read(fd, buf, sizeof buf)))
                return 1;
            return 0;
        }

        static int parse_request(char *buf, size_t len)
        {
            return len > 4 && buf[0] == 'G';
        }

        static void send_response(int fd, int status)
        {
            dprintf(fd, "HTTP/1.1 %d\\r\\n\\r\\n", status);
        }
    """),
    hint="Nothing above starts with s, so the backward search wraps around to the end of the file and works up "
         "from there: the later function comes first. For the second line, your new prototype is the nearest "
         "match.",
    uses=["o"],
)

# ---------- Ctrl-k ----------

digraph = drills.command(
    "digraph", "Ctrl-k {a}{b}", "type special characters",
    """Ctrl-k followed by two characters types a digraph: a special character with an easy-to-guess
    two-character name. An accent goes after its letter (e' é, e! è, e> ê, e: ë), arrows are drawn (-> →,
    <- ←), DG is the degree sign °, and box-drawing pieces are named after the directions their lines go:
    hh ─, vv │, dr ┌, dl ┐, ur └, ul ┘, vr ├, vh ┼. Digraphs work in Insert mode, on the command line, and
    after r, f and t. :digraphs lists them all.""",
    examples=[("Ctrl-k e'", "é"), ("Ctrl-k ->", "→"), ("Ctrl-k DG", "°"), ("Ctrl-k hh", "─"),
              ("r Ctrl-k dr", "replace a character with ┌"), ("Ctrl-k vh", "┼")],
    level="complex",
)
digraph.add(
    title="Café accents", par=11, ext="md", setup=OWN_FILE_ONLY,
    task="Add the accents: Café Zoë.",
    start="# Cafe Zoe",
    target="# Café Zoë",
    hint="r takes a digraph too: r Ctrl-k e' replaces a character with é. For ë, the accent mark is a colon.",
    uses=["f", "r", "line"],
)
digraph.add(
    title="Degrees and an arrow", par=16, ext="txt", setup=OWN_FILE_ONLY,
    task="Write the temperatures with degree signs and use a real arrow: 18°C → 22°C.",
    start="Fermentation: 18C -> 22C",
    target="Fermentation: 18°C → 22°C",
    hint="DG is the degree sign. Insert it before the first C, and . puts another before the C at the end. "
         "Then 2s replaces -> with the digraph of the same name.",
    uses=["f", "insert", "line", "dot", "c"],
)
digraph.add(
    title="A file tree", par=20, ext="txt", setup=OWN_FILE_ONLY,
    task="Draw the tree: main.c gets \"├── \" in front, and util.c, the last one, gets \"└── \".",
    start=text("""
        src
        main.c
        util.c
    """),
    target=text("""
        src
        ├── main.c
        └── util.c
    """),
    hint="├ has lines going vertical and right (vr), ─ is hh, └ goes up and right (ur). Type the first prefix, "
         "repeat it with . on the last line, then fix its first character with r.",
    uses=["insert", "plus", "dot", "line", "r"],
)
digraph.add(
    title="Real math signs", par=17, ext="md", setup=OWN_FILE_ONLY,
    task="Use real symbols in the precondition: Requires 0 ≤ x ≤ 10 and x ≠ 5.",
    start="Requires 0 <= x <= 10 and x != 5.",
    target="Requires 0 ≤ x ≤ 10 and x ≠ 5.",
    hint="Each sign replaces two characters, so 2s and a digraph: ≤ is =< and ≠ is !=. The second ≤ is the same "
         "change again, one ; away.",
    uses=["f", "c", "semicolon", "dot"],
)
digraph.add(
    title="Three names", par=18, ext="csv", setup=OWN_FILE_ONLY,
    task="Put the accents back: François Müller, São Paulo.",
    start="Francois Muller,Sao Paulo,BR",
    target="François Müller,São Paulo,BR",
    hint="r takes a digraph: the accent goes after the letter. A cedilla is a comma (c,), an umlaut a colon (u:), "
         "and a tilde a question mark (a?).",
    uses=["f", "r"],
)
digraph.add(
    title="A box around it", par=26, ext="txt", setup=OWN_FILE_ONLY,
    task="Close the box: add a top line ┌────────┐ above and a bottom line └────────┘ below, eight ─ in each.",
    start="│ deploy │",
    target=text("""
        ┌────────┐
        │ deploy │
        └────────┘
    """),
    hint="Type just the corners of both lines first: dr and dl on top, ur and ul below. Then a count of 8 fills "
         "one line with ─ (hh), and . fills the other.",
    uses=["o", "count", "insert", "dot"],
)

# ---------- Ctrl-v ----------

literal = drills.command(
    "literal", "Ctrl-v {key}", "type a key literally",
    """Ctrl-v inserts the next key as a character instead of letting it do its usual job. Ctrl-v Tab is a
    real tab character even though expandtab turns Tab into spaces (TSV files need real tabs), and Ctrl-v Esc
    puts an actual Escape character in the text. Ctrl-v u and four hex digits types any Unicode character by
    its code, like Ctrl-v u2550 for ═, which has no digraph (use U and up to eight digits above FFFF), and
    Ctrl-v 065 types A by its decimal code. It works in Insert mode, on the command line and after r.""",
    examples=[("Ctrl-v Tab", "a real tab"), ("Ctrl-v u2550", "═, by its code"), ("Ctrl-v 065", "A, in decimal"),
              ("r Ctrl-v Tab", "replace a character with a tab"), ("Ctrl-v Esc", "an Escape character")],
    level="complex",
)
literal.add(
    title="A new column", par=23, ext="tsv", setup=OWN_FILE_ONLY,
    task="Add a typing column, separated by a real tab like the others: typing in the header, static for "
         "both C and Go.",
    start=text("""
        language\tyear
        C\t1972
        Go\t2009
    """),
    target=text("""
        language\tyear\ttyping
        C\t1972\tstatic
        Go\t2009\tstatic
    """),
    hint="expandtab is on, so Tab types spaces. Ctrl-v Tab types a real tab, and . repeats it along with the "
         "rest of the insert.",
    uses=["insert", "dot"],
)
literal.add(
    title="A double-line lid", par=23, ext="txt", setup=OWN_FILE_ONLY,
    task="Put a double-line top on the label: ╔, seven ═, then ╗.",
    start="║ SAVED ║",
    target=text("""
        ╔═══════╗
        ║ SAVED ║
    """),
    hint="These have no digraphs, but Ctrl-v u types any character by its hex code: ╔ is 2554, ═ 2550 and "
         "╗ 2557. Type both corners first, then a count fills in the middle.",
    uses=["o", "count", "insert"],
)
literal.add(
    title="Double underlines", par=15, ext="txt", setup=OWN_FILE_ONLY,
    task="Turn every = in the underlines into ═.",
    start=text("""
        Install
        =======
        Run the installer.

        Configure
        =========
        Copy the example config.

        Use
        ===
        Open a file.

        Update
        ======
        Pull the new release.
    """),
    target=text("""
        Install
        ═══════
        Run the installer.

        Configure
        ═════════
        Copy the example config.

        Use
        ═══
        Open a file.

        Update
        ══════
        Pull the new release.
    """),
    hint="One :s for the whole file. Ctrl-v works on the command line too: Ctrl-v u2550 types the ═ in the "
         "replacement.",
    uses=["subst", "range"],
)
literal.add(
    title="Tabs in the header", par=7, ext="tsv", setup=OWN_FILE_ONLY,
    task="The rows are tab-separated but the header uses spaces: make both gaps in the header real tabs.",
    start=text("""
        name city country
        Ada\tLondon\tUK
        Grace\tNew York\tUS
    """),
    target=text("""
        name\tcity\tcountry
        Ada\tLondon\tUK
        Grace\tNew York\tUS
    """),
    hint="r replaces one character, and after r, Ctrl-v Tab gives a real tab instead of spaces. ; finds the next "
         "space, and . repeats the r.",
    uses=["f", "r", "semicolon", "dot"],
)
literal.add(
    title="Escape codes", par=7, ext="txt", setup=OWN_FILE_ONLY,
    task="The login banner's color codes are missing their Escape characters: put a real Escape in front of each "
         "[ (Neovim shows it as ^[).",
    start="[1;32mWelcome to web1[0m",
    target="\x1b[1;32mWelcome to web1\x1b[0m",
    hint="Ctrl-v Esc inserts an Escape character instead of leaving Insert mode, and the next Esc leaves. Then "
         ". puts one in front of the other [.",
    uses=["insert", "word", "count", "dot"],
)
literal.add(
    title="Round the corners", par=31, ext="txt", setup=OWN_FILE_ONLY,
    task="Give the box rounded corners: ╭ ╮ on top and ╰ ╯ at the bottom. Their codes are 256d, 256e, 2570 and "
         "256f.",
    start=text("""
        ┌──────┐
        │ done │
        └──────┘
    """),
    target=text("""
        ╭──────╮
        │ done │
        ╰──────╯
    """),
    hint="Rounded corners have no digraphs, but after r, Ctrl-v u and four hex digits type any character. G keeps "
         "the column, so from the top-right corner it lands on the bottom-right one.",
    uses=["r", "line", "gg"],
)

# ---------- q: ----------

cmdwin = drills.command(
    "cmdwin", "q:", "edit command lines in a window",
    """q: opens the command-line window: your command history, one command per line, as ordinary text. Move
    and edit with any Normal and Insert mode keys, then press <CR> to run the line under the cursor in the
    window you came from. The cursor starts on the empty line at the bottom, so k gets you your most recent
    command and 3k the one three back. It's the comfortable way to rerun a long command with a change in the
    middle. :q closes it without running anything, q/ does the same for your searches, and Ctrl-f opens it from
    a half-typed command line.""",
    examples=[("q:", "open the command-line window"), ("q: k", "up to your last command"),
              ("<CR>", "run the line under the cursor"), ("q/", "the same for searches"),
              ("Ctrl-f", "from the command line")],
    level="complex",
)
cmdwin.add(
    title="A different base", par=8, ext="css",
    setup=OWN_BUFFER_ONLY + [r"""call histadd(':', '%s#\v(\d+)px#\=printf(''%grem'', submatch(1) / 16.0)#g')"""],
    task="Convert the px sizes to rem for a 10px base, so 32px becomes 3.2rem. Your command history has the :s "
         "that does it for a 16px base.",
    start=text("""
        h1 { font-size: 32px; }
        p { margin: 12px 0; }
        .note { padding: 8px 24px; }
    """),
    target=text("""
        h1 { font-size: 3.2rem; }
        p { margin: 1.2rem 0; }
        .note { padding: 0.8rem 2.4rem; }
    """),
    hint="Retyping that :s is a lot of keys. q: shows your history as text: go up to the command, change the "
         "16 into 10, and press <CR> to run it.",
    uses=["f", "r"],
)
cmdwin.add(
    title="Same again, different colors", par=48, ext="css", setup=OWN_BUFFER_ONLY,
    task="Replace #222 with var(--text-strong) and #888 with var(--text-muted).",
    start=text("""
        h1 { color: #222; }
        p { color: #222; }
        small { color: #888; }
        .hint { color: #888; }
    """),
    target=text("""
        h1 { color: var(--text-strong); }
        p { color: var(--text-strong); }
        small { color: var(--text-muted); }
        .hint { color: var(--text-muted); }
    """),
    hint="Type the first :s in full. The second differs only in the middle: open q:, change 222 to 888 and "
         "strong to muted, and run it.",
    uses=["subst", "range", "f", "r", "c"],
)
cmdwin.add(
    title="Three commands back", par=13, ext="java",
    setup=OWN_BUFFER_ONLY + [r"call histadd(':', '%s/System\.out\.println(/log(/')",
                           r"call histadd(':', '%s/\s\+$//e')", "call histadd(':', 'nohlsearch')"],
    task="Three commands back in your history is the :s that turned System.out.println( into log(. Do the "
         "same for System.err.println(.",
    start=text("""
        static void check(Config c) {
            if (c.port() < 1024) {
                System.err.println("port too low: " + c.port());
            }
            if (c.host().isEmpty()) {
                System.err.println("host missing");
            }
        }
    """),
    target=text("""
        static void check(Config c) {
            if (c.port() < 1024) {
                log("port too low: " + c.port());
            }
            if (c.host().isEmpty()) {
                log("host missing");
            }
        }
    """),
    hint="In the q: window, older commands are further up: 3k reaches the third one back. Change out to err "
         "there and press <CR>.",
    uses=["count", "f", "c"],
)
cmdwin.add(
    title="Single quotes this time", par=10, ext="js",
    setup=OWN_BUFFER_ONLY + ["call histadd(':', 'set nowrap')", r"""call histadd(':', '%s/\v"(\w+)":/\1:/g')"""],
    task="Unquote the keys: 'host': becomes host: and so on. Your last command did that to a file whose keys "
         "were in double quotes.",
    start=text("""
        const config = {
            'host': 'db.internal',
            'port': 5432,
            'ssl': true,
        };
    """),
    target=text("""
        const config = {
            host: 'db.internal',
            port: 5432,
            ssl: true,
        };
    """),
    hint="In the q: window the command is ordinary text: f\" and r' fix the first quote, and ; with . fix the "
         "second. Then <CR> runs it.",
    uses=["f", "r", "semicolon", "dot"],
)
cmdwin.add(
    title="The negative asserts", par=15, ext="py",
    setup=OWN_BUFFER_ONLY + [r"call histadd(':', '%s/\vself\.assertEquals\((.*), (.*)\)/assert \1 == \2/')"],
    task="Your last command turned self.assertEquals(a, b) into assert a == b. Do the same for the "
         "assertNotEquals calls, with != instead of ==.",
    start=text("""
        import unittest


        class TestCart(unittest.TestCase):
            def test_total(self):
                cart = make_cart()
                assert cart.total() == 900
                self.assertNotEquals(cart.total(), 0)
                self.assertNotEquals(cart.items, [])
    """),
    target=text("""
        import unittest


        class TestCart(unittest.TestCase):
            def test_total(self):
                cart = make_cart()
                assert cart.total() == 900
                assert cart.total() != 0
                assert cart.items != []
    """),
    hint="Two small edits in the middle of a long command: Not goes in front of Equals (the only capital E), and "
         "the first = becomes a !.",
    uses=["f", "insert", "r"],
)
cmdwin.add(
    title="A typo in the history", par=8, ext="java",
    setup=OWN_BUFFER_ONLY + [r"call histadd(':', '%s/\v<(get|set)Lenght>/\1Size/g')"],
    task="Rename getLength and setLength to getSize and setSize. Your last command was meant to do that, but it "
         "has a typo.",
    start=text("""
        class Buffer {
            private int length;

            int getLength() { return length; }
            void setLength(int n) { length = n; }
        }
    """),
    target=text("""
        class Buffer {
            private int length;

            int getSize() { return length; }
            void setSize(int n) { length = n; }
        }
    """),
    hint="Lenght should be Length: the h and the t are swapped. In the q: window, xp swaps two letters.",
    uses=["f", "x", "p"],
)

# ---------- @: ----------

at_colon = drills.command(
    "at-colon", "@:", "repeat the last Ex command",
    """@: repeats the last command line exactly as you typed it, range included. After that, @@ repeats it
    again (@@ repeats whichever register you ran last, and : counts as one), and a count runs it several
    times, like 3@:. A relative range such as .,.+1 is measured from wherever the cursor is now, so you can
    run a command on one block, move, and rerun it on the next. . never repeats Ex commands, and & only
    repeats a :s; @: repeats any of them.""",
    examples=[("@:", "repeat the last command line"), ("@@", "and again"), ("3@:", "three more times"),
              ("5j@:", "move down, then repeat")],
    level="complex",
)
at_colon.add(
    title="Center the title and footer", par=9, ext="txt", setup=OWN_FILE_ONLY,
    task="Center the first and the last line in 40 columns (:center 40). Leave the lines in between alone.",
    start=text("""
        SUMMER FAIR

        Saturday 12 July, 10:00 to 16:00
        Live music, food and games for all ages

        Free entry
    """),
    target=text("""
                      SUMMER FAIR

        Saturday 12 July, 10:00 to 16:00
        Live music, food and games for all ages

                       Free entry
    """),
    hint=":ce40 centers the cursor line in 40 columns. Then go to the last line and repeat it with @:.",
    uses=["gg"],
)
at_colon.add(
    title="Two of three functions", par=23, ext="c", setup=OWN_FILE_ONLY,
    task="area() and perimeter() should use double instead of float everywhere. half() keeps float.",
    start=text("""
        float area(float w, float h) {
            float a = w * h;
            return a;
        }

        float half(float x) {
            return x / 2;
        }

        float perimeter(float w, float h) {
            float p = 2 * (w + h);
            return p;
        }
    """),
    target=text("""
        double area(double w, double h) {
            double a = w * h;
            return a;
        }

        float half(float x) {
            return x / 2;
        }

        double perimeter(double w, double h) {
            double p = 2 * (w + h);
            return p;
        }
    """),
    hint="2: fills in the range .,.+1, the cursor line and the next. After the :s, move to perimeter(): @: "
         "repeats the range too, measured from the new line.",
    uses=["subst", "range", "count"],
)
at_colon.add(
    title="Right-align the authors", par=14, ext="txt", setup=OWN_FILE_ONLY,
    task="Right-align each author's name to column 50 (:right 50). The quotes stay as they are.",
    start=text("""
        Premature optimization is the root of all evil.
        Donald Knuth

        Simplicity is prerequisite for reliability.
        Edsger Dijkstra

        Talk is cheap. Show me the code
        Linus Torvalds
    """),
    target=text("""
        Premature optimization is the root of all evil.
                                              Donald Knuth

        Simplicity is prerequisite for reliability.
                                           Edsger Dijkstra

        Talk is cheap. Show me the code
                                            Linus Torvalds
    """),
    hint=":ri50 on the first name, then @: on the second. After that, @@ repeats it once more, one key "
         "shorter.",
    uses=["count", "gg"],
)
at_colon.add(
    title="Two comments, not the code", par=15, ext="c", setup=OWN_FILE_ONLY,
    task="Squeeze the runs of spaces in the two comments down to one space each. The aligned fields must keep "
         "their spacing.",
    start=text("""
        // Config  holds the   server settings.
        struct config {
            char    *host;
            int     port;
        };

        // Client  talks to   the API.
        struct client {
            char    *base_url;
            int     timeout_ms;
        };
    """),
    target=text("""
        // Config holds the server settings.
        struct config {
            char    *host;
            int     port;
        };

        // Client talks to the API.
        struct client {
            char    *base_url;
            int     timeout_ms;
        };
    """),
    hint=":s/ \\+/ /g turns every run of spaces on the line into one. & would repeat it without the g, so only "
         "the first run; @: repeats the whole command line, flags and all.",
    uses=["subst", "count"],
)
at_colon.add(
    title="The top row only", par=13, ext="txt", setup=OWN_FILE_ONLY,
    task="Make the client and server boxes double-bordered: every - on their top and bottom lines becomes =. The "
         "arrow and the db box stay as they are.",
    start=text("""
        +--------+     +--------+
        | client | --> | server |
        +--------+     +--------+
                           |
                       +--------+
                       |   db   |
                       +--------+
    """),
    target=text("""
        +========+     +========+
        | client | --> | server |
        +========+     +========+
                           |
                       +--------+
                       |   db   |
                       +--------+
    """),
    hint="A range from line 1 to 3 would change the arrow too. Do line 1 with :s and the g flag, then repeat the "
         "whole command on line 3.",
    uses=["subst", "count"],
)
at_colon.add(
    title="Two lines at a time", par=12, ext="md", setup=OWN_FILE_ONLY,
    task="Line up the misindented items under Fruit and Vegetables at 4 spaces (:left 4). baby carrots is "
         "already right, at 8.",
    start=text("""
        ## Shopping
        - Fruit
           - apples
          - pears
        - Vegetables
             - leeks
         - carrots
                - baby carrots
        - Bread
    """),
    target=text("""
        ## Shopping
        - Fruit
            - apples
            - pears
        - Vegetables
            - leeks
            - carrots
                - baby carrots
        - Bread
    """),
    hint="Their indents are all different, so >> can't fix them, but :le4 sets the indent to exactly 4. 2: types "
         "the range .,.+1 for you, and @: repeats the range too, counted from the line the cursor is on.",
    uses=["count", "range", "center"],
)

# ---------- Ctrl-a (Insert) ----------

ctrl_a_insert = drills.command(
    "ctrl-a-insert", "Ctrl-a (Insert)", "type the last insert again",
    """In Insert mode, Ctrl-a types the text from your previous Insert-mode session again, exactly as you
    typed it, spaces included. It's handy when you need the same name or path again in a different kind of
    insert (an o, an A, a ci() where . can't help. Ctrl-r . does the same in two keys (. is the register that
    holds the last inserted text), and Ctrl-@ inserts it and leaves Insert mode.""",
    examples=[("Ctrl-a", "type the last insert again"), ("Ctrl-r .", "the same, from the . register"),
              ("Ctrl-@", "insert it and leave Insert mode")],
    level="complex",
)
ctrl_a_insert.add(
    title="Make it, then go there", par=24, ext="sh", setup=OWN_FILE_ONLY,
    task="Finish the line: mkdir -p build/release && cd build/release",
    start="mkdir -p",
    target="mkdir -p build/release && cd build/release",
    hint="Type \" build/release\" in one insert and leave it. A second A, and Ctrl-a types \" build/release\" "
         "again, leading space and all.",
    uses=["insert"],
)
ctrl_a_insert.add(
    title="Field and constructor", par=36, ext="java", setup=OWN_FILE_ONLY,
    task="Name the field and the parameter maxConnections, and assign it in the constructor: "
         "this.maxConnections = maxConnections;",
    start=text("""
        class Pool {
            private final int ;

            Pool(int ) {
            }
        }
    """),
    target=text("""
        class Pool {
            private final int maxConnections;

            Pool(int maxConnections) {
                this.maxConnections = maxConnections;
            }
        }
    """),
    hint="Type the name once. . puts it in the parameter list, and in the constructor's new line Ctrl-a types "
         "it twice more.",
    uses=["f", "insert", "dot", "o"],
)
ctrl_a_insert.add(
    title="An include guard", par=29, ext="c", setup=OWN_FILE_ONLY,
    task="Name the include guard CONFIG_PARSER_H on all three lines: #ifndef CONFIG_PARSER_H, "
         "#define CONFIG_PARSER_H and #endif /* CONFIG_PARSER_H */.",
    start=text("""
        #ifndef
        #define

        int parse(const char *src);

        #endif
    """),
    target=text("""
        #ifndef CONFIG_PARSER_H
        #define CONFIG_PARSER_H

        int parse(const char *src);

        #endif /* CONFIG_PARSER_H */
    """),
    hint=". repeats the name on #define. The #endif needs it inside a comment, a different insert, so there "
         "Ctrl-a types it again.",
    uses=["insert", "dot", "gg"],
)
ctrl_a_insert.add(
    title="Three times in one header", par=32, ext="c", setup=OWN_FILE_ONLY,
    task="Finish the loop header: for (size_t chunk = 0; chunk < chunk_count; chunk++) {",
    start=text("""
        size_t chunk_count = len / CHUNK_SIZE;
        for (size_t
    """),
    target=text("""
        size_t chunk_count = len / CHUNK_SIZE;
        for (size_t chunk = 0; chunk < chunk_count; chunk++) {
    """),
    hint="Type \" chunk\" on its own and leave Insert mode. In the next insert, each Ctrl-a types \" chunk\" again, "
         "space and all, and chunk_count is just Ctrl-a and _count.",
    uses=["insert"],
)
ctrl_a_insert.add(
    title="A footnote", par=50, ext="md", setup=OWN_FILE_ONLY,
    task="Back up the claim with a footnote: put [^cache-bench] at the end of the sentence, and at the end of the "
         "file, after a blank line, the note [^cache-bench]: Measured on a 2023 laptop.",
    start=text("""
        # Caching

        The new cache halves the page load time.

        ## Notes
    """),
    target=text("""
        # Caching

        The new cache halves the page load time.[^cache-bench]

        ## Notes

        [^cache-bench]: Measured on a 2023 laptop.
    """),
    hint="The marker is the whole of the first insert, so in the second one, at the end of the file, Ctrl-a "
         "types it again.",
    uses=["count", "insert", "gg", "o"],
)
ctrl_a_insert.add(
    title="Tag and push", par=47, ext="sh", setup=OWN_FILE_ONLY,
    task="Finish the line: git tag -a v2.4.0-rc1 -m \"Release v2.4.0-rc1\" && git push origin v2.4.0-rc1",
    start="git tag -a",
    target='git tag -a v2.4.0-rc1 -m "Release v2.4.0-rc1" && git push origin v2.4.0-rc1',
    hint="Type \" v2.4.0-rc1\" in an insert of its own. In the second insert, Ctrl-a types it twice more, the space "
         "in front included, inside the quotes and at the end. git is already on the line.",
    uses=["insert", "complete"],
)

# ---------- Ctrl-b Ctrl-e Ctrl-p Ctrl-n ----------

cmdline_keys = drills.command(
    "cmdline-keys", "Ctrl-b  Ctrl-e  Ctrl-p  Ctrl-n", "edit and recall command lines",
    """On the command line, Ctrl-b jumps to the start of what you've typed and Ctrl-e to the end. Ctrl-p
    replaces the line with the previous command from your history and Ctrl-n with the next one, so : then
    Ctrl-p brings back your last command, ready to edit and run again. (Up and Down do the same, but only
    recall commands that start with what you've already typed.) Ctrl-w, Ctrl-u and Ctrl-h delete as in Insert
    mode, and searches (/ and ?) have their own history with the same keys.""",
    examples=[(": Ctrl-p", "your last command, ready to edit"), ("Ctrl-p Ctrl-p", "the one before it"),
              ("Ctrl-b 5,9", "type a range at the start"), ("Ctrl-e", "back to the end"),
              ("Ctrl-w", "delete the last word")],
    level="complex",
)
cmdline_keys.add(
    title="Same :s, different tag", par=47, ext="md", setup=OWN_FILE_ONLY,
    task="Write the names last name first and tag them: \"Lovelace, Ada (staff)\" for staff, "
         "\"Hopper, Grace (guest)\" for guests.",
    start=text("""
        ## Staff
        Ada Lovelace
        Alan Turing

        ## Guests
        Grace Hopper
        Ken Thompson
    """),
    target=text("""
        ## Staff
        Lovelace, Ada (staff)
        Turing, Alan (staff)

        ## Guests
        Hopper, Grace (guest)
        Thompson, Ken (guest)
    """),
    hint="Do the staff with one :s on a two-line range (2: types .,.+1 for you). On the guests, : and Ctrl-p "
         "bring it back, and Ctrl-w deletes from the end, so only the tag needs retyping.",
    uses=["subst", "very-magic", "range", "count", "ctrl-w"],
)
cmdline_keys.add(
    title="Add a range in front", par=13, ext="txt", setup=OWN_FILE_ONLY,
    task="Right-align the date (line 1) and the three lines of the signature (lines 8 to 10) to column 40 "
         "with :right 40.",
    start=text("""
        12 March 2026

        Dear Ada,

        Thanks for the notes on the parser.
        I'll send the next draft on Friday.

        Best wishes,
        Charles Babbage
        London
    """),
    target=text("""
                                   12 March 2026

        Dear Ada,

        Thanks for the notes on the parser.
        I'll send the next draft on Friday.

                                    Best wishes,
                                 Charles Babbage
                                          London
    """),
    hint="Run :ri40 on line 1. Then : and Ctrl-p bring it back, Ctrl-b jumps to the start, and you only type "
         "the range. $ means the last line.",
    uses=["range"],
)
cmdline_keys.add(
    title="Both ends", par=20, ext="md",
    setup=OWN_FILE_ONLY + [r"call histadd(':', 's/\v(.*) by (\w+)/\2: \1 [novel]/')",
                           "call histadd(':', 'nohlsearch')", "call histadd(':', 'set wrap')"],
    task="Three commands back in your history is the :s that rewrote the novel as \"Herbert: Dune [novel]\". "
         "Do the same to the poetry (lines 5 to 7), tagged [poetry].",
    start=text("""
        # Novels
        Herbert: Dune [novel]

        # Poetry
        Ariel by Plath
        Howl by Ginsberg
        Odes by Keats
    """),
    target=text("""
        # Novels
        Herbert: Dune [novel]

        # Poetry
        Plath: Ariel [poetry]
        Ginsberg: Howl [poetry]
        Keats: Odes [poetry]
    """),
    hint="Ctrl-p three times brings the :s back. Ctrl-b jumps to its start for the range 5,7, Ctrl-e back to "
         "the end, where Ctrl-w deletes the old tag.",
    uses=["subst", "very-magic", "range", "ctrl-w"],
)
cmdline_keys.add(
    title="A :g in front", par=9, ext="py",
    setup=OWN_FILE_ONLY + ["call histadd(':', 'normal A  # noqa: E501')"],
    task="The linter says the two URL lines are too long. Your last command added a # noqa: E501 comment to one "
         "line: add it to both URL lines here.",
    start=text("""
        import requests

        DOCS_URL = "https://docs.acme.dev/reference/configuration/advanced-options#retries"
        TIMEOUT = 30
        STATUS_URL = "https://status.acme.dev/api/v2/components/7f3c9b1e/incidents.json"


        def status():
            return requests.get(STATUS_URL, timeout=TIMEOUT).json()
    """),
    target=text("""
        import requests

        DOCS_URL = "https://docs.acme.dev/reference/configuration/advanced-options#retries"  # noqa: E501
        TIMEOUT = 30
        STATUS_URL = "https://status.acme.dev/api/v2/components/7f3c9b1e/incidents.json"  # noqa: E501


        def status():
            return requests.get(STATUS_URL, timeout=TIMEOUT).json()
    """),
    hint="Bring the command back with : and Ctrl-p, then Ctrl-b and a :g/pattern/ in front run it on every "
         "matching line. Any short pattern that only the two URL lines contain will do.",
    uses=["global", "normal"],
)
cmdline_keys.add(
    title="A range and a flag", par=7, ext="java",
    setup=OWN_FILE_ONLY + [r"call histadd(':', 's/\<int\>/long/')"],
    task="Use long instead of int everywhere: on every line, and all of them on each line. Your last command did "
         "it for the first int of one line. printInt keeps its name.",
    start=text("""
        class Stats {
            int count;
            int total;

            int add(int a, int b) { return a + b; }

            void printInt(int x) { System.out.println(x); }
        }
    """),
    target=text("""
        class Stats {
            long count;
            long total;

            long add(long a, long b) { return a + b; }

            void printInt(long x) { System.out.println(x); }
        }
    """),
    hint=": and Ctrl-p bring the :s back. It needs a range in front and a flag at the end: Ctrl-b and Ctrl-e get "
         "you to each end.",
    uses=["subst", "range"],
)
cmdline_keys.add(
    title="Two searches back", par=19, ext="py",
    setup=OWN_FILE_ONLY + [r"call histadd('/', '\v<(get|fetch)_user>')", "call histadd('/', 'render')"],
    task="Both loaders are now one function: rename every get_user and fetch_user call to load_user. get_users and "
         "forget_user stay. Two searches ago you searched for exactly those calls.",
    start=text("""
        def show_profile(request):
            user = get_user(request.user_id)
            friends = get_users(user.friend_ids)
            return render(user, friends)


        def refresh(request):
            user = fetch_user(request.user_id)
            if user.deleted:
                forget_user(user)
    """),
    target=text("""
        def show_profile(request):
            user = load_user(request.user_id)
            friends = get_users(user.friend_ids)
            return render(user, friends)


        def refresh(request):
            user = load_user(request.user_id)
            if user.deleted:
                forget_user(user)
    """),
    hint="Searches have their own history: / and Ctrl-p twice bring the pattern back. Once you've run it, an empty "
         "pattern in :s reuses it.",
    uses=["search", "subst", "range"],
)
