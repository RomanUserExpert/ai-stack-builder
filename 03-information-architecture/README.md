# Lesson 03 — Information architecture

**A plan, not a result.** Written 2026-09-15, the day lesson 03 started. The method is the course's
lesson 3 — object model, surface map, navigation, screen composition — adapted to a product whose
**surfaces are already chosen**. [`CLAUDE.md`](../CLAUDE.md) §8 names four of them and the seam
between them, decided 2026-09-01 and confirmed 2026-09-02. That fact is the whole difficulty of this
lesson and it is dealt with under *What it is not*.

**Status, 2026-09-15: step 2a and the tree half of step 3 are written.** [`sitemap.md`](sitemap.md)
holds the **entity inventory** — **sixteen** objects with their fields, the job that raises each and
whose side it is on, plus **eleven candidates refused for a stated reason** — and the **screen tree**:
**seven screens and one orphan**, five for the owner and two for the receiver, derived from the jobs,
grouped by the person's three situations, with the persona split and a list of the things that are
states rather than screens. **A fourth section records where the day's decisions meet each other**,
including one collision that still needs an answer. **Routes and the
place/state classification are not done**, and the tree hands them two questions: *is `Item` a place or
a form*, and *is `Run` a place at all* now that nothing is stored.

**The order moved, deliberately, and step 2b then closed what the tree opened.** The tree was drawn
before the classification because the owner asked for the hierarchy first, and it worked: a screen tree
with no addressability in it **produced** the classification's hardest questions rather than needing
them answered first. Both are now answered — ~~**`Item` is a place** (a proposal to §8, which calls it
a form)~~ **`Item` is a form: the proposal went to the owner on 2026-09-16 and §8 was kept** — and
**`Run` is a mode of the Project**, because nothing is stored and there is nothing to return to.
**Five places in the product**: Library with one address per scope, Projects, Project, and the two the
shared link creates.

**Where this folder sits, and why.** [`research/`](../research/) holds lessons 01 and 02 as seven
numbered stages. Every lesson after them is its own deliverable, so each gets a folder at the
repository root named the way the research stages are named: `03-information-architecture`, and later
`04-…`, `05-…`. No `lessons/` wrapper — it would add a level that holds nothing. **If this lesson
gets a page, `.vercelignore` is a whitelist and both page templates carry the twelve-phase strip**;
see [`tools/README.md`](../tools/README.md).

**And the condition this lesson runs under, recorded before its first line of work.** The register's
sitting has not happened. Lesson 03 was started anyway, on the owner's decision — *we work with what
we have* — and that decision is written into [`CLAUDE.md`](../CLAUDE.md) §1 and
[`research/research-plan.md`](../research/research-plan.md). **It changes the order of work and
nothing else.** Six register entries keep their dispositions, four proposal lists stay unapplied, the
*provisional* label stays on stages 6 and 7, and no mark is promoted. What it costs is named in
*The honest problem*.

---

## What this lesson is for

**§8 is a choice. A choice is not a structure.** Four surfaces and a seam tell you nothing about what
is addressable, what a screen is made of, what the palette can reach, what an item card carries in the
five places an item appears, or where a finding attaches. This lesson produces that, and produces it
**without appearance**: no colour, no type scale, no grid, no layout, no component named in a way that
implies a look. The boundary is the one [`5-patterns/patterns.md`](../research/5-patterns/patterns.md)
set for itself and it holds here — structure is lessons 03 and 04, appearance starts at 06.

The deliverable, said as four questions the next lesson cannot start without:

- **What places exist, and how does somebody arrive at each one?**
- **What is each place made of** — in named regions, in reading order, with the states each region has?
- **What does an item carry in every context it appears in, and in each of the six states of §7?**
- **Where does a finding live** — on the row that owns it, on the stage that found it, or on the set?

---

## What it is not — the specific way it goes wrong here

**1. Transcribing §8.** This is stage 7's trap in a new costume. §8 is four bullets; an information
architecture that restates them as a tree has produced nothing and will read as confirmation. **The
test applied to every step: its output either says something §8 does not say, or it cites §8 as
already settled.** Step 1 exists to make that distinction cheap rather than a matter of memory.

**2. Appearance creep.** A region is *what is in it and what it is for*, never *a 280px left rail*.
The moment a sentence needs a pixel, a colour or a font to be true, it belongs to lesson 06 or later.

