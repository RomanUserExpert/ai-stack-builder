---
name: AI Stack Builder
description: A workspace where one person keeps their AI building blocks and assembles them into projects that export as a checked archive. Working style Mica · Lime, dark first.
colors:
  lime: "#C6EF5A"
  lime-hover: "#D3F57A"
  on-lime: "#141A08"
  mica-ground: "#1B1C19"
  bar: "#181916"
  tray: "#232420"
  cutout: "#1E1F1B"
  well-deep: "#161714"
  raised: "#2A2B27"
  control: "#2E302A"
  control-hover: "#383A33"
  line: "#343630"
  line-strong: "#4A4C44"
  control-edge: "#7C7F74"
  text: "#F3F4EF"
  text-2: "#C5C7BE"
  text-3: "#A1A49A"
  problem: "#FF8F98"
  note: "#F2C661"
  checked: "#C5C7BE"
  skipped: "#A1A49A"
  warning: "#EFA23A"
  on-warning: "#1A1200"
  danger: "#D4363F"
  danger-hover: "#BE2E37"
  on-danger: "#FFFFFF"
typography:
  display:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "28px"
    fontWeight: 600
    lineHeight: "34px"
    letterSpacing: "-0.018em"
  headline:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "20px"
    fontWeight: 600
    lineHeight: "26px"
    letterSpacing: "-0.012em"
  title:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 600
    lineHeight: "22px"
    letterSpacing: "-0.008em"
  body:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "14.5px"
    fontWeight: 400
    lineHeight: "21px"
  button:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "13.5px"
    fontWeight: 500
    lineHeight: "16px"
  small:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: "19px"
  micro:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 500
    lineHeight: "16px"
  label:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "11.5px"
    fontWeight: 600
    lineHeight: "16px"
    letterSpacing: "0.06em"
  code:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: "20px"
rounded:
  xs: "4px"
  sm: "6px"
  md: "10px"
  lg: "14px"
  xl: "18px"
  pill: "999px"
spacing:
  s1: "4px"
  s2: "8px"
  s3: "12px"
  s4: "16px"
  s5: "20px"
  s6: "24px"
  s8: "32px"
  s10: "40px"
  s12: "48px"
components:
  button-primary:
    backgroundColor: "{colors.lime}"
    textColor: "{colors.on-lime}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: "0 12px"
    height: "32px"
  button-primary-hover:
    backgroundColor: "{colors.lime-hover}"
  button-secondary:
    backgroundColor: "{colors.control}"
    textColor: "{colors.text}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: "0 12px"
    height: "32px"
  button-secondary-hover:
    backgroundColor: "{colors.control-hover}"
  button-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-warning}"
    rounded: "{rounded.sm}"
    height: "32px"
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-danger}"
    rounded: "{rounded.sm}"
    height: "32px"
  button-danger-hover:
    backgroundColor: "{colors.danger-hover}"
  search-field:
    backgroundColor: "{colors.well-deep}"
    textColor: "{colors.text}"
    typography: "{typography.small}"
    rounded: "{rounded.sm}"
    padding: "0 12px"
    height: "32px"
  row-tray:
    backgroundColor: "{colors.tray}"
    rounded: "{rounded.lg}"
    padding: "8px"
  row-cutout:
    backgroundColor: "{colors.cutout}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
  row-cutout-active:
    backgroundColor: "{colors.raised}"
  kind-tag:
    textColor: "{colors.text-2}"
    typography: "{typography.micro}"
    rounded: "{rounded.pill}"
    padding: "0 8px"
    height: "20px"
  finding-mark-problem:
    textColor: "{colors.problem}"
    typography: "{typography.micro}"
    rounded: "{rounded.pill}"
    padding: "0 12px 0 8px"
    height: "24px"
  finding-mark-note:
    textColor: "{colors.note}"
    typography: "{typography.micro}"
    rounded: "{rounded.pill}"
    padding: "0 12px 0 8px"
    height: "24px"
  project-card:
    backgroundColor: "{colors.raised}"
    rounded: "{rounded.lg}"
    padding: "20px"
  nav-place-current:
    backgroundColor: "{colors.raised}"
    textColor: "{colors.text}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: "0 12px"
    height: "32px"
  dialog:
    backgroundColor: "{colors.raised}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: "24px"
    width: "520px"
---

