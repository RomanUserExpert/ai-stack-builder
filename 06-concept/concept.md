# Concept — phase 06

**Started 2026-10-08, stage 2.** This file holds the **reasons** for the visual language. Values go in
`tokens.css` (stage 4), and the sources are in [`references.md`](references.md). **Every colour,
radius and font must trace to a line in *Designer's taste* or in *Attributes*. A value with neither is
the model's default, not a decision.**

---

## Designer's taste

**The owner's, dictated on 2026-10-08.** *Translated from the owner's Russian, close to the words.*
This list is the owner's and nobody else's. It is the only input to this phase that is allowed to be
a preference rather than a finding.

### Likes — products, not adjectives

- **Vercel.** A clean interface without decoration: the status, the fact and the consequence stand
  side by side. Monochrome. Colour appears only where it means something: an error, a warning, a
  success.
- **Figma.** A dense working surface of panels, layers and properties. A lot of information on screen,
  and it does not look overloaded, **because the hierarchy is held by the grid and the type, not by
  colour.**
- **Microsoft Teams / Slack.** Glass surfaces: translucent layers that blur what is behind them. **This
  is the product's signature touch. It should be noticeable, but used sparingly.**

- ~~**Microsoft Fluent System Icons** (added 2026-10-08).~~ **Superseded 2026-10-11 by Lucide** — see *Working style*. The icon set, chosen by the owner, **in
  place of the course's Solar.** [`microsoft/fluentui-system-icons`](https://github.com/microsoft/fluentui-system-icons),
  MIT, regular and filled at 16 / 20 / 24 px, as `@fluentui/svg-icons`. *It is the same family as
  Teams, which the glass line above already names, so the two likes come from one design language.*
  **Its colour variant is not used**: it puts colour on every icon, which breaks pair 5.

### Does not want

- **The palette an AI produces for the words "AI tool":** a dark ground, violet-blue neon gradients,
  glow.
- **A marketplace showcase:** `Verified` and `Popular` badges, stars, ratings, cover cards — as at
  Smithery, Glama and mcp.so (see [`research.md` §10](../01-research/research.md)).
- **Glass everywhere:** translucent content, text on a blurred background with no backing, glass that
  eats contrast.
- **A green tick as the main visual signal.** It promises *works*, and we run nothing.

---

## Attributes

**Five pairs of visual opposites**, each written as *this, not that*. Each one names **the line of data
it comes from**, **the device it leans on** in the references, and **what it stands on**:

- **data**: research, the brief or `CLAUDE.md`, with its mark as the source file gives it;
- **taste**: the list above;
- **[?]**: a line that `personas.md` or `jtbd.md` itself marks unknown.

> **One standing caution, applied to every pair.** *"The audience lives in Linear, Vercel, Raycast,
> Figma"* (`CLAUDE.md` §3) is **H11 in `personas.md`, the owner's assertion, not an observation**:
> *"No instrument in this repository can reach it, and none has… it stays a hypothesis through the
> design system."* **Wherever a pair leans on that sentence, it is marked taste + [?], never data.**

**Conflicts are named, not smoothed.** Where the data pulls one way and the taste another, the pair
says so. **The owner decides**, and the open decisions are collected at the end.

### 1 · An inspector's report, not a seller's badge

**What it means on screen.** A verdict is shown as **facts placed side by side**: what was examined,
how long it took, and the counts. It is never a seal. There is no score, no rating, no star, and no
green badge that stands in for a sentence.

**Where it comes from:**
- **EJ-2, *believe that a clean result was actually earned*** (`jtbd.md` §3). Marked `✓`: the
  utterances are re-runnable (*"blackbox oracles make bad workflows"*). The jobs file itself says
  **the inference that this is a feeling is ours, `R`**. Its P1 importance is **2**, restored on
  2026-09-10 on a named person with a reproduction repository.
- **P1 Trust triggers, *Repels: a green tick that was not earned*** (`personas.md` §4). Marked
  `*` + `✓` R7, and again *"the inference is ours"*.
- **`research.md` §10, finding 2, on the market's own words:** *"Trust is a number or a badge"*.
  Smithery `Verified`, Glama *Quality Score*, Tessl *You get a score*. Marked `✓`, fetched.
- **`voice.md` principle 1**, *say what was examined, never what it means*, and `CLAUDE.md` §5–§6:
  no score, no badge, *checked, never works*.
- **And Q20** (`CLAUDE.md` §8): the shared surfaces carry *"the most conservative treatment… show
  more and promise less"*.

**Devices:**
- **B1**, Vercel's stage row: duration plus verdict glyph at the right edge
  (`vercel-deployment-stages.jpg`).
