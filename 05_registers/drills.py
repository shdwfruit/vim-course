"""Drills for Project 05: short problems that practice one command at a time.
Play them with:  python3 check.py drill      (the reference solutions are in ../solutions/drills/)"""
from trainer import Drills, text

drills = Drills(__file__)

# ---------- "a … "z ----------

named = drills.command(
    "named", "\"a … \"z", "named registers",
    """Vim has 26 named registers, a to z, and it fills them only when you ask. Put " and a letter in front
    of a yank, delete or put: "ayy yanks the line into register a, "ap puts it after the cursor and "aP
    before it. Nothing else writes to them, so the text stays there while you yank and delete other things.
    A register remembers its shape: a yanked line goes back in as a whole line (below or above the cursor's
    line, wherever the cursor is), and a yanked word goes into the line. In Insert mode, Ctrl-r a types
    register a, and :reg a shows what's in it.""",
    examples=[("\"ayy", "yank the line into register a"), ("\"ap", "put register a after the cursor"),
              ("\"bP", "put register b before the cursor"), ("\"ayiw", "yank a word into register a"),
              ("\"a3p", "put register a three times"), ("Ctrl-r a", "type register a in Insert mode")],
)
named.add(
    title="Put a saved line", par=3, ext="java",
    task="Register a already holds a line you yanked earlier: import java.util.List;. Put it between the "
         "other two imports.",
    setup=['let @a = "import java.util.List;\\n"'],
    start=text("""
        import java.util.ArrayList;
        import java.util.Map;

        public class Inventory {
    """),
    target=text("""
        import java.util.ArrayList;
        import java.util.List;
        import java.util.Map;

        public class Inventory {
    """),
    hint="\"ap puts register a after the cursor. It holds a whole line, so it goes in below the cursor's line.",
    uses=["p"],
)
named.add(
    title="Put a saved word", par=6, ext="java",
    task="Register b already holds the word HashMap. Put it just after new, so the line ends with "
         "new HashMap<>();.",
    setup=['let @b = "HashMap"'],
    start="Map<String, Integer> counts = new <>();",
    target="Map<String, Integer> counts = new HashMap<>();",
    hint="Register b holds part of a line, so it goes into the line. Get onto the second < with 2f<, and "
         "\"bP puts the word before the cursor.",
    uses=["p", "f", "count"],
)
named.add(
    title="Frame the title", par=9, ext="txt",
    task="Register a already holds a border line, +----------+. Put a border above the title, one below "
         "it, and one at the very bottom.",
    setup=['let @a = "+----------+\\n"'],
    start=text("""
        |  SCORES  |
        | ana   42 |
        | bo    37 |
    """),
    target=text("""
        +----------+
        |  SCORES  |
        +----------+
        | ana   42 |
        | bo    37 |
        +----------+
    """),
    hint="\"aP puts the border above the cursor's line and \"ap below it. . repeats a put with the same "
         "register, so once you've used \"ap, G. adds the last one.",
    uses=["p", "dot", "gg"],
)
named.add(
    title="Grow the board", par=4, ext="txt",
    task="Register a already holds two lines: a separator, ---+---+---, and an empty row. Put them twice "
         "to finish the 3-by-3 board.",
    setup=['let @a = "---+---+---\\n   |   |   \\n"'],
    start=" X | O | X",
    target=text("""
         X | O | X
        ---+---+---
           |   |
        ---+---+---
           |   |
    """),
    hint="A count works with a register: \"a2p puts register a twice. A register can hold several lines.",
    uses=["p", "count"],
)
named.add(
    title="Wrap the traces", par=15, ext="c",
    task="Register a holds the line #ifdef DEBUG and register b holds #endif. Wrap each trace(s); call in "
         "them, so traces only run in debug builds.",
    setup=['let @a = "#ifdef DEBUG\\n"', 'let @b = "#endif\\n"'],
    start=text("""
        void step(State *s) {
            s->t += s->dt;
            trace(s);
            s->x += s->v * s->dt;
            trace(s);
        }
    """),
    target=text("""
        void step(State *s) {
            s->t += s->dt;
        #ifdef DEBUG
            trace(s);
        #endif
            s->x += s->v * s->dt;
        #ifdef DEBUG
            trace(s);
        #endif
        }
    """),
    hint="\"aP puts #ifdef above a trace and \"bp puts #endif below one. . repeats a put with the same "
         "register, so do both #ifdefs first (\"aP, then . on the other trace), then both #endifs.",
    uses=["p", "dot", "count"],
)
named.add(
    title="Point at the new server", par=8, ext="py",
    task="Register a already holds the new endpoint, https://api.internal.example.com/v2. Use it for "
         "both URLs.",
    setup=['let @a = "https://api.internal.example.com/v2"'],
    start=text("""
        PRIMARY = "http://10.0.0.12:8080/api"
        FALLBACK = "http://10.0.0.13:8080/api"
    """),
    target=text("""
        PRIMARY = "https://api.internal.example.com/v2"
        FALLBACK = "https://api.internal.example.com/v2"
    """),
    hint="ci\" clears the first URL, and Ctrl-r a types register a. After <Esc>, j. does the same on the "
         "next line.",
    uses=["ctrl-r", "c", "quote", "dot"],
)
named.add(
    title="Two names in a tuple", par=27, ext="py",
    task="Add a third line: limits = (MAX_CONNECTIONS, DEFAULT_TIMEOUT_SECONDS).",
    start=text("""
        MAX_CONNECTIONS = 100
        DEFAULT_TIMEOUT_SECONDS = 30
    """),
    target=text("""
        MAX_CONNECTIONS = 100
        DEFAULT_TIMEOUT_SECONDS = 30
        limits = (MAX_CONNECTIONS, DEFAULT_TIMEOUT_SECONDS)
    """),
    hint="Yank the first name into register a (\"ayiw) and the second one normally (yiw). Then open the "
         "new line and type it, inserting the names with Ctrl-r a and Ctrl-r 0.",
    uses=["ctrl-r", "y", "iw", "o", "yank0"],
)
named.add(
    title="A Markdown link", par=18, ext="md",
    task="Add a third line that links the title to the URL: [ASCII Garden](https://github.com/rick/ascii-garden).",
    start=text("""
        Repo: https://github.com/rick/ascii-garden
        Title: ASCII Garden
    """),
    target=text("""
        Repo: https://github.com/rick/ascii-garden
        Title: ASCII Garden
        [ASCII Garden](https://github.com/rick/ascii-garden)
    """),
    hint="Yank the URL into register a with \"ay$ and the title with plain y$. Then o opens the new line, "
         "and Ctrl-r \" and Ctrl-r a type the two parts.",
    uses=["ctrl-r", "y", "bigword", "word", "o"],
)
named.add(
    title="Sign off", par=32, ext="txt",
    task="Finish the commit message with a sign-off line built from lines 1 and 2: "
         "Signed-off-by: Ada Lovelace <ada@example.com>",
    start=text("""
        name: Ada Lovelace
        email: ada@example.com
    """),
    target=text("""
        name: Ada Lovelace
        email: ada@example.com
        Signed-off-by: Ada Lovelace <ada@example.com>
    """),
    hint="Yank the name into register a (\"ay$) and the address normally (y$). Then type the new line, "
         "using Ctrl-r a and Ctrl-r \" for the two parts.",
    uses=["ctrl-r", "y", "bigword", "word", "o"],
)
named.add(
    title="Log both values", par=42, ext="py",
    task="Add a third line that logs both variables: "
         "log.debug(\"user_id=%s retries=%s\", user_id, retries).",
    start=text("""
        user_id = request.args["user"]
        retries = int(request.args["retries"])
    """),
    target=text("""
        user_id = request.args["user"]
        retries = int(request.args["retries"])
        log.debug("user_id=%s retries=%s", user_id, retries)
    """),
    hint="Each name appears twice. Yank user_id into register a and retries normally, then type the line "
         "with Ctrl-r a and Ctrl-r 0 standing in for the names.",
    uses=["ctrl-r", "y", "iw", "yank0", "o"],
)
named.add(
    title="Pause in both functions", par=6, ext="js",
    task="Register a already holds the line debugger; (indented, ready to paste). Make it the first line of "
         "both function bodies.",
    setup=['let @a = "    debugger;\\n"'],
    start=text("""
        function parse(input) {
            const tokens = lex(input);
            return build(tokens);
        }

        function render(tree) {
            return tree.map(draw).join("\\n");
        }
    """),
    target=text("""
        function parse(input) {
            debugger;
            const tokens = lex(input);
            return build(tokens);
        }

        function render(tree) {
            debugger;
            return tree.map(draw).join("\\n");
        }
    """),
    hint="\"ap puts the line below the cursor's line. . repeats a put with the same register, so go down to "
         "the second function's first line and press it.",
    uses=["p", "dot", "count"],
)
named.add(
    title="Required columns", par=10, ext="sql",
    task="Register a already holds NOT NULL with a space in front. Make user_id, total and placed_at "
         "required: user_id BIGINT NOT NULL, and so on. note stays optional.",
    setup=['let @a = " NOT NULL"'],
    start=text("""
        CREATE TABLE orders (
            id BIGSERIAL PRIMARY KEY,
            user_id BIGINT,
            total NUMERIC(10, 2),
            placed_at TIMESTAMPTZ,
            note TEXT
        );
    """),
    target=text("""
        CREATE TABLE orders (
            id BIGSERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL,
            total NUMERIC(10, 2) NOT NULL,
            placed_at TIMESTAMPTZ NOT NULL,
            note TEXT
        );
    """),
    hint="The words go just before each line's last comma. $ lands on that comma, and \"aP puts the "
         "register before the cursor. . repeats the put, register and all. After a put the cursor is on "
         "its last character, past the end of the next line, so j lands on that line's comma.",
    uses=["p", "line", "dot", "count"],
)
named.add(
    title="One mirror for everything", par=12, ext="toml",
    task="Register a already holds the mirror's host name, artifacts.garden.internal. Put it in place of "
         "each CHANGEME.",
    setup=['let @a = "artifacts.garden.internal"'],
    start=text("""
        [mirrors]
        pypi = "https://CHANGEME/simple"
        npm = "https://CHANGEME/npm"
        cargo = "sparse+https://CHANGEME/cargo"
    """),
    target=text("""
        [mirrors]
        pypi = "https://artifacts.garden.internal/simple"
        npm = "https://artifacts.garden.internal/npm"
        cargo = "sparse+https://artifacts.garden.internal/cargo"
    """),
    hint="A search for an uppercase C finds each CHANGEME (smartcase). cw and Ctrl-r a replace it, and n. "
         "does the next one.",
    uses=["search", "c", "word", "ctrl-r", "dot"],
)
named.add(
    title="Read, then clamp", par=30, ext="c",
    task="Add a third line that reads channel 0 and clamps it: "
         "float t = clamp_temperature(read_sensor_channel(0));",
    start=text("""
        static float clamp_temperature(float celsius);
        static float read_sensor_channel(int channel);
    """),
    target=text("""
        static float clamp_temperature(float celsius);
        static float read_sensor_channel(int channel);
        float t = clamp_temperature(read_sensor_channel(0));
    """),
    hint="Yank one name into register a and the other one normally. In the new line, Ctrl-r a and Ctrl-r 0 "
         "type them. From the start of a word, ye yanks it in one key less than yiw.",
    uses=["ctrl-r", "y", "word", "o", "yank0", "count"],
)
named.add(
    title="Replace the stub", par=6, ext="py",
    task="Register a holds the three lines of the real implementation (indented, ready to paste). Replace "
         "the TODO comment and pass with them.",
    setup=["call setreg('a', ['    if shape.kind == \"circle\":', "
           "'        return math.pi * shape.r ** 2', '    return shape.w * shape.h'], 'l')"],
    start=text("""
        import math

        def area(shape):
            # TODO: compute it
            pass
    """),
    target=text("""
        import math

        def area(shape):
            if shape.kind == "circle":
                return math.pi * shape.r ** 2
            return shape.w * shape.h
    """),
    hint="Select the two stub lines with V, and \"ap replaces the selection with register a. (Or delete "
         "them first and put the register where they were.)",
    uses=["visual-line", "p", "gg"],
)
named.add(
    title="Bump the column", par=10, ext="md",
    task="Register a already holds the new version, 1.0.0. Put it in place of 0.9.0 for core, cli and web. "
         "docs stays at 0.8.2.",
    setup=['let @a = "1.0.0"'],
    start=text("""
        | package | version | status |
        |---------|---------|--------|
        | core    | 0.9.0   | ok     |
        | cli     | 0.9.0   | ok     |
        | web     | 0.9.0   | ok     |
        | docs    | 0.8.2   | frozen |
    """),
    target=text("""
        | package | version | status |
        |---------|---------|--------|
        | core    | 1.0.0   | ok     |
        | cli     | 1.0.0   | ok     |
        | web     | 1.0.0   | ok     |
        | docs    | 0.8.2   | frozen |
    """),
    hint="Select the three old versions as a block with Ctrl-v (a search for 0 gets you to the first). "
         "Putting a register that holds part of a line over a block puts it on every line of the block.",
    uses=["block-edit", "p", "search", "bigword", "count"],
)
named.add(
    title="A class on every button", par=9, ext="html",
    task="Register a already holds class=\"btn\" with a space in front. Add it to every <button> tag: "
         "<button class=\"btn\">Save</button>.",
    setup=["let @a = ' class=\"btn\"'"],
    start=text("""
        <nav class="toolbar">
          <button>Save</button>
          <button>Open</button>
          <button>Export</button>
          <button>Quit</button>
        </nav>
    """),
    target=text("""
        <nav class="toolbar">
          <button class="btn">Save</button>
          <button class="btn">Open</button>
          <button class="btn">Export</button>
          <button class="btn">Quit</button>
        </nav>
    """),
    hint="The four > of <button> are in one column. Ctrl-v selects them as a block, I inserts before it on "
         "every line, and Ctrl-r a types the register while you're inserting.",
    uses=["block-insert", "word", "ctrl-r", "count"],
)
named.add(
    title="A default policy", par=33, ext="py",
    task="Fill in the default: DEFAULT_POLICY = RetryPolicy(max_attempts=3, backoff_seconds=0.5).",
    start=text("""
        @dataclass
        class RetryPolicy:
            max_attempts: int
            backoff_seconds: float

        DEFAULT_POLICY = None
    """),
    target=text("""
        @dataclass
        class RetryPolicy:
            max_attempts: int
            backoff_seconds: float

        DEFAULT_POLICY = RetryPolicy(max_attempts=3, backoff_seconds=0.5)
    """),
    hint="Three long names, three registers: yank the class name into a, the first field into b and the "
         "second one normally. Then replace None, typing the names with Ctrl-r a, Ctrl-r b and Ctrl-r 0.",
    uses=["ctrl-r", "y", "word", "plus", "yank0", "c", "count"],
)
named.add(
    title="Two windows", par=14,
    task="Register a holds a window as a block: +--+, |  |, +--+ (4 columns, 3 rows). Put two windows in "
         "the wall, as in the target. The house stays the same width.",
    setup=["call setreg('a', ['+--+', '|  |', '+--+'], 'b')"],
    start=text("""
        +--------------+
        |              |
        |              |
        |              |
        |              |
        +--------------+
    """),
    target=text("""
        +--------------+
        | +--+    +--+ |
        | |  |    |  | |
        | +--+    +--+ |
        |              |
        +--------------+
    """),
    hint="A register remembers its shape, and this one is a block: \"ap inserts it on three lines at once, "
         "pushing the wall to the right. So first delete 8 columns of spaces as a block. Then put the "
         "window, and . puts it again.",
    uses=["block-edit", "p", "dot", "count"],
)
named.add(
    title="Fence the commands", par=19, ext="md",
    task="Register a holds the line ```sh and register b holds ```. Put each command in a fenced code "
         "block: ```sh above it and ``` below it.",
    setup=['let @a = "```sh\\n"', 'let @b = "```\\n"'],
    start=text("""
        Install it:
        pip install garden
        Then create a config:
        garden init --here
        And start it:
        garden serve --port 8080
    """),
    target=text("""
        Install it:
        ```sh
        pip install garden
        ```
        Then create a config:
        ```sh
        garden init --here
        ```
        And start it:
        ```sh
        garden serve --port 8080
        ```
    """),
    hint="\"ap and \"bp put the fences below the cursor's line, and . repeats a put with the same register. "
         "So put all the ```sh lines on the way down, then all the ``` lines on the way back up.",
    uses=["p", "dot", "count"],
)

