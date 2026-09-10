# FINAL — the closing document of the research phase

Written 2026-09-01, closed 2026-09-02. **The five-stage research phase is signed off.** Read this
instead of re-reading everything: it is what the phase produced, what it decided, and how the six open
questions were settled in the sitting of 2026-09-02.

**Updated 2026-09-07.** The phase was re-opened on 2026-09-06 with stages 6 and 7, and stage 6 is
now under way. **Section 6 below is the current state** — what exists, what the evidence rule now is,
and the four things in this document that have since been shown to be narrower than they read.
**Updated again 2026-09-10:** round 3 was run, two of those four narrowings are now measured rather
than inferred, and the one row this file said we could close ourselves is closed.
Nothing here is retracted.

Three documents govern this folder and none of them repeats another:

| | Holds |
|---|---|
| [`research-plan.md`](research-plan.md) | **Status.** The five stages, what each was for, and the register of open questions with their IDs. The source of truth for *what is done*. |
| **`FINAL.md`** (this file) | **The close.** What the phase produced, what it decided, how the six questions were settled and on what reading, and the documents that cut across stages. |
| [`CLAUDE.md`](../CLAUDE.md) | **The spec.** Decisions only, in product terms. Nothing here overrides it; everything here explains it. |

---

## 1. What the phase produced

```
research/
  research-plan.md      the spine — stages, status, the register
  FINAL.md              this file
  1-landscape/          stage 1 — who else is here
  2-flows/              stage 2 — twelve mechanisms captured from live products
  3-pain/               stage 3 — the first evidence about users
  4-benchmark/          stage 4 — a rubric, and 15 cells scored against it
  5-patterns/           stage 5 — five shapes for the key flow, one chosen
```

| Stage | What it answered | The one thing that changed the spec |
|---|---|---|
| **1 Landscape** ([`1-landscape/README.md`](1-landscape/README.md)) | Who else is in this space, on five axes, with 38 captures | The market has converged on **measured trust** — Tessl scores every skill, Smithery every server — and we cannot measure anything. Hence: usage facts, never a score (CLAUDE.md §5). |
| **2 Flows** ([`2-flows/README.md`](2-flows/README.md)) | Twelve mechanisms, ten closed, one declined, one handed forward | Figma models overrides precisely enough to offer `Reset fill` **by name** and then draws a modified instance identically to a clean one. The drift indicator is a **display** problem, not a modelling one (§7). |
| **3 Pain** ([`3-pain/README.md`](3-pain/README.md)) | What actually hurts, from two public trackers | Our thesis is **real and quiet** (13 reactions) while the loud pain is environmental (**182**). Everything downstream is weighted by this. **Two corrections since — see §6.** The loudest is **6,592**, not 182, and the reassembly friction stage 3 called invisible **is** filed, as feature requests. |
| **4 Benchmark** ([`4-benchmark/README.md`](4-benchmark/README.md)) | Who does each of our four flows best, and how well | Blocking is a choice almost nobody has to make. Terraform never refuses, npm refuses and prices the override, Figma disables and sign-posts. We confirm rather than refuse (§6). |
| **5 Patterns** ([`5-patterns/README.md`](5-patterns/README.md)) | What shape the key flow takes | **The library leaves the builder and drag stops being the verb** (§8). Held as provisional until the sitting below; **it survived unchanged.** |

## 2. Decisions taken, and where they live

All in CLAUDE.md, which is the source of truth. The reasoning and the rejected alternatives are in
[`1-landscape/comparison.md`](1-landscape/comparison.md) and in the stage documents.

| Decision | Answer | Spec |
|---|---|---|
| Does `visibility` appear in the MVP interface? | No. The field stays, the control is not shown. | §9 |
| What evidence does an item card carry? | Usage facts from the library. Never a score, rating, eval result or badge. | §5 |
| Does anything read `version`? | The field is cut; external references gain a pinned `ref`. | §5, §9 |
| Does the validation pass block, or grade? | Neither. Three severities, and export is never disabled — an unclean set is confirmed. | §6 |
| What shape does the key flow take? | Command-first assembly, run-centric check ending in export. **Confirmed 2026-09-02** — no answer added a surface. | §8 |
| Does a public, curated library ship with the MVP? | Yes, read-only, behind a scope switch beside `My library`. Plus one example project. | §8, §9, §11 |
| Who reads `SETUP.md`? | The agent that opens the project. It sets the project up from what the document states. | §6, §8 |
| Can a detached item be edited inside the project? | Yes — without it, detach is only unlink. | §5, §7, §8 |

