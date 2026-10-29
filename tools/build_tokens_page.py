"""Build 08-design-tokens/tokens.html — phase 08's page, in the same design language as phases 01–07.

Like ui.html it lifts the shared <style> block and the scroll-spy out of research-page.tpl.html at build time,
so the phase pages cannot drift. Its own content is tokens-page.tpl.html; the counts are read out of
08-design-tokens/tokens.css, components/ and the mockups folder, and the showcase and the screens are embedded live.

    python tools/build_tokens_page.py
"""
import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SHARED = os.path.join(HERE, "research-page.tpl.html")
TPL = os.path.join(HERE, "tokens-page.tpl.html")
SRC = os.path.join(ROOT, "08-design-tokens")
DST = os.path.join(SRC, "tokens.html")

shared = io.open(SHARED, encoding="utf-8").read()
tpl = io.open(TPL, encoding="utf-8").read()
tokens = io.open(os.path.join(SRC, "tokens.css"), encoding="utf-8").read()

i = shared.index("</style>") + len("</style>")
shared_head = re.sub(r"<title>.*?</title>\s*", "", shared[:i].strip(), count=1, flags=re.S)
m = re.search(r"\(function\(\)\{\s*\n\s*var links = .*?\}\)\(\);", shared, re.S)
if not m:
    raise SystemExit("scroll-spy not found in the shared template")
spy = m.group(0)
j = tpl.index("</style>") + len("</style>")
page_head, page_body = tpl[:j].strip(), tpl[j:].strip()


def block(opener):
    """The body of the first rule that opens with `opener`, up to its closing brace at column 0."""
    a = tokens.index(opener)
    return tokens[a:tokens.index("\n}", a)]


DECL = r"^\s*(--[\w-]+)\s*:\s*([^;]+);"
root = block(":root {")
prim = root[root.index("===== PRIMITIVE"):root.index("===== SEMANTIC")]
sem = root[root.index("===== SEMANTIC"):]
recipes = block(":root, [data-theme] {")
light = block('[data-theme="light"] {')

prims = re.findall(DECL, prim, re.M)
n_prim = len(prims)
n_prim_colour = len([1 for _, v in prims if re.match(r"#|rgba?\(", v.strip())])
n_sem = len(re.findall(DECL, sem, re.M)) + len(re.findall(DECL, recipes, re.M))
lights = re.findall(DECL, light, re.M)
n_light = len(lights)
for name, v in lights:  # the stress test's own rule, re-checked where the page claims it
    assert "#" not in v and not re.search(r"rgba?\(", v), "a literal in the light block: " + name
PAIR = r"^\s+[\d.]+ (AA|info)\s"  # every measured pair; a tag's outline is written as information, not as a claim
dark_p, light_p = re.findall(PAIR, root, re.M), re.findall(PAIR, light, re.M)
assert len(dark_p) == len(light_p) > 0, "pairs per theme differ: %d dark, %d light" % (len(dark_p), len(light_p))
assert dark_p.count("info") == light_p.count("info"), "information pairs differ between themes"
assert not re.search(r"^\s+[\d.]+ fail", tokens, re.M | re.I), "a pair below AA"
n_pairs, n_info = len(dark_p), dark_p.count("info")

# ---- the layers: primitive colour, primitive geometry, semantic colour, contrast — every block folds ----
import html as _html
import sys as _sys
_sys.path.insert(0, HERE)
import concept_tokens as ct  # noqa: E402  the same module that writes tokens.css: its resolver and its contrast pairs

LINE = r"^\s*(--[\w-]+)\s*:\s*([^;]+);\s*(?:/\*\s*(.*?)\s*\*/)?\s*$"
esc = lambda s: _html.escape(s, quote=True)


def decls(text):
    return [(n, v.strip(), (c or "").strip()) for n, v, c in re.findall(LINE, text, re.M)]


def many(n, word):
    return "%d %s%s" % (n, word, "" if n == 1 else "s")


def block(title, count, desc, body, open_=True, cls=""):
    return ('<details class="tm%s"%s><summary><span class="tm-t">%s</span><span class="tm-n">%s</span>'
            '<span class="tm-d">%s</span></summary><div class="tm-body">%s</div></details>'
            % (" " + cls if cls else "", " open" if open_ else "", title, count, desc, body))


def swatch(value, big=False):
    return '<i class="sw%s%s" style="--sw:%s"></i>' % (" a" if value.startswith("rgba") else "", " big" if big else "", value)


