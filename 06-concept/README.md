# Phase 06 — Concept

**A plan, not a result.** Written 2026-10-05, the day the phase's materials were read: the course
overview, the prompt pack, the homework, the 22 slides, and the recorded session. It is numbered by
the course's own seven stages from the start, as phase 05 was.

**What the phase does.** The product has a structure (phase 04) and a voice (phase 05). **Now it gets
a look**: a palette, type, form, iconography. It is derived from the same data the voice came from,
plus real references from the market and the owner's **written-down taste**. **It is proved on two
screens, not painted across the product.** The result is a found and tested visual language on a
main screen and a contrasting one. Documenting it (`DESIGN.md`) is phase 07, and so is rolling it out.

**The thesis is the course's, and it is the same discipline as phase 05: a reference is input, never
output.** One reference is the base, and one or two named devices are taken from the others. Every
colour, radius and font has a reason: an attribute derived from the data, or a line of the owner's
taste. *A decision with neither is the model's default, not a decision.* There are two defaults to
refuse. The universal one is a blue-violet gradient, glass cards and icons in circles. The category
one is the palette you could guess from the product's subject before seeing anything.

---

## What is already decided, and must not be re-decided here

`CLAUDE.md` fixed several things about the look long before this phase existed. Stage 2 starts from
them and cites them:

- **Dark theme from day one; light is a design decision, not a colour inversion** (§3). So the course's
  *light or dark* axis is **not free** for the three directions. Each direction is drawn dark-first,
  and the directions differ on the other axes: how much colour, the character of the type, the form.
  *Whether a direction shows its light theme at all in this phase is a decision owed (below).*
- **The audience lives in Linear, Vercel, Raycast and Figma. The bar for craft is high, and generic
  dashboard aesthetics read as cheap** (§3). This is data about the persona, not the owner's taste, and
  stage 2 treats it that way.
- **No UI kits. The design system is custom and is part of the product's value** (§10). The look is
  built, not borrowed.
- **The styling engine is decided in phase 08, on two built components** (§10). The course's
  `concept/tokens.css` is plain CSS custom properties, which every candidate engine (Tailwind, CSS
  Modules, vanilla-extract) can read. **It does not decide the engine.** It is the one file the two
  screens take their values from, and phase 08 formalises it.
- **Nothing the product draws may claim what it does not know.** No score, rating or badge (§5). A
  bare green tick is the unearned verdict (§6). `Skipped` has its own **neutral** glyph: not a green
  tick it did not earn, and not a red one it does not deserve. **Colour is a claim, and this is where
  it is held to the same rule as words.** The three severities need three treatments: *Problem*,
  *Note*, *Skipped*. A clean result is *checked* and never *works*.
- **The voice** (`05-tone-of-voice/voice.md`, `CLAUDE.md` §14). An error must not look festive, and a
  warning must not be invisible. That is the course's step-7 check, and our five principles already
  say why.

**And the evidence is partly gathered.** The course's stage 1 searches for *the benchmark of trust
that research already named*. Ours named it in phase 01: the **aspirational craft benchmark** is
Linear, Vercel, Raycast, Stripe and GitHub. There is also a folder of dark design language waiting
since stage 2:
[`01-research/2-flows/10-dark-design-language/`](../01-research/2-flows/10-dark-design-language/), with
Linear's dark theme at close range (two greys and a hairline instead of a shadow stack; hierarchy by
weight and dimming, colour reserved for meaning; key caps as a first-class component) and Vercel's
Geist grid, materials and type. **No new competitor search is made.**

---

## Our mapping of the course's paths

| The course says | Here it is |
|---|---|
| `concept/references.md`, `concept/directions.html`, `concept/tokens.css` | `06-concept/references.md`, `06-concept/directions.html`, `06-concept/tokens.css` |
| `concept.md`, `concept.html` | `06-concept/concept.md`, `06-concept/concept.html` |
| `wireframes/listings.html` (the main screen, dense) | **to be chosen**: see *Decisions owed*, recommended `04-wireframes/pages/library-my-*.html` |
| `wireframes/my-profile-seeker.html` (the contrasting screen, sparse) | **to be chosen**: recommended `04-wireframes/pages/run-*.html` |
| `research.md`, `personas.md`, `jtbd.md`, `voice.md` | `01-research/research.md`, `02-personas-jtbd/6-personas/personas.md`, `02-personas-jtbd/7-jobs-to-be-done/jtbd.md`, `05-tone-of-voice/voice.md` |
| the old `DESIGN.md` that leaks its palette | **There is no `DESIGN.md`**, but the leak exists. The phase pages' tokens (`tools/research-page.tpl.html`: paper ground, accent `#e05f03`) and the grey wireframe sheet (`04-wireframes/pages/wireframe.css`) are the two places a model would quietly take a palette from. **Neither is the product's**, and stage 3 says so before drawing |
| photos from Unsplash on every card | **Our content has no photographs.** It is skills, agents, MCP servers, file trees, code and refs. See *What does not transfer* |
| Solar icons, one style | Solar, one style: linear, bold or bold-duotone, chosen with the direction |

