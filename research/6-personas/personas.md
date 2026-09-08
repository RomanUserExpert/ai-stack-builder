# Personas — three, one primary

> **PROVISIONAL.** Written 2026-09-08, stage 6 step 3, from
> [`inventory.md`](inventory.md) (the register and the axes),
> [`re-research.md`](re-research.md) (four instruments on the public record) and
> [`agent-setup-interview.md`](agent-setup-interview.md) (**interview 1 of 5**). The label lifts on
> one event and one only: **the five practitioner conversations Q5 names**, run against
> [`interview-guide.md`](interview-guide.md) and filed here as source documents. Four are still owed,
> and the guide asks that **two of them be people who have never filed an issue in public** — see the
> bias in *What these portraits are drawn from*, below.

**The evidence base, in one paragraph.** Two issue trackers read in stage 3 (182 ranked records);
three more read in stage 6 — `anthropics/claude-code` (89,923 issues), `openai/codex` (26,451),
`google-gemini/gemini-cli` (14,163); **1,762 Hacker News comments** downloaded from eight threads and
read in full; Stack Overflow; a GitHub repository search; about 140 captured frames of other people's
products; and **one 30-minute conversation with one practitioner.** That is everything. Reddit, named
across community surveys as where this population actually talks, **blocks our crawler and is missing
entirely** ([`re-research.md`](re-research.md) R13).

**Three marks, per [`research.md`](../research.md), *The three marks*.** **`✓`** another person can
re-run the instrument and get the same answer · **`*`** a practitioner said it in an interview, from
memory, about their own work — **n = 1** everywhere in this file · **`[?]`** unknown, stated as a
hypothesis and repeated in *Hypotheses* at the end. **A `*` never becomes a `✓` by repetition**, and
**a re-runnable query proves that something was *said*, not that it is *true*** (rule 5).

**Why there are no names, ages, photographs or job titles.** The plan names the trap this stage falls
into ([`README.md`](README.md), *What it is not*): a persona invented from `CLAUDE.md` §3 and then
cited back at it as evidence. §3's *design engineers and AI engineers, 25+, visually literate, living
in Linear, Vercel, Raycast, Figma* is **the owner's assertion, written before a single user was
observed** — it is A-4 and A-5 in the register and it is under test, not established. So each persona
below is named by **what it does**, and the passport is left blank because we have nothing honest to
put in it. `[?]`

---

## The three, and the axes that separate them

Built on **X1** (does anyone else open this material) and **X2** (how many agent targets it must
serve), with **X4** (author or consumer) producing the third — [`inventory.md`](inventory.md) §D.

| | **P1 — The keeper who runs several agents** | **P2 — The receiver** | **P3 — The empty-handed** |
|---|---|---|---|
| **X1** solo ↔ handed over | Solo, until the day it is not | **Receives somebody else's** | Solo, and has nothing yet |
| **X2** one host ↔ several | **Two to four, kept in sync by hand** | Usually a different one from the author's | `[?]` |
| **X4** author ↔ consumer | **Author** | Author elsewhere, consumer here | **Consumer** |
| Standing | **`✓` + `*`, and primary** | **`✓` at population, `*` for the story** | **Mostly `[?]` — the persona the spec already ships for and nobody has met** |

---

# P1 · The keeper who runs several agents — **PRIMARY**

## 1. Context — who, and what situation they arrive from

They did not set out to build a library. **They copied one file into a second project, then a third,
and at the fourth they made a repository.** `*` [interview, Q4](agent-setup-interview.md) — *"the
origin is not 'I designed a system.' The origin is **'I got tired of copy-pasting one file.'**"*

