# Stage 2 — Flows

Twelve mechanisms captured from live products. Status per flow is in
[`research-plan.md`](../research-plan.md); this file is the brief each capture was made against.

---

## Flows to study

Twelve flows, derived from the "what to take" line of every entry in
[`1-landscape/competitors.md`](../1-landscape/competitors.md). Each one is a folder in here. This file says what the
flow is, why we want it, what we already captured, what is still missing, and what access it needs.

Screenshot paths are relative to [`1-landscape/screens-index.md`](../1-landscape/screens-index.md).

**Status key.** ● covered · ◐ partially covered · ○ nothing yet · → handed forward to the next phase.

**Priority.** P1 — blocks a design decision we are about to make. P2 — needed before mockups.
P3 — useful, not blocking.

---

## Access still needed

Nothing here requires a password. The workable route is the Claude in Chrome extension driving the
browser that is already signed in, with site permission granted per domain. Terraform is the one
exception — it is a local CLI install, no account at all.

| What | For which flows | Why it cannot be substituted |
|---|---|---|
| ~~**Figma**~~ — **done 2026-08-31** | 05, 09 | Captured in the owner's own file, and the library-updates modal supplied by the owner from a paid-team file. Flow closed. |
| ~~**Linear**~~ — **done 2026-09-01** | 02, 08, 10 | Palette, filter grammar and a genuine first-run state all captured in the owner's workspace. The workspace is new, so density under load was not obtainable and is no longer being chased. |
| ~~**Vercel**~~ — **done 2026-08-31** | 04, 07 | Build log, deployment stage list, deployments list, env-variable drawer and env empty state all captured. Read-only; nothing deployed or saved. |
| ~~**Notion**~~ — **done 2026-08-31** | 09, 12 | Share dialog, Publish-to-web tab, page menu and move-destination picker all captured. Nothing published, nothing duplicated. |
| ~~**GitHub**~~ — **done 2026-08-31** | 09, 12 | Fork form, Danger Zone visibility row and the owner's profile captured. The fork form was opened and abandoned, not submitted. |
| ~~**Terraform CLI**~~ — **done 2026-08-31** | 04, 11 | Run from a scratch directory, nothing installed system-wide. Output captured in `04-.../terraform-plan-output.md` and `11-.../dependency-conflict-copy.md`. |
| **Mobbin** — only if a subscription already exists | reference | It 403s unauthenticated and redirects to sign-in. Do not buy one for this; the flows below cover the same ground from the products themselves. |

**Correction — Raycast is not a dead end.** An earlier note in this file said the app was macOS-only
and therefore uncapturable on this Windows machine. That is wrong: Raycast for Windows came out of
beta on 25 August 2026, currently v2.1.2.0, Windows 10+, installable with `winget install raycast`
or from the Microsoft Store. Flow 10 can be closed properly, on this machine, with a local install.

**Cannot be seen at all:** Packmind (sales-gated, `app.packmind.com` does not resolve) and Continue
Hub (switched off). Both have substitutes — see below.

---

## Substitutes for what is closed

Not every gap needs filling, and two of the substitutes are better than the original would have been.

| Closed | Verdict | Substitute |
|---|---|---|
| **Packmind** — sales-gated | Replace | **Ruler**, the open-source CLI that syncs one `.ruler/` directory into 20+ agent formats. Run locally, it produces the actual per-target output — which is the thing we wanted Packmind for. A real format mapping beats a sales-demo screenshot. |
| **Continue Hub** — switched off | **Replaced, and done 2026-09-01** | Read from its Apache-2.0 repository: block schema, the `uses`/`with`/`override` composition primitive, identity and secret schemes, and the resolver. Written up in [`1-landscape/continue-postmortem.md`](../1-landscape/continue-postmortem.md). Only the visual design is lost. |
| **Vercel build log** — account | Replace, and it may be enough on its own | **GitHub Actions run logs on any public repository.** Fully open, no account: ordered steps, timings, collapsible groups, failure annotations. The lesson — a process running visibly and legibly instead of behind a spinner — is identical and available right now. |
| **Linear app** — *access granted, workspace empty* | Substitute only if flow 10 still wants density | Access arrived and closed flows 02 and 08. What it could **not** give is density, because the workspace holds four issues. If real rows are ever needed: **play.grafana.org** and **sandbox.sentry.io**, both open without login. P3. |
| **Figma editor** — account | **No substitute. Access needed.** | The nearest equivalent is **Penpot** (open source, browser-based, has components and detach), but it also requires a free account, so if a Figma login already exists that is the shorter path. Conceptual analogues for base-plus-local-override — Kustomize overlays, `patch-package` — inform the logic but teach us nothing about the interface language. |
| **Notion duplicate / GitHub fork** — session | Partially replaceable | GitHub's **"Use this template"** button is visible on public template repos without a session, and it is the same primitive. The dialog itself, and its warnings, still need a login. |
| **Mobbin** — subscription | **Do not replace.** | We are capturing the products themselves, which is the primary source; Mobbin would be a secondary one. No pattern-library subscription is worth buying for this. |
| **Agentman catalog** — login | Do not replace | Its lesson (permission tiers) is legible from their own marketing, and we already hold three open skill catalogs: Tessl, Smithery's skills section, agentskills.io. |
| **Stripe dashboard** — account | Do not replace | The lesson is object-relationship UI and error copy, and both live in the open documentation we already captured. |

