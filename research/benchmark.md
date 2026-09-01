# Benchmark — stage 4

Started 2026-09-01. **9 of 16 cells scored.** Status and design in
[`research-plan.md`](research-plan.md); this file is the scoring itself.

The question: **for each of our four core flows, who does it best, how well, and against what
standard?** Stages 1–3 produced observations. This turns them into a scale, and stage 5 spends it.

Captures live in [`benchmark/`](benchmark/), alongside the earlier ones in [`flows/`](flows/) —
several cells are scored from flow captures that were already good enough, and each says so.

---

## How to read a score

Five categories, each lifted from a finding in stages 1–3 so the rubric is grounded rather than
invented.

| # | Category | The question |
|---|---|---|
| **C1** | State legibility | Can you read the current state without acting on it? |
| **C2** | Consequence disclosure | Before an irreversible step, is the cost stated in advance? |
| **C3** | Failure copy | Does a message name the item, the rule and the observed value? |
| **C4** | Recovery | Is there a way back, offered where the problem is? |
| **C5** | Economy | Is anything on screen that cannot act, or missing that must be? |

Anchors, so a number means something:

- **1** — actively misleads. The interface implies something untrue.
- **2** — the information does not exist in the product.
- **3** — correct, but you must go looking for it.
- **4** — present where you need it, in the right words.
- **5** — you could not miss it, and it changed what you did next.

### Three rules the scoring follows

**Score first, then argue, then revise once.** The number is written before the sentence justifying
it, the sentence is written, and the number is revisited exactly once. Where the second look moved a
score, the move is recorded.

**A dash is not a zero.** `—` means the flow contains no instance of what the category grades, or we
did not observe one. It is always followed by which of the two, because *"this product has no failure
copy"* and *"we never made it fail"* are different facts and only one of them is the product's.

**The read-only method cannot see past a commit, and that is itself a finding.** C2 is the column
about the moment before an irreversible act. In a live account we will not perform one — no
production promotion, no library update accepted, no `apply`. So C2 is observable **only where the
disclosure arrives before the click**. Which is the point: a product whose disclosure appears after
you commit is invisible to this benchmark for exactly the reason it is useless to the user.

---

## What changed from the plan's candidate list

The plan noted availability per candidate. Three of those notes were wrong on this machine, and one
substitution follows.

| Plan said | Reality, 2026-09-01 | What we did |
|---|---|---|
| VS Code ✓ free | **Was not installed** — not in PATH, `Program Files`, or `AppData\Local\Programs` | **Installed 2026-09-01** at the owner's hand. It carries three cells (B1, B2, B3) and no substitute is as close to our mechanics. |
| Compose ✓ CLI | **Docker not installed** | Open. See *still to capture*. |
| Brewfile — read format only, macOS | Unchanged, and a format we can only read is not a benchmark | **Substituted with `npm install`** — the same problem (a declared set resolved against constraints the items carry), on a tool that is installed and can be made to fail. Documented in [`benchmark/npm-eresolve.md`](benchmark/npm-eresolve.md). |
| Obsidian ✓ free | **Not installed** | Open — another install, and the weakest of the four B1 candidates. |

---

## The matrix

`○` not yet captured · `—` see the cell's reasoning

| | Candidate | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|---|
| **B1 Find** | Linear ⌘K + filters | **5** | — | **4** | **5** | **5** |
| | VS Code palette + Extensions | ○ | ○ | ○ | ○ | ○ |
| | GitHub code search | ○ | ○ | ○ | ○ | ○ |
| | Obsidian quick switcher | ○ | ○ | ○ | ○ | ○ |
| **B2 Assemble** | Figma instances + library | **2** | **4** | — | **3** | **5** |
| | VS Code workspace extensions | ○ | ○ | ○ | ○ | ○ |
| | `npm install` *(substitute)* | **3** | **4** | **5** | **4** | **4** |
| | Docker Compose | ○ | ○ | ○ | ○ | ○ |
| **B3 Check** | `terraform` plan + validate | **5** | **5** | **4** | **4** | **5** |
| | VS Code Problems panel | ○ | ○ | ○ | ○ | ○ |
| | GitHub Actions run | **5** | — | **1** | **2** | **3** |
| | Vercel build log | **5** | — | — | — | **4** |
| **B4 Produce** | Vercel deploy | **5** | — | — | — | **3** |
| | `create-next-app` | **4** | **4** | — | **2** | **3** |
| | Figma export dialog | ○ | ○ | ○ | ○ | ○ |
| | Ruler per-agent output | **3** | **2** | — | **4** | **4** |

