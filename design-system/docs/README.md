# Docs

**The living documentation**, built by `tools/build_docs.py` (lesson 09, steps 2–7). Online: https://ai-stack-builder-research.vercel.app/design-system/docs. Locally, open
[`components.html`](components.html).

- `components.html` is the showcase: every component with a live preview, grouped as the kit groups them. `index.html`
  only sends to it. Vercel serves the folder's address without its slash, and a page there would load unstyled (I6).
- One page per component (46), in five parts:
  - **anatomy**: the live component, its parts numbered and outlined on hover;
  - **variants and states**: every one the screens have, cut from them;
  - **states**: hover, active, focus-visible and disabled, in both themes;
  - **when to use**;
  - **rule and anti-rule**, with a link to the component to take instead.
- `tokens.html`: every token in `../tokens.css`, with its level, its dark and light value, swatches, and the files that
  read it.
- `layouts.html`: the five frames a screen is set in.
- `patterns.html`: the six patterns.
- `why.html`: why the system looks as it does, from `06-concept/concept.md` and `references.md`.

**Every specimen is the product's own markup on `../index.css`.** The pieces come from `build_kit.components()`.
`07-ui-assembly/ui/kit.html` showed the same pieces until it was retired to a redirect here (D2). The words the docs say
are `tools/docs_content.py`. A hand edit here is overwritten by the next build.
