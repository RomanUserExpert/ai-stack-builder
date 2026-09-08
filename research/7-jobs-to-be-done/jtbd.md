# Jobs to be done — one main job, four on the way to it

> **PROVISIONAL.** Written 2026-09-08, stage 7 steps 1–4, from
> [`6-personas/personas.md`](../6-personas/personas.md) and the register and axes in
> [`6-personas/inventory.md`](../6-personas/inventory.md). **The matrix (step 5), the audit (step 6)
> and the reconciliation with the spec (step 7) are not in this file yet.** The label lifts on the
> same event as stage 6's: **five practitioner conversations** run against
> [`interview-guide.md`](../6-personas/interview-guide.md) and filed as source documents. **One has
> happened.**

**Three marks**, per [`research.md`](../research.md), *The three marks*: **`✓`** another person can
re-run the instrument · **`*`** a practitioner said it in an interview, from memory, about their own
work — **n = 1 everywhere in this file** · **`[?]`** unknown. **A `*` never becomes a `✓` by
repetition**, and **a re-runnable query proves that something was *said*, not that it is *true***
(rule 5).

**The rule this stage lives or dies by.** A job survives a change of product; a feature does not.
*"I want a price filter"* is a feature, *"I want to discard what I cannot afford, fast"* is a job.
The specific way it goes wrong **here** is not inventing jobs but **laundering the specification into
job form** — [`CLAUDE.md`](../../CLAUDE.md) already names four surfaces and all the mechanics, so a
sentence like *"when my set is complete, I want the system to run a validation pass"* would be §6
with a *when* in front of it, and the whole stage would confirm the spec by construction. **Step 4
below is the pass that catches it, and the corrections are shown rather than silently made.**

**Where the jobs came from.** Every job names its persona and its evidence. **A job whose evidence
is one person's aside, or nothing at all, is not in the main list** — it is in *Hypotheses* at the
end, written as *we assume X; we would check it by Y*. That is why the main list has four related
jobs and the hypothesis list has seven.

---

# 1. The main job

## The candidates, and what each stands on