<!-- Generated 2026-10-19 by /impeccable document from the 22 mockups of the main job
     (04-wireframes/mockups/: Projects, Project and Run, every state) and 06-concept/tokens.css.
     The values above mirror tokens.css. Values are changed there (tools/concept_tokens.py) and
     this file is regenerated; where the two disagree, tokens.css wins. -->

# Design System: AI Stack Builder

## Overview

**Creative North Star: "The Inspector's Report"**

The product reads like an inspection, not a sales sheet. It says what was examined, counts what it
found and names the cost before the step. It never says what any of that means, and it never says
*works*. The interface is a dark, neutral working surface of quiet layers: a Mica ground with a faint
lime tint, a tray, and every item pressed into its own cut-out. One lime marks what you can press and
where you are. The severities are tinted tags carrying a word and an icon. There is no success colour
at all: the best a check can say is *Checked*, drawn as a quiet dot.

Density sits between Default and Comfortable: a lot on the screen, held by the grid and the type
rather than by colour, as in Figma's panels. Edges come from hairlines before shadows, as in Linear.
Glass (acrylic) is the signature touch and is kept to the frame around a mode or a dialog. Text never
sits on glass; it sits on an opaque sheet.

The components are **quiet and exact**: grey controls, hairline edges, states named by a word and a
shape, and colour held in reserve.

**Rejected outright:**
- the AI-tool palette: violet-blue neon, gradients, glow;
- a marketplace showcase: `Verified` and `Popular` badges, stars, ratings, cover cards;
- glass everywhere, or text on a blur;
- a green tick as the main signal.

**Key Characteristics:**
- Dark first; the light theme is designed, not inverted. One light slice exists, and the full theme
  comes in phase 09.
- One brand colour, lime, which is never a verdict.
- Every item in its own rounded cut-out inside a tray; auto-added items nest under their parent
  behind a dashed rule.
- Findings are tinted capsules with an icon and a word: Problem and Note on the right of a row,
  `Conflict` beside the name.
- Paths, refs, timings and file contents are in Geist Mono with tabular figures.
- One primary action per screen.

## Colors

A near-monochrome Mica ground carries one acid lime for action, and two muted severity tints that
only ever appear as tags and boxes.

### Primary
- **Signal Lime** (`lime`): the only colour that invites an action. It fills the primary button and
  checked checkboxes and radios. As a mark it draws the active row's pill, the spinner's head, the
  focus ring and the pill on a finished export. It is never a verdict. Text on it is **Lime Ink**
  (`on-lime`, 13.5:1).

### Neutral
- **Mica Ground** (`mica-ground`): the page. A faint lime tint keeps it from reading as dead grey.
- **Top Bar** (`bar`): the app header, the Run bar and the library sidebar, one step below the ground.
- **Tray** (`tray`): the surface under a list of rows and under an empty or error state.
- **Cut-out** (`cutout`): each row's own pressed-in field inside the tray.
- **Deep Well** (`well-deep`): code blocks, the search field, the segmented control's track and the
  checkbox cell. It is the darkest surface, so its edge holds the column.
- **Raised** (`raised`): one step up. Cards, the item side panel, the active row, dialogs, and the
  current place in the top bar.
- **Control** (`control`, hover `control-hover`): secondary buttons and the empty-state tile. Controls
  stay grey.
- **Hairline** (`line`) and **Strong Hairline** (`line-strong`): every divider; a control's, tag's or
  callout's edge; dashed rules.
- **Control Edge** (`control-edge`): the border of a checkbox or radio, at 3:1 for WCAG 1.4.11.
- **Ink**, **Ink 2** and **Ink 3** (`text`, `text-2`, `text-3`): three text tones. They are for
  names, for sentences and descriptions, and for metadata and Skipped.

### State
- **Problem Rose** (`problem`): *the archive will be wrong.* Used on a tag, a capsule or a box's edge,
  always on a 10–14 % wash of itself.
- **Note Amber** (`note`): *correct but incomplete.* Same treatment as Problem.
- **Checked** (`checked`) and **Skipped** (`skipped`): neutral. A 6 px dot and a slashed circle.
- **Warning Amber** (`warning`): only on the button that goes ahead despite a Problem (*Export with
  1 problem*).
- **Remove Red** (`danger`, hover `danger-hover`, which darkens and never lightens): only on an act
  that removes something, in its confirmation.

