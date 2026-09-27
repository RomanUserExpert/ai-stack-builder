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
| `main-problem-fixed` | 8 yes · 9 yes → Configure, `✕`, **Save**, check again | 12 | Done |
| `main-problem-exported` | 8 yes · 9 no → **Export with 1 problem** | 7 | **Cost** — it ships with the collision |
| `main-target-changed` | 10 no → target to *Cursor*, verdict void, check again | 9 | Done, for Cursor |
| `main-new-project` | 1 no · 3 no · 4 yes — path B, from My library | 13 | Done |
| `main-no-projects` | 2 no → **Create project** → as `main-new-project` | 13 | Done |
| `main-first-run` | 2 yes (only the example) · 5 no · 6 yes — from the shelf | 14 | Done |
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

### Pages the prototypes drew that `pages/` does not have

Each is drawn in the wireframes' own markup and is **`new` until the owner keeps it** — then it moves
into `pages/` (`_conventions.md` §1).

| New page | Where | What it settles |
|---|---|---|
| **Run — building the archive** | every case's Export | The second wait in `Run`, named in `_screens.md` and never drawn |
| **Configuring — the add's round trip** | `new-project`, `first-run`, `set-incomplete`, `create-item` | The row appears at once, *Adding — finding what it requires…*; what it pulls in arrives after — **decided 2026-09-26 and not drawn until now** |
| **Configuring — a draft with a change** | `problem-fixed`, `error-save` | The head's counts follow the draft; the check line says *out of date since `eslint-autofix` was removed* |
| **Configuring — Save didn't land** | `error-save` | **Replaces the stale *an add that did not persist*** (Q33's draft): *Not saved*, the project as it was, the changes still here · **Save again** · **Discard changes** |
| **Configuring — the panel on All, on the shelf** | `new-project`, `first-run` | The sidebar filled from My library, and switched to Public library |
| **Add item over the Project** | `create-item` | The overlay's third door (§8): the Item sheet summoned over configuring, the keys warning first |
| **Projects — only the example** | `first-run` | The first run's Projects |
| **Run — the check didn't finish** | `error-check` | Stages done, the one that stopped, the rest *Not run*; Export says it needs a finished check |
| **Run — for Cursor** | `target-changed` | The verdict voided by a target change is not shown — the run starts again, *Checking again for Cursor* |

**Also caught:** the wireframes' Run names **2 env keys** and writes **3** into `.env.example`
(`SENTRY_AUTH_TOKEN`). The prototypes say 3; **`pages/run-*.html` are not fixed yet.**

### Waits and failures — which state each case leaves by

| Case | Leaves at | The state | Way back |
|---|---|---|---|
| `main-error-projects` | step 01 | `projects-error-server` | **Try again** → Projects, loading |
| `main-error-project` | step 02 | `project-error` | **Try again** → Project, loading |
| `main-error-save` | Configuring, **Save** | *Not saved* — new | **Save again** |
| `main-error-check` | Run, stage 4 | *The check didn't finish* — new | **Check again** |
| `main-error-export` | Run, Export | `run-error` — *the archive didn't build* | **Build the archive again** |

---

## The other flows — later, in this order

**RJ-2** (a and b) · **RJ-1** · **the single-item export** · **the receiver** · **RJ-3** · **RJ-4** —
each written down here as its forks and cases before any of it is built, the way `main` is above.
