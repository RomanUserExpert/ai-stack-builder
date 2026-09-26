# Screens of the main flow — lesson 04, step 1

> **Written 2026-09-26, out of [`sitemap.md`](../03-information-architecture/sitemap.md),
> [`flows.md`](../03-information-architecture/flows.md) and
> [`jtbd.md`](../research/7-jobs-to-be-done/jtbd.md) and nothing else.** This is the order for the next
> steps, not a wireframe: names, jobs, places in the flow, states. **The main flow only** — every other
> flow in the sitemap waits for step 8.

**The main flow is the main job's flow**, `flows.md` §*The main job*, walked by **P1, the keeper** —
the primary persona (Q7):

> *When something I have already got working has to live somewhere else — a second tool, a new
> machine, a container, a colleague's laptop — I want it to keep working there without me
> rediscovering everything it quietly depended on, so that the move costs me minutes instead of an
> afternoon of finding out what silently did not load.* — `jtbd.md` §1

Its route, from `sitemap.md` §Navigation, path B: **Projects → Project → configure → Check → Export.**
Four screens carry it.

---

## The table

`✓` — the state is real for this screen · `—` — the flow does not produce it.

| Screen | Empty | Error | Loading | Success |
|---|:-:|:-:|:-:|:-:|
| **Projects** | ✓ | ✓ | ✓ | — |
| **Project** | ✓ | ✓ | ✓ | — |
| **Configuring the set — a mode** | ✓ | ✓ | ✓ | — |
| **Run** | — | ✓ | ✓ | ✓ |

**Success is marked once, and on purpose.** It means a separate *it worked* moment, and the main flow
has exactly one: **the archive is built and in hand**, at the end of `Run`. Opening a list, opening a
project and adding an item are ordinary views of data, not outcomes. **Where success is `—`, the base
page is the screen filled with real data**; where it is `✓`, success gets its own page. *That departs
from the course's "base page = success" and is written into `_conventions.md` in step 2.*

**Two of the four are modes, not places** (`sitemap.md` §Places, modes). They still get rows, because
each **changes the whole screen**: configuring brings the library panel and the `✕`; `Run` takes the
surface. A mode can be wireframed; it just has no address.

---

## Each screen

### 1 · Projects

- **Name in `sitemap.md`:** `Projects` — a place.
- **Job:** **MAIN** — *"Get back to the set I keep for that piece of work — and see whether it is still
  checked"* (`sitemap.md`, *Each screen, its job*). `H-J2` also lands here, importance `[?]`, and is not
  a reason for the screen.
- **Place in the flow:** the **first node** of the main job's diagram, and its first decision — *A
  project for this work?* It is the first screen on a first run because `My library` is empty by
  design and the example project lives here (`sitemap.md` §Navigation, 2).
- **States:**
  - **Empty ✓** — *no projects at all*. The example project is **deletable** (§11), so this is
    reachable; `flows.md` decision 2 calls it *the emptiest surface the owner can produce and the only
    one with no shelf to fall back on*. Way out: create a project.
  - **Error ✓** — the list fails to load, or **creating a project** fails (`flows.md`, *Waits and
    failures*). The product is online (Q24).
  - **Loading ✓** — *the `Projects` list on arrival* is a named wait.
  - **Success —** — a list is not an outcome. Creating a project lands you in `Project`, not on a
    confirmation.
- **Inside the filled page, as content rather than pages:** *only the example project* on first run ·
  each row's verdict as counts and date — **checked, never works** · **a stale verdict**, which shows the
  date and *what* voided it, never the old verdict greyed (§6) · a shared project reading as shared.
- **Find — search, filter, sort** (Q30, 2026-09-26). Search over project names, descriptions **and the
  items inside them**; one filter by what the last check said — *All · Problems at last check · Out of
  date · Not checked yet · Shared*; *Checked for* a target; sort by *Last changed · Last checked ·
  Name*. **All of it but search sits behind one `Filters` button in the far right corner** (owner,
  same day) — the screen shows search and the list, nothing more. **Filtered to zero is content, not a
  page** — one line and *Clear filters*.

### 2 · Project

