# Stage 6 — Personas

**A plan, not a result.** Written 2026-09-06, before any persona exists. This stage and
[stage 7](../7-jobs-to-be-done/README.md) re-open a research phase that was signed off on 2026-09-02
in five stages; the re-opening is recorded in [`research-plan.md`](../research-plan.md), not hidden
here. The method is the one taught in lesson 2 of the design-engineering course (its prompt pack and
slides, read in full), adapted to this product and to this repository's evidence rules. Where the
lesson and this repository's protocol disagree, the protocol wins and the disagreement is stated.

Status: **not started.**

---

## What this stage is for

Two to four **behavioural** personas, one primary, every block of every persona carrying a link to
where in this repository it came from — so that the design system, the mockups and the copy can
settle a conflict by citing a person rather than a preference. The lesson's rule is the whole
stage: *a persona is a synthesis of research, not creativity; for every claim ask "where is this
from?", and if there is no answer mark it `[?]` and file it as a hypothesis.*

## What it is not — the specific way it goes wrong here

The lesson's generic trap is a persona invented from a blank page. Our trap is narrower and more
tempting: **a persona invented from CLAUDE.md §3 and then cited back as evidence.** §3 already
says who the audience is — *design engineers and AI engineers, 25+, who use AI heavily, visually
literate, live in Linear, Vercel, Raycast, Figma.* That is the owner's assertion, written before a
single user was observed. If stage 6 restates it with a name and a quote, the spec will end up
citing the persona and the persona citing the spec, and nothing will have been established. §3 is
therefore an **input to be tested**, listed below under *owner's assertions*, and it is never a
source.

Three more, from the lesson's four traps, in this product's terms:

- **Passport instead of behaviour.** "Senior" versus "junior", "designer" versus "engineer" are not
  personas unless their jobs, pains or trust triggers differ — and nothing in the repository says
  they do. Personas split on behaviour we can actually see: *breaks at handover* versus *loses
  material*, *one agent target* versus *several*, *writes own items* versus *consumes others'*.
- **Persona as decoration.** The lesson's test for every block: *which design question does it
  answer?* A block that answers none is ballast. For us the questions are already named — what is
  on an item card (§5), what an empty `My library` says (§8, §11), which register the validation
  copy uses (§6), what the handover stages disclose (§6) — and every block must point at one.
- **The circular quote.** The lesson wants a mood-setting quote from a real review or forum. Here
  the only real user words in the repository are issue titles and bodies in
  [`3-pain/_user-pain-issues.json`](../3-pain/_user-pain-issues.json). A quote comes from there with
  its URL and reaction count, or it is not a quote.

---

## Inputs

What each is expected to yield, and — the part that matters here — what kind of evidence it is.

