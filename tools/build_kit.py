"""Phase 07, step 3: the UI kit — the shell and the showcase. Phase 08, step 4: no kit.css any more.

    python tools/build_kit.py

Writes, into 07-ui-assembly/ui/:

- shell.html — the three shells as markup, for the grey screens to take: app header, shared header
              (door · receiver), Run bar.
- kit.html  — the showcase: every component of ui/inventory.md with its states.

Both link 08-design-tokens/tokens.css and components/index.css, as every mockup does. KIT_CSS below is the
source of the grey components (their look from DESIGN.md), and build_mockups.MOCK_CSS of the painted ones;
tools/build_components.py turns both into one file per component. Until phase 08 they were written into one
flat kit.css, which git keeps (last in d6d419a).

Nothing on the showcase is typed by hand except its own labels (class kit-*): every component is cut
out of a wireframe page, so its words are the page's, and the pages match microcopy.md line for line
(lesson 05, step 7). Then the page goes through build_mockups.transform — the same icons, glyphs,
portrait and tones as the mockups.
"""
from pathlib import Path
import html as htmllib
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build_mockups as bm  # noqa: E402
import concept_ui  # noqa: E402

PAGES = ROOT / "04-wireframes" / "pages"
OUT = ROOT / "07-ui-assembly" / "ui"
MICROCOPY = ROOT / "05-tone-of-voice" / "microcopy.md"

