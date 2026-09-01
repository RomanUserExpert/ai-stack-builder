# Open questions — the working sheet for the closing sitting

Prepared 2026-09-01, to be worked through in one sitting. **Six questions.**

**This is not a second register.** The register — with each question's ID, the stage that raised it,
what would answer it and what it blocks — stays at the end of
[`research-plan.md`](research-plan.md), and that file remains the source of truth for *status*. This
sheet holds the other half: **where to read before deciding**, the options actually on the table, and
a recommendation for each. When the sitting happens, the reasoning lands here and the one-line
disposition lands in the register.

CLAUDE.md §12 has been bitten twice by two lists drifting. Neither of these lists is a copy of the
other: one says *what is decided*, this one says *what to read and what the choices are*.

## Where each one stands

| | Question | Status going in |
|---|---|---|
| **Q1** | Cold start — demo problem or product decision? | Evidence answers it. Recommendation below. |
| **Q2** | How much weight does `SETUP.md` carry? | **Needs a call** — it is a scope boundary, not a wording choice. |
| **Q3** | Can a project contain a project? | Evidence answers it. Recommendation below. |
| **Q4** | Can a detached item be promoted back into the library? | Evidence answers it; one fork in the semantics. |
| **Q5** | Loss or reassembly cost — which drives adoption? | **Needs a call** — do we pay for an answer at all? |
| **Q6** | Styling engine | **Needs a call** — blocks nothing; timing only. |

---

## Q1 — Cold start: demo problem or product decision?

CLAUDE.md §11 plans *~30 realistic items for any mockup*. Linear ships a new workspace with four
**real**, editable objects, so the product is never empty and the model is learned by holding four
instances of it.

**Read before deciding**

- [`flows/08-empty-state-and-cold-start/NOTES-linear.md`](flows/08-empty-state-and-cold-start/NOTES-linear.md)
  — the four seeded issues, and the rule that picks between **three registers of emptiness**
  (never-used concept → define it · routine → one line · filtered to zero → count what is hidden).
- [`benchmark/NOTES-obsidian.md`](benchmark/NOTES-obsidian.md) — an empty query that becomes the
  create row, and an empty tab that is three actions with their shortcuts inline.
- [`benchmark/NOTES-vscode.md`](benchmark/NOTES-vscode.md) — the recommendation prompt on opening a
  folder, and `@recommended` split into counted sections.
- [`patterns.md`](patterns.md) — question 1 of the five, answered by each of the five shapes; three of
  them are broken without a seed.
- [`benchmark.md`](benchmark.md), finalisation — why the trackers are silent here and what that does
  and does not prove.

**Options.** (a) Ship a seeded library — real Items in a real Project, editable and deletable.
(b) Demo content behind a button. (c) Empty, with a strong empty state only.

**Recommendation — (a), and the size is set by a requirement rather than by taste.** The seed must
produce **at least one Problem and at least one Note**: a real conflict, a target-path collision and a
missing env key. A first run that shows six green ticks teaches nothing about what the product is for.
That is 8–12 items and one project. The ~30 in §11 stays true for mockups, which is a different job.

**Blocks:** CLAUDE.md §11 and the whole first-run experience.

---

## Q2 — How much weight does `SETUP.md` carry?

§6 gives it one line — *"external items become instructions in `SETUP.md`"* — while the loudest pain
in the ecosystem lives exactly there: the archive lands on a machine and does not run. Either we own
that problem or we say plainly it is not our war.

**Read before deciding**

- [`user-pain.md`](user-pain.md), finding 1 — *MCP Servers Don't Work with NVM*, **182 reactions**,
  and a top-of-tracker made of PATH, node version managers, platform paths and processes dying at
  startup. Read the *"most of this is out of our reach"* paragraph especially: it draws the line we
  are being asked to place.
- [`benchmark.md`](benchmark.md) — the four B4 cells (no candidate above 4), finding 8, and the
  finalisation's *gap* section: every cell scores what a product says about **its own state**, none
  about **the machine its artefact lands on**.
- [`flows/06-export-and-target-adaptation/ruler-per-agent-output.md`](flows/06-export-and-target-adaptation/ruler-per-agent-output.md)
  — the two distribution mechanics (copy with provenance, or point at a canonical file), the managed
  `.gitignore` block, and the `.bak` beside every overwritten file.
- [`benchmark/create-next-app-output.md`](benchmark/create-next-app-output.md) — the same two
  mechanics from an unrelated vendor, and a fenced block that **explains its own re-appearance** in
  three sentences. Also the anti-pattern: a run that ends on the word *Success!* and lists nothing.
- [`flows/04-validation-check-results/NOTES-vercel.md`](flows/04-validation-check-results/NOTES-vercel.md)
  — the stage list, and how a file tree is rendered inside a running process including how to cut it
  short.
- [`flows/07-env-and-secrets/NOTES.md`](flows/07-env-and-secrets/NOTES.md) — type before value, the
  irreversible option as default, and the note placeholder *"where to rotate, or who to contact"*.
- [`continue-postmortem.md`](continue-postmortem.md) — its identity and secret schemes, and the three
  things its resolver never did.

**Options**

1. **Disclose the handover inside Run.** The last stages of the check show what the archive contains
   and what the receiving machine must still do: a `SETUP.md` preview, the pinned `ref`s, the
   platform-correct `targetPath`s, `.env.example`. Read *before* Export is pressed. Nothing runs on
   anyone else's machine. Fits the current scope; it is two more stages in a list that already exists.
