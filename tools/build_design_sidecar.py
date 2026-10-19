"""Phase 07, step 1: the .impeccable/design.json sidecar, written from DESIGN.md.

impeccable reads it next to DESIGN.md: components as self-contained snippets (var() from
06-concept/tokens.css), shadows and motion that the DESIGN.md frontmatter cannot hold, and the
narrative pulled verbatim from DESIGN.md. Re-run whenever DESIGN.md changes.

    python tools/build_design_sidecar.py
"""
import json, datetime, re, sys

TOK = dict(re.findall(r"^\s*--([\w-]+):\s*(.*?);", open("06-concept/tokens.css", encoding="utf-8").read().split("\n.theme-light {")[0], re.M))

DESIGN = open('DESIGN.md', encoding='utf-8').read()

ca = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="8" y2="12"/><line x1="12" x2="12.01" y1="16" y2="16"/></svg>'
info = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>'
srch = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>'
upl = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" x2="12" y1="3" y2="15"/></svg>'
btn = ("display:inline-flex;align-items:center;gap:var(--s2);height:var(--control-h);padding:0 var(--s3);"
       "font:var(--t-button);border-radius:var(--r-sm);border:var(--hairline) solid;cursor:pointer;"
       "transition:background var(--dur) var(--ease)")
focus = "outline:0;box-shadow:var(--shadow-focus)"


def button(cls, label, bg, edge, fg, hover_bg, extra="", icon=""):
    css = (f".{cls}{{{btn};background:var({bg});border-color:var({edge});color:var({fg}){extra}}} "
           f".{cls}:hover{{background:var({hover_bg});border-color:var({hover_bg})}} "
           f".{cls}:focus-visible{{{focus}}}")
    return f'<button class="{cls}">{icon}{label}</button>', css


comps = []
for name, ref, desc, args in [
    ("Primary Button", "button-primary", "The one action per screen: lime fill, lime ink. Never a verdict.",
     ("ds-btn-primary", "Export", "--lime", "--lime", "--on-lime", "--lime-hover", ";font-weight:600", upl)),
    ("Warning Button", "button-warning", "Going ahead despite a Problem: the cost named, never celebrated in lime.",
     ("ds-btn-warning", "Export with 1 problem", "--warning", "--warning", "--on-warning", "--warning-hover")),
    ("Danger Button", "button-danger", "Only the confirmation of a removal. Hover darkens.",
     ("ds-btn-danger", "Remove from project", "--danger", "--danger", "--on-danger", "--danger-hover")),
]:
    html, css = button(*args)
    comps.append({"name": name, "kind": "button", "refersTo": ref, "description": desc, "html": html, "css": css})

html, css = button("ds-btn", "Configure", "--control", "--line-strong", "--text", "--control-hover")
css = css.replace(".ds-btn:hover{background:var(--control-hover);border-color:var(--control-hover)}",
                  ".ds-btn:hover{background:var(--control-hover)}")
comps.insert(1, {"name": "Secondary Button", "kind": "button", "refersTo": "button-secondary",
                 "description": "Every other action. Controls stay grey.", "html": html, "css": css})

