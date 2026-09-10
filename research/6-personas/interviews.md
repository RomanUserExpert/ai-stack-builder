# Interviews — the instrument, and the one conversation that happened

**Merged on 2026-09-10** from the files that were `interview-guide.md` and `agent-setup-interview.md`, both
unchanged. They are one thing read from two sides: the guide is the instrument that lifts
*provisional*, and the interview is the only time it has been used.

> **The remaining four conversations are unavailable, recorded 2026-09-09.** That removes an
> event; it does not lower a bar. Everything in part 2 is marked **`*`** and `n = 1`.

| | |
|---|---|
| **[1. The guide](#part-1-the-guide)** | The instrument for the five Q5 conversations |
| **[2. Interview 1 of 5](#part-2-interview-1-of-5)** | The one practitioner run against it |

---

# Part 1. The guide

### Interview guide — the instrument for the five conversations

**Stage 6 deliverable.** Written 2026-09-07, **before the conversations are scheduled**, which is the
point: the register wrote down a trigger — *ask five practitioners before the first feature that only
pays off under one answer* — and left it without an instrument. This is the instrument.

**It exists because of what the desk research could not do.**
[`re-research.md`](re-research.md) took four instruments to the public record and moved eleven of the
twenty unknowns in [`inventory.md`](inventory.md). **Nine did not move, and seven of those need a
person.** Every question below traces to one of them, and the coverage table in §8 proves it.

**What it is worth.** Five conversations cannot establish frequency, market size or demand. They can
**refute** a primary-persona choice and a main-job choice, which is exactly what stages 6 and 7 need
and cannot get anywhere else. Five is the number the register wrote down and it is the smallest
number that can do that job.

**When it fires, the label lifts.** Notes from all five, filed in this folder as a source document,
are the event that lifts **provisional** from `personas.md` and `jtbd.md`, and the named instrument
for **Q5**, **Q7**, **Q8** and **Q9** in [`research-plan.md`](../research-plan.md).

---

#### 1. The one thing this instrument exists to do

Everything else is secondary to this, and it is easy to lose:

> **NK-15 — are the loud pain and the quiet pain the same person?**
>
> The archive lands on another machine and does not run — **6,592 reactions** at the top of our
> audience's own tracker. Two items claim the same key and the first one silently wins — **13
> reactions**. Both were counted across the same corpora and **never joined per person.** A reaction
> count carries no identity, so no amount of further searching can answer this.
>
> **The whole primary-persona choice turns on it**, and so does the main job.

**This dictates the method.** Every one of the five people is asked **both** — §4's block B and block
C — regardless of which one they light up on. The answer is a **join across five rows**, not a tally
of anecdotes. Do not stop asking block C because someone answered block B vividly. That mistake would
reproduce the exact blindness the desk research already has.

---

#### 2. Who to talk to — and how not to select the answer

**Five people. Aim for four of these five profiles**, because a room of one profile answers NK-15 by
construction rather than by evidence.

| | Profile | Why |
|---|---|---|
| **P1** | Keeps agent material for **more than one target** — any two of Claude Code, Codex, Cursor, Copilot, Gemini, an open harness | The commonest observed shape ([re-research](re-research.md) R2) |
| **P2** | Uses **one** target and is happy about it | The control. If P2 has none of the pains, that is a finding |
| **P3** | Has **handed a setup to somebody else**, or received one | NK-7, and §6's *nothing blocks* premise rests on it |
| **P4** | Has **built or installed** a skill/rules manager | They already paid to solve this. What did it not fix? (R8) |
| **P5** | **Stopped** keeping this material, or never started | The only access we have to non-adoption. Hardest to recruit; worth the most |

**The recruiting screen, asked before agreeing a time.** Two questions, and neither mentions the
product:

> *"Do you use any coding agent day to day? Which ones?"*
> *"Do you keep any instructions, rules, prompts or skills for it in files you reuse?"*

**Anyone who says no to the second is still worth 30 minutes** — they are P5, and P5 is the profile
this repository has never once observed.

**NK-16, stated so it is not forgotten.** Everything we know about these people comes from those who
**file issues in public trackers**. That is a behaviour, not a job title, and it is possibly the most
self-selecting population in software. So: **at least two of the five must be people who have never
filed an issue about any of this.** Ask it directly at the end (§4, block F) and record it.

**Where they are** ([re-research](re-research.md) R13): Discord — Latent Space, Anthropic's Claude
Code channels, Cursor, Ollama; Reddit — r/ClaudeAI, r/ChatGPTCoding, r/AI_Agents; Hacker News. Note
the irony worth remembering while recruiting: **Reddit is where they are and it is the one place our
desk research could not read.**

---

#### 3. Six rules, and the first two are the whole method

**1. Ask for the last instance, never for the habit.** *"How do you usually organise your prompts"*
gets you a tidied-up story about the person they wish they were. *"Walk me through the last time you
started a new project — what did you actually do first?"* gets you what happened. **If an answer
comes back in the present tense and the plural, you asked the wrong question.** Reach for: *"When was
that?" · "Show me, if it's on this machine." · "What did you do right before that?"*

**2. Never pitch. Not once, not at the end, not to be polite.** The moment they know what you are
building, everything after it is worthless. This is not a demo call. If they ask what you are working
on, say *"I'll tell you at the end, I don't want to bias you"* — and mean it. §7 has the only place a
description is allowed, and it is after all the questions.

**3. Both blocks, every person.** See §1.

**4. Silence is a question.** Count to five after they stop. The second half of an answer is where
the friction lives.

**5. Never accept an abstraction.** *"It's a bit of a mess"* is not data. *"Show me"* or *"what was
the last thing that was a mess"* is.

**6. Ask about cost in time, money and mood — never on a scale.** Not *"how painful, 1 to 5"*. Ask
*"how long did that take"*, *"did you do anything about it"*, *"what did you do instead"*. **Whether
they ever paid for or built something is the strongest signal available**, because it is behaviour
rather than opinion.

---

#### 4. The thirty minutes

Times are a budget, not a script. If block B or C opens up, spend the time and cut block E.

##### A. Setup census — 4 min
*Answers: NK-4, NK-2, NK-3, NK-5 confirm, NK-16*

1. *"Which coding agents do you have installed right now?"* → then: *"Which did you use yesterday?"*
   — installed and used are different numbers; write both down.
2. *"When did you last open any of them?"* — never *"how often do you use it"*. **(NK-4)**
3. *"Do you have a file, folder or repo where you keep instructions, rules, prompts or skills for
   them? Where is it?"* → *"Can you say roughly how many things are in it?"* **(NK-2)**
4. *"How long has that existed? What was in it when you started?"* **(NK-3 — the only route to
   growth rate, and it is a memory, so treat it as soft)**
5. *"Did you set it up on more than one machine? What happened?"*

##### B. The last new project — 7 min
*Answers: NK-1 (reassembly), NK-8, NK-10, NK-14*

6. **"Take me through the last time you started a new project or a new repo. What did you do in the
   first hour?"** → follow with *"and what about the agent side of it?"* only if they do not raise it.
   **Do not raise it earlier — whether they mention it unprompted is itself the datum.**
7. *"Did anything come across from something you'd done before? What, and how did it get there?"*
   **(NK-10; expect symlinks, copy-paste, `@include`, a script)**
8. *"Was there anything you wanted to bring across and didn't? What stopped you?"* **(NK-8 — the
   closest thing to a direct read on wanting a previous project back)**
9. *"How long did that setup take, start to finish?"*
10. *"Has anything you copied across ever gone out of date, or drifted from the original? What
    happened then?"* **(NK-14)**

##### C. The last time it did not work — 7 min
*Answers: NK-1 (breakage), NK-20, NK-15 join, NK-11*

**Ask this of everyone, including the person who has just spent seven minutes on block B.**

11. **"Tell me about the last time you moved a setup to another machine — or a container, or a new
    laptop, or handed it to somebody — and it didn't work."** → *"How did you find out?"* ·
    *"How long did it take to fix?"*
12. *"Was that a one-off or does it happen?"*
13. *"Have you ever had the tool do something you didn't ask for, or ignore something you did ask
    for, and only found out later?"* **(NK-11, and the collision family — the phrasing avoids naming
    duplicates, keys or configs. Let them name it.)**
14. If they describe a silent wrong choice: *"How did you eventually notice?"* and *"what would you
    have wanted to happen instead?"*
15. *"When that happened, did you have a collection of this stuff already, or were you setting up one
    thing?"* **(NK-20 — the join between environmental pain and having a library at all)**

**On the sheet, mark both boxes for this person before moving on:** did block B land, did block C
land, and which one they told with more heat. **That pair of marks is NK-15.**

##### D. The material itself — 6 min
*Answers: NK-11, NK-12, NK-14, NK-17*

16. *"Of the things in that folder — is there anything you're not sure is doing anything?"*
    **(This is the doubt the threads are full of ([re-research](re-research.md) R7) and the spec never
    anticipated. Expect: "I can never quite tell if it's helping.")**
17. *"How would you find out whether it was working?"* → *"Have you ever actually checked?"*
18. *"Is there anything in there you'd delete if you were being honest?"* **(NK-14)**
19. *"When you go to that folder, what are you usually about to do?"* **(NK-17 — the situation people
    arrive from, which no instrument here has ever seen)**
20. *"If you were picking one of your own things to reuse and couldn't remember which was good — what
    would help you decide?"* **(NK-12. Ask it open. Never offer "used in 3 projects" as an option —
    if they invent a usage fact themselves, that is worth a great deal; if we suggest it, it is worth
    nothing.)**

