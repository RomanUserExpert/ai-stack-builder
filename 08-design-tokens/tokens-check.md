# Tokens check — phase 08, step 6

**The table first, then the fixes.** Written 2026-10-28. It checks `tokens.css`, `components/` and every dressed screen
against the course's seven defects, and adds the findings of `/impeccable audit`. Each row has a disposition: **fixed**,
or **kept** with the reason.

## How it was checked

All of it can be run again:
- **The guards**, `tools/kit_check.py`, run on every build:
  - 1: no literal in a component;
  - 5: no colour primitive in a component;
  - 2 and 6: no style on a screen, and only the two files linked.
- **The tokens' own check**, `check08()` in `tools/concept_tokens.py`. Every role resolves to the value phase 07 used.
  The light block holds no primitive and no hex. The contrast of 60 pairs (62 after the fixes) is written into each theme block.
- **Contrast in the browser**: `audit07.CONTRAST_JS` on all 83 pages, once dark and once with `?theme=light`. It takes
  each run of text, composites the background it really sits on, and compares the two.
- **Geometry**: every `calc()` in `components/` that multiplies or divides a primitive by a count.
- **`/impeccable audit`**: the detector run twice.
  - statically, over `08-design-tokens/`, the 83 pages, `kit.html` and `shell.html`: 401 findings;
  - in a browser at 1440 × 900, on `kit.html` and three screens in both themes: 121 findings.

## The table