---

## Collected 2026-08-31 — the no-account pass

26 screenshots and 3 written artifacts, gathered without signing into anything. Capture log:
`_flows-capture-log.json`.

| Flow | Added | Still missing |
|---|---|---|
| 01 | Tessl's Quality, **Evals** and Security tabs (the Evals tab shows per-scenario results — 84% with a ↑34% delta on "Contract Redlining and Annotation", each with a Details affordance); two Smithery servers that actually require config; Terraform module versions | Agentman's real skill page *(login)*; a proper version-history surface |
| 02 | Backstage filtered to `type=library` and a genuine no-results state; Tessl's ⌘K palette; Smithery search results; Raycast store with no matches | A command palette over a populated personal library *(Linear)* |
| 03 | Catalog Graph at depth 1 and depth 3 — the legibility control, side by side; GitHub **dependents**, i.e. blast radius rather than dependencies | nothing — flow closed |
| 04 | GitHub Actions workflow-run list and a run detail; Port governance section; **`terraform-plan-output.md`** — real `plan` output on a config that emits a `SETUP.md` and an `.env.example`, with the five mechanics that make it trustworthy | A Vercel build log *(account, but Actions may already cover it)*; a Port scorecard in a failing state |
| 06 | Backstage scaffolder template form; **`ruler-per-agent-output.md`** — the Packmind substitute, run locally | Packmind itself *(no access, and no longer needed)* |
| 07 | Doppler and Infisical product pages | Vercel's env-variables screen *(account)* |
| 10 | Geist typography, materials and grid | Linear's real density *(account)*; Raycast desktop *(installable, see note)* |
| 11 | Stripe error codes; **`dependency-conflict-copy.md`** — real Terraform version-clash, Terraform attribute error and npm `ERESOLVE`, with what to steal and what to avoid in each | Port's exact block-vs-warn wording |
| 12 | GitHub "Use this template" on a public template repo; a GitHub profile read as a portfolio | The visibility-toggle dialog and Notion share dialog *(session)* |

**Flows 05 and 09 got nothing**, as expected — both need Figma, Notion or a GitHub session.

**Raycast was not installed.** It is installable on this machine (`winget install raycast`), but
the app takes over a global hotkey and wants a sign-in for most of its surface, so it sits outside
a "no account, no side effects" pass. Worth doing deliberately, not incidentally.

**Nothing was installed system-wide.** Terraform v1.16.0 was unzipped into a scratch directory and
Ruler ran via `npx`; both worked on throwaway configs outside the repo.

---

## 01 — Item detail and trust ◐ P1

**Serves.** Tessl (item as versioned software), Smithery (config and quality signals in a huge
catalog), Agentman (permission tiers). Feeds our item card and states 1–7.

**Have.**
- `hard/tessl/skill-detail-scored.png` — the reference screen of the whole survey: composite 93, uplift 1.40×, Quality / Impact / Security bars, tabs SKILL.md · Quality · Evals · Security, install command, repo + path + commit.
- `hard/smithery/server-detail-exa.png` — score /100, verified badge, Tools/Resources/Prompts counts, licence, published date.
- `soft/terraform/module-overview-vpc.png`, `aspirational/raycast/extension-detail.png`, `soft/figma/community-file-detail.png`.

