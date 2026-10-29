"""Phase 06, stage 4: the one source of the working style's values -> 06-concept/tokens.css.

Every colour, type role, radius, spacing step, shadow and material of *Mica · Lime* is defined here
once, written to tokens.css, and nothing else holds a value: concept.html (the stand) and
mica-lime.html (the screens) link tokens.css and use var() only. tools/contrast.py reads the
written file back — not this module — so the contrast table is measured on what ships.

    python tools/concept_tokens.py   -> 06-concept/tokens.css

Each colour carries the attribute or decision it comes from (06-concept/concept.md).
"""
import re
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
    ("control-edge", "#7C7F74", "neutral", "the edge of a checkbox or a radio", "WCAG 1.4.11: a control’s boundary needs 3:1 — 3.5 on the panel"),
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
    ("warning", "#EFA23A", "state", "a button that goes ahead despite a Problem — Export with 1 problem", "Owner, 2026-10-11 (stage 7, #11): the cost of the step is named, never celebrated in lime"),
    ("warning-hover", "#E0962E", "state", "that button, hovered — darker", "States"),
    ("on-warning", "#1A1200", "state", "text on warning", "Contrast"),
    ("danger", "#D4363F", "state", "a button that removes something", "Owner, 2026-10-11: a red remove"),
    ("danger-hover", "#BE2E37", "state", "the remove, hovered — darker, never lighter", "Contrast: white stays above 4.5:1"),
    ("on-danger", "#FFFFFF", "state", "text on danger", "Contrast"),
]
# light slice (README: one light slice of the chosen direction, in stage 4) — overrides only
LIGHT = {
    "ground": "#F4F5EF", "bar": "#ECEDE6", "tray": "#E9EAE2", "cutout": "#FBFBF8", "well-deep": "#F0F1EA",
    "raised": "#FFFFFF", "control": "#FFFFFF", "control-edge": "#7E8276", "control-hover": "#F1F2EB", "line": "#DCDED4", "line-strong": "#C3C6BA",
    "text": "#181A14", "text-2": "#464A40", "text-3": "#5F6358", "lime": "#C6EF5A", "lime-hover": "#BCE84A",
    "on-lime": "#141A08", "lime-mark": "#55700F", "warning": "#9C5800", "warning-hover": "#8A4E00", "on-warning": "#FFFFFF", "problem": "#B4232E", "note": "#7A5600", "checked": "#464A40", "skipped": "#5F6358",
}
SPACE = [("1", 4), ("2", 8), ("3", 12), ("4", 16), ("5", 20), ("6", 24), ("8", 32), ("10", 40), ("12", 48)]
TYPE = [  # name, weight, size, line-height, sample, use
    ("display", 600, 28, 34, "acme-billing-api", "a project’s name"),
    ("title", 600, 20, 26, "Checked just now", "the Export mode’s verdict"),
    ("heading", 600, 16, 22, "Remove eslint-autofix from acme-billing-api?", "the item panel, a dialog, a card"),
    ("body", 400, 14.5, 21, "Reads a migration before it runs and flags long locks.", "names, sentences"),
    ("button", 500, 13.5, 16, "Export", "buttons and the places"),
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
    ("focus", "0 0 0 2px var(--ground), 0 0 0 4px var(--lime-mark)", "keyboard focus — 2 px lime with a gap; lime-mark, so the light theme’s ring holds 3:1 (phase 07 review)"),
]
MATERIAL = [
    ("acrylic", "color-mix(in srgb, var(--lime) 7%, rgba(62,64,58,.42))", "acrylic: the frame of the Export mode"),
    ("acrylic-dialog", "color-mix(in srgb, var(--lime) 7%, rgba(70,72,66,.45))", "acrylic: the frame of a dialog"),
    ("acrylic-blur", "blur(28px) saturate(140%)", "what the acrylic does to the place behind"),
    ("acrylic-edge", "rgba(255,255,255,.12)", "the frame’s edge"),
    ("sheet-edge", "rgba(255,255,255,.05)", "an opaque sheet inside the frame"),
    ("veil", "rgba(10,11,9,.58)", "the place behind a mode or a dialog, dimmed — .42 until phase 07: the critique found it barely separated"),
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
    ("segment-hover", "color-mix(in srgb, var(--raised) 55%, var(--well-deep))", "a segment under the pointer, on its recessed track — phase 07"),
    ("on-lime-track", "color-mix(in srgb, var(--on-lime) 25%, transparent)", "a spinner’s track on a lime button — phase 07"),
]
SIZE = [("hairline", "1px", "every line, edge and rule"), ("control-h", "32px", "a button, a field"), ("control-h-s", "28px", "a control inside a panel or a track: a tab, a segment, Add — phase 07"), ("tag-h", "20px", "a kind tag"), ("mark-h", "24px", "a finding tag"),
        ("bar-h", "52px", "the top bar"), ("icon", "16px", "an icon in a control"), ("icon-s", "14px", "an icon in a tag"),
        ("icon-l", "20px", "an icon shown alone"), ("panel-w", "384px", "the item panel"), ("pill-w", "3px", "the active row’s lime pill"),
        ("dot", "6px", "the Checked dot"), ("dt-w", "116px", "a fact’s label column"), ("stage-name-w", "300px", "a stage’s name column — wide enough for SETUP.md’s two-line name"),
        ("canvas", "1280px", "the width a screen is drawn at on the stand"),
                ("col-m", "200px", "a row’s actions column"), ("col-l", "320px", "a row’s middle column"), ("col-xl", "360px", "an aside"),
        ("side-w", "440px", "the library sidebar, the item drawer"), ("sheet-w", "640px", "a side sheet"),
        ("modal-w", "520px", "a dialog"), ("measure", "640px", "a readable line of prose"),
        ("measure-wide", "820px", "a lead paragraph on the stand"),
        ("z-sticky", "1", "a sticky head above its own list — phase 07"), ("z-popover", "5", "a popover above the page — phase 07")]
