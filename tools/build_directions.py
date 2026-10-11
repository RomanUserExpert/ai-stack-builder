"""Phase 06, stage 3: build 06-concept/directions.html — three directions side by side.

One sample (the Project screen with eslint-autofix open, a Run stage strip and the remove
dialog over it), drawn three times from one markup. Each direction is a set of tokens plus a
short block of its own CSS. Every word on the sample comes from 04-wireframes/pages/
project-item.html and run-remove.html, which are microcopy.md's lines, unchanged.

    python tools/build_directions.py   -> 06-concept/directions.html

Fluent icons are read from 06-concept/fluent/ (MIT, @fluentui/svg-icons 1.1.344) and inlined as
<symbol>s, so the page needs no icon request. Contrast ratios on the swatches are computed here.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / "06-concept" / "fluent"
OUT = ROOT / "06-concept" / "directions.html"

PORTRAIT = ("https://images.unsplash.com/photo-1580489944761-15a19d654956"
            "?w=96&h=96&fit=crop&crop=faces&auto=format&q=80")

# ---------------------------------------------------------------- contrast
def _lum(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = _lum(a), _lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


# ---------------------------------------------------------------- the three
DIRS = [
    {
        "id": "acrylic",
        "name": "Acrylic",
        "thesis": "The work is opaque and still. What you enter is acrylic laid over it — the "
                  "Export mode, a dialog, a menu — so the place you came from shows through, "
                  "blurred, at the edge.",
        "world": "Microsoft’s Fluent: Mica under the app, acrylic on what is temporary, Segoe’s "
                 "optical sizes, 4 px controls and 8 px flyouts.",
        "why": [
            ("Taste", "Teams / Slack glass, “noticeable, but sparing”; Fluent icons are the same family"),
            ("Pair 4", "glass is a layer over the work, never the work: rows, the item panel and the findings stay opaque"),
            ("Pair 2", "dense rows held by type weight and a tinted ground, not by cards"),
        ],
        "variants": [("Glass", "frame and edges only; text always on an opaque inner sheet (D2, D3)"),
                     ("Checked", "B — a quiet steel dot, not green (D1)"),
                     ("Icons", "Fluent regular, 20")],
        "raises": [
            "Severity is carried by shape as well as colour — a crossed circle, an i, a slashed circle, a tick — so it survives greyscale. Kept from a dance-notation score, where shading and shape encode level without colour.",
            "Every count and duration is set in tabular figures in one right-aligned column: 0.3 s and 0.1 s read as data. Kept from a data-sublime field of monospace numerics.",
            "One family through the whole scale: Segoe’s Display size for the title, Text for the rows. Kept from a type specimen that repeats one face at five sizes.",
        ],
        "risk": "Graphite with one accent is the nearest of the three to the dark-tool cluster; the berry has to stay flat and rare, or it slides toward the violet the taste refuses. Segoe is a system face: on a Mac it falls back to SF.",
        "guess": "Not from the subject: an “AI tool” guess is near-black with violet-blue glow. Graphite-blue Mica with a flat berry, no gradient, no glow.",
        "style": "regular",
        "checked_icon": "circle_small",
        "fonts": {"display": "Segoe UI Variable Display", "body": "Segoe UI Variable Text",
                  "mono": "Cascadia Code"},
        "font_note": "Segoe UI Variable is Windows’ own face, read from the system — Fluent’s rule. Cascadia Code is Microsoft’s mono, from Google Fonts, used only for paths, refs and file contents.",
        "tokens": {
            "bg": "#121418", "surface": "#181B20", "raised": "#20242A",
            "line": "#2B3037", "line2": "#3A4048",
            "text": "#ECEEF1", "text2": "#AAB0B9", "text3": "#8B929C",
            "accent": "#D97BD3", "on-accent": "#1E0E1C",
            "problem": "#F47C84", "note": "#EBC066", "checked": "#8FB0C8", "skipped": "#8B929C",
        },
        "swatches": [("bg", "Mica ground"), ("surface", "the set, the work"), ("raised", "item panel, sheets"),
                     ("line", "hairline"), ("text", "text"), ("text2", "secondary"), ("text3", "metadata"),
                     ("accent", "Berry — primary, selection"), ("problem", "Problem"), ("note", "Note"),
                     ("checked", "Checked — a dot")],
        "on": "surface",
    },
    {
        "id": "manifest",
        "name": "Manifest",
        "thesis": "A project is a consignment. Every row is a declared line, every fact sits in a "
                  "labelled field, and the item you open is the paper declaration pulled out of "
                  "the hall — the one light surface in a dark product.",
        "world": "Customs and shipping papers: the manifest, the declaration form, the inspection "
                 "slip; petrol-dark container steel, kraft paper, stamp inks.",
        "why": [
            ("Pair 3", "the consequence sits in a labelled field before the step, like a declared value"),
            ("Pair 1", "an inspector’s slip, not a seal: what was examined, when, the counts"),
            ("Data", "the export is a handover — the archive leaves for a receiving machine (§6)"),
        ],
        "variants": [("Glass", "only as the scrim: the place behind a mode is frosted, every sheet is opaque (D2 variant)"),
                     ("Checked", "C — small green, never the largest thing on screen (D1)"),
                     ("Icons", "Fluent filled, 20")],
        "raises": [],
        "risk": "The most committed of the three, and the paper panel is a light surface inside a dark product: it has to earn that by being the place a person reads closely, and it doubles the severity colours. A document world can turn into a costume if the ruling spreads past the fields.",
        "guess": "Not from the subject: petrol and paper belong to freight, not to AI. Nothing violet, nothing glowing.",
        "style": "filled",
        "checked_icon": "checkmark",
        "fonts": {"display": "Archivo", "body": "Archivo", "mono": "Martian Mono"},
        "font_note": "Archivo’s width axis does the work of two faces: 112 for the title, 100 for rows, 75 for the field labels of a form. Martian Mono for paths, refs and file contents only.",
        "tokens": {
            "bg": "#0C1E21", "surface": "#11272B", "raised": "#173237",
            "line": "#22424A", "line2": "#335A62",
            "text": "#E7EEEB", "text2": "#A5BBB6", "text3": "#8AA49F",
            "accent": "#EEE8DA", "on-accent": "#1B2321",
            "problem": "#EF6359", "note": "#E9BC3A", "checked": "#63C383", "skipped": "#8AA49F",
            "paper": "#EEE8DA", "ink": "#1B2321", "ink2": "#4F5854", "paperline": "#D3CAB6",
            "p-problem": "#A8261F", "p-note": "#7D5A00", "p-checked": "#256B3B",
        },
        "swatches": [("bg", "container steel"), ("surface", "the consignment"), ("line", "ruling"),
                     ("text", "text"), ("text2", "secondary"), ("text3", "field labels"),
                     ("paper", "paper — the open item, primary"), ("ink", "ink on paper"),
                     ("problem", "Problem stamp"), ("note", "Note placard"), ("checked", "Checked — small"),
                     ("p-problem", "Problem, on paper")],
        "on": "surface",
    },
    {
        "id": "catalogue",
        "name": "Catalogue",
        "thesis": "Matte black and white hairlines. Nothing is coloured until it states something "
                  "— so on this screen one Problem and two Notes are the only colour, and a check "
                  "is drawn as lines whose length is the time each stage took.",
        "world": "A record label’s catalogue sleeve: matte black, a white hairline plot as the "
                 "body ink, small engraved caps, vast unprinted ground, colour only where a code "
                 "is decoded.",
        "why": [
            ("Taste", "Vercel: monochrome, colour only for an error or a warning; Figma: the grid and the type hold the hierarchy"),
            ("Pair 5", "colour is a claim, held back — strictest reading"),
            ("Pair 1", "a duration on every verdict, drawn: the report shows it looked"),
        ],
        "variants": [("Glass", "none — every surface opaque, a dialog sits on a black scrim (D4)"),
                     ("Checked", "A — no colour: a tick in the secondary grey, as quiet as Skipped (D1)"),
                     ("Icons", "Fluent regular, 20")],
        "raises": [],
        "risk": "The closest to the category’s craft standard: black, white and one red is how Vercel already looks. What is ours is the plot and the discipline, not the palette — and a grey screen with one colour can read as unfinished.",
        "guess": "Not from the subject, but from the category: black and white is the dev-tool standard. Kept because the owner named it, and because D1-A and D4 need a real alternative.",
        "style": "regular",
        "checked_icon": "checkmark",
        "fonts": {"display": "Red Hat Display", "body": "Red Hat Text", "mono": "Red Hat Mono"},
        "font_note": "One superfamily in three cuts — Display, Text and its own Mono — neutral and drawn as one system. The caps are small and spaced; the title is the only large type. Red Hat Mono carries durations, paths and refs.",
        "tokens": {
            "bg": "#0A0A0A", "surface": "#0A0A0A", "raised": "#121212",
            "line": "#242424", "line2": "#3A3A3A",
            "text": "#F2F2F2", "text2": "#A8A8A8", "text3": "#858585",
            "accent": "#F2F2F2", "on-accent": "#0A0A0A",
            "problem": "#FF5A45", "note": "#F5C842", "checked": "#A8A8A8", "skipped": "#858585",
        },
        "swatches": [("bg", "matte black"), ("raised", "item panel, sheets"), ("line", "hairline"),
                     ("line2", "hairline, strong"), ("text", "white — body ink, primary"), ("text2", "secondary, Checked"),
                     ("text3", "metadata, Skipped"), ("problem", "Problem — decoded"), ("note", "Note — decoded")],
        "on": "bg",
    },
]

ICON_NAMES = ["puzzle_piece", "bot", "prompt", "plug_connected", "script", "app_generic",
              "error_circle", "info", "prohibited", "checkmark", "circle_small",
              "options", "share", "copy", "arrow_export_ltr", "dismiss", "link", "link_dismiss",
              "arrow_turn_down_right"]
KINDS = [("skill", "puzzle_piece"), ("agent", "bot"), ("prompt", "prompt"), ("mcp", "plug_connected"),
         ("script", "script"), ("app", "app_generic")]


def symbols():
    out = []
    for style in ("regular", "filled"):
        for n in ICON_NAMES:
            svg = (ICONS / f"{n}_20_{style}.svg").read_text(encoding="utf-8")
            inner = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1)
            out.append(f'<symbol id="i-{n}-{style}" viewBox="0 0 20 20">{inner}</symbol>')
    return '<svg width="0" height="0" style="position:absolute" aria-hidden="true">' + "".join(out) + "</svg>"


def ic(d, name, cls=""):
    if name == "circle_small":  # D1-B: Checked is a quiet dot, drawn, not an outline glyph
        return f'<span class="dot {cls}" aria-hidden="true"></span>'
    return (f'<svg class="ic {cls}" aria-hidden="true"><use href="#i-{name}-{d["style"]}"/></svg>')


# ---------------------------------------------------------------- the sample
def mark(d, kind):
    icons = {"problem": "error_circle", "note": "info", "skipped": "prohibited",
             "checked": d["checked_icon"]}
    word = {"problem": "Problem", "note": "Note", "skipped": "Skipped", "checked": "Checked"}[kind]
    return f'<span class="mark m-{kind}">{ic(d, icons[kind])}<span>{word}</span></span>'


def tag(text, state=None, d=None):
    if state:
        icon = {"conflict": "", "auto": "arrow_turn_down_right", "detached": "link_dismiss"}[state]
        return f'<span class="tag st st-{state}">{ic(d, icon) if icon else ""}{text}</span>'
    return f'<span class="tag kind">{text}</span>'


def row(d, name, kind, desc, facts, marks="", states=(), sel=False, sub=""):
    st = "".join(tag(t, s, d) for t, s in states)
    m = "".join(mark(d, k) for k in marks)
    return (f'<li><article class="row{" sel" if sel else ""}"><div class="rmain">'
            f'<h3><span class="nm">{name}</span>{tag(kind)}{st}</h3>'
            f'<p class="desc">{desc}</p><p class="facts">{facts}</p></div>'
            f'<p class="marks">{m}</p></article>{sub}</li>')


def screen(d, drawer=True):
    c = lambda s: f"<code>{s}</code>"
    seed = row(d, "seed-data", "script", "Loads a small, realistic dataset into a fresh database.",
               c("scripts/seed-data.sh"), states=[("Auto-added", "auto")])
    sub_db = f'<ol class="sub">{seed}</ol>'
    db = row(d, "db-migrate", "script",
             "Generates a Postgres migration from a schema diff and runs it — dry run first, then for real.",
             f'{c("scripts/db-migrate.sh")} + 2 files · 1 auto-added', states=[("Auto-added", "auto")], sub=sub_db)
    pg = row(d, "postgres-mcp", "mcp", "Read-only Postgres access for the agent: schema, explain plans, sample rows.",
             f'{c("modelcontextprotocol/servers-archived")} @ {c("9be4674")} · MIT · needs {c("DATABASE_URL")}',
             marks=["note"], states=[("Auto-added", "auto")])
    rows = "".join([
        row(d, "code-style", "skill", "How I want TypeScript written: naming, imports, error handling, no default exports.",
            f'{c(".claude/skills/code-style/SKILL.md")} · defers to <em>the client’s ESLint config</em>', marks=["note"]),
        row(d, "eslint-autofix", "script", "Runs ESLint with --fix on staged files before each commit.",
            f'{c("scripts/eslint-autofix.sh")} · conflicts with {c("code-style")}', marks=["problem"],
            states=[("Conflict", "conflict")], sel=drawer),
        row(d, "migration-reviewer", "agent",
            "Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills.",
            f'requires {c("db-migrate")}, {c("postgres-mcp")} · 3 auto-added', sub=f'<ol class="sub">{db}{pg}</ol>'),
        row(d, "github-mcp", "mcp", "Issues, pull requests and code search on GitHub, through GitHub’s own server.",
            f'{c("github/github-mcp-server")} @ {c("v0.9.0")} · MIT · needs {c("GITHUB_TOKEN")}'),
        row(d, "pr-reviewer", "agent", "Reviews Acme pull requests against their billing rules.",
            "differs from the original in <em>content</em> and <em>lands at</em>", states=[("Detached", "detached")]),
    ])
    aside = ""
    if drawer:
        aside = f'''<aside class="drawer">
  <div class="dhead"><h2>eslint-autofix {tag("script")} {tag("Conflict", "conflict", d)}</h2>
    <span class="btn icon-only" title="Close">{ic(d, "dismiss")}</span></div>
  <p class="desc">Runs ESLint with --fix on staged files before each commit.</p>
  <div class="callout c-problem"><span class="sev">{ic(d, "error_circle")}Problem at last check</span>
    <span>Declares a conflict with {c("code-style")}: it rewrites the imports that {c("code-style")} tells the agent to keep. The archive will contain both, and the agent will get two rules that disagree.</span></div>
  <section class="dsec"><h3>In this project</h3><p>Added by you · linked to the original in My library</p></section>
  <section class="dsec"><h3>Contents</h3>
<pre class="file">#!/usr/bin/env bash
# Fix what ESLint can fix, on staged files only.
files=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\\.(ts|tsx)$')
[ -z "$files" ] &amp;&amp; exit 0
npx eslint --fix $files &amp;&amp; git add $files</pre>
    <p class="meta">No files attached · no repo</p></section>
  <section class="dsec"><h3>Dependencies</h3>
    <dl class="dfacts"><dt>Requires</dt><dd>None</dd><dt>Conflicts with</dt><dd>{c("code-style")}</dd>
    <dt>Env keys</dt><dd>None</dd><dt>Lands at</dt><dd>{c("scripts/eslint-autofix.sh")}</dd></dl></section>
  <section class="dsec"><h3>Use</h3><p>Used in 2 projects · last exported 2 days ago</p></section>
  <div class="dact"><span class="btn">Open in My library</span><span class="btn">Configure to remove</span></div>
</aside>'''
    return f'''<div class="app">
<header class="apphead"><span class="product"><span class="logo"></span>AI Stack Builder</span>
  <nav><a>My library</a><a>Public library</a><a class="on">Projects</a></nav>
  <span class="account"><img src="{PORTRAIT}" alt="" width="24" height="24"><span>Maya Chen</span></span></header>
<main class="appmain">
  <p class="crumb">Projects /</p>
  <div class="phead"><div><h1>acme-billing-api</h1>
    <p class="hmeta"><span>14 items · 3 auto-added · 1 detached</span><span class="verdict">{ic(d, d["checked_icon"], "vdot")}Checked 2 days ago · for Claude Code · <b class="t-problem">1 problem</b> · <b class="t-note">2 notes</b> · 1 skipped</span></p></div>
    <div class="hact"><span class="btn">{ic(d, "options")}Configure</span><span class="btn">{ic(d, "share")}Share…</span><span class="btn">{ic(d, "copy")}Duplicate</span><span class="btn primary">{ic(d, "arrow_export_ltr")}Export…</span></div></div>
  <p class="pdesc">Client repo for Acme’s billing service. Code style, migration and review agents, the Postgres and GitHub MCP servers.</p>
  <div class="split{" with" if drawer else ""}"><ol class="rows">{rows}</ol>{aside}</div>
</main></div>'''


def stage(d, n, name, kind, result, t, body="", open_=False, w=0):
    plot = f'<span class="plot"><i style="width:{w}%"></i></span>' if d["id"] == "catalogue" else ""
    return (f'<li class="stage s-{kind}{" open" if open_ else ""}"><div class="sum"><span class="n">{n}</span>'
            f'<span class="sname">{name}</span><span class="res">'
            f'{ic(d, {"problem": "error_circle", "note": "info", "skipped": "prohibited", "checked": d["checked_icon"]}[kind], "g-" + kind)}'
            f'<span>{result}</span></span>{plot}<span class="time">{t}</span></div>{body}</li>')


def run_overlay(d, dialog=True):
    c = lambda s: f"<code>{s}</code>"
    problem_body = (f'<div class="sbody"><div class="callout c-problem"><span class="sev">{ic(d, "error_circle")}Problem</span>'
                    f'<span>{c("eslint-autofix")} declares a conflict with {c("code-style")}: it rewrites the imports that '
                    f'{c("code-style")} tells the agent to keep. The archive will contain both, and the agent will get two rules that disagree.</span>'
                    f'<span class="btn">Remove eslint-autofix…</span></div></div>')
    stages = "".join([
        stage(d, "02", "Declared conflicts", "problem", "1 problem", "0.1 s", problem_body, True, 25),
        stage(d, "03", "Command names", "skipped", "Skipped — no item declares a command", "—", w=0),
        stage(d, "04", "Target paths", "checked", "Checked — no two items write to the same path", "0.2 s", w=50),
        stage(d, "05", "Env keys", "note", "1 note · 3 keys named", "0.1 s", w=25),
    ])
    dlg = ""
    if dialog:
        dlg = ('<div class="dscrim"></div>'
               '<div class="dlg" role="dialog" aria-label="Remove eslint-autofix from acme-billing-api?"><div class="sheet">'
               '<h2>Remove eslint-autofix from acme-billing-api?</h2>'
               '<p>It leaves this project only. It stays in My library and in the other projects that use it.</p>'
               '<p class="meta">The check runs again as soon as it is removed.</p>'
               '<div class="dact"><span class="btn">Cancel</span><span class="btn primary">Remove from project</span></div>'
               '</div></div>')
    return f'''<div class="overlay-demo">
  {screen(d, drawer=False)}
  <div class="scrim"></div>
  <div class="runframe"><div class="runinner">
    <div class="runhead"><div><h2>Checked just now</h2><p class="counts"><b class="t-problem">1 problem</b> · <b class="t-note">2 notes</b> · 1 skipped</p>
      <p class="meta">acme-billing-api · 14 items · for Claude Code · 1.8 s</p></div>
      <span class="btn icon-only" title="Close">{ic(d, "dismiss")}</span></div>
    <h3 class="group">Findings</h3>
    <ol class="stages">{stages}</ol>
  </div></div>
  {dlg}
</div>'''


# ---------------------------------------------------------------- the fixed set
def fixed_set(d):
    t = d["tokens"]
    on = t[d["on"]]
    sw = []
    for key, role in d["swatches"]:
        hexv = t[key]
        base = t["paper"] if key.startswith("p-") or key == "ink" else on
        r = ratio(hexv, base)
        against = "on paper" if base != on else ("on ground" if d["on"] == "bg" else "on surface")
        show_r = key not in ("bg", "surface", "raised", "line", "line2", "paper") or key == "paper"
        rr = f'<span class="cr">{r:.1f}:1 {against}</span>' if show_r and hexv != base else '<span class="cr">&nbsp;</span>'
        sw.append(f'<li><span class="chip" style="background:{hexv}"></span><span class="hex">{hexv}</span>'
                  f'<span class="role">{role}</span>{rr}</li>')
    f = d["fonts"]
    kinds = "".join(f'<li>{ic(d, n)}<span>{k}</span></li>' for k, n in KINDS)
    sev = "".join(f'<li>{mark(d, k)}</li>' for k in ("problem", "note", "skipped", "checked"))
    acts = "".join(f'<li>{ic(d, n)}<span>{w}</span></li>' for w, n in
                   [("Configure", "options"), ("Share…", "share"), ("Duplicate", "copy"), ("Export…", "arrow_export_ltr"),
                    ("linked", "link"), ("Detached", "link_dismiss"), ("Auto-added", "arrow_turn_down_right"), ("Close", "dismiss")])
    return f'''<div class="fixed">
  <div class="fx-pal"><h3 class="lab">Palette</h3><ul class="swatches">{"".join(sw)}</ul></div>
  <div class="fx-type"><h3 class="lab">Type</h3>
  <div class="type">
    <p class="t-display">acme-billing-api</p>
    <p class="t-body">Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills.</p>
    <p class="t-mono">modelcontextprotocol/servers-archived @ 9be4674 · 0.3 s</p>
    <p class="t-names"><b>{f["display"]}</b> · <b>{f["body"]}</b> · <b>{f["mono"]}</b></p>
    <p class="fnote">{d["font_note"]}</p>
  </div></div>
  <div class="fx-parts"><h3 class="lab">Icons · Fluent {d["style"]}</h3>
  <ul class="icons">{kinds}</ul>
  <ul class="icons">{acts}</ul>
  <h3 class="lab">Buttons</h3>
  <div class="btnrow"><span class="btn primary">{ic(d, "arrow_export_ltr")}Export…</span><span class="btn">{ic(d, "options")}Configure</span><span class="btn">Cancel</span></div>
  <h3 class="lab">Severity marks</h3><ul class="sevs">{sev}</ul></div>
</div>'''


def column(d, n):
    d = dict(d, n=n)
    t = d["tokens"]
    vars_ = ";".join(f"--{k}:{v}" for k, v in t.items())
    vars_ += f';--font:"{d["fonts"]["body"]}",system-ui,sans-serif;--font-display:"{d["fonts"]["display"]}",system-ui,sans-serif;--font-mono:"{d["fonts"]["mono"]}",ui-monospace,monospace'
    why = "".join(f"<li><b>{a}</b> {b}</li>" for a, b in d["why"])
    var = "".join(f"<li><b>{a}</b> {b}</li>" for a, b in d["variants"])
    raises = ""
    if d["raises"]:
        raises = ('<details class="raises"><summary>Kept from the challengers this direction was weighed against</summary><ul>'
                  + "".join(f"<li>{r}</li>" for r in d["raises"]) + "</ul></details>")
    return f'''<section class="dir d-{d["id"]}" style='{vars_}' aria-labelledby="h-{d["id"]}">
  <header class="dirhead"><div class="dh-main">
    <p class="dnum">Direction {d["n"]} of 3</p>
    <h2 id="h-{d["id"]}">{d["name"]}</h2>
    <p class="thesis">{d["thesis"]}</p>
    <p class="world">{d["world"]}</p></div><div class="dh-side">
    <ul class="why">{why}</ul>
    <ul class="variants">{var}</ul>
    <p class="guess"><b>Guessable from the subject?</b> {d["guess"]}</p>
    <p class="risk"><b>Honest risk.</b> {d["risk"]}</p>
    {raises}
  </div></header>
  {fixed_set(d)}
  <h3 class="lab samplehead">The sample — acme-billing-api, eslint-autofix open</h3>
  <div class="scale"><div class="native">{screen(d)}</div></div>
  <h3 class="lab samplehead">Export, over the project — the stage strip</h3>
  <div class="scale"><div class="native">{run_overlay(d, dialog=False)}</div></div>
  <h3 class="lab samplehead">The remove dialog, over Export</h3>
  <div class="scale"><div class="native">{run_overlay(d)}</div></div>
</section>'''


CSS = r"""
:root{--page:#262626;--page-2:#2f2f2f;--page-ink:#e8e8e8;--page-ink-2:#b4b4b4;--page-line:#3d3d3d}
*{box-sizing:border-box}
html{background:var(--page)}
body{margin:0;background:var(--page);color:var(--page-ink);font:15px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}
.pagehead{max-width:1440px;margin:0 auto;padding:48px 24px 0}
.pagehead h1{font-size:40px;line-height:1.15;margin:0 0 10px;font-weight:600;letter-spacing:-.01em}
.pagehead p{margin:0 0 12px;color:var(--page-ink-2);max-width:90ch;font-size:17px}
.pagehead p b{color:var(--page-ink);font-weight:600}
.jump{position:sticky;top:0;z-index:5;display:flex;gap:6px;margin:22px -24px 0;padding:12px 24px;background:var(--page);border-bottom:1px solid var(--page-line)}
.jump a{font-size:15px;font-weight:600;color:var(--page-ink);text-decoration:none;padding:8px 14px;border-radius:6px;border:1px solid var(--page-line);background:var(--page-2)}
.jump a:hover{border-color:var(--page-ink-2)}
.jump a:focus-visible{outline:2px solid var(--page-ink);outline-offset:2px}
.grid{display:flex;flex-direction:column;gap:56px;max-width:1440px;margin:0 auto;padding:24px 24px 72px}
.pagefoot{max-width:1440px;margin:0 auto;padding:0 24px 48px;color:var(--page-ink-2);font-size:14px}
.dirhead h2{scroll-margin-top:90px}

/* ---------- a direction column: everything inside reads its own tokens ---------- */
.dir{background:var(--bg);color:var(--text);font-family:var(--font);border-radius:12px;padding:44px 48px 52px;min-width:0;overflow:hidden}
.dir code,.dir pre,.dir .t-mono{font-family:var(--font-mono)}
.dir .lab{font:600 13px/1.2 var(--font);letter-spacing:.08em;text-transform:uppercase;color:var(--text3);margin:0 0 14px}
.dir h4{font:600 11px/1.2 var(--font);letter-spacing:.08em;text-transform:uppercase;color:var(--text3)}
.dirhead{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:48px;margin-bottom:44px}
.dnum{margin:0 0 6px;font-size:14px;color:var(--text3)}
.dirhead h2{font-family:var(--font-display);font-size:56px;line-height:1.05;margin:0 0 18px;font-weight:600;letter-spacing:-.01em}
.thesis{font-size:21px;line-height:1.45;margin:0 0 14px;color:var(--text)}
.world{font-size:15.5px;color:var(--text2);margin:0 0 12px}
.why,.variants{list-style:none;margin:0 0 14px;padding:0;font-size:15px;color:var(--text2)}
.why li,.variants li{margin:0 0 7px}
.why b,.variants b{color:var(--text);font-weight:600;margin-right:4px}
.variants{border-top:1px solid var(--line);padding-top:14px}
.guess,.risk{font-size:15px;color:var(--text2);margin:0 0 8px}
.guess b,.risk b{color:var(--text)}
.raises{font-size:14.5px;color:var(--text2);margin:6px 0 0}
.raises summary{cursor:pointer;color:var(--text)}
.raises ul{padding-left:18px;margin:8px 0 0}
.raises li{margin:0 0 6px}

.fixed{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr) minmax(0,1fr);gap:44px;padding:36px 0 8px;border-top:1px solid var(--line)}
.fx-parts .lab:not(:first-child){margin-top:28px}
.swatches{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:14px 12px}
.swatches li{display:grid;grid-template-columns:44px 1fr;column-gap:12px;font-size:14px;line-height:1.35}
.swatches .chip{grid-row:1/4;width:44px;height:58px;border-radius:4px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.14)}
.swatches .hex{font-family:var(--font-mono);color:var(--text)}
.swatches .role{color:var(--text2)}
.swatches .cr{color:var(--text3);font-variant-numeric:tabular-nums}
.type p{margin:0 0 8px}
.t-display{font-family:var(--font-display);font-size:40px;line-height:1.15;font-weight:600;letter-spacing:-.01em}
.t-body{font-size:17px;color:var(--text)}
.t-mono{font-size:14px;color:var(--text2)}
.t-names{font-size:15px;color:var(--text2)}
.t-names b{color:var(--text);font-weight:600}
.fnote{font-size:14px;color:var(--text3)}
.icons{list-style:none;padding:0;margin:0 0 12px;display:flex;flex-wrap:wrap;gap:10px 18px}
.icons li{display:flex;align-items:center;gap:8px;font-size:15px;color:var(--text2)}
.icons .ic{color:var(--text);width:20px;height:20px}
.fixed .btn{height:40px;padding:0 16px;font-size:15px}
.fixed .btn .ic{width:18px;height:18px}
.fixed .mark{font-size:16px}
.fixed .mark .ic{width:20px;height:20px}
.fixed .dot{width:9px;height:9px}
.sevs{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:8px 18px}
.btnrow{display:flex;flex-wrap:wrap;gap:8px}
.samplehead{margin:48px 0 16px!important;font-size:15px!important}

