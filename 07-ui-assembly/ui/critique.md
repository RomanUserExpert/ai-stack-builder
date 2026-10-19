# Critique of the dressed screens and the kit

**Phase 07, step 6. Run 2026-10-19.** `/impeccable critique` was split across three sub-agents running in parallel. Each
was read-only and reported findings without fixing them:

- **G2**: viewer group 2, *What I am putting together*, all 26 dressed pages: Projects, Project, Configuring and
  Detached;
- **G3**: group 3, *What leaves*, the painted Run in 8 states plus the `main-success` flow;
- **K**: the kit itself, `kit.css`, `kit.html` and `shell.html`.

Groups 0, 1 and 4 are not dressed yet, so they were not critiqued.

Below is one table of 55 rows, with duplicates merged. The **Sources** column keeps the original row numbers
(`G2-1`, `G3-3`, `K-11`). **The priorities are the owner's to set.** The *Sev* column is the agents' own grading:
- **P1**: broken or misleading;
- **P2**: a clear defect;
- **P3**: polish.

**Route** says where a fix would go:
- **kit**: `kit.css` and `kit.html`, through `tools/build_kit.py` or `build_mockups.py`, then onto every screen;
- **copy**: `microcopy.md` and `rewrite_copy.py` (§14);
- **markup**: a page's structure, which is the wireframe's (lesson 04);
- **spec**: a product decision, which goes to the register.

