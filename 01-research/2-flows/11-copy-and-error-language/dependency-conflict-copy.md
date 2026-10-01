# Dependency-conflict copy: two real examples

Collected 2026-08-31 by reproducing both conflicts locally. These are the exact strings our own
conflict and version-clash messages will be measured against.

---

## 1. Terraform — two modules demanding incompatible provider versions

Module `a` requires `local ~> 2.4.0`, module `b` requires `local ~> 2.5.0`.

```
Initializing modules...
- b in modules\b
- a in modules\a

Initializing provider plugins...
- Finding hashicorp/local versions matching "~> 2.4.0, ~> 2.5.0"...

Error: Failed to query available provider packages

Could not retrieve the list of available versions for provider
hashicorp/local: no available releases match the given constraints ~> 2.4.0,
~> 2.5.0

To see which modules are currently depending on hashicorp/local and what
versions are specified, run the following command:
    terraform providers
```

**Why it works.**

- It shows the **merged constraint** (`"~> 2.4.0, ~> 2.5.0"`) before failing, so you see the
  contradiction itself rather than a verdict about it.
- The failure names the subject once, in plain words: *no available releases match*.
- **It hands you the next command.** It does not say "resolve the conflict"; it says run
  `terraform providers`, which prints who is asking for what. This is the single best idea here —
  our conflict state should always offer the "show me who pulled this in" action, not just the fact.

**Its weakness, which we can beat.** It does *not* say which module wanted which constraint. That
costs a second command. We already hold both edges of the graph, so we can name both sides in the
first message.

---

## 2. Terraform — a resource missing a required attribute

```
Error: Invalid Attribute Combination

  with local_file.broken,
  on main.tf line 6, in resource "local_file" "broken":
   6: resource "local_file" "broken" {

No attribute specified when one (and only one) of
[content,sensitive_content,content_base64] is required
```

**Why it works.** A titled error class, the object, the file and line, the source excerpt, and then
the rule stated as a rule — *one and only one of these three*. Our equivalent: an item that is
missing an env key, or two items writing the same `targetPath`.

---

## 3. npm — the most familiar dependency error in existence

```
npm error code ERESOLVE
npm error ERESOLVE unable to resolve dependency tree
npm error
npm error While resolving: conflict-demo@1.0.0
npm error Found: react@17.0.2
npm error node_modules/react
npm error   react@"17.0.2" from the root project
npm error
npm error Could not resolve dependency:
npm error peer react@"^18.0.0" from @testing-library/react@16.0.0
npm error node_modules/@testing-library/react
npm error   @testing-library/react@"16.0.0" from the root project
npm error
npm error Fix the upstream dependency conflict, or retry this command with --force or
npm error --legacy-peer-deps to accept an incorrect (and potentially broken) dependency resolution.
```

**What to take.** The `Found:` / `Could not resolve dependency:` pairing is the right structure —
here is what is installed, here is what wanted something else, and each side is traced to who asked
for it. That is precisely the two-sided story our conflict card must tell.

**What to avoid.** Two things.

- Every line is prefixed `npm error`, including the blank ones. Fourteen repetitions of the word
  "error" for one problem. Ours states the severity once.
- The remedy offered is `--force` or `--legacy-peer-deps`, described in the same breath as
  "incorrect (and potentially broken)". Offering an escape hatch you simultaneously disown teaches
  people to reach for it reflexively. If we let a user export over a soft conflict, the wording has
  to own that decision rather than warn against itself.

---

## The pattern across all three

Name the two sides, trace each to who asked for it, state the rule that was broken, and offer a
concrete next action. Terraform does the first, third and fourth well; npm does the second best.
Nobody does all four in one message — that is available to us.
