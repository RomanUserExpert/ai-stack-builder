"""Build the inventory table of 05-tone-of-voice/microcopy.md from the wireframe pages.

Lesson 05, step 1. Rows come from extract_copy.py; this groups them by screen, folds a line that
repeats across a screen's state pages into one row, decides whose words each line is, and applies the
marks defined below. Run from the repo root:

    python tools/build_microcopy.py > table.md   # then append it under microcopy.md's findings

The findings above the table in microcopy.md are written by hand from the marks; this script only
produces the table (its first line, a row count in a comment, is dropped). Once step 5 starts the table is edited by hand and this script is not re-run over
it.
"""
import re
import sys
from collections import OrderedDict, defaultdict

sys.path.insert(0, __file__.rsplit("\\", 1)[0].rsplit("/", 1)[0])
from extract_copy import rows  # noqa: E402

# page prefix → screen, in the order of the map (sitemap.md: the door, what I keep, what I assemble,
# what leaves, what somebody else opens). Longest prefix wins.
SCREENS = [
    ("sign-in", "Sign in"), ("sign-up", "Create an account"), ("password-reset", "Reset password"),
    ("library-my", "My library"), ("item", "Item — the add/edit overlay"),
    ("library-json", "Library — import and export as JSON"), ("library-public", "Public library"),
    ("projects", "Projects"), ("project-configuring", "Project — configuring the set"),
    ("project-detached", "Project — a detached row"), ("project", "Project"),
    ("run-item", "Run — a single item"), ("run-shared-item", "Run — a shared item"),
    ("run-shared", "Run — a shared project"), ("run", "Run"),
    ("shared-project", "Shared project"), ("shared-item", "Shared item"),
]
ORDER = ["Sign in", "Create an account", "Reset password", "My library", "Item — the add/edit overlay",
         "Library — import and export as JSON", "Public library", "Projects", "Project",
         "Project — configuring the set", "Project — a detached row", "Run", "Run — a single item",
         "Shared project", "Run — a shared project", "Shared item", "Run — a shared item"]


def screen_of(page):
    best = max((p for p, _ in SCREENS if page == p or page.startswith(p + "-")), key=len)
    return dict(SCREENS)[best], page[len(best) + 1:] or "default"


NOISE = re.compile(r"\d+|[\d.]+ s|—")          # stage numbers and durations: not copy
CHROME = ("App header", "Global nav")

PROJECTS = {"acme-billing-api", "agent-dotfiles", "docs-site-rewrite", "voice-notes-pipeline",
            "repo-triage-kit", "stripe-webhooks"}
PEOPLE = {"Maya Chen", "Maya", "maya@chen.dev", "maya-library-2026-09.json"}
DEFERS = {"the client’s ESLint config"}   # a defersTo value: the user's own words
PATH = re.compile(r"[\w.~-]*(/[\w.~-]+)+/?|[\w.-]+\.(md|sh|sql|mjs|js|ts|json)|\.[\w.]+")
FILTER_DATA = {"postgres", "migrations", "review", "docs", "typescript", "anthropics/skills",
               "modelcontextprotocol/servers", "github/github-mcp-server", "microsoft/playwright-mcp",
               "upstash/context7", "MIT", "Apache-2.0", "terraform", "linear", "sentry", "stripe"}


