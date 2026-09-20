# Sitemap — lesson 03, information architecture

> **A draft, in six sections.** Written 2026-09-15, **re-checked against the owner's decisions of
> 2026-09-16** — the credential refusal overruled, Q10 built as `defersTo`, and `Item` kept as a form.
> Everything they touch is marked with that date. **The fifth section, Navigation, was written the same
> day** out of the places the third established: two global entries, the click depth to the main job,
> and the global / contextual / deep split. **[`flows.md`](flows.md) then walked six paths through
> all of it** — the main job, RJ-1 to RJ-4 and the single-item export — **and needed no screen this
> file did not already have**, which is the closest thing to a test this section can be given.
> **The sixth section, Traceability, was written on 2026-09-20** once the owner accepted those flows:
> every job against every surface, the two orphan lists, and a decision for each orphan. **It is the
> second test, and a harder one** — the flows asked whether the map has a gap, and this asks whether
> anything on it is unearned. It decides nothing on implementation grounds:
> what the product is comes first, and how it is built comes after — a rule this file had to be
> corrected against once already, see *The screen P2 would have*. **Entities** — the objects a person handles in order to close a
> job. **Screens** — derived from those objects and from the jobs, never from anybody's product.
> **Places, modes, overlays and states** — what kind of thing each node actually is, which is where
> *five places* comes from — *this line said four when it was written, before Q13 added the two shared
> surfaces; six with them, and **five since 2026-09-16**, when the owner kept §8 and `Item` stopped
> being one.* **Routes are still not here**: naming them is step 3, and it now has both a shape to put
> them on and a navigation model constraining them — **Navigation**, step 4, written first because the
> owner asked for it and because it needed nothing step 3 produces.

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
- **What the page carries, updated 2026-09-16.** Everything the set contains, what each item needs,
  **what any of it defers to** (§5, `defersTo`) — and the receiver is precisely the person whose linter
  it is likely to be, which makes this the sharpest place the deference is read after `SETUP.md` — plus
  the origin and licence of anything that is not the sharer's own, and **the same Check the owner has**.
- **And creating a link refuses nothing, as of 2026-09-16.** For one day §6 blocked a share on a
  credential found in item content; **the owner overruled it** because detection was the unbuildable
  half. **What remains is the disclosure** — before the link exists, the product names what becomes
  visible, including that item **content** is visible — and the warning given far earlier, when the
  material entered the library (E2). **So this entity has no gate on it at all**, which restores §6's
  *nothing blocks* to being universal.

### E1 · Item

One reusable block. The atomic unit, and the thing every other entity is about.

- **Fields (§5).** `id` · `kind` — one of six, `skill | agent | prompt | mcp | script | app` · `name` ·
  `description` · `tags[]` · `visibility` · `source` — `inline | external` · `content` when inline ·
  `repoUrl`, `path`, `ref`, **`license`** when external · `requires[]` · `conflicts[]` ·
  **`defersTo[]`** · `needsEnv[]` · `targetPath`. *`license` added to §5 on 2026-09-15 — see E15.
  **`defersTo` added on 2026-09-16**, building Q10's answer: the external authorities this item yields
  to, declared by hand, raising a Note wherever the item sits in a set (§6).*
- **Parts that are not fields.** Its **usage facts** (E14) and, when external, its **provenance**
  (E15). Both are derived or borrowed rather than authored.
- **It can leave on its own, and it can be deleted** — both added 2026-09-20. **Export (Q15):** an item
  exports from the Library without a project, **the dependency walk still running**, so an item with
  `requires` leaves as a set of N named as one; an agent target is still chosen because `targetPath`
  needs one, and an external item still leaves as an instruction. **An item with an empty `requires`
  cannot produce a Problem**; **any `requires` edge makes it a set question** — resolved, the set can
  collide; **dangling, the edge is itself an unresolvable requirement** (§6, corrected 2026-09-20 after
  the review caught it contradicting Q17). It produces any Note either way. **Delete (Q17):** confirmed, never
  refused, naming the projects that hold it *and* that a `requires` edge may be left dangling (§5).
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
- **The way in carries a warning, and as of 2026-09-16 it is the product's answer on secrets.** Material
  entering this library — one item, or the whole library as JSON — is met with *check that these files
  carry no keys*, naming why: what comes in goes out in **every archive built from it** and, if the
  thing is ever shared, **onto an address anyone can open** (§11). **It is a reminder, not a scan**, and
  it says so; it is therefore **not one of §6's three severities**, and it does not block. *This
  replaced the credential refusal §6 carried for one day — see §6 and the register.* **Structurally it
  matters here because this entity has exactly one way in**, so there is exactly one place to say it.
- **And as of 2026-09-20 it has three ways out, which is one more than it had.** The archive built from
  a project (E11), **a single item exported on its own** (Q15, E1), and a **share link** (E16). *This
  matters to the warning above*: it was justified by *what comes in goes out in every archive built from
  it*, and that sentence now covers one more exit than when it was written. **Nothing about the warning
  changes** — it was never exit-specific, which was the point of putting it at the entrance.
- **The way out that is not an exit: delete** (Q17, 2026-09-20). Confirmed rather than refused, and the
  count it names is E14's. **What happens to a detached row whose original is deleted is open.**
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
- **Reachable during assembly since 2026-09-20** (Q14). The library panel carries the same scope
  switch the Library screen does, so the shelf is one control away **inside the Project**, which is
  what makes it answer cold start where it actually bites: `My library` is empty on first run by §11,
  and until now the way to the shelf led out of the builder and back. **This raises the shelf's
  stakes rather than its evidence** — it is more load-bearing and no better established, and Q9, what
  it holds and how it sorts, is still unanswered.
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
- **This entity is what the library panel's checkbox is about** (Q14, 2026-09-20), and saying so
  prevents a misreading. A checked row in the panel does not mean *this item is special*; it means
  **a `ProjectItem` exists for it in this project**. That is why **removal lives on the project row as
  an `✕`** and merely unchecks the panel: the row *is* the membership, and the panel is a view of it.
  **Both the checkbox and the `✕` live in the configuring mode** (2026-09-20): a row being read is not
  a row being changed. And it is why `addedBy: dependency` **refuses** — you cannot delete a membership
  the walk will recreate while its puller is there (§6). **A checkbox that refuses to clear is the honest rendering
  of this field**, not a defect in the control.
- **Job.** [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it)
  — the live link is *the one mechanism in the specification that exists for exactly that job*. And
  [H-J3](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list)
  — *change one copy for one project without touching the rest* — which is `detached` and `overrides`
  named as a requirement by one person on a public forum, blocked three ways at once.
- **Relation.** Owner. It binds E4 to E1 and belongs to neither.
- **Standing.** `§`5, §7. `✓` that copies drift and stay drifted — **14% of 7,506 duplicated items out
  of sync now; 383 divergences open at a median of 121 days; four ever reconciled.** H-J3's importance
  is a **2**, raised from `[?]` on 2026-09-10.
- **And the silence around it, found by [`flows.md`](flows.md) RJ-3. `[?]`** A detached row is
  **deliberately not reached** by a fix made in the library — that is what it is for — but **nothing in
  the Library says so at the moment of the edit** (E14). The flow draws it as a dead end: the old
  version survives in a project the person did not open. **Step 5's question, not §5's.**
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
  specification where the product refuses an action — **true when written, briefly false while §6
  carried a credential refusal, and true again since 2026-09-16.**

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
- **And a third declared thing, added 2026-09-16, which points *outside* the set.** **`defersTo`** (§5,
  *Deference*) names the external authorities an item yields to — *the client's ESLint config*, *the
  repo's commit convention* — hand-filled exactly as these two are, and for the same reason: §9 parses
  nothing. **The difference is structural and step 6 has to hold it.** `requires` and `conflicts` point
  at objects **inside** the library, so the walk can read them and a finding can point at both ends.
  `defersTo` points at something **we have never seen and can never compare against**, so it produces a
  Note that is carried rather than computed. It is Q10's mechanism.
- **Standing.** `§`5, §6 · `✓` for `requires` and `conflicts` · **`*`, n = 1, for `defersTo`** — one
  practitioner's aside, *"there's no precedence anywhere"*, and **building the mechanism did not
  promote the mark.**

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
- **It has three sources since 2026-09-20, and only two of them own a project.** The owner from their
  Project, the receiver from a shared link, and — Q15 — **the owner again from a Library row exporting
  a single item.** *Added after a review found the third written into §6 and into no entity.* The
  third sharpens what this entity already is: **a run with no project behind it leaves nothing at all**,
  which was true of a visitor's run and is now true of one of the owner's own.
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
  radius with a consequence attached. **`defersTo` joined the list of voiding edits on 2026-09-16**,
  beside `needsEnv` and `targetPath`, because it is an input to a finding.

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
- **A fourth kind of Note, added 2026-09-16 with Q10's mechanism, and it behaves unlike the others.**
  An item declaring `defersTo` raises a **Note on its own row** — *`code-style` defers to the client's
  ESLint config. Where they disagree, that wins.* **Nothing is compared**: the product repeats a
  sentence the user wrote. **And it never clears.** A missing env key clears by supplying it, an
  unpinned `ref` by pinning it; **a deference clears only by removing the declaration or the item**,
  because it reports a standing property of the set rather than a defect in it. **Two structural
  consequences for step 5 and step 7.** A set with three deferring items shows **three Notes at every
  check for as long as it exists**, so a project's `checkVerdict` counts may never reach `0 notes` —
  **the count is not a to-do list and the surfaces must not draw it as one.** And it is the first
  finding whose subject is **outside** everything the check can see.

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
- **What the product does about the other half — content, not keys, decided 2026-09-16.** `needsEnv`
  makes an **env value** structurally unleakable, but a key pasted into an item's `content` is not an
  env requirement and this entity never sees it. **The answer is a warning where material enters the
  library (E2), not a scan anywhere** — the credential refusal §6 carried for a day was overruled
  because detection was the part that could not be built. **So this entity's guarantee is exact and
  narrow, and must be stated as narrow**: we cannot leak a value we never hold; we can carry a key
  somebody typed into a file.
