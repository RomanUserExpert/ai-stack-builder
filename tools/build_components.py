"""Phase 08, step 3: the kit's classes, one file per component -> 08-design-tokens/components/.

    python -X utf8 tools/build_components.py          # writes components/*.css and components/index.css
    python -X utf8 tools/build_components.py --list   # which rule went to which file, nothing written

The source is the same as kit.css's: build_mockups.MOCK_CSS (the painted components), build_kit.KIT_CSS (the grey
ones) and the skeleton sizes. Each rule goes to the file of the component its selector names, keeping its order and
the comment above it. On the way, every colour variable becomes its role in 08-design-tokens/tokens.css: the same
value, a name that says what it is for. Where one phase-07 variable carried several roles (tokens-audit.md, M-1 …
M-15), the selector decides which role it is here. Geometry is not renamed: it reads the primitive directly.

Checks, and the build fails on any of them:
- a class holds a value of its own (hex, rgb(), px, a font name) — concept_ui.literals;
- a component reads a colour primitive (--color-*);
- a var() that tokens.css does not declare;
- a rule that no file claims;
- two rules whose order between files flipped, that set the same property at the same specificity.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build_mockups as bm  # noqa: E402
import build_kit  # noqa: E402
import concept_ui  # noqa: E402
import concept_tokens  # noqa: E402

TOKENS = ROOT / "08-design-tokens" / "tokens.css"
OUT = ROOT / "08-design-tokens" / "components"

# file, what it is (the header line), selectors it claims. First match wins, so the narrow ones come first.
FILES = [
    ("base", "the page itself: reset, ground, selection, scrollbars, the hidden helpers", [
        r"^\*$", r"^html$", r"^body", r"^a$", r"^h1,h2,h3", r"^ul,ol$", r"^::selection", r"^\.visually-hidden",
        r"^\.canvas", r"::-webkit-scrollbar", r"^svg\.sprite", r"^a\.check,a\.search,a\.pick", r"^a\.check>input", r"^@supports"]),
    ("icon", "an icon, and the product's mark", [r"^svg\.icon$", r"^\.icon\.logo"]),
    ("code", "machine text: inline code and a file block", [r"^code$", r"^pre\.file"]),
    ("button", "buttons: secondary, primary, quiet, danger, warning, the muted remove, the link-button, the ✕", [
        r"^button", r"^\.button", r":is\(button,\.button\)", r"^\.link-button", r"^\.remove"]),
    ("tag", "a kind tag, a state tag, and the finding capsules beside a row", [r"^\.tag", r"^\.marks", r"^\.mark"]),
    ("glyph", "the finding glyphs, the Checked dot, the spinner, a severity word", [
        r"^\.glyph", r"^svg\.glyph", r"^span\.glyph", r"^@keyframes mk-spin", r"^@media \(prefers-reduced-motion:reduce\)\{span\.glyph",
        r"^\.severity"]),
    ("frame", "the three bars, the places, the account, the main column", [
        r"^\.app-header", r"^\.app-nav", r"^img\.avatar", r"^\.app-main", r"^\.run-bar"]),
    ("page-head", "a page's head: title, actions, meta, description", [
        r"^\.page-head", r"^\.head-actions", r"^\.head-meta", r"^p\.meta\.head-meta", r"^\.meta", r"^\.description",
        r"^:is\(p,span\)\.meta\.error-code", r"^\.door-alt a:hover,a\.meta:hover"]),
    ("search", "search and the Filters button", [r"^\.find", r"^\.search", r"^\.filters-button"]),
    ("card", "a project card and its verdict", [r"^\.card", r"^\.verdict"]),
    ("row", "rows in a tray, each in its own cut-out; sub-rows; a row's facts and actions", [
        r"^\.row", r"^\.set-item", r"^\.sub-rows", r"^\.usage", r"^\.state-line"]),
    ("drawer", "the item beside the list", [r"^\.with-drawer", r"^\.drawer"]),
    ("callout", "a box attached to something: Problem, Note, the keys reminder, our failure", [r"^\.callout"]),
    ("select", "a select", [r"^select"]),
    ("run", "Run: the summary, the stages, the Export stage", [
        r"^\.summary", r"^\.stage-group", r"^\.stages", r"^\.stage-body", r"^\.export-stage", r"^\.export-actions",
        r"^\.plain-list"]),
    ("state", "empty, error and loading: the state block, its tile, the skeleton", [
        r"^\.state-block", r"^svg\.icon\.state-icon", r"^\.state-actions", r"^\.skeleton", r"^\.row-actions \.skeleton",
        r"^@keyframes mk-shimmer", r"^@media \(prefers-reduced-motion:reduce\)\{\.skeleton", r"^\.sk-"]),
    ("sidebar", "the configuring mode's library sidebar and its panel", [r"^\.config-layout", r"^\.library-sidebar", r"^\.panel"]),
    ("segmented", "the scope switch: a track with its current segment lifted", [r"^\.scope"]),
    ("tabs", "tabs, in the panel and at page size", [r"^\.tabs"]),
    ("checkbox", "a checkbox and a radio, drawn for the dark", [r"^input\[type=\"checkbox\"\]", r"^input\[type=\"radio\"\]"]),
    ("check", "Add / In this project: an icon button over a hidden checkbox", [r"^\.check"]),
    ("dialog", "the veil, a dialog, the Filters popover, the Item sheet", [
        r"^\.scrim", r"^dialog", r"^\.sheet-head", r"^\.popover", r"^fieldset", r"^legend"]),
    ("form", "a form: fields, a section, a file list, a dropzone, its actions, progress", [
        r"^\.form", r"^\.field", r"^\.file-list", r"^\.dropzone", r"^\.attach", r"^progress"]),
    ("door", "the door: the signed-out page", [r"^\.door"]),
    ("aside", "the receiver's aside", [r"^\.with-aside", r"^\.aside-box"]),
    ("library-version", "the original of a detached field", [r"^\.library-version"]),
    ("heading", "a small heading", [r"^h2\.heading-small"]),
]
ORDER = [f for f, _, _ in FILES]
# exceptions the first-match rule gets wrong: a rule whose selector starts with one component and belongs to another
OWNER = {
    ".row h2 a:hover,.row h3 a:hover,.card h2 a:hover,.callout a:hover": "row",
    ".row .facts code,.usage code,.callout code,.state-line code": "row",
    ".button-primary span.glyph-running": "button",
    ".panel-body .state-block": "sidebar",
    ".panel-body .row-list": "sidebar",
    ".panel .search": "sidebar",
    ".drawer-head .close,.sheet-head .close": "drawer",
    ".file-list .link-button": "form",
    "dialog.modal .callout": "dialog",
    "dialog.modal .field": "dialog",
    ".library-version summary .link-button": "library-version",
    ".library-version pre.file": "library-version",
    ".card .row-actions": "card",
    ".callout .row-actions": "callout",
}

# a phase-07 colour variable -> its role here. One name: the same everywhere. A list: the first rule whose selector
# matches decides (tokens-audit.md, the M rows). A colour the audit kept as one role keeps its name.
ROLES = {
    "lime": [(r"^\.button-primary", "action"), (r"^input\[type=\"(checkbox|radio)\"\]:checked", "control-on"),
             (r"^\.icon\.logo", "brand")],
    "lime-hover": "action-hover",
    "on-lime": "on-action",
    "lime-mark": [(r":focus-(visible|within)", "focus"), (r".", "mark")],
    "lime-selection": "selection",
    "on-lime-track": "on-action-track",
    "raised": [(r"^\.row-list>li:has\(> \.is-selected\)$", "selected"),
               (r"^\.(app-nav|tabs) a\[aria-current=\"page\"\]$", "current"), (r".", "raised")],
    "control": [(r"^button\[disabled\]", "disabled"), (r"^code$", "code-chip"), (r"^svg\.icon\.state-icon", "tile"),
                (r".", "control")],
    "line": [(r"^button\[disabled\]", "disabled-edge"), (r".", "line")],
    "text-3": [(r"^button\[disabled\]|^\.check:has\(input:(checked:)?disabled\)", "disabled-text"),
               (r"^\.(search|dropzone):hover$|^\.field input:not\(\[type=\"checkbox\"\]\):not\(\[type=\"radio\"\]\):hover", "edge-hover"),
               (r".", "text-3")],
    "text-2": [(r"^input\[type=\"checkbox\"\]:hover,input\[type=\"radio\"\]:hover$", "edge-hover"), (r".", "text-2")],  # T3-1
    "bar": [(r"^\.library-sidebar", "side"), (r".", "bar")],
    "tray": [(r"^\.state-block$", "state-ground"), (r".", "tray")],
    "cutout": [(r"^\.callout-reminder,\.callout-failure$", "neutral-box"), (r".", "cutout")],
}
COLOUR_PRIMITIVE = re.compile(r"var\(--color-[\w-]+\)")


def units(css):
    """Top-level rules and @-blocks in order, each with the comment written just above it."""
    out, i, pending = [], 0, []
    while i < len(css):
        if css[i].isspace():
            i += 1
            continue
        if css.startswith("/*", i):
            j = css.index("*/", i) + 2
            pending.append(css[i:j])
            i = j
            continue
        j, depth = css.index("{", i), 0
        k = j
        while True:
            depth += {"{": 1, "}": -1}.get(css[k], 0)
            k += 1
            if depth == 0:
                break
        head = " ".join(css[i:j].split())
        notes = [c for c in pending if not re.match(r"/\*\s*(---|=====)", c)]
        out.append({"head": head, "text": css[i:k], "notes": notes})
        pending = []
        i = k
        while i < len(css) and css[i] in " \t":          # a comment on the same line belongs to this rule
            i += 1
        if css.startswith("/*", i) and "\n" not in css[i:css.index("*/", i)]:
            j = css.index("*/", i) + 2
            out[-1]["tail"] = css[i:j]
            i = j
    return out


def owner(head, text=""):
    if head.startswith("@"):
        head = " ".join(text.split())  # an @-block is known by what it holds
    if head in OWNER:
        return OWNER[head]
    for f, _, pats in FILES:
        if any(re.search(p, head) for p in pats):
            return f
    return None


def role(var, selector):
    r = ROLES.get(var)
    if r is None:
        return var
    if isinstance(r, str):
        return r
    for pat, name in r:
        if re.search(pat, selector):
            return name
    raise SystemExit(f"--{var} in {selector}: no role")


# geometry a rule wrote as a count of a primitive -> the primitive that names it (tokens-check.md, T5). Longest first:
# a measure built on --s12 * 3 must not be caught by a dialog's --s12 * 3.
GEOMETRY = [
    ("calc(var(--measure) - var(--s12) * 3)", "var(--search-w)"),
    ("calc(var(--measure) + var(--s12) * 4)", "var(--callout-measure)"),
    ("calc(100vh - var(--s12) * 6)", "calc(100vh - var(--popover-reserve))"),
    ("calc(var(--s12) * 2 + var(--s6))", "var(--door-top)"),
    ("calc((var(--s12) - var(--icon-l)) / 2)", "var(--state-icon-inset)"),
    ("calc(var(--s12) * 3)", "var(--modal-top)"),
    ("calc(var(--s10) * 4)", "var(--textarea-min-h)"),
    ("calc(var(--s1) / 2 - var(--hairline))", "calc(var(--s-half) - var(--hairline))"),
    ("calc(var(--s1) / 2)", "var(--s-half)"),
    ("calc(var(--s1) * -0.5)", "calc(var(--s-half) * -1)"),
    ("calc(var(--s2) - var(--hairline) * 2)", "calc(var(--s2) - var(--hairline-2))"),
    ("calc(var(--hairline) * 2)", "var(--hairline-2)"),
    ("calc(var(--hairline) * 1)", "var(--hairline)"),
]
# a primitive times or over a count; a sign flip (* -1) is not a count
COUNT = re.compile(r"\*\s*(?!-1\b)-?\d|/\s*\d")


def rename(unit):
    """Every colour variable in the rule -> its role, decided by the rule's own selector."""
    if unit["head"].startswith("@"):
        return unit["text"]
    sel = unit["head"]
    body = re.sub(r"var\(--([\w-]+)\)", lambda m: f"var(--{role(m.group(1), sel)})", unit["text"])
    for old, new in GEOMETRY:
        body = body.replace(old, new)
    for old, new in REWRITE.get(sel, []):
        if old not in body:
            raise SystemExit(f"{sel}: the rewrite no longer matches its source — {old}")
        body = body.replace(old, new)
    return concept_tokens.rename08(body)   # phase 08's primitive names (Q47)


