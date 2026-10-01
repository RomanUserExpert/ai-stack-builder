"""The other six flows, up to five cases each, less detailed than the main job: wireframe pages as drawn,
wired step to step. Reuses build_main.py's helpers and cases, writes every case, walks every case,
and regenerates the viewer's Flows group."""
import pathlib, re, json, html, shutil

HERE = pathlib.Path(__file__).parent
src = (HERE / "build_main.py").read_text(encoding="utf-8")
exec(src.split("# ── write, and check every case end to end")[0])


# ── a chain: each step a page, wired to the next ──────────────────────────────

def row_mark(s, name, marker):
    """The first `marker` after the row whose name is `name`."""
    i = s.find(f">{name}</a>")
    if i < 0:
        i = s.index(f">{name}<span")
    return s.index(marker, i)


def after(s, anchor, marker):
    return s.index(marker, s.index(anchor))


def wire(s, how, target):
    kind = how[0]
    if kind == "a":
        m = how[1]
        if m not in s:   # the same link drawn with or without its icon
            k = m.index(">") + 1
            alt = m[:k] + m[k + len(ICON):] if m[k:].startswith(ICON) else m[:k] + ICON + m[k:]
            m = alt if alt in s else m
        return live(s, m, target)
    if kind == "btn":
        return btn(s, how[1], target)
    if kind == "wait":
        return wait(s, target)
    if kind in ("row", "after"):
        k = row_mark(s, how[1], how[2]) if kind == "row" else after(s, how[1], how[2])
        m = how[2]
        if m.startswith("<button"):
            j = s.index("</button>", k)
            inner = s[k + len(m):j]
            cls = re.search(r'class="([^"]*)"', m)
            aria = re.search(r'aria-label="([^"]*)"', m)
            a = f'<a class="button{" " + cls.group(1) if cls else ""}" href="{target}"' + (f' aria-label="{aria.group(1)}"' if aria else "") + ">"
            return s[:k] + a + inner + "</a>" + s[j + len("</button>"):]
        return s[:k] + m.replace("<a", f'<a href="{target}"', 1) + s[k + len(m):]
    raise ValueError(kind)


def chain(c, steps):
    """steps: (name, title, source, how, transform). source: a pages/ file, or a function returning html."""
    pages, files = {}, [P(c, i, st[0]) for i, st in enumerate(steps, 1)]
    for i, (name, title, source, how, tf) in enumerate(steps, 1):
        s = read(source) if isinstance(source, str) else source()
        if tf:
            s = tf(s)
        s = titled(inert(s), f"{i:02d} · {title}", c)
        if how:
            s = wire(s, how, files[i])
        pages[files[i - 1]] = s
    return pages


def modal(html_body):
    """Append a confirmation over the page — the wireframes' <dialog class="modal"> over a scrim."""
    def tf(s):
        return s.replace("\n  </div>\n\n</body>", "\n" + html_body + "\n  </div>\n\n</body>", 1)
    return tf


def seq(*fns):
    def tf(s):
        for f in fns:
            if f:
                s = f(s)
        return s
    return tf


def sub_(a, b):
    return lambda s: must(s, a, b)


def subs(pairs):
    return seq(*(sub_(a, b) for a, b in pairs))


BTN_PRIMARY = '<a class="button button-primary">'

# ── Single-item export ────────────────────────────────────────────────────────

@case("item-success")
def _():
    return chain("item-success", [
        ("library-my-default", "My library", "library-my-default.html", ("row", "migration-reviewer", '<a class="button">Export</a>'), None),
        ("run-item-loading", "Run, checking one item", "run-item-loading.html", ("wait",), None),
        ("run-item-default", "Run, checked", "run-item-default.html", ("a", f"{BTN_PRIMARY}Export</a>"), None),
        ("run-item-success", "Run, archive in hand", "run-item-success.html", None, None),
    ])


@case("item-from-shelf")
def _():
    return chain("item-from-shelf", [
        ("library-my-error-filtered", "My library, “terraform” matches nothing", "library-my-error-filtered.html", ("a", '<a>Public library</a>'), None),
        ("library-public-default", "Public library", "library-public-default.html", ("row", "playwright-mcp", '<a class="button">Export</a>'), None),
        ("run-item-loading", "Run, checking one item", "run-item-loading.html", ("wait",), None),
        ("run-item-default", "Run, checked", "run-item-default.html", ("a", f"{BTN_PRIMARY}Export</a>"), None),
        ("run-item-success", "Run, archive in hand", "run-item-success.html", None, None),
    ])


