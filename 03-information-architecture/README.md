# Lesson 03 — Information architecture

**A plan, not a result.** Written 2026-09-15, the day lesson 03 started, and **renumbered on
2026-09-20 to the course's own seven steps** once its prompt pack was read — the ten steps this file
opened with were our invention, and five of the seven were already done under other numbers. The
mapping, and where our four extra steps went, is in *Steps*. The method is the course's
lesson 3 — entities, sitemap from jobs, navigation, flows, traceability, critique, page — adapted to a
product whose **surfaces are already chosen**. [`CLAUDE.md`](../CLAUDE.md) §8 names four of them and the seam
between them, decided 2026-09-01 and confirmed 2026-09-02. That fact is the whole difficulty of this
lesson and it is dealt with under *What it is not*.

**Status, 2026-09-16: steps 2a and 2b are written, and the tree half of step 3.**
[`sitemap.md`](sitemap.md) holds the **entity inventory** — **sixteen** objects with their fields, the
job that raises each and whose side it is on, plus **eleven candidates refused for a stated reason**,
**two of which have since left the table because the owner applied them**: the licence and
`defersTo` — and the **screen tree**: **six screens and one orphan**, four for the owner and two for
the receiver, plus two nodes that are not screens, derived from the jobs, grouped by the person's three
situations, with the persona split and a list of the things that are states rather than screens. **Two
further sections record where the decisions meet each other** — one for 2026-09-15 and one for the
three the owner took on **2026-09-16**, whose finding is that they all land on the same overlay.
**Step 4, navigation, is written** — two global entries with the job cluster behind each, **three
clicks from the first screen to an archive** and four on the persona's most frequent arrival, and the
global / contextual / deep split. **And [`flows.md`](flows.md) walks five real paths through it** —
the main job and RJ-1 to RJ-4 — which **returned no new screen** and three consequences the static map
could not show. **Routes are still not written**, and the two questions the tree handed the
classification are both answered: **`Item` is a form** and **`Run` is a mode**.

**Status, 2026-09-20: the builder's adding mechanism changed, and the record was brought up to it.**
Four register entries were raised and answered the same day (Q14–Q17). **The `⌘K` palette is replaced
by a library panel inside `Project`** — a scope switch over `kind` tabs, `Related` first and default,
read-and-add only — **and the Library leaves the assembly path**, becoming the curator's room.
**A single item exports on its own**, the dependency walk still running. **An empty project is an
empty state whose one primary control is inert**, the product's one named exception, **and its one
action enters a *configuring* mode** — the panel, the checkbox and the `✕` live there and nowhere else,
which costs path B a fourth click and is counted rather than absorbed. **Deleting a
library item is confirmed rather than refused.** Every step that exists was re-checked against them —
**steps 1 and 5 were never started, and steps 3 and 5 gained new questions rather than answers.**
**The place count held at five**, and [`flows.md`](flows.md) now walks **six paths in seven diagrams** — the main
job **lost four nodes and four edges**, because the panel absorbed an excursion and Q16 removed a
branch. **No numbered step advanced on 2026-09-20; the existing ones were made true again** — and then the
owner accepted the flows and **a sixth section, Traceability, was added to `sitemap.md`**: every job
against every surface, with the orphan lists. **One orphan column** — library import/export as JSON,
which three separate instruments have now called an orphan — and **two orphan rows**, `SJ-2` and
`H-J5`, **neither of which can be honestly filled**: the product declines the first and is incapable
of the second. Each orphan carries a decision. **Like `flows.md`, it is a check across steps rather
than a numbered step of its own.**

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
is addressable, what a screen is made of, what the library panel can reach, what an item card carries in the
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

**4. Smoothing over the load §8 deliberately took on.** ~~§8 bought a known cost: *with no library pane
in the builder you cannot see what you are not using*, and three things carry that weight — the
palette opening on **related** items, the Library being one keystroke away and remembering where you
were, and per-item usage facts.~~ **Superseded 2026-09-20, Q14 — and read the change carefully, because
this trap is the one it is easiest to claim was sprung.** The owner **did** restore a library panel,
and the lesson did **not** do it quietly: it went to the register as an entry, was answered by the
owner, and carried a correction of the record — the score that killed a pane in stage 5 assumed the
check lived in the right-hand pane, and it has had its own surface since 2026-09-02. **The trap was
never *a pane is forbidden*; it was *a pane arriving by drift rather than by decision.*** The
obligation the trap names survives intact: **the IA has to show where the weight lands**, and the
three mitigations are rewritten rather than dropped in `sitemap.md` §Navigation — `Related` first in
the panel, the Library one keystroke away for corpus acts only, and per-item usage facts unchanged.
**A sidebar of *everything*, with no `Related` and no scope, would still spring it.**

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

