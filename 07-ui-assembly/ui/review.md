# Review of every dressed screen, every flow step, and the token chain

**Phase 07, step 8, 2026-10-19** (plan §4–5 in [`../README.md`](../README.md)). This review ran once all 80 pages and
239 flow steps were dressed. Four read-only sub-agents ran in parallel:
- **G01**: groups 0 and 1, 28 pages;
- **G34**: groups 3 and 4, 18 pages, plus regression checks on six painted pages;
- **F**: the flows. Every step was rendered, and every link was walked;
- **B**: the binding of DESIGN.md, `concept.md`, `tokens.css`, `kit.css`, `kit.html` and `inventory.md`.

**76 findings** came in, 3 of them P1. **54 are fixed, 3 are fixed in part (G34-15, B-14, B-15), and 19 are declined
with the reason**, one of which is a question for the owner. Each fix went by the routes in the README.

Before → after:
- **flow links:** 402 broken → **0** (144 checked);
- **flow steps showing the current place:** 0 of 134 → **134 of 134**;
- **contrast pairs:** 88 → **120**, all passing. One real failure was found and fixed: the light theme's focus ring
  was 1.21:1 and now uses `--lime-mark`;
- **guards** (`tools/kit_check.py`): the kit pages' variables and the showcase's words now fail the build.

## Fixed

| # | Sev | What | How |
|---|---|---|---|
| F1–F3 | P1 | Flow steps had the shell's header swapped in. That broke 402 links and three cases, and dropped the current place | `shell(flow=True)`: a flow step keeps the prototype's header, which is checked against the shell by class, not replaced |
| G34-4, G34-5 | P2 | No `SETUP.md` preview or archive tree on the non-project Runs | **Owner: yes.** `tools/review07_handover.py` derives them from the items' fields, in the form of run-default. Copy is in `microcopy.md` as generated rows |
| F4 | P1 | `rj2-auto-added-holds`: removing the puller broke the list's markup | `drop_li` matches the whole `</li>` line. The freed rows go back to *+ Add*. Only these two steps changed; the other 237 are byte-identical |
| G34-1 | P1 | *Stopped* was painted as a Problem on 3 error Runs | wireframes: `glyph-stopped` |
| G34-2 | P1 | The shared item's failed stage was closed | wireframe: `<details open>` |
| F5 | P2 | The sheet's primary lost to an empty state behind it | `PRIORITY`: an open sheet outranks a state block. An open dialog mutes every primary outside it (also G01-10) |
| F6 | P2 | *Adding — …* had no spinner and no `role=status` in the flows | `build_main.facts_line` |
| F7 | P2 | *Stopped* was drawn as *Waiting* in two flows | prototype builders: `glyph-stopped` |
| F10 | P3 | The file list's *Remove* overflowed its row | `.file-list .link-button` |
| G34-3 | P2 | The failure summary on three Runs had no `role=alert` | wireframes; the summary now gets `is-failed` |
| G34-6 | P2 | The dead link's tile showed *create folder* | transform: `unlink` |
| G34-7 | P2 | A plain list's wrapped line returned to the dash | kit: the dash hangs |
| G34-10, G01-20 | P3 | Inline code in a state line and in usage was a chip | kit: bare, as in facts |
| G34-15a | P3 | The `·` sat inside the mono number of `11 · Export` | transform |
| G01-1 | P2 | `inert` was written inside an attribute; the tabs behind the popover stayed live | transform `inert_behind` |
| G01-2, G01-19 | P2 | The Item sheet took the library's height, so Save sat below the fold | kit: `dialog.sheet` is fixed to the viewport and its body scrolls |
| G01-3 | P2 | The native select list would open light | kit: `color-scheme: dark` |
| G01-4 | P2 | A loading skeleton was painted as a Note | transform: neutral |
| G01-5 | P2 | Mono tokens broke mid-token in usage and callouts | kit: `nowrap` |
| G01-6 | P2 | Machine text was set in sans: file names, the 503 line, the Name field | transform: `.json`/`.md`/`.zip` names in `code`; any `NNN · ` line is `error-code`; `field-mono` on Name |
| G01-7, B-24 | P2 | The Item sheet and the small heading were missing from `kit.html` | `kit.html`: *One-off, styled in the kit* (5 entries); DESIGN.md prose |
| G01-12 | P3 | The Filters popover ran past the viewport | kit: `.popover-body` scrolls |
| G01-13 | P3 | Placeholders were clipped | copy (`microcopy.md`, *Phase 07 — the review*) |
| G01-14, -16 | P3 | Sign up lost the typed email and used `current-password`; fields stayed editable while busy | wireframes |
| G01-18, B-21 | P3 | No hover on title links, links in callouts, or filter rows | kit |
| B-1 | P2 | `kit.html` read `--canvas` and `--measure-wide`, which `kit.css` did not declare | `used_root` reads the showcase's styles; guard 4b |
| B-2 | P2 | DESIGN.md's type names were crossed with the tokens' | `title` = 20 (`--t-title`), `heading` = 16 (`--t-heading`) |
| B-3 | P3 | `problem-box` was rounded differently in two documents | `#342A28` in both |
| B-4, B-5, B-13 | P2 | Bare weights (≈25) did not match DESIGN.md's roles | tokens `--weight-regular/medium/strong`; roles *Button Strong* and *Micro Strong* |
| B-6 | P2 | DESIGN.md frontmatter listed 15 components | it lists 39 now, with `lime-mark` and `warning-hover` |
| B-7 | P2 | The sidecar held literals and the old field edge | `build_design_sidecar.py`: variables; shadows and motion read from `tokens.css` |
| B-8 | P2 | 20 class families were undocumented | DESIGN.md: *The frame*, *Item sheet and forms*, *Lists, blocks, smaller parts* |
| B-9 | P3 | Stale and contradictory lines (glass, rose on a wash, the mono label, *22 mockups*) | DESIGN.md |
| B-10 | P2 | Unsigned values: `--ease`, `--dur`, spin, shimmer, tracking, `--s12` | `concept.md`, *Phase 07 — the review's binding fixes* |
| B-11 | P3 | Orphan tokens | `--col-xs` and `--col-s` removed; `--panel-w` and `--canvas` signed as the stand's |
| B-12 | P3 | `concept.md`'s table was stale (Skipped outline, the rose remove, counts) | `concept.md` |
| B-15 (part) | P3 | Literals in `kit.html`'s own styles | `z-index` from tokens, `letter-spacing: normal` |
| B-17 | P2 | Tone was guessed from the glyph inside (`:has`) | transform: `mark-problem/note`, `result-problem/note` |
| B-18 | P3 | A disabled quiet remove turned rose on hover | kit: a disabled control does not answer the pointer |
| B-19, B-20 | P3 | Duplicate `.sheet-head .close`; dead `callout-spaced` | removed |
| B-14 (part) | P3 | `.scope`'s radius computed as `r-sm + s1` | `var(--r-md)` |
| B-23 | P3 | 18 pairs drawn but never measured | added to `contrast.py`. One real failure was found and fixed (above) |
| B-25 | P3 | `kit.html` showed no *Public library* current place; the Run bar showed one state | added; the Run bar is noted as the same in every state |
| B-26 | P3 | Stale inventory lines | `inventory.md`, *Step 7* |
| B-27 | P3 | Guard 8 did not exist; guards 2 and 4 skipped the kit pages | `kit_check.py`: 4b and 8 now fail the build |
| — | — | The blast radius before a save (*Used in 3 projects*) was rose | transform: neutral, like the keys reminder. A disclosure, not a finding. My own pass, before the review |
| — | — | A dialog over the Item sheet was hidden under it | kit: the sheet stacks by order. My own pass |

