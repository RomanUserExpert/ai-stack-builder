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
- **Nothing on the canvas that the product would not show** (2026-09-26). No zone captions, no notes
  to the reader, no *main action: …* labels — **every word on the canvas is a word the person using the
  product would read.** Zones are told apart by structure and spacing; what a zone is for goes in an
  HTML comment or an `aria-label`, and explanations about the screen go in the viewer's
  Persona · Job · Flow lines (§8) or in `_screens.md`. *The captions were in the first draft of this
  rule and came out after the first wireframe: they read as part of the screen.*
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
  viewer (§8) has script; it is chrome.
- **The wireframe's own chrome is outside the product markup** — see §8 below.

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
  - **An open popover is drawn as its own page, `<name>-filters.html`** — the default with the popover
    open. It is not one of the five states; it is how a page looks while a question is being asked of it.
  - **A state with more than one cause takes the cause as a suffix**: `<name>-<state>-<cause>.html`.
    Projects has two errors that ask for different ways out, so it has `projects-error-filtered.html`
    and `projects-error-server.html`, never one page trying to be both.
- Examples: `projects-default.html`, `projects-empty.html`, `projects-error-server.html`,
  `project-configuring-loading.html`, `run-success.html`.

## 5 · States — each one its own page

- **One state, one page.** Same structure, different content — the zones do not move between states.
- **Only the states `_screens.md` marks `✓`.** A `—` means no page.
- **No state is a dead end** (2026-09-26). **Every empty and every error carries at least one action
  that moves the person on**, and that way out is one `flows.md` already has. Where the first way out
  can itself fail — *Try again* on a server error — **a second one goes somewhere that does not depend
  on it** (*Open My library*).
- **The block says what happened, in the present tense, then the way out.** One heading, one sentence,
  the actions. For a server error, the code and time in small grey text under it — the person can quote
  it; it is not the message.
- **Filtered to zero is an error, not an empty** (owner, 2026-09-26). The things exist; the person's own
  search and filter hide them. The page keeps what was typed and which filters are on, says so, and its
  way out is **Clear filters**.
- **An action that cannot act is hidden in that state, not greyed.** Search and `Filters` are not drawn
  on an empty list or on a list that did not load — there is nothing to search. This is §9's rule, and
  it is the one case where a zone may be absent from a state; it never *moves*.
- **Error is real** — the product is online (Q24) — and uses the shapes already decided: *the edit did
  not land* (Q26), *the library reads as before* (Q27), *what could not be produced says so* (Q28).
- **A Problem is not an error.** A check that found Problems is a check that worked.
- **`Run` loading is the stage stack mid-sweep**, not a spinner (§6). **Every other wait is a
  skeleton** (decided on Projects, 2026-09-26): grey bars in the real rows' columns, at the real rows'
  heights, so nothing moves when the content arrives. The chrome, the page head and the controls are
  real; only the content is skeleton. **No spinner, and no row shown before it is real** — the
  optimistic option is not taken silently (register, *Waits*).
- **A form that is loading** (the Item sheet, 2026-09-26): **what is already known is real** — the title
  from the row you clicked, every label, every section heading — and **every field is a grey bar at its
  real height**. Nothing is editable, and **Save and Delete are not shown** until they can act; *Cancel*
  stays, so the sheet can always be left.
- **Nothing is disabled** except the empty project's control into `Run` (Q16), and it is labelled
  inert rather than hidden.
- **States that live inside a page are content, not pages**: §7's item states, the stale verdict, the
  example project, the unclean-export confirmation in the row under its finding.

## 6 · Patterns — Projects is the example

**`projects-default.html` is the reference page** (owner, 2026-09-26). Every other screen is built out of
the pieces it established, and **all of them live in `pages/wireframe.css`** — a product page carries no
`<style>` of its own. A new screen reuses a pattern before it invents one.

