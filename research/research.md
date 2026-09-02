# Research — the consolidated read

A digest of the whole research phase (2026-08-30 → 2026-09-02), in five sections: competitors,
flows, benchmark, patterns, conclusions.

**What this file is, and what it is not.** It is a *read* — one place to see what the phase found,
with every fact traceable. It is **not** the specification: that is [`CLAUDE.md`](../CLAUDE.md), and
where the two ever disagree, CLAUDE.md wins. It is **not** the sign-off document either: that is
[`research/FINAL.md`](FINAL.md), which records the decisions and the closed questions.
Nothing here is a third list of open questions — the register lives in
[`research/research-plan.md`](research-plan.md) and is currently empty.

**How to read the citations.** Every claim carries a link to the document or capture it came from.
Where a claim has no source in this repository it is marked **`данные не подтверждены`** and nothing
is invented to fill the space. Those marks are load-bearing: they are the honest edge of what was
actually established.

**The evidence base, counted rather than estimated.** 143 image captures, 36 source documents and
7 raw data logs in this folder, besides this digest and its rendered page. Stage 1's 38 are catalogued in
[`research/1-landscape/screens-index.md`](1-landscape/screens-index.md) with sign-in walls
labelled; the rest sit in their stage folders. Two public issue trackers were queried through the
GitHub API, raw results in
[`research/3-pain/_user-pain-issues.json`](3-pain/_user-pain-issues.json).

---

# 1. Competitors

Source for this whole section:
[`research/1-landscape/comparison.md`](1-landscape/comparison.md), built from the products
themselves, with the per-company entries and verified links in
[`research/1-landscape/competitors.md`](1-landscape/competitors.md).

## The matrix — fifteen products on five axes

Cells are condensed; the full text is in
[`comparison.md`](1-landscape/comparison.md). *Audience* — who it is sold to.
*Product base* — its atomic asset. *Key mechanism* — the thing nothing else does. *Trust* — how it
convinces you a unit is safe. *Monetisation* — as publicly presented.

### Hard — same product, same audience

| | Audience | Product base | Key mechanism | Trust | Monetisation |
|---|---|---|---|---|---|
| **Tessl** | Platform/security leadership. Buyer ≠ user | Skill as a versioned registry artifact, pinned to repo + path + commit | Publishing gated by evaluation — a skill ships only after it scores | **Measured.** Composite 93, uplift 1.40×, Quality/Impact %, Snyk scan | Registry free; platform sold to orgs, price undisclosed |
| **Packmind** | Tech leads, engineering managers | A versioned engineering playbook of standards | One source distributed into each agent's format, plus drift detection back | Governance framing; pre-commit violation blocking | Sales-led SaaS, no self-serve surface — **`данные не подтверждены`** (marked *unverified* in source; `app.packmind.com` does not resolve) |
| **Agentman** | Business teams, not developers | Skill as an executable, shareable unit | Visual assembly of skills into a working agent | Compliance badges + four permission tiers. Trust = *you cannot see inside* | Freemium plus plan tiers |
| **Smithery** | Developers wiring agents to tools | MCP server as a hosted, connectable endpoint | Connect once, reuse everywhere — it holds auth and sessions | Score /100, verified badge, usage counts, licence, last-deployed | Registry free, hosting paid. **Now part of Arcade.dev** |
| **Continue Hub** | Individual developers, then teams | A block: model, context, docs, MCP, rule, prompt, data | Compose blocks into a custom assistant | Open source and forkable — trust by inspection | Free OSS core plus hub tiers. **Acquired by Cursor, June 2026; hosted hub switched off** |

Captures: [`skill-detail-scored.png`](1-landscape/screens/hard/tessl/skill-detail-scored.png)
(the reference screen of the survey — composite 93, uplift 1.40×, Quality/Impact/Security bars, repo
+ path + commit) ·
[`server-detail-exa.png`](1-landscape/screens/hard/smithery/server-detail-exa.png) ·
[`acquisition-notice.png`](1-landscape/screens/hard/continue/acquisition-notice.png) ·
[`marketing-home.png`](1-landscape/screens/hard/packmind/marketing-home.png) ·
[`marketing-skills-library.png`](1-landscape/screens/hard/agentman/marketing-skills-library.png).

> **Two of the five hard competitors were never seen as products.** Agentman's catalog is
> login-walled and Packmind is sales-gated; both are marketing pages only. Their mechanisms are read
> from their own writing, not observed. Continue was read **from source** instead —
> [`continue-postmortem.md`](1-landscape/continue-postmortem.md) — which is the only place
> in this survey a competitor is read from its code rather than its claims.

### Soft — different product, same job

| | Audience | Product base | Key mechanism | Trust | Monetisation |
|---|---|---|---|---|---|
| **Backstage** | Platform teams in large orgs | A typed entity declared in YAML in the repo | Relations **derived and filtered, never drawn** — a graph with max-depth and kind filters | Ownership: every entity shows owner, lifecycle, source file | OSS, free |
| **Port** | Platform engineering leadership | Entity in a Context Lake, plus workflows and a Skills Registry | Standards applied as scorecards over the catalog | Scorecards: pass, warn or block, with the reason attached | Self-serve free tier plus enterprise |
| **Terraform** | Infrastructure engineers | A versioned module with declared constraints | `plan` — a legible, itemised dry run before the irreversible step | Version constraints, provider signing, download counts | Registry free; CLI BUSL; HCP paid |
| **Figma** | Designers, design engineers | A component in a library, and its instances | Live link with a deliberate **detach**, plus update propagation | Publisher identity; an instance always names its main component | Seat-based SaaS |
| **Notion** | Knowledge workers | A page, and a template as a duplicatable page | **Duplicate** as the distribution primitive | Creator profiles, usage counts, official gallery | Freemium plus template marketplace |

