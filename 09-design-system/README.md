# Phase 09 — Design system

**Opened 2026-11-03** (register Q48), when lesson 08 closed; **D1–D6 are answered as recommended** (see *Decisions*).
The plan below was written 2026-10-29, the day the phase's materials were read: the prompt pack
(`01-prompts.md`, seven steps) and the 21 slides of `lesson-09.pdf`. Both are course material and stay out of the
repo. It is numbered by the course's own seven steps.

**What the phase does.** Phase 08 gave the look an architecture: `tokens.css` on two levels and one file per
component. **But a folder of CSS is not a system.** The next person to open it — the owner a month from now, a
developer at handoff, Claude in a new session — cannot tell which variants of a component exist, when to take one
and not another, or what focus looks like from the keyboard. **This phase turns the files into a product with its
own users:**
- one package with one entry point, `index.css`, which the product consumes;
- **a living showcase**: a page per component, built on the same `index.css` as the screens, so it cannot lie
  about them;
- **four states on every component, in both themes at once**;
- **patterns**: the compositions that already repeat on three screens or more;
- **a rule of growth**: anything new appears in the system first, and on a screen second, never the other way.

**The thesis is the course's: the system is a separate product, and its main feature is a showcase that does not
lie** — because it is the same code as the product.

---

## What is already decided, and must not be re-decided here

- **Dark is the product, and light is a design decision** (§3). The course is light-first with
  `[data-theme="dark"]`; **ours is the mirror**: `:root` is dark, `[data-theme="light"]` overrides roles (§17).
  The course's rule holds as it stands — **a state token with a value in one theme only is a defect** — so every
  state gets a dark value and a light one.
- **The full light theme belongs here** (§1, §15, §16, §17). Four roles still draw dark in light — `--sheet-edge`,
  `--danger`, `--danger-hover`, `--on-danger` — and **signing them is this phase's**, by the owner's word, with the
  contrast measured (D4). **Whether light ships in the product is still the owner's** (Q44).
- **States are this phase's** (§17, lesson 08's plan): hover, focus-visible and disabled moved through lesson 08
  as they were. Their values exist; what does not exist is **a state as a system** — the same rule on every
  component, in both themes, documented.
- **A disabled control takes focus and points at its reason** (§16). That is a signed rule and it outranks the
  course's *disabled removes the cursor*.
- **Colour is a claim** (§15). A new state colour needs a reason in `concept.md` and its contrast in
  `tokens.css`; **AA for text, 3:1 for an edge or a mark, in both themes.**
- **One way in** (§16). The showcase, the screens, `tokens.css` and `components/` are all **generated**. The
  course's *move the files* and *update every wireframe* mean **changes to the generators**:
  `tools/concept_tokens.py`, `tools/build_components.py`, `tools/build_kit.py`, `tools/build_mockups.py`, and the
  guards in `tools/kit_check.py`. A hand edit to a generated file is overwritten by the next build.
- **Every word comes from `microcopy.md`** (§14). A word on a docs page that is not in the table fails the build,
  as it already does on `kit.html` (guard 8).
- **No UI kits, no engine** (§10, Q45). The system stays plain CSS by hand.
- **No pixel moves where nothing was meant to.** The pixel test (`tools/kit_pixel_test.py`) holds every step that
  is not a state or a light value to the goldens.
- **Do not design a screen that only makes sense once an out-of-scope thing exists** (§9), and **invent nothing on
  the receiver's surfaces** (§8, Q20). Both bear on step 6.

## What we have today (measured 2026-10-29)

- **Tokens**: `08-design-tokens/tokens.css`, two levels, 124 primitives (50 colour), 44 roles and 18 recipes, a
  light theme of 46 overrides, 62 contrast pairs per theme, all AA (§17).
- **Components**: `08-design-tokens/components/`, 27 files and `index.css`, cut from **41 components** in
  `07-ui-assembly/ui/inventory.md`.
- **A showcase already exists**: `07-ui-assembly/ui/kit.html` shows **every component in every state it has**, cut
  from the real pages, on the same two files the screens link, with its words checked against `microcopy.md`.
  **It is one long page, not documentation**: it shows *what*, and says nothing about *when*, *instead of what*, or
  *why*. Step 2 builds the second half; it does not start from nothing.
- **States that exist**: four hover recipes (kept apart, Q44 C), `--shadow-focus` on every focusable thing,
  disabled through three colour roles (`--disabled`, `--disabled-text`, `--disabled-edge`). **No pressed (active)
  state is drawn anywhere.**