Two contradictions inside the spec were closed on the way: `version` was both reserved-and-unread
and expected to produce conflicts; `conflicts` was to be hard or soft with no field able to say
which. A third correction went the other way — a cycle in `requires` is not a defect at all, because
a project is a set and not an execution order.

---

## 3. The sitting — 2026-09-02, and what the six questions became

Worked through in one sitting, as the protocol required. **Four answered, two deferred with a stated
reason.** Each entry below keeps what was read before deciding, then records the decision and what it
cost. The status table lives in the register at the end of
[`research-plan.md`](research-plan.md); this section holds the reasoning.

| | Question | Disposition |
|---|---|---|
| **Q1** | Cold start | **Answered** — a scope switch, plus one example project |
| **Q2** | The weight of `SETUP.md` | **Answered** — and the recipient turned out to be an agent |
| **Q3** | Project inside a project | **Deferred**, not refused — recursion |
| **Q4** | Promoting a detached item | **Answered** — a new item, and editing comes with it |
| **Q5** | Loss or reassembly cost | **Deferred** — accepted risk, trigger written down |
| **Q6** | Styling engine | **Deferred** to lesson 08, design tokens; criterion recorded |

**No answer added a surface**, which is the thing this sitting was most at risk of. Q2 lands as two
more stages inside Run, and Run is already a stage list. Q1 lands as a scope switch inside Library,
and Library is already a browse screen. Q4 lands as a command on a project row, exactly where stage 5
predicted. §8 therefore stands as written, and the *provisional* marks are gone.

**Two answers widened the MVP**, and both are recorded as scope rather than smuggled in as detail: a
curated public library ships with the product, and `SETUP.md` becomes a real artefact rather than a
one-line courtesy.

### Q1 — Cold start: answered, and none of the three drafted options

**What was read.** [`2-flows/08-empty-state-and-cold-start/NOTES-linear.md`](2-flows/08-empty-state-and-cold-start/NOTES-linear.md)
— the four seeded issues, and the rule that picks between three registers of emptiness (never-used
concept → define it · routine → one line · filtered to zero → count what is hidden).
[`4-benchmark/NOTES-obsidian.md`](4-benchmark/NOTES-obsidian.md) and
[`4-benchmark/NOTES-vscode.md`](4-benchmark/NOTES-vscode.md) for the empty query that becomes the
create row, and `@recommended` split into counted sections.
[`5-patterns/patterns.md`](5-patterns/patterns.md) — **three of the five shapes are broken without a
seed.**

**The three options on the table were (a) seed the library, (b) demo content behind a button,
(c) empty with a strong empty state. The answer taken is none of them, and it is better.**

> **The Library gains a scope switch: `My library` / `Public library`.** Visually identical, same
> search, same filters by kind and tag. One holds your things. The other holds a curated set that
> **ships with the application** — skills, agents, prompts, MCP servers, taken from sources we have
> checked — and it is **read-only**: you add from it into a project, or copy it into your library,
> and you cannot publish into it.

This dissolves the question rather than answering it. Option (a) put someone else's material into a
space labelled *mine*, which is a small lie told on the first screen. Option (c) leaves the
validation pass with nothing to run on. The switch gives the product material from the first second
**while `My library` starts honestly empty** — and an empty `My library` is then the cheap register
of emptiness, one line, because the concept has already been taught by the shelf beside it.

**One thing the switch does not deliver, so it is bought separately.** A public shelf guarantees
material; it does not guarantee that the first check says anything. A user who picks three unrelated
items gets six green ticks, and the recommendation this section carried into the sitting stands: *a
first run showing six green ticks teaches nothing about what the product is for.* So **one example
project ships in Projects**, built entirely from public items and composed so that it contains **at
least one Problem and at least one Note** — a real target-path collision, a genuinely missing env
key. Labelled as an example, deletable, and honest about being one, because it sits in Projects
rather than pretending to be the user's own work.

**Two consequences to carry into design, and neither is decided here.**

- **Provenance.** Public items are other people's work. Each carries its origin — `repoUrl` and a
  pinned `ref` — which the data model already has, and the design owes them visible attribution.
- **Staleness.** With no server the shelf ages. The pinned `ref` makes that honest rather than
  broken: it says *this is the version we checked*, not *this is current*.