@case("item-not-found")
def _():
    return chain("item-not-found", [
        ("library-my-error-filtered", "My library, nothing matches", "library-my-error-filtered.html", ("a", '<a>Public library</a>'), None),
        ("library-public-error-filtered", "Public library, nothing matches either — stuck", "library-public-error-filtered.html", None, None),
    ])


@case("item-error-check")
def _():
    return chain("item-error-check", [
        ("library-my-default", "My library", "library-my-default.html", ("row", "migration-reviewer", '<a class="button">Export</a>'), None),
        ("run-item-loading", "Run, checking one item", "run-item-loading.html", ("wait",), None),
        ("run-item-error", "Run, the check didn't finish", "run-item-error.html", ("a", f"{BTN_PRIMARY}{ICON}Check again</a>"), None),
        ("run-item-loading", "Run, checking again", "run-item-loading.html", ("wait",), None),
        ("run-item-default", "Run, checked", "run-item-default.html", ("a", f"{BTN_PRIMARY}Export</a>"), None),
        ("run-item-success", "Run, archive in hand", "run-item-success.html", None, None),
    ])


# ── RJ-1 · know what the other side will still need ───────────────────────────

STALE = "Checked 5 days ago · for Claude Code · out of date since <code>code-style</code> was edited in the Library"


def open_handover(s):
    """The handover read before Export: every handover stage open."""
    for name in ("What the archive contains", "SETUP.md — for the agent that opens it", ".env.example"):
        i = s.index(f'<span class="name">{name}</span>')
        k = s.rindex("<details>", 0, i)
        s = s[:k] + "<details open>" + s[k + len("<details>"):]
    return s


@case("rj1-stale-then-read")
def _():
    c = "rj1-stale-then-read"
    return chain(c, [
        ("project-default", "Project, the check out of date", lambda: project_page("clean", CLEAN[0], STALE, c, ""), ("a", f"{BTN_PRIMARY}{ICON}Check</a>"), None),
        ("run-loading", "Run, checking", lambda: run_page("run-loading.html", "clean", c, ""), ("wait",), None),
        ("run-default", "Run, the handover read before Export", lambda: export_section(run_page("run-default.html", "clean", c, ""), export_clean(), "Export is the final stage."),
         ("a", f"{BTN_PRIMARY}{ICON}Export for Claude Code</a>"), open_handover),
        ("run-loading-export", "Run, building the archive", lambda: run_building("clean", c, "", "x"), ("wait",), lambda s: re.sub(r'\n  <meta http-equiv="refresh"[^>]*>', "", s)),
        ("run-success", "Run, archive in hand — the other side is known", lambda: run_success("clean", c, "", "x"), None, lambda s: s.replace(' href="x"', "")),
    ])


PREVIEW_FAILED = '''<li>
            <details open>
              <summary><span class="n">09</span><span class="name">SETUP.md — for the agent that opens it</span><span class="result"><span class="glyph glyph-waiting" aria-hidden="true"></span>Couldn’t be written</span><span class="time">—</span></summary>
              <div class="stage-body">
                <div class="callout" role="alert">
                  <span class="severity">Missing, not empty</span>
                  <span><code>SETUP.md</code> couldn’t be produced — the server stopped while writing it. What you would read here is missing because something broke on our side, not because there is nothing to say (Q28). <span class="meta">503 · 14:06</span></span>
                  <div class="row-actions"><a class="button button-primary">Write it again</a></div>
                </div>
              </div>
            </details>
          </li>'''


