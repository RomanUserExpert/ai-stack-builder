"""Phase 09, step 4: patterns — compositions of components that already stand on three screens or more.

    python -X utf8 tools/build_patterns.py

Writes design-system/patterns/<slug>.html, one file per pattern: the composition cut from a real wireframe page and
dressed by build_mockups.transform, linking design-system/index.css alone, with no style of its own. Its head comment
names the components it is made of and the three screens or more where it already stands.

**A pattern exists only if it can name three screens.** Each has a signature — a test on a wireframe page's markup —
and the build runs it over all 80 pages and fails if it finds fewer than three screens. A screen counts once however many
of its pages carry it, and an overlay (Item overlay, Import/export) never counts: it draws My library under itself, so it
would count one screen twice. What was looked at and fell short is REJECTED, with its count, so it is not proposed again
from scratch. The docs page, design-system/docs/patterns.html, is built by build_docs from PATTERNS and REJECTED.

Contributing (CLAUDE.md §18): a composition that is about to stand on its third screen enters here first, as an
entry in PATTERNS, and the third screen is drawn from it — never collected afterwards from screens that grew it by hand.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build_kit as bk  # noqa: E402
import build_mockups as bm  # noqa: E402

PAGES = ROOT / "04-wireframes" / "pages"
OUT = ROOT / "design-system" / "patterns"
OVERLAYS = {"Item overlay", "Import/export"}
SCREENS = [("sign-in", "Sign in"), ("sign-up", "Create account"), ("password-reset", "Reset password"),
           ("library-my", "My library"), ("library-public", "Public library"), ("library-json", "Import/export"),
           ("item-", "Item overlay"), ("projects-", "Projects"), ("project-configuring", "Configuring"),
           ("project-detached", "Detached row"), ("project-", "Project"), ("run-shared-item", "Run shared item"),
           ("run-shared", "Run shared project"), ("run-item", "Run single item"), ("run-", "Run project"),
           ("shared-item", "Shared item"), ("shared-project", "Shared project")]


def screen(page):
    return next(s for pre, s in SCREENS if page.startswith(pre))


def pages():
    return {p.stem: re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)
            for p in sorted(PAGES.glob("*.html")) if p.stem != "wireframes"}


def dialogs(h):
    out, i = [], 0
    while True:
        try:
            d = bk.outer(h, "dialog", 'class="modal"', n=i)
        except SystemExit:
            return out
        out.append(d)
        i += 1


def ordered(h, *classes, span=20000):
    """The classes appear in this order, each within `span` characters of the last."""
    pos = 0
    for k, c in enumerate(classes):
        m = re.compile(rf'class="{c}"').search(h, pos)
        if not m or (k and m.start() - pos > span):
            return False
        pos = m.end()
    return True


# slug, name, signature, source page, what to cut (tag, attribute text) — siblings taken in order, the wrapper they
# stand in, the components it is made of (docs names), when to take the pattern, when to take the components instead
PATTERNS = [
    dict(slug="browse-head", name="Browse head",
         sig=lambda h: ordered(h, "page-head", "find", span=4000),
         source="projects-default", cut=[("div", 'class="page-head"'), ("form", 'class="find"')],
         wrap='<main class="app-main">{}</main>',
         parts=["Page head", "Search field", "Filters button and popover"],
         when="The top of a place that holds a collection a person searches and narrows: the name and the one act, then a "
              "search and one Filters button, right above the list or the grid.",
         instead="A place that holds one thing — a project, a shared item — takes the Page head alone: there is nothing "
                 "to search. A filter by kind is Tabs, under this head, not inside it."),
    dict(slug="set-with-side-panel", name="Set with an item side panel",
         sig=lambda h: 'class="with-drawer"' in h,
         source="project-item", cut=[("div", 'class="with-drawer"')],
         wrap='<main class="app-main">{}</main>',
         parts=["Row list", "Set row states (§7)", "Item side panel", "Close"],
         when="A project's set with one item opened beside it: the rows stay where they are, the open one carries the "
              "pill, and the panel holds what can be done to that item — Detach, Reset, Promote.",
         instead="Editing the library original is the Item sheet over My library, not this. A list whose rows open "
                 "nothing beside them is the Row list alone."),
    dict(slug="configuring-layout", name="Configuring layout",
         sig=lambda h: 'class="config-layout"' in h,
         source="project-configuring-default", cut=[("div", 'class="config-layout"')],
         wrap="{}",
         parts=["Library panel", "Scope switch", "Tabs", "Search field", "Add to set", "Page head", "Row list",
                "Remove from set"],
         when="The configuring mode: the library panel on the left reads and adds, the set on the right shows what is in "
              "it and removes. One fact in two places — membership shown in the panel, owned by the row.",
         instead="Viewing a project is the set alone, with no panel and no ✕: a row being read is not a row being "
                 "changed (Q21). Keeping and editing items is My library, not the panel."),
    dict(slug="run-report", name="Run report",
         sig=lambda h: ordered(h, "summary", "stage-group", "export-stage"),
         source="run-default", cut=[("main", 'class="app-main"')],
         wrap="{}",
         parts=["Run summary", "Check stages", "Finding box", "File block", "Export stage", "Button"],
         when="The Export mode's body, on every Run: the verdict line with its counts, the stages grouped as Findings "
              "and Handover, and the Export stage last — the irreversible step read after everything it depends on.",
         instead="A single finding outside Run is a Finding box on its own; a list of facts with no verdict is a Plain "
                 "list. Never put Export beside the check as a button: it is the last stage (§8)."),
    dict(slug="confirmation", name="Confirmation",
         sig=lambda h: any('class="form-actions"' in d and 'class="field' not in d for d in dialogs(h)),
         source="projects-delete", cut=[("div", 'class="scrim"'), ("dialog", 'class="modal"')],
         wrap="{}",
         parts=["Dialog", "Form actions", "Button"],
         when="Before a step that cannot be walked back or that publishes: the veil, the sheet, a head that names the "
              "thing, the consequence in the present tense, then Cancel … the act — red only when it removes.",
         instead="An unclean export is confirmed inside the Export stage, not here. A step that can be undone needs no "
                 "dialog at all."),
    dict(slug="dialog-with-field", name="Dialog with a field",
         sig=lambda h: any('class="form-actions"' in d and 'class="field' in d for d in dialogs(h)),
         source="project-detached-promote", cut=[("div", 'class="scrim"'), ("dialog", 'class="modal"')],
         wrap="{}",
         parts=["Dialog", "Text field", "Form actions", "Button"],
         when="A dialog that asks for one value before it acts, or hands one over: the name of a promoted item, a link to "
              "copy. The field sits 16 px under the head, the act after it.",
         instead="More than a field or two is the Item sheet. A dialog that only names a consequence is a Confirmation."),
]

REJECTED = [
    ("Kind tabs over a row list", "My library, Public library — and Item overlay and Import/export, which draw My library "
     "under themselves. Two places."),
    ("Receiver's content with an aside", "Shared project, Shared item. Two screens."),
    ("A sheet over a place", "Item overlay. One screen."),
    ("Empty or error state with its action", "Seven screens, but it is one component, Empty and error state, not a "
     "composition of several."),
    ("Our failure box with its action", "Fourteen screens, but it is one component, the Finding box's neutral variant."),
    ("The door", "Sign in, Create account, Reset password — one component, Door form."),
    ("The Filters popover", "My library, Public library, Projects — one component, Filters button and popover."),
]


def count(pat, all_pages):
    found = {}
    for n, h in all_pages.items():
        if pat["sig"](h):
            found.setdefault(screen(n), []).append(n)
    return {s: v for s, v in found.items() if s not in OVERLAYS}, {s: v for s, v in found.items() if s in OVERLAYS}


def fragment(pat, all_pages):
    src = all_pages[pat["source"]]
    return pat["wrap"].format("\n".join(bk.outer(src, tag, attr, page=pat["source"]) for tag, attr in pat["cut"]))


def page(pat, frag, screens, overlays):
    lines = [f"Pattern: {pat['name']}. Generated by tools/build_patterns.py; do not edit by hand.",
             f"Made of: {', '.join(pat['parts'])}. No style of its own: design-system/index.css only.",
             f"Stands on {len(screens)} screens: " + "; ".join(f"{s} ({', '.join(v)})" for s, v in screens.items()) + ".",
             f"Cut from: 04-wireframes/pages/{pat['source']}.html."]
    if overlays:
        lines.append("Also drawn under: " + ", ".join(overlays) + " (overlays, not counted).")
    head = "\n".join("  " + l for l in lines)
    src = f"""<!DOCTYPE html>
