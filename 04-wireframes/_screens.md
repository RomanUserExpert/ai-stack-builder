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

## Not taken, and why

Each of these is on the map; none is on the main path, so it waits for step 8.

| Screen | Why not now |
|---|---|
| **Item** — add/edit overlay | In the main flow only as a **side branch** — the panel's zero result. Its jobs are RJ-3 and EJ-3, not the main job. Step 8 |
| **Library** | **Left the assembly path** with Q14: *during building a project we will not open the library.* Its jobs are H-J1 and RJ-3. Step 8 |
| **Sign in** | **No job**, and no job could (§9). It is the door before the flow, not a step of it |
| **Library import / export** | No job — kept on a non-evidential basis (Q18). Two commands, not a screen |
| **Detached row** — edit · reset · promote | H-J3; not a node in the main flow. Its commands are marked on the configuring page and designed later |
| **Shared project** · **Shared item** | The **receiver's** flow, P2's surfaces — not the primary persona's path. Step 8, under Q20's conservative rule |
| **Run from a Library row** — single-item export | Its own flow in `flows.md` (Q15). Step 8 |
