# The check — the system and the product together

**Lesson 09, step 7, 2026-11-03.** The defect table comes first, and the fixes follow it. Two instruments were used:
- **`tools/system_check.py`** covers the course's five classes. It compares computed styles in a browser across 46 docs
  pages and 83 dressed screens, the classes in `components/` against what the docs show, the themes, the patterns and the
  docs' coverage. It is re-runnable, and its checks become guards when the table is fixed.
- **`/impeccable audit`**, with its bundled detector (`impeccable detect`, v4.5.2, over `design-system/` and every
  mockup), and a reading by hand. **Every detector finding was checked in a browser before it was counted.**

## The table

| # | Class | File | Element | What is wrong | How to fix | Sev. |
|---|---|---|---|---|---|---|
| **S1** | 1 · looks different | `build_mockups.transform` → 5 wireframe pages (Item sheet ×3, Add item, Import JSON) | `.callout` of the keys reminder and the blast radius | **The neutral tone is guessed from the first words** (*Before you…*, *Used in N project*). A new disclosure in other words is drawn Problem rose without a warning: found on `examples/copies.html` (backlog B5). The docs show a neutral Callout; the product gives it only to five sentences. | The wireframe source names `callout-reminder`, which `wireframe.css` ignores. The guess leaves `transform`. **Guard: a bare `.callout`, with no tone class, must be a Problem** (its severity starts *Problem*). Today 9 of 9 are | P1 |
| **S2** | 1 · looks different | `row.css` · Set row states (§7) docs page | `.set-item.is-selected .row-actions` | In the product, the row opened in the item side panel **hides its actions** (`display: none`, `project-item`). The docs page never shows that state, so the docs row and the product row differ. | Add the state *Opened in the side panel* to the Set row states page, cut from `project-item` | P2 |
| **S3** | 1 · looks different | `library-version.css` · Link button docs page | `.library-version summary .link-button` | Inside Library version's summary the Link button loses its padding (`4px` → `0`). The Link button page shows only the standalone one. | Add the in-summary variant to the Link button page, cut from `project-detached-default` | P3 |
| **S4** | 2 · docs ≠ code | `build_kit.py` · Button docs page | `<button>` *Duplicate* with a `copy` icon | The docs show a **secondary button with an icon**. No screen has one: every secondary button in the product is text only. | Drop the icon from that specimen, so the page shows what the product draws | P3 |
| **S5** | 2 · docs ≠ code | `page-head.css` | `.description-wide` | A Page head variant in the code (a wide description, on Project, Public library and Shared project) that **no docs page shows**. | Add the variant to the Page head page, cut from `project-default` | P2 |
| **S6** | 2 · docs ≠ code | `row.css` | `.row-tight.row-1`, `.row-tight.row-2` | Two Row list variants (one column, two columns) that `transform` sets on screens and **no docs page shows**. | Add both variants to the Row list page, cut from the screens that carry them | P2 |
| **S7** | 5 · no docs page | `base.css`, `frame.css`, `drawer.css`, `aside.css`, `sidebar.css` | `.canvas`, `.app-main`, `.with-drawer`, `.with-aside`, `.config-layout` | **Five layouts with no docs page.** Two appear only inside patterns, and `.with-aside`, the receiver's layout, appears nowhere in the docs. | A docs page, **Layouts**, generated like the others: each frame, what it holds, its screens, a live frame of one | P2 |
| **S8** | 5 · no docs page | `tokens.css` | **142 of 195 tokens** | Named on no docs page. Only the roles a component's anatomy cites appear anywhere. | A docs page, **Tokens**, generated from `tokens.css`: every token, its level, its dark and light value, a swatch, and the component files that read it | P1 |
| **S9** | 3 · one theme | — | — | **None found.** `concept_tokens.py` finds 0 roles without a light value and now fails the build on one; no component file holds a `[data-theme]` rule; `build_docs` checks in a browser that every state drawn differs from rest in both themes. | — | — |
| **S10** | 4 · pattern styles | — | — | **None found.** The six patterns have no `style=`, no `<style>` and no class of their own (guard 12). | — | — |
| **I1** | audit · a11y | `page-head.css` | `.meta a`: the Breadcrumb's link up; a project named on a usage line | **A link is told from its line by colour only.** On the Breadcrumb that is Ink 2 against Ink 3, about 1.4:1. On a usage line it is the same colour, 1:1 (backlog B1). WCAG 1.4.1 asks for 3:1 or a non-colour cue. | Underline the link at rest, the line drawn in a role (`--line-strong`), and brighten it on hover. **No new value** | P1 |
| **I2** | audit · a11y | `build_docs.py` → `docs/index.html` | the showcase's live previews | The previews are real screens, so the showcase's outline carries **4 `<h1>`s and an `h1 → h3` skip** (detector: `skipped-heading`, confirmed). A screen reader lands in the specimens' headings. | Mark each preview `aria-hidden` and `inert`. Each one is already a link to its page, which carries the name | P2 |
| **I3** | audit · theming | `tokens.css`, light | `--disabled` | **In light, a disabled field is white**, brighter than a field at rest, so it reads as more available. Found in step 3 and left to the owner. | A light value for `--disabled`, **proposed and signed** (§18): the light control ground one step down, so it reads as recessed | P2 |
| **I4** | audit · detector | 39 pages | `em-dash-overuse` (advisory) | The detector counts em dashes in the copy. | **Not a defect.** Punctuation is `voice.md`'s, and copy changes only through `microcopy.md` (§14). Recorded, not changed | — |
| **I5** | audit · detector | 142 pages · 123 pages | `design-system-color` (`rgb(0,0,0)`) · `flat-type-hierarchy` (16 / 16 / 16 px) | **False positives, verified.** The detector does not follow `@import`, so it reads the pages unstyled. In a browser the brand is `rgb(243,244,239)`, and h1 / h2 / body are 28 / 20 / 14.5 px. | None. Noted so the next audit does not re-raise them | — |

**In numbers:** 13 rows that need work — 3 P1, 6 P2, 2 P3, and S9 and S10 found nothing — plus 2 detector rows that are not
defects. Two rows wait on the owner: **I3**, a light value, and **the host** (below).

## /impeccable audit — the score

| # | Dimension | Score | Key finding |
|---|---|---|---|
| 1 | Accessibility | 3 | I1, a link told by colour only; I2, the showcase's outline. Contrast is 83 pairs per theme, all AA; focus is 3:1 on every ground; reduced motion stops the sweep and the skeleton |
| 2 | Performance | 4 | Static pages, a sprite of icons, no script but the theme switch and the docs' state copier |
| 3 | Theming | 3 | Two levels of tokens, no literal in a component (guards 1, 5); I3 in light |
| 4 | Responsive | — | **Not scored, by plan:** desktop-first (§3); responsive is lesson 10 |
| 5 | Implementation integrity | 3 | S1, a tone guessed from words; S2–S8, docs and code drifted at the edges |
| **Total** | | **13/16** | Good (four dimensions scored) |

**Integrity verdict: pass.** One system, guarded at build. The drift is at its edges: variants the docs miss, layouts and
tokens with no page. No screen carries a value of its own.

**What works:** every screen and docs page links one `index.css`, 12 guards run on every build, the docs' specimens are
the product's own markup, and the states are checked in a browser in both themes.

## Decided by the owner before the fixes

- **I3**, the light `--disabled` value.
- **The host for the showcase.** D7 recommended Vercel, where the showcase already is. The course asks for GitHub Pages.