# three rules that change form, not look (tokens-audit.md): the build fails if a source drifts from what they expect
REWRITE = {
    # V-5: the native controls' scheme follows the theme
    "html": [("color-scheme:dark", "color-scheme:var(--scheme)")],
    # V-12: the tick was a picture with --on-lime's hex inside it, which no theme can reach. It is a mask now,
    # painted in --control-on-ink, at the same size and place: 12 px in the middle of the 14 px inside the edge
    'input[type="checkbox"]:checked': [(
        "background:var(--control-on) var(--glyph-check) center / calc(var(--icon) - var(--s1)) no-repeat;",
        "background:var(--control-on);"),
        ("}", '}\ninput[type="checkbox"]:checked::before{content:"";display:block;width:calc(var(--icon) - var(--s1));'
              "height:calc(var(--icon) - var(--s1));margin:calc(var(--s-half) - var(--hairline));background:var(--control-on-ink);"
              "-webkit-mask:var(--glyph-check) center / contain no-repeat;mask:var(--glyph-check) center / contain no-repeat}")],
    # V-2: the door's column was a number times the spacing unit
    ".door": [("width:calc(var(--s1) * 100)", "width:var(--door-w)")],
}


def split_top(sel):
    """A selector list split on its top-level commas (not the ones inside :is() or :not())."""
    out, depth, cur = [], 0, ""
    for ch in sel:
        depth += {"(": 1, ")": -1}.get(ch, 0)
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    return out + [cur.strip()]


