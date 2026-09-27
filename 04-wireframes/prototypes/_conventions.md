# Prototype conventions — lesson 04

> **Written 2026-09-27.** A clickable prototype is **the wireframes, wired**. Everything in
> [`../_conventions.md`](../_conventions.md) holds unchanged — grey, Inter, 4 px grid, semantic HTML,
> real text, nothing on the canvas the product would not show. **This file adds only what clicking
> needs.** The cases themselves are in [`prototypes.md`](prototypes.md).

---

## 1 · A prototype is made of wireframes, not drawn beside them

- **Every step is a wireframe page**, copied from `pages/` with its links rewired. The structure, the
  zones and the text are the wireframe's; a prototype changes **only what the path needs** — a count
  after a fix, *checked just now* after a check.
- **A step the wireframes do not have is drawn in `pages/` first** or, where the owner has not seen it
  yet, drawn in the case and marked `new` in `prototypes.md`. **A prototype never quietly becomes the
  only place a screen exists.**
- **Two depths** (owner, 2026-09-27). **The main job is built in full**: every count, date and target
  follows the step. **Every other flow is built light**: up to five cases, **the pages as drawn**, and the
  data left as each page has it. The rules below hold at both depths; only the data is allowed to differ.
- **The stylesheet is the wireframes' own**: `../../pages/wireframe.css`. A prototype page carries no
  `<style>`.

## 2 · Files — `prototypes/<flow>-<case>/NN-<screen>-<state>.html`

- **One folder per case**, named `<flow>-<case>` — `main-success`, `main-problem-fixed`. The flow is the
  diagram's name in `flows.md` (`main` for the main job, `rj1`, `rj2`, `item`, `receiver`, …); the case
  says which way the forks went.
- **One file per step**, `NN-<screen>-<state>.html`: a two-digit step number, then the wireframe's own
  name. `03-run-loading.html` is step 3, and it is `run-loading.html` in `pages/`.
- **The name is a page that exists in `pages/`** (Q35) — the same screen and state. **What may differ is
  content**: a different row open, a count after a fix, the example alone on Projects. *A step that shows
  a different state is a new page in `pages/` first, never a step named after its neighbour.*
- **The number is the order, and it allows a screen twice.** A case that comes back to the Project
  after the archive has `02-project-default.html` and `07-project-default.html`, and the two differ in
  exactly what happened between them.
- **Each case is self-contained.** Its links point inside its own folder, so a case can be read, copied
  or deleted without touching another.

## 3 · Links — only the path is live

- **A link that is a step in this case has an `href`** to the next step's file. That is the whole
  mechanism: **no JavaScript in a prototype page**, exactly as in a wireframe.
- **A link that leaves the case is inert** — the `a` stays, with its text and its place, and **loses
  its `href`**. It is still visibly a link; it goes nowhere in this case. *Pointing it at the wireframe
  page would drop the person out of the prototype without telling them.*
- **A `button` stays a `button`.** Where a button is a step — **Check**, **Export**, **Save** — it
  becomes an `a class="button"` with the `href`, which is how the wireframes already draw *Check*.
- **A control that is a step becomes a link around itself** — a panel's *Add* checkbox, the search
  field that is typed into, the agent target. `<label class="check">` becomes `<a class="check">`,
  `<label class="search">` becomes `<a class="search">`, `<label class="pick">` becomes
  `<a class="pick">`, the control stays inside it drawn as it was, and `wireframe.css` makes it
  unclickable so **the click is the link's**. **What the control would have done is drawn on the next
  step**: the box ticked, the text typed, the target chosen. *Added 2026-09-27, when the cases needed
  a tick, a search and a target change.*
- **Exactly one way forward per step.** A page has **one** live link or **one** wait, never two — a
  case is one path, and a second live link would be a fork the case has already answered. The last
  step has none. **The build checks this on every page of every case.**
- **The way back is a step too.** A case ends on a page whose primary action returns somewhere real,
  and that link points at the case's last step, so the ending is visible rather than a dead page.
- **Expanding is not a step.** `details` opens and closes on its own; a stage stack is read by opening
  it, and nothing in the case depends on it.

## 4 · Waits advance by themselves

- **A wait is a page that moves on its own** — `<meta http-equiv="refresh" content="2;url=NN-….html">`.
  HTML, not script. **2 seconds** for the check sweep and the archive build, long enough to read that
  something is happening, short enough not to feel like a demo.
- **A wait is never skipped.** If the flow names it, the case shows it — the check is *a designed
  moment, not a spinner* (§6), and a prototype that jumps over it tests a product without it.
- **A wait can be a whole state or a row.** The check sweep and the archive build take the stage
  stack; **the add's round trip is one row** — *Adding — finding what it requires…* — and what the item
  pulls in arrives on the next step, nested under it (decided 2026-09-26, drawn here first).

## 5 · The viewer

- **Flows sit beside Wireframes in the viewer's sidebar**, as two collapsible groups. Under *Flows*:
  the flow as a folder, **its cases as one row each, with a play icon** — **two levels, never three**
  (owner, 2026-09-27): a case's steps are not listed in the tree; they live only in the row above the
  frame. **A case not built yet reads faint**, the same rule the wireframe tree uses for a page not drawn.
- **The address is `wireframes.html#flow/<flow>-<case>`**, and `#flow/<flow>-<case>/NN-<screen>-<state>`
  for one step of it. The viewer follows the clicks inside the frame and keeps the address in step.
- **Under the title: Persona · Job · Flow** — the case's, from `prototypes.md`. **Under them, the
  steps, as numbers** — `01 02 03 …`, the current one marked, **the step's name as the tooltip** and, for
  the current step, in the title beside the case's name. *Numbers, not names* (owner, 2026-09-27):
  thirteen named steps took three lines and shrank the frame. A step opens from the row, which is how a
  reviewer goes back without the browser's back button.
- **Show hotspots** draws **an orange outline, and nothing else**, around every live link in the frame —
  no fill, so no button changes colour (owner, 2026-09-27). It is the viewer's and never the page's:
  nothing in the prototype's markup changes, and **it is the one place the viewer's accent is drawn over
  the canvas**, because it is chrome laid on top of it rather than part of it. The choice is remembered.
- **The tree is written from the built cases**, with each step's name taken from its page's `<title>` —
  so a step renamed in its page is renamed in the viewer.
