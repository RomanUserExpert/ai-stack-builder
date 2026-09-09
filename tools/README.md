# tools — the research page generators

**Two generated pages, one design language, published as phases 01 and 02 of the course.**
**The phase list is a left sidebar; the section anchors are a sticky horizontal tab bar.** *Phase* is
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
scroll-spy, because that is the block `build_personas.py` lifts across. An `IntersectionObserver` band was tried first and left the indicator
blank between sections, which is wrong for something shaped like tabs. **That list is the course's and is fixed** — it is not the
project's build phases. **Adding a third page means editing the strip in both templates and adding
the file to `.vercelignore`, which is a whitelist.**
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
```

**Run all three after touching `research-page.tpl.html`**, because its `<style>` block is shared.

| File | What it is |
|---|---|
| `research-page.tpl.html` | The research page — content, **the CSS both pages share**, the small scroll-spy script. Captures are referenced as `{{IMG:key}}` placeholders. |
| `personas-page.tpl.html` | The personas-and-jobs page: a title and a body, and **no styles of its own**. Everything visual comes from the shared block. |
| `build_personas.py` | Lifts the shared `<style>` and the scroll-spy out of `research-page.tpl.html`, wraps this page's body in a standalone document, and asserts the tokens, the primary card, the matrix and every rail anchor survived. No images, so no embedding step. |
| `build_page.py` | Resolves each placeholder: reads the capture from `research/`, resizes to `MAXW`, re-encodes as JPEG at `QUALITY`, embeds it as a data URI. Fails loudly on a missing file, an unknown placeholder or an unsubstituted one. |
| `make_standalone.py` | Wraps the build output in `<!doctype html>` with a charset, a viewport and the small reset the artifact host would otherwise supply. **Without this step the page mojibakes** — every em dash, `×` and `⌘` in it depends on the charset declaration. |

**Two outputs, one template.** The build output is what gets published as an Artifact (the host adds
its own document wrapper); `research/research.html` is the standalone file. They are the same page.

**Adding or swapping a capture.** Add an entry to `IMAGES` in `build_page.py` — the key is yours to
choose, the value is a repo-relative path — then reference it as `{{IMG:your-key}}` in the template.
The build reports anything encoded but unused.

**Size.** ~3 MB at the current settings, against a 16 MB ceiling for a published artifact. There is
room to raise `QUALITY` or `MAXW` if a capture needs to be more legible.
