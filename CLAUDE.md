# CLAUDE.md — AI Stack Builder

Working context for Claude Code on this project. Read this before doing anything.
All documentation, code, comments and UI copy in this repo are written in **English**.

---

## 1. Current phase — read this first

**Phase: Research. Nothing else has started.**

There is no application code, no design system, no mockups. Do not create any.

The agreed order of work:

1. **Research** ← we are here
2. Design system (tokens, typography, color, components)
3. Mockups / screen design (static, no logic)
4. Static frontend implementation (markup only, no business logic)
5. Logic (state, storage, validation, export)

Do not skip ahead. If a request seems to jump to a later stage, confirm before acting.
Product logic described in this file is **specification, not a build order** — it is
written down so design decisions are made with the real mechanics in view.

---

## 2. What the product is

A workspace where an AI practitioner keeps their own AI building blocks — skills, agents,
system prompts, MCP servers, scripts, mini-apps — and assembles them into projects.
A project is a curated set of those blocks that exports as a ready-to-use archive.

The long-term ambition is **"GitHub / Confluence for AI people"**: store your work
independently of any one machine, keep it as a portfolio, make it public or private,
reuse and recombine it across projects.

The MVP ambition is narrower: a personal, local, single-user library plus a builder.

### The core value is assembly with validation, not storage

Git already stores files. What nothing does today is tell you that a skill needs a
particular MCP server, that two skills write to the same config file, that two items
register the same command name, or that an env variable is missing. Right now you find
out at runtime.

### The "wow" moment

The user has said it is the **export**: a working archive in thirty seconds, with the
system having checked that the set actually holds together. Design decisions should
serve that moment. Two supporting moments matter: the **validation pass** (an animated,
legible check that runs once the set is complete) and **duplicating a project** to
re-tune it for a new context.

---

## 3. Audience and platform

- Design engineers and AI engineers, 25+, who use AI heavily in daily work and have
  accumulated a lot of material they want to keep and reuse.
- Visually literate. They live in tools like Linear, Vercel, Raycast, Figma. The bar for
  craft is high; generic dashboard aesthetics will read as cheap.
- **Desktop-first.** Responsive/adaptive comes later, deliberately.
- **Dark theme from day one.** Light theme is not assumed to be free — treat it as a
  design decision, not a color inversion.

---

## 4. Vocabulary

Use these words consistently in code, design files and UI copy.

| Term | Meaning |
|---|---|
| **Item** | One reusable building block. The atomic unit of the library. |
| **Project** | A named set of items that exports as an archive. |
| **Library** | Everything the user owns, across all projects. |
| **Workspace** | The user's whole space. One per user. Not a team concept. |
| **Stack** | Informal name for the resolved set of items inside a project. |

The word **Bundle** from the original brief is retired. It is **Project**.

---

## 5. Data model (draft)

One entity shape for everything. `kind` is just a field.

```
Item
  id
  kind          skill | agent | prompt | mcp | script | app
  name
  description
  tags: []
  visibility    private | public        // public = eligible for the shared catalog (later)
  source        inline | external
  content                               // if inline
  repoUrl, path                         // if external (a GitHub repo)
  requires: [itemId]
  conflicts: [itemId]
  needsEnv: [string]
  targetPath                            // where it lands on export
  version                               // reserved, see section 9

Project
  id
  name
  description
  visibility    private | public
  members: [ProjectItem]

ProjectItem                             // an item's membership in one project
  itemId
  addedBy       manual | dependency     // dependency = auto-added, shows what pulled it in
  detached      boolean                 // false = live link to library, true = local override
  overrides                             // populated only when detached
```

### The six kinds

- `skill` — a capability definition for an agent
- `agent` — an agent definition / subagent
- `prompt` — a system prompt or prompt template
- `mcp` — an MCP server
- `script` — a small script that runs as part of the setup
- `app` — a mini-app: an external tool or repo used *in the pipeline* rather than by the
  model (text-to-speech, translator, converter). Usually external, but a user may hold a
  local copy.

`script` and `app` are deliberately separate: a script is a file that ships inside the
archive, an app is a program the project depends on.

### Item linkage — the important one

An item lives in the library **once**. Adding it to a project creates a **live link** by
default: editing the item in the library updates every project that links to it. A user
can **detach** an item inside one project and edit it locally without touching the
library or any other project.

Consequences the design must handle:

- an item card needs a "linked" vs "detached" state
- a detached item needs a visible relationship to its library original
  ("modified from library version"), with a way back
- editing a linked item needs to communicate blast radius: *"used in 3 projects"*

### Relations

`requires` and `conflicts` are filled in **manually** when adding or editing an item.
Parsing metadata automatically is out of scope.

---

## 6. Product logic (specification)

