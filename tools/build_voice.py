"""Build 05-tone-of-voice/voice.html.

Phase 05. Like the personas and IA pages it has no captures, and it lifts the shared
<style> block and the scroll-spy out of research-page.tpl.html at build time so the
pages cannot drift.

**The page is derived, not transcribed.** The principles, the dictionary, the forbidden
list and the rules by element are read out of voice.md; every count, the sample's
was/now and the per-screen roll-out out of microcopy.md; the defects table out of
microcopy.md's step-7 section. Edit those two files and rebuild — never this page.
"""

import io, os, re, html
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SHARED = os.path.join(HERE, "research-page.tpl.html")
TPL = os.path.join(HERE, "voice-page.tpl.html")
SRC = os.path.join(ROOT, "05-tone-of-voice")
DST = os.path.join(SRC, "voice.html")

shared = io.open(SHARED, encoding="utf-8").read()
tpl = io.open(TPL, encoding="utf-8").read()
voice = io.open(os.path.join(SRC, "voice.md"), encoding="utf-8").read()
micro = io.open(os.path.join(SRC, "microcopy.md"), encoding="utf-8").read()

# ---------------------------------------------------------------- shared head
i = shared.index("</style>") + len("</style>")
shared_head = re.sub(r"<title>.*?</title>\s*", "", shared[:i].strip(), count=1, flags=re.S)
m = re.search(r"\(function\(\)\{\s*\n\s*var links = .*?\}\)\(\);", shared, re.S)
if not m:
    raise SystemExit("scroll-spy not found in the shared template")
spy = m.group(0)
j = tpl.index("</style>") + len("</style>")
page_head, page_body = tpl[:j].strip(), tpl[j:].strip()


# ---------------------------------------------------------------- markdown, the subset these files use
def inline(t):
    """Escape, then code, bold, italics. Links keep their text and lose their target: the
    targets are .md files, which are not served."""
    codes = []
    def keep(mm):
        codes.append(html.escape(mm.group(1)))
        return "\x00%d\x00" % (len(codes) - 1)
    t = re.sub(r"`([^`]+)`", keep, t)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"~~(.+?)~~", r"<s>\1</s>", t)
    return re.sub(r"\x00(\d+)\x00", lambda mm: "<code>%s</code>" % codes[int(mm.group(1))], t)


def cells(line):
    return [c.strip().replace("\x01", "|") for c in line.strip().replace("\\|", "\x01").strip("|").split("|")]


def md(text, h_offset=0):
    out, lines, k = [], text.strip("\n").split("\n"), 0
    while k < len(lines):
        line = lines[k]
        st = line.strip()
        if not st or st == "---":
            k += 1
            continue
        mh = re.match(r"^(#{2,4})\s+(.*)", st)
        if mh:
            lvl = min(6, len(mh.group(1)) + h_offset)
            out.append("<h%d>%s</h%d>" % (lvl, inline(mh.group(2)), lvl))
            k += 1
            continue
        if st.startswith("|"):
            rows = []
            while k < len(lines) and lines[k].strip().startswith("|"):
                rows.append(lines[k])
                k += 1
            head, body = cells(rows[0]), [cells(r) for r in rows[2:]]
            t = ['<div class="tw"><table><thead><tr>']
            t += ["<th>%s</th>" % inline(c) for c in head]
            t.append("</tr></thead><tbody>")
            for r in body:
                t.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t))
            continue
        if st.startswith(">"):
            q = []
            while k < len(lines) and lines[k].strip().startswith(">"):
                q.append(lines[k].strip()[1:].strip())
                k += 1
            paras = "\n".join(q).split("\n\n")
            out.append("<blockquote>%s</blockquote>"
                       % "".join("<p>%s</p>" % inline(" ".join(p.split("\n"))) for p in paras if p.strip()))
            continue
        if re.match(r"^(- |\d+\. )", st):
            ordered = bool(re.match(r"^\d+\. ", st))
            items = []
            while k < len(lines) and lines[k].strip() and not lines[k].strip().startswith(("|", ">", "#")):
                s2 = lines[k].strip()
                if re.match(r"^(- |\d+\. )", s2):
                    items.append(re.sub(r"^(- |\d+\. )", "", s2))
                else:
                    items[-1] += " " + s2
                k += 1
            tag = "ol" if ordered else "ul"
            out.append("<%s>%s</%s>" % (tag, "".join("<li>%s</li>" % inline(x) for x in items), tag))
            continue
        para = []
        while k < len(lines) and lines[k].strip() and not re.match(r"^(\||>|#{2,4}\s|- |\d+\. )", lines[k].strip()):
            para.append(lines[k].strip())
            k += 1
        out.append("<p>%s</p>" % inline(" ".join(para)))
    return "\n".join(out)


