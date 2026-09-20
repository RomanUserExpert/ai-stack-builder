"""Build 03-information-architecture/ia.html.

Phase 03. Like the personas page it has no captures, so there is no embedding
step — and like that page it lifts the shared <style> block and the scroll-spy
out of research-page.tpl.html at build time so the three pages cannot drift.

What is different here: **the page is derived, not transcribed.** The screen
tree, the eight Mermaid diagrams and the traceability matrix are read out of
sitemap.md and flows.md at build time and substituted into the template. Nothing
is copied by hand, so the page cannot disagree with the work it is reporting —
which matters more than usual, because this phase rewrote both source files
several times in one day.

The orphan highlighting is computed rather than annotated: a column with no tick
in either block, and a row with no tick, are found by reading the tables.
"""

import io, os, re, html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SHARED = os.path.join(HERE, "research-page.tpl.html")
TPL = os.path.join(HERE, "ia-page.tpl.html")
SRC = os.path.join(ROOT, "03-information-architecture")
DST = os.path.join(SRC, "ia.html")

shared = io.open(SHARED, encoding="utf-8").read()
tpl = io.open(TPL, encoding="utf-8").read()
sitemap = io.open(os.path.join(SRC, "sitemap.md"), encoding="utf-8").read()
flows = io.open(os.path.join(SRC, "flows.md"), encoding="utf-8").read()

# ---------------------------------------------------------------- shared head
i = shared.index("</style>") + len("</style>")
shared_head = shared[:i].strip()
shared_head = re.sub(r"<title>.*?</title>\s*", "", shared_head, count=1, flags=re.S)

m = re.search(r"\(function\(\)\{\s*\n\s*var links = .*?\}\)\(\);", shared, re.S)
if not m:
    raise SystemExit("scroll-spy not found in the shared template")
spy = m.group(0)

j = tpl.index("</style>") + len("</style>")
page_head = tpl[:j].strip()
page_body = tpl[j:].strip()

# ---------------------------------------------------------------- the tree
mt = re.search(r"### The tree\s*\n+```\n(.*?)```", sitemap, re.S)
if not mt:
    raise SystemExit("screen tree not found in sitemap.md")
tree_raw = mt.group(1).rstrip("\n")

def tree_html(txt):
    """Escape, then mark the three things worth colouring: the group headings,
    the job tags in [square brackets], and the indented notes."""
    out = []
    for line in txt.split("\n"):
        e = html.escape(line)
        if re.match(r"^\d+ &middot;|^\d+ ·", e) or re.match(r"^\d+ ", e):
            e = "<b>%s</b>" % e
        else:
            e = re.sub(r"(\[[^\]]+\])", r"<i>\1</i>", e)
            # a continuation line carrying a note, not a node
            if re.match(r"^\s{8,}\S", line) and "──" not in line:
                e = "<u>%s</u>" % e
        out.append(e)
    return "\n".join(out)

# ---------------------------------------------------------------- the flows
blocks = re.findall(r"```mermaid\n(.*?)```", flows, re.S)
if len(blocks) != 8:
    raise SystemExit("expected 8 mermaid diagrams in flows.md, found %d" % len(blocks))

# Each diagram's title: the nearest preceding "## " heading, plus the bold "2a"/"2b"
# sub-label when there is one. RJ-2 is one job in two pictures, so seven headings carry
# eight diagrams and a positional zip would silently mislabel five of them.
titles = []
cur = None
sub = None
for line in flows.split("\n"):
    st = line.strip()
    if st.startswith("## "):
        cur = st[3:].strip()
        sub = None
    mm = re.match(r"\*\*(2[ab])\s", st)
    if mm:
        sub = mm.group(1)
    if st.startswith("```mermaid"):
        titles.append(cur if not sub else (cur + " \u00b7 " + sub))
        sub = None
if len(titles) != 8:
    raise SystemExit("expected 8 diagram titles, found %d:\n  %s"
                     % (len(titles), "\n  ".join(map(str, titles))))

def clean_title(t):
    t = t.replace("&mdash;", "—")
    return html.escape(t)

def counts(src):
    nodes = set()
    for mm in re.finditer(r"(?m)^\s*([A-Za-z][A-Za-z0-9]*)\s*(?:\[|\(|\{)", src):
        nodes.add(mm.group(1))
    for mm in re.finditer(r"-->(?:\|\"[^\"]*\"\|)?\s*([A-Za-z][A-Za-z0-9]*)", src):
        nodes.add(mm.group(1))
    # count the arrows and nothing else: a linkStyle line has no arrow in it, and
    # subtracting those was quietly reporting every diagram two edges short.
    edges = len(re.findall(r"-->", src))
    ends = {
        "done": len(re.findall(r'\(\["Done:', src)),
        "cost": len(re.findall(r'\(\["Cost:', src)),
        "stuck": len(re.findall(r'\(\["Stuck:', src)),
    }
    return len(nodes), edges, ends

flow_html = []
for n, (title, src) in enumerate(zip(titles, blocks)):
    nodes, edges, ends = counts(src)
    meta = ['<span>Nodes <b>%d</b></span>' % nodes, '<span>Edges <b>%d</b></span>' % edges]
    if ends["done"]:
        meta.append('<span>Done <b>%d</b></span>' % ends["done"])
    if ends["cost"]:
        meta.append('<span>Cost <b>%d</b></span>' % ends["cost"])
    if ends["stuck"]:
        meta.append('<span>Stuck <b>%d</b></span>' % ends["stuck"])
    else:
        meta.append('<span>Stuck <b>none</b></span>')
    flow_html.append(
        '<figure class="flow">\n'
        '  <figcaption><b>%s</b>Flow %d of 8</figcaption>\n'
        '  <div class="dg"><pre class="mermaid">%s</pre></div>\n'
        '  <div class="flowmeta">%s</div>\n'
        '</figure>' % (clean_title(title), n + 1, html.escape(src.rstrip()), "".join(meta))
    )

