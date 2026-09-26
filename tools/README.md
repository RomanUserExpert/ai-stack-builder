# tools — the course page generators

**Three generated pages, one design language, published as phases 01, 02 and 03 of the course.**
**The phase list is a left rail fixed to the window's edge, and it collapses to its numbers; the section anchors are a sticky horizontal tab bar.** *Since 2026-09-26 the rail is the same on every phase page and on the wireframes*: on `--sunken`, one tone below the page, each phase its own rounded bubble with no rules or bars — the current one tinted with the accent, the unbuilt ones outlined only; 240 px open, 64 px collapsed, the state kept in `localStorage` under `phases` and restored by a one-line script placed just before the `<nav>`, so it applies before paint. The toggle lives inside the scroll-spy IIFE **without an IIFE of its own** — `build_personas.py` and `build_ia.py` lift that script up to its first `})();`, and a nested one cut it in half the first time. Below 1080 px the rail is still the horizontal strip. *Phase* is
what the pages call the course's *lesson* — the label changed on 2026-09-09, the twelve entries did
not, and they are still the course's twelve and never this project's build phases (`CLAUDE.md` §1).
**In both, the small label sits *above* the title, not beside it** — the phase number in the
sidebar, the stage in the tab bar — and **both pages label their tabs with research stages**
(`START` · `STAGE 01`… · `CLOSE`), never with a bare ordinal, so the two read as one system. The
sidebar lists **all twelve course phases**, current one marked, the ten unbuilt ones *soon*. The tab
bar sticks to the top of the content column, and a scroll handler keeps **exactly one tab active** —
the last section whose top has reached the upper third of the viewport — and scrolls that tab into
view when the bar overflows. **Both horizontal bars are also dragged with the mouse** — press and
pull, `cursor:grab` appearing only while a bar actually overflows, and touch left to scroll natively.
A press is a click until it has travelled **5px**; past that it becomes a drag and eats the click it
would have ended in. **It must not use `setPointerCapture`** — a captured pointer retargets the click
at the scroller and the tab under the cursor never gets it, which is how the first version broke
every tab. The move and up handlers go on the `window` instead. It lives in the same IIFE as the
scroll-spy, because that is the block `build_personas.py` lifts across.

**The page scrolls to an anchor smoothly** — `html{scroll-behavior:smooth}`, under
`prefers-reduced-motion: no-preference`. It is set on the root only: `scroll-behavior` does not
inherit, so the two horizontal bars keep their 1:1 drag, and the spy asks for smoothness explicitly
when it glides the active tab into view. An `IntersectionObserver` band was tried first and left the indicator
blank between sections, which is wrong for something shaped like tabs. **That list is the course's and is fixed** — it is not the
project's build phases. **Adding a page means editing the strip in *every* template and in the generated pages beside them,
and adding the file to `.vercelignore`, which is a whitelist.** *Phase 04 became a link on 2026-09-26 — to `04-wireframes/pages/wireframes.html`, the wireframe viewer, which carries the same rail plus the wireframe tree; the wireframes are hand-written HTML, not generated.* *Phase 03 was added on 2026-09-20 and
that is five files, not two: two templates, the build artifact, and the two standalone pages, because
neither of the first two is rebuilt casually.*
[`../research/research.html`](../research/research.html) is phase 01, research stages 1–5;
[`../research/6-personas/personas.html`](../research/6-personas/personas.html) is stages 6 and 7 —
the persona cards, the job hierarchy and the jobs-against-personas matrix. **The second one pulls its
tokens, its shell and its scroll-spy out of the first at build time**, so the two cannot drift: edit
the shared `<style>` block in `research-page.tpl.html` and both pages move.

[`../research/research.html`](../research/research.html) is a **generated** file: one self-contained page with all 34
screen captures embedded as data URIs, so it opens from disk and can be sent to someone as a single
file with nothing to fetch. Do not hand-edit it — edit the template and rebuild.

```
python tools/build_page.py        # compress + embed the captures  -> tools/_research-page.build.html
python tools/make_standalone.py   # wrap in a full HTML document   -> research/research.html
python tools/build_personas.py    # personas + jobs, no captures   -> research/6-personas/personas.html
python tools/build_ia.py          # the IA, derived from its sources -> 03-information-architecture/ia.html
```

**Run all four after touching `research-page.tpl.html`**, because its `<style>` block is shared.

| File | What it is |
|---|---|
| `research-page.tpl.html` | The research page — content, **the CSS both pages share**, the small scroll-spy script. Captures are referenced as `{{IMG:key}}` placeholders. |
| `personas-page.tpl.html` | The personas-and-jobs page: a title and a body, and **no styles of its own**. Everything visual comes from the shared block. |
| `build_personas.py` | Lifts the shared `<style>` and the scroll-spy out of `research-page.tpl.html`, wraps this page's body in a standalone document, and asserts the tokens, the primary card, the matrix and every rail anchor survived. No images, so no embedding step. |
| `ia-page.tpl.html` | The information-architecture page: a title, **three components of its own** — the screen tree, a framed flow, and the traceability table with its orphan highlighting — and nothing else visual. |
| `build_ia.py` | **The only builder that reads the work rather than a template.** Each diagram is wrapped in a **pan-and-zoom window** whose height is capped at 78vh: drag to pan, `Ctrl`/`⌘` with the wheel to zoom, `Fit` for the whole shape, `1:1` for the column width. **The plain wheel is never taken** — a diagram that eats the page scroll is one you cannot get past — and the drag follows the same rule as the horizontal bars on these pages: a press is a click until it has travelled 5px, and the handlers go on the window rather than on a captured pointer. It lifts the shared style and spy like `build_personas.py`, and then **substitutes three things out of `sitemap.md` and `flows.md` at build time**: the screen tree verbatim, the **eight** Mermaid diagrams with their titles and their node and ending counts, and the traceability matrix as a table. **The orphan highlighting is computed, not annotated** — a column with no tick and a row with no tick are found by reading the tables — so the page cannot claim a coverage the work does not have. Mermaid comes from a CDN and is initialised on the **light** theme these pages use; the diagrams set stroke colours only and never fills, so the same source renders correctly on GitHub's light page and here. |
| `build_page.py` | Resolves each placeholder: reads the capture from `research/`, resizes to `MAXW`, re-encodes as JPEG at `QUALITY`, embeds it as a data URI. Fails loudly on a missing file, an unknown placeholder or an unsubstituted one. |
| `make_standalone.py` | Wraps the build output in `<!doctype html>` with a charset, a viewport and the small reset the artifact host would otherwise supply. **Without this step the page mojibakes** — every em dash, `×` and `⌘` in it depends on the charset declaration. |

**Two outputs, one template.** The build output is what gets published as an Artifact (the host adds
its own document wrapper); `research/research.html` is the standalone file. They are the same page.

**Adding or swapping a capture.** Add an entry to `IMAGES` in `build_page.py` — the key is yours to
choose, the value is a repo-relative path — then reference it as `{{IMG:your-key}}` in the template.
The build reports anything encoded but unused.

**Size.** ~3 MB at the current settings, against a 16 MB ceiling for a published artifact. There is
room to raise `QUALITY` or `MAXW` if a capture needs to be more legible.
