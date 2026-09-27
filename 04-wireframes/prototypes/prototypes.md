# Clickable prototypes — lesson 04

> **Written 2026-09-27, out of [`flows.md`](../../03-information-architecture/flows.md),
> [`_screens.md`](../_screens.md) and the wireframes in [`pages/`](../pages/) and nothing else.** A
> prototype is **a flow walked on the wireframes**: the same pages, wired by `href` so that one path
> through one flow can be clicked from its first screen to its ending. **No screen is invented here** —
> where a case needs a page the wireframes do not have, this file says so and the page is drawn in
> `pages/` first. The rules are in [`_conventions.md`](_conventions.md).

**Naming: `<flow>-<case>`.** A flow is one diagram in `flows.md`; a case is **one path through its
forks** — one answer to every decision on the way. Each case is a folder here, holding its steps.

**Order of work** (owner, 2026-09-27): the main job first, every fork of it written down as a case
below; **`main-success` built first**, reviewed, then **the other thirteen the same day**.

---

## Flow `main` — the main job

> *When something I have already got working has to live somewhere else — a second tool, a new
> machine, a container, a colleague's laptop — I want it to keep working there without me
> rediscovering everything it quietly depended on.* — `jtbd.md` §1

**P1, the keeper — primary (Q7).** Signed in, as every owner path is (`sitemap.md` §Navigation counts
depth *for somebody already signed in*). The diagram is `flows.md` §*The main job*: 31 nodes, 12
decisions. **Every case below is one answer to each decision it passes**, and together they reach
every node of the diagram at least once.

### The forks, and which case takes each branch

| # | Decision in `flows.md` | Yes → | No → |
|---|---|---|---|
| 1 | **A project for this work?** | `main-success` | `main-new-project`, `main-first-run`, `main-no-projects` |
| 2 | **Any projects at all?** | `main-first-run` (only the example) · `main-new-project` | `main-no-projects` |
| 3 | **Anything in the set?** | `main-success` | `main-new-project` — the empty project |
| 4 | **Panel offering anything?** | `main-new-project` | `main-first-run`, `main-create-item` |
| 5 | **Anything in My library yet?** | `main-create-item` (filtered to zero) | `main-first-run` (empty on first run) |
| 6 | **Switch the scope to the shelf?** | `main-first-run` | `main-create-item` — the row that creates |
| 7 | **Is the set complete?** | every case, at *Save* | `main-set-incomplete` |
| 8 | **Any Problems?** | `main-problem-fixed`, `main-problem-exported` | `main-success` |
| 9 | **Fixable from this row?** | `main-problem-fixed` | `main-problem-exported` |
| 10 | **Right agent target?** | `main-success` | `main-target-changed` |
| 11 | **Env values on that machine?** | — | — |

**Decision 11 is not prototyped, on purpose.** It is the product's ceiling — *checked, never works* —
and it happens on a machine we never touch. Every case that reaches **Archive in hand** stops there,
and the success page names the keys the other side still has to supply.

### The cases — all fourteen built (2026-09-27)

**Every case runs from step 01 to its ending, and the build checks it**: each page leads to the next by
**exactly one** live link or one self-advancing wait, and the last leads nowhere. The steps are listed
in the viewer; below is what each case proves and which of its pages are **new** — not in `pages/`.

| Case | Path through the forks | Steps | Ending |
|---|---|---|---|
| `main-success` | 1 yes · 3 yes · 8 no · 10 yes | 7 | Done — archive in hand |
| `main-problem-fixed` | 8 yes · 9 yes → **Remove** in Run, confirmed → the check runs again (Q34) | 10 | Done |
| `main-problem-exported` | 8 yes · 9 no → **Export with 1 problem** | 7 | **Cost** — it ships with the collision |
| `main-target-changed` | 10 no → target to *Cursor*, verdict void, check again | 9 | Done, for Cursor |
| `main-new-project` | 1 no · 3 no · 4 yes — path B; the new project opens with the panel open (Q34) | 12 | Done |
| `main-no-projects` | 2 no → **Delete example**, confirmed → **Create project** → as `main-new-project` | 14 | Done |
| `main-first-run` | 2 yes (only the example) · 5 no · 6 yes — from the shelf | 13 | Done |
| `main-set-incomplete` | 7 no → Configure, add from the panel, **Save** | 11 | Done |
| `main-create-item` | 5 yes (filtered to zero) · 6 no → the row that creates | 13 | Done |
| `main-error-projects` | Projects didn't load → **Try again** | 9 | Done |
| `main-error-project` | the project didn't load (Q26) → **Try again** | 9 | Done |
| `main-error-save` | **Save** didn't land → **Save again** | 11 | Done |
| `main-error-check` | the check didn't finish → **Check again** | 9 | Done |
| `main-error-export` | the archive didn't build → **Build the archive again** | 9 | Done |

**Every failure case comes back to the success path by the state's own way out** and finishes there,
so each case is whole on its own — a reviewer never has to switch cases to see an ending.

