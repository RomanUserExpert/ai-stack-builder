# Wireframe conventions — lesson 04, step 2

> **Written 2026-09-26, from [`sitemap.md`](../03-information-architecture/sitemap.md) and
> [`_screens.md`](_screens.md).** Every wireframe in this folder follows these rules, and lessons 05–08
> read them too: 05 rewrites the text, 06 brings the visual language, 07–08 build UI and tokens **on
> these same files** rather than redrawing them. A rule that changes is changed here first.

---

## 1 · Detail — structure, hierarchy, zones. Grey.

- **Only structure, hierarchy and zones.** What is on the screen, what matters more, what belongs
  together. Nothing about how it will look.
- **Grey only.** White, black and greys, nothing else. No colour anywhere, including states: a
  Problem, a Note and a `Skipped` stage are told apart by **words and position**, never by red, amber
  or green. *Colour is lesson 06.*
- **One typeface: Inter**, for everything, loaded from Google Fonts. It is there so proportions read,
  not as a type decision — sizes and weights are only as many as hierarchy needs. *The type scale is
  lesson 08.*
- **Images: a square crossed with an `X`** — an outlined box with both diagonals. Only where an image
  would really be; the product has almost none.
- **Icons: a black square with slightly rounded corners.** One size throughout, labelled by the text
  next to it or by `aria-label`. It marks *an icon goes here*, never which one.
- **A 4 px grid.** Every spacing, size and gap is a multiple of 4.
- **Zones are labelled** — a small grey caption naming the zone and its main action — and stay quiet
  enough that the screen still reads as a screen.
- **Neutral, not themed.** §3 says dark from day one; a wireframe is not a theme, and two real themes
  are designed in lesson 06, not inverted from this.

## 2 · Markup — semantic HTML

- **`header`, `nav`, `main`, `section`, `article`, `aside`, `form`, `button`, `ul/ol`, `table`,
  `details`** — the element that says what the thing is. **Not `div` soup**: a `div` only where no
  element has the meaning.
- **A button is a `button`, a link is an `a`.** Actions that change something are buttons; moving to
  another page is a link — which is how step 7 wires the flow.
- **A row in a set is an `article` or a list item**, carrying its own state in its text.
- **Stages of `Run` are an ordered list**, each expandable with `details` — the Vercel shape (§6).
- **No JavaScript** beyond what a link does. A state is a page, not a toggle.
- **The wireframe's own chrome is outside the product markup** — see §7 below.

## 3 · Text — real, from the domain

- **Real items, real projects, real findings.** `db-migrate`, `code-style`, `.mcp.json`,
  `GITHUB_TOKEN` — never *Lorem ipsum*, *Title 1* or *Item name*.
- **The vocabulary of §4, exactly**: *Item, Project, Library, Workspace*. **Never *Bundle*.** The six
  kinds are `skill · agent · prompt · mcp · script · app`.
- **Severities by their names**: *Problem*, *Note*, *Skipped*.
- **Checked, never works.** No *works*, *valid*, *passing* or a bare tick anywhere — the verdict is
  *checked* with its counts and date (§6).
- **No score, rating or badge** on anything. Usage facts only — *used in 3 projects* (§5).
- **Findings in the present tense, naming the consequence**: *Two items write to `.mcp.json`. The
  archive will contain only one of them — `db-tools`.*
- Text is written to be **replaced in lesson 05**; it must still be the real length, because width is
  one of the questions this lesson answers (the longest project row).

## 4 · File names — `<name>-<state>.html`

- **Every page is `<name>-<state>.html`**, Latin, lowercase, hyphenated, in this folder
  (`04-wireframes/`, the lesson's folder — the course's `wireframes/`).
- **Names**, from `_screens.md`:

  | Screen | `<name>` |
  |---|---|
  | Projects | `projects` |
  | Project — viewing | `project` |
  | Configuring the set — a mode | `project-configuring` |
  | Run | `run` |

  A mode is named after the place it belongs to, which is how the file says it is not a place.
- **States**: `default` · `empty` · `error` · `loading` · `success`.
  - **`default`** is the screen filled with real data. `_screens.md` keeps *success* for a real
    *it worked*, so the filled view needs a name of its own.
  - **`success`** exists only where `_screens.md` marks it — in the main flow, only `run-success.html`.
- Examples: `projects-default.html`, `projects-empty.html`, `project-configuring-loading.html`,
  `run-success.html`.

## 5 · States — each one its own page

- **One state, one page.** Same structure, different content — the zones do not move between states.
- **Only the states `_screens.md` marks `✓`.** A `—` means no page.
- **Empty and error always carry a way out**, and that way out is one `flows.md` already has.
- **Error is real** — the product is online (Q24) — and uses the shapes already decided: *the edit did
  not land* (Q26), *the library reads as before* (Q27), *what could not be produced says so* (Q28).
- **A Problem is not an error.** A check that found Problems is a check that worked.
- **`Run` loading is the stage stack mid-sweep**, not a spinner (§6). Ordinary waits elsewhere are
  decided on the first screen that has one, then written here.
- **Nothing is disabled** except the empty project's control into `Run` (Q16), and it is labelled
  inert rather than hidden.
- **States that live inside a page are content, not pages**: §7's item states, the stale verdict, the
  example project, the unclean-export confirmation in the row under its finding.

## 6 · What waits

**Final UI, final fonts and icons, colour, shadows, radii beyond the icon placeholder, motion, the
type scale, tokens and components.** Each has its lesson — 05 text, 06 concept, 07 UI, 08 tokens,
09 design system, 11 animation. A wireframe that starts to look finished is a wireframe that has
started deciding things it was not asked to.

## 7 · The frame around a wireframe

- **Desktop-first, one fixed canvas: 1440 px wide** (§3). Responsive is lesson 10. No horizontal
  scroll, and no scroll inside scroll.
- **Above the canvas, outside it**: the state switcher — links to every state of this screen, the
  current one marked.
- **Left of the canvas, outside it — two columns of chrome.**
  - **The phase rail**, fixed to the left edge of the window: the course's twelve phases, the same list
    `research.html`, `personas.html` and `ia.html` carry, with 04 current. **It collapses to its
    numbers**, which stay links; the state is remembered across pages. *This toggle is the one piece of
    script on a wireframe page, and it belongs to the chrome, not to the product.*
  - **The wireframe tree**, to the right of the rail (step 4): section → screen → state, current page
    marked. **It is the wireframe's navigation, not the product's.** The product has three global
    entries, `My library`, `Public library` and `Projects` (Q29), drawn inside the canvas; the tree must never read as a third menu.
  - Both use the site's background, mono and accent. **That accent is chrome and never crosses into
    the canvas.**
- **Inside the canvas is product, and only product.**
