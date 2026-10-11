"""Phase 06, stage 3, round 2: build 06-concept/directions-2.html — three new directions.

The owner turned down round 1 (Acrylic, Manifest, Catalogue) on 2026-10-11 and asked for three
entirely new directions, free to depart from the wireframes' layout: the wireframes are a
structure, not the look. The content is still the product's own: every word is from
project-item.html, run-default.html, run-remove.html and microcopy.md.

    python tools/build_directions_2.py   -> 06-concept/directions-2.html

Shares the icon, contrast and portrait helpers with tools/build_directions.py.
"""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("bd1", ROOT / "tools" / "build_directions.py")
bd1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bd1)
bd1.ICON_NAMES += ["library", "globe", "folder", "key", "chevron_down", "chevron_right", "clock"]
ratio, PORTRAIT, KINDS = bd1.ratio, bd1.PORTRAIT, bd1.KINDS
OUT = ROOT / "06-concept" / "directions-2.html"

DIRS = [
    {
        "id": "glasshouse", "name": "Glasshouse",
        "thesis": "A palm house at night. The work grows on a deep bottle-green ground; what you "
                  "enter — the Export mode, a dialog — is a pane of glass in a thin brass frame, "
                  "and the dependencies that pulled an item in are drawn as the stem it hangs from.",
        "world": "Victorian glasshouses: wrought-iron glazing bars, bottle-green glass, brass fittings, "
                 "the serif of a botanical label beside plain working type.",
        "why": [
            ("Taste", "Teams / Slack glass, noticeable but sparing — here it is literally framed, never under text"),
            ("Pair 4", "glass is a layer over the work: the set and the item panel are opaque, only modes are panes"),
            ("Research", "“serif for ideas, sans for the product” — Linear’s own method page (refs/README)"),
            ("Pair 5", "a green ground makes green mean nothing, so no green tick can claim <i>works</i>"),
        ],
        "variants": [("Layout", "a left rail for the three places; the set without boxes; auto-added items hang on a curved stem"),
                     ("Glass", "frame only: a brass-framed pane, the findings on an opaque sheet inside it (D2, D3)"),
                     ("Checked", "A — no colour; on a green ground green cannot be the verdict (D1)"),
                     ("Icons", "Fluent regular, 20")],
        "risk": "The most atmospheric of the three. A whole green product is a commitment people either keep or tire of, and the serif title has to stay on titles — on a row it would read as decoration.",
        "guess": "Not from the subject: nothing about AI tools says bottle green and brass.",
        "style": "regular", "checked_icon": "checkmark",
        "fonts": {"display": "Young Serif", "body": "Hanken Grotesk", "mono": "JetBrains Mono"},
        "font_note": "Young Serif only for titles: the project, the verdict, a dialog’s question. Hanken Grotesk for everything a person works with. JetBrains Mono for paths, refs and file contents.",
        "tokens": {"bg": "#0E1A15", "surface": "#13241D", "raised": "#1A2F26", "rail": "#0A1410",
                   "line": "#24392F", "line2": "#335045", "text": "#E8EFE9", "text2": "#A9BDB1", "text3": "#889B90",
                   "accent": "#CFE3D8", "on-accent": "#0E1A15", "brass": "#B8955A",
                   "problem": "#F2806F", "note": "#EDC14F", "checked": "#A9BDB1", "skipped": "#889B90"},
        "swatches": [("bg", "bottle-green ground"), ("surface", "the bench — the set"), ("raised", "item panel"),
                     ("line", "hairline"), ("text", "text"), ("text2", "secondary, Checked"), ("text3", "metadata, Skipped"),
                     ("accent", "pale glass — primary"), ("brass", "brass — glazing bars, selection"),
                     ("problem", "Problem"), ("note", "Note")],
        "on": "surface",
    },
    {
        "id": "kit", "name": "Kit",
        "thesis": "The drawer of a well-kept tool chest. Every item sits in its own soft cut-out in "
                  "dark foam, and the foam has a coloured layer underneath: colour only shows where "
                  "something is wrong or missing. A step that had nothing to check is an empty cut-out.",
        "world": "Two-tone shadow foam in a mechanic’s drawer: a black top layer, red or yellow beneath, "
                 "rounded outlines cut to the shape of each tool, steel on top.",
        "why": [
            ("Research", "the practitioner keeps it in a folder called ~/dev/kit — “40-something files” (interviews.md:376-378)"),
            ("EJ-3", "“maybe half of it” does nothing: a drawer shows at a glance what is used and what is missing"),
            ("Pair 5", "colour is a claim — here it is literally underneath, and only shows through a gap"),
            ("Pair 2", "density held by the outlines and the type, not by colour or cards"),
        ],
        "variants": [("Layout", "a top bar; each item in a rounded well; auto-added items sit inside their parent’s well"),
                     ("Glass", "none — foam and steel are opaque, the dialog is a lid with a real shadow (D4)"),
                     ("Checked", "B — a quiet steel dot, not green (D1)"),
                     ("Icons", "Fluent filled, 20")],
        "risk": "Inset wells are a physical metaphor; pushed too far they become skeuomorphic. The wells must stay quiet enough that fifty of them still read as a list.",
        "guess": "Not from the subject: charcoal foam and steel belong to a workshop, not to AI.",
        "style": "filled", "checked_icon": "circle_small",
        "fonts": {"display": "Rubik", "body": "Rubik", "mono": "Fira Code"},
        "font_note": "Rubik’s slightly rounded corners match the cut-outs: one family, weight carries the rank. Fira Code for paths, refs and file contents.",
        "tokens": {"bg": "#121314", "surface": "#1B1C1E", "well": "#0F1011", "raised": "#222326",
                   "line": "#2A2C2F", "line2": "#3A3D41", "text": "#ECEDEE", "text2": "#A7ABB0", "text3": "#878B91",
                   "accent": "#E3E5E8", "on-accent": "#121314",
                   "problem": "#FF5F57", "note": "#F5C451", "checked": "#9FB4C7", "skipped": "#878B91"},
        "swatches": [("bg", "the drawer"), ("surface", "foam, top layer"), ("well", "a cut-out"), ("line", "outline"),
                     ("text", "text"), ("text2", "secondary"), ("text3", "metadata, Skipped"), ("accent", "steel — primary"),
                     ("problem", "red foam — Problem"), ("note", "yellow foam — Note"), ("checked", "Checked — a dot")],
        "on": "surface",
    },
    {
        "id": "warm", "name": "Warm",
        "thesis": "A tool that feels made by a person for a person. A warm espresso ground, soft "
                  "cards with generous corners, comfortable type, and one bright colour that only "
                  "ever appears on something you can press.",
        "world": "The best consumer apps: soft-cornered cards on a warm tinted ground, plain-language "
                 "labels, a single saturated action colour, sheets that rise from the bottom.",
        "why": [
            ("Owner", "“beautiful, convenient, not so square” — the brief for this round"),
            ("Pair 3", "the consequence sits inside the card, above the button, never in a toast"),
            ("Voice", "plain words, counts and names — the copy already reads like a person wrote it"),
            ("Pair 5", "the one bright colour is an action, never a verdict, so it cannot be read as <i>works</i>"),
        ],
        "variants": [("Layout", "pill navigation; each item a card, auto-added items inside it; Export rises as a sheet"),
                     ("Glass", "a soft frosted veil behind the sheet; every sheet and card is opaque (D2 variant)"),
                     ("Checked", "A — no colour. C is not drawn in this round: two of three directions use green or near-green for the room or the key, where a green Checked would read as the button (D1)"),
                     ("Icons", "Fluent regular, 20")],
        "risk": "The furthest from the Linear / Vercel craft bar the research assumes (H11, a hypothesis). Soft cards cost density; at fifty items the cards must stay one line tall or the collector scrolls forever. Lime must never appear on anything that is not pressable.",
        "guess": "Not from the subject: warm brown and lime are a consumer palette, not an AI one.",
        "style": "regular", "checked_icon": "checkmark",
        "fonts": {"display": "Figtree", "body": "Figtree", "mono": "Source Code Pro"},
        "font_note": "Figtree is friendly and geometric without being round-cute; heavy weights for titles, regular for rows. Source Code Pro for paths, refs and file contents.",
        "tokens": {"bg": "#1C1713", "surface": "#261F1A", "raised": "#2F2721", "line": "#3A3029", "line2": "#4A3E35",
                   "text": "#F3ECE4", "text2": "#C2B4A6", "text3": "#A08F80",
                   "accent": "#CFEA5E", "on-accent": "#1C1713",
                   "problem": "#FF7A6B", "note": "#F4C35A", "checked": "#C2B4A6", "skipped": "#A08F80"},
        "swatches": [("bg", "espresso ground"), ("surface", "a card"), ("raised", "a sheet"), ("line", "divider"),
                     ("text", "text"), ("text2", "secondary, Checked"), ("text3", "metadata, Skipped"),
                     ("accent", "lime — only on what you can press"), ("problem", "Problem"), ("note", "Note")],
        "on": "surface",
    },
]

