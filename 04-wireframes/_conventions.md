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
- **No JavaScript in a product page** beyond what a link does. A state is a page, not a toggle. The
  viewer (§7) has script; it is chrome.
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

**Two kinds of file, and only one of them is product.**

- **`pages/<name>-<state>.html` is the product and nothing else** — the 1440 canvas, no chrome, no
  script. It opens directly as a page of its own, which is what later lessons grow.
- **`pages/index.html` is the viewer** — the only page with chrome, and the one phase 04 links to. It
  shows one wireframe at a time by its address, `index.html#projects-default`.

**The viewer, left to right:**

- **The phase rail**, fixed to the window's left edge: the course's twelve phases, the same rail
  `research.html`, `personas.html` and `ia.html` carry, with 04 current. **It collapses to its
  numbers**, and the state is shared with the phase pages.
- **The wireframe tree** (step 4): section → screen → state, current page marked. **Written once, in the
  viewer**, so it cannot drift between pages. **It is the wireframe's navigation, not the product's.**
  The product has three global entries, `My library`, `Public library` and `Projects` (Q29), drawn
  inside the canvas; the tree must never read as another menu.
- **The stage**: the screen's name, its states as a switcher, where it sits in the flow, and **Open as a
  page** — then **the frame**.

**The frame is 16:9 and shows the canvas at 80%**, scaled down further only when the window is too
small to hold it, and **it is centred, with its chrome, in the space beside the tree.** **The viewer page never scrolls** — not sideways, not down. **Only the wireframe
scrolls, vertically, inside its frame.**

The rail, the tree and the stage use the site's background, mono and accent. **That accent is chrome and
never crosses into the canvas.** Desktop-first, one 1440 canvas (§3); responsive is lesson 10.