**Dependency resolution.** Depth-first walk from the selected items along `requires`.
Everything found is added and marked auto-added. An auto-added item cannot be removed
while the item that pulled it in is still in the project.

**Cycle detection.** Same walk, three node states (untouched / in progress / done).
Hitting an "in progress" node means a cycle; show the chain.

**Conflicts.** Run the resolved set against `conflicts`. A hard conflict blocks export, a
soft one warns. Also check for **duplicate command names** and for items writing to the
**same target path**.

**Env variables.** Collect `needsEnv` across the set; missing ones are surfaced before
export and written to `.env.example`.

**Validation pass.** When the set is complete the user triggers a check that runs
visibly — an animated sweep across dependencies, collisions and missing keys. This is a
designed moment, not a spinner.

### Export

More than a zip of files:

- inline items are placed by `targetPath`, per kind
- external items become instructions in `SETUP.md` (repo link, clone command, placement)
- all MCP servers merge into a single config, with key collisions checked separately
- missing env variables are collected into `.env.example`

**Agent target.** The user picks the target before exporting, and naming and paths in the
generated docs adapt:

- `Claude Code` — `.claude/skills/`, `.claude/agents/`, `CLAUDE.md`, `.mcp.json`
- `Cursor` — `.cursor/rules`, MDC format, its own MCP config
- `Codex` — `AGENTS.md` conventions
- `Universal` — neutral structure plus `SETUP.md`; the agent adapts it later

External repos are **never vendored into the archive** — they are always instructions.

---

## 7. Item states in the list

This is the heart of the UI. A card must read unambiguously in each state:

1. not selected
2. selected manually
3. auto-added as a dependency (showing what pulled it in)
4. conflicts with something already selected
5. blocked because of a conflict
6. selected but missing an env variable
7. detached — locally modified inside this project

State 7 is new relative to the original brief and is easy to forget.

---

## 8. Screens (planned)

- **Library** — the full collection. Filters by kind and tag, search, add/edit form.
- **Project Builder** — a filtered sidebar of the library on the left; items are dragged
  into the project area to assemble the stack. Live validation as the set changes.
  This is *not* a node canvas: no hand-drawn edges, no execution order. The set is a set;
  relations come from the items themselves and are surfaced here, not authored here.
- **Result** — the file tree of the future archive, the env variable list, agent target
  selector, export button.
- **Projects** — saved projects, duplication, visibility.

---

## 9. Deliberately out of scope for the MVP

Kept in the architecture's line of sight, not built:

- **Versioning.** No history, no diffs, no rollback, no version pinning in projects. The
  `version` field is reserved and nothing reads it yet.
- **Sharing and the public catalog.** `visibility` exists in the model and in the UI's
  vocabulary; there is no server to publish to. Public/private is designed for, not wired
  up.
- **Accounts, sync, teams.** Single user, one workspace.
- **Automatic metadata parsing** from item content.
- **Automatic version conflict resolution.** A version mismatch is shown as a conflict.

Do not build these. Do not design a screen that only makes sense once they exist.

---

## 10. Tech stack and conventions

- **Next.js + React + TypeScript.** Chosen over Vite specifically so the later public
  catalog and shareable project pages do not require a migration. Until then it runs
  entirely client-side.
- **No UI kits.** No MUI, no shadcn, no Chakra. The design system is custom and is part of
  the product's value.
- **No Figma upstream.** Design happens in code and in whatever mockups we produce here.
- **Storage:** IndexedDB, once we get to logic. No backend.
- **Archive:** built in the browser (JSZip).
- **Library portability:** export/import of the whole library as JSON — this covers both
  backup and informal sharing before any server exists.
- Styling engine is still open (see section 12).

---

## 11. How items get into the library

Manually, by the user, from their local material. This is the known cold-start problem:
an empty library kills the product, because there is nothing to validate.

For any demo, mockup or prototype we need **~30 realistic items with meaningful relations
between them** — real dependency edges, at least one genuine conflict, several items
needing env keys. Placeholder lorem content makes the whole product look pointless.

Later, not now: a starter catalog, and public items flowing into a shared catalog.

---

## 12. Open questions

- Styling engine: Tailwind vs CSS Modules vs vanilla-extract. Not decided.
- Visual direction and tone. Deliberately postponed until after research.
- Competitors and references to position against — not yet surveyed.
- Whether a project can contain another project (composition), or only items.
- Whether detached items should be promotable back into the library as new items.

---

## 13. Working agreements

- Docs, code and UI copy in English. Conversation with the user may be in Russian.
- Do not scaffold the app, generate mockups, or pick a visual direction before the
  research phase is signed off.
- This file is the single source of truth for the product. The original brief has been
  folded into it and deleted; there is no other spec to reconcile against.
