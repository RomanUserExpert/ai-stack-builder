"""Phase 07, step 3: screenshots of kit.html and shell.html, for review.  python tools/kit_shots.py OUTDIR"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parent.parent
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    for name in ("kit", "shell"):
        pg.goto((ROOT / "07-ui-assembly" / "ui" / f"{name}.html").as_uri()); pg.wait_for_timeout(800)
        pg.screenshot(path=str(out / f"{name}.png"), full_page=True)
        print(name, pg.evaluate("document.documentElement.scrollHeight"))
    b.close()
