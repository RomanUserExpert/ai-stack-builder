# Lesson 05 — Tone of voice and microcopy

**Closed 2026-10-05 — every step done; the result is [`voice.md`](voice.md) and [`microcopy.md`](microcopy.md), and the lesson's page is [`voice.html`](voice.html), built by `tools/build_voice.py`.** *What follows is the plan as written on 2026-10-01.*

**A plan, not a result.** Written 2026-10-01, the day the lesson's materials were read, and **numbered
by the course's own seven steps from the start** — lesson 03 opened with ten steps of its own and had to
renumber mid-flight once its prompt pack was read. Not this time.

**What the lesson does.** The screens of lesson 04 already say real words, but those words were written
together with the structure, and in places they name the same thing differently. This lesson gives the
product **one voice**: a contract, `voice.md`, that any line of the product can be written against, and
a table, `microcopy.md`, holding every line of the product — **and then the text of every screen is
rewritten in one pass.** *A voice document that rewrote no screen is decoration* — the course's own
words, and the trap this plan is built to avoid.

**The thesis is the course's, and this file already lives by it: a voice is rules, not a mood.** Every
principle carries **a rule** in one sentence, **an example** line written by it, **an anti-example**
that breaks it, and **an explanation** — the line of our research it comes from. *A principle with no
line under it is invented*, the same way a persona with no data was in lesson 02. Better three honest
principles than five handsome ones.

---

## What is already decided, and must not be re-decided here

**`CLAUDE.md` fixed a register long before this lesson existed**, and the voice is derived from it, not
chosen beside it. Step 2 starts from these and cites them:

- **Checked, never works.** No *works*, *valid*, *passing* or a bare tick — §6. The strongest rule the
  product has, and a vocabulary rule as much as a logic one.
- **Findings in the present tense, naming the consequence** — GitHub's mergebox register: *Two items
  write to `.mcp.json`. The archive will contain only one of them — `db-tools`.* — §6.
- **Three severities by name** — *Problem, Note, Skipped* — and **nothing blocks**: a cost is named
  before the irreversible step, never enforced — §6, §11.
- **The keys reminder says it is a reminder.** *We do not read your files looking for secrets* — never a
  sentence implying a scan came back clean — §11.
- **A disclosure that could not be produced says so**, and **a verdict the product is not sure of is
  not shown** — Q26, Q28.
- **Usage facts, never a score** — *used in 3 projects* — and their stated ceiling: they answer *is it
  used*, never *is it any good* — §5, Q22.
- **The vocabulary of §4** — *Item, Project, Library, Workspace, Stack*; **never *Bundle***; the six
  kinds as written. Step 3's dictionary **extends** §4 and does not compete with it.
- **UI copy is in English** — §13. The course's *ти / ви* question becomes ours as *how the product
  addresses the person in English* — imperative, *you*, or neither — and is decided in step 3.

**And the evidence is already partly gathered.** The course's step 2 asks for the competitors' language
and says to fetch it if the research has none. **Ours has some**:
[`2-flows/11-copy-and-error-language/`](../01-research/2-flows/11-copy-and-error-language/) holds real
conflict and CI-failure copy from Terraform, npm and GitHub, written up as *why it works* and *what we
can beat*; the benchmark's notes carry Vercel, VS Code and Figma's consequence copy. **What is missing
is the quiet half** — empty states, buttons, confirmations, sign-in — and that is fetched in step 2,
not assumed.

---

## Our mapping of the course's paths

