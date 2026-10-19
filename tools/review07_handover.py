"""Phase 07, review G34-4/5 (owner: «да», 2026-10-19): the handover previews on the Runs that had none.

The project's Run shows what the archive contains (stage 08) and the SETUP.md the agent will read (stage 09). The
single-item Run, the shared project's Run and the shared item's Run had those stages with nothing inside, so the
handover §6 and Q28 put *before* Export could not be read. This writes them — derived, line by line, from the fields
the items already carry on their pages (requires, needsEnv, defersTo, repo @ ref, where each lands for Claude Code);
nothing is invented beyond that, and the form is run-default's.

    python tools/review07_handover.py

Each block goes into the stage's empty <details>; the run stops if a stage already has a body or is missing.
Copy: 05-tone-of-voice/microcopy.md, *Phase 07 — the review*, as generated rows.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "04-wireframes" / "pages"

SETUP_ITEM = """# Setup — migration-reviewer (Claude Code)

Read this first and perform each step.

## postgres-mcp
- External. Clone modelcontextprotocol/servers-archived at 9be4674.
- Needs DATABASE_URL. Ask the person for it; do not invent one.
- Required by migration-reviewer.

## db-migrate
- Lands at scripts/db-migrate.sh, with 2 files beside it.
- Needs DATABASE_URL.
- Requires seed-data. Required by migration-reviewer.

## seed-data
- Lands at scripts/seed-data.sh. Required by db-migrate.

## migration-reviewer
- Lands at .claude/agents/migration-reviewer.md."""

TREE_SHARED = """agent-dotfiles/
├── CLAUDE.md                       commit-conventions, shell-safety
├── SETUP.md
├── .env.example                    GITHUB_TOKEN
├── .mcp.json                       github-mcp, filesystem, memory
├── .claude/skills/code-style/SKILL.md
├── .claude/skills/session-notes/SKILL.md + 1 file
├── .claude/agents/pr-reviewer.md
└── scripts/  dotfiles-sync.sh + 4 files"""

SETUP_SHARED = """# Setup — agent-dotfiles (Claude Code)

Read this first and perform each step.

## github-mcp
- External. Clone github/github-mcp-server at v0.9.0.
- Needs GITHUB_TOKEN. Ask the person for it; do not invent one.
- Required by pr-reviewer.

## filesystem
- External. Clone modelcontextprotocol/servers at 2025.9.25.

## memory
- External. Same clone as filesystem.
- Required by session-notes.

## code-style
- Defers to the client’s ESLint config. Where they disagree, the ESLint config wins.
…"""

SETUP_SHARED_ITEM = """# Setup — code-style (Claude Code)

Read this first and perform each step.

## code-style
- Lands at .claude/skills/code-style/SKILL.md.
- Defers to the client’s ESLint config. Where they disagree, the ESLint config wins.
- Requires nothing. Needs no env keys."""

FILL = [
    (["run-item-default", "run-item-success"], "09", SETUP_ITEM),
    (["run-shared-default", "run-shared-success"], "08", TREE_SHARED),
    (["run-shared-default", "run-shared-success"], "09", SETUP_SHARED),
    (["run-shared-item-default", "run-shared-item-success"], "09", SETUP_SHARED_ITEM),
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    texts = {}
    for pages, n, block in FILL:
        for p in pages:
            t = texts.setdefault(p, (PAGES / f"{p}.html").read_text(encoding="utf-8"))
            m = re.search(rf'(<details>\s*<summary><span class="n">{n}</span>.*?</summary>)(\s*</details>)', t, re.S)
            if not m:
                sys.exit(f"{p}: stage {n} is missing or already has a body")
            body = f'\n              <div class="stage-body">\n                <pre class="file">{esc(block)}</pre>\n              </div>'
            texts[p] = t[:m.end(1)] + body + t[m.start(2):]
    for p, t in texts.items():
        (PAGES / f"{p}.html").write_text(t, encoding="utf-8")
    print(f"handover: {len(FILL)} blocks on {len(texts)} pages")


if __name__ == "__main__":
    main()
