# Comparison — fifteen products on five axes

Companion to [`competitors.md`](competitors.md). Built 2026-08-31 from the products themselves:
38 screen captures in [`screens/`](screens-index.md), plus page reads of the sites.

**Axes.** *Audience* — who it is sold to. *Product base* — what the product is actually made of,
its atomic asset. *Key mechanism* — the thing it does that nothing else does. *Trust* — how it
convinces you a unit is safe to use. *Monetisation* — how it charges.

Monetisation is recorded as publicly presented. Cells marked *(unverified)* were not confirmed
from a pricing page in this pass.

---

## Hard — same product, same audience

| | Audience | Product base | Key mechanism | Trust | Monetisation |
|---|---|---|---|---|---|
| **Tessl** | Platform, security and engineering leadership. Buyer ≠ user. | A skill as a versioned registry artifact, pinned to repo + path + commit. | Publishing gated by evaluation: a skill ships only after it scores. | **Measured, not social.** Composite score (93), uplift multiplier (1.40×), Quality %, Impact % across *n* eval scenarios, Security scan by Snyk with pass/fail. | Registry free to browse; platform sold to orgs, price not disclosed. |
| **Packmind** | Tech leads and engineering managers in enterprises. | A "living, versioned engineering playbook" of standards. | One source distributed into each agent's native format, plus drift detection back. | Governance and compliance framing; pre-commit violation blocking. | Sales-led SaaS. No self-serve product surface at all. *(unverified)* |
| **Agentman** | Business teams, not developers — marketing, M&A, healthcare, legal. | A skill as an executable, shareable unit of "how our people do this". | Visual assembly of skills into a working agent. | Compliance badges (HIPAA, SOC2, ISO 27001) plus four permission tiers: use-only / read / edit / admin. Trust = *you cannot see inside*. | Freemium: "Start Building Free" plus plan tiers. |
| **Smithery** | Developers wiring agents to tools. | An MCP server as a hosted, connectable endpoint. | Connect once, reuse everywhere: it holds auth, credentials and sessions. | Quality score /100, verified badge, usage counts, licence, last-deployed date. Trust = popularity + a number. | Registry free; hosting and Toolbox paid. **Now part of Arcade.dev.** |
| **Continue Hub** | Individual developers, then teams. | A block: model, context, docs, MCP server, rule, prompt, data. | Compose blocks into a custom assistant. | Open source and forkable — trust by inspection. | Free OSS core plus hub tiers. **Acquired by Cursor, June 2026: the hosted hub is switched off and user data deleted; the Apache-2.0 client survives, frozen.** |

## Soft — different product, same job

| | Audience | Product base | Key mechanism | Trust | Monetisation |
|---|---|---|---|---|---|
| **Backstage** | Platform teams inside large engineering orgs. | A typed entity in a catalog, declared in YAML in the repo. | Relations are **derived and filtered, never drawn**: a Catalog Graph with max-depth, kind and relation filters. | Ownership. Every entity shows an owner, a lifecycle stage and a source file you can open. | OSS, free. Monetised through Spotify Portal and IDP vendors. |
| **Port** | Platform engineering leadership; now pitching "Agentic-SDLC". | An entity in the Context Lake, plus workflows, self-service actions and a Skills Registry. | Standards applied as scorecards over the catalog, with governed self-service actions. | Scorecards: a check either passes, warns or blocks, with the reason attached. Role-scoped views. | Self-serve free tier plus enterprise sales ("Sign up free" / "Get a demo"). |
| **Terraform** | Infrastructure engineers. | A module or provider, versioned, with declared constraints. | `plan` — a legible, itemised dry run before the irreversible step. | Version constraints, provider signing, publisher namespace, download counts. | Registry free; CLI open (BUSL since 2023); HCP Terraform paid. |
| **Figma** | Designers and design engineers. | A component in a library, and its instances in files. | Live link with a deliberate **detach**, plus library-update propagation across files. | Publisher identity and library provenance; an instance always names its main component. | Seat-based SaaS. |
| **Notion** | Everyone; knowledge workers. | A page/database, and a template as a duplicatable page. | **Duplicate** as the distribution primitive — the gallery solves the empty workspace. | Creator profiles, usage counts, an official gallery with paid and free templates. | Freemium seats; template marketplace on top. |

## Aspirational — the benchmark

