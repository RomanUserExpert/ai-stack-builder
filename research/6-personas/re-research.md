# Re-research — closing what the inventory left open

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

## 1. The instruments, and what each can and cannot see

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
| [`_re-research-gh.json`](_re-research-gh.json) | 30 queries, 120 issues — title, reaction count, comment count, state, date, URL. **Plus the full body of all 21 issues quoted in this document**, so the quotes can be checked without re-fetching. |
| [`_re-research-hn-threads.json`](_re-research-hn-threads.json) | 8 threads, **1,762 comments in full text**, with author, date and item id. |
| [`_re-research-hn.json`](_re-research-hn.json) | 6 keyword queries, 38 hits, with the `nbHits` each query returned. |
| [`_re-research-web.json`](_re-research-web.json) | 9 web sources and 9 repositories, each with its **kind**, the specific figures taken from it, its caveat, and an HTTP link check run 2026-09-07. |

**What the logs deliberately do not hold.** Bodies for the 99 issues that were ranked but not
quoted — the ranking used titles and counts, and those are stored. Comment threads for the GitHub
issues. And the READMEs of the nine repositories in R8, which were read live and are quoted in place;
the repository list is logged so they can be re-read.

---

## 2. Findings

### R1 — The loudest thing in our audience's own tracker is *one source, many agents*

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

### R2 — And one person really does keep several targets at once

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

### R3 — Reassembly cost was filed after all, and stage 3 looked in the wrong shape

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

### R4 — The first real number on library size, and it disagrees with stage 5

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

### R5 — Where the material lives, and where people want it to live

- **[claude-code #1455 — does not respect the XDG Base Directory specification](https://github.com/anthropics/claude-code/issues/1455)** — **446 reactions**, open since 2025-05-31. The same request on Codex: [#1980](https://github.com/openai/codex/issues/1980), 134 reactions.
- **`~/.claude/skills/` versus the Desktop app's own location** — [#20697](https://github.com/anthropics/claude-code/issues/20697), 161 reactions.
- **A git repo as the source of truth** — [#28729](https://github.com/anthropics/claude-code/issues/28729), 151 reactions, asks for exactly that. On GitHub, `SkillCatalog` bills itself as *"a Git-native skill manager"* and `agent-dotfiles` as *"Write AI coding rules once, sync to every agent"*.
- **A personal directory plus symlinks** — R2's quotes.
- **Deliberately nowhere**: *"I really like Claude, but **I don't track Claude resources in our repos.** If something better comes along, I'm better [off]"* — [allknowingfrog](https://news.ycombinator.com/item?id=48184129), 2026-05-18. A refusal to commit the material at all, on lock-in grounds.

**Closes: NK-6.** It lives in dotfiles repos, in `~/.claude/skills/`, in per-project files, and in
symlink farms between them — and a weighted request exists for a **git repo to be the source**.

### R6 — The fear rows, and they are heavier than anything stage 3 found

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

### R7 — The doubt that actually dominates, and the spec never anticipated it

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

### R8 — The ground is not unoccupied any more

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

### R9 — The scale everything else now sits inside

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

### R10 — Portfolio: searched twice, found nothing

- **0 matches in 1,762 HN comments** for `portfolio`, `show off`, `publish my…`, `share my setup`.
- `portfolio in:title` in `anthropics/claude-code`: **2 issues, both 0 reactions, both unrelated** (a
  finance portfolio and a blocked API request).

**NK-18 stays `[?]`**, but the absence has now been looked for in two instruments rather than assumed.
Consistent with `CLAUDE.md` §9 keeping publishing out of the MVP.

### R11 — Licensing has a rule shape now

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

### R12 — Team and handover: somebody else does open these

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

### R13 — Where this population actually is

Named repeatedly across community surveys: **Discord** — Latent Space, Anthropic's own Claude Code
channels, Cursor, Ollama, Hugging Face; **Reddit** — r/ClaudeAI, r/ChatGPTCoding, r/LocalLLaMA,
r/AI_Agents; **Hacker News**; X. This is **methodology for the five Q5 conversations**, not a finding
about people: it says where to find five practitioners, and it says that **the largest of those
venues cannot be read by our tooling.**

### R14 — Stack Overflow is not where this happens, and that is itself a datum

Five searches returned almost nothing on topic. The two relevant hits are worth their view counts:

- *[How to reuse GitHub Copilot Custom Instructions across all projects](https://stackoverflow.com/questions/79602341/how-to-reuse-github-copilot-custom-instructions-across-all-projects)* — 4 votes, 2 answers, **3,775 views**
- *[Is there any support like agents.md or claude.md in antigravity?](https://stackoverflow.com/questions/79834343/is-there-any-support-like-agents-md-or-claude-md-in-antigravity)* — **2,618 views**

Views are the weakest weighting in this document, and both questions are *the reuse question*. Filed
as corroboration of R3 at low confidence.

---

## 3. What moved, row by row

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

## 4. What this hands to the audit — proposals, not edits

Recorded here so step 4 can put them to the owner. **Nothing below has been applied, and no file
outside this folder has been changed.**

1. **A correction to `3-pain/user-pain.md`.** Finding 4's *0 results* was measured on a frozen
   product's tracker with a bug-shaped query. The reassembly friction is filed on live trackers as
   feature requests (R3). The *method* section's claim that reassembly is invisible **by
   construction** should become: invisible to a bug search, visible to a feature-request search.
2. **A correction to `user-pain.md` finding 1's superlative**, carried over from
   [`inventory.md`](inventory.md) OBS-4 and now much larger: 182 is not the loudest anywhere. In the
   combined evidence base the loudest is **6,592**, and it is about multi-target support.
3. **A challenge to `CLAUDE.md` §2's *"nothing does this today"*** (R8). The item-level half of our
   thesis is shipped by several open-source tools with 400–4,500 stars. The set-level half — resolve
   a named set, check it, produce an archive with instructions for the receiving machine — appears
   not to be. The sentence needs narrowing, and `1-landscape/comparison.md` difference 1 needs a
   dated note that it surveyed funded vendors.
4. **A challenge to §5's *reasoning*** (R8), not necessarily its decision: the market no longer only
   converges on measured trust at the vendor tier — free tools ship trust scores at the practitioner
   tier. *We choose not to score* is a different argument from *nobody can score but the big vendors*.
5. **A new risk to §11's public library** (R6). We plan to ship a curated shelf of other people's
   skills. In a scan of 3,984 skills from two registries, 13.4% had critical security issues.
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

## 5. What this collection cannot do

It read the public record harder than anyone had read it. It did not ask anybody anything.

**Q5 is not closed and this document does not pretend to close it.** Every row above is still
someone typing in public, self-selected for having a complaint or an opinion. The rows that need a
person — *why would you adopt this*, *what does the first minute feel like*, *is the loud pain and
the quiet pain the same person*, *has anyone wanted a previous project back* — are exactly the rows
that did not move, and the five conversations remain the instrument. What changed is that
[`interview-guide.md`](interview-guide.md) can now be written against **evidence rather than
guesses**: it knows to ask about symlinks, about how many agents someone keeps, about the 20-to-30
threshold, and about whether they believe any of their own material is doing anything.
