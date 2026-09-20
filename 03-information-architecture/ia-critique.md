# IA critique — lesson 03, step 6

> **Written 2026-09-20, against [`sitemap.md`](sitemap.md) and [`flows.md`](flows.md) as they stand at
> `7f03956`.** Four defect classes, in the order the lesson sets: **dead ends and missing states first,
> because they are the dangerous ones.**
>
> **Nothing was fixed when this was written.** The list came first and the fixes were proposed
> separately at the end, in an order, unapplied — **and then the owner read the list and approved them,
> and what was done to each is recorded in *Applied* below.** *The list itself is left exactly as it was
> written, defects and all, because a critique edited after the fact is not a critique.* **That is the method's own rule and it is worth keeping**: three times this week
> a correction turned out to be wrong a day later, and each time the record survived because the
> reasoning was on the page before the edit.
>
> **The traceability matrix is read, not rebuilt** — class 4 checks against it.
>
> **One thing this critique is not allowed to do**: treat a limit the product drew honestly as a defect.
> Two of the endings in `flows.md` are outside the product by construction — env values on a machine we
> never touch, and copies a revoked link cannot recall. **Those are the shape of *checked, never works*,
> and calling them dead ends would be scoring the product down for telling the truth.**

---

## Class 1 · Dead ends

**Ten endings across seven diagrams; four of them do not survive.** The test applied: *is there an
action the product actually offers that the diagram does not draw?* If yes, the dead end is drawn and
not real, and the diagram is lying about the product. If no, it is real and stays.

| # | Where | What | How to fix |
|---|---|---|---|
| **1.1** | `flows.md` RJ-2b, `Stuck: the fix is elsewhere` | **It contradicts §6 and it contradicts the main flow in the same file.** A Problem that cannot be fixed from its row is not the end of anything: **export is never disabled**, and the person confirms an unclean export and leaves with the archive. **The main job draws exactly that route** — *fixable from this row? → no → unclean export confirmed → handover* — and RJ-2b, which is the flow specifically about Problems, draws a wall instead. **The most-specified escape hatch in the specification is missing from the one diagram that most needs it.** | Replace the ending with the route the main flow already has: *unclean export confirmed* → `Run: handover`. **The dead end disappears entirely** — nobody is ever stuck on a Problem, which is the whole point of *nothing blocks*. |
| **1.2** | `flows.md` RJ-4, `Stuck: nothing will catch it` | **The same flow contradicts itself two branches apart.** When the answer to *is that content yours to publish?* is no, the flow loops back through `Item: edit form` and lets the person fix it. When the answer to *did you take the keys out?* is no, it ends. **Both are the same act — go back to the file and take the thing out** — and only one of them is drawn. | Loop the *no* branch back to `Item: add form`, the way the tangled-content branch loops. **The ending is not deleted**: a person who declines to fix it still reaches *nothing will catch it*, which is the honest part. What changes is that declining becomes a choice rather than the only edge out of the node. |
| **1.3** | `flows.md` single-item export, `Stuck: cannot find it` | **RJ-3 asks a second question at this exact node and this flow does not.** In RJ-3, *can you find the item?* → no → *is it on the shelf?* → the `Public library`, a copy into `My library`, and back into the flow. In the single-item export the same question ends the path. **Two diagrams, one product, two different answers to one situation.** | Add the shelf branch, as RJ-3 has it. Roughly four nodes. **Or** state in the prose why a person exporting one item is not offered the shelf when a person fixing one is — **but there is no such reason, so the first is the honest fix.** |
| **1.4** | `flows.md` RJ-1, `Stuck: no run to re-read` | **The exit exists, is free, and is not drawn.** The person looks for last week's handover, finds no page, and the diagram stops. **§6's answer to precisely this is *re-reading it means checking again, which is cheap by construction* — an accepted cost with a named remedy.** The diagram draws the cost and omits the remedy. | Route it back into `Checking`, labelled as what it is. **The ending should survive in a weaker form** — *they looked for a link that does not exist* is a real moment and §6 predicts it — but as a detour, not a terminus. |
| **1.5** | `flows.md` RJ-1, `Stuck: exported unread` | **Mislabelled, not misdrawn.** The person pressed Export without reading the handover. **They are not stuck — they hold a correct archive.** What they lack is knowledge of what the other side still needs, which is a bad outcome and not an obstruction. Drawing it red beside *cannot find it* and *nothing will catch it* flattens a distinction the product spends §6 building: **a thing that went wrong, versus a thing you were not told.** | Either a third ending shape for *finished, but blind*, or keep two shapes and move this one to `Done:` with the cost in its label. **The second is cheaper and the file already has the vocabulary for it** — `Done: the other side is known` has an obvious opposite. |
| **1.6** | `flows.md` RJ-2a, `Stuck: auto-added row holds` | **Real, and it stays — but it is the only dead end in the product created by a refusal of ours**, and it should be re-tested every time *nothing blocks* is restated. The branch before it asks *remove its puller instead?*, so reaching the ending means declining an offer the product does make. **The finding is not that it is wrong; it is that it is load-bearing and unique, and nothing marks it as such.** | No change to the diagram. **Add one line to the prose** naming it as the single refusal-generated dead end, so a future pass does not quietly widen the pattern. |

