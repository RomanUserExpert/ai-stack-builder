# CLAUDE.md — AI Stack Builder

Working context for Claude Code on this project. Read this before doing anything.
All documentation, code, comments and UI copy in this repo are written in **English**.

**How to read this file.** It is the product's specification and the rules for working on it, stated **as they
hold now**. Each decision cites its register entry, `(Q24)`; the reasoning, the alternatives and the date are in
the register ([`01-research/research-plan.md`](01-research/research-plan.md)), not here. **This file keeps no
history**: superseded wording is not struck through and left in place — it is replaced, and git keeps the old
text (the last version that carried the full dated history is commit `9e61f7f`). Section numbers are stable
and are cited across the repo and by the generators (`CLAUDE.md §18`); **do not renumber them**.

---

## 1. Current phase — read this first

**Lessons 01–09 are closed. The next is 10, responsive, and it is not opened until the owner says so** — every
lesson opens on the owner's word. If a request jumps ahead — to responsive or motion — confirm before acting.
Until lesson 10 opens, the system grows only by §18, and **no colour value is written before the owner signs
it**. Every line of copy is written against §14.

**What exists:** research, personas and jobs, the information architecture, every screen as a wireframe and a
dressed mockup, every flow as a clickable prototype, the voice and every line of microcopy, the concept, and the
design system at [`design-system/`](design-system/README.md). **There is no application code.** Do not scaffold
the app before there is something for it to hold. Product logic in this file is **specification, not a build
order** — it is written down so design decisions are made with the real mechanics in view.

### The order of work — the course's twelve lessons

This work is homework for a design-engineering course, and the order of work **is the course's list**. Each
lesson is one folder (§13) with its own `README.md` and a phase page.