.ic{width:16px;height:16px;fill:currentColor;flex:none}
.dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:currentColor;margin:0 4px 0 4px;flex:none}
.scale{width:100%;overflow:hidden;border-radius:8px;box-shadow:0 0 0 1px var(--line2)}
.native{width:1120px;transform-origin:0 0}

/* ---------- the app, shared structure ---------- */
.app{background:var(--bg);color:var(--text);font-size:14px;line-height:1.45}
.apphead{display:flex;align-items:center;gap:28px;height:48px;padding:0 20px;border-bottom:1px solid var(--line)}
.product{display:flex;align-items:center;gap:8px;font-weight:600;font-size:14px}
.logo{width:14px;height:14px;border-radius:3px;background:var(--text)}
.apphead nav{display:flex;gap:4px}
.apphead nav a{padding:6px 10px;border-radius:var(--r-s,4px);color:var(--text2);font-size:13.5px}
.apphead nav a.on{color:var(--text);background:var(--raised)}
.account{margin-left:auto;display:flex;align-items:center;gap:8px;font-size:13px;color:var(--text2)}
.account img{width:24px;height:24px;border-radius:50%;object-fit:cover}
.appmain{padding:18px 24px 28px}
.crumb{margin:0 0 6px;font-size:13px;color:var(--text3)}
.phead{display:flex;justify-content:space-between;align-items:flex-start;gap:20px}
.phead h1{font-family:var(--font-display);font-size:26px;line-height:1.15;margin:0 0 8px;font-weight:600;letter-spacing:-.01em}
.hmeta{margin:0;display:flex;flex-direction:column;gap:2px;font-size:13px;color:var(--text2);font-variant-numeric:tabular-nums}
.verdict{display:flex;align-items:center;gap:6px}
.verdict .vdot{color:var(--checked)}
.t-problem{color:var(--problem);font-weight:600}
.t-note{color:var(--note);font-weight:600}
.hact{display:flex;gap:8px;flex:none}
.pdesc{margin:14px 0 16px;color:var(--text2);font-size:13.5px;max-width:80ch}

