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

# ---- the token map: one collapsible block per hue and per geometry group, each a table ----
import html as _html
LINE = r"^\s*(--[\w-]+)\s*:\s*([^;]+);\s*(?:/\*\s*(.*?)\s*\*/)?\s*$"
esc = lambda s: _html.escape(s, quote=True)


def decls(text):
    return [(n, v.strip(), (c or "").strip()) for n, v, c in re.findall(LINE, text, re.M)]


prim_colour = [(n, v, c) for n, v, c in decls(prim) if re.match(r"#|rgba?\(", v)]
prim_value = {n: v for n, v, _ in prim_colour}
sem_dark = decls(sem)
sem_light = {n: (v, c) for n, v, c in decls(light)}
HUES = [("neutral", "Neutral", "the style's Mica greys"),
        ("lime", "Lime", "the act and the mark"), ("rose", "Rose", "a Problem"),
        ("amber", "Amber", "a Note, and going ahead despite a Problem"), ("red", "Red", "removing"),
        ("white", "White and black", "ink on a fill, highlights, shadows"),
        ("black", "White and black", "")]
hue_of = lambda name: next(k for k, *_ in HUES if name[len("--color-"):].startswith(k))
HUE_KEYS = ["neutral", "lime", "rose", "amber", "red", "white"]
LABEL = {k: (l, d) for k, l, d in HUES if d}


def target(v):
    m = re.fullmatch(r"var\((--[\w-]+)\)", v)
    return m.group(1) if m else None


def many(n, word):
    return "%d %s%s" % (n, word, "" if n == 1 else "s")


def swatch(value):
    return '<i class="sw%s" style="--sw:%s"></i>' % (" a" if value.startswith("rgba") else "", value)


def colours(theme):
    roles = {}
    for n, v, c in sem_dark:
        kept = theme == "light" and n not in sem_light   # a gap: no light value of its own, so it draws dark
        if theme == "light" and n in sem_light:
            v, c = sem_light[n]
        t = target(v)
        assert t in prim_value, "a role that does not point at a colour primitive: %s -> %s" % (n, v)
        roles.setdefault(t, []).append((n, ("No light value of its own: keeps the dark one. " if kept else "") + c, kept))
    blocks, used = [], 0
    for key in HUE_KEYS:
        rows = [(n, v) for n, v, _ in prim_colour if n in roles and hue_of(n) in (key, "black" if key == "white" else key)]
        if not rows:
            continue
        used += len(rows)
        n_roles = sum(len(roles[n]) for n, _ in rows)
        strip = "".join(swatch(v) for _, v in rows)
        body = "".join(
            '<tr><td class="sw-c">%s</td><td class="nm"><code>%s</code></td><td class="val"><code>%s</code></td>'
            '<td class="to">&rarr;</td><td class="rl">%s</td></tr>' % (
                swatch(v), n, v, "".join('<code%s title="%s">%s</code>' % (' class="kept"' if k else "", esc(c), r)
                                          for r, c, k in roles[n]))
            for n, v in rows)
        label, desc = LABEL[key]
        blocks.append(
            '<details class="tm" open><summary><span class="tm-t">%s</span><span class="tm-strip">%s</span>'
            '<span class="tm-n">%s &middot; %s</span><span class="tm-d">%s</span></summary>'
            '<table class="tm-table col"><colgroup><col class="c-sw"><col class="c-nm"><col class="c-val"><col class="c-to"><col></colgroup>'
            '<thead><tr><th></th><th>Primitive</th><th>Value</th><th></th><th>Semantic roles that read it</th></tr></thead>'
            '<tbody>%s</tbody></table></details>' % (label, strip, many(len(rows), "primitive"), many(n_roles, "role"), desc, body))
    return '<div data-tmap="%s"%s>%s</div>' % (theme, "" if theme == "dark" else " hidden", "".join(blocks)), used


map_dark, used_dark = colours("dark")
map_light, used_light = colours("light")

rec = decls(recipes)


def recipes_of(theme):
    rows = []
    for n, v, c in rec:
        own = theme == "light" and n in sem_light   # a recipe the light theme signed apart
        if own:
            v, c = sem_light[n]
        refs = sorted(set(re.findall(r"var\((--[\w-]+)\)", v)))
        rows.append('<tr%s><td class="nm"><code>%s</code></td><td class="to">&larr;</td><td class="rl">%s</td>'
                    '<td class="ds">%s</td></tr>' % (
                        ' class="own"' if own else "", n,
                        "".join("<code>%s</code>" % r for r in refs) if refs else "<code>%s</code>" % esc(v),
                        esc(c.split(" — ")[0].split(" (")[0]) + (" <em>light&rsquo;s own</em>" if own else "")))
    return ('<table class="tm-table rec" data-tmap="%s"%s><colgroup><col class="c-nm"><col class="c-to"><col class="c-from"><col></colgroup>'
            '<thead><tr><th>Recipe</th><th></th><th>Built from</th><th>What it is</th>'
            '</tr></thead><tbody>%s</tbody></table>' % (theme, "" if theme == "dark" else " hidden", "".join(rows)))