---

## B1 — Find one thing in a large personal collection

Our screen: **Library**.

### Linear — ⌘K, filters, empty states

Source: [`flows/02-library-browse-filter-search/NOTES-linear.md`](flows/02-library-browse-filter-search/NOTES-linear.md) ·
[`flows/08-empty-state-and-cold-start/NOTES-linear.md`](flows/08-empty-state-and-cold-start/NOTES-linear.md)

- **C1 = 5.** A filter is a sentence with its own ✕, the state is in the URL, the keyboard-hint bar
  recomputes itself from what is currently possible, and a filter that matches nothing prints
  **"4 issues hidden by filters"**. It separates *there is nothing* from *there is something and you
  are not looking at it*, with a number. That is the anchor-5 case exactly: it changes what you do
  next.
- **C2 = —, no instance.** Nothing in finding is irreversible. The one state-creating action on the
  screen, `Save` a filter into a View, is trivially undone and discloses nothing; not enough to grade
  a column on.
- **C3 = 4.** *"No results found · Go to advanced search"*, and the query is quoted back into the
  results heading (*Quick results for "import"*). Named and specific. Not 5 because when a filter
  empties the list it says how many are hidden but never **which filter did it** — with three chips
  applied you still guess.
- **C4 = 5.** The row that reports the failure is the row you press to escape it, and `Clear
  Filters ✕` sits inside the empty state next to the count. Recovery is not adjacent to the problem;
  it is the same object.
- **C5 = 5.** The toolbar disappears over an empty Projects list; the hint bar shrinks to the two
  hints that still apply. *(Second look: the un-deduped duplicate filter chip tempted a 4. Rejected —
  that is a display bug, not something on screen that cannot act.)*

### Not yet captured

VS Code palette + Extensions search, GitHub code search, Obsidian quick switcher.

---

## B2 — Assemble a set from that collection, with constraints

Our screen: **Project Builder**.

### Figma — instances, overrides, library updates

Source: [`flows/05-linked-vs-detached/NOTES.md`](flows/05-linked-vs-detached/NOTES.md)

- **C1 = 2.** Figma states *"this is an instance"* three times — glyph, colour, and a sentence naming
  the library — and says nothing at all about *"this instance no longer matches its main"*. A
  modified instance is drawn identically to a clean one everywhere except a context menu you must
  open on an object you must first select. *(Second look moved this from 3 to 2. The case for 3 is
  that the information is reachable, so it is merely "go looking for it". The case for 2 is that
  three loud channels announcing the link, and silence about the drift, is read as a claim of
  cleanliness. We stopped short of 1 only because Figma never asserts "unmodified" in words.)*
- **C2 = 4.** The library-updates modal states **423 instances** before you accept, grouped by
  publish event with who published and when, and the count appears exactly when the scope widens past
  what you can see. Not 5: the counts only appear with *"Show updates for all pages"* switched on,
  and it is off by default — a disclosure you can miss is not one you could not miss.
- **C3 = —, not observed.** No failure state was produced in this flow. A missing or unavailable
  library was not captured.
- **C4 = 3.** Two halves pointing opposite ways, averaged honestly. While linked, recovery is
  outstanding: `Reset instance` and `Reset fill` — property-granular, self-labelling, sitting
  directly beside `Detach`. Across the detach boundary it is nothing at all: the origin is erased,
  there is no badge, no memory, no way back.
- **C5 = 5.** The reset rows are **absent** on a clean instance, not greyed out. The affordance
  appears only when it can act — the same decision Linear makes twice, and the one Vercel gets wrong.

### `npm install` — a declared set resolved against constraints *(substitute for Brewfile)*

Source: [`benchmark/npm-eresolve.md`](benchmark/npm-eresolve.md)

- **C1 = 3.** The resolved set is knowable — `npm ls`, the lockfile — but only by running something
  and reading a wall of text. Nothing shows you the shape of what you have declared.
