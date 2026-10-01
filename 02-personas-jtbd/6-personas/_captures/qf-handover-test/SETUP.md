# SETUP

This document is addressed to the coding agent that opens this project, not to a human reader.
Read it, then perform the setup it describes.

**Agent target:** `Claude Code`. Paths below are already correct for that target.

## What is already in place

These files ship inside this archive and are already at their target paths. Do not fetch them.

| Item | Kind | Lands at | From | Pinned at |
|---|---|---|---|---|
| `pdf` | skill | `.claude/skills/pdf/SKILL.md` | [anthropics/skills](https://github.com/anthropics/skills/blob/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/pdf/SKILL.md) | `41bbe19` |
| `webapp-testing` | skill | `.claude/skills/webapp-testing/SKILL.md` | [anthropics/skills](https://github.com/anthropics/skills/blob/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/webapp-testing/SKILL.md) | `41bbe19` |
| `with-server` | script | `.claude/skills/webapp-testing/scripts/with_server.py` | [anthropics/skills](https://github.com/anthropics/skills/blob/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/webapp-testing/scripts/with_server.py) | `41bbe19` |
| `systematic-debugging` | skill | `.claude/skills/systematic-debugging/SKILL.md` | [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase/blob/a95518f0cb67e86230119da40429169bc4c35a6f/.claude/skills/systematic-debugging/SKILL.md) | `a95518f` |
| `code-reviewer` | agent | `.claude/agents/code-reviewer.md` | [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase/blob/a95518f0cb67e86230119da40429169bc4c35a6f/.claude/agents/code-reviewer.md) | `a95518f` |
| `security-auditor` | agent | `.claude/agents/security-auditor.md` | [iannuttall/claude-agents](https://github.com/iannuttall/claude-agents/blob/f7df2c3e7395d163ad52d0793bac8fa7ce0d776a/agents/security-auditor.md) | `f7df2c3` |
| `review-cmd-a` | prompt | `.claude/commands/review.md` | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/.claude/commands/review.md) | `19392f7` |
| `review-cmd-b` | prompt | `.claude/commands/review.md` | [shotgun-sh/shotgun](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/.claude/commands/review.md) | `4d344d5` |
| `settings-showcase` | script | `.claude/settings.json` | [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase/blob/a95518f0cb67e86230119da40429169bc4c35a6f/.claude/settings.json) | `a95518f` |
| `settings-skills` | script | `.claude/settings.json` | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/.claude/settings.json) | `19392f7` |

## What each item requires

### `pdf` — skill

- Lands at `.claude/skills/pdf/SKILL.md`.
- Source: `https://github.com/anthropics/skills` at `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`.
- Requires no MCP server and no environment variable.

### `webapp-testing` — skill

- Lands at `.claude/skills/webapp-testing/SKILL.md`.
- Source: `https://github.com/anthropics/skills` at `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`.
- Requires these other items in this project: `with-server`. They are in this archive; nothing to fetch.
- Requires a browser automation server on the machine; see `playwright-mcp` below.

### `with-server` — script

- Lands at `.claude/skills/webapp-testing/scripts/with_server.py`.
- Source: `https://github.com/anthropics/skills` at `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`.
- Needs the Python package `playwright` on the machine that runs it (`pip install playwright && playwright install chromium`).
- Requires no MCP server and no environment variable.

### `systematic-debugging` — skill

- Lands at `.claude/skills/systematic-debugging/SKILL.md`.
- Source: `https://github.com/ChrisWiles/claude-code-showcase` at `a95518f0cb67e86230119da40429169bc4c35a6f`.
- Requires no MCP server and no environment variable.

### `code-reviewer` — agent

- Lands at `.claude/agents/code-reviewer.md`.
- Source: `https://github.com/ChrisWiles/claude-code-showcase` at `a95518f0cb67e86230119da40429169bc4c35a6f`.
- Requires no MCP server and no environment variable.

### `security-auditor` — agent

- Lands at `.claude/agents/security-auditor.md`.
- Source: `https://github.com/iannuttall/claude-agents` at `f7df2c3e7395d163ad52d0793bac8fa7ce0d776a`.
- Requires no MCP server and no environment variable.

### `review-cmd-a` — prompt

- Lands at `.claude/commands/review.md`.
- Source: `https://github.com/alirezarezvani/claude-skills` at `19392f7a08264ed00486a251f5b2098321771f94`.
- Registers the slash command `/review`.
- Requires no MCP server and no environment variable.

### `review-cmd-b` — prompt

- Lands at `.claude/commands/review.md`.
- Source: `https://github.com/shotgun-sh/shotgun` at `4d344d5a46aafc815de441ff670d4131187f33e6`.
- Registers the slash command `/review`.
- Requires no MCP server and no environment variable.

### `settings-showcase` — script

- Lands at `.claude/settings.json`.
- Source: `https://github.com/ChrisWiles/claude-code-showcase` at `a95518f0cb67e86230119da40429169bc4c35a6f`.
- Writes agent settings. Merge it with any settings the receiving machine already has rather than replacing them.
- Requires no MCP server and no environment variable.

### `settings-skills` — script

- Lands at `.claude/settings.json`.
- Source: `https://github.com/alirezarezvani/claude-skills` at `19392f7a08264ed00486a251f5b2098321771f94`.
- Writes agent settings. Merge it with any settings the receiving machine already has rather than replacing them.
- Requires no MCP server and no environment variable.

## MCP servers

All servers for this project are merged into `.mcp.json` at the root of this archive. Place that file where `Claude Code` reads project MCP configuration, merging rather than replacing.

| Server key | Command | Declared by | Pinned at | Environment it reads |
|---|---|---|---|---|
| `github` | `npx -y @anthropic/mcp-github` | ChrisWiles/claude-code-showcase | `a95518f` | `GITHUB_TOKEN` |
| `memory` | `npx -y @anthropic/mcp-memory` | ChrisWiles/claude-code-showcase | `a95518f` | — |
| `memory` | `npx -y @modelcontextprotocol/server-memory` | modelcontextprotocol/servers | `d73f99e` | `MEMORY_FILE_PATH` |

## External items — never vendored, always instructions

### `playwright-mcp`

Not present in this archive. Clone it at the pinned ref and place it at `vendor/playwright-mcp`:

```bash
git clone https://github.com/microsoft/playwright-mcp vendor/playwright-mcp
git -C vendor/playwright-mcp checkout 8a13ef8e9f7385a0f89477922127f31cbfde9761
```

The pinned ref is the version this project was checked against. It is not necessarily current.

## Environment

`.env.example` at the root lists every environment key this project reads, collected across all of its items. **None of them has a value.** Copy it to `.env` and fill in what the machine can supply; report anything it cannot.

- `GITHUB_TOKEN`
- `MEMORY_FILE_PATH`

## When you are done

State what you did, what you could not do, and what the machine still needs from a human.
