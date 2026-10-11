"""Phase 06, stage 4: build 06-concept/concept.html — the stand of the working style, Mica · Lime.

On top, the style at work: a shared project's card with its sharer's portrait, buttons, the top bar
and the Export head. Below: the colours with the attribute each comes from, the type pair and its
scale, the form (radius, shadow, spacing), Lucide icons in use, three components of AI Stack Builder,
the light slice, and the WCAG table measured by tools/contrast.py on tokens.css.

    python tools/concept_tokens.py && python tools/contrast.py && python tools/build_concept.py

Every value comes from 06-concept/tokens.css; this page's own CSS uses var() only.
"""
from pathlib import Path
import importlib.util
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import concept_ui  # noqa: E402
import concept_tokens as T  # noqa: E402
import contrast  # noqa: E402

_spec = importlib.util.spec_from_file_location("bd4", ROOT / "tools" / "build_directions_4.py")
bd4 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bd4)
bd2 = bd4.bd2
LIME = next(d for d in bd4.DIRS if d["id"] == "lime")
ic = bd4.ic
OUT = ROOT / "06-concept" / "concept.html"
PORTRAIT = bd2.PORTRAIT
C = lambda s: f"<code>{s}</code>"

PAGE_CSS = r"""
*{box-sizing:border-box}
html{background:var(--ground)}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
body{margin:0;background:var(--ground);color:var(--text);font:var(--t-body)}
.wrap{max-width:calc(var(--canvas) + var(--s12));margin:0 auto;padding:0 var(--s6)}
.top{padding-top:var(--s10)}
.top h1{font:var(--t-display);letter-spacing:var(--track-display);margin:0 0 var(--s2)}
.top p{margin:0 0 var(--s3);color:var(--text-2);max-width:92ch}
.top p b{color:var(--text)}
.top a,.foot a{color:var(--text)}
.jump{position:sticky;top:0;z-index:5;display:flex;flex-wrap:wrap;gap:var(--s1);margin:var(--s5) calc(var(--s6) * -1) 0;padding:var(--s2) var(--s6);background:var(--bar);border-bottom:var(--hairline) solid var(--line)}
.jump a{display:inline-flex;align-items:center;height:var(--control-h);padding:0 var(--s3);border-radius:var(--r-sm);color:var(--text-2);font:var(--t-button);text-decoration:none}
.jump a:hover{background:var(--hover-wash);color:var(--text)}
.jump a:focus-visible{outline:0;box-shadow:var(--shadow-focus)}
section.s{padding-top:var(--s12)}
section.s>h2{font:var(--t-title);letter-spacing:var(--track-title);margin:0 0 var(--s2);scroll-margin-top:calc(var(--s12) + var(--s4))}
section.s>p.lead{margin:0 0 var(--s5);color:var(--text-2);max-width:88ch}
.lab{margin:0 0 var(--s3);font:var(--t-label);letter-spacing:var(--track-label);text-transform:uppercase;color:var(--text-3)}
.panelbox{background:var(--tray);border-radius:var(--r-lg);padding:var(--s6)}
.grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s5)}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s5)}

/* the hero: the style at work */
.hero{background:var(--ground);border-radius:var(--r-xl);box-shadow:0 0 0 var(--hairline) var(--line);overflow:hidden}
.hero-body{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:var(--s6);padding:var(--s8)}
.card{align-self:start;background:var(--raised);border:var(--hairline) solid var(--line);border-radius:var(--r-lg);overflow:hidden}
.card .owner{display:flex;align-items:center;gap:var(--s3);padding:var(--s4) var(--s5);border-bottom:var(--hairline) solid var(--line);font:var(--t-small);color:var(--text-2)}
.card .owner img{width:calc(var(--s10) - var(--s1));height:calc(var(--s10) - var(--s1));border-radius:var(--r-pill);object-fit:cover;box-shadow:0 0 0 var(--hairline) var(--line-strong)}
.card .owner b{display:block;font:var(--t-body);font-weight:600;color:var(--text)}
.card .cb{padding:var(--s5)}
.card h3{margin:0;font:var(--t-display);letter-spacing:var(--track-display)}
.card .cmeta{display:flex;flex-wrap:wrap;gap:var(--s1) var(--s3);margin:var(--s2) 0 0;font:var(--t-small);color:var(--text-2)}
.card .cmeta span+span::before{content:"·";margin-right:var(--s3);color:var(--text-3)}
.card .cdesc{margin:var(--s3) 0 0;color:var(--text-2)}
.card .cact{display:flex;gap:var(--s2);margin-top:var(--s5)}
.stack{display:flex;flex-direction:column;gap:var(--s4)}
.btnrow{display:flex;flex-wrap:wrap;gap:var(--s2);align-items:center}
.runbar{display:flex;align-items:center;gap:var(--s5);padding:var(--s4) var(--s5);background:var(--raised);border:var(--hairline) solid var(--line);border-radius:var(--r-lg)}
.runbar h4{margin:0;font:var(--t-title);letter-spacing:var(--track-title)}
.runbar .rc{margin:var(--s1) 0 0;font:var(--t-small);font-weight:600}
.runbar .meta{margin-top:calc(var(--s1) / 2)}
.runbar .btn{margin-left:auto}

/* colours */
.cgroup{margin-bottom:var(--s8)}
.cgroup:last-child{margin-bottom:0}
.cgroup h3{margin:0 0 var(--s1);font:var(--t-heading)}
.cgroup>p{margin:0 0 var(--s4);font:var(--t-small);color:var(--text-2);max-width:88ch}
.sw{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(calc(var(--panel-w) - var(--s12)),1fr));gap:var(--s3)}
.sw li{display:grid;grid-template-columns:calc(var(--s12) + var(--s2)) minmax(0,1fr);gap:var(--s3);padding:var(--s3);background:var(--cutout);border-radius:var(--r-md);box-shadow:var(--shadow-cutout)}
.sw .chip{width:calc(var(--s12) + var(--s2));height:calc(var(--s12) + var(--s2));border-radius:var(--r-sm);box-shadow:inset 0 0 0 var(--hairline) var(--sheet-edge)}
.sw b{display:block;font:var(--t-code);color:var(--text)}
.sw .role{display:block;margin-top:calc(var(--s1) / 2);font:var(--t-small);color:var(--text)}
.sw .why{display:block;margin-top:var(--s1);font:var(--t-micro);font-weight:400;color:var(--text-3)}

/* type, form */
.types{list-style:none;margin:0;padding:0}
.types li{display:grid;grid-template-columns:calc(var(--dt-w) + var(--s10)) minmax(0,1fr) calc(var(--dt-w) * 2);gap:var(--s4);align-items:baseline;padding:var(--s3) 0;border-top:var(--hairline) solid var(--line)}
.types li:first-child{border-top:0}
.types .tn{font:var(--t-code);color:var(--text-3)}
.types .tu{font:var(--t-small);color:var(--text-3)}
.pair{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s5);margin-bottom:var(--s5)}
.pair div{padding:var(--s5);background:var(--cutout);border-radius:var(--r-md);box-shadow:var(--shadow-cutout)}
.pair .big{margin:0 0 var(--s2);font:var(--t-display);font-size:calc(var(--s12) - var(--s2));line-height:1.1}
.pair .big.m{font-family:var(--mono);font-weight:400}
.pair p{margin:0;font:var(--t-small);color:var(--text-2)}
.form3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s5)}
.spec{display:flex;flex-wrap:wrap;align-items:flex-end;gap:var(--s4)}
.spec figure{margin:0;display:flex;flex-direction:column;align-items:center;gap:var(--s2);font:var(--t-micro);font-weight:400;color:var(--text-3)}
.spec .r{width:calc(var(--s12) + var(--s2));height:calc(var(--s12) + var(--s2));background:var(--control);box-shadow:inset 0 0 0 var(--hairline) var(--line-strong)}
.spec .sp{background:var(--lime-mark);border-radius:var(--r-xs)}
.spec .sh{width:calc(var(--s12) * 2);height:calc(var(--s12) + var(--s2));background:var(--raised);border-radius:var(--r-md)}
.spec figcaption{text-align:center;max-width:calc(var(--s12) * 2 + var(--s4))}

/* icons */
.icongrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s5)}
.icongrid>div{padding:var(--s5);background:var(--cutout);border-radius:var(--r-md);box-shadow:var(--shadow-cutout)}
.icongrid h3{margin:0 0 var(--s4);font:var(--t-heading)}
.icongrid .kinds{display:flex;flex-wrap:wrap;gap:var(--s4) var(--s5)}
.icongrid .kinds span{display:flex;flex-direction:column;align-items:center;gap:var(--s2);font:var(--t-micro);font-weight:400;color:var(--text-2)}
.icongrid .kinds .ic{width:var(--icon-l);height:var(--icon-l);color:var(--text)}
.icongrid .row-of{display:flex;flex-wrap:wrap;gap:var(--s2);align-items:center}
.icongrid .note{margin:var(--s4) 0 0;font:var(--t-small);color:var(--text-3)}

/* components */
.comp{display:grid;grid-template-columns:calc(var(--panel-w) - var(--s12)) minmax(0,1fr);gap:var(--s8);padding:var(--s6);background:var(--tray);border-radius:var(--r-lg);margin-bottom:var(--s5)}
.comp h3{margin:0 0 var(--s2);font:var(--t-heading)}
.comp .why{margin:0 0 var(--s3);font:var(--t-small);color:var(--text-2)}
.comp ul{margin:0;padding-left:var(--s4);font:var(--t-small);color:var(--text-3)}
.comp ul li{margin-bottom:var(--s1)}
.comp .demo{display:flex;flex-direction:column;gap:var(--s3)}
.comp .demo .set{background:transparent;padding:0}
.comp .cap{margin:calc(var(--s1) * -1) 0 var(--s2);font:var(--t-micro);font-weight:400;color:var(--text-3)}
.fields{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s5)}

/* light slice */
.theme-light.slice{background:var(--ground);color:var(--text);border-radius:var(--r-lg);padding:var(--s6);box-shadow:0 0 0 var(--hairline) var(--line)}
.slice .set{background:var(--tray)}
.slice .btnrow{margin-top:var(--s4)}
.slice .lab{color:var(--text-3)}

/* the contrast table */
.ct{width:100%;border-collapse:collapse;font:var(--t-small)}
.ct th,.ct td{padding:var(--s2) var(--s3);border-bottom:var(--hairline) solid var(--line);text-align:left;vertical-align:middle}
.ct thead th{font:var(--t-label);letter-spacing:var(--track-label);text-transform:uppercase;color:var(--text-3);background:var(--cutout)}
.ct td.n{text-align:right;font:var(--t-code);font-variant-numeric:tabular-nums}
.ct .smp{display:inline-flex;align-items:center;justify-content:center;min-width:calc(var(--s12) + var(--s4));height:var(--mark-h);padding:0 var(--s2);border-radius:var(--r-sm);font:var(--t-micro);box-shadow:inset 0 0 0 var(--hairline) var(--sheet-edge)}
.ct code{font:var(--t-code);color:var(--text-2)}
.ct .ok{color:var(--checked)} .ct .bad{color:var(--problem);font-weight:600}
.ct .na{color:var(--text-3)}
.foot{padding:var(--s12) 0;color:var(--text-3);font:var(--t-small)}
@media (max-width:1100px){.hero-body,.grid2,.grid3,.pair,.form3,.icongrid,.comp,.fields{grid-template-columns:minmax(0,1fr)}.types li{grid-template-columns:minmax(0,1fr)}}
"""