> **Renumbered 2026-09-20 to the course's own seven.** This plan was written on 2026-09-15 with **ten
> steps of our own invention**, before the lesson's prompt pack was read. The pack has **seven**, and
> since this work is homework for that course, **its list wins.** Nothing that was done is discarded:
> five of the seven were already finished under other numbers, one addition we made is kept and marked
> as an addition, and **four of our ten leave the lesson** — with where each went written down rather
> than dropped. **The old numbers appear in `sitemap.md`, `flows.md` and the register**, and the
> mapping below is what reconciles them.

| Course step | Output | Our old number | State |
|---|---|---|---|
| **1** Entity inventory | `sitemap.md` §Entities | 2a | **done** 2026-09-15 |
| **—** *our addition:* place / mode / overlay / state | `sitemap.md` §Places | 2b | **done** 2026-09-15, amended 09-16 and 09-20 |
| **2** Sitemap from jobs, not from a menu | `sitemap.md` §Screens | 3, tree half | **done** 2026-09-15 |
| **3** Navigation model | `sitemap.md` §Navigation | 4 | **done** 2026-09-16, recounted 09-20 |
| **4** User flows in Mermaid | `flows.md` | unnumbered | **done** 2026-09-16, revised and accepted 09-20 |
| **5** Traceability matrix | `sitemap.md` §Traceability | unnumbered | **done** 2026-09-20, all seven findings disposed of |
| **6** IA critique | a defect table, then separate fixes | 9 | **not started** |
| **7** `ia.html` and the live documents | `ia.html`, `CLAUDE.md`, `README.md` | 10 | **not started** |

---

### 1 · Entity inventory — **done 2026-09-15**

The course's first step: *before designing screens, inventory the objects a person deals with in order
to close their jobs.* Each entity with its fields, **the job that raises it**, and what it is related
to. An entity with no job goes to a *in question* section, not the main list; anything assumed is
marked `[?]`.

**Output:** [`sitemap.md`](sitemap.md) §Entities — **sixteen entities**, each with fields, job, relation
and standing, plus **eleven candidates refused for a stated reason**. Two of the eleven have since been
applied by the owner (the licence, `defersTo`).

### — · Places, modes, overlays and states — **our addition, done 2026-09-15**

**Not in the course's seven, and kept.** The screen tree is a hierarchy; this asks what each node *is*,
on one test — *could somebody be sent there and arrive*. **It earned its place three times**: it
answered *is `Item` a place* and *is `Run` a place*, it kept the count at **five places** when the
library panel replaced the palette, and it is what classified the configuring mode on 2026-09-20.

**Output:** [`sitemap.md`](sitemap.md) §Places.

### 2 · Sitemap from jobs, not from a menu — **done 2026-09-15**

*An indented text tree, every node carrying the job it serves, grouped by the person's logic and not by
site sections; a screen with no job is marked `[ORPHAN]`; states are not screens; depth kept minimal.*

**Output:** [`sitemap.md`](sitemap.md) §Screens — six screens, one orphan, four nodes that are not
screens, with the persona split and a list of the things that are states rather than screens.

**What our old plan added here and the course does not ask for: route strings.** Literal addresses were
our own idea. **They are not written and this lesson does not owe them** — the course asks for a
*navigation model*, which is step 3, and the addressability rules are in §Places. **The three open
address questions stay recorded and unanswered**: whether the panel's scope and tab belong in the
Project's address, whether the configuring mode survives a reload, and where the agent target lives now
that a single item can be exported without a project.

### 3 · Navigation model — **done 2026-09-16, recounted 2026-09-20**

*Three to five global entries, each an entrance to a job cluster with the job named; **count the taps**
from the first screen to the main job for the primary persona; if more than three, restructure and
explain the compromise; then split global / contextual / deep.*

**Output:** [`sitemap.md`](sitemap.md) §Navigation. **Two global entries, not three to five** — and the
deviation is argued rather than quietly taken: a third cluster exists and its screen is a mode, so an
entry would point at something you cannot be sent to. **Depth: three to the archive**, which is the
furthest point this product owns, **four on the persona's most frequent arrival** and **four for a set
that does not exist yet** since the configuring mode was added. **Both fours are named with their
compromise**, as the course asks.

### 4 · User flows in Mermaid — **done 2026-09-16, revised and accepted 2026-09-20**

*The main job in full plus two or three related ones; screens as nodes named from the sitemap; decisions
as diamonds with yes/no branches; **states as their own nodes** — empty, error, loading; **both kinds of
ending**, success and the places a person gets stuck; every node must exist in the sitemap; valid
Mermaid that renders on GitHub; a list of decisions and states in words under each diagram.*

