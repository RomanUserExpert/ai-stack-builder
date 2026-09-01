# Patterns — stage 5

Written 2026-09-01. **Five shapes for the key flow, scored, one chosen.**

The key flow, named precisely: **assemble a set → check it → export**. Library to archive. Not "the
app" — the spine that carries the wow moment and both supporting moments (CLAUDE.md §2).

**Boundary, and it holds for every line below.** These are **flow structures, not screens**. Prose
and plain-text diagrams: boxes, order, what is on screen at each step. No visual design, no layout
grid, no colour, no type scale, no components. The design system is the next phase and this stage
must not quietly become it.

---

## How the scoring works here, and how it differs from stage 4

Stage 4 scored **products that exist**: *did this interface tell me the thing?* Nothing here exists,
so the question changes to the one a structure can actually answer:

> **Does this shape give the category a natural home — a place the right behaviour fits without
> being bolted on?**

Same five categories, same 1–5 anchors, re-read as structure:

| | | Read here as |
|---|---|---|
| **C1** | State legibility | Can the shape show the current set and its derived state without an extra surface? |
| **C2** | Consequence disclosure | Is there an obvious place for the cost of an irreversible step, before it? |
| **C3** | Failure copy | Is there room for *item + rule + observed value* where the finding belongs? |
| **C4** | Recovery | Does the remedy have somewhere to sit next to the problem? |
| **C5** | Economy | Is anything permanently on screen that cannot act in the current step? |

A score of 4 or 5 means the behaviour falls out of the shape. A 2 means you would have to invent a
surface to get it. **Nothing is scored on how pretty it would be.**

## The five questions every variant answers, in the same words

Set by the plan, so the variants can be compared rather than admired.

1. Where does the **cold start** land — empty library, and seeded library?
2. Where does the **validation pass** live — inline and continuous, or triggered and full-screen?
3. Where do the **six item states** render, especially *detached, locally modified*?
4. How does an **unclean export** get confirmed, and where does that confirmation appear?
5. What does it cost at **300 items** rather than 30?

## The constraints that are not up for negotiation

Desktop-first · dark from day one · **not a node canvas** · single user · local only · custom design
system. A variant that scores well and violates one of these loses regardless of its score.

---

# P1 — Two-pane drag

**The idea.** Library on the left, project on the right, items dragged in, validation live as the set
changes. This is the current CLAUDE.md §8 spec.

**Prior art.** Backstage's catalog beside a scaffolder form; Figma's assets panel dragged onto a
canvas.

```
┌─ LIBRARY ────────────────┬─ PROJECT: db-agent ───────────────┐
│ search…                  │ target: Claude Code               │
│ [skill][agent][mcp]…     │                                   │
│                          │  db-migrate      skill    manual  │
│  db-migrate      skill   │  postgres-mcp    mcp      ← pulled│
│  postgres-mcp    mcp     │  env-check       script   manual  │
│  env-check       script  │  db-tools        mcp      manual  │
│  vector-store    mcp     │                                   │
│  … 296 more              │  6 items · 1 problem · 2 notes    │
│                          │                     [Check][Export]│
└──────────────────────────┴───────────────────────────────────┘
```

### The five answers

1. **Cold start.** Its worst moment. Empty library means *both* panes are empty and the primary verb
   — drag — cannot be taught, because there is nothing to drag and nowhere the gesture is implied.
   Seeded, it is fine. The seed is therefore not a nice-to-have here; the shape does not work without
   it.
2. **Validation.** Live in the right pane as a derived strip. The *designed* pass — the animated,
   legible sweep of CLAUDE.md §6 — has nowhere to expand except a modal over both panes, or by taking
   the right pane over and leaving a library list beside a running check.
3. **Six states.** Every item renders **twice**: as a library row on the left and as a member on the
   right. States 3–6 exist only on the right. The card must therefore read in two contexts, and
   *detached* — a per-project fact — is invisible in the pane where you browse.
4. **Unclean export.** A dialog over the two panes. Nothing about the set's cost is visible until you
   press.
5. **300 items.** Filtering solves the finding (Linear-grade, and we have the notes for it). Dragging
   does not: item #250 to a target that may be scrolled out of view is the classic drag-at-scale
   failure. The mitigation is click-to-add — at which point drag is no longer the mechanism and P1
   has quietly become P2 with an extra pane.