| # | Where | Element | What is wrong | Sev | Route | Sources |
|---|---|---|---|---|---|---|
| 1 | run-error-setup | the summary *Checked just now*, and the Export stage | `SETUP.md` failed to write, yet the verdict reads as a normal check. Export offers itself without saying the archive will have no `SETUP.md`. This is the short, silent disclosure that Q28 forbids. | P1 | copy · markup | G3-1 |
| 2 | project-configuring-*, project-detached-* | panel rows db-migrate, postgres-mcp, seed-data (*Required by …*) | An auto-added row shows a live `✓ In this project` that can be unchecked. §8 says it refuses from both sides, and the panel neither refuses nor says so. | P1 | kit · markup | G2-2 |
| 3 | kit.html ↔ shell.html | top nav and intro links | Each page links to the other as `../pages/…`, so the two cannot reach each other. `inventory.md` is not served on Vercel. | P1 | kit | K-1 |
| 4 | project-configuring-item · run-error-setup · projects-filters | *Detach to edit here* + *Save* · *Write SETUP.md again* + *Export with 1 problem* · *Apply* + *New project* behind the popover | Two lime or filled primaries on one screen. The demotion rule only covers an error box against the page head. | P1 | kit | G2-1, G3-2, G2-22 |
| 5 | run-error-setup, run-error-export, project-configuring-error-server, project-detached-error, the dialog import errors | *our failure* (`.callout[role=alert]`, `.export-stage[role=alert]`) | Our server failing is painted in Problem rose, which claims *the archive will be wrong*. The same failure is the neutral tile on projects-error-server. One meaning has two looks, and the colour asserts a finding that isn't one. | P2 | kit | G3-3, G2-5, K-11 |
| 6 | all Run pages | `.stages summary` | A stage with nothing inside still has a pointer, toggles, and takes focus. There is no disclosure marker, so nothing says stages 05/06/08/09 hold the handover. There is no hover. The kit now has two disclosure patterns, since `library-version` has a chevron. | P2 | kit · markup | G3-5, G3-6, G3-7, K-6 |
| 7 | kit.css | `.export-stage:has(.plain-list)`, `.stages>li:has(.glyph-skipped)`, `.summary:has(>p:nth-of-type(3))` | A state is drawn from what the markup happens to contain, not from a class. A *ready* stage with a list gets the *exported* pill and title. Adding one line to a summary changes its layout. | P2 | kit · markup | G3-12, K-4, K-23 |
| 8 | kit.css | the demoted head primary | The demoted primary has no hover. Because warning and danger also carry `button-primary`, a demoted *Export with 1 problem* loses its amber. | P2 | kit | K-3 |
| 9 | project-configuring-item, project-detached-* | the `✕` on set rows | Opening the side panel hides every row's remove (`.with-drawer .set-item .row-actions`). kit.html shows the `✕` on the active row, which the screens never do. | P2 | kit | G2-9, K-2 |
| 10 | kit.css | `.field input`, textarea, `.search`, `select`, the secondary button | The edge is `--line-strong`, about 1.6–2:1. A field boundary needs 3:1 (WCAG 1.4.11). `--control-edge` (3.5:1) exists and is used only on checkboxes. | P2 | kit | K-9 |
| 11 | kit.css | `.link-button` | `button:hover` beats it, so on hover an underlined link turns into a grey chip that spills past its text. | P2 | kit | K-5 |
| 12 | kit.html, door pages | busy primary *Signing in* | It is still enabled and hoverable, with no `aria-busy`. The spinner's track is `--lime-hover` on lime (1.08:1). | P2 | kit · markup | K-7 |
| 13 | project-empty, configuring empty | disabled `Export` | The reason lives only in `title`, and the button can't take focus. Keyboard and screen-reader users never learn why it is inert, though Q16 says the inert control should teach. | P2 | markup · kit | K-8 |
| 14 | project-configuring-item, project-detached-* | the set between a 440 panel and a 440 side panel | The set column shrinks to about 350 px. Mono tokens break mid-token (`code-\nstyle`, `@\n9be4674`). This is the width cost §8 predicted. | P2 | kit · spec | G2-8 |
| 15 | run-error-setup · run-success · run-loading-export · project-detached-* | the code in a callout `.meta` · the zip name in `h2` and `.meta` · the *Lands at* input | Machine text is set in sans, which breaks Machine Reads Mono. The same 503 code is mono on run-error-check. | P2 | kit · markup | G3-8, G3-9, G3-10, G2-18 |
| 16 | project-configuring-error-server | head meta | The draft count (13) sits beside the last check's counts, which no longer describe this set. That is a stale verdict (Q26, §6). | P2 | copy · markup | G2-4 |
| 17 | projects-default | the agent-dotfiles card, `Share…` | The project is shared, but the button still says `Share…`. Q37 makes it `Stop sharing…`. | P2 | copy | G2-3 |
| 18 | projects-default vs project-revoke · Configuring pages | the `Shared` tag · the `Configuring` tag | `Shared` is an outlined pill on the card and plain text after the title. `Configuring`, a mode, is drawn as an outlined kind tag. | P2 | markup | G2-6, G2-7 |
| 19 | project-loading · project-configuring-loading | head actions | While loading, every head action is live, including `Share…`, though Share or Stop sharing can't be known yet. The configuring loading head shows only Cancel, so the head jumps when loading ends. | P2 | markup | G2-10, G2-11 |
| 20 | project-configuring-loading-add | `Export` disabled · *Adding — finding what it requires* | The project now holds an item, yet Export stays inert and nothing says why. The pending line has no busy glyph and no `role=status`. | P2 | markup · copy | G2-12, G2-13 |
| 21 | project-configuring-public | Public library panel rows | No repo, pinned `ref` or licence. §5 says a public item shows its origin, and the wireframe lacks it too. | P2 | markup · spec | G2-14 |
| 22 | run-error-check, run-error-setup | *Stopped — our server didn't answer* | A stage that broke uses the same empty circle as *Waiting*, so Stopped and Waiting can't be told apart. | P2 | kit | G3-4 |
| 23 | kit.html | missing states | Missing from kit.html: the library panel's no match, loading-add and Public scope; the side panel's loading, error and Note box; a clean *ready* Export; the aside's error; tabs with a 0 count and loading; the Run bar beyond default; an empty textarea; add-to-set *just added*; Filters closed but active. | P2 | kit | K-12, K-13, K-14, K-15 |
| 24 | kit.css | Item overlay sheet, `heading-small` | There are no classes for `sheet`, `form-section`, `field-row`, `file-list`, `dropzone`, `attach` or `heading-small`. Groups 1 and 4 can't be dressed from the kit as it stands. | P2 | kit | K-16 |
| 25 | kit.css | `.field input:focus-visible` | It loses on specificity to the base rule, so a text field never gets the lime edge on focus. Search and textarea do. | P3 | kit | K-10 |
| 26 | run-default, run-loading, run-success | the Problem box under stage 02 | It starts under the name column; DESIGN puts it under the result column. To the right is a wide, empty rose field. | P3 | kit | G3-14 |
| 27 | all Run pages | `11 · Export` | The number is sans and inline, where stages 01–10 put theirs in a mono column. On success it disappears. | P3 | kit · markup | G3-11 |
| 28 | run-error-check | `.summary` | The failure summary takes a different, stacked layout and reads as plain text at the top. | P3 | kit | G3-13 |
| 29 | Run, checked states | stages 01, 08–10 | The *Checked* dot marks things that were generated, not checked. The result lines follow no single pattern. | P3 | copy | G3-15 |
| 30 | run-default, run-success | the summary counts | They have no glyph and no tone, while the same counts on the stages do. | P3 | kit | G3-16 |
| 31 | run-loading, run-error-check | *stage 4 of 10* | There are 11 stages on the page. | P3 | copy | G3-17 |
| 32 | run-loading | `Remove eslint-autofix…` | The button is live while the check is still running. | P3 | markup | G3-18 |
| 33 | every dialog | `.scrim`, `dialog.modal` | The scrim barely dims, and uses `--veil` rather than `--veil-dialog`. On run-remove the dialog covers the Problem it is asking about. | P3 | kit | G3-19, G2-24, K-17 |
| 34 | run-success | the primary *Back to acme-billing-api* | The one lime button is spent on a way out that the Run bar already gives. | P3 | markup · copy | G3-20 |
| 35 | run-success, run-item-success, run-shared-item-success | *saved to Downloads* | We can't know where the browser saved the file. That breaks voice principle 1. | P3 | copy | G3-21 |
| 36 | all Run pages | em dashes | About nine per page, every result line in the same rhythm. The detector flags it. | P3 | copy | G3-22 |
| 37 | DESIGN.md, tokens | `--t-title` 20 / `--t-heading` 16 | The names are reversed against DESIGN.md's scale, where Headline is 20 and Title is 16. The Problem and Note box washes are not in DESIGN.md's frontmatter. | P3 | spec (lesson 08) | G3-23 |
| 38 | kit.css | duplicates | The spinner is defined twice. `.state-block` and `.tabs a` are each declared twice. Two close buttons are identical, the three bars repeat the same values, and the focus ring is spread over 7 rules. | P3 | kit | G3-24, K-20 |
| 39 | kit.css `:root` | unused values | Eight values are unused. `--panel-w` 384 contradicts DESIGN's 440, and `--acrylic-blur` contradicts DESIGN's *no blur*. | P3 | kit · spec | K-17 |
| 40 | kit.css | no hover | No hover on `.door-alt a`, `a.meta` (*Reset password*), the `library-version` summary or panel rows. | P3 | kit | K-18, G2-27 |
| 41 | kit.css | `glyph-waiting`, the Skipped outline | Both are about 1.9:1; a state mark needs 3:1. | P3 | kit | K-19 |
| 42 | kit.css | values | The scope hover's `color-mix 55%` and two `z-index` values are not variables. `sk-*` and `.door` widths are arithmetic on unrelated layout tokens, so resizing a dialog resizes skeletons. | P3 | kit | K-21 |
| 43 | kit.css | `.check`, `.scope a`, `.tabs a` | These controls are 28 px through `calc()`, with no token and nothing in DESIGN, which says 32. | P3 | kit · spec | K-22 |
| 44 | configuring panel | kind tabs | No counts. DESIGN and the inventory list them. | P3 | markup | G2-17 |
| 45 | project-detached-* | *Lands at* vs *Content* | One field shows its original inline; the other hides it behind a disclosure. | P3 | markup | G2-19 |
| 46 | project-detached-promote | the dialog's field | The label sits right under the title with no gap. | P3 | kit | G2-20, K-25 |
| 47 | project-item, project-configuring-item | `pre.file` in the side panel | Long lines are cut at the edge with no scroll cue. | P3 | kit | G2-21 |
| 48 | projects-empty vs projects-error-* | the head's `New project` | The empty state removes it; the error and no-match states demote it. One rule, two outcomes. | P3 | markup | G2-23 |
| 49 | project-default, configuring | *differs … in **content** and **lands at*** | A field name in bold mid-sentence reads as broken grammar. | P3 | copy | G2-25 |
| 50 | set pages | code-style / eslint-autofix | `Conflict` is drawn on one side of the pair only (§7, state 4). | P3 | markup · spec | G2-26 |
| 51 | project-configuring-public | panel search placeholder | Clipped at the field's edge. | P3 | copy | G2-15 |
| 52 | project-configuring-empty | `Open Public library` (primary) | It repeats the scope segment just above it, and *Open* reads as leaving the draft. | P3 | copy | G2-16 |
| 53 | kit.html | the showcase itself | A duplicate class. *grey* labels are stale after step 5. *grey* is drawn in Note amber. Library rows are cut mid-sentence. The Filters stage is mostly empty. Close is a link. | P3 | kit | K-24, K-25 |
| 54 | run-shared-* (not dressed) | `shared-header` above `run-bar` | Two 52 px bars stack. Decide before the shared Run is dressed. | P3 | spec | G3-25 |
| 55 | run-item-* (not dressed) | 10 stages for one item | Most of them are Skipped. The stack never collapses or groups them. | P3 | spec | G3-26 |