.btn{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px;border-radius:var(--r-s,4px);border:1px solid var(--line2);background:var(--surface);color:var(--text);font-size:13px;font-weight:500;white-space:nowrap}
.btn.primary{background:var(--accent);color:var(--on-accent);border-color:var(--accent);font-weight:600}
.btn.icon-only{width:32px;padding:0;justify-content:center}

.split{display:block}
.split.with{display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:16px;align-items:start}
.rows,.sub{list-style:none;margin:0;padding:0}
.rows{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-m,8px)}
.rows>li+li{border-top:1px solid var(--line)}
.sub{margin-left:28px;border-left:1px solid var(--line2)}
.sub>li{border-top:1px solid var(--line)}
.row{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:16px;padding:10px 14px}
.row h3{display:flex;align-items:center;gap:8px;margin:0 0 2px;font-size:14px;font-weight:600}
.desc{margin:0 0 2px;color:var(--text2);font-size:13px}
.facts{margin:0;color:var(--text3);font-size:12px}
.facts code,.dir .file,.dfacts code,.callout code,.sbody code{font-size:.92em}
.facts em{font-style:normal;color:var(--text2)}
.marks{margin:0;display:flex;gap:10px;align-items:flex-start;padding-top:1px}
.tag{display:inline-flex;align-items:center;gap:4px;font-size:11.5px;font-weight:500;color:var(--text2)}
.tag .ic{width:12px;height:12px}
.st-conflict{color:var(--problem)}
.mark{display:inline-flex;align-items:center;gap:5px;font-size:12.5px;font-weight:600}
.m-problem{color:var(--problem)} .m-note{color:var(--note)} .m-skipped{color:var(--skipped);font-weight:500} .m-checked{color:var(--checked);font-weight:500}

