# Microcopy — every line of the product

> **The source of truth for every line of the product, as of 2026-10-05 (lesson 05 closed).** It began as step 1's inventory, nothing rewritten, and the findings below are that inventory's. Written 2026-10-05 from the 80 product
> pages in [`04-wireframes/pages/`](../04-wireframes/pages/wireframes.html), as they stand after Q35.
> **By the end of the lesson this file is the source of truth**, the table every line of the product
> is checked against. In step 5 it gains *was / now*, and in step 7 it has to match the screens line for line.
> For now it records what the screens say, and **marks where they say the same thing differently**.

**How it was made.** [`tools/extract_copy.py`](../tools/extract_copy.py) reads every page and takes
out each line of text along with its zone and type. It also reads the attributes a person meets
without seeing them: `placeholder`, `aria-label`, `title`. Then
[`tools/build_microcopy.py`](../tools/build_microcopy.py) groups the lines by screen, folds a line
repeated across a screen's state pages into one row, decides whose words each line is, and applies
the marks. **5,300 occurrences across 80 pages make 1,462 rows**, and 764 of the lines are distinct.
The findings below were written by hand from those marks and checked against the pages.
*Once step 5 starts, the table is edited by hand and the script is not run over it again.*

**Left out on purpose.** Stage numbers (`01`…`10`) and durations (`0.3 s`, `—`), which are values
and not copy. Each page's `<title>` (*Run · default — wireframe*), which belongs to the wireframe and
not the product. The viewer `wireframes.html`. HTML comments. The 239 prototype pages, because they
are generated from these pages (`README.md`, *Our mapping*) and are rebuilt rather than inventoried.

---

## How to read the table

| Column | What it holds |
|---|---|
| **Screen** | One of the 17 screens on the map, plus *Everywhere — the app header*, listed once instead of 46 times |
| **Zone** | Where on the screen: the region and the landmark above it — *Run bar*, *Library panel › Row*, *Modal: Delete db-migrate?*, *Stages: Findings › Finding* |
| **Line** | The text exactly as it stands. `code` marks a value set in code on the page — a slot |
| **Type** | `title` · `heading` · `button` · `link` · `nav` · `field label` · `field hint` · `placeholder` · `option` · `state message` · `status label` · `severity` · `state badge` · `kind badge` · `stage name` · `stage result` · `fact` · `body` · `panel row line` · `generated file` · `item name` · `description` · `value` · `a11y label` · `tooltip` |
| **On** | Which of the screen's state pages carry the line; `all` when every one does |
| **Whose** | `product`: our words. · `product, with slots`: our sentence carrying the person's values (*`db-migrate` is used in 3 projects*); the sentence is ours to rewrite, the values are not. · `generated`: a file the product writes for the archive (`SETUP.md`, `.env.example`, the archive tree); ours, with slots. · **`user`**: **the person's own content** |
| **Mark** | The findings below, by id. A row can carry several |

**`user` is not rewritten.** That covers what the person wrote or named: item and project names,
descriptions, tags, file paths, env key **names**, repo URLs, `ref`s, licence ids, item content,
values typed into fields and search boxes, and their own name and email. **There are 362 such rows.**
The lesson changes the sentences around them, never the values.

---

## What the inventory found

### No cheer, no clichés, no placeholders left over

I searched every distinct line for exclamation marks, emoji, *successfully*, *oops*, *great*,
*congrats*, *awesome*, *welcome*, *let's*, *easily*, *simply*, *just*, *seamless*, *magic*,
*powerful*, *sorry*, *unfortunately*, *please*, *amazing*, *all set*, *lorem*, *TODO*, *TBD* and
*xxx*. **Nothing matched**, apart from *just now* in a timestamp, which is a fact and not a tone.
The wireframes were written in `CLAUDE.md`'s register from the start. What the lesson has to fix is
**inconsistency**, not cheer.

Three lines should not be on screen as they are:

| Mark | Where | What |
|---|---|---|
| **L1** | Run · `run-error-setup` | *…not because there is nothing to say **(Q28)**.* A register id has leaked into product copy |
| **L2** | Run · the `SETUP.md` stage | The preview ends in `…`. That was cut short in the drawing and is not a product decision. Step 4 decides whether a preview is cut, and how it says so |
| **L3** | Create an account · `loading` | **`Forgot password?`** appears on the sign-up form. It was copied from Sign in and appears on no other sign-up page |

### One thing under several names (D-marks)

Each item is a question for **step 3, the dictionary**. Nothing is decided here.