vals = {t: ct._theme_values(tokens, t) for t in ("dark", "light")}


def hexof(t, name):
    """A role's value in a theme, as a hex — or the primitive's own value when it is an alpha the resolver leaves."""
    try:
        return "#%02X%02X%02X" % ct.colour(vals[t], "var(--%s)" % name)
    except (ValueError, KeyError):
        v = vals[t][name]
        while v.startswith("var("):
            v = vals[t][v[6:-1]]
        return v

prim_colour = [(n, v, c) for n, v, c in decls(prim) if re.match(r"#|rgba?\(", v)]
prim_value = {n: v for n, v, _ in prim_colour}
sem_rows = decls(sem)
sem_light = {n: (v, c) for n, v, c in decls(light)}
target = lambda v: (re.fullmatch(r"var\((--[\w-]+)\)", v) or [None, None])[1]

# who reads each primitive, per theme
readers = {"dark": {}, "light": {}}
for n, v, _ in sem_rows:
    readers["dark"].setdefault(target(v), []).append(n)
    readers["light"].setdefault(target(sem_light[n][0]) if n in sem_light else target(v), []).append(n)
for n, v, _ in decls(recipes):
    for r in re.findall(r"var\((--color-[\w-]+)\)", v):
        readers["dark"].setdefault(r, []).append(n)
for n, (v, _) in sem_light.items():
    for r in re.findall(r"var\((--color-[\w-]+)\)", v):
        if not any(n == x for x, *_ in sem_rows):
            readers["light"].setdefault(r, []).append(n)

# ---- 1. primitive colour: cards by hue, the dark scale and the light-only one apart ----
HUES = [("neutral", "Neutral", "the style's Mica greys: grounds, layers, lines, text"),
        ("lime", "Lime", "the act and the mark"), ("rose", "Rose", "a Problem"),
        ("amber", "Amber", "a Note, and going ahead despite a Problem"), ("red", "Red", "removing"),
        ("white", "White, black and alpha", "ink on a fill, highlights, shadows, glass, the veil")]


def hue_key(name):
    h = name[len("--color-"):].split("-")[0]
    return "white" if h in ("white", "black") or re.search(r"-a\d+$", name) else h


def card(n, v):
    lines = []
    for t in ("dark", "light"):
        r = sorted(set(readers[t].get(n, [])))
        if r:
            lines.append('<span class="rd"><b>%s</b> %s</span>' % (t, " ".join("<code>%s</code>" % x for x in r)))
    return ('<div class="card-sw">%s<code class="nm">%s</code><code class="hx">%s</code>%s</div>'
            % (swatch(v, True), n, esc(v), "".join(lines) or '<span class="rd none">no role reads it</span>'))


prim_html = ""
for key, label, desc in HUES:
    rows = [(n, v) for n, v, _ in prim_colour if hue_key(n) == key]
    dark_rows = [r for r in rows if "-light-" not in r[0]]
    light_rows = [r for r in rows if "-light-" in r[0]]
    body = ""
    if dark_rows:
        body += '<p class="sub">Dark scale%s</p><div class="cards">%s</div>' % (
            "" if key == "white" else " &mdash; 50 is the lightest", "".join(card(*r) for r in dark_rows))
    if light_rows:
        body += '<p class="sub">Light only &mdash; read by the light theme alone</p><div class="cards">%s</div>' % "".join(card(*r) for r in light_rows)
    strip = "".join(swatch(v) for _, v in rows)
    prim_html += block('%s <span class="tm-strip">%s</span>' % (label, strip), many(len(rows), "primitive"), desc, body)
n_prim_dark = len([1 for n, _, _ in prim_colour if "-light-" not in n])

# ---- 2. primitive geometry: each group with a preview that shows the value instead of describing it ----
GEO = [("Space", "the 4 px scale", lambda n: n.startswith("--space-")),
       ("Radius", "corners", lambda n: n.startswith("--radius-")),
       ("Type scale", "size / line height, weight, family", lambda n: n.startswith("--typescale-")),
       ("Family, weight, tracking", "the faces and their settings", lambda n: n.startswith(("--font-", "--tracking-"))),
       ("Border width", "lines", lambda n: n.startswith("--border-width-")),
       ("Size", "controls, tags, marks, icons, dots", lambda n: n.startswith("--size-")),
       ("Width and measure", "columns, sheets, dialogs, lines of text", lambda n: n.startswith(("--width-", "--measure"))),
       ("Offset, inset, layer", "where a dialog or a door sits, and what stacks on what", lambda n: n.startswith(("--offset-", "--inset-", "--z-"))),
       ("Icons", "drawn by CSS as a mask", lambda n: n.startswith("--icon-")),
       ("Motion", "easing and durations — the runner crosses its track in the token's own time", lambda n: n.startswith(("--ease-", "--duration-")))]