- **Open. `[?]`** Proposal **S-4**: a receiving agent, told only to set the project up, **read the
  machine's live OAuth token out of the keyring and wrote it into a plaintext file.** The risk runs
  both ways and the specification names only one of them.

### E11 · Archive

What a project becomes. The product's stated wow moment (§2).

- **Parts (§6).** Inline items placed by `targetPath`, per kind · external items as **instructions,
  never vendored** · **all MCP servers merged into one config**, where a key collision is a Problem and
  **two items declaring the same key at different `ref`s is a collision too** · **`.env.example`** ·
  **`SETUP.md`** (E12) · everything named for the chosen **agent target** (E13).
- **It has a second source since 2026-09-20** (Q15). An archive is normally what a **project**
  becomes; it can now also be what a **single item** becomes, exported from the Library with no
  project around it. **The parts are identical** — the walk runs, the target is chosen, external stays
  an instruction, `.env.example` and `SETUP.md` are produced — and for a bare item most of them are
  empty, which the run reports as `Skipped`. **What differs is what is left behind: nothing**, because
  §6 puts the verdict on the project and there is no project (E4, E8).
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
  needs, the env keys it expects, the external repos to clone **at their pinned `ref`**, **what it
  defers to** (§5, added 2026-09-16), and where everything lands for the chosen target.
- **And the deference lands here harder than anywhere else.** Of the four readers told about a
  `defersTo` — the Note for the owner, the row, the shared page, this document — **this is the only one
  standing on the machine where the other rule actually lives.** It is therefore the only reader that
  can *act* on the sentence rather than note it, and acting on it is what Q10's answer asks for: the
  external one wins. **It is also the reader with a measured failure record** — Q-F watched one of
  three mis-resolve a defect it had not been told about — which is the same argument as **S-1**, one
  step over.
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
- **A single-item export needs one too** (Q15, 2026-09-20), and that sharpens the open question rather
  than answering it: `targetPath` is meaningless without a target, so **even one item cannot leave
  without this choice** — and there is no project to hold it. **Whichever way step 3 goes, *on the
  project* cannot be the whole answer.**
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
- **Where it is read, and what that cost on 2026-09-16.** These facts were the strongest argument for
  making `Item` a place: *used in 3 projects* is **a count that is also a link**, the benchmark's best
  consequence disclosure (VS Code Workspace Trust, C2 = 5), and a count you cannot follow is Figma's
  *423 instances*, scored a step lower for exactly that. **The owner kept §8's form, so there is no item
  to link to.** What this entity gets instead: **the count expands where it stands** — on the Library
  row, naming the three projects — and **each name leads to the Project**, which is a place. **The item
  is not addressable; what the count is about still is.** That is weaker than the benchmark's best and
  is recorded as weaker.
- **And it is read a second time, at the head of the add/edit form.** With no place to arrive at and
  read a blast radius, **the form states it before any field is editable** — *used in 3 projects ·
  saving un-checks all three* (§5, §6). So this entity is doing **two jobs on one surface**: telling the
  owner what they have, and telling them what they are about to disturb.
- **A third reading was added on 2026-09-20: the delete confirmation** (Q17). *`db-migrate` is used in
  3 projects. Deleting it may stop them working.* **The count now carries three different weights on
  three different surfaces** — informative on the row, cautionary before an edit, and consequential
  before a deletion — **and the open question below bites hardest on the third.** A count that silently
  includes detached copies understates an edit's reach; on a deletion it **overstates** it, because a
  detached row holds its own `overrides` and may not break at all. **Two surfaces reading one number in
  opposite directions is a step 5 problem, and it is named here rather than discovered there.**
- **Open, and [`flows.md`](flows.md) is what found it. `[?]`** *Used in 3 projects* counts **every**
  project holding the item, linked and **detached** alike — and a detached copy **by design does not
  receive the fix** (E5, §5). So the one number the owner reads before an edit with blast radius
  **does not say which of those three will not get it.** The mechanism is correct and the disclosure is
  missing. **Not decided here**: it is a question for step 5 about what the form's head says, not a
  change to §5, and it is the sharpest thing the five user flows returned.
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
| ~~**Q-E7**~~ | ~~**An external requirement** — a client's linter, a repo convention~~ | ~~That is **Q10**, live and standing on one person.~~ ~~Q10 was answered on 2026-09-15 … **It is not in §5 yet**, and the reason it is still in this table is that detection is impossible in the MVP~~ **Left this table on 2026-09-16: §5 and §6 now carry it.** `defersTo[]` is a field of **E1** and a declared relation alongside `requires` and `conflicts` (**E7**), raising a Note that never clears (**E9**) and read on the shared page (E16) and in `SETUP.md` (E12). **The reason it sat here is unchanged and is now written into §5**: detection is impossible, so the field discloses a constraint the user declared and **never compares anything**. The mark stays **`*`, n = 1** | — |
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
  ├── Library ......................................... [H-J1] [RJ-3] [EJ-3 partly]
  │     two scopes, one screen: My library · Public library  [H-J4 ?]
  │     │
  │     └── Item — add / edit form, an overlay, not a screen
  │           §8, kept 2026-09-16. It discloses blast radius
  │           before it accepts an edit
  │
  └── Library import / export (whole library as JSON) . [§10]
        no job raises it — and that stopped being the test
        on 2026-09-20 (Q18): its warrant is IndexedDB with
        no backend, so one browser profile holds everything

2 · WHAT I AM PUTTING TOGETHER  — the set for one piece of work
  │
  └── Projects ........................................ [MAIN] [H-J2 ?]
        │
        └── Project ................................... [MAIN] [RJ-2]
              │
              ├── Configuring the set — a mode ........... [MAIN] [RJ-2]
              │     Q14 amended 2026-09-20. Entered and left by a
              │     named action; the set is not editable outside it
              │     │
              │     └── Library panel — a region, not a screen
              │           Scope switch over kind tabs, Related first.
              │           Reads and adds; never edits
              │
              └── Detached row — edit, reset, promote .. [H-J3]

3 · WHAT LEAVES  — the thing that has to work somewhere else
  │
  └── Run ............................................. [MAIN] [RJ-2] [RJ-1] [RJ-4] [SJ-1]
        entered by Check from a Project, from a shared
        project, and — Q15, 2026-09-20 — from a Library
        row exporting one item. Ends in Export.

4 · WHAT SOMEBODY ELSE OPENS  — the receiver's only surfaces
  │
  ├── Shared project .................................. [MAIN] [RJ-1] [SJ-1]
  └── Shared item ..................................... [MAIN] [H-J4 ?]
        read-only, opened by anyone holding the link, and each offers
        a way to take it — the archive, or a copy into their own library