@case("rj1-preview-failed")
def _():
    c = "rj1-preview-failed"
    def failed(s):
        return re.sub(r'<li>\s*<details>\s*<summary><span class="n">09</span>.*?</li>', PREVIEW_FAILED, s, count=1, flags=re.S)
    resolved = lambda: export_section(run_page("run-default.html", "clean", c, ""), export_clean(), "Export is the final stage.")
    return chain(c, [
        ("project-default", "Project", lambda: project_page("clean", *CLEAN, c, ""), ("a", f"{BTN_PRIMARY}{ICON}Check</a>"), None),
        ("run-loading", "Run, checking", lambda: run_page("run-loading.html", "clean", c, ""), ("wait",), None),
        ("run-error-setup", "Run, SETUP.md couldn't be written (Q28)", resolved, ("a", '<a class="button button-primary">Write it again</a>'), failed),
        ("run-default", "Run, SETUP.md written — read it before Export", resolved, ("a", f"{BTN_PRIMARY}{ICON}Export for Claude Code</a>"), open_handover),
        ("run-success", "Run, archive in hand", lambda: run_success("clean", c, "", "x"), None, lambda s: s.replace(' href="x"', "")),
    ])


# ── RJ-2 · what my pieces drag in, and where two will fight ───────────────────

DRAWER_DBM = '''<aside class="drawer" aria-labelledby="drawer-title">
          <div class="drawer-head">
            <h2 id="drawer-title">db-migrate <span class="tag">script</span> <span class="tag tag-state">Auto-added</span></h2>
            <a class="button close" aria-label="Close"><span class="icon" aria-hidden="true"></span></a>
          </div>
          <p class="description">Generates a Postgres migration from a schema diff and runs it, dry run first.</p>
          <div class="callout callout-quiet">
            <span class="severity">Pulled in by migration-reviewer</span>
            <span>It has no remove of its own: it leaves the set when <code>migration-reviewer</code> does, and takes <code>seed-data</code> with it.</span>
          </div>
          <section class="drawer-section" aria-labelledby="d-deps">
            <h3 id="d-deps">Dependencies</h3>
            <dl class="drawer-facts">
              <dt>Required by</dt><dd><code>migration-reviewer</code></dd>
              <dt>Requires</dt><dd><code>seed-data</code></dd>
              <dt>Lands at</dt><dd><code>scripts/db-migrate.sh</code> + 2 files</dd>
            </dl>
          </section>
          <div class="drawer-actions">
            <a class="button">Detach to edit here</a>
            <a class="button">Open in My library</a>
          </div>
        </aside>'''


@case("rj2-auto-added-holds")
def _():
    c = "rj2-auto-added-holds"
    removed = "Checked 2 days ago · for Claude Code · out of date since <code>migration-reviewer</code> was removed"
    def drawer(s):
        s = re.sub(r'<aside class="drawer".*?</aside>', DRAWER_DBM, s, count=1, flags=re.S)
        s = s.replace("set-item is-selected", "set-item", 1)
        i = s.index(">db-migrate</a><span class=\"tag\">script</span><span class=\"tag tag-state\">Auto-added")
        k = s.rindex('<article class="row row-tight set-item">', 0, i)
        return s[:k] + '<article class="row row-tight set-item is-selected">' + s[k + len('<article class="row row-tight set-item">'):]
    drop_mr = lambda s: drop_li(s, ">migration-reviewer</a><span class=\"tag\">agent</span></h3>\n                <p class=\"description\">Reads a migration")
    return chain(c, [
        ("project-configuring-default", "Configuring", "project-configuring-default.html",
         ("after", 'aria-label="The set"', '<a>db-migrate</a>'), None),
        ("project-configuring-item", "Configuring, db-migrate open — it will not go on its own", "project-configuring-item.html",
         ("btn", '<button type="button" class="remove" aria-label="Remove migration-reviewer and the 3 items it brings">'), drawer),
        ("project-configuring-default", "Configuring, migration-reviewer removed — and the 3 it brought", "project-configuring-default.html",
         ("a", '<a class="button button-primary">Save</a>'), seq(drop_mr, subs([(ORIG_HEAD[0], "10 items · 1 detached"), (ORIG_HEAD[1], removed)]))),
        ("project-default", "Project, saved", "project-default.html", None,
         seq(lambda s: drop_li(s, ">migration-reviewer</a><span class=\"tag\">agent</span></h3>\n                <p class=\"description\">Reads a migration"),
             subs([(ORIG_HEAD[0], "10 items · 1 detached"), (ORIG_HEAD[1], removed)]))),
    ])


