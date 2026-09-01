# What actually hurts — evidence from issue trackers

Collected 2026-09-01. The gap this closes: **nothing in the research had ever established what hurts
the user.** [`1-landscape/comparison.md`](../1-landscape/comparison.md) compares fifteen vendors on audience, product base, key
mechanism, trust and monetisation — five axes about *companies*, none about *pain*. The word "pain"
appeared in zero files. CLAUDE.md §2 asserts the pain and the whole product rests on it:

> Nothing tells you that a skill needs a particular MCP server, that two items write to the same
> config file, or that an env key is missing. **You find that out at runtime.**

That was never checked. This document checks it, and the answer is partly uncomfortable.

## Method, and the bias to hold in mind the whole way down

Two public trackers, searched through the GitHub API, unauthenticated:
[`continuedev/continue`](https://github.com/continuedev/continue) (6,677 issues — the closest dead
competitor, same object model) and
[`modelcontextprotocol/servers`](https://github.com/modelcontextprotocol/servers) (1,186 issues — the
ecosystem our `mcp` kind lives in). Ranked by reactions, which is the only crowd-weighting these
trackers offer. Raw results in [`_user-pain-issues.json`](_user-pain-issues.json).

**An issue tracker records breakage, not friction.** People file an issue when something is broken,
not when something is tedious. *"I can't find the prompt I wrote three months ago"* and *"I copied the
same four files into a new project again"* never become issues. So this instrument can speak to one of
our three candidate pains and is **structurally blind to the other two**. That limit is not a caveat
at the bottom of the page; it is the first thing to know about everything below.

| Candidate pain | Can this source see it? |
|---|---|
| **A. Loss** — material scattered, cannot find what I wrote | **No.** Produces no issues. |
| **B. Reassembly cost** — re-copying the same set into every new project | **No.** Produces silent tedium. |
| **C. Silent breakage** — I configured it and it does not work | **Yes.** This is what trackers are made of. |

---

## Finding 1 — the loud pain is environmental, not compositional

The single most-reacted issue in either repository, by a factor of eight over anything
configuration-related:

> **[MCP Servers Don't Work with NVM](https://github.com/modelcontextprotocol/servers/issues/64)** —
> **182 reactions, 91 comments**
> *"When using NVM (Node Version Manager), the standard installation and usage instructions for MCP
> servers don't work. The app tries to use an incorrect Node and fails."*

It is not alone. The top of `modelcontextprotocol/servers` is almost entirely *it will not start on my
machine*:

| Issue | Reactions |
|---|---|
| MCP Servers Don't Work with NVM | **182** |
| Environment variables not respected in `@modelcontextprotocol/server-memory` | 23 |
| Security Proposal: credential management in MCP servers | 22 |
| GitHub MCP Server fails to start: `npx` command error, connection closed | 19 |
| Memory MCP ignores custom storage path setting | 15 |
| Server transport closed unexpectedly, process exiting early | 14 |
| Time server fails under EDT timezone | 14 |
| `filesystem`: Windows path rejected on casing | 13 |
| Fix "Client Closed" error by correcting npm config | 12 |

PATH, node version managers, platform-specific paths, timezones, processes dying at startup. **The
config is correct and the thing still does not run.**

**Most of this is out of our reach.** We validate a *set*; we cannot fix a user's `PATH`. Where it
touches us is the one place our output meets their machine: `SETUP.md` and the generated `.mcp.json`.

## Finding 2 — our thesis is observed, but quietly

It is there. It is just not loud.

> **[Unable to run multiple instances of `@modelcontextprotocol/server-postgres`
> simultaneously](https://github.com/modelcontextprotocol/servers/issues/1219)** — 13 reactions
> *"It's not possible to run multiple instances … to connect to different databases (e.g. production
> and development). When doing this, **the chat always chooses the first one specified in order of
> `mcp.json`**."*

That is our duplicate-key collision, reported by a user, in the exact file we generate, with the exact
failure mode we predicted: **the first one wins and nobody is told.** It is the same behaviour we
found in Continue's own source, where `BlockDuplicationDetector` correctly identifies the duplicate
and the merge silently discards the loser — see [`1-landscape/continue-postmortem.md`](../1-landscape/continue-postmortem.md).
Two independent sightings of one bug: once in the code, once in a user's words.

Two more of the same family, smaller:

> **[Multiple models with autocomplete role in
> config.yaml](https://github.com/continuedev/continue/issues/4306)** — *"How can I choose the
> autocomplete model when I define a few models that have autocomplete role?"* Two items claim one
> role and the user cannot tell which will win.
>
> **[Multiple local configs is not explained
> clearly](https://github.com/continuedev/continue/issues/8484)** — *"The documentation mentions
> 'Local Configs' in the plural form several times, but it's unclear how to actually set up multiple
> local configs."* Composition, not understood.

Plus `config.yaml contextLength is not applied to model`, and `toolOverrides not applied in system
message tools path` — *I set it and it was ignored*, which is the whole family in one sentence.

**Verdict on the bet.** Real, sighted, and small: 3 to 13 reactions, against 182 for the loud one.
CLAUDE.md's claim is **true and under-evidenced as a headline**. It describes a genuine failure that
users do hit and do not currently get told about. It does not describe the thing they shout about.

## Finding 3 — env and secrets rank higher than we assumed

Not a hypothesis we had, and it sits near the top of both trackers:

- **[storing api keys in plain text](https://github.com/continuedev/continue/issues/1729)** —
  32 reactions, 26 comments, on Continue.
- **Environment variables not respected in `server-memory`** — 23 reactions.
- **Security Proposal: credential management in MCP servers** — 22 reactions.
- **`[server-gitlab]` environment variables not properly expanded in Claude Desktop.**

Our §6 already collects `needsEnv` across the set and writes `.env.example`, and keys never enter the
archive. That was designed as hygiene. **It turns out to be aimed at a top-ranked pain**, which also
raises the value of the Vercel env-drawer findings in
[`2-flows/07-env-and-secrets/NOTES.md`](../2-flows/07-env-and-secrets/NOTES.md) — asking for the type before
the value, defaulting to the irreversible option, and a note field that asks *where to rotate, or who
to contact*.

## Finding 4 — nobody is asking for a composition layer

The uncomfortable one. Searches for sharing and reuse across projects return **nothing**:

- `reuse blocks assistant` in `continuedev/continue` — **0 results.**
- `share config across projects` — 12 results, all unrelated noise (autocomplete freezing, JetBrains
  URI errors).

In a 6,677-issue tracker for a product that **shipped a hub for exactly this**, there is no visible
pull for it. Set beside the post-mortem — the hosted hub is the half that was switched off, the local
client is the half still running on 1.58M machines — that is **two independent signals pointing the
same way**: the composition-and-sharing layer is not what users pull for.

Held against Finding 1's blindness caveat: reuse *friction* would not produce issues either. So this
is evidence of **no demand loud enough to file**, not evidence of no need. But it is one more reason
not to lead with sharing.

## What this changes

**Keep.** The validation pass. Finding 2 shows the failure is real and currently silent, and Finding 3
shows the env half of it is aimed at something people care about a lot. Nothing here says stop.

**Re-weight.** CLAUDE.md §6 gives `SETUP.md` a single line — *"external items become instructions in
`SETUP.md`"*. Finding 1 says the loudest pain in the whole ecosystem lives exactly there: the archive
lands on a machine and does not run. The generated setup instructions, the pinned `ref`, and the
platform-correct `targetPath` deserve more design attention than one bullet. The wow moment is *a
working archive*, and "working" is where users are actually bleeding.

**Do not lead with.** Sharing, publishing, a catalog. Finding 4 plus the post-mortem agree.

**Still unknown, and this source cannot tell us.** Whether loss (A) or reassembly cost (B) is what
would actually make someone adopt this. Both are invisible to issue trackers by construction. If we
ever want that answer it needs a different instrument — asking people, or watching them — and it is
worth saying plainly that we have not done it.
