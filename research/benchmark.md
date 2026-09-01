# Benchmark — stage 4

Written 2026-09-01. **All 15 cells scored.** Status and design in
[`research-plan.md`](research-plan.md); this file is the scoring itself.

The question: **for each of our four core flows, who does it best, how well, and against what
standard?** Stages 1–3 produced observations. This turns them into a scale, and stage 5 spends it.

Captures are in [`benchmark/`](benchmark/), and several cells are scored from
[`flows/`](flows/) captures that were already good enough. Every cell says which.

---

## How to read a score

Five categories, each lifted from a finding in stages 1–3, so the rubric is grounded rather than
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
score, the move is recorded in the cell.

**A dash is not a zero.** `—` means the flow contains no instance of what the category grades, or we
did not observe one. It is always followed by which of the two, because *"this product has no failure
copy"* and *"we never made it fail"* are different facts and only one of them is the product's.

**The read-only method cannot see past a commit, and that is itself a finding.** C2 is the column
about the moment before an irreversible act. In a live account we performed none — no production
promotion, no library update accepted, no `apply`, no export. So C2 is observable **only where the
disclosure arrives before the click**. Which is the point: a product whose disclosure appears after
you commit is invisible to this benchmark for exactly the reason it is useless to the user.

### Method

Public web through the browser; the owner's own sessions where the product needed one; local CLIs in
scratch directories outside the repo. **Desktop applications were driven from this session** — the
window raised, keystrokes sent to it, and each frame captured from that window's own rectangle, never
the whole screen. Two consequences worth stating:

- **Obsidian was pointed at a substituted vault.** The owner's vault holds one note, which cannot
  answer *find one thing in a large collection*. A scratch vault was built from this repository's own
  27 markdown files, `obsidian.json` was swapped with the original backed up, and it was **restored
  afterwards** — the app was restarted on the owner's vault and left as found.
- **Figma was driven by keyboard only**, in the owner's real design file: deselect, open the export
  dialog, close it. Nothing was clicked on the canvas, selected, changed or exported.

---

## What changed from the plan's candidate list

The plan noted availability per candidate. Three of those notes were wrong on this machine.

| Plan said | Reality, 2026-09-01 | Outcome |
|---|---|---|
| VS Code ✓ free | **Was not installed** | Installed by the owner. Carries three cells and no substitute is as close to our mechanics. All three captured. |
| Obsidian ✓ free | **Was not installed** | Installed by the owner. Captured against a substituted vault, as above. |
| Compose ✓ CLI | **Docker not installed** | **Dropped**, and the reason recorded: `npm install` already covers *assemble a set under constraints*, does it on a tool that is installed, and can be made to fail. Compose would have been a fourth opinion on a question already answered three ways. The matrix is **15 cells, not 16**. |
| Brewfile — read format only, macOS | Unchanged, and a format we can only read is not a benchmark | **Substituted with `npm install`** — [`benchmark/npm-eresolve.md`](benchmark/npm-eresolve.md). |

---

## The matrix

`—` means see the cell's reasoning.

| | Candidate | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|---|
| **B1 Find** | Linear ⌘K + filters | **5** | — | **4** | **5** | **5** |
| | GitHub code search | **5** | — | **3** | **3** | **4** |
| | Obsidian quick switcher | **4** | **2** | **2** | **5** | **4** |
| | VS Code palette + Extensions | **4** | — | **2** | **2** | **4** |
| **B2 Assemble** | VS Code workspace extensions + trust | **5** | **5** | — | **4** | **3** |
| | `npm install` *(substitute)* | **3** | **4** | **5** | **4** | **4** |
| | Figma instances + library | **2** | **4** | — | **3** | **5** |
| **B3 Check** | `terraform` plan + validate | **5** | **5** | **4** | **4** | **5** |
| | VS Code Problems panel | **5** | — | **4** | **4** | **5** |
| | Vercel build log | **5** | — | — | — | **4** |
| | GitHub Actions run | **5** | — | **1** | **2** | **3** |
| **B4 Produce** | Vercel deploy | **5** | — | — | — | **3** |
| | `create-next-app` | **4** | **4** | — | **2** | **3** |
| | Figma export dialog | **4** | — | **4** | **3** | **3** |
| | Ruler per-agent output | **3** | **2** | — | **4** | **4** |

### Who does it best

