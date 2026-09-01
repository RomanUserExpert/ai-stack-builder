# `create-next-app` — producing an artefact and handing it over

Collected 2026-09-01 in a scratch directory outside the repo. One non-interactive run:

```
npx --yes create-next-app@latest bench-app --ts --tailwind --eslint --app --src-dir \
  --import-alias "@/*" --use-npm --no-turbopack --yes
```

B4 candidate: *produce an artefact and hand it over to another machine.* This is the closest
available analogue to our export — a generator that writes a tree, adapts files to named targets,
and has to say what it did.

## Console output, verbatim

```
Creating a new Next.js app in C:\...\bench-app.

Using npm.

Initializing project with template: app-tw

Installing dependencies:
- next
- react
- react-dom

Installing devDependencies:
- @tailwindcss/postcss
- @types/node
- @types/react
- @types/react-dom
- eslint
- eslint-config-next
- tailwindcss
- typescript

npm warn deprecated eslint@9.39.5: This version is no longer supported.

added 358 packages, and audited 359 packages in 1m
146 packages are looking for funding
found 0 vulnerabilities

npm warn allow-scripts 1 package has install scripts not yet covered by allowScripts:
npm warn allow-scripts   unrs-resolver@1.12.2 (postinstall: node postinstall.js)
npm warn allow-scripts   Run `npm approve-scripts --allow-scripts-pending` to review,
npm warn allow-scripts   or `npm approve-scripts <pkg>` to allow.

Generating route types...
✓ Types generated successfully

Initialized a git repository.

Success! Created bench-app at C:\...\bench-app
```

## What it does well

**The manifest is printed before the work, split by role.** Dependencies and devDependencies are two
labelled lists, by name, before a single package is fetched. You can read what you are about to get
and stop. Our Result screen owes the same thing for the archive: what is going in, grouped by kind,
before the button.

**The named steps are the receipt.** `Initializing project with template: app-tw` ·
`Generating route types… ✓` · `Initialized a git repository.` Three side effects, each stated as a
completed fact. The git init in particular is the kind of thing a generator does silently and a user
discovers later; here it is one line and there is no surprise.

**`allow-scripts` is the best consequence disclosure in the run**, and it is npm's, not Next's. It
names the package (`unrs-resolver@1.12.2`), the exact hook (`postinstall: node postinstall.js`), the
count (`1 package`), and two commands — review, or allow this one. Four facts and a choice, in three
lines, about code that would otherwise have run on the machine unannounced.

## The finding: two vendors, independently, chose the same two distribution mechanics

The scaffold writes both an `AGENTS.md` and a `CLAUDE.md`. They are not two copies.

`AGENTS.md` carries the content, inside a **named fenced block**:

```markdown
<!-- BEGIN:nextjs-agent-rules -->

# This is NOT the Next.js you know
...
This block is written and re-added by `next dev` — verify at
`node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only
re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->
```

`CLAUDE.md` is **one line**:

```
@AGENTS.md
```

That is exactly the pair Ruler produced from a completely different codebase and vendor
([`2-flows/06-export-and-target-adaptation/ruler-per-agent-output.md`](../2-flows/06-export-and-target-adaptation/ruler-per-agent-output.md)):
**copy the content with provenance, or point at the canonical file.** Two independent
implementations, same two mechanics, same managed-block-with-markers for the copy. Flow 06 called
this "at most two mechanics plus a naming convention per agent" from a single sample. It now has two.

**And the block explains its own re-appearance.** Three sentences tell you who rewrites it, where to
verify that claim in source, and what happens if you delete it — *"Removing it from a diff only
re-creates the uncommitted change."* That is a generated file anticipating the exact confusion it
causes on the second run. Ruler solved the same problem with a `.bak` and a `.gitignore` block, and
said nothing; Next says it in the file itself, where the person looking at the diff already is.

## Where it falls short

- **The success line is the last line, and it is the only summary.** `Success! Created bench-app at
  …` — no count of files written, no tree, nothing about the two agent files it just put in your
  repository. A user who did not run `ls -a` does not know `CLAUDE.md` exists.
- **A deprecation warning scrolls past inside the install noise** and is never restated at the end.
  If it mattered at the top it matters at the bottom; nothing is carried forward into the summary.
- **The one genuinely dangerous thing in the run — an unreviewed postinstall script — is a `npm warn`
  among other `npm warn`s**, visually equal to a funding notice.

## Straight into our design

1. **Print the manifest before the act**, grouped by role, by name.
2. **State every side effect as a completed fact**, including the ones we think are obvious.
3. **The final summary carries counts and anything still outstanding** — a generator that ends on the
   word *Success!* and nothing else throws away the only line everyone reads.
4. **A generated file explains its own provenance and what happens if you delete it**, in the file.
5. **Severity must be visible in the shape of the line, not only in its words.** One `warn` prefix for
   both funding and unreviewed code execution is our `Problem` and our `Note` in the same grey.