def section(src, start, end=None):
    a = src.index(start) + len(start)
    b = src.index(end, a) if end else len(src)
    return src[a:b]


# ---------------------------------------------------------------- principles
prin_src = section(voice, "\n## Principles\n", "\n### What did not become a principle")
blocks = re.split(r"\n### (\d) · ", prin_src)[1:]
principles = []
for n, body in zip(blocks[0::2], blocks[1::2]):
    title, rest = body.split("\n", 1)
    def part(label, nxt):
        mm = re.search(r"\*\*%s\.\*\*(.*?)(?=\n\*\*(?:%s)\.\*\*|\n\*Settles:\*|\n---|\Z)" % (label, nxt), rest, re.S)
        return mm.group(1).strip() if mm else ""
    rule = part("Rule", "Example")
    ex = part("Example", "Anti-example")
    anti = part("Anti-example", "Explanation")
    why = part("Explanation", "What the rule does not license")
    settles = re.search(r"\n\*Settles:\*(.*?)(?=\n---|\Z)", rest, re.S)
    principles.append((n, title.strip(), rule, ex, anti, why, settles.group(1).strip() if settles else ""))
if len(principles) != 5:
    raise SystemExit("expected 5 principles, found %d" % len(principles))


def quote_lines(q):
    return "".join("<p>%s</p>" % inline(l.lstrip("> ").strip())
                   for l in q.split("\n") if l.strip().lstrip(">").strip())


prin_html = []
for n, title, rule, ex, anti, why, settles in principles:
    prin_html.append(
        '<article class="principle">\n'
        '  <header><b>Principle %s</b><h3>%s</h3></header>\n'
        '  <div class="rule">%s</div>\n'
        '  <div class="pair"><div class="yes"><p class="lab">Written by it</p>%s</div>'
        '<div class="no"><p class="lab">Breaks it</p>%s</div></div>\n'
        '  <div class="why">%s</div>\n'
        '  %s\n'
        '</article>' % (n, inline(title), md(rule), quote_lines(ex), quote_lines(anti), md(why),
                        ('<p class="settles"><strong>Settles</strong> %s</p>' % inline(settles)) if settles else ""))

not_prin = md(section(voice, "### What did not become a principle, and why\n", "\n## Dictionary"))
dictionary = md(section(voice, "\n## Dictionary\n", "\n## Forbidden"), h_offset=1)
forbidden = md(section(voice, "\n## Forbidden\n", "\n## Microcopy"), h_offset=1)

# ---------------------------------------------------------------- rules by element
el_src = section(voice, "\n## Microcopy — rules by element\n")
els = re.split(r"\n### ", el_src)[1:]
el_html = []
for e in els:
    name, rest = e.split("\n", 1)
    rule = re.search(r"\*\*Rule\.\*\*(.*?)(?=\n\*\*Example)", rest, re.S).group(1).strip()
    ex = re.search(r"\*\*Example\.\*\*\n(.*?)(?=\n\n(?!>)|\Z)", rest, re.S).group(1)
    chk = re.search(r"\*Checked against:\*(.*?)(?=\n\n|\Z)", rest, re.S)
    el_html.append('<div class="element"><h3>%s</h3><p>%s</p><blockquote>%s</blockquote>%s</div>'
                   % (inline(name.strip()), inline(" ".join(rule.split())), quote_lines(ex),
                      ('<p class="checked">Checked against %s</p>' % inline(" ".join(chk.group(1).split()))) if chk else ""))
if len(el_html) != 8:
    raise SystemExit("expected 8 element rules, found %d" % len(el_html))

# ---------------------------------------------------------------- the table: counts, sample, roll-out
table_src = micro[micro.index("## The table, screen by screen"):]
rows = []
for line in table_src.split("\n"):
    if line.startswith("| ") and not line.startswith("| Screen"):
        c = cells(line)
        if len(c) == 9:
            rows.append(c)