**Missing.**
- Tessl's Quality, Evals and Security tabs opened — we only have the default SKILL.md tab. *(open, capturable now)*
- A Smithery server that actually **requires** config; ours is the "no env vars" case. *(capturable)*
- Any version / history surface. Tessl pins a commit; we never saw how a version change is shown. *(capturable)*
- Agentman's real skill page and its four permission tiers. *(login)*

---

## 02 — Library browse, filter, search ● P1 — CLOSED, see [NOTES-linear](02-library-browse-filter-search/NOTES-linear.md)

**Serves.** Backstage (typed catalog at scale), Tessl and Smithery (registry browse), Linear (the
benchmark), Raycast, Notion. Feeds the Library screen.

**Have.**
- `soft/backstage/catalog-table.png` — the closest thing to our Library that exists: Name / System /
  Owner / Type / Lifecycle / Tags with a filter rail, plus a filtered state and a no-results state.
- **Linear's whole browsing grammar** — the `Ctrl K` palette doing commands and content in one field,
  a state-dependent keyboard-hint bar, the no-results row that *is* the next action, the filter picker
  as a typeahead that flattens its hierarchy into breadcrumbs, filter chips written as sentences with
  `Clear` and `Save` side by side, and the filtered-to-zero state that names **how many items are
  hidden**.
- `hard/tessl/registry-discover-categories.png`, `hard/smithery/registry-home.png`,
  `aspirational/raycast/store-browse.png`, `soft/notion/template-gallery.png`.

**The two to copy.** *Typing flattens the filter tree into breadcrumbs* — the path is shown, not
traversed, which is how two leaves with the same name stay distinguishable; our `mcp` kind and an
`mcp` tag will collide exactly like that. And *"4 issues hidden by filters · Clear Filters"* — the
difference between "there is nothing" and "you are not looking at it", stated as a number.

**Not captured, and not expected to be.** Behaviour at scale. The owner's workspace holds four issues,
so everything above is mechanics rather than density. See flow 10.

---

## 03 — Relations without a canvas ● P1 — CLOSED

**Serves.** Backstage (derived, filtered graph), Terraform (declared constraints), GitHub
(dependency graph). This is the market consensus we are betting on: nobody draws edges.

**Have.**
- `soft/backstage/catalog-relations-graph.png` — read-only graph, max-depth / kinds / relations / direction filters, edges labelled `hasPart / partOf`, `ownerOf / ownedBy`.
- `soft/backstage/entity-overview.png`, `soft/terraform/module-dependencies.png`, `aspirational/github/dependency-graph-nextjs.png`.

**Missing.**
- The depth control actually changing the graph — depth 1 vs 3 side by side, which is the legibility mechanism we would copy. *(capturable)*
- The reverse direction: GitHub's "Dependents" view, i.e. blast radius rather than dependencies. *(capturable)*

---

## 04 — Validation: pass, warn, block ● P1 — CLOSED

**Serves.** Port (scorecards), Terraform (`plan`), Vercel (build log), GitHub Actions (a run that
half-worked). This is the wow moment, and it is now the best-covered flow in the research.

**Four notes, four different lessons:**

| Note | Teaches |
|---|---|
| [`04-validation-check-results/terraform-plan-output.md`](04-validation-check-results/terraform-plan-output.md) | What a *result* should read like |
| [`04-validation-check-results/NOTES-vercel.md`](04-validation-check-results/NOTES-vercel.md) | What a *process* should read like |
| [`04-validation-check-results/NOTES-github-actions.md`](04-validation-check-results/NOTES-github-actions.md) | What *partial failure* should read like |
| [`04-validation-check-results/NOTES-port.md`](04-validation-check-results/NOTES-port.md) | What a *grade* should read like |

**Have.** Vercel's stage stack and build log; real `terraform plan` output; a GitHub Actions run of
102 jobs with 7 failed, 4 skipped and 1 cancelled, plus its counted Annotations digest and the PR
Checks tree; Port's scorecard ladder with a failing rule expanded to its predicate and observed value.

**The two findings that decide our design.**

- **Port's `where "Open Critical Vulnerabilities" = 0 · Value: 1`** against **GitHub's
  `Process completed with exit code 1`**. The same event — a check failed — written by someone who
  knew what was required and by someone who did not. Every row of our validation pass takes the
  first form.
