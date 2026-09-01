# Research plan

Updated 2026-09-01. The phase runs in five stages. **Four are done, stage 5 is not started.**

| # | Stage | What it produces | Status |
|---|---|---|---|
| 1 | **Landscape** | Who else is in this space, what they sell, and to whom | ● done |
| 2 | **Flows** | Twelve mechanisms captured from live products | ● done |
| 3 | **Pain** | The first evidence about users rather than vendors | ● done |
| 4 | **Benchmark** | A **scoring rubric** — five categories, applied to the best product in the world at each of our four core flows | ● done — 15 cells scored |
| 5 | **Patterns** | Five radically different shapes for our key flow, scored with that rubric, one chosen | ○ not started |

Stage 4 exists to make stage 5 decidable. Without a rubric, *"which of these five is best"* is settled
by taste; with one, it is settled by argument. And the rubric is not invented — its five categories
are lifted from what stages 1–3 actually found.

Sign-off comes after stage 5. Next phase: design system, per CLAUDE.md §1.

---

## Documents

| File | What it holds |
|---|---|
| [`competitors.md`](competitors.md) | 15 companies in three groups — hard, soft, aspirational. Why each is there, what to take from it, a verified link per entry. |
| [`comparison.md`](comparison.md) | All 15 compared on audience, product base, key mechanism, trust, monetisation. Three market patterns, three differences we can hold, and the three decisions the design system needed, each with its reasoning. |
| [`screens-index.md`](screens-index.md) | 38 product captures in [`screens/`](screens/), sorted group / competitor. Sign-in walls labelled. |
| [`user-pain.md`](user-pain.md) | What actually hurts, from two public issue trackers — the first evidence here about users rather than vendors. States plainly what the instrument cannot see. |
| [`continue-postmortem.md`](continue-postmortem.md) | The closest competitor read from source: its block model, the `uses`/`with`/`override` composition primitive, its identity and secret schemes, and the three things its resolver never did. |
| [`flows/README.md`](flows/README.md) | The twelve flows: what each is for, what is collected, what is missing, what access it needed. |
| [`benchmark.md`](benchmark.md) | **Stage 4.** The scored matrix — 15 cells, five categories — the three rules the scoring follows, and the argument behind every score below or above 4. Ends with eight findings, which are what stage 5 spends. Captures in [`benchmark/`](benchmark/). |
| `patterns.md` | **Stage 5 — not written yet.** |

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
| 02 | Library browse, filter, search | ● | [Linear](flows/02-library-browse-filter-search/NOTES-linear.md) |
| 03 | Relations without a canvas | ● | — |
| 04 | Validation: pass, warn, block | ● | [Terraform](flows/04-validation-check-results/terraform-plan-output.md) · [Vercel](flows/04-validation-check-results/NOTES-vercel.md) · [GitHub Actions](flows/04-validation-check-results/NOTES-github-actions.md) · [Port](flows/04-validation-check-results/NOTES-port.md) |
| 05 | Linked vs detached, blast radius | ● | [NOTES](flows/05-linked-vs-detached/NOTES.md) — all three instance states |
| 06 | Export and target adaptation | ● | [Ruler output](flows/06-export-and-target-adaptation/ruler-per-agent-output.md) |
| 07 | Env variables and secrets | ● | [NOTES](flows/07-env-and-secrets/NOTES.md) |
| 08 | Empty state and cold start | ● | [Linear](flows/08-empty-state-and-cold-start/NOTES-linear.md) |
| 09 | Duplicate and fork | ● | [NOTES](flows/09-duplicate-and-fork/NOTES.md) |
| 10 | Dark design language | → | [Material for the next phase](flows/10-dark-design-language/NOTES-linear.md) |
| 11 | Copy: errors, warnings, refusals | ● | [Conflict copy](flows/11-copy-and-error-language/dependency-conflict-copy.md) · [CI failure copy](flows/11-copy-and-error-language/ci-failure-copy.md) |
| 12 | Visibility and portfolio | ● | [NOTES](flows/12-visibility-and-portfolio/NOTES.md) |

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
recorded in [`benchmark.md`](benchmark.md) rather than repeated here.

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

### Done when

One pattern is chosen and written into CLAUDE.md §8, replacing the current one-line screen list, with
the four rejected variants kept in `patterns.md` and the reason each lost recorded.

