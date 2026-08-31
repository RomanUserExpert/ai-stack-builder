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

## Not captured, and why

**The "publish library update to N files" dialog — the blast-radius UI — could not be reached.**
This file is on a Free team plan, where publishing a library across files is a paid feature; the
Assets panel shows the upsell instead ("Reuse components across files … upgrade to a Professional
plan"). This is a plan limit, not an access limit. Options, in order of cost: check whether another
file of the owner's sits on a paid team; or accept the gap and design blast radius from the
Backstage and GitHub-dependents material in flow 03, which we already hold.
