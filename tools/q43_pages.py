"""Q43 (owner, 2026-10-23: «давай 2»): the owner can get a shared link again. A shared project or item keeps its
`Shared` tag and its button reads `Share…` again; on a shared object it opens the link — `Copy link`, and
`Stop sharing…` inside the dialog, which opens the confirmation Q37 and Q42 drew. `Create link` lands on the same
dialog, so the link is first seen there.

- Every `Stop sharing…` on a row, a card or a page head reads `Share…` (Q37 and Q42 are re-drawn, not undone:
  the tag still says the thing is shared, and stopping is one press inside the dialog).
- Two new wireframe pages: project-link.html and library-my-link.html, each over the shared state.
- The revoke confirmations' Cancel returns to the link; project-share's Create link lands on it.
- The viewer lists both under their screens.

    python tools/q43_pages.py      (once; it refuses to run twice)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "04-wireframes" / "pages"

# The address is drawn on a reserved domain (RFC 2606): the product's own domain is not decided anywhere.
LINK = '''
    <!-- A shared {what}'s link (Q43): the address again, to copy, and stopping it one step further (§5, Revocable). -->
    <div class="scrim" aria-hidden="true"></div>
    <dialog class="modal" open aria-labelledby="modal-title">
      <div class="sheet-head">
        <h2 id="modal-title">{name} is shared by link</h2>
      </div>
      <p>Anyone with the link can open this {what} and see it as it is now — and every edit you make later.</p>
      <label class="field"><span>Link</span>
        <input type="text" readonly value="https://aistack.example/s/{ref}">
      </label>
      <div class="form-actions">
        <a class="button" href="{revoke}">Stop sharing…</a>
        <a class="button push" href="{back}">Close</a>
        <button type="button" class="button-primary">Copy link</button>
      </div>
    </dialog>
'''

DIALOG = re.compile(r"\n\n    <!-- [^\n]*-->\n    <div class=\"scrim\" aria-hidden=\"true\"></div>\n    <dialog class=\"modal\" open.*?</dialog>\n", re.S)


def sub(t, a, b, n=1):
    assert t.count(a) == n, (a, t.count(a))
    return t.replace(a, b)


def main():
    if (PAGES / "project-link.html").exists():
        sys.exit("project-link.html exists — Q43 was applied already")
    changed = 0
    for p in sorted(PAGES.glob("*.html")):
        if p.stem == "wireframes":
            continue
        t = p.read_text(encoding="utf-8")
        t2 = t.replace('<a class="button" href="library-my-revoke.html">Stop sharing…</a>',
                       '<a class="button" href="library-my-link.html">Share…</a>')
        t2 = t2.replace('<button type="button">Stop sharing…</button>', '<button type="button">Share…</button>')
        t2 = t2.replace("and Share… or Stop sharing… is not known", "and whether it is shared is not known")
        if p.stem in ("project-revoke", "library-my-revoke"):
            back = "project-link.html" if p.stem == "project-revoke" else "library-my-link.html"
            t2 = re.sub(r'<a class="button push" href="[^"]*">Cancel</a>', f'<a class="button push" href="{back}">Cancel</a>', t2)
        if p.stem == "project-share":
            t2 = sub(t2, '<a class="button button-primary" href="project-default.html">Create link</a>',
                     '<a class="button button-primary" href="project-link.html">Create link</a>')
        if t2 != t:
            p.write_text(t2, encoding="utf-8")
            changed += 1

    for stem, base, name, what, ref, back in (
            ("project-link", "project-revoke", "acme-billing-api", "project", "k7Qm2xVb9RtL", "project-default.html"),
            ("library-my-link", "library-my-revoke", "github-mcp", "item", "Fh3wN8pZc2Ys", "library-my-default.html")):
        page = (PAGES / f"{base}.html").read_text(encoding="utf-8")
        page = sub(page, f"<title>", f"<title>", 1)
        page = re.sub(r"<title>([^·<]*)· revoke — wireframe</title>", r"<title>\1· link — wireframe</title>", page, count=1)
        assert "· link — wireframe" in page, stem
        dialog = LINK.format(name=name, what=what, ref=ref, revoke=f"{base}.html", back=back)
        page, n = DIALOG.subn("\n\n" + dialog, page, count=1)
        assert n == 1, stem
        (PAGES / f"{stem}.html").write_text(page, encoding="utf-8")

    v = PAGES / "wireframes.html"
    vt = v.read_text(encoding="utf-8")
    for stem in ("library-my", "project"):
        anchor = f'<li><a href="#{stem}-revoke"><svg class="wf-ico" aria-hidden="true"><use href="#i-file"/></svg><span class="wf-name">revoke</span></a></li>'
        vt = sub(vt, anchor, f'<li><a href="#{stem}-link"><svg class="wf-ico" aria-hidden="true"><use href="#i-file"/></svg><span class="wf-name">link</span></a></li>\n                  ' + anchor)
    v.write_text(vt, encoding="utf-8")
    print(f"Q43: Share… again on {changed} pages; project-link.html and library-my-link.html written; viewer lists them")


if __name__ == "__main__":
    main()