- **B1 Find — Linear**, and not narrowly. It is the only candidate that answers the dead end with a
  remedy in the same row, and the only one that distinguishes *there is nothing* from *there is
  something and you are not looking at it*. GitHub matches it on legibility and loses on the empty
  state; Obsidian wins the single best idea in the flow (zero results is a create row) and pays for it
  in honesty; VS Code is last, on the strength of one inert sentence.
- **B2 Assemble — VS Code**, on the back of Workspace Trust, which is the best consequence disclosure
  in the entire benchmark. npm has the best failure line; Figma has the best modelling and the worst
  display of it.
- **B3 Check — `terraform`**, with **VS Code's Problems panel** level on everything except the
  summary line. Vercel remains the reference for the *process*, GitHub Actions for the *verdict
  vocabulary*, and GitHub Actions is also the anti-reference for copy.
- **B4 Produce — nobody, and that is a finding.** The highest cell is a 4. Handover is the flow where
  the industry is weakest: Ruler overwrites without warning, `create-next-app` ends on the word
  *Success!* and lists nothing, Vercel's irreversible step is invisible from outside, and Figma's
  dialog disables its own primary action. **Our wow moment is aimed at the least-well-served flow of
  the four.**

---

## B1 — Find one thing in a large personal collection

Our screen: **Library**.

### Linear — ⌘K, filters, empty states

[`flows/02-library-browse-filter-search/NOTES-linear.md`](flows/02-library-browse-filter-search/NOTES-linear.md) ·
[`flows/08-empty-state-and-cold-start/NOTES-linear.md`](flows/08-empty-state-and-cold-start/NOTES-linear.md)

- **C1 = 5.** A filter is a sentence with its own ✕, the state is in the URL, the keyboard-hint bar
  recomputes from what is currently possible, and a filter matching nothing prints **"4 issues hidden
  by filters"** — the anchor-5 case: it changes what you do next.
- **C2 = —, no instance.** Nothing in finding is irreversible; `Save` a view is trivially undone.
- **C3 = 4.** *"No results found · Go to advanced search"*, with the query quoted back into the
  results heading. Not 5: when a filter empties the list it says how many are hidden but never
  **which filter did it**.
- **C4 = 5.** The row that reports the failure is the row you press to escape it; `Clear Filters ✕`
  sits inside the empty state beside the count.
- **C5 = 5.** The toolbar disappears over an empty list; the hint bar shrinks to what still applies.
  *(Second look: the un-deduped duplicate chip tempted a 4. Rejected — a display bug, not an inert
  control.)*

### GitHub code search

[`benchmark/NOTES-github-code-search.md`](benchmark/NOTES-github-code-search.md)

- **C1 = 5.** `10 files (324 ms) in [repo ✕]` — count, cost and scope in one line, the scope as a
  removable chip. The left rail counts **every other result type for the same query, including the
  zeros**, so you can see where the answer is not. Facets are computed from the result set, not from a
  fixed taxonomy. Per-file match counts, and truncation that states its own size: *Show 3 more
  matches*.
- **C2 = —, no instance.**
- **C3 = 3.** *"Your search did not match any code"* over six collapsible tips, one of them literally
  *"Why wasn't my code found?"*. It teaches, but never names which clause killed the result.
- **C4 = 3.** The remedies are generic and collapsed, and the one control that would widen this search
  — the ✕ on the scope chip — is not among them.
- **C5 = 4.** On zero results it keeps the whole rail, and **that rail is the answer**: every count is
  zero, so the term is absent from the entire repository and not just its code. The deduction is the
  half-viewport illustration and six accordions where one chip would do.

### Obsidian quick switcher

[`benchmark/NOTES-obsidian.md`](benchmark/NOTES-obsidian.md)

- **C1 = 4.** Rows are full paths with **every matched character bolded across the path**, so the
  ranking explains itself and the tail is visibly the tail. The search pane adds `6 results`,
  per-file match counts and a visible operator. Not 5: the switcher itself has no count, no scope,
  no filter — at 27 notes it is exemplary and about scale it is mute.
- **C2 = 2.** `Enter to create` is offered with no statement of where the note will be written. The
  stake is low; the information is nonetheless absent.
