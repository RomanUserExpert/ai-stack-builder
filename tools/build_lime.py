"""Phase 06, stage 3 → 4: build 06-concept/mica-lime.html — finishing the working style.

The owner fixed *Mica · Lime* as the working style on 2026-10-11 and asked for options on three
axes before it is finalised: navigation, how the active item is marked, and how a finding (Problem,
Note) is shown — without the coloured rings round the rows. Lucide is the icon library from now on.

    python tools/build_lime.py   -> 06-concept/mica-lime.html

Every option is one class on the sample's wrapper, so any navigation can be combined with any
selection and any finding style. Markup from tools/build_directions_2.py; tokens and base CSS from
tools/build_directions_4.py.
"""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("bd4", ROOT / "tools" / "build_directions_4.py")
bd4 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bd4)
bd2, ratio = bd4.bd2, bd4.ratio
OUT = ROOT / "06-concept" / "mica-lime.html"

LIME = next(d for d in bd4.DIRS if d["id"] == "lime")

NAV = [
    ("n1", "Top bar", "What round 4 drew: the three places as tabs in a bar across the top, the current one underlined in lime. The widest room for the set; the places are always in one line of sight."),
    ("n2", "Sidebar", "Fluent’s NavigationView: a left column with icon and label, the current place marked by a short lime pill. Room for more places later (a shared project, settings) without crowding the head."),
    ("n3", "Icon rail", "A narrow rail of icons with small labels under them, the current one on a lime-tinted tile. The most room for the work; the labels keep it readable without hovering."),
]
TOP = [
    ("t1", "Under-pill", "The same short lime pill as the active row (S2), turned on its side under the label. One indicator for “you are here” across the whole product."),
    ("t2", "Segmented", "The three places sit in a recessed track; the current one is a raised tile. No lime in the bar at all — only the icon of the current place is lime."),
    ("t3", "Lime capsule", "The current place is a capsule tinted with lime, its icon in full lime and the label in white. The most visible of the four."),
    ("t4", "Dot and weight", "No shape at all: the current label turns white and semibold with a small lime dot before it; the others stay grey. The quietest."),
]
SEL = [
    ("s1", "Tint", "The active cut-out fills with a faint lime tint. No line at all; the row reads as lit."),
    ("s2", "Pill", "Fluent’s selection indicator: a short lime pill at the left edge of the cut-out, the cut-out itself one step lighter."),
    ("s3", "Lift", "The active cut-out rises: a lighter surface and a soft shadow, as if picked out of the tray. No colour on the selection at all — lime stays for actions."),
]
FIND = [
    ("f1", "Tag", "The finding is a small tag on the right — a tinted capsule with the icon and the word. The row stays neutral."),
    ("f2", "Mark", "The quietest: the icon and the word in the finding’s colour, no capsule — the dot-and-word of Vercel (device B2)."),
    ("f3", "Gutter", "The finding’s icon stands in a column at the left, before the name, so a scan down the edge finds every Problem and Note; the word stays on the right in grey."),
]


def sample(cls, crop_h, offset=0, overlay=False):
    body = bd2.run(LIME, False) if overlay else bd2.app(LIME)
    return (f'<div class="scale" data-h="{crop_h}" data-o="{offset}"><div class="native {cls}">{body}</div></div>')


def option_block(axis_id, title, intro, opts, base, crop_h, offset):
    cards = []
    for oid, name, why in opts:
        cls = base.replace("{axis}", oid)
        cards.append(f'''<article class="opt" id="{oid}"><header><h3><span class="oid">{oid.upper()}</span> {name}</h3><p>{why}</p></header>
  {sample(cls, crop_h, offset)}</article>''')
    return f'''<section class="axis" id="{axis_id}" aria-labelledby="{axis_id}-h"><h2 id="{axis_id}-h">{title}</h2><p class="axisintro">{intro}</p>{"".join(cards)}</section>'''