- **Port does not block; it gates a level.** The demo has no blocking surface at all. A failed rule
  stops the entity climbing a cumulative `Basic → Low → Good → Great` ladder rather than forbidding
  anything. That is a live alternative to our hard-block / soft-warn binary, and it should be
  settled before the design system, not after.

**Missing.** Nothing blocking. Log *bodies* on GitHub need a sign-in even on a public repository —
the structure, glyphs, timings and annotations are all public, and the deep log reference stays
Vercel's.

---

## 05 — Linked vs detached, and blast radius ● P1 — CLOSED, see [NOTES](05-linked-vs-detached/NOTES.md)

**Serves.** Figma, one for one with our `ProjectItem.detached` and `overrides`.

**Have — all three states.** Clean instance (glyph, purple name, the `From this file` / library
provenance line, component properties); **linked but locally modified**, added 2026-09-01; and
detached. Plus the context menu vocabulary, the library-updates modal, and its per-row instance counts
(5, 2, 70, **423**).

**The finding, corrected twice and now settled.** Figma models drift precisely — the reset menu names
the exact overridden property, `Reset fill`, not a generic "reset overrides" — and then **never shows
it**. A modified instance is pixel-identical to a clean one in the layers tree, the properties panel
and the canvas. The only evidence is two rows appearing in a `…` menu you have to open on an object
you have to select. **The failure is display, not modelling**, and it is the exact trap our state 7
(*detached, locally modified*) is waiting to fall into.

Two things to take whole: **revert at two granularities** (whole instance, single property), and
**Reset next to Detach** as the two halves of one axis — one discards the overrides and keeps the
link, the other discards the link and keeps the overrides.

**Missing — and it stays missing.** The **cross-container** count: how many other *files* use a
component. That is the shape of our *"used in 3 projects"*, and it lives in Figma's library analytics
on a paid tier. Declined.

**And the part with no prior art at all:** a path back from detached to linked. Figma can undo
overrides while still linked, and offers nothing once the link is cut. Our return path is an
invention, not a copy.

---

## 06 — Export and target adaptation ● P2

**Serves.** Backstage (template → scaffold), Packmind (one source, many agent formats), Tessl
(install command). Feeds the Result screen and the archive.

**Have.**
- `soft/backstage/scaffolder-templates.png` — the template list, i.e. the entry point.

**Missing.**
- The scaffolder wizard end to end: parameter form → review step → what it hands you at the end. That whole sequence is our export flow in another domain. *(demo is open, capturable)*
- Tessl's install-command switcher (npm / pnpm / other) — the small "adapt to your target" affordance. *(capturable)*
- Packmind's one-source-many-targets screen. *(no access; work from their public writing instead)*

---

## 07 — Env variables and secrets ● P2 — see [NOTES](07-env-and-secrets/NOTES.md)

**Serves.** Smithery (how required config is presented), and our `needsEnv` plus `.env.example`.

**Have.**
- `hard/smithery/server-detail-exa.png` — but only the trivial case: "no env vars, no API keys".

**Missing.**
- A Smithery server that does require keys, and how it asks. *(capturable)*
- Vercel's environment variables screen. *(account)*
- One dedicated secrets product for comparison — Doppler or Infisical. *(marketing pages are public; capturable)*

---

## 08 — Empty state and cold start ● P2 — CLOSED, see [NOTES-linear](08-empty-state-and-cold-start/NOTES-linear.md)

**Serves.** Notion (template gallery as the answer to an empty workspace), Linear (a real first run),
Vercel (two honest empty states), and our known cold-start problem in CLAUDE.md §11.

**Have.**
- **A genuine first-run workspace at last.** The owner's Linear turned out to be new, so this is the
  real first five minutes rather than a reconstruction.
- Linear's **three registers of emptiness** — a never-used concept that defines itself, routine
  emptiness that says one line, and filtered-to-zero that counts what is hidden.
- `vercel-env-vars-empty-state.jpg`, `vercel-project-overview-checklist.jpg`,
  `soft/notion/template-gallery.png`.