**Changed:** CLAUDE.md §8 (the Library bullet), §9 (consuming a public set is in; publishing to one
is still out), §11 (the starter catalog moves from *later* into the MVP).

### Q2 — `SETUP.md`: answered, and the recipient is not who §6 assumed

**What was read.** [`3-pain/user-pain.md`](3-pain/user-pain.md), finding 1 — *MCP Servers Don't Work
with NVM*, **182 reactions**, over a top-of-tracker made of PATH, node version managers, platform
paths and processes dying at startup. [`4-benchmark/benchmark.md`](4-benchmark/benchmark.md) — the
four B4 cells (**nobody above 4**), finding 8, and the finalisation's gap: every cell scores what a
product says about its own state, none about the machine its artefact lands on.
[`2-flows/06-export-and-target-adaptation/ruler-per-agent-output.md`](2-flows/06-export-and-target-adaptation/ruler-per-agent-output.md)
and [`4-benchmark/create-next-app-output.md`](4-benchmark/create-next-app-output.md) — the same two
distribution mechanics from unrelated vendors. [`2-flows/07-env-and-secrets/NOTES.md`](2-flows/07-env-and-secrets/NOTES.md).
[`1-landscape/continue-postmortem.md`](1-landscape/continue-postmortem.md).

**The answer is option (1) — disclose the handover inside Run — with one correction that changes
what the document is for.**

> `SETUP.md` is **addressed to the agent that opens the project**, not to a human who reads it. It
> states, per item in the resolved set, what that item requires: its dependencies, the MCP servers it
> needs, the env keys it expects, the external repos to clone **at their pinned `ref`**, and where
> everything lands for the chosen agent target. On project init the agent reads it and performs the
> setup.

That correction is worth more than it looks. The prep sheet framed the choice as *own the problem
(emit a verify script) or say it is not our war*, and both framings assume the receiving end is a
human running commands. It is not: the archive is opened by Claude Code, Cursor or Codex, and those
are the readers. Writing for them is **cheaper than a verify script and aimed at the same 182
reactions** — no platform matrix, no script to maintain, no new artefact. And it explains why the
agent target selector already sits in Run: the target does not only choose paths, it chooses the
reader.

**What this does not include.** No verify script in the MVP. Option (2) stays additive — the export
is designed so that emitting one later is a new stage, not a rewrite. And we still run nothing on
anyone else's machine; we write instructions precise enough to be executed by something that can.

**Where it lands.** Run's last stages, before Export: what the archive contains, and what the
receiving machine must still do — `SETUP.md` preview, pinned `ref`s, target-correct paths,
`.env.example`. Read **before** Export is pressed, which is the C2 behaviour the rubric asks for.

**Changed:** CLAUDE.md §6 (the export subsection) and §8 (the Run bullet).

### Q3 — Project inside a project: deferred, not refused

**What was read.** [`3-pain/user-pain.md`](3-pain/user-pain.md), finding 4 — `reuse blocks
assistant`: **0 results** in a 6,677-issue tracker belonging to a product that shipped a hub for
exactly this. [`1-landscape/continue-postmortem.md`](1-landscape/continue-postmortem.md) — the
`uses`/`with`/`override` primitive, and which half of that product was switched off.
[`5-patterns/patterns.md`](5-patterns/patterns.md) — **no variant needed composition to work.**

**Out of the MVP. Items only — but recorded as deferred rather than closed**, because the reason for
holding it back is also the reason it stays interesting: composition is a real feature and it
**risks unbounded recursion**. A project containing a project containing a project is a resolution
problem we would have to bound, and the three-state walk in §6 exists for cycles among items, not
among sets.

**Revisit post-MVP, and decide the depth rule before the feature**, not after. Additive either way.

**Changed:** CLAUDE.md §9 — kept in the architecture's line of sight, with the recursion reason
attached.

### Q4 — Promoting a detached item: answered, and it drags a feature in with it

**What was read.** [`2-flows/05-linked-vs-detached/NOTES.md`](2-flows/05-linked-vs-detached/NOTES.md)
— `Reset instance` beside `Reset fill`, the 423-instance count, and the finding that decided it:
**there is no prior art for a return path**; Figma erases the origin at detach.
[`2-flows/09-duplicate-and-fork/NOTES.md`](2-flows/09-duplicate-and-fork/NOTES.md) for the naming.
[`5-patterns/patterns.md`](5-patterns/patterns.md) — the command has a home on the project row.