---

## Class 2 · Missing states

**This is the worst class in the file, and it got worse today rather than being discovered today.**
Q24 put the product online. **Every read and every write now crosses a network**, and the diagrams were
drawn for a product where none of them did.

| # | Where | What | How to fix |
|---|---|---|---|
| **2.1** | All seven diagrams | **There is no `loading` node anywhere.** Not one, in 27 + 20 + 22 + 12 + 16 + 21 + 26 nodes. The course names loading as one of three states a flow must show, and until this evening the file had an excuse — *the product is local*. **It has none now.** Opening the Library, saving an item, entering a project, opening a shared link: every one of them is a wait, and the product's own vocabulary has a word for a wait it takes seriously (`Checking`, drawn as a designed moment) and no word for the ordinary kind. | **Do not sprinkle `loading` into seven diagrams.** Decide once what the product's waiting looks like — §2 already says the validation pass is *a designed moment, not a spinner*, which begs the question of what everything else is — then draw it where a wait is long enough to be a state and not everywhere a request happens. **This is a composition decision that belongs to lesson 04**, and the flows should carry it only where a person makes a decision during the wait. |
| **2.2** | All seven diagrams | **There is no `error` node anywhere**, and after Q24 at least five distinct failures exist: **a revoked or expired link opened by a receiver**, a save that does not land, an archive that fails to build, **a session that expired mid-assembly**, and a shared page whose project has since been deleted. **None is drawn.** | Draw the ones where the person has a decision to make, not the ones where they only have a message to read. **By that test the first is mandatory and the rest are probably one shared pattern.** |
| **2.3** | `flows.md`, the receiver's side | **The most exposed error case in the whole product has no node: a receiver opening a dead link.** §5 says revoking *does not reach anything anybody already copied* and that the product must say so **at the moment of revoking** — which is the sender's side, and it is drawn. **The receiving side of the same event is drawn nowhere.** This is a person with **no account, no context and no other surface**, meeting the product for the first time at a 404. | A node, and a sentence for it in lesson 05. **It is the single highest-value missing state in the file**, because it is the only one where the person has nothing else to fall back on. |
| **2.4** | `flows.md` main job | **First-run `My library` empty is no longer drawn in any flow, and I removed it.** The 2026-09-20 revision replaced the excursion — palette → `Library` → *is it empty?* → `Public library` — with a scope switch inside the panel. **The detour deserved to die and the state went with it.** §11 guarantees that room is empty on first run; **seven diagrams now contain no node saying so.** | Add the state on the panel, where it now lives: *panel, `My library` scope, empty on first run* — one node in the main flow, on the branch that already exists for a panel offering nothing. **This is a regression introduced by a fix, and it is the reason this critique had to be run after the revision rather than before it.** |
| **2.5** | `flows.md`, `Projects` | **`Projects` with nothing in it is undrawn.** The main flow has *only the example*, which is the first run. **§11 makes the example deletable**, so *no projects at all* is reachable and nobody has drawn it. It is the emptiest surface the owner can produce and it is the one screen that cannot fall back on a shelf. | One state node on `Projects`. **And a question for lesson 04 rather than for the diagram**: the empty `Project` got one action and an inert control; an empty `Projects` has not been given the same treatment. |
| **2.6** | `flows.md`, the shared page | **The shared page's two stated facts are not drawn as states.** §6 requires it to say **when the owner last checked** and **whether the set has changed since** — the second being a *stale* state on somebody else's screen. **Neither appears in any diagram**, because the receiver's path is not drawn at all (see the block after class 4). | Falls out of drawing the receiver's flow. **Do not patch it into the sender's diagrams** — it is not the sender's state. |