### Scores

| C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|
| **4** | **3** | **3** | **4** | **2** |

- **C1 = 4.** Library and set are visible at once, which is a real advantage: *what else do I own that
  fits here?* is answerable without leaving. Not 5 because the same item in two panes means its state
  lives in one of them.
- **C2 = 3.** The confirmation is a dialog bolted onto a layout that has no room for it.
- **C3 = 3.** A finding needs *item + rule + observed value* — `db-tools writes .mcp.json, also
  written by postgres-mcp`. A right-pane strip beside a persistent library truncates exactly that
  sentence.
- **C4 = 4.** The library is right there, so remove/detach/reset sit next to the item.
- **C5 = 2.** Half the screen is inert during the check and during export. This is the benchmark's
  finding 7 applied to our own design: on a primary surface, what cannot act is not shown — and a
  library pane cannot act while a validation pass is running.

**Best at:** browsing and assembling in one breath. **Loses on:** the verb it is named after.

---

# P2 — Command-first

**The idea.** No persistent library pane. `⌘K` adds items by name; the project is a growing list;
checking is another command. The library is a search **index**, not a screen in this flow.

**Prior art.** Linear's palette (one field, three jobs); Tessl's `⌘K`; Raycast's launcher instead of
a screen; and — from the benchmark — Obsidian's switcher, where a query that matches nothing becomes
the row that creates it.

```
  db-agent                                    target: Claude Code
  ────────────────────────────────────────────────────────────────
   db-migrate        skill    manual
   postgres-mcp      mcp      required by db-migrate
   env-check         script   manual
   db-tools          mcp      manual        ✕ writes .mcp.json (2)
   web-search        agent    detached · content, targetPath differ
  ────────────────────────────────────────────────────────────────
   6 items · 1 problem · 2 notes
   [ ⌘K add ]                              [ Check ]  [ Export ]

  ⌘K ─────────────────────────────────────────────────────────────
   > postgres
     postgres-mcp          mcp     used in 3 projects
     pg-backup             script  requires postgres-mcp
     ─────────────────────────────
     No item named "postgres-vector" — create one            ⇧↵
```

### The five answers

1. **Cold start.** The best of the five, and it comes free. An empty library means the palette
   returns nothing — and the empty palette **is** the create path, which is Obsidian's finding used
   deliberately rather than copied blind: we keep the offer *and* say that nothing matched, which is
   the split the benchmark told us Obsidian gets wrong. The first item is created by the same control
   that will later add the thousandth.
2. **Validation.** Triggered. Each row annotates itself with its own finding — the VS Code Problems
   shape, one row, `item · rule · observed value` — and the full designed pass is a separate surface
   (see the choice below).
3. **Six states.** One rendering, not two. Every state is a property of the row: manual, pulled in by
   name, conflicting, missing env, **detached with the differing fields named**. There is no second
   context in which the same item must read differently.
4. **Unclean export.** `Export` is a command like any other, and its confirmation names the
   consequence in the present tense over the list that produced it.
5. **300 items.** The only variant that gets **better** as the library grows, because a palette is
   indifferent to list length and a pane is not.

### Scores

| C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|
| **3** | **4** | **5** | **4** | **5** |

- **C1 = 3, and this is the real cost.** The set is perfectly legible; the library is not visible at
  all. *What else do I own that would fit?* has no answer on screen. The mitigation — a palette that
  opens cold on **related** items, the ones that `require` or are required by what is already in the
  set — is better than a static pane, but it is a mitigation, and it only works once the set is
  non-empty.
- **C2 = 4.** A command's confirmation is a natural object. Not 5 because nothing about the archive is
  disclosed until the command is invoked.
- **C3 = 5.** A full-width row per item is exactly the room *item + rule + observed value* needs, and
  the benchmark's best failure lines (`ERESOLVE`, Terraform's `Reference to undeclared resource`) are
  one-line-per-finding shapes.
- **C4 = 4.** Remedies sit on the row: remove, detach, reset, promote to library.
- **C5 = 5.** Nothing is permanently on screen but the set. The palette exists only while invoked —
  the affordance appears when it can act.

