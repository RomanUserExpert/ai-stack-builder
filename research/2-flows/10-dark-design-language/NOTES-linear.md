# Linear's dark theme — captured 2026-09-01

Flow 10 wanted two things from Linear: **its dark palette and typography**, and **its density under
real load**. It got the first. The second is not obtainable here and the note says so.

## Handling

The workspace was set to `System preference`, resolving to light. To capture the dark language the
interface theme was switched to **Dark**, four screens were taken, and the setting was **restored to
`System preference`** — verified in Settings → Preferences → Interface theme, and the app repainted
light. That was the only setting touched, and it was touched with the owner's explicit agreement.

## What could not be captured, and will not be

**Real density under load.** The workspace holds four issues. No theme change fixes that. Linear's
famous list density — dozens of rows, grouped, with inline metadata and hover affordances — needs a
workspace with real work in it. If we still want it, the substitutes named in
[`README.md`](../README.md) stand: `play.grafana.org` and `sandbox.sentry.io`, both open without a
login. Neither has Linear's craft; both have real rows.

**What we did get** is arguably the more useful half for a design system: the palette, the elevation
model, the type scale and the treatment of secondary information, all at close range.

---

## 1. Two greys and a hairline, not a shadow stack

`linear-issues-list-dark.jpg`, `linear-command-palette-dark.jpg`,
`linear-command-palette-dark-detail.png` *(zoomed)*

The whole dark interface runs on very few surfaces:

- **Page ground** — near-black, and the sidebar sits on the *same* ground as the content area. The
  two are separated by a **single hairline rule**, not by a tonal step. There is no "sidebar is
  darker" convention here at all.
- **Raised surface** (the command palette) — a barely lighter grey, a hairline border, and a soft
  shadow. The lift is small enough that the border is doing most of the work.
- **Selected row** — a lighter fill again, no accent colour, no left bar.

The zoomed capture is the useful one: at 1:1 the palette's step above the ground is a few percent of
lightness. **Elevation is communicated by border and a whisper of tone, not by a shadow ramp.** That
is the opposite of the Material instinct and it is why the interface reads as flat and quiet rather
than layered.

## 2. Hierarchy is carried by weight and dimming, almost never by colour

In the dark issue list:

- issue identifiers (`ROM-1`) — dimmed, monospace-ish, tabular
- titles — near-white, medium weight
- group header (`Todo 4`) — the label at normal weight, the **count dimmed beside it**
- dates, avatars, priority glyphs — all dimmed to roughly the same secondary tone

There are effectively **three text tones**: primary, secondary, and the accent used sparingly (the
team's red mark, a single blue-violet on a primary button). Colour is reserved for meaning; everything
structural is greyscale. A design system needs only three or four foreground tokens to reproduce this,
which is a much smaller commitment than it looks.

## 3. Key caps are a first-class component

`linear-command-palette-dark-detail.png`

Every shortcut in the palette renders as a small key-cap chip: slightly lighter fill, hairline border,
tiny type, right-aligned. Chords render as **two caps with a lowercase word between them** —
`N` *then* `P` — so a two-step shortcut is legible as two steps.

Given how much keyboard vocabulary our product will accumulate (six kinds, filters, the validation
pass, export), this is a component to define early rather than improvise: `<Key>` and `<Chord>`.

## 4. Unset properties are verbs, not blanks

`linear-issue-detail-dark.jpg`, `linear-issue-detail-light.jpg`

The issue's property panel does not render empty fields. Where nothing is set, the row **is the action
that sets it**, with an icon and an imperative:

```
Properties    ○ Todo
              ⋯ Set priority
              ⌾ Assign
Labels        ▭ Add label
Project       ⬡ Add to project
```

No `Priority: —`, no `Assignee: Unassigned`. The absence and the affordance are the same row, grouped
under quiet headings.

**Take this whole.** Our item detail carries `requires`, `conflicts`, `needsEnv`, `targetPath`,
`tags` — most of them empty most of the time. They should read `Add requirement`, `Declare a
conflict`, `Add env variable`, not five rows of em-dashes.

## 5. Light and dark are the same layout, not the same colours inverted

The two issue-detail captures are pixel-identical in structure. What changes is the palette — and
notably the light theme is **not white**: it is a warm off-white ground with the same hairline
separators and the same three-tone hierarchy. Neither theme is the negative of the other; both are
built from the same small token set with different values.

That is the argument CLAUDE.md §3 already makes — light is a design decision, not an inversion — and
here is a product that did it properly to point at.

## 6. Straight into the design system

1. **Few surfaces.** Ground, one raised surface, one selected fill. Sidebar shares the ground.
2. **Hairlines over shadows.** Elevation = border + a few percent of lightness.
3. **Three foreground tones**, plus an accent used only for meaning.
4. **`<Key>` and `<Chord>` as real components**, defined before the shortcuts multiply.
5. **Empty property rows are imperatives.**
6. **Two themes, one token set** — not an inversion.
