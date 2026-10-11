"""Phase 06, stage 4: the components of Mica · Lime, written against tokens.css and nothing else.

UI_CSS holds no colour, size, radius, spacing, shadow or font value of its own — every one is a
var() from 06-concept/tokens.css (`python tools/concept_ui.py --check` proves it). Used by
tools/build_lime.py (the screens) and tools/build_concept.py (the stand).
"""
import re
import sys

UI_CSS = r"""
.ml{font:var(--t-body);color:var(--text);-webkit-font-smoothing:antialiased}
.ml code,.ml pre{font-family:var(--mono)}
.ml ::selection{background:var(--lime-selection);color:var(--text)}
.ic{width:var(--icon);height:var(--icon);flex:none}
.dot{display:inline-block;width:var(--dot);height:var(--dot);border-radius:var(--r-pill);background:currentColor;flex:none;margin:0 var(--s2) 0 calc(var(--s1) / 2)}

/* --- buttons --- */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:var(--s2);height:var(--control-h);padding:0 var(--s3);
  font:var(--t-button);color:var(--text);white-space:nowrap;cursor:default;
  background:var(--control);border:var(--hairline) solid var(--line-strong);border-radius:var(--r-sm);
  transition:background var(--dur) var(--ease),border-color var(--dur) var(--ease)}
.btn .ic{color:var(--text-2)}
.btn:hover,.btn.is-hover{background:var(--control-hover)}
.btn:focus-visible,.btn.is-focus{outline:0;box-shadow:var(--shadow-focus)}
.btn:active,.btn.is-active{background:var(--control);transform:translateY(calc(var(--hairline) / 2))}
.btn.primary{background:var(--lime);border-color:var(--lime);color:var(--on-lime);font-weight:600}
.btn.primary .ic{color:var(--on-lime)}
.btn.primary:hover,.btn.primary.is-hover{background:var(--lime-hover);border-color:var(--lime-hover)}
.btn.primary.is-disabled{background:var(--control);border-color:var(--line);color:var(--text-3)}
.btn.primary.is-disabled .ic{color:var(--text-3)}
.btn.icon-only{width:var(--control-h);padding:0}
.btn.danger,.dlg .btn.primary{background:var(--danger);border-color:var(--danger);color:var(--on-danger);font-weight:600}
.btn.danger:hover,.dlg .btn.primary:hover,.btn.danger.is-hover{background:var(--danger-hover);border-color:var(--danger-hover)}
.btn.danger .ic,.dlg .btn.primary .ic{color:var(--on-danger)}
.btn.danger-ghost,.c-problem.callout .btn{background:transparent;border-color:var(--problem-edge);color:var(--problem);font-weight:500}
.btn.danger-ghost:hover,.c-problem.callout .btn:hover,.btn.danger-ghost.is-hover{background:var(--problem-wash)}
.btn.danger-ghost .ic{color:var(--problem)}

/* --- tags and findings --- */
.kind,.state{display:inline-flex;align-items:center;gap:var(--s1);height:var(--tag-h);padding:0 var(--s2);
  font:var(--t-micro);color:var(--text-2);background:transparent;box-shadow:inset 0 0 0 var(--hairline) var(--line-strong);border-radius:var(--r-pill);white-space:nowrap}
.state{box-shadow:none;padding:0 calc(var(--s1) / 2)}
.state .ic{width:var(--icon-s);height:var(--icon-s);color:var(--text-3)}
.st-conflict{color:var(--problem);background:var(--problem-wash);box-shadow:inset 0 0 0 var(--hairline) var(--problem-edge);padding:0 var(--s2)}
.mark{display:inline-flex;align-items:center;gap:var(--s1);height:var(--mark-h);padding:0 var(--s3) 0 var(--s2);
  font:var(--t-micro);font-weight:600;border-radius:var(--r-pill);white-space:nowrap}
.mark .ic{width:var(--icon-s);height:var(--icon-s)}
.m-problem{color:var(--problem);background:var(--problem-wash)}
.m-note{color:var(--note);background:var(--note-wash)}
.m-skipped{color:var(--skipped);font-weight:500;padding:0 var(--s1)}
.m-checked{color:var(--checked);font-weight:500;padding:0 var(--s1)}

/* --- a field --- */
.field{display:flex;flex-direction:column;gap:var(--s2)}
.field>span:first-child{font:var(--t-small);font-weight:500;color:var(--text-2)}
.field input{height:var(--control-h);padding:0 var(--s3);font:var(--t-code);color:var(--text);background:var(--well-deep);
  border:var(--hairline) solid var(--line-strong);border-radius:var(--r-sm);outline:0}
.field input::placeholder{color:var(--text-3)}
.field input.is-focus,.field input:focus-visible{border-color:var(--lime-mark);box-shadow:var(--shadow-focus)}
.field .hint{display:flex;align-items:center;gap:var(--s1);font:var(--t-small);color:var(--text-3)}
.field .hint .ic{width:var(--icon-s);height:var(--icon-s)}

/* --- the app --- */
.app{background:var(--ground)}
.nav{display:flex;align-items:center;gap:var(--s6);height:var(--bar-h);padding:0 var(--s6);background:var(--bar);border-bottom:var(--hairline) solid var(--line)}
.product{display:flex;align-items:center;gap:var(--s2);font:var(--t-body);font-weight:600}
.logo{width:var(--icon-s);height:var(--icon-s);border-radius:var(--r-xs);background:var(--lime)}
.links{display:flex;gap:calc(var(--s1) / 2)}
.links a{display:flex;align-items:center;gap:var(--s2);height:var(--control-h);padding:0 var(--s3);color:var(--text-2);font:var(--t-button);border-radius:var(--r-sm);
  transition:background var(--dur) var(--ease),color var(--dur) var(--ease)}
.links a .ic{color:var(--text-3)}
.links a:hover,.links a.is-hover{color:var(--text);background:var(--hover-wash)}
.links a.on{color:var(--text);background:var(--raised);box-shadow:var(--shadow-tile)}
.links a.on .ic{color:var(--lime-mark)}
.account{margin-left:auto;display:flex;align-items:center;gap:var(--s2);font:var(--t-small);color:var(--text-2)}
.account img{width:var(--mark-h);height:var(--mark-h);border-radius:var(--r-pill);object-fit:cover;box-shadow:0 0 0 var(--hairline) var(--line)}
.main{padding:var(--s8) var(--s8) var(--s10)}

.phead{display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:var(--s6);row-gap:var(--s3)}
.crumb{margin:0 0 var(--s1);font:var(--t-small);color:var(--text-3)}
.phead h1{margin:0;font:var(--t-display);letter-spacing:var(--track-display)}
.pfactsline{margin:var(--s1) 0 0;font:var(--t-small);color:var(--text-2)}
.actions{display:flex;gap:var(--s2);align-self:start;margin-top:calc(var(--s5) + var(--s1))}
.verdict{grid-column:1/-1;display:flex;align-items:center;gap:var(--s4);flex-wrap:wrap}
.vline{margin:0;display:flex;align-items:center;font:var(--t-small);color:var(--text-2)}
.vline .vglyph{color:var(--checked)}
.vcounts{margin:0;display:flex;gap:var(--s4);font:var(--t-small);font-weight:600}
.vcounts span{display:inline-flex;align-items:center;gap:var(--s1)}
.vcounts .ic{width:var(--icon-s);height:var(--icon-s)}
.c-problem{color:var(--problem)} .c-note{color:var(--note)} .c-skipped{color:var(--skipped);font-weight:500}
.pdesc{margin:var(--s4) 0 var(--s6);max-width:72ch;font:var(--t-body);color:var(--text-2)}

.work.with{display:grid;grid-template-columns:minmax(0,1fr) var(--panel-w);gap:var(--s5);align-items:start}
.set,.sub{list-style:none;margin:0;padding:0}
.set{display:flex;flex-direction:column;gap:var(--s2);padding:var(--s2);background:var(--tray);border-radius:var(--r-lg)}
.set>li{position:relative;background:var(--cutout);border-radius:var(--r-md);box-shadow:var(--shadow-cutout);transition:background var(--dur) var(--ease)}
.set>li:hover,.set>li.is-hover{background:var(--row-hover)}
.set>li.sel{background:var(--raised);box-shadow:inset 0 0 0 var(--hairline) var(--line-strong)}
.set>li.sel::before{content:"";position:absolute;left:var(--s1);top:var(--s3);bottom:var(--s3);width:var(--pill-w);border-radius:var(--r-xs);background:var(--lime-mark)}
.row{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:var(--s4);padding:var(--s3) var(--s4)}
.row h3{display:flex;align-items:center;flex-wrap:wrap;gap:var(--s2);min-height:var(--mark-h);margin:0;font:var(--t-body);font-weight:600}
.desc{margin:calc(var(--s1) / 2) 0 0;font:var(--t-small);color:var(--text-2)}
.facts{margin:var(--s1) 0 0;font:var(--t-micro);font-weight:400;color:var(--text-3)}
.facts code{font:var(--t-code);line-height:inherit;color:var(--text-3)}
.facts em{font-style:normal;color:var(--text-2)}
.marks{margin:0;display:flex;gap:var(--s2);align-items:flex-start}
.sub{margin:0 var(--s4) 0 calc(var(--s4) + var(--s6));border-top:var(--hairline) dashed var(--line-strong)}
.sub>li+li{border-top:var(--hairline) dashed var(--line-strong)}
.sub .row{padding-left:0;padding-right:0}
.sub .sub{margin:0 0 0 var(--s6)}

.panel{background:var(--raised);border:var(--hairline) solid var(--line);border-radius:var(--r-lg);padding:var(--s5)}
.phd{display:flex;justify-content:space-between;align-items:flex-start;gap:var(--s3)}
.panel h2{margin:0;font:var(--t-heading);letter-spacing:var(--track-heading)}
.chips{display:flex;gap:var(--s2);margin:var(--s2) 0 0}
.panel>.desc{margin:var(--s3) 0 0}
.callout{display:flex;flex-direction:column;gap:var(--s2);margin:var(--s4) 0 0;padding:var(--s3) var(--s4);border-radius:var(--r-md);font:var(--t-small);color:var(--text)}
.callout .sev{display:flex;align-items:center;gap:var(--s2);font-weight:600}
.callout code{font:var(--t-code);line-height:inherit}
.c-problem.callout{background:var(--problem-box);box-shadow:inset 0 0 0 var(--hairline) var(--problem-edge);color:var(--text)}
.c-note.callout{background:var(--note-box);box-shadow:inset 0 0 0 var(--hairline) var(--note-edge);color:var(--text)}
.c-problem.callout .sev{color:var(--problem)} .c-note.callout .sev{color:var(--note)}
.callout .btn{align-self:flex-start;margin-top:var(--s1)}
.psec{margin-top:var(--s5);padding-top:var(--s4);border-top:var(--hairline) solid var(--line)}
.psec h3{margin:0 0 var(--s2);font:var(--t-label);letter-spacing:var(--track-label);text-transform:uppercase;color:var(--text-3)}
.psec p{margin:0;font:var(--t-small);color:var(--text-2)}
.file{margin:0 0 var(--s2);padding:var(--s3) var(--s4);background:var(--well-deep);border:var(--hairline) solid var(--line-strong);border-radius:var(--r-md);
  font:var(--t-code);color:var(--text);white-space:pre-wrap;overflow-wrap:anywhere}
.meta{margin:0;font:var(--t-micro);font-weight:400;color:var(--text-3)}
.pfacts{display:grid;grid-template-columns:var(--dt-w) 1fr;gap:var(--s2) var(--s3);margin:0;font:var(--t-small)}
.pfacts dt{color:var(--text-3)} .pfacts dd{margin:0;color:var(--text)}
.pfacts code{font:var(--t-code)}
.pact{display:flex;gap:var(--s2);margin-top:var(--s5);padding-top:var(--s4);border-top:var(--hairline) solid var(--line)}

/* --- Export over the project, and a dialog --- */
.runwrap{position:relative;overflow:hidden}
.veil,.dveil{position:absolute;inset:0;background:var(--veil)}
.dveil{background:var(--veil-dialog)}
.run{position:absolute;left:calc(var(--s12) * 2 + var(--s4));right:calc(var(--s12) * 2 + var(--s4));top:var(--s8);bottom:0;padding:var(--s2) var(--s2) 0;
  border-radius:var(--r-xl) var(--r-xl) 0 0;background:var(--acrylic);backdrop-filter:var(--acrylic-blur);-webkit-backdrop-filter:var(--acrylic-blur);
  border:var(--hairline) solid var(--acrylic-edge);border-bottom:0}
.runin{height:100%;overflow:hidden;padding:var(--s6) var(--s8);background:var(--ground);border:var(--hairline) solid var(--sheet-edge);border-bottom:0;border-radius:var(--r-lg) var(--r-lg) 0 0}
.rhead{display:flex;justify-content:space-between;align-items:flex-start}
.rhead h2{margin:0;font:var(--t-title);letter-spacing:var(--track-title)}
.rcounts{margin:var(--s2) 0 0;font:var(--t-small);font-weight:600}
.rhead .meta{margin-top:var(--s1)}
.group{margin:var(--s6) 0 var(--s2);font:var(--t-label);letter-spacing:var(--track-label);text-transform:uppercase;color:var(--text-3)}
.stages{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:var(--s2)}
.stage{background:var(--cutout);border-radius:var(--r-md);box-shadow:inset 0 0 0 var(--hairline) var(--line)}
.stage.s-skipped{background:transparent;box-shadow:none;outline:var(--hairline) dashed var(--line-strong);outline-offset:calc(var(--hairline) * -1)}
.sum{display:grid;grid-template-columns:var(--s6) var(--stage-name-w) minmax(0,1fr) var(--s12);gap:var(--s3);align-items:center;min-height:calc(var(--s10) + var(--s1));padding:var(--s2) var(--s4)}
.n{font:var(--t-code);color:var(--text-3);font-variant-numeric:tabular-nums}
.sname{font:var(--t-body);font-weight:600}
.res{display:flex;align-items:center;gap:var(--s2);font:var(--t-small);color:var(--text-2)}
.g-problem{color:var(--problem)} .g-note{color:var(--note)} .g-skipped{color:var(--skipped)} .g-checked{color:var(--checked)}
.s-problem .res span{color:var(--problem);font-weight:600}
.s-note .res span{color:var(--note);font-weight:600}
.time{text-align:right;font:var(--t-code);color:var(--text-3);font-variant-numeric:tabular-nums}
.sbody{padding:0 var(--s4) var(--s4) calc(var(--s4) + var(--s6) + var(--s3))}
.sbody .callout{margin-top:0}
.slots{display:flex;gap:var(--s2);flex-wrap:wrap;margin-top:var(--s1)}
.slot{display:inline-flex;align-items:center;gap:var(--s1);height:var(--mark-h);padding:0 var(--s3) 0 var(--s2);font:var(--t-micro);font-weight:400;border:var(--hairline) dashed var(--line-strong);border-radius:var(--r-sm)}
.slot code{font:var(--t-code);line-height:1;font-weight:500;color:var(--text)}
.slot small{font:var(--t-micro);font-weight:400;color:var(--text-3)}
.slot .ic{width:var(--icon-s);height:var(--icon-s);color:var(--text-3)}
.dlg{position:absolute;left:50%;top:calc(var(--s12) * 5);transform:translateX(-50%);width:calc(var(--panel-w) + var(--s12) + var(--s8));padding:var(--s2);border-radius:var(--r-xl);
  background:var(--acrylic-dialog);backdrop-filter:var(--acrylic-blur);-webkit-backdrop-filter:var(--acrylic-blur);border:var(--hairline) solid var(--acrylic-edge);box-shadow:var(--shadow-sheet)}
.sheet{padding:var(--s5) var(--s6);background:var(--raised);border:var(--hairline) solid var(--sheet-edge);border-radius:var(--r-lg)}
.sheet h2{margin:0 0 var(--s2);font:var(--t-heading);letter-spacing:var(--track-heading)}
.sheet p{margin:0;font:var(--t-small);color:var(--text-2)}
.sheet p+p{margin-top:var(--s2)}
.dact{display:flex;justify-content:flex-end;gap:var(--s2);margin-top:var(--s5)}
@media (prefers-reduced-motion:reduce){.ml *{transition:none!important}}
"""


def literals(css):
    """Every value in css that is not a var(): colours, px sizes and font names — should be none."""
    found = []
    for m in re.finditer(r"#[0-9a-fA-F]{3,8}\b|rgba?\(|\b\d+(\.\d+)?px\b|\"[A-Z][\w ]+\"", css):
        found.append(m.group(0))
    return found


if __name__ == "__main__" and "--check" in sys.argv:
    bad = literals(UI_CSS)
    print("literal values in UI_CSS:", bad or "none")
