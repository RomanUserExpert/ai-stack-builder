# Phase 08 — Design tokens

**A plan, not a result.** Written 2026-10-28, the day the phase's materials were read: the course overview, the prompt
pack, the homework, the 21 slides, and the recorded session of 2026-10-16 (transcribed locally, nothing sent out; the
transcript stays out of the repo because it is course material). It is numbered by the course's own six steps, plus one
step of ours, **7**, which `CLAUDE.md` owes this lesson and the course does not mention.

**What the phase does.** Phase 07 dressed every screen from one flat file, `07-ui-assembly/ui/kit.css`. Its `:root`
holds 110 variables, and each one knows its value but not whether that value is **a colour or a role**. This phase puts
**a layer of roles** between the value and the component. The flat kit splits into two parts:
- **`tokens.css`**, on two levels:
  - **primitive** holds the raw values, colour and geometry;
  - **semantic** holds the colour roles, each one commented with the uses it grew from.
- **`components/`**, one file per component plus `index.css`.

**A component reads colour only through a role, and reads geometry straight from a primitive.**

**The thesis is the course's: the same look, a new architecture.** This is a refactoring, not a redesign, and its test
is that **no screen moves by a pixel**. No value is invented. Every role is **read off real uses**, never taken from
somebody else's design system. Then **one theme proves the architecture**. It overrides only semantic tokens. If it
needs a change in `components/`, that change is a hole in the architecture, and the theme exists to find it.

---

## What is already decided, and must not be re-decided here

- **Dark from day one; light is a design decision, not an inversion** (§3). So **our stress test is the light theme,
  not the dark one.** The course's demo is light-first and proves itself with dark. We are the mirror image.
- **The light theme is not invented here either.** `06-concept/tokens.css` already has a signed light slice for 27
  colour variables, and `tools/contrast.py` measures 60 pairs in each theme. **The full light theme is lesson 09**
  (§1, §15). The stress test applies the slice we have, then lists every variable that the slice does not cover.
  **Those gaps are a finding, not a licence to invent values** (see *Decisions owed*, D1).
- **Every value has a reason in `concept.md`, and colour is a claim** (§15). A primitive takes over its value's
  signature. A semantic token's comment also has to name **the uses it grew from**, in the course's words.
- **One way in** (§16). `tokens.css` and the kit are **generated**, and so are the 83 pages and 241 flow steps. **The
  course's "move the classes" and "switch the screens" mean changes to the generators**:
  - `tools/concept_tokens.py`;
  - `tools/build_kit.py`;
  - `tools/build_mockups.py`;
  - the guards in `tools/kit_check.py`.

  They are never hand edits. A mockup edited by hand is overwritten by the next build.
- **The guards are scripts, not judgement.** The recording says it outright: whether a primitive colour has slipped
  into a component is checked by **a deterministic gate, not by the model**. `kit_check.py` is that gate, and this
  phase gives it new rules (step 6).
- **The pixel goldens exist.** All 83 pages were saved after Q43, by `tools/kit_pixel_test.py`. They are not in the
  repo but in the 2026-10-19 session's scratchpad. **Step 4 is held to them.**
- **States are lesson 09.** Hover, focus-visible and disabled are not redone here. Our tokens already carry hover
  values and `--shadow-focus`, so **those keep their values and move as they are**: no new state role is added.
- **The styling engine, Q6, is decided in this lesson, on two built components** (§10, §12). The course says nothing
  about it. That is step 7.

## What the kit looks like today (measured 2026-10-28)

- **110 variables** in the kit's `:root`, mirrored character for character from `tokens.css` (guard 5). **28 of them
  are hex colours, and they hold 25 distinct values.**
- **Our names are already roles.** `--ground`, `--cutout`, `--problem`, `--on-lime` and `--lime-mark` say what a
  colour is *for*. **What we lack is the level below**: there is no palette of raw values. So this phase **adds a
  floor under the names, not a ceiling over them.** Most semantic tokens will keep the name they have, and most
  classes will not change a character.
- **Three pairs already share one value under two names**:
  - `--text-2` and `--checked`, `#C5C7BE`;
  - `--text-3` and `--skipped`, `#A1A49A`;
  - `--lime` and `--lime-mark`, `#C6EF5A`.

  These are the course's *two roles, two tokens* rule, met by accident. **The light slice proves the third**: there,
  `--lime-mark` is `#55700F` and `--lime` stays `#C6EF5A`.
- **Literal colours live inside composite tokens**: 9 `rgba()` values in the shadows, the acrylic, the veil and the
  edges. This is the course's finding type 3 (*a value bypassing a variable*). Ours sit in the tokens, not in the
  classes, because guard 1 has kept the classes clean since phase 07.
