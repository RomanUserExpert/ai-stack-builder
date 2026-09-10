# Re-research — the public record, read four times

**A source document**, in the sense stages 1–3 used the word: it states the question, names the
instrument, logs what was collected, and says what that establishes **and what it does not.**

**Four rounds, merged into one file on 2026-09-10** so that the folder stops being a pile of
`re-research-N.md` with no stated order. **Nothing was dropped and nothing was rewritten** — each
round keeps its own dated part exactly as it was written, including the passes it discarded and the
claims it later withdrew. Where a round contradicts an earlier one, both stay and the later one
says so; that is rule 4.

| Round | Date | Instruments | What it produced |
|---|---|---|---|
| **[1. The public record](#round-1-the-public-record)** | 2026-09-07 | I1–I4 — three issue trackers, 1,762 HN comments, Stack Overflow, GitHub repository search | Eleven of the twenty unknowns moved. A correction to stage 3 and a challenge to `CLAUDE.md` §2 |
| **[2. Counting, not asking](#round-2-counting-not-asking)** | 2026-09-08 | I5, I6, I3b — repository search, **the `git/trees` count**, one Ask HN thread read in full | The 300-item claim refuted by measurement. The first evidence ever collected about P3, and it runs against the shelf |
| **[3. Five questions that need no interview](#round-3-five-questions-that-need-no-interview)** | 2026-09-10 | I7–I11 — **the handover test and the competitors, run on this machine**; forks, blob SHAs, registry series | **NK-13 closed.** The spec’s largest bet holds for performing and fails for checking. One headline withdrawn by its own control |
| **[4. The matrix’s empty cells](#round-4-the-matrixs-empty-cells)** | 2026-09-10 | I12–I15 — two vendor forums, HN searched by situation, **the shelves’ own issue trackers**, and our fork corpus re-asked | **Six matrix cells filled, two numbers raised** — the first upward movement the matrix has had. And the wall behind the rest, named |

**It is not a digest and nothing may cite it as a decision.** The digest entry it feeds is
[`research.md`](../research.md) §§7–9. The register it reports to is
[`research-plan.md`](../research-plan.md).

**Capture logs live in [`_captures/`](_captures/)**, one per round, plus the artefacts of the
handover test in [`_captures/qf-handover-test/`](_captures/qf-handover-test/).

**Rule 5 governs all of it, except where a round says otherwise.** A re-runnable query proves that
something was **said**, not that it is **true**. **Rounds 2, 3 and 4 each break that ceiling in
places** — a file count in a public tree, a blob SHA, a diff, and two experiments we ran ourselves
are measurements rather than utterances, and each is marked where it appears.

---
# Round 1. The public record

> **Collected 2026-09-07.** Four instruments taken to the public record for the first time.
>
> *Merged into this file on 2026-09-10 from the file that was `re-research.md`, unchanged.*

### Re-research — closing what the inventory left open

**Stage 6, step 5, run wide rather than surgically.** Collected 2026-09-07, the same day
[`inventory.md`](inventory.md) was written. **This is a source document**, in the sense stages 1–3
used the word: it states the question, names the instrument, logs what was collected, and says what
that establishes and what it does not. It is not a digest and nothing may cite it as a decision.

The stage plan asked for **one** audit question answered at point scale. The owner asked instead for
as many of the twenty `[?]` rows closed as the public record allows. So this ran four instruments
across three days of work compressed into one sitting, and it moved **eleven** of the twenty rows.

**It also contradicts a signed-off finding and challenges a sentence in `CLAUDE.md` §2.** Both are
recorded here and **neither is applied**. Stages 6 and 7 audit the spec; the owner edits it.

---

#### 1. The instruments, and what each can and cannot see

| # | Instrument | Weighting it offers | What it is blind to |
|---|---|---|---|
| **I1** | **`anthropics/claude-code` issue tracker — 89,923 issues**, searched through the GitHub API, sorted by reactions | Reactions, the same crowd-weighting stage 3 used | Friction that nobody bothers to file. **But see finding R3 — it is much less blind than stage 3 assumed.** |
| **I2** | **`openai/codex` (26,451) and `google-gemini/gemini-cli` (14,163)** | Same | Same |
| **I3** | **Hacker News via the Algolia API** — keyword search plus **eight complete comment threads, 1,762 comments**, downloaded and read locally | Points and comment counts on the *story*; comment scores are not exposed | A self-selecting, English-speaking, HN-shaped population. Loud opinions over quiet practice. |
| **I4** | **Stack Overflow via the Stack Exchange API** | Votes and **view counts** | Almost nothing here. See R14. |
| **I5** | **GitHub repository search**, sorted by stars | Stars, forks, last push | Stars measure attention, not use. A README is a claim, not a product. |
| **I6** | **Web search and page reads** — vendor reports, a security study, ecosystem surveys | None. Vendor content is positioning. | Everything. Cited as **V** and never as demand. |

**Two limits that govern every row below.**

**Reddit could not be read at all.** `reddit.com` blocks our crawler, and r/ClaudeAI, r/ChatGPTCoding
and r/AI_Agents are named by several sources as where this population actually talks. So the largest
practitioner forum in the space is **absent from this document by technical accident**, not by
judgement. Anything below that rests on HN inherits HN's skew and does not get Reddit's correction.

**A reaction count is still ordinal.** 6,592 against 48 says *louder*. It does not say *more
important*, and it never says anything about people who did not file.

**Capture logs, so every number below is reproducible.**

| Log | Holds |
|---|---|
| [`_captures/round1-github.json`](_captures/round1-github.json) | 30 queries, 120 issues — title, reaction count, comment count, state, date, URL. **Plus the full body of all 21 issues quoted in this document**, so the quotes can be checked without re-fetching. |
| [`_captures/round1-hn-threads.json`](_captures/round1-hn-threads.json) | 8 threads, **1,762 comments in full text**, with author, date and item id. |
| [`_captures/round1-hn.json`](_captures/round1-hn.json) | 6 keyword queries, 38 hits, with the `nbHits` each query returned. |
| [`_captures/round1-web.json`](_captures/round1-web.json) | 9 web sources and 9 repositories, each with its **kind**, the specific figures taken from it, its caveat, and an HTTP link check run 2026-09-07. |

**What the logs deliberately do not hold.** Bodies for the 99 issues that were ranked but not
quoted — the ranking used titles and counts, and those are stored. Comment threads for the GitHub
issues. And the READMEs of the nine repositories in R8, which were read live and are quoted in place;
the repository list is logged so they can be re-read.

---

#### 2. Findings

##### R1 — The loudest thing in our audience's own tracker is *one source, many agents*

Stage 3 read `continuedev/continue` and `modelcontextprotocol/servers`. It never read the tracker of
the product our users actually use. That tracker holds **89,923 issues**, and its most-reacted issue
by a factor of two over anything else is:

> **[Feature Request: Support AGENTS.md](https://github.com/anthropics/claude-code/issues/6235)** —
> **6,592 reactions, 389 comments**, filed 2025-08-21
>
> *"Codex, Amp, Cursor, and others are starting to standardize around AGENTS.md — a unified Markdown
> file that coding agents can use to understand a codebase. By contrast, CLAUDE.md feels too specific
> to Claude Code. **It doesn't work as well when collaborating with other developers who aren't using
> Claude Code.**"*

It is not alone, and the family spans three vendors' trackers:

| Issue | Reactions |
|---|---|
| [claude-code #6235 — Support AGENTS.md](https://github.com/anthropics/claude-code/issues/6235) | **6,592** |
| [claude-code #17118 — Support for OpenCode and Max plan](https://github.com/anthropics/claude-code/issues/17118) | 1,416 |
| [claude-code #2511 — Connect Claude Code to Claude.ai Projects knowledge bases](https://github.com/anthropics/claude-code/issues/2511) | 624 |
| [claude-code #31005 — Support for AGENTS.md and `.agents/skills/`, "the community has been asking since August"](https://github.com/anthropics/claude-code/issues/31005) | 472 |
| [claude-code #20697 — Sync Skills between Claude Desktop and Claude Code CLI](https://github.com/anthropics/claude-code/issues/20697) | 161 |
| [claude-code #28791 — Sync conversation history between CLI and desktop](https://github.com/anthropics/claude-code/issues/28791) | 155 |
| [codex #12115 — Dynamically loading nested AGENTS.md](https://github.com/openai/codex/issues/12115) | 114 |
| [claude-code #22648 — Account-level settings sync across devices](https://github.com/anthropics/claude-code/issues/22648) | 47 |
| [codex #6038 — Ability to include files in AGENTS.md](https://github.com/openai/codex/issues/6038) | 36 |
| [codex #17401 — `@include` directive for composable AGENTS.md files](https://github.com/openai/codex/issues/17401) | 21 |
| [claude-code #31992 — Cross-machine session resume](https://github.com/anthropics/claude-code/issues/31992) | 17 |
| [gemini-cli #12345 — Add AGENTS.md to the context filename list](https://github.com/google-gemini/gemini-cli/issues/12345) | 14 |
| [codex #3853 — Support global/centralized instructions + configuration](https://github.com/openai/codex/issues/3853) | 11 |

**Closes: NK-5 at population level.** The multi-target problem is the single loudest demand anywhere
in this repository's evidence base — **thirty-six times** the 182 that stage 3 called the loudest pain
in the ecosystem.

##### R2 — And one person really does keep several targets at once

NK-5's warning was that population variance is not per-person count. That gap is now closed with
people describing their own setups. From the HN threads and from the trackers:

- *"copying and keeping in-sync two files: AGENTS.md and CLAUDE.md **since I use both, claude, and
  others interchangeably in one project**"* — [freakynit](https://news.ycombinator.com/item?id=48180539), 2026-05-18
- *"I have **a directory of skills that I symlink to Codex/Claude/pi**. I make scripts that
  correspond with them to do any heavy lifting, **I avoid platform specific features like Claude's
  hooks**. I also symlink/share a user AGENTS.md/CLAUDE.md"* — [type4](https://news.ycombinator.com/item?id=47880290), 2026-04-23
- *"I have **4 CLI tools** I use for this setup. Claude Code, Codex, Copilot and Cursor CLI."* —
  [cheema33](https://news.ycombinator.com/item?id=46853351), 2026-02-02
- *"I use a mix of claude code, codex and cursor. **Whichever has more credits left.**"* —
  [rishabhpoddar](https://news.ycombinator.com/item?id=48616074), 2026-06-21
- *"I built this because **I use Claude Code, Cursor, and Codex — and got tired of maintaining the
  same rules in three different formats** (.md, .mdc, AGENTS.md)."* —
  [suntrix3](https://news.ycombinator.com/item?id=47138105), Show HN: AI-Nexus, 2026-02-24
- *"We symlink AGENTS.md and CLAUDE.md to a single file in our repo"* —
  [israrkhan](https://news.ycombinator.com/item?id=48359885)
- **[#20697](https://github.com/anthropics/claude-code/issues/20697)**, 161 reactions: *"Skills
  created in Desktop are not available in CLI… Users have to add the same skill twice. **Current
  Workaround: Manually copy skills to both locations.**"*

**Twenty-five comments** across the eight downloaded threads are explicitly about symlinking or
syncing one source into several agents' formats. The workarounds people report are: a symlink, an
`@AGENTS.md` include line, a wrapper script that creates the symlink and deletes it on exit, and
`ln -s AGENTS.md .github/copilot-instructions.md`.

**Closes: NK-5 at the individual level. Closes: NK-10** — *what do they do today* is **symlinks,
include directives, and hand-written scripts.**

##### R3 — Reassembly cost was filed after all, and stage 3 looked in the wrong shape

This is the finding that corrects a signed-off document.

Stage 3, finding 4, searched `continuedev/continue` for `reuse blocks assistant`, got **0 results**,
and concluded there is *no demand loud enough to file*. [`FINAL.md`](../FINAL.md) and `CLAUDE.md` §9
both lean on it, and Q5 was deferred partly because *an issue tracker records breakage, not
friction*.

**The friction is filed. It is filed as a feature request, not as a bug** — which is why a
bug-shaped search missed it — **and it was filed on the wrong tracker to find it.** Continue's hosted
half was already dead; these are live products.

> **[claude-code #9444 — Support for Plugin Dependencies and Shared Resources](https://github.com/anthropics/claude-code/issues/9444)**, 48 reactions
>
> *"Today, plugins are completely independent units. If multiple plugins need the same agents, hooks,
> or utilities, **each plugin must duplicate these resources.** This leads to: 1. **File
> duplication** — Same agent definitions copied across multiple plugins 2. **Maintenance burden** —
> Updates must be applied to all copies 3. **Inconsistency risk** — **Copies can drift out of sync**
> 4. Storage waste"*

That is our `requires` edge, our live link, and our drift problem, written by a user, in a tracker,
with reactions on it.

> **[codex #17401](https://github.com/openai/codex/issues/17401)**, 21 reactions
>
> *"**No modular reuse across projects.** A developer working across **10+ repos** with shared
> conventions m[ust]…"* — and the request is for an `@include` directive so instruction sets can be
> **modular**.

And in a practitioner's own words, with the wish attached:

> *"I have a **~200 line file of style rules that I copy and paste between all my projects**
> (**There's got to be a better way to manage files like that!**) but I can never quite tell if it's
> helping anything."* — [eternityforest](https://news.ycombinator.com/item?id=48638003), 2026-06-22

**What this changes.** Stage 3's *instrument blindness* table said reassembly cost is invisible to a
tracker **by construction**. That is too strong. Reassembly cost is invisible to a *bug* search and
visible to a *feature-request* search. The three-way blindness claim needs re-stating, and the
`0 results` finding needs the note that it was measured on a frozen product.

**Moves: NK-1 and Q5.** Not closed — none of this says reassembly *drives adoption*, only that it is
felt and reported. But *"which of loss / reassembly / breakage is even real"* is no longer symmetric:
**two of the three now have filed, weighted evidence, and loss still has none.**

##### R4 — The first real number on library size, and it disagrees with stage 5

> **[claude-code #28729 — Link a source control repo as the source for organization skills](https://github.com/anthropics/claude-code/issues/28729)**, 151 reactions
>
> *"This sorta works when you have a handful of skills… **Once you get to 20-30+ skills with multiple
> contributors, it becomes difficult to manage** — there's no version history, no review process, and
> no easy way to roll back a bad change."*

Corroborating orders of magnitude: a team hitting the limit of *"a flat list of skills"* and wanting
subfolders ([#10238](https://github.com/anthropics/claude-code/issues/10238), 168 reactions); a
200-line personal rules file (above); a *"terse ~100 line file"*
([p1necone](https://news.ycombinator.com/item?id=44958309)).

**Moves: NK-2.** The threshold where a collection stops being manageable is reported as **20–30
items**, not 300. That **supports `CLAUDE.md` §11's ~30** and **undercuts stage 5's 300-item claim**
(OBS-41), which was reasoned rather than measured and is what the chosen pattern's known cost was
priced against.

**And it carries a second thing the spec refuses.** The same issue asks for *version history* and
*rollback* — which §9 rules out. One request at 151 reactions is not a mandate, and it comes from an
*organisation* context rather than a single user. Recorded, not proposed.

##### R5 — Where the material lives, and where people want it to live

- **[claude-code #1455 — does not respect the XDG Base Directory specification](https://github.com/anthropics/claude-code/issues/1455)** — **446 reactions**, open since 2025-05-31. The same request on Codex: [#1980](https://github.com/openai/codex/issues/1980), 134 reactions.
- **`~/.claude/skills/` versus the Desktop app's own location** — [#20697](https://github.com/anthropics/claude-code/issues/20697), 161 reactions.
- **A git repo as the source of truth** — [#28729](https://github.com/anthropics/claude-code/issues/28729), 151 reactions, asks for exactly that. On GitHub, `SkillCatalog` bills itself as *"a Git-native skill manager"* and `agent-dotfiles` as *"Write AI coding rules once, sync to every agent"*.
- **A personal directory plus symlinks** — R2's quotes.
- **Deliberately nowhere**: *"I really like Claude, but **I don't track Claude resources in our repos.** If something better comes along, I'm better [off]"* — [allknowingfrog](https://news.ycombinator.com/item?id=48184129), 2026-05-18. A refusal to commit the material at all, on lock-in grounds.

**Closes: NK-6.** It lives in dotfiles repos, in `~/.claude/skills/`, in per-project files, and in
symlink farms between them — and a weighted request exists for a **git repo to be the source**.

##### R6 — The fear rows, and they are heavier than anything stage 3 found

**Someone else's material is genuinely dangerous.** Snyk's ToxicSkills study — read from Snyk
directly, not from the vendor report that cites it:

> **3,984 skills scanned** from ClawHub and skills.sh, **2026-02-05**. **534 (13.4%) critical
> security issues. 1,467 (36.82%) at least one security flaw. 76 confirmed malicious payloads; 8
> still public** at the time of writing. Of the confirmed malicious samples, **100% carried malicious
> code and 91% carried prompt injection.**
>
> *"The barrier to publishing a new agent skill on ClawHub? A `SKILL.md` Markdown file and a GitHub
> account that's one week old. **No code signing. No security review. No sandbox by default.**"*
>
> — [snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/)

*(Snyk's headline says "prompt injection in 36%"; the table in the same post gives 36.82% as "any
security flaw". The two numbers are not clearly the same measure and this document does not resolve
which the headline means.)*

**A set you did not assemble, appearing without consent:**

> **[claude-code #20412](https://github.com/anthropics/claude-code/issues/20412)** — **142 reactions**
>
> *"Claude Code 2.1.x **silently syncs MCP servers from the user's Claude.ai web account into Claude
> Code sessions without any opt-in, notification, or consent.** This creates **duplicate MCP
> servers** and significant memory overhead that causes OOM kills."*

**Material silently dropped:**

- [codex #13386](https://github.com/openai/codex/issues/13386): *"Codex **silently truncates
  `AGENTS.md` at 32 KB**… Any instructions past that limit are dropped and never sent to the model —
  **with no warning anywhere.**"*
- [claude-code #9716](https://github.com/anthropics/claude-code/issues/9716), 75 reactions, 69
  comments: the assistant does not notice skills that *are* present in `.claude/skills/`.

**Secrets, at weights that dwarf stage 3's:**

| Issue | Reactions |
|---|---|
| [#32733 — Secure secrets injection for Claude Code on the web](https://github.com/anthropics/claude-code/issues/32733) | 192 |
| [#401 — Claude loads my project's `.env` into its bash environment (!)](https://github.com/anthropics/claude-code/issues/401) | 54 |
| [#29910 — Built-in secrets management](https://github.com/anthropics/claude-code/issues/29910) | 45 |
| [#11927 — `env` vars from `settings.json` not passed to plugins/MCPs](https://github.com/anthropics/claude-code/issues/11927) | 31 |
| [#23642 — Support 1Password `op://` references](https://github.com/anthropics/claude-code/issues/23642) | 24 |
| [#4160 — `.claudeignore` to prevent secret exposure](https://github.com/anthropics/claude-code/issues/4160) | 13 |

**Moves: NK-11.** Confirms OBS-18 and OBS-21 at higher weight. And it raises something the spec has
not considered — see §3.

##### R7 — The doubt that actually dominates, and the spec never anticipated it

NK-11 asked what would make someone distrust our *check*. The threads answer a bigger question: what
these people distrust is **whether any of this material does anything at all.**

- *"I find the Claude.md file **mostly useless**. It seems to be **50/50 or LESS that Claude.md even
  reads/uses this file.** You can easily test this by adding some mandatory instruction… then watch
  it blow through this limit"* — [saberience](https://news.ycombinator.com/item?id=46106423)
- *"my results are very hit or miss. **Claude rarely actually reads the other documentation files I
  point it to.**"* — [sothatsit](https://news.ycombinator.com/item?id=46102180)
- *"…but **I can never quite tell if it's helping anything**"* — [eternityforest](https://news.ycombinator.com/item?id=48638003)
- *"**Blackbox oracles make bad workflows, and tend to produce a whole lot of cargo culting.** It's
  this kind of opacity… that makes me [wary]"* — [bandrami](https://news.ycombinator.com/item?id=46820441)
- A whole HN story titled **[*I am morally opposed to updating my Claude.md*](https://news.ycombinator.com/item?id=49376287)** (29 points, 28 comments)
- *"Until we have deterministic introspection for LLMs, **engineers will always invent weird
  heuristics to detect drift.**"* — [Alpha_Logic](https://news.ycombinator.com/item?id=46106973)
- A commenter cites an arXiv paper claiming AGENTS.md files largely make no measurable difference
  ([Systemerror7A69](https://news.ycombinator.com/item?id=49370316)). **The paper was not read and is
  not verified here.**

Against that, three HN stories in nine months are attempts to *measure* whether this material works:
**SkillsBench** (364 points), **Agent Skills Leaderboard** (135 points), **agent-skills-eval** (79
points), and *[AGENTS.md outperforms skills in our agent evals](https://news.ycombinator.com/item?id=46809708)*
(524 points).

**Moves: NK-11 and NK-12, and not in the direction the spec assumed.** The distrust to design against
is not *"your checker might be wrong"*. It is *"I have written a lot of this and I have no idea
whether it does anything"*. That is the register our copy has to survive, and it bears directly on
`CLAUDE.md` §2's premise that assembly-with-validation is the value.

##### R8 — The ground is not unoccupied any more

`comparison.md` difference 1 says the individual practitioner is unoccupied ground. That was true of
**funded vendors** and was measured in August 2026. It is **not true of open-source tooling in
September 2026.** GitHub repository search, sorted by stars:

| Repository | Stars | Its own description |
|---|---|---|
| [`xingkongliang/skills-manager`](https://github.com/xingkongliang/skills-manager) | **4,526** | *"One app to manage AI agent skills across all your coding tools"* |
| [`jeremylongshore/tons-of-skills-marketplace`](https://github.com/jeremylongshore/tons-of-skills-marketplace) | **2,706** | *"Model-agnostic agent-skills platform with a harness-free canonical [format]"* |
| [`MoizIbnYousaf/ai-agent-skills`](https://github.com/MoizIbnYousaf/ai-agent-skills) | **1,138** | *"Universal skill installer and package manager for AI coding agents"* |
| [`jiweiyeah/Skills-Manager`](https://github.com/jiweiyeah/Skills-Manager) | **986** | *"Free, open-source desktop manager for AI Agent Skills"* |
| [`luongnv89/asm`](https://github.com/luongnv89/asm) | **915** | *"The universal skill manager for AI coding agents"* |
| [`enulus/OpenPackage`](https://github.com/enulus/OpenPackage) | **613** | *"The package manager for coding agent configs"* |
| [`yibie/skills-manager`](https://github.com/yibie/skills-manager) | **440** | *"A native macOS app to manage skills across coding agents"* |
| [`RealZST/HarnessKit`](https://github.com/RealZST/HarnessKit) | **425** | *"One home for every agent… manage skills, MCP servers, plugins, hooks"* |
| [`tankpkg/tank`](https://github.com/tankpkg/tank) | 38 | *"Security-first package manager for AI agent skills"* |

Most were pushed within days of this collection; several on the day of it. On Hacker News the same
category shows up as a stream of Show HNs through 2026 — *AGENTS.lock*, *ArteSync*, *SkillCatalog*,
*Skilldeck*, *HiTank*, *Mother MCP*, *Promptlight*, *"Stop manually syncing rules between Claude,
Cursor, and Codex"* — **almost all of them scoring 1–6 points.** The Show HN scores are a weak
instrument and should not be read as failure; **the stars are the better signal, and they say the
category has real attention.**

**What they do, read from their READMEs** *(a claim, not a product — the same standard as stage 1's
marketing-page reads, and labelled as such)*:

- **`asm`** — *"`asm install` validates frontmatter, **scans security, pins registry commits**"*;
  *"Duplicate audit… removes redundant skills"*; *"Find same-job **near-duplicates** — `asm audit
  overlap`"*; a pre-install scan *"for shell exec, network access, credential exposure"*; a
  **verified badge** in its catalog; and, in its own words, *"Two of the signals the report would
  like to use — **trigger collision** and…"*
- **`HarnessKit`** — a built-in security engine with **18 static analysis rules** and a **Trust Score
  (0–100)** in tiers *Safe / Low / …*; *"**per-agent scanning** — even if multiple agents share the
  same extension, each agent's copy is audited independently — **because versions can drift**"*;
  *"works directly with your agents' native directories… **no shadow copies, no sync conflicts**"*
- **`tank`** — *"today's skill registries have **no versioning, no lockfiles, no permissions, and no
  security scanning**"*; lockfile integrity verification
- **`xingkongliang/skills-manager`** — *"Merges are skill-aware… and **true conflicts never block**:
  your local version stays put until you choose keep mine / use remote / keep both"*

**This is the most consequential finding in the document, and it cuts two ways.**

Against us: `CLAUDE.md` §2 says *"What nothing does today is tell you that a skill needs a particular
MCP server, that two skills write to the same config file, that two items register the same command
name."* **A 915-star tool audits duplicates and near-duplicates and names trigger collision. A
425-star tool detects version drift per agent and scores trust out of 100. A 4,526-star app has
already shipped our §6 principle** — *conflicts never block, you choose* — as a headline feature.

For us: **every one of them is an item-level manager.** Install, sync, audit, scan, score — the unit
is *the skill* and the question is *is this skill safe, duplicated or stale*. On this reading none of
them takes a **named set**, resolves it, checks **that set** for internal coherence — dependencies
between members, env keys collected across the whole set, one merged MCP config — and produces an
**archive with setup instructions written for the machine that receives it**. That is still ours.
But *"nothing does this today"* has become *"nothing does the set-level half of this today"*, and the
difference is not cosmetic.

**It also weakens the reasoning behind §5.** The decision to ship usage facts and never a score was
taken because *the market converged on measured trust and we can measure nothing*. These tools can
measure — they run static analysis over skill content — and they do, at the individual-practitioner
tier. The decision may still be right; **the argument for it no longer is.**

##### R9 — The scale everything else now sits inside

Vendor and third-party reporting — **kind V**, positioning, not demand:

- **more than 2,500 Claude Code plugin marketplaces** registered at claudemarketplaces.com
- **SkillsMP lists ~1.9 million public skills** scraped from GitHub; LobeHub lists 230,000+ skills and 56,000+ MCP servers
- **SkillsBench analysed 47,150 public skills** and found an average quality score of **6.2 out of 12**
- an audit of **22,511 skills found 140,963 issues** — roughly 6.3 each
- *"Discovery is no longer the bottleneck. **Judgment is.**"*
- **"2–3 targeted skills delivered +18.6 points, while monolithic skills reduced performance by 2.9 points"**

— [Agentman, *The Agent Skills Ecosystem in 2026*](https://agentman.ai/blog/agent-skills-ecosystem-report-2026), 2026-06-25. **Agentman is a hard competitor and sells curation**, so every number here favours their thesis. Cited as what a vendor published, never as fact.

The last line is the interesting one for us: if small curated sets outperform large ones, then *a
project is a curated subset* is a performance argument and not only an organisational one. **One
vendor's benchmark is not evidence.** Filed as a hypothesis worth testing, not as support.

##### R10 — Portfolio: searched twice, found nothing

- **0 matches in 1,762 HN comments** for `portfolio`, `show off`, `publish my…`, `share my setup`.
- `portfolio in:title` in `anthropics/claude-code`: **2 issues, both 0 reactions, both unrelated** (a
  finance portfolio and a blocked API request).

**NK-18 stays `[?]`**, but the absence has now been looked for in two instruments rather than assumed.
Consistent with `CLAUDE.md` §9 keeping publishing out of the MVP.

##### R11 — Licensing has a rule shape now

- The Agent Skills format carries an **optional `license` field** in `SKILL.md`, which may name a
  licence or point at a bundled licence file.
- Real catalogs pick a licence and say so: `tech-leads-club/agent-skills` uses **CC-BY-4.0** for
  files its maintainers authored; `lawve-ai/awesome-legal-skills` uses **CC BY-NC-ND 4.0** and states
  that every included resource keeps its own terms.
- The governing principle, stated plainly across those sources: **a publicly accessible skill is not
  necessarily free of restrictions, and a missing licence field does not prove that reuse is
  permitted.**
- There is an open discussion thread on exactly this: `agentskills/agentskills` discussion **#379**,
  *Skill licensing and attribution*.

**Moves: NK-19 from unanswered to answerable.** It is not a design decision; it is a field and a rule.

##### R12 — Team and handover: somebody else does open these

- **[#6235](https://github.com/anthropics/claude-code/issues/6235)**, 6,592 reactions — the stated
  motive is *"collaborating with other developers who aren't using Claude Code"*
- **[#10238](https://github.com/anthropics/claude-code/issues/10238)**, 168 reactions — *"We have
  started using and developing skills **with my team**"*
- **[#28729](https://github.com/anthropics/claude-code/issues/28729)**, 151 reactions — org-level
  skills, *"multiple contributors"*
- [#48322 — Team/Enterprise: shared routines](https://github.com/anthropics/claude-code/issues/48322), 53 reactions
- [#9756 — Auth on private marketplaces](https://github.com/anthropics/claude-code/issues/9756), 37 reactions
- *"**We** symlink AGENTS.md and CLAUDE.md to a single file in **our repo**"* — [israrkhan](https://news.ycombinator.com/item?id=48359885)

**Moves: NK-7.** The material is not always private to one machine. That does not make us a team
product — but it does undercut the premise §6 uses to justify *nothing blocks*: *"it is the user's
own library on their own machine."* Sometimes it demonstrably is not.

##### R13 — Where this population actually is

Named repeatedly across community surveys: **Discord** — Latent Space, Anthropic's own Claude Code
channels, Cursor, Ollama, Hugging Face; **Reddit** — r/ClaudeAI, r/ChatGPTCoding, r/LocalLLaMA,
r/AI_Agents; **Hacker News**; X. This is **methodology for the five Q5 conversations**, not a finding
about people: it says where to find five practitioners, and it says that **the largest of those
venues cannot be read by our tooling.**

##### R14 — Stack Overflow is not where this happens, and that is itself a datum

Five searches returned almost nothing on topic. The two relevant hits are worth their view counts:

- *[How to reuse GitHub Copilot Custom Instructions across all projects](https://stackoverflow.com/questions/79602341/how-to-reuse-github-copilot-custom-instructions-across-all-projects)* — 4 votes, 2 answers, **3,775 views**
- *[Is there any support like agents.md or claude.md in antigravity?](https://stackoverflow.com/questions/79834343/is-there-any-support-like-agents-md-or-claude-md-in-antigravity)* — **2,618 views**

Views are the weakest weighting in this document, and both questions are *the reuse question*. Filed
as corroboration of R3 at low confidence.

---

#### 3. What moved, row by row

> **Standing note added 2026-09-08, after the mark audit.** *Closed* in this table means **closed at
> the level of what the public record can show**, which for most of these rows is *people describing
> their own behaviour in public*. [`research.md`](../research.md) now carries that distinction as
> **rule 5**: a re-runnable query proves that something was **said**, not that it is **true**. Three
> rows this table calls *closed* — **NK-5, NK-6 and NK-10** — were re-marked in
> [`inventory.md`](inventory.md) from a plain `✓` to `✓` + `*`, because the utterance is confirmed and
> the behaviour under it is self-report. **Nothing collected here was withdrawn and no row moved back
> to `?`.** The table is left as written, so that what this collection concluded and what the audit
> made of it are both legible.

| Row | Before | After this collection |
|---|---|---|
| **NK-1** — loss / reassembly / breakage | `[?]` | **Moved, not closed.** Reassembly and breakage both now have filed, weighted evidence (R3, R1). **Loss still has none, in any instrument.** Adoption is still unmeasured. |
| **NK-2** — library size | `[?]` | **Partly closed.** 20–30 items is the reported threshold where a collection stops being manageable (R4). Supports §11's ~30, undercuts stage 5's 300. |
| **NK-3** — growth rate | `[?]` | **Unchanged.** Nothing observed anything over time. |
| **NK-4** — frequency of use | `[?]` | **Unchanged.** |
| **NK-5** — targets per person | `[?]` | **Closed.** Population (R1) and individual (R2). Two to four targets per person is normal; the loudest demand in our audience's tracker is one source for all of them. |
| **NK-6** — where material lives | `[?]` | **Closed.** Dotfiles repos, `~/.claude/skills/`, per-project files, symlink farms; and a weighted request for a git repo as the source (R5). |
| **NK-7** — alone, or handed over | `[?]` | **Partly closed.** Colleagues, teams and org contributors appear throughout (R12). Weakens §6's premise for *nothing blocks*. |
| **NK-8** — wanting a prior project back | `[?]` | **Unchanged.** Nothing found in either direction. |
| **NK-9** — would anyone adopt, and why | `[?]` | **Unchanged, and now harder.** R8 says there are already free tools with thousands of stars in the adjacent space. |
| **NK-10** — what they do today | `[?]` | **Closed.** Symlinks, `@include` lines, wrapper scripts, manual double-copies, and home-made managers (R2, R8). |
| **NK-11** — what would make them distrust | `[?]` | **Moved, and redirected.** The dominant doubt is *does any of this do anything* (R7), not *is the checker right*. Plus a real security fear with numbers behind it (R6). |
| **NK-12** — is a usage fact persuasive | `[?]` | **Unchanged as asked**, but the context changed: competitors ship trust scores at this tier now (R8). |
| **NK-13** — does an agent set up from `SETUP.md` | `[?]` | **Unchanged.** Still only testable by us, and still untested. |
| **NK-14** — is hand-entered metadata maintained | `[?]` | **Weak signal.** *"Copies can drift out of sync"* (#9444) and the staleness thread (R7) say people expect drift. Nobody observed maintenance. |
| **NK-15** — same people, loud pain and quiet pain | `[?]` | **Unchanged. Still unresolvable by counting.** Reactions carry no identity. This remains the single biggest obstacle to choosing a primary persona. |
| **NK-16** — are filers our audience | `[?]` | **Improved but open.** The corpus is now the tracker of the product our audience uses, not a dead competitor's. Self-selection for *people who file issues* stands. |
| **NK-17** — emotional register on arrival | `[?]` | **Unchanged.** |
| **NK-18** — portfolio | `[?]` | **Searched, nothing found** (R10). Still `[?]`, but now a looked-for absence. |
| **NK-19** — licence for redistribution | `[?]` | **Answerable.** An optional `license` field, and the rule that absence ≠ permission (R11). |
| **NK-20** — does the env-pain person have a library | `[?]` | **Unchanged.** Still not joinable per person. |

**Eleven rows moved. Nine did not, and seven of those nine need a person, not a search.**

---

#### 4. What this hands to the audit — proposals, not edits

Recorded here so step 4 can put them to the owner. **Nothing below has been applied, and no file
outside this folder has been changed.**

1. **A correction to `3-pain/user-pain.md`.** Finding 4's *0 results* was measured on a frozen
   product's tracker with a bug-shaped query. The reassembly friction is filed on live trackers as
   feature requests (R3). The *method* section's claim that reassembly is invisible **by
   construction** should become: invisible to a bug search, visible to a feature-request search.
2. **A correction to `user-pain.md` finding 1's superlative**, carried over from
   [`inventory.md`](inventory.md) OBS-4 and now much larger: 182 is not the loudest anywhere. In the
   combined evidence base the loudest is **6,592**, and it is about multi-target support.
3. **A challenge to `CLAUDE.md` §2's *"nothing does this today"*** (R8). ~~The item-level half of our
   thesis is shipped by~~ **Reworded 2026-09-08 after the mark audit: the item-level half of our
   thesis is *claimed by the READMEs of*** several open-source tools with 400–4,500 stars. **We
   installed none of them and ran none of them**, so what is `✓` here is their existence, their stars
   and their push dates; their capabilities are vendor self-description, exactly the standard §2 of
   this document already applied to them. The set-level half — resolve a named set, check it, produce
   an archive with instructions for the receiving machine — appears not to be claimed by any of them.
   The sentence needs narrowing either way, and `1-landscape/comparison.md` difference 1 needs a
   dated note that it surveyed funded vendors. **If the narrowing is ever to be more than a hedge,
   somebody has to install `asm` and `HarnessKit` and see what they actually do** — an afternoon,
   like NK-13.
4. **A challenge to §5's *reasoning*** (R8), not necessarily its decision: the market no longer only
   converges on measured trust at the vendor tier — free tools ship trust scores at the practitioner
   tier. *We choose not to score* is a different argument from *nobody can score but the big vendors*.
5. **A new risk to §11's public library** (R6). We plan to ship a curated shelf of other people's
   skills. In a scan of 3,984 skills from two registries, 13.4% had critical security issues —
   **published by Snyk and read at origin, not re-run or verified by us**, and their own post does
   not reconcile the headline *36%* with the table's *36.82%*. The order of magnitude is the part
   this proposal rests on.
   *Checked sources* in §11 currently means checked for provenance; it now has to mean checked for
   content, and the shelf needs a stated review standard.
6. **A field the `Item` model lacks** (R11): `license`, for public items, with the rule that a
   missing licence is not permission. §5 currently carries `repoUrl`, `path`, `ref` and no licence.
7. **A datum against stage 5's 300-item claim** (R4), which is what the chosen pattern's known cost
   was priced against.
8. **A weakened premise under §6's *nothing blocks*** (R12): *the user's own machine, only party at
   risk* is not always true.
9. **A register entry, not a proposal — the register's own protocol.** *Does the dominant doubt
   (R7 — "is any of this doing anything") mean the validation pass has to prove the set works, rather
   than that it coheres?* That is a different product, it cannot be settled here, and it is the
   sharpest question this collection produced.

---

#### 5. What this collection cannot do

It read the public record harder than anyone had read it. It did not ask anybody anything.

**Q5 is not closed and this document does not pretend to close it.** Every row above is still
someone typing in public, self-selected for having a complaint or an opinion. The rows that need a
person — *why would you adopt this*, *what does the first minute feel like*, *is the loud pain and
the quiet pain the same person*, *has anyone wanted a previous project back* — are exactly the rows
that did not move, and the five conversations remain the instrument. What changed is that
[`interviews.md` the guide](interviews.md#part-1-the-guide) can now be written against **evidence rather than
guesses**: it knows to ask about symlinks, about how many agents someone keeps, about the 20-to-30
threshold, and about whether they believe any of their own material is doing anything.


---

# Round 2. Counting, not asking

> **Collected 2026-09-08.** The five questions the audit raised, and the first instrument here that counts somebody’s collection instead of asking about it.
>
> *Merged into this file on 2026-09-10 from the file that was `re-research-2.md`, unchanged.*

### Re-research, round 2 — the five questions the critique raised

**A source document**, in the sense stages 1–3 used the word: it states the question, names the
instrument, logs what was collected, and says what that establishes and what it does not. Collected
2026-09-08, the same day [`personas-and-jobs-critique.md`](../personas-and-jobs-critique.md) was
written. Capture log beside it: [`_captures/round2-log.json`](_captures/round2-log.json).

**It is not a digest and nothing may cite it as a decision.** The digest entry it feeds is
[`research.md`](../research.md) §7, *Research justification*.

**Two questions came from the critique's Part 3 unchanged (Q-B, Q-C), one came from it and could not
be answered here (Q-A), and two were raised by the critique's dangerous list and added for this
round (Q-D from D-9, Q-E from D-4).**

**One finding contradicts a decision in `CLAUDE.md` §11 and one corrects a cell in our own matrix.
Neither is applied.**

---

#### The instruments, and what each can and cannot see

| # | Instrument | Weighting it offers | Blind to |
|---|---|---|---|
| **I5** | **GitHub repository search API**, unauthenticated | Stars, push dates | Private repositories, and anything unpublished. **The people most like our primary persona keep this material private** — the one practitioner interviewed keeps a *private* repo — so this instrument systematically over-samples people who publish |
| **I6** | **GitHub `git/trees` API**, recursive | **None — it is a direct count** | What any of those files is worth, and whether its owner still uses it. **This is the first instrument in the repository that counts somebody's collection instead of asking them how big it is** |
| **I3b** | **Hacker News via Algolia** — one Ask HN thread, *How do you manage skills files?*, **305 points, 274 comments, filed 2026-09-06**, read in full in four passes | Story points; per-comment scores are not exposed | A self-selecting, English-speaking, HN-shaped population. Loud opinions over quiet practice |

**Rule 5 governs everything below.** Where a row records what a person said, the re-runnable query
proves the **utterance**; the behaviour under it stays self-report. **The I6 rows are the exception**
— a file count in a public tree is a measurement, and it is marked `✓` on that basis.

---

#### Q-A — Does a receiving agent perform the setup from `SETUP.md` alone?

**The critique's D-1: the largest commitment in the spec, standing on nothing.**

##### Answer: not closed, and no web instrument can close it. But the adjacent evidence is not encouraging.

The most on-topic thread available was read in full for anyone automating this. **What people
actually use is human-written automation, not an agent reading prose:**

- *"manage them as part of my dotfiles using **chezmoi**. A `.agents/skills/` directory + a symlink"* — [jameshiew](https://news.ycombinator.com/item?id=49592102) `✓`
- *"I wrote a small **command-line tool** that installs skill packs into agent-specific project folders."* — [politician](https://news.ycombinator.com/item?id=49594099) `✓`
- *"configuration file of marketplaces and other skills to fetch… run **`skills.py`** to clean/fetch"* — [toffelx](https://news.ycombinator.com/item?id=49595485) `✓`
- *"relying on **vercel-labs/skills** is sound. It handles global installs"* — [FailMore](https://news.ycombinator.com/item?id=49595591) `✓`
- *"We have a **bootstrap script** to deploy company-managed skills to each developer's personal skills."* — [joshuanapoli](https://news.ycombinator.com/item?id=49592107) `✓`

**Two comments in 274 describe an agent acting on this material at all**, and neither is a setup:
an agent *editing* skills on request ([yatsyk](https://news.ycombinator.com/item?id=49594490)), and
an *"agentic workflow [that] runs biweekly to check if their content drifted compared to the docs and
opens PRs"* ([theletterf](https://news.ycombinator.com/item?id=49594183)).

**What this does and does not say.** It does **not** say a receiving agent cannot perform a setup
from a precise document — nobody in the thread was trying that. It says that **in the largest sample
of practice available, the job is being done by scripts and package managers**, and that the spec's
bet is not a thing people are currently reaching for. `CLAUDE.md` §6's bet is still untested, **and
it is now visibly against the grain of current practice** rather than merely unverified.

**NK-13 stays `?`.** The instrument is unchanged and it is still ours: compose a set by hand, write
the `SETUP.md` §6 describes, hand the archive to a fresh Claude Code, Cursor and Codex, and record
what each does. **Half a day, on this machine, and it is the highest-value unspent half-day in the
project.**

---

#### Q-B — Who receives a handed-over setup, and what happens?

**The critique's D-2: P2 stood on one author's motive sentence and one second-hand story.**

##### Answer: the population is confirmed. The first hour is still unobserved.

Six independent people in one thread describe **distributing this material to other people**:

> *"We have some company-managed skills, that help coding agents find the relationships between our
> repos, and our conventions, architecture… These are supposed to be portable between agents, and so
> **distributing them is currently awkward**."* — [joshuanapoli](https://news.ycombinator.com/item?id=49592107) `✓`

> *"skills need to be edited across projects and **across team members** in a controlled way.
> **Git is of course required for this but is not enough**"* — [mstr32](https://news.ycombinator.com/item?id=49594219) `✓`

- *"I commit them to git (**so complete team leverages them**)… the skills are the ones which I update at least twice a week."* — [chandureddyvari](https://news.ycombinator.com/item?id=49594125) `✓`
- *"**We** keep the skills in a repo, where an agentic workflow runs biweekly to check if their content drifted compared to the docs and opens PRs"* — [theletterf](https://news.ycombinator.com/item?id=49594183) `✓`
- A **public skill registry with profile-based syncing, for the Norwegian Government** — [starefossen](https://news.ycombinator.com/item?id=49594132) `✓`
- *"you need to treat your skills repo very carefully as **mistakes in there can easily spread to all of the new code you write** using a coding agent"* — [floriangoebel](https://news.ycombinator.com/item?id=49604214) `✓`

And separately, `CLAUDE.md team` over HN comments returned 44 hits, of which **6 concerned more than
one person and 38 were solo setups** — a ratio worth recording, because it is the first time this
repository has measured how often the material is shared rather than asserting either way.

**What moved.** P2's existence, its scale and its stated difficulty are now `✓` from **six
independent voices plus three issue threads**, not from one author's sentence. **`mstr32`'s line is
this product's thesis written by somebody else**: git is required and not enough.

**What did not.** **Nobody in the thread is a receiver describing receiving.** Every voice above is
the *sender*. The first hour on the other end remains `[?]`, and the guide still has no receiver
question block.

---

#### Q-C — What does a real agent-material repository actually contain?

**The critique's D-3: our "20 to 40 items" blended one organisation's threshold with one person's
recollection.**

##### Answer: counted, and the band is wider than we wrote.

**The population first.** `dotfiles claude agents` in name or description returns **93
repositories** (I5) — against **19,703** for published skill collections. Personal agent-material
repositories that are public are a small population, and this is the first time it has been sized.

**Then four of them, counted through the tree API** (I6) — not asked, counted:

| Repository | skills | agents | commands | **items** | files | **distinct tools configured** |
|---|---|---|---|---|---|---|
| [`goulvenclech/dotclaude`](https://github.com/goulvenclech/dotclaude) | 0 | 3 | 8 | **11** | 26 | 1 |
| [`utkuatasoy/dotfiles`](https://github.com/utkuatasoy/dotfiles) | 6 | 1 | 18 | **25** | — | 1 |
| [`sanketsudake/dotfiles`](https://github.com/sanketsudake/dotfiles) | 39 | 6 | 2 | **47** | 200+ | **4** — Claude, Devin, Copilot, Pi |
| [`jckeen/dotfiles`](https://github.com/jckeen/dotfiles) | 28 | 20 | — | **48** | ~280 | **3** — Claude, Codex, Antigravity |

Corroborating counts published in repository descriptions, unverified by tree:
`peopleforrester/claude-dotfiles` — *"70 skills, 15 agents, 21 rules, 14 hooks"*;
`flopperj/dotfiles-core` — *"30+ workflow skills, 5 reasoning agents"*. And a self-report from the
thread: *"I've got **9 skills** so far (many people have **100s** installed from marketplaces and
plugins)"* — [chandureddyvari](https://news.ycombinator.com/item?id=49594125) `✓` as an utterance.

**What moved — NK-2.** The counted band is **11 to 48 items**, with **two of four above 40**. Our
own documents say *"every library size on record is 20 to 40"*; that was written from one filer's
sentence and one recollection, and it is **too narrow at the top**. **Stage 5's 300 stays refuted** —
nothing observed comes close — and `CLAUDE.md` §11's *~30* sits inside the counted band rather than
at its centre. **The right statement is now: tens, not hundreds, and design for fifty rather than
for thirty.**

**What moved — NK-5, and this is the bigger one.** Two of four repositories configure **three and
four distinct agent tools**, counted from their trees: `.claude/settings.json` beside
`packages/devin/config.json`, `packages/copilot/settings.json` and `packages/pi/agent/settings.json`;
and `claude/` beside `codex/config.toml.example` and `antigravity/mcp_config.json.example`, with
`CLAUDE.md`, `AGENTS.md` and `MULTI-AGENT.md` side by side. **Until today "two to four targets" was
seven people's self-description. It is now a count in a public tree.**

**And where the material lives is confirmed the same way** — `chezmoi`, a `.agents/skills/` directory
plus a symlink, *"two source-of-truth git repos (private and public)… syncs to all coding agents
`~/.claude/skills/`, `~/.codex/skills`, `~/.pi/agent/skills`"*
([yatsyk](https://news.ycombinator.com/item?id=49594490)), *"a separate repo which has to be pulled
locally and the skills and agents are sym linked to projects"*
([lazy_afternoons](https://news.ycombinator.com/item?id=49594140)).

**The instrument's bias, printed here.** I5 and I6 can only see **public** repositories. The one
practitioner interviewed keeps his **private**. So this sample is drawn from people willing to
publish their setup, and the counts may run high or low for that reason in ways nothing here can
correct.

---

#### Q-D — Does anything already keep secrets out of a handed-over artefact?

**Raised by the critique's D-9:** our matrix wrote *"No, in this space"* for RJ-4's competitor cell,
while `2-flows/07-env-and-secrets/NOTES.md` records that **Doppler and Infisical were captured and
deliberately not scored**.

##### Answer: the runtime half is occupied. The handover half is not. Our cell was too strong.

What exists, from a 14-hit search plus the thread:

- **The phantom-token pattern** — a credential-injection proxy outside the sandbox, so the agent never sees a real credential. *"we give agents our API keys as environment variables, and a single prompt injection can exfiltrate them via `env`, `/proc/PID/environ`, or just an outbound HTTP call"* — [decodebytes](https://news.ycombinator.com/item?id=47237328) `✓`
- **A vault with time-scoped access**, skills retrieving credentials at call time — [sathish316](https://news.ycombinator.com/item?id=46908256) `✓`
- **A broker that injects keys into the shell** so agents *"can script and develop without having any keys"* — [stcredzero](https://news.ycombinator.com/item?id=47005411) `✓`
- **A WASM sandbox with a secret scanner** for API-key patterns, plus prompt-injection detection — [senza1dio](https://news.ycombinator.com/item?id=46889258) `✓` as an utterance; **the story it sits on is `[dead]` and its *"1.5M API keys leaked"* is unverified and should not be quoted forward**
- **Policy enforcement** — *"YAML policies for enforcement (e.g., **block secrets**, require >80% coverage)"* — [zen4ttitude](https://news.ycombinator.com/item?id=46877492) `✓`

**Every one of those keeps a key away from a *running* agent.** None of them is about what a set
**carries when it leaves**. And the failure they do not address is described by a person:

> *"a skills file can just easily say '**We connect to bob using key Z and user X**.'"*
> — [imadtaieber](https://news.ycombinator.com/item?id=49590065) `✓`

**What this changes.** The matrix cell for RJ-4 reads *"No, in this space"* and should read: **the
runtime problem is being worked on by several parties; the handover problem — what the artefact
contains when somebody else opens it — is still unoccupied.** The job stays in the MVP core; the
claim under it narrows. And the flow-07 note's decision not to score Doppler and Infisical was
reasonable then and is now a gap in the benchmark rather than an oversight in the matrix.

---

#### Q-E — Does the empty-handed consumer exist?

**Raised by the critique's D-4:** `CLAUDE.md` §8 and §11 ship two surfaces and a content commitment
for **P3, a persona nobody has ever observed.**

##### Answer: people in this shape were finally observed — and the first evidence is against the premise.

**The supply is vast and confirmed.** `"claude skills"` in repository name or description returns
**19,703 repositories** (I5); the top of that list is curated collections at five-figure star counts
— `ComposioHQ/awesome-claude-skills` **74,686★**, `alirezarezvani/claude-skills` **25,709★** and
*"380 Claude Code skills"*, `travisvn/awesome-claude-skills` **15,006★**.

**The demand, from the first practitioners ever observed on this question, is sceptical:**

> *"**I'm not sure I've ever used any of them**, and when I've looked at them it's been some
> **YouTuber trying to make money**."* — [SyneRyder](https://news.ycombinator.com/item?id=49591526) `✓`

> *"**I do not understand the appeal of skill shopping.** The one exception I have is things like the
> Axiom Apple development skills."* — [resonious](https://news.ycombinator.com/item?id=49595691) `✓`

- *"I try to keep my collection of community skills **short**, usually **a few established names** (mattpocock, mcollina, trailsofbit)."* — [osr00](https://news.ycombinator.com/item?id=49591803) `✓`
- Prefers **creating skills from session learnings** rather than downloading published ones — [sinuhe69](https://news.ycombinator.com/item?id=49595603) `✓`
- The one positive: *"Last week I had to reuse homemade skills on different project… ship as a plugin and **add your git repo as a marketplace**"* — [jve](https://news.ycombinator.com/item?id=49595170) `✓` — **and note it is his own material, distributed through a marketplace mechanism. That is P1's job, not P3's.**

The only volume figure comes second-hand: *"many people have **100s** installed from marketplaces and
plugins"* — [chandureddyvari](https://news.ycombinator.com/item?id=49594125), **describing other
people, not himself.**

**What this changes, and it is the most consequential thing in this round.** P3 was `[?]` — a persona
with no evidence in either direction. **It is no longer `[?]`. It has evidence, and the evidence
runs against it**: four of five observed opinions about installing strangers' material are refusal,
minimisation, or a preference for one's own. The one person who spoke well of the mechanism was
using it **to distribute his own work**.

**What this does not license.** Four sceptics on Hacker News are not a market. **HN is exactly the
population most likely to distrust a marketplace**, the thread self-selects for people who already
manage their own skills, and nobody asked a beginner anything. **This does not say cold start is
solved or that the shelf is wrong.** It says the shelf's premise — *the product has material from the
first second and that is what makes it usable* — now has its first contact with real opinion, and the
opinion is that **curated volume is not what these people want.** `osr00`'s *"a few established
names"* is the shape that survived: **provenance over volume.**

---

#### What this round hands forward

1. **To [`personas.md`](personas.md).** Five marks change and one persona changes character. Applied in this round and recorded in [`research.md`](../research.md) §7.
2. **To the register.** No new question. Q-A sharpens **NK-13** without moving it; Q-E bears directly on **Q9** — *which specified features close no evidenced job* — and gives that entry its first evidence.
3. **To the matrix in [`jtbd.md`](../7-jobs-to-be-done/jtbd.md).** RJ-4's competitor cell is too strong (Q-D) and H-J4's P3 column is no longer honestly `[?]` (Q-E). **Not applied here** — the matrix is stage 7's and it has its own audit still owed.
4. **To the benchmark.** Doppler and Infisical are captured and unscored; on the evidence of Q-D that is now a gap worth one afternoon.
5. ~~**The half-day that keeps not being spent.**~~ **Spent 2026-09-10** — [`re-research.md` round 3](re-research.md#round-3-five-questions-that-need-no-interview) Q-F; this line is left as written because this document is a dated record. NK-13 / Q-A. Every round of research makes it more load-bearing and none of them can touch it. **Round 3 finally points an instrument at it** — [`re-research.md` round 3](re-research.md#round-3-five-questions-that-need-no-interview) **Q-F**, written 2026-09-09 when the interviews became unavailable and the only questions left were the ones that need no person.


---

# Round 3. Five questions that need no interview

> **Collected 2026-09-10.** The interviews became unavailable. Three questions read behaviour left in public artefacts; **two are experiments we ran ourselves.**
>
> *Merged into this file on 2026-09-10 from the file that was `re-research-3.md`, unchanged.*

### Re-research, round 3 — five questions that need no interview

> **Planned 2026-09-09. Run 2026-09-10.** Every question below now carries an **Answer** section and
> the capture log exists: [`_captures/round3-log.json`](_captures/round3-log.json), plus
> [`_captures/qf-handover-test/`](_captures/qf-handover-test/) for the one experiment that produced an artefact.
> **The plan text is left exactly as written** so that what was predicted can be read against what
> was found — and in two places the finding is not what the plan expected.
>
> **Four of the five are answered. Q-I is answered in part.** The one thing to read first, if only
> one thing is read: **Q-F**. The spec's largest bet survives, and the reason it survives is not the
> reason §6 gives.
>
> **One headline was withdrawn by its own control after being written** — Q-G's 89.4% — and the
> sequence is left visible rather than tidied away.

**A plan, not a result. Written 2026-09-09.** Nothing here has been collected yet, and **nothing in
this file may be cited as evidence** until each question carries its capture log beside it, the way
[`re-research.md`](re-research.md) and [`re-research.md` round 2](re-research.md#round-2-counting-not-asking) do.

**Why it exists.** Every blocked cell in the matrix and five of the six live register entries were
pointed at the same instrument — **five practitioner conversations** — and that instrument is
**unavailable**. Rather than leave the blocked cells pointed at something that will not happen, this
round asks what can be established **without asking anybody anything**, and says plainly what cannot.

**The change of instrument class, and it is the whole point of this round.** Rounds 1 and 2 read what
people **wrote** — issues, comments, READMEs — and rule 5 governs all of it: *a re-runnable query
proves that something was said, not that it is true.* Round 2 broke that ceiling once, with the
`git/trees` count that measured somebody's collection instead of asking about it. **All five
questions below are of that kind or stronger.** Three read **behaviour left in public artefacts** —
what a person did to a repository, not what they said about it. Two are **things we run ourselves**,
where the observation is ours and the `✓` covers the behaviour rather than the utterance. That is the
first time this repository would measure its own claims instead of the ecosystem's opinion of them.

---

#### The instruments, and what each can and cannot see

| # | Instrument | What it observes | Blind to |
|---|---|---|---|
| **I7** | **The handover test — we run it.** A composed archive handed to a fresh Claude Code, Cursor and Codex in clean containers | **What a receiving agent actually does with `SETUP.md`**, step by step, on our own machine | What a **human** recipient does; other models and versions; whether an agent would ever reach for this unprompted |
| **I8** | **GitHub forks API + first-commit diffs.** Forks of public agent-material repositories | **What a receiver changes in inherited material, and in what order** — the receiving end, observed instead of asked | Why they changed it; private handovers; forks are a public, self-selecting, mostly-developer act, and a fork with no commits is ambiguous |
| **I9** | **Git history over duplicated files.** The same item held in several paths or several repositories | **Whether copies drift, how far and for how long** — RJ-3's premise as a measurement | Whether the drift cost anybody anything; private repositories; a copy deliberately kept different is indistinguishable from a copy forgotten |
| **I10** | **Registry download series + vendored-file activity.** npm/PyPI counts for the installer category; repositories that copied a known public skill in | **Whether consuming other people's material is recurring behaviour or a one-off**, and whether what was imported is ever touched again | Private use; who the person was; a download is not a use, and an untouched file is not necessarily a dead one |
| **I11** | **Run the competitors.** Install the tools whose READMEs claim duplicate audit, drift detection and trust scores, and point them at a deliberately broken set | **What the market actually detects** — the claim under `CLAUDE.md` §2 turned from vendor self-description into a measurement | Funded closed products (Tessl, Smithery) beyond their public surface; roadmaps; anything they do for paying customers |

**Two of these five need nothing but this machine (I7, I11), and they are the two that touch the
specification's core.** They have been named as *an afternoon* and *a half-day* in three documents
since 2026-09-07 and have never been run.

---

#### Q-F — Does a receiving agent perform the setup from `SETUP.md` alone? · **I7**

**The highest-value question in the project, and the only one on this list that is entirely ours.**

**What is blocked.** **NK-13**, the audit's **D-1**, and with them `CLAUDE.md` §6's decision that
`SETUP.md` is written for the agent rather than for a human reader, §8's handover stages as the last
stages of Run, and the Q2 disposition that made the document a real artefact. **Every other row in
the audit's dangerous list is downstream of this one.** Round 2 sharpened it and could not close it:
in 274 comments on exactly this topic the work is done by `chezmoi`, symlinks, CLI installers,
`skills.py` and bootstrap scripts, and **two comments describe an agent touching this material at all
— neither is a setup** ([`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-A).

**The procedure.**

1. **Compose a set by hand**, eight to ten real items from the public-shelf candidates, deliberately
   containing: at least one `requires` edge, **one duplicate command name**, **one pair writing to
   the same target path**, **one missing env key**, and **one external item pinned at a `ref`**.
2. **Build the archive exactly as §6 describes** — inline items placed by `targetPath`, external
   items as instructions at their pinned `ref`, all MCP servers merged into one config, `.env.example`
   from the collected `needsEnv`, and **`SETUP.md` stating per item what that item requires**.
3. **Hand it to three fresh agents in clean containers** — Claude Code, Cursor, Codex — each with no
   prior context and one instruction: *read `SETUP.md` and set this project up.*
4. **Record, per agent:** what it did and in what order; what it skipped silently; what it invented;
   what it asked; whether it noticed the duplicate command and the path collision; what it did about
   the missing key; and **whether the result runs**.

**What would count as an answer.** Three transcripts and a verdict per agent: *performed · performed
with gaps · did not attempt*. **Any outcome is worth having.** If they perform it, the spec's largest
bet is evidenced for the first time. If they do not, §6 changes shape before a single mockup is drawn
— and the *emit a verify script* option §6 already keeps additive stops being hypothetical.

**What it can never establish.** That a human recipient behaves this way; that any other model or
version behaves this way; that anybody would reach for such an archive unprompted. **It is a claim
about three machines on one day, and it must be dated and versioned in the write-up.**

**Cost.** Half a day. **Mark it would earn: `✓` — and it is the one `✓` in this repository that would
cover a behaviour rather than an utterance**, because we watched the behaviour happen.

##### Answer — run 2026-09-10. The setup gets performed. The *checking* does not, and that is the finding.

**Capture:** [`_captures/qf-handover-test/`](_captures/qf-handover-test/) — the ground truth of the composed set, the
`SETUP.md` the agents read, the two scripts that build the archive, and a transcript per run.

**What was built.** Ten real items from five checked sources, every one pinned at a commit
(`anthropics/skills` @ `41bbe19`, `ChrisWiles/claude-code-showcase` @ `a95518f`,
`iannuttall/claude-agents` @ `f7df2c3`, `alirezarezvani/claude-skills` @ `19392f7`,
`shotgun-sh/shotgun` @ `4d344d5`), plus `microsoft/playwright-mcp` @ `8a13ef8` as an external item
that is instructions and never files. Five defects planted: a duplicate command name, two
target-path collisions, an MCP key collision at two different refs, a missing env key. `SETUP.md`
names **none** of them, because §8 puts finding-disclosure on the sender's side and telling the
receiver would have destroyed the measurement.

**What was not available.** Cursor and Codex CLIs are not installed on this machine and were not
installed for this. *Three fresh agents in clean containers* became **three model tiers of one
vendor's agent in three fresh directories**, on a machine that had git, node, Python and an
authenticated `gh` CLI already on it. That is a weaker instrument than the plan asked for, and
everything below is bounded by it.

###### The mechanical half of the bet holds, three times out of three

Every one of the three cloned the external repository **at the exact pinned ref**, installed the
dependency the document named, created `.env` from `.env.example`, and reported at the end. No agent
refused, none asked to be told what to do, and none needed a human in the loop to get that far.
**`SETUP.md` written for a machine is read by a machine and acted on.** That is the first evidence
of any kind under `CLAUDE.md` §6's central decision, and it is positive.

###### The diagnostic half does not hold, and it splits by tier

| | run 1 · default tier | run 2 · sonnet | run 3 · haiku |
|---|---|---|---|
| clone at the pinned ref | yes | yes | yes |
| dependency installed, `.env` created | yes | yes | yes |
| **duplicate command `/review`** | **found** — fetched both upstreams, reported them as two unrelated commands | **found, then wrongly closed**: *"byte-identical, so there's no real conflict"* | **not seen** |
| **`.claude/settings.json` collision** | **found**, both losers preserved in a directory the agent does not scan | **found**, merged the two by hand | **not seen** |
| **MCP key collision on `memory`** | **found** | noticed the config *"already resolves"* it | **not seen** |
| **missing `GITHUB_TOKEN`** | left empty, and said why | **wrote the machine's live OAuth token into `.env`** | left empty, asked the human |
| third-party plugin marketplace enabled by the surviving settings | **flagged as a security decision** | not mentioned | described as *"example marketplace"* |
| two MCP packages that do not exist on npm | **found** | not found | not found |
| `pdf` skill missing the files it tells the agent to read | **found** | not found | not found |
| hook pointing at a script in no item | **found** | **found** | not found |
| verdict | **performed** | **performed with gaps** | **performed with gaps** |
| turns · time · cost | 20 · 321 s · $1.34 | 28 · 249 s · $0.45 | 14 · 79 s · $0.06 |

**Run 2's claim was checked and it is false.** The two `review.md` files are 1,125 and 850 bytes,
different sha1, different first lines, one a lint/CI gate and one a Python PR review. A receiver
**detected a Problem, produced a confident reason it was not one, and closed it.** That is the
Continue failure this repository already keeps as its sharpest post-mortem — *computed the duplicate
correctly and discarded the loser in silence* — reproduced on our own artefact by a current model.

**Run 2 also copied a live `gho_` credential out of the machine's keyring into a plaintext file**,
unprompted, having been told only to set the project up. It added a `.gitignore`. It is the first
observation ever made on the receiving side of **RJ-4**, *move the work without moving the secrets*,
and it runs the other way: the danger is not only what the sender packs, it is **what the receiver
fetches to fill the gap the sender left.** The token was redacted from every artefact in this folder
as soon as it was found.

**Run 3 performed the setup and saw nothing.** Its report reads *"✅ All skills are in place"*,
*"Commands: `/review`"* — singular — and *"settings.json configured with example marketplace"*. A
receiver that does the work and validates nothing is worse than one that refuses, because it
returns a green report.

###### What the test discovered that nobody planted

- **Two of the MCP servers in a real 6,062★ repository's real `.mcp.json` do not exist on npm.**
  `@anthropic/mcp-github` and `@anthropic/mcp-memory` both 404. The archive was correct, the pinned
  material was correct, and the set still cannot run.
- **An item is a directory, and §5 models it as a file.** The `pdf` skill's `SKILL.md` instructs the
  agent to read `REFERENCE.md`, `FORMS.md` and eight scripts. `Item.content` has room for one blob,
  `targetPath` for one destination, and the export placed one file. **The archive was silently
  incomplete and `SETUP.md` said the item required nothing.**
- **An archive can reconfigure the receiving agent before setup begins.** The `settings.json` that
  won the collision declares a third-party plugin marketplace and enables a plugin from it. Nothing
  in §6 treats a settings file as executable, and it is.
- **A surviving item can reference a file that belongs to the item that lost.** The hooks in the
  losing `settings.json` call `.claude/hooks/skill-eval.sh` — never an item, therefore never
  exported, therefore a failure on every prompt.

###### What this establishes, and what it does not

**Establishes `✓`, and the mark covers behaviour:** a coding agent reads a `SETUP.md` of this shape
and performs the setup it describes, including cloning at a pinned ref. **Three of three.**

**Establishes `✓` in the other direction:** leaving the Problems to the receiver does not work. Of
three receivers, one found them, one mis-resolved one and missed three, one saw none.

**Does not establish:** that a human recipient behaves this way; that Cursor or Codex behave this
way — neither was run; that any of this holds on another day, another version, or a machine without
network. **It is three tiers of one agent on one machine on 2026-09-10, and it must be re-run before
it is leaned on twice.**

**To the register, not to the spec.** Three proposals, all for the sitting: `SETUP.md` should carry
the set's Problems and not only its requirements, because the disclosure §8 gives the sender is the
disclosure the receiver turns out to need; `Item` needs to address a **directory**, not a file; and
a settings file is an executable item, which §6 does not currently allow for. **NK-13 and the
audit's D-1 are closed by this run.**

---

#### Q-G — What does a receiver actually do with inherited material? · **I8**

**The only way to see the receiving end without a receiver in the room.**

**What is blocked.** **The entire P2 column of the matrix** — MAIN/P2, RJ-1/P2, RJ-2/P2, RJ-3/P2,
RJ-4/P2, SJ-1/P2, H-J7/P2 — plus **NK-7's receiving half** and the audit's **D-2**, which is the
second most dangerous claim in the folder. Round 2 confirmed the population from **six independent
voices and every one of them is a sender** ([`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-B). Nobody has
ever described receiving, and the interview guide has no questions for one.

**The insight this rests on.** A fork **is** a handover, and its first commits are the first hour,
written down and public. We cannot ask a receiver what confused them; we can read what they changed
before they could do anything else.

**The procedure.**

1. Take the population round 2 sized — the **93** public personal agent-material repositories, plus
   the `dotfiles claude agents` set and the larger curated collections — and list their **forks** via
   the API.
2. For each fork, find the fork point and read **the first three commits after it**.
3. Classify every change: **paths** (`~/.claude` → something else, absolute → relative), **agent
   target** (a `CLAUDE.md` becoming an `AGENTS.md`, a new tool directory), **MCP configuration**
   (servers removed, commands rewritten, node versions pinned), **secrets** (a key removed, an
   `.env.example` filled in), **deletions** (items thrown away unread), **nothing at all**.
4. Count the fourth case separately and honestly: **a fork with no commits is a handover that went
   nowhere**, and it is as much a finding as any edit.
5. Measure **time from fork to first commit**, which is the closest public proxy to *the first hour*.

**What would count as an answer.** A distribution over those categories with n stated. Three outcomes
change different things. If receivers mostly **rewrite paths and configuration**, RJ-1 gets a real
number and the handover stages are aimed correctly. If they mostly **switch the agent target**, §6's
target selector is doing more work than the audit currently lets us claim. If they mostly **delete
things or never commit**, the archive is not being received at all and the whole P2 story needs
rewriting before it is designed for.

**What it can never establish.** Motive; whether anything confused them; what happens in the private
handover the one interview described — a repository handed to a contractor never appears as a fork.
**And publication bias runs the same way as in round 2**: this sees people who fork in public.

**Cost.** A day, mostly scripted. **Mark: `✓` for what was changed** — a diff is a behaviour, not a
self-report — **and `[?]` for every word about why.**

##### Answer — a striking number, and a control that takes it away again

**Instrument as run.** Sixteen repository-search queries built a population of **653 parent
repositories** holding one person's agent material and carrying between 1 and 99 forks. Repositories
above 99 forks were excluded on purpose: at that size the thing being forked is a template, and
forking a template is not receiving a handover. Every fork of every one of those parents was read
through the compare API across the fork point — **2,130 fork records, 103 of them unresolvable
(deleted, empty or gone private), 2,027 resolved.** Counts and queries in
[`_captures/round3-log.json`](_captures/round3-log.json).

###### The headline

> **1,813 of 2,027 forks — 89.4% — have not a single commit after the fork point.**

**214 forks, 10.6%, committed anything at all.** The plan said to count that case separately and
honestly, and it is now the largest number in the study.

**Of the 214 who did commit, when they did it:** median **25 minutes** after the fork,
**55% within the first hour**, 70% within a day (n = 159; 55 records excluded because their commits
predate the fork record and the timing cannot be trusted). **The first hour is real.** Whatever a
receiver does, they do it immediately or never.

###### What the 214 changed

Classified from the patch bodies, not from filenames. The first pass counted any diff line
*mentioning* a home directory as a path rewrite and produced 69%; that is what a dotfiles diff looks
like on every other line, and it was thrown away. The strict rule below only counts a **matched
pair** — a removed line and an added line that become the same string once the owner or user segment
is normalised away.

| What they did | of 214 committers |
|---|---|
| nothing that fits a category — ordinary continued development of the material | **125 · 58%** |
| deleted files that came with the fork | 53 · 25% |
| touched a second agent target (`AGENTS.md`, `.codex/`, `.cursor/`, `.gemini/`) | 33 · 15% |
| **literally substituted themselves for the author** | **25 · 12%** |
| changed MCP configuration | 13 · 6% |
| removed or rotated a key, or filled in an env example | 10 · 5% |
| a live-looking secret visible in the diff | 1 |
| commits are merges or upstream syncs — a **contributor**, not a receiver | 31 · 14% |

**The 25 self-substitutions are the cleanest thing in the round**, because each is a matched pair
that can be read:

- `curl -fsSL .../archibate/dotfiles-claude/main/setup.sh` → their own repository. **The setup script
  the author shipped would have installed the author's material onto the receiver's machine.**
- `STRAP_GITHUB_USER="br3ndonland"` → theirs. `user = br3ndonland` in a git config → theirs. Four
  different people did this to the same repository.
- `/Users/bbrowning/…/skills/pr-review/reference/jwt-security.md` → `/Users/emilien/…`. An absolute
  home path inside a skill.
- `Use the pattern: users/Max191/<short-description>` → their own handle. A **branch-naming
  convention addressed to the agent** that names the author.
- `A repo is user-owned if travisjneuman is the GitHub owner` → their own handle. **An instruction to
  the agent whose subject is the author's identity.**

That last class is the one no mechanism in `CLAUDE.md` reaches. `needsEnv` covers a key; nothing
covers *the author's name baked into a rule the agent obeys*.

###### What this does to the P2 column

The plan named three outcomes and said which each would change. **On the raw numbers the third looked
like it had fired** — *if they mostly delete things or never commit, the archive is not being received
at all and the whole P2 story needs rewriting before it is designed for.* **It had not.** The control
below shows why, and it is the reason this section reads as it does rather than as that sentence.

###### The control — run afterwards, and it takes the headline away

The paragraph above was written before the control existed, and it flagged the hole: *most forks of
most repositories on GitHub are dormant, and without the same number for comparable non-agent
repositories, 89.4% may be a fact about GitHub rather than about agent material.* **So the control
was run, with the same instrument, the same fork range and the same cap.**

| Population | resolved forks | no commit after the fork point |
|---|---|---|
| **Agent material** (this study) | 2,027 | **89.4%** |
| **Plain dotfiles**, agent words excluded | 1,118 | **84.8%** |
| **Ordinary small libraries**, 20–400★, pushed this year | 1,579 | **87.0%** |

**The gap is 2.4 to 4.6 points, and it points the wrong way for the interpretation.** Forks of agent
material are, if anything, **slightly more** dormant than forks of anything else. The differences are
larger than sampling noise — z = 2.2 and z = 3.8 — and they are far too small to carry the sentence
they were about to be used for.

> **The 89.4% is a fact about forks, not a fact about handover.** It stands as a count and it is
> withdrawn as evidence that *the archive is not being received*. The plan's third outcome did **not**
> fire; nothing here says the P2 story needs rewriting, and nothing here says it does not.

**This is the round's own instrument catching the round.** The number was arresting, it was about to
be the headline of a whole question, and the control cost twenty minutes. It is recorded in the
capture log with the two control queries so that anybody can re-run all three.

###### What survives the control

- **Timing.** Of the 214 who committed, **55% did so within the first hour** and 70% within a day,
  median 25 minutes. The control does not touch this: it is a statement about the people who *did*
  act, not about how many did.
- **The 25 self-substitutions**, which are matched pairs and can be read one by one. They are the
  thing no baseline explains away, because they are not *whether* somebody acted but *what the act
  was*: replacing the author with themselves in setup URLs, git identity, absolute paths, branch
  conventions and **instructions addressed to the agent that name the author's handle**.
- **The one handover this repository has ever heard described was private** — a repository handed to
  a contractor, [interview Q21](interviews.md#part-2-interview-1-of-5) — and it would appear in this instrument as
  nothing at all. That was true before the control and is still true.

**What it establishes `✓`:** when somebody takes another person's agent material and acts on it, they
act **within the hour**, and the commonest concrete edit is **replacing the author with themselves**.
**RJ-1 now has a behaviour under it**, which the audit had left it without. It is a modest one — 25
cases out of 2,027 forks — and it is not a self-report.

**What it does not establish:** anything about how often handover happens, in either direction.

---

#### Q-H — Do copies actually drift, and for how long? · **I9**

**What is blocked.** **RJ-3**, which the audit lowered from 3 to 2, and with it `CLAUDE.md` §5's
live link — *the single mechanism in the spec that exists for exactly this job*. Its evidence today
is one filed request at 48 reactions and **one person's story**, and the same person still moves
material with `cp -r`, which is the audit's **D-7**.

**The procedure.**

1. Find repositories that hold **the same item in more than one place** — the shape round 2 already
   saw in the trees: `claude/` beside `codex/`, `.claude/skills/` beside `packages/*/`, or one skill
   copied into several project directories.
2. Hash file contents across those paths **over history**, commit by commit.
3. Measure, per duplicated item: **how often an edit lands in one copy and not the others**; **how
   long the divergence lasts** before it is reconciled, if it ever is; and **how many copies exist by
   the end**.
4. Separate **deliberate divergence** — a copy that was changed once and never re-synced, plausibly on
   purpose — from **drift**, where the same edit later appears in the other copy, which is the visible
   signature of somebody noticing late.

**What would count as an answer.** A count of items whose copies diverged, with the duration of each
divergence. **The second edit arriving weeks later in the other copy is the measurement we want**: it
is the public, dated version of *found six weeks later by a client*.

**What it can never establish.** That the drift cost anybody anything, which is the part only a person
can say. And it cannot see the private repositories where this material mostly lives.

**Cost.** A day. **Mark: `✓` for divergence and its duration; `[?]` for harm.**

##### Answer — copies diverge, they stay diverged for months, and almost nobody ever reconciles

**Instrument as run, and it turned out cheaper than the plan assumed.** Git's object SHA is
content-addressed, so two copies of a file with the same blob SHA are byte-identical and two with
different SHAs have diverged. **The current state of every duplicate in a published tree is one API
call per repository and no cloning at all.** A duplicate is defined as the same path suffix under two
or more distinct agent roots — `.claude/skills/foo/SKILL.md` beside `.codex/skills/foo/SKILL.md` is
one item in two places. Generic basenames were excluded, because two unrelated `README.md`s are not
one item; a first pass that did not exclude them was thrown away.

**500 trees scanned. 38 repositories (8%) hold at least one duplicated item. 7,506 duplicated items.
1,024 of them — 14% — are out of sync right now.**

The concentration matters more than the average:

| Repository | ★ | duplicated items | out of sync | roots it keeps |
|---|---|---|---|---|
| [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) | 25,773 | 257 | **185 · 72%** | `.codex`, `.gemini`, `.hermes`, `.vibe` |
| [`agent-sh/agnix`](https://github.com/agent-sh/agnix) | 407 | 467 | **385 · 82%** | `skills`, `plugin/skills`, per-agent fixtures |
| [`Infrasity-Labs/dev-gtm-claude-skills`](https://github.com/Infrasity-Labs/dev-gtm-claude-skills) | 123 | 37 | **32 · 86%** | `agents`, plugin dirs |
| [`secondsky/claude-skills`](https://github.com/secondsky/claude-skills) | 217 | 17 | **17 · 100%** | per-plugin `agents`, `commands`, `skills` |
| [`atsushi-green/ds-ai-coding-skills`](https://github.com/atsushi-green/ds-ai-coding-skills) | 77 | 10 | **10 · 100%** | `.claude`, `.github` |
| [`huangserva/skill-prompt-generator`](https://github.com/huangserva/skill-prompt-generator) | 1,481 | 32 | **0 · 0%** | `.claude`, `.codex` |

**A 25,773-star repository whose whole proposition is one skill set for every agent has 72% of its
per-target copies out of sync with each other.** The one repository at 0% is the smallest and holds
two targets.

###### Duration, from history

Seven repositories were cloned and every duplicated item walked commit by commit — up to 200
duplicated items per repository, which is where the cap binds for the three largest.

> **383 divergences are open at HEAD. Median time open: 121 days. Longest: 218 days.**
>
> **Four divergences in the entire sample ever closed. All four closed within seven hours.**

**The plan predicted the wrong signature and that is worth recording.** It expected *the second edit
arriving weeks later in the other copy* — the public, dated version of *found six weeks later by a
client*. **That pattern occurs four times and never takes longer than an afternoon.** What actually
happens is that copies diverge and **stay** diverged, for a median of four months, with no
reconciliation ever observed.

###### What this establishes, and what it does not

**`✓` — divergence between copies of one item is real, common in the repositories that hold copies at
all, and measured in months.** RJ-3's premise is no longer only one filed request at 48 reactions
and one person's story.

**`[?]` — everything about harm and about intent, exactly as the plan said.** And the finding makes
intent *harder* to separate, not easier: since reconciliation is essentially never observed, there is
no behavioural signature distinguishing *drift nobody noticed* from *a copy somebody meant to keep
different*. A four-month-old divergence between `.claude/` and `.gemini/` copies of the same skill is
more plausibly the first than the second, and plausibility is not evidence.

**One thing it does bear on directly.** §5's live link exists so that a fix reaches every copy. The
measurement says the copies exist, they drift, and the drift persists. It says nothing about whether
anybody wants our mechanism — but the mechanism is now aimed at something that demonstrably happens.

---

#### Q-I — Does other people's material get kept, or only starred? · **I10**

**What is blocked.** **H-J4 and the whole P3 column**, **Q9** in the register, and `CLAUDE.md` §8's
scope switch and §11's shelf with its build commitment. Round 2 established the supply — **19,703
repositories, 74,686★ at the top, against 93 personal ones** — and reached five practitioners whose
opinion of installing others' material was four-to-one negative
([`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-E). **Opinion is not behaviour, and stars are not use.**

**The procedure.**

1. **Registry series.** For the installer category — the tools at 425–4,526★ in R8, plus
   `vercel-labs/skills` — pull **download counts over time** from npm or PyPI. A tool with five
   thousand stars and forty weekly downloads is a bookmark; one with a rising series is a habit.
2. **Vendored-file trace.** Pick five well-known public skills with distinctive frontmatter or names.
   Search GitHub code for that text **outside the source repository**. For every hit, record: the date
   it was added, whether the file was **ever modified afterwards**, and whether the repository is
   still active.
3. **Provenance retention.** In the same hits, count how many keep any statement of where the item
   came from — a `repoUrl`, a source line, an attribution. **This is a direct measurement of §5's
   claim that provenance matters and §11's that it must be shown.**

**What would count as an answer.** Two numbers with a shape: **what fraction of imports are ever
touched again**, and **whether the installer category's usage is growing or flat**. If imports are
touched, the shelf is serving a live behaviour and *provenance over volume* tells us how to sort it.
If imports are added once and never touched, the shelf is a bookmark bar — which does not remove it
from the MVP, and does change what it must be.

**What it can never establish.** Who the importer was, and in particular whether they were
**empty-handed** — the persona itself stays `[?]` until somebody in that shape is observed. **This
question is about the behaviour the shelf assumes, not about the person it was drawn for.**

**Cost.** Half a day. **Mark: `✓` for counts and dates; `[?]` for the persona.**

##### Answer — a third of imports get edited, two thirds never do, and the installer category is not flat

###### The registry series, with two identity corrections first

`npx skills` — [`vercel-labs/skills`](https://github.com/vercel-labs/skills), 30,841★ — **8,478,818
downloads last week.** The npm name predates the tool (it was registered in 2016), so the number was
split by version before it was believed: **98.4% of last week's traffic is `1.5.x` and 99.98% is
`1.3.0` or later**, which is the modern tool. Monthly, since the first modern version landed on
2026-01-30:

| 2025-12 | 2026-01 | 2026-02 | 2026-03 | 2026-04 | 2026-05 | 2026-06 | 2026-07 | 2026-08 |
|---|---|---|---|---|---|---|---|---|
| 19 | 240,953 | 988,785 | 2,635,935 | 3,026,631 | 4,760,931 | 38,867,068 | 44,425,540 | 39,859,796 |

**The rest of the category is flat and small**: `agent-skill-manager` 173/week, `ai-agent-skills`
183/week, `opkg` 170/week. And two of R8's tools are not on npm under the names their READMEs give —
`harnesskit` and `tank` both belong to unrelated projects, which is a correction to round 1.

**The caveat is load-bearing and belongs in the same breath as the number.** `npx` re-downloads on
every invocation unless the tool is installed globally, and CI counts. **8.5M/week is closer to
invocations than to people**, and no instrument here converts one into the other. What survives the
caveat is the *shape*: six orders of magnitude in eight months, then a plateau. **Whatever this is,
it is not a bookmark.**

###### The vendored-file trace

Five well-known public skills from `anthropics/skills`, each identified by a distinctive sentence of
its own frontmatter, searched for in every **other** repository on GitHub:

| Skill | repositories carrying the sentence verbatim |
|---|---|
| `skill-creator` | **4,024** |
| `mcp-builder` | **3,200** |
| `pdf` | **2,592** |
| `algorithmic-art` | **2,056** |
| `brand-guidelines` | **2,040** |

**446 unique foreign copies** were then read in full — 100 search results per skill, deduplicated —
and the commit history of each exact path was walked. They were added between **2025-08-14** and
**2026-09-02**.

> **143 of 446 — 32% — were modified after the day they were added.**
> **303 — 68% — have never been touched again.**
>
> Of the 143 that were edited: **median 27 days** between being added and last being touched, p75
> 87 days, longest 318. Only 17% were same-day.

**A median of 27 days is the interesting number.** It is not adaptation-at-install — that would be
same-day, and same-day is 17%. It is somebody coming back to a file weeks after importing it, which
is the signature of **use**.

###### Provenance, and a measurement thrown away

The first pass reported 82% of copies carrying "a statement of origin" and it was wrong: the rule
matched the word `license`, which **every one of these skills already carries in its own
frontmatter** (`license: Complete terms in LICENSE.txt`). That counts the original file surviving,
not the importer crediting anybody. A second rule matching *"based on"* was thrown away for the same
reason — sampled, it was matching ordinary prose inside the skills (*"Color based on cell size"*).

**The one rule that survives is the strict one: does the copied file name `anthropics/skills` or an
anthropics URL anywhere in its body.**

> **45 of 446 — 10%.**

###### What this establishes, and what it does not

**`✓` — consuming other people's agent material is a mass behaviour, not a niche one**, and it is
recurring rather than one-off: a third of imports are edited, at a median of four weeks after
arriving. **`✓` — provenance does not survive the copy.** Nine copies in ten carry no statement of
where they came from.

**Against round 2, and the plan predicted this.** [`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-E reached
five practitioners on installing other people's material and **four refused, minimised or preferred
their own**. This round measured the behaviour instead of the opinion and found thousands of
repositories doing it. **Both stand** (rule 4): a self-selected Hacker News thread says what a
certain kind of practitioner says, and the registry and the trees say what a much larger population
does. **The opinion is not refuted; it is placed.**

**Does not establish** who any of these importers is, and **in particular not that any of them is
P3.** The persona remains `[?]`, exactly as the plan said it would. This question was about the
behaviour the shelf assumes, and the behaviour is there.

**To Q9.** The shelf is not a bookmark bar. What the evidence says about *what it should hold* is
unchanged from round 2 — provenance over volume — and this round adds the sharper form of it:
**provenance is what everybody loses, so showing it is the part that has to be ours.** §5 already
requires `repoUrl` and a pinned `ref` shown rather than stored; this is the first measurement under
that decision, and it supports it.

---

#### Q-J — Does anything on the market actually perform the set-level check? · **I11**

**What is blocked.** **`CLAUDE.md` §2's core-value sentence** — *what nothing does today is tell you
that a skill needs a particular MCP server, that two skills write to the same config file, that two
items register the same command name* — which
[`FINAL.md`](../FINAL.md) §6 already lists as narrower than it reads, **on the strength of what
competing tools claim in their own READMEs, none of which we have run.** Also RJ-2's and EJ-2's
competitor cells, and the benchmark gap Q-D left: **Doppler and Infisical are captured and unscored.**

**The procedure.**

1. **Reuse the deliberately broken set from Q-F** — same duplicate command, same path collision, same
   missing key, same unpinned external item. One artefact, two experiments.
2. **Install and run** each tool that claims any part of our check: the per-agent sync tools, the
   skill managers claiming duplicate and near-duplicate audit, the one claiming trigger collision,
   the one claiming 0–100 scoring and per-agent drift detection.
3. **Record, per tool, per defect**: detected · detected and silently resolved · not detected · not
   applicable. **The middle column is the one that matters**, because the nearest dead competitor
   computed a duplicate correctly and **discarded the loser in silence** (post-mortem §5), and that
   failure is the reason §6 says *nothing blocks and everything is named*.
4. **Separately, the handover half of secrets**: whether Doppler's or Infisical's free tier does
   anything about what an artefact **carries when it leaves**, as opposed to what a running agent can
   read.

**What would count as an answer.** A grid of tools against our four defect classes. **Two outcomes,
both useful.** If nothing detects the set-level defects, §2's sentence is confirmed at the level it
actually claims and the narrowing in `FINAL.md` §6 can be made precise instead of cautious. If
something does, we learn it now rather than after building the thing it already does.

**What it can never establish.** What the funded closed products do behind their login walls, and
what any of them ships next quarter.

**Cost.** An afternoon, plus whatever the installs fight us over. **Mark: `✓` for what each tool did
on our set, dated and versioned.**

##### Answer — §2's sentence survives at the set level and has to be narrowed twice more at the item level

**Installed and run on 2026-09-10**, against the same archive Q-F used:

| Tool | Repo | ★ | Installed as |
|---|---|---|---|
| **asm** | [`luongnv89/asm`](https://github.com/luongnv89/asm) | 916 | `agent-skill-manager` **2.19.0** |
| **skills** | [`vercel-labs/skills`](https://github.com/vercel-labs/skills) | 30,841 | `skills` **1.5.25** |
| **ai-agent-skills** | [`MoizIbnYousaf/ai-agent-skills`](https://github.com/MoizIbnYousaf/ai-agent-skills) | 1,138 | `ai-agent-skills` **4.3.2** |
| **OpenPackage** | [`enulus/OpenPackage`](https://github.com/enulus/OpenPackage) | 613 | `opkg` **0.11.3** |

**Two of R8's tools could not be installed under the name their README gives**, and this is itself a
correction to round 1: the npm package `harnesskit` belongs to
`hashwanthsutharapu/harnesskit`, a different project, and `tank` belongs to a 2019 package,
`uxstone/mustang`. **`RealZST/HarnessKit`'s trust score and per-agent drift detection remain unrun**,
and the R8 line about them stays vendor self-description.

###### The grid — our four planted defect classes against four shipping tools

Read-only verbs only; nothing was asked to install or modify.

| Defect | asm | skills | ai-agent-skills | opkg |
|---|---|---|---|---|
| duplicate command name `/review` | **not detected** — `audit` reports *"No duplicate skills found"*, correctly, because its unit is a skill and ours were commands | no command concept | no command concept | **not detected** — `list` found nothing at all in the set |
| target-path collision on `.claude/settings.json` | not detected | not detected | not detected | not detected |
| MCP key collision on `memory`, two refs | **no MCP concept** | no MCP concept | no MCP concept | no MCP concept |
| missing env key `GITHUB_TOKEN` | **no env concept** | no env concept | no env concept | no env concept |
| the `pdf` item missing the files it tells the agent to read | **not detected** — `eval` scored it 61/100 with *Structure & completeness 8/10* | — | **not detected** — `validate` returned **PASS · Skill is valid** | — |

**Nothing in the market detects a set-level defect, because nothing in the market has a set-level
unit.** Every one of these tools takes *the skill* as its atom and asks *is this skill duplicated,
safe or stale*. `CLAUDE.md` §2's claim — *what nothing does today is tell you that a skill needs a
particular MCP server, that two skills write to the same config file, that two items register the
same command name* — **is confirmed as run, on four tools, on 2026-09-10.** The narrowing
[`FINAL.md`](../FINAL.md) §6 recorded on README-reading can now be made precise instead of cautious.

###### And then the tool was given a duplicate it *does* claim to handle

Our set contained no duplicate **skill**, so `asm audit`'s correct silence proved nothing. So one was
planted: the `pdf` skill copied into `.codex/skills/pdf/` and `.cursor/skills/pdf/`, and then the
Codex copy's `description:` line edited so the two differ.

- **It does not scan `.cursor/skills/`.** `asm list` shows the item as `[Claude Code] [Codex]`. The
  third copy is invisible — and it is the modified one.
- **On the two it does see, with the files at 8,072 and 8,088 bytes and different sha1s and a
  visibly different `description:` line, it reports:**

> ```
>   "pdf" (same dirName)
>      ✓ identical copies
>     [keep] Claude Code (project) …
>            Codex (project) …
>
>   Run asm audit -y to auto-remove duplicates
> ```

**A 916-star tool declares two demonstrably different files identical and offers to delete one of
them.** That is the Continue post-mortem — *computed the duplicate correctly and discarded the loser
in silence* — reproduced live, except that here it does not compute correctly either. It is the
single best piece of evidence this repository has for **§6's** *nothing blocks, and everything is
named*, and it is dated and re-runnable.

**A second one, same shape.** `asm audit security pdf` returns:

> `pdf — SAFE · 0 files | 0 lines · No suspicious patterns detected.`

A green verdict on a scan that had nothing to scan. **§6 gives *Skipped* its own neutral glyph
precisely so this cannot happen, and here it is happening in a shipping product.** The decision was
taken on reasoning; it now has a specimen.

###### What the market has that our benchmark said nobody had

Three findings that run against us, and they are the reason to run competitors rather than read them.

- **`asm doctor` is a B4 surface.** Thirteen environment health checks: git present and ≥ 2.20, `gh`
  present **and authenticated**, Node version, **21 provider directories writable**, config validity,
  lock-file integrity, registry reachable, disk space, and **PATH shadowing**. The benchmark's
  finding — *B4, produce an artefact and hand it over, is the weakest flow in the industry, nobody
  above 4, and not one cell scores what a product says about the machine its artefact lands on* — was
  measured on funded vendors in August 2026. **A 916-star open-source tool has that surface in
  September.** `ai-agent-skills doctor` has a smaller one, per-target writability across five agents.
- **`asm bundle` is a set.** Its own words: *"A bundle is a reusable recipe of skills for a particular
  workflow, domain, or project setup"*, with `create`, `install`, `list`, `show`, `export`, and
  **369 pre-defined bundles shipped with the tool**, each skill carrying its own
  `install: github:owner/repo:path`. That is a named, shareable, reusable set of items with pinned
  sources — the thing §4 calls a **Project** and §11 calls a **shelf**, in one artefact. **What it is
  not** is checked: a bundle has no dependency edges, no env keys, no MCP servers, no collision pass
  and no archive. **The set-level *concept* is taken. The set-level *check* is still open.**
- **`ai-agent-skills` records provenance and reasons.** `info <name>` shows *"skill details and
  provenance"*; `vendor <source> --why "…"` makes a house copy **with the reason stored**; `--no-deps`
  exists, so catalog installs expand dependencies between skills. §5's *provenance on every item* is
  not an idea we are alone in having.

###### What this establishes, and what it does not

**`✓`, and it covers behaviour, because we watched these programs run on our own artefact.** Dated
2026-09-10, versioned in the table above.

**It does not establish** what Tessl or Smithery do behind a login, what `HarnessKit` does — it could
not be installed — or what any of them ships next quarter. **And step 4 of the plan was not run:**
Doppler's and Infisical's free tiers were not tested for whether they touch what an artefact
**carries when it leaves**. That benchmark gap, opened by Q-D, is still open.

---

#### What these five cannot do, said once and plainly

> **Written before the round was run, and it held.** Nothing below was revised afterwards. Two of
> the five turned out to reach further than this section allowed for — Q-F answered a question about
> the **data model** that nobody had asked, and Q-I placed round 2's Q-E rather than merely adding to
> it — and one reached less far: **Q-G produced a number it cannot interpret without a control**, and
> that control is reported under Q-G rather than hidden here.

- **They do not lift `provisional`.** That label's trigger is five practitioner conversations, and it
  is written into stage 6's plan, stage 7's plan, `CLAUDE.md` §1 and the Q5 disposition. **Interviews
  being unavailable does not lower the bar; it removes the event.** What these five do instead is
  reduce the number of decisions that depend on the label lifting — and **whether anything else may
  ever lift it is the owner's call at the register's next sitting**, not a research finding. It is
  recorded in [`research-plan.md`](../research-plan.md) as a change of standing under Q5.
- **They do not answer Q5** — loss or reassembly cost as the driver of adoption. Q-I touches the edge
  of it and no instrument here can reach a motive.
- **They do not answer Q12** — observability of what ran. That needs a runtime we do not have and
  will not build, and it is the one question whose honest answer is a positioning decision.
- **They do not answer Q10 or Q11** — precedence against an external rule, and the unwritten half.
  Both are properties of a person's judgement; Q-G's fork diffs will show *changes* that were never
  documented, which is a hint at the size of the unwritten half and is not a measurement of it.
- **And none of them reaches a private repository**, which is where the material of the one
  practitioner we did speak to lives. **Every count in this round will over-sample people who
  publish.** That sentence belongs in the write-up of each answer, not only here.

#### What this round would hand forward

| Question | Cost | Cells or entries it could move |
|---|---|---|
| **Q-F** · the handover test | half a day | **NK-13 · D-1**; `CLAUDE.md` §6 and §8's handover stages; the spec's largest bet |
| **Q-G** · forks as receivers | a day | **The whole P2 column · NK-7's receiving half · D-2**; RJ-1's standing |
| **Q-H** · drift in history | a day | **RJ-3 · D-7**; §5's live link, the mechanism its justification rests on |
| **Q-I** · kept or only starred | half a day | **H-J4 · Q9 · NK-9**; what the shelf holds and how it sorts |
| **Q-J** · run the competitors | an afternoon | **§2's core-value sentence · `FINAL.md` §6's fourth narrowing**; RJ-2 and EJ-2's competitor cells; the Doppler/Infisical benchmark gap |

**The order to run them in is the order of the table**, and the reason is not cost. Q-F is the only
one whose result can change the shape of a document rather than the strength of a claim, and every
other row in the audit's dangerous list sits downstream of it.

**Each answer is filed the way rounds 1 and 2 were filed**: the question, the instrument, the capture
log beside it, what it establishes, and — the part this repository has been strict about and should
stay strict about — **what it does not.**

---

### What it actually handed forward — 2026-09-10

**Nothing here is applied to [`CLAUDE.md`](../../CLAUDE.md).** A research round may narrow a claim,
close a hypothesis and raise a proposal; the owner edits the spec, at the register's sitting. This
section is the list that sitting reads, on top of the two proposal lists it already had.

#### Two hypotheses are closed, and one register entry gains its first behavioural evidence

| | Was | Is now |
|---|---|---|
| **NK-13 / D-1** — *a receiving agent performs the setup from `SETUP.md` alone* | The spec's largest bet, taken on reasoning, never tested | **Closed `✓`.** Three of three receivers performed it, including cloning at the pinned ref. **And the second half of the bet failed**: leaving the Problems to the receiver does not work |
| **H6** in [`personas.md`](personas.md) | *Not closed, and the web cannot close it* | **Closed by Q-F**, on the same evidence |
| **H-J4 / Q9** — *does the shelf's premise describe a real behaviour* | Opinion only: four of five practitioners negative (Q-E) | **Behaviour measured.** Thousands of repositories vendor public skills; 32% of imports are edited, at a median of 27 days; 10% keep provenance |

#### Six proposals, each with the evidence that raised it

| # | Spec section | What was found | Proposal |
|---|---|---|---|
| **S-1** | **§6**, `SETUP.md` | Of three receivers, one found the Problems, one **mis-resolved** one on a false claim of byte-identity, one saw none. The document states requirements and not findings, by design | **`SETUP.md` should carry the set's Problems.** The disclosure §8 gives the *sender* before Export is the disclosure the *receiver* turns out to need. This is the round's largest proposal |
| **S-2** | **§5**, the `Item` shape | The `pdf` skill instructs the agent to read `REFERENCE.md`, `FORMS.md` and eight scripts. `content` holds one blob and `targetPath` one destination, so **the export was silently incomplete and `SETUP.md` said the item required nothing** | **An item addresses a directory, not a file.** This is a model change, and it is the only one this round proposes |
| **S-3** | **§6**, what an item can do | The `settings.json` that won the collision **declares a third-party plugin marketplace and enables a plugin from it**. An archive can reconfigure the receiving agent before setup begins | **Treat a settings file as an executable item**, and say so where §6 lists what export produces |
| **S-4** | **§6**, `needsEnv` · **RJ-4** | A receiver told only to *set this project up* **copied the machine's live OAuth token out of the keyring into a plaintext file**. First observation ever on RJ-4's receiving side | **The secrets risk runs both ways.** What the receiver fetches to fill the gap the sender left is a hazard the spec does not name |
| **S-5** | **§2**, *nothing does this today* | Four tools installed and run: **nothing detects a set-level defect, because nothing has a set-level unit.** But `asm` ships **369 pre-defined bundles** — *"a reusable recipe of skills for a project setup"* — and `asm doctor` is a **B4 surface**, which the benchmark said nobody had | **Narrow it precisely rather than cautiously.** The set-level *check* is unoccupied; the set-level *concept* and the receiving-machine *report* are not |
| **S-6** | **§6**, three severities | `asm audit` calls two files with different sha1s *"✓ identical copies"* and offers to auto-remove one. `asm audit security` returns **SAFE** on a scan of *0 files, 0 lines* | **No change — evidence for a decision already taken.** *Nothing blocks, everything is named*, and *Skipped* gets a glyph it earned, now each have a dated specimen in a shipping product |

#### What did not move, and one thing that got harder

- **Q5, Q10, Q11, Q12 are untouched**, exactly as the plan said. Motive, precedence against an
  external rule, the unwritten half, and observability all need a person.
- **The *provisional* label does not lift.** Its trigger is five practitioner conversations. Four
  hypotheses closing does not change what the trigger is, and this round deliberately does not argue
  that it should.
- **Q-H made intent harder to read, not easier.** Reconciliation is essentially never observed, so
  there is no behavioural signature separating *drift nobody noticed* from *a copy somebody meant to
  keep different*.
- **Two things this round was supposed to do and did not.** Doppler and Infisical were not tested for
  the handover half of secrets — the benchmark gap Q-D opened stays open. And `HarnessKit`, whose
  trust score and per-agent drift detection are the sharpest competing claims in R8, **could not be
  installed**: the npm name belongs to a different project.

#### And what the round says about its own instruments

**Three measurements were built, checked and thrown away before anything was written**: a path-rewrite
rule that counted every diff line mentioning a home directory (69% → 12% under a matched-pair rule);
a provenance rule that matched the word `license`, which every one of these skills carries in its own
frontmatter (82% → 10%); and a second provenance rule matching *"based on"*, which was matching
ordinary prose. **The discarded versions are named here on purpose.** A round that only reports the
rules that survived is indistinguishable from one that had no rules.

**And a fourth thing was thrown away after it was written: the round's most arresting number.** Q-G's
89.4% was already drafted as *the third outcome the plan named* when the control came back at 84.8%
and 87.0% for populations with nothing to do with agents. **The interpretation was withdrawn and the
draft rewritten**, and the sequence is left visible in the section rather than tidied away. The
control cost twenty minutes and it is the single most useful twenty minutes in the round.


---

# Round 4. The matrix’s empty cells

> **Collected 2026-09-10.** Straight at the persona columns, in venues this repository had never used — and then at our own fork corpus, asked a question nobody had asked it.
>
> *Merged into this file on 2026-09-10 from the file that was `re-research-4.md`, unchanged.*

### Re-research, round 4 — hunting the matrix's empty cells

**A source document.** Collected 2026-09-10, the same day round 3 was run. Capture log beside it:
[`_captures/round4-log.json`](_captures/round4-log.json).

**Why it exists.** Round 3 answered five questions and **moved no importance in the matrix**, for a
structural reason it stated plainly: the matrix's columns are people and round 3's instruments see
machines and artefacts. So this round goes after the columns directly. **The matrix has 36 `[?]`
cells** — 19 in the sourced table (P1 has two, P2 seven, P3 all ten) and 17 among the hypothesis
rows — and a cell is filled only by somebody in that persona's shape saying what something **cost**
them, or showing that they **changed how they work**.

**The instrument had to change, because the corpus has a hole in exactly the shape of the people we
need.** Everything read so far is GitHub issue filers and Hacker News commenters. **A receiver files
nothing** — the thing they received is not their project — **and a beginner has nothing to file
about.** That is why P2 carries a number in three rows of ten and P3 in none, and no amount of
re-reading the same two venues fixes it.

#### The venues, and one that still refuses

| # | Instrument | What it reaches | Blind to |
|---|---|---|---|
| **I12** | **[forum.cursor.com](https://forum.cursor.com)** — Discourse search and topic JSON | Cursor's own users asking for help in their own words, **and the vendor's staff answering them on the record** | Anyone not on that forum. A help forum over-samples people whose thing is broken |
| **I13** | **[community.openai.com](https://community.openai.com)** — same API | Codex and ChatGPT users, same shape | Same |
| **I3c** | **Hacker News via Algolia**, searched for the **situation** rather than the subject | Full comment text, exact phrases | The HN population, self-selected as ever |
| **I14** | **Reddit** | **Nothing. HTTP 403 on 2026-09-10** | Everything. This is [`re-research.md`](re-research.md) R13 unchanged: the venue a community survey names for this population has been unreachable to us for the whole phase |

**Neither Discourse forum has ever been touched by this repository**, and between them they are the
first venue in the corpus where **the vendor answers in public** — several findings below are a
vendor engineer confirming a defect, which is a different kind of source from a user reporting one.

**Volumes.** 25 body queries × 2 forums → 2,140 hits, **1,929 unique posts fetched in full**;
52 title queries → **955 unique topics**; 23 HN queries → **394 comments and stories**;
**17 threads read end to end.**

**One method note, because a discarded pass is worth as much as a kept one.** The first pass matched
first-person markers against post bodies and produced 52 "receivers" — nearly all of them Cursor's
own **model-inheritance** feature, where *"inherited"* is jargon. That pass was thrown away. The one
that worked searches **titles**: on a Q&A forum, a person in the shape we need announces it in the
title.

---

#### What was found, and what it does to the matrix

**Three cells change, and this is the first round that adds to the matrix rather than subtracting
from it.** The audit of 2026-09-09 only ever removed; round 3 moved nothing vertical. Below, two
`[?]` become numbers and one number goes up, each with the utterance under it.

---

##### F1 — RJ-2 / P1: **2 → 3.** A collection that collides, a vendor confirming it, and two people who rebuilt their tooling around it

**[Excessive Token Usage: Cursor auto-loads too many "Skills" from `~/.claude/skills`](https://forum.cursor.com/t/excessive-token-usage-cursor-auto-loads-too-many-skills-from-claude-skills-at-conversation-start/160677)** — 571 views, 9 replies, filed 2026-05-14, **still open**.

The filer's own words: Cursor *"recursively scan[s] hidden directories within the skills folder,
loading skills meant for other Agent CLIs (like openclaw) that are not relevant to the current
session. **Duplicated SKILLs will also be loaded.** E.g. when you install GStack, same SKILLs from
`~/.agent/skills` and `~/.claude/skills` will be loaded."*

**The vendor confirms it, in public, and names why the deduplication fails:**

> *"Confirmed: the recursive skills scanner doesn't filter hidden directories inside
> `~/.claude/skills/`, so anything in `.hermes/`, `.opencode/`, `.gstack/`, and similar subfolders
> from other agent CLIs gets pulled into context. **On dedup:** normalization works for
> `~/.claude/skills` vs `~/.cursor/skills`, but GStack stores skills in `~/.agent/skills` (no `s` at
> the end), and we only detect `~/.agents/skills`. **That's why duplicates don't collapse in your
> case.** … No fix yet."* — `deanrie`, Cursor

**Why this is a 3 and not a 2.** The audit's rule is that a **3** means *a reason they would change
how they work*, and it lowered four cells because the person on record demonstrably did not. Here
two people demonstrably did:

- **`Demianight`** moved the offending items by hand, found that *"every Cursor update re-downloads
  anything missing from `skills-cursor/`, so the fix doesn't survive"*, and **wrote a script that
  purges the folder and marks it immutable with `chflags uchg` after every update.**
- **`zar42stra`** wrote a wrapper that **re-executes `cursor-agent` inside a private mount namespace
  and bind-mounts empty directories over every skill root**, so only the intended ones remain
  visible. The vendor's reply calls it *"a workable solution"* and adds the caveats.

**And it carries X6 with it.** The claim that *the collection created the problem* has stood on one
sentence from one interview since 2026-09-08. Here it is again, independently:

> *"it's not really about context size — it's that **agents spread their focus onto irrelevant
> built-ins** … even when the task has nothing to do with that."* — `Demianight`

**The cost is stated in the unit the venue cares about**: the initial context window. **Note what the
cell now rests on**: a vendor-confirmed duplicate-detection failure across four skill roots, and two
users who rebuilt their tooling rather than live with it.

---

##### F2 — EJ-2 / P1: **`[?]` → 2.** Somebody asking to see the context window in order to tell *not loaded* from *not followed*

The audit withdrew this cell's number on 2026-09-09 (J-74) because the evidence under it was HN
comments with no weighting. It now has a person, a cost and ten days of chasing.

**[Rules not being applied as expected](https://forum.cursor.com/t/rules-not-being-applied-as-expected/144731)**
— 457 views, filed 2025-11-30 by `Margus_Niitsoo`, who built a **minimal reproduction repository**
for it. His conclusion after three rounds of replies:

> *"It would **Really** be useful if we could **inspect the raw full context window** of the Agent
> chat, as that would make it very easy to tell if it is **an issue with AI not loading the rule vs
> just deciding not to follow them**."*

**That sentence is the whole of EJ-2 in one line** — you cannot believe a result you cannot audit —
and it is the sharpest public statement of **Q12** anybody has made. The vendor's answer confirms the
ground under it:

> *"This is a known issue — rules apply inconsistently, especially with glob patterns and intelligent
> context. … Composer 1 often ignores conditional rules … **Even `alwaysApply: true` sometimes
> doesn't apply automatically on the first request.** … Regarding tooltip bugs: I completely agree.
> **'Active Rules' should show all applied rules**, not just `alwaysApply: true`."* — `deanrie`

**Why 2 and not 3.** It cost him a repro repo and ten days, and he calls the rules system *"rather
unusable"* — that is a cost. **He did not change how he works**; he asked the vendor for a way to
see. The rule says that is a 2.

**Register consequence, and it is the larger half of this finding. Q12 — *is the wanted thing
observability of what ran rather than validation that a set coheres* — has stood on one person since
2026-09-07.** It now stands on two, and the second is **public, dated and re-runnable**. The
disposition is still the owner's; what changed is that the question is no longer one interviewee's
aside.

---

##### F3 — H-J3 / P1: **`[?]` → 2.** The detach requirement, stated by somebody who has it and cannot get it

This is the cell the audit was harshest about. J-107, 2026-09-09: in-project editing and promotion
*"stand on nothing rather than on one aside"* — **"nobody has said anything about wanting one."**

**[Rules in home folder (`~/.cursor/rules`) are not applied](https://forum.cursor.com/t/rules-in-home-folder-cursor-rules-are-not-applied/147236)**
— 396 views, `shiitake3`, 2025-12-24. Asked why the documented feature does not work, he is pointed
at the vendor's User Rules setting, and answers with his actual requirements:

> *"I'm aware of that feature, but there are a few main drawbacks — no way to apply rules
> conditionally — **I need share the rules with my team** — **my organization doesn't allow us to use
> team rules** — **each user should be able to slightly modify the rules**."*

**One shared source, and each user able to slightly modify their copy, is `detached` and `overrides`
in §5, described as a requirement by somebody who has no mechanism for it.** He is blocked three
ways at once: the documented home-folder route is broken (the vendor confirms it is a bug), the
vendor's own team feature is forbidden by his organisation, and committing to the repo does not give
him the per-user variation.

**Why 2 and not 3.** It costs him — he cannot do the thing at all — and there is no evidence he
changed how he works.

**And it lands on §9's orphan list.** *Promote a detached item* was listed there as closing a job
that stands on **nothing**. It now stands on one person outside this project, in public, unprompted,
and describing the mechanism rather than the feature.

---

##### F4 — What did not change: the P2 column, and it is not for want of looking

**Handover to a team is asked about repeatedly on the vendor's own forum, and the official answer is
a workaround.** Four independent topics, three of them titled almost identically:

| Thread | When | What happened |
|---|---|---|
| [How do I share cursor rules with my team](https://forum.cursor.com/t/how-do-i-share-cursor-rules-with-my-team/48454) · 1,375 views | 2025-02 | Answer: *"you can always commit the rules inside of your Repo."* The asker replies: *"my problem is not really the sharing part. **My problem is the fact that AI doesnt seem to follow those rules**"* — and ends up invoking them by hand with `@` |
| [How do I share cursor rules with my team？](https://forum.cursor.com/t/how-do-i-share-cursor-rules-with-my-team/50213) · 1,384 views | 2025-02 | *"I enabled 'Share with Team' but **my team members don't see anything**."* Answer: *"You can commit cursorrules to git."* |
| [How can i share rules with my team?](https://forum.cursor.com/t/how-can-i-share-rules-with-my-team/144065) | 2025-11 | *"I wonder, if there any publish or pull method"* — **no reply, auto-closed after 90 days** |
| [Shared Skills on Cloud Agents](https://forum.cursor.com/t/shared-skills-on-cloud-agents/165324) | 2026-07 | *"I have **a custom MCP that requires a skill** to be able to use. **It's a PITA to distribute it to my team.**"* |

**Two things fall out of this and neither is a persona number.**

- **`requires` between an MCP server and a skill is sighted in the wild**, in a user's own words, as
  the reason distribution is hard. §5's `requires` relation and §6's dependency walk have their first
  public instance that is not our own reasoning.
- **The market's managed answer to set-level distribution is a paid tier.** The vendor's resolution
  for `lonny`: *"wrap the skill as a plugin in the **Team Marketplace** and mark it as **Required** so
  it installs for everyone automatically. But that's only available on **Teams/Enterprise**."* The
  user's reply: *"Huge unlock right now."* **A set that installs for everyone exists, behind a
  business plan**, and that is a competitor fact `CLAUDE.md` §2 should know.

**But every one of these people is a sender.** The receiver appears only in the third person — *"my
team members don't see anything"* — exactly as in every other instrument. **P2's seven `[?]` stay
`[?]`, and its three 2s stay second-hand.** After four rounds and five venues, **no receiver has
spoken in the first person**, which is now a finding about the population rather than about our
search: the person who receives has no reason to post, because the thing they received is not theirs.

---

##### F5 — P3: two beginners, and **neither reaches for a shelf**

The clearest beginner posts on the vendor's forum, both **asked once and never answered**:

- **[Beginner with Agents in Cursor AI](https://forum.cursor.com/t/beginner-with-agents-in-cursor-ai/137798)** — *"I've been using Cursor for a few days… I've connected a Supabase MCP and **created a detailed Markdown file with all the info about the project**… I've asked 10 times already."* **He wrote his own material on day one.** No reply; auto-closed.
- **[Cursor for beginner — need general guidance](https://forum.cursor.com/t/cursor-for-beginner-need-general-guidance/75300)** — *"I'm new here… I wanted to see what projects people have built… **I was wondering if anyone experienced here would be willing to let me shadow them as they code for 30 mins**."* **He asks for a person, not a library.** No reply.

**Neither is P3 in the sense §11's shelf is built for.** One had nothing and immediately made his own;
the other wanted to watch a human. **P3's column stays `[?]` in all ten rows**, and this is now the
third instrument to look for that persona and fail to find it — [`re-research.md` round 2](re-research.md#round-2-counting-not-asking)
Q-E, round 3's Q-I, and this. **What round 3 established stands and is unaffected**: the *behaviour*
the shelf assumes — importing other people's material and coming back to edit it — is real and large.
**What no instrument has found is a person who has nothing and wants somebody else's.**

---

##### F6 — Corroborations that change no cell and are worth having

- **The agent is a more reliable reader than the human.** *"I think it won't be bigger than the giant set of rules people are supposed to read through (**they never do**) when onboarding. At least with AGENTS/CLAUDE.md file, **you know the agent will re-read those rules on every new session**."* — [egeozcan, HN](https://news.ycombinator.com/item?id=46741655). This is `CLAUDE.md` §6's Q2 decision — *`SETUP.md` is written for the agent, not for a human reader* — argued by somebody who has never heard of us.
- **`CLAUDE.md` is described as onboarding documentation** by two independent HN commenters ([theshrike79](https://news.ycombinator.com/item?id=45123992), [btbuildem](https://news.ycombinator.com/item?id=44936992)), which is SJ-1's premise from the sender's side.
- **A handover artefact is wanted and does not exist.** [Help me find or create an handover skill](https://community.openai.com/t/help-me-find-or-create-an-handover-skill/1374002) — 453 views on a two-post thread: *"I'm looking for a skill which I can use at the end of a session to create an handoff document… I had a look at the `curated` skills using the `skill-installer` but **I couldn't find anything**."* The answer is a manual workaround: enforce a session log in `agents.md`.
- **Multi-device sync is "awkward", and the answer is again a repo.** [Sync global rules](https://forum.cursor.com/t/sync-global-rules-and-chats/66299), 760 views: three devices, *"Sharing rules is awkward, but doable"*; the community's answer is *"set up a repo for you to store all of your rules in… pull down what I need for each project"* — R2's symlink-and-repo workaround, a fourth time.
- **A second, independent source for §11's security number.** [Agensi](https://news.ycombinator.com/item?id=47846681), a curated SKILL.md marketplace, states *"36% of sampled skills had prompt injection vectors"* and scans every listing. Round 1's R6 had this from Snyk alone, *published, not verified by us*; it now has a second party acting on the same order of magnitude. **§11 still has no content-review standard.**

---

---

### Second pass, the same day — four more cells, two of them P2

**The first pass had a blind spot of its own.** It went looking for what people *say* and concluded
that the receiver never speaks. **That is true and it is not the only way to reach a receiver.**
Round 3 had already read **214 forks in full, with their patches**, and classified them for a
different question; nobody had asked that corpus about the matrix. **A receiver who never posts still
leaves a diff.**

Plus one more sweep of the two forums, aimed at the three P1 cells the first pass did not touch.

##### F7 — RJ-3 / P1: **2 → 3.** The job stated verbatim, with its cost, by somebody who tried five mechanisms

The audit lowered this cell to a 2 on 2026-09-09 with a sharp reason: the one person on record *"still
moves material with `cp -r`"* — he paid the price and changed nothing. **A second person did the
opposite.**

**[Question about syncing plugin changes across projects](https://forum.cursor.com/t/question-about-syncing-plugin-changes-across-projects-local-development/167666)**
— 8 replies, 2026-08-07, `Pavel_Mikhalev`:

> *"I'm forced to **duplicate configuration files (rules and skills) across projects manually**. This
> creates the following difficulties: **When I need to refine a rule in one project, I have to
> simultaneously apply the same changes to all other projects where that rule is used.** This
> approach requires constant context switching and carries the **risk of forgetting to update a copy,
> leading to inconsistencies in agent behavior across projects.**"*

**That is RJ-3's sentence, written by somebody who has never heard of us**, and the thread is a record
of **five mechanisms tried and five failures**: the plugin installer *"can stay pinned to the first
commit"*; the local plugin folder *"applies globally to all projects, and there's no way to
enable/disable them on a per-project basis"*; two marketplace update paths where *"nothing would
actually update"*; and the symlink route, which works and then dies — *"these rules shouldn't be
stored inside the project itself, which means they need to be in `.gitignore`. But if they're in
`.gitignore`, **Cursor doesn't see them and ignores them**."*

**Rebuilding your tooling five times is the audit's own test for a 3, met.** And the last failure is
**H-J3 again, from a second independent person**: what he needs is one shared source with per-project
enable and disable.

##### F8 — H-J1 / P1: **`[?]` → 2.** A prompt library that is a folder of notes in Telegram

H-J1 has stood on a single interview sighting since 2026-09-08, and jtbd's own orphan list called it
*"the market's best-served flow **and** our thinnest evidence"*.

**[Prompt library (Notepads 2.0)](https://forum.cursor.com/t/prompt-library-notepads-2-0/148996)** —
`Artemonim`, a Cursor user with skills and subagents:

> *"Right now, I have several templates **in my notes in Telegram**, and I have to copy them into new
> chats, **as well as manually enter each link to each file, command, or skill** that I want to use to
> start a new chat."*

He then asks himself whether skills already solve it — *"Maybe I should try the skills 🤔"* — and
answers two posts later: **"No, that's not it."**

**Corroborated in an adjacent population** by [a full specification of the missing
thing](https://community.openai.com/t/a-built-in-prompt-vault-or-prompt-library-added-to-chatgpt-would-be-extremely-useful/1390442):
save, name, **folders, tags, search**, edit, duplicate, templates with variables — *"I regularly
create prompts that I want to reuse, but currently there isn't a simple way to save individual
prompts… and organize them for later."* The vendor's answer: *"No timeline to share yet."*

**A 2: manual re-entry every time is a cost, and neither of them changed how they work.** The
adjacent-population caveat is real — the second person's use is image and SEO work, not coding — so
the cell rests on the first and cites the second.

##### F9 — RJ-4 / P2: **`[?]` → 2**, and it is **behaviour, not an account**

The cell read *"`.env.example` exists for the receiver, and **no receiver has said anything about
it**."* Still true. **Four of them were watched doing it instead.**

In the 214 forks round 3 read, at least four independent receivers touch secrets in inherited
material among their first commits:

- **[`insurgently/dotfiles`](https://github.com/insurgently/dotfiles)** — a commit titled **"remove
  encrypted files"**, deleting `home/.key.txt.age`, an encrypted VPN credential, the author's
  encrypted **GPG trustdb and keyring**, and an encrypted **SSH private key**.
- **`trang-kaleido/kaleid.mvp-claude`** — a commit titled **"Re-committing work without secrets"**,
  and in the same fork a **40-line `.env.example`** the inherited material did not have. **A receiver
  reinventing §6's mechanism after being burned by its absence.**
- **`toshiyan76/github-cursor-rules-agent`** — *"APIキーの変更"*, modifying `.env.example`.
- **`EyalShay-Debz/dotclaude`** — *"chore: utils and env key"*, modifying `.env.mcp`.

**A 2: a cleanup, and in one case a history rewrite. Not a 3 — nobody is on record changing how they
work.**

##### F10 — SJ-1 / P2: **`[?]` → 2.** Receivers write the manual the sender did not ship, and they name it themselves

**30 of 214 committers — 14% — added a setup, handover or installation document that the material
they received did not contain. Together: 21,266 lines.**

The names are theirs, not ours: **`HANDOFF.md` at 229 lines as the fork's only commit**; another
`HANDOFF.md` at 1,041; `SETUP.md` at 425; `INSTALL-GUIDE.md` at 283; **`docs/windows-setup.md` at
284** — which is stage 3's environmental pain, on the receiving side; `mcp-setup.md`, `lsp-setup.md`,
`developer-setup.md`, `cross-machine-claude-setup.md`; and one commit titled **"Make `setup.sh` safe
for complex pre-existing installs"** beside a 120-line note on adapting an install to a machine that
already had things.

**Counted strictly.** A fork adding its own `CLAUDE.md` or `AGENTS.md` is adding *material*, not
writing a *manual*; those are a separate 39 forks and are excluded from the 30.

**A 2: hours of writing, repeatedly, to supply what the sender did not send.**

##### F11 — RJ-1 / P1 was hunted deliberately and is still `[?]`, which is worth recording

[`jtbd.md`](../7-jobs-to-be-done/jtbd.md) §8 says the gap between what the spec spends on RJ-1 —
§8's whole disclosure-before-Export apparatus — and what the evidence carries there is **the widest in
the file**, and that *"if one practitioner says it plainly, it moves into the core ahead of RJ-3."*

**This round went looking for that sentence on purpose**, with six title queries aimed at it —
*what to include*, *checklist*, *what does it need*, *requirements to run*, *works on my machine*,
*missing dependency* — across both forums. **What came back was system requirements, to-do lists and
a method framework.** Nobody, anywhere in five venues, says *I wish I had known what the other side
would need before I sent it.*

**That is now a deliberate negative rather than an absence nobody looked for**, and it makes the gap
§8 named larger rather than smaller. **RJ-3 has since moved to a 3 (F7), so the sentence about RJ-1
overtaking it needs re-reading at the sitting.**

---

---

### Third pass — the last one, and it ends on a wall worth naming

Two cells filled in the first pass, four in the second. **This pass went at what was left, and got
one — and the reason it got only one is the most useful thing it produced.**

Three targets, one new venue, and one deliberate inversion of the method.

##### F12 — H-J7 / P1: **`[?]` → 2.** Four people, one price, and a sampling problem said out loud

The unwritten half has stood on **one aside from one interview** since 2026-09-07 — *"roughly half of
what makes a project go well is stuff I've never written down"* — and it is **Q11** in the register.
Four independent people say it in public, in the first person:

- *"You lose context, lose progress, **re-explain everything, and waste 10–30 minutes every time**"* —
  [Drift](https://news.ycombinator.com/item?id=47934325). **The only price anybody has put on it.**
- *"Claude Code keeps forgetting what it learned. **Every session I'd re-explain the architecture,
  re-discover the same bugs, re-learn the same solutions.** `CLAUDE.md` helps but it's manual"* —
  [Memory-Graph](https://news.ycombinator.com/item?id=46091577).
- *"Every time I switch tools/models, I have to re-explain the project. **Specs live in my head** or
  in random chat history"* — [Spec-AGENTS.md](https://news.ycombinator.com/item?id=46286705).
- *"I've been the lead developer for this client for over six years… **All the institutional
  knowledge lived in my head.** I brought up the bus factor problem myself and built a continuity
  package to eliminate it"* — [a continuity package](https://news.ycombinator.com/item?id=47309623).

**A 2, and deliberately not a 3, for a reason that had to be checked rather than assumed.** All four
also **built and shipped software** about it, which looks like the audit's test for a 3 — *a reason
they would change how they work*. **It is not, because of how they were found.** These are Show HN
posts, and in that venue **having built something is the entry ticket**: sampling there and then
counting the building as evidence of importance is circular. What survives the circularity is the
**stated cost**, four times, once with a number. **Their posts scored 1, 2, 2 and 3 points**, so the
venue's own weighting is worth nothing either — which is J-74's rule, applied to us this time.

**And the fourth voice repays reading beyond its cell.** The same person, handing six years of work
to a client, solved the credential problem **exactly as `CLAUDE.md` §6 does**, without having heard
of us: *"You need secrets accessible for handoff but you can't commit them… the documentation repo
has **references to every credential — what it is, where it's used, who owns it — but zero actual
values.** A separate gitignored secrets directory holds the real `.env` files."* That is
`needsEnv` collected across the set and written to `.env.example`, invented independently by somebody
doing a real handover. **It is one person on a post nobody read**, so it corroborates and does not
raise anything.

##### F13 — P3, at the shelf's own doorstep, and still nothing

Four instruments have hunted the empty-handed and failed. **This pass inverted the method**: instead
of going where people are and asking whether any of them has nothing, it went to **the shelves
themselves** — 18 of the largest public collections and installer tools, **568 issues** — on the
grounds that somebody who turns up at a stranger's shelf and asks a question is P3-shaped by
construction.

**Nine issues match the language. Three are real people, and not one can be shown to be
empty-handed.** They are, in order of what they teach:

- **[`vijaythecoder/awesome-claude-agents#28`](https://github.com/vijaythecoder/awesome-claude-agents/issues/28)** — 4,386★. *"Many agents in this repository are instructed to use a tool called **`context7 MCP`**… the project's documentation provides **no explanation of what this tool is, how to install it, or how it works.** This creates an immediate and significant usability hurdle for new users, **as they are unable to run these agents as intended, leading to immediate failure and frustration.**"* **A shelf of items with an undeclared MCP dependency, and consumers blocked at exactly the point §5's `requires`, §6's dependency walk and `SETUP.md` exist for.** It is the best public justification of the product's core mechanic in the entire corpus — and it fills no cell, because we cannot say who the filer is.
- **[`enulus/OpenPackage#45`](https://github.com/enulus/OpenPackage/issues/45)** — *"**first timer here. Is this supposed to happen? What should i do here?** It keeps spamming the message for every agents"*, against a prompt reading `File 'pattern' already exists in package 'project1'. Choose how to proceed: Keep existing file (skip) / Replace with workspace file / Cancel`. **A competitor's collision UX, met by a newcomer, per file, per agent, and he cannot answer it.** That is a warning aimed straight at §6's Run: naming a collision is not the same as making it answerable.
- **[`enulus/OpenPackage#12`](https://github.com/enulus/OpenPackage/issues/12)** — *"how to install a package for a particular agent **when you have multiple agents installed like I have**… It's not clear from the doc"*. And, in passing: *"I put this comment on reddit but **it got deleted**."*

**P3 stays `[?]` in all ten rows.**

##### F14 — RJ-1 and H-J2, hunted a second time and still empty

**RJ-1** was hunted in the second pass with six title queries and in this one from the opposite
direction — the receiver's complaint rather than the sender's regret. Nothing. **Nobody in six venues
says they wished they had known what the other side would need before sending.**

**H-J2** — *start from something I have done before and re-tune it* — was hunted with nine phrasings
across HN and both forums. **What came back was always sharing, never duplicating**: people want one
source of rules to reach several projects, which is RJ-3, and nobody describes copying a whole
previous project and adjusting it. **The specified feature it would justify is *duplicate a project*,
and after four rounds it is the one orphan on §9's list that nothing has touched.**

##### The wall, named

**The blocker on what remains is not evidence. It is persona attribution.**

This pass kept finding real people doing exactly the things the matrix is about — blocked by an
undeclared MCP dependency, unable to answer a collision prompt, confused by multiple agent targets —
and could not use any of them, **because a public artefact shows an act and a persona is defined by a
situation.** You can see that somebody installed a stranger's agents and could not run them. You
cannot see whether they had material of their own.

**That is the honest end of this method.** P2's remaining five and P3's ten are not waiting for a
better query; they are waiting for somebody to be **asked** — which is the instrument that became
unavailable on 2026-09-09, and the reason the *provisional* label is still where it is.

---

#### What the three passes did to the matrix, counted

| | This morning | Tonight |
|---|---|---|
| `[?]` cells in the matrix | **36** | **30** |
| `[?]` in the **P1** column | 7 | **3** — RJ-1, H-J2, H-J4 |
| `[?]` in the **P2** column | 7 | **5** |
| `[?]` in the **P3** column | 10 | **10** |
| Numbers raised | — | **RJ-2 2→3 · RJ-3 2→3** |
| Cells filled | — | **EJ-2/P1 · H-J3/P1 · H-J1/P1 · H-J7/P1 · RJ-4/P2 · SJ-1/P2** |
| Register entries that moved | — | **Q12** no longer one person · **Q11** no longer one aside |

**And one qualitative change worth more than the count.** [`jtbd.md`](../7-jobs-to-be-done/jtbd.md)
§7 said **every P2 cell carrying a number is second-hand.** That is no longer true: **RJ-4/P2 and
SJ-1/P2 rest on diffs.** The receiver still never speaks — **and we no longer need them to, for the
things a diff can show.**

#### What this round establishes, and what it does not

**Establishes, at utterance level, rule 5 governing:** three matrix cells have evidence they did not
have this morning, and **for the first time the movement is upward.** RJ-2's P1 rests on a
vendor-confirmed duplicate-detection failure and two people who rebuilt their tooling around it;
EJ-2's P1 and H-J3's P1 rest on one named person each, with the quote and the thread.

**Establishes about the population, not about our search:** **the receiver does not post.** Four
rounds, five venues, and every account of a handover is written by the person who sent it. That is
the strongest thing this round says about P2, and it is a reason to stop pointing register entries at
"ask a receiver" as though the difficulty were effort.

**Does not establish:** anything about P3, whose column is untouched and whose two clearest public
representatives did the opposite of what the shelf assumes. Anything about motive — Q5 is as far away
as ever. And nothing at all about the people for whom this works, because **every venue here is a
place people go when something is broken.**

**Not applied to [`CLAUDE.md`](../../CLAUDE.md).** Two things go to the register's sitting: **Q12 now
stands on two people rather than one**, and **§9's orphan entry for *promote a detached item* no
longer stands on nothing.** Neither is a decision, and this document does not take one.


---
