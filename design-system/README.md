# AI Stack Builder — design system

**The product's look as one package.** Every screen, the showcase and the shell link **one file**,
[`index.css`](index.css), and nothing else of ours. It imports the two things below, in this order.

| | What | Built by |
|---|---|---|
| [`index.css`](index.css) | **The one entry point**: `tokens.css`, then `components/index.css` | `tools/build_components.py` |
| [`tokens.css`](tokens.css) | The values on two levels: **primitive** (what a value is) and **semantic** (what a colour is for), dark in `:root`, light as `[data-theme="light"]` role overrides | `tools/concept_tokens.py` |
| [`components/`](components/) | One file per component (27), and `index.css` importing them in the kit's order | `tools/build_components.py` |
| [`docs/`](docs/components.html) | **The living documentation** — [online](https://ai-stack-builder-research.vercel.app/design-system/docs): [`components.html`](docs/components.html), the showcase (`index.html` sends to it); [`tokens.html`](docs/tokens.html), every token; [`layouts.html`](docs/layouts.html), the five frames; a page per component (46) — anatomy, variants and states, when to use, rule and anti-rule; [`why.html`](docs/why.html). All on this same `index.css` | `tools/build_docs.py`, the words in `tools/docs_content.py` |
| [`patterns/`](patterns/README.md) | **Six compositions found on three screens or more**, each cut from a real page, with no style of its own; shown on [`docs/patterns.html`](docs/patterns.html) | `tools/build_patterns.py` |
| [`examples/`](examples/README.md) | **A new screen built from the system alone**, labelled *an example, not in the product*: *Usage of My library*, for EJ-3. and *Copies of code-style*, for RJ-3. What they lacked is [`backlog.md`](backlog.md), eight entries | `tools/build_examples.py` |

**Every file here is generated.** A hand edit lasts until the next `python tools/build_mockups.py`, which rebuilds
the tokens, the components, this entry point and every screen, then runs the guards in `tools/kit_check.py`.

**Why it is at the root and not in a lesson's folder.** The repo is one folder per lesson, and this is the one named
exception (register Q48, D1): lessons 10–12 grow the system and the app will consume it, so no lesson number goes
into its import paths. The record of how it was made stays in the lessons:
[`08-design-tokens/`](../08-design-tokens/README.md) (the two levels) and
[`09-design-system/`](../09-design-system/README.md) (the system).

## Contributing

**New appears here first, and on a screen second, never the other way round.** A new value goes into `tokens.css` at
its level, with a value in both themes. A new component goes into `components/` with its docs page and its four states
in both themes. A composition about to stand on its third screen goes into `patterns/`. What cannot enter yet goes to
[`backlog.md`](backlog.md). The rule, with the generator and the guard for each case, is **`CLAUDE.md` §18**. The
same rule is in `DESIGN.md`, *Contributing to the system*. A guard that refuses a change names the section.

The rules on what a component may read and what a theme may override are `CLAUDE.md` §15–§17.
