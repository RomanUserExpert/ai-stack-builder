# Voice — how AI Stack Builder speaks

> **The contract any line of the product is written against.** Lesson 05 builds it in three parts.
> **Complete as of 2026-10-05.** It has four parts: **Principles** (step 2), the **Dictionary** and
> the **Forbidden** list (step 3), and the **Microcopy** rules by element (step 4). From here on, the
> whole product is written against it. Every line in
> [`microcopy.md`](microcopy.md) has to be defensible from this file. **A principle here is a rule,
> never an adjective**: each has one sentence for how the product speaks, a line written by it, a
> line that breaks it, and the line of our research it comes from. A principle without that last
> part was not kept.

**Who it is written for.** The primary reader is **P1, the keeper**
([`personas.md`](../02-personas-jtbd/6-personas/personas.md)). This person has been copying the same
files between projects for a year. They suspect half of what they keep does nothing, and they arrive
from one of three situations, none of which is browsing. What they hand over can break on a machine
they will never see, and their keys and their client's business ride inside the files. **They want
specifics, not an advertisement**, and the whole category they are choosing from writes like a shop
([`research.md` §10](../01-research/research.md)).

**What is already fixed and only restated here.** *Checked, never works*, findings in the present
tense, three severities, nothing blocks, the keys reminder that says it is a reminder: all of these
are in `CLAUDE.md` §5, §6 and §11. The principles explain why they hold, and extend them to the lines
`CLAUDE.md` never wrote: empty states, waits, failures of our own, buttons.

---

## Principles

### 1 · Say what was examined, never what it means

**Rule.** The product speaks like **an inspector's report, not a seller's badge**: it states what it
looked at and what it found, and it never makes a claim it did not earn by looking.

**Example.**
> Checked just now · 1 problem · 2 notes · 1 skipped
>
> Command names — Skipped: no item declares a command.

**Anti-example.**
> ✓ Your stack works. Verified and production-ready.
>
> Quality score 93 · Passing

**Explanation.** The doubt on record is not *is my set broken* but *does any of this do anything*.
**EJ-2**, `✓`: *"Blackbox oracles make bad workflows, and tend to produce a whole lot of cargo
culting"* ([`jtbd.md` §3](../02-personas-jtbd/7-jobs-to-be-done/jtbd.md)). P1's card lists what repels:
**"A green tick that was not earned… someone who suspects half his material does nothing will read
an unearned tick as proof the checker is decoration"** ([`personas.md`](../02-personas-jtbd/6-personas/personas.md),
*Trust triggers*). **This is where the voice differs from the competitors.** Trust in the category
is a number or a badge: Smithery's `Verified` and *22.49k uses*, Glama's *Quality Score*, Tessl's
*You get a score*, mcp.so's *Hand-picked, production-ready* ([`research.md` §10](../01-research/research.md),
points 1–2). We run nothing, so a word like *verified* or *works* would be the one claim we cannot
back. *Skipped* is the clearest place this shows: the product says it had nothing to check rather than
awarding a tick.

*Settles:* **D19**, which keeps every verdict line in the *checked* form. **D23**, where a stage that
did not finish says so, never a blank or a tick.

---

### 2 · Name the consequence, in the reader's terms, before the step

**Rule.** The product speaks like **a colleague who tells you what will happen, not an alarm that
tells you to be careful**. Before anything irreversible it says what will change and for whom, in the
present tense, and then it lets the person act.

**Example.**
> Two items write to `.mcp.json`. The archive will contain only one of them — `db-tools`.
>
> `db-migrate` is used in 3 projects. Deleting it may stop them working.

**Anti-example.**
> Warning: conflicts detected. Are you sure you want to continue?
>
> Export blocked: unresolved conflicts.

**Explanation.** P1's card lists among what convinces: **"A consequence named in the present tense
before the irreversible step"**, from Vercel's *"You can't reveal this value after saving"*
([`personas.md`](../02-personas-jtbd/6-personas/personas.md), *Trust triggers*, `M`). The research
gives the shape, which is mechanism, condition, consequence: *"`baseHints ||=` short-circuits… so
PPR-strategy prefetches of fully-static routes deopt to runtime"*. It also names our own worst
instinct as *"Export blocked: unresolved conflicts"*
([`ci-failure-copy.md`](../01-research/2-flows/11-copy-and-error-language/ci-failure-copy.md) §4–5).
**This is common ground with the best competitors, not a difference.** Vercel lists *"deployments,
domains, environment variables, and settings"* before a delete, and none of the sources reached writes
a bare *Are you sure?* ([`research.md` §10](../01-research/research.md), point 4). So it is a floor
the voice must not drop below, not something to claim as ours.

*Settles:* the form of every confirmation. It also sets a test for **D20**: a button that opens one
of these sentences must not promise less than the sentence delivers.

---

### 3 · Say what we did and what we did not, and own our own failures

**Rule.** The product speaks like **a tool that tells you when it made a choice, and when it could
not do its part**. It names its own limits before you rely on them, and it never lets a failure of
ours read as a fault in your work.

**Example.**
> Check that these files carry no keys. We don't read your files looking for secrets.
>
> Our server stopped during this stage. It says nothing about whether agent-dotfiles holds together.

**Anti-example.**
> Your files are safe — we scan everything for secrets.
>
> Something went wrong. Check failed.