def specificity(sel):
    """(ids, classes, elements). :is()/:not()/:has() count as their most specific argument."""
    def arg(m):
        return " " + max(split_top(m.group(2)), key=specificity).replace(" ", "")
    while re.search(r":(not|is|has)\(", sel):
        sel = re.sub(r":(not|is|has)\(((?:[^()]|\([^()]*\))*)\)", arg, sel)
    ids = len(re.findall(r"#[\w-]+", sel))
    cls = len(re.findall(r"\.[\w-]+|\[[^\]]*\]|(?<!:):(?!:)[\w-]+", sel))
    els = len(re.findall(r"(?:^|[\s>+~])([a-z][\w-]*)", sel)) + len(re.findall(r"::[\w-]+", sel))
    return (ids, cls, els)


def decls(text):
    body = text[text.index("{") + 1:text.rindex("}")]
    return {d.split(":", 1)[0].strip(): d.split(":", 1)[1].strip() for d in re.split(r";(?![^(]*\))", body) if ":" in d}


def subjects(sel):
    """The last compound, as (element or None, classes, pseudo-element), once per :is() alternative."""
    sel = re.sub(r":(not|has)\((?:[^()]|\([^()]*\))*\)", "", sel)
    m = re.search(r":is\(((?:[^()]|\([^()]*\))*)\)", sel)
    if m:
        return [s for alt in split_top(m.group(1)) for s in subjects(sel[:m.start()] + alt + sel[m.end():])]
    pseudo = re.search(r"::([\w-]+)", sel)
    sel = re.sub(r"::?[\w-]+(\([^)]*\))?", "", re.sub(r"\[[^\]]*\]", "", sel))
    part = re.split(r"[\s>+~]+", sel.strip())[-1]
    el = re.match(r"[a-z][\w-]*", part)
    return [(el.group(0) if el else None, set(re.findall(r"\.([\w-]+)", part)), pseudo.group(1) if pseudo else None)]


