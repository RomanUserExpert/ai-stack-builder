"""Build 09-design-system/system.html — phase 09's page, in the same design language as phases 01–08.

The shared <style> block and the scroll-spy come out of research-page.tpl.html, and the page parts it shares with phase
08 (.stand, .guards, .qs, .outs, .verdict) out of tokens-page.tpl.html, at build time, so the phase pages cannot drift.
Its own content is system-page.tpl.html; the counts are read out of design-system/ as built.

    python tools/build_system_page.py
"""
import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SYS = os.path.join(ROOT, "design-system")
DST = os.path.join(ROOT, "09-design-system", "system.html")


def read(*p):
    return io.open(os.path.join(*p), encoding="utf-8").read()


shared = read(HERE, "research-page.tpl.html")
tokens_tpl = read(HERE, "tokens-page.tpl.html")
tpl = read(HERE, "system-page.tpl.html")

i = shared.index("</style>") + len("</style>")
shared_head = re.sub(r"<title>.*?</title>\s*", "", shared[:i].strip(), count=1, flags=re.S)
m = re.search(r"\(function\(\)\{\s*\n\s*var links = .*?\}\)\(\);", shared, re.S)
if not m:
    raise SystemExit("scroll-spy not found in the shared template")
spy = m.group(0)
parts_css = re.search(r"<style>(.*?)</style>", tokens_tpl, re.S).group(1)  # phase 08's page parts, shared
j = tpl.index("</style>") + len("</style>")
page_head, page_body = tpl[:j].strip(), tpl[j:].strip()
page_head = page_head.replace("<style>", "<style>\n" + parts_css + "\n", 1)

# ---- the counts, from what is built
docs = os.path.join(SYS, "docs")
specials = {"index.html", "components.html", "why.html", "patterns.html", "tokens.html", "layouts.html"}
n_comps = len([f for f in os.listdir(docs) if f.endswith(".html") and f not in specials])
showcase = read(docs, "components.html")
n_spec = int(re.search(r"<b>(\d+)</b><span>variants and states", showcase).group(1))
tokens = read(SYS, "tokens.css")
n_tokens = len(set(re.findall(r"^\s*--([\w-]+)\s*:", tokens, re.M)))
assert len(set(re.findall(r'<tr id="([\w-]+)">', read(docs, "tokens.html")))) == n_tokens, "tokens.html misses a token"
n_patterns = len([f for f in os.listdir(os.path.join(SYS, "patterns")) if f.endswith(".html")])
n_files = len([f for f in os.listdir(os.path.join(SYS, "components")) if f.endswith(".css") and f != "index.css"])
root = tokens[tokens.index(":root {"):tokens.index("\n}", tokens.index(":root {"))]
n_pairs = len(re.findall(r"^\s+[\d.]+ (AA|info)\s", root, re.M))
backlog = read(SYS, "backlog.md")
n_backlog = len(re.findall(r"^\| \*\*B\d+\*\* \|", backlog, re.M)) - len(re.findall(r"\*\*Closed ", backlog))

for k, v in {"{{N_COMPS}}": n_comps, "{{N_SPEC}}": n_spec, "{{N_TOKENS}}": n_tokens, "{{N_PATTERNS}}": n_patterns,
             "{{N_FILES}}": n_files, "{{N_PAIRS}}": n_pairs, "{{N_BACKLOG}}": n_backlog}.items():
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

DESC = ("AI Stack Builder's design system as one package: living documentation on the product's own stylesheet, four "
        "states in both themes, patterns found on three screens, a rule of growth, two new screens built from the system "
        "alone, and the system and the product checked together.")

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
print("wrote %s  (%.0f KB) · components %d · specimens %d · tokens %d · patterns %d · pairs %d · backlog %d open"
      % (DST, os.path.getsize(DST) / 1024.0, n_comps, n_spec, n_tokens, n_patterns, n_pairs, n_backlog))

check = io.open(DST, encoding="utf-8").read()
for needle in ("<!doctype html>", 'charset="utf-8"', "Phase 09", 'class="shell"',
               'iframe src="../design-system/docs/components.html"', "</html>"):
    assert needle in check, "MISSING: " + needle
assert "--accent:#e05f03" in check, "shared design tokens did not come through"
assert not re.search(r"\blessons?\b", re.sub(r"<[^>]+>", " ", check), re.I), "the word lesson reached the page"
ids = set(re.findall(r'<section id="([^"]+)"', check))
for href in re.findall(r'<a href="#([^"]+)"', check):
    assert href in ids, "rail link with no section: #" + href
for href in re.findall(r'(?:href|src)="(\.\./[^"#?]+)"', check):
    assert os.path.exists(os.path.normpath(os.path.join(ROOT, "09-design-system", href))), "no such file: " + href
print("sections: %d · rail links resolve · every link out exists" % len(ids))