DANGLING = '''<li>
            <details open>
              <summary><span class="n">01</span><span class="name">Resolve the set</span><span class="result"><span class="glyph glyph-problem" aria-hidden="true"></span>1 problem · 1 requirement can’t be found</span><span class="time">0.3 s</span></summary>
              <div class="stage-body">
                <div class="callout">
                  <span class="severity">Problem</span>
                  <span><code>db-migrate</code> requires <code>seed-data</code>, which is no longer in My library. The archive will contain <code>db-migrate</code> without it.</span>
                  <div class="row-actions"><a class="button">Edit db-migrate</a></div>
                </div>
              </div>
            </details>
          </li>'''


@case("rj2-requirement-missing")
def _():
    c = "rj2-requirement-missing"
    gone = "Checked 2 days ago · for Claude Code · out of date since <code>seed-data</code> was deleted from My library"
    edited = "Checked 2 days ago · for Claude Code · out of date since <code>db-migrate</code> was edited in the Library"
    def dangling(s):
        s = re.sub(r'<li>\s*<details>\s*<summary><span class="n">01</span>.*?</li>', DANGLING, s, count=1, flags=re.S)
        return s.replace("<strong>0 problems · 2 notes · 1 skipped</strong>", "<strong>1 problem · 2 notes · 1 skipped</strong>")
    no_seed = lambda s: drop_li(s, ">seed-data</a>", indent="                  ") if ">seed-data</a>" in s else s
    return chain(c, [
        ("project-default", "Project, seed-data deleted from the Library", lambda: project_page("clean", CLEAN[0], gone, c, ""), ("a", f"{BTN_PRIMARY}{ICON}Check</a>"), None),
        ("run-loading", "Run, checking", lambda: run_page("run-loading.html", "clean", c, ""), ("wait",), None),
        ("run-default", "Run, 1 problem — a requirement that is not there", lambda: export_section(run_page("run-default.html", "clean", c, ""), export_clean(), "Export is the final stage."),
         ("a", '<a class="button">Edit db-migrate</a>'), dangling),
        ("item-default", "Edit db-migrate — take seed-data out of Requires", "item-default.html", ("btn", '<button type="submit" class="button-primary">'), None),
        ("project-default", "Project, db-migrate saved — the check out of date", lambda: project_page("clean", CLEAN[0], edited, c, ""), ("a", f"{BTN_PRIMARY}{ICON}Check</a>"), None),
        ("run-loading", "Run, checking again", lambda: run_page("run-loading.html", "clean", c, ""), ("wait",), None),
        ("run-default", "Run, nothing will fight", lambda: export_section(run_page("run-default.html", "clean", c, ""), export_clean(), "Export is the final stage."), None, None),
    ])


# ── RJ-3 · fix something once and have the fix reach every copy ───────────────

def projects_out_of_date(s):
    s = must(s, '<dd class="meta">1 problem · 2 notes · 1 skipped</dd>', '<dd class="meta">Out of date since <code>db-migrate</code> was edited in the Library</dd>')
    s = must(s, '<dd class="meta">1 problem · 1 note · 0 skipped</dd>', '<dd class="meta">Out of date since <code>db-migrate</code> was edited in the Library</dd>')
    return must(s, "Out of date since <code>code-style</code> was edited in the Library", "Out of date since <code>db-migrate</code> was edited in the Library")


@case("rj3-edit-reaches-all")
def _():
    return chain("rj3-edit-reaches-all", [
        ("library-my-default", "My library", "library-my-default.html", ("row", "db-migrate", '<a class="button">Edit</a>'), None),
        ("item-default", "Edit db-migrate — used in 3 projects, saving un-checks all three", "item-default.html", ("btn", '<button type="submit" class="button-primary">'), None),
        ("library-my-default", "My library, saved once", "library-my-default.html", ("a", '<a>Projects</a>'), None),
        ("projects-default", "Projects — all three out of date, none checked on the old version", "projects-default.html", None, projects_out_of_date),
    ])


@case("rj3-save-failed")
def _():
    return chain("rj3-save-failed", [
        ("library-my-default", "My library", "library-my-default.html", ("row", "db-migrate", '<a class="button">Edit</a>'), None),
        ("item-default", "Edit db-migrate", "item-default.html", ("btn", '<button type="submit" class="button-primary">'), None),
        ("item-error", "Edit db-migrate — the edit didn't land (Q26)", "item-error.html", ("btn", '<button type="button" class="button-primary">Save again'), None),
        ("library-my-default", "My library, saved", "library-my-default.html", None, None),
    ])


