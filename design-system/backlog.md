# Backlog

What a screen needed and the system could not take yet: a component, a state, a token. It is written down here, not
drawn on the screen (`CLAUDE.md` §18, *Contributing to the system*). **A gap is an order for the system, not an exception
for the screen.** Each entry enters the system by §18's table, or goes to the register first when it is a product
decision rather than a missing part.

## From the test of a new screen — lesson 09, step 6 (2026-11-03)

The screen: [`examples/usage.html`](examples/usage.html), *Usage of My library*, for EJ-3. It is built from the system
alone: two patterns (Browse head, Confirmation) and ten components (App header, Page head, Tag, Search field,
Filters button, Small heading, Row list, Button, Dialog, Form actions), 0 lines of style, 0 classes of its own, in dark and in
light. **What it lacked, four entries:**

| # | Kind | What was missing | Where it showed | What was done on the screen | Enters by |
|---|---|---|---|---|---|
| **B1** | state | **A link inside a meta line has no rest state.** At rest it has the line's colour and no underline (measured: `rgb(197,199,190)` on both, `text-decoration: none`). Only hover shows it is a link. | The usage line names the project (*Used in acme-billing-api*), because §5 says the count expands to name the projects. | Drawn as a link with the system's look, so it reads as text until hovered. | A rest state for `a` inside `.meta`, through a role, in both themes: `components/row.css` (or `base.css`) and the Row list's docs page and States block |
| **B2** | component | **A disclosure: a group that folds.** The system has two expansions, each with one job: the Check stage's (Run) and Library version's (the original of a detached field). Neither folds a group of rows. *Corrected the same day: this line first said the Check stage's was the only one.* | *In two projects or more · 7* is the least useful group for this job, and at fifty items it would be the longest. | Drawn open, every row shown. | A new component in `components/`, with its docs page and its states (closed, open, hover, focus, disabled) in both themes |
| **B3** | variant | **A count beside a Small heading.** `.count` is styled only inside `.tabs`, so a count elsewhere has no style. | *In no project · 3*: the count is set in the heading's own weight. | Written as text in the heading. | A variant of Small heading in `heading.css`, or `.count` lifted out of `tabs.css`, with the docs page updated |
| **B4** | component + decision | **Selecting several rows and acting on them at once**: a checkbox on a library row and a bar with the act. | Three items in no project, each deleted on its own: three confirmations for one decision. | One *Delete…* per row. | **The register first.** Bulk delete is not in the specification (§5 confirms one item at a time), so it is a product question before it is a part. If answered yes: a row selection state and an action bar, by §18 |

**Found on the first screen, and not a gap in the system** (they go elsewhere):
- **How a person gets to this screen.** No navigation leads here: global navigation has three entries (§8, Q29). That is
  information architecture, and the register's.
- **Delete on a library row.** The product deletes from the Item sheet (§5, Q17). The example puts *Delete…* on the row
  because curating by use is the job. The button and the Confirmation pattern already exist; *where* it lives is a
  product decision.
- **The screen's words are not in `microcopy.md`.** They are written against `voice.md`. A line enters the table when
  the screen enters the product (§14).

## From the second test — Copies of code-style (2026-11-03)

The screen: [`examples/copies.html`](examples/copies.html), *Copies of code-style*, for **RJ-3** (*fix something once and
have the fix reach every copy*, importance 3) and **H-J3** (*change one copy for one project*, importance 2). It shows the
original in My library beside its copy in each project: linked or detached, which fields differ, the original one fold
away. `copies-promote.html` adds the Dialog with a field pattern. The owner asked for a screen less like the existing ones.
It is built from one pattern and the Page head, Callout, Small heading, Row list, Card, Tag, File block, Library version,
Link button, Button, Dialog, Text field and Form actions, with no style and no class of its own, in both themes. **What
it lacked, four entries, one of them a defect:**

| # | Kind | What was missing | Where it showed | What was done on the screen | Enters by |
|---|---|---|---|---|---|
| **B5** | **defect** | **The neutral Callout's tone is guessed from its words.** `build_mockups.transform` turns `.callout` into `.callout-reminder` only when the first line starts *Before you* or *Used in N project*. Any other blast-radius sentence stays Problem rose, with no warning. This breaks §16, *every state is a class, never a guess from content*. | *Editing the original reaches 1 of 3 projects* came out rose on the first build. | The screen names the class, `callout callout-reminder`, which the system already has. | **Step 7's defect table.** The tone moves into the markup of every screen that carries a blast radius, and the guess is removed from `transform` |
| **B6** | component | **A comparison across copies**: one row per field, one column per copy, the original first. Cards cannot line fields up, so *Lands at* in one copy sits beside *Content* in the next. | The whole screen: the job is *which copy differs where*. | Drawn as one Card per project, each listing its own differing fields. | A new component, with its docs page and its states in both themes; it must hold mono values and a long path |
| **B7** | variant | **Changed lines marked in a File block.** The added line, *Money is integer cents*, looks like every other line. | Every detached copy's content. | The whole content shown; the original folds away under Library version, so the reader compares by eye. | A variant of File block (`code.css`): a line added, a line removed, through roles, in both themes, never by colour alone |
| **B8** | variant | **A File block that wraps.** In a narrow column it scrolls sideways (`overflow-x: auto`), so the end of a line is hidden. | The content of each card, at a third of the width. | Left to scroll. | A wrapping variant of File block for prose-like files, kept apart from code that must not wrap |

**Found on the second screen, and not a gap in the system:**
- **Reset and Promote outside the configuring mode.** §7 and Q21 keep a detached row's Edit, Reset and Promote in the
  project's configuring mode. The example offers them from the item's own screen, because the job reads across projects.
  Whether that is allowed is a product decision, for the register.
- **The entry point**, again: no navigation reaches this screen. The register's.
