# A failing run — GitHub Actions, captured 2026-09-01

The gap the plan called "a failing run: failed job, log annotations, the check summary on a PR".
Taken anonymously from a public repository; nothing was signed into, re-run or commented on.

**Source.** [`vercel/next.js` run 33473495683](https://github.com/vercel/next.js/actions/runs/33473495683)
— workflow `build-and-test`, run `#124424`, on [PR #98129](https://github.com/vercel/next.js/pull/98129),
commit `357605a`. **102 jobs: 7 failed, 4 skipped, 1 cancelled, the rest green.** A single run
carrying every verdict we will ever need to draw.

Companion to [`NOTES-vercel.md`](NOTES-vercel.md) (a process running visibly) and
[`terraform-plan-output.md`](terraform-plan-output.md) (a result reading legibly). This one is about
**partial failure**: what a run looks like when most of it worked.

---

## 1. Four verdicts, four glyphs, no colour dependency

`github-actions-run-failed-annotations.png`, `github-actions-failed-job-steps.png`

The left rail lists every job with a glyph, and the glyph alone distinguishes the states — colour is
redundant, not load-bearing:

| Verdict | Glyph |
|---|---|
| success | filled green disc, white tick |
| failure | filled red disc, white cross |
| **skipped** | hollow grey circle with a diagonal slash |
| **cancelled** | grey, distinct from both failure and skip |

**Skipped is not a failure and does not look like one.** Our validation pass has the same case — a
conflict check on a project with one item, an env check with no `needsEnv` — and it must get the
neutral glyph, not a green tick it did not earn and not a red one it does not deserve.

The same treatment runs one level down. Inside a job, every *step* carries its own glyph, and a step
can be tagged `BACKGROUND` (here, `Install Rust`) — a fourth thing that is neither pass, fail nor
skip: still running, deliberately, while the rest proceeds.

## 2. Annotations: a counted, collapsible digest above the detail

`github-actions-run-failed-annotations.png`

The run page carries an **Annotations** panel headed **"11 errors and 6 warnings"** — a count before
any content, exactly like Vercel's "66 lines". Each row is *job name* over *message*, in monospace,
with a `Show more` on anything long.

On the job page the same panel appears scoped and collapsed: **"Annotations · 1 error"**, shut by
default, above the step list. Same component, two altitudes. Worth copying: the run-level digest and
the item-level digest are the same object, filtered.

## 3. The failure line states a duration

> **test prod (1/10) / build** — *failed 4 hours ago in 14m 6s*

A failed job reports how long it took to fail. Most tools drop the timing once the verdict is bad, as
if a failure had no cost. Fourteen minutes is exactly what the reader wants to know before deciding
whether to re-run.

## 4. Where GitHub is worth copying, and where it is not

**The vocabulary of the good annotations** — three of the seventeen carry real information, and each
answers a different question:

| Annotation | What it adds |
|---|---|
| `Unable to download artifact(s): Failed to ListArtifacts: Received non-retryable error: Failed request: (403) Forbidden` | **Whether retrying will help.** "non-retryable" is one word that saves a wasted re-run. |
| `The job has exceeded the maximum execution time of 30m0s` | **The limit that was hit**, stated as a number, not "timed out". |
| `The operation was canceled.` | The *consequence*, filed separately from the cause — the same job emitted both, in that order. |

Cause and consequence as two annotations rather than one sentence is the right instinct: a cancelled
job is not a failing job, and the reason it stopped is a separate fact from the fact that it stopped.

**The anti-reference is everything else.** Fourteen of seventeen annotations read, in full:

```
Process completed with exit code 1.
```

This is the whole failure report for six different jobs. It names no test, no file, no assertion —
the annotation slot exists, is surfaced prominently, is counted in the header, and is filled with
nothing. Copy analysis is in [`11-copy-and-error-language/ci-failure-copy.md`](../11-copy-and-error-language/ci-failure-copy.md),
including the check that this is industry-wide rather than one repository's sloppiness.

## 5. The check summary on a PR

`github-pr-checks-failed-check-detail.png`

The PR's **Checks** tab (127 checks here) groups by workflow, each group labelled with its trigger —
`build-and-deploy · on: push`, `build-and-test · on: pull_request` — because the same workflow name
appears more than once with different triggers and would otherwise be ambiguous. Deep-linking to a
single check (`?check_run_id=…`) selects it in the tree and opens its detail on the right.

The commit selector carries a **partially-filled ring**, not a red cross: a mixed result gets its own
glyph rather than being flattened to the worst state. Our project header has the same problem the
moment one check blocks and four pass.

## 6. What could not be captured, and it matters

**Log bodies are behind a login.** Both the run page and the Checks tab say so —
*"Sign in to view logs"*, *"Sign in for the full log view"* — on a fully public repository. The step
list, its glyphs, the timings and the annotations are all public; the text of the log is not.

So the deep log reference stays [`NOTES-vercel.md`](NOTES-vercel.md), which was captured from inside
an account. What GitHub gives us that Vercel did not is the **partial-failure structure**: one run,
102 units, four verdicts, and a digest that counts them.

## 7. Straight into our design

1. **Skipped and cancelled need their own glyphs**, decided at design-system time, not invented later
   when the first check turns out not to have run.
2. **Count before content.** "6 problems in 4 items" above the list, mirrored per item.
3. **A failed stage keeps its duration.**
4. **Cause and consequence are separate rows.** "`db-migrate` requires `postgres-mcp`, which is not in
   this project" and "`db-migrate` cannot be exported" are two facts; showing only the second is what
   `exit code 1` does.
5. **Never ship our own `exit code 1`.** Every row our validation pass emits names the item, the
   rule and the observed value — see Port's `where "Open Critical Vulnerabilities" = 0 · Value: 1`
   in [`NOTES-port.md`](NOTES-port.md).
