# Linked vs detached — captured from Figma, 2026-08-31

Taken in the owner's own Figma file (STUDINFO) with their access. **The file was not changed.** The
detach was performed to capture the "after" state and undone immediately with Ctrl+Z; the restored
state is recorded in `figma-instance-relinked-after-undo.jpg`.

## What linked looks like

`figma-instance-linked-state.jpg`, `figma-instance-linked-panel-detail.png`

Two channels carry the link, and neither is colour alone:

- **Layers panel** — a diamond glyph ◇ plus the layer name rendered in purple. Sibling frames are a
  `#` glyph in black. You can read "this is an instance" from the tree without selecting anything.
- **Right panel** — the name with a dropdown chevron (swap instance), and directly beneath it the
  provenance line **"From this file ◇"**. Under that, the component's exposed properties
  (`Property 1: 2`).

So the link is stated three times: glyph, colour, and an explicit sentence about where the original
lives. The sentence is the part we do not have in our model yet.

## The vocabulary of the context menu

`figma-instance-context-menu.jpg`

The instance-specific block is exactly three items, in this order:

- **Change variant ›**
- **Reset instance** — throw away local overrides, keep the link
- **Detach instance** `Ctrl+Alt+B` — keep the local state, break the link
- **Main component ›** — go to the original

Reset and Detach are the two halves of the same axis: one discards the overrides, the other
discards the link. Our UI needs both, and they should sit next to each other exactly like this.

## What detached looks like — and the finding

`figma-instance-detached-state.jpg`, `figma-layers-after-detach-detail.png`,
`figma-panel-after-detach-detail.png`

- Layers panel: the diamond becomes a frame glyph, the purple becomes black.
- Right panel: the title is now just **"Frame"**. The "From this file" line is **gone**. The
  component properties are **gone**.

**Figma keeps no memory of where a detached instance came from.** There is no "modified from library
version", no badge, no way back. The link is not weakened, it is erased — the object becomes an
ordinary frame that happens to look like the component.

That matters for us directly. Our data model says a detached `ProjectItem` keeps `itemId` and
records `overrides`, and section 7 of CLAUDE.md asks for a visible relationship to the library
original with "a way back". **That is not a copy of Figma — it is a correction of Figma.** We should
treat it as a deliberate differentiator and design the badge and the return path properly, rather
than looking to Figma for a pattern that does not exist there.

## The library panel

`figma-assets-libraries-panel.jpg`

Local versus external is a flat two-level list: "STUDINFO — Created in this file — 368 components",
then "UI kits — iOS and iPadOS 27 UI Kit — 173 components", then "Add more libraries". Component
counts are shown per library and nothing else — no quality signal, no last-updated. Compare with
Tessl and Smithery, where the count is the least important number on the card.

## Library updates — the receiving end

`figma-manage-libraries-updates.png` — **supplied by the owner from a file on a paid team**, not
captured in this session. It fills the gap the Free-plan file left.

The "Manage libraries" modal, Updates tab. Its structure:

- **Grouped by publish event, not by component.** Each group header is *"Updates from UIR - LIB -
  Design System"* with a sub-line *"Published by Roman 11 days ago"*. Provenance — which library,
  who published, how long ago — sits on the group, and the components sit under it. Four groups are
  visible from two source libraries at two different times.
- **Per-item accept plus bulk accept.** Every component row has its own `Update` button, and the
  footer carries a primary `Update all`. Granularity at both levels, with the bulk action as the
  primary and the individual ones as secondary.
- **A thumbnail per component**, which is a preview rather than a diff — and one of them (`header`)
  renders as an empty grey box, so the preview is not dependable.
- **Structural changes get a sentence.** Under `handler-dropdown`: *"Moved from UIR - LIB - Design
  System"*. When something more than pixels changed, it is stated in words.
- **Scope defaults to the current page**, with a footer toggle *"Show updates for all pages"* that
  is off. The default answer to "what changed" is narrowed to what you are looking at.

### The counts are there — they are tied to the scope toggle

`figma-library-updates-instance-counts.png`

An earlier draft of this note claimed Figma never states how many instances an update will touch.
That was wrong, and the mistake was mine: I read the panel with *"Show updates for all pages"*
**off**, where no counts appear. Switch the toggle **on** and every component row grows a third
line with the number:

| Component | Change | Instances |
|---|---|---|
| `chatting-window-chat` | Moved from UIR - LIB - Design System | **5** |
| `handler-dropdown` | Moved from UIR - LIB - Design System | **2** |
| `dropdown-detailed-item` | — | **70** |
| `tag-ghost` | — | **423** |

So blast radius **is** quantified, and the design decision worth copying is the coupling: the count
appears exactly when the scope widens beyond what you can see. While you are looking at one page,
Figma assumes you can judge the damage yourself; once the action reaches the whole file, it tells
you the size first.

The spread in that table is the argument for the whole feature. `Update all` on this file means
touching two objects in one place and 423 in another, and without the numbers those two rows look
identical. Any bulk accept in our UI has to state its total before it runs, not after.

**What is still not shown is the cross-container number.** These counts are instances *within this
file*. Nothing here says how many other files use `tag-ghost`. That is the shape of our *"used in
3 projects"* — one item, many containers — and it stays uncovered by this panel. Figma's
cross-file usage lives in library analytics on the paid tiers, which we have not seen and should
not describe from memory.