**Best at:** scale, economy, and the cold start nobody else solves. **Loses on:** discovery — it
cannot show you what you have.

---

# P3 — Document

**The idea.** The project **is** an editable manifest. The UI is an assistant over the text;
validation is inline diagnostics, like a linter.

**Prior art.** Continue's `config.yaml` with `uses`/`with`/`override`; Terraform HCL; VS Code's
Problems panel over a file.

```
  project: db-agent
  target: claude-code

  items:
    - db-migrate                  ⚠ requires postgres-mcp — not in this project
    - env-check
    - db-tools                    ✕ writes .mcp.json — also written by postgres-mcp
    - web-search:
        detached: true
        overrides:
          content: …              ← the diff is the text
          targetPath: .claude/agents/search.md

  PROBLEMS  2 problems · 2 notes
   ✕ db-tools and postgres-mcp both write .mcp.json          [line 6]
   ⚠ ANTHROPIC_API_KEY declared by env-check, no value       [line 4]
```

### The five answers

1. **Cold start.** The worst of the five. A blank document is the least teachable empty state there
   is, and the fix — a commented template — is the thing every config tool ships and every user
   deletes.
2. **Validation.** The best fit of any variant: diagnostics in a gutter, a Problems list under the
   text, and both addressed by line. This is the benchmark's highest-scoring B3 shape almost
   verbatim.
3. **Six states.** Also strong, and for an unexpected reason: a detached item's `overrides` **are**
   text, so *naming the fields that differ* — the thing Figma computes and refuses to draw — falls
   out for free.
4. **Unclean export.** The strongest possible: `terraform apply`, printed. A plan above a typed
   confirmation, which the benchmark scored 5 on C2.
5. **300 items.** A manifest is unbrowsable. Finding an item to add means a palette — P2, embedded —
   and the document has bought nothing at that moment.

### Scores

| C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|
| **4** | **5** | **5** | **3** | **4** |

- **C1 = 4.** Exact and complete, and requires reading rather than scanning.
- **C2 = 5.** Nothing else in this document approaches it.
- **C3 = 5.** Line numbers, rule codes, a Problems list — the shape our validator wants.
- **C4 = 3.** The remedy is *edit the text*. Offering an actual remedy means building quick-fixes,
  which is a compiler feature, not a layout.
- **C5 = 4.** Text is economical by nature; the assistant panel is the only thing that can go idle.

**Where it dies, and it is not on the scores.** Two things kill P3. The post-mortem
([`1-landscape/continue-postmortem.md`](../1-landscape/continue-postmortem.md)) established that the composition layer is the
half of Continue that died, and stage 3 found **nobody asking for one**. And CLAUDE.md §3 puts the
craft bar at Linear and Raycast with a custom design system as part of the product's value — a
product whose main surface is a text editor makes that value invisible. P3 is the right answer to a
question our audience is not asking.

---

# P4 — Staged wizard

**The idea.** Target first, then one step per kind, then resolution, then review, then export.
Linear, finite, no free-form assembly.

**Prior art.** Backstage's scaffolder template form; GitHub's fork form.

```
  ① Target   ② Skills   ③ Agents   ④ MCP   ⑤ Scripts   ⑥ Resolve   ⑦ Review   ⑧ Export
  ─────────────────────────────────────────────────────────────────────────────────────
                                    step ④ of ⑧
   pick the MCP servers this project needs
     ☑ postgres-mcp        (pulled in by db-migrate at step ②)
     ☐ vector-store
     ☑ db-tools
                                                          [ Back ]  [ Next ]
```

### The five answers

1. **Cold start.** Its best moment, and the only category it wins. The wizard **is** the onboarding:
   it teaches the model by walking you through it, one kind at a time, and an empty library turns each
   step into a create prompt rather than a dead list.
2. **Validation.** Has a dedicated step, which is clean — and arrives too late to change anything you
   did four steps ago without walking back.
3. **Six states.** Badly. Items are split across steps by kind, so a dependency pulled in at step ②
   surfaces at step ④ with no way to see why except a parenthetical. *Detached* has no step of its
   own and therefore no home.
4. **Unclean export.** A final step, which is the right place. This part works.
5. **300 items.** Each step is a filtered list, so scale is fine.

### Scores

| C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|
| **3** | **4** | **4** | **2** | **2** |

