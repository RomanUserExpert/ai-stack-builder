"""Phase 06, stage 1 — the idea base: screenshots of public product UI, dark scheme.

Two modes, both read a plan from the lists below and write into 06-concept/refs/web/:

  python tools/capture_refs.py shots     # screenshot each page, 1440x900 viewport, prefers-color-scheme: dark
  python tools/capture_refs.py more      # the second pass, SHOTS_MORE
  python tools/capture_refs.py deep      # open the latest entries of each changelog, take their screens
  python tools/capture_refs.py harvest   # open each changelog/docs page, download its large images (product UI)

Nothing here logs in. Every page is public. Files are references, never assets (see references.md).
A manifest, refs/web/manifest.json, records each file's source URL and the capture date.
"""
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "06-concept" / "refs" / "web"
MANIFEST = OUT / "manifest.json"

# name -> url. Whole-viewport screenshots; "+full" in the name means full page.
SHOTS = {
    # Vercel's design system, Geist
    "geist-colors": "https://vercel.com/geist/colors",
    "geist-typography": "https://vercel.com/geist/typography",
    "geist-materials+full": "https://vercel.com/geist/materials",
    "geist-badge+full": "https://vercel.com/geist/badge",
    "geist-status-dot+full": "https://vercel.com/geist/status-dot",
    "geist-table+full": "https://vercel.com/geist/table",
    "geist-button+full": "https://vercel.com/geist/button",
    "geist-entity+full": "https://vercel.com/geist/entity",
    "geist-empty-state+full": "https://vercel.com/geist/empty-state",
    "geist-note+full": "https://vercel.com/geist/note",
    "geist-keyboard-input+full": "https://vercel.com/geist/keyboard-input",
    "geist-icons": "https://vercel.com/geist/icons",
    # GitHub, logged out, product UI that is public
    "github-actions-runs": "https://github.com/vercel/next.js/actions",
    "github-pulls": "https://github.com/vercel/next.js/pulls",
    "github-repo-code": "https://github.com/modelcontextprotocol/servers",
    "github-releases": "https://github.com/github/github-mcp-server/releases",
    # GitHub's design system, Primer
    "primer-label+full": "https://primer.style/product/components/label/",
    "primer-state-label+full": "https://primer.style/product/components/state-label/",
    "primer-counter-label+full": "https://primer.style/product/components/counter-label/",
    "primer-timeline+full": "https://primer.style/product/components/timeline/",
    "primer-color": "https://primer.style/product/primitives/color/",
    # Raycast
    "raycast-store": "https://www.raycast.com/store",
    "raycast-home": "https://www.raycast.com/",
    # Linear, public pages that render product UI
    "linear-home+full": "https://linear.app/",
    "linear-method": "https://linear.app/method",
    # Open product sandboxes: real rows, real states (README of 2-flows named both)
    "sentry-sandbox-issues": "https://sandbox.sentry.io/issues/",
    "grafana-play": "https://play.grafana.org/",
}

# Second pass, 2026-10-08: GitHub's product UI in depth, catalog pages, and the two registries the
# research named (Smithery, Tessl, CLAUDE.md §5) — the nearest public analogues of an item card.
SHOTS_MORE = {
    "github-run-summary+full": "https://github.com/vercel/next.js/actions/runs/37774917696",
    "github-job-failed": "https://github.com/vercel/next.js/actions/runs/37774917696/job/113303739131",
    "github-pr-checks": "https://github.com/vercel/next.js/pull/99860/checks",
    "github-pr-conversation+full": "https://github.com/vercel/next.js/pull/99860",
    "github-issues-labels": "https://github.com/vercel/next.js/issues",
    "vercel-templates": "https://vercel.com/templates",
    "vercel-marketplace": "https://vercel.com/marketplace",
    "raycast-extension-linear+full": "https://www.raycast.com/linear/linear",
    "smithery-home": "https://smithery.ai/",
    "tessl-registry": "https://tessl.io/registry",
}

