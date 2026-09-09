# Re-research, round 3 — five questions that need no interview

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

---

## What these five cannot do, said once and plainly

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
