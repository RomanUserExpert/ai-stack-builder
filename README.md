# AI Stack Builder

A workspace for your AI building blocks — skills, agents, system prompts, MCP servers,
scripts and mini-apps. Keep them in one library, assemble them into projects, export a
project as an archive that is ready to run.

**The point isn't storage — it's assembly with validation.** Git already stores files.
Nothing tells you that a skill needs a particular MCP server, that two items write to the
same config file, or that an env key is missing. You find that out at runtime. This does
the check before you export.

## Concepts

- **Item** — one reusable block: `skill`, `agent`, `prompt`, `mcp`, `script` or `app`.
- **Project** — a named set of items that exports as an archive.
- **Library** — everything you own, across all projects.

Items live in the library once. A project links to them, so editing an item updates every
project that uses it — unless you detach it and tune it locally for that project alone.

## What export produces

A zip, assembled rather than dumped: inline items placed at their target paths, external
repos written up as setup instructions, all MCP servers merged into one config, and every
missing env variable collected into `.env.example`. You pick the agent target first —
Claude Code, Cursor, Codex or Universal — and the paths and naming adapt.

The `SETUP.md` inside is written **for the agent that opens the project**, not for you to
read. It states what each item in the set requires — its dependencies, servers, env keys
and repos at their pinned versions — so the agent can set the project up on init.

## Who it's for

Design engineers and AI engineers who use AI daily and have accumulated more material
than they can keep straight. Desktop-first, dark theme.

## Status

**Research is done and the information architecture is nearly done. There is still no code.**
Stages 1–5 were signed off on 2026-09-02 and stages 6 and 7 — personas and jobs to be done — on
2026-09-09. *The blanket* provisional *label on those two was dropped on 2026-09-15 and no mark moved
with it*: the warning is carried per claim now, which is where it was always finer. **Lesson 03,
information architecture, ran from 15 to 20 September** and six of its seven steps are done — see
*Structure* below. No design system and no mockups yet, and **nothing so far decides how anything
looks.**

**One decision from 20 September changes the shape of everything after it: the product is online**, a
backend with accounts, so a person's library follows them between machines. **What the backend is
stays undecided on purpose** — this work designs the interface, and every rule in it is phrased as what
a person sees and what a surface may claim.

Roadmap — the twelve lessons of the course this work is homework for. *Corrected 2026-09-15;
this line used to read `research → design system → mockups → frontend → logic`, which put the
design system second when it is ninth.*

~~01 research and benchmark~~ → ~~02 personas and JTBD~~ → **03 information architecture** →
04 prototyping → 05 tone of voice → 06 concept → 07 UI assembly → 08 design tokens →
09 design system → 10 responsive → 11 animation → 12 handoff. Product logic — state,
storage, validation, export — comes after all twelve.

The library is not empty on first run: a curated, read-only **public library** ships with
the app beside your own, along with one example project that deliberately contains a real
problem to find.

A project or a single item can also be **shared by link** — an unlisted address, live rather than a
snapshot, openable by anyone holding it and revocable. **The receiver never signs in**, and they can
run the same check the owner has on the set in front of them. There is no catalog: a link is a
handover, and a catalog is a marketplace.

Planned stack: Next.js + React + TypeScript, with a backend. **Which backend is deliberately not
decided** — the product decides what it is and the implementation follows. JSZip for the archive, as a
choice rather than a constraint. Custom design system, no UI kits. *This line said `client-side only,
IndexedDB` until 2026-09-20.*

## Structure

**The information architecture lives in two documents, and they are ordered: one is derived from the
other.**

**[`03-information-architecture/sitemap.md`](03-information-architecture/sitemap.md) — the map, in six
sections.** **Entities**: sixteen objects a person handles in order to close a job, each with its
fields, the job that raises it and how well that job is known, plus **eleven candidates refused with a
stated reason**. **Screens**: a tree of **seven screens and one orphan**, grouped by the person's own
situations rather than by sections of a site, every node carrying the job it serves. **Places, modes,
overlays and states**: what each node *is*, on one test — *could somebody be sent there and arrive* —
which yields **six places and nothing else navigable**. **Navigation**: two global entries, the split
into global, contextual and deep, and **three taps from the first screen to an archive** for somebody
already signed in. **Traceability**: every job against every surface, with **two orphan columns and two
orphan rows**, each carrying a decision. And dated blocks recording where the decisions met each other,
because several of them arrived on the same afternoon and changed one another.

**[`03-information-architecture/flows.md`](03-information-architecture/flows.md) — seven paths in eight
Mermaid diagrams**, written out of the sitemap and nothing else. The main job, four related ones, the
single-item export and **the receiver's path**. Every node is a screen, mode, overlay, region or state
the map already had: **no new place appeared in any of them**, which is the closest thing to a test an
architecture like this can be given. Each diagram is followed by its decisions and states in words, and
by **what can go slowly and what can fail on that path** — named rather than drawn, because the product
is online and drawing it would have doubled every graph to say one thing eight times.

**Read them on GitHub or on the page**, not in a terminal preview: the diagrams need a renderer.

**[`03-information-architecture/ia-critique.md`](03-information-architecture/ia-critique.md)** is the
audit of both — sixteen defects in four classes plus one larger finding outside them, **written and
approved before anything was changed**, with what was done to each recorded underneath and the original
list left untouched.

**[`03-information-architecture/ia.html`](03-information-architecture/ia.html)** is all of it as one
page. **It is derived at build time from the two documents above**, so it cannot drift from them, and
the orphan highlighting in its matrix is computed rather than annotated.

## Files

- `CLAUDE.md` — full working context: data model, product logic, scope boundaries,
  conventions. The source of truth. Start here.
- `research/` — the research phase, one folder per stage. Stages 1–5 are closed; stages 6
  and 7 were added on 2026-09-06 and are *provisional*.
  - `research/research.md` — the consolidated read, in five sections: competitors,
    flows, benchmark, patterns, conclusions. Every fact links to its source or capture,
    and what was never established says so. A digest, not a spec.
  - `research/research.html` — the same research as one self-contained page, with 34
    captures embedded. Opens from disk, sends as a single file. Generated — see `tools/`.
  - `research/FINAL.md` — the closing document: what the phase produced, what it
    decided, and why. **Start here for the research** — it is the entry point the whole
    folder instructs.
  - `research/research-plan.md` — the spine, ending in the register: every open question
    with an ID, what would answer it, and what it blocks. The only list of open questions.
  - `research/6-personas/personas.md` and `research/7-jobs-to-be-done/jtbd.md` — three
    personas with one primary, and one main job with four related, three emotional and two
    social, each against a matrix of personas. Both *provisional*.
  - `research/6-personas/personas.html` — the same two documents as one generated page.
  - `research/personas-and-jobs-critique.md` — the audit of those two: 238 claims
    classified, 27 found invented, applied in full.
- `03-information-architecture/` — lesson 03, described under *Structure* above: `sitemap.md`,
  `flows.md`, `ia-critique.md`, the plan in `README.md`, and the generated `ia.html`.
- `tools/` — the generators for all three pages, and how to rebuild them.