**Output:** [`flows.md`](flows.md) — **six flows in seven diagrams**, more than the course asks for: the
main job, RJ-1 to RJ-4 and the single-item export. **Rendered and measured in a browser at an 880-pixel
column**, not merely parsed, because a parser passes a diagram nobody can read.

**One thing to carry into step 6 rather than defend.** The course names **empty, error and loading** as
the states a flow must show. Ours have **empty** in several forms and **void**, **stale** and
**checking** besides — and **no `loading` node anywhere, and no `error` node anywhere.** ~~Some of that is honest (the product is local, with no network in the MVP)~~ — **struck the same day
by Q24: the product is online, with a backend and accounts, so none of it is honest.** **Every read and
every write crosses a network**, which makes `loading` a real state on every surface and `error` a real
state wherever a request can fail: a revoked link opened by a receiver, an archive that fails to build,
a save that does not land, a session that has expired. **Step 6 inherits a larger gap than it was
written to expect.** **Step 6 is where that gets settled, not here.**

### 5 · Traceability matrix — **done 2026-09-20**

*Rows are every job, columns every screen, `✓` where the screen really takes part in closing the job;
then two defect lists — orphan screens and orphan jobs — and a decision for each: delete, add, attach,
or backlog.*

**Output:** [`sitemap.md`](sitemap.md) §Traceability — 17 jobs against 12 surfaces, sourced jobs and
hypotheses in separate blocks. **One orphan column, two orphan rows, and two defect classes the exercise
was not asked for.** All seven findings were put to the owner and disposed of the same day: Q12 closed
as refused, Q18 to Q23 answered.

**Where we did not reach the course's goal, and it is deliberate.** *No empty row and no empty column*
is achievable for the column and **not for two of the rows**: `SJ-2` is a job the product declines in
writing and `H-J5` is one it is incapable of. **Inventing a `✓` for either would make the matrix a
decoration.** Every orphan carries a decision instead, which is the part that was reachable.

### 6 · IA critique — **written 2026-09-20, fixes not applied**

*A close reading of `sitemap.md` and `flows.md` against four defect classes, returned as a table of
**where · what · how to fix**. **Change nothing silently**: the list first, the fixes proposed
separately. Dead ends and missing states are the most dangerous and go first.*

| # | Class | What it will probably bite on here |
|---|---|---|
| **1** | **Dead ends** — a *no* branch that leads nowhere, an error or empty with no way on | Ten endings across seven diagrams, and **two are outside the product by design** (env values on the receiving machine, copies a revoked link cannot recall). The critique has to separate *a dead end we built* from *a limit we drew honestly* — and **the auto-added row that will not go** is the one to argue about |
| **2** | **Missing states** — a happy path with no empty, error or loading | **The known gap**, stated in step 4 above. No `loading` node and no `error` node in the whole file |
| **3** | **Excess depth** — the main job or a frequent related job further than three taps | **Two paths sit at four** and both are already named with their compromise. The critique's job is to decide whether naming is enough |
| **4** | **Orphans** — check against the matrix, **do not build a new one** | One orphan column re-justified as `[§10]`, two orphan rows disposed of. The critique should test whether the re-justification holds or is special pleading |

**Output:** [`ia-critique.md`](ia-critique.md) — **written**. Sixteen defects across the four classes,
plus **one finding outside them and it is the largest: the receiver's path is not drawn.** Seven jobs
sit on `Shared project` and no diagram starts at *somebody sent me a link*.

**The fixes are proposed and none is applied**, which is the method's rule and it has earned itself
three times this week. **The list is ordered**; the sharpest items are that **RJ-2b's dead end
contradicts §6** — a Problem you cannot fix from its row is not an ending, because export is never
disabled and the main flow draws exactly that route — and that **two pairs of diagrams answer the same
situation two different ways.** **One defect is a regression from this morning**: removing the palette
excursion took first-run empty `My library` out of every flow with it.

**`loading` is deliberately not on the fix list.** It belongs to lesson 04: putting spinners in seven
diagrams before deciding what waiting looks like is trap 2.

### 7 · `ia.html` and the live documents — **not started**

*One clean page assembled from `sitemap.md` and `flows.md`: the tree with the job beside each screen,
every flow rendered as Mermaid, the traceability matrix as a table with orphans highlighted. Dark,
clean, in the language of `research.html` and `personas.html`. Then update the live documents.*

**Three deliverables, and two of them are not the page:**

1. **`ia.html`** — built the way the other two pages are, by a script in [`tools/`](../tools/), never
   hand-edited, and carrying the **twelve-phase strip** both page templates already have. **Mermaid
   from a CDN, initialised on the dark theme** — and note the diagrams were authored **outline-only**
   so they read on either theme, which is the same rule §10 sets for the product.