# ---------- "0 ----------

yank0 = drills.command(
    "yank0", "\"0", "the yank register",
    """Register 0 holds the text of your last yank (y, yy, yiw ...), and deletes and changes never touch it.
    That's what makes it useful: after yy and then dd, p puts the deleted line, but "0p still puts the
    yanked one. In Insert mode, Ctrl-r 0 types it. That's how you put a yank into a change like ciw or
    ct(: the change deletes text into the unnamed register first, so Ctrl-r " would give back what you just
    deleted, while Ctrl-r 0 gives the yank. Visual p also leaves "0 alone. Only a plain yank fills it:
    "ayy fills a, not 0.""",
    examples=[("\"0p", "put the last yank, even after a delete"), ("Ctrl-r 0", "type the last yank in Insert mode"),
              ("ciwCtrl-r 0", "replace a word with the yank"), ("viw\"0p", "replace a selection with the yank"),
              (":reg 0", "show what's in register 0")],
)
yank0.add(
    title="The yank, not the delete", par=8, ext="txt",
    task="Delete the TODO line, and copy the top border below the results line to close the box.",
    start=text("""
        +---------+
        | TODO    |
        | results |
    """),
    target=text("""
        +---------+
        | results |
        +---------+
    """),
    hint="Yank the border, then delete the TODO line. p would put the deleted line now, but \"0p puts the "
         "yank.",
    uses=["y", "dd", "p"],
)
yank0.add(
    title="Fix the spelling twice", par=13, ext="txt",
    task="Lines 2 and 3 start with a misspelled Mississippi. Spell them like line 1.",
    start=text("""
        The Mississippi is the second-longest river in North America.
        Misisipi comes from an Ojibwe word for "great river".
        Missisippi barges carry grain south to the Gulf.
    """),
    target=text("""
        The Mississippi is the second-longest river in North America.
        Mississippi comes from an Ojibwe word for "great river".
        Mississippi barges carry grain south to the Gulf.
    """),
    hint="Yank the good spelling with yiw. ciw on a misspelling deletes it into the unnamed register, so "
         "type the yank with Ctrl-r 0, not Ctrl-r \". Then . repeats the change on line 3.",
    uses=["ctrl-r", "c", "iw", "y", "dot", "plus"],
)
yank0.add(
    title="Rename two references", par=17, ext="java",
    task="The last word on lines 2 and 3 should be monthlyRate, the variable from line 1.",
    start=text("""
        double monthlyRate = annualRate / 12;
        double interest = balance * rate;
        double minimum = fee + balance * rate;
    """),
    target=text("""
        double monthlyRate = annualRate / 12;
        double interest = balance * monthlyRate;
        double minimum = fee + balance * monthlyRate;
    """),
    hint="Yank monthlyRate, then ciw on rate and Ctrl-r 0. On the next line, the same motion gets you to "
         "rate, and . repeats the change.",
    uses=["ctrl-r", "c", "iw", "y", "dot", "line", "word"],
)
yank0.add(
    title="One region everywhere", par=12, ext="java",
    task="Move everything to eu-west-1: give backup and audit the same region as primary.",
    start=text("""
        String primary = "eu-west-1";
        String backup = "us-east-2";
        String audit = "ap-south-1";
    """),
    target=text("""
        String primary = "eu-west-1";
        String backup = "eu-west-1";
        String audit = "eu-west-1";
    """),
    hint="yi\" yanks the region. ci\" on the next line clears the other one, and Ctrl-r 0 types the yank "
         "(Ctrl-r \" would type back the region you just deleted). j. does the last line.",
    uses=["ctrl-r", "c", "quote", "y", "dot"],
)
yank0.add(
    title="Same style for every plot", par=12, ext="py",
    task="Give the scatter and fill_between calls the same arguments as the plot call on line 1.",
    start=text("""
        plt.plot(xs, ys, color="tab:blue", linewidth=2)
        plt.scatter(xs, ys)
        plt.fill_between(xs, ys)
    """),
    target=text("""
        plt.plot(xs, ys, color="tab:blue", linewidth=2)
        plt.scatter(xs, ys, color="tab:blue", linewidth=2)
        plt.fill_between(xs, ys, color="tab:blue", linewidth=2)
    """),
    hint="yi( yanks everything inside the parentheses. ci( on the next line deletes the old arguments, "
         "Ctrl-r 0 types the yank, and j. does it again.",
    uses=["ctrl-r", "c", "paren", "y", "dot"],
)
yank0.add(
    title="Same path everywhere", par=14, ext="ini",
    task="Point logs and tmp at the same folder as cache.",
    start=text("""
        [paths]
        cache = /home/rick/.cache/garden
        logs = /tmp/logs
        tmp = /tmp/tmp
    """),
    target=text("""
        [paths]
        cache = /home/rick/.cache/garden
        logs = /home/rick/.cache/garden
        tmp = /home/rick/.cache/garden
    """),
    hint="Yank the cache path with y$. On the next line, B gets you to the start of the path, and C "
         "replaces it: type the yank with Ctrl-r 0. jB. does the last line.",
    uses=["ctrl-r", "c", "bigword", "y", "dot"],
)
yank0.add(
    title="Everything to stderr", par=12, ext="c",
    task="Send every message to stderr like line 1 does: printf( becomes fprintf(stderr, .",
    start=text("""
        fprintf(stderr, "loading %s\\n", path);
        printf("parsed %d rows\\n", n);
        printf("done\\n");
    """),
    target=text("""
        fprintf(stderr, "loading %s\\n", path);
        fprintf(stderr, "parsed %d rows\\n", n);
        fprintf(stderr, "done\\n");
    """),
    hint="Yank fprintf(stderr, up to and including the space with y and f<Space>. Then cf( replaces "
         "printf( and Ctrl-r 0 types the yank. + goes to the start of the next line for a .",
    uses=["ctrl-r", "c", "f", "y", "dot", "plus"],
)
yank0.add(
    title="A new prefix", par=14, ext="c",
    task="Rename the pt_ functions to match particle_init: pt_update becomes particle_update, and pt_draw "
         "becomes particle_draw.",
    start=text("""
        void particle_init(Particles *p, int n);
        void pt_update(Particles *p, float dt);
        void pt_draw(const Particles *p);
    """),
    target=text("""
        void particle_init(Particles *p, int n);
        void particle_update(Particles *p, float dt);
        void particle_draw(const Particles *p);
    """),
    hint="yt_ yanks particle. On the next line, ct_ changes pt, and Ctrl-r 0 types the yank. Then +w "
         "gets to the last line's pt, and . repeats.",
    uses=["ctrl-r", "c", "t", "y", "dot", "plus", "word"],
)
yank0.add(
    title="Inline the variable", par=18, ext="py",
    task="timeout is only used twice. Delete line 1 and put its expression, settings.get(\"timeout\", 30), "
         "where timeout is used.",
    start=text("""
        timeout = settings.get("timeout", 30)
        client = Client(timeout)
        retry = Retry(timeout)
    """),
    target=text("""
        client = Client(settings.get("timeout", 30))
        retry = Retry(settings.get("timeout", 30))
    """),
    hint="Yank the expression with y$, then dd the line: now the unnamed register holds the line, but "
         "register 0 still holds the expression. ciw on timeout and Ctrl-r 0, then . on the next line.",
    uses=["ctrl-r", "c", "iw", "y", "dd", "dot", "bigword", "line", "word"],
)
yank0.add(
    title="Name the magic number", par=25, ext="java",
    task="Use the constant: replace each 3600 with TIMEOUT_SECONDS, and give the constant the value 3600 "
         "instead of 0.",
    start=text("""
        static final int TIMEOUT_SECONDS = 0;

        void connect() { socket.setTimeout(3600); }
        void reconnect() { socket.setTimeout(3600); }
    """),
    target=text("""
        static final int TIMEOUT_SECONDS = 3600;

        void connect() { socket.setTimeout(TIMEOUT_SECONDS); }
        void reconnect() { socket.setTimeout(TIMEOUT_SECONDS); }
    """),
    hint="Yank the name, then ciw on each 3600 with Ctrl-r 0 (and . for the second). Each change also put "
         "the 3600 it deleted into the unnamed register, so the last step is a plain Visual p on the 0.",
    uses=["ctrl-r", "c", "iw", "y", "dot", "visual", "p", "f", "word", "gg"],
)
yank0.add(
    title="No more any", par=17, ext="ts",
    task="Replace each any with UserRecord, the interface on line 1.",
    start=text("""
        interface UserRecord { id: number; name: string; }
        function load(id: number): any {}
        function notify(user: any): boolean {}
        function cache(users: any[]): void {}
    """),
    target=text("""
        interface UserRecord { id: number; name: string; }
        function load(id: number): UserRecord {}
        function notify(user: UserRecord): boolean {}
        function cache(users: UserRecord[]): void {}
    """),
    hint="Yank the name. A search for any lands on the first one: cw deletes it into the unnamed "
         "register, so type the yank with Ctrl-r 0. Then n. does the next one.",
    uses=["ctrl-r", "c", "word", "y", "iw", "search", "dot"],
)
yank0.add(
    title="Same color everywhere", par=14, ext="c",
    task="Give bg, border and shadow the same initializer as fg: { .r = 255, .g = 255, .b = 255 }.",
    start=text("""
        struct color fg = { .r = 255, .g = 255, .b = 255 };
        struct color bg = { 0 };
        struct color border = { 0 };
        struct color shadow = { 0 };
    """),
    target=text("""
        struct color fg = { .r = 255, .g = 255, .b = 255 };
        struct color bg = { .r = 255, .g = 255, .b = 255 };
        struct color border = { .r = 255, .g = 255, .b = 255 };
        struct color shadow = { .r = 255, .g = 255, .b = 255 };
    """),
    hint="ya{ yanks the braces and everything inside them, and ca{ replaces another pair. Both find the "
         "next braces on the line, so you don't need to move onto them. Type the yank with Ctrl-r 0, then "
         "+. does each of the other lines.",
    uses=["ctrl-r", "c", "brace", "y", "plus", "dot"],
)
yank0.add(
    title="One JUnit version", par=15, ext="xml",
    task="Both dependencies should use the version in <junit.version>: 5.11.3.",
    start=text("""
        <properties>
          <junit.version>5.11.3</junit.version>
        </properties>
        <dependency>
          <artifactId>junit-jupiter-api</artifactId>
          <version>5.10.0</version>
        </dependency>
        <dependency>
          <artifactId>junit-jupiter-engine</artifactId>
          <version>5.9.2</version>
        </dependency>
    """),
    target=text("""
        <properties>
          <junit.version>5.11.3</junit.version>
        </properties>
        <dependency>
          <artifactId>junit-jupiter-api</artifactId>
          <version>5.11.3</version>
        </dependency>
        <dependency>
          <artifactId>junit-jupiter-engine</artifactId>
          <version>5.11.3</version>
        </dependency>
    """),
    hint="yit yanks the text inside the tag. cit on an old <version> deletes it, so type the yank with "
         "Ctrl-r 0. The second <version> is the same number of lines further down, so a count and . do "
         "it.",
    uses=["ctrl-r", "c", "tag", "y", "count", "dot"],
)
yank0.add(
    title="Fill in the tenant", par=17, ext="sql",
    task="For debugging, replace each ? placeholder with the tenant from the comment on line 1, quotes "
         "included: 'acme-industries'.",
    start=text("""
        -- tenant: 'acme-industries'
        SELECT id FROM orders WHERE tenant = ? AND status = 'open';
        SELECT id FROM invoices WHERE tenant = ? AND paid = false;
        DELETE FROM carts WHERE tenant = ? AND updated_at < now() - interval '30 days';
        UPDATE users SET active = false WHERE tenant = ?;
    """),
    target=text("""
        -- tenant: 'acme-industries'
        SELECT id FROM orders WHERE tenant = 'acme-industries' AND status = 'open';
        SELECT id FROM invoices WHERE tenant = 'acme-industries' AND paid = false;
        DELETE FROM carts WHERE tenant = 'acme-industries' AND updated_at < now() - interval '30 days';
        UPDATE users SET active = false WHERE tenant = 'acme-industries';
    """),
    hint="f' and y$ yank the tenant with its quotes. /? finds a placeholder, s deletes it (into the "
         "unnamed register) and Ctrl-r 0 types the yank. n. does each of the others.",
    uses=["ctrl-r", "c", "f", "y", "line", "search", "dot"],
)
yank0.add(
    title="No more wildcards", par=14, ext="java",
    task="Replace each <?> with the element type from line 1: Iterator<OrderLine>, and so on.",
    start=text("""
        List<OrderLine> lines = order.getLines();
        Iterator<?> it = lines.iterator();
        Optional<?> first = lines.stream().findFirst();
        Stream<?> big = lines.stream().filter(l -> l.qty() > 10);
    """),
    target=text("""
        List<OrderLine> lines = order.getLines();
        Iterator<OrderLine> it = lines.iterator();
        Optional<OrderLine> first = lines.stream().findFirst();
        Stream<OrderLine> big = lines.stream().filter(l -> l.qty() > 10);
    """),
    hint="i< is the text inside angle brackets, and like i( it finds the next pair on the line. yi< "
         "yanks OrderLine, and ci< on the next line replaces the ?, typing the yank with Ctrl-r 0. + goes "
         "to the start of a line, and . repeats the change from there.",
    uses=["ctrl-r", "c", "angle", "y", "plus", "dot"],
)
yank0.add(
    title="Same region for every store", par=15, ext="csv",
    task="Replace each TBD with the region of store 17: eu-west-1.",
    start=text("""
        store,city,region
        17,Dublin,eu-west-1
        203,Cork,TBD
        9,Galway,TBD
        41,Limerick,TBD
    """),
    target=text("""
        store,city,region
        17,Dublin,eu-west-1
        203,Cork,eu-west-1
        9,Galway,eu-west-1
        41,Limerick,eu-west-1
    """),
    hint="Get to the start of the region (it's 9 words in) and y$ yanks it. ciw on TBD with Ctrl-r 0 "
         "replaces it. After the change the cursor is past the end of the next line, so j lands on its "
         "last letter, inside TBD, and . does the rest.",
    uses=["ctrl-r", "c", "iw", "word", "count", "line", "y", "dot"],
)
yank0.add(
    title="Move to the new package", par=20, ext="java",
    task="The utilities moved into this file's package: org.legacy.util. becomes org.garden.core.model. "
         "in all three imports.",
    start=text("""
        package org.garden.core.model;

        import org.legacy.util.Strings;
        import static org.legacy.util.Dates.parse;
        import org.legacy.util.Money;
    """),
    target=text("""
        package org.garden.core.model;

        import org.garden.core.model.Strings;
        import static org.garden.core.model.Dates.parse;
        import org.garden.core.model.Money;
    """),
    hint="Yank garden.core.model with yt;. A search for le finds legacy, and c2t. changes up to just "
         "before the second dot: legacy.util. Type the yank with Ctrl-r 0, then n. for the others.",
    uses=["ctrl-r", "c", "t", "count", "y", "word", "search", "dot"],
)
yank0.add(
    title="Log in both branches", par=13, ext="py",
    task="Replace each pass  # log here with a copy of the logger.debug(...) line, at that line's "
         "indentation.",
    start=text("""
        def handler(event, context):
            logger.debug("event", extra={"request_id": context.aws_request_id})
            if event.get("dry_run"):
                pass  # log here
                return {"skipped": True}
            for record in event["Records"]:
                pass  # log here
                process(record)
    """),
    target=text("""
        def handler(event, context):
            logger.debug("event", extra={"request_id": context.aws_request_id})
            if event.get("dry_run"):
                logger.debug("event", extra={"request_id": context.aws_request_id})
                return {"skipped": True}
            for record in event["Records"]:
                logger.debug("event", extra={"request_id": context.aws_request_id})
                process(record)
    """),
    hint="Yank the logger line from its first non-blank with y$, so it holds no indentation. S clears a "
         "line but keeps its indent, and Ctrl-r 0 types the yank (S just put the old line in the "
         "unnamed register). A search for pa finds each pass, and n. does the second.",
    uses=["ctrl-r", "c", "y", "line", "plus", "search", "dot"],
)
yank0.add(
    title="Redact the clients", par=14, ext="log",
    task="Replace every client address at the start of a log line with <redacted>, from line 1.",
    start=text("""
        # client addresses are replaced with <redacted>
        10.0.3.17 - - [05/Nov/2026:09:14:07] "GET /api/users HTTP/1.1" 200
        192.168.1.4 - - [05/Nov/2026:09:14:09] "POST /login HTTP/1.1" 302
        10.0.3.17 - - [05/Nov/2026:09:15:32] "GET /api/orders HTTP/1.1" 500
    """),
    target=text("""
        # client addresses are replaced with <redacted>
        <redacted> - - [05/Nov/2026:09:14:07] "GET /api/users HTTP/1.1" 200
        <redacted> - - [05/Nov/2026:09:14:09] "POST /login HTTP/1.1" 302
        <redacted> - - [05/Nov/2026:09:15:32] "GET /api/orders HTTP/1.1" 500
    """),
    hint="$ and yiW yank <redacted>. + goes to the start of the next line, where cW changes the address "
         "(it's one WORD, dots and all) and Ctrl-r 0 types the yank. +. does each of the other lines.",
    uses=["ctrl-r", "c", "bigword", "iw-big", "y", "line", "plus", "dot"],
)
yank0.add(
    title="Links and a reference", par=16, ext="md",
    task="Use the docs URL from line 1 in both links, and finish the reference definition at the bottom: "
         "[docs]: https://garden.dev/docs/v2",
    start=text("""
        See https://garden.dev/docs/v2 for details.
        - [Install](TODO)
        - [Upgrade](TODO)

        [docs]:
    """),
    target=text("""
        See https://garden.dev/docs/v2 for details.
        - [Install](https://garden.dev/docs/v2)
        - [Upgrade](https://garden.dev/docs/v2)

        [docs]: https://garden.dev/docs/v2
    """),
    hint="yE yanks the URL. ci( finds the next parentheses, even on a later line, so it fills the first "
         "link with Ctrl-r 0 from where you are, and j. does the second. Each change put a TODO in the "
         "unnamed register, so at the bottom, Ctrl-r 0 is the one that types the URL.",
    uses=["ctrl-r", "c", "paren", "y", "bigword", "dot", "insert", "gg"],
)

