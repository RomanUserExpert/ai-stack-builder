"""Phase 06: build 06-concept/mica-lime.html — the working style, Mica · Lime, polished.

Fixed by the owner on 2026-10-11 (06-concept/concept.md, *Working style*). Rounds 3 and 4 drew it out of
three generators' stylesheets layered on top of each other; this file replaces that cascade with ONE
stylesheet written in tokens — a 4 px spacing scale, a type scale, a radius scale, the colours, and
every state a control has — so that one component has one set of values everywhere it appears.

    python tools/build_lime.py   -> 06-concept/mica-lime.html

Markup (every word from microcopy.md) comes from tools/build_directions_2.py; Lucide icons and the
lime tokens from tools/build_directions_4.py. Stage 4 lifts the .ml token block below into tokens.css.
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
ic = bd4.ic

# ------------------------------------------------------------------ the tokens
COLOR = [
    # name, hex, role, the surface its contrast is measured on (None for a surface)
    ("ground", "#1B1C19", "Mica ground, a faint lime tint", None),
    ("bar", "#181916", "the top bar", None),
    ("tray", "#232420", "the tray under the rows", None),
    ("cutout", "#1E1F1B", "a row’s cut-out", None),
    ("well-deep", "#161714", "a code block — darker than anything around it", None),
    ("raised", "#2A2B27", "item panel, the active row, a sheet", None),
    ("control", "#2E302A", "a secondary button, a tag", None),
    ("control-hover", "#383A33", "a secondary button, hovered", None),
    ("line", "#343630", "hairline", None),
    ("line-strong", "#4A4C44", "a control’s edge, a dashed rule", None),
    ("text", "#F3F4EF", "text", "tray"),
    ("text-2", "#C5C7BE", "secondary text", "tray"),
    ("text-3", "#A1A49A", "metadata, Skipped", "raised"),
    ("lime", "#C6EF5A", "brand: what you can press, where you are", "bar"),
    ("lime-hover", "#D3F57A", "the primary button, hovered", None),
    ("on-lime", "#141A08", "text on lime", "lime"),
    ("problem", "#FF8F98", "Problem", "raised"),
    ("note", "#F2C661", "Note", "raised"),
]
SPACE = [("1", 4), ("2", 8), ("3", 12), ("4", 16), ("5", 20), ("6", 24), ("8", 32), ("10", 40)]
TYPE = [  # name, size, line-height, weight, sample
    ("display", 28, 34, 600, "acme-billing-api"),
    ("title", 20, 26, 600, "Checked just now"),
    ("heading", 16, 22, 600, "Remove eslint-autofix from acme-billing-api?"),
    ("body", 14.5, 21, 400, "Reads a migration before it runs and flags long locks."),
    ("small", 13, 19, 400, "14 items · 3 auto-added · 1 detached"),
    ("micro", 12, 16, 500, "scripts/eslint-autofix.sh · Auto-added"),
]
RADIUS = [("xs", 4), ("sm", 6), ("md", 10), ("lg", 14), ("xl", 18), ("pill", 999)]
C = {n: h for n, h, _, _ in COLOR}


def token_css():
    v = [f"--{n}:{h};" for n, h, _, _ in COLOR]
    v += [f"--s{n}:{px}px;" for n, px in SPACE]
    v += [f"--t-{n}:{w} {size}px/{lh}px var(--font);" for n, size, lh, w, _ in TYPE]
    v += [f"--r-{n}:{px}px;" for n, px in RADIUS]
    v += ['--font:"Schibsted Grotesk",system-ui,sans-serif;', '--mono:"Source Code Pro",ui-monospace,monospace;',
          "--problem-wash:color-mix(in srgb,var(--problem) 14%,transparent);",
          "--note-wash:color-mix(in srgb,var(--note) 13%,transparent);",
          "--focus:0 0 0 2px var(--ground),0 0 0 4px var(--lime);",
          "--ease:cubic-bezier(.2,.7,.2,1);--dur:140ms;"]
    return ".ml{" + "".join(v) + "}"


CSS = r"""
:root{--page:#262626;--page-2:#2f2f2f;--page-ink:#e8e8e8;--page-ink-2:#b4b4b4;--page-line:#3d3d3d}
*{box-sizing:border-box}
html{background:var(--page)}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
body{margin:0;background:var(--page);color:var(--page-ink);font:15px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}
.pagehead,.sec,.pagefoot{max-width:1440px;margin:0 auto;padding-left:24px;padding-right:24px}
.pagehead{padding-top:40px}
.pagehead h1{font-size:30px;line-height:1.2;margin:0 0 10px;font-weight:600}
.pagehead p{margin:0 0 10px;color:var(--page-ink-2);max-width:96ch}
.pagehead p b{color:var(--page-ink)}
.bar{position:sticky;top:0;z-index:5;display:flex;gap:6px;align-items:center;margin:18px -24px 0;padding:10px 24px;background:var(--page);border-bottom:1px solid var(--page-line)}
.bar .k{font-size:13px;color:var(--page-ink-2);margin-right:4px}
.bar a{font-size:14px;font-weight:600;color:var(--page-ink);text-decoration:none;padding:6px 12px;border-radius:6px;border:1px solid var(--page-line);background:var(--page-2)}
.bar a:focus-visible{outline:2px solid var(--page-ink);outline-offset:2px}
.sec{padding-top:28px;padding-bottom:4px}
.sec>h2{font-size:22px;font-weight:600;margin:0 0 6px;scroll-margin-top:70px}
.sec>p{color:var(--page-ink-2);margin:0 0 16px;max-width:96ch}
.pagefoot{padding-top:24px;padding-bottom:48px;color:var(--page-ink-2);font-size:13.5px}

/* ================= Mica · Lime ================= */
.ml{font:var(--t-body);color:var(--text);-webkit-font-smoothing:antialiased}
.ml code,.ml pre{font-family:var(--mono)}
.ml ::selection{background:color-mix(in srgb,var(--lime) 35%,transparent);color:var(--text)}
.ml .card{background:var(--ground);border-radius:12px;padding:var(--s8);overflow:hidden}
.scale{width:100%;overflow:hidden;border-radius:var(--r-md);box-shadow:0 0 0 1px var(--line);background:var(--ground)}
.native{width:1280px;transform-origin:0 0}
.ic{width:16px;height:16px;flex:none}
.dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:currentColor;flex:none;margin:0 6px 0 2px}