Captures:
[`catalog-relations-graph.png`](1-landscape/screens/soft/backstage/catalog-relations-graph.png) ·
[`catalog-table.png`](1-landscape/screens/soft/backstage/catalog-table.png) ·
[`port-scorecard-rule-expanded.png`](2-flows/04-validation-check-results/port-scorecard-rule-expanded.png) ·
[`module-dependencies.png`](1-landscape/screens/soft/terraform/module-dependencies.png) ·
[`template-gallery.png`](1-landscape/screens/soft/notion/template-gallery.png).

### Aspirational — the craft benchmark

| | Audience | Product base | Key mechanism | Trust | Monetisation |
|---|---|---|---|---|---|
| **Linear** | Teams that care about craft | An issue in an opinionated workflow | Speed as a feature — keyboard-first, command menu, near-zero latency | Opinion: the product tells you how to work | Seat-based SaaS |
| **Raycast** | Individual power users on macOS | A command; an extension is a bundle of them | Launcher-first — everything one keystroke and a fuzzy search away | Open extension source, author identity, install counts | Free app plus Pro |
| **Vercel** | Frontend engineers | A deployment | The deploy as a designed event with a live build log you actually read | The log itself — every step visible, nothing behind a spinner | Usage-based hosting |
| **Stripe** | Developers integrating payments | An API object with explicit relationships | Documentation as interface — the reference *is* the product | Precision: exhaustive versioned docs, error copy naming the cause | Per-transaction fees |
| **GitHub** | Every developer | A repository | Fork and pull request — copying is a first-class social act | Network effects: stars, contributors, dependency graph | Freemium plus usage |

Captures:
[`vercel-deployment-stages.jpg`](2-flows/04-validation-check-results/vercel-deployment-stages.jpg) ·
[`linear-command-palette-default.jpg`](2-flows/02-library-browse-filter-search/linear-command-palette-default.jpg) ·
[`geist-colors.png`](1-landscape/screens/aspirational/vercel/geist-colors.png) ·
[`api-reference.png`](1-landscape/screens/aspirational/stripe/api-reference.png) ·
[`dependency-graph-nextjs.png`](1-landscape/screens/aspirational/github/dependency-graph-nextjs.png).

> Linear's app, Vercel's dashboard, Stripe's dashboard and Mobbin were captured **login-walled** in
> stage 1 and are stamped as such in
> [`screens-index.md`](1-landscape/screens-index.md). Linear and Vercel were later captured
> from the owner's own signed-in sessions in stage 2. Mobbin was never usable — it 403s
> unauthenticated fetches — so **no pattern-library material came from it**.

## Three market patterns

1. **The composition layer is consolidating, fast.** Of five hard competitors, one had its hosted
   layer switched off (Continue, acquired by Cursor in June 2026 — the Apache-2.0 client survives,
   frozen) and one was acquired *mid-survey* (Smithery is now part of Arcade.dev; the banner was
   found on their own server page, not in any article read). **What got absorbed in Continue's case
   is precise: the registry, the accounts and the subscriptions. The local client and the open format
   were left standing.** Source: [`comparison.md`](1-landscape/comparison.md),
   [`continue-postmortem.md`](1-landscape/continue-postmortem.md), capture
   [`acquisition-notice.png`](1-landscape/screens/hard/continue/acquisition-notice.png).

2. **Trust has moved from social proof to measurement.** Tessl scores every skill on quality, impact
   across *n* eval scenarios and a Snyk security scan, then shows a composite number and an uplift
   multiplier. Smithery shows a score out of 100 and a verified badge. Port shows pass/warn/block.
   **A number derived from *running* the thing has replaced stars and download counts.** Source:
   [`comparison.md`](1-landscape/comparison.md), captures
   [`skill-detail-scored.png`](1-landscape/screens/hard/tessl/skill-detail-scored.png),
   [`tessl-skill-evals-tab.png`](2-flows/01-item-detail-and-trust/tessl-skill-evals-tab.png).

3. **Nobody authors a graph; everybody derives one.** Backstage's Catalog Graph is read-only,
   filtered by depth and relation type, generated from YAML beside the code. Terraform resolves its
   graph from declared constraints. GitHub derives dependents. **Not one product in the survey asks a
   human to draw an edge** — so rejecting the node canvas is the market consensus, not a compromise.
   Source: [`comparison.md`](1-landscape/comparison.md), captures
   [`backstage-graph-depth-1.png`](2-flows/03-relations-without-canvas/backstage-graph-depth-1.png) and
   [`backstage-graph-depth-3.png`](2-flows/03-relations-without-canvas/backstage-graph-depth-3.png)
   (the same graph at two depths — the legibility control).

## Three differences we can hold

