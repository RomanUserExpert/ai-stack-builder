# FINAL — the closing document of the research phase

Written 2026-09-01. **Read this before signing the phase off, and read it instead of re-reading
everything.**

Three documents govern this folder and none of them repeats another:

| | Holds |
|---|---|
| [`research-plan.md`](research-plan.md) | **Status.** The five stages, what each was for, and the register of open questions with their IDs. The source of truth for *what is done*. |
| **`FINAL.md`** (this file) | **The close.** What the phase produced, what it decided, the six questions still open with what to read before deciding each, and the documents that cut across stages. |
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
| **5 Patterns** ([`5-patterns/README.md`](5-patterns/README.md)) | What shape the key flow takes | **The library leaves the builder and drag stops being the verb** (§8) — provisional until the questions below are closed. |

## 2. Decisions taken, and where they live

All in CLAUDE.md, which is the source of truth. The reasoning and the rejected alternatives are in
[`1-landscape/comparison.md`](1-landscape/comparison.md) and in the stage documents.

| Decision | Answer | Spec |
|---|---|---|
| Does `visibility` appear in the MVP interface? | No. The field stays, the control is not shown. | §9 |
| What evidence does an item card carry? | Usage facts from the library. Never a score, rating, eval result or badge. | §5 |
| Does anything read `version`? | The field is cut; external references gain a pinned `ref`. | §5, §9 |
| Does the validation pass block, or grade? | Neither. Three severities, and export is never disabled — an unclean set is confirmed. | §6 |
| What shape does the key flow take? | Command-first assembly, run-centric check ending in export. **Provisional.** | §8 |

Two contradictions inside the spec were closed on the way: `version` was both reserved-and-unread
and expected to produce conflicts; `conflicts` was to be hard or soft with no field able to say
which. A third correction went the other way — a cycle in `requires` is not a defect at all, because
a project is a set and not an execution order.

---

## 3. What is still open — six questions

Worked through in **one sitting**, once, and not before. A question answered on partial evidence has
to be re-opened later, and re-opening costs more than waiting. Each entry below carries what to read,
the options actually on the table, and a recommendation.

| | Question | Status going in |
|---|---|---|
| **Q1** | Cold start — demo problem or product decision? | Evidence answers it. |
| **Q2** | How much weight does `SETUP.md` carry? | **A call** — it is a scope boundary. |
| **Q3** | Can a project contain a project? | Evidence answers it. |
| **Q4** | Can a detached item be promoted back into the library? | Evidence answers it; one fork in the semantics. |
| **Q5** | Loss or reassembly cost — which drives adoption? | **A call** — whether to buy an answer at all. |
| **Q6** | Styling engine | **A call** — blocks nothing; timing only. |

### Q1 — Cold start: demo problem or product decision?

CLAUDE.md §11 plans *~30 realistic items for any mockup*. Linear ships a new workspace with four
**real**, editable objects, so the product is never empty and the model is learned by holding four
instances of it.

**Read first**

- [`2-flows/08-empty-state-and-cold-start/NOTES-linear.md`](2-flows/08-empty-state-and-cold-start/NOTES-linear.md)
  — the four seeded issues, and the rule that picks between **three registers of emptiness**
  (never-used concept → define it · routine → one line · filtered to zero → count what is hidden).
- [`4-benchmark/NOTES-obsidian.md`](4-benchmark/NOTES-obsidian.md) — an empty query that becomes the
  create row; an empty tab that is three actions with their shortcuts inline.
- [`4-benchmark/NOTES-vscode.md`](4-benchmark/NOTES-vscode.md) — the recommendation prompt on opening
  a folder, and `@recommended` split into counted sections.
- [`5-patterns/patterns.md`](5-patterns/patterns.md) — question 1 of the five: **three of the five
  shapes are broken without a seed.**

**Options.** (a) Ship a seeded library — real Items in a real Project, editable and deletable.
(b) Demo content behind a button. (c) Empty, with a strong empty state only.

**Recommendation — (a), and the size is set by a requirement rather than by taste.** The seed must
produce **at least one Problem and at least one Note**: a real conflict, a target-path collision, a
missing env key. A first run showing six green ticks teaches nothing about what the product is for.
That is 8–12 items and one project; the ~30 in §11 stays true for mockups, which is a different job.

**Blocks:** CLAUDE.md §11 and the whole first-run experience.

### Q2 — How much weight does `SETUP.md` carry?

§6 gives it one line while the loudest pain in the ecosystem lives exactly there: the archive lands
on a machine and does not run. Either we own that problem or we say plainly it is not our war.

**Read first**

- [`3-pain/user-pain.md`](3-pain/user-pain.md), finding 1 — *MCP Servers Don't Work with NVM*,
  **182 reactions**, over a top-of-tracker made of PATH, node version managers, platform paths and
  processes dying at startup. The *"most of this is out of our reach"* paragraph draws the very line
  this question asks us to place.
- [`4-benchmark/benchmark.md`](4-benchmark/benchmark.md) — the four B4 cells (**nobody above 4**),
  finding 8, and the finalisation's *gap*: every cell scores what a product says about its own state,
  none about the machine its artefact lands on.
- [`2-flows/06-export-and-target-adaptation/ruler-per-agent-output.md`](2-flows/06-export-and-target-adaptation/ruler-per-agent-output.md)
  — two distribution mechanics, a managed `.gitignore` block, a `.bak` beside every overwritten file.
- [`4-benchmark/create-next-app-output.md`](4-benchmark/create-next-app-output.md) — the same two
  mechanics from an unrelated vendor, and a fenced block that **explains its own re-appearance**.
- [`2-flows/07-env-and-secrets/NOTES.md`](2-flows/07-env-and-secrets/NOTES.md) — type before value,
  the irreversible option as the default, and *"where to rotate, or who to contact"*.
