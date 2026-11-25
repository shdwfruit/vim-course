"""What the maps in mapview.py are painted with: pixel sprites (trees, landmarks, level markers), each
island's colors and scenery, smooth noise for terrain, and the small animations that play over a map.

A pixel is half a character cell (mapview's Canvas draws two per cell with ▀), so pixels are about square.
Colors are xterm's 256. This file only paints onto a canvas: anything with dot(x, y, color) and shade().
"""
import math


# ---------- colors ----------

def rgb(n):
    if n < 16:
        return [(0, 0, 0), (205, 0, 0), (0, 205, 0), (205, 205, 0), (0, 0, 238), (205, 0, 205), (0, 205, 205),
                (229, 229, 229), (127, 127, 127), (255, 0, 0), (0, 255, 0), (255, 255, 0), (92, 92, 255),
                (255, 0, 255), (0, 255, 255), (255, 255, 255)][n]
    if n < 232:
        n, levels = n - 16, (0, 95, 135, 175, 215, 255)
        return levels[n // 36], levels[n // 6 % 6], levels[n % 6]
    return (8 + 10 * (n - 232),) * 3


def _nearest(r, g, b):
    return min(range(16, 256), key=lambda n: sum((p - q) ** 2 for p, q in zip(rgb(n), (r, g, b))))


def _table(change):
    return [_nearest(*change(*rgb(n))) for n in range(256)]


_TABLES = {}


def table(name):
    """A color -> color table: "grey" (fog: washed out) or "dark" (in shadow). Built the first time."""
    if name not in _TABLES:
        if name == "grey":
            def change(r, g, b):
                v = (r * 3 + g * 6 + b) / 10
                return [v * 0.55 + 70 + (p - v) * 0.12 for p in (r, g, b)]
        else:
            def change(r, g, b):
                return r * 0.72, g * 0.72, b * 0.78
        _TABLES[name] = _table(change)
    return _TABLES[name]


# ---------- noise ----------

def rand(x, y, seed):
    """A fixed number from 0 to 1 for whole numbers x, y."""
    n = (x * 374761393 + y * 668265263 + seed * 2147483647) & 0xffffffff
    n = ((n ^ (n >> 13)) * 1274126177) & 0xffffffff
    return ((n ^ (n >> 16)) & 0xffff) / 65535


def noise(x, y, seed):
    """Smooth noise from 0 to 1: nearby x, y give nearby values. Terrain comes from this."""
    x0, y0 = math.floor(x), math.floor(y)
    fx, fy = x - x0, y - y0
    fx, fy = fx * fx * (3 - 2 * fx), fy * fy * (3 - 2 * fy)
    a, b, c, d = rand(x0, y0, seed), rand(x0 + 1, y0, seed), rand(x0, y0 + 1, seed), rand(x0 + 1, y0 + 1, seed)
    return a + (b - a) * fx + (c - a) * fy + (a - b - c + d) * fx * fy


# ---------- sprites ----------

class Sprite:
    """Pixel art: rows of letters, each letter a color ("." is see-through). blink: letters that cycle
    through colors, for lights and lava."""

    def __init__(self, rows, blink=None, **colors):
        self.rows, self.colors, self.blink = rows.split(), colors, blink or {}
        self.w, self.h = max(map(len, self.rows)), len(self.rows)

    def small(self):
        """The same picture at half the size, for the small islands on the sea map."""
        tiny = Sprite("x", self.blink, **self.colors)
        tiny.rows = [row[::2] for row in self.rows[::2]]
        tiny.w, tiny.h = max(map(len, tiny.rows)), len(tiny.rows)
        return tiny

    def pixels(self, x, y, scale=1, swap=None):
        """((px, py), letter, color) for every pixel, drawn with its top-left corner at x, y."""
        for r, row in enumerate(self.rows):
            for c, letter in enumerate(row):
                if letter != ".":
                    color = (swap or {}).get(letter, self.colors[letter])
                    for dy in range(scale):
                        for dx in range(scale):
                            yield (x + c * scale + dx, y + r * scale + dy), letter, color

    def stamp(self, canvas, x, y, scale=1, swap=None):
        """Draw it. Returns the blinking pixels as [(px, py, colors)]."""
        lights = []
        for (px, py), letter, color in self.pixels(x, y, scale, swap):
            canvas.dot(px, py, color)
            if letter in self.blink:
                lights.append((px, py, self.blink[letter]))
        return lights


# Small scenery. G g: leaves, T: trunk.
SPRITES = dict(
    tree=Sprite(".GG. GGGG GgGG .TT.", G=28, g=22, T=94),
    bush=Sprite(".G. GgG", G=34, g=28),
    pine=Sprite(".P. PPP .P. PPP .T.", P=22, T=94),
    snowpine=Sprite(".W. PWP .P. PPP .T.", P=23, W=231, T=94),
    cactus=Sprite("C.C CCC .C. .C.", C=28),
    palm=Sprite("G.G.G .GGG. ..T.. ..T..", G=34, T=137),
    rock=Sprite(".RR RRr", R=245, r=240),
    redrock=Sprite(".R. RRr RRr", R=130, r=94),
    mesa=Sprite(".RRR. RRRRr RRRRr", R=167, r=94),
    snowman=Sprite(".W. .W. WWW", W=231),
    deadtree=Sprite("T.T .TT .T. .T.", T=58),
    reeds=Sprite("r.r r.r RrR", R=64, r=100),
    lily=Sprite("LL", L=77),
    charred=Sprite("K.K .K. .K.", K=233),
    spire=Sprite(".S. .S. SSs", S=235, s=232),
    emberrock=Sprite(".E. RRR", E=202, R=236, blink=dict(E=(202, 208, 166))),
    crystal=Sprite(".c. cCc cCc", C=51, c=159),
    pinkcrystal=Sprite(".c. cCc cCc", C=213, c=225),
    gem=Sprite("C", C=147, blink=dict(C=(147, 231, 147, 105))),
    puff=Sprite(".WWW. WWWWW", W=195),
    column=Sprite("GGG .G. .G. GGG", G=222),
    star=Sprite("S", S=228, blink=dict(S=(228, 231, 222))),
    house=Sprite(".RR. RRRR WYWW WWDW", R=95, W=102, Y=221, D=236, blink=dict(Y=(221, 221, 221, 179))),
    lamp=Sprite("Y P P", Y=226, P=240, blink=dict(Y=(226, 220))),
    darktree=Sprite(".GG. GGGG .TT.", G=23, T=236),
    pillar=Sprite("SSS .S. .S. SSS", S=247),
    tomb=Sprite(".S. SSS SSS", S=244),
    bones=Sprite("W.W .W.", W=253),
    torch=Sprite("F P P", F=208, P=94, blink=dict(F=(208, 214, 202))),
    flower=Sprite("F", F=218),
    yellowflower=Sprite("F", F=227),
    tuft=Sprite("g.g", g=64),
    drytuft=Sprite("g.g", g=137),
    mushroom=Sprite("RR .W", R=160, W=230),
)

# Landmarks: one per island.
LANDMARKS = dict(
    oak=Sprite("""
        ....GGGGGGG....
        ..GGGGgGGGGGG..
        .GGgGGGGGaGgGG.
        GGGGGGgGGGGGGGG
        GGaGGGGGGGGgGGG
        .GGGGGgGGGaGGG.
        ..GGGGGGGGGGG..
        ....GGTTTGG....
        ......TTT......
        ......TtT......
        ......TTT......
        .....TTTTT.....
        ....TT.T.TT....""", G=34, g=22, T=94, t=58, a=196),
    tower=Sprite("""
        ...RRRRR...
        ..RRRRRRR..
        ...WWWWW...
        ...WyWyW...
        ...WWWWW...
        ....T.T....
        ....TTT....
        ....T.T....
        ....TTT....
        ....T.T....
        ...TT.TT...""", R=124, W=137, y=220, T=94, blink=dict(y=(220, 220, 214, 220))),
    pyramid=Sprite("""
        .........Y.........
        ........YYy........
        .......YYYyy.......
        ......YYYYyyy......
        .....YYYYYyyyy.....
        ....YYYYYYyyyyy....
        ...YYYYYYYyyyyyy...
        ..YYYYYYYDyyyyyyy..
        .YYYYYYYYDyyyyyyyy.""", Y=221, y=136, D=52),
    igloo=Sprite("""
        ....WWWWW....
        ..WWWwWWWWW..
        .WWwWWWWwWWW.
        WWWWWwWWWWWWW
        WWwWWDDDWWwWW
        WWWWWDDDWWWWW""", W=195, w=110, D=24),
    arch=Sprite("""
        ..RRRRRRRRRRR..
        .RRRrRRRRRrRRR.
        RRRRRRRRRRRRRRR
        RRRr.......rRRR
        RRR.........RRR
        RRr.........rRR
        RRR.........RRR
        RRR.........RRR""", R=130, r=94),
    wreck=Sprite("""
        ......M..........
        ......M..........
        .....sMs.........
        ....ssMss........
        ......M.....H....
        .HH...M....HH....
        .HHHHHHHHHHHH....
        ..HHhHHHhHHH.....
        ...HHHHHHHH......""", M=94, s=187, H=95, h=52),
    crater=Sprite("""
        ......rLLLr......
        .....rLYLLLr.....
        ....DDrLLLrDD....
        ...DDDDdddDDDD...
        ..DDDdDDDDDdDDD..
        .DDDDDDLDDDDDDD..
        DDDdDDDLLDDDdDDD.
        DDDDDDDDLLDDDDDDD""", D=236, d=233, L=202, Y=226, r=124,
                  blink=dict(Y=(226, 220, 214, 220), L=(202, 202, 208, 202, 196))),
    spires=Sprite("""
        ......C......
        .....CcC.....
        .....CcC.....
        ..C..CcC..P..
        .CcC.CcC.PpP.
        .CcC.CcC.PpP.
        .CcCCCcCCPpP.
        .CcCCCcCCPpP.
        CCcCCCcCCPpPP""", C=45, c=195, P=213, p=225, blink=dict(c=(195, 195, 231, 195, 159))),
    castle=Sprite("""
        .B...........B.
        BBB....B....BBB
        BBB...BBB...BBB
        GGG...GGG...GGG
        GGGGGGGGGGGGGGG
        GgGGGgGGGgGGGgG
        GGGGGGDDDGGGGGG
        GGGGGGDDDGGGGGG""", B=33, G=222, g=179, D=94),
    lighthouse=Sprite("""
        ...YYY...
        ..YYYYY..
        ...WWW...
        ...RRR...
        ...WWW...
        ...RRR...
        ...WWW...
        ...RRR...
        ..WWWWW..
        ..WWDWW..
        .SSSSSSS.""", W=255, R=160, Y=226, S=244, D=94, blink=dict(Y=(226, 226, 228, 58, 58, 228))),
    skull=Sprite("""
        ...WWWWWWWWW...
        ..WWWWWWWWWWW..
        .WWWWWWWWWWWWW.
        WWWWWWWWWWWWWWW
        WWKKKKWWWKKKKWW
        WWKKRKWWWKRKKWW
        WWKKKKWWWKKKKWW
        WWWWWWWKWWWWWWW
        .WWWWWKKKWWWWW.
        ..WWWWWWWWWWW..
        ..WKWKWKWKWKW..
        ...W.W.W.W.W...""", W=253, K=16, R=196, blink=dict(R=(196, 196, 160, 88, 160))),
)

# Level markers, 5 pixels wide and 4 tall. C is the level's color (its mark), k the outline.
MARKERS = dict(
    level=Sprite(".kkk. kCCCk kCCCk .kkk.", C=250, k=16),
    boss=Sprite("C.C.C CCCCC CkCkC CCkCC", C=250, k=16),  # a little castle
    skull=Sprite(".CCC. CkCkC CCCCC .CkC.", C=250, k=16),  # the fortress's bosses
)
CAMP = Sprite("..T.. .TTT. TTkTT TTkTT", T=208, k=52)  # the training camp's tent, at the end of the road
FLAG = Sprite("pFF pFF p.. p..", p=252, F=41)  # planted on a solved level; gold at par


# ---------- islands ----------

# shades: the land, dark to light. beach, shallow (water by the shore), sea, wave. water: ponds and rivers.
# trees: what its forests are made of. bits: what's scattered between them. forest: how much of it is forest.
THEMES = [
    dict(name="meadow", shades=(64, 71, 113), beach=186, shallow=32, sea=25, wave=39, trail=230, water=39,
         trees=("tree", "tree", "bush"), bits=("flower", "yellowflower", "tuft", "tuft"), forest=0.4,
         landmark="oak", ambient=("shadows",)),
    dict(name="pine forest", shades=(23, 29, 35), beach=143, shallow=31, sea=24, wave=38, trail=223, water=38,
         trees=("pine",), bits=("mushroom", "rock", "tuft"), forest=0.55, landmark="tower", ambient=("fireflies",)),
    dict(name="dunes", shades=(180, 179, 222), beach=229, shallow=37, sea=30, wave=80, trail=231, water=44,
         trees=("cactus", "palm"), bits=("rock", "drytuft", "drytuft"), forest=0.14, landmark="pyramid",
         ambient=("wind",)),
    dict(name="snowfield", shades=(250, 254, 231), beach=195, shallow=74, sea=67, wave=153, trail=60, water=117,
         trees=("snowpine",), bits=("snowman", "rock"), forest=0.3, landmark="igloo", ambient=("snow",)),
    dict(name="canyon", shades=(131, 173, 216), beach=180, shallow=37, sea=31, wave=80, trail=230, water=37,
         trees=("mesa", "redrock"), bits=("cactus", "drytuft", "redrock"), forest=0.25, landmark="arch",
         ambient=("wind",)),
    dict(name="marsh", shades=(58, 65, 101), beach=100, shallow=29, sea=23, wave=36, trail=187, water=30,
         trees=("deadtree", "bush"), bits=("reeds", "reeds", "lily", "tuft"), forest=0.3, landmark="wreck",
         ambient=("fireflies",), ponds=4),
    dict(name="volcano", shades=(235, 239, 242), beach=52, shallow=160, sea=124, wave=208, trail=214, water=202,
         trees=("spire", "charred"), bits=("emberrock", "rock"), forest=0.25, landmark="crater",
         ambient=("embers",)),
    dict(name="crystal caverns", shades=(54, 60, 97), beach=103, shallow=18, sea=17, wave=62, trail=189, water=51,
         trees=("crystal", "pinkcrystal"), bits=("gem", "gem", "rock"), forest=0.3, landmark="spires",
         ambient=("twinkle",)),
    dict(name="cloud kingdom", shades=(189, 255, 231), beach=153, shallow=75, sea=39, wave=117, trail=67, water=117,
         trees=("puff", "column"), bits=("star", "star"), forest=0.25, landmark="castle", ambient=("wind",)),
    dict(name="twilight town", shades=(238, 60, 61), beach=59, shallow=18, sea=17, wave=25, trail=229, water=25,
         trees=("house", "darktree"), bits=("lamp", "darktree"), forest=0.35, landmark="lighthouse",
         ambient=("fireflies",)),
    dict(name="fortress", shades=(236, 240, 243), beach=234, shallow=88, sea=52, wave=160, trail=220, water=124,
         trees=("pillar", "tomb", "deadtree"), bits=("bones", "torch", "rock"), forest=0.28, landmark="skull",
         ambient=("embers",)),
]


def blob(cx, cy, rx, ry, rng):
    """The pixels of one island: an ellipse whose edge swells and dips with a few random waves, so no two
    islands have the same coast."""
    waves = [(rng.choice((2, 3, 4, 5, 6)), rng.uniform(0.05, 0.13), rng.uniform(0, 2 * math.pi)) for _ in range(3)]
    cells = set()
    for y in range(int(cy - ry * 1.4) - 1, int(cy + ry * 1.4) + 2):
        for x in range(int(cx - rx * 1.4) - 1, int(cx + rx * 1.4) + 2):
            dx, dy = (x - cx) / rx, (y - cy) / ry
            if math.hypot(dx, dy) < 1 + sum(a * math.sin(k * math.atan2(dy, dx) + p) for k, a, p in waves):
                cells.add((x, y))
    return cells


def curve(a, b, bend):
    """The pixels of a path from a to b that bows out to one side by `bend` of its length (0 is straight)."""
    (x0, y0), (x1, y1) = a, b
    cx, cy = (x0 + x1) / 2 - (y1 - y0) * bend, (y0 + y1) / 2 + (x1 - x0) * bend
    steps, path = int(max(abs(x1 - x0), abs(y1 - y0)) * 1.5) + 2, []
    for i in range(steps + 1):
        t = i / steps
        p = (round((1 - t) ** 2 * x0 + 2 * t * (1 - t) * cx + t * t * x1),
             round((1 - t) ** 2 * y0 + 2 * t * (1 - t) * cy + t * t * y1))
        if not path or p != path[-1]:
            path.append(p)
    return path


def paint_island(canvas, land, theme, seed, rng, keep_clear, roads, landmark_at=None, scale=1, mark=None):
    """Paint one island onto canvas: shaded land with a beach, ponds and a river, forests, scattered
    scenery and its landmark. land: its pixels. keep_clear: pixels nothing may be put on (markers, labels).
    roads: [(pixels, walked)], drawn over it all, with bridges where they cross water.
    Returns (pixels that blink as [(x, y, colors)], the landmark's box (x, y, w, h) or None)."""
    coast = {p for p in land if any(q not in land for q in ((p[0] + 1, p[1]), (p[0] - 1, p[1]),
                                                             (p[0], p[1] + 1), (p[0], p[1] - 1)))}
    beach = set(coast)
    for x, y in coast:  # the beach is wider in some places than others
        if noise(x / 5, y / 5, seed + 5) > 0.4:
            beach |= {q for q in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)) if q in land}
    for x, y in coast:  # shallow water around it
        for dx in range(-2, 3):
            for dy in (-1, 0, 1):
                if (x + dx, y + dy) not in land:
                    canvas.dot(x + dx, y + dy, theme["shallow"])
    dark, mid, light = theme["shades"]
    for x, y in land:
        n = noise(x / 8, y / 6, seed)
        canvas.dot(x, y, theme["beach"] if (x, y) in beach else dark if n < 0.36 else mid if n < 0.68 else light)

    road = {p for pixels, _ in roads for p in pixels}
    busy = set(keep_clear) | {(x + dx, y + dy) for x, y in road for dx in (-1, 0, 1) for dy in (-1, 0, 1)}
    inland = land - beach
    lights, box = [], None

    mark = mark or LANDMARKS[theme["landmark"]]
    if landmark_at:
        lx, ly = landmark_at
        lights += mark.stamp(canvas, lx, ly, scale)
        box = (lx, ly, mark.w * scale, mark.h * scale)
        busy |= {(lx + dx, ly + dy) for dx in range(-1, box[2] + 1) for dy in range(-1, box[3] + 1)}

    water = set()
    spots = sorted(inland - busy)
    for k in range(theme.get("ponds", 2) if len(spots) > 400 else 1 if len(spots) > 150 else 0):
        if not spots:
            break
        cx, cy = rng.choice(spots)
        pond = blob(cx, cy, rng.uniform(2.5, 5), rng.uniform(1.5, 3), rng) & inland
        if k == 0:  # the first pond has a river running to the sea
            angle, x, y = rng.uniform(0, 2 * math.pi), float(cx), float(cy)
            for step in range(200):
                if (round(x), round(y)) not in land:
                    break
                pond |= {(round(x), round(y)), (round(x) + 1, round(y))} & land
                turn = angle + 0.9 * math.sin(step / 5 + seed)
                x, y = x + math.cos(turn), y + math.sin(turn) * 0.8
        water |= pond - keep_clear - (set() if box is None else
                                      {(box[0] + dx, box[1] + dy) for dx in range(box[2]) for dy in range(box[3])})
    for x, y in water:
        canvas.dot(x, y, theme["water"])
    busy |= water

    def fits(sprite, x, y):
        cells = [p for p, _, _ in sprite.pixels(x, y)]
        return all(p in inland and p not in busy for p in cells), cells

    xs, ys = [p[0] for p in land], [p[1] for p in land]
    for y in range(min(ys), max(ys), 3):
        for x in range(min(xs), max(xs), 4):
            x1, y1 = x + rng.randint(0, 2), y + rng.randint(0, 1)
            wooded = noise(x / 11, y / 8, seed + 9) > 1 - theme["forest"]
            if wooded or rng.random() < 0.13:
                sprite = SPRITES[rng.choice(theme["trees"] if wooded else theme["bits"])]
                ok, cells = fits(sprite, x1, y1)
                if ok:
                    lights += sprite.stamp(canvas, x1, y1)
                    busy |= set(cells)

    for pixels, walked in roads:  # walked roads are solid, the rest dashed; a bridge where one crosses water
        for i, (x, y) in enumerate(pixels):
            if (x, y) in water:
                for dy in (-1, 0, 1):
                    canvas.dot(x, y + dy, 94 if dy else 180)
            elif walked or i % 4 < 2:
                canvas.dot(x, y, theme["trail"])
    return lights, box