# name -> page whose large <img> are product screenshots.
HARVEST = {
    "linear-changelog": "https://linear.app/changelog",
    "vercel-changelog": "https://vercel.com/changelog",
    "raycast-changelog": "https://www.raycast.com/changelog",
    "stripe-dashboard-docs": "https://docs.stripe.com/dashboard/basics",
    "github-changelog": "https://github.blog/changelog/",
    "railway-changelog": "https://railway.com/changelog",
    "resend-changelog": "https://resend.com/changelog",
    "supabase-changelog": "https://supabase.com/changelog",
    "cursor-changelog": "https://cursor.com/changelog",
}
# name -> (list page, regex an entry link must match). The list shows thumbnails; entries carry the screens.
HARVEST_DEEP = {
    "vercel-changelog": ("https://vercel.com/changelog", r"^https://vercel\.com/changelog/[a-z0-9-]+$"),
    "github-changelog": ("https://github.blog/changelog/", r"^https://github\.blog/changelog/\d{4}-\d{2}-\d{2}-[a-z0-9-]+/?$"),
    "railway-changelog": ("https://railway.com/changelog", r"^https://railway\.com/changelog/[a-z0-9-]+$"),
    "linear-changelog": ("https://linear.app/changelog", r"^https://linear\.app/changelog/\d{4}-\d{2}-\d{2}-[a-z0-9-]+$"),
}
DEEP_ENTRIES = 6

PER_PAGE = 8          # images kept per harvested page
MIN_WIDTH = 600       # natural width below this is an icon or an avatar, not a screen
MAX_RATIO = 3.2       # wider than this is a banner or a logo strip


def normalise(path):
    """A CDN may serve AVIF or WebP under any extension. Re-save anything that is not PNG/JPEG as PNG."""
    head = path.read_bytes()[:12]
    is_jpeg = head[:3] == bytes([0xFF, 0xD8, 0xFF])
    is_png = head[:8] == bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
    if (is_jpeg and path.suffix == ".jpg") or (is_png and path.suffix == ".png"):
        return path.name
    from PIL import Image
    new = path.with_suffix(".png")
    Image.open(path).save(new)
    if new != path:
        path.unlink()
    return new.name


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}


def save_manifest(m):
    m = {**load_manifest(), **m}            # merge: two modes may run at once
    MANIFEST.write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8")


def new_page(browser):
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, color_scheme="dark",
                              device_scale_factor=1, locale="en-US")
    return ctx.new_page()


def dismiss(page):
    """Close a cookie banner if one covers the page. Declines rather than accepts."""
    for label in ("Decline all", "Reject all", "Decline", "Reject", "Only necessary", "Accept all"):
        try:
            btn = page.get_by_role("button", name=label, exact=True)
            if btn.count():
                btn.first.click(timeout=2000)
                page.wait_for_timeout(500)
                return
        except Exception:
            pass


def shots(browser, m, plan=None, only=()):
    for name, url in (plan or SHOTS).items():
        if only and name.replace("+full", "") not in only:
            continue
        full = name.endswith("+full")
        fname = name.replace("+full", "") + ".jpg"
        page = new_page(browser)
        try:
            page.goto(url, wait_until="networkidle", timeout=45000)
        except Exception:
            try:
                page.wait_for_timeout(3000)
            except Exception:
                pass
        dismiss(page)
        try:
            page.wait_for_timeout(1500)
            page.screenshot(path=str(OUT / fname), full_page=full, type="jpeg", quality=80)
            m[fname] = {"source": url, "kind": "screenshot", "full_page": full, "date": str(date.today())}
            print("ok  ", fname)
        except Exception as e:
            print("FAIL", fname, str(e)[:120])
        page.context.close()


