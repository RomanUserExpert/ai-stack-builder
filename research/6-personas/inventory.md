# Inventory — what this repository actually says about people

**Stage 6, step 1.** Written 2026-09-07, per [`README.md`](README.md). This file extracts every
statement about *people* that exists anywhere in the research folder, records where each one came
from, and then — separately and at the same length — lists what nobody here knows.

It establishes nothing new. It is a stocktake, and its value is that it is honest about how small
the stock is.

**Nothing in this file is inferred.** Where a claim would need a step of reasoning to reach, it is
not in the *Observed* section; it is in *Not known*, marked `[?]`. Where the repository already
reasoned to a claim about a person, the claim is recorded as **reasoned**, with the reasoning's
owner named, and it is not treated as evidence.

---

## The instrument, before anything else

Everything below rests on one collection: **182 issue records** from two public GitHub trackers,
pulled unauthenticated through the search API and ranked by reactions —
[`3-pain/_user-pain-issues.json`](../3-pain/_user-pain-issues.json), analysed in
[`3-pain/user-pain.md`](../3-pain/user-pain.md).

That is the whole of the direct observation of people in this repository. Everything else in
`research/` is one of four other things, and the difference matters more here than anywhere else in
the phase:

| Kind | What it is | What it may be used for |
|---|---|---|
| **U** | Observed from users — the two trackers, and only those | Pain. Nothing else. |
| **V** | Vendor positioning — what a company sells, to whom, against which pain | *Who the market ignores.* **Never** *what a user wants.* |
| **M** | A mechanism captured from a live product | *What a person must be able to read on a screen.* **Never** *that it works on anyone.* |
| **E** | An event in the world — an acquisition, a download count | A fact about an outcome. Its cause is `[?]`. |
| **R** | Reasoned inside this repository, by us, from the above | A claim to be tested. Never a source. |
| **O** | Asserted by the owner in `CLAUDE.md`, before any user was observed | The claims under test. Section B. |

**The instrument's blindness is structural, not incidental.** An issue tracker records **breakage,
not friction** ([`3-pain/user-pain.md`](../3-pain/user-pain.md), *Method*). Nobody files *"I could
not find the prompt I wrote in March"* or *"I copied the same four files into a new project again"*.
Of the three candidate pains this product might rest on, **U can see exactly one**:

| Candidate pain | Visible to U? |
|---|---|
| **A. Loss** — material scattered, cannot find what I wrote | **No.** Produces no issues. |
| **B. Reassembly cost** — re-copying the same set into every project | **No.** Produces silent tedium. |
| **C. Silent breakage** — I configured it and it does not work | **Yes.** This is what trackers are made of. |

So the *Observed* section is dense about C and empty about A and B — and that emptiness is the
instrument's, not the world's. **Absence in U is never evidence of absence in the world.** Every use
of an absence below says so on the line.

**One population caveat, and it is not in `user-pain.md`.** The people in this corpus are whoever
files issues against `continuedev/continue` and `modelcontextprotocol/servers`. That they are the
same people as `CLAUDE.md` §3's audience — *design engineers and AI engineers, 25+, visually
literate, living in Linear, Vercel, Raycast, Figma* — is **not established anywhere**. It is assumed
by every downstream use of stage 3. Filed as `NK-16`.

---

# A. Observed

Every row carries a path or a URL. Reaction counts are given where the source has one, and a
reaction count is **ordinal**: 245 against 13 says *louder*, never *fourteen times more important*,
and says nothing at all about pains the instrument cannot see.

## A1. Who these people are