**The finding that changes our plan.** Linear does not answer an empty workspace with an empty state.
It answers it with **four real issues** — `Get familiar with Linear`, `Set up your teams`,
`Connect your tools`, `Import your data` — ordinary objects you can edit, complete or delete. The
onboarding checklist *is* the data model, exercised on itself, and the product is never empty at any
point. CLAUDE.md §11 currently plans ~30 demo items for mockups; this argues for shipping a small
number of **real** Items in a real Project on first run, so the validation pass has something to run
on before the user types anything.

**Second finding.** Verbosity scales with the chance the reader does not know what the object is.
`Projects` defines itself in a sentence; `My issues` says *"No issues assigned to you"* and stops. We
need one written definition per object — `Item`, `Project`, and each of the six kinds.

**Third.** Linear suppresses the toolbar over an empty screen; Vercel keeps a search box and four
filter dropdowns filtering nothing. Same situation, opposite decision — see
[`07-env-and-secrets/NOTES.md`](07-env-and-secrets/NOTES.md).

---

## 09 — Duplicate and fork ● P2 — see [NOTES](09-duplicate-and-fork/NOTES.md)

**Serves.** Notion (duplication as distribution), GitHub (fork), and our "duplicate a project"
moment. **Zero coverage.**

**Missing — everything.**
- Notion's duplicate-template flow including the destination picker. *(account)*
- GitHub's fork dialog — what it asks and what it warns about. *(session)*
- Figma's "duplicate to your drafts" from a community file. *(account)*

---

## 10 — Dark design language → handed to the design-system phase

**Not an open research gap.** This is the one flow in the twelve that is about *appearance* rather
than *behaviour*, and CLAUDE.md §12 postpones visual direction until after research, with §1 putting
the design system next. So flow 10 does not close here — it **opens the next phase**, with its
material already gathered.

**What is already in hand for that phase.**
- **Geist** — colour, typography, materials and grid: the token structure to argue against.
- **Linear's dark theme at close range** ([NOTES-linear](10-dark-design-language/NOTES-linear.md)) —
  few surfaces with the sidebar sharing the content ground, elevation as a hairline plus a few percent
  of lightness rather than a shadow ramp, three foreground tones with the accent reserved for meaning,
  key caps as a real component with a two-cap form for chords, and unset properties written as
  imperatives.
- **Raycast's tokens**, extracted and recorded in [`1-landscape/comparison.md`](../1-landscape/comparison.md): background
  `#07080a`, surface `#101111`, accent `#FF6363`, Inter + GeistMono, 8px spacing base, radius 2→20px.
- Plus every dark product surface captured across the other eleven flows.

**Raycast desktop — declined.** The install was left as an open decision for a fortnight; it is now
closed as *not worth it*. The reasoning that matters is behavioural, not visual: Raycast's one UX idea
is **the launcher instead of a screen** — no windows, no navigation, everything a command, every
destination one keystroke away. The question it would answer for us is whether the Library is a screen
or a palette. **We already have that answer from elsewhere**: Linear's `Ctrl K` doing commands and
content in one field, and Tessl's ⌘K over a typed catalog. Installing Raycast would add tone, not
mechanism, and it costs a global hotkey and a sign-in on the owner's machine.

**Density under load — declined**, and unobtainable regardless: the Linear workspace we were given is
new. `play.grafana.org` and `sandbox.sentry.io` remain open without a login if the design-system phase
ever wants real rows.

---

## 11 — Copy: errors, warnings, refusals ● P3 — CLOSED

**Serves.** Terraform (version-clash copy), Port (rule wording), Stripe (error copy), GitHub (failure
copy, good and bad). Feeds every message our validation pass will write.

**Have.**
- [`11-copy-and-error-language/dependency-conflict-copy.md`](11-copy-and-error-language/dependency-conflict-copy.md) — real
  Terraform version-clash, a Terraform attribute error and npm `ERESOLVE`, with what to steal and
  what to avoid in each.
- [`11-copy-and-error-language/ci-failure-copy.md`](11-copy-and-error-language/ci-failure-copy.md) — the failure channel:
  GitHub's empty annotation as the anti-reference, the three annotations that do work, and the bot
  comment that is the best failure copy in the survey.
- `stripe-error-codes.png`.

**The reference to copy.** A bot posts a distilled failure report *into the PR*, grouped by the
command that reproduces each failure, stamped with the commit, naming each failing test in full, with
`(job)` and `(DD)` links out and the raw output collapsed. Nobody opens a 102-job run to find seven
red squares — so the report goes to the reader instead.