def build():
    raw = rows()
    items = {t for _, _, t, k, _ in raw if k == "item name"}
    descriptions = {t for _, _, t, k, _ in raw if k == "description"}
    user = items | PROJECTS | PEOPLE | FILTER_DATA | DEFERS | descriptions

    def whose(text, kind):
        if kind == "generated file":
            return "user" if text.startswith(("---", "#!")) else "generated"
        if kind in ("item name", "description", "value"):
            return "user"
        if kind == "placeholder":                       # an example the product wrote
            return "product"
        if text in user or (PATH.fullmatch(text) and kind not in ("stage name", "button")):
            return "user"
        parts = [p for p in re.split(r"\s*(?:·|,| @ |\+|/$)\s*", text) if p]
        if parts and all(p.strip("`") in user or p.startswith("`") and p.endswith("`")
                         or re.fullmatch(r"[\d.]+ ?KB", p) for p in parts):
            return "user"
        if "`" in text or any(re.search(r"(?<![\w-])" + re.escape(u) + r"(?![\w-])", text)
                              for u in items | PROJECTS | PEOPLE | DEFERS):
            return "product, with slots"
        return "product"

    # item → its descriptions, in page order, to catch one item described two ways (U1)
    desc_of, last, at = defaultdict(set), None, None
    for page, z, t, k, _ in raw:
        if page != at or k == "title":
            last, at = None, page
        if k in ("item name",) or (k == "link" and t in items):
            last = t
        elif k in ("description",) or (t in descriptions and last):
            desc_of[last].add(t)
    # The pairing above is positional and can drift onto the next item on a page with a dialog; these
    # nine were read by hand and are the real ones.
    u1_items = {"code-style", "db-migrate", "migration-reviewer", "postgres-mcp", "github-mcp",
                "pr-reviewer", "commit-conventions", "filesystem", "memory"}
    u1 = {d for it, ds in desc_of.items() if it in u1_items and len(ds) > 1 for d in ds}

    grouped = OrderedDict()
    for page, z, t, k, _ in raw:
        if NOISE.fullmatch(t) and k in ("body", "duration"):
            continue
        screen, state = screen_of(page)
        if z.split(" › ")[0] in CHROME or z in CHROME:
            screen, state = "Everywhere — the app header", page
        if k == "severity" and t not in ("Problem", "Note", "Skipped"):
            k = "status label"
        key = (screen, z, t, k)
        grouped.setdefault(key, []).append(state)
    return grouped, whose, u1, desc_of


# ---- marks ------------------------------------------------------------------------------------
# Each: id, a test on (text, kind), and whether it applies to user content too.

def m(id_, rx, kinds=None, flags=0, user=False):
    r = re.compile(rx, flags)
    return id_, lambda t, k: (kinds is None or k in kinds) and bool(r.search(t)), user


BUTTONS = {"button"}
KINDS = {"title", "heading", "item name", "button", "option", "field label", "field hint", "nav", "link",
         "severity", "status label", "state badge", "kind badge", "generated file", "panel row line",
         "stage name", "stage result", "duration", "description", "state message", "fact", "disclosure",
         "body", "placeholder", "a11y label", "tooltip", "alt text", "value"}
