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

**All five research stages are done.** Landscape, flows and pain; then **benchmark** — 15
product-and-flow cells scored against five categories lifted from stages 1–3
([`research/benchmark.md`](research/benchmark.md)); then **patterns** — five shapes for the key flow
compared on that rubric, with the chosen one written into §8 below and the four rejected kept in
[`research/patterns.md`](research/patterns.md).

**One thing stands between here and sign-off**: the open-question register at the end of
[`research/research-plan.md`](research/research-plan.md), worked through in a single sitting. Until
that is done the phase is not signed off, and the design system does not start.

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
  repoUrl, path, ref                    // if external: repo, file, and a pinned commit/tag/version
  requires: [itemId]
  conflicts: [itemId]
  needsEnv: [string]
  targetPath                            // where it lands on export

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

**What an item card claims, and what it never claims** (decided 2026-09-01). Trust in a *set* comes
from the validation pass. The only per-item evidence we show is derived from the library itself —
*used in 3 projects*, *2 items require this*, *last exported 12 days ago*. Those are usage facts, not
quality judgements, and they need no network. We ship **no score, no rating, no eval result and no
badge**: the market has converged on measured trust (Tessl scores every skill, Smithery every server),
and we have no way to run an item, so any number we invented would be decoration.

### Relations

`requires` and `conflicts` are filled in **manually** when adding or editing an item.
Parsing metadata automatically is out of scope.

---

## 6. Product logic (specification)

**Dependency resolution.** Depth-first walk from the selected items along `requires`.
Everything found is added and marked auto-added. An auto-added item cannot be removed
while the item that pulled it in is still in the project.

**Cycles are information, not errors** (decided 2026-09-01). The walk still tracks three node
states (untouched / in progress / done), because it has to terminate. But a project is a **set**,
not an execution order — we never ask what runs first — so if A requires B and B requires A, both
are added and the set is complete and correct. A cycle is a hazard for our traversal, not a defect
in the user's work. Report it as a fact — *"these three always travel together"* — never as a
failure. An earlier draft said "show the chain", which was right, next to a heading that implied
something was wrong.

**Conflicts and collisions.** Run the resolved set against `conflicts`. Also check for **duplicate
command names** and for items writing to the **same target path**. Every one of these is a
*Problem* in the sense below — `conflicts` stays a flat `[itemId]` list with no hard/soft flag,
because nothing here blocks and the distinction therefore has no work to do. An earlier draft said
a hard conflict blocks and a soft one warns, which the data model had no way to express.

**Env variables.** Collect `needsEnv` across the set; missing ones are surfaced before
export and written to `.env.example`.

**Validation pass.** When the set is complete the user triggers a check that runs
visibly — an animated sweep across dependencies, collisions and missing keys. This is a
designed moment, not a spinner. Structurally it is a stack of stages, each carrying its own
verdict and its own duration, each expandable — the model is Vercel's deployment page, written up
in `research/flows/04-validation-check-results/NOTES-vercel.md`.

### Three severities, and nothing blocks

Decided 2026-09-01. Every finding is one of:

- **Problem** — the archive will be wrong. A duplicate command name, a target-path collision, a
  declared conflict, an unresolvable requirement.
- **Note** — the archive is correct but incomplete. Missing env keys, an external item with no
  pinned `ref`.
- **Skipped** — the check had nothing to check. It gets its own neutral glyph: not a green tick it
  did not earn, and not a red one it does not deserve.

**Export is never disabled.** Almost nothing makes an archive impossible to produce — a missing env
key still zips, a duplicate command still zips, it is simply wrong inside. Blocking is therefore
almost always a choice, and we do not make it, for three reasons. It is the user's own library on
their own machine. A permanently disabled export button is a dead end, and on **primary surfaces**
the research is consistent that an action which cannot act is not shown — a greyed-out primary
action is that same mistake on the most important control in the product. And the promise is
*the system checked*, not *the system forbade*.

Figma's export dialog does exactly what we are refusing — `0 of 0 selected` beside a greyed `Export`
— and the benchmark records why it gets away with it: the blocker is one named action away, it is a
property of this second's selection rather than of the document, and re-exporting costs nothing. Our
Problems are properties of the project, the fix may be four items away, and the archive is the whole
point of the product. See `research/benchmark/NOTES-figma-export.md`.

**Instead, an unclean export is confirmed.** Pressing Export on a set with Problems opens a
confirmation that names the consequence in the present tense, in GitHub's mergebox register:

> Two items write to `.mcp.json`. The archive will contain only one of them — `db-tools`.

This is `terraform apply`: never refuse, always make the cost legible before the irreversible step.
A grade — Port's `Basic → Low → Good → Great` — was considered and rejected: a ladder is for
comparing many entities against one standard, and we check one set against itself, where there is
no *better*, only *coherent* or *not*.

### Export

More than a zip of files:

- inline items are placed by `targetPath`, per kind
- external items become instructions in `SETUP.md` — repo link, clone command **at the pinned `ref`**, placement
- all MCP servers merge into a single config. A key collision is checked separately, and **two
  items declaring the same server key at different `ref`s is a collision too** — one of them will
  not be in the exported config, so say which and say both refs
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
5. selected but missing an env variable
6. **detached — locally modified inside this project**

State 6 is new relative to the original brief and is the easiest to forget. Figma proves how: it
models overrides precisely enough to offer `Reset fill` by name, and then draws a modified instance
identically to a clean one everywhere except a context menu. The diff is already computed, so the
card carries it — and names the fields that differ, not just the fact that some do. Revert needs two
granularities, the whole item and a single field, with Reset kept next to Detach as the two halves
of one axis. See `research/flows/05-linked-vs-detached/NOTES.md`.

