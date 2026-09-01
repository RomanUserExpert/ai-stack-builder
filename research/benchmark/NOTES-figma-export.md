# Figma's export dialog — a disabled primary action, sign-posted

Captured 2026-09-01 in the owner's own Figma desktop file (`UIR - LIB - Design System`), driven from
this session **by keyboard only** — `Esc` to deselect, `Ctrl Shift E` to open the dialog, `Esc` to
close. Nothing was clicked on the canvas, nothing selected, nothing exported, nothing changed.

`figma-export-empty-selection.png`

## What it shows

With nothing selected, the Export dialog is four elements:

```
Export                                                    ✕
☑  0 of 0 selected                              [ Export ]   ← greyed
   No selected layers have export settings. Click + in the
   export section of the properties panel to add one.
```

**A counted checkbox** — `0 of 0 selected` — in the same grammar as VS Code's `Showing 0 of 6`
([`NOTES-vscode.md`](NOTES-vscode.md)). **A disabled primary action.** And **a sentence that names
the remedy and its location**: not *"nothing to export"* but *where the missing setting is added*,
by control (`+`) and by panel (the export section of the properties panel).

## Why it matters to us, and it is not the obvious reason

CLAUDE.md §6 decided that **export is never disabled** — that a permanently greyed primary action is
a dead end, and that an unclean set is confirmed rather than refused. Here is the world's best design
tool doing the opposite on the same control, which deserves an honest reading rather than a
dismissal.

**The disabled button is tolerable here because of three properties we do not have:**

1. **The blocker is one action away, and the sentence says which one.** The dialog is not a dead end;
   it is a signpost with a greyed button attached.
2. **The condition is momentary.** Select a layer with export settings and it lights up. It is not a
   property of the document, it is a property of this second's selection.
3. **The act is repeatable and free.** Exporting a PNG again costs nothing, so refusing once costs
   nothing either.

Our Export has none of the three. A Problem in a set is a property of the project, not of a
selection; the fix may be four items away in the library; and the user is trying to get an archive
onto another machine, which is the whole point of the product. A greyed Export would be a dead end on
the load-bearing control, which is why §6 stands.

**What we take instead is the sentence.** Figma's refusal is legible because it names the remedy and
its location in one line. Our confirmation dialog owes the same: not *"this project has problems"*
but *"Two items write to `.mcp.json`. The archive will contain only one of them — `db-tools`."* —
and, on the row, where to go and what to press.

## And the count

`0 of 0 selected` is the third appearance of the same idiom in this benchmark — VS Code's
`Showing 0 of 6`, Linear's `4 issues hidden by filters`, this. Three unrelated products, one grammar:
**the number you can act on, next to the control that produced it.**