| | Lesson | State |
|---|---|---|
| **01** | Research and benchmark | Closed 2026-09-02 — stages 1–5 · [`research.html`](01-research/research.html) · start at [`FINAL.md`](01-research/FINAL.md) |
| **02** | Personas and JTBD | Closed 2026-09-09 — stages 6–7 · [`personas.html`](02-personas-jtbd/personas.html) |
| **03** | Information architecture | Closed 2026-09-20 · [`ia.html`](03-information-architecture/ia.html) · summary in §8 |
| **04** | Prototyping and wireframing | Closed 2026-09-27 — every screen and flow · [the viewer](04-wireframes/pages/wireframes.html) · [prototypes](04-wireframes/prototypes/prototypes.md) and their [conventions](04-wireframes/prototypes/_conventions.md) · [critique](04-wireframes/_critique.md) (Q35) |
| **05** | Tone of voice and microcopy | Closed 2026-10-05 · [`voice.html`](05-tone-of-voice/voice.html) · §14 |
| **06** | Concept | Closed 2026-10-11 — Mica · Lime · [`style.html`](06-concept/style.html) · §15 |
| **07** | UI assembly | Closed 2026-10-28 — every screen and flow step dressed · [`ui.html`](07-ui-assembly/ui.html) · §16 |
| **08** | Design tokens | Closed 2026-11-03 · [`tokens.html`](08-design-tokens/tokens.html) · §17 |
| **09** | Design system | Closed 2026-11-03 (Q51) · [`system.html`](09-design-system/system.html) · [the showcase online](https://ai-stack-builder-research.vercel.app/design-system/docs) · §18 |
| **10** | Responsive | **Next, not opened.** §3 says desktop-first and deliberately late; this is that lesson |
| **11** | Animation and micro-interactions | The validation pass is a designed moment (§6), and it gets designed here |
| **12** | Handoff and documentation | The thing being handed off is a product whose whole subject is handover |

*Logic* — state, storage, validation, export — comes after 12: nothing in the twelve requires it. *Static
frontend implementation* is how 07 and 09 are built, because design happens in code (§10).

**The phase pages.** The pages call a lesson a *phase* (*Phase 01* is the course's lesson 01). Each has the same
shape as the course's reference page: a skip link, a meta line saying which phase of twelve and when it was last
re-verified, a rail titled *in this phase*, an **Overview** of what we saw and what we decided, the stage
sections, and the evidence. A sidebar lists **all twelve** lessons, the current one marked and the unbuilt ones
marked *soon* — **the strip shows the twelve and nothing else.** Their look is not the product's; it is
[`DESIGN-artifacts.md`](DESIGN-artifacts.md) (§13).

### Evidence — the rule every claim about people follows

Every claim about people carries one of three marks, defined in [`01-research/research.md`](01-research/research.md),
*The three marks*: **`✓`** confirmed by an instrument another person can re-run · **`*`** reported by a
practitioner in an interview · **`?`** unknown.

- **A `*` never becomes a `✓` by repetition.**
- **A re-runnable query proves that something was *said*, not that it is *true*.** An issue body, a forum comment
  and a README are people describing their own behaviour; the `✓` covers the utterance, not the behaviour.
- **The mark is per claim, not per document.** No document carries a blanket label.
- **We have one interview, no analytics and no users.** Four practitioner conversations are owed and cannot be
  run; nothing is promoted because of that. The adoption story is hypothesis marked `[?]`.
- **Where a structural decision would need a `[?]` cell of the jobs matrix to be a number, say so on the spot and
  leave the decision marked — do not invent the person.** The matrix has about thirty `[?]` cells.
- **The receiver (P2) has never spoken in the first person**: after four rounds and five venues, every account
  of a handover is written by the sender. That is why §8's shared surfaces carry the most conservative rule in
  the product.

### What the research established, in brief

- **Three personas, one primary** ([`personas.md`](02-personas-jtbd/6-personas/personas.md)): *the keeper who
  runs several agents* — **the collector**, primary (Q7, §3) — *the receiver*, and *the empty-handed*, for whom
  §8's scope switch and §11's shelf ship. The empty-handed has been observed once: four of five voices refused,
  minimised or preferred their own material; what survived is *provenance over volume*.
- **Jobs** ([`jtbd.md`](02-personas-jtbd/7-jobs-to-be-done/jtbd.md)): one main job, four related, three emotional,
  two social, seven hypothesis jobs, and the matrix. **The main job is *assemble a set that holds together*
  (Q8), so §2 stands as written**; the *transfer* wording the evidence produced is recorded in `jtbd.md` §1 and
  not adopted. A second main-job candidate — observability of what ran — is a different product and is refused
  (Q12, §9).
- **The MVP core is three jobs**: the main job; *move the work without moving the secrets*; *fix it once and have
  the fix reach every copy* (§5's live link). Only the first is selected by the matrix mechanically; the other
  two are kept on stated grounds — the market is open in both, and this file already spends a mechanism on each.
  `jtbd.md` §8 says so. *(A `3` in the matrix means a reason they would change how they work; where the person on
  record demonstrably did not, the cell was lowered.)*
- **Six specified features close a job whose every cell is `[?]`** — sharpest, the public shelf and the example
  project. **That is a list of hypotheses, not a cut list. Nothing is removed** — it rests on absences in
  instruments that cannot see presence, four sceptics on Hacker News are not a market, and no beginner was asked
  anything. It bears on what the shelf holds and how it sorts (Q9).
- **The handover test** ([round 3](02-personas-jtbd/6-personas/re-research.md#round-3-five-questions-that-need-no-interview),
  Q-F, [captures](02-personas-jtbd/6-personas/_captures/qf-handover-test/)): three receiving agents handed an
  archive built as §6 describes **all performed the setup**, including cloning an external item at its pinned
  ref. With the Problems left undisclosed, one found them, one mis-resolved one on a false claim of
  byte-identity, and one saw none.
- **Four claims in this file are narrower than they read**, including §2's *"nothing does this today"*, which
  rests on what competing tools claim in their own READMEs. [`FINAL.md`](01-research/FINAL.md) §6 lists them.

**Lesson 02's sources:** [`inventory.md`](02-personas-jtbd/6-personas/inventory.md) — the twenty questions about
people, each with its answer, data and mark; [`interviews.md`](02-personas-jtbd/6-personas/interviews.md) — the
guide and interview 1 of 5 (the guide recruits a receiver and has no question block for one);
[`re-research.md`](02-personas-jtbd/6-personas/re-research.md) — rounds 1–4 taken to the public record, with
[`_captures/`](02-personas-jtbd/6-personas/_captures/round3-log.json); and the audit,
[`personas-and-jobs-critique.md`](02-personas-jtbd/personas-and-jobs-critique.md) — 238 claims classified, 27
found invented, applied in full. The page, `personas.html`, is generated by `tools/build_personas.py`.

**Proposal lists not applied.** Stage 6's nine
([`re-research.md` §4](02-personas-jtbd/6-personas/re-research.md)), stage 7's nine
([`jtbd.md` §12](02-personas-jtbd/7-jobs-to-be-done/jtbd.md) — the shorter list, and it names the sections),
round 3's six and round 4's two are one input to the register. **Only stage 6's proposal 6, the `license` field,
is applied** (§5). One of round 3's — *an item addresses a directory, not a file* — has since been taken in the
interface (Q31, §5). **Read `jtbd.md` §12 and `re-research.md` §4 before the next change to this file.**

**Where things are.** [`FINAL.md`](01-research/FINAL.md) closes the research — start there.
[`research.md`](01-research/research.md) is a digest of it and **never a source of truth**; do not answer a
question from the digest that this file, `FINAL.md` or the register answers differently. The register,
[`research-plan.md`](01-research/research-plan.md), is the only list of open questions (§12).

**Work handed forward:** the curated public library has to be **built** — real items from checked sources,
composed so the example project produces at least one Problem and one Note. It is not a demo asset (§11).

---

## 2. What the product is

A workspace where an AI practitioner keeps their own AI building blocks — skills, agents, system prompts, MCP
servers, scripts, mini-apps — and assembles them into projects. A project is a curated set of those blocks that
exports as a ready-to-use archive.

The long-term ambition is **"GitHub / Confluence for AI people"**: store your work independently of any one
machine, keep it as a portfolio, make it public or private, reuse and recombine it across projects.

**The MVP** is a personal, single-user library plus a builder, **online** — a backend and accounts, so a person's
library follows them between machines (Q24) — **and one way out of it**: a project or an item can be **shared by
link** (§5, *Sharing*), the one place the MVP reaches somebody who is not the owner. From the ambition, *store
independently of any machine* and *public or private — as a link* are in the MVP; **the catalog and the team
stay in the ambition** (§9).

### The core value is assembly with validation, not storage

Git already stores files. What nothing does today is tell you that a skill needs a particular MCP server, that
two skills write to the same config file, that two items register the same command name, or that an env variable
is missing. Right now you find out at runtime.

### The "wow" moment

The user has said it is the **export**: a working archive in thirty seconds, with the system having checked that
the set actually holds together. Design decisions should serve that moment. Two supporting moments matter: the
**validation pass** (an animated, legible check that runs once the set is complete) and **duplicating a
project** to re-tune it for a new context.

---

## 3. Audience and platform

- Design engineers and AI engineers, 25+, who use AI heavily in daily work and have accumulated a lot of material
  they want to keep and reuse.
- **The primary persona is the collector** (Q7). Of the two candidates — the practitioner whose pain is an archive
  that lands and does not run, and the keeper of an accumulated corpus — **the corpus wins design conflicts.**
  The handover mechanisms in §6 stay as they are: not *the point*, but *the mechanism*. **The cost is recorded**:
  this is the thinner half of the evidence.
- Visually literate. They live in tools like Linear, Vercel, Raycast, Figma. The bar for craft is high; generic
  dashboard aesthetics will read as cheap.
- **Desktop-first.** Responsive/adaptive comes later, deliberately (lesson 10).
- **Dark theme from day one.** Light theme is not assumed to be free — treat it as a design decision, not a
  color inversion. Whether light ships is open (Q44, §17).

---

## 4. Vocabulary

Use these words consistently in code, design files and UI copy. The full on-screen dictionary is §14's.

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
  visibility    private | public        // public = reachable by anyone holding its link (§5, Sharing)
  shareRef                              // the unguessable part of that link. Absent unless shared
  source        inline | external       // superseded in the interface by Q32 — see "Not yet in the model"
  content                               // if inline
  repoUrl, path, ref                    // if external: repo, file, and a pinned commit/tag/version
  license                               // if external: SPDX id. Absent = no licence stated, which is not permission
  requires: [itemId]
  conflicts: [itemId]
  defersTo: [string]                    // external authorities this item yields to, declared by hand. Q10
  needsEnv: [string]                    // names only, never values
  targetPath                            // where it lands on export

Project
  id
  name
  description
  visibility    private | public
  shareRef                              // as on Item
  members: [ProjectItem]
  checkedAt                             // when the last check ran. The run itself is not stored — §6
  checkVerdict                          // counts from that check: problems, notes, skipped
  checkTarget                           // the agent target it ran against — a different one voids it

ProjectItem                             // an item's membership in one project
  itemId
  addedBy       manual | dependency     // dependency = auto-added, shows what pulled it in
  detached      boolean                 // false = live link to library, true = local override
  overrides                             // populated only when detached
```

### Not yet in the model — the interface is ahead on purpose (Q31, Q32)

The wireframes already draw two things this model does not express. **The model is not amended until they are
decided**; the register says exactly what would change.

- **An item can be a folder** (Q31). A dropped file fills `content`; a dropped folder needs an item to address a
  directory, not a file. Open: what an item's content is when it is a tree of files, where it lands (a directory
  under the target), and how the edit sheet and the detached row's diff show more than one file.
- **An item has no source switch** (Q32). It is made of **three optional parts, in any mix, at least one**:
  **Content** (written or pasted), **Files** (a file or a folder), **Repository** (cloned at a pinned `ref`, never
  vendored). Library rows read what an item is made of; the filter is *Made of*, not *Source*. What would change:
  `source` goes; content, a file list and `repoUrl · path · ref · license` become three optional parts;
  **`license` belongs to the repo part**; and `targetPath` — one destination — is open, because a mixed item may
  land in more than one place. Nothing in §6 depends on the switch: a mixed item writes its own parts as files and
  its repo as instructions in `SETUP.md`.

### The six kinds

- `skill` — a capability definition for an agent
- `agent` — an agent definition / subagent
- `prompt` — a system prompt or prompt template
- `mcp` — an MCP server
- `script` — a small script that runs as part of the setup
- `app` — a mini-app: an external tool or repo used *in the pipeline* rather than by the model (text-to-speech,
  translator, converter). Usually external, but a user may hold a local copy.

`script` and `app` are deliberately separate: a script is a file that ships inside the archive, an app is a
program the project depends on.

### Item linkage — the important one

An item lives in the library **once**. Adding it to a project creates a **live link** by default: editing the
item in the library updates every project that links to it. A user can **detach** an item inside one project and
edit it locally without touching the library or any other project.

Consequences the design must handle:

- an item card needs a "linked" vs "detached" state
- a detached item needs a visible relationship to its library original ("modified from library version"), with a
  way back
- editing a linked item communicates blast radius at three altitudes: *used in 3 projects* · **this edit
  un-checks those of them that were checked** (§6 — it voids the verdict of every checked project whose resolved
  set contains the item) · **and one of them is shared**, because sharing is live and every edit is also a
  publication (§5, *Sharing*)

**A detached item is edited inside the project.** This is what makes detaching a feature rather than a toggle: if
every edit still had to happen in the Library, *detached* would be a synonym for *unlinked*, `overrides` would
never fill, and state 6 in §7 would be decoration. The edit happens on the project's row and writes to
`overrides`, never to the library item.

**The way back is promotion, and it creates a new item.** A detached item can be promoted into the Library **as a
new item**, with the project's row re-linking to it. It is not merged into the original: that would spend blast
radius on an action taken inside one project. *Push my changes to the original* is a different action with a
different confirmation and is **not built in the MVP**. There is no prior art for a return path — Figma erases the
origin at detach — see `01-research/2-flows/05-linked-vs-detached/NOTES.md`.

**The product never shows a verdict state it is not sure of** (Q26). The product is online, so a save can fail
after the blast-radius sentence has been read. When the result is unknown, **the screen says the edit did not
land**, and the affected projects are shown **neither as checked nor as un-checked on the strength of it.** It is
§6's *a stale verdict is not shown* one step earlier. *How that is made true underneath is not decided here*
(§10).

**Deleting an item is confirmed, never refused** (Q17). A live link means a project's row depends on an item the
project does not own, and **a `requires` edge from another item may be left pointing at nothing**, which §6 then
reports as an unresolvable requirement in a set nobody touched. So the product names the consequence in the
present tense and lets the person act:

> **`db-migrate` is used in 3 projects. Deleting it may stop them working.** · **Delete** · **Cancel**

The count **expands to name the three**, as on the Library row, and the dangling-`requires` half is stated too,
because a project count does not cover it. Same discipline as an unclean export (§6) and as material coming in
(§11): **name the cost before the irreversible step. Nothing blocks.**

**Open (Q17):** a **detached** row holds its own content in `overrides`. When the library original is deleted,
**does that row survive as a local copy or go with it?** Not decided; do not invent it.

**What an item card claims, and what it never claims.** Trust in a *set* comes from the validation pass. The only
per-item evidence we show is derived from the library itself — *used in 3 projects*, *2 items require this*,
*last exported 12 days ago*. These are usage facts, not quality judgements. We ship **no score, no rating, no
eval result and no badge**: the market has converged on measured trust (Tessl scores every skill, Smithery every
server), and we have no way to run an item, so any number we invented would be decoration.

**Their ceiling is stated beside them** (Q22). **The usage facts answer *is it used*, never *is it any good*, and
must never be read as though they did.** The job underneath — *stop suspecting that half of what I keep is dead
weight* — is importance 3 for the primary persona, and this product touches it and cannot close it: an item can
sit in three projects and be useless in all three. **We run nothing, so we cannot tell.** Nothing is built on top
of the facts that would imply more.

### Public items

Some items are not the user's own. The **public library** (§8, §11) ships with the application and is
**read-only**: an item there can be added to a project or copied into `My library`, but never edited in place and
never published to. Public items are ordinary `Item`s otherwise — they carry `repoUrl`, a pinned `ref` and a
`license`. Each public item **shows its origin**, because it is someone else's work, and the pinned `ref` keeps
the shelf honest — it says *this is the version we checked*, not *this is current*. **A pin is a claim about what
was examined**; a server would not let us examine anything we have not.

**Every external item carries its licence, and a missing licence is not permission.** `license` holds an SPDX
identifier — `MIT`, `Apache-2.0` — and where a source states none, the field is **absent and shown as absent**:
*no licence stated*, never a blank row. It sits beside `repoUrl`, `path` and `ref` because it is the same kind of
fact — where this came from, and on what terms.

- **Its basis is legal, not evidential, and is stated as such.** No user asked for it and it closes no job. We
  carry other people's work inside an archive the user hands to somebody else, and **absence of a licence is
  absence of permission**. Stage 6's proposal 6, applied by the owner.
- **It is not a trust signal and must not be drawn as one.** A licence says what you may do with an item, never
  whether it is good. A licence rendered as a badge would reintroduce what the refusal of badges prevents.

### Sharing — a link to a project or to an item

A project **and** an item can each be shared by link (Q13). It was taken as a product decision: *if it matters to
the person, it is in the MVP, and how it is built comes afterwards.* It is the only route by which **the receiver
ever sees a surface of ours** rather than a file.

**A link is an unlisted address**: whoever holds it can open the thing, and nothing is listed, searched, browsed,
ranked or moderated. **It is not the public catalog §9 refuses.**

**Four properties:**

- **Both objects.** A project carries a set; an item carries one block. Both are things people hand over.
- **Live, not a snapshot.** The holder sees the thing **as it is now** — §5's live link pointed outward. **So
  sharing is a standing decision, not a single act:** every later edit is also a publication, which is the third
  altitude of the blast radius above.
- **Anyone holding the link.** No named viewers, no sign-in **for the viewer**. The owner signs in (Q24); the
  receiver does not, and never does by opening a link (§9). **The link is the credential, so it must not be
  guessable** — that is `shareRef`.
- **Revocable, and honest about what revoking cannot do.** Stopping the share kills the address. It does **not**
  reach anything anybody already copied or downloaded, and the product says so at the moment of revoking rather
  than implying a recall.

**The archive and the link say different things, and both are true.** The archive is a **snapshot**; the link is
**live**. A receiver holding last week's archive holds something the page may no longer match, so **the page
states when the project last changed** — the same honesty the pinned `ref` buys on the shelf.

**A shared item that is not the user's own carries its origin**: `repoUrl`, the pinned `ref` and the **licence**.

**On screen** (Q37, Q42, Q43): a shared project or item **reads as shared** wherever it appears — a `Shared` tag.
Its `Share…` opens **the link dialog** — `Copy link`, `Close`, and `Stop sharing…`, which opens the revoke
confirmation. `Create link` lands on the same dialog, so the link is first seen there. The drawings use a
reserved domain, `aistack.example`, because the product's own is not decided.

### Relations

`requires` and `conflicts` are filled in **manually** when adding or editing an item. Parsing metadata
automatically is out of scope (§9).

### Deference — the rule that is not ours

Q10: **where the user's own rule and an external requirement disagree, the external one wins, and the product
says so rather than resolving it silently.** It comes from one practitioner, from memory (`*`): *"My `CLAUDE.md`
says one thing, the client's linter says another, and there's no precedence anywhere."*

**`defersTo` holds the names of things this item yields to**, in the user's own words: *the client's ESLint
config*, *the repo's commit convention*, *the team's Terraform standard*. It is declared by hand, like `requires`
and `conflicts`, because §9 parses nothing and the other machine is never ours.

**What it records is precedence, and nothing else.** It is not a description of the external rule and must never
be drawn as one — we do not know what that rule says, whether it is in force, or whether it disagrees with
anything here. **It records one fact: when this item and that authority disagree, that authority wins.** The name
encodes the answer, so the field cannot quietly drift into meaning something else — do not rename it.

**We cannot detect a mismatch and must not imply that we have.** The user says *this one answers to something
outside*, and the product **carries that sentence to everybody who later acts on the item**: §6's Note, the
item's row, the shared page, and `SETUP.md`.

---

## 6. Product logic (specification)

**Dependency resolution.** Depth-first walk from the selected items along `requires`. Everything found is added
and marked auto-added. **An auto-added item cannot be removed while the item that pulled it in is still in the
project** — the product's only refusal, and a rule about the coherence of a set, not about anybody's content.

**Cycles are information, not errors.** The walk tracks three node states (untouched / in progress / done)
because it has to terminate. But a project is a **set**, not an execution order — if A requires B and B requires
A, both are added and the set is complete and correct. Report it as a fact — *"these three always travel
together"* — never as a failure.

**Conflicts and collisions.** Run the resolved set against `conflicts`. Also check for **duplicate command
names** and for items writing to the **same target path**. Each is a *Problem*. `conflicts` stays a flat
`[itemId]` list with no hard/soft flag: nothing blocks, so the distinction would have no work to do.

**Env variables.** Collect `needsEnv` across the set; missing ones are surfaced before export and written to
`.env.example`.

**Deference.** Collect `defersTo` across the set. **Each item that declares one raises a Note on its own row**
(§8): *`code-style` defers to the client's ESLint config. Where they disagree, that wins.* Nothing is compared or
detected. **This Note is cleared only by removing the declaration or the item**, because it reports a standing
property of the set, not a defect — so a set with three deferring items carries three Notes at every check. That
is intended, and it means **the note count is not a to-do list**; no surface may read it as one.

**Validation pass.** When the set is complete the user triggers a check that runs visibly — an animated sweep
across dependencies, collisions and missing keys. A designed moment, not a spinner (lesson 11). Structurally it
is a stack of stages, each with its own verdict and duration, each expandable — the model is Vercel's deployment
page, `01-research/2-flows/04-validation-check-results/NOTES-vercel.md`.

### Three severities, and nothing blocks

Every finding is one of:

- **Problem** — the archive will be wrong. A duplicate command name, a target-path collision, a declared conflict,
  an unresolvable requirement.
- **Note** — the archive is correct but incomplete. Missing env keys, an external item with no pinned `ref`, an
  item that defers to something outside the set.
- **Skipped** — the check had nothing to check. Its own neutral glyph: not a green tick it did not earn, not a red
  one it does not deserve.

**A Note is a property of one item; a Problem is a property of `requires`** (Q15). **Count the edges, not the
members.**

- **An item with an empty `requires` cannot produce a Problem**: the other three Problems need two items, and
  nothing collides with itself.
- **Any `requires` edge makes it a set question.** Resolved, the walk builds a set that collides like any other.
  **Dangling** — the far end deleted (Q17) — **the edge is itself an unresolvable requirement**, a Problem raised
  by an item whose resolved set is only itself.

**Export is never disabled.** Almost nothing makes an archive impossible to produce — a missing env key still
zips, a duplicate command still zips, it is simply wrong inside. Blocking is a choice, and we do not make it: it
is the user's own library; a permanently disabled primary action is a dead end, and on primary surfaces an action
that cannot act is not shown; and the promise is *the system checked*, not *the system forbade*.

Figma's export dialog greys `Export` beside `0 of 0 selected` and gets away with it on three conditions: the
blocker is one named action away, it is a property of this second rather than of the document, and re-doing it
costs nothing (`01-research/4-benchmark/NOTES-figma-export.md`). **A set with Problems fails two of the three** —
the fix may be four items away and it is a property of the project.

**There is exactly one exception, written down as an exception so it cannot spread** (Q16). **On a project with
nothing in it, the one control that enters `Run` is inert** — one control, because Export is Run's final stage,
not a button beside it. The rule above is about **findings**; an empty project has no findings, it has no
content. It passes both tests:

- **Figma's three conditions all hold**: put something in it is one named action, it is a property of this
  second, and re-doing it costs nothing. **Two failures out of three is the line**; any future exception has to
  clear it.
- **§9's *not shown* rule yields for the reason its own documented exception uses** — context menus grey rather
  than hide, because **stability of the surface beats brevity**. This is the screen's single primary verb;
  showing it inert teaches what a Project is for, hiding it leaves an empty room. The person pressing it on an
  empty project is asking what the product does.

**The main control reads `Export`** (Q36, Q38). It opens the mode titled `Export`; the archive is made at its last
stage, after the findings and the handover. **The check keeps its own words**: *Checking*, *Checked*,
`Check again`. On an empty project the inert control is a greyed `Export`. *If `Export` ever became a separate
control on the Project screen, that would reopen §8*, which puts Export inside Run on purpose.

**An unclean export is confirmed.** Pressing Export on a set with Problems opens a confirmation that names the
consequence in the present tense, in GitHub's mergebox register:

> Two items write to `.mcp.json`. The archive will contain only one of them — `db-tools`.

This is `terraform apply`: never refuse, always make the cost legible before the irreversible step. A grade —
Port's `Basic → Low → Good → Great` — is rejected: a ladder compares many entities against one standard, and we
check one set against itself, where there is only *coherent* or *not*.

### Sharing is disclosed, and it refuses nothing

**Nothing blocks on the way out or on the way in**: no export is refused, no share is refused, nothing coming into
the library is refused. (This is about content; the auto-added refusal above is about the coherence of a set.)

**There is no credential scan and no block on sharing.** A block would stand on detection we cannot do reliably —
it would stop the file that was fine and wave through the one that was not, and a product that refuses is
understood to have looked. GitHub's push protection, the best-resourced detector in the industry, lets the person
through on a stated reason. And content leaves by **two** exits, the archive and the link, so guarding only the
share would leave the older exit open. **The reminder lives where material comes in** (§11): the only moment the
person is looking at the file itself, the cheapest to fix, and it covers every later use.

**The moment of sharing is a disclosure moment.** Before the link exists, the product names in the present tense
what becomes visible: which items, that their **content** is visible, which env key **names** appear, which
external repos are referenced. The model is Notion's *"anyone with the link can view this page's content and see
contributor names"* — naming the second-order consequence the reader would not have thought of. *The content of
these items is visible* is the plain form of *whatever is inside them goes with them*; after the link exists it
is no longer recallable.

**The tangled case is named, not detected.** *The private and the reusable are tangled in the same files* — a
client's API shape in an example, a rule naming a client, **an env key whose own name names a customer**. We
cannot detect these and must not pretend to; they are stated as a Note at the moment of sharing.

**What the product never has.** `needsEnv` holds **names and never values**, so a shared surface **structurally
cannot leak an env value**. A property of the model, not a promise about our care.

### The receiver checks it too, and it is the same check

Whoever opens a shared link can **run the check themselves**, on the set in front of them. Every input — the walk
along `requires`, `conflicts`, command names, target paths, `needsEnv` names — is data the page already carries,
and the check reveals nothing the page was not already showing.

- **Why it is not computed quietly for them:** the validation pass is a designed moment, and the person who most
  needs it wrote none of this. And sharing is live: the owner checked on Monday, edited on Tuesday, the visitor
  arrives on Wednesday — **the only verdict worth anything is the one taken now, by the person looking at it.**
- **Before they press anything, the page states when the owner last checked and whether the set has changed
  since.** Facts, not a verdict standing in for one.
- **The ceiling and the word are identical: checked, never works.** A receiver's check answers *does this set
  cohere*, not *will this run on my machine* — whether a key exists there is a fact about a machine we never
  touch. It matters more here, because this reader has no other reassurance.
- **Nothing is stored for a visitor.** The verdict lives on a project, and a visitor owns none.

The receiver's path — open the link · read the set · check it · read what the receiving machine still needs · take
the archive — is Library-to-archive performed by somebody who owns nothing. Recorded as an observation, not as a
claim about adoption.

### The run is a moment; the project carries the verdict

**No run is stored.** Run is a surface, not a record — opening it starts a check, closing it ends one. No run id,
no run list, no history of checks, **nothing to link to afterwards**. It is §9's refusal of a second mechanism
for *what was true earlier*. **A backend does not change this** (Q24): the reason was never that we had nowhere
to put runs.

**What survives is three facts on the project**: **when** it was last checked, **what that check found** as
counts — `2 problems · 1 note · 1 skipped` — and **which agent target it ran against**. Not the findings: to see
them again you check again, which costs nothing. The counts are what you can act on and what invites the click
(`01-research/4-benchmark/NOTES-vscode.md`), and the click is a fresh check.

**The word is *checked*, never *works*.** Nothing was run: no archive opened, no server started, no agent read a
`SETUP.md`. *Works*, *valid*, *passing* and a bare green tick all promise the receiving machine, and that promise
belongs to nobody in this product.

**The verdict is void the moment the set changes, and the product says what voided it.** It is void when: an item
is added or removed · **any item in the resolved set** is edited in the library, including one pulled in by
`requires` · a `requires` or `conflicts` edge changes · `needsEnv`, a `targetPath` or a `defersTo` changes · a
detached item's `overrides` change · **the agent target changes**, because a path collision is a collision under
a target.

**Void means the verdict is not shown, and the date still is**: *checked 3 days ago, out of date since `db-tools`
was edited* — naming **what** invalidated it. Showing a stale verdict greyed out is the unearned tick this section
refuses.

**Accepted cost:** the handover disclosure is read **during** a run; re-reading it means checking again.

**Open (Q16):** `0 problems · 0 notes` reads the same on an empty set and a perfect one — whether counts are a
wide enough channel to carry a verdict is not settled.

### Export

More than a zip of files:

- inline items are placed by `targetPath`, per kind
- external items become instructions in `SETUP.md` — repo link, clone command **at the pinned `ref`**, placement
- all MCP servers merge into a single config. A key collision is checked separately, and **two items declaring
  the same server key at different `ref`s is a collision too** — one of them will not be in the exported config,
  so say which and say both refs
- missing env variables are collected into `.env.example`
- external repos are **never vendored into the archive** — they are always instructions

**`SETUP.md` is written for the agent that opens the project, not for a human reader** (Q2):

> `SETUP.md` states, **per item in the resolved set**, what that item requires — its dependencies, the MCP servers
> it needs, the env keys it expects, the external repos to clone **at their pinned `ref`**, **what it defers to**
> (§5), and where everything lands for the chosen agent target. On project init the agent reads it and performs
> the setup.

- **Why:** the loudest pain in the ecosystem is *the archive lands on a machine and does not run* — 182 reactions
  for *MCP Servers Don't Work with NVM*, over a tracker topped by PATH, node version managers and platform paths
  (`01-research/3-pain/user-pain.md`); and the benchmark found **B4 — produce an artefact and hand it over — the
  weakest flow in the industry**. Writing for an agent aims at that pain without a platform matrix and without a
  new artefact. It is also why the target selector sits where it does: the target chooses the reader.
- **Of the four places a deference is stated, `SETUP.md` is the sharpest**: it is read on the machine where the
  other rule lives, by the only reader in a position to act on it.
- **What this is not.** We run nothing on anyone else's machine, and there is **no verify script in the MVP**.
  Emitting one later must be a new stage in the run, not a rewrite of the export; design it so.

**A disclosure that could not be produced says so** (Q28). The `SETUP.md` preview, `.env.example`, the archive's
file tree and the share disclosure are **generated, not stored**, and online they can fail. A disclosure that
quietly renders short is an unearned tick delivered by omission, so **the surface names what it could not
produce**, in the present tense. It matters most for the `SETUP.md` preview, which is the whole of RJ-1 — *know
what the other side will still need, before I send it*.

**The handover is disclosed before Export, not after.** Run's last stages state what the archive contains and
what the receiving machine must still do — `SETUP.md` preview, pinned `ref`s, target-correct paths,
`.env.example` — read **before** the irreversible step.

**Agent target.** The user picks the target before exporting, and naming and paths adapt:

- `Claude Code` — `.claude/skills/`, `.claude/agents/`, `CLAUDE.md`, `.mcp.json`
- `Cursor` — `.cursor/rules`, MDC format, its own MCP config
- `Codex` — `AGENTS.md` conventions
- `Universal` — neutral structure plus `SETUP.md`; the agent adapts it later

### A single item exports on its own

An item can be exported from the Library **without a project built around it** (Q15). The project is still what
gets checked, because every Problem needs a set — but an item is not unconditionally self-contained:

- `requires`, `needsEnv`, `defersTo` and `targetPath` survive the item leaving every project, so **an agent
  target is still chosen**. An **external** item still leaves as an instruction to clone at its pinned `ref`.
- **The walk still runs.** An item that requires another **exports as a set of N items, named as one** — never as
  a bare file that will not work on arrival.
- **It enters `Run`**, the same mode, from a Library row — the third entry beside `Project` and `Shared project`.
  For a bare item most stages are `Skipped`, each on its own row (Q40).
- **Nothing is stored**: there is no project to carry a verdict.

---

## 7. Item states in the list

This is the heart of the UI. A card must read unambiguously in each state:

1. not selected
2. selected manually
3. auto-added as a dependency (showing what pulled it in)
4. conflicts with something already selected
5. selected but missing an env variable
6. **detached — locally modified inside this project**

State 6 is the easiest to forget. Figma proves how: it models overrides precisely enough to offer `Reset fill` by
name, then draws a modified instance identically to a clean one everywhere except a context menu. The diff is
already computed, so the card carries it — **and names the fields that differ**, not just the fact that some do.
Revert has two granularities, the whole item and a single field, with Reset next to Detach as the two halves of
one axis (`01-research/2-flows/05-linked-vs-detached/NOTES.md`).

**State 6 carries three commands, one axis:** **Edit** here, in the project — the only place a detached item is
editable; **Reset**, whole-item or single-field; **Promote**, which lifts the copy into the Library as a new item
and re-links this row (§5).

**All three live in the configuring mode** (Q21): they change the set, and **a row being read is not a row being
changed.** A detached row is not an exception — a viewing mode that can change the set is not a viewing mode. The
cost — one entry into configuring for a person who spotted the difference while reading — is accepted.

**No state is "blocked".** Nothing blocks (§6), so no item is ever unselectable. A conflicting item reads as
state 4, and the Problem is carried by the project, not by the card. **Both items of a declared conflict read as
state 4** (Q41): the `Conflict` mark stands on the item that declares it and on the one it names; the Problem
annotates the declaring row (§8).

---

## 8. Screens

The key flow is **assemble a set → check it → export**: **list-and-panel assembly** (Q14) and **a run-centric
check that ends in the export.** The five shapes compared, the four rejected and what each donated are in
[`01-research/5-patterns/patterns.md`](01-research/5-patterns/patterns.md); the benchmark's rubric grades craft,
not weight ([`benchmark.md`](01-research/4-benchmark/benchmark.md)).

- **Library** — the full collection: filters by kind and tag, search, the add/edit overlay, the per-item usage
  facts of §5, delete (confirmed), copy from the shelf, share an item, JSON in and out. **It is the curator's
  room** — the primary persona's own ground — **and it is not part of the builder flow**: *during building a
  project we will not open the library, there is no need* (owner). Drag is not the mechanism anywhere; it does not
  survive 300 items.

  **Two scopes, two addresses of one place**: **`My library`** and **`Public library`** — visually identical, the
  same rows, search and filters. `My library` holds the user's own items and **starts empty on first run**,
  honestly. `Public library` is a curated set that ships with the application, **read-only**: add from it into a
  project or copy into your library, never edit in place, never publish to it (§5, §11).
- **Project** — the set as a **list**, not a canvas and not a node graph: no hand-drawn edges, no execution order.
  Every row carries its own state, including *detached* with the differing fields named (§7), and **a finding
  annotates the row that owns it**. Relations come from the items and are surfaced here, not authored here.

  **Two modes.** **Viewing** is the set as it stands. **Configuring** is where it is changed — entered by one named
  action, and **the set is not editable by accident**: *adding and removing items is a thing you go into rather
  than a thing that is always available* (owner). What a project is in repose is a thing you send; changing it is
  an act you enter. **The mode is a draft** (Q33): its head reads *Cancel · Export · **Save***, so adds, removes
  and a detached row's edits are kept on `Save` and dropped on `Cancel`. `Promote` is the one immediate act inside
  it, because it creates a library item. **`Run` stays reachable from both modes** — the fix-and-recheck loop is
  the busiest path in the product (derived, not decided by the owner).

  **The library panel** is the configuring mode's own surface and the only corpus surface the builder has — a full
  left sidebar (Q33).
  - **Two levels of filter, of different kinds**: a **scope switch** above — `My library` · `Public library`,
    because that changes whose work it is and what you may do with it — and **tabs** below: `Related · All · the
    six kinds`.
  - **`Related` is first and the default**: items that require, or are required by, what is in the set. It answers
    *what belongs here*, where a typological index answers only *what exists*. **The panel opens on `All` when the
    set is empty.**
  - Search filters within the current scope and tab, and **a zero result still carries the row that creates**, so
    the first item and the thousandth arrive through the same control.
  - **The panel reads and adds. It never edits** — two renderings that can both change things drift within a
    month. **The one exception is to *where*, not *what***: the row that creates opens **the same add/edit overlay,
    summoned over the Project**, because creating is a corpus act and the person needing it is mid-assembly. That
    is the overlay's third door (after the Library row and the Library's *add*); the overlay is already the
    product's busiest disclosure surface — keys reminder, blast radius, `defersTo` — and that is thin ice.
  - **Membership is shown in the panel and owned by the row.** A row already in the set reads as checked in the
    panel. **Removal is an `✕` on the project row, in the configuring mode only, and it unchecks the panel.**
  - **An auto-added row nests under the item that pulled it in**, as a sub-row with no remove of its own — the
    nesting carries §6's refusal: *remove what dragged it in*. The panel inherits that refusal, never softens it.

  **A click on a row opens the item in a side panel beside the set** (Q33). That panel is where **`Detach`** lives,
  with the detached row's differing fields, `Reset` per field and whole, and `Promote`.

  **A new project opens in the configuring mode, the panel already open, its body only text** (Q16, Q34). The
  control into `Run` is inert until the set has something in it (§6).
- **Run** — a mode titled `Export`, entered by the **`Export`** control from a Project, by the same control on a
  **shared project**, and **from a Library row exporting a single item** (§6). It takes the whole surface: a stack
  of stages, each with its own verdict, duration and expansion, in the shape of a Vercel deployment page. The file
  tree of the future archive, the env variable list and the agent target selector live here, and **Export is the
  final stage**. Export is always live (§6); an unclean set is confirmed in the row below the finding that caused
  it.
  - **A Problem's item can be removed from Run itself** (Q34): *Remove eslint-autofix* opens **a confirmation that
    names the scope** — this project only; it stays in My library and in every other project — and on *Remove*
    **the check runs again by itself.** It is saved at once, not held as a draft.
  - **The last stages before Export are the handover**: what the archive contains and what the receiving machine
    must still do — the `SETUP.md` the agent will read, the pinned `ref`s, the target-correct paths,
    `.env.example` — stages like any other, read **before** the irreversible step.
- **Shared project** and **shared item** — **the receiving side's only surfaces** (Q13). Read-only, opened by
  anyone holding the link, built for somebody who wrote none of it: what the set contains, what each item needs,
  what the receiving machine must still have, **what any of it defers to**, the origin and licence of anything not
  the sharer's own, **the same Check the owner has** (§6), and **a way to take it** — the archive, or a copy into
  their own library — because a link that cannot be acted on is a brochure. **Run is a mode of this surface too**;
  the receiver's Run keeps two bars, the shared header over the Run bar (Q39). It is the read-only public item's
  shape pointed at one person's work.

  **The most conservative rule in the product applies here** (Q20). The shared project carries **seven jobs** in
  the coverage matrix — more than `Projects`, more than the library panel — while P2 has never spoken in the
  first person. **Invent nothing here that is not derived from what P1 needs.** Where a choice has no answer in
  P1's evidence, make the one that **shows more and promises less**, and mark it — **do not design for a person
  nobody has met.**
- **Projects** — saved projects and duplication, plus **the example project that ships on first run** (§11),
  labelled as an example. **Delete example is an ordinary, active button**, confirmed — the only way to the empty
  Projects (Q34). **Drawn as cards, not rows**, so a project is never mistaken for an item; found by **search plus
  one `Filters` button** — last check, the target it was checked for, sharing, the order (Q30). **Each card
  carries its check verdict and when**: the counts, the date, and — where the set has changed since — *what*
  changed instead of a verdict that is no longer true. Never *works*: **checked**. **A shared project reads as
  shared** here and everywhere it appears (Q37). **No visibility switch on this screen**: a project becomes
  public only by being shared (§5, *Sharing*).

### The information architecture, in one place

The work is [`03-information-architecture/sitemap.md`](03-information-architecture/sitemap.md) and
[`flows.md`](03-information-architecture/flows.md); **this is a digest and never a source of truth.**

**The top-level map — grouped by the person's own situations.**

```
0 · the door           Sign in · Create account · Reset password — the owner passes through, the receiver never does
1 · what I keep        Library — My library · Public library   ( + the Item add/edit overlay )
                       Library import / export as JSON
2 · what I assemble    Projects → Project   ( + the configuring mode, the library panel, the item side panel )
3 · what leaves        Run — a mode titled Export, entered by Export
4 · what somebody
    else opens         Shared project · Shared item
```

**Six places, and that is the whole navigable surface**: `Library` (one address per scope), `Projects`,
`Project`, `Shared project`, `Shared item`, `Sign in` (Q25 — it passes all three addressability tests).
**Everything else is a mode, an overlay, a region, a state or content** — including `Run`, which takes the whole
screen and is still not a place: nothing is stored and no address returns you to it.

**Global navigation: three entries — `My library` · `Public library` · `Projects`** (Q29). The shelf is one click
away, still one screen, read-only. `Run` has no entry: an entry pointing at a mode would promise a place nobody
can be sent to.

**The main flow:** `Projects` → a `Project` → **configure** it from the library panel until the set is complete →
**`Export`**, which enters `Run` → read the findings, fix what is fixable from its row, confirm the rest → read the
handover → **Export**. **Nothing blocks anywhere along it**, and it cannot promise the end: whether the env values
exist on the receiving machine is a fact about a machine we never touch. **Checked, never works.**

**Depth to the archive, signed in:** three taps — `Projects` → `Project` → `Export` (the control) → `Export` (the
final stage). Four when the set does not exist yet, four through the Library, **two for the receiver**. Every path
costs one more from a cold, signed-out start.

**What the panel costs.** An item **renders twice** — as a panel row and as a set row — and the panel cannot show
*detached*, *auto-added by X* or *conflicting*, which are properties of membership. **The set row is the only
place an item's state is true.** The project row — the widest thing in the product, `item · rule · observed
value` — now shares its width with the panel; that is measurable: write the longest real row and see whether it
survives. **What the old builder relied on, and where it is now:** *opening on related* is the panel's default
tab; the Library is still one step away and remembers its place, for the corpus acts; the per-item usage facts
still show what it costs to touch an item, which no pane does.

---

## 9. Deliberately out of scope for the MVP

Kept in the architecture's line of sight, not built. **Do not build these. Do not design a screen that only makes
sense once they exist.**

- **Versioning of your own items.** No history, no diffs, no rollback, **no `version` field on the item**. An item
  lives in the library once and projects link to it live, so `detached` plus `overrides` already does a version
  number's job — it is how a project says *I do not want the current one*. A second mechanism for the same thing
  is not built. **External references are pinned** — `ref`, §5. Real versioning, if ever wanted, is additive.
- **Composition — a project inside a project. Deferred, not refused** (Q3). None of the five pattern variants
  needed it, and `reuse blocks assistant` returned **0 results** in a 6,677-issue tracker of a product that
  shipped a hub for exactly this. **Composition risks unbounded recursion**: the three-state walk in §6 is for
  cycles among items, not among sets. **Decide the depth rule before the feature.**
- **A public catalog.** **A share link is in the MVP; a catalog is not** — discovery, search, ranking, a place
  where other people's work is *found* rather than *given to you*, and the moderation it requires. **A link is a
  handover; a catalog is a marketplace.**
  - **The request will not arrive wearing this word** (Q23). Stage 7 lists the same job twice: **`SJ-2` — *have
    something I would put my name to*** and **`H-J6` — *my work counts as something I can show*** (one job, do not
    count it twice). A proposal for a profile, a listing or a place where work is *visible* is this refusal tested
    in functional clothing — recognise it before weighing it. **Its importance is 1, the lowest in the base,
    established by absence**: 0 of 1,762 Hacker News comments, and a `portfolio in:title` search returning two
    unrelated issues.
  - **`visibility` is a control the user can touch** — the share — because it can act. An action that cannot act
    is not shown on a primary surface (Linear, Figma and GitHub all hide it until it has something to do). The one
    documented exception: **context menus grey rather than hide**, because a stable item order is worth more than
    a short list (finding 7, `01-research/4-benchmark/benchmark.md`).
  - **Consuming the curated public library is in the MVP; publishing to it is not.** It is read-only because **we
    curate it** — which is why an item whose licence we cannot state does not go on it — and the catalog is refused
    **on the evidence**.
- **Observability of what actually ran — refused, a different product** (Q12). *When I depend on something I
  cannot see working, I want to watch what it actually did* is importance 3 for the primary persona and the second
  main-job candidate of stage 7. **No surface touches it** — a row of twelve blanks under a 3 in the traceability
  matrix. It is refused, not deferred: we **run nothing on anybody's machine**, so any screen answering it would
  promise a runtime we do not own. **The nearest honest thing is already shipped and must not grow into a claim**:
  *last exported 12 days ago* reports what this product did, never what an agent did with the archive.
- **An account surface beyond a way in** (Q25). Accounts are in the MVP; **a profile, a settings screen and a
  session list are not** — no job raises any of them. **The door is built to the minimum**: Sign in, Create
  account, Reset password (Q35).
  - **The receiver never meets it.** The viewer stays anonymous, and **the archive branch of a shared page stays
    free of any door** — it is the branch that must always work. The only way somebody who arrived by link meets a
    sign-in is by choosing *copy into my library*, and then they are no longer a visitor. **A dead shared link
    keeps no action** — the receiver is kept off the door (Q35).
  - **A session that ends mid-work**: you return to **where you were**, nothing is re-run, nothing saved is lost.
    You return to **the place**, not into the act — configuring and `Run` are modes, and *halfway through
    assembling* is not something this product can restore, so it does not pretend to. A reload during a check
    returns to the Project and does not silently start a new check: a re-run is a choice nobody made (EJ-1).
- **Teams.** The product is online with accounts and sync (Q24), and **identity is not a team**. Still single user,
  still one workspace (§4); it follows them between machines. No job raises a second person inside one workspace.
- **Automatic metadata parsing** from item content.

---

## 10. Tech stack and conventions

- **Next.js + React + TypeScript**, chosen over Vite so that **shareable pages** (in the MVP, §5) and any later
  public page need no migration.
- **We design the interface, not the backend.** A backend exists (Q24); **what it is and how it behaves is
  deliberately not decided anywhere in this file**, nor how shared links are served. Every rule here is about
  **what a person sees and what a surface may claim**. *If a line in this file can only be satisfied by a
  particular storage design, it is written wrongly.*
- **Because the product is online, `loading` and `error` are real states on every surface**, and each is drawn
  (§15, *a screen is drawn whole*). Our failures read as ours (§14, principle 3).
- **No UI kits.** No MUI, no shadcn, no Chakra. The design system is custom and part of the product's value.
- **No Figma upstream.** Design happens in code and in the mockups we produce here.
- **Storage: a backend, and the library is reachable from any machine** (Q24). Which backend is not decided.
  IndexedDB may survive as a local cache; that is an implementation question, not a product one.
- **Archive: built in the browser (JSZip)** — a choice, not a constraint; nothing in §6 depends on where the zip
  is assembled.
- **Library portability: export/import of the whole library as JSON** (Q18). **Its warrant is that the user can
  leave with their work**: the product holds people's corpora on a server, §11 tells them to pour everything in,
  and a hosted product that says *bring it all* and offers no way out is lock-in. **Its basis is not evidential**
  — no job in the matrix raises it — and is labelled as such, the same class of decision as the `license` field.
  - **A person is never left in front of a library they cannot account for** (Q27): **either the import finished,
    or the library reads as it did before it started.** After a half-finished import the person cannot enumerate
    what arrived, so §11's keys reminder would have been given about a set nobody can inspect. *The alternative —
    show the partial import and report exactly what landed — is honest, and needs a report surface nobody has
    designed.* How it is arranged is not decided here.
- **Styling: no engine — plain CSS, written by hand** (Q45). The product is styled by
  `design-system/tokens.css` (custom properties on two levels, themes as `[data-theme]` overrides) and
  `design-system/components/` (one CSS file per component), behind one `design-system/index.css`. **No Tailwind,
  no CSS Modules, no vanilla-extract, no CSS-in-JS.** The basis is the course's purpose — understanding how tokens,
  components and themes work. Q6's criterion — tokens and two real themes first-class, no utility classes in
  components — is met and enforced by `tools/kit_check.py`. How the CSS is loaded in the app is left to the build.

---

## 11. How items get into the library

**Manually, by the user**, from their own material. `My library` starts empty on first run and fills up this way.
An empty library kills the product, because there is nothing to validate — that is cold start, answered below.

**Material coming in carries a warning about keys.** When the user brings their own files in — one item, or the
whole library as JSON (§10) — the product says before accepting them: **check that these files carry no keys.**
Two reasons: the material **leaves the person's machine the moment it is accepted**, onto a server we run; and it
**goes out in every archive built from it** and, if shared, **onto an address anyone can open** — and neither
exit is checked.

- **It is a reminder, and it says so**: *We do not read your files looking for secrets.* It must never be worded
  as though something had been scanned and come back clean, and it is **not one of §6's three severities** —
  nothing was checked, so there is no finding.
- **It does not block.** Name the consequence before the step, then let the person act. **The person who wrote
  these files is the only one who can tell a key from an example.**

**And from the public library, which ships with the application.** A curated, **read-only** set of real items —
skills, agents, prompts, MCP servers — taken from sources we have checked, reachable from the first second (§8).
The user adds from it into a project, or copies an item into `My library` and owns the copy from then on. This is
what solves cold start, and `My library` stays honestly the user's.

**A shelf guarantees material, not a first check that says anything.** Three unrelated items give six green ticks
and teach nothing. So **one example project ships too**, in Projects, built entirely from public items and
composed so it contains **at least one Problem and at least one Note** — a real target-path collision, a genuinely
missing env key. Labelled as an example, deletable, in Projects rather than in the library, because that is where
being an example is honest.

**What has to be built, and to what standard.** Real work, not a demo asset:

- **Real content from checked sources.** Placeholder lorem makes the whole product look pointless.
- **Meaningful relations** — real `requires` edges, at least one genuine `conflicts` pair, several items with
  `needsEnv`, at least two items that write to the same target path.
- **Provenance on every item**: `repoUrl`, a pinned `ref` **and the licence**, shown, not just stored. **An item
  whose licence we cannot state does not go on the shelf.**
- **Enough of it to browse rather than to read — about 30 realistic items**; the same set serves the mockups.

**How far to design it** (Q19): **build the ~30 items in full** — the content is what makes the architecture
arguable — and **design the browsing surface only as far as the example project needs**. The shelf has two ticks
in the traceability matrix and only one from an evidenced job (RJ-3, *copy it into mine to make it fixable*); the
rest is H-J4, `[?]` in all three persona columns. **A surface that keeps getting heavier without getting better
founded is where design effort goes to be wasted.** Sorting, ranking, recommending and curating are downstream of
**Q9 — what the shelf holds and how it sorts** — and none is designed before it. The only evidence so far points
to *provenance over volume*.

**Out of the library to another person: a link, in the MVP** (§5). **Into a catalog: refused** (§9).

---

## 12. Open questions

**The open ones live in one place, and it is not here.** [`01-research/research-plan.md`](01-research/research-plan.md)
ends with a register — every question with an ID, who raised it, **what would answer it**, and what it blocks.
Section 3 of [`01-research/FINAL.md`](01-research/FINAL.md) holds what was read before each early decision. **Do
not keep a second list of questions in this file** — two lists drift.

**The protocol, used by every lesson.** Questions are added to the register as work turns them up and answered in
a sitting, once the picture is whole, rather than one at a time on partial evidence. **If a lesson finds that a
section of this file has to change, it goes to the register as an entry first**, and the answer is then written
here. The model proposes; the owner decides.

**The absence rule.** Any argument of the form *we cannot, because there is no X* is only as durable as the
absence of X. **When an absence ends, every refusal that leaned on it is re-argued or dropped, in writing.**
(When the product went online, three refusals were re-argued and survived on other grounds — the run being a
moment, the catalog, *checked, never works* — and one, the first answer to Q18, was void.)

**Open now — pointers only; the register holds each in full:**

| ID | What is open | Where it bears |
|---|---|---|
| Q5 | Loss or reassembly cost — which drives adoption. Deferred, accepted risk; ask five practitioners before the first feature that pays off under only one answer. The instrument is unavailable | Positioning, not the build |
| Q9 | What the public shelf holds and how it sorts | §11 |
| Q11 | If half of what makes a setup work was never written down, what is the ceiling on validating the written part | The promise at handover |
| Q16 (half) | Whether counts are a wide enough channel for a verdict | §6 |
| Q17 (half) | Whether a detached row survives its original's deletion | §5 |
| Q31, Q32 | The model for folder and mixed items | §5 |
| Q44 | Whether light ships in the product | §17 |
| Q51 | The phase pages' orange link at about 3.5:1; lesson 07's page linking the retired `ui/kit.css` | Phase pages, not the product |
| — | The product's own domain (the drawings use `aistack.example`) | §5 |

### Decision index

Where each answered entry is written in this file. **The register is the source**; this is a map.

| ID | Decision | § |
|---|---|---|
| Q1 | Cold start is a product decision: a read-only public library and an example project ship | 8, 11 |
| Q2 | `SETUP.md` is written for the agent that opens the archive; no verify script | 6 |
| Q3 | No project inside a project in the MVP — deferred, depth rule first | 9 |
| Q4 | A detached item is edited in the project and promoted as a new item | 5, 7 |
| Q6 | Styling engine — answered by Q45 | 10 |
| Q7 | The primary persona is the collector | 3 |
| Q8 | The main job is *assemble a set that holds together*; §2 stands | 1, 2 |
| Q10 | An external requirement beats the user's own rule, and the product says so — `defersTo` | 5, 6 |
| Q12 | Observability of what ran — refused, a different product | 9 |
| Q13 | Sharing a project or an item by link is in the MVP | 5, 6, 8, 9 |
| Q14 | A library panel inside Project; the Library leaves the assembly path | 8 |
| Q15 | A single item exports on its own, the walk still running; Notes are per item, Problems per `requires` | 6 |
| Q16 | An empty project: the one control into Run is inert — the only exception | 6, 8 |
| Q17 | Deleting an item is confirmed, never refused | 5 |
| Q18 | Library JSON export/import ships; its warrant is that the user can leave | 10 |
| Q19 | The shelf is built in full and designed only as far as the example needs | 11 |
| Q20 | The shared surfaces get the most conservative treatment | 8 |
| Q21 | Edit, Reset and Promote of a detached row live in the configuring mode | 7 |
| Q22 | Usage facts carry their ceiling: *is it used*, never *is it any good* | 5 |
| Q23 | `SJ-2` stays out; it will return as `H-J6` | 9 |
| Q24 | The product is online: a backend and accounts; teams stay out | 2, 9, 10 |
| Q25 | Sign-in built to the minimum; six places; no account surface | 8, 9 |
| Q26 | The product never shows a verdict state it is not sure of | 5 |
| Q27 | A person is never left in front of a library they cannot account for | 10 |
| Q28 | A generated disclosure that could not be produced says so | 6 |
| Q29 | `Public library` is a third global entry | 8 |
| Q30 | Projects: cards, search and one `Filters` button | 8 |
| Q31, Q32 | Folder items and no source switch — in the interface only | 5 |
| Q33 | Configuring: left sidebar panel, item side panel with `Detach`, nested auto-added rows, a draft kept by `Save` | 8 |
| Q34 | Remove a Problem's item from Run, re-check by itself; a new project opens configuring; Delete example is active | 8 |
| Q35 | Independent critique of lesson 04, 23 defects fixed: the door gains Create account and Reset password; a dead shared link keeps no action; **every page the prototypes drew first is kept into the wireframes**; Delete item is drawn; `db-migrate` requires `seed-data`, one direction everywhere. The choices were proposed with the fix, not picked by the owner | 8, 9 |
| Q36, Q38 | The main control reads `Export`, no ellipsis | 6, 14 |
| Q37, Q42 | A shared project and a shared item read as shared | 5, 8 |
| Q39 | The receiver's Run keeps two bars | 8 |
| Q40 | A single item's Run keeps every Skipped stage on its own row | 6 |
| Q41 | Both items of a declared conflict read as state 4 | 7 |
| Q43 | The link of a shared thing can be had again, in one link dialog | 5 |
| Q44 | Token decisions of lesson 08 (splits, roles, recipes, one generator) | 17 |
| Q45 | No styling engine, plain CSS | 10 |
| Q46, Q47 | Primitive names: 50-step grades, one scale per theme; Tailwind v4 / Primer namespaces | 17 |
| Q48 | Lesson 09 opened; the package at `design-system/`; docs replace `kit.html` | 13, 17 |
| Q49, Q50 | States signed; light disabled ground `#ECEDE6`; the showcase on Vercel | 17 |
| Q51 | Lesson 09 closed | 1 |

---

## 13. Working agreements

- Docs, code and UI copy in English. Conversation with the user may be in Russian.
- **Lessons open and close on the owner's word**, one at a time, in the course's order (§1).
- **Every value comes from `design-system/tokens.css`**, never from a page (§15, §17). `06-concept/tokens.css` is
  the same source, written flat for the stand.
- **Do not scaffold the app before there is something for it to hold.**
- **The repo is one folder per lesson, numbered as the course numbers them**: `01-research/` · `02-personas-jtbd/`
  · `03-information-architecture/` · `04-wireframes/` · `05-tone-of-voice/` · `06-concept/` · `07-ui-assembly/` ·
  `08-design-tokens/` · `09-design-system/`, each indexed by its own `README.md`.
  - **One named exception (Q48): `design-system/` at the root** is the system's package, not a lesson's record —
    lessons 10–12 grow it and the app consumes it, so no lesson number goes into its paths.
  - **The register stays in `01-research/research-plan.md`** — every lesson writes to it.
  - **Generators** — the lesson pages, the prototypes, the mockups, the system — **live in `tools/`**; nothing
    that builds something lives only in a scratchpad.
  - **The deploy is `vercel.json` plus `.vercelignore`, a whitelist**: a new page is not served until it is listed
    there, and a moved page needs a redirect from its old address.
- **Every lesson keeps one scratch file, `PROGRESS-NN.local.md`, in its own folder** — gitignored, the
  day-by-day: what was tried, what was wrong for a day, which regressions were caught. **It is closed on the day
  the lesson is, not deleted. Nothing in one is a source of truth**, and nothing durable may live only there:
  decisions go to the register, and what they change goes here.
- **The phase pages have their own look, not the product's**: [`DESIGN-artifacts.md`](DESIGN-artifacts.md) — the
  paper ground, the orange accent, the page anatomy. **It is deliberately not named `DESIGN.md`**, so no tool
  reads it as the product's design. The product's is [`DESIGN.md`](DESIGN.md).
- **This file is the single source of truth for the product.** The original brief was folded into it and deleted;
  there is no other spec to reconcile against. Write it in the present tense; history goes to the register and to
  git, not here.

---

## 14. Voice

The product speaks by one contract, [`05-tone-of-voice/voice.md`](05-tone-of-voice/voice.md), and every line it
says is in one table, [`05-tone-of-voice/microcopy.md`](05-tone-of-voice/microcopy.md). **Any new line on any
screen is written against the first and recorded in the second**, and the second is the source of truth: *a line
on a screen and not in the table, or the reverse, is a defect.* `voice.md` extends §4 and does not compete with
it.

**The five principles, each a rule rather than an adjective:**

1. **Say what was examined, never what it means.** An inspector's report, not a seller's badge — *checked, never
   works* (§6) extended to every verdict line.
2. **Name the consequence, in the reader's terms, before the step.** No *Are you sure?*, no blocking words.
3. **Say what we did and what we did not, and own our own failures.** Our failures read *Our server didn't
   answer*; the keys reminder says it is a reminder (§11).
4. **Counts and names, not adjectives.** No score, rating or badge (§5). The count you can act on, never only
   *none*.
5. **Write for whoever acts next.** The owner, the receiver and the agent reading `SETUP.md` are three readers.
   *The receiving machine* for the owner and *your machine* for the receiver is a variant kept on purpose.

**The words that are fixed.** The person is *you*. Buttons are imperative. The product says *we* only about its
own acts. *my* appears only inside the name **`My library`**, never a bare *library*; the other place is
**`Public library`**, never *the shelf*. A project is a **project**, not *a set*; *Stack* stays off the screen. A
required item is **auto-added**, a project's own copy is **detached** from **the original**, and the archive is
**exported** (`Export` opens the mode; *Exported — x.zip*). The full list, with *not* and *why* for each entry,
is `voice.md`'s *Dictionary*. The *Forbidden* list holds clichés, cheer, motivational and selling copy,
*successfully*, exclamation marks, emoji in system messages, *Are you sure?* and internal ids.

**When copy changes, change the page and the table together, and rebuild the prototypes.** The tools are in
`tools/`: `extract_copy.py` reads every line off the pages, `build_microcopy.py` builds the table,
`rewrite_copy.py` applies a rewrite with exact occurrence counts (Q38 was applied this way, by its `stage7`).
The lesson's page, [`voice.html`](05-tone-of-voice/voice.html), is built by `tools/build_voice.py`.

---

## 15. Concept

The product looks one way, **Mica · Lime**, written down in three places that must agree:
[`06-concept/concept.md`](06-concept/concept.md) holds **every decision and its reason**,
[`design-system/tokens.css`](design-system/tokens.css) holds **every value** (`06-concept/tokens.css` is the same
values, flat, for [the stand](06-concept/concept.html)), and the stand shows them. Both `tokens.css` files are
generated by `tools/concept_tokens.py`; **no page holds a value of its own** — `python tools/concept_ui.py --check`
and the mockup build refuse a literal colour, px size or font name.

**The style in one paragraph.** A neutral **Mica** ground with a faint lime tint, quiet layers, hairlines before
shadows. **Lime `#C6EF5A`** is the only colour that invites an action — the primary button, the current place, the
active row's pill — and **never a verdict**. Findings are tinted **tags**: Problem `#FF8F98`, Note `#F2C661`;
**Checked is a quiet dot, there is no success colour** (§6). Red `--danger` only removes; amber `--warning` only
goes ahead despite a Problem. Glass (acrylic) **only around a mode or a dialog**, text always on an opaque sheet.
**Geist** and **Geist Mono**, **Lucide** icons, a 4 px spacing scale, radii 6 · 10 · 14 · 18, density between
Default and Comfortable. Every item in its own **cut-out**; no rings round rows.

**The rules:**

- **Colour is a claim.** A new colour needs an attribute or the owner's word in `concept.md`, and its contrast in
  `06-concept/contrast.md`, measured by `tools/contrast.py` on `tokens.css` as written: AA for text, 3:1 for a control's edge or a state
  mark. Every pair passes in both themes.
- **One element, one set of values**, by class, never by where it sits.
- **A screen is drawn whole**: every state, or none.
- **The wireframes stay.** Mockups are generated twins (`tools/build_mockups.py` → `04-wireframes/mockups/`) with
  the same markup and words; the viewer switches between Wireframe and Design (§16).
- **Copy still changes in one place** (§14).
- **"Оставляем" on a visual change means the system, not the screen.** When the owner says *оставляем* (*we keep
  it*) about a visual edit, it is §18 in one word: the change goes where §18's table sends it — a value to its
  token, a component to `components/` and its docs page together, a new composition to `patterns/`, markup to the
  component's specimen and every screen where it stands. **A fix on one screen is a desync**, and so is a theme
  fixed in a component.

**Left on purpose:** whether light ships (Q44, §17); responsive (lesson 10); motion — the validation pass as a
designed moment (lesson 11).

---

## 16. UI assembly

Every screen of the product is dressed in Mica · Lime as a **generated twin of its wireframe**: every page in
[`04-wireframes/mockups/`](04-wireframes/mockups/) and every step of the clickable cases in `mockups/flows/`. The
wireframes stay as they are, and the viewer's **Wireframe / Design** switch moves between the two. The pipeline
and the guards are in [`07-ui-assembly/README.md`](07-ui-assembly/README.md).

**One way in for each kind of change, so nothing drifts:**

- **A value** → `tools/concept_tokens.py` → [`design-system/tokens.css`](design-system/tokens.css), at its level,
  signed in `concept.md` (§17).
- **How a component looks** → `KIT_CSS` in `tools/build_kit.py` or `MOCK_CSS` in `tools/build_mockups.py` →
  `tools/build_components.py` → [`design-system/components/`](design-system/components/), shown on
  [the docs](design-system/docs/components.html), signed in [`DESIGN.md`](DESIGN.md).
- **What a component's docs page says** — anatomy, when to use, rule, anti-rule → `tools/docs_content.py`;
  `tools/build_docs.py` writes [`design-system/docs/`](design-system/docs/index.html) from it and from the kit's
  specimens. (`kit.html` is retired to a redirect to the docs.)
- **A composition on three screens or more** → `tools/build_patterns.py` → `design-system/patterns/`. Fewer than
  three is not a pattern; the build refuses it.
- **Structure** → the wireframe page, then rebuild everything.
- **A word** → `microcopy.md` and the page together (§14).
- **A tone the structure cannot carry** → `build_mockups.transform`: danger, warning, the one primary, state
  classes, the shell, mono for machine text, the state tile, hidden section headings.
- **A mockup is never edited by hand** — the next build overwrites it.
- **The order is fixed: the system first, the screen second** (§18).

**The guards** are `tools/kit_check.py`, run at the end of every build; a failure names its guard and points to
§18. They refuse:

- a literal value in a component; geometry written as a count of a primitive;
- a `style=` or `<style>` on a screen; a class no component defines;
- a variable `tokens.css` does not declare, including in the shell's and the docs' own styles;
- a colour primitive read by a component;
- a page linking anything but `design-system/index.css`; `kit.css` coming back; `tokens.css` or `components/` back
  in `08-design-tokens/`;
- two primaries on one screen;
- a word in a docs specimen that is not in `microcopy.md`;
- a component with no docs page; a docs page linking anything but `index.css` or reading a colour primitive;
- a pattern on fewer than three screens, or with a style or class of its own;
- an example screen with a style or class of its own, or not labelled *Example*;
- a bare `.callout` that is not a Problem — a tone is a class, never a guess from the words;
- a class in `components/` that no docs page shows; a token with no row on `docs/tokens.html`;
- in a browser, a component that looks different on its docs page and on a screen, or a meta-line link told by
  colour alone (instrument: `tools/system_check.py`; record: [`09-design-system/system-check.md`](09-design-system/system-check.md)).

**Re-runnable checks beyond the build:** `tools/kit_pixel_test.py` (goldens before a change, the same pages
after); `tools/audit07.py` (markup consistency per component, contrast measured in the browser on every text run,
images and icons, words against `microcopy.md`); `tools/contrast.py`.

**Rules the assembly settled:**

- **One primary per screen**, settled by the build, ranked: an open dialog's primary, a failure box's, the Item
  sheet's, an empty or error state's, the page head's, the item panel's, the Export stage's.
- **Our failure is neutral**, not Problem rose. So are the keys reminder and the blast radius.
- **A disabled control takes focus and points at its reason.**
- **Machine text is mono.**
- **Every state is a class**, never a guess from content.

**The record** ([`07-ui-assembly/ui/`](07-ui-assembly/ui/)): [`inventory.md`](07-ui-assembly/ui/inventory.md),
[`critique.md`](07-ui-assembly/ui/critique.md), [`review.md`](07-ui-assembly/ui/review.md),
[`audit.md`](07-ui-assembly/ui/audit.md) — each finding with a disposition.

---

## 17. Tokens

Every screen, the docs and the shell link one file, **`design-system/index.css`**, which imports
[`design-system/tokens.css`](design-system/tokens.css) (the values, on two levels) and then
[`design-system/components/index.css`](design-system/components/) (one file per component, in the kit's order).
The record of how this was built is [`08-design-tokens/`](08-design-tokens/README.md):
[the audit](08-design-tokens/tokens-audit.md) — every variable, where it is read, its role in each place — and
[the check](08-design-tokens/tokens-check.md), each finding with a disposition. The flat kit it replaced,
`07-ui-assembly/ui/kit.css`, is gone; git keeps it, last in `d6d419a`.

**The two levels:**

- **PRIMITIVE says what a value is** — colour, type, space, radius, size, motion, icons, with no roles.
  - **Names follow Tailwind v4 and Primer** (Q47): `--color-*`, `--font-sans`, `--font-mono`, `--font-weight-*`,
    `--typescale-*`, `--tracking-*`, `--space-*` (`--space-1` is 4 px, `--space-0-5` 2 px),
    `--radius-xs … --radius-full`, `--border-width-thin/thick`, `--size-*`, `--width-*`, `--measure*`,
    `--offset-*`, `--inset-*`, `--z-*`, `--icon-*`, `--ease-out`, `--duration-*`.
  - **A colour is `--color-<hue>-<grade>`** (Q46): neutral (Mica's greys — Mica is the style, not a hue), lime,
    rose, amber, red. The grade is 50, 100, 150 … from the lightest of that hue, in OKLab order.
    `--color-neutral-600` is the dark ground. **One scale per theme**: a value only light reads is
    `--color-neutral-light-50 …`. An alpha is `--color-neutral-a45`, `--color-black-a35`.
  - `06-concept/tokens.css`, the stand's flat file, keeps phase 06's names; `RENAME08` in
    `tools/concept_tokens.py` maps them, and `check08` reads the new file back through it.
- **SEMANTIC says what a colour is for** — `--ground`, `--action`, `--focus`, `--problem`.
  - Every role is a `var()` to a primitive, and its comment names the uses it grew from.
  - Washes, hovers and shadows are recipes over a role, so they follow it into any theme.
  - **Two roles are two tokens even when their value is the same today** (Q44): `--selected` and `--current`,
    `--focus` and `--mark`. In light, `--mark` and `--action` already part.

**The rules:**

- **A component reads colour only through a role, and geometry straight from a primitive.** Geometry has no
  semantic level.
- **No geometry is written as a count of a primitive** (`--space-12 * 3`); it gets a name, as `--offset-modal`
  did. The skeleton sizes are kept on purpose: they are content, measured in the scale's unit.
- **A theme overrides semantic roles and nothing else.** `:root` is dark, the product (§3).
  `[data-theme="light"]` is phase 06's signed slice, role by role, plus values signed with their reasons: the
  light glass and lighter sheet shadow; Deep Lime with a white tick for a checked control, because lime on white
  is 1.32:1; `--sheet-edge` as the light hairline; the Remove Red family keeping its dark values (Q49). **Every
  role has a light value.** `[data-theme="dark"]` repeats the dark roles so a dark subtree can stand inside a
  light page.
- **States** (Q49): pressed is one recipe per ground (`--*-active`, in the recipes block, so in both themes);
  focus is `--focus` / `--shadow-focus`, 3:1 on every ground in both themes; disabled is its three roles, never an
  opacity, and in light its ground is `#ECEDE6`, recessed under the ground (Q50). **No state moves or resizes
  anything.**
- **Whether light ships in the product is the owner's call** (Q44). Until then its switch lives in the viewer's
  toolbar (*Dark · Light*, beside *Wireframe · Design*) and on the docs — not in the product's top bar.
- **The showcase is served from Vercel** (Q50), not GitHub Pages.

**One generator per level, and each refuses what this section forbids:**

- `tools/concept_tokens.py` writes both `tokens.css` files and proves them: every role resolves to the value it
  had before; no hex appears that was not in phase 06's file; every named geometry equals the `calc()` it
  replaced; the light block holds no primitive and no hex; every role has a value in every theme. It writes the
  contrast of every pair into each theme block, and all pass.
- `tools/build_components.py` writes `components/`: every rule to its component's file, in order; every colour as
  the role its selector names; and a browser check on every page that no reordering between files lets one rule
  override another.
- `tools/kit_check.py` runs the guards (§16).

---

## 18. Contributing to the system

Read this before adding anything a screen will show. The same rule is in [`DESIGN.md`](DESIGN.md), *Contributing
to the system*, and every guard that refuses a change points back here.

**The rule is one: new appears in [`design-system/`](design-system/README.md) first, and on a screen second, never
the other way round.** A screen takes only what the system already has: its components' classes, its patterns, its
tokens. When a screen needs something the system lacks, **the work stops on the screen and moves to the system**,
and the screen is drawn after, from what the system now holds. A thing grown on a screen first and collected into
the system later is the order this section forbids, even when the result looks the same: by then two screens
disagree.

**Where each new thing enters:**

| New | Goes into | Written through | Enters together with | Refused by |
|---|---|---|---|---|
| **a value** | [`design-system/tokens.css`](design-system/tokens.css), at its level. A raw value goes in **PRIMITIVE** (`--color-<hue>-<grade>`, `--space-*`, … §17). What a colour is for goes in **SEMANTIC**, as a role with **a value in every theme** | `tools/concept_tokens.py` | the owner's signature in [`concept.md`](06-concept/concept.md); each new colour pair in `contrast_pairs()` | `concept_tokens.py`: a role resolving to the wrong value, **a role with no light value**, a pair under its bar (AA for text, 3:1 for an edge or a mark). Guards 1, 4, 5, 10 |
| **a component** | one file in [`design-system/components/`](design-system/components/) | `KIT_CSS` in `tools/build_kit.py` or `MOCK_CSS` in `tools/build_mockups.py` → `tools/build_components.py` | **its docs page**: its specimen and variants in `build_kit.components()`, its anatomy, *when to use*, rule and anti-rule in `tools/docs_content.py` (`C`). **Its states**: hover, active, focus-visible and disabled, through roles, so they hold **in both themes**, as a `STATES` spec, or the reason it has none in `STATIC`. Its look signed in `DESIGN.md` | guard 3, a class on a screen no component defines; guard 11, a component with no page; `build_docs`, a component with no entry or no states, and a state that changes nothing, or moves or resizes anything |
| **a composition** | [`design-system/patterns/`](design-system/patterns/README.md), **when it is about to stand on its third screen**. The third screen is drawn from the pattern | `tools/build_patterns.py`: an entry in `PATTERNS` with its signature, its source page, its components, *when* and *instead* | its three screens, counted by the build over every wireframe page | `build_patterns`, fewer than three screens; guard 12, a style or a class of its own |
| **a screen** | `04-wireframes/pages/`, then rebuilt into its dressed twin | `tools/build_mockups.py` | only classes, patterns and tokens the system already has; its words in `microcopy.md` (§14) | guards 2, 3, 6, 7, 8 |

**Never, anywhere:** a `style=` or a `<style>` on a screen (guard 2); a class of a screen's own (guard 3); a value
written inside a component (guard 1); a component reading a colour primitive (guard 5); a role with a value in one
theme only; a state that moves a thing or changes its size; **a generated file edited by hand** — every file in
`design-system/` and every dressed screen is generated, and the next build overwrites the edit.

**What the system lacks is written down, not drawn.** `design-system/examples/` holds screens built from the
system alone to find exactly this — [`usage.html`](design-system/examples/usage.html) for EJ-3 and
[`copies.html`](design-system/examples/copies.html) for RJ-3. If a screen needs something the system does not have and it cannot enter now —
a value nobody has signed, a component nobody has decided — it goes to
[`design-system/backlog.md`](design-system/backlog.md), and the screen does without it or waits.

**The order of one change:**

1. **Look first**: the showcase, [`design-system/docs/`](design-system/docs/index.html), and
   [the patterns](design-system/docs/patterns.html). If it is there, use it as it is.
2. **If it is not, add it to the system**, by the table above.
3. **Build:** `python -X utf8 tools/build_mockups.py`. One command rebuilds the tokens, the components, the entry
   point, the docs, the patterns and every screen, then runs the guards. A failure names its guard and this
   section.
4. **Only then the screen.**
5. **Sign:** a value in `concept.md`, a look in `DESIGN.md`, a product decision in the register (§12). **The model
   proposes and the owner signs.** No colour value is written before its signature — a light value and a pressed
   value included.

**The *оставляем* rule (§15) is this section in one word**: a value goes to its token; a component goes to
`components/` and its docs page together; a new composition goes to `patterns/`.