def hero():
    nav = (f'<nav class="nav"><span class="product"><span class="logo"></span>AI Stack Builder</span>'
           f'<span class="links"><a>{ic(LIME, "library")}My library</a><a>{ic(LIME, "globe")}Public library</a>'
           f'<a class="on">{ic(LIME, "folder")}Projects</a></span>'
           f'<span class="account"><img src="{PORTRAIT}" alt="" width="24" height="24"><span>Maya Chen</span></span></nav>')
    card = f'''<article class="card" aria-label="A shared project">
  <div class="owner"><img src="{PORTRAIT.replace("w=96&h=96", "w=160&h=160")}" alt="Maya Chen" width="36" height="36"><span><b>Shared by Maya Chen</b>AI Stack Builder</span></div>
  <div class="cb"><h3>agent-dotfiles</h3>
    <p class="cmeta"><span>9 items</span><span>Changed 1 day ago</span></p>
    <p class="cmeta"><span>Maya checked it 5 days ago · for Claude Code — the project has changed since</span></p>
    <p class="cdesc">My everyday setup across machines: commit conventions, the review subagent, the filesystem and memory MCP servers.</p>
    <div class="cact"><span class="btn">Copy to My library</span><span class="btn primary">{ic(LIME, "arrow_export_ltr")}Export…</span></div></div>
</article>'''
    row = '<ol class="set">' + bd2.item(LIME, "eslint-autofix", "script", "Runs ESLint with --fix on staged files before each commit.",
                                         f'{C("scripts/eslint-autofix.sh")} · conflicts with {C("code-style")}', marks=["problem"],
                                         states=[("Conflict", "conflict")], sel=True) + \
          bd2.item(LIME, "postgres-mcp", "mcp", "Read-only Postgres access for the agent: schema, explain plans, sample rows.",
                   f'{C("modelcontextprotocol/servers-archived")} @ {C("9be4674")} · MIT · needs {C("DATABASE_URL")}',
                   marks=["note"], states=[("Auto-added", "auto")]) + '</ol>'
    btns = (f'<div class="btnrow"><span class="btn primary">{ic(LIME, "arrow_export_ltr")}Export…</span>'
            f'<span class="btn">{ic(LIME, "options")}Configure</span><span class="btn">{ic(LIME, "share")}Share…</span>'
            f'</div><div class="btnrow"><span class="btn danger-ghost">Remove eslint-autofix…</span><span class="btn danger">Remove from project</span><span class="btn">Cancel</span></div>')
    runbar = (f'<div class="runbar"><div><h4>Checked just now</h4><p class="rc"><span class="c-problem">1 problem</span> · '
              f'<span class="c-note">2 notes</span> · <span class="c-skipped">1 skipped</span></p>'
              f'<p class="meta">acme-billing-api · 14 items · for Claude Code · 1.8 s</p></div>'
              f'<span class="btn primary">{ic(LIME, "arrow_export_ltr")}Export with 1 problem</span></div>')
    return f'<div class="hero">{nav}<div class="hero-body">{card}<div class="stack">{row}{btns}{runbar}</div></div></div>'