---

## Class 3 · Excess depth

**The count is in `sitemap.md` §Navigation and it is honest. What the critique tests is whether
*explaining the compromise* is doing real work or standing in for a fix.**

| # | Where | What | How to fix |
|---|---|---|---|
| **3.1** | `sitemap.md` §Navigation, path **B** | **Four taps, and one of them is purchasable.** `Projects → New project ① → Configure ② → Run ③ → Export ④`. **A brand-new project is empty by definition, and §8 gives its empty state exactly one action — enter configuring.** A screen whose only action is *go here next* is a screen that could have gone there. **Auto-entering configuring on a project created a second ago would put B back at three.** | **A trade, not a bug, and it must be stated as one.** Buying the tap back means **the empty state is never seen on the path that creates it** — which was the owner's decision on 2026-09-20 and is the one surface where a new person learns what a project is for. **Recommendation: keep four, and write the trade into §Navigation**, because right now the row says *four* and does not say *and here is what three would cost*. |
| **3.2** | `sitemap.md` §Navigation, path **C** | **Four taps, already argued, and the argument got better today.** The panel made starting in the Library **optional** rather than merely paid for — the same errand now runs as path B. | No change. **One wording fix**: the row still reads as the persona's most frequent arrival, which is now the arrival they no longer need to make. |
| **3.3** | `sitemap.md` §Navigation, global entries | **Two, where the course asks for three to five.** The reason is written — the third cluster's screen is a mode, so an entry would point at something nobody can be sent to. **The reasoning is sound and the deviation is undeclared as a deviation**: a reader comparing against the method sees two and no note saying *we know*. | One sentence naming it as a deliberate deviation with its reason, in §Navigation. |
| **3.4** | Everywhere | **Q24 added a surface that has no depth count at all: sign-in.** If a session can expire, **the depth to the main job from a cold start is not three, it is three plus whatever authentication costs**, and no path in the table begins there. | Not fixable in the table until the sign-in surface exists. **Record it as a known incompleteness in §Navigation**, so the *three taps* claim is not read as covering a cold, logged-out start. |

---

## Class 4 · Orphans

**Checked against the existing matrix in `sitemap.md` §Traceability. No new matrix.**