FONTS = [("font", '"Geist", system-ui, sans-serif'), ("mono", '"Geist Mono", ui-monospace, monospace')]
MOTION = [("ease", "cubic-bezier(.2,.7,.2,1)"), ("dur", "140ms"), ("dur-spin", "900ms"), ("dur-shimmer", "1400ms")]
TRACK = [("track-display", "-.018em"), ("track-title", "-.012em"), ("track-heading", "-.008em"), ("track-label", ".06em")]
# weights a role overrides (phase 07 review, B-13: they were bare numbers in the kit)
WEIGHT = [("weight-regular", "400"), ("weight-medium", "500"), ("weight-strong", "600")]
# icons that CSS draws itself (a mask), so a control needs no extra markup — Lucide, 1.75 stroke
CSS_ICONS = [("icon-add", "plus", "a row you can add to the set"), ("icon-added", "check", "a row already in the set"),
             ("icon-empty-set", "layers", "an empty state that has no icon of its own in the markup"),
             ("icon-chevron", "chevron-right", "a disclosure that opens: the original of a detached field (phase 07)")]
# drawn in a colour (a background image, not a mask): the tick inside a checked checkbox, in --on-lime
CSS_GLYPHS = [("glyph-check", "check", "#141A08", "2.5", "the tick in a checked checkbox, --on-lime on --lime")]


def _icon_uri(name, stroke="black", width="1.75"):
    import re as _re
    svg = (ROOT / "06-concept" / "icons" / "lucide" / f"{name}.svg").read_text(encoding="utf-8")
    inner = _re.search(r"<svg[^>]*>(.*)</svg>", svg, _re.S).group(1).strip()
    inner = _re.sub(r"\s+", " ", inner).replace('"', "'")
    body = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='" + stroke.replace("#", "%23") + "' stroke-width='" + width + "' "
            "stroke-linecap='round' stroke-linejoin='round'>" + inner + "</svg>")
    return 'url("data:image/svg+xml,' + body.replace("<", "%3C").replace(">", "%3E") + '")'


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
    out += [f"  --{n}: {v};" for n, v in WEIGHT]
    out.append("  /* spacing — a 4 px scale */")
    out += [f"  --s{n}: {px}px;" for n, px in SPACE]
    out.append("  /* radius */")
    out += [f"  --r-{n}: {px}px;" for n, px in RADIUS]
    out.append("  /* size */")
    out += [f"  --{n}: {v};  /* {use} */" for n, v, use in SIZE]
    out.append("  /* icons CSS draws as a mask */")
    out += [f"  --{n}: {_icon_uri(f)};  /* {use} */" for n, f, use in CSS_ICONS]
    out += [f"  --{n}: {_icon_uri(f, c, w)};  /* {use} */" for n, f, c, w, use in CSS_GLYPHS]
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


# ===== phase 08: the same values on two levels -> 08-design-tokens/tokens.css =====
# Nothing below holds a value of its own: every primitive is read off COLORS and the lists above, and check08()
# proves that every semantic token resolves to exactly the value phase 07's kit used for that role.
OUT08 = ROOT / "08-design-tokens" / "tokens.css"


def _oklab_l(hexv):
    def lin(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(int(hexv[i:i + 2], 16)) for i in (1, 3, 5))
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    return 0.2104542553 * l ** (1 / 3) + 0.7936177850 * m ** (1 / 3) - 0.0040720145 * s ** (1 / 3)


def step(hexv):
    """OKLab lightness, inverted, x1000: what a scale is sorted by. Darker is a bigger number. Until 2026-10-29 it
    was also the name (D4); the owner moved the names to a 50-step grade (Q46), and this stays the order."""
    return round((1 - _oklab_l(hexv)) * 1000)


# hue families, by DESIGN.md's own names: Mica, Signal Lime, Problem Rose, Note and Warning Amber, Remove Red
HUE = {"#C6EF5A": "lime", "#D3F57A": "lime", "#141A08": "lime", "#FF8F98": "rose", "#F2C661": "amber",
       "#EFA23A": "amber", "#E0962E": "amber", "#1A1200": "amber", "#D4363F": "red", "#BE2E37": "red",
       # the light slice (phase 06, stage 4), which joins in phase 08, step 5
       "#BCE84A": "lime", "#55700F": "lime", "#B4232E": "rose", "#7A5600": "amber", "#9C5800": "amber", "#8A4E00": "amber"}
# the rgba() the tokens wrote inline (audit V-8 … V-11), now named: colour + alpha
ALPHA = [("black-a35", "rgba(0,0,0,.35)", "the shadow’s black — written three times in phase 07 (audit D-4), once here"),
         ("black-a12", "rgba(0,0,0,.12)", "the sheet’s shadow in light — owner, 2026-10-28: .35 read too heavy on light"),
         ("white-a04", "rgba(255,255,255,.04)", "the tile’s top highlight"),
         ("white-a05", "rgba(255,255,255,.05)", "an opaque sheet’s edge"),
         ("mica-a58", "rgba(10,11,9,.58)", "the veil: a near-black Mica at 58 %"),
         ("mica-a45", "rgba(70,72,66,.45)", "the acrylic’s grey: a mid Mica at 45 %"),
         ("mica-light-a45", "rgba(195,198,186,.45)", "the acrylic’s grey in light: light’s --line-strong at the same 45 % — owner, 2026-10-28: the dark glass read too heavy on light")]


def _scale(values, hue):
    """One hue's values in one theme, lightest first: the order its grades are given in."""
    return sorted({v.upper() for v in values if v.upper() != "#FFFFFF" and HUE.get(v.upper(), "mica") == hue}, key=step)


