# Obsidian — B1, and the one product that refuses to report a failure

Captured 2026-09-01 on an Obsidian installed the same day, driven from this session. **Not in the
owner's own vault.** A scratch vault was assembled from this repository's own markdown — 27 notes in
their real folders, with their real names and cross-links — and Obsidian was pointed at it by
swapping `obsidian.json`, with the original backed up and **restored afterwards**; the app was
restarted on the owner's vault and left as it was found.

That substitution is the point, not a workaround. The plan's B1 question is *find one thing in a
large personal collection*, and a vault holding one `Welcome.md` cannot answer it. A vault holding
`research/flows/04-validation-check-results/NOTES-vercel.md` next to nine other `NOTES` files can.

Five frames, beside this file: `obsidian-*.png`.

---

## 1. The switcher matches paths, and shows its work

`obsidian-quick-switcher.png` · `obsidian-quick-switcher-query.png`

`Ctrl O` opens one field. Its placeholder is **"Find or create a note…"** — both jobs stated in the
placeholder, before you type anything.

Typing `notes` returns rows that are **full paths with every matched character bolded across the
whole path**:

```
research/flows/12-visibility-and-portfolio/NOTES
research/flows/09-duplicate-and-fork/NOTES
research/flows/04-validation-check-results/NOTES-port
research/flows/10-dark-design-language/NOTES-linear
…
research/flows/09-duplicate-and-fork/notion-move-destination-picker.jpg
research/flows/04-validation-check-results/github-actions-failed-job-steps.png
```

The list degrades visibly. Contiguous matches on the filename come first; by the bottom you are
looking at `notion-move-destination-picker` matching *n-o-t-e-s* scattered across a filename. **You
can see the quality gradient**, because the bolding shows which characters earned each row its place.

Two consequences for our Library:

- **The path is the disambiguator.** Nine files named `NOTES` are told apart by the folder they sit
  in, and the folder is on the row. Our items will collide by name across kinds and projects the same
  way, and the answer is the same: show the container, not a tooltip.
- **There is no count, no scope indicator, no filter.** You cannot tell whether you are seeing five
  matches or fifty, or how much of the vault is behind the fold. Linear counts what its filters hide;
  VS Code writes `Showing 0 of 6` inside the input; the switcher says nothing at all.

## 2. Zero results is not a failure. It is the create row.

`obsidian-quick-switcher-no-match.png`

Type something that matches nothing and the list does not empty. It shows **one row containing your
query**, with `Enter to create` on the right:

```
noteszzqqxx                                              Enter to create
↑↓ to navigate  ↵ to open  ctrl ↵ to open in new tab  shift ↵ to create  esc to dismiss
```

There is no "no results" message anywhere. The dead end has been designed out: the thing you could
not find becomes the thing you are one keystroke from making.

**This is the strongest C4 in the benchmark**, and it beats Linear's *"No results found · Go to
advanced search"* on the same axis Linear already wins — the row that would report the failure is the
row that resolves it — by removing the report entirely.

**And it is the weakest C3, for exactly the same reason.** A typo renders as a plausible row. Press
Enter and you own a note called `noteszzqqxx`. The interface never says *nothing matched*, so it
cannot distinguish *this does not exist* from *you mistyped*, and it resolves the ambiguity in favour
of creating a file. The full-text search pane, one pane away, says **`0 results · No matches found.`**
plainly — so the product knows how to say it and chooses not to, here.

For us the trade is instructive and the answer is a split: **an empty Library search should offer to
create the item, and should still say that nothing matched.** Both, in that order. The two are not
alternatives; Obsidian merely treats them as though they were.

## 3. The search pane is the counted half of the same product

`obsidian-search-operators.png` · `obsidian-search-zero.png`

`Ctrl Shift F` opens full-text search, and everything missing from the switcher is here:

- **`path:flows collision` — operators, and the operator's effect is visible**: `flows` is
  highlighted inside every result path, so you can see the filter acting on the data rather than
  taking its word for it.
- **`6 results`** above the list, a **per-file match count** badge (`2`), and a sort control
  (`File name (A to Z)`).
- **The matching line is quoted with the term highlighted**, so a result is judged without opening
  it.
- Zero matches reads `0 results` and `No matches found.` — flat, honest, and no create offer, because
  this pane is not a creation surface.

Two surfaces, two philosophies, one product: the switcher optimises for the next keystroke, the
search pane for the evidence. Our Library needs both behaviours and should not have to pick — the
palette can create, the list must count.

## 4. Economy

`obsidian-quick-switcher.png`

The empty tab is three lines, each an action with its shortcut inline: `Create new note (Ctrl + N)` ·
`Go to file (Ctrl + O)` · `Close`. No illustration, no toolbar, no filter chrome over nothing. The
hint bar under the switcher lists five modifiers and what each does.

One blemish, and it is the same class of mistake this research has been tallying: in the **no-match**
state the hint bar still advertises `↵ to open`, and there is nothing to open. Four of the five hints
recompute correctly; one does not.

---

## Straight into our design

1. **Show the container on the row.** Nine identically named things are told apart by their path,
   inline, not on hover.
2. **Bold the matched characters** so the ranking explains itself and the tail is visibly the tail.
3. **Offer to create from an empty search — and still say nothing matched.** Obsidian proves the
   offer works and that dropping the report is what it costs.
4. **A find surface that cannot count is a find surface you cannot trust at 300 items.** The switcher
   is exemplary at 27 notes and mute about scale.
5. **Recompute every hint, not most of them.**
