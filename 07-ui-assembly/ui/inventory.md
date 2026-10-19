# UI inventory: the components the product actually has

**Phase 07, step 2. Written 2026-10-19.** Read off all 80 wireframe pages in
[`04-wireframes/pages/`](../../04-wireframes/pages/wireframes.html), with every state, against
[`03-information-architecture/sitemap.md`](../../03-information-architecture/sitemap.md). **Grey wireframes
included**: 58 of the 80 pages have no mockup yet. They count the same as the 22 painted ones.

**How it was counted.**
- **A screen** is one of the viewer's 17 screens. There are three door screens (Sign in, Create
  account, Reset password). There are three Library screens (My library, Public library,
  Import/export) and the Item overlay. There are four Project screens (Projects, Project, Configuring,
  Detached row) and four Run modes (project, single item, shared project, shared item). Then come the
  two shared surfaces (Shared project, Shared item). A page's suffix (`-loading`, `-error-server`…)
  is a **state** of its screen, not a screen.
- **A component is in the table only if it stands on two screens or more.** Anything on one screen is
  under *One-off* at the end, and does not go into the kit.
- **Overlays count the screen they lie over**, because the page draws it. The Item overlay and
  Import/export pages show the Library behind them. That is why some Library components count those
  two as well.
- Names are the wireframes' own class names, in `code`, so step 3 can find every occurrence.
  **Nothing is invented**: a component the course's demo has (chat bubble, verification-code field,
  tab bar, banner carousel) is absent here because no wireframe draws it.
- **Image**: does the component need a picture. Only the **portrait** does. Items are files, folders
  and repos, so the product has no content photography (`PRODUCT.md`, *Evidence on hand*). Step 4
  (own visuals) was skipped by the owner on 2026-10-19, and the one portrait stays.
- **Painted** means the component is already drawn in a mockup (`04-wireframes/mockups/`), so the kit
  must **reproduce** it. **Grey** means step 3 takes its structure from the wireframe and its look
  from `DESIGN.md`.

---

## Navigation

| Component | Screens | States | Image | Painted |
|---|---|---|---|---|
| **App header** — product mark · global nav · signed-in person (`app-header`, `app-nav`, `account`) | 8: My library, Public library, Import/export, Item overlay, Projects, Project, Configuring, Detached row | current place (`aria-current`) for each of the three places · hover · focus | **yes**: the owner's portrait, 24 px (`avatar`) | yes |
| **Shared header** — product mark, and the sharer when there is one (`shared-header`, `owner`) | 7: Sign in, Create account, Reset password, Shared project, Shared item, Run shared project, Run shared item | **two variants**: *door* (mark only, on the three door screens) · *shared* (*Shared by Maya Chen* with a portrait, on the four receiver screens) | **yes** on the shared variant: the sharer's portrait | no |
| **Run bar** — back to where it was entered · `Export` · agent target (`run-bar`, `back`, `title`, `pick`) | 4: Run project, Run single item, Run shared project, Run shared item | follows the Run states (loading · default · exporting · exported · error) | no | yes (Run project) |
| **Breadcrumb** — `Projects /` above the name (`meta` > link) | 3: Project, Configuring, Detached row | default · hover | no | yes |
| **Page head** — title, head meta, head actions (`page-head`, `head-meta`, `head-actions`) | 10: My library, Public library, Import/export, Item overlay, Projects, Project, Configuring, Detached row, Shared project, Shared item | with or without actions · the `Shared` and `Example` tags after the title · loading (skeleton meta) | no | yes |
| **Tabs** — kind tabs with counts (`tabs`; on a page `tabs-page`, with `count`) | 7: My library, Public library, Import/export, Item overlay (page tabs) · Project, Configuring, Detached row (panel tabs, `Related · All · six kinds`) | current tab · hover · a count of 0 · scrolls rather than wraps · loading | no | panel tabs: no · page tabs: no |
| **Scope switch** — `My library · Public library` as a segmented control (`scope`) | 3: Project (its empty state), Configuring, Detached row | current segment · hover · focus | no | no (drawn on the stand) |
| **Library panel** — the configuring sidebar: head with scope, search and tabs; body with rows (`library-sidebar`, `panel`, `panel-head`, `panel-body`, `config-layout`) | 3: Project (empty), Configuring, Detached row | default · empty (`No items in My library yet`) · no match · loading · loading-add · Public scope | no | no |

## Cards and lists

