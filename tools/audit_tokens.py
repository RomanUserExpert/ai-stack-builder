"""Phase 08, step 1: where every variable of the kit is read, and on which dressed pages.

    python -X utf8 tools/audit_tokens.py            # prints the uses as JSON (for the audit's author)
    python -X utf8 tools/audit_tokens.py --md       # prints the generated tables of tokens-audit.md

Reads 07-ui-assembly/ui/kit.css and every dressed page (04-wireframes/mockups/*.html, mockups/flows/**).
A rule counts as standing on a page when the page carries every class of the selector's last compound
(or, for a bare element selector, the element). That is an approximation and the audit says so.
Nothing is changed: this only reads.
"""
import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / "07-ui-assembly" / "ui" / "kit.css"
MOCK = ROOT / "04-wireframes" / "mockups"


def strip_comments(css):
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


def root_vars(css):
    block = re.search(r":root\{(.*?)\n\}", css, re.S).group(1)
    out = {}
    for m in re.finditer(r"--([\w-]+):\s*(.*?);[ \t]*(?:/\*\s*(.*?)\s*\*/)?[ \t]*$", block, re.M):
        out["--" + m.group(1)] = {"value": m.group(2).strip(), "note": (m.group(3) or "").strip()}
    return out


def rules(css):
    """Flat (selector, body) pairs, @media/@supports unwrapped, keyframes skipped."""
    css = strip_comments(css)
    css = css[css.index("}", css.index(":root")) + 1:]
    out, i, stack = [], 0, []
    sel_start = 0
    while i < len(css):
        c = css[i]
        if c == "{":
            head = css[sel_start:i].strip()
            if head.startswith("@keyframes"):
                depth, j = 1, i + 1
                while depth:
                    depth += {"{": 1, "}": -1}.get(css[j], 0)
                    j += 1
                i, sel_start = j, j
                continue
            if head.startswith("@"):
                stack.append(head)
                i += 1
                sel_start = i
                continue
            j = css.index("}", i)
            out.append((" ".join(head.split()), css[i + 1:j].strip()))
            i = j + 1
            sel_start = i
            continue
        if c == "}":
            stack and stack.pop()
            sel_start = i + 1
        i += 1
    return out


def declarations(body):
    for d in re.split(r";(?![^(]*\))", body):
        if ":" in d:
            p, v = d.split(":", 1)
            yield p.strip(), v.strip()


def last_compound(sel):
    """Every class anywhere in the selector (an ancestor's class must be on the page too), and the last tag."""
    sel = re.sub(r":(not|has|is)\((?:[^()]|\([^()]*\))*\)", "", sel)   # :not(), :has(), :is() say nothing of presence
    sel = re.sub(r"::?[\w-]+(\([^)]*\))?", "", sel)          # pseudo-classes and elements
    sel = re.sub(r"\[[^\]]*\]", "", sel)                     # attributes
    classes = re.findall(r"\.([\w-]+)", sel)
    part = re.split(r"[\s>+~]+", sel.strip())[-1]
    tag = re.match(r"[a-z][\w-]*", part)
    return classes, (tag.group(0) if tag else None)


def pages():
    out = {}
    for p in sorted(MOCK.glob("*.html")):
        out[p.stem] = p.read_text(encoding="utf-8")
    for p in sorted((MOCK / "flows").rglob("*.html")):
        out["flows/" + p.relative_to(MOCK / "flows").as_posix()[:-5]] = p.read_text(encoding="utf-8")
    return out


def page_index(texts):
    idx = {}
    for name, t in texts.items():
        cls = set()
        for m in re.finditer(r'class="([^"]*)"', t):
            cls.update(m.group(1).split())
        tags = set(re.findall(r"<([a-z][\w-]*)", t))
        idx[name] = (cls, tags)
    return idx


def standing(sel, idx):
    hit = set()
    for s in sel.split(","):
        classes, tag = last_compound(s)
        for name, (cls, tags) in idx.items():
            if classes and all(c in cls for c in classes) and (not tag or tag in tags):
                hit.add(name)
            elif not classes and tag and tag in tags:
                hit.add(name)
            elif not classes and not tag:                     # *, :root-like, html
                hit.add(name)
    return hit


def collect():
    import subprocess  # the kit as step 1 read it: kit.css left the tree in step 4, and git keeps it
    css = subprocess.run(["git", "show", "d6d419a:07-ui-assembly/ui/kit.css"], cwd=ROOT, capture_output=True,
                         check=True).stdout.decode("utf-8")
    rv = root_vars(css)
    idx = page_index(pages())
    uses = collections.defaultdict(list)
    for sel, body in rules(css):
        for prop, val in declarations(body):
            for v in set(re.findall(r"var\((--[\w-]+)", val)):
                uses[v].append({"sel": sel, "prop": prop, "val": val})
    # composite tokens read other tokens
    for name, d in rv.items():
        for v in set(re.findall(r"var\((--[\w-]+)", d["value"])):
            uses[v].append({"sel": ":root " + name, "prop": name, "val": d["value"]})
    page_hits = {}
    for v, us in uses.items():
        hit = set()
        for u in us:
            if not u["sel"].startswith(":root"):
                hit |= standing(u["sel"], idx)
        page_hits[v] = hit
    # a variable read only through a composite stands wherever the composite does
    for _ in range(3):
        for v, us in uses.items():
            for u in us:
                if u["sel"].startswith(":root"):
                    page_hits[v] |= page_hits.get(u["prop"], set())
    # values written in a class rather than through a variable
    literal = []
    for sel, body in rules(css):
        for prop, val in declarations(body):
            bare = re.sub(r"var\([^)]*\)", "", val)
            for m in re.finditer(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|-?\d*\.?\d+(px|ms|s|deg|em|%|vh)\b|\b\d+\b", bare):
                literal.append({"sel": sel, "prop": prop, "lit": m.group(0)})
    return rv, uses, page_hits, literal, idx


def main():
    rv, uses, hits, literal, idx = collect()
    n_pages = sum(1 for k in idx if not k.startswith("flows/"))
    n_steps = len(idx) - n_pages
    if "--md" not in sys.argv:
        json.dump({"vars": rv, "uses": uses, "pages": {k: sorted(v) for k, v in hits.items()},
                   "literal": literal, "n_pages": n_pages, "n_steps": n_steps}, sys.stdout, ensure_ascii=False, indent=1)
        return
    print(f"<!-- generated by tools/audit_tokens.py --md: {n_pages} pages, {n_steps} flow steps -->")
    print("| Variable | Value | Rules | Pages | Steps | Read by (property → selectors) |")
    print("|---|---|---|---|---|---|")
    for name, d in rv.items():
        us = uses.get(name, [])
        by = collections.defaultdict(list)
        for u in us:
            by[u["prop"]].append(u["sel"])
        where = "<br>".join(f"`{p}` → " + ", ".join(f"`{s}`" for s in sorted(set(ss))) for p, ss in sorted(by.items()))
        hp = hits.get(name, set())
        pg = sum(1 for h in hp if not h.startswith("flows/"))
        val = d["value"] if len(d["value"]) < 60 else d["value"][:57] + "…"
        print(f"| `{name}` | `{val}` | {len(us)} | {pg} | {len(hp) - pg} | {where or '—'} |")


if __name__ == "__main__":
    main()