- **C3 = 2.** There is no failure message at all: zero matches renders as a create row containing
  your typo. The product knows how to say it — the search pane prints `0 results · No matches found.`
  — and chooses not to here. *(Second look: 1 was argued, on the grounds that a plausible-looking row
  where there is no match implies a match. Held at 2 because the row does say `Enter to create`.)*
- **C4 = 5.** The strongest recovery in the benchmark. The dead end is designed out: the thing you
  could not find is one keystroke from existing.
- **C5 = 4.** The empty tab is three actions with their shortcuts inline; the hint bar lists exactly
  the modifiers that apply — except in the no-match state, where it still advertises `↵ to open` with
  nothing to open.

### VS Code — palette and Extensions search

[`benchmark/NOTES-vscode.md`](benchmark/NOTES-vscode.md)

- **C1 = 4.** The mode is a visible prefix character in the input (`>` commands, `@` symbols, `:` a
  line), the view title states the active filter (*Extensions: Marketplace*, *Extensions: Builtin*),
  and **matched substrings are bolded inside each row**. Not 5: opened cold it is the entire command
  list, alphabetically, from `Accounts: Manage Accounts` — no grouping, no counts anywhere.
- **C2 = —, no instance** in this flow. (Its Workspace Trust screen is scored under B2, where it
  belongs.)
- **C3 = 2.** *"No matching commands"*. The query is not quoted back, nothing is offered, nothing can
  be pressed. The weakest dead end of the four candidates.
- **C4 = 2.** Nothing offered from an empty result, in either the palette or the marketplace search.
- **C5 = 4.** Nothing inert on the surfaces themselves; the clear button appears only with text in
  the box.

**The marketplace card, recorded here because it settles a decision elsewhere.** Cards carry download
count, star rating and a verified publisher — and two rows apart the ratings read `5` on a 4K-download
extension and `1` on a 33K one. The signal is strong at the head and noise in the tail, and a personal
library is all tail. That is the concrete argument behind CLAUDE.md §5.

---

## B2 — Assemble a set from that collection, with constraints

Our screen: **Project Builder**.

### VS Code — per-workspace extensions, recommendations, Workspace Trust

[`benchmark/NOTES-vscode.md`](benchmark/NOTES-vscode.md)

- **C1 = 5.** `@recommended` splits into **Workspace Recommendations (3)** and **Other
  Recommendations (4)**, each counted in its header, with a pencil beside the first that opens
  `.vscode/extensions.json` — the file the list is read from. The set is authored as text and rendered
  as a list, and the UI says so. The detail pane states constraints in words: *"bundled with Visual
  Studio Code. It can be disabled but not uninstalled."*
- **C2 = 5.** **Workspace Trust**: two columns, *In a Trusted Folder* against *In Restricted Mode*,
  the current one outlined, four ✓/✕ lines each — and two of them counted **and hyperlinked**:
  *"95 workspace settings are not applied"*, *"10 extensions are disabled or have limited
  functionality"*. It beats Figma's *423 instances* on the axis Figma leaves open: the number is a
  link to the list. The button carries its shortcut inside it.
- **C3 = —, not observed.** No failure was produced in assembly.
- **C4 = 4.** After trusting, the heading, the outline and the button all flip in place: the same
  control, same position, now reading **`Don't Trust`**. Enable/Disable are offered at two named
  granularities — `Disable` and `Disable (Workspace)`. Not 5: per-extension only, no bulk, and the
  way back lives in a context menu you must open per item.
- **C5 = 3.** The context menu greys `Enable`, `Enable (Workspace)`, `Uninstall` and `Install Specific
  Version…` rather than hiding them, and the recommendation notification names **publishers**
  (*"from Prettier, Microsoft and others"*) where the file it just read names three extensions by id
  — a disclosure at the wrong grain.

### `npm install` — a declared set resolved against constraints

[`benchmark/npm-eresolve.md`](benchmark/npm-eresolve.md)

- **C1 = 3.** The resolved set is knowable — `npm ls`, the lockfile — but only by running something
  and reading a wall of text.
- **C2 = 4.** The unreviewed `postinstall` is not run and is named precisely: package, version, the
  hook itself, and two commands. Not 5: printed as `npm warn`, visually identical to a funding notice
  three lines above.
- **C3 = 5.** `ERESOLVE` answers all four questions a conflict message owes — required
  (`peer react@"^18.0.0 || ^19.0.0"`), found (`react@17.0.2`), who required it, and **who asked for
  what was found** (`from the root project`), which is our `addedBy: manual | dependency`. Then both
  escape hatches with the cost in the same sentence: *"to accept an incorrect (and potentially broken)
  dependency resolution."*
