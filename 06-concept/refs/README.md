# refs — the idea base for phase 06

**Collected 2026-10-08.** A wider pool than [`../references.md`](../references.md), which is the
**decision**: one base and named devices. This folder is **the material**, so later stages can point at
a file instead of a memory. *A file here is a reference, never an asset*: every screenshot is someone
else's product.

- **`lazyweb-*.jpg`** (4): found through the Lazyweb MCP for stage 1. The Linear and Vercel ones are
  Mobbin captures, and the Vercel ones date from 2023.
- **`web/`** (57): taken by [`tools/capture_refs.py`](../../tools/capture_refs.py), public pages only,
  no sign-in, 1440×900, `prefers-color-scheme: dark`. **`web/manifest.json` records the source URL of
  every file**, and its capture date.
  - 36 **screenshots** of pages (`shots`, `more`).
  - 21 images **harvested** from changelogs (`harvest`, `deep`). The harvest kept only images ≥ 600 px
    wide. **Pruned by hand**: release-cover art (Raycast, most of Resend), a logo and a YouTube tile.
    Linear serves AVIF under `.png`. The script now converts that to PNG on download.

Re-run with `python tools/capture_refs.py shots|more|harvest|deep [name …]`.

**What did not work, so nobody tries it again blind.**
- **Sentry's sandbox** sits behind an email gate. The shot was removed.
- **Primer's docs ignore the dark scheme**, so they are light.
- **Vercel's and GitHub's changelog entries** are mostly text, which is why there are only one or two
  images from each.
- **Supabase's changelog** rendered no images at all.
- **Stripe's dashboard** is not reachable without an account. Stripe stays a gap, as it was in
  `references.md`.

---

## By what it is good for

### A dense list of named things with state: `My library`

| File | What to look at |
|---|---|
| `web/linear-changelog-08.png` | **Initiatives table. Child rows hang off a parent on a thin vertical guide line**, each with a dimmed second line of description. Counts read `42 / 68` beside a small glyph. **This is our nesting of auto-added rows under the item that pulled them in (Q33)**, already drawn by someone else. Colour lives only in the 16 px icons and the health glyph |
| `web/linear-changelog-02.png` | Labels as **a coloured dot plus the word**: `● QA Pass`, `● Human review`, `● QA Fail`. Section heads are dimmed and sit above their lists. A status uses **a ring glyph, part-filled**. Panels are separated by tone alone |
| `lazyweb-linear-issues-dark.jpg` | Grouped issue list. Each group head has a dimmed count. Chips are grey with a dot |
| `web/linear-changelog-04.png`, `-10.png` | Inbox and activity feed. A time column on the right. Older entries are dimmed rather than hidden |
| `web/github-issues-labels.jpg` | Issue rows with **coloured labels inline after the title**, metadata on a second dimmed line, and `Open 1,078 · Closed 24,444` counts as tabs |
| `web/github-pulls.jpg` | The same shape for pull requests. The status icon sits left of the title, and a comment count is pushed to the right edge |
| `web/raycast-store.jpg`, `lazyweb-raycast-store.jpg` | Two-column cards. The single action is top-right. A metadata footer reads `author · ◎ 9 Commands · ⊙ 359,272` |
| `web/vercel-templates.jpg`, `web/vercel-marketplace.jpg` | A filter sidebar of checkboxes next to a card grid. **A category tag sits top-right on each card** |

### One item, in detail: the item side panel and `Shared item`

| File | What to look at |
|---|---|
| `web/raycast-extension-linear.jpg` | One extension: icon, name, one-line description, then **a metadata row**: author · `402,404 Installs` · `AI Extension`. Tabs: `Overview · Commands · Version History`. Contributors are listed on the right. **The closest shape to our shared item page** |
| `web/github-releases.jpg` | A release. Its **tag is a mono chip, its commit hash sits next to it**, and a `Latest` badge marks the current one. Assets are listed with sizes. This is what our pinned `ref` plus licence line wants to look like |
| `web/github-repo-code.jpg` | Repo home. The About panel on the right lists **licence, stars, forks and releases as quiet facts, each with an icon** |
| `web/tessl-registry.jpg` | **Tessl**, a registry the research named. A green mono eyebrow (`SKILLS REGISTRY`). Search carries a `Ctrl K` key cap. **A CLI equivalent sits under the search in mono, with a copy button** (`npx tessl search`). **Their pitch, "Evaluated, secured", is the score §5 refuses.** Read it as the thing we are not |
| `web/smithery-home.jpg` | **Smithery**: cards carry `9.18k uses`. A banner reads ***"Smithery is now a part of Arcade.dev"*** — market news as of 2026-10-08, worth a line in the register |

### A check that runs in stages: `Run`