<!--
{head}
-->
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{pat['name']} · Pattern</title>
  <link rel="stylesheet" href="wireframe.css">
</head>
<body class="product-page">
{frag}
</body>
</html>
"""
    out = bm.transform(src, "../../", f"pattern-{pat['slug']}", [], kit_href=["../index.css"], frame=False)
    return re.sub(r"<title>(.*?) — design</title>", r"<title>\1</title>", out)


def build():
    all_pages = pages()
    OUT.mkdir(parents=True, exist_ok=True)
    short, report = [], []
    for pat in PATTERNS:
        screens, overlays = count(pat, all_pages)
        if len(screens) < 3:
            short.append(f"{pat['name']}: {len(screens)} screens ({', '.join(screens)})")
            continue
        if screen(pat["source"]) not in screens:
            short.append(f"{pat['name']}: its source page {pat['source']} does not carry its signature")
        frag = fragment(pat, all_pages)
        (OUT / f"{pat['slug']}.html").write_text(page(pat, frag, screens, overlays), encoding="utf-8")
        pat["screens"], pat["overlays"], pat["fragment"] = screens, overlays, frag
        report.append(f"{pat['name']} ({len(screens)})")
    if short:
        raise SystemExit("patterns that are not patterns — fewer than three screens:\n  " + "\n  ".join(short)
                         + "\nA composition on fewer screens stays on its screens — CLAUDE.md §18, Contributing to the system.")
    stale = {p.name for p in OUT.glob("*.html")} - {f"{p['slug']}.html" for p in PATTERNS}
    for f in stale:
        (OUT / f).unlink()
    print(f"patterns: {len(PATTERNS)} — " + " · ".join(report))
    return PATTERNS


if __name__ == "__main__":
    build()