**Promote as a new item, with the project's row re-linking to it.** Updating the original changes
every other project that links to it — blast radius spent on an action taken inside one project,
which is what §5 exists to warn about. *Push my changes to the original* is a different action with
a different confirmation, and it is not built in the MVP.

**And the sitting made explicit what the recommendation had left implicit.** Promotion is only worth
anything if the detached copy is **edited inside the project**. If detaching merely severs the link
and every edit still has to happen in the Library, then *detached* is a synonym for *unlinked*, state
6 in §7 is decoration, `overrides` never fills, and the P3 mechanism stage 5 imported — *name the
fields that differ* — has nothing to name.

> **In-project editing of a detached item is in the MVP.** It is what makes detach a feature rather
> than a toggle.

**Changed:** CLAUDE.md §5, §7 and §8.

### Q5 — Loss or reassembly cost: deferred, accepted risk

*I cannot find what I wrote three months ago* versus *I re-copy the same four files into every new
project*. CLAUDE.md §2 bets on neither; it bets on silent breakage.

**What was read, and what it was for.** Nothing in this repository can answer this question; the
reading frames it. [`3-pain/user-pain.md`](3-pain/user-pain.md) — the method section and the
blindness table: a tracker records **breakage, not friction**, so both candidates are invisible to it
by construction. [`1-landscape/competitors.md`](1-landscape/competitors.md) and
[`1-landscape/comparison.md`](1-landscape/comparison.md) — who positions on loss, who on reassembly,
who on breakage; positioning is not demand, but it is what fifteen companies believed.
[`1-landscape/continue-postmortem.md`](1-landscape/continue-postmortem.md) — which half of a product
with 1.58M installs survived.

**Deferred as accepted risk, and the trigger is written down**: ask five practitioners **before the
first feature that only pays off under one of the answers** — a *reassemble from a previous project*
flow versus serious investment in library-wide search. Until then the MVP is the same product under
either answer, which is why this deferral is cheap and why leaving it unmarked would not have been.

**One honest note about the sitting itself.** Q1's answer leans very slightly toward *reassembly* —
shipping a shelf of ready-made blocks is a bet that people want material, not that they want to find
their own. That is a hint, not evidence, and it is recorded as a hint so nobody later mistakes it for
the answer.

**Blocks:** positioning and the post-MVP order. **Not** the MVP build.

### Q6 — Styling engine: deferred to lesson 08, design tokens

Tailwind vs CSS Modules vs vanilla-extract. Almost nothing in the research bears on it, which is
worth stating rather than padding: CLAUDE.md §10 (**no UI kits** — the design system is custom and
*is part of the product's value*), §3 (**dark from day one**, light as a design decision rather than a
colour inversion — a theming requirement, not a preference), and
[`2-flows/10-dark-design-language/NOTES-linear.md`](2-flows/10-dark-design-language/NOTES-linear.md),
which is material for the next phase.

**Decided there, on two built components, with the criterion recorded now:** tokens and two real
themes must be first-class, and the engine must not push utility classes into components that are
themselves the product's value.

**Blocks:** nothing.

---

## 4. The documents that cut across stages

Most files belong to the stage that produced them. These do not — they are filed in one place and
read from several, which is exactly how a folder becomes confusing. Filed here so that stops.

