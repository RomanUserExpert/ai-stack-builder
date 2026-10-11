"""Phase 06: build 06-concept/mica-lime.html — the screens in the working style, Mica · Lime.

Fixed by the owner on 2026-10-11 (06-concept/concept.md, *Working style*). Since stage 4 the page
links 06-concept/tokens.css and holds no value of its own: the components are tools/concept_ui.py,
the page around them below uses var() only. The stand, with the system laid out, is concept.html.

    python tools/build_lime.py   -> 06-concept/mica-lime.html

Markup (every word from microcopy.md) comes from tools/build_directions_2.py; Lucide icons from
tools/build_directions_4.py.
"""
from pathlib import Path
import importlib.util
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import concept_ui  # noqa: E402

_spec = importlib.util.spec_from_file_location("bd4", ROOT / "tools" / "build_directions_4.py")
bd4 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bd4)
bd2 = bd4.bd2
OUT = ROOT / "06-concept" / "mica-lime.html"
LIME = next(d for d in bd4.DIRS if d["id"] == "lime")
FONTS = "https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap"

PAGE_CSS = r"""
*{box-sizing:border-box}
html{background:var(--page)}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
body{margin:0;background:var(--page);color:var(--page-ink);font:var(--t-body)}
.pagehead,.sec,.pagefoot{max-width:calc(var(--canvas) + var(--s12) * 3);margin:0 auto;padding-left:var(--s6);padding-right:var(--s6)}
.pagehead{padding-top:var(--s10)}
.pagehead h1{font:var(--t-display);letter-spacing:var(--track-display);margin:0 0 var(--s3)}
.pagehead p{margin:0 0 var(--s3);color:var(--page-ink-2);max-width:var(--measure-wide)}
.pagehead p b{color:var(--page-ink)}
.pagehead a{color:var(--page-ink)}
.bar{position:sticky;top:0;z-index:5;display:flex;gap:var(--s2);align-items:center;margin:var(--s5) calc(var(--s6) * -1) 0;padding:var(--s3) var(--s6);background:var(--page);border-bottom:var(--hairline) solid var(--page-line)}
.bar .k{font:var(--t-small);color:var(--page-ink-2);margin-right:var(--s1)}
.bar a{font:var(--t-button);font-weight:600;color:var(--page-ink);text-decoration:none;padding:var(--s2) var(--s3);border-radius:var(--r-sm);border:var(--hairline) solid var(--page-line);background:var(--page-2)}
.bar a:focus-visible{outline:0;box-shadow:var(--shadow-focus)}
.sec{padding-top:var(--s8)}
.sec>h2{font:var(--t-title);letter-spacing:var(--track-title);margin:0 0 var(--s2);scroll-margin-top:var(--s12)}
.sec>p{color:var(--page-ink-2);margin:0 0 var(--s4);max-width:var(--measure-wide)}
.pagefoot{padding-top:var(--s6);padding-bottom:var(--s12);color:var(--page-ink-2);font:var(--t-small)}
.scale{width:100%;overflow:hidden;border-radius:var(--r-md);box-shadow:0 0 0 var(--hairline) var(--line);background:var(--ground)}
.native{width:var(--canvas);transform-origin:0 0}
.app{min-height:calc(var(--canvas) * .6)}
.runwrap{height:calc(var(--canvas) * .9)}
"""

JS = r"""
(function(){
  var C=parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--canvas'))||1280;
  function fit(){document.querySelectorAll('.scale').forEach(function(s){
    var n=s.firstElementChild,w=s.clientWidth,k=Math.min(1,w/C);
    n.style.width=(w>C?w:C)+'px';n.style.transform='scale('+k+')';s.style.height=(n.offsetHeight*k)+'px';});}
  window.addEventListener('resize',fit);
  if(document.fonts&&document.fonts.ready){document.fonts.ready.then(fit);}
  window.addEventListener('load',fit);fit();
})();
"""


def trim_sprite(page):
    """Only the symbols the page uses (stage 7, #25)."""
    import re as _re
    used = set(_re.findall(r'<use href="#([^"]+)"', page))
    return _re.sub(r'<symbol id="([^"]+)"[^>]*>.*?</symbol>', lambda m: m.group(0) if m.group(1) in used else "", page, flags=_re.S)


def build():
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mica Lime screens · AI Stack Builder</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}"><link rel="stylesheet" href="tokens.css">
<style>{PAGE_CSS}{concept_ui.UI_CSS}</style></head>
<body>{bd4.symbols()}
<header class="pagehead">
  <h1>Mica · Lime — the screens</h1>
  <p>The working style on the fixed sample. Every value comes from <a href="tokens.css">tokens.css</a>; the system itself is laid out on <a href="concept.html">the stand</a>. Every word on the screens is from <code>microcopy.md</code>.</p>
  <div class="bar"><span class="k">Jump to</span><a href="#screen">The screen</a><a href="#export">Export</a><a href="#dialog">Dialog</a><a href="concept.html">The stand</a></div>
</header>
<div class="ml">
<section class="sec" id="screen" aria-labelledby="screen-h"><h2 id="screen-h">The project, with eslint-autofix open</h2><p>1:1 on the canvas width.</p>
  <div class="scale"><div class="native">{bd2.app(LIME)}</div></div></section>
<section class="sec" id="export" aria-labelledby="export-h"><h2 id="export-h">Export, over the project</h2><p>Acrylic only around the mode; the findings sit on an opaque sheet. No ring on a stage: its verdict is its icon and its words.</p>
  <div class="scale"><div class="native">{bd2.run(LIME, False)}</div></div></section>
<section class="sec" id="dialog" aria-labelledby="dialog-h"><h2 id="dialog-h">The remove dialog, over Export</h2><p>The same acrylic frame, smaller; the question on an opaque sheet; the remove in solid red.</p>
  <div class="scale"><div class="native">{bd2.run(LIME, True)}</div></div></section>
</div>
<p class="pagefoot">Built by <code>tools/build_lime.py</code>. Icons: Lucide (ISC). Portrait: Jake Nackos on Unsplash (unsplash.com/photos/IF9TK5Uy-KI).</p>
<script>{JS}</script></body></html>'''
    # one <main> per page: each screen is a labelled region (stage 7, #20)
    page = page.replace('<main class="main">', '<div class="main" role="region" aria-label="Mockup of the Project screen">').replace('</main></div>', '</div></div>')
    # tones by class, never by context (#12, #13)
    page = page.replace('<span class="btn">Remove eslint-autofix…</span>', '<span class="btn danger-ghost">Remove eslint-autofix…</span>')
    page = page.replace('<span class="btn primary">Remove from project</span>', '<span class="btn danger">Remove from project</span>')
    page = trim_sprite(page)
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}  {len(page)//1024} KB · page literals: {concept_ui.literals(PAGE_CSS) or 'none'}")


if __name__ == "__main__":
    build()