def prim_name(hexv):
    """A primitive's name: its hue and its grade, 50, 100, 150 … from the lightest value of that hue (owner, Q46).
    There is one scale per theme: the dark kit's values are --mica-50 …, a value only the light slice has is
    --mica-light-50 … . The tight Mica layers do not fit one 50–950 grid: 26 values against 19 steps."""
    hexv = hexv.upper()
    if hexv == "#FFFFFF":
        return "white"
    hue = HUE.get(hexv, "mica")
    dark = [v for _, v, *_ in COLORS]
    if hexv in {v.upper() for v in dark}:
        return f"{hue}-{(_scale(dark, hue).index(hexv) + 1) * 50}"
    return f"{hue}-light-{(_scale(light_prims(), hue).index(hexv) + 1) * 50}"


def p(name):
    """var() to the primitive that holds the kit's value for colour `name`."""
    return f"var(--{prim_name(dict((n, v) for n, v, *_ in COLORS)[name])})"


# name, value, source: the uses in 08-design-tokens/tokens-audit.md it grew from; "was --x" when renamed or split
SEMANTIC = [
    ("surfaces", [
        ("ground", p("ground"), "the page’s ground — html, body, .canvas (83 pages / 241 steps); also the gap in the focus ring (M-15, kept with it until phase 09)"),
        ("bar", p("bar"), "the top bar — .app-header, .shared-header, .run-bar (83 / 241)"),
        ("side", p("bar"), "a side panel — .library-sidebar and its sticky head (13 / 42). Split from --bar, M-13"),
        ("tray", p("tray"), "the tray under the rows — .row-list (37 / 115)"),
        ("state-ground", p("tray"), "the ground of an empty or error state — .state-block (15 / 13). Split from --tray, M-12"),
        ("cutout", p("cutout"), "a row’s cut-out — .row-list>li, .stages>li (59 / 214); the base of the finding boxes and of the row hover"),
        ("neutral-box", p("cutout"), "a box that is not a finding — .callout-reminder, .callout-failure (15 / 14), §11 and critique #5. Split from --cutout, M-11"),
        ("well-deep", p("well-deep"), "the Deep Well — pre.file, .search, .field input and textarea, .dropzone, the track of .scope, a checkbox’s bed (59 / 157). One role in DESIGN.md (M-7), not split"),
        ("raised", p("raised"), "a panel one step up — .card, .drawer, .aside-box, .export-stage, dialog.modal, dialog.popover, dialog.sheet; the skeleton’s base; what every hover is mixed towards (73 / 239)"),
        ("selected", p("raised"), "the selected row — .row-list>li:has(>.is-selected) (37 / 115). Split from --raised, M-5"),
        ("current", p("raised"), "the current place and the current tab — .app-nav a[aria-current], .tabs a[aria-current] (49 / 136). Split from --raised, M-5. The current segment is a lifted control and reads --control (D-3, signed)"),
        ("control", p("control"), "a secondary control — button, .button, .check, select; the lifted current segment, .scope a[aria-current] (80 / 240). Also the progress track: one screen, flagged below"),
        ("control-hover", p("control-hover"), "a control under the pointer — button, .check, select, .remove :hover; the skeleton’s shimmer band"),
        ("disabled", p("control"), "a disabled control’s fill — button[disabled] and its :hover. Split from --control, M-6"),
        ("code-chip", p("control"), "an inline code chip — code (54 / 224). Split from --control, M-6"),
        ("tile", p("control"), "the neutral tile of an empty or error state — svg.icon.state-icon (15 / 13); concept.md: one tile everywhere. Split from --control, M-6"),
    ]),
    ("lines and edges", [
        ("line", p("line"), "a hairline — 14 dividers; the edge of .card, .drawer, .aside-box, .stages>li, .scope; img.avatar’s ring; the cut-out’s inner edge (83 / 241). Divider and edge kept as one (M-8)"),
        ("disabled-edge", p("line"), "a disabled control’s edge — button[disabled]. Split from --line, M-8"),
        ("line-strong", p("line-strong"), "a control’s edge, a tag’s outline, a dashed rule — button, .check, .tag, .sub-rows, .export-stage, pre.file, .card:hover, the selected row’s and the lifted segment’s edge, the neutral box’s edge, the spinner’s track, the scrollbar (83 / 241). Ten jobs, M-9, not split"),
        ("control-edge", p("control-edge"), "the 3:1 edge of a field or a checkbox — .search, .field input and textarea, select, .dropzone, checkbox, radio; a waiting stage’s ring; a Skipped stage’s dashed outline (83 / 241)"),
        ("edge-hover", p("text-3"), "a field’s or a checkbox’s edge under the pointer — .search, .field input, .field textarea, .dropzone, checkbox and radio :hover. Split from --text-3, M-4; the checkbox read Ink 2 until step 6 (T3-1: one role, one name)"),
        ("sheet-edge", "var(--white-a05)", "the edge of an opaque sheet — dialog.modal, dialog.popover, dialog.sheet (20 / 22)"),
    ]),
    ("text", [
        ("text", p("text"), "Ink: primary text — body, dialogs, .callout, .verdict dd, fields, code, pre.file, buttons; emphasis inside secondary text; a place under the pointer or current (83 / 241)"),
        ("text-2", p("text-2"), "Ink 2: sentences and descriptions — ~35 rules; a place at rest; an icon in a secondary button; the stopped glyph; the empty state’s icon; the + Add glyph (83 / 241)"),
        ("text-3", p("text-3"), "Ink 3: metadata — .meta, facts, counts, numbers, times, error codes; section labels; placeholders; a waiting stage; separators; chevrons (83 / 241)"),
        ("disabled-text", p("text-3"), "a disabled control’s text and icon — button[disabled], .check:has(input:disabled). Split from --text-3, M-4"),
    ]),
    ("lime: the act and the mark", [
        ("action", p("lime"), "the primary action — .button-primary’s fill and edge, its busy hover (64 / 168). Was --lime; split, M-1"),
        ("action-hover", p("lime-hover"), "the primary action under the pointer — .button-primary:hover. Was --lime-hover"),
        ("on-action", p("on-lime"), "Lime Ink: text, icon and spinner arc on the action — .button-primary. Was --on-lime"),
        ("control-on", p("lime"), "a checked checkbox or radio — input:checked (45 / 89). Split from --lime, M-1"),
        ("control-on-ink", p("on-lime"), "the tick in a checked checkbox. Split from --on-lime, M-1. Its value used to be a hex inside --glyph-check’s SVG (V-12); the tick is a mask now, drawn in this role"),
        ("brand", p("lime"), "the brand — .icon.logo (71 / 153); the tint of a dialog’s acrylic and of selected text. Split from --lime, M-1"),
        ("mark", p("lime-mark"), "lime as a mark — where you are (the selected row’s pill), Exported (the Export stage’s pill), In this project (.check:has(:checked)::before), running (span.glyph-running), progress (80 / 240). Was --lime-mark"),
        ("focus", p("lime-mark"), "keyboard focus — the ring of --shadow-focus, and the edge of .search, .field input, .dropzone in focus (14 rules). Split from --lime-mark, M-2"),
    ]),
    ("findings", [
        ("problem", p("problem"), "Problem Rose — .tag-problem, .mark-problem, svg.glyph-problem, .callout>.severity, .result-problem; the muted remove inside a Problem, .button-danger-quiet (signed, M-14) (39 / 145)"),
        ("note", p("note"), "Note Amber — .mark-note, svg.glyph-note, .callout-quiet>.severity, .result-note (25 / 136)"),
        ("checked", p("checked"), "Checked: the quiet dot — span.glyph-checked (20 / 99). One component, but a signed role (§6, D1-B), kept"),
        ("skipped", p("skipped"), "Skipped: the slashed circle — svg.glyph-skipped (18 / 92). One component, but a signed role (§6), kept"),
    ]),
    ("acts that cost something", [
        ("warning", p("warning"), "Warning Amber: going ahead despite a Problem — .button-warning. ONE SCREEN (run-default and its 2 steps): flagged for step 6; kept because the owner signed it (2026-10-11)"),
        ("warning-hover", p("warning-hover"), "the same, under the pointer — .button-warning:hover. One screen, as above"),
        ("on-warning", p("on-warning"), "text and icon on warning — .button-warning. One screen, as above"),
        ("danger", p("danger"), "Remove Red: removing something, in its confirmation — .button-danger (5 / 3)"),
        ("danger-hover", p("danger-hover"), "the same, under the pointer, darker — .button-danger:hover"),
        ("on-danger", p("on-danger"), "text and icon on danger — .button-danger"),
    ]),
]
# recipes over a role: each is a shade of one role, so it follows that role into any theme
DERIVED = [
    ("problem-wash", "color-mix(in srgb, var(--problem) 14%, transparent)", "a Problem capsule’s fill — .tag-problem, .mark-problem; the muted remove under the pointer (20 / 72). 14 % against Note’s 13 %: D-2, not merged"),
    ("problem-edge", "color-mix(in srgb, var(--problem) 38%, transparent)", "a Problem box’s and a Conflict tag’s edge; the muted remove’s edge (39 / 145)"),
    ("problem-box", "color-mix(in srgb, var(--problem) 10%, var(--cutout))", "a Problem box — .callout (31 / 84)"),
    ("note-wash", "color-mix(in srgb, var(--note) 13%, transparent)", "a Note capsule’s fill — .mark-note (13 / 69)"),
    ("note-edge", "color-mix(in srgb, var(--note) 30%, transparent)", "a Note box’s edge — .callout-quiet (14 / 69)"),
    ("note-box", "color-mix(in srgb, var(--note) 9%, var(--cutout))", "a Note box — .callout-quiet (14 / 69)"),
    ("hover-wash", "color-mix(in srgb, var(--raised) 60%, transparent)", "a place or a tab under the pointer; In this project under the pointer (49 / 136). One of four hover recipes, D-1: kept apart"),
    ("row-hover", "color-mix(in srgb, var(--raised) 50%, var(--cutout))", "a row or a stage under the pointer (57 / 214). D-1"),
    ("segment-hover", "color-mix(in srgb, var(--raised) 55%, var(--well-deep))", "a segment under the pointer, on its track — .scope a:hover (13 / 42). D-1"),
    ("selection", "color-mix(in srgb, var(--brand) 35%, transparent)", "selected text — ::selection (83 / 241). Was --lime-selection"),
    ("on-action-track", "color-mix(in srgb, var(--on-action) 25%, transparent)", "a spinner’s track on the action — .button-primary span.glyph-running (3 / 8). Was --on-lime-track"),
    ("acrylic-dialog", "color-mix(in srgb, var(--brand) 7%, var(--mica-a45))", "glass round a dialog and the Filters popover — dialog.modal, dialog.popover (16 / 16)"),
    ("veil", "var(--mica-a58)", "the place behind a mode or a dialog, dimmed — .scrim (17 / 22)"),
    ("shadow-tile", "0 1px 2px var(--black-a35), inset 0 1px 0 var(--white-a04)", "lifted one step: the current place, the current segment (49 / 136)"),
    ("shadow-cutout", "inset 0 0 0 1px var(--line), inset 0 1px 2px var(--black-a35)", "pressed in: a row’s cut-out — .row-list>li (37 / 115)"),
    ("shadow-sheet", "0 18px 40px var(--black-a35)", "over the place: dialog.modal, dialog.popover, dialog.sheet (20 / 22)"),
    ("shadow-focus", "0 0 0 2px var(--ground), 0 0 0 4px var(--focus)", "keyboard focus on every focusable thing (14 rules)"),
    ("scheme", "dark", "the native controls’ scheme, for html’s color-scheme — a literal in a class until now (V-5)"),
]
# phase 07's names, for the proof that nothing moved: new semantic token -> the kit variable whose value it took
WAS = {"side": "bar", "state-ground": "tray", "neutral-box": "cutout", "selected": "raised", "current": "raised",
       "disabled": "control", "code-chip": "control", "tile": "control", "disabled-edge": "line", "edge-hover": "text-3",
       "disabled-text": "text-3", "action": "lime", "action-hover": "lime-hover",
       "on-action": "on-lime", "control-on": "lime", "control-on-ink": "on-lime", "brand": "lime", "mark": "lime-mark",
       "focus": "lime-mark", "selection": "lime-selection", "on-action-track": "on-lime-track"}
