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

comp = os.path.join(SRC, "components")
n_files = len([f for f in os.listdir(comp) if f.endswith(".css") and f != "index.css"])
mock = os.path.join(ROOT, "04-wireframes", "mockups")
n_pages = len([f for f in os.listdir(mock) if f.endswith(".html")])
flows = os.path.join(mock, "flows")
n_steps = sum(len([f for f in os.listdir(os.path.join(flows, d)) if f.endswith(".html")]) for d in os.listdir(flows)
              if os.path.isdir(os.path.join(flows, d)))

for k, v in {"{{N_PRIM}}": n_prim, "{{N_PRIM_COLOUR}}": n_prim_colour, "{{N_SEM}}": n_sem, "{{N_LIGHT}}": n_light,
             "{{N_FILES}}": n_files, "{{N_PAIRS}}": n_pairs, "{{N_INFO}}": n_info, "{{N_PAGES}}": n_pages, "{{N_STEPS}}": n_steps}.items():
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