def colours():
    groups = [
        ("primary", "Primary — lime, the one colour that acts",
         "Lime is the brand and the only colour that invites an action: the primary button, where you are, the active row. It never states a verdict, so it can never be read as “works”."),
        ("neutral", "Neutrals — Mica",
         "A neutral ground with a faint lime tint, and quiet layers above it: hierarchy by layer and weight, not by colour."),
        ("state", "States — what was found",
         "Problem and Note carry colour because they state something the product knows. There is no success colour: the best a check says is <i>Checked</i>, a quiet dot. The red is kept for an act that removes something."),
    ]
    out = []
    for g, title, intro in groups:
        items = [c for c in T.COLORS if c[2] == g]
        lis = "".join(f'<li><span class="chip" style="background:var(--{n})"></span><span><b>--{n} {v}</b>'
                      f'<span class="role">{role}</span><span class="why">{why}</span></span></li>' for n, v, _, role, why in items)
        out.append(f'<div class="cgroup"><h3>{title}</h3><p>{intro}</p><ul class="sw">{lis}</ul></div>')
    return "".join(out)


def typography():
    lis = "".join(f'<li><span class="tn">--t-{n} · {s:g}/{lh} · {w}</span>'
                  f'<span style="font:var(--t-{n});{"text-transform:uppercase;letter-spacing:var(--track-label);" if n == "label" else ""}color:var(--text)">{sample}</span>'
                  f'<span class="tu">{use}</span></li>' for n, w, s, lh, sample, use in T.TYPE)
    return (f'<div class="pair"><div><p class="big">Geist</p><p>The interface: names, sentences, buttons, titles. One family, weight carries rank; '
            f'the owner’s choice after the polish.</p></div><div><p class="big m">Geist Mono</p><p>Only for what is literally code: paths, '
            f'refs, env key names, file contents, durations.</p></div></div>'
            f'<div class="panelbox"><ul class="types">{lis}</ul></div>')