WEIGHED = [
    ("Spectral plate", "challenger, competitive",
     "Charcoal with colour only as needle-thin emission lines; state carried by line height and dash. Strong on the rule that colour is a claim, but close to round 1’s Catalogue, which was turned down. Its discipline is kept in Glasshouse: auto-added is a drawn line, not a badge."),
    ("Airport wayfinding", "challenger, declined",
     "Saturated yellow bands and black type. Yellow is our Note, so the room would shout a warning. Kept: every panel shows only the actions ahead of you — the item panel ends in exactly two."),
    ("Crouwel grid specimen", "challenger, declined", "A visible construction grid and monumental letters. Kept: one spacing grid, 4 px, under all three."),
    ("Airline timetable on a light table", "challenger, declined", "Raked glass slides at one type size. Kept: rank by weight before size."),
    ("Vertical media feed", "challenger, declined", "One item owns the whole viewport. Not for a set of fifty."),
    ("Braun product family", "our own, not drawn",
     "Warm dark plastic, soft keys, colour only on the one functional key. Close to Warm and Kit at once; held back so the three stay distinct."),
    ("Star atlas", "our own, not drawn", "Items as stars, `requires` as constellation lines. Night-sky palettes slide toward the AI default."),
]


def ic(d, name, cls=""):
    return bd1.ic(d, name, cls)


def mark(d, kind):
    return bd1.mark(d, kind)


def kind_chip(k):
    return f'<span class="kind">{k}</span>'


def state_chip(d, text, st):
    icon = {"conflict": "", "auto": "arrow_turn_down_right", "detached": "link_dismiss"}[st]
    return f'<span class="state st-{st}">{ic(d, icon) if icon else ""}{text}</span>'


def item(d, name, kind, desc, facts, marks=(), states=(), sel=False, sub=""):
    st = "".join(state_chip(d, t, s) for t, s in states)
    m = "".join(mark(d, k) for k in marks)
    cls = ["it"] + (["sel"] if sel else []) + [f"has-{k}" for k in marks] + (["has-sub"] if sub else [])
    return (f'<li class="{" ".join(cls)}"><article class="row"><div class="rmain">'
            f'<h3><span class="nm">{name}</span>{kind_chip(kind)}{st}</h3>'
            f'<p class="desc">{desc}</p><p class="facts">{facts}</p></div>'
            f'<p class="marks">{m}</p></article>{sub}</li>')


C = lambda s: f"<code>{s}</code>"


def the_set(d, sel=True):
    seed = item(d, "seed-data", "script", "Loads a small, realistic dataset into a fresh database.",
                C("scripts/seed-data.sh"), states=[("Auto-added", "auto")])
    db = item(d, "db-migrate", "script",
              "Generates a Postgres migration from a schema diff and runs it — dry run first, then for real.",
              f'{C("scripts/db-migrate.sh")} + 2 files · 1 auto-added', states=[("Auto-added", "auto")],
              sub=f'<ol class="sub">{seed}</ol>')
    pg = item(d, "postgres-mcp", "mcp", "Read-only Postgres access for the agent: schema, explain plans, sample rows.",
              f'{C("modelcontextprotocol/servers-archived")} @ {C("9be4674")} · MIT · needs {C("DATABASE_URL")}',
              marks=["note"], states=[("Auto-added", "auto")])
    return "".join([
        item(d, "code-style", "skill", "How I want TypeScript written: naming, imports, error handling, no default exports.",
             f'{C(".claude/skills/code-style/SKILL.md")} · defers to <em>the client’s ESLint config</em>', marks=["note"]),
        item(d, "eslint-autofix", "script", "Runs ESLint with --fix on staged files before each commit.",
             f'{C("scripts/eslint-autofix.sh")} · conflicts with {C("code-style")}', marks=["problem"],
             states=[("Conflict", "conflict")], sel=sel),
        item(d, "migration-reviewer", "agent",
             "Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills.",
             f'requires {C("db-migrate")}, {C("postgres-mcp")} · 3 auto-added', sub=f'<ol class="sub">{db}{pg}</ol>'),
        item(d, "github-mcp", "mcp", "Issues, pull requests and code search on GitHub, through GitHub’s own server.",
             f'{C("github/github-mcp-server")} @ {C("v0.9.0")} · MIT · needs {C("GITHUB_TOKEN")}'),
        item(d, "pr-reviewer", "agent", "Reviews Acme pull requests against their billing rules.",
             "differs from the original in <em>content</em> and <em>lands at</em>", states=[("Detached", "detached")]),
    ])