n_rows = len(rows)
changed = [r for r in rows if r[3] != "="]
n_user = sum(1 for r in rows if r[6] == "user")

per = OrderedDict()
for r in rows:
    s = per.setdefault(r[0], [0, 0])
    s[0] += 1
    if r[3] != "=":
        s[1] += 1
mx = max(v[1] for v in per.values()) or 1
ro = ['<table class="wn"><thead><tr><th>Screen</th><th class="n">Lines</th><th class="n">Rewritten</th><th></th></tr></thead><tbody>']
for s, (tot, ch) in per.items():
    ro.append('<tr><td>%s</td><td class="n">%d</td><td class="n">%d</td><td><span class="bar" style="width:%dpx"></span></td></tr>'
              % (html.escape(s), tot, ch, round(160 * ch / mx)))
ro.append("</tbody></table>")

sample = ['<table class="wn"><thead><tr><th>Zone</th><th>Was</th><th>Now</th><th>Why</th></tr></thead><tbody>']
seen = set()
for r in rows:
    if r[0] != "Run" or r[3] == "=" or (r[2], r[3]) in seen:
        continue
    seen.add((r[2], r[3]))
    sample.append('<tr><td class="why">%s</td><td class="was">%s</td><td class="now">%s</td><td class="why">%s</td></tr>'
                  % (inline(r[1]), inline(r[2].replace("<br>", " ")), inline(r[3].strip("*")), inline(r[8])))
sample.append("</tbody></table>")

defects = md(section(micro, "## Step 7 — the check, and what it fixed\n", "\n---\n\n## The table"))

# ---------------------------------------------------------------- substitute
for k_, v in {"{{PRINCIPLES}}": "\n\n  ".join(prin_html), "{{NOT_PRINCIPLES}}": not_prin,
              "{{DICTIONARY}}": dictionary, "{{FORBIDDEN}}": forbidden, "{{ELEMENTS}}": "\n".join(el_html),
              "{{SAMPLE}}": "".join(sample), "{{ROLLOUT}}": "".join(ro), "{{DEFECTS}}": defects,
              "{{N_ROWS}}": "{:,}".format(n_rows), "{{N_CHANGED}}": str(len(changed)),
              "{{N_USER}}": str(n_user)}.items():
    page_body = page_body.replace(k_, v)
# The front end never says *lesson* (owner, 2026-10-05). The top level is a *phase*, as on the strip
# and in every eyebrow; what a phase is made of is a *stage*. The source files keep their own words.
page_body = re.sub(r"\b([Ss])tep(s?)\b(?=[-\s]?\d)", lambda mm: ("S" if mm.group(1) == "S" else "s") + "tage" + mm.group(2), page_body)
page_body = re.sub(r"\b([Ss])teps (\d)", lambda mm: mm.group(1) + "tages " + mm.group(2), page_body)
page_body = re.sub(r"\b([Ll])esson(s?)\b", lambda mm: ("P" if mm.group(1) == "L" else "p") + "hase" + mm.group(2), page_body)
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

DESC = ("The voice of AI Stack Builder: five principles drawn from research, a dictionary with one "
        "word per concept, a forbidden list, rules for each kind of interface line, and every line "
        "of the product rewritten against them, before and after.")

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
for needle in ("<!doctype html>", 'charset="utf-8"', "Tone of voice and microcopy", 'class="shell"',
               'class="principle"', 'class="element"', 'class="wn"', "</body>", "</html>"):
    assert needle in check, "MISSING: " + needle
assert check.count("<body>") == 1 and check.count("</html>") == 1
assert "--accent:#e05f03" in check, "shared design tokens did not come through"
assert not re.search(r"\blessons?\b", re.sub(r"<[^>]+>", " ", check), re.I), "the word lesson reached the page"
assert check.count('class="principle"') == 5 and check.count('class="element"') == 8
ids = set(re.findall(r'<section id="([^"]+)"', check))
for href in re.findall(r'<a href="#([^"]+)"', check):
    assert href in ids, "rail link with no section: #" + href
print("sections: %d · rail links resolve · principles 5 · elements 8 · rows %d · rewritten %d · user %d"
      % (len(ids), n_rows, len(changed), n_user))