MARKS = [
    ("D1", lambda t, k: bool(re.search(r"library|your items|your own items",
                                       re.sub(r"My library|Public library", "", t), re.I)), False),
    m("D2", r"\bshelf\b|items we have checked"),
    m("D3", r"^(Check|Export one item|Take as an archive)$", {"title"}),
    m("D4", r"^(Export|Export with .*|Download .*|Build the archive again|Take as an archive|"
            r"Check it, then take the archive)$|^11 · |^Archive (built|downloaded)", {"button", "heading"}),
    m("D5", r"^(Copy (to|into) .*|Add to My library)$", BUTTONS),
    m("D6", r"\b(the|this) set\b|\bin the set\b|\bfrom the set\b"),
    m("D7", r"auto-added|pulled in|\bbrings\b|comes? in with|walk along", flags=re.I),
    m("D8", r"detach|linked|library version|the original|\bdiffers?\b|Modified in this project", flags=re.I),
    m("D9", r"server (did not|didn’t|stopped)|our server|our side|our failure", flags=re.I),
    m("D10", r"\b503\b"),
    m("D11", r"^(Loading|Opening|Signing in|Creating your account|Adding —|Checking)"),
    m("D12", r"again$|^Try ", BUTTONS),
    m("D13", r"is empty$|^No \w+ (yet|match)$|^Nothing (in this project yet|called .* here)$|"
             r"^Nothing called .*$", {"heading"}),
    m("D14", r"^(Clear|Reset) (search|filters)|^Clear search · show All$", BUTTONS),
    m("D15", r"^Search ", {"placeholder"}),
    m("D16", r"^(Cancel|Close|Dismiss|Discard changes)$", BUTTONS | {"a11y label"}),
    m("D17", r"create (an )?account|sign in|reset (your )?password|forgot password|reset link", flags=re.I),
    m("D18", r"receiving machine|your machine", flags=re.I),
    m("D19", r"checked (just now|\d|by|it)|last checked|^Just now|^Checked", flags=re.I),
    m("D20", r"^(?!Signing|Creating).*…$|^(Share|Delete example|Remove eslint-autofix)$", BUTTONS),
    m("D21", r"^(Share|Share the project|Create link|Stop sharing)$", BUTTONS),
    m("D22", r"^Remove\b", BUTTONS | {"a11y label"}),
    m("D23", r"^(Didn’t complete|Stopped — .*|Couldn’t be written|Not run|Waiting)$", {"stage result"}),
    m("U3", r"beside the 10 you have|You have 10 items", user=True),
    m("V1", r"\bpieces\b|pipelines|harnesses", flags=re.I),
    m("V2", r"MCP servers?\b"),
    m("T1", r"'"),
    m("T2", r"\b(did not|can not|cannot|do not|does not)\b", KINDS - {"generated file"}),
    m("T3", r"Licence|summari[sz]"),
    m("L1", r"\(Q\d+\)"),
    m("L2", r"…$", {"generated file"}),
    m("U2", r"query-explainer|schema-docs|stripe-rules|webapp-testing|stripe-webhooks", user=True),
]


def marks_for(text, kind, who, u1, screen=""):
    if screen == "Create an account" and text == "Forgot password?":
        return ["L3"]
    out = [id_ for id_, test, on_user in MARKS if (on_user or who != "user") and test(text, kind)]
    if text in u1:
        out.append("U1")
    return out


def cell(s):
    s = s.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace("\n", "<br>").replace("⏎", "<br>")


def render():
    grouped, whose, u1, desc_of = build()
    by_screen = OrderedDict((s, []) for s in ["Everywhere — the app header"] + ORDER)
    for (screen, z, t, k), states in grouped.items():
        by_screen[screen].append((z, t, k, states))

    out = []
    total = 0
    for screen, lines in by_screen.items():
        if not lines:
            continue
        states_all = OrderedDict.fromkeys(s for _, _, _, ss in lines for s in ss)
        out.append(f"\n### {screen}\n")
        if screen.startswith("Everywhere"):
            out.append(f"On {len(states_all)} pages — every page with the app header. "
                       "Listed once; the column says how many pages carry it.\n")
        else:
            out.append("State pages: " + " · ".join(f"`{s}`" for s in states_all) + "\n")
        out.append("| Screen | Zone | Line | Type | On | Whose | Mark |")
        out.append("|---|---|---|---|---|---|---|")
        for z, t, k, states in lines:
            who = whose(t, k)
            mk = marks_for(t, k, who, u1, screen)
            uniq = list(OrderedDict.fromkeys(states))
            if screen.startswith("Everywhere"):
                on = f"{len(uniq)} pages"
            elif len(uniq) == len(states_all):
                on = "all"
            else:
                on = " · ".join(uniq)
            total += 1
            short = screen
            out.append(f"| {short} | {cell(z)} | {cell(t)} | {k} | {on} | {who} | {' '.join(mk)} |")
    return "\n".join(out), total, desc_of


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    body, total, _ = render()
    print(f"<!-- {total} rows -->")
    print(body)


# ---- was / now (lesson 05, step 6) ------------------------------------------------------------
# The pages' markup is unchanged by the rewrite, so a page's rows before and after align one to one.
# `base` is the commit holding the pages as the inventory found them.