| File | What to look at |
|---|---|
| `web/github-run-summary.jpg` | Run summary. **A head row of labelled facts**: `Status Failure · Total duration 27m 18s · Artifacts 138`. Jobs are listed on the left with a glyph each, and the failed job is expanded |
| `web/github-job-failed.jpg` | A failed job's steps. **`⊘` marks skipped steps beside `✓` passed ones**, and a `BACKGROUND` capsule tags one step. This is device C1 in `references.md` |
| `web/github-pr-checks.jpg` | Checks grouped by workflow. Each group has a count, and each check has a glyph |
| `web/github-changelog-01.png` | **A merge stack: items joined by a vertical connector line, each line tinted by the item's state.** `Ready` and `Merged` are **tinted pills**: a low-alpha fill with coloured text, not a solid fill. **A blue left bar marks the selected row.** The primary button carries a count (`Merge stack 2`). Good material for a `requires` chain |
| `lazyweb-vercel-deployment-status.jpg` | Vercel, 2023: a failed build. A **`Build Failed` card with a red hairline border**. The log has filter chips `All Logs (21) · Errors (2) · Warnings (1)` |
| `web/geist-status-dot.jpg` | Geist's status dot: `Queued · Building · Error · Ready`, **dot plus label** (device B2) |
| `web/geist-note.jpg` | Geist's `Note`: an inline message in a hairline box with an icon, at several sizes. A candidate shape for our *Note* findings |

### The system underneath: tokens, type, materials

| File | What to look at |
|---|---|
| `web/geist-colors.jpg` | **10-step scales per hue** (grey, grey-alpha, blue, red, amber, green). Backgrounds are a separate pair |
| `web/geist-materials.jpg` | Named materials: **radius 6 px** (base, small) and **12 px** (medium, large) |
| `web/geist-typography.jpg` | Type as named presets (`text-copy-16`, `heading-72`), plus *Subtle* and *Strong* modifiers |
| `web/geist-badge.jpg` | Badges: solid and subtle variants per hue |
| `web/geist-keyboard-input.jpg` | Key caps: modifiers, combinations, sizes |
| `web/geist-table.jpg`, `web/geist-entity.jpg`, `web/geist-empty-state.jpg`, `web/geist-button.jpg`, `web/geist-icons.jpg` | Table, the two-column *entity* row (content left, controls right), empty-state framework, button sizes, the icon set |
| `web/primer-label.jpg`, `primer-state-label.jpg`, `primer-counter-label.jpg`, `primer-timeline.jpg`, `primer-color.jpg` | GitHub's Primer. `StateLabel` is a pill with an icon (`Open`). `CounterLabel` is the count capsule (device C2). `Timeline` is a vertical line with nodes. Colour roles: fg, accent, attention, danger. **Light only**, see above |

### Tone and mood: not product UI, kept for contrast

| File | What to look at |
|---|---|
| `web/linear-home.jpg`, `web/linear-method.jpg` | Linear's marketing. Product UI rendered as a dark slab. **A serif display face on `/method`**: Linear uses a serif when it talks about ideas, not in the product |
| `web/raycast-home.jpg` | Raycast's red ribbons. `references.md` explains why this is refused |
| `web/resend-changelog-01.jpg`, `-07.jpg` | Resend's changelog covers: **serif display type on near-black, glossy 3D objects, and code in a panel.** A strong marketing voice, and a useful anti-reference for the product: the product is not a launch page |
| `web/railway-changelog-01.webp` | A CLI's `--help` output rendered as an image. Mono typography as a first-class surface |
| `web/cursor-changelog-01..05.png` | Cursor: settings rows with toggles, a security-review card, a machines table with **thin usage bars**, a run-on menu. **Light and dark both appear.** A data point for Q: light theme |
| `web/grafana-play.jpg` | Grafana Play. **Shown as the other end of the scale**: the busy, colourful dashboard that §3 calls *generic dashboard aesthetics* |
| `web/vercel-changelog-01.png` | A rule builder: filter rows of `field · operator · value`. Relevant later to the `Filters` popover (Q30) |

---

## What the wider pool adds to `references.md`

**Nothing is adopted here.** Stage 4 decides, and anything it adopts goes into `concept.md` with its
reason. These are **candidates** the first pass did not have, each with the file that shows it:

1. **The nesting line.** Auto-added rows hang off their puller on a thin vertical guide
   (`linear-changelog-08`). Q33 decided the nesting and no reference drew it until now.
2. **The tinted pill against the dot-and-word.** GitHub's `Ready` and `Merged` pills
   (`github-changelog-01`) versus Vercel's `● Ready`. **The dot is quieter and does not read as a
   seal**, which is why B2 chose it. The tinted pill is the fallback if a dot proves too small at our
   density. Decide on a built row in stage 5, not here.
3. **A CLI line under the search** (`tessl-registry`). Our archive is opened by an agent and its
   readers live in terminals. A copyable command beside a human control fits principle 5 of `voice.md`
   (*write for whoever acts next*). **Copy is the owner's call. This is only the shape.**
4. **A head row of labelled facts** (`github-run-summary`: `Status · Total duration · Artifacts`).
   It is the same idea as our `Checked just now · 1 problem · 2 notes · 1 skipped`, laid out as
   label-over-value columns.
5. **Serif for ideas, sans for the product** (`linear-method`). That holds only if the owner's taste
   points that way. Recorded so it is not lost, not proposed.
