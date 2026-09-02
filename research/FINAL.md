# FINAL — the closing document of the research phase

Written 2026-09-01, closed 2026-09-02. **The research phase is signed off.** Read this instead of
re-reading everything: it is what the phase produced, what it decided, and how the six open questions
were settled in the sitting of 2026-09-02.

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
| **3 Pain** ([`3-pain/README.md`](3-pain/README.md)) | What actually hurts, from two public trackers | Our thesis is **real and quiet** (13 reactions) while the loud pain is environmental (**182**). Everything downstream is weighted by this. |
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
| **Q6** | Styling engine | **Deferred** to the design-system phase, criterion recorded |

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

### Q6 — Styling engine: deferred to the design-system phase

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
| [`2-flows/10-dark-design-language/NOTES-linear.md`](2-flows/10-dark-design-language/NOTES-linear.md) | Stage 2 | **Nothing in this phase.** Deliberately handed forward: it is the one flow about appearance, and CLAUDE.md postpones visual direction to the design-system phase. Its first reader has not started work yet. |
| [`1-landscape/screens-index.md`](1-landscape/screens-index.md) | Stage 1 | Stage 2's README addresses captures through it. Sign-in walls are labelled, which is why some flows read as partial. |

---

## 5. Sign-off — 2026-09-02

- [x] Stages 1–5 complete, each closed or declined with its reasoning recorded
- [x] The six questions marked **answered** or **deferred with a stated reason**, in one sitting
- [x] The dispositions written into the register in [`research-plan.md`](research-plan.md)
- [x] Decisions that change the spec written into [`CLAUDE.md`](../CLAUDE.md)
- [x] The **provisional** marks removed from [`5-patterns/patterns.md`](5-patterns/patterns.md) and
      CLAUDE.md §8 — the shape needed no revision, because Q2 added no surface

**The research phase is closed.** Next phase: the design system, whose first task is the visual
direction, with its reference material already gathered in
[`2-flows/10-dark-design-language/`](2-flows/10-dark-design-language/).

Two things this phase deliberately hands forward as work rather than as decisions: **the curated
public library has to be built** — real items from checked sources, with provenance and pinned
`ref`s, composed so the example project genuinely produces a Problem and a Note — and **Q5 carries a
trigger**, not a schedule. Neither blocks the design system.