def panel(d):
    return f'''<aside class="panel">
  <div class="phd"><div><h2>eslint-autofix</h2><p class="chips">{kind_chip("script")}{state_chip(d, "Conflict", "conflict")}</p></div>
    <span class="btn icon-only" title="Close">{ic(d, "dismiss")}</span></div>
  <p class="desc">Runs ESLint with --fix on staged files before each commit.</p>
  <div class="callout c-problem"><span class="sev">{ic(d, "error_circle")}Problem at last check</span>
    <span>Declares a conflict with {C("code-style")}: it rewrites the imports that {C("code-style")} tells the agent to keep. The archive will contain both, and the agent will get two rules that disagree.</span></div>
  <section class="psec"><h3>In this project</h3><p>Added by you · linked to the original in My library</p></section>
  <section class="psec"><h3>Contents</h3>
<pre class="file">#!/usr/bin/env bash
# Fix what ESLint can fix, on staged files only.
files=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\\.(ts|tsx)$')
[ -z "$files" ] &amp;&amp; exit 0
npx eslint --fix $files &amp;&amp; git add $files</pre>
    <p class="meta">No files attached · no repo</p></section>
  <section class="psec"><h3>Dependencies</h3>
    <dl class="pfacts"><dt>Requires</dt><dd>None</dd><dt>Conflicts with</dt><dd>{C("code-style")}</dd>
    <dt>Env keys</dt><dd>None</dd><dt>Lands at</dt><dd>{C("scripts/eslint-autofix.sh")}</dd></dl></section>
  <section class="psec"><h3>Use</h3><p>Used in 2 projects · last exported 2 days ago</p></section>
  <div class="pact"><span class="btn">Open in My library</span><span class="btn">Configure to remove</span></div>
</aside>'''


def app(d, with_panel=True):
    nav = (f'<nav class="nav"><span class="product"><span class="logo"></span>AI Stack Builder</span>'
           f'<span class="links"><a>{ic(d, "library")}My library</a><a>{ic(d, "globe")}Public library</a>'
           f'<a class="on">{ic(d, "folder")}Projects</a></span>'
           f'<span class="account"><img src="{PORTRAIT}" alt="" width="28" height="28"><span>Maya Chen</span></span></nav>')
    verdict = (f'<div class="verdict"><p class="vline">{ic(d, d["checked_icon"], "vglyph")}<span>Checked 2 days ago · for Claude Code</span></p>'
               f'<p class="vcounts"><span class="c-problem">{ic(d, "error_circle")}1 problem</span>'
               f'<span class="c-note">{ic(d, "info")}2 notes</span><span class="c-skipped">{ic(d, "prohibited")}1 skipped</span></p></div>')
    actions = (f'<div class="actions"><span class="btn">{ic(d, "options")}Configure</span><span class="btn">{ic(d, "share")}Share…</span>'
               f'<span class="btn">{ic(d, "copy")}Duplicate</span><span class="btn primary">{ic(d, "arrow_export_ltr")}Export…</span></div>')
    return f'''<div class="app">{nav}<main class="main">
  <header class="phead"><div class="ptitle"><p class="crumb">Projects /</p><h1>acme-billing-api</h1>
    <p class="pfactsline">14 items · 3 auto-added · 1 detached</p></div>{actions}{verdict}</header>
  <p class="pdesc">Client repo for Acme’s billing service. Code style, migration and review agents, the Postgres and GitHub MCP servers.</p>
  <div class="work{" with" if with_panel else ""}"><ol class="set">{the_set(d, with_panel)}</ol>{panel(d) if with_panel else ""}</div>
</main></div>'''


def stage(d, n, name, kind, result, t, body="", w=0):
    g = {"problem": "error_circle", "note": "info", "skipped": "prohibited", "checked": d["checked_icon"]}[kind]
    return (f'<li class="stage s-{kind}"><div class="sum"><span class="n">{n}</span><span class="sname">{name}</span>'
            f'<span class="res">{ic(d, g, "g-" + kind)}<span>{result}</span></span><span class="time">{t}</span></div>{body}</li>')


def run(d, dialog):
    prob = (f'<div class="sbody"><div class="callout c-problem"><span class="sev">{ic(d, "error_circle")}Problem</span>'
            f'<span>{C("eslint-autofix")} declares a conflict with {C("code-style")}: it rewrites the imports that {C("code-style")} '
            f'tells the agent to keep. The archive will contain both, and the agent will get two rules that disagree.</span>'
            f'<span class="btn">Remove eslint-autofix…</span></div></div>')
    keys = "".join(f'<span class="slot">{ic(d, "key")}<code>{k}</code><small>{who}</small></span>'
                   for k, who in [("DATABASE_URL", "postgres-mcp"), ("GITHUB_TOKEN", "github-mcp"), ("SENTRY_AUTH_TOKEN", "sentry-mcp")])
    env = (f'<div class="sbody"><div class="callout c-note"><span class="sev">{ic(d, "info")}Note</span>'
           f'<span>{C("DATABASE_URL")} (postgres-mcp), {C("GITHUB_TOKEN")} (github-mcp) and {C("SENTRY_AUTH_TOKEN")} (sentry-mcp) are needed. '
           f'They go into {C(".env.example")} as names; the receiving machine supplies the values.</span>'
           f'<span class="slots">{keys}</span></div></div>')
    stages = "".join([
        stage(d, "01", "Requirements", "checked", "14 items · 3 auto-added · no cycles", "0.3 s"),
        stage(d, "02", "Declared conflicts", "problem", "1 problem", "0.1 s", prob),
        stage(d, "03", "Command names", "skipped", "Skipped — no item declares a command", "—"),
        stage(d, "04", "Target paths", "checked", "Checked — no two items write to the same path", "0.2 s"),
        stage(d, "05", "Env keys", "note", "1 note · 3 keys named", "0.1 s", env),
    ])
    dlg = ""
    if dialog:
        dlg = (f'<div class="dveil"></div><div class="dlg" role="dialog" aria-label="Remove eslint-autofix from acme-billing-api?"><div class="sheet">'
               f'<h2>Remove eslint-autofix from acme-billing-api?</h2>'
               f'<p>It leaves this project only. It stays in My library and in the other projects that use it.</p>'
               f'<p class="meta">The check runs again as soon as it is removed.</p>'
               f'<div class="dact"><span class="btn">Cancel</span><span class="btn primary">Remove from project</span></div></div></div>')
    return f'''<div class="runwrap{" withdlg" if dialog else ""}">{app(d, with_panel=False)}<div class="veil"></div>
  <section class="run"><div class="runin">
    <header class="rhead"><div><h2>Checked just now</h2>
      <p class="rcounts"><span class="c-problem">1 problem</span> · <span class="c-note">2 notes</span> · <span class="c-skipped">1 skipped</span></p>
      <p class="meta">acme-billing-api · 14 items · for Claude Code · 1.8 s</p></div>
      <span class="btn icon-only" title="Close">{ic(d, "dismiss")}</span></header>
    <h3 class="group">Findings</h3><ol class="stages">{stages}</ol>
  </div></section>{dlg}</div>'''