CSS = bd4.CSS + r"""
/* ---------- page ---------- */
.axis{max-width:1440px;margin:0 auto;padding:8px 24px 28px}
.axis>h2{font-size:24px;margin:28px 0 6px;font-weight:600}
.axisintro{color:var(--page-ink-2);margin:0 0 16px;max-width:96ch}
.opt{background:#1B1C19;border-radius:12px;padding:20px 22px 24px;margin:0 0 18px;color:#F3F4EF;font-family:"Schibsted Grotesk",system-ui,sans-serif}
.opt>header{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.6fr);gap:24px;align-items:baseline;margin-bottom:14px}
.opt>header>h3{margin:0;font-size:20px;font-weight:600}
.opt .oid{display:inline-block;font:600 12px/1 "Source Code Pro",monospace;letter-spacing:.06em;padding:4px 7px;border-radius:6px;background:#2E302A;color:#C6EF5A;margin-right:6px;vertical-align:3px}
.opt>header>p{margin:0;color:#C5C7BE;font-size:14.5px}
.decided{max-width:1440px;margin:0 auto;padding:0 24px 8px}
.decided .box{background:#1B1C19;border-radius:12px;padding:18px 22px;color:#C5C7BE;font-family:"Schibsted Grotesk",system-ui,sans-serif;font-size:14.5px}
.decided .box b{color:#F3F4EF}
.decided ul{margin:8px 0 0;padding-left:18px}
.decided li{margin:0 0 4px}
.full{max-width:1440px;margin:0 auto;padding:0 24px}

/* ---------- the working style: no rings round the rows ---------- */
.lime .set>li.has-problem,.lime .set>li.has-note{box-shadow:inset 0 0 0 1px var(--line),inset 0 1px 3px rgba(0,0,0,.45)}
.lime .set>li.sel{outline:0}
.lime .stage.s-problem,.lime .stage.s-note{box-shadow:inset 0 0 0 1px var(--line)}
.lime .callout.c-problem{box-shadow:none;background:color-mix(in srgb,var(--problem) 9%,var(--well))}
.lime .callout.c-note{box-shadow:none;background:color-mix(in srgb,var(--note) 8%,var(--well))}

/* ---------- navigation ---------- */
.n2 .app,.n3 .app{display:grid;align-items:stretch}
.n2 .app{grid-template-columns:224px minmax(0,1fr)}
.n2 .nav{display:flex;flex-direction:column;align-items:stretch;gap:20px;height:auto;padding:20px 12px;border-bottom:0;border-right:1px solid var(--line)}
.n2 .product{padding:0 10px}
.n2 .links{flex-direction:column;gap:2px}
.n2 .links a{position:relative;padding:9px 12px 9px 14px}
.n2 .links a.on{background:var(--raised);box-shadow:none}
.n2 .links a.on::before{content:"";position:absolute;left:3px;top:10px;bottom:10px;width:3px;border-radius:2px;background:var(--brand)}
.n2 .account{margin:auto 0 0;padding:0 10px}
.n3 .app{grid-template-columns:84px minmax(0,1fr)}
.n3 .nav{display:flex;flex-direction:column;align-items:center;gap:18px;height:auto;padding:16px 8px;border-bottom:0;border-right:1px solid var(--line)}
.n3 .product{font-size:0;gap:0}
.n3 .product .logo{width:22px;height:22px;border-radius:7px}
.n3 .links{flex-direction:column;gap:6px;width:100%}
.n3 .links a{flex-direction:column;gap:4px;padding:9px 2px;font-size:11px;text-align:center;border-radius:10px}
.n3 .links a .ic{width:20px;height:20px}
.n3 .links a.on{background:color-mix(in srgb,var(--brand) 14%,transparent);box-shadow:none;color:var(--text)}
.n3 .links a.on .ic{color:var(--brand)}
.n3 .account{margin-top:auto;font-size:0;gap:0}
.n3 .account img{width:30px;height:30px}

/* ---------- the current place in the top bar ---------- */
.t1 .links a.on,.t2 .links a.on,.t3 .links a.on,.t4 .links a.on{box-shadow:none}
.t1 .links a{position:relative;background:transparent!important}
.t1 .links a.on{color:var(--text)}
.t1 .links a.on::after{content:"";position:absolute;left:50%;bottom:-1px;width:18px;height:3px;margin-left:-9px;border-radius:2px;background:var(--brand)}
.t1 .links a.on .ic{color:var(--text)}
.t2 .links{background:transparent;padding:3px;box-shadow:none}
.t2 .links a{border-radius:8px}
.t2 .links a.on{background:var(--raised);box-shadow:0 1px 2px rgba(0,0,0,.45),inset 0 1px 0 rgba(255,255,255,.05)}
.t2 .links a.on .ic{color:var(--brand)}
.t3 .links a{border-radius:999px;padding-left:12px;padding-right:14px}
.t3 .links a.on{background:color-mix(in srgb,var(--brand) 16%,transparent);color:var(--text)}
.t3 .links a.on .ic{color:var(--brand)}
.t4 .links a{background:transparent!important;position:relative}
.t4 .links a.on{color:var(--text);font-weight:650}
.t4 .links a.on::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--brand);margin-right:-2px}

/* ---------- the active item ---------- */
.s1 .set>li.sel{background:color-mix(in srgb,var(--brand) 9%,var(--well));box-shadow:inset 0 0 0 1px color-mix(in srgb,var(--brand) 22%,transparent)}
.s2 .set>li.sel{position:relative;background:var(--raised)}
.s2 .set>li.sel::before{content:"";position:absolute;left:5px;top:14px;bottom:14px;width:3px;border-radius:2px;background:var(--brand)}
.s3 .set>li.sel{background:#353731;box-shadow:0 6px 18px rgba(0,0,0,.45),0 1px 0 rgba(255,255,255,.06) inset;transform:translateY(-1px)}

/* ---------- a finding ---------- */
.f1 .marks,.f2 .marks{align-items:flex-start}
.f1 .mark{padding:3px 9px 3px 7px;border-radius:999px;font-weight:600}
.f1 .m-problem{background:color-mix(in srgb,var(--problem) 15%,transparent)}
.f1 .m-note{background:color-mix(in srgb,var(--note) 14%,transparent)}
.f1 .st-conflict{padding:1px 8px;border-radius:999px;background:color-mix(in srgb,var(--problem) 12%,transparent)}
.f3 .row{grid-template-columns:20px minmax(0,1fr) auto}
.f3 .marks{display:contents}
.f3 .mark{grid-column:1;grid-row:1;align-self:start;margin-top:2px;gap:0}
.f3 .mark>span{display:none}
.f3 .rmain{grid-column:2}
.f3 .it.has-problem>.row::after,.f3 .it.has-note>.row::after{grid-column:3;grid-row:1;font-size:var(--fs-s);color:var(--text2);font-weight:500}
.f3 .it.has-problem>.row::after{content:"Problem"}
.f3 .it.has-note>.row::after{content:"Note"}
"""

