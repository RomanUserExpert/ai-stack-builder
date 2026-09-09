# Re-research, round 2 — the five questions the critique raised

**A source document**, in the sense stages 1–3 used the word: it states the question, names the
instrument, logs what was collected, and says what that establishes and what it does not. Collected
2026-09-08, the same day [`personas-and-jobs-critique.md`](../personas-and-jobs-critique.md) was
written. Capture log beside it: [`_re-research-2-log.json`](_re-research-2-log.json).

**It is not a digest and nothing may cite it as a decision.** The digest entry it feeds is
[`research.md`](../research.md) §7, *Research justification*.

**Two questions came from the critique's Part 3 unchanged (Q-B, Q-C), one came from it and could not
be answered here (Q-A), and two were raised by the critique's dangerous list and added for this
round (Q-D from D-9, Q-E from D-4).**

**One finding contradicts a decision in `CLAUDE.md` §11 and one corrects a cell in our own matrix.
Neither is applied.**

---

## The instruments, and what each can and cannot see

| # | Instrument | Weighting it offers | Blind to |
|---|---|---|---|
| **I5** | **GitHub repository search API**, unauthenticated | Stars, push dates | Private repositories, and anything unpublished. **The people most like our primary persona keep this material private** — the one practitioner interviewed keeps a *private* repo — so this instrument systematically over-samples people who publish |
| **I6** | **GitHub `git/trees` API**, recursive | **None — it is a direct count** | What any of those files is worth, and whether its owner still uses it. **This is the first instrument in the repository that counts somebody's collection instead of asking them how big it is** |
| **I3b** | **Hacker News via Algolia** — one Ask HN thread, *How do you manage skills files?*, **305 points, 274 comments, filed 2026-09-06**, read in full in four passes | Story points; per-comment scores are not exposed | A self-selecting, English-speaking, HN-shaped population. Loud opinions over quiet practice |

**Rule 5 governs everything below.** Where a row records what a person said, the re-runnable query
proves the **utterance**; the behaviour under it stays self-report. **The I6 rows are the exception**
— a file count in a public tree is a measurement, and it is marked `✓` on that basis.

---

## Q-A — Does a receiving agent perform the setup from `SETUP.md` alone?

**The critique's D-1: the largest commitment in the spec, standing on nothing.**

### Answer: not closed, and no web instrument can close it. But the adjacent evidence is not encouraging.

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

## Q-B — Who receives a handed-over setup, and what happens?

**The critique's D-2: P2 stood on one author's motive sentence and one second-hand story.**

### Answer: the population is confirmed. The first hour is still unobserved.

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

## Q-C — What does a real agent-material repository actually contain?

**The critique's D-3: our "20 to 40 items" blended one organisation's threshold with one person's
recollection.**

### Answer: counted, and the band is wider than we wrote.

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

## Q-D — Does anything already keep secrets out of a handed-over artefact?

**Raised by the critique's D-9:** our matrix wrote *"No, in this space"* for RJ-4's competitor cell,
while `2-flows/07-env-and-secrets/NOTES.md` records that **Doppler and Infisical were captured and
deliberately not scored**.

### Answer: the runtime half is occupied. The handover half is not. Our cell was too strong.

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

## Q-E — Does the empty-handed consumer exist?

**Raised by the critique's D-4:** `CLAUDE.md` §8 and §11 ship two surfaces and a content commitment
for **P3, a persona nobody has ever observed.**

### Answer: people in this shape were finally observed — and the first evidence is against the premise.

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

## What this round hands forward

1. **To [`personas.md`](personas.md).** Five marks change and one persona changes character. Applied in this round and recorded in [`research.md`](../research.md) §7.
2. **To the register.** No new question. Q-A sharpens **NK-13** without moving it; Q-E bears directly on **Q9** — *which specified features close no evidenced job* — and gives that entry its first evidence.
3. **To the matrix in [`jtbd.md`](../7-jobs-to-be-done/jtbd.md).** RJ-4's competitor cell is too strong (Q-D) and H-J4's P3 column is no longer honestly `[?]` (Q-E). **Not applied here** — the matrix is stage 7's and it has its own audit still owed.
4. **To the benchmark.** Doppler and Infisical are captured and unscored; on the evidence of Q-D that is now a gap worth one afternoon.
5. **The half-day that keeps not being spent.** NK-13 / Q-A. Every round of research makes it more load-bearing and none of them can touch it. **Round 3 finally points an instrument at it** — [`re-research-3.md`](re-research-3.md) **Q-F**, written 2026-09-09 when the interviews became unavailable and the only questions left were the ones that need no person.