**What the agents found working:**
- the focus ring on every control they tabbed through;
- the Run stack, which reads as a deployment page;
- no success colour anywhere;
- `Export with 1 problem` naming its cost in place;
- the quiet-danger remove;
- the named `✕` labels;
- text contrast throughout. Ink 3 is still 4.55:1 on Control Hover.

---

## Disposition — the owner said *фикси*, 2026-10-19

Fixes went through four routes:
- **the kit**: `tools/build_kit.py` and `tools/build_mockups.py`, then onto every screen;
- **the wireframes' structure and copy**: [`tools/critique07_pages.py`](../../tools/critique07_pages.py), with the copy
  recorded in `microcopy.md` under *Phase 07 — the critique*. The prototypes were rebuilt from the wireframes;
- **the register**: Q39–Q41;
- **DESIGN.md**: each kit change is signed there as *Phase 07 critique*.

**Fixed (43):**
- **P1, all four**: 1 · 2 · 3 · 4.
- **P2**: 5 · 6 · 7 · 8 · 9 · 10 · 11 · 12 · 13 · 15 · 16 · 17 · 18 · 20 · 21 · 22 · 23.
- **P3**: 25 · 27 · 32 · 34 · 35 · 38 · 39 · 40 · 41 · 42 · 43 · 46 · 49 · 51 · 52 · 53.
- **Fixed in part**:
  - #19 (head actions while loading): `project-loading` now shows no action that cannot act. The configuring head
    keeping only *Cancel* is §9 and its own wireframe comment, so that half is declined.
  - #33 (the scrim): the veil is .58. That the dialog covers the Problem it asks about is declined: the dialog names
    the item and the consequence in its own sentence.
  - #37 (tokens): DESIGN.md's frontmatter now has `problem-box` and `note-box`. The reversed `--t-title` and
    `--t-heading` names go to **lesson 08, design tokens**.
  - #14 (the narrow set): mono tokens no longer break mid-token. The narrow set beside two 440 px panels is the
    width cost §8 already records.