- **Name in `sitemap.md`:** `Project` — a place, here in its **viewing** mode.
- **Job:** **MAIN** · **RJ-2** — *"When I put together the pieces a project needs, I want to learn now
  what else has to come with them and where two of them will quietly fight over the same thing, so
  that I do not learn it three days later from an agent behaving strangely."* In the sitemap's words:
  *put the set together and see what it drags in — every row carrying its own state.*
- **Place in the flow:** node `Project`, then the decision *Anything in the set?* — no goes to the empty
  state, yes to `Project: the set`, and from the set, **Check** enters `Run`. Path A, *the set already
  exists*, is three clicks from here to the archive.
- **States:**
  - **Empty ✓** — **Q16**: a project with nothing in it. **One action, and it enters the configuring
    mode**; the control that enters `Run` is **inert** — the product's one named exception to *nothing
    is disabled*. The state names what it offers, not what is dead in it (`flows.md` decision 3).
  - **Error ✓** — the set fails to load. **Q26 governs what the verdict shows** when the product is not
    sure: neither *checked* nor *un-checked* on the strength of a failed read.
  - **Loading ✓** — *opening a project — the set plus every row's state* is a named wait.
  - **Success —** — viewing a set is not an outcome; the outcome lives in `Run`.
- **Inside the filled page:** §7's item states that are readable while viewing — manual, auto-added
  *by X*, conflicting, missing an env key, **detached with the differing fields named** · a finding
  annotating the row that owns it · the verdict with its date, or the stale form.

### 3 · Configuring the set — a mode

- **Name in `sitemap.md`:** `Configuring the set — a mode`, with the `Library panel` as its region
  (Q14, amended 2026-09-20). `flows.md` draws it as `Project: configuring`.
- **Job:** **MAIN** · **RJ-2** — the same line as `Project`; the panel's own purpose in the sitemap is
  *"See what I own that fits here, and put it in"*, **the question the palette could not answer**.
- **Place in the flow:** node `Project: configuring`, entered from the empty project's one action or
  from the set; its decision is *Panel offering anything?*, and the loop *Is the set complete? → no*
  comes back here. **This is where the product's real depth lives: selection, not traversal.**
- **States:**
  - **Empty ✓** — **the panel offers nothing**, in two forms `flows.md` keeps apart: `My library`
    **empty on first run** (§11 guarantees it) and **filtered to zero**. Ways out, both in the flow:
    **switch the scope to `Public library`**, or **the row that creates** — which opens the `Item` add
    form over the Project.
  - **Error ✓** — *the panel cannot load the corpus* · *an add that does not persist* (`flows.md`).
  - **Loading ✓** — *the panel's first fill*, which needs the resolved set before it can order
    `Related` · filtering as you type · and **the wait nobody has noticed**: the dependency walk runs on
    the server, so an add pulls auto-added rows in after a round trip. **How that wait looks is this
    lesson's decision** — rows that appear and then vanish would be EJ-1, and that option is not taken
    silently.
  - **Success —** — an added item is a row in the set and a tick in the panel, not an outcome.
- **Inside the filled page:** scope switch · `kind` tabs with `Related` first and default · rows
  already in the set reading as checked · the `✕` on project rows · **the auto-added row's refusal**,
  the product's only one — *remove what dragged it in* · the detached row's `Edit`, `Reset`, `Promote`
  (Q21), marked but not designed here.

### 4 · Run

- **Name in `sitemap.md`:** `Run` — a mode of the Project, entered by **Check**, ending in **Export**.
  `flows.md` draws it in three nodes: `Run: findings`, `Run: handover`, `Export`.
- **Job:** **MAIN** · **RJ-2** · **RJ-1** · **RJ-4** · **SJ-1** — the sitemap's line: *"Find out
  whether it holds together, see what the other side still needs, and get the archive out."* RJ-1 is
  the handover stages: *"I want to know in advance what that side will still have to have, so that
  they do not find out by watching things quietly fail."*
- **Place in the flow:** from *Is the set complete? → yes* through `Checking`, *Any Problems?*,
  *Fixable from this row?* (yes goes back to the Project), the unclean-export confirmation, the
  handover, *Right agent target?* (no voids the verdict and re-checks), to `Export` and **Archive in
  hand**. It is the end of the part of the main job the product owns — **checked, never works**.