| | Audience | Product base | Key mechanism | Trust | Monetisation |
|---|---|---|---|---|---|
| **Linear** | Product and engineering teams that care about craft. | An issue, in an opinionated workflow. | Speed as a feature: keyboard-first, command menu, near-zero latency. | Opinion. The product tells you how to work (the Linear Method) and is trusted for it. | Seat-based SaaS with a free tier. |
| **Raycast** | Individual power users on macOS. | A command; an extension is a bundle of commands. | Launcher-first: everything is one keystroke and a fuzzy search away. | Open extension source, author identity, install counts, review before store listing. | Free app, Pro subscription, team plans. |
| **Vercel** | Frontend engineers. | A deployment. | The deploy as a designed event, with a live build log you actually read. | The log itself: every step visible, failures legible, nothing hidden behind a spinner. | Usage-based hosting; Geist published free. |
| **Stripe** | Developers integrating payments. | An API object with explicit relationships. | Documentation as interface — the reference *is* the product surface. | Precision. Exhaustive, honest, versioned docs; error copy that names the cause. | Per-transaction fees. |
| **GitHub** | Every developer. | A repository. | Fork and pull request — copying is a first-class, social act. | Network effects: stars, contributors, visible history, dependency graph. | Freemium seats plus usage (Actions, storage). |

---

## Three market patterns

1. **The composition layer is consolidating, fast.** Of five hard competitors, one has had its hosted
   layer switched off (Continue, acquired by Cursor in June 2026 — the Apache-2.0 client survives,
   frozen) and one has been acquired mid-survey (Smithery is now part of Arcade.dev — we found the
   banner on their own server page, it was not in any article we read). Standalone "assemble your AI
   building blocks" businesses are being absorbed by the agent vendors and the tool-infrastructure
   players on either side. **Note precisely what got absorbed in Continue's case: the registry, the
   accounts and the subscriptions. The local client and the open format were left standing.**

2. **Trust has moved from social proof to measurement.** Tessl scores every skill on quality,
   impact across eval scenarios and a Snyk security scan, then shows a composite number and an
   uplift multiplier. Smithery shows a score out of 100 and a verified badge. Port shows
   pass/warn/block. Stars and download counts are no longer the trust story — a *number derived
   from running the thing* is.

3. **Nobody authors a graph; everybody derives one.** Backstage's Catalog Graph is read-only,
   filtered by depth and relation type, generated from YAML that lives next to the code. Terraform
   resolves the graph from declared constraints. Not one product in this survey asks a human to
   draw edges. Our decision to reject the node canvas is the market consensus, not a compromise.

## Three differences we can hold

1. **Every live hard competitor sells to an organisation; the practitioner is not the buyer.**
   Tessl sells to security and platform leadership, Packmind to engineering managers, Agentman to
   business teams, Port to platform engineering. The value proposition is always control over
   *other people's* work: governance, drift, compliance, standards enforcement. A personal library
   that answers to nobody is unoccupied ground.

2. **They all trust the network; we can trust the file.** Every catalog above solves cold start
   with curation and volume — 17,500 MCP servers, 3,000 skills, 115 business skills. None of them
   makes your own accumulated material better. Our unit of value is the user's existing corpus,
   which means we do not need a network to be useful on day one.

3. **Assembly is a side effect for them and the whole product for us.** Smithery composes so it
   can host. Tessl composes so it can govern. Backstage composes so it can scaffold a repo. Nobody
   treats "does this set actually hold together" as the product. The validation pass — dependency
   walk, conflict, collision, missing env — is genuinely unclaimed.

## Three decisions the design system needs

Rewritten 2026-09-01. An earlier version of this section asked three strategic questions —
*is there a business, what is our answer to Continue, is single-user only a wedge*. Those were the
wrong shape: CLAUDE.md §9 has already made the scope decisions, and research does not answer whether
a project is worth doing. What is genuinely undecided is narrower, and each item below has a concrete
cost if it is decided late.

**The strategic context, recorded but not blocking.** Every live hard competitor sells to an
organisation — Tessl to security and platform leadership, Packmind to engineering managers, Agentman
to business teams, Port to platform engineering. The individual practitioner is unoccupied ground.
Continue is the single data point on whether that ground pays, and it reads both ways: its hosted,
monetised half was switched off and erased, and its free, local, open half is still installed on 1.58M
machines. See [`continue-postmortem.md`](continue-postmortem.md). **None of this changes what the MVP
is.** It is the same product under either answer, which is why it is context here and not a question.

---

### Decision 1 — does `visibility` appear in the MVP interface?

**The field is settled; the control is not.** CLAUDE.md §9 says `visibility` "exists in the model and
in the UI's vocabulary" and is "designed for, not wired up". That leaves the actual screen ambiguous.