**The pages are rewritten in place, and the prototypes are rebuilt from them**, as in phase 05. The
239 prototype pages in `04-wireframes/prototypes/` are generated from `pages/` by
`tools/prototypes/`. **Painting a page means the prototypes repaint on the next build**, which is the
point. Their screens use the same `wireframe.css`, so *rolling the language out to every page* has to
be stopped here on purpose: the course paints **exactly two** screens.

**Copy and structure do not change.** `microcopy.md` is the source of truth for every line, and
`voice.md` for every word. A colour that needs a different word goes to the register, not into the
page.

---

## What does not transfer, said before it is discovered

1. **Photos.** The demo product is about rooms and people, and its cards are photographs. **Ours has
   none**: an item is a file or a folder, and a project is a set of them. The course's rule behind
   the photos is *no grey placeholder where real content belongs*. **For us that rule is about real
   content**: real file trees, real code, real repo refs, the real avatar of the signed-in person.
   It never means a stock image on an item card. *A decorative photograph on a skill would be the
   category default dressed up as content.* **The one place a photograph is honest is a person**: the
   signed-in owner and the sharer on a shared page, which are portraits. That is what stage 4 tests.
2. **The trust benchmark.** The course's is Airbnb, Bumble and Couchsurfing, trust between strangers.
   **Ours is trust in a result**: *checked, never works*. So the references are read for how they
   **show a verdict, a state and a count** (Vercel's deployment stages, Linear's dimming, GitHub's
   checks), not for how they make a stranger look safe.
3. **Mobile-first.** The demo is a mobile web app with a tab bar. **Ours is desktop-first** (§3), and
   the course's *bottom menu* on the stand becomes **the app header, the global nav and the run bar**.

---

## Stages — the course's seven

| # | Stage | Output | State |
|---|---|---|---|
| **1** | **References**: first describe the repo (screens, generators, shared styles, which files could leak a palette) and pick the main and contrasting screens. Then search **Refero** for the visual language of the craft benchmark research already named, Linear · Vercel · Raycast · GitHub · Stripe: 3–4 *styles*, 2–3 *screens* (a verdict or check-run list, a dense list with status). One base and one or two named devices from the others, each with **the persona's worry it removes**. The dark-design-language captures are read as references too | `06-concept/references.md` | **done 2026-10-08** — Refero not connected; Lazyweb, SaaSUI and our phase-01 captures instead, stated in the file. Plus an idea base of 61 images, [`refs/`](refs/README.md), by `tools/capture_refs.py` |
| **2** | **Taste and attributes.** The owner dictates *Designer's taste*: 2–3 **named** products they like, not adjectives, and the anti-references. Then 3–5 **pairs of visual opposites** from the data, each with its source line, the device it borrows, and its strength: data, or a hypothesis carrying `[?]`. A pair against the taste, or without a reason, does not pass | `06-concept/concept.md` · *Designer's taste*, *Attributes* | **done 2026-10-08** — five pairs; five conflicts (D1–D5) carried into stage 3 as variants, by the owner's decision |
| **3** | **Three directions**, under the **impeccable** skill. Three that genuinely differ, all dark-first, on at least two of: amount of colour, type character, form. **A palette guessable from the subject is replaced, not recoloured.** One page, live: palette with hex, a type pair, **an item card with real content**, a button, the three severity marks, Solar icons in the direction's style. Then stop | `06-concept/directions.html` | — |
| **4** | **The choice and the stand.** The only stage whose input is the owner's decision, made in the browser and passed as one sentence (number and name). The stand shows the language at work: the main card, buttons, the app header, the run bar. Below it: colours with the attribute each comes from (including **Problem / Note / Skipped / checked**), type pair and scale, radii, shadows, spacing, the person's portrait, **an icon coverage plan** (the six kinds, the three severities, nav, the run bar, buttons, states), and three components: **the primary action, the item row with its state badges, a form field**. Every value lives in `tokens.css`. **WCAG AA contrast is computed by a script**, as a table | `06-concept/concept.html`, `06-concept/tokens.css`, contrast table | — |
| **5** | **The sample**: the main screen with **all its state pages**, under impeccable's laws. Values come only from `tokens.css`. **Every repeat of a component gets the same values**, not just the first. Any new colour pair has its contrast computed. Copy and structure stay. Then `/impeccable critique`, and the owner reads every state in the browser | the main screen's pages | — |
| **6** | **The contrasting screen.** The same language, with nothing new invented. It shows a different density and a different mood. Compared side by side with the sample: **one product, not two** | the second screen's pages | — |
| **7** | **Check and close.** A defects table first, every row with **evidence** (a selector and its value, or a contrast ratio). It looks for: a decision without an attribute or a taste line; contrast below AA; colour against the voice (a festive error, an invisible warning, a green that claims *works*); the two screens out of step; one component with two values on a page; a placeholder where real content belongs; an icon outside the set; a hard-coded value. Add the `/impeccable audit` findings. The owner reviews, then fixes go into the pages and `concept.md` together. `CLAUDE.md` gains a *Concept* section and `README.md` a *Concept* section. Push | defects table, fixes, docs | — |

