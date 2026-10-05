"""Builds every case of the main job's flow into 04-wireframes/prototypes/main-*/.
Rules: 04-wireframes/prototypes/_conventions.md. Cases: prototypes.md. Pages are the source once built."""
import re, pathlib, shutil, json

ROOT = pathlib.Path(__file__).resolve().parents[2] / "04-wireframes"
SRC = ROOT / "pages"
PROTO = ROOT / "prototypes"
ICON = '<span class="icon" aria-hidden="true"></span>'


def read(name):
    return (SRC / name).read_text(encoding="utf-8")


def must(s, old, new, count=1):
    assert s.count(old) >= 1, f"missing: {old[:90]}"
    return s.replace(old, new, count)


# ── wiring ────────────────────────────────────────────────────────────────────

def inert(s):
    """Every page link and every '#' goes nowhere; the stylesheet comes from pages/."""
    s = s.replace('href="wireframe.css"', 'href="../../pages/wireframe.css"')
    s = re.sub(r'(<a\b[^>]*?)\s+href="(?:[a-z0-9-]+\.html|#)"', r"\1", s)
    s = re.sub(r'(<form\b[^>]*?)\s+action="[a-z0-9-]+\.html"', r"\1", s)   # Enter in a field is not a way forward
    return s


def live(s, marker, target):
    """Give the one element found by `marker` (an inert opening tag, unique) its href."""
    assert s.count(marker) == 1, f"marker x{s.count(marker)}: {marker[:90]}"
    return s.replace(marker, marker.replace("<a", f'<a href="{target}"', 1), 1)


def btn(s, marker, target):
    """A button that is a step becomes a link to the next step (conventions §3)."""
    assert s.count(marker) == 1, f"button x{s.count(marker)}: {marker[:90]}"
    i = s.index(marker)
    tag = marker[:marker.index(">") + 1]   # the marker may carry the button's text after its tag
    j = s.index("</button>", i)
    inner = s[i + len(tag):j]
    cls = re.search(r'class="([^"]*)"', tag)
    classes = "button" + (" " + cls.group(1) if cls else "")
    aria = re.search(r'aria-label="([^"]*)"', tag)
    a = f'<a class="{classes}" href="{target}"' + (f' aria-label="{aria.group(1)}"' if aria else "") + ">"
    return s[:i] + a + inner + "</a>" + s[j + len("</button>"):]


def control(s, marker, end, target, cls):
    """A label holding an input or a select, as a step: the whole control becomes the link."""
    assert s.count(marker) == 1, f"control x{s.count(marker)}: {marker[:90]}"
    i = s.index(marker)
    j = s.index(end, i)
    inner = s[i + len(marker):j]
    return s[:i] + f'<a class="{cls}" href="{target}">' + inner + "</a>" + s[j + len(end):]


def panel_tick(s, name, target):
    """The panel row for `name`: its 'Add' checkbox is the step."""
    i = s.index(f">{name}</a><span class=\"tag\">")
    k = s.index('<label class="check">', i)
    j = s.index("</label>", k)
    inner = s[k + len('<label class="check">'):j]
    return s[:k] + f'<a class="check" href="{target}">' + inner + "</a>" + s[j + len("</label>"):]


def titled(s, title, case):
    return re.sub(r"<title>.*?</title>", f"<title>{title} — prototype · {case}</title>", s, count=1)


def wait(s, target, seconds=2):
    return s.replace("</title>", f'</title>\n  <meta http-equiv="refresh" content="{seconds};url={target}">', 1)


# ── the acme-billing-api set, in its variants ─────────────────────────────────

def drop_li(s, needle, indent="          "):
    i = s.index(needle)
    start = s.rindex(f"{indent}<li>", 0, i)
    end = s.index(f"{indent}</li>\n", i) + len(f"{indent}</li>\n")
    return s[:start] + s[end:]


def set_row(name, kind, desc, facts, remove=False, state=None, mark=None, extra=""):
    tags = f'<span class="tag">{kind}</span>' + (f'<span class="tag tag-state">{state}</span>' if state else "")
    marks = f'<span class="mark"><span class="glyph glyph-{mark.lower()}" aria-hidden="true"></span>{mark}</span>' if mark else ""
    act = (f'<button type="button" class="remove" aria-label="Remove {name} from this project">{ICON}</button>' if remove else "")
    return f'''          <li>
            <article class="row row-tight set-item">
              <div>
                <h3><a href="project-configuring-item.html">{name}</a>{tags}</h3>
                <p class="description">{desc}</p>
                <p class="facts meta"><span>{facts}</span></p>{extra}
              </div>
              <p class="marks">{marks}</p>
              <div class="row-actions">{act}</div>
            </article>
          </li>
'''


QUERY = dict(name="query-explainer", kind="agent", desc="Explains a slow query from its plan and suggests the index that would fix it.",
             facts="requires <code>postgres-mcp</code> · <code>.claude/agents/query-explainer.md</code>")
STRIPE = dict(name="stripe-rules", kind="prompt", desc="How Acme calls Stripe: an idempotency key on every POST, webhooks verified before they are read.",
              facts="<code>CLAUDE.md</code>, appended")

ORIG_HEAD = ("14 items · 3 auto-added · 1 detached", "Checked 2 days ago · for Claude Code · 1 problem · 2 notes · 1 skipped")


def acme_set(s, variant, remove):
    """variant: orig · clean · query · stripe. Inserted rows go before github-mcp."""
    if variant != "orig":
        s = drop_li(s, ">eslint-autofix</a><span class=\"tag\">script")
    extra = {"query": QUERY, "stripe": STRIPE}.get(variant)
    if extra:
        anchor = s.rindex("          <li>", 0, s.index(">github-mcp</a>"))
        s = s[:anchor] + set_row(remove=remove, **extra) + s[anchor:]
    return s


def head_meta(s, counts, check):
    s = must(s, ORIG_HEAD[0], counts)
    return must(s, ORIG_HEAD[1], check)


def project_page(variant, counts, check, case, title, links=(), check_to=None, configure_to=None, pre=None):
    s = read("project-default.html")
    s = acme_set(s, variant, remove=False)
    s = head_meta(s, counts, check)
    if pre:
        s = pre(s)
    s = titled(inert(s), title, case)
    if check_to:
        s = live(s, '<a class="button button-primary">', check_to)
    if configure_to:
        s = live(s, '<a class="button">Configure</a>', configure_to)
    for m, t in links:
        s = live(s, m, t)
    return s


def configuring_page(variant, counts, check, case, title, pre=None):
    s = read("project-configuring-default.html")
    s = acme_set(s, variant, remove=True)
    s = head_meta(s, counts, check)
    if pre:
        s = pre(s)
    return titled(s, title, case)


# ── Run on acme-billing-api ───────────────────────────────────────────────────

CONFLICTS_CHECKED = '''<li>
            <details>
              <summary><span class="n">02</span><span class="name">Declared conflicts</span><span class="result"><span class="glyph glyph-checked" aria-hidden="true"></span>Checked — no two items declare a conflict</span><span class="time">0.1 s</span></summary>
            </details>
          </li>'''


def run_env_fix(s):
    """The wireframe names 2 keys and writes 3 into .env.example — the prototype says 3."""
    s = s.replace("1 note · 2 keys named", "1 note · 3 keys named")
    return s.replace(
        "<code>DATABASE_URL</code> (postgres-mcp) and <code>GITHUB_TOKEN</code> (github-mcp) are needed.",
        "<code>DATABASE_URL</code> (postgres-mcp), <code>GITHUB_TOKEN</code> (github-mcp) and <code>SENTRY_AUTH_TOKEN</code> (sentry-mcp) are needed.")


