# Scorecards in a failing state — Port, captured 2026-09-01

The gap the plan called "a scorecard in a blocking state, and its wording". Taken from the open
`demo.port.io`, which needs no account. Read-only: nothing was edited, run or saved.

Supersedes the thin `port-governance-standards.png` from the first pass, which showed the governance
section but no result.

---

## The headline finding: Port does not block. Port gates a level.

**We did not find a blocking state, because the demo has none.** Nothing in the scorecard surface
refuses an action or says "blocked". What exists instead is a **cumulative level ladder**: a rule
that fails does not stop you doing anything, it stops the entity climbing.

`port-service-scorecards-tab.png`

On a service entity's **Scorecards** tab, a four-stop rail runs `Basic → Low → Good → Great`, with
achieved stops filled green and the rest hollow. Below it, one section per tier:

```
Low Tier                                             0/2   ②
  ✗ Code coverage > 75
  ✗ No open critical vulnerabilities
Good Tier                                            0/3   ③
  ✗ Branch Protection Set
  ✗ Sonar Issues < 5
  ✗ Security Hotspots < 5
Great Tier                                           0/3   ③
  ✗ No High Vulnerability
  ✗ Repo requires approval
  ✗ Freshness < 7 days
```

Each tier shows `passed/total` plus an orange badge counting what is *unmet*. The two numbers are not
redundant: `0/2` is progress, `②` is work outstanding, and the badge is the one coloured.

**This is a real answer to a question we have not settled.** Our validation pass currently splits
hard-blocks from soft-warnings — a binary. Port's ladder is a third option: nothing is forbidden, but
the project's grade is stated, and you can see precisely which rule stands between you and the next
grade. Worth weighing against the binary before the design system fixes it.

## Rules are named as the state you want, never as the failure

Every rule in the list above reads as a satisfiable condition — `Code coverage > 75`,
`Branch Protection Set`, `No open critical vulnerabilities`, `Freshness < 7 days`. Not one is phrased
as a complaint (`Coverage too low`, `Missing branch protection`). The red cross supplies the polarity;
the text supplies the target. One string serves the passing row and the failing row.

Our equivalents write themselves: `Every required item present`, `No duplicate command names`,
`No two items write to the same path`, `Every needed env variable declared`.

## Expanding a rule gives the predicate and the observed value

`port-scorecard-rule-expanded.png` — **the single most useful thing in this pass.**

Clicking a failing row opens exactly one line:

```
✗  [where]  "Open Critical Vulnerabilities" = 0                          Value: 1
```

The condition it required, tagged `where`, on the left. The value it actually found, right-aligned.
No prose, no error code, no severity word. You can see in one glance both what was demanded and how
far off you are, and the same line renders for a rule that passes.

Set beside `Process completed with exit code 1` from
[`NOTES-github-actions.md`](NOTES-github-actions.md), this is the whole lesson of flow 04 in two
lines of copy.

## Level vocabularies are per-scorecard, and that is a mistake we should not repeat

`port-scorecards-list.png`, `port-scorecard-ai-coding-standards.png`

Across the fourteen scorecards in the demo there are at least five different ladders:

| Scorecard | Levels |
|---|---|
| Jira Metrics, Reliability Health, Production Readiness… | Basic · Bronze · Silver · Gold |
| DORA Metrics | Low · Medium · High · Elite |
| Security Maturity | Basic · Low · Good · Great |
| Protection Metrics | Basic · Low · Medium · High |
| **AI Coding Security Standards** | **Critical · Compliant · Elite** |

The same entity therefore shows, in one row of chips: `Security Maturity · Basic`,
`Production Readiness · Red`, `DORA Metrics · Low`, `Service Health · Bronze`,
`AI Coding Security Standards · Critical`. Five scales, one screen, and `Critical` is the *bottom*
rung of one ladder while reading as an emergency everywhere else. The reader cannot compare two chips
without knowing which ladder each belongs to.

**Take the ladder, reject the per-scorecard vocabulary.** If we grade a project, one scale, fixed in
the design system.

## The two directions of the same data

Port publishes the scorecard both ways round, as two separate screens, and both are useful to us:

- **By scorecard** (`port-scorecards-list.png`) — `Rules tested · Rules passed · % of rules passed`.
  Security & Compliance over repositories: 72 tested, 26 passed, **36.11%**. Production Readiness
  over APIs: 48 of 48, **100%**.
- **By rule** (`port-scorecard-rules-list.png`) — the transpose: `Entities tested · Entities passed ·
  % of entities passed`, 31 rules. This is *how much of the estate one rule affects*, which is the
  same shape as our blast-radius question, "used in 3 projects", pointed at rules instead of items.

## The scorecard's own page treats the score as a metric over time

`port-scorecard-security-compliance.png` — a big `36.11`, a passed/not-passed donut, **a trend line
of the same percentage from March to August**, a rule-results table grouped by level, and a breakdown
by team.

Out of scope for us: our MVP has no history and no teams (CLAUDE.md §9). Recorded because it shows
where a validation result goes once it is stored rather than recomputed — and it argues that the
moment a score is persisted, someone will want its trend. A reason to keep our validation result
derived and momentary, not saved.

## What to carry into design

1. **Consider a grade, not only a verdict.** Blocked / warned / clean may be the wrong shape; Port's
   ladder is the alternative to weigh.
2. **A rule is a condition, never a complaint.** One string, both polarities.
3. **Failure detail = predicate + observed value.** `where … = 0 · Value: 1`.
4. **Two counts per group**: progress `0/2`, and the coloured badge for what is outstanding.
5. **One severity vocabulary across the whole product.**
6. **Both projections of the check** — by item, and by rule.
