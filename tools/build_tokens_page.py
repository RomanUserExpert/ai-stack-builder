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

# ---- the token map: every colour primitive, the roles that point at it, per theme ----
import html as _html
LINE = r"^\s*(--[\w-]+)\s*:\s*([^;]+);\s*(?:/\*\s*(.*?)\s*\*/)?\s*$"


def decls(text):
    return [(n, v.strip(), (c or "").strip()) for n, v, c in re.findall(LINE, text, re.M)]


prim_colour = [(n, v, c) for n, v, c in decls(prim) if re.match(r"#|rgba?\(", v)]
prim_value = {n: v for n, v, _ in prim_colour}
sem_dark = decls(sem)
sem_light = {n: (v, c) for n, v, c in decls(light)}
HUES = [("mica", "Mica"), ("lime", "Lime"), ("rose", "Rose"), ("amber", "Amber"), ("red", "Red"),
        ("white", "White and black"), ("black", "White and black")]


def target(v):
    m = re.fullmatch(r"var\((--[\w-]+)\)", v)
    return m.group(1) if m else None


def tree(theme):
    roles = {}
    for n, v, c in sem_dark:
        if theme == "light" and n in sem_light:
            v, c = sem_light[n]
        t = target(v)
        assert t in prim_value, "a role that does not point at a colour primitive: %s -> %s" % (n, v)
        kept = theme == "light" and n not in sem_light  # a gap: no light value of its own, so it draws dark
        roles.setdefault(t, []).append((n, ("No light value of its own: keeps the dark one. " if kept else "") + c, kept))
    out, last = [], None
    order = [label for _, label in HUES]
    hue_of = lambda name: next(label for key, label in HUES if name[2:].startswith(key))
    for name, value, _ in sorted(prim_colour, key=lambda p: order.index(hue_of(p[0]))):  # stable: file order in a hue
        if name not in roles:
            continue
        hue = hue_of(name)
        if hue != last:
            out.append('<li class="hue">%s</li>' % hue)
            last = hue
        chips = "".join('<code%s title="%s">%s</code>' % (' class="kept"' if k else "", _html.escape(c, quote=True), r)
                        for r, c, k in roles[name])
        alpha = " a" if value.startswith("rgba") else ""
        out.append('<li><span class="prim"><i class="sw%s" style="--sw:%s"></i><code>%s</code><small>%s</small></span>'
                   '<span class="roles">%s</span></li>' % (alpha, value, name, value, chips))
    used = sum(1 for n, _, _ in prim_colour if n in roles)
    return '<ol class="tmap" data-tmap="%s"%s>%s</ol>' % (theme, "" if theme == "dark" else " hidden", "".join(out)), used


map_dark, used_dark = tree("dark")
map_light, used_light = tree("light")
rec = decls(recipes)


def recipes_of(theme):
    chips = []
    for n, v, c in rec:
        own = theme == "light" and n in sem_light  # a recipe the light theme signed apart
        if own:
            v, c = sem_light[n]
        refs = sorted(set(re.findall(r"var\((--[\w-]+)\)", v)))
        chips.append('<code%s title="%s">%s <b>&larr;</b> %s</code>' % (
            ' class="own"' if own else "", _html.escape(c, quote=True), n, ", ".join(refs) if refs else _html.escape(v)))
    return '<div class="chips" data-tmap="%s"%s>%s</div>' % (theme, "" if theme == "dark" else " hidden", "".join(chips))


rec_html = recipes_of("dark") + recipes_of("light")
geo_groups = [
    ["type", lambda n: n.startswith(("--font", "--mono", "--weight", "--t-", "--track")), []],
    ["space", lambda n: re.fullmatch(r"--s\d+|--s-half", n), []],
    ["radius", lambda n: n.startswith("--r-"), []],
    ["size, column, layer", None, []],
    ["icons", lambda n: n in ("--icon-add", "--icon-added", "--icon-chevron") or n.startswith("--glyph"), []],
    ["motion", lambda n: n in ("--ease", "--dur", "--dur-spin", "--dur-shimmer"), []],
]
for n, v, _ in decls(prim):
    if n in prim_value:
        continue
    g = next((g for g in geo_groups if g[1] and g[1](n)), geo_groups[3])
    if g[0] in ("icons", "type"):
        g[2].append('<code title="%s">%s</code>' % (_html.escape(v, quote=True), n))
    else:
        g[2].append('<code>%s <small>%s</small></code>' % (n, _html.escape(v)))
n_geo = sum(len(g[2]) for g in geo_groups)
assert n_geo + len(prim_colour) == n_prim, "a primitive the map does not show"
geo_html = "".join('<div><span class="k">%s</span>%s</div>' % (g[0], "".join(g[2])) for g in geo_groups if g[2])
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
