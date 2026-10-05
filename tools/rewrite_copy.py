"""Rewrite product copy on wireframe pages by voice.md — text only, markup untouched.

Lesson 05, steps 5–6. Each entry is (pages, was, now, n): `was` is matched exactly as it stands in
the HTML (so it may carry the tags around the text, to pin it to one place), and must occur exactly
`n` times across the listed pages, or nothing is written. Run from the repo root:

    python tools/rewrite_copy.py run        # the sample screen (step 5)

The was/now pairs are the source for the *Was / Now* columns of 05-tone-of-voice/microcopy.md.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "04-wireframes" / "pages"

PROJECT = ["project-default", "project-empty", "project-item", "project-loading", "project-revoke",
           "project-share", "project-configuring-default", "project-configuring-empty",
           "project-configuring-error-filtered", "project-configuring-error-server", "project-configuring-item",
           "project-configuring-loading-add", "project-configuring-public", "project-detached-default",
           "project-detached-error", "project-detached-loading", "project-detached-promote"]
RUN = ["run-default", "run-error-check", "run-error-export", "run-error-setup", "run-loading",
       "run-loading-export", "run-remove", "run-success"]

# (pages, was, now, expected occurrences across those pages, why — the voice.md entry)
SETS = {
    "run": [
        (RUN, '<span class="name">Resolve the set</span>', '<span class="name">Requirements</span>', 8,
         "Dictionary: project, not set (D6)"),
        (RUN, "You chose 11. The walk along <code>requires</code> added 3:",
         "You added 11. 3 more were auto-added because another item <code>requires</code> them:", 8,
         "Dictionary: auto-added; *walk* never on a screen (D7)"),
        (RUN, '<span class="name">Deference</span>', '<span class="name">Defers to</span>', 8,
         "Jargon: *deference* as a noun never on a screen"),
        (RUN, '>Remove eslint-autofix</a>', '>Remove eslint-autofix…</a>', 8,
         "Typography: `…` on a button that opens a confirmation (D20)"),
        (RUN, "<strong>1 problem is still in the set.</strong>", "<strong>1 problem is still in this project.</strong>", 3,
         "Dictionary: project, not set (D6)"),
        (RUN, '>Fix it in the project first</a>', '>Configure acme-billing-api</a>', 3,
         "Button: verb + object, the result visible — it opens the configuring mode"),
        (RUN, "<p>The server stopped answering at stage 4 of 10. Nothing in the project changed; its last check still reads 2 days ago.</p>",
         "<p>Our server stopped answering at stage 4 of 10. Nothing in the project changed, and its last check still reads 2 days ago.</p>", 1,
         "Dictionary: our failure (D9)"),
        (RUN, "Didn’t complete", "Stopped — our server didn’t answer", 1,
         "Dictionary: a stage that started and did not finish (D23)"),
        (RUN, "<p>The server stopped at 12 of 18 files. Nothing was downloaded. The check above still stands — nothing in the set changed.</p>",
         "<p>Our server stopped at 12 of 18 files. Nothing was downloaded. The check above still stands — nothing in the project changed.</p>", 1,
         "Dictionary: our failure (D9); project, not set (D6)"),
        (RUN, '<p class="meta">503 · 14:07</p>', '<p class="meta">503 · Service unavailable · 14:07</p>', 1,
         "Dictionary: one form for the error code (D10)"),
        (RUN, "Build the archive again</a>", "Export again</a>", 1,
         "Dictionary: Export; retry names the verb (D4, D12)"),
        (RUN, "Couldn’t be written", "Stopped — our server didn’t answer", 1,
         "Dictionary: a stage that started and did not finish (D23)"),
        (RUN, "<span><code>SETUP.md</code> couldn’t be produced — the server stopped while writing it. What you would read here is missing because something broke on our side, not because there is nothing to say (Q28). <span class=\"meta\">503 · 14:06</span>",
         "<span><code>SETUP.md</code> wasn’t written — our server stopped while writing it. What you would read here is missing because our server failed, not because there is nothing to say. <span class=\"meta\">503 · Service unavailable · 14:06</span>", 1,
         "Forbidden: internal ids (L1); our failure (D9); the error code (D10)"),
        (RUN, ">Write it again</a>", ">Write SETUP.md again</a>", 1,
         "Dictionary: retry names the verb and its object (D12)"),
        (RUN, "<strong>Building the archive — 18 files for Claude Code</strong>", "<strong>Exporting — 18 files for Claude Code</strong>", 1,
         "Dictionary: Export (D4); Loading: say what is loading"),
        (RUN, "</span>Checking…</span>", "</span>Checking</span>", 1,
         "Typography: `…` only on a button that opens a confirmation (D20); the glyph shows it is running"),
        (RUN, '<p class="meta">After the handover stages.</p>', '<p class="meta">Opens after the handover stages.</p>', 1,
         "Loading: the waiting stage says what will happen, not only where"),
        (RUN, '<a class="button button-primary" href="run-loading.html">Remove</a>',
         '<a class="button button-primary" href="run-loading.html">Remove from project</a>', 1,
         "Dangerous action: the confirm button repeats the verb of the act (D22)"),
        (RUN, "Archive built — acme-billing-api-claude-code.zip", "Exported — acme-billing-api-claude-code.zip", 1,
         "Dictionary: it is built — *Exported* (D4)"),
        (RUN, "Checked just now with 1 problem, 2 notes and 1 skipped.", "Checked just now · 1 problem · 2 notes · 1 skipped.", 1,
         "Dictionary: the verdict, one form (D19)"),
        (RUN, '<button type="button">Share the project</button>', '<button type="button">Share…</button>', 1,
         "Dictionary: Share… opens the disclosure (D21, D20)"),
    ],
    # Q36 (owner, 2026-10-05): the Project screen's main control reads Export. It opens the same mode,
    # whose title follows it; the check inside is a sub-process. `…` because the archive is not made
    # until the mode's last stage — more is shown before the irreversible step (D20).
    "q36": [
        (PROJECT, '<span class="icon" aria-hidden="true"></span>Check</a>',
         '<span class="icon" aria-hidden="true"></span>Export…</a>', 13,
         "Q36: the main control reads Export; `…` — the archive comes at the mode's last stage (D20)"),
        (PROJECT, '<span class="icon" aria-hidden="true"></span>Check</button>',
         '<span class="icon" aria-hidden="true"></span>Export…</button>', 4,
         "Q36, the empty project's inert control (Q16)"),
        (RUN, '<span class="title">Check</span>', '<span class="title">Export</span>', 8,
         "Q36: the mode is titled by what it ends in; the check is its sub-process"),
    ],
}


def apply(name):
    edits = SETS[name]
    texts = {}
    for pages, was, now, n, _ in edits:
        for p in pages:
            texts.setdefault(p, (PAGES / f"{p}.html").read_text(encoding="utf-8"))
    for pages, was, now, n, why in edits:
        found = sum(texts[p].count(was) for p in pages)
        if found != n:
            sys.exit(f"expected {n}, found {found}: {was[:80]}")
        for p in pages:
            texts[p] = texts[p].replace(was, now)
    for p, t in texts.items():
        (PAGES / f"{p}.html").write_text(t, encoding="utf-8")
    print(f"{name}: {len(edits)} edits over {len(texts)} pages")


if __name__ == "__main__":
    apply(sys.argv[1])
