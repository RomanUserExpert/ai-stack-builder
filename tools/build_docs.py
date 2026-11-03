"""Phase 09, step 2: the living documentation — design-system/docs/.

    python -X utf8 tools/build_docs.py          # writes every page, then checks them in a browser
    python -X utf8 tools/build_docs.py --fast   # writes, skips the browser check

Writes, into design-system/docs/:

- components.html  the showcase: every component, grouped as the kit groups them, each with a live preview.
                 index.html sends to it: served as /design-system/docs with no slash (Vercel, trailingSlash:
                 false), a page there resolves ../index.css against /design-system/ and loads unstyled (I6)
- <slug>.html  one page per component, in four parts: anatomy (the live component with its parts numbered),
               variants and states (every one the kit shows, which is every one inventory.md lists), when to use,
               rule and anti-rule
- why.html     why the system looks as it does: the owner's taste, the five attributes, the four rounds of
               directions, the references and what was taken from each — from 06-concept/concept.md and
               references.md (D8: read from there, nothing copied)

**Nothing here is a picture or a copy of CSS.** Every specimen is build_kit.components()'s — the same pieces kit.html
shows, cut from the wireframe pages and dressed by build_mockups.transform — and every page links
design-system/index.css alone, as every screen does. What the docs *say* is tools/docs_content.py.

Checks, and the build fails on any:
- a component of the kit with no entry in docs_content, or the reverse;
- an anti-rule pointing at a component that does not exist;
- the docs' own styles holding a value (concept_ui.literals);
- a word in a specimen that is not in microcopy.md (the kit's own check, on the docs' specimens);
- in a browser: an anatomy part whose selector finds nothing in its live specimen.
"""
from pathlib import Path
import html as htmllib
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build_kit as bk  # noqa: E402
import build_mockups as bm  # noqa: E402
import concept_ui  # noqa: E402
import docs_content  # noqa: E402

SYSTEM = ROOT / "design-system"
OUT = SYSTEM / "docs"
HREF = ["../index.css"]
E = htmllib.escape