/* --- controls --- */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:var(--s2);height:32px;padding:0 var(--s3);
  font:500 13.5px/1 var(--font);color:var(--text);white-space:nowrap;cursor:default;
  background:var(--control);border:1px solid var(--line-strong);border-radius:var(--r-sm);
  transition:background var(--dur) var(--ease),border-color var(--dur) var(--ease)}
.btn .ic{width:16px;height:16px;color:var(--text-2)}
.btn:hover,.btn.is-hover{background:var(--control-hover)}
.btn:focus-visible,.btn.is-focus{outline:0;box-shadow:var(--focus)}
.btn:active,.btn.is-active{background:var(--control);transform:translateY(.5px)}
.btn.primary{background:var(--lime);border-color:var(--lime);color:var(--on-lime);font-weight:600}
.btn.primary .ic{color:var(--on-lime)}
.btn.primary:hover,.btn.primary.is-hover{background:var(--lime-hover);border-color:var(--lime-hover)}
.btn.primary.is-disabled{background:var(--control);border-color:var(--line);color:var(--text-3)}
.btn.primary.is-disabled .ic{color:var(--text-3)}
.btn.icon-only{width:32px;padding:0}
.kind,.state{display:inline-flex;align-items:center;gap:var(--s1);height:20px;padding:0 var(--s2);
  font:var(--t-micro);color:var(--text-2);background:transparent;box-shadow:inset 0 0 0 1px var(--line-strong);border-radius:var(--r-pill);white-space:nowrap}
.state{background:transparent;box-shadow:none;padding:0 2px}
.state .ic{width:13px;height:13px;color:var(--text-3)}
.st-conflict{color:var(--problem);background:var(--problem-wash);box-shadow:inset 0 0 0 1px color-mix(in srgb,var(--problem) 40%,transparent);padding:0 var(--s2)}
.mark{display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 var(--s3) 0 var(--s2);
  font:600 12.5px/1 var(--font);border-radius:var(--r-pill);white-space:nowrap}
.mark .ic{width:14px;height:14px}
.m-problem{color:var(--problem);background:var(--problem-wash)}
.m-note{color:var(--note);background:var(--note-wash)}
.m-skipped{color:var(--text-3);font-weight:500;padding:0 var(--s1)}
.m-checked{color:var(--text-2);font-weight:500;padding:0 var(--s1)}

