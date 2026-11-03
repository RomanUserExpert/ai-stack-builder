"""Phase 09, step 7: the system and the product checked together — the five classes of defect the course names.

    python -X utf8 tools/system_check.py            # print the findings
    python -X utf8 tools/system_check.py --json F   # and write them to F

1. look   — a component looks different in the product than on its docs page: every element of a docs specimen and
             of every dressed page is signed by tag, component classes and state attributes, and its computed style
             compared; a signature drawn both places with a style one side never has is a finding.
2. drift  — the docs describe a variant or a state the code does not have, or the reverse: a class in components/
             that no docs specimen shows; a component the docs call stateless whose file has :hover/:active/:focus/
             :disabled rules.
3. theme  — a state in one theme only: tokens.css's own light-gap check, and a component rule fixed to one theme.
4. pattern — a pattern with a style of its own (guard 12, repeated here so the table has its row).
5. orphan — a component or a token with no docs page.

It reads what is built, so run tools/build_mockups.py first. kit_check.py carries the same checks as guards 14–16.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
SYSTEM = ROOT / "design-system"
DOCS = SYSTEM / "docs"
MOCK = ROOT / "04-wireframes" / "mockups"

PROPS = ["color", "backgroundColor", "borderTopColor", "borderTopWidth", "borderRadius", "fontSize", "fontWeight",
         "fontFamily", "paddingTop", "paddingLeft", "boxShadow", "textDecorationLine", "opacity", "display", "gap"]
ATTRS = ["aria-current", "aria-disabled", "disabled", "aria-busy", "open", "aria-expanded", "aria-pressed", "checked",
         "aria-selected"]

SIGN_JS = """([root, props, attrs]) => {
  const out = {};
  const els = root === 'docs'
    ? [...document.querySelectorAll('#variants .kit-demo *')]
    : [...document.querySelectorAll('body *')];
  for (const el of els) {
    if (el.closest('svg') && el.tagName.toLowerCase() !== 'svg') continue;
    if (el.closest('.visually-hidden')) continue;
    const cls = [...el.classList].filter(c => !/^(kit-|doc-)/.test(c)).sort();
    if (!cls.length) continue;
    const at = attrs.filter(a => el.hasAttribute(a)).map(a => a + '=' + el.getAttribute(a));
    const pe = el.parentElement;
    const parent = pe ? pe.tagName.toLowerCase() + '.' + [...pe.classList].filter(c => !/^(kit-|doc-)/.test(c)).sort().join('.') : '';
    const sig = el.tagName.toLowerCase() + '.' + cls.join('.') + (at.length ? '[' + at.join(',') + ']' : '') + ' < ' + parent;
    const cs = getComputedStyle(el);
    const st = props.map(p => p === 'fontFamily' ? cs[p].split(',')[0].replace(/"/g, '') : cs[p]).join('|');
    (out[sig] = out[sig] || {})[st] = (out[sig][st] || 0) + 1;
  }
  return out;
}"""


def sign_pages(files, root, theme="dark"):
    from playwright.sync_api import sync_playwright
    seen = {}
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 1440, "height": 900})
        for f in files:
            pg.goto(f.as_uri(), wait_until="load")
            if theme != "dark":
                pg.evaluate(f"document.documentElement.dataset.theme = '{theme}'")
            for sig, sts in pg.evaluate(SIGN_JS, [root, PROPS, ATTRS]).items():
                for st in sts:
                    seen.setdefault(sig, {}).setdefault(st, set()).add(f.stem)
        br.close()
    return seen


def look(docs_pages, mock_pages):
    d, m = sign_pages(docs_pages, "docs"), sign_pages(mock_pages, "page")
    out = []
    for sig in sorted(set(d) & set(m)):
        only_docs = set(d[sig]) - set(m[sig])
        only_prod = set(m[sig]) - set(d[sig])
        if not only_docs and not only_prod:
            continue
        def diff(a, b):
            pa, pb = a.split("|"), b.split("|")
            return {PROPS[i]: (pa[i], pb[i]) for i in range(len(PROPS)) if pa[i] != pb[i]}
        ref_p = next(iter(m[sig]))
        for st in only_docs:
            out.append(dict(kind="look", sig=sig, where="docs " + ", ".join(sorted(d[sig][st])[:3]),
                            diff=diff(st, min(m[sig], key=lambda x: len(diff(st, x))))))
        for st in only_prod:
            out.append(dict(kind="look", sig=sig, where="product " + ", ".join(sorted(m[sig][st])[:3]),
                            diff=diff(min(d[sig], key=lambda x: len(diff(x, st))), st)))
    return out


def component_classes():
    css = "".join(p.read_text(encoding="utf-8") for p in (SYSTEM / "components").glob("*.css") if p.name != "index.css")
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    return set(re.findall(r"\.([a-z][a-z0-9-]*)", css)), css


def drift():
    import build_kit as bk
    import docs_content
    groups = bk.components()
    shown = set()  # what the docs show, as built — transform adds tone classes (button-danger, callout-reminder) when dressing
    for f in DOCS.glob("*.html"):
        if f.stem in ("index", "components", "why", "patterns", "tokens", "layouts"):
            continue
        for m in re.findall(r'class="([^"]*)"', f.read_text(encoding="utf-8")):
            shown |= set(m.split())
    shown |= {lay["cls"] for lay in docs_content.LAYOUTS}  # a frame is documented on layouts.html (S7)
    classes, css = component_classes()
    out = []
    for c in sorted(classes - shown):
        if c.startswith("sk-"):
            continue  # skeleton sizes: content, shown as the Skeleton's own specimens are measured (§17)
        files = [p.name for p in (SYSTEM / "components").glob("*.css") if re.search(rf"\.{c}\b", p.read_text(encoding="utf-8"))]
        out.append(dict(kind="drift", sig="." + c, where=", ".join(files), diff="in the code, shown on no docs page"))
    for name, (why, _to) in docs_content.STATIC.items():
        comp = next(c for comps in groups.values() for c in comps if c.name == name)
        own = {k.strip() for k in comp.cls.split("·")} - {"", "icon", "meta", "button", "visually-hidden"}
        states = sorted({m.group(0) for k in own for m in
                         re.finditer(rf"\.{re.escape(k)}\b[^{{,]*:(hover|active|focus-visible|focus-within|disabled)", css)})
        if states:
            out.append(dict(kind="drift", sig=name, where="docs_content.STATIC",
                            diff=f"the docs say no state of its own; the code has {states[:3]}"))
    return out


def theme():
    import concept_tokens as ct
    out = [dict(kind="theme", sig="--" + g, where="tokens.css", diff="no light value") for g in ct.light_gaps()]
    for p in (SYSTEM / "components").glob("*.css"):
        if "data-theme" in p.read_text(encoding="utf-8"):
            out.append(dict(kind="theme", sig=p.name, where=p.name, diff="a rule fixed to one theme inside a component"))
    return out


def pattern():
    out = []
    for f in sorted((SYSTEM / "patterns").glob("*.html")):
        h = f.read_text(encoding="utf-8")
        if re.search(r'\sstyle="', h) or "<style" in h:
            out.append(dict(kind="pattern", sig=f.name, where=f"patterns/{f.name}", diff="a style of its own"))
    return out


def orphan():
    out = []
    tokens = re.findall(r"^\s*--([\w-]+)\s*:", (SYSTEM / "tokens.css").read_text(encoding="utf-8"), flags=re.M)
    page = DOCS / "tokens.html"
    rows = set(re.findall(r'<tr id="([\w-]+)">', page.read_text(encoding="utf-8"))) if page.exists() else set()
    missing = sorted({t for t in tokens if t not in rows})
    if missing:
        out.append(dict(kind="orphan", sig=f"{len(missing)} of {len(set(tokens))} tokens", where="design-system/docs/",
                        diff="named on no docs page: " + ", ".join("--" + t for t in missing[:8]) + " …"))
    return out


LINK_JS = """() => [...document.querySelectorAll('.meta a')].filter(a => !a.closest('.visually-hidden, [inert]'))
  .filter(a => !getComputedStyle(a).textDecorationLine.includes('underline'))
  .map(a => a.textContent.trim().slice(0, 30))"""


def links(files):
    """I1: a link in a meta line carries a non-colour cue at rest (WCAG 1.4.1)."""
    from playwright.sync_api import sync_playwright
    out = []
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 1440, "height": 900})
        for f in files:
            pg.goto(f.as_uri(), wait_until="load")
            bad = pg.evaluate(LINK_JS)
            if bad:
                out.append(dict(kind="link", sig=".meta a", where=f.stem, diff=f"told from its line by colour only: {bad[:3]}"))
        br.close()
    return out


def docs_component_pages():
    return [p for p in sorted(DOCS.glob("*.html")) if p.stem not in ("index", "components", "why", "patterns", "tokens", "layouts")]


def look_and_links():
    mock_pages = sorted(MOCK.glob("*.html"))
    return look(docs_component_pages(), mock_pages) + links(mock_pages + sorted((SYSTEM / "examples").glob("*.html")))


def run():
    return look_and_links() + drift() + theme() + pattern() + orphan()


if __name__ == "__main__":
    found = run()
    for f in found:
        print(f["kind"].ljust(8), f["sig"][:90], "|", f["where"][:60], "|", f["diff"])
    print(f"{len(found)} findings")
    if "--json" in sys.argv:
        Path(sys.argv[sys.argv.index("--json") + 1]).write_text(json.dumps(found, indent=1, default=str), encoding="utf-8")
