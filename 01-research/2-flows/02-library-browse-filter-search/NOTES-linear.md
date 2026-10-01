# Command palette, filters and search — Linear, captured 2026-09-01

The benchmark this flow has been waiting for. Taken in the owner's signed-in Linear workspace,
read-only: nothing created, edited or deleted, and the filters applied here are transient view state
encoded in the URL.

**Caveat, stated plainly.** The workspace holds four issues. Everything below is about the *mechanics*
of browsing — the palette, the filter grammar, the empty results — and none of it is about behaviour
at scale. Density under load remains uncaptured, and no longer looks likely to be.

Companion: [`08-empty-state-and-cold-start/NOTES-linear.md`](../08-empty-state-and-cold-start/NOTES-linear.md).

---

## 1. The palette is one input with three jobs

`linear-command-palette-default.jpg`, `linear-command-palette-search-results.jpg`

`Ctrl K` opens a single field whose placeholder is *"Type a command or search…"* — commands and
content share one entrance. Opened cold it lists **actions grouped by object type**, each group
labelled, each row carrying its shortcut on the right:

```
Issues      Create new issue…              C
            Create issue in fullscreen…    V
            Create new label…
Projects    Create new project…            N then P
Documents   Create new document in…
Views       Create view…
```

Type text and the same field becomes search: a group headed **`Quick results for "import"`** — the
query is quoted back into the heading — then the matches, then a persistent row:

> 🔍 **Search entire workspace**  *import*

That row is the third job: **widen the scope without losing what you typed.** The palette starts
narrow and offers the escalation instead of guessing.

Two more details worth taking:

- **`Ask Linear  Tab`** sits at the top right of the field throughout — the AI escape hatch is
  bound to a key, present but not occupying a row.
- Opened from an issue, the palette shows a **context chip** above the input (`ROM-1 · Get familiar
  with Linear`) — the palette states what it is scoped to rather than leaving you to infer it.

## 2. The hint bar adapts to what is currently possible

Under the results sits a row of keyboard hints. With results:

`↵ Open` · `Advanced search Ctrl /` · `Alt ↵ More actions` · `Quick look →`

With no results, it shrinks to the two that still apply:

`↵ Select` · `Advanced search Ctrl /`

The affordance list is **computed from the current state**, not a static footer. This is the same
principle as suppressing a toolbar over an empty screen, applied to keyboard hints.

## 3. The no-results state is the next action

`linear-command-palette-no-results.jpg`

> 🔍 **No results found**  *Go to advanced search*

One row. The message and the remedy are the same object — the row that reports the failure is the row
you press to escape it. No illustration, no separate panel, no "try a different search term".

## 4. The filter picker is itself a command palette

`linear-add-filter-menu.jpg`

Pressing `F` opens **`Add Filter…`**, a typeahead — not a dropdown of checkboxes. Under it, the
dimensions grouped by separator: issue attributes (Status, Assignee, Creator, Priority, Labels,
Relations, Dates…), then Project, then meta (Subscribers, Auto-closed, Content, Links, Template).
`AI filter` and `Advanced filter` sit above everything.

**And typing flattens the tree into breadcrumbs** — `linear-filter-typeahead-breadcrumbs.jpg`. Typing
`urgent` returns:

```
Priority › Urgent
Project properties › Project priority › Urgent
AI filter  "urgent"
```

You never navigate the submenus; the **path is displayed rather than traversed**, which is also what
disambiguates two leaves that share a name. Our Library has exactly that collision waiting — a tag and
a kind could both be called `mcp` — and this solves it without a nested menu.

## 5. Filters read as sentences, and clear and save sit together

`linear-filtered-to-zero-hidden-count.jpg`

An applied filter becomes a chip built as subject–verb–object with its own remove control:

> `▮ Priority` **is** `❗Urgent` **✕**

At the right end of the bar, two words: **`Clear`** and **`Save`**. Discard the filter, or promote it
into a saved View — the ad-hoc and the durable version of the same thing, one click apart, at equal
weight. That is the cheapest possible route from "I filtered something" to "I have a view", and it is
what our Library needs between a filtered library and a saved Project.

The filter state is encoded in the URL, so a narrowed library is linkable.

**One honest blemish:** the same filter applied twice produced two identical chips. Linear does not
dedupe. Worth not copying.

## 6. The best thing on this screen: the count of what is hidden

When the filter matches nothing:

> **No issues matching the filters**
>
> **4 issues** hidden by filters · **Clear Filters ✕**

It distinguishes *"there is nothing"* from *"there is something and you are not looking at it"*, and
it does so with a **number**. Then it offers the single action that undoes the cause.

Our Library will be filtered to zero constantly — six kinds, arbitrary tags, a search box. Saying
"No items" there would be a lie. It has to say **how many exist behind the filter**, and offer one
click back.

## 7. Straight into our design

1. **One palette, three jobs**: commands, content search, and an explicit widen-the-scope row.
2. **Quote the query back** in the results heading.
3. **Keyboard hints computed from state**, not a fixed footer.
4. **The no-results row is the next action.**
5. **The filter picker is a typeahead, and typing flattens the hierarchy into breadcrumbs.**
6. **A filter chip is a sentence** with its own ✕; `Clear` and `Save` share the same corner.
7. **Never say "nothing here" when the answer is "nothing matching".** Count what is hidden.