# ------------------------------------------------------------------ the grey components' source
KIT_CSS = r"""
/* ===== grey in the mockups: structure from the wireframe, look from DESIGN.md (phase 07, step 3) ===== */

/* a text field and a textarea: a label over a Deep Well, the search field's material */
.form{display:flex;flex-direction:column;gap:var(--s4)}
.field{display:flex;flex-direction:column;gap:var(--s1)}
.field>span:first-child{font:var(--t-micro);font-weight:var(--weight-strong);color:var(--text-2)}
.field-label{display:flex;justify-content:space-between;align-items:baseline}
.field-label .meta{font-weight:var(--weight-regular)}
.field .hint{font:var(--t-micro);font-weight:var(--weight-regular);color:var(--text-3)}
.field input:not([type="checkbox"]):not([type="radio"]),.field textarea{width:100%;height:var(--control-h);padding:0 var(--s3);
  font:var(--t-small);color:var(--text);background:var(--well-deep);border:var(--hairline) solid var(--control-edge);border-radius:var(--r-sm);outline:0;
  transition:border-color var(--dur) var(--ease),box-shadow var(--dur) var(--ease)}
.field input:not([type="checkbox"]):not([type="radio"]):hover,.field textarea:hover{border-color:var(--text-3)}
.field input::placeholder,.field textarea::placeholder{color:var(--text-3)}
.field input:not([type="checkbox"]):not([type="radio"]):focus-visible,.field textarea:focus-visible{border-color:var(--lime-mark);box-shadow:var(--shadow-focus)}
.field textarea{height:auto;min-height:calc(var(--s10) * 4);padding:var(--s2) var(--s3);font:var(--t-code);resize:vertical}
.field select{width:100%}

/* busy: the spinner inside a primary button turns dark on lime */
.button-primary span.glyph-running{border-color:var(--on-lime-track);border-top-color:var(--on-lime)}

/* remove from set: the ✕ on a set row — quiet, square, named by its aria-label */
.remove{width:var(--control-h);padding:0;background:transparent;border-color:transparent}
.remove:hover{background:var(--control-hover)}

/* the door: the signed-out page, one column */
.door{width:calc(var(--s1) * 100);margin:calc(var(--s12) * 2 + var(--s6)) auto 0;display:flex;flex-direction:column;gap:var(--s6)}
.door h1{font:var(--t-display);letter-spacing:var(--track-display)}
.door .head-meta{display:block;font:var(--t-body);color:var(--text-2)}
.door-alt{padding-top:var(--s4);border-top:var(--hairline) solid var(--line);font:var(--t-small);color:var(--text-2);text-align:center}
.door-alt a{color:var(--text)}

/* the receiver's aside: what their machine still needs, and the way to take it */
.with-aside{display:grid;grid-template-columns:minmax(0,1fr) var(--col-xl);gap:var(--s8);align-items:start}
.aside-box{position:sticky;top:var(--s4);display:flex;flex-direction:column;gap:var(--s3);padding:var(--s5);background:var(--raised);border:var(--hairline) solid var(--line);border-radius:var(--r-lg)}
.aside-box h2{font:var(--t-heading);letter-spacing:var(--track-heading)}
.aside-box .meta{font:var(--t-small);color:var(--text-2)}
.aside-box .button{align-self:flex-start}

/* page tabs: the panel's tabs at page size */
.tabs-page a{font:var(--t-button)}

/* the original of a detached field — one-off (Detached row), styled here because a screen holds no style:
   a quiet disclosure, the library's version in a file block under it */
.library-version summary{display:flex;align-items:center;gap:var(--s1);cursor:pointer;list-style:none;font:var(--t-small);color:var(--text-3)}
.library-version summary::-webkit-details-marker{display:none}
.library-version summary::before{content:"";width:var(--icon-s);height:var(--icon-s);flex:none;background:var(--text-3);
  -webkit-mask:var(--icon-chevron) center / contain no-repeat;mask:var(--icon-chevron) center / contain no-repeat;transition:transform var(--dur) var(--ease)}
.library-version[open] summary::before{transform:rotate(90deg)}
.library-version summary .link-button{margin:0;padding:0 var(--s1)}
.library-version summary:focus-visible{outline:0;box-shadow:var(--shadow-focus);border-radius:var(--r-xs)}
.library-version pre.file{margin-top:var(--s2)}

/* the Item sheet: the add/edit overlay over the Library — a side sheet, the item's whole form (group 1, phase 07) */
dialog.sheet{position:fixed;top:0;right:0;bottom:0;left:auto;width:var(--sheet-w);max-width:none;max-height:none;height:auto;margin:0;padding:var(--s8);
  overflow:auto;display:flex;flex-direction:column;gap:var(--s6);color:var(--text);background:var(--raised);border:0;border-left:var(--hairline) solid var(--sheet-edge);box-shadow:var(--shadow-sheet)}
.form-section{display:flex;flex-direction:column;gap:var(--s4);padding-top:var(--s5);border-top:var(--hairline) solid var(--line)}
.form-section>h3{font:var(--t-label);letter-spacing:var(--track-label);text-transform:uppercase;color:var(--text-3)}
.field-row{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:var(--s4)}
.file-list{display:flex;flex-direction:column;margin-bottom:var(--s2);border-top:var(--hairline) solid var(--line)}
.file-list li{display:flex;gap:var(--s3);align-items:center;padding:var(--s2) 0;border-bottom:var(--hairline) solid var(--line);font:var(--t-small)}
.file-list .meta{margin-left:auto}
.dropzone{display:flex;flex-direction:column;align-items:center;gap:var(--s2);padding:var(--s8) var(--s6);text-align:center;cursor:pointer;
  font:var(--t-small);color:var(--text-2);background:var(--well-deep);border:var(--hairline) dashed var(--control-edge);border-radius:var(--r-md);
  transition:border-color var(--dur) var(--ease)}
.dropzone:hover{border-color:var(--text-3)}
.dropzone:focus-within{border-color:var(--lime-mark);box-shadow:var(--shadow-focus)}
.dropzone strong{color:var(--text);font-weight:var(--weight-strong)}
.dropzone-small{padding:var(--s4);gap:var(--s1)}
.attach{align-self:flex-start}

/* a small heading: the shared item's content title (group 4) */
h2.heading-small{font:var(--t-body);font-weight:var(--weight-strong)}

/* the icon sprite every page carries: out of the flow */
svg.sprite{position:absolute}

/* progress: the import's bar — a native <progress>, the count above it says the same in words */
progress.progress{-webkit-appearance:none;appearance:none;display:block;width:100%;height:var(--s2);margin-top:var(--s2);border:0;border-radius:var(--r-pill);background:var(--control);overflow:hidden}
progress.progress::-webkit-progress-bar{background:var(--control);border-radius:var(--r-pill)}
progress.progress::-webkit-progress-value{background:var(--lime-mark);border-radius:var(--r-pill)}
progress.progress::-moz-progress-bar{background:var(--lime-mark);border-radius:var(--r-pill)}

/* the keys reminder: not a finding (§11) — so no Problem rose and no Note amber, a neutral box */
.callout-reminder,.callout-failure{background:var(--cutout);box-shadow:inset 0 0 0 var(--hairline) var(--line-strong)}
.callout-reminder>.severity,.callout-failure>.severity{color:var(--text)}
/* our failure is not a finding either (critique #5): the same neutral box; its code is mono, Ink 3 */

/* a stage that started and broke — not one that waits (critique #22) */
svg.glyph-stopped{color:var(--text-2)}

/* the Export stage's number, as the other stages carry theirs (critique #27); the archive's name in mono (#15) */
.export-stage h2 .n{font-family:var(--mono);font-weight:var(--weight-regular);color:var(--text-3)}
.export-stage h2 code{font:inherit;font-family:var(--mono);background:none;padding:0}
.export-stage .meta code{background:none;padding:0;color:inherit}
.field-mono input:not([type="checkbox"]):not([type="radio"]){font:var(--t-code)}
/* code inside a button takes the button's colour: no Ink on lime (audit #3) */
:is(button,.button) code{color:inherit;background:none;padding:0}
/* a file's name inside a stage's name: mono, but no chip in a heading-like line */
.stages summary .name code{font:inherit;font-family:var(--mono);background:none;padding:0}

/* a path or an item name keeps together on a narrow row (critique #14, review G01-5); inline code in a row's
   lines is bare, as in its facts (review G34-10, G01-20) */
.row .facts code,.usage code,.callout code,.state-line code{white-space:nowrap}
.usage code,.state-line code{background:none;padding:0}

/* hover where it was missing (critique #11, #40; review G01-18, B-21) */
.row h2 a:hover,.row h3 a:hover,.card h2 a:hover,.callout a:hover{text-decoration:underline}
.popover-group label{cursor:pointer}
.popover-group label:hover{color:var(--text)}
/* a disabled control does not answer the pointer, whatever its tone (review B-18) */
button[disabled]:hover,.button[aria-disabled="true"]:hover{background:var(--control);border-color:var(--line);color:var(--text-3)}
/* the file list's remove sits inside its row (review F10) */
.file-list .link-button{margin:0;padding:0 0 0 var(--s2)}
/* a long popover scrolls inside itself; its head and foot stay (review G01-12) */
.popover-body{max-height:calc(100vh - var(--s12) * 6);overflow:auto}
button.link-button:hover{background:none;color:var(--text)}
.door-alt a:hover,a.meta:hover{color:var(--text);text-decoration:underline;text-decoration-thickness:calc(var(--hairline) * 2)}
.library-version summary:hover{color:var(--text-2)}
.library-version summary:hover::before{background:var(--text-2)}

/* an auto-added row refuses, and looks it: no hover, the tick in Ink 3 (critique #2, §8) */
.check:has(input:disabled){color:var(--text-3);cursor:default}
.check:has(input:disabled) input{cursor:default}
.check:has(input:disabled):hover{background:transparent}
.check:has(input:checked:disabled)::before{background:var(--text-3)}

/* busy: cannot be sent twice, keeps its lime; the spinner's track shows on lime (critique #12) */
.button-primary[aria-busy="true"]{cursor:progress}
.button-primary[aria-busy="true"]:hover{background:var(--lime);border-color:var(--lime)}

/* a dialog's field sits below its title (critique #46) */
dialog.modal .field{margin-top:var(--s4)}
"""