**Between stages, the course's one rule for a small adjustment.** A change lives where the language
lives, not where it was noticed. Try it on the screen. If the owner says **"keep it"**
(*залишаємо*), the value goes into `tokens.css` and `concept.html`, the reason into `concept.md`, and
it is carried to the second screen and every repeat. A change that contradicts an attribute changes
the attribute. *The course suggests writing this rule into `CLAUDE.md` once, so "keep it" is a
one-word instruction; that is done when the phase's section is written.*

**The course's own checks, kept as this phase's bar.** `references.md` has 3–5 sources, each with a
device and a reason, and none copied whole. *Taste* names products, not adjectives. Attributes are
3–5 pairs, none against the taste. Three directions are live, and the chosen one is not guessable
from the category. **The owner made the choice in the browser.** The stand carries an icon coverage
plan and three components, and every decision has its reason. Contrast is AA by a script, including
the pairs that appear in stages 5–6. **There are no hard-coded colours, radii or fonts on the
pages.** Both screens are painted by the same files. Copy and structure are unchanged. One component
has one set of values. One icon set and one style. **Exactly two screens painted**, and no
`DESIGN.md` written ahead of time.

---

## Prerequisites, owed before stage 1

- **The Refero MCP server is not connected in this environment.** Stage 1's search runs through it.
  *The owner connects it*, or stage 1 falls back to the captures already in the repo plus public pages
  read directly, and says so in `references.md`.
- **The impeccable plugin — installed 2026-10-08**, v4.5.0 from the marketplace `pbakaus/impeccable`,
  **scope `local`**: this project only, kept in the gitignored `.claude/settings.local.json`. It brings
  one skill with 24 commands (`/impeccable critique`, `/impeccable audit`, …) and **three hooks**
  (session start, after every `Edit`/`Write`, and a design pass on stop). Its engine binary sits in
  `~/.impeccable/bin`, SHA-256 checked. *Scoped locally on purpose*, so the hooks do not fire in other
  folders.
- **Unsplash**: needed for the portraits only (see *What does not transfer*). Each link is checked to
  open, and checked to be a portrait.

---

## Decisions owed to the owner

- **Which two screens** (stage 1). The course pairs a dense main list with a sparse single-focus
  page. **Recommended: `My library` as the main screen** (dense rows, kind badges, usage facts, six
  state pages: the corpus is the primary persona's own ground) **and `Run` as the contrasting one**
  (a stage stack and a verdict, with Problem / Note / Skipped carrying meaning, the product's designed
  moment). *Alternatives:* `Projects` (cards) as the main screen, and `Shared item` (one item, a
  receiver, the sparsest page there is) as the contrasting one.
- ***Designer's taste*** (stage 2): the named products and the anti-references. **Only the owner can
  write this list.**
- **Whether a direction shows its light theme** (stage 3). Dark is decided. The question is whether
  light is shown now, as a proof that it was designed rather than inverted, or left to phase 09.
- **The direction itself** (stage 4), in the browser.

## What it is not

- **Not the whole product.** Two screens. The roll-out is phase 07.
- **Not documentation.** No `DESIGN.md`; it is generated from the built code in phase 07.
- **Not tokens as a system.** `tokens.css` is one flat file of the language's values. The three-level
  token architecture is phase 08, and so is the styling engine (§10).
- **Not copy or structure.** Any line that wants to change goes back through `voice.md` and
  `microcopy.md`, and any structure goes to the register.
- **Not motion.** The validation pass is a designed moment (§6), and it gets designed in phase 11.
  Stage 4 may show a still of it.

Day-by-day notes: `PROGRESS-06.local.md` in this folder, gitignored (`CLAUDE.md` §13).
