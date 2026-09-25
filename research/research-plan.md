# Research plan

Updated 2026-09-10. The phase ran in five stages and was **signed off on 2026-09-02**; the register
was worked through in one sitting that day. **On 2026-09-06 the phase was re-opened with two more
stages, 6 and 7** — personas and jobs to be done — because the sign-off had established what vendors
sell and what breaks, and never who the person is or what they hire the product for. The five-stage
sign-off stands as written; stages 6–7 are an addition to it, not a correction. **What comes next is
lesson 03, information architecture** — *corrected 2026-09-09; this said "the design system", which
is lesson 09, and five lessons stand between them. CLAUDE.md §1 carries the twelve.*

| # | Stage | What it produces | Status |
|---|---|---|---|
| 1 | **Landscape** | Who else is in this space, what they sell, and to whom | ● done |
| 2 | **Flows** | Twelve mechanisms captured from live products | ● done |
| 3 | **Pain** | The first evidence about users rather than vendors | ● done |
| 4 | **Benchmark** | A **scoring rubric** — five categories, applied to the best product in the world at each of our four core flows | ● done — 15 cells scored |
| 5 | **Patterns** | Five radically different shapes for our key flow, scored with that rubric, one chosen | ● done — hybrid chosen, CLAUDE.md §8 rewritten |
| 6 | **Personas** | 2–4 behavioural personas, one primary, every block sourced or `[?]` — **provisional** until five practitioners are asked | ● done 2026-09-09 — three personas, one primary; audited and applied. **Provisional stands: four interviews are unavailable.** Four collection rounds since |
| 7 | **Jobs to be done** | One main job, related, emotional and social jobs, and a jobs × personas matrix that says what to build first and what not to build | ● done 2026-09-09 — one main job, four related, three emotional, two social, seven hypotheses and the matrix. **Rounds 3 and 4 have since moved it: 36 `[?]` cells → 31, two numbers raised** |

Stage 4 exists to make stage 5 decidable. Without a rubric, *"which of these five is best"* is settled
by taste; with one, it is settled by argument. And the rubric is not invented — its five categories
are lifted from what stages 1–3 actually found.

Sign-off came after stage 5. Stages 6 and 7 read stage 3 more than anything else, and inherit its
limit: a tracker sees breakage, not friction. Both ship **provisional**; the label lifts on the Q5
trigger — five practitioner conversations, filed as a source document.

---

## Documents

The folder is organised by stage. Each stage folder has a short README that says what it produced
and where to start; this table says what each document holds.

```
research/
  research-plan.md      the spine — stages, status, the register of open questions
  FINAL.md              the closing document — decisions, what is open, what cuts across stages
  1-landscape/  2-flows/  3-pain/  4-benchmark/  5-patterns/
```