/* --- the app --- */
.app{background:var(--ground);min-height:780px}
.nav{display:flex;align-items:center;gap:var(--s6);height:52px;padding:0 var(--s6);background:var(--bar);border-bottom:1px solid var(--line)}
.product{display:flex;align-items:center;gap:var(--s2);font:600 14.5px/1 var(--font);letter-spacing:-.005em}
.logo{width:14px;height:14px;border-radius:var(--r-xs);background:var(--lime)}
.links{display:flex;gap:2px}
.links a{display:flex;align-items:center;gap:var(--s2);height:32px;padding:0 var(--s3);color:var(--text-2);font:500 14px/1 var(--font);border-radius:var(--r-sm);transition:background var(--dur) var(--ease),color var(--dur) var(--ease)}
.links a .ic{color:var(--text-3)}
.links a:hover,.links a.is-hover{color:var(--text);background:color-mix(in srgb,var(--raised) 60%,transparent)}
.links a.on{color:var(--text);background:var(--raised);box-shadow:0 1px 2px rgba(0,0,0,.35),inset 0 1px 0 rgba(255,255,255,.04)}
.links a.on .ic{color:var(--lime)}
.account{margin-left:auto;display:flex;align-items:center;gap:var(--s2);font:var(--t-small);color:var(--text-2)}
.account img{width:24px;height:24px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 1px var(--line)}
.main{padding:var(--s8) var(--s8) var(--s10)}

.phead{display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:var(--s6);row-gap:var(--s3)}
.crumb{margin:0 0 var(--s1);font:var(--t-small);color:var(--text-3)}
.phead h1{margin:0;font:var(--t-display);letter-spacing:-.018em}
.pfactsline{margin:var(--s1) 0 0;font:var(--t-small);color:var(--text-2)}
.actions{display:flex;gap:var(--s2);align-self:start;margin-top:calc(19px + var(--s1) + 1px)}
.verdict{grid-column:1/-1;display:flex;align-items:center;gap:var(--s4);flex-wrap:wrap}
.vline{margin:0;display:flex;align-items:center;font:var(--t-small);color:var(--text-2)}
.vline .vglyph{color:var(--text-3)}
.vcounts{margin:0;display:flex;gap:var(--s4);font:600 13px/19px var(--font)}
.vcounts span{display:inline-flex;align-items:center;gap:6px}
.vcounts .ic{width:14px;height:14px}
.c-problem{color:var(--problem)} .c-note{color:var(--note)} .c-skipped{color:var(--text-3);font-weight:500}
.pdesc{margin:var(--s4) 0 var(--s6);max-width:72ch;font:var(--t-body);color:var(--text-2)}

.work.with{display:grid;grid-template-columns:minmax(0,1fr) 384px;gap:var(--s5);align-items:start}
.set,.sub{list-style:none;margin:0;padding:0}
.set{display:flex;flex-direction:column;gap:var(--s2);padding:var(--s2);background:var(--tray);border-radius:var(--r-lg)}
.set>li{position:relative;background:var(--cutout);border-radius:var(--r-md);box-shadow:inset 0 0 0 1px var(--line),inset 0 1px 2px rgba(0,0,0,.35);transition:background var(--dur) var(--ease)}
.set>li:hover,.set>li.is-hover{background:color-mix(in srgb,var(--raised) 55%,var(--cutout))}
.set>li.sel{background:var(--raised);box-shadow:inset 0 0 0 1px var(--line-strong)}
.set>li.sel::before{content:"";position:absolute;left:5px;top:var(--s3);height:24px;width:3px;border-radius:2px;background:var(--lime)}
.row{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:var(--s4);padding:var(--s3) var(--s4)}
.row h3{display:flex;align-items:center;flex-wrap:wrap;gap:var(--s2);min-height:24px;margin:0;font:600 14.5px/21px var(--font);letter-spacing:-.003em}
.desc{margin:2px 0 0;font:var(--t-small);color:var(--text-2)}
.facts{margin:var(--s1) 0 0;font:400 12px/16px var(--font);color:var(--text-3)}
.facts code{font-size:11.5px;color:var(--text-3)}
.facts em{font-style:normal;color:var(--text-2)}
.marks{margin:0;display:flex;gap:var(--s2);align-items:flex-start}
.sub{margin:0 var(--s2) 0 var(--s6);border-top:1px dashed var(--line-strong)}
.sub>li+li{border-top:1px dashed var(--line-strong)}
.sub .row{padding-left:var(--s2)}
.sub .sub{margin-left:var(--s6);margin-right:0}

