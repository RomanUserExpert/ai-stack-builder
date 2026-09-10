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
| [`6-personas/re-research.md`](6-personas/re-research.md) | **Stage 6, step 5.** A source document. Four instruments taken to the public record — the `anthropics/claude-code`, `openai/codex` and `gemini-cli` trackers, 1,762 Hacker News comments read in full, Stack Overflow, GitHub repository search. Eleven of the twenty unknowns moved. Contains a correction to stage 3 and a challenge to CLAUDE.md §2, neither applied. |
| [`6-personas/personas.md`](6-personas/personas.md) | **Stage 6, step 3, written 2026-09-08.** Three personas on the axes in `inventory.md` §D — **P1 the keeper who runs several agents (primary)**, P2 the receiver, P3 the empty-handed. Five blocks each (context, jobs, pains, trust triggers, quote) plus environment; every block sourced or `[?]`; **eleven hypotheses** in their own table, each with the instrument that would close it. **Provisional** until five interviews. |
| [`personas-and-jobs-critique.md`](personas-and-jobs-critique.md) | **The audit, written 2026-09-08 and applied 2026-09-09** — merged with stage 7's step 6 at the owner's request. 238 claims classified across both files, 27 found invented. Confirmed / hypothesis / invented, the dangerous list, and the proposals. **D-1 was closed on 2026-09-10.** |
| [`6-personas/agent-setup-interview.md`](6-personas/agent-setup-interview.md) | **Interview 1 of 5.** The first practitioner run against the guide. Everything in it is **`*`**. Does not lift the provisional label — that needs five. |
| [`6-personas/interview-guide.md`](6-personas/interview-guide.md) | **The instrument for lifting *provisional*.** A 30-minute guide covering the fifteen rows that need a person, built around the one question no search can answer — whether the loud pain and the quiet pain belong to the same people. Recruiting screen, six rules, six blocks, the words never to say, and a coverage table. Ready before the conversations are scheduled. |
| [`7-jobs-to-be-done/README.md`](7-jobs-to-be-done/README.md) | **Stage 7 — the plan.** The canonical job form, the hierarchy, the feature-name test, the matrix, and what each of its two answers is worth. |
| [`7-jobs-to-be-done/jtbd.md`](7-jobs-to-be-done/jtbd.md) | **Stage 7, written 2026-09-08, audited and reconciled 2026-09-09.** Main-job candidates and the choice, the hierarchy, the matrix with feature and competitor columns, the two conclusions, and §12's nine proposals. **§7 now carries what rounds 3 and 4 did to the matrix.** Provisional. |
| [`6-personas/re-research-2.md`](6-personas/re-research-2.md) · [`-3.md`](6-personas/re-research-3.md) · [`-4.md`](6-personas/re-research-4.md) | **Three more collection rounds.** Round 2 (2026-09-08) counts somebody's collection instead of asking about it. **Round 3 (2026-09-10) stops reading the record and runs experiments** — the handover test and the competitors, installed. **Round 4 (2026-09-10) goes after the matrix's persona columns** in two vendor forums nobody here had used, and turns round 3's fork corpus on a question nobody had asked it. |

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
| 10 | Dark design language | → | [Material for the next phase](2-flows/10-dark-design-language/NOTES-linear.md) |
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

Next after that: **lesson 03, information architecture** — not started. *Corrected 2026-09-09: this
said "design system", which is lesson 09. Five lessons stand between the two, and CLAUDE.md §1 now
carries the twelve.*

---

## Open questions — the register

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
| **Q5** | Loss or reassembly cost — which drives adoption? | **Deferred — accepted risk, with the trigger written down.** Nothing in this repository can answer it; trackers are blind to both candidates by construction. Ask five practitioners **before the first feature that only pays off under one answer** — a *reassemble from a previous project* flow versus serious investment in library-wide search. The MVP is the same product under either answer. **Instrument named 2026-09-06: [`6-personas/interview-guide.md`](6-personas/interview-guide.md). The same event also lifts the provisional label on stages 6 and 7.** | Positioning, and the provisional label on stages 6–7. Nothing in the build |
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
([`6-personas/agent-setup-interview.md`](6-personas/agent-setup-interview.md)) and recorded in
[`6-personas/inventory.md`](6-personas/inventory.md) as NK-21 to NK-23. All three stand on **one
person** — mark `*` — which is why they are entries here and not findings anywhere.