- **B2**, status as a dot plus a word (`● Ready`).
- **C1**, GitHub's neutral `⊘` for Skipped (`github-actions-failed-job-steps.png`).

**Stands on: data.** The two *feeling* readings are our inference, `R`, and the source files say so.

**Taste: agrees.** Vercel is liked for *status, fact and consequence side by side*. The anti-list
refuses the marketplace showcase and the green tick.

### 2 · Dense and counted, not spacious and showcased

**What it means on screen.** A row carries many small facts at once: kind, path, usage, requires,
needs, defers-to, a pinned `ref` and its licence. **Hierarchy comes from the grid and the type
weight, not from colour or cards.** Counts sit next to the control they count, and **a count is a
link to the list behind it.**

**Where it comes from:**
- **P1's collection is 11 to 48 items** (`personas.md` P1 §1), **`✓` counted** through the GitHub
  tree API: **"Design for fifty, not for thirty"**, NK-2.
- **The usage fact is the one thing a practitioner asked for unprompted** (`personas.md` P1 §4):
  *"Usage data, first… that alone would let me delete half of it with confidence"*. Marked `*`, one
  person, *"the strongest form a `*` can take"*.
- **EJ-3, *stop suspecting that half of what I keep is dead weight*.** Importance **3**, `✓` + `*`.
- **`voice.md` principle 4**, *counts and names, not adjectives*.
- **And `research.md` §10, finding 1:** *"The shelf talks about itself, not about the item."*

**Devices:**
- **Figma's properties panel**
  (`01-research/2-flows/05-linked-vs-detached/figma-instance-overridden-panel.png`). Small section
  heads (`Position`, `Auto layout`, `Appearance`, `Fill`); rows of label left, value right; grey
  field fills; **the only colour is the selection and the component's own mark.**
- **The count beside the action:** Figma's *423 instances*. **A correction to the brief:** that count
  is not in the layers panel. **It is in the library-updates dialog** (flow 05, `README.md`, and
  `figma-library-updates-instance-counts.png`).
- **And OBS-29 says Figma loses on exactly this axis.** VS Code's *"95 workspace settings are not
  applied"* is **a number that is also a link**, and Figma's is bare. **Take the position from
  Figma and the link from VS Code.** Marked `M`: *"evidence of what a good product chose, not that it
  works on this person"*, `[?]` → H3.
- **C2**, GitHub's count capsule after a tab label.
- **D1**, Raycast's dimmed metadata line.

**Stands on: data** for the counts and the usage facts. **Taste** for *Figma* as the model of density.

