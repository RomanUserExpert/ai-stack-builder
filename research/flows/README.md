# Flows to study

Twelve flows, derived from the "what to take" line of every entry in
[`../competitors.md`](../competitors.md). Each one is a folder in here. This file says what the
flow is, why we want it, what we already captured, what is still missing, and what access it needs.

Screenshot paths are relative to [`../screens/`](../screens-index.md).

**Status key.** ● covered · ◐ partially covered · ○ nothing yet.

**Priority.** P1 — blocks a design decision we are about to make. P2 — needed before mockups.
P3 — useful, not blocking.

---

## Access still needed

Nothing here requires a password. The workable route is the Claude in Chrome extension driving the
browser that is already signed in, with site permission granted per domain. Terraform is the one
exception — it is a local CLI install, no account at all.

| What | For which flows | Why it cannot be substituted |
|---|---|---|
| **Figma** — editor access to any file with a component library | 05, 09 | The linked/detached instance model exists nowhere else. Community file pages show the published artifact, not the instance panel, the detach action or the library-update dialog. This is our own data model, and we currently have **zero** captures of it. |
| **Linear** — any workspace | 02, 08, 10 | The marketing site runs product UI, but not the real thing: no ⌘K palette in a populated workspace, no genuine empty state, no real density under load. |
| **Vercel** — any account with one deployed project | 04, 07 | The build log is our single best reference for the validation pass, and it is behind the dashboard. Env-variable UI likewise. |
| **Notion** — any workspace | 09, 12 | The duplicate-into-workspace flow and the share/publish dialog only exist once signed in. |
| **GitHub** — signed-in session | 09, 12 | Fork dialog, repo visibility settings and the profile-as-portfolio view need a session. Public repos alone give us the dependency graph and nothing else. |
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
| **Continue Hub** — switched off | Replace | Its own Apache-2.0 repository. The block schema and the assistant composition format are readable from source; nothing is lost but the visual design. |
| **Vercel build log** — account | Replace, and it may be enough on its own | **GitHub Actions run logs on any public repository.** Fully open, no account: ordered steps, timings, collapsible groups, failure annotations. The lesson — a process running visibly and legibly instead of behind a spinner — is identical and available right now. |
| **Linear app** — account | Replace only if access does not arrive | Dense dark product UIs that are open without login: **play.grafana.org** and **sandbox.sentry.io** (both verified reachable). Neither matches Linear's craft, but both show real density under real data. Granting Linear access is cheaper than this workaround. |
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

## 02 — Library browse, filter, search ◐ P1

**Serves.** Backstage (typed catalog at scale), Tessl and Smithery (registry browse), Raycast
(browsing small units with no chrome), Notion (gallery). Feeds the Library screen.

**Have.**
- `soft/backstage/catalog-table.png` — the closest thing to our Library that exists: Name / System / Owner / Type / Lifecycle / Tags with a filter rail.
- `hard/tessl/registry-discover-categories.png`, `hard/smithery/registry-home.png`, `aspirational/raycast/store-browse.png`, `soft/notion/template-gallery.png`, `soft/terraform/module-browse.png`.

**Missing.**
- Filters actually applied — every capture is the default unfiltered view. We need the narrowed state and the "clear filters" affordance. *(capturable)*
- A no-results state. *(capturable)*
- A command palette open over a populated library — Tessl advertises ⌘K, Linear is the benchmark. *(Tessl capturable; Linear needs an account)*

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

## 04 — Validation: pass, warn, block ◐ P1

**Serves.** Port (scorecards), Terraform (`plan`), Vercel (build log). This is the wow moment, and
it is the thinnest folder relative to its importance.

**Have.**
- `soft/port/governance-users.png` — governance section, but not a scorecard result.

**Missing — all of it.**
- A Port scorecard with a **failing** check: the wording, what it offers you to do next. *(demo is open, needs deeper navigation)*
- Real `terraform plan` output, and separately a real version-conflict error. *(local CLI)*
- A build log, success and failure. *(Vercel needs an account; **GitHub Actions run logs on a public repo are open and teach the same thing** — capture those first)*
- A failing GitHub Actions check with its annotation. *(capturable on a public repo)*

---

## 05 — Linked vs detached, and blast radius ○ P1

**Serves.** Figma, one for one with our `ProjectItem.detached` and `overrides`. **Zero coverage.**
This is the single biggest gap in the research.

