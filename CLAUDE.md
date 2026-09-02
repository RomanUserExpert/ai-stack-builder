# CLAUDE.md — AI Stack Builder

Working context for Claude Code on this project. Read this before doing anything.
All documentation, code, comments and UI copy in this repo are written in **English**.

---

## 1. Current phase — read this first

**Phase: Research is signed off (2026-09-02). The design system is next and has not started.**

There is still no application code, no design system, no mockups. The design system may now begin;
nothing after it may.

The agreed order of work:

1. ~~Research~~ — **done, signed off 2026-09-02**
2. **Design system** (tokens, typography, color, components) ← next, not started
3. Mockups / screen design (static, no logic)
4. Static frontend implementation (markup only, no business logic)
5. Logic (state, storage, validation, export)

**All five research stages are done.** Landscape, flows and pain; then **benchmark** — 15
product-and-flow cells scored against five categories lifted from stages 1–3
([`research/4-benchmark/benchmark.md`](research/4-benchmark/benchmark.md)); then **patterns** — five shapes for the key flow
compared on that rubric, with the chosen one written into §8 below and the four rejected kept in
[`research/5-patterns/patterns.md`](research/5-patterns/patterns.md).

**The six open questions were closed in one sitting on 2026-09-02** — four answered, two deferred
with a stated reason. Everything they changed is in this file; the reasoning, and what was read
before each decision, is in section 3 of [`research/FINAL.md`](research/FINAL.md). Two of the
answers widened the MVP and are marked as such below: a **curated public library ships with the
product** (§8, §11), and **`SETUP.md` is written for the agent that opens the archive** (§6).

**For a single consolidated read of the whole phase**, see [`research.md`](research.md) — competitors,
flows, benchmark, patterns and conclusions in five sections, every fact linked to its source or
capture, and every unestablished claim marked as such. **It is a digest and never a source of
truth**: this file is the spec, [`research/FINAL.md`](research/FINAL.md) is the close, and the
register in [`research/research-plan.md`](research/research-plan.md) is the only list of open
questions. Do not answer a question from the digest that these three answer differently.

**The research folder is organised by stage**, and two files govern it:
[`research/FINAL.md`](research/FINAL.md) is the closing document — what the phase produced, the
decisions taken, how the six questions were settled, and the documents that are read from more than
one stage. [`research/research-plan.md`](research/research-plan.md) is the spine and holds the
register, now empty. **Start at `FINAL.md`.**

Do not skip ahead. If a request seems to jump past the design system, confirm before acting.
Product logic described in this file is **specification, not a build order** — it is
written down so design decisions are made with the real mechanics in view.

**One piece of the research phase is handed forward as work rather than as a decision:** the curated
public library has to be **built** — real items from checked sources, each with its origin and a
pinned `ref`, composed so the example project genuinely produces one Problem and one Note. It does
not block the design system, and it is not a demo asset. See §11.

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

**A detached item is edited inside the project** (decided 2026-09-02). This is what makes detaching a
feature rather than a toggle: if every edit still had to happen in the Library, *detached* would be a
synonym for *unlinked*, `overrides` would never fill, and state 6 in §7 would be decoration. The edit
happens on the project's row and writes to `overrides`, never to the library item.

**The way back is promotion, and it creates a new item** (decided 2026-09-02). A detached item can be
promoted into the Library **as a new item**, with the project's row re-linking to it. It is not
merged into the original: updating the original would change every other project that links to it —
blast radius spent on an action taken inside one project, which is the thing this section exists to
warn about. *Push my changes to the original* is a different action with a different confirmation and
is **not built in the MVP**. Flow 05 found there is no prior art for a return path — Figma erases the
origin at detach — so this one is invented rather than copied; see
`research/2-flows/05-linked-vs-detached/NOTES.md`.

**What an item card claims, and what it never claims** (decided 2026-09-01). Trust in a *set* comes
from the validation pass. The only per-item evidence we show is derived from the library itself —
*used in 3 projects*, *2 items require this*, *last exported 12 days ago*. Those are usage facts, not
quality judgements, and they need no network. We ship **no score, no rating, no eval result and no
badge**: the market has converged on measured trust (Tessl scores every skill, Smithery every server),
and we have no way to run an item, so any number we invented would be decoration.

### Public items