The other half of the finding stands unchanged: a **detached** instance keeps no memory of its
origin. Figma counts what is still linked and forgets what is not.

### What this changes for our design

- Group our update feed by **source and publish event**, not by item — provenance belongs on the
  header.
- Offer accept-one and accept-all, with accept-all primary.
- Say in words what kind of change it is; a thumbnail is not a diff and sometimes renders empty.
- Default the scope to the current project, with an explicit switch to the whole library.
- And then do the thing Figma does not: **state the count before the user commits.**

---

# The third state: linked but locally modified — 2026-09-01

Supplied by the owner from their own file (`UIR - PG - Working file`, component `button-filled` from
`UIR - LIB - Design System`). This was the last gap in the flow: the state **between** a clean
instance and a detached one. Two instances of the same component sit side by side — one untouched,
one with its fill overridden from `surface-container/info/bold/default` to
`surface-container/success/bold/default`.

## The finding: the override is invisible until you ask for it

`figma-instance-clean-panel.png` · `figma-instance-overridden-panel.png`

Put the two panels side by side and **nothing distinguishes them but the fill value itself**:

| Channel | Clean instance | Overridden instance |
|---|---|---|
| Layers panel glyph | purple diamond ◇ | purple diamond ◇ — **identical** |
| Layer name colour | purple | purple — **identical** |
| Right panel title | `button-filled ⌄` | `button-filled ⌄` — **identical** |
| Provenance line | `UIR - LIB - Design System` 📖 | **identical** |
| Component properties | type / case / state / value | **identical** |
| Canvas | — | no badge, no marker, no dot |

The three channels that so carefully announce *"this is an instance"* — glyph, colour, and an explicit
sentence naming the library — say **nothing at all** about *"this instance no longer matches its
main"*. You cannot scan a page and see which instances have drifted. You cannot even tell by selecting
one.

## The only signal is a context menu that grows two rows

`figma-context-menu-clean.png` · `figma-context-menu-overridden-reset.png`

The `…` menu on a **clean** instance:

```
Toggle ready for dev status
Create component        Ctrl+Alt+K
Detach instance         Ctrl+Alt+B
Use as mask             Ctrl+Alt+M
Union / Subtract / Intersect / Exclude / Flatten
```

The same menu on the **overridden** instance is the same list with **two rows inserted**:

```
Detach instance         Ctrl+Alt+B
▸ Reset instance                      ← discard every override
▸ Reset fill                          ← discard this one property
Use as mask             Ctrl+Alt+M
```

That is the entire user-facing evidence that the instance was modified: a menu you have to open, on
an object you have to select first.

## Two halves, and they point opposite ways

**The half to reject.** There is no persistent indicator of drift anywhere — not in the layers tree,
not in the properties panel, not on the canvas. Drift is discoverable one object at a time, by
opening a menu. In a file of any size that is not discoverable at all.

**The half to steal.** The menu is **property-granular and self-labelling**. It does not offer a
generic "reset overrides" — it says **`Reset fill`**, naming the exact property that differs. Reset is
therefore offered at two granularities: the whole instance, or the single property. Which means
**Figma knows precisely which fields were overridden.** The data exists and is accurate. The only
thing missing is showing it.

That reframes the correction recorded on 2026-08-31. It is not that Figma lacks the information about
local modification — it is that Figma **has** the information and surfaces it only on demand, behind
a click, in a menu. The failure is display, not modelling.

## Cross-link: the affordance appears only when it can act

The reset rows do not sit greyed out on a clean instance; they are absent. That is the third product
in this research doing the same thing — Linear's keyboard-hint bar recomputing itself when a search
returns nothing, Linear's empty Projects screen suppressing its toolbar
([`08-empty-state-and-cold-start/NOTES-linear.md`](../08-empty-state-and-cold-start/NOTES-linear.md)),
and Figma hiding a reset that has nothing to reset. Against it stands Vercel, keeping four filter
dropdowns over an empty list ([`07-env-and-secrets/NOTES.md`](../07-env-and-secrets/NOTES.md)).

Three to one. Treat it as settled: **an action that cannot do anything is not shown.**

## What this fixes in our design

Our model already says a detached `ProjectItem` keeps `itemId` and records `overrides`. This capture
sharpens what the UI owes on top of that:

1. **A modified item is legible without being selected.** CLAUDE.md §7 lists state 7 — *detached,
   locally modified* — as a state a card must read unambiguously. Figma proves how easy it is to
   model that state correctly and still never draw it. The card carries the marker; the list is
   scannable.

2. **Name the fields that differ, in the card.** Not "modified" — *"content and targetPath differ from
   the library version"*. Figma's `Reset fill` shows this is cheap: the diff is already known.

3. **Revert at two granularities.** `Reset instance` and `Reset fill` are the right pair: discard
   everything, or discard one field. Our `overrides` object supports exactly this, and both need a
   control.

4. **Keep Reset and Detach adjacent and opposite.** The 2026-08-31 note called them two halves of one
   axis — one discards the overrides and keeps the link, the other discards the link and keeps the
   overrides. This capture confirms Figma places them next to each other, and that Reset appears only
   once there is something to reset.

5. **And the part with no prior art remains ours.** Nothing here is a path back from *detached* to
   *linked*. Figma offers a way to undo overrides while still linked, and no way at all once the link
   is cut. Our return path is still an invention.

**Flow 05 is now fully closed.** Clean, modified and detached are all captured, along with the
library-update modal and its instance counts.