**A nuance worth stating.** Fifty items is not many. **The density is per row, not per screen.** It
comes from how many facts one item carries (`CLAUDE.md` §5's fields), not from how many items there
are. *Dense* must not turn into *tiny type to fit a thousand rows*.

**Taste: agrees.** Figma is liked for exactly this. The anti-list refuses cover cards.

### 3 · The consequence is visible before the step, not after it

**What it means on screen.** The sentence that names a cost sits **inside the control it applies to,
above the button**. Examples: *used in 3 projects · saving un-checks all three*, *the archive will
contain only one of them*. It does not appear in a toast afterwards, and it is not an *Are you sure?*

**Where it comes from:**
- **OBS-31**, P1 Trust triggers, *Convinces: a consequence named in the present tense before the
  irreversible step*. Marked `M`: a product's choice, not a proof that it moves this person.
- **EJ-1, *not be quietly overruled by my own tools*.** Importance **3** for P1, `✓` + `*`, *"the
  strongest emotional job in the file"*.
- **`voice.md` principle 2**, *name the consequence, in the reader's terms, before the step*.
- **`CLAUDE.md` §6**: the unclean export is confirmed with the consequence, and nothing blocks.

**Device: Vercel's env drawer**
(`01-research/2-flows/07-env-and-secrets/vercel-add-env-variable-drawer.jpg`). The choice `Secret`
carries **"You can't reveal this value after saving"** *inside the option itself*, before `Save`. The
optional note's placeholder is *"Where to rotate, or who to contact"*.

**Stands on: data** (EJ-1). The device is `M`.

**Taste: agrees.** It is the *consequence* in *status, fact and consequence side by side*.

### 4 · Glass is a layer over the work, not the work itself

**What it means on screen:**
- **Glass appears only on temporary surfaces:** the `Export` mode's frame, the library panel in the
  configuring mode, dialogs, menus, popovers.
- **The library and the project stay opaque**, and so does every surface a person reads to decide
  something. Text always sits on a backing.
- **Through the glass you see the place you came from, blurred.** A mode is not a place (`CLAUDE.md`
  §8: *"Everything else is a mode, an overlay… including `Run`… because nothing is stored and no
  address returns you to it"*). The glass shows that structurally: you are *over* the Project, not
  somewhere else.

**Where it comes from:**
- **Taste.** Teams / Slack, *noticeable but sparing*, and the anti-list's *glass everywhere*.
- **The structure, which is data:**
  - `CLAUDE.md` §8: six places, everything else a mode or an overlay.
  - Q33: configuring is a draft you enter and leave by `Save` or `Cancel`.
  - Q25: a session returns you *to the place, not into the act*.

**Device: translucent panels and overlays in Microsoft Teams and Slack.** **There is no capture of
either in this repo** — a gap. Stage 3 must take one, or the device is cited from memory, which this
file does not allow. **The nearest captured contrast** is Vercel's env drawer: the same idea, *a
temporary surface over a dimmed place*, done **opaque with a scrim**. That is the non-glass version
of this pair, and the fallback if glass fails the checks below.

**Stands on: taste**, with data only for *where*. **No line in `personas.md` or `jtbd.md` asks for
glass or refuses it**, so there is no `[?]` either way. This pair is the owner's signature, and it is
labelled as one.

**Four conflicts, named and not resolved:**

1. **Glass against WCAG AA, measured in stage 4.**
   - The contrast of text on glass depends on what is behind it, so **it cannot be computed once,
     statically**. Stage 4's contrast script needs a fixed pair.
   - *Proposed:* text on glass is never measured against the blur. It sits on an inner backing with a
     fixed minimum opacity, and the ratio is computed against the **worst case** underneath (the
     lightest content in the product).
   - **This is the owner's own anti-reference** (*no text on blur without a backing*), so it narrows
     the taste rather than fighting it. *But it makes the glass visible only at the frame and the
     edges — confirm that is still the signature you want.*
2. **Glass against the base reference.**
   - `references.md` chose Linear as the base, and Linear's elevation is **"border and a whisper of
     tone, not a shadow ramp… flat and quiet"**. Glass is a different elevation model.
   - *Proposed:* two models with one rule. **In-flow surfaces** (places) are Linear-flat. **Temporary
     surfaces** (modes, overlays) are glass. *This is a real seam in the language, and the owner
     should accept it knowingly.*
3. **Glass against the course's own list of defaults.**
   - [`README.md`](README.md) lists the universal AI default to refuse as **"a blue-violet gradient,
     glass cards and icons in circles"**.
   - *Glass cards* are exactly the owner's anti-reference *glass everywhere*, so the taste and the
     course agree on cards. **They disagree on glass as such.** The course treats it as a default
     symptom; the owner treats it as a signature.
   - *Proposed:* glass never touches a card or a row. *Stage 3's three directions should include one
     with no glass at all*, so the choice in stage 4 is made against a real alternative.
4. **Glass on `Export`, the surface where findings are read.**
   - `Run` *"takes the whole surface"* (§8), and it is where a person reads a *Problem* before an
     irreversible step: the most decisive reading in the product.
   - If the mode is glass, its findings must still be opaque (conflict 1). In practice that leaves the
     mode's **head and edges** as glass, and the stage stack solid.
   - *Proposed as above. Raised because "glass on Export" in the brief could be read as glass under
     the findings, which would break pair 1.*

### 5 · Colour is a claim, held back — not a colourful dashboard, and not AI neon

**What it means on screen:**
- The interface is greyscale.
- **Colour appears only where it states something the product actually knows:** a *Problem*, a
  *Note*, a selection, a link.
- Kind (`skill`, `mcp`…) is **not** a colour claim. It is a word on a grey chip, carrying at most one
  small dot.
- **There are no gradients and no glow**, anywhere.

**Where it comes from:**
- **`CLAUDE.md` §6**, three severities. *Skipped* gets a **neutral** glyph: *"not a green tick it did
  not earn, and not a red one it does not deserve"*. *Checked*, never *works*.
- **`CLAUDE.md` §3**, *"generic dashboard aesthetics will read as cheap"*. **This stands on H11: taste
  + [?].**
- **`voice.md` *Forbidden***: cheer, selling copy, festive errors (stage 7's check: *an error must not
  look festive, a warning must not be invisible*).

**Devices:**
- **Linear, the base:** *"Colour is reserved for meaning; everything structural is greyscale"*, and
  labels drawn as a grey chip with a single coloured dot (`refs/web/linear-changelog-02.png`).
- **Vercel's monochrome.**
- **Grafana Play** (`refs/web/grafana-play.jpg`), kept as **the counter-example**.

**Stands on:**
- **data** for *colour must mean something* (§5, §6);
- **taste + [?]** for *greyscale as the craft bar* (H11);
- **taste** for *no neon* (the anti-list).

**One conflict inside the taste itself, for the owner to settle.**
- *Likes: Vercel* says colour appears on **"an error, a warning, a success"**.
- *Does not want* says **no green tick as the main signal, because it promises *works*.**
- **And this product has no *success*.** It has *Checked*: examined, cohered at that moment
  (`CLAUDE.md` §6). So the question is concrete: **does *Checked* get a colour at all?**
  - **A.** **No colour.** *Checked* is neutral like *Skipped*, with a distinct glyph. Colour belongs
    only to *Problem* and *Note*. Strictest reading of §6 and of pair 1.
  - **B.** **A quiet colour** — a dot, not a tick, not a filled disc (device B2), in a hue that is
    *not* the conventional success-green.
  - **C.** **Green, but small and never the largest thing on the screen.** Closest to Vercel, and
    nearest to the anti-reference.
  - *My reading of the data favours **A**, with **B** as the fallback if a neutral *Checked* reads as
    "nothing happened". This is the owner's decision.*

---

## Decisions owed to the owner, from this stage

**Answered 2026-10-08, by the owner: none of these is decided in the abstract. Each is proposed as a
variant in stage 3's concepts, and chosen in the browser with the direction in stage 4.** So the three
directions must between them **cover the live options**: at least one without glass (D4), at least one
with glass held to the frame and edges (D2, D3), and *Checked* drawn differently across them (D1 — A,
B and C each appear at least once, or the reason one does not is stated on the page). D5 is stage 3's
own job: a Teams or Slack capture before the glass direction is drawn.

| # | Question | Where |
|---|---|---|
| D1 | **Does *Checked* carry colour?** A neutral · B quiet non-green dot · C small green | Pair 5 |
| D2 | **Glass only at the frame and edges** (text always on an opaque backing, contrast measured against the worst case): is that still the signature you want? | Pair 4, conflict 1 |
| D3 | **Two elevation models**, flat for places and glass for modes: accepted as a deliberate seam? | Pair 4, conflict 2 |
| D4 | **Should one of stage 3's three directions have no glass**, so the choice is made against a real alternative? | Pair 4, conflict 3 |
| D5 | **A Teams or Slack capture** for the glass device: the owner supplies one, or stage 3 takes one from public pages | Pair 4, *Device* |

**What this section does not decide.** No hex, no font, no radius. Stage 3 draws three directions
from these five pairs, and **a direction that breaks a pair is not drawn**.

---

## Working style — Mica · Lime

**Fixed by the owner on 2026-10-11, after four rounds of directions** (`directions.html` → `directions-2.html` →
`directions-3.html` → `directions-4.html`). Round 1 and round 2 were turned down; from round 3 the owner kept
*Mica* and a density between Default and Comfortable; from round 4 *Lime*, in round 2's *Kit* row form.
**This is the base for stage 4 (`tokens.css`, the stand). Values below are stage-3 values, not yet tokens.**

| Decision | Value | Reason |
|---|---|---|
| Material | Mica: neutral ground `#1B1C19` with a faint lime tint; layers `#232420` / `#2A2B27`; cut-out `#1E1F1B` | Taste: Teams glass, *noticeable but sparing*; pair 4 |
| Glass | Acrylic **only around ~~the Export mode and~~ a dialog** **and the Filters popover**; text always on an opaque sheet (D2, D3 accepted). *Phase 07, owner 2026-10-19, "for now": in the product it is an 8 px translucent edge with no blur, and Run has no frame; the blurred frame is on the stand only* | Pair 4, conflicts 1–4; owner, 2026-10-19 |
| Brand | Lime `#C6EF5A`, ink `#141A08` on it (13.5:1). **Only on what you can press and where you are**: primary button, current place, selection | Pair 5: colour is a claim; lime is never a verdict |
| Severities | Problem `#FF8F98`, Note `#F2C661`, Skipped neutral with Lucide `ban`, **Checked a quiet dot, never green (D1-B)** | §6; pair 1 |
| Type | ~~Schibsted Grotesk; Source Code Pro~~ **Geist; Geist Mono for paths, refs, file contents** (owner, 2026-10-11, after the polish). *impeccable flags Geist as an overused face; kept on the owner's word — the brief wins* | Owner |
| Segmented control | **Not the top bar** (owner, 2026-10-11): a scope switch such as *My library · Public library* sits in a recessed track (`--well-deep`, a hairline edge) and its current segment is lifted out of it (`--control`, `--shadow-tile`, a `--line-strong` edge). The top bar has no track: its current place is a raised tile on the bar itself | Owner, 2026-10-11 |
| Add to the set | **An icon button, not a bare checkbox** (owner, 2026-10-11): *+ Add* is a small secondary button; once the item is in the set it reads *✓ In this project* — no fill, a lime-mark tick, quiet. The native checkbox stays for the keyboard and screen readers, out of sight. The two icons are tokens (`--icon-add`, `--icon-added`, Lucide as CSS masks), so the control needs no extra markup | Owner, 2026-10-11 |
| Radios and checkboxes | **Drawn for the dark theme, never the browser’s white box** (owner, 2026-10-11): a recessed `--well-deep` cell with a `--control-edge` border (`#7C7F74`, added for WCAG 1.4.11 — a control’s boundary needs 3:1; `--line-strong` gave 1.6). Checked: a checkbox fills with lime and carries the `--glyph-check` tick in `--on-lime`; a radio becomes a lime ring with a lime dot. Hover lifts the edge, focus is the lime ring | Owner, 2026-10-11 |
| Empty and error states | **One tile everywhere** (owner, 2026-10-11): a neutral 48 px tile (`--control`), the icon 20 px in `--text-2` — the empty Projects, no match, an empty project, a server error. Not lime, not a problem wash: the sentence carries what happened. A state the wireframe drew without an icon gets one from CSS (`--icon-empty-set`, Lucide *layers*), so no markup changes | Owner, 2026-10-11 |
| Shadow | **Hairlines first; a shadow only where something is lifted over the place under it** (stage 7, #9): `--shadow-tile` on the top bar’s current place (one step up, `0 1px 2px`) **and on a segmented control’s lifted segment**, `--shadow-sheet` under a dialog **or the Filters popover** over a mode. Rows and panels carry **no drop shadow** — Linear’s *border and a whisper of tone* (references.md, A). **A row’s cut-out carries an inward one, `--shadow-cutout`** (a hairline and a 1–2 px inner shade): it is the *pressed in* of the owner’s cut-out, not a lift. *Phase 07: this row read "rows carry none", and the mockups draw the inward shade on every row* | Linear base; pair 4; owner, round 4 (the cut-out) |
| Radius | **Soft, not round** (stage 7, #10): 6 on a control, 10 on a row’s cut-out and a box inside it, 14 on a panel, a tray, **a card and a dialog**, 18 on the acrylic frame, a pill on a tag. The cut-out form is the owner’s, from round 2’s *Kit*; the step grows with the size of the thing, so nesting reads. *Phase 07: 18 appears only on the stand. The mockups have no acrylic frame round the Export mode (see* Phase 07 — reconciled with the mockups*)* | Owner, round 4 |
| Warning | **`Export with 1 problem` is drawn in warning amber** (`--warning #EFA23A`, dark text 8.8:1; light `#9C5800` with white, 5.5:1) — the cost of going ahead is visible, never celebrated in lime (owner, stage 7, #11) | Owner, 2026-10-11; voice.md principle 2 |
| Destructive action | **A red button, `--danger #D4363F` with white text (4.8:1)**, only on an act that removes something: *Remove from project* in its dialog. **Inside a Problem the remove is muted** — a ghost button, red text and a red-tinted edge, filled only on hover — because there it is one way out, not the loudest thing on the screen; the solid red is kept for the confirmation | Owner, 2026-10-11 |
| Icons | **Lucide**, ISC, 1.75 px stroke, one style. **Replaces Fluent (owner, 2026-10-11)** | Owner, round 4 |
| Density | Between Default and Comfortable: body 14.5 px, small 13, ~~rows 11 px vertical padding, buttons 33 px~~ **rows 12 px vertical padding, controls 32 px** — *phase 07: the values the mockups draw, on the 4 px scale (`--s3`, `--control-h`); 11 and 33 were stage-3 values from before the scale* | Owner, round 3; the 4 px scale (polish) |
| Rows | Each item in its own rounded cut-out; auto-added items inside the parent's, behind a dashed rule | Owner, round 4 (Kit's form) |
| Findings on a row | **No coloured ring round the row**, and no outline round a selected row | Owner, 2026-10-11 |

| Navigation | **Top bar (N1)** — the three places in one line across the top | Owner, 2026-10-11 |
| Active row | **A short lime pill at the left edge of the cut-out, the cut-out one step lighter (S2)** — Fluent's selection indicator | Owner, 2026-10-11 |
| Findings on a row | **A tinted tag with the icon and the word (F1)**: Problem and Note as capsules on the right, `Conflict` as a tag beside the name | Owner, 2026-10-11 |

| Current place in the top bar | **A raised tile ~~, its icon in lime~~ with the tile shadow, its label in `--text`; the other places sit on no track and wash on hover** (T2 without its track). The round-4 look — a tile with a lime underline — was turned down. *Phase 07: the places in the mockups carry no icons (the wireframes give them none), so there is no lime icon to draw; the tile alone marks the place* | Owner, 2026-10-11; the wireframes’ markup |
| Product mark | **A 14 px lime square before *AI Stack Builder***, the one lime that is neither an action nor a place. *Phase 07: drawn on every mockup and never written down. It is the brand’s single mark, so pair 5 holds: it claims whose product this is, nothing about state* | The mockups; pair 5 |
| One primary per screen | **When an empty or error state carries its own primary, the head’s primary drops to secondary** (stage 5 critique). *Phase 07: carried into this table from stage 5’s prose* | Pair 5; stage 5 |
| Skipped stage | **A Skipped stage has no fill and a dashed `--line-strong` outline**, the result Lucide `ban` in `--text-3` — the check had nothing to check, so its row is drawn as absent rather than passed. *Phase 07: drawn in the mockups, not written down until now* | §6 (Skipped); D1-B |
| Finding capsules | **Problem and Note capsules are a wash and a coloured word with its icon (`circle-alert`, `info`), with no edge**; the `Conflict` tag and the Problem and Note **boxes** do carry an edge. *Phase 07: the polish rule "every boxed object has a visible edge" is about a box holding inset text; a 24 px capsule is held by its wash* | Pair 1; polish |

**Polished on 2026-10-11** (impeccable *polish*): the style was drawn out of three generators' stylesheets layered
on top of each other, so one component had several values. `tools/build_lime.py` now writes it as **one stylesheet in
tokens** — spacing on a 4 px scale (4 · 8 · 12 · 16 · 20 · 24 · 32 · 40), six type roles (display 28/34 · title 20/26 ·
heading 16/22 · body 14.5/21 · small 13/19 · micro 12/16), six radii (4 · 6 · 10 · 14 · 18 · pill), seventeen colours
each with its contrast, and drawn states for buttons, places and rows. **Lowest text contrast on the page: 5.3:1**
(`--text-3` on a secondary button); `--text-3` was raised from `#9C9F95` to `#A1A49A` for it. **Every boxed object has a visible edge** (tags as outlines, callouts and the code block edged): an object whose fill disappears into its surface makes its inset text read as a broken left edge.

**Nothing in the working style is open any more.** [`mica-lime.html`](mica-lime.html) shows the fixed screen and the
Export mode; it is the input to stage 4 (`tokens.css` and the stand).

---

## Stage 4 — the stand and the tokens

**Built 2026-10-11.** From the working style above, three files and one measurement:

- **[`tokens.css`](tokens.css)** — every colour, type role, radius, spacing step, shadow, material and size of
  *Mica · Lime*, 117 custom properties, written by `tools/concept_tokens.py`. **Each colour carries the attribute or
  decision it follows from**, in a comment beside it. A `.theme-light` block holds the light slice.
- **[`concept.html`](concept.html)** — the stand: the style in use (a shared project’s card with Maya Chen’s portrait,
  the top bar, rows, buttons, the Export head), then colour by role with its reason, the type pair and its nine-step
  scale, form (radius · spacing · shadow), Lucide icons in three uses, three components — **the item row**, **a stage
  of the check**, **a field** — the light slice, and the contrast table. Built by `tools/build_concept.py`.
- **[`mica-lime.html`](mica-lime.html)** — the screens, now on `tokens.css` too.
- **[`contrast.md`](contrast.md)** — `tools/contrast.py` reads `tokens.css` as written, resolves the colour-mix boxes,
  and checks 31 text-on-surface pairs in dark and 31 in light. **All 62 pass AA.**

**No page holds a value of its own.** The components (`tools/concept_ui.py`) and both pages’ CSS use `var()` only;
`python tools/concept_ui.py --check` lists any literal colour, px size or font name (none — even hairlines are
`--hairline`). The one exception is the 1100 px breakpoint, because a media query cannot read a custom property.

**What the measurement changed** — the reason to measure rather than eyeball:
- `--danger-hover` was lighter than `--danger` and dropped white text to 3.99:1. **Hover on a red button darkens**:
  `#BE2E37`, 5.78:1.
- **In light, lime as a mark vanishes** — the current place’s icon and the active row’s pill measured 1.12:1 and
  1.32:1. Light gets its own **`--lime-mark #55700F`** (4.8:1 and 5.7:1); the primary button keeps the lime fill,
  where dark text on it is 13.5:1. This is exactly the risk the light slice was put in stage 4 to catch.

**And one defect the eye caught that the script could not** (owner, 2026-10-11): hovering a row in the light slice
turned it dark grey. Tokens built from colours (`--hover-wash`, the finding boxes, the shadows) were declared on
`:root` only, and a `var()` inside a custom property resolves **where it is declared** — so light inherited the dark
results. They now live in a `:root, .theme-light` block and recompute per theme. A row’s hover is its own opaque
`--row-hover`, half a step from the cut-out towards `--raised`. **The active row’s lime pill now runs the whole height
of the item**, inset by `--s3`, not only beside its title.

**Colour roles, as the stand names them.** *Primary* is lime — the only colour that invites an action. *Accent* is the
same lime used as a mark (`--lime-mark`), not a second hue: the product holds colour back (pair 5). *Neutrals* are the
Mica layers. *States*: Problem, Note, Skipped — and **no success colour**: the best a check says is *Checked*, a quiet
dot (D1-B). Red is reserved for an act that removes something.

---

## Stage 5 — mockups of the main job

**Started 2026-10-11.** The owner kept the wireframes and asked for a design twin instead of a repaint: the viewer is
renamed **Wireframes and mockups** and carries a **Wireframe / Design** switch, so any screen or flow step that has a
mockup opens in the working style with one click. **Scope, owner's call: the main job first** — Projects, Project and
Run, **every state of each** (22 pages; the first pass drew only four states of Project and the owner caught it — a screen
is drawn whole or not at all), and the flow `main-success` (7 steps). `?mode=design#<page>` opens the viewer straight on a
mockup. *Stop sharing* joins *Remove* and *Delete* as a destructive confirmation (red); the Filters popover hangs from its
button on the same acrylic edge as a dialog.

**How.** `tools/build_mockups.py` reads each wireframe page and writes `04-wireframes/mockups/<page>.html`:
- **the same markup and the same words.** Only the stylesheet changes, to `mockup.css` + `06-concept/tokens.css`;
- **grey placeholders become material**: every `.icon` gets the Lucide icon its label asks for (*New project* → plus,
  *Export…* → upload, *Load again* → refresh, a search → search, the back link → arrow…), the avatar the portrait, the
  empty state's image a `folder-plus` tile, the error state's icon `cloud-off` / `search-x` on a problem wash;
- **a class is added only where the structure cannot carry a tone**: the `Conflict` tag (problem), a primary button
  that removes something (danger). `callout` is a Problem and `callout-quiet` a Note in every wireframe, so their tone
  is read from structure;
- **`mockup.css` holds no value of its own** — the build refuses to write it otherwise. New layout columns were added to
  `tokens.css` (`--col-*`, `--side-w`, `--sheet-w`, `--modal-w`, `--measure`): 128 tokens now.
- **New colour pairs were measured**: placeholder, state sentence, inline code, error code, the Conflict/Problem and Note
  tags over their washes, the error tile, the empty-state illustration — **8 pairs × 2 themes, all AA** (`contrast.md`).

**`/impeccable critique`, dual-agent, 29/40.** What was fixed in the stylesheet and the generator, never in the words:
- **broken:** the error and no-match state icon was crushed by a specificity clash → its own rule;
- **colour lying:** stage 01 *Requirements* wore the Note glyph in every wireframe while the summary counts 2 notes —
  **a wireframe slip**, corrected in the mockups (the wireframe itself is left as drawn);
- **the payoff was flat:** a finished export now carries the lime "you are here" pill and a title-size heading; a failed
  export sits on the problem wash; an export in progress has a spinner;
- one primary per screen (a state's own action wins over the head's); the Problem/Note tags reach the row's edge;
  the error check's summary stacks; error codes in mono everywhere; the breadcrumb is not underlined; `Example` after the
  name; inline code without padding before punctuation; kind tabs on one line; focus rings on the current place, a
  select and a stage.

**Kept, on purpose:** the red `Conflict` tag beside a red `Problem` tag (the owner saw it on the stand and kept it);
project cards of equal height with the last check at the foot (verdicts align across a row); the live actions on
`project-loading` (the wireframe's decision, not the style's). **Detector leftovers judged not defects:** heading levels
and em dashes come from the wireframes and `microcopy.md`; "flat type hierarchy" counts row headings at body size; the
skeleton's even rhythm is intended; the success box's "cramped" edge is its lime pill. **Responsive is phase 10**: at
390 px the pages overflow, as the wireframes do.

---

## Stage 7 — the check

**Run 2026-10-11.** Every page drawn in the style — `concept.html`, `mica-lime.html`, 22 mockups and 7 flow steps — was
checked against this file by two measuring agents (computed contrast on every text node, component values compared
within a page, icons, images, literal values) and **`/impeccable audit`: 13/20** (accessibility 3, performance 3, theming
3, responsive 1 — lesson 10 — integrity 3). **29 problems, each with its evidence**, went to the owner first; four
needed a decision, the rest were done in the order *tokens → generator → stand and screens → docs*.

**The owner’s four decisions.** #11 — `Export with 1 problem` gets its own **warning** colour (a new token family).
#19 — the panel’s `+ Add` gets an accessible name, *Add code-style* / *code-style, in this project*. **#22 and #23 — no
hidden h2 and no skip link for now**: both would add markup the wireframes do not have. #29 — the empty project reads
*Add items from the left* (the panel adds with buttons, not ticks). **And one more, mid-check: `Export` loses its
ellipsis everywhere** — Q38 in the register, over Q36’s `Export…`.

**What was fixed, by kind:**
- **focus and motion:** behind an open dialog or the Filters popover everything is `inert`, so Tab starts in it
  (WCAG 2.4.3, 2.4.11); the export spinner stops under reduced motion; the search input fills its box; the back link and
  *Clear filters* are full targets;
- **values only from tokens:** animation durations (`--dur-spin`, `--dur-shimmer`), a wide measure for lead text
  (`--measure-wide` instead of `88ch`–`96ch`), the stage name column (`--stage-name-w 300px`, so *SETUP.md — for the agent
  that opens it* stays one line), the skeletons’ 164 inline px re-expressed in spacing tokens by the generator, the
  stand’s contrast samples drawn from `var()` instead of pasted hex;
- **one element, one set of values:** the muted remove and the dialog’s red confirm carry their classes
  (`button-danger-quiet`, `danger`) instead of being styled by where they sit; the label specimen is in its own tone;
- **layout:** the Note in the share dialog has its gap; the Export frame on `mica-lime.html` is no longer cut off; code
  scrolls instead of breaking mid-flag;
- **integrity:** 52 links to pages with no mockup now open the wireframe; each screen on `mica-lime.html` is a region, not
  a second `<main>`; sprites carry only the symbols a page uses (stand 105 → 85 KB, screens 70 → 47 KB); the portrait is
  stored in the repo (`06-concept/img/`) instead of hotlinked; the stale *error tile* contrast row is replaced.

**Contrast after the check: 88 pairs (44 dark, 44 light), all AA** (`contrast.md`). **Left on purpose:** the 1100 px
breakpoint on the stand (a media query cannot read a custom property — the one literal); responsive at 390 px
(lesson 10); detector notes that are content or wireframe structure (em dashes, heading order, Geist as overused —
the owner’s font).


---

## Phase 07 — reconciled with the mockups

**2026-10-19.** `DESIGN.md` was generated at the root by `/impeccable document` from the 22 mockups of the main
job (`04-wireframes/mockups/`) and `tokens.css`, North Star **"The Inspector's Report"** (pair 1, voice.md
principle 1; owner's pick), components **quiet and exact**. The mockups are the truth, so this file now follows them.
Where it lagged, the *Working style* table was corrected in place, each change marked *Phase 07*:
- **Density:** rows 12, controls 32. These were 11 and 33 before the 4 px scale.
- **Current place:** a raised tile with the tile shadow. There is no lime icon, because the places
  have no icons.
- **Shadow:** a row's cut-out has an inward shadow; the segment and the popover are lifted.
- **Radius:** a card and a dialog are 14. The 18 frame exists only on the stand.
- **Four rows that were drawn but never written down:** the product mark, one primary per screen, the
  Skipped stage, and finding capsules without an edge.

**Two things in the mockups looked as if they disagreed with the owner's own words, and were not written in.** The
owner decides:

1. **Glass is almost gone from the mockups.**
   - *Designer's taste* says Teams/Slack glass is *the product's signature touch. It should be
     noticeable, but used sparingly*, and the working style puts acrylic round the Export mode and a
     dialog.
   - In the mockups, **Run (Export) is an opaque full-screen mode with no acrylic frame**. A dialog and
     the Filters popover keep only an 8 px translucent lime-tinted edge **with no blur**, because
     `mockup.css` has no `backdrop-filter`.
   - The stand (`concept.html`, `mica-lime.html`) has the blurred frame. So the signature lives on the
     stand and not in the product.
   - **Owner, 2026-10-19: kept as it is in the mockups for now.** In the product, glass is the 8 px
     translucent edge of a dialog and of the Filters popover. It has no blur, and Run has no frame.
     The stand's blurred frame stays as the phase-06 record. *Not closed for good: "for now" is the
     owner's word.*
2. ~~**The active row draws an outline.**~~ **Not a conflict; I raised it wrongly** (checked with
   the owner on 2026-10-19, zoomed). Every cut-out has its own hairline edge (`--line`, part of
   `--shadow-cutout`). The active one only brightens that same edge a step, to `--line-strong`, along
   with the raised fill and the lime pill. **There is no extra ring**, and *no outline round a
   selected row* holds.