def fixed_set(d):
    t = d["tokens"]
    on = t[d["on"]]
    sw = []
    for key, role in d["swatches"]:
        hexv = t[key]
        show = key not in ("bg", "surface", "raised", "line", "line2", "well", "rail")
        rr = f'<span class="cr">{ratio(hexv, on):.1f}:1 on {d["on"]}</span>' if show else '<span class="cr">&nbsp;</span>'
        sw.append(f'<li><span class="chip" style="background:{hexv}"></span><span class="hex">{hexv}</span><span class="role">{role}</span>{rr}</li>')
    f = d["fonts"]
    kinds = "".join(f'<li>{ic(d, n)}<span>{k}</span></li>' for k, n in KINDS)
    acts = "".join(f'<li>{ic(d, n)}<span>{w}</span></li>' for w, n in
                   [("My library", "library"), ("Public library", "globe"), ("Projects", "folder"), ("Configure", "options"),
                    ("Share…", "share"), ("Duplicate", "copy"), ("Export…", "arrow_export_ltr"), ("Detached", "link_dismiss"),
                    ("Auto-added", "arrow_turn_down_right"), ("Env key", "key"), ("Close", "dismiss")])
    sev = "".join(f'<li>{mark(d, k)}</li>' for k in ("problem", "note", "skipped", "checked"))
    return f'''<div class="fixed">
  <div><h3 class="lab">Palette</h3><ul class="swatches">{"".join(sw)}</ul></div>
  <div><h3 class="lab">Type</h3><p class="t-display">acme-billing-api</p>
    <p class="t-body">Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills.</p>
    <p class="t-mono">modelcontextprotocol/servers-archived @ 9be4674 · 0.3 s</p>
    <p class="t-names"><b>{f["display"]}</b> · <b>{f["body"]}</b> · <b>{f["mono"]}</b></p><p class="fnote">{d["font_note"]}</p></div>
  <div><h3 class="lab">Icons · Fluent {d["style"]}</h3><ul class="icons">{kinds}</ul><ul class="icons">{acts}</ul>
    <h3 class="lab">Buttons</h3><div class="btnrow"><span class="btn primary">{ic(d, "arrow_export_ltr")}Export…</span><span class="btn">{ic(d, "options")}Configure</span><span class="btn">Cancel</span></div>
    <h3 class="lab">Severity marks</h3><ul class="sevs">{sev}</ul></div>
</div>'''


def block(d, n):
    t = d["tokens"]
    vars_ = ";".join(f"--{k}:{v}" for k, v in t.items())
    vars_ += (f';--font:"{d["fonts"]["body"]}",system-ui,sans-serif;--font-display:"{d["fonts"]["display"]}",system-ui,sans-serif;'
              f'--font-mono:"{d["fonts"]["mono"]}",ui-monospace,monospace')
    why = "".join(f"<li><b>{a}</b> {b}</li>" for a, b in d["why"])
    var = "".join(f"<li><b>{a}</b> {b}</li>" for a, b in d["variants"])
    return f'''<section class="dir d-{d["id"]}" style='{vars_}' aria-labelledby="h-{d["id"]}">
  <header class="dirhead"><div><p class="dnum">Direction {n} of 3</p><h2 id="h-{d["id"]}">{d["name"]}</h2>
    <p class="thesis">{d["thesis"]}</p><p class="world">{d["world"]}</p></div>
    <div><ul class="why">{why}</ul><ul class="variants">{var}</ul>
    <p class="note2"><b>Guessable from the subject?</b> {d["guess"]}</p><p class="note2"><b>Honest risk.</b> {d["risk"]}</p></div></header>
  {fixed_set(d)}
  <h3 class="lab samplehead">The project, with eslint-autofix open</h3>
  <div class="scale"><div class="native">{app(d)}</div></div>
  <h3 class="lab samplehead">Export, over the project</h3>
  <div class="scale"><div class="native">{run(d, False)}</div></div>
  <h3 class="lab samplehead">The remove dialog, over Export</h3>
  <div class="scale"><div class="native">{run(d, True)}</div></div>
</section>'''