**3. Inventing places for people nobody has met.** **P3's column in the jobs matrix is `[?]` in all
ten rows**, and the two clearest public beginners anyone found *wrote their own material on day one or
asked to shadow a human* rather than reaching for a shelf
([`re-research.md` round 4](../research/6-personas/re-research.md#round-4-the-matrixs-empty-cells) F5, F13).
An onboarding tour, a getting-started surface, a *recommended for you* sort — each is a structure for
a person who has never been observed. They may be drawn, but only **marked `[?]` and named as
hypotheses**, and never load-bearing for anything else in the map.

**4. Smoothing over the load §8 deliberately took on.** §8 bought a known cost: *with no library pane
in the builder you cannot see what you are not using*, and three things carry that weight — the
palette opening on **related** items, the Library being one keystroke away and remembering where you
were, and per-item usage facts. **The IA has to show where that weight lands.** Quietly restoring a
library pane, or a sidebar of *everything*, reverses a decision this lesson has no standing to
reverse.

**5. Building on proposals that are not applied.** Four lists wait for the sitting, and one of them
changes the shape of the central noun: **S-2 — an item addresses a directory, not a file**
([`re-research.md` round 3](../research/6-personas/re-research.md#round-3-five-questions-that-need-no-interview)). If it is taken, an item card
and the archive tree both change. **Draw against the spec as it stands, and name the dependency at
every point it touches.** Not pre-applied, not ignored.

**6. Deciding what §9 refused.** Versioning, composition, publishing, accounts. §9 also forbids a
screen that only makes sense once they exist. An IA is where that leaks in — an empty *History* tab is
a structure for a feature we are not building.

---

## Inputs

| Input | Kind | What it yields |
|---|---|---|
| [`CLAUDE.md`](../CLAUDE.md) §8 | **Decided.** | The four surfaces and the seam at Check. The fixed frame. Step 1 turns it into citable points. |
| [`CLAUDE.md`](../CLAUDE.md) §4, §5 | **Decided.** | The vocabulary every label in the map must use, and the entity shape behind every place — including `ProjectItem`, which is the noun the IA has to decide the *kind* of. |
| [`CLAUDE.md`](../CLAUDE.md) §6 | **Decided.** | What Run is made of: the walk, cycles as information, three severities, `.env.example`, the merge, the handover stages, the unclean-export confirmation. Structure, not logic, is what this lesson takes from it. |
| [`CLAUDE.md`](../CLAUDE.md) §7 | **Decided.** | Six item states, and the three commands state 6 carries. Every one has to have a place to be rendered in. |
| [`CLAUDE.md`](../CLAUDE.md) §9, §11 | **Decided.** | What must have no structure at all, and what ships in the box — two library scopes and one example project, which are three first-run states. |
| [`5-patterns/patterns.md`](../research/5-patterns/patterns.md) | Reasoned, stage 5. | Why this shape and not the other four, what each rejected variant donated, and the stated cost the map must expose rather than hide. |
| [`2-flows/`](../research/2-flows/README.md) 01, 02, 03, 04, 05, 07, 08, 11 | Captured mechanisms. | Item detail and trust; filter grammar and *name how many items are hidden*; relations without a canvas and the depth filter; the stage list with verdict, duration and expansion; drift computed and displayed; the env drawer; emptiness scaled to how new the concept is; two rows for cause and consequence. **Mechanisms to structure, never sitemaps to copy.** |
| [`4-benchmark/benchmark.md`](../research/4-benchmark/benchmark.md) | Rubric. | B1–B4 are four things a user does — find, assemble, check, hand over — and the finalisation says which two carry the value. Useful as a check that every one has a home. |
| [`6-personas/personas.md`](../research/6-personas/personas.md) | **Provisional.** | P1 is primary and wins structural conflicts. P2 has **never spoken in the first person**. P3 has never been observed. Read *What this card is allowed to settle* before leaning on any of it. |
| [`7-jobs-to-be-done/jtbd.md`](../research/7-jobs-to-be-done/jtbd.md) §7, §8 | **Provisional.** | Which jobs the structure must serve first, and the thirty `[?]` cells that say where it cannot know. §8's shortlist is under a recorded correction; read the note at its head. |
| [`research/research-plan.md`](../research/research-plan.md) — the register | Open questions. | **Q9** bears on what the shelf holds and how it sorts; **Q10** is a conflict with something outside the set that the model has nowhere to put; **Q12** is a want we cannot close. Each is a place the IA marks rather than answers. |
| The four proposal lists | **Pending, not applied.** | Constraints to name: **S-1** (`SETUP.md` carrying the set's Problems), **S-2** (item as a directory), **S-3** (a settings file is executable), **S-4** (the receiver's own secrets hazard), plus stage 6's nine and stage 7's nine. |
| [`research/research.md`](../research/research.md) | Digest. | Orientation only. **Never a source** — the spec, `FINAL.md` and the register outrank it by rule. |

**Not an input:** the course's demo IA, and any competitor's sitemap. The flows are captured
*mechanisms*; a mechanism is evidence about behaviour, and a sitemap copied from a product with a
different data model is a shape with no argument under it.

---

## Steps

Nine, and the last three are one closing pass. Each step names its output section in
[`sitemap.md`](sitemap.md) so the document is assembled rather than written.

### 1. The fixed points — what this lesson may not re-decide

Every structural commitment already in the spec, in one table: what it fixes, which section says so,
and what it therefore forbids. Nothing is argued here; it is extracted.

**Output:** `sitemap.md` §1. **Rule it sets up:** from here on, *the spec says so* is a citation with a
section number or it is not a reason.

### 2a. The entities — **done 2026-09-15**

**Before anything is classified, what are the objects?** Every entity the person handles in order to
close a job, each with **its fields and parts**, **the job that raises it** with a link into
[`jtbd.md`](../research/7-jobs-to-be-done/jtbd.md), and **whose side it is on** — owner, consumer or
external author.

**The rule it obeys: an object earns its place by closing a job.** An object with no job goes to *In
question* whatever the specification says about it, and nothing is added because products of this kind
usually have one.

**Output:** [`sitemap.md`](sitemap.md), *Entities* and *In question*. **Fifteen and eleven.** Two
things came out of it that were not visible before: **§5 has no object for the check or for a finding**,
which §8 gives a whole surface, and **the best-evidenced entity in the product — `SETUP.md` — belongs
to the persona nobody has ever interviewed.**

### 2b. Nouns, and what kind of thing each one is

The same objects, classified: is each a **place** you can arrive at, a **state** of a place, a
**mode**, or an **overlay**?

**The rule that decides it:** *a noun is a place only if somebody could be sent there and arrive.*
`ProjectItem` and `finding` are the interesting cases and each gets its argument written out rather
than assumed.

**Output:** `sitemap.md` §2b.

### 3. The surface map, and the route shape

The four surfaces plus whatever is global, with nesting, and **page versus overlay** decided for each.
Then the route shape: §10 is Next.js, so a route is real and **a route is a promise about what is
addressable.** The questions this step must answer rather than leave: is a finished Run addressable ·
is item detail a page or an overlay · does the library scope live in the URL · what does a project row
link to.

**Output:** `sitemap.md` §3 — a tree and a route table.

### 4. Getting between places, and what is remembered

The palette's reach and its **cold state** (§8 says *related* items — that is a structural claim with
a mechanism behind it), the seam at Check, what Back does from Run, what survives a reload, and the
Library remembering where you were. **Each entry says which of §8's three load-bearing mitigations it
implements**, so trap 4 is visible rather than avoided by silence.

**Output:** `sitemap.md` §4.

### 5. What each surface is made of

Named regions in reading order, per surface: what is always there, what appears only in a state, and
what each region is *for*. Then **the three first-run states**, which §11 makes real rather than
hypothetical: `My library` empty beside a full shelf · Projects holding only the example project · a
Project with nothing in it yet. Flow 08's rule governs the register of each — *scale the explanation
to how new the concept is.*

**Output:** `sitemap.md` §5.

### 6. The item, in every context and every state

One table of **six** contexts — library row, public-shelf row, project row, palette result,
archive-tree leaf, **and the shared page somebody else opens** (added 2026-09-15 with Q13) — against
what an item carries in each. **The sixth is the hard one**: it is read by a person who wrote none of
it, and it is the only context where getting it wrong is visible outside this machine. Then §7's six states against those contexts, saying
**which context has to be able to render which state**, and where state 6's three commands live. Plus
what a card **never** claims: no score, no rating, no eval result, no badge (§5), against the usage
facts it does carry.

**This is the deliverable [`CLAUDE.md`](../CLAUDE.md) §1 names for this lesson** — *what an item card
carries*. **And it is where S-2 lands:** if an item is a directory, this table changes. Say so in it.

**Output:** `sitemap.md` §6.

### 7. Where a finding lives

Three severities (§6) against three candidate homes: the row that owns it, the stage that found it,
and the set. §8 already says a finding annotates the row that owns it — this step has to handle the
finding that belongs to **no** row, since a missing env key and a merge collision are properties of
the set. Run's stage list as a structure — verdict, duration, expansion, in flow 04's shape — the
handover stages, and where the unclean-export confirmation sits relative to the finding that caused
it.

**Output:** `sitemap.md` §7.

### 8. Taxonomy, filters, search — and the one sort we cannot decide

Six kinds, tags, what a filter chip says, and flow 02's rule that a filtered-to-zero state **names how
many items are hidden** and never claims there are none. Search scope: does it cross the two library
scopes. **And the shelf's sort order, which is Q9 and gets a marked placeholder rather than an
answer** — *provenance over volume* is the only shape any observed person has endorsed, on four
practitioners in a self-selecting venue, and that is not enough to fix an order.

**Output:** `sitemap.md` §8.

### 9. The closing pass — mark, audit, hand back

**9a — the marked list.** Every structural decision that needed a cell nobody has filled, with the
register entry it belongs to. This is the rule [`CLAUDE.md`](../CLAUDE.md) §1 now sets for work done
before the sitting: *name the missing cell at the point of the decision and leave the decision
marked.*

**9b — the audit.** Every claim in `sitemap.md` classified **fixed by the spec** / **derived, with the
derivation shown** / **invented**, in the manner of
[`personas-and-jobs-critique.md`](../research/personas-and-jobs-critique.md), which found 27 invented
claims in 238. **An information architecture is where invention hides best, because a structure looks
inevitable the moment it is drawn.** Filed as `ia-critique.md` so it can be read as an audit, and
applied in place with the pass recorded in `sitemap.md`.

**9c — reconcile and hand back.** Proposals to the register, in the established form — *what was found
· what is proposed · which entry it belongs to*. **Nothing is written into `CLAUDE.md`.** A lesson may
narrow a claim and raise an entry; the owner edits the spec.

### 10. The page — phase 03

Last, and not part of the IA's correctness. Built the way the other two are: the shared `<style>`
block lifted from `research-page.tpl.html`, the twelve-phase strip updated in **both** templates, the
file added to `.vercelignore`, which is a whitelist. See [`tools/README.md`](../tools/README.md).

---

## Output files

| File | What it is |
|---|---|
| `README.md` | This plan. |
| [`sitemap.md`](sitemap.md) | The work, sections 1–8 plus the marked list — **the entity inventory is written**. The source of truth for structure, subordinate to `CLAUDE.md` in every conflict. |
| `ia-critique.md` | Step 9b. Claim-by-claim, with its application recorded in `sitemap.md`. |
| `ia.html` | Step 10, if it is built. Generated — never hand-edited. |

---

## The evidence rule, for this repository

The three marks hold, defined once in [`research/research.md`](../research/research.md): **`✓`**
confirmed by an instrument another person can re-run · **`*`** reported by one practitioner · **`[?]`**
unknown. **A `*` never becomes a `✓` by repetition**, and a re-runnable query proves something was
*said*, not that it is *true* (rule 5).

**This lesson adds a fourth kind of line, because most of its claims are neither observations nor
guesses:** **`§`** — *decided in the specification*, with the section number. A `§` line needs no
evidence and carries none; it is a citation.

**And the rule that matters here:** **a structure derived from a `[?]` is itself `[?]`**, however
obvious it looks once drawn. That is the failure mode step 9b exists to catch.

---

## The honest problem

**Three, and the first is new to this lesson.**

**The spec has pending amendments, and one of them is the central noun.** S-2 would make an item a
directory. The IA is drawn against the spec as it stands, so §6 of `sitemap.md` is being written against a
shape that has a known, unapplied proposal to change it. That is the cost of starting before the
sitting, it is accepted deliberately, and the way it is paid is by naming the dependency wherever it
touches rather than by guessing which way the sitting will go.

**Two of three personas cannot answer a structural question.** P2 has never spoken in the first
person — four rounds, five venues, every account of a handover written by the sender. P3 has never been
observed at all. So **every structure for arriving with nothing, and every structure for receiving,
is invention** until somebody is asked. The map may contain them; it may not rest on them.

**And nothing here can be validated by use.** There are no users. The only tests available before
lesson 04 are internal: consistency with the spec, and whether each job in the matrix has a home. That
is a weaker test than it will feel while passing it.

---

## Definition of done

- [ ] `sitemap.md` §1 lists every fixed point with its section number
- [x] Every entity in §2a carries its fields, its job with a link, and its relation — and every
      object with no job is refused in *In question* with a reason
- [x] Every noun in §2b classified, with the borderline cases argued rather than asserted
- [ ] A route table, and every route a promise about something addressable
- [ ] §8's three load-bearing mitigations each visible in the navigation model
- [ ] Every surface composed in named regions, plus the three first-run states
- [ ] The item table complete across six contexts and six states, with S-2's dependency named
- [ ] Every one of §6's three severities has a home, including the finding that belongs to no row
- [ ] Nothing in the map requires a feature §9 refuses
- [ ] The marked list written, each entry naming its register entry
- [ ] `ia-critique.md` written and applied, with the pass recorded
- [ ] Proposals handed to the register; **`CLAUDE.md` untouched**