KIT_DROPPED = set()   # D5: --canvas and --measure-wide looked unused (audit §1), but the showcase's own frame reads them
# geometry a class wrote as a number (audit V-2), named; check08() proves the value is the one the class computed
NEW_GEOMETRY = [
    ("s-half", "2px", "calc(var(--s1) / 2)", "half a step: a chip's padding, a gap between places, tabs and segments — was calc(var(--s1) / 2) ×7 (check T5-1)"),
    ("hairline-2", "2px", "calc(var(--hairline) * 2)", "a doubled line: the spinner's ring, a link's hover underline — was calc(var(--hairline) * 2) (T5-2)"),
    ("door-w", "400px", "calc(var(--s1) * 100)", "the door's one column — .door, was calc(var(--s1) * 100) (audit V-2)"),
    ("door-top", "120px", "calc(var(--s12) * 2 + var(--s6))", "the door's distance from the bar — was calc(var(--s12) * 2 + var(--s6)) (T5-3)"),
    ("modal-top", "144px", "calc(var(--s12) * 3)", "a dialog's distance from the top — was calc(var(--s12) * 3) (T5-3)"),
    ("popover-reserve", "288px", "calc(var(--s12) * 6)", "what a popover leaves of the viewport's height — was 100vh - calc(var(--s12) * 6) (T5-3)"),
    ("search-w", "496px", "calc(var(--measure) - var(--s12) * 3)", "the search field's widest — was calc(var(--measure) - var(--s12) * 3) (T5-3)"),
    ("callout-measure", "832px", "calc(var(--measure) + var(--s12) * 4)", "a callout's sentence, widest — was calc(var(--measure) + var(--s12) * 4) (T5-3)"),
    ("textarea-min-h", "160px", "calc(var(--s10) * 4)", "a textarea's least height — was calc(var(--s10) * 4) (T5-3)"),
    ("state-icon-inset", "14px", "calc((var(--s12) - var(--icon-l)) / 2)", "the inset that centres a 20 px icon in the 48 px state tile — was calc((var(--s12) - var(--icon-l)) / 2) (T5-3)"),
]
NOT_IN_KIT = {"panel-w", "icon-empty-set", "r-xl"}   # in 06's tokens.css, never copied into the kit
STAND_ONLY = NOT_IN_KIT | {"acrylic", "acrylic-blur", "acrylic-edge", "veil-dialog", "page", "page-2", "page-ink", "page-ink-2", "page-line"}  # the stand's, read by no screen
FLAGGED = [  # for step 6's critique: the course's rule — a colour on one screen is not yet a role
    ("--warning, --warning-hover, --on-warning", "one screen: run-default and its flow steps. Kept as roles because the owner signed them"),
    ("the progress track", "one screen: library-json-loading. Not a role: it reads --control (the same value), its value --mark"),
]