def run_variant(s, variant, target="Claude Code"):
    """orig keeps the Problem; clean/query/stripe drop eslint-autofix and add their own item."""
    s = run_env_fix(s)
    if variant == "orig":
        n, chose, files = 14, 11, 18
    else:
        s = re.sub(r"<li>\s*<details open>\s*<summary><span class=\"n\">02</span>.*?</li>", CONFLICTS_CHECKED, s, count=1, flags=re.S)
        s = s.replace("<strong>1 problem · 2 notes · 1 skipped</strong>", "<strong>0 problems · 2 notes · 1 skipped</strong>")
        s = s.replace("db-migrate.sh · seed-data.sh · eslint-autofix.sh · openapi-lint.sh", "db-migrate.sh · seed-data.sh · openapi-lint.sh")
        n, chose, files = {"clean": (13, 10, 17), "query": (14, 11, 18), "stripe": (14, 11, 17)}[variant]
    s = s.replace("14 items · 3 auto-added · no cycles", f"{n} items · 3 auto-added · no cycles")
    s = s.replace("You added 11.", f"You added {chose}.")
    s = s.replace("acme-billing-api · 14 items", f"acme-billing-api · {n} items")
    s = s.replace("Written · 14 items", f"Written · {n} items")
    s = s.replace("18 files for Claude Code", f"{files} files for Claude Code")
    if variant == "query":
        s = s.replace("├── .claude/agents/test-runner.md\n", "├── .claude/agents/test-runner.md\n├── .claude/agents/query-explainer.md\n")
    if variant == "stripe":
        s = s.replace("CLAUDE.md                       commit-conventions, api-contracts", "CLAUDE.md                       commit-conventions, api-contracts, stripe-rules")
    if target == "Cursor":
        s = to_cursor(s, n)
    return s


def to_cursor(s, n):
    """The same set under the Cursor target (§6): rules as MDC in .cursor/rules, its own MCP config."""
    s = s.replace("<option selected>Claude Code</option><option>Cursor</option>", "<option>Claude Code</option><option selected>Cursor</option>")
    s = s.replace("for Claude Code", "for Cursor")
    s = re.sub(r'<pre class="file">acme-billing-api/.*?</pre>', '''<pre class="file">acme-billing-api/
├── SETUP.md
├── .env.example                    DATABASE_URL, GITHUB_TOKEN, SENTRY_AUTH_TOKEN
├── .cursor/mcp.json                postgres-mcp, github-mcp, sentry-mcp
├── .cursor/rules/code-style.mdc
├── .cursor/rules/changelog-writer.mdc
├── .cursor/rules/commit-conventions.mdc
├── .cursor/rules/api-contracts.mdc
├── .cursor/rules/migration-reviewer.mdc
├── .cursor/rules/acme-pr-reviewer.mdc      detached
├── .cursor/rules/test-runner.mdc
└── scripts/  db-migrate.sh · seed-data.sh · openapi-lint.sh</pre>''', s, count=1, flags=re.S)
    s = re.sub(r"\d+ files for Cursor", "15 files for Cursor", s)
    s = s.replace("# Setup — acme-billing-api (Claude Code)", "# Setup — acme-billing-api (Cursor)")
    return s


EXPORT_RE = re.compile(r"<!-- (?:Export is the final stage|Loading is the stack|Success: the archive|Error: the archive).*?</section>", re.S)


def export_section(s, html, comment):
    assert EXPORT_RE.search(s), "no export section"
    return EXPORT_RE.sub(lambda m: f"<!-- {comment} -->\n      " + html, s, count=1)


def export_clean(target="Claude Code"):
    return f'''<section class="export-stage" aria-labelledby="export-title">
        <h2 id="export-title">11 · Export</h2>
        <p>Nothing in this project is a Problem. The two notes name what the receiving machine still has to supply.</p>
        <div class="export-actions">
          <a class="button button-primary">{ICON}Export</a>
        </div>
      </section>'''


def export_building(files, zipname):
    return f'''<section class="export-stage" aria-labelledby="export-title">
        <h2 id="export-title">11 · Export</h2>
        <p role="status"><strong>Exporting — {files}</strong></p>
        <p class="meta">{zipname}</p>
      </section>'''


def run_page(template, variant, case, title, target="Claude Code"):
    s = run_variant(read(template), variant, target)
    return titled(s, title, case)


def run_resolved(variant, case, title, target="Claude Code", problem_export=False):
    s = run_page("run-default.html", variant, case, title, target)
    if not problem_export:
        s = export_section(s, export_clean(target), "Export is the final stage, always live (§6). No Problem in the set: a plain export, nothing to confirm.")
    return inert(s)


def run_building(variant, case, title, nxt, target="Claude Code"):
    s = run_page("run-default.html", variant, case, title, target)
    files = re.search(r"(\d+) files for " + target, s).group(0)
    zipname = "acme-billing-api-" + target.lower().replace(" ", "-") + ".zip"
    s = export_section(s, export_building(files, zipname), "Building the archive: the second wait in Run, an ordinary one (_screens.md). Nothing to press while it runs.")
    return wait(inert(s), nxt)


def run_success(variant, case, title, back, target="Claude Code"):
    s = run_page("run-success.html", variant, case, title, target)
    files = int(re.search(r"(\d+) files for " + target, s).group(1))
    verdict = "1 problem · 2 notes · 1 skipped" if variant == "orig" else "0 problems · 2 notes · 1 skipped"
    s = must(s, "18 files · 41 KB · saved to Downloads. Checked just now · 1 problem · 2 notes · 1 skipped.",
             f"{files} files · {files * 2 + 5} KB · saved to Downloads. Checked just now · {verdict}.")
    s = s.replace("acme-billing-api-claude-code.zip", "acme-billing-api-" + target.lower().replace(" ", "-") + ".zip")
    s = inert(s)
    return live(s, '<a class="button button-primary">Back to acme-billing-api</a>', back)


def run_loading(variant, case, title, nxt, target="Claude Code", heading=None):
    s = run_page("run-loading.html", variant, case, title, target)
    if heading:
        s = must(s, '<h1 role="status">Checking — stage 4 of 10</h1>', f'<h1 role="status">{heading}</h1>')
    return wait(inert(s), nxt)


# ── new pages, drawn in the wireframes' own markup ────────────────────────────

MY_LIBRARY = [  # read from library-my-default.html
    ("code-style", "skill", "How I want TypeScript written: naming, imports, error handling, no default exports."),
    ("db-migrate", "script", "Generates a Postgres migration from a schema diff and runs it — dry run first, then for real."),
    ("seed-data", "script", "Loads a small, realistic dataset into a fresh database."),
    ("migration-reviewer", "agent", "Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills."),
    ("postgres-mcp", "mcp", "Read-only Postgres access for the agent: schema, explain plans, sample rows."),
    ("github-mcp", "mcp", "Issues, pull requests and code search on GitHub, through GitHub’s own server."),
    ("pr-reviewer", "agent", "Reads a pull request diff and leaves review comments the way I would write them."),
    ("commit-conventions", "prompt", "Conventional commits, imperative mood, and a body that says why rather than what."),
    ("writing-style", "prompt", "Plain English for docs: short sentences, no marketing words, an example before every rule."),
    ("link-checker", "script", "Crawls the built docs and lists every broken internal and external link, with the page it is on."),
    ("whisper", "app", "Speech-to-text, run locally on voice memos before they are summarised."),
]
PUBLIC_LIBRARY = [  # read from library-public-default.html
    ("filesystem", "mcp", "Read and write files inside the directories you allow, and nowhere else."),
    ("memory", "mcp", "A knowledge graph the agent can write to and read back between sessions."),
    ("fetch", "mcp", "Fetches a URL and hands the agent the page as Markdown."),
    ("github-mcp-server", "mcp", "GitHub’s own MCP server: issues, pull requests, Actions and code search."),
    ("playwright-mcp", "mcp", "Drives a real browser through the accessibility tree rather than screenshots."),
    ("context7", "mcp", "Pulls current, version-specific library documentation into the prompt."),
    ("mcp-builder", "skill", "A guide for building an MCP server: tool design, error messages, evaluation."),
    ("webapp-testing", "skill", "Tests a local web app with Playwright: start the server, drive the page, read the logs."),
]