Some items are not the user's own. The **public library** (§8, §11) ships with the application and is
**read-only**: an item there can be added to a project or copied into `My library`, but never edited
in place and never published to. Public items are ordinary `Item`s in every other respect — the shape
above already carries what they need, `repoUrl` and a pinned `ref`. Two things follow for design:
each public item **shows its origin**, because it is someone else's work, and the pinned `ref` is
what keeps a shelf with no server behind it honest — it says *this is the version we checked*, not
*this is current*.

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
in `research/2-flows/04-validation-check-results/NOTES-vercel.md`.

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
point of the product. See `research/4-benchmark/NOTES-figma-export.md`.

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

**`SETUP.md` is written for the agent that opens the project, not for a human reader** (decided
2026-09-02). This is the answer to the open question about how much weight the document carries, and
it changes what the document is rather than only how long it is:

> `SETUP.md` states, **per item in the resolved set**, what that item requires — its dependencies,
> the MCP servers it needs, the env keys it expects, the external repos to clone **at their pinned
> `ref`**, and where everything lands for the chosen agent target. On project init the agent reads it
> and performs the setup.

The reasoning is in `research/FINAL.md` §3, Q2, and it rests on two things. The loudest pain in the
ecosystem is *the archive lands on a machine and does not run* — 182 reactions for
*MCP Servers Don't Work with NVM*, over a top-of-tracker made of PATH, node version managers and
platform paths (`research/3-pain/user-pain.md`). And the benchmark found **B4 — produce an artefact
and hand it over — is the weakest flow in the industry**, nobody above 4, with every cell scoring
what a product says about its own state and none about the machine its artefact lands on.

Writing for an agent aims at that pain **without a platform matrix and without a new artefact**. It
also explains why the agent target selector sits where it does: the target does not only choose
paths, it chooses the reader.

**What this is not.** We run nothing on anyone else's machine, and there is **no verify script in the
MVP** — we write instructions precise enough to be executed by something that can. Emitting a verify
script later must be a new stage in the run, not a rewrite of the export; design it so.

**The handover is disclosed before Export, not after.** Run's last stages state what the archive
contains and what the receiving machine must still do — `SETUP.md` preview, pinned `ref`s,
target-correct paths, `.env.example` — read **before** the irreversible step, which is the
consequence-disclosure standard the rest of this file holds itself to.

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
of one axis. See `research/2-flows/05-linked-vs-detached/NOTES.md`.

**State 6 carries three commands, and they are one axis, not three features** (2026-09-02): **Edit**
here, in the project, which is the only place a detached item is editable and the reason the state
exists at all; **Reset**, whole-item or single-field, which walks the change back; and **Promote**,
which lifts the modified copy into the Library as a new item and re-links this row to it. See §5.

**A former state, "blocked because of a conflict", is gone** (2026-09-01). Nothing blocks — see
section 6 — so no item is ever unselectable. A conflicting item reads as state 4, and the Problem
is carried by the project, not by the card.

---

## 8. Screens

Chosen 2026-09-01 at the end of the research phase. Five shapes for the key flow — **assemble a set
→ check it → export** — were compared on the benchmark's five categories; the reasoning, the four
rejected variants and what each donated are in [`research/5-patterns/patterns.md`](research/5-patterns/patterns.md).

The result is a hybrid, stated as a choice: **command-first assembly, and a run-centric check that
ends in the export.** Three surfaces in the flow, plus Projects.

**Confirmed 2026-09-02, when the open-question register was closed.** This section was provisional
because Q1, Q2 and Q4 land inside this flow and Q2 might have added a surface no variant had. It did
not: Q2 lands as two more stages inside Run, which is already a stage list; Q1 as a scope switch
inside Library, which is already a browse screen; Q4 as commands on a project row, exactly where
stage 5 predicted. **Three surfaces plus Projects, and the seam is still Check.** The finalisation
section of [`research/4-benchmark/benchmark.md`](research/4-benchmark/benchmark.md) still governs how
to read the scores behind it: the rubric grades craft, not weight.

- **Library** — the full collection. Filters by kind and tag, search, add/edit form, and the
  per-item usage facts of §5. It is where you keep things, and **it is not part of the builder
  flow**. (This is the change: an earlier draft put a filtered library sidebar inside the builder and
  made drag the mechanism. Drag does not survive 300 items, and a pane that cannot act during a check
  is the mistake §6 and §9 already refuse elsewhere.)

  **It has two scopes, and one switch between them** (decided 2026-09-02): **`My library`** and
  **`Public library`**. Visually identical — same rows, same search, same filters — because they are
  the same object seen in two places. `My library` holds the user's own items and **starts empty on
  first run**, honestly. `Public library` holds a curated set that ships with the application,
  **read-only**: add from it into a project, or copy it into your library, but never edit it in place
  and never publish to it. This is how the product has material from the first second without putting
  someone else's work in a space labelled *mine* — see §11 for what ships and §5 for how public items
  behave.
