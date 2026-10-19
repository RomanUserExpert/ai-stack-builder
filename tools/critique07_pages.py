"""Phase 07, step 6: the critique's fixes that belong to the wireframe pages — structure and copy.

The critique (07-ui-assembly/ui/critique.md) found defects whose fix is the page's structure or its words, not the
kit's look. They are applied here, on 04-wireframes/pages, because a mockup takes its structure and text from its
wireframe; the mockups and prototypes are then rebuilt from them. The copy changes are recorded in
05-tone-of-voice/microcopy.md, *Phase 07 — the critique* (§14: copy changes in one place).

Every edit is (pages, was, now, n, critique row, why): `was` must occur exactly n times across those pages, or
nothing is written — the discipline of tools/rewrite_copy.py.

    python tools/critique07_pages.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "04-wireframes" / "pages"
ALL = sorted(p.stem for p in PAGES.glob("*.html") if p.stem != "wireframes")
PROJECTS = ["projects-default", "projects-delete", "projects-filters"]
SUCCESS = ["run-success", "run-item-success", "run-shared-success", "run-shared-item-success"]

COPY = [
    (["run-error-setup"],
     "the agent will get two rules that disagree about imports.</p>\n        <div class=\"export-actions\">",
     "the agent will get two rules that disagree about imports.</p>\n"
     "        <p><strong><code>SETUP.md</code> isn’t written.</strong> An archive exported now goes without it, and the agent that opens it has no setup to read.</p>\n"
     "        <div class=\"export-actions\">", 1,
     "#1", "Q28: a disclosure that could not be produced says so — before the step, not after"),
    (PROJECTS,
     "every edit is visible to them</dd>\n              </dl>\n              <div class=\"row-actions\">\n                <button type=\"button\">Duplicate</button>\n                <button type=\"button\">Share…</button>",
     "every edit is visible to them</dd>\n              </dl>\n              <div class=\"row-actions\">\n                <button type=\"button\">Duplicate</button>\n                <button type=\"button\">Stop sharing…</button>", 3,
     "#17", "Q37: a shared project reads as shared — its Share… reads Stop sharing…"),
    (["project-configuring-error-server"],
     "<span>13 items · 3 auto-added · 1 detached</span><span>Checked 2 days ago · for Claude Code · 1 problem · 2 notes · 1 skipped</span>",
     "<span>13 items in your changes · not saved</span><span>The saved project: 14 items · checked 2 days ago · for Claude Code · 1 problem · 2 notes · 1 skipped</span>", 1,
     "#16", "Q26: never a verdict beside a set it does not describe — the draft and the saved project are named apart"),
    (SUCCESS[:1] + SUCCESS[1:2] + SUCCESS[3:], "KB · saved to Downloads.", "KB.", 3,
     "#35", "Principle 1: say what was examined — we cannot know where the browser put the file"),
    (ALL, "differs from the original in <em>content</em> and <em>lands at</em>",
     "differs from the original in <em>Content</em> and <em>Lands at</em>", 12,
     "#49", "The fields named as their labels read them, so a name reads as a name mid-sentence"),
    (ALL, "Search Public library — filesystem, playwright, anthropics\"", "Search Public library — filesystem, playwright\"", 5,
     "#51", "Placeholder: fits the field (it was clipped)"),
    (["project-configuring-empty"], ">Open Public library</a>", ">Show Public library</a>", 1,
     "#52", "It switches the panel's scope; *Open* read as leaving the draft"),
]

MARKUP = [
    (ALL, "<span class=\"tag\">Shared</span>", "<span class=\"tag tag-state\">Shared</span>", 14,
     "#18", "Shared is a state, drawn as the states are (Auto-added, Detached), never as a kind"),
    (ALL, "<span class=\"tag\">Example</span>", "<span class=\"tag tag-state\">Example</span>", 3, "#18", "a state, not a kind"),
    (ALL, "<span class=\"tag\">Configuring</span>", "<span class=\"tag tag-state\">Configuring</span>", 13, "#18", "a mode, not a kind"),
    (ALL, "glyph-waiting\" aria-hidden=\"true\"></span>Stopped", "glyph-stopped\" aria-hidden=\"true\"></span>Stopped", 2,
     "#22", "a stage that broke is not a stage that waits — its own glyph"),
    (["sign-in-loading", "sign-up-loading"], "class=\"button-primary\"><span class=\"glyph glyph-running\"",
     "class=\"button-primary\" aria-disabled=\"true\" aria-busy=\"true\"><span class=\"glyph glyph-running\"", 2,
     "#12", "busy: it cannot be sent twice, and says it is working"),
    (["project-empty", "project-configuring-empty"],
     "<button type=\"button\" disabled title=\"Add an item first\">",
     "<button type=\"button\" aria-disabled=\"true\" aria-describedby=\"export-why\" title=\"Add an item first\">", 2,
     "#13", "Q16: the inert control teaches — it takes focus and its reason is read out"),
    (["project-empty", "project-configuring-empty"],
     "<p>Add items from the left. Anything they require is auto-added. Export opens once this project has an item.</p>",
     "<p id=\"export-why\">Add items from the left. Anything they require is auto-added. Export opens once this project has an item.</p>", 2,
     "#13", "the reason the inert Export points at"),
    (["project-configuring-public"],
     "<button type=\"button\" disabled title=\"Add an item first\">",
     "<button type=\"button\" aria-disabled=\"true\" title=\"Add an item first\">", 1, "#13", "focusable, as on the empty project"),
    (["project-configuring-loading-add"],
     "<button type=\"button\" disabled title=\"Add an item first\"><span class=\"icon\" aria-hidden=\"true\"></span>Export</button>",
     "<a class=\"button\" href=\"run-loading.html\"><span class=\"icon\" aria-hidden=\"true\"></span>Export</a>", 1,
     "#20", "Q16: the project has an item, so Export is no longer the inert exception"),
    (["project-configuring-loading-add"],
     "<p class=\"facts meta\"><span>Adding — finding what it requires</span></p>",
     "<p class=\"facts meta\" role=\"status\"><span class=\"glyph glyph-running\" aria-hidden=\"true\"></span><span>Adding — finding what it requires</span></p>", 1,
     "#20", "a pending round trip is busy, and says so to a screen reader"),
    (["run-loading"], "<a class=\"button\" href=\"run-remove.html\">Remove eslint-autofix…</a>",
     "<a class=\"button\" aria-disabled=\"true\" title=\"The check is still running\">Remove eslint-autofix…</a>", 1,
     "#32", "no remove while the check that would re-run is still running"),
    (SUCCESS, "class=\"button button-primary\" href=\"", "class=\"button\" href=\"", 4,
     "#34", "the primary is not spent on a way out the Run bar already gives"),
    (["project-loading"],
     "          <div class=\"head-actions\">\n            <a class=\"button\" href=\"project-configuring-default.html\">Configure</a>\n            <button type=\"button\">Share…</button>\n            <button type=\"button\">Duplicate</button>\n            <a class=\"button button-primary\" href=\"run-loading.html\"><span class=\"icon\" aria-hidden=\"true\"></span>Export</a>\n          </div>",
     "          <div class=\"head-actions\">\n            <!-- Loading: nothing here can act yet, and Share… or Stop sharing… is not known — so nothing is shown,\n                 as on project-configuring-loading (§9: an action that cannot act is not shown). Phase 07, critique #19. -->\n          </div>", 1,
     "#19", "§9 — and the sibling configuring-loading already does this"),
]


def auto_added_refuse(text):
    """#2 — a panel row auto-added (*Required by …*) cannot be unchecked: §8's only refusal, shown, not just stated."""
    return re.sub(r'(<p class="state-line">Required by .*?</p>\s*</div>\s*<label class="check")([^>]*)><input type="checkbox" checked>',
                  r'\1\2 title="Auto-added — remove what requires it"><input type="checkbox" checked disabled>', text, flags=re.S)