geo = [(n, v) for n, v, _ in decls(prim) if n not in prim_value]
assert sum(1 for n, _ in geo if any(t(n) for *_, t in GEO)) == len(geo), "a geometry primitive in no group"
px = lambda v: float(v[:-2]) if re.fullmatch(r"-?[\d.]+px", v) else None
SAMPLE = "Export &middot; acme-billing-api"


def font_of(v):
    v = re.sub(r"var\(--font-weight-(\w+)\)", lambda m: {"regular": "400", "medium": "500", "semibold": "600"}[m.group(1)], v)
    return v.replace("var(--font-sans)", '"Geist", system-ui, sans-serif').replace("var(--font-mono)", '"Geist Mono", ui-monospace, monospace')


def preview(n, v):
    p = px(v)
    if n.startswith("--space-"):
        return '<i class="bar" style="width:%gpx"></i>' % p
    if n.startswith("--radius-"):
        return '<i class="rad" style="border-radius:%gpx"></i>' % min(p, 18)
    if n.startswith("--typescale-"):
        return '<span class="spec" style="font:%s">%s</span>' % (esc(font_of(v)), SAMPLE)
    if n.startswith("--font-weight-"):
        return '<span class="spec" style="font-weight:%s">%s</span>' % (v, SAMPLE)
    if n in ("--font-sans", "--font-mono"):
        return '<span class="spec" style="font-family:%s">%s</span>' % (esc(v), SAMPLE)
    if n.startswith("--tracking-"):
        return '<span class="spec caps" style="letter-spacing:%s">Checked just now</span>' % v
    if n.startswith("--border-width-"):
        return '<i class="ln" style="border-top-width:%gpx"></i>' % p
    if n.startswith("--size-") and p is not None:
        return '<i class="sq" style="width:%gpx;height:%gpx"></i>' % (p, p)
    if n.startswith(("--width-", "--measure")) and p is not None:
        return '<i class="bar w" style="width:%.1f%%"></i>' % (100 * p / 1280)
    if n.startswith("--icon-"):
        return '<i class="ic" style="-webkit-mask:%s center / contain no-repeat;mask:%s center / contain no-repeat"></i>' % (esc(v), esc(v))
    if n.startswith("--duration-"):
        return '<span class="track"><i class="runner" style="animation-duration:%s"></i></span>' % v
    if n.startswith("--ease-"):
        return '<span class="track"><i class="runner" style="animation-timing-function:%s"></i></span>' % esc(v)
    return ""


geo_html = ""
for title, desc, test in GEO:
    rows = [(n, v) for n, v in geo if test(n)]
    if title in ("Space", "Size", "Width and measure"):
        rows.sort(key=lambda r: px(r[1]) or 0)
    def shown(v):
        if v.startswith("url("):
            return "<em>an SVG mask</em>"
        m = re.fullmatch(r"var\(--font-weight-(\w+)\) ([\d.]+px/[\d.]+px) var\(--font-(\w+)\)", v)
        if m:   # a type style, said the way a designer reads it: weight · size/line · family
            w = {"regular": 400, "medium": 500, "semibold": 600}[m.group(1)]
            return '<code>%d &middot; %s &middot; %s</code>' % (w, m.group(2), m.group(3))
        return "<code>%s</code>" % esc(v)
    body = ('<table class="tm-table geo"><colgroup><col class="c-nm"><col class="c-gv"><col></colgroup><thead><tr>'
            '<th>Primitive</th><th>Value</th><th>Looks like</th></tr></thead><tbody>%s</tbody></table>'
            % "".join('<tr><td class="nm"><code>%s</code></td><td class="val">%s</td><td class="pv">%s</td></tr>'
                      % (n, shown(v), preview(n, v)) for n, v in rows))
    geo_html += block(title, many(len(rows), "primitive"), desc, body, open_=title in ("Space", "Radius", "Type scale"))
n_geo = len(geo)