| Document | Filed under | Read from |
|---|---|---|
| [`3-pain/user-pain.md`](3-pain/user-pain.md) | Stage 3 | **Everything downstream.** Stage 4's finalisation re-weights the four flows by it; stage 5 is read against it; five of the six open questions cite it. Read its *method* section before its findings — the instrument is blind to two of our three candidate pains, and that governs every use. |
| [`1-landscape/continue-postmortem.md`](1-landscape/continue-postmortem.md) | Stage 1 — it is a competitor | Stage 3 (findings 2 and 4 both lean on it), Q3, Q5. It is the only place a competitor is read **from source** rather than from its marketing. |
| [`4-benchmark/benchmark.md`](4-benchmark/benchmark.md) — *finalisation* section | Stage 4 | Stage 5, and every question. It is a statement about the **instrument**: the rubric grades craft, not weight, and the five pattern variants differ most where the pain evidence is thinnest. Read it before treating any score as a reason. |
| [`2-flows/05-linked-vs-detached/NOTES.md`](2-flows/05-linked-vs-detached/NOTES.md) | Stage 2 | CLAUDE.md §5 and §7, and Q4. The single most spec-bearing capture in the folder. |
| [`2-flows/11-copy-and-error-language/ci-failure-copy.md`](2-flows/11-copy-and-error-language/ci-failure-copy.md) | Stage 2 | §6, and every sentence the validation pass will ever write. Paired with `4-benchmark/npm-eresolve.md` and `terraform-validate-errors.md`, which are the same subject at a higher standard. |
| [`2-flows/10-dark-design-language/NOTES-linear.md`](2-flows/10-dark-design-language/NOTES-linear.md) | Stage 2 | **Nothing in this phase.** Deliberately handed forward: it is the one flow about appearance, and CLAUDE.md postpones visual direction. **Its first reader is lesson 06, concept** — corrected 2026-09-09, it used to say the design-system phase, which is lesson 09 — and that reader has not started work yet. |
| [`1-landscape/screens-index.md`](1-landscape/screens-index.md) | Stage 1 | Stage 2's README addresses captures through it. Sign-in walls are labelled, which is why some flows read as partial. |
| [`personas-and-jobs-critique.md`](personas-and-jobs-critique.md) | **The research root** — it spans two stages | **Stage 6 step 4 and stage 7 step 6, merged at the owner's request.** 238 claims in `personas.md` and `jtbd.md` classified Confirmed / Hypothesis / Invented; it edited nothing, and everything it proposed was applied on 2026-09-09 ([`jtbd.md` §11](7-jobs-to-be-done/jtbd.md), and in place in `personas.md`). Read Part 2, *the dangerous list*, before any design decision leans on a persona. |
| [`6-personas/re-research-2.md`](6-personas/re-research-2.md) | Stage 6 | **Stage 7's matrix and this document's §6.** The round that answered the audit's questions, and **the first instrument in the repository that counts somebody's collection instead of asking about it**. Two of its five answers change what was written elsewhere; one of them, Q-E, is the first evidence ever collected about P3 and it runs against the shelf. |

---

## 5. Sign-off — 2026-09-02

- [x] Stages 1–5 complete, each closed or declined with its reasoning recorded
- [x] The six questions marked **answered** or **deferred with a stated reason**, in one sitting
- [x] The dispositions written into the register in [`research-plan.md`](research-plan.md)
- [x] Decisions that change the spec written into [`CLAUDE.md`](../CLAUDE.md)
- [x] The **provisional** marks removed from [`5-patterns/patterns.md`](5-patterns/patterns.md) and
      CLAUDE.md §8 — the shape needed no revision, because Q2 added no surface

> **Re-opened 2026-09-06 with two more stages** — [personas](6-personas/README.md) and
> [jobs to be done](7-jobs-to-be-done/README.md) — because everything above establishes what vendors
> sell and what breaks, and nothing establishes who the person is or what they hire the product for.
> **Nothing in this document is retracted**; the five-stage sign-off stands and the two new stages
> audit the spec rather than edit it. This close will need a second half once they finish. The status
> and the three questions they raised are in [`research-plan.md`](research-plan.md).

**The five-stage research phase is closed.** Next: stages 6 and 7 — **lesson 02** — and after them
**lesson 03, information architecture**, not the design system, which is lesson 09 — *corrected
2026-09-09; this sentence used to send the reader straight from research to the design system, and
five lessons stand between them.* The visual direction, which this document called the design-system
phase's first task, is **lesson 06, concept**, with its reference material already gathered in
[`2-flows/10-dark-design-language/`](2-flows/10-dark-design-language/).

Two things this phase deliberately hands forward as work rather than as decisions: **the curated
public library has to be built** — real items from checked sources, with provenance and pinned
`ref`s, composed so the example project genuinely produces a Problem and a Note — and **Q5 carries a
trigger**, not a schedule. Neither blocks lesson 03.

---

## 6. Stage 6 in progress — what it has produced, and what it has moved

**Added 2026-09-07.** Stage 6 is not finished and this is not a second close. It is here because a
reader who starts at this file — which the whole repository instructs — would otherwise get the
five-stage picture with no sign that parts of it have moved.

**Four documents exist**, all in [`6-personas/`](6-personas/):

