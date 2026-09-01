# Visibility and portfolio — captured 2026-08-31

From the owner's signed-in GitHub and Notion. Nothing was changed; the GitHub Danger Zone was
photographed, not touched.

## Notion — publish to web

`notion-publish-to-web.jpg`

The whole decision is one tab, one preview and one button:

- Tabs **Share | Publish** — invite-people and publish-to-world are separated, which is the right
  split. They are not two values of one dropdown.
- A **live preview of the published page** rendered inside the dialog, so you see what strangers
  would see before you decide.
- One blue **Publish** button.
- The consequence in plain language underneath: *"When published to web, anyone with the link can
  view this page's content and see contributor names."* Note that it names the second-order leak —
  contributor names — not just the content.

That last sentence is the model for our `visibility` copy. Ours has an equivalent second-order leak
to name: a public project exposes the names and descriptions of the items in it, and whatever an
inline item's content contains.

## Notion — share

`notion-share-dialog.jpg`

Invite field, per-person access level ("Full access"), and **General access: "Only people invited"**
as a single dropdown with a lock glyph. The default state is stated as a phrase, not a toggle.

*Contains the owner's email address — it is their own account, and this repository is private.*

## GitHub — visibility lives in the Danger Zone

`github-danger-zone-visibility.jpg`

Five rows, ordered by how bad the mistake would be: change visibility, disable branch protection,
transfer ownership, archive, delete. Each row is a title, one line of plain consequence, and a
red-outlined button on the right. The visibility row reads: *"Change repository visibility — This
repository is currently private."*

Two things to take. First, **the current state is stated in the row itself**, so the button never
has to be read as a toggle. Second, the severity is carried by grouping and by outline weight —
these are all outlined buttons, not filled ones. Nothing here shouts; the section heading does the
shouting once.

## GitHub — profile as portfolio

`github-own-profile-portfolio.jpg` (the owner's), `github-profile-as-portfolio.png` (a heavily used
public profile, for contrast)

Pinned "Popular repositories" cards, each carrying a **Public** badge, a language dot and a
description; then the contribution graph; then activity. Visibility is a small grey pill on the
card, never a separate screen — it is metadata, not a setting you visit.

The contrast between the two captures is the useful part: the same layout reads as a portfolio when
it is full and as an empty template when it is not. Our profile ambition inherits that risk
directly, which is another argument for the cold-start work being a product problem rather than a
demo problem.