**Explanation.** **EJ-1**, `✓` and `*`, the strongest emotional job in the file: *"When a tool makes
a choice I did not make, I want it to tell me it made one"*. Behind it are servers *"silently synced…
without any opt-in, notification, or consent"* (#20412, 142 reactions) and instructions *"dropped and
never sent to the model — with no warning anywhere"* (codex #13386)
([`jtbd.md` §3](../02-personas-jtbd/7-jobs-to-be-done/jtbd.md)). P1's pains: *"broken config doesn't
announce itself, it degrades quietly"* ([`personas.md`](../02-personas-jtbd/6-personas/personas.md),
`*`). A product that writes *Check failed* when its own server stopped does exactly that. It degrades
quietly, and it hands the person a fault that is not theirs. **Against the competitors:** Tessl opens
its trust pitch with *"One in seven skills carries a critical security risk"* and sells a scan as the
answer. Claude Code's docs say the same risk as a plain instruction and sell nothing
([`research.md` §10](../01-research/research.md), point 3). Our keys reminder is the second kind, and
it has to say so.

*Settles:* **D9**. When the failure is ours, the product says *our*, in every state and not only on
the receiver's side. Step 3 picks the exact words. It also settles **L1**: a register id like
*(Q28)* is us talking to ourselves on the person's screen.

---

### 4 · Counts and names, not adjectives

**Rule.** The product speaks like **someone who has counted, not someone who is selling**: a number
that can be checked, and the name of the thing it counts, in place of any word that grades.

**Example.**
> Used in 3 projects · 1 item requires this · last exported 12 days ago
>
> Nothing matches "terraform" among your agents. You have 11 items — the search hides all of them in this tab.

**Anti-example.**
> Popular · Trending · A great fit for your stack
>
> No results.

**Explanation.** P1, asked with our vocabulary forbidden, invented this unprompted: **"Usage data,
first. Just: this file was loaded in 40 sessions, this one in 2, this one never. That alone would let
me delete half of it with confidence."** ([`personas.md`](../02-personas-jtbd/6-personas/personas.md),
`*`, *the strongest form a `*` can take*). The benchmark's best consequence disclosure is a count you
can open, *"95 workspace settings are not applied"*. Its rule is **"the number you can act on, next to
the control that produced it — and never the word *none*"**
([`research.md` §3](../01-research/research.md), mechanism 2). **Against the competitors:** registries
describe the shelf with scale and judgement — *96,436 in the Glama Registry*, *thousands of tools*,
*Sprinkle a little magic* — rather than the item ([`research.md` §10](../01-research/research.md),
points 1 and 6). The people nearest to our shelf say how that reads: *"when I've looked at them it's
been some YouTuber trying to make money"* and *"I do not understand the appeal of skill shopping"*
([`personas.md`](../02-personas-jtbd/6-personas/personas.md), P3, `✓`).

**The ceiling is part of the rule.** A count says *is it used*. It never says *is it any good*, and
no line may read one as the other (`CLAUDE.md` §5, Q22).

*Settles:* **D13**, where an empty or filtered list says what it holds and what hides it. **V1**,
where *pieces*, *pipelines and harnesses* are words that stand in for a count of named kinds. **U3**,
where a count on the screen must agree with the screen. It also leaves a dictionary question for step
3: the plain verb over the vendor's metaphor, `Install Extension` against `Add to toolbox`
([`research.md` §10](../01-research/research.md), point 5).

---

### 5 · Write for whoever acts next

**Rule.** The product speaks **to the person or agent who has to do the next thing, about what they
will have to do**. The owner, a receiver and the agent reading `SETUP.md` are three readers, and a
line is written for the one in front of it.

**Example.**
> Your machine needs a value for `GITHUB_TOKEN`. The archive carries only its name. *(a receiver)*
>
> Needs DATABASE_URL. Ask the person for it; do not invent one. *(`SETUP.md`, for the agent)*

**Anti-example.**
> Configure environment variables as needed.
>
> Some setup may be required.

**Explanation.** **SJ-1**: *"that was the moment I understood the config had become **tribal knowledge
rather than a setup**"*. Behind it, a contractor with broken paths who *"assumed that was normal and
worked around it for two days without mentioning it"* ([`jtbd.md` §4](../02-personas-jtbd/7-jobs-to-be-done/jtbd.md),
[`personas.md`](../02-personas-jtbd/6-personas/personas.md) P2, `*`, n = 1). It is **not one person
only**. When receivers were read through their forks, **30 of 214 wrote 21,266 lines of setup and
handover manual the sender never shipped**, naming the files `HANDOFF.md` and `SETUP.md`
([`research.md` §9](../01-research/research.md), `✓` on the diffs). A line written for nobody in
particular, like *Configure as needed*, is the gap those 21,266 lines were written to fill.

**What the rule does not license.** P2 has never spoken in the first person, and `CLAUDE.md` §8 gives
the receiver's surfaces the most conservative rule in the product. So a line addressed to the receiver
states **what their machine needs**, which the evidence supports. It never guesses at **how they
feel**, which nobody has asked.

*Settles:* **D18**, *the receiving machine* for the owner and *your machine* for the receiver. That is
a variant made **on purpose**, and step 3 keeps it rather than flattening it. It also decides who the
generated `SETUP.md` is written for (`CLAUDE.md` §6).

---

### What did not become a principle, and why

