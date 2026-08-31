# Competitor landscape — US / Europe

Research phase. Surveyed August 2026. Three groups, five entries each.

- **Hard** — same product, same audience.
- **Soft** — different product, same underlying job: keeping documents and data, composing them,
  shipping a result.
- **Aspirational** — the international benchmark for the category we want to be in.

Each entry leads with **Product** — the live surface to click through, chosen over marketing and
documentation wherever one is publicly reachable. Documentation follows only where it is the only
way to see the thing (a CLI output, a design system).

Every link was checked on 2026-08-31; see [Link check](#link-check). Facts marked *(unverified)*
are inference, not confirmed from a primary source.

---

## Hard — same product, same audience

### 1. Tessl — London, UK

**Product.** [tessl.io/registry](https://tessl.io/registry) — the registry UI, browsable without an
account. Marketing: [tessl.io](https://tessl.io/).

**Why here.** An "agent enablement platform": a searchable, versioned registry of 3,000+ public
skills plus private org workspaces, with security scanning and evaluation gating each change.
Skills install into Claude Code, Cursor, Copilot and Gemini. Same atomic object as our `Item`,
same distribution surface. The difference is the buyer — Tessl sells to security leaders,
platform teams and engineering leadership; we are single-user and local.

**What to take.**

- Treating an item as software with a lifecycle. Our `version` field is reserved and unread —
  Tessl shows what the UI eventually has to carry once it is not.
- Their three visibility layers (published, project coverage, real activation on machines). That
  is a worked answer to our blast-radius problem: *"used in 3 projects"*.
- Registry browse and search over a typed catalog — directly relevant to our Library screen.

### 2. Packmind — France

**Product.** No open surface — the app sits behind a sales motion, and `app.packmind.com` does not
resolve. Closest available: [packmind.com](https://packmind.com/), plus their own
[survey of the field](https://packmind.com/context-engineering-ai-coding/best-context-engineering-tools/),
which doubles as a description of what their product does. **To see the product we would have to
book a demo.**

**Why here.** Captures an engineering playbook as versioned context and distributes it in the
exact format each agent expects — Claude Code, Cursor, Copilot. That is our export-target
adaptation, sold as an entire product. Also does drift detection and pre-commit checks.

**What to take.**

- Their per-agent format mapping is a free spec review of our export: what genuinely differs
  between `.claude/`, `.cursor/rules` MDC, `AGENTS.md` and `copilot-instructions.md`.
- How they narrate "one source, many targets" — we need the same idea legible in one screen.
- Their governance and drift framing is the enterprise wedge we deliberately do not take. Worth
  knowing where the line runs.

### 3. Agentman (myAgentSkills) — US

**Product.** [agentman.ai/agentskills](https://agentman.ai/agentskills) — the live skills library,
115 skills across 16 categories, browsable. Marketing: [agentman.ai](https://agentman.ai/).
`myagentskills.ai` redirects into the library.

**Why here.** A curated catalog plus a visual builder that assembles skills into working agents,
with versioning and team publishing. Library plus assembly, which is our two main screens. Caveat
found on inspection: the catalog is business-function skills (marketing, M&A, healthcare, legal,
sales), not developer tooling, so the audience overlap is partial.

**What to take.**

- The assembly interaction itself: what the UI shows at the moment a skill enters the set.
- Their per-skill permission tiers (use-only / read / edit / admin) — a sharper model than our
  binary `visibility`, worth keeping in view for when sharing arrives.
- The curated catalog as a model for our cold-start problem. We need ~30 realistic items with real
  relations before any demo means anything.

### 4. Smithery — US (founded Dec 2024, backed by South Park Commons)

**Product.** [smithery.ai](https://smithery.ai/) — the registry UI, open. A single server page,
which is the detail view worth studying: [Exa](https://smithery.ai/servers/exa). The wider field:
[Glama](https://glama.ai/mcp/servers), [PulseMCP](https://www.pulsemcp.com/).

**Why here.** MCP registry — 17,500+ servers as of August 2026 — with a hosting layer, managed
auth/credentials/sessions, and a router. Owns one of our six kinds outright, and its config
generation covers part of what our export does. For scale: Glama lists 71k+ servers, PulseMCP 22k+;
the field has sorted into a canonical registry plus marketplaces competing on curation.

**What to take.**

- How a server's required config and env keys are presented. Note what we found: there is *no*
  standardised format — each server documents its own requirements. That inconsistency is the
  argument for our `needsEnv` being a structured field.
- Install flows and quality signals inside a very large catalog (usage counts as the trust signal).
- The strategic read: these registries compete on curation, not storage. Same thesis as ours.

### 5. Continue Hub — US (acquired by Cursor ~16 Jun 2026, shut down; cloud data deleted after 15 Jul 2026)

**Product.** Gone. [continue.dev](https://continue.dev/) is now an acquisition notice — "Continue
has joined Cursor". The product survives only as source:
[github.com/continuedev/continue](https://github.com/continuedev/continue) (Apache-2.0). **To study
the hub we have to read the repository, or run it locally.**

**Why here.** Continue Hub let you publish blocks — models, context, docs, MCP servers, rules,
prompts, data — and compose them into custom assistants. That is our product, close to one for
one, built by a team with a 34k-star open-source project. It was acqui-hired and switched off.

**What to take.** The post-mortem is the highest-value item in this document.

- The block schema and the assistant composition format, recoverable from the repository.
- Why a standalone composition layer did not hold as a business while the agent vendors moved into
  the same space. Our answer has to differ: personal library, local ownership, and export to *any*
  target rather than into one vendor.

**Also in the field, below the top five:** [skills.sh](https://www.skills.sh/) (Vercel-backed,
npm-style CLI), [Ruler](https://github.com/intellectronica/ruler) (open-source CLI, syncs one
`.ruler/` directory into 20+ agent formats), [agentskills.io](https://agentskills.io/home).

---

## Soft — different product, same job

### 1. Backstage / Spotify Portal — Sweden / US

**Product.** [demo.backstage.io](https://demo.backstage.io/) — a live demo instance of the real
thing. This is the one to click through: catalog, entity pages, relations, the scaffolder.
*(It loads; it is a single-page app, so whether any panel asks for sign-in we could not confirm
without a browser.)* Docs, if the demo is not enough:
[Software Catalog](https://backstage.io/docs/features/software-catalog/),
[Software Templates](https://backstage.io/docs/features/software-templates/). Commercial version:
[Spotify Portal](https://backstage.spotify.com/).

**Why here.** A software catalog of typed entities with declared relations (`dependsOn`,
`providesApis`) plus Software Templates, which scaffold a ready repository from a chosen template.
A catalog of typed things with relations, and an action that produces a working artifact — our
shape, a different domain.

**What to take.**

- How relations are surfaced without a node canvas. We explicitly rejected the canvas; Backstage
  shows what the alternative looks like at scale.
- Template to scaffold is structurally our export.
- Its known failure mode: catalogs rot when nobody maintains the metadata. Our `requires` and
  `conflicts` are filled in by hand, so we carry the same exposure and the UI has to fight it.

### 2. Port — US *(HQ unverified)*

**Product.** [demo.port.io](https://demo.port.io/) — a live demo environment.
*(Same caveat: it loads, sign-in requirement unconfirmed headlessly.)* Marketing:
[port.io](https://www.port.io/). The scorecard model in writing:
[standards and compliance](https://docs.port.io/governance/standards-and-compliance/concepts-and-structure/).

**Why here.** Catalog plus scorecards plus self-service actions. Scorecards are validation as a
first-class designed surface — our validation pass, applied to services instead of stacks.

**Flag: Port is drifting toward us.** Its homepage now leads with an "Agentic-SDLC" platform that
includes a **Skills Registry** — a marketplace for skills, plugins and agents — and auto-discovery
of agents, MCP servers and skills for standards enforcement. On the next survey Port may belong in
the hard group. It stays here because the lesson we want from it is still the scorecard UI, and
because its scope is enterprise governance, not a personal library.

**What to take.**

- How a single check result is presented: pass, warn or block; why it failed; what to do next.
- The language separating a blocking failure from a warning. We need exactly this distinction for
  hard versus soft conflicts.
- Alternates worth a look: [Cortex](https://www.cortex.io/), [OpsLevel](https://www.opslevel.com/).

### 3. HashiCorp Terraform (registry + `plan`) — US

**Product.** [registry.terraform.io](https://registry.terraform.io/browse/modules) — the registry
UI, open. [Providers](https://registry.terraform.io/browse/providers) is where version-constraint
presentation lives. The other half we want, `plan`, is a CLI output, so the
[documentation](https://developer.hashicorp.com/terraform/cli/commands/plan) is the only way to
read it short of running Terraform ourselves — **which is worth doing once, on a throwaway config,
to see the real thing.**

**Why here.** Registry modules with version constraints and `required_providers`, plus
`terraform plan`, which shows precisely what will happen before the irreversible step. Dependency
resolution, conflict detection and a dry run before commitment — our mechanic, mature.

**What to take.**

- `plan` output is the reference for our validation pass: itemised, diff-shaped, trustworthy, and
  readable without a spinner.
- Version-clash and provider-conflict error copy. Best in class at explaining what collided.

### 4. Figma — US

**Product.** [figma.com/community](https://www.figma.com/community) — open, and full of real files
to open. The linked/detached instance behaviour itself only shows up in the editor, so it needs an
account we already have. Marketing: [figma.com](https://www.figma.com/). The behaviour in writing:
[applying changes to instances](https://help.figma.com/hc/en-us/articles/360039150733-Apply-changes-to-instances).

**Why here.** Component libraries, instances linked to a main component, detach instance, and
library updates that propagate into files. Our item linkage — live link, detached, "modified from
library version" — is this model one for one.

**What to take.**

- The visual language separating a linked instance from a detached one.
- The "push update to N files" confirmation: a solved blast-radius UI.
- The return path from detached back to linked, which in Figma is weak. That is an opening for us,
  and it maps to our open question about promoting a detached item back into the library.

### 5. Notion — US

**Product.** [notion.com/templates](https://www.notion.com/templates) — the gallery, fully open and
the exact surface we came for. Marketing: [notion.com](https://www.notion.com/).

**Why here.** Holds a growing personal corpus of documents and data and makes pieces of it
reusable. Its template gallery is the industry's best answer to a cold library, which is our known
cold-start problem.

**What to take.**

- The template gallery as a solution to the empty state.
- Duplication as a first-class designed primitive. We have named duplicating a project as a
  supporting moment; Notion treats duplication as distribution.

**Also worth a look:** [Obsidian](https://obsidian.md/) (local-first ownership, plugin ecosystem),
[n8n](https://n8n.io/) (credential handling, workflow import/export as JSON — and a cautionary tale
about canvases), [Doppler](https://www.doppler.com/) and [Infisical](https://infisical.com/) (env
variable UX), [Artifact Hub](https://artifacthub.io/) (Helm chart dependencies and values).

---

## Aspirational — the benchmark

### 1. Linear — US / distributed EU

**Product.** [linear.app](https://linear.app/) — the app needs an account, but the marketing site
runs real product UI at full fidelity, which for our purposes is enough. The thinking behind it:
[the Linear Method](https://linear.app/method).

**Why here.** The craft benchmark for precisely our audience: speed, keyboard-first navigation, an
opinionated dark interface, and a stated method behind the product.

**What to take.** The interaction budget — very few modal flows; density and typography in a dark
UI; command-K as primary navigation; and the discipline of shipping a small number of states
properly rather than many states approximately.

### 2. Raycast — US / Germany

**Product.** [raycast.com/store](https://www.raycast.com/store) — the extension store, open in the
browser, and the surface closest to our Library. Marketing: [raycast.com](https://www.raycast.com/).
The app itself is a free download, **worth installing if we are studying the assembly feel.**

**Why here.** Same audience, local-first, dark-first, an extension store of small units, and a very
high craft bar.

**What to take.** How a store of small units is browsed and installed with almost no chrome; empty
states; and the tone of copy written for professionals — no hand-holding.

### 3. Vercel (Geist) — US

**Product.** [vercel.com](https://vercel.com/) — the dashboard and the build log need an account.
Open and directly usable: the [Geist design system](https://vercel.com/geist/introduction) and
[its color system](https://vercel.com/geist/colors), which are a live component gallery rather than
prose.

**Why here.** A public dark-first design system — high-contrast accessible color, Geist Sans and
Mono, materials (radii, fills, strokes, shadows), grid — plus the deploy moment with a live build
log.

**What to take.** Geist's token structure as a reference for building our own — structure, not
appearance. And the build log as the reference for our validation pass: the best existing example
of a process running visibly and legibly instead of behind a spinner.

### 4. Stripe — US / Ireland

**Product.** [dashboard.stripe.com/login](https://dashboard.stripe.com/login) — account required, so
the dashboard is not casually studiable. The open substitute is
[the API reference](https://docs.stripe.com/api), which is itself the object-relationship interface
we came to look at. Marketing: [stripe.com](https://stripe.com/).

**Why here.** The benchmark for explaining a non-trivial data model through interface and docs. Our
model — items, live links, detached overrides, requires and conflicts — is not simple, and most of
the design risk sits in making it legible.

**What to take.** Object-relationship UI (how one object shows what it is connected to), error and
warning copy, and documentation surfaced inside the product.

### 5. GitHub — US

**Product.** [github.com](https://github.com/) — fully open; any public repository is a live
example. The specific surface:
[the dependency graph](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-graph),
visible on any public repo under Insights.

**Why here.** It is the stated long-term ambition: "GitHub for AI people". It is the benchmark for
the category we say we want to enter.

**What to take.** Profile as portfolio; public and private as a lightweight, low-ceremony decision;
fork as our duplicate; the dependency graph and insight surfaces. And the caution: GitHub's value
is its network, which we will not have on day one. Day-one value has to be local assembly and
validation, not the social layer.

---

## Read-through

Three things this survey changes.

1. **The closest hard competitor is dead.** Continue Hub was our product and was switched off in
   June 2026 after an acqui-hire. Every live hard competitor sells to teams and enterprises —
   registry, governance, drift, compliance — and Port is moving the same way from the other side.
   Nobody is currently serving the individual practitioner with a personal, local library. That is
   the gap, and it is also the reason to ask why the gap is empty.
2. **The validation moment has strong prior art, none of it in our category.** Terraform `plan`,
   Port scorecards and Vercel build logs are better references for our wow moment than anything a
   competitor in the AI-context space currently ships.
3. **Cold start is the shared unsolved problem.** Every catalog above solves it with curation. Our
   own answer is still ~30 hand-built realistic items, which is a demo answer, not a product
   answer.

### What is actually clickable

Open right now, no account: Tessl registry, Agentman skills library, Smithery, Backstage demo,
Port demo, Terraform registry, Figma Community, Notion templates, Raycast store, Geist, GitHub.

Needs an account: Linear, Vercel dashboard and build log, Stripe dashboard, the Figma editor.

Not reachable at all: Packmind (sales-gated) and Continue Hub (switched off — repository only).

---

## Link check

Checked 2026-08-31. Every URL was requested with redirects followed; all returned HTTP 200 at the
URL exactly as written here. Destinations of the non-obvious ones were read and confirmed against
the claim made about them: Tessl, Packmind, Agentman, Smithery, Continue, Port, Vercel Geist.

Known limits of this check:

- `demo.backstage.io` and `demo.port.io` are single-page apps. Both load and return the right page
  title, but a headless fetch cannot tell us whether a panel inside asks for sign-in. Confirm in a
  browser before planning a session around them.
- Three links were rewritten to their canonical targets after a redirect was observed: the Port
  scorecards doc (`promote-scorecards` → `governance/standards-and-compliance/…`), the Figma
  article (`Detach-an-instance` → `Apply-changes-to-instances`) and the Smithery server page
  (`/server/exa` → `/servers/exa`).
- `myagentskills.ai` redirects to `agentman.ai/agentskills`.
- `hashicorp.com/products/terraform` returned 429 (rate limited) and is therefore not linked;
  `developer.hashicorp.com` and the registry are used instead.

## Sources for the survey itself

- [Cursor acquires Continue — The New Stack](https://thenewstack.io/cursor-acquires-continue-coding/)
- [Cursor acquires Continue, July 15 export deadline — DEV](https://dev.to/leobaniak/cursor-acquires-continue-and-gives-its-users-a-july-15-export-deadline-5dkn)
- [Continue.dev deep dive 2026](https://www.digitalapplied.com/blog/continue-dev-deep-dive-open-source-ai-coding-assistant-2026)
- [Best context engineering tools 2026 — Packmind](https://packmind.com/context-engineering-ai-coding/best-context-engineering-tools/)
- [Agent Skills ecosystem report 2026 — Agentman](https://agentman.ai/blog/agent-skills-ecosystem-report-2026)
- [Best MCP registries 2026 — TrueFoundry](https://www.truefoundry.com/blog/best-mcp-registries)
- [Smithery review 2026](https://tooldirectory.ai/tools/smithery)
- [Smithery vs Glama vs Agensi (2026)](https://www.agensi.io/learn/smithery-vs-glama-vs-agensi-comparison)
- [Claude Skills marketplace directories compared](https://localskills.sh/blog/claude-skills-marketplace-guide)
- [Best prompt management tools 2026 — PromptLayer](https://www.promptlayer.com/blog/best-prompt-management-tools-2026-field-guide/)