| # | Observation | Kind | Source |
|---|---|---|---|
| **OBS-1** | The corpus is made almost entirely of **one person, one machine, one config file**. The recurring objects are `config.yaml`, `.mcp.json`, `~/.continue/`, `PATH`, `npx`, a workspace folder. | U | [`_user-pain-issues.json`](../3-pain/_user-pain-issues.json) — 182 records, read in full |
| **OBS-2** | **In 182 ranked issues across two trackers there is not one issue about a team, a colleague, an organisation, a rollout, a portfolio, a backup or a sync.** A title search for `team · share · organi · colleague · onboard · portfolio · reuse · across projects · sync · backup · telemetry` returns four hits and three are unrelated: a Python import bug (#367, 2), a telemetry opt-out request ([#567](https://github.com/continuedev/continue/issues/567), 2), an `/onboard` command bug (#3293, 0). The fourth is the *opposite* complaint — [*Chat persists across projects*](https://github.com/continuedev/continue/issues/6437) (0), someone wanting **less** carryover between projects, not more. | U | Title search over [`_user-pain-issues.json`](../3-pain/_user-pain-issues.json), run 2026-09-07 |
| **OBS-3** | **The loudest single thing in the whole corpus is *bring this to the editor I already use*.** [*Neovim support needed*](https://github.com/continuedev/continue/issues/917) — **245 reactions, 38 comments**, open since 2024-03-03 — is the most-reacted issue in either repository. Second is [*Visual Studio (not Code) extension?*](https://github.com/continuedev/continue/issues/759) — **115**. Also [*Support Sublime Text*](https://github.com/continuedev/continue/issues/1440) — 24. The host is not negotiable for these people; the tool is expected to come to them. | U | [`_user-pain-issues.json`](../3-pain/_user-pain-issues.json) |
| **OBS-4** | **`user-pain.md` misstates this, and the correction belongs in the audit rather than in an edit.** It calls the NVM issue (182) *"the single most-reacted issue in either repository"*. It is the most-reacted in `modelcontextprotocol/servers`; in the combined corpus it is **second**, behind #917 at 245. Finding 1's *direction* survives — the top of the combined corpus is still environment and host, never composition — and its headline number does not. | U | [`3-pain/user-pain.md`](../3-pain/user-pain.md) finding 1, against [`_user-pain-issues.json`](../3-pain/_user-pain-issues.json) |
| **OBS-5** | **One request in the corpus is explicitly about one source feeding several agents**: [*Add Support for Agent Rules Standard via Root `AGENTS.md` File for Unified AI Coding Guidelines*](https://github.com/continuedev/continue/issues/6716) — **18 reactions**, 10 comments. It is the only issue in 182 that asks for a **shared format across tools**. | U | [`_user-pain-issues.json`](../3-pain/_user-pain-issues.json) |
| **OBS-6** | These people run on **hosts the instructions did not assume**: WSL ([#2822](https://github.com/continuedev/continue/issues/2822), 15 · #6339, 4 · #9151, 3 · #10433, 2 · #6242, 2), dev containers (#6320, 3), Remote-SSH (#1450, 15), Docker (#6284, 8 · #812, 6), JetBrains / IntelliJ / Android Studio (#2061, 30 · #8085, 17 · #4135, 10), Claude Desktop (#1748, 14 · #2729, 6), Windsurf (#2089, 2), Cursor (#727, 3). | U | [`_user-pain-issues.json`](../3-pain/_user-pain-issues.json) |
| **OBS-7** | They care, in public and with reactions behind it, **where their material sits on disk**: [*Migrate `~/.continue/config.py` to `XDG_CONFIG_HOME`*](https://github.com/continuedev/continue/issues/558) — 23 · [*Default Linux config directory should be `.config/continue`*](https://github.com/continuedev/continue/issues/5397) — 18 · [*Memory MCP ignores custom storage path setting*](https://github.com/modelcontextprotocol/servers/issues/692) — 15 · [*`memory` server NO persistent `memory.json` location!*](https://github.com/modelcontextprotocol/servers/issues/220) — 13 · *Keep an easy way to open `config.json`* (#5094, 4) · *Add project-specific `config.json` files* (#4720, 2). | U | [`_user-pain-issues.json`](../3-pain/_user-pain-issues.json) |
| **OBS-8** | A practitioner population of this kind exists **at scale and stayed local**: the Continue VS Code extension shows **1,582,464 downloads** on open-vsx (v2.1.0, published 2026-06-19) and is still installable, after the hosted half of the same product was switched off. | E | [`1-landscape/continue-postmortem.md`](../1-landscape/continue-postmortem.md) §0 |

## A2. Why they do it — and this is the thin part

**Almost nothing here is observed.** U sees a person at the moment something broke; it never sees
what they were doing an hour before, or why they built the thing that broke. Every row in this
subsection is either an *event* whose cause is unknown, or a *vendor's bet*.

| # | Observation | Kind | Source |
|---|---|---|---|
| **OBS-9** | **Nobody in the corpus asks for a composition or sharing layer.** `reuse blocks assistant` returns **0 results** in a 6,677-issue tracker belonging to a product that shipped a hub for exactly that. `share config across projects` returns 12, all unrelated noise. **Evidence of no demand loud enough to file, not evidence of no need** — reuse friction produces no issues by construction. | U | [`3-pain/user-pain.md`](../3-pain/user-pain.md) finding 4 |
| **OBS-10** | The half of the closest competitor that **needed a business died**; the half that needed none did not. `hub.continue.dev` and `api.continue.dev` no longer resolve, all user data was deleted, and the Apache-2.0 local client is frozen but running on 1.58M machines. **This reads both ways and must keep reading both ways**: it is a fact about a company's economics as much as about users' preferences. | E | [`1-landscape/continue-postmortem.md`](../1-landscape/continue-postmortem.md) §0 |
| **OBS-11** | **Every live hard competitor sells to an organisation, and none to the individual practitioner** — Tessl to security and platform leadership, Packmind to engineering managers, Agentman to business teams, Port to platform engineering, Smithery to developers but monetised through hosting. The buyer is never the practitioner. | V | [`1-landscape/comparison.md`](../1-landscape/comparison.md), difference 1 |
| **OBS-12** | **Every catalog in the survey solves cold start with curation and volume** — 17,500 MCP servers (Smithery), 3,000+ skills (Tessl), 115 business skills (Agentman), Notion's template gallery. Not one makes a user's *own* accumulated material better. | V | [`1-landscape/comparison.md`](../1-landscape/comparison.md), difference 2 |
| **OBS-13** | **Nobody treats *does this set hold together* as the product.** Smithery composes in order to host, Tessl in order to govern, Backstage in order to scaffold. In the closest competitor's source, `BlockDuplicationDetector` computes the duplicate correctly and `mergeUnrolledAssistants` then **silently discards the loser** — no error, no warning, no entry in an errors array. | V + E | [`1-landscape/comparison.md`](../1-landscape/comparison.md), difference 3 · [`continue-postmortem.md`](../1-landscape/continue-postmortem.md) §5 |
| **OBS-14** | **Nobody authors a graph; everybody derives one.** Not one of fifteen products asks a human to draw an edge between two objects. | V | [`1-landscape/comparison.md`](../1-landscape/comparison.md), pattern 3 |

## A3. What actually hurts them

The one subsection that stands on observation, and the reason stage 3 exists.

| # | Observation | Kind | Source |
|---|---|---|---|
| **OBS-15** | **The loudest pain is environmental, not compositional.** [*MCP Servers Don't Work with NVM*](https://github.com/modelcontextprotocol/servers/issues/64) — **182 reactions, 91 comments**. The top of `modelcontextprotocol/servers` is almost entirely *it will not start on my machine*: `npx` failures (#1097, 19 · #4791, 17 · #891, 12), a process dying at startup (#1748, 14), a timezone (#786, 14 · #612, 10), Windows path casing (#470, 13 · #1838, 4 · #447, 0 · #4487, 0). **The config is correct and the thing still does not run.** | U | [`3-pain/user-pain.md`](../3-pain/user-pain.md) finding 1 |
| **OBS-16** | **Our own thesis is sighted in the wild, in the exact file we generate, with the exact failure mode we predicted.** [*Unable to run multiple instances of `@modelcontextprotocol/server-postgres` simultaneously*](https://github.com/modelcontextprotocol/servers/issues/1219) — 13 reactions: *"the chat always chooses the first one specified in order of `mcp.json`."* **The first one wins and nobody is told.** | U | [`3-pain/user-pain.md`](../3-pain/user-pain.md) finding 2 |
| **OBS-17** | The same family, quieter still — *I set it and it was ignored*: [*Multiple local configs is not explained clearly*](https://github.com/continuedev/continue/issues/8484) — **6** · [*Multiple models with autocomplete role*](https://github.com/continuedev/continue/issues/4306) — **3** · *`contextLength` is not applied to model* (#4638) — **2** · *`toolOverrides` not applied in system message tools path* (#11060) — **0** · *`systemMessage` in `config.yaml` is ignored* (#5105) — 0 · *Markdown files in `prompts` misidentified as rules and dropped* (#12412) — 0. | U | [`_user-pain-issues.json`](../3-pain/_user-pain-issues.json) — counts added here; `user-pain.md` quotes these without them |
| **OBS-18** | **Env variables and secrets rank near the top of both trackers**, and this was not a hypothesis anyone had: [*storing api keys in plain text*](https://github.com/continuedev/continue/issues/1729) — 32 reactions, 26 comments · [*Environment variables not respected in `server-memory`*](https://github.com/modelcontextprotocol/servers/issues/1018) — 23 · [*Security Proposal: credential management in MCP servers*](https://github.com/modelcontextprotocol/servers/issues/754) — 22 · *`[server-gitlab]` env vars not properly expanded* (#1039) — 1. | U | [`3-pain/user-pain.md`](../3-pain/user-pain.md) finding 3 |
| **OBS-19** | The pain of OBS-15 is **mostly out of our reach** and touches us in exactly one place: where our output meets their machine — the generated `SETUP.md` and the merged `.mcp.json`. | R | [`3-pain/user-pain.md`](../3-pain/user-pain.md), *What this changes* |
| **OBS-20** | **No product in the survey scores anything about the machine its artefact lands on.** Fifteen benchmark cells all score what a product says about *its own* state; B4 — produce an artefact and hand it over — is the weakest flow in the industry, **no candidate above 4**, because none of them has such a surface to score. | V | [`4-benchmark/benchmark.md`](../4-benchmark/benchmark.md), *The gap neither instrument covers* |

## A4. What could frighten them, or make them distrust

The rows split into **what a person actually said** (U) and **what a vendor decided a person would
need to be told** (M). The second is not evidence that anyone was ever frightened.

| # | Observation | Kind | Source |
|---|---|---|---|
| **OBS-21** | **Credentials in the clear.** 32 reactions and 26 comments on [*storing api keys in plain text*](https://github.com/continuedev/continue/issues/1729), and a formal [*Security Proposal: Adopt Best Practices for Credential Management*](https://github.com/modelcontextprotocol/servers/issues/754) at 22. This is the one fear in the corpus with a crowd behind it. | U | [`3-pain/user-pain.md`](../3-pain/user-pain.md) finding 3 |
| **OBS-22** | Sharper, quieter security fears from the same population: [*mcp-server-fetch lacks SSRF protection; cloud-hosted agent hosts can leak IAM credentials*](https://github.com/modelcontextprotocol/servers/issues/4143) — 1 reaction, 8 comments · [*memory: safer persistence defaults, atomic writes, quotas, redaction, and destructive-operation guards*](https://github.com/modelcontextprotocol/servers/issues/4117) — 1 reaction, **21 comments**. Low reactions, high discussion: a few people who think about this a lot. | U | [`_user-pain-issues.json`](../3-pain/_user-pain-issues.json) |
| **OBS-23** | **Being silently overruled.** OBS-16 and OBS-17 are the same shape as a fear rather than a bug: the tool made a choice, it was the wrong one, and it did not say. The user's own words are *"the chat always chooses the first one specified"*. | U | [`3-pain/user-pain.md`](../3-pain/user-pain.md) finding 2 |
| **OBS-24** | **Being reported on.** [*Improve Telemetry Opt-Out Experience: In-Extension Setting*](https://github.com/continuedev/continue/issues/567) — 2 reactions, 6 comments. One data point, recorded because it is the only one of its kind in the corpus. | U | [`_user-pain-issues.json`](../3-pain/_user-pain-issues.json) |
| **OBS-25** | **A hosted layer can vanish and take the data with it, and this happened to this exact audience** — Continue's FAQ: *"All user data has been deleted in accordance with the privacy notice."* Whether anyone was frightened by it is `[?]`; that it occurred is not. | E | [`1-landscape/continue-postmortem.md`](../1-landscape/continue-postmortem.md) §0 |
| **OBS-26** | **An origin that cannot be recovered.** Figma keeps **no memory of where a detached instance came from** — no "modified from library version", no way back. The state exists in the product and is a dead end. | M | [`2-flows/05-linked-vs-detached/NOTES.md`](../2-flows/05-linked-vs-detached/NOTES.md) |
| **OBS-27** | **Drift you cannot see.** Figma computes the override diff precisely enough to name a single field (`Reset fill`) and then draws a modified instance **identically** to a clean one — three channels announce *this is an instance* and none announces *this no longer matches*. The data existed, was correct, and nobody was told. Same shape as OBS-13. | M | [`2-flows/05-linked-vs-detached/NOTES.md`](../2-flows/05-linked-vs-detached/NOTES.md) |
| **OBS-28** | **A blast radius stated as a number.** Figma's library-update dialog counts instances per component — one row touching 2 objects beside one touching **423** — and without the numbers the two rows look identical. The count is *within the file*; the cross-file number sits behind a paid tier and was never seen. | M | [`2-flows/05-linked-vs-detached/NOTES.md`](../2-flows/05-linked-vs-detached/NOTES.md) |
| **OBS-29** | **The best-observed version of *tell me what I am agreeing to*:** VS Code's Workspace Trust puts *In a Trusted Folder* against *In Restricted Mode* in two columns, four ✓/✕ lines each, and **counts and hyperlinks** two of them — *"95 workspace settings are not applied"*, *"10 extensions are disabled or have limited functionality"*. It beats Figma's 423 on the axis Figma leaves open: the number is a link to the list. | M | [`4-benchmark/benchmark.md`](../4-benchmark/benchmark.md) B2 · [`NOTES-vscode.md`](../4-benchmark/NOTES-vscode.md) |
| **OBS-30** | **Naming the second-order leak.** Notion's publish dialog says *"anyone with the link can view this page's content **and see contributor names**"* — it names the leak the reader would not have thought of, not just the obvious one. | M | [`2-flows/12-visibility-and-portfolio/NOTES.md`](../2-flows/12-visibility-and-portfolio/NOTES.md) |
| **OBS-31** | **Asking the question someone will have at 3am.** Vercel's env drawer asks for the *type* before the value, defaults to the irreversible option (`Secret`), states the consequence rather than the category — *"You can't reveal this value after saving"* — and placeholds its optional note field *"Where to rotate, or who to contact"*. | M | [`2-flows/07-env-and-secrets/NOTES.md`](../2-flows/07-env-and-secrets/NOTES.md) |
| **OBS-32** | **Severity, as the nearest competitor shipped it, is a boolean** — `ConfigValidationError { fatal: boolean }` — and a block that failed to resolve is filed as `fatal: false`, so a missing dependency degrades the result quietly rather than stopping it. | E | [`1-landscape/continue-postmortem.md`](../1-landscape/continue-postmortem.md) §5 |

## A5. What vendors bet convinces people

**None of this is evidence that it works on anyone.** It is fifteen companies' collective guess, and
it is recorded because a guess made fifteen times is worth knowing about.

| # | Observation | Kind | Source |
|---|---|---|---|
| **OBS-33** | **Trust has moved from social proof to measurement.** Tessl: a composite score (93), an uplift multiplier (1.40×), Quality % and Impact % across *n* eval scenarios, a Snyk scan. Smithery: a score out of 100, a verified badge, usage counts. Port: pass / warn / block with the reason attached. **Stars and download counts are no longer the trust story — a number derived from running the thing is.** | V | [`1-landscape/comparison.md`](../1-landscape/comparison.md), pattern 2 |
| **OBS-34** | The older signals are still in use elsewhere: Terraform — version constraints, provider signing, publisher namespace, download counts. Figma — publisher identity and library provenance; an instance always names its main component. Raycast — open source, author identity, install counts, review before listing. Backstage — an owner, a lifecycle stage and a source file you can open, on every entity. | V | [`1-landscape/comparison.md`](../1-landscape/comparison.md), the three matrices |
| **OBS-35** | **We can produce none of it.** No network, no reviews, no way to run a skill. Any number we invented would be decoration. | R | [`1-landscape/comparison.md`](../1-landscape/comparison.md), decision 2 |
| **OBS-36** | **A first run does not have to be empty, and the best observed answer is not an empty state at all.** A brand-new Linear workspace opens on the Issues list already holding **four real issues** — real IDs, statuses, dates, deletable — so the onboarding checklist *is* the data model exercised on itself. Observed in the owner's own new workspace, which is the one first-run capture in the whole phase. | M | [`2-flows/08-empty-state-and-cold-start/NOTES-linear.md`](../2-flows/08-empty-state-and-cold-start/NOTES-linear.md) |
| **OBS-37** | **Emptiness has three registers, and the rule picking between them is legible**: a concept you may never have used → define it in a paragraph; routine emptiness → one line; emptied by your own filter → **say how many are hidden and offer one click back**. Verbosity scales with the chance the reader does not know what the object is. | M | [`2-flows/08-empty-state-and-cold-start/NOTES-linear.md`](../2-flows/08-empty-state-and-cold-start/NOTES-linear.md) |
| **OBS-38** | **A control that cannot act is not shown** — Linear suppresses the toolbar over an empty screen; Figma shows `Reset` only when there is something to reset; Vercel keeps a search box and four filter dropdowns over an empty env list, which the note records as the flaw to avoid. Three products against one. | M | [`2-flows/08-empty-state-and-cold-start/NOTES-linear.md`](../2-flows/08-empty-state-and-cold-start/NOTES-linear.md) · [`07-env-and-secrets/NOTES.md`](../2-flows/07-env-and-secrets/NOTES.md) |
| **OBS-39** | **Duplication is a keystroke when the copy stays with you and a form when it leaves.** Notion: `Ctrl+D` in a menu, no dialog. GitHub fork: a form with a prefilled name, live availability checking, and a checkbox that narrows what is copied. | M | [`2-flows/09-duplicate-and-fork/NOTES.md`](../2-flows/09-duplicate-and-fork/NOTES.md) |
| **OBS-40** | **The same layout reads as a portfolio when it is full and as an empty template when it is not** — two captures of the same GitHub profile surface, one heavily used and one the owner's. | M | [`2-flows/12-visibility-and-portfolio/NOTES.md`](../2-flows/12-visibility-and-portfolio/NOTES.md) |

## A6. Claims about people this repository has already reasoned to

**Not evidence.** Listed so that stage 6 does not mistake its own earlier reasoning for a source.
Each is `[?]` about a person until someone is asked.

| # | Claim | Whose reasoning | Source |
|---|---|---|---|
| **OBS-41** | The library will hold **~300 items**, and the chosen shape must survive that. | Stage 5 | [`5-patterns/patterns.md`](../5-patterns/patterns.md), *What this costs us* · flagged unobserved in [`research.md`](../research.md) G4 |
| **OBS-42** | People **find what they can name and stay blind to what they cannot** — so the cost of dropping the library pane is discovery, not search. | Stage 5 | [`research.md`](../research.md) G4 |
| **OBS-43** | Every browse mechanic in the phase was captured against **four issues** (Linear) and **27 notes** (Obsidian). **Density under load was never observed at all.** | Method fact | [`research.md`](../research.md), *What the flows could not see* |
| **OBS-44** | **Silent breakage is a retention argument, not an acquisition one** — what makes the product trusted once adopted, not what makes anyone try it. | Digest | [`research.md`](../research.md) G9 |
| **OBS-45** | **Reassembly cost, not loss, is what converts.** Written as the falsifiable form of Q5, with the one hint on record noted as a hint: shipping a public shelf is a bet that people want *material*, not that they want to find their own. | Digest | [`research.md`](../research.md) G1 |
| **OBS-46** | **A seed of 8–12 items producing at least one Problem and one Note teaches the product better than 30 clean ones.** | Digest | [`research.md`](../research.md) G5 |

---

# B. Asserted by the owner

The claims under test. Each is stated in `CLAUDE.md`, was written **before any user was observed**,
and is listed here so that stage 6 cannot cite it as evidence and then cite the persona back to it.

| # | The assertion | Where | What would test it |
|---|---|---|---|
| **A-1** | *"The core value is **assembly with validation**, not storage."* | §2 | Ask what someone last did with a skill they already had. If the answer is *looked for it* rather than *put it together with three others*, the emphasis is wrong. Partly supported already: OBS-16 sights the failure, OBS-9 finds nobody asking for composition. |
| **A-2** | *"**The user has said** it is the export: a working archive in thirty seconds."* | §2 | The five conversations, asked as a situation — *what happened the last time you moved a setup to another machine* — never as a pitch. Note the phrasing: this is the one assertion in the file that presents itself as a user quote, and no source is attached to it. |
| **A-3** | Two supporting moments matter: the **validation pass**, and **duplicating a project** to re-tune it for a new context. | §2 | Has anyone ever re-tuned a set for a second context? `[?]` — no evidence in either direction anywhere in the phase. |
| **A-4** | The audience is *design engineers and AI engineers, **25+**, who use AI heavily and have **accumulated a lot of material** they want to keep and reuse.* | §3 | Nothing here establishes age, role, corpus size, or that accumulation is felt as a problem. OBS-1 and OBS-2 are consistent with a solitary practitioner; consistent is not confirmed. |
| **A-5** | They are **visually literate**, live in *Linear, Vercel, Raycast, Figma*, and *"generic dashboard aesthetics will read as cheap."* | §3 | Not testable by any instrument in this repository. The trackers show people who tolerate a JetBrains sidebar that freezes for years ([#8085](https://github.com/continuedev/continue/issues/8085), 17). |
| **A-6** | **Desktop-first**, responsive later. | §3 | Consistent with OBS-1 and OBS-6 — every environment in the corpus is a desktop one — but the corpus belongs to a desktop product, so it could not have said otherwise. |
| **A-7** | **Dark theme from day one**; light is a design decision, not an inversion. | §3 | A craft decision, not a claim about people. Not tested by this stage. |
| **A-8** | *"An **empty library kills the product**, because there is nothing to validate."* | §11 | Half-supported by reasoning rather than observation: three of five pattern variants are broken without a seed ([`5-patterns/patterns.md`](../5-patterns/patterns.md)), and OBS-36 shows a product that refuses to be empty. Nobody has watched a real first run of *this* product. |
| **A-9** | The only honest per-item evidence is **usage facts from the library** — *used in 3 projects*, *2 items require this* — never a score. | §5 | An owner's call taken against OBS-33 and OBS-35, both sound. What is `[?]` is whether a usage fact convinces anyone of anything; OBS-28 and OBS-29 are vendors betting that counts work, not proof that they do. |
| **A-10** | **Nothing blocks**; an unclean export is confirmed, never refused, because *"it is the user's own library on their own machine."* | §6 | The premise is a claim about the person: that they are the only party at risk. Consistent with OBS-1 and OBS-2. `[?]` the moment an archive is handed to anybody else — see NK-7. |
| **A-11** | `SETUP.md` is **written for the agent that opens the project**, not for a human reader. | §6 | Aimed squarely at OBS-15 and OBS-20, which is the best-evidenced aim in the spec. `[?]` is whether a receiving agent actually performs the setup correctly from prose — see NK-13. |
| **A-12** | The public library gives the product **material from the first second**, and `My library` *"stays honestly the user's."* | §8, §11 | OBS-12 says every catalog solves cold start with volume; OBS-45 flags that shipping a shelf is itself a bet on *material* over *finding*. Whether a read-only shelf reads as generous or as filler is `[?]`. |
| **A-13** | **~30 realistic items** is the right order of magnitude for the shelf. | §11 | Against OBS-46 (8–12, composed to produce a Problem and a Note) and OBS-43 (density never observed at any size). The two numbers answer different questions — *enough to browse* and *enough to teach* — and the spec does not say which governs. |
| **A-14** | The known cost of dropping the library pane is carried by three things: the palette opening on **related** items, Library one keystroke away, per-item usage facts. | §8 | Testable the moment a seeded library exists (OBS-42). Not testable now. |

---

# C. Not known

**Equal in weight to section A, and longer than is comfortable.** Each row says the question and why
nothing in this repository can answer it. Every one of these is `[?]`.

## C1. The eight the stage plan named

| # | Question | Why nothing here answers it |
|---|---|---|
| **NK-1** | **Which of loss, reassembly cost or silent breakage actually drives adoption?** (Q5) | Two of the three are invisible to the only instrument, by construction. Deferred 2026-09-02 as accepted risk with a trigger written down. The one hint on record — shipping a public shelf leans toward *reassembly* — is filed in [`FINAL.md`](../FINAL.md) §3 Q5 **as a hint, so nobody mistakes it for the answer.** |
| **NK-2** | **How large is one person's library?** | The 300-item figure is stage 5's reasoning (OBS-41), never a count of anything. No capture in the phase exceeds 27 objects (OBS-43). |
| **NK-3** | **How fast does it grow?** | Nothing in the phase observes a collection over time. Not one capture is a second visit to the same surface. |
| **NK-4** | **How often is a tool like this opened?** — daily, weekly, once per project | The *weekly* claim behind the chosen pattern is stage 5's reasoning. No usage data exists anywhere in this repository, ours or anyone else's. |
| **NK-5** | **How many agent targets does one person actually keep?** | OBS-3, OBS-5 and OBS-6 show that *hosts vary across the population*, and that one person asked for a unified format. **Neither shows how many targets a single person maintains at once.** Population variance is not per-person count, and conflating the two is the specific error this row exists to prevent. |
| **NK-6** | **Where does this material live today?** — dotfiles, gists, a repo folder, chat history, a Notion page, nowhere | OBS-7 shows people arguing about *where a tool puts its own config*, which is not the same as where a person keeps their own store. Nothing observes a practitioner's filing habits. This is the row step 5 can plausibly convert into an observation. |
| **NK-7** | **Does the person work alone, or does anyone else ever open their archive?** | OBS-2's silence is the instrument's, not the world's. And §6's *nothing blocks* rests on the answer being *alone* (A-10), so this is not a decorative unknown. |
| **NK-8** | **Has anyone ever wanted a previous project back?** | The duplicate-and-re-tune moment (A-3) and the promote path (§5, §7) both rest on it. Zero evidence in either direction; flow 09 captured the *mechanism* in Notion and GitHub, never a person needing it. |

## C2. The ones this inventory adds

| # | Question | Why nothing here answers it |
|---|---|---|
| **NK-9** | **Would anyone adopt this at all, and why?** | Named in the stage plan as the one row no step in stage 6 can lift. U only ever sees people who already adopted something else and then hit a wall. |
| **NK-10** | **What do they do today instead?** | No substitute behaviour was ever observed — not a shell script, not a dotfiles repo, not copy-paste. The entire *before* state is missing. |
| **NK-11** | **What would make someone distrust our check?** | OBS-28, OBS-29, OBS-31 and OBS-33 are vendors' bets about what convinces. Nobody has been shown our three severities, and *Skipped* — the glyph that exists precisely so a green tick is not claimed unearned (§6) — has never been in front of a person. |
| **NK-12** | **Is a usage fact — *used in 3 projects* — persuasive, or is it noise?** | A-9 is sound about what we can honestly show. It is silent, and this repository is silent, on whether it changes anyone's behaviour. |
| **NK-13** | **Does a receiving agent actually set a project up correctly from `SETUP.md` alone?** | A-11 is the spec's most load-bearing bet, and it is a bet on a *machine's* behaviour rather than a person's. It has never been run once. It is also testable cheaply and by us, with no users needed — which makes it different in kind from everything else in this section. |
| **NK-14** | **Is hand-entered `requires` / `conflicts` data ever actually maintained?** | §5 says relations are entered manually. Backstage's known failure mode is that catalogs rot when nobody maintains the metadata ([`competitors.md`](../1-landscape/competitors.md), Backstage). Whether a single-user library rots the same way is unobserved. |
| **NK-15** | **Does the loudest observed pain (OBS-15) belong to the same people as the quietest (OBS-16)?** | Both were counted across the same corpus, never joined per person. 182 and 13 may be two crowds or one. The whole primary-persona choice turns on this, and **the instrument cannot resolve it** — reaction counts carry no identity. |
| **NK-16** | **Are tracker filers the same population as `CLAUDE.md` §3's audience?** | Assumed by every downstream use of stage 3, established nowhere. Filing issues against a free OSS extension is a behaviour, not a job title. |
| **NK-17** | **What is the emotional register of the moment this product is opened?** | Every persona template wants a *context* block — the situation someone arrives from. U sees the moment of breakage and never the hour before it. The stage plan predicted this block would be *mostly `[?]`*, and it is. |
| **NK-18** | **Does anyone want their work to be a portfolio?** | §2's long-term ambition and OBS-40's observation are both about a *surface*. Not one issue, capture or source in the phase records a practitioner wanting to be seen. |
| **NK-19** | **Under what licence may someone else's skill ship inside our public library?** | G6 in the digest. Not a question about what people want but about what we are allowed to hand them, and it is unanswered — a licence review, not a design decision. |
| **NK-20** | **Does the person hitting OBS-15 have a library at all?** | The archive-does-not-run pain is felt by someone installing *one* server as easily as by someone assembling thirty items. If it is mostly the former, the pain is real and **not ours**. |

---

## What this file changes

**Nothing.** It is a stocktake and it edits no file outside this folder — `CLAUDE.md` least of all.
Three things it hands forward:

1. **Step 2, the axes.** OBS-3, OBS-5 and OBS-6 look like an axis — *one host* against *several* —
   and NK-5 says why they are not one yet. OBS-15 against OBS-16 is the axis with evidence at both
   ends, and NK-15 is the reason those two ends may turn out to be one person.
2. **Step 4, the audit.** **OBS-4 is a correction to a signed-off document.** It is filed here as an
   observation and **not applied**; it belongs in the audit's proposals, where the owner decides.
3. **Step 5, the one question re-researched at point scale.** **NK-6 is the strongest candidate** — a
   GitHub search for repositories carrying `.claude/`, `CLAUDE.md`, `.cursor/rules` and `AGENTS.md`
   observes where material lives and, per repository, how many targets sit side by side, which
   touches NK-5 as well. It costs one API session and turns two `[?]` rows into observations, or
   into a documented failure to observe.
