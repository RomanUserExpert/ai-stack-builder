# `terraform validate` against a broken config — the C3 capture flow 04 was missing

Collected 2026-09-01, Terraform v1.16.0, downloaded to a scratch directory outside the repo, nothing
installed system-wide. Same method as
[`2-flows/04-validation-check-results/terraform-plan-output.md`](../2-flows/04-validation-check-results/terraform-plan-output.md),
which captured a **successful** plan and left failure copy unobserved.

The config was written to produce our three findings, deliberately, in one file:

| Our finding | The Terraform equivalent planted in the config |
|---|---|
| Two items write to the same target path | two `local_file` resources named `manifest`, both writing `./out/SETUP.md` |
| A required item is not in the project | `local_file.readme` referencing `local_file.db_tools`, which does not exist |
| An item is missing something it needs | `local_file.env_example` with a `filename` and no content |

---

## Run 1 — the collision, and what it hides

```
Error: Duplicate resource "local_file" configuration

  on main.tf line 15:
  15: resource "local_file" "manifest" {

A local_file resource named "manifest" was already declared at
main.tf:10,1-33. Resource names must be unique per type in each module.
```

**Both sides of the collision are named**, and the second one with a column range —
`main.tf:10,1-33`. Not *"duplicate name"*, not *"a conflict was found"*: here is the one you just
wrote, here is the one that was already there, and here is the rule that makes them incompatible.

CLAUDE.md §6 asks for exactly this on a merged MCP config — *say which one wins and say both refs*.
This is the sentence to model it on.

**And it is the only error printed.** The other two defects are in the same file, untouched, and
invisible: a parse-level failure aborts before the schema and reference checks run. `terraform init`
fails the same way, with the same single message.

## Run 2 — the same file with the duplicate removed

Now the later stages run, and Terraform reports **every** remaining problem in one pass:

```
Error: Invalid Attribute Combination

  with local_file.env_example,
  on main.tf line 15, in resource "local_file" "env_example":
  15: resource "local_file" "env_example" {

No attribute specified when one (and only one) of
[content,sensitive_content,source] is required
```

…repeated **four times**, once per permutation of the mutually exclusive set
(`[content,sensitive_content,source]`, `[content,sensitive_content,content_base64]`,
`[content,content_base64,source]`, `[sensitive_content,content_base64,source]`) — and then:

```
Error: Reference to undeclared resource

  on main.tf line 20, in resource "local_file" "readme":
  20:   content  = local_file.db_tools.content

A managed resource "local_file" "db_tools" has not been declared in the root
module.
```

## What is worth copying

**The anatomy of the reference error is complete.** Four facts in five lines: the item that has the
problem (`local_file.readme`), where it is (`main.tf` line 20), **the source line itself echoed
back**, and the rule in plain words — *"has not been declared in the root module"*. It never says
"unresolved dependency". It names the thing, quotes the line, and states what is untrue about it.

That echoed source line is the detail to steal. It costs nothing — we have the item — and it removes
the step where the reader goes to look at what they wrote.

**A `with` line and an `on` line are different addresses, and both are given.** `with
local_file.env_example` is the *logical* address in the resolved set; `on main.tf line 15` is the
*physical* one in the source. Our findings have the same pair: the item, and the file inside the
archive it will land in. Print both.

**It reports the whole set once the parse succeeds.** Five diagnostics, no early exit, no "1 of many
errors". This is the opposite of npm's ERESOLVE, which stops at the first unsatisfiable edge
([`npm-eresolve.md`](npm-eresolve.md)), and it is the behaviour our validation pass needs: one press,
every Problem.

## What is worth avoiding, and it is sharper than it looks

**One defect produced four errors.** A single resource with no content emits four diagnostics that
differ only in which three-element permutation they quote. The reader's first inference is that there
are four separate problems; the second is that they must satisfy four different requirements. Both are
wrong. This is a validator emitting one message per internal rule that failed, rather than one message
per thing that is wrong with the user's work — the error list is a report about the checker, not about
the config.

We have exactly this exposure. A target-path collision between three items is *one* Problem, not three
pairs. A duplicate command name across four items is one row that names four, not six rows naming two
each. **Count Problems the way the user counts them: one per defect in their set.**

**A blocking error silently cancels the checks behind it.** Run 1 reported one error out of three
because the parse stage aborted. Terraform never says *"the reference check did not run"* — it simply
shows less, and a reader who fixes the duplicate and re-runs discovers two new errors that were there
all along. That reads as the tool finding new problems each time you fix one, which is corrosive to
trust in exactly the moment trust matters.

**Our answer to this already exists and now has its justification.** CLAUDE.md §6 gives us a third
severity — **Skipped**, with its own neutral glyph, for a check that had nothing to check. The same
glyph carries the case Terraform leaves silent: a check that *could not* run because an earlier stage
failed. The stage list stays complete, and the count of what has been verified never quietly shrinks.

## Straight into our design

1. **Name both sides of a collision**, with their locations, and say which wins.
2. **Echo the offending line back** — the item's field, verbatim.
3. **Two addresses per finding**: the item in the set, and the path in the archive.
4. **One Problem per defect in the user's set**, never one per internal rule that fired.
5. **A stage that could not run says so.** Skipped covers both "nothing to check" and "blocked by an
   earlier stage"; what it must never do is disappear.
