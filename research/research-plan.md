# Research plan

Status of the research phase. Updated 2026-09-01.

## Documents

| File | What it holds |
|---|---|
| [`competitors.md`](competitors.md) | 15 companies in three groups — hard, soft, aspirational. Why each is there, what to take from it, a verified link per entry. |
| [`comparison.md`](comparison.md) | All 15 compared on audience, product base, key mechanism, trust, monetisation. Three market patterns, three differences we can hold, three open questions for the PM. |
| [`screens-index.md`](screens-index.md) | 38 product captures in [`screens/`](screens/), sorted group / competitor. Sign-in walls labelled. |
| [`continue-postmortem.md`](continue-postmortem.md) | The closest competitor read from source: its block model, the uses/with/override composition primitive, its identity and secret schemes, and the three things its resolver never did. Feeds open question 1. |
| [`flows/README.md`](flows/README.md) | The twelve flows: what each is for, what is collected, what is missing, what access it needs. |

## Flows

**10 of 12 closed.** Flow 01 is declined (login-walled, and its other gap is out of MVP scope).
Flow 10 is **handed to the design-system phase** rather than left open — it is the one flow about
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
| 10 | Dark design language | → | [Material for the next phase](flows/10-dark-design-language/NOTES-linear.md) — Geist, Linear's dark theme at close range, Raycast's tokens |
| 11 | Copy: errors, warnings, refusals | ● | [Conflict copy](flows/11-copy-and-error-language/dependency-conflict-copy.md) · [CI failure copy](flows/11-copy-and-error-language/ci-failure-copy.md) |
| 12 | Visibility and portfolio | ● | [NOTES](flows/12-visibility-and-portfolio/NOTES.md) |

## What is left

**Nothing to collect.** Every remaining item is declined, and the reasoning is recorded rather than
deferred.

| What | For | Why it is closed |
|---|---|---|
| Raycast desktop app | 10 | **Declined on behavioural grounds.** Its one UX idea is the launcher instead of a screen; the question it would answer — *is the Library a screen or a palette?* — is already answered by Linear's `Ctrl K` and Tessl's ⌘K. Tone, not mechanism, for a global hotkey and a sign-in. |
| Linear's density under load | 10 | Unobtainable — the workspace granted is new. `play.grafana.org` and `sandbox.sentry.io` stay available if the design-system phase wants real rows. |
| Agentman skill page and permission tiers | 01 | Behind login. Lesson legible from their marketing; three open skill catalogs already captured. |
| A version / history surface | 01 | Out of MVP scope per CLAUDE.md §9 — `version` is reserved and nothing reads it. |
| Cross-file component usage count | 05 | Figma library analytics, paid tier. The in-file count is captured; the cross-container number — the shape of our *"used in 3 projects"* — is not. |
| ~~A failing GitHub Actions run~~ | 04, 11 | **Done 2026-09-01.** Log *bodies* need a sign-in even on a public repo; structure, glyphs and timings do not. |
| ~~A scorecard in a blocking state~~ | 04 | **Answered 2026-09-01 — there isn't one.** Port gates a level rather than forbidding an action. |
| ~~A Linear workspace~~ | 02, 08 | **Done 2026-09-01.** Closed both flows outright. |
| ~~An instance linked but locally modified~~ | 05 | **Done 2026-09-01.** The state exists in the model and is drawn nowhere. |
| Packmind product | 06 | Sales-gated. Substituted by Ruler, run locally. |
| Continue Hub | 06, and question 1 | Switched off. **Read from source instead** — see [`continue-postmortem.md`](continue-postmortem.md). |
| Mobbin | reference | 403s without a subscription. Not worth buying; we capture products directly. |

## The four findings the design system has to answer to

All four landed on 2026-09-01, and each changes a decision that would otherwise be made by default.

1. **The failure line.** Port writes `where "Open Critical Vulnerabilities" = 0 · Value: 1` — the
   condition required and the value found. GitHub writes `Process completed with exit code 1`, and a
   sweep of five major repositories found it writes nothing else. The difference is not polish; it is
   whether the message is emitted at the altitude that knows what was required. Every row our
   validation pass produces takes Port's form.

2. **Blocking may be the wrong primitive.** Our spec has hard-block and soft-warn, a binary. Port has
   neither: a failed rule stops an entity climbing `Basic → Low → Good → Great` and forbids nothing.
   That is a third shape for the validation result, and it needs deciding before the design system
   fixes the vocabulary — because a grade and a verdict do not look alike.

3. **Cold start is a product decision, not a demo problem.** CLAUDE.md §11 plans ~30 realistic items
   *for mockups*. Linear ships a new workspace with four **real** issues — editable, completable,
   deletable — so the product is never empty and the model is learned by holding four instances of it.
   Our equivalent: a small starter set of genuine Items in a genuine Project on first launch, so the
   validation pass runs before the user types anything. That puts the wow moment on first launch
   instead of after an evening of data entry.

4. **The drift indicator is a display problem, not a modelling one.** Figma tracks overrides precisely
   enough to offer `Reset fill` by name, then shows a modified instance as pixel-identical to a clean
   one everywhere except a context menu. Our state 7 — *detached, locally modified* — is the state
   CLAUDE.md §7 flags as easiest to forget, and this is exactly how it gets forgotten. The diff is
   already computed; putting it on the card costs nothing. Revert needs two granularities, whole item
   and single field, with Reset kept next to Detach as the two halves of one axis.

## Definition of done

**Collection is finished.** Ten flows are ●, flow 01 is declined, and flow 10 is handed to the next
phase rather than left open. Nothing outstanding requires access we do not have, and every gap that
remains is closed by a recorded decision rather than deferred.

**What the phase was for, and what it deliberately was not.** These twelve flows studied **behaviour**
— how a check reports a failure, how a filter says it is hiding things, how a product answers its own
emptiness, how a modified object announces that it has drifted. Visual direction is postponed by
CLAUDE.md §12 and belongs to the design system, which is the next stage. Flow 10 collected reference
for that stage; it was never a research question.

**What now gates the design system is answers, not material.**
[`comparison.md`](comparison.md)'s **three open questions for the PM** — what our answer is to
Continue Hub dying, which trust signal we ship without a network or an eval harness, and whether a
personal library has a business. They decide what `visibility`, `Workspace` and `version` have to
mean. Beside them sits the **block-or-grade** question in finding 2, which is ours to settle rather
than the market's.

Next stage after sign-off: design system. Not started, per CLAUDE.md section 1.