# ---- 3. semantic colour: one table per group of roles, both themes side by side ----
groups, cur = [], None
for line in sem.splitlines():
    m = re.match(r"^\s*/\* ([a-z][^*]*?) \*/\s*$", line)
    if m:
        cur = [m.group(1), []]
        groups.append(cur)
    d = re.match(LINE, line)
    if d and cur:
        cur[1].append((d.group(1), d.group(2).strip(), (d.group(3) or "").strip()))


def theme_cell(t, n, v):
    p = target(v)
    gap = t == "light" and n not in sem_light
    return ('<span class="th%s">%s<code>%s</code><code class="hx">%s</code></span>%s'
            % (" kept" if gap else "", swatch(hexof(t, n[2:])), p, hexof(t, n[2:]),
               '<small class="gapnote">keeps the dark value &mdash; a gap</small>' if gap else ""))


sem_html = ""
n_gaps = 0
for name, rows in groups:
    body = ('<table class="tm-table sem"><colgroup><col class="c-nm"><col class="c-th"><col class="c-th"><col></colgroup>'
            '<thead><tr><th>Role</th><th>Dark</th><th>Light</th><th>What it is for, and where it grew from</th></tr></thead><tbody>%s</tbody></table>'
            % "".join('<tr><td class="nm"><code>%s</code></td><td>%s</td><td>%s</td><td class="ds">%s</td></tr>'
                      % (n, theme_cell("dark", n, v), theme_cell("light", n, sem_light.get(n, (v,))[0]), esc(c)) for n, v, c in rows))
    n_gaps += sum(1 for n, _, _ in rows if n not in sem_light)
    sem_html += block(name[0].upper() + name[1:], many(len(rows), "role"), "", body)
rec = decls(recipes)
rec_body = ('<table class="tm-table sem"><colgroup><col class="c-nm"><col class="c-th"><col class="c-th"><col></colgroup>'
            '<thead><tr><th>Recipe</th><th>Dark</th><th>Light</th><th>What it is</th></tr></thead><tbody>%s</tbody></table>'
            % "".join('<tr><td class="nm"><code>%s</code></td><td><code class="ex">%s</code></td><td>%s</td><td class="ds">%s</td></tr>'
                      % (n, esc(v), '<code class="ex own">%s</code>' % esc(sem_light[n][0]) if n in sem_light else '<span class="same">the same recipe</span>', esc(c))
                      for n, v, c in rec))
sem_html += block("Recipes over a role", many(len(rec), "recipe"),
                  "washes, hovers, shadows, glass: built from roles, so they follow them into any theme", rec_body, open_=False)

# ---- 4. contrast: every pair in both themes, drawn ----
pairs = []
for t in ("dark", "light"):
    rows = []
    for fg, bg, what, bar in ct.contrast_pairs():
        v = vals[t]
        if "@" in bg:
            wash, under = bg.split("@")
            b = ct.colour(v, v[wash], ct.colour(v, "var(--%s)" % under))
        else:
            b = ct.colour(v, "var(--%s)" % bg)
        f = ct.colour(v, "var(--%s)" % fg, b)
        import contrast as _c
        rows.append((fg, bg, what, bar, f, b, _c.ratio(f, b)))
    pairs.append(rows)
rgb = lambda c: "#%02X%02X%02X" % c


def sample(f, b, bar):
    glyph = "Aa" if bar == 4.5 else "&#9679;"
    return '<i class="aa%s" style="color:%s;background:%s">%s</i>' % ("" if bar == 4.5 else " nt", rgb(f), rgb(b), glyph)


def verdict(r, bar):
    if bar == 1.0:
        return '<span class="info">info</span>'
    return '<b>%.2f</b><span class="%s">%s</span>' % (r, "ok" if r >= bar else "no", "AA" if r >= bar else "fails")


crow = {4.5: [], 3.0: [], 1.0: []}
for (fg, bg, what, bar, f, b, r), (_, _, _, _, f2, b2, r2) in zip(*pairs):
    crow[bar].append('<tr><td class="pr"><code>--%s</code> <span>on</span> <code>--%s</code><small>%s</small></td>'
                     '<td class="cv">%s%s</td><td class="cv">%s%s</td></tr>'
                     % (fg, bg.replace("@", " over --"), esc(what), sample(f, b, bar), verdict(r, bar), sample(f2, b2, bar), verdict(r2, bar)))