def css08():
    colors = dict((n, v) for n, v, *_ in COLORS)
    prims = {}
    for n, v in colors.items():
        prims.setdefault(prim_name(v), (v.upper(), []))[1].append(n)
    fam = ["mica", "white", "lime", "rose", "amber", "red"]
    order = sorted(prims.items(), key=lambda kv: (fam.index(kv[0].split("-")[0]), step(kv[1][0])))
    pad = lambda s: " " * max(1, 26 - len(s))
    out = ["/* tokens.css — AI Stack Builder, Mica · Lime, on two levels. Phase 08, step 2.",
           "   Generated by tools/concept_tokens.py, the same source as 06-concept/tokens.css; do not edit by hand.",
           "",
           "   PRIMITIVE  what a value is: colour, type, space, radius, size, motion, icons. No roles.",
           "              A colour is named by its hue (DESIGN.md: Mica, Lime, Rose, Amber, Red) and its grade: 50, 100,",
           "              150 … from the lightest value of that hue, ordered by OKLab lightness. One scale per theme: a",
           "              value only the light theme reads is --<hue>-light-<grade>. An alpha is --<hue>-a<percent>.",
           "   SEMANTIC   what a colour is for. Every token is a var() to a primitive, and its comment names the uses in",
           "              08-design-tokens/tokens-audit.md it grew from (pages / flow steps). The recipes at the end",
           "              (washes, hovers, shadows) are shades of one role, and follow it into any theme.",
           "",
           "   A component reads colour only through SEMANTIC, and geometry straight from PRIMITIVE.",
           "   No value here is new: the generator checks that every semantic token resolves to the value phase 07's",
           "   kit used for that role, and that no hex appears that the kit or phase 06's light slice did not have.",
           "   THEMES  :root is dark, the product's (§3). [data-theme=\"light\"] is the stress test of step 5, at the end. */",
           "",
           ":root {",
           "  /* ===== PRIMITIVE ===== */",
           "  /* colour — dark; the light values join in step 5 */"]
    for name, (v, was) in order:
        out.append(f"  --{name}: {v};{pad(name + v)}/* was --{', --'.join(was)} */")
    out.append("  /* colour — light: phase 06's signed slice, read by the light theme only */")
    for v in sorted(light_prims(), key=lambda v: (fam.index(HUE.get(v, "mica")), step(v))):
        name = prim_name(v)
        was = [k for k, lv in LIGHT.items() if lv.upper() == v]
        out.append(f"  --{name}: {v};{pad(name + v)}/* light --{', --'.join(was)} */")
    for name, v, why in ALPHA:
        out.append(f"  --{name}: {v};{pad(name + v)}/* {why} */")
    out.append("  /* type */")
    out += [f"  --{n}: {v};" for n, v in FONTS]
    out += [f"  --{n}: {v};" for n, v in WEIGHT]
    wt = {400: "regular", 500: "medium", 600: "strong"}
    out += [f"  --t-{n}: var(--weight-{wt[wg]}) {s}px/{lh}px var(--{'mono' if n == 'code' else 'font'});  /* {use}; the weight was a bare {wg} (audit D-5) */"
            for n, wg, s, lh, _, use in TYPE]
    out += [f"  --{n}: {v};" for n, v in TRACK]
    out.append("  /* space — a 4 px scale */")
    out += [f"  --s{n}: {px}px;" for n, px in SPACE]
    out.append("  /* radius */")
    out += [f"  --r-{n}: {px}px;" for n, px in RADIUS if f"r-{n}" not in NOT_IN_KIT]
    out.append("  /* size, column, layer */")
    out += [f"  --{n}: {v};  /* {use} */" for n, v, use in SIZE if n not in KIT_DROPPED | NOT_IN_KIT]
    out += [f"  --{n}: {v};  /* {use} */" for n, v, _, use in NEW_GEOMETRY]
    out.append("  /* icons CSS draws as a mask */")
    out += [f"  --{n}: {_icon_uri(f)};  /* {use} */" for n, f, use in CSS_ICONS if n not in NOT_IN_KIT]
    out += [f"  --{n}: {_icon_uri(f, 'black', wd)};  /* the tick in a checked checkbox, now a mask: its colour is --control-on-ink, not a hex inside the SVG (audit V-12) */" for n, f, c, wd, use in CSS_GLYPHS]
    out.append("  /* motion */")
    out += [f"  --{n}: {v};" for n, v in MOTION]
    out += ["", "  /* ===== SEMANTIC ===== */"]
    for grp, rows in SEMANTIC:
        out.append(f"  /* {grp} */")
        out += [f"  --{n}: {v};{pad(n + v)}/* {src} */" for n, v, src in rows]
    out += [""] + contrast_comment("dark") + ["}", "", "/* ===== SEMANTIC: recipes over a role. Declared wherever a theme is set, so a theme recomputes them",
            "   (a var() inside a custom property resolves where it is declared, not where it is used) ===== */",
            ':root, [data-theme] {']
    out += [f"  --{n}: {v};  /* {src} */" for n, v, src in DERIVED]
    out += ["}", ""] + light_block() + ["", "/* FLAGGED for step 6's critique:"]
    out += [f"   - {what}: {why}" for what, why in FLAGGED]
    out[-1] += " */"
    out.append("")
    return "\n".join(out)