**The sentence to copy.** An automated reviewer's one-line explanation:
*"`baseHints ||=` short-circuits and drops the `ShouldAttemptStaticPrefetch` bit when both
static-attempt flags are true, so PPR-strategy prefetches of fully-static routes deopt to runtime."*
Mechanism, condition, consequence — no severity word, attached to the four lines it is about.

**The anti-reference, and it is industry-wide.** Fourteen of seventeen annotations on the run read
`Process completed with exit code 1`, and a sweep of `denoland/deno`, `withastro/astro`, `vitejs/vite`
and `rust-lang/rust-clippy` found the same in every one. The failure channel carries less information
than the deprecation channel.

**Missing.** Port's block-vs-warn wording, because **Port has no blocking state** — see
[`04-validation-check-results/NOTES-port.md`](04-validation-check-results/NOTES-port.md). The item is answered, not outstanding.

---

## 12 — Visibility and portfolio ● P3 — see [NOTES](12-visibility-and-portfolio/NOTES.md)

**Serves.** GitHub (public/private as a low-ceremony decision, profile as portfolio), Agentman
(permission tiers), and our `visibility` field. **Zero coverage.**

**Missing — everything.**
- GitHub's repository visibility setting and what it warns when you flip it. *(session)*
- A GitHub profile read as a portfolio. *(public, capturable)*
- Notion's share and publish-to-web dialog. *(account)*

---

## Collected 2026-08-31 — the account pass

The owner granted access to their signed-in browser: Figma, Notion and GitHub. 15 further captures
and three written notes. **Nothing was created, published, submitted or left changed.**

| Flow | Added | Handling |
|---|---|---|
| 05 | The whole linked/detached model from a real component library: instance selected and linked, the right-panel provenance line "From this file", the context menu with Reset / Detach / Main component, the detached result, and the restored state. See [NOTES](05-linked-vs-detached/NOTES.md). | The detach was undone immediately with Ctrl+Z and the restored state photographed as proof. |
| 09 | GitHub's "Create a new fork" form and Notion's duplicate menu item and move-destination picker. See [NOTES](09-duplicate-and-fork/NOTES.md). | The fork form was opened and abandoned; the picker was cancelled with Escape. |
| 12 | Notion's Share and Publish-to-web dialogs, GitHub's Danger Zone visibility row, and the owner's own profile beside a heavily used public one. See [NOTES](12-visibility-and-portfolio/NOTES.md). | Read-only. Nothing in the Danger Zone was clicked. |

**The one finding worth carrying into design:** Figma keeps *no* record of where a detached instance
came from. Title reverts to "Frame", the provenance line and the component properties vanish, and
there is no way back. Our model — a detached `ProjectItem` that keeps `itemId`, shows "modified from
library version" and offers a return path — is therefore a **correction of Figma, not a copy of it**.
Design it deliberately; there is no prior art for the *return path*. Blast-radius counting, by
contrast, does have prior art — see the correction below.

**The library-updates modal is now covered too** — the owner supplied it from a file on a paid team,
which the Free-plan file could not show. Figma groups updates by publish event, offers accept-one
and accept-all, and explains structural changes in words.

**Correction, made 2026-08-31 after the owner sent a second capture:** an earlier version of this
line said Figma never states how many instances an update will touch. It does — the count sits on
each row (5, 2, 70, **423 instances**), and it appears when the *"Show updates for all pages"*
toggle is on. Read with the toggle off, the panel shows no numbers, which is what I had seen. The
coupling is the lesson: the count appears exactly when the action reaches beyond what you can see.
What remains uncovered here is the **cross-container** number — how many other *files* use a
component — which is the shape of our *"used in 3 projects"*.

---

## Collected 2026-08-31 — the Vercel pass

Owner's signed-in Vercel (`portfolio-react`). Read-only: no deployment triggered, no rollback, no
setting saved; the add-variable drawer was opened and closed.

