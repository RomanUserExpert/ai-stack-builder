# User flows — lesson 03, information architecture

> **Written 2026-09-16, out of [`sitemap.md`](sitemap.md) and nothing else.** Every screen node in
> these diagrams is a screen, mode, overlay or state that section already established. **No new screen
> was invented, and none was needed** — which is the first thing the exercise was meant to test.
>
> **Five flows: the main job, and four related ones.** Each is drawn from
> [`jtbd.md`](../research/7-jobs-to-be-done/jtbd.md), named with the job's own wording rather than with
> a feature name, and each ends in **both** kinds of ending — the one where the person is done, and the
> ones where they are stuck.

**How to read the shapes.**

| Shape | Meaning |
|---|---|
| `[ rectangle ]` | **A screen, mode or overlay** — the name is the one [`sitemap.md`](sitemap.md) uses |
| `[/ parallelogram /]` | **A state** of one of those — empty, loading, filtered to zero, mid-check, stale, error |
| `{ diamond }` | **A decision**, always a yes/no question. **The green branch is *yes*, the red branch is *no*** |
| `([ stadium ])` | **An ending.** Green = the job is closed · red = a dead end, where the person is stuck |

**One thing the colours do not mean.** A red branch is not a failure and a green one is not a success —
*no* is often the right answer. The colour marks **which way the question was answered**, and the
ending nodes are where success and dead ends are actually distinguished.

---

## The main job — "when something I have already got working has to live somewhere else, I want it to keep working there"