## Declined, with the reason

| # | Sev | What | Why not |
|---|---|---|---|
| G34-8 | P3 | Export appears twice on the shared project | The head is the mode's control; the aside is the action beside what the machine needs. Only one is primary |
| G34-9 | P3 | Shared rows wash on hover without being links | DESIGN.md: a cut-out moves half a step on hover, everywhere |
| G34-11, -12, -13, -14 | P3 | *Defers to* drawn three ways; machine words in Notes in sans; *shared by* repeated; skeleton shapes | Wireframe content and copy across many lines. Listed for the next copy pass |
| G34-15b | P3 | A demoted *Export with 1 problem* loses its amber | Two filled buttons shouting at once was critique #2. The cost is still named in words |
| G01-8 | P2 | A shared item still reads *Share…* | Q37 decided this for a project only. **Raised for the owner:** does a shared item read *Stop sharing…* too? Nothing changed |
| G01-9, -11, -21, -22, -23 | P3 | Public skeleton shape; filter state vs the list; *requires* in two places; reset copy order; a four-fact usage line | Wireframe content, listed for the next pass |
| G01-15 | P3 | Duplicate recovery actions | The failure box names its own way on; the form keeps its own |
| G01-17 | P3 | Sign up's failure has no code | Its message covers two causes on purpose, so as not to say whether an account exists. A code would say it |
| F8, F9, F11 | P3 | Flow content: a copied description, the head meta while adding, a Run's back target | Prototype content at the light depth `_conventions.md` allows |
| B-14 | P2 | Sizes composed by `calc()` from the scale | They are sums of scale steps. Half steps (2, 3, 6) are optical alignment inside a control. Named in DESIGN.md |
| B-15 | P3 | `linear` on a spin, percentages in a gradient, `50%` centring | Geometry, not design values |
| B-16 | P2 | `.meta`, `.description` and `code` change with context | Painted heritage. Splitting them means new classes on all 80 wireframes. **Lesson 09** (the design system) |
| B-22 | P3 | The fallback icon's offset assumes 48 px padding | No panel state uses the fallback; all seven were measured |

## Owner's questions raised by this review

1. **G01-8:** does a shared *item* read *Stop sharing…*, as Q37 decided for a project?
2. ~~**G34-4/5:** should the single-item Run and the shared Runs carry the `SETUP.md` preview and the archive tree?~~
   **Yes (owner)**, and they do.
