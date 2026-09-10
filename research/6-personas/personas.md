# Personas — three, one primary

> **There is a page.** [`personas.html`](personas.html) renders this file and
> [`../7-jobs-to-be-done/jtbd.md`](../7-jobs-to-be-done/jtbd.md) together — cards, hierarchy, matrix,
> marks visible — and it is linked from the research page. **This markdown is the source; the page is
> the read.**

> **PROVISIONAL.** Written 2026-09-08, stage 6 step 3, from
> [`inventory.md`](inventory.md) (the register and the axes),
> [`re-research.md`](re-research.md) (four instruments on the public record) and
> [`interviews.md` interview 1](interviews.md#part-2-interview-1-of-5) (**interview 1 of 5**), and — since
> 2026-09-08 — [`re-research.md` round 2](re-research.md#round-2-counting-not-asking), a second targeted collection run against the
> five questions in [`personas-and-jobs-critique.md`](../personas-and-jobs-critique.md). **Five marks
> changed and P3 changed character; each change is recorded in [`research.md`](../research.md) §7,
> *Research justification*.** **And on 2026-09-09 the audit itself was applied**: the eleven invented
> claims [`personas-and-jobs-critique.md`](../personas-and-jobs-critique.md) found in this file are
> corrected in place, each marked with its ID. **Every correction weakened a claim; none reversed a
> finding, and no persona changed.** The label lifts on
> one event and one only: **the five practitioner conversations Q5 names**, run against
> [`interviews.md` the guide](interviews.md#part-1-the-guide) and filed here as source documents. **Four are still owed
> and, as of 2026-09-09, unavailable — so the label does not lift, and nothing on these cards is
> promoted because the event will not arrive.** What is reachable without a person is
> [`re-research.md` round 3](re-research.md#round-3-five-questions-that-need-no-interview); it reaches the receiver's column and the shelf's premise in
> part, and it reaches nothing about motive or feeling. Four were owed,
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
| **X2** one host ↔ several | **Two to four, counted in public trees** | `[?]` — **one filed motive says so**; no instrument measured how often (P-06) | `[?]` |
| **X4** author ↔ consumer | **Author** | Author elsewhere, consumer here | **Consumer** |
| Standing | **`✓` + `*`, and primary** | **`✓` at population** — six independent senders and three issue threads; **`*` and second-hand for the receiving end** | **`[?]` that the persona exists; `✓` that the nearest observed people are sceptical of the shelf's premise.** Changed 2026-09-08 |

---

# P1 · The keeper who runs several agents — **PRIMARY**

## 1. Context — who, and what situation they arrive from

They did not set out to build a library. **They copied one file into a second project, then a third,
and at the fourth they made a repository.** `*` [interview, Q4](interviews.md#part-2-interview-1-of-5) — *"the
origin is not 'I designed a system.' The origin is **'I got tired of copy-pasting one file.'**"*

Fourteen months later it holds **tens of items, not hundreds** — the counted band is **11 to 48**
across skills, agents, commands, instruction files and MCP configs. **Upgraded to `✓` on 2026-09-08,
and widened.** `✓` **counted, not asked** — four public agent-material repositories read through the
GitHub tree API: 11 items, 25, 47 and 48 ([`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-C, with the counts
and the queries). `✓` [claude-code #28729](https://github.com/anthropics/claude-code/issues/28729),
151 reactions — *"once you get to **20-30+ skills**… it becomes difficult to manage"*, which is one
filer's sentence and carries only that (rule 5) · `*` [interview, Q3](interviews.md#part-2-interview-1-of-5) —
*"call it 40-something files"*, ~6k lines. **This card said *20 to 40* until the count was run; two of
the four repositories exceed 40, so the top of the band was wrong.** Stage 5's **300 stays refuted** —
nothing observed approaches it. **Design for fifty, not for thirty** —
[`inventory.md`](inventory.md) NK-2.

**They arrive at our product from one of three situations, and only three, because those are the only
three anyone has described:** copying something out of the collection into a new project; adding a
rule immediately after an agent did something annoying; or hunting for something they know they wrote
and cannot find. `*` [interview, Q19](interviews.md#part-2-interview-1-of-5) — *"I basically never go in there to
read or review. **There's no reason to, nothing prompts it, so it doesn't happen.**"*

**The second most frequent reason to open the folder is an edit written in irritation.** *Corrected
2026-09-09 (P-13): this read "they arrive irritated more often than not", which reverses the
respondent's own ordering — **copying something out is the most frequent mode**, the irritated edit
is second.* `*` [interview, Q19](interviews.md#part-2-interview-1-of-5) — *"most edits are written while irritated,
which is probably visible in the tone of some of them."* Whether this holds for anyone else is
**`[?]` → H1**, and the copy register for a Problem and a Note (§6) is being tuned to a mood we have
ranked second, not first.

### Environment — the block this repository added

- **Two to four agents installed, two of them used on any given day. `✓` — and as of 2026-09-08 this is counted rather than reported.** Two of four public agent-material repositories configure **four** and **three** distinct tools, read straight from their trees: `.claude/settings.json` beside `packages/devin/config.json`, `packages/copilot/settings.json` and `packages/pi/agent/settings.json`; and `claude/` beside `codex/config.toml.example` and `antigravity/mcp_config.json.example`, with `CLAUDE.md`, `AGENTS.md` and `MULTI-AGENT.md` side by side ([`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-C). `✓` [`re-research.md`](re-research.md) R1–R2 — the demand for one source across agents is the loudest thing in the whole evidence base, [#6235](https://github.com/anthropics/claude-code/issues/6235) at **6,592 reactions**; **25 HN comments** about symlinking one source into several formats. **The per-person count used to be `*`, seven people's self-description; it is now `✓` in two public trees** — NK-5.
- **The material lives in a git repository they own**, symlinked into `~/.claude/` and the other places each agent expects. **`✓` as of 2026-09-08** — the arrangement is visible in the trees themselves and described independently by six people in one thread: `chezmoi` with *"a `.agents/skills/` directory + a symlink"*; *"two source-of-truth git repos (private and public)… syncs to all coding agents `~/.claude/skills/`, `~/.codex/skills`, `~/.pi/agent/skills`"*; *"a separate repo which has to be pulled locally and the skills and agents are sym linked to projects"* ([`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-C). `*` [interview, Q3](interviews.md#part-2-interview-1-of-5) · `✓` that people care intensely where it sits ([#1455](https://github.com/anthropics/claude-code/issues/1455), XDG, **446 reactions**) — NK-6. **The instrument's bias, printed here: this counts only people who publish their setup, and the one practitioner interviewed keeps his private.**
- **Three, if you count containers** — `*` one person, [interview, Q5](interviews.md#part-2-interview-1-of-5); *"or more"* was added by us and is now removed (P-23). The environments are exactly the ones the instructions did not assume — WSL, dev containers, Remote-SSH, Docker, JetBrains — and **`✓` covers only that these hosts appear in the trackers with those reaction counts** (OBS-6), never a per-person machine count, which no instrument has measured.
- **Nothing is public.** `✓` R10 — **0 of 1,762** HN comments mention a portfolio, and `portfolio in:title` in the audience's own tracker returns two unrelated issues.

## 2. Jobs — what they are trying to do

- **Get the same rules to hold across every agent they use, without maintaining N copies by hand.** `✓` [#6235](https://github.com/anthropics/claude-code/issues/6235) 6,592 · [#20697](https://github.com/anthropics/claude-code/issues/20697) 161 — *"users have to add the same skill twice. **Current workaround: manually copy skills to both locations.**"* · [codex #17401](https://github.com/openai/codex/issues/17401) 21 — *"no modular reuse across projects. A developer working across **10+ repos**…"* **This is the loudest job in the evidence base and our agent-target selector already aims at it** (`CLAUDE.md` §6).
- **Start a new project without spending the same forty minutes again.** `*` [interview, Q6, Q9](interviews.md#part-2-interview-1-of-5) — thirty-five of the first sixty minutes went on the agent side, *"and I usually round that down to 'ten minutes, it's just a copy'"* · `✓` the friction is filed, as a feature request rather than a bug: [claude-code #9444](https://github.com/anthropics/claude-code/issues/9444), 48 reactions — *"each plugin must duplicate these resources… maintenance burden… **copies can drift out of sync**"* — [`re-research.md`](re-research.md) R3.
- **Stop the copies from diverging.** `✓` #9444 again · `*` [interview, Q10](interviews.md#part-2-interview-1-of-5) — the same fix made in one project and not the other two, found six weeks later by a client, **three hours of debugging a bug he had already fixed elsewhere.** This is the job `CLAUDE.md` §5's live link exists to do — NK-14.
- **Reuse something they already built, without dragging its old project with it.** `*` [interview, Q8](interviews.md#part-2-interview-1-of-5) — the eval harness he could not extract because it was *"welded to that project's data model"*, so he wrote a worse one in an hour and never fixed it. **One person, and the only evidence this question has ever had** — NK-8, **`[?]` at population → H2**.
- **Delete half of it with confidence.** `*` [interview, Q18, Q20](interviews.md#part-2-interview-1-of-5) — *"deleting feels riskier than keeping… so the folder only grows, which is a bad property for a thing whose job is to be precise."*

## 3. Pains — from trackers, forums and one conversation

- **It lands on a fresh machine and quietly does not run.** `✓` [mcp/servers #64](https://github.com/modelcontextprotocol/servers/issues/64) — *MCP Servers Don't Work with NVM*, **182 reactions, 91 comments**, over a top-of-tracker made of `npx` failures, processes dying at startup, timezones and Windows path casing — [`user-pain.md`](../3-pain/user-pain.md) finding 1. `*` [interview, Q11](interviews.md#part-2-interview-1-of-5) — a devcontainer on Node 18 against a server needing 20+: *"the failure mode is that the agent just doesn't have those tools and carries on without them, cheerfully."* **Detection took 25 minutes; the fix took two.**
- **The failure does not announce itself.** `*` [interview, Q11](interviews.md#part-2-interview-1-of-5) — *"broken config doesn't announce itself, **it degrades quietly**"*, and — `*` [Q12](interviews.md#part-2-interview-1-of-5), **not Q11 as this line used to say** (P-37) — *"**one in three** fresh environments has something silently not loading"* (a recollection, not a measurement — rule 3). `✓` the same shape, filed: [codex #13386](https://github.com/openai/codex/issues/13386) — `AGENTS.md` **silently truncated at 32 KB**, *"with no warning anywhere"* · [claude-code #9716](https://github.com/anthropics/claude-code/issues/9716), 75 reactions — skills present and not noticed.
- **Two things claim the same slot and the first one silently wins.** `✓` [mcp/servers #1219](https://github.com/modelcontextprotocol/servers/issues/1219), 13 reactions — *"the chat always chooses the first one specified in order of `mcp.json`"* — **our own collision thesis, sighted in the wild, in the exact file we generate.** Quieter than the environmental pain by a factor of fourteen, and that ratio is the honest weighting — OBS-16, [`user-pain.md`](../3-pain/user-pain.md) finding 2.
- **Env keys and secrets.** `✓` and heavier than stage 3 found: [#32733](https://github.com/anthropics/claude-code/issues/32733) 192 · [#401](https://github.com/anthropics/claude-code/issues/401) 54 — *"Claude loads my project's `.env` into its bash environment"* · [#29910](https://github.com/anthropics/claude-code/issues/29910) 45 · [continue #1729](https://github.com/continuedev/continue/issues/1729) 32 — *"storing api keys in plain text"* · [mcp/servers #1018](https://github.com/modelcontextprotocol/servers/issues/1018) 23 · [#754](https://github.com/modelcontextprotocol/servers/issues/754) 22 — R6, OBS-18.
- **Being silently overruled by their own tooling.** `*` [interview, Q13](interviews.md#part-2-interview-1-of-5) — a formatting rule left over from another project reformatted a codebase as a side effect, **1,100 lines of noise pushed into a colleague's review branch.** `✓` the same class: [#20412](https://github.com/anthropics/claude-code/issues/20412), 142 reactions — MCP servers *"silently synced… without any opt-in, notification, or consent."*
- **The deepest one: not knowing whether any of it does anything.** `✓` across the threads — *"mostly useless… **50/50 or less** that Claude.md even reads/uses this file"* ([saberience](https://news.ycombinator.com/item?id=46106423)) · *"Claude rarely actually reads the other documentation files I point it to"* ([sothatsit](https://news.ycombinator.com/item?id=46102180)) · an entire story titled *[I am morally opposed to updating my Claude.md](https://news.ycombinator.com/item?id=49376287)* · *"**Blackbox oracles make bad workflows, and tend to produce a whole lot of cargo culting**"* ([bandrami](https://news.ycombinator.com/item?id=46820441)). `*` [interview, Q16–Q17](interviews.md#part-2-interview-1-of-5) — *"maybe **half of it**, if you want the real answer… **I've never A/B'd anything.**"* — R7, NK-11.

## 4. Trust triggers — what convinces, what repels

**Convinces:**

- **A usage fact about their own material — and this is the one thing a practitioner asked for in our own words, unprompted.** `*` [interview, Q20](interviews.md#part-2-interview-1-of-5), asked with our vocabulary deliberately forbidden ([`interviews.md` the guide](interviews.md#part-1-the-guide) §4): *"**Usage data, first.** Just: this file was loaded in 40 sessions, this one in 2, this one never. **That alone would let me delete half of it with confidence.**"* Then he extended it past our spec: **last actually useful**, not created-date; and counted **per session** — NK-12. **One person, and the strongest form a `*` can take.**
- **A number that is also a link to the list behind it.** `M` OBS-29 — VS Code's Workspace Trust: *"95 workspace settings are not applied"*, *"10 extensions are disabled"*, both hyperlinked. It beats Figma's bare *423 instances* on exactly the axis Figma leaves open. **Evidence of what a good product chose, not that it works on this person** — `[?]` → H3.
- **A consequence named in the present tense before the irreversible step.** `M` OBS-31 — Vercel's env drawer: *"You can't reveal this value after saving"*, and its optional note placeheld *"Where to rotate, or who to contact."* This is the register `CLAUDE.md` §6 already adopted for the unclean-export confirmation.

**Repels:**

- **A score we invented.** `V` OBS-33 — the market converged on *measured* trust (Tessl: composite 93, uplift 1.40×; Smithery: a score out of 100) and we can run nothing, so any number we produced would be decoration — `CLAUDE.md` §5. **And the argument has weakened, not the decision:** free tools at the practitioner tier now ship trust scores too (`HarnessKit` *"scores trust 0–100"*, by its own README) — [`re-research.md`](re-research.md) R8. **Whether a score would repel *this person* is `[?]` → H4.**
- **A green tick that was not earned.** The reason `CLAUDE.md` §6 gives *Skipped* its own neutral glyph. Directly downstream of the doubt in Pains: someone who suspects half his material does nothing will read an unearned tick as proof the checker is decoration. `*` + `✓` R7 — the inference is ours, `R`.
- **A check that answers a question they did not ask.** `*` [interview, Q25](interviews.md#part-2-interview-1-of-5), the genie question, asked before the product was ever described: *"**Show me what actually loaded and what actually mattered.** Per session: these files were read, this rule fired here, **these six things were present and had no observable effect.** I don't need it to fix anything, **I need to see it**."* **Our validation pass answers *does this set cohere*. He asked for *what ran*. Those are not the same product**, and it is now **Q12** in the register — NK-23.
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

**Whether they usually run a different agent from the person who wrote it is `[?]`.** *Corrected
2026-09-09 (P-71): this asserted "usually", a frequency no instrument measured, and leaned on R1's
thirteen-issue family — five of which are about session, history, account or subscription sync rather
than instruction files.* **The situation is filed once with a stated motive** — #6235, whose author
says collaborators are not using the same tool — and **its frequency is not known**. The
instruction-file family is eight issues, not thirteen (R1).

**Environment. Half of H5 closed on 2026-09-08; the other half did not.** `✓` **the sending side and
its difficulty**, from six independent voices in one Ask HN thread of 305 points and 274 comments
([`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-B): company-managed skills pushed to every developer by a
**bootstrap script**, with the sender saying *"these are supposed to be portable between agents, and
so **distributing them is currently awkward**"*; skills committed to git *"so complete team leverages
them"*; a **public skill registry with profile-based syncing for the Norwegian Government**; and the
sentence that is this product's thesis written by somebody else —

> *"skills need to be edited across projects and **across team members** in a controlled way.
> **Git is of course required for this but is not enough**."*
> — [mstr32](https://news.ycombinator.com/item?id=49594219) `✓`

**Still `[?]`:** what a receiver has installed, what they are allowed to install, whether they can ask
the author, and **what the first hour is like** — because **every voice above is the sender.** A
second measurement, worth recording: `CLAUDE.md team` across HN comments returned 44 hits, of which
**6 concerned more than one person and 38 were solo setups.** That is the first time this repository
has measured how often the material is shared rather than asserting either way.

## 2. Jobs

- **Get the thing to run, today, without becoming an expert in somebody else's setup.** `✓` #6235's motive · `*` [interview, Q21](interviews.md#part-2-interview-1-of-5).
- **Find out what is actually load-bearing.** `*` [interview, Q22](interviews.md#part-2-interview-1-of-5) — what he had to explain, twice, on a call: *"which files are load-bearing and which are aspirational. **Which rules are real constraints from the client versus my personal taste.**"* **None of that is written down anywhere**, so the explanation is a twenty-minute conversation with a human.

## 3. Pains

- **The handover fails silently and the receiver does not know it failed.** `*` [interview, Q21](interviews.md#part-2-interview-1-of-5) — a contractor got the repo including the agent config: *"paths broken, one server not starting, and **he assumed that was normal and worked around it for two days without mentioning it.**"* Found out on a call, from a workflow that made no sense. *"That was the moment I understood the config had become **tribal knowledge rather than a setup**."* **This is second-hand and n = 1** — the contractor was never asked.
- **Half of what makes the setup work was never written down at all.** `*` [interview, Q26](interviews.md#part-2-interview-1-of-5) — *"roughly **half** of what makes a project go well is stuff I've never written down because writing it down felt too obvious. Then a contractor joins and **none of it transfers**."* **This bounds the ceiling of our entire product** — we validate the written part — and it is now **Q11** in the register — NK-22.
- **A rule from the author's world colliding with the receiver's.** `*` [interview, Q26](interviews.md#part-2-interview-1-of-5) — *"my CLAUDE.md says one thing, the client's linter says another, and **there's no precedence anywhere**; it's resolved by whichever I remember at the time."* `CLAUDE.md` §6 models conflicts **between our items** and has nowhere to put this one — **Q10** in the register, NK-21.

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
anything about how the receiver *feels*, because **no receiver has ever been asked**. Six more voices
arrived on 2026-09-08 and **every one of them is a sender too** — the population, its scale and its
stated difficulty are now `✓`; the experience on the receiving end is exactly as unobserved as it was
([`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-B). **The guide still has no receiver question block.**

---

# P3 · The empty-handed — secondary, and **changed on 2026-09-08**

> **This card used to say that nobody in this shape had ever been observed. That stopped being true,
> and the first evidence runs against the persona rather than for it.** Five practitioners were
> found stating what they do about other people's material, and four of the five refuse it, minimise
> it, or prefer their own ([`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-E). `CLAUDE.md` §8 and §11 ship
> two surfaces and a content commitment for this person. **Read the card as a warning, and read the
> quote block, which is no longer empty.**

## 1. Context

Someone with no collection of their own, or a collection so young it does nothing, opening the
product for the first time. **Still `[?]` that this person exists in numbers — H7 is not closed — but
it is no longer `[?]` in both directions.** The supply is confirmed and enormous; the first demand
signal is scepticism.

**The supply. `✓`** — `"claude skills"` in repository name or description returns **19,703
repositories**, and the top of that list is curated collections at five-figure star counts:
`ComposioHQ/awesome-claude-skills` **74,686★**, `alirezarezvani/claude-skills` **25,709★** and
*"380 Claude Code skills"*, `travisvn/awesome-claude-skills` **15,006★**
([`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-E). **Against that, personal agent-material repositories
that are public number 93.**

**The demand, from the first people ever observed on this question. `✓` as utterances, and four of
five are negative:**

- *"**I'm not sure I've ever used any of them**, and when I've looked at them it's been some **YouTuber trying to make money**."* — [SyneRyder](https://news.ycombinator.com/item?id=49591526)
- *"**I do not understand the appeal of skill shopping.**"* — [resonious](https://news.ycombinator.com/item?id=49595691)
- *"I try to keep my collection of community skills **short**, usually **a few established names**."* — [osr00](https://news.ycombinator.com/item?id=49591803)
- Prefers **creating skills from session learnings** rather than downloading published ones — [sinuhe69](https://news.ycombinator.com/item?id=49595603)
- The one positive is not this persona: *"ship as a plugin and **add your git repo as a marketplace**"* — [jve](https://news.ycombinator.com/item?id=49595170) — **distributing his own material. That is P1's job.**

**What this does not license.** Four sceptics on Hacker News are not a market, that venue is the one
most likely to distrust a marketplace, the thread self-selects for people already managing their own
skills, and **nobody asked a beginner anything.** It does not say cold start is solved or that the
shelf is wrong. **It says the shelf's premise has had its first contact with real opinion and the
opinion is that curated volume is not what these people want** — `osr00`'s *"a few established
names"* is the shape that survived: **provenance over volume.**

What still stands behind the surfaces, and none of it is a person:

- **`V`** A whole tool category exists to install other people's material — `xingkongliang/skills-manager` 4,526★, `MoizIbnYousaf/ai-agent-skills` *"universal skill installer and package manager"* 1,138★, `luongnv89/asm` 915★ — [`re-research.md`](re-research.md) R8. **Their existence and their stars are `✓`; what they do is their own README and we ran none of them** (rule 5).
- **`V`** Catalogs report skills at six and seven figures — Agentman published the figures — and *"discovery is no longer the bottleneck. **Judgment is.**"* comes from **agensi.io, a third-party affiliate-shaped comparison**, not from a hard competitor's own report. *Corrected 2026-09-09 (P-89); the error entered in [`re-research.md`](re-research.md) R9, which lists the sentence under the Agentman bullet.*
- **`V`** OBS-12 — every catalog in the survey solves cold start with **curation and volume**, and not one makes a user's own accumulated material better.

**Nothing in that list is a person.** It is what tools and vendors bet — and as of 2026-09-08 it is
outweighed, in the only sample of actual opinion anyone has taken, by people saying they do not do
this.

## 2. Jobs

**Still `[?]` → H8, and H8 is now a harder hypothesis than it was.** The plausible jobs — *get
something working without composing it myself*; *see what good looks like before writing my own* —
remain unestablished, and **the first opinions collected point the other way**: the observed
practitioners either do not install other people's skills at all, or keep the number deliberately
small and chosen by author reputation. `CLAUDE.md` §11's reasoning for the shelf — *"an empty library
kills the product, because there is nothing to validate"* — is the owner's assertion A-8 and it is
still `[?]`; what changed is that **the alternative reading now has evidence and it did not before.**

## 3. Pains

- **`✓` published, not verified by us — taking other people's material is measurably risky.** [Snyk's ToxicSkills study](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/), 3,984 skills scanned from two public registries on 2026-02-05: **13.4% with critical security issues**, 1,467 with at least one flaw, **76 confirmed malicious payloads**, and *"the barrier to publishing? A `SKILL.md` and a GitHub account that's one week old. **No code signing. No security review. No sandbox by default.**"* We did not re-run the scan and cannot; Snyk sells security tooling; its own post does not reconcile 36% with 36.82%. **The order of magnitude is what this carries, and it is enough:** §11's *"checked sources"* currently means checked for **provenance** and now has to mean checked for **content** — R6, and proposal 5 in [`re-research.md`](re-research.md) §4.
- **`[?]` → H9** — everything else. Whether a curated shelf reads as generous or as filler; whether six green ticks on a first check teach anything; whether an example project labelled *example* is opened at all.

## 4. Trust triggers

- **Convinces, on the best first-run capture in the phase:** `M` OBS-36 — a brand-new Linear workspace opens on the Issues list **already holding four real issues**, with real IDs, statuses and dates, deletable, so the onboarding checklist *is* the data model exercised on itself. This is the shape `CLAUDE.md` §11's example project already copies.
- **Convinces, presumably: provenance.** `CLAUDE.md` §5 requires every public item to show its origin and a pinned `ref`, which is what keeps a shelf with no server behind it honest — *this is the version we checked*, not *this is current*. `M` OBS-34 — Terraform, Figma, Raycast and Backstage all attach an identity to a shared artefact. **That any of it convinces this person is `[?]` → H10.**
- **Repels: emptiness that is also a dead end.** `M` OBS-37 — Linear's three registers of emptiness, and the rule between them: verbosity scales with the chance the reader does not know what the object is. `M` OBS-38 — a control that cannot act is not shown, three products against one.

## 5. Quote

**This box was empty until 2026-09-08, and the absence was the finding. It is no longer empty, and
what filled it is a refusal:**

> *"**I'm not sure I've ever used any of them**, and when I've looked at them it's been some
> **YouTuber trying to make money**."*
>
> — [SyneRyder, Hacker News, *Ask HN: How do you manage skills files?*](https://news.ycombinator.com/item?id=49591526) `✓`

Beside it, from the same thread: *"**I do not understand the appeal of skill shopping.**"* —
[resonious](https://news.ycombinator.com/item?id=49595691) `✓`

**Read what this is and what it is not.** It is a real sentence with a URL, from the thread most
on-topic to this product that anyone has found — 305 points, 274 comments, two days old at
collection. It is **not** the P5 recruit the guide asks for: *someone who does not keep this material
at all*. **Everyone quoted here keeps their own**, which makes them sceptical *consumers*, not
empty-handed newcomers. **The persona this card describes is still unobserved. What is now observed
is the attitude of the people nearest to it, and that attitude is not friendly to a shelf.**

## What this card is allowed to settle

**More than it could yesterday, and still not much.** It may not be cited for the scope switch, the
shelf's size, or the example project's composition — those are `CLAUDE.md` decisions taken on
reasoning. **What it may now be cited for is a warning:** the nearest observed population states a
preference for **a few items from named authors** over curated volume, which bears on **what the
shelf should contain and how it should be sorted**, not on whether it ships. **And it settles exactly
one thing outright:** that the shelf needs a **stated
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
> run. **The collection created the problem.**"* — [interview, Q15](interviews.md#part-2-interview-1-of-5) `*`

That is X6 in [`inventory.md`](inventory.md) §D, it is **one sentence from one person**, and it is the
only causal claim anybody has made. If it holds, the collector *is* the breaker, and P1 is not a
choice between two candidates but the merge of them.

**Four reasons P1 is primary, in descending strength:**

1. **It is the persona with the most agreement between `✓` and `*` from independent instruments** on its jobs and its pains — the multi-target job at 6,592, the drift job at 48, the environmental pain at 182, the collision at 13, and the doubt found **in four of the eight threads read**, plus one interview. *Corrected 2026-09-09: "the only persona" was a superlative P2's own card contradicts (P-107), and "across eight threads" was not what was read (P-108). Reason 1 is weaker than it was written; reasons 2 to 4 still carry the choice.*
2. **It is where the value was already found to concentrate.** The benchmark re-weighted the four flows by pain and put the value in **B3 (check)** and **B4 (produce)** — [`benchmark.md`](../4-benchmark/benchmark.md), *finalisation*. Those are P1's two moments.
3. **It carries the higher risk and has the fewer levers**, which is the lesson's own rule for choosing. If we are wrong about P1, Run and the item card are both wrong, and they are the product. If we are wrong about P3, one scope switch and one seeded project are wrong.
4. **P2's job is a *consequence* of P1's set, not an independent product.** The receiver's pain begins with an archive P1 produced. Designing for P2 without P1 has nothing to design against.

## What would overturn this choice — stated in advance, so it can happen

- **Four more Q15 answers that separate the collection from the breakage.** If practitioners two through five say the breakage came from a single server on a new laptop and had nothing to do with the size of their collection, **X6 collapses**, P1 splits back into two personas, and the primary becomes whichever of them the remaining evidence favours — [`interviews.md` the guide](interviews.md#part-1-the-guide) Q15.
- **An answer to Q5 that says adoption is driven by getting *material*, not by keeping one's own.** Then **P3 becomes primary**, the Library scope switch becomes the centre of the product rather than a switch on a browse screen, and Run's prominence in `CLAUDE.md` §8 is wrong — register Q5 and Q7, [`research-plan.md`](../research-plan.md).
- **A strong answer to guide Q25 that repeats the observability ask.** If four more practitioners answer the genie question with *show me what ran* rather than *check that it holds together*, the primary persona survives but **`CLAUDE.md` §2's core-value sentence does not** — that is **Q12**, and it is the sharpest question this stage produced.

## What these portraits are drawn from — the bias, printed on the page

- **Every public source is a person who chose to write in public.** The whole corpus is filers and commenters — X5, NK-16. The one practitioner interviewed is *also* a filer, so n = 1 cannot correct it. **The guide requires two of the five to have never filed anything in public** ([`interviews.md` the guide](interviews.md#part-1-the-guide) §2); that has not happened yet.
- **Reddit is missing**, and **one community survey names it among the venues this population uses** — R13. *Corrected 2026-09-09 (P-114): "named across community surveys as the largest venue" was a plural and a ranking built on a single unranked survey.*
- **Every number spoken in the interview is a recollection** — *forty-something files*, *one in three fresh environments*, *about half of it* — and the respondent flags his own unreliability twice unprompted. Rule 3.
- **P3 is mostly `[?]`; P1 and P2 are mostly `*` and utterance-level `✓`.** *Corrected 2026-09-09 (P-116): this said "roughly half of every card is `[?]`", and the count refutes it — P1 carries 20 `✓`, 19 `*` and 5 `[?]`; P2 5 / 5 / 2; P3 2 / 0 / 6.* **The adoption half of the prediction was right and stands**: all of the adoption story is `[?]`. The risk the wrong sentence created is the one to keep in mind — a reader leaning on P1's card at `✓` strength because they were told it is only half hypothesis, when most of it is one person's recollection.

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
| **H5** | The **receiver** has a different agent and cannot easily ask the author | **Half closed 2026-09-08.** `✓` that senders distribute across agents and find it *"currently awkward"* — six independent voices ([`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-B). **The receiving end is untouched: every one of those six is a sender.** Ask a receiver — nobody has. *Corrected 2026-09-09 (P-119): the guide **does** recruit one — §2's P3 profile is "has handed a setup to somebody else, **or received one**" — what it lacks is **a block of questions for a receiver**; every question in §4 is addressed to an author* — NK-7 | What `SETUP.md` assumes about its reader (§6) |
| **H6** | A **receiving agent performs the setup correctly from `SETUP.md` alone** | **CLOSED 2026-09-10 — the half-day was run.** [`re-research.md` round 3](re-research.md#round-3-five-questions-that-need-no-interview) Q-F, capture in [`_captures/qf-handover-test/`](_captures/qf-handover-test/). **Performs: yes, three of three**, including cloning an external item at its pinned ref. **Correctly: no.** With the set's Problems undisclosed, one receiver found them, one **mis-resolved one on a false claim of byte-identity**, one saw none — and one copied the machine's live OAuth token into a plaintext file unprompted. The web could not close this and did not have to; we ran it. **The 2026-09-08 reading still stands beside it**: the bet is against the grain of current practice (`re-research.md` round 2 Q-A, two comments in 274) **and the mechanism works anyway**, which is a stronger position than either half alone. Bounded: three model tiers of one vendor's agent, one machine, one day — NK-13 | The spec's most load-bearing bet (§6, §8) |
| **H7** | The **empty-handed persona exists** in numbers that justify shipping a shelf | **Not closed, and it got harder 2026-09-08.** The supply is `✓` and enormous — 19,703 repositories, awesome-lists at five figures — against **93** public personal ones. The first five practitioners ever observed on installing others' material: **four refuse, minimise or prefer their own** ([`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-E). **Still nobody in the shape itself**: everyone quoted keeps their own material. The guide's P5 recruit — someone who does not keep this material at all — remains unfound — NK-9. **Split in two on 2026-09-10.** The *behaviour* the shelf assumes is now `✓` and large — thousands of repositories carry verbatim copies of public skills, 32% of 446 traced copies were edited after import at a median of 27 days ([`re-research.md` round 3](re-research.md#round-3-five-questions-that-need-no-interview) Q-I) — **and the persona is still `[?]`, because no instrument here can say who any importer was.** The hypothesis as written is about *people in that shape*; what got easier is the premise under the feature, not the count of the persona | The `Public library` scope switch (§8, §11) |
| **H8** | Their job is *get something working without composing it myself* | **Unestablished, and the first opinions point the other way** — the observed preference is **a few items from named authors**, not curated volume ([`re-research.md` round 2](re-research.md#round-2-counting-not-asking) Q-E). The same P5 conversation, asked as a situation, never as a pitch | Whether the shelf is a browse surface or a starter kit — **and now also what it should contain and how it should sort** |
| **H9** | A first check showing **one Problem and one Note** teaches the product better than six green ticks | First use of the seeded example project, watched — G5 in [`research.md`](../research.md) | The example project's composition (§11) |
| **H10** | **Provenance and a pinned `ref`** are what make a read-only shelf trustworthy without a server | **Two measurements, 2026-09-10, and they pull the same way.** `✓` **Provenance does not survive a copy**: of 446 foreign copies of five public skills, **45 — 10% — name their origin anywhere in the file** ([`re-research.md` round 3](re-research.md#round-3-five-questions-that-need-no-interview) Q-I). And `✓` **a pinned `ref` did real work in front of us**: in Q-F the receiving agent used the refs in `SETUP.md` to fetch back **both items the archive had silently lost to collisions**, and could then say which of the two was the substantive one. Neither measures *trust*; together they say the thing is scarce and load-bearing. Still open: the same first use, and whether anyone clicks through to an origin — NK-19 | Public item cards (§5), and the licence field that model lacks |
| **H11** | `CLAUDE.md` §3's audience — **25+, visually literate, living in Linear, Vercel, Raycast, Figma** — describes these people | **No instrument in this repository can reach it**, and none has. It is A-4 and A-5, and it stays a hypothesis through the design system unless someone asks | Visual direction, and who the craft bar is set for |

---

# What this hands forward

1. **To the audit (step 4).** The dangerous list is already visible: **every claim carrying only `*` bears on a design decision and stands on one person** — and in this file that includes the whole of P1's trust-trigger block and the whole of P2's pain block.
2. **To the register.** Nothing new. P1's overturning conditions are Q5, Q7 and Q12; P2's pains are Q10 and Q11; P3 is Q9's *which specified features close no evidenced job* with two candidates already named.
3. **To the owner, as work.** **H6 is ours to close** and needs an afternoon. It is the only hypothesis in the table that does not need another person.
4. **Not to `CLAUDE.md`.** Nothing here is applied. Stage 6 audits; the owner edits. If a persona refutes a surface, that is a register entry and not an edit — [`README.md`](README.md), definition of done.