| # | Where | What | How to fix |
|---|---|---|---|
| **4.1** | `sitemap.md` §Traceability, and `CLAUDE.md` §9, §10 | **Q24 created a class of surface the matrix has never seen, and nobody has counted it.** Accounts and sync entered the MVP this evening. **Sign-in, session, account settings, sign-out** — **no job in the matrix raises any of them**, and none exists in the screen tree. **They are orphans by the same test that condemned the JSON export, and they arrived after the test was run.** | **Do not add screens to the tree by reflex.** Name the minimum the decision forces — a way in, and what happens when a session ends — and take it to the register as an entry. **The matrix must be re-run over whatever is added**, or the coverage claim in §Traceability quietly stops being true. |
| **4.2** | `sitemap.md` §Traceability, JSON column | **An empty column that ships, on a declared preference.** That is legitimate and it is on the page. **What the critique flags is the count**: there are now **two** mechanisms in this product with no evidenced job and a stated non-evidential basis — the `license` field and this. **Two is a pair. Three is a habit**, and the habit is how a specification stops being evidence-led without anybody deciding that it should. | No change. **A line in §Traceability keeping the count visible**, so the third one is noticed when it arrives. |
| **4.3** | `sitemap.md` §Traceability, `L-pub` | **The shelf still stands mostly on a hypothesis**, and Q19 already narrowed what gets designed. **The critique adds one thing**: Q24 removed the *needs no server* half of its justification the same day, so the column is thinner by one argument than it was when the matrix was drawn. | No new action. **The matrix's own note should say the basis changed**, or a reader will reconcile two documents written hours apart and find them disagreeing. |
| **4.4** | `sitemap.md` §Traceability, rows `SJ-2` and `H-J5` | **Both still empty, both disposed of** — declined and refused respectively. **No defect.** Re-checked against Q24: **a backend does not give us the user's agent runtime**, so `H-J5` stays impossible and Q12 stays closed. | None. |

---

## Outside the four classes, and it is the largest finding in this document

**The receiver's path is not drawn.**

`Shared project` carries **seven jobs** in the traceability matrix — more than `Projects`, more than the
library panel — and `Shared item` nearly as many. **Together the two surfaces do about a third of the
product's job-closing work.** They appear in `flows.md` only as **nodes inside the sender's diagrams**.

**There is no diagram that starts at *somebody sent me a link*.** §6 specifies that path in prose, and
in some detail — *open the link · read the set · check it · read what the receiving machine still needs
· take the archive* — and calls it **Library-to-archive performed by somebody who owns nothing.** It is
written, and it has never been walked.

**Why this is not a nitpick.** Every defect in class 2 above lands hardest on this person: they have no
account, no context, no second surface, and **the only failure state in the product that leaves them
with literally nothing is the dead link, which is undrawn.** And Q20 — decided today — says these
surfaces get the most conservative treatment anywhere in the product **because their persona has never
spoken in the first person.** *A surface we have committed to being most careful with is the one surface
we have never walked.*

**Fix: one more diagram**, `RJ-5` in position or unnumbered — the receiver, end to end, with the dead
link in it. **It is the only proposal in this critique that adds work rather than correcting it**, and
it is the one I would do first.

---

## Applied — 2026-09-20, after the owner read the list

**Everything below was proposed first and approved before anything was touched**, which is the method's
rule and the reason this section exists underneath the list rather than instead of it.

| Item | What was done |
|---|---|
| **The receiver's flow** | **Drawn** — an eighth diagram, with the dead link as its first node. 20 nodes, 836 units, **scale 1.0**, the cleanest in the file |
| **1.1** RJ-2b's dead end | **Replaced** by the unclean-export route the main flow already had. RJ-2b now has **no `Stuck:` at all**, which is what *nothing blocks* looks like when it is drawn |
| **1.2** RJ-4's keys branch | **Loops back** to the add form; declining still reaches the ending |
| **1.3** single-item, *cannot find it* | **Gained the shelf branch**, as RJ-3 has it |
| **1.4** RJ-1, *no run to re-read* | **Routed back into `Checking`** — a detour, not a terminus |
| **1.5** RJ-1, *exported unread* | **Re-shaped**, and it produced a change to the file's own vocabulary — see below |
| **1.6** RJ-2a's refusal | **Marked as unique** in the prose |
| **2.4** first-run empty `My library` | **Restored**, on the panel where it now lives |
| **2.5** empty `Projects` | **Added** |
| **3.1–3.4** depth | **Four wording fixes**: the path-B trade, path C's stale description, the two-entry deviation named as one, and the cold-start gap recorded |
| **4.1** sign-in | **Taken to the register as Q25 and answered the same day.** The minimum only — a way in and a session-end rule; **no profile, no settings, no session list**, because no job raises them. **It cost a place: six, not five**, and the tests decided that, not a preference |
| **3.4** cold-start depth | **Answered with it.** Every path costs one more from a signed-out start; the floor of three is a floor for somebody already signed in, and §Navigation says so |
| **4.2, 4.3** | The *pair, not a habit* count and the shelf's changed basis, both written into §Traceability |
| **2.1** `loading` | **No nodes, deliberately — but no longer undescribed.** Every flow now carries a short **Waits and failures** list in words, so the waits are named where they happen while the composition decision stays with lesson 04 |
| **2.2** `error` | **One drawn, the rest named.** The dead link is a node in the receiver's flow; the other failures are in each flow's list, including two that are cross-cutting — **an expired session** and **a second tab on the same account** |