def harvest(browser, m, only=()):
    for name, url in HARVEST.items():
        if only and name not in only:
            continue
        page = new_page(browser)
        try:
            page.goto(url, wait_until="networkidle", timeout=45000)
        except Exception:
            pass
        try:
            for _ in range(6):                      # lazy images load on scroll
                page.mouse.wheel(0, 2500)
                page.wait_for_timeout(600)
            imgs = page.eval_on_selector_all(
                "img", "els => els.map(e => ({src: e.currentSrc || e.src, w: e.naturalWidth, h: e.naturalHeight, alt: e.alt || ''}))")
        except Exception as e:
            print("FAIL", name, str(e)[:120]); page.context.close(); continue
        seen, kept = set(), 0
        for im in imgs:
            src = im["src"]
            if not src or src.startswith("data:") or src in seen or im["w"] < MIN_WIDTH                     or not im["h"] or im["w"] / im["h"] > MAX_RATIO or src.lower().split("?")[0].endswith(".svg"):
                continue
            seen.add(src)
            ext = ".png" if ".png" in src.lower() and "fm=jpg" not in src else ".jpg"
            if re.search(r"\.(webp|avif)(\?|$)", src.lower()) or "format=webp" in src or "fm=webp" in src:
                ext = ".webp"
            fname = f"{name}-{kept + 1:02d}{ext}"
            try:
                req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
                (OUT / fname).write_bytes(urllib.request.urlopen(req, timeout=30).read())
                fname = normalise(OUT / fname)
            except Exception as e:
                print("skip", src[:80], str(e)[:60]); continue
            m[fname] = {"source": url, "image": src, "alt": im["alt"][:200], "kind": "harvested",
                        "date": str(date.today())}
            kept += 1
            if kept >= PER_PAGE:
                break
        print(f"ok   {name}: {kept} of {len(imgs)} images")
        page.context.close()


def collect(page, name, source, m, start, limit):
    """Download up to `limit` large images from the open page, numbering from `start`."""
    for _ in range(6):
        page.mouse.wheel(0, 2500)
        page.wait_for_timeout(500)
    imgs = page.eval_on_selector_all(
        "img", "els => els.map(e => ({src: e.currentSrc || e.src, w: e.naturalWidth, h: e.naturalHeight, alt: e.alt || ''}))")
    kept = 0
    for im in imgs:
        src = im["src"]
        if not src or src.startswith("data:") or im["w"] < MIN_WIDTH or not im["h"]                 or im["w"] / im["h"] > MAX_RATIO or src.lower().split("?")[0].endswith(".svg")                 or any(v.get("image") == src for v in m.values()):
            continue
        ext = ".webp" if ("webp" in src.lower()) else ".png" if ".png" in src.lower() else ".jpg"
        fname = f"{name}-{start + kept:02d}{ext}"
        try:
            req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
            (OUT / fname).write_bytes(urllib.request.urlopen(req, timeout=30).read())
            fname = normalise(OUT / fname)
        except Exception:
            continue
        m[fname] = {"source": source, "image": src, "alt": im["alt"][:200], "kind": "harvested",
                    "date": str(date.today())}
        kept += 1
        if kept >= limit:
            break
    return kept


def harvest_deep(browser, m, only=()):
    for name, (url, pattern) in HARVEST_DEEP.items():
        if only and name not in only:
            continue
        page = new_page(browser)
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(2500)
            links = page.eval_on_selector_all("a[href]", "els => els.map(e => e.href)")
        except Exception as e:
            print("FAIL", name, str(e)[:100]); page.context.close(); continue
        entries = list(dict.fromkeys(l.split("#")[0] for l in links if re.match(pattern, l.split("#")[0])))[:DEEP_ENTRIES]
        n = 1 + sum(1 for k in m if k.startswith(name + "-"))
        total = 0
        for e in entries:
            try:
                page.goto(e, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(2000)
                k = collect(page, name, e, m, n, 3)
                n += k; total += k
            except Exception:
                pass
        print(f"ok   {name}: {total} images from {len(entries)} entries")
        page.context.close()


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "shots"
    OUT.mkdir(parents=True, exist_ok=True)
    m = load_manifest()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        only = tuple(sys.argv[2:])
        {"shots": lambda b, mm: shots(b, mm, SHOTS, only),
         "more": lambda b, mm: shots(b, mm, SHOTS_MORE, only),
         "harvest": lambda b, mm: harvest(b, mm, only),
         "deep": lambda b, mm: harvest_deep(b, mm, only)}[mode](browser, m)
        browser.close()
    save_manifest(m)


if __name__ == "__main__":
    main()