# ---------- "_ ----------

blackhole = drills.command(
    "blackhole", "\"_", "the black hole register",
    """Whatever you delete into register _ is simply gone, and no register changes. Normally every d, c, x
    and s replaces the unnamed register (and "1 or "-), so the text you were about to put with p gets
    pushed out. Put "_ in front of the delete ("_dd, "_dw, "_D, "_x, "_ciw) and p still puts what you cut or
    yanked before. . remembers the register, so after "_dd, . deletes into the black hole too. Often "0
    (for a yank) or "1 to "9 (for a line you cut) would get the text back just as well; the black hole
    keeps it in plain p.""",
    examples=[("\"_dd", "delete a line, keep the registers"), ("\"_D", "delete to the end of the line"),
              ("\"_x", "delete a character"), ("\"_dw", "delete a word"), ("\"_ciw", "change a word without saving it"),
              ("\"_3dd", "delete three lines")],
)
blackhole.add(
    title="Keep the cut", par=9, ext="py",
    task="The return ended up too early. Move it to the end of the function, and delete the debug print.",
    start=text("""
        def mean(xs):
            return total / len(xs)
            total = sum(xs)
            print("xs =", xs)
            check(xs)
    """),
    target=text("""
        def mean(xs):
            total = sum(xs)
            check(xs)
            return total / len(xs)
    """),
    hint="Cut the return with dd. Delete the print into the black hole with \"_dd, so the unnamed register "
         "still holds the return when you press p.",
    uses=["dd", "p"],
)
blackhole.add(
    title="Close the front matter", par=9, ext="md",
    task="Delete the draft: true line, and close the front matter with a copy of the --- line, just after "
         "the date.",
    start=text("""
        ---
        title: Notes on registers
        draft: true
        date: 2026-10-29

        Registers are Vim's clipboards.
    """),
    target=text("""
        ---
        title: Notes on registers
        date: 2026-10-29
        ---

        Registers are Vim's clipboards.
    """),
    hint="Yank the --- line. Delete the draft line with \"_dd, which leaves the yank in the unnamed "
         "register, and put it with p.",
    uses=["y", "dd", "p", "count"],
)
blackhole.add(
    title="Drop the comment", par=9, ext="java",
    task="Move the return to the end, and delete the // TODO comment on the declaration.",
    start=text("""
        return result;
        int result = compute();  // TODO: cache this
        log(result);
    """),
    target=text("""
        int result = compute();
        log(result);
        return result;
    """),
    hint="Cut the return with dd. On the next line, f/ finds the comment, and \"_D deletes to the end of "
         "the line without touching the unnamed register. (The spaces left before it don't count.)",
    uses=["dd", "d", "f", "p"],
)
blackhole.add(
    title="No more debug output", par=9, ext="c",
    task="free(buf) should come last, after both fclose calls. Delete the two debug puts lines.",
    start=text("""
        free(buf);
        puts("closing");
        fclose(out);
        puts("closed");
        fclose(in);
    """),
    target=text("""
        fclose(out);
        fclose(in);
        free(buf);
    """),
    hint="Cut free(buf) with dd, then \"_dd the first puts. . repeats the delete, black hole included, "
         "so j. removes the other one. Then p.",
    uses=["dd", "dot", "p"],
)
blackhole.add(
    title="Three commented lines", par=8, ext="py",
    task="Delete the three commented-out prints, and move cleanup() below save().",
    start=text("""
        cleanup()
        # print(a)
        # print(b)
        # print(c)
        save()
    """),
    target=text("""
        save()
        cleanup()
    """),
    hint="Cut cleanup() with dd. A count works with the black hole: \"_3dd deletes three lines and saves "
         "none of them.",
    uses=["dd", "count", "p"],
)
blackhole.add(
    title="The old main goes", par=8, ext="py",
    task="main() is called before it's defined. Move the call to the end of the file, and delete the "
         "commented-out old_main.",
    start=text("""
        main()
        # def old_main():
        #     run(legacy=True)
        def main():
            run()
    """),
    target=text("""
        def main():
            run()
        main()
    """),
    hint="Cut main() with dd. \"_dj deletes the line you're on and the one below it into the black hole. "
         "Then go down a line and p.",
    uses=["dd", "d", "p"],
)
blackhole.add(
    title="An extra parenthesis", par=8, ext="py",
    task="Move the return to the end, and delete the extra ) at the end of line 2.",
    start=text("""
        return result
        result = parse(text))
        validate(result)
    """),
    target=text("""
        result = parse(text)
        validate(result)
        return result
    """),
    hint="dd cuts the return. x would put the ) in the unnamed register, so delete it with \"_x. Then j "
         "and p.",
    uses=["x", "dd", "line", "p"],
)
blackhole.add(
    title="Drop the sudo", par=8, ext="sh",
    task="The script already runs as root. Delete sudo (and its space), and move exit 0 to the end.",
    start=text("""
        exit 0
        sudo apt-get install -y ripgrep
        echo "done"
    """),
    target=text("""
        apt-get install -y ripgrep
        echo "done"
        exit 0
    """),
    hint="Cut exit 0 with dd, delete the first word with \"_dw, and put the cut line below echo.",
    uses=["dd", "d", "word", "p"],
)
blackhole.add(
    title="A whole section goes", par=8, ext="md",
    task="Delete the Old notes section (with the blank line after it), and move garden --help below the "
         "Usage heading.",
    start=text("""
        garden --help
        ## Old notes
        Remove before release.
        Nothing here is true anymore.

        ## Usage
    """),
    target=text("""
        ## Usage
        garden --help
    """),
    hint="Cut the first line with dd. \"_dap deletes a paragraph and the blank line after it into the "
         "black hole, and leaves the cursor on the Usage heading, ready for p.",
    uses=["dd", "ip", "p"],
)
blackhole.add(
    title="Swap in the other list", par=16, ext="java",
    task="Make the queue a LinkedList, and delete the ArrayList import, which is then unused.",
    start=text("""
        import java.util.LinkedList;
        import java.util.ArrayList;
        List<String> queue = new ArrayList<>();
    """),
    target=text("""
        import java.util.LinkedList;
        List<String> queue = new LinkedList<>();
    """),
    hint="Yank LinkedList, delete the ArrayList import with \"_dd, then select ArrayList with viw and "
         "press p. The yank is still in the unnamed register because the delete went into the black hole.",
    uses=["y", "iw", "dd", "visual", "p", "f", "line", "word"],
)
blackhole.add(
    title="Trap after the function", par=8, ext="sh",
    task="trap must come after the function it calls. Move it to the end of the file, and delete the "
         "debug echo.",
    start=text("""
        trap cleanup EXIT
        echo "debug: $*"
        cleanup() {
            rm -rf "$TMP"
        }
    """),
    target=text("""
        cleanup() {
            rm -rf "$TMP"
        }
        trap cleanup EXIT
    """),
    hint="Cut the trap with dd. Delete the echo with \"_dd, so the unnamed register still holds the trap, "
         "then G and p.",
    uses=["dd", "gg", "p"],
)
blackhole.add(
    title="An argument too many", par=10, ext="c",
    task="free(buf) should come last, after fclose(fp). Also delete the extra , NULL argument from the "
         "fread call.",
    start=text("""
        free(buf);
        n = fread(buf, 1, size, fp, NULL);
        fclose(fp);
    """),
    target=text("""
        n = fread(buf, 1, size, fp);
        fclose(fp);
        free(buf);
    """),
    hint="Cut free(buf) with dd. % jumps to the call's closing ), and from there \"_dF, deletes back to "
         "the comma before it without touching the unnamed register. Then j and p.",
    uses=["dd", "d", "f", "percent", "p"],
)
blackhole.add(
    title="Modifiers in order", par=9, ext="java",
    task="Put the modifiers in the usual order and drop final: static public final void run() becomes "
         "public static void run().",
    start="static public final void run() {",
    target="public static void run() {",
    hint="dw cuts public and its space into the unnamed register, and leaves you on final. \"_dw deletes "
         "that without saving it, so 0P still puts public at the front.",
    uses=["d", "word", "line", "p"],
)
blackhole.add(
    title="Finish the commit message", par=9, ext="txt",
    task="The Signed-off-by trailer goes at the end of the message, after the body and a blank line. Move "
         "it there, and delete the two # comment lines Git added.",
    start=text("""
        Fix the crash on empty input
        Signed-off-by: Ada Lovelace <ada@example.com>

        The parser assumed at least one token.

        # Please enter the commit message for your changes.
        # Lines starting with '#' will be ignored.
    """),
    target=text("""
        Fix the crash on empty input

        The parser assumed at least one token.

        Signed-off-by: Ada Lovelace <ada@example.com>
    """),
    hint="Cut the trailer with jdd. On the last line, dk deletes it and the line above. Send those into "
         "the black hole, and the cursor lands on the blank line, right where p puts the trailer.",
    uses=["dd", "d", "gg", "p"],
)
blackhole.add(
    title="Load the script last", par=10, ext="html",
    task="Move the <script> line below <main>, and empty the placeholder paragraph: <p class=\"lead\"></p>.",
    start=text("""
        <body>
        <script src="app.js"></script>
        <p class="lead">Lorem ipsum dolor sit amet.</p>
        <main id="app"></main>
        </body>
    """),
    target=text("""
        <body>
        <p class="lead"></p>
        <main id="app"></main>
        <script src="app.js"></script>
        </body>
    """),
    hint="Cut the script line with dd. dit empties a tag, and \"_dit does it without replacing the "
         "unnamed register. Then j and p.",
    uses=["dd", "tag", "d", "p"],
)
blackhole.add(
    title="It's not a constant", par=13, ext="js",
    task="total changes in the loop, so it can't be const: make it let. And move the return to the end "
         "of the function.",
    start=text("""
        function sum(items) {
            return total;
            const total = 0;
            for (const item of items) total += item.price;
        }
    """),
    target=text("""
        function sum(items) {
            let total = 0;
            for (const item of items) total += item.price;
            return total;
        }
    """),
    hint="Cut the return with dd. cw would put const into the unnamed register, so change it with \"_cw. "
         "Then j and p.",
    uses=["dd", "plus", "c", "word", "p"],
)
blackhole.add(
    title="No options", par=10, ext="js",
    task="Close the database last, after render(rows), and drop the options object from the query: "
         "db.query(sql).",
    start=text("""
        await db.close();
        const rows = await db.query(sql, { timeout: 0, retries: 99 });
        render(rows);
    """),
    target=text("""
        const rows = await db.query(sql);
        render(rows);
        await db.close();
    """),
    hint="Cut the first line with dd. From the comma, % jumps to the } that closes the next bracket, so "
         "\"_d% deletes , { ... } without touching the unnamed register. Then j and p.",
    uses=["dd", "d", "percent", "f", "p"],
)
blackhole.add(
    title="Paste from the REPL", par=9, ext="py",
    task="These lines came from the Python prompt. Delete the >>> prompts (with their space), and move "
         "print(total) to the end.",
    start=text("""
        print(total)
        >>> prices = [3, 5, 8]
        >>> total = sum(prices)
    """),
    target=text("""
        prices = [3, 5, 8]
        total = sum(prices)
        print(total)
    """),
    hint="Cut the print with dd. \"_4x deletes the four characters of a prompt into the black hole, and "
         "j. does the next one: . remembers the register. Then p.",
    uses=["dd", "x", "count", "dot", "p"],
)
blackhole.add(
    title="Default arguments only", par=9, ext="py",
    task="Create the app with its default settings, create_app(), and move run() to the end of the file.",
    start=text("""
        run()
        app = create_app(debug=True, testing=True)
        configure(app)
    """),
    target=text("""
        app = create_app()
        configure(app)
        run()
    """),
    hint="Cut run() with dd. \"_di( empties the parentheses without touching the unnamed register, and "
         "like di( it finds them on the line even from column 1. Then j and p.",
    uses=["dd", "paren", "d", "p"],
)
blackhole.add(
    title="Rename on the way", par=24, ext="js",
    task="Rename sum to subtotal (all three uses), and move the return to the end.",
    start=text("""
        return format(total);
        let sum = 0;
        for (const x of xs) sum += x;
        const total = sum * 1.2;
    """),
    target=text("""
        let subtotal = 0;
        for (const x of xs) subtotal += x;
        const total = subtotal * 1.2;
        return format(total);
    """),
    hint="Cut the return with dd. * on sum finds its next use, \"_ciw renames it without touching the "
         "unnamed register, and n. does the others (. remembers the black hole). Then G and p.",
    uses=["dd", "star", "c", "iw", "dot", "word", "gg", "p"],
)