| Input | Kind | What it yields |
|---|---|---|
| [`3-pain/user-pain.md`](../3-pain/user-pain.md) | **The only observation of users.** Two public trackers, ranked by reactions. | Pain, weighted: environmental breakage at handover (182 reactions), env and secrets near the top of both trackers (32, 23, 22), our own collision thesis sighted but quiet (13, and 3–13 for its family), and **0 results** for cross-project reuse. Read its *method* section first: the instrument sees breakage, not friction, and is blind to loss and reassembly cost by construction. Everything a persona says about *why* someone hurts comes from here; nothing it says about *why someone would adopt* can. |
| [`3-pain/_user-pain-issues.json`](../3-pain/_user-pain-issues.json) | Raw API results. | The quotes. Every persona quote is an issue body with a URL and a reaction count — [#64](https://github.com/modelcontextprotocol/servers/issues/64), [#1219](https://github.com/modelcontextprotocol/servers/issues/1219), [#1729](https://github.com/continuedev/continue/issues/1729), [#4306](https://github.com/continuedev/continue/issues/4306), [#8484](https://github.com/continuedev/continue/issues/8484) are the ones already read. The JSON holds more that were ranked but not quoted. |
| [`1-landscape/comparison.md`](../1-landscape/comparison.md) | Vendor positioning. | The *Audience* axis for fifteen products: every live hard competitor sells to an organisation and **the individual practitioner is unoccupied ground**. This is what fifteen companies believed about who pays, not what any user said. Usable for *who the market ignores*, never for *what that person wants*. |
| [`1-landscape/continue-postmortem.md`](../1-landscape/continue-postmortem.md) | A competitor read from source. | The one behavioural datum about practitioners at scale: the hosted composition hub was switched off, the free local client stays installed on **1.58M** machines. Read both ways in Q5 and it must stay that way here. |
| [`1-landscape/competitors.md`](../1-landscape/competitors.md) | Vendor positioning. | Who each competitor says it is for, and which of the three candidate pains (loss / reassembly / breakage) each one sells against. Positioning is not demand. |
| [`2-flows/`](../2-flows/README.md) captures | Mechanisms, not people. | Trust triggers **as products chose to show them** — Tessl's score, Figma's *423 instances*, VS Code's Workspace Trust, Vercel's env drawer asking *where to rotate, or who to contact*. Evidence of what vendors bet convinces; not evidence that it does. Flow 08 (cold start) and flow 05 (detach) carry the states a persona must be able to read. |
| [`4-benchmark/benchmark.md`](../4-benchmark/benchmark.md), *finalisation* | Instrument statement. | The four flows re-weighted by pain: value in B3 and B4, craft in B1 and B2. A persona whose whole story lives in B1 (*find my things*) has no evidence behind it yet; one whose story lives in B4 (*hand it over and it runs*) does. |
| [`5-patterns/patterns.md`](../5-patterns/patterns.md) | Reasoned, not observed. | The claims about the person that the chosen shape already depends on — *300 items*, *a tool people open weekly*, *finds what they can name and stays blind to what they cannot*. All unobserved; all belong in the inventory's *what we do not know*. |
| [`research.md`](../research.md) §5 | Digest. | Gaps G1, G4, G5 and G9 are already written as falsifiable hypotheses about people. The inventory should carry them over rather than rediscover them. A digest, never a source: cite the stage document behind each. |
| [`CLAUDE.md`](../../CLAUDE.md) §2, §3, §11 | **Owner's assertions.** | The claims under test. §3's audience sentence; §2's *"the user has said it is the export"*; §11's *"an empty library kills the product"*. Each is listed in the inventory as *stated by the owner, not observed*, and each is a thing this stage should be able to confirm, qualify or refute. |

Not an input: the lesson's demo product ("Куток", a flatmate-search service in Kyiv). Its
seeker/lister split, its trust triggers about strangers and its OLX-and-chats pains are examples of
the structure, not requirements.

---

## Steps

Adapted from the lesson's seven-step chain (inventory → personas → jobs → matrix → critique →
targeted re-research → HTML). Jobs and the matrix are stage 7; this stage takes the rest. Each step
names what it reads, what it writes and the bar that says it is done.

### 1. Inventory — what the repository actually says about people

**Does.** Reads every input above and extracts every statement about *people* — who they are,
what drives them, what they fear, how they choose, where they break — grouped into observations.
Then, separately and at equal length, lists what we do not know.

**Reads.** All inputs. `user-pain.md` and the JSON in full; the rest for people-claims only.

**Writes.** `inventory.md`, three sections: *Observed* (each row: the observation, its source path
or URL, the reaction count where there is one), *Asserted by the owner* (each row: the claim, the
CLAUDE.md section, and what would test it), *Not known* (each row: the question, and why no
document here can answer it).

**Done when.** Every row in *Observed* has a path or a URL. *Not known* explicitly contains: which
of loss / reassembly / breakage drives adoption (Q5); library size and growth rate; frequency of
use; how many agent targets one person actually uses; where material lives today (dotfiles, gists,
repo folders, chat history); whether the person works alone or hands archives to others; whether
anyone has ever wanted a prior project back. If any of these has been quietly answered, the answer
is a `[?]`.

### 2. Behavioural axes — how people differ, in ways we can see

**Does.** Before writing a single persona, proposes the axes that would split one persona from
another, and keeps only those with evidence on both ends. Candidates, from the inventory:
*breaks at handover* vs *loses material* (the tracker sees one end only); *one agent target* vs
*several* (Ruler and `create-next-app` show the mechanism exists; nobody here shows who needs it);
*writes own items* vs *consumes a public shelf* (Q1's answer bets on the second; §3 describes the
first); *files an issue when it breaks* vs *tolerates tedium silently*.