def skeleton_css():
    """The skeletons' sizes, which the wireframes give inline, as kit classes — every size any page uses."""
    seen = set()
    for f in sorted(PAGES.glob("*.html")):
        for m in re.finditer(r'class="skeleton"[^>]*?style="([^"]*)"', f.read_text(encoding="utf-8")):
            if "linear-gradient" not in m.group(1):  # the import's progress bar, see bm.progress
                seen.update(bm.skeleton_parts(m.group(1)))
    order = {"width": 0, "height": 1, "margin-top": 2}
    rules = []
    for prop, val in sorted(seen, key=lambda pv: (order[pv[0]], pv[1].endswith("%"), int(pv[1].rstrip("px%")))):
        v = f"calc(var(--s1) * {int(val[:-2]) // 4})" if val.endswith("px") else val
        if val.endswith("px") and int(val[:-2]) % 4:
            raise SystemExit(f"a skeleton size off the 4 px scale: {val}")
        rules.append(f".{bm.skeleton_class(prop, val)}{{{prop}:{v}}}")
    return "\n/* skeleton sizes: the wireframes' inline sizes as classes (phase 07, step 5 — no style on a screen) */\n" + "\n".join(rules) + "\n"


# ------------------------------------------------------------------ cutting components out of the pages
def outer(src, tag, attr="", contains=None, n=0, page="?"):
    """The outer HTML of the n-th <tag> whose start tag holds `attr` and whose markup holds `contains`."""
    seen = 0
    for m in re.finditer(rf"<{tag}\b[^>]*>", src):
        if attr and attr not in m.group(0):
            continue
        depth, pos = 1, m.end()
        for t in re.finditer(rf"<{tag}\b[^>]*>|</{tag}>", src[m.end():]):
            depth += -1 if t.group(0).startswith("</") else 1
            if depth == 0:
                pos = m.end() + t.end()
                break
        frag = src[m.start():pos]
        if contains and contains not in frag:
            continue
        if seen == n:
            return frag
        seen += 1
    raise SystemExit(f"not found: <{tag} {attr}> containing {contains!r} on {page}")


_cache = {}
_nfrag = [0]


def raw(page, tag, attr="", contains=None, n=0):
    """An element as the page has it, comments out — links and ids untouched."""
    if page not in _cache:
        _cache[page] = (PAGES / f"{page}.html").read_text(encoding="utf-8")
    return re.sub(r"\s*<!--.*?-->", "", outer(_cache[page], tag, attr, contains, n, page), flags=re.S)


def shell_source():
    """The three shells (four headers) as wireframe markup — what shell.html shows and every mockup is framed in."""
    return {"app": raw("project-default", "header", 'class="app-header"'),
            "door": raw("sign-in-default", "header", 'class="shared-header"'),
            "receiver": raw("shared-project-default", "header", 'class="shared-header"'),
            "run": raw("run-default", "header", 'class="run-bar"')}


def cut(page, tag, attr="", contains=None, n=0, wrap="{}"):
    frag = raw(page, tag, attr, contains, n)
    _nfrag[0] += 1
    k = f"k{_nfrag[0]}-"
    # ids are per page; on one showcase they must not collide
    frag = re.sub(r'\b(id|for|aria-labelledby|aria-describedby|aria-controls)="([^"]+)"',
                  lambda m: f'{m.group(1)}="' + " ".join(k + v for v in m.group(2).split()) + '"', frag)
    frag = re.sub(r'href="[^"#]*\.html(#[^"]*)?"', 'href="#"', frag)
    frag = re.sub(r'\s(action)="[^"]*"', "", frag)
    return wrap.format(frag)


def state(label, *frags, note=""):
    n = f'<p class="kit-note">{note}</p>' if note else ""
    return f'<div class="kit-state"><p class="kit-label">{label}</p>{n}<div class="kit-demo">{"".join(frags)}</div></div>'


def stage(*frags):
    """A dialog or a popover needs a place to hang in."""
    return f'<div class="kit-stage"><div class="scrim"></div>{"".join(frags)}</div>'


def comp(name, cls, screens, painted, *states):
    return (f'<section class="kit-comp" id="c-{re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")}">'
            f'<header class="kit-comp-head"><h3>{name}</h3><p class="kit-meta"><code>{cls}</code> · {screens}</p></header>{"".join(states)}</section>')
    # every screen is dressed since phase 07 step 7, so "painted / grey" no longer tells anything (review B-24)


RL = '<ol class="row-list">{}</ol>'
ICON = '<span class="icon" aria-hidden="true"></span>'