1. **Every live hard competitor sells to an organisation; the practitioner is not the buyer.** Tessl
   to security and platform leadership, Packmind to engineering managers, Agentman to business teams,
   Port to platform engineering. The value proposition is always control over *other people's* work —
   governance, drift, compliance. **A personal library that answers to nobody is unoccupied ground.**

2. **They all trust the network; we can trust the file.** Every catalog above solves cold start with
   curation and volume — 17,500 MCP servers, 3,000 skills, 115 business skills. None of them makes
   *your own accumulated material* better. Our unit of value is the user's existing corpus, so we do
   not need a network to be useful on day one.

3. **Assembly is a side effect for them and the whole product for us.** Smithery composes so it can
   host, Tessl so it can govern, Backstage so it can scaffold a repo. **Nobody treats *does this set
   actually hold together* as the product.** The validation pass — dependency walk, conflict,
   collision, missing env — is genuinely unclaimed.

All three: [`comparison.md`](1-landscape/comparison.md).

> **Whether difference 1 is an opportunity or the reason nobody is there is not established.**
> Continue is the single data point and it reads both ways: the hosted, monetised half was switched
> off and erased; the free, local, open half is still installed on 1.58M machines
> ([`continue-postmortem.md`](1-landscape/continue-postmortem.md)). Beyond that —
> **`данные не подтверждены`**.

---

# 2. Flows

Twelve mechanisms captured from live products. Brief, coverage and access notes:
[`research/2-flows/README.md`](2-flows/README.md). Ten closed, one declined, one handed
forward.

| # | Flow | Status | The insight it produced | Source |
|---|---|---|---|---|
| **01** | Item detail and trust | ◐ declined | Trust has moved from social proof to **measurement** — a number derived from running the thing. We can run nothing, so we ship none of it | [`tessl-skill-evals-tab.png`](2-flows/01-item-detail-and-trust/tessl-skill-evals-tab.png), [`tessl-skill-quality-tab.png`](2-flows/01-item-detail-and-trust/tessl-skill-quality-tab.png), [`smithery-server-github-config.png`](2-flows/01-item-detail-and-trust/smithery-server-github-config.png) |
| **02** | Library browse, filter, search | ● closed | Typing **flattens a filter tree into breadcrumbs** — the path is shown, not traversed, which is how two leaves with the same name stay distinguishable. A filter chip is a sentence. And **name how many items are hidden**, never claim there are none: *"4 issues hidden by filters · Clear Filters ✕"* | [`NOTES-linear.md`](2-flows/02-library-browse-filter-search/NOTES-linear.md), [`linear-filtered-to-zero-hidden-count.jpg`](2-flows/02-library-browse-filter-search/linear-filtered-to-zero-hidden-count.jpg), [`linear-filter-typeahead-breadcrumbs.jpg`](2-flows/02-library-browse-filter-search/linear-filter-typeahead-breadcrumbs.jpg) |
| **03** | Relations without a canvas | ● closed | **Nobody authors a graph.** It is derived from declared relations and made legible with a depth filter. GitHub's *Dependents* is the reverse direction — blast radius rather than dependencies | [`backstage-graph-depth-1.png`](2-flows/03-relations-without-canvas/backstage-graph-depth-1.png), [`backstage-graph-depth-3.png`](2-flows/03-relations-without-canvas/backstage-graph-depth-3.png), [`github-dependents-blast-radius.png`](2-flows/03-relations-without-canvas/github-dependents-blast-radius.png) |
| **04** | Validation: pass, warn, block | ● closed | A check is a **stack of stages, each with its own verdict and duration**, expandable. And **Port does not block — it gates a level**: a failed rule stops an entity climbing `Basic → Low → Good → Great` rather than forbidding anything. The demo has no blocking surface at all | [`NOTES-vercel.md`](2-flows/04-validation-check-results/NOTES-vercel.md), [`NOTES-port.md`](2-flows/04-validation-check-results/NOTES-port.md), [`NOTES-github-actions.md`](2-flows/04-validation-check-results/NOTES-github-actions.md), [`terraform-plan-output.md`](2-flows/04-validation-check-results/terraform-plan-output.md), [`vercel-deployment-stages.jpg`](2-flows/04-validation-check-results/vercel-deployment-stages.jpg), [`port-scorecard-rule-expanded.png`](2-flows/04-validation-check-results/port-scorecard-rule-expanded.png) |
| **05** | Linked vs detached, blast radius | ● closed | **Drift is computed precisely and displayed nowhere.** Figma's menu names the exact overridden property — `Reset fill`, not "reset overrides" — yet a modified instance is pixel-identical to a clean one in the layers tree, the properties panel and the canvas. **The failure is display, not modelling.** Also: revert at two granularities, and Reset kept next to Detach as two halves of one axis | [`NOTES.md`](2-flows/05-linked-vs-detached/NOTES.md), [`figma-context-menu-overridden-reset.png`](2-flows/05-linked-vs-detached/figma-context-menu-overridden-reset.png), [`figma-context-menu-clean.png`](2-flows/05-linked-vs-detached/figma-context-menu-clean.png), [`figma-library-updates-instance-counts.png`](2-flows/05-linked-vs-detached/figma-library-updates-instance-counts.png) |
| **06** | Export and target adaptation | ● closed | **One source, many targets** — and external repos are always *instructions*, never vendored. Ruler emits a managed `START/END` fenced block so a re-run replaces exactly what it wrote, and drops a `.bak` beside every overwritten file | [`ruler-per-agent-output.md`](2-flows/06-export-and-target-adaptation/ruler-per-agent-output.md), [`backstage-scaffolder-templates.png`](1-landscape/screens/soft/backstage/scaffolder-templates.png) |
| **07** | Env variables and secrets | ● closed | **Ask the type before the value**, default to the irreversible option (Secret, not Config), and let the placeholder pose the real question — Vercel's note field reads *"Where to rotate, or who to contact"* | [`NOTES.md`](2-flows/07-env-and-secrets/NOTES.md), [`vercel-add-env-variable-drawer.jpg`](2-flows/07-env-and-secrets/vercel-add-env-variable-drawer.jpg) |
| **08** | Empty state and cold start | ● closed | **Answer an empty product with real objects, not an empty state.** A new Linear workspace opens on four *real* issues — editable, completable, deletable — so the model is learned by holding four instances of it. And **three registers of emptiness**: never-used concept → define it; routine → one line; filtered to zero → count what is hidden | [`NOTES-linear.md`](2-flows/08-empty-state-and-cold-start/NOTES-linear.md), [`linear-first-run-seeded-issues.jpg`](2-flows/08-empty-state-and-cold-start/linear-first-run-seeded-issues.jpg), [`linear-projects-empty-state.jpg`](2-flows/08-empty-state-and-cold-start/linear-projects-empty-state.jpg) |
| **09** | Duplicate and fork | ● closed | **Duplication is a distribution primitive**, and the copy dialog states what will and will not come along | [`NOTES.md`](2-flows/09-duplicate-and-fork/NOTES.md), [`github-create-fork-form.jpg`](2-flows/09-duplicate-and-fork/github-create-fork-form.jpg), [`notion-page-menu-duplicate.jpg`](2-flows/09-duplicate-and-fork/notion-page-menu-duplicate.jpg) |
| **10** | Dark design language | → handed forward | Few surfaces with the sidebar sharing the content ground; elevation as a hairline plus a few percent of lightness rather than a shadow ramp; three foreground tones with the accent reserved for meaning; key caps as a real component. **Deliberately not spent in this phase** — it is the one flow about appearance, and it opens the design-system phase | [`NOTES-linear.md`](2-flows/10-dark-design-language/NOTES-linear.md), [`linear-command-palette-dark-detail.png`](2-flows/10-dark-design-language/linear-command-palette-dark-detail.png) |
| **11** | Copy: errors, warnings, refusals | ● closed | **Cause and consequence are two rows**, and you group by the action that fixes a failure, not the check that found it. The anti-reference is industry-wide: 14 of 17 annotations on one run read `Process completed with exit code 1`, and the same was found in `denoland/deno`, `withastro/astro`, `vitejs/vite` and `rust-lang/rust-clippy` | [`ci-failure-copy.md`](2-flows/11-copy-and-error-language/ci-failure-copy.md), [`dependency-conflict-copy.md`](2-flows/11-copy-and-error-language/dependency-conflict-copy.md), [`github-actions-run-failed-annotations.png`](2-flows/04-validation-check-results/github-actions-run-failed-annotations.png) |
| **12** | Visibility and portfolio | ● closed | **Public/private is a low-ceremony decision**, and the profile is the portfolio | [`NOTES.md`](2-flows/12-visibility-and-portfolio/NOTES.md), [`github-danger-zone-visibility.jpg`](2-flows/12-visibility-and-portfolio/github-danger-zone-visibility.jpg), [`notion-publish-to-web.jpg`](2-flows/12-visibility-and-portfolio/notion-publish-to-web.jpg) |