# ===== phase 08, step 5: the stress test — the light theme overrides SEMANTIC only =====
# The light slice of phase 06 (LIGHT, below COLORS) is written in phase 07's names; each role takes the value of the
# variable it was split from (WAS). A role whose source has no light value keeps its dark one: a gap, listed, not
# filled (D1) — a value is the owner's to sign, not the refactor's to invent.
LIGHT_RECIPES = [("shadow-cutout", "inset 0 0 0 1px var(--line)", "light: the hairline only, no inner shade"),
                 ("problem-box", "color-mix(in srgb, var(--problem) 7%, var(--cutout))", "light: 7 %, not 10 %"),
                 ("note-box", "color-mix(in srgb, var(--note) 8%, var(--cutout))", "light: 8 %, not 9 %"),
                 ("acrylic-dialog", "color-mix(in srgb, var(--brand) 7%, var(--mica-light-a45))", "light: a light grey under the same 7 % lime — owner, 2026-10-28"),
                 ("shadow-sheet", "0 18px 40px var(--black-a12)", "light: the same lift at a third of the black — owner, 2026-10-28")]


# a role whose light value is not the slice's, and why (tokens-check.md)
LIGHT_FIXED = {"control-on": ("#55700F", "the light mark, not the slice's lime: lime on white is 1.32:1, and a checked control needs 3:1 (T7-1)"),
               "control-on-ink": ("#FFFFFF", "white, the tick on the light mark: 5.66:1 (T7-1)")}


def light_values():
    out = {}
    for _, rows in SEMANTIC:
        for n, _v, _src in rows:
            src = WAS.get(n, n)
            if n in LIGHT_FIXED:
                out[n] = f"var(--{prim_name(LIGHT_FIXED[n][0])})"
            elif src in LIGHT:
                out[n] = f"var(--{prim_name(LIGHT[src])})"
    return out


def light_source(n):
    """T4-1: the source comment of a light line."""
    if n in LIGHT_FIXED:
        return LIGHT_FIXED[n][1]
    src = WAS.get(n, n)
    return f"the slice's light --{src}" + ("" if src == n else f" (this role was split from it)")


def light_gaps():
    return [n for _, rows in SEMANTIC for n, _v, _s in rows if n not in light_values()]