2. **Also emit a verify script** into the archive, which the user runs on the target machine — is
   node present, is the path what we assumed, are the keys visible. Aims straight at the 182-reaction
   pain, and expands the MVP: a new generated artefact, plus platform coverage.
3. **Say it is not our war**, keep `SETUP.md` as one line, and record the reason.

**Recommendation — (1), with the export designed so that (2) is additive rather than a rewrite.**

**Blocks:** the real scope of CLAUDE.md §6.

---

## Q3 — Can a project contain another project, or only items?

**Read before deciding**

- [`user-pain.md`](user-pain.md), finding 4 — `reuse blocks assistant`: **0 results** in a
  6,677-issue tracker belonging to a product that shipped a hub for exactly this.
- [`continue-postmortem.md`](continue-postmortem.md) — the `uses`/`with`/`override` composition
  primitive, and which half of that product was switched off.
- [`patterns.md`](patterns.md) — **no variant needed composition to work**, which was the named
  instrument for this question.
- [`comparison.md`](comparison.md) — the three market patterns, for where composition sits
  commercially.

**Recommendation — no. Items only.** Three independent signals point the same way, and nothing in the
five shapes asked for it. Additive later if it is ever wanted.

**Blocks:** the data model, later. Not the MVP.

---

## Q4 — Can a detached item be promoted back into the library?

**Read before deciding**

- [`flows/05-linked-vs-detached/NOTES.md`](flows/05-linked-vs-detached/NOTES.md) — the whole file.
  `Reset instance` beside `Reset fill` (two granularities, self-labelling), the 423-instance count,
  and the finding that matters here: **there is no prior art for a return path.** Figma erases the
  origin at detach.
- [`flows/09-duplicate-and-fork/NOTES.md`](flows/09-duplicate-and-fork/NOTES.md) — duplicate and fork
  semantics, for the naming.
- [`patterns.md`](patterns.md) — in the chosen shape the command has an obvious home: the project row,
  next to detach and reset.
- CLAUDE.md §5 (linkage and blast radius) and §7 (state 6, *detached, locally modified*).

**The fork.** Promote as a **new item**, or **update the original**?

**Recommendation — a new item, with the project's row re-linking to it.** Updating the original would
change every other project that links to it — blast radius spent on an action the user took inside
one project, which is the thing §5 exists to warn about. *"Push my changes to the original"* is a
different action with a different confirmation, and it is not built in the MVP.

**Blocks:** CLAUDE.md §5, later.

---

## Q5 — Loss or reassembly cost: which actually drives adoption?

*I cannot find what I wrote three months ago* versus *I re-copy the same four files into every new
project*. CLAUDE.md §2 bets on neither; it bets on silent breakage.

**Read before deciding — and note what these are for.** Nothing in this repository can answer this
question. The links below frame it; they do not decide it.

- [`user-pain.md`](user-pain.md) — the method section and the blindness table. An issue tracker
  records **breakage, not friction**, so both candidates are invisible to it by construction. This is
  the reason the question is still open and the reason no planned stage touched it.
- [`competitors.md`](competitors.md) and [`comparison.md`](comparison.md) — who positions on loss, who
  on reassembly, who on breakage. Positioning is not evidence of demand, but it is evidence of what
  fifteen companies believed.
- [`continue-postmortem.md`](continue-postmortem.md) — which half of a real product with 1.58M
  installs survived.

**Options.** (a) Defer as accepted risk, with a named trigger. (b) Add a stage: five to eight
conversations with practitioners before sign-off. (c) Declare a third answer from the pain data —
*it does not run when it lands*, 182 reactions — and mark plainly that this is ecosystem pain, not a
reason to adopt our product.

**Recommendation — (a), with the trigger written down**: ask five people **before the first feature
that only pays off under one of the answers** (a "reassemble from a previous project" flow versus
serious investment in library-wide search). The MVP is the same product under either answer, so the
question blocks nothing today — it blocks the pitch and the post-MVP order.

**Blocks:** positioning. **Not** the MVP build.

---

## Q6 — Styling engine

Tailwind vs CSS Modules vs vanilla-extract.

**Read before deciding.** Almost nothing in the research bears on this, and that is worth stating
rather than padding:

- CLAUDE.md §10 — **no UI kits**, the design system is custom and *is part of the product's value*.
- CLAUDE.md §3 — **dark from day one**, and light is a design decision rather than a colour
  inversion. That is a theming requirement, not a preference.
- [`flows/10-dark-design-language/NOTES-linear.md`](flows/10-dark-design-language/NOTES-linear.md) —
  the material already gathered for the design-system phase, which is where this decision belongs.

**The criterion, whenever it is decided.** Tokens and two real themes must be first-class, and the
engine must not push utility classes into components that are themselves the product's value.

**Options.** (a) Defer to the design-system phase, decided on two built components, with the criterion
recorded now. (b) CSS Modules + custom properties. (c) vanilla-extract.

**Recommendation — (a).** It blocks nothing in this phase, and the register's own instinct was right:
this is best decided with a component in hand rather than in the abstract.

**Blocks:** nothing in this phase.

---

## Tomorrow

Three of the six have recommendations that follow from evidence already collected — **Q1, Q3, Q4**.
Three are calls to make — **Q2** (a scope boundary), **Q5** (whether to buy an answer), **Q6**
(timing only).

When they are settled: the dispositions go into the register in
[`research-plan.md`](research-plan.md), the decisions that change the spec go into CLAUDE.md, and the
provisional marks come off [`patterns.md`](patterns.md) and CLAUDE.md §8 — which is the last thing
the research phase does before sign-off.
