# Critique — lesson 04 wireframes and prototypes

> **Written 2026-09-27, by a reviewer who did not draw them.** Reviewed: the 66 product pages in
> [`pages/`](pages/) (the viewer `wireframes.html` and `wireframe.css` only for leaks into the canvas),
> and the 37 cases in [`prototypes/`](prototypes/). Judged against [`_conventions.md`](_conventions.md),
> [`_screens.md`](_screens.md), [`prototypes/_conventions.md`](prototypes/_conventions.md),
> [`prototypes/prototypes.md`](prototypes/prototypes.md),
> [`sitemap.md`](../03-information-architecture/sitemap.md),
> [`flows.md`](../03-information-architecture/flows.md) and the register, Q29–Q34
> ([`research-plan.md`](../research/research-plan.md)). Things the rules allow — the black icon
> square, the crossed image box, the viewer's orange chrome and hotspots, kind tabs pointing at `#` —
> are not reported.

**23 defects: 6 × P1, 6 × P2, 11 × P3.** Nine were fixed in `pages/`; the rest need the owner or
belong to the prototype build. Nothing under `prototypes/`, `CLAUDE.md`, `sitemap.md`, `flows.md` or
the register was touched.

Priority: **P1** dead ends and missing states · **P2** no main action, or off the map · **P3** look and
placeholders.

---

## The table