- **C2 = 4.** The unreviewed `postinstall` is not run, and is named precisely: package, version, the
  hook itself, and two commands — review, or allow this one. Not 5: it is printed as `npm warn`,
  visually identical to a funding notice three lines above it.
- **C3 = 5.** `ERESOLVE` answers all four questions a conflict message owes — what was required
  (`peer react@"^18.0.0 || ^19.0.0"`), what was found (`react@17.0.2`), who required it, and who
  asked for what was found (`from the root project`). That last one is our
  `addedBy: manual | dependency`, and almost nothing else in this benchmark states it. Then it prints
  both escape hatches with the cost in the same sentence: *"to accept an incorrect (and potentially
  broken) dependency resolution."*
- **C4 = 4.** `--force` and `--legacy-peer-deps` are offered in the failure itself with their price
  named. Not 5: `Fix the upstream dependency conflict` is homework, not a remedy — npm knows the
  range and the registry and never suggests the version that would satisfy both.
- **C5 = 4.** Twelve lines on screen, the full trace on disk. Deductions: the path to that trace is
  an absolute cache directory nobody will open, and *"146 packages are looking for funding"* is
  printed at the same weight as everything else.

### Not yet captured

VS Code per-workspace extensions and Recommended Extensions; Docker Compose.

---

## B3 — Check a set and report what is wrong

Our screen: **the validation pass**.

### `terraform` — a successful plan, and validate against a broken config

Source: [`flows/04-validation-check-results/terraform-plan-output.md`](flows/04-validation-check-results/terraform-plan-output.md) ·
[`benchmark/terraform-validate-errors.md`](benchmark/terraform-validate-errors.md)

- **C1 = 5.** One summary line that is a count — `Plan: 2 to add, 0 to change, 0 to destroy` — you
  can act on alone. Every resource addressed by name before it is described. A symbol per operation
  in the left margin, colour redundant. And `(known after apply)` on every value it cannot compute:
  it never guesses and never hides the gap.
- **C2 = 5.** The artefact exists for no other reason. Then it undercuts its own authority on
  purpose — *"Terraform can't guarantee to take exactly these actions"* unless you saved the plan —
  which is why the rest is believed.