# ---------- Ctrl-r ----------

ctrl_r = drills.command(
    "ctrl-r", "Ctrl-r {r}", "insert a register while typing",
    """In Insert mode, Ctrl-r and a register name types that register's text at the cursor, and you stay in
    Insert mode to keep typing. That makes it the tool for building new text around something you yanked:
    yiw, then o, type, Ctrl-r ", type some more. Inside a change, remember that the change deletes first:
    after ciw, Ctrl-r " (and Ctrl-r -) give back the word you just replaced, Ctrl-r 0 gives your last yank,
    and Ctrl-r . the text you typed last time. Ctrl-r works on the : and / command lines too.""",
    examples=[("Ctrl-r \"", "what you last yanked or deleted"), ("Ctrl-r 0", "your last yank"),
              ("Ctrl-r a", "register a"), ("Ctrl-r -", "your last small delete"),
              ("Ctrl-r .", "the text you last typed"), (":%s/x/Ctrl-r \"/", "on the command line too")],
)
ctrl_r.add(
    title="Print the total", par=13, ext="py",
    task="Add a second line that prints the variable: print(total_revenue).",
    start="total_revenue = sum(order.amount for order in orders)",
    target=text("""
        total_revenue = sum(order.amount for order in orders)
        print(total_revenue)
    """),
    hint="Yank the name with yiw. Then o, type print(, and Ctrl-r \" types the name for you.",
    uses=["y", "iw", "o"],
)
ctrl_r.add(
    title="Quote the command", par=9, ext="md",
    task="Finish line 2 by quoting the command from line 1 in backticks: "
         "Install it with `pip install ascii-garden`.",
    start=text("""
        pip install ascii-garden
        Install it with .
    """),
    target=text("""
        pip install ascii-garden
        Install it with `pip install ascii-garden`.
    """),
    hint="y$ yanks the whole command. Go to the period on line 2 and insert before it: a backtick, "
         "Ctrl-r \", another backtick.",
    uses=["y", "line", "insert"],
)
ctrl_r.add(
    title="A default argument", par=22, ext="py",
    task="Give port the default DEFAULT_PORT, and add a new parameter timeout=30: "
         "def connect(host, port=DEFAULT_PORT, timeout=30):",
    start=text("""
        DEFAULT_PORT = 5432
        def connect(host, port):
            ...
    """),
    target=text("""
        DEFAULT_PORT = 5432
        def connect(host, port=DEFAULT_PORT, timeout=30):
            ...
    """),
    hint="Yank DEFAULT_PORT, then insert before the ) on line 2: =, Ctrl-r 0, and the rest. You never "
         "leave Insert mode.",
    uses=["y", "iw", "f", "insert"],
)
ctrl_r.add(
    title="Keep the old name in a comment", par=24, ext="py",
    task="Rename limit to max_items, and note the old name at the end of the line: "
         "max_items = 10  # was limit.",
    start="limit = 10",
    target="max_items = 10  # was limit",
    hint="ciw puts the word it deletes in the unnamed and small delete registers. After you type the new "
         "name, A takes you to the end of the line, where Ctrl-r - (or Ctrl-r \") types limit.",
    uses=["c", "iw", "insert", "small-delete"],
)
ctrl_r.add(
    title="The title, twice", par=24, ext="md",
    task="Replace TITLE with Terminal Garden, and use the same title as the link text on line 2: "
         "Back to [Terminal Garden](README.md).",
    start=text("""
        # TITLE
        Back to [](README.md)
    """),
    target=text("""
        # Terminal Garden
        Back to [Terminal Garden](README.md)
    """),
    hint="Type the title once. Register . holds the text you last typed, so between the brackets, "
         "Ctrl-r . types it again.",
    uses=["c", "word", "f", "insert", "readonly"],
)
ctrl_r.add(
    title="Call the getter", par=23, ext="java",
    task="Print through the getter: println(balance) should become println(account.getBalance()).",
    start=text("""
        public double getBalance() { return balance; }
        System.out.println(balance);
    """),
    target=text("""
        public double getBalance() { return balance; }
        System.out.println(account.getBalance());
    """),
    hint="Yank getBalance. ciw on balance deletes it into the unnamed register, so type account., then "
         "Ctrl-r 0 for the yank, then ().",
    uses=["c", "iw", "y", "yank0", "word", "f"],
)
ctrl_r.add(
    title="From the command line", par=15, ext="md",
    task="Replace every TBD with the default from line 1: ask in #garden-ops.",
    start=text("""
        Default: ask in #garden-ops
        - backups: TBD
        - alerts: TBD
        - on-call: TBD
    """),
    target=text("""
        Default: ask in #garden-ops
        - backups: ask in #garden-ops
        - alerts: ask in #garden-ops
        - on-call: ask in #garden-ops
    """),
    hint="Yank the default with y$. Then :%s/TBD/ and Ctrl-r \" types it into the command line as the "
         "replacement. (Project 07 covers :s.)",
    uses=["subst", "y", "bigword"],
)
ctrl_r.add(
    title="An id from the heading", par=14, ext="html",
    task="Give the heading an id with the same text: <h2 id=\"pricing\">pricing</h2>.",
    start="<h2>pricing</h2>",
    target='<h2 id="pricing">pricing</h2>',
    hint="yit yanks the text inside the tag and moves the cursor there. Go back to the > of <h2>, insert "
         "before it, and Ctrl-r \" types the yank between the quotes.",
    uses=["tag", "y", "f", "insert"],
)
ctrl_r.add(
    title="Make the folder", par=30, ext="sh",
    task='Add a second line: mkdir -p "$BACKUP_DIR" && cd "$BACKUP_DIR"',
    start='BACKUP_DIR="/mnt/backups/garden"',
    target=text("""
        BACKUP_DIR="/mnt/backups/garden"
        mkdir -p "$BACKUP_DIR" && cd "$BACKUP_DIR"
    """),
    hint="Yank the variable name, then type the line with o. Each $ is followed by Ctrl-r \", which you "
         "can use as often as you like.",
    uses=["y", "iw", "o"],
)
ctrl_r.add(
    title="Print a field", par=32, ext="c",
    task="Add a second line that prints the field: printf(\"max_connections=%d\\n\", cfg.max_connections);",
    start="struct config { int max_connections; };",
    target=text("""
        struct config { int max_connections; };
        printf("max_connections=%d\\n", cfg.max_connections);
    """),
    hint="Yank max_connections, open a new line, and type the printf with Ctrl-r \" wherever the name "
         "goes.",
    uses=["y", "iw", "count", "word", "o"],
)
ctrl_r.add(
    title="Log it with a label", par=26, ext="js",
    task="Add a second line that logs the value with its name: "
         "console.log(\"sessionTimeoutMs\", sessionTimeoutMs);",
    start='const sessionTimeoutMs = config.get("session.timeout");',
    target=text("""
        const sessionTimeoutMs = config.get("session.timeout");
        console.log("sessionTimeoutMs", sessionTimeoutMs);
    """),
    hint="Yank the name (ye from its first letter), then o and type the line. Ctrl-r \" types the name "
         "both times.",
    uses=["y", "word", "o"],
)
ctrl_r.add(
    title="Clean up on exit", par=16, ext="sh",
    task="Below the function, add a line that runs it when the script exits: trap cleanup_temp_files EXIT",
    start=text("""
        cleanup_temp_files() {
            rm -rf "$TMPDIR/garden"
        }
    """),
    target=text("""
        cleanup_temp_files() {
            rm -rf "$TMPDIR/garden"
        }
        trap cleanup_temp_files EXIT
    """),
    hint="ye yanks the function name. G and o open the new line, and Ctrl-r \" types the name.",
    uses=["y", "word", "gg", "o"],
)
ctrl_r.add(
    title="Label the deployment", par=21, ext="yaml",
    task="Add labels with an app label that matches the name: under metadata, labels: and then "
         "app: payments-worker.",
    start=text("""
        metadata:
          name: payments-worker
        spec: {}
    """),
    target=text("""
        metadata:
          name: payments-worker
          labels:
            app: payments-worker
        spec: {}
    """),
    hint="The name has a dash, so yank it as a WORD: $ and yiW. Then o, type labels: and Enter (YAML "
         "indents the next line for you), and app: with Ctrl-r \".",
    uses=["y", "iw-big", "line", "o"],
)
ctrl_r.add(
    title="A list type", par=23, ext="ts",
    task="Add a type for a list of them: type PaymentIntentList = PaymentIntent[];",
    start="interface PaymentIntent { id: string; amount: number; }",
    target=text("""
        interface PaymentIntent { id: string; amount: number; }
        type PaymentIntentList = PaymentIntent[];
    """),
    hint="Yank PaymentIntent, open a new line, and type it with Ctrl-r \" in both places.",
    uses=["y", "word", "o"],
)
ctrl_r.add(
    title="Assign the field", par=19, ext="java",
    task="Fill in the constructor: this.retryPolicy = retryPolicy;",
    start=text("""
        private final RetryPolicy retryPolicy;
        Client(RetryPolicy retryPolicy) {
        }
    """),
    target=text("""
        private final RetryPolicy retryPolicy;
        Client(RetryPolicy retryPolicy) {
            this.retryPolicy = retryPolicy;
        }
    """),
    hint="Yank retryPolicy (the last word of line 1). Open a line inside the constructor, and type the "
         "assignment with Ctrl-r \" for both names.",
    uses=["y", "word", "line", "o"],
)
ctrl_r.add(
    title="Finish the include guard", par=33, ext="c",
    task="Complete the include guard: #define GARDEN_CONFIG_H on line 2, and #endif /* GARDEN_CONFIG_H */ "
         "at the end, after a blank line.",
    start=text("""
        #ifndef GARDEN_CONFIG_H

        struct config { int port; };
    """),
    target=text("""
        #ifndef GARDEN_CONFIG_H
        #define GARDEN_CONFIG_H

        struct config { int port; };

        #endif /* GARDEN_CONFIG_H */
    """),
    hint="Yank the name once. Ctrl-r \" types it on the new line 2, and again in the #endif comment: "
         "a register stays put until you yank or delete something else.",
    uses=["y", "bigword", "word", "o", "gg"],
)
ctrl_r.add(
    title="Include your own header", files={"garden_sync.c": (
        text("""
            #include <stdio.h>

            int garden_sync(const char *dir) {
        """),
        text("""
            #include "garden_sync.h"
            #include <stdio.h>

            int garden_sync(const char *dir) {
        """),
    )}, par=16,
    task="A C file includes its own header first. Add #include \"garden_sync.h\" above the other include.",
    hint="Register % holds the file name, garden_sync.c. Type it with Ctrl-r %, and Backspace turns the c "
         "into an h.",
    uses=["o", "readonly"],
)
ctrl_r.add(
    title="Name the index", par=45, ext="sql",
    task="Add an index on order_id, named after the table and the column: "
         "CREATE INDEX order_items_order_id_idx ON order_items (order_id);",
    setup=["setlocal indentexpr="],
    start="CREATE TABLE order_items (order_id BIGINT NOT NULL, sku TEXT, qty INT);",
    target=text("""
        CREATE TABLE order_items (order_id BIGINT NOT NULL, sku TEXT, qty INT);
        CREATE INDEX order_items_order_id_idx ON order_items (order_id);
    """),
    hint="Two names, each used twice. Yank the table into register a and the column normally, then type "
         "the line with Ctrl-r a and Ctrl-r \".",
    uses=["y", "word", "count", "o", "named"],
)
ctrl_r.add(
    title="Comments above the fields", par=20, ext="c",
    task="Move each trailing // comment onto its own line, above its field and at the same indent.",
    start=text("""
        struct conn {
            int fd;             // socket, or -1 when closed
            unsigned retries;   // reconnect attempts so far
            time_t last_seen;   // last time we heard from the peer
        };
    """),
    target=text("""
        struct conn {
            // socket, or -1 when closed
            int fd;
            // reconnect attempts so far
            unsigned retries;
            // last time we heard from the peer
            time_t last_seen;
        };
    """),
    hint="D cuts a comment from its //. O opens a line above, already indented, and Ctrl-r \" types the "
         "comment there. (O<Esc>p would lose the indent: an empty new line doesn't keep it.) A count of w "
         "gets from one // to the next.",
    uses=["d", "o", "word", "count"],
)
ctrl_r.add(
    title="Fall back to the default", par=18, ext="c",
    task="Give each getenv call the default from line 1: getenv(\"GARDEN_STATE\") ?: DEFAULT_STATE_DIR; and "
         "the same for the other two.",
    start=text("""
        static const char *DEFAULT_STATE_DIR = "/var/lib/garden";
        const char *state = getenv("GARDEN_STATE");
        const char *cache = getenv("GARDEN_CACHE");
        const char *logs = getenv("GARDEN_LOGS");
    """),
    target=text("""
        static const char *DEFAULT_STATE_DIR = "/var/lib/garden";
        const char *state = getenv("GARDEN_STATE") ?: DEFAULT_STATE_DIR;
        const char *cache = getenv("GARDEN_CACHE") ?: DEFAULT_STATE_DIR;
        const char *logs = getenv("GARDEN_LOGS") ?: DEFAULT_STATE_DIR;
    """),
    hint="Yank DEFAULT_STATE_DIR. On the next line, $ lands on the ; and i inserts before it: ?: and "
         "Ctrl-r \". Afterwards the cursor is past the end of the next line, so j lands on its ;, and . "
         "repeats the insert.",
    uses=["y", "word", "count", "line", "insert", "dot"],
)

