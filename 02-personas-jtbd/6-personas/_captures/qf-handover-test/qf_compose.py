"""Q-F step 1+2 - compose the set by hand, then build the archive exactly as CLAUDE.md 6 describes.

Ten real items from four checked sources, every one pinned at a commit SHA.
The set is composed to contain, on purpose:

  requires edge        webapp-testing -> with_server (script)
  duplicate command    two independent sources both register /review
  target-path clash    two independent sources both write .claude/settings.json
  missing env key      the github MCP server wants GITHUB_TOKEN, nothing supplies it
  mcp key clash        two items declare the server key `memory` at different refs
  external item        playwright-mcp is never vendored, only instructed, at a pinned ref

Nothing here is invented content: every byte of every item is fetched from its
source repository at the pinned ref and written unmodified.
"""
import json, os, sys, base64
from ghlib import gh, save

OUT = os.path.join(os.path.dirname(__file__), 'qf')
ARCH = os.path.join(OUT, 'archive')

SRC = {
    'anthropics/skills': '41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f',
    'ChrisWiles/claude-code-showcase': 'a95518f0cb67e86230119da40429169bc4c35a6f',
    'iannuttall/claude-agents': 'f7df2c3e7395d163ad52d0793bac8fa7ce0d776a',
    'alirezarezvani/claude-skills': '19392f7a08264ed00486a251f5b2098321771f94',
    'shotgun-sh/shotgun': None,  # resolved below
    'modelcontextprotocol/servers': 'd73f99efbfd40c3aa1b61e88728b3d49fb52608f',
}

ITEMS = [
    # id, kind, repo, path in repo, targetPath in the archive, extras
    ('pdf', 'skill', 'anthropics/skills', 'skills/pdf/SKILL.md',
     '.claude/skills/pdf/SKILL.md', {}),
    ('webapp-testing', 'skill', 'anthropics/skills', 'skills/webapp-testing/SKILL.md',
     '.claude/skills/webapp-testing/SKILL.md', {'requires': ['with-server']}),
    ('with-server', 'script', 'anthropics/skills', 'skills/webapp-testing/scripts/with_server.py',
     '.claude/skills/webapp-testing/scripts/with_server.py', {}),
    ('systematic-debugging', 'skill', 'ChrisWiles/claude-code-showcase',
     '.claude/skills/systematic-debugging/SKILL.md',
     '.claude/skills/systematic-debugging/SKILL.md', {}),
    ('code-reviewer', 'agent', 'ChrisWiles/claude-code-showcase',
     '.claude/agents/code-reviewer.md', '.claude/agents/code-reviewer.md', {}),
    ('security-auditor', 'agent', 'iannuttall/claude-agents',
     'agents/security-auditor.md', '.claude/agents/security-auditor.md', {}),
    # --- the duplicate command name: two independent sources, same registered name
    ('review-cmd-a', 'prompt', 'alirezarezvani/claude-skills', '.claude/commands/review.md',
     '.claude/commands/review.md', {'command': 'review'}),
    ('review-cmd-b', 'prompt', 'shotgun-sh/shotgun', '.claude/commands/review.md',
     '.claude/commands/review.md', {'command': 'review'}),
    # --- the target-path collision: two independent sources, same settings file
    ('settings-showcase', 'script', 'ChrisWiles/claude-code-showcase',
     '.claude/settings.json', '.claude/settings.json', {}),
    ('settings-skills', 'script', 'alirezarezvani/claude-skills',
     '.claude/settings.json', '.claude/settings.json', {}),
]

# MCP servers. Two of them declare the key `memory`, at different refs.
MCP = [
    {'id': 'mcp-github', 'key': 'github', 'source': 'ChrisWiles/claude-code-showcase',
     'ref': SRC['ChrisWiles/claude-code-showcase'],
     'config': {'type': 'stdio', 'command': 'npx', 'args': ['-y', '@anthropic/mcp-github'],
                'env': {'GITHUB_TOKEN': '${GITHUB_TOKEN}'}},
     'needsEnv': ['GITHUB_TOKEN']},
    {'id': 'mcp-memory-a', 'key': 'memory', 'source': 'ChrisWiles/claude-code-showcase',
     'ref': SRC['ChrisWiles/claude-code-showcase'],
     'config': {'type': 'stdio', 'command': 'npx', 'args': ['-y', '@anthropic/mcp-memory']},
     'needsEnv': []},
    {'id': 'mcp-memory-b', 'key': 'memory', 'source': 'modelcontextprotocol/servers',
     'ref': SRC['modelcontextprotocol/servers'],
     'config': {'type': 'stdio', 'command': 'npx',
                'args': ['-y', '@modelcontextprotocol/server-memory'],
                'env': {'MEMORY_FILE_PATH': '${MEMORY_FILE_PATH}'}},
     'needsEnv': ['MEMORY_FILE_PATH']},
]

EXTERNAL = [
    {'id': 'playwright-mcp', 'kind': 'mcp', 'repoUrl': 'https://github.com/microsoft/playwright-mcp',
     'ref': None, 'path': '.', 'targetPath': 'vendor/playwright-mcp',
     'note': 'never vendored into the archive - instructions only'},
]


def head_sha(repo):
    st, d, _ = gh('/repos/%s/commits' % repo, {'per_page': 1})
    if st != 200:
        raise SystemExit('cannot pin %s: %s' % (repo, d))
    return d[0]['sha']


def fetch(repo, ref, path):
    st, d, _ = gh('/repos/%s/contents/%s' % (repo, path), {'ref': ref})
    if st != 200 or not isinstance(d, dict) or 'content' not in d:
        return None, st
    return base64.b64decode(d['content']), 200


def main():
    for r, v in list(SRC.items()):
        if v is None:
            SRC[r] = head_sha(r)
            sys.stderr.write('pinned %s @ %s\n' % (r, SRC[r]))
    for e in EXTERNAL:
        repo = e['repoUrl'].split('github.com/')[1]
        e['ref'] = head_sha(repo)
        sys.stderr.write('pinned %s @ %s\n' % (repo, e['ref']))

    os.makedirs(ARCH, exist_ok=True)
    manifest = []
    for iid, kind, repo, path, target, extra in ITEMS:
        ref = SRC[repo]
        blob, st = fetch(repo, ref, path)
        if blob is None:
            sys.stderr.write('MISSING %s %s@%s %s -> %s\n' % (iid, repo, ref[:7], path, st))
            continue
        rec = {'id': iid, 'kind': kind, 'source': 'inline',
               'repoUrl': 'https://github.com/' + repo, 'path': path, 'ref': ref,
               'targetPath': target, 'bytes': len(blob)}
        rec.update(extra)
        manifest.append(rec)
        dest = os.path.join(ARCH, target.replace('/', os.sep))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        # a real target-path collision: last writer wins, and the archive is wrong
        with open(dest, 'wb') as f:
            f.write(blob)
        sys.stderr.write('%-22s %6d B -> %s\n' % (iid, len(blob), target))

    save('qf/_qf_manifest.json', {'sources': SRC, 'items': manifest,
                                  'mcp': MCP, 'external': EXTERNAL})
    print(json.dumps({'items': len(manifest)}))


if __name__ == '__main__':
    main()
