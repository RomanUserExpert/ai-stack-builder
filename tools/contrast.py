"""Phase 06, stage 4: measure WCAG contrast on 06-concept/tokens.css, as written.

Reads the file — not the generator — resolves the hex colours and the three colour-mix boxes the
pages use, and checks every text-on-surface pair the stand and the screens actually draw.

    python tools/contrast.py   -> 06-concept/contrast.md, and prints the table

AA: 4.5:1 for text, 3:1 for large text (24 px, or 18.66 px bold) and for a control's edge or icon.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "06-concept" / "tokens.css"
OUT = ROOT / "06-concept" / "contrast.md"

# text token, surface token, what it is, the AA bar
PAIRS = [
    ("text", "tray", "a row’s name", 4.5), ("text", "cutout", "a row’s name in its cut-out", 4.5),
    ("text", "raised", "panel and dialog text", 4.5), ("text", "ground", "the project’s name", 4.5),
    ("text", "bar", "the current place", 4.5), ("text", "control", "a secondary button’s label", 4.5),
    ("text", "well-deep", "code", 4.5), ("text", "problem-box", "a Problem’s sentence", 4.5),
    ("text", "note-box", "a Note’s sentence", 4.5),
    ("text-2", "cutout", "a row’s description", 4.5), ("text-2", "raised", "panel description", 4.5),
    ("text-2", "bar", "a place, not current", 4.5), ("text-2", "ground", "the project description", 4.5),
    ("text-3", "cutout", "a row’s path, metadata", 4.5), ("text-3", "raised", "a section label in the panel", 4.5),
    ("text-3", "control", "a disabled button’s label", 4.5), ("text-3", "ground", "the breadcrumb", 4.5),
    ("on-lime", "lime", "the primary button", 4.5), ("on-lime", "lime-hover", "the primary button, hovered", 4.5),
    ("on-danger", "danger", "the remove in a dialog", 4.5), ("on-danger", "danger-hover", "the remove, hovered", 4.5),
    ("problem", "cutout", "a Problem tag on a row", 4.5), ("problem", "raised", "a Problem in the panel", 4.5),
    ("problem", "problem-box", "the muted remove, and a Problem’s head", 4.5),
    ("note", "cutout", "a Note tag on a row", 4.5), ("note", "note-box", "a Note’s head", 4.5),
    ("checked", "cutout", "Checked, a stage verdict", 4.5), ("skipped", "ground", "Skipped, a stage verdict", 4.5),
    ("lime-mark", "bar", "the current place’s icon (non-text, 3:1)", 3.0), ("lime-mark", "raised", "the active row’s pill (non-text, 3:1)", 3.0),
    ("line-strong", "raised", "a tag’s outline (non-text, 3:1)", 1.0),
    # added with the mockups (2026-10-11)
    ("text-3", "well-deep", "mockups: a search field’s placeholder", 4.5), ("text-2", "tray", "mockups: an empty or error state’s sentence", 4.5),
    ("text", "control", "mockups: inline code", 4.5), ("text-3", "tray", "mockups: an error code under a state", 4.5),
    ("problem", "problem-wash@cutout", "mockups: the Conflict tag and a Problem tag on a row", 4.5),
    ("note", "note-wash@cutout", "mockups: a Note tag on a row", 4.5),
    ("text-2", "control", "mockups: an empty or error state’s icon on its neutral tile (non-text, 3:1)", 3.0),
    ("on-warning", "warning", "Export with 1 problem — the warning button", 4.5),
    ("on-warning", "warning-hover", "the warning button, hovered", 4.5),
    ("lime-mark", "cutout", "mockups: the empty state’s illustration (non-text, 3:1)", 3.0),
    ("control-edge", "raised", "mockups: a checkbox or radio’s edge in a popover (non-text, 3:1)", 3.0),
    ("control-edge", "bar", "mockups: a checkbox or radio’s edge in the sidebar (non-text, 3:1)", 3.0),
    ("on-lime", "lime", "mockups: the tick in a checked checkbox", 4.5),
    # added by the phase 07 review (2026-10-19): pairs the kit draws that were never measured
    ("problem", "problem-wash@problem-box", "kit: the quiet remove inside a Problem, hovered", 4.5),
    ("problem", "problem-wash@raised", "kit: a Conflict tag or a Problem capsule on the active row", 4.5),
    ("note", "note-wash@raised", "kit: a Note capsule on the active row", 4.5),
    ("text-3", "row-hover", "kit: a row's facts, hovered", 4.5), ("text-2", "row-hover", "kit: a row's description, hovered", 4.5),
    ("text-3", "bar", "kit: a tab's count in the library sidebar", 4.5),
    ("text-2", "well-deep", "kit: a segment not current; the drop zone's sentence", 4.5),
    ("text-2", "hover-wash@cutout", "kit: In this project, hovered", 4.5),
    ("text", "control-hover", "kit: a secondary button, hovered", 4.5), ("text", "segment-hover", "kit: a segment, hovered", 4.5),
    ("text", "hover-wash@bar", "kit: a place in the top bar, hovered", 4.5),
    ("control-edge", "ground", "kit: a field's edge; the Skipped outline (non-text, 3:1)", 3.0),
    ("control-edge", "cutout", "kit: the waiting ring (non-text, 3:1)", 3.0),
    ("control-edge", "well-deep", "kit: a field's edge on its own well (non-text, 3:1)", 3.0),
    ("lime-mark", "control", "kit: the import progress bar (non-text, 3:1)", 3.0),
    ("lime-mark", "ground", "kit: the focus ring (non-text, 3:1)", 3.0),
]


def _hex(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _lum(rgb):
    c = [x / 255 for x in rgb]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = _lum(a), _lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def read(theme=":root"):
    css = TOKENS.read_text(encoding="utf-8")
    # the plain :root block and the shared ":root, .theme-light" block of derived tokens
    root = "".join(re.findall(r"\n:root(?:, \.theme-light)?\s*\{(.*?)\n\}", "\n" + css, re.S))
    vals = dict(re.findall(r"--([\w-]+):\s*(#[0-9A-Fa-f]{6})", root))
    mix_re = r"--([\w-]+):\s*color-mix\(in srgb,\s*var\(--([\w-]+)\)\s*(\d+)%,\s*var\(--([\w-]+)\)\)"
    mixes = {m[0]: m[1:] for m in re.findall(mix_re, root)}
    if theme != ":root":
        block = re.search(r"\n" + re.escape(theme) + r"\s*\{(.*?)\n\}", css, re.S).group(1)
        vals.update(dict(re.findall(r"--([\w-]+):\s*(#[0-9A-Fa-f]{6})", block)))
        mixes.update({m[0]: m[1:] for m in re.findall(mix_re, block)})
    rgb = {k: _hex(v) for k, v in vals.items()}
    washes = {m[0]: (m[1], int(m[2])) for m in re.findall(r"--([\w-]+):\s*color-mix\(in srgb,\s*var\(--([\w-]+)\)\s*(\d+)%,\s*transparent\)", root + (block if theme != ":root" else ""))}
    for name, (a, pct, b) in mixes.items():
        p = int(pct) / 100
        rgb[name] = tuple(round(rgb[a][i] * p + rgb[b][i] * (1 - p)) for i in range(3))
    for w, (col, pct) in washes.items():
        rgb[w + "@"] = (col, pct)
    return rgb


def _resolve(rgb, name):
    if "@" not in name:
        return rgb.get(name)
    wash, base = name.split("@")
    spec, b = rgb.get(wash + "@"), rgb.get(base)
    if not spec or not b:
        return None
    col, pct = spec
    p = pct / 100
    return tuple(round(rgb[col][i] * p + b[i] * (1 - p)) for i in range(3))


def rows(theme=":root"):
    rgb = read(theme)
    out = []
    for fg, bg, what, bar in PAIRS:
        f, b = _resolve(rgb, fg), _resolve(rgb, bg)
        if f is None or b is None:
            continue
        r = ratio(f, b)
        out.append({"fg": fg, "bg": bg, "fgv": "#%02X%02X%02X" % f, "bgv": "#%02X%02X%02X" % b,
                    "what": what, "ratio": r, "bar": bar, "pass": r >= bar})
    return out


def build():
    dark, light = rows(), rows(".theme-light")
    lines = ["# Contrast — Mica · Lime", "",
             "**Measured by `tools/contrast.py` on `tokens.css` as written** (phase 06, stage 4). AA is 4.5:1 for text,",
             "3:1 for a control's edge or an icon shown as a state. The outline of a tag is decorative support for its text",
             "(the text itself passes), so its row is informational.", ""]
    for title, rs in (("Dark — the product", dark), ("Light — the slice", light)):
        lines += [f"## {title}", "", "| Text | On | Ratio | AA | Where |", "|---|---|---:|:---:|---|"]
        for r in rs:
            mark = "—" if r["bar"] == 1.0 else ("pass" if r["pass"] else "**fail**")
            lines.append(f"| `--{r['fg']}` {r['fgv']} | `--{r['bg']}` {r['bgv']} | {r['ratio']:.2f} | {mark} | {r['what']} |")
        lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    bad = [r for r in dark + light if not r["pass"] and r["bar"] > 1]
    print(f"wrote {OUT.relative_to(ROOT)} · {len(dark)} dark + {len(light)} light pairs · failing: {len(bad)}")
    for r in bad:
        print("  FAIL", r["fg"], "on", r["bg"], round(r["ratio"], 2))
    return dark, light


if __name__ == "__main__":
    build()