def landmark_spot(land, mark, avoid, scale=1):
    """Where a landmark fits best: on land, as far from the roads and markers as it can be.
    Returns its top-left corner, or None if there's no room."""
    w, h = mark.w * scale, mark.h * scale
    xs, ys = [p[0] for p in land], [p[1] for p in land]
    avoid = list(avoid)[::2] or [(10 ** 6, 10 ** 6)]
    best = None
    for y in range(min(ys) + 1, max(ys) - h, 2):
        for x in range(min(xs) + 1, max(xs) - w, 2):
            corners = [(x - 1, y - 1), (x + w, y - 1), (x - 1, y + h), (x + w, y + h), (x + w // 2, y + h // 2),
                       (x + w // 2, y - 1), (x + w // 2, y + h), (x - 1, y + h // 2), (x + w, y + h // 2)]
            if all(p in land for p in corners):
                cx, cy = x + w / 2, y + h / 2
                room = min(max(abs(px - cx) - w / 2, abs(py - cy) - h / 2) for px, py in avoid)
                if room >= 1 and (best is None or room > best[0]):
                    best = (room, x, y)
    return best and best[1:]


# ---------- things that move ----------

def ambient(canvas, kind, frame, x0, y0, x1, y1, seed):
    """One frame of an island's weather, over the pixels from x0, y0 to x1, y1."""
    w, h = x1 - x0, y1 - y0
    if w <= 0 or h <= 0:
        return
    n = max(3, w * h // 110)
    if kind == "snow":
        for k in range(n):
            x = (rand(k, 1, seed) * w + frame * (rand(k, 3, seed) - 0.5) * 0.6) % w
            y = (rand(k, 2, seed) * h + frame * (0.5 + rand(k, 4, seed))) % h
            canvas.dot(x0 + int(x), y0 + int(y), 231)
    elif kind == "embers":
        for k in range(n // 2):
            x = (rand(k, 1, seed) * w + math.sin(frame / 3 + k) * 1.5) % w
            y = (rand(k, 2, seed) * h - frame * (0.4 + rand(k, 4, seed) * 0.6)) % h
            canvas.dot(x0 + int(x), y0 + int(y), (208, 214, 202, 196)[(k + frame // 2) % 4])
    elif kind in ("fireflies", "twinkle"):
        for k in range(n // 2):
            if rand(k, frame // 3, seed) > 0.62:
                canvas.dot(x0 + int(rand(k, 1, seed) * w), y0 + int(rand(k, 2, seed) * h),
                           226 if kind == "fireflies" else (231, 195, 225)[k % 3])
    elif kind == "wind":
        for k in range(max(2, n // 6)):
            x = int(rand(k, 1, seed) * w + frame * (1.5 + rand(k, 3, seed))) % w
            y = y0 + int(rand(k, 2, seed) * h)
            for dx in range(3 + k % 3):
                canvas.dot(x0 + (x + dx) % w, y, 231)
    elif kind == "shadows":
        for k in range(2):  # cloud shadows drifting across
            cx = (rand(k, 1, seed) * w + frame * 0.7) % (w + 30) - 15
            cy, rx, ry = rand(k, 2, seed) * h, 9 + 4 * k, 3 + k
            for y in range(int(cy - ry), int(cy + ry) + 1):
                half = rx * math.sqrt(max(0, 1 - ((y - cy) / ry) ** 2))
                for x in range(int(cx - half), int(cx + half) + 1):
                    if x0 <= x0 + x < x1 and y0 <= y0 + y < y1:
                        canvas.shade(x0 + x, y0 + y, "dark")


def fireworks(canvas, step, x, y, seed):
    """One frame (step 0 to about 34) of fireworks bursting above x, y."""
    for b in range(6):
        age = step - b * 4
        if 0 <= age < 12:
            bx, by = x + int((rand(b, 1, seed) - 0.5) * 34), y - 4 - int(rand(b, 2, seed) * 12)
            color = (226, 213, 51, 46, 208, 231)[b] if age < 8 else (240, 238)[age % 2]
            for k in range(14):
                r = 1 + age * 0.9
                canvas.dot(bx + round(math.cos(k * 0.449) * r), by + round(math.sin(k * 0.449) * r + age * age * 0.03),
                           color)
