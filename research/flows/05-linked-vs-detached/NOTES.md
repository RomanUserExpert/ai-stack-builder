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

### The finding that survives

**Nowhere does it say how many instances the update will touch.** Not per component, not in the
bulk action. You are told a new version exists and asked to accept it; you are never told the size
of what you are accepting. Combined with what we already found — that a detached instance keeps no
memory of its origin — the picture is consistent: **Figma never quantifies impact, in either
direction.**

So blast radius remains genuinely unclaimed. Our *"used in 3 projects"* has no prior art in the
tool whose linking model we are otherwise borrowing. The closest working examples stay the ones in
flow 03: Backstage's Catalog Graph with its depth control, and GitHub's dependents view.

### What this changes for our design

- Group our update feed by **source and publish event**, not by item — provenance belongs on the
  header.
- Offer accept-one and accept-all, with accept-all primary.
- Say in words what kind of change it is; a thumbnail is not a diff and sometimes renders empty.
- Default the scope to the current project, with an explicit switch to the whole library.
- And then do the thing Figma does not: **state the count before the user commits.**
