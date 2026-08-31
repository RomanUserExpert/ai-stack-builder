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
| **Continue Hub** | Individual developers, then teams. | A block: model, context, docs, MCP server, rule, prompt, data. | Compose blocks into a custom assistant. | Open source and forkable — trust by inspection. | Free OSS core plus hub tiers. **Dead: acquired by Cursor, June 2026.** |

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

1. **The composition layer is consolidating, fast.** Of five hard competitors, one is dead
   (Continue, acquired by Cursor in June 2026) and one has been acquired mid-survey (Smithery is
   now part of Arcade.dev — we found the banner on their own server page, it was not in any
   article we read). Standalone "assemble your AI building blocks" businesses are being absorbed
   by the agent vendors and the tool-infrastructure players on either side.

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

## Three open questions for the PM

1. **Continue Hub was this product and it died. What is our answer?** Same object model, same
   audience, open source, 34k stars, and it was acqui-hired and switched off within a year. If the
   answer is "local ownership and vendor-neutral export", we should be able to say why that is a
   business and not a feature Cursor ships next quarter. This is the question the whole survey
   points at.

2. **Which trust signal do we ship, given we have no network and no eval harness?** The market has
   converged on measured trust — scores, evals, security scans. We have neither reviews nor a way
   to run a skill. Is our validation pass itself the trust signal (this *set* is coherent), or do
   we need per-item quality signals, and if so where do they come from?

3. **Does a personal library have a business at all, or is single-user only the wedge?** Every
   company in the hard group monetises the organisation. If our MVP is deliberately single-user
   and local, we should decide now whether the eventual charge is for hosting the portfolio, for
   the public catalog, or for a team tier — because that answer changes what `visibility` and
   `Workspace` have to mean in the data model, and the model is being designed this month.

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