# ---------- "A … "Z ----------

append = drills.command(
    "append", "\"A … \"Z", "append to a named register",
    """An uppercase register name adds to the register instead of replacing it: "Ayy appends the line to
    register a, and "Adiw appends a word. If the old contents and the new text are both within a line, they
    are joined with nothing in between ("ayiw on foo, then "Ayiw on bar gives foobar). If either one is a
    whole line, the register holds whole lines. . remembers the register, so "Add followed by n. keeps
    collecting. Registers start empty in these drills; in your own Neovim, empty one first with qaq.""",
    examples=[("\"Ayy", "append the line to register a"), ("\"Add", "cut the line onto the end of a"),
              ("\"Ayiw", "append a word, with no space"), ("\"Add n.", "collect the next match too"),
              ("qaq", "empty register a first")],
    level="complex",
)
append.add(
    title="Gather the action items", par=16, ext="md",
    task="Move every ACTION: line to the end, under ## Actions, in the order they appear.",
    start=text("""
        ## Notes
        Budget is fine.
        ACTION: Ada books the room.
        Next sprint starts Monday.
        ACTION: Linus updates the README.
        Demo went well.
        ACTION: Grace files the bug.
        ## Actions
    """),
    target=text("""
        ## Notes
        Budget is fine.
        Next sprint starts Monday.
        Demo went well.
        ## Actions
        ACTION: Ada books the room.
        ACTION: Linus updates the README.
        ACTION: Grace files the bug.
    """),
    hint="Search for the first one with /AC. \"Add cuts a line onto the end of register a, and n. does it "
         "again on the next match. One G\"ap puts them all.",
    uses=["dd", "search", "dot", "gg", "named", "p"],
)
append.add(
    title="Build the URL", par=21, ext="py",
    task="Fill in url with the three parts above it joined together: "
         "url = \"https://api.example.com/v2/orders\".",
    start=text("""
        BASE = "https://api.example.com"
        VERSION = "/v2"
        ENDPOINT = "/orders"
        url = ""
    """),
    target=text("""
        BASE = "https://api.example.com"
        VERSION = "/v2"
        ENDPOINT = "/orders"
        url = "https://api.example.com/v2/orders"
    """),
    hint="Yank the first string into register a with \"ayi\", then append the others with \"Ayi\". Parts "
         "within a line are joined with nothing in between, which is just what a URL needs.",
    uses=["y", "quote", "named", "p"],
)
append.add(
    title="Split out the debug flags", par=15, ext="mk",
    task="Move -g and -DDEBUG from CFLAGS to the end of DEBUG_FLAGS: DEBUG_FLAGS = -g -DDEBUG.",
    start=text("""
        CFLAGS = -O2 -g -Wall -DDEBUG -Wextra
        DEBUG_FLAGS =
    """),
    target=text("""
        CFLAGS = -O2 -Wall -Wextra
        DEBUG_FLAGS = -g -DDEBUG
    """),
    hint="\"AdaW cuts a flag and the space after it onto register a. . does the same to the next flag. "
         "Then append to line 2 with A, a space, and Ctrl-r a.",
    uses=["d", "iw-big", "f", "dot", "insert", "ctrl-r"],
)
append.add(
    title="Copy the errors to the summary", par=21, ext="log",
    task="Copy every ERROR line, in order, below -- errors -- at the end. The originals stay where they "
         "are.",
    start=text("""
        09:14:07 INFO  web started
        09:14:09 ERROR db timeout after 5s
        09:15:32 WARN  slow request /api/users
        09:16:02 ERROR cache unreachable
        09:16:03 INFO  retrying
        09:17:44 ERROR disk full on /var
        -- errors --
    """),
    target=text("""
        09:14:07 INFO  web started
        09:14:09 ERROR db timeout after 5s
        09:15:32 WARN  slow request /api/users
        09:16:02 ERROR cache unreachable
        09:16:03 INFO  retrying
        09:17:44 ERROR disk full on /var
        -- errors --
        09:14:09 ERROR db timeout after 5s
        09:16:02 ERROR cache unreachable
        09:17:44 ERROR disk full on /var
    """),
    hint="/E finds an ERROR line (the capital E makes the search match case). \"Ayy appends a line to "
         "register a. A yank isn't a change, so . can't repeat it: type \"Ayy again after each n. Then one "
         "put at the end.",
    uses=["y", "search", "gg", "named", "p"],
)
append.add(
    title="Deprecated goes last", par=15, ext="md",
    task="Move the two (deprecated) sections, each with its text and the blank line after it, to the end, "
         "below ## Deprecated and its blank line, in the order they appear.",
    start=text("""
        ## open
        Opens a file.

        ## save (deprecated)
        Use write instead.

        ## write
        Writes a file.

        ## close (deprecated)
        Closes everything.

        ## Deprecated

    """) + "\n",
    target=text("""
        ## open
        Opens a file.

        ## write
        Writes a file.

        ## Deprecated

        ## save (deprecated)
        Use write instead.

        ## close (deprecated)
        Closes everything.
    """),
    hint="A search for (d finds the first one. \"Adap cuts a paragraph and the blank line after it onto "
         "the end of register a, and n. does the same for the next one. Then G and \"ap.",
    uses=["search", "ip", "d", "dot", "gg", "named", "p"],
)
append.add(
    title="Too long; didn't read", par=23, ext="md",
    task="Fill in the TL;DR line with the first sentence of each paragraph, in order: TL;DR: Registers "
         "are Vim's clipboards. The yank register keeps your last yank. The black hole register forgets.",
    start=text("""
        TL;DR:

        Registers are Vim's clipboards. There are dozens of them, and most fill themselves.

        The yank register keeps your last yank. Deletes never touch it, so it survives a dd.

        The black hole register forgets. Delete into it when you want to keep what you cut.
    """),
    target=text("""
        TL;DR: Registers are Vim's clipboards. The yank register keeps your last yank. The black hole register forgets.

        Registers are Vim's clipboards. There are dozens of them, and most fill themselves.

        The yank register keeps your last yank. Deletes never touch it, so it survives a dd.

        The black hole register forgets. Delete into it when you want to keep what you cut.
    """),
    hint="y) yanks from the cursor to the start of the next sentence, so it takes the space after the "
         "period too. \"ay) the first sentence, \"Ay) the other two, and the spaces join them. Then type "
         "register a after TL;DR: with Ctrl-r a.",
    uses=["y", "sentence", "count", "gg", "insert", "ctrl-r", "named"],
)