- **Project** — the set as a **list**, not a canvas and not a pane pair. `⌘K` adds items by name; the
  palette is the only way the library reaches this screen, and it opens cold on **related** items —
  the ones that require, or are required by, what is already in the set. Every row carries its own
  state, including *detached* with the differing fields named (§7), and a finding annotates the row
  that owns it. **A detached row is also where that item is edited, reset and promoted** (§5, §7) —
  the project is the only place a local override exists, so it is the only place it can be worked on.
  Still *not* a node canvas: no hand-drawn edges, no execution order. The set is a set; relations
  come from the items and are surfaced here, not authored here.
- **Run** — entered by **Check**, and it takes the whole surface: a stack of stages, each with its
  own verdict, duration and expansion, in the shape of a Vercel deployment page. The file tree of the
  future archive, the env variable list and the agent target selector live here, and **Export is the
  final stage** rather than a button beside the check. Export is always live (§6); an unclean set is
  confirmed in the row below the finding that caused it.

  **The last stages before Export are the handover** (added 2026-09-02): what the archive contains,
  and what the receiving machine must still do — the `SETUP.md` the agent will read, the pinned
  `ref`s, the target-correct paths, `.env.example`. They are stages like any other, with verdicts and
  expansion, and they are read **before** the irreversible step. See §6.
- **Projects** — saved projects and duplication, plus **the example project that ships on first
  run** (§11), labelled as an example and deletable. **Not visibility** — §9 keeps that control out
  of the MVP interface entirely, and this line used to say otherwise. Corrected 2026-09-02.

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
- **Composition — a project inside a project.** **Deferred, not refused** (2026-09-02). Items only
  in the MVP. Two reasons: none of the five pattern variants needed composition in order to work, and
  a search for `reuse blocks assistant` returned **0 results** in a 6,677-issue tracker belonging to a
  product that shipped a hub for exactly this. But it stays interesting, and the reason to hold it
  back is also the reason to be careful with it later — **composition risks unbounded recursion**. A
  project containing a project containing a project is a resolution problem we would have to bound,
  and the three-state walk in §6 exists for cycles among *items*, not among sets. **Revisit post-MVP,
  and decide the depth rule before the feature**, not after.
- **Publishing to a public catalog.** `visibility` stays in the model, and there is no server to
  publish to — so **the control is not shown in the MVP interface at all** (decided 2026-09-01).
  **Note the asymmetry, added 2026-09-02: consuming a curated public library is in the MVP (§8, §11);
  publishing to one is not.** A read-only shelf that ships with the application needs no server,
  no accounts and no moderation. Nothing about it makes `visibility` a control the user can touch.
  A switch that cannot act does not belong on a primary surface: Linear, Figma and GitHub all hide
  an action there until it has something to do. Do not ship a dead toggle on the most load-bearing
  word in the model. (The rule has one documented exception and it does not apply here — **context
  menus grey rather than hide**, because a stable item order is worth more than a short list. See
  finding 7 in `research/4-benchmark/benchmark.md`.)
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
- **Styling engine — deferred to the design-system phase** (2026-09-02), decided on two built
  components rather than in the abstract. The criterion is fixed now: **tokens and two real themes
  must be first-class**, and the engine must not push utility classes into components that are
  themselves the product's value. Tailwind, CSS Modules and vanilla-extract are all still live.

---

## 11. How items get into the library

Two ways, and the second is new as of 2026-09-02.

**Manually, by the user**, from their own local material. `My library` starts empty on first run and
fills up this way. This was the known cold-start problem: an empty library kills the product, because
there is nothing to validate.

**And from the public library, which ships with the application.** A curated, **read-only** set of
real items — skills, agents, prompts, MCP servers — taken from sources we have checked, reachable
from the first second behind the scope switch in §8. The user adds from it into a project, or copies
an item into `My library` and owns the copy from then on. This is what solves cold start: the product
has material immediately, and `My library` stays honestly the user's.

**A public shelf guarantees material; it does not guarantee the first check says anything.** A user
who picks three unrelated items gets six green ticks, which teaches nothing about what the product is
for. So **one example project ships too**, in Projects, built entirely from public items and composed
so that it contains **at least one Problem and at least one Note** — a real target-path collision, a
genuinely missing env key. It is labelled as an example and it is deletable. It sits in Projects
rather than in the library, because that is where being an example is honest.