def form():
    radii = "".join(f'<figure><span class="r" style="border-radius:var(--r-{n})"></span><figcaption>--r-{n}<br>{px if px < 999 else "pill"}{"" if px >= 999 else " px"}</figcaption></figure>' for n, px in T.RADIUS)
    space = "".join(f'<figure><span class="sp" style="width:var(--s{n});height:var(--s{n})"></span><figcaption>--s{n}<br>{px}</figcaption></figure>' for n, px in T.SPACE)
    shadows = "".join(f'<figure><span class="sh" style="box-shadow:var(--shadow-{n})"></span><figcaption>--shadow-{n}<br>{use}</figcaption></figure>' for n, _, use in T.SHADOW)
    return (f'<div class="form3"><div class="panelbox"><p class="lab">Radius</p><div class="spec">{radii}</div></div>'
            f'<div class="panelbox"><p class="lab">Spacing · a 4 px scale</p><div class="spec">{space}</div></div>'
            f'<div class="panelbox"><p class="lab">Shadow · hairlines first, shadows rare</p><div class="spec">{shadows}</div></div></div>')


def icons():
    kinds = "".join(f'<span>{ic(LIME, n)}{k}</span>' for k, n in bd2.KINDS)
    places = f'<div class="nav" style="padding:0;height:auto;background:transparent;border:0"><span class="links"><a>{ic(LIME, "library")}My library</a><a class="is-hover">{ic(LIME, "globe")}Public library</a><a class="on">{ic(LIME, "folder")}Projects</a></span></div>'
    btns = (f'<div class="row-of"><span class="btn">{ic(LIME, "options")}Configure</span><span class="btn">{ic(LIME, "share")}Share…</span>'
            f'<span class="btn">{ic(LIME, "copy")}Duplicate</span><span class="btn primary">{ic(LIME, "arrow_export_ltr")}Export…</span>'
            f'<span class="btn icon-only" title="Close">{ic(LIME, "dismiss")}</span></div>')
    states = (f'<div class="row-of">{bd2.mark(LIME, "problem")}{bd2.mark(LIME, "note")}{bd2.mark(LIME, "skipped")}{bd2.mark(LIME, "checked")}</div>'
              f'<div class="row-of" style="margin-top:var(--s3)"><span class="state">{ic(LIME, "arrow_turn_down_right")}Auto-added</span>'
              f'<span class="state">{ic(LIME, "link_dismiss")}Detached</span><span class="slot">{ic(LIME, "key")}<code>DATABASE_URL</code><small>postgres-mcp</small></span></div>')
    return (f'<div class="icongrid"><div><h3>The six kinds, alone</h3><div class="kinds">{kinds}</div><p class="note">20 px, 1.75 px stroke, in the text colour.</p></div>'
            f'<div><h3>In controls</h3>{places}<div style="height:var(--s4)"></div>{btns}<p class="note">16 px, in the label’s secondary tone; lime only on the current place.</p></div>'
            f'<div><h3>As states and facts</h3>{states}<p class="note">14 px, in the finding’s colour; the shape differs too, so it survives greyscale.</p></div></div>')