def light_block():
    vals = light_values()
    out = ['/* ===== THEME: light — the stress test of the semantic level (phase 08, step 5) =====',
           "   Only SEMANTIC tokens are overridden. Not a primitive, not a component: if the light theme needed either,",
           "   the architecture would have a hole. The values are phase 06's signed light slice (concept.md), each role",
           "   taking the value of the variable it was split from. Whether light stays in the product is the owner's call.",
           "   GAPS (D1): these roles have no light value of their own, so they keep the dark one —",
           "     " + ", ".join("--" + g for g in light_gaps()) + ".",
           "   Filling them is the owner's word or lesson 09, never the refactor's. */",
           '[data-theme="light"] {']
    for grp, rows in SEMANTIC:
        names = [n for n, _v, _s in rows if n in vals]
        if names:
            out.append(f"  /* {grp} */")
            out += [f"  --{n}: {vals[n]};{' ' * max(1, 30 - len(n + vals[n]))}/* {light_source(n)} */" for n in names]
    out.append("  /* recipes the slice signed apart */")
    out += [f"  --{n}: {v};  /* {why} */" for n, v, why in LIGHT_RECIPES]
    out.append("  --scheme: light;  /* native controls drawn light */")
    out += [""] + contrast_comment("light") + ["}"]
    return out


def light_prims():
    return sorted({LIGHT[k].upper() for k in LIGHT} - {v.upper() for _, v, *_ in COLORS}, key=step)


# contrast: phase 06's pairs (tools/contrast.py), in today's role names, measured on this file as written
RENAMED = {"lime": "action", "lime-hover": "action-hover", "on-lime": "on-action", "lime-mark": "mark"}
PAIR_ROLE = {"kit: the focus ring (non-text, 3:1)": ("focus", "ground"),
             "mockups: the tick in a checked checkbox": ("control-on-ink", "control-on"),
             "mockups: a checkbox or radio’s edge in a popover (non-text, 3:1)": ("control-edge", "raised"),
             "mockups: a checkbox or radio’s edge in the sidebar (non-text, 3:1)": ("control-edge", "side"),
             "kit: a tab's count in the library sidebar": ("text-3", "side"),
             "a disabled button’s label": ("disabled-text", "disabled"),
             "mockups: inline code": ("text", "code-chip"),
             "mockups: an empty or error state’s icon on its neutral tile (non-text, 3:1)": ("text-2", "tile"),
             "mockups: an empty or error state’s sentence": ("text-2", "state-ground"),
             "mockups: an error code under a state": ("text-3", "state-ground"),
             "kit: the import progress bar (non-text, 3:1)": ("mark", "control")}
# pairs phase 08 measures that contrast.py never did (tokens-check.md)
EXTRA_PAIRS = [("control-on", "raised", "phase 08: a checked checkbox or radio on a panel (non-text, 3:1) — T7-1", 3.0),
               ("control-on", "well-deep", "phase 08: a checked radio's dot against its well (non-text, 3:1) — T7-1", 3.0)]


def _theme_values(text, theme):
    import re as _re
    root = "\n".join(_re.findall(r"^(?::root|:root, \[data-theme\]) \{\n(.*?)\n\}", text, _re.S | _re.M))
    vals = dict(_re.findall(r"^\s*--([\w-]+):\s*(.*?);", root, _re.M))
    if theme == "light":
        blk = _re.search(r'^\[data-theme="light"\] \{\n(.*?)\n\}', text, _re.S | _re.M)
        if blk:
            vals.update(dict(_re.findall(r"^\s*--([\w-]+):\s*(.*?);", blk.group(1), _re.M)))
    return vals


def colour(vals, expr, base=None):
    """An opaque RGB for a colour expression: a hex, a var(), or a color-mix over a colour or over transparent
    (then laid on `base`, the surface it sits on)."""
    import re as _re
    expr = expr.strip()
    m = _re.fullmatch(r"var\(--([\w-]+)\)", expr)
    if m:
        return colour(vals, vals[m.group(1)], base)
    if expr.startswith("#"):
        return tuple(int(expr[i:i + 2], 16) for i in (1, 3, 5))
    m = _re.fullmatch(r"color-mix\(in srgb, (var\(--[\w-]+\)) (\d+)%, (.*)\)", expr)
    if m:
        a, p = colour(vals, m.group(1)), int(m.group(2)) / 100
        b = base if m.group(3) == "transparent" else colour(vals, m.group(3))
        return tuple(round(a[i] * p + b[i] * (1 - p)) for i in range(3))
    raise ValueError(expr)


def contrast_pairs():
    import contrast as _c
    out = []
    for fg, bg, what, bar in _c.PAIRS:
        if what in PAIR_ROLE:
            fg, bg = PAIR_ROLE[what]
        else:
            fg = RENAMED.get(fg, fg)
            bg = "@".join(RENAMED.get(x, x) for x in bg.split("@"))
        out.append((fg, bg, what, bar))
    return out + EXTRA_PAIRS


def measure(text, theme):
    import contrast as _c
    vals = _theme_values(text, theme)
    rows = []
    for fg, bg, what, bar in contrast_pairs():
        if "@" in bg:
            wash, under = bg.split("@")
            b = colour(vals, vals[wash], colour(vals, f"var(--{under})"))
        else:
            b = colour(vals, f"var(--{bg})")
        f = colour(vals, f"var(--{fg})", b)
        rows.append((fg, bg, what, bar, _c.ratio(f, b)))
    return rows


