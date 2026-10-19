# Audit: every screen against the kit, DESIGN.md and microcopy.md

**Phase 07, step 9, 2026-10-19.** Two instruments ran against all 80 dressed pages and 239 flow steps:
- [`tools/audit07.py`](../../tools/audit07.py), checks A–E. They are re-runnable, and contrast is measured in the
  browser on every page;
- the `impeccable audit` detector (`impeccable detect`) over every mockup and `kit.css`. Each of its findings was
  checked in context.

**The table came first and the fixes after**, as asked. The *Done* column records what was done.

## Defects

| # | Check | File(s) | Element | What is wrong | How to fix | Done |
|---|---|---|---|---|---|---|
| 1 | one component, several markups | 24 pages (projects-*, library-*, item-*, json-*) and their flow steps | `.page-head` | Three shapes. The `h1` is sometimes wrapped in a `div` and sometimes bare (Library, Item). The action is either in `.head-actions` or a bare `a.button` (Projects) | The build gives every page head one shape: `div` (title, meta) + `div.head-actions`. Drop the kit rule `.page-head>.button` | ✓ |
| 2 | one component, several markups | Project body, Library and Projects empty, the dead links | the state tile in `.state-block` | Three drawings. `svg.state-icon`; `span.state-image` holding an `svg`; or no element, with the tile and icon painted by CSS (`::before`/`::after`, a mask) | One element everywhere: `svg.icon.state-icon`, its icon chosen by the build. The kit's `.state-image` and its fallback pseudo-elements are removed | ✓ |
| 3 | contrast below AA | run-error-setup (and its flow step) | `code` *SETUP.md* inside the lime *Write SETUP.md again* | Ink on lime, **1.2:1**. My phase-07 wrap of file names in `<code>` gave the code the Ink colour inside a lime button | Kit: `code` inside a button inherits the button's colour, with no chip | ✓ |
| 4 | a heading level skipped (impeccable) | Project, Configuring, Detached row, Shared project: about 120 pages and steps | the set's rows (`h3`) under `h1` | The section is named only by `aria-label`, so `h1` jumps to `h3` and the outline has a hole | The build adds a visually hidden `h2` that names the section, from its own `aria-label`. No visible change | ✓ |
| 5 | text not in microcopy.md | project-configuring-*, project-detached-*, run-loading | the `title` *Auto-added — remove what requires it*; *The check is still running* | Two tooltips added by the phase 07 critique (#2, #32) never reached the table | Add the rows to `microcopy.md` | ✓ |
| 6 | text not in microcopy.md | project-item | the side panel's file block | **False positive of the audit.** The row exists; the table escapes `\|` and the check did not | `audit07.py` reads `\|` as `|` | ✓ |
| 7 | a stock image instead of the product's visuals | 205 pages (two headers) | `img.avatar`, `06-concept/img/portrait-96.jpg` (Unsplash) | The only photo is stock, and there is no `visuals/` | **Kept, on the owner's word** (step 4 skipped, 2026-10-19: *одна фотка… пофиг*). Recorded in DESIGN.md as a placeholder portrait, not a product visual | recorded |
| 8 | prototype markup differs from the page | 9 flow steps | `a.check`, `a.search`, `a.pick`, `a.remove` | A flow's one live hotspot is a link wrapping the control, so the markup differs from its page | **Kept.** This is the prototype's mechanism (`_conventions.md` §3); the dressed look is the same | kept |
| 9 | own styles / not on kit.css / a style outside the kit | all 319 | — | **None.** Guards 1–7 pass: no `style=`, no `<style>`, one stylesheet, every class in the kit, every variable declared, the `:root` equal to `tokens.css` | — | pass |
| 10 | an icon outside the set | all 319 | the sprite and the CSS masks | **None.** 30 icons, all from `06-concept/icons/lucide`, none guessed (`circle-dashed`); the masks come from the same set | — | pass |
| 11 | dressed words ≠ wireframe words | all 80 | — | **None.** Every dressed page carries exactly its wireframe's lines | — | pass |

## The detector's other findings, checked in context

| Finding | Count | Verdict |
|---|---|---|
| `flat-type-hierarchy` (*body 16, h1 16, h2 16*) | 299 | **False positive.** The detector cannot resolve `font: var(--t-…)`. In the browser: Display 28, Title 20, Heading 16, Body 14.5 |
| `overused-font` (Geist) | 88 | **The owner's choice** in phase 06 (concept.md, Typography); it stays |
| `icon-tile-stack` (a 48 px tile above a heading) | 3 | **The owner's decision**, 2026-10-11: *one neutral icon tile on every empty and error state* |
| `em-dash-overuse` | ≈120 | **Declined before** (critique #36): the dictionary's form, D23 |
| `cramped-padding` on `.export-stage` | 26 | **False positive.** Measured at 20 px all round on a 142 px card |

## Scores (`impeccable audit`, 0–4)

| Dimension | Score | Why |
|---|---|---|
| Accessibility | **3 → 4 after the fixes** | Contrast was measured on every text run of all 80 pages: one failure (#3), now fixed. There is a focus ring on every control, named removes, `inert` behind overlays, `aria-busy` and `aria-disabled` where they belong, and the heading outline is fixed (#4). Reduced motion stops shimmer and spinners |
| Performance | **4** | Static pages, one 40 KB stylesheet, an inline sprite of only the icons a page uses, two font families. No layout animation; only background and border transitions |
| Theming | **3** | Every value comes from a token, and the kit `:root` mirrors `tokens.css`. **Only the dark theme is dressed.** The light theme is one slice on the stand, its contrast measured (60 pairs); the full theme is lesson 09 |
| Responsive | **1, deliberate** | Desktop-first by §3. Screens are drawn at 1440 with fixed panels (440, 640). Controls are 28–32 px, under the 44 px touch target. **Lesson 10 is this** |
| Implementation integrity | **4** | The guards make drift fail the build, and the detector's findings were checked one by one above. Nothing decorative or generic is left, other than what the owner chose |

**Open, not a defect of this audit:** whether a shared *item* reads *Stop sharing…* (review G01-8). It waits for the
owner's answer.