def components():
    one = lambda cls, cap: (f'<ol class="set"><li class="it {cls}"><article class="row"><div class="rmain"><h3><span class="nm">github-mcp</span>'
                            f'<span class="kind">mcp</span></h3><p class="desc">Issues, pull requests and code search on GitHub, through GitHub’s own server.</p>'
                            f'<p class="facts">{C("github/github-mcp-server")} @ {C("v0.9.0")} · MIT · needs {C("GITHUB_TOKEN")}</p></div>'
                            f'<p class="marks"></p></article></li></ol><p class="cap">{cap}</p>')
    rows = ('<ol class="set">' + bd2.the_set(LIME, sel=True).split('<li class="it has-sub">')[0] + '</ol><p class="cap">with a Note, active with a Problem and a Conflict</p>'
            + one("", "default") + one("is-hover", "hover"))
    item_c = f'''<div class="comp"><div><h3>1 · The item row</h3>
  <p class="why">The only place an item’s state is true (§8). A cut-out per item; a finding as a tag on the right; the active row as a lime pill.</p>
  <ul><li>name 14.5/600 · kind tag 12 outline · description 13 · path in Geist Mono 12</li><li>padding --s3 --s4 · radius --r-md · gap between rows --s2</li><li>states: default · hover (--hover-wash) · active (--raised + lime pill)</li></ul></div>
  <div class="demo">{rows}</div></div>'''
    prob = (f'<div class="sbody"><div class="callout c-problem"><span class="sev">{ic(LIME, "error_circle")}Problem</span>'
            f'<span>{C("eslint-autofix")} declares a conflict with {C("code-style")}: it rewrites the imports that {C("code-style")} tells the agent to keep. '
            f'The archive will contain both, and the agent will get two rules that disagree.</span><span class="btn">Remove eslint-autofix…</span></div></div>')
    keys = "".join(f'<span class="slot">{ic(LIME, "key")}<code>{k}</code><small>{w}</small></span>' for k, w in
                   [("DATABASE_URL", "postgres-mcp"), ("GITHUB_TOKEN", "github-mcp"), ("SENTRY_AUTH_TOKEN", "sentry-mcp")])
    env = (f'<div class="sbody"><div class="callout c-note"><span class="sev">{ic(LIME, "info")}Note</span>'
           f'<span>{C("DATABASE_URL")} (postgres-mcp), {C("GITHUB_TOKEN")} (github-mcp) and {C("SENTRY_AUTH_TOKEN")} (sentry-mcp) are needed. '
           f'They go into {C(".env.example")} as names; the receiving machine supplies the values.</span><span class="slots">{keys}</span></div></div>')
    stages = "".join([bd2.stage(LIME, "02", "Declared conflicts", "problem", "1 problem", "0.1 s", prob),
                      bd2.stage(LIME, "03", "Command names", "skipped", "Skipped — no item declares a command", "—"),
                      bd2.stage(LIME, "04", "Target paths", "checked", "Checked — no two items write to the same path", "0.2 s"),
                      bd2.stage(LIME, "05", "Env keys", "note", "1 note · 3 keys named", "0.1 s", env)])
    stage_c = f'''<div class="comp"><div><h3>2 · A stage of the check</h3>
  <p class="why">The designed moment (§2, §6): what was examined, its verdict, how long it took. Nothing blocks; the remove inside a Problem is muted.</p>
  <ul><li>number and duration in Geist Mono, tabular</li><li>Problem and Note boxes: a wash and an edge in their colour</li><li>Skipped is an empty dashed outline; Checked a quiet dot, never green</li></ul></div>
  <div class="demo"><ol class="stages">{stages}</ol></div></div>'''
    hint = f'<span class="hint">{ic(LIME, "info")}Names only. Values never live here.</span>'
    field_c = f'''<div class="comp"><div><h3>3 · A field</h3>
  <p class="why">From the item form: the value is code, so it is set in Geist Mono on the darkest well; the hint says what the product never stores.</p>
  <ul><li>label 13/500 · input 32 high, --r-sm, --well-deep</li><li>focus: a lime edge and the 2 px focus ring</li><li>hint 13 in --text-3, with its icon</li></ul></div>
  <div class="demo"><div class="fields">
    <label class="field"><span>Env keys it needs</span><input value="DATABASE_URL" placeholder="GITHUB_TOKEN" readonly>{hint}</label>
    <label class="field"><span>Env keys it needs</span><input class="is-focus" value="DATABASE_URL, SENTRY_AUTH_TOKEN" readonly>{hint}</label>
    <label class="field"><span>Lands at</span><input value="" placeholder=".claude/skills/release-notes/SKILL.md" readonly></label>
    <label class="field"><span>Defers to</span><input value="the client’s ESLint config" readonly><span class="hint">{ic(LIME, "info")}Where they disagree, that wins.</span></label>
  </div><p class="cap">default · focus · empty with its placeholder · with a hint</p></div></div>'''
    return item_c + stage_c + field_c


