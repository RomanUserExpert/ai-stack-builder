# Critique — personas and jobs, every claim checked against its source

**Stage 6 step 4 and stage 7 step 6, merged into one document at the owner's request. Written
2026-09-08.** Sits at the research root because it spans two stages. Audits
[`6-personas/personas.md`](6-personas/personas.md) and
[`7-jobs-to-be-done/jtbd.md`](7-jobs-to-be-done/jtbd.md), both written 2026-09-08 and never audited
before. **Nothing in either file was edited.** Corrections are proposed in the *Note* column and
nowhere else.

**The rule applied**, from [`research.md`](research.md), *The three marks*: `✓` is earned only by an
instrument another person can re-run; `*` is one respondent's memory about their own work and, since
there has been exactly one interview, **every `*` in the repository is n = 1**; an unmarked sentence
is being asserted as `✓`. Rule 5 governs the hardest cases: a re-runnable query proves that
something was **said**, not that it is **true**.

**What was actually re-run for this audit.** Every reaction count in both documents was looked up
in [`3-pain/_user-pain-issues.json`](3-pain/_user-pain-issues.json) or
[`6-personas/_captures/round1-github.json`](6-personas/_captures/round1-github.json); every quoted issue body was
searched in the latter; every Hacker News quote was searched by item id in
[`_captures/round1-hn-threads.json`](6-personas/_captures/round1-hn-threads.json) and
[`_captures/round1-hn.json`](6-personas/_captures/round1-hn.json); the portfolio search was re-run over the
1,762 comments; the feature-name test was re-run over every job clause in `jtbd.md`; every interview
quote was matched to its question in [`interviews.md` interview 1](6-personas/interviews.md#part-2-interview-1-of-5);
every `M`, `V` and `E` citation was opened in its flow note, the benchmark, the comparison or the
post-mortem; and the marks on each persona card were counted.

**What could not be verified either way, stated once so it is not repeated in every row.**
The star counts in R8 (the web log lists repository names and no figures); the point totals for
three of the four evaluation stories under EJ-3 (only *AGENTS.md outperforms skills*, 524, is in a
log); the *25 comments about symlinking* (a hand count — the log yields 29 comments containing
*symlink*, 19 of which also name `AGENTS.md` or `CLAUDE.md`); the interview's *30-minute* duration
(the guide budgets it; the interview file does not record it); and four of the quoted HN commenters
— **eternityforest, freakynit, type4, israrkhan** — who appear in no capture log and only in
`re-research.md`'s prose. Each of those is marked *URL-only* below rather than *Invented*, because the
URL can be visited; but they fail the repository's own standard that every number in `re-research.md`
is reproducible from its logs.

**Classification** is one of three: **Confirmed** — a source in this repository supports it at the
strength claimed; **Hypothesis** — plausible, and the source establishes something narrower, or the
claim is `*` and reads as general; **Invented** — no source, or the cited source does not say this,
including a number that does not match, a misattributed quote, a superlative the data refutes, a
mark the register withdrew, or an inference written as an observation.

---

# Part 1 — Every factual claim, classified

## `personas.md`

### Header and axes

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| P-01 | The evidence base: two trackers (182 records); `anthropics/claude-code` 89,923 issues, `openai/codex` 26,451, `google-gemini/gemini-cli` 14,163; 1,762 HN comments from eight threads; Stack Overflow; a GitHub repository search; ~140 captured frames; one 30-minute conversation | Header, *The evidence base* | `re-research.md` | **Confirmed** | 1,762 is the sum of the eight thread logs (381+210+245+162+28+290+258+188); the tracker totals are the gh log's `CC.top-all` and I2 queries; `research.md` counts 143 captures. The *30-minute* duration is the guide's budget, not recorded in the interview file. |
| P-02 | Reddit is "named across community surveys as where this population actually talks" and blocks the crawler | Header | R13 | **Hypothesis** | The block is stated in `re-research.md` §1. The web log holds **one** community survey (daily.dev), so "across community surveys" is plural on one source. |
| P-03 | `*` is n = 1 everywhere in this file | Header | — | **Confirmed** | One interview filed. |
| P-04 | §3's audience sentence is the owner's assertion, A-4 and A-5, under test | Header, *Why there are no names* | `inventory.md` B | **Confirmed** | |
| P-05 | P1's X2 end: "two to four, kept in sync by hand" | Axes table | `inventory.md` §D | **Hypothesis** | The count is seven people's self-description (NK-5, re-marked `*`). "By hand" is loose: R2's own workarounds are symlinks and scripts, and the respondent has a bootstrap script (Q3) and still copies with `cp -r` (Q7). |
| P-06 | P2's X2 end: "usually a different one from the author's" | Axes table | — | **Invented** | No instrument measured frequency. One filer's motive (#6235) says collaborators use other tools. Correction: `[?]`, "one filed motive says so". |
| P-07 | P2's standing: "`✓` at population" | Axes table | R12 | **Hypothesis** | The population `✓` rests on #6235, #10238, #28729 — all filed by **authors** on teams; no receiver wrote any of them. And #6235 is the same issue that anchors P1's X2 end, so P1 and P2 share their loudest `✓`. Correction: "`✓` that authors report others opening their material". |
| P-08 | P3 is "the persona the spec already ships for and nobody has met" | Axes table | X4 | **Confirmed** | X4's end B is `V` only; the P5 recruit has not happened. |

### P1 — Context

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| P-09 | They copied one file into a second project, a third, and made a repository at the fourth | P1 §1 | `*` Q4 | **Confirmed** `*` | Verbatim in Q4. Hypothesis about anyone else. |
| P-10 | "Fourteen months later it holds **20 to 40 items**" | P1 §1 | `✓` #28729 (151) · `*` Q3 | **Invented** | The range blends two different measures from two sources. Q3 says *"40-something files"* (11 skills, 6 templates, 9 server configs, a prompts folder, scripts). #28729's *"20-30+ skills"* is the point at which an **organisation's shared set with multiple contributors** becomes hard to manage — a threshold, not a size, and not a personal library. "Fourteen months" is `*` and belongs to the 40, not to the 20. Correction: "`*` about forty files after fourteen months, one person; `✓` that a filer named 20–30+ shared skills as where management breaks". Same defect in `research.md` G4 ("every actual report clusters at 20–40") and `patterns.md`'s standing note. |
| P-11 | "What the `✓` carries is that a filer wrote that and 151 people reacted" | P1 §1 | NK-2 | **Confirmed** | Rule 5 applied correctly. |
| P-12 | They arrive from "one of three situations, and only three, because those are the only three anyone has described" | P1 §1 | `*` Q19 | **Confirmed** `*` | Q19 names exactly three. "Anyone" is one person; hypothesis at population. |
| P-13 | "**They arrive irritated more often than not**" | P1 §1 | `*` Q19 | **Invented** | Q19 says most *edits* are written while irritated, and ranks the modes: **copying out is the most frequent**, the irritated edit is second. "More often than not" reverses the respondent's own ordering. Correction: "the second most frequent reason to open the folder is an edit written in irritation". |
| P-14 | Whether this holds for anyone else is `[?]` → H1 | P1 §1 | — | **Confirmed** | Marked correctly. |

### P1 — Environment

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| P-15 | "Two to four agents installed, two of them used on any given day" | P1 Env | R1–R2 · Q1 | **Hypothesis** | Q1: four installed plus a dead Continue; two used *yesterday*. "Any given day" generalises one day. R2's six commenters give 2–4 targets each; three of the six (freakynit, type4, israrkhan) are URL-only. |
| P-16 | #6235 at 6,592 reactions is "the loudest thing in the whole evidence base" | P1 Env | R1 | **Confirmed** | gh log: 6,592 / 389; maximum in every log. |
| P-17 | "Six practitioners describe their own multi-tool setups in public" | P1 Env | R2 | **Confirmed** (utterance) | Three of the six are not in any capture log. |
| P-18 | "25 HN comments are about symlinking one source into several formats" | P1 Env | R2 | **Hypothesis** (count) | A hand count; not reproducible as stated. Re-run: 29 comments contain *symlink*, 19 of those name `AGENTS.md`/`CLAUDE.md`. Order of magnitude holds. |
| P-19 | The per-person count is seven people's self-description: `*` on the number, `✓` on the pattern | P1 Env | NK-5 | **Confirmed** | Matches the 2026-09-08 re-marking. |
| P-20 | Material lives in a git repository they own, symlinked into `~/.claude/` | P1 Env | `*` Q3 | **Confirmed** `*` | Q3 verbatim. Hypothesis at population; NK-6 says so. |
| P-21 | #1455 XDG, 446 reactions | P1 Env | R5 | **Confirmed** | gh log: 446. |
| P-22 | #28729 asks for a git repo as the source of truth, "which is evidence that it is not yet how that person works" | P1 Env | R5 | **Confirmed** | Title and body verified; the inference is labelled. |
| P-23 | "**Three machines or more**, counting containers" — `✓` OBS-6 with reaction counts · `*` Q5 | P1 Env | OBS-6 · Q5 | **Invented** (in part) | Q5 says *"Three, if you count containers"* — "or more" is added. OBS-6 lists host **types** (WSL, dev containers, Remote-SSH, Docker, JetBrains) with counts and carries no per-person machine count, so the `✓` does not support the number. Correction: "`*` three, one person; `✓` that these hosts appear in the trackers". |
| P-24 | The environments are WSL, dev containers, Remote-SSH, Docker, JetBrains | P1 Env | OBS-6 | **Confirmed** | OBS-6 lists each with an issue and count. |
| P-25 | "**Nothing is public.** `✓` R10 — 0 of 1,762 HN comments mention a portfolio; `portfolio in:title` returns two unrelated issues" | P1 Env | R10 | **Hypothesis** | R10 re-runs clean (0 matches for all four strings; `T.portfolio` total 2). But it establishes that nobody *mentioned* a portfolio, not that P1's material is private. The environment fact is `*` Q23 (*"None of it"*). Correction: mark `*`, cite Q23; keep R10 as the population absence. |

### P1 — Jobs

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| P-26 | Same rules across every agent: #6235 6,592 · #20697 161 *"manually copy skills to both locations"* · codex #17401 21 *"10+ repos"* | P1 §2 | R1, R3 | **Confirmed** | All three counts and bodies verified in the gh log. |
| P-27 | "This is the loudest job in the evidence base" | P1 §2 | — | **Confirmed** | |
| P-28 | Start a new project without the same forty minutes: thirty-five of the first sixty minutes; *"ten minutes, it's just a copy"* | P1 §2 | `*` Q6, Q9 | **Confirmed** `*` | Q6 verbatim; Q9 gives 40–60 minutes. |
| P-29 | #9444, 48 reactions — *"copies can drift out of sync"* | P1 §2 | R3 | **Confirmed** | Body verified. |
| P-30 | Stop the copies diverging: the same fix in one of three projects, found six weeks later by a client, three hours | P1 §2 | `*` Q10 | **Confirmed** `*` | Q10 verbatim. |
| P-31 | This is the job §5's live link exists to do | P1 §2 | NK-14 | **Confirmed** (R) | |
| P-32 | The eval harness "welded to that project's data model"; "the only evidence this question has ever had" | P1 §2 | `*` Q8 · NK-8 | **Confirmed** `*` | Q8 verbatim; NK-8: "nothing in the repository, in either direction, before it". |
| P-33 | Delete half of it with confidence; *"the folder only grows"* | P1 §2 | `*` Q18, Q20 | **Confirmed** `*` | Both verbatim. |

### P1 — Pains

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| P-34 | mcp/servers #64, 182 reactions, 91 comments, over a top-of-tracker of `npx` failures, processes dying, timezones, Windows path casing | P1 §3 | finding 1 | **Confirmed** | JSON: 182 / 91; finding 1's table. |
| P-35 | Devcontainer on Node 18 vs a server needing 20+; *"carries on without them, cheerfully"*; detection 25 minutes, fix two | P1 §3 | `*` Q11 | **Confirmed** `*` | Q11 verbatim. |
| P-36 | *"broken config doesn't announce itself, it degrades quietly"* | P1 §3 | `*` Q11 | **Confirmed** `*` | |
| P-37 | *"one in three fresh environments has something silently not loading"* — cited to Q11 | P1 §3 | `*` Q11 | **Invented** (misattribution) | The words are **Q12**. Correction: cite Q12. |
| P-38 | codex #13386 — `AGENTS.md` silently truncated at 32 KB, *"with no warning anywhere"* | P1 §3 | R6 | **Confirmed** | Body verified. (11 reactions; not quoted anywhere.) |
| P-39 | claude-code #9716, 75 reactions — skills present and not noticed | P1 §3 | R6 | **Confirmed** | 75 / 69. |
| P-40 | mcp/servers #1219, 13 reactions — *"the chat always chooses the first one specified"* | P1 §3 | finding 2 | **Confirmed** | JSON: 13. |
| P-41 | "Our own collision thesis, sighted in the wild, in the exact file we generate" | P1 §3 | OBS-16 | **Confirmed** (R) | |
| P-42 | "Quieter than the environmental pain **by a factor of fourteen, and that ratio is the honest weighting**" | P1 §3 | OBS-16 | **Hypothesis** (contradicts the rule) | 182 ÷ 13 = 14, but `inventory.md` §A, `jtbd.md` §7 and both stage plans say a reaction count is **ordinal** and "never fourteen times". Correction: "quieter; the ratio carries no weight". |
| P-43 | Env keys: #32733 192 · #401 54 · #29910 45 · continue #1729 32 · mcp #1018 23 · #754 22 | P1 §3 | R6, OBS-18 | **Confirmed** | All six verified across the two logs. |
| P-44 | #401 — *"Claude loads my project's `.env` into its bash environment"* | P1 §3 | R6 | **Confirmed** | Title and body. |
| P-45 | A formatting rule left over from another project; 1,100 lines of noise into a colleague's review branch | P1 §3 | `*` Q13 | **Confirmed** `*` | Q13 verbatim. |
| P-46 | #20412, 142 — *"silently synced… without any opt-in, notification, or consent"* | P1 §3 | R6 | **Confirmed** | 142; body verified. |
| P-47 | The doubt "across the threads": saberience, sothatsit, the *morally opposed* story, bandrami | P1 §3 | R7 | **Confirmed** (utterances) | All four in the thread log: 46106423, 46102180, 49376287 (29 pts / 28 comments), 46820441; text matches. Three of the four comments sit in **one** thread (46098838); see P-108 on "eight threads". |
| P-48 | *"maybe half of it… I've never A/B'd anything"* | P1 §3 | `*` Q16–Q17 | **Confirmed** `*` | |

### P1 — Trust triggers

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| P-49 | A usage fact is "the one thing a practitioner asked for in our own words, unprompted" — *"Usage data, first… loaded in 40 sessions… delete half of it with confidence"* | P1 §4 | `*` Q20 | **Confirmed** `*` | Q20 verbatim. "Unprompted" holds if the guide was followed as written; the interview is "lightly cleaned up" and records no deviation. Hypothesis about anyone else. |
| P-50 | Asked with our vocabulary forbidden, per the guide | P1 §4 | guide §4 | **Confirmed** | Guide Q20 forbids offering *used in 3 projects*; §6 bans the vocabulary. |
| P-51 | He extended it: *last actually useful*, not created-date; counted per session | P1 §4 | `*` Q20 | **Confirmed** `*` | |
| P-52 | "One person, and the strongest form a `*` can take" | P1 §4 | NK-12 | **Confirmed** (the register's own judgement) | |
| P-53 | OBS-29 — VS Code Workspace Trust: *"95 workspace settings are not applied"*, *"10 extensions are disabled"*, hyperlinked | P1 §4 | `M` | **Confirmed** | `NOTES-vscode.md` lines 72–75. |
| P-54 | It beats Figma's bare *423 instances* on the axis Figma leaves open | P1 §4 | OBS-29 | **Confirmed** (`M`, a judgement about two products) | |
| P-55 | OBS-31 — Vercel: *"You can't reveal this value after saving"*; *"Where to rotate, or who to contact"* | P1 §4 | `M` | **Confirmed** | Flow 07 `NOTES.md` lines 14, 23. |
| P-56 | This is the register §6 adopted for the unclean-export confirmation | P1 §4 | CLAUDE.md §6 | **Confirmed** | |
| P-57 | OBS-33 — Tessl composite 93, uplift 1.40×; Smithery score /100 | P1 §4 | `V` | **Confirmed** | Comparison matrix. |
| P-58 | `HarnessKit` *"scores trust 0–100"* by its own README | P1 §4 | R8 | **Confirmed** (README claim) | Rule 5 applied. README text not logged. |
| P-59 | An unearned green tick will be read as proof the checker is decoration — "the inference is ours, `R`" | P1 §4 | R7 | **Hypothesis** | Self-declared inference. |
| P-60 | The genie answer, verbatim, "asked before the product was ever described" | P1 §4 | `*` Q25 | **Confirmed** `*` | Q25 verbatim. The guide places any description after Q26; the interview file records no post-disclosure section, so whether a description was given at all is unrecorded. |
| P-61 | "Our validation pass answers *does this set cohere*. He asked for *what ran*. Those are not the same product" — Q12 | P1 §4 | NK-23 | **Confirmed** (R; in the register) | |
| P-62 | continue #567, telemetry opt-out, 2 reactions, the only one of its kind in 182 records | P1 §4 | OBS-24 | **Confirmed** | JSON: 2 / 6; OBS-2's title search. |
| P-63 | OBS-25 — Continue's hosted half switched off, *"all user data has been deleted"* | P1 §4 | `E` | **Confirmed** | Post-mortem §0. |
| P-64 | allknowingfrog — *"I don't track Claude resources in our repos…"* — "a refusal to commit the material at all, on lock-in grounds" | P1 §4 | HN | **Confirmed** (utterance) · **Hypothesis** (motive) | Keyword log 48184129, 2026-05-18, text matches. The comment's own frame is letting team members choose their tools; "lock-in" is a reading. |

### P1 — Quote and settlement

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| P-65 | The eternityforest quote, 2026-06-22, marked `✓` | P1 §5 | HN 48638003 | **Hypothesis** (on the mark) | Text and date match R3/R7. The comment is in **neither** capture log; the `✓` rests on the URL alone. The plan (README, *The circular quote*) requires a quote "with its URL and reaction count" from the JSON; HN exposes no comment score, and `personas.md` restates the rule as "a URL or it is not a quote" — a softening it does not announce. Correction: log the comment (Algolia `items/48638003`) and say the `✓` is URL-only. |
| P-66 | "Both halves of this persona are in one sentence… It is the whole of P1" | P1 §5 | — | **Hypothesis** (R) | |
| P-67 | This card may settle: the Run stage list and verdicts (§6, §8); the copy register for a Problem and a Note (§6); "what an item card carries — usage facts, and specifically *last actually useful* rather than *last exported*" (§5); the handover stages (§6); the target selector's prominence (§6) | P1 *What this card is allowed to settle* | — | **Hypothesis** (overreach on two of five) | *Last actually useful* is n = 1 and is not in the spec — §5 says *last exported*; the card claims settlement on a field the data model has no source for (no session concept in §5, no runtime in §10). The copy register rests on H1, which the same card marks `[?]`. The other three rest on `✓` utterances at population and are within the marks. |
| P-68 | It may not settle the Library screen at scale or positioning | P1 *Settle* | README | **Confirmed** | |

### P2 — Context and jobs

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| P-69 | They are handed a repository and expected to work in it — `✓` #6235's motive *"collaborating with other developers who aren't using Claude Code"* | P2 §1 | R12 | **Confirmed** (utterance) · **Hypothesis** (as a receiver's situation) | The filer is the author. No receiver wrote it. |
| P-70 | #10238 168 *"with my team"* · #28729 151 *"multiple contributors"* · #48322 53 | P2 §1 | R12 | **Confirmed** | Bodies and titles verified. All three are authors on teams asking for tooling. |
| P-71 | "**They usually run a different agent** from the person who wrote it. `✓` — that is what #6235 is about, and the same family spans three vendors' trackers (R1)" | P2 §1 | R1 | **Invented** | "Usually" is a frequency no instrument measured. And R1's thirteen-issue family includes five issues about session, history, account or subscription sync (#17118, #2511, #28791, #22648, #31992), not instruction files; the instruction-file family is eight. Correction: "`[?]` — the situation is filed once with a stated motive; its frequency is not known". |
| P-72 | Environment `[?]` almost entirely → H5 | P2 §1 | — | **Confirmed** | |
| P-73 | Job: get the thing to run today — `✓` #6235's motive · `*` Q21 | P2 §2 | — | **Hypothesis** | #6235's motive is a shared format for collaborators; it does not say *get it running today*. Q21 is the author's account. Correction: `*` second-hand only. |
| P-74 | Job: find out what is load-bearing — *"which files are load-bearing and which are aspirational… None of that is written down anywhere"*, a twenty-minute call | P2 §2 | `*` Q22 | **Confirmed** `*` | Q22 verbatim. |

### P2 — Pains, trust, quote, settlement

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| P-75 | The handover failed silently for two days — verbatim; "second-hand and n = 1" | P2 §3 | `*` Q21 | **Confirmed** `*` | Verbatim, and correctly flagged. |
| P-76 | Half of what makes the setup work was never written down — verbatim; "bounds the ceiling of our entire product"; Q11 | P2 §3 | `*` Q26 | **Confirmed** `*` | Verbatim; the ceiling claim is R and is in the register. |
| P-77 | A rule from the author's world colliding with the receiver's — *"my CLAUDE.md says one thing, the client's linter says another"* | P2 §3 | `*` Q26 | **Hypothesis** (misplaced) | Q26 describes the **author's** own rule against a **client's** linter in the author's own project. Nothing in it involves a receiver. Correction: move to P1's pains (it is Q10 either way). |
| P-78 | The benchmark found no product with such a surface — OBS-20, B4, *nobody above 4* | P2 §4 | `V` | **Confirmed** (as the benchmark's stated finding) | `benchmark.md` lines 115, 471, finalisation. Note for the record: the benchmark's own matrix gives Vercel deploy **C1 = 5** inside B4, so "no cell above 4" holds for the row-level reading the benchmark uses, not for every category score. Inherited from stage 4. |
| P-79 | Never tested on a receiving agent or person — `[?]` → H6, NK-13 | P2 §4 | — | **Confirmed** | |
| P-80 | OBS-30 — Notion: *"anyone with the link can view this page's content and see contributor names"* | P2 §4 | `M` | **Confirmed** | Flow 12 `NOTES.md` lines 17–19. |
| P-81 | #20412 — duplicates and OOM kills | P2 §4 | R6 | **Confirmed** | Body. |
| P-82 | OBS-32 — `ConfigValidationError { fatal: boolean }`, a block that failed to resolve filed as `fatal: false` | P2 §4 | `E` | **Confirmed** | Post-mortem lines 179–186. |
| P-83 | The #6235 quote; 6,592 reactions, 389 comments, filed 2025-08-21 | P2 §5 | gh log | **Confirmed** | Body, counts and date all in the log. |
| P-84 | "The most-reacted issue anywhere in this repository's evidence base is **about the receiver**. That is the single strongest argument for keeping this persona" | P2 §5 | — | **Hypothesis** | The issue asks for `AGENTS.md` support; one sentence of its motive names collaborators on other tools. Reading it as *about the receiver* is an interpretation, and the same issue anchors P1's X2 end (P-07). An issue that anchors both personas cannot be the strongest argument for keeping them apart. |
| P-85 | This card may settle what `SETUP.md` states and in what order (§6); which stages sit before Export (§6, §8); the wording of a Note about a missing env key | P2 *Settle* | — | **Hypothesis** (overreach) | Every P2 row is a filed request by an author or a second-hand `*`; the card says itself no receiver was asked. "What `SETUP.md` states and in what order" is a content decision for the reader nobody has met. |
| P-86 | "No receiver has ever been asked" | P2 *Settle* | — | **Confirmed** | |

### P3 — all blocks

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| P-87 | `xingkongliang/skills-manager` 4,526★, `MoizIbnYousaf/ai-agent-skills` 1,138★, `luongnv89/asm` 915★ | P3 §1 | R8 | **Confirmed** (as of 2026-09-07, unlogged) | The web log lists the nine repository names and no star counts; the figures live only in `re-research.md`'s prose and drift daily. Not re-runnable to the same value. |
| P-88 | "Their existence and their stars are `✓`; what they do is their own README and we ran none of them" | P3 §1 | rule 5 | **Confirmed** | |
| P-89 | Catalogs report six and seven figures, and "one vendor's own report says *'discovery is no longer the bottleneck. Judgment is.'* — R9, published by a hard competitor that sells curation" | P3 §1 | R9 | **Invented** (attribution) | The web log attributes the *Judgment* sentence to **agensi.io**, a third-party "affiliate-shaped comparison", and the seven-figure counts to Agentman and agensi. `re-research.md` R9 lists it under the Agentman bullet, which is where the error entered. Correction: attribute to agensi.io; keep Agentman for the figures it published. |
| P-90 | OBS-12 — every catalog in the survey solves cold start with curation and volume | P3 §1 | `V` | **Confirmed** | Comparison, difference 2. |
| P-91 | "Nothing in that list is a person" | P3 §1 | — | **Confirmed** | |
| P-92 | Jobs all `[?]` → H8; §11's reasoning is A-8, standing `[?]` | P3 §2 | inventory B | **Confirmed** | |
| P-93 | Snyk: 3,984 skills scanned from two registries on 2026-02-05; 13.4% critical; 1,467 with at least one flaw; 76 confirmed malicious; the *"one week old… No code signing"* quote | P3 §3 | R6 | **Confirmed** (published, not verified by us) | Every figure and the quote are in the web log with that caveat. |
| P-94 | Snyk's post does not reconcile 36% with 36.82% | P3 §3 | R6 | **Confirmed** | Web log caveat. |
| P-95 | §11's *"checked sources"* must come to mean checked for content — proposal 5 | P3 §3 | `re-research.md` §4 | **Confirmed** (as a proposal) | |
| P-96 | Everything else `[?]` → H9 | P3 §3 | — | **Confirmed** | |
| P-97 | OBS-36 — a new Linear workspace opens on four real issues, deletable | P3 §4 | `M` | **Confirmed** | `NOTES-linear.md` lines 5, 16–30. |
| P-98 | This is the shape §11's example project copies | P3 §4 | CLAUDE.md §11 | **Confirmed** (R) | |
| P-99 | §5 requires origin and a pinned `ref` on every public item | P3 §4 | CLAUDE.md §5 | **Confirmed** | |
| P-100 | OBS-34 — Terraform, Figma, Raycast and Backstage attach an identity to a shared artefact | P3 §4 | `V` | **Confirmed** | Comparison matrices. |
| P-101 | OBS-37 three registers of emptiness; OBS-38 a control that cannot act is not shown, three products against one | P3 §4 | `M` | **Confirmed** | `NOTES-linear.md` §2, §4; flow 07. |
| P-102 | "Nobody in this shape has said anything anywhere we looked — 1,762 HN comments, five trackers, one conversation" | P3 §5 | — | **Hypothesis** | A pass over the thread log for people installing others' skills finds six comments about skills.sh and marketplaces, none from a self-described empty-handed person — the absence stands for HN. But no query in the gh log targets this shape, so "five trackers" were not looked at for it. One datum the card missed: bazhand (46877112) reports a skills.sh skill at *"50k/week installs"* — a `V`/`E`-grade consumption figure, self-reported by a commenter about a site. |
| P-103 | The guide's P5 recruit has not been found | P3 §5 | guide §2 | **Confirmed** | |
| P-104 | It settles exactly one thing: the shelf needs a stated content-review standard, because the one hard number is 13.4% | P3 *Settle* | R6 | **Confirmed** (as proposal 5; the number is published-not-verified) | |

### Why P1 is primary, the overturn conditions, the bias

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| P-105 | "The one practitioner asked says they are the same person" — *"The collection created the problem"* | *Why P1* | `*` Q15 | **Confirmed** `*` | Verbatim. |
| P-106 | X6 is one sentence from one person, "the only causal claim anybody has made" | *Why P1* | inventory §D | **Confirmed** | One interview exists. |
| P-107 | Reason 1: "It is **the only persona** with `✓` and `*` agreeing from independent instruments" | *Why P1* | — | **Invented** (superlative) | P2's own card claims exactly that combination ("`✓` at population, `*` for the story"), and `jtbd.md` gives RJ-1 — P2's job — the standing `✓` + `*`. Correction: "the persona with the most such agreement". |
| P-108 | Reason 1's counts: 6,592 · 48 · 182 · 13 · "the doubt **across eight threads** and one interview" | *Why P1* | R7 | **Confirmed** (counts) · **Invented** (the thread count) | The R7 quotes come from three comments in thread 46098838, one in 46809708, the 28-comment story 49376287, and one comment outside the threads. A keyword pass finds doubt-shaped comments in six of the eight threads at 0–5 each; "across eight threads" is not what was read. Correction: "in four of the eight threads". |
| P-109 | Reason 2: the benchmark re-weighted the flows by pain and put the value in B3 and B4 | *Why P1* | finalisation | **Confirmed** | `benchmark.md` line 508. |
| P-110 | Reason 3: higher risk and fewer levers is the lesson's rule | *Why P1* | README step 3 | **Confirmed** (the rule) · **Hypothesis** (its application) | |
| P-111 | Reason 4: P2's job is a consequence of P1's set | *Why P1* | — | **Hypothesis** (R) | |
| P-112 | Three overturning conditions, each with an instrument | *What would overturn* | guide Q15, Q25; register Q5, Q7, Q12 | **Confirmed** | Each names an existing instrument. |
| P-113 | Every public source is a person who chose to write in public; the respondent is also a filer | *Bias* | X5, Q24 | **Confirmed** | |
| P-114 | Reddit "is named across community surveys as **the largest venue** for this population" | *Bias* | R13 | **Invented** (superlative) | The web log holds one survey; its *taken* list names venues without ranking them. "Largest" appears only in `re-research.md`'s own prose. Correction: "named in a community survey as one of the venues". |
| P-115 | Every number in the interview is a recollection; the respondent flags his unreliability twice | *Bias* | rule 3 | **Confirmed** | Interview header. |
| P-116 | "**Roughly half of every card above is `[?]`**, and all of the adoption story is" | *Bias* | README | **Invented** (self-description) | Counted: P1's card carries 20 `✓`, 19 `*`, 5 `[?]`; P2's 5 / 5 / 2; P3's 2 / 0 / 6. Half holds for P3 only. The adoption half is right. Correction: "P3 is mostly `[?]`; P1 and P2 are mostly `*` and utterance-level `✓`". |

### Hypotheses and hand-forward

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| P-117 | H1–H11, each in the form *we assume X; we would check it by Y* | *Hypotheses* | — | **Hypothesis** (by construction) | Sub-claims checked: H9 cites G5 correctly; H10's missing licence field is R11; H11 is A-4/A-5. |
| P-118 | H3: a count that links to its list convinces this audience "**as it does in VS Code and Figma**" | *Hypotheses* | OBS-28, OBS-29 | **Hypothesis** (presupposition) | The `M` captures show the mechanism exists in both products, never that it convinces anyone. The clause assumes what the hypothesis is meant to test. |
| P-119 | H5: "Ask a receiver. Nobody has, and **the guide does not currently recruit one**" | *Hypotheses* | guide §2 | **Invented** (in part) | Guide §2's P3 profile is *"has handed a setup to somebody else, **or received one**"* — it does recruit one. What the guide lacks is a block of questions **for** a receiver; every question is addressed to an author. Correction: "the guide recruits one and has no questions for them". |
| P-120 | "Every claim carrying only `*` bears on a design decision and stands on one person — the whole of P1's trust-trigger block and the whole of P2's pain block" | *Hands forward* | — | **Confirmed** (self-assessment) | P1's trust block also carries three `M` rows. |
| P-121 | H6 is ours to close in an afternoon, the only hypothesis that needs no other person | *Hands forward* | NK-13 | **Confirmed** | |

## `jtbd.md`

### Header and §1 — the main job

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| J-01 | One of the five conversations has happened | Header | — | **Confirmed** | |
| J-02 | Four related jobs in the main list, seven hypothesis jobs | Header | — | **Confirmed** | Counted. |
| J-03 | Candidate A: #6235 6,592 "and **a twelve-issue family across three vendors' trackers**"; #20697 161; 25 HN comments | §1 table | R1, R2 | **Confirmed** (the two counts) · **Hypothesis** (the family) | R1's thirteen rows include five about session, history, account or subscription sync — #17118 *OpenCode and Max plan* (1,416), #2511, #28791, #22648, #31992 — not instruction files. The instruction-file family is eight issues across three trackers. The 25 is a hand count (P-18). |
| J-04 | A's standing: "`✓`, and the loudest thing in the entire evidence base" | §1 table | — | **Confirmed** | |
| J-05 | Candidate B: #64 182; #13386; #9716 75; `*` Q5, Q11 | §1 table | — | **Confirmed** | |
| J-06 | Candidate C: #9444 48; #17401 21; `*` Q4, Q6, Q9; "`[?]` as a driver of adoption — this is Q5" | §1 table | — | **Confirmed** | |
| J-07 | Candidate D: `*` Q19 *"it usually takes longer than rewriting it would"*; "one sighting, ever; loss has no evidence in any instrument tried" | §1 table | NK-1 | **Confirmed** | Q19 verbatim; R3 and NK-1 say loss has none. |
| J-08 | Candidate E: `✓` R7 · `*` Q16, Q17, Q25 | §1 table | — | **Confirmed** | |
| J-09 | "A and B are one job seen along two axes… C is the same job at the moment a project begins. So A, B and C merge" | §1 | inventory §D | **Hypothesis** (R) | A synthesis. Note the register's Q8 treats *assemble* against *hand over* as possibly two products; the merge decides Q8 by construction, before the sitting. |
| J-10 | The main job, as worded | §1 | — | **Hypothesis** (a synthesis, not a claim about the world) | Verified by grep: it names no §4 noun, §6 mechanism or §8 surface. |
| J-11 | P2 is on the other end of the same sentence | §1 | — | **Hypothesis** (R) | |
| J-12 | Grew from: #6235 6,592/389 with its motive; #64 182/91; #9444 48; #17401 21; 25 HN comments; `*` Q5 (four servers silently not starting, twenty minutes believing the model had got worse); Q11 | §1 | — | **Confirmed** | All verified. Q5: *"I spent the first twenty minutes thinking the model had gotten worse."* |
| J-13 | B4 is the weakest flow, nobody above 4, "because no product has a surface that says anything about the machine its artefact lands on" | §1 | benchmark | **Confirmed** | Finalisation, *The gap neither instrument covers*. See P-78's note. |
| J-14 | "**The two loudest numbers in the repository — 6,592 and 182** — are both inside it" | §1 *Standing* | — | **Invented** | In the gh log alone #17118 (1,416), #2511 (624), #31005 (472) and #1455 (446) exceed 182; in the stage-3 JSON #917 (245) does. 182 is the loudest in `modelcontextprotocol/servers` only. Correction: "the loudest number in each of two corpora". |
| J-15 | A symlink farm, a dotfiles repo, a package manager and a bootstrap script "all close it today, **badly**" | §1 | R2, R8 | **Hypothesis** | That they exist is `✓` (utterances, READMEs). "Badly" is R — nobody watched one run. |
| J-16 | §2 words the value as assembly with validation and the wow moment as the export | §1 | CLAUDE.md §2 | **Confirmed** | |
| J-17 | "The evidence says the value is that the set still works after it leaves" | §1 | — | **Hypothesis** (R, and labelled a difference of emphasis) | |
| J-18 | Supports G1's *reassembly over loss* half; does not settle G9 | §1 | `research.md` §5 | **Confirmed** | G1 and G9 wording checked. |
| J-19 | Candidate E did not fold; both have `✓` and `*` behind them | §1 | — | **Confirmed** | |
| J-20 | It is already Q12 in the register | §1 | `research-plan.md` | **Confirmed** | |
| J-21 | "It is the one we cannot build: §6 runs nothing on anyone's machine" | §1 | CLAUDE.md §6 | **Confirmed** | |

### §2 — Related jobs

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| J-22 | RJ-1 grew from `*` Q21, verbatim | RJ-1 | — | **Confirmed** `*` | |
| J-23 | `✓` #6235, whose motive is collaboration across tools | RJ-1 | — | **Confirmed** (utterance) | |
| J-24 | "`V` benchmark B4 — **fifteen products, none above 4**" | RJ-1 | benchmark | **Invented** (count) | The benchmark scored **15 cells** across four flows, drawn from **ten** products; B4 holds **four** cells (Vercel deploy, `create-next-app`, Figma export, Ruler). Correction: "four B4 cells, none above 4". |
| J-25 | Standing: "`✓` that the need exists and is unserved; `*` for what it costs" | RJ-1 | — | **Hypothesis** | That a **sender** needs to know in advance is in no source — Q21's respondent found out on a call, and §7 says so. Correction: "`✓` that handovers happen and fail; `[?]` that senders want to know beforehand". |
| J-26 | RJ-2: #1219, 13, verbatim | RJ-2 | — | **Confirmed** | |
| J-27 | continue #8484 6, #4306 3, and four more at 0–2 (OBS-17) | RJ-2 | JSON | **Confirmed** | 6, 3, 2, 0, 0, 0. |
| J-28 | `*` Q13, 1,100 lines | RJ-2 | — | **Confirmed** `*` | |
| J-29 | "13 against 182… a reaction count is ordinal, so *quieter* is all it says" | RJ-2 | — | **Confirmed** | The rule, stated correctly here — against P-42. |
| J-30 | RJ-3: #9444 48, verbatim | RJ-3 | — | **Confirmed** | |
| J-31 | `*` Q10 verbatim, including *"It's a loop"* | RJ-3 | — | **Confirmed** `*` | |
| J-32 | "`✓` `competitors.md` — the same failure named as Backstage's known one, cited as corroboration" | RJ-3 | competitors.md | **Invented** (a withdrawn mark) | `inventory.md` NK-14 re-marked this exact source **Not `✓`** on 2026-09-08: *"our own stage-1 write-up of community lore about someone else's product; it corroborates and it measures nothing."* `jtbd.md` restores the mark the register withdrew. Correction: cite it unmarked. |
| J-33 | "The best-evidenced job in the file after the main one — NK-14" | RJ-3 | — | **Hypothesis** (judgement) | RJ-4 carries six verified `✓` counts to RJ-3's one. |
| J-34 | RJ-4: the six issue counts | RJ-4 | R6, OBS-18, OBS-21 | **Confirmed** | |
| J-35 | `*` Q23 verbatim; *"a couple of hours that are never the most urgent couple of hours"* | RJ-4 | — | **Confirmed** `*` | |
| J-36 | "The blocker is not encrypting anything, it is that the private and the reusable are tangled in the same files" | RJ-4 | `*` Q23 | **Confirmed** `*` | n = 1. |

### §3 and §4 — Emotional and social jobs

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| J-37 | EJ-1: #20412 142; #13386; #1219; `*` Q13 *"it's a story I tell myself"* | EJ-1 | — | **Confirmed** | |
| J-38 | "The strongest emotional job in the file, and the one OBS-23 already named" | EJ-1 | OBS-23 | **Confirmed** (OBS-23) · judgement on "strongest" | |
| J-39 | EJ-2: bandrami and Alpha_Logic, verbatim | EJ-2 | HN | **Confirmed** | Thread log 46820441, 46106973; text matches. |
| J-40 | OBS-32 | EJ-2 | `E` | **Confirmed** | |
| J-41 | "The inference that this is what a person *feels* is ours, `R`" | EJ-2 | — | **Hypothesis** (self-declared) | |
| J-42 | EJ-3: saberience, eternityforest, the *morally opposed* story | EJ-3 | R7 | **Confirmed** (utterances; eternityforest URL-only) | |
| J-43 | `*` Q16, Q18 verbatim | EJ-3 | — | **Confirmed** `*` | |
| J-44 | "The emotional face of main-job candidate E — Q12" | EJ-3 | — | **Confirmed** (R) | |
| J-45 | The social layer's population evidence is an absence looked for twice: 0 of 1,762 and two unrelated issues | §4 | R10 | **Confirmed** | Re-run: 0 matches for all four strings; `T.portfolio` total 2. |
| J-46 | SJ-1: `*` Q21, Q22 verbatim; `✓` #6235, #10238, #28729 | SJ-1 | R12 | **Confirmed** | |
| J-47 | Standing: "`✓` that the situation occurs" | SJ-1 | — | **Hypothesis** | The `✓` is that authors on teams filed requests; *somebody else opens something I made* is inferred from that. Utterance-level. |
| J-48 | SJ-2: `*` Q23 *"publishing forces cleanup"*; `✓` and `*` disagree and both stay | SJ-2 | rule 4 | **Confirmed** | |

### §5 — The feature-name test

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| J-49 | The six *written first* rows and their rewrites | §5 table | — | **Confirmed** (a record of the document's own drafts, not claims about the world) | |
| J-50 | "No *I want* clause contains: item · project · library · … · archive" | §5 | — | **Confirmed** | Re-run over the nine block-quoted jobs and every table job: no listed word inside an *I want* clause. For the record, *project(s)* appears in the **when** clauses of RJ-2, RJ-3 and H-J3, and *run* in SJ-1's **so that** clause, all in ordinary senses. The plan's test covers *I want* and *motivation*, so this passes as scoped; the when-clauses were not swept. |
| J-51 | "The word *archive*… **appears in RJ-1's *when* clause** in its ordinary English sense and nowhere else" | §5 | — | **Invented** | *Archive* does not appear in RJ-1's when-clause (*"When I am about to hand a working setup to another machine or another person"*). In the whole file it appears twice: in this table (line 290) and in this sentence (line 298). Correction: "*archive* appears in no job". |
| J-52 | "*export* appears only in this table" | §5 | — | **Invented** | It also appears in §1 (*"the wow moment is the export"*, line 78) and three times in the matrix's feature column (*"before Export"*, *"before export"*, lines 345, 349, 350). Correction: "*export* appears in no job; it appears in this table and in the feature column". |

### §6 — Hypothesis jobs

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| J-53 | H-J1–H-J7, each in the required form | §6 | — | **Hypothesis** (by construction) | Sub-claims: H-J1 "the only sighting of loss anywhere in the repository" — Confirmed (NK-1, R3); H-J3's `M` flow 05 — Confirmed; H-J4's 425–4,526★ — Confirmed, unlogged (P-87); H-J5 `✓` + `*` — Confirmed; H-J7 Q26 — Confirmed. |
| J-54 | H-J3 stands on Q26's *"there's no precedence anywhere"* and "this is **Q10** in the register" | §6 | NK-21 | **Hypothesis** (an equation that does not hold) | Q10 is a conflict between the user's rule and something **outside** the set — a client's linter. H-J3 is *change one copy for one project without touching the rest* — a per-project **override**. The aside supports Q10; it says nothing about wanting an override. Equating them lends H-J3 evidence it does not have. See J-107. |

### §7 — The matrix

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| J-55 | P2 carries a number in three cells; P3 in none | §7 intro | matrix | **Confirmed** | MAIN 3, RJ-1 3, EJ-1 2; P3 all `[?]`. |
| J-56 | "An importance nobody has told us is `[?]`, not 2" | §7 intro | README | **Confirmed** (the rule) | See J-60, J-61, J-74 for cells that break it. |
| J-57 | MAIN, P1 = 3 — `✓` #6235, #64; `*` Q5, Q11 | §7 MAIN | — | **Confirmed** (the evidence) · **Hypothesis** (the 3 at population) | The 3 — *a reason they would change how they work* — is the best-supported cell in the matrix: the respondent built a repo and a bootstrap script (Q3, Q4), which is behaviour. |
| J-58 | "#64 182, **the loudest pain in the older corpus**" | §7 MAIN | JSON | **Hypothesis** | #917 (245, *Neovim support*) is the most-reacted issue in the older corpus (OBS-3, OBS-4); #64 is the loudest **pain** only if a feature request is not a pain. Say so. |
| J-59 | MAIN, P2 = 3 — "`✓` #6235's stated motive **is** this job" · `*` Q21 second-hand | §7 MAIN | — | **Invented** (the number) | A 3 means the person would change how they work. The only receiver on record *"assumed that was normal and worked around it for two days without mentioning it"* — evidence that he did **not**. #6235's filer is an author. Correction: `[?]`, or at most 2 on the second-hand story, and say which. |
| J-60 | MAIN competitors: B4 nobody above 4; not one of fifteen cells scores the receiving machine; per-agent output exists (Ruler, `create-next-app`, flow 06); skill managers claim per-agent sync in READMEs, unrun | §7 MAIN | benchmark, flow 06, R8 | **Confirmed** | `ruler-per-agent-output.md` is in flow 06; the finalisation's *gap* section says every cell scores the product's own state. |
| J-61 | RJ-1, P1 = 2 — "`*` Q21 only, plus `V` the B4 gap. He found out on a call; **that he wanted to know beforehand is our inference, `R`**" | §7 RJ-1 | — | **Invented** (the number) | The cell holds a number on evidence the document itself calls inference, against its own rule (J-56). Correction: `[?]`. |
| J-62 | RJ-1, P2 = 3 — `*` Q21 second-hand · `✓` #6235's motive | §7 RJ-1 | — | **Invented** (the number) | As J-59: a 3 for a person never asked, from a story in which he changed nothing. Correction: `[?]` or 2. |
| J-63 | RJ-1 competitors: "no candidate has a surface that describes the receiving machine at all" | §7 RJ-1 | finalisation | **Confirmed** | |
| J-64 | RJ-2, P1 = 2 — `✓` 13 and the family; `*` Q13 | §7 RJ-2 | — | **Hypothesis** (supported) | Q13's 1,100 lines, noticed from a colleague's comment, is *it costs them something*. |
| J-65 | RJ-2 competitors: post-mortem §5 (`BlockDuplicationDetector` then `mergeUnrolledAssistants`, no error); npm `ERESOLVE`, `terraform validate`; `asm`'s README on trigger collision | §7 RJ-2 | — | **Confirmed** | Post-mortem lines 152–154; benchmark files; R8. |
| J-66 | RJ-3, P1 = 3 — `✓` #9444 48; `*` Q10 | §7 RJ-3 | — | **Hypothesis** (the 3 overreaches) | Q10's respondent lost three hours and still moves material by `cp -r` (Q7). *A reason they would change how they work* is not what he reports; Q10 supports 2. |
| J-67 | RJ-3 competitors: Figma's *423 instances* (flow 05); Continue's hub did it for this material and was switched off; `HarnessKit` README | §7 RJ-3 | — | **Confirmed** | Flow 05 table; post-mortem lines 72, 86 (`uses` — a live link by slug) and §0. |
| J-68 | RJ-4, P1 = 3 — "**the largest crowd in the corpus**: 192 · 54 · 45 · 32 · 23 · 22"; `*` Q23 | §7 RJ-4 | — | **Invented** (superlative) · **Hypothesis** (the 3) | The R1 family (6,592, 1,416, 624, 472, 161, …) is larger by any measure. And Q23's respondent has **not** done the separation — *"never the most urgent couple of hours"* — so the story supports 2. Correction: "the largest crowd on a fear, after the multi-target family"; reconsider the 3. |
| J-69 | RJ-4, P2 `[?]` — "no receiver has said anything about it" | §7 RJ-4 | — | **Confirmed** | |
| J-70 | RJ-4 competitors: "**No, in this space**… No candidate in the survey does this for a handed-over artefact" | §7 RJ-4 | flow 07 | **Hypothesis** | True of the fifteen benchmark cells. Doppler and Infisical were captured in flow 07 as marketing pages, and `tank` and `asm` claim credential scanning in their READMEs (R8); none was run. "Nobody in this space" is not established for the space. |
| J-71 | EJ-1, P1 = 3 — #20412 142; #13386; #1219; `*` Q13, Q14 *"my guesses are unfalsifiable"* | §7 EJ-1 | — | **Confirmed** (evidence) | Q14 verbatim. The 3 is a judgement. |
| J-72 | EJ-1, P2 = 2 — `*` Q21 second-hand, "overruled by absence" | §7 EJ-1 | — | **Hypothesis** | Two days lost is *it costs them something*; second-hand, and flagged. |
| J-73 | EJ-1 competitors: Port pass/warn/block; GitHub's mergebox; Continue's `fatal: false` | §7 EJ-1 | comparison, CLAUDE.md §6, post-mortem | **Confirmed** | |
| J-74 | EJ-2, P1 = 2 — "HN comment scores are not exposed, so **this evidence carries no weighting at all**" | §7 EJ-2 | I3 | **Invented** (the number) | The cell states its evidence carries no weighting and then holds a 2. The matrix's own rule says `[?]`. Correction: `[?]`, or state the non-count basis for 2. |
| J-75 | EJ-2 competitors: Tessl 93, Smithery /100, `HarnessKit` 0–100; "reading their scores as a failure at this job is our inference, `R`" | §7 EJ-2 | — | **Confirmed** / self-declared | |
| J-76 | EJ-3, P1 = 3 — "`✓` R7 **across eight threads**"; `*` Q16, Q17, Q18 | §7 EJ-3 | — | **Invented** (the count) · **Confirmed** (the rest) | See P-108. |
| J-77 | EJ-3 feature: "Nothing — and nothing can. §5's usage facts answer *is it used*, not *did it change anything*. §6 runs nothing" | §7 EJ-3 | CLAUDE.md | **Confirmed** (R) | |
| J-78 | EJ-3 competitors: "`V` **four HN stories in nine months**: *AGENTS.md outperforms skills* (524), SkillsBench (364), Agent Skills Leaderboard (135), agent-skills-eval (79)" | §7 EJ-3 | R7 | **Hypothesis** | 524 is in the thread log (46809708, 524p/196c). 364, 135 and 79 are in no capture log; `re-research.md` R7 gives them in prose and says *"three HN stories"* while listing four. "Nine months" is undated anywhere. Correction: log the three story ids or mark the points unverified. |
| J-79 | SJ-1, P1 = 2 — `*` Q21, Q22; `✓` #6235, #10238, #28729 | §7 SJ-1 | — | **Hypothesis** (supported) | Twenty minutes on a call, twice. |
| J-80 | SJ-2, P1 = 1 — `✓` the absence (R10); `*` Q23 | §7 SJ-2 | — | **Confirmed** | 1 is *it comes up*. |
| J-81 | SJ-2 competitors: Figma Community, Notion's gallery, Raycast's store, a GitHub profile (flow 12) | §7 SJ-2 | — | **Confirmed** | Comparison; flow 12. |
| J-82 | "Every cell here is `[?]` except one" | §7 hypothesis matrix | — | **Confirmed** | H-J5, P1 = 3. |
| J-83 | "Four specified features close nothing else" | §7 hypothesis matrix | — | **Confirmed** (as the tally) | §9 lists six features; four (the switch and shelf, the example project, duplicate, promote) close only `[?]` jobs; search and usage facts carry a `*`. |
| J-84 | H-J1 competitors: "B1 is where the craft is concentrated: Linear's palette and filter grammar, **Backstage's catalog, Raycast**, Obsidian" | §7 H-J1 | benchmark | **Hypothesis** (partly invented) | The benchmark's B1 candidates were Linear, GitHub code search, Obsidian and VS Code. Backstage and Raycast were surveyed in stage 1 and never benchmarked. Correction: "Linear, GitHub, Obsidian (B1); Backstage and Raycast from the landscape". |
| J-85 | H-J2 competitors: Notion's `Ctrl+D` with no dialog; GitHub's fork form | §7 H-J2 | flow 09 | **Confirmed** | |
| J-86 | H-J3: Q10 "is a conflict with something outside the set entirely, which §5 has nowhere to put"; Figma erases the origin at detach | §7 H-J3 | NK-21, flow 05 | **Confirmed** (both facts) · see J-54 on the link to H-J3 | |
| J-87 | H-J4 competitors: Smithery 17,500, Tessl 3,000+, Agentman 115, Notion's gallery; every catalog solves cold start this way (OBS-12) | §7 H-J4 | `V` | **Confirmed** | |
| J-88 | H-J5, P1 = 3 — `✓` R7, `*` Q25; counted once with EJ-3 | §7 H-J5 | — | **Confirmed** | |
| J-89 | H-J7 competitors: "Nobody in the survey attempts it" | §7 H-J7 | — | **Confirmed** | Trivially: no surveyed product claims to move unwritten knowledge. |

### §8 — What to build first

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| J-90 | Five jobs score 3 for P1 — the main job, RJ-3, RJ-4, EJ-1, EJ-3 | §8 | matrix | **Confirmed** | H-J5's 3 is merged with EJ-3. |
| J-91 | "Cells: P1 = 3, P2 = 3. **The only row with a number in both people-columns**" | §8.1 | matrix | **Invented** | RJ-1 (2, 3) and EJ-1 (3, 2) also carry numbers in both. Correction: "the only row with a 3 in both". |
| J-92 | Market: nobody above 4 on B4, structurally | §8.1 | finalisation | **Confirmed** | |
| J-93 | "The spec already spends most of its handover budget here" | §8.1 | — | **Hypothesis** (R) | |
| J-94 | RJ-4: "on **the largest `✓` crowd in the corpus** — 192, 54, 45, 32, 23, 22, **across two ecosystems**" | §8.2 | — | **Invented** (superlative) | As J-68. And the six issues come from **three** trackers (`anthropics/claude-code`, `continuedev/continue`, `modelcontextprotocol/servers`). |
| J-95 | "Market: nobody in this space. The best prior art (Vercel's env drawer) belongs to a different product" | §8.2 | flow 07 | **Hypothesis** | As J-70. |
| J-96 | RJ-3: `✓` at 48 with a `*` price tag — six weeks, a client complaint, three hours | §8.3 | — | **Confirmed** | |
| J-97 | "Solved beautifully for design components and dead for this material — the one product that shipped it here was switched off" | §8.3 | flow 05, post-mortem | **Confirmed** | |
| J-98 | "§5's live link is the single mechanism in the spec that exists for exactly this job" | §8.3 | CLAUDE.md §5 | **Confirmed** | |
| J-99 | EJ-1 "belongs in the core as a rule, not as a row" | §8 | — | **Hypothesis** (R) | |
| J-100 | EJ-3 / H-J5 is "the highest-importance job in the matrix that the product cannot close" — Q12 | §8 | matrix | **Confirmed** | |
| J-101 | RJ-1 scores P1 = 2, P2 = 3, market nobody; "that number is an inference: the respondent found out on a call and never said he wanted to know beforehand" | §8 | — | **Confirmed** (as self-description of J-61) | It is the admission that the cell breaks the matrix's rule. |
| J-102 | RJ-1 "is also the job the spec has invested in most heavily" | §8 | — | **Hypothesis** (R) | Defensible from §6 and §8's word count; not measured. |
| J-103 | Agrees with §6 and §8 on the handover and with §5's live link; qualifies §2; touches no surface in §8 | §8 | — | **Confirmed** (the document's stated position) | |

### §9 and §10 — What might not be worth building; hand-forward

| ID | Claim | Where | Cites | Class | Note |
|---|---|---|---|---|---|
| J-104 | The shelf and switch: every cell `[?]`; P3 never observed; 13.4% critical in 3,984 (R6); "the most crowded space in the entire survey"; Q9 | §9 table | — | **Confirmed** | R6 published-not-verified; OBS-12; register. |
| J-105 | The example project: §11's reasoning is sound reasoning and not evidence; OBS-36 supports the shape, never the need | §9 table | — | **Confirmed** | |
| J-106 | Duplicate a project: `[?]` entirely; §2 names it; nobody has said it; the market closes it in a keystroke | §9 table | A-3, flow 09 | **Confirmed** | |
| J-107 | Promote: "One aside, `*`, and it is **Q10**… promotion only has value if in-project editing exists. Both stand on the same single `[?]`" | §9 table | Q4 | **Hypothesis** (the link to Q10 does not hold) | Q4's disposition is quoted correctly. But the one aside is about an external conflict (J-54); no one has said anything about wanting a per-project override. Promote and in-project editing stand on **nothing**, not on one aside. |
| J-108 | Search and filters: the market's best-served flow (B1); "a cost priced at **300 items, which nothing supports** (R4). **Build it for 20–40, not for 300**" | §9 table | patterns.md, R4 | **Confirmed** (B1; the 300 note) · **Invented** (the instruction) | `patterns.md`'s standing note says the reports are *"enough to refute 300, not enough to replace it with a number"*. "Build it for 20–40" replaces it with a number made of one organisation's threshold and one person's file count (P-10). Correction: "Do not price it against 300; no replacement figure exists". |
| J-109 | Per-item usage facts: "the strongest `*` in the repository — a practitioner invented our exact mechanism unprompted" | §9 table | NK-12 | **Confirmed** `*` | |
| J-110 | Publishing: §9 refuses it and the matrix agrees — SJ-2 scores 1 on a looked-for absence; every competitor that closes it needs a server | §9 | — | **Confirmed** | |
| J-111 | Composition: one of §9's two signals has failed — the `0 results` was a bug-shaped query on a frozen product; the friction is filed (#9444, #17401); the deferral stands on recursion | §9 | R3 | **Confirmed** | `user-pain.md` finding 4's standing note; CLAUDE.md §9. |
| J-112 | Versioning: #28729, 151, *"no version history, no review process, and no easy way to roll back a bad change"*, from an organisation context | §9 | gh log | **Confirmed** | Body verified; title says *organization skills*. |
| J-113 | "P3's column is entirely `[?]` — **nine rows out of nine**" | §10 | matrix | **Invented** (count) | The sourced matrix has **ten** rows: MAIN, RJ-1 to RJ-4, EJ-1 to EJ-3, SJ-1, SJ-2. The same "nine" is repeated in the stage 7 README and `FINAL.md` §6. Correction: "ten of ten". |
| J-114 | P2 carries a number in only three | §10 | matrix | **Confirmed** | |
| J-115 | Every P2 cell carrying a number is second-hand; RJ-1's P1 = 2 is an inference | §10 | — | **Confirmed** (self-assessment) | |
| J-116 | The whole orphan list rests on absences in instruments that cannot see presence | §10 | — | **Confirmed** (R) | |
| J-117 | Three questions come out for the guide, including one that "does not exist in the guide yet — **ask a receiver**" | §10 | guide | **Confirmed** (in the sense that matters) | The guide already **recruits** a receiver (§2, P3: *"or received one"*) but every question in §4 is addressed to an author. The missing thing is a receiver's question block, not a receiver's profile. See P-119. |

## Counts

| | Claims | Confirmed | Hypothesis | Invented |
|---|---|---|---|---|
| `personas.md` | 121 | 87 | 22 | 12 |
| `jtbd.md` | 117 | 76 | 26 | 15 |
| **Both** | **238** | **163** | **48** | **27** |

Rows classified in two parts (an utterance confirmed, a number invented) are counted under the
stronger finding — Invented over Hypothesis over Confirmed. The tally was made by script over the
table above, not by hand. A *Confirmed* `*` is confirmed as one respondent's statement and is a
hypothesis about anyone else; that is stated once here rather than thirty times in the table.

**The twelve invented claims in `personas.md`:** P-06, P-10, P-13, P-23, P-37, P-71, P-89, P-107,
P-108, P-114, P-116, P-119. Three more are classified *Hypothesis* because the surrounding sentence
is defensible, and the owner should still read them: P-42's "honest weighting", P-84's "single
strongest argument", P-67's *last actually useful* settlement.

**The fifteen in `jtbd.md`:** J-14, J-24, J-32, J-51, J-52, J-59, J-61, J-62, J-68, J-74, J-76,
J-91, J-94, J-108, J-113.

**A pattern, not a coincidence.** Thirteen of the twenty-seven are **superlatives or counts** — *the
only*, *the largest*, *the two loudest*, *fifteen products*, *eight threads*, *nine rows*, *half of
every card*, *usually*. None of them changes a finding's direction; every one of them changes how
much a reader is allowed to lean on it. Four are **numbers in matrix cells** that the matrix's own
rule forbids (J-59, J-61, J-62, J-74). Two are **marks the register had already withdrawn or never
granted** (J-32, P-71). One is a **misattributed quote** (P-37), one a **misattributed source**
(P-89), one an **inference that reverses its source** (P-13), and two are **false statements about
the document's own text** (J-51, J-52).

## Against their own plans

**`personas.md` against stage 6, step 3.** *No block unsourced and unmarked* — met, with the
exceptions above where a mark outruns its source (P-06, P-71, P-23). *Every block answers a named
design question* — met by the *allowed to settle* sections, two of which claim more than their
marks (P-67, P-85). *The primary is chosen with an argument that names what would overturn it* — met.
*A quote is a real issue body with URL and reactions* — met for P2; **not met for P1**, whose quote
is an HN comment with no reaction count and no log entry, under a restated rule the file does not
announce as a change (P-65); met for P3 by leaving the box empty. The environment block the plan
added is filled. *Roughly half of every card will be hypothesis* — the plan's prediction was wrong
in the reassuring direction for P1 and P2, and the file repeats the prediction as if it had held
(P-116).

**`jtbd.md` against stage 7, steps 1–5.** Step 1: *one chosen, or two surviving and recorded as a
register entry rather than a choice* — the file does both: it records E as surviving and Q12, **and**
chooses the transfer job as main and builds §8 on it. The plan's rule was not to pick by taste if two
survive; the file picks and calls the second a rival. Defensible, but it is a choice the plan said to
hand to the sitting. Step 2: three to five related jobs, each sourced — met. Step 4: the grep test —
**passes** on the *I want* clauses; the file's own account of the test contains two false statements
(J-51, J-52). Step 5: *no cell holds a number without a source line* — **not met**: J-61 is a number
on a self-declared inference, J-74 a number on evidence the cell calls weightless, J-59 and J-62
numbers for a person nobody asked. *No averaged cells* — met. The two conclusions — met, with the
orphan list correctly labelled a list of hypotheses. Steps 6 and 7 — this document is step 6; the
reconciliation table and the merge of questions into the guide are still owed, and Part 3 below is
written so that the merge can be done from it.

---

# Part 2 — The dangerous list

Claims that bear on a design decision and stand on `[?]`, on one person, or on invention. **Ranked
by the size of the `CLAUDE.md` commitment that rests on the claim, then by how far the claim's
wording overruns its mark.** A cheap feature on a false superlative ranks below an expensive surface
on an honest `[?]`.

> **Dated note, 2026-09-10 — read before the list.** This audit is a **record of what was true on
> 2026-09-09** and is not rewritten. But **D-1 has since been closed**, and a reader consulting the
> dangerous list before a design decision should know it:
> [`6-personas/re-research.md (round 3)`](6-personas/re-research.md#round-3-five-questions-that-need-no-interview) Q-F ran the handover test on
> 2026-09-10. **Three receiving agents out of three performed the setup**, so the claim D-1 called
> unsupported is supported. **And the half nobody had thought to doubt failed**: with the set's
> defects undisclosed, one receiver found them, one closed a real conflict on a false claim of
> byte-identity, and one saw none. **D-2's receiving half was partly addressed too** — 25 receivers
> observed in public diffs, which is behaviour where every P2 number was second-hand. **Every other
> row below stands as written.**

| # | ID | The claim | What it stands on | The decision it endangers | What breaks if it is wrong |
|---|---|---|---|---|---|
| ~~D-1~~ **CLOSED 2026-09-10** | P-79 · NK-13 · H6 | A receiving agent performs the setup correctly from `SETUP.md` alone | ~~**Nothing.** `[?]`; never run once. Both documents say so.~~ **Run: performs yes, three of three; checks correctly, no.** Q-F | §6: `SETUP.md` written for the agent, per item in the resolved set; §8: the handover stages as the last stages of Run; the Q2 disposition that made `SETUP.md` a real artefact | The spec's most load-bearing bet. If a fresh agent does not act on prose, the archive still lands and does not run — the exact pain the product is aimed at — and the handover stages disclose something nobody executes. Every other row below is downstream of this one. |
| D-2 | P-07 · P-71 · P-84 · J-59 · J-62 | P2 exists as a population, usually runs a different agent from the author, and cares at level 3 | One issue's motive sentence, filed by an **author**; two more issues from authors on teams; one second-hand story in which the receiver changed nothing. The same issue anchors P1's X2 end. | §6: who `SETUP.md` is addressed to and what it must state; §6: the **agent target selector** and its prominence; §8: the handover stages; §11's rationale that provenance is for someone else's reader | If receivers are mostly the **same person on a second machine**, the target selector is doing less than assumed and `SETUP.md`'s reader is the author. If receivers are on the **same** agent as the author, the four-target adaptation is over-built. If receivers are rare, a whole persona and the P2 column of the matrix are decoration. |
| D-3 | P-10 · J-108 | A personal collection holds **20 to 40 items**, and the Library should be built for that | One organisation's shared-skills threshold (with multiple contributors) and one person's *"40-something files"*, blended into a range. `patterns.md` says no replacement figure exists. | §8: the accepted cost of **no library pane** in the builder, priced against 300; the palette as the only route from Library to Project; §11's ~30-item shelf; §8's Library filters and search | If collections run to 100+ (skills, templates, MCP configs, prompts and scripts together, as the respondent's does), the palette-only assembly and "Library one keystroke away" fail at exactly the scale stage 5 priced for and the file now says not to price for. If they run to 5–10, the Library screen and its filters are the market's best-served flow built for nobody. Either way, "build it for 20–40" is a number with two data points under it. |
| D-4 | P-102 · J-104 · H7 · H8 | The empty-handed persona exists in numbers that justify shipping a shelf | **`[?]` entirely.** Vendor counts, tool stars (unlogged), one commenter's install figure the card missed. Not one observed person. | §8: the `My library` / `Public library` scope switch; §11: ~30 real items with provenance, a pinned `ref`, a licence check and a **content-review standard the spec does not have**; §11: the example project | A build commitment — real items from checked sources, composed to produce a Problem and a Note — spent on a persona nobody has met, in the most crowded space in the survey, with 13.4% of comparable public material carrying critical issues. And the reverse: if Q5 answers *material, not keeping*, P3 is primary and §8's weighting of Run over Library is wrong. |
| D-5 | J-61 · J-25 | Senders want to know what the other side will need **before** they send (RJ-1, P1 = 2) | A self-declared inference. The one sender on record found out on a call and did not say he wanted to know beforehand. | §6, §8: the **disclosure stages before Export** — `SETUP.md` preview, pinned `ref`s, target paths, `.env.example` — read before the irreversible step | If senders do not read them, Run's last stages lengthen the check for no reader, and the consequence-disclosure standard the spec holds itself to is performed to an empty room. The stages may still be right for the *receiver*; nobody has asked one (D-2). |
| D-6 | J-107 · J-54 · H-J3 | A user wants to change one copy for one project without touching the rest | **Nothing.** The one aside cited is about an external conflict (Q10); no one has mentioned wanting an override. | §5: `detached`, `overrides`, promotion **as a new item**; §7: state 6 with the differing fields named; the Q4 disposition that put **in-project editing** in the MVP | Three mechanisms and the hardest card state in §7 stand on zero evidence. The spec already notes promotion has value only if in-project editing exists; both now stand on nothing rather than on one aside. Flow 05 found no prior art for the return path — the one feature that is invented rather than copied is also the one with no demand behind it. |
| D-7 | J-66 · J-32 · P-31 | Fixing once and having it reach every copy is a level-3 job for P1 (RJ-3) | One filed request (48) and one `*` story whose respondent still moves material by `cp -r`; a corroboration the register un-marked and `jtbd.md` re-marked. | §5: **live link by default**, blast radius (*used in 3 projects*), detach as the exception | If practitioners in fact want copies — which is what the respondent's own behaviour shows, bootstrap script notwithstanding — link-by-default plus blast-radius warnings solves a problem people route around, and every edit to a library item becomes a confirmation nobody asked for. |
| D-8 | P-67 · P-51 · NK-12 | The item card should carry *last actually useful*, counted per session, rather than *last exported* | One person, unprompted — the strongest `*` in the repository, and still n = 1. The data model has no session concept and no runtime. | §5: the per-item usage facts (*used in 3 projects*, *last exported*); §10: no backend, client-side only | If built: a field with no data source, which is the decoration §5 refuses. If ignored: the one thing a practitioner asked for in our own words is dropped. The card claims the right to settle this; it has the right to raise it. |
| D-9 | J-70 · J-95 | Nobody in the space keeps secrets out of a handed-over artefact, so RJ-4 is in the core | Fifteen benchmark cells; Doppler and Infisical captured and not scored; `tank` and `asm` claiming credential scanning, unrun | §8's *what to build first* — RJ-4 is second by the rule *not closed by the market*; §6's `.env.example` as a differentiator rather than hygiene | Low breakage — `.env.example` is cheap and right either way — but the shortlist's second place was awarded by a test that was not run against the products that exist. |
| D-10 | J-14 · J-68 · J-94 · P-42 | The secrets crowd is the largest in the corpus; 182 is the second-loudest number; 182:13 is the honest weighting | Superlatives the logs refute; a ratio the repository's own rule forbids | §8's ranking method, stated as "applied mechanically"; the relative weight of RJ-4 against RJ-3 and the collision job | If the ranking is by count, the counts are wrong; if it is by judgement, it should say so. The collision check (§6) — the product's original thesis — is weighted at "a factor of fourteen" below an environmental pain the product cannot fix. |
| D-11 | P-13 · H1 | P1 arrives irritated more often than not | One person, and the sentence reverses his own frequency ordering | §6: the copy register for a Problem and a Note | Low cost, direct effect: tone tuned to a mood the source ranks second. The right register is still unknown. |
| D-12 | P-107 · P-108 · P-116 | P1 is the only persona with `✓` and `*` agreeing; the doubt spans eight threads; half of every card is `[?]` | Overstated counts | Q7 — which persona wins design conflicts | Reason 1 for the primary is weaker than written; reasons 2–4 still carry the choice. The risk is a reader trusting P1's card at `✓` strength because it was told it is only half hypothesis when it is mostly `*`. |
| D-13 | J-74 · J-59 | EJ-2 and the P2 = 3 cells hold numbers on weightless or second-hand evidence | The matrix's own rule, broken | §6: *Skipped*'s neutral glyph; §5: no score — both already decided on reasoning | Nothing breaks; the cells lend the decisions evidence they do not have. |

---

# Part 3 — Three questions, and where the answers are

Chosen for instruments that exist, over questions that merely matter. The observability question
(Q12) is the sharpest thing either stage produced and is **not** here, because its instrument —
guide Q25, four more times, before any description — is already named in the register and needs
nothing from this audit.

## Q-A — Does a fresh agent actually perform the setup from `SETUP.md` alone, and what does it do when an item's requirement cannot be met?

**Closes:** D-1 outright; D-5's receiver half; the mechanism under D-2. It is H6 and NK-13, the one
row both documents say is ours to fill.

**Where to look.** Nowhere public; on this machine. Compose a set of five to eight items by hand from
material that already exists in the repository's evidence — an MCP server config with a hard-coded
absolute path (the respondent's own failure, Q5), a server needing a Node version the container
does not have (Q11), two items writing to `.mcp.json` with the same server key (§6's collision), one
item with a `needsEnv` key deliberately missing, one external repo at a pinned `ref`. Write the
`SETUP.md` §6 describes, per item. Then, in **three** fresh, empty directories, open the archive with
a fresh **Claude Code**, **Cursor** (agent mode) and **Codex CLI** session, with the single
instruction *"set this project up"* and nothing else, and record per item what each agent did:
cloned, placed, merged, asked, skipped, or carried on without it. A fourth run — `Universal` target
handed to any one of them — tests whether the neutral structure adapts. Half a day, not an
afternoon, because three agents and four targets.

**A good answer** is a table, agent × item × outcome, with at least one failure in it — the run
where the agent *"carries on without them, cheerfully"* (Q11) is the result that tells us whether
the disclosure stages before Export have to say more than the archive contains. **A bad answer** is
*"it worked"* on one agent, with the author watching and nudging; or a run on the author's own
machine where every path already resolves. The run has to be on a machine that does not have what
the archive assumes, or it tests nothing.

## Q-B — Who receives a handed-over agent setup, on which agent, and what did they do in the first hour?

**Closes:** D-2 and D-5 directly; the P2 column of the matrix (J-59, J-62, J-72); H5. It is the
question the guide recruits for and never asks.

**Where to look, in two halves — one re-runnable, one that needs a person.**

*The re-runnable half* is the instrument the register already names under Q7 and nobody has run:
**GitHub code search** for repositories that carry more than one agent's material side by side —
`path:.claude/ path:.cursor/rules`, `filename:CLAUDE.md filename:AGENTS.md`, `path:.claude/skills
path:.agents/skills` — filtered to repositories with **two or more contributors**. Sample thirty.
For each, read the commit log of the agent files: did a second contributor ever touch them, and did
the commit that added the second agent's directory come from the same author as the first? That
observes receivers instead of asking authors about them, and it observes which agent they brought.
The GitHub search works (stage 6 confirmed it; Stack Overflow does not, Reddit is blocked).

*The half that needs a person:* two of the four remaining interviews should be **receivers**, recruited
through the guide's own P3 profile with the second clause made the screen — *"has somebody handed you
a repo with `.claude/`, `.cursor/rules` or `AGENTS.md` already in it?"* Where: the **Claude Code
Discord's help channels** and the **Cursor Discord**, which R13 names and which the tooling cannot
read but a person can post to; the ask is a thirty-minute call, no product mentioned. Add one block
to the guide, addressed to the receiver, in the guide's own register: *"take me through the first
hour after you opened it — what ran, what didn't, how did you find out, did you tell anyone."* The
guide has no such block; this is the merge stage 7 step 6 owes.

**A good answer** names the receiver's agent, whether it matched the author's, and what they did
about the parts that failed — worked around, asked, fixed, or never noticed. Two receivers on the
same agent as their author, fixing paths themselves, would move the target selector down and
`SETUP.md`'s reader back to the author. **A bad answer** is another author's account of a receiver,
or a receiver who says the archive *"would be useful"* — the guide's own rule 2.

## Q-C — What does a real, public agent-material repository contain: how many items, of which kinds, and how many of them are somebody else's?

**Closes:** D-3 (the 20–40 figure), and the observed half of D-4 (whether anyone in the wild installs
other people's material into their own collection — H-J4, H7); it also produces the first count of
kinds that §5's six `kind`s can be checked against.

**Where to look.** **GitHub repository search**, sorted by stars and by recent push, for the shape
the respondent described and R5 named: personal repositories whose name or description carries
`agent-kit`, `agent-dotfiles`, `claude-config`, `ai-rules`, `dotfiles` **and** which contain
`.claude/skills/` or `CLAUDE.md` or `.cursor/rules` — the stage-6 plan's step 5 instrument, listed
in `README.md` and never run. Take fifty. For each, count with the tree API: skill directories,
instruction files, MCP config entries, prompt files, scripts; note the repository's age from its
first commit; and count **provenance** — `SKILL.md` files whose frontmatter names an author or
source other than the repository owner, `.agents/skills/` directories pulled from a marketplace, a
`skills.lock` or similar. Also read the commit history for a **deletion**: NK-3's claim that the
folder only grows is testable on a git log, and the register says so.

**A good answer** is a distribution — median and spread of items per repository, by kind, with age
— and a fraction of items that are third-party. A median near 40 with a long tail past 150 says the
palette-only builder must survive the tail; a median near 12 says §11's ~30-item shelf is larger
than most people's own collection. A third-party fraction above zero is the first observed P3
behaviour anywhere in the phase. **A bad answer** is fifty repositories that are all awesome-lists
and marketplaces — filter those out by requiring a `CLAUDE.md` at the root that is not a README —
or a count of *files* that treats a 200-line rules file and a skill directory as one item each
without saying so, which is exactly how the current 20–40 was made.

---

**What this document does not do.** It edits nothing. It proposes twenty-seven corrections in Part 1's
*Note* column; applying them is the owner's, or the next revision of each file's. It adds no register
entry: every gap found above already has one (Q5, Q7, Q9, Q10, Q12) or is NK-13. Part 3's Q-B block
for the guide is the stage 7 step 6 merge, written here and not yet in `interviews.md` the guide.