.drawer{background:var(--raised);border:1px solid var(--line);border-radius:var(--r-m,8px);padding:16px}
.dhead{display:flex;justify-content:space-between;gap:10px;align-items:flex-start}
.dhead h2{margin:0 0 6px;font-size:17px;display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-family:var(--font-display);font-weight:600}
.drawer .desc{margin-bottom:12px}
.callout{display:flex;flex-direction:column;gap:6px;padding:10px 12px;border-radius:var(--r-s,4px);font-size:13px;border:1px solid var(--line2);background:var(--surface)}
.callout .sev{display:flex;align-items:center;gap:6px;font-weight:600;color:var(--problem)}
.callout .btn{align-self:flex-start;margin-top:4px}
.dsec{margin-top:14px}
.dsec h3{font:600 11px/1.2 var(--font);letter-spacing:.08em;text-transform:uppercase;color:var(--text3);margin:0 0 6px}
.dsec p{margin:0;font-size:13px;color:var(--text2)}
.file{margin:0 0 6px;padding:10px 12px;background:var(--bg);border:1px solid var(--line);border-radius:var(--r-s,4px);font-size:11.5px;line-height:1.55;white-space:pre-wrap;overflow-wrap:anywhere;color:var(--text)}
.meta{font-size:12px;color:var(--text3)!important}
.dfacts{display:grid;grid-template-columns:120px 1fr;gap:4px 10px;margin:0;font-size:13px}
.dfacts dt{color:var(--text3)} .dfacts dd{margin:0}
.dact{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap}