def panel_rows(items, ticked, lines=None):
    out = []
    for name, kind, desc in items:
        line = (lines or {}).get(name, desc)
        box = '<input type="checkbox" checked> In this project' if name in ticked else '<input type="checkbox"> Add'
        out.append(f'''          <li>
            <article class="row row-compact">
              <div>
                <h3><a href="project-configuring-item.html">{name}</a><span class="tag">{kind}</span></h3>
                <p class="state-line">{line}</p>
              </div>
              <label class="check">{box}</label>
            </article>
          </li>''')
    return '<ol class="row-list">\n' + "\n".join(out) + "\n        </ol>"


def nested(parent_html, children_html, label):
    """Put sub-rows under the last row's </article> of parent_html."""
    i = parent_html.rindex("            </article>\n") + len("            </article>\n")
    sub = f'            <ol class="sub-rows" aria-label="{label}">\n' + children_html.replace("\n          ", "\n              ").replace("          <li>", "              <li>", 1) + "            </ol>\n"
    return parent_html[:i] + sub + parent_html[i:]


def sub(html):
    """Indent a row one level so it sits inside sub-rows."""
    return "\n".join(("    " + l if l.strip() else l) for l in html.splitlines()) + "\n"


def stripe_set(stage, remove):
    """stripe-webhooks from My library: migration-reviewer (+ db-migrate → seed-data, postgres-mcp), then code-style.
    stage: 'mr-adding' · 'mr' · 'cs-adding' · 'full'"""
    rows = ""
    if stage in ("cs-adding", "full"):
        if stage == "cs-adding":
            rows += set_row("code-style", "skill", MY_LIBRARY[0][2], "Adding — finding what it requires")
        else:
            rows += set_row("code-style", "skill", MY_LIBRARY[0][2], "<code>.claude/skills/code-style/SKILL.md</code> · defers to <em>the client’s ESLint config</em>", remove=remove, mark="Note" if not remove else None)
    if stage == "mr-adding":
        return set_row("migration-reviewer", "agent", MY_LIBRARY[3][2], "Adding — finding what it requires")
    mr = set_row("migration-reviewer", "agent", MY_LIBRARY[3][2], "requires <code>db-migrate</code>, <code>postgres-mcp</code> · 3 auto-added", remove=remove)
    seed = set_row("seed-data", "script", "Loads a small, realistic dataset into a fresh database.", "<code>scripts/seed-data.sh</code>", state="Auto-added")
    dbm = set_row("db-migrate", "script", MY_LIBRARY[1][2], "<code>scripts/db-migrate.sh</code> + 2 files · 1 auto-added", state="Auto-added")
    dbm = nested(dbm, seed, "Auto-added for db-migrate")
    pg = set_row("postgres-mcp", "mcp", MY_LIBRARY[4][2], "<code>modelcontextprotocol/servers-archived</code> @ <code>9be4674</code> · MIT · needs <code>DATABASE_URL</code>", state="Auto-added")
    mr = nested(mr, sub(dbm) + sub(pg), "Auto-added for migration-reviewer")
    return rows + mr


def shelf_set(stage, remove):
    """stripe-webhooks from the Public library: webapp-testing (+ playwright-mcp), then github-mcp-server.
    stage: 'wt-adding' · 'wt' · 'gh-adding' · 'full'"""
    rows = ""
    if stage == "wt-adding":
        return set_row("webapp-testing", "skill", PUBLIC_LIBRARY[7][2], "Adding — finding what it requires")
    wt = set_row("webapp-testing", "skill", PUBLIC_LIBRARY[7][2], "<code>anthropics/skills</code> @ <code>c74d647</code> · Apache-2.0 · requires <code>playwright-mcp</code> · 1 auto-added", remove=remove)
    pw = set_row("playwright-mcp", "mcp", PUBLIC_LIBRARY[4][2], "<code>microsoft/playwright-mcp</code> @ <code>v0.0.40</code> · Apache-2.0", state="Auto-added")
    wt = nested(wt, sub(pw), "Auto-added for webapp-testing")
    if stage == "gh-adding":
        rows += set_row("github-mcp-server", "mcp", PUBLIC_LIBRARY[3][2], "Adding — finding what it requires")
    elif stage == "full":
        rows += set_row("github-mcp-server", "mcp", PUBLIC_LIBRARY[3][2], "<code>github/github-mcp-server</code> @ <code>v0.9.0</code> · MIT · needs <code>GITHUB_TOKEN</code>", remove=remove, mark=None if remove else "Note")
    return wt + rows


def page_with(template, main_html, case, title, current="projects"):
    """Swap the <main> of a wireframe page for main_html."""
    s = read(template)
    s = re.sub(r'    <main class="app-main">.*?</main>', main_html, s, count=1, flags=re.S)
    return titled(s, title, case)


def configuring_new(case, title, name, meta, panel_html, set_html, scope="My library", tab="All", check_live=False):
    s = read("project-configuring-empty.html")
    other = "Public library" if scope == "My library" else "My library"
    scope_nav = f'<nav class="scope" aria-label="Scope"><a href="#"{" aria-current=\"page\"" if scope == "My library" else ""}>My library</a><a href="#"{" aria-current=\"page\"" if scope == "Public library" else ""}>Public library</a></nav>'
    s = re.sub(r'<nav class="scope".*?</nav>', scope_nav, s, count=1)
    if scope == "Public library":   # the placeholder project-configuring-public.html carries
        s = must(s, 'placeholder="Search My library — migrate, GITHUB_TOKEN, review"', 'placeholder="Search Public library — filesystem, playwright, anthropics"')
    s = re.sub(r'(<div class="panel-body">).*?(\n      </div>\n    </aside>)', lambda m: m.group(1) + "\n        " + panel_html + m.group(2), s, count=1, flags=re.S)
    s = s.replace("<h1 id=\"page-title\">stripe-webhooks", f"<h1 id=\"page-title\">{name}")
    s = must(s, '<p class="meta head-meta"><span>No items yet</span></p>', f'<p class="meta head-meta"><span>{meta}</span></p>')
    if set_html is not None:
        s = re.sub(r'<section aria-label="Items in this project">.*?</section>', '<section aria-label="Items in this project">\n      <ol class="row-list">\n' + set_html + '        </ol>\n      </section>', s, count=1, flags=re.S)
    if check_live:
        s = must(s, f'<button type="button" disabled title="Add an item first">{ICON}Export…</button>', f'<a class="button" href="run-loading.html">{ICON}Export…</a>')
    return titled(s, title, case)


def project_new(case, title, name, meta, set_html, check_to=None):
    s = read("project-default.html")
    s = s.replace("<h1 id=\"page-title\">acme-billing-api</h1>", f"<h1 id=\"page-title\">{name}</h1>")
    s = must(s, f'<p class="meta head-meta"><span>{ORIG_HEAD[0]}</span><span>{ORIG_HEAD[1]}</span></p>', f'<p class="meta head-meta">{meta}</p>')
    s = re.sub(r'\n      <p class="description" style="max-width: 800px">.*?</p>\n', "\n", s, count=1)
    s = re.sub(r'(<section aria-label="Items in this project">\s*<ol class="row-list">).*?(\n        </ol>\n      </section>)', lambda m: m.group(1) + "\n" + set_html + m.group(2)[1:], s, count=1, flags=re.S)
    s = titled(inert(s), title, case)
    if check_to:
        s = live(s, '<a class="button button-primary">', check_to)
    return s


# A run for a set that is not acme-billing-api, in run-default's own markup.

def stage(n, name, glyph, result, time, body=None, open_=False, waiting=False):
    b = f'\n              <div class="stage-body">\n                {body}\n              </div>' if body else ""
    return f'''          <li{' class="waiting"' if waiting else ''}>
            <details{' open' if open_ else ''}>
              <summary><span class="n">{n:02d}</span><span class="name">{name}</span><span class="result"><span class="glyph glyph-{glyph}" aria-hidden="true"></span>{result}</span><span class="time">{time}</span></summary>{b}
            </details>
          </li>'''


def note(text):
    return f'<div class="callout callout-quiet">\n                  <span class="severity">Note</span>\n                  <span>{text}</span>\n                </div>'


STAGE_NAMES = ["Requirements", "Declared conflicts", "Command names", "Target paths", "Env keys", "Defers to", "Pinned refs",
               "What the archive contains", "SETUP.md — for the agent that opens it", ".env.example"]