- **States:**
  - **Empty —** — Q16 makes `Run` unreachable from an empty set, so there is no empty `Run`.
  - **Error ✓** — the check cannot complete · **Q28: a generated disclosure that could not be produced
    says so** — `SETUP.md` preview, `.env.example`, the archive tree — rather than rendering short ·
    **an export that fails to build**, the most expensive failure in the flow because the person has
    already read the handover. **Problems are not this state**: a set with Problems is a successful
    check with findings, and it still exports.
  - **Loading ✓** — **the check running**, which §6 makes *a designed moment, not a spinner*: the stage
    stack mid-sweep, stages resolving one by one. And *building the archive* at Export, a second,
    ordinary wait.
  - **Success ✓** — **the archive is built and in hand.** The only *it worked* in the main flow. Its
    words are held to §6: the set **was checked** and the archive **was produced**; what the receiving
    machine still needs is named, and nothing says *works*.
- **Inside the base page (stages resolved, before Export):** each stage with its verdict, duration and
  expansion · the three severities, `Skipped` with its own neutral glyph · **the unclean-export
  confirmation as a row under the finding, never a modal** · the handover stages before Export — the
  `SETUP.md` preview, pinned `ref`s, target paths, `.env.example` · the agent target selector ·
  **a verdict voided by a target change**.

---

## The whole map — every screen in `sitemap.md`

> **Added 2026-09-26, as structure only.** The main flow above is drawn first; everything here is the
> order for step 8. **No page below exists yet**, and the viewer's tree lists them all so the gaps are
> visible rather than forgotten. Same rules: a name from `sitemap.md`, a job or a stated reason for
> having none, a place in `flows.md`, and a state only where a flow produces it.

**Grouped by the sitemap's situations** (0 the door · 1 what I keep · 2 what I assemble · 3 what
leaves · 4 what somebody else opens). **The Library is shown as two screens** because Q29 made its two
scopes two global entries — they are still **one screen with two addresses**, so they share every rule.

| # | Screen | Kind | `<name>` | Empty | Error | Loading | Success |
|---|---|---|---|:-:|:-:|:-:|:-:|
| 0 | **Sign in** | place | `sign-in` | — | ✓ | ✓ | — |
| 1 | **Library · My library** | place | `library-my` | ✓ | ✓ | ✓ | — |
| 1 | **Library · Public library** | place | `library-public` | — | ✓ | ✓ | — |
| 1 | **Item — add / edit** | overlay | `item` | ✓ | ✓ | ✓ | — |
| 1 | **Library import / export** | commands | `library-json` | — | ✓ | ✓ | ✓ |
| 2 | **Projects** | place | `projects` | ✓ | ✓ | ✓ | — |
| 2 | **Project** | place | `project` | ✓ | ✓ | ✓ | — |
| 2 | **Configuring the set** | mode | `project-configuring` | ✓ | ✓ | ✓ | — |
| 2 | **Detached row — edit · reset · promote** | mode of a row | `project-detached` | — | ✓ | ✓ | — |
| 3 | **Run** — from a Project | mode | `run` | — | ✓ | ✓ | ✓ |
| 3 | **Run — one item**, from a Library row | mode | `run-item` | — | ✓ | ✓ | ✓ |
| 3 | **Run — on a shared project**, by the receiver | mode | `run-shared` | — | ✓ | ✓ | ✓ |
| 4 | **Shared project** | place | `shared-project` | — | ✓ | ✓ | — |
| 4 | **Shared item** | place | `shared-item` | — | ✓ | ✓ | — |

**Fourteen screens and 51 pages** — every state marked `✓` plus a `default` for each. *The course's
advice is 20–30 pages to learn the method*; the main flow is 16 of these, and **which of the rest get
drawn is decided at step 8, not by this table.**

### What each one is for, and why its states are the ones marked

**Sign in** — `[no job]`, and no job could (§9, Q25). *The door the online decision put in front of the
owner's work.* **Flow:** before every path, never on the receiver's. **Error** — the way in fails ·
**loading** — signing in · **no success screen**: you are handed on to **where you were** (Q25) · no
empty — a form is never empty of anything.