- **C4 = 2.** Going back means re-walking. And the second supporting moment in CLAUDE.md §2 is
  **duplicating a project to re-tune it for a new context** — which in a wizard means eight steps to
  change one item. The shape is hostile to the exact motion the product promises.
- **C5 = 2.** Steps you have not reached and steps you will skip are on screen the whole time.

**Rejected on:** repeat use. A wizard optimises the first run at the cost of every run after it, and
this is a tool people open weekly.

---

# P5 — Run-centric

**The idea.** Assembly is small and secondary. Pressing **Check** turns the whole surface into the
stage list with verdicts and durations, and **Export is its final stage** — not a button beside it.

**Prior art.** Vercel's deployment page (the benchmark's C1 = 5 for B3); a GitHub Actions run and its
four verdict glyphs; Terraform's summary line.

```
  db-agent                                             target: Claude Code
  ────────────────────────────────────────────────────────────────────────
  ▸ Resolve dependencies        6 items          ✓        120 ms
  ▸ Cycles                      1 note           ✓         40 ms
      db-tools and pg-backup always travel together
  ▾ Conflicts                   1 problem        ✕         80 ms
      db-tools conflicts with legacy-pg — both declared by you
  ▸ Command names               nothing to check  ○
  ▾ Target paths                1 problem        ✕         60 ms
      db-tools and postgres-mcp both write .mcp.json
      the archive will contain one of them — db-tools
  ▸ Environment                 2 notes          ⚠         30 ms
  ────────────────────────────────────────────────────────────────────────
  ▸ Export                      ready                        [ Export ]
```

### The five answers

1. **Cold start.** Strong *if* seeded: the product opens on a validation pass that already ran, which
   is the Linear finding at full strength — the wow moment happens before the user has typed anything.
   Empty, there is nothing to check and the screen is a list of skipped stages.
2. **Validation.** It *is* the product. Triggered, full-surface, stages with their own verdicts and
   durations, expandable. This is the designed moment with a whole screen to be designed in.
3. **Six states.** Its weakness, and a disqualifying one on its own. A stage list is about **checks**,
   not items. *Detached, locally modified* is a property of an item and has no home here at all.
4. **Unclean export.** The best of the five. Export as the **final stage** means the confirmation is
   not a dialog interrupting a flow — it is the next row in a list the user is already reading, and
   the consequence sentence sits where the finding that caused it already sits.
5. **300 items.** Irrelevant to this screen, which is exactly the problem: assembly is "small and
   secondary" and therefore unspecified. P5 needs another variant to do a third of the flow.

### Scores

| C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|
| **5** | **5** | **5** | **4** | **5** |

Straight fives on four categories, and it still cannot be the answer on its own, because **it does
not assemble anything**. The scores are honest and the coverage is not: P5 is a superb answer to the
second and third thirds of the spine.

---

# The comparison

| | P1 two-pane | P2 command | P3 document | P4 wizard | P5 run |
|---|---|---|---|---|---|
| C1 state legibility | 4 | 3 | 4 | 3 | **5** |
| C2 consequence | 3 | 4 | **5** | 4 | **5** |
| C3 failure copy | 3 | **5** | **5** | 4 | **5** |
| C4 recovery | 4 | 4 | 3 | 2 | 4 |
| C5 economy | 2 | **5** | 4 | 2 | **5** |
| **Covers assemble** | ● | ● | ● | ● | ○ |
| **Covers check** | ◐ | ◐ | ● | ● | ● |
| **Covers export** | ◐ | ◐ | ● | ● | ● |
| Fixed constraints | ok | ok | **craft bar** | ok | ok |

---

# The choice

> **Provisional, deliberately.** The shape below is what the rubric chooses. It is **not final until
> the open-question register is worked through** — Q1, Q2 and Q4 all land inside this flow, and Q2 in
> particular may add a surface that none of the five variants has. Read the finalisation section of
> [`4-benchmark/benchmark.md`](../4-benchmark/benchmark.md) before treating any of this as settled: the rubric grades craft, not
> weight, and the five variants differ most in the third of the flow where the pain evidence is
> thinnest.

**A hybrid, and it is stated as a choice rather than a failure to choose — as the plan required.**