def run_generic(spec, case, title, mode, nxt=None, back=None):
    """mode: loading · default · building · success. spec: name, n, verdict, stages (10 tuples), files, zip, needs, time."""
    done = 4 if mode == "loading" else 10
    items = []
    for i, st in enumerate(spec["stages"], 1):
        glyph, result, time, body = st
        if mode == "loading" and i == done:
            items.append(stage(i, STAGE_NAMES[i - 1], "running", "Checking", ""))
        elif mode == "loading" and i > done:
            items.append(stage(i, STAGE_NAMES[i - 1], "waiting", "Waiting", "", waiting=True))
        else:
            items.append(stage(i, STAGE_NAMES[i - 1], glyph, result, time, body))
    if mode == "loading":
        summary = f'<h1 role="status">Checking — stage 4 of 10</h1>\n        <p class="meta">{spec["name"]} · {spec["n"]} items · for Claude Code</p>'
    else:
        summary = f'<h1>Checked just now</h1>\n        <p><strong>{spec["verdict"]}</strong></p>\n        <p class="meta">{spec["name"]} · {spec["n"]} items · for Claude Code · {spec["time"]}</p>'
    if mode == "loading":
        exp = '<!-- Loading is the stack mid-sweep, not a spinner (§6). Export is waiting like the stages, not greyed. -->\n      <section class="export-stage" aria-labelledby="export-title">\n        <h2 id="export-title">11 · Export</h2>\n        <p class="meta">Opens after the handover stages.</p>\n      </section>'
    elif mode == "default":
        exp = "<!-- Export is the final stage, always live (§6). No Problem in the set: a plain export, nothing to confirm. -->\n      " + export_clean().replace("The two notes name", spec["notes_line"])
    elif mode == "building":
        exp = "<!-- Building the archive: the second wait in Run (_screens.md). -->\n      " + export_building(f'{spec["files"]} files for Claude Code', spec["zip"])
    else:
        needs = "\n".join(f"            <li>{x}</li>" for x in spec["needs"])
        exp = f'''<!-- Success: the archive is built and in hand. Checked, never works (§6). -->
      <section class="export-stage" aria-labelledby="export-title">
        <h2 id="export-title">Exported — {spec["zip"]}</h2>
        <p>{spec["files"]} files · {spec["files"] * 2 + 3} KB · saved to Downloads. Checked just now · {spec["verdict"]}.</p>
        <div>
          <p><strong>The receiving machine still needs</strong></p>
          <ul class="plain-list">
{needs}
          </ul>
        </div>
        <div class="export-actions">
          <a class="button button-primary">Back to {spec["name"]}</a>
          <button type="button">Download again</button>
          <button type="button">Share…</button>
        </div>
      </section>'''
    main = f'''    <main class="app-main">

      <section class="summary" aria-label="Verdict">
        {summary}
      </section>

      <section class="stage-group" aria-labelledby="g-find">
        <h2 id="g-find">Findings</h2>
        <ol class="stages">
{chr(10).join(items[:7])}
        </ol>
      </section>

      <!-- The handover is read before Export, never after it (§6). -->
      <section class="stage-group" aria-labelledby="g-hand">
        <h2 id="g-hand">Handover — what the receiving machine still needs</h2>
        <ol class="stages">
{chr(10).join(items[7:])}
        </ol>
      </section>

      {exp}

    </main>'''
    s = read("run-default.html")
    s = re.sub(r'    <main class="app-main">.*?</main>', lambda m: main, s, count=1, flags=re.S)
    s = s.replace('<span class="icon" aria-hidden="true"></span>acme-billing-api</a>', f'<span class="icon" aria-hidden="true"></span>{spec["name"]}</a>')
    s = titled(inert(s), title, case)
    if mode == "default":
        s = live(s, f'<a class="button button-primary">{ICON}Export</a>', nxt)
    if mode in ("loading", "building"):
        s = wait(s, nxt)
    if mode == "success":
        s = live(s, f'<a class="button button-primary">Back to {spec["name"]}</a>', back)
    return s


STRIPE_RUN = dict(
    name="stripe-webhooks", n=5, time="0.9 s", files=9, zip="stripe-webhooks-claude-code.zip",
    verdict="0 problems · 2 notes · 1 skipped",
    notes_line="The two notes name",
    needs=["A value for <code>DATABASE_URL</code>", "One repo cloned at its pinned ref — <code>SETUP.md</code> says which", "An agent that reads <code>SETUP.md</code> first"],
    stages=[
        ("note", "5 items · 3 auto-added · no cycles", "0.2 s", "<p>You added 2. 3 more were auto-added because another item <code>requires</code> them: <code>db-migrate</code> and <code>postgres-mcp</code> for <code>migration-reviewer</code>, and <code>seed-data</code> for <code>db-migrate</code>.</p>"),
        ("checked", "Checked — no two items declare a conflict", "0.1 s", None),
        ("skipped", "Skipped — no item declares a command", "—", None),
        ("checked", "Checked — no two items write to the same path", "0.1 s", None),
        ("note", "1 note · 1 key named", "0.1 s", note("<code>DATABASE_URL</code> (postgres-mcp) is needed. It goes into <code>.env.example</code> as a name; the receiving machine supplies the value.")),
        ("note", "1 note", "0.1 s", note("<code>code-style</code> defers to the client’s ESLint config. Where they disagree, that wins.")),
        ("checked", "Checked — 1 external item, pinned", "0.2 s", None),
        ("checked", "9 files for Claude Code", "0.1 s", '''<pre class="file">stripe-webhooks/
├── SETUP.md
├── .env.example                    DATABASE_URL
├── .mcp.json                       postgres-mcp
├── .claude/skills/code-style/SKILL.md
├── .claude/agents/migration-reviewer.md
└── scripts/  db-migrate.sh + 2 files · seed-data.sh</pre>'''),
        ("checked", "Written · 5 items", "0.2 s", '''<pre class="file"># Setup — stripe-webhooks (Claude Code)

Read this first and perform each step.

## postgres-mcp
- External. Clone modelcontextprotocol/servers-archived at 9be4674.
- Needs DATABASE_URL. Ask the person for it; do not invent one.
- Required by migration-reviewer.

## code-style
- Defers to the client’s ESLint config. Where they disagree, the ESLint config wins.
…</pre>'''),
        ("checked", "1 key, names only", "0.1 s", '<pre class="file">DATABASE_URL=</pre>'),
    ])

SHELF_RUN = dict(
    name="stripe-webhooks", n=3, time="0.8 s", files=6, zip="stripe-webhooks-claude-code.zip",
    verdict="0 problems · 1 note · 2 skipped",
    notes_line="The note names",
    needs=["A value for <code>GITHUB_TOKEN</code>", "3 repos cloned at their pinned refs — <code>SETUP.md</code> says which", "An agent that reads <code>SETUP.md</code> first"],
    stages=[
        ("note", "3 items · 1 auto-added · no cycles", "0.2 s", "<p>You added 2, both from Public library. 1 more was auto-added because another item <code>requires</code> it: <code>playwright-mcp</code> for <code>webapp-testing</code>.</p>"),
        ("checked", "Checked — no two items declare a conflict", "0.1 s", None),
        ("skipped", "Skipped — no item declares a command", "—", None),
        ("checked", "Checked — no two items write to the same path", "0.1 s", None),
        ("note", "1 note · 1 key named", "0.1 s", note("<code>GITHUB_TOKEN</code> (github-mcp-server) is needed. It goes into <code>.env.example</code> as a name; the receiving machine supplies the value.")),
        ("skipped", "Skipped — no item defers to anything", "—", None),
        ("checked", "Checked — 3 external items, all pinned", "0.3 s", None),
        ("checked", "6 files for Claude Code", "0.1 s", '''<pre class="file">stripe-webhooks/
├── SETUP.md
├── .env.example                    GITHUB_TOKEN
├── .mcp.json                       playwright-mcp, github-mcp-server
└── .claude/skills/webapp-testing/  SKILL.md + 2 files</pre>'''),
        ("checked", "Written · 3 items", "0.2 s", '''<pre class="file"># Setup — stripe-webhooks (Claude Code)

Read this first and perform each step.

## webapp-testing
- External. Clone anthropics/skills at c74d647; take skills/webapp-testing.
- Requires playwright-mcp.

## github-mcp-server
- External. Clone github/github-mcp-server at v0.9.0.
- Needs GITHUB_TOKEN. Ask the person for it; do not invent one.
…</pre>'''),
        ("checked", "1 key, names only", "0.1 s", '<pre class="file">GITHUB_TOKEN=</pre>'),
    ])