contrast_html = ""
for bar, title, desc in ((4.5, "Text", "4.5:1 &mdash; WCAG 1.4.3"), (3.0, "Non-text", "3:1 &mdash; a control&rsquo;s edge, a mark, a focus ring, WCAG 1.4.11"),
                         (1.0, "For information", "a tag&rsquo;s outline: measured, not claimed")):
    if crow[bar]:
        contrast_html += block(title, many(len(crow[bar]), "pair"), desc,
                               '<table class="tm-table con"><colgroup><col><col class="c-cv"><col class="c-cv"></colgroup><thead><tr><th>Pair</th><th>Dark</th><th>Light</th></tr></thead><tbody>%s</tbody></table>' % "".join(crow[bar]),
                               open_=bar != 1.0)
fails = sum(1 for rows in pairs for r in rows if r[3] > 1 and r[6] < r[3])
assert fails == 0, "a contrast pair below its bar"

TOKEN_MAP = {"{{PRIM_COLOUR}}": prim_html, "{{PRIM_GEO}}": geo_html, "{{SEMANTIC}}": sem_html, "{{CONTRAST}}": contrast_html,
             "{{N_PRIM_DARK}}": n_prim_dark, "{{N_PRIM_LIGHTONLY}}": len(prim_colour) - n_prim_dark, "{{N_GEO}}": n_geo,
             "{{N_DIRECT}}": len(sem_rows), "{{N_RECIPES}}": len(rec), "{{N_GAPS}}": n_gaps,
             "{{N_TEXT_PAIRS}}": len(crow[4.5]), "{{N_NT_PAIRS}}": len(crow[3.0])}

comp = os.path.join(SRC, "components")
n_files = len([f for f in os.listdir(comp) if f.endswith(".css") and f != "index.css"])
mock = os.path.join(ROOT, "04-wireframes", "mockups")
n_pages = len([f for f in os.listdir(mock) if f.endswith(".html")])
flows = os.path.join(mock, "flows")
n_steps = sum(len([f for f in os.listdir(os.path.join(flows, d)) if f.endswith(".html")]) for d in os.listdir(flows)
              if os.path.isdir(os.path.join(flows, d)))

for k, v in {"{{N_PRIM}}": n_prim, "{{N_PRIM_COLOUR}}": n_prim_colour, "{{N_SEM}}": n_sem, "{{N_LIGHT}}": n_light,
             "{{N_FILES}}": n_files, "{{N_PAIRS}}": n_pairs, "{{N_INFO}}": n_info, "{{N_PAGES}}": n_pages, "{{N_STEPS}}": n_steps, **TOKEN_MAP}.items():
    page_body = page_body.replace(k, str(v))
for left in re.findall(r"\{\{[^}]+\}\}", page_body):
    raise SystemExit("unsubstituted placeholder: " + left)

RESET = """
<style>
/* Baseline the artifact host normally supplies. */
html{color-scheme:light dark}
body{margin:0}
img{max-width:100%}
[hidden]{display:none!important}
</style>
""".strip()

DESC = ("AI Stack Builder's flat kit split into tokens on two levels and one CSS file per component, every screen "
        "moved without a pixel changing, and a light theme made of semantic overrides alone.")

doc = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="%s">
%s
%s
%s
</head>
<body>
%s

<script>
%s
</script>
</body>
</html>
""" % (DESC, RESET, page_head, shared_head, page_body, spy)

io.open(DST, "w", encoding="utf-8", newline="\n").write(doc)
print("wrote %s  (%.0f KB) · primitives %d (%d colour) · roles %d · light %d · files %d · pairs %d (%d info) · pages %d + %d steps"
      % (DST, os.path.getsize(DST) / 1024.0, n_prim, n_prim_colour, n_sem, n_light, n_files, n_pairs, n_info, n_pages, n_steps))

check = io.open(DST, encoding="utf-8").read()
for needle in ("<!doctype html>", 'charset="utf-8"', "Phase 08", 'class="shell"',
               'iframe src="../07-ui-assembly/ui/kit.html"', "</html>"):
    assert needle in check, "MISSING: " + needle
assert "--accent:#e05f03" in check, "shared design tokens did not come through"
assert not re.search(r"\blessons?\b", re.sub(r"<[^>]+>", " ", check), re.I), "the word lesson reached the page"
ids = set(re.findall(r'<section id="([^"]+)"', check))
for href in re.findall(r'<a href="#([^"]+)"', check):
    assert href in ids, "rail link with no section: #" + href
for page in re.findall(r'data-page="([^"]+)"', check):
    assert os.path.exists(os.path.join(mock, page + ".html")), "no such screen: " + page
print("sections: %d · rail links resolve · screens exist" % len(ids))
