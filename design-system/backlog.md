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
| **B2** | component | **A disclosure: a group that folds.** The system's only expansion is the Check stage's, which belongs to Run. | *In two projects or more · 7* is the least useful group for this job, and at fifty items it would be the longest. | Drawn open, every row shown. | A new component in `components/`, with its docs page and its states (closed, open, hover, focus, disabled) in both themes |
| **B3** | variant | **A count beside a Small heading.** `.count` is styled only inside `.tabs`, so a count elsewhere has no style. | *In no project · 3*: the count is set in the heading's own weight. | Written as text in the heading. | A variant of Small heading in `heading.css`, or `.count` lifted out of `tabs.css`, with the docs page updated |
| **B4** | component + decision | **Selecting several rows and acting on them at once**: a checkbox on a library row and a bar with the act. | Three items in no project, each deleted on its own: three confirmations for one decision. | One *Delete…* per row. | **The register first.** Bulk delete is not in the specification (§5 confirms one item at a time), so it is a product question before it is a part. If answered yes: a row selection state and an action bar, by §18 |

**Found, and not a gap in the system** (they go elsewhere):
- **How a person gets to this screen.** No navigation leads here: global navigation has three entries (§8, Q29). That is
  information architecture, and the register's.
- **Delete on a library row.** The product deletes from the Item sheet (§5, Q17). The example puts *Delete…* on the row
  because curating by use is the job. The button and the Confirmation pattern already exist; *where* it lives is a
  product decision.
- **The screen's words are not in `microcopy.md`.** They are written against `voice.md`. A line enters the table when
  the screen enters the product (§14).