### Named Rules
**The Colour Is a Claim Rule.** A colour on screen asserts something. Lime asserts *you can act here*
or *you are here*. Rose and amber assert a finding. Nothing else gets a hue.

**The No Success Rule.** There is no green anywhere. A passed check is a quiet neutral dot, because we
examined the set and ran nothing.

**The One Red Rule.** Red appears only on the step that removes. Inside a Problem the remove is a
ghost button with rose text and a rose edge, filled only on hover; the solid red is kept for the
confirmation.

## Typography

**Display Font:** Geist (with system-ui)
**Body Font:** Geist (with system-ui)
**Label/Mono Font:** Geist Mono (with ui-monospace)

**Character:** One sans face for everything a person reads, and a mono for everything a machine
reads: paths, refs, timings, error codes, file contents. The hierarchy is carried by size and weight
steps, not by colour.

### Hierarchy
- **Display** (600, 28/34, −0.018em): a project's name, the one per screen.
- **Headline** (600, 20/26, −0.012em): the Export mode's verdict (*Checked just now*), and the title
  of an empty, error or finished-export state.
- **Title** (600, 16/22, −0.008em): a card's name, the side panel's item, a dialog.
- **Body** (400, 14.5/21): names and sentences. Row names are body at 600. Prose holds to 640 px.
- **Button** (500, 13.5/16): buttons, places in the top bar, segments.
- **Small** (400, 13/19): descriptions, counts, head meta, dialog text.
- **Micro** (500, 12/16): tags and finding capsules (600 there); facts under a row at 400.
- **Label** (600, 11.5/16, +0.06em, uppercase): section labels such as *FINDINGS* and *IN THIS
  PROJECT*.
- **Code** (Geist Mono 400, 12/20): paths, refs, step numbers, durations, contents.

### Named Rules
**The Machine Reads Mono Rule.** If a string would be typed into a terminal or read by an agent, it
is set in Geist Mono. Step numbers and durations also take tabular figures.

## Layout

Desktop first. The screens are drawn at 1440. A page has a 52 px bar, then a main column padded
32 px with 24 px between blocks. The spacing scale is 4 px (4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 ·
48), and nothing sits off it.

- **Projects:** a three-column card grid with a 20 px gap. Search and one `Filters` button sit above
  it, and the Filters popover hangs from its button.
- **Project:** a list of rows in a tray. Opening an item puts a 440 px side panel beside the list, and
  the panel stays sticky. A row's grid is name · middle column (320) · actions (200), or name · marks
  when it only carries findings.
- **Configuring:** a 440 px library sidebar on the left, with the set beside it.
- **Run (Export):** takes the whole surface under its own bar (back · `Export` · agent target). It
  has a summary line, then grouped stages (*Findings*, *Handover*), then the Export stage last. A
  stage row is number (24) · name (300) · result · time (48).
- Density sits between Default and Comfortable: rows have 12 px vertical padding, and controls are
  32 px high.

Responsive is phase 10; at 390 px the pages overflow, as the wireframes do.

## Elevation & Depth

Tonal layering, not shadows. Depth is a step in the Mica ramp: ground → tray → cut-out pressed into
it → raised for what is open or active. A hairline marks every edge.

### Shadow Vocabulary
- **Cut-out** (`inset 0 0 0 1px line, inset 0 1px 2px rgba(0,0,0,.35)`): a row pressed into its
  tray. It is inward, never a drop shadow.
- **Tile** (`0 1px 2px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.04)`): the current place in
  the top bar, and the lifted segment of a segmented control.
- **Sheet** (`0 18px 40px rgba(0,0,0,.35)`): a dialog or popover over a mode.
- **Focus** (`0 0 0 2px ground, 0 0 0 4px lime`): 2 px of lime with a gap, on every focusable thing.

### Named Rules
**The Hairline First Rule.** Rows, cards and panels carry no drop shadow. A shadow appears only where
something is lifted over the place under it: the current place, a segment, a dialog.

**The Glass Frames, Never Holds Rule.** Acrylic is an 8 px lime-tinted translucent edge with no blur.
It belongs only to the frame around a dialog or the Filters popover, and the sheet inside is always
opaque. The Export mode has no frame. *Owner, 2026-10-19: kept like this for now. The blurred frame
lives only on the phase-06 stand.*

## Shapes

