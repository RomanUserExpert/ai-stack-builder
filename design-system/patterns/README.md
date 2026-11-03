# Patterns

**Compositions of components that already stand on three screens or more**, built by `tools/build_patterns.py`
(lesson 09, step 4). One file per pattern, cut from a real wireframe page, linking `../index.css` alone, with no style of
its own. Each file's head comment names its components and the screens it stands on.

| File | Pattern | Screens |
|---|---|---|
| `browse-head.html` | Page head, then search and Filters, above a collection | Projects, My library, Public library |
| `set-with-side-panel.html` | A project's set with one item open beside it | Project, Configuring, Detached row |
| `configuring-layout.html` | The library panel and the set, side by side | Configuring, Detached row, Project (empty) |
| `run-report.html` | Summary, stages, the Export stage last | Run project, single item, shared project, shared item |
| `confirmation.html` | Veil, sheet, the consequence, Cancel … the act | My library, Project, Projects, Run project |
| `dialog-with-field.html` | A dialog that asks for one value, or hands one over | My library, Project, Detached row |

**A pattern exists only if it can name three screens.** Its signature runs over all 80 pages at every build, and the
build fails below three; an overlay never counts. What was looked at and fell short is listed on
[`docs/patterns.html`](../docs/patterns.html). A hand edit here is overwritten by the next build.
