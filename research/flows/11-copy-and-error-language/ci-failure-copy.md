# CI failure copy — what a failing run actually says

Captured 2026-09-01 from public GitHub, no account. Companion to
[`dependency-conflict-copy.md`](dependency-conflict-copy.md), which covers *conflict* wording;
this one covers *failure* wording. Structural findings from the same run are in
[`../04-validation-check-results/NOTES-github-actions.md`](../04-validation-check-results/NOTES-github-actions.md).

Source: [`vercel/next.js` PR #98129](https://github.com/vercel/next.js/pull/98129), commit `357605a`,
run `33473495683` — 102 jobs, 7 failed.

---

## 1. The anti-reference: the annotation slot that says nothing

The run's Annotations panel is headed **"11 errors and 6 warnings"**. Fourteen of the seventeen rows
read, in their entirety:

```
Process completed with exit code 1.
```

That is the complete public failure report for six separate jobs. The slot is prominent, counted in
a header, rendered in monospace, and empty of information: no test name, no file, no assertion, no
next step.

**We checked whether this is one repository being careless. It is not.** Every failure annotation
across `vercel/next.js`, `denoland/deno`, `withastro/astro`, `vitejs/vite` and `rust-lang/rust-clippy`
was of the form `Process completed with exit code N` — 1, 2 and 101. The only long-form annotation
found anywhere in the sweep was a *warning* about Node.js 20 deprecation. **The failure channel
carries less information than the deprecation channel.**

The reason is structural and applies to us directly: the annotation is emitted by the process that
*noticed* the failure (the shell wrapper), not by the process that *caused* it (the test runner). If
our validation pass reports at the wrong altitude — "export blocked" rather than "`db-migrate`
requires `postgres-mcp`, which is not in this project" — we will produce exactly this.

## 2. The three annotations that do work, and what each supplies

| Text | What it adds | Steal |
|---|---|---|
| `Unable to download artifact(s): Failed to ListArtifacts: Received non-retryable error: Failed request: (403) Forbidden` | Whether retrying helps | **`non-retryable`.** One word that prevents a wasted re-run. Our analogue: which problems the user can fix here, and which need the library. |
| `The job has exceeded the maximum execution time of 30m0s` | The limit that was hit, as a number | State the threshold, not the judgement. "Timed out" tells you nothing; `30m0s` tells you whether to raise it. |
| `The operation was canceled.` | The consequence, as its own row | The same job emitted the timeout *and* this, in that order. **Cause and consequence are two rows.** |

## 3. The reference: a bot that posts a distilled failure report where the reader is

`github-pr-bot-failing-test-suites.png` — the best failure copy in the survey, and it is not on the
run page at all. A bot posts it into the PR conversation:

> ## Failing test suites
> Commit: `357605a` | About building and testing Next.js
>
> `pnpm test-start-experimental-turbo test/e2e/app-dir/segment-cache/prefetch-inlining/prefetch-inlining.test.ts`
> (turbopack) (Experimental) (**job**)
> - prefetch inlining > partially generated dynamic route: build hints use the most specific shell (**DD**)
>
> ▶ Expand output

Six decisions worth taking whole:

1. **It goes to the reader, not to a log.** Nobody opens a 102-job run to find seven red squares.
2. **It is grouped by the command that reproduces it**, not by CI job. The heading of each group is
   a copy-pasteable line that runs exactly that suite locally. The most actionable thing on the page
   is the group header.
3. **It names the commit it is about.** Failure reports go stale; this one is stamped.
4. **The failing test is named in full**, as its nested description path —
   `prefetch inlining > partially generated dynamic route: build hints use the most specific shell` —
   which is a sentence, not an ID.
5. **Two escape hatches per row, both parenthesised and tiny**: `(job)` back to CI, `(DD)` out to the
   observability tool. The detail is reachable without being present.
6. **`Expand output` is collapsed by default.** The raw text is there; it is not the first thing.

Our validation result should read like this, not like a build log: grouped by what the user would do
about it, each row naming the item and the rule, raw detail one disclosure away.

## 4. The best sentence in the capture: cause, then consequence

`github-pr-bot-suggested-change.png` — an automated reviewer leaves a diff suggestion and one line of
prose beneath it:

> `baseHints ||=` short-circuits and drops the `ShouldAttemptStaticPrefetch` bit when both
> static-attempt flags are true, so PPR-strategy prefetches of fully-static routes deopt to runtime.

Its shape: **the mechanism** (`||=` short-circuits), **the condition under which it bites** (when both
flags are true), **the consequence in the reader's terms** (prefetches deopt to runtime). No severity
word, no "error", no apology, no imperative. And it arrives *attached to the four lines it is about*,
with the fix already written as an applyable diff.

That is the template for every conflict message we write:

> `web-search` and `web-fetch` both register the command `search`, so whichever loads second wins and
> the other is silently unreachable.

Mechanism · condition · consequence. Then the fix, next to the thing.

## 5. Blocking stated as a requirement, not an error

`github-pr-conversation-failing.png` — the Reviewers panel does not say "you cannot merge". It says:

> At least 1 approving review is required to merge this pull request.

Present tense, names the requirement, names the count, no red, no exclamation. Compare our own
worst instinct — "Export blocked: unresolved conflicts". The GitHub form generalises to:

> Two items write to `.mcp.json`. Resolve the collision to export this project.

Two more things on the same screen. The commit list carries **per-commit check status inline** — only
the head commit `357605a` shows a red cross, the two before it show no glyph at all rather than a
stale green one. And the sentence above is filed under **Reviewers**, next to the reviewer who is
missing, not in a banner at the top: the requirement lives where the thing that satisfies it lives.

**Limit worth recording:** PR #98129 is a *draft*, and a signed-out visitor does not get the
"Some checks were not successful" merge box on a draft PR. The per-check verdicts are all public on
the Checks tab; that one merge-box sentence was not capturable here.

## 6. Checklist for our copy

- Never emit a message the item's own name is missing from.
- Name the threshold or the expected value, never only the judgement.
- Say whether the user can act on it now.
- Cause and consequence are separate rows.
- Group by the action that fixes it, not by the check that found it.
- Raw detail collapsed, present, one click away.
- Blocking reads as a requirement in the present tense.