SHELF_RUN["notes_line"] = "The note names"


def fix_notes_line(s, spec):
    return s.replace("Nothing in this project is a Problem. The note names what the receiving machine still has to supply.",
                     "Nothing in this project is a Problem. The note names what the receiving machine still has to supply.")


# ── the cases ─────────────────────────────────────────────────────────────────

CASES = {}


def case(cid):
    def deco(fn):
        CASES[cid] = fn
        return fn
    return deco


def P(case_id, n, name):
    return f"{n:02d}-{name}.html"


def projects(case_id, title, variant="orig", card_to=None, new_to=None, only_example=False):
    s = read("projects-default.html")
    if variant != "orig":
        s = must(s, "<span>14 items</span>", "<span>13 items</span>")
        s = must(s, '<dd class="meta">1 problem · 2 notes · 1 skipped</dd>', '<dd class="meta">0 problems · 2 notes · 1 skipped</dd>')
    if only_example:
        s = re.sub(r'(<ol class="card-grid">).*?(\n          <!-- The example project)', r"\1\2", s, count=1, flags=re.S)
    s = titled(inert(s), title, case_id)
    if card_to:
        s = live(s, "<a>acme-billing-api</a>", card_to)
    if new_to:
        s = live(s, '<a class="button button-primary">', new_to)
    return s


CLEAN = ("13 items · 3 auto-added · 1 detached", "Checked 2 days ago · for Claude Code · 0 problems · 2 notes · 1 skipped")
JUST = "Checked just now · for Claude Code · 0 problems · 2 notes · 1 skipped"


def tail_clean(c, start, variant="clean", counts="13 items · 3 auto-added · 1 detached", target="Claude Code"):
    """Run → Export → archive → back to the project: the shared ending of every case that checks clean."""
    n = start
    pages = {
        P(c, n, "run-loading"): run_loading(variant, c, f"{n:02d} · Run, checking", P(c, n + 1, "run-default"), target),
        P(c, n + 1, "run-default"): live(run_resolved(variant, c, f"{n + 1:02d} · Run, checked", target),
                                          f'<a class="button button-primary">{ICON}Export</a>', P(c, n + 2, "run-loading-export")),
        P(c, n + 2, "run-loading-export"): run_building(variant, c, f"{n + 2:02d} · Run, building the archive", P(c, n + 3, "run-success"), target),
        P(c, n + 3, "run-success"): run_success(variant, c, f"{n + 3:02d} · Run, archive in hand", P(c, n + 4, "project-default"), target),
        P(c, n + 4, "project-default"): project_page(variant, counts, JUST.replace("Claude Code", target), c, f"{n + 4:02d} · Project, checked just now"),
    }
    return pages


@case("main-success")
def _():
    c = "main-success"
    pages = {
        P(c, 1, "projects-default"): projects(c, "01 · Projects", "clean", card_to=P(c, 2, "project-default")),
        P(c, 2, "project-default"): project_page("clean", *CLEAN, c, "02 · Project", check_to=P(c, 3, "run-loading")),
    }
    pages.update(tail_clean(c, 3))
    return pages


@case("main-problem-fixed")
def _():
    c = "main-problem-fixed"
    s4 = inert(run_page("run-default.html", "orig", c, "04 · Run, 1 problem"))
    s4 = live(s4, '<a class="button">Remove eslint-autofix…</a>', P(c, 5, "run-remove"))
    s5 = inert(run_page("run-remove.html", "orig", c, "05 · Run, remove eslint-autofix?"))
    s5 = live(s5, '<a class="button button-primary">Remove from project</a>', P(c, 6, "run-loading"))
    pages = {
        P(c, 1, "projects-default"): projects(c, "01 · Projects", card_to=P(c, 2, "project-default")),
        P(c, 2, "project-default"): project_page("orig", *ORIG_HEAD, c, "02 · Project", check_to=P(c, 3, "run-loading")),
        P(c, 3, "run-loading"): run_loading("orig", c, "03 · Run, checking", P(c, 4, "run-default")),
        P(c, 4, "run-default"): s4,
        P(c, 5, "run-remove"): s5,
    }
    t = tail_clean(c, 6)
    t[P(c, 6, "run-loading")] = run_loading("clean", c, "06 · Run, eslint-autofix removed — checking again", P(c, 7, "run-default"),
                                            heading="eslint-autofix removed · checking again — stage 4 of 10")
    pages.update(t)
    return pages


@case("main-problem-exported")
def _():
    c = "main-problem-exported"
    s4 = inert(run_page("run-default.html", "orig", c, "04 · Run, 1 problem"))
    s4 = live(s4, f'<a class="button button-primary">{ICON}Export with 1 problem</a>', P(c, 5, "run-loading-export"))
    return {
        P(c, 1, "projects-default"): projects(c, "01 · Projects", card_to=P(c, 2, "project-default")),
        P(c, 2, "project-default"): project_page("orig", *ORIG_HEAD, c, "02 · Project", check_to=P(c, 3, "run-loading")),
        P(c, 3, "run-loading"): run_loading("orig", c, "03 · Run, checking", P(c, 4, "run-default")),
        P(c, 4, "run-default"): s4,
        P(c, 5, "run-loading-export"): run_building("orig", c, "05 · Run, building the archive with 1 problem", P(c, 6, "run-success")),
        P(c, 6, "run-success"): run_success("orig", c, "06 · Run, archive in hand — with the collision", P(c, 7, "project-default")),
        P(c, 7, "project-default"): project_page("orig", ORIG_HEAD[0], "Checked just now · for Claude Code · 1 problem · 2 notes · 1 skipped", c, "07 · Project, checked just now"),
    }


@case("main-target-changed")
def _():
    c = "main-target-changed"
    s4 = inert(run_page("run-default.html", "clean", c, "04 · Run, checked for Claude Code"))
    s4 = export_section(s4, export_clean(), "Export is the final stage, always live (§6).")
    s4 = control(s4, '<label class="pick">', "</label>", P(c, 5, "run-loading"), "pick")
    pages = {
        P(c, 1, "projects-default"): projects(c, "01 · Projects", "clean", card_to=P(c, 2, "project-default")),
        P(c, 2, "project-default"): project_page("clean", *CLEAN, c, "02 · Project", check_to=P(c, 3, "run-loading")),
        P(c, 3, "run-loading"): run_loading("clean", c, "03 · Run, checking for Claude Code", P(c, 4, "run-default")),
        P(c, 4, "run-default"): s4,
    }
    t = tail_clean(c, 5, target="Cursor")
    first = P(c, 5, "run-loading")
    t[first] = run_loading("clean", c, "05 · Run, target changed — checking again for Cursor", P(c, 6, "run-default"), "Cursor",
                           heading="Checking again for Cursor — stage 4 of 10")
    pages.update(t)
    return pages