[The main job](../research/7-jobs-to-be-done/jtbd.md#the-main-job) · **P1**, primary · `✓` + `*`, and
the loudest number in the evidence base sits inside it.


```mermaid
flowchart TD
    A["Projects"] --> B{"Is there already a project for this work?"}
    B -->|"No"| C[/"Projects: first run, only the example project"/]
    C --> D["Project"]
    B -->|"Yes"| D
    D --> E{"Does the set have anything in it?"}
    E -->|"No"| F[/"Project: no members yet"/]
    F --> G{"Press Check anyway?"}
    G -->|"Yes"| H[/"Run: every stage Skipped, a neutral glyph it did not earn either way"/]
    H --> I(["Dead end: an empty archive, and nothing was checked"])
    G -->|"No"| J["Palette: ⌘K, opens cold on related items"]
    E -->|"Yes"| K["Project: rows carrying their own state"]
    J --> L{"Did the palette have anything to offer?"}
    L -->|"No"| M[/"Palette: filtered to zero"/]
    M --> N["Library: My library"]
    N --> O{"Is My library empty?"}
    O -->|"Yes"| P[/"Library: My library empty on first run"/]
    P --> Q["Library: Public library, read-only"]
    Q --> J
    O -->|"No"| J
    L -->|"Yes"| K
    K --> R{"Is the set complete?"}
    R -->|"No"| J
    R -->|"Yes"| S[/"Run: check in progress"/]
    S --> T{"Did the check find Problems?"}
    T -->|"Yes"| U["Run: findings, each annotating the row that owns it"]
    U --> V{"Can it be fixed from this row?"}
    V -->|"Yes"| K
    V -->|"No"| W[/"Run: unclean export confirmation, in the row below the finding"/]
    W --> X["Run: the handover stages"]
    T -->|"No"| X
    X --> Y{"Is the agent target the right one?"}
    Y -->|"No"| Z[/"Run: target changed, verdict void, the check runs again"/]
    Z --> S
    Y -->|"Yes"| AA["Export: the final stage of Run"]
    AA --> AB(["Archive in hand: this set was checked, and checked is not works"])
    AB --> AC{"Does the receiving machine have the env values?"}
    AC -->|"Yes"| AD(["It keeps working there: the main job is closed"])
    AC -->|"No"| AE(["Dead end: .env.example names the keys, and we never held the values"])
    classDef screen fill:#12161c,stroke:#7c8899,stroke-width:1px,color:#e8edf4
    classDef state fill:#1b1a12,stroke:#a8913f,stroke-width:1px,color:#f4efdd
    classDef win fill:#0d2b1e,stroke:#16a34a,stroke-width:2px,color:#dff5e8
    classDef dead fill:#2b1114,stroke:#dc2626,stroke-width:2px,color:#fadfe1
    linkStyle 3,7,10,15,19,22,24,26,33,36 stroke:#16a34a,stroke-width:2px
    linkStyle 1,5,9,12,18,21,27,29,31,37 stroke:#dc2626,stroke-width:2px
    class A,D,J,K,N,Q,U,X,AA screen
    class C,F,H,M,P,S,W,Z state
    class AD,AB win
    class I,AE dead
```

**The decisions, in words.**

1. **Is there already a project for this work?** — the only fork at the top, and it is why `Projects`
   is the first screen on a first run rather than `Library` (§Navigation).
2. **Does the set have anything in it?** — the state nobody designs for, and the one that produces the
   product's emptiest possible result.
3. **Press Check anyway?** — kept as a real branch because nothing blocks: the button is live on an
   empty set exactly as it is on a full one.
4. **Did the palette have anything to offer?** — the palette is *the only way the library reaches this
   screen* (§8), so a cold palette is a wall, not an inconvenience.
5. **Is My library empty?** — §11 guarantees it is, on first run. The way out is the `Public library`
   scope, which is why the shelf exists at all.
6. **Is the set complete?** — the loop back into the palette. This is where the product's real depth
   lives: selection, not traversal.
7. **Did the check find Problems?** — three severities, and none of them blocks.
8. **Can it be fixed from this row?** — §8 says a finding annotates the row that owns it. When the fix
   is four items away, this is a *no*, and the unclean export is the honest route.
9. **Is the agent target the right one?** — changing it **voids the verdict** (§6), because a path
   collision is a collision *under a target*.
10. **Does the receiving machine have the env values?** — the product's ceiling, drawn as a decision it
    does not get to make.

**The states, in words.** *Projects holding only the example project* · *a project with no members* ·
*every stage Skipped* · *the palette filtered to zero* · *`My library` empty on first run* · *the
check in progress* · *the unclean-export confirmation* · *the verdict voided by a target change*.

**Where a person gets stuck.** Two places, and neither is an error. **An empty archive** — they checked
a set with nothing in it, got a column of neutral glyphs, and exported a zip that teaches nothing.
**The env values on the other side** — the archive is correct, `.env.example` names the keys, and the
product has nothing to give them because `needsEnv` holds names and never values. That second one is
the main job's own ceiling: **checked, never works.**

---

## RJ-1 — "know what the other side will still need, before I send it"

[RJ-1](../research/7-jobs-to-be-done/jtbd.md#rj-1--know-what-the-other-side-will-still-need-before-i-send-it)
· **P1** sending, **P2** receiving · importance **`[?]`** for the primary — the cell was withdrawn by
the audit and hunted for twice since.


```mermaid
flowchart TD
    A["Project"] --> B{"Has anything changed since the last check?"}
    B -->|"Yes"| C[/"Projects: checked 3 days ago, out of date since db-tools was edited"/]
    C --> D[/"Run: check in progress"/]
    B -->|"No"| E{"Trust the old verdict and skip the check?"}
    E -->|"Yes"| F(["Dead end: the verdict is a moment, and the handover is only read during a run"])
    E -->|"No"| D
    D --> G{"Did every stage resolve?"}
    G -->|"No"| H["Run: findings, before the handover"]
    H --> A
    G -->|"Yes"| I["Run: the handover stages begin"]
    I --> J{"Is the agent target the one the other side uses?"}
    J -->|"No"| K[/"Run: target changed, verdict void, paths and reader both change"/]
    K --> D
    J -->|"Yes"| L["Run: SETUP.md preview, pinned refs, target-correct paths"]
    L --> M{"Does anything external lack a pinned ref?"}
    M -->|"Yes"| N[/"Run: an external item with no pinned ref, a Note"/]
    N --> O["Library: My library"]
    O --> P["Item: add or edit form"]
    P --> A
    M -->|"No"| Q{"Does any item defer to something outside the set?"}
    Q -->|"Yes"| R[/"Run: this item defers to the client's ESLint config, a Note that never clears"/]
    R --> S["Run: .env.example, the last stage before Export"]
    Q -->|"No"| S
    S --> T{"Read the handover before pressing Export?"}
    T -->|"No"| U(["Dead end: Export is irreversible and the disclosure was there to be read first"])
    T -->|"Yes"| V["Export: the final stage of Run"]
    V --> W(["Archive in hand, and the sender knows what the other side still needs"])
    classDef screen fill:#12161c,stroke:#7c8899,stroke-width:1px,color:#e8edf4
    classDef state fill:#1b1a12,stroke:#a8913f,stroke-width:1px,color:#f4efdd
    classDef win fill:#0d2b1e,stroke:#16a34a,stroke-width:2px,color:#dff5e8
    classDef dead fill:#2b1114,stroke:#dc2626,stroke-width:2px,color:#fadfe1
    linkStyle 1,4,9,13,15,20,25 stroke:#16a34a,stroke-width:2px
    linkStyle 3,5,7,11,19,22,24 stroke:#dc2626,stroke-width:2px
    class A,H,I,L,O,P,S,V screen
    class C,D,K,N,R state
    class W win
    class F,U dead
```

**The decisions, in words.**

1. **Has anything changed since the last check?** — six events void a verdict (§6), and one of them is
   an edit to an item the person never touched because `requires` pulled it in.
2. **Trust the old verdict and skip the check?** — there is nothing to trust: the verdict survives as
   counts and a date, the findings do not, and **the handover stages only exist inside a run.**
3. **Did every stage resolve?** — findings come before the handover; an unresolvable requirement is
   read on the project, not in the disclosure.
4. **Is the agent target the one the other side uses?** — it selects the paths **and the reader**, since
   `SETUP.md` is addressed to an agent.
5. **Does anything external lack a pinned ref?** — a Note, and the one the handover test proved
   load-bearing: the receiving agent used the pins to fetch back both items the archive had lost.
6. **Does any item defer to something outside the set?** — Q10's Note, carried to the receiver because
   **the receiver is the person whose linter it is going to be.**
7. **Read the handover before pressing Export?** — the whole job in one question.

**The states, in words.** *A stale verdict naming what voided it* · *the check in progress* · *the
verdict voided by a target change* · *an unpinned external item* · *a deference Note that never
clears*.

**Where a person gets stuck.** **Skipping the check** — because no run is stored, there is no page
where last week's handover can be re-read; re-reading means checking again, and a person who does not
know that will look for a link that does not exist. **Pressing Export without reading** — the
disclosure was placed before the irreversible step precisely so this could not happen quietly, and the
flow draws it as reachable anyway, because nothing blocks.

---

## RJ-2 — "find out what my pieces drag in, and where two of them will fight, while I can still act"

[RJ-2](../research/7-jobs-to-be-done/jtbd.md#rj-2--find-out-what-my-pieces-drag-in-and-where-two-of-them-will-fight-while-i-can-still-act)
· **P1** · importance **3**, and `✓` that **nothing on the market has this object at all**: four skill
managers were run against a deliberately broken set and none saw a set-level defect.


```mermaid
flowchart TD
    A["Project"] --> B["Palette: ⌘K, opens cold on related items"]
    B --> C[/"Project: the row is selected manually"/]
    C --> D{"Does it require anything?"}
    D -->|"Yes"| E[/"Project: auto-added rows, each naming what pulled it in"/]
    D -->|"No"| F["Project: the set as it stands"]
    E --> F
    F --> G{"Do you want one of those rows out of the set?"}
    G -->|"Yes"| H{"Is that row auto-added?"}
    H -->|"No"| I[/"Project: the row is gone"/]
    I --> F
    H -->|"Yes"| J{"Remove the item that pulled it in instead?"}
    J -->|"Yes"| I
    J -->|"No"| K(["Dead end: an auto-added row cannot be removed while its puller is in the set"])
    G -->|"No"| L[/"Run: check in progress"/]
    L --> M{"Did the walk find a cycle?"}
    M -->|"Yes"| N[/"Run: these three always travel together, information and not a failure"/]
    M -->|"No"| O["Run: findings, each annotating the row that owns it"]
    N --> O
    O --> P{"Is any of it a Problem?"}
    P -->|"No"| Q(["The set is legible: what it drags in and where it would fight, while there is still time to act"])
    P -->|"Yes"| R{"Is a required item missing from the library altogether?"}
    R -->|"Yes"| S[/"Run: an unresolvable requirement"/]
    S --> T["Library: My library"]
    T --> U["Item: add or edit form"]
    U --> A
    R -->|"No"| V[/"Run: a declared conflict, a duplicate command name or a target-path collision"/]
    V --> W{"Can you act on it from the row that owns it?"}
    W -->|"Yes"| X["Project: drop one of them, or change a target path"]
    X --> Y[/"Projects: the verdict is void, because the set changed"/]
    Y --> L
    W -->|"No"| Z(["Dead end: the fix is not in this project, and the archive will carry only one of the two"])
    classDef screen fill:#12161c,stroke:#7c8899,stroke-width:1px,color:#e8edf4
    classDef state fill:#1b1a12,stroke:#a8913f,stroke-width:1px,color:#f4efdd
    classDef win fill:#0d2b1e,stroke:#16a34a,stroke-width:2px,color:#dff5e8
    classDef dead fill:#2b1114,stroke:#dc2626,stroke-width:2px,color:#fadfe1
    linkStyle 3,7,10,11,15,20,21,27 stroke:#16a34a,stroke-width:2px
    linkStyle 4,8,12,13,16,19,25,30 stroke:#dc2626,stroke-width:2px
    class A,B,F,O,T,U,X screen
    class C,E,I,L,N,S,V,Y state
    class Q win
    class K,Z dead
```

**The decisions, in words.** *Rewritten 2026-09-16: the first version of this diagram mixed the two
moments — it asked about **check findings** on the Project screen, before and after the run. Every
Problem in §6 is produced by the check and nowhere else, and the flow now says so.*

1. **Does it require anything?** — the depth-first walk, run at the moment the item is added. Auto-added
   rows appear on the Project screen **with no check involved**, each naming what pulled it in.
2. **Do you want one of those rows out of the set?** — the removal branch, and the only place in the
   entire specification where the product refuses an action.
3. **Is that row auto-added?** and **remove the item that pulled it in instead?** — the refusal has a
   shape, and it is worth drawing: **you do not remove the dependency, you remove what dragged it in.**
   A person who does not see that is genuinely stuck.
4. **Did the walk find a cycle?** — **not an error.** A project is a set and never an execution order,
   so the answer is *these three always travel together*, reported as information.
5. **Is any of it a Problem?** — and this is the only place the word appears, because **the check is the
   only thing that produces one.**
6. **Is a required item missing from the library altogether?** — an unresolvable requirement, whose fix
   leaves this flow entirely: you go and author the missing item, and come back to a set that has
   changed.
7. **Can you act on it from the row that owns it?** — §8 says a finding annotates its own row. When it
   can be acted on, the set changes and **the verdict is void**, which is why the loop goes back through
   the check rather than around it.

**The states, in words.** *A row selected manually* · *auto-added rows naming what pulled them in* · *a
row removed* · *the check in progress* · *a cycle reported as information* · *an unresolvable
requirement* · *a conflict, a duplicate command name or a target-path collision* · *the verdict voided
because the set changed*.

**Where a person gets stuck.** **The auto-added row that will not go** — the product's one refusal, and
the dead end is real: if it does not occur to you to remove the puller instead, there is no other way
out. **The Problem you cannot reach from here** — the fix is four items away or in another project, and
the archive will carry only one of the two, which is correct behaviour and still a bad afternoon.

**What changed in the redraw, since the first version was wrong rather than merely rough.** The old
diagram asked *is a required item missing* and *do two items write to the same target path* as
questions on the Project screen — but both are findings **§6 produces inside the check**. It also had a
removal branch that made no sense (if the puller is gone, the row is not auto-added any more), and it
asked about a path collision **immediately after removing a row**, which **voids the verdict** and makes
the question unanswerable until a new check runs. The three moments are now separate: **assemble ·
try to remove · check · act.**

---

## RJ-3 — "fix something once and have the fix reach every copy of it"

[RJ-3](../research/7-jobs-to-be-done/jtbd.md#rj-3--fix-something-once-and-have-the-fix-reach-every-copy-of-it)
· **P1** · importance **3** · `✓` that copies drift and **stay** drifted: 14% of 7,506 duplicated items
out of sync now, 383 divergences open at a median of 121 days, four ever reconciled.


```mermaid
flowchart TD
    A["Library: My library"] --> B{"Can you find the item?"}
    B -->|"No"| C[/"Library: filtered to zero"/]
    C --> D{"Is it on the shelf rather than yours?"}
    D -->|"Yes"| E["Library: Public library, read-only"]
    E --> F["Library: copy it into My library"]
    F --> A
    D -->|"No"| G(["Dead end: you cannot fix what you cannot find, and nothing here prompts a review"])
    B -->|"Yes"| H["Item: add or edit form"]
    H --> I[/"Item: used in 3 projects, and saving un-checks all three"/]
    I --> J{"Still want to change it?"}
    J -->|"No"| A
    J -->|"Yes"| K["Library: the item is saved once"]
    K --> L[/"Projects: every project holding it now reads as out of date"/]
    L --> M{"Is a copy of it detached in some project?"}
    M -->|"No"| N["Project"]
    M -->|"Yes"| O{"Did anything tell you about the detached copy?"}
    O -->|"No"| P(["Dead end: the detached copy keeps the old version, silently, in a project you did not open"])
    O -->|"Yes"| Q["Detached row: edit, reset, promote"]
    Q --> R{"Reset it back to the library version?"}
    R -->|"Yes"| N
    R -->|"No"| S[/"Detached row: kept as a deliberate exception, with the differing fields named"/]
    S --> N
    N --> T[/"Run: check in progress"/]
    T --> U(["One edit, and every linked copy has it"])
    classDef screen fill:#12161c,stroke:#7c8899,stroke-width:1px,color:#e8edf4
    classDef state fill:#1b1a12,stroke:#a8913f,stroke-width:1px,color:#f4efdd
    classDef win fill:#0d2b1e,stroke:#16a34a,stroke-width:2px,color:#dff5e8
    classDef dead fill:#2b1114,stroke:#dc2626,stroke-width:2px,color:#fadfe1
    linkStyle 3,7,11,15,17,19 stroke:#16a34a,stroke-width:2px
    linkStyle 1,6,10,14,16,20 stroke:#dc2626,stroke-width:2px
    class A,E,F,H,K,N,Q screen
    class C,I,L,S,T state
    class U win
    class G,P dead
```

**The decisions, in words.**

1. **Can you find the item?** — H-J1, importance **2**, and the thinnest evidence behind any screen in
   the product.
2. **Is it on the shelf rather than yours?** — the `Public library` scope is read-only: you copy it
   into `My library` and own the copy from then on, which is the only way to make it fixable.
3. **Still want to change it?** — the blast radius is disclosed **before any field is editable**, which
   is where it had to go once `Item` stayed a form rather than becoming a place.
4. **Is a copy of it detached in some project?** — the exception `detached` and `overrides` exist for.
5. **Did anything tell you about the detached copy?** — the honest question, and the answer today is
   that the Library row does not say it.
6. **Reset it back to the library version?** — a *no* is a legitimate answer: the override was the
   point, and the row names the fields that differ.

**The states, in words.** *The Library filtered to zero* · *the blast radius at the head of the form* ·
*every holding project reading as out of date* · *a detached row kept deliberately* · *the check in
progress*.

**Where a person gets stuck.** **The item they cannot find** — nothing in this product prompts a
review of the corpus, which the practitioner on record says plainly: *"I basically never go in there to
read or review."* **The detached copy nobody mentioned** — the fix reaches every **linked** copy and
by design skips the detached one, and this flow is where that design decision becomes a person
discovering it weeks later. **It is the sharpest thing these five diagrams found**, and it is listed in
`sitemap.md` as an open consequence rather than quietly fixed here.

---

## RJ-4 — "move my work without moving my secrets or my client's business with it"

[RJ-4](../research/7-jobs-to-be-done/jtbd.md#rj-4--move-my-work-without-moving-my-secrets-or-my-clients-business-with-it)
· **P1** and **P2** · `✓`, the largest crowd on a fear after the multi-target family — 192, 54, 45, 32,
23, 22 across three trackers.


```mermaid
flowchart TD
    A["Library: My library"] --> B{"Bringing in the whole library as JSON?"}
    B -->|"No"| C["Item: add or edit form"]
    B -->|"Yes"| D["Library: import and export as JSON"]
    C --> E[/"Library: check that these files carry no keys"/]
    D --> E
    E --> F{"Did you take the keys out?"}
    F -->|"Yes"| G["Library: My library"]
    F -->|"No"| H(["Dead end: we do not read your files looking for secrets, so nothing here will stop it"])
    G --> I["Project"]
    I --> J[/"Run: check in progress"/]
    J --> K{"Does the set need env keys it does not carry?"}
    K -->|"Yes"| L[/"Run: the missing names collected, a Note, never the values"/]
    K -->|"No"| M["Run: the handover stages"]
    L --> M
    M --> N{"Share a link instead of sending the archive?"}
    N -->|"No"| O["Export: the final stage of Run"]
    O --> P(["Archive in hand: env values were never in it, because we never held any"])
    N -->|"Yes"| Q["Project"]
    Q --> R[/"Project: what becomes visible, including that item content is visible"/]
    R --> S{"Is anything in that content yours to publish?"}
    S -->|"No"| T[/"Project: the private and the reusable are tangled, a Note we cannot detect for you"/]
    T --> U["Item: add or edit form"]
    U --> Q
    S -->|"Yes"| V["Shared project"]
    V --> X{"Change your mind and revoke it?"}
    X -->|"Yes"| Y[/"Project: the address is dead, and nothing already taken comes back"/]
    Y --> Z(["Dead end: revoking recalls nothing, and the product says so at that moment"])
    X -->|"No"| W
    classDef screen fill:#12161c,stroke:#7c8899,stroke-width:1px,color:#e8edf4
    classDef state fill:#1b1a12,stroke:#a8913f,stroke-width:1px,color:#f4efdd
    classDef win fill:#0d2b1e,stroke:#16a34a,stroke-width:2px,color:#dff5e8
    classDef dead fill:#2b1114,stroke:#dc2626,stroke-width:2px,color:#fadfe1
    linkStyle 2,6,11,17,23,25 stroke:#16a34a,stroke-width:2px
    linkStyle 1,7,12,15,20,27 stroke:#dc2626,stroke-width:2px
    class A,C,D,G,I,M,O,Q,U,V screen
    class E,J,L,R,T,Y state
    class P,W win
    class H,Z dead
```

**The decisions, in words.**

1. **Bringing in the whole library as JSON?** — both answers land on the same warning, which is the
   point: **the library has exactly one way in, so there is exactly one place to say this.** *Yes* is
   the orphan — §10 commits to JSON import and export and **no job raises it.**
2. **Did you take the keys out?** — **asked of the person, never answered by the product.** This is the
   decision that used to be a refusal and became a warning on 2026-09-16: detection was the part that
   could not be built, and a block standing on a scan we do not trust stops the file that was fine.
3. **Does the set need env keys it does not carry?** — a Note, and the strongest guarantee in the
   product sits under it: `needsEnv` holds **names and never values**, so there is structurally no
   value to leak.
4. **Share a link instead of sending the archive?** — the two exits, and until 2026-09-16 only one of
   them was ever going to be checked.
5. **Is anything in that content yours to publish?** — the tangled case a practitioner actually
   described: a client's internal API shape in an example, a rule naming a client, an env key whose own
   **name** names a customer. **We cannot detect these and must not pretend to.**
6. **Change your mind and revoke it?** — a real branch with an ending that is not a success.

**The states, in words.** *The warning where material comes in* · *the check in progress* · *missing env
names as a Note* · *the sharing disclosure* · *the tangled-content Note* · *a revoked address*.

**Where a person gets stuck.** **The key they left in** — nothing in this product will catch it, and
the flow says so out loud rather than drawing a scanner that does not exist. **The link they revoked**
— the address dies and every copy already taken lives on, which the product must state **at the moment
of revoking** rather than implying a recall.

---

## What these five flows did to the sitemap

**Nothing, and that is the result worth recording.** Every node above is a screen, mode, overlay or
state that [`sitemap.md`](sitemap.md) had already established — **no new screen appeared, in five flows
covering the main job and four related ones.** An information architecture that needs a new place the
moment somebody walks a real path through it is an architecture that was drawn from a product rather
than from jobs.

**Three things the flows surfaced that the static map did not, and each is a consequence rather than a
gap.**

1. **The detached copy nobody is told about** (RJ-3). *Fix it once and have the fix reach every copy*
   is importance **3**, and a detached row is **by design** not reached. The Library row that says
   *used in 3 projects* does not say *and one of them will not get this.* **The mechanism is correct
   and the disclosure is missing**, which is a step 5 question about what the form's head says, not a
   change to §5.
2. **The empty set that checks clean** (main job). A project with no members produces a column of
   Skipped and an archive containing nothing. §6 gave *Skipped* its own neutral glyph for exactly this
   honesty, and the flow shows the one path where neutral glyphs all the way down is still a wasted
   afternoon.
3. **Two of the eight dead ends are outside the product** (the env values on the receiving machine, the
   revoked link's copies). **Neither is a defect and neither can be designed away** — they are the
   shape of *checked, never works* and of *revoking recalls nothing*, drawn so that step 5 writes
   sentences for them instead of discovering them.