Soft, not round, and the radius grows with the size of the thing so that nesting reads:
- 4 (`xs`): inline code, the pill marks and skeleton bars;
- 6 (`sm`): a control;
- 10 (`md`): a row's cut-out and a box inside it;
- 14 (`lg`): a tray, a card, a panel, a dialog;
- 18 (`xl`): the acrylic frame on the stand;
- pill: tags and finding capsules.

Every boxed object has a visible edge. A dashed rule means *belongs to the row above*: auto-added
items, and a Skipped stage's outline.

## Components

### Buttons
- **Shape:** soft rectangle (6 px), 32 px high, 12 px side padding, icon (16) and label 8 px apart.
- **Secondary (default):** a Control fill with a Strong Hairline edge and Ink text. On hover it steps
  to Control Hover.
- **Primary:** lime fill, Lime Ink at 600. **One per screen.** When an empty or error state carries
  its own primary, the head's primary drops to secondary.
- **Warning:** amber fill, dark text. Only *Export with 1 problem*.
- **Danger:** red fill, white text. Only a removal confirmation. **Quiet danger** is the in-Problem
  remove: transparent, rose text and edge, washed on hover.
- **Quiet:** no fill, no edge, Ink 2.
- **Disabled:** Control fill, Hairline edge, Ink 3. It exists for one case only, the empty project's
  `Export`.
- **Focus:** the lime focus ring.

### Tags and finding capsules
- **Kind tag** (`skill`, `script`, `mcp`…): a 20 px pill outlined by a Strong Hairline, Micro, Ink 2.
- **`Conflict` tag:** the same pill in rose on a rose wash with a rose edge, beside the name.
- **Finding capsule** (Problem, Note): a 24 px pill holding an icon and a word, 600, in its tone on
  its wash, at the row's right edge. Problem uses Lucide `circle-alert` and Note uses `info`.
- **Stage result:** inline. Problem and Note carry their glyph and bold tone; Checked is a 6 px
  neutral dot; Skipped is Lucide `ban` in Ink 3.

### Rows (the signature component)
- **Tray and cut-out:** rows sit in a Tray (14 px, 8 px padding, 8 px gap). Each row is its own
  Cut-out (10 px) with the inward cut-out shadow; hovered, it moves half a step towards Raised, still
  opaque.
- **Content:** a name (body 600) with its kind tag, a description (Small, Ink 2, ≤ 640), then facts
  (Micro, Ink 3, mono for paths).
- **Auto-added:** nested inside the parent's cut-out behind a dashed rule, indented by 24, and with no
  remove of its own.
- **Active:** the cut-out steps to Raised, and a 3 px lime pill runs the full height of the item at
  the left edge, inset 12 top and bottom. The cut-out's own hairline edge brightens one step, to Strong
  Hairline. There is no extra ring.
- **No ring:** a finding never draws a coloured ring round a row.

### Cards
- **Project card:** Raised, 14 px, a Hairline edge (Strong on hover), 20 px padding. The name is
  Title, with tags after it. The last check sits at the foot above a hairline, as a Label-cased
  *Last check* with its line, so verdicts align across a row of cards.

### Inputs / Fields
- **Search:** Deep Well, a Strong Hairline edge, 6 px, 32 px high, a search icon in Ink 3 and
  placeholder in Ink 3. On focus the edge goes lime-mark and the focus ring shows.
- **Select:** a secondary button's shape.
- **Checkbox / radio:** a 16 px Deep Well cell with a Control Edge border. Checked: the checkbox fills
  with lime and shows a dark tick; the radio becomes a lime ring with a lime dot.
- **Add to set:** an icon button, *+ Add*. Once added it reads *✓ In this project*, unfilled, with a
  lime-mark tick. The native checkbox stays underneath for the keyboard.

### Navigation
- **Top bar:** 52 px on Top Bar. It holds the product mark (a 14 px lime square), then the three
  places — `My library` · `Public library` · `Projects` — as text, with the signed-in person (a 24 px
  portrait) at the right. **The current place is a Raised tile with the tile shadow, in Ink.** The
  others sit on nothing and wash on hover.
- **Segmented control** (scope switch): a recessed Deep Well track with a hairline edge. The current
  segment is lifted out of it on Control with the tile shadow. It is a different element from the top
  bar.
- **Kind tabs:** one line that scrolls rather than wraps. The current tab is on Raised at 600, and
  counts are in Ink 3.

