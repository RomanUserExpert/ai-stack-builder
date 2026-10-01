# Duplicate and fork — captured 2026-08-31

From the owner's signed-in Notion and GitHub. **Nothing was created or submitted:** the fork form
was opened and left, the Notion move-picker was opened and cancelled with Escape.

## GitHub — "Create a new fork"

`github-create-fork-form.jpg`

This is our "duplicate a project" screen, already solved by someone else. What it asks, in order:

1. **Owner** — a dropdown, because the copy has to land somewhere.
2. **Repository name** — prefilled with the original name, with **live availability checking**
   underneath: "✓ typescript-action is available." One line, immediate, no submit needed.
3. A sentence explaining the default: "By default, forks are named the same as their upstream
   repository. You can customize the name to distinguish it further."
4. **Description** — prefilled from the original, with a `84 / 350 characters` counter.
5. **Copy the `main` branch only** — checked by default. The scope reducer: take the useful part,
   not everything.
6. A quiet status line: "You are creating a fork in your personal account."
7. One primary button, **Create fork**.

Worth stealing wholesale: prefilled-but-editable name, live availability, the one-line explanation
of what the default does, and a checkbox that narrows what gets copied. Our duplicate dialog has the
same job — name the copy, say where it goes, decide whether detached items come across as detached
or get re-linked.

## Notion — duplication as a menu item, not a screen

`notion-page-menu-duplicate.jpg`

Duplicate sits in the page's ••• menu with a shortcut, `Ctrl+D`, between "Copy page contents" and
"Move to". There is no dialog at all — the copy appears next to the original. Notion's bet is that
duplication is so routine it should not cost a screen.

Two different philosophies, then: GitHub gives duplication a form because the copy leaves your
hands; Notion gives it a keystroke because the copy stays in your workspace. **Ours is the Notion
case** — a duplicated project stays in the same single-user library — which argues for a keystroke
and an inline rename, not a modal.

## Notion — the destination picker

`notion-move-destination-picker.jpg`

Opened via "Move to". A search field, a "Suggested" section, then the teamspace tree, and a
workspace switcher pinned at the bottom. Search-first, hierarchy second. If our projects ever
acquire folders, this is the reference.