DOC_CSS = r"""
.doc-page .kit-body{gap:var(--space-12)}
.doc-crumb{font:var(--typescale-small);color:var(--text-3)}
.doc-crumb a{color:var(--text-2)}
.doc-crumb a:hover{color:var(--text)}
.doc-lead{max-width:var(--measure-wide);color:var(--text-2)}
.doc-meta{display:flex;flex-wrap:wrap;gap:var(--space-2) var(--space-4);font:var(--typescale-micro);color:var(--text-3)}
.doc-meta code{background:none;padding:0;color:var(--text-2)}
.doc-sec{display:flex;flex-direction:column;gap:var(--space-5)}
.doc-sec>h2{font:var(--typescale-title);letter-spacing:var(--tracking-title);padding-bottom:var(--space-3);border-bottom:var(--border-width-thin) solid var(--line-strong)}
.doc-sec>h2 .kit-meta{margin-left:var(--space-2)}
.doc-anatomy{position:relative;padding:var(--space-10) var(--space-8);background:var(--tray);border:var(--border-width-thin) solid var(--line);border-radius:var(--radius-lg)}
.doc-anatomy>.kit-demo{grid-column:auto;grid-row:auto}
.doc-pins{position:absolute;inset:0;pointer-events:none}
.doc-pin,.doc-parts li::before{display:inline-flex;align-items:center;justify-content:center;min-width:var(--size-tag);height:var(--size-tag);padding:0 var(--space-1);border-radius:var(--radius-full);background:var(--mark);color:var(--ground);font:var(--typescale-micro);font-weight:var(--font-weight-semibold);font-variant-numeric:tabular-nums}
.doc-pin{position:absolute;box-shadow:0 0 0 var(--border-width-thick) var(--tray)}
.doc-hl{position:absolute;display:none;border:var(--border-width-thick) solid var(--mark);border-radius:var(--radius-sm);pointer-events:none}
.doc-parts{display:grid;grid-template-columns:repeat(auto-fill,minmax(var(--width-col-lg),1fr));gap:var(--space-3) var(--space-8);list-style:none;counter-reset:part}
.doc-parts li{display:grid;grid-template-columns:var(--size-tag) minmax(0,1fr);gap:0 var(--space-3);align-items:start;font:var(--typescale-small);color:var(--text-2);cursor:default}
.doc-parts li::before{counter-increment:part;content:counter(part)}
.doc-parts li:hover b{color:var(--text)}
.doc-parts b{font-weight:var(--font-weight-semibold);color:var(--text)}
.doc-parts code{grid-column:2;font:var(--typescale-code);color:var(--text-3);background:none;padding:0}
.doc-prose{display:flex;flex-direction:column;gap:var(--space-3);max-width:var(--measure)}
.doc-prose p{color:var(--text-2)}
.doc-prose strong{color:var(--text);font-weight:var(--font-weight-semibold)}
.doc-size{font:var(--typescale-small);color:var(--text-3)}
.doc-rules{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-4)}
.doc-rule{display:flex;flex-direction:column;gap:var(--space-2);padding:var(--space-5);background:var(--raised);border:var(--border-width-thin) solid var(--line);border-radius:var(--radius-lg);color:var(--text-2)}
.doc-rule.doc-anti{background:var(--cutout)}
.doc-rule a{color:var(--text)}
.doc-pager{display:flex;justify-content:space-between;gap:var(--space-4);padding-top:var(--space-5);border-top:var(--border-width-thin) solid var(--line);font:var(--typescale-small)}
.doc-pager a{color:var(--text-2)}
.doc-pager a:hover{color:var(--text)}
.doc-group{display:flex;flex-direction:column;gap:var(--space-5)}
.doc-group>h2{font:var(--typescale-title);letter-spacing:var(--tracking-title);padding-bottom:var(--space-3);border-bottom:var(--border-width-thin) solid var(--line-strong)}
.doc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(var(--width-col-xl),1fr));gap:var(--space-5)}
.doc-card{position:relative;display:flex;flex-direction:column;gap:var(--space-2);padding:var(--space-3);background:var(--raised);border:var(--border-width-thin) solid var(--line);border-radius:var(--radius-lg)}
.doc-card:hover{border-color:var(--line-strong)}
.doc-card h3{font:var(--typescale-heading);letter-spacing:var(--tracking-heading);padding:0 var(--space-2)}
.doc-card h3 a{color:var(--text);text-decoration:none}
.doc-card h3 a::after{content:"";position:absolute;inset:0}
.doc-card p{padding:0 var(--space-2) var(--space-2);font:var(--typescale-small);color:var(--text-2)}
.doc-preview{height:var(--width-col-md);overflow:hidden;padding:var(--space-4);background:var(--tray);border-radius:var(--radius-md);pointer-events:none}
.doc-preview .kit-demo{grid-column:auto;grid-row:auto;width:var(--width-sheet);transform:scale(.5);transform-origin:0 0}
.doc-preview .kit-stage dialog.modal{margin:0 auto}
.doc-entry{display:flex;flex-direction:column;gap:var(--space-3);max-width:var(--measure-wide)}
.doc-entry pre{padding:var(--space-4);background:var(--well-deep);border:var(--border-width-thin) solid var(--line-strong);border-radius:var(--radius-md);font:var(--typescale-code);color:var(--text);overflow-x:auto}
.doc-facts{display:flex;flex-wrap:wrap;gap:var(--space-8)}
.doc-facts div{display:flex;flex-direction:column;gap:var(--space-1)}
.doc-facts b{font:var(--typescale-display);letter-spacing:var(--tracking-display);color:var(--text)}
.doc-facts span{font:var(--typescale-small);color:var(--text-3)}
.doc-links{display:flex;flex-wrap:wrap;gap:var(--space-2)}
.doc-table{width:100%;border-collapse:collapse;font:var(--typescale-small)}
.doc-table th{text-align:left;font:var(--typescale-label);letter-spacing:var(--tracking-label);text-transform:uppercase;color:var(--text-3);padding:var(--space-2) var(--space-3);border-bottom:var(--border-width-thin) solid var(--line-strong)}
.doc-table td{vertical-align:top;padding:var(--space-3);border-bottom:var(--border-width-thin) solid var(--line);color:var(--text-2)}
.doc-table td:first-child{color:var(--text);font-weight:var(--font-weight-semibold);white-space:nowrap}
.doc-pairs{display:grid;grid-template-columns:repeat(auto-fill,minmax(var(--width-col-lg),1fr));gap:var(--space-4)}
.doc-pair{display:flex;flex-direction:column;gap:var(--space-2);padding:var(--space-5);background:var(--raised);border:var(--border-width-thin) solid var(--line);border-radius:var(--radius-lg)}
.doc-pair h3{font:var(--typescale-heading);letter-spacing:var(--tracking-heading)}
.doc-pair p{font:var(--typescale-small);color:var(--text-2)}
.doc-pair .kit-label{color:var(--text-3)}
.doc-rounds{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--space-4);list-style:none;counter-reset:round}
.doc-rounds li{display:flex;flex-direction:column;gap:var(--space-2);padding:var(--space-4);background:var(--cutout);border:var(--border-width-thin) solid var(--line);border-radius:var(--radius-md);font:var(--typescale-small);color:var(--text-2)}
.doc-rounds li.is-kept{background:var(--raised);border-color:var(--line-strong)}
.doc-rounds b{color:var(--text);font-weight:var(--font-weight-semibold)}
.doc-ref{display:flex;flex-direction:column;gap:var(--space-4);padding:var(--space-5) 0;border-top:var(--border-width-thin) solid var(--line)}
.doc-ref h3{font:var(--typescale-heading);letter-spacing:var(--tracking-heading)}
.doc-ref .doc-prose{max-width:var(--measure-wide)}
.doc-ref .kit-demo{grid-column:auto;grid-row:auto}
.doc-states-wrap{display:flex;flex-direction:column;gap:var(--space-2);overflow-x:auto}
.doc-states{display:grid;grid-template-columns:var(--width-col-md) repeat(5,minmax(max-content,1fr));gap:var(--space-2);align-items:stretch}
.doc-states>.kit-label{align-self:center}
.doc-cell{display:flex;align-items:center;justify-content:flex-start;gap:var(--space-2);padding:var(--space-6) var(--space-5);background:var(--ground);color:var(--text);font:var(--typescale-body);border:var(--border-width-thin) solid var(--line);border-radius:var(--radius-md)}
.doc-cell.is-bar{background:var(--bar)}
.doc-cell>*{min-width:0}
.doc-cell .kit-demo{grid-column:auto;grid-row:auto}
.doc-cell .kit-demo>:is(.field,.search,.field-row,.dropzone,.file-list,.callout,.aside-box){width:var(--width-col-md)}
.doc-na{align-items:flex-start;font:var(--typescale-small);color:var(--text-3);border-style:dashed;white-space:normal;max-width:var(--width-col-lg)}
.doc-static{display:flex;flex-direction:column;gap:var(--space-2);max-width:var(--measure);color:var(--text-2)}
.doc-states-note{font:var(--typescale-micro);color:var(--text-3)}
.doc-states-off .doc-cell[data-ds-state]{opacity:.4}
.doc-pattern{display:flex;flex-direction:column;gap:var(--space-4);padding-top:var(--space-6);border-top:var(--border-width-thin) solid var(--line)}
.doc-pattern h2{font:var(--typescale-title);letter-spacing:var(--tracking-title)}
.doc-frame{width:100%;height:var(--width-sheet);border:var(--border-width-thin) solid var(--line-strong);border-radius:var(--radius-lg);background:var(--ground)}
.doc-scroll{overflow-x:auto}
.doc-tokens td{font:var(--typescale-small)}
.doc-tokens td code{background:none;padding:0;color:var(--text-2);white-space:nowrap}
.doc-tokens td:first-child code{color:var(--text)}
.doc-sw{white-space:nowrap}
.doc-swatch{display:inline-block;width:var(--size-mark);height:var(--size-mark);margin-right:var(--space-1);border:var(--border-width-thin) solid var(--line-strong);border-radius:var(--radius-xs);vertical-align:middle}
"""

