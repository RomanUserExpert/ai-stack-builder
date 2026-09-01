# Research plan

Status of the research phase. Updated 2026-09-01.

## Documents

| File | What it holds |
|---|---|
| [`competitors.md`](competitors.md) | 15 companies in three groups — hard, soft, aspirational. Why each is there, what to take from it, a verified link per entry. |
| [`comparison.md`](comparison.md) | All 15 compared on audience, product base, key mechanism, trust, monetisation. Three market patterns, three differences we can hold, three open questions for the PM. |
| [`screens-index.md`](screens-index.md) | 38 product captures in [`screens/`](screens/), sorted group / competitor. Sign-in walls labelled. |
| [`flows/README.md`](flows/README.md) | The twelve flows: what each is for, what is collected, what is missing, what access it needs. |

## Flows

**11 of 12 closed.**

| # | Flow | Status | Notes |
|---|---|---|---|
| 01 | Item detail and trust | ◐ | Held open only by Agentman's login-walled skill page |
| 02 | Library browse, filter, search | ● | [Linear](flows/02-library-browse-filter-search/NOTES-linear.md) |
| 03 | Relations without a canvas | ● | — |
| 04 | Validation: pass, warn, block | ● | [Terraform](flows/04-validation-check-results/terraform-plan-output.md) · [Vercel](flows/04-validation-check-results/NOTES-vercel.md) · [GitHub Actions](flows/04-validation-check-results/NOTES-github-actions.md) · [Port](flows/04-validation-check-results/NOTES-port.md) |
| 05 | Linked vs detached, blast radius | ● | [NOTES](flows/05-linked-vs-detached/NOTES.md) — all three instance states captured |
| 06 | Export and target adaptation | ● | [Ruler output](flows/06-export-and-target-adaptation/ruler-per-agent-output.md) |
| 07 | Env variables and secrets | ● | [NOTES](flows/07-env-and-secrets/NOTES.md) |
| 08 | Empty state and cold start | ● | [Linear](flows/08-empty-state-and-cold-start/NOTES-linear.md) |
| 09 | Duplicate and fork | ● | [NOTES](flows/09-duplicate-and-fork/NOTES.md) |
| 10 | Dark design language | ◐ | [Linear](flows/10-dark-design-language/NOTES-linear.md) — palette captured; density judged unobtainable |
| 11 | Copy: errors, warnings, refusals | ● | [Conflict copy](flows/11-copy-and-error-language/dependency-conflict-copy.md) · [CI failure copy](flows/11-copy-and-error-language/ci-failure-copy.md) |
| 12 | Visibility and portfolio | ● | [NOTES](flows/12-visibility-and-portfolio/NOTES.md) |

## What is left

### Needs no access — nothing left

The last item, an instance **linked but locally modified**, was supplied by the owner on 2026-09-01.
Flow 05 is fully closed.

### Needs a decision, not access

| What | For | Note |
|---|---|---|
| Raycast desktop app | 10 | Installable here (`winget install raycast`), but wants a sign-in and takes a global hotkey. A deliberate step, not part of a sweep. |

### Declined, out of reach, or answered

| What | For | Why |
|---|---|---|
| ~~A failing GitHub Actions run~~ | 04, 11 | **Done 2026-09-01.** 102 jobs, 7 failed, 4 skipped, 1 cancelled, with its annotations digest and PR Checks tree. Log *bodies* need a sign-in even on a public repo; structure, glyphs and timings do not. |
| ~~A scorecard in a blocking state~~ | 04 | **Answered 2026-09-01, and the answer is that there isn't one.** Port does not block — a failed rule gates a cumulative level ladder rather than forbidding an action. |
| ~~A Linear workspace~~ | 02, 08, 10 | **Done 2026-09-01.** Closed flows 02 and 08 outright. |
| Linear's density under load | 10 | **Not pursued.** The workspace granted is new — four issues — so density is not there to capture at any access level. `play.grafana.org` and `sandbox.sentry.io` remain open substitutes if P3 ever becomes P1. |
| Agentman skill page and permission tiers | 01 | Behind login. Lesson is legible from their marketing; three open skill catalogs already captured. |
| Cross-file component usage count | 05 | Figma library analytics, paid tier. The in-file instance count is captured; the cross-container number is not, and it is the shape of our "used in 3 projects". |
| Packmind product, Continue Hub | 06 | Sales-gated and switched off. Both substituted — Ruler and the Continue repository. |
| ~~An instance linked but locally modified~~ | 05 | **Done 2026-09-01.** The state exists in the model and is drawn nowhere — the only evidence is two rows appearing in a context menu. |
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

**Collection is finished.** Eleven flows are ●. Flow 01 is held open only by Agentman's login-walled
skill page (declined), and flow 10 only by the Raycast install, which is a decision rather than an
access problem. Nothing outstanding requires access we do not have.

What gates the design system now is answers, not material: [`comparison.md`](comparison.md)'s **three
open questions for the PM** — what our answer is to Continue Hub dying, which trust signal we ship
without a network or an eval harness, and whether a personal library has a business. They decide what
`visibility`, `Workspace` and `version` have to mean. Beside them sits the **block-or-grade** question
in finding 2, which is ours to settle rather than the market's.

Next stage after sign-off: design system. Not started, per CLAUDE.md section 1.
