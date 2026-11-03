"""Phase 09, step 6: the test of a new screen — built from the system alone.

    python -X utf8 tools/build_examples.py

Writes design-system/examples/<page>.html: a screen the product does not have, which a job asks for, written as wireframe
markup here and dressed by build_mockups.transform like every screen, linking design-system/index.css alone. **No style,
no class of its own** — kit_check guard 13 refuses either. What the screen needed and the system did not have is not
drawn: it is written to design-system/backlog.md, by hand, as an order for the system (CLAUDE.md §18).

The screen is *Usage of My library*, for EJ-3 — *stop suspecting that half of what I keep is dead weight* — importance 3
for the primary persona and, in lesson 03's traceability matrix, only partial ticks (the usage line on a Library row and
the Filters popover's *In no project*). The owner picked it on 2026-11-03 (D6). **It is an example, not in the product**:
if the product ever wants it, it goes to the register. It says what §5's usage facts say and stops at their ceiling —
*is it used*, never *is it any good*. Three of its items (old-review-prompt, sql-formatter, notes-to-issues) exist only
here, so the screen has something used nowhere; the other eleven are My library's.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build_mockups as bm  # noqa: E402

OUT = ROOT / "design-system" / "examples"
MOCK = "../../04-wireframes/mockups/"

# name, kind, description, facts (html), usage (html)
GROUPS = [
    ("In no project", [
        ("old-review-prompt", "prompt", "The first review prompt, written before pr-reviewer existed.",
         "<span><code>CLAUDE.md</code>, appended</span>",
         "In no project · nothing requires it · never exported"),
        ("sql-formatter", "script", "Formats SQL files in place: two-space indents, upper-case keywords.",
         "<span><code>scripts/format-sql.sh</code></span>",
         "In no project · nothing requires it · last exported 5 months ago"),
        ("notes-to-issues", "script", "Turns a meeting note’s action items into draft GitHub issues.",
         "<span><code>scripts/notes-to-issues.mjs</code></span><span>Needs <code>GITHUB_TOKEN</code></span>",
         "In no project · nothing requires it · never exported"),
    ]),
    ("In one project", [
        ("migration-reviewer", "agent", "Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills.",
         "<span>requires <code>db-migrate</code>, <code>postgres-mcp</code></span>",
         'Used in <a href="{m}project-default.html">acme-billing-api</a>'),
        ("writing-style", "prompt", "Plain English for docs: short sentences, no marketing words, an example before every rule.",
         "<span><code>CLAUDE.md</code>, appended</span>",
         'Used in <a href="{m}project-default.html">docs-site-rewrite</a>'),
        ("link-checker", "script", "Crawls the built docs and lists every broken internal and external link, with the page it is on.",
         "<span><code>scripts/check-links.mjs</code></span>",
         'Used in <a href="{m}project-default.html">docs-site-rewrite</a>'),
        ("whisper", "app", "Speech-to-text, run locally on voice memos before they are summarised.",
         "<span><code>openai/whisper</code> @ <code>v20240930</code> · MIT</span>",
         'Used in <a href="{m}project-default.html">agent-dotfiles</a> · last exported 3 weeks ago'),
    ]),
    ("In two projects or more", [
        ("commit-conventions", "prompt", "Conventional commits, imperative mood, and a body that says why rather than what.",
         "<span><code>CLAUDE.md</code>, appended</span>", "Used in 4 projects · last exported 2 days ago"),
        ("code-style", "skill", "How I want TypeScript written: naming, imports, error handling, no default exports.",
         "<span><code>.claude/skills/code-style/SKILL.md</code></span>", "Used in 3 projects · last exported 2 days ago"),
        ("db-migrate", "script", "Generates a Postgres migration from a schema diff and runs it — dry run first, then for real.",
         "<span><code>scripts/db-migrate.sh</code> + 2 files</span>",
         "Used in 3 projects · 1 item requires this · last exported 12 days ago"),
        ("seed-data", "script", "Loads a small, realistic dataset into a fresh database.",
         "<span><code>scripts/seed-data.sh</code></span>", "Used in 3 projects · 1 item requires this"),
        ("github-mcp", "mcp", "Issues, pull requests and code search on GitHub, through GitHub’s own server.",
         "<span><code>github/github-mcp-server</code> @ <code>v0.9.0</code> · MIT</span>", "Used in 3 projects"),
        ("postgres-mcp", "mcp", "Read-only Postgres access for the agent: schema, explain plans, sample rows.",
         "<span><code>modelcontextprotocol/servers-archived</code> @ <code>9be4674</code> · MIT</span>",
         "Used in 2 projects · 1 item requires this"),
        ("pr-reviewer", "agent", "Reads a pull request diff and leaves review comments the way I would write them.",
         "<span><code>.claude/agents/pr-reviewer.md</code></span>", "Used in 2 projects · detached in 1"),
    ]),
]


def row(name, kind, desc, facts, usage):
    return f"""          <li>
            <article class="row row-tight">
              <div>
                <h3><a href="{MOCK}item-default.html">{name}</a><span class="tag">{kind}</span></h3>
                <p class="description">{desc}</p>
                <p class="facts meta">{facts}</p>
              </div>
              <p class="usage meta">{usage.format(m=MOCK)}</p>
              <div class="row-actions">
                <a class="button" href="{MOCK}item-default.html">Edit</a>
                <a class="button" href="usage-delete.html">Delete…</a>
              </div>
            </article>
          </li>"""


def groups():
    out = []
    for k, (title, rows) in enumerate(GROUPS):
        out.append(f"""      <section aria-labelledby="group-{k}">
        <h2 class="heading-small" id="group-{k}">{title} · {len(rows)}</h2>
        <ol class="row-list">
{chr(10).join(row(*r) for r in rows)}
        </ol>
      </section>""")
    return "\n\n".join(out)


DIALOG = """
    <div class="scrim" aria-hidden="true"></div>
    <dialog class="modal" open aria-labelledby="modal-title">
      <div class="sheet-head">
        <h2 id="modal-title">Delete old-review-prompt?</h2>
      </div>
      <p><strong><code>old-review-prompt</code> is used in no project, and nothing requires it.</strong></p>
      <p>No project changes, and no check goes out of date.</p>
      <p class="meta">This can’t be undone.</p>
      <div class="form-actions">
        <a class="button push" href="usage.html">Cancel</a>
        <a class="button button-primary" href="usage.html">Delete</a>
      </div>
    </dialog>
