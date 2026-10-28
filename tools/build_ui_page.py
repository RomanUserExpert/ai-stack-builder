"""Build 07-ui-assembly/ui.html — phase 07's page, in the same design language as phases 01–06.

Like style.html it lifts the shared <style> block and the scroll-spy out of research-page.tpl.html at build time,
so the phase pages cannot drift. Its own content is ui-page.tpl.html; the counts are read out of the kit, the
mockups folder and 06-concept/contrast.md, and the showcase, the shell and the screens are embedded live.

    python tools/build_ui_page.py
"""
import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SHARED = os.path.join(HERE, "research-page.tpl.html")
TPL = os.path.join(HERE, "ui-page.tpl.html")
SRC = os.path.join(ROOT, "07-ui-assembly")
DST = os.path.join(SRC, "ui.html")

shared = io.open(SHARED, encoding="utf-8").read()
tpl = io.open(TPL, encoding="utf-8").read()
# phase 07's kit, as phase 07 closed it: kit.css left the tree in phase 08, step 4, and git keeps it
import subprocess
kit = subprocess.run(["git", "show", "d6d419a:07-ui-assembly/ui/kit.css"], cwd=ROOT, capture_output=True,
                     check=True).stdout.decode("utf-8")
contrast = io.open(os.path.join(ROOT, "06-concept", "contrast.md"), encoding="utf-8").read()

i = shared.index("</style>") + len("</style>")
shared_head = re.sub(r"<title>.*?</title>\s*", "", shared[:i].strip(), count=1, flags=re.S)
m = re.search(r"\(function\(\)\{\s*\n\s*var links = .*?\}\)\(\);", shared, re.S)
if not m:
    raise SystemExit("scroll-spy not found in the shared template")
spy = m.group(0)
j = tpl.index("</style>") + len("</style>")
page_head, page_body = tpl[:j].strip(), tpl[j:].strip()

root = re.search(r":root\s*\{(.*?)\}", kit, re.S).group(1)
n_vars = len(re.findall(r"--[\w-]+\s*:", root))
rules = re.sub(r"/\*.*?\*/", "", kit[kit.index("}", kit.index(":root")) + 1:], flags=re.S)
n_classes = len(set(re.findall(r"\.([a-zA-Z][\w-]*)", re.sub(r"url\([^)]*\)", "", rules))))  # as kit_check counts them
n_pairs = len(re.findall(r"^\| `--", contrast, re.M))  # every measured pair; the two tag outlines are informational
mock = os.path.join(ROOT, "04-wireframes", "mockups")
n_pages = len([f for f in os.listdir(mock) if f.endswith(".html")])
flows = os.path.join(mock, "flows")
n_steps = sum(len([f for f in os.listdir(os.path.join(flows, d)) if f.endswith(".html")]) for d in os.listdir(flows)
              if os.path.isdir(os.path.join(flows, d)))

for k, v in {"{{N_VARS}}": str(n_vars), "{{N_CLASSES}}": str(n_classes), "{{N_PAIRS}}": str(n_pairs),
             "{{N_PAGES}}": str(n_pages), "{{N_STEPS}}": str(n_steps)}.items():
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

DESC = ("Every screen of AI Stack Builder built from one UI kit: DESIGN.md, the inventory, the kit and its showcase, "
        "the wireframe and its dressed twin, the guards that stop the build, and three passes over the screens.")

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
print("wrote %s  (%.0f KB) · vars %d · classes %d · pairs %d · pages %d + %d steps" % (DST, os.path.getsize(DST) / 1024.0, n_vars, n_classes, n_pairs, n_pages, n_steps))

check = io.open(DST, encoding="utf-8").read()
for needle in ("<!doctype html>", 'charset="utf-8"', "Phase 07", 'class="shell"', 'iframe src="ui/kit.html"', "</html>"):
    assert needle in check, "MISSING: " + needle
assert "--accent:#e05f03" in check, "shared design tokens did not come through"
assert not re.search(r"\blessons?\b", re.sub(r"<[^>]+>", " ", check), re.I), "the word lesson reached the page"
ids = set(re.findall(r'<section id="([^"]+)"', check))
for href in re.findall(r'<a href="#([^"]+)"', check):
    assert href in ids, "rail link with no section: #" + href
print("sections: %d · rail links resolve" % len(ids))
