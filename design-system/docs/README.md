# Docs

**The living documentation**, built by `tools/build_docs.py` (lesson 09, step 2). Open [`index.html`](index.html).

- `index.html`: the showcase, every component with a live preview, grouped as the kit groups them.
- One page per component (46), in four parts: **anatomy** (the live component, its parts numbered and outlined on
  hover), **variants and states** (every one the kit shows, cut from the screens), **when to use**, **rule and
  anti-rule** (with a link to the component to take instead).
- `why.html`: why the system looks as it does, from `06-concept/concept.md` and `references.md`.

**Every specimen is the product's own markup on `../index.css`**, the same pieces `07-ui-assembly/ui/kit.html` shows.
The words the docs say are `tools/docs_content.py`. A hand edit here is overwritten by the next build.