comps += [
    {"name": "Search Field", "kind": "input", "refersTo": "search-field",
     "description": "A recessed well with a hairline edge; the lime ring on focus.",
     "html": f'<label class="ds-search">{srch}<input placeholder="Search projects"></label>',
     "css": (".ds-search{display:flex;gap:var(--s2);align-items:center;width:var(--col-l);height:var(--control-h);padding:0 var(--s3);"
             "background:var(--well-deep);border:var(--hairline) solid var(--control-edge);border-radius:var(--r-sm);color:var(--text-3)} "
             ".ds-search input{flex:1;border:0;background:transparent;color:var(--text);font:var(--t-small);outline:0} "
             ".ds-search input::placeholder{color:var(--text-3)} "
             ".ds-search:focus-within{border-color:var(--lime-mark);box-shadow:var(--shadow-focus)}")},
    {"name": "Top Bar Navigation", "kind": "nav", "refersTo": "nav-place-current",
     "description": "Three places as text; the current one is a raised tile.",
     "html": '<nav class="ds-nav"><a href="#">My library</a><a href="#">Public library</a><a href="#" aria-current="page">Projects</a></nav>',
     "css": (".ds-nav{display:flex;gap:calc(var(--s1) / 2);padding:var(--s2);background:var(--bar)} "
             ".ds-nav a{display:flex;align-items:center;height:var(--control-h);padding:0 var(--s3);border-radius:var(--r-sm);"
             "color:var(--text-2);text-decoration:none;font:var(--t-button)} "
             ".ds-nav a:hover{color:var(--text);background:var(--hover-wash)} "
             ".ds-nav a[aria-current=page]{color:var(--text);background:var(--raised);box-shadow:var(--shadow-tile)} "
             f".ds-nav a:focus-visible{{{focus}}}")},
    {"name": "Kind Tag and Finding Capsules", "kind": "chip", "refersTo": "finding-mark-problem",
     "description": "Kind as an outlined pill; Conflict beside the name; Problem and Note as tinted capsules with icon and word.",
     "html": (f'<div class="ds-tags"><span class="ds-tag">script</span><span class="ds-tag ds-tag-conflict">Conflict</span>'
              f'<span class="ds-mark ds-mark-problem">{ca}Problem</span><span class="ds-mark ds-mark-note">{info}Note</span></div>'),
     "css": (".ds-tags{display:flex;gap:var(--s2);align-items:center} "
             ".ds-tag{display:inline-flex;align-items:center;height:var(--tag-h);padding:0 var(--s2);font:var(--t-micro);color:var(--text-2);"
             "border-radius:var(--r-pill);box-shadow:inset 0 0 0 var(--hairline) var(--line-strong)} "
             ".ds-tag-conflict{color:var(--problem);background:var(--problem-wash);box-shadow:inset 0 0 0 var(--hairline) var(--problem-edge)} "
             ".ds-mark{display:inline-flex;align-items:center;gap:var(--s1);height:var(--mark-h);padding:0 var(--s3) 0 var(--s2);"
             "font:var(--t-micro);font-weight:var(--weight-strong);border-radius:var(--r-pill)} "
             ".ds-mark-problem{color:var(--problem);background:var(--problem-wash)} "
             ".ds-mark-note{color:var(--note);background:var(--note-wash)}")},
    {"name": "Item Row in its Cut-out", "kind": "custom", "refersTo": "row-cutout",
     "description": "The signature: every item pressed into its own cut-out inside a tray; the active one raised, with a lime pill.",
     "html": ('<ul class="ds-tray"><li class="ds-row"><b>code-style</b> <span class="ds-k">skill</span>'
              '<p>How I want TypeScript written.</p><code>.claude/skills/code-style/SKILL.md</code></li>'
              '<li class="ds-row ds-row-active"><b>eslint-autofix</b> <span class="ds-k">script</span>'
              '<p>Runs ESLint with --fix on staged files.</p><code>scripts/eslint-autofix.sh</code></li></ul>'),
     "css": (".ds-tray{list-style:none;margin:0;display:flex;flex-direction:column;gap:var(--s2);padding:var(--s2);"
             "background:var(--tray);border-radius:var(--r-lg);width:var(--modal-w)} "
             ".ds-row{position:relative;padding:var(--s3) var(--s4);background:var(--cutout);border-radius:var(--r-md);"
             "box-shadow:var(--shadow-cutout);font:var(--t-body);color:var(--text);transition:background var(--dur) var(--ease)} "
             ".ds-row:hover{background:var(--row-hover)} .ds-row b{font-weight:var(--weight-strong)} "
             ".ds-row p{margin:calc(var(--s1) / 2) 0 0;font:var(--t-small);color:var(--text-2)} .ds-row code{font:var(--t-code);color:var(--text-3)} "
             ".ds-k{font:var(--t-micro);color:var(--text-2);padding:0 var(--s2);border-radius:var(--r-pill);"
             "box-shadow:inset 0 0 0 var(--hairline) var(--line-strong)} "
             ".ds-row-active{background:var(--raised)} "
             ".ds-row-active::before{content:'';position:absolute;left:var(--s1);top:var(--s3);bottom:var(--s3);"
             "width:var(--pill-w);border-radius:var(--r-xs);background:var(--lime-mark)}")},
]