| File | What it is |
|---|---|
| [`inventory.md`](6-personas/inventory.md) | Every statement about people in this repository, with its source and its kind of evidence; the owner's fourteen assertions with a standing mark each; and **a register of twenty questions**, each with the answer we have, the data under it, and a mark. |
| [`re-research.md`](6-personas/re-research.md) | **A source document.** Four instruments taken to the public record — the `anthropics/claude-code` tracker (89,923 issues), `openai/codex`, `google-gemini/gemini-cli`, 1,762 Hacker News comments read in full, Stack Overflow, GitHub repository search. Logs committed beside it. |
| [`interview-guide.md`](6-personas/interview-guide.md) | The instrument for the five Q5 conversations, built around the one question no search can answer. |
| [`agent-setup-interview.md`](6-personas/agent-setup-interview.md) | **Interview 1 of 5.** Everything in it is `*`. |

**Added 2026-09-08:** the behavioural axes ([`inventory.md`](6-personas/inventory.md) §D — six
proposed, **two used to split, one one-ended axis that deletes a split rather than making one**) and
[`personas.md`](6-personas/personas.md) — **three personas, one primary.** The contest the plan
expected, *collector* against *the person who breaks at handover*, **did not happen**: the one
practitioner asked says the collection **caused** the breakage, so the primary merges them, and four
more Q15 answers are what would refute the merge. **Done since:** the page (2026-09-08), the audit and its application
(2026-09-09). **Still to do: four more interviews**, and a block of questions for a receiver,
which the guide does not have.

**And stage 7 opened the same day.** [`7-jobs-to-be-done/jtbd.md`](7-jobs-to-be-done/jtbd.md) — steps
1 to 4: one main job, four related, three emotional, two social, seven hypothesis jobs, and a visible
list of the six sentences that had to be rewritten because they were the specification with a *when*
in front of them. **Two main-job candidates survived**, which the method says means two products; the
second is **Q12**, and §6 forbids us to build it. The main job reads as **transfer** — *what I got
working here has to keep working there* — where §2 reads as **assembly with validation**. Stated as a
difference of emphasis, in one sentence, and **not applied.**

**The matrix (step 5) is in the same file.** Three jobs were named for the MVP core — important for
the primary persona **and** not closed by the market: the main job, *move the work without moving the
secrets*, and *fix it once and have the fix reach every copy*. Two jobs scored 3 for the primary and
are **not** in the core, and the reasons matter more than the shortlist: *not be quietly overruled* is
a constraint on every feature rather than a feature, and *stop suspecting half of it is dead weight*
has an **empty feature cell**, because §6 runs nothing on anyone's machine. **P3's column is `[?]` in
all ten rows** — this document said *nine* until 2026-09-09, and so did the stage README. Six
specified features close only a job whose every cell is `[?]` — **a list of hypotheses about an
absence, not a cut list**; nothing is removed.

**Both stages closed on 2026-09-09, and the closing pass changed the shortlist.** The audit
([`personas-and-jobs-critique.md`](personas-and-jobs-critique.md), stage 6 step 4 and stage 7 step 6
merged) classified 238 claims across the two documents — **163 confirmed, 48 hypothesis, 27
invented** — and was then applied. In the matrix it **only ever subtracted**: two cells lost their
numbers and four were lowered from 3 to 2, because a **3** means *a reason they would change how they
work* and in every case the person on record demonstrably did not. **The consequence is that the core
three is no longer a result the rule produces**: after the correction the rule selects **one**
buildable job, and *keys staying behind* and *one fix reaching every copy* are kept on stated
grounds — the market is open in both and the spec has already spent a mechanism on each. `jtbd.md` §8
says so in those words.

**The one thing that gained evidence argues against a feature.** [`re-research-2.md`](6-personas/re-research-2.md)
Q-E reached the first five practitioners ever observed on installing other people's material: **four
refuse it, minimise it, or prefer their own**, and what survived is *"a few established names"* —
**provenance over volume**. That is the first evidence under **Q9**, and it bears on **what the public
shelf holds and how it sorts**, not on whether it ships. Four sceptics on Hacker News are not a
market; the venue self-selects; no beginner was asked.

### The evidence rule changed, and it applies to this file too

There are now **three marks**, defined once in [`research.md`](research.md), *The three marks*:
**`✓`** confirmed by an instrument another person can re-run · **`*`** reported by a practitioner in
an interview, from memory, about their own work · **`?`** unknown. **A `*` never becomes a `✓` by
repetition** — only an instrument promotes it. The stage documents still write the third as `[?]`
and the digest still writes it as **`данные не подтверждены`**; those are one level in two registers.

### What has moved in what this document already says