def new_project_steps(c, n, entry_title):
    """From the empty project to the archive, assembling from My library (stripe-webhooks)."""
    lines = {"db-migrate": MY_LIBRARY[1][2]}
    ticked_mr = {"migration-reviewer", "db-migrate", "postgres-mcp", "seed-data"}
    pages = {}
    # the new project opens with the panel already open (Q34): tick straight away
    s = titled(inert(read("project-empty.html")), f"{n:02d} · {entry_title}", c)
    s = panel_tick(s, "migration-reviewer", P(c, n + 1, "project-configuring-loading-add"))
    pages[P(c, n, "project-empty")] = s
    n -= 1

    s = configuring_new(c, f"{n + 2:02d} · Configuring, adding migration-reviewer", "stripe-webhooks", "1 item",
                        panel_rows(MY_LIBRARY, {"migration-reviewer"}), stripe_set("mr-adding", True))
    pages[P(c, n + 2, "project-configuring-loading-add")] = wait(inert(s), P(c, n + 3, "project-configuring-default"))

    s = configuring_new(c, f"{n + 3:02d} · Configuring, what it brought with it", "stripe-webhooks", "4 items · 3 auto-added",
                        panel_rows(MY_LIBRARY, ticked_mr), stripe_set("mr", True), check_live=True)
    s = inert(s)
    s = panel_tick(s, "code-style", P(c, n + 4, "project-configuring-loading-add"))
    pages[P(c, n + 3, "project-configuring-default")] = s

    s = configuring_new(c, f"{n + 4:02d} · Configuring, adding code-style", "stripe-webhooks", "5 items · 3 auto-added",
                        panel_rows(MY_LIBRARY, ticked_mr | {"code-style"}), stripe_set("cs-adding", True), check_live=True)
    pages[P(c, n + 4, "project-configuring-loading-add")] = wait(inert(s), P(c, n + 5, "project-configuring-default"))

    s = configuring_new(c, f"{n + 5:02d} · Configuring, the set complete", "stripe-webhooks", "5 items · 3 auto-added",
                        panel_rows(MY_LIBRARY, ticked_mr | {"code-style"}), stripe_set("full", True), check_live=True)
    s = live(inert(s), '<a class="button button-primary">Save</a>', P(c, n + 6, "project-default"))
    pages[P(c, n + 5, "project-configuring-default")] = s

    pages[P(c, n + 6, "project-default")] = project_new(c, f"{n + 6:02d} · Project, saved", "stripe-webhooks",
                                                        "<span>5 items · 3 auto-added</span><span>Not checked yet</span>",
                                                        stripe_set("full", False).replace('<span class="mark"><span class="glyph glyph-note" aria-hidden="true"></span>Note</span>', ""),
                                                        check_to=P(c, n + 7, "run-loading"))
    k = n + 7
    pages[P(c, k, "run-loading")] = run_generic(STRIPE_RUN, c, f"{k:02d} · Run, checking", "loading", nxt=P(c, k + 1, "run-default"))
    pages[P(c, k + 1, "run-default")] = run_generic(STRIPE_RUN, c, f"{k + 1:02d} · Run, checked", "default", nxt=P(c, k + 2, "run-loading-export"))
    pages[P(c, k + 2, "run-loading-export")] = run_generic(STRIPE_RUN, c, f"{k + 2:02d} · Run, building the archive", "building", nxt=P(c, k + 3, "run-success"))
    pages[P(c, k + 3, "run-success")] = run_generic(STRIPE_RUN, c, f"{k + 3:02d} · Run, archive in hand", "success", back=P(c, k + 4, "project-default"))
    pages[P(c, k + 4, "project-default")] = project_new(c, f"{k + 4:02d} · Project, checked just now", "stripe-webhooks",
                                                        "<span>5 items · 3 auto-added</span><span>Checked just now · for Claude Code · 0 problems · 2 notes · 1 skipped</span>",
                                                        stripe_set("full", False))
    return pages


@case("main-new-project")
def _():
    c = "main-new-project"
    pages = {P(c, 1, "projects-default"): projects(c, "01 · Projects", new_to=P(c, 2, "project-empty"))}
    pages.update(new_project_steps(c, 2, "Project, just created — empty"))
    return pages


DELETE_MODAL = '''
    <!-- Deleting the example is confirmed (owner, 2026-09-27, Q34) — the one way Projects becomes empty. -->
    <div class="scrim" aria-hidden="true"></div>
    <dialog class="modal" open aria-labelledby="modal-title">
      <div class="sheet-head">
        <h2 id="modal-title">Delete repo-triage-kit?</h2>
      </div>
      <p><code>repo-triage-kit</code> leaves Projects. Its 7 items stay in the Public library, where it came from.</p>
      <p class="meta">This can’t be undone.</p>
      <div class="form-actions">
        <a class="button push">Cancel</a>
        <a class="button button-primary">Delete example</a>
      </div>
    </dialog>
'''


@case("main-no-projects")
def _():
    c = "main-no-projects"
    s1 = projects(c, "01 · Projects, only the example", only_example=True)
    s1 = live(s1, '<a class="button">Delete example…</a>', P(c, 2, "projects-delete"))
    s2 = projects(c, "02 · Projects, delete the example?", only_example=True)
    s2 = s2.replace("\n  </div>\n\n</body>", "\n" + DELETE_MODAL + "\n  </div>\n\n</body>", 1)
    s2 = live(s2, '<a class="button button-primary">Delete example</a>', P(c, 3, "projects-empty"))
    s = titled(inert(read("projects-empty.html")), "03 · Projects, none at all", c)
    s = live(s, '<a class="button button-primary">', P(c, 4, "project-empty"))
    pages = {P(c, 1, "projects-default"): s1, P(c, 2, "projects-delete"): s2, P(c, 3, "projects-empty"): s}
    pages.update(new_project_steps(c, 4, "Project, just created — empty"))
    return pages


@case("main-first-run")
def _():
    c = "main-first-run"
    pages = {P(c, 1, "projects-default"): projects(c, "01 · Projects, only the example", only_example=True, new_to=P(c, 2, "project-configuring-empty"))}
    s = titled(inert(read("project-configuring-empty.html")), "02 · Project, just created — My library empty on first run", c)
    pages[P(c, 2, "project-configuring-empty")] = live(s, '<a class="button button-primary">Open Public library</a>', P(c, 3, "project-configuring-public"))
    O = -1  # every later step is one earlier than before
    shelf_lines = {"playwright-mcp": "Required by <code>webapp-testing</code>"}
    s = configuring_new(c, "03 · Configuring, the Public library", "stripe-webhooks", "No items yet", panel_rows(PUBLIC_LIBRARY, set()), None, scope="Public library")
    pages[P(c, 3, "project-configuring-public")] = panel_tick(inert(s), "webapp-testing", P(c, 4, "project-configuring-loading-add"))
    s = configuring_new(c, "04 · Configuring, adding webapp-testing", "stripe-webhooks", "1 item", panel_rows(PUBLIC_LIBRARY, {"webapp-testing"}), shelf_set("wt-adding", True), scope="Public library")
    pages[P(c, 4, "project-configuring-loading-add")] = wait(inert(s), P(c, 5, "project-configuring-default"))
    s = configuring_new(c, "05 · Configuring, what it brought with it", "stripe-webhooks", "2 items · 1 auto-added", panel_rows(PUBLIC_LIBRARY, {"webapp-testing", "playwright-mcp"}), shelf_set("wt", True), scope="Public library", check_live=True)
    pages[P(c, 5, "project-configuring-default")] = panel_tick(inert(s), "github-mcp-server", P(c, 6, "project-configuring-loading-add"))
    s = configuring_new(c, "06 · Configuring, adding github-mcp-server", "stripe-webhooks", "3 items · 1 auto-added", panel_rows(PUBLIC_LIBRARY, {"webapp-testing", "playwright-mcp", "github-mcp-server"}), shelf_set("gh-adding", True), scope="Public library", check_live=True)
    pages[P(c, 6, "project-configuring-loading-add")] = wait(inert(s), P(c, 7, "project-configuring-default"))
    s = configuring_new(c, "07 · Configuring, the set complete", "stripe-webhooks", "3 items · 1 auto-added", panel_rows(PUBLIC_LIBRARY, {"webapp-testing", "playwright-mcp", "github-mcp-server"}), shelf_set("full", True), scope="Public library", check_live=True)
    pages[P(c, 7, "project-configuring-default")] = live(inert(s), '<a class="button button-primary">Save</a>', P(c, 8, "project-default"))
    pages[P(c, 8, "project-default")] = project_new(c, "08 · Project, saved", "stripe-webhooks", "<span>3 items · 1 auto-added · all from the Public library</span><span>Not checked yet</span>",
                                                    shelf_set("full", False).replace('<span class="mark"><span class="glyph glyph-note" aria-hidden="true"></span>Note</span>', ""), check_to=P(c, 9, "run-loading"))
    k = 9
    pages[P(c, k, "run-loading")] = run_generic(SHELF_RUN, c, f"{k:02d} · Run, checking", "loading", nxt=P(c, k + 1, "run-default"))
    pages[P(c, k + 1, "run-default")] = run_generic(SHELF_RUN, c, f"{k + 1:02d} · Run, checked", "default", nxt=P(c, k + 2, "run-loading-export"))
    pages[P(c, k + 2, "run-loading-export")] = run_generic(SHELF_RUN, c, f"{k + 2:02d} · Run, building the archive", "building", nxt=P(c, k + 3, "run-success"))
    pages[P(c, k + 3, "run-success")] = run_generic(SHELF_RUN, c, f"{k + 3:02d} · Run, archive in hand", "success", back=P(c, k + 4, "project-default"))
    pages[P(c, k + 4, "project-default")] = project_new(c, f"{k + 4:02d} · Project, checked just now", "stripe-webhooks",
                                                        "<span>3 items · 1 auto-added · all from the Public library</span><span>Checked just now · for Claude Code · 0 problems · 1 note · 2 skipped</span>",
                                                        shelf_set("full", False))
    return pages


