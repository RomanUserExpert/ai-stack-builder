# Sitemap — lesson 03, information architecture

> **A draft, in three sections.** Written 2026-09-15. It decides nothing on implementation grounds:
> what the product is comes first, and how it is built comes after — a rule this file had to be
> corrected against once already, see *The screen P2 would have*. **Entities** — the objects a person handles in order to close a
> job. **Screens** — derived from those objects and from the jobs, never from anybody's product.
> **Places, modes, overlays and states** — what kind of thing each node actually is, which is where
> *four places* comes from. **Routes are still not here**: naming them is step 3, and it now has a
> shape to put them on.

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
| **E16** | **Shared link** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [SJ-1](../research/7-jobs-to-be-done/jtbd.md#sj-1--not-be-the-missing-manual-for-my-own-work) | **Consumer** | `§`5, §8, §9 · **a decision, not a finding** |
| **E15** | **Provenance** | [H-J4](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) · [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) | **External author** | `§`5, §11 · `✓` measured twice |

---

### E16 · Shared link — added 2026-09-15

The address that makes a project or an item reachable by somebody who is not its owner.

- **Fields (§5).** `visibility` — the standing decision — and `shareRef`, the unguessable part of the
  address. **Absent unless shared**, on both `Item` and `Project`.
- **Job.** [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) — it is a way for the work to
  live somewhere else · [SJ-1](../research/7-jobs-to-be-done/jtbd.md#sj-1--not-be-the-missing-manual-for-my-own-work),
  because the page states what the receiver needs and is therefore the manual the sender otherwise has
  to be · and [RJ-1](../research/7-jobs-to-be-done/jtbd.md#rj-1--know-what-the-other-side-will-still-need-before-i-send-it)
  on the sending side.
- **Relation.** **Consumer**, and it is the first object in this inventory that **gives the consumer a
  surface of ours** rather than a file.
- **Standing.** `§`5, `§`8, `§`9 — **a product decision taken on 2026-09-15 with the evidence against
  it recorded**: no observed person has asked for a link, handover in practice is git and files, and
  [SJ-2](../research/7-jobs-to-be-done/jtbd.md#sj-2--have-something-i-would-put-my-name-to--post-mvp)
  scores **1**. It is in because the owner judged it part of the base, and the register says so in
  those words.
- **Three properties with consequences.** **Live** — so sharing is a standing decision and every later
  edit is a publication. **Anyone holding it** — so the link is the credential. **Revocable, and
  revoking recalls nothing** already taken, which the product must say rather than imply otherwise.

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

- **Fields (§5).** `id` · `name` · `description` · `visibility` · `members[ProjectItem]` ·
  **`checkedAt`, `checkVerdict`, `checkTarget`** — added 2026-09-15, when the run was decided to be a
  moment. The project is where a check leaves its trace, because **the run leaves none of its own**
  (E8).
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
  has no object for it** — no `id`, no fields, nothing that says a run is a thing rather than a moment.
- **Answered 2026-09-15, and the answer is *a moment*.** `§`6 now says it: no run is stored, no run
  id, no run list, no history, **nothing to link to afterwards** — opening Run starts a check and
  closing it ends one. So **E8 is not an entity with a lifetime**; it is the surface on which a check
  happens, and the only thing it leaves behind lands on **E4**: `checkedAt`, `checkVerdict` as counts,
  and `checkTarget`.
- **Three consequences the architecture has to carry.** A finished run has **no address** — whatever
  Run turns out to be in step 3, it is not a place you can be sent to and find yesterday's result.
  **The handover disclosure is read during a run**, because there is no run to re-open; re-reading it
  means checking again, which costs nothing since we run nothing. And the **Vercel shape §6 borrows is
  a history** — we take its stage list and deliberately not its persistence, which is a thing to know
  while drawing it rather than to discover afterwards.
- **And the verdict is void the moment the set changes**, which makes invalidation a structural fact
  rather than a detail: editing one library item **un-checks every project whose resolved set contains
  it**, including projects that never named it, because `requires` pulled it in. That is §5's blast
  radius with a consequence attached.

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
- **Standing.** `§`6. **Not in §5, and since 2026-09-15 that is a decision rather than a gap**:
  findings live as long as the run that produced them. What survives on the project is **their
  counts** — `2 problems · 1 note · 1 skipped` — never the findings themselves; to read one again you
  check again. And one structural fact the architecture must carry: §8
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
| **Q-E4** | **`visibility`** | **§9 keeps the field and does not show the control at all.** *Its stated reason — that there is nothing to publish to — is the same kind of reason struck on 2026-09-15, so it is under review with **Q13**.* The job behind it is [SJ-2](../research/7-jobs-to-be-done/jtbd.md#sj-2--have-something-i-would-put-my-name-to--post-mvp), scored **1** for the primary persona | **Q13.** If a link is in the MVP, this control can act, and §9 hid it precisely because it could not |
| ~~**Q-E5**~~ | ~~**Licence of an external item** `[?]`~~ | ~~**Proposed, not applied** (stage 6 proposal 6). It closes no job — it is a legal constraint on shipping E3, which is a different kind of reason~~ **Left this table on 2026-09-15: the owner applied it.** It is now a field of **E15**, and the reason it was refused here is still true — **it closes no job**, and §5 now says so in those words rather than acquiring one | — |
| **Q-E6** | **A profile of the receiving machine** | **RJ-1 wants the *knowledge*, and the specification answers it with E12 rather than with an object.** RJ-1's importance for the primary is **`[?]`** — the cell was withdrawn by the audit, then hunted deliberately with six queries across two forums and **nobody says they wished they had known.** The market has such a surface (`asm doctor`); we do not need the object to close the job | One practitioner saying it plainly — which would also move RJ-1 into the core |
| ~~**Q-E7**~~ | **An external requirement** — a client's linter, a repo convention | ~~That is **Q10**, live and standing on one person. **No object until the question is answered**~~ **Q10 was answered on 2026-09-15: the external requirement wins, and the product must say when it disagrees.** So an object *is* wanted — **a declared external constraint on an item**, hand-filled the way `requires` and `conflicts` are. **It is not in §5 yet**, and the reason it is still in this table is that detection is impossible in the MVP: §9 parses nothing and we never see the other machine, so what is buildable is **disclosure of a constraint the user declared**, never a comparison | The field, once §5 and §6 carry it |
| **Q-E8** | **An execution record** — what actually ran, per session | This is the highest-importance job the product **cannot** close: EJ-3 / H-J5 score **3** for the primary and **§6 runs nothing on anyone's machine.** An object here would be a promise we cannot keep. **This is Q12, and it is a positioning question rather than a backlog item** | A different product. Named here so nobody adds it later as *just a log* |
| **Q-E9** | **Version or history of an own item** | **§9 refuses it**, and `detached` + `overrides` (E5) already does the job a version number would. One datum against the refusal is recorded — **151 reactions** asking for history and rollback, from an organisation context — and the disposition is the owner's | The register |
| **Q-E10** | **A project inside a project** | **§9 defers it over unbounded recursion**, and no pattern variant needed it. Decide the depth rule before the feature, not after | Post-MVP, with a depth rule first |
| **Q-E11** | **A folder or collection inside the library** | **Nobody has asked for one.** The find job is served by six kinds, tags and search; a tree is the object an information architecture invents when it is uncomfortable with a flat list of fifty things. **Fifty is the counted band** | Somebody asked |

---

---

## Screens — the draft tree

> **Written 2026-09-15, after the entity inventory and from it.** Derived from **what the person is
> trying to get done**, not from anybody's product. No competitor's sitemap was opened while writing
> it; the flows in [`2-flows/`](../research/2-flows/README.md) are captured mechanisms and were read as
> mechanisms, never as structures to copy.

**Depth is deliberately shallow.** Three levels, no more. Levels are added on purpose in step 3, when
routes and addressability are decided — a tree that grows depth before it has a reason is how an
information architecture acquires places nobody asked for.

**A screen is not a state.** Empty, loading, filtered-to-zero, mid-check and error are **states** of a
screen. They are listed under *What is not a screen* below and they will be composed in step 5.

**Every screen carries the job it serves, or it is marked `[orphan]`.** An orphan is not a mistake to
delete on sight — it is a screen the specification wants and the jobs do not raise, and saying so is
the point of the mark.

### The tree

```
1 · WHAT I KEEP  — the corpus I have accumulated
  │
  ├── Library ......................................... [H-J1] [RJ-3]
  │     two scopes, one screen: My library · Public library  [H-J4 ?]
  │     │
  │     └── Item .................................... [RJ-3] [EJ-3 partly]
  │
  └── Library import / export (whole library as JSON) . [orphan]

2 · WHAT I AM PUTTING TOGETHER  — the set for one piece of work
  │
  └── Projects ........................................ [MAIN] [H-J2 ?]
        │
        └── Project ................................... [MAIN] [RJ-2]
              │
              └── Detached row — edit, reset, promote .. [H-J3]

3 · WHAT LEAVES  — the thing that has to work somewhere else
  │
  └── Run ............................................. [MAIN] [RJ-2] [RJ-1] [RJ-4] [SJ-1]
        entered by Check, from a Project. Ends in Export.

4 · WHAT SOMEBODY ELSE OPENS  — the receiver's only surfaces
  │
  ├── Shared project .................................. [MAIN] [RJ-1] [SJ-1]
  └── Shared item ..................................... [MAIN] [H-J4 ?]
        read-only, opened by anyone holding the link, and each offers
        a way to take it — the archive, or a copy into their own library
```

**Five screens and one orphan.** The three groups are the person's own three situations, in the order
[`personas.md`](../research/6-personas/personas.md) records them: *copying something out of the
collection into a new project · adding a rule right after an agent did something annoying · hunting
for something they know they wrote.* They are not navigation sections and should not become a menu in
step 3 — they are why the screens exist.

### Each screen, its job, and what the person came to do

| Screen | Job it serves | What the person arrived to do | Persona |
|---|---|---|---|
| **Library** | [H-J1](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) · [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it) | *Lay hands on the thing I know I wrote* — and reach the one copy that a fix has to land on | **P1** · P3 in its public scope `[?]` |
| **Item** | [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it) · [EJ-3](../research/7-jobs-to-be-done/jtbd.md#ej-3--stop-suspecting-that-half-of-what-i-keep-is-dead-weight) partly | *Fix this once*, and see who else it reaches before touching it | **P1** |
| **Projects** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [H-J2](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) `[?]` | *Get back to the set I keep for that piece of work* — and see whether it is still checked | **P1** · P3 for the example `[?]` |
| **Project** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act) | *Put the set together and see what it drags in* — every row carrying its own state | **P1** |
| **Detached row** — edit · reset · promote | [H-J3](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) | *Change it here only, without the others getting it* | **P1** |
| **Run** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act) · [RJ-1](../research/7-jobs-to-be-done/jtbd.md#rj-1--know-what-the-other-side-will-still-need-before-i-send-it) · [RJ-4](../research/7-jobs-to-be-done/jtbd.md#rj-4--move-my-work-without-moving-my-secrets-or-my-clients-business-with-it) · [SJ-1](../research/7-jobs-to-be-done/jtbd.md#sj-1--not-be-the-missing-manual-for-my-own-work) | *Find out whether it holds together, see what the other side still needs, and get the archive out* | **P1** |
| **Shared project** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [RJ-1](../research/7-jobs-to-be-done/jtbd.md#rj-1--know-what-the-other-side-will-still-need-before-i-send-it) · [SJ-1](../research/7-jobs-to-be-done/jtbd.md#sj-1--not-be-the-missing-manual-for-my-own-work) | *Somebody sent me this — what is it, what do I still need, and how do I take it* | **P2**, and it is their only surface |
| **Shared item** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [H-J4](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) `[?]` | *Somebody sent me one block — what is it, whose is it, may I use it* | **P2** · P3 `[?]` |
| **Library import / export** | **`[orphan]`** | — | — |

**The orphan, named rather than quietly dropped.** `CLAUDE.md` §10 commits to **export and import of
the whole library as JSON**, *"which covers both backup and informal sharing before any server
exists"*. **No job in the matrix raises it.** Backup appears nowhere in the evidence — nobody has said
they lost a corpus — and *informal sharing* is the transfer family's wording for something the archive
already does. It is kept in the tree **because the specification wants it and because naming an orphan
is cheaper than discovering one at step 5**; whether it is a screen at all, or two commands living on
the Library, is exactly the kind of thing step 2b decides.

### Which screens each persona needs

| | Screens | Reading |
|---|---|---|
| **P1 — the keeper of a corpus** · **primary** | **All five**, and Library and Item carry more weight than they did before 2026-09-15 | Q7 named the collector primary, so the corpus screens stop being the place you pass through on the way to Run. **The cost is on the record**: the collector's own job is the thinnest evidence in the folder |
| **P2 — the receiver** · secondary | **Two, as of 2026-09-15: the shared project and the shared item** — plus `SETUP.md` inside the archive, which is not a screen | **The finding changed the same day it was written.** It read *the receiver needs no screen at all*; **Q13 answered yes to a link**, and P2 now has exactly the two surfaces a link can lead to. **What has not changed is the hard part:** they are still designed for a person who, in five venues and four rounds, **has never spoken in the first person** — so these two screens are the most `[?]`-laden places in the product, and the archive must still be complete on its own, because whoever gets the link may only ever get the file |
| **P3 — the empty-handed** · secondary `[?]` | **No screen of their own**: Library in its **Public** scope, and Projects for the **example project** | Nothing is built only for P3, and that is deliberate. The persona has never been observed, and the two clearest public beginners wrote their own material or asked to shadow a human rather than reach for a shelf. **A screen built only for them would be a place invented for somebody nobody has met** |

### The screen P2 has — **answered 2026-09-15, and the reasoning was corrected on the way**

> **Written, corrected and answered in one day, and the sequence is left visible.** This block first
> argued that a shared link is out of the MVP, and **two of its three reasons were about
> implementation** — there is no server, storage is one browser. **That is not a reason; both are
> struck.** The product decides what it is and the implementation follows. The question that survived
> became **Q13**, and **the owner answered it: yes.** A link to a project **and** to an item, **live**,
> openable by **anyone holding it**.

**So the receiver has two surfaces**, and they are the only places in this product built for somebody
who wrote none of it. What follows is the evidence as it stood when the decision was taken — recorded
in full, including the half that argues the other way, because the decision was made on product
judgement rather than on a finding.

~~**There is nothing to put behind a URL.** Storage is IndexedDB and there is no backend (§10)~~ —
**struck: an implementation fact, standing in for an argument it cannot make.**

**What the evidence actually says, in both directions, because it does not point one way:**

- **The job is the loudest thing in the base, and it is not about a link.** 6,592 reactions for one
  source across several agents, 182 for an archive that lands and does not run. **The job is
  transfer; the link is one mechanism for it, and the archive is another.**
- **Nobody observed asks us for a link.** Handover in the largest sample of practice is `chezmoi`,
  symlinks, CLI installers, bootstrap scripts, git and forks. **`SJ-2` — the one job about being seen
  — scores 1 for the primary persona**, on an absence looked for twice: **0 of 1,762** Hacker News
  comments mention a portfolio.
- **And the market's answer to distributing a *set* is a paid tier** — *"wrap the skill as a plugin in
  the Team Marketplace and mark it as Required so it installs for everyone automatically… only
  available on Teams/Enterprise"*, answered with *"Huge unlock."* That says distribution is worth money
  to somebody. It does not say our person wants a link from us.
- **The strongest argument for it is not in the evidence at all, and should be said out loud.** An
  archive is a **file**, and a file still needs a channel — mail, git, a chat. **A link removes that
  step**, and it is the only route by which **P2 ever gets a screen of ours**.
- **The strongest argument against is the same one:** designing that screen means designing for a
  person who, in **five venues and four rounds, has never spoken in the first person.** Every account
  of a handover is written by the sender.

**What it would bring with it — product consequences, not build ones.** `visibility` stops being a
field §9 hides and becomes **a control that can act** — which reverses §9's own reasoning rather than
contradicting it, since §9 hid it precisely because nothing could act on it. A shared project needs to
say **who may open it**. It needs an answer to **snapshot or live** — our model links live (§5), but a
receiver's setup changing under them is a different matter. And **RJ-4 gets sharper**, not softer: the
one thing observed on the receiving side is four people stripping the author's credentials out of
inherited material, and an agent copying a live token out of a keyring.

**Where it attaches, unchanged.** A public project or item page is a **consumption surface for
somebody else's work**, which is what the Public scope and the read-only public item already are
(E3, E15). The shape exists and `visibility` is already on both entities (§5).

**One rule survives whichever way Q13 goes**, and it is worth keeping for its own sake: **the archive
must be complete on its own.** Whoever gets the link may also just get the file, and the file is what
lands on the machine.

### What is not a screen

Listed because each one is a thing an information architecture is tempted to promote, and every
promotion here would be a place with no job under it.

- **The first run.** `My library` empty beside a full shelf, Projects holding only the example — these
  are **states** of two screens (§11), and flow 08's rule scales the explanation to how new the
  concept is. **Not an onboarding screen, not a tour, not a wizard.**
- **The check in progress.** A **state** of Run, not a screen of its own. Neither is the unclean-export
  confirmation, which §6 puts in the row below the finding that caused it.
- **The example project.** An **instance** of Project with a label and a delete, not a place.
- **The public shelf.** A **scope** of Library — same rows, same search, same filters, because it is
  the same object seen in two places (§8). A second screen would say it is a different kind of thing.
- **Settings, account, sync, team.** §9 refuses all of it and there is no job. **Not proposed.**
- **A dashboard of what is working.** It would answer [EJ-3](../research/7-jobs-to-be-done/jtbd.md#ej-3--stop-suspecting-that-half-of-what-i-keep-is-dead-weight)
  — importance **3** for the primary persona, the highest the product cannot close — and §6 **runs
  nothing on anyone's machine**, so it would be a promise we have no way to keep. **The job is real and
  the screen is forbidden**, which is Q12.

### Where this disagrees with §8, and it is one place

`CLAUDE.md` §8 names **Library, Project, Run and Projects**. This derivation produces the same four
**and one more: Item.** §8 folds an item's editing into the Library as an *add/edit form*.

**The argument for a place rather than a form** is [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it),
importance **3** for the primary persona: *fix it once and have the fix reach every copy* is an act
with **blast radius**, and §5 requires that radius to be legible before the edit — *used in 3
projects*, and since 2026-09-15 *this edit un-checks 3 checked projects* (§6). A form is opened to be
filled and closed; that is a different thing from a place you go to in order to understand what you
are about to disturb. **Q7's answer pushes the same way**: with the collector primary, the item is the
unit the person lives among rather than something they fill in on the way to a project.

**This is not decided here.** It is the question step 2b answers — *is Item a place somebody can be
sent to, or a state of the Library* — and this section records that the jobs argue for a place while
§8 currently says a form.

**And one question today's decision forced into the open.** Since **the run is a moment and nothing is
stored** (§6, decided 2026-09-15), **Run has nothing to be linked to afterwards.** So *is Run a place
at all, or a mode the Project enters?* The tree draws it as a screen because it takes the whole
surface and has its own content; **whether it is addressable is step 2b's**, and the honest note is
that a place you can never return to is an unusual kind of place.

---

---

## Places, modes, overlays and states — what kind of thing each one is

> **Step 2b, written 2026-09-15.** The screen tree above is a hierarchy; this is what each node
> actually *is*. No backend is involved and none is assumed: everything here is client-side logic,
> flow and experience.

**The rule, restated for a product with no server.** *A thing is a **place** only if somebody could be
sent there and arrive.* With storage in one browser and nothing to share, *being sent* does not mean a
link to another person — it means **the three things a place owes you on your own machine**: you can
**reload** and still be where you were, **Back** means something, and the address can be **written
down** and come back to the same view tomorrow. Anything that fails those three is not a place, however
much of the screen it occupies.

**Four kinds, and the difference that matters is addressability, not size.**

| Kind | Test it passes | Test it fails |
|---|---|---|
| **Place** | Reload lands you here · Back is meaningful · the address survives | — |
| **Mode** | Takes the surface, has a way out | **Not addressable** — reload cannot restore it |
| **Overlay** | Summoned over what you were doing, dismissed back onto it | Never in the address; loses nothing when dismissed |
| **State** | A place or a mode looking different **because of the data** | Not navigated to at all |

### The classification

| Thing | Kind | Why |
|---|---|---|
| **Library** | **Place** | Reload, Back and a written-down address all work, and §8 requires it to be *one keystroke away and remembering where you were* |
| **Library scope** — `My library` · `Public library` | **Part of the Library's address**, not a toggle state | If the scope were transient, a reload would drop you into `My library` — which on first run is **empty by design** (§11), so the one situation the product must not dump you into is the one a reload would produce. Two addresses of one screen, same rows and same filters |
| **Item** | **Place** | Decided below |
| **Projects** | **Place** | The list you come back to, now carrying each project's verdict and date (§6) |
| **Project** | **Place** | The set you work in; every row carries its own state (§7) |
| **Run** | **Mode of the Project** | Decided below |
| **Editing an item that exists** | **Mode of the Item place** | You are still looking at the same object; leaving returns you to it |
| **Creating an item** | **Overlay on the Library** | There is no object yet, so there is nothing to be a place for |
| **A detached row — edit, reset, promote** | **Mode of the row, inside Project** | The override exists only in this project (§5), so it has no meaning without the project around it |
| **The `⌘K` palette** | **Overlay** | Summoned, dismissed, never in the address — and it is *the only way the library reaches the Project screen* (§8), which makes it load-bearing rather than a convenience |
| **A finding** | **Content**, not navigation | It annotates the row that owns it (§8); the ones that own no row belong to the set |
| **The unclean-export confirmation** | **State of a row inside Run** | §8 puts it *in the row below the finding that caused it* — **not a modal**, and this is where somebody would otherwise draw one |
| **The check running** | **State of the Run mode** | — |
| **Empty `My library` · Projects holding only the example · a project with no members** | **States** | §11 and flow 08 — *scale the explanation to how new the concept is* |
| **A stale verdict** | **State of a project row** | §6: the verdict is not shown, the date is, and what voided it is named |
| **Shared project** · **Shared item** | **Places**, and the most place-like things in the product | The link **is** the address — it is written down, sent, reloaded and bookmarked by somebody who has nothing else. They are the only places whose address has to survive leaving this machine |
| **Sharing something, and revoking it** | **A state of the thing shared**, disclosed at the moment it changes | §5: sharing is a **standing decision**, so *shared* is how a project or item reads everywhere it appears — not a screen, and not a one-time dialog either |
| **Library import / export** | **Two commands on the Library** — not a screen | This resolves the orphan's own open question: it is cheaper than it looked. **It is still an orphan** — no job raises it — but a command with no job is a smaller thing to carry than a place with no job |

### `Item` is a place, and this is a proposal to §8

**The rule answers it.** Being sent to an item and arriving is something the product needs internally:
*used in 3 projects* is a **count that is also a link** — the best consequence disclosure in the whole
benchmark (VS Code Workspace Trust, C2 = 5) — and what it links to is the item, or the projects. A
count you cannot follow is Figma's *423 instances*, which the benchmark scored one step behind for
exactly that reason.

**The job argues the same way.** [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it)
is importance **3** for the primary persona, and editing a linked item has **blast radius**: §5 wants
it legible *before* the edit, and since 2026-09-15 that radius has a second half — the edit **un-checks
every project whose resolved set contains the item** (§6). *A form is opened in order to be filled and
closed. A place is where you go to understand what you are about to disturb.* And with **Q7 naming the
collector primary**, the item is the unit this person lives among rather than something filled in on
the way to a project.

**§8 currently says the Library holds an *add/edit form*.** This section proposes: **add** stays an
overlay on the Library, **edit** becomes a mode of the Item place. **Not applied** — §8 is the
owner's, and lesson 03 raises rather than edits.

### `Run` is a mode, not a place — and that follows from the run being a moment

**Apply the three tests.** Since 2026-09-15 **no run is stored** (§6): no id, no list, nothing to
return to. So *reload* cannot land you back in a check — the check is gone. The address could not
survive, because there is nothing for it to name. **Run fails two of the three tests, so it is not a
place.**

**What it is instead: the mode the Project enters when you press Check.** It still takes the whole
surface, exactly as §8 says — **taking the surface and being addressable are different properties**,
and this is the case that separates them.

**Two behaviours follow, and they are decisions rather than details.**

- **Back leaves the check and returns to the Project.** There is nowhere else it could go.
- **A reload during a check returns to the Project and does *not* silently start a new one.** Checking
  is an action the person takes; a reload that re-runs it is the product making a choice nobody made,
  which is [EJ-1](../research/7-jobs-to-be-done/jtbd.md#ej-1--not-be-quietly-overruled-by-my-own-tools)
  — importance **3** for the primary persona and the one job §6 already treats as a constraint on
  everything else.

**And one honest consequence.** Because Run is a mode and nothing is stored, **the handover disclosure
cannot be bookmarked or returned to** — re-reading it means checking again. That is the price of the
decision, it is cheap because we run nothing on anyone's machine, and it is recorded here rather than
discovered in step 5.

### Six places, and that is the whole navigable surface

**`Library` · `Item` · `Projects` · `Project`**, with the Library carrying two addresses, one per
scope — **plus the two the link creates, `Shared project` and `Shared item`** (Q13, 2026-09-15).
**Everything else is a mode, an overlay, a state or content.** That is the shape step 3 will put
routes on, and it is deliberately small: **four places for the owner, two for everybody else**, in a
product whose primary persona keeps **tens of items, not hundreds**.

**The split matters and step 3 has to honour it.** The owner's four are addressable **on one
machine** — reload, Back, a bookmark. The receiver's two are addressable **off it**: the link is
written down, sent, and opened by somebody who has nothing else and no context. **That is the only
line in this architecture where an address has to mean something to a person who did not make the
thing it names.**

---

## What this section establishes, and what it does not

**Establishes.** **Fifteen entities, each with a job and a link to it**, and **eleven candidates
refused for a stated reason — of which one, the licence, was promoted on 2026-09-15 by an owner's
decision rather than by evidence, and is recorded as such in both places.** Three relations, not one: most of this product belongs to its owner,
**three entities exist for the receiver** — the archive, `SETUP.md` and the agent target — and **one
points at an external author**.

**And two findings that were not visible before the objects were laid out side by side:**

1. ~~**§5 has no object for the check or for a finding**, and §8 gives the check an entire surface, so
   *does a run persist* has no answer anywhere.~~ **Raised and answered the same day, 2026-09-15: the
   run is a moment.** Nothing is stored; the project keeps when it was checked, what the check found
   as counts, and against which target, and **that verdict is void as soon as the set changes.** §5,
   §6 and §8 carry it. **This is the one thing lesson 03 has changed in the specification so far, and
   it was a gap rather than a disagreement** — the architecture could not be drawn without an answer.
2. **The best-evidenced entity in the product is the one built for the persona nobody has ever
   interviewed.** `SETUP.md` has `✓` behaviour under it — three of three, and 30 of 214 receivers
   writing the manual themselves — while every *account* of the receiving end is written by a sender.

**What the sitting of 2026-09-15 does to this inventory.** **Q7 named the collector as the primary
persona** and **Q8 kept §2's *assembly with validation* as the main job**, which together move weight
**toward E1, E2 and E14** — the item, the personal library and the usage facts that let somebody judge
their own corpus — and leave **E11, E12 and E13** standing as **mechanisms rather than as the point**.
No entity is added or removed by it: a disposition decides emphasis, and every object here still earns
its place by closing a job. **The cost is recorded in the register**: the collector's own job is the
thinnest evidence in the folder, so the surfaces that now carry the most weight are the ones with the
least under them.

**And the screen tree establishes five screens and one orphan**, each with the job it serves, grouped
by the person's own three situations rather than by anything that could become a menu. **Its two
findings are refusals rather than places, and one is now under review:** the receiver needs **no screen
in the product as specified today** — their whole surface is `SETUP.md` inside the archive — **which
holds only while a shared link is out of scope, and that is Q13** in
[the register](../research/research-plan.md); and the highest-importance job the primary persona has is
one **no screen may serve**, because a dashboard of *what is working* promises a runtime §6 does not
have.

**And the classification answers the two questions the tree raised. `Item` is a place** — a count
that is also a link needs somewhere to lead, and an edit with blast radius needs somewhere to stand,
which is a **proposal to §8** rather than an edit of it. **`Run` is a mode of the Project, not a
place** — it fails two of the three tests because nothing is stored, and taking the whole surface is
not the same property as being addressable. **Four places in the whole product**: Library with an
address per scope, Item, Projects, Project.

**Does not establish. Routes** — the strings themselves, and what each promises — which is step 3. Nor
the shape of E1, which proposal **S-2** would change from a file to a directory, and which the sitting
has not decided.
