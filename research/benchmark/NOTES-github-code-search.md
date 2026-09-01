# GitHub code search — the counted rail, and the teaching dead end

Captured 2026-09-01 in Chrome, anonymously, on a public repository
(`modelcontextprotocol/servers`). Two queries, both read-only: one that matches, one that cannot.

`github-code-search-results.jpg` · `github-code-search-no-results.jpg`

---

## 1. Everything about the result set is stated before the results

```
10 files (324 ms) in [ modelcontextprotocol/servers ✕ ]
```

Three facts in one line: **how many**, **how long it took**, and **what the scope was** — the scope
as a chip with its own ✕, exactly Linear's grammar for a filter. Elapsed time is unusual and worth
noting: it is the only product in this benchmark that tells you the search itself was cheap, which is
what stops you wondering whether it finished.

## 2. The rail counts the doors you did not open

```
Code            10
Issues         204
Pull requests  125
Discussions      0
Commits         14
Packages         0
Wikis            0
```

The left rail counts **every other kind of result for the same query**, including the zeros. You are
not told only what is here; you are told what is *elsewhere*, and where there is nothing. `Issues 204`
next to `Code 10` reroutes you before you have read a single result.

Below it, facets computed from the result set rather than from a fixed taxonomy — **Languages**
(Markdown, JSON, each with its colour dot) and **Paths** (`src/`, `src/fetch/`, `src/memory/`…),
each with `More…`. The filters offered are the ones that would actually cut *this* set.

**This is the answer to our Library's filter panel.** Six kinds and arbitrary tags, and the panel
should show what each option would leave — the dimensions that can still cut, with their counts,
computed from what is currently on screen.

## 3. Per-file: a count, and truncation that says how much it hid

Each file group carries its path, a language badge, and a **match count** (`5`, `3`, `2`). The
snippets show line numbers with the term highlighted, and long lists end in

> **Show 3 more matches**

— truncation with a number rather than a scroll. Vercel does the same thing inside a build log
(`└ [+9 more paths]`). Our Result screen renders the archive's file tree, and it needs exactly this:
cut it short, say by how much.

## 4. Zero results: a lesson where a remedy should be

> ### Your search did not match any code
> You could try one of the tips below.
>
> ▸ Search across repositories ▸ Search across an organization ▸ Find a particular file extension
> ▸ **Why wasn't my code found?** ▸ Regular expressions ▸ Saved searches

Six collapsed tips and an illustration occupying half the viewport. It is the most *educational*
empty state in the benchmark — one of the accordions is literally the question the user is asking —
and the least *actionable*.

Because the one control that would fix this search is not in the list. The result was narrowed by
`repo:modelcontextprotocol/servers`, and the way out is the **✕ on the scope chip at the top of the
page**, which the tips never mention. Linear, in the same situation, prints *"4 issues hidden by
filters · Clear Filters ✕"* — the cause, the size of what it hid, and the undo, in one line.

Note also what the rail does here: **every count goes to zero**. That is genuinely useful — no
issues, no PRs, no discussions match either, so the term is absent from the whole repository rather
than just from its code. The rail earns its place on an empty page, which is not something this
research has been able to say about any other toolbar over an empty list.

---

## Straight into our design

1. **Count, cost and scope in one line above the results**, the scope as a removable chip.
2. **Count what is behind the doors you are not looking through**, including the zeros.
3. **Facets computed from the current result set**, not a fixed list of every dimension.
4. **Truncate with a number**: *Show 3 more matches*, never a silent cut.
5. **An empty state teaches or it acts — and if it only teaches, put the undo where the cause is.**
   Six tips are worth less than one chip with an ✕.