def shares(a, b):
    """Could the two selectors land on one element? Same pseudo-element, compatible element types, and a common
    class — or no class on one side, so only the element type decides."""
    for ea, ca, pa in subjects(a):
        for eb, cb, pb in subjects(b):
            if pa != pb or (ea and eb and ea != eb):
                continue
            if ca & cb or not ca or not cb:
                return True
    return False


def flips(all_units, placed):
    """Pairs whose order changed between files and that could fight: the same element, the same property set to a
    different value, at the same specificity — the only case where moving a rule to another file changes a pixel."""
    pos = {id(u): n for n, u in enumerate(all_units)}
    new = {id(u): (ORDER.index(placed[id(u)]), pos[id(u)]) for u in all_units}
    out = []
    plain = [u for u in all_units if not u["head"].startswith("@")]
    for a in plain:
        da = decls(a["text"])
        for b in plain:
            if not (pos[id(a)] < pos[id(b)] and new[id(a)] > new[id(b)]):
                continue
            db = decls(b["text"])
            fight = sorted(p for p in set(da) & set(db) if da[p] != db[p])
            if not fight:
                continue
            for sa in split_top(a["head"]):
                for sb in split_top(b["head"]):
                    if specificity(sa) == specificity(sb) and shares(sa, sb):
                        out.append((sa, sb, fight))
    return sorted(set((a, b, tuple(f)) for a, b, f in out))


