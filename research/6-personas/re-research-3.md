# Re-research, round 3 — five questions that need no interview

> **Planned 2026-09-09. Run 2026-09-10.** Every question below now carries an **Answer** section and
> the capture log exists: [`_re-research-3-log.json`](_re-research-3-log.json), plus
> [`_qf-handover-test/`](_qf-handover-test/) for the one experiment that produced an artefact.
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
[`re-research.md`](re-research.md) and [`re-research-2.md`](re-research-2.md) do.

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

## The instruments, and what each can and cannot see

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

## Q-F — Does a receiving agent perform the setup from `SETUP.md` alone? · **I7**

**The highest-value question in the project, and the only one on this list that is entirely ours.**

**What is blocked.** **NK-13**, the audit's **D-1**, and with them `CLAUDE.md` §6's decision that
`SETUP.md` is written for the agent rather than for a human reader, §8's handover stages as the last
stages of Run, and the Q2 disposition that made the document a real artefact. **Every other row in
the audit's dangerous list is downstream of this one.** Round 2 sharpened it and could not close it:
in 274 comments on exactly this topic the work is done by `chezmoi`, symlinks, CLI installers,
`skills.py` and bootstrap scripts, and **two comments describe an agent touching this material at all
— neither is a setup** ([`re-research-2.md`](re-research-2.md) Q-A).

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

### Answer — run 2026-09-10. The setup gets performed. The *checking* does not, and that is the finding.

**Capture:** [`_qf-handover-test/`](_qf-handover-test/) — the ground truth of the composed set, the
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

#### The mechanical half of the bet holds, three times out of three

Every one of the three cloned the external repository **at the exact pinned ref**, installed the
dependency the document named, created `.env` from `.env.example`, and reported at the end. No agent
refused, none asked to be told what to do, and none needed a human in the loop to get that far.
**`SETUP.md` written for a machine is read by a machine and acted on.** That is the first evidence
of any kind under `CLAUDE.md` §6's central decision, and it is positive.

#### The diagnostic half does not hold, and it splits by tier

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

#### What the test discovered that nobody planted

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

#### What this establishes, and what it does not

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

## Q-G — What does a receiver actually do with inherited material? · **I8**

**The only way to see the receiving end without a receiver in the room.**

**What is blocked.** **The entire P2 column of the matrix** — MAIN/P2, RJ-1/P2, RJ-2/P2, RJ-3/P2,
RJ-4/P2, SJ-1/P2, H-J7/P2 — plus **NK-7's receiving half** and the audit's **D-2**, which is the
second most dangerous claim in the folder. Round 2 confirmed the population from **six independent
voices and every one of them is a sender** ([`re-research-2.md`](re-research-2.md) Q-B). Nobody has
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

### Answer — a striking number, and a control that takes it away again

**Instrument as run.** Sixteen repository-search queries built a population of **653 parent
repositories** holding one person's agent material and carrying between 1 and 99 forks. Repositories
above 99 forks were excluded on purpose: at that size the thing being forked is a template, and
forking a template is not receiving a handover. Every fork of every one of those parents was read
through the compare API across the fork point — **2,130 fork records, 103 of them unresolvable
(deleted, empty or gone private), 2,027 resolved.** Counts and queries in
[`_re-research-3-log.json`](_re-research-3-log.json).

#### The headline

> **1,813 of 2,027 forks — 89.4% — have not a single commit after the fork point.**

**214 forks, 10.6%, committed anything at all.** The plan said to count that case separately and
honestly, and it is now the largest number in the study.

**Of the 214 who did commit, when they did it:** median **25 minutes** after the fork,
**55% within the first hour**, 70% within a day (n = 159; 55 records excluded because their commits
predate the fork record and the timing cannot be trusted). **The first hour is real.** Whatever a
receiver does, they do it immediately or never.

#### What the 214 changed

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

#### What this does to the P2 column