.panel{background:var(--raised);border:1px solid var(--line);border-radius:var(--r-lg);padding:var(--s5)}
.phd{display:flex;justify-content:space-between;align-items:flex-start;gap:var(--s3)}
.panel h2{margin:0;font:var(--t-heading);letter-spacing:-.008em}
.chips{display:flex;gap:var(--s2);margin:var(--s2) 0 0}
.panel>.desc{margin:var(--s3) 0 0;font:var(--t-small);color:var(--text-2)}
.callout{display:flex;flex-direction:column;gap:6px;margin:var(--s4) 0 0;padding:var(--s3) var(--s4);border-radius:var(--r-md);font:var(--t-small);color:var(--text)}
.callout .sev{display:flex;align-items:center;gap:6px;font-weight:600}
.callout .sev .ic{width:15px;height:15px}
.callout code{font-size:12px}
.c-problem.callout{background:color-mix(in srgb,var(--problem) 10%,var(--cutout));box-shadow:inset 0 0 0 1px color-mix(in srgb,var(--problem) 34%,transparent);color:var(--text)}
.c-note.callout{background:color-mix(in srgb,var(--note) 9%,var(--cutout));box-shadow:inset 0 0 0 1px color-mix(in srgb,var(--note) 30%,transparent);color:var(--text)}
.c-problem.callout .sev{color:var(--problem)} .c-note.callout .sev{color:var(--note)}
.callout .btn{align-self:flex-start;margin-top:var(--s1)}
.psec{margin-top:var(--s5);padding-top:var(--s4);border-top:1px solid var(--line)}
.psec h3{margin:0 0 var(--s2);font:600 11.5px/16px var(--font);letter-spacing:.06em;text-transform:uppercase;color:var(--text-3)}
.psec p{margin:0;font:var(--t-small);color:var(--text-2)}
.file{margin:0 0 var(--s2);padding:var(--s3) var(--s4);background:var(--well-deep);border:1px solid var(--line-strong);border-radius:var(--r-md);
  font:400 12px/1.65 var(--mono);color:var(--text);white-space:pre-wrap;overflow-wrap:anywhere}
.meta{margin:0;font:400 12px/16px var(--font);color:var(--text-3)!important}
.pfacts{display:grid;grid-template-columns:116px 1fr;gap:6px var(--s3);margin:0;font:var(--t-small)}
.pfacts dt{color:var(--text-3)} .pfacts dd{margin:0;color:var(--text)}
.pfacts code{font-size:12px}
.pact{display:flex;gap:var(--s2);margin-top:var(--s5);padding-top:var(--s4);border-top:1px solid var(--line)}

/* --- Export over the project --- */
.runwrap{position:relative;height:780px;overflow:hidden}
.runwrap .app{min-height:780px}
.veil,.dveil{position:absolute;inset:0;background:rgba(10,11,9,.42)}
.run{position:absolute;left:112px;right:112px;top:var(--s8);bottom:0;padding:var(--s2) var(--s2) 0;border-radius:var(--r-xl) var(--r-xl) 0 0;
  background:color-mix(in srgb,var(--lime) 7%,rgba(62,64,58,.42));backdrop-filter:blur(28px) saturate(140%);-webkit-backdrop-filter:blur(28px) saturate(140%);
  border:1px solid rgba(255,255,255,.12);border-bottom:0}
