# Jobs to be done — one main job, four on the way to it

> **There is a page.** [`../6-personas/personas.html`](../6-personas/personas.html) renders the
> hierarchy and the matrix beside the personas they came from, with every mark visible. **This
> markdown is the source; the page is the read.**

> **PROVISIONAL.** Written 2026-09-08, stage 7 **steps 1 to 5**, from
> [`6-personas/personas.md`](../6-personas/personas.md) and the register and axes in
> [`6-personas/inventory.md`](../6-personas/inventory.md). **Audited and reconciled 2026-09-09.**
> Step 6 is [`personas-and-jobs-critique.md`](../personas-and-jobs-critique.md), written against this
> file and **now applied to it** — every change is listed in §11. Step 7 is §12: what this stage
> proposes to the specification, handed to the register rather than written into `CLAUDE.md`. The
> label lifts on the same event as stage 6's: **five practitioner conversations** run against
> [`interview-guide.md`](../6-personas/interview-guide.md) and filed as source documents. **One has
> happened.**

> **What the audit did to the matrix, before you read it.** It **removed evidence, it did not add
> any**. Two cells lost their numbers outright and four were lowered, because they held an importance
> the evidence under them did not carry. **The consequence lands on §8**: the *core three* was
> announced as a rule applied mechanically, and after the audit the rule selects **one** buildable
> job rather than three. §8 now says so. The only cell in the whole matrix that gained evidence is
> **H-J4's P3**, from [`re-research-2.md`](../6-personas/re-research-2.md) Q-E — **and the evidence
> runs against the feature.**

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
with a *when* in front of it, and the whole stage would confirm the spec by construction. **§5
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

**Standing. `✓` + `*`.** Both instrument families point at it, and **the loudest number in the whole
evidence base — 6,592 — sits inside it**, as does the 182 that stage 3 called the loudest pain in the
ecosystem. **Corrected 2026-09-08:** this sentence said *the two loudest numbers*, which the audit
refuted — 182 is not second, and 1,416, 624, 472, 446 and 245 all sit above it
([`personas-and-jobs-critique.md`](../personas-and-jobs-critique.md), J-14).

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
[`benchmark.md`](../4-benchmark/benchmark.md) B4 — **four cells, none above 4** (the benchmark scored
15 cells across four flows, drawn from ten products; B4 holds four of them), and not one cell scores
what a product says about the machine its artefact lands on. **Corrected 2026-09-09** — this read
*fifteen products* (J-24).
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
**It's a loop.**"* · [`competitors.md`](../1-landscape/competitors.md) — the same failure named as
Backstage's known one, **cited unmarked**: [`inventory.md`](../6-personas/inventory.md) NK-14 withdrew
the `✓` from this source on 2026-09-08 — *our own stage-1 write-up of community lore about somebody
else's product; it corroborates and it measures nothing* — and this file had restored the mark the
register removed. **Corrected 2026-09-09** (J-32).
**Standing.** `✓` + `*` — one filed request at 48 with a `*` price tag on it. **The importance it
earns is 2 and not 3** (§7, J-66): the respondent lost three hours to the drift and **still moves
material by `cp -r`** (Q7), which is not the behaviour of a person about to change how they work.

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
promote · public library · setup.md · .env.example · target · export · archive*. **The word *archive*
appears in no job**; in this file it occurs only in this table and in this paragraph. **The word
*export* appears in no job either** — it occurs in this table, in §1, and three times in the matrix's
feature column, where it names our own mechanism and is supposed to. **Corrected 2026-09-09**: this
paragraph used to place *archive* in RJ-1's *when* clause, where it does not appear, and to say
*export* occurs only here (J-51, J-52).

---

# 6. Hypotheses — the jobs that did not earn the main list

Written in the plan's required form. **None of these may be cited as a finding**, and none may be used
to add or remove anything from the specification.

| # | We assume | Persona | What it stands on today | We would check it by |
|---|---|---|---|---|
| **H-J1** | *When I half-remember something I wrote, I want to lay hands on it quickly, so that I stop rewriting things I already own.* | P1 | `*` one sighting, [interview Q19](../6-personas/agent-setup-interview.md) — *"it usually takes longer than rewriting it would"*. **The only sighting of loss anywhere in the repository**, and the trackers are blind to it by construction | Guide Q19, four more times. It is also main-job candidate D, and it is half of Q5 |
| **H-J2** | *When a new piece of work resembles one I have done, I want to start from that one and re-tune it, so that I am not starting from nothing.* | P1 | `[?]` — `CLAUDE.md` §2 names it as a supporting moment; nobody has said it. The nearest thing is `*` [Q8](../6-personas/agent-setup-interview.md), where the thing he wanted back was **welded to its project** and he wrote a worse one instead | Guide Q8, four more times — NK-8 |
| **H-J3** | *When one project needs a version of something the others must not get, I want to change it there only, so that one exception does not become everybody's problem.* | P1 | `*` one aside, [Q26](../6-personas/agent-setup-interview.md) — *"my CLAUDE.md says one thing, the client's linter says another, and **there's no precedence anywhere**"* · `M` flow 05, a mechanism captured from Figma, which is evidence of what a product chose | The remaining four conversations, asked as a situation. This is **Q10** in the register — NK-21 |
| **H-J4** | *When I have nothing of my own yet, I want to get moving with material somebody else made, so that I am not staring at an empty room.* | **P3** | **No longer `[?]` in both directions — and what arrived runs against it.** Updated 2026-09-09 from [`re-research-2.md`](../6-personas/re-research-2.md) Q-E. **The supply is `✓` and enormous**: 19,703 repositories match `"claude skills"`, topped by curated collections at **74,686★**, 25,709★ and 15,006★ — against **93** public personal agent-material repositories. **The demand, from the first five practitioners ever observed on the question, is four refusals to one qualified yes**, and the yes was distributing **his own** material. What survived is *"a few established names"* — **provenance over volume** | The guide's **P5 recruit** — someone who does not keep this material at all. **Not yet found**, and four sceptics on Hacker News are not a market: that venue self-selects for people who already manage their own material, and no beginner was asked anything. This is **Q9**, and it is the job two specified surfaces already assume |
| **H-J5** | *When I depend on something I cannot see working, I want to watch what it actually did, so that I stop guessing.* | P1 | `✓` + `*` — **and this is main-job candidate E, which survived.** It is in this table not because it is weak but because **we cannot close it**: §6 runs nothing on anyone's machine | Guide Q25, four more times, asked before the product is described. **Q12** |
| **H-J6** | *When my work is good, I want it to count as something I can show, so that the effort is visible outside the projects it went into.* | P1 | `*` one answer, and it **reframes**: publishing wanted as a **forcing function for cleanup**, not for being seen · `✓` the absence, searched twice | Guide Q23, four more times. **Post-MVP either way** — §9 |
| **H-J7** | *When what I have written down is only half of what makes the work go well, I want the unwritten half to travel too, so that handing something over is not a twenty-minute call.* | P2 | `*` one answer, [Q26](../6-personas/agent-setup-interview.md) — *"roughly **half** of what makes a project go well is stuff I've never written down"*. **If it holds, it bounds the ceiling of the entire product**, because we validate the written part | The four remaining conversations, plus the NK-13 test. This is **Q11** — NK-22 |

