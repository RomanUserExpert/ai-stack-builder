# Phase 07 — UI assembly

**What this phase does.** Every screen of the product is dressed in the working style, Mica · Lime (§15), as a
generated twin of its wireframe. The wireframes stay as they are. The **Wireframe / Design** switch in
[the viewer](../04-wireframes/pages/wireframes.html) moves between the two.

Steps 1–6 are done:
- **1.** `DESIGN.md` at the root;
- **2.** [`ui/inventory.md`](ui/inventory.md);
- **3.** the kit: [`ui/kit.css`](ui/kit.css), [`ui/kit.html`](ui/kit.html), [`ui/shell.html`](ui/shell.html);
- **5.** group 2 dressed;
- **6.** [`ui/critique.md`](ui/critique.md), with its fixes.

Step 4, the product's own visuals, was skipped by the owner. **This file is the plan for the rest: dressing all
80 pages, then a review, then the fixes.** It was written 2026-10-19.

---

## 1. The pipeline: one way in, so nothing drifts

*Since lesson 08 (2026-10-28) `kit.css` is gone: the values are in `08-design-tokens/tokens.css`, the classes in
`08-design-tokens/components/`, and the guards point at them (CLAUDE.md §16–17). This section is the record of lesson 07.*

```
06-concept/tokens.css   ← tools/concept_tokens.py      every value, the only place a value is written
        │ copied (dark, used vars only)
07-ui-assembly/ui/kit.css ← tools/build_kit.py          :root + the classes (MOCK_CSS + KIT_CSS + skeleton sizes)
        │ linked, alone
04-wireframes/pages/*.html → tools/build_mockups.py → 04-wireframes/mockups/*.html   (and every flow step)
   structure + words            transform: icons, portrait, tones, shell, one primary, state classes
        │
04-wireframes/prototypes/*/ (tools/prototypes/build_*.py) → mockups/flows/*/
```

**Where a change goes, and where it never goes:**

| Change | Goes into | Never into |
|---|---|---|
| A value: colour, size, radius, motion | `tools/concept_tokens.py` → `tokens.css`, signed in `concept.md` | `kit.css`, a page, a `style=` |
| How a component looks | `MOCK_CSS` (painted) or `KIT_CSS` (added in phase 07), signed in `DESIGN.md` | a mockup page |
| A tone the structure cannot carry: danger, warning, a demoted primary, a state class | `build_mockups.transform` | a wireframe class added only for looks |
| Structure: an element, an attribute, a state | the wireframe page (the spec), then rebuild | the mockup |
| A word | `microcopy.md` + the page, together (§14) | the mockup, the kit |
| A new component | `kit.css` **and** `kit.html` **and** `inventory.md` first, then the screens | one screen alone |

**The owner's *оставляем*** (CLAUDE.md §15) is the same row as *how a component looks*. It goes into the kit, is
signed in `DESIGN.md`, and reaches every screen where the component stands.

## 2. The guards: run on every build, and they stop it

`tools/kit_check.py` runs at the end of `build_mockups.py` and fails the build on any of these:

1. **No value outside a variable.** No hex, `rgb()`, `px` or font name in the classes of `kit.css` (`concept_ui.literals`).
2. **No style on a screen.** No `style=` attribute and no `<style>` element in any mockup or flow step.
3. **Every class is the kit's.** Every class on a dressed page is defined in `kit.css`, except a short, named list:
   - utilities the markup carries for meaning: `visually-hidden`, `product-page`, `image`;
   - the wireframe frame: `wf-*`, `device`.
4. **Every variable is defined.** Every `var(--x)` in `kit.css` is declared in its `:root`.
5. **The kit mirrors the tokens.** Every `:root` value in `kit.css` equals its `tokens.css` value, character for
   character.
6. **The stylesheet is the kit's.** Every mockup links exactly one stylesheet, `kit.css`, plus the Geist font.
   There is no `tokens.css` and no `wireframe.css`.
7. **One primary.** No dressed page has more than one `button-primary`.
8. **The words are the product's.** The showcase's words are in `microcopy.md`, as `build_kit.py` already checks.
   On a screen they stay the wireframe's own, by construction.
9. **Coverage.** The check reports how many of the wireframe pages, and how many flow steps, have a twin.

A mockup is never edited by hand, because the next build would overwrite it.

## 3. The order of work

| | Batch | Pages | New in the kit |
|---|---|---|---|
| **A** | 0 · The door: Sign in, Create account, Reset password | 8 | — (`door`, `field` exist) |
| **B** | 1 · What I keep: My library, Public library, Import/export, the Item overlay | 20 | the Item sheet: `sheet`, `form-section`, `field-row`, `file-list`, `dropzone`, `attach` |
| **C** | 3 · What leaves: Run for a single item, a shared project, a shared item | 12 | — |
| **D** | 4 · What somebody else opens: Shared project, Shared item | 6 | `heading-small` |
| **E** | every flow step of the 37 clickable cases | 241 | — |

Each batch follows the same steps:
1. new components go into the kit;
2. the pages are added to `PAGES`;
3. the build runs, and the guards must pass;
4. every page is screenshotted and looked at;
5. the painted screens are checked against their goldens. A painted screen must not move unless the batch meant it
   to.

## 4. The review

**A detailed review, read-only, runs once every page is dressed.** Parallel sub-agents cover four lenses:
- **0+1** (door, library, item);
- **3+4** (every Run, the shared surfaces);
- **the flows**;
- **the binding** of the kit. This lens checks every value in `kit.css` and `tokens.css` against `DESIGN.md` and
  `concept.md`, every `var()` against its declaration, every component on `kit.html` against `inventory.md`, and
  every class on a page against the kit.

Their findings go into one table in [`ui/review.md`](ui/review.md).

## 5. The fixes

Each finding goes by the table in §1.

## State, 2026-10-19

**Steps 7 and 8 are done.** All 83 pages and 241 flow steps are dressed, and the guards pass. The review
([`ui/review.md`](ui/review.md)) has 76 findings, each with a disposition: 54 fixed, 3 fixed in part, 19 declined with the reason.
One of the declined is a question for the owner. The goldens were re-saved after the fixes.

**Step 9, the audit, is done** ([`ui/audit.md`](ui/audit.md)). Every screen was checked against the kit, DESIGN.md and
microcopy.md, and the `impeccable audit` detector ran on all of them. It found 3 real markup inconsistencies (the page
head, the state tile, and code inside a button at 1.2:1), one heading level skipped across about 120 pages, and 2
tooltips missing from the table. All of them are fixed. The re-run shows 0 contrast failures, 0 lines outside
microcopy.md, 0 pages whose words differ from their wireframe, and 0 icons outside Lucide.

**The phase page is [`ui.html`](ui.html)** (2026-10-23), built by `tools/build_ui_page.py` from `tools/ui-page.tpl.html`
like the pages of phases 01–06. It embeds the kit, the shell and a Wireframe / Design switch over eight screens, and
reads its counts from `kit.css`, the mockups and `contrast.md` at build time. Phase 07 is a link on every phase rail.

## Closed, 2026-10-28

**The lesson is closed.** Every line of *Done means* below holds. Left open on purpose: whether a shared link can be
replaced by a new one without stopping the share (register, Q43). The light theme is lesson 09, responsive 10, motion 11.

## 6. Done means

- 83 of 83 wireframe pages and every flow step have a dressed twin.
- The guards pass, and the goldens are re-saved.
- `review.md` has a disposition for every row.
- `DESIGN.md`, `inventory.md`, `kit.html` and the register agree.