### The data each case stands on

- **`acme-billing-api` in four versions.** *As drawn* — 14 items, the `eslint-autofix` ↔ `code-style`
  conflict, 1 problem (`problem-fixed`, `problem-exported`, `error-save`). **Clean** — the same project
  one decision later, `eslint-autofix` removed, 13 items, 0 problems (`success`, `target-changed`, the
  error cases). **+ `query-explainer`** (`set-incomplete`) and **+ `stripe-rules`** (`create-item`) —
  14 items, still clean.
- **`stripe-webhooks` from My library** (`new-project`, `no-projects`) — the name the empty project
  already carries. Tick `migration-reviewer`, which brings `db-migrate` → `seed-data` and
  `postgres-mcp`; then `code-style`. **5 items · 0 problems · 2 notes · 1 skipped.**
- **`stripe-webhooks` from the shelf** (`first-run`) — `webapp-testing`, which brings `playwright-mcp`,
  and `github-mcp-server`. **3 items · 0 problems · 1 note · 2 skipped.**

**Invented for the prototype, and to be confirmed** — none of it is in the wireframes or the specification:

- `query-explainer`'s and `stripe-rules`' descriptions and contents.
- **`webapp-testing` requires `playwright-mcp`** — a `requires` edge on shelf data. §11 wants real edges
  on the shelf; this one is plausible, not checked.
- **The archive under Cursor** — rules as `.mdc` in `.cursor/rules/`, agents among them, `.cursor/mcp.json`.
  §6 fixes only *`.cursor/rules`, MDC, its own MCP config*; where agents land under Cursor is not decided.
- **An item created from the panel's zero result goes into the set as well as into My library.** §8 says
  the row that creates *authors the missing item* and does not say it is added; the person needing it is
  mid-assembly, so the prototype adds it.
- **Archive sizes** are arithmetic, not measurement.

**The owner's first review, 2026-09-27 — Q34.** Remove from Run with a confirmation and the check
re-running by itself (`run-remove.html`, new in `pages/`); a new project opening with the panel open
(`project-empty.html`, redrawn); *Delete example* active and confirmed. The cases above are rebuilt on it.

### Pages the prototypes drew first — all kept into `pages/` (Q35)

**Kept on 2026-09-27**, after the independent critique: every page below now exists in `pages/` under the name its steps carry (`project-configuring-loading-add`, `run-loading-export`, `run-error-check`, `run-error-setup`, `project-configuring-public`, `project-configuring-error-server`, `projects-delete`, `project-share`, `project-revoke`, `project-detached-promote`). **The table is kept as the record of where each one came from.**


Each is drawn in the wireframes' own markup and is **`new` until the owner keeps it** — then it moves
into `pages/` (`_conventions.md` §1).

| New page | Where | What it settles |
|---|---|---|
| **Run — building the archive** | every case's Export | The second wait in `Run`, named in `_screens.md` and never drawn |
| **Configuring — the add's round trip** | `new-project`, `first-run`, `set-incomplete`, `create-item` | The row appears at once, *Adding — finding what it requires…*; what it pulls in arrives after — **decided 2026-09-26 and not drawn until now** |
| **Configuring — a draft with a change** | `error-save` | The head's counts follow the draft; the check line says *out of date since `eslint-autofix` was removed* |
| **Configuring — Save didn't land** | `error-save` | **Replaces the stale *an add that did not persist*** (Q33's draft): *Not saved*, the project as it was, the changes still here · **Save again** · **Discard changes** |
| **Configuring — the panel on All, on the shelf** | `new-project`, `first-run` | The sidebar filled from My library, and switched to Public library |
| **Add item over the Project** | `create-item` | The overlay's third door (§8): the Item sheet summoned over configuring, the keys warning first |
| **Projects — only the example** | `first-run` | The first run's Projects |
| **Run — the check didn't finish** | `error-check` | Stages done, the one that stopped, the rest *Not run*; Export says it needs a finished check |
| **Projects — delete the example** | `no-projects` | The only way to an empty Projects, confirmed (Q34) |
| **Run — for Cursor** | `target-changed` | The verdict voided by a target change is not shown — the run starts again, *Checking again for Cursor* |

**Also caught:** the wireframes' Run names **2 env keys** and writes **3** into `.env.example`
(`SENTRY_AUTH_TOKEN`). The prototypes say 3; **`pages/run-*.html` fixed the same day (Q35).**

### Waits and failures — which state each case leaves by

| Case | Leaves at | The state | Way back |
|---|---|---|---|
| `main-error-projects` | step 01 | `projects-error-server` | **Try again** → Projects, loading |
| `main-error-project` | step 02 | `project-error` | **Try again** → Project, loading |
| `main-error-save` | Configuring, **Save** | *Not saved* — new | **Save again** |
| `main-error-check` | Run, stage 4 | *The check didn't finish* — new | **Check again** |
| `main-error-export` | Run, Export | `run-error` — *the archive didn't build* | **Build the archive again** |