def light_slice():
    rows = '<ol class="set">' + bd2.item(LIME, "eslint-autofix", "script", "Runs ESLint with --fix on staged files before each commit.",
                                          f'{C("scripts/eslint-autofix.sh")} · conflicts with {C("code-style")}', marks=["problem"],
                                          states=[("Conflict", "conflict")], sel=True) + \
           bd2.item(LIME, "code-style", "skill", "How I want TypeScript written: naming, imports, error handling, no default exports.",
                    f'{C(".claude/skills/code-style/SKILL.md")} · defers to <em>the client’s ESLint config</em>', marks=["note"]) + '</ol>'
    marks = f'<div class="btnrow">{bd2.mark(LIME, "problem")}{bd2.mark(LIME, "note")}{bd2.mark(LIME, "skipped")}{bd2.mark(LIME, "checked")}</div>'
    btns = f'<div class="btnrow"><span class="btn primary">{ic(LIME, "arrow_export_ltr")}Export…</span><span class="btn">{ic(LIME, "options")}Configure</span><span class="btn danger-ghost">Remove eslint-autofix…</span></div>'
    return f'<div class="theme-light slice ml">{rows}<div style="height:var(--s4)"></div>{marks}{btns}</div>'


def contrast_table():
    out = []
    for title, rs in (("Dark — the product", contrast.rows()), ("Light — the slice", contrast.rows(".theme-light"))):
        trs = []
        for r in rs:
            verdict = ('<span class="na">—</span>' if r["bar"] == 1.0 else
                       (f'<span class="ok">pass</span>' if r["pass"] else '<span class="bad">fail</span>'))
            trs.append(f'<tr><td><span class="smp" style="background:{r["bgv"]};color:{r["fgv"]}">Aa</span></td>'
                       f'<td><code>--{r["fg"]}</code> {r["fgv"]}</td><td><code>--{r["bg"]}</code> {r["bgv"]}</td>'
                       f'<td class="n">{r["ratio"]:.2f}</td><td>{verdict}</td><td>{r["what"]}{" · bar 3:1" if r["bar"] == 3.0 else ""}</td></tr>')
        out.append(f'<p class="lab" style="margin-top:var(--s6)">{title}</p><div class="panelbox" style="padding:0;overflow:auto"><table class="ct">'
                   f'<thead><tr><th>Sample</th><th>Text</th><th>Background</th><th>Ratio</th><th>AA</th><th>Where</th></tr></thead>'
                   f'<tbody>{"".join(trs)}</tbody></table></div>')
    return "".join(out)