**Library · My library** — **H-J1** *lay hands on the thing I know I wrote* · **RJ-3** *fix something
once and have the fix reach every copy*. **Flow:** RJ-3, the single-item export, and *Anything in My
library yet?* in the main job. **Empty ✓** — **first run, guaranteed by §11**; since Q29 its way out is
the `Public library` entry, not a switch · **error** — the corpus fails to load · **loading** — the list
and its usage facts, which are computed · **no success** — a list is not an outcome. *Filtered to zero
is content, and carries the row that creates.*

**Library · Public library** — **H-J4** `[?]` · **RJ-3** through *copy it into mine*. **Flow:** the
single-item export's *Is it on the shelf?*, the panel's scope switch. **No empty** — the shelf ships
with the product (§11) · **error**, **loading** as above · **no success** — *copy into My library*
lands as a row that reads as copied. **Designed only as far as the example project needs** (Q19); Q9 —
what it holds and how it sorts — is still open.

**Item — add / edit** — **RJ-3** · **EJ-3** partly. An **overlay**, summoned from the Library row, the
Library's *add*, and the panel's zero result (§8). **Flow:** RJ-3 and RJ-4. **Empty ✓** — *add*: no
item yet, the blank form, and **the keys warning before the material is accepted** (§11) · **default**
— *edit*: **the blast radius at the head of the form**, *used in 3 projects · saving un-checks all
three* · **error** — **Q26: the edit did not land**, and those projects read neither checked nor
un-checked · **loading** — the usage facts at the head of the form, and the save · **no success** — you
return to the row you came from.

**Library import / export** — `[§10]`, no job; kept so the user can leave with their work (Q18). **Two
commands on the Library, not a screen** — drawn because the import carries the §11 keys warning and a
state nobody else has. **Flow:** RJ-4. **Loading** — *potentially the longest wait in the product* ·
**error** — **Q27: the library reads as it did before it started** · **success ✓** — the import finished,
or the file is in hand: a real outcome · no empty.

**Projects**, **Project**, **Configuring the set**, **Run** — the main flow, above.

**Detached row — edit · reset · promote** — **H-J3** *change it here only, without the others getting
it*. A **mode of the row, inside configuring** (Q21). **Flow:** RJ-3's *a detached row kept
deliberately*. **Default** — the override with **the differing fields named**, and Reset beside Detach
(§7) · **error** — the override or the promotion did not land · **loading** — saving it · **no
success** — *promote* re-links the row, which is the row's new state, not a screen.

**Run — one item** — the **main job at its smallest scale** (Q15), from a Library row. **Flow:** *The
single-item export*. The same stages as `Run`, **most of them `Skipped`**, and **nothing stored** — no
project to hold a verdict. **Error**, **loading**, **success ✓** — the same as `Run` · **no empty** — a
row always holds an item.

**Run — on a shared project** — the **receiver's** Check: **MAIN** · **RJ-1** · **RJ-2** · **SJ-1**, by
**P2**. **Flow:** *The receiver*. Same stages, **no global navigation, nothing stored, anonymous**.
**Error** — *the check fails on somebody else's set, and they cannot tell whether that is the set's
fault or ours* · **loading** — the check they run themselves · **success ✓** — the archive taken.
**Q20 applies: invent nothing not derived from P1; show more, promise less.**

**Shared project** — **MAIN** · **RJ-1** · **RJ-2** · **SJ-1**, **P2**'s only surface and the one
carrying **seven jobs**. **Flow:** *The receiver*. **Default** — what the set is, what each item needs,
**when the owner last checked and whether it changed since** (§6), origins and licences, **Check**, and a
way to take it · **error** — **the dead link**, revoked or deleted: *the only place in the product where
somebody is left with nothing at all* · **loading** — **opening the page**, their first impression of
the product · **no empty** — no flow produces one, and **Q20 forbids inventing it** · no success —
taking the archive happens in `Run`.

**Shared item** — **MAIN** · **H-J4** `[?]`. **Flow:** *The receiver*, at one block. **Default** —
what it is, **whose it is** (origin, pinned `ref`, **licence**), what it needs, and a way to take it ·
**error** — the dead link · **loading** — opening it · no empty, no success, for the same reasons.

**Two things on the map that are not in this table, on purpose.** **The library panel** is a region of
*Configuring the set* and is drawn inside it. **Sharing and revoking** are a state of the thing shared,
disclosed where it changes (§5) — they appear on the Project and the Item, not as screens.