> **P2 wins the spine. P5 becomes the check-and-export surface. P3 donates one mechanism.**

Neither half is a compromise: the two variants win different thirds of the same flow, cleanly, and
their scores say so. P2 takes 5 on economy and failure copy and owns the cold start; P5 takes 5 on
four categories and owns the moment the product exists for. The seam between them is a single
control — **Check** — which is the natural boundary anyway.

## The spine, end to end

**Three surfaces. Not four, and not one.**

```
  LIBRARY                    PROJECT                     RUN
  browse, edit, add          the set, as a list          stages, verdicts, export
  usage facts per item       ⌘K adds · rows carry        Export is the final stage
  not part of the builder    every item state
        │                          │                           │
        └──── ⌘K reaches it ───────┤                           │
                                   └───────── Check ───────────┘
                                   ←──────── back to fix ──────┘
```

1. **Library** stays a screen — browse, filter, add, edit, and the per-item usage facts of CLAUDE.md
   §5. It is where you keep things. **It is not part of the builder flow**, which is the substantive
   change from the current §8.
2. **Project** is a list, not a canvas and not a pane pair. `⌘K` adds by name; every row carries its
   own state, including *detached* with the differing fields named; findings annotate the row that
   owns them.
3. **Run** is entered by **Check** and is the whole surface: stages with verdicts, durations and
   expansion, ending in **Export as the final stage**. An unclean export is confirmed there, in the
   row below the finding that caused it.

## What each rejected variant donates, and what dies with it

- **P1 → the thing worth keeping is the question it answers**: *what else do I own that fits?* P2
  must answer it inside the palette — opening cold on **related items**, the ones that require or are
  required by what is already in the set. **What dies: drag as the mechanism.** It does not survive
  300 items, and every mitigation turns P1 into P2 with an idle pane.
- **P3 → one mechanism, and it is precise**: a detached item names the fields that differ, because
  `overrides` is already a keyed object. Figma computes this and refuses to draw it (flow 05); we
  draw it. **What dies: the manifest as the main surface** — no evidence anyone wants a composition
  layer, and it makes our design system invisible.
- **P4 → the observation that a first run wants to be linear.** That belongs in the seeded library and
  the empty states, not in the builder. **What dies: the wizard**, on the second use and every use
  after.
- **P5 → almost everything, and it is not rejected so much as promoted** to the surface it was always
  best at. Nothing dies.

## What this costs us, said plainly

The hybrid's weakest point is **P2's C1 = 3**: with no library pane, you cannot see what you are not
using. Three things carry that weight, and if all three fail, this choice was wrong:

1. the palette opening cold on **related** items rather than on an alphabetical index,
2. the Library screen being one keystroke away and remembering where you were,
3. per-item usage facts (*used in 3 projects*, *2 items require this*) doing the work a visible pane
   would otherwise do.

---

# What this stage found for the open register

Recorded as **evidence, not answers** — the register is worked through in one sitting once stage 5 is
in, per the protocol in [`research-plan.md`](../research-plan.md).

- **Q1 — cold start.** Every one of the five needs a seeded library to be demonstrable, and three of
  them (P1, P3, P5) are actively broken without one. P2 is the only shape where the empty case has a
  native answer, and even there the *validation pass* has nothing to run on until items exist. This is
  as close to a settled question as evidence can get: **seeding is a product decision, not a demo
  problem.**
- **Q3 — can a project contain a project?** **No variant needed it.** Five shapes, none of which
  required composition to work, and the post-mortem plus stage 3 both point the same way.
- **Q4 — promoting a detached item back into the library.** In the chosen shape it has an obvious
  home: a command on the row, next to detach and reset. That is a place, not yet a decision — the
  semantics (new item, or update the original?) remain open.
- **Q2 — how much weight `SETUP.md` carries.** Stage 4 found B4 to be the industry's weakest flow
  (`benchmark.md`, finding 8). P5's export-as-final-stage gives the answer somewhere to live: what
  the archive contains, and what the receiving machine must still do, as the last two rows of the run.

---

# What changes in CLAUDE.md

§8 currently describes P1: *"a filtered sidebar of the library on the left; items are dragged into
the project area"*. That is replaced by the three surfaces above. The four rejected variants stay
here, with the reason each lost.