def public_origin(texts):
    """#21 — a public item in the panel shows its origin (§5): the facts line the Public library already carries."""
    src = (PAGES / "library-public-default.html").read_text(encoding="utf-8")
    facts = {}
    for m in re.finditer(r'<h2>([^<]+)<span class="tag">.*?(<p class="facts meta">.*?</p>)', src, re.S):
        facts.setdefault(m.group(1), m.group(2))
    t = texts["project-configuring-public"]
    def add(m):
        f = facts.get(m.group(2))
        return m.group(0) if not f or "facts meta" in m.group(0) else m.group(0) + "\n                " + f
    t2 = re.sub(r'(<h3><a href="[^"]*">([^<]+)</a><span class="tag">[^<]+</span></h3>\s*<p class="state-line">[^<]*</p>)', add, t)
    return t2, t2.count("facts meta") - t.count("facts meta")


def main():
    texts = {p: (PAGES / f"{p}.html").read_text(encoding="utf-8") for p in ALL}
    for pages, was, now, n, row, why in COPY + MARKUP:
        found = sum(texts[p].count(was) for p in pages)
        if found != n:
            sys.exit(f"{row}: expected {n}, found {found}: {was[:70]}")
        for p in pages:
            texts[p] = texts[p].replace(was, now)
    refused = 0
    for p in ALL:
        new = auto_added_refuse(texts[p])
        refused += new.count("checked disabled>") - texts[p].count("checked disabled>")
        texts[p] = new
    texts["project-configuring-public"], origins = public_origin(texts)
    changed = 0
    for p, t in texts.items():
        f = PAGES / f"{p}.html"
        if f.read_text(encoding="utf-8") != t:
            f.write_text(t, encoding="utf-8")
            changed += 1
    print(f"critique07: {len(COPY)} copy edits, {len(MARKUP)} markup edits, {refused} auto-added rows refuse, "
          f"{origins} public rows show their origin — {changed} pages written")