"""


def usage_main():
    total = sum(len(r) for _, r in GROUPS)
    counts = " · ".join(f"{len(r)} {t[0].lower() + t[1:]}" for t, r in GROUPS)
    return f"""      <section aria-labelledby="page-title">
        <div class="page-head">
          <div>
            <h1 id="page-title">Usage of My library <span class="tag tag-state">Example</span></h1>
            <p class="meta head-meta">{total} items · {counts}. Where each item is used, what requires it, and when it was
              last exported. It says whether an item is used, never whether it is any good.</p>
          </div>
        </div>
      </section>

      <section aria-label="Find">
        <form class="find" role="search">
          <label class="search">
            <span class="icon" aria-hidden="true"></span>
            <input type="search" name="q" placeholder="Search My library — migrate, GITHUB_TOKEN, review">
          </label>
          <button type="button" class="filters-button"><span class="icon" aria-hidden="true"></span>Filters</button>
        </form>
      </section>

{groups()}"""


# ------------------------------------------------------------------ the second test: Copies of code-style (RJ-3, H-J3)
# The original in My library beside its copy in each project that uses it: which copy is linked, which is detached and
# which fields differ. Owner's pick, 2026-11-03, the second test. For this example code-style is detached in two of its
# three projects; in the wireframes it is linked in all three.
ORIGINAL = """---
name: code-style
description: How I want TypeScript written.
---
Named exports only. Imports sorted: node, packages, local.
Errors are typed and thrown, never returned as strings."""

COPIES = [
    ("acme-billing-api", "Detached", "2 fields differ from the original.", "Edited 9 days ago",
     [("Lands at", ".claude/skills/acme-code-style/SKILL.md", ".claude/skills/code-style/SKILL.md")],
     """---
name: code-style
description: How Acme wants TypeScript written.
---
Named exports only. Imports sorted: node, packages, local.
Errors are typed and thrown, never returned as strings.
Money is integer cents. Never a float, never a string."""),
    ("agent-dotfiles", "Linked", "Follows the original. Nothing differs.", "Gets every edit to the original", [], None),
    ("docs-site-rewrite", "Detached", "1 field differs from the original.", "Edited 3 weeks ago", [],
     """---