**Reads.** `inventory.md`.

**Writes.** A short section appended to `inventory.md` — *Axes*, each with the evidence at each
end or `[?]`.

**Done when.** No axis is demographic. Every retained axis names what separates its two ends and
where that came from. An axis with `[?]` at both ends is listed and not used.

### 3. Personas — with attachment

**Does.** Builds 2–4 personas from the retained axes. Blocks per persona, from the lesson, in
this product's terms: **context** — the situation they arrive from (a new machine; an archive that
did not run; a fourth project needing the same four files; a colleague asking for the setup);
**jobs and pains** — what they are trying to do and what hurts in how they do it now; **trust
triggers** — what would convince them a set holds together and what would make them distrust the
check (a score, per §5's decision; a green tick that was not earned, per §6's *Skipped*); **quote** —
a real issue body with URL and reactions. A fourth block the lesson does not have and this product
needs: **environment** — agent targets, where their material lives, whether anyone else opens their
archives — filled only from evidence, otherwise `[?]` throughout.

One persona is **primary**. The lesson's rule for choosing: the one with the higher risk and fewer
levers in a conflict. Here the candidates pull apart, and the choice must be argued in the file:
the person whose pain is *sighted* (an archive that lands and does not run; a duplicate key that
silently wins) against the person the spec is *positioned for* (a collector with a large corpus
who wants to find and reuse it). The evidence favours the first; the owner's assertions favour the
second. Whichever is chosen, the other's existence is the reason the primary is provisional.

**Reads.** `inventory.md`; the JSON for quotes.

**Writes.** `personas.md`. Header states the evidence base in one paragraph and carries the
**provisional** label (see *The honest problem*). Each persona is a card with the blocks above;
every block ends with its source line or `[?]`; every `[?]` is restated as a hypothesis in a
*Hypotheses* section at the end of the file, in the lesson's form: *we assume X; we would check it
by Y.*

**Done when.** No persona differs from another only by demographics — if so, they are merged. No
block is unsourced and unmarked. Every block answers a named design question (which surface, which
state, which copy). The primary is chosen with an argument, and the argument names what would
overturn it.

### 4. Audit — the check for sagging

**Does.** The lesson's step 5, and the one it says the author does well against their own work when
asked directly. Every claim in `personas.md` classified as **confirmed by research / hypothesis /
invented**, in a table. Then the dangerous list: claims that **bear on a design decision** and stand
on `[?]` or on invention. Then three pointed questions that would close the biggest gaps, each with
where the answer would be found.

**Reads.** `personas.md`, `inventory.md`.

**Writes.** `audit.md` — the classification table, the dangerous list, the three questions. Anything
found *invented* is removed from `personas.md` or converted to a marked hypothesis; the audit records
what changed.

**Done when.** The table covers every sentence with a factual claim. The dangerous list is
non-empty (it will be — see below) and each row names the decision it endangers. Each of the three
questions names an instrument that exists.

### 5. Targeted re-research — one question, surgically

**Does.** Takes the first question from the audit and answers it with the tools of stages 1–3, at
point scale: one question, one collection, one update. Not a restart. The lesson's instrument is
web fetch of reviews and forums; ours has no product reviews to read, so the instruments are the
ones that see practitioners rather than vendors:

- **Public behaviour on GitHub** — repositories containing `.claude/skills`, `.claude/agents`,
  `CLAUDE.md`, `.cursor/rules`, `AGENTS.md`; dotfiles repos with agent material in them;
  awesome-lists of skills and their forks. This is observable evidence of where material lives and
  how many targets one person keeps, and it costs one API session.
- **Forum threads** — practitioner discussion of keeping and reusing skills, prompts and MCP
  configs across projects (Hacker News, the Claude and Cursor communities), read for *friction*,
  which the trackers cannot see. Quoted with URL; weighted by nothing, since forums have no
  reaction ranking worth trusting.
- **The remainder of the tracker JSON** — issues ranked but not yet read.

**Reads.** `audit.md` question 1; whatever the instrument returns.