STATES_JS = r"""<script>
(function(){
  /* the States block: the product's own :hover, :active, :focus-visible and :focus-within rules, copied once with the
     pseudo-class turned into an attribute, so a state can be put on a specimen and held there. Nothing of the product's
     CSS is changed; disabled is the real attribute. */
  var MAP = [[':focus-visible', '[data-ds-focus]'], [':focus-within', '[data-ds-focus-within]'],
             [':hover', '[data-ds-hover]'], [':active', '[data-ds-active]']];
  var out = [], ok = true;
  function walk(sheet){
    var rules; try { rules = sheet.cssRules; } catch (e) { if (!sheet.href || new URL(sheet.href).origin === location.origin) ok = false; return; }  /* a font's sheet on another host is not ours to read */
    for (var i = 0; i < rules.length; i++){
      var r = rules[i];
      if (r.styleSheet) { walk(r.styleSheet); continue; }
      if (r.cssRules && !r.selectorText) { walk(r); continue; }
      if (!r.selectorText || !/:(hover|active|focus-visible|focus-within)/.test(r.selectorText)) continue;
      var sel = r.selectorText;
      MAP.forEach(function(m){ sel = sel.split(m[0]).join(m[1]); });
      out.push(sel + '{' + r.style.cssText + '}');
    }
  }
  for (var i = 0; i < document.styleSheets.length; i++) walk(document.styleSheets[i]);
  var st = document.createElement('style'); st.id = 'ds-forced'; st.textContent = out.join(' '); document.head.appendChild(st);
  if (!ok) document.documentElement.classList.add('doc-states-off');
  var FOCUSABLE = 'a[href],button,input:not([type=hidden]),select,textarea,summary';
  var FIELD = 'button,input,select,textarea';
  function up(el, cell, attr){ while (el && el !== cell){ el.setAttribute(attr, ''); el = el.parentElement; } }
  document.querySelectorAll('.doc-cell[data-ds-state]').forEach(function(cell){
    var sel = cell.closest('[data-ds-target]').getAttribute('data-ds-target');
    var root = cell.querySelector('.kit-demo');
    var t = sel ? root.querySelector(sel) : root.firstElementChild;
    if (!t) return;
    var s = cell.getAttribute('data-ds-state');
    var f = t.matches(FOCUSABLE) ? t : t.querySelector(FOCUSABLE);
    if (s === 'hover') up(t, cell, 'data-ds-hover');
    if (s === 'active') { up(t, cell, 'data-ds-hover'); up(t, cell, 'data-ds-active'); if (f) up(f, cell, 'data-ds-active'); }
    if (s === 'focus' && f) { f.setAttribute('data-ds-focus', ''); up(f, cell, 'data-ds-focus-within'); }
    if (s === 'disabled') {
      var d = t.matches(FIELD) ? t : t.querySelector(FIELD);
      if (d) d.disabled = true; else t.setAttribute('aria-disabled', 'true');
    }
  });
})();
</script>"""

PIN_JS = r"""<script>
(function(){
  function place(){
    document.querySelectorAll('[data-anatomy]').forEach(function(box){
      var spec = box.querySelector('.kit-demo'), layer = box.querySelector('.doc-pins'), hl = box.querySelector('.doc-hl');
      var b = box.getBoundingClientRect(), taken = [];
      layer.innerHTML = '';
      box.parentNode.querySelectorAll('.doc-parts li').forEach(function(li, i){
        var el = spec.querySelector(li.getAttribute('data-sel'));
        if (!el) return;
        var r = el.getBoundingClientRect(), x = r.left - b.left, y = r.top - b.top;
        var pin = document.createElement('span');
        pin.className = 'doc-pin'; pin.textContent = i + 1; layer.appendChild(pin);
        var w = pin.offsetWidth, h = pin.offsetHeight;
        x = Math.max(0, x - w * 0.7); y = Math.max(0, y - h * 0.7);
        taken.forEach(function(t){ if (Math.abs(t[0] - x) < w && Math.abs(t[1] - y) < h) x = t[0] + w + 2; });
        taken.push([x, y]);
        pin.style.left = x + 'px'; pin.style.top = y + 'px';
        function show(){ hl.style.display = 'block'; hl.style.left = (r.left - b.left) + 'px'; hl.style.top = (r.top - b.top) + 'px';
                         hl.style.width = r.width + 'px'; hl.style.height = r.height + 'px'; }
        li.onmouseenter = show; li.onmouseleave = function(){ hl.style.display = 'none'; };
      });
    });
  }
  window.addEventListener('load', place); window.addEventListener('resize', place);
  if (document.fonts) document.fonts.ready.then(place);
  document.addEventListener('ds-theme', place);
  var t = document.querySelector('.kit-theme');
  if (t && document.documentElement.getAttribute('data-theme') === 'light') t.textContent = 'Dark theme';
})();
</script>"""


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def reprefix(frag, p):
    """A specimen shown twice on one page must not repeat its ids."""
    return re.sub(r'\b(id|for|aria-labelledby|aria-describedby|aria-controls)="([^"]+)"',
                  lambda m: f'{m.group(1)}="' + " ".join(p + v for v in m.group(2).split()) + '"', frag)


def files_for(cls):
    """Which files in components/ hold the classes a component is named by: a rule that starts with one of them
    (an element before it allowed). Failing that — input[type=checkbox], glyph-* — the one file that names it most."""
    files = [f for f in sorted((SYSTEM / "components").glob("*.css")) if f.name != "index.css"]
    texts = {f.name: f.read_text(encoding="utf-8") for f in files}
    tokens = [t.rstrip("-*") for t in re.findall(r"[a-z][a-z0-9*-]+", cls) if t not in ("type", "role")]
    found = [n for n, t in texts.items()
             if any(re.search(rf"(^|[,}}]\s*)[a-z]*\.{re.escape(c)}(?![\w])", t, re.M) for c in tokens)]
    if found:
        return found
    best = max(texts, key=lambda n: sum(len(re.findall(rf"{re.escape(c)}", texts[n])) for c in tokens))
    return [best]


def page(title, body, nav, name):
    src = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="stylesheet" href="wireframe.css">
  <style>{bk.concept_tokens.rename08(bk.PAGE_CSS.strip())}{DOC_CSS.strip()}</style>
</head>
<body class="product-page kit-page doc-page">
<header class="kit-top"><strong><a href="components.html" class="doc-home">Design system</a></strong><nav>{nav}</nav><button type="button" class="button-quiet kit-theme" onclick="var l=document.documentElement.getAttribute('data-theme')==='light';dsTheme(l?'dark':'light');this.textContent=l?'Light theme':'Dark theme';document.dispatchEvent(new Event('ds-theme'))">Light theme</button><span class="kit-meta">09 · Design system</span></header>
{body}
{STATES_JS if 'data-ds-target' in body else ''}
{PIN_JS}
</body>
</html>
"""
    unknown = []
    out = bm.transform(src, "../../", name, unknown, kit_href=HREF, frame=False)
    out = re.sub(r"<title>(.*?) — design</title>", r"<title>\1</title>", out)
    bad = concept_ui.literals(re.search(r"<style>(.*?)</style>", out, re.S).group(1))
    if bad:
        raise SystemExit(f"docs/{name}: the docs' own styles hold values: {bad}")
    return out


def demo(frag):
    return frag.replace(" inert", "")  # the wireframes draw dialogs over an inert page; a specimen is live


def nav_links():
    # kit.html retired in phase 09, step 7 (D2): the docs are the showcase
    return ('<a href="components.html">Components</a><a href="patterns.html">Patterns</a><a href="layouts.html">Layouts</a>'
            '<a href="tokens.html">Tokens</a><a href="why.html">Why it looks like this</a>')


DOCS_REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Design system · AI Stack Builder</title>
  <meta http-equiv="refresh" content="0; url=components.html">
  <link rel="canonical" href="components.html">
</head>
<body><p>The showcase is <a href="components.html">components.html</a>.</p></body>
</html>
"""


