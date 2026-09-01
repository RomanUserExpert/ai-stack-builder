# `npm install` against a peer conflict — the best failure line we have found

Collected 2026-09-01, npm 11.x, in a scratch directory outside the repo. A three-line
`package.json` was written to force a real conflict — `react@17.0.2` against
`@testing-library/react@16.1.0`, which requires `react@^18 || ^19` as a peer — and `npm install`
was run once. Nothing was installed into this project.

**Why this capture exists.** Stage 4 lists Homebrew's `Brewfile` and Docker Compose as B2
candidates for *assemble a set under constraints*. Neither can be run on this machine — Brewfile is
macOS, Docker is not installed. npm is, it is the same problem exactly (a declared set, resolved
against constraints the items carry themselves), and unlike a `Brewfile` read from documentation it
can actually be made to fail. Recorded as a **documented substitution**, not a silent one.

## Output, verbatim

```
npm error code ERESOLVE
npm error ERESOLVE unable to resolve dependency tree
npm error
npm error While resolving: conflict-probe@1.0.0
npm error Found: react@17.0.2
npm error node_modules/react
npm error   react@"17.0.2" from the root project
npm error
npm error Could not resolve dependency:
npm error peer react@"^18.0.0 || ^19.0.0" from @testing-library/react@16.1.0
npm error node_modules/@testing-library/react
npm error   @testing-library/react@"16.1.0" from the root project
npm error
npm error Fix the upstream dependency conflict, or retry this command with --force or
npm error --legacy-peer-deps to accept an incorrect (and potentially broken) dependency resolution.
npm error
npm error For a full report see:
npm error C:\Users\...\_logs\2026-09-01T16_27_46_114Z-eresolve-report.txt
```

## Why it scores where it does

**It answers all four questions a conflict message owes**, and they are separable:

| Question | The line that answers it |
|---|---|
| What was required? | `peer react@"^18.0.0 \|\| ^19.0.0"` — the range, not "a newer version" |
| What was found? | `Found: react@17.0.2` |
| Who required it? | `from @testing-library/react@16.1.0` |
| Who asked for the thing that was found? | `react@"17.0.2" from the root project` |

That last row is the one almost nothing else does. It distinguishes *you chose this* from *something
else dragged this in* — which is precisely our `addedBy: manual | dependency`. A user cannot act on
a conflict until they know whether the offending item is theirs to remove.

**It names both escape hatches and labels the cost of taking them.** `--force` and
`--legacy-peer-deps` are printed in the failure itself, with the consequence attached in the same
sentence: *"to accept an incorrect (and potentially broken) dependency resolution."* Not a warning
triangle, not a docs link — the word **incorrect**, about the state you will be in if you proceed.

This is the same primitive as our unclean export (CLAUDE.md §6): never refuse, state the cost in the
present tense, let the user proceed. npm arrives at it from the opposite direction — it *does* refuse
by default, then hands you the override and tells you what it buys. Ours is the softer of the two and
should borrow the sentence, not the refusal.

**It splits the summary from the full report.** Twelve lines on screen, a path to the complete
resolution trace on disk. Count-and-digest, the same instinct as Vercel's *"66 lines"* and GitHub's
*"11 errors and 6 warnings"*.

## Where it falls short

- **It reports one conflict, not the set.** The resolver stops at the first unsatisfiable edge. A
  project with four incompatible items is four sequential runs. Our validation pass reports every
  Problem in one sweep, and that is a genuine advantage worth keeping — a stack of collapsed stages
  (Vercel) filled with npm-grade sentences.
- **No remedy is offered in place.** `Fix the upstream dependency conflict` is not an action; it is
  a homework assignment. Nothing suggests the version that *would* satisfy both, though npm knows the
  range and the registry. Our conflicts are declared by the user between two items in their own
  library, so our equivalent remedy — *remove one, detach one, or accept* — is offerable and should
  be offered on the row.
- **The path to the full report is absolute, long, and in a cache directory** most people will never
  visit. A digest that no one opens is a digest that does not exist.

## Straight into our design

1. **Four facts per conflict row**: required, found, who required it, who brought in what was found.
2. **Print the override next to the refusal, with the word for what it costs.**
3. **Report every problem in one pass, not the first one.**
4. **Offer the remedy on the row**, since unlike npm we know the whole library and can name it.