##### E. Other people — 4 min
*Answers: NK-7, NK-18, NK-16*

21. *"Has anyone else ever opened or run your setup? Who, and what happened?"* **(NK-7 — §6's
    *"their own machine, only party at risk"* rests on the answer)**
22. *"Have you ever given this material to somebody — a colleague, a friend, publicly?"* → if yes:
    *"what did you have to explain to them?"*
23. *"Is any of it public? Would you want it to be?"* **(NK-18 — the row that came back empty from
    every search. Ask it plainly and record a plain no as a real answer.)**
24. *"Have you ever filed an issue or posted publicly about any of this?"* **(NK-16)**

##### F. Close — 2 min
*Answers: NK-9*

25. **"If a genie fixed exactly one thing about all of this tomorrow, what would you have it fix?"**
    → then the important half: *"and have you ever gone looking for something that does that?"* →
    *"did you find anything? did you keep using it?"* **(NK-9, and it is the only read we get on
    non-adoption: people who searched, found something, and stopped using it.)**
26. *"Is there anything I should have asked and didn't?"*

---

#### 5. The three register questions, and how the sheet answers them

The guide is not organised by register question, because a person cannot be interviewed by
register question. This is the mapping used when the five sheets are read together.

| | Question | What in the sheet answers it |
|---|---|---|
| **Q5** | Loss, reassembly cost, or breakage — which drives adoption? | Q6–Q9 against Q11–Q12, plus Q25's *did you go looking*. **Loss has no evidence in any instrument so far** — if nobody in five raises *I couldn't find something I'd written*, that is a real result and must be written down as one, not glossed over. |
| **Q7** | Who is the primary persona — the one whose pain is *sighted* (breaks at handover) or the *collector* §3 describes? | **The block B / block C marks in §4C.** Five rows, joined per person. If both land on the same people, we have one persona and the spec's framing survives. If they split, we have two and the primary must be argued. |
| **Q8** | Is the main job *assemble a set that holds together* or *hand a set to a machine and have it run first time*? | Q6 and Q11 told as stories, plus Q25. **The lesson's rule applies: if both survive, that is two products, and it goes back to the register as a finding rather than being resolved by taste.** |
| **Q9** | Which specified features close no evidenced job? | Q8 (duplicate/promote), Q20 (usage facts), Q21–Q23 (visibility, publishing), Q3 and Q16 (a public shelf, if they raise installing other people's material unprompted). **Absence in five conversations is not grounds to cut a feature** — it is grounds for a register entry saying so. |

---

#### 6. Words never to say

Our own vocabulary would launder the answers — the same trap stage 7's feature-name test exists to
catch, applied to a live conversation where it cannot be edited afterwards.

**Never say:** *item · project · library · workspace · stack · validation · validate · check · run ·
Problem · Note · Skipped · export · archive · bundle · detach · promote · dependency · conflict ·
collision · palette · target · `SETUP.md` · `.env.example` · public library · assemble.*

**Say instead:** *thing · folder · files · the stuff you keep · did it work · what happened · did
anything break · did you copy it · give it to someone.*

**And never ask any of these** — each one hands over the answer:

- ❌ *"Would it be useful if something checked your setup before you shipped it?"* — everyone says yes.
- ❌ *"How painful is it when configs collide?"* — presupposes both the pain and the word.
- ❌ *"Would you use a tool that…"* — hypothetical purchase intent is worthless.
- ❌ *"Do you lose track of your prompts?"* — this is Q5's own hypothesis, read aloud. **Loss must be
  raised by them or not at all.**

---

#### 7. The one place a description is allowed

**After question 26 and not before.** If you want a reaction, describe it in one sentence with no
vocabulary from §6 — *"a place to keep this stuff and put a set of it together for a project, that
tells you if the set won't work before you hand it over"* — and then **write down the first thing
they say and stop talking.** Their first sentence is data. The conversation after it is not, and
nothing said after this point may be used to source a persona block. Mark it on the sheet as
**post-disclosure**.

---

#### 8. Coverage — every open row, and where it is asked

| Row | Status before | Asked at |
|---|---|---|
| **NK-1** — which pain drives adoption | Moved, not closed | Q6–Q9 vs Q11–Q12, Q25 |
| **NK-2** — library size | Partly closed (20–30 reported) | Q3 |
| **NK-3** — growth rate | Untouched | Q4 |
| **NK-4** — frequency of use | Untouched | Q2 |
| **NK-7** — alone or handed over | Partly closed | Q21, Q22 |
| **NK-8** — wanting a prior project back | Untouched | Q8 |
| **NK-9** — would anyone adopt, and why | Untouched | Q25 |
| **NK-11** — what makes them distrust | Moved, redirected | Q13, Q14, Q16, Q17 |
| **NK-12** — is a usage fact persuasive | Untouched | Q20 |
| **NK-14** — is metadata maintained | Weak signal only | Q10, Q18 |
| **NK-15** — same person, loud and quiet pain | **Untouched, and unresolvable by search** | **§4C marks — the whole point** |
| **NK-16** — are filers our audience | Improved, open | Q24, plus the recruiting rule in §2 |
| **NK-17** — emotional register on arrival | Untouched | Q19 |
| **NK-18** — portfolio | Searched, nothing found | Q23 |
| **NK-20** — env pain and having a library | Untouched | Q15 |

**Not in this guide, deliberately.** **NK-5**, **NK-6** and **NK-10** are closed by
[`re-research.md`](re-research.md) — Q1, Q3 and Q7 re-ask them only as corroboration, and a
contradiction there would be a finding worth more than a confirmation. **NK-13** — *does a receiving
agent set a project up from `SETUP.md` alone* — is not a question for a person: **we test it
ourselves, and it is still untested.** **NK-19** — licensing — is a rule and a field, not a
conversation.

---

#### 9. What to write down, and how to file it

**During:** verbatim quotes with the question number, and the §4C pair of marks. **Never write
conclusions in the room.**

**Within an hour, one sheet per person**, in this folder as `interview-01.md` … `interview-05.md`:

```
Person 01 · date · profile P1–P5 · targets installed / used yesterday · collection size · how long it has existed
Ever filed publicly about this: yes / no
Block B landed: yes / no / partly     ← the last new project
Block C landed: yes / no / partly     ← the last time it did not work
Told with more heat: B / C / neither
Loss raised unprompted: yes / no      ← Q5's third candidate; record a no as a result
Verbatim quotes, by question number
What surprised me
What I asked badly
Post-disclosure reaction (single first sentence, marked as such)
```

**After all five**, one `interviews.md` — a **source document**, in the sense stages 1–3 used the
word: what was asked, who was asked, what came back, what it establishes and what it does not. Then,
and only then, the `[?]` marks lift in [`inventory.md`](inventory.md), `personas.md` and `jtbd.md`,
each one carrying its new source. **A `[?]` lifted without a quote behind it is the failure mode this
whole stage was built to avoid.**

---

#### 10. What this instrument still cannot do

Five people cannot tell us how many people. They cannot price anything, they cannot size a market,
and they cannot tell us whether a product would sell — **and the temptation to read them that way
will be strongest precisely where the evidence is thinnest**, which is adoption.

They also arrive after a desk pass that already has a favourite. [`re-research.md`](re-research.md)
found the multi-target problem at 6,592 reactions, and that number will be sitting in the room. **The
questions in §4 are ordered so that block B — the reassembly story — is asked before block C, which
is the loud one**, precisely so the loud finding does not set the frame. If the interviewer starts
hearing what they already found, that is a sign the rules in §3 slipped, not a sign of confirmation.

**Stage 7 adds its three audit questions here** when `jtbd.md` is written, so that one conversation
serves both stages. Until then this guide covers stage 6's rows and the four register questions
named in §5.


---

# Part 2. Interview 1 of 5

### Agent Setup Interview

> **Standing: `*` practitioner-reported. One person.** Filed 2026-09-07, run against
> [`interviews.md` the guide](interviews.md#part-1-the-guide). **Everything in this file is `*`** under the evidence rule
> in [`research.md`](../research.md), *The three marks*: it is evidence about **this respondent**,
> spoken from memory about their own work, and it is not a fact about anybody else. Every number in
> it — *forty-something files*, *one in three fresh environments*, *about half of it* — is a
> recollection, not a measurement, and the respondent flags his own unreliability twice unprompted
> (*"I usually round that down"*, *"it's a story I tell myself"*).
>
> **This is one of the five the trigger names, not the five.** Q5's disposition, and the
> **provisional** label on stage 6 and stage 7, both lift on **five** conversations filed as a source
> document — five being the smallest number that can refute a primary-persona choice rather than
> merely colour it. **Four still to run**, and §2 of the guide asks that at least two of them be
> people who have never filed an issue in public, and that one be someone who does not keep this
> material at all.
>
> **The respondent is described but not identified**, and the answers are written as spoken and
> lightly cleaned up — so this cannot be re-run by a third party the way a logged query can. That is
> what separates `*` from `✓` and it is not a defect: no instrument in this repository before it could
> reach motive, cost or feeling at all.

Respondent: AI engineer, 4+ years. Mixed client work and own products.
Format: answers written as spoken, lightly cleaned up.

---

#### A. Setup census

**1. Which coding agents do you currently have installed? And which one did you actually use yesterday?**

Installed: Claude Code, Cursor, Codex CLI, and Aider, which I haven't opened since maybe October. Continue is technically still in my VS Code extensions but it's dead weight.

Yesterday it was Claude Code, in the terminal, two sessions. One on a client repo doing a boring migration of an old chunking pipeline, one on my own thing where I was trying to get an eval harness to stop flaking. Cursor I open when I want to read code more than write it; the inline stuff is nicer for browsing. But the real work goes through Claude Code because it can run things and see what broke.

**2. When did you last open any of them?**

About forty minutes ago. It's open right now in another tab, sitting on a failed test I've been ignoring.

**3. Is there a file, folder or repo where you keep instructions, rules, prompts or skills for them? Where? Roughly how much is in it?**

Yes. `~/dev/kit/agents/`, which is a private GitHub repo called `agent-kit`. It gets symlinked into `~/.claude/` and a couple of other places.

Contents, roughly: 11 skills, 6 CLAUDE.md templates split by stack, an `mcp/` folder with 9 server configs, a `prompts/` folder that's honestly a separate thing that ended up living here anyway, and a `scripts/` folder with the bootstrap script that does the symlinking. Call it 40-something files. Somewhere around 6k lines total if you count the markdown, and most of that is markdown.

**4. How long has it existed? What was in it at the start?**

Fourteen months, give or take. It started as exactly one file: a CLAUDE.md I wrote for a client project that kept making the agent write raw SQL when the project had a repository layer. I copied that file to the next project, then the next, and at project four I got annoyed and made a repo.

So the origin is not "I designed a system." The origin is "I got tired of copy-pasting one file."

**5. Have you deployed it on more than one machine? What happened?**

Three, if you count containers. Work MacBook, home Linux box on Ubuntu, and devcontainers for two client projects that require an isolated environment.

What happened is it broke on Linux, and it broke in the stupidest possible way: absolute paths. The MCP configs had `/Users/me/...` hardcoded in the `command` and `args` fields because that's what the docs example looked like when I set it up and I never went back. On the Mac everything worked for months so I had no reason to look. Moved to Linux, four MCP servers just silently didn't start, and Claude Code doesn't scream about that, it just doesn't have the tools. I spent the first twenty minutes thinking the model had gotten worse.

---

#### B. The last new project

**6. Walk me through the last time you started a new project or repo. What did you do in the first hour?**

Three weeks ago, a small internal tool for a client, document intake with classification on top. First hour, honestly:

Ten minutes of `mkdir`, git init, pushing an empty repo. Then Python env, pinning versions, the usual. Then I wrote the README before any code, which is a habit I picked up because if I can't write the README the scope isn't clear yet. Then about fifteen minutes arguing with myself about whether this needed Postgres or whether SQLite would carry it to the end of the engagement.

Then I wrote a fake input document and a fake expected output, because I wanted the shape of the thing pinned down before anything real existed.

**> And on the agent side?**

Right, that. I copied CLAUDE.md from a previous project of a similar shape, and that took two minutes, and then I spent maybe twenty minutes editing it, which is the part nobody counts. Then I pulled two skills across, one for the eval format and one for the commit convention I use on client repos. Then the MCP config, which I copied wholesale and then trimmed, because half the servers in it were irrelevant to this project and I didn't want the tool list bloated.

So call it thirty-five minutes of the first hour, if I'm being honest about it, and I usually round that down to "ten minutes, it's just a copy" when someone asks.

**7. Did anything carry over from earlier work? What exactly, and how?**

The CLAUDE.md, the two skills, the MCP config. All of it moved by `cp`. Not by git submodule, not by a package, not by the bootstrap script that exists specifically to do this. By `cp -r` from a sibling directory.

The bootstrap script only handles the global `~/.claude/` layer. Per-project stuff I've never automated, and I keep meaning to.

**8. Was there something you wanted to bring over and didn't? What stopped you?**

Yeah, the eval harness from the invoice project. It's the best thing I've built for this category of work and I use maybe a third of what it can do on any given project.

I didn't bring it because it's welded to that project's data model. Extracting it means either doing a proper generalization pass, which is half a day I wasn't going to bill anyone for, or copying it and mutilating it, which is how I ended up with three divergent copies of the chunking module. So I wrote a worse thing from scratch in an hour and told myself I'd fix it later. I did not fix it later.

**9. How long did the whole setup take end to end?**

Between forty minutes and an hour for the agent side alone, spread across the first day. Not one continuous block; it's more like I hit a wall, realize the agent doesn't know something, go add a paragraph to CLAUDE.md, continue. Then again two hours later.

That trickle is the actual cost and it's invisible because no single instance of it feels expensive.

**10. Has anything you copied ever gone stale or diverged from the original? What happened?**

The chunking module, and it cost me real money.

Same code in three projects. I fixed an off-by-one in the overlap logic in one of them, on a Friday, and it never got back to the other two. Six weeks later a client flagged that retrieval was returning fragments cut mid-sentence, which is exactly the bug I'd already fixed elsewhere and had zero memory of. I debugged it for three hours as if it were new before I opened the other repo and saw my own fix sitting there.

Same thing happens to CLAUDE.md, just less visibly. The version in project A says "use pytest fixtures, never module-level setup." Project B's copy predates that rule, so the agent happily writes module-level setup and I don't notice until review, and when I do notice I fix it in B and not in the template, so the next copy is wrong too. It's a loop.

---

#### C. The last time it didn't work

**11. Tell me about the last time you moved your setup to another machine, a container, a new laptop, or handed it to someone, and it didn't work. How did you find out? How long to fix?**

The Linux move I mentioned, plus a devcontainer one that was worse.

The devcontainer case: the container had Node 18, one of my MCP servers needs 20+. Server exits immediately on start. The failure mode is that the agent just doesn't have those tools and carries on without them, cheerfully, improvising with bash instead. I found out because it started writing curl commands against an API it should have had a proper tool for, and I sat there for a while thinking it was being weird before I checked the logs.

Detection took the longest, maybe twenty-five minutes of being confused. The fix was two minutes once I knew. That ratio is the whole problem: broken config doesn't announce itself, it degrades quietly.

**12. One-off, or does this happen?**

It happens. Not every time, but I'd say one in three fresh environments has something silently not loading. Paths, versions, a missing env var, an auth token that expired months ago and the server starts but every call 401s.

**13. Has a tool ever done something you didn't ask for, or ignored something you did ask for, and you only found out later?**

Both, repeatedly. The one that stung: a skill of mine had a formatting rule left over from a project that used Prettier with 120-char lines. Carried it into a repo that uses Black at 88. Agent reformatted a big chunk of the codebase as a side effect of a small change, I didn't read the diff carefully because it was "just a small change," and I pushed 1,100 lines of noise into a branch a colleague was reviewing.

The ignoring is more common and less dramatic. CLAUDE.md says don't touch migrations without asking. It touches migrations. Not always, and I've never worked out the pattern. My honest suspicion is that when the file gets long, the middle of it stops mattering, but I've never actually tested that; it's a story I tell myself.

**14. How did you notice? What should have happened instead?**

Noticed in the PR diff, from someone else's comment, which is the worst way. What should have happened: the rule that got applied should have been traceable. I want to be able to ask, after the fact, which instruction produced that behaviour. Right now I can't, so I guess, and my guesses are unfalsifiable.

**15. When it happened, did you already have the collection, or were you setting up one thing?**

Already had the collection, and that's the point. When it was one file I knew what was in it. At forty files with overlapping instructions I have no working model of what's active on a given run. The collection created the problem.

---

#### D. The material itself

**16. Is there anything in that folder you're not sure actually does anything?**

Maybe half of it, if you want the real answer.

Specific examples: I have a skill about error handling conventions that I wrote in one sitting nine months ago, and I've never once seen output I could attribute to it. A CLAUDE.md section about preferring composition over inheritance which reads like something I'd say in an interview rather than something that changes behaviour. Two MCP servers in the config that I'm fairly sure haven't been called this year.

**17. How would you know whether it works? Have you ever checked?**

Properly, no. I've never A/B'd anything.

What I could do is obvious in principle: same task, same repo state, run it with the file and without, compare. It's not hard. I've never done it because each individual file feels too small to justify the ceremony, and it's forty small things, so the total never gets audited.

The closest I've come was accidental. I once had a run where the config didn't load, and the output was noticeably worse in a way I could point at, which told me *something* in there works. It didn't tell me which part.

**18. Is there anything in there you'd delete, honestly?**

The Aider config, gone, I don't use it. The composition-over-inheritance paragraph. Probably three of the eleven skills, and I could name two of them right now.

What stops me isn't sentiment, it's that deleting feels riskier than keeping. If I remove something and quality drops, I won't connect the two events; the feedback is too slow and too noisy. So the folder only grows, which is a bad property for a thing whose job is to be precise.

**19. When you go into that folder, what are you usually about to do?**

Three modes, in descending frequency. Most often I'm copying something out of it into a new project. Second, I'm adding a rule right after the agent did something annoying, which means most edits are written while irritated, which is probably visible in the tone of some of them. Third, and rarest, I'm looking for something I know I wrote and can't find; that's usually a prompt, and it usually takes longer than rewriting it would.

I basically never go in there to read or review. There's no reason to, nothing prompts it, so it doesn't happen.

**20. If you were picking something of your own to reuse and couldn't remember which parts were good, what would help you decide?**

Usage data, first. Just: this file was loaded in 40 sessions, this one in 2, this one never. That alone would let me delete half of it with confidence.

After that, some record of when a rule got applied and what it changed. Not full traces, I don't want to read logs. Something more like: here's where this instruction actually affected output.

And a date. Not created-date, last-actually-useful date. If a skill hasn't influenced anything in four months it's either dead or it's a rule I've internalized and no longer need written down. Either way I want to know.

---

#### E. Other people

**21. Has anyone else ever opened or run your setup? Who, and how did it go?**

Once, properly. A contractor I brought onto a project last winter. I gave him the repo including the agent config, and he got roughly the same experience as my Linux move: paths broken, one server not starting, and he assumed that was normal and worked around it for two days without mentioning it. I found out during a call when he described a workflow that made no sense unless he was missing half his tools.

That was the moment I understood the config had become tribal knowledge rather than a setup.

**22. Have you ever given this material to someone, a colleague, a friend, publicly? What did you have to explain?**

Twice, both informally, both to people I know.

What I had to explain: which files are load-bearing and which are aspirational. Which rules are real constraints from the client versus my personal taste. Why there are two CLAUDE.md templates that look almost identical, where the difference is a single paragraph and the reason is a project from a year ago that no longer exists.

None of that is written down anywhere, so the explanation is me, on a call, for twenty minutes.

**23. Is any of it public? Would you want it to be?**

None of it. I'd like a slice of it public, mostly for the reason that publishing forces cleanup and I need external pressure to do that. But I can't publish as-is because client-specific rules are scattered through it, some naming conventions I shouldn't share, one file that has an internal API shape in an example. Separating that is a couple of hours of careful work and it's never the most urgent couple of hours.

**24. Have you ever filed an issue or written publicly about any of this?**

One issue, about MCP config path handling, which is the thing that burned me on Linux. Got a reasonable answer, not much came of it.

Written about it, no. I've drafted a post twice about how these config folders rot and deleted it both times because it felt like complaining without a solution.

---

#### F. Closing

**25. If a genie fixed exactly one thing tomorrow, what would you assign it?**

Show me what actually loaded and what actually mattered. Per session: these files were read, this rule fired here, these six things were present and had no observable effect. That's it. I don't need it to fix anything, I need to see it, because everything else I'd fix myself in an afternoon if I could see it.

**> Have you ever gone looking for something that does that?**

Yeah, twice, both times right after being burned.

**> Did you find anything? Did you keep using it?**

Sort of and no. There are session viewers and log tools, and they tell you what happened in the conversation, which isn't the same question. I want to know which of *my* files was responsible, and nothing I found connects a behaviour back to a config line. I used one for about a week, mostly to look at token counts, then stopped, and I couldn't tell you the exact day I stopped.

**26. Anything I should have asked and didn't?**

Two things.

You didn't ask what happens when a rule and a client requirement conflict. That comes up constantly. My CLAUDE.md says one thing, the client's linter says another, and there's no precedence anywhere; it's resolved by whichever I remember at the time, which is a bad way to resolve anything.

And you didn't ask about the boundary between what lives in these files and what lives in my head. Roughly half of what makes a project go well is stuff I've never written down because writing it down felt too obvious. Then a contractor joins and none of it transfers. If you're studying why these setups fail, "the written part was never the whole thing" is probably a bigger factor than anything about the files themselves.