# ------------------------------------------------------------------ tokens (phase 09, step 7, S8)
def token_rows():
    """Every custom property in tokens.css: its level, its dark value, its light value where light overrides it, its
    comment, and the component files that read it. Read from the file as written, so the page cannot disagree with it."""
    text = (SYSTEM / "tokens.css").read_text(encoding="utf-8")
    root = text.split(":root {", 1)[1].split("\n}", 1)[0]
    prim, sem = root.split("SEMANTIC =====", 1)
    recipes = text.split(":root, [data-theme] {", 1)[1].split("\n}", 1)[0]
    light = text.split('[data-theme="light"] {', 1)[1].split("\n}", 1)[0]
    decl = re.compile(r"^\s*--([\w-]+)\s*:\s*(.*?);\s*(?:/\*\s*(.*?)\s*\*/)?\s*$", re.M)
    lightv = {m.group(1): m.group(2) for m in decl.finditer(light)}
    comps = {f.name: f.read_text(encoding="utf-8") for f in sorted((SYSTEM / "components").glob("*.css")) if f.name != "index.css"}
    rows = []
    for level, block in (("Primitive", prim), ("Semantic", sem), ("Recipe", recipes)):
        for m in decl.finditer(block):
            n = m.group(1)
            readers = [f.removesuffix(".css") for f, t in comps.items() if f"var(--{n})" in t]
            rows.append(dict(name=n, level=level, dark=m.group(2), light=lightv.get(n), why=m.group(3) or "", readers=readers))
    return rows


def is_colour(name, value):
    return name.startswith("color-") or bool(re.match(r"(#|rgba?\(|color-mix|var\(--color-|var\(--[a-z-]+\)$)", value)) and \
        not re.match(r"var\(--(space|radius|size|width|font|typescale|duration|ease|z|border)", value)


def tokens_page():
    rows = token_rows()
    sections = []
    for level, lead in (("Primitive", "What a value is, with no role: colour, type, space, radius, size, motion. A component reads geometry straight from here and colour never."),
                        ("Semantic", "What a colour is for. A theme overrides these and nothing else; the light column is the light block's own value, blank where light keeps the dark one."),
                        ("Recipe", "A wash, a hover, a pressed state or a shadow mixed over a role, declared wherever a theme is set, so it follows the role into either theme.")):
        trs = []
        for r in (r for r in rows if r["level"] == level):
            colour = is_colour(r["name"], r["dark"])
            sw = (f'<span class="doc-swatch" data-theme="dark" style="background:var(--{r["name"]})"></span>'
                  f'<span class="doc-swatch" data-theme="light" style="background:var(--{r["name"]})"></span>') if colour else ""
            light = f"<code>{E(r['light'])}</code>" if r["light"] else ""
            used = ", ".join(r["readers"]) if r["readers"] else "—"
            trs.append(f'<tr id="{E(r["name"])}"><td><code>--{E(r["name"])}</code></td><td class="doc-sw">{sw}</td>'
                       f'<td><code>{E(r["dark"])}</code></td><td>{light}</td><td>{E(r["why"])}</td><td>{E(used)}</td></tr>')
        sections.append(f"""<section class="doc-sec" id="{level.lower()}"><h2>{level} <span class="kit-meta">{len(trs)}</span></h2>
  <p class="doc-lead">{E(lead)}</p>
  <div class="doc-scroll"><table class="doc-table doc-tokens"><thead><tr><th>Token</th><th>Dark · light</th><th>Value</th><th>Light</th><th>What it is</th><th>Read by</th></tr></thead>
  <tbody>{"".join(trs)}</tbody></table></div>
</section>""")
    body = f"""<main class="kit-body">
<div class="kit-intro">
  <p class="doc-crumb"><a href="components.html">Design system</a> / Tokens</p>
  <h1>Tokens</h1>
  <p>Every value in <code>design-system/tokens.css</code>, {len(rows)} of them, read from the file at every build. The swatches are the token itself, drawn once in each theme. A value changes only in <code>tools/concept_tokens.py</code>, signed in <code>concept.md</code> (CLAUDE.md §18).</p>
</div>
{"".join(sections)}
</main>"""
    return page("Tokens · Design system", body, nav_links(), "tokens"), rows


# ------------------------------------------------------------------ layouts (phase 09, step 7, S7)
def layouts_page():
    mock = ROOT / "04-wireframes" / "mockups"
    blocks = []
    for lay in docs_content.LAYOUTS:
        on = sorted(p.stem for p in mock.glob("*.html") if f'class="{lay["cls"]}"' in p.read_text(encoding="utf-8")
                    or f'class="{lay["cls"]} ' in p.read_text(encoding="utf-8"))
        blocks.append(f"""<section class="doc-pattern" id="{lay['cls']}">
  <h2>{E(lay['name'])}</h2>
  <p class="doc-meta"><span><code>.{E(lay['cls'])}</code></span><span><code>components/{E(lay['file'])}</code></span><span>{len(on)} dressed pages</span></p>
  <div class="doc-prose"><p>{E(lay['what'])}</p></div>
  <iframe class="doc-frame" title="{E(lay['name'])}" data-src="../../04-wireframes/mockups/{lay['example']}.html" loading="lazy"></iframe>
  <div class="doc-rules">
    <div class="doc-rule"><p class="kit-label">Take it</p><p>{E(lay['when'])}</p></div>
    <div class="doc-rule doc-anti"><p class="kit-label">Take another</p><p>{E(lay['instead'])}</p></div>
  </div>
</section>""")
        lay["pages"] = on
    body = f"""<main class="kit-body">
<div class="kit-intro">
  <p class="doc-crumb"><a href="components.html">Design system</a> / Layouts</p>
  <h1>Layouts</h1>
  <p>The frames a screen is set in. A layout holds components and places them; it has no colour of its own beyond the ground. Each frame below is a dressed screen that uses it.</p>
</div>
{"".join(blocks)}
</main>"""
    return page("Layouts · Design system", body, nav_links(), "layouts").replace("</body>", FRAME_JS + "</body>")


STATE_COLS = [("rest", "Rest"), ("hover", "Hover"), ("active", "Active"), ("focus", "Focus-visible"), ("disabled", "Disabled")]


