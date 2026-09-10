# Re-research, round 4 — hunting the matrix's empty cells

**A source document.** Collected 2026-09-10, the same day round 3 was run. Capture log beside it:
[`_re-research-4-log.json`](_re-research-4-log.json).

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

## The venues, and one that still refuses

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

## What was found, and what it does to the matrix

**Three cells change, and this is the first round that adds to the matrix rather than subtracting
from it.** The audit of 2026-09-09 only ever removed; round 3 moved nothing vertical. Below, two
`[?]` become numbers and one number goes up, each with the utterance under it.

---

### F1 — RJ-2 / P1: **2 → 3.** A collection that collides, a vendor confirming it, and two people who rebuilt their tooling around it

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

### F2 — EJ-2 / P1: **`[?]` → 2.** Somebody asking to see the context window in order to tell *not loaded* from *not followed*

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

### F3 — H-J3 / P1: **`[?]` → 2.** The detach requirement, stated by somebody who has it and cannot get it

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

### F4 — What did not change: the P2 column, and it is not for want of looking

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

### F5 — P3: two beginners, and **neither reaches for a shelf**

The clearest beginner posts on the vendor's forum, both **asked once and never answered**:

- **[Beginner with Agents in Cursor AI](https://forum.cursor.com/t/beginner-with-agents-in-cursor-ai/137798)** — *"I've been using Cursor for a few days… I've connected a Supabase MCP and **created a detailed Markdown file with all the info about the project**… I've asked 10 times already."* **He wrote his own material on day one.** No reply; auto-closed.
- **[Cursor for beginner — need general guidance](https://forum.cursor.com/t/cursor-for-beginner-need-general-guidance/75300)** — *"I'm new here… I wanted to see what projects people have built… **I was wondering if anyone experienced here would be willing to let me shadow them as they code for 30 mins**."* **He asks for a person, not a library.** No reply.

**Neither is P3 in the sense §11's shelf is built for.** One had nothing and immediately made his own;
the other wanted to watch a human. **P3's column stays `[?]` in all ten rows**, and this is now the
third instrument to look for that persona and fail to find it — [`re-research-2.md`](re-research-2.md)
Q-E, round 3's Q-I, and this. **What round 3 established stands and is unaffected**: the *behaviour*
the shelf assumes — importing other people's material and coming back to edit it — is real and large.
**What no instrument has found is a person who has nothing and wants somebody else's.**

---

### F6 — Corroborations that change no cell and are worth having

- **The agent is a more reliable reader than the human.** *"I think it won't be bigger than the giant set of rules people are supposed to read through (**they never do**) when onboarding. At least with AGENTS/CLAUDE.md file, **you know the agent will re-read those rules on every new session**."* — [egeozcan, HN](https://news.ycombinator.com/item?id=46741655). This is `CLAUDE.md` §6's Q2 decision — *`SETUP.md` is written for the agent, not for a human reader* — argued by somebody who has never heard of us.
- **`CLAUDE.md` is described as onboarding documentation** by two independent HN commenters ([theshrike79](https://news.ycombinator.com/item?id=45123992), [btbuildem](https://news.ycombinator.com/item?id=44936992)), which is SJ-1's premise from the sender's side.
- **A handover artefact is wanted and does not exist.** [Help me find or create an handover skill](https://community.openai.com/t/help-me-find-or-create-an-handover-skill/1374002) — 453 views on a two-post thread: *"I'm looking for a skill which I can use at the end of a session to create an handoff document… I had a look at the `curated` skills using the `skill-installer` but **I couldn't find anything**."* The answer is a manual workaround: enforce a session log in `agents.md`.
- **Multi-device sync is "awkward", and the answer is again a repo.** [Sync global rules](https://forum.cursor.com/t/sync-global-rules-and-chats/66299), 760 views: three devices, *"Sharing rules is awkward, but doable"*; the community's answer is *"set up a repo for you to store all of your rules in… pull down what I need for each project"* — R2's symlink-and-repo workaround, a fourth time.
- **A second, independent source for §11's security number.** [Agensi](https://news.ycombinator.com/item?id=47846681), a curated SKILL.md marketplace, states *"36% of sampled skills had prompt injection vectors"* and scans every listing. Round 1's R6 had this from Snyk alone, *published, not verified by us*; it now has a second party acting on the same order of magnitude. **§11 still has no content-review standard.**

---

## What this round establishes, and what it does not

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
