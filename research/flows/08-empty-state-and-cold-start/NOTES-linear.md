# Cold start — Linear, captured 2026-09-01

The gap the research had carried since the beginning: *"A genuine first-run empty state from anyone.
Every capture we have is of a full system."* Taken in the owner's own signed-in Linear workspace
(`romanovcharenko`), which turned out to be **brand new** — four onboarding issues and nothing else.

Read-only. Nothing was created, edited, assigned, completed or deleted. One account setting — the
interface theme — was changed to capture flow 10 and restored to its original value
(`System preference`); see [`../10-dark-design-language/NOTES-linear.md`](../10-dark-design-language/NOTES-linear.md).

**The trade.** An empty workspace cannot show density under load, so flow 10 loses that. In exchange
it hands us the one thing no populated system could: the real first five minutes.

---

## 1. The answer to cold start is not an empty state. It is four real objects.

`linear-first-run-seeded-issues.jpg`

A new Linear workspace does not open on an illustration inviting you to create your first issue. It
opens on the **Issues list, already populated**, with four issues that are real in every respect —
IDs `ROM-1` … `ROM-4`, a `Todo` group with a count of 4, statuses, dates:

- **Get familiar with Linear**
- **Set up your teams**
- **Connect your tools**
- **Import your data**

They are ordinary issues. You can complete them, reorder them, delete them. The onboarding checklist
*is* the data model, exercised on itself. You learn what an issue is by having four of them, and the
product is never empty at any point.

`linear-issue-detail-light.jpg` — opening `ROM-1` shows the same: a normal issue whose description
happens to be a welcome video and a set of setup guides branched by company size.

**This is the sharpest answer yet to CLAUDE.md §11.** Our known problem is that an empty library kills
the product because there is nothing to validate. The plan has been "~30 realistic items for the
demo". Linear suggests something stronger for the real product: **ship a handful of genuine Items in a
genuine Project, and let the first validation pass run on them.** Not sample data behind a "load
demo content" button — the user's first library, which they can edit or throw away. The wow moment
then happens before the user has typed anything.

There is a second, smaller version of the same idea in the sidebar: a **`Try`** section holding
`Import issues`, `Invite people`, `Connect GitHub` — the setup actions live *in the navigation*, as
a labelled, evidently temporary group, rather than in a banner that has to be dismissed.

## 2. Three registers of emptiness, and the rule that picks between them

Linear does not have "an empty state". It has three, and which one appears depends on **why** the
screen is empty.

| | Screen | What it shows |
|---|---|---|
| **Concept you may never have used** | `linear-projects-empty-state.jpg`, `linear-views-empty-state.jpg` | Isometric line illustration · the object's name as the heading · **a definition, not an apology** · primary action **with its keyboard shortcut inside the button** · a `Documentation` link |
| **Routine, temporary emptiness** | `linear-my-issues-empty-state.jpg` | One line — *"No issues assigned to you"* — and one button. No illustration, no explanation |
| **Emptied by the user's own filter** | `linear-filtered-to-zero-hidden-count.jpg` | *"No issues matching the filters"* plus **"4 issues hidden by filters · Clear Filters ✕"** |

**The rule: verbosity scales with the chance that the reader does not know what the object is.**
"My issues" is empty for a reason you already understand, so it says almost nothing. "Projects" may be
a word you have never used in this product, so it defines itself:

> Projects are larger units of work with a clear outcome, such as a new feature you want to ship.
> They can be shared across multiple teams and are comprised of issues and optional documents.

That is a definition of the concept, written for someone deciding whether they need it. Our `Project`
and our six `kind`s need exactly this treatment, and it is cheap: one paragraph per object, written
once, shown only when there is nothing else to show.

**The Views empty state goes one better** and teaches the *other* way in:

> You can also save any existing view by clicking the ◈ icon or by pressing `Alt V`.

The empty state does not only offer the create button — it tells you the shortcut that turns work you
are already doing into the object. Our Library's empty state should say the equivalent: that a project
you have assembled can be saved, and how.

## 3. The shortcut lives inside the button

`Create new project` carries `N then P` **inside the button itself**, styled as two key caps. Not a
tooltip, not a help page, not a hint that appears after you have already clicked. The moment you are
most likely to press the button is the moment you are taught how never to need it again.

This is how a keyboard-first product bootstraps its own keyboard use, and it costs nothing.

## 4. The toolbar disappears when it cannot do anything

The Projects empty state carries **one tab and two icons** — nothing else. Compare the flaw recorded
in [`../07-env-and-secrets/NOTES.md`](../07-env-and-secrets/NOTES.md): Vercel's env-variables empty
state keeps a search box and four filter dropdowns on screen, all filtering nothing.

Same situation, opposite decision. Linear is right. Our Library empty state suppresses search,
kind filters and tag filters until there is something for them to act on.

## 5. What to carry into design

1. **Seed the library.** A few real Items in a real Project on first run, editable and deletable —
   not a demo mode. The validation pass should have something to validate on day one.
2. **Write one definition per object.** `Item`, `Project`, and each of the six kinds. Shown in the
   empty state, reused in tooltips.
3. **Three empty states, not one.** Never-used concept → define it. Routine emptiness → one line.
   Filtered to nothing → **say how many are hidden and offer one click back.**
4. **Put shortcuts in buttons.**
5. **Setup actions go in the navigation as a labelled temporary group**, not in a dismissible banner.
6. **Suppress controls that cannot act.**