RESET_PAIRS = [("differs from the library in <em>content</em> and <em>lands at</em>", "<code>.claude/agents/pr-reviewer.md</code> · back to the library version")]


def pr_linked(s):
    s = must(s, '<a href="project-detached-default.html">pr-reviewer</a><span class="tag">agent</span><span class="tag tag-state">Detached</span>',
             '<a href="project-detached-default.html">pr-reviewer</a><span class="tag">agent</span>')
    return subs(RESET_PAIRS)(s)


@case("rj3-detached-reset")
def _():
    c = "rj3-detached-reset"
    reset = "Checked 2 days ago · for Claude Code · out of date since <code>pr-reviewer</code> was reset"
    return chain(c, [
        ("project-default", "Project — pr-reviewer is detached", "project-default.html", ("a", '<a class="button">Configure</a>'), None),
        ("project-configuring-default", "Configuring", "project-configuring-default.html", ("after", 'aria-label="The set"', '<a>pr-reviewer</a>'), None),
        ("project-detached-default", "Configuring, pr-reviewer open — what differs from the library", "project-detached-default.html", ("btn", '<button type="button">Reset whole item'), None),
        ("project-configuring-default", "Configuring, pr-reviewer back to the library version", "project-configuring-default.html", ("a", '<a class="button button-primary">Save</a>'),
         seq(pr_linked, subs([(ORIG_HEAD[0], "14 items · 3 auto-added"), (ORIG_HEAD[1], reset)]))),
        ("project-default", "Project, saved — the fix reaches this copy too", "project-default.html", None,
         seq(lambda s: must(s, '<span class="tag tag-state">Detached</span></h3>', "</h3>"), subs(RESET_PAIRS), subs([(ORIG_HEAD[0], "14 items · 3 auto-added"), (ORIG_HEAD[1], reset)]))),
    ])


PROMOTE_MODAL = '''
    <!-- Promote (§5, Q4): a new item, never a merge into the original. It happens at once — it creates a library item. -->
    <div class="scrim" aria-hidden="true"></div>
    <dialog class="modal" open aria-labelledby="modal-title">
      <div class="sheet-head">
        <h2 id="modal-title">Promote pr-reviewer to My library?</h2>
      </div>
      <form class="form">
        <label class="field"><span>Name of the new item</span><input name="name" value="acme-pr-reviewer"></label>
      </form>
      <p>It becomes a new item in My library with this project’s changes, and this row links to it. The original <code>pr-reviewer</code>, and the other project that uses it, stay as they are.</p>
      <div class="form-actions">
        <a class="button push">Cancel</a>
        <a class="button button-primary">Promote</a>
      </div>
    </dialog>
'''


def promoted(s):
    s = must(s, '<a href="project-detached-default.html">pr-reviewer</a><span class="tag">agent</span><span class="tag tag-state">Detached</span>',
             '<a href="project-detached-default.html">acme-pr-reviewer</a><span class="tag">agent</span>')
    return must(s, "differs from the library in <em>content</em> and <em>lands at</em>", "<code>.claude/agents/acme-pr-reviewer.md</code> · promoted to My library just now")


def promote_steps(c, fail):
    steps = [
        ("project-configuring-default", "Configuring", "project-configuring-default.html", ("after", 'aria-label="The set"', '<a>pr-reviewer</a>'), None),
        ("project-detached-default", "Configuring, pr-reviewer open", "project-detached-default.html", ("a", '<a class="button">Promote to My library…</a>'), None),
        ("project-detached-promote", "Promote pr-reviewer — a new item, not a merge", "project-detached-default.html", ("a", '<a class="button button-primary">Promote</a>'), modal(PROMOTE_MODAL)),
    ]
    if fail:
        steps.append(("project-detached-error", "Promote didn't land", "project-detached-error.html", ("btn", '<button type="button" class="button-primary">Promote again'), None))
    steps.append(("project-configuring-default", "Configuring, the row links to acme-pr-reviewer", "project-configuring-default.html", None,
                  seq(promoted, subs([(ORIG_HEAD[0], "14 items · 3 auto-added")]))))
    return chain(c, steps)