def components():
    g = {}
    g["Navigation"] = [
        comp("App header", "app-header · app-nav · account", "8 screens", "painted",
             state("Projects is the current place", cut("project-default", "header", 'class="app-header"')),
             state("Public library is the current place", cut("library-public-default", "header", 'class="app-header"')),
             state("My library is the current place", cut("library-my-default", "header", 'class="app-header"'),
                   note="Hover a place for the wash; Tab for the focus ring.")),
        comp("Shared header", "shared-header · owner", "7 screens", "grey",
             state("Door — the mark only", cut("sign-in-default", "header", 'class="shared-header"')),
             state("Receiver — Shared by, with the sharer's portrait", cut("shared-project-default", "header", 'class="shared-header"'))),
        comp("Run bar", "run-bar · back · title · pick", "4 screens", "painted",
             state("Default", cut("run-default", "header", 'class="run-bar"'),
                   note="The same in every Run state: loading, exporting, exported, error.")),
        comp("Breadcrumb", "app-main > p.meta", "3 screens", "painted",
             state("Default", cut("project-default", "p", 'class="meta"', contains="Projects</a> /"))),
        comp("Page head", "page-head · head-meta · head-actions", "10 screens", "painted",
             state("Project: head actions, the primary last", cut("project-default", "div", 'class="page-head"')),
             state("Projects: one action", cut("projects-default", "div", 'class="page-head"')),
             state("Shared project: the Shared tag after the title", cut("shared-project-default", "div", 'class="page-head"')),
             state("Loading: skeleton meta", cut("project-loading", "div", 'class="page-head"'))),
        comp("Tabs", "tabs · tabs-page · count", "7 screens", "painted (panel tabs) · grey (page tabs)",
             state("Page tabs, with counts", cut("library-my-default", "nav", 'class="tabs tabs-page"')),
             state("A count of 0", cut("library-public-default", "nav", 'class="tabs tabs-page"')),
             state("Loading — no counts yet", cut("library-my-loading", "nav", 'class="tabs tabs-page"')),
             state("Panel tabs: Related first and current", cut("project-configuring-default", "nav", 'class="tabs"'),
                   note="One line; it scrolls rather than wraps.")),
        comp("Scope switch", "scope", "3 screens", "painted",
             state("My library current", cut("project-configuring-default", "nav", 'class="scope"', wrap='<div class="kit-narrow">{}</div>')),
             state("Public library current", cut("project-configuring-public", "nav", 'class="scope"', wrap='<div class="kit-narrow">{}</div>'))),
        comp("Library panel", "config-layout · library-sidebar · panel-head · panel-body", "3 screens", "painted",
             state("Default", cut("project-configuring-default", "aside", 'class="panel library-sidebar"', wrap='<div class="kit-panel">{}</div>')),
             state("Empty — No items in My library yet", cut("project-configuring-empty", "aside", 'class="panel library-sidebar"', wrap='<div class="kit-panel">{}</div>')),
             state("Loading", cut("project-configuring-loading", "aside", 'class="panel library-sidebar"', wrap='<div class="kit-panel">{}</div>')),
             state("No match", cut("project-configuring-error-filtered", "aside", 'class="panel library-sidebar"', wrap='<div class="kit-panel">{}</div>')),
             state("Just added — the row at once, what it requires after the round trip", cut("project-configuring-loading-add", "aside", 'class="panel library-sidebar"', wrap='<div class="kit-panel">{}</div>')),
             state("Public library — each item with its origin", cut("project-configuring-public", "aside", 'class="panel library-sidebar"', wrap='<div class="kit-panel">{}</div>'))),
    ]
    g["Cards and lists"] = [
        comp("Row list", "row-list > row · row-tight · set-item · row-compact", "8 screens", "painted (set rows, panel rows) · grey (library rows)",
             state("Library rows, with usage facts", cut("library-my-default", "li", contains='class="usage', n=0, wrap=RL), cut("library-my-default", "li", contains='class="usage', n=1, wrap=RL)),
             state("Set rows", cut("project-default", "li", contains="test-runner", wrap=RL), cut("project-default", "li", contains="changelog-writer", n=0, wrap=RL)),
             state("Active — the item open beside the set", cut("project-detached-default", "li", contains="is-selected", wrap=RL)),
             state("Loading", cut("project-loading", "ol", 'class="row-list"'))),
        comp("Item text block", "description · facts", "9 screens", "painted",
             state("Defers to", cut("project-default", "li", contains="code-style</a>", wrap=RL)),
             state("Pinned repo · licence · needs an env key", cut("project-default", "li", contains="github-mcp</a>", wrap=RL)),
             state("A detached row names the fields that differ", cut("project-default", "li", contains="pr-reviewer</a>", wrap=RL))),
        comp("Set row states (§7)", "sub-rows · tag-state · marks · state-line", "3 screens", "painted",
             state("Auto-added, nested under what pulled it in", cut("project-default", "li", contains="migration-reviewer</a><span", wrap=RL)),
             state("Conflicting", cut("project-default", "li", contains="eslint-autofix</a>", wrap=RL)),
             state("Configuring: Required by, and the remove", cut("project-configuring-default", "li", contains="Remove migration-reviewer", wrap=RL))),
        comp("Kind tag", "tag · tag-state", "10 screens", "painted",
             state("Kinds", '<div class="kit-row">' + "".join(f'<span class="tag">{k}</span>' for k in ("skill", "agent", "prompt", "mcp", "script", "app")) + '</div>'),
             state("States", '<div class="kit-row"><span class="tag">Shared</span> <span class="tag">Example</span> '
                   '<span class="tag tag-state">Conflict</span> <span class="tag tag-state">Auto-added</span> <span class="tag tag-state">Detached</span></div>')),
        comp("Usage facts", "usage", "3 screens", "grey",
             state("Default", cut("library-my-default", "li", contains="1 item requires this · requires", wrap=RL))),
        comp("Item side panel", "with-drawer · drawer · drawer-head · drawer-section · drawer-facts · drawer-actions", "3 screens", "painted",
             state("A linked item", cut("project-item", "aside", 'class="drawer"', wrap='<div class="kit-drawer">{}</div>')),
             state("A linked item with a Note", cut("project-configuring-item", "aside", 'class="drawer"', wrap='<div class="kit-drawer">{}</div>')),
             state("A detached item: Reset, Promote", cut("project-detached-default", "aside", 'class="drawer"', wrap='<div class="kit-drawer">{}</div>')),
             state("Loading", cut("project-detached-loading", "aside", 'class="drawer"', wrap='<div class="kit-drawer">{}</div>')),
             state("Our failure — Promote didn’t land", cut("project-detached-error", "aside", 'class="drawer"', wrap='<div class="kit-drawer">{}</div>')),
             state("One-off: the original of a detached field", cut("project-detached-default", "details", 'class="library-version"', wrap='<div class="kit-drawer">{}</div>'),
                   note="Detached row only; in the kit because a screen holds no style.")),
        comp("Check stages", "stage-group · stages · stage-body", "4 screens", "painted",
             state("Checked: note · problem (open) · skipped", cut("run-default", "section", 'class="stage-group"'),
                   note="A stage with something inside carries a chevron; one with nothing takes no focus."),
             state("Our failure: stopped, then not run", cut("run-error-check", "section", 'class="stage-group"')),
             state("Checking: running · waiting", cut("run-loading", "section", 'class="stage-group"'))),
        comp("Run summary", "summary", "4 screens", "painted",
             state("Checking", cut("run-loading", "section", 'class="summary"')),
             state("Checked, with counts", cut("run-default", "section", 'class="summary"')),
             state("Error, the code in mono", cut("run-error-check", "section", 'class="summary"'))),
        comp("Export stage", "export-stage · export-actions", "4 screens", "painted",
             state("Ready", cut("run-item-default", "section", 'class="export-stage"')),
             state("Ready, with a Problem", cut("run-default", "section", 'class="export-stage"')),
             state("Exporting", cut("run-loading-export", "section", 'class="export-stage"')),
             state("Exported", cut("run-success", "section", 'class="export-stage"')),
             state("Failed — our failure, neutral", cut("run-error-export", "section", 'class="export-stage"'))),
        comp("File block", "pre.file", "7 screens", "painted",
             state("SETUP.md", cut("run-default", "pre", 'class="file"', n=1))),
        comp("Plain list", "plain-list", "7 screens", "painted",
             state("Default", cut("shared-project-default", "ul", 'class="plain-list"'))),
        comp("Aside box", "with-aside · aside-box", "2 screens", "grey",
             state("Default", cut("shared-project-default", "aside", 'class="aside-box"', wrap='<div class="kit-aside">{}</div>')),
             state("Loading", cut("shared-project-loading", "aside", 'class="aside-box"', wrap='<div class="kit-aside">{}</div>'))),
    ]
    g["Forms"] = [
        comp("Button", "button · button-primary · button-quiet · button-danger · button-warning · button-danger-quiet", "17 screens", "painted · busy: grey",
             state("Primary · secondary · quiet", f'<div class="kit-row"><a class="button button-primary" href="#">{ICON}Export</a>'
                   f'<a class="button" href="#">Configure</a><button type="button">{ICON}Duplicate</button><a class="button button-quiet" href="#">Cancel</a></div>',
                   note="One primary per screen. Hover and Tab are live."),
             state("Danger — only a removal's confirmation", '<div class="kit-row"><button type="button" class="button button-primary">Delete</button>'
                   '<button type="button" class="button button-primary">Stop sharing</button></div>'),
             state("Warning — only Export with 1 problem", '<div class="kit-row"><button type="button" class="button button-primary">Export with 1 problem</button></div>'),
             state("Quiet danger — the remove inside a Problem", cut("run-default", "div", 'class="callout"', contains="Remove eslint-autofix")),
             state("Disabled — only Export on an empty project", f'<div class="kit-row"><button type="button" disabled title="Add an item first">{ICON}Export</button></div>'),
             state("Busy", cut("sign-in-loading", "button", 'type="submit"'))),
        comp("Link button", "link-button", "5 screens", "painted",
             state("Clear filters, in the popover's head", cut("projects-filters", "button", 'class="link-button"'))),
        comp("Search field", "find · search", "8 screens", "painted",
             state("Empty, with a placeholder", cut("projects-default", "label", 'class="search"')),
             state("Filled — the no-match state", cut("projects-error-filtered", "label", 'class="search"')),
             state("In the panel", cut("project-configuring-default", "label", 'class="search"'), note="Focus: the lime edge and ring.")),
        comp("Filters button and popover", "filters-button · find-zone · popover", "5 · 3 screens", "painted",
             state("Closed, one filter on", cut("projects-error-filtered", "form", 'class="find"')),
             state("Open", stage(cut("projects-filters", "section", 'class="find-zone"', wrap='<div class="kit-find">{}</div>')))),
        comp("Text field", "field · field-label", "5 screens", "painted (side panel) · grey (door, item form)",
             state("Empty, with a placeholder", cut("sign-in-default", "label", 'class="field"')),
             state("With an inline link", cut("sign-in-default", "label", 'class="field"', n=1)),
             state("Filled", cut("sign-in-error", "label", 'class="field"'))),
        comp("Select", "select", "5 screens", "painted (agent target) · grey (Kind)",
             state("Agent target", cut("run-default", "label", 'class="pick"')),
             state("Kind, in a field", cut("item-default", "label", 'class="field"', contains="<select"))),
        comp("Textarea", "field textarea", "2 screens", "painted (side panel) · grey (item form)",
             state("Empty, with a placeholder", cut("item-empty", "label", 'class="field"', contains="<textarea")),
             state("Filled", cut("item-default", "label", 'class="field"', contains="<textarea"))),
        comp("Add to set", "check", "3 screens", "painted",
             state("Auto-added — refuses: remove what requires it", cut("project-configuring-default", "label", 'class="check"', contains="disabled")),
             state("Not in the set · in the set", cut("project-configuring-default", "label", 'class="check"', contains="Add"),
                   ' ', cut("project-configuring-default", "label", 'class="check"', contains="checked"))),
        comp("Checkbox", "input[type=checkbox]", "3 screens", "painted",
             state("Unchecked · checked", cut("projects-filters", "fieldset", contains='type="checkbox"'))),
        comp("Radio", "input[type=radio]", "2 screens", "painted",
             state("Unselected · selected", cut("projects-filters", "fieldset", contains='type="radio"'))),
        comp("Remove from set", "remove", "2 screens", "painted",
             state("On a set row; absent on an auto-added one", cut("project-configuring-default", "button", 'class="remove"'),
                   note="Its aria-label names the item: Remove code-style from this project.")),
        comp("Close", "close", "5 screens", "painted",
             state("Default", cut("project-item", "a", 'class="button close"'))),
        comp("Form actions", "form-actions · push", "6 screens", "painted",
             state("Cancel … the primary pushed right", cut("library-json-default", "div", 'class="form-actions"'))),
        comp("Door form", "door · form · door-alt", "3 screens", "grey",
             state("Sign in", cut("sign-in-default", "section", 'class="door"')),
             state("Error", cut("sign-in-error", "section", 'class="door"')),
             state("Signing in", cut("sign-in-loading", "section", 'class="door"')),
             state("Reset password — sent", cut("password-reset-success", "section", 'class="door"'))),
    ]
    g["Feedback"] = [
        comp("Finding box", "callout · callout-quiet · severity", "11 screens", "painted (Problem, Note) · grey (reminder)",
             state("Problem", cut("run-default", "div", 'class="callout"', contains="declares a conflict")),
             state("Note", cut("run-default", "div", 'class="callout callout-quiet"')),
             state("Our failure — not a finding, so neutral", cut("run-error-setup", "div", 'role="alert"')),
             state("The keys reminder — not a finding", cut("library-json-default", "div", 'class="callout"', contains="carry no keys"))),
        comp("Finding capsule", "marks · mark", "3 screens", "painted",
             state("Problem · Note", '<div class="kit-row">', cut("project-default", "p", 'class="marks"', contains="glyph-problem"), cut("project-default", "p", 'class="marks"', contains="glyph-note"), '</div>')),
        comp("Severity glyph", "glyph-*", "9 screens", "painted",
             state("problem · note · checked · skipped · waiting · running · stopped",
                   '<div class="kit-row">' + "".join(f'<span class="kit-glyph"><span class="glyph glyph-{x}" aria-hidden="true"></span><span class="kit-label">{x}</span></span>'
                                                     for x in ("problem", "note", "checked", "skipped", "waiting", "running", "stopped")) + '</div>')),
        comp("Empty and error state", "state-block · state-image · state-icon · state-actions", "7 screens", "painted (Projects, Project) · grey (the rest)",
             state("Empty", cut("projects-empty", "section", 'class="state-block"')),
             state("No match", cut("projects-error-filtered", "section", 'class="state-block"')),
             state("Server error", cut("projects-error-server", "section", 'class="state-block"')),
             state("Dead link", cut("shared-project-error", "section", 'class="state-block"'))),
        comp("Skeleton", "skeleton", "10 screens", "painted",
             state("Loading", cut("projects-loading", "ol", 'class="card-grid"', wrap='<div class="kit-clip">{}</div>'),
                   note="Still under reduced motion.")),
        comp("Busy indicator", "glyph-running · role=status", "6 screens", "painted (Run)",
             state("Exporting", cut("run-loading-export", "p", 'role="status"', wrap='<div class="export-stage">{}</div>')),
             state("Importing — a progress bar under the count", cut("library-json-loading", "div", 'aria-busy="true"', wrap='<div class="kit-narrow">{}</div>'),
                   note="A native progress element; the count above says the same in words.")),
        comp("Dialog", "modal · sheet-head · scrim", "6 screens", "painted (confirms) · grey (import, promote)",
             state("Destructive confirm", stage(cut("projects-delete", "dialog", 'class="modal"'))),
             state("Disclosure confirm — Share", stage(cut("project-share", "dialog", 'class="modal"'))),
             state("Neutral confirm — Promote", stage(cut("project-detached-promote", "dialog", 'class="modal"'))),
             state("Import — the keys reminder", stage(cut("library-json-default", "dialog", 'class="modal"'))),
             state("Import — in progress", stage(cut("library-json-loading", "dialog", 'class="modal"'))),
             state("Import — failed", stage(cut("library-json-error", "dialog", 'class="modal"'))),
             state("Import — done", stage(cut("library-json-success", "dialog", 'class="modal"')))),
    ]
    g["One-off, styled in the kit"] = [
        comp("Item sheet", "dialog.sheet · sheet-head · form-section", "Item overlay",
             state("Edit db-migrate — the whole form, over My library", stage(cut("item-default", "dialog", 'class="sheet"')),
                   note="A side sheet the viewport's height; its body scrolls.")),
        comp("Two fields in a row", "field-row", "Item overlay",
             state("Requires · Conflicts with", cut("item-default", "div", 'class="field-row"'))),
        comp("File list", "file-list", "Item overlay",
             state("Two files, each removable", cut("item-default", "ul", 'class="file-list"', wrap='<div class="kit-narrow">{}</div>'))),
        comp("Drop zone", "dropzone · dropzone-small · attach", "Item overlay",
             state("Empty item", cut("item-empty", "label", 'class="dropzone', wrap='<div class="kit-narrow">{}</div>')),
             state("Below a file list — small", cut("item-default", "label", 'class="dropzone dropzone-small"', wrap='<div class="kit-narrow">{}</div>')),
             state("Attach a repo", cut("item-default", "button", 'class="attach"'))),
        comp("Small heading", "heading-small", "Shared item",
             state("Content · lands at", cut("shared-item-default", "h2", 'class="heading-small"'))),
    ]
    return g


