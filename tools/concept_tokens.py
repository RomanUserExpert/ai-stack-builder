"""Phase 06, stage 4: the one source of the working style's values -> 06-concept/tokens.css.

Every colour, type role, radius, spacing step, shadow and material of *Mica · Lime* is defined here
once, written to tokens.css, and nothing else holds a value: concept.html (the stand) and
mica-lime.html (the screens) link tokens.css and use var() only. tools/contrast.py reads the
written file back — not this module — so the contrast table is measured on what ships.

    python tools/concept_tokens.py   -> 06-concept/tokens.css

Each colour carries the attribute or decision it comes from (06-concept/concept.md).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "06-concept" / "tokens.css"

# name, value, group, role, why (the attribute / decision in concept.md)
COLORS = [
    ("ground", "#1B1C19", "neutral", "Mica ground, a faint lime tint", "Taste: Teams’ material, Mica; dark from day one (§3)"),
    ("bar", "#181916", "neutral", "the top bar", "Pair 2: hierarchy by layer, not by colour"),
    ("tray", "#232420", "neutral", "the tray under the rows", "Owner, round 4: Kit’s cut-out form"),
    ("cutout", "#1E1F1B", "neutral", "a row’s cut-out", "Owner, round 4: every item in its own cut-out"),
    ("well-deep", "#161714", "neutral", "a code block", "Polish: the darkest well, so its edge holds the column"),
    ("raised", "#2A2B27", "neutral", "item panel, the active row, a sheet", "Pair 2: one step up = one layer up"),
    ("control", "#2E302A", "neutral", "a secondary button", "Pair 5: controls stay grey; lime only where you act first"),
    ("control-hover", "#383A33", "neutral", "a secondary button, hovered", "States, drawn"),
    ("line", "#343630", "neutral", "hairline", "Linear base: hairlines instead of shadows"),
    ("line-strong", "#4A4C44", "neutral", "a control’s edge, a tag’s outline, a dashed rule", "Polish: every boxed object has a visible edge"),
    ("text", "#F3F4EF", "neutral", "text", "Three text tones (Linear base)"),
    ("text-2", "#C5C7BE", "neutral", "secondary text", "Three text tones"),
    ("text-3", "#A1A49A", "neutral", "metadata, Skipped", "Three text tones; raised for 5.3:1 on a button"),
    ("lime", "#C6EF5A", "primary", "the brand: what you can press, where you are", "Owner, round 4 (Lime); pair 5: colour is a claim, lime never a verdict"),
    ("lime-hover", "#D3F57A", "primary", "the primary button, hovered", "States"),
    ("on-lime", "#141A08", "primary", "text on lime", "Contrast"),
    ("lime-mark", "#C6EF5A", "primary", "lime as a mark: the current place’s icon, the active row’s pill", "Same as lime in the dark; its own value in light"),
    ("problem", "#FF8F98", "state", "Problem — the archive will be wrong", "§6: three severities; pair 1"),
    ("note", "#F2C661", "state", "Note — correct but incomplete", "§6: three severities"),
    ("checked", "#C5C7BE", "state", "Checked — a quiet dot, no colour: the product has no success", "D1-B: never a green tick that claims works"),
    ("skipped", "#A1A49A", "state", "Skipped — a slashed circle, neutral", "§6: not a green tick, not a red one"),
    ("danger", "#D4363F", "state", "a button that removes something", "Owner, 2026-10-11: a red remove"),
    ("danger-hover", "#BE2E37", "state", "the remove, hovered — darker, never lighter", "Contrast: white stays above 4.5:1"),
    ("on-danger", "#FFFFFF", "state", "text on danger", "Contrast"),
]
# light slice (README: one light slice of the chosen direction, in stage 4) — overrides only
LIGHT = {
    "ground": "#F4F5EF", "bar": "#ECEDE6", "tray": "#E9EAE2", "cutout": "#FBFBF8", "well-deep": "#F0F1EA",
    "raised": "#FFFFFF", "control": "#FFFFFF", "control-hover": "#F1F2EB", "line": "#DCDED4", "line-strong": "#C3C6BA",
    "text": "#181A14", "text-2": "#464A40", "text-3": "#5F6358", "lime": "#C6EF5A", "lime-hover": "#BCE84A",
    "on-lime": "#141A08", "lime-mark": "#55700F", "problem": "#B4232E", "note": "#7A5600", "checked": "#464A40", "skipped": "#5F6358",
}
SPACE = [("1", 4), ("2", 8), ("3", 12), ("4", 16), ("5", 20), ("6", 24), ("8", 32), ("10", 40), ("12", 48)]
TYPE = [  # name, weight, size, line-height, sample, use
    ("display", 600, 28, 34, "acme-billing-api", "a project’s name"),
    ("title", 600, 20, 26, "Checked just now", "the Export mode’s verdict"),
    ("heading", 600, 16, 22, "Remove eslint-autofix from acme-billing-api?", "the item panel, a dialog, a card"),
    ("body", 400, 14.5, 21, "Reads a migration before it runs and flags long locks.", "names, sentences"),
    ("button", 500, 13.5, 16, "Export…", "buttons and the places"),
    ("small", 400, 13, 19, "14 items · 3 auto-added · 1 detached", "descriptions, counts"),
    ("micro", 500, 12, 16, "Auto-added", "tags, findings"),
    ("label", 600, 11.5, 16, "IN THIS PROJECT", "section labels, uppercase"),
    ("code", 400, 12, 20, "scripts/eslint-autofix.sh", "paths, refs, file contents (mono)"),
]
RADIUS = [("xs", 4), ("sm", 6), ("md", 10), ("lg", 14), ("xl", 18), ("pill", 999)]
SHADOW = [
    ("tile", "0 1px 2px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.04)", "the current place in the top bar"),
    ("cutout", "inset 0 0 0 1px var(--line), inset 0 1px 2px rgba(0,0,0,.35)", "a row’s cut-out, pressed into the tray"),
    ("sheet", "0 18px 40px rgba(0,0,0,.35)", "a dialog over a mode"),
    ("focus", "0 0 0 2px var(--ground), 0 0 0 4px var(--lime)", "keyboard focus — 2 px lime with a gap"),
]
MATERIAL = [
    ("acrylic", "color-mix(in srgb, var(--lime) 7%, rgba(62,64,58,.42))", "acrylic: the frame of the Export mode"),
    ("acrylic-dialog", "color-mix(in srgb, var(--lime) 7%, rgba(70,72,66,.45))", "acrylic: the frame of a dialog"),
    ("acrylic-blur", "blur(28px) saturate(140%)", "what the acrylic does to the place behind"),
    ("acrylic-edge", "rgba(255,255,255,.12)", "the frame’s edge"),
    ("sheet-edge", "rgba(255,255,255,.05)", "an opaque sheet inside the frame"),
    ("veil", "rgba(10,11,9,.42)", "the place behind a mode, dimmed"),
    ("veil-dialog", "rgba(10,11,9,.30)", "a mode behind a dialog, dimmed"),
    ("problem-wash", "color-mix(in srgb, var(--problem) 14%, transparent)", "a Problem tag’s fill"),
    ("note-wash", "color-mix(in srgb, var(--note) 13%, transparent)", "a Note tag’s fill"),
    ("problem-edge", "color-mix(in srgb, var(--problem) 38%, transparent)", "a Problem box’s and the muted remove’s edge"),
    ("note-edge", "color-mix(in srgb, var(--note) 30%, transparent)", "a Note box’s edge"),
    ("problem-box", "color-mix(in srgb, var(--problem) 10%, var(--cutout))", "a Problem box"),
    ("note-box", "color-mix(in srgb, var(--note) 9%, var(--cutout))", "a Note box"),
    ("hover-wash", "color-mix(in srgb, var(--raised) 60%, transparent)", "a place in the top bar under the pointer"),
    ("row-hover", "color-mix(in srgb, var(--raised) 50%, var(--cutout))", "a row under the pointer — opaque, half a step up"),
    ("lime-selection", "color-mix(in srgb, var(--lime) 35%, transparent)", "selected text"),
]
SIZE = [("hairline", "1px", "every line, edge and rule"), ("control-h", "32px", "a button, a field"), ("tag-h", "20px", "a kind tag"), ("mark-h", "24px", "a finding tag"),
        ("bar-h", "52px", "the top bar"), ("icon", "16px", "an icon in a control"), ("icon-s", "14px", "an icon in a tag"),
        ("icon-l", "20px", "an icon shown alone"), ("panel-w", "384px", "the item panel"), ("pill-w", "3px", "the active row’s lime pill"),
        ("dot", "6px", "the Checked dot"), ("dt-w", "116px", "a fact’s label column"), ("stage-name-w", "184px", "a stage’s name column"),
        ("canvas", "1280px", "the width a screen is drawn at on the stand"),
        ("col-xs", "96px", "a narrow column: a finding beside a row"), ("col-s", "160px", "a row’s usage column"),
        ("col-m", "200px", "a row’s actions column"), ("col-l", "320px", "a row’s middle column"), ("col-xl", "360px", "an aside"),
        ("side-w", "440px", "the library sidebar, the item drawer"), ("sheet-w", "640px", "a side sheet"),
        ("modal-w", "520px", "a dialog"), ("measure", "640px", "a readable line of prose")]
FONTS = [("font", '"Geist", system-ui, sans-serif'), ("mono", '"Geist Mono", ui-monospace, monospace')]
MOTION = [("ease", "cubic-bezier(.2,.7,.2,1)"), ("dur", "140ms")]
TRACK = [("track-display", "-.018em"), ("track-title", "-.012em"), ("track-heading", "-.008em"), ("track-label", ".06em")]
# the grey chrome around the stand and the screens — not the product, but values all the same
CHROME = [("page", "#262626"), ("page-2", "#2F2F2F"), ("page-ink", "#E8E8E8"), ("page-ink-2", "#B4B4B4"), ("page-line", "#3D3D3D")]


def css():
    out = ["/* tokens.css — Mica · Lime, the working style of AI Stack Builder.",
           "   Generated by tools/concept_tokens.py; do not edit by hand. Stage 4 of phase 06.",
           "   concept.html and mica-lime.html take every value from here. */", "", ":root {"]
    grp = None
    for n, v, g, role, why in COLORS:
        if g != grp:
            out.append(f"  /* colour · {g} */")
            grp = g
        out.append(f"  --{n}: {v};{' ' * max(1, 10 - len(v))}/* {role} — {why} */")
    out.append("  /* type */")
    out += [f"  --{n}: {v};" for n, v in FONTS]
    out += [f"  --t-{n}: {w} {s}px/{lh}px var(--{'mono' if n == 'code' else 'font'});  /* {use} */" for n, w, s, lh, _, use in TYPE]
    out += [f"  --{n}: {v};" for n, v in TRACK]
    out.append("  /* spacing — a 4 px scale */")
    out += [f"  --s{n}: {px}px;" for n, px in SPACE]
    out.append("  /* radius */")
    out += [f"  --r-{n}: {px}px;" for n, px in RADIUS]
    out.append("  /* size */")
    out += [f"  --{n}: {v};  /* {use} */" for n, v, use in SIZE]
    out.append("  /* motion */")
    out += [f"  --{n}: {v};" for n, v in MOTION]
    out.append("  /* the grey page around the stand — not part of the style */")
    out += [f"  --{n}: {v};" for n, v in CHROME]
    out.append("}")
    out += ["", "/* built from the colours: declared on every theme root, so each theme recomputes them",
            "   (a var() inside a custom property resolves where it is declared, not where it is used) */",
            ":root, .theme-light {", "  /* shadow */"]
    out += [f"  --shadow-{n}: {v};  /* {use} */" for n, v, use in SHADOW]
    out.append("  /* material and washes */")
    out += [f"  --{n}: {v};  /* {use} */" for n, v, use in MATERIAL]
    out.append("}")
    out += ["", "/* the light slice — one proof that light is designed, not inverted (README, stage 4). Full theme: phase 09. */",
            ".theme-light {"]
    out += [f"  --{n}: {v};" for n, v in LIGHT.items()]
    out += ["  --shadow-cutout: inset 0 0 0 1px var(--line);", "  --problem-box: color-mix(in srgb, var(--problem) 7%, var(--cutout));",
            "  --note-box: color-mix(in srgb, var(--note) 8%, var(--cutout));", "}", ""]
    return "\n".join(out)


def build():
    OUT.write_text(css(), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