```

**Six screens and one orphan, and the tree lists four nodes that are not screens** — the `Item`
add/edit form, an **overlay** on the Library (§8, kept 2026-09-16), the **detached row**, a mode
inside Project, and, since 2026-09-20, the **configuring mode** and the **library panel**, a region
inside it (Q14). *An earlier
count here said five screens and was stale: it predates the two surfaces Q13 added. The non-screen
count was two until the panel replaced the palette.* **The screen count did not change when the
builder's mechanism did**, which is the thing worth noticing: a palette that was an overlay became a
panel that is a region, and no place was created by either. The three groups are the person's own three situations, in the order
[`personas.md`](../research/6-personas/personas.md) records them: *copying something out of the
collection into a new project · adding a rule right after an agent did something annoying · hunting
for something they know they wrote.* They are not navigation sections and should not become a menu in
step 3 — they are why the screens exist.

### Each screen, its job, and what the person came to do

| Screen | Job it serves | What the person arrived to do | Persona |
|---|---|---|---|
| **Library** | [H-J1](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) · [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it) | *Lay hands on the thing I know I wrote* — and reach the one copy that a fix has to land on | **P1** · P3 in its public scope `[?]` |
| **Item** — *not a screen: an overlay* (§8, 2026-09-16) | [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it) · [EJ-3](../research/7-jobs-to-be-done/jtbd.md#ej-3--stop-suspecting-that-half-of-what-i-keep-is-dead-weight) partly | *Fix this once*, and see who else it reaches before touching it — **which the form must say before it accepts the edit**, since there is no place to arrive at and read it | **P1** |
| **Projects** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [H-J2](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) `[?]` | *Get back to the set I keep for that piece of work* — and see whether it is still checked | **P1** · P3 for the example `[?]` |
| **Project** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act) | *Put the set together and see what it drags in* — every row carrying its own state | **P1** |
| **Library panel** — *not a screen: a region of Project's configuring mode* (Q14, 2026-09-20) | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act) | *See what I own that fits here, and put it in* — **the question the palette could not answer**, and the reason the corpus is present during assembly at all | **P1** · P3 through the shelf scope `[?]` |
| **Detached row** — edit · reset · promote | [H-J3](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) | *Change it here only, without the others getting it* | **P1** |
| **Run** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act) · [RJ-1](../research/7-jobs-to-be-done/jtbd.md#rj-1--know-what-the-other-side-will-still-need-before-i-send-it) · [RJ-4](../research/7-jobs-to-be-done/jtbd.md#rj-4--move-my-work-without-moving-my-secrets-or-my-clients-business-with-it) · [SJ-1](../research/7-jobs-to-be-done/jtbd.md#sj-1--not-be-the-missing-manual-for-my-own-work) | *Find out whether it holds together, see what the other side still needs, and get the archive out* | **P1** |
| **Shared project** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [RJ-1](../research/7-jobs-to-be-done/jtbd.md#rj-1--know-what-the-other-side-will-still-need-before-i-send-it) · [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act) · [SJ-1](../research/7-jobs-to-be-done/jtbd.md#sj-1--not-be-the-missing-manual-for-my-own-work) | *Somebody sent me this — what is it, does it hold together, what do I still need, how do I take it* | **P2**, and it is their only surface |
| **Shared item** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · [H-J4](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) `[?]` | *Somebody sent me one block — what is it, whose is it, may I use it* | **P2** · P3 `[?]` |
| **Library import / export** | ~~`[orphan]`~~ **`[§10]`** — settled 2026-09-20, Q18 | *Get my corpus out of the one browser profile that holds it* — **not a job anybody stated; a consequence of the storage decision** | P1 |

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
| **P1 — the keeper of a corpus** · **primary** | **All four of the owner's** — Library, Projects, Project, Run — and the Library carries more weight than it did before 2026-09-15, **now including the weight `Item` would have carried** (2026-09-16) | Q7 named the collector primary, so the corpus screens stop being the place you pass through on the way to Run. **The cost is on the record**: the collector's own job is the thinnest evidence in the folder |
| **P2 — the receiver** · secondary | **Two, as of 2026-09-15: the shared project and the shared item** — plus `SETUP.md` inside the archive, which is not a screen | **The finding changed the same day it was written.** It read *the receiver needs no screen at all*; **Q13 answered yes to a link**, and P2 now has exactly the two surfaces a link can lead to. **And as of the same day they can do the product's central act on them**: the receiver runs **the same Check**, on the set in front of them, and takes the archive from its last stage. **Library-to-archive, performed by somebody who owns nothing.** **What has not changed is the hard part:** these screens are still designed for a person who, in five venues and four rounds, **has never spoken in the first person** — so they are the most `[?]`-laden places in the product, and the archive must still be complete on its own, because whoever gets the link may only ever get the file |
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
  the screen is forbidden**, ~~which is Q12~~ — **and on 2026-09-20 Q12 was closed as *refused* rather
  than deferred** (§9). The traceability matrix below is what settled it: `H-J5` is **importance 3 with
  twelve blank cells**, and an open question at that importance would otherwise be asked again on every
  surface in lessons 04 to 09. **It is a second product**, in stage 7's own words, and this one does not
  build it.

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

~~**This is not decided here.**~~ **Decided 2026-09-16: §8 stands and `Item` is a form.** The jobs
argued for a place, the owner kept the form, and **the requirement the argument was built on does not
go away with it** — the blast radius still has to be legible before the edit, so **the form discloses
it before accepting one**. See *`Item` is a form* in the classification for what that costs and what
carries it.

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
| **Item** | **Overlay, owned by the Library and summoned from three places** — add *and* edit | **Decided 2026-09-16: §8 stands.** The proposal to make it a place was rejected; see below for what the decision costs and what carries it instead. **Since 2026-09-20 it has a third door**: the library panel's zero result offers to author the missing item and opens this overlay **over the Project** (Q14). *Owned by* and *opened from* are different questions, and §8 answered only the first |
| **Projects** | **Place** | The list you come back to, now carrying each project's verdict and date (§6) |
| **Project** | **Place** | The set you work in; every row carries its own state (§7) |
| **Run** | **Mode of the Project, of the Shared project — and, since 2026-09-20, of the Library** | Decided below. **Three** places now enter the same mode: the owner from their project, the receiver from the link, and the owner again from a Library row exporting a single item (Q15). *The third was added by the review of 2026-09-20, which found it written into §6 and nowhere else.* **Nothing is stored in any of the three** — the verdict lives on a project, and two of the three have none. **The argument that Run is a mode rather than a place is unaffected and is now better supported**: a thing that three different places enter, and that no address returns you to, is not a place |
| **Editing an item that exists** | **Overlay on the Library** | ~~Mode of the Item place.~~ **§8: the Library holds one add/edit form** (2026-09-16). Dismissing it returns you to the row you opened it from, and the Library's address never changed |
| **Creating an item** | **The same overlay — from the Library, or from the panel's zero result** | There is no object yet, so there is nothing to be a place for — **and the same overlay serves both**, which is what §8 said all along. **The panel's door (Q14, 2026-09-20) does not make the panel an editor**: it summons the authoring surface, because creating is a corpus act and assembling is not. **It does mean a person can reach this overlay without ever opening the Library** |
| **A detached row — edit, reset, promote** | **Mode of the row, inside Project's configuring mode** | The override exists only in this project (§5), so it has no meaning without the project around it. **All three commands live in configuring** (Q21, 2026-09-20): they change the content of the set, and the rule written for the `✕` covers them — *a row being read is not a row being changed*. **A detached row is not an exception to it**, because a viewing mode that can change the set is not one |
| **Configuring the set** | **Mode of the `Project` place** — added 2026-09-20 | **The screen has two modes**: *viewing* the set, and *configuring* it. By the four tests it is a mode and not a state — **nothing about the data decides which one you are in, your intent does** — and not a place, because a reload returns you to the Project, not to the act. It takes the surface in the sense that matters: **the panel is present and rows can be removed, and neither is true outside it.** Whether it survives a reload is **step 3's**, and the honest default is the one already set for `Run`: it does not. **`Run` remains reachable from both modes**, so the fix-and-recheck loop is not charged an exit per cycle |
| ~~**The `⌘K` palette**~~ · **The library panel** | **Part of the `Project` place, in its configuring mode** — not an overlay, and not a place of its own | **Changed 2026-09-20, Q14.** The palette was an overlay: summoned, dismissed, never in the address. **The panel is none of those things** — it is on the screen whenever the Project is, it is not summoned and cannot be dismissed onto what you were doing, and it has no address of its own because **the Project already is one.** By this section's four tests it fails *place* (reload restores the Project, not the panel), fails *mode* (it takes no surface and there is nothing to leave), and fails *overlay* (it covers nothing). What is left is what it is: **a region of a place.** Its scope and tab are **candidates for the Project's address** and that is step 3's, not this row's |
| **A finding** | **Content**, not navigation | It annotates the row that owns it (§8); the ones that own no row belong to the set |
| **The unclean-export confirmation** | **State of a row inside Run** | §8 puts it *in the row below the finding that caused it* — **not a modal**, and this is where somebody would otherwise draw one |
| **The check running** | **State of the Run mode** | — |
| **Empty `My library` · Projects holding only the example · a project with no members** | **States** | §11 and flow 08 — *scale the explanation to how new the concept is* |
| **A stale verdict** | **State of a project row** | §6: the verdict is not shown, the date is, and what voided it is named |
| **Shared project** · **Shared item** | **Places**, and the most place-like things in the product | The link **is** the address — it is written down, sent, reloaded and bookmarked by somebody who has nothing else. They are the only places whose address has to survive leaving this machine |
| **Sharing something, and revoking it** | **A state of the thing shared**, disclosed at the moment it changes | §5: sharing is a **standing decision**, so *shared* is how a project or item reads everywhere it appears — not a screen, and not a one-time dialog either |
| **Library import / export** | **Two commands on the Library** — not a screen | This resolves the orphan's own open question: it is cheaper than it looked. **It is still an orphan** — no job raises it — but a command with no job is a smaller thing to carry than a place with no job |

### `Item` is a form — the proposal was raised and the owner kept §8

> **Decided 2026-09-16: *we go by §8*.** The proposal below was put to the owner and **rejected**.
> **The Library holds an add/edit form, and there is no `Item` place.** The argument is left standing
> because this file records what was weighed, not only what was chosen — and because the cost it names
> is now a cost we carry, which is the next block.

~~**The rule answers it.**~~ Being sent to an item and arriving is something the product **appeared to
need** internally: *used in 3 projects* is a **count that is also a link** — the best consequence
disclosure in the whole benchmark (VS Code Workspace Trust, C2 = 5) — and what it links to is the item,
or the projects. A count you cannot follow is Figma's *423 instances*, which the benchmark scored one
step behind for exactly that reason.

**The job argued the same way.** [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it)
is importance **3** for the primary persona, and editing a linked item has **blast radius**: §5 wants
it legible *before* the edit, and since 2026-09-15 that radius has a second half — the edit **un-checks
every project whose resolved set contains the item** (§6). *A form is opened in order to be filled and
closed. A place is where you go to understand what you are about to disturb.* And with **Q7 naming the
collector primary**, the item is the unit this person lives among rather than something filled in on
the way to a project.

**What the decision costs, and it is named rather than absorbed.** Two things the place was carrying
have to be carried by something else, and there are exactly two candidates: the **row** in the Library
and the **head of the form**.

- **The counter has nowhere to lead.** *Used in 3 projects* cannot open a place that does not exist.
  **This is the Figma outcome we scored a product down for**, and pretending otherwise would be worse
  than paying it. What survives is a weaker but real version: **the count expands where it stands** —
  on the Library row, naming the three projects — and each name leads to the **Project**, which *is* a
  place. **The item is not addressable; what the count is about still is.**
- **Blast radius moves to the head of the form, and that is now its only possible home.** §5 requires
  the radius to be legible **before** the edit and never named a surface; with no place to arrive at,
  the form's own opening is the last moment before the change. So the form **states, before any field
  is editable**: *used in 3 projects · saving un-checks all three* (§6). **A form that discloses
  before it accepts is not the thing the argument above objected to** — what it objected to was a form
  that discloses nothing.

**One consequence to keep visible, because it is genuinely odd.** A **shared item** is a place — the
link is its address (Q13) — while **your own item is not**. So the product can address an item, just
never one of yours. It is not a contradiction: the shared page exists because somebody outside has
nothing else to hold. **But it is the seam to look at first if `Item` is ever reconsidered**, because
half the surface would already be built.

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

### Five places, and that is the whole navigable surface

> **Was six until 2026-09-16.** `Item` left the list when the owner kept §8's form — see above for
> what that costs and what carries it instead.
>
> **Re-checked on 2026-09-20 against Q14, and it did not move.** The library panel is the biggest
> change the builder has had, and **it adds no place**: it is a region of `Project`, which is a place
> already. The check was run the only way it can be — **by putting the panel through the four tests
> above**, not by counting screens — and it failed place, mode and overlay in turn. **What *does* move
> is a step 3 question**: if the panel's scope and tab are to survive a reload, they belong in the
> Project's address, exactly as the Library's scope belongs in the Library's.

**`Library` · `Projects` · `Project`**, with the Library carrying two addresses, one per scope —
**plus the two the link creates, `Shared project` and `Shared item`** (Q13, 2026-09-15).
**Everything else is a mode, an overlay, a state or content.** That is the shape step 3 will put
routes on, and it is deliberately small: **three places for the owner, two for everybody else**, in a
product whose primary persona keeps **tens of items, not hundreds** — which was always the strongest
argument against giving each of them an address.

**The split matters and step 3 has to honour it.** The owner's three are addressable **on one
machine** — reload, Back, a bookmark. The receiver's two are addressable **off it**: the link is
written down, sent, and opened by somebody who has nothing else and no context. **That is the only
line in this architecture where an address has to mean something to a person who did not make the
thing it names.**

---

---

## Navigation — the entries, the depth, and what is always there

> **Step 4, written 2026-09-16, out of the five places step 2b established.** **No screen is invented
> here and none is added.** Navigation is a question about the screens that already exist: which of
> them a person may reach without being sent, how far the main job sits from the first one, and which
> commands are on the surface at all times versus in the flow versus out of the way.

**The rule this section obeys: an entry earns its place by opening a job cluster, and the cluster is
named with a link.** Not because a product of this kind usually has a sidebar with four things in it.

---

### 1 · Global navigation — two entries, and the third cluster deliberately has none

**The screen tree is grouped into three situations** — *what I keep*, *what I am putting together*,
*what leaves*. **They do not become three nav items, and the tree said so when it was drawn**: they
explain why the screens exist, they are not a menu. The navigation has **two entries**, and the third
cluster is reached through the second.

| Entry | The job cluster it opens | Which arrival it serves | Standing |
|---|---|---|---|
| **Library** | [RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it) — *fix it once and have the fix reach every copy*, importance **3** for P1 · [H-J1](../research/7-jobs-to-be-done/jtbd.md#6-hypotheses--the-jobs-that-did-not-earn-the-main-list) — *lay hands on the thing I know I wrote*, **2** · [EJ-3](../research/7-jobs-to-be-done/jtbd.md#ej-3--stop-suspecting-that-half-of-what-i-keep-is-dead-weight) partly | **Arrivals 2 and 3** of the three [`personas.md`](../research/6-personas/personas.md) records: *adding a rule right after an agent did something annoying*, and *hunting for something they know they wrote* | `§`8 · `✓` the corpus · **`*`/`[?]` the browse-and-find job** |
| **Projects** | [MAIN](../research/7-jobs-to-be-done/jtbd.md#the-main-job) — the set is the unit that moves · [RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act) — *what my pieces drag in*, **3** | **Arrival 1**, the most frequent one: *copying something out of the collection into a new project* — whose **destination** is a project even though the person describes it from the collection's end | `§`8 · `✓` |

**Why *what leaves* gets no entry, and it is structural rather than a matter of taste.** **`Run` is a
mode, not a place** — it fails two of the three addressability tests because no run is stored (§6). **A
nav item pointing at a mode is an item you cannot be returned to**: press it twice and the second press
means something different from the first. And there is nothing to point it at from a standing start —
**you cannot check a set you have not assembled** — so the door to *what leaves* is **Check**, on a
project, which is where §8 already put the seam. **The navigation restates the seam rather than adding
one.**

**Three things that are not entries, named because each is what a designer reaches for first.**

- **`Public library` is not a third entry.** It is **the Library's second address** (step 2b) — same
  rows, same search, same filters, one switch. Promoting it would say the shelf is a peer of the
  corpus; **its job is `[?]` in all three persona columns** (E3) and the corpus's is not.
- **`Run` is not an entry**, per above. Neither is **Export**: it is Run's final stage (§8), and an
  entry beside Check would be a second door into one room.
- **There is no Settings.** §9 refuses accounts, sync and teams, and nothing else has accumulated a
  preference. **An empty settings screen is the clearest sign a navigation was copied rather than
  derived.**

**And the receiver has no global navigation at all — by construction, not by omission.** `Shared
project` and `Shared item` are places whose address is the link (E16). **There is nowhere else for that
person to go**: they own no library and no projects, and a nav bar would advertise an account §9 does
not give them. What their page carries instead is **one way out that is not navigation** — take the
archive, or copy it into a library of their own, which is the first act of becoming P1 rather than P2.

---

### 2 · Depth — clicks from the first screen to the main job, for P1

**Where the count stops, stated before any number.** The main job is *something I already have working
has to keep working somewhere else*. **The product cannot carry it to the end** — it never touches the
receiving machine, which is why §6 says **checked, never works**. So the count runs to **the archive in
hand**, which is the furthest point this product owns.

**What the first screen is.** **Where you were last** — §8's own mitigation, *the Library one keystroke
away and remembering where you were*, generalised to the whole product. **Only the first run ever needs
a decision, and it is `Projects`**: `My library` is empty by design on first run (§11), and **the one
thing in the product that demonstrates anything is the example project**, which ships in Projects and
is built to produce a real Problem and a real Note. **Landing a new person in the one room we
guaranteed would be empty is the mistake §11 exists to prevent.**

| Path | Route | Clicks |
|---|---|---|
| **A · The set already exists** — and this is literally what the main job describes, *something I have already got working* | Projects → **Project** ① → **Check** ② → **Export** ③ | **3** |
| **B · The set does not exist yet** | Projects → **New project** ① → **Configure** ② → **the panel** × n, adding items → **Check** ③ → **Export** ④ | **4 + n selections** |
| **C · Arriving through the Library** — the persona's own description of their most frequent act | Library → **Projects** ① → **Project / New** ② → **Check** ③ → **Export** ④ | **4** |
| **D · First run ever, owning nothing** | Projects → **the example project** ① → **Check** ② → **Export** ③ | **3** |
| **P2 · The receiver, for contrast** | the link → **Check** ① → **take the archive** ② | **2** |

**Four things fall out of the count, and three of them are findings rather than numbers.**

1. **Three is the floor, and B stopped sitting on it on 2026-09-20.** *This row read "three is the
   floor, and it does not move when the set does not exist" until the panel was put inside a mode.*
   **It moves now**: a project with nothing in it shows an empty state whose one action **enters the
   configuring mode**, and that is one click before anything can be added. **B is four.** A and D are
   still three, so **the floor holds; what fails is the claim that the floor is indifferent to whether
   the set exists.** *Recomputed rather than edited, which is what this table is for.*

   **The sentence underneath the number survives.** The fourth click is **a mode entry inside one place,
   not a traversal to another**, so *the depth of this product is in selection, not in traversal* still
   holds. *Until 2026-09-20 this finding also ended "which is the strongest argument for §8's
   list-plus-palette choice over a pane pair."* **That was never an argument against a pane** — it is
   an argument against *traversal*, and a pane inside the place you are already in adds none. What it
   still rules out is the shape where assembling means **going somewhere else**; entering a mode is not
   that, and the one click it costs is named here rather than absorbed.
2. **The persona's most frequent arrival costs four — and since 2026-09-20 it is optional, and no
   longer alone at four.** *This row said "the only four-click path"; B joined it the same day when the
   panel moved into a mode.* **The two fours are different in kind and that is the point**: C's fourth
   click is a **traversal** — you started in the wrong place — while B's is a **mode entry** in the
   right one. Arrival 1 — *copying something out of the collection into a new project* — is described
   from the collection's end, and the collection is **not part of the builder flow** (§8). **That
   decision shows up here as one click, and it is named rather than absorbed.** ~~What pays for it is
   mitigation 1: the palette opens cold on related items.~~ **What changed with Q14 is better than a
   payment.** The corpus is now present *inside* the Project as a panel, with `Related` first and the
   shelf one switch away, **so the person who would have started in the collection no longer has to**:
   the same errand runs as path B, at three clicks. **Path C is not shortened — it is made
   unnecessary**, and it stays in this table because a person who *chooses* to start in their
   collection still pays the fourth click, and because it is the row that records what the choice
   costs.
3. **The receiver is shallower than the owner — 2 against 3.** The person who owns nothing has the
   shortest path to an archive in the whole product. **Recorded as an observation and not as a claim
   about adoption**, exactly as §6 records the same shape: *Library-to-archive performed by somebody
   who owns nothing.* **P2 has still never spoken in the first person**, so this is a number about our
   structure, not about their experience.
4. **No path to the main job passes through the Library — and as of 2026-09-20 that is deliberate
   rather than a tension.** It was the plainest statement of what **Q7 created and did not resolve**:
   the sitting made **the collector primary**, and the collector's own ground was the one place the
   product's central act did not touch. **Q14 resolved it from the other side.** The corpus reaches
   assembly as a panel, so **the Library does not need to be on the route in order to be present in the
   work** — and the owner said it in those terms: *during building a project we will not open the
   library, there is no need.* The Library is the **curator's room**: read, curate, edit, add, delete,
   usage facts, copy from the shelf, share, JSON. **The warning below it survives intact and is now
   sharper**: if the Library ever grows builder machinery to justify itself, this row is the reason
   why — and it has **two** refusals behind it now, §8's original one and a panel built specifically so
   the Library would not have to.

**The three load-bearing mitigations, and where each is now doing its work** — §8 named them and this
section is the first place they are accountable.

> **Rewritten 2026-09-20 against Q14.** These three existed to pay for **not having a pane**. One is
> now paid by the pane, one has changed what it pays for, and one is untouched — **and none of them
> silently disappeared**, which is the only way this table can be rewritten honestly.

| Mitigation (§8) | Where it pays now | If it fails |
|---|---|---|
| **`Related` first and default in the panel** — *was: the palette opens cold on related items* | Path B's n selections. **It is the same mitigation in a new home**, and it is the one thing that stops the panel being a typological index of everything you own | The panel answers *what exists* instead of *what belongs here*, and n selections become n searches |
| **The Library is one keystroke away and remembers where you were** | **No longer pays for assembly at all** — assembly does not go there. It pays for the corpus acts: the first screen is *where you were*, and arrivals 2 and 3 cost one keystroke | Every corpus act starts with re-finding your place, and **EJ-3** — already unclosable — gets worse |
| **Per-item usage facts do the work a visible pane would do** | **Unchanged in wording, and carrying more than it was.** The panel shows what you own; only the facts say what it costs to touch it — on the row, at the head of the form, and now in the delete confirmation (E14). **That third reading is new on 2026-09-20 and the same day found the number wrong in two directions** (see the dated block below), so *unchanged* describes the sentence and not the load | The panel makes the corpus visible and the consequences invisible, which is a worse trade than the one §8 started from |

**And the two costs that replaced them, because a rewritten mitigation table that lists no new cost is
a table that stopped looking.** The item **renders twice** — panel row and set row — and only the set
row can be true about *detached*, *auto-added by X* and *conflicting*. And the **width** the Project
row needs for `item · rule · observed value` is now shared with a panel; that is measurable and belongs
to step 5.

---

### 3 · Global, contextual, deep

**The rule.** **Global** — on the surface at all times, because leaving it out would strand somebody.
**Contextual** — it appears where it can act, because §9's *an action that cannot act is not shown*
applies to navigation as much as to a toggle. **Deep** — reachable, out of the way, because the
evidence puts it far from anybody's week.

| Tier | What is in it | Why it is there |
|---|---|---|
| **Global** | **Library** (two scopes) · **Projects** | The only two places nothing else has to hand you. Everything else in the product is reached *from* one of them |
| **Contextual** | **Check** — on a Project with members; the seam (§8) · **Export** — Run's final stage, never a button beside the check · **Configure** — on a Project, the mode where the set is changed (Q14, amended 2026-09-20) · **the panel's scope switch and `kind` tabs** — inside that mode, where the corpus reaches the builder · **add / edit** — the Library's overlay · **export this item on its own** — on a Library row (Q15) · **delete** — on a Library row, confirmed with its usage count (Q17) · **Edit · Reset · Promote** — only on a **detached** row, since an override exists nowhere else (§5) · **agent target** — inside Run, where it selects the paths *and the reader* (E13) · **share / revoke** — on a project or an item · **copy into `My library`** — on a `Public library` row · **the usage count expanding** — on a Library row | Each one is a command with a subject. **Off its subject it cannot act**, and §9's rule says it is then not shown — with the one documented exception that **context menus grey rather than hide** (benchmark finding 7) |
| **Deep** | **Library import / export as JSON** — two commands on the Library, **the orphan**: §10 commits to it and **no job raises it** · **Promote a detached item** — *the thinnest demand of any mechanism in the specification*, and no prior art (E5) · **Revoke a share** — reversing a standing decision, and the product must say at that moment that revoking **recalls nothing already taken** (§5) · **Delete the example project** — once, ever (§11) | **Rarity is read off the evidence, not guessed.** Each of these is raised by no job at all, or by the thinnest evidence in the folder. **Deep does not mean hidden**: it means it does not compete with a command somebody uses weekly |

~~**`⌘K` is contextual, and the temptation to make it global is named here so it is not taken by
accident.**~~ **Superseded 2026-09-20, Q14 — and the warning it carried survives the change, pointed at
a different object.** The palette had exactly one job: the only way the library reaches the Project
screen. **The panel has the same one**, and the same temptation applies to it in a new form: **a panel
that also navigates — projects in it, recent things, a way to jump anywhere — would quietly become the
navigation this section just derived**, two entries on the surface and a hidden third way of reaching
everything. **The panel shows items, in the current scope and tab, and adds them. Nothing else.**
If a job ever asks for more, it is additive. **Nothing asks now.**

**And one thing the panel must not become, which the palette could not have been.** The Library is the
only place an item is edited (§8, Q14). **A panel that grows an inline edit is a second library**, and
two renderings that can both change things drift. The division is the decision: **the panel answers
*what goes in this set*; the Library answers *what do I own*.**

---

### 4 · What survives leaving, and what does not

**Decided in step 2b and restated here, because a navigation model is not complete without it.** **Back
from Run returns to the Project** — there is nowhere else it could go. **A reload during a check returns
to the Project and does not silently start a new one**, because a reload that re-runs is the product
making a choice nobody made — [EJ-1](../research/7-jobs-to-be-done/jtbd.md#ej-1--not-be-quietly-overruled-by-my-own-tools),
importance **3**. **The Library's scope is part of its address**, so a reload cannot drop you into the
room §11 guarantees is empty. **No finished run has an address** (E8), so nothing in this navigation may
promise a way back to yesterday's result.

**And one consequence this section inherits rather than causes.** The handover disclosure is read
**during** a run (§6) — it cannot be bookmarked, linked or navigated to. **Re-reading it means checking
again**, which is cheap because we run nothing. **No navigation may imply otherwise**, and a
*"handover"* entry anywhere would.

---

### What this section establishes, and what it does not

**Establishes.** **Two global entries**, each opening a named job cluster, with the third cluster
deliberately entry-less because its screen is a mode. **A floor of three clicks** from the first screen
to an archive, unchanged by whether the set exists, **four on the persona's most frequent arrival**, and
**two for the receiver**. **A three-tier split** whose rarity is read off the evidence rather than
guessed. And **the three §8 mitigations made accountable**, each with the row it pays for and what
breaks without it.

**Does not establish. Route strings** — the literal addresses — which are still step 3's, and which this
section constrains without writing: five places, two of them addressable off this machine. Nor **what
each surface is made of**, which is step 5, and which now has a warning waiting for it: the `Item`
overlay is carrying three disclosures nobody chose to put together.

---

---

## Traceability — every job against every surface

> **Written 2026-09-20, after the owner accepted the flows.** Not a numbered step: a **check across
> steps 2a, 2b and 3**, run the only way a coverage claim can be run — by putting both lists side by
> side and looking for the empty line. **Rows are every job in
> [`jtbd.md`](../research/7-jobs-to-be-done/jtbd.md)** — one main, four related, three emotional, two
> social, and the seven hypotheses in a block of their own. **Columns are every surface this file
> establishes**, screens and non-screens alike.
>
> **Why non-screens are columns.** A matrix of screens only would hand `Project` the ✓ that belongs to
> the library panel, and hand `Library` the one that belongs to the `Item` overlay. **The question is
> which surface does the work**, not which of them has an address. Each column says what kind of thing
> it is.
>
> **What a ✓ means, stated before the table so it cannot drift.** *This surface takes part in closing
> this job* — the person is on it while the job is being done, and something on it moves the job
> forward. **Being a route to the surface that does the work is not participation**, or every column
> would be full and the exercise would return nothing.

### The matrix — sourced jobs

**P1** is the primary persona's importance, from `jtbd.md` §7. Surfaces: **`L-my`** `My library` ·
**`L-pub`** `Public library`, the shelf · **`Item`** the add/edit overlay · **`Pj`** Projects ·
**`P-v`** Project, viewing · **`P-c`** Project, configuring · **`Pan`** the library panel ·
**`Det`** the detached row · **`Run`** · **`Sh-p`** shared project · **`Sh-i`** shared item ·
**`JSON`** library import / export.

| Job | P1 | L-my | L-pub | Item | Pj | P-v | P-c | Pan | Det | Run | Sh-p | Sh-i | JSON |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **MAIN** — make it keep working somewhere else | **3** | ✓ | | | ✓ | ✓ | ✓ | ✓ | | ✓ | ✓ | ✓ | |
| **RJ-1** — know what the other side needs | `[?]` | ✓ | | ✓ | ✓ | ✓ | | | | ✓ | ✓ | ✓ | |
| **RJ-2** — what it drags in, where two fight | **3** | ✓ | | ✓ | | ✓ | ✓ | ✓ | | ✓ | ✓ | ✓ | |
| **RJ-3** — fix it once, reach every copy | **3** | ✓ | ✓ | ✓ | ✓ | ✓ | | | ✓ | ✓ | | | |
| **RJ-4** — move the work, not the secrets | **2** | ✓ | | ✓ | ✓ | ✓ | | | | ✓ | ✓ | ✓ | |
| **EJ-1** — not be quietly overruled | **3** | ✓ | | ✓ | ✓ | ✓ | ✓ | | | ✓ | | | |
| **EJ-2** — believe a clean result was earned | **2** | | | | ✓ | ✓ | | | | ✓ | ✓ | ✓ | |
| **EJ-3** — stop suspecting half is dead weight | **3** | ✓* | | ✓* | | | | | | | | | |
| **SJ-1** — not be the missing manual | **2** | | | ✓ | | ✓ | | | | ✓ | ✓ | ✓ | |
| **SJ-2** — something I would put my name to | **1** | | | | | | | | | | | | |

`✓*` — **partial by construction, not by omission.** See EJ-3 below.

### The matrix — hypothesis jobs

**Kept in a block of their own**, because `jtbd.md` forbids citing them as findings and **four
specified features close nothing else.** A column standing only on this block is a column standing on
an assumption, and that is a defect of a third kind.

| Job | P1 | L-my | L-pub | Item | Pj | P-v | P-c | Pan | Det | Run | Sh-p | Sh-i | JSON |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **H-J1** — lay hands on something I wrote | **2** | ✓ | | | | | | ✓ | | | | | |
| **H-J2** — start from one I have done | `[?]` | | | | ✓ | | | | | | | | |
| **H-J3** — change one copy for one project | **2** | | | | | ✓ | ✓ | | ✓ | | | | |
| **H-J4** — get moving with somebody else's | `[?]` | | ✓ | | ✓ | | | ✓ | | | | ✓ | |
| **H-J5** — watch what actually ran | **3** | | | | | | | | | | | | |
| **H-J6** — my work counts as something | — | *the same job as SJ-2 in functional wording; not counted twice* | | | | | | | | | | | |
| **H-J7** — the unwritten half travels too | **2** | | | ✓ | | ✓ | | | | ✓ | ✓ | ✓ | |

---

### Defect 1 · Orphan columns — a surface with no job

**One, and it is the one already carrying the mark.**

**`JSON` — library import / export.** Empty in both tables. `CLAUDE.md` §10 commits to *export and
import of the whole library as JSON*, and **no job in either block raises it.** The entity inventory
named it an orphan on 2026-09-15 and step 2b reduced it from a screen to **two commands on the
Library**; this matrix is the third instrument to reach the same answer independently, which is worth
more than any one of them.

**One thing must not be mistaken for coverage.** [`flows.md`](flows.md) RJ-4 draws a path through it —
*the whole library as JSON?* → the keys warning. **That is exposure, not closure**: the flow passes
through this surface because material can get in that way, and the job it serves is *move the work
without moving the secrets*, which the warning closes and the JSON route only complicates. **Counting
it as a ✓ would launder an orphan into a feature.**

~~**Resolution: keep as two commands, in the deep tier, with a named trigger for removal.**~~
**Settled 2026-09-20 by the owner, and the answer overturns the question rather than the finding
(Q18).** The finding stands exactly as measured: **no job raises it.** What changed is the standing of
that measurement. **Coverage was measured against jobs, and this mechanism does not stand on one — it
stands on §10.** Storage is **IndexedDB with no backend**, so the only copy of everything a person has
accumulated sits in **one browser profile**, which clears. That is a property of the architecture, not
somebody's stated need, and **no instrument pointed at people was ever going to find it.**

**So it keeps its place, and its entry keeps its honesty**: the column is empty, the mark changes from
`[orphan]` to `[§10]`, and the sentence to remember is **it is not unjustified, it was being measured
with the wrong instrument.** Half of its old justification did go: *informal sharing before any server
exists* is what a share link does now (Q13). **What is left is durability, and that is enough.**

**One thing this does not license.** It remains in the **deep** tier and gets no more design than two
commands need. A warrant is not a promotion.

### Defect 2 · Orphan rows — a job with no surface

**Two, and they fail in opposite directions. Neither is fixed by adding a screen, and saying so is the
result rather than an excuse.**

**`SJ-2` — have something I would put my name to.** Importance **1** for P1, the lowest in the base,
and `jtbd.md` marks it **post-MVP** in its own heading. `§9` refuses the catalog; the closest thing in
the product, a **share link**, is deliberately *a handover, not a portfolio* — unlisted, unranked, not
browsable. **The row is empty because the product declines the job, in writing, twice.**

> **Resolution, settled 2026-09-20 (Q23): backlog, and the empty row is correct.** It is the only row
> in this matrix where emptiness is a decision already taken rather than a gap discovered here.
> **What this exercise adds is one caution, and it is now written into §9 rather than left here**:
> `SJ-2` and `H-J6` are the same job in two wordings, and `jtbd.md` says not to count it twice.
> **The first is easy to refuse and the second is not.** So a proposal for a profile, a listing or a
> place where work is *visible* is this refusal being tested in functional clothing, and the caution
> lives next to the refusal it protects.

**`H-J5` — watch what actually ran.** **Importance 3, and this is the serious one.** It is the
**surviving second main-job candidate** — the one `jtbd.md` §1 says makes two products — and
`CLAUDE.md` §6 cannot close it: **we run nothing on anybody's machine.** The sitemap has already
refused the screen that would answer it, under *What is not a screen*: *"the job is real and the screen
is forbidden, which is Q12."*

> **Resolution, settled 2026-09-20: Q12 is closed as *refused*, not deferred, and it moves into §9.**
> **The screen is forbidden rather than missing**, and the distinction is the whole point: a product
> that drew it would be promising a runtime it does not have, which is the unearned tick §6 spends a
> section refusing. **This is the highest-importance job in the product that no surface touches, and
> the matrix is the first document to state it as a number** — 3, with a row of twelve blanks under it.
>
> **Why it is closed rather than deferred a second time.** The answer cannot change without a runtime
> the MVP will never have, and **an open question at importance 3 gets asked again on every surface in
> lessons 04 to 09** — *should this show what ran?* — which is a tax with no possible payoff. Stage 7's
> method says two surviving main-job candidates mean **two products**; this is the other one, and
> naming it that is cheaper than carrying it. **The nearest honest thing is already shipped and must not
> grow**: *last exported 12 days ago* reports what **this product** did, never what an agent did
> afterwards.

**Both stay empty on purpose. The instruction this exercise was given asks for no empty row or column,
and two rows cannot honestly be filled** — one because the product declines the job and one because it
is incapable of it. **Inventing a ✓ for either would make the matrix a decoration.** Every orphan has a
decision, which is the part that was reachable.

### Defect 3 · The defect the exercise was not looking for — surfaces standing on assumptions

**A column is not safe because it has a ✓. It matters which block the ✓ came from.**

- **`L-pub`, the shelf — two ✓, and only one is from a sourced job.** `RJ-3` reaches it through a
  single branch (*copy it into mine to make it fixable*), and everything else it carries is **H-J4,
  whose importance is `[?]` in all three persona columns.** `CLAUDE.md` §11 commits to it, §8 gives it
  a scope switch, the panel now carries it into assembly, and lesson 03 has made it more load-bearing
  three times without it gaining a single point of evidence. **Not an orphan; the thinnest column in
  the product**, and E3 already says so in its own words.
  **Settled 2026-09-20 (Q19): build the content in full, design the surface only as far as the example
  project needs.** The ~30 items with provenance and licences are built — **content is what makes an
  architecture arguable** — and **browsing, sorting, ranking and recommending get no design until Q9 has
  an answer.** A surface that keeps getting heavier without getting better founded is where design
  effort goes to be wasted, and this is the one place in the product where that is measurably
  happening. See `CLAUDE.md` §11.
- **`Det`, the detached row — two ✓, one sourced.** `RJ-3` at importance 3 carries it, and `H-J3`
  supplies the rest. That is enough, and it is worth knowing it rests on one number.
- **`Pan`, the library panel — four ✓, two of them MAIN and RJ-2 at importance 3.** Well founded, which
  is worth recording given how recently it was added and how much it now carries.

### Defect 4 · One row whose ✓ do not mean what the others mean

**`EJ-3` — stop suspecting that half of what I keep is dead weight.** Importance **3**, and it has two
ticks, both marked `✓*`. **Usage facts answer *is it used*; they do not answer *did it change
anything*.** E14 says this in its own entry and the honest reading of the row is: **the product touches
this job and cannot close it.** It is the same family as `H-J5` — Q12 — and the two together are the
product's ceiling written as a matrix: **two of the four importance-3 emotional and hypothesis jobs are
beyond what a thing that runs nothing can do.**

> **Resolution, settled 2026-09-20 (Q22): accept it, and write the ceiling beside the facts
> themselves.** Not in a research file where nobody building a screen will meet it — **in `CLAUDE.md`
> §5, next to *used in 3 projects*,** so that the sentence *these answer* is it used, *not* is it any
> good *is read by whoever draws the row.* **Nothing is added to the facts to close the gap**: the
> obvious extension — counting exports, or whether an item was ever in a checked set — is still
> *used*, and would read as *useful*, which is the decoration §5 refuses two paragraphs later.

### What the matrix found that nothing else had

1. **`Run` and `P-v` are the busiest columns, and `Sh-p` is third** — the receiver's surface carries
   seven jobs, which is more than `Projects` and more than the panel. **A surface built for somebody
   who has never spoken in the first person is doing a third of the product's work**, and the evidence
   under that person is the thinnest in the folder. Not a defect; the largest exposure on the board.
   **Settled 2026-09-20 (Q20) as a design constraint rather than as a worry**: on the two shared
   surfaces, **invent nothing that is not derived from what P1 needs.** Where a choice has no answer in
   P1's evidence, take the one that **shows more and promises less**, and mark it. **Do not design for
   a person nobody has met** — which is trap 3 in this lesson's own plan, and this is the column where
   it would be easiest to spring. Written into `CLAUDE.md` §8.
2. **`P-c`, configuring, is thinner than expected — four ✓.** It was added hours before this matrix and
   it does the work of assembling; most of what it enables is scored against `P-v` and `Pan` because
   that is where the person is looking. **If configuring ever needs to justify itself, this is the row
   count it will be asked about.**
3. ~~**`H-J3` needs a mode this file has not assigned it.**~~ **Answered the same day, Q21.** The
   detached row's **Edit, Reset and Promote** are changes to the set's content, and by the rule stated
   for the `✕` — *a row being read is not a row being changed* — **they live in configuring.** The
   alternative was put and rejected: a detached row as an exception to the rule would mean a viewing
   mode that can change the set, which is not a viewing mode. **The cost is one entry into configuring
   for somebody who spotted the difference while reading**, named rather than absorbed.

---

---

## Where the day's decisions meet each other

> **Written 2026-09-15 as a re-check, after four decisions landed in one day.** Each was recorded
> where it belonged. **This section is the part that no single decision owns: what they do to one
> another.** Three interactions, two of them settled here and one that needs an answer.

### 1 · A live shared page meets a verdict that can be void — **answered: the receiver checks it**

**The collision.** A project's check verdict is **void the moment the set changes** (§6, the run is a
moment). A shared page is **live** (§5, *Sharing*). So the ordinary case is: the owner checked on
Monday, edited an item on Tuesday, and **the person who opens the link on Wednesday is looking at a
set that has never been checked in the state they are seeing.**

**Why it cannot be waved through.** This is the exact situation the handover evidence is about. In the
one behavioural test ever run here, three receiving agents were handed a set whose defects were not
disclosed: **one found them, one mis-resolved one on a false claim, and one saw none.** A page that
shows a set and says nothing about whether it coheres reproduces that test on purpose.

**Three answers are available and they are not equivalent:**

| | What the page does | What it costs |
|---|---|---|
| **a** | **Says nothing about the check.** | The receiver is in Q-F's position, which we have measured and which went badly two times in three |
| **b** | **Shows the owner's last verdict, with its date, and says plainly when it no longer applies.** | Honest and cheap, and it is §6's existing rule — *the date survives, the verdict does not* — pointed at a second reader. But it leaves the receiver with *nobody has checked this*, and no way to find out |
| **c** | **Computes the findings when the page is opened**, so what the receiver reads is about the set in front of them. | It is the same check over the same data, and it makes the page answer the receiver's actual question. **It is also close to the pending proposal S-1** — *`SETUP.md` should carry the set's Problems* — which is not applied, so taking it here would be deciding a shape the register has not sat on |

**Answered 2026-09-15, and none of the three was the answer. (d): the receiver runs the check
themselves.** The question that produced it was *why can the person holding the link not just check
it?* — and there is no reason. **We nearly invented an obstacle out of our own classification**: Run
is a mode of the *Project*, and the Project is the owner's place, so the receiver's side looked
closed. That was a description of the owner's surfaces being read as a law.

**Nothing prevents it.** The check walks `requires`, compares `conflicts`, looks for duplicate command
names and shared target paths, and collects `needsEnv` **names** — every input is data the shared page
already carries. No machine is touched, nothing is revealed that §6's sharing disclosure did not
already make visible.

**And it is better than (c), the page computing quietly.** The validation pass is specified as **a
designed moment rather than a spinner**, and the person who most needs that moment is the one who
wrote none of this. It also settles the staleness properly: with the page live, **the only verdict
worth anything is the one taken now by the person looking at it.** (b)'s honesty survives as facts
rather than as a substitute verdict — the page states **when the owner last checked and whether the
set has changed since**, because Q-F says a receiver who digs is the exception.

**The ceiling is unchanged and it matters more here.** Their check answers *does this set cohere*, not
*will it run on my machine* — `needsEnv` holds names, and what exists over there is a fact about a
machine we never touch. **Checked, never works**, for the reader who has no other source of
reassurance.

**And nothing is stored for them at all.** §6 puts the verdict on the **project**, and a visitor owns
none — so their run is a moment with nothing left behind, which is the same rule one step further.

### 2 · The archive a visitor takes is built from the live set — **settled**

A shared page offers **a way to take it** (§8), and nothing is stored: there is no archive sitting
anywhere from the owner's last export. **So what a visitor takes is built from the set as it is when
they take it** — the live one, not the one the owner exported last week.

**That is consistent rather than awkward**, and it makes §5's sentence about the two artefacts exact:
**the link is live, the archive is a snapshot** — *the snapshot is taken at the moment somebody takes
it.* Two people who follow the same link a week apart may hold different archives, and **each holds
one that matches what the page said when they took it**, which is the property that matters.

### 3 · A shared item carries its licence — **settled, and it is why the field went in**

The licence was added to `Item` on the same day, hours before Q13 was answered, **on a legal basis and
with no job behind it** (E15). Sharing is where it pays: **a shared item may be somebody else's work
being passed onward**, and the page carries `repoUrl`, the pinned `ref` and the licence. A decision
taken for one reason turned out to be load-bearing for another, and that is worth recording rather
than enjoying quietly.

### ~~And one thing that still owes a mechanism~~ — built 2026-09-16

~~**Q10 was answered and has nowhere to live yet.**~~ **`defersTo[]` is now a field on `Item`** (§5,
*Deference*), raising a **Note** on the item's row (§6) and read on the shared page (§8) and in
`SETUP.md` (§6). The reasoning is unchanged and is now written into the specification rather than owed
by it: detection is impossible — §9 parses nothing, the other machine is never ours — so the field
**discloses a constraint the user declared and compares nothing.** **No disposition from the sitting is
owing a mechanism now.**

---

## 2026-09-16 — three decisions, and they land on the same surface

> **A second re-check, one day after the first.** The owner overruled the credential refusal, took
> Q10's mechanism as a Note, and kept §8's form. **Recorded separately because what they do together is
> not what any of them does alone.**

### The `Item` add/edit overlay is now the product's busiest disclosure surface

**It was described as *a form* and left at that.** After three decisions it carries, in order:

1. **On the way in — *check that these files carry no keys*** (E2, §11). The refusal moved here, so
   this overlay is the **only** place the product speaks about secrets before the material is inside.
2. **Before an edit — the blast radius** (E14, §5): *used in 3 projects · saving un-checks all three*.
   It landed here because the `Item` place that would have held it was not built.
3. **As a field — `defersTo`** (E7, §5): the thing this item answers to outside the library, which
   nothing else in the product can discover.

**A fourth thing arrived on 2026-09-20, and it is a door rather than a disclosure.** The library
panel's **row that creates** — a zero result offering to author the missing item — opens **this
overlay, over the Project** (Q14). The panel never edits, and this is not an exception to that: it
**summons the authoring surface** rather than becoming one, because creating is a corpus act. **But it
is the overlay's third door**, after the Library row and the Library's *add*, and it is the first one
reached from **inside assembly**. The person who arrives through it is mid-set, not mid-curation, and
**every disclosure listed above is waiting for them there.**

**That is the finding, and it is a warning for step 5.** Two of the three were re-homed here *because a
place was refused*, and nobody decided that this overlay should carry them — **it is where they fell.**
An overlay is summoned and dismissed, it is not addressable, and **a person cannot be sent to it to
read any of this.** It works, and it is thin ice: **step 5 must compose this surface deliberately
rather than let three unrelated disclosures stack up in a dialog.**

### And one count that can never reach zero

A deference raises a Note **that never clears** (E9), and a project's row carries `checkVerdict` as
**counts** (E4, §6). So a project holding three deferring items reads `0 problems · 3 notes` **for as
long as it exists**. **Nothing is wrong with it and nothing can be done about it**, which makes it the
first verdict in this product that is not a to-do list. **Projects and Run must not draw notes as
work outstanding** — and this is the case that proves the rule, not an edge of it.

---

## 2026-09-20 — the panel, and what it moved

> **A third re-check, four days after the second.** The owner replaced the builder's adding mechanism,
> took the Library off the assembly path, let a single item leave on its own, and settled the empty
> project and the delete. **Recorded here because what they do together is again not what any of them
> does alone.**

### The architecture survived its biggest mechanical change without gaining a place

**The palette was an overlay; the panel is a region of `Project`.** Between them sits the whole way the
corpus reaches the builder, and **the place count did not move**: five, exactly as on 2026-09-16.
That is not luck and it is not a boast — **it is what the four tests are for.** The panel fails *place*
(a reload restores the Project, not the panel), fails *mode* (it takes no surface, and there is nothing
to leave), and fails *overlay* (it covers nothing and dismisses to nothing). **A thing that fails all
three and is still on the screen is a region**, and regions are composed in step 5, not navigated in
step 3.

**Amended the same day, during the owner's review of the flows: the panel lives in a mode.** The
Project screen is *viewing* or *configuring*, and the panel, the checkbox and the `✕` exist only in the
second. **That adds a mode and no place** — still five — **and it moves a number this section had
called immovable**: path B is four clicks, because the empty state's one action is the entry into
configuring. **The fourth click is a mode entry, not a traversal**, so the finding it sits under
survives with a corrected number. **`Run` stays reachable from both modes**, which is derived rather
than decided: the fix-and-recheck loop would otherwise pay an exit every cycle.

**What step 3 inherits is two sharpened questions.** Whether the configuring mode survives a reload —
the honest default is `Run`'s, which is *no* — and this one: The Library's scope is **part of its
address**, because a reload must not drop you into the room §11 guarantees is empty. **The panel now
has a scope of its own**, and on first run it is the shelf that carries the material. So: **does the
panel's scope — and its tab — belong in the Project's address?** The argument that settled the Library
applies here word for word, and step 3 should not have to rediscover it.

### The panel absorbed a detour and inherited a debt

**What it absorbed.** In the main flow, a palette that matched nothing sent the person to `Library`, on
to `Public library`, and back — **three screens of detour in the middle of assembly**, drawn honestly
because it was real, and existing only because the palette searched one scope. **A scope switch inside
the panel ends it.** The person does not leave the Project. That branch is gone from
[`flows.md`](flows.md), and **it is the first time a decision has removed a path from these diagrams
rather than adding one.**

**What it inherited.** The panel is now **the only corpus surface the builder has** (Q14, D2). The
palette was one channel among the Library's; the panel has no fallback behind it, because the fallback
*was* the Library and assembly no longer goes there. **Load-bearing is the right word and it should be
read as a warning**: every weakness of the panel is now a weakness with nowhere to route around it.

### One number, three surfaces, and now two directions

**E14's *used in 3 projects* is read in three places** — on the Library row, at the head of the
add/edit form before an edit, and, since today, in the **delete confirmation** (Q17). The open question
that [`flows.md`](flows.md) found — **the count includes detached copies, which by design do not
receive a fix** — was one-directional when it was found. **It is not any more.**

- **Before an edit, the count overstates the reach of the fix**: one of the three will not get it.
- **Before a deletion, the same count overstates the damage**: a detached row holds its own
  `overrides` and may lose nothing at all — **though whether it survives the deletion is itself open**
  (Q17).

**One number cannot be wrong in two directions and still be one number.** That is a step 5 finding with
a sharper edge than the one it came from, and it is recorded here rather than left to be met twice.

### And the product's first shown-but-disabled action

**An empty project disables `Check` and `Export`** (Q16). This architecture has been built on *an
action that cannot act is not shown*, and §6 refuses a greyed primary control in the strongest terms it
uses anywhere. **The exception holds because §6 supplied the test itself**: the three conditions it
used to excuse Figma's `0 of 0 selected` — the blocker is one named action away, it is a property of
this second rather than of the document, and re-doing it costs nothing — **are all three true of an
empty project, and none of them is true of a set with Problems.**

**The consequence for this section is small and worth writing down.** *A project with no members* was
already classified as a **state** (see the classification), and it stays one. **What changed is that
the state now has a defined composition**: one action in the body, and two primary controls visible
and inert. **The action points at the panel, which is already on the screen** — so it exists to say
*what to do*, not to reach anywhere, and step 5 should not draw it as navigation.

---

## What this section establishes, and what it does not

**Establishes.** **Sixteen entities, each with a job and a link to it** — fifteen on the first pass
and **E16, the shared link, added the same day when Q13 was answered** — and **eleven candidates
refused for a stated reason**, of which one, the licence, was promoted by an owner's decision rather
than by evidence and is recorded as such in both places. Three relations, not one: most of this product belongs to its owner,
**three entities exist for the receiver** — the archive, `SETUP.md` and the agent target — and **one
points at an external author**.

**And two findings that were not visible before the objects were laid out side by side:**

1. ~~**§5 has no object for the check or for a finding**, and §8 gives the check an entire surface, so
   *does a run persist* has no answer anywhere.~~ **Raised and answered the same day, 2026-09-15: the
   run is a moment.** Nothing is stored; the project keeps when it was checked, what the check found
   as counts, and against which target, and **that verdict is void as soon as the set changes.** §5,
   §6 and §8 carry it. **It was a gap rather than a disagreement** — the architecture could not be
   drawn without an answer, which is why it did not wait for a sitting.
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

**And the screen tree establishes six screens and one orphan, plus four nodes that are not screens**
(*two until the library panel and the configuring mode arrived on 2026-09-20*) —
four for the owner and **two for the receiver, added when Q13 was answered**; the two non-screens are
the `Item` add/edit overlay (§8, kept 2026-09-16) and the detached row. Each screen carries the job it
serves, grouped
by the person's own three situations rather than by anything that could become a menu. **Its two
findings are refusals rather than places, and one is now under review:** the receiver needs **no screen
in the product as specified today** — their whole surface is `SETUP.md` inside the archive — **which
holds only while a shared link is out of scope, and that is Q13** in
[the register](../research/research-plan.md); and the highest-importance job the primary persona has is
one **no screen may serve**, because a dashboard of *what is working* promises a runtime §6 does not
have.

**And the classification answers the two questions the tree raised.** ~~**`Item` is a place**~~ —
**`Item` is a form, decided by the owner on 2026-09-16: §8 stands.** The argument for a place was a
count that needs somewhere to lead and an edit with blast radius that needs somewhere to stand; it was
raised as a **proposal to §8** and rejected. **The count now expands in place on the Library row and
its project names lead to the Project, and the radius is disclosed at the head of the form** — a
weaker answer than a place, named as weaker, and the only one available without one. **`Run` is a mode
of the Project, not a place** — it fails two of the three tests because nothing is stored, and taking
the whole surface is not the same property as being addressable. **Five places in the whole product**:
Library with an address per scope, Projects, Project, and the two the link creates.

**And one field was added to this inventory after it was written.** **`defersTo` on E1** — Q10's
mechanism, built 2026-09-16 — which is the only object here that **points outside everything the
product can see**, and therefore the only one whose finding is carried rather than computed. It left
*In question* as Q-E7 the day §5 and §6 took it, the way the licence left as Q-E5 the day before.

**A third finding, and it came from the decisions rather than from the objects.** The `Item` overlay
now carries **three unrelated disclosures** — keys on the way in, blast radius before an edit, and a
declared deference — **two of which were re-homed there because a place was refused, and none of which
anybody chose to put there.** It is written up above as its own section, because the thing to avoid in
step 5 is a dialog that accumulated its contents by default.

**Does not establish. Routes** — the strings themselves, and what each promises — which is step 3. Nor
the shape of E1, which proposal **S-2** would change from a file to a directory, and which the sitting
has not decided.