**Writes.** `re-research.md` in this folder — a **source document**, not a digest entry: the
question, the instrument, what was collected (logged, as stages 1–3 logged captures), what it
established. Then the affected rows in `personas.md`: a confirmed `[?]` is lifted with the new
source beside it; a refuted claim is corrected and the correction noted in the card. No other file
changes. The digest ([`research.md`](../research.md)) gains a subsection *after* the source document
exists, never before.

**Done when.** One question is closed or explicitly not closable with these instruments. Every
lifted `[?]` has a source line. No `[?]` was lifted without new data — the lesson's last follow-up
prompt is the test.

### 6. Page — `personas.html`

**Does.** One page for a human reader, in the identity of [`research.html`](../research.html):
persona cards with the primary marked, and — once stage 7 exists — the job hierarchy and the
matrix as a table. `[?]` and *hypothesis* marks stay visible on the page; the lesson's reason is
the right one: the honesty of the personas should be visible to whoever is shown them.

**Reads.** `personas.md`, and stage 7's `jtbd.md` when it exists.

**Writes.** `personas.html` beside this file. [`vercel.json`](../../vercel.json) serves the research
page at the root with clean URLs; this page is reachable at `/research/6-personas/personas` and
`research.html` links to it. No new rewrite needed; the cache header pattern is copied.

**Done when.** Every card and cell on the page traces to a line in the markdown. Built after step 4,
never before — a page built from an unaudited file publishes the invention.

### 7. Hand back

**Does.** The lesson's step 8 adds a block to CLAUDE.md — primary persona in 2–3 lines, the main job,
the top three jobs. This repository's protocol is that the spec is edited by the owner on a
proposal, and that the register in [`research-plan.md`](../research-plan.md) is the only list of open
questions. So this step **writes the proposal, not the spec**: the block for CLAUDE.md, the digest
section for `research.md`, and any register entries the audit produced (next ID after the last one
in the register; which stage raised it; what would answer it).

**Writes.** A *Proposals* section at the end of `audit.md`, quoted as markdown, ready to apply.

**Done when.** The owner can apply each proposal without reading the stage.

---

## Output files

| File | What it holds |
|---|---|
| `inventory.md` | What the repository says about people, what the owner asserts, what nobody knows. Plus the behavioural axes. |
| `personas.md` | 2–4 personas, one primary, every block sourced or `[?]`, hypotheses at the end. **Provisional** until the lifting event below. |
| `audit.md` | Confirmed / hypothesis / invented, the dangerous list, three questions, and the proposals for CLAUDE.md, the digest and the register. |
| `re-research.md` | Source document for the one question closed at point scale — instrument, log, result. |
| `interview-guide.md` | The three audit questions and the primary-persona choice, written as a 30-minute conversation guide, so that the Q5 trigger has an instrument ready the day it fires. |
| `personas.html` | The human-readable page, in the research page's identity. Built last. |

---

## The evidence rule, for this repository

Every claim carries its source, as a repo-relative path or a URL, on the same line or the line
after. Anything without one is marked `[?]`, is worded as a hypothesis — *we assume X; we would
check it by Y* — and lives in the *Hypotheses* section, never in the main body of a card.

Where the sources actually are:

- **Pain, with weight** — [`3-pain/user-pain.md`](../3-pain/user-pain.md) and its JSON. Cite the
  issue URL and its reaction count, because the count is the only weighting this repository has.
- **Positioning** — [`1-landscape/comparison.md`](../1-landscape/comparison.md) and
  [`competitors.md`](../1-landscape/competitors.md). Cite as *what vendor X sells against*, never as
  *what users want*.
- **Mechanisms and the states a person must read** — the flow captures under
  [`2-flows/`](../2-flows/README.md), addressed through the notes files that cite them.
- **Instrument limits** — the *method* section of `user-pain.md` and the *finalisation* section of
  [`4-benchmark/benchmark.md`](../4-benchmark/benchmark.md). A claim that leans on a stage must respect
  what that stage said it could not see.
- **Owner's assertions** — [`CLAUDE.md`](../../CLAUDE.md), cited as such: *stated in §3, not observed.*