- **Screens**: 83 dressed pages and 241 flow steps, generated twins of the wireframes (§16).
- **The deploy is Vercel**, by `vercel.json` and the `.vercelignore` allow-list, not GitHub Pages.

## Our mapping of the course's paths

| The course says | Here it is |
|---|---|
| `design-system/` | **`design-system/` at the root** (D1, Q48); this folder keeps the lesson's record |
| `tokens.css`, `components/` *moved* in | `08-design-tokens/tokens.css` and `components/` move, and their generators write the new path. `06-concept/tokens.css` stays: it is the stand's |
| `design-system/index.css` | the one entry point: `@import` of `tokens.css`, then `components/index.css` |
| `wireframes/*.html` switch to one import | `04-wireframes/mockups/` (83) and `mockups/flows/` (241), by `build_mockups.py`; `kit.html` and `shell.html` by `build_kit.py`. **Guard 6 changes from two links to one.** The grey `pages/` link no kit and are not touched |
| `docs/` — a page per component + `index.html` | generated from the same sources `kit.html` is cut from, plus `inventory.md`, `DESIGN.md`, `microcopy.md`, `concept.md`, `06-concept/references.md` (D8) |
| `docs/why.html` | *why the system is like this*: from `concept.md` and `references.md` — the four rounds of directions and the working style, Mica · Lime |
| `--bg-hover`, `--color-focus`, `--opacity-disabled` | our names already exist: the hover recipes, `--focus`, the disabled roles. **No rename for the course's sake** (D3) |
| `patterns/` from `wireframes/*.html` | from the 80 wireframe pages, with `inventory.md` and `sitemap.md` as the index; **a pattern stands on three named screens or it does not exist** |
| *«залишаємо»* leads into the system | §15's *оставляем* rule, re-routed: a value → `tokens.css` at its level; a component → `components/` **and its docs page**; a composition → `patterns/` |
| a new screen in `examples/` | **D6, Q48**: a screen a job asks for, built from the system alone; what is missing goes to `backlog.md` |
| GitHub Pages | **Vercel**, with the docs added to the allow-list (D7) |
| `README.md`, *Design system* | `README.md`, *Design system*, with the showcase's address |

## The steps

| | Step | Out | State |
|---|---|---|---|
| **1** | **One package.** Create the system's folder (D1) with `patterns/`, `docs/`, `examples/`. Move `tokens.css` and `components/` into it — **move, not copy**: the generators write the new path and git keeps the old one. Add `index.css`, which imports both. Every page links **only** `index.css`. Guards re-pointed (6: one link; 4 and 5: the new paths). Pixel test identical on every page, `kit.html`, `shell.html`. | the folder, `index.css`, the generators, `kit_check.py` | **done 2026-11-03** |
| **2** | **Living documentation.** A page per component in `docs/`, plus `index.html` that gathers them, plus `why.html`. Each component page has four parts: **anatomy** (the live component with its parts named), **variants and sizes** (every one `inventory.md` lists, side by side), **when to use** (from `DESIGN.md` and `microcopy.md`: the role it plays), **rule and anti-rule** (a right use, and a case for another component). **Built on `index.css`, never a picture.** Words checked against `microcopy.md`. | `docs/*.html`, a generator in `tools/` | **done 2026-11-03** |
| **3** | **States, in both themes.** Every component gets **hover, active, focus-visible, disabled**, through semantic roles, each with a dark and a light value. **Focus** passes 3:1 against every ground it sits on, in both themes. **Hover and active** change ground, colour or edge, never position or size. **Disabled** per D3. The four light gaps are signed (D4). Each docs page gets a *States* block: all four, dark and light side by side. New pairs join `contrast_pairs()`. | `tokens.css`, `components/`, `docs/`, `concept.md` | **done 2026-11-03** (Q49) |
| **4** | **Patterns from the screens.** Read every wireframe page and find the compositions on **three or more** screens. Each becomes one file in `patterns/`, **made of existing components with no style of its own**. Candidates to test, not to assume: the page head with its actions; an empty or error state with its one action; a row list with the item side panel; the Run stage list ending in Export; a confirmation that names the consequence. A docs page: when to take a pattern, when separate components. | `patterns/`, `docs/patterns.html` | **done 2026-11-03** |
| **5** | **Rules of contribution.** `DESIGN.md` and `CLAUDE.md` gain *Contributing to the system*: **new appears in the system first, on a screen second.** A new component goes to `components/` with its docs page and its states in both themes; a new composition to `patterns/`; a new value to `tokens.css` at its level. §15's *оставляем* rule re-routed into the system. Written so the next session reads it from the repo, not from the chat. | `DESIGN.md`, `CLAUDE.md` §15/§16/§17 and a new §18 | **done 2026-11-03** |
| **6** | **The test of a new screen.** Build a screen the product does not have yet, but a job asks for (D6), **from the system alone**: existing components and patterns, tokens only, no style on the screen. **What is missing is written down, not drawn**: `backlog.md`, honest. The screen stays in `examples/` as a demonstration. **It is not a product decision**: if it is ever wanted in the product, it goes to the register. | `examples/`, `backlog.md` | **done 2026-11-03** |
| **7** | **The check, and the showcase online.** A table of defects — file, element, what is wrong, how to fix: a component that looks different on a screen and on its docs page · a docs page describing a variant or state the code does not have, or the reverse · a state with a value in one theme only · a pattern with styles of its own · a component or token with no docs page. Plus `/impeccable audit`. **The table first; the owner sets priorities; then everything is fixed together.** Every class of defect becomes a guard. The showcase deployed on Vercel; `README.md`, *Design system*, with its address. | `system-check.md`, `kit_check.py`, the deploy | |

