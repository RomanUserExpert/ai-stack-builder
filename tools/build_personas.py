"""Build research/6-personas/personas.html.

The page has no captures, so there is no image-embedding step. What it does need
is the *same* design language as the research page, and the way to guarantee that
is to lift the shared <style> block out of research-page.tpl.html at build time
rather than copying it. Edit the shared tokens in one place and both pages move.
"""

import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SHARED = os.path.join(HERE, "research-page.tpl.html")
TPL = os.path.join(HERE, "personas-page.tpl.html")
DST = os.path.join(os.path.dirname(HERE), "research", "6-personas", "personas.html")

shared = io.open(SHARED, encoding="utf-8").read()
tpl = io.open(TPL, encoding="utf-8").read()

# --- the shared head: everything up to and including the first </style>,
#     with the research page's own <title> dropped.
i = shared.index("</style>") + len("</style>")
shared_head = shared[:i].strip()
shared_head = re.sub(r"<title>.*?</title>\s*", "", shared_head, count=1, flags=re.S)

# --- the scroll-spy, reused verbatim so the rail behaves identically.
m = re.search(r"\(function\(\)\{\s*\n\s*var links = .*?\}\)\(\);", shared, re.S)
if not m:
    raise SystemExit("scroll-spy not found in the shared template")
spy = m.group(0)

# --- this page's own head (title + component styles) and its body.
j = tpl.index("</style>") + len("</style>")
page_head = tpl[:j].strip()
page_body = tpl[j:].strip()

RESET = """
<style>
/* Baseline the artifact host normally supplies. */
html{color-scheme:light dark}
body{margin:0}
img{max-width:100%}
[hidden]{display:none!important}
</style>
""".strip()

DESC = ("Three behavioural personas and a job hierarchy for AI Stack Builder, with every claim "
        "marked confirmed, practitioner-reported or unknown, and the jobs-to-be-done matrix that "
        "says what to build first and what closes no evidenced job.")

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

os.makedirs(os.path.dirname(DST), exist_ok=True)
io.open(DST, "w", encoding="utf-8", newline="\n").write(doc)

print("wrote %s  (%.0f KB)" % (DST, os.path.getsize(DST) / 1024.0))

check = io.open(DST, encoding="utf-8").read()
for needle in ("<!doctype html>", 'charset="utf-8"',
               "Personas and JTBD",
               'class="shell"', 'class="pc primary"', 'class="matrix"', "</body>", "</html>"):
    assert needle in check, "MISSING: " + needle
assert check.count("<body>") == 1 and check.count("</html>") == 1
assert "--accent:#e05f03" in check, "shared design tokens did not come through"
assert "IntersectionObserver" in check, "scroll-spy did not come through"

# every rail link must point at a section that exists
ids = set(re.findall(r'<section id="([^"]+)"', check))
for href in re.findall(r'<a href="#([^"]+)"', check):
    assert href in ids, "rail link with no section: #" + href
print("sections: %d · rail links all resolve · structure ok" % len(ids))