def states_block(c):
    """Phase 09, step 3: the four states, beside rest, in dark and in light."""
    if c.name in docs_content.STATIC:
        why, to = docs_content.STATIC[c.name]
        more = f' → <a href="{slug(to)}.html">{E(to)}</a>' if to else ""
        return f'<div class="doc-static"><p>No state of its own. {E(why)}{more}</p></div>'
    tables = []
    for k, spec in enumerate(docs_content.STATES[c.name]):
        cut = spec["cut"]
        frag = bk.outer(demo(c.states[spec["of"]].demo), cut[0], cut[1], cut[2] if len(cut) > 2 else None,
                        cut[3] if len(cut) > 3 else 0, page=c.name)
        frag = spec.get("wrap", "{}").format(frag)
        na = spec.get("na", {})
        cells = ['<span></span>'] + [f'<p class="kit-label">{lab}</p>' for _, lab in STATE_COLS]
        for theme in ("dark", "light"):
            cells.append(f'<p class="kit-label">{theme.capitalize()}</p>')
            for st, _lab in STATE_COLS:
                bar = " is-bar" if spec.get("bar") else ""
                if st in na:
                    cells.append(f'<div class="doc-cell doc-na{bar}" data-theme="{theme}">{E(na[st])}</div>')
                    continue
                f = reprefix(frag, f"s{k}{theme[0]}{st}-")
                cells.append(f'<div class="doc-cell{bar}" data-theme="{theme}" data-ds-state="{st}"><div class="kit-demo">{f}</div></div>')
        cap = f'<p class="kit-label">{E(spec["label"])}</p>' if spec.get("label") else ""
        tables.append(f'<div class="doc-states-wrap" data-ds-target="{E(spec["target"])}">{cap}<div class="doc-states">{"".join(cells)}</div></div>')
    return ("".join(tables) + '<p class="doc-states-note">Each state is held on the live component by copying the '
            "product's own :hover, :active and :focus-visible rules onto an attribute; disabled is the real attribute. "
            "Pressed was signed by the owner on 2026-11-03 (Q49).</p>")


# ------------------------------------------------------------------ one page per component
def comp_page(group, c, prev, nxt):
    d = docs_content.C[c.name]
    st = c.states[d.get("anat", 0)]
    parts = "".join(f'<li data-sel="{E(sel)}"><span><b>{E(part)}</b> — {E(what)}</span><code>{E(sel)}</code></li>'
                    for sel, part, what in d["parts"])
    anatomy = (f'<div class="doc-anatomy" data-anatomy><div class="kit-demo">{reprefix(demo(st.demo), "a-")}</div>'
               f'<div class="doc-pins"></div><div class="doc-hl"></div></div><ol class="doc-parts">{parts}</ol>')
    files = d.get("files") or files_for(c.cls)
    size = f'<p class="doc-size">Size: {E(d["size"])}</p>' if d.get("size") else ""
    anti_text, anti_to = d["anti"]
    body = f"""<main class="kit-body">
<div class="kit-intro">
  <p class="doc-crumb"><a href="components.html">Design system</a> / {E(group)}</p>
  <h1>{E(c.name)}</h1>
  <p>{E(d["when"].split(". ")[0].rstrip("."))}.</p>
  <p class="doc-meta"><span><code>{E(c.cls)}</code></span><span>{E(c.screens)}</span><span>{" · ".join(f"<code>components/{f}</code>" for f in files)}</span></p>
</div>
<section class="doc-sec" id="anatomy"><h2>Anatomy</h2>
  <p class="doc-lead">The live component, drawn on <code>design-system/index.css</code> as every screen is. Point at a part to see it.</p>
  {anatomy}
</section>
<section class="doc-sec" id="variants"><h2>Variants and states <span class="kit-meta">{len(c.states)}</span></h2>
  <p class="doc-lead">Every variant and state <code>inventory.md</code> lists, each cut from a screen that has it.</p>
  {"".join(reprefix(demo(s), f"v{i}-") for i, s in enumerate(c.states))}
  {size}
</section>
<section class="doc-sec" id="states"><h2>States</h2>
  <p class="doc-lead">Hover, active, focus-visible and disabled, beside rest, in both themes. No state moves the component or changes its size.</p>
  {states_block(c)}
</section>
<section class="doc-sec" id="when"><h2>When to use</h2>
  <div class="doc-prose"><p>{E(d["when"])}</p></div>
</section>
<section class="doc-sec" id="rule"><h2>Rule and anti-rule</h2>
  <div class="doc-rules">
    <div class="doc-rule"><p class="kit-label">Use it</p><p>{E(d["rule"])}</p></div>
    <div class="doc-rule doc-anti"><p class="kit-label">Take another</p><p>{E(anti_text)} → <a href="{slug(anti_to)}.html">{E(anti_to)}</a></p></div>
  </div>
</section>
<nav class="doc-pager" aria-label="Components">{f'<a href="{slug(prev.name)}.html">← {E(prev.name)}</a>' if prev else '<span></span>'}{f'<a href="{slug(nxt.name)}.html">{E(nxt.name)} →</a>' if nxt else '<span></span>'}</nav>
</main>"""
    return page(f"{c.name} · Design system", body, nav_links(), slug(c.name))


# ------------------------------------------------------------------ the showcase
def index_page(groups, counts):
    cards = []
    n = 0
    for gname, comps in groups.items():
        items = []
        for c in comps:
            n += 1
            d = docs_content.C[c.name]
            first = reprefix(demo(c.states[d.get("anat", 0)].demo), f"i{n}-")
            # I2: a preview is a picture of the page it links to; its headings stay out of the showcase's outline
            items.append(f'<article class="doc-card"><div class="doc-preview" inert aria-hidden="true"><div class="kit-demo">{first}</div></div>'
                         f'<h3><a href="{slug(c.name)}.html">{E(c.name)}</a></h3><p>{len(c.states)} '
                         f'{"state" if len(c.states) == 1 else "states"} · {E(c.screens)}</p></article>')
        cards.append(f'<section class="doc-group" id="{slug(gname)}"><h2>{E(gname)} <span class="kit-meta">{len(comps)}</span></h2>'
                     f'<div class="doc-grid">{"".join(items)}</div></section>')
    body = f"""<main class="kit-body">
<div class="kit-intro">
  <h1>AI Stack Builder · Mica · Lime</h1>
  <p>The product's look as one package. Every screen links one file, and so does this page: the components below are not pictures of the product, they are the product's own markup on the product's own stylesheet. Switch the theme at the top right and every one of them changes, because a theme overrides roles and nothing else.</p>
</div>
<div class="doc-facts">
  <div><b>{counts["comps"]}</b><span>components, each with a page</span></div>
  <div><b>{counts["states"]}</b><span>variants and states, cut from the screens</span></div>
  <div><b>{counts["files"]}</b><span>files in components/</span></div>
  <div><b>{counts["roles"]}</b><span>semantic roles, dark and light</span></div>
</div>
<div class="doc-entry">
  <p class="kit-label">One entry point</p>
  <pre>&lt;link rel="stylesheet" href="design-system/index.css"&gt;</pre>
  <p class="doc-lead"><code>index.css</code> imports <code>tokens.css</code> (the values: primitive, then semantic) and <code>components/index.css</code> (one file per component). A component reads colour only through a role. Why it looks like this is <a href="why.html">its own page</a>.</p>
</div>
{"".join(cards)}
</main>"""
    return page("Design system · AI Stack Builder", body, nav_links(), "components")