| # | Check | File | Element | What is wrong | How to fix | Disposition |
|---|---|---|---|---|---|---|
| T1 | hex or font name in a class | `components/*.css` | — | **none**: guard 1, and `build_components.py` refuses one | — | clean |
| T2 | a component reads a colour primitive | `components/*.css`, `kit.html`'s own styles | — | **none**: guard 5 | — | clean |
| T3-1 | two names, one role | `tokens.css`, `checkbox.css` | `--edge-hover` and `--check-edge-hover` | One role, *a field's edge under the pointer*, has two names and two values: Ink 3 on fields, Ink 2 on a checkbox. It is audit M-3/M-4, kept apart in step 2 so that no pixel moved | One token, `--edge-hover`, read by the checkbox and the radio too. **Only the hover changes**: a checkbox's edge under the pointer takes Ink 3, like a field's. No screen is drawn hovered, so the goldens do not move | **fixed** |
| T3-2 | two names, one role | `tokens.css` | `--hover-wash`, `--row-hover`, `--segment-hover`, `--control-hover` | *Under the pointer, half a step up* is written four ways (audit D-1) | — | **kept**, by the owner (C, 2026-10-28). Each sits on a different ground: transparent, the cut-out, the track, a control. Merging them would be a redesign |
| T3-3 | two names, one value | `tokens.css` | `--side`/`--bar`, `--selected`/`--current`/`--raised`, `--disabled`/`--code-chip`/`--tile`/`--control`, `--focus`/`--mark`, `--brand`/`--action` | Same value, different names | — | **not a defect**: two roles, approved by the owner (A). The course's own rule is *two roles, two tokens, even if the value is the same today*. `--mark`/`--focus` and `--control-on`/`--action` already differ in light |
| T4-1 | semantic token with no source comment | `tokens.css`, `[data-theme="light"]` | all 45 overrides | The dark definitions name their uses. The light lines name nothing, so a reader cannot tell why `--side` is `--mica-57` | Each light line names the phase-07 variable whose light value it takes, or the reason it differs | **fixed** |
| T5-1 | geometry as a number | `code`, `frame`, `row`, `segmented`, `tabs`, `tag`, `checkbox`, `glyph` | `calc(var(--s1) / 2)` ×7, `calc(var(--s1) * -0.5)` | A 2 px step the scale did not have, written as half of `--s1` | Primitive **`--s-half`: 2px** | **fixed** |
| T5-2 | geometry as a number | `glyph`, `page-head`, `tabs` | `calc(var(--hairline) * 2)` ×3, `calc(var(--hairline) * 1)` | A doubled line (the spinner's ring, an underline) as a count of hairlines; `* 1` does nothing | Primitive **`--hairline-2`: 2px**; `* 1` → `var(--hairline)` | **fixed** |
| T5-3 | geometry as a number | `dialog`, `door`, `search`, `callout`, `form`, `state` | `--s12 * 3` (a dialog's top), `100vh - --s12 * 6` (a popover's height), `--s12 * 2 + --s6` (the door's top), `--measure - --s12 * 3` (the search field), `--measure + --s12 * 4` (a callout's sentence), `--s10 * 4` (a textarea), `(--s12 - --icon-l) / 2` (the state tile's inset) | Positions and measures as multiples of a spacing step | Primitives `--modal-top` 144px, `--popover-reserve` 288px, `--door-top` 120px, `--search-w` 496px, `--callout-measure` 832px, `--textarea-min-h` 160px, `--state-icon-inset` 14px. Each is checked to equal what its `calc()` gave | **fixed** |
| T5-4 | geometry as a number | `state.css` | 34 skeleton classes, `calc(var(--s1) * N)` | A size written as a count of `--s1` | — | **kept** (owner, 2026-10-28, with the step-1 recommendations). A skeleton's width is the length of the line it stands in for, copied from the wireframe: content, measured in the scale's unit, not a system size. 34 primitives would hold nothing anyone reuses |
| T5-5 | geometry as a number | `button`, `icon`, `run` | `* -1` | — | — | **not a defect**: a sign flip of a primitive, not a count |
| T5-6 | geometry as a number | `kit.html`'s own frame (`build_kit.PAGE_CSS`) | `--s12 * 12`, `* 8`, `* 14`… | The showcase's frame | — | **kept**: it is the showcase's frame, not a product component. It holds no colour of its own (guard 5) |
| T6 | a screen still on `kit.css`, or with its own styles | 83 pages, 241 steps | — | **none**: guards 2 and 6. `kit.css` is gone and guard 6 fails if it returns | — | clean |
| T7-1 | contrast below AA | `tokens.css`, `[data-theme="light"]` | `--control-on`: a checked checkbox or radio | **1.32:1** against a white panel, where WCAG 1.4.11 needs 3:1. A checked radio's dot barely shows. It is the same lime as the action, from the slice. No measured pair covered it | In light, `--control-on` → `--lime-494`, the light mark: 5.66:1 on a panel, 4.98:1 against its well. `--control-on-ink` → `--white`: the tick at 5.66:1. Dark is unchanged (10.79:1). The pair joins the measured list | **fixed** |
| T7-2 | contrast below AA | 83 pages × 2 themes | every run of text | **none**: 0 runs below AA in dark, 0 in light (in the browser); 60 of 60 measured pairs pass in each theme | — | clean |
| T7-3 | a role with no light value | `tokens.css` | `--sheet-edge`, `--danger`, `--danger-hover`, `--on-danger` | They keep their dark value in light (D1) | — | **kept**, listed in the light block. `--danger` passes AA (4.77:1 for its white text). `--sheet-edge` is white at 5 %, so it is invisible on light, but a sheet there is held by the veil and the shadow. Signing their light values is lesson 09's |

## `/impeccable audit`

| # | Finding (detector) | Where | Verified | Disposition |
|---|---|---|---|---|
| I-1 | `design-system-color`: a colour outside DESIGN.md (71 in the browser) | every light colour; the veil | **true**: DESIGN.md names only the dark palette, and not the veil | **fixed**: DESIGN.md gains the light palette, the two token levels and the veil |
| I-2 | `low-contrast` 212, `flat-type-hierarchy` 68, `cramped-padding` 8 | static scan only | **false**: the static scan does not follow `components/index.css`'s `@import`, so text reads as black and every heading as 16 px. The browser scan finds 0 of each | not a defect |
| I-3 | `kicker-above-heading` 10, `nested-cards` 3, `skipped-heading` 2 | `kit.html` only | **true of the showcase, not of a screen**: each state's `kit-label` sits above the demo's own `h1`, and a dialog is shown inside its stage frame | **kept**: the showcase's frame. The product pages have none (phase 07 fixed the heading skip there) |
| I-4 | `text-occlusion` 3 | `projects-filters`, light | the Filters popover covers the cards behind it | **kept**: that is a popover |
| I-5 | `overused-font`: Geist, 96 % | everywhere | true | **kept**: the owner's choice (concept.md, DESIGN.md) |
| I-6 | `em-dash-overuse` (advisory) | 28 pages | true | **kept**: declined in phase 07 (voice.md) |
| I-7 | `design-system-color` on an `outline`: `rgb(170,170,170)`, `rgb(0,0,0)` | inputs | **false**: the browser's default outline colour on an element whose outline is `0` or hidden | not a defect |

### Scores (`impeccable audit`, 0–4), before the fixes

| Dimension | Score | Key finding |
|---|---|---|
| Accessibility | 3 | T7-1, the light checked control at 1.32:1. Text is AA everywhere, in both themes |
| Performance | 4 | static pages; one `@import` chain of 27 small files (fine for a mockup; the app will bundle) |
| Theming | 3 | a full two-level token system with a working second theme; T3-1, T4-1, and DESIGN.md silent on light |
| Responsive | — | not scored: desktop first is §3's, and responsive is lesson 10 |
| Implementation integrity | 4 | no literal, no primitive in a component, one source for every value, a deterministic gate for each rule |

## After the fixes

Every check was run again on the rebuilt files:
- **The guards** pass, all ten. Guard 10, new, finds no geometry written as a count outside the skeletons.
- **`check08()`** passes:
  - every role resolves to phase 07's value;
  - every named geometry equals the `calc()` it replaced (a planted error is caught);
  - **62 pairs, all pass in dark and all in light**, the two new T7-1 pairs included.
- **The pixel test** against the goldens:
  - **83 of 83 pages** identical;
  - flow steps: 227 of 241 on the first pass. **The 14 that differ are the two flaky spots seen before any change**
    in this lesson: the run bar's native `select` on loading screens, and the Item sheet, at up to 2/255. A re-run
    moves them between steps.
  - The checkbox's hover edge (T3-1) is the one intended change. No screen is drawn hovered.
- **`/impeccable detect` in the browser**, light: one `design-system-color` is left, I-7, the browser's own outline
  colour. DESIGN.md now names the light palette.

| Dimension | Before | After |
|---|---|---|
| Accessibility | 3 | 4: text AA everywhere in both themes; a checked control at 5.66:1 in light |
| Performance | 4 | 4 |
| Theming | 3 | 4: one name per role, a source on every line, DESIGN.md knows the light theme |
| Responsive | — | — (lesson 10) |
| Implementation integrity | 4 | 4 |
