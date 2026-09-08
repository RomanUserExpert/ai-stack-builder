# Inventory — what this repository actually says about people

**Stage 6, step 1 — revalidated 2026-09-07.** Written per [`README.md`](README.md). This file
extracts every statement about *people* that exists anywhere in the research folder, records where
each one came from, and then — separately and at the same length — accounts for what nobody here
knows.

**Section C is no longer a list of unknowns; it is a register.** Every one of the twenty questions
now carries the answer we have, **the data that answer rests on with a link**, and **a mark saying
how true it is** — `✓` confirmed · `*` practitioner-reported · `?` unknown, per
[`research.md`](../research.md), *The three marks*. Three more questions arrived with the first
interview and are recorded at the end as NK-21 to NK-23. **Section B now carries the same marks
against the owner's fourteen assertions.**

It establishes nothing new. It is a stocktake, and its value is that it is honest about how small
the stock is.

**Two scales, and they do not compete.** Section A tags each row with a **kind** — `U` observed from
users · `V` vendor positioning · `M` a mechanism captured from a product · `E` an event in the world ·
`R` reasoned here · `O` asserted by the owner — which is the finer, older scheme and is explained
below. Sections B and C carry the **three marks** (`✓` / `*` / `?`). They map loosely: only `U` and
`E` can support a `✓`, `V` and `M` are evidence of what a company decided rather than of anything
about a person, and `R` and `O` are claims under test. Where a section-C row cites a section-A
observation, the mark is the one that governs.

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

> **Superseded in part, 2026-09-07.** [`re-research.md`](re-research.md) R3 found reassembly friction
> **filed** on live trackers — as feature requests rather than as bugs, which is why a bug-shaped
> search missed it. Row **B** should read *invisible to a bug search, visible to a feature-request
> search*. Row **A** stands: loss has no evidence in any instrument tried. The table is left as it
> was so that what stage 3 believed, and what corrected it, are both legible.

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


## Standing of the owner's assertions, 2026-09-07

Same three marks. **Nothing here is applied to `CLAUDE.md`** — this says what the evidence now does to
each claim, and the owner decides what follows.

| # | The assertion, in short | Standing | On what |
|---|---|---|---|
| **A-1** | The core value is assembly **with validation**, not storage | **Contested `*`** | The one practitioner asked wants **observability of what ran**, not a coherence check — NK-23. And what built his collection was reassembly, not validation — NK-1 |
| **A-2** | *"The user has said"* the wow moment is the **export** | **Unsupported** | Never tested. Asked what a genie should fix, he asked to **see what loaded**, not for an archive — NK-23 `*` |
| **A-3** | Supporting moments: the validation pass, and **duplicating a project** to re-tune it | **Partly `*`** | First evidence that someone wanted a previous thing back — and could not have it, because it was welded to its project — NK-8 |
| **A-4** | Practitioners who have **accumulated a lot of material** | **`*`** | 40-something files, ~6k lines, 14 months, one person — NK-2, NK-3 |
| **A-5** | Visually literate, living in Linear, Vercel, Raycast, Figma | **`?`** | No instrument here can reach it, and none has |
| **A-6** | **Desktop-first** | **`*`** consistent | Every environment described is a desktop or a container on one — NK-5, NK-6 |
| **A-7** | **Dark from day one** | **`?`**, and not a claim about people | Untouched by this stage |
| **A-8** | *"An empty library kills the product"* | **`?`** | Still nobody has watched a first run of **this** product |
| **A-9** | Per-item evidence is **usage facts, never a score** | **`*`, invented unprompted, n = 1** | Asked openly what would help him choose among his own things, he invented our mechanism — *"loaded in 40 sessions, this one in 2, this one never"* — and extended it: **last actually useful**, counted **per session** — NK-12 |
| **A-10** | Nothing blocks, because *"it is the user's own library on their own machine"* | **Premise weakened `✓` + `*`** | Not his own machine only: a contractor got the setup, half his tools silently missing, **worked around it for two days** — NK-7 |
| **A-11** | `SETUP.md` is written **for the agent** that opens the project | **`?` on the mechanism, `*` on the target** | Never run once — NK-13. The pain it aims at is real: Node 18 against a server needing 20+, *"it degrades quietly"* |
| **A-12** | A public shelf gives material **from the first second** | **`?`, and now carrying a risk** | Untested — plus 13.4% of 3,984 scanned public skills carry critical security issues ([re-research](re-research.md) R6) |
| **A-13** | **~30 realistic items** is the right order of magnitude | **`✓` + `*`, and read rule 5 on the `✓`** | 20–30+ named as the threshold where management breaks — **one filer's sentence, with the 151 reactions sitting on the request around it, not on the number**; 40-something files reported by one practitioner. Three reports in total. **They refute stage 5's 300 without establishing a figure of their own** — NK-2 |
| **A-14** | Three things carry the cost of having no library pane | **`?`, and its premise moved** | Untested, and it was priced against surviving 300 items, which nothing supports — NK-2 |

**Two of the fourteen have moved decisively, in opposite directions.** **A-9 is the best-supported
claim in the spec** — a practitioner invented it unprompted, which is the strongest *form* a `*` can
take and is still **one person**; the word *confirmed* was removed from this row on 2026-09-08
because it is the reserved name of `✓`. **A-10's premise is the weakest** — the archive does leave the
machine, and when it did, the person receiving it lost two days without knowing anything was wrong.

---

# C. The twenty questions, revalidated

