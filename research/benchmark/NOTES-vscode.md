# VS Code — B1, B2 and B3 in one product

Captured 2026-09-01 on a VS Code installed the same day, driven from this session: the window was
brought to the foreground, keys were sent to it, and each frame was taken from the window's own
rectangle. No account was signed into. The workspace is a three-file fixture written for this
capture, outside the repo, carrying our three findings on purpose:

| Our finding | What the fixture plants |
|---|---|
| Two items declare the same MCP server key | `.mcp.json` with `postgres` twice, plus a trailing comma |
| A field that is not in the model | `detached: true` on an object typed as `Item` |
| A required item that is not in the set | a reference to `local_file`-style `collectTargets`, undeclared |

Eleven frames, in [`.`](.): `vscode-*.png`.

---

## B1 — Find

### The palette is one field with a mode character

`vscode-palette-default.png` · `vscode-palette-query.png` · `vscode-palette-no-results.png`

`F1` opens a field prefixed **`>`**. The prefix is the grammar: `>` commands, nothing files, `@`
symbols, `:` a line number. The mode is a visible character in the input rather than a tab or a
segmented control, so switching mode is editing text.

Opened cold on a fresh install it is **the entire command list, alphabetically, from
`Accounts: Manage Accounts`**. No grouping by object, no counts, no context chip. Linear's palette
opens on actions grouped and labelled by object type
([`../flows/02-library-browse-filter-search/NOTES-linear.md`](../flows/02-library-browse-filter-search/NOTES-linear.md));
VS Code opens on an index. Keybindings render as key caps down the right in both.

Typing narrows, and **the matched substrings are bold inside each row** — `toggle secondary` bolds
*Toggle*, *Secondary* and *Side Bar* separately in `View: Toggle Secondary Side Bar Visibility`. You
can see *why* a row is in the list, which is the part Linear replaces with grouping.

The empty result is one row and it is inert:

> **No matching commands**

No query quoted back, no widening offered, nothing to press. Compare Linear — *"No results found ·
Go to advanced search"*, where the row that reports the failure is the row that escapes it — and
Obsidian, which does not report a failure at all
([`NOTES-obsidian.md`](NOTES-obsidian.md)). Of the three, this is the weakest dead end in the
benchmark.

### The marketplace card is the trust signal we decided not to ship

`vscode-extensions-search.png` · `vscode-extensions-recommended.png`

Searching `mcp server` returns cards carrying, in this order: icon, name, **download count**
(`1.4M`, `215K`, `27K`, `4K`), **star rating**, one-line description, publisher with a **verified
tick**, and `Install`.

Two rows down the list the ratings read `5` on a 4K-download extension and `1` on a 33K one. The
signal is strong at the head and noise in the tail — and the tail is where a personal library lives.
This is the concrete argument behind CLAUDE.md §5: the market's trust apparatus is downloads plus
stars plus a verified publisher, we have none of the three, and inventing a number to stand in their
place would be decoration.

---

## B2 — Assemble

### Workspace Trust is the best consequence disclosure in this benchmark

`vscode-workspace-trust.png` · `vscode-workspace-trust-granted.png`

Two columns, side by side, headed **In a Trusted Folder** and **In Restricted Mode**. The state you
are actually in is the one with the border. Each column is four lines with a ✓ or an ✕ — glyph first,
so colour is redundant — and two of the four are **counted and hyperlinked**:

> ✕ **95 workspace settings** are not applied
> ✕ **10 extensions** are disabled or have limited functionality

That beats Figma's *423 instances* on the one axis Figma leaves open: the number is a **link to the
list**. You are told the size of the consequence and can go read exactly what it consists of before
deciding. And the button carries its shortcut inside it — `Trust`, with `Ctrl+Enter` beneath — the
same trick as Linear's `Create new project  N then P`.

**The way back is the same control, relabelled.** After trusting, the heading becomes *"You trust
this folder"*, the border moves to the left column, and the button in the identical position reads
**`Don't Trust`**. No second screen, no settings page, no hunt. Our detach/reset pair and our export
confirmation both want this shape.

### The recommendation set is a file with a view over it

`vscode-extensions-recommended.png`

`@recommended` splits into **Workspace Recommendations** (3) and **Other Recommendations** (4), each
counted in the section header. Beside the first heading sit two icons: install-all, and a **pencil
that opens `.vscode/extensions.json`** — the file the list is read from. The set is authored as text
and rendered as a list, and the UI says so by putting the way into the text one click from the way
into the list.

That is prior art for stage 5's **P3 (Document)** variant, and it is the moderate version of it: the
manifest is the source of truth, the panel is a view, and neither pretends to be the only way in.

**One thing it gets wrong, and it is the notification.** The prompt that fires on opening the folder
reads:

> Do you want to install the recommended extensions from **Prettier, Microsoft and others** for this
> repository?

It names **publishers**, not extensions. The file lists three extensions by id; the notification
turns them into two brand names and an "and others". The disclosure exists at the wrong grain — and
the correct grain was sitting in the file it just read.

