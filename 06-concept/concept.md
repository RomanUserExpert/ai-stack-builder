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