# ------------------------------------------------------------------ patterns (phase 09, step 4)
FRAME_JS = r"""<script>
(function(){
  function theme(){ return document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark'; }
  function load(){ document.querySelectorAll('iframe[data-src]').forEach(function(f){ f.src = f.getAttribute('data-src') + '?theme=' + theme(); }); }
  load(); document.addEventListener('ds-theme', load);
})();
</script>"""


def patterns_page(pats, rejected):
    blocks = []
    for p in pats:
        parts = " · ".join(f'<a href="{slug(n)}.html">{E(n)}</a>' for n in p["parts"])
        where = "; ".join(f"<strong>{E(sc)}</strong> <code>{E(', '.join(v))}</code>" for sc, v in p["screens"].items())
        under = (f' Also drawn under {", ".join(E(o) for o in p["overlays"])}, which are overlays and not counted.'
                 if p["overlays"] else "")
        blocks.append(f"""<section class="doc-pattern" id="{p['slug']}">
  <h2>{E(p['name'])}</h2>
  <p class="doc-meta"><span>Made of: {parts}</span><span><code>patterns/{p['slug']}.html</code></span></p>
  <div class="doc-prose"><p>Stands on {len(p['screens'])} screens: {where}.{under}</p></div>
  <iframe class="doc-frame" title="{E(p['name'])}" data-src="../patterns/{p['slug']}.html" loading="lazy"></iframe>
  <div class="doc-rules">
    <div class="doc-rule"><p class="kit-label">Take the pattern</p><p>{E(p['when'])}</p></div>
    <div class="doc-rule doc-anti"><p class="kit-label">Take the components</p><p>{E(p['instead'])}</p></div>
  </div>
</section>""")
    rej = "".join(f"<tr><td>{E(n)}</td><td>{E(w)}</td></tr>" for n, w in rejected)
    body = f"""<main class="kit-body">
<div class="kit-intro">
  <p class="doc-crumb"><a href="components.html">Design system</a> / Patterns</p>
  <h1>Patterns</h1>
  <p>A pattern is a composition of components that already stands on three screens or more. Each one here was found on the screens, not designed for them: its signature is run over all 80 wireframe pages at every build, and the build fails if it stands on fewer than three. A screen counts once, and an overlay never counts. Every pattern is a file in <code>design-system/patterns/</code> with no style of its own — the frames below are those files.</p>
</div>
<section class="doc-sec"><h2>Pattern or components</h2>
  <div class="doc-prose"><p><strong>Take a pattern</strong> when the screen does the job the pattern already does somewhere else: the same parts, in the same order, for the same reason. Then the screen inherits a layout that has been reviewed three times, and a person who has seen one of those screens already knows how this one works.</p>
  <p><strong>Take the components</strong> when the job differs even if the parts are the same — a place with one thing in it needs no search; a step that can be undone needs no confirmation. And when a composition is on one or two screens only: it is not a pattern yet. If it reaches a third, it is added here, with the three screens named.</p></div>
</section>
{"".join(blocks)}
<section class="doc-sec"><h2>Looked at, and not a pattern</h2>
  <table class="doc-table"><thead><tr><th>Composition</th><th>Why not</th></tr></thead><tbody>{rej}</tbody></table>
</section>
</main>"""
    return page("Patterns · Design system", body, nav_links(), "patterns").replace("</body>", FRAME_JS + "</body>")


