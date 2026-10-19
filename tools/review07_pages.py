"""Phase 07, step 8: the review's fixes that belong to the wireframe pages — structure and copy.

The review of all 80 dressed pages and 239 flow steps (07-ui-assembly/ui/review.md) found defects whose fix is
a page's structure or words. They are applied here, on 04-wireframes/pages; mockups and prototypes are rebuilt
from them. Copy changes are recorded in 05-tone-of-voice/microcopy.md, *Phase 07 — the review*.

Every edit is (pages, was, now, n, review row, why); `was` must occur exactly n times, or nothing is written.

    python tools/review07_pages.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "04-wireframes" / "pages"
RUN_ERR = ["run-item-error", "run-shared-error", "run-shared-item-error"]
ITEM = ["item-default", "item-delete", "item-empty", "item-error"]

EDITS = [
    (RUN_ERR, 'glyph-problem" aria-hidden="true"></span>Stopped', 'glyph-stopped" aria-hidden="true"></span>Stopped', 3,
     "G34-1", "our server breaking mid-stage is not a Problem — the stopped glyph, as on run-error-check"),
    (RUN_ERR, "<h1>The check didn’t finish</h1>", "<h1 role=\"alert\">The check didn’t finish</h1>", 3,
     "G34-3", "the failure summary is announced and drawn as on run-error-check"),
    (["run-shared-item-error"],
     "            <details>\n              <summary><span class=\"n\">04</span><span class=\"name\">Target pat",
     "            <details open>\n              <summary><span class=\"n\">04</span><span class=\"name\">Target pat", 1,
     "G34-2", "the failed stage is open, so its explanation and its way on are on the screen"),
    (["sign-up-error"], 'autocomplete="email" placeholder="maya@chen.dev">',
     'autocomplete="email" value="maya@chen.dev" placeholder="maya@chen.dev">', 1,
     "G01-14", "an error keeps what the person typed, as Sign in does"),
    (["sign-up-loading"], 'autocomplete="current-password" value="••••••••••">', 'autocomplete="new-password" value="••••••••••" readonly>', 1,
     "G01-14, G01-16", "a new account's password is new-password; fields are read-only while the request runs"),
    (["sign-up-loading", "sign-in-loading"], 'autocomplete="email" value="maya@chen.dev" placeholder="maya@chen.dev">',
     'autocomplete="email" value="maya@chen.dev" placeholder="maya@chen.dev" readonly>', 2,
     "G01-16", "what was sent cannot change while it is being sent"),
    (["sign-in-loading"], 'autocomplete="current-password" value="••••••••••">', 'autocomplete="current-password" value="••••••••••" readonly>', 1,
     "G01-16", "as above"),
    (ITEM, 'placeholder="Items this one requires — postgres-mcp"', 'placeholder="postgres-mcp, seed-data"', 4,
     "G01-13", "copy: the label already says Requires; the placeholder is an example that fits"),
    (ITEM, 'placeholder="Items that clash with this one in a project — eslint-autofix"', 'placeholder="eslint-autofix"', 4,
     "G01-13", "copy: the label already says Conflicts with"),
]


def main():
    names = sorted({p for pages, *_ in EDITS for p in pages})
    texts = {p: (PAGES / f"{p}.html").read_text(encoding="utf-8") for p in names}
    for pages, was, now, n, row, why in EDITS:
        found = sum(texts[p].count(was) for p in pages)
        if found != n:
            sys.exit(f"{row}: expected {n}, found {found}: {was[:70]}")
        for p in pages:
            texts[p] = texts[p].replace(was, now)
    for p, t in texts.items():
        (PAGES / f"{p}.html").write_text(t, encoding="utf-8")
    print(f"review07: {len(EDITS)} edits over {len(texts)} pages")


if __name__ == "__main__":
    main()
