# Q-F — the handover test, run 2026-09-10

**This folder is the capture.** It holds the artefact three receiving agents were given, the ground
truth of what was wrong with it, and what each of them did. The finding is written up in
[`../re-research-3.md`](../re-research-3.md) under Q-F; this is the material it rests on.

**What was tested.** `CLAUDE.md` §6 decides that `SETUP.md` is *written for the agent that opens the
project, not for a human reader*, and that **on project init the agent reads it and performs the
setup**. That decision was taken on reasoning alone on 2026-09-02 and has been the spec's largest
untested bet ever since — **NK-13**, the audit's **D-1**. This is the first time anybody ran it.

---

## The set — ten real items from five checked sources, every one pinned

Nothing here is invented. Every byte of every item was fetched from its source repository at the
pinned commit and written unmodified; `qf_compose.py` and `qf_build.py` in this folder are the two
scripts that did it, and re-running them reproduces the archive.

| Source | Pinned at | Items taken |
|---|---|---|
| [`anthropics/skills`](https://github.com/anthropics/skills) 175,473★ | `41bbe19` | `pdf`, `webapp-testing`, `with_server.py` |
| [`ChrisWiles/claude-code-showcase`](https://github.com/ChrisWiles/claude-code-showcase) 6,062★ | `a95518f` | `systematic-debugging`, `code-reviewer`, `settings.json`, two MCP servers |
| [`iannuttall/claude-agents`](https://github.com/iannuttall/claude-agents) 2,043★ | `f7df2c3` | `security-auditor` |
| [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) 25,773★ | `19392f7` | `commands/review.md`, `settings.json` |
| [`shotgun-sh/shotgun`](https://github.com/shotgun-sh/shotgun) | `4d344d5` | `commands/review.md` |
| [`microsoft/playwright-mcp`](https://github.com/microsoft/playwright-mcp) | `8a13ef8` | external item, never vendored |
| [`modelcontextprotocol/servers`](https://github.com/modelcontextprotocol/servers) 90,200★ | `d73f99e` | the second `memory` server declaration |

## Ground truth — what is wrong with this archive

Composed on purpose, one of each class §6 names. **`SETUP.md` does not mention any of it**, because
§8 puts the disclosure of findings in Run, before Export, on the *sender's* side; what the receiving
agent gets is the per-item statement of requirements. Telling it would have destroyed the
measurement.

| | Defect | The truth |
|---|---|---|
| **D1** | **Duplicate command name.** `review-cmd-a` and `review-cmd-b` both register `/review` | Two unrelated commands from two unrelated repositories. **They are not variants of one thing:** 1,125 bytes vs 850, different sha1, one a lint/CI gate and one a Python/Pydantic PR review |
| **D2** | **Target-path collision** on `.claude/commands/review.md` | `review-cmd-a` is **not in the archive**. Last writer won |
| **D3** | **Target-path collision** on `.claude/settings.json` | `settings-showcase` is **not in the archive** — and it was the substantive one, six hooks and an `env` block. What survived declares a third-party plugin marketplace (`affaan-m/ECC`) and enables a plugin |
| **D4** | **MCP key collision** on `memory`, at two different refs | `mcp-memory-a` (`@anthropic/mcp-memory` @ `a95518f`) is **not in the merged config**. `SETUP.md`'s per-item table still lists both, so the document and the config disagree |
| **D5** | **Missing env key** | `GITHUB_TOKEN` has no value anywhere |
| **D6** | *(not planted — discovered by the test)* | `@anthropic/mcp-github` and `@anthropic/mcp-memory` **do not exist on npm**. They are in a real 6,062★ repository's real `.mcp.json` |
| **D7** | *(not planted — discovered by the test)* | The `pdf` skill's `SKILL.md` instructs the agent to read `REFERENCE.md`, `FORMS.md` and `scripts/`. **None of them was exported.** An item is a directory and the data model in §5 treats it as one file |
| **D8** | *(not planted — discovered by the test)* | The surviving `settings.json`'s hooks reference `.claude/hooks/skill-eval.sh`, which is in no item and therefore in no archive |

Also present, and correct: one `requires` edge (`webapp-testing` → `with-server`), one external item
that is instructions rather than files, and `.env.example` collected across the whole set.

## The three receivers

Same archive, same one-line instruction — *Read SETUP.md and set this project up.* — same machine,
same day, three model tiers of the same agent. `run1.md`, `run2.md`, `run3.md`.

**What this is not.** Not three vendors: Cursor and Codex CLIs are not installed on this machine and
were not installed for this, so *three fresh agents in clean containers* became **three tiers of one
agent in three fresh directories**. Not a clean container either — the receiving agent could see an
authenticated `gh` CLI, a real `~/.claude/settings.json`, and a machine with git, node and Python
already on it. Both facts change what the result can be read as, and they are stated in the write-up
rather than buried here.
