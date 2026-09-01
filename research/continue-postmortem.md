# Continue Hub — post-mortem from source

The closest hard competitor: same object model, same audience, 34k stars, Apache-2.0 — acqui-hired by
Cursor around 16 June 2026 and switched off, cloud data deleted after 15 July 2026.
[`competitors.md`](competitors.md) calls this post-mortem the highest-value item in the survey, and
[`comparison.md`](comparison.md)'s **first open question for the PM** is *"Continue Hub was this
product and it died. What is our answer?"* — which cannot be answered without knowing precisely what
it did.

Read from [`github.com/continuedev/continue`](https://github.com/continuedev/continue), package
`packages/config-yaml`, on 2026-09-01.

**Caveat, and it matters.** This is **current HEAD, post-acquisition**. The composition machinery
survives because the config format is still used locally; the *hub* surfaces — publishing, browsing,
versioning on `hub.continue.dev` — have been stripped from the docs. So what follows is an accurate
account of the **format and the resolver**, and a thinner one of the marketplace around them. Where
this note describes the product rather than the code, it is inference from the format, and says so.

---

## 1. What it was

A registry of **blocks** plus a composition format that assembled them into an **assistant**. You
published a block, someone referenced it by slug in their `config.yaml`, and the resolver — Continue's
word is **unroll** — pulled every referenced block in and flattened the result into a single
configuration the extension could run.

One entity, seven types. From `load/getBlockType.ts`:

```
models · context · data · mcpServers · rules · prompts · docs
```

Compare our six kinds — `skill · agent · prompt · mcp · script · app`. Three overlap almost exactly
(`prompts`, `mcpServers`, and `rules` ≈ our `skill`). They carried `models`, `data`, `docs` and
`context`, which we deliberately do not. We carry `agent`, `script` and `app`, which they did not.

**A block is exactly one thing.** `blockSchema` is a union in which each arm requires an array of
`.length(1)`. There is no such thing as a block containing two rules. Our `Item` has the same
atomicity, enforced by convention rather than by schema — worth tightening.

## 2. The composition primitive, and it is our linked/detached question already answered

This is the find. A project references a block three ways at once:

```yaml
models:
  - uses: test-org/gemini            # live link to the library block
    override:                        # local modification, link intact
      contextLength: 500000
      apiBase: https://example.com

  - uses: test-org/claude35sonnet
    with:                            # template inputs
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}

  - name: gpt-5                      # inline, no link at all
    provider: openai
    model: gpt-5
```

- **`uses`** — a live link by slug. Our `ProjectItem` with `detached: false`.
- **`with`** — template inputs filled at resolution. We have no equivalent and probably need one.
- **`override`** — **a partial local override that keeps the link.** Our `ProjectItem.overrides`.
- An inline object with no `uses` — our `source: inline`.

**Continue never detaches.** There is no operation that severs the link and keeps the content. You
either link and layer an override on top, or you write the thing inline from the start. That is a
simpler model than ours, and it dodges the problem Figma has and we inherited — a detached object with
no way home — by never creating the state.

Two details worth carrying:

- **`mergeOverrides` is a shallow, top-level key overwrite** (`load/unroll.ts`). No deep merge. An
  override replaces a whole field, never part of one. Simple, predictable, and the right default.
- **`rules` cannot be overridden.** Every other block type accepts `override`; rules accept only
  `uses` and `with`. An asymmetry with no comment explaining it — either a deliberate call that prose
  is not partially patchable, or an oversight. Ours is the same question for `skill` content.

## 3. Identity: one string that is either a slug or a path

From `interfaces/slugs.ts`:

```
ownerSlug/packageSlug@versionSlug      →  a registry block, "latest" if the version is omitted
./relative/path,  /absolute,  ~/home   →  a local file
```

`PackageIdentifier` is a discriminated union of `{uriType:"slug"}` and `{uriType:"file"}`, and
`decodePackageIdentifier` picks between them by first character. That is one field doing the work our
model spreads across `source`, `content`, `repoUrl` and `path` — and it is better: a single
identifier, parsed, with the local and remote cases equally first-class.

## 4. Secrets: a fully qualified name, and it solves a problem we have not noticed

`FQSN` — Fully Qualified Secret Name — encodes a secret as **the chain of packages it was requested
through**, not just its name:

```
owner-a/block-a/owner-b/block-b/ANTHROPIC_API_KEY
```

If block A uses block B and B needs `ANTHROPIC_API_KEY`, the secret's identity carries the path. Two
blocks in one project can therefore both want `API_KEY` and mean different keys.

Our `needsEnv: [string]` is a flat list of bare names and cannot express that. Collecting `needsEnv`
across a resolved set and writing `.env.example` — CLAUDE.md §6 — silently assumes every same-named
variable is the same variable. On any real set it will not be.

## 5. What the resolver did — and the three things it did not

`unrollAssistant` walks the referenced blocks, fills template variables, applies overrides, and
flattens everything into `AssistantUnrolled`, where every section is a flat array. Errors are
**collected, not thrown**: the walk continues, and a block that failed to resolve is left in place as
**`null`** rather than dropped. The resolved config preserves the hole.

That last part is good and we should copy it. The three gaps are the interesting half.

### It has no cycle detection. None.

`grep -rniE "cycle|circular|visited|maxDepth"` across `packages/config-yaml` returns nothing but an
unrelated model flag. A block that references a block that references the first has no guard in this
code path. CLAUDE.md §6 specifies a three-colour walk for exactly this — untouched / in progress /
done — which turns out to be a feature the nearest competitor never shipped.

### It detects duplicates and then throws the answer away

`BlockDuplicationDetector` is a whole class. It keys on `block.name` per block type (for rules, the
rule string itself; for context, `name ?? params.title ?? provider`). It works. And then, in
`mergeUnrolledAssistants`:

```ts
for (const block of allOfType) {
  if (block && !duplicationDetector.isDuplicated(block, blockType)) {
    deduplicated.push(block);
  }
}
```

The duplicate is **silently discarded**. No error, no warning, nothing added to an `errors` array —
that function does not even have one. First occurrence in the merged order wins; the loser vanishes
without a message.

**This is our product's entire thesis, sitting unclaimed in the closest competitor's source.**
CLAUDE.md's opening argument is that nothing tells you *"that two items register the same command
name"*. Continue **computed exactly that** and then dropped it on the floor. Not a missing feature —
a surfacing failure, the same shape as the Figma override finding in
[`flows/05-linked-vs-detached/NOTES.md`](flows/05-linked-vs-detached/NOTES.md): the data existed and
was correct, and no one was told.

### Severity is a boolean

```ts
export interface ConfigValidationError {
  fatal: boolean;
  message: string;
  uri?: string;
}
```

`fatal: true | false` — our hard-block / soft-warn binary, already built by someone else. And a block
that failed to resolve is filed as `fatal: false`, so a missing dependency degrades the assistant
quietly rather than stopping it. Set against Port's level ladder
([`flows/04-validation-check-results/NOTES-port.md`](flows/04-validation-check-results/NOTES-port.md)),
this is the other pole of the **block-or-grade** question, and it is a data point *for* the binary
being too coarse.

## 6. What this changes for us

**Take:**

1. **`uses` / `with` / `override` as the membership model.** Ours is the same idea with worse names,
   and `with` — template inputs at resolution — is missing entirely.
2. **One parsed identifier** instead of `source` + `content` + `repoUrl` + `path`.
3. **Qualify env variables by the chain that asked for them.** A flat `needsEnv` list is wrong.
4. **Keep the hole.** An unresolvable member stays in the resolved set as an explicit null.
5. **Shallow, top-level overrides.** Predictable beats clever.

**Reject:**

6. **Never silently dedupe.** A duplicate name is the finding, not a nuisance to clean up.
7. **Ship the cycle check.** They had none; §6 already specifies ours.
8. **`fatal: boolean` is not enough severity.** See the block-or-grade question.

**And the strategic reading.** Continue built the object model, the resolver, the registry and the
open-source distribution, and still could not hold a standalone composition layer while the agent
vendors moved into the same space. What they did **not** build is the part we are calling the product:
they resolved a set in order to *run* it, and told the user nothing about whether it held together.
The composition layer was a means; for us it is the end. That is the beginning of an answer to
question 1 — but only the beginning, because "we surface what they discarded" is a feature, and the
question asks why it is a business.