| Option | Consequence |
|---|---|
| **Hide it. Keep the field.** | Nothing in the UI lies. Retrofitting the control later means finding a home for it in a finished layout. |
| **Show it with an honest empty state** — a private/public control that says there is nowhere to publish yet | Teaches the vocabulary early and reserves the space. Costs a control that cannot act. |
| Show it as a working toggle | Rejected. It would be a lie. |

**Recommendation: hide it, keep the field.** Three products in this survey against one settled the
principle — Linear recomputes its keyboard hints and suppresses the toolbar over an empty screen,
Figma shows `Reset` only once there is something to reset, against Vercel keeping four filter
dropdowns over an empty list. A control that cannot act is not shown. A dead visibility toggle is
that same mistake on the most load-bearing word in the model.

### Decision 2 — what evidence does an item card carry that the item is worth using?

The market has converged on **measured** trust: Tessl's composite score with an uplift multiplier over
*n* eval scenarios plus a Snyk scan, Smithery's score out of 100 and verified badge, Port's
pass/warn/block. We have no network, no reviews and no way to run a skill, so none of that is
available to us.

| Option | Consequence |
|---|---|
| **The validation pass is the whole trust signal** — trust is a property of the *set*, never of an item | Honest and cheap. An item card carries no quality claim at all. |
| **Add facts derived from the user's own library** — *used in 3 projects*, *last exported 12 days ago*, *2 items depend on this* | Computable locally, no network, and it is the blast-radius number flow 05 spent the whole research chasing. Not a quality judgement — a usage fact. |
| Import signals from the source for external items — stars, last commit, licence | Needs the network at exactly the moment we said we would not. Cheap to add later. |

**Recommendation: the first two together.** Trust in the *set* comes from the validation pass; the
only per-item claim we can honestly make is how the user's own library uses the item. Both are derived
from data we already hold, which keeps CLAUDE.md §10's client-only commitment intact.

### Decision 3 — does the validation pass read `version`? (a contradiction in §9)

**CLAUDE.md contradicts itself here and the design system cannot proceed past it.**

> §9: "No history, no diffs, no rollback, no version pinning in projects. The `version` field is
> reserved and **nothing reads it yet**."
>
> §9: "Automatic version conflict resolution. **A version mismatch is shown as a conflict.**"

If nothing reads `version`, there is no mismatch to show. One of the two lines has to go.

| Option | Consequence |
|---|---|
| **Nothing reads it. Drop version conflicts from the MVP.** | The validation pass has five checks, not six: requires, cycles, conflicts, duplicate commands, target-path collisions, missing env. No version anywhere in the UI. |
| **The validation pass reads it** — a version mismatch between two items becomes a conflict row | One field is read, so the item form needs a version input, the card needs to show it, and "what is a version of *my own* item" needs an answer. |
| Cut the field entirely | Cleanest MVP, most expensive to reverse — every stored item would need migrating. |

**Recommendation: nothing reads it, drop version conflicts from the MVP, keep the field.** `requires`
and `conflicts` are filled in by hand (§5); a hand-entered version on a hand-entered item is a number
the user invents and then has to keep true against itself. Every other check in the pass is derived
from structure the user already declared. Version would be the only one that depends on a discipline
we have no way to enforce.

---

## Method and limits

- Screens captured with Playwright headless Chromium; see [`screens-index.md`](screens-index.md).
  Nothing was captured from inside an account, and nothing was signed into.
- Login-walled surfaces are stamped **ДОСТУП ОГРАНИЧЕН · ACCESS RESTRICTED**: Linear app, Vercel
  dashboard, Stripe dashboard, Mobbin.
- **Mobbin was unusable.** It 403s unauthenticated fetches and redirects to sign-in, so no pattern
  library material came from it. UX-teardown material used instead: a written breakdown of the
  Linear/Vercel/Raycast aesthetic, and a documented extraction of Raycast's design tokens
  (background `#07080a`, surface `#101111`, accent `#FF6363`, Inter + GeistMono, 8px spacing base,
  radius scale 2→20px). Both are in Sources below.
- Agentman's catalog and Packmind's product could not be seen at all — marketing pages only.
- One methodological catch worth carrying forward: `registry.terraform.io/.../latest/dependencies`
  returns **HTTP 200 with a 404 body**. Status-code checking alone is not link verification.

## Sources

- [The Linear, Vercel and Raycast aesthetic](https://studiomaydit.com/blog/linear-vercel-raycast-aesthetic)
- [Raycast design system — colours, typography, tokens](https://oh-my-design.kr/design-systems/raycast)
- Products themselves, captured in `screens/`.