2. **`CLAUDE.md`** — the course asks for the top-level sitemap, the main flow, the global navigation and
   the depth to the main job, stated briefly. **Most of this file's IA content arrived piecemeal
   through Q14 to Q23**; this is where it gets one coherent place instead of eight dated amendments.
3. **`README.md`** at the repository root — a *Structure* section saying what lives in `sitemap.md` and
   `flows.md`.

**And one conditional the course states and we should honour**: *if building the IA found a hole in the
data, patch `research.md`.* **It did** — the traceability matrix is the first document to state `H-J5`
as importance 3 with no surface, and `EJ-3` as touched-but-unclosable.

---

### What left the lesson, and where each piece went

**Four of our ten steps are not in the course's list.** None is deleted; each has a home.

| Our old step | Where it goes | Why |
|---|---|---|
| **1** Fixed points — what this lesson may not re-decide | **Dropped, and the reason is that the work it was insurance against did not happen.** It was a guard against transcribing §8 instead of deriving from it. **The lesson demonstrably derived**: it produced a panel, a mode, a matrix and eight register entries, and §8 was changed by the register rather than copied into a tree. *A guard that was never needed is cheaper to retire than to perform.* |
| **5** What each surface is made of, in named regions | **Lesson 04, prototyping and wireframing** | *What a screen is made of* is a wireframe. It arrives there carrying four things lesson 03 found: the `Item` overlay's three disclosures and its third door, the note count that can never reach zero, the detached copy nobody is told about, and the panel's width against the project row |
| **6** The item in six contexts and six states | **Lesson 04** | The same reason, and it is still **partly blocked by S-2** — whether an item addresses a directory rather than a file |
| **7** Where a finding lives | **Half answered already, half to lesson 04** | §8 settles the common case — *a finding annotates the row that owns it* — and the flows confirmed it. What is left is the finding belonging to no row, which is a composition question |
| **8** Taxonomy, filters, the shelf's sort | **Lesson 04, and partly blocked** | **Q19 settled on 2026-09-20 that sorting, ranking and recommending get no design until Q9 has an answer**, and Q9 is deferred |

---

## Output files

| File | What it is |
|---|---|
| `README.md` | This plan. |
| [`sitemap.md`](sitemap.md) | The work, **six sections** — Entities, Screens, Places, Navigation, Traceability, plus the dated blocks recording where the decisions meet each other. The source of truth for structure, subordinate to `CLAUDE.md` in every conflict. |
| [`flows.md`](flows.md) | **User flows in Mermaid** — six flows in seven diagrams, each with its decisions, its states and both kinds of ending. **Derived from `sitemap.md` and adding nothing to it**: every node is a screen, mode, overlay, region or state that already existed. |
| `ia-critique.md` | **Step 6.** The defect table — where · what · how to fix — then the fixes proposed separately and applied visibly. |
| `ia.html` | **Step 7.** Generated by a script in [`tools/`](../tools/) — never hand-edited. |

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

**Rewritten 2026-09-20 against the course's seven steps.** Four lines left with the four steps that
left the lesson; they are in lesson 04's brief instead.

- [x] Every entity carries its fields, its job with a link, and its relation — and every object with
      no job is refused in *In question* with a reason
- [x] Every noun classified as place, mode, overlay, region or state, with the borderline cases argued
      rather than asserted
- [x] Every screen in the tree carries the job it serves, or the mark that says it does not
- [x] A navigation model with the taps to the main job counted, and every count above three named with
      its compromise
- [x] §8's three load-bearing mitigations each visible in the navigation model, and each re-homed or
      struck when the panel replaced the palette
- [x] User flows in valid Mermaid, every node existing in `sitemap.md`, decisions and states listed in
      words underneath, **and both kinds of ending**
- [x] A coverage matrix with both orphan lists, and **a decision for every orphan**
- [x] Nothing in the map requires a feature §9 refuses
- [ ] `ia-critique.md` written — four defect classes, a table of where · what · how to fix — and the
      fixes applied **separately and visibly**, nothing changed silently
- [ ] `ia.html` generated, carrying the tree, all seven diagrams and the matrix
- [ ] `CLAUDE.md` carrying the top-level sitemap, the main flow, the global navigation and the depth
      to the main job **in one place** rather than in eight dated amendments
- [ ] The root `README.md` carrying a *Structure* section
- [x] ~~Proposals handed to the register; **`CLAUDE.md` untouched**~~ — **superseded.** The owner
      answered ten register entries between 2026-09-15 and 2026-09-20 and applied them to `CLAUDE.md`
      the same days. **The protocol held**: every change went through the register first, which is what
      the line was protecting; what it got wrong was assuming the sitting would be late rather than
      continuous.