**Declined, with the reason:**
- **#24** (no item-form classes): deferred to dressing group 1. The rule is that a component enters the kit when a
  screen needs it.
- **#26** (the finding box's column): the mockup is the truth. DESIGN.md said *under the result column*, and that
  wording is corrected.
- **#28** (the failed summary's layout): the stacked failure summary is the painted state, now set by a class.
- **#29** (the Checked dot): the dot says *done, nothing to report*. The glyph set has no *generated*, and this is the
  nearest honest mark. *The owner may want a different one.*
- **#30** (summary counts without glyphs): the counts are words (principle 4). The glyphs belong to the stages.
- **#31** (*stage 4 of 10*): the check has ten stages, and Export is the act after it.
- **#36** (em dashes): the dash in result lines is the dictionary's form (D23).
- **#44** (panel tab counts): the panel's wireframe has none, so numbers would be invented.
- **#45** (Lands at vs Content): the long field folds; the short one shows its original in place.
- **#47** (a clipped file block): it scrolls, with the styled scrollbar. The headless screenshots hid it.
- **#48** (New project on the empty Projects): the empty state's own primary is that same action, so it is not shown
  twice.

**To the register, answered by the owner the same day:**
- **#54** → **Q39**: two bars stay.
- **#55** → **Q40**: no collapse; each Skipped stage keeps its own row.
- **#50** → **Q41**: `Conflict` on both rows, applied on 11 pages and the item panel.
