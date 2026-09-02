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

**Research is done and signed off. The design system is next and has not started.** No
code, no design system, no mockups yet.

Roadmap: ~~research~~ → **design system** → mockups → static frontend → logic.

The library is not empty on first run: a curated, read-only **public library** ships with
the app beside your own, along with one example project that deliberately contains a real
problem to find.

Planned stack: Next.js + React + TypeScript, client-side only, IndexedDB for storage,
JSZip for the archive. Custom design system, no UI kits.

## Files

- `CLAUDE.md` — full working context: data model, product logic, scope boundaries,
  conventions. The source of truth. Start here.
- `research.md` — the consolidated read of the research phase in five sections:
  competitors, flows, benchmark, patterns, conclusions. Every fact links to its source
  or capture, and what was never established says so. A digest, not a spec.
- `research/` — the closed research phase, one folder per stage. `research/FINAL.md` is
  the closing document: what it produced, what it decided, and why.