| The course says | Here it is |
|---|---|
| `wireframes/*.html` | [`04-wireframes/pages/*.html`](../04-wireframes/pages/wireframes.html) — **80 product pages** plus the viewer and the stylesheet |
| `wireframes/_screens.md` | [`04-wireframes/_screens.md`](../04-wireframes/_screens.md) |
| `research.md`, `competitors.md` | [`01-research/research.md`](../01-research/research.md), [`01-research/1-landscape/competitors.md`](../01-research/1-landscape/competitors.md) |
| `personas.md`, `jtbd.md` | [`02-personas-jtbd/6-personas/personas.md`](../02-personas-jtbd/6-personas/personas.md), [`02-personas-jtbd/7-jobs-to-be-done/jtbd.md`](../02-personas-jtbd/7-jobs-to-be-done/jtbd.md) |
| `voice.md`, `microcopy.md` | **this folder** |
| the main screen, `listings.html` | **to be chosen** — see step 5 |

**The prototypes are not a second copy to rewrite by hand.** The 239 pages in
[`04-wireframes/prototypes/`](../04-wireframes/prototypes/prototypes.md) are **generated from `pages/`**
by [`tools/prototypes/`](../tools/README.md), which was checked on 2026-10-01 to reproduce them
exactly. So the pages are rewritten, and the prototypes are **rebuilt**. *The cost to know about now:
the generators find their wiring points by matching text on the page, and they assert that text exists
— a rewritten button label is a broken assertion. Expect to update the generators in step 6, and treat
every failed assertion as a line `microcopy.md` must account for.*

**User content is the product's subject, and it is not rewritten.** Item names and descriptions,
project names, file paths, env key **names**, repo URLs, `ref`s, licence ids, the content of an item,
and the `SETUP.md` an item ships with. **The product's own sentences that carry those values are
product copy with slots** — *`db-migrate` is used in 3 projects* — and they are rewritten; the value in
the slot is not.

---

## Steps — the course's seven

| # | Step | Output | State |
|---|---|---|---|
| **1** | **Inventory** — every line of `pages/*.html` in one table: screen, zone, line, type. Mark, do not rewrite: one thing under two names, one action under two labels, AI clichés and cheer, placeholders left over. **User content marked separately.** | `microcopy.md` as an inventory | **done 2026-10-05** — 1,462 rows, 23 divergences, no cheer found |
| **2** | **Principles** — 3–5, each with rule, example, anti-example, explanation from a line of `research.md`, `competitors.md`, `personas.md` or `jtbd.md`. Part of them from **the competitors' language**: where everybody writes the same way, the difference is the voice. Fetch the quiet half first. | `voice.md` · *Principles*; `research.md` · *Competitors' language* if fetched | **done 2026-10-05** — five principles; `research.md` §10, sixteen quotes |
| **3** | **Dictionary and forbidden** — no new search: one word per concept for every divergence step 1 marked, each with why; the form of address; which loanwords and jargon are allowed. Forbidden: clichés, motivational tone, exclamations, emoji in system messages, *successfully* — each with *was / should be*. | `voice.md` · *Dictionary*, *Forbidden* | **done 2026-10-05** — every D/V/T mark closed; `Check` / `Export` answered as naming, the owner confirms in step 5 |
| **4** | **Microcopy rules** by element: button, screen title, field (label / hint / validation), empty, error, loading, success, **dangerous action** — one example each, from our product. | `voice.md` complete | **done 2026-10-05** — eight elements, one example each, each checked against the principles and the dictionary |
| **5** | **The sample** — the main screen with all its state pages rewritten; `microcopy.md` gains *was / now*. **Reviewed by the owner on the screen, read aloud, before anything else is touched.** | rewritten pages, *was / now* | **`Run` rewritten 2026-10-05** — 21 lines on 8 pages, markup identical; **approved by the owner 2026-10-05**, with Q36 (`Export…` as the main control) |
| **6** | **Roll out** — subagents, one per screen with its states, contract `voice.md`, reference the sample; their rows merged into `microcopy.md`; the same action checked to carry the same label everywhere. **Prototypes rebuilt.** | every page rewritten, `microcopy.md` final | **done 2026-10-05** — 16 screens by 16 agents, 264 of 1,462 rows changed, markup identical; prototypes rebuilt (37 cases, 239 pages, no old phrase survives); open points await the owner |
| **7** | **Check and close** — a defects table first (term not in the dictionary · one action, two labels · forbidden slipped in · tone not by state · a line on a screen and not in the table, or the reverse), reviewed by the owner, then fixed in the pages and the table together. `CLAUDE.md` gains a *Voice* section, `README.md` a *Voice* section; pushed. | defects table, fixes, docs | **done 2026-10-05** — 22 defects, all fixed by the owner's *исправляй*; Q37; `CLAUDE.md` §14 and `README.md` *Voice*. **Lesson 05 closed** |

