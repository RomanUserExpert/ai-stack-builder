"""Phase 06, stage 3, round 4: build 06-concept/directions-4.html — Mica, three ways.

The owner's answer to round 3 (2026-10-11): Mica, more or less; density between Default and
Comfortable; now three variants of Mica with different typefaces, different icon libraries if
useful, and different brand colours. The material (Mica ground, acrylic only at the frame of a
mode) and the layout stay; type, icons and brand colour change.

    python tools/build_directions_4.py   -> 06-concept/directions-4.html

Markup from tools/build_directions_2.py, base CSS from tools/build_directions_3.py.
Icons: Fluent (06-concept/fluent, MIT), Phosphor (06-concept/icons/phosphor, MIT),
Lucide (06-concept/icons/lucide, ISC).
"""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("bd3", ROOT / "tools" / "build_directions_3.py")
bd3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bd3)
bd2, bd1, ratio = bd3.bd2, bd3.bd1, bd3.ratio
OUT = ROOT / "06-concept" / "directions-4.html"

# canonical icon name -> file name in each library
ICONMAP = {
    "fluent": {n: n for n in ["library", "globe", "folder", "options", "share", "copy", "arrow_export_ltr", "dismiss",
                              "link", "link_dismiss", "arrow_turn_down_right", "key", "error_circle", "info", "prohibited",
                              "checkmark", "puzzle_piece", "bot", "prompt", "plug_connected", "script", "app_generic"]},
    "phosphor": {"library": "books", "globe": "globe", "folder": "folder", "options": "sliders-horizontal",
                 "share": "share-network", "copy": "copy", "arrow_export_ltr": "export", "dismiss": "x", "link": "link",
                 "link_dismiss": "link-break", "arrow_turn_down_right": "arrow-elbow-down-right", "key": "key",
                 "error_circle": "warning-circle", "info": "info", "prohibited": "prohibit", "checkmark": "check",
                 "puzzle_piece": "puzzle-piece", "bot": "robot", "prompt": "chat-text", "plug_connected": "plug",
                 "script": "file-code", "app_generic": "app-window"},
    "lucide": {"library": "library", "globe": "globe", "folder": "folder", "options": "sliders-horizontal",
               "share": "share-2", "copy": "copy", "arrow_export_ltr": "upload", "dismiss": "x", "link": "link",
               "link_dismiss": "unlink", "arrow_turn_down_right": "corner-down-right", "key": "key-round",
               "error_circle": "circle-alert", "info": "info", "prohibited": "ban", "checkmark": "check",
               "puzzle_piece": "puzzle", "bot": "bot", "prompt": "message-square-text", "plug_connected": "plug",
               "script": "file-code", "app_generic": "app-window"},
}
LIBNOTE = {"fluent": "Microsoft Fluent System Icons, regular, MIT",
           "phosphor": "Phosphor Icons, regular, MIT (@phosphor-icons/core 2.1.1)",
           "lucide": "Lucide, 1.75 px stroke, ISC (lucide-static 1.55.0)"}


def _symbol(lib, canon, file):
    if lib == "fluent":
        svg = (ROOT / "06-concept" / "fluent" / f"{file}_20_regular.svg").read_text(encoding="utf-8")
        attrs = 'viewBox="0 0 20 20" fill="currentColor"'
    elif lib == "phosphor":
        svg = (ROOT / "06-concept" / "icons" / "phosphor" / f"{file}.svg").read_text(encoding="utf-8")
        attrs = 'viewBox="0 0 256 256" fill="currentColor"'
    else:
        svg = (ROOT / "06-concept" / "icons" / "lucide" / f"{file}.svg").read_text(encoding="utf-8")
        attrs = ('viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" '
                 'stroke-linecap="round" stroke-linejoin="round"')
    inner = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1).strip()
    return f'<symbol id="j-{lib}-{canon}" {attrs}>{inner}</symbol>'


def symbols():
    out = [_symbol(lib, c, f) for lib, m in ICONMAP.items() for c, f in m.items()]
    return '<svg width="0" height="0" style="position:absolute" aria-hidden="true">' + "".join(out) + "</svg>"


def ic(d, name, cls=""):
    if name == "circle_small":
        return f'<span class="dot {cls}" aria-hidden="true"></span>'
    return f'<svg class="ic {cls}" aria-hidden="true"><use href="#j-{d["lib"]}-{name}"/></svg>'


bd1.ic = ic  # every markup helper in rounds 1-3 resolves ic through bd1 at call time

