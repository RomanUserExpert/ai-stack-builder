# Stage 7 — Jobs to be done

**A plan, not a result.** Written 2026-09-06, alongside [stage 6](../6-personas/README.md), which
it reads from. The method is lesson 2's steps 3 and 4 — jobs in the *when / I want / so that* form,
one main job with related, emotional and social jobs around it, then a matrix of jobs against
personas that decides what to build first and what not to build at all — adapted to a product whose
screens are already specified. That last fact is the whole difficulty of this stage and is dealt
with below.

Status, **2026-09-08: steps 1–5 are done; steps 6 and 7 are not.**
[`jtbd.md`](jtbd.md) holds the main-job candidates and the choice, the hierarchy — **one main job,
four related, three emotional, two social** — the *Rewritten* list from the feature-name test,
**seven hypothesis jobs**, and **the matrix with both of its conclusions**. **Still owed:**
`audit.md` (step 6), the reconciliation with the spec (step 7), and the section on the shared page.

**The matrix came out the shape the plan predicted, which is a warning and not a result.**
**P3's column is `[?]` in all nine rows** and P2 carries a number in three, because only one issue's
stated motive speaks for receivers and **no receiver has ever been asked**. So *what to build first*
is evidenced — the main job, keys staying behind, one fix reaching every copy — and **what might not
be worth building is a list of hypotheses about an absence**, which is why this stage removes
nothing.

**The step-1 rule fired.** Two main-job candidates survived — *make it work somewhere else* and
*know whether any of this does anything* — and the lesson's rule for that case is that you have two
products. It is **recorded and not resolved**, because it is already **Q12** in the register and it
is the one we cannot build. `personas.md` exists; `audit.md` does not, and the jobs were written
from the personas and the register directly, with each job's standing inherited rather than
re-argued.

---

## What this stage is for

Jobs that survive a change of solution. The lesson's test is exact: *a good job does not change
depending on which product closes it* — "I want a price filter" is a feature; "I want to discard
what I cannot afford, fast" is a job ten products could close. The product's value is then argued
from the matrix — which jobs the primary persona needs, which the market leaves open, which of our
specified features closes no job at all — rather than felt. The matrix's two answers are the
deliverable: **what to build first, and what not to build.**

## What it is not — the specific way it goes wrong here

The lesson expects jobs to come *before* the information architecture; here [CLAUDE.md §8](../../CLAUDE.md)
already names four surfaces, §6 already specifies the logic, and §2 already says what the core value
is. So the temptation is not to invent jobs but to **launder the spec into job form**: *"When my set
is complete, I want the system to run a validation pass, so that I see Problems and Notes"* is §6
with a *when* in front of it. It fails the feature test twice over — it names the mechanism and it
names our severities — and it would make the matrix a mirror of §8 that confirms §8 by
construction.

The specific claim at risk is §2's: *the core value is assembly with validation, not storage* and
*the user has said [the wow moment] is the export*. Both are **the owner's assertions**. The second
is literally the owner's own preference recorded in the voice of a user. They may well be right —
the pain evidence leans their way — but they are exactly what this stage exists to confirm or
refute, and they cannot be used as sources for the jobs that test them. Every main-job candidate
below carries the standing of its evidence for that reason.

Two smaller ones:

- **The single-user trap for social jobs.** The lesson's demo has a social layer because strangers
  meet. Ours is a single-user desktop tool; the social jobs are thin and mostly post-MVP (§2's
  portfolio ambition, §9's publishing). Thin is the honest answer. Do not invent a social layer to
  fill the template.
- **Averaging the matrix.** An importance score nobody has told us is `[?]`, not 2. The lesson says
  this; the reason it matters here is that our only weighting is reaction counts on one kind of
  pain, so an averaged cell would silently encode the tracker's blindness as a middle value.

---

## Inputs

| Input | Kind | What it yields |
|---|---|---|
| `6-personas/personas.md` (not written yet) | Stage 6's output. | The carriers of each job, and the primary that wins conflicts. Jobs are written *from* personas, and each job names which persona and which evidence it grew from. |
| [`6-personas/inventory.md`](../6-personas/inventory.md), `6-personas/audit.md` (not written yet) | Stage 6's output. | The observed / asserted / not-known split, reused so that every job's standing is inherited rather than re-argued. |
| [`3-pain/user-pain.md`](../3-pain/user-pain.md) | Observation, weighted. | The evidence for the job candidates on the check-and-handover side: 182 for *it does not run on my machine*, 32/23/22 for env and secrets, 13 for the silent collision, 0 for cross-project reuse. The *method* section governs how the matrix may weight anything. |
| [`4-benchmark/benchmark.md`](../4-benchmark/benchmark.md) | Rubric and finalisation. | B1–B4 are already four candidate related jobs in disguise — find, assemble, check, hand over — and the finalisation says which two carry the value. Also the raw material for the *competitors* column: who does each flow best, and how well. |
| [`1-landscape/comparison.md`](../1-landscape/comparison.md), [`competitors.md`](../1-landscape/competitors.md) | Positioning. | The *competitors* column: which player closes which job, with the caveat that a vendor selling against a pain is not the same as closing it. The three *differences we can hold* are three job-shaped claims — a personal library that answers to nobody, trusting the file instead of the network, assembly as the product — and each gets tested rather than copied. |
| [`5-patterns/patterns.md`](../5-patterns/patterns.md) | Reasoned. | Where each job would land on the chosen shape, and the stated cost — *you cannot see what you are not using* — which is a job the shape decided to serve badly. The matrix should show whether that cost falls on the primary persona. |
| [`2-flows/`](../2-flows/README.md) captures | Mechanisms. | Flow 09 (duplicate and fork) for the *re-tune for a new context* job; flow 05 for the *change one copy without touching the rest* job; flow 07 for env; flow 08 for cold start. |
| [`CLAUDE.md`](../../CLAUDE.md) §2, §6, §8, §9, §11 | **Owner's assertions and specified features.** | §2 supplies the main-job candidates *under test*. §6 and §8 supply the *feature* column — every mechanism the product commits to. §9 supplies the features already refused, which the matrix should be able to agree or disagree with. §11's public library and example project are features whose job has to be found or admitted missing. |
| [`research.md`](../research.md) §5 | Digest. | G1 and G9 are already the two competing positioning hypotheses — *reassembly converts* and *silent breakage retains, not acquires*. The main-job argument should end by saying which it supports. Digest, never a source. |

Not an input: the lesson's demo jobs. *Safely decide whom to live with* and *not look desperate*
are the template's shape, not its content.

---

## Steps

Adapted from the lesson's steps 3, 4 and 5, with two additions this product needs (step 1, because
the main job is contested; step 7, because the spec already exists and has to be reconciled rather
than written).

### 1. Main-job candidates — and the standing of each

**Does.** Writes two or three candidate main jobs, in the canonical form, each with the evidence
that would make it the main one and its standing. The candidates the evidence already suggests:

| Candidate, as a job | Grew from | Standing |
|---|---|---|
| *When I hand a set of AI building blocks to a machine or an agent that did not make them, I want it to run first time, so that I never debug configuration at runtime.* | Stage 3, finding 1 (182), finding 2 (13), finding 3 (32/23/22); benchmark B4 — nobody above 4 | **Observed**, and the loudest thing observed. Note it is a *handover* job; §2 words the product as an *assembly* job. |
| *When I start a new project, I want the blocks I already trust to be in it without re-copying them, so that setup costs minutes rather than an afternoon.* | §2's "reassembly" reading; comparison.md difference 3; Q5 | `[?]` — the tracker cannot see it, and Q5 was deferred on exactly this |
| *When I need something I wrote months ago, I want to find it and know it still works, so that I stop rewriting what I already have.* | §2's storage ambition; §3's "accumulated a lot of material"; Q5 | `[?]` — same blindness; and §2 itself says the value is not storage |