| Component | Screens | States | Image | Painted |
|---|---|---|---|---|
| **Row list** — the tray of item rows (`row-list` > `row`; variants `row-tight`, `row-compact` in the panel, `set-item` in a project) | 8: My library, Public library, Import/export, Item overlay, Project, Configuring, Detached row, Shared project | default · hover · **active** (`is-selected`, 3 screens) · loading (skeleton rows) | no | yes (`set-item`) · no (library rows, panel rows) |
| **Item text block** — name + kind tag + description + facts line (`description`, `facts`, mono path) | 9: My library, Public library, Import/export, Item overlay, Projects, Project, Configuring, Detached row, Shared project | with or without description · facts with `defers to`, `conflicts with`, `needs ENV`, `@ ref · licence` | no | yes |
| **Set row states (§7)** — the row in a project: auto-added nested under its parent (`sub-rows`), `Conflict` tag, finding marks, the *detached* state line (`state-line`) | 3: Project, Configuring, Detached row (+ `state-line` on Shared project) | selected · auto-added (nested, 1–2 levels) · conflicting · missing an env key (Note) · detached (differing fields named) · active | no | yes (Project) · no (configuring, detached) |
| **Kind tag** — outlined pill (`tag`) | 10: My library, Public library, Import/export, Item overlay, Projects, Project, Configuring, Detached row, Shared project, Shared item | **variants**: kind (`skill` … `app`) · `Shared` (15 pages) · `Example` (Projects) · `Conflict` (3 screens, in rose) · `Auto-added` (`tag-state`, 3 screens, no outline) | no | yes |
| **Usage facts** — *used in 3 projects*, *2 items require this* (`usage`) | 3: My library, Import/export, Item overlay | default | no | no |
| **Item side panel** — the item opened beside the set: head with close, sections, facts list, actions (`drawer`, `drawer-head`, `drawer-section`, `drawer-facts`, `drawer-actions`, `with-drawer`) | 3: Project, Configuring, Detached row | open on a linked item · on a detached item (differing fields, `Reset`, `Promote`) · with a Problem or Note box · loading · error | no | yes (Project) |
| **Check stages** — numbered stages with result and time, each a disclosure (`stages`, `stage-group`, `n`, `name`, `result`, `time`, `stage-body`) | 4: Run project, Run single item, Run shared project, Run shared item | waiting · running · checked · problem · note · skipped · expanded | no | yes (Run project) |
| **Run summary** — the verdict line and counts (`summary`) | 4: the four Run modes | checking · checked with counts · error (code in mono) | no | yes |
| **Export stage** — the last stage, which makes the archive (`export-stage`, `export-actions`) | 4: the four Run modes | ready · ready with a Problem (`Export with 1 problem`) · exporting (`role=status`) · exported (`plain-list` of what is inside) · failed (`role=alert`) | no | yes |
| **File block** — a file's contents or a path tree in mono (`pre.file`) | 7: Project, Configuring, Detached row, Run project, Run single item, Run shared item, Shared item | default · scrolls sideways | no | yes |
| **Plain list** — a dash list of facts (`plain-list`) | 7: Project, Run project, Run single item, Run shared project, Run shared item, Shared project, Shared item | default | no | yes |
| **Aside box** — *What your machine still needs*, with the Export action (`with-aside`, `aside-box`) | 2: Shared project, Shared item | default · loading. *There is no error state of its own: on error the dead-link state replaces the page (corrected in step 6).* | no | no |

## Forms

| Component | Screens | States | Image | Painted |
|---|---|---|---|---|
| **Button** (`button`, `button-primary`, `button-quiet`) | 17: every screen | **variants**: primary · secondary · quiet (4 screens) · destructive confirm (the wireframes mark it as primary; the mockups draw it red) · `Export with 1 problem` (mockups: warning) · with an icon · **disabled** (`Export` on an empty project; 4 pages, Project + Configuring) · **busy** (`glyph-running` + *Signing in*, on the door screens) · hover · focus | no | yes (most variants) · busy: no |
| **Link button** — an action set as a link (`link-button`) | 5: My library, Public library, Projects, Item overlay, Detached row | default · hover · focus | no | yes (*Clear filters*) |
| **Search field** — icon + input (`search`, inside `find`) | 8: My library, Public library, Import/export, Item overlay, Projects, Project, Configuring, Detached row | empty with placeholder · filled (the no-match state) · focus | no | yes (Projects) · panel search: no |
| **Filters button and popover** — `Filters` hangs a popover: groups, checkboxes or radios, *Clear* + apply (`filters-button`, `find-zone`, `popover`, `popover-head/body/group/foot`) | button 5: My library, Public library, Import/export, Item overlay, Projects · popover 3: My library, Public library, Projects | closed · open · with active filters | no | yes (Projects) |
| **Text field** — label over input (`field`; `field-label` with an inline link on Sign in) | 5: Sign in, Create account, Reset password, Item overlay, Detached row | empty · placeholder · filled · while submitting. **No per-field error**: errors arrive as an alert box (see Feedback) | no | no |
| **Select** (`select`) | 5: Item overlay (*Kind*) · the four Run modes (*Agent target*) | default · focus | no | yes (agent target) |
| **Textarea** (`textarea`) | 2: Item overlay, Detached row | default · filled | no | no |
| **Add to set** — *+ Add* / *✓ In this project* over a hidden checkbox (`check`) | 3: Project (empty), Configuring, Detached row | not in the set · in the set · hover · focus · just added: the row at once, what it requires after the round trip (`loading-add`) | no | yes (CSS ready; screen not painted) |
| **Checkbox** (`input[type=checkbox]` in the popover) | 3: My library, Public library, Projects | unchecked · checked · hover · focus | no | yes |
| **Radio** (`input[type=radio]` in the popover) | 2: My library, Projects | unselected · selected · focus | no | yes |
| **Remove from set** — the `✕` on a set row, with a named aria-label (`remove`) | 2: Configuring, Detached row | default · hover · focus · absent on an auto-added row (the refusal) | no | no |
| **Close** — the `✕` of a panel or sheet (`close`) | 5: Item overlay, Import/export, Project, Configuring, Detached row | default · hover · focus | no | yes |
| **Form actions** — Cancel … primary, the primary pushed right (`form-actions`, `push`) | 6: Item overlay, Import/export, Projects, Project, Detached row, Run project | default | no | yes |
| **Door form** — the signed-out page: title and lead, a form, an alternative link under it (`door`, `form`, `door-alt`) | 3: Sign in, Create account, Reset password | default · loading · error · (Reset password) success | no | no |