**And the lesson's page**, `09-design-system/system.html`, built from a template in `tools/` like every phase
page, with phase 09 linked in every rail and in the viewer, and listed in `.vercelignore`.

## State, 2026-11-03

**Lesson 09 is open. Step 1 is done** (2026-11-03): [`design-system/`](../design-system/README.md) holds `tokens.css`
and `components/`, moved with `git mv` and unchanged to the byte, behind one `index.css` that imports them; every
mockup, flow step, `kit.html` and `shell.html` links it alone; the generators write the new path; guards 4, 5 and 6
are re-pointed, and guard 6 also refuses the files coming back to `08-design-tokens/`. **Pixel test: 83 of 83 pages,
`kit.html` and `shell.html` identical; 235 of 241 flow steps**, the six others a 3 × 28 px spinner spot at up to
2/255 that differs at HEAD too. `patterns/`, `examples/` and `backlog.md` stand empty for their steps.

**Step 2 is done** (2026-11-03): [`design-system/docs/`](../design-system/docs/index.html), built by
`tools/build_docs.py`. **46 component pages** — the kit's 41 and its five one-offs — each with anatomy (the live
specimen, its parts numbered by selector and checked in a browser), every variant and state the kit shows (114 in
all), when to use, rule and anti-rule with a link to the other component; **`index.html`**, the showcase, every
component with a live preview; **`why.html`**, from `concept.md` and `references.md` (D8), its specimens live. The
specimens are `build_kit.components()`'s own, so the docs and `kit.html` cannot disagree; the words the docs say are
`tools/docs_content.py`. Guard 11 checks every component has a page linking `index.css` alone. **Found on the way: the
five one-offs on `kit.html` had no specimens** — their first state landed in the unused *painted* argument of
`comp()` and was dropped since lesson 07. Fixed; `kit.html` now shows them. **D2:** the docs now cover every component
and state of `kit.html`; its retirement, with a redirect and guard 8 moved, waits for step 7's check. D1–D6 were answered by the owner in one word, *as recommended* (Q48).
D4 and D5 answered the **procedure**: the four light values and the pressed recipes are still proposed by the model
and signed by the owner one by one. D7 and D8 stand as recommended defaults. **Q44 — whether light ships — is still
the owner's.** **Step 3 is done** (2026-11-03); its values were **signed by the owner the same day (Q49)**. Pressed on every
control through nine new recipes in `tokens.css` (`--action-active`, `--control-active`, `--row-active`,
`--segment-active`, `--wash-active`, `--danger-active`, `--warning-active`, `--problem-active`, `--edge-active`), each over a
role and so in both themes; disabled through the three roles on every control (D3: no opacity token), with
`cursor: not-allowed`; focus measured 3:1 on every ground in both themes (10 new pairs, lowest 4.67 in light); the four
light gaps filled as proposals (D4). Contrast: **83 pairs per theme, all pass**. A `[data-theme="dark"]` block lets a dark
specimen stand on a light page. Every docs page has a *States* block — rest, hover, active, focus-visible, disabled, dark
and light — and the build checks in a browser that every state drawn differs from rest and changes nothing's size.
Pixel test: 83/83 pages, kit and shell identical; flows 235/241, the known spinner spot. **Found:** in light, a disabled
field is white (`--disabled` takes the slice's light control), brighter than a field at rest — a question for the light
theme, not changed here.

**Step 4 is done** (2026-11-03): six patterns in [`design-system/patterns/`](../design-system/patterns/README.md), built by
`tools/build_patterns.py`. Each has a signature run over all 80 wireframe pages; a screen counts once, an overlay never
counts, and the build fails below three. **Browse head** (Projects, My library, Public library), **Set with an item side
panel** (Project, Configuring, Detached row), **Configuring layout** (Configuring, Detached row, Project), **Run report**
(the four Runs), **Confirmation** (My library, Project, Projects, Run project), **Dialog with a field** (My library, Project,
Detached row). Each file is cut from a real page, links `index.css` alone and holds no style. Looked at and refused, with
the count: kind tabs over a row list (two places — the overlays draw My library), the receiver's aside (two), a sheet
(one), and four that repeat often but are one component each. [`docs/patterns.html`](../design-system/docs/patterns.html):
when the pattern, when the components; the patterns shown in frames of their own files. Guard 12.

**Step 5 is done** (2026-11-03): the rule of contribution, **new appears in the system first, on a screen second**,
is `CLAUDE.md` §18 and `DESIGN.md`, *Contributing to the system*. It holds a table of where each new thing enters (a
value, a component, a composition, a screen), the generator that writes it, what it must bring with it, and the guard
that refuses it. §15's *оставляем* rule is re-routed into the system: a value goes to its token, a component to
`components/` **and its docs page**, a composition to `patterns/`. The rule is also in the code, so a session reads it
from the repo. `concept_tokens.py` now **fails** on a role with no light value or a pair under its bar; until now it
only printed them. `build_docs` fails on a component with neither a States spec nor a reason in `STATIC`. Every
refusal of `kit_check.py`, `build_docs` and `build_patterns` names §18. `design-system/README.md` and `backlog.md` say
the same.

**Step 6 is done** (2026-11-03). The owner picked **EJ-3** from the candidates (D6): *stop suspecting that half of
what I keep is dead weight*. It is importance 3 for the primary persona, and lesson 03's matrix gave it only partial ticks.
Refused as candidates: SJ-2/H-J6 (§9), H-J5 (Q12), H-J4 (it is already drawn, and one of its surfaces is the receiver's),
H-J2 (Duplicate exists, and the evidence is `[?]`). The screen is
[*Usage of My library*](../design-system/examples/usage.html): every item grouped by how many projects use it, with the
projects named, what requires it and when it was last exported. Deleting one item used nowhere goes through the
Confirmation pattern. It is built by `tools/build_examples.py` from two patterns and ten components, with 0 lines of
style and 0 classes of its own, in both themes. It stops at §5's ceiling: *is it used*, never *is it any good*.
**[`backlog.md`](../design-system/backlog.md), four orders, none drawn:**
- B1, a link inside a meta line with no rest state (measured);
- B2, a disclosure;
- B3, a count beside a Small heading;
- B4, bulk selection, which is a register question first.

Three findings are not system gaps and go elsewhere: the entry point, Delete on a row, and the words. Guard 13 refuses a
style, a class of its own or a missing *Example* label in `examples/`. It was negative-tested.

**A second test, the same day, on the owner's word that the first was too familiar**:
[*Copies of code-style*](../design-system/examples/copies.html), for RJ-3 and H-J3. It shows the original beside its copy in
each project, which fields differ, the original folded under Library version, Reset and Promote, and Dialog with a field
for the promote. Four more entries:
- **B5, a defect.** The neutral Callout's tone is guessed by `transform` from its first words, so a new blast-radius
  sentence came out rose. It goes to step 7's table.
- B6, a comparison across copies.
- B7, changed lines marked in a File block.
- B8, a File block that wraps.

B2 was corrected: the system has two single-purpose expansions, neither a group fold.

Next: step 7, the check and the showcase online. B5 enters its defect table.

## Decisions — answered 2026-11-03 (Q48), D1–D6 as recommended


- **D1 · Where the system lives.** *Answered: `design-system/` at the root.* The repo is one folder per lesson (§13), but the system is not a lesson's
  record: lessons 10–12 grow it, and the app will consume it. **Recommended:** the package at the root,
  `design-system/`, as the one named exception to one-folder-per-lesson; **this folder keeps the lesson's record**
  — the plan, the check, the backlog, the page. The alternative is `09-design-system/design-system/`, which keeps
  the rule and puts a lesson number in every import path the product will ever have.
- **D2 · `kit.html` and the docs.** *Answered: the docs become the showcase, `kit.html` retires.* Both would show every component. **Recommended:** `docs/index.html` becomes
  the showcase and **`kit.html` is retired once the docs cover every component and state**, with a redirect from
  its address; guard 8 moves to the docs. Until then both are built from one source, so they cannot disagree.
- **D3 · Disabled.** *Answered: the roles stay, no opacity token.* The course dims with `--opacity-disabled`. **We have three signed colour roles**, and a rule
  that a disabled control keeps focus and points at its reason (§16). Opacity would also dim the reason it points
  at. **Recommended:** keep the roles, add no opacity token, and document the rule on every page that has a
  disabled state.
- **D4 · The four light gaps.** *Answered: the model proposes, the owner signs each.* `--sheet-edge`, `--danger`, `--danger-hover`, `--on-danger`. **Recommended:** the
  model proposes values with measured contrast and the reasoning; **the owner signs each one** in `concept.md`
  before it is written. white on `--danger` already reads 4.77:1 in light, so that gap may be a signature rather than
  a new value.
- **D5 · Active (pressed).** *Answered: one recipe per ground, signed on the showcase.* No screen draws it, so its values do not exist. **Recommended:** one recipe per ground,
  half a step past hover, with no movement and no size change, proposed on the showcase and signed by the owner.
- **D6 · Which screen the test builds.** *Answered: the owner picks from the matrix's candidates.* The course's example is *my saved listings*. Ours must answer a job in
  `jtbd.md` that **no screen answers yet**, must not need anything §9 refuses, and must not be a receiver surface
  (Q20). **Recommended:** the owner picks from candidates the model reads off lesson 03's traceability matrix — a
  job with evidence and a blank row — and the screen is labelled *an example, not in the product*.
- **D7 · Where the showcase is served.** *The recommendation is the default, taken in step 7.* **Recommended:** Vercel, as every phase page is: the system's `docs/`
  added to the allow-list, with a stable address. Not GitHub Pages: two hosts for one site is two places to drift.
- **D8 · `references.md`.** *The recommendation is the default, taken in step 2.* The course reads it for `why.html`. Ours is `06-concept/references.md` with
  `06-concept/refs/`. **Recommended:** read from there; nothing is copied.

## Traps, the course's five and ours

1. **A copy of the kit with no rules.** The files move into `design-system/` and nothing else changes; a week
   later styles grow on screens again. **A system without a rule of growth is a folder with a new name.**
2. **Docs apart from the code.** A docs page with a picture of a component, or a copy of its CSS, starts lying
   the day the product changes. **A docs page pulls the same `index.css`, or it is dead.**
3. **States without the other theme.** Focus with a value in one theme only. **Every state token, twice.**
4. **Patterns from a textbook.** A *card grid* the product does not have. **A pattern is the one you can find on
   three screens.**
5. **No new-screen test.** The system is called finished without one screen built from it alone. **A new screen
   finds the holes.**
6. **Ours: editing a generated file.** Every docs page, every screen, `tokens.css` and `components/` are built.
7. **Ours: renaming for the course's sake.** `--bg-hover`, `--color-focus` are the course's names. Ours are signed
   and guarded (Q47). A state token is named in our scheme or not at all.
8. **Ours: the example screen as a product decision.** `examples/` demonstrates the system. Whether the product
   ever has that screen is a register question, and the screen must not slip into the viewer's product groups.

## Done means

- The system's folder exists (D1) with `tokens.css`, `components/`, `patterns/`, `docs/`, `examples/`,
  `index.css`, `backlog.md`. `08-design-tokens/` holds the record, not the files. Every page links `index.css`
  alone, and the pixel test is identical.
- `docs/`: a page per component with anatomy, variants, when to use, rule and anti-rule, and states in both
  themes; `index.html`; `why.html`; a page of patterns. **Built on `index.css`**, words from `microcopy.md`.
- Every component has hover, active, focus-visible and disabled, with **a dark and a light value for every state
  token**, and focus passing 3:1 on every ground in both themes. The four light gaps are signed.
- `patterns/` holds only compositions named on three screens, with no style of their own.
- `DESIGN.md` and `CLAUDE.md` carry the rule of contribution, and *оставляем* leads into the system.
- One screen in `examples/` built from the system alone, and `backlog.md` listing what it lacked.
- The defect table with a disposition per row; every class of defect a guard in `kit_check.py`.
- The showcase online, `README.md` *Design system* pointing at it, and the phase page built and served.
