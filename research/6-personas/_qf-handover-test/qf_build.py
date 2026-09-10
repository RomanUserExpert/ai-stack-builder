"""Q-F step 2 - the generated half of the archive, exactly as CLAUDE.md 6 describes it.

  .mcp.json     all MCP servers merged into a single config
  .env.example  every env key collected across the resolved set
  SETUP.md      per item in the resolved set, what that item requires

SETUP.md deliberately does NOT name the Problems in this set. The spec puts the
disclosure of findings in Run, before Export, for the SENDER (CLAUDE.md 8); what
the receiving agent gets is the per-item statement of requirements and nothing
else. Whether it notices the duplicate command name and the path collision by
itself is the thing this test is trying to find out, so telling it would destroy
the measurement.
"""
import json, os, zipfile

HERE = os.path.dirname(__file__)
QF = os.path.join(HERE, 'qf')
ARCH = os.path.join(QF, 'archive')
M = json.load(open(os.path.join(QF, '_qf_manifest.json'), encoding='utf-8'))

TARGET = 'Claude Code'

# ---- merged MCP config. Two items declare `memory`; one of them wins, in silence,
# ---- which is the collision CLAUDE.md 6 says must be named. It is not named here.
servers, mcp_losers = {}, []
for s in M['mcp']:
    if s['key'] in servers:
        # last writer wins; the one already there is the one that will not be in the config
        mcp_losers.append(prev_by_key[s['key']])
    prev_by_key = locals().get('prev_by_key', {})
    prev_by_key[s['key']] = s['id']
    servers[s['key']] = s['config']
with open(os.path.join(ARCH, '.mcp.json'), 'w', encoding='utf-8') as f:
    json.dump({'mcpServers': servers}, f, indent=2)

# ---- env keys collected across the resolved set
env_keys = []
for s in M['mcp']:
    for k in s['needsEnv']:
        if k not in env_keys:
            env_keys.append(k)
with open(os.path.join(ARCH, '.env.example'), 'w', encoding='utf-8') as f:
    f.write('# Collected from the items in this project. Nothing here has a value yet.\n')
    for k in env_keys:
        f.write('%s=\n' % k)

# ---- SETUP.md, addressed to the agent that opens the project
L = []
w = L.append
w('# SETUP')
w('')
w('This document is addressed to the coding agent that opens this project, not to a human reader.')
w('Read it, then perform the setup it describes.')
w('')
w('**Agent target:** `%s`. Paths below are already correct for that target.' % TARGET)
w('')
w('## What is already in place')
w('')
w('These files ship inside this archive and are already at their target paths. Do not fetch them.')
w('')
w('| Item | Kind | Lands at | From | Pinned at |')
w('|---|---|---|---|---|')
for it in M['items']:
    w('| `%s` | %s | `%s` | [%s](%s/blob/%s/%s) | `%s` |' % (
        it['id'], it['kind'], it['targetPath'],
        it['repoUrl'].split('github.com/')[1], it['repoUrl'], it['ref'], it['path'], it['ref'][:7]))
w('')
w('## What each item requires')
w('')
for it in M['items']:
    w('### `%s` — %s' % (it['id'], it['kind']))
    w('')
    w('- Lands at `%s`.' % it['targetPath'])
    w('- Source: `%s` at `%s`.' % (it['repoUrl'], it['ref']))
    if it.get('requires'):
        w('- Requires these other items in this project: %s. They are in this archive; '
          'nothing to fetch.' % ', '.join('`%s`' % r for r in it['requires']))
    if it.get('command'):
        w('- Registers the slash command `/%s`.' % it['command'])
    if it['id'] == 'with-server':
        w('- Needs the Python package `playwright` on the machine that runs it '
          '(`pip install playwright && playwright install chromium`).')
    if it['id'] in ('settings-showcase', 'settings-skills'):
        w('- Writes agent settings. Merge it with any settings the receiving machine already has '
          'rather than replacing them.')
    w('- Requires no MCP server and no environment variable.'
      if it['id'] not in ('webapp-testing',) else
      '- Requires a browser automation server on the machine; see `playwright-mcp` below.')
    w('')
w('## MCP servers')
w('')
w('All servers for this project are merged into `.mcp.json` at the root of this archive. '
  'Place that file where `%s` reads project MCP configuration, merging rather than replacing.' % TARGET)
w('')
w('| Server key | Command | Declared by | Pinned at | Environment it reads |')
w('|---|---|---|---|---|')
for s in M['mcp']:
    cfg = s['config']
    w('| `%s` | `%s %s` | %s | `%s` | %s |' % (
        s['key'], cfg['command'], ' '.join(cfg['args']), s['source'], s['ref'][:7],
        ', '.join('`%s`' % k for k in s['needsEnv']) or '—'))
w('')
w('## External items — never vendored, always instructions')
w('')
for e in M['external']:
    w('### `%s`' % e['id'])
    w('')
    w('Not present in this archive. Clone it at the pinned ref and place it at `%s`:' % e['targetPath'])
    w('')
    w('```bash')
    w('git clone %s %s' % (e['repoUrl'], e['targetPath']))
    w('git -C %s checkout %s' % (e['targetPath'], e['ref']))
    w('```')
    w('')
    w('The pinned ref is the version this project was checked against. It is not necessarily current.')
    w('')
w('## Environment')
w('')
w('`.env.example` at the root lists every environment key this project reads, collected across '
  'all of its items. **None of them has a value.** Copy it to `.env` and fill in what the '
  'machine can supply; report anything it cannot.')
w('')
for k in env_keys:
    w('- `%s`' % k)
w('')
w('## When you are done')
w('')
w('State what you did, what you could not do, and what the machine still needs from a human.')
w('')

with open(os.path.join(ARCH, 'SETUP.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(L))

# ---- zip it
zp = os.path.join(QF, 'project-archive.zip')
with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _dirs, files in os.walk(ARCH):
        for fn in files:
            p = os.path.join(root, fn)
            z.write(p, os.path.relpath(p, ARCH).replace(os.sep, '/'))

print('mcp servers merged :', list(servers))
print('mcp keys lost      :', [s['id'] for s in mcp_losers])
print('env keys           :', env_keys)
print('archive            :', zp, os.path.getsize(zp), 'bytes')