@case("rj3-detached-promote")
def _():
    return promote_steps("rj3-detached-promote", False)


@case("rj3-promote-failed")
def _():
    return promote_steps("rj3-promote-failed", True)


# ── RJ-4 · move my work without my secrets ────────────────────────────────────

@case("rj4-add-item")
def _():
    return chain("rj4-add-item", [
        ("library-my-default", "My library", "library-my-default.html", ("a", f'{BTN_PRIMARY}{ICON}Add item</a>'), None),
        ("item-empty", "Add item — check that these files carry no keys", "item-empty.html", ("btn", '<button type="submit" class="button-primary">'), None),
        ("library-my-default", "My library, added", "library-my-default.html", None, None),
    ])


@case("rj4-import")
def _():
    return chain("rj4-import", [
        ("library-my-default", "My library", "library-my-default.html", ("a", '<a class="button">Import JSON</a>'), None),
        ("library-json-default", "Import — the keys warning before anything is accepted", "library-json-default.html", ("a", f'{BTN_PRIMARY}Import 47 items</a>'), None),
        ("library-json-loading", "Importing — if it stops, the library stays as it was", "library-json-loading.html", ("wait",), None),
        ("library-json-success", "47 items imported", "library-json-success.html", None, None),
    ])


@case("rj4-import-failed")
def _():
    return chain("rj4-import-failed", [
        ("library-json-default", "Import", "library-json-default.html", ("a", f'{BTN_PRIMARY}Import 47 items</a>'), None),
        ("library-json-loading", "Importing", "library-json-loading.html", ("wait",), None),
        ("library-json-error", "The import didn't finish — nothing was imported (Q27)", "library-json-error.html", ("a", f'{BTN_PRIMARY}Try the import again</a>'), None),
        ("library-json-loading", "Importing again", "library-json-loading.html", ("wait",), None),
        ("library-json-success", "47 items imported", "library-json-success.html", None, None),
    ])


SHARE_MODAL = '''
    <!-- The moment of sharing is a disclosure moment (§6): what becomes visible, in the present tense, before the link exists. -->
    <div class="scrim" aria-hidden="true"></div>
    <dialog class="modal" open aria-labelledby="modal-title">
      <div class="sheet-head">
        <h2 id="modal-title">Share acme-billing-api by link?</h2>
      </div>
      <p>Anyone with the link can open this project and see it as it is now — and every edit you make later.</p>
      <div>
        <p><strong>What becomes visible</strong></p>
        <ul class="plain-list">
          <li>The content of all 14 items — whatever is inside them goes with them</li>
          <li>3 env key names: <code>DATABASE_URL</code>, <code>GITHUB_TOKEN</code>, <code>SENTRY_AUTH_TOKEN</code> — names only, never values</li>
          <li>3 external repos, at their pinned refs</li>
          <li>When you last checked it</li>
        </ul>
      </div>
      <div class="callout callout-quiet">
        <span class="severity">Note</span>
        <span>We can’t tell what in these items is your client’s — a rule naming them, an API shape in an example. Look before you share.</span>
      </div>
      <div class="form-actions">
        <a class="button push">Cancel</a>
        <a class="button button-primary">Create link</a>
      </div>
    </dialog>
'''

REVOKE_MODAL = '''
    <!-- Revoking is honest about what it cannot do (§5): the address dies, what was taken stays taken. -->
    <div class="scrim" aria-hidden="true"></div>
    <dialog class="modal" open aria-labelledby="modal-title">
      <div class="sheet-head">
        <h2 id="modal-title">Stop sharing acme-billing-api?</h2>
      </div>
      <p>The link stops working at once.</p>
      <p>It can’t reach what was already taken: anyone who downloaded the archive or copied its items keeps them.</p>
      <div class="form-actions">
        <a class="button push">Cancel</a>
        <a class="button button-primary">Stop sharing</a>
      </div>
    </dialog>
'''