| # | Screen / file | What is wrong | How to fix | Rule | P | Status |
|---|---|---|---|---|:-:|---|
| 1 | `sign-in-default`, `-error`, `-loading` | *Create an account* links to `sign-up-default.html`, which does not exist — a 404 from the door | Make the link inert until the page exists or is dropped | `_conventions.md` §5, *no dead end* | P1 | **Fixed** (inert) |
| 2 | **Create account** (`sign-up-*`) | `_screens.md`'s whole-map table marks default · error · loading `✓`; no page exists | Draw the three pages — or drop the row (see #9) | `_conventions.md` §5, *only the states `_screens.md` marks `✓`*; `_screens.md`, *The whole map* | P1 | Owner |
| 3 | `project-configuring-empty` | The empty panel's primary way out, **Switch to Public library**, is `href="#"`, as is the scope switch. The other way, *Add item*, opens `item-empty.html` over My library, whose Cancel and close land on `library-my-default` — out of the draft | Draw the panel on the Public scope in `pages/` (the prototype has it: `main-first-run/03`, marked new) and point the button at it | `_conventions.md` §5; `_screens.md` §3, *Empty — ways out* | P1 | Owner |
| 4 | `project-detached-error` | A server error with one way out, *Promote again*, which depends on the server; no code and time | Add a second way that does not depend on it, and the grey code line | `_conventions.md` §5, *a second one … that does not depend on it*; *the code and time in small grey text* | P1 | **Fixed** |
| 5 | `run-error` | `_screens.md` §4 gives Run's error three causes with different ways out — the check cannot complete · a generated disclosure was not produced (Q28) · the export fails. Only the export failure is a page. The other two exist only in prototypes (`main-error-check/04`, `rj1-preview-failed/03`), marked new | Keep them into `pages/` as `run-error-check` and `run-error-setup`; rename this one `run-error-export` | `_conventions.md` §4, *a state with more than one cause takes the cause as a suffix*; §5, Q28 | P1 | Owner |
| 6 | `run-loading` | `_screens.md` §4 names a second wait, *building the archive at Export*; no page draws it (prototype `run-exporting`, new) | Keep it into `pages/`, e.g. `run-loading-export` | `_screens.md` §4, *Loading ✓*; `_conventions.md` §4 | P1 | Owner |
| 7 | `shared-project-error`, `shared-item-error` | The dead link's only action, **What is AI Stack Builder?**, goes to `sign-in-default`. The label promises an explanation and delivers a door; §9 and Q25 say a receiver meets the sign-in *only* by choosing *copy into my library*; `flows.md` ends this branch *Stuck: nothing to fall back on*. The page satisfies one rule by breaking two | Decide which rule wins: an honest `Stuck` with no action, or a way out that exists on the map | `CLAUDE.md` §9; Q25; `flows.md`, *The receiver*, decision 1; `_conventions.md` §5 | P2 | Owner |
| 8 | `sign-in-*` | *Forgot password?* and *Reset password* (the error's primary way out) are `href="#"`: a password-reset flow is on neither the sitemap nor `flows.md`, and Q25 leaves *what the way in is* undecided | Put reset on the map, or remove it from the door | `_conventions.md` §5; Q25 | P2 | Owner |
| 9 | **Create account** | Listed in `_screens.md` and linked from the door, but not in `sitemap.md` (six places, Sign in the only door) and not in `flows.md`; Q25 builds *the minimum and nothing beyond it* and says the matrix must be re-run over whatever is added | Register entry: add it to the map, or drop the link and the tree entry | Defect class 6; Q25 | P2 | Owner |
| 10 | `project-configuring-error-server` | *Not added — the server didn't confirm it … Add again* describes an add persisted on the spot. Q33 made configuring a draft kept by *Save*; `prototypes.md` says *Save didn't land* replaces it. The page is stale, and shows *Tried just now* instead of a code and time | Keep the prototype's *Not saved · Save again · Discard changes* (`main-error-save/05`) into `pages/` in its place | Q33 §4; `prototypes.md`, *Pages the prototypes drew* | P2 | Owner |
| 11 | `item-default`, `item-error` | *Delete item…* promises a dialog that is drawn nowhere. §5 (Q17) fixes its words — *used in 3 projects · deleting it may stop them working*, the count expanding to name them, the dangling `requires` said too | Draw it as `run-remove` is drawn, a modal over the sheet | `CLAUDE.md` §5, Q17 | P2 | Owner |
| 12 | Share and Stop sharing (Projects cards, Project head, My library rows); *Promote to My library…*; *Delete example* | Every one opens a dialog that exists only in a prototype, marked new — the share disclosure (`rj4-share/02`), revoke (`rj4-revoke/02`), promote (`rj3-detached-promote/03`), delete example (`main-no-projects/02`, which `prototypes.md`'s new-pages table does not list) | Keep or reject each; kept ones move into `pages/` and the tree | `prototypes/_conventions.md` §1, *a prototype never quietly becomes the only place a screen exists* | P2 | Owner |
| 13 | `run-default`, `-error`, `-remove`, `-success` | Stage 05 says *2 keys named* while `.env.example` and the success page carry 3 — `SENTRY_AUTH_TOKEN` (sentry-mcp) was missing. Already caught in `prototypes.md` | Name all three | `_conventions.md` §3, real text | P3 | **Fixed** |
| 14 | `run-shared-item-default`, `-success` | *6 skipped* over five `Skipped` stages (02, 03, 05, 07, 10) | *5 skipped*. `_screens.md` still says 6 | `_conventions.md` §3 | P3 | **Fixed** (page) |
| 15 | `projects-filters` | *Delete example* still drawn quiet (`button-quiet`) — the look Q34 retired because it read as disabled; `projects-default` has it plain | Plain button | Q34 §3 | P3 | **Fixed** |
| 16 | `wireframe.css` — `dialog.popover` | A drop shadow on the Filters popover, in the canvas | Remove it; the border already separates it | `_conventions.md` §7, *shadows* wait | P3 | **Fixed** |
| 17 | `wireframe.css` — `.avatar`, `.skeleton`, `.glyph-running` | Radii beyond the icon placeholder: the avatar's crossed box drawn as a circle (the image placeholder is a square); a 2 px radius on skeleton bars; the running glyph a circle with a gap — a spinner by another name | Square all three; the running glyph keeps its open top edge | `_conventions.md` §1 *images*, §5 *no spinner*, §7 *radii* | P3 | **Fixed** |
| 18 | `wireframe.css`; `project-loading`, `project-configuring-loading` | Off the 4 px grid: `.row-tight .description` 2 px, `.severity .glyph` 6 px, skeleton `margin-top: 6px` ×28 | 4 px, 8 px, 8 px | `_conventions.md` §1, *4 px grid* | P3 | **Fixed** |
| 19 | `project-configuring-empty` | *8 checked items* — *checked* is the verdict word, here worn by items as if they had a verdict | *8 items, each pinned to the version we checked* (§5's own wording) | `_conventions.md` §3, *checked, never works*; `CLAUDE.md` §5 | P3 | **Fixed** |
| 20 | `project-default`, `project-item`, `shared-project-default`, `shared-item-default`, `project-configuring-error-server` | Inline `style` outside the skeletons — `max-width: 800px` on descriptions, a font size on an `h2`, a margin on a callout | Move each into a class in `wireframe.css` | `_conventions.md` §6, *a product page carries no `<style>` of its own* | P3 | Not fixed — cosmetic |
| 21 | `item-default`, `item-error`, `library-my-*`, `run-item-*` | The `db-migrate` ↔ `seed-data` edge runs both ways. Project and Run: *seed-data for db-migrate* (db-migrate requires it). Item sheet: *2 items require this: migration-reviewer, seed-data*, with *Requires* empty. `seed-data` is in the project but not among My library's 10 items, and `run-item` exports migration-reviewer as 3 items where the project says it brings 3 | Settle the direction once (the main job's data says db-migrate → seed-data), then correct the sheet, add `seed-data` to My library and its counts, and make the single-item export 4 items | `_conventions.md` §3, real text | P3 | Not fixed — six pages and the tab counts |
| 22 | `shared-project-default` | *3 repos cloned at pinned refs*, but `filesystem` and `memory` share `modelcontextprotocol/servers` at one ref — two clones for three external items. `run-shared-success` repeats *the 3 external repos* | Say *3 external items from 2 repos*, or count per item on purpose | `_conventions.md` §3 | P3 | Not fixed |
| 23 | `_conventions.md` §4 | The naming list has no form for a page with a modal or panel open — `run-remove`, `project-item`, `project-configuring-item` are justified by Q33 and Q34 but not by §4, and the prototypes coined `run-exporting`, `projects-delete`, `project-share`, `project-revoke` | Add the rule to §4 once: `<name>-<what is open>.html`, like `-filters` | `_conventions.md` §4 | P3 | Owner (doc) |

---

## Fixed

- **`sign-in-default.html`, `sign-in-error.html`, `sign-in-loading.html`** → *Create an account* pointed
  at a page that does not exist → the link is inert (an `a` with no `href`, the prototypes' own form for
  a link that goes nowhere yet), with an HTML comment saying why.
- **`project-detached-error.html`** → a server error whose only way out depended on the server → added
  **Dismiss** (the second button `project-configuring-error-server` already uses: the row stays
  detached, the edits stay) and the grey line *503 · Service unavailable · 14:02*.
- **`run-default.html`, `run-error.html`, `run-remove.html`, `run-success.html`** → *2 keys named* →
  *3 keys named*, and the Note names `SENTRY_AUTH_TOKEN` (sentry-mcp), in the prototypes' exact words.
- **`run-shared-item-default.html`, `run-shared-item-success.html`** → *6 skipped* → *5 skipped*.
- **`projects-filters.html`** → *Delete example* lost `button-quiet`, matching `projects-default` (Q34).
- **`project-configuring-empty.html`** → *8 checked items* → *8 items, each pinned to the version we
  checked*.
- **`wireframe.css`** → removed the popover's `box-shadow`; removed the radii on `.avatar`, `.skeleton`
  and `.glyph-running`; `.row-tight .description` 2 → 4 px, `.severity .glyph` 6 → 8 px. The prototypes
  load this stylesheet, so they pick these up too.
- **`project-loading.html`, `project-configuring-loading.html`** → skeleton `margin-top: 6px` → `8px`.

Checked after: every relative `href` on every product page resolves to a file that exists; no product
page has a `<style>` or `<script>`; no colour was added. `project-detached-error.html` loads from the
local server.

## Not fixed — needs the owner

1. **Create account (#1, #2, #9).** It is in `_screens.md` and the tree, linked from the door, and on
   neither the sitemap nor `flows.md`. **Is it a screen of this product?** If yes, it needs a register
   entry and a place on the map before its three pages; if no, the link and the tree entry go.
2. **Password reset (#8).** *Forgot password?* and the error's *Reset password* go nowhere. **Does the
   door carry a reset flow, and where is it on the map?** Q25 left *what the way in is* open.
3. **The dead link (#7).** The page sends an anonymous receiver to Sign in under the label *What is AI
   Stack Builder?* **Which wins — `flows.md`'s declared `Stuck: nothing to fall back on` (no action), or
   `_conventions.md` §5's *every error carries a way on*?** If the second, the way on has to be one the
   map already has, and the only candidate is a door Q25 says this person never meets.
4. **Pages drawn only in prototypes, marked new (#3, #5, #6, #10, #12).** Each one closes a defect in
   `pages/` the moment it is kept: the panel on the Public scope, the two further Run errors, the
   archive build, *Save didn't land*, the share disclosure, Stop sharing, Promote, Delete example. **Keep
   or reject each?** Kept ones need a `pages/` name (#23) and a line in the tree.
5. **Delete item (#11).** §5 writes its words; no page draws it. **Draw it as a modal over the sheet, like
   `run-remove`?**
6. **`_screens.md`** still says the shared single-item run is *6 skipped*; the pages now say 5.

## Prototype defects

Not edited — the prototypes are generated from `pages/`. Each is a place where the build needs a rule.

- **Form actions are not rewired.** 17 steps keep `<form class="find" action="projects-default.html">`
  from the wireframe. The search form has one text field and no submit button, so **Enter in the search
  field submits it — to a file that is not in the case folder, a 404** — a second, broken way forward.
  Steps: `01-projects-default` in `main-create-item`, `main-error-check`, `main-error-export`,
  `main-error-project`, `main-error-save`, `main-first-run`, `main-new-project`, `main-no-projects`,
  `main-problem-exported`, `main-problem-fixed`, `main-set-incomplete`, `main-success`,
  `main-target-changed`; `main-error-projects/02` and `/03`; `main-no-projects/02`;
  `rj3-edit-reaches-all/04`. The build should strip `action` the way it strips an off-path `href`.
- **`receiver-copy/02-sign-in-default`** keeps `action="sign-in-loading.html"`, not in the folder.
  Latent — two text fields block implicit submission — but the same fix.
- **Steps named after a wireframe they are not.** `prototypes/_conventions.md` §2 says a step carries
  *the wireframe's own name*; these carry a name whose page in `pages/` shows something else:
  `main-error-check/04-run-error` (the check didn't finish; `pages/run-error` is the export failure),
  `rj1-preview-failed/03-run-error` (`SETUP.md` not written), `main-create-item/05-item-empty` (the
  sheet over configuring), `rj2-auto-added-holds/02-project-configuring-item` (an auto-added row),
  `rj3-detached-promote/03` and `rj3-promote-failed/03-project-detached-default` (the Promote dialog),
  the `project-configuring-loading` steps `main-first-run/04` and `/06`, `main-new-project/03` and
  `/05`, `main-no-projects/05` and `/07` (the add's round trip; `pages/` has the mode opening),
  `main-first-run/01-projects-default` (only the example). A reviewer opening *the wireframe for this
  step* from the viewer gets a different screen.
- **Names outside the state vocabulary:** `run-exporting`, `projects-delete`, `project-share`,
  `project-revoke` (#23).
- **`prototypes.md`'s table of new pages omits the *Delete example* confirmation**
  (`main-no-projects/02-projects-delete`), which Q34 introduced.

Every case otherwise holds: each step has exactly one live link or one 2-second wait, off-path links
have no `href`, no step uses `#`, every ending has no way forward, and no prototype page carries a
`<style>` or `<script>`.

---

## Closed — 2026-09-27, Q35

**The owner answered *fix all*.** Every row above is closed; the choices for the six owner questions were
proposed with the fix and are recorded as such in the register ([Q35](../research/research-plan.md)).

| # | Closed by |
|---|---|
| 1, 2, 9 | **Create account on the map**, drawn at the minimum — `sign-up-default`, `-error`, `-loading`; the door links to it again |
| 8 | **Reset password on the map** — `password-reset-default`, `-success`; *Forgot password?* and the error's *Reset password* go there |
| 3 | `project-configuring-public` kept; *Switch to Public library* and the scope switch point at it |
| 5 | `run-error-check`, `run-error-setup` kept; `run-error` renamed `run-error-export` |
| 6 | `run-loading-export` kept; *Export with 1 problem* goes through it |
| 7 | **The dead link keeps no action** — `flows.md`'s `Stuck`; `_conventions.md` §5 names the exception |
| 10 | `project-configuring-error-server` replaced by *Not saved · Save again · Discard changes*, with the code and time |
| 11 | `item-delete` drawn in Q17's words; *Delete item…* opens it |
| 12 | `project-share`, `project-revoke`, `project-detached-promote`, `projects-delete` kept; the controls that open them are links |
| 20 | The inline styles are classes — `.description-wide`, `.heading-small` |
| 21 | **`db-migrate` requires `seed-data`** everywhere; `seed-data` joins My library (11 items, script 3); the single-item export of `migration-reviewer` is a set of 4 |
| 22 | *3 external items, cloned from 2 repos* |
| 23 | `_conventions.md` §4: `<name>-<what is open>.html`, and cause suffixes |
| — | `_screens.md`: the shared single-item run says 5 skipped |

**Prototype defects, closed in the build.** Form `action`s are stripped like off-path `href`s — Enter in a
search field goes nowhere; **every step is now named after a page that exists in `pages/`** (checked by
script: 239 steps, 0 without a page); the renamed steps are `run-loading-export`, `run-error-check`,
`run-error-setup`, `run-error-export`, `project-configuring-loading-add`, `project-configuring-public`,
`project-detached-promote`; the Delete example confirmation is in `prototypes.md`'s table. All 37 cases
rebuilt and walked.
