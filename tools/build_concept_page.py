"""Build 06-concept/style.html — phase 06's page, in the same design language as phases 01–05.

Like voice.html it lifts the shared <style> block and the scroll-spy out of research-page.tpl.html at
build time, so the phase pages cannot drift. Its own content is concept-page.tpl.html; the counts and
the palette strip are read out of 06-concept/tokens.css, contrast.md and the mockups folder, and the
stand itself (concept.html) is embedded live.

    python tools/build_concept_page.py
"""
import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SHARED = os.path.join(HERE, "research-page.tpl.html")
TPL = os.path.join(HERE, "concept-page.tpl.html")
SRC = os.path.join(ROOT, "06-concept")
DST = os.path.join(SRC, "style.html")

shared = io.open(SHARED, encoding="utf-8").read()
tpl = io.open(TPL, encoding="utf-8").read()
tokens = io.open(os.path.join(SRC, "tokens.css"), encoding="utf-8").read()
contrast = io.open(os.path.join(SRC, "contrast.md"), encoding="utf-8").read()

i = shared.index("</style>") + len("</style>")
shared_head = re.sub(r"<title>.*?</title>\s*", "", shared[:i].strip(), count=1, flags=re.S)
m = re.search(r"\(function\(\)\{\s*\n\s*var links = .*?\}\)\(\);", shared, re.S)
if not m:
    raise SystemExit("scroll-spy not found in the shared template")
spy = m.group(0)
j = tpl.index("</style>") + len("</style>")
page_head, page_body = tpl[:j].strip(), tpl[j:].strip()

root = re.search(r":root\s*\{(.*?)\n\}", tokens, re.S).group(1)
n_tokens = len(re.findall(r"^\s*--[\w-]+:", tokens, re.M))
n_pairs = contrast.count("| pass |")
mock = os.path.join(ROOT, "04-wireframes", "mockups")
n_mockups = len([f for f in os.listdir(mock) if f.endswith(".html")])
n_flow = len([f for f in os.listdir(os.path.join(mock, "flows", "main-success")) if f.endswith(".html")])

SWATCHES = [("ground", "Mica ground"), ("tray", "the tray"), ("raised", "a panel, the active row"), ("text", "text"),
            ("text-2", "secondary"), ("text-3", "metadata"), ("lime", "lime — act, or you are here"),
            ("problem", "Problem"), ("note", "Note"), ("warning", "going ahead despite a Problem"), ("danger", "removes")]
vals = dict(re.findall(r"--([\w-]+):\s*(#[0-9A-Fa-f]{6})", root))
palette = "".join(f'<div><i style="background:{vals[n]}"></i><span><code>--{n}</code><br>{vals[n]} &middot; {role}</span></div>'
                  for n, role in SWATCHES)

for k, v in {"{{N_TOKENS}}": str(n_tokens), "{{N_PAIRS}}": str(n_pairs), "{{N_MOCKUPS}}": str(n_mockups),
             "{{N_FLOW}}": str(n_flow), "{{PALETTE}}": palette}.items():
    page_body = page_body.replace(k, v)
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

DESC = ("The visual language of AI Stack Builder, Mica · Lime: four rounds of directions, the stand with every "
        "value and its reason, the mockups of the main job, and the check that held them to it.")

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
print("wrote %s  (%.0f KB) · tokens %d · pairs %d · mockups %d + %d" % (DST, os.path.getsize(DST) / 1024.0, n_tokens, n_pairs, n_mockups, n_flow))

check = io.open(DST, encoding="utf-8").read()
for needle in ("<!doctype html>", 'charset="utf-8"', "Phase 06", 'class="shell"', 'iframe src="concept.html"', "</html>"):
    assert needle in check, "MISSING: " + needle
assert "--accent:#e05f03" in check, "shared design tokens did not come through"
assert not re.search(r"\blessons?\b", re.sub(r"<[^>]+>", " ", check), re.I), "the word lesson reached the page"
ids = set(re.findall(r'<section id="([^"]+)"', check))
for href in re.findall(r'<a href="#([^"]+)"', check):
    assert href in ids, "rail link with no section: #" + href
print("sections: %d · rail links resolve" % len(ids))