def shared(s):
    s = must(s, '<h1 id="page-title">acme-billing-api</h1>', '<h1 id="page-title">acme-billing-api<span class="tag">Shared</span></h1>')
    s = must(s, f"<span>{ORIG_HEAD[1]}</span></p>", f'<span>{ORIG_HEAD[1]}</span><span>Shared by link · anyone holding it sees it as it is now</span></p>')
    return must(s, '<a class="button" href="project-share.html">Share</a>', '<a class="button" href="project-revoke.html">Stop sharing</a>')


@case("rj4-share")
def _():
    return chain("rj4-share", [
        ("project-default", "Project", "project-default.html", ("a", '<a class="button">Share</a>'), None),
        ("project-share", "Share — what becomes visible, before the link exists", "project-default.html", ("a", '<a class="button button-primary">Create link</a>'), modal(SHARE_MODAL)),
        ("project-default", "Project, shared — every later edit is a publication", "project-default.html", None, shared),
    ])


@case("rj4-revoke")
def _():
    return chain("rj4-revoke", [
        ("project-default", "Project, shared", "project-default.html", ("a", '<a class="button">Stop sharing</a>'), shared),
        ("project-revoke", "Stop sharing — copies already taken stay taken", "project-default.html", ("a", '<a class="button button-primary">Stop sharing</a>'), seq(shared, modal(REVOKE_MODAL))),
        ("project-default", "Project, no longer shared", "project-default.html", None, None),
    ])


# ── The receiver ──────────────────────────────────────────────────────────────

@case("receiver-check-take")
def _():
    return chain("receiver-check-take", [
        ("shared-project-default", "Shared project — somebody sent a link", "shared-project-default.html", ("a", f'{BTN_PRIMARY}Check this set</a>'), None),
        ("run-shared-loading", "Run, checking somebody else's set", "run-shared-loading.html", ("wait",), None),
        ("run-shared-default", "Run, checked — what this machine still needs", "run-shared-default.html", ("a", f'{BTN_PRIMARY}Download the archive</a>'), None),
        ("run-shared-success", "Run, archive in hand", "run-shared-success.html", None, None),
    ])


@case("receiver-check-failed")
def _():
    return chain("receiver-check-failed", [
        ("shared-project-default", "Shared project", "shared-project-default.html", ("a", f'{BTN_PRIMARY}Check this set</a>'), None),
        ("run-shared-loading", "Run, checking", "run-shared-loading.html", ("wait",), None),
        ("run-shared-error", "Run, the check didn't finish — and it says whose failure it is", "run-shared-error.html", ("a", f'{BTN_PRIMARY}Check again</a>'), None),
        ("run-shared-loading", "Run, checking again", "run-shared-loading.html", ("wait",), None),
        ("run-shared-default", "Run, checked", "run-shared-default.html", ("a", f'{BTN_PRIMARY}Download the archive</a>'), None),
        ("run-shared-success", "Run, archive in hand", "run-shared-success.html", None, None),
    ])


@case("receiver-copy")
def _():
    return chain("receiver-copy", [
        ("shared-project-default", "Shared project", "shared-project-default.html", ("a", '<a class="button">Copy into my library</a>'), None),
        ("sign-in-default", "Sign in — the only door, and chosen", "sign-in-default.html", ("btn", '<button type="submit" class="button-primary">'), None),
        ("library-my-default", "My library — it is mine now", "library-my-default.html", None, None),
    ])


@case("receiver-item")
def _():
    return chain("receiver-item", [
        ("shared-item-default", "Shared item — one block, and whose it is", "shared-item-default.html", ("a", f'{BTN_PRIMARY}Take as an archive</a>'), None),
        ("run-shared-item-loading", "Run, checking one block", "run-shared-item-loading.html", ("wait",), None),
        ("run-shared-item-default", "Run, checked", "run-shared-item-default.html", ("a", f'{BTN_PRIMARY}Download the archive</a>'), None),
        ("run-shared-item-success", "Run, archive in hand", "run-shared-item-success.html", None, None),
    ])


@case("receiver-dead-link")
def _():
    return chain("receiver-dead-link", [
        ("shared-project-error", "The link no longer opens — stuck", "shared-project-error.html", None, None),
    ])


# ── write, walk, and the viewer's tree ────────────────────────────────────────