# ------------------------------------------------------------------ why it looks like this
def why_page(groups):
    by = {c.name: c for comps in groups.values() for c in comps}

    def live(name, i=0):
        return f'<div class="kit-demo">{reprefix(demo(by[name].states[i].demo), f"w{slug(name)}{i}-")}</div>'

    taste = [("Vercel", "A clean interface without decoration: the status, the fact and the consequence stand side by side. "
                        "Monochrome; colour only where it means something."),
             ("Figma", "A dense working surface. A lot on screen, and it does not look overloaded, because the hierarchy is "
                       "held by the grid and the type, not by colour."),
             ("Teams and Slack", "Glass: translucent layers. The product's signature touch — noticeable, used sparingly.")]
    refused = ["The palette an AI produces for the words “AI tool”: a dark ground, violet-blue neon gradients, glow.",
               "A marketplace showcase: Verified and Popular badges, stars, ratings, cover cards.",
               "Glass everywhere: translucent content, text on a blur, glass that eats contrast.",
               "A green tick as the main signal. It promises works, and we run nothing."]
    pairs = [("An inspector's report, not a seller's badge",
              "A verdict is facts side by side: what was examined, how long it took, the counts. Never a seal — no score, no "
              "rating, no green badge standing in for a sentence.", "Data: EJ-2, believe that a clean result was earned"),
             ("Dense and counted, not spacious and showcased",
              "A row carries many small facts at once. Hierarchy comes from the grid and the type weight, not from colour or "
              "cards; a count sits by what it counts.", "Data for the counts; taste for Figma"),
             ("The consequence is visible before the step, not after it",
              "The sentence that names a cost sits inside the control it applies to, above the button — never a toast "
              "afterwards, never Are you sure?", "Data: EJ-1"),
             ("Glass is a layer over the work, not the work itself",
              "Glass only on a temporary surface — a dialog, the Filters popover. What a person reads to decide something is "
              "opaque, and text always sits on a sheet.", "Taste; data only for where"),
             ("Colour is a claim, held back",
              "The interface is greyscale. Colour appears only where it states something the product knows: a Problem, a "
              "Note, what you can press, where you are.", "Data: §5's refusal of badges; taste: Vercel")]
    rounds = [("Round 1", "Acrylic · Manifest · Catalogue", "Turned down.", False),
              ("Round 2", "Glasshouse · Kit · Warm", "Turned down — but Kit's cut-out row came back in round 4.", False),
              ("Round 3", "Mica · Cut-out · Canon", "Mica kept, and a density between Default and Comfortable.", False),
              ("Round 4", "Mica · Cobalt · Jade · Lime", "Lime, in Kit's cut-out form. Fixed on 2026-10-11.", True)]
    refs = [("Linear — the base", "Its system, not its surface: three surfaces, edges by hairline rather than shadow, three "
             "text tones, colour only for meaning, dimmed counts beside a group's label. No violet, nothing of its brand.",
             "Every item in its own cut-out in a tray, held by hairlines and three inks.", "Row list", 0),
            ("Vercel — two devices", "B1: a stage is name, duration and a verdict glyph at the right, expanding in place. "
             "B2: status is a dot and a word, never a filled pill. A duration beside a verdict is evidence it looked.",
             "Run's stages, and Checked as a quiet dot.", "Check stages", 0),
            ("GitHub Actions — two devices", "C1: Skipped is its own neutral glyph, a slashed circle. C2: a count sits in a "
             "small grey capsule after a tab's label. Not taken: the filled green disc on a passed job.",
             "The kind tabs with their counts.", "Tabs", 0),
            ("Raycast Store — one device", "D1: a dimmed metadata line under the description, quiet enough not to compete "
             "with the name. Not taken: its red ribbons, store-sized icons and centred marketing layout.",
             "The usage facts on a Library row.", "Usage facts", 0)]
    style = [("Material", "Mica: a neutral ground with a faint lime tint, quiet layers — tray, cut-out, raised.", "The owner's taste for glass, held to pair 4"),
             ("Brand", "Lime, only on what you can press and where you are. Never a verdict.", "Pair 5"),
             ("Severities", "Problem in rose, Note in amber, as tinted tags with an icon and a word. Checked is a quiet dot; Skipped is ban.", "§6; pair 1; D1-B"),
             ("Glass", "Acrylic only round a dialog and the Filters popover: an 8 px translucent edge, the sheet inside opaque.", "Pair 4; owner, 2026-10-19"),
             ("Type", "Geist for what a person reads, Geist Mono for what a machine reads.", "The owner's word"),
             ("Icons", "Lucide, 1.75 px stroke, one style.", "Owner, round 4"),
             ("Shape", "Soft, not round: 6 on a control, 10 on a cut-out, 14 on a panel, a pill on a tag. The radius grows with the thing, so nesting reads.", "Owner, round 4"),
             ("Depth", "Hairlines first. A shadow only where something is lifted: the current place, a segment, a dialog.", "Linear; pair 4"),
             ("Density", "Between Default and Comfortable: 32 px controls, 12 px row padding, body at 14.5.", "Owner, round 3"),
             ("Red", "Only on the step that removes, in its confirmation. Amber only for going ahead despite a Problem.", "Owner, 2026-10-11")]
    body = f"""<main class="kit-body">
<div class="kit-intro">
  <p class="doc-crumb"><a href="components.html">Design system</a> / Why</p>
  <h1>Why it looks like this</h1>
  <p>The product reads like an inspection, not a sales sheet: it says what was examined, counts what it found and names the cost before the step. Every value in the system traces to a line of the owner's taste or to one of five attributes, written before anything was drawn. This page is read from <code>06-concept/concept.md</code> and <code>06-concept/references.md</code>; the specimens on it are live.</p>
</div>
<section class="doc-sec"><h2>The owner's taste</h2>
  <div class="doc-pairs">{"".join(f'<div class="doc-pair"><p class="kit-label">Likes</p><h3>{E(n)}</h3><p>{E(t)}</p></div>' for n, t in taste)}</div>
  <div class="doc-prose"><p><strong>Does not want.</strong></p>{"".join(f"<p>— {E(r)}</p>" for r in refused)}</div>
</section>
<section class="doc-sec"><h2>Five attributes <span class="kit-meta">this, not that</span></h2>
  <p class="doc-lead">Each pair names the line of data it stands on, or says it is taste. A direction that broke a pair was not drawn.</p>
  <div class="doc-pairs">{"".join(f'<div class="doc-pair"><p class="kit-label">{i}</p><h3>{E(t)}</h3><p>{E(m)}</p><p class="kit-meta">{E(s)}</p></div>' for i, (t, m, s) in enumerate(pairs, 1))}</div>
</section>
<section class="doc-sec"><h2>Four rounds to Mica · Lime</h2>
  <p class="doc-lead">Three directions a round, each drawn on the same sample; the owner chose in the browser. <a href="../../06-concept/directions.html">Round 1</a> · <a href="../../06-concept/directions-2.html">2</a> · <a href="../../06-concept/directions-3.html">3</a> · <a href="../../06-concept/directions-4.html">4</a> · <a href="../../06-concept/style.html">the phase page</a></p>
  <ol class="doc-rounds">{"".join(f'<li class="{"is-kept" if k else ""}"><p class="kit-label">{E(r)}</p><b>{E(n)}</b><span>{E(o)}</span></li>' for r, n, o, k in rounds)}</ol>
</section>
<section class="doc-sec"><h2>Where each device came from</h2>
  <p class="doc-lead">None is copied whole. Each reference gives a named device and the worry it removes; what was refused is named too, because each refused thing claims more than this product knows.</p>
  {"".join(f'<div class="doc-ref"><div class="doc-prose"><h3>{E(h)}</h3><p>{E(t)}</p><p><strong>Here:</strong> {E(w)} → <a href="{slug(c)}.html">{E(c)}</a></p></div>{live(c, i)}</div>' for h, t, w, c, i in refs)}
</section>
<section class="doc-sec"><h2>The working style</h2>
  <table class="doc-table"><thead><tr><th>Decision</th><th>What it is</th><th>Stands on</th></tr></thead><tbody>
  {"".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in style)}
  </tbody></table>
</section>
<section class="doc-sec"><h2>Colour is a claim, on screen</h2>
  <p class="doc-lead">The severity marks, live: colour only where the product knows something. There is no success colour; the best a check can say is Checked.</p>
  {live("Severity glyph")}
  {live("Finding capsule")}
</section>
</main>"""
    return page("Why it looks like this · Design system", body, nav_links(), "why")


# ------------------------------------------------------------------ checks
def check_content(groups):
    names = [c.name for comps in groups.values() for c in comps]
    missing = [n for n in names if n not in docs_content.C]
    extra = [n for n in docs_content.C if n not in names]
    dangling = [f"{n} → {d['anti'][1]}" for n, d in docs_content.C.items() if d["anti"][1] not in names]
    bad_anat = [n for n in names if n in docs_content.C and docs_content.C[n].get("anat", 0) >= len(
        next(c for comps in groups.values() for c in comps if c.name == n).states)]
    no_states = [n for n in names if n not in docs_content.STATES and n not in docs_content.STATIC]
    if missing or extra or dangling or bad_anat or no_states:
        raise SystemExit(f"docs_content: no entry for {missing}; no component for {extra}; anti-rule to nothing: {dangling}; "
                         f"anatomy on a state that does not exist: {bad_anat}; no States spec and no reason in STATIC: "
                         f"{no_states}. A component enters the system with its page and its states in both themes — "
                         "CLAUDE.md §18, Contributing to the system.")


def check_words(groups):
    """The specimens' words are the product's: the kit's own check, run on every specimen the docs show."""
    demos = "".join(demo(s.demo) for comps in groups.values() for c in comps for s in c.states)
    out = bk.finish(bk.page("words", "", f'<main class="kit-body">{demos}</main>', ""), "words")
    return [w for w in bk.words_check(out) if not re.fullmatch(r"\d+(\.\d+)? s", w)]