---

## Decisions already taken

All four landed on 2026-09-01 and are recorded in CLAUDE.md, which is the source of truth.
[`comparison.md`](comparison.md) keeps the reasoning and the rejected alternatives.

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
   [`user-pain.md`](user-pain.md))* A user reports that two `server-postgres` entries in one
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
- [ ] Stage 5 — five patterns compared on that rubric, one chosen and written into CLAUDE.md §8
- [ ] Every question in the register below marked **answered** or **deferred with a stated reason** —
      in one sitting, once stages 4 and 5 are in, not one at a time along the way

Next phase after sign-off: design system. Not started, per CLAUDE.md §1.

---

## Open questions — the register

**This is the last section on purpose, and it is a running list.** Questions land here as stages
raise them. They are **not** answered as they arrive.

**The protocol.** When a stage turns up something we cannot settle yet, it gets an entry here and the
stage carries on. Nothing is answered mid-flight, because a question answered on partial evidence has
to be re-opened later, and re-opening costs more than waiting. When stages 4 and 5 are done and the
picture is whole, the register is worked through **in one sitting**, and every entry leaves as either
*answered* or *deferred with a stated reason*. That is the last thing the research phase does before
sign-off.

**Adding an entry.** Give it the next ID, say which stage raised it, and — the part that matters —
say **what would answer it**. A question with no named instrument is not a question, it is a worry.

### Live

| ID | Question | Raised by | What would answer it | What it blocks |
|---|---|---|---|---|
| **Q1** | **Cold start: demo problem or product decision?** CLAUDE.md §11 plans *~30 realistic items for any mockup*. Linear seeds a new workspace with four **real**, editable objects, so the product is never empty and the validation pass has something to run on before the user types anything. | Stage 2, flow 08 | **Stage 5.** Every variant must show itself with an empty library and with a seeded one — the cheapest possible resolution, since it falls out of work we are doing anyway. | CLAUDE.md §11, and the whole first-run experience |
| **Q2** | **How much weight does `SETUP.md` carry?** §6 gives it one line, while [`user-pain.md`](user-pain.md) finds the loudest pain in the ecosystem lives exactly there — the archive lands on a machine and does not run. Either we own that problem or we say plainly it is not our war. | Stage 3, finding 5 | **Stage 4, flow B4** (produce and hand over), plus the export end of stage 5. | The real scope of CLAUDE.md §6 |
| **Q3** | **Can a project contain another project**, or only items? | CLAUDE.md §12, from the start | **Stage 5** — whether any of the five variants needs composition in order to work. If none does, it is out. | The data model, later. Not the MVP |
| **Q4** | **Can a detached item be promoted back into the library** as a new item? | CLAUDE.md §12, sharpened by flow 05 | **Stage 5** — the variant that renders state 6, *detached and locally modified*, will show whether a return path has anywhere to live. Flow 05 established there is **no prior art** for it, so this one we invent rather than copy. | CLAUDE.md §5, later |
| **Q5** | **Loss or reassembly cost — which actually drives adoption?** *I cannot find what I wrote three months ago* versus *I re-copy the same four files into every new project*. CLAUDE.md §2 bets on neither; it bets on silent breakage. | Stage 3 | **Nothing we have used so far.** Issue trackers are blind to both by construction — neither ever becomes an issue. This needs asking people. | Positioning and the pitch. **Not** the MVP build, which is the same product under any answer |
| **Q6** | **Styling engine** — Tailwind vs CSS Modules vs vanilla-extract. | CLAUDE.md §12, from the start | Not research. A design-system decision, best made with a component or two actually built. | Nothing in this phase |

### Notes on two of them

**Q5 is the one to be honest about.** It is the only entry here that no planned stage will touch.
Stage 4 benchmarks products and stage 5 compares shapes; neither asks a human anything. So Q5 leaves
the register as *deferred — accepted risk* unless we deliberately add a stage that asks people. Saying
that out loud is the whole point: an unmarked unknown is the dangerous kind.

**Q1 and Q2 are pending rather than open.** Both are already scheduled into stage 5, and they are the
reason that stage has a fixed list of questions every variant must answer.

### Answered and closed

Nothing yet. Four decisions were taken on 2026-09-01, before this register existed, and are recorded
under *Decisions already taken* above with their reasoning in [`comparison.md`](comparison.md).