### Check stages (Run)
- A stack of 10 px cut-outs, each a disclosure: step number (mono, Ink 3), name (body 600), result,
  and duration (mono, tabular, right-aligned). Expanding shows the finding's box under the result
  column.
- A **Skipped** stage has no fill and a dashed Strong Hairline outline: the check had nothing to
  check.
- The **Export stage** is last: a Raised card. When it is finished it gets a lime pill at its left
  edge and a Headline title. When it has failed it sits on the Problem box. While it is in progress
  it shows a lime-headed spinner.

### Findings boxes (callouts)
- **Problem box:** rose at 10 % over the cut-out, a rose edge, 10 px. A bold rose *Problem* label,
  then the sentence in Ink with inline code, then actions.
- **Note box:** the same in amber.

### Empty and error states
- **One tile everywhere:** on a Tray, centred. A 48 px Control tile holds a 20 px icon in Ink 2. The
  title is Headline, the sentence is body in Ink 2, and error codes are in mono Ink 3. Not lime and
  not a wash: the sentence carries what happened.
- **Loading:** skeleton bars (4 px radius) shimmering Raised → Control Hover → Raised, still under
  reduced motion.

### Dialogs and the Filters popover
- **Dialog:** a 520 px Raised sheet with a 14 px radius, an opaque body and the sheet shadow. Its
  frame is an 8 px acrylic edge (`acrylic-dialog`) over a veil that dims the mode behind. The
  confirmation names the consequence; the destructive confirm is Remove Red.
- **Popover:** the same sheet and edge, 360 wide, hanging from its button. It has a header, groups
  under Label legends, and a footer with *Clear* and the primary.

## Do's and Don'ts

### Do:
- **Do** take every value from `06-concept/tokens.css` through `var()`. `tools/concept_ui.py
  --check` and the mockup build refuse a literal colour, px size or font name.
- **Do** keep lime to what you can press and where you are, and keep one primary per screen.
- **Do** pair a severity's colour with its icon and its word, as a tinted capsule or box.
- **Do** draw *Checked* as the quiet neutral dot, and *Skipped* as `ban` with a dashed stage outline.
- **Do** set paths, refs, timings, codes and file contents in Geist Mono.
- **Do** put every item in its own cut-out, and nest auto-added items under their parent behind a
  dashed rule.
- **Do** give every boxed object a visible edge; use hairlines before shadows.
- **Do** measure every new colour pair with `tools/contrast.py`. AA applies to text, and 3:1 to a
  control's edge or a state mark. Today that is 88 pairs, all passing.

### Don't:
- **Don't** use a green tick, or any success colour. We examined the set; we ran nothing.
- **Don't** use violet-blue neon, gradients or glow: the palette an AI produces for "AI tool".
- **Don't** add `Verified` or `Popular` badges, stars, ratings, scores or cover cards. Usage facts are
  the only per-item evidence.
- **Don't** put text on glass, or use glass outside the frame of a mode, dialog or popover.
- **Don't** draw a coloured ring round a row that carries a finding.
- **Don't** use red for anything but removal, or lime for a verdict.
- **Don't** let the browser draw a white checkbox or radio on the dark theme.

## Sources

- [`06-concept/concept.md`](06-concept/concept.md): **why** each value is what it is. It holds the
  designer's taste, the five attribute pairs, the *Working style — Mica · Lime* table, and the stages
  that produced it. As of 2026-10-19 it follows the mockups; see its *Phase 07* section.
- [`06-concept/references.md`](06-concept/references.md): the references: Linear as the base, and the
  devices taken from Vercel, GitHub, Raycast and Teams.
- [`06-concept/tokens.css`](06-concept/tokens.css): **every value**, generated by
  `tools/concept_tokens.py`. The frontmatter above mirrors it.
- [`06-concept/contrast.md`](06-concept/contrast.md): every colour pair, measured.
- [`05-tone-of-voice/voice.md`](05-tone-of-voice/voice.md): the voice the North Star is taken from.
- The evidence: [`04-wireframes/mockups/`](04-wireframes/mockups/), the 22 pages this file was read
  from.
- [`PRODUCT.md`](PRODUCT.md): the product, as a digest of `CLAUDE.md`.
- **Not a source:** [`DESIGN-artifacts.md`](DESIGN-artifacts.md) is the look of the phase pages, not
  the product's.
