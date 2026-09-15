# Sitemap — lesson 03, information architecture

> **A draft, and only its first section.** Written 2026-09-15 as the *entity inventory* — the objects a
> person actually handles in order to close a job. **No screens and no navigation are proposed here**,
> deliberately: what a place is, what is addressable and what a surface is made of come after this, in
> steps 3 to 5 of [the plan](README.md).

**Sources read in full before writing this:**
[`personas.md`](../research/6-personas/personas.md),
[`jtbd.md`](../research/7-jobs-to-be-done/jtbd.md),
[`research.md`](../research/research.md), against the specification in
[`CLAUDE.md`](../CLAUDE.md) §4–§11.

**Four marks, per [the plan](README.md).** **`§`** decided in the specification, with the section ·
**`✓`** confirmed by an instrument another person can re-run · **`*`** one practitioner, from memory ·
**`[?]`** unknown. **A structure derived from a `[?]` is itself `[?]`.**

---

## Entities

**The rule this section obeys: an object earns its place by closing a job, and the job is named with a
link.** An object that closes nothing is not here — it is in *In question* below, whatever the
specification says about it. Nothing is added because a product of this kind usually has one.

**Relation** answers one question: **whose side is this object on?** **Owner** — the keeper who builds
and keeps the material (P1, primary). **Consumer** — the receiver on the other end of the archive
(P2). **External author** — somebody who is neither, whose work we carry.