JS = r"""
(function(){
  function fit(){document.querySelectorAll('.scale').forEach(function(s){
    var n=s.firstElementChild,k=Math.min(1,s.clientWidth/1280),h=+s.dataset.h||0,o=+s.dataset.o||0;
    n.style.transform='scale('+k+') translateY('+(-o)+'px)';
    s.style.height=((h||n.offsetHeight)*k)+'px';});}
  window.addEventListener('resize',fit);
  if(document.fonts&&document.fonts.ready){document.fonts.ready.then(fit);}
  window.addEventListener('load',fit);fit();
})();
"""


def build():
    t = LIME["tokens"]
    vars_ = ";".join(f"--{k}:{v}" for k, v in t.items())
    vars_ += (';--font:"Schibsted Grotesk",system-ui,sans-serif;--font-display:"Schibsted Grotesk",system-ui,sans-serif;'
              '--font-mono:"Source Code Pro",ui-monospace,monospace')
    wrap = lambda inner: f'<div class="dir d-mica v-lime limewrap" style=\'{vars_};padding:0;background:transparent\'>{inner}</div>'
    base_nav = "lime {axis} s1 f1"
    base_sel = "lime n1 {axis} f1"
    base_find = "lime n1 s1 {axis}"
    top = option_block("top", "The current place in the top bar", "The top bar stays (N1). Only the look of the current place changes — here <i>Projects</i>. Shown with S2 and F1, which are fixed.", TOP, "lime n1 {axis} s2 f1", 150, 0)
    nav = option_block("nav", "Navigation", "Three ways to reach the three places — <i>My library</i>, <i>Public library</i>, <i>Projects</i>. Shown with selection S1 and findings F1.", NAV, base_nav, 300, 0)
    sel = option_block("sel", "The active item", "How the row you opened is marked — here <code>eslint-autofix</code>, open in the panel. No outline round it. Shown with N1 and F1.", SEL, base_sel, 420, 250)
    fnd = option_block("find", "A finding", "How a Problem and a Note show on a row now that the coloured rings are gone. Shown with N1 and S1.", FIND, base_find, 420, 250)
    full = f'<section class="full" aria-label="The whole screen"><div class="opt"><header><h3><span class="oid">N1 · T2 · S2 · F1</span> The whole screen, as fixed</h3><p>Top bar, the active row marked by a lime pill at its edge, findings as tinted tags. The current place in the bar is a raised tile with a lime icon, on no track (T2 without its track).</p></header>{sample("lime n1 t2 s2 f1", 0)}</div></section>'
    run = f'<section class="full" aria-label="Export"><div class="opt"><header><h3><span class="oid">Export</span> The same rules in the Export mode</h3><p>No rings on the stages either: a stage’s verdict is its icon and words; the finding’s box is a faint tint of its colour.</p></header>{sample("lime n1 t2 s2 f1", 560, 0, overlay=True)}</div></section>'
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mica Lime · AI Stack Builder</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{bd4.FONTS}"><style>{CSS}</style></head>
<body data-density="between">{bd4.symbols()}
<header class="pagehead">
  <h1>Mica · Lime — finishing the working style</h1>
  <p>Fixed as the working style on 11 Oct 2026. Fixed by the owner the same evening: <b>the top bar (N1)</b>, <b>the active row as a lime pill at its edge (S2)</b> and <b>findings as tinted tags (F1)</b>. And the current place in the bar: <b>a raised tile with a lime icon, with no track behind the others</b>. Nothing on this page is open any more; it is the input to stage 4. Every word is from <code>microcopy.md</code>.</p>
  <div class="bar"><nav aria-label="Sections"><span class="k">Jump to</span><span class="k">The fixed screen, then Export</span></nav></div>