.runin{height:100%;overflow:hidden;padding:var(--s6) var(--s8);background:var(--ground);border:1px solid rgba(255,255,255,.05);border-bottom:0;border-radius:var(--r-lg) var(--r-lg) 0 0}
.rhead{display:flex;justify-content:space-between;align-items:flex-start}
.rhead h2{margin:0;font:var(--t-title);letter-spacing:-.012em}
.rcounts{margin:var(--s2) 0 0;font:600 13px/19px var(--font)}
.rhead .meta{margin-top:var(--s1)}
.group{margin:var(--s6) 0 var(--s2);font:600 11.5px/16px var(--font);letter-spacing:.06em;text-transform:uppercase;color:var(--text-3)}
.stages{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:var(--s2)}
.stage{background:var(--cutout);border-radius:var(--r-md);box-shadow:inset 0 0 0 1px var(--line)}
.stage.s-skipped{background:transparent;box-shadow:none;outline:1px dashed var(--line-strong);outline-offset:-1px}
.sum{display:grid;grid-template-columns:24px 184px minmax(0,1fr) 56px;gap:var(--s3);align-items:center;min-height:44px;padding:var(--s2) var(--s4)}
.n{font:400 12px/16px var(--mono);color:var(--text-3);font-variant-numeric:tabular-nums}
.sname{font:600 14.5px/21px var(--font)}
.res{display:flex;align-items:center;gap:var(--s2);font:var(--t-small);color:var(--text-2)}
.res .ic{width:15px;height:15px}
.g-problem{color:var(--problem)} .g-note{color:var(--note)} .g-skipped{color:var(--text-3)} .g-checked{color:var(--text-2)}
.s-problem .res span{color:var(--problem);font-weight:600}
.s-note .res span{color:var(--note);font-weight:600}
.time{text-align:right;font:400 12px/16px var(--mono);color:var(--text-3);font-variant-numeric:tabular-nums}
.sbody{padding:0 var(--s4) var(--s4) calc(var(--s4) + 24px + var(--s3))}
.sbody .callout{margin-top:0}
.slots{display:flex;gap:var(--s2);flex-wrap:wrap;margin-top:var(--s1)}
.slot{display:inline-flex;align-items:center;gap:6px;height:26px;padding:0 var(--s3) 0 var(--s2);font:400 12px/1 var(--font);border:1px dashed var(--line-strong);border-radius:var(--r-sm)}
.slot code{font-size:11.5px;font-weight:500;color:var(--text)}
.slot small{color:var(--text-3);font-size:11.5px}
.slot .ic{width:13px;height:13px;color:var(--text-3)}
.dveil{background:rgba(10,11,9,.30)}
.dlg{position:absolute;left:50%;top:248px;transform:translateX(-50%);width:468px;padding:var(--s2);border-radius:var(--r-xl);
  background:color-mix(in srgb,var(--lime) 7%,rgba(70,72,66,.45));backdrop-filter:blur(24px) saturate(140%);-webkit-backdrop-filter:blur(24px) saturate(140%);
  border:1px solid rgba(255,255,255,.14);box-shadow:0 18px 40px rgba(0,0,0,.35)}
.sheet{padding:var(--s5) var(--s6);background:var(--raised);border:1px solid rgba(255,255,255,.05);border-radius:var(--r-lg)}
.sheet h2{margin:0 0 var(--s2);font:var(--t-heading);letter-spacing:-.008em}
.sheet p{margin:0;font:var(--t-small);color:var(--text-2)}
.sheet p+p{margin-top:var(--s2)}
.dact{display:flex;justify-content:flex-end;gap:var(--s2);margin-top:var(--s5)}