| Flow | Added |
|---|---|
| 04 | Deployments list with per-run duration; the deployment page as a **stack of collapsed stages each carrying its own glyph and duration** — the structural model for our validation pass; the build log with its "66 lines" header, in-log search, ASCII route tree with a counted `[+9 more paths]` truncation, and a timestamp tooltip giving **relative to start** and **relative to previous**. See [NOTES-vercel](04-validation-check-results/NOTES-vercel.md). |
| 07 | The Add Environment Variable drawer: **Secret vs Config** as two explained radio cards with the irreversible one as default, a Note field whose placeholder is *"Where to rotate, or who to contact"*, a value reveal toggle, and two bulk paths (`Import .env`, paste a whole `.env` into the Key field). See [NOTES](07-env-and-secrets/NOTES.md). |
| 08 | Two genuine empty states at last — the env-variables empty state, and the project overview's `Production Checklist 4/5`. |

---

## Collected 2026-09-01 — the failing-state pass

Everything the plan listed as *needs no access* except the Figma item. Anonymous, read-only: nothing
signed into, nothing re-run, nothing commented on, nothing saved.

| Flow | Added | Source |
|---|---|---|
| 04 | A GitHub Actions run of **102 jobs — 7 failed, 4 skipped, 1 cancelled** — with four distinct glyphs, a counted **"11 errors and 6 warnings"** annotations digest, a failed job reporting `failed … in 14m 6s`, its full step list (including a `BACKGROUND` step badge), and the PR Checks tree grouped by workflow *and trigger*. See [NOTES-github-actions](04-validation-check-results/NOTES-github-actions.md). | `vercel/next.js` run 33473495683, public |
| 04 | Port's scorecards in a **failing** state: the cumulative `Basic → Low → Good → Great` rail, tiers showing `0/2` beside an orange count of what is unmet, and a rule expanded to `where "Open Critical Vulnerabilities" = 0 · Value: 1`. Plus the by-scorecard and by-rule projections of the same data. See [NOTES-port](04-validation-check-results/NOTES-port.md). | `demo.port.io`, open |
| 11 | The failure channel: GitHub's empty annotation as an anti-reference **verified across five repositories**, the three annotations that carry real information, the bot comment that is the best failure copy in the survey, and an automated reviewer's mechanism-condition-consequence sentence. See [ci-failure-copy](11-copy-and-error-language/ci-failure-copy.md). | same PR, public |

**Two answers, not just captures.**

- *"A scorecard in a blocking state, and its wording"* — **Port has no blocking state.** A failed rule
  gates a level, it does not forbid an action. The item is answered rather than outstanding, and it
  hands us a real alternative to our hard-block / soft-warn binary.
- *"Log annotations"* — GitHub's are content-free by construction, because the annotation is emitted
  by the process that noticed the failure, not the one that caused it. That is a trap our validation
  pass can fall into verbatim.

**One thing turned out to be gated.** Log *bodies* on GitHub Actions require a sign-in even on a fully
public repository (*"Sign in to view logs"*). Step structure, glyphs, timings and annotations are all
public. The deep log reference therefore stays Vercel's.

---

## Collected 2026-09-01 — the Linear pass

The owner granted their signed-in Linear (`romanovcharenko`, team ROM). 16 captures and three notes.
**Nothing was created, edited, assigned, completed or deleted.** One account setting — the interface
theme — was changed with explicit agreement to capture flow 10, then restored to its original value
(`System preference`) and verified.

**The workspace turned out to be brand new: four onboarding issues and nothing else.** That inverted
what this pass could deliver.

| Flow | Added | Status |
|---|---|---|
| 02 | The `Ctrl K` palette running commands and content search in one field, with a *"Search entire workspace"* escalation row; a keyboard-hint bar computed from the current state; a no-results row that **is** the next action; the filter picker as a typeahead that flattens its tree into **breadcrumbs**; filter chips written as sentences with `Clear` and `Save` in the same corner; and the filtered-to-zero state naming **"4 issues hidden by filters"**. See [NOTES-linear](02-library-browse-filter-search/NOTES-linear.md). | ● closed |
| 08 | A **genuine first-run workspace** — the gap this research has carried from the beginning. Linear answers an empty product with four *real* issues rather than an empty state, and carries three distinct registers of emptiness. See [NOTES-linear](08-empty-state-and-cold-start/NOTES-linear.md). | ● closed |
| 10 | Linear's dark language at close range: few surfaces, hairlines instead of a shadow ramp, three foreground tones, key caps as a component, unset properties as imperatives. See [NOTES-linear](10-dark-design-language/NOTES-linear.md). | ◐ |

**The trade, stated plainly.** An empty workspace cannot show density under load, so flow 10 does not
get the thing it most wanted from Linear and is not going to. In exchange flow 08 got something no
populated system could have given: the real first five minutes.