**What has to be built, and to what standard.** This is real work, not a demo asset:

- **Real content from checked sources.** Placeholder lorem makes the whole product look pointless.
- **Meaningful relations** — real `requires` edges, at least one genuine `conflicts` pair, several
  items with `needsEnv`, at least two items that write to the same target path.
- **Provenance on every item.** These are other people's work: `repoUrl` and a pinned `ref`, shown,
  not just stored (§5).
- **Enough of it to browse rather than to read** — the switch has to feel like a library, not a list.
  The **~30 realistic items** figure that used to live here as a mockup requirement is the right
  order of magnitude for this too, and the same set serves both jobs.

Later, still not now: user items flowing *out* into a shared catalog. That needs a server; see §9.

---

## 12. Open questions

**The open ones live in one place, and it is not here.**
[`research/research-plan.md`](research/research-plan.md) ends with a register — every open question
with an ID, who raised it, **what would answer it**, and what it blocks. Section 3 of
[`research/FINAL.md`](research/FINAL.md) holds the other half: what was read before each decision and
what the alternatives were. Questions are added to the register as work turns them up and answered
together in a sitting, once the picture is whole, rather than one at a time on partial evidence. Do
not keep a second list in this file; two lists drift, and this document has already been bitten by
that twice. **The protocol outlived the research phase** — the design system uses the same register.

**The register is empty.** All six were closed in one sitting on 2026-09-02 — four answered, two
deferred with a stated reason. Their dispositions are below; the reasoning, and what was read before
each, is in section 3 of [`research/FINAL.md`](research/FINAL.md).

**Closed, and recorded here because the answers are part of the spec.**

- ~~Competitors and references to position against~~ — surveyed. 15 companies, 12 flows, ~70 captures,
  two issue trackers and the source of the nearest dead competitor, in [`research/`](research/), one
  folder per stage. Start at [`research/FINAL.md`](research/FINAL.md).
- ~~Visual direction and tone~~ — still not chosen, but no longer a question *here*: it is the first
  task of the design-system phase, with its reference material already gathered in
  `research/2-flows/10-dark-design-language/`.
- ~~Does `visibility` appear in the MVP interface~~ — no. Section 9.
- ~~Does anything read `version`~~ — the field is gone; external references are pinned instead.
  Sections 5 and 9.
- ~~What per-item trust signal do we ship~~ — usage facts from the library, never a score. Section 5.
- ~~Does the validation pass block, or grade?~~ — neither. Three severities, and export is never
  disabled; an unclean set is confirmed rather than refused. Section 6.

**Closed on 2026-09-02, in the sitting that signed the research phase off.**

- ~~Cold start: demo problem or product decision? (Q1)~~ — a product decision. A **read-only public
  library ships with the application** behind a scope switch beside `My library`, plus one example
  project carrying a real Problem and a real Note. Sections 8 and 11.
- ~~How much weight does `SETUP.md` carry? (Q2)~~ — more than one line, and the recipient changed:
  it is **written for the agent that opens the project**, which reads it and performs the setup. No
  verify script in the MVP. Section 6.
- ~~Can a project contain another project? (Q3)~~ — not in the MVP. **Deferred rather than refused**,
  because of recursion; decide the depth rule before ever building it. Section 9.
- ~~Can a detached item be promoted back into the library? (Q4)~~ — yes, **as a new item**, with the
  row re-linking to it. And it drags a feature in with it: **a detached item is edited inside the
  project**, without which detach is only unlink. Sections 5, 7 and 8.
- ~~Loss or reassembly cost — which drives adoption? (Q5)~~ — **deferred, accepted risk.** No
  instrument here can answer it. The trigger is written down: ask five practitioners before the first
  feature that only pays off under one answer. Blocks positioning, not the build.
- ~~Styling engine (Q6)~~ — **deferred to the design-system phase**, decided on two built components.
  The criterion is recorded: tokens and two real themes first-class, and the engine must not push
  utility classes into components that are themselves the product's value. Section 10.

---

## 13. Working agreements

- Docs, code and UI copy in English. Conversation with the user may be in Russian.
- The research phase is signed off (2026-09-02) and the design system may start. Do not scaffold
  the app or generate mockups before the design system exists.
- This file is the single source of truth for the product. The original brief has been
  folded into it and deleted; there is no other spec to reconcile against.