**A former state, "blocked because of a conflict", is gone** (2026-09-01). Nothing blocks — see
section 6 — so no item is ever unselectable. A conflicting item reads as state 4, and the Problem
is carried by the project, not by the card.

---

## 8. Screens

Chosen 2026-09-01 at the end of the research phase. Five shapes for the key flow — **assemble a set
→ check it → export** — were compared on the benchmark's five categories; the reasoning, the four
rejected variants and what each donated are in [`research/patterns.md`](research/patterns.md).

The result is a hybrid, stated as a choice: **command-first assembly, and a run-centric check that
ends in the export.** Three surfaces in the flow, plus Projects.

**This section is provisional until the open-question register is closed.** Q1, Q2 and Q4 all land
inside this flow, and Q2 may add a surface no variant has — see the finalisation section of
[`research/benchmark.md`](research/benchmark.md), which records that the rubric grades craft rather
than weight, and that the pain evidence sits in the check-and-export end of the flow. Do not build
against this yet.

- **Library** — the full collection. Filters by kind and tag, search, add/edit form, and the
  per-item usage facts of §5. It is where you keep things, and **it is not part of the builder
  flow**. (This is the change: an earlier draft put a filtered library sidebar inside the builder and
  made drag the mechanism. Drag does not survive 300 items, and a pane that cannot act during a check
  is the mistake §6 and §9 already refuse elsewhere.)
- **Project** — the set as a **list**, not a canvas and not a pane pair. `⌘K` adds items by name; the
  palette is the only way the library reaches this screen, and it opens cold on **related** items —
  the ones that require, or are required by, what is already in the set. Every row carries its own
  state, including *detached* with the differing fields named (§7), and a finding annotates the row
  that owns it. Still *not* a node canvas: no hand-drawn edges, no execution order. The set is a set;
  relations come from the items and are surfaced here, not authored here.
- **Run** — entered by **Check**, and it takes the whole surface: a stack of stages, each with its
  own verdict, duration and expansion, in the shape of a Vercel deployment page. The file tree of the
  future archive, the env variable list and the agent target selector live here, and **Export is the
  final stage** rather than a button beside the check. Export is always live (§6); an unclean set is
  confirmed in the row below the finding that caused it.
- **Projects** — saved projects, duplication, visibility.

**The known cost of this choice.** With no library pane in the builder, you cannot see what you are
not using. Three things carry that weight and are therefore load-bearing, not decorative: the
palette opening on related items, the Library being one keystroke away and remembering where you
were, and per-item usage facts doing the work a visible pane would otherwise do.

---

## 9. Deliberately out of scope for the MVP

Kept in the architecture's line of sight, not built:

- **Versioning of your own items.** No history, no diffs, no rollback, and **no `version` field on
  the item** — decided 2026-09-01. An item lives in the library once and projects link to it live,
  so `detached` plus `overrides` already does the job a version number would: it is how a project
  says *I do not want the current one*. A second, parallel mechanism for the same thing is not
  built. **External references are a different matter and are pinned** — see `ref` in section 5.
  If real versioning is ever wanted, both the field and the history are additive.
- **Sharing and the public catalog.** `visibility` stays in the model, and there is no server to
  publish to — so **the control is not shown in the MVP interface at all** (decided 2026-09-01).
  A switch that cannot act does not belong on a primary surface: Linear, Figma and GitHub all hide
  an action there until it has something to do. Do not ship a dead toggle on the most load-bearing
  word in the model. (The rule has one documented exception and it does not apply here — **context
  menus grey rather than hide**, because a stable item order is worth more than a short list. See
  finding 7 in `research/benchmark.md`.)
- **Accounts, sync, teams.** Single user, one workspace.
- **Automatic metadata parsing** from item content.

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

**The open ones live in one place, and it is not here.**
[`research/research-plan.md`](research/research-plan.md) ends with a register — every open question
with an ID, which stage raised it, **what would answer it**, and what it blocks. Questions are added
there as stages turn them up and answered together at the end, once the picture is whole, rather than
one at a time on partial evidence. Do not keep a second list in this file; two lists drift, and this
document has already been bitten by that twice.

Live at the time of writing: cold start (Q1), how much weight `SETUP.md` carries (Q2), project
composition (Q3), promoting a detached item back into the library (Q4), what actually drives adoption
(Q5), and the styling engine (Q6).

**Closed, and recorded here because the answers are part of the spec.**

- ~~Competitors and references to position against~~ — surveyed. 15 companies, 12 flows, ~70 captures,
  two issue trackers and the source of the nearest dead competitor, in [`research/`](research/). Start
  at [`research/research-plan.md`](research/research-plan.md).
- ~~Visual direction and tone~~ — still not chosen, but no longer a question *here*: it is the first
  task of the design-system phase, with its reference material already gathered in
  `research/flows/10-dark-design-language/`.
- ~~Does `visibility` appear in the MVP interface~~ — no. Section 9.
- ~~Does anything read `version`~~ — the field is gone; external references are pinned instead.
  Sections 5 and 9.
- ~~What per-item trust signal do we ship~~ — usage facts from the library, never a score. Section 5.
- ~~Does the validation pass block, or grade?~~ — neither. Three severities, and export is never
  disabled; an unclean set is confirmed rather than refused. Section 6.

---

## 13. Working agreements

- Docs, code and UI copy in English. Conversation with the user may be in Russian.
- Do not scaffold the app, generate mockups, or pick a visual direction before the
  research phase is signed off.
- This file is the single source of truth for the product. The original brief has been
  folded into it and deleted; there is no other spec to reconcile against.