- **Two variables are declared and never read**: `--canvas` and `--measure-wide`.
- **The light slice is not in the kit at all.** `kit.css` copies only the dark `:root`, so no screen has ever been
  drawn light.

## Our mapping of the course's paths

| The course says | Here it is |
|---|---|
| `ui/kit.css` | `07-ui-assembly/ui/kit.css`, generated by `tools/build_kit.py` |
| `tokens-audit.md` | `08-design-tokens/tokens-audit.md` |
| `tokens.css` in the root | `08-design-tokens/tokens.css`, generated (see D3) |
| `components/` + `index.css` | `08-design-tokens/components/`, generated by `build_kit.py` from the same sources as today |
| `ui/kit.html`, `ui/shell.html` | `07-ui-assembly/ui/kit.html`, `shell.html`; they switch from `kit.css` to the two new files |
| `wireframes/*.html` | `04-wireframes/mockups/*.html` (83 pages) and `mockups/flows/` (241 steps), all generated. **The grey wireframes in `pages/` are not touched**: they link no kit |
| subagents by role to switch the screens | **not needed**: one build switches every screen. Subagents return in step 6, as review lenses |
| three control screens | **every page**, against the goldens, plus `kit.html`, `shell.html` and a sample of flow steps |
| the theme switch in the navigation | **see D2**: on our side this is a product control, and a product control goes through the register |
| `CLAUDE.md` «Токени», `README.md` «Tokens» | a new **§17 Tokens**, and §15 and §16 rewritten where they route a value; `README.md`, *Tokens* |
| `/impeccable audit` | the same skill, as in phase 07's step 9 |

## The steps

| | Step | Out | State |
|---|---|---|---|
| **1** | **Audit the kit.** Every variable: its value, every class and page that reads it, and the role it plays in each place. Three kinds of finding: drift, one variable carrying several roles, and a value bypassing a variable. At the bottom, the candidate roles, each with its addresses. **Nothing is fixed or renamed.** | `tokens-audit.md` | |
| **2** | **`tokens.css` on two levels.** **Primitive**: every raw value from the kit and the light slice, colour and geometry, with drift merged and marked. **Semantic**: the colour roles from the audit, each one a `var()` to a primitive with a comment naming its uses. Names come from the audit and `concept.md`. A colour that stands in exactly one class is not a role; it is flagged for step 6. **Nothing new.** | `tokens.css`, `tools/concept_tokens.py` | |
| **3** | **The classes into `components/`.** One file per component, by `ui/inventory.md`'s 41 components, plus `index.css`. Colour only through semantic, geometry from primitive, no literal. Markup unchanged. `kit.html` switches over; **`kit.css` stays for the comparison.** | `components/`, `tools/build_kit.py` | |
| **4** | **The screens onto the new files.** `build_mockups.py` links `tokens.css` + `components/index.css`. **Pixel test** on all 83 pages, `kit.html`, `shell.html` and a flow sample, against the goldens. A difference is a defect in the tokens or a component, never in a screen. Then `kit.css` is deleted, and the guards that named it are rewritten. | the same mockups | |
| **5** | **The stress test: light.** `[data-theme="light"]` overrides **only semantic tokens**, with the signed light values. The switch goes where D2 decides. Contrast for every light pair, written as a comment and measured by `contrast.py`. Anything that needed `components/` is a hole: find it and route it through a role. **Whether light stays in the product is the owner's decision, taken after looking.** The *оставляем* rule in `CLAUDE.md` now routes a value into the token of its level. | `tokens.css`, the switch, `CLAUDE.md` §15/§16 | |
| **6** | **The check and the close.** A table of defects: a hex colour outside primitive · a component reading a colour primitive · two names for one role · a semantic token with no source comment · geometry written as a number · a page still on `kit.css` · contrast below AA in either theme. **Every class of defect becomes a rule in `kit_check.py`**, so it cannot come back. Plus the `/impeccable audit` findings. **The table first; the owner sets priorities; then everything is fixed together.** | `tokens-check.md`, `kit_check.py` | |
| **7** | **Ours: Q6, the styling engine.** Two built components, the button and the project row, are read against §10's criterion: **tokens and two themes first-class, and no utility classes pushed into components that are the product's value.** The candidates are Tailwind, CSS Modules and vanilla-extract. The finding is put to the owner and the answer goes into the register. **No app is scaffolded** (§13). | a register entry, `CLAUDE.md` §10 | |

**And the lesson's page**, `08-design-tokens/tokens.html`, built from a template in `tools/` like every phase page, with
phase 08 linked in every rail and the page listed in `.vercelignore`.

## State, 2026-10-28