name: code-style
description: How I want TypeScript written.
---
Named exports only, except pages/: Next.js needs a default export there.
Errors are typed and thrown, never returned as strings."""),
]


def copy_card(project, state, says, when, fields, content):
    diff = []
    for label, value, original in fields:
        diff.append(f"""              <p class="meta">{label} <code>{value}</code></p>
              <p class="meta">Original: <code>{original}</code> · <button type="button" class="link-button">Reset this field</button></p>""")
    if content:
        diff.append(f"""              <p class="meta">Content</p>
              <pre class="file">{content}</pre>
              <details class="library-version">
                <summary class="meta">Original · <span class="link-button">Reset this field</span></summary>
                <pre class="file">{ORIGINAL}</pre>
              </details>""")
    actions = ("""              <div class="row-actions">
                <button type="button">Reset to the original</button>
                <a class="button" href="copies-promote.html">Promote to My library…</a>
              </div>""" if state == "Detached" else f"""              <div class="row-actions">
                <a class="button" href="{MOCK}project-default.html">Open the project</a>
              </div>""")
    return f"""          <li>
            <article class="card">
              <div>
                <h2><a href="{MOCK}project-default.html">{project}</a><span class="tag tag-state">{state}</span></h2>
                <p class="description">{says}</p>
                <p class="facts meta"><span>{when}</span></p>
              </div>
{chr(10).join(diff)}
{actions}
            </article>
          </li>"""


def copies_main():
    return f"""      <section aria-labelledby="page-title">
        <div class="page-head">
          <div>
            <h1 id="page-title">Copies of code-style <span class="tag tag-state">Example</span></h1>
            <p class="meta head-meta">The original in My library, and its copy in each project that uses it. A linked copy
              gets every edit to the original; a detached copy keeps its own.</p>
          </div>
          <div class="head-actions">
            <a class="button button-primary" href="{MOCK}item-default.html">Edit the original</a>
          </div>
        </div>
      </section>

      <div class="callout callout-reminder">
        <span class="severity">Editing the original reaches 1 of 3 projects · saving un-checks agent-dotfiles</span>
        <span><a href="{MOCK}project-default.html">agent-dotfiles</a> is linked and gets the edit.
          <a href="{MOCK}project-default.html">acme-billing-api</a> and
          <a href="{MOCK}project-default.html">docs-site-rewrite</a> are detached and keep their own copies until one is
          reset.</span>
      </div>

      <section aria-labelledby="original-title">
        <h2 class="heading-small" id="original-title">The original</h2>
        <ol class="row-list">
          <li>
            <article class="row row-tight">
              <div>
                <h3><a href="{MOCK}item-default.html">code-style</a><span class="tag">skill</span></h3>
                <p class="description">How I want TypeScript written: naming, imports, error handling, no default exports.</p>
                <p class="facts meta"><span><code>.claude/skills/code-style/SKILL.md</code></span><span>Defers to <em>the client’s ESLint config</em></span></p>
              </div>
              <p class="usage meta">Used in 3 projects · detached in 2 · last exported 2 days ago</p>
            </article>
          </li>
        </ol>
      </section>

      <section aria-labelledby="copies-title">
        <h2 class="heading-small" id="copies-title">In 3 projects</h2>
        <ol class="card-grid">
{chr(10).join(copy_card(*c) for c in COPIES)}
        </ol>
      </section>"""


PROMOTE = """
    <div class="scrim" aria-hidden="true"></div>
    <dialog class="modal" open aria-labelledby="modal-title">
      <div class="sheet-head">
        <h2 id="modal-title">Promote acme-billing-api’s code-style to My library?</h2>
      </div>
      <form class="form">
        <label class="field"><span>Name of the new item</span><input name="name" value="acme-code-style"></label>
      </form>
      <p>It becomes a new item in My library with this project’s changes, and acme-billing-api links to it. The original
        <code>code-style</code>, and the two other projects that use it, stay as they are.</p>
      <div class="form-actions">
        <a class="button push" href="copies.html">Cancel</a>
        <a class="button button-primary" href="copies.html">Promote</a>
      </div>
    </dialog>
"""


def source(title, main, dialog, job):
    return f"""<!doctype html>
<!--
  Example: {title}. Generated by tools/build_examples.py; do not edit by hand.
  An example, not in the product — lesson 09, step 6, the test of a new screen built from the system alone.
  {job} No style of its own: design-system/index.css only.
  What it lacked is in design-system/backlog.md, not drawn here.
-->
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} · example</title>
  <link rel="stylesheet" href="wireframe.css">
</head>
<body class="product-page">

  <div class="canvas">

    <header class="app-header">
      <span class="product"><span class="icon" aria-hidden="true"></span>AI Stack Builder</span>
      <nav class="app-nav" aria-label="Global">
        <ul>
          <li><a href="{MOCK}library-my-default.html" aria-current="page">My library</a></li>
          <li><a href="{MOCK}library-public-default.html">Public library</a></li>
          <li><a href="{MOCK}projects-default.html">Projects</a></li>
        </ul>
      </nav>
      <p class="account" aria-label="Signed in as Maya Chen">
        <span class="image avatar" aria-hidden="true"></span>
        <span>Maya Chen</span>
      </p>
    </header>

    <main class="app-main">

{main}

    </main>
{dialog}
  </div>

</body>
</html>
"""


USAGE_JOB = "Job: EJ-3 (jtbd.md). Patterns: Browse head, Confirmation."
COPIES_JOB = "Jobs: RJ-3 and H-J3 (jtbd.md). Pattern: Dialog with a field."
# slug, title, render() -> the full page source
PAGES = [
    ("usage", "Usage of My library", lambda: source("Usage of My library", usage_main(), "", USAGE_JOB)),
    ("usage-delete", "Usage of My library · delete", lambda: source("Usage of My library · delete", usage_main(), DIALOG, USAGE_JOB)),
    ("copies", "Copies of code-style", lambda: source("Copies of code-style", copies_main(), "", COPIES_JOB)),
    ("copies-promote", "Copies of code-style · promote", lambda: source("Copies of code-style · promote", copies_main(), PROMOTE, COPIES_JOB)),
]


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, title, render in PAGES:
        out = bm.transform(render(), "../../", f"example-{slug}", [], kit_href=["../index.css"], frame=False)
        out = re.sub(r"<title>(.*?) — design</title>", r"<title>\1</title>", out)
        (OUT / f"{slug}.html").write_text(out, encoding="utf-8")
    print(f"examples: {len(PAGES)} pages — " + " · ".join(s for s, _, _ in PAGES))


if __name__ == "__main__":
    build()