- **"Short and fast, like Linear."** The audience lives in Linear, Vercel and Raycast (`CLAUDE.md` §3),
  but nothing in the research says *brevity* convinces this person. The best lines on record are long
  where the consequence is long (npm `ERESOLVE`). Length is a rule per element, in step 4, not a
  principle.
- **"Calm, because they arrive irritated."** P1's second most frequent mode is an edit written in
  irritation, and whether that holds for anyone else is **`[?]` → H1**. A principle tuned to a mood
  ranked second, on one person's word, would be the invented kind.
- **"Welcoming to newcomers."** P3 has never been observed. Its nearest voices refuse the shelf rather
  than ask to be welcomed, so a warm onboarding register would be written for a person nobody has met
  (`CLAUDE.md` §9, and lesson 03's trap 3: *do not invent a place for a person nobody has met*).
- **The form of address** — imperative, *you*, or neither — is a dictionary decision and is made in
  step 3. Principle 5 constrains it: whatever the form, the line is addressed to whoever acts next.

---

## Dictionary

**One concept, one word.** Written 2026-10-05 in step 3, from the marks in
[`microcopy.md`](microcopy.md). No new search was made: each entry closes a mark the inventory already
found. **It extends `CLAUDE.md` §4 and does not compete with it.** *Item, Project, Library, Workspace*
keep their meanings, and *Bundle* stays retired. The **why** of each entry is written in the words
the people in the research use, or it points at the principle that decides it. Where neither
applies, the entry says so.

### How the product addresses the person

| | The rule | Why |
|---|---|---|
| **The person** | **"you"**, the same on every screen: *You have 11 items.* *Your machine needs a value for `GITHUB_TOKEN`.* | English has no *ты/вы*. What the course's question becomes here is whether there is a second person at all, and the answer is yes. Principle 5 says a line is addressed to whoever acts next, and *you* is the only form that names them |
| **Buttons and commands** | **Imperative, no pronoun**: `Export…`, `Check again`, `Copy to My library`, `Clear search` | The button is the person speaking. *Copy into **my** library* mixes the two voices on one control (D5) |
| **The product about itself** | **"we" and "our"**, only for what the product did or failed to do: *We don't read your files looking for secrets.* *Our server didn't answer.* **Never *I***, and never a *we* that cheers (*We're glad you're here*) | Principle 3: the tool says when it made a choice and when it failed. EJ-1: *"silently synced… without any opt-in, notification, or consent"* |
| **"my"** | **Only inside the proper name `My library`**. Everywhere else the product says *you/your* | The name is the nav entry, written from the person's side. A sentence that says *my* in the product's own voice (*a library of my own*) is the product pretending to be the person |
| **`SETUP.md`** | **Imperative to the agent, uncontracted**: *Ask the person for it; do not invent one.* The human is *the person* | Principle 5: this file's reader is an agent, and *do not* is harder to misread than *don't* |
| **Contractions** | **Yes, in everything addressed to a person**: *didn't*, *can't*, *don't*. This settles **T2** | Most of the inventory already contracts, and *did not* survives in five lines (T2), where it reads as a second author |

### The words

**Places and objects**

| Concept | **Write** | **Not** | Why | Closes |
|---|---|---|---|---|
| The person's own items | **`My library`**, always as the name | *your library*, *the library*, *the Library*, *my library*, *a library of my own*, *your items*, *your own items* | It is the word on the nav and the scope switch, so it is the word the person clicks. The ownership in it is the point: the material is theirs, and `CLAUDE.md` §11 keeps anybody else's work out of *a space labelled mine*. A bare *library* cannot tell the reader which of the two places is meant. So *Your library is empty* becomes *No items in My library yet*, and *Search your items…* becomes *Search My library…* | D1 |
| The curated shelf | **`Public library`** | *the shelf*, *items we have checked* | *Shelf* is our internal word, used in `CLAUDE.md` and the research, and it never appears on a control the person can press. The audience's own name for such places is a **registry** (Tessl, Glama), which is the thing §9 refuses to be. So we use the name on the nav, plainly | D2 |
| A named set of items | **project** | *the set*, *this set*, *the stack* | It is the person's own word for a piece of work: *"at project four I got annoyed and made a repo"*, *"10+ repos with shared conventions"*. *Set* is a word from inside our specification. So *Remove from the set* becomes *Remove from project*, *1 problem is still in the set* becomes *in this project*, and the stage *Resolve the set* becomes **Requirements**. **`Stack` stays informal** (`CLAUDE.md` §4) and does not appear in the interface, apart from the product's own name | D6 |
| One building block | **item** · in prose, by kind: **skill, agent, prompt, MCP server, script, app** | *piece*, *block*, *pipeline*, *harness* | The six kinds are the model's (§5), and the plural prose is how practitioners file them: *"MCP Servers Don't Work with NVM"*, *"20-30+ skills"*. *Pipelines and harnesses* names no kind the product has. The door's line becomes *skills, agents, prompts, MCP servers, scripts and apps* | V1 |
| The kind on a badge or tab | **the kind as written in the model**: `skill` `agent` `prompt` `mcp` `script` `app` | *MCP* on a badge, *mcp servers* in prose | Two altitudes of one word, kept on purpose: the badge shows the field value, the way `.mcp.json` does, and prose spells it out. **No other kind needs this**, because only `mcp` is an abbreviation | V2 |
| What leaves the product | **archive** | *zip*, *bundle*, *package*, *export* as a noun | `CLAUDE.md` §4 retired *Bundle*. *Archive* is what `.zip` is to anybody who has been handed one, and the file name carries the extension anyway | D4 |

**The run, the check, the export.** *This is the `Run` / `Export` question that lesson 04 handed over
(Q16), and it is answered as naming only.*

| Concept | **Write** | **Not** | Why | Closes |
|---|---|---|---|---|
| The control that starts it, everywhere | **`Export…`**: on Project (the main control, and the configuring head), on a shared project, on a shared item, on a Library row exporting one item | *Check* as the entry, *Check this set*, *Check it, then take the archive*, *Take as an archive* | **The owner's decision, Q36.** The act is named for its outcome, the archive, and the check is its sub-process. **The `…` keeps principle 2**: it says more is shown before the act completes, and the mode shows every finding and the handover before the archive exists | D3 |
| The surface it opens | **`Export`** as the title, with the subject in the meta line: *acme-billing-api · 14 items · for Claude Code* | *Check*, *Export one item*, *Take as an archive* | One mode entered four ways is still one mode (§8), titled for what it ends in | D3 |
| The check inside it | **Checking — stage N of 10** · **Checked …** · **`Check again`** | *Exporting* for the check | Principle 1: the verdict keeps *checked*. Only the act around it is named *Export* | D3 |
| Building the archive | **`Export`**, as the final stage and its button, **for the owner and the receiver alike**: `Export`, `Export with 1 problem`, `Export again` | *Take the archive*, *Download the archive*, *Build the archive again* | The research's wow moment is *"the export"* (`CLAUDE.md` §2), and a receiver who checks and takes the archive performs the same act on somebody else's work. The entry's `Export…` and this `Export` are one act, opened and then completed | D4 |
| It is built | **Exported — `acme-billing-api-claude-code.zip`** | *Archive built — …*, *Archive downloaded — …* | One word for the outcome, for both readers, and it matches the button that caused it | D4 |
| Fetching the same file again | **`Download again`** | — | **A different act, so a different word.** Nothing is rebuilt or re-checked; the browser fetches the file it already has | D4 |

> **Decided by the owner on the sample, 2026-10-05 (Q36).** This dictionary first recommended `Check`
> as the entry. The owner chose `Export`, which puts Export on the Project screen, so it went to the
> register first (`research-plan.md`, Q36; `CLAUDE.md` §6, §8).

**Relations and states**

| Concept | **Write** | **Not** | Why | Closes |
|---|---|---|---|---|
| An item that came in because another requires it | **auto-added**: the badge `Auto-added`; *3 auto-added*; a11y *Auto-added for migration-reviewer*; *requires `db-migrate`, `postgres-mcp` · 3 auto-added* | *pulled in by*, *brings 3 items with it*, *the 3 items it brings*, *comes in with them*, *the walk along `requires` added 3* | It says that **the tool** made a choice the person did not. That is EJ-1 exactly: *"silently synced… without any opt-in"*, and *"the first one wins"*. *Pulled in* and *brings* make it sound as if the item did it. *Walk* is a word from our algorithm, not from the screen | D7 |
| The relation fields | **requires** · **required by** · **conflicts with** · **defers to** | *dependency*, *depends on*, *needs* (for an item) | They are the model's fields (§5), and the person fills them in by hand. **`needs` is kept for env keys only**: *needs `DATABASE_URL`* | — |
| A project's own copy of an item | **detached**: the badge `Detached`, the action `Detach`, *1 detached* | *modified in this project*, *differs from the library* | The audience knows the word from Figma, where *detach* is exactly this act (`CLAUDE.md` §5, flow 05) | D8 |
| The copy in My library a row links to | **the original**: *2 fields differ from the original*; *Reset to the original*; *Linked to the original in My library* | *the library version*, *Library version*, *Library:*, *the library* | *Version* promises a history that does not exist, and §9 refuses versioning by name. The promote dialog already says *the original `pr-reviewer`*, and the detach note says *keep the original* | D8 |
| A row tied to the original | **linked** | — | One word for one state: *linked* is the opposite of *detached* | D8 |
| Taking somebody else's item | **`Copy to My library`**, on the Public library, a shared project, a shared item, and after a shared check | *Copy into my library*, *Copy into a library of my own* | One label for one act. The copy keeps its origin, which is why it is *copy*, not *add* | D5 |
| Making a new item from your own material | **`Add to My library`** (the submit of *Add item*) | — | **A different act**: nothing has an origin elsewhere. Two verbs, because §11 treats the two ways in differently, and only one of them carries the keys reminder | D5 |

**Checks and verdicts**

| Concept | **Write** | **Not** | Why | Closes |
|---|---|---|---|---|
| The verdict | **Checked** + when + *for* target + the three counts, **zeros included**: *Checked 2 days ago · for Claude Code · 1 problem · 2 notes · 1 skipped* | *works*, *valid*, *passing*, *verified*, a bare ✓; *code-style, checked by you*; *Just now · …* | Principle 1 and `CLAUDE.md` §6. **All three counts always**, so *0 problems* is a count you read rather than an absence you infer (principle 4) | D19 |
| Who checked, when it was not the owner | **by you** or **by Maya** after the time: *Checked just now by you*; *Maya checked it 5 days ago · for Claude Code* | *Maya last checked it…* | The same line, plus who. The receiver needs to know which verdict is theirs (§6) | D19 |
| A stage that started and did not finish | **Stopped — our server didn't answer** | *Didn't complete*, *Couldn't be written* | One word for the event and one reason, in our voice (principle 3) | D23 |
| A stage after it | **Not run** | — | The check never reached it. That is not *Waiting*, because nothing will come | D23 |
| A stage not reached yet, while the check runs | **Waiting** | — | Something will come | D23 |
| The three severities | **Problem · Note · Skipped** | *error*, *warning*, *info*, *failed* | `CLAUDE.md` §6, unchanged | — |
| The keys | **env key**; its **name**; its **value** | *env variable*, *secret*, *token* (as the class) | The field is `needsEnv` and holds names. Practitioners file it as *"api keys in plain text"* and *"loads my project's `.env`"*. **The name / value split is the whole guarantee** (§6: no value is ever stored) | — |

**Failures, waits and leaving**

| Concept | **Write** | **Not** | Why | Closes |
|---|---|---|---|---|
| Our failure | **Our server didn't answer** · **Our server stopped at …** | *The server did not answer*, *something broke on our side*, *Something went wrong* | Principle 3: one voice, ours. P1's pain is *"broken config doesn't announce itself, it degrades quietly"*, and a failure with no owner is that pain | D9, T2 |
| The error code | On its own line, always the same three parts: **`503 · Service unavailable · 14:02`** | `503 · 14:07`; the code at the end of a sentence | A code is for the person who reports it. It is read separately from the sentence and should look the same every time it is copied | D10 |
| Data arriving | **Loading** + what: *Loading My library*, *Loading acme-billing-api*, *Loading the shared project* | *Opening …* | One verb for one wait. *Opening* says nothing *Loading* does not, and it reads like a different event | D11 |
| The check running | **Checking — stage 4 of 10** | *Checking…* with no count | Principle 4: *N of M* is the count you can read | D11 |
| Trying again | **The verb that will happen again, + *again***: `Load again`, `Save again`, `Check again`, `Export again`, `Import again`, `Promote again`, `Write SETUP.md again` | `Try again`, `Try the import again`, `Build the archive again`, `Write it again` | Principle 2: the button names what it does. *Try* names nothing | D12 |
| Never anything here | **No … yet**: *No items in My library yet*, *No projects yet*, *No items in this project yet* | *Your library is empty*, *My library is empty*, *Nothing in this project yet* | One form for one state. *Yet* is true: the state ends when the person adds something | D13 |
| Filtered to zero | **Nothing matches "…"**, then the count the search hides: *Nothing matches "stripe" among projects that are Not checked yet. You have 5 projects — the search and the filter hide all of them.* | *No items match*, *No projects match*, *Nothing called "sentry" here* | Principle 4: the number you can act on, and never only *none* (research §3, mechanism 2) | D13 |
| Undoing a search | **`Clear search`** | `Clear search · show All` | One act per label. Showing All is the tab, already one click away | D14 |
| Undoing filters | **`Clear filters`**, in the popover and on the filtered state | `Reset filters` | The same act in two places takes the same word | D14 |
| A search box | **Search** + the place + **—** + three real examples: *Search My library — migrate, GITHUB_TOKEN, review* | *Search your items by name, description or tag*, *Search the shelf…* | The place is named as it is on the nav (D1, D2). The examples teach what is searchable better than a list of fields | D15 |
| Leaving a dialog without acting | **`Cancel`** | `Dismiss` | Nothing happens, and *Cancel* is the word for that | D16 |
| Closing something that only informs | **`Close`** | — | There is nothing to cancel | D16 |
| Leaving with edits unsaved | **`Discard changes`** | — | **A different act with a cost**, so it is named (principle 2) | D16 |

**The door and the share**

| Concept | **Write** | **Not** | Why | Closes |
|---|---|---|---|---|
| Signing in | **`Sign in`**, as the title, the button and the link | `Sign in instead` | One act, one label | D17 |
| Making an account | **`Create account`**, as the title, the button and the link | *Create an account* | As above | D17 |
| Getting a new password | **`Reset password`**, as the link on Sign in, the title and the error's button. The form's submit is **`Send reset link`** | *Forgot password?*, *Reset your password*, *Send a reset link* | Three labels led to one place. The submit is a different act: it sends | D17 |
| Sharing | **`Share…`** opens the disclosure · **`Create link`** confirms · **`Stop sharing…`** revokes | `Share the project` | The button opens a dialog, so it takes the `…` (D20). *Create link* says exactly what confirming does | D21 |
| Removing an item from a project | **`Remove from project`** · a11y *Remove code-style from this project* · in Check: **`Remove eslint-autofix…`** | *Remove from the set*, *Remove in Configure* | One verb, *remove*, which is the word §6 uses. *Remove in Configure* names a place, not an act. In viewing it becomes the fact *To remove it, configure the project*, and the control stays where §8 puts it | D22 |
| The machine the archive lands on | **the receiving machine** for the owner · **your machine** for the receiver | — | **A variant kept on purpose** (principle 5). Each reader is told about the machine that is theirs to act on. *What your machine will need* becomes *What your machine still needs*, so the receiver sees one form | D18 |

### Jargon: what is allowed, and what never reaches a screen

**Allowed, because the person writes it in their own files and trackers:** *MCP server*, *skill*,
*agent*, *prompt*, *env key*, *repo*, *commit*, *ref* (*pinned ref*), *licence id* (SPDX: `MIT`,
`Apache-2.0`), *agent target*, file names as code (`SETUP.md`, `CLAUDE.md`, `.mcp.json`,
`.env.example`). The evidence base is written in these words: *"MCP Servers Don't Work with NVM"*,
*"my CLAUDE.md says one thing"*, *"pins registry commits"*.

**Never on a screen, because these are our words about the product, not the person's words about
their work:**

| Internal word | On a screen it is |
|---|---|
| *resolved set*, *stack*, *the walk* | the project · *auto-added* · *Requirements* |
| *shelf* | Public library |
| *overrides* | *2 fields differ from the original* |
| *blast radius*, *puller* | *used in 3 projects* · *auto-added for migration-reviewer* |
| *deference* (as a noun) | the stage **Defers to**, the field *defers to* |
| *cohere*, *coherent* | *checked* |
| register ids, persona ids (*Q28*, *P1*, *RJ-1*) | nothing — they are removed (**L1**) |

### Spelling and typography

- **American spelling**, so the product matches the audience's tools: **`License`**, not *Licence*.
  The model's field is `license`, and so are `package.json` and every SPDX page. This settles **T3**.
  *User content keeps its own spelling (*summarised* is theirs).*
- **Curly quotes and apostrophes**: `’` `“ ”`. Never `'` or `"` in product copy (**T1**). Code keeps
  its own straight quotes.
- **One separator per job.** ` · ` joins facts on one line. ` — ` opens an explanation or a
  consequence. A colon introduces a list.
- **`…` on a button means it opens a confirmation first**: `Delete item…`, `Share…`,
  `Remove eslint-autofix…`, `Promote to My library…`, `Delete example…`, `Stop sharing…`. **A
  button in progress takes no `…`**. It reads *Signing in* with the spinner beside it, so the glyph
  keeps one meaning (**D20**).
- **Numbers as digits**, units after a space: *3 projects*, *41 KB*, *0.3 s*.

---

## Forbidden

**What the product never writes, each with what it was or would be, and what it is instead.** The
inventory found **no** cheer, clichés, exclamations or emoji on any of the 80 pages
([`microcopy.md`](microcopy.md), *No cheer, no clichés*). So where a *was* is marked
*(not on our screens)*, it is the line the category writes in the same place, and it is listed so
the next writer recognises it. Where the *was* is from our own pages, it is quoted.

### AI clichés and service cheer

| Forbidden | Was / would be | Instead |
|---|---|---|
| **The apologetic shrug** | *(not on our screens)* **Oops, something went wrong.** | **Our server didn't answer, so your projects can't be shown.** · `503 · Service unavailable · 14:02` · `Load again` |
| **Welcome** | *(not on our screens)* **Welcome to AI Stack Builder! Let's get started.** | Sign in's title is **`Sign in`**. The empty library says what it holds and what to do: **No items in My library yet.** *Add the first one, import a library you exported before, or copy from the Public library.* |
| **Congratulations, success** | *(not on our screens)* **🎉 Congratulations! Your project was successfully exported!** | **Exported — `acme-billing-api-claude-code.zip`** · *18 files · 41 KB · saved to Downloads. Checked just now · 1 problem · 2 notes · 1 skipped.* |
| **The word *successfully*** | *(not on our screens)* **Item successfully saved.** | Nothing, if the result is visible. If it is not: **Saved.** *Successfully* adds a grade to a fact (principle 4) |
| **The apology that names nothing** | *(not on our screens)* **Sorry, we couldn't load your library. Please try again later.** | **Our server didn't answer, so My library can't be shown right now.** `Load again`. *Sorry* and *please* stand in for the cause, and principle 3 says to give the cause |
| **The unearned verdict** | *(not on our screens)* **✓ All good — your stack works!** | **Checked just now · 0 problems · 0 notes · 3 skipped.** *Works* promises the receiving machine, which belongs to nobody in this product (`CLAUDE.md` §6) |

### The motivational and the selling

| Forbidden | Was / would be | Instead |
|---|---|---|
| **The journey** | *(not on our screens)* **Start your journey to the perfect AI stack.** | **A project holds items from My library. It is checked as a whole and exported as one archive.** *(The empty Projects line as it reads now, *a set of items*, with D6's word fixed.)* |
| **The promise of magic and speed** | Raycast: *"Sprinkle a little magic on your day"*; Tessl: *"Build your software factory"* · *(ours would be)* **Build your dream stack in seconds!** | **What this checks: requirements, conflicts, command names, target paths, env keys, what each item defers to, pinned refs.** A list the person can verify instead of a feeling they cannot |
| **Grades and shop words** | Smithery `Verified`; mcp.so *"Hand-picked, production-ready"*; Glama *"Quality Score"* · *(ours would be)* **Popular · Recommended · Best for your stack** | **Used in 3 projects · last exported 12 days ago** · on the Public library: **`modelcontextprotocol/servers` @ `2025.9.25` · MIT**, which is the origin, not a grade (`CLAUDE.md` §5: no score, no rating, no badge) |
| **Selling with fear** | Tessl: *"One in seven skills carries a critical security risk"*, followed by its score · *(ours would be)* **Protect your secrets — scan with AI Stack Builder** | **Check that these files carry no keys. We don't read your files looking for secrets.** The risk is stated, and so is the fact that we did not look (principle 3, `CLAUDE.md` §11) |
| **The minimiser** | *(not on our screens)* **Just pick a few items and you're done!** | **Tick items on the left to add them. Anything they require is auto-added.** *Just*, *simply* and *easily* tell a person their difficulty is not real. P1's forty minutes per project is real (`personas.md`, *Jobs*) |
| **The vendor's metaphor** | Smithery `Add to toolbox`; Claude Code *"adds it to its toolkit"* · *(ours would be)* **Add to your arsenal** | **`Copy to My library`** · **`Add to My library`**. The plain verb and the name on the nav |

### Punctuation, glyphs and register

| Forbidden | Was / would be | Instead |
|---|---|---|
| **Exclamation marks** | *(not on our screens)* **Link created!** | **Link created.** Better still, show the link with **`Copy link`** beside it. The page shows it happened |
| **Emoji in system messages** | *(not on our screens)* **✅ 3 keys named · ⚠️ 1 problem** | **3 keys named · 1 problem.** Severity is carried by the **glyph beside the line** (Problem, Note, Skipped, `CLAUDE.md` §6), which is designed, neutral for *Skipped*, and never inside the sentence |
| **Shouting** | *(not on our screens)* **WARNING: CONFLICT DETECTED** | **`eslint-autofix` declares a conflict with `code-style`: it rewrites the imports `code-style` tells the agent to keep.** Mechanism, then consequence (principle 2) |
| ***Are you sure?*** | *(not on our screens)* **Are you sure you want to delete db-migrate?** | **`db-migrate` is used in 3 projects. Deleting it may stop them working.** · `Delete` · `Cancel`. None of the competitors reached writes it either (`research.md` §10, point 4) |
| **Internal ids and our own jargon** | Ours, Run · `run-error-setup`: **…not because there is nothing to say (Q28).** | **…not because there is nothing to say.** Register ids, persona ids and the words in *Never on a screen* above are for this repository, not for the person (**L1**) |
| **Blocking words** | Our own worst instinct, from the research: **Export blocked: unresolved conflicts.** | **1 problem is still in this project. The archive will contain both `eslint-autofix` and `code-style`.** · `Export with 1 problem`. Nothing blocks (`CLAUDE.md` §6) |

---

## Microcopy — rules by element

**The last part of the contract.** Written 2026-10-05 in step 4. Each rule has one example from AI
Stack Builder, written by the dictionary above, and a line saying which principle and dictionary
entries it was checked against. **The states follow
[`04-wireframes/_screens.md`](../04-wireframes/_screens.md)**, the map of which states each screen
has. *Success* exists only where an outcome exists: the archive at the end of `Export`, a finished import, a
reset link sent. A list or a project opening is a view of data, not an outcome, and it gets no
success line.

**Where an example line differs from the page today, the example is the target.** Steps 5 and 6
carry it onto the page.

### Button

**Rule.** **A verb, plus the object when the screen does not already name it, so the result is
visible from the label.** If the act has a cost, the label carries it. A button that opens a
confirmation ends in `…`. Never *OK*, *Next*, *Continue*, *Submit*, *Yes*, or *Confirm*.

**Example.**
> `Export with 1 problem` · `Copy to My library` · `Remove eslint-autofix…` · `Export…`

*`Export…` stands alone because the screen's title is the object: it sits under* acme-billing-api. *The
same rule writes `Load again` on an error, never `Try again`.*

**Not.** `Continue`, which is Vercel's second step on a delete (research §10, 14) · `OK` · `Yes,
delete` · `Proceed anyway`.

*Checked against:* principle 2 (the label is the first sentence of the consequence) · Dictionary,
*Trying again* (D12), *`…` on a button* (D20), *Copy / Add* (D5), *the control that starts it* (D3, Q36).

### Screen title

**Rule.** **The name of the place, in the dictionary's words. On an object's own screen, the object's
name.** A title is a noun, never a sentence and never a greeting. A mode the person has entered is
shown as a badge beside the title, not by renaming it.

**Example.**
> `My library` · `Public library` · `Projects` · `acme-billing-api` with the badge `Configuring` · `Export`

**Not.** *Your library* · *Welcome back, Maya* · *Let's build your stack* · *Export one item* as the
title of the same mode entered from a Library row.

*Checked against:* principle 4 (a name, not an adjective) · Dictionary, *My library* (D1), *Public
library* (D2), *the surface it opens* (D3) · Forbidden, *Welcome*.

### Form field

**Rule.** **The label says what to enter, as a noun from the dictionary. The hint says how, with a
real example. A validation error names the field, says exactly what is wrong with what was typed, and
says what would be right.** It appears under the field it is about, never in a banner. Errors about
the person's own input are said in plain terms, without *we*: the fault is not ours, and principle 3
does not ask us to take it.

**Example.**
> **Env keys it needs** · *hint:* Names only, like `DATABASE_URL`. Values never live here.
>
> **Email** · *error:* `maya@chen` has no domain. An email address looks like `maya@chen.dev`.

*The wireframes draw no field-level validation yet. Sign in's error is form-level, and on purpose:
**Email or password is wrong** does not say which. The second example shows the form a field error
takes when one is drawn, not a new rule about what is validated.*

**Not.** *Invalid input* · *Please enter a valid value* · *Env variables (optional)* · a hint that
repeats the label.

*Checked against:* principle 4 (name what is wrong, never only *invalid*) · principle 5 (the person
fixing it is the reader) · Dictionary, *env key, name, value*.

### Empty state

**Rule.** **Why it is empty, then what to do next, with the action as a button.** There are two
empties and they never share words. **Never had anything** reads *No … yet*: say what belongs here,
and offer the ways in. **Filtered to zero** reads *Nothing matches "…"*: say how many the search and
filters hide, and offer the way to clear them. The more likely it is that the reader does not know
what the place is for, the more an empty state explains. A first-run Projects page explains. A tab
filtered to zero only counts.

**Example.**
> **No projects yet.** A project holds items from My library. It is checked as a whole and exported
> as one archive. · `New project` · `Open Public library`
>
> **Nothing matches "stripe"** among projects that are Not checked yet. You have 5 projects — the
> search and the filter hide all of them. · `Clear filters`

**Not.** *No results.* · *It's lonely in here!* · *Start your journey…* · an empty state with no
button.

*Checked against:* principle 4 (the count you can act on, never only *none*) · Dictionary, *Never
anything here*, *Filtered to zero* (D13), *Undoing filters* (D14) · research §3, mechanism 2 ·
personas, P3 *Repels: emptiness that is also a dead end*.

### Error

**Rule.** **Say what happened and whose failure it is. Then say what did not change, and what to do
now: a button with the verb that will happen again, and a second way out that does not depend on
what failed.** The code goes on its own line, for whoever reports it. No apology, no joke, no
*something*. *What did not change* is not optional: it is the half that tells a person their work is
safe (Q26, Q27).

**Example.**
> **Our server didn't answer, so your projects can't be shown.** Nothing in them changed.
> `Load again` · `Open My library`
> `503 · Service unavailable · 14:02`

**Not.** *Oops! Something went wrong.* · *Sorry, please try again later.* · *Check failed* when our
server stopped, which hands the person a fault that is not theirs.

*Checked against:* principle 3 (our failures in our voice) · principle 2 (what will happen if they
press) · Dictionary, *Our failure* (D9), *The error code* (D10), *Trying again* (D12) · Forbidden,
*The apologetic shrug*, *The apology that names nothing*.

### Loading

**Rule.** **A short wait is silent: the skeleton of what is coming, with nothing to read.** A wait
that is long, staged, or risky **says exactly what is loading, and how far it has got**, as *N of M*
where there is a count. A wait that could leave something half-done also says what happens if it
stops, **while it runs**, not after (Q27). The words are *Loading* + what, *Checking — stage N of 10*,
*Exporting — N of M files*.

**Example.**
> *(Projects on arrival: the card grid as skeletons, no text.)*
>
> **Importing 47 items** · 18 of 47 · `release-notes` · If this stops before the end, My library
> stays exactly as it was before the import — none of the 47 are kept.

**Not.** *Please wait…* · *Hang tight, magic is happening* · *Loading…* over a stage list that could
say which stage · *Opening acme-billing-api* beside *Loading projects*.

*Checked against:* principle 4 (*N of M*) · principle 3 (say what happens if it stops) · Dictionary,
*Data arriving*, *The check running* (D11) · Forbidden, *The promise of magic and speed*.

### Success

**Rule.** **Name the fact, with its numbers. Then name the next step: what still has to happen, and
the control for it.** A success line restates what was produced and what was checked, never that it
*works*. No celebration, no *successfully*, no exclamation.

**Example.**
> **Exported — `acme-billing-api-claude-code.zip`** · 18 files · 41 KB · saved to Downloads. Checked
> just now · 1 problem · 2 notes · 1 skipped.
> The receiving machine still needs: values for `DATABASE_URL`, `GITHUB_TOKEN` and
> `SENTRY_AUTH_TOKEN` · three repos cloned at their pinned refs — `SETUP.md` says which.
> `Download again` · `Share…`

**Not.** *🎉 Your project was successfully exported!* · *All set — it's ready to go!* · *Archive
built* for the owner beside *Archive downloaded* for the receiver.

*Checked against:* principle 1 (*checked*, never *works*) · principle 5 (the next step for whoever acts
next: here, the receiving machine) · Dictionary, *It is built*, *Fetching the same file again* (D4),
*The verdict* (D19) · Forbidden, *Congratulations, success*, *successfully*.

### Dangerous action

**Rule.** **Before the press, say what will happen, to what, with the count expanded into names.
Say what stays, and say what cannot be undone.** The confirm button repeats the verb of the act;
`Cancel` sits beside it. **Nothing is blocked and nothing asks the person to type a name.** We confirm
rather than refuse (`CLAUDE.md` §6), and the cost is carried by the sentence, not by friction. An
unclean export is confirmed **in the row under the finding**, never in a modal.

**Example.**
> **Delete db-migrate?**
> `db-migrate` is used in 3 projects: acme-billing-api · agent-dotfiles · docs-site-rewrite. Deleting
> it may stop them working. `migration-reviewer` requires it, so that requirement will point at
> nothing, and the next check in each project names it as a Problem. This can't be undone.
> `Delete` · `Cancel`
>
> **Stop sharing acme-billing-api?** The link stops working at once. It can't reach what was already
> taken: anyone who exported the archive or copied its items keeps them. `Stop sharing` · `Cancel`

**Not.** *Are you sure?* · *This action is irreversible. Continue?* · `Yes` / `No` · GitHub's
type-the-name step, which is friction standing in for a sentence.

*Checked against:* principle 2 (the consequence in the reader's terms, before the step) · principle 4
(the count, and the names behind it) · Dictionary, *`…` on a button* (D20), *Sharing* (D21),
*Removing an item* (D22) · Forbidden, *Are you sure?*, *Blocking words* · research §10, point 4.