**Steps 1–6 are done.** Step 7 (Q6, the styling engine) is owed, and so is the lesson's page.
- **1. The audit**, [`tokens-audit.md`](tokens-audit.md). Two of its counts were corrected later: `--canvas` and
  `--measure-wide` are read by the showcase, and the light slice has 28 entries.
- **2. [`tokens.css`](tokens.css)** on two levels.
- **3. [`components/`](components/)**, 27 files.
- **4. Every screen moved**, with `kit.css` deleted. 83 of 83 pages and 241 of 241 steps match their goldens. The
  only differences are two flaky spots seen before the change.
- **5. The light theme**, by semantic overrides only: no component file touched. Its switch is in the viewer and on
  `kit.html`.
- **6. [`tokens-check.md`](tokens-check.md)**: every defect has a disposition, and the fixes are in.

The owner's answers are register entry **Q44**: A, B, C, D3 and D4 as recommended, plus the light glass and
shadow. **Still the owner's:** whether light ships, and the light values of `--sheet-edge` and Remove Red.

## Decisions owed — the owner's, before or during the steps

- **D1 · What the light stress test may use.** The signed slice covers 27 colour variables. The materials, shadows,
  `--danger`, `--on-danger` and the washes have no light value of their own, and the washes recompute from their base.
  Under the rule *nothing new*, they **inherit their dark value**, and the stress test shows the result as it is.
  **Recommended:** run it that way and list the gaps as findings. Each gap is then filled in lesson 09 or by the
  owner's word, **never by the model in the middle of a refactor**.
- **D2 · Where the theme switch goes.** The course puts it in the product's top bar. For us, that is **a new control on
  every screen**: structure in 83 wireframe pages, a new line in `microcopy.md`, and an entry in the register. It is
  also for a theme whose future is undecided. **Recommended:** put the switch in **the viewer's toolbar**, beside
  *Wireframe / Design*, and on `kit.html`. It then reaches every real screen without changing the product. If the owner
  keeps light, the product's own control comes through the register as a decision rather than as a by-product of a
  test.
- **D3 · Where the values live.** Today `06-concept/tokens.css` is the only source, and the stand, `style.html` and
  `ui.html` read it. **Recommended:** `tools/concept_tokens.py` stays the one place a value is written. It emits **both**
  files: phase 06's flat file, unchanged so the stand stays as it was signed, and phase 08's two-level file. One source,
  so no drift. §13's line *every value comes from `06-concept/tokens.css`* is then reworded.
- **D4 · How primitives are named.** The instructor argued with the model's `green`/`red` names on the recording.
  **Recommended:** hue plus step, from the style's own words: `--mica-950 … --mica-50`, `--lime-400`, `--rose-300`,
  `--amber-300` and the like. They are names of what a value **is**. Every name that says what it is **for** stays on
  the semantic level.
- **D5 · `--canvas` and `--measure-wide`, declared and unused.** **Recommended:** keep them in primitive if `concept.md`
  signs them, otherwise drop them. The audit says which.

## Traps, the course's four and ours

1. **Roles out of somebody's head.** A semantic token with no addresses is thrown out.
2. **"Fixed it while I was there."** No shade or radius changes during the refactor. A visual change waits for the end
   and goes through *оставляем*.
3. **A token for everything.** A one-off value does not become a role. Geometry never gets a semantic level.
4. **A theme made of component edits.** The theme lives in `tokens.css` and overrides semantic tokens only.
5. **Ours: editing a generated file.** `kit.css`, `components/`, the mockups and `tokens.css` are all built. A hand
   edit lasts until the next build and then the drift is invisible.
6. **Ours: the composite tokens.** A shadow or an acrylic built from `rgba()` is a role made of literals. Its colours
   go into primitive. The composite stays a semantic token, because the light theme has to redefine it (D1).

## Done means

- `tokens-audit.md`: every variable of the kit with its uses; drift and bypassing values found; roles with addresses.
- `tokens.css`: two levels; every semantic token is a `var()` to a primitive with its source comment; no value that was
  not in the kit or the signed light slice, except merged drift, which is marked.
- `components/`: a file per component plus `index.css`. No literal in a class, and no colour primitive read by a
  component. Geometry from primitive.
- The guards in `kit_check.py` enforce every line above, and pass.
- All 83 pages and 241 steps link `tokens.css` + `components/index.css`. `kit.css` is deleted. **The pixel test is
  identical** (±1/255) against the post-Q43 goldens.
- Light works by the switch on any screen, by semantic overrides alone. Contrast in both themes is in `tokens.css`
  and `contrast.md`. Whether light stays is the owner's decision, recorded in the register.
- Q6 is answered, or deferred with a reason, in the register.
- `CLAUDE.md` (§1, §13, §15, §16, a new §17 *Tokens*) and `README.md` (*Tokens*) know about the tokens. The phase page
  is built and served.