</header>
<section class="decided"><div class="box"><b>Already decided.</b><ul>
<li><b>Material:</b> Mica — a neutral ground with a faint lime tint, quiet layers; acrylic only around the Export mode and a dialog, text always on an opaque sheet.</li>
<li><b>Type:</b> Schibsted Grotesk; Source Code Pro for paths, refs and file contents. <b>Icons:</b> Lucide, 1.75 px stroke.</li>
<li><b>Brand:</b> lime <code>#C6EF5A</code>, only on what you can press and where you are. <b>Density:</b> between Default and Comfortable.</li>
<li><b>Rows:</b> each item in its own rounded cut-out, auto-added items inside their parent’s behind a dashed rule. <b>No rings</b> round a row for a finding or a selection.</li>
<li><b>Checked</b> is a quiet dot, never green (D1-B).</li>
<li><b>Navigation:</b> the top bar (N1). <b>Active row:</b> a short lime pill at its left edge, the cut-out one step lighter (S2). <b>Findings:</b> a tinted tag with the icon and the word (F1). <b>Current place in the bar:</b> a raised tile, its icon in lime; the other places sit on nothing (T2, no track).</li></ul></div></section>
{wrap(full + run)}
<p class="pagefoot">Built by <code>tools/build_lime.py</code>. Icons: Lucide (ISC). Portrait: Jake Nackos on Unsplash (unsplash.com/photos/IF9TK5Uy-KI).</p>
<script>{JS}</script></body></html>'''
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}  {len(html)//1024} KB")
    for k in ("text3", "problem", "note"):
        for bg in ("well", "raised"):
            print(k, "on", bg, round(ratio(t[k], t[bg]), 2))


if __name__ == "__main__":
    build()
