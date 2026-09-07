# Interview guide — the instrument for the five conversations

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

## 1. The one thing this instrument exists to do

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

## 2. Who to talk to — and how not to select the answer

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

## 3. Six rules, and the first two are the whole method

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

## 4. The thirty minutes

Times are a budget, not a script. If block B or C opens up, spend the time and cut block E.

### A. Setup census — 4 min
*Answers: NK-4, NK-2, NK-3, NK-5 confirm, NK-16*

1. *"Which coding agents do you have installed right now?"* → then: *"Which did you use yesterday?"*
   — installed and used are different numbers; write both down.
2. *"When did you last open any of them?"* — never *"how often do you use it"*. **(NK-4)**
3. *"Do you have a file, folder or repo where you keep instructions, rules, prompts or skills for
   them? Where is it?"* → *"Can you say roughly how many things are in it?"* **(NK-2)**
4. *"How long has that existed? What was in it when you started?"* **(NK-3 — the only route to
   growth rate, and it is a memory, so treat it as soft)**
5. *"Did you set it up on more than one machine? What happened?"*

### B. The last new project — 7 min
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

### C. The last time it did not work — 7 min
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

### D. The material itself — 6 min
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

### E. Other people — 4 min
*Answers: NK-7, NK-18, NK-16*

21. *"Has anyone else ever opened or run your setup? Who, and what happened?"* **(NK-7 — §6's
    *"their own machine, only party at risk"* rests on the answer)**
22. *"Have you ever given this material to somebody — a colleague, a friend, publicly?"* → if yes:
    *"what did you have to explain to them?"*
23. *"Is any of it public? Would you want it to be?"* **(NK-18 — the row that came back empty from
    every search. Ask it plainly and record a plain no as a real answer.)**
24. *"Have you ever filed an issue or posted publicly about any of this?"* **(NK-16)**

### F. Close — 2 min
*Answers: NK-9*

25. **"If a genie fixed exactly one thing about all of this tomorrow, what would you have it fix?"**
    → then the important half: *"and have you ever gone looking for something that does that?"* →
    *"did you find anything? did you keep using it?"* **(NK-9, and it is the only read we get on
    non-adoption: people who searched, found something, and stopped using it.)**
26. *"Is there anything I should have asked and didn't?"*

---

## 5. The three register questions, and how the sheet answers them

The guide is not organised by register question, because a person cannot be interviewed by
register question. This is the mapping used when the five sheets are read together.

| | Question | What in the sheet answers it |
|---|---|---|
| **Q5** | Loss, reassembly cost, or breakage — which drives adoption? | Q6–Q9 against Q11–Q12, plus Q25's *did you go looking*. **Loss has no evidence in any instrument so far** — if nobody in five raises *I couldn't find something I'd written*, that is a real result and must be written down as one, not glossed over. |
| **Q7** | Who is the primary persona — the one whose pain is *sighted* (breaks at handover) or the *collector* §3 describes? | **The block B / block C marks in §4C.** Five rows, joined per person. If both land on the same people, we have one persona and the spec's framing survives. If they split, we have two and the primary must be argued. |
| **Q8** | Is the main job *assemble a set that holds together* or *hand a set to a machine and have it run first time*? | Q6 and Q11 told as stories, plus Q25. **The lesson's rule applies: if both survive, that is two products, and it goes back to the register as a finding rather than being resolved by taste.** |
| **Q9** | Which specified features close no evidenced job? | Q8 (duplicate/promote), Q20 (usage facts), Q21–Q23 (visibility, publishing), Q3 and Q16 (a public shelf, if they raise installing other people's material unprompted). **Absence in five conversations is not grounds to cut a feature** — it is grounds for a register entry saying so. |

---

## 6. Words never to say

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

## 7. The one place a description is allowed

**After question 26 and not before.** If you want a reaction, describe it in one sentence with no
vocabulary from §6 — *"a place to keep this stuff and put a set of it together for a project, that
tells you if the set won't work before you hand it over"* — and then **write down the first thing
they say and stop talking.** Their first sentence is data. The conversation after it is not, and
nothing said after this point may be used to source a persona block. Mark it on the sheet as
**post-disclosure**.

---

## 8. Coverage — every open row, and where it is asked

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

## 9. What to write down, and how to file it

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

## 10. What this instrument still cannot do

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
