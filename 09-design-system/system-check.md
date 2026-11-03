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
| **I6** | audit · deploy | `vercel.json` · `docs/index.html` | the showcase's address | **Found while fixing, live**: Vercel serves `/design-system/docs` with no trailing slash (`trailingSlash: false`), so the page resolves `../index.css` against `/design-system/` → `/index.css`, a 404. **The showcase online was unstyled and its links went nowhere.** | The showcase moves to `docs/components.html`; `index.html` sends to it; `vercel.json` redirects `/design-system/docs` to `/design-system/docs/components` | P0 |
| **I4** | audit · detector | 39 pages | `em-dash-overuse` (advisory) | The detector counts em dashes in the copy. | **Not a defect.** Punctuation is `voice.md`'s, and copy changes only through `microcopy.md` (§14). Recorded, not changed | — |
| **I5** | audit · detector | 142 pages · 123 pages | `design-system-color` (`rgb(0,0,0)`) · `flat-type-hierarchy` (16 / 16 / 16 px) | **False positives, verified.** The detector does not follow `@import`, so it reads the pages unstyled. In a browser the brand is `rgb(243,244,239)`, and h1 / h2 / body are 28 / 20 / 14.5 px. | None. Noted so the next audit does not re-raise them | — |

**In numbers:** 14 rows that need work — 1 P0 (I6, found while fixing), 3 P1, 6 P2, 2 P3; S9 and S10 found nothing — plus 2
detector rows that are not defects. Two rows wait on the owner: **I3**, a light value, and **the host** (below).

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

## Decided by the owner before the fixes — Q50, *делай по рекомендациям*

- **I3: `--disabled` in light is `#ECEDE6`**, `--color-neutral-light-250`, the light bar's grey, already a primitive. It
  sits 1.07:1 under the ground, and Ink 3 on it is 5.22:1. Signed in `06-concept/concept.md`.
- **The host stays Vercel (D7).** The course asks for GitHub Pages; two hosts for one site would be two places to drift.
  The showcase's address is in `README.md`, *Design system*.

## Dispositions — every row fixed on 2026-11-03, every class a guard

| # | Fixed by | Guard |
|---|---|---|
| S1 | `callout-reminder` named on the 5 wireframe pages (and the 8 prototype steps rebuilt from them); the guess left `transform` | **14** — a bare `.callout` must be a Problem; negative-tested |
| S2 | *Active, viewing — no actions* on the Row list page, cut from `project-item` | **17** — docs and screens compared in a browser |
| S3 | *Inside Library version's summary* on the Link button page | **17** |
| S4 | The icon dropped from *Duplicate* | **17** |
| S5 | *A wide description* on the Page head page | **15** — a class in `components/` shown on no docs page |
| S6 | *Two columns* and *One column* on the Row list page | **15** |
| S7 | [`docs/layouts.html`](../design-system/docs/layouts.html): five frames, each with its screens and a live frame; words in `docs_content.LAYOUTS` | **15** |
| S8 | [`docs/tokens.html`](../design-system/docs/tokens.html): all 195 tokens, level, dark and light value, swatches in both themes, the files that read each | **16** — a token with no row; negative-tested |
| S9, S10 | Nothing to fix | `concept_tokens.py` (a role in one theme fails the build since step 5); guard 12 |
| I1 | `.meta a` underlined at rest in Ink 3, brighter on hover; no new value. 20 pages change, the Breadcrumb only; 63 of 83 identical | **17** — a link in a meta line with no underline |
| I2 | The showcase's previews are `inert` and `aria-hidden` | — (the detector's `skipped-heading` is gone) |
| I3 | `LIGHT_FIXED["disabled"]`, signed (Q50) | `concept_tokens.py` checks the light value against the signature |
| I6 | `components.html`, the redirect page, the `vercel.json` redirect | guard 11 expects `components.html`; the address is checked after the deploy |
| I4, I5 | Not defects | — |

**D2 is done with the table:** `07-ui-assembly/ui/kit.html` is now a generated redirect to the docs. Its address stays,
so lessons 07 and 08's pages, which frame it, show the docs. Guard 8 checks the docs' specimens' words. The flip check in
`build_components.py` runs over the docs pages instead of the kit.

**`tools/system_check.py` stays as the instrument.** `kit_check.py` runs its checks at every build as guards 15–17, and
17 runs in a browser (`--fast` skips it).

## Found after the close of the table (2026-11-03, the owner)

| # | File | Element | What was wrong | Fixed by | Guard |
|---|---|---|---|---|---|
| **I7** | `build_mockups.transform` → every docs page | the docs' navigation, crumbs and pager | **Dead since step 2.** `transform` rewrites a link to a page with no mockup into `../pages/…`, which is right for a screen and wrong for the docs, whose `patterns.html` and `components.html` are no screens. Every link in the docs' head led nowhere. | `transform` relinks only a screen of the product. A specimen's own links now lead to the screen it was cut from (`04-wireframes/mockups/`), from the docs and the patterns alike | **18**: every local link on the docs, the patterns and the examples leads to a file; negative-tested |
| **I8** | `build_docs.py` → `components.html` | the previews of Row list and Usage facts | A library row drawn at a sheet's 640 px leaves its name 35 px: the usage line and the actions take the rest. | Those two previews are drawn at a screen's width (`--width-canvas`) and scaled to fit | — |

**What the check missed, and why:** `system_check.py` compared how things look, not where they lead. Guard 18 is the
class it lacked.
