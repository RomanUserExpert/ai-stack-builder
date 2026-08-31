# Research plan

Status of the research phase. Updated 2026-08-31.

## Documents

| File | What it holds |
|---|---|
| [`competitors.md`](competitors.md) | 15 companies in three groups — hard, soft, aspirational. Why each is there, what to take from it, a verified link per entry. |
| [`comparison.md`](comparison.md) | All 15 compared on audience, product base, key mechanism, trust, monetisation. Three market patterns, three differences we can hold, three open questions for the PM. |
| [`screens-index.md`](screens-index.md) | 38 product captures in [`screens/`](screens/), sorted group / competitor. Sign-in walls labelled. |
| [`flows/README.md`](flows/README.md) | The twelve flows: what each is for, what is collected, what is missing, what access it needs. |

## Flows

8 of 12 closed.

| # | Flow | Status | Notes |
|---|---|---|---|
| 01 | Item detail and trust | ◐ | — |
| 02 | Library browse, filter, search | ◐ | — |
| 03 | Relations without a canvas | ● | — |
| 04 | Validation: pass, warn, block | ● | [Terraform](flows/04-validation-check-results/terraform-plan-output.md) · [Vercel](flows/04-validation-check-results/NOTES-vercel.md) |
| 05 | Linked vs detached, blast radius | ● | [NOTES](flows/05-linked-vs-detached/NOTES.md) |
| 06 | Export and target adaptation | ● | [Ruler output](flows/06-export-and-target-adaptation/ruler-per-agent-output.md) |
| 07 | Env variables and secrets | ● | [NOTES](flows/07-env-and-secrets/NOTES.md) |
| 08 | Empty state and cold start | ◐ | — |
| 09 | Duplicate and fork | ● | [NOTES](flows/09-duplicate-and-fork/NOTES.md) |
| 10 | Dark design language | ◐ | — |
| 11 | Copy: errors, warnings, refusals | ● | [Conflict copy](flows/11-copy-and-error-language/dependency-conflict-copy.md) |
| 12 | Visibility and portfolio | ● | [NOTES](flows/12-visibility-and-portfolio/NOTES.md) |

## What is left

### Needs no access — can run on request

| What | For | Where from |
|---|---|---|
| A failing run: failed job, log annotations, the check summary on a PR | 04, 11 | GitHub Actions on a public repository |
| A scorecard in a blocking state, and its wording | 04 | demo.port.io, navigating deeper |
| An instance that is linked **but locally modified** — the state between clean and detached | 05 | The owner's Figma, access already granted. Reversible with Ctrl+Z, as before |

### Needs an account

| What | For | Note |
|---|---|---|
| Linear workspace | 02, 08, 10 | Command palette over populated data, a genuine first-run empty state, real density under load. Not self-hostable — cloud only, account required. Substitute if declined: `play.grafana.org` and `sandbox.sentry.io`, both open without login. |

### Declined or out of reach

| What | For | Why |
|---|---|---|
| Agentman skill page and permission tiers | 01 | Behind login. Lesson is legible from their marketing; three open skill catalogs already captured. |
| Cross-file component usage count | 05 | Figma library analytics, paid tier. The in-file instance count is captured; the cross-container number is not, and it is the shape of our "used in 3 projects". |
| Raycast desktop app | 10 | Installable here (`winget install raycast`), but wants a sign-in and takes a global hotkey. Needs a deliberate decision, not a sweep. |
| Packmind product, Continue Hub | 06 | Sales-gated and switched off. Both substituted — Ruler and the Continue repository. |
| Mobbin | reference | 403s without a subscription. Not worth buying; we capture products directly. |

## Definition of done

The research phase is finished when every flow is either ● or explicitly declined above, and
`comparison.md`'s three open questions have been answered by the PM. Those three questions —
what our answer is to Continue Hub dying, which trust signal we ship without a network or an eval
harness, and whether a personal library has a business — gate the design system, because they
decide what `visibility`, `Workspace` and `version` have to mean.

Next stage after sign-off: design system. Not started, per CLAUDE.md section 1.
