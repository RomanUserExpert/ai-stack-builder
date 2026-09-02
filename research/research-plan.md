# Research plan

Updated 2026-09-02. The phase runs in five stages. **All five are done, and the register at the end
of this file was worked through in one sitting on 2026-09-02.** The research phase is signed off.
Next phase: design system, per CLAUDE.md §1.

| # | Stage | What it produces | Status |
|---|---|---|---|
| 1 | **Landscape** | Who else is in this space, what they sell, and to whom | ● done |
| 2 | **Flows** | Twelve mechanisms captured from live products | ● done |
| 3 | **Pain** | The first evidence about users rather than vendors | ● done |
| 4 | **Benchmark** | A **scoring rubric** — five categories, applied to the best product in the world at each of our four core flows | ● done — 15 cells scored |
| 5 | **Patterns** | Five radically different shapes for our key flow, scored with that rubric, one chosen | ● done — hybrid chosen, CLAUDE.md §8 rewritten |

Stage 4 exists to make stage 5 decidable. Without a rubric, *"which of these five is best"* is settled
by taste; with one, it is settled by argument. And the rubric is not invented — its five categories
are lifted from what stages 1–3 actually found.

Sign-off comes after stage 5. Next phase: design system, per CLAUDE.md §1.

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

---

## Stages 1–3 — done

### Flows

**10 of 12 closed.** Flow 01 is declined (login-walled, and its other gap is out of MVP scope).
Flow 10 is handed to the design-system phase rather than left open — it is the one flow about
appearance rather than behaviour, and CLAUDE.md §12 postpones visual direction until after research.

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
grids, no colour, no components. CLAUDE.md §1 puts the design system and mockups after this phase and
this stage must not quietly become them.

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

**Signed off 2026-09-02.** Next phase: design system — not started, per CLAUDE.md §1.

---

## Open questions — the register

**This is the last section on purpose, and it is a running list.** Questions land here as stages
raise them. They are **not** answered as they arrive. **The list is currently empty** — the six that
stood here were closed on 2026-09-02 and are recorded below with their dispositions.

**The protocol.** When a stage turns up something we cannot settle yet, it gets an entry here and the
stage carries on. Nothing is answered mid-flight, because a question answered on partial evidence has
to be re-opened later, and re-opening costs more than waiting. When stages 4 and 5 are done and the
picture is whole, the register is worked through **in one sitting**, and every entry leaves as either
*answered* or *deferred with a stated reason*. That is the last thing the research phase does before
sign-off.

**Adding an entry.** Give it the next ID, say which stage raised it, and — the part that matters —
say **what would answer it**. A question with no named instrument is not a question, it is a worry.

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
| **Q5** | Loss or reassembly cost — which drives adoption? | **Deferred — accepted risk, with the trigger written down.** Nothing in this repository can answer it; trackers are blind to both candidates by construction. Ask five practitioners **before the first feature that only pays off under one answer** — a *reassemble from a previous project* flow versus serious investment in library-wide search. The MVP is the same product under either answer. | Positioning. Nothing in the build |
| **Q6** | Styling engine | **Deferred to the design-system phase**, with the criterion recorded now: tokens and two real themes first-class, and the engine must not push utility classes into components that are themselves the product's value. Decide on two built components. | CLAUDE.md §10, §12 |

**What the sitting did not change.** No answer added a surface. Q2 lands as two more stages inside
Run, which is already a stage list; Q1 lands as a scope switch inside Library, which is already a
browse screen; Q4 lands as a command on a project row, exactly where stage 5 predicted. **CLAUDE.md
§8 therefore stands as written** — three surfaces plus Projects — and the *provisional* marks are
gone from it and from [`5-patterns/patterns.md`](5-patterns/patterns.md).

**Two answers widened the MVP**, and both are recorded as scope rather than smuggled in as detail:
a curated public library ships with the product (Q1), and `SETUP.md` becomes a real artefact written
for an agent rather than a one-line courtesy (Q2). Both were the owner's calls, taken with the
evidence in view.

### Nothing is live

The register is empty. New questions get the next ID and the same protocol: say which stage or
sitting raised it, and say what would answer it.

### Earlier decisions

Four were taken on 2026-09-01, before this register existed, and are recorded under *Decisions
already taken* above with their reasoning in [`1-landscape/comparison.md`](1-landscape/comparison.md).