# ------------------------------------------------------------------ the showcase's own frame
PAGE_CSS = r"""
.kit-page{min-height:100vh}
.kit-top{position:sticky;top:0;z-index:calc(var(--z-popover) + var(--z-sticky));display:flex;align-items:center;gap:var(--s6);height:var(--bar-h);padding:0 var(--s6);background:var(--bar);border-bottom:var(--hairline) solid var(--line)}
.kit-top strong{font:var(--t-body);font-weight:var(--weight-strong)}
.kit-top nav{display:flex;gap:var(--s4);font:var(--t-small)}
.kit-top nav a{color:var(--text-2);text-decoration:none}
.kit-top nav a:hover{color:var(--text)}
.kit-top .kit-theme{margin-left:auto}
.kit-body{display:flex;flex-direction:column;gap:var(--s12);padding:var(--s8);max-width:calc(var(--canvas) + var(--s12) * 3);margin:0 auto}
.kit-intro{max-width:var(--measure-wide);display:flex;flex-direction:column;gap:var(--s2);color:var(--text-2)}
.kit-intro h1{font:var(--t-display);letter-spacing:var(--track-display);color:var(--text)}
.kit-group{display:flex;flex-direction:column;gap:var(--s8)}
.kit-group>h2{font:var(--t-title);letter-spacing:var(--track-title);padding-bottom:var(--s3);border-bottom:var(--hairline) solid var(--line-strong)}
.kit-comp{display:flex;flex-direction:column;gap:var(--s4)}
.kit-comp-head h3{font:var(--t-heading);letter-spacing:var(--track-heading)}
.kit-meta{font:var(--t-micro);font-weight:var(--weight-regular);color:var(--text-3)}
.kit-meta code{background:none;padding:0;color:var(--text-2)}
.kit-state{display:grid;grid-template-columns:var(--col-m) minmax(0,1fr);gap:var(--s2) var(--s6);align-items:start}
.kit-label{font:var(--t-label);letter-spacing:var(--track-label);text-transform:uppercase;color:var(--text-3)}
.kit-note{grid-column:1;font:var(--t-micro);font-weight:var(--weight-regular);color:var(--text-3)}
.kit-state>.kit-label{grid-column:1}
.kit-demo{grid-column:2;grid-row:1 / span 2;display:flex;flex-direction:column;align-items:flex-start;gap:var(--s3);min-width:0}
.kit-demo>:is(ol,header,section,pre,.kit-clip,.kit-stage,.kit-row,.callout,.form-actions,.marks,div:not(.kit-narrow,.kit-panel,.kit-drawer,.kit-aside)){align-self:stretch}
.kit-demo>.search{width:calc(var(--measure) - var(--s12) * 3)}
.kit-demo>.field{width:calc(var(--side-w) - var(--s10))}
.kit-row{display:flex;gap:var(--s2);flex-wrap:wrap;align-items:center}
.kit-glyph{display:inline-flex;align-items:center;gap:var(--s1);margin-right:var(--s4)}
.kit-glyph .kit-label{text-transform:none;letter-spacing:normal}
.kit-demo>header{border:var(--hairline) solid var(--line);border-radius:var(--r-md)}
.kit-panel{width:var(--side-w);max-height:calc(var(--s12) * 12);overflow:auto;border:var(--hairline) solid var(--line);border-radius:var(--r-md)}
.kit-drawer,.kit-aside,.kit-narrow{width:var(--side-w)}
.kit-drawer .drawer,.kit-aside .aside-box{position:static}
.kit-clip{max-height:calc(var(--s12) * 8);overflow:hidden;border-radius:var(--r-lg)}
.kit-stage{position:relative;overflow:hidden;border-radius:var(--r-lg);background:var(--ground);border:var(--hairline) solid var(--line)}
.kit-stage dialog.modal{position:relative;top:auto;margin:var(--s8) auto}
.kit-stage dialog.sheet{position:relative;inset:auto;margin:0 0 0 auto;max-height:calc(var(--s12) * 14)}
.kit-stage:has(.popover){min-height:calc(var(--s12) * 15);max-width:calc(var(--col-xl) + var(--s12) * 4)}
.kit-find{position:absolute;top:var(--s6);right:var(--s6);display:flex;justify-content:flex-end}
.kit-find dialog.popover{position:absolute}
.kit-demo .door{margin:0;width:calc(var(--side-w) - var(--s10))}
.kit-demo>.export-stage{max-width:var(--measure)}
.kit-shell{display:flex;flex-direction:column;gap:var(--s8)}
.kit-shell .canvas{min-height:0;border:var(--hairline) solid var(--line);border-radius:var(--r-lg);overflow:hidden}
.kit-shell .app-main{min-height:calc(var(--s12) * 3);color:var(--text-3)}
"""