BASE = {"problem": "#FF8F98", "note": "#F2C661", "skipped": None}
DIRS = [
    {
        "id": "cobalt", "name": "Mica · Cobalt", "lib": "fluent",
        "thesis": "The closest to Windows itself: Fluent icons, a cobalt that reads as the system accent, "
                  "and Mona Sans — GitHub’s typeface — so it sits naturally beside the repos everything here comes from.",
        "brand_note": "Cobalt is familiar in tools, so it carries the least risk and the least character. It is used only where you can act or where you are: the primary button, the current place, a selection.",
        "fonts": {"display": "Mona Sans", "body": "Mona Sans", "mono": "JetBrains Mono"},
        "font_note": "Mona Sans: GitHub’s own grotesk, slightly wide, calm at small sizes. JetBrains Mono for paths, refs and file contents.",
        "tokens": {"bg": "#1A1B1F", "surface": "#22242A", "raised": "#292B31", "well": "#1D1E22", "nav": "#17181B",
                   "btn": "#2C2F36", "line": "#33363D", "line2": "#444851",
                   "text": "#F2F3F5", "text2": "#C3C6CC", "text3": "#9A9EA6",
                   "brand": "#7DA2FF", "on-brand": "#0D1324", "sel": "#252C3D",
                   "accent": "#7DA2FF", "on-accent": "#0D1324",
                   "problem": "#FF8F98", "note": "#F2C661", "checked": "#A9BBD0", "skipped": "#9A9EA6"},
    },
    {
        "id": "jade", "name": "Mica · Jade", "lib": "phosphor",
        "thesis": "Softer and a little warmer: Phosphor’s rounder icons, Onest’s open forms, and a jade "
                  "brand colour that no AI tool wears — calm, but not grey.",
        "brand_note": "Jade sits between blue and green. Green here never means a verdict — Checked stays a quiet dot — so the brand cannot be read as “works”.",
        "fonts": {"display": "Onest", "body": "Onest", "mono": "Fira Code"},
        "font_note": "Onest: a humanist-geometric sans with open apertures, friendly at 14–15 px without looking rounded-cute. Fira Code for paths, refs and file contents.",
        "tokens": {"bg": "#1A1C1B", "surface": "#212524", "raised": "#282C2B", "well": "#1C1F1E", "nav": "#171918",
                   "btn": "#2B302F", "line": "#323837", "line2": "#434A48",
                   "text": "#F1F4F3", "text2": "#C1C8C6", "text3": "#98A09E",
                   "brand": "#4FD6B4", "on-brand": "#0A1A15", "sel": "#1F302C",
                   "accent": "#4FD6B4", "on-accent": "#0A1A15",
                   "problem": "#FF8F98", "note": "#F2C661", "checked": "#B5C4C0", "skipped": "#98A09E"},
    },
    {
        "id": "lime", "name": "Mica · Lime", "lib": "lucide",
        "thesis": "The sharpest of the three: Lucide’s thin line icons, Schibsted Grotesk’s editorial "
                  "precision, and a lime brand that you cannot miss — but only ever see on what you can press.",
        "brand_note": "Lime is loud, so it is rationed hardest: the primary button and the current place, nothing else. It is the most memorable of the three and the one most likely to tire.",
        "fonts": {"display": "Schibsted Grotesk", "body": "Schibsted Grotesk", "mono": "Source Code Pro"},
        "font_note": "Schibsted Grotesk: a newspaper grotesk, compact and precise, a firmer voice than the other two. Source Code Pro for paths, refs and file contents.",
        "tokens": {"bg": "#1B1C19", "surface": "#232420", "raised": "#2A2B27", "well": "#1E1F1B", "nav": "#181916",
                   "btn": "#2E302A", "line": "#343630", "line2": "#464840",
                   "text": "#F3F4EF", "text2": "#C5C7BE", "text3": "#9C9F95",
                   "brand": "#C6EF5A", "on-brand": "#141A08", "sel": "#2A3020",
                   "accent": "#C6EF5A", "on-accent": "#141A08",
                   "problem": "#FF8F98", "note": "#F2C661", "checked": "#C5C7BE", "skipped": "#9C9F95"},
    },
]
for d in DIRS:
    d.update({"style": "regular", "checked_icon": "circle_small", "on": "surface",
              "swatches": [("bg", "Mica ground, tinted"), ("surface", "a layer"), ("raised", "item panel"),
                           ("line", "stroke"), ("text", "text"), ("text2", "secondary"), ("text3", "metadata, Skipped"),
                           ("brand", "brand — primary, current, selection"), ("problem", "Problem"), ("note", "Note"),
                           ("checked", "Checked — a dot")]})


def fixed_set(d):
    # round 2's fixed set, with the icon line naming the library actually used
    html = bd2.fixed_set(d)
    return html.replace(f'Icons · Fluent {d["style"]}', f'Icons · {LIBNOTE[d["lib"]]}')