CSS = r"""
:root{--page:#262626;--page-2:#2f2f2f;--page-ink:#e8e8e8;--page-ink-2:#b4b4b4;--page-line:#3d3d3d}
*{box-sizing:border-box}
html{background:var(--page)}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
body{margin:0;background:var(--page);color:var(--page-ink);font:16px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}
.pagehead{max-width:1440px;margin:0 auto;padding:48px 24px 0}
.pagehead h1{font-size:40px;line-height:1.15;margin:0 0 12px;font-weight:600;letter-spacing:-.01em}
.pagehead p{margin:0 0 12px;color:var(--page-ink-2);max-width:90ch;font-size:17px}
.pagehead p b{color:var(--page-ink);font-weight:600}
.pagehead a{color:var(--page-ink)}
.jump{position:sticky;top:0;z-index:5;display:flex;gap:6px;margin:22px -24px 0;padding:12px 24px;background:var(--page);border-bottom:1px solid var(--page-line)}
.jump a{font-size:15px;font-weight:600;color:var(--page-ink);text-decoration:none;padding:8px 14px;border-radius:6px;border:1px solid var(--page-line);background:var(--page-2)}
.jump a:hover{border-color:var(--page-ink-2)}
.jump a:focus-visible{outline:2px solid var(--page-ink);outline-offset:2px}
.grid{display:flex;flex-direction:column;gap:56px;max-width:1440px;margin:0 auto;padding:24px 24px 56px}
.weighed{max-width:1440px;margin:0 auto;padding:0 24px 32px}
.weighed h2{font-size:22px;margin:0 0 6px}
.weighed>p{color:var(--page-ink-2);margin:0 0 16px;max-width:90ch}
.weighed ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:12px}
.weighed li{background:var(--page-2);border:1px solid var(--page-line);border-radius:8px;padding:14px 16px;font-size:14.5px;color:var(--page-ink-2)}
.weighed li b{display:block;color:var(--page-ink);font-size:15.5px}
.weighed li i{font-style:normal;font-size:13px;color:var(--page-ink-2)}
.pagefoot{max-width:1440px;margin:0 auto;padding:0 24px 48px;color:var(--page-ink-2);font-size:14px}

.dir{background:var(--bg);color:var(--text);font-family:var(--font);border-radius:14px;padding:44px 48px 52px;min-width:0;overflow:hidden}
.dir code,.dir pre,.dir .t-mono{font-family:var(--font-mono)}
.dir .lab{font:600 13px/1.2 var(--font);letter-spacing:.08em;text-transform:uppercase;color:var(--text3);margin:0 0 14px}
.dirhead{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:48px;margin-bottom:44px}
.dirhead h2{font-family:var(--font-display);font-size:60px;line-height:1.02;margin:0 0 18px;font-weight:700;letter-spacing:-.02em;scroll-margin-top:90px}
.dnum{margin:0 0 6px;font-size:14px;color:var(--text3)}
.thesis{font-size:21px;line-height:1.45;margin:0 0 14px}
.world{font-size:15.5px;color:var(--text2);margin:0}
.why,.variants{list-style:none;margin:0 0 14px;padding:0;font-size:15px;color:var(--text2)}
.why li,.variants li{margin:0 0 7px}
.why b,.variants b{color:var(--text);margin-right:5px}
.variants{border-top:1px solid var(--line);padding-top:14px}
.note2{font-size:15px;color:var(--text2);margin:0 0 10px}
.note2 b{color:var(--text)}
.fixed{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr) minmax(0,1fr);gap:44px;padding:36px 0 8px;border-top:1px solid var(--line)}
.fixed>div>.lab:not(:first-child){margin-top:28px}
.swatches{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:14px 12px}
.swatches li{display:grid;grid-template-columns:44px 1fr;column-gap:12px;font-size:14px;line-height:1.35}
.swatches .chip{grid-row:1/4;width:44px;height:58px;border-radius:8px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.14)}
.swatches .hex{font-family:var(--font-mono)}
.swatches .role{color:var(--text2)}
.swatches .cr{color:var(--text3);font-variant-numeric:tabular-nums}
.t-display{font-family:var(--font-display);font-size:42px;line-height:1.1;margin:0 0 10px;font-weight:700}
.t-body{font-size:17px;margin:0 0 10px}
.t-mono{font-size:14px;color:var(--text2);margin:0 0 10px}
.t-names{font-size:15px;color:var(--text2);margin:0 0 8px}
.t-names b{color:var(--text)}
.fnote{font-size:14px;color:var(--text3);margin:0}
.icons{list-style:none;padding:0;margin:0 0 12px;display:flex;flex-wrap:wrap;gap:10px 18px}
.icons li{display:flex;align-items:center;gap:8px;font-size:15px;color:var(--text2)}
.icons .ic{width:20px;height:20px;color:var(--text)}
.btnrow{display:flex;flex-wrap:wrap;gap:10px}
.fixed .btn{height:40px;padding:0 16px;font-size:15px}
.sevs{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:10px 20px}
.fixed .mark{font-size:16px}
.fixed .mark .ic{width:20px;height:20px}
.samplehead{margin:48px 0 16px!important;font-size:15px!important}
.scale{width:100%;overflow:hidden;border-radius:10px;box-shadow:0 0 0 1px var(--line2)}
.native{width:1200px;transform-origin:0 0}

.ic{width:18px;height:18px;fill:currentColor;flex:none}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:currentColor;margin:0 5px;flex:none}
.mark{display:inline-flex;align-items:center;gap:6px;font-size:13.5px;font-weight:600;white-space:nowrap}
.m-problem{color:var(--problem)} .m-note{color:var(--note)} .m-skipped{color:var(--skipped);font-weight:500} .m-checked{color:var(--checked);font-weight:500}
.c-problem{color:var(--problem)} .c-note{color:var(--note)} .c-skipped{color:var(--skipped)}
.g-problem{color:var(--problem)} .g-note{color:var(--note)} .g-skipped{color:var(--skipped)} .g-checked{color:var(--checked)}

/* ---------- the app, common ---------- */
.app{background:var(--bg);color:var(--text);font-size:14.5px;line-height:1.45;min-height:820px}
.nav .logo{display:inline-block;width:16px;height:16px;background:var(--text)}
.product{display:flex;align-items:center;gap:10px;font-weight:700;font-size:15px}
.links{display:flex}
.links a{display:flex;align-items:center;gap:8px;color:var(--text2);font-size:14px;font-weight:500}
.links a.on{color:var(--text)}
.account{display:flex;align-items:center;gap:10px;font-size:14px;color:var(--text2)}
.account img{width:28px;height:28px;object-fit:cover}
.phead{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:14px 24px;align-items:start}
.crumb{margin:0 0 4px;font-size:13.5px;color:var(--text3)}
.phead h1{font-family:var(--font-display);margin:0;line-height:1.1}
.pfactsline{margin:6px 0 0;color:var(--text2);font-size:14px}
.actions{display:flex;gap:8px}
.verdict{grid-column:1/-1;display:flex;align-items:center;gap:22px;flex-wrap:wrap}
.vline{margin:0;display:flex;align-items:center;gap:8px;color:var(--text2);font-size:14px}
.vglyph{color:var(--checked)}
.vcounts{margin:0;display:flex;gap:18px;font-size:14.5px;font-weight:600}
.vcounts span{display:flex;align-items:center;gap:6px}
.pdesc{color:var(--text2);max-width:78ch;margin:16px 0 22px}
.btn{display:inline-flex;align-items:center;gap:7px;height:36px;padding:0 14px;font-size:14px;font-weight:500;white-space:nowrap;color:var(--text);border:1px solid var(--line2);background:var(--surface)}
.btn.primary{background:var(--accent);color:var(--on-accent);border-color:var(--accent);font-weight:600}
.btn.icon-only{width:36px;padding:0;justify-content:center}
.work.with{display:grid;grid-template-columns:minmax(0,1fr) 400px;gap:20px;align-items:start}
.set,.sub{list-style:none;margin:0;padding:0}
.row{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:16px;padding:12px 16px}
.row h3{display:flex;align-items:center;gap:9px;margin:0 0 3px;font-size:15px;font-weight:600}
.desc{margin:0 0 3px;color:var(--text2);font-size:14px}
.facts{margin:0;color:var(--text3);font-size:12.5px}
.facts em{font-style:normal;color:var(--text2)}
.facts code,.callout code,.pfacts code,.sbody code{font-size:.92em}
.marks{margin:0;display:flex;gap:12px}
.kind{font-size:12px;font-weight:500;color:var(--text2)}
.state{display:inline-flex;align-items:center;gap:4px;font-size:12px;font-weight:500;color:var(--text2)}
.state .ic{width:14px;height:14px}
.st-conflict{color:var(--problem)}
.panel{background:var(--raised);padding:20px}
.phd{display:flex;justify-content:space-between;gap:12px}
.panel h2{margin:0 0 6px;font-size:19px;font-weight:700}
.chips{display:flex;gap:10px;margin:0 0 10px}
.callout{display:flex;flex-direction:column;gap:7px;padding:12px 14px;font-size:14px;margin:4px 0 6px}
.callout .sev{display:flex;align-items:center;gap:7px;font-weight:600}
.callout.c-problem,.callout.c-note{color:var(--text)}
.c-problem.callout .sev{color:var(--problem)} .c-note.callout .sev{color:var(--note)}
.callout .btn{align-self:flex-start;margin-top:4px}
.psec{margin-top:16px}
.psec h3{margin:0 0 6px;font-size:12px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:var(--text3)}
.psec p{margin:0;font-size:14px;color:var(--text2)}
.file{margin:0 0 6px;padding:12px 14px;font-size:12px;line-height:1.6;white-space:pre-wrap;overflow-wrap:anywhere;background:var(--bg)}
.meta{font-size:12.5px;color:var(--text3)!important}
.pfacts{display:grid;grid-template-columns:128px 1fr;gap:6px 10px;margin:0;font-size:14px}
.pfacts dt{color:var(--text3)} .pfacts dd{margin:0}
.pact{display:flex;gap:8px;margin-top:18px;flex-wrap:wrap}

/* ---------- Export, common ---------- */
.runwrap{position:relative;height:860px;overflow:hidden}
.runwrap .app{min-height:860px}
.veil,.dveil{position:absolute;inset:0}
.run{position:absolute}
.runin{height:100%;overflow:hidden;padding:24px 28px}
.rhead{display:flex;justify-content:space-between;align-items:flex-start}
.rhead h2{font-family:var(--font-display);font-size:30px;margin:0 0 6px;line-height:1.1}
.rcounts{margin:0 0 3px;font-size:15.5px;font-weight:600}
.group{margin:22px 0 10px;font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--text3)}
.stages{list-style:none;margin:0;padding:0}
.sum{display:grid;grid-template-columns:30px 190px minmax(0,1fr) 60px;gap:14px;align-items:center;padding:12px 16px;font-size:14.5px}
.n{font-size:12.5px;color:var(--text3);font-variant-numeric:tabular-nums}
.sname{font-weight:600}
.res{display:flex;align-items:center;gap:8px;color:var(--text2)}
.s-problem .res span{color:var(--problem);font-weight:600}
.s-note .res span{color:var(--note);font-weight:600}
.time{text-align:right;font-family:var(--font-mono);font-size:12.5px;color:var(--text2);font-variant-numeric:tabular-nums}
.sbody{padding:0 16px 14px 60px}
.slots{display:flex;gap:10px;flex-wrap:wrap;margin-top:6px}
.slot{display:inline-flex;align-items:center;gap:7px;font-size:13px}
.slot small{color:var(--text3);font-size:12px}
.slot .ic{width:16px;height:16px;color:var(--text2)}
.dlg{position:absolute;left:50%;top:330px;transform:translateX(-50%);width:500px}
.sheet{padding:24px}
.sheet h2{font-family:var(--font-display);font-size:21px;margin:0 0 12px;line-height:1.2}
.sheet p{margin:0 0 8px;font-size:14.5px;color:var(--text2)}
.dact{display:flex;justify-content:flex-end;gap:10px;margin-top:18px}

/* ===================== Glasshouse ===================== */
.d-glasshouse .app{display:grid;grid-template-columns:232px minmax(0,1fr)}
.d-glasshouse .nav{background:var(--rail);border-right:1px solid var(--line);display:flex;flex-direction:column;gap:26px;padding:22px 16px}
.d-glasshouse .logo{border-radius:50% 50% 3px 3px;background:var(--brass)}
.d-glasshouse .links{flex-direction:column;gap:4px}
.d-glasshouse .links a{padding:9px 12px;border-radius:10px}
.d-glasshouse .links a.on{background:rgba(207,227,216,.10);box-shadow:inset 0 0 0 1px rgba(207,227,216,.18)}
.d-glasshouse .account{margin-top:auto}
.d-glasshouse .account img{border-radius:50%}
.d-glasshouse .main{padding:30px 36px}
.d-glasshouse .phead h1{font-size:40px;font-weight:400}
.d-glasshouse .verdict{padding:12px 16px;border-radius:12px;background:var(--surface);border:1px solid var(--line)}
.d-glasshouse .btn{border-radius:10px;background:transparent;border-color:var(--line2)}
.d-glasshouse .btn.primary{background:var(--accent);border-color:var(--accent)}
.d-glasshouse .set{background:var(--surface);border-radius:16px;padding:6px 0}
.d-glasshouse .set>li+li{border-top:1px solid var(--line)}
.d-glasshouse .kind{padding:1px 8px;border-radius:999px;background:rgba(207,227,216,.08);color:var(--text2)}
.d-glasshouse .it.sel>.row{background:rgba(184,149,90,.09);box-shadow:inset 0 0 0 1px var(--brass);border-radius:12px;margin:0 6px}
/* the stem: auto-added items hang from the item that pulled them in */
.d-glasshouse .sub{margin-left:30px}
.d-glasshouse .sub>li{position:relative;padding-left:26px}
.d-glasshouse .sub>li::before{content:"";position:absolute;left:0;top:-6px;width:20px;height:30px;border-left:1.5px solid var(--line2);border-bottom:1.5px solid var(--line2);border-bottom-left-radius:12px}
.d-glasshouse .sub>li:not(:last-child)::after{content:"";position:absolute;left:0;top:24px;bottom:0;border-left:1.5px solid var(--line2)}
.d-glasshouse .panel{border-radius:18px;border:1px solid var(--line)}
.d-glasshouse .callout{border-radius:12px;background:rgba(242,128,111,.08);border:1px solid rgba(242,128,111,.35)}
.d-glasshouse .callout.c-note{background:rgba(237,193,79,.07);border-color:rgba(237,193,79,.32)}
.d-glasshouse .file{border-radius:10px;border:1px solid var(--line)}
.d-glasshouse .veil{background:rgba(5,12,9,.35)}
.d-glasshouse .run{left:150px;right:150px;top:44px;bottom:0;padding:12px 12px 0;border-radius:22px 22px 0 0;
  background:rgba(120,170,145,.16);backdrop-filter:blur(26px) saturate(150%);-webkit-backdrop-filter:blur(26px) saturate(150%);
  border:1.5px solid var(--brass);border-bottom:0}
.d-glasshouse .run::before{content:"";position:absolute;left:50%;top:0;bottom:0;border-left:1.5px solid rgba(184,149,90,.55);pointer-events:none;z-index:0;display:none}
.d-glasshouse .runin{background:var(--bg);border-radius:14px 14px 0 0;position:relative}
.d-glasshouse .rhead h2{font-weight:400}
.d-glasshouse .stages{background:var(--surface);border-radius:14px}
.d-glasshouse .stage+.stage{border-top:1px solid var(--line)}
.d-glasshouse .slot{padding:6px 10px;border-radius:999px;border:1px solid var(--line2)}
.d-glasshouse .dveil{background:rgba(5,12,9,.30)}
.d-glasshouse .dlg{padding:12px;border-radius:22px;background:rgba(120,170,145,.18);border:1.5px solid var(--brass);
  backdrop-filter:blur(22px) saturate(150%);-webkit-backdrop-filter:blur(22px) saturate(150%)}
.d-glasshouse .sheet{background:var(--raised);border-radius:14px}
.d-glasshouse .sheet h2{font-weight:400}

/* ===================== Kit ===================== */
.d-kit .nav{display:flex;align-items:center;gap:30px;height:60px;padding:0 24px;background:var(--surface);border-bottom:1px solid var(--line)}
.d-kit .logo{border-radius:5px;background:var(--accent)}
.d-kit .links{gap:6px;background:var(--well);padding:4px;border-radius:12px;box-shadow:inset 0 1px 3px rgba(0,0,0,.6)}
.d-kit .links a{padding:7px 14px;border-radius:9px}
.d-kit .links a.on{background:var(--raised);box-shadow:0 1px 0 rgba(255,255,255,.06),0 1px 3px rgba(0,0,0,.5)}
.d-kit .account{margin-left:auto}
.d-kit .account img{border-radius:9px}
.d-kit .main{padding:28px 32px;background:var(--bg)}
.d-kit .phead h1{font-size:36px;font-weight:700;letter-spacing:-.02em}
.d-kit .verdict{padding:10px 14px;border-radius:14px;background:var(--well);box-shadow:inset 0 1px 4px rgba(0,0,0,.7)}
.d-kit .btn{border-radius:11px;background:var(--raised);border-color:var(--line2);box-shadow:0 1px 0 rgba(255,255,255,.05)}
.d-kit .btn.primary{background:var(--accent);border-color:var(--accent);box-shadow:0 1px 0 rgba(255,255,255,.4) inset}
/* every item in its own cut-out; colour only shows through where something is wrong */
.d-kit .set{display:flex;flex-direction:column;gap:10px;padding:12px;background:var(--surface);border-radius:20px}
.d-kit .it{background:var(--well);border-radius:16px;box-shadow:inset 0 2px 5px rgba(0,0,0,.75),inset 0 0 0 1px rgba(255,255,255,.03)}
.d-kit .it.has-problem{box-shadow:inset 0 0 0 2px var(--problem),inset 0 2px 5px rgba(0,0,0,.75)}
.d-kit .it.has-note{box-shadow:inset 0 0 0 2px rgba(245,196,81,.75),inset 0 2px 5px rgba(0,0,0,.75)}
.d-kit .it.sel{outline:2px solid var(--accent);outline-offset:3px}
.d-kit .sub{display:flex;flex-direction:column;padding:0 6px 4px 28px}
.d-kit .sub .it{background:transparent;box-shadow:none;border-top:1px dashed var(--line2);border-radius:0}
.d-kit .sub .it.sel{outline:none}
.d-kit .kind{padding:2px 9px;border-radius:999px;background:var(--surface);color:var(--text2)}
.d-kit .panel{border-radius:20px;background:var(--raised);box-shadow:0 18px 40px rgba(0,0,0,.45),0 1px 0 rgba(255,255,255,.05) inset}
.d-kit .callout{border-radius:14px;background:var(--well);box-shadow:inset 0 0 0 2px var(--problem)}
.d-kit .callout.c-note{box-shadow:inset 0 0 0 2px rgba(245,196,81,.75)}
.d-kit .file{border-radius:12px;box-shadow:inset 0 2px 5px rgba(0,0,0,.7)}
.d-kit .veil{background:rgba(0,0,0,.55)}
.d-kit .run{right:0;top:0;bottom:0;width:820px;background:var(--surface);border-radius:24px 0 0 24px;box-shadow:-30px 0 60px rgba(0,0,0,.5)}
.d-kit .stages{display:flex;flex-direction:column;gap:10px}
.d-kit .stage{background:var(--well);border-radius:16px;box-shadow:inset 0 2px 5px rgba(0,0,0,.75)}
.d-kit .stage.s-problem{box-shadow:inset 0 0 0 2px var(--problem),inset 0 2px 5px rgba(0,0,0,.75)}
.d-kit .stage.s-note{box-shadow:inset 0 0 0 2px rgba(245,196,81,.75),inset 0 2px 5px rgba(0,0,0,.75)}
.d-kit .stage.s-skipped{background:transparent;box-shadow:none;outline:1.5px dashed var(--line2);outline-offset:-1.5px}
.d-kit .stage .callout{box-shadow:none;background:transparent;padding:0}
.d-kit .sum{grid-template-columns:30px 180px minmax(0,1fr) 56px}
.d-kit .sbody{padding-left:60px}
.d-kit .slot{padding:8px 12px;border-radius:12px;outline:1.5px dashed var(--line2);outline-offset:-1.5px}
.d-kit .dveil{background:rgba(0,0,0,.45)}
.d-kit .sheet{background:var(--raised);border-radius:22px;box-shadow:0 30px 70px rgba(0,0,0,.6),0 1px 0 rgba(255,255,255,.06) inset}

/* ===================== Warm ===================== */
.d-warm .nav{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;height:68px;padding:0 28px}
.d-warm .logo{border-radius:6px;background:var(--text)}
.d-warm .links{gap:4px;background:var(--surface);padding:5px;border-radius:999px}
.d-warm .links a{padding:8px 16px;border-radius:999px}
.d-warm .links a.on{background:var(--text);color:var(--bg)}
.d-warm .account{justify-self:end}
.d-warm .account img{border-radius:50%}
.d-warm .main{padding:14px 40px 36px}
.d-warm .phead{background:var(--surface);border-radius:26px;padding:26px 28px}
.d-warm .phead h1{font-size:38px;font-weight:800;letter-spacing:-.02em}
.d-warm .verdict{padding-top:16px;border-top:1px solid var(--line)}
.d-warm .vcounts{font-size:15.5px}
.d-warm .btn{border-radius:999px;background:var(--raised);border-color:transparent;height:40px;padding:0 18px}
.d-warm .btn.primary{background:var(--accent);color:var(--on-accent)}
.d-warm .btn.icon-only{width:40px;padding:0}
.d-warm .set{display:flex;flex-direction:column;gap:12px}
.d-warm .set>li{background:var(--surface);border-radius:22px;padding:4px 4px}
.d-warm .set>li.sel{box-shadow:0 0 0 2px var(--text)}
.d-warm .row{padding:14px 18px}
.d-warm .sub{margin:0 14px 10px 26px;border-top:1px solid var(--line)}
.d-warm .sub .sub{margin:0 0 0 22px;border-top:0}
.d-warm .sub>li+li,.d-warm .sub .sub>li{border-top:1px solid var(--line)}
.d-warm .sub .row{padding:12px 4px}
.d-warm .kind{padding:2px 10px;border-radius:999px;background:var(--raised)}
.d-warm .panel{border-radius:26px}
.d-warm .panel .btn,.d-warm .panel .kind{background:var(--surface)}
.d-warm .panel .btn.icon-only{background:var(--surface)}
.d-warm .callout{border-radius:18px;background:rgba(255,122,107,.10)}
.d-warm .callout.c-note{background:rgba(244,195,90,.09)}
.d-warm .file{border-radius:14px}
.d-warm .veil{background:rgba(20,15,11,.45);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
.d-warm .run{left:70px;right:70px;top:90px;bottom:0;background:var(--raised);border-radius:32px 32px 0 0;box-shadow:0 -20px 60px rgba(0,0,0,.45)}
.d-warm .run::before{content:"";position:absolute;left:50%;top:10px;width:44px;height:5px;margin-left:-22px;border-radius:3px;background:var(--line2)}
.d-warm .runin{padding:30px 34px}
.d-warm .rhead h2{font-weight:800;font-size:32px}
.d-warm .stages{display:flex;flex-direction:column;gap:10px}
.d-warm .stage{background:var(--surface);border-radius:20px}
.d-warm .slot{padding:7px 12px;border-radius:999px;background:var(--raised)}
.d-warm .dveil{background:rgba(20,15,11,.5)}
.d-warm .sheet{background:var(--surface);border-radius:28px;box-shadow:0 30px 70px rgba(0,0,0,.5)}
.d-warm .sheet h2{font-weight:800}

@media (max-width:1100px){.dirhead,.fixed{grid-template-columns:minmax(0,1fr);gap:28px}.dir{padding:28px 20px 32px}.dirhead h2{font-size:42px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

JS = r"""
(function(){
  function fit(){document.querySelectorAll('.scale').forEach(function(s){
    var n=s.firstElementChild,k=s.clientWidth/1200;n.style.transform='scale('+k+')';s.style.height=(n.offsetHeight*k)+'px';});}
  window.addEventListener('resize',fit);
  if(document.fonts&&document.fonts.ready){document.fonts.ready.then(fit);}
  window.addEventListener('load',fit);fit();
})();
"""

FONTS = ("https://fonts.googleapis.com/css2?family=Young+Serif&family=Hanken+Grotesk:wght@400;500;600;700"
         "&family=JetBrains+Mono:wght@400;500&family=Rubik:wght@400;500;600;700&family=Fira+Code:wght@400;500"
         "&family=Figtree:wght@400;500;600;700;800&family=Source+Code+Pro:wght@400;500&display=swap")


def build():
    blocks = "".join(block(d, i + 1) for i, d in enumerate(DIRS))
    weighed = "".join(f"<li><b>{n}</b><i>{k}</i><br>{t}</li>" for n, k, t in WEIGHED)
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Three more directions · AI Stack Builder</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}"><style>{CSS}</style></head>
<body>{bd1.symbols()}
<header class="pagehead">
  <h1>Three more directions for AI Stack Builder</h1>
  <p>Phase 06, stage 3, <b>round 2</b>. Round 1 — <a href="directions.html">Acrylic, Manifest, Catalogue</a> — was turned down, and none of its directions comes back here. <b>These three are new worlds, and they are allowed to change the layout</b>: the wireframes fixed what is on the screen, not how it looks. Each one rearranges the Project screen its own way — a left rail and stems, a drawer of cut-outs, soft cards and a rising sheet.</p>
  <p><b>What did not change</b>: every word is from <code>microcopy.md</code>; dark-first (CLAUDE.md §3); colour only where it states something; no score, no badge, no green tick that claims <i>works</i>. Between them the three still cover D1 and D2–D4.</p>
  <p><b>This grey page is not part of any direction.</b> Ratios on the swatches are WCAG contrast, computed when the page is built.</p>
  <nav class="jump" aria-label="Directions"><a href="#h-glasshouse">1 · Glasshouse</a><a href="#h-kit">2 · Kit</a><a href="#h-warm">3 · Warm</a><a href="#weighed">Also weighed</a></nav>
</header>
<main class="grid">{blocks}</main>
<section class="weighed" id="weighed" aria-labelledby="w-h"><h2 id="w-h">Also weighed, and not drawn</h2>
<p>The other candidates of this round, so the choice is made against the whole hand. Any of them can be drawn on request.</p><ul>{weighed}</ul></section>
<p class="pagefoot">Built by <code>tools/build_directions_2.py</code>. Icons: Microsoft Fluent System Icons, MIT, @fluentui/svg-icons 1.1.344. Portrait: Jake Nackos on Unsplash (unsplash.com/photos/IF9TK5Uy-KI), standing in for the signed-in person.</p>
<script>{JS}</script></body></html>'''
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