- **C4 = 4.** `--force` and `--legacy-peer-deps` in the failure itself, priced. Not 5: *Fix the
  upstream dependency conflict* is homework — npm knows the range and the registry and never suggests
  the version that satisfies both.
- **C5 = 4.** Twelve lines on screen, the full trace on disk — behind an absolute cache path nobody
  will open, next to *"146 packages are looking for funding"* at equal weight.

### Figma — instances, overrides, library updates

[`flows/05-linked-vs-detached/NOTES.md`](flows/05-linked-vs-detached/NOTES.md)

- **C1 = 2.** Figma says *"this is an instance"* three times — glyph, colour, and a sentence naming
  the library — and nothing at all about *"this instance no longer matches its main"*. A modified
  instance is drawn identically to a clean one everywhere except a context menu you must open on an
  object you must first select. *(Second look moved this from 3 to 2: three loud channels announcing
  the link, and silence about the drift, reads as a claim of cleanliness. Short of 1 only because
  Figma never asserts "unmodified" in words.)*
- **C2 = 4.** The library-updates modal states **423 instances** before you accept, grouped by publish
  event. Not 5: the counts appear only with *"Show updates for all pages"* on, and it is off by
  default.
- **C3 = —, not observed.**
- **C4 = 3.** Two halves pointing opposite ways. While linked, recovery is outstanding — `Reset
  instance` and `Reset fill`, property-granular and self-labelling, beside `Detach`. Across the detach
  boundary there is nothing: the origin is erased.
- **C5 = 5.** The reset rows are **absent** on a clean instance, not greyed.

---

## B3 — Check a set and report what is wrong

Our screen: **the validation pass**.

### `terraform` — a successful plan, and validate against a broken config

[`flows/04-validation-check-results/terraform-plan-output.md`](flows/04-validation-check-results/terraform-plan-output.md) ·
[`benchmark/terraform-validate-errors.md`](benchmark/terraform-validate-errors.md)

- **C1 = 5.** One summary line that is a count — `Plan: 2 to add, 0 to change, 0 to destroy`. Every
  resource named before it is described, a symbol per operation in the left margin, and `(known after
  apply)` on every value it cannot compute: it never guesses and never hides the gap.
- **C2 = 5.** The artefact exists for no other reason, and then undercuts its own authority on
  purpose — *"Terraform can't guarantee to take exactly these actions"* unless you saved the plan.
- **C3 = 4.** `Reference to undeclared resource` names the item, the file and line, **echoes the
  offending source line**, and states the rule in words. The duplicate names **both** sides with a
  column range, `main.tf:10,1-33` — the sentence CLAUDE.md §6 asks for on a merged MCP config.
  *(Second look moved this from 5 to 4.)* Two deductions, both ours to avoid: one defect produced
  **four** diagnostics differing only in which permutation of a mutually exclusive set they quote; and
  a parse-level error silently cancels the checks behind it, so fixing one problem appears to reveal
  new ones.
- **C4 = 4.** Recovery is structural and total — a plan mutates nothing. Not 5: when the plan is
  wrong nothing is offered in place; you leave for the editor.
- **C5 = 5.** No spinner, no progress theatre; text that appears when ready and reads correctly
  frozen. The argument for keeping our "animated sweep" subordinate to a result that survives being
  paused.

### VS Code Problems panel

[`benchmark/NOTES-vscode.md`](benchmark/NOTES-vscode.md)

- **C1 = 5.** The same count at four altitudes that agree: status bar `⊗4 ⚠2`, panel badge `6`,
  per-file badge `3`, and the number on the editor tab. Severity glyphs distinct, errors sorted above
  warnings, each file a collapsible group.
- **C2 = —, no instance.**
- **C3 = 4.** Every row is message + **rule code** (`ts(2353)`, `json(520)`) + `[Ln 14, Col 66]`, with
  the underlying cause nested one level down. Not 5: our exact case — `postgres` declared twice in
  `.mcp.json` — produces **two independent warnings** at `Ln 3` and `Ln 7` that never mention each
  other and never say which wins. Terraform says it in one message.