| File | What it holds |
|---|---|
| [`FINAL.md`](FINAL.md) | **Read before sign-off.** What the phase produced, the decisions taken, the six open questions with what to read before deciding each, and the documents that are read from more than one stage. |
| [`1-landscape/competitors.md`](1-landscape/competitors.md) | 15 companies in three groups — hard, soft, aspirational. Why each is there, what to take from it, a verified link per entry. |
| [`1-landscape/comparison.md`](1-landscape/comparison.md) | All 15 compared on audience, product base, key mechanism, trust, monetisation. Three market patterns, three differences we can hold, and the three decisions the design system needed, each with its reasoning. |
| [`1-landscape/screens-index.md`](1-landscape/screens-index.md) | 38 product captures in [`1-landscape/screens/`](1-landscape/screens/), sorted group / competitor. Sign-in walls labelled. |
| [`3-pain/user-pain.md`](3-pain/user-pain.md) | What actually hurts, from two public issue trackers — the first evidence here about users rather than vendors. States plainly what the instrument cannot see. |
| [`1-landscape/continue-postmortem.md`](1-landscape/continue-postmortem.md) | The closest competitor read from source: its block model, the `uses`/`with`/`override` composition primitive, its identity and secret schemes, and the three things its resolver never did. |
| [`2-flows/README.md`](2-flows/README.md) | The twelve flows: what each is for, what is collected, what is missing, what access it needed. |
| [`4-benchmark/benchmark.md`](4-benchmark/benchmark.md) | **Stage 4.** The scored matrix — 15 cells, five categories — the three rules the scoring follows, and the argument behind every score below or above 4. Ends with eight findings, which are what stage 5 spends. Captures in [`4-benchmark/`](4-benchmark/). |
| [`5-patterns/patterns.md`](5-patterns/patterns.md) | **Stage 5.** Five shapes for *assemble → check → export*, each answering the same five questions, each scored on the stage-4 rubric read as *does the shape give this a home*. The choice, what each rejected variant donates, and what the choice costs. |
| [`6-personas/README.md`](6-personas/README.md) | **Stage 6 — the plan.** What the stage is for, the way it goes wrong here, the inputs classified by kind of evidence, seven steps with a done-bar each, the evidence rule and the honest problem. |
| [`6-personas/inventory.md`](6-personas/inventory.md) | **Stage 6, step 1, revalidated.** Every statement about people in this repository with its source and kind of evidence; the owner's fourteen assertions with a standing mark each; and **a register of the twenty questions** — the answer we have, the data it rests on with links, and a `✓` / `*` / `?` mark on each. Three more questions arrived with the first interview: NK-21 to NK-23. |
| [`6-personas/re-research.md`](6-personas/re-research.md) | **Stage 6, step 5, and everything after it — four collection rounds merged into one source document on 2026-09-10.** **[Round 1](6-personas/re-research.md#round-1-the-public-record)** took four instruments to the public record; **[round 2](6-personas/re-research.md#round-2-counting-not-asking)** counted somebody's collection instead of asking about it; **[round 3](6-personas/re-research.md#round-3-five-questions-that-need-no-interview)** stopped reading and ran two experiments, closing NK-13; **[round 4](6-personas/re-research.md#round-4-the-matrixs-empty-cells)** went at the matrix's persona columns and moved six cells. Capture logs in [`6-personas/_captures/`](6-personas/_captures/). |
| [`6-personas/personas.md`](6-personas/personas.md) | **Stage 6, step 3, written 2026-09-08.** Three personas on the axes in `inventory.md` §D — **P1 the keeper who runs several agents (primary)**, P2 the receiver, P3 the empty-handed. Five blocks each (context, jobs, pains, trust triggers, quote) plus environment; every block sourced or `[?]`; **eleven hypotheses** in their own table, each with the instrument that would close it. **Provisional** until five interviews. |
| [`personas-and-jobs-critique.md`](personas-and-jobs-critique.md) | **The audit, written 2026-09-08 and applied 2026-09-09** — merged with stage 7's step 6 at the owner's request. 238 claims classified across both files, 27 found invented. Confirmed / hypothesis / invented, the dangerous list, and the proposals. **D-1 was closed on 2026-09-10.** |
| [`6-personas/interviews.md`](6-personas/interviews.md) | **The instrument, and the one conversation that happened**, merged 2026-09-10. **[Part 1, the guide](6-personas/interviews.md#part-1-the-guide)** — the 30-minute instrument that lifts *provisional*, covering the fifteen rows that need a person. **[Part 2, interview 1 of 5](6-personas/interviews.md#part-2-interview-1-of-5)** — the only practitioner ever run against it; everything in it is **`*`** and `n = 1`. **The remaining four are unavailable.** |
| [`6-personas/_captures/`](6-personas/_captures/) | **The capture logs, one per round**, plus [`qf-handover-test/`](6-personas/_captures/qf-handover-test/) — the archive three receiving agents were given, the ground truth of what was wrong with it, and a transcript per run. |
| [`7-jobs-to-be-done/README.md`](7-jobs-to-be-done/README.md) | **Stage 7 — the plan.** The canonical job form, the hierarchy, the feature-name test, the matrix, and what each of its two answers is worth. |
| [`7-jobs-to-be-done/jtbd.md`](7-jobs-to-be-done/jtbd.md) | **Stage 7, written 2026-09-08, audited and reconciled 2026-09-09.** Main-job candidates and the choice, the hierarchy, the matrix with feature and competitor columns, the two conclusions, and §12's nine proposals. **§7 now carries what rounds 3 and 4 did to the matrix.** Provisional. |
| [`6-personas/personas.html`](6-personas/personas.html) | **Generated.** Phase 02 of the course — the persona cards, the job hierarchy and the matrix, built by `tools/build_personas.py` from `tools/personas-page.tpl.html`. Do not hand-edit. |

---

## Stages 1–3 — done

### Flows

**10 of 12 closed.** Flow 01 is declined (login-walled, and its other gap is out of MVP scope).
Flow 10 is handed forward rather than left open — it is the one flow about appearance rather than
behaviour, and CLAUDE.md §12 postpones visual direction until after research. **Its reader is
lesson 06, concept** (corrected 2026-09-09; it used to say the design-system phase).

**Status key.** ● closed · ◐ partially covered · → handed forward to the next phase.

| # | Flow | Status | Notes |
|---|---|---|---|
| 01 | Item detail and trust | ◐ | Declined — Agentman is login-walled; version history is out of MVP scope (§9) |
| 02 | Library browse, filter, search | ● | [Linear](2-flows/02-library-browse-filter-search/NOTES-linear.md) |
| 03 | Relations without a canvas | ● | — |
| 04 | Validation: pass, warn, block | ● | [Terraform](2-flows/04-validation-check-results/terraform-plan-output.md) · [Vercel](2-flows/04-validation-check-results/NOTES-vercel.md) · [GitHub Actions](2-flows/04-validation-check-results/NOTES-github-actions.md) · [Port](2-flows/04-validation-check-results/NOTES-port.md) |
| 05 | Linked vs detached, blast radius | ● | [NOTES](2-flows/05-linked-vs-detached/NOTES.md) — all three instance states |
| 06 | Export and target adaptation | ● | [Ruler output](2-flows/06-export-and-target-adaptation/ruler-per-agent-output.md) |
| 07 | Env variables and secrets | ● | [NOTES](2-flows/07-env-and-secrets/NOTES.md) |
| 08 | Empty state and cold start | ● | [Linear](2-flows/08-empty-state-and-cold-start/NOTES-linear.md) |
| 09 | Duplicate and fork | ● | [NOTES](2-flows/09-duplicate-and-fork/NOTES.md) |
| 10 | Dark design language | → | [Material for lesson 06, concept](2-flows/10-dark-design-language/NOTES-linear.md) |
| 11 | Copy: errors, warnings, refusals | ● | [Conflict copy](2-flows/11-copy-and-error-language/dependency-conflict-copy.md) · [CI failure copy](2-flows/11-copy-and-error-language/ci-failure-copy.md) |
| 12 | Visibility and portfolio | ● | [NOTES](2-flows/12-visibility-and-portfolio/NOTES.md) |

### Nothing left to collect in stages 1–3

Every remaining item is declined with the reasoning recorded: Raycast desktop (its one UX idea, the
launcher instead of a screen, is already answered by Linear and Tessl), Linear's density under load
(the workspace granted is new), Agentman (login-walled), a version/history surface (out of MVP scope),
Figma's cross-file usage count (paid tier), Packmind and Continue Hub (substituted), Mobbin (not worth
a subscription).

---

## Stage 4 — Benchmark

**Question it answers.** For each of our four core flows, who in the world does it best, how well, and
against what standard?

**Why it comes now.** Stages 1–3 produced observations — *Linear counts what its filter hides*, *Port
prints the condition and the observed value*, *Figma computes drift and never draws it*. Those are
anecdotes until they are turned into a **scale**. Stage 4 turns them into one, and stage 5 spends it.

**Deliverable.** `benchmark.md`: a scored matrix, one row per app-and-flow, five columns, plus the
reasoning behind every score below 4 and above 4. Captures go in `benchmark/` alongside `flows/`.

### The four flows benchmarked

Not all twelve. Only the spine of the product — the path a user actually walks.

| | Flow | Our screen |
|---|---|---|
| **B1** | Find one thing in a large personal collection | Library |
| **B2** | Assemble a set from that collection, with constraints | Project Builder |
| **B3** | Check a set and report what is wrong | Validation pass |
| **B4** | Produce an artefact and hand it over to another machine | Result / Export |

### The five categories

Each is lifted from a finding in stages 1–3, so the rubric is grounded rather than invented.

| # | Category | The question | Where it came from |
|---|---|---|---|
| **C1** | **State legibility** | Can you read the current state without acting on it? | Figma draws a modified instance identically to a clean one; Linear says *"4 issues hidden by filters"* |
| **C2** | **Consequence disclosure** | Before an irreversible step, is the cost stated in advance? | `terraform apply` asks you to type `yes`; Figma's library modal shows **423 instances** before you accept |
| **C3** | **Failure copy** | Does a message name the item, the rule and the observed value? | Port: `where "Open Critical Vulnerabilities" = 0 · Value: 1`. GitHub: `Process completed with exit code 1` |
| **C4** | **Recovery** | Is there a way back, offered where the problem is? | Figma puts `Reset` next to `Detach` — and offers nothing at all once detached |
| **C5** | **Economy** | Is anything on screen that cannot act, or missing that must be? | Linear suppresses its toolbar over an empty list; Vercel keeps four filter dropdowns over nothing |

**Score anchors**, so a number means something:

- **1** — actively misleads. The interface implies something untrue.
- **2** — the information does not exist in the product.
- **3** — correct, but you must go looking for it.
- **4** — present where you need it, in the right words.
- **5** — you could not miss it, and it changed what you did next.

### Candidates

Best-in-class, competitors allowed but not required. Availability on this machine noted, because a
benchmark we cannot capture is a benchmark we cannot defend.

**As planned, and as it ended up.** Two candidates were replaced and one dropped; the reasoning is
recorded in [`4-benchmark/benchmark.md`](4-benchmark/benchmark.md) rather than repeated here.

| Flow | Candidates, final | Change from the plan |
|---|---|---|
| **B1** Find | **Linear** ⌘K · **GitHub** code search · **Obsidian** quick switcher · **VS Code** palette + Extensions | none — all four captured |
| **B2** Assemble | **VS Code** per-workspace extensions + Workspace Trust · **`npm install`** · **Figma** instances and library | `Brewfile` → `npm` (a format we can only read is not a benchmark); **Docker Compose dropped** (not installed, and the question was answered three ways already) |
| **B3** Check | **Terraform** `plan` + `validate` · **VS Code** Problems panel · **Vercel** build log · **GitHub Actions** run | `validate` against a deliberately broken config was added, to capture the failure copy the successful plan could not |
| **B4** Produce | **Vercel** deploy · **`create-next-app`** · **Figma** export dialog · **Ruler** | none |

**VS Code earns its place three times over.** Free, installed, and it is the closest thing in
existence to our product's mechanics: an extension list that is browsed and filtered, a set enabled
per workspace with recommendations resolved from a file, and a Problems panel that reports what is
wrong with file, line and rule. Not a competitor, best-in-class at our flows — exactly the brief.

**Substitutes for what cannot be run here.** Ableton's *Collect All and Save* would be the ideal B4 —
it gathers every referenced sample into one folder and reports what it could not find, which is our
export with missing-dependency reporting, note for note. No licence here. Xcode's Archive/Organizer,
same story. Both are described from documentation if needed, and clearly labelled as unseen.

### Method

Same discipline as stage 2. Playwright for anything public, Claude in Chrome for anything behind the
owner's session, local CLI for anything installable without side effects. Read-only. Every capture
logged. **Scores are written before the reasoning, then the reasoning is written and the score
revisited once** — so the number is argued, not rationalised.

### Done — 2026-09-01

All fifteen cells scored, every score justified, the five categories carried into stage 5 unchanged.
Eight findings came out of it; two of them corrected this research rather than the products —
**the "an action that cannot act is not shown" rule holds on primary surfaces and reverses in context
menus**, and **B4 is the weakest flow in the industry**, which is where our wow moment is aimed.

---

## Stage 5 — Patterns

**Question it answers.** What shape does our key flow take?

**The key flow, named precisely.** Not "the app". The spine: **assemble a set → check it → export**.
Library to archive. It contains the wow moment (CLAUDE.md §2) and both supporting moments.

**Deliverable.** `patterns.md`: five variants, each described structurally, each scored on C1–C5 plus
fit to the fixed constraints, and one chosen with the reasoning for the rejection of the other four.

**Boundary, and it matters.** These are **flow structures, not screens**. Described in prose and
plain-text diagrams — boxes, order, what is on screen at each step. No visual design, no layout
grids, no colour, no components. CLAUDE.md §1 puts information architecture, prototyping, the concept
and UI assembly after this phase — lessons 03 to 07 — and this stage must not quietly become any of
them.

### The five variants

Radically different framings, not five layouts of one idea. Each carries prior art from stages 1–3, so
the comparison is between things that exist rather than between guesses.

| | Variant | The idea | Prior art |
|---|---|---|---|
| **P1** | **Two-pane drag** | Library on the left, project area on the right, items dragged in, validation live as the set changes. The current §8 spec. | Backstage catalog; Figma assets panel |
| **P2** | **Command-first** | No persistent library pane. ⌘K adds items by name, the project is a growing list, checking is another command. The library is a search index, not a screen. | Linear ⌘K; Tessl ⌘K; Raycast's launcher-instead-of-a-screen |
| **P3** | **Document** | The project *is* an editable manifest. The UI is an assistant over the text and validation is inline diagnostics, like a linter. | Continue's `config.yaml` with `uses`/`with`/`override`; Terraform HCL; VS Code Problems panel |
| **P4** | **Staged wizard** | Target first, then one step per kind, then resolution, then review, then export. Linear, finite, no free-form assembly. | Backstage scaffolder; GitHub's fork form |
| **P5** | **Run-centric** | Assembly is small and secondary. Pressing **Check** turns the whole surface into the stage list with verdicts and durations, and Export is its final stage. The validation pass is the product's main screen, not a modal. | Vercel's deployment page; a GitHub Actions run |

### What each variant must answer, in the same words

So they can be compared rather than admired:

1. Where does the **cold start** land — what does this look like with an empty library, and with a
   seeded one? (Bears directly on the open question below.)
2. Where does the **validation pass** live — inline and continuous, or triggered and full-screen?
3. Where do the **six item states** (§7) render, especially *detached, locally modified*?
4. How does an **unclean export** get confirmed (§6), and where does that confirmation appear?
5. What does it cost when the library has **300 items** rather than 30?

### Choosing

Score C1–C5 from stage 4's rubric, then check against the constraints that are already fixed and not
up for negotiation: desktop-first, dark from day one, **not a node canvas**, single user, local only,
custom design system. A variant that scores well and violates a fixed constraint loses.

**Expect a hybrid, and say so honestly if it happens.** The likely outcome is that one variant wins
the spine and another donates a mechanism — P2's palette inside P1's two panes, or P5's run screen as
P1's Result. That is a legitimate result as long as it is stated as a choice and not as a failure to
choose.

### Done — 2026-09-01

**A hybrid, stated as a choice.** P2 (command-first) wins the spine; P5 (run-centric) becomes the
check-and-export surface; P3 donates one mechanism — a detached item naming the fields that differ.
CLAUDE.md §8 is rewritten to three surfaces plus Projects, and the change of substance is that **the
library is no longer inside the builder and drag is no longer the mechanism**: it does not survive
300 items, and a pane that cannot act during a check is the mistake §6 and §9 refuse elsewhere.

The four rejected variants, and the reason each lost, are in [`5-patterns/patterns.md`](5-patterns/patterns.md). So is what
the choice costs — with no library pane you cannot see what you are not using, and three things now
carry that weight.

---

## Decisions already taken

All four landed on 2026-09-01 and are recorded in CLAUDE.md, which is the source of truth.
[`1-landscape/comparison.md`](1-landscape/comparison.md) keeps the reasoning and the rejected alternatives.

| Decision | Answer | Where |
|---|---|---|
| Does `visibility` appear in the MVP interface? | No. The field stays, the control is not shown. | CLAUDE.md §9 |
| What evidence does an item card carry? | Usage facts from the library — *used in 3 projects*. Never a score, rating, eval result or badge. | CLAUDE.md §5 |
| Does anything read `version`? | The field is cut. External references gain a pinned `ref` instead — Tessl's model, not Terraform's. | CLAUDE.md §5, §9 |
| Does the validation pass block, or grade? | Neither. Three severities — Problem / Note / Skipped — and export is never disabled; an unclean set is confirmed, not refused. | CLAUDE.md §6 |

Two contradictions inside the spec surfaced while answering these and are now closed: `version` was
both reserved-and-unread and expected to produce conflicts; `conflicts` was to be hard or soft with no
field able to say which. A third correction went the other way — a cycle in `requires` is not a defect
at all, because a project is a set and not an execution order.

---

## The five findings that changed the spec

1. **The failure line.** *(standing guidance for every message the validation pass writes)* Port
   writes `where "Open Critical Vulnerabilities" = 0 · Value: 1` — the condition required and the
   value found. GitHub writes `Process completed with exit code 1`, and a sweep of five major
   repositories found it writes nothing else. The difference is whether the message is emitted at the
   altitude that knows what was required.

2. **Blocking may be the wrong primitive.** *(acted on — CLAUDE.md §6)* Port gates a level and forbids
   nothing; Continue used the same `fatal: true | false` binary we had specified and filed a missing
   dependency as non-fatal. Both poles have shipped. We chose neither.

3. **Cold start is a product decision, not a demo problem.** *(open — CLAUDE.md §11 unchanged)* Linear
   ships a new workspace with four **real** issues — editable, completable, deletable — so the product
   is never empty and the model is learned by holding four instances of it.

4. **The drift indicator is a display problem, not a modelling one.** *(acted on — CLAUDE.md §7)*
   Figma tracks overrides precisely enough to offer `Reset fill` by name, then draws a modified
   instance identically to a clean one everywhere except a context menu.

5. **The pain we bet on is real but quiet; the loud pain is environmental.** *(added 2026-09-01 — see
   [`3-pain/user-pain.md`](3-pain/user-pain.md))* A user reports that two `server-postgres` entries in one
   `mcp.json` end with *"the chat always chooses the first one specified"* — our duplicate-key
   collision, in the file we generate, failing exactly as predicted and telling nobody. That is the
   thesis, sighted in the wild. But it carries 13 reactions against **182** for *MCP Servers Don't
   Work with NVM*, and the top of that tracker is PATH, node versions, platform paths and processes
   dying at startup. Most of that is out of our reach, except at the one place our output meets their
   machine: `SETUP.md`, the pinned `ref`, and the generated config. Two further readings: env and
   secrets rank higher than we assumed, which our `needsEnv` work already serves; and nobody is asking
   for a composition layer, which agrees with the post-mortem about which half of Continue died.

---

## Definition of done

The research phase is finished when:

- [x] Stage 1 — landscape surveyed
- [x] Stage 2 — flows captured, every one closed or declined with reasoning
- [x] Stage 3 — pain evidenced, with the instrument's blind spots stated
- [x] Stage 4 — fifteen benchmark cells scored against five grounded categories
- [x] Stage 5 — five patterns compared on that rubric, one chosen and written into CLAUDE.md §8
- [x] Every question in the register below marked **answered** or **deferred with a stated reason** —
      in one sitting, once stages 4 and 5 were in, not one at a time along the way

**Signed off 2026-09-02.**

**Re-opened 2026-09-06.** The six items above stand. Two more before the phase closes again:

- [ ] Stage 6 — personas built from the inventory, audited, one question re-researched at point
      scale, `personas.html` published, proposals handed back
- [ ] Stage 7 — jobs in canonical form, feature test passed, matrix with no averaged cell, three core
      jobs and the orphan list named, reconciliation against the spec handed back
- [ ] Every register entry raised by stages 6–7 marked **answered** or **deferred with a stated
      reason**, in one sitting, once both stages are in

Next after that: **lesson 03, information architecture** — ~~not started~~ started 2026-09-15, closed 2026-09-20. *Corrected 2026-09-09: this
said "design system", which is lesson 09. Five lessons stand between the two, and CLAUDE.md §1 now
carries the twelve.*

---

## Open questions — the register

> **Where it stands, 2026-09-20.** The paragraph below describes the register as it was in 2026-09-06.
> Since then the sitting was held (2026-09-15) and lesson 03 has raised eight more entries. **Live now:
> Q9 and Q11, deferred at the sitting, plus Q16 and Q17, each raised and part-answered on 2026-09-20
> with one named question left open.** **Q12 is closed as *refused*** — not deferred a second time —
> after the traceability matrix showed it at importance 3 with twelve blank cells. **Nothing is live from lesson 03 as of the evening of 2026-09-20** — Q25 was answered the same day it
> was raised, along with Q26, Q27 and Q28, which the flows' waits-and-failures pass turned up. **Q9 and
> Q11 remain deferred from the sitting, and Q16 and Q17 each keep one named open half.** Q13 to Q15 and
> Q18 to Q28 are answered — **the traceability matrix's seven findings were all disposed of on 2026-09-20,
> four of them building nothing.** **Read the dated sections at the end of this file for the current state; the
> prose here is the protocol, not the status.**

**This is the last section on purpose, and it is a running list.** Questions land here as stages
raise them. They are **not** answered as they arrive. The six that stood here were closed on
2026-09-02 and are recorded below with their dispositions. **Six more are live** — Q7, Q8 and Q9,
raised on 2026-09-06 by the planning of stages 6 and 7, and **Q10, Q11 and Q12, raised on 2026-09-07
by the first practitioner interview.** All six are answered in one sitting once both stages are in.

**The protocol.** When a stage turns up something we cannot settle yet, it gets an entry here and the
stage carries on. Nothing is answered mid-flight, because a question answered on partial evidence has
to be re-opened later, and re-opening costs more than waiting. When stages 4 and 5 are done and the
picture is whole, the register is worked through **in one sitting**, and every entry leaves as either
*answered* or *deferred with a stated reason*. That is the last thing the research phase does before
sign-off.

**Adding an entry.** Give it the next ID, say which stage raised it, and — the part that matters —
say **what would answer it**. A question with no named instrument is not a question, it is a worry.

**Marking an answer.** Since 2026-09-07 every claim about people carries one of three marks, defined
once in [`research.md`](research.md), *The three marks*: **`✓`** confirmed by an instrument another
person can re-run · **`*`** reported by a practitioner in an interview · **`?`** unknown, written `[?]`
in the stage documents and **`данные не подтверждены`** in the digest. **A `*` never becomes a `✓` by
repetition** — only an instrument promotes it, which is why five interviews lift a *provisional*
label and still do not turn a recollection into a measurement. **And, from the mark audit of
2026-09-08 — rule 5 in the digest — a re-runnable query proves that something was *said*, not that it
is *true*.** An issue body, a forum comment and a tool's own README are people describing their own
behaviour: the `✓` covers the utterance, and rule 2 still governs the behaviour under it. Four rows
in [`6-personas/inventory.md`](6-personas/inventory.md) were re-marked for exactly this.

**The prep sheet for the sitting is section 3 of [`FINAL.md`](FINAL.md)** — per question, where to
read before deciding, the options actually on the table, and a recommendation. It holds the
reasoning; this register holds the status. Neither is a copy of the other.

**The evidence was in, and the sitting used it.** Stage 5 was the named instrument for Q1, Q3 and
Q4, and stage 4's B4 work for Q2. What each turned up is recorded at the end of
[`5-patterns/patterns.md`](5-patterns/patterns.md) as *evidence, not answers*; the sitting on
2026-09-02 turned it into the dispositions below. Q5 had no instrument and left the register
deferred, exactly as this section warned it would.

### Closed — the sitting, 2026-09-02

**All six left the register in one sitting, as the protocol required.** Four *answered*, two
*deferred with a stated reason*. The reasoning and what was read before each is in section 3 of
[`FINAL.md`](FINAL.md); this table is the status.

| ID | Question | Disposition | Where it landed |
|---|---|---|---|
| **Q1** | Cold start: demo problem or product decision? | **Answered — a product decision.** Library gains a **scope switch**, `My library` / `Public library`. Public is a curated set that ships with the app, **read-only**, so there is material from the first second. One **example project** ships alongside it, built from public items and containing at least one Problem and one Note. `My library` starts genuinely empty. | CLAUDE.md §8, §9, §11 |
| **Q2** | How much weight does `SETUP.md` carry? | **Answered — more than §6 implied, and the recipient changed.** `SETUP.md` is addressed to **the agent that opens the project**, not to a human reader. It carries what each item in the resolved set requires — dependencies, servers, env keys, external repos at their pinned `ref`, target paths for the chosen agent — so that on init the agent reads it and performs the setup. No verify script in the MVP; it stays additive. | CLAUDE.md §6, §8 |
| **Q3** | Can a project contain another project? | **Deferred — not refused.** Out of the MVP. Two reasons, and the second is the owner's: no variant needed composition to work, **and composition risks unbounded recursion**. Worth revisiting post-MVP, with a depth rule decided before the feature. | CLAUDE.md §9 |
| **Q4** | Can a detached item be promoted back into the library? | **Answered — as a new item**, with the project's row re-linking to it. *Push my changes to the original* is a different action with a different confirmation and is not built. **And the consequence is now explicit:** promotion only has value if a detached item can be **edited inside the project** — otherwise detach is merely unlink. In-project editing is therefore in the MVP. | CLAUDE.md §5, §7, §8 |
| **Q5** | Loss or reassembly cost — which drives adoption? | **Deferred — accepted risk, with the trigger written down.** Nothing in this repository can answer it; trackers are blind to both candidates by construction. Ask five practitioners **before the first feature that only pays off under one answer** — a *reassemble from a previous project* flow versus serious investment in library-wide search. The MVP is the same product under either answer. **Instrument named 2026-09-06: [`6-personas/interviews.md (the guide)`](6-personas/interviews.md#part-1-the-guide). The same event also lifts the provisional label on stages 6 and 7.** | Positioning, and the provisional label on stages 6–7. Nothing in the build |
| **Q6** | Styling engine | **Deferred to lesson 08, design tokens**, with the criterion recorded now: tokens and two real themes first-class, and the engine must not push utility classes into components that are themselves the product's value. Decide on two built components. | CLAUDE.md §10, §12 |

**What the sitting did not change.** No answer added a surface. Q2 lands as two more stages inside
Run, which is already a stage list; Q1 lands as a scope switch inside Library, which is already a
browse screen; Q4 lands as a command on a project row, exactly where stage 5 predicted. **CLAUDE.md
§8 therefore stands as written** — three surfaces plus Projects — and the *provisional* marks are
gone from it and from [`5-patterns/patterns.md`](5-patterns/patterns.md).

**Two answers widened the MVP**, and both are recorded as scope rather than smuggled in as detail:
a curated public library ships with the product (Q1), and `SETUP.md` becomes a real artefact written
for an agent rather than a one-line courtesy (Q2). Both were the owner's calls, taken with the
evidence in view.

### Live — raised 2026-09-06 by the planning of stages 6–7

**Not answered now.** The protocol holds: they leave the register in one sitting, once stages 6 and 7
are done and the picture is whole. Each carries a named instrument, which is what makes it a question
rather than a worry.

**Q10, Q11 and Q12 were added 2026-09-07**, raised by the **first practitioner interview**
([`6-personas/interviews.md (interview 1)`](6-personas/interviews.md#part-2-interview-1-of-5)) and recorded in
[`6-personas/inventory.md`](6-personas/inventory.md) as NK-21 to NK-23. All three stand on **one
person** — mark `*` — which is why they are entries here and not findings anywhere.

| ID | Question | Raised by | What would answer it | Blocks |
|---|---|---|---|---|
| **Q7** | Who is the primary persona — the practitioner whose pain is *sighted* (an archive that lands and does not run; a key that silently wins) or the collector §3 describes (large corpus, wants to find and reuse)? | Stage 6, step 3 | The five practitioner conversations Q5 names, run against [`6-personas/interviews.md (the guide)`](6-personas/interviews.md#part-1-the-guide); plus a GitHub search for repositories carrying `.claude/`, `CLAUDE.md`, `.cursor/rules`, `AGENTS.md`, which observes where material lives and how many targets one person keeps | Which persona wins design conflicts — empty states, what a card carries, the register of validation copy |
| **Q8** | Is the main job *assemble a set that holds together* (§2, owner's assertion) or *hand a set to a machine and have it run first time* (stage 3, observed)? If both survive, the lesson's rule says two products. | Stage 7, step 1 | The same conversations, asked as situations (*what did you last do with a skill you already had; what happened the last time you moved a setup to another machine*), never as pitches; the matrix's main-job row with sourced cells | Positioning; the relative weight of the Project screen and Run in mockups |
| **Q9** | Which specified features close no evidenced job — candidates: the public library switch and example project, duplicate project, promote, the target selector, library-wide search? | Stage 7, step 5 | The matrix's *feature* column, then Q7/Q8's conversations for the `[?]` rows. Absence in the trackers is not evidence of no job, so this closes only with people asked | Mockup scope. Not the design system |
| **Q10** | When the user's own rule and an **external** requirement conflict — a client's linter, a repo convention — which wins, and where does the product put that? | Stage 6, the first interview (NK-21) | The remaining four conversations, asked as a situation (*what happened the last time your own rule and the project's tooling disagreed*). §6 models conflicts **between our items** and the data model has nowhere to put this one | The `Item` model, and what the validation pass is allowed to claim |
| **Q11** | If roughly half of what makes a setup work was **never written down**, what is the ceiling on validating the written part? | Stage 6, the first interview (NK-22) | The same four conversations, plus the NK-13 test: hand a coherent archive to a fresh agent and see what still does not transfer | The promise the product makes at handover. Not the build |
| **Q12** | Is the wanted thing **observability of what ran** rather than **validation that a set coheres**? If both survive, the lesson's rule says two products — the same shape as Q8. | Stage 6, the first interview (NK-23) | Guide Q25 (*what would a genie fix*) four more times, asked before any description of the product. **We cannot build the first** — §6 runs nothing on anyone's machine — so a strong answer here is a positioning finding, not a feature request | `CLAUDE.md` §2's core-value sentence, and positioning |

**Q5 is re-pointed, not re-opened.** Its disposition stands — deferred, accepted risk — but its
instrument was unnamed beyond *five practitioners*. Stage 6 makes
[`6-personas/interviews.md (the guide)`](6-personas/interviews.md#part-1-the-guide) that instrument and stage 7 gives it
the questions. Its *blocks* line widens accordingly: **positioning, and the provisional label on
stages 6 and 7**, because the label lifts on the same event.

### What the closing of stages 6 and 7 did to this register — 2026-09-09

**No question was answered, none was added, and one gained its first evidence.** The protocol holds:
the six live entries leave in one sitting, and that sitting has not happened. What changed is what
the sitting will read.

- **Q9 — *which specified features close no evidenced job* — now has evidence, and it is the first
  ever collected about the persona underneath it.** [`6-personas/re-research.md (round 2)`](6-personas/re-research.md#round-2-counting-not-asking)
  Q-E reached five practitioners on installing other people's material: **four refuse it, minimise it,
  or prefer their own**, and the one positive was distributing **his own** work. The supply side is
  settled and enormous — 19,703 repositories, curated collections at 74,686★ — against **93** public
  personal ones. **This does not answer Q9 and it does not cut anything.** It moves the question from
  *does the shelf close a job* to **what the shelf holds and how it sorts**: *provenance over volume*
  is the only shape any observed person endorsed. Four sceptics on Hacker News are not a market, the
  venue self-selects, and no beginner was asked.
- **Q7 and Q8 are unmoved.** Both need the four remaining conversations. What did move is the ground
  under them: the audit lowered or withdrew six matrix cells, so **the *core three* the sitting was
  going to read is now one job the rule chooses and two kept on stated grounds**
  ([`7-jobs-to-be-done/jtbd.md`](7-jobs-to-be-done/jtbd.md) §8, §11).
- **Q10, Q11 and Q12 are unmoved and still stand on one person.** Q-A sharpened the ground under
  **NK-13** without moving it: in the largest available sample of practice, handover is done by
  `chezmoi`, symlinks, CLI installers and bootstrap scripts, and **two comments in 274 describe an
  agent touching this material at all — neither is a setup.** The spec's bet is *against the grain of
  current practice*, which is a stronger statement than *untested* and still not a refutation.
- **A second proposal list now exists.** Stage 6's nine proposals are in
  [`6-personas/re-research.md`](6-personas/re-research.md) §4; stage 7's nine are in
  [`7-jobs-to-be-done/jtbd.md`](7-jobs-to-be-done/jtbd.md) §12, written as *what was found · what is
  proposed · which entry it belongs to*. **Both are inputs to the sitting, not decisions**, and
  `CLAUDE.md` is untouched by either.
- **What is still owed before the sitting is worth holding:** four interviews, **a receiver's question
  block the guide does not have** — every line about P2 is somebody else's account of them — and
  **NK-13**, the half-day that is ours to run.

### The interviews are unavailable — 2026-09-09, and it is a change of standing, not an answer

**Q5's instrument has been withdrawn by circumstance.** Five practitioner conversations were the named
instrument for **Q5, Q7, Q8, Q9, Q10, Q11 and Q12** — every live entry but none of them fully — and
they are the event that lifts the *provisional* label on stages 6 and 7. **They cannot be run.**

**What this does and does not mean.** It does **not** answer anything, and it does **not** lower the
bar: an unavailable instrument removes an event, it does not make weaker evidence sufficient. The
dispositions stand exactly as written. **What changes is that five entries now point at an instrument
that will not arrive**, and a question with no reachable instrument is, by this register's own rule,
a worry rather than a question.

**What replaces it, in part.** [`6-personas/re-research.md (round 3)`](6-personas/re-research.md#round-3-five-questions-that-need-no-interview) — five
questions answerable **without asking anybody anything**, each with a named instrument, a procedure
and a statement of what it can never establish. They are a different class from rounds 1 and 2: three
read **behaviour left in public artefacts**, two are **ours to run**. Their reach against this
register:

| Entry | Does round 3 touch it? |
|---|---|
| **Q5** — loss or reassembly | **No.** Q-I touches its edge; motive is out of reach of every instrument here |
| **Q7** — who is primary | **Partly.** Q-G is the first behavioural evidence about P2, which is one half of the contest |
| **Q8** — the main job | **Partly.** Q-F tests whether the transfer job's mechanism works at all |
| **Q9** — which features close no evidenced job | **Yes, materially.** Q-I measures whether imported material is kept, which is the behaviour the shelf assumes |
| **Q10** — precedence against an external rule | **No.** A property of judgement |
| **Q11** — the unwritten half | **No.** Q-G hints at its size and cannot measure it |
| **Q12** — observability rather than validation | **No, and nothing can.** It needs a runtime we will not build |

### Round 3 was run — 2026-09-10. No question is answered; three now carry behavioural evidence

**The protocol holds. The six live entries still leave in one sitting, and that sitting has not
happened.** What changed is what it will read: the five questions of
[`6-personas/re-research.md (round 3)`](6-personas/re-research.md#round-3-five-questions-that-need-no-interview) were run in full, and for the first time
this repository has marks that cover a **behaviour** rather than an utterance — two experiments we ran
ourselves, three instruments reading what people did to repositories rather than what they said.
Capture: [`6-personas/_captures/round3-log.json`](6-personas/_captures/round3-log.json) and
[`6-personas/_captures/qf-handover-test/`](6-personas/_captures/qf-handover-test/).

| Entry | What round 3 did to it | Standing now |
|---|---|---|
| **Q5** — loss or reassembly | **Nothing**, as predicted. Motive is out of reach of every instrument here | Deferred, unchanged |
| **Q7** — who is primary | **Partly, and less than it first looked.** Q-G is the first behavioural evidence about **P2**. Its headline — 89.4% of 2,027 forks of personal agent material carry no commit at all — **was withdrawn by its own control**: plain dotfiles 84.8%, ordinary small libraries 87.0%, so the dormancy is a fact about forks and not about handover. **What survives is the 12% who replace the author with themselves**, and the fact that whoever acts, acts within the hour | Unmoved as a question. Its P2 half is no longer `[?]` in every cell, on a modest 25 cases |
| **Q8** — the main job | **Partly.** Q-F tested the transfer job's mechanism and **it works**: three of three receiving agents performed the setup from `SETUP.md`. The job's feature has a working mechanism for the first time | Unmoved. Needs the conversations |
| **Q9** — which features close no evidenced job | **Materially, and it is the second time.** Round 2 gave it opinion; Q-I gives it behaviour. **Thousands of repositories vendor public skills; 32% of traced copies are edited after import, at a median of 27 days; 10% keep any provenance.** The shelf's premise describes something people do | Still open, and now with evidence on both sides of it |
| **Q10** — precedence against an external rule | **Nothing.** A property of judgement | Unchanged |
| **Q11** — the unwritten half | **Nothing.** Q-F bounded a different thing: what the *written* half fails to carry — an item's sibling files, a settings file's executability, the author's identity inside a rule | Unchanged |
| **Q12** — observability rather than validation | **Nothing, and nothing can.** Needs a runtime we will not build | Unchanged |

**Two hypotheses left the board.** **NK-13 / D-1** — *does a receiving agent perform the setup from
`SETUP.md` alone* — is **closed `✓`**, and so is **H6** in [`6-personas/personas.md`](6-personas/personas.md),
which is the same claim. That was the half-day this register has been owed since 2026-09-07.

**Six proposals were raised and none applied**, listed at the end of
[`6-personas/re-research.md (round 3)`](6-personas/re-research.md#round-3-five-questions-that-need-no-interview). One of them is a **change to the data
model** — an item addresses a directory, not a file — which is the first thing any round has proposed
to §5's shape rather than to its reasoning. **They join the two lists already waiting** (stage 6's
nine, stage 7's nine) as input to the same sitting.

**And the label does not lift.** Its trigger is five practitioner conversations. Four hypotheses
closing does not change what the trigger is, and this round says so itself rather than arguing
otherwise.

### Round 4 — 2026-09-10, and this one moved the matrix

**[`6-personas/re-research.md (round 4)`](6-personas/re-research.md#round-4-the-matrixs-empty-cells)**, capture log
[`_captures/round4-log.json`](6-personas/_captures/round4-log.json). Round 3 answered five questions and
moved no importance in the matrix, for a structural reason: its instruments see machines, and the
matrix's columns are people. **Round 4 went after the columns**, in two venues this repository had
never used — **forum.cursor.com** and **community.openai.com**, both Discourse, both with the vendor
answering on the record. 2,140 body hits over 1,929 posts read in full, 955 topics by title, 394 HN
comments, 17 threads read end to end. **Reddit refused again — HTTP 403 — which is R13 unchanged.**

**Three matrix cells moved and all three moved up**, which no round had done before: **RJ-2/P1 2 → 3**
on a vendor-confirmed duplicate-detection failure plus two people who rebuilt their tooling around it;
**EJ-2/P1 `[?]` → 2** and **H-J3/P1 `[?]` → 2**, each on one named person with the thread under it.
The pass is in [`7-jobs-to-be-done/jtbd.md`](7-jobs-to-be-done/jtbd.md) §7.

**What it does to the live entries:**

| Entry | What round 4 did |
|---|---|
| **Q12** — observability rather than validation | **It no longer stands on one person.** [Cursor forum #144731](https://forum.cursor.com/t/rules-not-being-applied-as-expected/144731): a named user with a reproduction repository asks to *"inspect the raw full context window… to tell if it is an issue with AI not loading the rule vs just deciding not to follow them"*, and the vendor confirms rules apply inconsistently. **Public, dated, re-runnable.** The disposition is still the owner's; the question is no longer one interviewee's aside |
| **Q9** — which features close no evidenced job | **Two movements, opposite directions.** *Promote a detached item* was listed as closing a job standing on **nothing**; H-J3 now has a person and a 2. And **P3 was looked for a third time and not found**: the two clearest public beginners wrote their own material on day one, or asked to shadow a human — neither reached for a library, and neither thread got a reply |
| **Q7** — who is primary | **A finding about the population, not about the search.** After four rounds and five venues, **no receiver has spoken in the first person.** Every account of a handover is written by the sender. Pointing register entries at *"ask a receiver"* treats as effort what looks like a property: the person who receives has no reason to post, because the thing they received is not theirs |
| **Q5, Q8, Q10, Q11** | Unmoved |

**One competitor fact for the sitting.** The market's managed answer to distributing a **set** is a
paid tier: the vendor's own resolution is *"wrap the skill as a plugin in the Team Marketplace and
mark it as Required so it installs for everyone automatically… only available on Teams/Enterprise"*,
and the user answers *"Huge unlock."* That belongs beside round 3's Q-J.

**A second pass the same day** turned round 3's own fork corpus on a question nobody had asked it — *a receiver who never posts still leaves a diff* — and filled four more cells: **RJ-3/P1 2 → 3** (the job stated verbatim, then five mechanisms tried and failed), **H-J1/P1 `[?]` → 2**, and **two P2 cells on behaviour rather than accounts** — **RJ-4/P2** on four receivers stripping the author's credentials out of inherited material, **SJ-1/P2** on 30 of 214 receivers writing 21,266 lines of setup and handover manual the sender never shipped. **RJ-1/P1 was hunted on purpose with six targeted queries and stays `[?]`**, which makes the gap §8 calls the widest in the file wider still.

**The day's arithmetic: 36 `[?]` cells this morning, 30 tonight; P1 from seven unknowns to three; P3 unchanged at ten.**

**A third pass closed one more and ended on a wall worth naming.** **H-J7/P1 `[?]` → 2** — the unwritten half, four independent voices, one of whom prices it at *“10–30 minutes every time”*; the cell is deliberately **not** a 3, because all four were found in a venue where having built something is the entry ticket, and counting the building as importance would be circular. **And P3 was hunted a fourth time, by inverting the method**: instead of going where people are, go to **the shelves themselves** — 18 of the largest public collections, **568 issues**. Three real consumers turned up, blocked by exactly what this product exists to prevent: a 4,386★ collection whose agents require an **undeclared `context7 MCP`** so that *“new users… are unable to run these agents as intended, leading to immediate failure and frustration”*; a **first-timer facing a per-file collision prompt** — *“Is this supposed to happen? What should i do here?”* — repeated for every agent; and somebody lost between multiple installed agents. **None of them fills a cell, and the reason is the finding: the blocker on what remains is persona attribution, not evidence.** A public artefact shows an act; a persona is defined by a situation. You can see that somebody installed a stranger's agents and could not run them; you cannot see whether they had material of their own. **P2's five and P3's ten are not waiting for a better query — they are waiting for somebody to be asked.**

**Nothing is applied to `CLAUDE.md`, and the label does not lift.**

**The question this raises and does not answer: what, if anything, may ever lift *provisional*?**
That is the owner's call at the sitting, not a research finding. Three positions are available and
each has a cost — keep the label until conversations become possible; replace the trigger with a
named non-interview event and say what it is; or drop the label and carry the marks alone, which is
what the three-mark system was built to make survivable. **It is recorded here so the sitting takes
it deliberately.**

### The sitting was not held before lesson 03 — 2026-09-15, and it is a change of order, not of standing

**The owner's decision, in their own words: *we work with what we have.*** Lesson 03, information
architecture, started on 2026-09-15 **without the sitting this register has been owed since
2026-09-09.**

**What it does not do.** It answers nothing, applies nothing and promotes no mark. All six live
entries — **Q7 to Q12** — keep the dispositions written above. The four proposal lists stay unapplied:
stage 6's nine ([`6-personas/re-research.md`](6-personas/re-research.md) §4), stage 7's nine
([`7-jobs-to-be-done/jtbd.md`](7-jobs-to-be-done/jtbd.md) §12), round 3's six, and round 4's two
movements. The *provisional* label on stages 6 and 7 stands, on the trigger it has always had. And the
question this register left for the sitting — *what, if anything, may ever lift it* — is still the
sitting's, not lesson 03's.

**What it does do, and it is worth naming rather than assuming.** An information architecture is now
being argued **against the evidence as it stands**: three personas of which **P3 has never been
observed**, a receiver who **has never spoken in the first person**, and a matrix with **thirty `[?]`
cells** — ten of them P3's entire column. The risk is specific: a structure invented for a person
nobody has met reads afterwards as a requirement. **The rule lesson 03 works under is therefore the
one this register already enforces** — where a structural decision would need an `[?]` cell to carry a
number, it says so at the point of the decision and leaves the decision marked. It does not fill the
cell.

**And the protocol is unchanged.** Lesson 03 raises entries here; it does not edit
[`CLAUDE.md`](../CLAUDE.md) §2–§11 in place. Two lists drift.

**One proposal was applied ahead of the sitting — 2026-09-15, and it is recorded here so the sitting
does not decide it twice.** **Stage 6's proposal 6** — *a `license` field the `Item` model lacks, with
the rule that a missing licence is not permission* — was applied to
[`CLAUDE.md`](../CLAUDE.md) §5 and §11 by the owner. **What it does not do:** it answers none of Q7 to
Q12, it promotes no mark, and **the other eight proposals of that list, stage 7's nine, round 3's six
and round 4's two movements are untouched.** **The basis is worth naming because it is not this
register's usual one:** the licence closes **no job** — lesson 03's entity inventory had refused it for
exactly that reason — and it was taken on a **legal** ground instead: we carry other people's work
inside an archive the user hands on, and absence of a licence is absence of permission. **A second
question was deliberately left open**: whether a user's *own* external item with no stated licence
produces a **Note**, the way an external item with no pinned `ref` already does (§6). That would create
a finding, and a new finding changes what the validation pass claims.

### The sitting — 2026-09-15, held on lesson 03's doorstep

**All six live entries left the register in one sitting, as the protocol requires.** Two *answered*,
four *deferred with a stated reason*. The owner took them; this section holds the status and the
reasoning together, because unlike 2026-09-02 there was no prep sheet written in advance — the sitting
happened when lesson 03 needed the answers rather than when the picture was whole, and that is itself
part of the record.

| ID | Question | Disposition |
|---|---|---|
| **Q7** | Who is the primary persona | **Answered — the collector.** The merge in [`personas.md`](6-personas/personas.md) is resolved toward its **collecting** half rather than its handover half: the person with an accumulated corpus is who the product is for, and who wins a design conflict |
| **Q8** | Which is the main job | **Answered — *assemble a set that holds together*.** `CLAUDE.md` §2 stands as written. The *transfer* wording the evidence produced is recorded in [`jtbd.md`](7-jobs-to-be-done/jtbd.md) §1 and **is not adopted** |
| **Q9** | Which specified features close no evidenced job | **Deferred — skipped deliberately.** Nothing in lesson 03 turns on it, and it is the one entry whose evidence bears on *what the shelf holds and how it sorts* rather than on *whether it ships*. It cuts nothing either way, so answering it now would spend a judgement for no gain |
| **Q10** | Whose rule wins, mine or an external one | **Answered — the external requirement wins, and the product must say when it disagrees.** A client's linter or a repo convention beats the user's own rule. **The disclosure half is the answer; the detection half is an open problem** — below |
| **Q11** | The unwritten half | **Deferred — to a section of its own.** It bounds the ceiling of the entire product and deserves to be worked rather than answered in a line |
| **Q12** | Observability rather than validation | **Deferred.** §6 runs nothing on anyone's machine, so a strong answer here is a positioning finding and never a feature. Parked with its evidence intact |

#### Q7 — what the answer does, and the one thing it does not do

**The collector is primary.** [`personas.md`](6-personas/personas.md) had refused the contest the plan
expected: the one practitioner asked said *"the collection created the problem"*, so P1 was written as
the **merge** of the collector and the person who breaks at handover. **This answer resolves that merge
toward collection** — the corpus is the situation the person arrives from, and the surfaces that serve
it win conflicts.

**Read against the evidence, plainly, because it does not go with the grain of it.** The loudest
evidenced demand in the whole base is the transfer family — **6,592** for one source across agents,
**182** for an archive that lands and does not run — while the collector's own job, *lay hands on
something I wrote months ago*, is a **hypothesis job at importance 2 standing on one named person**, in
the flow the market serves best (B1) and where our evidence is thinnest. **The decision is the owner's
and it is taken with that in view.** What it costs is that two things now lean on the weakest evidence
in the folder: library-wide search, and whatever the Library screen becomes.

**And what it does not do.** It does **not** remove §6's handover investment — `SETUP.md` written for
the receiving agent, the pinned refs, the target selector, the disclosure stages before Export. Those
stand on the loudest numbers in the base **and on the only behavioural test this repository has ever
passed**: three receiving agents out of three performed the setup. **They stop being *the point* and
remain *the mechanism*.** Anything stronger — cutting handover surfaces because the primary persona
changed — is not what this disposition says and is not applied.

#### Q8 — §2 is confirmed rather than edited

The main job as the evidence words it is a **transfer** job; §2 words the value as **assembly with
validation**. [`jtbd.md`](7-jobs-to-be-done/jtbd.md) §1 stated the difference and did not apply it, and
**proposal R-1 asked for the difference to be stated inside §2.** The answer settles it the other way:
**§2 stands unchanged, and R-1 is closed without being applied.** Assembly is the product; the move is
what assembly is for. Consistent with Q7 — both answers choose the corpus over the handover as the
product's centre.

#### Q10 — the answer is disclosure, and detection is the unsolved half

**Answered:** where the user's own rule and an external requirement disagree, **the external one wins**,
and **the product must notify about the mismatch** rather than resolve it silently.

**The obstacle, stated before anything is designed against this.** §9 refuses automatic metadata
parsing, and nothing in the product can see a client's linter, a repo convention or a team standard —
they live on a machine we never touch. **So a mismatch cannot be *detected* by anything the MVP
contains.** The answer is buildable only in the direction of disclosure:

- an item can **carry a declared external constraint**, the way `requires` and `conflicts` are declared
  by hand (§5), and
- the product can **show it wherever that item sits in a set**, stating that the external rule takes
  precedence — which is a **Note** in §6's sense rather than a Problem: the archive is correct, the
  reader is not fully informed.

**Not applied.** It needs a field on `Item` and a line in §6, and it is recorded here so that lesson 03
can leave it a place without inventing the mechanism.

#### The *provisional* label — decided, and it is dropped

**The register asked what, if anything, may ever lift it, named three positions and left the choice to
the owner. The owner delegated the choice. It is taken here, with its cost.**

**Position (b) — replace the trigger with a named non-interview event — is refused on this
repository's own finding.** Round 3 said it in its own words: *importance is a fact about somebody, and
this round asked nobody anything.* No artefact instrument reaches motive or feeling, so naming a
substitute event would **lower the bar while keeping the word** — the one outcome the three-mark system
was built to prevent.

**Position (a) — hold the label until conversations become possible — is refused because the trigger
cannot occur.** A warning whose condition can never be met stops being a warning and becomes
furniture, and work is already being built on these documents.

**Position (c) is taken: the blanket label is dropped, and every mark stays exactly where it is.** The
argument is the evidence rule's own **rule 1** — *the mark is per claim, not per document* — and the
audit's counts, which show one word doing two wrong things at once: it **over-warns** about P1, which
carries 20 `✓` against 5 `[?]`, and it **under-warns** about P3, which carries 2 `✓` against 6 `[?]`
and is the persona two shipped surfaces already serve.

**What dropping it does not do, and this is the whole safeguard. No mark is promoted.** Every `*` stays
a `*`, every `[?]` stays a `[?]`, the four owed interviews stay owed and unavailable, and each document
keeps a **standing block** in place of the label: the counted split, what the card may settle, and what
it may not. **The warning becomes finer-grained rather than absent** — which is what three marks were
for.

### Raised and answered the same day — 2026-09-15, the run's lifetime

**Lesson 03's entity inventory turned up a gap rather than a question about people**, so it did not
wait for a sitting. [`CLAUDE.md`](../CLAUDE.md) §6 and §8 give the validation pass an entire surface
and §5 had **no object for a run or for a finding** — so *does last night's check still exist this
morning* had no answer anywhere in the specification, and the architecture could not be drawn without
one.

**Answered: the run is a moment.** Nothing is stored — no run id, no list, no history, nothing to link
to. What survives lands on the **project**: `checkedAt`, `checkVerdict` as counts, and `checkTarget`.
**The verdict is void the moment the resolved set changes** — including when an item the user never
touched is edited in the library, because `requires` pulled it into the set — and the product names
**what** voided it rather than only that something did.

**Two things were decided with it and both are refusals.** The status word is **checked**, never
*works*: we start nothing, open nothing and read no `SETUP.md`, so a claim about the receiving machine
is one this product cannot make — the same argument that gives *Skipped* its own neutral glyph. And a
**stale verdict is not shown at all**, greyed or otherwise, because a claim that is no longer true is
the unearned tick §6 exists to refuse; the date survives, the verdict does not.

**Standing.** This is a decision about our own mechanism, not a claim about people: **no mark, no
persona and no matrix cell is involved**, and nothing in the four proposal lists moves. It is recorded
here because the register is the only list, and because lesson 03 is meant to raise entries rather
than edit the spec — this one was edited on the owner's own answer, the same hour it was raised.

### Q13 — raised 2026-09-15 by lesson 03, and by a correction to how it was being argued

**One entry is live again.** The register emptied at the sitting the same morning; this is the first
question after it, and it arrived because an argument was found to be built on the wrong thing.

**What happened.** Lesson 03's screen tree concluded that **the receiver needs no screen**, since a
handover is a file and the receiver never opens our product. The owner raised the obvious case — *a
receiver can be sent a link to a public project or item* — and the answer given was that this is
post-MVP, on three reasons of which **two were about implementation**: storage is one browser, there
is no backend. **The owner rejected that order of reasoning and is right to.** *If it matters to the
person, it is in the MVP; how it is built comes after.* The implementation reasons are struck in
[`03-information-architecture/sitemap.md`](../03-information-architecture/sitemap.md) and what remains
is a product question.

| | |
|---|---|
| **Q13** | **Is sharing a link — to a project, and possibly to an item — in the MVP?** |
| **Raised by** | Lesson 03, the screen tree, and the owner's correction that implementation may not decide product scope |
| **What would answer it** | **No instrument reaches it** — this is a scope decision, not a finding. What the evidence *bears* on it is listed below, and it points both ways |
| **Blocks** | Whether **P2 has a screen at all**; whether `visibility` becomes a control §9 currently hides; step 3's routes, since a shared page is a route with a different audience; and §9's own asymmetry between consuming a shelf and publishing to one |

**What the evidence says, and it does not settle it.**

- **For.** The main job is transfer and it is the loudest thing in the base — **6,592** and **182**. A
  file still needs a channel; a link removes that step. And it is **the only route by which P2 ever
  gets a screen of ours.**
- **Against.** **Nobody observed asks us for a link.** Handover in the largest sample of practice is
  `chezmoi`, symlinks, installers, bootstrap scripts, git and forks. **SJ-2 scores 1** for the primary
  persona, on an absence looked for twice — **0 of 1,762** Hacker News comments mention a portfolio.
  And the screen it would create is **for a persona who has never spoken in the first person** in five
  venues and four rounds.
- **Sideways.** The market's answer to distributing a **set** is a **paid team tier**, answered by a
  user with *"Huge unlock."* That says distribution is worth money to somebody; it says nothing about
  our person wanting it from us.

**Four sub-questions that have to be answered with it, not after it.** They are product questions and
none of them is about a build:

1. **A link to what** — a project, an item, or both.
2. **Snapshot or live.** §5 links items live *inside* this product; a receiver whose setup changes
   under them is a different proposition, and the archive is a snapshot by nature.
3. **Who may open it.** *Anyone with the URL* is the low-ceremony answer flow 12 found in the survey.
   *Named people* means accounts, which §9 refuses and which is a much larger product.
4. **What a shared surface must never carry.** RJ-4 gets **sharper**, not softer: the only thing ever
   observed on the receiving side is four people stripping the author's credentials out of inherited
   material, and a receiving agent copying a live OAuth token out of a keyring.

**And one thing this entry puts under review without answering.** §9 hides the `visibility` control
with the reasoning *there is no server to publish to* — **which is the same kind of reason that was
just struck.** If Q13 is answered yes, §9's asymmetry is re-decided with it; if no, §9 should say so on
a product ground rather than on an absent backend.

### Q13 answered — 2026-09-15, the same day it was raised

**Answered: yes.** A link is in the MVP. The owner took it as a product decision, with the evidence
above in view and pointing both ways, and the four sub-questions were answered with it rather than
after it.

| | Answer | What it commits us to |
|---|---|---|
| **A link to what** | **Both** — a project and an item | Two read-only surfaces, §8 |
| **Snapshot or live** | **Live** | Sharing is a **standing decision**, not an act: every later edit is also a publication. §5's blast radius gains a third altitude |
| **Who may open it** | **Anyone holding the link** | No accounts, no named viewers — **§9's refusal of accounts is untouched**, because the viewer is anonymous and the owner is still the only user. The link is the credential, so it must not be guessable |
| **What it must never carry** | **Delegated to the design**, and taken as below | One refusal, one disclosure moment, and one guarantee that costs nothing |

**The boundary that keeps this from becoming a different product.** §9 refused *publishing to a public
catalog*; that refusal is **narrowed, not reversed.** A link is an **unlisted address** — nothing is
listed, searched, ranked or moderated. **A link is a handover; a catalog is a marketplace**, and the
evidence puts somebody in need of the first and nobody in need of the second: SJ-2 scores **1**, and
the portfolio absence was looked for twice and found twice.

**And §9's *no dead toggle* rule is satisfied rather than broken.** `visibility` was hidden because
nothing could act on it. Something can now, so the control appears — which is the same rule producing
the opposite outcome, as it should.

#### What the fourth answer became — *"protect the keys and everything else"*

**Three layers, and the first is free.** `needsEnv` holds **names and never values** (§5), so a shared
surface **structurally cannot leak an env value**. That is a property of the model rather than a
promise about our care, which makes it the strongest thing here.

**Second, the one refusal in the product — and it lasted one day. Overruled 2026-09-16; see *The
credential refusal is overruled* below. The paragraph is left as it was written, because the reasoning
that fell is the point.** §6 refuses to block, and its stated premise is *the user's
own library on their own machine* — **sharing breaks that premise**, which stage 6's **proposal 8**
had already flagged as weakened. So: **a credential found in item content stops the share.** The
reason is irreversibility, not tidiness — a bad archive sits on your own disk and can be rebuilt; a
key on an address anyone can open is out, and unsharing does not recall it. **Everything else is
disclosed and blocks nothing.**

**Third, sharing is a disclosure moment in the register this project already uses.** Before the link
exists, the product names in the present tense what becomes visible — the items, that their **content**
is visible, the env key **names**, the external repos. The model is Notion's *"anyone with the link can
view this page's content and see contributor names"*, which is the trust trigger the research recorded
**for the receiving side** specifically.

**And what it deliberately does not claim.** We cannot detect the thing a practitioner actually
described — *the private and the reusable are tangled in the same files*: a client's internal API shape
in an example, a rule naming a client, **an env key whose own name names a customer.** Those are a
Note, not a scan result, and pretending otherwise would be the unearned tick §6 exists to refuse.

**What this does not settle.** Whether anybody wants the link remains unmeasured: **no instrument
reached it, none was claimed, and the decision was taken on product grounds with the evidence against
it recorded in full.** If it turns out to close nothing, the thing to revisit is **two surfaces**, not
the model — `visibility` and `shareRef` cost nothing when unused.

### The receiver runs the check — 2026-09-15, and it closed the collision Q13 opened

**The question was the owner's and it was one sentence: why can the person holding the link not run
the check?** There is no reason, and the architecture had nearly invented one — Run had been
classified as a mode of the *Project*, the Project is the owner's place, and a description of the
owner's surfaces was being read as a law about the receiver's.

**Answered: the receiver runs the same check, on the set in front of them.** Every input is data the
shared page already carries — `requires`, `conflicts`, command names, target paths, `needsEnv` names.
No machine is touched and nothing is revealed that the sharing disclosure had not already made
visible.

**It closes the collision this register recorded hours earlier.** A live page plus a verdict that
voids on change meant a receiver could be looking at a set nobody had checked in that state. **With
the check in their hands the staleness stops mattering**: the only verdict worth anything is the one
taken now, by the person looking at it. The page still states **when the owner last checked and
whether the set has changed since** — facts, not a substitute verdict.

**Three things are deliberately unchanged.** The ceiling: their check says *this set coheres*, never
*this will run here*, because `needsEnv` holds names and their machine is not ours — **checked, never
works.** The storage: **nothing is kept for a visitor**, who owns no project to carry a date. And the
evidence standing: this gives P2 a screen and a verb, and **P2 has still never been asked anything**,
so it is a decision with an unobserved person on the other end of it.

**One observation, recorded as an observation.** The receiver's path — open the link, read the set,
check it, read what the machine still needs, take the archive — **is the product's whole spine
performed by somebody who owns nothing.** It was not designed as an answer to cold start and it is not
claimed as one: **H-J4 and P3 are exactly as `[?]` as they were.**

### The credential refusal is overruled — 2026-09-16, and the product refuses nothing again

**The owner's decision, answering the first of the two questions lesson 03 had left standing.** It was
raised as *confirm or overrule*, and it is overruled. **§6's *nothing blocks* has no exception again.**

**The reason given, in the owner's words.** GitHub takes everything, and *it is not realistic to check
all of it*. **What that strikes is detection, not irreversibility** — the original argument's
irreversibility half was never disputed and is still true. But the refusal rested on both halves, and
with detection gone it rested on nothing: **a block standing on a scan we do not trust stops the file
that was fine and lets through the one that was not**, and it spends the user's trust doing it,
because a product that refuses is read as a product that looked.

**And the specification was already contradicting itself on the point.** §6 said in one paragraph that
a credential is detected and blocks, and in the next that the tangled private-and-reusable case
**cannot be detected and must not be pretended at.** Only one of those two survives a hard look, and
it is the second.

**Two things the overrule exposed that the refusal had hidden.**

1. **The guard was on the newer of two exits.** Content leaves this product in an **archive** and — as
   of Q13 — on a **link**. The archive has never been checked for a key and nobody proposed that it
   should be. Guarding the share alone was a guard against the exit we had just invented.
2. **The nearest real system lands where the owner did.** GitHub's push protection scans, blocks —
   **and is bypassed with a stated reason.** The best-resourced detector in the industry treats its own
   finding as a warning.

**What replaces it, and where.** A **warning at the moment the user's own material comes into the
library** — one item, or the whole library as JSON — saying **check that these files carry no keys**,
and naming why: what comes in this way goes out in every archive built from it and, if it is ever
shared, onto an address anyone can open. **It is a reminder and it says so** — *we do not read your
files looking for secrets* — so it is **not one of §6's three severities**, because nothing was
checked. **It does not block.** Written into **§11**, with §6 recording the supersession.

**What is unchanged.** The **disclosure at the moment of sharing** — which items, that their content is
visible, which env key **names**, which external repos — stands exactly as written; it is now the
sentence carrying the keys at the moment they stop being recallable. And the free guarantee stands:
`needsEnv` holds **names and never values**, so a shared surface **structurally cannot leak an env
value**.

**The standing of this decision, stated plainly.** It is a product decision taken by the owner, on
grounds of what is realistic to build, and **no instrument was run for it** — as against the original
refusal, which also had none. Stage 6's **proposal 8** remains what it was: the observation that
sharing weakens §6's *only the user is at risk* premise. **That premise is still weakened, and the
answer to it is now a warning rather than a block.**

### Q10 gets its mechanism — 2026-09-16, and it is a Note

**The sitting answered Q10 and left it unbuilt**, which made it the one disposition still owing a
mechanism. Built today, in the shape the sitting itself specified: **a declared field and a Note.**

**`defersTo` on `Item`** (§5, *Deference*) — a hand-declared list naming the external authorities this
item yields to, in the user's own words: *the client's ESLint config*, *the repo's commit convention*.
Declared exactly as `requires` and `conflicts` are, and for the sitting's stated reason: **§9 parses
nothing and the other machine is never ours.**

**The name is the answer.** Q10's content is **precedence** — the external one wins — so the field says
that and nothing else. It is not a description of the external rule: we do not know what that rule
says, whether it still holds, or whether it disagrees with anything here. **One fact: when these two
disagree, that one wins.**

**A Note, per the recommendation, and it is stated where four different readers meet the item.** The
Note on the item's own row for the owner (§6, §8); the shared page for the receiver (§8); and
**`SETUP.md` for the agent** (§6) — which on reflection is the sharpest of them, because it is the only
reader **standing on the machine where the other rule lives**, and therefore the only one that can act
on the sentence rather than note it. Acting on it is what the answer asks for.

**One property recorded rather than discovered later.** This Note is unlike the other two: a missing
env key clears by supplying it, an unpinned `ref` by pinning it, **a deference clears only by removing
the declaration or the item.** A set with three deferring items carries three Notes at every check for
as long as it exists. **That is intended** — the complaint being answered is *"there's no precedence
anywhere"*, and a fact that stops being said stops working — but it means **the note count is not a
to-do list**, and §6 says so where the counts are specified.

**Standing, unchanged by building it.** The evidence under Q10 is **one practitioner, from memory** —
`*`, the [interview Q26](6-personas/interviews.md#part-2-interview-1-of-5) aside — and *what happened
the last time your own rule and the project's tooling disagreed* is still on the guide for the four
conversations that cannot be run. **Building the mechanism does not promote the mark.** What it does
remove is the sitting's outstanding item: **no disposition from 2026-09-15 is now owing a mechanism.**

### `Item` stays a form — 2026-09-16, and §8 is kept as written

**Lesson 03 raised it as a proposal and the owner rejected it, in three words: *we go by §8*.** The
Library holds an **add/edit form**; there is no `Item` place, and the product's navigable surface drops
from six addresses to **five** — Library with one address per scope, Projects, Project, and the two the
link creates.

**What was argued, so that the rejection is a decision and not an omission.** Two things pushed toward
a place. *Used in 3 projects* is a **count that is also a link** — the benchmark's best consequence
disclosure, VS Code Workspace Trust at C2 = 5 — and a count you cannot follow is Figma's *423
instances*, scored a step lower for exactly that. And editing a linked item has **blast radius** that
§5 wants legible *before* the edit, with a second half since 2026-09-15: the edit **un-checks every
project whose resolved set contains the item** (§6).

**The counter-argument, which is the one that won.** The primary persona keeps **tens of items, not
hundreds** — counted, not assumed: four public trees hold 11, 25, 47 and 48. **An address per item is
a place invented for a scale this product does not have**, and every place costs a route, a set of
empty states and a decision about what lives on it.

**What the decision costs, recorded rather than absorbed.** The requirement the argument rested on does
not disappear with the place, so it is re-homed:

- **The count expands where it stands.** *Used in 3 projects* opens on the Library row, naming the
  three, and **each name leads to the Project**, which is a place. **The item is not addressable; what
  the count is about still is.** This is weaker than a link to the item and it is named as weaker.
- **Blast radius moves to the head of the form**, which is now its only possible home: §5 requires the
  radius before the edit and never named a surface, so the form **states it before any field is
  editable** — *used in 3 projects · saving un-checks all three* (§6). A form that discloses before it
  accepts is not what the argument objected to; what it objected to was a form that discloses nothing.

**One asymmetry worth keeping in view.** A **shared item** is a place — the link is its address (Q13) —
while **the owner's own item is not.** The product can address an item, just never one of yours. Not a
contradiction: the shared page exists because somebody outside holds nothing else. **But it is the seam
to look at first if this is ever reconsidered**, since half the surface would already be built.

**It unblocks steps 3 and 6** — routes, and the item in six contexts and six states — which were
waiting on exactly this.

### Q14 — the library panel replaces the palette — raised and answered 2026-09-20

**Raised by lesson 03, and by the owner saying plainly that the mechanism did not feel usable.** The
chosen shape put **no library surface inside the builder**: `⌘K` summoned a palette, the palette added
by name, and the corpus was otherwise absent from the Project screen. **Answered the same day, because
two of the three things that had held the refusal turned out not to be holding it any more.**

**The answer. A library panel lives inside `Project`.** A scope switch — `My library` · `Public
library` — **above** tabs by `kind`, with **`Related` first and default**: the ones that require, or
are required by, what is already in the set. Search filters within the current scope and tab. **A zero
result still carries the row that creates**, which is P2's Obsidian finding kept rather than dropped.
**The panel reads and adds. It never edits.** And **drag is not the mechanism** — a row is checked, or
it is added from its row; the gesture that killed P1 does not come back with the pane.

**Removal is owned by the project row.** An `✕` on the row takes the item out of the set, **and that
unchecks it in the panel**. One fact, two places, and the place that owns the action is the one where
the item's membership actually lives. **The auto-added row still refuses** — §6's only refusal in the
whole product — and the panel inherits it rather than softening it: a checked row held by a puller
cannot be unchecked from either side, and what it says is *remove what dragged it in*.

**`Library` leaves the assembly path, and that is the second half of the answer.** In the owner's
words, *during building a project we will not open the library, there is no need*. So the two surfaces
divide rather than duplicate: **the panel answers *what goes in this set*; the Library answers *what do
I own*** — read, curate, edit, add, delete, usage facts, copy from the shelf, share an item, JSON in
and out. **The panel is therefore load-bearing in a way the palette was not**: during assembly it is
the only surface the corpus has, and if it is weak there is nowhere else to go.

**What shifted, stated separately from what was decided, because they are different kinds of thing.**

- **Evidence, and it is a correction rather than a new finding.** P1 — *two-pane drag* — lost stage 5
  on two scores, and one of them **no longer applies**. **C5 = 2**, *economy*, was awarded because
  *"half the screen is inert during the check and during export"*. That was true of P1 as drawn, where
  validation lived in the right-hand pane. **The chosen hybrid moved the check onto its own surface**:
  `Run` takes the whole screen and the Project is not on it. **A pane that is not on screen during the
  check cannot be inert during it.** The score stands as the historical record of P1-as-drawn; it is
  not an argument against a pane in today's architecture, and anybody reaching for it should be told
  so. See the dated note at the end of [`5-patterns/patterns.md`](5-patterns/patterns.md).
- **And what the proposal is *not*.** It is **not P1**. `patterns.md` says of P1 that the mitigation
  for drag-at-scale *"is click-to-add — at which point drag is no longer the mechanism and P1 has
  quietly become P2 with an extra pane."* **A checkbox is click-to-add.** So what was decided here is
  **the chosen variant plus a pane**, not the rejected variant restored, and the question it turns on
  is narrower than the one stage 5 answered: *is the pane worth what it costs?*
- **Judgement, and it is the owner's.** The cost is real and is not waved away: the item **renders
  twice** — as a panel row and as a set row — and the panel structurally cannot show *detached*,
  *auto-added by X* or *conflicting*, which is why P1 scored C1 = 4 rather than 5. **What buys it** is
  C1 itself: *what else do I own that fits here* is the one question the palette could not answer, and
  it is the primary persona's own ground.
- **No mark is promoted by any of this.** The owner's discomfort with the palette is a practitioner
  reporting their own experience — **`*`**, exactly like every other sentence from the same source.
  Nothing here is `✓`, and the panel is not evidenced, it is decided.

**Amended the same day, in the owner's review of the flows: the panel lives in a mode.** Reading the
main flow aloud, the owner rejected the empty-state node for naming a dead control, and then said the
larger thing behind it: ***the project and its editing — adding and removing items — are separate
states of the screen.*** **Taken, with one correction of vocabulary**: nothing about the *data* decides
which one you are in, your *intent* does, so by this project's own four tests it is a **mode**, not a
state.

- **`Project` has two modes.** *Viewing* the set, and *configuring* it. **The panel, the membership
  checkbox and the `✕` exist only in the second.** The set is not editable by accident.
- **It is the same logic as the owner's other thought that morning** — that the main action should be
  Export and the check a sub-process. **What a project is in repose is a thing you send; changing it is
  an act you enter.**
- **It adds a mode and no place.** Five still, re-checked against the same four tests.
- **And it moves a number the navigation section had called immovable.** The empty project's one action
  is the entry into configuring, so **path B is four clicks, not three.** A and D are still three, so
  the floor holds; what fails is *the floor is indifferent to whether the set exists*. **The fourth
  click is a mode entry, not a traversal**, so the finding under the number survives.
- **`Run` stays reachable from both modes, and that part is derived rather than decided.** The
  fix-and-recheck loop — find a Problem, act on the row, check again — is the busiest path in the
  product, and charging it a mode exit every cycle would tax the flow §6 is built around. **Nobody
  asked for this half; it is marked so it can be disagreed with.**

**Three things the answer buys that were not the reason for it**, recorded because they are the kind
of thing that later gets mistaken for the argument:

1. **The excursion dies.** In the main flow, a palette that matched nothing sent the person out to
   `Library`, on to `Public library` and back — **three screens of detour in the middle of assembly**,
   which existed only because the palette searched one scope. A scope switch inside the panel absorbs
   it, and **the person never leaves the Project screen.**
2. **Cold start is answered inside the builder.** `My library` is empty on first run by §11; a panel
   opening on `Public library` puts real material where it is needed in the first second. P1 could not
   do this — an empty pane was its worst moment — and it is only possible because the shelf exists.
3. **The Library becomes what Q7 made primary.** With assembly served by the panel, the Library stops
   being a station on a route and becomes **the curator's room**, which is the collector's own ground.
   **Navigation finding 4 — *no path to the main job passes through the Library* — stays true and
   becomes deliberate**, where it was previously a tension to watch.

**What it does not settle, and both go to step 5.** Whether the control is a checkbox or a click, and
how a **held** row — checked, and refusing to uncheck because a puller holds it — reads without looking
broken. And **the width**: the Project row is the widest thing in the product — name, kind, *required
by X*, *detached* with its differing fields named, plus a finding's `item · rule · observed value` — and
C3 = 5 was awarded for having the full width for it. **That is measurable rather than arguable**: write
the longest real row and see whether it survives 1440 minus the panel.

**One idea parked.** **`⌘K` surviving as a keystroke that focuses the panel's filter** is kept as an
idea and **deferred to lesson 04**, to be looked at in a wireframe rather than argued in prose. It is
not in the spec.

### Q15 — a single item exports on its own — raised and answered 2026-09-20

**Raised by the owner, from the Library's side**: an item is a block, and a block should be able to
leave without a project being built around it. **Answered yes**, with the one fork named and taken.

**The reasoning the question came with, and the part of it that is exactly right.** *The project is
what gets checked and set up; a single item is independent.* The first half is the product's whole
claim: **every Problem in §6 — a duplicate command name, a target-path collision, a declared conflict —
needs at least two items.** One item cannot collide with itself. That is the set-level object the
benchmark found nobody has: four skill managers run against a deliberately broken set, and **not one
saw a defect of the set**.

**The part that is not right, and it is where the fork is.** An item is **not** unconditionally
self-contained. Four fields on `Item` survive its removal from any project: **`requires`**,
**`needsEnv`**, **`defersTo`** and **`targetPath`** — and the last means **an agent target must still
be chosen**, because without one there is nowhere to put the file. An **external** item is not a file
at all: it leaves as an instruction to clone at a pinned `ref`, exactly as it does inside a project.

**The fork: what happens when the one item requires another.**

- **Ship the bare file.** Hand over something that will not run — which is precisely the pain the whole
  product exists against: *the archive lands on a machine and does not work.*
- **Run the walk anyway.** Then one item becomes a set, and a set is what we already know how to
  handle.

**Answered: the walk runs**, and the result is **named honestly as a set of N items** rather than
presented as one. Nothing new is invented; it is the existing mechanism with an unnamed set.

**Two consequences, and they are derived here rather than stated by the owner** — flagged so they can
be disagreed with on their own:

1. **The severity rule needs its exact form, and it took two attempts to get it.** *A single item
   cannot produce a Problem* is loose. **The first correction was also wrong** — it said *a bare item,
   one whose resolved set is itself, cannot produce a Problem*, and **Q17, answered the same hour,
   creates the counter-example**: an item whose only `requires` points at something deleted has a
   resolved set of exactly itself **and raises an unresolvable requirement**, which §6 lists as a
   Problem. *Found by the review of 2026-09-20 and corrected in §6, in E1, and in the single-item
   flow.*
   **The rule is about the field, not the count. An item with an empty `requires` cannot produce a
   Problem. Any `requires` edge makes it a set question**: resolved, the walk builds a set that
   collides like any other; dangling, the edge fails on its own. `Notes` — a missing env name, an
   unpinned `ref`, a deference — are item-level throughout and survive alone, so a single-item export
   producing **Notes and no Problems** remains the ordinary case.
2. **It enters `Run`.** The same mode, from a Library row, as a **third entry point** beside `Project`
   and `Shared project`. Everything it needs is already there — the target selector, the `SETUP.md`
   preview, `.env.example`, Export as the final stage — and for a bare item most stages are `Skipped`,
   which is what that glyph is for. The alternative, **a lightweight export dialog, is a new surface**,
   and this architecture has gone five flows without adding one. **Nothing is stored either way**: §6
   puts the verdict on the **project**, and there is no project here — the same rule that already
   governs a visitor's run.

**And it is not a new concept from the receiver's side.** §8 already gives the **shared item** page *a
way to take it — the archive, or a copy into their own library*. **A single-item archive is in the
specification already**; what this answers is that the owner can produce one too, from their own
Library, without a link and without a project.

### Q16 — the empty project — raised and answered 2026-09-20

**Raised by reading the main flow aloud**: it draws a branch where somebody presses `Check` on a
project with nothing in it, gets a column of `Skipped` and exports an archive containing nothing.
**Two questions fell out of it, and the second is the one worth keeping.**

**First: how does a project come to be empty at all?** Three ways, and they are not of equal quality.
**Creating and filling are two acts**, so every project is empty for its first moment — this is the
normal initial state and not an edge. **A manually added row can always be removed**, so the last one
can be. And **§11's example project is deletable and re-usable**, so *empty it out and build my own in
it* is a plausible path. **Q17 adds a fourth** and it is the one nothing answers.

**The answer. An empty project is an empty state, and the control that enters `Run` is inert.** The
body carries **one** action, whose label is step 5's to settle — the owner's candidates were *edit* and
*configure*, and whatever it is called it has to lead to putting the first item in.

**It is one control and not two.** *The first wording of this answer said "`Check` and `Export` are
disabled", and the review of 2026-09-20 pointed out that it named a control the Project screen does not
have*: §8 puts `Export` inside `Run` as its final stage, never a button beside the check, so an
unreachable Run takes Export with it and there is nothing else to grey.

**And one thing the owner deferred in the same breath.** *The main action should be Export, and checks
and runs are sub-processes* — called a naming question and **sent to lesson 05, tone of voice and
microcopy**, with the control named `Run` until then. **It is recorded here because it may not stay a
naming question**: if `Export` ever becomes a control on the Project screen, §8 has to be reopened,
since §8 puts it inside Run deliberately.

**This is the product's one place where a primary action is shown and cannot act, and it is written
down as an exception rather than smuggled.** §9's rule is *an action that cannot act is not shown*, and
§6 refuses a greyed `Export` in the strongest terms. **Both stay as written**, because §6's rule is
about **findings** — *a missing env key still zips, a duplicate command still zips, it is simply wrong
inside* — and an empty project has no findings, it has no content. **There is nothing to be wrong.**

**The basis is §6's own analysis of the case it refused.** §6 records why Figma's greyed `Export`
beside `0 of 0 selected` gets away with it: **the blocker is one named action away**, **it is a
property of this second's selection rather than of the document**, and **re-doing it costs nothing.**
Those three were given as the reasons our Problems are *not* that case. **All three hold for an empty
project** — the action is *add an item*, emptiness is this second's state, and checking again is free.
**The same three conditions that excused Figma excuse this, and they are the test any future exception
has to pass.**

**And the second question, which is not answered and stays live.** §6 keeps the verdict on the project
as **counts** — `checkVerdict`, *problems · notes · skipped*. **An empty set and a perfectly assembled
one both read `0 problems · 0 notes`.** On `Projects`, a row for an empty project would say *checked*
and look like a clean one. **That is the unearned green tick §6 spends a section refusing, arriving
through the counters rather than through a glyph.** Disabling `Check` on an empty project removes the
only way to *reach* that state today — but the shape is still there, and it is the same family as **the
count that can never reach zero** (`defersTo` raising a Note that never clears). **Left open: whether
counts are a wide enough channel to carry a verdict.** It belongs to step 5 and to whoever writes what
a project row says.

**And the state is reachable by a second route, which the first wording of this entry missed** (found
by the review). Check a full set, then remove every row: §6 voids the verdict, so the counts go — **but
`checkedAt` survives on a project that is now empty.** So *disabling the control removes the only way to
reach it* was too strong. **Disabling removes the way in; it does not remove the shape.**

### Q17 — deleting an item from the library — raised and answered 2026-09-20

**Raised because §5 has no delete.** The data model describes a live link from a project row to a
library item and **says nothing about the item going away.** So a project could be emptied, or broken,
without anybody opening it — and a `requires` edge could be left pointing at nothing, which §6 reports
as an **unresolvable requirement**, a Problem produced by a set nobody touched.

**Answered: it is confirmed, never refused.** The product states the consequence in the present tense —
***used in 3 projects. Deleting it may stop them working.*** — and offers **Delete** and **Cancel**.
This is the register §6 already uses for an unclean export and §11 for material coming in: **name the
cost before the irreversible step, then let the person act.** *Nothing blocks* is untouched.

**What the confirmation must carry**: **how many projects hold it**, because that is the fact the
Library row already computes (E14), and **that a `requires` edge from another item may be left
dangling**, because that is the half a project count does not cover.

**One thing is recorded open rather than invented.** A **detached** row holds its own content in
`overrides` (§5). When the library original is deleted, **does that row survive as a local copy, or go
with it?** Both are arguable — the override is the project's own work, and a row whose original is gone
is a thing the model has no word for. **Nothing in §5 answers it, and this entry does not either.** It
goes to step 5, and it is the second question in two days to come out of `detached` being a state that
the rest of the model does not fully see — the first being *used in 3 projects* counting copies that a
fix will not reach.

### Stage 5's basis shifted — recorded 2026-09-20

**Not a question and not an answer. A note, so that a signed-off document is not read as saying
something it no longer says.**

[`5-patterns/patterns.md`](5-patterns/patterns.md) scored **P1, two-pane drag**, at **C5 = 2** on the
stated ground that *"half the screen is inert during the check and during export"*. **That assumed P1's
own answer to validation** — a live strip in the right-hand pane, with the designed pass having
nowhere to expand. **The hybrid that was chosen does not do that**: `Run` is entered by `Check` and
takes the whole surface, so **the Project screen, and anything on it, is not present during a check.**

**The score is left exactly as it is**, because it is the record of what was weighed on 2026-09-02 and
it was correct about P1-as-drawn. **What is added is a pointer**, at *The choice*, saying that one of
the five categories no longer bears on a pane in today's architecture, and naming Q14 as where that was
used. **Nothing else in stage 5 is rewritten** — not the variants, not the scores, not the comparison.

### The traceability matrix — 2026-09-20, and it closed one entry and raised three

**Lesson 03 ran a coverage check after the owner accepted the flows**: every job in
[`7-jobs-to-be-done/jtbd.md`](7-jobs-to-be-done/jtbd.md) against every surface in
[`sitemap.md`](../03-information-architecture/sitemap.md), sourced jobs and hypotheses in separate
blocks. **One orphan column, two orphan rows, and two further defects nobody asked it to look for** —
*and a second orphan column later the same day, when Q25 added the sign-in and the matrix was re-run
over it, as that entry required of itself.*
The matrix is in `sitemap.md` §Traceability; the dispositions are here. **All four were put to the
owner as options and answered the same day.**

#### Q12 is closed as *refused*, not deferred a second time

**`H-J5` — *watch what actually ran* — is importance 3 for the primary persona and has twelve blank
cells.** It is the **second main-job candidate that survived** stage 7's method, which by that method's
own rule means **two products**. §6 runs nothing on anybody's machine, so no surface here can touch it,
and the sitemap had already refused the screen — *the job is real and the screen is forbidden*.

**Why it is closed rather than deferred again.** The answer **cannot change** without a runtime the MVP
will never have. **An open question at importance 3 gets asked again on every surface in lessons 04 to
09** — *should this show what ran?* — and that is a tax with no possible payoff. **It moves into
`CLAUDE.md` §9** with the other refusals, and it is the first entry on that list that is refused
**because the product is incapable of it** rather than because the MVP is narrow.

**What must not grow into it.** *Last exported 12 days ago* (§5) reports **what this product did**,
never what an agent did with the archive afterwards. That boundary is the whole of what is shippable
here, and it is already shipped.

#### Q18 — the JSON route keeps its place, on the architecture rather than on a job

**Answered: keep it, and stop calling it an orphan — the measurement was pointed at the wrong thing.**

**The finding stands as measured.** `Library import / export as JSON` is empty in both blocks of the
matrix, and **three separate instruments** now say so independently: the entity inventory on
2026-09-15, step 2b reducing it from a screen to two commands, and this matrix.

**What changed is the standing of that measurement, not the measurement.** Coverage was measured
**against jobs**. This mechanism does not stand on one. **§10 puts storage in IndexedDB with no
backend**, so the only copy of everything a person has accumulated lives in **one browser profile,
which clears.** That is a property of the architecture, and **no instrument pointed at people was ever
going to find it** — nobody says *I would like a way to survive my browser clearing site data* until
the afternoon it happens.

**Half of its old justification did go, and is not missed.** §10 justified it as *backup and informal
sharing before any server exists*; **informal sharing is what a share link does now** (Q13). What
remains is **durability**, and that is enough on its own.

**It is not promoted by being justified.** It stays in the **deep** tier and gets no more design than
two commands need. **The mark changes from `[orphan]` to `[§10]`** and the empty column stays empty.

#### Q19 — the shelf is built in full and designed only as far as the example needs

**Answered: build the ~30 items; design the browsing surface no further than the example project
requires; touch nothing downstream of Q9.**

**The number that decided it.** `Public library` has **two ticks in the matrix, and only one comes from
a job anybody has evidenced** — RJ-3 reaches it through the single branch *copy it into mine to make it
fixable*. Everything else is **H-J4, whose importance is `[?]` in all three persona columns**.

**Against that, lesson 03 made it more load-bearing three times in five days** — the scope switch in
§8, the panel carrying it into assembly, cold start answered inside the builder — **and it gained no
evidence at all while that happened.** **A surface that keeps getting heavier without getting better
founded is where design effort goes to be wasted.**

**So the split is between content and surface.** The **content is built in full**, because §11 is right
that an information architecture argued against an empty library is argued against nothing, and because
the example project needs real `requires` edges, a real conflict and a real target-path collision.
**The surface waits**: sorting, ranking, recommending and curating are all downstream of **Q9**, which
is unanswered, and **its only evidence is *provenance over volume*.**

#### Q20 — the shared surfaces get the product's most conservative treatment

**Answered: on `Shared project` and `Shared item`, invent nothing that is not derived from what P1
needs.**

**The exposure, as a number.** `Shared project` carries **seven jobs** in the matrix — **more than
`Projects` and more than the library panel** — and `Shared item` nearly as many. Together the
receiver's two surfaces do about a third of the product's job-closing work.

**And the evidence under them is the thinnest in the folder. P2 has never spoken in the first person.**
After four rounds and five venues, **every account of a handover in this repository was written by the
sender.** Round 3 went looking for the receiving side deliberately, by reading forks as handovers, and
what it found was machines performing setups — not a person describing one.

**The rule, therefore.** Where a choice on those surfaces has no answer in P1's evidence, **make the
one that shows more and promises less, and mark it.** This is lesson 03's own **trap 3 — inventing
places for people nobody has met** — and the matrix says this is the column where it would be easiest
to spring. Written into `CLAUDE.md` §8.

#### Two defects recorded without a disposition, because the owner has not ruled on them

**`EJ-3`'s ticks are partial by construction** — usage facts answer *is it used*, not *did it change
anything* — and **the detached row's `Edit`, `Reset` and `Promote` have not been assigned to a mode**,
although the rule written for the `✕` on 2026-09-20 implies they belong in configuring. **Both are put
to the owner and neither is decided here.** A third, `SJ-2`, is empty in the matrix and already
post-MVP by stage 7's own heading; the only thing the matrix adds is that **`SJ-2` and `H-J6` are one
job in two wordings**, so a proposal for a profile or a listing will arrive in the functional one.

### The matrix's last three — 2026-09-20, and none of them adds anything to the product

**The traceability matrix put seven things to the owner. Four were answered the same afternoon and are
above; these are the remaining three, answered after being explained a second time.** What they have in
common is worth stating: **not one of them builds anything.** Two write down a limit and one closes a
rule that was left half-written. **A matrix whose findings all ended in new features would have been a
wishlist, not a check.**

#### Q21 — the detached row's three commands live in the configuring mode

**Answered: all three, in configuring, and a detached row is not an exception.**

**What was open.** `Edit`, `Reset` and `Promote` (§7, state 6) change the content of the set, and
nothing had said which of `Project`'s two modes they belong to. The rule written for the `✕` on the
same day — ***a row being read is not a row being changed*** — implies configuring, and an implication
is not a decision.

**What was rejected, and why it mattered.** The alternative was to treat the detached row as **the one
exception**: you notice the difference while reading, so you fix it while reading. **A viewing mode
that can change the set is not a viewing mode**, and the separation the owner introduced hours earlier
would have leaked on its first day.

**What it costs, named rather than absorbed.** Somebody who spots a divergence while reading has to
enter configuring before acting on it. **One entry, and the rule stays whole.**

#### Q22 — `EJ-3`'s ceiling is written beside the usage facts, and nothing is added to close it

**Answered: accept the partial coverage and state it where it will be read.**

**The gap.** *Stop suspecting that half of what I keep is dead weight* is **importance 3** — one of the
highest in the base, and the only sighting of it is a person saying *"mostly useless… 50/50"*. What the
product shows against it is **usage facts**: *used in 3 projects*, *2 items require this*, *last
exported 12 days ago*. **Those answer *is it used*. The job asks *is it any good*.** An item can sit in
three projects and be useless in all three; the counter still reads three. **We cannot tell the
difference, because we run nothing** — which is the same wall as Q12, one importance-3 job away.

**Where the sentence goes, and why the location is the decision.** Into **`CLAUDE.md` §5, immediately
beside the facts** — not into a research file that nobody drawing a row will open. The people this
protects are in lessons 05, 07 and 09, reading *used in 3 projects* and deciding what it means.

**And nothing is added to narrow the gap.** The obvious extension — count the exports, or flag whether
an item was ever in a checked set — is **still *used*, and would read as *useful***. That is the
decoration §5 refuses two paragraphs later when it refuses scores and badges, and it would be worse
here because it would look earned.

#### Q23 — `SJ-2` stays in the backlog, and the caution moves next to the refusal it protects

**Answered: backlog, and write into §9 that the request will arrive in the other wording.**

**Nothing here is a new decision.** `SJ-2` — *have something I would put my name to* — is **importance
1, the lowest in the base**, and it was established **by absence, looked for deliberately in two
instruments**: **0 of 1,762** Hacker News comments, and `portfolio in:title` returning two unrelated
issues. `jtbd.md` marks it **post-MVP** in its own heading and §9 refuses the catalog. Its row in the
matrix is empty because **the product declines the job in writing, twice.**

**What the matrix added is one recognition, and it is the whole entry.** Stage 7 carries the same job
**twice** — as `SJ-2` and as **`H-J6` — *my work counts as something I can show*** — and says not to
count it twice. **The first is easy to refuse and the second is not.** *Portfolio* sounds like vanity;
*visibility of work* sounds like a need. **So a future proposal for a profile, a listing or a place
where work is seen is this refusal being tested in functional clothing**, and the caution now sits in
**§9, beside the refusal**, rather than in a matrix nobody will re-read.

### Q24 — the product is online: a backend and accounts — 2026-09-20

**Raised by the owner in four words, correcting a sentence of mine.** Lesson 03's plan said, in passing,
*the product is local, with no network in the MVP*, and the answer was: **it is not local, it will be
online.** Put as a question with three readings — hosting only, a backend without accounts, or a backend
with accounts — **the owner chose the third.**

**The answer. Data lives on a server, there is a sign-in, and a person's library is reachable from any
machine.** `CLAUDE.md` §9's *accounts, sync, teams* bullet loses two of its three, and §10's *storage:
IndexedDB, no backend* is gone.

**This is a decision, not a finding, and the mark discipline applies as always.** No evidence was
produced and none is promoted. **What it is is an implementation fact with product consequences** —
which is exactly the class of thing this repository has twice been bitten by, so the consequences are
enumerated rather than left to be discovered.

#### What falls

- **§9 — accounts and sync move into the MVP.** **Teams do not**, and the distinction is kept on
  purpose: a server needs identity, and identity is not a team. §4 still says a workspace is **one per
  user and not a team concept**, and no job in the matrix raises a second person inside one workspace.
- **§10 — storage.** *IndexedDB, once we get to logic. No backend* is replaced. **Which backend is
  deliberately not decided here**, in the same words §5 already uses about serving shared links: the
  product decides what it is, the implementation follows. **IndexedDB may survive as a local cache** and
  that is an implementation question, not a product one.
- **§10 — the archive.** *Built in the browser (JSZip)* becomes **a choice rather than a constraint.**
  Nothing in §6 depends on where the zip is assembled, and no decision is taken here.
- **§2 — a piece of the long-term ambition moves into the MVP.** *Store your work independently of any
  one machine* was written as the ambition; **a backend is what that sentence asked for**, and it
  arrives before the catalog and before teams, which stay in the ambition.
- **§11 — the shelf's justification, not the shelf.** *A read-only shelf that ships with the application
  needs no server, no accounts and no moderation* was half an argument from absence. **The absence is
  gone.** The shelf is still read-only and publishing to it is still out, **but those now have to stand
  on curation and on evidence** — which they can, and §9's refusal of the catalog already does.
- **§11 — the keys warning gets sharper and must say so.** It was justified by *what comes in goes out in
  every archive built from it*. **Now the material also leaves the person's machine the moment it is
  accepted**, onto a server we run. **That is a second reason, not a replacement**, and it strengthens
  the case for the reminder rather than weakening it.

#### What stands, and why each survives

- **§6 — *we run nothing on anybody's machine*.** A backend of ours is not the user's agent runtime.
  **Q12 stays closed**: *watch what actually ran* is still a job about a machine we never touch.
- **§6 — *the run is a moment; nothing is stored*.** A server makes storing runs trivial, so it is worth
  saying why this is unaffected: **its reason was never that we had nowhere to put them.** It was §9's
  refusal of a second mechanism for *what was true earlier*. **The argument was a product argument and
  it survives the thing that would have made it easy to break.**
- **§5, Q13 — the shared link.** *No accounts, no named viewers, no sign-in* was about **the viewer**,
  and the viewer is still anonymous. **The owner having an account does not give the receiver one**, and
  nothing about a link changes: it is still the credential, still unguessable, still revocable, still
  live. **How it is served stops being undecided and becomes ordinary.**
- **§9 — the catalog refusal.** It already stopped leaning on *there is no server to publish to* on
  2026-09-15. **Now the implementation excuse is gone entirely and the evidence carries it alone** —
  which is where it should have been, and where it already is.
- **§3, §7, §8** — untouched. Desktop-first, the six item states, and every surface in the flow are
  indifferent to where the bytes live.

#### What it reopens

- **Q18, answered earlier the same day, is void and must be re-answered.** The JSON export kept its
  place on **one sentence**: *storage is IndexedDB with no backend, so the only copy of everything a
  person has accumulated lives in one browser profile, which clears.* **That sentence is now false.**
  The finding underneath it is unchanged — **no job raises it** — so the mechanism is back to standing
  on nothing unless a different warrant is found. **Two candidates and neither is taken here**:
  *portability*, meaning the user can leave with their data and is not locked in, which is a real
  argument nobody in the evidence base has made; and *nothing*, in which case it is cut. **Put to the
  owner.**
- **`loading` and `error` become real states everywhere**, not only on a shared page. Lesson 03's step 6
  — the IA critique — already names missing states as a defect class, and **the excuse written into the
  plan that morning, *the product is local, with no network in the MVP*, is struck.**

#### One more thing to watch, recorded now so it is not discovered later

**Every argument in this repository of the form *we cannot, because there is no server* is now
suspect.** Three were checked above and all three survive on other grounds — the run being a moment, the
catalog, and *checked, never works*. **The rule going forward: if a refusal's reason is an absence, and
the absence ends, the refusal has to be re-argued or dropped.** That is what happened to stage 5's
C5 = 2 on 2026-09-20, and it is the second time in one day.

### Q18 re-answered — portability, and the mechanism outlived three justifications — 2026-09-20

**Void for one evening, kept by the owner the same night.** Q24 destroyed the warrant this entry was
given that morning; the question went back with two candidates and **the first was taken: it ships, on
portability — the user can leave with their work.**

**The basis is declared non-evidential, and that is the whole of the honesty here.** **No job raises
it**, in a matrix that checked all seventeen, and the empty column stays empty on the page. What
changed is not the measurement but what the product became: **it now holds somebody's accumulated
corpus on a server**, and §11 spends a section telling them to put it all there. **A hosted product
that says *bring it all* and offers no way out is the lock-in the word was invented for.** It is the
same class of decision as the **`license` field** (§5) — closes no evidenced job, taken on other
grounds, labelled as such rather than dressed as a finding.

**Worth keeping as a specimen.** This mechanism has now been: an **orphan** by job coverage · justified
by **storage** · **void** when the storage changed · kept on a **stated preference**. **Four
standings in six days, and the measurement under it never moved once.** That is the difference between
measuring and deciding, and both halves belong on the page.

### Q25 — the product is online, and nobody has drawn the way in — raised 2026-09-20, unanswered

**Raised by lesson 03's IA critique, hours after Q24.** Accounts and sync entered the MVP; **sign-in,
session and account did not enter the screen tree, the entity inventory or the traceability matrix.**

**They are orphans by the test that condemned the JSON export, and they arrived after the test was
run.** No job in the matrix raises a sign-in — no job could, since the matrix was drawn against a
product that had no accounts four hours earlier. **The finding is not that they are unjustified; it is
that nothing has been asked about them at all.**

**What it already breaks.** §Navigation counts **three taps to the archive** from the first screen, and
**every path in that table begins at a screen.** With a session that can expire there is something
before the first screen, so **the depth from a genuinely cold start is unknown**, and the table now says
so rather than implying coverage it does not have.

**What would answer it.** The minimum the decision forces, named rather than assumed: **a way in**, and
**what happens when a session ends mid-work** — the second being the more interesting, because §6's
configuring mode and `Run` are both unaddressable, so an expiry mid-assembly is a state nothing in this
architecture has a word for. **And then the matrix is re-run over whatever is added**, or the coverage
claim in §Traceability quietly stops being true.

**Not answered here, and deliberately not designed here.** *Do not add screens to the tree by reflex* is
the whole of lesson 03's method, and a sign-in invented on the evening of the decision that created it
would be exactly the reflex.

### Q25 answered — the minimum a sign-in forces, and it costs a place — 2026-09-20

**Answered: build the minimum the decision forces and nothing beyond it.** A **way in**, and a **rule
for a session that ends mid-work.** **No account screen, no settings, no session list** — *no job in
the matrix raises any of them*, and §9's rule plus this lesson's trap 3 both say the same thing: **do
not invent a place for a person nobody has met.**

**What happens when a session ends mid-work, derived rather than invented.** §Navigation already
settles the shape of this for the nearest case: *a reload during a check returns to the Project and does
not silently start a new one, because a reload that re-runs is the product making a choice nobody made*
— **EJ-1, importance 3.** So: **after signing back in you return to where you were, nothing is re-run,
and nothing that had been saved is lost.** And because **configuring and `Run` are modes, not places**,
you return to **the Project** — not into the act. *You were halfway through assembling a set* is not a
thing this architecture can restore, and pretending otherwise would be the same unearned claim §6 spends
a section refusing.

**One persona never meets it, and that is worth stating because it is easy to lose.** **The receiver
does not sign in.** Q13 keeps the viewer of a shared link **anonymous**, Q24 gave the *owner* an
account, and the two do not touch. **The archive branch of the receiver's flow stays free of any door**
— which is what makes it the branch that must always work. **The only way P2 meets this screen is by
choosing *copy into my library***, and at that moment they have stopped being P2: they are somebody with
a corpus of their own. *That is the cleanest statement yet of where the receiver ends and an owner
begins, and it fell out of a sign-in rather than out of anything about receivers.*

**And it costs a place, which is the part worth recording rather than hiding.** **Sign-in passes all
three of this section's tests**: a reload lands you on it, Back means something, and the address can be
written down and come back tomorrow. **By the section's own mechanical test it is a place, so there are
six**, not five — for the first time since `Item` left the list on 2026-09-16.

**It is also the only one of the six that exists for the product rather than for the person's work.**
The other five are things somebody goes to in order to get something done; **this one is a gate you are
sent to and handed on from.** *The temptation was to invent a fourth kind — place, mode, overlay, gate —
and it was refused: a classification that grows a category every time something does not fit is not a
classification.* **The tests decided it and the count moved.**

**What it does to the depth count.** §Navigation measures from the first screen, and **there is now
something before the first screen.** Every path costs **one more from a cold, signed-out start** — and
the table says so rather than implying a coverage it does not have. **The floor of three is a floor for
somebody already signed in**, which is the ordinary case and the honest thing to state.

**The matrix was re-run, the same day.** `In` is a column in both blocks of §Traceability and **it is
empty in both**, which was never in doubt. **What the re-run is for is the distinction it forced**: an
empty column can mean *we chose a mechanism nobody asked for* — the JSON route — or *another decision
forced a place on us*, which is this. **The first is a candidate for removal and the second is not**,
they look identical in the table, and **they are now labelled apart.** *And the empty column turns out
to be the sharpest available argument against a profile screen and a settings page: each would be
another one, with a real design cost behind it.*

**What is not answered and is deliberately left open.** **What the way in actually is** — a password, a
link, a provider — is not a product question this lesson can settle, and §10 already says *how it is
served is deliberately not decided here.* **The matrix must be re-run over whatever is added**, or
§Traceability's coverage claim quietly stops being true.

### Q26 — the product never shows a verdict state it is not sure of — raised and answered 2026-09-20

**Raised by writing the waits and failures under the flows.** §5 requires the blast radius to be legible
**before** the edit — *used in 3 projects · saving un-checks all three* — and then the product is online
(Q24), so **the save can fail after that sentence has been read.** **Did it un-check them or not?**
Nothing on that screen can say, and the answer decides what three other projects currently claim about
themselves.

**Answered: when the result of the save is unknown, the screen says the edit did not land, and the
three projects are shown neither as checked nor as un-checked on the strength of it.**

*Restated the same evening.* **The first wording was *the edit and the voiding are one operation*, which
is a sentence about storage, and the owner set the working rule that we are designing the interface and
not the backend.** **What is decided has not changed**; what changed is that it is now expressed as
what a surface may claim, which is the only form this specification is entitled to use. *If a line here
can only be satisfied by one storage design, it is written wrongly.*

**The rule it follows is already in §6 and this is the same discipline one step earlier.** *A stale
verdict is not shown, and the date still is* — **never display a claim that may no longer be true.** A
half-applied edit produces exactly that claim in three other places at once.

**Why it is a product decision and not an implementation one.** *How many of my projects are currently
checked* is a fact the product states on the `Projects` screen. **A fact the product asserts is the
product's to get right**, and this file's own rule is that the product decides what it is and the
implementation follows.

### Q27 — a person is never left in front of a library they cannot account for — 2026-09-20

**Raised the same way.** §10 commits to importing the whole library as JSON and **never says whether
that is a transaction.** Online, it can fail halfway.

**Answered: either the import finished, or the library reads as it did before it started.**

*Restated the same evening, for the same reason as Q26.* **The first wording was *all or nothing*, which
describes a transaction.** The decision is unchanged and is now about **what the person is looking at**;
how it is arranged underneath is not this file's business.

**The reason is §11 and it is about the one subject where being wrong cannot be walked back.** Material
entering the library is met with *check that these files carry no keys* — **a reminder addressed to a
set of files the person is expected to know.** After a half-finished import **they cannot enumerate what
arrived**, so the warning has been given about something nobody can inspect. **A warning about an
unknown set is not a warning.**

**The alternative was available and is recorded as refused**: allow the partial import and report
exactly what landed. **Honest, and it needs a report surface nobody has designed** — which is the reflex
this lesson exists to refuse.

### Q28 — a disclosure that failed must say it failed — raised and answered 2026-09-20

**Raised by the same pass, and it generalises further than the case that found it.** `SETUP.md`'s
preview is **generated, not stored.** If generation fails, the person does not see an error — **they see
a page with less on it**, and they have no way to know that what they are reading is short because
something broke.

**Answered: the disclosure states what it could not produce.** In §6's own register, naming the gap in
the present tense.

**This is not microcopy, and calling it microcopy is how it would have been lost.** RJ-1's whole job is
*know what the other side will still need, before I send it*, and **the preview is that knowledge.** A
preview that quietly renders short is the job silently not happening — **an unearned tick delivered by
omission**, which is the thing §6 spends a section refusing in its explicit form and had never
considered in this one.

**It generalises, and the general form is the entry.** **Any surface whose purpose is to disclose must
say when it could not.** That covers the `SETUP.md` preview, `.env.example`, the file tree of the future
archive, and the share disclosure — **all four are generated, and all four are read immediately before
an irreversible step.**

### Two decisions taken the same day that raised nothing — 2026-09-20

**The main job is not split.** At **3,528 pixels** it is the tallest diagram in `flows.md` by some
margin, and the question has been open since 2026-09-16. **Left whole, on this file's own restated
rule**: the test is *render it and look*, **height does not hurt legibility and width does** — and its
width passes at 0.747. §8 names exactly one seam in this product, **Check**, and cutting there was the
only non-invented split available; **the owner declined it.** *Recorded so the question is closed rather
than perpetually open.*

**The wait on the dependency walk goes to lesson 04** with the rest of waiting. §2 calls the validation
pass *a designed moment, not a spinner*, **which leaves open what ordinary waiting looks like**, and
deciding that one interaction at a time is trap 2. **One thing is fixed in advance so it cannot be taken
by default: the optimistic option — rows appear instantly and reconcile later — must not be chosen
silently.** Rows that appear and then vanish are **EJ-1, *not be quietly overruled by my own tools*,
importance 3.**

### Earlier decisions

Four were taken on 2026-09-01, before this register existed, and are recorded under *Decisions
already taken* above with their reasoning in [`1-landscape/comparison.md`](1-landscape/comparison.md).
