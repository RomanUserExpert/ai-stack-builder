# tools — the research page generator

[`../research/research.html`](../research/research.html) is a **generated** file: one self-contained page with all 34
screen captures embedded as data URIs, so it opens from disk and can be sent to someone as a single
file with nothing to fetch. Do not hand-edit it — edit the template and rebuild.

```
python tools/build_page.py        # compress + embed the captures  -> tools/_research-page.build.html
python tools/make_standalone.py   # wrap in a full HTML document   -> research/research.html
```

| File | What it is |
|---|---|
| `research-page.tpl.html` | The page itself — content, CSS, the small scroll-spy script. Captures are referenced as `{{IMG:key}}` placeholders. |
| `build_page.py` | Resolves each placeholder: reads the capture from `research/`, resizes to `MAXW`, re-encodes as JPEG at `QUALITY`, embeds it as a data URI. Fails loudly on a missing file, an unknown placeholder or an unsubstituted one. |
| `make_standalone.py` | Wraps the build output in `<!doctype html>` with a charset, a viewport and the small reset the artifact host would otherwise supply. **Without this step the page mojibakes** — every em dash, `×` and `⌘` in it depends on the charset declaration. |

**Two outputs, one template.** The build output is what gets published as an Artifact (the host adds
its own document wrapper); `research/research.html` is the standalone file. They are the same page.

**Adding or swapping a capture.** Add an entry to `IMAGES` in `build_page.py` — the key is yours to
choose, the value is a repo-relative path — then reference it as `{{IMG:your-key}}` in the template.
The build reports anything encoded but unused.

**Size.** ~3 MB at the current settings, against a 16 MB ceiling for a published artifact. There is
room to raise `QUALITY` or `MAXW` if a capture needs to be more legible.
