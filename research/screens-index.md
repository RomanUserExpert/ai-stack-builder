# Screens index

The full catalogue of screen captures collected during the research phase, with what each one
shows and why it was worth taking. Files live under [`screens/`](screens/), organised as
`group / competitor / semantic-name.png`.

## Method

38 screenshots, taken 2026-08-31 with Playwright headless Chromium at 1440×900, 2× DPR, dark
colour scheme requested. Nothing was captured from inside an account — every screen is what an
unauthenticated visitor sees. Screens behind a sign-in wall carry a stamped red banner reading
**ДОСТУП ОГРАНИЧЕН · ACCESS RESTRICTED** and their filenames end in `-restricted`. Raw run logs
are in `screens/_capture-log.json`, `screens/_capture-log-2.json` and
`screens/_capture-log-3.json`.

Two capture caveats worth remembering:

- `registry.terraform.io/.../latest/dependencies` returns HTTP 200 with a 404 body. The real URL
  is `?tab=dependencies`.
- Mobbin returns 403 to unauthenticated fetches and redirects to sign-in, so no pattern-library
  material came from it.

Groups: **hard** — products aiming at the same job as ours; **soft** — adjacent products whose
catalogue, dependency or template mechanics we borrow from; **aspirational** — craft references;
**reference** — pattern libraries.

---

## Hard

### Tessl

| File | What it shows | Restricted |
|---|---|---|
| [`hard/tessl/registry-landing-cookie-dialog.png`](screens/hard/tessl/registry-landing-cookie-dialog.png) | Registry landing with ⌘K search and the `npx tessl search` CLI affordance. The cookie dialog is still on screen in this one. | No |
| [`hard/tessl/registry-landing.png`](screens/hard/tessl/registry-landing.png) | The same registry landing with the cookie dialog dismissed — the clean read of the page. | No |
| [`hard/tessl/marketing-home.png`](screens/hard/tessl/marketing-home.png) | Marketing home. Positioning and tone for the registry product. | No |
| [`hard/tessl/skill-detail-scored.png`](screens/hard/tessl/skill-detail-scored.png) | **The most instructive screen in the set.** A single skill page carrying a composite score of 93, an uplift figure of 1.40×, separate Quality / Impact / Security bars (security scored by Snyk), the tab row SKILL.md · Quality · Evals · Security, an install command, and provenance as repo + path + commit. This is the closest anyone has come to making a reusable AI building block legible at a glance. | No |
| [`hard/tessl/registry-discover-categories.png`](screens/hard/tessl/registry-discover-categories.png) | Category browse — how the registry slices its collection for discovery. | No |

### Packmind

| File | What it shows | Restricted |
|---|---|---|
| [`hard/packmind/marketing-home.png`](screens/hard/packmind/marketing-home.png) | Marketing home, and marketing only — the product is sales-gated and `app.packmind.com` does not resolve. Nothing of the actual application could be seen. | Product unreachable |

### Agentman

| File | What it shows | Restricted |
|---|---|---|
| [`hard/agentman/marketing-skills-library.png`](screens/hard/agentman/marketing-skills-library.png) | Marketing page for the skills library: "115 production-ready AI skills, ready to clone", with HIPAA / SOC2 / ISO 27001 compliance badges doing the trust work. The catalog itself sits behind login, so only the pitch is visible. | Catalog behind login |

### Smithery

| File | What it shows | Restricted |
|---|---|---|
| [`hard/smithery/registry-home.png`](screens/hard/smithery/registry-home.png) | Registry home — the browse-and-search entry point for MCP servers. | No |
| [`hard/smithery/server-detail-exa.png`](screens/hard/smithery/server-detail-exa.png) | Server page for Exa: quality score 90/100, a verified badge, counts of Tools / Resources / Prompts, repo link, licence and published date. Also carries the banner **"Smithery is now a part of Arcade.dev"** — the second consolidation signal in the hard group. | No |
| [`hard/smithery/skills-section.png`](screens/hard/smithery/skills-section.png) | Smithery's skills section, added alongside MCP servers — evidence that a server registry is broadening into the same block-library territory we are aiming at. | No |

### Continue

| File | What it shows | Restricted |
|---|---|---|
| [`hard/continue/acquisition-notice.png`](screens/hard/continue/acquisition-notice.png) | The "Continue has joined Cursor" notice. The product is gone; this is the record of it. | No |
| [`hard/continue/github-repository.png`](screens/hard/continue/github-repository.png) | The Apache-2.0 repository — all that is left of Continue to study. | No |

---

## Soft

### Backstage

| File | What it shows | Restricted |
|---|---|---|
| [`soft/backstage/catalog-table.png`](screens/soft/backstage/catalog-table.png) | The catalog table: columns Name / System / Owner / Type / Lifecycle / Description / Tags, with Kind, Type, Owner, Lifecycle and Tag filters in a left rail. The closest thing to our Library screen that exists in the wild. | No |
| [`soft/backstage/entity-overview.png`](screens/soft/backstage/entity-overview.png) | A single entity page — how one catalogued thing presents its metadata and relations. | No |
| [`soft/backstage/catalog-relations-graph.png`](screens/soft/backstage/catalog-relations-graph.png) | Catalog Graph: a derived relation graph with Max depth, Kinds, Relations and Direction filters, edges labelled `hasPart / partOf` and `ownerOf / ownedBy`. Read-only, and the key point for us — the graph is *derived* from the entities, never hand-authored. | No |
| [`soft/backstage/scaffolder-templates.png`](screens/soft/backstage/scaffolder-templates.png) | The Software Templates list — Backstage's "produce a working artifact" action, the nearest analogue to our export. | No |