def page(title, desc, body, nav):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="stylesheet" href="wireframe.css">
  <style>{PAGE_CSS.strip()}</style>
</head>
<body class="product-page kit-page">
<header class="kit-top"><strong>{title}</strong><nav>{nav}</nav><button type="button" class="button-quiet kit-theme" onclick="var l=document.documentElement.getAttribute('data-theme')==='light';dsTheme(l?'dark':'light');this.textContent=l?'Light theme':'Dark theme'">Light theme</button><span class="kit-meta">{desc}</span></header>
{body}
</body>
</html>
"""


# phase 08: the showcase and the shell read what every mockup reads
TOKENS08 = ["../../08-design-tokens/tokens.css", "../../08-design-tokens/components/index.css"]


def finish(src, name, hrefs=TOKENS08):
    unknown = []
    out = bm.transform(src, "../../", name, unknown, kit_href=hrefs, frame=False)
    out = re.sub(r"<title>(.*?) — design</title>", r"<title>\1</title>", out)
    out = out.replace(" inert", "")  # a showcase shows its dialogs beside everything else
    bad = concept_ui.literals(re.search(r"<style>(.*?)</style>", out, re.S).group(1))
    if bad:
        raise SystemExit(f"{name}: the showcase's own styles hold values: {bad}")
    for p, ctx in unknown:
        print("  icon guessed (circle-dashed):", p, "…", ctx[-80:])
    return out


def shell_html():
    canvases = [
        ("App header", "The owner's places: My library · Public library · Projects. Put aria-current=\"page\" on the current one.",
         cut("project-default", "header", 'class="app-header"')),
        ("Shared header — door", "Sign in, Create account, Reset password: the mark only.",
         cut("sign-in-default", "header", 'class="shared-header"')),
        ("Shared header — receiver", "Shared project, Shared item and their Run: the sharer, no account.",
         cut("shared-project-default", "header", 'class="shared-header"')),
        ("Run bar", "The mode: back to where it was entered, the title, the agent target.",
         cut("run-default", "header", 'class="run-bar"')),
    ]
    body = ['<main class="kit-body"><div class="kit-intro"><h1>Shell</h1><p>The frame every screen sits in, as markup: '
            'a <code>.canvas</code>, one of these headers, and <code>&lt;main class="app-main"&gt;</code> for the screen. '
            'Grey screens take their frame from here.</p></div><div class="kit-shell">']
    for name, note, hdr in canvases:
        sid = re.sub(r"[^a-z]+", "-", name.lower()).strip("-")
        body.append(f'<section id="{sid}"><p class="kit-label">{name}</p><p class="kit-note">{note}</p>'
                    f'<div class="canvas">\n{hdr}\n<main class="app-main"><p class="kit-meta">the screen</p></main>\n</div></section>')
    body.append("</div></main>")
    nav = "".join(f'<a href="#{re.sub(r"[^a-z]+", "-", n.lower()).strip("-")}">{n}</a>' for n, _, _ in canvases) + '<a href="kit.html">Kit</a>'
    return finish(page("Shell", "07 · UI assembly", "".join(body), nav), "shell")


def kit_html():
    groups = components()
    n = sum(len(v) for v in groups.values())
    body = ['<main class="kit-body"><div class="kit-intro"><h1>UI kit</h1>'
            f'<p>{n} components: the 41 rows of <a href="inventory.md">the inventory</a> and the one-offs that need a class, every one with its states. Each component is cut from a wireframe page, '
            'so its words are the product\'s own (<code>microcopy.md</code>); the painted ones are drawn exactly as in the mockups, '
            'the grey ones take their look from <code>DESIGN.md</code>. Two stylesheets: <code>tokens.css</code>, the values on two levels, and <code>components/</code>, one file per component. '
            'The frame is on <a href="shell.html">the shell page</a>.</p></div>']
    nav = []
    for gname, comps in groups.items():
        gid = re.sub(r"[^a-z]+", "-", gname.lower()).strip("-")
        nav.append(f'<a href="#{gid}">{gname}</a>')
        body.append(f'<section class="kit-group" id="{gid}"><h2 class="kit-h">{gname} <span class="kit-meta">{len(comps)}</span></h2>{"".join(comps)}</section>')
    body.append("</main>")
    nav.append('<a href="shell.html">Shell</a>')
    return finish(page("UI kit", "07 · UI assembly", "".join(body), "".join(nav)), "kit"), n


# ------------------------------------------------------------------ every word is in microcopy.md
def words_check(out):
    """Each run of text on the showcase, outside its own kit-* labels, appears in microcopy.md."""
    mc = htmllib.unescape(MICROCOPY.read_text(encoding="utf-8")).replace("`", "")
    body = re.search(r"<body[^>]*>(.*)</body>", out, re.S).group(1)
    body = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
    body = re.sub(r"<style.*?</style>", "", body, flags=re.S)
    body = re.sub(r'<header class="kit-top">.*?</header>', "", body, flags=re.S)
    body = re.sub(r'<(p|span|h1|h2|h3|header)[^>]*class="kit-[^"]*"[^>]*>.*?</\1>', "", body, flags=re.S)
    body = re.sub(r'<div class="kit-intro">.*?</div>', "", body, flags=re.S)
    body = re.sub(r"<pre.*?</pre>", "", body, flags=re.S)  # generated files: their own table rows, line by line
    body = re.sub(r"<textarea.*?</textarea>", "", body, flags=re.S)  # a person's content, not the product's words
    missing = set()
    for chunk in re.split(r"<[^>]+>", body):
        t = re.sub(r"\s+", " ", htmllib.unescape(chunk)).strip(" ·,.—:()")
        if len(t) >= 3 and t not in mc:
            missing.add(t)
    return sorted(missing)


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "shell.html").write_text(shell_html(), encoding="utf-8")
    kit, n = kit_html()
    (OUT / "kit.html").write_text(kit, encoding="utf-8")
    missing = words_check(kit)
    print(f"kit: shell.html · kit.html ({n} components) · literals: none · words not in microcopy.md: {len(missing)}")
    for t in missing:
        print("  ", t)


if __name__ == "__main__":
    build()
