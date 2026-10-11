# DESIGN-artifacts — how the phase pages look

**This file describes the course pages, not the product.** The pages are where the work of each
phase is published on Vercel: `research.html`, `personas.html`, `ia.html`, `voice.html`, and every
phase page after them. **AI Stack Builder itself has no visual language yet.** It gets one in phase
06, concept (`06-concept/`), and it is recorded in `DESIGN.md` in phase 07.

> **Nothing here may leak into the product.** The paper ground, the orange `#e05f03`, Special
> Gothic Expanded One and the 10 px bordered boxes belong to the pages. A model or a tool that is
> choosing the product's palette must not read this file as a source. That is why it is not named
> `DESIGN.md`: tools such as impeccable pick that name up automatically as the product's design
> authority (`06-concept/references.md` §1 named this leak).

*Written 2026-10-11, from the code as it stands. The code is the source of truth. Where this file and
`tools/research-page.tpl.html` disagree, the template wins and this file is corrected.*

---

## 1. Where the language lives

- **One shared `<style>` block, in `tools/research-page.tpl.html`.** Every other phase page has its
  CSS lifted from it at build time (`build_personas.py`, `build_ia.py`, `build_voice.py`), so the
  pages cannot drift. **Edit the tokens and the shared components there and nowhere else**, then
  rebuild every page (`tools/README.md`).
- **A page template adds only its own components**, in a small `<style>` of its own. It never
  redefines a token or a shared component.
- **The origin is the owner's portfolio, r-o-design.tech**, which uses the same tokens, the same type
  pairing and the same border-led grammar. The course site uses the same orange family.
- **The wireframes are a different world**: `04-wireframes/pages/wireframe.css`, grey on white,
  Inter, no colour. They share only the phase rail with these pages. **Nothing below applies to
  wireframe content.**

---

## 2. Tokens

Light is the default. Dark follows `prefers-color-scheme` and can be forced with `data-theme`. Both
themes are written out in full, in all three places the template repeats them. **A token added to one
theme is added to both.**

| Token | Light | Dark | What it is for |
|---|---|---|---|
| `--paper` / `--bg` | `#f9f9f7` | `#161614` | The page ground: warm paper, not white |
| `--surface` | `#fdfdfb` | `#1e1e1c` | Boxes on the page: tables, cards, panels |
| `--sunken` | `#f0f0ee` | `#121210` | One tone below the page: the phase rail, table heads, an open `<details>` |
| `--surface-hover` | `#ebebea` | `#232321` | Hover on a row or a summary |
| `--ink` | `#0d0d0d` | `#f0efe9` | Headings and body |
| `--ink-2` | `#3f3f3d` | `#ababab` | Secondary text: standfirst, descriptions, captions |
| `--ink-3` | `#5a5a56` | `#909090` | Tertiary: labels, counts, metadata |
| `--rule` | `#d4d4cf` | `#52524f` | A box's border, a section's hairline |
| `--rule-soft` | `#e2e2dd` | `#3a3a37` | Lines inside a box |
| `--accent` | `#e05f03` | `#f57722` | Links, the current phase and tab, stage labels, the one thing to look at |
| `--accent-hover` | `#c45200` | `#ff8c3d` | |
| `--accent-06` / `-18` / `-45` | accent at 7 / 19 / 47 % | stronger in dark | Tints for a highlighted box, a score scale |
| `--bad` / `--bad-soft` | `#a3342a` / `#f4e3e0` | `#e88b80` / `#3a201d` | Unknown, unverified, missing: a `?` mark, *no source*, a gap with no evidence |
| `--fill-strong` | `#c45200` | `#f57722` | A solid accent fill. **White on the brand orange is only 3.6:1; on this, 5.2** |
| `--fill-bad` | `#a3342a` | `#e0655a` | A solid "bad" fill |
| `--on-fill` | `#ffffff` | `#161614` | Text on a solid fill. In dark, dark text on a bright fill is the legible one |
| `--shadow` | `0 2px 12px rgba(0,0,0,.07)` | `… .45` | Used once: the primary persona card. Elevation is otherwise by border |
| `--ease` / `--dur` | `cubic-bezier(.4,0,.2,1)` / `.18s` | | Every transition |
| `--phases-w` | `240px`, `64px` collapsed | | The phase rail's width |

**Colour has two meanings, and only two.** The accent means *this is where you are* or *this is the
point*. `--bad` means *we do not know* or *this is missing*. **Everything else is greyscale.** A score
scale is one hue, the accent, because it measures magnitude; only a value that means something
different gets a different colour.

---

## 3. Type

| Role | Face | Size and setting |
|---|---|---|
| Display: `h1`, `h2`, card titles | **Special Gothic Expanded One**, weight 400 only | `h1` `clamp(30px, 4.4vw, 54px)`, line-height 1.02, max 17ch, balanced. `h2` `clamp(24px, 2.9vw, 34px)` |
| Body and UI | **Inter** 400 / 500 / 600 / 700 | 16 px, line-height 1.6. Standfirst 17 px. Tables 13.5 px |
| `h3` | Inter 600 | 18 px |
| Small labels: `h4`, table heads, `dt`, rail labels | Inter 600, uppercase | 10.5–11 px, tracking .12–.14em, `--ink-3` |
| Code, file names, captions, ids, the phase meta line | System mono (`ui-monospace, SF Mono, Menlo, Consolas`) | 11.5–12 px |

- Both web faces load from Google Fonts in one `<link>`. Mono is never a web font.
- **Numbers in tables and fact strips are `tabular-nums`.**
- **Prose is measured at 74ch** (`.col > *`). A `.wide` element takes the full column.
- Uppercase is only for small labels, never for a sentence.

---