def acme_add_steps(c, n, which, via_search):
    """Configure → (search → zero → row that creates → item form) or (tick) → adding → added → Save → project → the clean tail."""
    extra = {"query": QUERY, "stripe": STRIPE}[which]
    name = extra["name"]
    pages = {}
    added = f"Checked 2 days ago · for Claude Code · out of date since <code>{name}</code> was added"
    counts14 = "14 items · 3 auto-added · 1 detached"
    s = inert(configuring_page("clean", *CLEAN, c, f"{n:02d} · Configuring"))
    if via_search:
        s = control(s, '<label class="search">', "</label>", P(c, n + 1, "project-configuring-error-filtered"), "search")
    else:
        s = panel_tick(s, name, P(c, n + 1, "project-configuring-loading-add"))
    pages[P(c, n, "project-configuring-default")] = s
    k = n + 1
    if via_search:
        s = read("project-configuring-error-filtered.html")
        s = acme_set(s, "clean", remove=True)
        s = head_meta(s, *CLEAN)
        s = s.replace('value="sentry"', 'value="stripe"').replace("“sentry”", "“stripe”")
        s = titled(inert(s), f"{k:02d} · Configuring, “stripe” matches nothing", c)
        s = live(s, f'<a class="button">{ICON}Add “stripe” as a new item</a>', P(c, k + 1, "item-empty"))
        pages[P(c, k, "project-configuring-error-filtered")] = s
        # the Add item sheet, summoned over the Project (§8, the overlay's third door)
        form = re.search(r'    <div class="scrim".*?</dialog>\n', read("item-empty.html"), re.S).group(0)
        form = form.replace('<input name="name" placeholder="release-notes">', '<input name="name" value="stripe-rules">')
        form = form.replace('<option selected>skill</option><option>agent</option><option>prompt</option>', '<option>skill</option><option>agent</option><option selected>prompt</option>')
        form = form.replace('<input name="description" placeholder="One line: what it does and when it is used">', f'<input name="description" value="{STRIPE["desc"]}">')
        form = form.replace('<textarea name="content" placeholder="Write or paste it here"></textarea>', '<textarea name="content">Every POST to Stripe carries an Idempotency-Key. Webhook bodies are verified with the signing secret before anything reads them.</textarea>')
        form = form.replace('<input name="target" placeholder=".claude/skills/release-notes/SKILL.md">', '<input name="target" value="CLAUDE.md, appended">')
        s = pages[P(c, k, "project-configuring-error-filtered")]
        s = s.replace(f'<a class="button" href="{P(c, k + 1, "item-empty")}">', '<a class="button">')
        s = s.replace("\n  </div>\n\n</body>", "\n" + form + "\n  </div>\n\n</body>")
        s = titled(s, f"{k + 1:02d} · Add item, over the Project", c)
        s = btn(inert(s), '<button type="submit" class="button-primary">', P(c, k + 2, "project-configuring-loading-add"))
        pages[P(c, k + 1, "item-empty")] = s
        k += 2
    # adding: the row at once, what it requires after the round trip
    def with_adding(s):
        anchor = s.rindex("          <li>", 0, s.index(">github-mcp</a>"))
        row = set_row(name, extra["kind"], extra["desc"], "Adding — finding what it requires")
        return s[:anchor] + row + s[anchor:]
    s = configuring_page("clean", counts14, added, c, f"{k:02d} · Configuring, adding {name}", pre=with_adding)
    if not via_search:
        s = s.replace(f'<h3><a href="project-configuring-item.html">{name}</a><span class="tag">agent</span></h3>\n                <p class="state-line">Requires <code>postgres-mcp</code></p>\n              </div>\n              <label class="check"><input type="checkbox"> Add</label>',
                      f'<h3><a href="project-configuring-item.html">{name}</a><span class="tag">agent</span></h3>\n                <p class="state-line">Requires <code>postgres-mcp</code></p>\n              </div>\n              <label class="check"><input type="checkbox" checked> In this project</label>')
    pages[P(c, k, "project-configuring-loading-add")] = wait(inert(s), P(c, k + 1, "project-configuring-default"))
    s = configuring_page(which, counts14, added, c, f"{k + 1:02d} · Configuring, {name} in the set")
    if not via_search:
        s = s.replace('<p class="state-line">Requires <code>postgres-mcp</code></p>\n              </div>\n              <label class="check"><input type="checkbox"> Add</label>\n            </article>\n          </li>\n          <li>\n            <article class="row row-compact">\n              <div>\n                <h3><a href="project-detached',
                      '<p class="state-line">Requires <code>postgres-mcp</code></p>\n              </div>\n              <label class="check"><input type="checkbox" checked> In this project</label>\n            </article>\n          </li>\n          <li>\n            <article class="row row-compact">\n              <div>\n                <h3><a href="project-detached')
    pages[P(c, k + 1, "project-configuring-default")] = live(inert(s), '<a class="button button-primary">Save</a>', P(c, k + 2, "project-default"))
    pages[P(c, k + 2, "project-default")] = project_page(which, counts14, added, c, f"{k + 2:02d} · Project, saved — the check is out of date", check_to=P(c, k + 3, "run-loading"))
    pages.update(tail_clean(c, k + 3, variant=which, counts=counts14))
    return pages


@case("main-set-incomplete")
def _():
    c = "main-set-incomplete"
    pages = {
        P(c, 1, "projects-default"): projects(c, "01 · Projects", "clean", card_to=P(c, 2, "project-default")),
        P(c, 2, "project-default"): project_page("clean", *CLEAN, c, "02 · Project", configure_to=P(c, 3, "project-configuring-default")),
    }
    pages.update(acme_add_steps(c, 3, "query", via_search=False))
    return pages


@case("main-create-item")
def _():
    c = "main-create-item"
    pages = {
        P(c, 1, "projects-default"): projects(c, "01 · Projects", "clean", card_to=P(c, 2, "project-default")),
        P(c, 2, "project-default"): project_page("clean", *CLEAN, c, "02 · Project", configure_to=P(c, 3, "project-configuring-default")),
    }
    pages.update(acme_add_steps(c, 3, "stripe", via_search=True))
    return pages


# ── waits and failures ────────────────────────────────────────────────────────

@case("main-error-projects")
def _():
    c = "main-error-projects"
    s = titled(inert(read("projects-error-server.html")), "01 · Projects didn't load", c)
    s = live(s, f'<a class="button button-primary">{ICON}Load again</a>', P(c, 2, "projects-loading"))
    s2 = titled(inert(read("projects-loading.html")), "02 · Projects, loading", c)
    pages = {
        P(c, 1, "projects-error-server"): s,
        P(c, 2, "projects-loading"): wait(s2, P(c, 3, "projects-default")),
        P(c, 3, "projects-default"): projects(c, "03 · Projects", "clean", card_to=P(c, 4, "project-default")),
        P(c, 4, "project-default"): project_page("clean", *CLEAN, c, "04 · Project", check_to=P(c, 5, "run-loading")),
    }
    pages.update(tail_clean(c, 5))
    return pages