---

# 7. The matrix — jobs against personas

**Stage 7, step 5.** Rows are the jobs above; columns are the three personas from
[`personas.md`](../6-personas/personas.md). **A cell holds an importance of 1–3 with the source of
that number, or `[?]`.** There is no averaging and no default: *an importance nobody has told us is
`[?]`, not 2*, because our only weighting is reaction counts on one kind of pain, and a middle value
would silently encode the instrument's blindness as a measurement.

**1** = it comes up · **2** = it costs them something · **3** = it is a reason they would change how
they work.

**And a reaction count is ordinal.** 6,592 against 13 says *louder*; it never says *five hundred
times more important*, and it says nothing at all about the pains no tracker can see. Every cell that
cites a count means *louder than*.

**Read the P2 and P3 columns before anything else.** P2 carries a number in three of ten rows —
**and after the audit all three are 2s, every one of them second-hand**, because only one issue's
stated motive speaks for receivers and **no receiver has ever been asked**. P3 carries a number in
none of the ten. That is a fact about our instruments rather than about those people — and it is the
most useful thing this matrix produces.

**Audited 2026-09-09, and the audit only ever subtracted.** Two cells lost their numbers — **RJ-1/P1**
and **EJ-2/P1** — because each held an importance on evidence the cell itself described as an
inference or as carrying no weighting, which is what the rule in the paragraph above forbids. Four
were lowered from 3 to 2 — **MAIN/P2**, **RJ-1/P2**, **RJ-3/P1**, **RJ-4/P1** — because a **3** means
*a reason they would change how they work*, and in each case the person on record demonstrably did
not: the one receiver worked around it for two days and said nothing; the one keeper still moves
material with `cp -r`; the one person afraid of leaking client material has never spent the couple of
hours it would take to separate it. Every changed cell names its audit ID. **One cell gained anything
at all — H-J4's P3 — and what it gained argues against the feature.**

## The sourced jobs