rec_html = ('<details class="tm"><summary><span class="tm-t">Recipes over a role</span><span class="tm-strip"></span>'
            '<span class="tm-n">%d recipes</span><span class="tm-d">washes, hovers, shadows, glass &mdash; they follow their roles into any theme</span>'
            '</summary>%s%s</details>' % (len(rec), recipes_of("dark"), recipes_of("light")))

GEO = [("Type", "families, weights, the type scale, tracking", lambda n: n.startswith(("--font-", "--typescale-", "--tracking-"))),
       ("Space", "the 4 px scale", lambda n: n.startswith("--space-")),
       ("Radius", "corners", lambda n: n.startswith("--radius-")),
       ("Border width", "lines", lambda n: n.startswith("--border-width-")),
       ("Size", "controls, tags, marks, icons, dots", lambda n: n.startswith("--size-")),
       ("Width and measure", "columns, sheets, dialogs, lines of text", lambda n: n.startswith(("--width-", "--measure"))),
       ("Offset and inset", "where a dialog or a door sits", lambda n: n.startswith(("--offset-", "--inset-"))),
       ("Layer", "stacking", lambda n: n.startswith("--z-")),
       ("Icons", "drawn by CSS as a mask", lambda n: n.startswith("--icon-")),
       ("Motion", "easing and durations", lambda n: n.startswith(("--ease-", "--duration-")))]
geo = [(n, v) for n, v, _ in decls(prim) if n not in prim_value]
px = lambda v: float(v[:-2]) if re.fullmatch(r"[\d.]+px", v) else None
groups = [(t, d, [(n, v) for n, v in geo if test(n)]) for t, d, test in GEO]
assert sum(len(g) for *_, g in groups) == len(geo), "a geometry primitive in no group: " + ", ".join(
    n for n, _ in geo if not any(test(n) for *_, test in GEO))
n_geo = len(geo)


def preview(title, n, v):
    p = px(v)
    if title == "Space" and p is not None:
        return '<i class="bar" style="width:%gpx"></i>' % p
    if title == "Radius" and p is not None:
        return '<i class="rad" style="border-top-left-radius:%gpx"></i>' % min(p, 24)
    if title == "Type" and n.startswith("--typescale-"):
        return '<span class="spec" style="font:%s">Aa</span>' % esc(v.replace("var(--font-weight-regular)", "400")
            .replace("var(--font-weight-medium)", "500").replace("var(--font-weight-semibold)", "600")
            .replace("var(--font-sans)", "system-ui, sans-serif").replace("var(--font-mono)", "ui-monospace, monospace"))
    return ""


geo_html = ""
for title, desc, rows in groups:
    if title == "Space":
        rows = sorted(rows, key=lambda r: px(r[1]))
    shown = lambda v: "<code>%s</code>" % esc(v) if not v.startswith("url(") else "<em>an SVG mask</em>"
    body = "".join('<tr><td class="nm"><code>%s</code></td><td class="val">%s</td><td class="pv">%s</td></tr>'
                   % (n, shown(v), preview(title, n, v)) for n, v in rows)
    geo_html += ('<details class="tm"><summary><span class="tm-t">%s</span><span class="tm-strip"></span><span class="tm-n">%s</span>'
                 '<span class="tm-d">%s</span></summary><table class="tm-table geo"><colgroup><col class="c-nm"><col class="c-gv"><col></colgroup>'
                 '<thead><tr><th>Primitive</th><th>Value</th><th></th></tr></thead><tbody>%s</tbody></table></details>'
                 % (title, many(len(rows), "primitive"), desc, body))

TOKEN_MAP = {"{{MAP_DARK}}": map_dark, "{{MAP_LIGHT}}": map_light, "{{RECIPES}}": rec_html, "{{GEOMETRY}}": geo_html,
             "{{N_USED_DARK}}": used_dark, "{{N_USED_LIGHT}}": used_light, "{{N_RECIPES}}": len(rec),
             "{{N_DIRECT}}": len(sem_dark), "{{N_GEO}}": n_geo}

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