# ---------- "1 … "9 ----------

numbered = drills.command(
    "numbered", "\"1 … \"9", "the delete history",
    """Registers 1 to 9 remember your last nine big deletes. Every delete or change of a line or more (dd,
    3dd, cc, dj, dap) goes into "1, and the older ones shift down: "1 moves to "2, "2 to "3, and "9 falls
    off the end. Deletes within a line (x, dw, D, diw) go to "- instead, except a delete with one of the
    motions % ( ) ` / ? n N { }, which always lands in "1 too. After a numbered put, . moves on to the next
    number, so "1p.. puts the last three deletes, and "1pu.u. browses back until you find the one you want.""",
    examples=[("\"1p", "put the most recent delete"), ("\"3p", "put the delete from three deletes ago"),
              ("\"1p..", "put \"1, then \"2, then \"3"), ("\"1pu.u.", "browse: undo, try the next one"),
              ("d)", "delete to the next sentence; it goes into \"1")],
    level="complex",
)
numbered.add(
    title="Tear down in reverse", par=12, ext="sql",
    task="Teardown runs in the reverse order of setup: reverse the four DROP lines.",
    start=text("""
        -- teardown runs in the reverse order of setup
        DROP TABLE accounts;
        DROP TABLE users;
        DROP TABLE carts;
        DROP TABLE orders;
    """),
    target=text("""
        -- teardown runs in the reverse order of setup
        DROP TABLE orders;
        DROP TABLE carts;
        DROP TABLE users;
        DROP TABLE accounts;
    """),
    hint="Delete the four lines one at a time (dd and .), so the last one deleted is in register 1. Then "
         "\"1p puts it, and each . puts the next older one.",
    uses=["dd", "dot", "p"],
)
numbered.add(
    title="Three deletes ago", par=10, ext="py",
    task="Delete both debug prints, and move cleanup() below run().",
    start=text("""
        import os
        cleanup()
        print("debug 1")
        run()
        print("debug 2")
    """),
    target=text("""
        import os
        run()
        cleanup()
    """),
    hint="Cut cleanup() and delete the two prints with dd and j. as you go. The cut line is now three "
         "deletes back, in register 3.",
    uses=["dd", "dot", "p"],
)
numbered.add(
    title="A sentence to the end", par=10, ext="txt",
    task="Move the second sentence, \"Each one holds text.\", to the end of the paragraph, and delete the "
         "doubled \"are\".",
    start="Vim has many registers. Each one holds text. They are are named after letters.",
    target="Vim has many registers. They are named after letters. Each one holds text.",
    hint=") jumps to the next sentence, and d) deletes one. Because it uses the ) motion, it goes into "
         "register 1 even though it's within the line, so it survives the dw you use on \"are\". Then append "
         "a space and Ctrl-r 1.",
    uses=["d", "sentence", "word", "insert", "ctrl-r"],
)
numbered.add(
    title="The second of four", par=8, ext="py",
    task="While tidying up you deleted four lines with dd, in this order: metrics.incr(\"handler\"), "
         "print(event), audit(event) and log.info(\"done\"). Registers 1 to 4 still hold them. Put "
         "audit(event) back below validate(event), and the metrics line back as the first line of the body.",
    setup=["call setreg('4', ['    metrics.incr(\"handler\")'], 'l')", "call setreg('3', ['    print(event)'], 'l')",
           "call setreg('2', ['    audit(event)'], 'l')", "call setreg('1', ['    log.info(\"done\")'], 'l')"],
    start=text("""
        def handler(event):
            validate(event)
            return respond(event)
    """),
    target=text("""
        def handler(event):
            metrics.incr("handler")
            validate(event)
            audit(event)
            return respond(event)
    """),
    hint="The most recent delete is in \"1, so the first of four is in \"4 and the third in \"2. \"2p puts "
         "a line below the cursor's line and \"4P above it.",
    uses=["p"],
)
numbered.add(
    title="Exports first, in order", par=17, ext="sh",
    task="Move the three export lines up, just below the #! line, keeping their order.",
    start=text("""
        #!/bin/sh
        echo "starting"
        export GARDEN_HOME=/opt/garden
        mkdir -p "$GARDEN_HOME/var"
        export GARDEN_ENV=prod
        cd "$GARDEN_HOME"
        export GARDEN_PORT=8080
        exec garden serve
    """),
    target=text("""
        #!/bin/sh
        export GARDEN_HOME=/opt/garden
        export GARDEN_ENV=prod
        export GARDEN_PORT=8080
        echo "starting"
        mkdir -p "$GARDEN_HOME/var"
        cd "$GARDEN_HOME"
        exec garden serve
    """),
    hint="Delete them top to bottom with dd and n. (search for xp: exec has no xp). The last one is in \"1. "
         "\"1P puts it above the cursor, and each . puts the next older one above that, so they come back "
         "in their original order.",
    uses=["search", "dd", "dot", "gg", "p"],
)
numbered.add(
    title="Teardown goes last", par=11, ext="py",
    task="Delete both debug prints, and move log.flush() and then conn.close() to the end, after "
         "report(rows), in that order.",
    start=text("""
        conn = connect()
        print("connected")
        conn.close()
        rows = conn.query(SQL)
        log.flush()
        print("rows:", len(rows))
        report(rows)
    """),
    target=text("""
        conn = connect()
        rows = conn.query(SQL)
        report(rows)
        log.flush()
        conn.close()
    """),
    hint="Delete all four lines with dd and . as you go down. Then the flush is in \"2 and the close in \"3. "
         "After a numbered put, . puts the next number, so \"2p. puts both.",
    uses=["dd", "dot", "p"],
)