| # | Candidate, in the canonical form | Grew from | Standing |
|---|---|---|---|
| **A** | *When the same rules have to apply in more than one place, I want to keep one copy of them and have every place follow it, so that I stop maintaining the same thing three times over.* | P1, P2 · [#6235](https://github.com/anthropics/claude-code/issues/6235) **6,592 reactions** and a twelve-issue family across three vendors' trackers; [#20697](https://github.com/anthropics/claude-code/issues/20697) 161 — *"manually copy skills to both locations"*; **25 HN comments** about symlinking one source into several formats | **`✓`, and the loudest thing in the entire evidence base** |
| **B** | *When I move a working setup to another machine or container, I want it to behave there the way it behaved here, so that I do not spend the first hour finding out what silently did not load.* | P1, P2 · [mcp/servers #64](https://github.com/modelcontextprotocol/servers/issues/64) **182**; [codex #13386](https://github.com/openai/codex/issues/13386) — silent truncation *"with no warning anywhere"*; [#9716](https://github.com/anthropics/claude-code/issues/9716) 75 · `*` [interview Q5, Q11](../6-personas/agent-setup-interview.md) | **`✓` + `*`** |
| **C** | *When I start something new, I want the pieces I already trust to be in it without me carrying them across by hand, so that the beginning costs minutes instead of an afternoon.* | P1 · [#9444](https://github.com/anthropics/claude-code/issues/9444) 48 — *"copies can drift out of sync"*; [codex #17401](https://github.com/openai/codex/issues/17401) 21 — *"no modular reuse across projects… 10+ repos"* · `*` [interview Q4, Q6, Q9](../6-personas/agent-setup-interview.md) | **`✓` filed, `[?]` as a driver of adoption** — this is Q5 |
| **D** | *When I need something I made months ago, I want to lay hands on it and know it still does what I think it does, so that I stop rebuilding what I already have.* | P1 · `*` [interview Q19](../6-personas/agent-setup-interview.md) — *"it usually takes longer than rewriting it would"* | **`[?]`.** One sighting, ever. Loss has no evidence in any instrument tried |
| **E** | *When I have been accumulating rules and instructions for months, I want to know which of them has actually changed anything, so that I can throw away what does not earn its place instead of keeping all of it.* | P1 · `✓` widespread public doubt (R7) · `*` [interview Q16, Q17, Q25](../6-personas/agent-setup-interview.md) | **`✓` + `*` — and it is a rival, not a step. See below** |

**A and B are one job seen along two axes**, and those are exactly the axes the personas split on
([`inventory.md`](../6-personas/inventory.md) §D): **X2** — the same material has to serve two to four
tools — and **X1** — the same material has to survive somebody else opening it. In both, *what I made
here has to work there.* **C is the same job at the moment a project begins**: copying `CLAUDE.md`
into a fourth project is that material having to live somewhere else. So A, B and C merge, and the
merge is the main job.

## The main job

> ## When something I have already got working has to live somewhere else — a second tool, a new machine, a container, a colleague's laptop — I want it to keep working there without me rediscovering everything it quietly depended on, so that the move costs me minutes instead of an afternoon of finding out what silently did not load.

**Persona.** **P1, the keeper who runs several agents** — primary
([`personas.md`](../6-personas/personas.md)). **P2, the receiver**, is on the other end of the same
sentence, which is why P2 exists as a persona rather than as a moment.

**Grew from.**
- `✓` [#6235](https://github.com/anthropics/claude-code/issues/6235) — **6,592 reactions, 389 comments**, and its stated motive is *"it doesn't work as well when collaborating with other developers who aren't using Claude Code"* — [`re-research.md`](../6-personas/re-research.md) R1, NK-5.
- `✓` [mcp/servers #64](https://github.com/modelcontextprotocol/servers/issues/64) — **182 reactions, 91 comments** — over a top-of-tracker of `npx` failures, processes dying at startup, path casing — [`user-pain.md`](../3-pain/user-pain.md) finding 1.
- `✓` [#9444](https://github.com/anthropics/claude-code/issues/9444) 48 and [codex #17401](https://github.com/openai/codex/issues/17401) 21 — the reassembly half, filed as feature requests, which is why a bug-shaped search missed it — R3.
- `✓` **25 HN comments** on symlinking one source into many formats; the reported workarounds are a symlink, an include line, a wrapper script — R2.
- `*` [interview Q5](../6-personas/agent-setup-interview.md) — four MCP servers silently not starting on Linux, twenty minutes spent believing *the model had gotten worse*; [Q11](../6-personas/agent-setup-interview.md) — Node 18 against a server needing 20+, *"broken config doesn't announce itself, **it degrades quietly**"*.
- `✓` `V` [`benchmark.md`](../4-benchmark/benchmark.md) — **B4, produce an artefact and hand it over, is the weakest flow in the industry, nobody above 4**, because no product has a surface that says anything about the machine its artefact lands on.

**Standing. `✓` + `*`.** Both instrument families point at it, and the two loudest numbers in the
repository — 6,592 and 182 — are both inside it.

**It passes the three tests.** It names no mechanism and no surface. It survives a change of product:
a symlink farm, a dotfiles repo, a package manager and a hand-written bootstrap script all close it
today, badly ([`re-research.md`](../6-personas/re-research.md) R2, R8). It starts from a situation
rather than from a wish.

## Where this differs from what the specification says

[`CLAUDE.md`](../../CLAUDE.md) §2 words the product's value as **assembly with validation** and says
the wow moment is **the export**. The main job above is a **transfer** job: assembly is what you do
in order to move something, and the check is how you find out before the move rather than after.

**That is a difference of emphasis, not a contradiction, and it is not applied to the spec.**
Stated once, plainly, as the plan requires: *§2 says the value is putting a set together correctly;
the evidence says the value is that the set still works after it leaves.* The second contains the
first — a set that does not cohere will not survive the move — but it puts the weight on the far
side of the handover, which is where `CLAUDE.md` §6's own decision about `SETUP.md` already went.

**Which digest hypothesis this supports.** [`research.md`](../research.md) §5: it supports **G1's**
*reassembly over loss* half — reassembly is inside the main job with filed evidence behind it, loss
is candidate D with one sighting. It **does not settle G9** — whether silent breakage retains rather
than acquires is the same unanswered question as Q5, and no job formulation closes it.

## The second candidate survived, and the lesson's rule says what that means

**Candidate E did not fold into the main job.** *Knowing whether any of my material does anything* is
not a step on the way to *making it work somewhere else* — you could close one perfectly and leave the
other untouched. Both have `✓` and `*` behind them.

> **"If two main jobs survive, you have two products."**

**So this is recorded, not resolved.** It is already **Q12** in
[`research-plan.md`](../research-plan.md) — *is the wanted thing observability of what ran rather than
validation that a set coheres* — raised by the first interview, standing on one person, **and it is
the one we cannot build**: `CLAUDE.md` §6 runs nothing on anyone's machine. The instrument is guide
Q25 asked four more times, before the product is ever described.

**What tips it.** If four more practitioners answer the genie question with *show me what ran*, the
main job above stays true and stops being the one that matters most — and §2's core-value sentence
is the thing that has to change, not §8's surfaces.

---

# 2. Related jobs — four, on the way to the main one

Each is a step someone has to complete before the main job is done. Each names its persona, its
evidence and its standing. **Jobs that could not carry a source are not here** — see *Hypotheses*.

### RJ-1 · Know what the other side will still need, before I send it

> **When I am about to hand a working setup to another machine or another person, I want to know in
> advance what that side will still have to have, so that they do not find out by watching things
> quietly fail.**

**Persona.** P1 sending, P2 receiving.
**Grew from.** `*` [interview Q21](../6-personas/agent-setup-interview.md) — a contractor got the repo,
*"paths broken, one server not starting, and **he assumed that was normal and worked around it for
two days without mentioning it**"* · `✓` [#6235](https://github.com/anthropics/claude-code/issues/6235)
6,592, whose motive is collaboration across different tools · `V`
[`benchmark.md`](../4-benchmark/benchmark.md) B4 — **fifteen products, none above 4**, and not one
cell scores what a product says about the machine its artefact lands on.
**Standing.** `✓` that the need exists and is unserved; `*` for what it costs when it fails, n = 1.

### RJ-2 · Find out what my pieces drag in, and where two of them will fight, while I can still act

> **When I put together the pieces a project needs, I want to learn now what else has to come with
> them and where two of them will quietly fight over the same thing, so that I do not learn it three
> days later from an agent behaving strangely.**

**Persona.** P1.
**Grew from.** `✓` [mcp/servers #1219](https://github.com/modelcontextprotocol/servers/issues/1219),
13 reactions — *"the chat always chooses the first one specified in order of `mcp.json`"*: **the first
one wins and nobody is told**, our own thesis sighted in the wild in the exact file we generate · `✓`
the quieter family of *I set it and it was ignored* — [continue #8484](https://github.com/continuedev/continue/issues/8484)
6, [#4306](https://github.com/continuedev/continue/issues/4306) 3, and four more at 0–2 (OBS-17) ·
`*` [interview Q13](../6-personas/agent-setup-interview.md) — a formatting rule carried in from another
project reformatted a codebase as a side effect, **1,100 lines of noise pushed into a colleague's
review branch**.
**Standing.** `✓` + `*`. **And the honest weighting: 13 against 182.** This is real and it is quiet —
a reaction count is ordinal, so *quieter* is all it says, but it says that clearly.

### RJ-3 · Fix something once and have the fix reach every copy of it

> **When the same thing exists in several projects and I correct it in one of them, I want the
> correction to reach the others, so that I do not pay for the same mistake a second time months
> later.**

**Persona.** P1.
**Grew from.** `✓` [#9444](https://github.com/anthropics/claude-code/issues/9444), 48 reactions —
*"file duplication… maintenance burden… **inconsistency risk — copies can drift out of sync**"* · `*`
[interview Q10](../6-personas/agent-setup-interview.md) — the same off-by-one fixed on a Friday in one
of three projects, **found six weeks later by a client**, three hours of debugging a bug he had
already fixed elsewhere; and the same loop in the instruction files, *"so the next copy is wrong too.
**It's a loop.**"* · `✓` [`competitors.md`](../1-landscape/competitors.md) — the same failure named as
Backstage's known one, cited as corroboration and not as a measurement.
**Standing.** `✓` + `*`. This is the best-evidenced job in the file after the main one — NK-14.

### RJ-4 · Move my work without moving my secrets or my client's business with it

> **When I take something from one place to another, I want my keys and the parts that belong to a
> particular client to stay behind, so that I am never the reason something private turns up
> somewhere it should not be.**

**Persona.** P1 moving, P2 receiving.
**Grew from.** `✓` and heavier than stage 3 found:
[#32733](https://github.com/anthropics/claude-code/issues/32733) 192 ·
[#401](https://github.com/anthropics/claude-code/issues/401) 54 — *"Claude loads my project's `.env`
into its bash environment"* · [#29910](https://github.com/anthropics/claude-code/issues/29910) 45 ·
[continue #1729](https://github.com/continuedev/continue/issues/1729) 32 — *"storing api keys in plain
text"* · [mcp/servers #1018](https://github.com/modelcontextprotocol/servers/issues/1018) 23 ·
[#754](https://github.com/modelcontextprotocol/servers/issues/754) 22 — R6, OBS-18, OBS-21 · `*`
[interview Q23](../6-personas/agent-setup-interview.md) — he cannot share any of it because
*"client-specific rules are scattered through it… one file that has an internal API shape in an
example"*, and separating them is **a couple of hours that are never the most urgent couple of
hours**.
**Standing.** `✓` + `*`. Note what the `*` adds that no count could: the blocker is not *encrypting*
anything, it is that **the private and the reusable are tangled in the same files.**

---

# 3. Emotional jobs

How the person wants to feel. Kept separate from the functional list on purpose, and each one is
sourced or it is not here.

### EJ-1 · Not be quietly overruled by my own tools

> **When a tool makes a choice I did not make, I want it to tell me it made one, so that I am not
> left inventing theories about why my own setup behaves the way it does.**

`✓` [#20412](https://github.com/anthropics/claude-code/issues/20412), **142 reactions** — servers
*"silently synced… **without any opt-in, notification, or consent**"* · `✓`
[codex #13386](https://github.com/openai/codex/issues/13386) — instructions past 32 KB *"dropped and
never sent to the model — **with no warning anywhere**"* · `✓` #1219 — the first one wins · `*`
[interview Q13](../6-personas/agent-setup-interview.md) — *"it touches migrations. Not always, and
I've never worked out the pattern. My honest suspicion is… **but I've never actually tested that;
it's a story I tell myself.**"*
**Standing.** `✓` + `*`. The strongest emotional job in the file, and the one OBS-23 already named.

### EJ-2 · Believe that a clean result was actually earned

> **When I am told everything is fine, I want to know that something was genuinely looked at, so that
> I am not carrying a private suspicion that the reassurance is decoration.**

`✓` [bandrami](https://news.ycombinator.com/item?id=46820441) — *"**Blackbox oracles make bad
workflows, and tend to produce a whole lot of cargo culting.** It's this kind of opacity… that makes
me [wary]"* · `✓` [Alpha_Logic](https://news.ycombinator.com/item?id=46106973) — *"until we have
deterministic introspection for LLMs, **engineers will always invent weird heuristics to detect
drift**"* · `E` OBS-32 — the nearest dead competitor filed **a block that failed to resolve** as
`fatal: false`, so a missing dependency degraded the result quietly.
**Standing.** `✓`. The inference that this is what a person *feels* is ours, `R` — but the quotes are
about opacity and trust, not about mechanics.

### EJ-3 · Stop suspecting that half of what I keep is dead weight

> **When I have been adding to something for over a year, I want to stop suspecting that most of it
> does nothing, so that I can keep it because it works rather than because I am afraid to remove it.**

`✓` R7 — *"mostly useless… **50/50 or less** that Claude.md even reads/uses this file"*
([saberience](https://news.ycombinator.com/item?id=46106423)); *"I can never quite tell if it's
helping anything"* ([eternityforest](https://news.ycombinator.com/item?id=48638003)); an entire story
titled *[I am morally opposed to updating my Claude.md](https://news.ycombinator.com/item?id=49376287)*
· `*` [interview Q16, Q18](../6-personas/agent-setup-interview.md) — *"maybe **half of it**, if you
want the real answer"*, and *"deleting feels riskier than keeping. If I remove something and quality
drops, I won't connect the two events… **so the folder only grows, which is a bad property for a
thing whose job is to be precise.**"*
**Standing.** `✓` + `*`. **This is the emotional face of main-job candidate E**, and it is the same
open question — Q12.

---

# 4. Social jobs

**Two, and thin on purpose.** This is a single-user desktop tool
([`CLAUDE.md`](../../CLAUDE.md) §9 — no accounts, no sync, no teams), and the population evidence for
a social layer is **an absence that was looked for twice**: 0 of 1,762 HN comments and two unrelated
issues for `portfolio in:title` ([`re-research.md`](../6-personas/re-research.md) R10). Inventing a
social layer to fill the template is what the plan told this stage not to do.

### SJ-1 · Not be the missing manual for my own work

> **When somebody else opens something I made, I want them to get moving without twenty minutes of me
> on a call, so that what I built is a setup rather than something only I know how to run.**

**Persona.** P1 as the author, P2 as the person opening it.
`*` [interview Q21](../6-personas/agent-setup-interview.md) — *"that was the moment I understood the
config had become **tribal knowledge rather than a setup**"* · `*`
[Q22](../6-personas/agent-setup-interview.md) — what he had to explain, twice, on a call: *"which
files are load-bearing and which are aspirational. Which rules are real constraints from the client
versus my personal taste… **None of that is written down anywhere.**"* · `✓` at population that other
people do open this material — [#6235](https://github.com/anthropics/claude-code/issues/6235) 6,592,
[#10238](https://github.com/anthropics/claude-code/issues/10238) 168 *"with my team"*,
[#28729](https://github.com/anthropics/claude-code/issues/28729) 151 *"multiple contributors"* — R12,
NK-7.
**Standing.** `✓` that the situation occurs; `*` for the feeling, **n = 1, and the receiver has never
been asked.**

### SJ-2 · Have something I would put my name to — **post-MVP**

> **When I think about showing my work, I want it to be in a state I would not have to apologise for,
> so that the prospect of being seen is a reason to tidy it rather than a reason to keep it hidden.**

`*` [interview Q23](../6-personas/agent-setup-interview.md) — *"I'd like a slice of it public, mostly
for the reason that **publishing forces cleanup and I need external pressure to do that**"* · `✓` the
**absence**, searched for deliberately in two instruments and not found — R10, NK-18.
**Standing.** `✓` and `*` **disagree, and both stay** (rule 4). The `*` reframes rather than
contradicts: the want is **not to be seen; it is a forcing function for cleanup.** **Out of scope
either way** — `CLAUDE.md` §9 keeps publishing out of the MVP and there is no server to publish to.
Listed so that the matrix can show it closes nothing *now* without pretending it does not exist.

---

# 5. The feature-name test — what was rewritten

Step 4 of the plan: a pass over every *I want* clause for vocabulary from `CLAUDE.md` §4, mechanisms
from §6 and surfaces from §8. **The laundering is shown rather than silently fixed**, because seeing
what it looked like is the only way to keep catching it.

| Written first — and wrong | Why it fails | Rewritten as |
|---|---|---|
| *When my set is complete, I want the system to run a validation pass, so that I see Problems and Notes* | Names a mechanism (§6) **and** our severities. It is §6 with a *when* in front of it | **RJ-2** — *learn now what else has to come with them and where two of them will quietly fight* |
| *I want the archive to carry a `SETUP.md` the receiving agent can read* | Names an artefact (§6) and decides its form | **RJ-1** — *know in advance what that side will still have to have* |
| *I want to detach an item in a project and edit it there* | Two mechanisms (§5, §7) and a §4 noun | **H-J3**, and it went to *Hypotheses*, because its evidence is one aside |
| *I want the public library to give me items on the first run* | A surface (§8) and a decision (§11) | **H-J4** — *get moving with material I did not write* |
| *I want usage facts on the item card — used in 3 projects* | A mechanism (§5) and a §4 noun | **EJ-3** and **H-J1** — *keep it because it works rather than because I am afraid to remove it* |
| *I want to pick an agent target before exporting* | A control (§6) | Absorbed into the **main job** — *a second tool* |

**The check, re-run over this file.** No *I want* clause contains: *item · project · library ·
workspace · stack · validation pass · check · run · problem · note · skipped · palette · detach ·
promote · public library · setup.md · .env.example · target · export · archive*. The word *archive*
survives nowhere in a motivation; **it appears in RJ-1's *when* clause in its ordinary English sense
and nowhere else**, and *export* appears only in this table.

---

# 6. Hypotheses — the jobs that did not earn the main list

Written in the plan's required form. **None of these may be cited as a finding**, and none may be used
to add or remove anything from the specification.

| # | We assume | Persona | What it stands on today | We would check it by |
|---|---|---|---|---|
| **H-J1** | *When I half-remember something I wrote, I want to lay hands on it quickly, so that I stop rewriting things I already own.* | P1 | `*` one sighting, [interview Q19](../6-personas/agent-setup-interview.md) — *"it usually takes longer than rewriting it would"*. **The only sighting of loss anywhere in the repository**, and the trackers are blind to it by construction | Guide Q19, four more times. It is also main-job candidate D, and it is half of Q5 |
| **H-J2** | *When a new piece of work resembles one I have done, I want to start from that one and re-tune it, so that I am not starting from nothing.* | P1 | `[?]` — `CLAUDE.md` §2 names it as a supporting moment; nobody has said it. The nearest thing is `*` [Q8](../6-personas/agent-setup-interview.md), where the thing he wanted back was **welded to its project** and he wrote a worse one instead | Guide Q8, four more times — NK-8 |
| **H-J3** | *When one project needs a version of something the others must not get, I want to change it there only, so that one exception does not become everybody's problem.* | P1 | `*` one aside, [Q26](../6-personas/agent-setup-interview.md) — *"my CLAUDE.md says one thing, the client's linter says another, and **there's no precedence anywhere**"* · `M` flow 05, a mechanism captured from Figma, which is evidence of what a product chose | The remaining four conversations, asked as a situation. This is **Q10** in the register — NK-21 |
| **H-J4** | *When I have nothing of my own yet, I want to get moving with material somebody else made, so that I am not staring at an empty room.* | **P3** | **`[?]` entirely.** What exists is `V`: an installer tool category at 425–4,526★ (R8) and catalogs reporting six- and seven-figure counts (R9), **all of it vendors' and tools' own numbers, and not one person observed** | The guide's **P5 recruit** — someone who does not keep this material at all. **Not yet found.** This is **Q9**, and it is the job two specified surfaces already assume |
| **H-J5** | *When I depend on something I cannot see working, I want to watch what it actually did, so that I stop guessing.* | P1 | `✓` + `*` — **and this is main-job candidate E, which survived.** It is in this table not because it is weak but because **we cannot close it**: §6 runs nothing on anyone's machine | Guide Q25, four more times, asked before the product is described. **Q12** |
| **H-J6** | *When my work is good, I want it to count as something I can show, so that the effort is visible outside the projects it went into.* | P1 | `*` one answer, and it **reframes**: publishing wanted as a **forcing function for cleanup**, not for being seen · `✓` the absence, searched twice | Guide Q23, four more times. **Post-MVP either way** — §9 |
| **H-J7** | *When what I have written down is only half of what makes the work go well, I want the unwritten half to travel too, so that handing something over is not a twenty-minute call.* | P2 | `*` one answer, [Q26](../6-personas/agent-setup-interview.md) — *"roughly **half** of what makes a project go well is stuff I've never written down"*. **If it holds, it bounds the ceiling of the entire product**, because we validate the written part | The four remaining conversations, plus the NK-13 test. This is **Q11** — NK-22 |

---

# 7. What this hands forward

1. **To step 5, the matrix.** Rows are the jobs above; columns are P1, P2, P3; cells are 1–3 **with a source, or `[?]` — never an averaged 2**. Two more columns: which specified feature closes the job (or *nothing*, which is the interesting answer), and which of the fifteen competitors closes it as against merely selling against it. **The prediction to test rather than assume:** the evidenced rows will be exactly the ones the trackers can see, and **P3's column will be almost entirely `[?]`** — which is a fact about our instruments, not about that person.
2. **To the register.** Nothing new. The main job's rival is **Q12**; H-J3 is **Q10**; H-J7 is **Q11**; H-J1 and H-J2 are **Q5** and **Q7**; H-J4 is **Q9**.
3. **To the interview guide.** Three questions come out of this stage for step 6 to merge, and they are already implied above: the genie question asked four more times before any description of the product (Q12); *what happened the last time your own rule and the project's tooling disagreed* (Q10); and one that does not exist in the guide yet — **ask a receiver**, not an author, because every line about P2 is currently somebody else's account of them.
4. **Not to `CLAUDE.md`.** Nothing here is applied. **No feature is removed by this stage**, and the difference of emphasis between §2's *assembly with validation* and this file's *transfer* main job is stated once, above, as a difference — not as a correction.