def contrast_comment(theme):
    rows = measure(_CURRENT[0], theme) if _CURRENT else []
    if not rows:
        return [f"  /* contrast ({theme}): measured after the file is written — see build() */"]
    fails = [r for r in rows if r[3] > 1 and r[4] < r[3]]
    out = [f"  /* CONTRAST, {theme} — WCAG AA, measured on this file as written by tools/concept_tokens.py:",
           "     4.5:1 for text, 3:1 for a control's edge or a mark (non-text). " +
           (f"{len(rows) - len(fails)} of {len(rows)} pass." if not fails else f"FAILING: {len(fails)} of {len(rows)}.")]
    for fg, bg, what, bar, r in rows:
        mark = "info" if bar == 1.0 else ("AA  " if r >= bar else "FAIL")
        out.append(f"     {r:5.2f} {mark}  --{fg} on --{bg} — {what}")
    out.append("  */")
    return out


_CURRENT = []


def _resolve(decls, expr, depth=0):
    import re as _re
    assert depth < 12, expr
    return _re.sub(r"var\(--([\w-]+)\)", lambda m: _resolve(decls, decls[m.group(1)], depth + 1), expr)


def check08(text):
    """No value is new and nothing moved: every token resolves to the kit's value for its role. The kit's :root
    was 06-concept/tokens.css's dark values, character for character (phase 07's guard 5), so that is the
    baseline now that kit.css is gone (phase 08, step 4)."""
    import re as _re
    kit_css = css()
    kit = {}
    for blk in _re.findall(r"^:root(?:, \.theme-light)? \{\n(.*?)\n\}", kit_css, _re.S | _re.M):
        kit.update(dict(_re.findall(r"^\s*--([\w-]+):\s*(.*?);", blk, _re.M)))
    new = _theme_values(text, "dark")
    prims = {prim_name(v) for _, v, *_ in COLORS} | {n for n, *_ in ALPHA} | {prim_name(v) for v in light_prims()}
    bad = []
    for n in new:
        if n in prims or n == "scheme":
            continue
        if n == "glyph-check":   # the same tick, drawn as a mask: only its stroke colour left the SVG
            a, b = new[n].replace("stroke='black'", ""), kit[n].replace("stroke='%23141A08'", "")
            if a != b:
                bad.append("--glyph-check is not the kit's tick")
            continue
        geo = {g: (v, was) for g, v, was, _ in NEW_GEOMETRY}
        if n in geo:
            expr = re.sub(r"var\(--([\w-]+)\)", lambda m: kit[m.group(1)].replace("px", ""), geo[n][1][5:-1])
            want = eval(expr, {"__builtins__": {}})  # arithmetic on the kit's own px values, nothing else
            if new[n] != f"{want:g}px":   # the value as written in the file, not as this module meant it
                bad.append(f"--{n} = {new[n]} but {geo[n][1]} is {want:g}px")
            continue
        old = WAS.get(n, n)
        if old not in kit:
            bad.append(f"--{n}: no kit variable --{old}")
            continue
        a = _resolve(new, new[n]).replace(" ", "").lower()
        b = _resolve(kit, kit[old]).replace(" ", "").lower()
        if a != b:
            bad.append(f"--{n} = {a}  but the kit's --{old} = {b}")
    missing = set(kit) - {WAS.get(n, n) for n in new} - KIT_DROPPED - STAND_ONLY - {"lime", "lime-hover", "on-lime", "lime-mark", "lime-selection", "on-lime-track"}
    if missing:
        bad.append("kit variables with no token: " + ", ".join(sorted(missing)))
    hexes = lambda t: {h.upper() for h in _re.findall(r"#[0-9A-Fa-f]{6}\b", t)}
    allowed = hexes(kit_css)   # 06's file holds the dark values and the light slice
    if hexes(text) - allowed:
        bad.append("new hex values: " + ", ".join(sorted(hexes(text) - allowed)))
    # the light theme: every role it overrides resolves to phase 06's light value for the variable it came from
    light = _theme_values(text, "light")
    for n, v in light_values().items():
        got = _resolve(light, light[n]).upper()
        if n in LIGHT_FIXED:
            if got != LIGHT_FIXED[n][0]:
                bad.append(f"light --{n} = {got}, tokens-check.md says {LIGHT_FIXED[n][0]}")
            continue
        if got != LIGHT[WAS.get(n, n)].upper():
            bad.append(f"light --{n} = {got}, the slice says {LIGHT[WAS.get(n, n)]}")
    blk = _re.search(r'^\[data-theme="light"\] \{\n(.*?)\n\}', text, _re.S | _re.M).group(1)
    overridden = set(_re.findall(r"^\s*--([\w-]+):", blk, _re.M))
    if overridden & prims:
        bad.append("the light theme overrides a primitive: " + ", ".join(sorted(overridden & prims)))
    if hexes(blk):
        bad.append("the light theme writes a hex instead of a primitive: " + ", ".join(sorted(hexes(blk))))
    unused = {pn for pn in prims if f"var(--{pn})" not in text}
    if unused:
        bad.append("primitives no role reads: " + ", ".join(sorted(unused)))
    if bad:
        raise SystemExit("08-design-tokens/tokens.css does not keep the kit's values:\n  " + "\n  ".join(bad))
    return len(new)


def build():
    OUT.write_text(css(), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    _CURRENT[:] = [css08()]          # once to have the values, once more to write their contrast into the file
    text = css08()
    n = check08(text)
    fails = [(t, r) for t in ("dark", "light") for r in measure(text, t) if r[3] > 1 and r[4] < r[3]]
    OUT08.write_text(text, encoding="utf-8")
    print(f"wrote {OUT08.relative_to(ROOT)}: {n} tokens, each resolves to the kit's value for its role; "
          f"contrast {len(contrast_pairs())} pairs × 2 themes, failing: {len(fails)}; light gaps: {len(light_gaps())}")
    for t, r in fails:
        print(f"  FAIL {t}: --{r[0]} on --{r[1]} {r[4]:.2f} — {r[2]}")


if __name__ == "__main__":
    build()