- **C4 = 4.** A lightbulb replaces the severity glyph on rows where a Quick Fix exists — the remedy on
  the problem itself, and its absence elsewhere is information too.
- **C5 = 5.** Filtering to nothing puts **`Showing 0 of 6` inside the input** and one line under it:
  *"No results found with provided filter criteria. Clear Filters."* The count of what is hidden and
  the remedy as a link — Linear's decision, placed better.

### Vercel build log

[`flows/04-validation-check-results/NOTES-vercel.md`](flows/04-validation-check-results/NOTES-vercel.md)

- **C1 = 5.** A deployment is a stack of collapsed stages, each with its own verdict and duration; a
  stage that did not run gets a clock, not a failure. `66 lines` before you read, `Find in logs`, and
  a timestamp hover giving **relative to start** and **relative to previous** — how you find the step
  that hung without arithmetic. Structurally this is our validation pass, and it is the reference.
- **C2 = —, no instance** in the surfaces captured. · **C3 = —, not observed:** every deployment in
  the account succeeded. · **C4 = —, not observed:** Instant Rollback exists; performing one is out of
  bounds.
- **C5 = 4.** Nothing inert on the log page. Not 5 because the same product one screen away is this
  research's standing counter-example — see B4.

### GitHub Actions run

[`flows/04-validation-check-results/NOTES-github-actions.md`](flows/04-validation-check-results/NOTES-github-actions.md)

- **C1 = 5.** Four verdicts, four glyphs, colour redundant; **skipped** and **cancelled** each
  distinct from failure; a mixed commit gets a partially-filled ring rather than being flattened to
  its worst state; and a failed job keeps its duration — *failed 4 hours ago in 14m 6s*.
- **C2 = —, no instance.**
- **C3 = 1.** Fourteen of seventeen annotations read, in full, `Process completed with exit code 1.`
  The slot is prominent, counted in the header as *"11 errors and 6 warnings"*, and empty. A count
  promises eleven pieces of information: the interface implies something untrue. The three exceptions
  show what a 4 looks like — `non-retryable`, `exceeded the maximum execution time of 30m0s`, and
  cause and consequence filed as two annotations.
- **C4 = 2.** Nothing offered next to a failure; the one piece of recovery guidance in the run arrives
  by luck of which subsystem emitted it.
- **C5 = 3.** The digest is the same component at two altitudes, collapsed by default. But on a fully
  public repository the log bodies sit behind *"Sign in to view logs"* — the thing you came for is
  missing, and a control is shown over it.

---

## B4 — Produce an artefact and hand it over to another machine

Our screen: **Result / Export**. **The weakest flow in the benchmark; the highest cell is a 4.**

### Vercel deploy

- **C1 = 5.** Duration in the deployments list before you open anything — what makes a list scannable
  for the anomaly. `Assigning Custom Domains ✓` states the handover as a stage like any other.
- **C2 = —, unobservable.** Promoting to production is the irreversible step and we will not perform
  one in the owner's account. · **C3 = —, not observed.** · **C4 = —, not observed.**
- **C5 = 3.** The environment-variables empty state keeps a search box, four filter dropdowns and a
  sort control on screen, all filtering nothing — on the screen our `needsEnv` work copies most from.

### `create-next-app`

[`benchmark/create-next-app-output.md`](benchmark/create-next-app-output.md)

- **C1 = 4.** The manifest is printed before the work, split by role, by name, before a single package
  is fetched; side effects are stated as completed facts, including `Initialized a git repository.`
  Not 5: it ends on `Success!` and nothing else — no count of files, no tree, and no mention that it
  wrote a `CLAUDE.md` and an `AGENTS.md` into your repository.
- **C2 = 4.** Inherited from npm's `allow-scripts` gate, credited honestly.
- **C3 = —, not observed.**
- **C4 = 2.** Nothing offered for undoing a scaffold. The `git init` is an accidental recovery, never
  presented as one.
- **C5 = 3.** The signal is buried in 358 packages of install noise, a deprecation warning scrolls
  past and is never restated, and the one dangerous line sits at the same weight as a funding notice.

### Figma export dialog

[`benchmark/NOTES-figma-export.md`](benchmark/NOTES-figma-export.md)