**Missing — everything.**
- The instance panel showing a live link to a main component.
- The detach action, and what the object looks like afterwards.
- The "publish library update" dialog listing how many files are affected — the solved blast-radius UI we want to learn from.
- The override indicator, and whatever return path from detached to linked exists.

**Access.** Figma editor. No substitute: this behaviour has no public page.

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

## 07 — Env variables and secrets ◐ P2

**Serves.** Smithery (how required config is presented), and our `needsEnv` plus `.env.example`.

**Have.**
- `hard/smithery/server-detail-exa.png` — but only the trivial case: "no env vars, no API keys".

**Missing.**
- A Smithery server that does require keys, and how it asks. *(capturable)*
- Vercel's environment variables screen. *(account)*
- One dedicated secrets product for comparison — Doppler or Infisical. *(marketing pages are public; capturable)*

---

## 08 — Empty state and cold start ◐ P2

**Serves.** Notion (template gallery as the answer to an empty workspace), Raycast (empty states),
and our known cold-start problem.

**Have.**
- `soft/notion/template-gallery.png`, `soft/notion/template-collection-detail.png`.

**Missing.**
- A genuine first-run empty state from anyone. Every capture we have is of a full system.
- Backstage or Port with an empty catalog — approximable by filtering to zero results. *(capturable)*
- A brand-new Linear workspace. *(account)*

---

## 09 — Duplicate and fork ○ P2

**Serves.** Notion (duplication as distribution), GitHub (fork), and our "duplicate a project"
moment. **Zero coverage.**

**Missing — everything.**
- Notion's duplicate-template flow including the destination picker. *(account)*
- GitHub's fork dialog — what it asks and what it warns about. *(session)*
- Figma's "duplicate to your drafts" from a community file. *(account)*

---

## 10 — Dark design language ◐ P3

**Serves.** Vercel Geist (token structure), Linear (density and typography), Raycast (tone).

**Have.**
- `aspirational/vercel/geist-colors.png`, `hard/tessl/registry-landing.png`, `aspirational/linear/marketing-home.png`, `aspirational/raycast/store-browse.png`.
- Plus a documented extraction of Raycast's tokens (background `#07080a`, surface `#101111`, accent `#FF6363`, Inter + GeistMono, 8px spacing base, radius 2→20px), recorded in [`../comparison.md`](../comparison.md).

**Missing.**
- Geist's typography, materials and grid pages — we only took colour. *(capturable)*
- Linear's real application density under load. *(account, or substitute with Grafana Play / Sentry sandbox)*
- Raycast's desktop app — **obtainable after all**: `winget install raycast` (Windows build, stable since 25 August 2026).

---

## 11 — Copy: errors, warnings, refusals ● P3

**Serves.** Terraform (version-clash copy), Port (block vs warn language), Stripe (error copy).
Feeds every message our validation pass will need to write.

**Have.**
- `aspirational/stripe/api-reference.png`.

**Missing.**
- Stripe's error-codes reference. *(capturable)*
- A real Terraform conflict message. *(local CLI)*
- npm's `ERESOLVE` peer-dependency output — the most familiar dependency-conflict text in existence, and a useful anti-reference. *(reproducible locally)*
- Port's exact wording where a check blocks rather than warns. *(capturable)*

---

## 12 — Visibility and portfolio ◐ P3

**Serves.** GitHub (public/private as a low-ceremony decision, profile as portfolio), Agentman
(permission tiers), and our `visibility` field. **Zero coverage.**

**Missing — everything.**
- GitHub's repository visibility setting and what it warns when you flip it. *(session)*
- A GitHub profile read as a portfolio. *(public, capturable)*
- Notion's share and publish-to-web dialog. *(account)*

---

## What is left, now that the no-account pass is done

Everything reachable without an account has been taken. What remains splits in two.

**Needs access.** Flow 05 (linked vs detached) and flow 09 (duplicate and fork) are still at zero,
and 05 is the one our data model depends on most — Figma is the only source. Beyond those: Linear
for real density and a populated command palette, Vercel for the env-variable screen, Notion and a
GitHub session for the sharing and forking dialogs.

**Needs a decision, not access.** Raycast is installable here but grabs a global hotkey and wants a
sign-in, so it should be a deliberate step rather than part of a sweep. Port's failing-scorecard
state may be reachable by navigating the open demo further; it was not found in this pass.
