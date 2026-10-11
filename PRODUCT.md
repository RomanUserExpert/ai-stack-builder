# Product

<!-- impeccable:product-schema 1 -->

> **A digest, never a source of truth.** Written 2026-10-11 so the impeccable skill has the product
> record it expects. **[`CLAUDE.md`](CLAUDE.md) is the spec**; where this file and it disagree, it
> wins and this file is corrected. Nothing here is new: every line is taken from `CLAUDE.md`,
> `02-personas-jtbd/` or `05-tone-of-voice/voice.md`.

## Platform

web

## Users

- **Primary: the collector** (`CLAUDE.md` §3, Q7). An AI practitioner, a design engineer or an AI
  engineer, 25+, who keeps a corpus of their own building blocks: skills, agents, system prompts,
  MCP servers, scripts and mini-apps. **11 to 48 items, counted** (`personas.md` P1). Design for
  fifty, not for thirty.
- **The receiver** opens a shared link, owns nothing, and never signs in. **Never observed in the
  first person**, so the surfaces they see get the most conservative treatment (§8, Q20).
- **The empty-handed** starts with an empty `My library` and the public library. Mostly `[?]`.
- **The agent** that opens the exported archive and reads `SETUP.md` is a fourth reader of the
  product's words.

## Product Purpose

A workspace where one person keeps their AI building blocks and **assembles them into projects that
export as a ready-to-use archive.** The core value is **assembly with validation**: the product tells
you that a skill needs a particular MCP server, that two items write to the same file, that a command
name is registered twice, that an env key is missing, before runtime does. The "wow" moment is the
export: a working archive in thirty seconds, with the set checked first.

## Positioning

**It checks a set, it never runs one.** Every verdict is *checked*, never *works*. There is no score,
rating, eval result or badge on an item, only usage facts from the person's own library (*used in 3
projects*). Competitors sell measured trust and governance to organisations; this is one person's
library, with the consequence named before every irreversible step.

## Operating Context

- **Desktop-first, dark theme from day one.** Light is a design decision, not an inversion (§3).
  Responsive comes later on purpose.
- The audience lives in Linear, Vercel, Raycast and Figma (§3); **that is the owner's assertion, H11,
  not an observation.**
- Places: `My library`, `Public library`, `Projects`, `Project`, `Shared project`, `Shared item`,
  `Sign in`. Everything else is a mode or an overlay: the configuring mode, the library panel, `Run`
  (the mode `Export…` opens), the item side panel, dialogs.

## Capabilities and Constraints

- Six kinds: `skill`, `agent`, `prompt`, `mcp`, `script`, `app`.
- Three severities: **Problem** (the archive will be wrong), **Note** (correct but incomplete),
  **Skipped** (nothing to check, its own neutral glyph). **Nothing blocks**; an unclean export is
  confirmed with the consequence named.
- Item states in a project: not selected, selected, auto-added (with what pulled it in), conflicting,
  missing an env key, detached (with the differing fields named).
- Sharing by unlisted link; no catalog, no teams, no versioning (§9).
- No UI kits. The design system is custom (§10). Styling engine decided in phase 08.

## Brand Commitments

- **Voice:** [`05-tone-of-voice/voice.md`](05-tone-of-voice/voice.md). Five principles: say what was
  examined, never what it means; name the consequence before the step; own our own failures; counts
  and names, not adjectives; write for whoever acts next. Every line on a screen is in
  [`microcopy.md`](05-tone-of-voice/microcopy.md).
- **Icons:** Microsoft Fluent System Icons, one style, never the colour variant (owner, 2026-10-08).
- **The owner's taste** is in [`06-concept/concept.md`](06-concept/concept.md), *Designer's taste*.
  It is the only input allowed to be a preference.
- **The phase pages' look** ([`DESIGN-artifacts.md`](DESIGN-artifacts.md)) is not the product's and
  is never a source for it.

## Evidence on Hand

- Real content: the 80 wireframe pages in `04-wireframes/pages/`, with every line from `microcopy.md`.
  The example project is `acme-billing-api`; the signed-in person in the wireframes is *Maya Chen*.
- The curated public library is specified (§11) but **not built yet**: no real shelf to show.
- **No photographs belong to the content**: items are files, folders and repos. The only honest
  photograph is a person's portrait (the owner, a sharer).

## Product Principles

1. **Colour and words are claims.** Nothing the product draws may claim what it does not know.
2. **Name the cost before the irreversible step, and never block.**
3. **The set row is the only place an item's state is true.**
4. **A mode is entered and left; a place is where you are.**
5. **Show more, promise less** wherever the reader has never been met.

## Accessibility & Inclusion

WCAG AA contrast, computed by a script, for every colour pair the concept uses (`06-concept/README.md`,
stage 4).