| ID | Question | Raised by | What would answer it | Blocks |
|---|---|---|---|---|
| **Q7** | Who is the primary persona — the practitioner whose pain is *sighted* (an archive that lands and does not run; a key that silently wins) or the collector §3 describes (large corpus, wants to find and reuse)? | Stage 6, step 3 | The five practitioner conversations Q5 names, run against [`6-personas/interview-guide.md`](6-personas/interview-guide.md); plus a GitHub search for repositories carrying `.claude/`, `CLAUDE.md`, `.cursor/rules`, `AGENTS.md`, which observes where material lives and how many targets one person keeps | Which persona wins design conflicts — empty states, what a card carries, the register of validation copy |
| **Q8** | Is the main job *assemble a set that holds together* (§2, owner's assertion) or *hand a set to a machine and have it run first time* (stage 3, observed)? If both survive, the lesson's rule says two products. | Stage 7, step 1 | The same conversations, asked as situations (*what did you last do with a skill you already had; what happened the last time you moved a setup to another machine*), never as pitches; the matrix's main-job row with sourced cells | Positioning; the relative weight of the Project screen and Run in mockups |
| **Q9** | Which specified features close no evidenced job — candidates: the public library switch and example project, duplicate project, promote, the target selector, library-wide search? | Stage 7, step 5 | The matrix's *feature* column, then Q7/Q8's conversations for the `[?]` rows. Absence in the trackers is not evidence of no job, so this closes only with people asked | Mockup scope. Not the design system |
| **Q10** | When the user's own rule and an **external** requirement conflict — a client's linter, a repo convention — which wins, and where does the product put that? | Stage 6, the first interview (NK-21) | The remaining four conversations, asked as a situation (*what happened the last time your own rule and the project's tooling disagreed*). §6 models conflicts **between our items** and the data model has nowhere to put this one | The `Item` model, and what the validation pass is allowed to claim |
| **Q11** | If roughly half of what makes a setup work was **never written down**, what is the ceiling on validating the written part? | Stage 6, the first interview (NK-22) | The same four conversations, plus the NK-13 test: hand a coherent archive to a fresh agent and see what still does not transfer | The promise the product makes at handover. Not the build |
| **Q12** | Is the wanted thing **observability of what ran** rather than **validation that a set coheres**? If both survive, the lesson's rule says two products — the same shape as Q8. | Stage 6, the first interview (NK-23) | Guide Q25 (*what would a genie fix*) four more times, asked before any description of the product. **We cannot build the first** — §6 runs nothing on anyone's machine — so a strong answer here is a positioning finding, not a feature request | `CLAUDE.md` §2's core-value sentence, and positioning |

**Q5 is re-pointed, not re-opened.** Its disposition stands — deferred, accepted risk — but its
instrument was unnamed beyond *five practitioners*. Stage 6 makes
[`6-personas/interview-guide.md`](6-personas/interview-guide.md) that instrument and stage 7 gives it
the questions. Its *blocks* line widens accordingly: **positioning, and the provisional label on
stages 6 and 7**, because the label lifts on the same event.

### What the closing of stages 6 and 7 did to this register — 2026-09-09

**No question was answered, none was added, and one gained its first evidence.** The protocol holds:
the six live entries leave in one sitting, and that sitting has not happened. What changed is what
the sitting will read.

- **Q9 — *which specified features close no evidenced job* — now has evidence, and it is the first
  ever collected about the persona underneath it.** [`6-personas/re-research-2.md`](6-personas/re-research-2.md)
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

**What replaces it, in part.** [`6-personas/re-research-3.md`](6-personas/re-research-3.md) — five
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
[`6-personas/re-research-3.md`](6-personas/re-research-3.md) were run in full, and for the first time
this repository has marks that cover a **behaviour** rather than an utterance — two experiments we ran
ourselves, three instruments reading what people did to repositories rather than what they said.
Capture: [`6-personas/_re-research-3-log.json`](6-personas/_re-research-3-log.json) and
[`6-personas/_qf-handover-test/`](6-personas/_qf-handover-test/).

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
[`6-personas/re-research-3.md`](6-personas/re-research-3.md). One of them is a **change to the data
model** — an item addresses a directory, not a file — which is the first thing any round has proposed
to §5's shape rather than to its reasoning. **They join the two lists already waiting** (stage 6's
nine, stage 7's nine) as input to the same sitting.

**And the label does not lift.** Its trigger is five practitioner conversations. Four hypotheses
closing does not change what the trigger is, and this round says so itself rather than arguing
otherwise.

### Round 4 — 2026-09-10, and this one moved the matrix

**[`6-personas/re-research-4.md`](6-personas/re-research-4.md)**, capture log
[`_re-research-4-log.json`](6-personas/_re-research-4-log.json). Round 3 answered five questions and
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

**The day's arithmetic: 36 `[?]` cells this morning, 31 tonight; P1 from seven unknowns to four; P3 unchanged at ten.**

**Nothing is applied to `CLAUDE.md`, and the label does not lift.**

**The question this raises and does not answer: what, if anything, may ever lift *provisional*?**
That is the owner's call at the sitting, not a research finding. Three positions are available and
each has a cost — keep the label until conversations become possible; replace the trigger with a
named non-interview event and say what it is; or drop the label and carry the marks alone, which is
what the three-mark system was built to make survivable. **It is recorded here so the sitting takes
it deliberately.**

### Earlier decisions

Four were taken on 2026-09-01, before this register existed, and are recorded under *Decisions
already taken* above with their reasoning in [`1-landscape/comparison.md`](1-landscape/comparison.md).