- **C1 = 4.** `0 of 0 selected` states the state exactly, in the same grammar as VS Code's `Showing 0
  of 6`. Not 5: it never says what *would* be exportable.
- **C2 = —, not observed.** Seeing the disclosure for a real export would mean selecting layers in the
  owner's file; out of bounds.
- **C3 = 4.** *"No selected layers have export settings. Click + in the export section of the
  properties panel to add one."* — the condition and the location of the remedy, in one sentence.
- **C4 = 3.** The remedy is described but not offered: there is no `+` in this dialog. You must leave
  it and find the panel.
- **C5 = 3.** A **disabled primary action** sits on screen. It is tolerable here for three reasons we
  do not have — the blocker is one action away and named, the condition is a property of this
  second's selection rather than of the document, and re-exporting is free. Our Export has none of
  the three, which is why CLAUDE.md §6 stands.

### Ruler — one source, six agent targets

[`flows/06-export-and-target-adaptation/ruler-per-agent-output.md`](flows/06-export-and-target-adaptation/ruler-per-agent-output.md)

- **C1 = 3.** Six log lines for six targets and a fenced managed block in `.gitignore` naming what was
  generated — but the mapping from target to artefact is knowable only by listing the directory
  afterwards, and two announced targets produce no file of their own.
- **C2 = 2.** It overwrites files in your repository and says nothing in advance about which. The
  `.bak` is a remedy, not a disclosure.
- **C3 = —, not observed.**
- **C4 = 4.** A `.bak` beside every overwritten file **and** a named `START/END` block so a re-run
  finds and replaces exactly what it wrote. Not 5: nothing tells you the backups exist.
- **C5 = 4.** Six lines, one summary, no theatre.

---

## What the rubric says

This is what stage 5 spends.

1. **A failure line is only as good as the altitude that emits it.** The 5-grade messages —
   npm's `ERESOLVE`, Port's `where "Open Critical Vulnerabilities" = 0 · Value: 1` — are written where
   the *requirement* is known. The 1-grade one, `Process completed with exit code 1`, is written by a
   process that only knows it stopped. VS Code and Terraform sit at 4 by carrying a **rule code** and
   a **location** on every row. This is an architecture decision in our validator, not a copy
   decision: **the check that knows the rule must be the thing that writes the sentence.**

2. **One defect is one Problem, and a check that could not run must say so.** Terraform reports every
   diagnostic in one pass where npm stops at the first — ours should be Terraform's. But it emits one
   message per internal rule that fired (four messages, one defect), and VS Code reports a duplicate
   key as two unjoined rows. **Count problems the way the user counts them.** And where Terraform's
   parse failure silently cancels the later stages, our **Skipped** severity (CLAUDE.md §6) covers
   both *nothing to check* and *blocked by an earlier stage*, so the stage list never quietly shrinks.

3. **C2 splits the field, and building the way back is what gets built instead.** Terraform, VS Code
   and Figma disclose before the act and score 4–5. Ruler, `create-next-app` and Vercel disclose after
   or not at all — and the good behaviour they do have (`.bak` files, `git init`) is *recovery wearing
   consequence disclosure's clothes*. Saying what will happen is more expensive than making it
   undoable, so it is rarer. Our unclean-export confirmation is squarely in the expensive half, which
   is the point of it.

4. **The best disclosure in the benchmark makes its number a link.** VS Code's Workspace Trust prints
   *"95 workspace settings are not applied"* and *"10 extensions are disabled"* as hyperlinks, beside
   a column showing what the other state would give you. Figma's *423 instances* is the same idea one
   step behind — a count you cannot open, behind a toggle that is off by default. **Our export
   confirmation should name the count and let the user open it.**

5. **`N of M` is the idiom the whole industry converged on.** Linear: *4 issues hidden by filters*.
   VS Code: *Showing 0 of 6*, inside the input. Figma: *0 of 0 selected*. GitHub: *10 files (324 ms)
   in `repo ✕`*, plus a rail counting the doors you did not open. Four unrelated products, one
   grammar: **the number you can act on, next to the control that produced it.** Our Library filtered
   to zero, our selection, our export set — all three want this and none of them wants the word
   "none".

6. **The dead end is where the four find-flows differ most, and the ranking is not the obvious one.**
   Obsidian removes the failure entirely (zero results *is* the create row) and thereby cannot tell a
   typo from an absence. Linear reports the failure and makes the report the remedy. GitHub teaches
   with six tips and hides the one control that would help. VS Code writes *"No matching commands"*
   and stops. **Our empty Library search should do both halves Obsidian splits: offer to create the
   item, and still say that nothing matched.**

7. **The economy rule has a genre exception, and the earlier tally was wrong.** This document
   previously recorded *"an action that cannot act is not shown"* as settled four to one. It is
   settled **for primary surfaces** — Linear suppresses a toolbar and trims a hint bar, Figma hides a
   reset with nothing to reset, GitHub's zero-count rail earns its place because the zeros are the
   answer. It is **reversed in context menus**, where VS Code greys four inapplicable items rather
   than reordering the list under the reader's hand, and position is worth more than brevity. Vercel's
   four dropdowns over an empty list remain simply wrong, and Figma's disabled Export button is the
   in-between case: inert, but sign-posted by the sentence beside it. The rule we carry forward is
   the split, not the tally.

8. **Handover is the industry's weakest flow, and it is ours to win.** No B4 cell scores above 4. The
   two vendors who write agent files — Ruler and `create-next-app` — independently arrived at the same
   two mechanics (copy the content in a named fenced block, or point at the canonical file), which
   collapses our four export targets into two mechanics plus a naming convention. Neither states what
   it will overwrite. **The archive-in-thirty-seconds moment is aimed at the flow where the
   competition is weakest, and the specific gap is disclosure before the write.**

---

## Nothing is left to capture

Every cell is scored, and the two dropped candidates are recorded above with their reasons. The five
categories carry into stage 5 unchanged, which is what the plan's *done when* asks for.

---

# Finalisation — what this rubric measures, and what it does not

Added after stage 5, when the rubric had been spent once and its shape was visible. It belongs here
rather than in [`patterns.md`](patterns.md), because it is a fact about the instrument.

## The rubric grades craft, not weight

The five categories were lifted from stages 1–3, and those stages surveyed **products**. So every
score in this document answers *did this interface tell me the thing* — and none of them answers
*does anyone bleed here*. A cell scoring 5 means a vendor solved a problem beautifully. It does not
mean the problem mattered.

Read the four flows against [`user-pain.md`](user-pain.md) instead, and the weights come out uneven:

| | Flow | What the pain evidence says |
|---|---|---|
| **B1** | Find | An issue tracker is **structurally blind** here — nobody files *I cannot find what I wrote in March*. No evidence of pain, and none of its absence either. |
| **B2** | Assemble | Same blindness, plus finding 4: **nobody is asking for a composition layer**, in a 6,677-issue tracker belonging to a product that shipped one. |
| **B3** | Check | Where our thesis is actually sighted — the duplicate `server-postgres` key, *"the chat always chooses the first one specified"*, 13 reactions — and where env and secrets sit, which rank near the top of **both** trackers. |
| **B4** | Produce | Where the **loudest pain in the ecosystem** lives: 182 reactions on *MCP Servers Don't Work with NVM*, and a top-of-tracker made of PATH, node versions, platform paths and processes dying at startup. The archive lands on a machine and does not run. |

**So the value is concentrated in B3 and B4, and the craft is concentrated in B1 and B2.** Linear,
GitHub and Obsidian are exemplary at a flow nobody files issues about; the flow people shout about is
the one where no candidate scored above 4.

## The consequence for how a rubric score may be used

Stage 5 compared five shapes of *assemble → check → export*. Four of the five differ from each other
mainly in **assembly** — P1, P2, P3 and P4 are four ways to put items into a set — and barely at all
in check-and-export.

> **The variants differ most where the pain is least.**

A category score is therefore **not sufficient to choose a shape**. It has to be read next to which
third of the flow the shape owns. P5 scored 5 on four categories *and* owns the two thirds that carry
the pain; P2 won its half on economy and cold start, which are real and cheap. That is a different
sentence from *P2 and P5 both scored well*, and it is the sentence stage 5's scores alone could not
produce.

## The gap neither instrument covers

Every cell in this matrix scores what a product says **about its own state**. Not one scores what a
product says about **the machine its artefact lands on** — and no candidate offered anything to
score, because none of them has such a surface.

That is the single square where our weakest-flow finding and the ecosystem's loudest pain point at
the same thing. It is **Q2** in the register, it was raised by stage 3, and stage 4 could only
confirm that nobody solves it. Whatever the final shape is, the answer lives in the last stages of
the run and in what `SETUP.md` is allowed to become.
