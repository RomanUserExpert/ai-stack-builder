"""Phase 07, step 9: the audit of every dressed screen against the kit, DESIGN.md and microcopy.md.

    python tools/audit07.py [--json OUT]

Six checks, each re-runnable; the table they feed is 07-ui-assembly/ui/audit.md.
  A  own styles / no kit.css / a style outside the kit's classes     (tools/kit_check.py, guards 1–7)
  B  one component, several markups — the structure of each kit component compared across all pages and flow steps
  C  contrast below WCAG AA — measured in the browser on every page: each text run's colour against the opaque
     background it actually sits on (ancestors composited), 4.5:1, or 3:1 for large text
  D  images not from the product's visuals, icons not from the Lucide set in 06-concept/icons/lucide
  E  text that differs from microcopy.md — every line of every wireframe page against the table; every dressed page's
     words against its wireframe's
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
WF = ROOT / "04-wireframes"
MOCK = WF / "mockups"
LUCIDE = ROOT / "06-concept" / "icons" / "lucide"

# the kit's components, by the class on their root element
COMPONENTS = ["app-header", "shared-header", "run-bar", "page-head", "tabs", "scope", "row", "callout", "state-block",
              "export-stage", "summary", "stage-group", "drawer", "aside-box", "card", "door", "field", "check", "search",
              "popover", "modal", "sheet", "dropzone", "file-list", "marks", "form-actions", "filters-button", "remove", "close"]


def pages(flows=True):
    out = sorted(MOCK.glob("*.html"))
    return out + (sorted((MOCK / "flows").glob("*/*.html")) if flows else [])


def check_a():
    import io
    import contextlib
    import kit_check
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = kit_check.main()
    return code, buf.getvalue().strip()


def signature(frag):
    """A component's markup shape: its root tag, then the tags and classes of its direct children, in order —
    words, ids, hrefs and states (aria-*, open, checked) left out."""
    tag = re.match(r"<(\w+)", frag).group(1)
    inner = frag[frag.index(">") + 1:frag.rindex("<")]
    kids, depth = [], 0
    for m in re.finditer(r"<(/?)(\w+)([^>]*?)(/?)>", inner):
        close, t, attrs, selfclose = m.groups()
        void = t in ("input", "img", "br", "use", "meta", "link") or selfclose
        if close:
            depth -= 1
            continue
        if depth == 0:
            cls = re.search(r'class="([^"]*)"', attrs)
            kids.append(t + ("." + ".".join(c for c in cls.group(1).split()
                                             if not c.startswith(("is-", "button-primary", "button-warning", "button-danger"))) if cls else ""))
        if not void:
            depth += 1
    return tag + " > " + " ".join(kids)


def check_b():
    import build_kit
    seen = defaultdict(Counter)
    where = defaultdict(lambda: defaultdict(list))
    for p in pages():
        h = p.read_text(encoding="utf-8")
        name = p.relative_to(MOCK).as_posix()
        for comp in COMPONENTS:
            for m in re.finditer(rf'<(\w+)\b[^>]*class="(?:[\w-]+ )*{comp}(?: [\w-]+)*"[^>]*>', h):
                frag = build_kit.outer(h[m.start():], m.group(1), "", None, 0, name) if m.group(1) not in ("input",) else m.group(0)
                sig = signature(frag)
                seen[comp][sig] += 1
                if len(where[comp][sig]) < 3:
                    where[comp][sig].append(name)
    return {c: [(s, n, where[c][s]) for s, n in v.most_common()] for c, v in seen.items() if len(v) > 1}


CONTRAST_JS = r"""
() => {
  const parse = s => { const m = s.match(/rgba?\(([^)]+)\)/); if (!m) return null;
    const p = m[1].split(/[ ,\/]+/).filter(Boolean).map(Number); return [p[0], p[1], p[2], p.length > 3 ? p[3] : 1]; };
  const lum = c => { const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2]); };
  const over = (top, under) => { const a = top[3]; return [0,1,2].map(i => top[i] * a + under[i] * (1 - a)).concat(1); };
  const bgOf = el => { const stack = []; let e = el;
    while (e) { const cs = getComputedStyle(e); const c = parse(cs.backgroundColor);
      if (cs.backgroundImage && cs.backgroundImage !== 'none' && !cs.backgroundImage.startsWith('url')) return null;
      if (c && c[3] > 0) { stack.push(c); if (c[3] >= 1) break; }
      e = e.parentElement; }
    let base = [255, 255, 255, 1]; for (let i = stack.length - 1; i >= 0; i--) base = over(stack[i], base); return base; };
  const out = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const done = new Set();
  while (walker.nextNode()) {
    const t = walker.currentNode; const el = t.parentElement;
    if (!t.textContent.trim() || done.has(el)) continue; done.add(el);
    if (el.closest('svg, .visually-hidden, [aria-hidden="true"], .skeleton, option, title')) continue;
    const r = el.getBoundingClientRect(); if (r.width === 0 || r.height === 0) continue;
    const cs = getComputedStyle(el); if (cs.visibility === 'hidden' || +cs.opacity === 0) continue;
    const fg = parse(cs.color); const bg = bgOf(el); if (!fg || !bg) continue;
    const c = over(fg, bg); const L1 = lum(c), L2 = lum(bg);
    const ratio = (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
    const size = parseFloat(cs.fontSize), weight = +cs.fontWeight;
    const large = size >= 24 || (size >= 18.66 && weight >= 700);
    const need = large ? 3 : 4.5;
    // a control that cannot act (WCAG 1.4.3 exempts inactive components)
    const inactive = !!el.closest('[disabled], [aria-disabled="true"], [inert]');
    if (ratio < need) out.push({text: t.textContent.trim().slice(0, 50), cls: el.className || el.tagName.toLowerCase(),
      ratio: Math.round(ratio * 100) / 100, need, inactive, fg: cs.color, bg: 'rgb(' + bg.slice(0,3).map(Math.round).join(',') + ')'});
  }
  return out;
}
"""


def check_c():
    from playwright.sync_api import sync_playwright
    found = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1440, "height": 900})
        for f in pages(flows=False):
            pg.goto(f.as_uri())
            pg.add_style_tag(content="*{transition:none!important;animation:none!important}")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150)
            for r in pg.evaluate(CONTRAST_JS):
                r["page"] = f.stem
                found.append(r)
        b.close()
    return found


def check_d():
    lucide = {p.stem for p in LUCIDE.glob("*.svg")}
    imgs, icons, guessed = Counter(), Counter(), []
    for p in pages():
        h = p.read_text(encoding="utf-8")
        for src in re.findall(r'<img[^>]*src="([^"]+)"', h):
            imgs[re.sub(r"^(\.\./)+", "", src)] += 1
        for sym in re.findall(r'<symbol id="l-([\w-]+)"', h):
            icons[sym] += 1
        if "#l-circle-dashed" in h:
            guessed.append(p.relative_to(MOCK).as_posix())
    import subprocess  # phase 07's kit, from git: it left the tree in phase 08, step 4
    css = subprocess.run(["git", "show", "d6d419a:07-ui-assembly/ui/kit.css"], cwd=ROOT, capture_output=True,
                         check=True).stdout.decode("utf-8")
    masks = re.findall(r"--(icon-[\w-]+|glyph-[\w-]+):", css)
    return {"images": dict(imgs), "icons_outside": sorted(set(icons) - lucide), "icons": len(icons),
            "guessed": guessed, "masks": masks}


def norm(s):
    s = s.replace("`", "").replace("<br>", "\n").replace("**", "").replace("\\|", "|")  # the table escapes a pipe
    return re.sub(r"[ \t]+", " ", s).strip()


def check_e():
    import extract_copy as ec
    mc = (ROOT / "05-tone-of-voice" / "microcopy.md").read_text(encoding="utf-8")
    known = set()
    for line in mc.split("\n"):
        if not line.startswith("| ") or line.startswith("| ---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        if len(cells) < 4:
            continue
        now = cells[3]
        known.add(norm(cells[2] if now == "=" else now))
    wf_rows = ec.rows()
    missing = sorted({(r[0], r[2]) for r in wf_rows if norm(r[2]) not in known and r[3] not in ("value",) and r[4] != "user"
                      and not re.fullmatch(r"[\d.]+ s|—|\d\d", r[2])})
    # dressed vs wireframe: the same words, page by page
    ec_pages = ec.PAGES
    ec.PAGES = MOCK
    try:
        mock_rows = ec.rows()
    finally:
        ec.PAGES = ec_pages
    by = lambda rows: {(r[0]): Counter(norm(r[2]) for r in rows if r[3] not in ("a11y label", "tooltip")) for r in rows}
    w, m = defaultdict(Counter), defaultdict(Counter)
    for r in wf_rows:
        if r[3] not in ("a11y label", "tooltip"):
            w[r[0]][norm(r[2])] += 1
    for r in mock_rows:
        if r[3] not in ("a11y label", "tooltip"):
            m[r[0]][norm(r[2])] += 1
    # the build names a section with a visually hidden h2 taken from its own aria-label: same words, now a heading
    labels = defaultdict(set)
    for r in wf_rows:
        if r[3] == "a11y label":
            labels[r[0]].add(norm(r[2]))
    drift = []
    for page in sorted(w):
        a, b = w[page], m.get(page, Counter())
        lost = a - b
        added = Counter({k: v for k, v in (b - a).items() if k not in labels[page]})
        if lost or added:
            drift.append((page, sorted(lost)[:4], sorted(added)[:4]))
    return missing, drift


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    res = {}
    code, out = check_a()
    res["A"] = {"exit": code, "out": out}
    print("A", out)
    res["B"] = check_b()
    print("B components with more than one markup:", {k: len(v) for k, v in res["B"].items()})
    res["C"] = check_c()
    active = [r for r in res["C"] if not r["inactive"]]
    print("C contrast below AA:", len(res["C"]), "runs,", len(active), "on active elements")
    res["D"] = check_d()
    print("D images:", res["D"]["images"], "· icons outside Lucide:", res["D"]["icons_outside"], "· guessed:", len(res["D"]["guessed"]))
    missing, drift = check_e()
    res["E"] = {"missing": missing, "drift": drift}
    print("E wireframe lines not in microcopy.md:", len(missing), "· pages whose words differ from their wireframe:", len(drift))
    if "--json" in sys.argv:
        Path(sys.argv[sys.argv.index("--json") + 1]).write_text(json.dumps(res, indent=1, ensure_ascii=False, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