## The four flow findings that changed the specification

1. **Cold start is a product decision, not a demo problem** (flow 08). Linear ships four real
   objects rather than an illustration. → became the public library and the example project,
   [`CLAUDE.md`](../CLAUDE.md) §8 and §11.
2. **The drift indicator is a display problem, not a modelling one** (flow 05). The diff is already
   computed, so putting it on the card costs nothing — and Figma refuses to. → [`CLAUDE.md`](../CLAUDE.md) §7.
3. **There is no prior art for the return path** (flow 05). Figma erases the origin at detach and
   offers nothing afterwards. → our promotion path is an invention, [`CLAUDE.md`](../CLAUDE.md) §5.
4. **An action that cannot act is not shown — on primary surfaces** (flows 05, 08, plus the benchmark's
   correction). Linear suppresses its toolbar over an empty list and recomputes its hint bar; Figma
   hides a reset with nothing to reset; Vercel keeps four filter dropdowns over nothing and is simply
   wrong. → [`CLAUDE.md`](../CLAUDE.md) §6 and §9.

## What the flows could not see

- **Density under load.** Every browse mechanic in flow 02 was captured in a workspace holding
  **four issues**, and the benchmark's Obsidian cell against a **27-note** vault. All of it is
  mechanics; none of it is scale. The claim that our chosen shape survives 300 items is reasoned, not
  observed — **`данные не подтверждены`**.
  ([`README.md`](2-flows/README.md), *the trade, stated plainly*.)
- **Cross-file usage counts.** Figma's *how many other files use this component* — the exact shape of
  our *used in 3 projects* — sits behind a paid tier. Declined.