JS = r"""(function(){})();"""


def build():
    T.build()
    contrast.build()
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Concept · AI Stack Builder</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="tokens.css">
<style>{concept_ui.UI_CSS}{PAGE_CSS}</style></head>
<body class="ml">{bd4.symbols()}
<header class="wrap top">
  <h1>Mica · Lime</h1>
  <p>The visual language of AI Stack Builder — phase 06, stage 4. <b>A neutral Mica ground, one lime that only ever means “you can press this” or “you are here”, findings as tinted tags, and nothing that claims more than the product checked.</b> Every value on this page and on <a href="mica-lime.html">the screens</a> comes from <a href="tokens.css">tokens.css</a>. The road here — four rounds of directions and every decision — is in <code>concept.md</code>.</p>
  <nav class="jump" aria-label="On this page"><a href="#action">In use</a><a href="#colour">Colour</a><a href="#type">Type</a><a href="#form">Form</a><a href="#icons">Icons</a><a href="#components">Components</a><a href="#light">Light slice</a><a href="#contrast">Contrast</a><a href="mica-lime.html">The screens</a></nav>
</header>
<main class="wrap">
<section class="s" id="action" aria-labelledby="action-h"><h2 id="action-h">The style in use</h2>
  <p class="lead">A shared project’s card with the portrait of the person who shared it, the top bar, an active row with a Problem and an auto-added one with a Note, the buttons, and the head of the Export mode. All words from <code>microcopy.md</code>.</p>{hero()}</section>