The lesson's rule closes the step: **if two main jobs survive, you have two products.** If that
happens here, the step does not pick by taste — it records the fact and hands it to the register
(see *Hand back*), because it is the Q5 question wearing job clothing.

**Reads.** `personas.md`, `user-pain.md`, `benchmark.md` finalisation, CLAUDE.md §2.

**Writes.** The opening section of `jtbd.md` — candidates, standing, the one chosen and why, and
which of G1 / G9 the choice supports.

**Done when.** Every candidate passes the feature test and the change-of-product test. The chosen
main job is stated with its standing, and where it differs from §2's wording the difference is said
in one sentence rather than smoothed over.

### 2. Related jobs — three to five, on the way to the main one

**Does.** The path to the main job, as jobs. Candidates from the material, each to be re-cut
against personas rather than copied: *find one thing in my own collection* (B1 — `[?]` by
blindness); *put together the set this project needs, and see what it drags in* (B2, and §6's
dependency walk — the evidence is 0 results for reuse and a family of *"I set it and it was
ignored"* issues); *know before I ship whether the set holds together* (B3 — observed, 13 and the
family); *know what the receiving machine must still do* (B4, Q2 — observed, 182); *change one copy
for one project without touching the rest* (flow 05, Q4 — mechanism observed, demand `[?]`);
*re-tune a set I already have for a new context* (§2's second supporting moment, flow 09 — `[?]`);
*keep my keys out of what I hand over* (finding 3 — observed, 32).

**Reads.** `personas.md`, the flow notes named above, `benchmark.md`.

**Writes.** `jtbd.md`, the hierarchy: main → related, each related job with the persona it grew
from, its evidence line and its standing. Unsupported ones go to the *Hypotheses* section at the
end, not into the list.

**Done when.** Three to five in the main list, each sourced. The rest in *Hypotheses*, each with
what would test it. Every *I want* clause read aloud contains no noun from §4's vocabulary, no
mechanism from §6 and no surface from §8.

### 3. Emotional and social jobs — kept separate, and kept thin

**Does.** The layer the lesson says distinguishes a product from a catalogue: how the person wants
to feel and to look. Here the emotional candidates are sourced — *not be told by a runtime what I
should have been told by the tool* (finding 2), *trust that a green tick was earned* (§6's *Skipped*
severity exists for this), *not fear that the archive carries my keys* (finding 3). The social
candidates are mostly not — *hand a colleague a setup that does not embarrass me* (`[?]`; the
trackers have people filing issues on behalf of others, which is a hint), *have my work be a
portfolio* (§2's long-term ambition, §9 out of scope — `[?]` and post-MVP).

**Reads.** `personas.md`, `user-pain.md`, CLAUDE.md §2, §9.

**Writes.** `jtbd.md`, the third level. Social jobs that are post-MVP are listed as such so that the
matrix can show they close nothing *in the MVP* without pretending they do not exist.

**Done when.** Emotional jobs are sourced or marked. The social list is short and says why.

### 4. The feature-name test — over every clause

**Does.** A pass over every *I want* in the file. Three tests, from the lesson: no feature name in
the motivation; the job survives a change of product; the job starts from a situation, not a wish.
In this repository, the feature names to catch are specific: *validation pass*, *check*, *Run*,
*Problem*, *Note*, *palette*, *⌘K*, *detach*, *promote*, *public library*, *`SETUP.md`*,
*`.env.example`*, *target*. Any of them in a motivation is a stolen decision.

**Reads.** `jtbd.md`.

**Writes.** Corrections in place; a short *Rewritten* list at the end of `jtbd.md` showing the
before and after, so the laundering is visible rather than silently fixed.

**Done when.** A grep of `jtbd.md`'s *I want* clauses for the list above returns nothing.

### 5. The matrix — jobs × personas, plus feature and competitors

**Does.** Rows are jobs, columns are personas. A cell holds the job's importance for that persona,
**1–3**, and the evidence for that number from the repository. No evidence, no number: `[?]`, not 2.
Two more columns: **feature** — what in the specified product closes this job, cited to the CLAUDE.md
section (or *nothing*, which is the interesting answer); **competitors** — which of the fifteen close
it, cited to `comparison.md`, with *sells against it* distinguished from *closes it*.

Then the two conclusions the lesson requires, in this product's terms:

- **What to build first.** Three jobs for the MVP core: important for the primary persona *and* not
  closed by the market. The benchmark finalisation predicts the answer sits in B3 and B4; the matrix
  either confirms that with cells that have evidence in them, or shows it was assumed.
- **What not to build.** Features that close no job, or only a job whose every cell is `[?]`. The
  candidates to test are the ones the spec already commits to: the public library scope switch and
  the example project (§8, §11), duplicate project (§8), promote (§5), the agent target selector
  (§6), per-item usage facts (§5), library-wide search and filters (§8). And the ones §9 already
  refuses — versioning, composition, publishing — which the matrix should find closing no evidenced
  job, or else say so.

**Reads.** `jtbd.md`, `personas.md`, `comparison.md`, CLAUDE.md §5–§9, §11.

**Writes.** The matrix appended to `jtbd.md`, with the two conclusions beneath it.

**Done when.** No cell holds a number without a source line. The three core jobs are named with
their cells quoted. The orphan list is named. Both lists say where they agree with §2, §8 and §9 and
where they do not.

### 6. Audit

**Does.** Lesson step 5, run over `jtbd.md` as stage 6 ran it over `personas.md`: every claim
confirmed / hypothesis / invented; the dangerous list — jobs or cells that bear on a design decision
and stand on `[?]`; three questions with instruments. The dangerous list here is predictable and the
audit must still write it out: any cell in the *find* and *reassemble* rows, every cell of the
primary persona if the primary was chosen on the sourced half only, and the main job itself if a
second candidate survived step 1.

**Reads.** `jtbd.md`.

**Writes.** `audit.md` in this folder.

**Done when.** As in stage 6. In addition, the three questions are merged into
[`6-personas/interview-guide.md`](../6-personas/interview-guide.md), so that one conversation serves
both stages.

### 7. Reconcile with the spec — and hand back

**Does.** The step the lesson does not need and this repository does. A table, one row per claim in
CLAUDE.md §2, §8 and §9 that the matrix touches: *what the spec says · what the matrix says ·
agree / qualify / disagree · standing of the matrix's evidence*. Where the matrix disagrees on
evidence, that is a proposal to change the spec. Where it disagrees on `[?]`, that is a register
entry — a question with a named instrument — and not a proposal. Where §2's owner assertions are
confirmed, the table says on what evidence, so that §2 can cite it from then on instead of asserting.

Then the proposals, in the same form as stage 6's: the block for CLAUDE.md (main job, top three
jobs, the orphan list as candidates for the owner's decision), the digest section for `research.md`,
the matrix section for `personas.html`, and the register entries.

**Writes.** A *Reconciliation* section and a *Proposals* section at the end of `audit.md`.

**Done when.** No file outside this folder has been edited. The owner can apply each proposal
without reading the stage.

---

## Output files

| File | What it holds |
|---|---|
| `jtbd.md` | Main-job candidates and the choice; the hierarchy — main, related, emotional and social — each job with persona, evidence and standing; the *Rewritten* list from the feature test; the matrix with the feature and competitors columns; the two conclusions; hypotheses at the end. **Provisional** in the header. |
| `audit.md` | Confirmed / hypothesis / invented; the dangerous list; three questions; the reconciliation table against CLAUDE.md; the proposals. |
| Section in [`6-personas/personas.html`](../6-personas/personas.html) | The hierarchy and the matrix as a table on the shared page, marks visible. One page for both stages, as the lesson has it. |
| Additions to [`6-personas/interview-guide.md`](../6-personas/interview-guide.md) | This stage's three questions, merged. |

---

## The evidence rule, for this repository

The same as stage 6, with one addition for the matrix. Every job names the persona and the source
it grew from; every cell names the source of its number; anything without one is `[?]` and moves to
*Hypotheses*. The addition: **a reaction count is ordinal, not cardinal.** 182 against 13 says which
pain is louder; it does not say the first is fourteen times as important to anyone, and it says
nothing at all about pains the instrument cannot see. A cell that cites a count says *louder than*,
never *more important than*, unless a persona's evidence says so on its own.

Where the sources are: pain with weight in [`3-pain/user-pain.md`](../3-pain/user-pain.md) and
[`_user-pain-issues.json`](../3-pain/_user-pain-issues.json); who closes what in
[`1-landscape/comparison.md`](../1-landscape/comparison.md) (positioning, cited as such); how well
in [`4-benchmark/benchmark.md`](../4-benchmark/benchmark.md); the mechanisms in the
[`2-flows/`](../2-flows/README.md) notes; the specified features in CLAUDE.md by section, cited as
*specified*, never as *needed*.

---

## The honest problem

**Importance is the thing nobody has told us.** A persona can be built from pain evidence and be
half sourced; a matrix cell is a claim about how much a *person* cares, and no document in this
repository was produced by asking anyone. So the first version of the matrix will have evidence in
exactly the rows the trackers can see — check, handover, env — and `[?]` in the rows the product's
own §2 and §3 are built on — find, reassemble, keep. The three core jobs the matrix names will
therefore be the three the instrument can see, and the plan says this now so that the result is not
mistaken for a discovery.

**What fraction.** Of the hierarchy: the main job and two or three related jobs sourced; two or
three related jobs and every social job `[?]`. Of the matrix: roughly a third of cells with a
number and a source, the rest `[?]` — and every `[?]` cell sits in a row that decides whether the
Library screen, the public shelf, duplication or promotion earn their place. **The "what to build
first" answer will be evidenced; the "what not to build" answer will be a list of hypotheses**, and
it must be labelled as one, because acting on it would cut specified features on the strength of an
instrument's blindness.

**Q5, restated.** Stage 3 called it *loss or reassembly cost — which drives adoption*, and the
register deferred it with a five-practitioner trigger. Step 1 above will meet it again as *which
main job is the main one*, and the matrix will meet it a third time as an empty column. The
question does not get a new answer here. It gets a sharper instrument: the interview guide, with
the main-job candidates written as situations to ask about rather than as pitches to confirm.

**The label.** `jtbd.md` ships **provisional**, and the label lifts on the same event as stage 6's:
five practitioner conversations run against the guide and filed as a source document. Until then
the matrix is allowed to settle conflicts about the check, the handover and the copy — the rows
with evidence — and is not allowed to remove a feature from §8. Removing is the owner's call on a
register entry, and the entry must say that the evidence for removal is an absence in an instrument
that cannot see presence.

---

## Definition of done

- [ ] Main-job candidates written in the canonical form, each with standing; one chosen, or two
      surviving and recorded as a register entry rather than a choice
- [ ] Hierarchy — one main, 3–5 related, emotional and social separate — every job with persona,
      source and standing; unsupported jobs in *Hypotheses*
- [ ] Feature-name test passed: no vocabulary from CLAUDE.md §4, no mechanism from §6, no surface
      from §8 in any *I want* clause; the *Rewritten* list kept
- [ ] Matrix — jobs × personas, 1–3 or `[?]` with a source per cell, feature and competitors
      columns cited, no averaged cells
- [ ] The two conclusions — three core jobs with their cells quoted; the orphan list, labelled as
      hypothesis where its cells are `[?]`
- [ ] `audit.md` — classification, dangerous list, three questions merged into the interview guide,
      the reconciliation table against §2, §8, §9
- [ ] Where §2's owner assertions are confirmed, the evidence is named so §2 can cite it; where they
      are not, the disagreement is a register entry with an instrument
- [ ] `personas.html` gains the hierarchy and the matrix, marks visible
- [ ] Proposals for CLAUDE.md, the digest and the register written and **not applied**
- [ ] No feature removed from CLAUDE.md by this stage