# ---------- "- ----------

small_delete = drills.command(
    "small-delete", "\"-", "the small delete register",
    """Register - holds the last delete or change that stayed within one line (x, dw, D, ciw ...), as long
    as you didn't name a register. Whole-line deletes like dd don't touch it, and neither do yanks, so a
    word you cut is still in "- after a dd has replaced the unnamed register. In Insert mode, Ctrl-r -
    types it. And in a change you repeat with ., Ctrl-r - types the register's contents at the time of the
    repeat, not the text from the first time, which makes "wrap this word" changes repeatable.""",
    examples=[("\"-p", "put the last small delete"), ("Ctrl-r -", "type it in Insert mode"),
              ("ciwf(Ctrl-r -)", "wrap a word in f( ), repeatable with ."), (":reg -", "show what's in it")],
    level="complex",
)
small_delete.add(
    title="Move the modifier", par=9, ext="java",
    task="final is on the wrong method: move it from save() to load(), and delete the TODO comment.",
    start=text("""
        public final void save() {}
        // TODO: make load final too
        public void load() {}
    """),
    target=text("""
        public void save() {}
        public final void load() {}
    """),
    hint="dw cuts final and its space into \"- (and \"\"). Delete the TODO with dd, which replaces \"\" but "
         "not \"-, and put the word with \"-P.",
    uses=["d", "word", "dd", "p"],
)
small_delete.add(
    title="Round every amount", par=28, ext="java",
    task="Round each amount: total += Math.round(price); and the same for shipping and tax.",
    start=text("""
        total += price;
        total += shipping;
        total += tax;
    """),
    target=text("""
        total += Math.round(price);
        total += Math.round(shipping);
        total += Math.round(tax);
    """),
    hint="ciw deletes the word into \"-. Type Math.round(, Ctrl-r -, and ). When you repeat that with ., "
         "Ctrl-r - types whatever that repeat just deleted.",
    uses=["ctrl-r", "c", "iw", "dot", "line", "word"],
)
small_delete.add(
    title="Rename, then alias", par=25, ext="py",
    task="Rename fetch_user to get_user, delete the commented-out print, and add fetch_user = get_user at "
         "the end, after a blank line, so old callers keep working.",
    start=text("""
        def fetch_user(user_id):
            return db.get(user_id)
        # print("loaded")
    """),
    target=text("""
        def get_user(user_id):
            return db.get(user_id)

        fetch_user = get_user
    """),
    hint="cw puts fetch_user in \"- and \"\". The dd that removes the comment replaces \"\", but \"- still "
         "holds the old name for Ctrl-r -. The new name is in \". (the text you typed last).",
    uses=["c", "word", "dd", "o", "ctrl-r", "readonly"],
)
small_delete.add(
    title="No NULLs in the report", par=25, ext="sql",
    task="Wrap each money column in COALESCE so NULL counts as 0: COALESCE(discount, 0), and the same for "
         "tax and shipping.",
    start="SELECT id, discount, tax, shipping FROM orders;",
    target="SELECT id, COALESCE(discount, 0), COALESCE(tax, 0), COALESCE(shipping, 0) FROM orders;",
    hint="ciw deletes the column name into \"-. Type COALESCE(, Ctrl-r -, and , 0). When . repeats the "
         "change on the next column, Ctrl-r - types that column's name.",
    uses=["ctrl-r", "c", "iw", "dot", "word", "count"],
)
small_delete.add(
    title="Move the !important", par=13, ext="css",
    task="!important is on the wrong rule: move it from the .btn color to the .btn-primary background, "
         "and delete the TODO comment.",
    start=text("""
        .btn { color: white !important; }
        /* TODO: remove the old rule */
        .btn-primary { background: navy; }
    """),
    target=text("""
        .btn { color: white; }
        .btn-primary { background: navy !important; }
    """),
    hint="From the ;, dF<Space> cuts  !important and the space before it. It's a small delete, so it's "
         "in \"-, and the dd that removes the comment doesn't touch \"-. Then \"-P before the other ;.",
    uses=["d", "f", "dd", "p"],
)
small_delete.add(
    title="Quote the variables", par=15, ext="sh",
    task="Quote every argument that uses a variable, so paths with spaces work: cp \"$SRC_DIR/config.toml\" "
         "\"$DEST_DIR/\", and so on.",
    start=text("""
        cp $SRC_DIR/config.toml $DEST_DIR/
        rm -rf $CACHE_DIR
        mkdir -p $LOG_DIR/$RUN_ID
    """),
    target=text("""
        cp "$SRC_DIR/config.toml" "$DEST_DIR/"
        rm -rf "$CACHE_DIR"
        mkdir -p "$LOG_DIR/$RUN_ID"
    """),
    hint="ciW changes a whole argument, slashes and all. Type a quote, Ctrl-r - and another quote, and . "
         "repeats that on any other argument, wherever in it the cursor is. The arguments to fix on lines "
         "2 and 3 are the last ones, so look for cheap ways to their ends.",
    uses=["ctrl-r", "c", "iw-big", "bigword", "dot", "line"],
)

# ---------- Ctrl-r = ----------

expr = drills.command(
    "expr", "Ctrl-r =  \"=", "the expression register: a calculator",
    """Register = is a calculator. In Insert mode, Ctrl-r = opens a prompt at the bottom of the screen:
    type an expression, press Enter, and its result is typed for you. In Normal mode, "=6*7<CR>p puts 42
    after the cursor. Whole numbers give whole results (7/2 is 3, 7/2.0 is 3.5), and hex like 0xff works.
    The prompt is a command line, so Ctrl-r works in it: Ctrl-r 0 drops in a formula you yanked, and after
    a ciw or C, Ctrl-r - drops in the text you just deleted.""",
    examples=[("Ctrl-r =60*60*24<CR>", "type 86400"), ("\"=6*7<CR>p", "put 42 in Normal mode"),
              ("Ctrl-r =7/2.0<CR>", "type 3.5"), ("Ctrl-r =0xff<CR>", "type 255"),
              ("Ctrl-r =Ctrl-r 0<CR>", "type the value of a yanked formula")],
    level="complex",
)
expr.add(
    title="Config files can't multiply", par=19, ext="toml",
    task="TOML has no arithmetic. Replace each formula with its value: 26214400 and 2592000.",
    start=text("""
        max_upload = 25 * 1024 * 1024
        session_ttl = 60 * 60 * 24 * 30
    """),
    target=text("""
        max_upload = 26214400
        session_ttl = 2592000
    """),
    hint="C deletes the formula into \"-, so in the Ctrl-r = prompt, Ctrl-r - types it back for Vim to "
         "work out. Enter inserts the result.",
    uses=["c", "ctrl-r", "small-delete", "f", "bigword", "word"],
)
expr.add(
    title="JSON has no hex", par=21, ext="json",
    task="JSON doesn't allow hex numbers. Write both colors in decimal: 2003199 and 16753920.",
    start='{"accent": 0x1E90FF, "warning": 0xFFA500}',
    target='{"accent": 2003199, "warning": 16753920}',
    hint="ciw on a hex number deletes it into \"-. In the Ctrl-r = prompt, Ctrl-r - types it back, and "
         "Enter converts it.",
    uses=["c", "iw", "ctrl-r", "small-delete", "f"],
)
expr.add(
    title="Nanoseconds per day", par=11, ext="c",
    task="Fill in NS_PER_DAY with the value of the formula in the comment, 86400000000000.",
    start=text("""
        // 24 * 60 * 60 * 1000000000
        const long long NS_PER_DAY = ;
    """),
    target=text("""
        // 24 * 60 * 60 * 1000000000
        const long long NS_PER_DAY = 86400000000000;
    """),
    hint="Yank the formula. In Normal mode, \"= picks the expression register: type Ctrl-r 0 at its prompt, "
         "press Enter, and P puts the result before the ;.",
    uses=["y", "word", "line", "ctrl-r", "yank0", "p"],
)
expr.add(
    title="Frame buffer sizes", par=18, ext="c",
    task="Write each array size as a number: 8294400 and 2073600.",
    start=text("""
        static uint8_t framebuffer[1920 * 1080 * 4];
        static uint16_t depth[1920 * 1080];
    """),
    target=text("""
        static uint8_t framebuffer[8294400];
        static uint16_t depth[2073600];
    """),
    hint="ci[ finds the brackets on the line and deletes the formula into \"-. In the Ctrl-r = prompt, "
         "Ctrl-r - types it back for Vim to work out.",
    uses=["c", "bracket", "ctrl-r", "small-delete", "plus"],
)
expr.add(
    title="No math in .env", par=17, ext="sh",
    task="An .env file can't hold expressions. Replace each one with its value: 52428800 and 604800.",
    start=text("""
        # .env: plain values only
        MAX_UPLOAD_BYTES=50*1024*1024
        CACHE_TTL_SECONDS=7*24*60*60
    """),
    target=text("""
        # .env: plain values only
        MAX_UPLOAD_BYTES=52428800
        CACHE_TTL_SECONDS=604800
    """),
    hint="Get to the first digit of an expression (a count of w does it), and C deletes the expression "
         "into \"-. Ctrl-r = and Ctrl-r - type it into the prompt, and Enter inserts the value.",
    uses=["c", "word", "count", "ctrl-r", "small-delete"],
)
expr.add(
    title="Keep the formula in a comment", par=37, ext="c",
    task="Write each size as a number, and keep its formula in a comment: "
         "#define CACHE_BYTES 67108864  /* (64 * 1024 * 1024) */, and the same for LOG_BYTES.",
    start=text("""
        #define CACHE_BYTES (64 * 1024 * 1024)
        #define LOG_BYTES (512 * 1024 * 1024)
    """),
    target=text("""
        #define CACHE_BYTES 67108864  /* (64 * 1024 * 1024) */
        #define LOG_BYTES 536870912  /* (512 * 1024 * 1024) */
    """),
    hint="C from the ( deletes the formula into \"-. Ctrl-r = and Ctrl-r - type its value, and after "
         "that, a plain Ctrl-r - types the formula itself into the comment.",
    uses=["c", "f", "ctrl-r", "small-delete", "plus", "semicolon"],
)