def render_wasnow(base="56777bc"):
    import difflib
    import json
    import subprocess
    from extract_copy import Tree, Node, walk, PAGES
    why = json.load(open(__file__.rsplit("build_microcopy.py", 1)[0] + "copy_why.json", encoding="utf-8"))

    def rows_of(html, stem):
        t = Tree()
        t.feed(html)
        body = next(c for c in t.root.children if isinstance(c, Node) and c.tag == "html")
        rs = []
        walk(body, rs, stem)
        return rs

    grouped0, whose, u1, _ = build()
    grouped = OrderedDict()
    for p in sorted(PAGES.glob("*.html")):
        if p.name == "wireframes.html":
            continue
        old = subprocess.run(["git", "show", f"{base}:04-wireframes/pages/{p.name}"],
                             capture_output=True).stdout.decode("utf-8")
        a, c = rows_of(old, p.stem), rows_of(p.read_text(encoding="utf-8"), p.stem)
        aligned = []
        # Text-only rewrites align one to one. Step 7 added and removed a few elements, so rows are
        # matched on type and element, and an unmatched row reads as added or removed.
        key = lambda r: (r[3], r[4].tag, tuple(r[4].cls))   # not the zone: zones carry aria-labels, which changed
        sm = difflib.SequenceMatcher(a=[key(r) for r in a], b=[key(r) for r in c], autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal" or (op == "replace" and i2 - i1 == j2 - j1):
                aligned += [(a[i], c[j][2]) for i, j in zip(range(i1, i2), range(j1, j2))]
            else:
                aligned += [(a[i], "(removed)") for i in range(i1, i2)]
                aligned += [((c[j][0], c[j][1], "(added)", c[j][3], None), c[j][2]) for j in range(j1, j2)]
        for (pg, z, t, k, _), n in aligned:
            if NOISE.fullmatch(t) and k in ("body", "duration"):
                continue
            screen, state = screen_of(pg)
            if z.split(" › ")[0] in CHROME:
                screen, state = "Everywhere — the app header", pg
            if k == "severity" and t not in ("Problem", "Note", "Skipped"):
                k = "status label"
            grouped.setdefault((screen, z, t, n, k), []).append(state)

    by_screen = OrderedDict((s, []) for s in ["Everywhere — the app header"] + ORDER)
    for (screen, z, t, n, k), states in grouped.items():
        by_screen[screen].append((z, t, n, k, states))
    out, total, changed = [], 0, 0
    for screen, lines in by_screen.items():
        states_all = OrderedDict.fromkeys(s for *_, ss in lines for s in ss)
        out.append(f"\n### {screen}\n")
        if screen.startswith("Everywhere"):
            out.append(f"On {len(states_all)} pages — every page with the app header. Listed once.\n")
        else:
            out.append("State pages: " + " · ".join(f"`{s}`" for s in states_all) + "\n")
        out.append("| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |")
        out.append("|---|---|---|---|---|---|---|---|---|")
        for z, t, n, k, states in lines:
            who = whose(t, k)
            mk = marks_for(t, k, who, u1, screen)
            uniq = list(OrderedDict.fromkeys(states))
            on = f"{len(uniq)} pages" if screen.startswith("Everywhere") else \
                "all" if len(uniq) == len(states_all) else " · ".join(uniq)
            y = ""
            if n != t:
                changed += 1
                y = why.get(screen, {}).get(t) or why.get("*", {}).get(t) or ""
                s7 = [r for f, r in why.get("step7", {}).items() if f in n and f not in t]
                if "503 ·" in t and "503 ·" not in n:
                    s7.append("Step 7 #19: the error code moved to a line of its own (D10)")
                if s7:
                    y = "; ".join(([y] if y else []) + s7)
                if n == "(removed)":
                    y = why.get("removed", {}).get(t, y)
            total += 1
            out.append(f"| {screen} | {cell(z)} | {cell(t)} | {('**' + cell(n) + '**') if n != t else '='} | "
                       f"{k} | {on} | {who} | {' '.join(mk)} | {y} |")
    return "\n".join(out), total, changed
