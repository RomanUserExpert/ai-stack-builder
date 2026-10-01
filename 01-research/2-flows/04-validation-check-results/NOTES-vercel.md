# Vercel build log — the closest thing to our validation pass

From the owner's signed-in Vercel (`portfolio-react`), captured 2026-08-31. Read-only; no
deployment was triggered or rolled back.

Companion to [`terraform-plan-output.md`](terraform-plan-output.md) in this folder. Terraform shows
what a *result* should read like; Vercel shows what a *process* should read like.

## A deployment is a list of stages, each with its own status

`vercel-deployment-stages.jpg`

The deployment page is a stack of collapsed sections, each with a status glyph on the right:

| Section | Right-hand side |
|---|---|
| Deployment Settings | `2 Recommendations` badge |
| **Build Logs** | `32s` ✓ |
| Deployment Summary | `Resources` button, ✓ |
| Deployment Checks | clock glyph — not run |
| Assigning Custom Domains | ✓ |

**This is our validation pass, structurally.** Dependency walk, cycle check, conflicts, duplicate
commands, target-path collisions, missing env — six stages, each collapsed, each carrying its own
verdict and its own duration, all expandable. Nothing is a spinner; a stage that did not run gets a
distinct neutral glyph rather than a failure. Note also that "2 Recommendations" is a *third*
severity sitting beside pass and skip — advice that blocks nothing.

## The log itself

`vercel-build-logs-collapsed.jpg`, `vercel-build-log-timestamp-tooltip.jpg`

- The header states the size before you read: **"66 lines"**, with a copy-all button and
  **"Find in logs  Ctrl F"**. You are told how much there is and given a way to search it.
- Every line carries a millisecond timestamp in a dimmed gutter.
- **Hovering a timestamp opens a small table** — and this is the detail worth stealing outright:

  | | |
  |---|---|
  | Europe/Kiev | Jul 23, 2026, 5:13:35.072 PM |
  | UTC | Jul 23, 2026, 2:13:35.072 PM |
  | Relative | about 1 month ago |
  | **Relative to start** | **25s** |
  | **Relative to previous** | **0ms** |

  Absolute time for the record, relative time for the human, and two *derived* numbers — how far
  into the run this line happened, and how long since the previous line. The second one is how you
  spot the step that hung, without doing arithmetic.

- The log renders structure as an **ASCII tree with symbols**: `├ ○ /icon.svg`, `├ ● /projects/[slug]`,
  `│ ├ /projects/risklayer`, `└ [+9 more paths]`. Two glyphs distinguish kinds of route, and long
  lists truncate with a counted marker rather than scrolling forever. Our Result screen shows the
  file tree of the future archive; this is a working precedent for rendering one inside a running
  process, including how to cut it short.

## The runs list

`vercel-deployments-list.jpg`

One row per deployment: status dot plus `Ready`, **duration** (`32s`), an environment badge
(Production filled, Preview outlined), commit hash, branch, date. Filter chips sit above —
Author, Environment, Status — as removable chips rather than a filter panel.

Duration in the list, before you open anything, is what makes the list scannable for the anomaly.

## What we now have for flow 04

Terraform `plan` for the result, Vercel for the process and stage structure, GitHub Actions as the
open substitute. **The only thing still missing is a failure** — every deployment in this account
succeeded, so the failure-state copy is still uncaptured. GitHub Actions on a public repository is
the place to get it without touching anything of the owner's.