def in_dom(pairs):
    """Of the candidate pairs, the ones where some element on a real page matches both selectors. :hover and the
    like are taken as true (they can happen to anything), and the pseudo-element must be the same. Every mockup,
    every flow step, and the showcase."""
    from playwright.sync_api import sync_playwright

    def static(s):
        s = re.sub(r"::?(hover|focus-visible|focus-within|focus|active)\b", "", s)
        return re.sub(r"::[\w-]+(\([^)]*\))?$", "", s).strip() or "*"
    pages = [ROOT / "07-ui-assembly" / "ui" / "kit.html", *sorted((ROOT / "04-wireframes" / "mockups").glob("*.html")),
             *sorted((ROOT / "04-wireframes" / "mockups" / "flows").rglob("*.html"))]
    js = "pairs => pairs.map(([a, b]) => { const B = new Set(document.querySelectorAll(b)); return [...document.querySelectorAll(a)].some(e => B.has(e)); })"
    real = {}
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page()
        for f in pages:
            pg.goto(f.as_uri(), wait_until="domcontentloaded")
            hits = pg.evaluate(js, [[static(a), static(b)] for a, b, _ in pairs])
            for (a, b, fight), hit in zip(pairs, hits):
                if hit:
                    real.setdefault((a, b, fight), f.relative_to(ROOT).as_posix())
        br.close()
    return real


def source():
    body = re.sub(r"^\s*/\* mockup\.css.*?\*/\s*", "", bm.MOCK_CSS, flags=re.S)
    return body.strip() + "\n" + build_kit.KIT_CSS + build_kit.skeleton_css()


def build(write=True):
    all_units = units(source())
    placed, files, lost = {}, {f: [] for f in ORDER}, []
    for u in all_units:
        f = owner(u["head"], u["text"])
        if f is None:
            lost.append(u["head"])
            continue
        placed[id(u)] = f
        files[f].append(u)
    if lost:
        raise SystemExit("rules no component claims:\n  " + "\n  ".join(lost))
    fought = flips(all_units, placed)
    tokens = TOKENS.read_text(encoding="utf-8")
    declared = set(re.findall(r"^\s*--([\w-]+):", tokens, re.M))
    problems, out = [], {}
    for f, desc, _ in FILES:
        lines = [f"/* {f}.css — {desc}.", "   Generated by tools/build_components.py from the kit's sources; do not edit by hand.",
                 "   Colour through a role in tokens.css; geometry straight from a primitive. */", ""]
        for u in files[f]:
            text = rename(u)
            lines += u["notes"]
            lines.append(text + (" " + u["tail"] if u.get("tail") else ""))
            for v in set(re.findall(r"var\(--([\w-]+)\)", text)):
                if v not in declared:
                    problems.append(f"{f}.css: --{v} is not in tokens.css")
            if COLOUR_PRIMITIVE.search(text):
                problems.append(f"{f}.css: a colour primitive read directly in {u['head']}")
            # T5: geometry is a primitive, not a count of one — the skeleton sizes are kept on purpose (T5-4)
            if not u["head"].startswith(".sk-") and any(COUNT.search(c) for c in re.findall(r"calc\((?:[^()]|\([^()]*\))*\)", text)):
                problems.append(f"{f}.css: geometry written as a count in {u['head']}")
        out[f] = "\n".join(lines) + "\n"
        bad = concept_ui.literals(out[f])
        if bad:
            problems.append(f"{f}.css holds values of its own: {bad}")
    if problems:
        raise SystemExit("components/ fails:\n  " + "\n  ".join(problems))
    index = ["/* components/index.css — every component, in the kit's order. Link tokens.css first, then this. */"]
    index += [f'@import url("{f}.css");' for f in ORDER]
    if write:
        OUT.mkdir(parents=True, exist_ok=True)
        for f in ORDER:
            (OUT / f"{f}.css").write_text(out[f], encoding="utf-8")
        (OUT / "index.css").write_text("\n".join(index) + "\n", encoding="utf-8")
    return files, fought


if __name__ == "__main__":
    files, fought = build(write="--list" not in sys.argv)
    for f in ORDER:
        print(f"{f:16} {len(files[f]):3} rules")
    print(f"{sum(len(v) for v in files.values())} rules in {len(ORDER)} files")
    print(f"{len(fought)} pairs changed order and could fight on paper; checking them on every page")
    real = in_dom(fought) if fought else {}
    for (a, b, p), where in real.items():
        print(f"  ORDER FLIP on a real element: [{a}] now after [{b}] on {', '.join(p)} — {where}")
    if real:
        sys.exit(1)