### Two granularities, named — and the affordance rule breaks here

`vscode-extension-context-menu.png`

Right-click on an extension:

```
Enable                    (greyed)
Enable (Workspace)        (greyed)
Disable
Disable (Workspace)
Install Specific Version… (greyed)
Uninstall                 (greyed)
Copy / Copy Extension ID
Settings
```

**Global and per-workspace are both named, in the same menu, in a matched pair.** That is our library
edit versus our per-project override, and the naming convention — the narrower scope in parentheses
after the same verb — is worth copying outright.

But the pair that cannot act is **greyed, not hidden**, and so are `Uninstall` and `Install Specific
Version…` on a built-in. This benchmark had recorded *"an action that cannot act is not shown"* as
settled at four to one. It is not settled: it is settled **for primary surfaces** — toolbars, empty
states, panels — and reversed in **context menus**, where a stable item order is worth more than a
short list, because people reach for position before they read. Both halves are real, and the split
runs along the genre of the surface.

The detail pane beside it does the other half of the job in a sentence: *"This extension is bundled
with Visual Studio Code. It can be disabled but not uninstalled."* The constraint is stated in words
next to the greyed control that embodies it.

---

## B3 — Check

`vscode-problems-panel.png` · `vscode-problems-json.png` · `vscode-problems-filtered-zero.png`

### Counts at four altitudes, and they agree

Status bar `⊗ 4  ⚠ 2` · panel badge `Problems 6` · per-file badge `3` and `3` · the editor tab
carrying `3` next to the filename · a dot on the parent folder in the explorer. The same number,
rendered at every altitude the reader might be looking at, from the whole workspace down to one tab.

Severity has its own glyph, errors sort above warnings, and each file is a collapsible group.

### The anatomy of a row

```
Trailing comma            json(519)  [Ln 9, Col 38]
Duplicate object key      json(520)  [Ln 3, Col 5]
Duplicate object key      json(520)  [Ln 7, Col 5]

Object literal may only specify known properties, and 'detached' does not exist
in type 'Item'.           ts(2353)   [Ln 14, Col 66]
  Argument of type 'Item | undefined' is not assignable to parameter of type 'Item'.
    Type 'undefined' is not assignable to type 'Item'.
Cannot find name 'collectTargets'.   ts(2304)  [Ln 26, Col 24]
```

Message, **rule code**, **line and column**. The rule code is the part most validators drop, and it
is what makes a problem searchable and suppressible. The nested row under `ts(2345)` carries the
underlying cause a level down — consequence outside, cause inside, expandable.

And a **lightbulb replaces the severity glyph on the row where a Quick Fix exists**. The remedy is
offered on the problem, and its absence on the other rows is information too.

### The duplicate key: the same defect, twice, unjoined

Our exact case — `postgres` declared twice in `.mcp.json` — produces **two independent warnings**, at
`Ln 3` and `Ln 7`. Neither mentions the other. Nothing says which one wins.

`terraform validate` on the equivalent config says it in one message:
*"A local_file resource named "manifest" was already declared at main.tf:10,1-33"*
([`terraform-validate-errors.md`](terraform-validate-errors.md)). One finding, both locations, the
rule, and the resolution order implied by which one it calls the earlier.

For us this is settled by the pair: **a collision is one Problem naming every participant**, not one
row per participant. VS Code's shape is what you get when the checker reports positions; Terraform's
is what you get when it reports defects.

### Filtered to zero, and it is the Linear behaviour

`vscode-problems-filtered-zero.png`

Typing a filter that matches nothing puts a badge **inside the input** —

> `Showing 0 of 6`

— and one line below it:

> No results found with provided filter criteria. **Clear Filters**.

The count of what is hidden, and the remedy as a link. Linear does the same thing on a filtered issue
list and puts the count in the empty state; VS Code puts it in the input, where the cause is. Two
independent products, same decision, and CLAUDE.md's Library needs it on day one: **never say
"nothing" when the answer is "nothing matching".**

---

## Straight into our design

1. **A mode character in the search field**, not a tab strip, if the Library's one input is to do
   more than one job.
2. **Bold the matched substring** so a row explains its own presence in the list.
3. **Never ship `No matching commands`.** The dead end is the one thing all three B1 candidates
   answer differently, and VS Code's answer is the one to reject.
4. **Consequence as two columns with counted, clickable lines** — the shape of our unclean-export
   confirmation.
5. **The way back is the same control, relabelled and in the same place.**
6. **Scope in parentheses after the verb**: `Disable` and `Disable (Workspace)`.
7. **The affordance rule has a genre exception.** Hide what cannot act on primary surfaces; grey it
   in context menus, where position is the interface.
8. **Every finding carries a rule code**, not only a sentence.
9. **One collision is one Problem naming both sides**, never two rows that never meet.
10. **The count of what is hidden goes in the input**, next to the thing that hid it.