def check_browser(pages):
    """Every anatomy part is found in its live specimen, with a size."""
    from playwright.sync_api import sync_playwright
    js = """() => [...document.querySelectorAll('.doc-parts li')].map(li => {
        const box = li.closest('section').querySelector('[data-anatomy] .kit-demo');
        const el = box.querySelector(li.dataset.sel);
        if (!el) return li.dataset.sel + ' (nothing)';
        const r = el.getBoundingClientRect();
        return r.width && r.height ? '' : li.dataset.sel + ' (no size)';
      }).filter(Boolean)"""
    bad = {}
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 1440, "height": 900})
        for f in pages:
            pg.goto(f.as_uri(), wait_until="load")
            miss = pg.evaluate(js)
            if miss:
                bad[f.name] = miss
        br.close()
    return bad


STATE_JS_CHECK = """() => {
  const PROPS = ['background-color', 'color', 'border-top-color', 'border-bottom-color', 'box-shadow', 'text-decoration-line',
                 'text-decoration-color'];
  const FOCUSABLE = 'a[href],button,input:not([type=hidden]),select,textarea,summary';
  const bad = [], seen = [];
  if (document.documentElement.classList.contains('doc-states-off')) return ['the product CSS could not be read'];
  document.querySelectorAll('[data-ds-target]').forEach((wrap, w) => {
    const sel = wrap.getAttribute('data-ds-target');
    const cells = [...wrap.querySelectorAll('.doc-cell')];
    for (const theme of ['dark', 'light']) {
      const row = cells.filter(c => c.getAttribute('data-theme') === theme);
      const look = cell => {
        const root = cell.querySelector('.kit-demo');
        const t = sel ? root.querySelector(sel) : root.firstElementChild;
        if (!t) return null;
        const f = t.matches(FOCUSABLE) ? t : t.querySelector(FOCUSABLE);
        const els = [t, f].filter(Boolean);
        for (let e = t.parentElement; e && e !== cell; e = e.parentElement) els.push(e);
        const sig = els.map(e => { const cs = getComputedStyle(e), bf = getComputedStyle(e, '::before');
          return PROPS.map(p => cs.getPropertyValue(p)).join('|') + '|' + bf.getPropertyValue('background-color'); }).join('#');
        const r = t.getBoundingClientRect();
        return {sig, w: r.width, h: r.height};
      };
      const rest = look(row[0]);
      if (!rest) { bad.push(`${w} ${theme}: target ${sel} not found`); continue; }
      row.slice(1).forEach(cell => {
        const st = cell.getAttribute('data-ds-state');
        if (!st) return;
        const now = look(cell);
        if (!now) { bad.push(`${w} ${theme} ${st}: target ${sel} not found`); return; }
        if (now.sig === rest.sig) bad.push(`${w} ${theme} ${st}: looks the same as rest`);
        if (Math.abs(now.w - rest.w) > 0.5 || Math.abs(now.h - rest.h) > 0.5) bad.push(`${w} ${theme} ${st}: changes size`);
      });
    }
  });
  return bad;
}"""


def check_states(pages):
    """Over http (a file:// page may not read its own stylesheets' rules): every state the docs draw differs from rest
    on the live component, in both themes, and changes nothing's size."""
    import functools, http.server, threading
    from playwright.sync_api import sync_playwright
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    handler = functools.partial(Quiet, directory=str(ROOT))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    bad = {}
    try:
        with sync_playwright() as p:
            br = p.chromium.launch()
            pg = br.new_page(viewport={"width": 1440, "height": 900})
            for f in pages:
                url = f"http://127.0.0.1:{srv.server_port}/" + f.relative_to(ROOT).as_posix()
                pg.goto(url, wait_until="load")
                miss = pg.evaluate(STATE_JS_CHECK)
                if miss:
                    bad[f.name] = miss
            br.close()
    finally:
        srv.shutdown()
    return bad


def build(browser=True):
    groups = bk.components()
    check_content(groups)
    OUT.mkdir(parents=True, exist_ok=True)
    flat = [(g, c) for g, comps in groups.items() for c in comps]
    written = []
    for i, (g, c) in enumerate(flat):
        prev = flat[i - 1][1] if i else None
        nxt = flat[i + 1][1] if i + 1 < len(flat) else None
        f = OUT / f"{slug(c.name)}.html"
        f.write_text(comp_page(g, c, prev, nxt), encoding="utf-8")
        written.append(f)
    tokens = (SYSTEM / "tokens.css").read_text(encoding="utf-8")
    sem = tokens.split("SEMANTIC =====", 1)[1].split("[data-theme", 1)[0]
    counts = {"comps": len(flat), "states": sum(len(c.states) for _, c in flat),
              "files": len([f for f in (SYSTEM / "components").glob("*.css") if f.name != "index.css"]),
              "roles": len(set(re.findall(r"^\s*--([\w-]+):\s*var\(--color-", sem, re.M)))}
    (OUT / "components.html").write_text(index_page(groups, counts), encoding="utf-8")
    (OUT / "index.html").write_text(DOCS_REDIRECT, encoding="utf-8")  # I6: the folder's address lands on the showcase
    (OUT / "why.html").write_text(why_page(groups), encoding="utf-8")
    import build_patterns
    pats = build_patterns.build()
    (OUT / "patterns.html").write_text(patterns_page(pats, build_patterns.REJECTED), encoding="utf-8")
    tok, rows = tokens_page()
    (OUT / "tokens.html").write_text(tok, encoding="utf-8")
    (OUT / "layouts.html").write_text(layouts_page(), encoding="utf-8")
    print(f"docs: tokens.html ({len(rows)} tokens) · layouts.html ({len(docs_content.LAYOUTS)} layouts)")
    words = check_words(groups)
    if words:
        raise SystemExit(f"docs: words in specimens not in microcopy.md: {words}")
    print(f"docs: {len(flat)} component pages · components.html · why.html · {counts['states']} specimens · "
          f"{counts['roles']} roles · words not in microcopy.md: 0")
    if browser:
        bad = check_browser(written)
        if bad:
            raise SystemExit("docs: anatomy parts not found in their specimen:\n  " +
                             "\n  ".join(f"{k}: {v}" for k, v in bad.items()))
        print(f"docs: every anatomy part found in its live specimen ({len(written)} pages)")
        bad = check_states(written)
        if bad:
            raise SystemExit("docs: States block — a state that is not one:\n  " +
                             "\n  ".join(f"{k}: {v}" for k, v in bad.items()))
        print("docs: every state drawn differs from rest and moves nothing, in both themes")


if __name__ == "__main__":
    build(browser="--fast" not in sys.argv)