<section class="s" id="colour" aria-labelledby="colour-h"><h2 id="colour-h">Colour</h2>
  <p class="lead">Each colour with the attribute or decision it follows from (<code>concept.md</code>, <i>Attributes</i> and <i>Working style</i>).</p>{colours()}</section>
<section class="s" id="type" aria-labelledby="type-h"><h2 id="type-h">Type — a pair and a scale</h2>
  <p class="lead">Two faces of one family. Nine roles; the step between neighbours is small because this is a working surface, and weight does the rest.</p>{typography()}</section>
<section class="s" id="form" aria-labelledby="form-h"><h2 id="form-h">Form — radius, spacing, shadow</h2>
  <p class="lead">Soft but not round: 6 px on controls, 10 on cut-outs, 14 on panels, 18 on the acrylic frame. Everything on a 4 px grid. Edges are hairlines; a shadow appears only where something is lifted or pressed.</p>{form()}</section>
<section class="s" id="icons" aria-labelledby="icons-h"><h2 id="icons-h">Icons — Lucide</h2>
  <p class="lead">One library, one stroke (1.75 px), three sizes by use. Never a coloured icon set; colour on an icon is the state it stands for.</p>{icons()}</section>
<section class="s" id="components" aria-labelledby="components-h"><h2 id="components-h">Three components</h2>
  <p class="lead">The three that carry the most of the product: the row where an item’s state is true, a stage of the check, and a field of the item form.</p>{components()}</section>
<section class="s" id="light" aria-labelledby="light-h"><h2 id="light-h">The light slice</h2>
  <p class="lead">Decided on 11 Oct: one small slice of light here, the full theme in phase 09. It caught one thing already — lime as a mark disappears on white (1.1:1), so light gets its own <code>--lime-mark #55700F</code> for the current place and the active row, while the button keeps the lime fill.</p>{light_slice()}</section>
<section class="s" id="contrast" aria-labelledby="contrast-h"><h2 id="contrast-h">Contrast — measured, not eyeballed</h2>
  <p class="lead"><code>tools/contrast.py</code> reads <code>tokens.css</code> as written, resolves the colour-mix boxes, and checks every text-on-surface pair the stand and the screens draw. AA: 4.5:1 for text, 3:1 for an icon or a mark that stands for a state. The same table is in <code>contrast.md</code>.</p>{contrast_table()}</section>
</main>
<p class="wrap foot">Built by <code>tools/build_concept.py</code> from <code>tools/concept_tokens.py</code> (tokens.css), <code>tools/concept_ui.py</code> (components) and <code>tools/contrast.py</code>. Icons: Lucide (ISC). Portrait: Jake Nackos on <a href="https://unsplash.com/photos/IF9TK5Uy-KI">Unsplash</a>.</p>
</body></html>'''
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}  {len(page)//1024} KB · page literals: {concept_ui.literals(PAGE_CSS) or 'none'}")


if __name__ == "__main__":
    build()