The plan named three outcomes and said which each would change. **On the raw numbers the third looked
like it had fired** — *if they mostly delete things or never commit, the archive is not being received
at all and the whole P2 story needs rewriting before it is designed for.* **It had not.** The control
below shows why, and it is the reason this section reads as it does rather than as that sentence.

#### The control — run afterwards, and it takes the headline away

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

#### What survives the control

- **Timing.** Of the 214 who committed, **55% did so within the first hour** and 70% within a day,
  median 25 minutes. The control does not touch this: it is a statement about the people who *did*
  act, not about how many did.
- **The 25 self-substitutions**, which are matched pairs and can be read one by one. They are the
  thing no baseline explains away, because they are not *whether* somebody acted but *what the act
  was*: replacing the author with themselves in setup URLs, git identity, absolute paths, branch
  conventions and **instructions addressed to the agent that name the author's handle**.
- **The one handover this repository has ever heard described was private** — a repository handed to
  a contractor, [interview Q21](agent-setup-interview.md) — and it would appear in this instrument as
  nothing at all. That was true before the control and is still true.

**What it establishes `✓`:** when somebody takes another person's agent material and acts on it, they
act **within the hour**, and the commonest concrete edit is **replacing the author with themselves**.
**RJ-1 now has a behaviour under it**, which the audit had left it without. It is a modest one — 25
cases out of 2,027 forks — and it is not a self-report.

**What it does not establish:** anything about how often handover happens, in either direction.

---

## Q-H — Do copies actually drift, and for how long? · **I9**

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

### Answer — copies diverge, they stay diverged for months, and almost nobody ever reconciles

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

#### Duration, from history

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

#### What this establishes, and what it does not

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

## Q-I — Does other people's material get kept, or only starred? · **I10**

**What is blocked.** **H-J4 and the whole P3 column**, **Q9** in the register, and `CLAUDE.md` §8's
scope switch and §11's shelf with its build commitment. Round 2 established the supply — **19,703
repositories, 74,686★ at the top, against 93 personal ones** — and reached five practitioners whose
opinion of installing others' material was four-to-one negative
([`re-research-2.md`](re-research-2.md) Q-E). **Opinion is not behaviour, and stars are not use.**

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

### Answer — a third of imports get edited, two thirds never do, and the installer category is not flat

#### The registry series, with two identity corrections first

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

#### The vendored-file trace

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

#### Provenance, and a measurement thrown away

The first pass reported 82% of copies carrying "a statement of origin" and it was wrong: the rule
matched the word `license`, which **every one of these skills already carries in its own
frontmatter** (`license: Complete terms in LICENSE.txt`). That counts the original file surviving,
not the importer crediting anybody. A second rule matching *"based on"* was thrown away for the same
reason — sampled, it was matching ordinary prose inside the skills (*"Color based on cell size"*).

**The one rule that survives is the strict one: does the copied file name `anthropics/skills` or an
anthropics URL anywhere in its body.**

> **45 of 446 — 10%.**

#### What this establishes, and what it does not

**`✓` — consuming other people's agent material is a mass behaviour, not a niche one**, and it is
recurring rather than one-off: a third of imports are edited, at a median of four weeks after
arriving. **`✓` — provenance does not survive the copy.** Nine copies in ten carry no statement of
where they came from.

**Against round 2, and the plan predicted this.** [`re-research-2.md`](re-research-2.md) Q-E reached
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

## Q-J — Does anything on the market actually perform the set-level check? · **I11**

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

### Answer — §2's sentence survives at the set level and has to be narrowed twice more at the item level

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

#### The grid — our four planted defect classes against four shipping tools

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

#### And then the tool was given a duplicate it *does* claim to handle

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

#### What the market has that our benchmark said nobody had

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

#### What this establishes, and what it does not

**`✓`, and it covers behaviour, because we watched these programs run on our own artefact.** Dated
2026-09-10, versioned in the table above.

