# AI Stack Builder

A workspace for your AI building blocks — skills, agents, system prompts, MCP servers,
scripts and mini-apps. Keep them in one library, assemble them into projects, export a
project as an archive that is ready to run.

**The point isn't storage — it's assembly with validation.** Git already stores files.
Nothing tells you that a skill needs a particular MCP server, that two items write to the
same config file, or that an env key is missing. You find that out at runtime. This does
the check before you export.

## Concepts

- **Item** — one reusable block: `skill`, `agent`, `prompt`, `mcp`, `script` or `app`.
- **Project** — a named set of items that exports as an archive.
- **Library** — everything you own, across all projects.

Items live in the library once. A project links to them, so editing an item updates every
project that uses it — unless you detach it and tune it locally for that project alone.

## What export produces

A zip, assembled rather than dumped: inline items placed at their target paths, external
repos written up as setup instructions, all MCP servers merged into one config, and every
missing env variable collected into `.env.example`. You pick the agent target first —
Claude Code, Cursor, Codex or Universal — and the paths and naming adapt.

The `SETUP.md` inside is written **for the agent that opens the project**, not for you to
read. It states what each item in the set requires — its dependencies, servers, env keys
and repos at their pinned versions — so the agent can set the project up on init.

## Who it's for

Design engineers and AI engineers who use AI daily and have accumulated more material
than they can keep straight. Desktop-first, dark theme.

## Status

**Research is done; the design work has not started.** Stages 1–5 were signed off on
2026-09-02, and stages 6 and 7 — personas and jobs to be done — on 2026-09-09. Those two ship
marked *provisional*: the five practitioner conversations that would lift the label cannot be
run. No code, no information architecture, no design system, no mockups yet.

Roadmap — the twelve lessons of the course this work is homework for. *Corrected 2026-09-15;
this line used to read `research → design system → mockups → frontend → logic`, which put the
design system second when it is ninth.*

~~01 research and benchmark~~ → ~~02 personas and JTBD~~ → **03 information architecture** →
04 prototyping → 05 tone of voice → 06 concept → 07 UI assembly → 08 design tokens →
09 design system → 10 responsive → 11 animation → 12 handoff. Product logic — state,
storage, validation, export — comes after all twelve.

The library is not empty on first run: a curated, read-only **public library** ships with
the app beside your own, along with one example project that deliberately contains a real
problem to find.

Planned stack: Next.js + React + TypeScript, client-side only, IndexedDB for storage,
JSZip for the archive. Custom design system, no UI kits.

## Files

- `CLAUDE.md` — full working context: data model, product logic, scope boundaries,
  conventions. The source of truth. Start here.
- `research/` — the research phase, one folder per stage. Stages 1–5 are closed; stages 6
  and 7 were added on 2026-09-06 and are *provisional*.
  - `research/research.md` — the consolidated read, in five sections: competitors,
    flows, benchmark, patterns, conclusions. Every fact links to its source or capture,
    and what was never established says so. A digest, not a spec.
  - `research/research.html` — the same research as one self-contained page, with 34
    captures embedded. Opens from disk, sends as a single file. Generated — see `tools/`.
  - `research/FINAL.md` — the closing document: what the phase produced, what it
    decided, and why. **Start here for the research** — it is the entry point the whole
    folder instructs.
  - `research/research-plan.md` — the spine, ending in the register: every open question
    with an ID, what would answer it, and what it blocks. The only list of open questions.
  - `research/6-personas/personas.md` and `research/7-jobs-to-be-done/jtbd.md` — three
    personas with one primary, and one main job with four related, three emotional and two
    social, each against a matrix of personas. Both *provisional*.
  - `research/6-personas/personas.html` — the same two documents as one generated page.
  - `research/personas-and-jobs-critique.md` — the audit of those two: 238 claims
    classified, 27 found invented, applied in full.
- `tools/` — the generators for both pages, and how to rebuild them.