FLOWS = [
    ("main", "Main job", "P1 the keeper — primary", "MAIN keep it working somewhere else"),
    ("item", "Single-item export", "P1 the keeper — primary", "MAIN, at its smallest scale (Q15)"),
    ("rj1", "RJ-1 · The handover", "P1 sending · P2 receiving", "RJ-1 know what the other side will still need, before I send it"),
    ("rj2", "RJ-2 · Drags in, fights", "P1 the keeper — primary", "RJ-2 find out what my pieces drag in, and where two will fight"),
    ("rj3", "RJ-3 · Fix once", "P1 the keeper — primary", "RJ-3 fix something once and have the fix reach every copy"),
    ("rj4", "RJ-4 · No secrets", "P1 the keeper · P2", "RJ-4 move my work without moving my secrets or my client’s business"),
    ("receiver", "The receiver", "P2 the receiver — never heard in the first person (Q20)", "MAIN · RJ-1 · RJ-2 · SJ-1, performed by somebody who owns nothing"),
]
MAIN_META = json.loads((HERE / "main_meta.json").read_text(encoding="utf-8"))


def flow_line(cid, files, pages_dir):
    titles = []
    for f in files:
        t = (pages_dir / f).read_text(encoding="utf-8")
        titles.append(html.unescape(re.search(r"<title>\d\d · (.*?) — prototype", t).group(1)))
    return " → ".join(titles)


built = {}
for cid, fn in CASES.items():
    out = PROTO / cid
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    pages = fn()
    for name, h in pages.items():
        (out / name).write_text(h, encoding="utf-8")
    names = sorted(pages)
    for i, name in enumerate(names):
        t = (out / name).read_text(encoding="utf-8")
        nxt = re.findall(r'href="(\d\d-[a-z-]+\.html)"', t) + re.findall(r'url=(\d\d-[a-z-]+\.html)', t)
        stray = re.findall(r'<a\b[^>]*href="(?!\d\d-|https?:|\.\./)[^"]*"', t)
        want = names[i + 1] if i + 1 < len(names) else None
        assert not stray, f"{cid}/{name}: stray live links {stray}"
        assert (nxt == [want]) if want else (nxt == []), f"{cid}/{name}: leads to {nxt}, want {want}"
    built[cid] = names
    print(f"{cid}: {len(names)} steps ok")

PLAY = '<svg class="wf-ico" aria-hidden="true"><use href="#i-play"/></svg>'
CHEV = '<svg class="wf-ico" aria-hidden="true"><use href="#i-chev"/></svg>'
FOLDER = '<svg class="wf-ico" aria-hidden="true"><use href="#i-folder"/></svg>'
sections = []
for prefix, title, persona, job in FLOWS:
    rows = []
    for cid, files in built.items():
        if cid.split("-")[0] != prefix:
            continue
        steps = []
        for f in files:
            t = (PROTO / cid / f).read_text(encoding="utf-8")
            steps.append(f"{f[:-5]}:" + html.escape(html.unescape(re.search(r"<title>(.*?) — prototype", t).group(1)), quote=True))
        meta = MAIN_META.get(cid)
        p, j, fl = meta if meta else (persona, job, flow_line(cid, files, PROTO / cid))
        p, j, fl = (html.escape(x, quote=True) for x in (p, j, fl))
        rows.append(f'                <li class="wf-case" data-case="{cid}" data-persona="{p}" data-job="{j}" data-flow="{fl}" data-steps="{"|".join(steps)}"><a href="#flow/{cid}">{PLAY}<span class="wf-name">{cid}</span></a></li>')
    sections.append(f'''            <li class="wf-section">
              <details>
                <summary>{CHEV}{FOLDER}<span class="wf-name">{title}</span></summary>
                <ul>
{chr(10).join(rows)}
                </ul>
              </details>
            </li>''')
v = ROOT / "pages" / "wireframes.html"
s = v.read_text(encoding="utf-8")
s, n = re.subn(r'(<span class="wf-name">Flows</span></summary>\n          <ul class="wf-group-list">\n).*?(\n          </ul>\n        </details>\n      </li>\n    </ul>\n  </nav>)',
               lambda m: m.group(1) + "\n".join(sections) + m.group(2), s, count=1, flags=re.S)
assert n == 1, "flows group not found"
v.write_text(s, encoding="utf-8")
print(len(built), "cases,", sum(len(x) for x in built.values()), "pages")