/* --- the system, shown --- */
.sys{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:var(--s10)}
.sys>div>h3{margin:0 0 var(--s3);font:600 11.5px/16px var(--font);letter-spacing:.06em;text-transform:uppercase;color:var(--text-3)}
.sys>div>h3:not(:first-child){margin-top:var(--s8)}
.swatches{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:var(--s3) var(--s4)}
.swatches li{display:grid;grid-template-columns:40px 1fr;column-gap:var(--s3);font:400 12px/16px var(--font);color:var(--text-2)}
.swatches .chip{grid-row:1/4;width:40px;height:48px;border-radius:var(--r-sm);box-shadow:inset 0 0 0 1px rgba(255,255,255,.12)}
.swatches b{font:500 12px/16px var(--mono);color:var(--text)}
.swatches .cr{color:var(--text-3);font-variant-numeric:tabular-nums}
.types{list-style:none;margin:0;padding:0}
.types li{display:grid;grid-template-columns:112px minmax(0,1fr);gap:var(--s3);align-items:baseline;padding:var(--s3) 0;border-top:1px solid var(--line)}
.types li>span:first-child{font:400 12px/16px var(--mono);color:var(--text-3)}
.row-of{display:flex;align-items:flex-end;gap:var(--s4);flex-wrap:wrap}
.row-of>div{display:flex;flex-direction:column;align-items:center;gap:6px;font:400 12px/16px var(--font);color:var(--text-3)}
.row-of i{display:block;background:color-mix(in srgb,var(--lime) 55%,transparent);border-radius:2px}
.radii i{width:44px;height:44px;background:var(--control);box-shadow:inset 0 0 0 1px var(--line-strong)}
.row-of .ic{width:20px;height:20px;color:var(--text)}
.tagsrow{display:flex;align-items:center;gap:var(--s3);flex-wrap:wrap}
.states{display:grid;grid-template-columns:96px repeat(4,max-content);gap:var(--s3) var(--s4);align-items:center}
.states>span{font:400 12px/16px var(--font);color:var(--text-3)}
.states .links{display:contents}
.states-rows{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s3);margin-top:var(--s5)}
.states-rows figure{margin:0}
.states-rows figcaption{margin-top:6px;font:400 12px/16px var(--font);color:var(--text-3)}
@media (max-width:1100px){.sys{grid-template-columns:minmax(0,1fr)}.ml .card{padding:var(--s5)}.states-rows{grid-template-columns:minmax(0,1fr)}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

JS = r"""
(function(){
  function fit(){document.querySelectorAll('.scale').forEach(function(s){
    var n=s.firstElementChild,w=s.clientWidth,k=Math.min(1,w/1280);
    n.style.width=(w>1280?w:1280)+'px';n.style.transform='scale('+k+')';s.style.height=(n.offsetHeight*k)+'px';});}
  window.addEventListener('resize',fit);
  if(document.fonts&&document.fonts.ready){document.fonts.ready.then(fit);}
  window.addEventListener('load',fit);fit();
})();
"""


def system_block():
    sw = []
    for n, h, role, against in COLOR:
        cr = f'<span class="cr">{ratio(h, C[against]):.1f}:1 on {against}</span>' if against else '<span class="cr">a surface</span>'
        sw.append(f'<li><span class="chip" style="background:{h}"></span><b>--{n} {h}</b><span>{role}</span>{cr}</li>')
    types = "".join(f'<li><span>{n} {s:g}/{lh} · {w}</span><span style="font:{w} {s}px/{lh}px var(--font);color:var(--text)">{sample}</span></li>'
                    for n, s, lh, w, sample in TYPE)
    space = "".join(f'<div><i style="width:{px}px;height:{px}px"></i>{px}</div>' for _, px in SPACE)
    radii = "".join(f'<div><i style="border-radius:{min(px, 22)}px"></i>{n if px >= 999 else f"{n} · {px}"}</div>' for n, px in RADIUS)
    b = lambda cls, label, icon: f'<span class="btn {cls}">{ic(LIME, icon)}{label}</span>'
    states = ('<div class="states">'
              '<span>Primary</span>' + b("primary", "Export…", "arrow_export_ltr") + b("primary is-hover", "Export…", "arrow_export_ltr")
              + b("primary is-focus", "Export…", "arrow_export_ltr") + b("primary is-disabled", "Export…", "arrow_export_ltr")
              + '<span>Secondary</span>' + b("", "Configure", "options") + b("is-hover", "Configure", "options")
              + b("is-focus", "Configure", "options") + b("is-active", "Configure", "options")
              + '<span></span><span>default</span><span>hover</span><span>focus</span><span>inert · pressed</span>'
              + '<span>Place</span><span class="links"><a>' + ic(LIME, "library") + 'My library</a><a class="is-hover">'
              + ic(LIME, "globe") + 'Public library</a><a class="on">' + ic(LIME, "folder") + 'Projects</a></span><span></span>'
              + '<span></span><span>default</span><span>hover</span><span>current</span><span></span></div>')
    one = lambda cls, cap: (f'<figure><ol class="set"><li class="it {cls}"><article class="row"><div class="rmain"><h3><span class="nm">github-mcp</span>'
                            f'<span class="kind">mcp</span></h3><p class="desc">Issues, pull requests and code search on GitHub.</p></div>'
                            f'<p class="marks"></p></article></li></ol><figcaption>{cap}</figcaption></figure>')
    rows = '<div class="states-rows">' + one("", "row · default") + one("is-hover", "row · hover") + one("sel", "row · active, the lime pill") + '</div>'
    tags = ('<div class="tagsrow"><span class="kind">script</span><span class="state st-conflict">Conflict</span>'
            f'<span class="state">{ic(LIME, "arrow_turn_down_right")}Auto-added</span><span class="state">{ic(LIME, "link_dismiss")}Detached</span>'
            + bd2.mark(LIME, "problem") + bd2.mark(LIME, "note") + bd2.mark(LIME, "skipped") + bd2.mark(LIME, "checked") + '</div>')
    icons = "".join(f'<div>{ic(LIME, n)}{k}</div>' for k, n in bd2.KINDS)
    return f'''<div class="card"><div class="sys">
  <div><h3>Colour — ratios computed at build</h3><ul class="swatches">{"".join(sw)}</ul>
    <h3>Tags and findings</h3>{tags}
    <h3>States, drawn</h3>{states}{rows}</div>
  <div><h3>Type — Schibsted Grotesk · Source Code Pro</h3><ul class="types">{types}</ul>
    <h3>Spacing — a 4 px scale</h3><div class="row-of">{space}</div>
    <h3>Radius</h3><div class="row-of radii">{radii}</div>
    <h3>Icons — Lucide, 1.75 px stroke, 16 px in controls</h3><div class="row-of">{icons}</div></div>
</div></div>'''


def build():
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mica Lime · AI Stack Builder</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700&family=Source+Code+Pro:wght@400;500&display=swap">
<style>{token_css()}{CSS}</style></head>
<body>{bd4.symbols()}
<header class="pagehead">
  <h1>Mica · Lime — the working style</h1>
  <p>Fixed by the owner on 11 Oct 2026 (<code>concept.md</code>, <i>Working style</i>): a top bar with the current place as a raised tile, the active row marked by a lime pill, findings as tinted tags, no rings anywhere. <b>This is the polish pass</b>: one stylesheet in tokens — a 4 px spacing scale, six type sizes, six radii, the colours with their contrast — and the states of every control. Every word on the screens is from <code>microcopy.md</code>.</p>
  <div class="bar"><span class="k">Jump to</span><a href="#screen">The screen</a><a href="#export">Export</a><a href="#dialog">Dialog</a><a href="#system">The system</a></div>
</header>
<div class="ml">
<section class="sec" id="screen" aria-labelledby="screen-h"><h2 id="screen-h">The project, with eslint-autofix open</h2><p>1:1 on a 1280 px canvas.</p>
  <div class="scale"><div class="native">{bd2.app(LIME)}</div></div></section>
<section class="sec" id="export" aria-labelledby="export-h"><h2 id="export-h">Export, over the project</h2><p>Acrylic only around the mode; the findings sit on an opaque sheet. No ring on a stage: its verdict is its icon and its words.</p>
  <div class="scale"><div class="native">{bd2.run(LIME, False)}</div></div></section>
<section class="sec" id="dialog" aria-labelledby="dialog-h"><h2 id="dialog-h">The remove dialog, over Export</h2><p>The same acrylic frame, smaller; the question on an opaque sheet.</p>
  <div class="scale"><div class="native">{bd2.run(LIME, True)}</div></div></section>
<section class="sec" id="system" aria-labelledby="system-h"><h2 id="system-h">The system under it</h2><p>What stage 4 lifts into <code>tokens.css</code>. The states are drawn, so they can be judged without hovering.</p>
  {system_block()}</section>
</div>
<p class="pagefoot">Built by <code>tools/build_lime.py</code>. Icons: Lucide (ISC). Portrait: Jake Nackos on Unsplash (unsplash.com/photos/IF9TK5Uy-KI).</p>
<script>{JS}</script></body></html>'''
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}  {len(page)//1024} KB")
    pairs = [("text", "tray"), ("text-2", "tray"), ("text-2", "raised"), ("text-2", "control"), ("text-3", "tray"), ("text-3", "raised"),
             ("text-3", "cutout"), ("text-3", "control"), ("problem", "raised"), ("problem", "cutout"), ("note", "cutout"),
             ("on-lime", "lime"), ("on-lime", "lime-hover"), ("lime", "bar"), ("lime", "raised")]
    for a, b in pairs:
        r = ratio(C[a], C[b])
        print(f"{a:8} on {b:12} {r:5.2f}{'  < 4.5' if r < 4.5 else ''}")


if __name__ == "__main__":
    build()