| # | Entity | Job that raises it | Relation | Standing |
|---|---|---|---|---|
| **E1** | **Item** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it) | Owner | `§`5 · `✓` |
| **E2** | **Personal library** (`My library`) | [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it) · [H-J1](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) | Owner | `§`4, §8 · job `✓`/`[?]` split |
| **E3** | **Public library** (the shelf) | [H-J4](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) | Consumer + External author | `§`8, §11 · job **`[?]` in all three columns** |
| **E4** | **Project** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act) | Owner | `§`5, §8 · `✓` |
| **E5** | **Project membership** (`ProjectItem`) | [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it) · [H-J3](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) | Owner | `§`5, §7 · `✓` + one named person |
| **E6** | **Resolved set** (§4's *Stack*) | [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act) · [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) | Owner | `§`6 · derived, never authored |
| **E7** | **Declared relation** (`requires`, `conflicts`) | [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act) | Owner | `§`5, §6 · `✓` at a **3** |
| **E8** | **Check run** | [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act) · [EJ-1](../research/7-jobs-to-be-done/jtbd.md#ej-1--not-be-quietly-overruled-by-my-own-tools) · [EJ-2](../research/7-jobs-to-be-done/jtbd.md#ej-2--believe-that-a-clean-result-was-actually-earned) | Owner | **`§`6, §8 as a surface — absent from §5 as data** |
| **E9** | **Finding** (Problem · Note · Skipped) | [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act) · [EJ-1](../research/7-jobs-to-be-done/jtbd.md#ej-1--not-be-quietly-overruled-by-my-own-tools) | Owner · **and the consumer, if S-1 is taken** | `§`6 · same gap as E8 |
| **E10** | **Env requirement** | [RJ-4](../research/7-jobs-to-be-done/jtbd.md#rj-4--move-my-work-without-moving-my-secrets-or-my-clients-business-with-it) | Both | `§`5, §6 · `✓` |
| **E11** | **Archive** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [SJ-1](../research/7-jobs-to-be-done/jtbd.md#sj-1--not-be-the-missing-manual-for-my-own-work) | Consumer | `§`6 · `✓` |
| **E12** | **`SETUP.md`** | [RJ-1](../research/7-jobs-to-be-done/jtbd.md#rj-1--know-what-the-other-side-will-still-need-before-i-send-it) · [SJ-1](../research/7-jobs-to-be-done/jtbd.md#sj-1--not-be-the-missing-manual-for-my-own-work) | **Consumer** | `§`6 · **`✓` behaviour, 3 of 3** |
| **E13** | **Agent target** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) | Consumer | `§`6 · `✓` **6,592**, the loudest thing in the base |
| **E14** | **Usage fact** | [EJ-3](../research/7-jobs-to-be-done/jtbd.md#ej-3--stop-suspecting-that-half-of-what-i-keep-is-dead-weight) · [H-J1](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) | Owner | `§`5 · `*` n = 1, **the strongest `*` in the repository** |
| **E15** | **Provenance** | [H-J4](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) · [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) | **External author** | `§`5, §11 · `✓` measured twice |

---

### E1 · Item

One reusable block. The atomic unit, and the thing every other entity is about.

- **Fields (§5).** `id` · `kind` — one of six, `skill | agent | prompt | mcp | script | app` · `name` ·
  `description` · `tags[]` · `visibility` · `source` — `inline | external` · `content` when inline ·
  `repoUrl`, `path`, `ref`, **`license`** when external · `requires[]` · `conflicts[]` · `needsEnv[]` ·
  `targetPath`. *`license` added to §5 on 2026-09-15 — see E15.*
- **Parts that are not fields.** Its **usage facts** (E14) and, when external, its **provenance**
  (E15). Both are derived or borrowed rather than authored.
- **Job.** [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) — an item is what has to keep
  working somewhere else. And [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it):
  *fix it once and have the fix reach every copy* is only possible because the item exists **once** and
  projects point at it.
- **Relation.** **Owner.** P1 writes it, keeps it, and is the only person who can edit it.
- **Standing.** `§`5. `✓` that people keep material of exactly this shape, **counted rather than
  asked**: four public trees hold **11, 25, 47 and 48 items** — *tens, not hundreds; design for fifty*
  ([research.md §7, Q-C](../research/research.md)).
- **Open, and it is the sharpest open thing in this inventory. `[?]`** Proposal **S-2** would make an
  item address **a directory, not a file** — raised because the `pdf` skill instructs the agent to read
  eight further files, so `content` held one blob, `targetPath` one destination, and the export was
  **silently incomplete**. It is not applied. Everything downstream of *what an item is made of* is
  provisional until the register sits.

### E2 · Personal library — `My library`

Everything the owner owns, across all projects.

- **Fields and parts.** **None of its own.** It is the set of every Item whose owner is the user, plus
  the axes it is read along: `kind`, `tags`, free text. §11: it **starts genuinely empty on first run**.
- **Job.** [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it)
  needs one home, or a fix has nowhere to land that reaches anything. The *finding* job —
  [H-J1](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list),
  *lay hands on something I wrote months ago* — is a **hypothesis job**, raised from `[?]` to **2** on
  2026-09-10 by one named person whose prompt library is a folder of notes in Telegram.
- **Relation.** Owner.
- **Standing.** `§`4, §8. The collection is `✓`; **the browse-and-search job behind it is the market's
  best-served flow (B1) and our thinnest evidence** — which is why nothing here may grow a mechanism
  on the strength of *libraries usually have one*.

### E3 · Public library — the shelf `[?]`

A curated, read-only set that ships with the application.

- **Fields and parts.** A set of Items, every one `source: external`, each carrying **provenance**
  (E15) that is **shown, not merely stored** (§5). Read-only: addable to a project, copyable into
  `My library`, never editable in place and never published to (§8, §11). §11 also commits to
  composition — real `requires` edges, at least one genuine `conflicts` pair, several `needsEnv`, two
  items writing to one target path.
- **Job.** [H-J4](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list)
  — *get moving with material somebody else made.*
- **Relation.** **Consumer** of somebody else's work, and **External author** for every item on it.
  The user is a consumer here and an owner everywhere else, which is the only place in this inventory
  where that flips.
- **Standing. `§`8 and §11 as a decision; the job is `[?]` in all three persona columns**, and the
  nearest observed people are against the premise: **four of five practitioners refuse other people's
  material, minimise it, or prefer their own**, and what survived is *"a few established names"* —
  **provenance over volume**. Against that, the *behaviour* is real and large: thousands of
  repositories carry verbatim copies of public skills, **32% of 446 traced copies were edited after
  import** at a median of 27 days, and **10% keep any statement of origin**.
- **Why it is in the main list anyway, said plainly.** It has a named job and the specification
  commits to it. **If the rule for this section were *a job with an evidenced importance*, this entity
  would be in *In question*.** It is marked `[?]` for that reason, and it is the entity whose structure
  must lean on nothing else.
- **Open.** §11's *checked sources* means checked for **provenance** and has **no content-review
  standard**, against **13.4% critical** in a scan of 3,984 public skills. And the shelf's **sort order
  is Q9** — unanswered.

### E4 · Project

A named set of items that exports as an archive.

- **Fields (§5).** `id` · `name` · `description` · `visibility` · `members[ProjectItem]`.
- **Job.** [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) — the project is **the unit that
  moves**; and [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act),
  because a collision is a property of a *set* and this is the set.
- **Relation.** Owner.
- **Standing.** `§`5, §8.
- **One instance is special, and it is not a second entity. `[?]`** §11 ships **one example project**,
  built entirely from public items, composed to contain **at least one Problem and at least one Note**,
  **labelled as an example and deletable**. That needs a flag on this entity and nothing more. Its job
  is H-J4 plus an onboarding argument, and §11's reasoning for it — *a shelf guarantees material, not
  that the first check says anything* — is **reasoning, not evidence**.

### E5 · Project membership — `ProjectItem`

One item's membership in one project. The entity that makes a live link a feature rather than a
sentence.

- **Fields (§5).** `itemId` · `addedBy` — `manual | dependency`, which is what lets a row say what
  pulled it in · `detached` · `overrides`, populated only when detached.
- **Parts.** `overrides` is **keyed by field**, which is what lets a row **name the fields that
  differ** rather than only that some do (§7, flow 05). Revert therefore exists at **two
  granularities** — the whole item and a single field.
- **Job.** [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it)
  — the live link is *the one mechanism in the specification that exists for exactly that job*. And
  [H-J3](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list)
  — *change one copy for one project without touching the rest* — which is `detached` and `overrides`
  named as a requirement by one person on a public forum, blocked three ways at once.
- **Relation.** Owner. It binds E4 to E1 and belongs to neither.
- **Standing.** `§`5, §7. `✓` that copies drift and stay drifted — **14% of 7,506 duplicated items out
  of sync now; 383 divergences open at a median of 121 days; four ever reconciled.** H-J3's importance
  is a **2**, raised from `[?]` on 2026-09-10.
- **Open. `[?]`** **Promotion** — a detached item lifted into the library as a *new* item, with this
  row re-linking to it (§5, §7) — **has no prior art in the survey and the thinnest demand of any
  mechanism in the specification.** It is invented rather than copied, which cuts both ways.

### E6 · Resolved set — §4's *Stack*

What a project actually is once `requires` has been walked. **Derived, never authored.**

- **Fields and parts.** The project's members, plus every item reached along `requires`, each marked
  auto-added and each carrying **what pulled it in**. Plus **cycle groups**, which §6 reports as
  information — *"these three always travel together"* — and never as a failure, because a project is
  a set and not an execution order.
- **Job.** [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act)
  — *what my pieces drag in* is literally this object. And
  [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job), because the resolved set and not the
  member list is what travels.
- **Relation.** Owner.
- **Standing.** `§`6. **`✓` that nothing on the market has this object at all**: four skill managers
  were installed and run against a deliberately broken set, and **none detected a set-level defect,
  because none has a set-level unit.**
- **Note for later, not a decision.** An auto-added item cannot be removed while the item that pulled
  it in is still in the project (§6). That is a rule about this entity, and it is the only place in the
  specification where the product refuses an action.

### E7 · Declared relation — `requires` and `conflicts`

- **Fields.** `requires: [itemId]` and `conflicts: [itemId]`, **filled in manually** when adding or
  editing an item; automatic metadata parsing is out of scope (§5, §9). `conflicts` is a **flat list
  with no hard/soft flag**, because nothing blocks and the distinction would have no work to do (§6).
- **Not a record of its own.** These are fields on E1. Listed as an entity because they are what the
  walk reads and what a finding points at, so the architecture has to give them somewhere to be seen.
- **Job.** [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act),
  **importance 3 for the primary persona** — raised from 2 on 2026-09-10, on a duplicate-collapse
  failure the vendor confirmed in public and **two people who rebuilt their tooling rather than live
  with it.**
- **Relation.** Owner declares them; **the market consensus is that nobody draws them** — not one of
  fifteen products asks a human to author a graph, so relations are *derived and filtered*, never
  drawn.
- **Standing.** `§`5, §6 · `✓`.

### E8 · Check run

One execution of the validation pass over one resolved set.

- **Fields and parts.** A **stack of stages**, each carrying its own verdict, duration and expansion
  (§6, flow 04's Vercel shape) · the findings it produced (E9) · the chosen agent target (E13) · the
  env requirements it collected (E10) · the file tree of the future archive · and **Export as the final
  stage** rather than a button beside the check (§8).
- **Job.** [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act)
  — *while I can still act* is this entity's whole reason for existing ·
  [EJ-1](../research/7-jobs-to-be-done/jtbd.md#ej-1--not-be-quietly-overruled-by-my-own-tools) ·
  [EJ-2](../research/7-jobs-to-be-done/jtbd.md#ej-2--believe-that-a-clean-result-was-actually-earned),
  which is what *Skipped* having its own neutral glyph is for.
- **Relation.** Owner — the sender runs it, and §8 puts finding-disclosure on the sender's side.
- **Standing, and the finding this inventory produced. `§`6 and §8 give this a whole surface, and §5
  has no object for it.** Whether a run has a lifetime — whether last night's check still exists this
  morning — is **`[?]`** and is not answered anywhere in the specification. **To the register at step
  9, not decided here.**

### E9 · Finding — Problem · Note · Skipped

One thing the check has to say.

- **Fields and parts.** Its **severity**, one of three (§6) · **what it is about** — which items, or
  the set · the sentence that names **what was required and what was found**, at the altitude that
  knows the rule · and for a Problem, **the consequence in the present tense** — *"Two items write to
  `.mcp.json`. The archive will contain only one of them — `db-tools`."*
- **Job.** [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act)
  and [EJ-1](../research/7-jobs-to-be-done/jtbd.md#ej-1--not-be-quietly-overruled-by-my-own-tools):
  *not be quietly overruled* is closed by naming the choice, never by refusing it.
- **Relation.** Owner today. **And the consumer, if proposal S-1 is taken** — three receiving agents
  were handed a set whose Problems the document did not name, and **one mis-resolved a defect on a
  false claim of byte-identity and one saw none.** *The disclosure the sender gets before Export is the
  disclosure the receiver turns out to need.* Not applied.
- **Standing.** `§`6. **Not in §5, like E8.** And one structural fact the architecture must carry: §8
  says a finding annotates **the row that owns it**, but a missing env key and a merge collision are
  properties of **the set** and own no row.

### E10 · Env requirement

A named key the set needs and does not carry.

- **Fields and parts.** The key's **name**, from `needsEnv[]` on each item (§5) · which items in the
  resolved set ask for it · whether it is satisfied. **`needsEnv` is a list of strings: the product
  stores names and never values**, which is a property of the model rather than a policy anybody wrote
  down. Collected across the set and written to **`.env.example`** before export (§6).
- **Job.** [RJ-4](../research/7-jobs-to-be-done/jtbd.md#rj-4--move-my-work-without-moving-my-secrets-or-my-clients-business-with-it)
  — *move the work without moving the secrets.*
- **Relation.** **Both.** The owner declares the need; **the receiver is the one who has to fill it**,
  and `.env.example` is an instruction to go and find a value.
- **Standing.** `§`5, §6 · **`✓`, the largest crowd on a fear after the multi-target family** — 192,
  54, 45, 32, 23, 22 across three trackers. Importance **2** for P1, because the one practitioner on
  record has never spent the *"couple of hours"* to separate the private from the reusable, and **2**
  for P2 on behaviour: four receivers were watched stripping the author's credentials out of inherited
  material.
- **Open. `[?]`** Proposal **S-4**: a receiving agent, told only to set the project up, **read the
  machine's live OAuth token out of the keyring and wrote it into a plaintext file.** The risk runs
  both ways and the specification names only one of them.

### E11 · Archive

What a project becomes. The product's stated wow moment (§2).

- **Parts (§6).** Inline items placed by `targetPath`, per kind · external items as **instructions,
  never vendored** · **all MCP servers merged into one config**, where a key collision is a Problem and
  **two items declaring the same key at different `ref`s is a collision too** · **`.env.example`** ·
  **`SETUP.md`** (E12) · everything named for the chosen **agent target** (E13).
- **Job.** [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) — this is the move ·
  [SJ-1](../research/7-jobs-to-be-done/jtbd.md#sj-1--not-be-the-missing-manual-for-my-own-work).
- **Relation.** **Consumer.** It is the only thing in this inventory that leaves the owner's machine,
  and every decision about it is a decision about somebody else's first hour.
- **Standing.** `§`6 · `✓` that the need is unserved — **B4 is the weakest flow in the industry,
  nobody above 4.**
- **Open. `[?]`** Proposal **S-3**: a `settings.json` that wins a collision can **declare a
  third-party plugin marketplace and enable a plugin from it**, so an archive can reconfigure the
  receiving agent before setup begins. §6 lists what export produces and does not say that some items
  are executable.

### E12 · `SETUP.md`

The handover document, **addressed to the agent that opens the project** and not to a human reader.

- **Fields and parts (§6).** **Per item in the resolved set**: its dependencies, the MCP servers it
  needs, the env keys it expects, the external repos to clone **at their pinned `ref`**, and where
  everything lands for the chosen target.
- **Job.** [RJ-1](../research/7-jobs-to-be-done/jtbd.md#rj-1--know-what-the-other-side-will-still-need-before-i-send-it)
  and [SJ-1](../research/7-jobs-to-be-done/jtbd.md#sj-1--not-be-the-missing-manual-for-my-own-work)
  — *not be the missing manual for my own work.*
- **Relation.** **Consumer, and it is the only entity here whose reader is not the owner.** That
  matters more than it reads: **no receiver has ever spoken in the first person** in five venues and
  four rounds, so this document is designed for a person nobody has interviewed.
- **Standing. The best-evidenced object in this inventory, and the evidence is behaviour rather than
  opinion.** `✓` **three receiving agents out of three performed the setup from it**, including cloning
  an external item at its pinned `ref`. Also `✓`, in the other direction: **30 of 214 receivers wrote
  21,266 lines** of setup and handover manual the sender never shipped — `HANDOFF.md` at 229 lines as a
  fork's only commit, a `SETUP.md` at 425.
- **Open.** **S-1** — it should carry the set's **Problems**, not only its requirements. **The largest
  proposal any round has made.**

### E13 · Agent target

`Claude Code` · `Cursor` · `Codex` · `Universal`.

- **Fields and parts.** An enumerated choice that selects paths, naming and file formats — and, since
  §6 made `SETUP.md` an agent's document, **it also selects the reader**.
- **Not a record in §5.** It is a choice made before export. **Where it lives — on the project, on the
  run, or nowhere but the moment — is `[?]`** and is a question for step 3, not for this section.
- **Job.** [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job). *A second tool* is the first
  clause of the main job.
- **Relation.** Consumer — it describes the receiving environment; the owner chooses it.
- **Standing.** `§`6 · **`✓` and it is the loudest demand in the entire evidence base**: **6,592
  reactions** on *one instruction source across several agents*, plus a counted per-person figure —
  public trees configuring **three and four** distinct tools.

### E14 · Usage fact

The only per-item evidence the product ships. **Derived from the library, never from running anything.**

- **Parts (§5).** *used in 3 projects* · *2 items require this* · *last exported 12 days ago*. And what
  it is **not**: no score, no rating, no eval result, no badge — the market converged on **measured**
  trust and we can measure nothing, so any number we invented would be decoration.
- **Job.** [EJ-3](../research/7-jobs-to-be-done/jtbd.md#ej-3--stop-suspecting-that-half-of-what-i-keep-is-dead-weight)
  — partially, and the limit is worth stating: usage facts answer *is it used*, **not *did it change
  anything***. EJ-3 scores **3** for the primary persona and **the product cannot close it**; that is
  **Q12**. Also [H-J1](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list).
- **Relation.** Owner.
- **Standing.** `§`5 · **`*`, n = 1, and the strongest `*` in the repository**: asked with our
  vocabulary deliberately forbidden, a practitioner invented this mechanism unprompted — *"Usage data,
  first… that alone would let me delete half of it with confidence"* — then extended it past our spec
  to **last actually useful** and **counted per session**. **Both extensions need a runtime we do not
  have**, so they are recorded and not promised.

### E15 · Provenance

Where a piece of somebody else's work came from.

- **Fields (§5).** `repoUrl` · `path` · **`ref`, pinned** — *this is the version we checked*, not
  *this is current*, which is what keeps a shelf with no server behind it honest · **`license`, an
  SPDX identifier, added 2026-09-15**. §11: **shown, not just stored.**
- **Job.** [H-J4](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list)
  `[?]` for the shelf, and [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) for the pin: an
  external item travels as an instruction to clone **at a named ref**.
- **Relation.** **External author.** The only relation in this inventory pointing at somebody who is
  neither the owner nor the receiver.
- **Standing.** `§`5, §11 · **`✓` twice, and they pull the same way.** Provenance **does not survive a
  copy** — only **10% of 446** traced copies name their origin anywhere — and a pinned ref **did real
  work in front of us**: in the handover test the receiving agent used the pins to fetch back **both
  items the archive had silently lost to collisions.** So the thing is scarce *and* load-bearing.
- **The licence — added 2026-09-15, and it is the one part of this inventory with no job under it.**
  `license` holds an SPDX identifier, and **absence is shown as absence** — *no licence stated*, never
  a blank row — because **a missing licence is not permission but the lack of it**. Stage 6's proposal
  6, applied by the owner ahead of the register's sitting.
  **Read what basis it has, since this file's own rule is that an object earns its place by closing a
  job.** This one does not: nobody has asked for it, and it is not here because a persona needs it. It
  is here because **we carry other people's work inside an archive the user then hands on**, which is a
  legal constraint rather than a job — a different kind of reason, and the file says so rather than
  inventing a job to cover it. §5 also fixes what it may not become: **a licence is not a trust signal
  and must not be drawn as a badge**, or the refusal of scores comes back through the side door.
- **Still open. `[?]`** **Whether a user's own external item with no stated licence produces a Note**
  — the same shape §6 already gives *an external item with no pinned `ref`*. **Not decided, and
  deliberately not taken here**: it would create a finding, and a new finding changes what the
  validation pass claims. §11 covers the shelf by a build standard instead — an item whose licence we
  cannot state does not ship on it.

---

## In question — objects with no job behind them

**Nothing here is proposed.** Each row is either vocabulary that is not an object, a field the
specification keeps for a reason other than a job, or a thing the architecture will be tempted to
invent. **They are listed so that the temptation is visible** rather than acted on in step 3.

| # | Candidate | Why it is not in the main list | What would move it |
|---|---|---|---|
| **Q-E1** | **Workspace** (§4) | **No job requires it.** One per user, not a team concept, and §9 refuses accounts, sync and teams — so nothing can ever be inside it except everything. It is a word for *all of this*, not an object with parts | A second workspace, which §9 forbids |
| **Q-E2** | **Stack** (§4) | **Not a second entity.** §4 calls it the *informal* name for the resolved set, which is **E6**. Two names for one object is how a vocabulary drifts | Nothing. Prefer *resolved set* in structure, keep *stack* as speech |
| **Q-E3** | **Tag** | A **field on E1**, not an object. The only job that touches it is H-J1, whose importance is a **2** on one person — and nothing anybody has said requires tags to have a life of their own (rename, merge, describe, own a colour) | Somebody asked to manage tags rather than to use them |
| **Q-E4** | **`visibility`** | **§9 keeps the field and does not show the control at all**, because there is no server to publish to. The only job behind it is [SJ-2](../research/7-jobs-to-be-done/jtbd.md#sj-2--have-something-i-would-put-my-name-to--post-mvp), scored **1** for the primary persona and **post-MVP** | A server, and a register decision |
| ~~**Q-E5**~~ | ~~**Licence of an external item** `[?]`~~ | ~~**Proposed, not applied** (stage 6 proposal 6). It closes no job — it is a legal constraint on shipping E3, which is a different kind of reason~~ **Left this table on 2026-09-15: the owner applied it.** It is now a field of **E15**, and the reason it was refused here is still true — **it closes no job**, and §5 now says so in those words rather than acquiring one | — |
| **Q-E6** | **A profile of the receiving machine** | **RJ-1 wants the *knowledge*, and the specification answers it with E12 rather than with an object.** RJ-1's importance for the primary is **`[?]`** — the cell was withdrawn by the audit, then hunted deliberately with six queries across two forums and **nobody says they wished they had known.** The market has such a surface (`asm doctor`); we do not need the object to close the job | One practitioner saying it plainly — which would also move RJ-1 into the core |
| **Q-E7** | **An external requirement** — a client's linter, a repo convention | The conflict a practitioner actually described is with something **outside the set**, and §5 has nowhere to put it. That is **Q10**, live and standing on one person. **No object until the question is answered** | Q10 answered |
| **Q-E8** | **An execution record** — what actually ran, per session | This is the highest-importance job the product **cannot** close: EJ-3 / H-J5 score **3** for the primary and **§6 runs nothing on anyone's machine.** An object here would be a promise we cannot keep. **This is Q12, and it is a positioning question rather than a backlog item** | A different product. Named here so nobody adds it later as *just a log* |
| **Q-E9** | **Version or history of an own item** | **§9 refuses it**, and `detached` + `overrides` (E5) already does the job a version number would. One datum against the refusal is recorded — **151 reactions** asking for history and rollback, from an organisation context — and the disposition is the owner's | The register |
| **Q-E10** | **A project inside a project** | **§9 defers it over unbounded recursion**, and no pattern variant needed it. Decide the depth rule before the feature, not after | Post-MVP, with a depth rule first |
| **Q-E11** | **A folder or collection inside the library** | **Nobody has asked for one.** The find job is served by six kinds, tags and search; a tree is the object an information architecture invents when it is uncomfortable with a flat list of fifty things. **Fifty is the counted band** | Somebody asked |

---

## What this section establishes, and what it does not

**Establishes.** **Fifteen entities, each with a job and a link to it**, and **eleven candidates
refused for a stated reason — of which one, the licence, was promoted on 2026-09-15 by an owner's
decision rather than by evidence, and is recorded as such in both places.** Three relations, not one: most of this product belongs to its owner,
**three entities exist for the receiver** — the archive, `SETUP.md` and the agent target — and **one
points at an external author**.

**And two findings that were not visible before the objects were laid out side by side:**

1. **§5 has no object for the check or for a finding**, and §8 gives the check an entire surface. E8
   and E9 are specified as behaviour and absent as data, so *does a run persist* has no answer
   anywhere. **To the register at step 9.**
2. **The best-evidenced entity in the product is the one built for the persona nobody has ever
   interviewed.** `SETUP.md` has `✓` behaviour under it — three of three, and 30 of 214 receivers
   writing the manual themselves — while every *account* of the receiving end is written by a sender.

**Does not establish.** Anything about places, screens, routes or navigation — **none of that is in
this file yet, by instruction.** Nor the shape of E1, which proposal **S-2** would change from a file
to a directory, and which the sitting has not decided.