## Feedback

| Component | Screens | States | Image | Painted |
|---|---|---|---|---|
| **Finding box** — a severity label, the sentence, actions (`callout` = Problem, `callout-quiet` = Note, `severity`) | 11: Sign in, Create account, Import/export, Item overlay, Project, Configuring, Detached row, Run project, Run single item, Run shared project, Run shared item | **variants**: Problem · Note · **our failure** (`role=alert`: *Our server didn't…*, on 10 screens) · **keys reminder** (*Check that these files carry no keys*: Item overlay, Import/export) | no | yes (Problem, Note) · our failure: partly · reminder: no |
| **Finding capsule** — icon + word on a set row (`marks`, `mark`) | 3: Project, Configuring, Detached row | Problem · Note | no | yes |
| **Severity glyph** (`glyph-problem`, `-note`, `-checked`, `-skipped`, `-waiting`, `-running`) | 9: Sign in, Create account, Project, Configuring, Detached row, the four Run modes | problem · note · checked (dot) · skipped (`ban`) · waiting · running (spinner) · **stopped** (`cloud-off`, our server broke mid-stage — added in step 6) | no | yes |
| **Empty and error state** — a tile, a title, a sentence, actions (`state-block`, `state-icon` / `state-image`, `state-actions`) | 7: My library, Public library, Projects, Project, Configuring, Shared project, Shared item | **empty** (*No items in My library yet*, *No projects yet*, *No items in this project yet*) · **no match** (*Nothing matches “…”*) · **server error** (*… didn't load*, with a mono code) · **dead link** (*This link doesn't open anything any more*) | the wireframes draw an image placeholder (`state-image`) on 4 pages; **no photo**: the mockups draw one neutral icon tile (owner, phase 06) | yes (Projects, Project) · no (the rest) |
| **Skeleton** (`skeleton`) | 10: My library, Public library, Import/export, Item overlay, Projects, Project, Configuring, Detached row, Shared project, Shared item | shimmering · still under reduced motion. Widths are inline styles today, to become kit classes | no | yes (Projects, Project) |
| **Busy indicator** — spinner with a status line (`glyph-running`, `role=status`) | 6: Sign in, Create account, the four Run modes | running · stopped under reduced motion | no | yes (Run) |
| **Dialog** — a sheet over a scrim: title, sentence, sometimes a box, actions (`modal`, `sheet-head`, `scrim`) | 6: Projects (*Delete repo-triage-kit?*), Project (*Share … by link?*, *Stop sharing …?*), Run project (*Remove eslint-autofix …?*), Item overlay (*Delete db-migrate?*), Import/export (*Import a library*), Detached row (*Promote pr-reviewer to My library?*) | **variants**: destructive confirm (delete, remove, stop sharing) · disclosure confirm (share) · neutral confirm (promote) · import with **progress**, **error** and **result** | no | yes (Projects, Project, Run) · no (Item, Import, Promote) |

---

## One-off: not pulled into the kit

Each stands on one screen only. They stay part of their screen and are drawn there from kit parts.

- **Project card and card grid**, with the verdict block at the foot (`card-grid`, `card`, `verdict`).
  **Projects only.** *It is the most visible one-off; if a second screen ever lists projects, it moves
  into the kit.*
- **Item form sheet**: sections, a two-field row, the file list, the drop zone, *Attach a repo*, the
  hint (`sheet`, `form-section`, `field-row`, `file-list`, `dropzone`, `dropzone-small`, `attach`,
  `hint`). **Item overlay only.**
- **The blast-radius box**: *Used in 3 projects · saving un-checks all three*, as a Note box with the
  projects named. **Item overlay only**, though it is built from the Finding box.
- **The original of a detached field**: a disclosure *Original · Reset this field* holding the
  library version (`library-version`). **Detached row only.**
- **Small heading** in the shared item's aside (`heading-small`). **Shared item only.**
- **Field label with an inline link**: *Password · Reset password* (`field-label`). **Sign in only.**
- **Row-width variants** `row-1` (Shared project) and `row-2` (Public library). These are grid
  variants of the row, not components.

- **Import progress**: the bar under *18 of 47* while a library imports. **Import/export only.** The
  wireframe draws it as a skeleton with an inline gradient; the kit draws it as a native `<progress>`
  (`progress`), its value taken from the count above it. *Added in step 5, when screens stopped holding
  styles of their own.*

**One-offs that still need a class.** A dressed screen holds no style of its own (step 5), so a one-off
that needs a look gets its class in `kit.css` and a line on `kit.html`, and stays out of the table:
`library-version` (the detached field's original, a quiet disclosure) and `progress`.

**Not components at all:**
- `visually-hidden` and `description-wide` are utilities;
- `product-page`, `app-main` and `icon` are the page frame and the icon slot. They carry the shell
  for step 3.
- The **unclean-export confirmation** is a state of the Export stage, not a dialog (sitemap,
  *Places, modes, overlays and states*).

---

## What this means for step 3

- **The kit holds 41 components across the four groups.**
  - **15 are painted in full** and must be reproduced exactly.
  - **17 are painted in part**: on some screens or in some variants.
  - **9 are not painted at all**: shared header, scope switch, library panel, usage facts, aside box,
    text field, textarea, remove from set, door form.

  The unpainted ones and the unpainted variants take their structure from the wireframes and their
  look from `DESIGN.md`.
- **The shell has three variants, not one**:
  1. the **app header** for the owner's places;
  2. the **shared header**, door or receiver, with no account;
  3. the **Run bar** for the mode.

  The configuring head (*Cancel · Export · Save*) is a mode head inside the Project, not a shell.
  *This is the instructor's finding from the recording, borne out by the count.*
- **One empty/error state with four variants, not one per screen.** It is already one tile in the
  mockups, and the kit keeps it one class.
- **The busiest unpainted components** are the library panel and its rows, the text field, the door
  form, the dialog's import variants, and the *our failure* box. Painting groups 0 and 1 in step 5
  will exercise all of them.
- **The only image is the portrait**, in two headers.

---

## Step 5 — what dressing the screens added

- **Group 2, *What I am putting together*, is dressed** (2026-10-19): Configuring and Detached row, 12
  pages, beside Projects and Project. These components moved from *grey* to *painted*: library panel,
  scope switch, panel tabs, add to set, remove from set, the configuring set-row states, the detached
  item side panel, and text field and textarea (in the side panel).
- **Into the kit on the way**: skeleton sizes as classes (`sk-w48`, `sk-h24`, `sk-mt8` — every size any
  wireframe uses); the sprite's position (`svg.sprite`); `progress`; `library-version`; and **one primary
  per screen** extended from empty states to error boxes — an error box with its own primary demotes the
  head's (*Save again* beside *Save*).
- **An empty state's tile is the empty-set icon** (`layers`), not the alert circle: the panel's *No items in
  My library yet* is not an alarm.

---

## Step 6 — what the critique changed in the kit

The critique is in [`critique.md`](critique.md), and its disposition is at the end of that file. These changes are
to the components in this table.

- **Finding box**: *our failure* is now its own class, `callout-failure`. It is neutral, as the keys reminder is,
  because neither is a finding.
- **Export stage**: it has state classes, `is-exported` and `is-failed`. A failed stage is neutral.
- **Run summary**: when the run fails, its summary gets the state class `is-failed`.
- **Check stages**:
  - a stage with something inside has a chevron and a hover;
  - a stage with nothing inside (`stage-empty`) takes no focus;
  - Skipped is drawn by the class `is-skipped`;
  - the waiting ring and the Skipped outline are now at 3:1.
- **Severity glyph**: the new *stopped* glyph.
- **Add to set**: a new *auto-added, refuses* state, with the checkbox disabled.
- **Button**:
  - a primary that has been demoted is drawn as a real secondary;
  - *busy* is `aria-busy`;
  - *disabled* takes focus (`aria-disabled`);
  - the link button keeps its look on hover.
- **Text field, search and select**: the edge is now Control Edge, at 3:1. A field holding a path, a name or a key
  is mono (`field-mono`).
- **Error codes**: wherever they stand, they carry `error-code`, which is mono Ink 3.
- **Dialog**: the veil is .58, and a field inside it sits 16 below the title.