**The course's own checks, kept as this lesson's bar**: `microcopy.md` covers **every screen and every
state page**; no principle is an adjective; one concept, one word; the forbidden list has *was / should
be* for each entry; the four states follow their rules; **structure and markup unchanged — only text**;
user content untouched; `microcopy.md` matches the screens line for line.

---

## What lesson 04 handed this lesson

Each lands in a named step, so none of them is discovered late.

1. **`Run` or `Export` — the deferred naming question** (Q16, `CLAUDE.md` §6). *The main action should
   be Export, and checks and runs are sub-processes.* A dictionary question → **step 3**. **If it turns
   out to be more than naming — if `Export` becomes a control on the Project screen — it is not decided
   here: it goes to the register, because it reopens §8.**
2. **The add/edit overlay** — the product's busiest disclosure surface: the keys reminder, the blast
   radius, `defersTo`, and since Q14 a third door from the library panel. *Composing it is lesson 05's
   first job on this surface* (§8) → **steps 4 and 6**, and a candidate for the sample.
3. **The longest project row** — `item · rule · observed value`, now sharing its width with the panel.
   *Write the longest real row and see whether it survives* (§8). Wireframe text was written at real
   length for exactly this → **step 5 or 6**, measured on the page, not argued.
4. **The dead shared link** — a receiver with no account, no context and no other surface, meeting the
   product at a 404, and since Q35 **with no action at all**. *A node, and a sentence for it in lesson
   05* (`ia-critique.md` 2.3). The single sentence with the least to lean on → **step 6, written first**.
5. **Counts as a verdict** — `0 problems · 0 notes` reads the same on an empty set and a perfect one
   (Q16, left open). Partly a copy question → **step 4**, and to the register if copy cannot carry it.
6. **Content invented in the prototypes and never confirmed** — `query-explainer`, `stripe-rules`,
   `webapp-testing` requires `playwright-mcp`, the Cursor archive layout. **That is user content and
   this lesson does not rewrite it** — but step 1 marks it, so it is not mistaken for decided.
7. **Two small debts from `PROGRESS-04`**: the env stage of `pages/run-*.html` says *2 keys named*
   while `.env.example` holds three; and §5 still describes one file where Q31–Q32 made an item a
   folder of any mix. The first is fixed in **step 1** as an inventory finding; the second is the
   owner's and goes to the register if the dictionary needs it.

---

## Decisions owed to the owner

- **Which screen is the sample** (step 5). The course takes the main list. **Ours has two candidates:**
  `Project`, the main screen of the main flow, or `Run`, which carries Problems, Notes, the handover and
  Export — the wow moment and nearly every register `CLAUDE.md` has fixed. *Recommended: `Run`* — it is
  where a wrong word costs most, and a sample that clears it sets the bar highest.
- **Form of address in English** (step 3).
- **`Run` / `Export`** (step 3), within the limit above.

## What it is not

- **Not visual.** No colour, type, size or components — lessons 06–09. Width is measured only to answer
  whether the longest row survives.
- **Not structure.** No element added, moved or removed, except where a sentence the product owes has
  nowhere to stand — and then it is a register entry first.
- **Not new product logic.** If writing a sentence reveals the product cannot honestly say it, that is
  a finding for the register, not a rewording.

Day-by-day notes: `PROGRESS-05.local.md` in this folder, gitignored (`CLAUDE.md` §13).