**The finding that reaches back into the product spec.** CLAUDE.md §11 treats cold start as a demo
problem — "~30 realistic items for any mockup". Linear treats it as a product decision: seed the
workspace with real, editable objects so the system is never empty and the user learns the model by
holding four instances of it. For us that means shipping a small starter set of genuine Items in a
genuine Project, so the **validation pass runs before the user has typed anything** — which is the
wow moment, delivered on first launch.

---

## Collected 2026-09-01 — the Figma override state

Supplied by the owner from their own file, closing the last gap that needed no new access: an
instance **linked but locally modified**, beside a clean one, and the `…` menu on each.

| Flow | Added | Status |
|---|---|---|
| 05 | The third instance state. Clean and overridden are **indistinguishable** in the layers tree, the properties panel and on the canvas; the only evidence of drift is two rows appearing in the `…` menu — **`Reset instance`** and **`Reset fill`**. Figma therefore knows exactly which property differs and simply never displays it. See [NOTES](05-linked-vs-detached/NOTES.md). | ● fully closed |

**Why it matters more than it looks.** Our state 7 — *detached, locally modified* — is the state
CLAUDE.md §7 warns is easiest to forget. Figma models it correctly and draws it nowhere, which is the
precise failure mode to design against: the diff is already computed, so putting it on the card costs
nothing. Also worth taking: **revert at two granularities** (whole item, single field), and Reset kept
adjacent to Detach as the two halves of one axis.

**A rule now confirmed three times to one.** The reset rows are *absent* on a clean instance, not
greyed out — same instinct as Linear recomputing its keyboard-hint bar and suppressing the toolbar over
an empty screen, against Vercel keeping four filter dropdowns over an empty list. Treat it as settled:
**an action that cannot do anything is not shown.**

---

## What is left

**Nothing that needs access, and nothing that needs collecting.**

| | |
|---|---|
| **Flows 02–09, 11, 12** | ● closed |
| **Flow 01** | ◐ — held open only by Agentman's login-walled skill page. **Declined.** Its lesson (permission tiers) is legible from their marketing, three open skill catalogs are already captured, and the other gap — a version-history surface — is out of MVP scope per CLAUDE.md §9 |
| **Flow 10** | → **handed to the design-system phase**, not outstanding. It is the one flow about appearance rather than behaviour, and CLAUDE.md §12 postpones visual direction until after research |

**Raycast: declined**, on behavioural grounds. Its one UX idea is the launcher instead of a screen,
and the question it would answer — *is the Library a screen or a palette?* — is already answered by
Linear's `Ctrl K` and Tessl's ⌘K. Tone, not mechanism, for the price of a global hotkey and a sign-in.

**Also declined and settled:** Figma's cross-file usage count (paid tier), Linear's density under load
(the workspace granted is new), Packmind and Continue Hub (substituted by Ruler and the Continue
repository), Mobbin (not worth a subscription). Full reasoning in
[`research-plan.md`](../research-plan.md).

---

## What the twelve flows actually produced

The phase was about **behaviour, not appearance**. The mechanisms worth carrying forward, one line
each:

| Flow | The mechanism |
|---|---|
| 01 | Trust has moved from social proof to measurement — a number derived from *running* the thing |
| 02 | Typing flattens a filter tree into a path; a filter chip is a sentence; **name how many items are hidden**, never claim there are none |
| 03 | Nobody authors a graph. It is derived from declared relations and made legible with a depth filter |
| 04 | A check is a stack of stages, each with its own verdict and duration — and Port gates a *level* rather than blocking anything |
| 05 | Drift is computed precisely and displayed nowhere; revert belongs at two granularities; the return path has no prior art |
| 06 | One source, many targets; external repos are always instructions, never vendored |
| 07 | Ask the type before the value, default to the irreversible one, and let the placeholder pose the real question |
| 08 | Answer an empty product with **real objects**, not an empty state; scale the explanation to how new the concept is |
| 09 | Duplication is a distribution primitive, and the copy dialog states what will and will not come along |
| 10 | *(appearance — next phase)* |
| 11 | Cause and consequence are two rows; group by the action that fixes it, not the check that found it |
| 12 | Public/private is a low-ceremony decision, and the profile is the portfolio |