**Superseded 2026-09-07 — there are now three marks, not two.** The scale is defined once, in
[`research.md`](../research.md), *The three marks*: **✓** confirmed by a re-runnable instrument · **★**
reported by a practitioner in an interview · **`?`** unknown. The stage documents write the third as
`[?]` and the digest writes it as **`данные не подтверждены`**; those two are the same level in two
registers, and each keeps its own wording. **A ★ never becomes a ✓ by repetition** — only an
instrument promotes it.

---

## The honest problem

**We have no interviews, no analytics and no users.** The phase read fifteen vendors, captured
about 140 frames of other people's products, and queried two issue trackers. That is the entire
evidence base about people, and stage 3 said what it is worth: a tracker sees breakage, not
friction, so two of the three candidate pains are invisible to it by construction. Q5 — *loss or
reassembly cost, which drives adoption?* — was deferred on 2026-09-02 precisely because nothing in
this repository can answer it, with the trigger written down: *ask five practitioners before the
first feature that only pays off under one answer.* Stage 6 does not change that. It makes the gap
legible by giving it a face.

**What fraction will be hypothesis.** Block by block, honestly:

| Block | Expected standing on first pass |
|---|---|
| Context — the situation they arrive from | Mostly `[?]`. The trackers show the *moment of breakage*; nothing shows what the person was doing an hour before. |
| Jobs and pains — breakage at handover, silent collision, env and secrets | **Sourced**, with reaction counts. This is the one block that stands on observation. |
| Jobs and pains — loss, reassembly, finding one's own material | `[?]` entirely. Blind spot by construction. |
| Trust triggers | Half and half: what vendors chose to show is sourced; whether it works on anyone is `[?]`. §5's own decision (usage facts, never a score) is an owner's call, not a trigger observed. |
| Quote | Sourced, by rule. |
| Environment — targets, where material lives, who else opens the archive | `[?]` until step 5's GitHub search, which can turn *where material lives* and *how many targets* into observations. |
| Why they would adopt at all | `[?]` — and no step in this stage can lift it. |

Roughly **half of every card, and all of the part that decides positioning**, will be hypothesis.
The primary persona will be chosen on the half that is sourced, which biases the choice toward the
person the trackers can see — the one who breaks at handover — and against the collector the spec
describes. That bias is the instrument's, and the file must say so where the choice is made.

**The label.** The personas ship marked **provisional**, in the header of `personas.md` and on every
card of `personas.html`. The label lifts per claim as sources arrive, and lifts from the document
when one event has happened: **the five practitioner conversations that Q5 already names**, run
against `interview-guide.md`, with notes filed in this folder as a source document. Five is the
number the register wrote down; it is the smallest number that can refute a primary-persona choice
rather than merely colour it. A seeded library in the hands of one real user would lift the
*environment* and *density* rows (G4, G5) but not the adoption row; it is a second event, not a
substitute for the first.

**What this stage is allowed to conclude anyway.** A persona whose pains are sourced and whose
adoption story is `[?]` is still worth having — it can settle every conflict about the check, the
handover and the copy, which is where the value was found to concentrate. It cannot settle a
conflict about the Library screen or positioning, and it must not pretend to.

---

## Definition of done

- [ ] `inventory.md` — observed / asserted / not-known, every observed row with a path or URL,
      every owner's assertion listed as such, the not-known list containing at least the eight
      questions named in step 1
- [ ] Behavioural axes chosen, none demographic, each with evidence at both ends or set aside
- [ ] `personas.md` — 2–4 personas, one primary chosen with an argument that names what would
      overturn it, every block sourced or `[?]`, hypotheses in their own section, **provisional** in
      the header
- [ ] `audit.md` — every factual claim classified, the dangerous list with the decision each row
      endangers, three questions each with a named instrument
- [ ] `re-research.md` — one audit question closed or declared unclosable, as a source document;
      every lifted `[?]` carrying its new source
- [ ] `interview-guide.md` — the instrument for the lifting event, ready before it is needed
- [ ] `personas.html` — built from the audited files, marks visible, linked from `research.html`
- [ ] Proposals for CLAUDE.md, the digest and the register written into `audit.md` and **not
      applied** by this stage
- [ ] Nothing in this stage edits CLAUDE.md §8. If a persona refutes a surface, that is a register
      entry, not an edit