- **Log bodies on GitHub Actions.** Gated behind a sign-in even on a fully public repository. Step
  structure, glyphs, timings and annotations are public; the deep log reference stays Vercel's.
- **Agentman's permission tiers and Packmind's product.** Never observed —
  **`данные не подтверждены`** beyond their own marketing.

---

# 3. Benchmark

Fifteen cells, four flows, five categories lifted from stages 1–3 so the rubric is grounded rather
than invented. Full scoring and the argument behind every number:
[`research/4-benchmark/benchmark.md`](4-benchmark/benchmark.md).

**The categories.** C1 state legibility · C2 consequence disclosure · C3 failure copy · C4 recovery ·
C5 economy. **The anchors.** 1 actively misleads · 2 the information does not exist · 3 correct but
you must go looking · 4 present where you need it · 5 you could not miss it and it changed what you
did next. `—` is not a zero: it means the flow contains no instance, and the cell always says
whether that is the product's fault or the method's.

| | Candidate | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|---|
| **B1 Find** | Linear ⌘K + filters | **5** | — | 4 | **5** | **5** |
| | GitHub code search | **5** | — | 3 | 3 | 4 |
| | Obsidian quick switcher | 4 | 2 | 2 | **5** | 4 |
| | VS Code palette + Extensions | 4 | — | 2 | 2 | 4 |
| **B2 Assemble** | VS Code workspace extensions + trust | **5** | **5** | — | 4 | 3 |
| | `npm install` | 3 | 4 | **5** | 4 | 4 |
| | Figma instances + library | 2 | 4 | — | 3 | **5** |
| **B3 Check** | `terraform` plan + validate | **5** | **5** | 4 | 4 | **5** |
| | VS Code Problems panel | **5** | — | 4 | 4 | **5** |
| | Vercel build log | **5** | — | — | — | 4 |
| | GitHub Actions run | **5** | — | **1** | 2 | 3 |
| **B4 Produce** | Vercel deploy | **5** | — | — | — | 3 |
| | `create-next-app` | 4 | 4 | — | 2 | 3 |
| | Figma export dialog | 4 | — | 4 | 3 | 3 |
| | Ruler per-agent output | 3 | 2 | — | 4 | 4 |

**Who wins each flow.** B1 — Linear, and not narrowly. B2 — VS Code, on Workspace Trust. B3 —
`terraform`, with VS Code's Problems panel level on everything but the summary line.
**B4 — nobody: the highest cell is a 4.**

## The three mechanisms to take into the MVP

### 1. The run as a stack of stages — Vercel's deployment page

**What it is.** A deployment is a stack of *collapsed stages, each carrying its own glyph, verdict
and duration*, each expandable. A stage that did not run gets a clock, not a failure. The log header
states `66 lines` before you read it, offers `Find in logs`, and a timestamp hover gives **relative
to start** and **relative to previous** — which is how you find the step that hung without doing
arithmetic. Scored **C1 = 5** for B3.

**Why it is right for us.** The validation pass in [`CLAUDE.md`](../CLAUDE.md) §6 is specified as a
designed, legible moment rather than a spinner, and this is that moment's structure, already proven.
It also supplies the home for two things we need and nobody else has a place for: our **Skipped**
severity maps onto Vercel's clock glyph, and the handover disclosure becomes two more stages rather
than a new surface. Terraform reinforces the same discipline from the other side — **no progress
theatre; text that appears when ready and reads correctly frozen**, which is the argument for keeping
our animated sweep subordinate to a result that survives being paused.

**Source.**
[`NOTES-vercel.md`](2-flows/04-validation-check-results/NOTES-vercel.md) ·
[`vercel-deployment-stages.jpg`](2-flows/04-validation-check-results/vercel-deployment-stages.jpg) ·
[`vercel-build-log-timestamp-tooltip.jpg`](2-flows/04-validation-check-results/vercel-build-log-timestamp-tooltip.jpg) ·
[`terraform-plan-output.md`](2-flows/04-validation-check-results/terraform-plan-output.md) ·
[`benchmark.md`](4-benchmark/benchmark.md), B3.

### 2. `N of M`, and a count that is a link — VS Code Workspace Trust

**What it is.** Workspace Trust shows two columns — *In a Trusted Folder* against *In Restricted
Mode* — with the current one outlined and four ✓/✕ lines each. Two of those lines are counted **and
hyperlinked**: *"95 workspace settings are not applied"*, *"10 extensions are disabled or have
limited functionality"*. Scored **C2 = 5**, the best consequence disclosure in the entire benchmark.

**Why it is right for us.** [`CLAUDE.md`](../CLAUDE.md) §6 refuses to block an unclean export and
confirms it instead, which puts the whole weight on the confirmation sentence. This is the shape that
sentence should take: **name the count, and let the user open it.** Figma's *423 instances* is the
same idea one step behind — a count you cannot click, behind a toggle that is off by default.

The same grammar showed up in four unrelated products, which is why it is a mechanism and not a
preference: Linear's *4 issues hidden by filters*; VS Code's *Showing 0 of 6* placed **inside the
filter input**; Figma's *0 of 0 selected*; GitHub's *10 files (324 ms) in `repo ✕`* beside a rail
counting every result type including the zeros. **The number you can act on, next to the control that
produced it** — and never the word "none". Our filtered Library, our selection and our export set all
want this.