| Mark | The thing | Here | There | And there |
|---|---|---|---|---|
| **D1** | The person's own items | **`My library`** (nav, scope, buttons) | *your library* (*Your library is empty*, *didn't load*, *Loading your library*), *your items*, *your own items* | *the library* / *the Library* (*linked to the library version*, *edited in the Library*), *my library* (*Copy into my library*), *a library of my own*. And **the same empty state is headed two ways**: *Your library is empty* (My library) and *My library is empty* (the panel) |
| **D2** | The Public library | **`Public library`** | *the shelf* (*Search the shelf…*, *Nothing on the shelf matches*, *the shelf can't be shown*, *on the shelf*) | *items we have checked* (My library · empty) |
| **D3** | The surface the check runs on, and the verb that opens it | Run's title **`Check`** (owner) | **`Export one item`** (a single item), **`Take as an archive`** (a receiver) | The button that enters it: **`Check`** (Project), **`Check this set`**, **`Check it, then take the archive`** (Shared project), **`Take as an archive`** (Shared item). *This is the `Run` / `Export` question handed over by lesson 04 (Q16)* |
| **D4** | Getting the archive | Stage **`11 · Export`**, button **`Export with 1 problem`**, row button **`Export`** | Stage **`11 · Take the archive`**, **`Download the archive`** (receiver) | Success **`Archive built — ….zip`** (owner) vs **`Archive downloaded — ….zip`** (receiver). Retry: **`Build the archive again`**, **`Download again`** |
| **D5** | Taking an item into your own library | **`Copy to My library`** (Public library) | **`Copy into my library`** (Shared project, Shared item) | **`Copy into a library of my own`** (Run · shared success) · **`Add to My library`** (submit of the Add item overlay) |
| **D6** | What a project holds | *project* (*Nothing in this project yet*, *Fix it in the project first*, *It leaves this project only*) | ***the set*** (*Resolve the set*, *Remove from the set*, *In the set*, *Check this set*, *1 problem is still in the set*, a11y *The set*) | §4 has **Stack** as the informal word for the resolved set, and **no screen uses it** |
| **D7** | An item that came in because something requires it | **`Auto-added`** (badge), *3 auto-added* | *Pulled in by migration-reviewer* (a11y), *Pulled into every project that holds this one* (field hint) | *brings 3 items with it*, *the 3 items it brings*, *comes in with them*, *The walk along `requires` added 3*, *auto-added — required by `pr-reviewer`* |
| **D8** | Linked vs detached, and the library's copy | **`Detached`**, *1 detached*, *detached in 1*, **`Detach to edit here`** | *Modified in this project*, *differs from the library in*, *2 fields differ from the library* | *the library version* / *Library version* / *Library:* / *the original*. *linked to the library* vs *Linked to the library — an edit in My library reaches…* |
| **D9** | The server failing | *The server **did not** answer* (My library, Public library, Projects, Project) | *the server **didn't** answer* (Create an account), *Stopped — the server didn't answer* (Run stages), *The server didn't confirm the save* | ***Our** server stopped* (receiver's Run), *something broke on **our side***, *This is **our failure**, not the item's / the set's*. Three registers for one fact: impersonal, contracted and impersonal, first person |
| **D10** | The error code and time | **`503 · Service unavailable · 14:02`** on its own line | **`503 · 14:07`** on its own line | *…still here. **503 · 14:09*** at the end of a sentence (Configuring), *… (Q28). 503 · 14:06* (Run · setup) |
| **D11** | Waiting | *Loading your library*, *Loading the Public library*, *Loading projects*, *Loading the set and the library* | *Opening db-migrate*, *Opening acme-billing-api*, *Opening the shared project / item* | *Checking…*, *Checking — stage 4 of 10*, *Checking agent-dotfiles — stage 3 of 10*, *Adding — finding what it requires…*, *Signing in…*, *Creating your account…*. Some end in `…` and some do not |
| **D12** | Trying again after a failure | **`Try again`** (My library, Public library, Projects, Project) | **`Save again`**, **`Promote again`**, **`Check again`**, **`Write it again`**, **`Download again`** | **`Try the import again`**, **`Build the archive again`**. Some name the verb and some do not |
| **D13** | A list with nothing in it | *Your library is empty*, *My library is empty* | *No projects yet*, *Nothing in this project yet*, *Nothing in it yet* (fact), *Created just now · nothing in it yet* | Filtered to zero: *No items match* and *No projects match* vs ***Nothing called "sentry" here*** (Configuring) |
| **D14** | Undoing a search or a filter | **`Clear search · show All`** (My library, Public library) | **`Clear search`** (Configuring), **`Clear filters`** (Projects · filtered) | **`Reset filters`** (inside every Filters popover) |
| **D15** | The search box, by scope | *Search **your items** by name, description or tag — …* | *Search **the shelf** by name, kind or source — …* | *Search projects and the items in them — …*, ***Search My library***, ***Search Public library*** (the panel) |
| **D16** | Leaving without acting | **`Cancel`** (every dialog and the configuring head) | **`Close`** (a11y on the overlay's ✕; a button after the import fails) | **`Dismiss`** (Promote failed) · **`Discard changes`** (save failed) |
| **D17** | The door | Title *Create an account*, button **`Create account`**, link *Create an account* | Title *Reset your password*, button **`Reset password`** (Sign in · error), link *Forgot password?*, button **`Send a reset link`** | **`Sign in`**, **`Sign in instead`**, *Back to sign in* appears both as a link and as a button on Reset password |
| **D18** | The machine the archive lands on | ***the receiving machine*** (owner's Run: *Handover — what the receiving machine still needs*) | ***your machine*** (receiver: *Handover — what your machine still needs*, *Your machine still needs*) | ***What your machine will need*** (Shared project). The owner's single-item Run also says *the receiving machine* |
| **D19** | The verdict line | *Checked 2 days ago · for Claude Code · 1 problem · 2 notes · 1 skipped* | *Checked just now*, ***Checked just now, by you***, ***code-style, checked by you***, *Just now · for Claude Code · shared by Maya Chen* | *Maya last checked it 5 days ago, for Claude Code*, *checked by you with 0 problems and 2 notes*. Stage results also read *Checked — …* |
| **D20** | A button that opens a confirmation | With `…`: **`Delete item…`**, **`Promote to My library…`** | Without `…`: **`Share`**, **`Delete example`**, **`Remove eslint-autofix`** | One convention for all of them, or none |
| **D21** | Sharing | **`Share`** (rows, the Project head) | **`Share the project`** (Run · success) | **`Create link`** (the share dialog's confirm) · **`Stop sharing`** |
| **D22** | Removing an item from a project | **`Remove from the set`** (side panel) | **`Remove in Configure`** (side panel, viewing) · a11y *Remove code-style* on the ✕ | **`Remove eslint-autofix`** (Run) · **`Remove`** (a file in the overlay, and the Run confirmation) |
| **D23** | A stage that did not finish | *Didn't complete* (owner's Run · check error) | *Stopped — the server didn't answer* (single item, receiver) · *Couldn't be written* (`SETUP.md`) | Stages after it: *Not run* (after a failure) vs *Waiting* (while loading) |

### Words outside the vocabulary, and typography

| Mark | What | Where |
|---|---|---|
| **V1** | **Terms that are not in §4.** *pipelines and harnesses* is listed among the things the library holds, and neither is one of the six kinds. *the pieces every project is built from* is a synonym for *items* | The door's description (Sign in, Create an account, Reset password) · My library · empty |
| **V2** | **A kind written two ways.** The badge and tab say `mcp`, while prose says *MCP servers* (*31 skills · 6 agents · 5 prompts · 3 MCP servers · 2 scripts*) | The door · My library · empty · the import dialog |
| **T1** | **Straight apostrophes** where every other line uses `’`: *Projects didn't load*, *your projects can't be shown*, and in user content *Acme's* (Projects card) vs *Acme’s* (Project) | Projects · `error-server`, `default` |
| **T2** | **Contraction mixed.** *did not answer* in four error messages and *didn't* in the rest (see D9). *the file did not hold* in the import | Error states |
| **T3** | **British spelling** in product copy: the filter label **`Licence`**, while the data model's field is `license`. One spelling for the product, decided in step 3 | Public library · Filters |

### The person's own content — marked, not ours to rewrite

These are defects in the **drawing's sample data**, not in the voice. They are listed so they are not
mistaken for decisions.

| Mark | What |
|---|---|
| **U1** | **One item described differently on different screens**, although an item has one description (§5). *code-style*: three versions (*How I want TypeScript written: naming, imports, error handling, no default exports.* / *…error handling.* / *How TypeScript is written: …*). Also *db-migrate*, *migration-reviewer*, *postgres-mcp*, *github-mcp*, *commit-conventions* (three), *filesystem* and *memory*: each has a long version in the Library or on the shelf and a short one in the project or the shared page. *pr-reviewer* has three, and only one of them is legitimate: the **detached** row may differ, since `overrides` can change the description |
| **U2** | **Content invented in the prototypes and never confirmed** (lesson 04 handoff 6): *query-explainer*, *schema-docs*, *webapp-testing*, and the project *stripe-webhooks* |
| **U3** | **A count that contradicts the screen.** My library holds **11** items (*All 11*, and the import's success and error both say *the 11 you had*), but the import dialog says *beside the **10** you have*, and My library · filtered says *You have **10** items* |

**Lesson 04's small debt is already paid.** The env stage's *2 keys named* against three keys in
`.env.example` was fixed in `456b466` (Q35). Every Run page now says *3 keys named*, and no page
says *2 keys*.

### What this hands to the next steps

- **Step 2, principles.** The marks show the register is already uniform in content: findings name
  the consequence in the present tense, and *checked, never works* holds on every page (D19 varies
  in form, never in claim). **The variation is in form**: who speaks when the server fails (D9),
  how a wait is named (D11), and how a retry is labelled (D12).
- **Step 3, dictionary.** D1–D8, D13–D18 and D21–D23 each need one word, and V1, V2 and T3 need a
  vocabulary decision. **D3 and D4 are the `Run` / `Export` question**, with its limit from
  `README.md`: if `Export` becomes a control on the Project screen, it goes to the register.
  **D18 is the one place where a variant may be right on purpose**: the owner reads *the receiving
  machine* and the receiver reads *your machine*. Step 3 decides that rather than flattening it.
- **Step 4, element rules.** D10 (error code), D11 (waiting), D12 (retry), D16 (leaving) and D20
  (the `…` convention) are rules per element, not dictionary entries.
- **Fix with the rewrite, outside the voice.** L1, L3 and T1 are plain errors. U1 and U3 are the
  drawing's data. Step 6 corrects them where it touches the pages, and records each correction here.

---

## Step 7 — the check, and what it fixed

**2026-10-05.** Every product line on the 80 pages was checked against `voice.md` and this table. Two
scans ran first: the screens against this table in both directions, and a search for dictionary
synonyms and the forbidden list. Then all 474 distinct product lines were read by hand. **Screen ↔
table: 0 differences either way. No cliché, exclamation, emoji or *successfully*.** Twenty-two
defects were found, reviewed by the owner (*исправляй*), and fixed in the pages, the prototype
generators and this table together. **Rows changed in step 7 carry *Step 7 #n* in *Why*.**

| # | Screen | Line | What was wrong | Fixed to |
|---|---|---|---|---|
| 1 | Run · error-export | *Nothing was downloaded.* | D4: the archive is exported | *Nothing was exported.* |
| 2 | Run · shared project, error | *…whether agent-dotfiles holds together* | *holds together* is *cohere*, which never reaches a screen | *…about agent-dotfiles itself.* |
| 3 | Run · shared item, error | *Nothing was downloaded.* | D4 | *Nothing was exported.* |
| 4 | Project · detached row | `Reset whole item` | The dictionary (D8) says *Reset to the original* | `Reset to the original` |
| 5 | Sign in · error | *Check them and try again.* | *Check* is the product's verb; *try* names nothing | *Enter them again.* |
| 6 | Run · single item, shared item | *Skipped — none declared* · *Skipped — no command declared* | One check, several forms | *Skipped — no item declares a conflict / a command* |
| 7 | Run · shared item | *Skipped — none needed* | Not the *Skipped — no item …* form | *Skipped — no item needs an env key* |
| 8 | My library, Public library, Configuring · filtered | *Nothing matches “terraform” among your agents…* | The body repeated the heading. Projects did not, so one state had two forms | *The tab shows only agents. You have 11 items — …* (and *skills*, *items related to this project*) |
| 9 | Shared item | *This page is live: it shows…* | Typography: ` — ` opens an explanation | *This page is live — it shows…* |
| 10 | Shared item | *Written by Maya Chen — her own…* | A pronoun guessed from a name | *Written by Maya Chen, not from an external source* |
| 11 | Projects · delete | *Delete the example project?* | Dangerous action: name the object | *Delete repo-triage-kit?* |
| 12 | Item · delete | *…the next check in each project…* | `migration-reviewer` is in one project. The line claimed more than it knows | *…the next check in acme-billing-api…* |
| 13 | Run · shared item, success | *To know that the client’s ESLint config wins…* | A list of what the machine needs held a piece of knowledge, not a thing | *The client’s ESLint config, which wins where it disagrees with this skill* |
| 14 | Run · success | *Three repos cloned…* | Numbers as digits | *3 repos cloned…* |
| 15 | Project · share | *3 external items, at their pinned refs* | Dangerous action: a count expands into names (§6) | *3 external items: modelcontextprotocol/servers-archived, github/github-mcp-server, getsentry/sentry-mcp — at their pinned refs* |
| 16 | Reset password · success | `Check your email` | A title is a noun | `Reset link requested` |
| 17 | Create account · loading | the `Reset password` link (L3) | A stray element copied from Sign in | **Removed.** Markup change, approved |
| 18 | Item · error, Run · single item / shared project / shared item, error | — | No error-code line (D10) | `503 · Service unavailable · HH:MM` **added** on its own line. Markup change |
| 19 | Configuring · error-server, Run · error-setup | the code at the end of a sentence | D10 | Moved to a line of its own. Markup change |
| 20 | Project · revoke | the head read `Share…` | A shared project did not read as shared, and nothing opened *Stop sharing* (§8) | The badge `Shared` and `Stop sharing…`. **Q37** in the register |
| 21 | Run · single item | *4 files* | U3: the archive tree on the same page shows 8 | *8 files* |
| 22 | Library, Project, Shared pages | one item, several descriptions (U1) · *Acme's* | Sample data disagreed with itself | One description per item, the one in My library. The detached `pr-reviewer` row keeps its own, legitimately. *Acme’s* |

**Prototypes rebuilt** (37 cases, 239 pages) with the generators updated for #4, #11, #14, #15, #19 and
#22. No old phrase from this table survives in them.

---

## The table, screen by screen

**Was / Now since 2026-10-05 (steps 5, 6 and 7).** *Was* is the line as the inventory found it at
`56777bc`; *Now* is the line on the page; `=` means unchanged. Built by
`tools/build_microcopy.py` (`render_wasnow`), which walks each page at `56777bc` and as it is now:
the rewrite changed no markup until step 7, so the walks align line for line; step 7 added the error-code lines and the *Shared* badge and removed one stray link, and those rows read *(added)* / *(removed)*. *Why* names the `voice.md`
entry or mark behind each change. **Marks are those of the *Was* line** — most of them are now closed.

### Everywhere — the app header

On 46 pages — every page with the app header. Listed once.

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Everywhere — the app header | App header | AI Stack Builder | = | body | 46 pages | product |  |  |
| Everywhere — the app header | App header › Global nav | Global | = | a11y label | 46 pages | product |  |  |
| Everywhere — the app header | App header › Global nav | My library | = | nav | 46 pages | product |  |  |
| Everywhere — the app header | App header › Global nav | Public library | = | nav | 46 pages | product |  |  |
| Everywhere — the app header | App header › Global nav | Projects | = | nav | 46 pages | product |  |  |
| Everywhere — the app header | App header | Signed in as Maya Chen | = | a11y label | 46 pages | product, with slots |  |  |
| Everywhere — the app header | App header | Maya Chen | = | body | 46 pages | user |  |  |

### Sign in

State pages: `default` · `error` · `loading`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Sign in | Shared header | AI Stack Builder | = | body | all | product |  |  |
| Sign in | Main › Door | Sign in | = | title | all | product | D17 |  |
| Sign in | Main › Door | AI Stack Builder is a library for your AI work — skills, agents, prompts, MCP servers, pipelines and harnesses. Keep them in one place, add and edit them, and put them together into projects you can export. | **AI Stack Builder is a library for your AI work — skills, agents, prompts, MCP servers, scripts and apps. Keep them in one place, add and edit them, and put them together into projects you can export.** | body | all | product | D1 V1 V2 | V1: the six kinds |
| Sign in | Door › Form | Email | = | field label | all | product |  |  |
| Sign in | Door › Form | maya@chen.dev | = | placeholder | all | product |  |  |
| Sign in | Door › Form | Password | = | field label | all | product |  |  |
| Sign in | Door › Form | Forgot password? | **Reset password** | link | all | product | D17 | D17 |
| Sign in | Door › Form | Sign in | = | button | default · error | product | D17 |  |
| Sign in | Main › Door | No account yet? Create an account | **No account yet? Create account** | body | all | product | D17 | D17 |
| Sign in | Door › Finding | Email or password is wrong | = | status label | error | product |  |  |
| Sign in | Door › Finding | Check them and try again. If you don’t remember the password, reset it — we’ll send a link to maya@chen.dev. | **Enter them again. If you don’t remember the password, reset it — we’ll send a link to maya@chen.dev.** | state message | error | product, with slots |  | Step 7 #5 Check is the product's verb; name the act |
| Sign in | Door › Finding | Reset password | = | button | error | product | D17 |  |
| Sign in | Door › Form | maya@chen.dev | = | value | error · loading | user |  |  |
| Sign in | Door › Form | •••••••••• | = | value | loading | user |  |  |
| Sign in | Door › Form | Signing in… | **Signing in** | button | loading | product | D11 | D20, D11: a button in progress takes no … |
| Sign in | Door › Form | Signing in as maya@chen.dev | = | body | loading | product, with slots | D11 |  |

### Create an account

State pages: `default` · `error` · `loading`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Create an account | Shared header | AI Stack Builder | = | body | all | product |  |  |
| Create an account | Main › Door | Create an account | **Create account** | title | all | product | D17 | D17 |
| Create an account | Main › Door | AI Stack Builder is a library for your AI work — skills, agents, prompts, MCP servers, pipelines and harnesses. Keep them in one place, add and edit them, and put them together into projects you can export. | **AI Stack Builder is a library for your AI work — skills, agents, prompts, MCP servers, scripts and apps. Keep them in one place, add and edit them, and put them together into projects you can export.** | body | all | product | D1 V1 V2 | V1: the six kinds |
| Create an account | Door › Form | Email | = | field label | all | product |  |  |
| Create an account | Door › Form | maya@chen.dev | = | placeholder | all | product |  |  |
| Create an account | Door › Form | Password | = | field label | default · error | product |  |  |
| Create an account | Door › Form | Create account | = | button | default · error | product | D17 |  |
| Create an account | Main › Door | Already have an account? Sign in | = | body | all | product | D17 |  |
| Create an account | Door › Finding | The account wasn’t created | = | status label | error | product |  |  |
| Create an account | Door › Finding | That email may already have an account, or the server didn’t answer. Try again, or sign in instead. | **That email may already have an account, or our server didn’t answer. Nothing was created. Sign in if the account is yours, or create it again.** | state message | error | product | D9 D17 | D9; Error: what did not change; D12; D17 |
| Create an account | Door › Finding | Sign in instead | **Sign in** | button | error | product | D17 | D17 |
| Create an account | Door › Form | maya@chen.dev | = | value | loading | user |  |  |
| Create an account | Door › Form | Password | **(removed)** | field label | loading | product |  | Step 7 #17 (L3): the label held the stray link; it is now a plain label, below as added |
| Create an account | Door › Form | Forgot password? | **(removed)** | link | loading | product | L3 | Step 7 #17 (L3): a stray copied from Sign in — removed (it had read Reset password since step 6) |
| Create an account | Door › Form | (added) | **Password** | field label | loading | product |  | Step 7 #17 (L3): the stray Reset password link removed from the label |
| Create an account | Door › Form | •••••••••• | = | value | loading | user |  |  |
| Create an account | Door › Form | Creating your account… | **Creating account** | button | loading | product | D11 | D11, D20 |
| Create an account | Door › Form | Creating your account as maya@chen.dev | **Creating account for maya@chen.dev** | body | loading | product, with slots | D11 | D11: the wait in the button's words |

### Reset password

State pages: `default` · `success`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Reset password | Shared header | AI Stack Builder | = | body | all | product |  |  |
| Reset password | Main › Door | Reset your password | **Reset password** | title | default | product | D17 | Dictionary, Getting a new password (D17) |
| Reset password | Main › Door | AI Stack Builder is a library for your AI work — skills, agents, prompts, MCP servers, pipelines and harnesses. Keep them in one place, add and edit them, and put them together into projects you can export. | **AI Stack Builder is a library for your AI work — skills, agents, prompts, MCP servers, scripts and apps. Keep them in one place, add and edit them, and put them together into projects you can export.** | body | all | product | D1 V1 V2 | V1: the six kinds |
| Reset password | Door › Form | Email | = | field label | default | product |  |  |
| Reset password | Door › Form | maya@chen.dev | = | placeholder | default | product |  |  |
| Reset password | Door › Form | Send a reset link | **Send reset link** | button | default | product | D17 | D17 |
| Reset password | Main › Door | Back to sign in | **Sign in** | link | default | product | D17 | D17: one label for Sign in |
| Reset password | Main › Door | Check your email | **Reset link requested** | title | success | product |  | Step 7 #16 a title is a noun |
| Reset password | Main › Door | If an account exists for maya@chen.dev, a link to set a new password is on its way. It works once, for an hour. | = | body | success | product, with slots |  |  |
| Reset password | Main › Door | Back to sign in | **Sign in** | button | success | product | D17 | D17: one label for Sign in |
| Reset password | Main › Door | Nothing arrived? Send it again | = | body | success | product |  |  |

### My library

State pages: `default` · `empty` · `error-filtered` · `error-server` · `filters` · `loading`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| My library | Main › Page head | My library | = | title | all | product |  |  |
| My library | Main › Page head | Import JSON | = | button | default · error-filtered · filters · loading | product |  |  |
| My library | Main › Page head | Export JSON | = | button | default · error-filtered · filters · loading | product |  |  |
| My library | Main › Page head | Add item | = | button | default · error-filtered · error-server · filters · loading | product |  |  |
| My library | Main › Find | Find | = | a11y label | default · error-filtered · filters · loading | product |  |  |
| My library | Main › Find | Search your items by name, description or tag — migrate, GITHUB_TOKEN, review | **Search My library — migrate, GITHUB_TOKEN, review** | placeholder | default · error-filtered · filters · loading | product | D1 D15 | D1, D15 |
| My library | Main › Find | Filters | = | button | default · error-filtered · loading | product |  |  |
| My library | Main › Kind | Kind | = | a11y label | default · error-filtered · filters · loading | product |  |  |
| My library | Main › Kind | All 11 | = | nav | default · filters | product |  |  |
| My library | Main › Kind | skill 1 | = | nav | default · filters | product |  |  |
| My library | Main › Kind | agent 2 | = | nav | default · filters | product |  |  |
| My library | Main › Kind | prompt 2 | = | nav | default · filters | product |  |  |
| My library | Main › Kind | mcp 2 | = | nav | default · filters | product |  |  |
| My library | Main › Kind | script 3 | = | nav | default · filters | product |  |  |
| My library | Main › Kind | app 1 | = | nav | default · filters | product |  |  |
| My library | Main › Items | Items | = | a11y label | default · filters · loading | product |  |  |
| My library | Items › Row | code-style | = | item name | default · filters | user |  |  |
| My library | Items › Row | skill | = | kind badge | default · filters | product |  |  |
| My library | Items › Row | How I want TypeScript written: naming, imports, error handling, no default exports. | = | description | default · filters | user |  |  |
| My library | Items › Row | .claude/skills/code-style/SKILL.md | = | fact | default · filters | user |  |  |
| My library | Items › Row | Defers to the client’s ESLint config | = | fact | default · filters | product, with slots |  |  |
| My library | Items › Row | Used in 3 projects · last exported 2 days ago | = | fact | default · filters | product |  |  |
| My library | Items › Row | Edit | = | button | default · filters | product |  |  |
| My library | Items › Row | Export | **Export…** | button | default · filters | product | D4 | D3, Q36, D20 |
| My library | Items › Row | Share | **Share…** | button | default · filters | product | D20 D21 | D21, D20 |
| My library | Items › Row | db-migrate | = | item name | default · filters | user |  |  |
| My library | Items › Row | script | = | kind badge | default · filters | product |  |  |
| My library | Items › Row | Generates a Postgres migration from a schema diff and runs it — dry run first, then for real. | = | description | default · filters | user |  |  |
| My library | Items › Row | `scripts/db-migrate.sh` + 2 files | = | fact | default · filters | product, with slots |  |  |
| My library | Items › Row | Used in 3 projects · 1 item requires this · requires `seed-data` · last exported 12 days ago | = | fact | default · filters | product, with slots |  |  |
| My library | Items › Row | seed-data | = | item name | default · filters | user |  |  |
| My library | Items › Row | Loads a small, realistic dataset into a fresh database. | = | description | default · filters | user |  |  |
| My library | Items › Row | scripts/seed-data.sh | = | fact | default · filters | user |  |  |
| My library | Items › Row | Used in 3 projects · 1 item requires this | = | fact | default · filters | product |  |  |
| My library | Items › Row | migration-reviewer | = | item name | default · filters | user |  |  |
| My library | Items › Row | agent | = | kind badge | default · filters | product |  |  |
| My library | Items › Row | Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills. | = | description | default · filters | user |  |  |
| My library | Items › Row | requires `db-migrate`, `postgres-mcp` | = | fact | default · filters | product, with slots |  |  |
| My library | Items › Row | Used in 1 project | = | fact | default · filters | product |  |  |
| My library | Items › Row | postgres-mcp | = | item name | default · filters | user |  |  |
| My library | Items › Row | mcp | = | kind badge | default · filters | product |  |  |
| My library | Items › Row | Read-only Postgres access for the agent: schema, explain plans, sample rows. | = | description | default · filters | user |  |  |
| My library | Items › Row | `modelcontextprotocol/servers-archived` @ `9be4674` · MIT | = | fact | default · filters | user |  |  |
| My library | Items › Row | Needs `DATABASE_URL` | = | fact | default · filters | product, with slots |  |  |
| My library | Items › Row | Used in 2 projects · 1 item requires this | = | fact | default · filters | product |  |  |
| My library | Items › Row | github-mcp | = | item name | default · filters | user |  |  |
| My library | Items › Row | Shared | = | state badge | default · filters | product |  |  |
| My library | Items › Row | Issues, pull requests and code search on GitHub, through GitHub’s own server. | = | description | default · filters | user |  |  |
| My library | Items › Row | `github/github-mcp-server` @ `v0.9.0` · MIT | = | fact | default · filters | user |  |  |
| My library | Items › Row | Needs `GITHUB_TOKEN` | = | fact | default · filters | product, with slots |  |  |
| My library | Items › Row | Used in 3 projects · copied from the Public library | = | fact | default · filters | product |  |  |
| My library | Items › Row | pr-reviewer | = | item name | default · filters | user |  |  |
| My library | Items › Row | Reads a pull request diff and leaves review comments the way I would write them. | = | description | default · filters | user | U1 |  |
| My library | Items › Row | .claude/agents/pr-reviewer.md | = | fact | default · filters | user |  |  |
| My library | Items › Row | Used in 2 projects · detached in 1 | = | fact | default · filters | product | D8 |  |
| My library | Items › Row | commit-conventions | = | item name | default · filters | user |  |  |
| My library | Items › Row | prompt | = | kind badge | default · filters | product |  |  |
| My library | Items › Row | Conventional commits, imperative mood, and a body that says why rather than what. | = | description | default · filters | user |  |  |
| My library | Items › Row | `CLAUDE.md`, appended | = | fact | default · filters | product, with slots |  |  |
| My library | Items › Row | Used in 4 projects · last exported 2 days ago | = | fact | default · filters | product |  |  |
| My library | Items › Row | writing-style | = | item name | default · filters | user |  |  |
| My library | Items › Row | Plain English for docs: short sentences, no marketing words, an example before every rule. | = | description | default · filters | user |  |  |
| My library | Items › Row | link-checker | = | item name | default · filters | user |  |  |
| My library | Items › Row | Crawls the built docs and lists every broken internal and external link, with the page it is on. | = | description | default · filters | user |  |  |
| My library | Items › Row | scripts/check-links.mjs | = | fact | default · filters | user |  |  |
| My library | Items › Row | whisper | = | item name | default · filters | user |  |  |
| My library | Items › Row | app | = | kind badge | default · filters | product |  |  |
| My library | Items › Row | Speech-to-text, run locally on voice memos before they are summarised. | = | description | default · filters | user |  |  |
| My library | Items › Row | `openai/whisper` @ `v20240930` · MIT | = | fact | default · filters | user |  |  |
| My library | Items › Row | Used in 1 project · last exported 3 weeks ago | = | fact | default · filters | product |  |  |
| My library | Main › State block | Your library is empty | **No items in My library yet** | a11y label | empty | product | D1 | D13, D1 |
| My library | Main › State block | Your library is empty | **No items in My library yet** | heading | empty | product | D1 D13 | D13, D1 |
| My library | Main › State block | This is where your own skills, agents, prompts, MCP servers, scripts and apps live — the pieces every project is built from. Add the first one, bring in a library you exported before, or start from items we have checked. | **My library holds your own skills, agents, prompts, MCP servers, scripts and apps. Add the first one, import a library you exported before, or copy from the Public library.** | state message | empty | product | D1 D2 V1 V2 | D1, D2, V1, D5 |
| My library | Main › State block | Add item | = | button | empty | product |  |  |
| My library | Main › State block | Import JSON | = | button | empty | product |  |  |
| My library | Main › State block | Explore Public library | **Open Public library** | button | empty | product |  | Button: plain verb |
| My library | Main › Find | terraform | = | value | error-filtered | user |  |  |
| My library | Main › Kind | All 0 | = | nav | error-filtered | product |  |  |
| My library | Main › Kind | skill 0 | = | nav | error-filtered | product |  |  |
| My library | Main › Kind | agent 0 | = | nav | error-filtered | product |  |  |
| My library | Main › Kind | prompt 0 | = | nav | error-filtered | product |  |  |
| My library | Main › Kind | mcp 0 | = | nav | error-filtered | product |  |  |
| My library | Main › Kind | script 0 | = | nav | error-filtered | product |  |  |
| My library | Main › Kind | app 0 | = | nav | error-filtered | product |  |  |
| My library | Main › State block | No items match | **Nothing matches “terraform”** | a11y label | error-filtered | product |  | D13 |
| My library | Main › State block | No items match | **Nothing matches “terraform”** | heading | error-filtered | product | D13 | D13 |
| My library | Main › State block | Nothing matches “terraform” among your agents. You have 10 items — the search hides all of them in this tab. | **The tab shows only agents. You have 11 items — the search hides all of them in this tab.** | state message | error-filtered | product | U3 | U3; Step 7 #8 filtered body, one form |
| My library | Main › State block | Clear search · show All | **Clear search** | button | error-filtered | product | D14 | D14 |
| My library | Main › State block | Add “terraform” as a new item | = | button | error-filtered | product |  |  |
| My library | Main › State block | Your library didn’t load | **My library didn’t load** | a11y label | error-server | product | D1 | D1 |
| My library | Main › State block | Your library didn’t load | **My library didn’t load** | heading | error-server | product | D1 | D1 |
| My library | Main › State block | The server did not answer, so your items can’t be shown right now. | **Our server didn’t answer, so My library can’t be shown right now. Nothing in it changed.** | state message | error-server | product | D1 D9 T2 | D9, T2, D1; Error: what did not change |
| My library | Main › State block | 503 · Service unavailable · 14:02 | = | state message | error-server | product | D10 |  |
| My library | Main › State block | Try again | **Load again** | button | error-server | product | D12 | D12 |
| My library | Main › State block | Open Projects | = | button | error-server | product |  |  |
| My library | Main › Find | Filters · 1 | = | button | filters | product |  |  |
| My library | Popover: Filters › Form | Filters | = | heading | filters | product |  |  |
| My library | Popover: Filters › Form | Reset filters | **Clear filters** | button | filters | product | D14 | D14 |
| My library | Popover: Filters › Form | Use | = | field label | filters | product |  |  |
| My library | Popover: Filters › Form | Any | = | option | filters | product |  |  |
| My library | Popover: Filters › Form | In at least one project | = | option | filters | product |  |  |
| My library | Popover: Filters › Form | In no project | = | option | filters | product |  |  |
| My library | Popover: Filters › Form | Made of | = | field label | filters | product |  |  |
| My library | Popover: Filters › Form | Content written here | = | option | filters | product |  |  |
| My library | Popover: Filters › Form | Files from my computer | **Files from your computer** | option | filters | product |  | Dictionary: my only inside My library |
| My library | Popover: Filters › Form | A pinned repo | = | option | filters | product |  |  |
| My library | Popover: Filters › Form | Needs | = | field label | filters | product |  |  |
| My library | Popover: Filters › Form | Env keys | = | option | filters | product |  |  |
| My library | Popover: Filters › Form | Other items (requires) | = | option | filters | product |  |  |
| My library | Popover: Filters › Form | An outside rule (defers to) | = | option | filters | product |  |  |
| My library | Popover: Filters › Form | Tags | = | field label | filters | product |  |  |
| My library | Popover: Filters › Form | postgres | = | option | filters | user |  |  |
| My library | Popover: Filters › Form | migrations | = | option | filters | user |  |  |
| My library | Popover: Filters › Form | review | = | option | filters | user |  |  |
| My library | Popover: Filters › Form | docs | = | option | filters | user |  |  |
| My library | Popover: Filters › Form | typescript | = | option | filters | user |  |  |
| My library | Popover: Filters › Form | Sharing | = | field label | filters | product |  |  |
| My library | Popover: Filters › Form | Only items shared by link | = | option | filters | product |  |  |
| My library | Popover: Filters › Form | Sort by | = | field label | filters | product |  |  |
| My library | Popover: Filters › Form | Name | = | option | filters | product |  |  |
| My library | Popover: Filters › Form | Last changed | = | option | filters | product |  |  |
| My library | Popover: Filters › Form | Most used | = | option | filters | product |  |  |
| My library | Popover: Filters › Form | Cancel | = | button | filters | product | D16 |  |
| My library | Popover: Filters › Form | Apply | = | button | filters | product |  |  |
| My library | Main › Kind | All | = | nav | loading | product |  |  |
| My library | Main › Kind | skill | = | nav | loading | product |  |  |
| My library | Main › Kind | agent | = | nav | loading | product |  |  |
| My library | Main › Kind | prompt | = | nav | loading | product |  |  |
| My library | Main › Kind | mcp | = | nav | loading | product |  |  |
| My library | Main › Kind | script | = | nav | loading | product |  |  |
| My library | Main › Kind | app | = | nav | loading | product |  |  |
| My library | Main › Items | Loading your library | **Loading My library** | body | loading | product | D1 D11 | D11, D1 |

### Item — the add/edit overlay

State pages: `default` · `delete` · `empty` · `error` · `loading`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Item — the add/edit overlay | Main › Page head | My library | = | title | all | product |  |  |
| Item — the add/edit overlay | Main › Page head | Import JSON | = | button | all | product |  |  |
| Item — the add/edit overlay | Main › Page head | Export JSON | = | button | all | product |  |  |
| Item — the add/edit overlay | Main › Page head | Add item | = | button | all | product |  |  |
| Item — the add/edit overlay | Main › Find | Find | = | a11y label | all | product |  |  |
| Item — the add/edit overlay | Main › Find | Search your items by name, description or tag — migrate, GITHUB_TOKEN, review | **Search My library — migrate, GITHUB_TOKEN, review** | placeholder | all | product | D1 D15 | D1, D15 |
| Item — the add/edit overlay | Main › Find | Filters | = | button | all | product |  |  |
| Item — the add/edit overlay | Main › Kind | Kind | = | a11y label | all | product |  |  |
| Item — the add/edit overlay | Main › Kind | All 11 | = | nav | all | product |  |  |
| Item — the add/edit overlay | Main › Kind | skill 1 | = | nav | all | product |  |  |
| Item — the add/edit overlay | Main › Kind | agent 2 | = | nav | all | product |  |  |
| Item — the add/edit overlay | Main › Kind | prompt 2 | = | nav | all | product |  |  |
| Item — the add/edit overlay | Main › Kind | mcp 2 | = | nav | all | product |  |  |
| Item — the add/edit overlay | Main › Kind | script 3 | = | nav | all | product |  |  |
| Item — the add/edit overlay | Main › Kind | app 1 | = | nav | all | product |  |  |
| Item — the add/edit overlay | Main › Items | Items | = | a11y label | all | product |  |  |
| Item — the add/edit overlay | Items › Row | code-style | = | item name | all | user |  |  |
| Item — the add/edit overlay | Items › Row | skill | = | kind badge | all | product |  |  |
| Item — the add/edit overlay | Items › Row | How I want TypeScript written: naming, imports, error handling, no default exports. | = | description | all | user |  |  |
| Item — the add/edit overlay | Items › Row | .claude/skills/code-style/SKILL.md | = | fact | all | user |  |  |
| Item — the add/edit overlay | Items › Row | Defers to the client’s ESLint config | = | fact | all | product, with slots |  |  |
| Item — the add/edit overlay | Items › Row | Used in 3 projects · last exported 2 days ago | = | fact | all | product |  |  |
| Item — the add/edit overlay | Items › Row | Edit | = | button | all | product |  |  |
| Item — the add/edit overlay | Items › Row | Export | **Export…** | button | all | product | D4 | D3, Q36 |
| Item — the add/edit overlay | Items › Row | Share | **Share…** | button | all | product | D20 D21 | D20, D21 |
| Item — the add/edit overlay | Items › Row | db-migrate | = | item name | all | user |  |  |
| Item — the add/edit overlay | Items › Row | script | = | kind badge | all | product |  |  |
| Item — the add/edit overlay | Items › Row | Generates a Postgres migration from a schema diff and runs it — dry run first, then for real. | = | description | all | user |  |  |
| Item — the add/edit overlay | Items › Row | `scripts/db-migrate.sh` + 2 files | = | fact | all | product, with slots |  |  |
| Item — the add/edit overlay | Items › Row | Used in 3 projects · 1 item requires this · requires `seed-data` · last exported 12 days ago | = | fact | all | product, with slots |  |  |
| Item — the add/edit overlay | Items › Row | seed-data | = | item name | all | user |  |  |
| Item — the add/edit overlay | Items › Row | Loads a small, realistic dataset into a fresh database. | = | description | all | user |  |  |
| Item — the add/edit overlay | Items › Row | scripts/seed-data.sh | = | fact | all | user |  |  |
| Item — the add/edit overlay | Items › Row | Used in 3 projects · 1 item requires this | = | fact | all | product |  |  |
| Item — the add/edit overlay | Items › Row | migration-reviewer | = | item name | all | user |  |  |
| Item — the add/edit overlay | Items › Row | agent | = | kind badge | all | product |  |  |
| Item — the add/edit overlay | Items › Row | Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills. | = | description | all | user |  |  |
| Item — the add/edit overlay | Items › Row | requires `db-migrate`, `postgres-mcp` | = | fact | all | product, with slots |  |  |
| Item — the add/edit overlay | Items › Row | Used in 1 project | = | fact | all | product |  |  |
| Item — the add/edit overlay | Items › Row | postgres-mcp | = | item name | all | user |  |  |
| Item — the add/edit overlay | Items › Row | mcp | = | kind badge | all | product |  |  |
| Item — the add/edit overlay | Items › Row | Read-only Postgres access for the agent: schema, explain plans, sample rows. | = | description | all | user |  |  |
| Item — the add/edit overlay | Items › Row | `modelcontextprotocol/servers-archived` @ `9be4674` · MIT | = | fact | all | user |  |  |
| Item — the add/edit overlay | Items › Row | Needs `DATABASE_URL` | = | fact | all | product, with slots |  |  |
| Item — the add/edit overlay | Items › Row | Used in 2 projects · 1 item requires this | = | fact | all | product |  |  |
| Item — the add/edit overlay | Items › Row | github-mcp | = | item name | all | user |  |  |
| Item — the add/edit overlay | Items › Row | Shared | = | state badge | all | product |  |  |
| Item — the add/edit overlay | Items › Row | Issues, pull requests and code search on GitHub, through GitHub’s own server. | = | description | all | user |  |  |
| Item — the add/edit overlay | Items › Row | `github/github-mcp-server` @ `v0.9.0` · MIT | = | fact | all | user |  |  |
| Item — the add/edit overlay | Items › Row | Needs `GITHUB_TOKEN` | = | fact | all | product, with slots |  |  |
| Item — the add/edit overlay | Items › Row | Used in 3 projects · copied from the Public library | = | fact | all | product |  |  |
| Item — the add/edit overlay | Items › Row | pr-reviewer | = | item name | all | user |  |  |
| Item — the add/edit overlay | Items › Row | Reads a pull request diff and leaves review comments the way I would write them. | = | description | all | user | U1 |  |
| Item — the add/edit overlay | Items › Row | .claude/agents/pr-reviewer.md | = | fact | all | user |  |  |
| Item — the add/edit overlay | Items › Row | Used in 2 projects · detached in 1 | = | fact | all | product | D8 |  |
| Item — the add/edit overlay | Items › Row | commit-conventions | = | item name | all | user |  |  |
| Item — the add/edit overlay | Items › Row | prompt | = | kind badge | all | product |  |  |
| Item — the add/edit overlay | Items › Row | Conventional commits, imperative mood, and a body that says why rather than what. | = | description | all | user |  |  |
| Item — the add/edit overlay | Items › Row | `CLAUDE.md`, appended | = | fact | all | product, with slots |  |  |
| Item — the add/edit overlay | Items › Row | Used in 4 projects · last exported 2 days ago | = | fact | all | product |  |  |
| Item — the add/edit overlay | Items › Row | writing-style | = | item name | all | user |  |  |
| Item — the add/edit overlay | Items › Row | Plain English for docs: short sentences, no marketing words, an example before every rule. | = | description | all | user |  |  |
| Item — the add/edit overlay | Items › Row | link-checker | = | item name | all | user |  |  |
| Item — the add/edit overlay | Items › Row | Crawls the built docs and lists every broken internal and external link, with the page it is on. | = | description | all | user |  |  |
| Item — the add/edit overlay | Items › Row | scripts/check-links.mjs | = | fact | all | user |  |  |
| Item — the add/edit overlay | Items › Row | whisper | = | item name | all | user |  |  |
| Item — the add/edit overlay | Items › Row | app | = | kind badge | all | product |  |  |
| Item — the add/edit overlay | Items › Row | Speech-to-text, run locally on voice memos before they are summarised. | = | description | all | user |  |  |
| Item — the add/edit overlay | Items › Row | `openai/whisper` @ `v20240930` · MIT | = | fact | all | user |  |  |
| Item — the add/edit overlay | Items › Row | Used in 1 project · last exported 3 weeks ago | = | fact | all | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Edit db-migrate | = | heading | default · delete · error · loading | product, with slots |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Close | = | a11y label | default · delete · error · loading | product | D16 |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Finding | Used in 3 projects · saving un-checks all three | = | status label | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Finding | acme-billing-api · agent-dotfiles · docs-site-rewrite. 1 item requires this: `migration-reviewer`. It requires `seed-data`. | **acme-billing-api · agent-dotfiles · docs-site-rewrite. 1 item requires this: `migration-reviewer`. This one requires `seed-data`.** | state message | default · delete · error | product, with slots |  | Principle 4: name which item |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Name | = | field label | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | release-notes | = | placeholder | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | db-migrate | = | value | default · delete · error | user |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Kind | = | field label | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | skill | = | option | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | agent | = | option | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | prompt | = | option | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | mcp | = | option | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | script | = | option | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | app | = | option | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Description | = | field label | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | One line: what it does and when it is used | = | placeholder | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Generates a Postgres migration from a schema diff and runs it — dry run first, then for real. | = | value | default · delete · error | user |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Tags | = | field label | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | postgres, review | = | placeholder | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | postgres, migrations | = | value | default · delete · error | user |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Contents | = | heading | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Content | = | field label | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Write or paste it here | = | placeholder | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Files | = | body | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | templates/create_table.sql | = | body | default · delete · error | user |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | 1.2 KB | = | fact | default · delete · error | user |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Remove | = | button | default · delete · error | product | D22 |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | templates/add_column.sql | = | body | default · delete · error | user |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | 0.8 KB | = | fact | default · delete · error | user |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Drop files or a folder here | = | body | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | or choose from your computer · a dropped SKILL.md also fills the name and kind | = | field hint | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Repository | = | body | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Attach a repo | = | button | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Cloned at a pinned commit or tag when the archive is set up — never copied into it | = | field hint | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Dependencies | = | heading | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Requires | = | field label | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Items this one needs — postgres-mcp | **Items this one requires — postgres-mcp** | placeholder | default · delete · error | product |  | Dictionary: needs is for env keys only |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | seed-data | = | value | default · delete · error | user |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Pulled into every project that holds this one | **Auto-added to every project that holds this one** | field hint | default · delete · error | product | D7 | D7 |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Conflicts with | = | field label | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Items it must not travel with | **Items that clash with this one in a project — eslint-autofix** | placeholder | default · delete · error | product |  | Nothing blocks: must not promises enforcement |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Env keys it needs | = | field label | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | GITHUB_TOKEN | = | placeholder | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | DATABASE_URL | = | value | default · delete · error | user |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Names only. Values never live here. | = | field hint | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Defers to | = | field label | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | the client’s ESLint config | = | placeholder | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Where they disagree, that wins | **Where they disagree, that wins. We don’t compare the two — every check, shared page and SETUP.md repeats this line.** | field hint | default · delete · error | product |  | Principle 3; CLAUDE.md §5 Deference |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Lands at | = | field label | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | .claude/skills/release-notes/SKILL.md | = | placeholder | default · delete · error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | scripts/db-migrate.sh | = | value | default · delete · error | user |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Delete item… | = | button | default · delete · error | product | D20 |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Cancel | = | button | default · delete · error | product | D16 |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Form | Save | = | button | default · delete · error | product |  |  |
| Item — the add/edit overlay | Modal: Delete db-migrate? | Delete db-migrate? | = | heading | delete | product, with slots |  |  |
| Item — the add/edit overlay | Modal: Delete db-migrate? | `db-migrate` is used in 3 projects. Deleting it may stop them working. | = | body | delete | product, with slots |  |  |
| Item — the add/edit overlay | Modal: Delete db-migrate? | acme-billing-api · agent-dotfiles · docs-site-rewrite | = | body | delete | user |  |  |
| Item — the add/edit overlay | Modal: Delete db-migrate? | `migration-reviewer` requires it; that requirement will point at nothing, and the next check in each project names it as a Problem. | **`migration-reviewer` requires it, so that requirement will point at nothing, and the next check in acme-billing-api names it as a Problem.** | body | delete | product, with slots |  | Dangerous action example; Step 7 #12 claim only what is known |
| Item — the add/edit overlay | Modal: Delete db-migrate? | This can’t be undone. | = | fact | delete | product |  |  |
| Item — the add/edit overlay | Modal: Delete db-migrate? | Cancel | = | button | delete | product | D16 |  |
| Item — the add/edit overlay | Modal: Delete db-migrate? | Delete | = | button | delete | product |  |  |
| Item — the add/edit overlay | Sheet: Add item | Add item | = | heading | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item | Close | = | a11y label | empty | product | D16 |  |
| Item — the add/edit overlay | Sheet: Add item › Finding | Before you add it | = | status label | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Finding | Check that these files carry no keys. We don’t read your files looking for secrets. What you add here is stored on our server, goes out in every archive built from it, and — if you ever share it — onto a link anyone can open. | = | state message | empty | product | D9 |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Name | = | field label | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | release-notes | = | placeholder | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Kind | = | field label | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | skill | = | option | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | agent | = | option | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | prompt | = | option | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | mcp | = | option | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | script | = | option | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | app | = | option | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Description | = | field label | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | One line: what it does and when it is used | = | placeholder | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Tags | = | field label | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | postgres, review | = | placeholder | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Contents | = | heading | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Content | = | field label | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Write or paste it here | = | placeholder | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Files | = | body | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Drop files or a folder here | = | body | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | or choose from your computer · a dropped SKILL.md also fills the name and kind | = | field hint | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Repository | = | body | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Attach a repo | = | button | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Cloned at a pinned commit or tag when the archive is set up — never copied into it | = | field hint | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Dependencies | = | heading | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Requires | = | field label | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Items this one needs — postgres-mcp | **Items this one requires — postgres-mcp** | placeholder | empty | product |  | Dictionary: needs is for env keys only |
| Item — the add/edit overlay | Sheet: Add item › Form | Pulled into every project that holds this one | **Auto-added to every project that holds this one** | field hint | empty | product | D7 | D7 |
| Item — the add/edit overlay | Sheet: Add item › Form | Conflicts with | = | field label | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Items it must not travel with | **Items that clash with this one in a project — eslint-autofix** | placeholder | empty | product |  | Nothing blocks: must not promises enforcement |
| Item — the add/edit overlay | Sheet: Add item › Form | Env keys it needs | = | field label | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | GITHUB_TOKEN | = | placeholder | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Names only. Values never live here. | = | field hint | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Defers to | = | field label | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | the client’s ESLint config | = | placeholder | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Where they disagree, that wins | **Where they disagree, that wins. We don’t compare the two — every check, shared page and SETUP.md repeats this line.** | field hint | empty | product |  | Principle 3; CLAUDE.md §5 Deference |
| Item — the add/edit overlay | Sheet: Add item › Form | Lands at | = | field label | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | .claude/skills/release-notes/SKILL.md | = | placeholder | empty | product |  |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Cancel | = | button | empty | product | D16 |  |
| Item — the add/edit overlay | Sheet: Add item › Form | Add to My library | = | button | empty | product | D5 |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Finding | Your edit didn’t land | = | status label | error | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Finding | The server didn’t confirm the save, so `db-migrate` is shown as it was. Your changes are still in this form. Until a save goes through, acme-billing-api, agent-dotfiles and docs-site-rewrite show no verdict. | **Our server didn’t confirm the save, so `db-migrate` is shown as it was. Your changes are still in this form. Until a save goes through, acme-billing-api, agent-dotfiles and docs-site-rewrite show no verdict.** | state message | error | product, with slots | D9 | D9 |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Finding | (added) | **503 · Service unavailable · 14:11** | state message | error | product |  | Step 7 #18/#19: the error code on its own line (D10) |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Finding | Save again | = | button | error | product | D12 |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate › Finding | Discard changes | = | button | error | product | D16 |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Opening db-migrate | **Loading db-migrate** | body | loading | product, with slots | D11 | D11 |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Name | = | body | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Kind | = | body | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Description | = | body | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Tags | = | body | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Contents | = | heading | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Content | = | body | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Files | = | body | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Repository | = | body | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Dependencies | = | heading | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Requires | = | body | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Conflicts with | = | body | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Env keys it needs | = | body | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Defers to | = | body | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Lands at | = | body | loading | product |  |  |
| Item — the add/edit overlay | Sheet: Edit db-migrate | Cancel | = | button | loading | product | D16 |  |

### Library — import and export as JSON

State pages: `default` · `error` · `loading` · `success`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Library — import and export as JSON | Main › Page head | My library | = | title | all | product |  |  |
| Library — import and export as JSON | Main › Page head | Import JSON | = | button | all | product |  |  |
| Library — import and export as JSON | Main › Page head | Export JSON | = | button | all | product |  |  |
| Library — import and export as JSON | Main › Page head | Add item | = | button | all | product |  |  |
| Library — import and export as JSON | Main › Find | Find | = | a11y label | all | product |  |  |
| Library — import and export as JSON | Main › Find | Search your items by name, description or tag — migrate, GITHUB_TOKEN, review | **Search My library — migrate, GITHUB_TOKEN, review** | placeholder | all | product | D1 D15 | D15, D1 |
| Library — import and export as JSON | Main › Find | Filters | = | button | all | product |  |  |
| Library — import and export as JSON | Main › Kind | Kind | = | a11y label | all | product |  |  |
| Library — import and export as JSON | Main › Kind | All 11 | = | nav | all | product |  |  |
| Library — import and export as JSON | Main › Kind | skill 1 | = | nav | all | product |  |  |
| Library — import and export as JSON | Main › Kind | agent 2 | = | nav | all | product |  |  |
| Library — import and export as JSON | Main › Kind | prompt 2 | = | nav | all | product |  |  |
| Library — import and export as JSON | Main › Kind | mcp 2 | = | nav | all | product |  |  |
| Library — import and export as JSON | Main › Kind | script 3 | = | nav | all | product |  |  |
| Library — import and export as JSON | Main › Kind | app 1 | = | nav | all | product |  |  |
| Library — import and export as JSON | Main › Items | Items | = | a11y label | all | product |  |  |
| Library — import and export as JSON | Items › Row | code-style | = | item name | all | user |  |  |
| Library — import and export as JSON | Items › Row | skill | = | kind badge | all | product |  |  |
| Library — import and export as JSON | Items › Row | How I want TypeScript written: naming, imports, error handling, no default exports. | = | description | all | user |  |  |
| Library — import and export as JSON | Items › Row | .claude/skills/code-style/SKILL.md | = | fact | all | user |  |  |
| Library — import and export as JSON | Items › Row | Defers to the client’s ESLint config | = | fact | all | product, with slots |  |  |
| Library — import and export as JSON | Items › Row | Used in 3 projects · last exported 2 days ago | = | fact | all | product |  |  |
| Library — import and export as JSON | Items › Row | Edit | = | button | all | product |  |  |
| Library — import and export as JSON | Items › Row | Export | **Export…** | button | all | product | D4 | D3, Q36, D20 |
| Library — import and export as JSON | Items › Row | Share | **Share…** | button | all | product | D20 D21 | D21, D20 |
| Library — import and export as JSON | Items › Row | db-migrate | = | item name | all | user |  |  |
| Library — import and export as JSON | Items › Row | script | = | kind badge | all | product |  |  |
| Library — import and export as JSON | Items › Row | Generates a Postgres migration from a schema diff and runs it — dry run first, then for real. | = | description | all | user |  |  |
| Library — import and export as JSON | Items › Row | `scripts/db-migrate.sh` + 2 files | = | fact | all | product, with slots |  |  |
| Library — import and export as JSON | Items › Row | Used in 3 projects · 1 item requires this · requires `seed-data` · last exported 12 days ago | = | fact | all | product, with slots |  |  |
| Library — import and export as JSON | Items › Row | seed-data | = | item name | all | user |  |  |
| Library — import and export as JSON | Items › Row | Loads a small, realistic dataset into a fresh database. | = | description | all | user |  |  |
| Library — import and export as JSON | Items › Row | scripts/seed-data.sh | = | fact | all | user |  |  |
| Library — import and export as JSON | Items › Row | Used in 3 projects · 1 item requires this | = | fact | all | product |  |  |
| Library — import and export as JSON | Items › Row | migration-reviewer | = | item name | all | user |  |  |
| Library — import and export as JSON | Items › Row | agent | = | kind badge | all | product |  |  |
| Library — import and export as JSON | Items › Row | Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills. | = | description | all | user |  |  |
| Library — import and export as JSON | Items › Row | requires `db-migrate`, `postgres-mcp` | = | fact | all | product, with slots |  |  |
| Library — import and export as JSON | Items › Row | Used in 1 project | = | fact | all | product |  |  |
| Library — import and export as JSON | Items › Row | postgres-mcp | = | item name | all | user |  |  |
| Library — import and export as JSON | Items › Row | mcp | = | kind badge | all | product |  |  |
| Library — import and export as JSON | Items › Row | Read-only Postgres access for the agent: schema, explain plans, sample rows. | = | description | all | user |  |  |
| Library — import and export as JSON | Items › Row | `modelcontextprotocol/servers-archived` @ `9be4674` · MIT | = | fact | all | user |  |  |
| Library — import and export as JSON | Items › Row | Needs `DATABASE_URL` | = | fact | all | product, with slots |  |  |
| Library — import and export as JSON | Items › Row | Used in 2 projects · 1 item requires this | = | fact | all | product |  |  |
| Library — import and export as JSON | Items › Row | github-mcp | = | item name | all | user |  |  |
| Library — import and export as JSON | Items › Row | Shared | = | state badge | all | product |  |  |
| Library — import and export as JSON | Items › Row | Issues, pull requests and code search on GitHub, through GitHub’s own server. | = | description | all | user |  |  |
| Library — import and export as JSON | Items › Row | `github/github-mcp-server` @ `v0.9.0` · MIT | = | fact | all | user |  |  |
| Library — import and export as JSON | Items › Row | Needs `GITHUB_TOKEN` | = | fact | all | product, with slots |  |  |
| Library — import and export as JSON | Items › Row | Used in 3 projects · copied from the Public library | = | fact | all | product |  |  |
| Library — import and export as JSON | Items › Row | pr-reviewer | = | item name | all | user |  |  |
| Library — import and export as JSON | Items › Row | Reads a pull request diff and leaves review comments the way I would write them. | = | description | all | user | U1 |  |
| Library — import and export as JSON | Items › Row | .claude/agents/pr-reviewer.md | = | fact | all | user |  |  |
| Library — import and export as JSON | Items › Row | Used in 2 projects · detached in 1 | = | fact | all | product | D8 |  |
| Library — import and export as JSON | Items › Row | commit-conventions | = | item name | all | user |  |  |
| Library — import and export as JSON | Items › Row | prompt | = | kind badge | all | product |  |  |
| Library — import and export as JSON | Items › Row | Conventional commits, imperative mood, and a body that says why rather than what. | = | description | all | user |  |  |
| Library — import and export as JSON | Items › Row | `CLAUDE.md`, appended | = | fact | all | product, with slots |  |  |
| Library — import and export as JSON | Items › Row | Used in 4 projects · last exported 2 days ago | = | fact | all | product |  |  |
| Library — import and export as JSON | Items › Row | writing-style | = | item name | all | user |  |  |
| Library — import and export as JSON | Items › Row | Plain English for docs: short sentences, no marketing words, an example before every rule. | = | description | all | user |  |  |
| Library — import and export as JSON | Items › Row | link-checker | = | item name | all | user |  |  |
| Library — import and export as JSON | Items › Row | Crawls the built docs and lists every broken internal and external link, with the page it is on. | = | description | all | user |  |  |
| Library — import and export as JSON | Items › Row | scripts/check-links.mjs | = | fact | all | user |  |  |
| Library — import and export as JSON | Items › Row | whisper | = | item name | all | user |  |  |
| Library — import and export as JSON | Items › Row | app | = | kind badge | all | product |  |  |
| Library — import and export as JSON | Items › Row | Speech-to-text, run locally on voice memos before they are summarised. | = | description | all | user |  |  |
| Library — import and export as JSON | Items › Row | `openai/whisper` @ `v20240930` · MIT | = | fact | all | user |  |  |
| Library — import and export as JSON | Items › Row | Used in 1 project · last exported 3 weeks ago | = | fact | all | product |  |  |
| Library — import and export as JSON | Modal: Import a library | Import a library | = | heading | default | product | D1 |  |
| Library — import and export as JSON | Modal: Import a library | Close | = | a11y label | default | product | D16 |  |
| Library — import and export as JSON | Modal: Import a library | maya-library-2026-09.json · 47 items · 212 KB | = | body | default | product, with slots | D1 |  |
| Library — import and export as JSON | Modal: Import a library | 31 skills · 6 agents · 5 prompts · 3 MCP servers · 2 scripts. They are added to My library beside the 10 you have. | **31 skills · 6 agents · 5 prompts · 3 MCP servers · 2 scripts. They are added to My library beside the 11 you have.** | fact | default | product | U3 V2 | U3 |
| Library — import and export as JSON | Modal: Import a library › Finding | Before you import it | = | status label | default | product |  |  |
| Library — import and export as JSON | Modal: Import a library › Finding | Check that these files carry no keys. We don’t read your files looking for secrets. What you import is stored on our server, goes out in every archive built from it, and — if you ever share it — onto a link anyone can open. | = | state message | default | product | D9 |  |
| Library — import and export as JSON | Modal: Import a library | Choose another file | = | button | default | product |  |  |
| Library — import and export as JSON | Modal: Import a library | Cancel | = | button | default | product | D16 |  |
| Library — import and export as JSON | Modal: Import a library | Import 47 items | = | button | default | product |  |  |
| Library — import and export as JSON | Modal: The import didn’t finish | The import didn’t finish | = | heading | error | product |  |  |
| Library — import and export as JSON | Modal: The import didn’t finish | Close | = | a11y label | error | product | D16 |  |
| Library — import and export as JSON | Modal: The import didn’t finish › Finding | Nothing was imported | = | status label | error | product |  |  |
| Library — import and export as JSON | Modal: The import didn’t finish › Finding | The server stopped at item 18 of 47. Your library is as it was before — the 11 items you had, and none of the 47. | **Our server stopped at item 18 of 47. My library is as it was before — the 11 items you had, and none of the 47.** | state message | error | product | D1 D9 | D9, D1 |
| Library — import and export as JSON | Modal: The import didn’t finish | maya-library-2026-09.json · 503 · 14:02 | **maya-library-2026-09.json · 503 · Service unavailable · 14:02** | fact | error | product, with slots | D1 D10 | D10; Step 7 #18/#19: the error code on its own line (D10) |
| Library — import and export as JSON | Modal: The import didn’t finish | Close | = | button | error | product | D16 |  |
| Library — import and export as JSON | Modal: The import didn’t finish | Try the import again | **Import again** | button | error | product | D12 | D12 |
| Library — import and export as JSON | Modal: Importing 47 items | Importing 47 items | = | heading | loading | product |  |  |
| Library — import and export as JSON | Modal: Importing 47 items | Close | = | a11y label | loading | product | D16 |  |
| Library — import and export as JSON | Modal: Importing 47 items | 18 of 47 · `release-notes` | = | body | loading | product, with slots |  |  |
| Library — import and export as JSON | Modal: Importing 47 items | If this stops before the end, your library stays exactly as it was before the import — none of the 47 are kept. | **If this stops before the end, My library stays exactly as it was before the import — none of the 47 are kept.** | fact | loading | product | D1 | D1 |
| Library — import and export as JSON | Modal: Importing 47 items | Cancel import | = | button | loading | product |  |  |
| Library — import and export as JSON | Modal: 47 items imported | 47 items imported | = | heading | success | product |  |  |
| Library — import and export as JSON | Modal: 47 items imported | Close | = | a11y label | success | product | D16 |  |
| Library — import and export as JSON | Modal: 47 items imported | All 47 items from maya-library-2026-09.json are in My library, beside the 11 you had. | = | body | success | product, with slots | D1 |  |
| Library — import and export as JSON | Modal: 47 items imported | None of them are in a project yet. Their `requires` edges came with them; 3 point at items the file did not hold, and the check will name them when it meets them. | **None of them are in a project yet. Their `requires` fields came with them, and 3 point at items the file didn’t hold — a check names each of those as a Problem.** | fact | success | product, with slots | T2 | T2; jargon (edges); Success: the next consequence |
| Library — import and export as JSON | Modal: 47 items imported | Close | = | button | success | product | D16 |  |
| Library — import and export as JSON | Modal: 47 items imported | See the new items | = | button | success | product |  |  |

### Public library

State pages: `default` · `error-filtered` · `error-server` · `filters` · `loading`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Public library | Main › Page head | Public library | = | title | all | product |  |  |
| Public library | Main › Page head | Read-only. Every item is pinned to the version we checked — not the latest one. | = | fact | all | product |  |  |
| Public library | Main › Find | Find | = | a11y label | default · error-filtered · filters · loading | product |  |  |
| Public library | Main › Find | Search the shelf by name, kind or source — filesystem, playwright, anthropics | **Search Public library — filesystem, playwright, anthropics** | placeholder | default · error-filtered · filters · loading | product | D2 D15 | D2, D15 |
| Public library | Main › Find | Filters | = | button | default · error-filtered · loading | product |  |  |
| Public library | Main › Kind | Kind | = | a11y label | default · error-filtered · filters · loading | product |  |  |
| Public library | Main › Kind | All 8 | = | nav | default · filters | product |  |  |
| Public library | Main › Kind | skill 2 | = | nav | default · filters | product |  |  |
| Public library | Main › Kind | agent 0 | = | nav | default · error-filtered · filters | product |  |  |
| Public library | Main › Kind | prompt 0 | = | nav | default · error-filtered · filters | product |  |  |
| Public library | Main › Kind | mcp 6 | = | nav | default · filters | product |  |  |
| Public library | Main › Kind | script 0 | = | nav | default · error-filtered · filters | product |  |  |
| Public library | Main › Kind | app 0 | = | nav | default · error-filtered · filters | product |  |  |
| Public library | Main › Items | Items | = | a11y label | default · filters · loading | product |  |  |
| Public library | Items › Row | filesystem | = | item name | default · filters | user |  |  |
| Public library | Items › Row | mcp | = | kind badge | default · filters | product |  |  |
| Public library | Items › Row | Read and write files inside the directories you allow, and nowhere else. | = | description | default · filters | user |  |  |
| Public library | Items › Row | `modelcontextprotocol/servers` @ `2025.9.25` · MIT | = | fact | default · filters | user |  |  |
| Public library | Items › Row | Copy to My library | = | button | default · filters | product | D5 |  |
| Public library | Items › Row | Export | **Export…** | button | default · filters | product | D4 | D3, Q36, D20 |
| Public library | Items › Row | memory | = | item name | default · filters | user |  |  |
| Public library | Items › Row | A knowledge graph the agent can write to and read back between sessions. | = | description | default · filters | user |  |  |
| Public library | Items › Row | fetch | = | item name | default · filters | user |  |  |
| Public library | Items › Row | Fetches a URL and hands the agent the page as Markdown. | = | description | default · filters | user |  |  |
| Public library | Items › Row | github-mcp-server | = | item name | default · filters | user |  |  |
| Public library | Items › Row | GitHub’s own MCP server: issues, pull requests, Actions and code search. | = | description | default · filters | user |  |  |
| Public library | Items › Row | `github/github-mcp-server` @ `v0.9.0` · MIT | = | fact | default · filters | user |  |  |
| Public library | Items › Row | In My library as `github-mcp` | = | fact | default · filters | product, with slots |  |  |
| Public library | Items › Row | playwright-mcp | = | item name | default · filters | user |  |  |
| Public library | Items › Row | Drives a real browser through the accessibility tree rather than screenshots. | = | description | default · filters | user |  |  |
| Public library | Items › Row | `microsoft/playwright-mcp` @ `v0.0.40` · Apache-2.0 | = | fact | default · filters | user |  |  |
| Public library | Items › Row | context7 | = | item name | default · filters | user |  |  |
| Public library | Items › Row | Pulls current, version-specific library documentation into the prompt. | = | description | default · filters | user |  |  |
| Public library | Items › Row | `upstash/context7` @ `v1.0.20` · MIT | = | fact | default · filters | user |  |  |
| Public library | Items › Row | mcp-builder | = | item name | default · filters | user |  |  |
| Public library | Items › Row | skill | = | kind badge | default · filters | product |  |  |
| Public library | Items › Row | A guide for building an MCP server: tool design, error messages, evaluation. | = | description | default · filters | user |  |  |
| Public library | Items › Row | `anthropics/skills` @ `c74d647` · Apache-2.0 | = | fact | default · filters | user |  |  |
| Public library | Items › Row | webapp-testing | = | item name | default · filters | user | U2 |  |
| Public library | Items › Row | Tests a local web app with Playwright: start the server, drive the page, read the logs. | = | description | default · filters | user |  |  |
| Public library | Main › Find | linear | = | value | error-filtered | user |  |  |
| Public library | Main › Kind | All 0 | = | nav | error-filtered | product |  |  |
| Public library | Main › Kind | skill 0 | = | nav | error-filtered | product |  |  |
| Public library | Main › Kind | mcp 0 | = | nav | error-filtered | product |  |  |
| Public library | Main › State block | No items match | **Nothing matches “linear”** | a11y label | error-filtered | product |  | D13 |
| Public library | Main › State block | No items match | **Nothing matches “linear”** | heading | error-filtered | product | D13 | D13 |
| Public library | Main › State block | Nothing on the shelf matches “linear” among skills. The shelf holds 8 items — the search hides all of them in this tab. | **The tab shows only skills. Public library holds 8 items — the search hides all of them in this tab.** | state message | error-filtered | product | D2 | D2, D13; Step 7 #8 filtered body, one form |
| Public library | Main › State block | Clear search · show All | **Clear search** | button | error-filtered | product | D14 | D14 |
| Public library | Main › State block | Search My library instead | = | button | error-filtered | product |  |  |
| Public library | Main › State block | The Public library didn’t load | **Public library didn’t load** | a11y label | error-server | product |  | D2 |
| Public library | Main › State block | The Public library didn’t load | **Public library didn’t load** | heading | error-server | product |  | D2 |
| Public library | Main › State block | The server did not answer, so the shelf can’t be shown right now. Your own items are not affected. | **Our server didn’t answer, so Public library can’t be shown right now. My library isn’t affected.** | state message | error-server | product | D1 D2 D9 T2 | D9, T2, D2, D1 |
| Public library | Main › State block | 503 · Service unavailable · 14:02 | = | state message | error-server | product | D10 |  |
| Public library | Main › State block | Try again | **Load again** | button | error-server | product | D12 | D12 |
| Public library | Main › State block | Open My library | = | button | error-server | product |  |  |
| Public library | Main › Find | Filters · 1 | = | button | filters | product |  |  |
| Public library | Popover: Filters › Form | Filters | = | heading | filters | product |  |  |
| Public library | Popover: Filters › Form | Reset filters | **Clear filters** | button | filters | product | D14 | D14 |
| Public library | Popover: Filters › Form | Source | = | field label | filters | product |  |  |
| Public library | Popover: Filters › Form | anthropics/skills | = | option | filters | user |  |  |
| Public library | Popover: Filters › Form | modelcontextprotocol/servers | = | option | filters | user |  |  |
| Public library | Popover: Filters › Form | github/github-mcp-server | = | option | filters | user |  |  |
| Public library | Popover: Filters › Form | microsoft/playwright-mcp | = | option | filters | user |  |  |
| Public library | Popover: Filters › Form | upstash/context7 | = | option | filters | user |  |  |
| Public library | Popover: Filters › Form | Licence | **License** | field label | filters | product | T3 | T3 |
| Public library | Popover: Filters › Form | MIT | = | option | filters | user |  |  |
| Public library | Popover: Filters › Form | Apache-2.0 | = | option | filters | user |  |  |
| Public library | Popover: Filters › Form | My library | = | field label | filters | product |  |  |
| Public library | Popover: Filters › Form | Hide items I already copied | **Hide items already in My library** | option | filters | product |  | Dictionary: my only inside My library |
| Public library | Popover: Filters › Form | Cancel | = | button | filters | product | D16 |  |
| Public library | Popover: Filters › Form | Apply | = | button | filters | product |  |  |
| Public library | Main › Kind | All | = | nav | loading | product |  |  |
| Public library | Main › Kind | skill | = | nav | loading | product |  |  |
| Public library | Main › Kind | agent | = | nav | loading | product |  |  |
| Public library | Main › Kind | prompt | = | nav | loading | product |  |  |
| Public library | Main › Kind | mcp | = | nav | loading | product |  |  |
| Public library | Main › Kind | script | = | nav | loading | product |  |  |
| Public library | Main › Kind | app | = | nav | loading | product |  |  |
| Public library | Main › Items | Loading the Public library | **Loading Public library** | body | loading | product | D11 | D11 |

### Projects

State pages: `default` · `delete` · `empty` · `error-filtered` · `error-server` · `filters` · `loading`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Projects | Main › Page head | Projects | = | title | all | product |  |  |
| Projects | Main › Page head | New project | = | button | default · delete · error-filtered · error-server · filters · loading | product |  |  |
| Projects | Main › Find projects | Find projects | = | a11y label | default · delete · error-filtered · loading | product |  |  |
| Projects | Find projects › Find | Search projects and the items in them — db-migrate, .mcp.json, acme | **Search projects and their items — db-migrate, .mcp.json, acme** | placeholder | default · delete · error-filtered · loading | product | D15 | D15 |
| Projects | Find projects › Find | Filters | = | button | default · delete · loading | product |  |  |
| Projects | Main › Projects | Projects | = | a11y label | default · delete · filters · loading | product |  |  |
| Projects | Projects › Project card | acme-billing-api | = | item name | default · delete · filters | user |  |  |
| Projects | Projects › Project card | Client repo for Acme's billing service. Code style, migration and review agents, the Postgres and GitHub MCP servers. | **Client repo for Acme’s billing service. Code style, migration and review agents, the Postgres and GitHub MCP servers.** | description | default · delete · filters | user |  | Step 7 #22 typography in sample data |
| Projects | Projects › Project card | 14 items | = | fact | default · delete · filters | product |  |  |
| Projects | Projects › Project card | 3 auto-added | = | fact | default · delete · filters | product | D7 |  |
| Projects | Projects › Project card | 1 detached | = | fact | default · delete · filters | product | D8 |  |
| Projects | Projects › Project card | Last check | = | field label | default · delete · filters | product |  |  |
| Projects | Projects › Project card | Checked 2 days ago · for Claude Code | = | body | default · delete · filters | product | D19 |  |
| Projects | Projects › Project card | 1 problem · 2 notes · 1 skipped | = | fact | default · delete · filters | product |  |  |
| Projects | Projects › Project card | Duplicate | = | button | default · delete · filters | product |  |  |
| Projects | Projects › Project card | Share | **Share…** | button | default · delete · filters | product | D20 D21 | D20, D21 |
| Projects | Projects › Project card | agent-dotfiles | = | item name | default · delete · filters | user |  |  |
| Projects | Projects › Project card | Shared | = | state badge | default · delete · filters | product |  |  |
| Projects | Projects › Project card | My everyday setup across machines: commit conventions, the review subagent, the filesystem and memory MCP servers. | = | description | default · delete · filters | user |  |  |
| Projects | Projects › Project card | 9 items | = | fact | default · delete · filters | product |  |  |
| Projects | Projects › Project card | 2 auto-added | = | fact | default · delete · filters | product | D7 |  |
| Projects | Projects › Project card | Checked 5 days ago · for Claude Code | = | body | default · delete · filters | product | D19 |  |
| Projects | Projects › Project card | Out of date since `code-style` was edited in the Library | **Out of date since `code-style` was edited in My library** | fact | default · delete · filters | product, with slots | D1 | D1 |
| Projects | Projects › Project card | Shared | = | field label | default · delete · filters | product |  |  |
| Projects | Projects › Project card | Anyone with the link sees it as it is now — every edit is visible to them | = | fact | default · delete · filters | product |  |  |
| Projects | Projects › Project card | docs-site-rewrite | = | item name | default · delete · filters | user |  |  |
| Projects | Projects › Project card | Rewriting the product docs in MDX. Writing-style prompt, link checker script, the Context7 and Playwright MCP servers. | = | description | default · delete · filters | user |  |  |
| Projects | Projects › Project card | 11 items | = | fact | default · delete · filters | product |  |  |
| Projects | Projects › Project card | 4 auto-added | = | fact | default · delete · filters | product | D7 |  |
| Projects | Projects › Project card | Checked 3 weeks ago · for Cursor | = | body | default · delete · filters | product | D19 |  |
| Projects | Projects › Project card | 1 problem · 1 note · 0 skipped | = | fact | default · delete · filters | product |  |  |
| Projects | Projects › Project card | voice-notes-pipeline | = | item name | default · delete · filters | user |  |  |
| Projects | Projects › Project card | Transcribe voice memos, summarise them, file them into notes. Whisper as an external app, a summariser prompt, a sorting script. | = | description | default · delete · filters | user |  |  |
| Projects | Projects › Project card | 6 items | = | fact | default · delete · filters | product |  |  |
| Projects | Projects › Project card | 1 auto-added | = | fact | default · delete · filters | product | D7 |  |
| Projects | Projects › Project card | Not checked yet | = | body | default · delete · filters | product |  |  |
| Projects | Projects › Project card | Example | = | state badge | default · delete · filters | product |  |  |
| Projects | Projects › Project card | repo-triage-kit | = | item name | default · delete · filters | user |  |  |
| Projects | Projects › Project card | Built from the Public library to show what a check finds. Two items write to `.mcp.json`, and one needs `GITHUB_TOKEN`. | = | description | default · delete · filters | user |  |  |
| Projects | Projects › Project card | 7 items | = | fact | default · delete · filters | product |  |  |
| Projects | Projects › Project card | all from the Public library | = | fact | default · delete · filters | product |  |  |
| Projects | Projects › Project card | Delete example | **Delete example…** | button | default · delete · filters | product | D20 | D20 |
| Projects | Modal: Delete the example project? | Delete the example project? | **Delete repo-triage-kit?** | heading | delete | product |  | Step 7 #11 dangerous action names the object |
| Projects | Modal: Delete the example project? | `repo-triage-kit` leaves Projects. Its 7 items stay in the Public library, where it came from. | = | body | delete | product, with slots |  |  |
| Projects | Modal: Delete the example project? | This can’t be undone. | = | fact | delete | product |  |  |
| Projects | Modal: Delete the example project? | Cancel | = | button | delete | product | D16 |  |
| Projects | Modal: Delete the example project? | Delete example | = | button | delete | product | D20 |  |
| Projects | Main › State block | No projects yet | = | heading | empty | product | D13 |  |
| Projects | Main › State block | A project is a set of items from your library, checked together and exported as one archive. Start one now, or see what the Public library already holds. | **A project holds items from My library. It is checked as a whole and exported as one archive.** | state message | empty | product | D1 | D6, D1 |
| Projects | Main › State block | Create project | **New project** | button | empty | product |  | one act, one label (the head's New project) |
| Projects | Main › State block | Explore Public library | **Open Public library** | button | empty | product |  | Button: plain verb |
| Projects | Find projects › Find | stripe | = | value | error-filtered | user |  |  |
| Projects | Find projects › Find | Filters · 1 | = | button | error-filtered | product |  |  |
| Projects | Main › State block | No projects match | **Nothing matches “stripe”** | heading | error-filtered | product | D13 | D13 |
| Projects | Main › State block | Nothing matches “stripe” among projects that are Not checked yet. You have 5 projects — the search and the filter hide all of them. | **The filter shows only projects that are Not checked yet. You have 5 projects — the search and the filter hide all of them.** | state message | error-filtered | product |  | D13: the heading carries the match |
| Projects | Main › State block | Clear filters | = | button | error-filtered | product | D14 |  |
| Projects | Main › State block | Projects didn't load | **Projects didn’t load** | heading | error-server | product | T1 | T1 |
| Projects | Main › State block | The server did not answer, so your projects can't be shown right now. | **Our server didn’t answer, so your projects can’t be shown right now. Nothing in them changed.** | state message | error-server | product | D9 T1 T2 | D9, T2, T1; Error: what did not change |
| Projects | Main › State block | 503 · Service unavailable · 14:02 | = | state message | error-server | product | D10 |  |
| Projects | Main › State block | Try again | **Load again** | button | error-server | product | D12 | D12 |
| Projects | Main › State block | Open My library | = | button | error-server | product |  |  |
| Projects | Main › Find | Find projects | = | a11y label | filters | product |  |  |
| Projects | Main › Find | Search projects and the items in them — db-migrate, .mcp.json, acme | **Search projects and their items — db-migrate, .mcp.json, acme** | placeholder | filters | product | D15 | D15 |
| Projects | Main › Find | Filters · 1 | = | button | filters | product |  |  |
| Projects | Popover: Filters › Form | Filters | = | heading | filters | product |  |  |
| Projects | Popover: Filters › Form | Reset filters | **Clear filters** | button | filters | product | D14 | D14 |
| Projects | Popover: Filters › Form | Last check | = | field label | filters | product |  |  |
| Projects | Popover: Filters › Form | Any | = | option | filters | product |  |  |
| Projects | Popover: Filters › Form | Problems at last check | = | option | filters | product |  |  |
| Projects | Popover: Filters › Form | Out of date | = | option | filters | product |  |  |
| Projects | Popover: Filters › Form | Not checked yet | = | option | filters | product |  |  |
| Projects | Popover: Filters › Form | Checked for | = | field label | filters | product | D19 |  |
| Projects | Popover: Filters › Form | Claude Code | = | option | filters | product |  |  |
| Projects | Popover: Filters › Form | Cursor | = | option | filters | product |  |  |
| Projects | Popover: Filters › Form | Codex | = | option | filters | product |  |  |
| Projects | Popover: Filters › Form | Universal | = | option | filters | product |  |  |
| Projects | Popover: Filters › Form | Sharing | = | field label | filters | product |  |  |
| Projects | Popover: Filters › Form | Only projects shared by link | = | option | filters | product |  |  |
| Projects | Popover: Filters › Form | Sort by | = | field label | filters | product |  |  |
| Projects | Popover: Filters › Form | Last changed | = | option | filters | product |  |  |
| Projects | Popover: Filters › Form | Last checked | = | option | filters | product | D19 |  |
| Projects | Popover: Filters › Form | Name | = | option | filters | product |  |  |
| Projects | Popover: Filters › Form | Cancel | = | button | filters | product | D16 |  |
| Projects | Popover: Filters › Form | Apply | = | button | filters | product |  |  |
| Projects | Main › Projects | Loading projects | = | body | loading | product | D11 |  |

### Project

State pages: `default` · `empty` · `error` · `item` · `loading` · `revoke` · `share`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Project | Main | Projects / | = | fact | all | product |  |  |
| Project | Main › Page head | acme-billing-api | = | title | default · error · item · loading · revoke · share | user |  |  |
| Project | Main › Page head | 14 items · 3 auto-added · 1 detached | = | fact | default · item · revoke · share | product | D7 D8 |  |
| Project | Main › Page head | Checked 2 days ago · for Claude Code · 1 problem · 2 notes · 1 skipped | = | fact | default · item · revoke · share | product | D19 |  |
| Project | Main › Page head | Configure | = | button | default · item · loading · revoke · share | product |  |  |
| Project | Main › Page head | Share | **Share…** | button | default · item · loading · share | product | D20 D21 | D20, D21 |
| Project | Main › Page head | Duplicate | = | button | default · item · loading · revoke · share | product |  |  |
| Project | Main › Page head | Check | **Export…** | button | default · empty · item · loading · revoke · share | product |  | Q36: the mode is titled by what it ends in; the check is its sub-process |
| Project | Main | Client repo for Acme’s billing service. Code style, migration and review agents, the Postgres and GitHub MCP servers. | = | description | default · item · revoke · share | user |  |  |
| Project | Main › The set | The set | **Items in this project** | a11y label | default · empty · item · loading · revoke · share | product |  | D6 |
| Project | The set › Set row | code-style | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | skill | = | kind badge | default · item · revoke · share | product |  |  |
| Project | The set › Set row | How I want TypeScript written: naming, imports, error handling. | **How I want TypeScript written: naming, imports, error handling, no default exports.** | description | default · item · revoke · share | user |  | Step 7 #22 U1 |
| Project | The set › Set row | `.claude/skills/code-style/SKILL.md` · defers to the client’s ESLint config | = | fact | default · item · revoke · share | product, with slots |  |  |
| Project | The set › Set row | Note | = | severity | default · item · revoke · share | product |  |  |
| Project | The set › Set row | eslint-autofix | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | script | = | kind badge | default · item · revoke · share | product |  |  |
| Project | The set › Set row | Conflict | = | state badge | default · item · revoke · share | product |  |  |
| Project | The set › Set row | Runs ESLint with --fix on staged files before each commit. | = | description | default · item · revoke · share | user |  |  |
| Project | The set › Set row | `scripts/eslint-autofix.sh` · conflicts with `code-style` | = | fact | default · item · revoke · share | product, with slots |  |  |
| Project | The set › Set row | Problem | = | severity | default · item · revoke · share | product |  |  |
| Project | The set › Set row | migration-reviewer | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | agent | = | kind badge | default · item · revoke · share | product |  |  |
| Project | The set › Set row | Reads a migration before it runs and flags long locks and missing down steps. | **Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills.** | description | default · item · revoke · share | user |  | Step 7 #22 U1 |
| Project | The set › Set row | requires `db-migrate`, `postgres-mcp` · brings 3 items with it | **requires `db-migrate`, `postgres-mcp` · 3 auto-added** | fact | default · item · revoke · share | product, with slots | D7 | D7 |
| Project | Main › The set | Pulled in by migration-reviewer | **Auto-added for migration-reviewer** | a11y label | default · item · revoke · share | product, with slots | D7 | D7 |
| Project | The set › Set row | db-migrate | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | Auto-added | = | state badge | default · item · revoke · share | product | D7 |  |
| Project | The set › Set row | Generates a Postgres migration from a schema diff and runs it, dry run first. | **Generates a Postgres migration from a schema diff and runs it — dry run first, then for real.** | description | default · item · revoke · share | user |  | Step 7 #22 U1 |
| Project | The set › Set row | `scripts/db-migrate.sh` + 2 files · brings 1 item with it | **`scripts/db-migrate.sh` + 2 files · 1 auto-added** | fact | default · item · revoke · share | product, with slots | D7 | D7 |
| Project | Main › The set | Pulled in by db-migrate | **Auto-added for db-migrate** | a11y label | default · item · revoke · share | product, with slots | D7 | D7 |
| Project | The set › Set row | seed-data | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | Loads a small, realistic dataset into a fresh database. | = | description | default · item · revoke · share | user |  |  |
| Project | The set › Set row | scripts/seed-data.sh | = | fact | default · item · revoke · share | user |  |  |
| Project | The set › Set row | postgres-mcp | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | mcp | = | kind badge | default · item · revoke · share | product |  |  |
| Project | The set › Set row | Read-only Postgres access: schema, explain plans, sample rows. | **Read-only Postgres access for the agent: schema, explain plans, sample rows.** | description | default · item · revoke · share | user |  | Step 7 #22 U1 |
| Project | The set › Set row | `modelcontextprotocol/servers-archived` @ `9be4674` · MIT · needs `DATABASE_URL` | = | fact | default · item · revoke · share | product, with slots |  |  |
| Project | The set › Set row | github-mcp | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | Issues, pull requests and code search on GitHub. | **Issues, pull requests and code search on GitHub, through GitHub’s own server.** | description | default · item · revoke · share | user |  | Step 7 #22 U1 |
| Project | The set › Set row | `github/github-mcp-server` @ `v0.9.0` · MIT · needs `GITHUB_TOKEN` | = | fact | default · item · revoke · share | product, with slots |  |  |
| Project | The set › Set row | pr-reviewer | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | Detached | = | state badge | default · item · revoke · share | product | D8 |  |
| Project | The set › Set row | Reviews Acme pull requests against their billing rules. | = | description | default · item · revoke · share | user | U1 |  |
| Project | The set › Set row | differs from the library in content and lands at | **differs from the original in content and lands at** | fact | default · item · revoke · share | product | D1 D8 | D8 |
| Project | The set › Set row | commit-conventions | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | prompt | = | kind badge | default · item · revoke · share | product |  |  |
| Project | The set › Set row | Conventional commits, imperative mood, a body that says why. | **Conventional commits, imperative mood, and a body that says why rather than what.** | description | default · item · revoke · share | user |  | Step 7 #22 U1 |
| Project | The set › Set row | `CLAUDE.md`, appended | = | fact | default · item · revoke · share | product, with slots |  |  |
| Project | The set › Set row | test-runner | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | Runs the affected tests after a change and reports only the failures. | = | description | default · item · revoke · share | user |  |  |
| Project | The set › Set row | .claude/agents/test-runner.md | = | fact | default · item · revoke · share | user |  |  |
| Project | The set › Set row | changelog-writer | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | Writes the changelog entry from merged pull requests since the last tag. | = | description | default · item · revoke · share | user |  |  |
| Project | The set › Set row | .claude/skills/changelog-writer/SKILL.md | = | fact | default · item · revoke · share | user |  |  |
| Project | The set › Set row | api-contracts | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | The billing API’s rules: idempotency keys, money as integer cents. | = | description | default · item · revoke · share | user |  |  |
| Project | The set › Set row | openapi-lint | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | Lints the OpenAPI spec and fails on breaking changes. | = | description | default · item · revoke · share | user |  |  |
| Project | The set › Set row | scripts/openapi-lint.sh | = | fact | default · item · revoke · share | user |  |  |
| Project | The set › Set row | sentry-mcp | = | item name | default · item · revoke · share | user |  |  |
| Project | The set › Set row | Reads Sentry issues and stack traces for the service. | = | description | default · item · revoke · share | user |  |  |
| Project | The set › Set row | `getsentry/sentry-mcp` @ `0.17.1` · Apache-2.0 · needs `SENTRY_AUTH_TOKEN` | = | fact | default · item · revoke · share | product, with slots |  |  |
| Project | Library panel | Library panel | **Add items** | a11y label | empty | product | D1 | D1 |
| Project | Library panel | Add from | = | heading | empty | product |  |  |
| Project | Library panel › Scope | Scope | = | a11y label | empty | product |  |  |
| Project | Library panel › Scope | My library | = | nav | empty | product |  |  |
| Project | Library panel › Scope | Public library | = | nav | empty | product |  |  |
| Project | Library panel | Search My library | **Search My library — migrate, GITHUB_TOKEN, review** | placeholder | empty | product | D15 | D15: the place + three real examples, as on the detached-row pages |
| Project | Library panel › Kind | Kind | = | a11y label | empty | product |  |  |
| Project | Library panel › Kind | Related | = | nav | empty | product |  |  |
| Project | Library panel › Kind | All | = | nav | empty | product |  |  |
| Project | Library panel › Kind | skill | = | nav | empty | product |  |  |
| Project | Library panel › Kind | agent | = | nav | empty | product |  |  |
| Project | Library panel › Kind | prompt | = | nav | empty | product |  |  |
| Project | Library panel › Kind | mcp | = | nav | empty | product |  |  |
| Project | Library panel › Kind | script | = | nav | empty | product |  |  |
| Project | Library panel › Kind | app | = | nav | empty | product |  |  |
| Project | Library panel › Row | code-style | = | item name | empty | user |  |  |
| Project | Library panel › Row | skill | = | kind badge | empty | product |  |  |
| Project | Library panel › Row | How I want TypeScript written: naming, imports, error handling, no default exports. | = | panel row line | empty | user |  |  |
| Project | Library panel › Row | Add | = | option | empty | product |  |  |
| Project | Library panel › Row | db-migrate | = | item name | empty | user |  |  |
| Project | Library panel › Row | script | = | kind badge | empty | product |  |  |
| Project | Library panel › Row | Generates a Postgres migration from a schema diff and runs it — dry run first, then for real. | = | panel row line | empty | user |  |  |
| Project | Library panel › Row | seed-data | = | item name | empty | user |  |  |
| Project | Library panel › Row | Loads a small, realistic dataset into a fresh database. | = | panel row line | empty | user |  |  |
| Project | Library panel › Row | migration-reviewer | = | item name | empty | user |  |  |
| Project | Library panel › Row | agent | = | kind badge | empty | product |  |  |
| Project | Library panel › Row | Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills. | = | panel row line | empty | user |  |  |
| Project | Library panel › Row | postgres-mcp | = | item name | empty | user |  |  |
| Project | Library panel › Row | mcp | = | kind badge | empty | product |  |  |
| Project | Library panel › Row | Read-only Postgres access for the agent: schema, explain plans, sample rows. | = | panel row line | empty | user |  |  |
| Project | Library panel › Row | github-mcp | = | item name | empty | user |  |  |
| Project | Library panel › Row | Issues, pull requests and code search on GitHub, through GitHub’s own server. | = | panel row line | empty | user |  |  |
| Project | Library panel › Row | pr-reviewer | = | item name | empty | user |  |  |
| Project | Library panel › Row | Reads a pull request diff and leaves review comments the way I would write them. | = | panel row line | empty | user | U1 |  |
| Project | Library panel › Row | commit-conventions | = | item name | empty | user |  |  |
| Project | Library panel › Row | prompt | = | kind badge | empty | product |  |  |
| Project | Library panel › Row | Conventional commits, imperative mood, and a body that says why rather than what. | = | panel row line | empty | user |  |  |
| Project | Library panel › Row | writing-style | = | item name | empty | user |  |  |
| Project | Library panel › Row | Plain English for docs: short sentences, no marketing words, an example before every rule. | = | panel row line | empty | user |  |  |
| Project | Library panel › Row | link-checker | = | item name | empty | user |  |  |
| Project | Library panel › Row | Crawls the built docs and lists every broken internal and external link, with the page it is on. | = | panel row line | empty | user |  |  |
| Project | Library panel › Row | whisper | = | item name | empty | user |  |  |
| Project | Library panel › Row | app | = | kind badge | empty | product |  |  |
| Project | Library panel › Row | Speech-to-text, run locally on voice memos before they are summarised. | = | panel row line | empty | user |  |  |
| Project | Main › Page head | stripe-webhooks | = | title | empty | user | U2 |  |
| Project | Main › Page head | Configuring | = | state badge | empty | product |  |  |
| Project | Main › Page head | Created just now · nothing in it yet | **Created just now · no items yet** | fact | empty | product |  | D13 |
| Project | Main › Page head | Cancel | = | button | empty | product | D16 |  |
| Project | Main › Page head | Add an item first | = | tooltip | empty | product |  |  |
| Project | Main › Page head | Save | = | button | empty | product |  |  |
| Project | The set › State block | Nothing in this project yet | **No items in this project yet** | heading | empty | product | D13 | D13 |
| Project | The set › State block | Tick items in the library on the left to add them. Anything they require comes in with them, and Check opens once the set has something in it. | **Tick items on the left to add them. Anything they require is auto-added. Export… opens once this project has an item.** | state message | empty | product | D1 D6 D7 | Forbidden: the minimiser; D7, D6, Q36 |
| Project | Main › Page head | Last check not shown — the project didn’t load | = | fact | error | product |  |  |
| Project | Main › State block | This project didn’t load | = | a11y label | error | product |  |  |
| Project | Main › State block | This project didn’t load | = | heading | error | product |  |  |
| Project | Main › State block | The server did not answer, so the set and its last check can’t be shown. Nothing in the project was changed. | **Our server didn’t answer, so this project’s items and its last check can’t be shown. Nothing in the project changed.** | state message | error | product | D6 D9 T2 | D9, T2, D6 |
| Project | Main › State block | 503 · Service unavailable · 14:02 | = | state message | error | product | D10 |  |
| Project | Main › State block | Try again | **Load again** | button | error | product | D12 | D12 |
| Project | Main › State block | Back to Projects | = | button | error | product |  |  |
| Project | Main › Side panel: eslint-autofix | eslint-autofix | = | heading | item | user |  |  |
| Project | Main › Side panel: eslint-autofix | script | = | kind badge | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | Conflict | = | state badge | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | Close | = | a11y label | item | product | D16 |  |
| Project | Main › Side panel: eslint-autofix | Runs ESLint with --fix on staged files before each commit. | = | description | item | user |  |  |
| Project | Side panel: eslint-autofix › Finding | Problem at last check | = | status label | item | product |  |  |
| Project | Side panel: eslint-autofix › Finding | Declared conflict with `code-style`: it rewrites the imports that `code-style` tells the agent to keep. The archive will contain both. | **Declares a conflict with `code-style`: it rewrites the imports that `code-style` tells the agent to keep. The archive will contain both, and the agent will get two rules that disagree.** | state message | item | product, with slots |  | Principle 2: the consequence in the reader's terms, as in Run |
| Project | Main › Side panel: eslint-autofix | In this project | = | heading | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | Added by you · linked to the library version | **Added by you · linked to the original in My library** | body | item | product | D1 D8 | D8 |
| Project | Main › Side panel: eslint-autofix | Contents | = | heading | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | #!/usr/bin/env bash<br># Fix what ESLint can fix, on staged files only.<br>files=$(git diff --cached --name-only --diff-filter=ACM \| grep -E '\.(ts\|tsx)$')<br>[ -z "$files" ] && exit 0<br>npx eslint --fix $files && git add $files | = | generated file | item | user |  |  |
| Project | Main › Side panel: eslint-autofix | No files attached · no repo | = | fact | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | Dependencies | = | heading | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | Requires | = | field label | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | Nothing | **None** | body | item | product |  | One word for an empty field (Env keys reads None) |
| Project | Main › Side panel: eslint-autofix | Conflicts with | = | field label | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | code-style | = | body | item | user |  |  |
| Project | Main › Side panel: eslint-autofix | Env keys | = | field label | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | None | = | body | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | Lands at | = | field label | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | scripts/eslint-autofix.sh | = | body | item | user |  |  |
| Project | Main › Side panel: eslint-autofix | Use | = | heading | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | Used in 2 projects · last exported 2 days ago | = | body | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | Open in My library | = | button | item | product |  |  |
| Project | Main › Side panel: eslint-autofix | Remove in Configure | **Configure to remove** | button | item | product | D22 | D22 |
| Project | Main › The set | Opening acme-billing-api | **Loading acme-billing-api** | body | loading | product, with slots | D11 | D11 |
| Project | Main › Page head | (added) | **Shared** | state badge | revoke | product |  | Step 7 #20, Q37 |
| Project | Main › Page head | Share | **Stop sharing…** | button | revoke | product | D20 D21 | D20, D21; Step 7 #20, Q37: a shared project reads as shared, and stopping it is one press away |
| Project | Modal: Stop sharing acme-billing-api? | Stop sharing acme-billing-api? | = | heading | revoke | product, with slots |  |  |
| Project | Modal: Stop sharing acme-billing-api? | The link stops working at once. | = | body | revoke | product |  |  |
| Project | Modal: Stop sharing acme-billing-api? | It can’t reach what was already taken: anyone who downloaded the archive or copied its items keeps them. | **It can’t reach what was already taken: anyone who exported the archive or copied its items keeps them.** | body | revoke | product |  | D4; Dangerous action example |
| Project | Modal: Stop sharing acme-billing-api? | Cancel | = | button | revoke | product | D16 |  |
| Project | Modal: Stop sharing acme-billing-api? | Stop sharing | = | button | revoke | product | D21 |  |
| Project | Modal: Share acme-billing-api by link? | Share acme-billing-api by link? | = | heading | share | product, with slots |  |  |
| Project | Modal: Share acme-billing-api by link? | Anyone with the link can open this project and see it as it is now — and every edit you make later. | = | body | share | product |  |  |
| Project | Modal: Share acme-billing-api by link? | What becomes visible | = | body | share | product |  |  |
| Project | Modal: Share acme-billing-api by link? | The content of all 14 items — whatever is inside them goes with them | = | body | share | product |  |  |
| Project | Modal: Share acme-billing-api by link? | 3 env key names: `DATABASE_URL`, `GITHUB_TOKEN`, `SENTRY_AUTH_TOKEN` — names only, never values | = | body | share | product, with slots |  |  |
| Project | Modal: Share acme-billing-api by link? | 3 external items, at their pinned refs | **3 external items: modelcontextprotocol/servers-archived, github/github-mcp-server, getsentry/sentry-mcp — at their pinned refs** | body | share | product |  | Step 7 #15 the count expanded into names |
| Project | Modal: Share acme-billing-api by link? | When you last checked it | = | body | share | product | D19 |  |
| Project | Modal: Share acme-billing-api by link? › Finding | Note | = | severity | share | product |  |  |
| Project | Modal: Share acme-billing-api by link? › Finding | We can’t tell what in these items is your client’s — a rule naming them, an API shape in an example. Look before you share. | = | state message | share | product |  |  |
| Project | Modal: Share acme-billing-api by link? | Cancel | = | button | share | product | D16 |  |
| Project | Modal: Share acme-billing-api by link? | Create link | = | button | share | product | D21 |  |

### Project — configuring the set

State pages: `default` · `empty` · `error-filtered` · `error-server` · `item` · `loading-add` · `loading` · `public`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Project — configuring the set | Library panel | Library panel | **Add items** | a11y label | all | product | D1 | D1 |
| Project — configuring the set | Library panel | Add from | = | heading | all | product |  |  |
| Project — configuring the set | Library panel › Scope | Scope | = | a11y label | all | product |  |  |
| Project — configuring the set | Library panel › Scope | My library | = | nav | all | product |  |  |
| Project — configuring the set | Library panel › Scope | Public library | = | nav | all | product |  |  |
| Project — configuring the set | Library panel | Search My library | **Search My library — migrate, GITHUB_TOKEN, review** | placeholder | default · empty · error-filtered · error-server · item · loading-add · loading | product | D15 | D15: the place + three real examples, as on the detached-row pages |
| Project — configuring the set | Library panel › Kind | Kind | = | a11y label | all | product |  |  |
| Project — configuring the set | Library panel › Kind | Related | = | nav | all | product |  |  |
| Project — configuring the set | Library panel › Kind | All | = | nav | all | product |  |  |
| Project — configuring the set | Library panel › Kind | skill | = | nav | all | product |  |  |
| Project — configuring the set | Library panel › Kind | agent | = | nav | all | product |  |  |
| Project — configuring the set | Library panel › Kind | prompt | = | nav | all | product |  |  |
| Project — configuring the set | Library panel › Kind | mcp | = | nav | all | product |  |  |
| Project — configuring the set | Library panel › Kind | script | = | nav | all | product |  |  |
| Project — configuring the set | Library panel › Kind | app | = | nav | all | product |  |  |
| Project — configuring the set | Library panel › Row | db-migrate | = | item name | default · error-server · item · loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | script | = | kind badge | default · error-server · item · loading-add | product |  |  |
| Project — configuring the set | Library panel › Row | Required by `migration-reviewer` | = | panel row line | default · error-server · item | product, with slots |  |  |
| Project — configuring the set | Library panel › Row | In the set | **In this project** | option | default · error-server · item · loading-add | product | D6 | D6 |
| Project — configuring the set | Library panel › Row | postgres-mcp | = | item name | default · error-server · item · loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | mcp | = | kind badge | default · error-server · item · loading-add · public | product |  |  |
| Project — configuring the set | Library panel › Row | seed-data | = | item name | default · error-server · item · loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | Required by `db-migrate` | = | panel row line | default · error-server · item | product, with slots |  |  |
| Project — configuring the set | Library panel › Row | schema-docs | = | item name | default · error-server · item | user | U2 |  |
| Project — configuring the set | Library panel › Row | prompt | = | kind badge | default · error-server · item · loading-add | product |  |  |
| Project — configuring the set | Library panel › Row | Requires `postgres-mcp` | = | panel row line | default · error-server · item | product, with slots |  |  |
| Project — configuring the set | Library panel › Row | Add | = | option | default · error-server · item · loading-add · public | product |  |  |
| Project — configuring the set | Library panel › Row | query-explainer | = | item name | default · error-server · item | user | U2 |  |
| Project — configuring the set | Library panel › Row | agent | = | kind badge | default · error-server · item · loading-add | product |  |  |
| Project — configuring the set | Library panel › Row | pr-reviewer | = | item name | default · error-server · item · loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | Used with `github-mcp` in 2 projects | = | panel row line | default · error-server · item | product, with slots |  |  |
| Project — configuring the set | Main | Projects / | = | fact | all | product |  |  |
| Project — configuring the set | Main › Page head | acme-billing-api | = | title | default · error-filtered · error-server · item · loading | user |  |  |
| Project — configuring the set | Main › Page head | Configuring | = | state badge | all | product |  |  |
| Project — configuring the set | Main › Page head | 14 items · 3 auto-added · 1 detached | = | fact | default · error-filtered · item | product | D7 D8 |  |
| Project — configuring the set | Main › Page head | Checked 2 days ago · for Claude Code · 1 problem · 2 notes · 1 skipped | = | fact | default · error-filtered · error-server · item | product | D19 |  |
| Project — configuring the set | Main › Page head | Cancel | = | button | all | product | D16 |  |
| Project — configuring the set | Main › Page head | Check | **Export…** | button | default · empty · error-filtered · error-server · item · loading-add · public | product |  | Q36: the mode is titled by what it ends in; the check is its sub-process |
| Project — configuring the set | Main › Page head | Save | = | button | default · empty · error-filtered · error-server · item · loading-add · public | product |  |  |
| Project — configuring the set | Main › The set | The set | **Items in this project** | a11y label | all | product |  | D6 |
| Project — configuring the set | The set › Set row | code-style | = | item name | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | skill | = | kind badge | default · error-filtered · error-server · item | product |  |  |
| Project — configuring the set | The set › Set row | How I want TypeScript written: naming, imports, error handling. | **How I want TypeScript written: naming, imports, error handling, no default exports.** | description | default · error-filtered · error-server · item | user |  | Step 7 #22 U1 |
| Project — configuring the set | The set › Set row | `.claude/skills/code-style/SKILL.md` · defers to the client’s ESLint config | = | fact | default · error-filtered · error-server · item | product, with slots |  |  |
| Project — configuring the set | The set › Set row | Note | = | severity | default · error-filtered · error-server · item | product |  |  |
| Project — configuring the set | The set › Set row | Remove code-style | **Remove code-style from this project** | a11y label | default · error-filtered · error-server · item | product, with slots | D22 | D22 |
| Project — configuring the set | The set › Set row | eslint-autofix | = | item name | default · error-filtered · item | user |  |  |
| Project — configuring the set | The set › Set row | script | = | kind badge | default · error-filtered · error-server · item | product |  |  |
| Project — configuring the set | The set › Set row | Conflict | = | state badge | default · error-filtered · item | product |  |  |
| Project — configuring the set | The set › Set row | Runs ESLint with --fix on staged files before each commit. | = | description | default · error-filtered · item | user |  |  |
| Project — configuring the set | The set › Set row | `scripts/eslint-autofix.sh` · conflicts with `code-style` | = | fact | default · error-filtered · item | product, with slots |  |  |
| Project — configuring the set | The set › Set row | Problem | = | severity | default · error-filtered · item | product |  |  |
| Project — configuring the set | The set › Set row | Remove eslint-autofix | **Remove eslint-autofix from this project** | a11y label | default · error-filtered · item | product, with slots | D22 | D22 |
| Project — configuring the set | The set › Set row | migration-reviewer | = | item name | default · error-filtered · error-server · item · loading-add | user |  |  |
| Project — configuring the set | The set › Set row | agent | = | kind badge | default · error-filtered · error-server · item · loading-add | product |  |  |
| Project — configuring the set | The set › Set row | Reads a migration before it runs and flags long locks and missing down steps. | **Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills.** | description | default · error-filtered · error-server · item | user |  | Step 7 #22 U1 |
| Project — configuring the set | The set › Set row | requires `db-migrate`, `postgres-mcp` · brings 3 items with it | **requires `db-migrate`, `postgres-mcp` · 3 auto-added** | fact | default · error-filtered · error-server · item | product, with slots | D7 | D7 |
| Project — configuring the set | The set › Set row | Remove migration-reviewer and the 3 items it brings | **Remove migration-reviewer and its 3 auto-added items from this project** | a11y label | default · error-filtered · error-server · item | product, with slots | D7 D22 | D7, D22 |
| Project — configuring the set | Main › The set | Pulled in by migration-reviewer | **Auto-added for migration-reviewer** | a11y label | default · error-filtered · error-server · item | product, with slots | D7 | D7 |
| Project — configuring the set | The set › Set row | db-migrate | = | item name | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | Auto-added | = | state badge | default · error-filtered · error-server · item | product | D7 |  |
| Project — configuring the set | The set › Set row | Generates a Postgres migration from a schema diff and runs it, dry run first. | **Generates a Postgres migration from a schema diff and runs it — dry run first, then for real.** | description | default · error-filtered · error-server · item | user |  | Step 7 #22 U1 |
| Project — configuring the set | The set › Set row | `scripts/db-migrate.sh` + 2 files · brings 1 item with it | **`scripts/db-migrate.sh` + 2 files · 1 auto-added** | fact | default · error-filtered · error-server · item | product, with slots | D7 | D7 |
| Project — configuring the set | Main › The set | Pulled in by db-migrate | **Auto-added for db-migrate** | a11y label | default · error-filtered · error-server · item | product, with slots | D7 | D7 |
| Project — configuring the set | The set › Set row | seed-data | = | item name | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | Loads a small, realistic dataset into a fresh database. | = | description | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | scripts/seed-data.sh | = | fact | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | postgres-mcp | = | item name | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | mcp | = | kind badge | default · error-filtered · error-server · item | product |  |  |
| Project — configuring the set | The set › Set row | Read-only Postgres access: schema, explain plans, sample rows. | **Read-only Postgres access for the agent: schema, explain plans, sample rows.** | description | default · error-filtered · error-server · item | user |  | Step 7 #22 U1 |
| Project — configuring the set | The set › Set row | `modelcontextprotocol/servers-archived` @ `9be4674` · MIT · needs `DATABASE_URL` | = | fact | default · error-filtered · error-server · item | product, with slots |  |  |
| Project — configuring the set | The set › Set row | github-mcp | = | item name | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | Issues, pull requests and code search on GitHub. | **Issues, pull requests and code search on GitHub, through GitHub’s own server.** | description | default · error-filtered · error-server · item | user |  | Step 7 #22 U1 |
| Project — configuring the set | The set › Set row | `github/github-mcp-server` @ `v0.9.0` · MIT · needs `GITHUB_TOKEN` | = | fact | default · error-filtered · error-server · item | product, with slots |  |  |
| Project — configuring the set | The set › Set row | Remove github-mcp | **Remove github-mcp from this project** | a11y label | default · error-filtered · error-server · item | product, with slots | D22 | D22 |
| Project — configuring the set | The set › Set row | pr-reviewer | = | item name | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | Detached | = | state badge | default · error-filtered · error-server · item | product | D8 |  |
| Project — configuring the set | The set › Set row | Reviews Acme pull requests against their billing rules. | = | description | default · error-filtered · error-server · item | user | U1 |  |
| Project — configuring the set | The set › Set row | differs from the library in content and lands at | **differs from the original in content and lands at** | fact | default · error-filtered · error-server · item | product | D1 D8 | D8 |
| Project — configuring the set | The set › Set row | Remove pr-reviewer | **Remove pr-reviewer from this project** | a11y label | default · error-filtered · error-server · item | product, with slots | D22 | D22 |
| Project — configuring the set | The set › Set row | commit-conventions | = | item name | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | prompt | = | kind badge | default · error-filtered · error-server · item | product |  |  |
| Project — configuring the set | The set › Set row | Conventional commits, imperative mood, a body that says why. | **Conventional commits, imperative mood, and a body that says why rather than what.** | description | default · error-filtered · error-server · item | user |  | Step 7 #22 U1 |
| Project — configuring the set | The set › Set row | `CLAUDE.md`, appended | = | fact | default · error-filtered · error-server · item | product, with slots |  |  |
| Project — configuring the set | The set › Set row | Remove commit-conventions | **Remove commit-conventions from this project** | a11y label | default · error-filtered · error-server · item | product, with slots | D22 | D22 |
| Project — configuring the set | The set › Set row | test-runner | = | item name | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | Runs the affected tests after a change and reports only the failures. | = | description | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | .claude/agents/test-runner.md | = | fact | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | Remove test-runner | **Remove test-runner from this project** | a11y label | default · error-filtered · error-server · item | product, with slots | D22 | D22 |
| Project — configuring the set | The set › Set row | changelog-writer | = | item name | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | Writes the changelog entry from merged pull requests since the last tag. | = | description | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | .claude/skills/changelog-writer/SKILL.md | = | fact | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | Remove changelog-writer | **Remove changelog-writer from this project** | a11y label | default · error-filtered · error-server · item | product, with slots | D22 | D22 |
| Project — configuring the set | The set › Set row | api-contracts | = | item name | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | The billing API’s rules: idempotency keys, money as integer cents. | = | description | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | Remove api-contracts | **Remove api-contracts from this project** | a11y label | default · error-filtered · error-server · item | product, with slots | D22 | D22 |
| Project — configuring the set | The set › Set row | openapi-lint | = | item name | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | Lints the OpenAPI spec and fails on breaking changes. | = | description | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | scripts/openapi-lint.sh | = | fact | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | Remove openapi-lint | **Remove openapi-lint from this project** | a11y label | default · error-filtered · error-server · item | product, with slots | D22 | D22 |
| Project — configuring the set | The set › Set row | sentry-mcp | = | item name | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | Reads Sentry issues and stack traces for the service. | = | description | default · error-filtered · error-server · item | user |  |  |
| Project — configuring the set | The set › Set row | `getsentry/sentry-mcp` @ `0.17.1` · Apache-2.0 · needs `SENTRY_AUTH_TOKEN` | = | fact | default · error-filtered · error-server · item | product, with slots |  |  |
| Project — configuring the set | The set › Set row | Remove sentry-mcp | **Remove sentry-mcp from this project** | a11y label | default · error-filtered · error-server · item | product, with slots | D22 | D22 |
| Project — configuring the set | Library panel › State block | My library is empty | **No items in My library yet** | a11y label | empty | product |  | D13 |
| Project — configuring the set | Library panel › State block | My library is empty | **No items in My library yet** | heading | empty | product | D13 | D13 |
| Project — configuring the set | Library panel › State block | Your own items appear here once you add them. The Public library has 8 items, each pinned to the version we checked, that you can add right now. | **Items you add to My library appear here. The Public library has 8 items, each pinned to the version we checked, and you can add any of them now.** | state message | empty | product | D1 | D1 |
| Project — configuring the set | Library panel › State block | Switch to Public library | **Open Public library** | button | empty | product |  | Button: plain verb |
| Project — configuring the set | Library panel › State block | Add item | = | button | empty | product |  |  |
| Project — configuring the set | Main › Page head | stripe-webhooks | = | title | empty · loading-add · public | user | U2 |  |
| Project — configuring the set | Main › Page head | Nothing in it yet | **No items yet** | fact | empty · public | product |  | D13 |
| Project — configuring the set | Main › Page head | Add an item first | = | tooltip | empty · loading-add · public | product |  |  |
| Project — configuring the set | The set › State block | Nothing in this project yet | **No items in this project yet** | heading | empty · public | product | D13 | D13 |
| Project — configuring the set | The set › State block | Tick items in the library on the left to add them. Anything they require comes in with them, and Check opens once the set has something in it. | **Tick items on the left to add them. Anything they require is auto-added. Export… opens once this project has an item.** | state message | empty · public | product | D1 D6 D7 | Forbidden: the minimiser; D7, D6, Q36 |
| Project — configuring the set | Library panel | sentry | = | value | error-filtered | user |  |  |
| Project — configuring the set | Library panel › State block | Nothing called “sentry” here | **Nothing matches “sentry”** | a11y label | error-filtered | product |  | D13 |
| Project — configuring the set | Library panel › State block | Nothing called “sentry” here | **Nothing matches “sentry”** | heading | error-filtered | product | D13 | D13 |
| Project — configuring the set | Library panel › State block | No item related to this set matches “sentry”. It may be under another kind, on the shelf, or not written yet. | **The tab shows only items related to this project. It holds 6 — the search hides all of them. “sentry” may be under All, in Public library, or not written yet.** | state message | error-filtered | product | D2 D6 | D13, principle 4, D2, D6; Step 7 #8 filtered body, one form |
| Project — configuring the set | Library panel › State block | Clear search | = | button | error-filtered | product | D14 |  |
| Project — configuring the set | Library panel › State block | Add “sentry” as a new item | = | button | error-filtered | product |  |  |
| Project — configuring the set | Main › Page head | 13 items · 3 auto-added · 1 detached | = | fact | error-server | product | D7 D8 |  |
| Project — configuring the set | The set › Finding | Not saved | = | status label | error-server | product |  |  |
| Project — configuring the set | The set › Finding | The server didn’t confirm the save, so acme-billing-api is as it was — 14 items, `eslint-autofix` still in it. Your changes are still here. 503 · 14:09 | **Our server didn’t confirm the save, so acme-billing-api is as it was — 14 items, `eslint-autofix` still in it. Your changes are still here.** | state message | error-server | product, with slots | D9 D10 | D9, D10; Step 7 #19: the error code moved to a line of its own (D10) |
| Project — configuring the set | Items in this project › Finding | (added) | **503 · Service unavailable · 14:09** | state message | error-server | product |  | Step 7 #18/#19: the error code on its own line (D10) |
| Project — configuring the set | The set › Finding | Save again | = | button | error-server | product | D12 |  |
| Project — configuring the set | The set › Finding | Discard changes | = | button | error-server | product | D16 |  |
| Project — configuring the set | Main › Side panel: code-style | code-style | = | heading | item | user |  |  |
| Project — configuring the set | Main › Side panel: code-style | skill | = | kind badge | item | product |  |  |
| Project — configuring the set | Main › Side panel: code-style | Close | = | a11y label | item | product | D16 |  |
| Project — configuring the set | Main › Side panel: code-style | How I want TypeScript written: naming, imports, error handling. | **How I want TypeScript written: naming, imports, error handling, no default exports.** | description | item | user |  | Step 7 #22 U1 |
| Project — configuring the set | Main › Side panel: code-style | Linked to the library — an edit in My library reaches this project and the 2 others that use it. | **Linked to the original in My library — an edit there reaches this project and the 2 others that use it.** | fact | item | product | D1 D8 | D8 |
| Project — configuring the set | Side panel: code-style › Finding | Note at last check | = | status label | item | product |  |  |
| Project — configuring the set | Side panel: code-style › Finding | Where `code-style` and the client’s ESLint config disagree, the ESLint config wins. | = | state message | item | product, with slots |  |  |
| Project — configuring the set | Main › Side panel: code-style | Contents | = | heading | item | product |  |  |
| Project — configuring the set | Main › Side panel: code-style | ---<br>name: code-style<br>description: How TypeScript is written in my projects.<br>---<br>- Named exports only. No default exports.<br>- Imports: built-ins, then packages, then local.<br>- Throw typed errors from lib code; catch only at the edge. | = | generated file | item | user |  |  |
| Project — configuring the set | Main › Side panel: code-style | Dependencies | = | heading | item | product |  |  |
| Project — configuring the set | Main › Side panel: code-style | Requires | = | field label | item | product |  |  |
| Project — configuring the set | Main › Side panel: code-style | Nothing | **None** | body | item | product |  | One word for an empty field, as on Project's side panel |
| Project — configuring the set | Main › Side panel: code-style | Defers to | = | field label | item | product |  |  |
| Project — configuring the set | Main › Side panel: code-style | the client’s ESLint config | = | body | item | user |  |  |
| Project — configuring the set | Main › Side panel: code-style | Lands at | = | field label | item | product |  |  |
| Project — configuring the set | Main › Side panel: code-style | .claude/skills/code-style/SKILL.md | = | body | item | user |  |  |
| Project — configuring the set | Main › Side panel: code-style | Detach to edit here | = | button | item | product | D8 |  |
| Project — configuring the set | Main › Side panel: code-style | Open in My library | = | button | item | product |  |  |
| Project — configuring the set | Main › Side panel: code-style | Remove from the set | **Remove from project** | button | item | product | D6 D22 | D6, D22 |
| Project — configuring the set | Main › Side panel: code-style | Detach makes a copy for this project only. My library and the other projects keep the original. | = | fact | item | product | D8 |  |
| Project — configuring the set | Library panel › Row | code-style | = | item name | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | skill | = | kind badge | loading-add · public | product |  |  |
| Project — configuring the set | Library panel › Row | How I want TypeScript written: naming, imports, error handling, no default exports. | = | panel row line | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | Generates a Postgres migration from a schema diff and runs it — dry run first, then for real. | = | panel row line | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | Loads a small, realistic dataset into a fresh database. | = | panel row line | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | migration-reviewer | = | item name | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills. | = | panel row line | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | Read-only Postgres access for the agent: schema, explain plans, sample rows. | = | panel row line | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | github-mcp | = | item name | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | Issues, pull requests and code search on GitHub, through GitHub’s own server. | = | panel row line | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | Reads a pull request diff and leaves review comments the way I would write them. | = | panel row line | loading-add | user | U1 |  |
| Project — configuring the set | Library panel › Row | commit-conventions | = | item name | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | Conventional commits, imperative mood, and a body that says why rather than what. | = | panel row line | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | writing-style | = | item name | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | Plain English for docs: short sentences, no marketing words, an example before every rule. | = | panel row line | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | link-checker | = | item name | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | Crawls the built docs and lists every broken internal and external link, with the page it is on. | = | panel row line | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | whisper | = | item name | loading-add | user |  |  |
| Project — configuring the set | Library panel › Row | app | = | kind badge | loading-add | product |  |  |
| Project — configuring the set | Library panel › Row | Speech-to-text, run locally on voice memos before they are summarised. | = | panel row line | loading-add | user |  |  |
| Project — configuring the set | Main › Page head | 1 item | = | fact | loading-add | product |  |  |
| Project — configuring the set | The set › Set row | Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills. | = | description | loading-add | user |  |  |
| Project — configuring the set | The set › Set row | Adding — finding what it requires… | **Adding — finding what it requires** | fact | loading-add | product | D11 | D20, D11 |
| Project — configuring the set | Main › The set | Loading the set and the library | **Loading acme-billing-api and My library** | body | loading | product | D1 D6 D11 | D11, D1, D6 |
| Project — configuring the set | Library panel | Search Public library | **Search Public library — filesystem, playwright, anthropics** | placeholder | public | product | D15 | D15 |
| Project — configuring the set | Library panel › Row | filesystem | = | item name | public | user |  |  |
| Project — configuring the set | Library panel › Row | Read and write files inside the directories you allow, and nowhere else. | = | panel row line | public | user |  |  |
| Project — configuring the set | Library panel › Row | memory | = | item name | public | user |  |  |
| Project — configuring the set | Library panel › Row | A knowledge graph the agent can write to and read back between sessions. | = | panel row line | public | user |  |  |
| Project — configuring the set | Library panel › Row | fetch | = | item name | public | user |  |  |
| Project — configuring the set | Library panel › Row | Fetches a URL and hands the agent the page as Markdown. | = | panel row line | public | user |  |  |
| Project — configuring the set | Library panel › Row | github-mcp-server | = | item name | public | user |  |  |
| Project — configuring the set | Library panel › Row | GitHub’s own MCP server: issues, pull requests, Actions and code search. | = | panel row line | public | user |  |  |
| Project — configuring the set | Library panel › Row | playwright-mcp | = | item name | public | user |  |  |
| Project — configuring the set | Library panel › Row | Drives a real browser through the accessibility tree rather than screenshots. | = | panel row line | public | user |  |  |
| Project — configuring the set | Library panel › Row | context7 | = | item name | public | user |  |  |
| Project — configuring the set | Library panel › Row | Pulls current, version-specific library documentation into the prompt. | = | panel row line | public | user |  |  |
| Project — configuring the set | Library panel › Row | mcp-builder | = | item name | public | user |  |  |
| Project — configuring the set | Library panel › Row | A guide for building an MCP server: tool design, error messages, evaluation. | = | panel row line | public | user |  |  |
| Project — configuring the set | Library panel › Row | webapp-testing | = | item name | public | user | U2 |  |
| Project — configuring the set | Library panel › Row | Tests a local web app with Playwright: start the server, drive the page, read the logs. | = | panel row line | public | user |  |  |

### Project — a detached row

State pages: `default` · `error` · `loading` · `promote`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Project — a detached row | Library panel | Library panel | **Add items** | a11y label | all | product | D1 | D1 |
| Project — a detached row | Library panel | Add from | = | heading | all | product |  |  |
| Project — a detached row | Library panel › Scope | Scope | = | a11y label | all | product |  |  |
| Project — a detached row | Library panel › Scope | My library | = | nav | all | product |  |  |
| Project — a detached row | Library panel › Scope | Public library | = | nav | all | product |  |  |
| Project — a detached row | Library panel | Search My library | **Search My library — migrate, GITHUB_TOKEN, review** | placeholder | all | product | D15 | D15 |
| Project — a detached row | Library panel › Kind | Kind | = | a11y label | all | product |  |  |
| Project — a detached row | Library panel › Kind | Related | = | nav | all | product |  |  |
| Project — a detached row | Library panel › Kind | All | = | nav | all | product |  |  |
| Project — a detached row | Library panel › Kind | skill | = | nav | all | product |  |  |
| Project — a detached row | Library panel › Kind | agent | = | nav | all | product |  |  |
| Project — a detached row | Library panel › Kind | prompt | = | nav | all | product |  |  |
| Project — a detached row | Library panel › Kind | mcp | = | nav | all | product |  |  |
| Project — a detached row | Library panel › Kind | script | = | nav | all | product |  |  |
| Project — a detached row | Library panel › Kind | app | = | nav | all | product |  |  |
| Project — a detached row | Library panel › Row | db-migrate | = | item name | all | user |  |  |
| Project — a detached row | Library panel › Row | script | = | kind badge | all | product |  |  |
| Project — a detached row | Library panel › Row | Required by `migration-reviewer` | = | panel row line | all | product, with slots |  |  |
| Project — a detached row | Library panel › Row | In the set | **In this project** | option | all | product | D6 | D6 |
| Project — a detached row | Library panel › Row | postgres-mcp | = | item name | all | user |  |  |
| Project — a detached row | Library panel › Row | mcp | = | kind badge | all | product |  |  |
| Project — a detached row | Library panel › Row | seed-data | = | item name | all | user |  |  |
| Project — a detached row | Library panel › Row | Required by `db-migrate` | = | panel row line | all | product, with slots |  |  |
| Project — a detached row | Library panel › Row | schema-docs | = | item name | all | user | U2 |  |
| Project — a detached row | Library panel › Row | prompt | = | kind badge | all | product |  |  |
| Project — a detached row | Library panel › Row | Requires `postgres-mcp` | = | panel row line | all | product, with slots |  |  |
| Project — a detached row | Library panel › Row | Add | = | option | all | product |  |  |
| Project — a detached row | Library panel › Row | query-explainer | = | item name | all | user | U2 |  |
| Project — a detached row | Library panel › Row | agent | = | kind badge | all | product |  |  |
| Project — a detached row | Library panel › Row | pr-reviewer | = | item name | all | user |  |  |
| Project — a detached row | Library panel › Row | Used with `github-mcp` in 2 projects | = | panel row line | all | product, with slots |  |  |
| Project — a detached row | Main | Projects / | = | fact | all | product |  |  |
| Project — a detached row | Main › Page head | acme-billing-api | = | title | all | user |  |  |
| Project — a detached row | Main › Page head | Configuring | = | state badge | all | product |  |  |
| Project — a detached row | Main › Page head | 14 items · 3 auto-added · 1 detached | = | fact | all | product | D7 D8 |  |
| Project — a detached row | Main › Page head | Checked 2 days ago · for Claude Code · 1 problem · 2 notes · 1 skipped | = | fact | all | product | D19 |  |
| Project — a detached row | Main › Page head | Cancel | = | button | all | product | D16 |  |
| Project — a detached row | Main › Page head | Check | **Export…** | button | all | product |  | Q36: the mode is titled by what it ends in; the check is its sub-process |
| Project — a detached row | Main › Page head | Save | = | button | all | product |  |  |
| Project — a detached row | Main › The set | The set | **Items in this project** | a11y label | all | product |  | D6 |
| Project — a detached row | The set › Set row | code-style | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | skill | = | kind badge | all | product |  |  |
| Project — a detached row | The set › Set row | How I want TypeScript written: naming, imports, error handling. | **How I want TypeScript written: naming, imports, error handling, no default exports.** | description | all | user |  | Step 7 #22 U1 |
| Project — a detached row | The set › Set row | `.claude/skills/code-style/SKILL.md` · defers to the client’s ESLint config | = | fact | all | product, with slots |  |  |
| Project — a detached row | The set › Set row | Note | = | severity | all | product |  |  |
| Project — a detached row | The set › Set row | Remove code-style | **Remove code-style from this project** | a11y label | all | product, with slots | D22 | D22 |
| Project — a detached row | The set › Set row | eslint-autofix | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | script | = | kind badge | all | product |  |  |
| Project — a detached row | The set › Set row | Conflict | = | state badge | all | product |  |  |
| Project — a detached row | The set › Set row | Runs ESLint with --fix on staged files before each commit. | = | description | all | user |  |  |
| Project — a detached row | The set › Set row | `scripts/eslint-autofix.sh` · conflicts with `code-style` | = | fact | all | product, with slots |  |  |
| Project — a detached row | The set › Set row | Problem | = | severity | all | product |  |  |
| Project — a detached row | The set › Set row | Remove eslint-autofix | **Remove eslint-autofix from this project** | a11y label | all | product, with slots | D22 | D22 |
| Project — a detached row | The set › Set row | migration-reviewer | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | agent | = | kind badge | all | product |  |  |
| Project — a detached row | The set › Set row | Reads a migration before it runs and flags long locks and missing down steps. | **Reads a migration before it runs and flags long locks, missing down steps and unbatched backfills.** | description | all | user |  | Step 7 #22 U1 |
| Project — a detached row | The set › Set row | requires `db-migrate`, `postgres-mcp` · brings 3 items with it | **requires `db-migrate`, `postgres-mcp` · 3 auto-added** | fact | all | product, with slots | D7 | D7 |
| Project — a detached row | The set › Set row | Remove migration-reviewer and the 3 items it brings | **Remove migration-reviewer and its 3 auto-added items from this project** | a11y label | all | product, with slots | D7 D22 | D7, D22 |
| Project — a detached row | Main › The set | Pulled in by migration-reviewer | **Auto-added for migration-reviewer** | a11y label | all | product, with slots | D7 | D7 |
| Project — a detached row | The set › Set row | db-migrate | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | Auto-added | = | state badge | all | product | D7 |  |
| Project — a detached row | The set › Set row | Generates a Postgres migration from a schema diff and runs it, dry run first. | **Generates a Postgres migration from a schema diff and runs it — dry run first, then for real.** | description | all | user |  | Step 7 #22 U1 |
| Project — a detached row | The set › Set row | `scripts/db-migrate.sh` + 2 files · brings 1 item with it | **`scripts/db-migrate.sh` + 2 files · 1 auto-added** | fact | all | product, with slots | D7 | D7 |
| Project — a detached row | Main › The set | Pulled in by db-migrate | **Auto-added for db-migrate** | a11y label | all | product, with slots | D7 | D7 |
| Project — a detached row | The set › Set row | seed-data | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | Loads a small, realistic dataset into a fresh database. | = | description | all | user |  |  |
| Project — a detached row | The set › Set row | scripts/seed-data.sh | = | fact | all | user |  |  |
| Project — a detached row | The set › Set row | postgres-mcp | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | mcp | = | kind badge | all | product |  |  |
| Project — a detached row | The set › Set row | Read-only Postgres access: schema, explain plans, sample rows. | **Read-only Postgres access for the agent: schema, explain plans, sample rows.** | description | all | user |  | Step 7 #22 U1 |
| Project — a detached row | The set › Set row | `modelcontextprotocol/servers-archived` @ `9be4674` · MIT · needs `DATABASE_URL` | = | fact | all | product, with slots |  |  |
| Project — a detached row | The set › Set row | github-mcp | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | Issues, pull requests and code search on GitHub. | **Issues, pull requests and code search on GitHub, through GitHub’s own server.** | description | all | user |  | Step 7 #22 U1 |
| Project — a detached row | The set › Set row | `github/github-mcp-server` @ `v0.9.0` · MIT · needs `GITHUB_TOKEN` | = | fact | all | product, with slots |  |  |
| Project — a detached row | The set › Set row | Remove github-mcp | **Remove github-mcp from this project** | a11y label | all | product, with slots | D22 | D22 |
| Project — a detached row | The set › Set row | pr-reviewer | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | Detached | = | state badge | all | product | D8 |  |
| Project — a detached row | The set › Set row | Reviews Acme pull requests against their billing rules. | = | description | all | user | U1 |  |
| Project — a detached row | The set › Set row | differs from the library in content and lands at | **differs from the original in content and lands at** | fact | all | product | D1 D8 | D8 |
| Project — a detached row | The set › Set row | Remove pr-reviewer | **Remove pr-reviewer from this project** | a11y label | all | product, with slots | D22 | D22 |
| Project — a detached row | The set › Set row | commit-conventions | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | prompt | = | kind badge | all | product |  |  |
| Project — a detached row | The set › Set row | Conventional commits, imperative mood, a body that says why. | **Conventional commits, imperative mood, and a body that says why rather than what.** | description | all | user |  | Step 7 #22 U1 |
| Project — a detached row | The set › Set row | `CLAUDE.md`, appended | = | fact | all | product, with slots |  |  |
| Project — a detached row | The set › Set row | Remove commit-conventions | **Remove commit-conventions from this project** | a11y label | all | product, with slots | D22 | D22 |
| Project — a detached row | The set › Set row | test-runner | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | Runs the affected tests after a change and reports only the failures. | = | description | all | user |  |  |
| Project — a detached row | The set › Set row | .claude/agents/test-runner.md | = | fact | all | user |  |  |
| Project — a detached row | The set › Set row | Remove test-runner | **Remove test-runner from this project** | a11y label | all | product, with slots | D22 | D22 |
| Project — a detached row | The set › Set row | changelog-writer | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | Writes the changelog entry from merged pull requests since the last tag. | = | description | all | user |  |  |
| Project — a detached row | The set › Set row | .claude/skills/changelog-writer/SKILL.md | = | fact | all | user |  |  |
| Project — a detached row | The set › Set row | Remove changelog-writer | **Remove changelog-writer from this project** | a11y label | all | product, with slots | D22 | D22 |
| Project — a detached row | The set › Set row | api-contracts | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | The billing API’s rules: idempotency keys, money as integer cents. | = | description | all | user |  |  |
| Project — a detached row | The set › Set row | Remove api-contracts | **Remove api-contracts from this project** | a11y label | all | product, with slots | D22 | D22 |
| Project — a detached row | The set › Set row | openapi-lint | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | Lints the OpenAPI spec and fails on breaking changes. | = | description | all | user |  |  |
| Project — a detached row | The set › Set row | scripts/openapi-lint.sh | = | fact | all | user |  |  |
| Project — a detached row | The set › Set row | Remove openapi-lint | **Remove openapi-lint from this project** | a11y label | all | product, with slots | D22 | D22 |
| Project — a detached row | The set › Set row | sentry-mcp | = | item name | all | user |  |  |
| Project — a detached row | The set › Set row | Reads Sentry issues and stack traces for the service. | = | description | all | user |  |  |
| Project — a detached row | The set › Set row | `getsentry/sentry-mcp` @ `0.17.1` · Apache-2.0 · needs `SENTRY_AUTH_TOKEN` | = | fact | all | product, with slots |  |  |
| Project — a detached row | The set › Set row | Remove sentry-mcp | **Remove sentry-mcp from this project** | a11y label | all | product, with slots | D22 | D22 |
| Project — a detached row | Main › Side panel: pr-reviewer | pr-reviewer | = | heading | all | user |  |  |
| Project — a detached row | Main › Side panel: pr-reviewer | agent | = | kind badge | all | product |  |  |
| Project — a detached row | Main › Side panel: pr-reviewer | Detached | = | state badge | all | product | D8 |  |
| Project — a detached row | Main › Side panel: pr-reviewer | Close | = | a11y label | all | product | D16 |  |
| Project — a detached row | Main › Side panel: pr-reviewer | Modified in this project. My library and the other project that uses `pr-reviewer` don’t get these changes. | **Edited for this project only. The original in My library, and the other project that uses `pr-reviewer`, don’t get these changes.** | fact | default · error · promote | product, with slots | D8 | D8 |
| Project — a detached row | Main › Side panel: pr-reviewer | 2 fields differ from the library | **2 fields differ from the original** | heading | default · error · promote | product | D1 D8 | D8 |
| Project — a detached row | Main › Side panel: pr-reviewer | Lands at | = | field label | default · error · promote | product |  |  |
| Project — a detached row | Main › Side panel: pr-reviewer | .claude/agents/acme-pr-reviewer.md | = | value | default · error · promote | user |  |  |
| Project — a detached row | Main › Side panel: pr-reviewer | Library: `.claude/agents/pr-reviewer.md` · | **Original: `.claude/agents/pr-reviewer.md` ·** | fact | default · error · promote | product, with slots | D1 | D8 |
| Project — a detached row | Main › Side panel: pr-reviewer | Reset this field | = | button | default · error · promote | product |  |  |
| Project — a detached row | Main › Side panel: pr-reviewer | Content | = | field label | default · error · promote | product |  |  |
| Project — a detached row | Main › Side panel: pr-reviewer | Library version · | **Original ·** | fact | default · error · promote | product | D1 D8 | D8 |
| Project — a detached row | Main › Side panel: pr-reviewer | ---<br>name: pr-reviewer<br>description: Review a pull request the way I would.<br>---<br>Read the diff. Comment the way Maya would: short,<br>specific, one suggestion per comment. | = | generated file | default · error · promote | user |  |  |
| Project — a detached row | Main › Side panel: pr-reviewer | Reset whole item | **Reset to the original** | button | default · error · promote | product |  | Step 7 #4 D8 dictionary |
| Project — a detached row | Main › Side panel: pr-reviewer | Promote to My library… | = | button | default · error · promote | product | D20 |  |
| Project — a detached row | Main › Side panel: pr-reviewer | Remove from the set | **Remove from project** | button | default · error · promote | product | D6 D22 | D6, D22 |
| Project — a detached row | Main › Side panel: pr-reviewer | Changes here are kept when you save the project. | = | fact | default · error · promote | product |  |  |
| Project — a detached row | Side panel: pr-reviewer › Finding | Promote didn’t land | = | status label | error | product |  |  |
| Project — a detached row | Side panel: pr-reviewer › Finding | The server didn’t confirm it, so there is no new item in My library and this row is still detached. Your edits below are untouched. | **Our server didn’t confirm it, so there is no new item in My library and this row is still detached. Your edits below are untouched.** | state message | error | product | D8 D9 | D9 |
| Project — a detached row | Side panel: pr-reviewer › Finding | 503 · Service unavailable · 14:02 | = | state message | error | product | D10 |  |
| Project — a detached row | Side panel: pr-reviewer › Finding | Promote again | = | button | error | product | D12 |  |
| Project — a detached row | Side panel: pr-reviewer › Finding | Dismiss | **Close** | button | error | product | D16 | D16 |
| Project — a detached row | Main › Side panel: pr-reviewer | Comparing pr-reviewer with the library version | **Loading pr-reviewer and the original in My library** | body | loading | product, with slots | D1 D8 | D11, D8 |
| Project — a detached row | Main › Side panel: pr-reviewer | Lands at | = | body | loading | product |  |  |
| Project — a detached row | Main › Side panel: pr-reviewer | Content | = | body | loading | product |  |  |
| Project — a detached row | Modal: Promote pr-reviewer to My library? | Promote pr-reviewer to My library? | = | heading | promote | product, with slots |  |  |
| Project — a detached row | Modal: Promote pr-reviewer to My library? › Form | Name of the new item | = | field label | promote | product |  |  |
| Project — a detached row | Modal: Promote pr-reviewer to My library? › Form | acme-pr-reviewer | = | value | promote | user |  |  |
| Project — a detached row | Modal: Promote pr-reviewer to My library? | It becomes a new item in My library with this project’s changes, and this row links to it. The original `pr-reviewer`, and the other project that uses it, stay as they are. | **It becomes a new item in My library with this project’s changes, and this row links to it. The original `pr-reviewer`, and the other project that uses it, stay as they are. This happens now, not when you save the project.** | body | promote | product, with slots | D8 | Principle 2: Promote is immediate inside a draft |
| Project — a detached row | Modal: Promote pr-reviewer to My library? | Cancel | = | button | promote | product | D16 |  |
| Project — a detached row | Modal: Promote pr-reviewer to My library? | Promote | = | button | promote | product |  |  |

### Run

State pages: `default` · `error-check` · `error-export` · `error-setup` · `loading-export` · `loading` · `remove` · `success`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Run | Run bar | acme-billing-api | = | link | all | user |  |  |
| Run | Run bar | Check | **Export** | title | all | product | D3 | Q36: the mode is titled by what it ends in; the check is its sub-process |
| Run | Run bar | Agent target | = | field label | all | product |  |  |
| Run | Run bar | Claude Code | = | option | all | product |  |  |
| Run | Run bar | Cursor | = | option | all | product |  |  |
| Run | Run bar | Codex | = | option | all | product |  |  |
| Run | Run bar | Universal | = | option | all | product |  |  |
| Run | Main › Verdict | Verdict | = | a11y label | all | product |  |  |
| Run | Main › Verdict | Checked just now | = | title | default · error-export · error-setup · loading-export · remove · success | product | D19 |  |
| Run | Main › Verdict | 1 problem · 2 notes · 1 skipped | = | state message | default · error-export · error-setup · loading-export · remove · success | product |  |  |
| Run | Main › Verdict | acme-billing-api · 14 items · for Claude Code · 1.8 s | = | state message | default · error-export · error-setup · loading-export · remove · success | product, with slots |  |  |
| Run | Main › Stages: Findings | Findings | = | heading | all | product |  |  |
| Run | Main › Stages: Findings | Resolve the set | **Requirements** | stage name | all | product | D6 | Dictionary: project, not set (D6) |
| Run | Main › Stages: Findings | 14 items · 3 auto-added · no cycles | = | stage result | all | product | D7 |  |
| Run | Main › Stages: Findings | You chose 11. The walk along `requires` added 3: `db-migrate` and `postgres-mcp` for `migration-reviewer`, and `seed-data` for `db-migrate`. | **You added 11. 3 more were auto-added because another item `requires` them: `db-migrate` and `postgres-mcp` for `migration-reviewer`, and `seed-data` for `db-migrate`.** | body | all | product, with slots | D7 | D7: auto-added; the walk never on a screen |
| Run | Main › Stages: Findings | Declared conflicts | = | stage name | all | product |  |  |
| Run | Main › Stages: Findings | 1 problem | = | stage result | all | product |  |  |
| Run | Stages: Findings › Finding | Problem | = | severity | all | product |  |  |
| Run | Stages: Findings › Finding | `eslint-autofix` declares a conflict with `code-style`: it rewrites the imports that `code-style` tells the agent to keep. The archive will contain both, and the agent will get two rules that disagree. | = | state message | all | product, with slots |  |  |
| Run | Stages: Findings › Finding | Remove eslint-autofix | **Remove eslint-autofix…** | button | all | product, with slots | D20 D22 | Typography: `…` on a button that opens a confirmation (D20) |
| Run | Main › Stages: Findings | Command names | = | stage name | all | product |  |  |
| Run | Main › Stages: Findings | Skipped — no item declares a command | = | stage result | all | product |  |  |
| Run | Main › Stages: Findings | Target paths | = | stage name | all | product |  |  |
| Run | Main › Stages: Findings | Checked — no two items write to the same path | = | stage result | default · error-export · error-setup · loading-export · remove · success | product | D19 |  |
| Run | Main › Stages: Findings | Env keys | = | stage name | all | product |  |  |
| Run | Main › Stages: Findings | 1 note · 3 keys named | = | stage result | default · error-export · error-setup · loading-export · remove · success | product |  |  |
| Run | Stages: Findings › Finding | Note | = | severity | default · error-export · error-setup · loading-export · remove · success | product |  |  |
| Run | Stages: Findings › Finding | `DATABASE_URL` (postgres-mcp), `GITHUB_TOKEN` (github-mcp) and `SENTRY_AUTH_TOKEN` (sentry-mcp) are needed. They go into `.env.example` as names; the receiving machine supplies the values. | = | state message | default · error-export · error-setup · loading-export · remove · success | product, with slots | D18 |  |
| Run | Main › Stages: Findings | Deference | **Defers to** | stage name | all | product |  | Jargon: *deference* as a noun never on a screen |
| Run | Main › Stages: Findings | 1 note | = | stage result | default · error-export · error-setup · loading-export · remove · success | product |  |  |
| Run | Stages: Findings › Finding | `code-style` defers to the client’s ESLint config. Where they disagree, that wins. | = | state message | default · error-export · error-setup · loading-export · remove · success | product, with slots |  |  |
| Run | Main › Stages: Findings | Pinned refs | = | stage name | all | product |  |  |
| Run | Main › Stages: Findings | Checked — 3 external items, all pinned | = | stage result | default · error-export · error-setup · loading-export · remove · success | product | D19 |  |
| Run | Main › Stages: Handover — what the receiving machine still needs | Handover — what the receiving machine still needs | = | heading | all | product | D18 |  |
| Run | Main › Stages: Handover — what the receiving machine still needs | What the archive contains | = | stage name | all | product |  |  |
| Run | Main › Stages: Handover — what the receiving machine still needs | 18 files for Claude Code | = | stage result | default · error-export · error-setup · loading-export · remove · success | product |  |  |
| Run | Main › Stages: Handover — what the receiving machine still needs | acme-billing-api/<br>├── CLAUDE.md                       commit-conventions, api-contracts<br>├── SETUP.md<br>├── .env.example                    DATABASE_URL, GITHUB_TOKEN, SENTRY_AUTH_TOKEN<br>├── .mcp.json                       postgres-mcp, github-mcp, sentry-mcp<br>├── .claude/skills/code-style/SKILL.md<br>├── .claude/skills/changelog-writer/SKILL.md<br>├── .claude/agents/migration-reviewer.md<br>├── .claude/agents/acme-pr-reviewer.md     detached<br>├── .claude/agents/test-runner.md<br>└── scripts/  db-migrate.sh · seed-data.sh · eslint-autofix.sh · openapi-lint.sh | = | generated file | default · error-export · error-setup · loading-export · remove · success | generated | D8 |  |
| Run | Main › Stages: Handover — what the receiving machine still needs | SETUP.md — for the agent that opens it | = | stage name | all | product |  |  |
| Run | Main › Stages: Handover — what the receiving machine still needs | Written · 14 items | = | stage result | default · error-export · loading-export · remove · success | product |  |  |
| Run | Main › Stages: Handover — what the receiving machine still needs | # Setup — acme-billing-api (Claude Code)<br><br>Read this first and perform each step.<br><br>## postgres-mcp<br>- External. Clone modelcontextprotocol/servers-archived at 9be4674.<br>- Needs DATABASE_URL. Ask the person for it; do not invent one.<br>- Required by migration-reviewer.<br><br>## code-style<br>- Defers to the client’s ESLint config. Where they disagree, the ESLint config wins.<br>… | = | generated file | default · error-export · loading-export · remove · success | generated | L2 |  |
| Run | Main › Stages: Handover — what the receiving machine still needs | .env.example | = | stage name | all | product |  |  |
| Run | Main › Stages: Handover — what the receiving machine still needs | 3 keys, names only | = | stage result | default · error-export · error-setup · loading-export · remove · success | product |  |  |
| Run | Main › Stages: Handover — what the receiving machine still needs | DATABASE_URL=<br>GITHUB_TOKEN=<br>SENTRY_AUTH_TOKEN= | = | generated file | default · error-export · error-setup · loading-export · remove · success | generated |  |  |
| Run | Main › Export stage | 11 · Export | = | heading | default · error-check · error-setup · loading-export · loading · remove | product | D4 |  |
| Run | Main › Export stage | 1 problem is still in the set. The archive will contain both `eslint-autofix` and `code-style`, and the agent will get two rules that disagree about imports. | **1 problem is still in this project. The archive will contain both `eslint-autofix` and `code-style`, and the agent will get two rules that disagree about imports.** | state message | default · error-setup · remove | product, with slots | D6 | D6 |
| Run | Main › Export stage | Export with 1 problem | = | button | default · error-setup · remove | product | D4 |  |
| Run | Main › Export stage | Fix it in the project first | **Configure acme-billing-api** | button | default · error-setup · remove | product |  | Button: verb + object, the result visible — it opens the configuring mode |
| Run | Main › Verdict | The check didn’t finish | = | title | error-check | product |  |  |
| Run | Main › Verdict | The server stopped answering at stage 4 of 10. Nothing in the project changed; its last check still reads 2 days ago. | **Our server stopped answering at stage 4 of 10. Nothing in the project changed, and its last check still reads 2 days ago.** | state message | error-check | product | D9 | Dictionary: our failure (D9) |
| Run | Main › Verdict | 503 · Service unavailable · 14:05 | = | state message | error-check | product | D10 |  |
| Run | Main › Verdict | acme-billing-api · 14 items · for Claude Code | = | state message | error-check · loading | product, with slots |  |  |
| Run | Main › Stages: Findings | Didn’t complete | **Stopped — our server didn’t answer** | stage result | error-check | product | D23 | Dictionary: a stage that started and did not finish (D23) |
| Run | Main › Stages: Findings | Not run | = | stage result | error-check | product | D23 |  |
| Run | Main › Stages: Handover — what the receiving machine still needs | Not run | = | stage result | error-check | product | D23 |  |
| Run | Main › Export stage | The archive is built from a finished check. Checking again costs nothing. | = | state message | error-check | product |  |  |
| Run | Main › Export stage | Check again | = | button | error-check | product | D12 |  |
| Run | Main › Export stage | Back to acme-billing-api | = | button | error-check · error-export · success | product, with slots |  |  |
| Run | Main › Export stage | 11 · Export — the archive didn’t build | = | heading | error-export | product | D4 |  |
| Run | Main › Export stage | The server stopped at 12 of 18 files. Nothing was downloaded. The check above still stands — nothing in the set changed. | **Our server stopped at 12 of 18 files. Nothing was exported. The check above still stands — nothing in the project changed.** | state message | error-export | product | D6 D9 | Dictionary: our failure (D9); project, not set (D6); Step 7 #1 #3 D4 |
| Run | Main › Export stage | 503 · 14:07 | **503 · Service unavailable · 14:07** | state message | error-export | product | D10 | Dictionary: one form for the error code (D10); Step 7 #18/#19: the error code on its own line (D10) |
| Run | Main › Export stage | Build the archive again | **Export again** | button | error-export | product | D4 D12 | Dictionary: Export; retry names the verb (D4, D12) |
| Run | Main › Stages: Handover — what the receiving machine still needs | Couldn’t be written | **Stopped — our server didn’t answer** | stage result | error-setup | product | D23 | Dictionary: a stage that started and did not finish (D23) |
| Run | Stages: Handover — what the receiving machine still needs › Finding | Missing, not empty | = | status label | error-setup | product |  |  |
| Run | Stages: Handover — what the receiving machine still needs › Finding | `SETUP.md` couldn’t be produced — the server stopped while writing it. What you would read here is missing because something broke on our side, not because there is nothing to say (Q28). 503 · 14:06 | **`SETUP.md` wasn’t written — our server stopped while writing it. What you would read here is missing because our server failed, not because there is nothing to say.** | state message | error-setup | product, with slots | D9 D10 L1 | Forbidden: internal ids (L1); our failure (D9); the error code (D10); Step 7 #19: the error code moved to a line of its own (D10) |
| Run | Stages: Handover — what the receiving machine still needs › Finding | (added) | **503 · Service unavailable · 14:06** | state message | error-setup | product |  | Step 7 #18/#19: the error code on its own line (D10) |
| Run | Stages: Handover — what the receiving machine still needs › Finding | Write it again | **Write SETUP.md again** | button | error-setup | product | D12 | Dictionary: retry names the verb and its object (D12) |
| Run | Main › Export stage | Building the archive — 18 files for Claude Code | **Exporting — 18 files for Claude Code** | state message | loading-export | product |  | Dictionary: Export (D4); Loading: say what is loading |
| Run | Main › Export stage | acme-billing-api-claude-code.zip | = | state message | loading-export | product |  |  |
| Run | Main › Verdict | Checking — stage 4 of 10 | = | title | loading | product | D11 |  |
| Run | Main › Stages: Findings | Checking… | **Checking** | stage result | loading | product | D11 | Typography: `…` only on a button that opens a confirmation (D20); the glyph shows it is running |
| Run | Main › Stages: Findings | Waiting | = | stage result | loading | product | D23 |  |
| Run | Main › Stages: Handover — what the receiving machine still needs | Waiting | = | stage result | loading | product | D23 |  |
| Run | Main › Export stage | After the handover stages. | **Opens after the handover stages.** | state message | loading | product |  | Loading: the waiting stage says what will happen, not only where |
| Run | Modal: Remove eslint-autofix from acme-billing-api? | Remove eslint-autofix from acme-billing-api? | = | heading | remove | product, with slots |  |  |
| Run | Modal: Remove eslint-autofix from acme-billing-api? | It leaves this project only. It stays in My library and in the other projects that use it. | = | body | remove | product |  |  |
| Run | Modal: Remove eslint-autofix from acme-billing-api? | The check runs again as soon as it is removed. | = | fact | remove | product |  |  |
| Run | Modal: Remove eslint-autofix from acme-billing-api? | Cancel | = | button | remove | product | D16 |  |
| Run | Modal: Remove eslint-autofix from acme-billing-api? | Remove | **Remove from project** | button | remove | product | D22 | Dangerous action: the confirm button repeats the verb of the act (D22) |
| Run | Main › Export stage | Archive built — acme-billing-api-claude-code.zip | **Exported — acme-billing-api-claude-code.zip** | heading | success | product | D4 | Dictionary: it is built — *Exported* (D4) |
| Run | Main › Export stage | 18 files · 41 KB · saved to Downloads. Checked just now with 1 problem, 2 notes and 1 skipped. | **18 files · 41 KB · saved to Downloads. Checked just now · 1 problem · 2 notes · 1 skipped.** | state message | success | product | D19 | D19 |
| Run | Main › Export stage | The receiving machine still needs | = | state message | success | product | D18 |  |
| Run | Main › Export stage | Values for `DATABASE_URL`, `GITHUB_TOKEN` and `SENTRY_AUTH_TOKEN` | = | state message | success | product, with slots |  |  |
| Run | Main › Export stage | Three repos cloned at their pinned refs — `SETUP.md` says which | **3 repos cloned at their pinned refs — `SETUP.md` says which** | state message | success | product, with slots |  | Step 7 #14 numbers as digits |
| Run | Main › Export stage | An agent that reads `SETUP.md` first | = | state message | success | product, with slots |  |  |
| Run | Main › Export stage | Download again | = | button | success | product | D4 D12 |  |
| Run | Main › Export stage | Share the project | **Share…** | button | success | product | D21 | Dictionary: Share… opens the disclosure (D21, D20) |

### Run — a single item

State pages: `default` · `error` · `loading` · `success`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Run — a single item | Run bar | My library | = | link | all | product |  |  |
| Run — a single item | Run bar | Export one item | **Export** | title | all | product | D3 | D3, Q36 |
| Run — a single item | Run bar | Agent target | = | field label | all | product |  |  |
| Run — a single item | Run bar | Claude Code | = | option | all | product |  |  |
| Run — a single item | Run bar | Cursor | = | option | all | product |  |  |
| Run — a single item | Run bar | Codex | = | option | all | product |  |  |
| Run — a single item | Run bar | Universal | = | option | all | product |  |  |
| Run — a single item | Main › Verdict | Verdict | = | a11y label | all | product |  |  |
| Run — a single item | Main › Verdict | migration-reviewer, with the 3 items it brings | **Checked just now** | title | default · success | product, with slots | D7 | D19, D7; as the sample |
| Run — a single item | Main › Verdict | 0 problems · 1 note · 3 skipped | = | state message | default · success | product |  |  |
| Run — a single item | Main › Verdict | Checked just now · for Claude Code · nothing is saved from this check — there is no project to hold it | **migration-reviewer · 4 items · for Claude Code · nothing is saved from this check — there is no project to hold it** | state message | default · success | product | D19 | D3: subject in the meta line |
| Run — a single item | Main › Stages: Findings | Findings | = | heading | all | product |  |  |
| Run — a single item | Main › Stages: Findings | Resolve the set | **Requirements** | stage name | all | product | D6 | D6 |
| Run — a single item | Main › Stages: Findings | 4 items — migration-reviewer and the 3 it brings | **4 items · 3 auto-added** | stage result | all | product, with slots | D7 | D7 |
| Run — a single item | Main › Stages: Findings | `migration-reviewer` requires `db-migrate` and `postgres-mcp`, and `db-migrate` requires `seed-data`, so it exports as a set of 4, named as one. | **`migration-reviewer` requires `db-migrate` and `postgres-mcp`, and `db-migrate` requires `seed-data`, so 3 items are auto-added and all 4 export as one archive, named for migration-reviewer.** | body | all | product, with slots |  | D7, D4, D6 |
| Run — a single item | Main › Stages: Findings | Declared conflicts | = | stage name | all | product |  |  |
| Run — a single item | Main › Stages: Findings | Skipped — none declared | **Skipped — no item declares a conflict** | stage result | default · error · success | product |  | Step 7 #6 one Skipped form |
| Run — a single item | Main › Stages: Findings | Command names | = | stage name | all | product |  |  |
| Run — a single item | Main › Stages: Findings | Skipped — no item declares a command | = | stage result | default · error · success | product |  |  |
| Run — a single item | Main › Stages: Findings | Target paths | = | stage name | all | product |  |  |
| Run — a single item | Main › Stages: Findings | Checked — no two items write to the same path | = | stage result | default · success | product | D19 |  |
| Run — a single item | Main › Stages: Findings | Env keys | = | stage name | all | product |  |  |
| Run — a single item | Main › Stages: Findings | 1 note | = | stage result | default · success | product |  |  |
| Run — a single item | Stages: Findings › Finding | Note | = | severity | default · success | product |  |  |
| Run — a single item | Stages: Findings › Finding | `DATABASE_URL` (postgres-mcp) goes into `.env.example` as a name. | = | state message | default · success | product, with slots |  |  |
| Run — a single item | Main › Stages: Findings | Deference | **Defers to** | stage name | all | product |  | jargon |
| Run — a single item | Main › Stages: Findings | Skipped — nothing defers | **Skipped — no item defers to anything** | stage result | default · success | product |  | Skipped form |
| Run — a single item | Main › Stages: Findings | Pinned refs | = | stage name | all | product |  |  |
| Run — a single item | Main › Stages: Findings | Checked — postgres-mcp pinned at 9be4674 | = | stage result | default · success | product, with slots | D19 |  |
| Run — a single item | Main › Stages: Handover — what the receiving machine still needs | Handover — what the receiving machine still needs | = | heading | all | product | D18 |  |
| Run — a single item | Main › Stages: Handover — what the receiving machine still needs | What the archive contains | = | stage name | all | product |  |  |
| Run — a single item | Main › Stages: Handover — what the receiving machine still needs | 4 files for Claude Code | **8 files for Claude Code** | stage result | default · success | product |  | Step 7 #21 U3 count matches the tree |
| Run — a single item | Main › Stages: Handover — what the receiving machine still needs | migration-reviewer/<br>├── SETUP.md<br>├── .env.example        DATABASE_URL<br>├── .mcp.json           postgres-mcp<br>├── .claude/agents/migration-reviewer.md<br>└── scripts/  db-migrate.sh + 2 files · seed-data.sh | = | generated file | default · success | generated |  |  |
| Run — a single item | Main › Stages: Handover — what the receiving machine still needs | SETUP.md — for the agent that opens it | = | stage name | all | product |  |  |
| Run — a single item | Main › Stages: Handover — what the receiving machine still needs | Written · 4 items | = | stage result | default · success | product |  |  |
| Run — a single item | Main › Stages: Handover — what the receiving machine still needs | .env.example | = | stage name | all | product |  |  |
| Run — a single item | Main › Stages: Handover — what the receiving machine still needs | 1 key, name only | = | stage result | default · success | product |  |  |
| Run — a single item | Main › Export stage | 11 · Export | = | heading | default · loading | product | D4 |  |
| Run — a single item | Main › Export stage | 4 items as one archive, for Claude Code. | = | state message | default | product |  |  |
| Run — a single item | Main › Export stage | Export | = | button | default | product | D4 |  |
| Run — a single item | Main › Verdict | The check didn’t finish | = | title | error | product |  |  |
| Run — a single item | Main › Verdict | migration-reviewer · 4 items · for Claude Code | = | state message | error | product, with slots |  |  |
| Run — a single item | Main › Stages: Findings | Stopped — the server didn’t answer | **Stopped — our server didn’t answer** | stage result | error | product | D9 D23 | D9, D23 |
| Run — a single item | Stages: Findings › Finding | This is our failure, not the item’s | = | status label | error | product | D9 |  |
| Run — a single item | Stages: Findings › Finding | The server stopped during this stage. Nothing was exported, and nothing is known about the stages after it. | **Our server stopped during this stage. Nothing was exported, and nothing in My library changed. The stages after it didn’t run.** | state message | error | product | D9 | D9; Error: what did not change |
| Run — a single item | Stages: Findings › Finding | (added) | **503 · Service unavailable · 14:04** | state message | error | product |  | Step 7 #18/#19: the error code on its own line (D10) |
| Run — a single item | Stages: Findings › Finding | Check again | = | button | error | product | D12 |  |
| Run — a single item | Stages: Findings › Finding | Back to My library | = | button | error | product |  |  |
| Run — a single item | Main › Stages: Findings | Not run | = | stage result | error | product | D23 |  |
| Run — a single item | Main › Stages: Handover — what the receiving machine still needs | Not run | = | stage result | error | product | D23 |  |
| Run — a single item | Main › Verdict | Checking migration-reviewer — stage 2 of 10 | **Checking — stage 2 of 10** | title | loading | product, with slots | D11 | D11 |
| Run — a single item | Main › Verdict | 4 items · for Claude Code | **migration-reviewer · 4 items · for Claude Code** | state message | loading | product |  | meta as in the sample |
| Run — a single item | Main › Stages: Findings | Checking… | **Checking** | stage result | loading | product | D11 | D20 |
| Run — a single item | Main › Stages: Findings | Waiting | = | stage result | loading | product | D23 |  |
| Run — a single item | Main › Stages: Handover — what the receiving machine still needs | Waiting | = | stage result | loading | product | D23 |  |
| Run — a single item | Main › Export stage | After the handover stages. | **Opens after the handover stages.** | state message | loading | product |  | Loading |
| Run — a single item | Main › Export stage | Archive built — migration-reviewer-claude-code.zip | **Exported — migration-reviewer-claude-code.zip** | heading | success | product | D4 | D4 |
| Run — a single item | Main › Export stage | 4 files · 9 KB · saved to Downloads. Checked just now with 0 problems, 1 note and 3 skipped. Nothing is saved from this check. | **8 files · 9 KB · saved to Downloads. Checked just now · 0 problems · 1 note · 3 skipped. Nothing is saved from this check.** | state message | success | product | D19 | D19; Step 7 #21 U3 |
| Run — a single item | Main › Export stage | The receiving machine still needs | = | state message | success | product | D18 |  |
| Run — a single item | Main › Export stage | A value for `DATABASE_URL` | = | state message | success | product, with slots |  |  |
| Run — a single item | Main › Export stage | `modelcontextprotocol/servers-archived` cloned at `9be4674` — `SETUP.md` says how | = | state message | success | product, with slots |  |  |
| Run — a single item | Main › Export stage | Back to My library | = | button | success | product |  |  |
| Run — a single item | Main › Export stage | Download again | = | button | success | product | D4 D12 |  |

### Shared project

State pages: `default` · `error` · `loading`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Shared project | Shared header | AI Stack Builder | = | body | all | product |  |  |
| Shared project | Shared header | Shared by Maya Chen | = | body | default | product, with slots |  |  |
| Shared project | Main › Page head | agent-dotfiles | = | title | default | user |  |  |
| Shared project | Main › Page head | 9 items | = | fact | default | product |  |  |
| Shared project | Main › Page head | Changed 1 day ago | = | fact | default | product |  |  |
| Shared project | Main › Page head | Maya last checked it 5 days ago, for Claude Code — the set has changed since | **Maya checked it 5 days ago · for Claude Code — the project has changed since** | fact | default | product, with slots | D6 D19 | D19, D6 |
| Shared project | Main › Page head | Copy into my library | **Copy to My library** | button | default | product | D1 D5 | D1, D5 |
| Shared project | Main › Page head | Check this set | **Export…** | button | default | product | D6 | D3, Q36 |
| Shared project | Main | My everyday setup across machines: commit conventions, the review subagent, the filesystem and memory MCP servers. | = | description | default | user |  |  |
| Shared project | Main › What the set contains | What the set contains | **What this project contains** | a11y label | default · loading | product | D6 | D6 |
| Shared project | What the set contains › Row | commit-conventions | = | item name | default | user |  |  |
| Shared project | What the set contains › Row | prompt | = | kind badge | default | product |  |  |
| Shared project | What the set contains › Row | Conventional commits, imperative mood, and a body that says why. | **Conventional commits, imperative mood, and a body that says why rather than what.** | description | default | user |  | Step 7 #22 U1 |
| Shared project | What the set contains › Row | Maya’s own | = | fact | default | product, with slots |  |  |
| Shared project | What the set contains › Row | pr-reviewer | = | item name | default | user |  |  |
| Shared project | What the set contains › Row | agent | = | kind badge | default | product |  |  |
| Shared project | What the set contains › Row | Reads a pull request diff and leaves review comments. | **Reads a pull request diff and leaves review comments the way I would write them.** | description | default | user |  | Step 7 #22 U1 |
| Shared project | What the set contains › Row | Requires `github-mcp` | = | panel row line | default | product, with slots |  |  |
| Shared project | What the set contains › Row | code-style | = | item name | default | user |  |  |
| Shared project | What the set contains › Row | skill | = | kind badge | default | product |  |  |
| Shared project | What the set contains › Row | How TypeScript is written: naming, imports, error handling. | **How I want TypeScript written: naming, imports, error handling, no default exports.** | description | default | user |  | Step 7 #22 U1 |
| Shared project | What the set contains › Row | Defers to the client’s ESLint config — where they disagree, that wins | = | panel row line | default | product, with slots |  |  |
| Shared project | What the set contains › Row | github-mcp | = | item name | default | user |  |  |
| Shared project | What the set contains › Row | mcp | = | kind badge | default | product |  |  |
| Shared project | What the set contains › Row | Issues, pull requests and code search on GitHub. | **Issues, pull requests and code search on GitHub, through GitHub’s own server.** | description | default | user |  | Step 7 #22 U1 |
| Shared project | What the set contains › Row | Needs `GITHUB_TOKEN` · auto-added — required by `pr-reviewer` | **Needs `GITHUB_TOKEN` · auto-added for `pr-reviewer`** | panel row line | default | product, with slots | D7 | D7 |
| Shared project | What the set contains › Row | `github/github-mcp-server` @ `v0.9.0` · MIT | = | fact | default | user |  |  |
| Shared project | What the set contains › Row | filesystem | = | item name | default | user |  |  |
| Shared project | What the set contains › Row | Read and write files inside the directories you allow. | **Read and write files inside the directories you allow, and nowhere else.** | description | default | user |  | Step 7 #22 U1 |
| Shared project | What the set contains › Row | `modelcontextprotocol/servers` @ `2025.9.25` · MIT | = | fact | default | user |  |  |
| Shared project | What the set contains › Row | memory | = | item name | default | user |  |  |
| Shared project | What the set contains › Row | A knowledge graph the agent writes to and reads back. | **A knowledge graph the agent can write to and read back between sessions.** | description | default | user |  | Step 7 #22 U1 |
| Shared project | What the set contains › Row | session-notes | = | item name | default | user |  |  |
| Shared project | What the set contains › Row | Keeps a running log of decisions in `NOTES.md` at the end of each session. | = | description | default | user |  |  |
| Shared project | What the set contains › Row | Requires `memory` | = | panel row line | default | product, with slots |  |  |
| Shared project | What the set contains › Row | shell-safety | = | item name | default | user |  |  |
| Shared project | What the set contains › Row | Never run destructive commands without saying what they delete first. | = | description | default | user |  |  |
| Shared project | What the set contains › Row | dotfiles-sync | = | item name | default | user |  |  |
| Shared project | What the set contains › Row | script | = | kind badge | default | product |  |  |
| Shared project | What the set contains › Row | Links the agent config into `~/.claude` on a new machine. | = | description | default | user |  |  |
| Shared project | Main | What your machine will need | **What your machine still needs** | heading | default | product | D18 | D18 |
| Shared project | Main | A value for `GITHUB_TOKEN` | = | body | default | product, with slots |  |  |
| Shared project | Main | 3 external items, cloned from 2 repos at pinned refs — `SETUP.md` in the archive says which | = | body | default | product, with slots |  |  |
| Shared project | Main | An agent that reads `SETUP.md` first | = | body | default | product, with slots |  |  |
| Shared project | Main | This page is live: it shows the set as Maya has it now. An archive you take is a snapshot of this moment. | **This page is live — it shows the project as Maya has it now. An archive you export is a snapshot of this moment.** | fact | default | product, with slots | D6 | D6, D4 |
| Shared project | Main | Check it, then take the archive | **Export…** | button | default | product | D4 | D3, D4, Q36 |
| Shared project | Main › State block | This link doesn’t open anything any more | = | a11y label | error | product |  |  |
| Shared project | Main › State block | This link doesn’t open anything any more | = | heading | error | product |  |  |
| Shared project | Main › State block | The person who shared this project turned the link off, or deleted the project. Ask them for a new link. If you already downloaded an archive from it, that copy is still yours. | **The person who shared this project turned the link off, or deleted the project. Ask them for a new link. If you already exported an archive or copied items from it, those are still yours.** | state message | error | product |  | D4; Error: what did not change |
| Shared project | Main | Opening the shared project | **Loading the shared project** | body | loading | product | D11 | D11 |

### Run — a shared project

State pages: `default` · `error` · `loading` · `success`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Run — a shared project | Shared header | AI Stack Builder | = | body | all | product |  |  |
| Run — a shared project | Shared header | Shared by Maya Chen | = | body | all | product, with slots |  |  |
| Run — a shared project | Run bar | agent-dotfiles | = | link | all | user |  |  |
| Run — a shared project | Run bar | Check | **Export** | title | all | product | D3 | D3, Q36 |
| Run — a shared project | Run bar | Agent target | = | field label | all | product |  |  |
| Run — a shared project | Run bar | Claude Code | = | option | all | product |  |  |
| Run — a shared project | Run bar | Cursor | = | option | all | product |  |  |
| Run — a shared project | Run bar | Codex | = | option | all | product |  |  |
| Run — a shared project | Run bar | Universal | = | option | all | product |  |  |
| Run — a shared project | Main › Verdict | Verdict | = | a11y label | all | product |  |  |
| Run — a shared project | Main › Verdict | Checked just now, by you | **Checked just now by you** | title | default · success | product | D19 | D19 |
| Run — a shared project | Main › Verdict | 0 problems · 2 notes · 1 skipped | = | state message | default · success | product |  |  |
| Run — a shared project | Main › Verdict | agent-dotfiles, as it is now · 9 items · for Claude Code · nothing is saved from this check | = | state message | default · success | product, with slots |  |  |
| Run — a shared project | Main › Stages: Findings | Findings | = | heading | all | product |  |  |
| Run — a shared project | Main › Stages: Findings | Resolve the set | **Requirements** | stage name | all | product | D6 | D6 |
| Run — a shared project | Main › Stages: Findings | 9 items · 2 auto-added · no cycles | = | stage result | all | product | D7 |  |
| Run — a shared project | Main › Stages: Findings | Declared conflicts | = | stage name | all | product |  |  |
| Run — a shared project | Main › Stages: Findings | Checked — none found | = | stage result | all | product | D19 |  |
| Run — a shared project | Main › Stages: Findings | Command names | = | stage name | all | product |  |  |
| Run — a shared project | Main › Stages: Findings | Skipped — no item declares a command | = | stage result | default · error · success | product |  |  |
| Run — a shared project | Main › Stages: Findings | Target paths | = | stage name | all | product |  |  |
| Run — a shared project | Main › Stages: Findings | Checked — no two items write to the same path | = | stage result | default · error · success | product | D19 |  |
| Run — a shared project | Main › Stages: Findings | Env keys | = | stage name | all | product |  |  |
| Run — a shared project | Main › Stages: Findings | 1 note | = | stage result | default · success | product |  |  |
| Run — a shared project | Stages: Findings › Finding | Note | = | severity | default · success | product |  |  |
| Run — a shared project | Stages: Findings › Finding | Your machine needs a value for `GITHUB_TOKEN` (github-mcp). The archive carries only its name. | = | state message | default · success | product, with slots | D18 |  |
| Run — a shared project | Main › Stages: Findings | Deference | **Defers to** | stage name | all | product |  | jargon |
| Run — a shared project | Stages: Findings › Finding | `code-style` defers to the client’s ESLint config. Where they disagree, that wins. | = | state message | default · success | product, with slots |  |  |
| Run — a shared project | Main › Stages: Findings | Pinned refs | = | stage name | all | product |  |  |
| Run — a shared project | Main › Stages: Findings | Checked — 3 external items, all pinned | = | stage result | default · success | product | D19 |  |
| Run — a shared project | Main › Stages: Handover — what the receiving machine still needs | Handover — what the receiving machine still needs | **Handover — what your machine still needs** | heading | all | product | D18 | D18 (receiver) |
| Run — a shared project | Main › Stages: Handover — what the receiving machine still needs | What the archive contains | = | stage name | all | product |  |  |
| Run — a shared project | Main › Stages: Handover — what the receiving machine still needs | 13 files for Claude Code | = | stage result | default · success | product |  |  |
| Run — a shared project | Main › Stages: Handover — what the receiving machine still needs | SETUP.md — for the agent that opens it | = | stage name | all | product |  |  |
| Run — a shared project | Main › Stages: Handover — what the receiving machine still needs | Written · 9 items | = | stage result | default · success | product |  |  |
| Run — a shared project | Main › Stages: Handover — what the receiving machine still needs | .env.example | = | stage name | all | product |  |  |
| Run — a shared project | Main › Stages: Handover — what the receiving machine still needs | 1 key, name only | = | stage result | default · success | product |  |  |
| Run — a shared project | Main › Export stage | 11 · Take the archive | **11 · Export** | heading | default · loading | product | D4 | D4 |
| Run — a shared project | Main › Export stage | A snapshot of agent-dotfiles as it is now. The shared page may change after you take it. | **The archive is a snapshot of agent-dotfiles as it is now. The shared page may change after you export it.** | state message | default | product, with slots |  | D4 |
| Run — a shared project | Main › Export stage | Download the archive | **Export** | button | default | product | D4 | D4 |
| Run — a shared project | Main › Verdict | The check didn’t finish | = | title | error | product |  |  |
| Run — a shared project | Main › Verdict | agent-dotfiles · 9 items · for Claude Code | = | state message | error | product, with slots |  |  |
| Run — a shared project | Main › Stages: Findings | Stopped — the server didn’t answer | **Stopped — our server didn’t answer** | stage result | error | product | D9 D23 | D9, D23 |
| Run — a shared project | Stages: Findings › Finding | This is our failure, not the set’s | **This is our failure, not the project’s** | status label | error | product | D6 D9 | D6 |
| Run — a shared project | Stages: Findings › Finding | Our server stopped during this stage. It says nothing about whether agent-dotfiles holds together. Nothing was downloaded. | **Our server stopped during this stage. It says nothing about agent-dotfiles itself. Nothing was exported.** | state message | error | product, with slots | D9 | Step 7 #1 #3 D4; Step 7 #2 jargon (cohere) |
| Run — a shared project | Stages: Findings › Finding | (added) | **503 · Service unavailable · 14:08** | state message | error | product |  | Step 7 #18/#19: the error code on its own line (D10) |
| Run — a shared project | Stages: Findings › Finding | Check again | = | button | error | product | D12 |  |
| Run — a shared project | Stages: Findings › Finding | Back to the shared page | **Back to the shared project** | button | error | product |  | Back to + the place by name, as Back to the shared item |
| Run — a shared project | Main › Stages: Findings | Not run | = | stage result | error | product | D23 |  |
| Run — a shared project | Main › Stages: Handover — what the receiving machine still needs | Not run | = | stage result | error | product | D23 |  |
| Run — a shared project | Main › Verdict | Checking agent-dotfiles — stage 3 of 10 | **Checking — stage 3 of 10** | title | loading | product, with slots | D11 | D11 |
| Run — a shared project | Main › Verdict | 9 items · for Claude Code | **agent-dotfiles · 9 items · for Claude Code** | state message | loading | product |  | meta as in the sample |
| Run — a shared project | Main › Stages: Findings | Checking… | **Checking** | stage result | loading | product | D11 | D20 |
| Run — a shared project | Main › Stages: Findings | Waiting | = | stage result | loading | product | D23 |  |
| Run — a shared project | Main › Stages: Handover — what the receiving machine still needs | Waiting | = | stage result | loading | product | D23 |  |
| Run — a shared project | Main › Export stage | After the handover stages. | **Opens after the handover stages.** | state message | loading | product |  | Loading |
| Run — a shared project | Main › Export stage | Archive downloaded — agent-dotfiles-claude-code.zip | **Exported — agent-dotfiles-claude-code.zip** | heading | success | product | D4 | D4 |
| Run — a shared project | Main › Export stage | 13 files · 22 KB. A snapshot of the set as it was a minute ago, checked by you with 0 problems and 2 notes. | **13 files · 22 KB. A snapshot of agent-dotfiles as it was a minute ago. Checked just now by you · 0 problems · 2 notes · 1 skipped.** | state message | success | product | D6 D19 | D6, D19 |
| Run — a shared project | Main › Export stage | Your machine still needs | = | state message | success | product | D18 |  |
| Run — a shared project | Main › Export stage | A value for `GITHUB_TOKEN` | = | state message | success | product, with slots |  |  |
| Run — a shared project | Main › Export stage | An agent that reads `SETUP.md` first — it clones the 2 external repos — 3 items — at their pinned refs | **An agent that reads `SETUP.md` first. It clones 2 repos at their pinned refs, for the 3 external items** | state message | success | product, with slots |  | Typography: one separator per job |
| Run — a shared project | Main › Export stage | Back to the shared page | **Back to the shared project** | button | success | product |  | Back to + the place by name, as Back to the shared item |
| Run — a shared project | Main › Export stage | Copy into a library of my own | **Copy to My library** | button | success | product | D1 D5 | D1, D5 |

### Shared item

State pages: `default` · `error` · `loading`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Shared item | Shared header | AI Stack Builder | = | body | all | product |  |  |
| Shared item | Shared header | Shared by Maya Chen | = | body | default | product, with slots |  |  |
| Shared item | Main › Page head | code-style | = | title | default | user |  |  |
| Shared item | Main › Page head | skill | = | kind badge | default | product |  |  |
| Shared item | Main › Page head | Written by Maya Chen — her own, not from an external source | **Written by Maya Chen, not from an external source** | fact | default | product, with slots |  | Step 7 #10 no pronoun guessed from a name |
| Shared item | Main › Page head | Changed 2 days ago | = | fact | default | product |  |  |
| Shared item | Main › Page head | Copy into my library | **Copy to My library** | button | default | product | D1 D5 | D5, D1 |
| Shared item | Main › Page head | Take as an archive | **Export…** | button | default | product | D4 | D3, D4, Q36 |
| Shared item | Main | Content · lands at `.claude/skills/code-style/SKILL.md` | = | heading | default | product, with slots |  |  |
| Shared item | Main | ---<br>name: code-style<br>description: How TypeScript is written in my projects.<br>---<br>- Named exports only. No default exports.<br>- Imports: node built-ins, then packages, then local — one blank line between groups.<br>- Errors: throw typed errors from lib code; catch only at the edge.<br>- Names say what a thing is, not what type it is: `invoices`, not `invoiceArray`. | = | generated file | default | user |  |  |
| Shared item | Main | What it needs, and what it answers to | = | heading | default | product |  |  |
| Shared item | Main | Requires nothing else | = | body | default | product |  |  |
| Shared item | Main | No env keys | = | body | default | product |  |  |
| Shared item | Main | Defers to the client’s ESLint config — where they disagree, that wins | = | body | default | product, with slots |  |  |
| Shared item | Main | This page is live: it shows the item as Maya has it now. | **This page is live — it shows the item as Maya has it now.** | fact | default | product, with slots |  | Step 7 #9 typography |
| Shared item | Main › State block | This link doesn’t open anything any more | = | a11y label | error | product |  |  |
| Shared item | Main › State block | This link doesn’t open anything any more | = | heading | error | product |  |  |
| Shared item | Main › State block | The person who shared this item turned the link off, or deleted the item. Ask them for a new link. If you already downloaded an archive from it, that copy is still yours. | **The person who shared this item turned the link off, or deleted the item. Ask them for a new link. If you already exported it or copied it to My library, that copy is still yours.** | state message | error | product |  | D4, D5; Error: what did not change |
| Shared item | Main | Opening the shared item | **Loading the shared item** | body | loading | product | D11 | D11 |

### Run — a shared item

State pages: `default` · `error` · `loading` · `success`

| Screen | Zone | Was | Now | Type | On | Whose | Mark | Why |
|---|---|---|---|---|---|---|---|---|
| Run — a shared item | Shared header | AI Stack Builder | = | body | all | product |  |  |
| Run — a shared item | Shared header | Shared by Maya Chen | = | body | all | product, with slots |  |  |
| Run — a shared item | Run bar | code-style | = | link | all | user |  |  |
| Run — a shared item | Run bar | Take as an archive | **Export** | title | all | product | D3 | D3, Q36 |
| Run — a shared item | Run bar | Agent target | = | field label | all | product |  |  |
| Run — a shared item | Run bar | Claude Code | = | option | all | product |  |  |
| Run — a shared item | Run bar | Cursor | = | option | all | product |  |  |
| Run — a shared item | Run bar | Codex | = | option | all | product |  |  |
| Run — a shared item | Run bar | Universal | = | option | all | product |  |  |
| Run — a shared item | Main › Verdict | Verdict | = | a11y label | all | product |  |  |
| Run — a shared item | Main › Verdict | code-style, checked by you | **Checked just now by you** | title | default · success | product, with slots | D19 | D19 |
| Run — a shared item | Main › Verdict | 0 problems · 1 note · 5 skipped | = | state message | default · success | product |  |  |
| Run — a shared item | Main › Verdict | Just now · for Claude Code · shared by Maya Chen · nothing is saved from this check | **code-style · 1 item · for Claude Code · shared by Maya Chen · nothing is saved from this check** | state message | default · success | product, with slots | D19 | D19: subject in the meta line |
| Run — a shared item | Main › Stages: Findings | Findings | = | heading | all | product |  |  |
| Run — a shared item | Main › Stages: Findings | Resolve the set | **Requirements** | stage name | all | product | D6 | D6 |
| Run — a shared item | Main › Stages: Findings | 1 item — code-style requires nothing | = | stage result | all | product, with slots |  |  |
| Run — a shared item | Main › Stages: Findings | Declared conflicts | = | stage name | all | product |  |  |
| Run — a shared item | Main › Stages: Findings | Skipped — one item has nothing to conflict with | = | stage result | all | product |  |  |
| Run — a shared item | Main › Stages: Findings | Command names | = | stage name | all | product |  |  |
| Run — a shared item | Main › Stages: Findings | Skipped — no command declared | **Skipped — no item declares a command** | stage result | all | product |  | Step 7 #6 one Skipped form |
| Run — a shared item | Main › Stages: Findings | Target paths | = | stage name | all | product |  |  |
| Run — a shared item | Main › Stages: Findings | Checked — one path | **Checked — 1 path** | stage result | default · success | product | D19 | Typography: digits |
| Run — a shared item | Main › Stages: Findings | Env keys | = | stage name | all | product |  |  |
| Run — a shared item | Main › Stages: Findings | Skipped — none needed | **Skipped — no item needs an env key** | stage result | default · success | product |  | Step 7 #7 one Skipped form |
| Run — a shared item | Main › Stages: Findings | Deference | **Defers to** | stage name | all | product |  | jargon |
| Run — a shared item | Main › Stages: Findings | 1 note | = | stage result | default · success | product |  |  |
| Run — a shared item | Stages: Findings › Finding | Note | = | severity | default · success | product |  |  |
| Run — a shared item | Stages: Findings › Finding | `code-style` defers to the client’s ESLint config. Where they disagree, that wins — on your machine too. | = | state message | default · success | product, with slots | D18 |  |
| Run — a shared item | Main › Stages: Findings | Pinned refs | = | stage name | all | product |  |  |
| Run — a shared item | Main › Stages: Findings | Skipped — no repo attached | = | stage result | default · success | product |  |  |
| Run — a shared item | Main › Stages: Handover — what your machine still needs | Handover — what your machine still needs | = | heading | all | product | D18 |  |
| Run — a shared item | Main › Stages: Handover — what your machine still needs | What the archive contains | = | stage name | all | product |  |  |
| Run — a shared item | Main › Stages: Handover — what your machine still needs | 2 files for Claude Code | = | stage result | default · success | product |  |  |
| Run — a shared item | Main › Stages: Handover — what your machine still needs | code-style/<br>├── SETUP.md<br>└── .claude/skills/code-style/SKILL.md | = | generated file | default · success | generated |  |  |
| Run — a shared item | Main › Stages: Handover — what your machine still needs | SETUP.md — for the agent that opens it | = | stage name | all | product |  |  |
| Run — a shared item | Main › Stages: Handover — what your machine still needs | Written · 1 item | = | stage result | default · success | product |  |  |
| Run — a shared item | Main › Stages: Handover — what your machine still needs | .env.example | = | stage name | all | product |  |  |
| Run — a shared item | Main › Stages: Handover — what your machine still needs | Skipped — no keys | = | stage result | default · success | product |  |  |
| Run — a shared item | Main › Export stage | 11 · Take the archive | **11 · Export** | heading | default · loading | product | D4 | D4 |
| Run — a shared item | Main › Export stage | A snapshot of `code-style` as it is now. The shared page may change after you take it. | **A snapshot of `code-style` as it is now. The shared page may change after you export it.** | state message | default | product, with slots |  | D4 |
| Run — a shared item | Main › Export stage | Download the archive | **Export** | button | default | product | D4 | D4 |
| Run — a shared item | Main › Verdict | The check didn’t finish | = | title | error | product |  |  |
| Run — a shared item | Main › Verdict | code-style · 1 item · for Claude Code | = | state message | error | product, with slots |  |  |
| Run — a shared item | Main › Stages: Findings | Stopped — the server didn’t answer | **Stopped — our server didn’t answer** | stage result | error | product | D9 D23 | D9, D23 |
| Run — a shared item | Stages: Findings › Finding | This is our failure, not the item’s | = | status label | error | product | D9 |  |
| Run — a shared item | Stages: Findings › Finding | Our server stopped during this stage. It says nothing about `code-style` itself. Nothing was downloaded. | **Our server stopped during this stage. It says nothing about `code-style` itself. Nothing was exported.** | state message | error | product, with slots | D9 | Step 7 #1 #3 D4 |
| Run — a shared item | Stages: Findings › Finding | (added) | **503 · Service unavailable · 14:12** | state message | error | product |  | Step 7 #18/#19: the error code on its own line (D10) |
| Run — a shared item | Stages: Findings › Finding | Check again | = | button | error | product | D12 |  |
| Run — a shared item | Stages: Findings › Finding | Back to the shared item | = | button | error | product |  |  |
| Run — a shared item | Main › Stages: Findings | Not run | = | stage result | error | product | D23 |  |
| Run — a shared item | Main › Stages: Handover — what your machine still needs | Not run | = | stage result | error | product | D23 |  |
| Run — a shared item | Main › Verdict | Checking code-style — stage 4 of 10 | **Checking — stage 4 of 10** | title | loading | product, with slots | D11 | D11 |
| Run — a shared item | Main › Verdict | 1 item · for Claude Code | **code-style · 1 item · for Claude Code** | state message | loading | product |  | meta as in the sample |
| Run — a shared item | Main › Stages: Findings | Checking… | **Checking** | stage result | loading | product | D11 | D20 |
| Run — a shared item | Main › Stages: Findings | Waiting | = | stage result | loading | product | D23 |  |
| Run — a shared item | Main › Stages: Handover — what your machine still needs | Waiting | = | stage result | loading | product | D23 |  |
| Run — a shared item | Main › Export stage | After the handover stages. | **Opens after the handover stages.** | state message | loading | product |  | Loading |
| Run — a shared item | Main › Export stage | Archive downloaded — code-style-claude-code.zip | **Exported — code-style-claude-code.zip** | heading | success | product | D4 | D4 |
| Run — a shared item | Main › Export stage | 2 files · 3 KB. A snapshot of the item as it was a minute ago, checked by you with 0 problems and 1 note. | **2 files · 3 KB · saved to Downloads. A snapshot of the item as it was a minute ago. Checked just now by you · 0 problems · 1 note · 5 skipped.** | state message | success | product | D19 | D19 |
| Run — a shared item | Main › Export stage | Your machine still needs | = | state message | success | product | D18 |  |
| Run — a shared item | Main › Export stage | An agent that reads `SETUP.md` first | = | state message | success | product, with slots |  |  |
| Run — a shared item | Main › Export stage | To know that the client’s ESLint config wins where it disagrees with this skill | **The client’s ESLint config, which wins where it disagrees with this skill** | state message | success | product, with slots |  | Step 7 #13 a thing the machine needs |
| Run — a shared item | Main › Export stage | Back to the shared item | = | button | success | product |  |  |
| Run — a shared item | Main › Export stage | Copy into a library of my own | **Copy to My library** | button | success | product | D1 D5 | D1, D5 |