Q41 = ["project-configuring-default", "project-configuring-error-filtered", "project-configuring-item", "project-default",
       "project-detached-default", "project-detached-error", "project-detached-loading", "project-detached-promote",
       "project-item", "project-revoke", "project-share"]


def q41():
    """Q41, answered by the owner 2026-10-19 (*на обеих*): both items of a declared conflict read as state 4 — the
    `Conflict` tag on code-style too. The Problem itself still annotates the row that declares it (§8)."""
    edits = [(Q41, '>code-style</a><span class="tag">skill</span></h3>',
              '>code-style</a><span class="tag">skill</span><span class="tag tag-state">Conflict</span></h3>', 11),
             (["project-configuring-item"], 'id="drawer-title">code-style <span class="tag">skill</span>',
              'id="drawer-title">code-style <span class="tag">skill</span><span class="tag tag-state">Conflict</span>', 1)]
    texts = {}
    for pages, was, now, n in edits:
        for pg in pages:
            texts.setdefault(pg, (PAGES / f"{pg}.html").read_text(encoding="utf-8"))
        found = sum(texts[pg].count(was) for pg in pages)
        if found != n:
            sys.exit(f"Q41: expected {n}, found {found}: {was}")
        for pg in pages:
            texts[pg] = texts[pg].replace(was, now)
    for pg, t in texts.items():
        (PAGES / f"{pg}.html").write_text(t, encoding="utf-8")
    print(f"critique07: Q41 — Conflict on both rows, {len(texts)} pages")


def origin_only():
    texts = {"project-configuring-public": (PAGES / "project-configuring-public.html").read_text(encoding="utf-8")}
    t, n = public_origin(texts)
    (PAGES / "project-configuring-public.html").write_text(t, encoding="utf-8")
    print(f"critique07: {n} public rows show their origin")


if __name__ == "__main__":
    origin_only() if "--origin" in sys.argv else q41() if "--q41" in sys.argv else main()