Fourteen months later it holds **20 to 40 items** across skills, instruction files, MCP configs and
scripts. `✓` [claude-code #28729](https://github.com/anthropics/claude-code/issues/28729), 151
reactions — *"once you get to **20-30+ skills**… it becomes difficult to manage"* · `*`
[interview, Q3](agent-setup-interview.md) — *"call it 40-something files"*, ~6k lines. **What the `✓`
carries is that a filer wrote that and 151 people reacted to the request around it**, not that 20–30
is a population figure (rule 5) — [`inventory.md`](inventory.md) NK-2.

**They arrive at our product from one of three situations, and only three, because those are the only
three anyone has described:** copying something out of the collection into a new project; adding a
rule immediately after an agent did something annoying; or hunting for something they know they wrote
and cannot find. `*` [interview, Q19](agent-setup-interview.md) — *"I basically never go in there to
read or review. **There's no reason to, nothing prompts it, so it doesn't happen.**"*

**They arrive irritated more often than not**, because the second of those three modes is an edit
written straight after a failure. `*` [interview, Q19](agent-setup-interview.md) — *"most edits are
written while irritated, which is probably visible in the tone of some of them."* Whether this holds
for anyone else is **`[?]` → H1**.

### Environment — the block this repository added

- **Two to four agents installed, two of them used on any given day.** `✓` [`re-research.md`](re-research.md) R1–R2 — the demand for one source across agents is the loudest thing in the whole evidence base, [#6235](https://github.com/anthropics/claude-code/issues/6235) at **6,592 reactions**; six practitioners describe their own multi-tool setups in public; **25 HN comments** are about symlinking one source into several formats. The **per-person count** of two-to-four is seven people's self-description, so `*` on the number and `✓` on the pattern — NK-5.
- **The material lives in a git repository they own**, symlinked into `~/.claude/` and the other places each agent expects. `*` [interview, Q3](agent-setup-interview.md) · `✓` that people care intensely where it sits ([#1455](https://github.com/anthropics/claude-code/issues/1455), XDG, **446 reactions**) and that a filer asked for **a git repo as the source of truth** ([#28729](https://github.com/anthropics/claude-code/issues/28729)) — **which is evidence that it is not yet how that person works** — NK-6.
- **Three machines or more, counting containers**, and the environments are exactly the ones the instructions did not assume — WSL, dev containers, Remote-SSH, Docker, JetBrains. `✓` OBS-6, with reaction counts · `*` [interview, Q5](agent-setup-interview.md).
- **Nothing is public.** `✓` R10 — **0 of 1,762** HN comments mention a portfolio, and `portfolio in:title` in the audience's own tracker returns two unrelated issues.

## 2. Jobs — what they are trying to do

- **Get the same rules to hold across every agent they use, without maintaining N copies by hand.** `✓` [#6235](https://github.com/anthropics/claude-code/issues/6235) 6,592 · [#20697](https://github.com/anthropics/claude-code/issues/20697) 161 — *"users have to add the same skill twice. **Current workaround: manually copy skills to both locations.**"* · [codex #17401](https://github.com/openai/codex/issues/17401) 21 — *"no modular reuse across projects. A developer working across **10+ repos**…"* **This is the loudest job in the evidence base and our agent-target selector already aims at it** (`CLAUDE.md` §6).
- **Start a new project without spending the same forty minutes again.** `*` [interview, Q6, Q9](agent-setup-interview.md) — thirty-five of the first sixty minutes went on the agent side, *"and I usually round that down to 'ten minutes, it's just a copy'"* · `✓` the friction is filed, as a feature request rather than a bug: [claude-code #9444](https://github.com/anthropics/claude-code/issues/9444), 48 reactions — *"each plugin must duplicate these resources… maintenance burden… **copies can drift out of sync**"* — [`re-research.md`](re-research.md) R3.
- **Stop the copies from diverging.** `✓` #9444 again · `*` [interview, Q10](agent-setup-interview.md) — the same fix made in one project and not the other two, found six weeks later by a client, **three hours of debugging a bug he had already fixed elsewhere.** This is the job `CLAUDE.md` §5's live link exists to do — NK-14.
- **Reuse something they already built, without dragging its old project with it.** `*` [interview, Q8](agent-setup-interview.md) — the eval harness he could not extract because it was *"welded to that project's data model"*, so he wrote a worse one in an hour and never fixed it. **One person, and the only evidence this question has ever had** — NK-8, **`[?]` at population → H2**.
- **Delete half of it with confidence.** `*` [interview, Q18, Q20](agent-setup-interview.md) — *"deleting feels riskier than keeping… so the folder only grows, which is a bad property for a thing whose job is to be precise."*

## 3. Pains — from trackers, forums and one conversation

- **It lands on a fresh machine and quietly does not run.** `✓` [mcp/servers #64](https://github.com/modelcontextprotocol/servers/issues/64) — *MCP Servers Don't Work with NVM*, **182 reactions, 91 comments**, over a top-of-tracker made of `npx` failures, processes dying at startup, timezones and Windows path casing — [`user-pain.md`](../3-pain/user-pain.md) finding 1. `*` [interview, Q11](agent-setup-interview.md) — a devcontainer on Node 18 against a server needing 20+: *"the failure mode is that the agent just doesn't have those tools and carries on without them, cheerfully."* **Detection took 25 minutes; the fix took two.**
- **The failure does not announce itself.** `*` [interview, Q11](agent-setup-interview.md) — *"broken config doesn't announce itself, **it degrades quietly**"*, and *"**one in three** fresh environments has something silently not loading"* (a recollection, not a measurement — rule 3). `✓` the same shape, filed: [codex #13386](https://github.com/openai/codex/issues/13386) — `AGENTS.md` **silently truncated at 32 KB**, *"with no warning anywhere"* · [claude-code #9716](https://github.com/anthropics/claude-code/issues/9716), 75 reactions — skills present and not noticed.
- **Two things claim the same slot and the first one silently wins.** `✓` [mcp/servers #1219](https://github.com/modelcontextprotocol/servers/issues/1219), 13 reactions — *"the chat always chooses the first one specified in order of `mcp.json`"* — **our own collision thesis, sighted in the wild, in the exact file we generate.** Quieter than the environmental pain by a factor of fourteen, and that ratio is the honest weighting — OBS-16, [`user-pain.md`](../3-pain/user-pain.md) finding 2.
- **Env keys and secrets.** `✓` and heavier than stage 3 found: [#32733](https://github.com/anthropics/claude-code/issues/32733) 192 · [#401](https://github.com/anthropics/claude-code/issues/401) 54 — *"Claude loads my project's `.env` into its bash environment"* · [#29910](https://github.com/anthropics/claude-code/issues/29910) 45 · [continue #1729](https://github.com/continuedev/continue/issues/1729) 32 — *"storing api keys in plain text"* · [mcp/servers #1018](https://github.com/modelcontextprotocol/servers/issues/1018) 23 · [#754](https://github.com/modelcontextprotocol/servers/issues/754) 22 — R6, OBS-18.
- **Being silently overruled by their own tooling.** `*` [interview, Q13](agent-setup-interview.md) — a formatting rule left over from another project reformatted a codebase as a side effect, **1,100 lines of noise pushed into a colleague's review branch.** `✓` the same class: [#20412](https://github.com/anthropics/claude-code/issues/20412), 142 reactions — MCP servers *"silently synced… without any opt-in, notification, or consent."*
- **The deepest one: not knowing whether any of it does anything.** `✓` across the threads — *"mostly useless… **50/50 or less** that Claude.md even reads/uses this file"* ([saberience](https://news.ycombinator.com/item?id=46106423)) · *"Claude rarely actually reads the other documentation files I point it to"* ([sothatsit](https://news.ycombinator.com/item?id=46102180)) · an entire story titled *[I am morally opposed to updating my Claude.md](https://news.ycombinator.com/item?id=49376287)* · *"**Blackbox oracles make bad workflows, and tend to produce a whole lot of cargo culting**"* ([bandrami](https://news.ycombinator.com/item?id=46820441)). `*` [interview, Q16–Q17](agent-setup-interview.md) — *"maybe **half of it**, if you want the real answer… **I've never A/B'd anything.**"* — R7, NK-11.

## 4. Trust triggers — what convinces, what repels

**Convinces:**

- **A usage fact about their own material — and this is the one thing a practitioner asked for in our own words, unprompted.** `*` [interview, Q20](agent-setup-interview.md), asked with our vocabulary deliberately forbidden ([`interview-guide.md`](interview-guide.md) §4): *"**Usage data, first.** Just: this file was loaded in 40 sessions, this one in 2, this one never. **That alone would let me delete half of it with confidence.**"* Then he extended it past our spec: **last actually useful**, not created-date; and counted **per session** — NK-12. **One person, and the strongest form a `*` can take.**
- **A number that is also a link to the list behind it.** `M` OBS-29 — VS Code's Workspace Trust: *"95 workspace settings are not applied"*, *"10 extensions are disabled"*, both hyperlinked. It beats Figma's bare *423 instances* on exactly the axis Figma leaves open. **Evidence of what a good product chose, not that it works on this person** — `[?]` → H3.
- **A consequence named in the present tense before the irreversible step.** `M` OBS-31 — Vercel's env drawer: *"You can't reveal this value after saving"*, and its optional note placeheld *"Where to rotate, or who to contact."* This is the register `CLAUDE.md` §6 already adopted for the unclean-export confirmation.

**Repels:**

- **A score we invented.** `V` OBS-33 — the market converged on *measured* trust (Tessl: composite 93, uplift 1.40×; Smithery: a score out of 100) and we can run nothing, so any number we produced would be decoration — `CLAUDE.md` §5. **And the argument has weakened, not the decision:** free tools at the practitioner tier now ship trust scores too (`HarnessKit` *"scores trust 0–100"*, by its own README) — [`re-research.md`](re-research.md) R8. **Whether a score would repel *this person* is `[?]` → H4.**
- **A green tick that was not earned.** The reason `CLAUDE.md` §6 gives *Skipped* its own neutral glyph. Directly downstream of the doubt in Pains: someone who suspects half his material does nothing will read an unearned tick as proof the checker is decoration. `*` + `✓` R7 — the inference is ours, `R`.
- **A check that answers a question they did not ask.** `*` [interview, Q25](agent-setup-interview.md), the genie question, asked before the product was ever described: *"**Show me what actually loaded and what actually mattered.** Per session: these files were read, this rule fired here, **these six things were present and had no observable effect.** I don't need it to fix anything, **I need to see it**."* **Our validation pass answers *does this set cohere*. He asked for *what ran*. Those are not the same product**, and it is now **Q12** in the register — NK-23.
- **Being reported on, and a hosted layer that can vanish.** `✓` [continue #567](https://github.com/continuedev/continue/issues/567) — a telemetry opt-out request, 2 reactions, the only one of its kind in 182 records (OBS-24) · `E` OBS-25 — Continue's hosted half was switched off and *"all user data has been deleted"*, to this exact audience · `✓` [allknowingfrog](https://news.ycombinator.com/item?id=48184129) — *"**I don't track Claude resources in our repos.** If something better comes along, I'm better off"*, a refusal to commit the material at all, on lock-in grounds.

## 5. Quote — the mood

> *"I have a **~200 line file of style rules that I copy and paste between all my projects**
> (**There's got to be a better way to manage files like that!**) but **I can never quite tell if
> it's helping anything**."*
>
> — [eternityforest, Hacker News, 2026-06-22](https://news.ycombinator.com/item?id=48638003) `✓`

**Both halves of this persona are in one sentence**: the reassembly that built the collection, and
the doubt that it is worth anything. **It is the whole of P1.**

## What this card is allowed to settle

The Run stage list and the verdict each stage carries (`CLAUDE.md` §6, §8) · the copy register for a
Problem and for a Note (§6) · **what an item card carries — usage facts, and specifically *last
actually useful* rather than *last exported*** (§5) · the handover stages before Export (§6) · the
agent target selector's prominence (§6). **It may not settle** anything about the Library screen at
scale, or about positioning, because both rest on `[?]` rows.

---

# P2 · The receiver — secondary

**The person on the other end of the archive.** They are a persona rather than a moment because the
behaviour is different in kind: they did not write this material, they cannot tell which parts are
load-bearing, and **they do not know what is missing.**

## 1. Context

They are handed a repository, a config or a project and expected to work in it. `✓` [#6235](https://github.com/anthropics/claude-code/issues/6235), **6,592 reactions** — the stated motive of the loudest request in the evidence base is *"collaborating with other developers **who aren't using Claude Code**"* · [#10238](https://github.com/anthropics/claude-code/issues/10238) 168 — *"we have started using and developing skills **with my team**"* · [#28729](https://github.com/anthropics/claude-code/issues/28729) 151 — org skills, *"multiple contributors"* · [#48322](https://github.com/anthropics/claude-code/issues/48322) 53 — team/enterprise shared routines — [`re-research.md`](re-research.md) R12, NK-7.

**They usually run a different agent from the person who wrote it.** `✓` — that is what #6235 is
about, and the same family spans three vendors' trackers (R1).

**Environment.** `[?]` almost entirely → **H5**. We know they exist and we know one story about one of
them. We do not know what they have installed, what they are allowed to install, or whether they can
even ask the author.

## 2. Jobs

- **Get the thing to run, today, without becoming an expert in somebody else's setup.** `✓` #6235's motive · `*` [interview, Q21](agent-setup-interview.md).
- **Find out what is actually load-bearing.** `*` [interview, Q22](agent-setup-interview.md) — what he had to explain, twice, on a call: *"which files are load-bearing and which are aspirational. **Which rules are real constraints from the client versus my personal taste.**"* **None of that is written down anywhere**, so the explanation is a twenty-minute conversation with a human.

## 3. Pains

- **The handover fails silently and the receiver does not know it failed.** `*` [interview, Q21](agent-setup-interview.md) — a contractor got the repo including the agent config: *"paths broken, one server not starting, and **he assumed that was normal and worked around it for two days without mentioning it.**"* Found out on a call, from a workflow that made no sense. *"That was the moment I understood the config had become **tribal knowledge rather than a setup**."* **This is second-hand and n = 1** — the contractor was never asked.
- **Half of what makes the setup work was never written down at all.** `*` [interview, Q26](agent-setup-interview.md) — *"roughly **half** of what makes a project go well is stuff I've never written down because writing it down felt too obvious. Then a contractor joins and **none of it transfers**."* **This bounds the ceiling of our entire product** — we validate the written part — and it is now **Q11** in the register — NK-22.
- **A rule from the author's world colliding with the receiver's.** `*` [interview, Q26](agent-setup-interview.md) — *"my CLAUDE.md says one thing, the client's linter says another, and **there's no precedence anywhere**; it's resolved by whichever I remember at the time."* `CLAUDE.md` §6 models conflicts **between our items** and has nowhere to put this one — **Q10** in the register, NK-21.

## 4. Trust triggers

- **Convinces: being told what the machine still has to do, before anything is written.** This is exactly what `CLAUDE.md` §6's handover stages and `SETUP.md`-for-an-agent were designed for, and the benchmark found **no product in the survey has such a surface** — `V` OBS-20, B4, *nobody above 4*. **Whether it works has never been tested on a receiving agent or a receiving person: `[?]` → H6, and it is NK-13, the one blank row we can fill ourselves.**
- **Convinces: naming the second-order consequence the reader would not have thought of.** `M` OBS-30 — Notion's publish dialog: *"anyone with the link can view this page's content **and see contributor names**."*
- **Repels: a set that appears without consent.** `✓` [#20412](https://github.com/anthropics/claude-code/issues/20412), 142 reactions — servers *"silently synced… without any opt-in, notification, or consent"*, producing duplicates and OOM kills.
- **Repels: severity that lies.** `E` OBS-32 — the nearest dead competitor shipped `ConfigValidationError { fatal: boolean }` and filed **a block that failed to resolve as `fatal: false`**, so a missing dependency degraded the result quietly. `CLAUDE.md` §6 chose three severities and *nothing blocks* partly against this.

## 5. Quote

> *"Codex, Amp, Cursor, and others are starting to standardize around AGENTS.md… By contrast,
> CLAUDE.md feels too specific to Claude Code. **It doesn't work as well when collaborating with
> other developers who aren't using Claude Code.**"*
>
> — [claude-code #6235](https://github.com/anthropics/claude-code/issues/6235), **6,592 reactions,
> 389 comments**, filed 2025-08-21 `✓`

**The most-reacted issue anywhere in this repository's evidence base is about the receiver.** That is
the single strongest argument for keeping this persona and not folding it into P1.

## What this card is allowed to settle

What `SETUP.md` states and in what order (`CLAUDE.md` §6) · which stages sit before Export in Run and
what they disclose (§6, §8) · the wording of a Note about a missing env key. **It may not settle**
anything about how the receiver *feels*, because **no receiver has ever been asked** — every line
above is either a filed request or the author's account of somebody else.

---

# P3 · The empty-handed — secondary, and **mostly hypothesis**

> **Read this card as a warning, not as a portrait.** `CLAUDE.md` §8 and §11 already ship two
> surfaces for this person — the **`Public library` scope switch** and the **example project** — and
> **not one person in this shape has been observed anywhere in the phase.** The card exists so the
> gap has a face and a name, which is the whole point of the stage.

## 1. Context

Someone with no collection of their own, or a collection so young it does nothing, opening the
product for the first time. **`[?]` → H7.** What exists instead of evidence:

- **`V`** A whole tool category exists to install other people's material — `xingkongliang/skills-manager` 4,526★, `MoizIbnYousaf/ai-agent-skills` *"universal skill installer and package manager"* 1,138★, `luongnv89/asm` 915★ — [`re-research.md`](re-research.md) R8. **Their existence and their stars are `✓`; what they do is their own README and we ran none of them** (rule 5).
- **`V`** Catalogs report skills at six and seven figures, and one vendor's own report says *"discovery is no longer the bottleneck. **Judgment is.**"* — R9, **published by a hard competitor that sells curation**.
- **`V`** OBS-12 — every catalog in the survey solves cold start with **curation and volume**, and not one makes a user's own accumulated material better.

**Nothing in that list is a person.** It is what tools and vendors bet.

## 2. Jobs

**All `[?]` → H8.** The plausible ones, written as hypotheses rather than facts: *get something
working without composing it myself*; *see what good looks like before writing my own*. **No
instrument in this repository has established either**, and `CLAUDE.md` §11's own reasoning for the
shelf — *"an empty library kills the product, because there is nothing to validate"* — is the owner's
assertion A-8, standing `[?]`.

## 3. Pains

- **`✓` published, not verified by us — taking other people's material is measurably risky.** [Snyk's ToxicSkills study](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/), 3,984 skills scanned from two public registries on 2026-02-05: **13.4% with critical security issues**, 1,467 with at least one flaw, **76 confirmed malicious payloads**, and *"the barrier to publishing? A `SKILL.md` and a GitHub account that's one week old. **No code signing. No security review. No sandbox by default.**"* We did not re-run the scan and cannot; Snyk sells security tooling; its own post does not reconcile 36% with 36.82%. **The order of magnitude is what this carries, and it is enough:** §11's *"checked sources"* currently means checked for **provenance** and now has to mean checked for **content** — R6, and proposal 5 in [`re-research.md`](re-research.md) §4.
- **`[?]` → H9** — everything else. Whether a curated shelf reads as generous or as filler; whether six green ticks on a first check teach anything; whether an example project labelled *example* is opened at all.

## 4. Trust triggers

- **Convinces, on the best first-run capture in the phase:** `M` OBS-36 — a brand-new Linear workspace opens on the Issues list **already holding four real issues**, with real IDs, statuses and dates, deletable, so the onboarding checklist *is* the data model exercised on itself. This is the shape `CLAUDE.md` §11's example project already copies.
- **Convinces, presumably: provenance.** `CLAUDE.md` §5 requires every public item to show its origin and a pinned `ref`, which is what keeps a shelf with no server behind it honest — *this is the version we checked*, not *this is current*. `M` OBS-34 — Terraform, Figma, Raycast and Backstage all attach an identity to a shared artefact. **That any of it convinces this person is `[?]` → H10.**
- **Repels: emptiness that is also a dead end.** `M` OBS-37 — Linear's three registers of emptiness, and the rule between them: verbosity scales with the chance the reader does not know what the object is. `M` OBS-38 — a control that cannot act is not shown, three products against one.

## 5. Quote

**There is none, and the absence is the finding.** `[?]`

Every quote in this file comes from a tracker, a thread or the interview, under the rule that a quote
carries a URL or it is not a quote ([`README.md`](README.md), *The circular quote*). **Nobody in this
shape has said anything anywhere we looked** — 1,762 HN comments, five trackers, one conversation.
**Writing a plausible sentence here and attributing it to a plausible person is exactly the failure
this stage was re-opened to prevent.** So the box stays empty until someone fills it — the guide's P5
recruit, *someone who does not keep this material at all*
([`interview-guide.md`](interview-guide.md) §2), who has not been found.

## What this card is allowed to settle

**Almost nothing, and that is the point.** It may not be cited for the scope switch, the shelf's size,
or the example project's composition — those are `CLAUDE.md` decisions taken on reasoning, and this
card adds no evidence to them. **It settles exactly one thing:** that the shelf needs a **stated
content-review standard** before it ships, because the one hard number attached to this persona is
13.4%.

---

# Why P1 is primary

**The plan expected a contest** between the person whose pain is *sighted* — an archive that lands
and does not run — and the *collector* `CLAUDE.md` §3 is positioned for
([`README.md`](README.md), step 3). **The contest did not happen, for a reason worth more than the
answer:** the one practitioner asked says they are the same person.

> *"**Already had the collection, and that's the point.** When it was one file I knew what was in it.
> At forty files with overlapping instructions I have no working model of what's active on a given
> run. **The collection created the problem.**"* — [interview, Q15](agent-setup-interview.md) `*`

That is X6 in [`inventory.md`](inventory.md) §D, it is **one sentence from one person**, and it is the
only causal claim anybody has made. If it holds, the collector *is* the breaker, and P1 is not a
choice between two candidates but the merge of them.

**Four reasons P1 is primary, in descending strength:**

1. **It is the only persona with `✓` and `*` agreeing from independent instruments** on its jobs and its pains — the multi-target job at 6,592, the drift job at 48, the environmental pain at 182, the collision at 13, the doubt across eight threads and one interview.
2. **It is where the value was already found to concentrate.** The benchmark re-weighted the four flows by pain and put the value in **B3 (check)** and **B4 (produce)** — [`benchmark.md`](../4-benchmark/benchmark.md), *finalisation*. Those are P1's two moments.
3. **It carries the higher risk and has the fewer levers**, which is the lesson's own rule for choosing. If we are wrong about P1, Run and the item card are both wrong, and they are the product. If we are wrong about P3, one scope switch and one seeded project are wrong.
4. **P2's job is a *consequence* of P1's set, not an independent product.** The receiver's pain begins with an archive P1 produced. Designing for P2 without P1 has nothing to design against.

## What would overturn this choice — stated in advance, so it can happen

- **Four more Q15 answers that separate the collection from the breakage.** If practitioners two through five say the breakage came from a single server on a new laptop and had nothing to do with the size of their collection, **X6 collapses**, P1 splits back into two personas, and the primary becomes whichever of them the remaining evidence favours — [`interview-guide.md`](interview-guide.md) Q15.
- **An answer to Q5 that says adoption is driven by getting *material*, not by keeping one's own.** Then **P3 becomes primary**, the Library scope switch becomes the centre of the product rather than a switch on a browse screen, and Run's prominence in `CLAUDE.md` §8 is wrong — register Q5 and Q7, [`research-plan.md`](../research-plan.md).
- **A strong answer to guide Q25 that repeats the observability ask.** If four more practitioners answer the genie question with *show me what ran* rather than *check that it holds together*, the primary persona survives but **`CLAUDE.md` §2's core-value sentence does not** — that is **Q12**, and it is the sharpest question this stage produced.

## What these portraits are drawn from — the bias, printed on the page

- **Every public source is a person who chose to write in public.** The whole corpus is filers and commenters — X5, NK-16. The one practitioner interviewed is *also* a filer, so n = 1 cannot correct it. **The guide requires two of the five to have never filed anything in public** ([`interview-guide.md`](interview-guide.md) §2); that has not happened yet.
- **Reddit is missing**, and it is named across community surveys as the largest venue for this population — R13.
- **Every number spoken in the interview is a recollection** — *forty-something files*, *one in three fresh environments*, *about half of it* — and the respondent flags his own unreliability twice unprompted. Rule 3.
- **Roughly half of every card above is `[?]`, and all of the adoption story is.** That was predicted in the plan before any of it was written ([`README.md`](README.md), *The honest problem*), and it turned out to be accurate.

---

# Hypotheses

Every `[?]` above, restated in the plan's required form — *we assume X; we would check it by Y* —
so that none of it can be read as a finding.

| # | We assume | We would check it by | Which decision it holds up |
|---|---|---|---|
| **H1** | P1 arrives **irritated**, and the tone of a failure message therefore matters more than its completeness | Guide Q19, four more times, listening for the emotional register rather than the three modes — NK-17 | The copy register for a Problem (`CLAUDE.md` §6) |
| **H2** | People want a **previous project back**, and are stopped by entanglement rather than by not finding it | Guide Q8, four more times — NK-8 | Duplicate-a-project, and item granularity (§5, §8) |
| **H3** | A **count that links to its list** convinces this audience, as it does in VS Code and Figma | The five conversations, shown two variants of the same finding; or first use of a seeded library — NK-12 | *Used in 3 projects* on an item card (§5) |
| **H4** | A **score would repel** rather than reassure, now that free tools at this tier ship one | Guide Q20 open, four more times, plus asking directly about `asm` and `HarnessKit` if the respondent knows them — NK-12, R8 | §5's *usage facts, never a score* |
| **H5** | The **receiver** has a different agent and cannot easily ask the author | Ask a receiver. **Nobody has**, and the guide does not currently recruit one — NK-7 | What `SETUP.md` assumes about its reader (§6) |
| **H6** | A **receiving agent performs the setup correctly from `SETUP.md` alone** | **Us, in an afternoon** — compose a set by hand, write the `SETUP.md` §6 describes, hand the archive to a fresh Claude Code, Cursor and Codex, record what each actually does — NK-13 | The spec's most load-bearing bet (§6, §8) |
| **H7** | The **empty-handed persona exists** in numbers that justify shipping a shelf | The guide's P5 recruit — someone who does not keep this material at all — not yet found — NK-9 | The `Public library` scope switch (§8, §11) |
| **H8** | Their job is *get something working without composing it myself* | The same P5 conversation, asked as a situation, never as a pitch | Whether the shelf is a browse surface or a starter kit |
| **H9** | A first check showing **one Problem and one Note** teaches the product better than six green ticks | First use of the seeded example project, watched — G5 in [`research.md`](../research.md) | The example project's composition (§11) |
| **H10** | **Provenance and a pinned `ref`** are what make a read-only shelf trustworthy without a server | The same first use; and whether anyone clicks through to an origin — NK-19 | Public item cards (§5), and the licence field that model lacks |
| **H11** | `CLAUDE.md` §3's audience — **25+, visually literate, living in Linear, Vercel, Raycast, Figma** — describes these people | **No instrument in this repository can reach it**, and none has. It is A-4 and A-5, and it stays a hypothesis through the design system unless someone asks | Visual direction, and who the craft bar is set for |

---

# What this hands forward

1. **To the audit (step 4).** The dangerous list is already visible: **every claim carrying only `*` bears on a design decision and stands on one person** — and in this file that includes the whole of P1's trust-trigger block and the whole of P2's pain block.
2. **To the register.** Nothing new. P1's overturning conditions are Q5, Q7 and Q12; P2's pains are Q10 and Q11; P3 is Q9's *which specified features close no evidenced job* with two candidates already named.
3. **To the owner, as work.** **H6 is ours to close** and needs an afternoon. It is the only hypothesis in the table that does not need another person.
4. **Not to `CLAUDE.md`.** Nothing here is applied. Stage 6 audits; the owner edits. If a persona refutes a surface, that is a register entry and not an edit — [`README.md`](README.md), definition of done.