# narrative pulled verbatim from DESIGN.md
ov = DESIGN.split('## Overview', 1)[1].split('## Colors', 1)[0]
paras = [p.strip() for p in ov.split('\n\n') if p.strip()]
overview = '\n\n'.join(p for p in paras[1:4])
keys = re.findall(r'^- (.+(?:\n  .+)*)', ov.split('**Key Characteristics:**', 1)[1], re.M)
keys = [' '.join(k.split()) for k in keys]
rules = []
for sec in ['Colors', 'Typography', 'Elevation & Depth']:
    body = DESIGN.split(f'## {sec}', 1)[1].split('\n## ', 1)[0]
    for name, text in re.findall(r'\*\*The (.+?) Rule\.\*\* (.+?)(?=\n\n|\Z)', body, re.S):
        rules.append({"name": f"The {name} Rule", "body": ' '.join(text.split()),
                      "section": {'Colors': 'colors', 'Typography': 'typography', 'Elevation & Depth': 'elevation'}[sec]})
dd = DESIGN.split("## Do's and Don'ts", 1)[1].split('## Sources', 1)[0]
do_part, dont_part = dd.split("### Don't:", 1)
bullets = lambda s: [' '.join(b.split()) for b in re.findall(r'^- (.+(?:\n  .+)*)', s, re.M)]

data = {
    "schemaVersion": 2,
    "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
    "title": "Design System: AI Stack Builder",
    "extensions": {
        "colorMeta": {
            "lime": {"role": "primary", "displayName": "Signal Lime"},
            "mica-ground": {"role": "neutral", "displayName": "Mica Ground",
                            "tonalRamp": ["#161714", "#181916", "#1B1C19", "#1E1F1B", "#232420", "#2A2B27", "#2E302A", "#383A33"]},
            "text": {"role": "neutral", "displayName": "Ink", "tonalRamp": ["#A1A49A", "#C5C7BE", "#F3F4EF"]},
            "problem": {"role": "state", "displayName": "Problem Rose"},
            "note": {"role": "state", "displayName": "Note Amber"},
            "warning": {"role": "state", "displayName": "Warning Amber"},
            "danger": {"role": "state", "displayName": "Remove Red"},
            "checked": {"role": "state", "displayName": "Checked"},
        },
        "typographyMeta": {
            "display": {"displayName": "Display", "purpose": "A project's name, one per screen."},
            "title": {"displayName": "Title", "purpose": "The Export mode's verdict; an empty or error state's title."},
            "code": {"displayName": "Code", "purpose": "Paths, refs, step numbers, durations, file contents."},
        },
        # read from tokens.css, never typed here (phase 07 review, B-7)
        "shadows": [{"name": f"shadow-{n}", "value": TOK[f"shadow-{n}"], "purpose": w} for n, w in (
            ("cutout", "A row pressed into its tray."), ("tile", "The current place; a lifted segment."),
            ("sheet", "A dialog, a popover or the Item sheet over the page."), ("focus", "Keyboard focus."))],
        "motion": [{"name": n, "value": TOK[n], "purpose": w} for n, w in (
            ("ease", "Every state transition."), ("dur", "Hover and state changes."),
            ("dur-spin", "The spinners; stopped under reduced motion."), ("dur-shimmer", "Skeleton shimmer; stopped under reduced motion."))],
    },
    "components": comps,
    "narrative": {
        "northStar": "The Inspector's Report",
        "overview": overview,
        "keyCharacteristics": keys,
        "rules": rules,
        "dos": bullets(do_part),
        "donts": bullets(dont_part),
    },
}
json.dump(data, open('.impeccable/design.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(len(comps), 'components;', len(rules), 'rules;', len(keys), 'keys;', len(data['narrative']['dos']), 'dos;', len(data['narrative']['donts']), 'donts')