### Port

| File | What it shows | Restricted |
|---|---|---|
| [`soft/port/workflows-management.png`](screens/soft/port/workflows-management.png) | The live demo, which opens straight into Workflow management with a "You are viewing as Taylor (Platform) (Admin)" role switcher. No login required — a demo strategy worth noting in its own right. | No |
| [`soft/port/context-lake-data-model.png`](screens/soft/port/context-lake-data-model.png) | The Context Lake data model — Port's catalog layer, i.e. how it structures the entities everything else reads from. | No |
| [`soft/port/governance-users.png`](screens/soft/port/governance-users.png) | The governance section, users view. | No |
| [`soft/port/self-serve-actions.png`](screens/soft/port/self-serve-actions.png) | Self-service actions — the catalogue turned into things a user can run. | No |

### Terraform Registry

| File | What it shows | Restricted |
|---|---|---|
| [`soft/terraform/module-browse.png`](screens/soft/terraform/module-browse.png) | Module browse — registry-scale listing and filtering. | No |
| [`soft/terraform/module-overview-vpc.png`](screens/soft/terraform/module-overview-vpc.png) | A module page (VPC for AWS): the overview presentation of a reusable unit. | No |
| [`soft/terraform/module-dependencies.png`](screens/soft/terraform/module-dependencies.png) | The Dependencies tab — the mature, boring, correct way to show what a unit pulls in. Captured via `?tab=dependencies`; the pretty `/latest/dependencies` URL returns HTTP 200 with a 404 body. | No |
| [`soft/terraform/provider-overview-aws.png`](screens/soft/terraform/provider-overview-aws.png) | An AWS provider page — specifically for its version constraint presentation. | No |

### Figma Community

| File | What it shows | Restricted |
|---|---|---|
| [`soft/figma/community-browse.png`](screens/soft/figma/community-browse.png) | Community browse — a public catalogue of reusable files. | No |
| [`soft/figma/community-file-detail.png`](screens/soft/figma/community-file-detail.png) | A community file page. Note the limit of this capture: the linked/detached instance behaviour that actually interests us lives inside the editor and is not visible here. | Editor behaviour not capturable |

### Notion

| File | What it shows | Restricted |
|---|---|---|
| [`soft/notion/template-gallery.png`](screens/soft/notion/template-gallery.png) | The template gallery — the industry's standard answer to an empty library, which is our known cold-start problem. | No |
| [`soft/notion/template-collection-detail.png`](screens/soft/notion/template-collection-detail.png) | A single template page: the duplicate-into-your-workspace moment, framed and sold. | No |

---

## Aspirational

### Linear

| File | What it shows | Restricted |
|---|---|---|
| [`aspirational/linear/marketing-home.png`](screens/aspirational/linear/marketing-home.png) | The marketing home, which runs real product UI rather than screenshots of it. | No |
| [`aspirational/linear/app-login-restricted.png`](screens/aspirational/linear/app-login-restricted.png) | **ДОСТУП ОГРАНИЧЕН · ACCESS RESTRICTED** — the app itself requires an account. | Yes |

### Raycast

| File | What it shows | Restricted |
|---|---|---|
| [`aspirational/raycast/store-browse.png`](screens/aspirational/raycast/store-browse.png) | The extension store — browse density and card craft for a catalogue of small units. | No |
| [`aspirational/raycast/extension-detail.png`](screens/aspirational/raycast/extension-detail.png) | A single extension page: the install affordance and the metadata that surrounds it. | No |

### Vercel

| File | What it shows | Restricted |
|---|---|---|
| [`aspirational/vercel/geist-colors.png`](screens/aspirational/vercel/geist-colors.png) | The Geist colour system, live — a reference for building a dark-first palette as a system rather than a set of hex values. | No |
| [`aspirational/vercel/dashboard-login-restricted.png`](screens/aspirational/vercel/dashboard-login-restricted.png) | **ДОСТУП ОГРАНИЧЕН · ACCESS RESTRICTED** — the dashboard and the build log both require an account. | Yes |

### Stripe

| File | What it shows | Restricted |
|---|---|---|
| [`aspirational/stripe/api-reference.png`](screens/aspirational/stripe/api-reference.png) | The API reference — the benchmark for an object-relationship interface: many linked entities made navigable without a diagram. | No |
| [`aspirational/stripe/dashboard-login-restricted.png`](screens/aspirational/stripe/dashboard-login-restricted.png) | **ДОСТУП ОГРАНИЧЕН · ACCESS RESTRICTED** — the dashboard requires an account. | Yes |

### GitHub

| File | What it shows | Restricted |
|---|---|---|
| [`aspirational/github/dependency-graph-nextjs.png`](screens/aspirational/github/dependency-graph-nextjs.png) | The dependency graph on a public repository (Next.js) — dependency relations presented as a list, not a canvas. | No |

---

## Reference

### Mobbin

| File | What it shows | Restricted |
|---|---|---|
| [`reference/mobbin/signin-wall-restricted.png`](screens/reference/mobbin/signin-wall-restricted.png) | **ДОСТУП ОГРАНИЧЕН · ACCESS RESTRICTED** — Mobbin redirects to sign-in and returns 403 to unauthenticated fetches. No pattern-library material could be pulled from it. | Yes |