| Job | **P1** keeper · *primary* | **P2** receiver | **P3** empty-handed | Feature that closes it | Do competitors close it? |
|---|---|---|---|---|---|
| **MAIN — make it keep working somewhere else** | **3** — `✓` [#6235](https://github.com/anthropics/claude-code/issues/6235) **6,592**, the loudest demand anywhere in the base, and [#64](https://github.com/modelcontextprotocol/servers/issues/64) **182**, the loudest pain in the older corpus · `*` Q5, Q11 — twenty-five minutes to detect, two to fix | **2** — *lowered from 3, 2026-09-09, J-59.* `✓` #6235's stated motive **is** this job: *"it doesn't work as well when collaborating with developers who aren't using Claude Code"* — **but its filer is an author**, and the only receiver ever described *worked around it for two days without mentioning it*. That is *it costs them something*; it is not *a reason they would change how they work* · `*` Q21, **second-hand** | **`[?]`** — someone with nothing has nothing to move. Plausible is not evidence | **§6** — the agent target selector, `SETUP.md` written for the receiving agent, pinned `ref`s, target-correct paths · **§8** — the handover stages before Export | **No.** `V` [`benchmark.md`](../4-benchmark/benchmark.md) — **B4 is the weakest flow in the industry, nobody above 4**, and not one of fifteen cells scores what a product says about the machine its artefact lands on. Per-agent *output* exists (Ruler, `create-next-app`, flow 06) and skill managers **claim** per-agent sync in their READMEs (R8, unrun) — **the item-level half is contested, the set-level half is open** |
| **RJ-1 — know what the other side needs, before I send it** | **`[?]`** — *the number was withdrawn 2026-09-09, J-61.* The cell held a **2** on evidence it described in the same breath as an inference: `*` Q21 only, plus `V` the B4 gap. **He found out on a call and never said he wanted to know beforehand**, and the rule above says an importance nobody has told us is `[?]` | **2** — *lowered from 3, 2026-09-09, J-62.* `*` Q21: *"he assumed that was normal and **worked around it for two days without mentioning it**"* — two days lost is *it costs them something*, and **he changed nothing**, which is the opposite of a 3 · `✓` #6235's motive, filed by an author. **Second-hand — the contractor was never asked** | **`[?]`** | **§6** — `SETUP.md` per item in the resolved set, `.env.example`, pinned `ref`s · **§8** — the last stages of Run, read before the irreversible step | **No, and this is the clearest open cell in the matrix.** Nobody above 4 on B4, for a structural reason: no candidate has a surface that describes the receiving machine at all |
| **RJ-2 — what my pieces drag in, and where two will fight** | **2** — `✓` [#1219](https://github.com/modelcontextprotocol/servers/issues/1219) **13**, our own thesis sighted in the exact file we generate, plus the *set-and-ignored* family at 6, 3, 2, 0, 0, 0 (OBS-17) · `*` Q13 — 1,100 lines of noise into a colleague's branch. **13 against 182 is *quieter*, and that is all the count says** | **`[?]`** — a receiver does not assemble the set; whether they inherit its collisions is unestablished | **`[?]`** | **§6** — the dependency walk, `conflicts`, duplicate command names, same-target-path, cycles reported as information · **§8** — Run as a stage list | **Partly, and never for this material.** `E` the nearest dead competitor **computed the duplicate correctly and discarded the loser in silence** — `BlockDuplicationDetector`, then `mergeUnrolledAssistants`, no error, no warning (postmortem §5). `M` npm `ERESOLVE` and `terraform validate` do it excellently **in their own domains**. `V` `asm`'s README claims duplicate and near-duplicate audit and names *trigger collision* — unrun |
| **RJ-3 — fix it once and have the fix reach every copy** | **2** — *lowered from 3, 2026-09-09, J-66.* `✓` [#9444](https://github.com/anthropics/claude-code/issues/9444) **48**: *"maintenance burden… **inconsistency risk — copies can drift out of sync**"* · `*` Q10 — the same off-by-one fixed in one of three projects, **found six weeks later by a client, three hours to re-debug**. The price is real and the behaviour is not: **he still moves material by `cp -r`** (Q7) | **`[?]`** — whether a receiver cares about the author's other copies is unestablished | **`[?]`** | **§5** — an item lives in the library once and projects link to it **live**. The one mechanism in the spec that exists for exactly this job | **Solved elsewhere, dead here.** `M` Figma does it well for components, down to *423 instances* on one row (flow 05). `E` Continue's hub did it for **this** material and was switched off. `V` `HarnessKit`'s README claims per-agent drift detection — unrun |
| **RJ-4 — move the work without moving the secrets** | **2** — *lowered from 3, 2026-09-09, J-68; the superlative corrected with it.* `✓` **the largest crowd on a fear, after the multi-target family** — *largest in the corpus* was wrong, the R1 family (6,592 · 1,416 · 624 · 472) is larger by any measure — **across three trackers**: [#32733](https://github.com/anthropics/claude-code/issues/32733) 192 · [#401](https://github.com/anthropics/claude-code/issues/401) 54 · [#29910](https://github.com/anthropics/claude-code/issues/29910) 45 · [continue #1729](https://github.com/continuedev/continue/issues/1729) 32 · [#1018](https://github.com/modelcontextprotocol/servers/issues/1018) 23 · [#754](https://github.com/modelcontextprotocol/servers/issues/754) 22 · `*` Q23 — the private and the reusable are **tangled in the same files**, and **he has not done the separation**: *"never the most urgent couple of hours"*, which is a 2 | **`[?]`** — `.env.example` exists for the receiver, and **no receiver has said anything about it** | **`[?]`** | **§5** `needsEnv` · **§6** — collected across the resolved set and written to `.env.example` before export | **The runtime half is occupied; the handover half is not.** *Narrowed 2026-09-09 on [`re-research-2.md`](../6-personas/re-research-2.md) Q-D — this cell read "No, in this space", which J-70 and D-9 showed was too strong.* What exists: a credential-injection proxy outside the sandbox, a vault with time-scoped access, a key broker that injects into the shell, a WASM sandbox with a secret scanner, *"block secrets"* policies. **Every one of them keeps a key away from a *running* agent; none is about what a set carries when it leaves** — and a person names our exact failure: *"a skills file can just easily say '**We connect to bob using key Z and user X**'"*. `M` Vercel's env drawer is still the best-observed prior art in the phase (flow 07) and belongs to a different product. **Doppler and Infisical are captured in flow 07 and still unscored — a gap in the benchmark, one afternoon** |
| **EJ-1 — not be quietly overruled by my own tools** | **3** — `✓` [#20412](https://github.com/anthropics/claude-code/issues/20412) **142**, *"silently synced… without any opt-in, notification, or consent"* · `✓` [codex #13386](https://github.com/openai/codex/issues/13386), dropped *"with no warning anywhere"* · `✓` #1219 · `*` Q13, Q14 — *"my guesses are unfalsifiable"* | **2** — `*` Q21: overruled by **absence** — half his tools missing, and nothing said. **Second-hand** | **`[?]`** | **§6** — three severities, *nothing blocks*, the unclean export **confirmed** with its consequence in the present tense, and *Skipped* given a glyph it earned · **§7** — state 6 naming the fields that differ | **The market has the mechanism and the nearest competitor failed at it.** `M` Port ships pass / warn / block with the reason attached; GitHub's mergebox names consequences. `E` **Continue shipped `ConfigValidationError { fatal: boolean }` and filed a block that failed to resolve as `fatal: false`** — the exact failure, in our space, in production |
| **EJ-2 — believe a clean result was earned** | **`[?]`** — *the number was withdrawn 2026-09-09, J-74: the cell stated that its own evidence carries no weighting and then held a 2.* The utterances stand: `✓` R7: *"**blackbox oracles make bad workflows, and tend to produce a whole lot of cargo culting**"* ([bandrami](https://news.ycombinator.com/item?id=46820441)); *"engineers will always invent weird heuristics to detect drift"* ([Alpha_Logic](https://news.ycombinator.com/item?id=46106973)). **HN comment scores are not exposed, so this evidence carries no weighting at all** | **`[?]`** | **`[?]`** — arguably central for someone taking strangers' material; arguable is not evidence | **§6** — *Skipped* gets a neutral glyph rather than a tick it did not earn · **§5** — no score, no rating, no badge | **They close a different job.** Tessl scores 93 with an uplift multiplier, Smithery out of 100, `HarnessKit` claims 0–100 (`V`). Those answer *give me a signal*; whether a produced number makes anyone **believe** is `[?]`, and reading their scores as a failure at *this* job is **our inference, `R`** |
| **EJ-3 — stop suspecting half of what I keep is dead weight** | **3** — `✓` R7, **in four of the eight threads read** (*across eight threads* was the count; corrected 2026-09-09, J-76 · P-108): *"mostly useless… 50/50 or less"*, *"I can never quite tell if it's helping anything"*, a story titled *[I am morally opposed to updating my Claude.md](https://news.ycombinator.com/item?id=49376287)* · `*` Q16, Q17, Q18 — *"maybe half of it"*, *"I've never A/B'd anything"*, *"the folder only grows"* | **`[?]`** | **`[?]`** | **Nothing — and nothing can.** §5's usage facts are the nearest thing and they answer *is it used*, not *did it change anything*. **§6 runs nothing on anyone's machine.** This is **Q12** | **The market is forming here and we are not in it.** `V` four HN stories in nine months trying to measure exactly this: *AGENTS.md outperforms skills in our agent evals* (524 points), **SkillsBench** (364), Agent Skills Leaderboard (135), agent-skills-eval (79) |
| **SJ-1 — not be the missing manual for my own work** | **2** — `*` Q21, Q22: *"which files are load-bearing and which are aspirational… **none of that is written down anywhere**"* · `✓` that other people do open this material — #6235 6,592, [#10238](https://github.com/anthropics/claude-code/issues/10238) 168, [#28729](https://github.com/anthropics/claude-code/issues/28729) 151 | **`[?]`** — the receiver's half of this job is **H-J7**, and it stands on one aside | **`[?]`** | **§6** — `SETUP.md` addressed to the agent that opens the project, stating per item what it requires | **No.** The same structural gap as RJ-1: B4, nobody above 4 |
| **SJ-2 — have something I would put my name to** · *post-MVP* | **1** — `✓` the **absence**, looked for deliberately in two instruments: **0 of 1,762** HN comments, and `portfolio in:title` returning two unrelated issues (R10) · `*` Q23, a qualified yes **for a different motive**: *"publishing forces cleanup and I need external pressure"*. **They disagree and both stay** (rule 4) | **`[?]`** | **`[?]`** | **None in the MVP, by decision.** §9 keeps publishing out and does not show `visibility` at all | **Yes, all of them, and all need a server.** `M` Figma Community, Notion's gallery, Raycast's store, and a GitHub profile that reads as a portfolio when full and as an empty template when not (flow 12) |

## The hypothesis jobs, in the same matrix

**Every cell here is `[?]` except one, and that is the point of the block.** These rows exist because
**four specified features close nothing else.**

| Job | P1 | P2 | P3 | Feature that closes it | Do competitors close it? |
|---|---|---|---|---|---|
| **H-J1 — lay hands on something I wrote months ago** | **`[?]`** — one sighting, `*` Q19: *"it usually takes longer than rewriting it would"*. Evidence that it **happened**, not of how much it matters | **`[?]`** | **`[?]`** | **§8** — Library, filters by kind and tag, search · **§5** — per-item usage facts | **Yes, and well.** B1 is where the craft is concentrated — **Linear, GitHub code search, Obsidian and VS Code are the cells that were actually scored**; Backstage's catalog and Raycast's store were surveyed in stage 1 and never benchmarked (corrected 2026-09-09, J-84). **We would be competing where the market is strongest and our evidence thinnest** |
| **H-J2 — start from something I have done before and re-tune it** | **`[?]`** — §2 names it as a supporting moment; **nobody has said it.** The nearest sighting is `*` Q8, where the thing he wanted back was **welded to its project** and he wrote a worse one instead | **`[?]`** | **`[?]`** | **§8** — Projects, and duplication | **Yes, cheaply.** `M` Notion's `Ctrl+D` with no dialog; GitHub's fork form with a prefilled name and a narrowing checkbox (flow 09) |
| **H-J3 — change one copy for one project without touching the rest** | **`[?]`** — one aside, `*` Q26: *"my rule says one thing, the client's linter says another, and **there's no precedence anywhere**"*. That is **Q10**, and it is a conflict with something **outside** the set entirely, which §5 has nowhere to put | **`[?]`** | **`[?]`** | **§5** — `detached`, `overrides`, promotion as a new item · **§7** — state 6, with the differing fields named | **Half.** `M` Figma models overrides precisely enough to offer *Reset fill* by name — **and erases the origin at detach, so there is no way back** (flow 05). Our return path has **no prior art in the survey**, which cuts both ways |
| **H-J4 — get moving with material somebody else made** | **`[?]`** | **`[?]`** | **`[?]` as an importance — and no longer `[?]` in both directions.** *Updated 2026-09-09 from [`re-research-2.md`](../6-personas/re-research-2.md) Q-E — the only cell in this matrix that gained evidence, and it argues against the feature.* **Four of the first five practitioners ever observed on installing other people's material refuse it, minimise it, or prefer their own**; the one positive was distributing **his own** work through a marketplace mechanism, which is P1's job. What survived is *"a few established names"* — **provenance over volume**. **Nobody in P3's shape has still ever been asked anything, so there is no number here and cannot yet be one** | **§8** — the `My library` / `Public library` scope switch · **§11** — the curated read-only shelf and the example project | **Yes — the most crowded space in the entire survey, and as of 2026-09-09 the supply is counted rather than quoted.** `✓` **19,703 repositories** match `"claude skills"` in name or description, topped by curated collections at **74,686★**, 25,709★ and 15,006★ — against **93** public personal agent-material repositories (Q-E). `V` Smithery 17,500 servers, Tessl 3,000+ skills, Agentman 115 business skills, Notion's template gallery, plus the whole installer category. **Every catalog in the phase solves cold start this way** (OBS-12) |
| **H-J5 — watch what actually ran** · *the surviving second main job* | **3** — `✓` R7 · `*` Q25, the genie question, asked before the product was ever described. **Its importance is not in doubt; its closability is** | **`[?]`** | **`[?]`** | **Nothing, and nothing can be.** The same cell as EJ-3, which is this job's emotional face — **counted once, not twice** | **Forming.** The four measurement projects listed under EJ-3 |
| **H-J6 — my work counts as something I can show** | See **SJ-2** — the same job in functional wording, **not counted twice** | — | — | None in the MVP (§9) | Yes, and all of them need a server |
| **H-J7 — the unwritten half travels too** | **`[?]`** | **`[?]`** — `*` Q26, one aside: *"roughly **half** of what makes a project go well is stuff I've never written down"*. **If it holds it bounds the ceiling of the product**, because we validate the written part. **Q11** | **`[?]`** | **Nothing, and nothing can be** | **No.** Nobody in the survey attempts it |

---

# 8. What to build first — one job the rule chooses, and two kept on stated grounds

**Rewritten 2026-09-09, and the rewrite is the most consequential thing the audit caused.** This
section used to open *"the rule, applied mechanically"* and produce three jobs. It no longer does.

**The rule as written:** importance **3** for the primary persona **and** not closed by the market.
Before the audit five jobs scored 3 for P1 — the main job, RJ-3, RJ-4, EJ-1 and EJ-3. **After it,
three do**: the main job, EJ-1 and EJ-3. And of those three, **EJ-1 is a constraint on how every
other feature behaves rather than a thing to build, and EJ-3 is the one job in the matrix the product
cannot close at all.** So the rule, applied mechanically to the corrected matrix, yields **exactly
one buildable job.**

**One job is not a plan, so the other two are kept deliberately — and the change of basis is stated
rather than hidden.** RJ-4 and RJ-3 now score **2** for P1. They stay in the core on two grounds that
are not importance: **the market is open in both**, and **the specification has already spent a
mechanism on each** — `needsEnv` collected across the resolved set and written to `.env.example` for
one, the live link for the other. That is **a judgement with the matrix as its input**. It is not a
result the matrix produces on its own, and presenting it as one would be exactly the laundering §5
exists to catch.

### 1 · The main job — make it keep working somewhere else

> *"Codex, Amp, Cursor, and others are starting to standardize around AGENTS.md… **It doesn't work as
> well when collaborating with other developers who aren't using Claude Code.**"* — **6,592 reactions**

**Cells: P1 = 3, P2 = 2** — the P2 cell lowered by the audit and second-hand either way. It is one of
only **two** rows carrying a number in both people-columns (the other is EJ-1) and the only functional
one; *the only row with a number in both* was wrong (J-91). **Market: nobody above 4 on B4**, and
structurally so — no candidate has a surface that says anything about the machine its
artefact lands on. **The spec already spends most of its handover budget here** — §6's `SETUP.md`
decision, the target selector, the disclosure stages — which this row confirms rather than discovers.

### 2 · RJ-4 — move the work without moving the secrets

**Cell: P1 = 2**, lowered by the audit, on **the largest `✓` crowd on a fear after the multi-target
family** — 192, 54, 45, 32, 23, 22, across **three** trackers (*the largest crowd in the corpus*,
*two ecosystems*: both wrong, J-68 · J-94) — plus the `*` no count could give: **the private and the
reusable are tangled in the same files**, and separating them is *"a couple of hours that are never
the most urgent couple of hours."* **That last clause is also why the cell is a 2 and not a 3: he has
not done it.**

**Market: the runtime half is occupied and the handover half is not** (Q-D) — narrower than the
*nobody in this space* this section used to claim, and still an open cell, because everything that
exists keeps keys away from a **running** agent rather than out of a **handed-over** artefact. The
best prior art anywhere in the phase (Vercel's env drawer) belongs to a different product entirely,
and **Doppler and Infisical are captured and unscored**, which is a gap in the benchmark rather than
a finding here.

### 3 · RJ-3 — fix it once and have the fix reach every copy

**Cell: P1 = 2** after the audit, `✓` at 48 with a `*` price tag attached: six weeks, a client
complaint, three hours re-debugging a bug already fixed elsewhere — **and a respondent who, having
paid that price, still moves material with `cp -r`.** That is the whole reason the cell is not a 3.
**Market: solved beautifully for design components and dead for this material** — the one product that shipped it here was switched off. **§5's live link is
the single mechanism in the spec that exists for exactly this job**, and this row is its
justification.

### The two other 3s, and neither is a row to build — this matters more than the shortlist

- **EJ-1 — not be quietly overruled.** P1 = 3, on 142 plus two more `✓`. It is **not a feature to build**; it is a **constraint on how every other feature behaves**, and §6 already encodes it — nothing blocks, the consequence is named in the present tense, *Skipped* gets a glyph it earned. **It belongs in the core as a rule, not as a row.**
- **EJ-3 / H-J5 — stop suspecting half of it is dead weight.** P1 = 3, market forming, **and the *feature* cell is empty because nothing we can build fills it.** §6 runs nothing on anyone's machine. **This is the highest-importance job in the matrix that the product cannot close.** It is **Q12**, and its honest form is a positioning question, not a backlog item.

### The fourth, named because it is close

**RJ-1** — *know what the other side needs before I send it* — scored **P1 = 2, P2 = 3** and now
scores **P1 = `[?]`, P2 = 2, market nobody.** The audit took the primary's number away entirely,
because this section had already admitted what it rested on: the respondent found out on a call and
never said he wanted to know beforehand. **It is also the job the specification has invested in most
heavily** — the disclosure stages before Export exist for it. **That gap, between what the spec
spends here and what the evidence carries here, is now the widest in the file**, and it is D-5 in the
audit. If one practitioner says it plainly, it moves into the core ahead of RJ-3.

### Where this agrees with the specification, and where it does not

**Agrees** with §6 and §8 on the handover, and with §5's live link — both now have a job with
evidence behind them rather than a rationale, **though after the audit the live link's job is a 2 and
not a 3**. **Qualifies §2**: the three core jobs are one transfer
job and two of its failure modes, not *assembly with validation* — assembly is what you do in order
to move something. **Touches no surface in §8**, and proposes no new one.

---

# 9. What might not be worth building — a list of hypotheses, not a cut list

> **Read the label before the list.** Every feature below closes **a job whose every cell is `[?]`**.
> That is not evidence that nobody wants it. **It is an absence in instruments that cannot see
> presence** — the trackers are blind to *find* and *reassemble* by construction, and no person in
> P3's shape has ever been observed at all. **Cutting a feature on this list would be acting on our
> own blindness.** This stage removes nothing; removals are the owner's call on a register entry, and
> the entry has to say that the evidence for removal is an absence.

| Specified feature | The only job it closes | Standing of that job | What the matrix actually says |
|---|---|---|---|
| **The `Public library` scope switch** (§8) and **the curated shelf** (§11) | **H-J4** | **Every cell `[?]` as an importance** — and as of 2026-09-09 **the persona it serves is no longer unobserved, and the first evidence is against the premise**: four of five practitioners refuse, minimise or prefer their own material (Q-E). What else exists is vendor counts and tool READMEs | **The sharpest finding in the matrix, and it got sharper.** Two surfaces, a build commitment of real content from checked sources, and **a security standard the spec does not yet have** — 13.4% critical in a scan of 3,984 public skills (R6) — all closing one job whose persona, now that it has finally been observed, **prefers a few established names to curated volume.** The supply side is settled and enormous (19,703 repositories; 74,686★ at the top); the demand side has its first five voices and four of them are negative. **This does not say cut it** — four sceptics on Hacker News are not a market, the venue self-selects, and no beginner was asked. It says **Q9 now has evidence to be answered on, and the question is what the shelf contains and how it sorts, not only whether it ships** |
| **The example project** (§11) | **H-J4**, plus an onboarding argument | `[?]`, and §11's own reasoning — *a shelf guarantees material, not that the first check says anything* — is sound reasoning and **not evidence** | **Weaker as a feature and stronger as an argument** than the shelf itself. `M` OBS-36, the best first-run capture in the phase — Linear opening on four real issues — supports the **shape**, never the need |
| **Duplicate a project** (§8) | **H-J2** | `[?]` entirely. §2 names it as a supporting moment; **nobody has said it** | Cheap to build, closes nothing evidenced, and the market closes it in a keystroke. **A candidate to postpone, not to cut** |
| **Promote a detached item** (§5, §7) | **H-J3** | **Nothing.** *Corrected 2026-09-09 (J-107):* this read *one aside, `*`* — but that aside is about a conflict with something **outside** the set (the client's linter, Q10), which is not a request for a per-project override. **Nobody has said anything about wanting one** | Q4's disposition already noted that promotion only has value if in-project editing exists. **Both stand on nothing rather than on one aside, and they stand or fall together.** Flow 05 found no prior art for the return path — so the one mechanism in the spec that is invented rather than copied is also the one with no demand behind it (D-6) |
| **Library-wide search and filters** (§8) | **H-J1** | One sighting, `*` | **The awkward one.** It is the market's best-served flow (B1) **and** our thinnest evidence **and** the thing `CLAUDE.md` §8's accepted cost was priced against — a cost priced at **300 items**, which nothing supports (R4). **The replacement figure is now counted rather than blended**: four public agent-material repositories hold **11, 25, 47 and 48 items**, two of them above 40 ([`re-research-2.md`](../6-personas/re-research-2.md) Q-C). *Corrected 2026-09-09 (J-108): this said "build it for 20–40", a range made of one organisation's threshold and one person's file count.* **Tens, not hundreds — design for fifty**, and note the instrument only sees people who publish |
| **Per-item usage facts** (§5) | **H-J1** and **EJ-3**, partially | `*` n = 1 — **and the strongest `*` in the repository**: a practitioner invented our exact mechanism unprompted, with our vocabulary forbidden in the question, then **extended it** — *last actually useful*, counted **per session** | **Not an orphan.** The only specified feature a real person asked for in our own words. The evidence is still one person; two more unprompted repetitions would make §5 as close to validated as this method allows |

### Where this agrees with §9's refusals, and where it does not

- **Publishing to a public catalog — §9 refuses it and the matrix agrees.** SJ-2 scores **1** for the primary, on an absence looked for in two instruments, and every competitor that closes it needs a server. **The strongest agreement in the file.**
- **Composition — §9 defers it and the matrix qualifies the reasoning.** One of the two signals §9 leaned on has since failed: the `0 results` was a bug-shaped query on a frozen product, and the same friction **is** filed on live trackers ([#9444](https://github.com/anthropics/claude-code/issues/9444), [codex #17401](https://github.com/openai/codex/issues/17401)). **The deferral still stands on recursion**, which was always the better half of the argument.
- **Versioning of your own items — §9 refuses it, and the matrix has a datum against the refusal.** [#28729](https://github.com/anthropics/claude-code/issues/28729), **151 reactions**, asks for exactly what §9 rules out: *"there's no version history, no review process, and **no easy way to roll back a bad change**."* It comes from an **organisation** context, and one request is not a mandate — **but §9 currently reads as though nobody wants it, and somebody does.** Recorded; the disposition is the owner's.

---

# 10. What this hands forward


1. **The prediction the plan made about the matrix held, and it should be read as a warning rather than as a result.** The plan said the evidenced rows would be exactly the ones the trackers can see, and that P3's column would be almost entirely `[?]`. **It is entirely `[?]`** — **ten rows out of ten**; *nine of nine* was a miscount, corrected 2026-09-09 (J-113), and the same nine is repeated in this stage's README and in `FINAL.md` §6 — and P2 carries a number in only three, all of them 2s and all second-hand. So *what to build first* is evidenced and *what might not be worth building* is a list of hypotheses, and the second list must never be read as the first.
2. **Step 6 was written and is now applied.** [`personas-and-jobs-critique.md`](../personas-and-jobs-critique.md) audited all 117 claims in this file — 76 confirmed, 26 hypothesis, 15 invented — and every correction it proposed for this file has been made, listed cell by cell in §11. The dangerous list it produced was already visible from the matrix itself: **every P2 cell carrying a number is second-hand**; **RJ-1's P1 was an inference** and no longer carries a number; and **the whole of the orphan list rests on absences** in instruments that cannot see presence.
3. **To the register.** **No new question, and one existing question gained its first evidence:** **Q9** — *which specified features close no evidenced job* — now has Q-E under it, and the evidence is about what the shelf should hold rather than about whether it ships. The main job's rival is **Q12**; H-J3 is **Q10**; H-J7 is **Q11**; H-J1 and H-J2 are **Q5** and **Q7**.
4. **To the interview guide.** Three questions come out of this stage for step 6 to merge, and they are already implied above: the genie question asked four more times before any description of the product (Q12); *what happened the last time your own rule and the project's tooling disagreed* (Q10); and one that does not exist in the guide yet — **ask a receiver**, not an author, because every line about P2 is currently somebody else's account of them.
5. **Not to `CLAUDE.md`.** Nothing here is applied to the specification. **No feature is removed by this stage**, and the difference of emphasis between §2's *assembly with validation* and this file's *transfer* main job is stated once, above, as a difference — not as a correction. **§12 lists what this stage proposes**, and every item there goes to the register's next sitting rather than into the spec.

---

# 11. The audit pass — every change made to this file on 2026-09-09

**Step 6 of the plan.** [`personas-and-jobs-critique.md`](../personas-and-jobs-critique.md) was
written on 2026-09-08 against this file and edited nothing; this section is what happened when it
was applied. **117 claims were classified — 76 confirmed, 26 hypothesis, 15 invented.** Everything
below is either a correction from that audit or a finding from
[`re-research-2.md`](../6-personas/re-research-2.md), the targeted round the audit asked for.

**Read the direction before the table. The audit subtracted; the new research added one cell, against
us.** Nothing in this pass made a job more important than it was.

| # | Where | Was | Is | Why |
|---|---|---|---|---|
| 1 | Matrix **MAIN / P2** | 3 | **2** | J-59 — #6235's filer is an author; the only receiver on record worked around it for two days and changed nothing |
| 2 | Matrix **RJ-1 / P1** | 2 | **`[?]`** | J-61 — the cell called its own basis an inference and then held a number |
| 3 | Matrix **RJ-1 / P2** | 3 | **2** | J-62 — two days lost is *it costs them something*; he changed nothing |
| 4 | Matrix **RJ-3 / P1** | 3 | **2** | J-66 — the respondent paid the price and still moves material by `cp -r` |
| 5 | Matrix **RJ-4 / P1** | 3 | **2** | J-68 — he has never spent the *"couple of hours"*; and *the largest crowd in the corpus* was a superlative the logs refute |
| 6 | Matrix **EJ-2 / P1** | 2 | **`[?]`** | J-74 — the cell stated that its evidence carries no weighting and then held a 2 |
| 7 | Matrix **RJ-4 / competitors** | *"No, in this space"* | **the runtime half is occupied, the handover half is not** | Q-D · J-70 · D-9 — five mechanisms exist and every one keeps a key from a *running* agent |
| 8 | Matrix **H-J4 / P3** | `[?]` in both directions | **`[?]` as an importance, with evidence against the premise** | Q-E — four of five refuse, minimise or prefer their own; *provenance over volume* |
| 9 | Matrix **H-J4 / competitors** | vendor counts | **19,703 repositories, 74,686★ at the top, against 93 personal** | Q-E, counted |
| 10 | Matrix **H-J1 / competitors** | Linear, Backstage, Raycast, Obsidian | **Linear, GitHub, Obsidian, VS Code — the cells actually scored** | J-84 — Backstage and Raycast were surveyed, never benchmarked |
| 11 | Matrix **EJ-3 / P1** | *across eight threads* | **in four of the eight threads read** | J-76 · P-108 |
| 12 | §1 *Standing* | *the two loudest numbers* | *the loudest number in each of two corpora* | J-14 — applied 2026-09-08, recorded here for completeness |
| 13 | §2 **RJ-1** | *fifteen products, none above 4* | **four B4 cells, none above 4** | J-24 — the benchmark scored 15 cells across ten products; B4 holds four |
| 14 | §2 **RJ-3** | `✓` on `competitors.md` | **cited unmarked** | J-32 — NK-14 withdrew that `✓` and this file had restored it |
| 15 | §5 the check | *archive appears in RJ-1's when clause*; *export appears only in this table* | **neither word appears in any job** | J-51, J-52 |
| 16 | §6 **H-J4** | *`[?]` entirely* | **the supply counted, the demand sceptical** | Q-E |
| 17 | **§8** | *the rule, applied mechanically* → three jobs | **the rule yields one buildable job; two more are kept on stated grounds** | The consequence of rows 1–6 |
| 18 | §8.1 | *the only row with a number in both people-columns* | **one of two, and the only functional one** | J-91 — RJ-1 and EJ-1 also carried numbers in both |
| 19 | §9 **promote** | *one aside, `*`* | **nothing** | J-107 — the aside is about a conflict outside the set, not a wish for an override |
| 20 | §9 **search** | *build it for 20–40* | **11 to 48, counted; design for fifty** | J-108 + Q-C |
| 21 | §10 | *nine rows out of nine* | **ten of ten** | J-113 |

**What was audited and left standing, so it is not re-litigated later.** The main job itself and its
`✓` + `*` standing; RJ-2's evidence and its honest *13 against 182* weighting; EJ-1's three
confirmations; SJ-2's 1 on an absence looked for in two instruments; every competitor cell not listed
above; and the hypothesis list's shape. **The audit did not overturn a single job.** It changed what
we are allowed to lean on.

**What is still owed and cannot be closed here.** Four interviews, and the receiver's question block
the guide does not have — **every line in the P2 column is somebody else's account of a person nobody
has asked.** And **NK-13**: compose a set, write the `SETUP.md` §6 describes, hand the archive to a
fresh Claude Code, Cursor and Codex, record what each does. Half a day, on this machine, and after
two rounds of research it is still the most load-bearing untested claim in the project.

---

# 12. Reconciliation with the specification — what this stage proposes and does not apply

**Step 7 of the plan.** [`CLAUDE.md`](../../CLAUDE.md) is untouched by this stage and stays untouched
until the register's next sitting. **This is the list the sitting reads.** Nothing here is a decision,
nothing here removes a feature, and every item names the evidence that raised it and the entry it
belongs to.

| # | Spec section | What this stage found | Proposal | Register |
|---|---|---|---|---|
| **R-1** | **§2**, the core-value sentence | The evidence words the main job as **transfer** — *what I got working here has to keep working there* — where §2 words the value as **assembly with validation**. The second is contained in the first | **State the difference in §2 rather than resolve it.** Assembly is what you do in order to move something; the check is how you find out before the move | **Q8**, and **Q12** if the rival main job wins |
| **R-2** | **§8, §11**, the public shelf | The persona it serves has now been observed for the first time, and **four of five prefer a few established names to curated volume** (Q-E) | **Do not cut it; re-aim it.** The open question is what the shelf holds and how it sorts — provenance first, volume never — and §11 still has **no content-review standard** against 13.4% critical in 3,984 public skills | **Q9**, which now has its first evidence |
| **R-3** | **§11**, *~30 realistic items* | Counted rather than asserted: **11, 25, 47 and 48 items** in four public repositories, two above 40 (Q-C) | **Say tens, not hundreds, and design the Library for fifty.** §8's accepted cost was priced against 300 and that stays refuted | Feeds **Q5**, blocks nothing |
| **R-4** | **§5, §7**, detach → promote | After the audit, in-project editing and promotion stand on **nothing** — the one aside cited is about a conflict outside the set (D-6, J-107) | **Nothing to change now.** Q4's disposition was taken on reasoning and holds; but this is the least evidenced mechanism in the spec and the only one with no prior art | **Q10** |
| **R-5** | **§6, §8**, the disclosure stages before Export | RJ-1's sender-side cell lost its number entirely (D-5). The stages may still be right **for the receiver** — and no receiver has been asked | **Keep, and note what they rest on.** One practitioner saying it plainly moves RJ-1 into the core | **Q7 / Q8** |
| **R-6** | **§6**, `SETUP.md` written for the agent | In 274 comments on exactly this topic, the work is done by `chezmoi`, symlinks, a CLI installer, `skills.py` and bootstrap scripts; **two comments describe an agent touching this material and neither is a setup** (Q-A) | **The bet is not refuted — it is against the grain of current practice.** Run NK-13 before the first mockup that shows the handover stages | **NK-13**, the named half-day |
| **R-7** | **§6**, `.env.example` and RJ-4 | The runtime half of this problem is occupied by several parties; **the handover half is not** (Q-D) | **Keep it in the core, narrow the claim.** It is hygiene that happens to be unoccupied, not a differentiator we invented | — |
| **R-8** | **§9**, versioning refused | [#28729](https://github.com/anthropics/claude-code/issues/28729), **151 reactions**, asks for exactly what §9 rules out — from an organisation context | **§9 currently reads as though nobody wants it, and somebody does.** Record the datum; the disposition is the owner's | Owner's call |
| **R-9** | **§9**, composition deferred | One of the two signals §9 leaned on has failed — the `0 results` was a bug-shaped query on a frozen product — and the friction is filed live (#9444, codex #17401). **The deferral stands on recursion**, which was always the better half | **Change the stated reason, not the decision** | Owner's call |

**The rule this section obeys.** A research stage may narrow a claim, name a risk and hand back a
proposal. **It may not edit the specification, and it may not remove a feature on an absence** — the
instruments that produced these absences cannot see presence, and the one persona they finally
reached was reached in the venue least likely to like it.