**Source.**
[`NOTES-vscode.md`](4-benchmark/NOTES-vscode.md) ·
[`vscode-workspace-trust.png`](4-benchmark/vscode-workspace-trust.png) ·
[`vscode-problems-filtered-zero.png`](4-benchmark/vscode-problems-filtered-zero.png) ·
[`linear-filtered-to-zero-hidden-count.jpg`](2-flows/02-library-browse-filter-search/linear-filtered-to-zero-hidden-count.jpg) ·
[`benchmark.md`](4-benchmark/benchmark.md), findings 4 and 5.

### 3. The failure line written at the altitude that knows the rule — npm `ERESOLVE` and Port

**What it is.** npm's `ERESOLVE` answers all four questions a conflict message owes: what was
**required** (`peer react@"^18.0.0 || ^19.0.0"`), what was **found** (`react@17.0.2`), **who required
it**, and **who asked for what was found** (`from the root project`) — which is exactly our
`addedBy: manual | dependency`. Then both escape hatches with the cost in the same sentence:
*"to accept an incorrect (and potentially broken) dependency resolution."* Scored **C3 = 5**. Port
writes the same shape for a rule: `where "Open Critical Vulnerabilities" = 0 · Value: 1` — the
condition required and the value found.

**Why it is right for us.** The contrast is the whole lesson. GitHub Actions writes `Process
completed with exit code 1` and scored **C3 = 1** — *actively misleads*, because the header counts
*"11 errors and 6 warnings"* and the slot behind the count is empty. **The difference is not writing
quality; it is architecture.** The 5-grade messages are emitted where the requirement is known; the
1-grade one is emitted by a process that only knows it stopped. So this is a decision about our
validator's internals: **the check that knows the rule must be the thing that writes the sentence.**

Two refinements come with it. **Count problems the way the user counts them** — Terraform emitted
four diagnostics for one defect, and VS Code reported a duplicate JSON key as two unjoined rows that
never mention each other. And **a check that could not run must say so**, which is why *Skipped*
exists as a third severity rather than a silently missing row.

**Source.**
[`npm-eresolve.md`](4-benchmark/npm-eresolve.md) ·
[`NOTES-port.md`](2-flows/04-validation-check-results/NOTES-port.md) ·
[`port-scorecard-rule-expanded.png`](2-flows/04-validation-check-results/port-scorecard-rule-expanded.png) ·
[`NOTES-github-actions.md`](2-flows/04-validation-check-results/NOTES-github-actions.md) ·
[`github-actions-run-failed-annotations.png`](2-flows/04-validation-check-results/github-actions-run-failed-annotations.png) ·
[`ci-failure-copy.md`](2-flows/11-copy-and-error-language/ci-failure-copy.md) ·
[`benchmark.md`](4-benchmark/benchmark.md), findings 1 and 2.

## The one that will not work for us — Figma's disabled export

**What it is.** Figma's export dialog with nothing selected reads `0 of 0 selected` beside a **greyed
`Export` button**, with the explanation *"No selected layers have export settings. Click + in the
export section of the properties panel to add one."* It scores respectably — C1 = 4, C3 = 4 — because
the state and the remedy are both stated precisely.

**Why we cannot copy it.** It works in Figma for three reasons, and **we have none of the three**:

| Figma | Us |
|---|---|
| The blocker is **one named action away** | Our Problem may be four items away, in another surface |
| The condition is a property of **this second's selection**, not of the document | Our Problems are properties of the **project** |
| **Re-exporting costs nothing** | The archive **is** the product's whole point |

A greyed primary action is a dead end on the most important control in the product, and the promise
in [`CLAUDE.md`](../CLAUDE.md) §2 is *the system checked*, not *the system forbade*. So the mechanism is
refused outright: **export is never disabled; an unclean set is confirmed, not blocked** (§6).

**A second documented rejection, for completeness.** Port's grade ladder —
`Basic → Low → Good → Great`, where a failed rule gates a level rather than forbidding anything — was
a genuine live alternative and was also rejected, on structural grounds: **a ladder is for comparing
many entities against one standard, and we check one set against itself**, where there is no
*better*, only *coherent* or *not*.

**Source.**
[`NOTES-figma-export.md`](4-benchmark/NOTES-figma-export.md) ·
[`figma-export-empty-selection.png`](4-benchmark/figma-export-empty-selection.png) ·
[`NOTES-port.md`](2-flows/04-validation-check-results/NOTES-port.md) ·
[`benchmark.md`](4-benchmark/benchmark.md), finding 7 · [`CLAUDE.md`](../CLAUDE.md) §6.

## The caveat that governs every score above

**The rubric grades craft, not weight.** The five categories were lifted from stages 1–3, and those
stages surveyed *products*. So every cell answers *did this interface tell me the thing* — and none
answers *does anyone bleed here*. Read the four flows against the pain evidence instead
([`user-pain.md`](3-pain/user-pain.md)) and the weights come out uneven:

| | Flow | What the pain evidence says |
|---|---|---|
| **B1** | Find | A tracker is **structurally blind** — nobody files *I cannot find what I wrote in March*. No evidence of pain, and none of its absence |
| **B2** | Assemble | Same blindness, plus: **nobody is asking for a composition layer** — `reuse blocks assistant` returns **0 results** in a 6,677-issue tracker belonging to a product that shipped one |
| **B3** | Check | Where our thesis is actually sighted: two `server-postgres` entries in one `mcp.json`, *"the chat always chooses the first one specified"* — **13 reactions**. And env/secrets rank near the top of both trackers |
| **B4** | Produce | Where the **loudest pain lives**: **182 reactions** on *MCP Servers Don't Work with NVM*, over a top-of-tracker made of PATH, node version managers, platform paths and processes dying at startup |

**The value is concentrated in B3 and B4; the craft is concentrated in B1 and B2.** Linear, GitHub
and Obsidian are exemplary at a flow nobody files issues about; the flow people shout about is the one
where no candidate scored above 4. **Our wow moment is aimed at the least-well-served flow of the
four** — and the specific gap is *disclosure before the write*.

Sources: [`benchmark.md`](4-benchmark/benchmark.md) finalisation ·
[`user-pain.md`](3-pain/user-pain.md) ·
[`_user-pain-issues.json`](3-pain/_user-pain-issues.json) ·
[issue #64](https://github.com/modelcontextprotocol/servers/issues/64) ·
[issue #1219](https://github.com/modelcontextprotocol/servers/issues/1219).

---

# 4. Patterns

Five radically different shapes for the key flow — **assemble a set → check it → export** — each
answering the same five questions, each scored on the benchmark's rubric read as *does this shape give
the category a natural home*. Full write-up:
[`research/5-patterns/patterns.md`](5-patterns/patterns.md).

| | P1 two-pane drag | P2 command-first | P3 document | P4 wizard | P5 run-centric |
|---|---|---|---|---|---|
| C1 state legibility | 4 | 3 | 4 | 3 | **5** |
| C2 consequence | 3 | 4 | **5** | 4 | **5** |
| C3 failure copy | 3 | **5** | **5** | 4 | **5** |
| C4 recovery | 4 | 4 | 3 | 2 | 4 |
| C5 economy | 2 | **5** | 4 | 2 | **5** |
| Covers **assemble** | ● | ● | ● | ● | ○ |
| Covers **check** | ◐ | ◐ | ● | ● | ● |
| Covers **export** | ◐ | ◐ | ● | ● | ● |
| Fixed constraints | ok | ok | **fails craft bar** | ok | ok |

## The chosen pattern

> **A hybrid, stated as a choice: P2 wins the spine, P5 becomes the check-and-export surface, P3
> donates one mechanism.** Three surfaces in the flow, plus Projects. The seam between P2 and P5 is a
> single control — **Check** — which is the natural boundary anyway.

**Library** (browse, filter, add, edit; two scopes, `My library` and `Public library`) → **Project**
(the set as a list; `⌘K` adds by name; every row carries its own state) → **Run** (entered by Check;
stages with verdicts and durations; **Export is the final stage**, not a button beside the check).

Written into [`CLAUDE.md`](../CLAUDE.md) §8, and confirmed 2026-09-02 when the open questions closed —
no answer added a surface.

## Why this one, for our context specifically

**1. It is the only shape that gets better as the library grows.** P2's palette is indifferent to
list length; a pane is not. P1's drag fails the concrete test — item #250 dragged to a target that may
be scrolled out of view — and every mitigation for that is click-to-add, at which point **P1 has
quietly become P2 with an extra pane**. Our library is meant to hold the user's whole accumulated
corpus, so this is the constraint that does the most work.

**2. It obeys our own economy rule instead of breaking it.** [`CLAUDE.md`](../CLAUDE.md) §6 and §9 both
refuse controls that cannot act — that is why the `visibility` toggle is not shipped. **A library pane
cannot act while a validation pass is running**, so P1 scores C5 = 2 by making half the screen inert at
the product's most important moment. Applying our own rule to our own design is what removed the pane.

**3. It puts the wow moment on a whole surface.** [`CLAUDE.md`](../CLAUDE.md) §2 names the export as the
wow moment and the validation pass as a designed moment rather than a spinner. P5 scores straight 5s on
four categories and **owns both of the two thirds that carry the pain** (B3 and B4 above). Export as
the *final stage* also makes the unclean-export confirmation the next row in a list the user is already
reading, rather than a dialog interrupting a flow.

**4. It renders the six item states once, not twice.** In P1 every item renders as a library row *and*
as a member, so `detached` — a per-project fact — is invisible in the pane where you browse. In P2
every state is a property of one row. P3 donates the precision: because `overrides` is a keyed object,
a detached row can **name the fields that differ**, which is the thing Figma computes and refuses to
draw (flow 05).

**Why the others lost.** P3 is the best-scoring assembly shape and dies outside the scores: nobody is
asking for a composition layer ([`user-pain.md`](3-pain/user-pain.md), finding 4; and the
composition layer is the half of Continue that was switched off), and a product whose main surface is a
text editor makes our custom design system invisible — which [`CLAUDE.md`](../CLAUDE.md) §10 says *is part
of the product's value*. P4 optimises the first run at the cost of every run after it, and is hostile
to duplicating a project to re-tune it — the second supporting moment in §2. P5 alone cannot assemble
anything. P1 loses on the verb it is named after.

## What the choice costs, stated plainly

The hybrid's weakest point is **P2's C1 = 3: with no library pane, you cannot see what you are not
using.** Three things carry that weight, and if all three fail the choice was wrong:

1. the palette opening cold on **related** items — the ones that require, or are required by, what is
   already in the set — rather than on an alphabetical index;
2. the Library being one keystroke away and remembering where you were;
3. per-item usage facts (*used in 3 projects*, *2 items require this*) doing the work a visible pane
   would otherwise do.

Source: [`patterns.md`](5-patterns/patterns.md), *What this costs us, said plainly*.

---

# 5. Conclusions — the gaps, and a hypothesis for each

Each row is something the research **did not establish**, a hypothesis to test against it, and the
section above it comes from. A hypothesis is written as a claim that could be shown false; where there
is no evidence at all in either direction, the row says so.

| # | The gap | Hypothesis | Derives from |
|---|---|---|---|
| **G1** | **Nobody was ever asked anything.** Both trackers are structurally blind to *loss* and to *reassembly cost*; the entire phase read vendors and artefacts, never users. **`данные не подтверждены`** on which pain drives adoption | **Reassembly cost, not loss, is what converts** — a practitioner adopts to stop re-copying the same four files, and finds *searching my own corpus* valuable only afterwards. Falsifiable in five conversations. Note the one weak hint on record: the decision to ship a public library is itself a bet that people want *material*, not that they want to find their own | §3 Benchmark (the weighting caveat) · §2 Flows |
| **G2** | **B4 has no prior art to copy.** No candidate scored above 4, and **not one cell in the matrix scores what a product says about the machine its artefact lands on** — because no candidate has such a surface | **Disclosure before the write is the whole opportunity.** If Run's last stages state what the archive contains and what the receiving machine must still do, the archive-does-not-run pain drops without us running anything on that machine. Falsifiable: if users still hit environment failures at the same rate, the disclosure was theatre | §3 Benchmark (B4, finding 8) |
| **G3** | **The return path has no prior art.** Figma erases the origin at detach and offers nothing afterwards; no product in the survey lets a local override become a first-class object again | **Promotion as a *new* item is safe and *update the original* is not** — because the second spends blast radius on an action taken inside one project. Falsifiable: if users routinely promote and then immediately delete the original, they wanted a merge and we built the wrong verb | §2 Flows (flow 05) |
| **G4** | **Density was never observed.** Flow 02's whole browsing grammar was captured against **four** issues, and the benchmark's Obsidian cell against **27** notes. The 300-item claim behind the chosen pattern is reasoned, not measured — **`данные не подтверждены`** | **The palette holds at 300 items and the failure mode is discovery, not search** — people will find what they can name and stay blind to what they cannot. That is precisely the C1 = 3 cost already accepted, so it is testable the moment a seeded library exists | §4 Patterns (the cost) · §2 Flows (what the flows could not see) |
| **G5** | **The public library does not exist yet.** It is a decision with no content behind it: no items, no verified sources, no composed example project | **A seed of 8–12 items that produces at least one Problem and one Note teaches the product better than 30 clean ones.** Falsifiable on first use: if the first run's six green ticks leave users unable to say what the product is for, the seed was decorative | §1 Competitors (they all solve cold start with volume; we cannot) · §2 Flows (flow 08) |
| **G6** | **Licensing and attribution for redistributed items.** Nothing in this repository covers the terms under which someone else's skill may ship inside our public library — **`данные не подтверждены`** | **Pinned `ref` plus visible provenance is necessary but may not be sufficient.** This needs a licence review before the shelf is built, not a design decision | §1 Competitors · §4 Patterns |
| **G7** | **Two of five hard competitors were never seen.** Agentman is login-walled, Packmind sales-gated; their mechanisms and Packmind's monetisation are **`данные не подтверждены`** | **Neither changes the picture**, because both sell to organisations and difference 1 already covers the whole group. Falsifiable if either turns out to sell to individuals | §1 Competitors |
| **G8** | **Item versioning and history were never observed** (flow 01 declined; Tessl pins a commit but a version *change* was never seen) | **Not needed**: `detached` + `overrides` does the job for our own items, and a pinned `ref` does it for external ones. Falsifiable the first time a user asks *what did this item look like last month* | §2 Flows (flow 01) |
| **G9** | **Our own thesis is real but quiet.** The duplicate-key collision is sighted in the wild with **13 reactions** against **182** for an environmental failure | **Silent breakage is a retention argument, not an acquisition one** — it is what makes the product trusted once adopted, and not what makes anyone try it. That is a positioning claim, and it is the same product either way | §3 Benchmark (the weighting caveat) |

## What is not a gap

Worth stating, so these do not get re-opened by accident:

- **The node canvas.** Rejected on market consensus, not taste — not one of fifteen products asks a
  human to draw an edge (§1, pattern 3).
- **Blocking.** Settled: three severities, export never disabled, an unclean set confirmed (§3, the
  mechanism that will not work).
- **A composition layer.** Two independent signals against it — 0 results in a 6,677-issue tracker,
  and it is the half of Continue that was switched off (§3, weighting caveat; §4).
- **Per-item scores or badges.** The market converged on measured trust and we can measure nothing;
  usage facts from the user's own library instead (§1, pattern 2).
- **Visual direction.** Deliberately not decided here. Flow 10 was handed forward with its material
  gathered (§2).
