"""The guards — nothing on a dressed screen drifts from the components, and no component from the tokens.

    python tools/kit_check.py

Run at the end of tools/build_mockups.py, and on its own. Exits non-zero on any failure. Phase 07 wrote these
against one flat kit.css (07-ui-assembly/README.md §2); phase 08, step 4 moved them onto the two files that
replaced it, 08-design-tokens/tokens.css and components/. The numbers are kept:

1. no class in components/ holds a value of its own (hex, rgb(), px, a font name)
2. no style= and no <style> on any mockup or flow step
3. every class on a dressed page is defined in components/ (a short named list excepted)
4. every var(--x) in components/, and in the showcase's own styles, is declared in tokens.css
5. no component reads a colour primitive: colour only through a role (tokens.css, SEMANTIC)
6. every mockup links Geist, tokens.css and components/index.css, nothing else; index.css imports every file
7. no dressed page has more than one button-primary
8. kit.html's words are in microcopy.md (build_kit checks it; repeated here as a count)
9. coverage: wireframe pages and flow steps with a twin
10. no geometry written as a count of a primitive (calc(var(--s12) * 3)) outside the skeleton sizes (tokens-check.md, T5)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import concept_ui  # noqa: E402

TOKENS = ROOT / "08-design-tokens" / "tokens.css"
COMPONENTS = ROOT / "08-design-tokens" / "components"
UI = ROOT / "07-ui-assembly" / "ui"
WF = ROOT / "04-wireframes"
ALLOWED = {"visually-hidden", "product-page", "image"}  # utilities the markup carries for meaning
LINKS = ("08-design-tokens/tokens.css", "08-design-tokens/components/index.css")
COLOUR_PRIMITIVE = re.compile(r"var\(--((?:mica|lime|rose|amber|red)-(?:light-)?(?:\d+|a\d+)|white|(?:black|white)-a\d+)\)")


def main():
    fails = []
    tokens = TOKENS.read_text(encoding="utf-8")
    declared = set(re.findall(r"^\s*--([\w-]+):", tokens, re.M))
    files = sorted(p for p in COMPONENTS.glob("*.css") if p.name != "index.css")
    body = "\n".join(re.sub(r"/\*.*?\*/", "", p.read_text(encoding="utf-8"), flags=re.S) for p in files)
    # 1 — values only in variables
    bad = concept_ui.literals(body)
    if bad:
        fails.append(f"1 components/ hold literal values: {sorted(set(bad))[:10]}")
    # 4 — every var declared
    undefined = sorted(set(re.findall(r"var\(--([\w-]+)\)", body)) - declared)
    if undefined:
        fails.append(f"4 var() in components/ not declared in tokens.css: {undefined}")
    # 5 — colour through a role
    direct = sorted({f"{p.name}: --{m}" for p in files for m in COLOUR_PRIMITIVE.findall(p.read_text(encoding="utf-8"))})
    if direct:
        fails.append(f"5 a component reads a colour primitive: {direct[:8]}")
    # 10 — geometry by name: a count of a primitive is a number in disguise (the skeletons' sizes are kept, T5-4)
    counts = []
    for p in files:
        for sel, decl in re.findall(r"([^{}]+)\{([^{}]*)\}", re.sub(r"/\*.*?\*/", "", p.read_text(encoding="utf-8"), flags=re.S)):
            if sel.strip().startswith(".sk-"):
                continue
            for c in re.findall(r"calc\((?:[^()]|\([^()]*\))*\)", decl):
                if re.search(r"\*\s*(?!-1\b)-?\d|/\s*\d", c):
                    counts.append(f"{p.name}: {sel.strip()[:40]} {c}")
    if counts:
        fails.append(f"10 geometry written as a count: {counts[:6]}")
    # 6b — index.css imports every component file, once
    imports = re.findall(r'@import url\("([\w-]+\.css)"\)', (COMPONENTS / "index.css").read_text(encoding="utf-8"))
    if sorted(imports) != sorted(p.name for p in files):
        fails.append(f"6 index.css imports {len(imports)} files, components/ holds {len(files)}")
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
        if len(links) != 2 or not all(l.endswith(want) for l, want in zip(links, LINKS)):
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
        fails.append("3 classes not in components/: " + "; ".join(f"{c} ({len(v)}: {v[0]})" for c, v in sorted(unknown.items())))
    if sheets:
        fails.append(f"6 a page links something other than tokens.css + components/index.css: {sheets[:5]}")
    if primaries:
        fails.append(f"7 more than one primary: {primaries[:8]}")
    # 4b, 6c — the showcase and the shell: the same two files, and their own styles read only declared variables
    for f in (UI / "kit.html", UI / "shell.html"):
        h = f.read_text(encoding="utf-8")
        links = re.findall(r'<link rel="stylesheet" href="([^"]+)"', h)
        if len(links) != 2 or not all(l.endswith(want) for l, want in zip(links, LINKS)):
            fails.append(f"6 {f.name} links {links}")
        styles = "".join(re.findall(r"<style>(.*?)</style>", h, re.S))
        missing = sorted(set(re.findall(r"var\(--([\w-]+)\)", styles)) - declared)
        if missing:
            fails.append(f"4 {f.name} reads variables tokens.css does not declare: {missing}")
        direct = sorted(set(COLOUR_PRIMITIVE.findall(styles)))
        if direct:
            fails.append(f"5 {f.name}'s own styles read a colour primitive: {direct}")
    if (UI / "kit.css").exists():
        fails.append("6 07-ui-assembly/ui/kit.css is back: phase 08 retired it")
    # 8 — the showcase's words are the product's (a stage's duration is a value, not a line: microcopy.md leaves it out)
    import build_kit
    words = [w for w in build_kit.words_check((UI / "kit.html").read_text(encoding="utf-8"))
             if not re.fullmatch(r"\d+(\.\d+)? s", w)]
    if words:
        fails.append(f"8 words on kit.html not in microcopy.md: {words[:6]}")
    # 9 — coverage
    wf = sorted(p.stem for p in (WF / "pages").glob("*.html") if p.stem != "wireframes")
    dressed = {p.stem for p in (WF / "mockups").glob("*.html")}
    steps = sum(1 for _ in (WF / "prototypes").glob("*/*.html"))
    dsteps = sum(1 for _ in (WF / "mockups" / "flows").glob("*/*.html"))
    print(f"kit check: {len(pages)} dressed pages · {len(declared)} tokens · {len(files)} component files · "
          f"{len(classes)} classes · coverage {len(dressed & set(wf))}/{len(wf)} pages, {dsteps}/{steps} flow steps")
    for f in fails:
        print("  FAIL", f)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