## 4. The anatomy of a phase page

Every phase page has the same shape, in this order. It is the course's reference shape.

1. **A skip link**, `Skip to the material`, to `#content`.
2. **The phase rail**, fixed to the window's left edge from 1080 px up, a horizontal strip below it.
   It lists **all twelve course phases**, always twelve. The current one is tinted with the accent,
   built ones are links, unbuilt ones are outlined and marked *soon*. It collapses to its numbers, and
   the state is kept in `localStorage` under `phases` by a one-line script placed before the `<nav>`,
   so it applies before paint. **Adding a phase page means updating the rail in every template and in
   every built page.**
3. **The masthead** (`.mast`): the label `Phase NN · Name` above the title, the `h1`, the meta line
   (`Phase N of 12 · … · re-verified <date> · source brief: CLAUDE.md`), a standfirst, and a fact
   strip (`.facts`) of 4–6 counts.
4. **The tab bar** (`.rail`, *In this phase*): sticky, one tab per section, each tab a small label
   above its name: `Start`, `Stage 01`…, `Close`. **Exactly one tab is active**: the last section
   whose top has crossed the upper third of the viewport. Drag-to-scroll with a 5 px click threshold,
   handlers on `window`, never `setPointerCapture`.
5. **Sections**, `Overview` first, then one per stage, then the close. Each opens with a
   `.stagehead`, which is the stage label in a small accent box plus the `h2`, and a `.qline`: the
   question the section answers, in one sentence.
6. **The overview always has two lists: *What we saw* and *What we decided*.**
7. **The evidence**: captures in a scrolling `.shots` well, a lightbox on click, a mono caption under
   each.
8. **A footer.**

**The words on the page** (fixed 2026-10-05). The top level is a **phase**: the strip and every
label say *Phase*. What a phase is made of is a **stage**. **The words *lesson* and *step* never
reach the page**, even when the source file uses them. `build_voice.py` rewrites them at render time
and asserts the result.

---

## 5. Components

**The grammar is border-led.** A box is `1px solid var(--rule)`, radius **10 px**, on `--surface`.
Lines inside it are `--rule-soft`. Small chips and marks are radius **3–4 px**. There are no shadows,
except the one on the primary persona card.

| Component | Class | Where |
|---|---|---|
| Fact strip | `.facts` | Masthead: a row of counts, each with a small label and a sub-line |
| Stage label | `.stagenum` | An accent outline box, uppercase, before every `h2` |
| Conclusion box | `.verdict` | The end of a stage. It has a 3 px accent left edge, the one place a thick edge is allowed |
| Table | `.tw > table` | `thead` on `--sunken`; `.band` rows group the body; `td.name` is bold and does not wrap |
| Score cells | `td.s1`–`s5`, `.score` | Accent tints by magnitude; `s1` and a `?` are `--bad` |
| Numbered list that opens | `.flows > details` | A number, a title with a sub-line, a status chip, and a chevron |
| Status chip | `.fstat`, `.st-closed` | Grey by default, accent when closed |
| Decisions | `.decisions > .dec` | Two columns: *what* on the left, *why* on the right |
| Gaps | `.gap`, `.gap.unverified` | 2 px top edge: accent, or `--bad` when unverified |
| *No source* | `.nd` | Inline `--bad` chip |
| Evidence mark | `.m-y` `✓` · `.m-s` `*` · `.m-q` `?` | The three marks from `01-research/research.md` |
| Persona card | `.pc`, `.pc.primary` | The primary card is the one with an accent border and a shadow |
| Main job, jobs | `.mainjob`, `.job`, `.job.hyp` | A hypothesis job is dashed, on `--sunken` |
| Pull quote | `blockquote`, `.pq` | 2–3 px accent left edge |
| Pan-and-zoom diagram | `.vp`, `.zoomer` (ia) | Mermaid, **stroke colours only, never fills**, light theme |
| Principle, element (voice) | `.principle`, `.pair`, `.element` | A rule with *yes / no* side by side |

**A new component** is added to the page template that needs it, written in these tokens. If a
second page needs it, it moves into the shared block.

---

## 6. Rules

- **Every page is self-contained.** Captures are embedded as data URIs (`build_page.py`), so a page
  opens from disk and can be sent as one file. The only external requests are Google Fonts and, on
  the IA page, Mermaid from jsDelivr.
- **Generated pages are never hand-edited.** Edit the template or the source `.md`, then rebuild.
- **A page is not published until it is listed in `.vercelignore`**, which is a whitelist. A moved
  page needs a redirect in `vercel.json`.
- **Accessibility.** The focus ring is 2 px accent with a 3 px offset. Motion is off under
  `prefers-reduced-motion`. Smooth scroll is on the root only. Text on a solid fill uses
  `--fill-strong` / `--on-fill`, never the raw accent.
- **Copy is English**, and it reports. It states what was examined and what was decided, with dates
  and counts, in the same register as `05-tone-of-voice/voice.md`.
- **Both themes are kept.** A change is checked in light and in dark.

### Known drift, kept visible

Five colours are hard-coded outside the tokens and should become tokens the next time those
templates are touched:
- `voice-page.tpl.html`: a green `#15803d` / `#16a34a` for the *yes* side of a principle.
- `ia-page.tpl.html`: green, amber `#8a6508` / `#b8860b` and red `#b91c1c` / `#dc2626` for flow
  endings, plus two Mermaid colours copied from the light theme.

They do not follow dark mode.

---

## 7. What this file is not

- **Not the product's design.** See the warning at the top. The product's language is decided in
  `06-concept/concept.md` and `tokens.css`.
- **Not a design system.** It records one small page language as it exists, so a new phase page
  looks like the others without reading 1,500 lines of template first.
