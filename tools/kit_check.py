"""Phase 07: the guards — nothing on a dressed screen drifts from the kit, and nothing in the kit from the tokens.

    python tools/kit_check.py

Run at the end of tools/build_mockups.py, and on its own. Exits non-zero on any failure. The rules are
07-ui-assembly/README.md §2:

1. kit.css's classes hold no value of their own (hex, rgb(), px, a font name)
2. no style= and no <style> on any mockup or flow step
3. every class on a dressed page is defined in kit.css (a short named list excepted)
4. every var(--x) in kit.css is declared in its :root
5. every :root value in kit.css equals tokens.css's, character for character
6. every mockup links Geist and kit.css, nothing else
7. no dressed page has more than one button-primary
8. kit.html's words are in microcopy.md (build_kit checks it; repeated here as a count)
9. coverage: wireframe pages and flow steps with a twin
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import concept_ui  # noqa: E402

KIT = ROOT / "07-ui-assembly" / "ui" / "kit.css"
TOKENS = ROOT / "06-concept" / "tokens.css"
WF = ROOT / "04-wireframes"
ALLOWED = {"visually-hidden", "product-page", "image"}  # utilities the markup carries for meaning


def root_and_body(css):
    m = re.search(r"^:root\{\n(.*?)\n\}\n", css, re.S | re.M)
    return m.group(1), css[m.end():]


def decls(block):
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^\s*--([\w-]+):\s*(.*?);(?:\s*/\*.*\*/)?\s*$", block, re.M)}


def main():
    fails = []
    css = KIT.read_text(encoding="utf-8")
    root, body = root_and_body(css)
    # 1 — values only in variables
    bad = concept_ui.literals(re.sub(r"/\*.*?\*/", "", body, flags=re.S))
    if bad:
        fails.append(f"1 kit.css classes hold literal values: {sorted(set(bad))[:10]}")
    # 4 — every var defined
    declared = decls(root)
    used = set(re.findall(r"var\(--([\w-]+)\)", css))
    undefined = sorted(used - set(declared))
    if undefined:
        fails.append(f"4 var() used but not declared in kit.css :root: {undefined}")
    # 5 — kit mirrors tokens
    tok = TOKENS.read_text(encoding="utf-8")
    tdecl = {}
    for blk in re.findall(r"^:root(?:, \.theme-light)? \{\n(.*?)\n\}", tok, re.S | re.M):
        tdecl.update(decls(blk))
    drift = sorted(n for n, v in declared.items() if tdecl.get(n) != v)
    if drift:
        fails.append(f"5 kit.css :root differs from tokens.css: {drift[:10]}")
    # 2, 3, 6, 7 — every dressed page
    classes = set(re.findall(r"\.([a-zA-Z][\w-]*)", re.sub(r"url\([^)]*\)", "", body)))
    pages = sorted((WF / "mockups").glob("*.html")) + sorted((WF / "mockups" / "flows").glob("*/*.html"))
    unknown, styled, sheets, primaries = {}, [], [], []
    for p in pages:
        h = p.read_text(encoding="utf-8")
        name = p.relative_to(WF / "mockups").as_posix()
        if re.search(r"\sstyle=\"", h) or "<style" in h:
            styled.append(name)
        links = re.findall(r'<link rel="stylesheet" href="([^"]+)"', h)
        if len(links) != 1 or not links[0].endswith("07-ui-assembly/ui/kit.css"):
            sheets.append(f"{name}: {links}")
        for c in set(c for m in re.findall(r'class="([^"]*)"', h) for c in m.split()):
            if c not in classes and c not in ALLOWED and not c.startswith("wf-") and c != "device":
                unknown.setdefault(c, []).append(name)
        n = len(re.findall(r'class="[^"]*\bbutton-primary\b', h))
        if n > 1:
            primaries.append(f"{name} ({n})")
    if styled:
        fails.append(f"2 style on a screen: {styled[:8]}")
    if unknown:
        fails.append("3 classes not in kit.css: " + "; ".join(f"{c} ({len(v)}: {v[0]})" for c, v in sorted(unknown.items())))
    if sheets:
        fails.append(f"6 a page links something other than kit.css: {sheets[:5]}")
    if primaries:
        fails.append(f"7 more than one primary: {primaries[:8]}")
    # 4b — the showcase links kit.css alone, so its own styles may only read variables kit.css declares (review B-1)
    for f in (KIT.parent / "kit.html", KIT.parent / "shell.html"):
        styles = "".join(re.findall(r"<style>(.*?)</style>", f.read_text(encoding="utf-8"), re.S))
        missing = sorted(set(re.findall(r"var\(--([\w-]+)\)", styles)) - set(declared))
        if missing:
            fails.append(f"4 {f.name} reads variables kit.css does not declare: {missing}")
    # 8 — the showcase's words are the product's (a stage's duration is a value, not a line: microcopy.md leaves it out)
    import build_kit
    words = [w for w in build_kit.words_check((KIT.parent / "kit.html").read_text(encoding="utf-8"))
             if not re.fullmatch(r"\d+(\.\d+)? s", w)]
    if words:
        fails.append(f"8 words on kit.html not in microcopy.md: {words[:6]}")
    # 9 — coverage
    wf = sorted(p.stem for p in (WF / "pages").glob("*.html") if p.stem != "wireframes")
    dressed = {p.stem for p in (WF / "mockups").glob("*.html")}
    steps = sum(1 for _ in (WF / "prototypes").glob("*/*.html"))
    dsteps = sum(1 for _ in (WF / "mockups" / "flows").glob("*/*.html"))
    print(f"kit check: {len(pages)} dressed pages · {len(declared)} variables · {len(classes)} classes · "
          f"coverage {len(dressed & set(wf))}/{len(wf)} pages, {dsteps}/{steps} flow steps")
    for f in fails:
        print("  FAIL", f)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