/* ---------- Export over the project ---------- */
.overlay-demo{position:relative;height:560px;overflow:hidden}
.scrim,.dscrim{position:absolute;inset:0}
.runframe{position:absolute;inset:56px 80px 0}
.runinner{height:100%;background:var(--bg);border:1px solid var(--line2);border-radius:var(--r-m,8px) var(--r-m,8px) 0 0;padding:20px 24px;overflow:hidden}
.runhead{display:flex;justify-content:space-between;align-items:flex-start}
.runhead h2{font-family:var(--font-display);font-size:24px;margin:0 0 4px;font-weight:600}
.counts{margin:0 0 2px;font-size:14px;font-variant-numeric:tabular-nums}
.group{font:600 11px/1 var(--font);letter-spacing:.08em;text-transform:uppercase;color:var(--text3);margin:20px 0 8px}
.stages{list-style:none;margin:0;padding:0;border:1px solid var(--line);border-radius:var(--r-m,8px);background:var(--surface)}
.stage+.stage{border-top:1px solid var(--line)}
.sum{display:grid;grid-template-columns:28px 180px minmax(0,1fr) 56px;gap:12px;align-items:center;padding:10px 14px;font-size:13.5px}
.d-catalogue .sum{grid-template-columns:28px 170px minmax(0,1fr) 120px 56px}
.n{color:var(--text3);font-variant-numeric:tabular-nums;font-size:12px}
.sname{font-weight:600}
.res{display:flex;align-items:center;gap:8px;color:var(--text2)}
.g-problem{color:var(--problem)} .g-note{color:var(--note)} .g-skipped{color:var(--skipped)} .g-checked{color:var(--checked)}
.s-problem .res span{color:var(--problem);font-weight:600}
.s-note .res span{color:var(--note);font-weight:600}
.time{text-align:right;font-family:var(--font-mono);font-size:12px;color:var(--text2);font-variant-numeric:tabular-nums}
.sbody{padding:0 14px 14px 54px}
.dlg{position:absolute;left:50%;top:250px;transform:translateX(-50%);width:460px}
.sheet{background:var(--raised);border:1px solid var(--line2);border-radius:var(--r-m,8px);padding:20px}
.sheet h2{font-family:var(--font-display);font-size:18px;margin:0 0 10px;font-weight:600}
.sheet p{margin:0 0 8px;font-size:13.5px;color:var(--text2)}
.sheet .dact{justify-content:flex-end}