- **C3 = 4.** Captured on purpose: a config carrying our three findings — a target-path collision, a
  reference to something not in the set, an item missing what it needs. `Reference to undeclared
  resource` is a 5 on its own — it names the item (`local_file.readme`), the file and line, **echoes
  the offending source line back**, and states the rule in words (*"has not been declared in the root
  module"*). The duplicate names **both** sides with a column range, `main.tf:10,1-33`, which is
  precisely the sentence CLAUDE.md §6 asks for on a merged MCP config. *(Second look moved this from
  5 to 4.)* Two deductions, and both are ours to avoid: one defect — a resource with no content —
  produced **four** diagnostics differing only in which permutation of a mutually exclusive set they
  quote, so the list counts internal rules rather than things wrong with the user's work; and a
  parse-level error silently cancels the checks behind it, so fixing one problem appears to reveal
  new ones.
- **C4 = 4.** The recovery is structural and total: a plan mutates nothing, so there is nothing to
  come back from. Not 5 because when the plan is wrong, nothing is offered in place — you leave for
  the editor.
- **C5 = 5.** No spinner, no progress theatre. Text that appears when it is ready and reads correctly
  frozen. Our brief calls the validation pass "an animated sweep"; this is the argument for keeping
  the animation subordinate to a result that survives being paused.

### GitHub Actions — a run with 102 jobs and four verdicts

Source: [`flows/04-validation-check-results/NOTES-github-actions.md`](flows/04-validation-check-results/NOTES-github-actions.md)

- **C1 = 5.** Four verdicts, four glyphs, colour redundant rather than load-bearing; **skipped** and
  **cancelled** each distinct from failure; a mixed commit gets a partially-filled ring instead of
  being flattened to its worst state; a counted digest above the detail; and a failed job keeps its
  duration — *failed 4 hours ago in 14m 6s*.
- **C2 = —, no instance.** A run is a report of something already done.
- **C3 = 1.** Fourteen of seventeen annotations read, in full, `Process completed with exit code 1.`
  The slot is prominent, counted in the header as **"11 errors and 6 warnings"**, and empty. A count
  promises eleven pieces of information; this is the anchor-1 case — the interface implies something
  untrue. The three exceptions show what a 4 looks like: `non-retryable` (whether a re-run helps),
  `exceeded the maximum execution time of 30m0s` (the limit as a number), and cause and consequence
  filed as two separate annotations.
- **C4 = 2.** Nothing is offered next to a failure. The single piece of recovery guidance in the whole
  run — the word `non-retryable` — arrives by luck of which subsystem emitted it.
- **C5 = 3.** The digest is the same component at run and job altitude, collapsed by default, and
  deep links select in the tree. But on a fully public repository the log bodies are behind
  *"Sign in to view logs"* — the thing you came for is missing, and a control is shown over it.

### Vercel — the build log and the deployment page

Source: [`flows/04-validation-check-results/NOTES-vercel.md`](flows/04-validation-check-results/NOTES-vercel.md)

- **C1 = 5.** A deployment is a stack of collapsed stages, each with its own verdict and its own
  duration; a stage that did not run gets a clock, not a failure. The log header states **"66 lines"**
  before you read and offers `Find in logs`. Hovering a timestamp gives absolute time, relative time,
  **relative to start** and **relative to previous** — the last of which is how you find the step that
  hung without doing arithmetic. This is our validation pass, structurally, and it is the reference.
- **C2 = —, no instance** in the surfaces captured.
- **C3 = —, not observed.** Every deployment in the account succeeded. Stated as a gap in the
  original note and still open; GitHub Actions was captured to cover it.
- **C4 = —, not observed.** Instant Rollback exists in the product and performing one is out of
  bounds for a read-only capture in the owner's account.
- **C5 = 4.** The log page carries nothing that cannot act. Not 5 because the same product, one
  screen away, is this research's standing counter-example — see the B4 cell below.

### Not yet captured

VS Code Problems panel with ESLint/tsc — the one candidate here that reports **a set of files**
rather than a run, which is our case exactly.

---

## B4 — Produce an artefact and hand it over to another machine

Our screen: **Result / Export**.

### Vercel deploy

Source: as above, plus [`flows/07-env-and-secrets/NOTES.md`](flows/07-env-and-secrets/NOTES.md)

**A thin cell, and it should be read as thin.** Vercel's strength is the process (B3); as a
*handover* it gives us the stage structure and little else within read-only reach.

- **C1 = 5.** Duration in the deployments list before you open anything, which is what makes a list
  scannable for the anomaly. `Assigning Custom Domains ✓` states the handover as a stage like any
  other.
- **C2 = —, unobservable.** Promoting to production is the irreversible step and we will not perform
  one in the owner's account.
- **C3 = —, not observed.** · **C4 = —, not observed.**
- **C5 = 3.** The environment-variables empty state keeps a search box, four filter dropdowns and a
  sort control on screen, all filtering nothing. Three products in this research suppress an
  affordance that cannot act; this is the one that does not, and it does it on the screen our
  `needsEnv` work copies most from.

### `create-next-app`

Source: [`benchmark/create-next-app-output.md`](benchmark/create-next-app-output.md)

- **C1 = 4.** The manifest is printed before the work and split by role — dependencies and
  devDependencies, by name, before a single package is fetched. Side effects are stated as completed
  facts, including `Initialized a git repository.` Not 5: the run ends on `Success!` and nothing
  else — no count of files, no tree, and no mention that it just wrote a `CLAUDE.md` and an
  `AGENTS.md` into your repository.
- **C2 = 4.** Inherited from npm's `allow-scripts` gate, and credited honestly: the unreviewed
  `postinstall` is named and not run.
- **C3 = —, not observed.** The scaffold succeeded.
- **C4 = 2.** Nothing offered for undoing a scaffold. The `git init` is an accidental recovery — the
  tree is inspectable afterwards — but it is never presented as one.
- **C5 = 3.** The signal is buried in 358 packages of install noise, a deprecation warning scrolls
  past and is never restated at the end, and the one genuinely dangerous line sits at the same weight
  as a funding notice. **Severity that lives only in the words and not in the shape of the line** is
  our `Problem` and our `Note` rendered in the same grey.

### Ruler — one source, six agent targets

Source: [`flows/06-export-and-target-adaptation/ruler-per-agent-output.md`](flows/06-export-and-target-adaptation/ruler-per-agent-output.md)

- **C1 = 3.** Six log lines for six targets and a fenced managed block in `.gitignore` naming what
  was generated — but the mapping from target to artefact is knowable only by listing the directory
  afterwards, and two targets it announces produce no file of their own.
- **C2 = 2.** It overwrites files in your repository and says nothing in advance about which. The
  `.bak` beside each is a remedy, not a disclosure; the information does not exist before the act.
- **C3 = —, not observed.**
- **C4 = 4.** A `.bak` beside every overwritten file **and** a named `START/END` block so a re-run
  can find and replace exactly what it wrote. Real recovery, located on disk where the damage would
  be. Not 5: nothing tells you the backups exist.
- **C5 = 4.** Six lines, one summary, no theatre.

### Not yet captured

Figma's export dialog — the only remaining candidate here that is a *dialog* rather than a log, which
is the shape our Export confirmation actually takes.

---

## What the rubric is already saying

Written down now because it is what stage 5 spends. All of it is provisional until the matrix fills.

1. **Nothing in this benchmark scores well on C3 by accident.** The two 5-grade failure messages we
   have — npm's `ERESOLVE` and Port's `where "Open Critical Vulnerabilities" = 0 · Value: 1` — are
   both emitted at the altitude that knows what was *required*. The 1-grade one, `exit code 1`, is
   emitted by a process that only knows it stopped. This is an architecture decision in our validator,
   not a copy decision: the check that knows the rule must be the thing that writes the sentence.

2. **C2 splits products into two groups, and it is not the group you would guess.** Terraform and
   Figma disclose before the act and score 4–5. Ruler, `create-next-app` and Vercel disclose after,
   or not at all, and the good behaviour they do have (`.bak` files, `git init`) is *recovery wearing
   consequence disclosure's clothes*. Building the way back is cheaper than saying what will happen,
   so it is what gets built. Our unclean-export confirmation (CLAUDE.md §6) is squarely in the
   expensive half, which is the point of it.

3. **Two independent vendors, two mechanics, same two.** Ruler and `create-next-app` both write
   agent files, and both landed on *copy the content in a named fenced block* or *point at the
   canonical file*. Flow 06 inferred "at most two mechanics plus a naming convention per agent" from
   one sample; it now has two, from unrelated codebases. Our four export targets are not four
   formats.

4. **Count problems the way the user counts them, and say when a check did not run.** Terraform
   reports every diagnostic in one pass where npm stops at the first — the right instinct, and ours.
   But it emits one message per internal rule that fired, not one per defect in the work, and a
   parse-level failure cancels the later stages without a word. Both are avoidable, and the second one
   is already answered: **Skipped** (CLAUDE.md §6) covers *nothing to check* and *blocked by an
   earlier stage* alike, so the stage list never quietly shrinks.

5. **The economy rule is now four to one.** Linear suppresses a toolbar and trims a hint bar, Figma
   hides a reset that has nothing to reset, npm's ERESOLVE prints only the hatches that apply.
   Vercel keeps four dropdowns over an empty list. Settled: **an action that cannot act is not
   shown** — which is, in this document, the fourth independent confirmation of the decision already
   taken in CLAUDE.md §9.

---

## Still to capture

| What | Cells | Needs |
|---|---|---|
| VS Code — palette, Extensions search, per-workspace enable + Recommended Extensions, Problems panel with ESLint/tsc | B1, B2, B3 | The install now in progress |
| Figma export dialog | B4 | A browser session in the owner's Figma |
| GitHub code search | B1 | Browser, public, no login |
| Obsidian quick switcher | B1 | Another install — the weakest of the four B1 candidates. Drop it and score B1 on three, unless it is wanted |
| Docker Compose | B2 | Docker not installed. `npm` already covers assemble-under-constraints; propose dropping and recording why |

**Two candidates are proposed for removal** rather than installation — Obsidian and Docker Compose —
on the grounds that each duplicates a candidate already scored and neither is best-in-class at
anything the others miss. That would make the matrix 14 cells, not 16, with the reason recorded here.
The plan's *done when* is written as sixteen; changing it is a decision, so it is proposed and not
taken.