**It does not establish** what Tessl or Smithery do behind a login, what `HarnessKit` does — it could
not be installed — or what any of them ships next quarter. **And step 4 of the plan was not run:**
Doppler's and Infisical's free tiers were not tested for whether they touch what an artefact
**carries when it leaves**. That benchmark gap, opened by Q-D, is still open.

---

## What these five cannot do, said once and plainly

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

## What this round would hand forward

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

# What it actually handed forward — 2026-09-10

**Nothing here is applied to [`CLAUDE.md`](../../CLAUDE.md).** A research round may narrow a claim,
close a hypothesis and raise a proposal; the owner edits the spec, at the register's sitting. This
section is the list that sitting reads, on top of the two proposal lists it already had.

## Two hypotheses are closed, and one register entry gains its first behavioural evidence

| | Was | Is now |
|---|---|---|
| **NK-13 / D-1** — *a receiving agent performs the setup from `SETUP.md` alone* | The spec's largest bet, taken on reasoning, never tested | **Closed `✓`.** Three of three receivers performed it, including cloning at the pinned ref. **And the second half of the bet failed**: leaving the Problems to the receiver does not work |
| **H6** in [`personas.md`](personas.md) | *Not closed, and the web cannot close it* | **Closed by Q-F**, on the same evidence |
| **H-J4 / Q9** — *does the shelf's premise describe a real behaviour* | Opinion only: four of five practitioners negative (Q-E) | **Behaviour measured.** Thousands of repositories vendor public skills; 32% of imports are edited, at a median of 27 days; 10% keep provenance |

## Six proposals, each with the evidence that raised it

| # | Spec section | What was found | Proposal |
|---|---|---|---|
| **S-1** | **§6**, `SETUP.md` | Of three receivers, one found the Problems, one **mis-resolved** one on a false claim of byte-identity, one saw none. The document states requirements and not findings, by design | **`SETUP.md` should carry the set's Problems.** The disclosure §8 gives the *sender* before Export is the disclosure the *receiver* turns out to need. This is the round's largest proposal |
| **S-2** | **§5**, the `Item` shape | The `pdf` skill instructs the agent to read `REFERENCE.md`, `FORMS.md` and eight scripts. `content` holds one blob and `targetPath` one destination, so **the export was silently incomplete and `SETUP.md` said the item required nothing** | **An item addresses a directory, not a file.** This is a model change, and it is the only one this round proposes |
| **S-3** | **§6**, what an item can do | The `settings.json` that won the collision **declares a third-party plugin marketplace and enables a plugin from it**. An archive can reconfigure the receiving agent before setup begins | **Treat a settings file as an executable item**, and say so where §6 lists what export produces |
| **S-4** | **§6**, `needsEnv` · **RJ-4** | A receiver told only to *set this project up* **copied the machine's live OAuth token out of the keyring into a plaintext file**. First observation ever on RJ-4's receiving side | **The secrets risk runs both ways.** What the receiver fetches to fill the gap the sender left is a hazard the spec does not name |
| **S-5** | **§2**, *nothing does this today* | Four tools installed and run: **nothing detects a set-level defect, because nothing has a set-level unit.** But `asm` ships **369 pre-defined bundles** — *"a reusable recipe of skills for a project setup"* — and `asm doctor` is a **B4 surface**, which the benchmark said nobody had | **Narrow it precisely rather than cautiously.** The set-level *check* is unoccupied; the set-level *concept* and the receiving-machine *report* are not |
| **S-6** | **§6**, three severities | `asm audit` calls two files with different sha1s *"✓ identical copies"* and offers to auto-remove one. `asm audit security` returns **SAFE** on a scan of *0 files, 0 lines* | **No change — evidence for a decision already taken.** *Nothing blocks, everything is named*, and *Skipped* gets a glyph it earned, now each have a dated specimen in a shipping product |

## What did not move, and one thing that got harder

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

## And what the round says about its own instruments

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
