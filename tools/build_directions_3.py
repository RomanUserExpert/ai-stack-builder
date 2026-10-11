"""Phase 06, stage 3, round 3: build 06-concept/directions-3.html — calmer, three densities.

The owner turned down round 2 and answered three questions (2026-10-11): calmer but better made;
Acrylic and Kit were closest; the type and the spacing felt too large — show several densities, so
style and density can be combined later. So this round is three directions times three densities,
switched on the page, and the samples are drawn at 1:1, never scaled up.

    python tools/build_directions_3.py   -> 06-concept/directions-3.html

Markup comes from tools/build_directions_2.py (the same content, every word from microcopy.md);
the CSS here is new and is written in density variables.
"""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("bd2", ROOT / "tools" / "build_directions_2.py")
bd2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bd2)
bd1, ratio = bd2.bd1, bd2.ratio
OUT = ROOT / "06-concept" / "directions-3.html"

DIRS = [
    {
        "id": "mica", "name": "Mica",
        "thesis": "Acrylic, calmed down. Windows 11’s own dark materials: a neutral Mica ground, "
                  "quiet layers, Segoe at its real UI sizes. Glass appears only around what you "
                  "enter — the Export mode and a dialog — as a thin acrylic frame.",
        "from": "Round 1’s Acrylic, which you marked as close. The berry accent and the blue tint are gone; the frame-only glass stays.",
        "competitors": "Windows 11 Settings, Microsoft Teams, Figma’s desktop app",
        "variants": [("Glass", "frame only, text always on an opaque sheet (D2, D3)"),
                     ("Checked", "B — a quiet steel dot (D1)"), ("Icons", "Fluent regular")],
        "risk": "Close to the platform: on Windows it will feel native, on a Mac a little foreign. Its signature is the material, so it lives or dies on how well the acrylic is made.",
        "style": "regular", "checked_icon": "circle_small",
        "fonts": {"display": "Segoe UI Variable Display", "body": "Segoe UI Variable Text", "mono": "Cascadia Code"},
        "font_note": "Segoe is read from the system, as Fluent does; on a Mac it falls back to SF. Cascadia Code for paths, refs and file contents.",
        "tokens": {"bg": "#1C1C1C", "surface": "#242424", "raised": "#2B2B2B", "well": "#1F1F1F",
                   "line": "#333333", "line2": "#444444", "text": "#F3F3F3", "text2": "#C4C4C4", "text3": "#9E9E9E",
                   "accent": "#F3F3F3", "on-accent": "#1C1C1C", "sel": "#2F3338",
                   "problem": "#FF8F98", "note": "#F2C661", "checked": "#9DB7CC", "skipped": "#9E9E9E"},
        "swatches": [("bg", "Mica ground"), ("surface", "a layer"), ("raised", "item panel"), ("line", "stroke"),
                     ("text", "text, primary"), ("text2", "secondary"), ("text3", "metadata, Skipped"),
                     ("problem", "Problem"), ("note", "Note"), ("checked", "Checked — a dot")],
        "on": "surface",
    },
    {
        "id": "cutout", "name": "Cut-out",
        "thesis": "Kit, made quiet. Every item still sits in its own cut-out, but the cut-out is a "
                  "hairline and a breath of shadow, not foam. Colour still only shows through where "
                  "something is wrong, as a thin ring; a step with nothing to check is an empty outline.",
        "from": "Round 2’s Kit, which you marked as close. The heavy wells, the thick rings and the round-cute type are gone; the idea stays.",
        "competitors": "Raycast, Arc, Things",
        "variants": [("Glass", "none — opaque, a dialog lifts with a soft shadow (D4)"),
                     ("Checked", "A — no colour: a tick in the secondary grey (D1)"), ("Icons", "Fluent filled")],
        "risk": "The ring has to stay thin and rare; if three rows in ten carry one, the screen starts to look alarmed. Rows in cut-outs cost a few pixels each against a plain list.",
        "style": "filled", "checked_icon": "checkmark",
        "fonts": {"display": "Rubik", "body": "Rubik", "mono": "Fira Code"},
        "font_note": "Rubik’s softened corners echo the cut-outs, used at small sizes and medium weight so it stays calm. Fira Code for paths, refs and file contents.",
        "tokens": {"bg": "#131415", "surface": "#18191B", "raised": "#1F2023", "well": "#121315",
                   "line": "#26282B", "line2": "#34373B", "text": "#EDEDEE", "text2": "#A6AAB0", "text3": "#888C92",
                   "accent": "#E3E5E8", "on-accent": "#131415", "sel": "#22252A",
                   "problem": "#FF6B63", "note": "#F2C14E", "checked": "#A6AAB0", "skipped": "#888C92"},
        "swatches": [("bg", "ground"), ("surface", "the tray"), ("well", "a cut-out"), ("line", "outline"),
                     ("text", "text"), ("text2", "secondary, Checked"), ("text3", "metadata, Skipped"),
                     ("accent", "steel — primary"), ("problem", "Problem ring"), ("note", "Note ring")],
        "on": "surface",
    },
    {
        "id": "canon", "name": "Canon",
        "thesis": "The category standard, played straight and done well: a near-black ground, three "
                  "greys, hairlines instead of shadows, a white primary button, status as a dot and "
                  "a word. No world and no theme — only the craft the audience already lives in.",
        "from": "What every product in the benchmark converges on (references.md: Linear as the base, Vercel’s dot and word, GitHub’s neutral Skipped).",
        "competitors": "Linear, Vercel, Raycast",
        "variants": [("Glass", "none on surfaces; a light blur behind the dialog’s scrim only (D2 variant)"),
                     ("Checked", "C — a small green dot and the word, never larger than the text (D1)"), ("Icons", "Fluent regular")],
        "risk": "It is familiar on purpose, so it will not be remembered for its look. The bar it sets is execution: if spacing, type and states are not exact, it reads as one more dashboard.",
        "style": "regular", "checked_icon": "circle_small",
        "fonts": {"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
        "font_note": "Inter, because the category is set in it (Linear, Vercel’s old UI, Raycast’s docs); chosen for familiarity, which is this card’s whole point. JetBrains Mono for paths and refs.",
        "tokens": {"bg": "#0E0E10", "surface": "#141416", "raised": "#1A1A1D", "well": "#111113",
                   "line": "#232327", "line2": "#303036", "text": "#EDEDEF", "text2": "#A1A1AA", "text3": "#84848D",
                   "accent": "#EDEDEF", "on-accent": "#0E0E10", "sel": "#1C1C21",
                   "problem": "#F26D6D", "note": "#E8B54A", "checked": "#4CC38A", "skipped": "#84848D"},
        "swatches": [("bg", "ground"), ("surface", "surface"), ("raised", "item panel"), ("line", "hairline"),
                     ("text", "text, primary"), ("text2", "secondary"), ("text3", "metadata, Skipped"),
                     ("problem", "Problem"), ("note", "Note"), ("checked", "Checked — small")],
        "on": "surface",
    },
]

DENSITIES = [("compact", "Compact"), ("default", "Default"), ("comfortable", "Comfortable")]


def block(d, n):
    t = d["tokens"]
    vars_ = ";".join(f"--{k}:{v}" for k, v in t.items())
    vars_ += (f';--font:"{d["fonts"]["body"]}",system-ui,sans-serif;--font-display:"{d["fonts"]["display"]}",system-ui,sans-serif;'
              f'--font-mono:"{d["fonts"]["mono"]}",ui-monospace,monospace')
    var = "".join(f"<li><b>{a}</b> {b}</li>" for a, b in d["variants"])
    return f'''<section class="dir d-{d["id"]}" style='{vars_}' aria-labelledby="h-{d["id"]}">
  <header class="dirhead"><div><p class="dnum">Direction {n} of 3</p><h2 id="h-{d["id"]}">{d["name"]}</h2>
    <p class="thesis">{d["thesis"]}</p></div>
    <div><p class="note2"><b>Where it comes from.</b> {d["from"]}</p>
    <p class="note2"><b>Sits beside.</b> {d["competitors"]}</p>
    <ul class="variants">{var}</ul><p class="note2"><b>Honest risk.</b> {d["risk"]}</p></div></header>
  {bd2.fixed_set(d)}
  <h3 class="lab samplehead">The project, with eslint-autofix open</h3>
  <div class="scale"><div class="native">{bd2.app(d)}</div></div>
  <h3 class="lab samplehead">Export, over the project</h3>
  <div class="scale"><div class="native">{bd2.run(d, False)}</div></div>
  <h3 class="lab samplehead">The remove dialog, over Export</h3>
  <div class="scale"><div class="native">{bd2.run(d, True)}</div></div>
</section>'''


CSS = r"""
:root{--page:#262626;--page-2:#2f2f2f;--page-ink:#e8e8e8;--page-ink-2:#b4b4b4;--page-line:#3d3d3d}
*{box-sizing:border-box}
html{background:var(--page)}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
body{margin:0;background:var(--page);color:var(--page-ink);font:15px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}
.pagehead{max-width:1440px;margin:0 auto;padding:40px 24px 0}
.pagehead h1{font-size:30px;line-height:1.2;margin:0 0 10px;font-weight:600}
.pagehead p{margin:0 0 10px;color:var(--page-ink-2);max-width:96ch}
.pagehead p b{color:var(--page-ink)}
.pagehead a{color:var(--page-ink)}
.bar{position:sticky;top:0;z-index:5;display:flex;flex-wrap:wrap;gap:18px;align-items:center;margin:18px -24px 0;padding:10px 24px;background:var(--page);border-bottom:1px solid var(--page-line)}
.bar nav,.bar .seg{display:flex;gap:6px;align-items:center}
.bar .k{font-size:13px;color:var(--page-ink-2);margin-right:4px}
.bar a,.bar button{font:inherit;font-size:14px;font-weight:600;color:var(--page-ink);text-decoration:none;padding:6px 12px;border-radius:6px;border:1px solid var(--page-line);background:var(--page-2);cursor:pointer}
.bar button[aria-pressed="true"]{background:var(--page-ink);color:var(--page);border-color:var(--page-ink)}
.bar a:focus-visible,.bar button:focus-visible{outline:2px solid var(--page-ink);outline-offset:2px}
.grid{display:flex;flex-direction:column;gap:44px;max-width:1440px;margin:0 auto;padding:24px 24px 56px}
.pagefoot{max-width:1440px;margin:0 auto;padding:0 24px 48px;color:var(--page-ink-2);font-size:13.5px}

/* ---------- the direction block: modest sizes this time ---------- */
.dir{background:var(--bg);color:var(--text);font-family:var(--font);border-radius:12px;padding:32px 36px 40px;overflow:hidden}
.dir code,.dir pre,.dir .t-mono{font-family:var(--font-mono)}
.dir .lab{font:600 11.5px/1.2 var(--font);letter-spacing:.07em;text-transform:uppercase;color:var(--text3);margin:0 0 12px}
.dirhead{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:40px;margin-bottom:30px}
.dnum{margin:0 0 4px;font-size:13px;color:var(--text3)}
.dirhead h2{font-family:var(--font-display);font-size:34px;line-height:1.1;margin:0 0 12px;font-weight:600;letter-spacing:-.015em;scroll-margin-top:70px}
.thesis{font-size:16px;line-height:1.55;margin:0}
.note2{font-size:14px;color:var(--text2);margin:0 0 8px}
.note2 b{color:var(--text)}
.variants{list-style:none;margin:6px 0 10px;padding:8px 0 0;border-top:1px solid var(--line);font-size:14px;color:var(--text2)}
.variants li{margin:0 0 4px}
.variants b{color:var(--text);margin-right:5px}
.fixed{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr) minmax(0,1fr);gap:36px;padding:26px 0 4px;border-top:1px solid var(--line)}
.fixed>div>.lab:not(:first-child){margin-top:22px}
.swatches{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
.swatches li{display:grid;grid-template-columns:34px 1fr;column-gap:10px;font-size:12.5px;line-height:1.35}
.swatches .chip{grid-row:1/4;width:34px;height:46px;border-radius:6px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.14)}
.swatches .hex{font-family:var(--font-mono)}
.swatches .role{color:var(--text2)}
.swatches .cr{color:var(--text3);font-variant-numeric:tabular-nums}
.t-display{font-family:var(--font-display);font-size:28px;line-height:1.15;margin:0 0 8px;font-weight:600;letter-spacing:-.01em}
.t-body{font-size:15px;margin:0 0 8px}
.t-mono{font-size:12.5px;color:var(--text2);margin:0 0 8px}
.t-names{font-size:13.5px;color:var(--text2);margin:0 0 6px}
.t-names b{color:var(--text)}
.fnote{font-size:13px;color:var(--text3);margin:0}
.icons{list-style:none;padding:0;margin:0 0 10px;display:flex;flex-wrap:wrap;gap:8px 16px}
.icons li{display:flex;align-items:center;gap:7px;font-size:13.5px;color:var(--text2)}
.icons .ic{width:18px;height:18px;color:var(--text)}
.btnrow{display:flex;flex-wrap:wrap;gap:8px}
.sevs{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:8px 18px}
.samplehead{margin:34px 0 12px!important}
.scale{width:100%;overflow:hidden;border-radius:8px;box-shadow:0 0 0 1px var(--line2);background:var(--bg)}
.native{width:1280px;transform-origin:0 0}

.ic{width:16px;height:16px;fill:currentColor;flex:none}
.dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:currentColor;margin:0 4px;flex:none}
.mark{display:inline-flex;align-items:center;gap:6px;font-size:var(--fs-s);font-weight:600;white-space:nowrap}
.m-problem{color:var(--problem)} .m-note{color:var(--note)} .m-skipped{color:var(--skipped);font-weight:500} .m-checked{color:var(--checked);font-weight:500}
.c-problem{color:var(--problem)} .c-note{color:var(--note)} .c-skipped{color:var(--skipped)}
.g-problem{color:var(--problem)} .g-note{color:var(--note)} .g-skipped{color:var(--skipped)} .g-checked{color:var(--checked)}

/* ---------- density: one set of variables, three values ---------- */
.dir{--fs:14px;--fs-s:12.5px;--fs-xs:11.5px;--fs-h1:24px;--fs-h2:17px;--py:9px;--px:14px;--gap:8px;--sec:20px;--btn-h:30px;--btn-px:12px;--panel-w:360px;--pad:24px;--ico:16px}
body[data-density="compact"] .dir{--fs:13px;--fs-s:11.5px;--fs-xs:11px;--fs-h1:20px;--fs-h2:15px;--py:6px;--px:12px;--gap:6px;--sec:14px;--btn-h:26px;--btn-px:10px;--panel-w:320px;--pad:18px;--ico:14px}
body[data-density="comfortable"] .dir{--fs:15px;--fs-s:13.5px;--fs-xs:12.5px;--fs-h1:30px;--fs-h2:19px;--py:13px;--px:18px;--gap:12px;--sec:28px;--btn-h:36px;--btn-px:15px;--panel-w:400px;--pad:32px;--ico:18px}
.app .ic{width:var(--ico);height:var(--ico)}

/* ---------- the app, common ---------- */
.app{background:var(--bg);color:var(--text);font-size:var(--fs);line-height:1.45;min-height:760px}
.nav .logo{display:inline-block;width:14px;height:14px;background:var(--text);border-radius:4px}
.product{display:flex;align-items:center;gap:9px;font-weight:600;font-size:var(--fs)}
.links{display:flex;gap:2px}
.links a{display:flex;align-items:center;gap:7px;color:var(--text2);font-size:var(--fs);font-weight:500;padding:calc(var(--py) - 2px) 10px;border-radius:6px}
.links a.on{color:var(--text);background:var(--sel)}
.account{display:flex;align-items:center;gap:8px;font-size:var(--fs-s);color:var(--text2)}
.account img{width:22px;height:22px;object-fit:cover;border-radius:50%}
.main{padding:var(--pad) calc(var(--pad) + 4px)}
.phead{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:var(--gap) 20px;align-items:start}
.crumb{margin:0 0 2px;font-size:var(--fs-s);color:var(--text3)}
.phead h1{font-family:var(--font-display);margin:0;font-size:var(--fs-h1);line-height:1.2;font-weight:600;letter-spacing:-.012em}
.pfactsline{margin:4px 0 0;color:var(--text2);font-size:var(--fs-s)}
.actions{display:flex;gap:6px}
.verdict{grid-column:1/-1;display:flex;align-items:center;gap:18px;flex-wrap:wrap;margin-top:2px}
.vline{margin:0;display:flex;align-items:center;gap:6px;color:var(--text2);font-size:var(--fs-s)}
.vglyph{color:var(--checked)}
.vcounts{margin:0;display:flex;gap:14px;font-size:var(--fs-s);font-weight:600}
.vcounts span{display:flex;align-items:center;gap:5px}
.pdesc{color:var(--text2);max-width:80ch;margin:var(--gap) 0 var(--sec);font-size:var(--fs)}
.btn{display:inline-flex;align-items:center;gap:6px;height:var(--btn-h);padding:0 var(--btn-px);font-size:var(--fs-s);font-weight:500;white-space:nowrap;color:var(--text);border:1px solid var(--line2);background:var(--surface);border-radius:var(--r-s,6px)}
.btn.primary{background:var(--accent);color:var(--on-accent);border-color:var(--accent);font-weight:600}
.btn.icon-only{width:var(--btn-h);padding:0;justify-content:center}
.work.with{display:grid;grid-template-columns:minmax(0,1fr) var(--panel-w);gap:var(--sec);align-items:start}
.set,.sub{list-style:none;margin:0;padding:0}
.row{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:14px;padding:var(--py) var(--px)}
.row h3{display:flex;align-items:center;gap:8px;margin:0 0 1px;font-size:var(--fs);font-weight:600}
.desc{margin:0 0 1px;color:var(--text2);font-size:var(--fs-s)}
.facts{margin:0;color:var(--text3);font-size:var(--fs-xs)}
.facts em{font-style:normal;color:var(--text2)}
.facts code,.callout code,.pfacts code,.sbody code{font-size:.93em}
.marks{margin:0;display:flex;gap:10px}
.kind{font-size:var(--fs-xs);font-weight:500;color:var(--text2)}
.state{display:inline-flex;align-items:center;gap:4px;font-size:var(--fs-xs);font-weight:500;color:var(--text2)}
.state .ic{width:13px;height:13px}
.st-conflict{color:var(--problem)}
.sub{margin-left:calc(var(--px) + 8px)}
.panel{background:var(--raised);padding:calc(var(--pad) - 4px);border-radius:var(--r-m,8px);border:1px solid var(--line)}
.phd{display:flex;justify-content:space-between;gap:10px}
.panel h2{margin:0 0 4px;font-size:var(--fs-h2);font-weight:600}
.chips{display:flex;gap:8px;margin:0 0 8px}
.callout{display:flex;flex-direction:column;gap:6px;padding:calc(var(--py) + 1px) var(--px);font-size:var(--fs-s);margin:4px 0 4px;border-radius:var(--r-s,6px);border:1px solid var(--line2);background:var(--surface)}
.callout .sev{display:flex;align-items:center;gap:6px;font-weight:600}
.callout.c-problem,.callout.c-note{color:var(--text)}
.c-problem.callout .sev{color:var(--problem)} .c-note.callout .sev{color:var(--note)}
.callout .btn{align-self:flex-start;margin-top:2px}
.psec{margin-top:var(--sec)}
.psec h3{margin:0 0 5px;font-size:var(--fs-xs);font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--text3)}
.psec p{margin:0;font-size:var(--fs-s);color:var(--text2)}
.file{margin:0 0 5px;padding:var(--py) var(--px);font-size:var(--fs-xs);line-height:1.6;white-space:pre-wrap;overflow-wrap:anywhere;background:var(--well);border:1px solid var(--line);border-radius:var(--r-s,6px)}
.meta{font-size:var(--fs-xs);color:var(--text3)!important}
.pfacts{display:grid;grid-template-columns:112px 1fr;gap:4px 10px;margin:0;font-size:var(--fs-s)}
.pfacts dt{color:var(--text3)} .pfacts dd{margin:0}
.pact{display:flex;gap:6px;margin-top:var(--sec);flex-wrap:wrap}

.runwrap{position:relative;height:760px;overflow:hidden}
.runwrap .app{min-height:760px}
.veil,.dveil{position:absolute;inset:0}
.run{position:absolute;left:120px;right:120px;top:36px;bottom:0}
.runin{height:100%;overflow:hidden;padding:var(--pad);background:var(--bg);border:1px solid var(--line2);border-bottom:0;border-radius:var(--r-m,8px) var(--r-m,8px) 0 0}
.rhead{display:flex;justify-content:space-between;align-items:flex-start}
.rhead h2{font-family:var(--font-display);font-size:var(--fs-h1);margin:0 0 4px;line-height:1.2;font-weight:600}
.rcounts{margin:0 0 2px;font-size:var(--fs);font-weight:600}
.group{margin:var(--sec) 0 8px;font-size:var(--fs-xs);font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:var(--text3)}
.stages{list-style:none;margin:0;padding:0;border:1px solid var(--line);border-radius:var(--r-m,8px);background:var(--surface)}
.stage+.stage{border-top:1px solid var(--line)}
.sum{display:grid;grid-template-columns:26px 170px minmax(0,1fr) 56px;gap:12px;align-items:center;padding:var(--py) var(--px);font-size:var(--fs)}
.n{font-size:var(--fs-xs);color:var(--text3);font-variant-numeric:tabular-nums}
.sname{font-weight:600}
.res{display:flex;align-items:center;gap:7px;color:var(--text2);font-size:var(--fs-s)}
.s-problem .res span{color:var(--problem);font-weight:600}
.s-note .res span{color:var(--note);font-weight:600}
.time{text-align:right;font-family:var(--font-mono);font-size:var(--fs-xs);color:var(--text2);font-variant-numeric:tabular-nums}
.sbody{padding:0 var(--px) var(--py) calc(var(--px) + 38px)}
.slots{display:flex;gap:8px;flex-wrap:wrap;margin-top:4px}
.slot{display:inline-flex;align-items:center;gap:6px;font-size:var(--fs-xs);padding:3px 9px;border-radius:999px;border:1px solid var(--line2)}
.slot small{color:var(--text3);font-size:var(--fs-xs)}
.slot .ic{width:13px;height:13px;color:var(--text2)}
.dlg{position:absolute;left:50%;top:260px;transform:translateX(-50%);width:440px}
.sheet{padding:calc(var(--pad) - 2px);background:var(--raised);border:1px solid var(--line2);border-radius:var(--r-m,8px)}
.sheet h2{font-family:var(--font-display);font-size:var(--fs-h2);margin:0 0 8px;line-height:1.3;font-weight:600}
.sheet p{margin:0 0 6px;font-size:var(--fs-s);color:var(--text2)}
.dact{display:flex;justify-content:flex-end;gap:8px;margin-top:var(--sec)}

/* ================= Mica ================= */
.d-mica{--r-s:4px;--r-m:8px}
.d-mica .nav{display:flex;align-items:center;gap:22px;height:calc(var(--btn-h) + 16px);padding:0 calc(var(--pad) + 4px);background:#1A1A1A;border-bottom:1px solid var(--line)}
.d-mica .links a{border-radius:4px}
.d-mica .links a.on{background:var(--raised);box-shadow:inset 0 -2px 0 var(--text2)}
.d-mica .account{margin-left:auto}
.d-mica .btn{background:#2D2D2D;border-color:#3A3A3A;border-bottom-color:#2A2A2A}
.d-mica .btn.primary{background:var(--accent);border-color:var(--accent)}
.d-mica .set{background:var(--surface);border:1px solid var(--line);border-radius:8px}
.d-mica .set>li+li{border-top:1px solid var(--line)}
.d-mica .sub>li{border-top:1px solid var(--line)}
.d-mica .sub{border-left:1px solid var(--line2)}
.d-mica .kind{padding:0 6px;border-radius:4px;background:#2F2F2F}
.d-mica .it.sel>.row{background:var(--sel);box-shadow:inset 0 0 0 1px #5A6470;border-radius:4px}
.d-mica .veil{background:rgba(0,0,0,.30)}
.d-mica .run{padding:8px 8px 0;border-radius:12px 12px 0 0;background:rgba(60,60,60,.42);backdrop-filter:blur(30px) saturate(140%);-webkit-backdrop-filter:blur(30px) saturate(140%);border:1px solid rgba(255,255,255,.12);border-bottom:0}
.d-mica .runin{border-color:rgba(255,255,255,.06)}
.d-mica .dveil{background:rgba(0,0,0,.25)}
.d-mica .dlg{padding:8px;border-radius:12px;background:rgba(70,70,70,.45);backdrop-filter:blur(26px) saturate(140%);-webkit-backdrop-filter:blur(26px) saturate(140%);border:1px solid rgba(255,255,255,.14)}
.d-mica .callout.c-problem{border-color:rgba(255,143,152,.32);background:rgba(255,143,152,.06)}
.d-mica .callout.c-note{border-color:rgba(242,198,97,.30);background:rgba(242,198,97,.05)}

/* ================= Cut-out ================= */
.d-cutout{--r-s:8px;--r-m:12px}
.d-cutout .nav{display:flex;align-items:center;gap:22px;height:calc(var(--btn-h) + 18px);padding:0 calc(var(--pad) + 4px);border-bottom:1px solid var(--line)}
.d-cutout .links{background:var(--well);padding:3px;border-radius:9px;box-shadow:inset 0 0 0 1px var(--line)}
.d-cutout .links a.on{background:var(--raised);box-shadow:0 1px 2px rgba(0,0,0,.4)}
.d-cutout .account{margin-left:auto}
.d-cutout .account img{border-radius:7px}
.d-cutout .btn{background:var(--raised);border-color:var(--line2)}
.d-cutout .btn.primary{background:var(--accent);border-color:var(--accent)}
.d-cutout .set{display:flex;flex-direction:column;gap:var(--gap);padding:var(--gap);background:var(--surface);border-radius:14px;border:1px solid var(--line)}
.d-cutout .set>li{background:var(--well);border-radius:10px;box-shadow:inset 0 0 0 1px var(--line),inset 0 1px 2px rgba(0,0,0,.45)}
.d-cutout .set>li.has-problem{box-shadow:inset 0 0 0 1.5px var(--problem),inset 0 1px 2px rgba(0,0,0,.45)}
.d-cutout .set>li.has-note{box-shadow:inset 0 0 0 1.5px rgba(242,193,78,.7),inset 0 1px 2px rgba(0,0,0,.45)}
.d-cutout .set>li.sel{outline:1.5px solid var(--accent);outline-offset:2px}
.d-cutout .sub{margin-left:calc(var(--px) + 10px);padding-bottom:2px}
.d-cutout .sub>li{border-top:1px dashed var(--line2)}
.d-cutout .kind{padding:0 7px;border-radius:999px;background:var(--raised)}
.d-cutout .panel{border-radius:14px;box-shadow:0 10px 30px rgba(0,0,0,.35)}
.d-cutout .callout{background:var(--well);border-color:transparent;box-shadow:inset 0 0 0 1.5px var(--problem)}
.d-cutout .callout.c-note{box-shadow:inset 0 0 0 1.5px rgba(242,193,78,.7)}
.d-cutout .veil{background:rgba(0,0,0,.5)}
.d-cutout .run{left:auto;right:0;top:0;width:840px}
.d-cutout .runin{border-radius:16px 0 0 16px;border-bottom:1px solid var(--line2);background:var(--surface)}
.d-cutout .stages{display:flex;flex-direction:column;gap:var(--gap);border:0;background:transparent}
.d-cutout .stage{background:var(--well);border-radius:10px;box-shadow:inset 0 0 0 1px var(--line)}
.d-cutout .stage+.stage{border-top:0}
.d-cutout .stage.s-problem{box-shadow:inset 0 0 0 1.5px var(--problem)}
.d-cutout .stage.s-note{box-shadow:inset 0 0 0 1.5px rgba(242,193,78,.7)}
.d-cutout .stage.s-skipped{background:transparent;box-shadow:none;outline:1px dashed var(--line2);outline-offset:-1px}
.d-cutout .stage .callout{box-shadow:none;background:transparent;padding:0}
.d-cutout .slot{border-style:dashed;border-radius:8px}
.d-cutout .dveil{background:rgba(0,0,0,.4)}
.d-cutout .sheet{border-radius:14px;box-shadow:0 20px 50px rgba(0,0,0,.5)}

/* ================= Canon ================= */
.d-canon{--r-s:6px;--r-m:10px}
.d-canon .app{display:grid;grid-template-columns:200px minmax(0,1fr)}
.d-canon .nav{display:flex;flex-direction:column;gap:18px;padding:var(--pad) 12px;border-right:1px solid var(--line);background:var(--bg)}
.d-canon .product{padding:0 8px}
.d-canon .links{flex-direction:column}
.d-canon .links a.on{background:var(--raised)}
.d-canon .account{margin-top:auto;padding:0 8px}
.d-canon .btn{background:transparent;border-color:var(--line2)}
.d-canon .btn.primary{background:var(--accent);border-color:var(--accent)}
.d-canon .set{border-top:1px solid var(--line)}
.d-canon .set>li{border-bottom:1px solid var(--line)}
.d-canon .sub>li{border-top:1px solid var(--line)}
.d-canon .kind{color:var(--text3)}
.d-canon .it.sel>.row{background:var(--sel)}
.d-canon .panel{border-radius:10px}
.d-canon .callout.c-problem{border-color:rgba(242,109,109,.3);background:rgba(242,109,109,.05)}
.d-canon .callout.c-note{border-color:rgba(232,181,74,.28);background:rgba(232,181,74,.05)}
.d-canon .veil{background:rgba(0,0,0,.55)}
.d-canon .run{left:160px;right:160px;top:40px}
.d-canon .dveil{background:rgba(0,0,0,.35);backdrop-filter:blur(3px);-webkit-backdrop-filter:blur(3px)}
.d-canon .sheet{box-shadow:0 16px 40px rgba(0,0,0,.5)}

@media (max-width:1100px){.dirhead,.fixed{grid-template-columns:minmax(0,1fr);gap:24px}.dir{padding:24px 18px 28px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

JS = r"""
(function(){
  function fit(){document.querySelectorAll('.scale').forEach(function(s){
    var n=s.firstElementChild,k=Math.min(1,s.clientWidth/1280);n.style.transform='scale('+k+')';s.style.height=(n.offsetHeight*k)+'px';});}
  var bs=document.querySelectorAll('[data-d]');
  function set(v){document.body.dataset.density=v;bs.forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.d===v));});
    try{localStorage.setItem('directions-density',v);}catch(e){} fit();}
  bs.forEach(function(b){b.addEventListener('click',function(){set(b.dataset.d);});});
  try{var v=localStorage.getItem('directions-density'); if(v){set(v);} }catch(e){}
  window.addEventListener('resize',fit);
  if(document.fonts&&document.fonts.ready){document.fonts.ready.then(fit);}
  window.addEventListener('load',fit);fit();
})();
"""

FONTS = ("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500"
         "&family=Rubik:wght@400;500;600&family=Fira+Code:wght@400;500&family=Cascadia+Code:wght@400&display=swap")


def build():
    blocks = "".join(block(d, i + 1) for i, d in enumerate(DIRS))
    dens = "".join(f'<button type="button" data-d="{k}" aria-pressed="{str(k == "default").lower()}">{v}</button>' for k, v in DENSITIES)
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Round three · AI Stack Builder</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}"><style>{CSS}</style></head>
<body data-density="default">{bd1.symbols()}
<header class="pagehead">
  <h1>Three calmer directions, at three densities</h1>
  <p>Phase 06, stage 3, <b>round 3</b>, after <a href="directions.html">round 1</a> and <a href="directions-2.html">round 2</a>. What you asked for: <b>calmer but better made</b>; <b>Acrylic and Kit were the closest</b>; <b>the type and the spacing were too large</b>. So two directions are calm descendants of those two, the third is the category standard done properly, and <b>density is its own switch</b> — choose a style and a density separately, and combine them.</p>
  <p>The samples are drawn at <b>1:1</b> on a 1280 px canvas, never scaled up. Every word is from <code>microcopy.md</code>. Ratios are WCAG contrast, computed at build.</p>
  <div class="bar"><nav aria-label="Directions"><span class="k">Jump to</span><a href="#h-mica">1 · Mica</a><a href="#h-cutout">2 · Cut-out</a><a href="#h-canon">3 · Canon</a></nav>
    <div class="seg" role="group" aria-label="Density"><span class="k">Density</span>{dens}</div></div>
</header>
<main class="grid">{blocks}</main>
<p class="pagefoot">Built by <code>tools/build_directions_3.py</code>. Icons: Microsoft Fluent System Icons, MIT, @fluentui/svg-icons 1.1.344. Portrait: Jake Nackos on Unsplash (unsplash.com/photos/IF9TK5Uy-KI), standing in for the signed-in person.</p>
<script>{JS}</script></body></html>'''
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}  {len(html)//1024} KB")
    for d in DIRS:
        t = d["tokens"]
        for bgk in (d["on"], "raised", "well", "sel"):
            low = [(k, round(ratio(t[k], t[bgk]), 2)) for k in ("text", "text2", "text3", "problem", "note", "checked")
                   if ratio(t[k], t[bgk]) < 4.5]
            if low:
                print(d["name"], "on", bgk, "below 4.5:", low)


if __name__ == "__main__":
    build()