**Rewritten 2026-09-07**, after [`re-research.md`](re-research.md) took four instruments to the
public record and after the first practitioner interview arrived. This section used to be a list of
things nobody knew. It is now a **register**: every question, the answer we currently have, **the
data that answer rests on with a link to it**, and **a mark saying how true it is.**

**The marks are defined once**, in [`research.md`](../research.md), *The three marks*:

| | Means | Here |
|---|---|---|
| **`✓`** | Confirmed — another person can re-run the instrument and get the same answer | A logged query with its count, a captured page, a source read at origin |
| **`*`** | Practitioner-reported — said in an interview, from memory, about their own work | [`agent-setup-interview.md`](agent-setup-interview.md), **n = 1** |
| **`?`** | Unknown — no instrument has established it in either direction | |

**Three things to hold while reading.**

**A `*` never becomes a `✓` by repetition**, and right now there is only one interview, so every `*`
below is **one person**. Four more are required before the *provisional* label lifts, and five is
still the number that can *refute* a choice rather than measure a population.

**Where `✓` and `*` disagree, both are kept** — rule 4. Three rows below do disagree, and they are
the most interesting rows in the document: NK-1, NK-2 and NK-18.

**A closed row is not a settled row.** `✓` means checkable, not permanent. Two rows closed by
re-research are re-asked in the interview guide as corroboration, because a contradiction there would
be worth more than a confirmation.

> **Re-marked 2026-09-08, after an audit of every mark in this folder.** The audit found one mistake
> made five times, and it is the one [`research.md`](../research.md) now carries as **rule 5**: *a
> re-runnable query proves that something was **said**, not that it is **true**.* An issue body, a
> forum comment and a tool's own README are all people describing their own behaviour or their own
> product. The `✓` on them covers the **utterance** — this was written, this many reacted, anyone can
> go and read it — and the behaviour underneath is still self-report, to which rule 2 applies. Five
> rows were carrying a plain `✓` for a claim only the utterance supported: **NK-5, NK-6, NK-10 and
> NK-19** are re-marked below, and **NK-14** moves the other way, because its own *Rests on* listed
> two re-runnable sources under a `*` header. Nothing new was collected; only the marks changed.

---

## The register at a glance

| # | Question | Mark | Where it stands |
|---|---|---|---|
| **NK-1** | Which pain drives adoption — loss, reassembly, breakage? | **`*`** | For one practitioner **reassembly built the collection**; breakage is what he *files* about. Loss appeared for the first time — also from him |
| **NK-2** | How large is one person's library? | **`✓` + `*`** | Reported sizes cluster at **20–40 items**. Stage 5's 300 has nothing behind it |
| **NK-3** | How fast does it grow? | **`*`** | One file → ~40 files in 14 months, by accretion, never by design |
| **NK-4** | How often is it opened? | **`*`** | Agents daily. The **collection** is entered to copy out, to add a rule in irritation, or to search — **never to review** |
| **NK-5** | How many agent targets per person? | **`✓` + `*`** | `✓` One source for all of them is the loudest demand in the whole evidence base. `*` *Two to four each* is seven people's self-description |
| **NK-6** | Where does the material live? | **`✓` + `*`** | `✓` People care loudly where it sits, and ask for git to be the source. `*` The private repo symlinked into `~/.claude/` is one person's |
| **NK-7** | Alone, or does anyone else open it? | **`✓` + `*`** | **Not alone.** And the handover failed silently for two days |
| **NK-8** | Has anyone wanted a previous project back? | **`*`** | **Yes** — and he could not have it, so he rewrote a worse one |
| **NK-9** | Would anyone adopt this, and why? | **`*`** | He went looking twice, used something for a week, stopped. Still the weakest row |
| **NK-10** | What do they do today instead? | **`✓` + `*`** | `cp -r`, symlinks, `@include`, hand-written scripts — said in public many times, watched by nobody |
| **NK-11** | What would make them distrust? | **`✓` + `*`** | Not *your checker is wrong* — ***half of my own material may do nothing*** |
| **NK-12** | Is a usage fact persuasive? | **`*`** | **Asked for it unprompted, in our own words**, when the question was put open |
| **NK-13** | Does an agent set up from `SETUP.md` alone? | **`?`** | **Still untested, and we are the ones who can test it** |
| **NK-14** | Is hand-entered metadata maintained? | **`✓` + `*`** | **No.** Drift is filed and reacted to; for one person it cost three hours and a client complaint |
| **NK-15** | Are the loud pain and the quiet pain the same person? | **`*`** | **Yes, for this one — and he says the collection caused the second** |
| **NK-16** | Are tracker filers our audience? | **`?`** | Unresolved. He is a filer, so n=1 cannot answer it |
| **NK-17** | What is the emotional register on arrival? | **`*`** | Three modes, and **most edits are written while irritated** |
| **NK-18** | Does anyone want their work to be a portfolio? | **`✓` + `*`** | Two searches found nothing; he says a qualified yes **for a different motive** |
| **NK-19** | Licence for redistribution? | **`✓` + `?`** | `✓` A field exists and absence of a licence is not permission. `?` **No item on our planned shelf has had its licence looked at** |
| **NK-20** | Does the person hitting env pain have a library? | **`*`** | **Yes** — same answer as NK-15, same sentence |

**After the 2026-09-08 re-marking: nine rows carry a `✓` somewhere, nine rest on one person alone,
and two carry no evidence at all — NK-13 and NK-16. Only one of those two is ours to fill.**

---

## Row by row

### NK-1 — Which pain drives adoption: loss, reassembly cost, or breakage? `*`

**Answer, and it is not what either side of the argument expected.** For the one practitioner asked,
**reassembly cost is what built the collection** — it is the origin story, told without prompting:

> *"It started as exactly one file… I copied that file to the next project, then the next, and at
> project four I got annoyed and made a repo. So the origin is not 'I designed a system.' The origin
> is **'I got tired of copy-pasting one file.'**"* — [interview, Q4](agent-setup-interview.md) `*`

And the cost is described as invisible by construction, which is why no tracker ever saw it:

> *"That trickle is the actual cost and **it's invisible because no single instance of it feels
> expensive**."* — [interview, Q9](agent-setup-interview.md) `*`

**Loss appeared for the first time in this repository**, unprompted, inside an answer about something
else:

> *"…I'm looking for something I know I wrote and can't find; that's usually a prompt, and **it
> usually takes longer than rewriting it would**."* — [interview, Q19](agent-setup-interview.md) `*`

**Rests on.**
- `*` The three quotes above. **One person.**
- `✓` [`re-research.md`](re-research.md) R3 — the reassembly complaint is filed on live trackers as feature requests: [claude-code #9444](https://github.com/anthropics/claude-code/issues/9444) (48 reactions, *"copies can drift out of sync"*), [codex #17401](https://github.com/openai/codex/issues/17401) (*"no modular reuse across projects… 10+ repos"*).
- `✓` [`3-pain/user-pain.md`](../3-pain/user-pain.md) — breakage is what gets filed and reacted to, at 182 and now 6,592.

**How true.** The `✓` half says **what people file about**: breakage. The `*` half says **what made
one person start keeping a collection**: reassembly. Those are different questions, the disagreement
is real, and **both stay** (rule 4). Still `?`: whether either converts a stranger into a user.

**What would move it.** Four more interviews, and specifically guide Q25 — *did you go looking, did
you find anything, did you keep using it.*

---

### NK-2 — How large is one person's library? `✓` + `*`

**Answer. Twenty to forty items — and stage 5's 300 has nothing behind it.**

**Rests on.**
- `✓` [claude-code #28729](https://github.com/anthropics/claude-code/issues/28729), 151 reactions: *"Once you get to **20-30+ skills** with multiple contributors, it becomes difficult to manage."* The `✓` is that this was written and reacted to — not that 20–30 is a population truth.
- `✓` [claude-code #10238](https://github.com/anthropics/claude-code/issues/10238), 168 reactions — a team hitting the limit of *"a flat list of skills"*.
- `*` [interview, Q3](agent-setup-interview.md): *"11 skills, 6 CLAUDE.md templates…, an `mcp/` folder with 9 server configs, a `prompts/` folder…, a `scripts/` folder… **Call it 40-something files.** Somewhere around **6k lines**."*
- `?` [`5-patterns/patterns.md`](../5-patterns/patterns.md) — the **300-item** figure the chosen shape was priced against. Reasoned, never measured, and now contradicted by every actual report.

**How true.** The order of magnitude comes from two independent instruments; they agree with each
other and disagree with us. **`CLAUDE.md` §11's ~30 is the well-supported number; stage 5's 300 is
not.** That matters because §8's accepted cost — no library pane — was priced against surviving 300.

**What would move it.** Three more people answering guide Q3 with a count.

---

### NK-3 — How fast does it grow? `*`

**Answer.** From one file to roughly forty in fourteen months — **by accretion after irritation, and
never downward.**

**Rests on.**
- `*` [interview, Q4](agent-setup-interview.md): *"**Fourteen months**, give or take. It started as **exactly one file**."*
- `*` [interview, Q18](agent-setup-interview.md): *"deleting feels riskier than keeping. If I remove something and quality drops, I won't connect the two events… **So the folder only grows, which is a bad property for a thing whose job is to be precise.**"*

**How true.** One person, from memory; the curve is a recollection. The **mechanism** is the useful
part — grows on irritation, never shrinks because deletion has no feedback loop — and it is specific
enough to design against and specific enough to be wrong.

**What would move it.** Not a conversation. This one wants a real folder, examined with its git log.

---

### NK-4 — How often is a tool like this opened? `*`

**Answer.** The **agents** are open constantly. The **collection** is opened for three reasons, and
reviewing it is not one of them.

> *"Three modes, in descending frequency. Most often I'm **copying something out of it** into a new
> project. Second, I'm **adding a rule right after the agent did something annoying**… Third, and
> rarest, I'm **looking for something I know I wrote and can't find**… **I basically never go in
> there to read or review. There's no reason to, nothing prompts it, so it doesn't happen.**"*
> — [interview, Q19](agent-setup-interview.md) `*`

**Rests on.** That quote, plus `*` [Q2](agent-setup-interview.md) — *"About forty minutes ago. It's
open right now in another tab."*

**How true.** One person. But three named modes are a brief, and the third one — searching for
something he wrote and cannot find — is the only sighting of *loss* anywhere in this repository.

**What would move it.** Guide Q19, four more times. If the three modes recur, they are the Library
screen's requirements.

---

### NK-5 — How many agent targets does one person keep? `✓` + `*`

**Answer. Two to four** — and **one source feeding all of them is the loudest demand anywhere in this
repository's evidence base.**

**Rests on.**
- `✓` [claude-code #6235](https://github.com/anthropics/claude-code/issues/6235) — **6,592 reactions**: *"CLAUDE.md feels too specific to Claude Code. It doesn't work as well when collaborating with other developers who aren't using Claude Code."* Plus the twelve-issue family in [`re-research.md`](re-research.md) R1, across three vendors' trackers.
- `✓` [`re-research.md`](re-research.md) R2 — six practitioners describing their own setups in public, and **25 comments** across eight downloaded HN threads about symlinking one source into several formats.
- `*` [interview, Q1](agent-setup-interview.md) — four installed (Claude Code, Cursor, Codex CLI, Aider) plus a dead Continue; two used yesterday.

**How true.** Split the row in two, because the header used to hide the split. **The demand is `✓`**:
re-runnable queries, three trackers, a five-figure reaction count, and what is confirmed is that
thousands of people asked for one instruction source across agents. **The per-person count is `*`** —
six people describing their own setups in public plus one interview, which is self-report seven times
over and, under rule 5, does not become a measurement by being public. *Two to four* is the number to
design against and not a number to quote.

**What would move it.** Nothing urgent. Best-evidenced row in the document.

---

### NK-6 — Where does the material live today? `✓` + `*`

**Answer.** For the one person asked, in a **git repository he owns**, symlinked into the places each
agent expects. At population level, what is established is narrower: **people care intensely where
this material sits, and a weighted request exists for git to be the source of truth.**

**Rests on.**
- `✓` [`re-research.md`](re-research.md) R5 — [#1455](https://github.com/anthropics/claude-code/issues/1455) XDG at **446 reactions**; [#28729](https://github.com/anthropics/claude-code/issues/28729) asking for a **git repo as the source of truth**; `agent-dotfiles` and `SkillCatalog` built on exactly that premise.
- `*` [interview, Q3](agent-setup-interview.md): *"`~/dev/kit/agents/`, which is a **private GitHub repo** called `agent-kit`. It gets **symlinked** into `~/.claude/` and a couple of other places."*

**How true.** Weaker than it read before 2026-09-08. `✓` covers three things: that 446 people reacted
to a request about *where the config directory lives*, that a filer asked for **a git repo as the
source of truth**, and that tools built on that premise exist. Note what the second one means —
**a request is evidence that this is not yet how that person works.** The actual arrangement in the
answer above, a private repo symlinked into `~/.claude/`, is **one practitioner's**, `*`. The two
instruments point the same way; only one of them observed anybody.

**What would move it.** The instrument stage 6's plan named and nobody has run: a GitHub search for
repositories that actually carry `.claude/`, `CLAUDE.md`, `.cursor/rules` and `AGENTS.md` side by
side. That would observe the arrangement instead of asking about it. Guide Q3 corroborates cheaply.

---

### NK-7 — Does the person work alone, or does anyone else open the archive? `✓` + `*`

**Answer. Not alone — and the handover failed silently for two days.**

> *"A contractor… I gave him the repo including the agent config, and he got roughly the same
> experience as my Linux move: paths broken, one server not starting, and **he assumed that was
> normal and worked around it for two days without mentioning it**… That was the moment I understood
> the config had become **tribal knowledge rather than a setup**."*
> — [interview, Q21](agent-setup-interview.md) `*`

**Rests on.**
- `*` Q21 above, and [Q22](agent-setup-interview.md) — given away twice, informally, each time needing twenty minutes of live explanation of *"which files are load-bearing and which are aspirational."*
- `✓` [`re-research.md`](re-research.md) R12 — #6235's stated motive is collaboration with developers on other agents; [#10238](https://github.com/anthropics/claude-code/issues/10238) *"with my team"*; [#28729](https://github.com/anthropics/claude-code/issues/28729) *"multiple contributors"*.

**How true.** Both instruments agree and one is re-runnable. **It weakens a premise the spec leans
on**: §6 justifies *nothing blocks* partly with *"it is the user's own library on their own machine."*
Sometimes it is not, and the second party lost two days without knowing anything was wrong.

**What would move it.** Nothing. What is open is what we *do* about it, which is design, not research.

---

### NK-8 — Has anyone ever wanted a previous project back? `*`

**Answer. Yes — and the interesting half is why he could not have it.**

> *"The eval harness from the invoice project. **It's the best thing I've built for this category of
> work**… I didn't bring it because it's **welded to that project's data model**. Extracting it means
> either doing a proper generalization pass, which is half a day I wasn't going to bill anyone for, or
> copying it and mutilating it, which is **how I ended up with three divergent copies of the chunking
> module**. So I wrote a worse thing from scratch in an hour and told myself I'd fix it later. **I did
> not fix it later.**"* — [interview, Q8](agent-setup-interview.md) `*`

**Rests on.** That answer alone. **Nothing in the repository, in either direction, before it.**

**How true.** One person — but the first evidence this question has ever had, and it answers more
than it was asked. The blocker is not *finding* the previous thing; it is that the thing is
**entangled with its project**. That is an argument about item granularity, and it lands next to
`detached` / `overrides` in §5.

**What would move it.** Guide Q8, four more times. If it recurs, it is a job for stage 7's matrix.

---

### NK-9 — Would anyone adopt this at all, and why? `*`

**Answer. Still the weakest row**, and the one data point is about **lapsing, not rejecting**:

> *"Yeah, twice, both times right after being burned… There are session viewers and log tools, and
> they tell you what happened in the conversation, which isn't the same question… **I used one for
> about a week**, mostly to look at token counts, **then stopped**, and I couldn't tell you the exact
> day I stopped."* — [interview, Q25](agent-setup-interview.md) `*`

**Rests on.**
- `*` Q25 above — searched twice, adopted briefly, drifted away without a decision.
- `✓` [`re-research.md`](re-research.md) R8 — the adjacent category is crowded with free tools at 400–4,500 stars, so *nothing exists* is not a reason anyone would come to us.

**How true.** One person's lapse is not a market signal. What it establishes is the **shape of the
risk**: exactly our audience, went looking unprompted, found something adjacent, and **left silently**.

**What would move it.** Q25 four more times, and above all the **P5 recruit** — someone who does not
keep this material at all. The guide asks for it; it has not happened.

---

### NK-10 — What do they do today instead? `✓` + `*`

**Answer.** `cp -r`, symlinks, `@AGENTS.md` include lines, wrapper scripts, home-made managers.
**And notably not the automation they already built:**

> *"The CLAUDE.md, the two skills, the MCP config. All of it moved by `cp`. **Not by git submodule,
> not by a package, not by the bootstrap script that exists specifically to do this.** By `cp -r`
> from a sibling directory."* — [interview, Q7](agent-setup-interview.md) `*`

**Rests on.** `✓` [`re-research.md`](re-research.md) R2 and R8 · `*` Q7 above.

**How true.** Two instruments agree, and rule 5 says what the `✓` is actually carrying: **twenty-five
comments and several issues in which people say they symlink** — the utterance, re-readable by anyone.
Nobody watched a single one of them do it, and repetition does not promote self-report. The `*` adds
what no amount of that could see: **a person who built the automation and still copied by hand**,
because his tool covered the global layer and not the per-project one. That is a warning about where
our own value has to sit, and it is the most useful sentence in the row.

**What would move it.** Nothing. Corroborate in passing.

---

### NK-11 — What would make someone distrust the check? `✓` + `*`

**Answer, and it is not the question we thought we were asking.** The distrust on record is not *your
checker may be wrong*. It is **half of my own material may be doing nothing.**

> *"Maybe **half of it**, if you want the real answer."* — [interview, Q16](agent-setup-interview.md) `*`
>
> *"Properly, no. **I've never A/B'd anything**… each individual file feels too small to justify the
> ceremony, and it's forty small things, so the total never gets audited."*
> — [Q17](agent-setup-interview.md) `*`
>
> *"The rule that got applied should have been **traceable**. I want to be able to ask, after the
> fact, **which instruction produced that behaviour**. Right now I can't, so I guess, and **my
> guesses are unfalsifiable**."* — [Q14](agent-setup-interview.md) `*`

**Rests on.**
- `*` The three quotes above.
- `✓` [`re-research.md`](re-research.md) R7 — the same doubt across the HN threads: *"mostly useless… 50/50 or less that Claude.md even reads/uses this file"*, *"I can never quite tell if it's helping anything"*, and a story titled *I am morally opposed to updating my Claude.md*.
- `✓` R6 — with a real security fear underneath it: [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/), 3,984 skills scanned, 13.4% carrying critical issues. **`✓` that the study is published and readable at origin, not that we verified it** — we cannot re-run the scan, Snyk sells security tooling, and its own post does not reconcile *36%* in the headline with *36.82%* for a different measure in the table. The order of magnitude is what this carries.

**How true.** `✓` and `*` agree from independent instruments — the strongest combination available
here. **The consequence is uncomfortable**: our validation pass answers *does this set cohere*, and
the doubt on record is *does any of this do anything*. Not the same promise. See NK-23.

**What would move it.** Nothing; this is established. What to do about it is a register question.

---

### NK-12 — Is a usage fact persuasive, or is it noise? `*`

**Answer. Persuasive — and he asked for it in our own words, unprompted.** Guide Q20 is deliberately
open and **forbids offering** *used in 3 projects* as an option, precisely so that an answer would be
worth something:

> *"**Usage data, first.** Just: **this file was loaded in 40 sessions, this one in 2, this one never.
> That alone would let me delete half of it with confidence.** After that, some record of when a rule
> got applied and what it changed… And a **date. Not created-date, last-actually-useful date.**"*
> — [interview, Q20](agent-setup-interview.md) `*`

**Rests on.** That answer, under the open-question rule in [`interview-guide.md`](interview-guide.md) §4.

**How true.** One person — but this is the strongest **form** a `*` can take: an unprompted invention
of the exact mechanism `CLAUDE.md` §5 already chose, by someone who had never seen the spec. **It
confirms the decision and extends it**: he wants *last actually useful* rather than *last exported*,
and he wants the count **per session** — which our data model does not currently produce.

**What would move it.** Q20 four more times, still open. Two more unprompted inventions would make §5
as close to validated as this method allows.

---

### NK-13 — Does a receiving agent set a project up correctly from `SETUP.md` alone? `?`

**Answer. Nobody knows and nobody has tried.** The only row in the register that is **blank and ours
to fill.**

**Rests on.** Nothing. `CLAUDE.md` §6 and the Q2 disposition in [`FINAL.md`](../FINAL.md) commit to it
on reasoning alone.

**How true.** `?`. It is not a question about people at all — it is a claim about a **machine's**
behaviour, it is the spec's most load-bearing bet, and it has never been run once.

**What would move it.** **Us, in an afternoon.** Compose a small set by hand, write the `SETUP.md` §6
describes, hand the archive to a fresh Claude Code, Cursor and Codex, record what each actually does.
Adjacent evidence says the target is real: `*` [interview, Q11](agent-setup-interview.md) — a
devcontainer with Node 18 against a server needing 20+, and *"broken config doesn't announce itself,
**it degrades quietly**."*

---

### NK-14 — Is hand-entered metadata ever actually maintained? `✓` + `*`

**Answer. No — and the failure has a price tag.**

> *"Same code in three projects. I fixed an off-by-one… on a Friday, and it never got back to the
> other two. **Six weeks later a client flagged** that retrieval was returning fragments cut
> mid-sentence, which is exactly the bug I'd already fixed elsewhere… I debugged it for **three
> hours** as if it were new before I opened the other repo and saw my own fix sitting there."*
> — [interview, Q10](agent-setup-interview.md) `*`

The same loop runs in the instruction files, which is our object exactly: a rule fixed in project B
and never in the template, *"so the next copy is wrong too. **It's a loop.**"*

**Rests on.**
- `*` Q10 and [Q18](agent-setup-interview.md).
- `✓` [claude-code #9444](https://github.com/anthropics/claude-code/issues/9444) — *"Maintenance burden… Inconsistency risk — **copies can drift out of sync**"*, filed and reacted to.
- **Not `✓`** — [`1-landscape/competitors.md`](../1-landscape/competitors.md) on Backstage's known failure mode, *catalogs rot when nobody maintains the metadata*. That is our own stage-1 write-up of community lore about someone else's product; it corroborates and it measures nothing. Re-marked 2026-09-08.

**How true.** Two instruments and one piece of corroboration, all saying the same thing. **A `✓`-grade conclusion
about the world with a `*`-grade story about the cost.** The header used to say `*`, which contradicted
this paragraph and the *Rests on* above it; corrected 2026-09-08. It is also the register's strongest
argument for the live link in §5 — that mechanism exists to break precisely this loop.

**What would move it.** Nothing. Act on it.

---

### NK-15 — Are the loud pain and the quiet pain the same person? `*`

**The question the whole interview guide was built around**
([`interview-guide.md`](interview-guide.md) §1), because no amount of searching can join two reaction
counts to one identity.

**Answer. For this person, yes — and he volunteers a causal direction we had not considered.**

> *"**Already had the collection, and that's the point.** When it was one file I knew what was in it.
> At forty files with overlapping instructions **I have no working model of what's active on a given
> run. The collection created the problem.**"* — [interview, Q15](agent-setup-interview.md) `*`

**Rests on.** That answer, produced by guide Q15, which exists solely to make this join.

**How true.** **One person, and the row needs five.** But note what it is: not two pains sitting side
by side in one person — a claim that **the second pain is caused by having a collection at all.** If
that holds, the persona does not split into *breaks at handover* versus *collector*; **the collector
becomes the person who breaks**, and the primary-persona argument changes shape entirely.

**What would move it.** Four more Q15 answers, with the block-B / block-C marks on each sheet.
**Until then no primary persona may be declared** — which is the whole point of §1 of the guide.

---

### NK-16 — Are tracker filers the same population as `CLAUDE.md` §3's audience? `?`

**Answer. Unresolved — and this interview could not resolve it**, because the respondent *is* a filer:

> *"One issue, about MCP config path handling… Got a reasonable answer, not much came of it. Written
> about it, no. **I've drafted a post twice** about how these config folders rot and **deleted it both
> times** because it felt like complaining without a solution."*
> — [interview, Q24](agent-setup-interview.md) `*`

**Rests on.** `*` Q24 · `✓` [`re-research.md`](re-research.md) R1 — the corpus is at least now the
tracker of the product our audience actually uses rather than a dead competitor's.

**How true.** `?`. One filer says nothing about non-filers. The useful part is the last line: **the
pain is felt more often than it is reported**, because the report gets deleted for lacking a solution.
That is a mechanism for tracker under-count, and it is `*`.

**What would move it.** The guide's recruiting rule — **at least two of the five must never have filed
anything in public.** Not yet satisfied.

---

### NK-17 — What is the emotional register on arrival? `*`

**Answer. Irritation, mostly — and it is baked into the material.**

> *"…I'm adding a rule right after the agent did something annoying, which means **most edits are
> written while irritated, which is probably visible in the tone of some of them**."*
> — [interview, Q19](agent-setup-interview.md) `*`

**Rests on.** That quote, plus Q19's three modes (NK-4).

**How true.** One person. But it is the first answer this question has ever had, and it is exactly the
kind of thing no tracker could produce: **the library is written in anger and read in a hurry.** It
bears on tone, on the copy register (§6), and on what an item card should surface.

**What would move it.** Guide Q19, four more times.

---

### NK-18 — Does anyone want their work to be a portfolio? `✓` + `*`

**Answer. Two searches found nothing. The one person asked said a qualified yes — for a motive that
has nothing to do with being seen.**

> *"None of it. I'd like a slice of it public, mostly for the reason that **publishing forces cleanup
> and I need external pressure to do that**. But I can't publish as-is because client-specific rules
> are scattered through it…"* — [interview, Q23](agent-setup-interview.md) `*`

**Rests on.**
- `✓` [`re-research.md`](re-research.md) R10 — **0 of 1,762** HN comments; `portfolio in:title` in `anthropics/claude-code` returns **2 issues, both 0 reactions, both unrelated**.
- `*` Q23 above.

**How true.** **These disagree and both stay** (rule 4). The `✓` absence is real and was looked for
deliberately. The `*` reframes rather than contradicts: the want is **not to be seen, it is a forcing
function for cleanup**, and it is blocked by client material tangled through the files. `CLAUDE.md`
§9's decision to keep publishing out of the MVP is untouched by either.

**What would move it.** Q23 four more times, and the answer recorded plainly whichever way it falls.

---

### NK-19 — Under what licence may someone else's skill ship in our public library? `✓` + `?`

**Answer, for the general rule. Not a research question any more — a field and a rule.**
**For the question as actually asked — under what licence may *these* items ship on *our* shelf — the
answer is still `?`, because no item on the planned shelf has had its licence looked at.**

**Rests on.** `✓` [`re-research.md`](re-research.md) R11 — the Agent Skills format carries an
**optional `license` field**; real catalogs pick one and say so
([tech-leads-club](https://github.com/tech-leads-club/agent-skills), CC-BY-4.0;
[awesome-legal-skills](https://github.com/lawve-ai/awesome-legal-skills), CC BY-NC-ND 4.0, with
included resources keeping their own terms); and the governing principle: **a publicly accessible
skill is not necessarily free of restrictions, and a missing licence field does not prove that reuse
is permitted.**

**How true.** `✓` for the rule, and the rule is the easy half. **`?` for the shelf**, and that is the
half with work in it: §5's `Item` carries `repoUrl`, `path` and `ref` and **no licence field**, §11's
*"checked sources"* has no stated review standard, and **not one candidate item has been checked** —
which, given R6's 13.4%, is the same gap the security proposal is about. Marking this row a plain `✓`
made a decided rule look like a cleared shelf. Both halves are proposals in
[`re-research.md`](re-research.md) §4.

**What would move it.** Deciding the rule closes nothing on its own. The `?` closes only when the
shelf is actually built and each item's licence is recorded beside its `ref`.

---

### NK-20 — Does the person hitting the environment pain even have a library? `*`

**Answer. Yes — in the same sentence that answers NK-15.** The worry behind this row was that *the
archive lands and does not run* might belong mostly to people installing **one** server, in which case
the pain is real and **not ours**. For this person it is not that:

> *"Already had the collection, and that's the point… **The collection created the problem.**"*
> — [interview, Q15](agent-setup-interview.md) `*`

Corroborated by the scale of his failures: `*` [Q5](agent-setup-interview.md) — four MCP servers
silently not starting on Linux because of absolute paths copied from a docs example; `*`
[Q12](agent-setup-interview.md) — *"**one in three fresh environments** has something silently not
loading."*

**Rests on.** Q15, Q5, Q12. **One person.**

**How true.** `*` — and it **shares its evidence with NK-15**, so the two rows are not independent
confirmations of each other. Worth stating, because counting them twice would be the easiest mistake
in this document.

**What would move it.** Guide Q15, four more times.

---

## Three questions the interview added

The protocol says questions land in the register as work turns them up. The interview turned up three
— two of them in answer to *"anything I should have asked?"* — and **none was among the twenty.**

### NK-21 — What happens when the user's own rule and an external requirement conflict? `*`

> *"You didn't ask what happens when a rule and a client requirement conflict. **That comes up
> constantly.** My CLAUDE.md says one thing, the client's linter says another, and **there's no
> precedence anywhere**; it's resolved by whichever I remember at the time, which is a bad way to
> resolve anything."* — [interview, Q26](agent-setup-interview.md) `*`

**Why it matters.** §6 models conflicts **between items in our library**. This is a conflict between
an item and **something outside the set entirely** — a linter, a client standard, a repo convention —
and the data model has nowhere to put it. Neither `conflicts` nor `requires` reaches it.

### NK-22 — How much of what makes a setup work was never written down? `*`

> *"Roughly **half of what makes a project go well is stuff I've never written down** because writing
> it down felt too obvious. Then a contractor joins and none of it transfers. If you're studying why
> these setups fail, **'the written part was never the whole thing'** is probably a bigger factor than
> anything about the files themselves."* — [interview, Q26](agent-setup-interview.md) `*`

**Why it matters.** It bounds the ceiling of the entire product. We validate the written part. If the
written part is half the system, a perfectly coherent archive still under-delivers at handover —
which is exactly what happened to his contractor (NK-7).

### NK-23 — Is the wanted thing observability rather than validation? `*`

Asked what one thing a genie should fix, he did not ask for a checker:

> *"**Show me what actually loaded and what actually mattered.** Per session: these files were read,
> this rule fired here, **these six things were present and had no observable effect.** That's it. I
> don't need it to fix anything, **I need to see it**, because everything else I'd fix myself in an
> afternoon if I could see it."* — [interview, Q25](agent-setup-interview.md) `*`

**Why it matters.** `CLAUDE.md` §2 says the core value is **assembly with validation**. The one
practitioner asked wants **observability of what ran**. Those overlap and they are not the same
product — and one of them we cannot build, because we run nothing on anyone's machine (§6). **This is
the sharpest open question in the folder**, and it belongs in the sitting that closes stages 6 and 7,
as a register entry with a named instrument: guide Q25, four more times.

---

## What this section changes

**Nothing, still.** It is a register, and registers are read before decisions rather than instead of
them. It edits no file outside this folder.

**What it hands forward.**

1. **To the axes (step 2).** NK-15 is the one that matters, and its `*` answer suggests the axis may
   not exist as drawn: if the collection *causes* the breakage, then *collector* and *person who
   breaks* are one persona at two moments, not two personas.
2. **To the audit (step 4).** The dangerous list writes itself from this section — **every row
   carrying only `*` bears on a design decision and stands on one person**: NK-8, NK-9, NK-12, NK-15,
   NK-17, NK-20, NK-21, NK-22, NK-23.
3. **To the owner, as work rather than research.** **NK-13 is the only blank row we can fill
   ourselves**, it needs an afternoon, and it tests the spec's most load-bearing bet.
4. **To the register in [`research-plan.md`](../research-plan.md).** NK-21, NK-22 and NK-23 are
   candidates for Q10, Q11 and Q12, each with a named instrument, to be dispositioned in the same
   sitting as Q7–Q9 once stage 7 is in.

---

# D. The behavioural axes

**Stage 6, step 2. Written 2026-09-08**, after section C and before `personas.md`, because the plan
([`README.md`](README.md), step 2) forbids writing a persona until the thing that would separate one
from another has been named and checked. **The rule that governs this section: no axis is
demographic, and an axis is only used to split a persona if there is evidence at *both* ends.** An
axis with evidence at one end is recorded and **not used** — a one-ended axis produces a persona and
its shadow, which is invention wearing a table.

**Every axis below was proposed in step 2 of the plan or produced by section C, and each is stated as
a behaviour someone could be observed doing.**

| # | The axis | Evidence at end A | Evidence at end B | Used to split? |
|---|---|---|---|---|
| **X1** | **Does anyone else ever open this material?** *Solo* ↔ *handed over* | **`✓` Solo.** 182 ranked issues across two trackers contain **not one** about a team, a colleague, an organisation, a rollout or a sync — OBS-2, a title search run over the raw JSON | **`✓` Handed over.** [#6235](https://github.com/anthropics/claude-code/issues/6235)'s stated motive is *"collaborating with other developers who aren't using Claude Code"* (6,592); [#10238](https://github.com/anthropics/claude-code/issues/10238) *"with my team"* (168); [#28729](https://github.com/anthropics/claude-code/issues/28729) *"multiple contributors"* (151). Plus `*` the contractor who lost two days — NK-7 | **Yes.** Both ends re-runnable, and the two ends want different things from the same archive |
| **X2** | **How many agent targets does the same material have to serve?** *One host, non-negotiable* ↔ *two to four, kept in sync by hand* | **`✓` One host.** The most-reacted issue in the stage-3 corpus is *bring this to the editor I already use* — [continue #917](https://github.com/continuedev/continue/issues/917), **245 reactions**; and #759 at 115, #1440 at 24 — OBS-3 | **`✓` Several.** [#6235](https://github.com/anthropics/claude-code/issues/6235) at **6,592** plus a twelve-issue family across three vendors' trackers; **25 HN comments** about symlinking one source into several formats — R1, R2 | **Yes.** The strongest pair of ends in the document |
| **X3** | **What does the person believe their own material does?** *It works, I just cannot find it* ↔ *half of it may do nothing* | **`?`** Nothing observed anyone believing their material works. The nearest thing is that people keep adding to it, which is not the same claim | **`✓` + `*` Doubt.** *"Mostly useless… 50/50 or less that Claude.md even reads/uses this file"* — [saberience](https://news.ycombinator.com/item?id=46106423); an HN story titled *[I am morally opposed to updating my Claude.md](https://news.ycombinator.com/item?id=49376287)*; and `*` *"Maybe half of it, if you want the real answer"* — R7, NK-11 | **No — one-ended.** Recorded because end B is heavily evidenced and belongs in **every** card, not because it separates anybody |
| **X4** | **Does the person write their own material, or install other people's?** *Author* ↔ *consumer* | **`✓` + `*` Author.** The whole of section A is people configuring their own things; `*` a repo grown from one file over fourteen months — NK-3 | **`V` Consumer, vendor-grade only.** An entire tool category exists to install other people's skills (R8, 425–4,526★) and catalogs report skills at six and seven figures (R9) — **but every one of those numbers is a vendor's or a tool's own count, and not one person was observed consuming** | **Yes, with a warning printed on it.** Used because §8 and §11 already ship a surface for end B; **end B has no observed person behind it**, and the persona built on it says so in every line |
| **X5** | **Does the person file when it breaks, or absorb it silently?** *Files* ↔ *works around it* | **`✓` Files.** The entire evidence base is, by construction, people who filed | **`*` Absorbs.** The contractor *"assumed that was normal and worked around it for two days without mentioning it"*; and the respondent *"drafted a post twice… deleted it both times"* — NK-7, NK-16 | **No — this is a sampling caveat, not a split.** It says our portrait is drawn from filers (NK-16) and must be labelled as such wherever it is used |
| **X6** | **Is the collection the victim of the breakage, or its cause?** *Victim* ↔ *cause* | **`?`** Nobody has said the collection was merely unlucky | **`*` Cause.** *"Already had the collection, and that's the point… At forty files with overlapping instructions I have no working model of what's active on a given run. **The collection created the problem.**"* — NK-15, one person | **No, and it is the most important axis here.** One-ended, `*`, n = 1 — **and if it holds it deletes a split rather than making one.** See below |

## What X6 does to the persona set, and why it is not a split

The plan anticipated the primary-persona choice as a contest: **the person whose pain is *sighted*
— an archive that lands and does not run — against the *collector* the spec is positioned for**
([`README.md`](README.md), step 3). X6 says those may be **one person at two moments**: the
collection grows past the point where its owner can hold it in their head, and *that* is when the
silent breakage starts.

**It stands on one sentence from one practitioner and it may not survive four more conversations.**
But it is the only causal claim anyone has made, and the honest consequence is that we do **not**
build a persona set around a collector/breaker split that the only direct evidence says is a single
person. **The primary persona merges them, and the merge is what four more Q15 answers would
refute** (guide Q15, [`interview-guide.md`](interview-guide.md) §1).

## The axes actually used

**X1 and X2 separate the personas. X4 produces a third that is almost entirely hypothesis and is
labelled as such.** X3 is carried by every card because it is evidenced everywhere and distinguishes
nobody. X5 is a caveat printed on the whole document. X6 is the reason the primary is shaped as it is.

**Nothing here is demographic.** No axis names an age, a job title, a seniority, a city or a tool
preference as such, because [`CLAUDE.md`](../../CLAUDE.md) §3's audience sentence is a claim under
test (section B, A-4 and A-5) and cannot be used to divide people it has not been shown to describe.