def block(d, n):
    t = d["tokens"]
    vars_ = ";".join(f"--{k}:{v}" for k, v in t.items())
    vars_ += (f';--font:"{d["fonts"]["body"]}",system-ui,sans-serif;--font-display:"{d["fonts"]["display"]}",system-ui,sans-serif;'
              f'--font-mono:"{d["fonts"]["mono"]}",ui-monospace,monospace')
    br = t["brand"]
    pairs = (f'{ratio(t["on-brand"], br):.1f}:1 text on the button · {ratio(br, t["surface"]):.1f}:1 as a colour on the surface')
    return f'''<section class="dir d-mica v-{d["id"]}" style='{vars_}' aria-labelledby="h-{d["id"]}">
  <header class="dirhead"><div><p class="dnum">Variant {n} of 3</p><h2 id="h-{d["id"]}">{d["name"]}</h2>
    <p class="thesis">{d["thesis"]}</p></div>
    <div><p class="note2"><b>Brand colour.</b> {d["brand_note"]}</p><p class="note2"><b>Contrast.</b> {pairs}</p>
    <ul class="variants"><li><b>Type</b> {d["fonts"]["body"]} + {d["fonts"]["mono"]}</li><li><b>Icons</b> {LIBNOTE[d["lib"]]}</li>
    <li><b>Same as Mica</b> Mica ground, acrylic only around the Export mode and a dialog, Checked as a quiet dot (D1-B)</li></ul></div></header>
  {fixed_set(d)}
  <h3 class="lab samplehead">The project, with eslint-autofix open</h3>
  <div class="scale"><div class="native">{bd2.app(d)}</div></div>
  <h3 class="lab samplehead">Export, over the project</h3>
  <div class="scale"><div class="native">{bd2.run(d, False)}</div></div>
  <h3 class="lab samplehead">The remove dialog, over Export</h3>
  <div class="scale"><div class="native">{bd2.run(d, True)}</div></div>
</section>'''


CSS = bd3.CSS + r"""
/* the owner's density: between Default and Comfortable */
body[data-density="between"] .dir{--fs:14.5px;--fs-s:13px;--fs-xs:12px;--fs-h1:27px;--fs-h2:18px;--py:11px;--px:16px;--gap:10px;--sec:24px;--btn-h:33px;--btn-px:14px;--panel-w:380px;--pad:28px;--ico:17px}
.ic{fill:none}

/* Mica, made brand-aware: the brand appears where you can act or where you are, nowhere else */
.v-cobalt,.v-jade,.v-lime{--r-s:5px;--r-m:9px}
.d-mica .nav{background:var(--nav)}
.d-mica .logo{background:var(--brand)}
.d-mica .links a.on{background:var(--raised);box-shadow:inset 0 -2px 0 var(--brand);color:var(--text)}
.d-mica .btn{background:var(--btn);border-color:var(--line2)}
.d-mica .btn.primary{background:var(--brand);color:var(--on-brand);border-color:var(--brand)}
.d-mica .it.sel>.row{background:var(--sel);box-shadow:inset 0 0 0 1px var(--brand);border-radius:5px}
.d-mica .kind{background:var(--btn)}
.d-mica .run{background:color-mix(in srgb,var(--brand) 9%,rgba(58,60,64,.45))}
.d-mica .dlg{background:color-mix(in srgb,var(--brand) 9%,rgba(64,66,70,.45))}
.d-mica .swatches .chip{border-radius:5px}
.v-lime .phead h1,.v-lime .rhead h2{letter-spacing:-.02em}
.d-mica .dlg{width:500px}

/* the owner's form (2026-10-11, from round 2's Kit): every item in its own rounded cut-out,
   a coloured ring only where a finding is, the selection as an outline around the cut-out,
   auto-added items inside their parent's cut-out behind a dashed rule */
.d-mica{--r-s:7px;--r-m:14px}
.d-mica .set{display:flex;flex-direction:column;gap:var(--gap);padding:var(--gap);background:var(--surface);border:0;border-radius:18px}
.d-mica .set>li{background:var(--well);border-radius:12px;box-shadow:inset 0 0 0 1px var(--line),inset 0 1px 3px rgba(0,0,0,.45)}
.d-mica .set>li+li{border-top:0}
.d-mica .set>li.has-problem{box-shadow:inset 0 0 0 1.5px var(--problem),inset 0 1px 3px rgba(0,0,0,.45)}
.d-mica .set>li.has-note{box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--note) 75%,transparent),inset 0 1px 3px rgba(0,0,0,.45)}
.d-mica .set>li.sel{outline:1.5px solid var(--brand);outline-offset:3px}
.d-mica .it.sel>.row{background:transparent;box-shadow:none}
.d-mica .sub{border-left:0;margin-left:calc(var(--px) + 12px);padding-bottom:2px}
.d-mica .sub>li{border-top:1px dashed var(--line2)}
.d-mica .kind{padding:1px 8px;border-radius:999px;background:var(--btn)}
.d-mica .btn{border-radius:8px}
.d-mica .links a{border-radius:8px}
.d-mica .panel{border-radius:18px;border:1px solid var(--line)}
.d-mica .callout{border-radius:12px}
.d-mica .callout.c-problem{background:var(--well);border-color:transparent;box-shadow:inset 0 0 0 1.5px var(--problem)}
.d-mica .callout.c-note{background:var(--well);border-color:transparent;box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--note) 75%,transparent)}
.d-mica .file{border-radius:10px}
.d-mica .stages{display:flex;flex-direction:column;gap:var(--gap);border:0;background:transparent}
.d-mica .stage{background:var(--well);border-radius:12px;box-shadow:inset 0 0 0 1px var(--line)}
.d-mica .stage+.stage{border-top:0}
.d-mica .stage.s-problem{box-shadow:inset 0 0 0 1.5px var(--problem)}
.d-mica .stage.s-note{box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--note) 75%,transparent)}
.d-mica .stage.s-skipped{background:transparent;box-shadow:none;outline:1px dashed var(--line2);outline-offset:-1px}
.d-mica .stage .callout{box-shadow:none;background:transparent;padding:0}
.d-mica .slot{border-style:dashed;border-radius:8px}
.d-mica .run{border-radius:20px 20px 0 0}
.d-mica .runin{border-radius:14px 14px 0 0}
.d-mica .dlg{border-radius:20px}
.d-mica .sheet{border-radius:14px}
"""