- [`1-landscape/continue-postmortem.md`](1-landscape/continue-postmortem.md) — its identity and
  secret schemes, and the three things its resolver never did.

**Options**

1. **Disclose the handover inside Run.** The last stages show what the archive contains and what the
   receiving machine must still do — `SETUP.md` preview, pinned `ref`s, platform-correct
   `targetPath`s, `.env.example` — read *before* Export is pressed. Nothing runs on anyone else's
   machine. Fits current scope: two more stages in a list that already exists.
2. **Also emit a verify script** into the archive, run by the user on the target machine. Aims
   straight at the 182-reaction pain, and expands the MVP with a new artefact plus platform coverage.
3. **Say it is not our war**, keep the one line, record the reason.

**Recommendation — (1), with the export designed so that (2) is additive rather than a rewrite.**

**Blocks:** the real scope of CLAUDE.md §6.

### Q3 — Can a project contain another project, or only items?

**Read first**

- [`3-pain/user-pain.md`](3-pain/user-pain.md), finding 4 — `reuse blocks assistant`: **0 results**
  in a 6,677-issue tracker belonging to a product that shipped a hub for exactly this.
- [`1-landscape/continue-postmortem.md`](1-landscape/continue-postmortem.md) — the
  `uses`/`with`/`override` primitive, and which half of that product was switched off.
- [`5-patterns/patterns.md`](5-patterns/patterns.md) — **no variant needed composition to work.**

**Recommendation — no. Items only.** Three independent signals point the same way. Additive later if
it is ever wanted.

**Blocks:** the data model, later. Not the MVP.

### Q4 — Can a detached item be promoted back into the library?

**Read first**

- [`2-flows/05-linked-vs-detached/NOTES.md`](2-flows/05-linked-vs-detached/NOTES.md) — the whole
  file. `Reset instance` beside `Reset fill`, the 423-instance count, and the finding that decides
  this question: **there is no prior art for a return path.** Figma erases the origin at detach.
- [`2-flows/09-duplicate-and-fork/NOTES.md`](2-flows/09-duplicate-and-fork/NOTES.md) — for the naming.
- [`5-patterns/patterns.md`](5-patterns/patterns.md) — in the chosen shape the command has a home:
  the project row, next to detach and reset.

**The fork.** Promote as a **new item**, or **update the original**?

**Recommendation — a new item, with the project's row re-linking to it.** Updating the original
changes every other project that links to it — blast radius spent on an action taken inside one
project, which is what §5 exists to warn about. *"Push my changes to the original"* is a different
action with a different confirmation, and it is not built in the MVP.

**Blocks:** CLAUDE.md §5, later.

### Q5 — Loss or reassembly cost: which actually drives adoption?

*I cannot find what I wrote three months ago* versus *I re-copy the same four files into every new
project*. CLAUDE.md §2 bets on neither; it bets on silent breakage.

**Read first — and note what these are for.** Nothing in this repository can answer this question.
The reading frames it; it does not decide it.

- [`3-pain/user-pain.md`](3-pain/user-pain.md) — the method section and the blindness table. A
  tracker records **breakage, not friction**, so both candidates are invisible to it by construction.
  This is why the question is still open and why no planned stage touched it.
- [`1-landscape/competitors.md`](1-landscape/competitors.md) and
  [`1-landscape/comparison.md`](1-landscape/comparison.md) — who positions on loss, who on
  reassembly, who on breakage. Positioning is not demand, but it is what fifteen companies believed.
- [`1-landscape/continue-postmortem.md`](1-landscape/continue-postmortem.md) — which half of a real
  product with 1.58M installs survived.

**Options.** (a) Defer as accepted risk, with a named trigger. (b) Add a stage: five to eight
conversations with practitioners before sign-off. (c) Declare a third answer from the pain data —
*it does not run when it lands* — and mark plainly that this is ecosystem pain, not a reason to adopt
our product.

**Recommendation — (a), with the trigger written down**: ask five people **before the first feature
that only pays off under one of the answers** — a *reassemble from a previous project* flow versus
serious investment in library-wide search. The MVP is the same product under either answer.

**Blocks:** positioning and the post-MVP order. **Not** the MVP build.

### Q6 — Styling engine

Tailwind vs CSS Modules vs vanilla-extract.

**Read first.** Almost nothing in the research bears on this, which is worth stating rather than
padding:

- CLAUDE.md §10 — **no UI kits**; the design system is custom and *is part of the product's value*.
- CLAUDE.md §3 — **dark from day one**, light as a design decision rather than a colour inversion.
  That is a theming requirement, not a preference.
- [`2-flows/10-dark-design-language/NOTES-linear.md`](2-flows/10-dark-design-language/NOTES-linear.md)
  — the material already gathered for the design-system phase, which is where this belongs.

**The criterion, whenever it is decided.** Tokens and two real themes must be first-class, and the
engine must not push utility classes into components that are themselves the product's value.

**Recommendation — defer to the design-system phase**, decided on two built components, with the
criterion recorded now.

**Blocks:** nothing in this phase.

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

## 5. What sign-off requires

- [x] Stages 1–5 complete, each closed or declined with its reasoning recorded
- [ ] The six questions above marked **answered** or **deferred with a stated reason**, in one sitting
- [ ] The dispositions written into the register in [`research-plan.md`](research-plan.md)
- [ ] Decisions that change the spec written into [`CLAUDE.md`](../CLAUDE.md)
- [ ] The **provisional** marks removed from [`5-patterns/patterns.md`](5-patterns/patterns.md) and
      CLAUDE.md §8 — or the shape revised, if Q2 adds a surface none of the five variants has

Next phase after sign-off: the design system. Not started, per CLAUDE.md §1.