@case("main-error-project")
def _():
    c = "main-error-project"
    s = titled(inert(read("project-error.html")), "02 · Project didn't load", c)
    s = live(s, f'<a class="button button-primary">{ICON}Load again</a>', P(c, 3, "project-loading"))
    s3 = titled(inert(read("project-loading.html")), "03 · Project, loading", c)
    pages = {
        P(c, 1, "projects-default"): projects(c, "01 · Projects", "clean", card_to=P(c, 2, "project-error")),
        P(c, 2, "project-error"): s,
        P(c, 3, "project-loading"): wait(s3, P(c, 4, "project-default")),
        P(c, 4, "project-default"): project_page("clean", *CLEAN, c, "04 · Project", check_to=P(c, 5, "run-loading")),
    }
    pages.update(tail_clean(c, 5))
    return pages


@case("main-error-save")
def _():
    c = "main-error-save"
    removed = "Checked 2 days ago · for Claude Code · out of date since <code>eslint-autofix</code> was removed"
    s3 = btn(inert(configuring_page("orig", *ORIG_HEAD, c, "03 · Configuring")), '<button type="button" class="remove" aria-label="Remove eslint-autofix from this project">', P(c, 4, "project-configuring-default"))
    s4 = live(inert(configuring_page("clean", CLEAN[0], removed, c, "04 · Configuring, not saved yet")), '<a class="button button-primary">Save</a>', P(c, 5, "project-configuring-error-server"))
    callout = f'''<section aria-label="Items in this project">
        <!-- Save did not land (Q33's draft model, Q26): the project reads as it was, the draft stays here. -->
        <div class="callout" role="alert" style="margin-bottom: 16px">
          <span class="severity">Not saved</span>
          <span>Our server didn’t confirm the save, so acme-billing-api is as it was — 14 items, <code>eslint-autofix</code> still in it. Your changes are still here.</span>
          <span class="meta">503 · Service unavailable · 14:09</span>
          <div class="row-actions"><button type="button" class="button-primary">Save again</button><button type="button">Discard changes</button></div>
        </div>'''
    s5 = configuring_page("clean", CLEAN[0], "Checked 2 days ago · for Claude Code · 1 problem · 2 notes · 1 skipped", c, "05 · Configuring, the save didn't land",
                          pre=lambda s: must(s, '<section aria-label="Items in this project">', callout))
    s5 = btn(inert(s5), '<button type="button" class="button-primary">', P(c, 6, "project-default"))
    pages = {
        P(c, 1, "projects-default"): projects(c, "01 · Projects", card_to=P(c, 2, "project-default")),
        P(c, 2, "project-default"): project_page("orig", *ORIG_HEAD, c, "02 · Project", configure_to=P(c, 3, "project-configuring-default")),
        P(c, 3, "project-configuring-default"): s3,
        P(c, 4, "project-configuring-default"): s4,
        P(c, 5, "project-configuring-error-server"): s5,
        P(c, 6, "project-default"): project_page("clean", CLEAN[0], removed, c, "06 · Project, saved — the check is out of date", check_to=P(c, 7, "run-loading")),
    }
    pages.update(tail_clean(c, 7))
    return pages


@case("main-error-check")
def _():
    c = "main-error-check"
    s = run_page("run-loading.html", "clean", c, "04 · Run, the check didn't finish")
    s = must(s, '<h1 role="status">Checking — stage 4 of 10</h1>',
             '<h1 role="alert">The check didn’t finish</h1>\n        <p>Our server stopped answering at stage 4 of 10. Nothing in the project changed, and its last check still reads 2 days ago.</p>\n        <p class="meta">503 · Service unavailable · 14:05</p>')
    s = must(s, '<span class="glyph glyph-running" aria-hidden="true"></span>Checking', '<span class="glyph glyph-waiting" aria-hidden="true"></span>Stopped — our server didn’t answer')
    s = s.replace('<span class="glyph glyph-waiting" aria-hidden="true"></span>Waiting', '<span class="glyph glyph-waiting" aria-hidden="true"></span>Not run')
    s = export_section(s, f'''<section class="export-stage" aria-labelledby="export-title">
        <h2 id="export-title">11 · Export</h2>
        <p>The archive is built from a finished check. Checking again costs nothing.</p>
        <div class="export-actions">
          <a class="button button-primary">{ICON}Check again</a>
          <a class="button">Back to acme-billing-api</a>
        </div>
      </section>''', "Error: the check did not complete — whose failure it is, and a way on that does not depend on this run.")
    s = live(inert(s), f'<a class="button button-primary">{ICON}Check again</a>', P(c, 5, "run-loading"))
    pages = {
        P(c, 1, "projects-default"): projects(c, "01 · Projects", "clean", card_to=P(c, 2, "project-default")),
        P(c, 2, "project-default"): project_page("clean", *CLEAN, c, "02 · Project", check_to=P(c, 3, "run-loading")),
        P(c, 3, "run-loading"): run_loading("clean", c, "03 · Run, checking", P(c, 4, "run-error-check")),
        P(c, 4, "run-error-check"): s,
    }
    pages.update(tail_clean(c, 5))
    return pages


@case("main-error-export")
def _():
    c = "main-error-export"
    s6 = inert(run_page("run-error-export.html", "clean", c, "06 · Run, the archive didn't build"))
    s6 = must(s6, "Our server stopped at 12 of 18 files.", "Our server stopped at 12 of 17 files.")
    s6 = live(s6, f'<a class="button button-primary">{ICON}Export again</a>', P(c, 7, "run-loading-export"))
    pages = {
        P(c, 1, "projects-default"): projects(c, "01 · Projects", "clean", card_to=P(c, 2, "project-default")),
        P(c, 2, "project-default"): project_page("clean", *CLEAN, c, "02 · Project", check_to=P(c, 3, "run-loading")),
        P(c, 3, "run-loading"): run_loading("clean", c, "03 · Run, checking", P(c, 4, "run-default")),
        P(c, 4, "run-default"): live(run_resolved("clean", c, "04 · Run, checked"), f'<a class="button button-primary">{ICON}Export</a>', P(c, 5, "run-loading-export")),
        P(c, 5, "run-loading-export"): run_building("clean", c, "05 · Run, building the archive", P(c, 6, "run-error-export")),
        P(c, 6, "run-error-export"): s6,
        P(c, 7, "run-loading-export"): run_building("clean", c, "07 · Run, building the archive again", P(c, 8, "run-success")),
        P(c, 8, "run-success"): run_success("clean", c, "08 · Run, archive in hand", P(c, 9, "project-default")),
        P(c, 9, "project-default"): project_page("clean", CLEAN[0], JUST, c, "09 · Project, checked just now"),
    }
    return pages


# ── write, and check every case end to end ────────────────────────────────────

manifest = {}
for cid, fn in CASES.items():
    out = PROTO / cid
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    pages = fn()
    for name, html in pages.items():
        html = fix_notes_line(html, None)
        (out / name).write_text(html, encoding="utf-8")
    # walk: from step 01, every page must lead to the next by exactly one live link or one refresh, the last by none
    names = sorted(pages)
    for i, name in enumerate(names):
        t = (out / name).read_text(encoding="utf-8")
        nxt = re.findall(r'href="(\d\d-[a-z-]+\.html)"', t) + re.findall(r'url=(\d\d-[a-z-]+\.html)', t)
        stray = re.findall(r'<a\b[^>]*href="(?!\d\d-|https?:|\.\./)[^"]*"', t)
        want = names[i + 1] if i + 1 < len(names) else None
        assert not stray, f"{cid}/{name}: stray live links {stray}"
        assert (nxt == [want]) if want else (nxt == []), f"{cid}/{name}: leads to {nxt}, want {want}"
    manifest[cid] = names
    print(f"{cid}: {len(names)} steps ✓")

(PROTO / "_manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