# ---------- ". "% ": "/ ----------

readonly = drills.command(
    "readonly", "\".  \"%  \":  \"/", "read-only registers",
    """Vim fills four registers for you, and you can put them like any other (".p, "%P, Ctrl-r :) but not
    yank into them. ". holds the last text you typed in Insert mode, "% the name of the current file, ":
    the last command line you ran, and "/ the last search pattern (after * on count, that's \\<count\\>). On
    the command line, Ctrl-r : types the last command again, so you can run it on something else or edit
    it first.""",
    examples=[("\".p", "put the text you last typed"), ("\"%P", "put the file name"),
              ("Ctrl-r .", "type the last insert again"), (":Ctrl-r :", "bring back the last command"),
              ("Ctrl-r /", "type the last search pattern")],
    level="complex",
)
readonly.add(
    title="Name the script", par=7,
    task="The usage message should name this script. Put the file name, backup_photos.py, between "
         "python3 and SRC (there's already a space on each side).",
    files={"backup_photos.py": (
        text("""
            import sys

            if len(sys.argv) != 3:
                sys.exit("usage: python3  SRC DEST")
        """),
        text("""
            import sys

            if len(sys.argv) != 3:
                sys.exit("usage: python3 backup_photos.py SRC DEST")
        """),
    )},
    hint="Register % holds the file name. Get onto the first of the two spaces, and \"%p puts it after the "
         "cursor.",
    uses=["gg", "f", "p"],
)
readonly.add(
    title="Use math.pi twice", par=22, ext="py",
    task="Replace 3.14 with math.pi, and fill the gap in the circumference formula with math.pi too: "
         "2 * math.pi * r.",
    start=text("""
        def area(radius):
            return 3.14 * radius ** 2
        def circumference(r):
            return 2 *  * r
    """),
    target=text("""
        def area(radius):
            return math.pi * radius ** 2
        def circumference(r):
            return 2 * math.pi * r
    """),
    hint="Type math.pi once, with ciW on 3.14. Register . now holds it, and \".P puts it in the gap. . can't "
         "do it: it would repeat the whole ciW.",
    uses=["c", "iw-big", "bigword", "f", "p"],
)
readonly.add(
    title="Center the credits too", par=21, ext="txt",
    task="Center the title lines (1 and 2) in 40 columns with :'<,'>center 40, then the credits (lines 4 "
         "and 5) the same way. Line 3 stays as it is.",
    start=text("""
        GARDEN
        a terminal plant sim
        Plants grow while you work. Water them with :w.
        Made by Rick
        October 2026
    """),
    target="""                 GARDEN
          a terminal plant sim
Plants grow while you work. Water them with :w.
              Made by Rick
              October 2026""",
    hint="Select lines 1 and 2 and run :center 40 (: in Visual mode types the range for you). Then select "
         "lines 4 and 5, press :, and Ctrl-r : types the last command line again.",
    uses=["visual-line", "visual-ex", "count", "ctrl-r"],
)
readonly.add(
    title="The workflow watches itself", par=4,
    task="Re-run this workflow when the workflow itself changes: fill in the empty path with its own file "
         "name, .github/workflows/lint.yml.",
    files={".github/workflows/lint.yml": (
        text("""
            on:
              push:
                paths:
                  - "src/**"
                  - ""
        """),
        text("""
            on:
              push:
                paths:
                  - "src/**"
                  - ".github/workflows/lint.yml"
        """),
    )},
    hint="Register % holds the file's name, path and all, the way Neovim opened it. Get onto the closing "
         "quote of the empty string (with no blank line, } goes to the end of the file), and \"%P puts "
         "the name before it.",
    uses=["paragraph", "p"],
)
readonly.add(
    title="Write down what you ran", par=18, ext="md",
    task="Center the first two lines in 30 columns with :center 30 on a Visual selection of them. Then "
         "record the command you ran after \"done with:\": done with: '<,'>center 30",
    start=text("""
        GARDEN
        a terminal plant sim
        done with:
    """),
    target="""            GARDEN
     a terminal plant sim
done with: '<,'>center 30""",
    hint="Vj and : type the range for you. Register : then holds the whole command line you ran, so "
         "append a space after done with: and type it with Ctrl-r :.",
    uses=["visual-line", "visual-ex", "center", "insert", "ctrl-r", "gg"],
)
readonly.add(
    title="A better name, three times", par=35, ext="js",
    task="Rename the cb parameter to onComplete, and add a first line to the body that defaults it: "
         "if (!onComplete) onComplete = noop;",
    start=text("""
        function run(job, cb) {
            job.start();
        }
    """),
    target=text("""
        function run(job, onComplete) {
            if (!onComplete) onComplete = noop;
            job.start();
        }
    """),
    hint="Type onComplete once, in the cw that renames cb. Register . holds the text you typed last, so "
         "in the new line, Ctrl-r . types it twice more without leaving Insert mode.",
    uses=["c", "word", "count", "o", "ctrl-r"],
)

# ---------- Ctrl-r Ctrl-w ----------

ctrl_r_ctrl_w = drills.command(
    "ctrl-r-ctrl-w", "Ctrl-r Ctrl-w  Ctrl-r Ctrl-a", "the word under the cursor, on the command line",
    """On the : or / command line, Ctrl-r Ctrl-w types the word under the cursor in your file, and Ctrl-r
    Ctrl-a types the WORD, everything between spaces (config.timeout, ops@example.com). So a rename never
    needs the long name typed: with the cursor on the new name, :%s/old/Ctrl-r Ctrl-w types it as the
    replacement. When the word under the cursor is the one you're replacing, * followed by :%s//new (an
    empty pattern means the last search) is a key shorter.""",
    examples=[(":%s/old/Ctrl-r Ctrl-w", "replace old with the word under the cursor"),
              (":%s/Ctrl-r Ctrl-a/new", "replace the WORD under the cursor"),
              ("/Ctrl-r Ctrl-a", "search for the WORD under the cursor")],
    level="complex",
)
ctrl_r_ctrl_w.add(
    title="Rename to the variable", par=14, ext="java",
    task="The limit is now in maxAttempts. Replace each tries with maxAttempts.",
    start=text("""
        int maxAttempts = 5;
        for (int i = 0; i < tries; i++) {
            if (i == tries - 1) log.warn("last try");
        }
    """),
    target=text("""
        int maxAttempts = 5;
        for (int i = 0; i < maxAttempts; i++) {
            if (i == maxAttempts - 1) log.warn("last try");
        }
    """),
    hint="Put the cursor on maxAttempts and type :%s/tries/. Ctrl-r Ctrl-w types the word under the "
         "cursor as the replacement.",
    uses=["subst", "range", "word"],
)
ctrl_r_ctrl_w.add(
    title="Use the local variable", par=19, ext="py",
    task="Lines 2 and 3 should use the local timeout instead of config.timeout_seconds. Line 1 stays.",
    start=text("""
        timeout = config.timeout_seconds
        connect(host, config.timeout_seconds)
        retry(config.timeout_seconds * 2)
    """),
    target=text("""
        timeout = config.timeout_seconds
        connect(host, timeout)
        retry(timeout * 2)
    """),
    hint="With the cursor on config.timeout_seconds in line 1, Ctrl-r Ctrl-a types that whole WORD into the "
         "command line (Ctrl-r Ctrl-w would stop at the dot). Run the substitute on lines 2 to the end: "
         ":2,$s/.",
    uses=["subst", "range", "bigword"],
)
ctrl_r_ctrl_w.add(
    title="Fill in the address", par=15, ext="md",
    task="Replace each OWNER with the address from line 1, help-desk@garden.dev.",
    start=text("""
        Questions go to help-desk@garden.dev now.
        - Billing: email OWNER
        - Outages: email OWNER
    """),
    target=text("""
        Questions go to help-desk@garden.dev now.
        - Billing: email help-desk@garden.dev
        - Outages: email help-desk@garden.dev
    """),
    hint="Put the cursor on the address and type :%s/OWNER/. The address isn't one word (- and @ split it), "
         "but it's one WORD, so Ctrl-r Ctrl-a types all of it.",
    uses=["subst", "range", "bigword"],
)
ctrl_r_ctrl_w.add(
    title="Just this request", par=11, ext="log",
    task="Keep only the log lines for request req-7f3a91, the one on line 1. Delete every other line.",
    start=text("""
        req-7f3a91 GET /api/cart 200 12ms
        req-7f3a19 GET /api/user 200 8ms
        req-7f3a91 SELECT carts 4ms
        req-97f3a1 POST /api/login 302 31ms
        req-7f3a91 SELECT items 6ms
        req-7f9a91 GET /health 200 1ms
        req-3a917f GET /api/cart 500 40ms
        req-7f3a91 cache miss: cart:12
        req-7f3a19 SELECT users 3ms
    """),
    target=text("""
        req-7f3a91 GET /api/cart 200 12ms
        req-7f3a91 SELECT carts 4ms
        req-7f3a91 SELECT items 6ms
        req-7f3a91 cache miss: cart:12
    """),
    hint="Filter the whole file through grep, which keeps the lines that match: :%!grep and the id. The "
         "cursor is on it, and it's one WORD, so Ctrl-r Ctrl-a types all of it.",
    uses=["filter", "range", "bigword"],
)
ctrl_r_ctrl_w.add(
    title="Decimal first, hex in a comment", par=35, ext="c",
    task="Write each base address in decimal, and keep the hex in a comment after it: "
         "#define SRAM_BASE   536870912 /* 0x20000000 */, and the same for PERIPH_BASE (1073741824).",
    start=text("""
        #define SRAM_BASE   0x20000000
        #define PERIPH_BASE 0x40000000
    """),
    target=text("""
        #define SRAM_BASE   536870912 /* 0x20000000 */
        #define PERIPH_BASE 1073741824 /* 0x40000000 */
    """),
    hint="The Ctrl-r = prompt is a command line too, and Ctrl-r Ctrl-w there types the word under the "
         "cursor. So insert in front of the hex number (i), get its value with Ctrl-r = Ctrl-r Ctrl-w, "
         "and type the comment around the number that's still there.",
    uses=["expr", "insert", "line", "word", "count"],
)
ctrl_r_ctrl_w.add(
    title="From state to a hook", par=14, ext="js", cursor=(2, 18),
    task="This component now gets count from a hook: replace every this.state.count with count. Leave "
         "this.state.total and this.props.count alone. The cursor starts on this.state.count in line 2.",
    start=text("""
        increment() {
            const next = this.state.count + 1;
            this.setState({ count: next, total: this.state.total + 1 });
            if (next > this.props.count) log("over", this.state.count);
            return this.state.count * 2;
        }

        reset() {
            this.setState({ count: 0, last: this.state.count });
        }
    """),
    target=text("""
        increment() {
            const next = count + 1;
            this.setState({ count: next, total: this.state.total + 1 });
            if (next > this.props.count) log("over", count);
            return count * 2;
        }

        reset() {
            this.setState({ count: 0, last: count });
        }
    """),
    hint="* would search for the word count, which this.props.count has too. / and Ctrl-r Ctrl-a search "
         "for the whole WORD instead. At each match, d2f. deletes this.state., and n. does the next one.",
    uses=["search", "d", "f", "count", "dot"],
)
