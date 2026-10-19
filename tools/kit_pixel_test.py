"""Phase 07: the pixel test — screens drawn before a change and after it must be the same.

    python tools/kit_pixel_test.py save DIR [PAGE ...]    # the goldens: every mockup as it is now
    python tools/kit_pixel_test.py check DIR [PAGE ...]   # the same pages now, against those goldens

Each page is drawn at 1440 wide, full height. The look is compared, not the motion: shimmer, spinners,
transitions and the caret are stopped, and the page's sheets are reloaded once so every shot goes the
same render path. A difference of at most 1/255 is the rasteriser on a rounded corner — reported, not
failed. With no PAGE, every page in 04-wireframes/mockups/.
"""
import io
import sys
from pathlib import Path
from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
MOCKUPS = ROOT / "04-wireframes" / "mockups"
STILL = "*,*::before,*::after{animation:none!important;transition:none!important;caret-color:transparent!important}"
RELOAD = """() => Promise.all([...document.querySelectorAll('link[rel=stylesheet]')].filter(l => !l.href.includes('fonts.googleapis'))
  .map(l => new Promise(done => { l.onload = done; l.href = l.href.split('?')[0] + '?again'; })))"""


def shoot(pg, name):
    pg.goto((MOCKUPS / f"{name}.html").as_uri())
    pg.add_style_tag(content=STILL)
    pg.evaluate(RELOAD)
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(500)
    return Image.open(io.BytesIO(pg.screenshot(full_page=True, animations="disabled"))).convert("RGB")


def main(mode, out, pages):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    pages = pages or sorted(p.stem for p in MOCKUPS.glob("*.html"))
    bad = 0
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1440, "height": 900})
        for name in pages:
            img = shoot(pg, name)
            if mode == "save":
                img.save(out / f"{name}.png")
                continue
            gold = Image.open(out / f"{name}.png").convert("RGB")
            if gold.size != img.size:
                print(f"  DIFF  {name}  size {gold.size} -> {img.size}")
                bad += 1
                img.save(out / f"{name}-now.png")
                continue
            d = ImageChops.difference(gold, img)
            box, top = d.getbbox(), d.convert("L").getextrema()[1]
            if not box:
                print(f"  same  {name}")
            elif top <= 1:
                print(f"  same  {name}  (±1/255 antialiasing in {box})")
            else:
                print(f"  DIFF  {name}  {box} up to {top}/255")
                bad += 1
                img.save(out / f"{name}-now.png")
        b.close()
    if mode == "save":
        print(f"goldens: {len(pages)} pages saved to {out}")
    else:
        print(f"pixel test: {len(pages) - bad} of {len(pages)} identical")
    return bad


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("save", "check"):
        raise SystemExit(__doc__)
    sys.exit(1 if main(sys.argv[1], sys.argv[2], sys.argv[3:]) else 0)