---

## The other flows — built 2026-09-27, lighter than the main job

**Owner: the same logic, conventions and rules, up to five of the most important cases per flow, and
not as detailed.** *Lighter* means one thing: **the steps are the wireframe pages as drawn**, wired
step to step, and **the data is left as each page has it** — a shared Run may be on `agent-dotfiles`
while its shared page is not, a My library row may say *used in 3 projects* after an edit. The main
job adjusts every count to the step; these do not. **Every other rule holds**: one way forward per
step, off-path links inert, waits advance by themselves, controls that are steps wrap themselves in the
link, and **the build walks every case** the same way.

**23 cases in six flows**, chosen where the flow forks or fails, and none repeating a main-job case:

| Flow | Case | Path | Steps | Ending |
|---|---|---|---|---|
| **Single-item export** | `item-success` | My library → Export on `migration-reviewer` → Run → Export | 4 | Done |
| | `item-from-shelf` | nothing in My library → Public library → Export on `playwright-mcp` | 5 | Done |
| | `item-not-found` | nothing in My library, nothing on the shelf | 2 | **Stuck** — cannot find it |
| | `item-error-check` | the check didn't finish → Check again | 6 | Done |
| **RJ-1 · The handover** | `rj1-stale-then-read` | the verdict out of date → Check → **the handover stages open, read before Export** | 5 | Done — the other side is known |
| | `rj1-preview-failed` | `SETUP.md` couldn't be written (Q28) — *missing, not empty* → Write it again | 5 | Done |
| **RJ-2 · Drags in, fights** | `rj2-auto-added-holds` | open `db-migrate` — *pulled in by migration-reviewer* → remove the puller → the three go | 4 | Done |
| | `rj2-requirement-missing` | `seed-data` deleted → *an unresolvable requirement* → Edit `db-migrate` → check again | 7 | Done — nothing will fight |
| **RJ-3 · Fix once** | `rj3-edit-reaches-all` | Edit `db-migrate` — *used in 3 projects* → Save → Projects: all three out of date | 4 | Done |
| | `rj3-save-failed` | the edit didn't land (Q26) → Save again | 4 | Done |
| | `rj3-detached-reset` | `pr-reviewer` detached → **Reset whole item** → Save | 5 | Done — the fix reaches this copy |
| | `rj3-detached-promote` | `pr-reviewer` → **Promote** → a new item, the row re-linked | 4 | Done |
| | `rj3-promote-failed` | Promote didn't land → Promote again | 5 | Done |
| **RJ-4 · No secrets** | `rj4-add-item` | Add item — *check that these files carry no keys* → Add | 3 | Done |
| | `rj4-import` | Import JSON — the same warning → importing → 47 imported | 4 | Done |
| | `rj4-import-failed` | the import didn't finish — *nothing was imported* (Q27) → again | 5 | Done |
| | `rj4-share` | Share → **what becomes visible, before the link exists** → Create link | 3 | Done — the secrets stayed |
| | `rj4-revoke` | Stop sharing → **copies already taken stay taken** | 3 | **Cost** — copies already taken |
| **The receiver** | `receiver-check-take` | a link → Check this set → Download the archive | 4 | Done |
| | `receiver-check-failed` | the check didn't finish — *whose failure it is* → Check again | 6 | Done |
| | `receiver-copy` | Copy into my library → **Sign in, the only door, chosen** → My library | 3 | Done — it is mine now |
| | `receiver-item` | a shared item → Take as an archive | 4 | Done |
| | `receiver-dead-link` | the link no longer opens | 1 | **Stuck** — nothing to fall back on |

**Drawn here first — kept into `pages/` the same day (Q35)** except the three that are content, not pages (a shared project, an auto-added item open, the unresolvable requirement):

- **The share disclosure** (`rj4-share`) — §6's disclosure moment, never drawn: what becomes visible,
  the env key **names**, the external repos, and the tangled-content Note.
- **Stop sharing** (`rj4-revoke`) — *the link stops working at once; it can't reach what was taken.*
- **Promote to My library…** (`rj3-detached-promote`) — the dialog the ellipsis promised: a name for the
  new item, and *the original stays as it is*.
- **A shared project** — the Project with a *Shared* tag, the *anyone holding it* line, *Stop sharing*.
- **An auto-added item in the side panel** (`rj2-auto-added-holds`) — *pulled in by migration-reviewer;
  it has no remove of its own.*
- **The unresolvable requirement** (`rj2-requirement-missing`) — the Problem a deleted item leaves (Q17),
  on stage 01, with *Edit db-migrate*.
- **`SETUP.md` couldn't be written** (`rj1-preview-failed`) — Q28 on the page: *missing, not empty*.

**Not built, on purpose:** RJ-1's *exported unread* is the success path without opening a stage — nothing
to click differently; RJ-2's collision shipped is `main-problem-exported`; the cycle reported as
information has no data in the wireframes to stand on.