**Three things the fixes produced that the critique did not predict.**

1. **The file needed a third kind of ending.** Applying *is this person actually stuck?* to all ten
   endings moved **four** out of red, and the two-colour legend could not hold the difference between
   *you were told and proceeded* and *there is nothing left to do*. **`Cost:` now exists, in amber**, and
   **three genuine `Stuck:` remain in the whole file** — two outside our reach and one the product's
   only refusal. **Two flows — RJ-1 and RJ-2b — now have no dead end at all**, which is a result rather
   than a gap: they are the flows about findings, and a finding never blocks anybody.
2. **The single-item flow was restructured rather than patched.** Adding the shelf branch pushed it to
   **0.716**, below this file's own scale floor. **Narrowing the branch barely helped — the width was
   the three-way fork**, so the fork moved **below the check**, which is also more accurate: nobody
   knows a `requires` edge is dangling until the walk runs. **The product does not ask; the check finds
   out.**
3. **The scale floor turned out to be wrong, and rendering caught it.** At 0.716 the diagram was
   rendered alone and looked at, and **every label reads without effort** — its width is empty space
   from two back edges, not density. **`0.74` and `900 units` are demoted to a screen rather than a
   verdict**, and the restated rule is in `flows.md`.

**One thing got worse and is not fixed.** The main job is **3,528 pixels tall on 31 nodes** — the only
diagram over 3,000, and three revisions have each made it taller. **The owner's open question about
splitting it along *assemble · check · hand over* is the one item nothing has touched.**

---

## Proposed fixes, in order — the list as it stood before any of them was applied

**The method's rule: the list above is the deliverable, and these are proposals.** *Kept unedited; what
happened to each is in the table above.*

1. **Draw the receiver's flow**, with the revoked-link state in it. *Largest gap, and it subsumes 2.3
   and 2.6.*
2. **RJ-2b's dead end → the unclean-export route** (1.1). *The diagram currently contradicts §6.*
3. **RJ-4's keys branch loops back to the add form** (1.2), and **the single-item flow gets RJ-3's shelf
   branch** (1.3). *Two flows disagreeing with two others about the same situation.*
4. **RJ-1: route `no run to re-read` back into `Checking`** (1.4), and **re-shape `exported unread` as a
   costly success** (1.5).
5. **Restore first-run empty `My library`** on the panel (2.4) and **add empty `Projects`** (2.5).
   *The first is a regression I introduced this morning.*
6. **Take the sign-in surface to the register** (4.1) before drawing anything, and **note the depth
   table's cold-start gap** (3.4).
7. **Wording, all cheap**: the path-B trade (3.1), path C's stale description (3.2), the two-entry
   deviation (3.3), the pair-not-habit line (4.2), the shelf's changed basis (4.3), and the one line
   marking RJ-2a's refusal as unique (1.6).
8. **`loading` is not on this list on purpose** (2.1). It is a composition decision, it belongs to
   lesson 04, and putting spinners in seven diagrams before deciding what waiting looks like would be
   the appearance creep this lesson's plan lists as trap 2.
