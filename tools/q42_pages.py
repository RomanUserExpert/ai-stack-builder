"""Q42 (owner, 2026-10-19: «да, создай»): a shared item reads as shared, and stopping is one press away — as Q37
decided for a project.

- On every page that draws My library's rows, the shared item (github-mcp, tagged `Shared`) reads `Stop sharing…`
  instead of `Share…`; on library-my-default it opens the new state.
- A new wireframe page, library-my-revoke.html: My library under the confirmation, worded as project-revoke.html is
  (§5, *Revocable, and honest about what revoking cannot do*).
- The viewer lists it under My library.

    python tools/q42_pages.py      (once; it refuses to run twice)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "04-wireframes" / "pages"
ROW = re.compile(r'(<h2><a href="item-default\.html">github-mcp</a><span class="tag">mcp</span><span class="tag tag-state">Shared</span></h2>'
                 r'(?:(?!</article>).)*?)<button type="button">Share…</button>', re.S)

DIALOG = '''
    <!-- Stop sharing an item (Q42, as Q37 for a project; §5): the address dies at once, what was taken stays taken. -->
    <div class="scrim" aria-hidden="true"></div>
    <dialog class="modal" open aria-labelledby="modal-title">
      <div class="sheet-head">
        <h2 id="modal-title">Stop sharing github-mcp?</h2>
      </div>
      <p>The link stops working at once.</p>
      <p>It can’t reach what was already taken: anyone who exported the item or copied it into a library keeps it.</p>
      <div class="form-actions">
        <a class="button push" href="library-my-default.html">Cancel</a>
        <a class="button button-primary" href="library-my-default.html">Stop sharing</a>
      </div>
    </dialog>
'''


def main():
    out = PAGES / "library-my-revoke.html"
    if out.exists():
        sys.exit("library-my-revoke.html exists — Q42 was applied already")
    changed = 0
    for p in sorted(PAGES.glob("*.html")):
        if p.stem == "wireframes":
            continue
        t = p.read_text(encoding="utf-8")
        link = '<a class="button" href="library-my-revoke.html">Stop sharing…</a>' if p.stem == "library-my-default" else '<button type="button">Stop sharing…</button>'
        t2, n = ROW.subn(lambda m: m.group(1) + link, t)
        if n:
            p.write_text(t2, encoding="utf-8")
            changed += 1
    base = (PAGES / "library-my-default.html").read_text(encoding="utf-8")
    page = re.sub(r"<title>[^<]*</title>", "<title>My library · revoke — wireframe</title>", base, count=1)
    page = page.replace('<a class="button" href="library-my-revoke.html">Stop sharing…</a>', '<button type="button">Stop sharing…</button>', 1)
    end = page.rindex("    </main>") + len("    </main>")
    page = page[:end] + "\n\n" + DIALOG + page[end:]
    out.write_text(page, encoding="utf-8")
    v = PAGES / "wireframes.html"
    vt = v.read_text(encoding="utf-8")
    anchor = '<li><a href="#library-my-filters"><svg class="wf-ico" aria-hidden="true"><use href="#i-file"/></svg><span class="wf-name">filters</span></a></li>'
    assert vt.count(anchor) == 1
    vt = vt.replace(anchor, anchor + '\n                  <li><a href="#library-my-revoke"><svg class="wf-ico" aria-hidden="true"><use href="#i-file"/></svg><span class="wf-name">revoke</span></a></li>')
    v.write_text(vt, encoding="utf-8")
    print(f"Q42: Stop sharing… on {changed} pages; library-my-revoke.html written; viewer lists it")


if __name__ == "__main__":
    main()
