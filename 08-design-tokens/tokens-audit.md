# Tokens audit — phase 08, step 1

**Facts, not decisions.** Written 2026-10-28. This file reads `07-ui-assembly/ui/kit.css` and every dressed page: 83
pages in `04-wireframes/mockups/` and 241 flow steps in `mockups/flows/`. It names what each variable is used for and
where. **Nothing is renamed, merged or fixed here.** The decisions are step 2's (`README.md`, *The steps*).

**How it was counted.** `tools/audit_tokens.py` reads every rule in the kit and every class on every page. A rule
counts as standing on a page when the page carries every class in its selector. `:not()`, `:has()` and `:is()` are
ignored. A bare element selector counts wherever that element is. **This is an approximation.** It cannot see whether a
`:hover` or `:focus-visible` ever happens, only that the element that would carry it is on the page. A variable read
only through a composite token, such as `--font` through `--t-body`, stands wherever the composite does. That is why
`--lime` stands on every page: `::selection` reads it through `--lime-selection`. The appendix
is the tool's own output, and the tables above it were written from it.

```
python -X utf8 tools/audit_tokens.py --md     # the appendix
python -X utf8 tools/audit_tokens.py          # every use as JSON
```

---

## 1. The kit in numbers

| | |
|---|---|
| Variables in the kit's `:root` | **110** |
| …of which colours written as hex | **28**, holding **25 distinct values** |
| …of which colours built from other colours or written as `rgba()` (`color-mix`, shadows, material) | **18** |
| …type (families, composites, tracking, weight) | 18 |
| …geometry (space, radius, size, column, z-index) | 38 |
| …icons as masks, motion | 4 + 4 |
| Rules in the kit below `:root` | ~390 |
| Variables declared and read by nothing | ~~**2**: `--canvas`, `--measure-wide`~~ **0**. *Corrected in step 3: the showcase's own frame (`build_kit.PAGE_CSS`, inside `kit.html`) reads both. This audit read the kit's classes only* |
| Hex or `rgb()` written in a class | **0** (guard 1 since phase 07) |
| Hex or `rgb()` written on a page | **0**. The 981 inline icons draw in `currentColor` |
| Literal colours inside tokens | **8**: 7 `rgba()` and one hex inside an SVG |
| Variables in `06-concept/tokens.css` that the kit does not copy | 12: `--acrylic`, `--acrylic-blur`, `--acrylic-edge`, `--veil-dialog`, `--r-xl`, `--panel-w`, `--icon-empty-set`, and the five `--page*` of the stand |

**Two corrections to the plan.** `README.md` says the light slice covers *27 colour variables*. It holds **28
entries**: 25 hex colours and 3 composites (`--shadow-cutout`, `--problem-box`, `--note-box`). **Three hex colours of
the kit have no light value: `--danger`, `--danger-hover` and `--on-danger`.** And it says *9 `rgba()` values*: there
are **7**, in five tokens.

---

## 2. Colour: every variable, where it is read, and the role in each place

*Pages* is pages / flow steps where at least one of its rules stands. A role in **bold** is the variable's main one,
the one its signature in `tokens.css` names. Every other role in the same row is **a second job the variable has been
given**. Those are the rows §4 is about.

### Surfaces

| Variable | Value | Pages | Where (classes) | Role in each place |
|---|---|---|---|---|
| `--ground` | `#1B1C19` | 83 / 241 | `html`, `body`, `.canvas` · inside `--shadow-focus` | **the page's ground** · the gap between an element and its focus ring |
| `--bar` | `#181916` | 83 / 241 | `.app-header`, `.shared-header`, `.run-bar` · `.library-sidebar`, `.library-sidebar .panel-head` | **the top bar** · the library sidebar and its sticky head: the panel of the configuring mode |
| `--tray` | `#232420` | 49 / 123 | `.row-list` · `.state-block` | **the tray under the rows** · the ground of an empty or error state |
| `--cutout` | `#1E1F1B` | 59 / 214 | `.row-list>li` · `.stages>li` · `.callout-reminder`, `.callout-failure` · inside `--problem-box`, `--note-box`, `--row-hover` | **a row's cut-out** · a stage of Run · the neutral box (the keys reminder, our failure) · the base the finding boxes and the row hover are mixed on |
| `--well-deep` | `#161714` | 59 / 157 | `.search` · `.field input`, `.field textarea` · `.dropzone` · `pre.file` · `.scope` · `input[type=checkbox\|radio]` · inside `--segment-hover` | **a code block** · the well of a field (search, input, textarea, dropzone) · the bed of a checkbox or radio · the track of a segmented control · the inner ring of a checked radio (`box-shadow`) |
| `--raised` | `#2A2B27` | 73 / 239 | `.card` · `.drawer` · `.aside-box` · `.export-stage` · `dialog.modal`, `dialog.popover`, `dialog.sheet` · `.row-list>li:has(>.is-selected)` · `.app-nav a[aria-current]` · `.tabs a[aria-current]` · `.skeleton` · inside `--hover-wash`, `--row-hover`, `--segment-hover` | **a panel one step up**: card, drawer, aside, Export stage, every dialog · the selected row · the current place in the top bar · the current tab · the skeleton's base · the colour every hover is mixed towards |
| `--control` | `#2E302A` | 80 / 240 | `button`, `.button` · `.check` · `select` · `button[disabled]` · `.scope a[aria-current]` · `code` · `progress` (track) · `svg.icon.state-icon` | **a secondary control's fill** · a disabled button's fill · the current segment, lifted · an inline code chip · the progress track · the neutral tile of an empty or error state |
| `--control-hover` | `#383A33` | 81 / 240 | `button:hover`, `.check:hover`, `select:hover`, `.remove:hover` · `.skeleton` | **a control under the pointer** · the light band of the skeleton's shimmer |

### Lines and edges

| Variable | Value | Pages | Where (classes) | Role in each place |
|---|---|---|---|---|
| `--line` | `#343630` | 83 / 241 | dividers (`border-top`/`-bottom`): the three bars, `.tabs`, `.drawer-section`, `.drawer-actions`, `.card .verdict`, `.form-section`, `.form-actions`, `.file-list`, `.popover-head`/`-foot`, `.door-alt`, `.library-sidebar` (right) · edges: `.card`, `.drawer`, `.aside-box`, `.stages>li`, `.scope` · `img.avatar` ring · `button[disabled]` edge · inside `--shadow-cutout` | **a hairline divider** · the edge of a panel · the edge of a stage and of a segmented track · the avatar's ring · the edge of a disabled button · the cut-out's inner edge |
| `--line-strong` | `#4A4C44` | 83 / 241 | `button`, `.button`, `.check` · `.tag` (inset) · `.sub-rows` (dashed) · `.export-stage` · `pre.file` · `.card:hover` · `.row-list>li:has(>.is-selected)` · `.scope a[aria-current]` · `.callout-reminder`, `.callout-failure` · `span.glyph-running` (ring) · `::-webkit-scrollbar-thumb`, `scrollbar-color` | **a control's edge** · a tag's outline · the dashed rule between auto-added sub-rows · the edge of the Export stage and of a code block · a card under the pointer · the selected row's edge · the lifted segment's edge · the neutral box's edge · the spinner's track · the scrollbar thumb |
| `--control-edge` | `#7C7F74` | 83 / 241 | `.search`, `.field input`, `.field textarea`, `select`, `.dropzone` (dashed) · `input[type=checkbox\|radio]` · `span.glyph-waiting` · `.stages>li.is-skipped` (dashed outline) · `::-webkit-scrollbar-thumb:hover` | **the 3:1 edge of a field or a checkbox** · the ring of a waiting stage · the dashed outline of a Skipped stage · the scrollbar thumb under the pointer |

### Text

| Variable | Value | Pages | Where (classes) | Role in each place |
|---|---|---|---|---|
| `--text` | `#F3F4EF` | 83 / 241 | `body`, `dialog.*`, `.callout`, `.verdict dd`, field and search input, `code`, `pre.file`, `button` · `strong` inside `.state-line`, `.summary p`, `.export-stage p`, `.state-block`, `.dropzone` · hover and current: `.app-nav a`, `.tabs a`, `.scope a`, `.run-bar .back`, `.meta a`, `.door-alt a`, `.popover-group label` · `.callout-reminder>.severity` | **primary text** · emphasis inside secondary text · a link or a place under the pointer or current · the neutral box's severity word |
| `--text-2` | `#C5C7BE` | 83 / 241 | ~35 rules: `.description`, `.head-meta`, `.drawer-section p`, `.state-block p`, `.summary p`, `.export-stage p`, `.plain-list`, `.usage`, `.state-line`, `.tag`, `.field>span:first-child`, the places at rest (`.app-nav a`, `.tabs a`, `.scope a`), `.link-button`, `.button-quiet` · `button svg.icon` · `svg.glyph-stopped` · `svg.icon.state-icon` · `.check::before` (mask) · `.library-version summary:hover::before` · `input[type=checkbox\|radio]:hover` (**border**) · `.check:has(input:checked)` | **secondary text** · a place at rest · an icon inside a secondary button · the glyph of a stopped stage · the empty state's icon · the *+ Add* glyph · a checkbox's edge under the pointer |
| `--text-3` | `#A1A49A` | 83 / 241 | ~30 rules: `.meta`, `.row .facts`, `.card .facts`, `.verdict dt`, section labels (`.drawer-section h3`, `.stage-group>h2`, `.form-section>h3`, `legend`), `.tabs .count`, `.stages summary .n`, `.time`, the `·` and `–` separators, error codes · placeholders · `.search` (icon) · disabled: `button[disabled]`, its icon, `.check:has(input:disabled)` · waiting stages · glyphs as masks: `.stages summary::after`, `.library-version summary::before`, `.check:has(input:checked:disabled)::before` · `.search:hover`, `.field input:hover`, `.dropzone:hover` (**border**) | **metadata** · a section label · a placeholder · a disabled control's text and icon · a waiting stage · a separator · a chevron · a field's edge under the pointer |