/* ================= Acrylic ================= */
.d-acrylic{--r-s:4px;--r-m:8px}
.d-acrylic .tag.kind{padding:1px 7px;border-radius:4px;background:rgba(255,255,255,.07)}
.d-acrylic .row.sel{background:#262A31;box-shadow:inset 0 0 0 1px var(--accent);border-radius:4px}
.d-acrylic .apphead{background:#0F1115}
.d-acrylic .apphead nav a.on{background:#252A31;box-shadow:inset 0 -2px 0 var(--accent)}
.d-acrylic .btn{border-color:transparent;background:#262A31}
.d-acrylic .btn.primary{background:var(--accent);border-color:var(--accent)}
/* acrylic: only the frame is glass; what is read sits on an opaque sheet */
.d-acrylic .scrim{background:rgba(8,9,12,.25)}
.d-acrylic .runframe{inset:44px 64px 0;padding:10px 10px 0;border-radius:14px 14px 0 0;
  background:rgba(48,54,66,.42);backdrop-filter:blur(28px) saturate(160%);-webkit-backdrop-filter:blur(28px) saturate(160%);
  border:1px solid rgba(255,255,255,.14);border-bottom:0}
.d-acrylic .runinner{border-color:rgba(255,255,255,.06)}
.d-acrylic .dscrim{background:rgba(8,9,12,.30)}
.d-acrylic .dlg{padding:10px;border-radius:14px;background:rgba(58,64,78,.45);
  backdrop-filter:blur(26px) saturate(160%);-webkit-backdrop-filter:blur(26px) saturate(160%);border:1px solid rgba(255,255,255,.16);
  box-shadow:0 18px 48px rgba(0,0,0,.45)}
.d-acrylic .sheet{border-color:rgba(255,255,255,.06)}
.d-acrylic .callout.c-problem{border-color:rgba(244,124,132,.35);background:rgba(244,124,132,.07)}

/* ================= Manifest ================= */
.d-manifest{--r-s:2px;--r-m:2px;font-stretch:100%}
.d-manifest .dirhead h2,.d-manifest .phead h1,.d-manifest .t-display,.d-manifest .runhead h2{font-stretch:112%;font-weight:700;letter-spacing:-.005em}
.d-manifest h4,.d-manifest .lab,.d-manifest .group,.d-manifest .dfacts dt{font-stretch:75%;letter-spacing:.1em}
.d-manifest .tag.kind{font-stretch:75%;text-transform:uppercase;letter-spacing:.08em;font-size:11px;font-weight:600;border:1px solid var(--line2);padding:0 5px;border-radius:2px;color:var(--text2)}
.d-manifest .tag.st{font-stretch:87%}
.d-manifest .apphead{background:#081517;border-bottom-color:var(--line2)}
.d-manifest .logo{border-radius:0;background:var(--paper)}
.d-manifest .apphead nav a{border-radius:0}
.d-manifest .apphead nav a.on{background:transparent;color:var(--paper);box-shadow:inset 0 -2px 0 var(--paper)}
.d-manifest .account img{border-radius:2px}
.d-manifest .rows{border-color:var(--line2)}
.d-manifest .row{grid-template-columns:minmax(0,1fr) 110px}
.d-manifest .marks{border-left:1px solid var(--line);padding-left:12px;align-self:stretch}
.d-manifest .row.sel{background:#1A3A40;box-shadow:inset 0 0 0 1px var(--paper)}
.d-manifest .btn{border-color:var(--line2);background:transparent}
.d-manifest .btn.primary{background:var(--paper);color:var(--ink);border-color:var(--paper)}
.d-manifest .verdict .vdot{width:12px;height:12px}
/* the open item is the paper declaration */
.d-manifest .drawer{background:var(--paper);color:var(--ink);border:0;
  --text:var(--ink);--text2:var(--ink2);--text3:#5F665F;--line:var(--paperline);--line2:#BDB39C;--surface:#E6DFCF;--bg:#E2DAC8;
  --problem:var(--p-problem);--note:var(--p-note);--checked:var(--p-checked)}
.d-manifest .drawer .btn{border-color:var(--ink2);color:var(--ink)}
.d-manifest .drawer .dsec{border-top:1px solid var(--paperline);padding-top:10px}
.d-manifest .drawer .dfacts{grid-template-columns:120px 1fr}
.d-manifest .drawer .dfacts dt,.d-manifest .drawer .dfacts dd{border-bottom:1px solid var(--paperline);padding:3px 0}
.d-manifest .drawer .tag.kind{border-color:var(--ink2);color:var(--ink2)}
.d-manifest .callout{border-width:1px 1px 1px 1px}
.d-manifest .drawer .callout.c-problem{border-color:var(--p-problem);background:#F3DED6}
/* glass only as the scrim: the place behind is frosted, the sheets are opaque */
.d-manifest .scrim{background:rgba(6,18,20,.45);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.d-manifest .runinner{border-color:var(--line2)}
.d-manifest .dscrim{background:rgba(6,18,20,.40);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
.d-manifest .sheet{background:var(--paper);color:var(--ink);border:0;--text2:var(--ink2);--text3:#5F665F;--line2:var(--ink2)}
.d-manifest .sheet .btn{border-color:var(--ink2);color:var(--ink)}
.d-manifest .sheet .btn.primary{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.d-manifest .callout.c-problem{border-color:rgba(239,99,89,.55)}
.d-manifest .swatches .chip{border-radius:2px}

/* ================= Catalogue ================= */
.d-catalogue{--r-s:0;--r-m:0}
.d-catalogue .dirhead h2,.d-catalogue .phead h1,.d-catalogue .t-display,.d-catalogue .runhead h2{font-weight:500;letter-spacing:-.025em}
.d-catalogue h4,.d-catalogue .lab,.d-catalogue .group{font-family:var(--font-mono);font-weight:500;letter-spacing:.14em;font-size:11px}
.d-catalogue .tag.kind{font-family:var(--font-mono);font-size:11px;color:var(--text3);font-weight:400}
.d-catalogue .logo{border-radius:0;width:10px;height:10px}
.d-catalogue .apphead nav a.on{background:transparent;box-shadow:inset 0 -1px 0 var(--text)}
.d-catalogue .account img{border-radius:0;filter:grayscale(1)}
.d-catalogue .rows{border-width:1px 0;border-color:var(--line2);background:transparent}
.d-catalogue .row.sel{box-shadow:inset 0 2px 0 var(--text),inset 0 -2px 0 var(--text)}
.d-catalogue .btn{background:transparent;border-color:var(--line2)}
.d-catalogue .btn.primary{background:var(--text);color:var(--bg);border-color:var(--text)}
.d-catalogue .drawer{background:var(--bg);border-width:0 0 0 1px;border-color:var(--line2);padding:4px 0 0 18px}
.d-catalogue .callout{background:transparent;border-color:var(--problem)}
.d-catalogue .file{background:var(--raised)}
.d-catalogue .stages{border-width:1px 0;background:transparent}
.d-catalogue .plot{display:block;height:12px;position:relative}
.d-catalogue .plot i{position:absolute;left:0;top:5px;height:1px;background:var(--text)}
.d-catalogue .s-problem .plot i{background:var(--problem);height:2px;top:5px}
.d-catalogue .s-note .plot i{background:var(--note)}
.d-catalogue .s-skipped .plot i{display:none}
.d-catalogue .scrim{background:rgba(0,0,0,.72)}
.d-catalogue .runinner{border-width:1px 1px 0}
.d-catalogue .dscrim{background:rgba(0,0,0,.6)}
.d-catalogue .sheet{background:var(--raised)}
.d-catalogue .swatches .chip{border-radius:0}

@media (max-width:1100px){.dirhead,.fixed{grid-template-columns:minmax(0,1fr);gap:28px}.dir{padding:28px 20px 32px}.dirhead h2{font-size:40px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
"""

JS = r"""
(function(){
  function fit(){
    document.querySelectorAll('.scale').forEach(function(s){
      var n=s.firstElementChild, k=s.clientWidth/1120;
      n.style.transform='scale('+k+')';
      s.style.height=(n.offsetHeight*k)+'px';
    });
  }
  window.addEventListener('resize', fit);
  if(document.fonts&&document.fonts.ready){document.fonts.ready.then(fit);}
  window.addEventListener('load', fit); fit();
})();
"""

FONTS = ("https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..700"
         "&family=Martian+Mono:wght@400;500&family=Red+Hat+Display:wght@500;600&family=Red+Hat+Text:wght@400;500;600&family=Red+Hat+Mono:wght@400;500"
         "&family=Cascadia+Code:wght@400&display=swap")


def build():
    cols = "".join(column(d, i + 1) for i, d in enumerate(DIRS))
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Three directions · AI Stack Builder</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<style>{CSS}</style>
</head>
<body>
{symbols()}
<header class="pagehead">
  <h1>Three directions for AI Stack Builder</h1>
  <p>Phase 06, stage 3. <b>All three are dark-first</b> (CLAUDE.md §3), and they differ on the other three axes at once: <b>how much colour</b> (Catalogue almost none, Acrylic a tinted ground and one accent, Manifest a committed ground and a paper surface), <b>the character of the type</b> (Segoe’s humanist, Archivo’s widths, Red Hat’s neutral grotesk) and <b>the form</b> (4 / 8 px and acrylic, 2 px and ruling, 0 px and hairlines).</p>
  <p><b>The sample is fixed</b> (README, stage 3): the Project screen with <code>eslint-autofix</code> open, then the Export mode over the project with the remove dialog over it. Every word is from <code>project-item.html</code>, <code>run-remove.html</code> and <code>microcopy.md</code>, unchanged. Between them the three cover D1 (A, B and C for <i>Checked</i>) and D2–D4 (glass at the frame, glass as the scrim, no glass).</p>
  <p><b>This grey page is not part of any direction.</b> Each direction is one block, top to bottom: what it is, its palette, type, icons and parts, then the sample at full width. Ratios on the swatches are WCAG contrast against the direction’s own ground, computed when the page is built.</p>
  <nav class="jump" aria-label="Directions"><a href="#h-acrylic">1 · Acrylic</a><a href="#h-manifest">2 · Manifest</a><a href="#h-catalogue">3 · Catalogue</a></nav>
</header>
<main class="grid">{cols}</main>
<p class="pagefoot">Built by <code>tools/build_directions.py</code>. Icons: Microsoft Fluent System Icons, MIT, @fluentui/svg-icons 1.1.344. Portrait: Jake Nackos on Unsplash (unsplash.com/photos/IF9TK5Uy-KI), standing in for the signed-in person.</p>
<script>{JS}</script>
</body>
</html>'''
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}  {len(html)//1024} KB")
    for d in DIRS:
        t = d["tokens"]
        on = t[d["on"]]
        low = [(k, round(ratio(t[k], on), 2)) for k in ("text", "text2", "text3", "accent", "problem", "note", "checked")
               if ratio(t[k], on) < 4.5]
        print(d["name"], "below 4.5:", low or "none")


if __name__ == "__main__":
    build()