FONTS = ("https://fonts.googleapis.com/css2?family=Mona+Sans:wght@400;500;600;700&family=Onest:wght@400;500;600;700"
         "&family=Schibsted+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Fira+Code:wght@400;500"
         "&family=Source+Code+Pro:wght@400;500&display=swap")
DENS = [("default", "Default"), ("between", "Between"), ("comfortable", "Comfortable")]


def build():
    blocks = "".join(block(d, i + 1) for i, d in enumerate(DIRS))
    dens = "".join(f'<button type="button" data-d="{k}" aria-pressed="{str(k == "between").lower()}">{v}</button>' for k, v in DENS)
    js = bd3.JS.replace("directions-density", "directions4-density")
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mica, three ways · AI Stack Builder</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}"><style>{CSS}</style></head>
<body data-density="between">{symbols()}
<header class="pagehead">
  <h1>Mica, three ways</h1>
  <p>Phase 06, stage 3, <b>round 4</b>. From <a href="directions-3.html">round 3</a> you kept <b>Mica</b>, at a density <b>between Default and Comfortable</b>. These three keep Mica’s material and layout and change three things: <b>the typeface</b>, <b>the icon library</b> and <b>the brand colour</b>. The brand colour is rationed: the primary button, the place you are, a selection — never a verdict.</p>
  <p>The samples are 1:1 on a 1280 px canvas. Every word is from <code>microcopy.md</code>. Ratios are WCAG contrast, computed at build.</p>
  <div class="bar"><nav aria-label="Variants"><span class="k">Jump to</span><a href="#h-cobalt">1 · Cobalt</a><a href="#h-jade">2 · Jade</a><a href="#h-lime">3 · Lime</a></nav>
    <div class="seg" role="group" aria-label="Density"><span class="k">Density</span>{dens}</div></div>
</header>
<main class="grid">{blocks}</main>
<p class="pagefoot">Built by <code>tools/build_directions_4.py</code>. Icons: Fluent (MIT), Phosphor (MIT), Lucide (ISC). Portrait: Jake Nackos on Unsplash (unsplash.com/photos/IF9TK5Uy-KI), standing in for the signed-in person.</p>
<script>{js}</script></body></html>'''
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}  {len(html)//1024} KB")
    for d in DIRS:
        t = d["tokens"]
        for bgk in ("surface", "raised", "sel"):
            low = [(k, round(ratio(t[k], t[bgk]), 2)) for k in ("text", "text2", "text3", "problem", "note", "checked", "brand")
                   if ratio(t[k], t[bgk]) < 4.5]
            if low:
                print(d["name"], "on", bgk, "below 4.5:", low)
        print(d["name"], "on-brand", round(ratio(t["on-brand"], t["brand"]), 2))


if __name__ == "__main__":
    build()