# ---------------------------------------------------------------- the matrix
HDR = "| Job | P1 | L-my | L-pub | Item | Pj | P-v | P-c | Pan | Det | Run | Sh-p | Sh-i | JSON | In |"
COLS = ["L-my", "L-pub", "Item", "Pj", "P-v", "P-c", "Pan", "Det", "Run", "Sh-p", "Sh-i", "JSON", "In"]
FULL = {
    "L-my": "My library", "L-pub": "Public library", "Item": "Item overlay", "Pj": "Projects",
    "P-v": "Project, viewing", "P-c": "Project, configuring", "Pan": "Library panel",
    "Det": "Detached row", "Run": "Run", "Sh-p": "Shared project", "Sh-i": "Shared item",
    "JSON": "Library JSON", "In": "Sign in",
}

def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

rows = []            # (kind, job, importance, [cells]) — kind in {sourced, hypo, note}
seen_header = 0
mode = None
for line in sitemap.split("\n"):
    st = line.strip()
    if st == HDR:
        seen_header += 1
        mode = "sourced" if seen_header == 1 else "hypo"
        continue
    if mode and st.startswith("|") and not st.startswith("|---"):
        cells = split_row(st)
        if len(cells) != 15:
            mode = None
            continue
        job, imp, rest = cells[0], cells[1], cells[2:]
        if "not counted twice" in " ".join(rest):
            rows.append(("note", job, imp, rest))
        else:
            rows.append((mode, job, imp, rest))
    elif mode and not st.startswith("|"):
        if st:
            mode = None

if seen_header != 2:
    raise SystemExit("expected 2 matrix headers, found %d" % seen_header)
if len(rows) != 17:
    raise SystemExit("expected 17 job rows, found %d" % len(rows))

def md_inline(t):
    t = html.escape(t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", t)
    return t

def is_tick(c):
    return c.startswith("✓")

orphan_cols = set()
for k, name in enumerate(COLS):
    if not any(is_tick(r[3][k]) for r in rows if r[0] != "note"):
        orphan_cols.add(name)
orphan_rows = set()
for r in rows:
    if r[0] == "note":
        continue
    if not any(is_tick(c) for c in r[3]):
        orphan_rows.add(r[1])

out = ['<table class="trace">', "<thead><tr>",
       '<th class="job">Job</th><th>P1</th>']
for name in COLS:
    cls = ' class="ocol"' if name in orphan_cols else ""
    out.append('<th%s title="%s">%s</th>' % (cls, FULL[name], html.escape(name)))
out.append("</tr></thead><tbody>")

for kind, job, imp, cells in rows:
    if kind == "note":
        out.append('<tr class="note"><td class="job">%s</td><td colspan="14">%s</td></tr>'
                   % (md_inline(job), md_inline(cells[0])))
        continue
    rc = []
    if kind == "hypo":
        rc.append("hypo")
    if job in orphan_rows:
        rc.append("orow")
    out.append('<tr%s>' % (' class="%s"' % " ".join(rc) if rc else ""))
    out.append('<td class="job">%s</td>' % md_inline(job))
    out.append('<td class="imp">%s</td>' % md_inline(imp))
    for k, c in enumerate(cells):
        cls = []
        if COLS[k] in orphan_cols:
            cls.append("ocol")
        if is_tick(c):
            cls.append("y")
        out.append('<td%s>%s</td>' % (' class="%s"' % " ".join(cls) if cls else "", html.escape(c)))
    out.append("</tr>")
out.append("</tbody></table>")
matrix_html = "\n".join(out)

# ---------------------------------------------------------------- substitute
page_body = page_body.replace("{{TREE}}", tree_html(tree_raw))
page_body = page_body.replace("{{FLOWS}}", "\n\n  ".join(flow_html))
page_body = page_body.replace("{{MATRIX}}", matrix_html)
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

DESC = ("The information architecture for AI Stack Builder: sixteen entities, seven screens, six "
        "places and seven user flows derived from jobs to be done, with a coverage matrix that "
        "names every surface no job raises and every job no surface closes.")

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
print("wrote %s  (%.0f KB)" % (DST, os.path.getsize(DST) / 1024.0))

# ---------------------------------------------------------------- assertions
check = io.open(DST, encoding="utf-8").read()
for needle in ("<!doctype html>", 'charset="utf-8"', "Information architecture",
               'class="shell"', 'class="tree"', 'class="trace"', 'class="flow"',
               "mermaid.esm.min.mjs", "</body>", "</html>"):
    assert needle in check, "MISSING: " + needle
assert check.count("<body>") == 1 and check.count("</html>") == 1
assert "--accent:#e05f03" in check, "shared design tokens did not come through"
assert "IntersectionObserver" in check or "scrollIntoView" in check, "scroll-spy did not come through"
assert check.count('class="mermaid"') == 8, "expected 8 diagrams on the page"

ids = set(re.findall(r'<section id="([^"]+)"', check))
for href in re.findall(r'<a href="#([^"]+)"', check):
    assert href in ids, "rail link with no section: #" + href

print("sections: %d · rail links resolve · diagrams: 8 · matrix rows: %d" % (len(ids), len(rows)))
print("orphan columns: %s" % (", ".join(sorted(orphan_cols)) or "none"))
print("orphan rows:    %s" % (", ".join(sorted(r.split("**")[1] for r in orphan_rows)) or "none"))