### Lime

| Variable | Value | Pages | Where (classes) | Role in each place |
|---|---|---|---|---|
| `--lime` | `#C6EF5A` | 83 / 241 | `.button-primary` (fill, edge, the busy state's hover) · `input[type=checkbox]:checked`, `input[type=radio]:checked` · `.icon.logo` · inside `--acrylic-dialog`, `--lime-selection` | **the primary action** · a checked checkbox or radio · the product's logo tile · the tint of a dialog's acrylic frame · the tint of selected text |
| `--lime-hover` | `#D3F57A` | 64 / 168 | `.button-primary:hover` | **the primary action under the pointer** |
| `--on-lime` | `#141A08` | 64 / 168 | `.button-primary` text and icon · `.button-primary span.glyph-running` (arc) · inside `--on-lime-track` · **as a literal** inside `--glyph-check` (`%23141A08`) | **text on lime** · the busy spinner on lime · the tick in a checked checkbox |
| `--lime-mark` | `#C6EF5A` | 80 / 240 | `.row-list>li:has(>.is-selected)::before` (pill) · `.export-stage.is-exported::before` (pill) · `.check:has(input:checked)::before` (✓) · `span.glyph-running` (arc) · `progress` value · `.search:focus-within`, `.field input:focus-visible`, `.dropzone:focus-within` (**border**) · inside `--shadow-focus` | **lime as a mark: where you are** (the selected row's pill) · *Exported* · *In this project* · something is running · progress · focus, as an edge and as the ring |

### Findings and their states

| Variable | Value | Pages | Where (classes) | Role in each place |
|---|---|---|---|---|
| `--problem` | `#FF8F98` | 39 / 145 | `.tag-problem`, `.mark-problem`, `svg.glyph-problem`, `.callout>.severity`, `.stages summary .result-problem` · `.button-danger-quiet` · inside `--problem-wash`, `--problem-edge`, `--problem-box` | **a Problem** · the muted remove inside a Problem |
| `--note` | `#F2C661` | 25 / 136 | `.mark-note`, `svg.glyph-note`, `.callout-quiet>.severity`, `.stages summary .result-note` · inside `--note-wash`, `--note-edge`, `--note-box` | **a Note** |
| `--checked` | `#C5C7BE` | 20 / 99 | `span.glyph-checked` | **Checked: the quiet dot** |
| `--skipped` | `#A1A49A` | 18 / 92 | `svg.glyph-skipped` | **Skipped: the slashed circle** |
| `--problem-wash` | `color-mix(--problem 14%, transparent)` | 20 / 72 | `.tag-problem`, `.mark-problem` · `.button-danger-quiet:hover` | **a Problem capsule's fill** · the muted remove under the pointer |
| `--problem-edge` | `color-mix(--problem 38%, transparent)` | 39 / 145 | `.callout`, `.tag-problem` (inset) · `.button-danger-quiet` | **a Problem box's edge** · a `Conflict` tag's edge · the muted remove's edge |
| `--problem-box` | `color-mix(--problem 10%, --cutout)` | 31 / 84 | `.callout` | **a Problem box** |
| `--note-wash` | `color-mix(--note 13%, transparent)` | 13 / 69 | `.mark-note` | **a Note capsule's fill** |
| `--note-edge` | `color-mix(--note 30%, transparent)` | 14 / 69 | `.callout-quiet` | **a Note box's edge** |
| `--note-box` | `color-mix(--note 9%, --cutout)` | 14 / 69 | `.callout-quiet` | **a Note box** |

### Acts that cost something

| Variable | Value | Pages | Where | Role |
|---|---|---|---|---|
| `--warning` | `#EFA23A` | 1 / 2 | `.button-warning` | **going ahead despite a Problem**: *Export with 1 problem* |
| `--warning-hover` | `#E0962E` | 1 / 2 | `.button-warning:hover` | the same, under the pointer |
| `--on-warning` | `#1A1200` | 1 / 2 | `.button-warning` text and icon | text on warning |
| `--danger` | `#D4363F` | 5 / 3 | `.button-danger` | **removing something**, in its confirmation |
| `--danger-hover` | `#BE2E37` | 5 / 3 | `.button-danger:hover` | the same, under the pointer |
| `--on-danger` | `#FFFFFF` | 5 / 3 | `.button-danger` text and icon | text on danger |

### Built from colours: hover, focus, material, shadow

| Variable | Value | Pages | Where | Role in each place |
|---|---|---|---|---|
| `--hover-wash` | `color-mix(--raised 60%, transparent)` | 49 / 136 | `.app-nav a:hover` · `.tabs a:hover` · `.check:has(input:checked):hover` | **a place or a tab under the pointer** · *In this project* under the pointer |
| `--row-hover` | `color-mix(--raised 50%, --cutout)` | 57 / 214 | `.row-list>li:hover` · `.stages details>summary:hover` | **a row under the pointer** · a stage under the pointer |
| `--segment-hover` | `color-mix(--raised 55%, --well-deep)` | 13 / 42 | `.scope a:hover` | **a segment under the pointer** |
| `--lime-selection` | `color-mix(--lime 35%, transparent)` | 83 / 241 | `::selection` | **selected text** |
| `--on-lime-track` | `color-mix(--on-lime 25%, transparent)` | 3 / 8 | `.button-primary span.glyph-running` | **a spinner's track on lime** |
| `--shadow-focus` | `0 0 0 2px --ground, 0 0 0 4px --lime-mark` | 79 / 240 | 11 rules: every `:focus-visible` and `:focus-within` | **keyboard focus** |
| `--shadow-tile` | `0 1px 2px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.04)` | 49 / 136 | `.app-nav a[aria-current]` · `.scope a[aria-current]` | **lifted one step**: the current place, the current segment |
| `--shadow-cutout` | `inset 0 0 0 1px --line, inset 0 1px 2px rgba(0,0,0,.35)` | 37 / 115 | `.row-list>li` | **pressed in**: a row's cut-out |
| `--shadow-sheet` | `0 18px 40px rgba(0,0,0,.35)` | 20 / 22 | `dialog.modal`, `dialog.popover`, `dialog.sheet` | **over the place**: a dialog, a popover, a side sheet |
| `--acrylic-dialog` | `color-mix(--lime 7%, rgba(70,72,66,.45))` | 16 / 16 | `dialog.modal`, `dialog.popover` (as an 8 px spread) | **the glass frame of a dialog** · and of the Filters popover |
| `--sheet-edge` | `rgba(255,255,255,.05)` | 20 / 22 | `dialog.modal`, `dialog.popover` (border) · `dialog.sheet` (left border) | **the edge of an opaque sheet** inside glass, or against the place |
| `--veil` | `rgba(10,11,9,.58)` | 17 / 22 | `.scrim` | **the place behind a mode or a dialog, dimmed** |

---

## 3. Type, geometry, motion, icons

These do not carry a theme, and the course gives geometry no semantic level. **They are listed for the primitive
level and for finding 3**, with one line each. Every use is in the appendix.

| Group | Variables | Read by | Notes for step 2 |
|---|---|---|---|
| Families | `--font`, `--mono` | `--font` only through the eight `--t-*` composites; `--mono` through `--t-code` and four rules that set `font-family` on code inside a heading | `--font` has no direct reader |
| Type composites | `--t-display` · `-title` · `-heading` · `-body` · `-button` · `-small` · `-micro` · `-label` · `-code` | `font:` in ~80 rules | **Each composite writes its size, its line height and its weight as literals**: `600 28px/34px`. The weights repeat `--weight-*` (see 4.3) |
| Tracking | `--track-display`, `-title`, `-heading`, `-label` | always beside their composite | one to one with `--t-display`/`-title`/`-heading`/`-label` |
| Weight | `--weight-regular` 400, `-medium` 500, `-strong` 600 | 25 rules that lighten or bolden a composite | `--weight-medium` has one reader, `.button-danger-quiet` |
| Space | `--s1` 4 · `--s2` 8 · `--s3` 12 · `--s4` 16 · `--s5` 20 · `--s6` 24 · `--s8` 32 · `--s10` 40 · `--s12` 48 | ~240 rules | **Space is also used as size**: `svg.state-icon` is `--s12` square; a stage's grid columns are `--s6` and `--s12`; `progress` is `--s2` high; scrollbars are `--s3` wide. **`--s1` is a unit**: 34 skeleton classes and `.door` multiply it (see 4.3) |
| Radius | `--r-xs` 4 · `--r-sm` 6 · `--r-md` 10 · `--r-lg` 14 · `--r-pill` 999 | ~45 rules | clean: each step is one kind of object (chip · control · row · panel · capsule) |
| Line | `--hairline` 1 | 54 rules | also used as a unit: `calc(var(--hairline) * 2)` for the spinner ring and the link underline, `* -1` for an outline offset, and `* 1` once, which does nothing |
| Control sizes | `--control-h` 32, `--control-h-s` 28, `--tag-h` 20, `--mark-h` 24, `--bar-h` 52 | | **`--mark-h` also sizes the avatar** (`img.avatar` is 24 px because a finding capsule is) |
| Icon sizes | `--icon` 16, `--icon-s` 14, `--icon-l` 20 | | `--icon-s` also sizes the logo tile; `--icon` sizes a checkbox and a stage's chevron column |
| Marks | `--pill-w` 3, `--dot` 6 | the selected row's and the Export stage's pill · the Checked dot | |
| Columns and widths | `--dt-w` 116 · `--stage-name-w` 300 · `--col-m` 200 · `--col-l` 320 · `--col-xl` 360 · `--side-w` 440 · `--sheet-w` 640 · `--modal-w` 520 · `--measure` 640 · `--canvas` 1280 · `--measure-wide` 820 | | **`--canvas` and `--measure-wide` are read by nothing** (they were the stand's). `--col-xl` is both the aside and the popover's width. `--modal-w` is also the empty state's measure |
| Layers | `--z-sticky` 1, `--z-popover` 5 | one rule each | |
| Motion | `--ease`, `--dur` 140 ms, `--dur-spin` 900 ms, `--dur-shimmer` 1400 ms | 13 transitions, the spinner, the skeleton | the skeleton's animation is `ease-in-out` and the spinner's `linear`: **keywords, not `--ease`** (see 4.3) |
| Icons as masks | `--icon-add`, `--icon-added`, `--icon-chevron`, `--glyph-check` | `.check::before`, `.stages summary::after`, `.library-version summary::before`, a checked checkbox | the three masks draw in `black` (a mask, so the colour is irrelevant). **`--glyph-check` is a background, not a mask, and its stroke is `#141A08` written inside the SVG** (see 4.3) |

---

## 4. Findings

### 4.1 Drift: one role written with different values

**The kit has little drift in the course's sense.** Every hex comes from one generator, and guard 5 holds the kit to
`tokens.css` character for character, so *#2E6E5C here, #2F6F5D there* cannot happen. What remains is drift in
**recipes**: one role mixed several ways.

| # | Role | Written as | Signed? | Note |
|---|---|---|---|---|
| D-1 | **something under the pointer, lifted half a step** | `--hover-wash` = `--raised` **60%** over transparent · `--row-hover` = `--raised` **50%** over `--cutout` · `--segment-hover` = `--raised` **55%** over `--well-deep` · `--control-hover` = a hex of its own, `#383A33` | `--row-hover` and `--segment-hover` are signed in `concept.md` (phase 07) as *half a step*. **The 60 / 50 / 55 split is not explained** | Four recipes for one role, and each differs because of the ground under it. **Merging them would move pixels**, which is what the course says merged drift does. Step 2 decides whether this is drift or one role on four grounds |
| D-2 | **a finding's wash, edge and box** | Problem **14% / 38% / 10%** · Note **13% / 30% / 9%** | not signed per hue | It may be a deliberate balance of two hues of different lightness (`contrast.md` measures the tag pairs, not the percentages). **Not called drift without the owner's word** |
| D-3 | **the current place** | top bar: `--raised` + `--shadow-tile` · current tab: `--raised`, no shadow · current segment: `--control` + `--shadow-tile` + a `--line-strong` edge | **signed** (`concept.md`, *Segmented control*, owner 2026-10-11): the segment is lifted out of a track, the top bar has none | **Not drift.** Three named shapes of *current*. Recorded so that step 2 does not merge them by value |
| D-4 | **black shadow** | `rgba(0,0,0,.35)` three times: `--shadow-tile`, `--shadow-cutout`, `--shadow-sheet` | | **One value written three times.** It is not drift, since the values agree, but it is a primitive waiting to be named |
| D-5 | **a weight** | `600` in five `--t-*` composites and `--weight-strong: 600`; `500` in `--t-button`, `--t-micro` and `--weight-medium`; `400` likewise | | The same value written twice in two places. It is consistent today, and nothing keeps it so |

### 4.2 One variable, several roles

**This is the kit's main finding.** Most of our names already *are* roles. The trouble is the second jobs that
phase 07 gave them. Each row is a place where a theme would have to choose, and where the light slice already
*has* chosen differently for some of them.

| # | Variable | Roles it carries | Which of them may come apart | Evidence that they already do |
|---|---|---|---|---|
| M-1 | `--lime` | the primary action · a **checked control** · the **logo** · the acrylic's tint · selection's tint | an action and a *state* of a control are different claims (§15: lime is *what you can press, where you are*). The logo is brand, not action | — |
| M-2 | `--lime-mark` | **where you are** (selected row) · **Exported** · **In this project** · **running** · **progress** · **focus** | focus is an accessibility role with its own 3:1 rule; *running* and *progress* are a process; *Exported* is a past fact | `--lime-mark` itself split from `--lime` because the light theme needed 3:1 (`#55700F` against `#C6EF5A`). **This is the course's *two roles, two tokens*, already proved once** |
| M-3 | `--text-2` | secondary text · an icon in a button · a stopped stage's glyph · the empty state's icon · the *+ Add* glyph · **a checkbox's edge under the pointer** | **a text tone used as an edge** is the clearest one: an edge needs 3:1, and text needs 4.5:1 | — |
| M-4 | `--text-3` | metadata · a section label · placeholder · **disabled** · waiting · separators · chevrons · **a field's edge under the pointer** | *disabled* is a state (lesson 09 owns states, but the role already exists); **again a text tone used as an edge** | — |
| M-5 | `--raised` | a panel one step up · **the selected row** · **the current place** · **the current tab** · the skeleton · the base of every hover | *selected* and *current* are states, and a panel is a surface | — |
| M-6 | `--control` | a secondary control's fill · **a disabled button** · **the current segment** · an inline **code chip** · a **progress track** · the **empty state's tile** | a code chip is not a control; the empty-state tile is signed as *neutral*, not as a control | — |
| M-7 | `--well-deep` | a code block · **a field's well** · a checkbox's bed · a segmented **track** · a checked radio's inner ring | the variable's own signature is *a code block*, and its widest use is fields | — |
| M-8 | `--line` | a divider · a panel's edge · a stage's edge · the avatar's ring · **a disabled button's edge** | a divider separates and an edge contains. The light slice gives them one value, so they have not come apart yet | — |
| M-9 | `--line-strong` | a control's edge · a tag's outline · a dashed rule · the Export stage's edge · a code block's edge · a card under the pointer · the selected row's edge · the neutral box's edge · **the spinner's track** · **the scrollbar thumb** | ten jobs. Its signature names three of them (*a control's edge, a tag's outline, a dashed rule*) | — |
| M-10 | `--control-edge` | a field's or checkbox's 3:1 edge · a waiting stage's ring · **a Skipped stage's dashed outline** · the scrollbar under the pointer | Skipped has its own colour, `--skipped`, and its stage outline does not use it | — |
| M-11 | `--cutout` | a row · a stage · **the neutral box** (keys reminder, our failure) · the base of the finding boxes | the neutral box is signed as *not a finding*: it borrows the row's ground | — |
| M-12 | `--tray` | the tray under rows · **the ground of an empty or error state** | — | — |
| M-13 | `--bar` | the top bar · **the configuring mode's sidebar** | the sidebar is a panel, not a bar | — |
| M-14 | `--problem` (+ `-wash`, `-edge`) | a Problem · **the muted remove inside a Problem** | **signed** (`concept.md`, *Destructive action*): inside a Problem the remove is muted rose *because it is one way out*. **Signed, but still a remove wearing a finding's colour** | — |
| M-15 | `--ground` | the page's ground · **the gap in the focus ring** | the gap has to equal whatever the focused element stands on, which is not always the ground (a field on `--raised` inside a dialog) | — |
| M-16 | `--text` | primary text · emphasis · **a place under the pointer or current** · the neutral box's word | — | — |
| M-17 | `--hover-wash` | a place or tab under the pointer · **In this project under the pointer** | — | — |
| M-18 | `--sheet-edge`, `--acrylic-dialog`, `--shadow-sheet` | a dialog · **the Filters popover** · (`--sheet-edge`, `--shadow-sheet`) the side sheet | **signed**: the popover hangs *on the same acrylic edge as a dialog* | — |

### 4.3 Values bypassing a variable

**In a class: no colour, no px, no font name** (guard 1). What does stand in the classes is geometry as **a number
times a variable**, and a few keywords:

| # | Where | What | Why it matters for step 2 |
|---|---|---|---|
| V-1 | 34 skeleton classes `.sk-w32` … `.sk-h240`, `.sk-mt8`, `.sk-mt12` | `calc(var(--s1) * N)`, N from 2 to 130 | the size is the number, and `--s1` is only its unit. **This is geometry written as a number**, the course's defect, in disguise. They are the wireframes' inline sizes moved into classes in phase 07 |
| V-2 | `.door` | `width: calc(var(--s1) * 100)` (400 px), `margin-top: calc(var(--s12) * 2 + var(--s6))` | a column width written as a multiple of space |
| V-3 | `dialog.modal` `top`, `.search` `max-width`, `.callout>span` `max-width`, `.popover-body` `max-height`, `.field textarea` `min-height` | `--s12 * 3`, `--measure - --s12 * 3`, `--measure + --s12 * 4`, `100vh - --s12 * 6`, `--s10 * 4` | the same: positions and measures made from space × a number |
| V-4 | halves and doubles | `calc(var(--s1) / 2)` six times (2 px gaps and padding), `calc(var(--hairline) * 2)` (spinner ring, underline), `calc(var(--hairline) * 1)` once | a 2 px step that the scale does not have |
| V-5 | `html` | `color-scheme: dark` | **a theme written in a class.** In light it would draw native controls (a select's list, scrollbars) dark |
| V-6 | `.skeleton` | `animation: … ease-in-out`, a gradient at `0% 50% 100%` · `span.glyph-running` `linear` · rotations `90deg`, `360deg` | motion keywords beside `--ease` |
| V-7 | 21 rules | `transparent` | a keyword for *no fill*. Not a defect, but every `transparent` button (`.button-quiet`, `.remove`, `.check:has(:checked)`, `.button-danger-quiet`) is **a role written as a keyword** |

**Inside the tokens**, which is where our literals actually live:

| # | Token | Literal | Note |
|---|---|---|---|
| V-8 | `--shadow-tile`, `--shadow-cutout`, `--shadow-sheet` | `rgba(0,0,0,.35)` ×3, `rgba(255,255,255,.04)`, and the offsets `0 1px 2px`, `0 18px 40px`, `1px` | the shadows' colours and geometry |
| V-9 | `--sheet-edge` | `rgba(255,255,255,.05)` | white at 5%: an edge that only works on dark |
| V-10 | `--veil` | `rgba(10,11,9,.58)` | the veil's own near-black, which is not `--well-deep` or `--ground` |
| V-11 | `--acrylic-dialog` | `rgba(70,72,66,.45)` | the acrylic's own grey |
| V-12 | `--glyph-check` | `stroke='%23141A08'` inside the SVG | **`--on-lime`'s value copied into a data URI.** A theme that changes `--on-lime` leaves this tick behind. In the light slice `--on-lime` stays `#141A08`, so it does not show yet |
| V-13 | the twelve `color-mix()` | 7%, 9%, 10%, 13%, 14%, 25%, 30%, 35%, 38%, 50%, 55%, 60% | ratios as literals (see D-1, D-2) |
| V-14 | the nine `--t-*` | size, line height and weight in px and numbers | the type scale has no primitive of its own for size or line height |
| V-15 | `--shadow-focus` | `2px`, `4px` | the ring's gap and width |

---

## 5. Candidate semantic roles, and the uses they are read from

**Named from what the kit already does and from `concept.md`'s words, not from another system.** Each candidate lists
the uses it would take over. Where today's name already says the role, it is given as it is. **A candidate is not a
token yet**: step 2 decides, and a candidate with one use is marked as such, because the course says that is not a
role.

### Surfaces

| Candidate | Uses it is read from | Today written as | Uses |
|---|---|---|---|
| **the page's ground** | `html`, `body`, `.canvas` (83 / 241) | `--ground` | 3 |
| **the top bar** | `.app-header`, `.shared-header`, `.run-bar` (83 / 241) | `--bar` | 1 rule, 3 bars |
| **a side panel** | `.library-sidebar` and its head (13 / 42) | `--bar` (M-13) | 2 |
| **a tray** | `.row-list` (37 / 115) | `--tray` | 1 |
| **a state's ground** | `.state-block` (15 / 13) | `--tray` (M-12) | 1, **single use** |
| **a row** | `.row-list>li`, `.stages>li` (72 / 239) | `--cutout` | 2 |
| **a neutral box** | `.callout-reminder`, `.callout-failure` (15 / 14) | `--cutout` (M-11) | 1 rule |
| **a well** | `.search`, `.field input`, `.field textarea`, `.dropzone`, a checkbox's bed (59 / 157) | `--well-deep` (M-7) | 5 |
| **a code block** | `pre.file` (18 / 74) | `--well-deep` | 1 |
| **a track** | `.scope` (13 / 42) | `--well-deep` | 1 |
| **a panel** | `.card`, `.drawer`, `.aside-box`, `.export-stage` (`.is-failed`) (~30 / 120) | `--raised` | 5 |
| **a sheet** (opaque, over a mode) | `dialog.modal`, `dialog.popover`, `dialog.sheet` (20 / 22) | `--raised` | 3 |
| **a control** | `button`, `.button`, `.check`, `select` (75 / 197) | `--control` | 4 |
| **a control under the pointer** | `button:hover`, `.check:hover`, `select:hover`, `.remove:hover` | `--control-hover` | 4 |
| **an inline code chip** | `code` (54 / 224) | `--control` (M-6) | 1 |
| **a neutral tile** | `svg.icon.state-icon` (15 / 13) | `--control` (M-6) | 1, **single use** |
| **a track for progress** | `progress` (1 / 3) | `--control` (M-6) | 1, **single use** |
| **the place behind, dimmed** | `.scrim` (17 / 22) | `--veil` | 1 |
| **glass around a dialog** | `dialog.modal`, `dialog.popover` | `--acrylic-dialog` | 2 |
| **a skeleton** and **its shimmer** | `.skeleton` (9 / 2) | `--raised`, `--control-hover` | 1 rule |

### State of a place or a row (the course leaves states to lesson 09; these already exist and only move)

| Candidate | Uses | Today | Uses |
|---|---|---|---|
| **selected** | `.row-list>li:has(>.is-selected)`: its fill, its edge, its pill (37 / 115) | `--raised`, `--line-strong`, `--lime-mark` | 1 rule × 3 |
| **current** (a place, a tab, a segment) | `.app-nav a[aria-current]`, `.tabs a[aria-current]`, `.scope a[aria-current]` | `--raised` ×2, `--control` (D-3) | 3 |
| **under the pointer** | `--hover-wash`, `--row-hover`, `--segment-hover`, `--control-hover`, `.card:hover` | four recipes (D-1) | 10 |
| **disabled** | `button[disabled]` fill, edge, text and icon; `.check:has(:disabled)` | `--control`, `--line`, `--text-3` | 4 |
| **focus** | 11 `:focus-visible`/`:focus-within` rules (ring); the edge of `.search`, `.field input`, `.dropzone` in focus | `--shadow-focus` built from `--lime-mark` and `--ground` (M-2, M-15) | 14 |

### Text

| Candidate | Uses | Today | Uses |
|---|---|---|---|
| **primary text** | `body`, dialogs, `.callout`, `.verdict dd`, fields, `code`, `pre.file`, buttons | `--text` | ~15 |
| **emphasis in secondary text** | `strong` in `.state-line`, `.summary p`, `.export-stage p`, `.state-block`, `.dropzone` | `--text` (M-16) | 5 |
| **secondary text** | `.description`, `.head-meta`, `.drawer-section p`, `.state-block p`, `.summary p`, `.export-stage p`, `.plain-list`, `.usage`, `.state-line`, `.tag`, field labels | `--text-2` | ~25 |
| **metadata** | `.meta`, `.row .facts`, `.card .facts`, `.tabs .count`, `.stages summary .n`, `.time`, error codes, separators | `--text-3` | ~15 |
| **a section label** | `.verdict dt`, `.drawer-section h3`, `.stage-group>h2`, `.form-section>h3`, `legend` | `--text-3` | 5 |
| **a placeholder** | `.search input::placeholder`, `.field input::placeholder` | `--text-3` | 2 |
| **a place at rest** and **a place active** | `.app-nav a`, `.tabs a`, `.scope a`, `.run-bar .back`, `.link-button`, `.button-quiet` · their `:hover` and `[aria-current]` | `--text-2` → `--text` | 12 |

### Edges

| Candidate | Uses | Today | Uses |
|---|---|---|---|
| **a divider** | `border-top`/`-bottom` in 14 rules | `--line` | 14 |
| **a panel's edge** | `.card`, `.drawer`, `.aside-box`, `.stages>li`, `.scope`, the cut-out's inset | `--line` (M-8) | 6 |
| **a control's edge** | `button`, `.button`, `.check`, `.tag`, `pre.file`, `.export-stage` | `--line-strong` | 6 |
| **a field's edge (3:1)** | `.search`, `.field input`, `.field textarea`, `select`, `.dropzone`, checkbox, radio | `--control-edge` | 7 |
| **a field's edge under the pointer** | `.search:hover`, `.field input:hover`, `.dropzone:hover`, checkbox and radio `:hover` | `--text-3` ×3, `--text-2` ×2 (M-3, M-4) | 5, **two values for one role** |
| **a dashed rule** | `.sub-rows`, `.sub-rows>li+li` | `--line-strong` | 2 |
| **the edge of an opaque sheet** | `dialog.modal`, `dialog.popover`, `dialog.sheet` | `--sheet-edge` | 3 |

### Lime, the act and the mark

| Candidate | Uses | Today | Uses |
|---|---|---|---|
| **the action** (the one primary) | `.button-primary`: fill, edge, hover, busy (64 / 168) | `--lime`, `--lime-hover` | 4 |
| **on the action** | `.button-primary` text, icon, spinner arc; the busy spinner's track | `--on-lime`, `--on-lime-track` | 4 |
| **a checked control** | `input[type=checkbox]:checked`, `input[type=radio]:checked` (45 / 89), the tick | `--lime`, `--on-lime` in `--glyph-check` (M-1, V-12) | 2 |
| **the brand** | `.icon.logo` (71 / 153) | `--lime` (M-1) | 1, **single use** |
| **where you are** | the selected row's pill, the Export stage's pill | `--lime-mark` | 2 |
| **in the set** | `.check:has(input:checked)::before` (10 / 39) | `--lime-mark` (M-2) | 1, **single use** |
| **running / progress** | `span.glyph-running`, the Export status spinner, `progress` value | `--lime-mark` (M-2) | 3 |
| **focus** | `--shadow-focus` and three focus edges | `--lime-mark` (M-2) | 14 (see above) |
| **selected text** | `::selection` | `--lime-selection` | 1, **single use** |

### Findings, and acts that cost something

| Candidate | Uses | Today | Uses |
|---|---|---|---|
| **Problem**: word, glyph, wash, edge, box | `.tag-problem`, `.mark-problem`, `svg.glyph-problem`, `.callout>.severity`, `.result-problem`, `.callout` | `--problem` + 3 composites | 7 |
| **Note**: word, glyph, wash, edge, box | `.mark-note`, `svg.glyph-note`, `.callout-quiet>.severity`, `.result-note`, `.callout-quiet` | `--note` + 3 composites | 6 |
| **Checked** | `span.glyph-checked` | `--checked` | 1, **single use**, and **a signed role of its own** (§6, D1-B) |
| **Skipped** | `svg.glyph-skipped` · the Skipped stage's dashed outline, `.stages>li.is-skipped`, is **not** drawn in it but in `--control-edge` | `--skipped` | 1, **single use**, signed (§6) |
| **waiting** | `span.glyph-waiting`, `.stages .waiting summary` | `--control-edge`, `--text-3` | 2 |
| **stopped** | `svg.glyph-stopped` | `--text-2` | 1, **single use** |
| **a remove inside a Problem** | `.button-danger-quiet` (8 / 6) | `--problem`, `-wash`, `-edge` (M-14) | 1 rule |
| **a remove** (confirmed) | `.button-danger` (5 / 3) | `--danger`, `-hover`, `--on-danger` | 1 rule |
| **going ahead despite a Problem** | `.button-warning` (1 / 2: `run-default` and its flow steps) | `--warning`, `-hover`, `--on-warning` | 1 rule, **single use** |

### Single-use colours, flagged for step 6 as the course asks

A colour that stands in exactly one rule is not made a semantic token by the course's rule. It is flagged instead,
because it may be a real role that has not repeated yet. **Ours are**:
- `--warning` and its family: one button, on one page;
- `--checked` and `--skipped`: one glyph each;
- the brand tile;
- *in the set*;
- selected text;
- the neutral tile;
- the progress track;
- a state's ground;
- *stopped*.

**Five of them are signed in `§6` or `concept.md` as roles in their own right**: Checked, Skipped, warning, the
neutral tile, and the keys reminder's box. So the course's rule and our *colour is a claim* (§15) meet here, and step
2 has to say which one wins for each.

**Read again in step 2 (2026-10-28).** The list above counts *rules*. The course's wording is *one file, one class,
nowhere else in the product*: one **screen**. Counted by screens, only two colours stand in one place:
- `.button-warning`, on `run-default` and its flow steps. It stays a role because it is signed (B).
- the progress track, on `library-json-loading`. It is not a role: it reads `--control`.

Every other entry above stands on 3 to 83 screens. Step 2 split the ones the owner approved (A), and the rest stay in
their role. `08-design-tokens/tokens.css` lists both one-screen colours in its *FLAGGED* block for step 6.

---

## Appendix — every variable's uses, generated

The tool's output, as of 2026-10-28. *Pages* and *Steps* are counted by the rule above. *Rules* is the number of
declarations that read the variable, including a composite token's own definition.

<!-- generated by tools/audit_tokens.py --md: 83 pages, 241 flow steps -->
| Variable | Value | Rules | Pages | Steps | Read by (property → selectors) |
|---|---|---|---|---|---|
| `--ground` | `#1B1C19` | 4 | 83 | 241 | `--shadow-focus` → `:root --shadow-focus`<br>`background` → `.canvas`, `body`, `html` |
| `--bar` | `#181916` | 3 | 83 | 241 | `background` → `.app-header,.shared-header,.run-bar`, `.library-sidebar`, `.library-sidebar .panel-head` |
| `--tray` | `#232420` | 2 | 49 | 123 | `background` → `.row-list`, `.state-block` |
| `--cutout` | `#1E1F1B` | 6 | 59 | 214 | `--note-box` → `:root --note-box`<br>`--problem-box` → `:root --problem-box`<br>`--row-hover` → `:root --row-hover`<br>`background` → `.callout-reminder,.callout-failure`, `.row-list>li`, `.stages>li` |
| `--well-deep` | `#161714` | 9 | 59 | 157 | `--segment-hover` → `:root --segment-hover`<br>`background` → `.dropzone`, `.field input:not([type="checkbox"]):not([type="radio"]),.field textarea`, `.scope`, `.search`, `input[type="checkbox"],input[type="radio"]`, `pre.file`<br>`box-shadow` → `input[type="radio"]:checked`, `input[type="radio"]:checked:focus-visible` |
| `--raised` | `#2A2B27` | 15 | 73 | 239 | `--hover-wash` → `:root --hover-wash`<br>`--row-hover` → `:root --row-hover`<br>`--segment-hover` → `:root --segment-hover`<br>`background` → `.app-nav a[aria-current="page"]`, `.aside-box`, `.card`, `.drawer`, `.export-stage`, `.export-stage.is-failed`, `.row-list>li:has(> .is-selected)`, `.skeleton`, `.tabs a[aria-current="page"]`, `dialog.modal`, `dialog.popover`, `dialog.sheet` |
| `--control` | `#2E302A` | 10 | 80 | 240 | `background` → `.check`, `.scope a[aria-current="page"]`, `button,.button`, `button[disabled],button[aria-disabled="true"]:not([aria-busy]),.button[aria-disabled="true"]`, `button[disabled]:hover,.button[aria-disabled="true"]:hover`, `code`, `progress.progress`, `progress.progress::-webkit-progress-bar`, `select`, `svg.icon.state-icon` |
| `--control-hover` | `#383A33` | 5 | 81 | 240 | `background` → `.check:hover`, `.remove:hover`, `.skeleton`, `button:hover,.button:hover`, `select:hover` |
| `--line` | `#343630` | 22 | 83 | 241 | `--shadow-cutout` → `:root --shadow-cutout`<br>`border` → `.aside-box`, `.card`, `.drawer`<br>`border-bottom` → `.app-header,.shared-header,.run-bar`, `.file-list li`, `.popover-head`, `.tabs`<br>`border-color` → `button[disabled],button[aria-disabled="true"]:not([aria-busy]),.button[aria-disabled="true"]`, `button[disabled]:hover,.button[aria-disabled="true"]:hover`<br>`border-right` → `.library-sidebar`<br>`border-top` → `.card .verdict`, `.door-alt`, `.drawer-actions`, `.drawer-section`, `.file-list`, `.form-actions`, `.form-section`, `.popover-foot`<br>`box-shadow` → `.scope`, `.stages>li`, `img.avatar` |
| `--line-strong` | `#4A4C44` | 16 | 83 | 241 | `background` → `::-webkit-scrollbar-thumb`<br>`border` → `.check`, `.export-stage`, `button,.button`, `pre.file`, `span.glyph-running,.export-stage [role="status"]::before`<br>`border-color` → `.card:hover`, `.export-stage.is-exported`, `.export-stage.is-failed`<br>`border-top` → `.sub-rows`, `.sub-rows>li+li`<br>`box-shadow` → `.callout-reminder,.callout-failure`, `.row-list>li:has(> .is-selected)`, `.scope a[aria-current="page"]`, `.tag`<br>`scrollbar-color` → `*` |
| `--control-edge` | `#7C7F74` | 8 | 83 | 241 | `background-color` → `::-webkit-scrollbar-thumb:hover`<br>`border` → `.dropzone`, `.field input:not([type="checkbox"]):not([type="radio"]),.field textarea`, `.search`, `input[type="checkbox"],input[type="radio"]`, `select`<br>`box-shadow` → `span.glyph-waiting`<br>`outline` → `.stages>li.is-skipped` |
| `--text` | `#F3F4EF` | 33 | 83 | 241 | `color` → `.app-nav a:hover`, `.app-nav a[aria-current="page"]`, `.callout`, `.callout-reminder>.severity,.callout-failure>.severity`, `.check`, `.door-alt a`, `.door-alt a:hover,a.meta:hover`, `.dropzone strong`, `.export-stage p strong`, `.export-stage[role="alert"] h2`, `.field input:not([type="checkbox"]):not([type="radio"]),.field textarea`, `.meta a:hover`, `.popover-group label`, `.popover-group label:hover`, `.run-bar .back:hover`, `.scope a:hover`, `.scope a[aria-current="page"]`, `.search input`, `.state-block strong`, `.state-line strong`, `.summary p strong`, `.tabs a:hover`, `.tabs a[aria-current="page"]`, `.verdict dd`, `body`, `button,.button`, `button.link-button:hover`, `code`, `dialog.modal`, `dialog.popover`, `dialog.sheet`, `pre.file`, `select` |
| `--text-2` | `#C5C7BE` | 40 | 83 | 241 | `background` → `.check::before`, `.library-version summary:hover::before`<br>`border-color` → `input[type="checkbox"]:hover,input[type="radio"]:hover`<br>`color` → `.app-header .account,.shared-header .owner`, `.app-nav a`, `.aside-box .meta`, `.button-quiet`, `.card .description`, `.check:has(input:checked)`, `.description`, `.door .head-meta`, `.door-alt`, `.drawer-section p`, `.dropzone`, `.export-stage p`, `.field>span:first-child`, `.head-meta`, `.library-version summary:hover`, `.link-button`, `.meta a`, `.plain-list`, `.row .description`, `.row .facts em`, `.run-bar .back`, `.run-bar .pick`, `.scope a`, `.stages summary .result`, `.state-block p`, `.state-line`, `.summary p`, `.tabs a`, `.tag`, `.tag-state`, `.usage`, `.verdict dd.meta`, `button svg.icon,.button svg.icon`, `dialog.modal p`, `dialog.modal ul`, `svg.glyph-stopped`, `svg.icon.state-icon` |
| `--text-3` | `#A1A49A` | 37 | 83 | 241 | `background` → `.check:has(input:checked:disabled)::before`, `.library-version summary::before`, `.stages summary::after`<br>`border-color` → `.dropzone:hover`, `.field input:not([type="checkbox"]):not([type="radio"]):hover,.field textarea:hover`, `.search:hover`<br>`color` → `.app-main>.meta:first-child`, `.card .facts`, `.check:has(input:disabled)`, `.drawer-facts dt`, `.drawer-section h3`, `.export-stage h2 .n`, `.field .hint`, `.field input::placeholder,.field textarea::placeholder`, `.form-section>h3`, `.head-meta span+span::before`, `.library-version summary`, `.meta`, `.plain-list li::before`, `.popover-group .hint`, `.row .facts`, `.row .facts code`, `.search`, `.search input::placeholder`, `.stage-group>h2`, `.stages .waiting summary`, `.stages .waiting summary .name`, `.stages summary .n`, `.stages summary .time`, `.state-block .meta`, `.tabs .count`, `.verdict dt`, `:is(p,span).meta.error-code`, `button[disabled] svg.icon,button[aria-disabled="true"]:not([aria-busy]) svg.icon,.button[aria-disabled="true"] svg.icon`, `button[disabled],button[aria-disabled="true"]:not([aria-busy]),.button[aria-disabled="true"]`, `button[disabled]:hover,.button[aria-disabled="true"]:hover`, `legend` |
| `--lime` | `#C6EF5A` | 11 | 83 | 241 | `--acrylic-dialog` → `:root --acrylic-dialog`<br>`--lime-selection` → `:root --lime-selection`<br>`background` → `.button-primary`, `.button-primary[aria-busy="true"]:hover`, `.icon.logo`, `input[type="checkbox"]:checked`, `input[type="radio"]:checked`<br>`border-color` → `.button-primary`, `.button-primary[aria-busy="true"]:hover`, `input[type="checkbox"]:checked`, `input[type="radio"]:checked` |
| `--lime-hover` | `#D3F57A` | 2 | 64 | 168 | `background` → `.button-primary:hover`<br>`border-color` → `.button-primary:hover` |
| `--on-lime` | `#141A08` | 4 | 64 | 168 | `--on-lime-track` → `:root --on-lime-track`<br>`border-top-color` → `.button-primary span.glyph-running`<br>`color` → `.button-primary`, `.button-primary svg.icon` |
| `--lime-mark` | `#C6EF5A` | 10 | 80 | 240 | `--shadow-focus` → `:root --shadow-focus`<br>`background` → `.check:has(input:checked)::before`, `.export-stage.is-exported::before`, `.row-list>li:has(> .is-selected)::before`, `progress.progress::-moz-progress-bar`, `progress.progress::-webkit-progress-value`<br>`border-color` → `.dropzone:focus-within`, `.field input:not([type="checkbox"]):not([type="radio"]):focus-visible,.field textarea:focus-visible`, `.search:focus-within`<br>`border-top-color` → `span.glyph-running,.export-stage [role="status"]::before` |
| `--problem` | `#FF8F98` | 9 | 39 | 145 | `--problem-box` → `:root --problem-box`<br>`--problem-edge` → `:root --problem-edge`<br>`--problem-wash` → `:root --problem-wash`<br>`color` → `.button-danger-quiet`, `.callout>.severity`, `.mark-problem`, `.stages summary .result-problem`, `.tag-problem`, `svg.glyph-problem` |
| `--note` | `#F2C661` | 7 | 25 | 136 | `--note-box` → `:root --note-box`<br>`--note-edge` → `:root --note-edge`<br>`--note-wash` → `:root --note-wash`<br>`color` → `.callout-quiet>.severity`, `.mark-note`, `.stages summary .result-note`, `svg.glyph-note` |
| `--checked` | `#C5C7BE` | 1 | 20 | 99 | `background` → `span.glyph-checked` |
| `--skipped` | `#A1A49A` | 1 | 18 | 92 | `color` → `svg.glyph-skipped` |
| `--warning` | `#EFA23A` | 2 | 1 | 2 | `background` → `.button-warning`<br>`border-color` → `.button-warning` |
| `--warning-hover` | `#E0962E` | 2 | 1 | 2 | `background` → `.button-warning:hover`<br>`border-color` → `.button-warning:hover` |
| `--on-warning` | `#1A1200` | 2 | 1 | 2 | `color` → `.button-warning`, `.button-warning svg.icon` |
| `--danger` | `#D4363F` | 2 | 5 | 3 | `background` → `.button-danger`<br>`border-color` → `.button-danger` |
| `--danger-hover` | `#BE2E37` | 2 | 5 | 3 | `background` → `.button-danger:hover`<br>`border-color` → `.button-danger:hover` |
| `--on-danger` | `#FFFFFF` | 2 | 5 | 3 | `color` → `.button-danger`, `.button-danger svg.icon` |
| `--font` | `"Geist", system-ui, sans-serif` | 8 | 83 | 241 | `--t-body` → `:root --t-body`<br>`--t-button` → `:root --t-button`<br>`--t-display` → `:root --t-display`<br>`--t-heading` → `:root --t-heading`<br>`--t-label` → `:root --t-label`<br>`--t-micro` → `:root --t-micro`<br>`--t-small` → `:root --t-small`<br>`--t-title` → `:root --t-title` |
| `--mono` | `"Geist Mono", ui-monospace, monospace` | 4 | 83 | 241 | `--t-code` → `:root --t-code`<br>`font-family` → `.export-stage h2 .n`, `.export-stage h2 code`, `.stages summary .name code` |
| `--t-display` | `600 28px/34px var(--font)` | 2 | 59 | 141 | `font` → `.door h1`, `.page-head h1` |
| `--t-title` | `600 20px/26px var(--font)` | 3 | 35 | 112 | `font` → `.export-stage.is-exported h2`, `.state-block h2`, `.summary h1` |
| `--t-heading` | `600 16px/22px var(--font)` | 7 | 52 | 176 | `font` → `.aside-box h2`, `.card h2`, `.drawer-head h2`, `.export-stage h2`, `.panel h2`, `.popover-head h2`, `dialog.modal h2,.sheet-head h2` |
| `--t-body` | `400 14.5px/21px var(--font)` | 8 | 83 | 241 | `font` → `.app-header .product,.shared-header .product`, `.door .head-meta`, `.row h2,.row h3`, `.run-bar .title`, `.stages summary .name`, `.state-block p`, `body`, `h2.heading-small` |
| `--t-button` | `500 13.5px/16px var(--font)` | 7 | 79 | 240 | `font` → `.app-nav a`, `.check`, `.run-bar .back`, `.scope a`, `.tabs-page a`, `button,.button`, `select` |
| `--t-small` | `400 13px/19px var(--font)` | 29 | 79 | 240 | `font` → `.app-header .account,.shared-header .owner`, `.app-main>.meta:first-child`, `.aside-box .meta`, `.callout`, `.card .description`, `.door-alt`, `.drawer-facts`, `.drawer-section p`, `.dropzone`, `.export-stage p`, `.field input:not([type="checkbox"]):not([type="radio"]),.field textarea`, `.file-list li`, `.head-meta`, `.library-version summary`, `.link-button`, `.plain-list`, `.popover-group label`, `.row .description`, `.run-bar .pick`, `.search input`, `.severity`, `.stages summary .result`, `.summary p`, `.tabs a`, `.verdict dd`, `.verdict dd.meta`, `dialog.modal p`, `dialog.modal ul`, `p.meta.head-meta,.head-meta.meta` |
| `--t-micro` | `500 12px/16px var(--font)` | 9 | 72 | 236 | `font` → `.card .facts`, `.field .hint`, `.field>span:first-child`, `.mark`, `.meta`, `.popover-group .hint`, `.row .facts`, `.state-line`, `.tag` |
| `--t-label` | `600 11.5px/16px var(--font)` | 5 | 36 | 128 | `font` → `.drawer-section h3`, `.form-section>h3`, `.stage-group>h2`, `.verdict dt`, `legend` |
| `--t-code` | `400 12px/20px var(--mono)` | 8 | 83 | 241 | `font` → `.field textarea`, `.field-mono input:not([type="checkbox"]):not([type="radio"])`, `.stages summary .n`, `.stages summary .time`, `.state-block .meta`, `:is(p,span).meta.error-code`, `code`, `pre.file` |
| `--track-display` | `-.018em` | 2 | 59 | 141 | `letter-spacing` → `.door h1`, `.page-head h1` |
| `--track-title` | `-.012em` | 3 | 35 | 112 | `letter-spacing` → `.export-stage.is-exported h2`, `.state-block h2`, `.summary h1` |
| `--track-heading` | `-.008em` | 6 | 44 | 142 | `letter-spacing` → `.aside-box h2`, `.card h2`, `.drawer-head h2`, `.export-stage h2`, `.popover-head h2`, `dialog.modal h2,.sheet-head h2` |
| `--track-label` | `.06em` | 5 | 36 | 128 | `letter-spacing` → `.drawer-section h3`, `.form-section>h3`, `.stage-group>h2`, `.verdict dt`, `legend` |
| `--weight-regular` | `400` | 10 | 69 | 238 | `font-weight` → `.card .facts`, `.export-stage h2 .n`, `.field .hint`, `.field-label .meta`, `.meta`, `.popover-group .hint`, `.row .facts`, `.stages .waiting summary .name`, `.state-line`, `.tabs .count` |
| `--weight-medium` | `500` | 1 | 8 | 6 | `font-weight` → `.button-danger-quiet` |
| `--weight-strong` | `600` | 14 | 83 | 241 | `font-weight` → `.app-header .product,.shared-header .product`, `.button-primary`, `.dropzone strong`, `.field>span:first-child`, `.mark`, `.row h2,.row h3`, `.run-bar .title`, `.severity`, `.stages summary .name`, `.stages summary .result-note`, `.stages summary .result-problem`, `.state-line strong`, `.tabs a[aria-current="page"]`, `h2.heading-small` |
| `--s1` | `4px` | 69 | 83 | 241 | `background` → `input[type="checkbox"]:checked`<br>`border` → `::-webkit-scrollbar-thumb`<br>`box-shadow` → `input[type="radio"]:checked`, `input[type="radio"]:checked:focus-visible`<br>`gap` → `.app-nav ul`, `.card .facts`, `.check`, `.dropzone-small`, `.field`, `.head-meta`, `.library-version summary`, `.mark`, `.plain-list`, `.row .facts`, `.scope`, `.severity`, `.summary.is-failed`, `.tabs`, `.tag`, `dialog.modal ul`<br>`height` → `.sk-h12`, `.sk-h16`, `.sk-h160`, `.sk-h20`, `.sk-h24`, `.sk-h240`, `.sk-h32`, `.sk-h40`<br>`left` → `.row-list>li:has(> .is-selected)::before`<br>`margin` → `.link-button`, `span.glyph-checked`<br>`margin-bottom` → `svg.icon.state-icon`<br>`margin-left` → `.tabs .count`<br>`margin-right` → `.glyph`<br>`margin-top` → `.callout .row-actions`, `.row .description`, `.row .facts`, `.sk-mt12`, `.sk-mt8`, `.state-line`, `.verdict dd`<br>`min-height` → `.stages summary`<br>`padding` → `.library-version summary .link-button`, `.link-button`, `.scope`, `.tag-state`, `code`<br>`vertical-align` → `.glyph`, `svg.icon`<br>`width` → `.door`, `.sk-w140`, `.sk-w160`, `.sk-w180`, `.sk-w200`, `.sk-w220`, `.sk-w240`, `.sk-w260`, `.sk-w280`, `.sk-w32`, `.sk-w420`, `.sk-w440`, `.sk-w460`, `.sk-w48`, `.sk-w480`, `.sk-w520`, `.sk-w56`, `.sk-w64`, `.sk-w72`, `.sk-w80` |
| `--s2` | `8px` | 61 | 83 | 241 | `box-shadow` → `dialog.modal`, `dialog.popover`<br>`gap` → `.app-header .account,.shared-header .owner`, `.app-header .product,.shared-header .product`, `.app-nav a`, `.callout`, `.card h2`, `.drawer-actions`, `.drawer-facts`, `.drawer-head h2`, `.drawer-section`, `.dropzone`, `.export-actions`, `.export-stage [role="status"]`, `.form-actions`, `.head-actions`, `.marks`, `.popover-foot`, `.popover-group`, `.popover-group label`, `.row h2,.row h3`, `.row-actions`, `.row-list`, `.run-bar .back`, `.run-bar .pick`, `.search`, `.stage-group`, `.stages`, `.state-actions`, `.summary`, `button,.button`<br>`height` → `progress.progress`<br>`left` → `.export-stage.is-exported::before`<br>`margin` → `.link-button`, `span.glyph-checked`<br>`margin-bottom` → `.export-stage.is-exported>div>p`, `.file-list`, `legend`<br>`margin-top` → `.card .description`, `.export-stage.is-exported>div:not(.export-actions)`, `.head-meta`, `.library-version pre.file`, `.state-actions`, `dialog.modal p`, `dialog.modal ul`, `progress.progress`<br>`padding` → `.check`, `.field textarea`, `.file-list .link-button`, `.file-list li`, `.link-button`, `.mark`, `.row-compact`, `.row-list`, `.stages summary`, `.tabs a`, `.tag`, `.tag-problem`<br>`padding-bottom` → `.tabs`<br>`padding-left` → `.export-stage.is-exported`<br>`top` → `dialog.popover` |
| `--s3` | `12px` | 34 | 83 | 241 | `bottom` → `.row-list>li:has(> .is-selected)::before`<br>`gap` → `.aside-box`, `.card .facts`, `.drawer-facts`, `.drawer-head`, `.export-stage`, `.file-list li`, `.page-head h1`, `.panel-head`, `.row .facts`, `.stage-body`, `.stages summary`, `.state-block`<br>`height` → `.skeleton`, `::-webkit-scrollbar`<br>`margin-right` → `.card .facts span+span::before`<br>`margin-top` → `.card .facts`, `.verdict dd+dt`<br>`padding` → `.app-nav a`, `.callout`, `.check`, `.field input:not([type="checkbox"]):not([type="radio"]),.field textarea`, `.field textarea`, `.mark`, `.popover-foot`, `.row`, `.search`, `.stage-body`, `button,.button`, `pre.file`, `select`<br>`padding-left` → `.plain-list li`<br>`top` → `.row-list>li:has(> .is-selected)::before`<br>`width` → `::-webkit-scrollbar` |
| `--s4` | `16px` | 31 | 77 | 238 | `gap` → `.card`, `.drawer`, `.field-row`, `.find`, `.form`, `.form-section`, `.head-meta`, `.row`, `.sheet-head`<br>`margin` → `.sub-rows`<br>`margin-right` → `.head-meta span+span::before`<br>`margin-top` → `dialog.modal .callout`, `dialog.modal .field`<br>`padding` → `.callout`, `.dropzone-small`, `.panel-body .state-block`, `.panel-head`, `.popover-body`, `.popover-head`, `.row`, `.row-compact`, `.stage-body`, `.stages summary`, `pre.file`<br>`padding-top` → `.card .verdict`, `.door-alt`, `.drawer-actions`, `.drawer-section`, `.form-actions`<br>`top` → `.aside-box`, `.drawer` |
| `--s5` | `20px` | 15 | 47 | 143 | `bottom` → `.export-stage.is-exported::before`<br>`gap` → `.card-grid`, `.popover-body`, `.with-drawer`<br>`margin-top` → `.form-actions`<br>`padding` → `.aside-box`, `.card`, `.drawer`, `.export-stage`, `.popover-body`, `.popover-foot`, `.popover-head`<br>`padding-left` → `.export-stage.is-exported`<br>`padding-top` → `.form-section`<br>`top` → `.export-stage.is-exported::before` |
| `--s6` | `24px` | 16 | 83 | 241 | `gap` → `.app-header,.shared-header,.run-bar`, `.app-main`, `.door`, `.page-head`, `.summary`, `dialog.sheet`<br>`grid-template-columns` → `.stages summary`<br>`margin` → `.door`, `.sub-rows`, `.sub-rows .sub-rows`<br>`padding` → `.app-header,.shared-header,.run-bar`, `.dropzone`, `.panel-body`, `.panel-head`, `.stage-body`, `dialog.modal` |
| `--s8` | `32px` | 5 | 83 | 241 | `gap` → `.with-aside`<br>`padding` → `.app-main`, `.dropzone`, `.state-block`, `dialog.sheet` |
| `--s10` | `40px` | 3 | 31 | 116 | `min-height` → `.field textarea`, `.stages summary`<br>`padding` → `.panel-body .state-block` |
| `--s12` | `48px` | 10 | 77 | 194 | `grid-template-columns` → `.stages summary`<br>`height` → `svg.icon.state-icon`<br>`margin` → `.door`<br>`max-height` → `.popover-body`<br>`max-width` → `.callout>span`, `.search`<br>`padding` → `.state-block`, `svg.icon.state-icon`<br>`top` → `dialog.modal`<br>`width` → `svg.icon.state-icon` |
| `--r-xs` | `4px` | 7 | 83 | 241 | `border-radius` → `.export-stage.is-exported::before`, `.icon.logo`, `.library-version summary:focus-visible`, `.row-list>li:has(> .is-selected)::before`, `.skeleton`, `code`, `input[type="checkbox"],input[type="radio"]` |
| `--r-sm` | `6px` | 8 | 79 | 240 | `border-radius` → `.app-nav a`, `.check`, `.field input:not([type="checkbox"]):not([type="radio"]),.field textarea`, `.scope a`, `.search`, `.tabs a`, `button,.button`, `select` |
| `--r-md` | `10px` | 8 | 72 | 223 | `border-radius` → `.callout`, `.dropzone`, `.row-list>li`, `.scope`, `.stages summary`, `.stages>li`, `pre.file`, `svg.icon.state-icon` |
| `--r-lg` | `14px` | 8 | 72 | 238 | `border-radius` → `.aside-box`, `.card`, `.drawer`, `.export-stage`, `.row-list`, `.state-block`, `dialog.modal`, `dialog.popover` |
| `--r-pill` | `999px` | 12 | 83 | 241 | `border-radius` → `.mark`, `.tag`, `::-webkit-scrollbar-thumb`, `img.avatar`, `input[type="radio"]`, `progress.progress`, `progress.progress::-moz-progress-bar`, `progress.progress::-webkit-progress-bar`, `progress.progress::-webkit-progress-value`, `span.glyph-checked`, `span.glyph-running,.export-stage [role="status"]::before`, `span.glyph-waiting` |
| `--hairline` | `1px` | 54 | 83 | 241 | `border` → `.aside-box`, `.card`, `.check`, `.drawer`, `.dropzone`, `.export-stage`, `.field input:not([type="checkbox"]):not([type="radio"]),.field textarea`, `.search`, `::-webkit-scrollbar-thumb`, `button,.button`, `dialog.modal`, `dialog.popover`, `input[type="checkbox"],input[type="radio"]`, `pre.file`, `select`, `span.glyph-running,.export-stage [role="status"]::before`<br>`border-bottom` → `.app-header,.shared-header,.run-bar`, `.file-list li`, `.popover-head`, `.tabs`<br>`border-left` → `dialog.sheet`<br>`border-right` → `.library-sidebar`<br>`border-top` → `.card .verdict`, `.door-alt`, `.drawer-actions`, `.drawer-section`, `.file-list`, `.form-actions`, `.form-section`, `.popover-foot`, `.sub-rows`, `.sub-rows>li+li`<br>`box-shadow` → `.callout`, `.callout-quiet`, `.callout-reminder,.callout-failure`, `.row-list>li:has(> .is-selected)`, `.scope`, `.scope a[aria-current="page"]`, `.stages>li`, `.tag`, `.tag-problem`, `img.avatar`, `input[type="radio"]:checked`, `input[type="radio"]:checked:focus-visible`, `span.glyph-waiting`<br>`height` → `.visually-hidden`<br>`outline` → `.stages>li.is-skipped`<br>`outline-offset` → `.stages>li.is-skipped`<br>`padding` → `.scope`, `.tabs a`<br>`text-decoration-thickness` → `.door-alt a:hover,a.meta:hover`<br>`vertical-align` → `span.glyph-checked`, `svg.icon`<br>`width` → `.visually-hidden` |
| `--control-h` | `32px` | 9 | 79 | 240 | `height` → `.app-nav a`, `.field input:not([type="checkbox"]):not([type="radio"]),.field textarea`, `.run-bar .back`, `.search`, `button,.button`, `select`<br>`top` → `dialog.popover`<br>`width` → `.drawer-head .close,.sheet-head .close`, `.remove` |
| `--control-h-s` | `28px` | 3 | 32 | 69 | `height` → `.check`, `.scope a`, `.tabs a` |
| `--tag-h` | `20px` | 1 | 38 | 132 | `height` → `.tag` |
| `--mark-h` | `24px` | 4 | 59 | 151 | `height` → `.mark`, `img.avatar`<br>`min-height` → `.row h2,.row h3`<br>`width` → `img.avatar` |
| `--bar-h` | `52px` | 1 | 83 | 241 | `height` → `.app-header,.shared-header,.run-bar` |
| `--icon` | `16px` | 10 | 83 | 241 | `background` → `input[type="checkbox"]:checked`<br>`grid-template-columns` → `.stages summary`<br>`height` → `.check::before`, `.stages summary::after`, `input[type="checkbox"],input[type="radio"]`, `svg.icon`<br>`width` → `.check::before`, `.stages summary::after`, `input[type="checkbox"],input[type="radio"]`, `svg.icon` |
| `--icon-s` | `14px` | 8 | 83 | 241 | `height` → `.export-stage [role="status"]::before`, `.glyph`, `.icon.logo`, `.library-version summary::before`<br>`width` → `.export-stage [role="status"]::before`, `.glyph`, `.icon.logo`, `.library-version summary::before` |
| `--icon-l` | `20px` | 1 | 15 | 13 | `padding` → `svg.icon.state-icon` |
| `--pill-w` | `3px` | 2 | 41 | 137 | `width` → `.export-stage.is-exported::before`, `.row-list>li:has(> .is-selected)::before` |
| `--dot` | `6px` | 2 | 20 | 99 | `height` → `span.glyph-checked`<br>`width` → `span.glyph-checked` |
| `--dt-w` | `116px` | 1 | 2 | 1 | `grid-template-columns` → `.drawer-facts` |
| `--stage-name-w` | `300px` | 1 | 20 | 99 | `grid-template-columns` → `.stages summary` |
| `--canvas` | `1280px` | 0 | 0 | 0 | — |
| `--col-m` | `200px` | 1 | 37 | 115 | `grid-template-columns` → `.row` |
| `--col-l` | `320px` | 2 | 37 | 115 | `grid-template-columns` → `.row`, `.row-tight` |
| `--col-xl` | `360px` | 2 | 7 | 4 | `grid-template-columns` → `.with-aside`<br>`width` → `dialog.popover` |
| `--side-w` | `440px` | 2 | 14 | 42 | `grid-template-columns` → `.config-layout`, `.with-drawer` |
| `--sheet-w` | `640px` | 1 | 5 | 6 | `width` → `dialog.sheet` |
| `--modal-w` | `520px` | 2 | 28 | 29 | `max-width` → `.state-block p`<br>`width` → `dialog.modal` |
| `--measure` | `640px` | 4 | 62 | 206 | `max-width` → `.callout>span`, `.description-wide`, `.row .description`, `.search` |
| `--measure-wide` | `820px` | 0 | 0 | 0 | — |
| `--z-sticky` | `1` | 1 | 13 | 42 | `z-index` → `.library-sidebar .panel-head` |
| `--z-popover` | `5` | 1 | 3 | 0 | `z-index` → `dialog.popover` |
| `--icon-add` | `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2…` | 2 | 10 | 39 | `-webkit-mask` → `.check::before`<br>`mask` → `.check::before` |
| `--icon-added` | `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2…` | 2 | 10 | 39 | `-webkit-mask-image` → `.check:has(input:checked)::before`<br>`mask-image` → `.check:has(input:checked)::before` |
| `--icon-chevron` | `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2…` | 4 | 23 | 105 | `-webkit-mask` → `.library-version summary::before`, `.stages summary::after`<br>`mask` → `.library-version summary::before`, `.stages summary::after` |
| `--glyph-check` | `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2…` | 1 | 45 | 89 | `background` → `input[type="checkbox"]:checked` |
| `--ease` | `cubic-bezier(.2,.7,.2,1)` | 13 | 80 | 240 | `transition` → `.card`, `.check`, `.dropzone`, `.field input:not([type="checkbox"]):not([type="radio"]),.field textarea`, `.library-version summary::before`, `.row-list>li`, `.scope a`, `.stages summary`, `.stages summary::after`, `.tabs a`, `button,.button`, `input[type="checkbox"],input[type="radio"]`, `select` |
| `--dur` | `140ms` | 13 | 80 | 240 | `transition` → `.card`, `.check`, `.dropzone`, `.field input:not([type="checkbox"]):not([type="radio"]),.field textarea`, `.library-version summary::before`, `.row-list>li`, `.scope a`, `.stages summary`, `.stages summary::after`, `.tabs a`, `button,.button`, `input[type="checkbox"],input[type="radio"]`, `select` |
| `--dur-spin` | `900ms` | 1 | 20 | 105 | `animation` → `span.glyph-running,.export-stage [role="status"]::before` |
| `--dur-shimmer` | `1400ms` | 1 | 9 | 2 | `animation` → `.skeleton` |
| `--shadow-tile` | `0 1px 2px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255…` | 2 | 49 | 136 | `box-shadow` → `.app-nav a[aria-current="page"]`, `.scope a[aria-current="page"]` |
| `--shadow-cutout` | `inset 0 0 0 1px var(--line), inset 0 1px 2px rgba(0,0,0,.…` | 1 | 37 | 115 | `box-shadow` → `.row-list>li` |
| `--shadow-sheet` | `0 18px 40px rgba(0,0,0,.35)` | 3 | 20 | 22 | `box-shadow` → `dialog.modal`, `dialog.popover`, `dialog.sheet` |
| `--shadow-focus` | `0 0 0 2px var(--ground), 0 0 0 4px var(--lime-mark)` | 11 | 79 | 240 | `box-shadow` → `.app-nav a:focus-visible,.app-nav a[aria-current="page"]:focus-visible,select:focus-visible,.stages summary:focus-visible`, `.check:has(input:focus-visible)`, `.dropzone:focus-within`, `.field input:not([type="checkbox"]):not([type="radio"]):focus-visible,.field textarea:focus-visible`, `.library-version summary:focus-visible`, `.scope a:focus-visible`, `.search:focus-within`, `.tabs a:focus-visible`, `button:focus-visible,.button:focus-visible,a:focus-visible`, `input[type="checkbox"]:focus-visible,input[type="radio"]:focus-visible`, `input[type="radio"]:checked:focus-visible` |
| `--acrylic-dialog` | `color-mix(in srgb, var(--lime) 7%, rgba(70,72,66,.45))` | 2 | 16 | 16 | `box-shadow` → `dialog.modal`, `dialog.popover` |
| `--sheet-edge` | `rgba(255,255,255,.05)` | 3 | 20 | 22 | `border` → `dialog.modal`, `dialog.popover`<br>`border-left` → `dialog.sheet` |
| `--veil` | `rgba(10,11,9,.58)` | 1 | 17 | 22 | `background` → `.scrim` |
| `--problem-wash` | `color-mix(in srgb, var(--problem) 14%, transparent)` | 3 | 20 | 72 | `background` → `.button-danger-quiet:hover`, `.mark-problem`, `.tag-problem` |
| `--note-wash` | `color-mix(in srgb, var(--note) 13%, transparent)` | 1 | 13 | 69 | `background` → `.mark-note` |
| `--problem-edge` | `color-mix(in srgb, var(--problem) 38%, transparent)` | 3 | 39 | 145 | `border-color` → `.button-danger-quiet`<br>`box-shadow` → `.callout`, `.tag-problem` |
| `--note-edge` | `color-mix(in srgb, var(--note) 30%, transparent)` | 1 | 14 | 69 | `box-shadow` → `.callout-quiet` |
| `--problem-box` | `color-mix(in srgb, var(--problem) 10%, var(--cutout))` | 1 | 31 | 84 | `background` → `.callout` |
| `--note-box` | `color-mix(in srgb, var(--note) 9%, var(--cutout))` | 1 | 14 | 69 | `background` → `.callout-quiet` |
| `--hover-wash` | `color-mix(in srgb, var(--raised) 60%, transparent)` | 3 | 49 | 136 | `background` → `.app-nav a:hover`, `.check:has(input:checked):hover`, `.tabs a:hover` |
| `--row-hover` | `color-mix(in srgb, var(--raised) 50%, var(--cutout))` | 2 | 57 | 214 | `background` → `.row-list>li:hover`, `.stages details:not(.stage-empty)>summary:hover` |
| `--lime-selection` | `color-mix(in srgb, var(--lime) 35%, transparent)` | 1 | 83 | 241 | `background` → `::selection` |
| `--segment-hover` | `color-mix(in srgb, var(--raised) 55%, var(--well-deep))` | 1 | 13 | 42 | `background` → `.scope a:hover` |
| `--on-lime-track` | `color-mix(in srgb, var(--on-lime) 25%, transparent)` | 1 | 3 | 8 | `border-color` → `.button-primary span.glyph-running` |