| Pattern | Where it is first | What it is |
|---|---|---|
| **Page head** | Projects | The title, and the page's actions on the right. A line of facts under it only when they are product facts (*14 items · checked 2 days ago*), never a caption |
| **Find** | Projects | Search on the left, one `Filters` button in the far right corner. Everything else is behind it |
| **Card grid** | Projects | **Projects are cards, items are rows** (owner, 2026-09-26) — a project is a set you come back to, an item is a line in a list, and the two must never be mistaken for each other. Three columns: name and description · facts · the last check under a rule · actions at the foot |
| **Kind tabs** | My library, Public library, the library panel | `All` first, then one tab per kind in §5's order — `skill · agent · prompt · mcp · script · app`. **On a page they carry counts** (owner, 2026-09-26), **and the counts follow the search**, so a tab with matches is itself a way out. A zero is shown, never hidden, so the order holds. Kind is a tab, not a filter — `Filters` holds the rest |
| **Row list** | My library, Project | `ol` of `article`s: what it is · what it says · what you can do. Kinds as a small outlined tag. **Rows are short** (owner, 2026-09-26): source, origin and **licence go in one grey line under the description**, usage is one line in the middle — no stacked labels, so a row is two or three lines tall |
| **Filters popover** | Projects, My library, Public library | **One shape everywhere** (owner, 2026-09-26): title *Filters* · **Reset filters** on its right · the groups, each a `fieldset` with its `legend` · **Cancel / Apply** at the foot. It hangs from the `Filters` button, right-aligned. Nothing applies until *Apply*; the button then carries the count, *Filters · 1*. **Which filters a page gets comes from its persona and its content**, and a page with no evidence for sorting gets no sort |
| **Set list** | Project, Configuring | **The Library's row, in a set** (owner, 2026-09-26): name · kind · **state badges** (*Auto-added*, *Detached*, *Conflict* — a dashed tag) · one line of description · one grey line of facts. **Findings from the last check are a mark** — a glyph and a word, *Problem* or *Note* — in a narrow middle column. In Configuring the right column carries the `✕`, the refusal, or the detached row's commands |
| **Side panel** | Project — `project-item.html` | **Clicking a row opens the item beside the list, not over it** — a column on the right, the set still in view, the selected row filled grey. Read-only: *Open in My library*, *Remove in Configure*. Drawn as its own page, like the filters popover |
| **State block** | Projects empty / error | Icon or image, one heading, one sentence, the ways out. Server errors add the code and time in grey |
| **Skeleton** | Projects loading | Grey bars in the real rows' columns; head and controls real |
| **Callout** | Project, Run | A finding or a disclosure: a rule on the left, the severity **as a word** — *Problem*, *Note*, *Before you add it* |
| **Library sidebar** | Configuring | **The library panel is a full left sidebar** (owner, 2026-09-26), the height of the screen under the header — scope switch, search, kind tabs, rows with a tick. The set and its head sit to the right |
| **Sheet / dialog** | Item, Import | `<dialog open>` over a dimmed page: a sheet on the right for a form, a dialog in the middle for a command |
| **Run bar + stages** | Run | A bar that replaces the navigation, then an `ol` of `details` stages, then Export as the last stage |
| **Receiver's header** | Shared | The product's mark and *Shared by …*. No navigation, no sign-in |

## 7 · What waits

**Final UI, final fonts and icons, colour, shadows, radii beyond the icon placeholder, motion, the
type scale, tokens and components.** Each has its lesson — 05 text, 06 concept, 07 UI, 08 tokens,
09 design system, 11 animation. A wireframe that starts to look finished is a wireframe that has
started deciding things it was not asked to.

## 8 · The frame around a wireframe

**Two kinds of file, and only one of them is product.**

- **`pages/<name>-<state>.html` is the product and nothing else** — the 1440 canvas, no chrome, no
  script. It opens directly as a page of its own, which is what later lessons grow.
- **`pages/wireframes.html` is the viewer** — the only page with chrome, and the one phase 04 links to. It
  shows one wireframe at a time by its address, `wireframes.html#projects-default`. **It is not called
  `index.html`**: with `cleanUrls` and no trailing slash, Vercel serves an index at `/04-wireframes/pages`,
  and every relative path on it — the stylesheet, the frame, the page check — then resolves one folder
  too high. *Renamed 2026-09-26, after the deployed viewer came up unstyled.*

**The viewer, left to right:**

- **The phase rail**, fixed to the window's left edge: the course's twelve phases, the same rail
  `research.html`, `personas.html` and `ia.html` carry, with 04 current. **It collapses to its
  numbers**, and the state is shared with the phase pages.
- **The wireframe tree** (step 4): section → screen → state, current page marked. **Written once, in the
  viewer**, so it cannot drift between pages. **It is the wireframe's navigation, not the product's.**
  The product has three global entries, `My library`, `Public library` and `Projects` (Q29), drawn
  inside the canvas; the tree must never read as another menu.
- **The stage**: the screen's name and its state as the title, and **Open as a page** — then **the
  frame**. **Under Persona · Job · Flow, a row of the current screen's states** (restored 2026-09-26,
  owner) — one click between states without opening the tree. **It is generated from the tree**, so the
  two cannot say different things; states not drawn yet are faded in both.
- **Under the title, always three lines — Persona · Job · Flow.** Which persona the screen is for, which
  job from `jtbd.md` it closes, and where it sits in `flows.md`, taken from `_screens.md`. **Where a
  screen has none, the line says so in words** — *No job — and no job could (§9, Q25)* — **never blank
  and never omitted**: a missing job is a finding, the same rule the sitemap uses for an orphan.
- **The tree reads like a file explorer**: sections and screens are folders that open and close, states
  are files, guide lines with rounded elbows show the nesting, and the folder holding the current page
  opens itself.

**The frame is 16:9 and shows the canvas at 90%**, scaled down further only when the window is too
small to hold it, and **it is centred, with its chrome, in the space beside the tree.** **The viewer page never scrolls** — not sideways, not down. **Only the wireframe
scrolls, vertically, inside its frame.**

The rail, the tree and the stage use the site's background, mono and accent. **That accent is chrome and
never crosses into the canvas.** Desktop-first, one 1440 canvas (§3); responsive is lesson 10.