**Nothing above is retracted, and four things are now narrower than they read** — the sentence said
*three* against four bullets until 2026-09-08, and the fourth is the one that carries the least
weight, so it was the wrong one to lose count of. **Each bullet now says what its mark is carrying**,
per rule 5 in [`research.md`](research.md): a re-runnable query proves that something was *said*, not
that it is *true*.

- **Stage 3, finding 4 — *nobody is asking for a composition layer*.** Measured as `0 results` on
  `continuedev/continue`, with a bug-shaped query, on a product whose hosted half was already dead.
  On live trackers the same friction **is** filed, as feature requests:
  [claude-code #9444](https://github.com/anthropics/claude-code/issues/9444) — *"each plugin must
  duplicate these resources… maintenance burden… copies can drift out of sync"* —
  and [codex #17401](https://github.com/openai/codex/issues/17401) — *"no modular reuse across
  projects… 10+ repos"*. The *method* section's claim that reassembly cost is invisible **by
  construction** should read: invisible to a bug search, visible to a feature-request search. `✓`
- **Stage 3, finding 1's superlative.** 182 is the most-reacted issue in
  `modelcontextprotocol/servers`, not anywhere. The most-reacted issue in the audience's own tracker
  is [claude-code #6235](https://github.com/anthropics/claude-code/issues/6235) at **6,592
  reactions**, asking for one instruction source across several agents. Finding 1's *direction*
  survives — the top of the corpus is environment and host, never composition. `✓`
- **Stage 5's 300-item claim**, which is what §8's accepted cost was priced against. **Counted on
  2026-09-08 rather than reported**: four public agent-material repositories hold **11, 25, 47 and 48
  items**, two of them above forty, read through the GitHub tree API
  ([`re-research-2.md`](6-personas/re-research-2.md) Q-C). **The 300 is refuted by measurement, and
  the replacement is a band, not a point: tens, not hundreds — design for fifty.** The earlier
  *"20–40"* was a blend of one organisation's management threshold with one person's file count and
  is withdrawn. The instrument sees only people who publish their setup.
- **`CLAUDE.md` §2's *"nothing does this today"*, at the item level.** Open-source skill managers
  with 400–4,500 stars **say in their READMEs** that they audit duplicates, detect version drift and
  score trust. The **set-level** half — resolve a named set, check that set, hand it over with
  instructions for the receiving machine — appears in nobody's README. ~~**`✓` on their existence,
  their stars and their push dates; their capabilities are vendor self-description and we ran none of
  them.**~~ **The afternoon was spent on 2026-09-10** (round 3, Q-J): four of them were installed and
  pointed at a deliberately broken set — `agent-skill-manager` 2.19.0, `skills` 1.5.25,
  `ai-agent-skills` 4.3.2, `opkg` 0.11.3. **Two more could not be installed under the name their
  README gives**, the npm packages `harnesskit` and `tank` belonging to unrelated projects, so
  `HarnessKit`'s trust score and drift detection stay unrun for a stated reason. **The set-level half
  held and is now measured rather than inferred: none of the four has a set-level unit at all**, so
  none detected the duplicate command name, the two items writing to one config file, or the key
  missing across the set. **Two item-level claims failed contact**: `asm doctor` describes the
  **receiving machine**, which the benchmark said nobody did, and `asm audit` — given one skill in
  three directories with one copy edited — skipped a directory it does not scan and called the other
  two, 8,072 bytes against 8,088, **`✓ identical copies`**, offering to delete one. **So the sentence
  still needs narrowing at the item level and is confirmed where it matters**, and the narrowing can
  now be written from a measurement.

**None of it is applied.** Stages 6 and 7 audit the spec; the owner edits it. **The proposals now sit
in two places and both are for the same sitting**: [`re-research.md`](6-personas/re-research.md) §4,
nine of them from stage 6, and [`jtbd.md` §12](7-jobs-to-be-done/jtbd.md), nine more from stage 7 —
the reconciliation, written as a table of *what was found · what is proposed · which register entry
it belongs to*. **Read §12 first**; it is the shorter list and it names the sections.

### The marks were audited on 2026-09-08

Every mark in the folder was re-read against its own evidence. **Nothing was collected and nothing
was withdrawn; eleven marks changed and two counts were wrong** — five register rows, two of the
owner's-assertion standings, the Snyk figures, and three of the digest's stage-6 findings. The rule the audit produced is now
**rule 5** in [`research.md`](research.md) — *a re-runnable query proves that something was said, not
that it is true* — and it is what four of the changes turn on: an issue body, a forum comment and a
tool's own README are people describing their own behaviour, so the `✓` on them covers the utterance
and rule 2 still governs the behaviour underneath. In
[`inventory.md`](6-personas/inventory.md): **NK-5, NK-6, NK-10** and **NK-19** lost a plain `✓`,
**NK-14** gained one it had already earned in its own *Rests on*, and the Snyk figures are now marked
*published, not verified by us*. The register's own summary line was wrong in the same direction and
now reads **nine `✓`, nine on one person, two with nothing at all**.

### The register grew

**Six questions are live**, not three: Q7–Q9 from the planning of stages 6–7, and **Q10, Q11 and Q12
raised on 2026-09-07 by the first interview** — precedence between a user's own rule and an external
requirement; the unwritten half of a setup; and whether the wanted thing is **observability of what
ran** rather than validation that a set coheres. All three stand on one person. The register is in
[`research-plan.md`](research-plan.md) and remains the only list.

### The one row we could close ourselves — closed 2026-09-10

**`SETUP.md` had never been tested.** `CLAUDE.md` §6 and Q2 above commit to an agent reading it and
performing the setup, on reasoning alone. It was the spec's most load-bearing bet, it is a claim about
a **machine** rather than a person, and it needed an afternoon. **It was written out on 2026-09-09 as
Q-F in [`6-personas/re-research-3.md`](6-personas/re-research-3.md)** — together with four more
questions that need no interview, because **the interviews became unavailable**, which removes the
instrument five register entries were pointed at and lowers no bar — and **the whole round was run on
2026-09-10.**

**All five were run. Four are answered, one in part**, and the capture is
[`6-personas/_re-research-3-log.json`](6-personas/_re-research-3-log.json) with
[`6-personas/_qf-handover-test/`](6-personas/_qf-handover-test/) beside it. **This is the first time
this repository measured its own claims rather than the ecosystem's opinion of them**, and four of the
marks it produced cover a behaviour rather than an utterance — the exception rule 5 was written to
allow for.

- **Q-F — the bet holds, and its second half does not.** Ten real pinned items with five planted
  defects, handed to three receivers. **All three performed the setup**, including cloning an external
  item at its pinned ref. **One found the Problems, one mis-resolved one on a false claim, one saw
  none** — and one copied the machine's live OAuth token into a plaintext file, unprompted. It also
  turned up three defects nobody planted, the sharpest being that **an item is a directory and §5
  models it as a file.** **NK-13 and the audit's D-1 are closed.**
- **Q-G — a striking number, withdrawn by its own control.** 89.4% of 2,027 forks of personal agent
  material have no commit after the fork point — **and the control says 84.8% for plain dotfiles and
  87.0% for ordinary small libraries.** The gap is 2–5 points and points the wrong way for the
  reading it was about to carry, so **the 89.4% stands as a count and is withdrawn as evidence that
  the archive is not being received.** What survives the control: of the 10.6% who do commit, 55% do
  so within the hour, and **25 of them literally substitute themselves for the author** — setup URLs,
  git identity, absolute paths, and instructions to the agent naming the author's handle. **RJ-1 has
  a behaviour under it for the first time.**
- **Q-H — copies diverge and stay diverged.** 14% of 7,506 duplicated items in 500 published trees are
  out of sync now; over history, **383 divergences are open at HEAD with a median age of 121 days, and
  four ever closed, all within seven hours.**
- **Q-I — the shelf's premise describes a real behaviour.** Thousands of repositories carry verbatim
  copies of public skills; **32% of 446 traced copies were edited after import, at a median of 27
  days; 10% keep any statement of origin.** This places round 2's four-of-five refusal rather than
  refuting it.
- **Q-J — §2's sentence survives where it matters and narrows twice more.** Four tools installed and
  run against the same broken set: **nothing detects a set-level defect, because nothing has a
  set-level unit.** But `asm` ships 369 pre-defined **bundles** and a `doctor` that is a **B4 surface**
  — which the benchmark said nobody had — and its duplicate audit calls two files with different
  sha1s *"identical copies"* and offers to delete one.

**Six proposals go to the register's sitting**, listed at the end of that file. **Nothing is applied
to `CLAUDE.md`, and the *provisional* label does not lift** — its trigger is five practitioner
conversations, and closing four hypotheses does not change what the trigger is.
