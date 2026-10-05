"""Extract every line of interface text from the wireframe pages.

Lesson 05, step 1. Reads 04-wireframes/pages/*.html (not the viewer, not the prototypes, which are
generated from these pages) and writes one row per line of text: page, zone, line, type, and the
user-content flag. Run from the repo root:

    python tools/extract_copy.py > scratch.tsv          # raw rows, one per page occurrence

The table in 05-tone-of-voice/microcopy.md is built from these rows by build_microcopy.py.
"""
import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "04-wireframes" / "pages"

VOID = {"meta", "link", "input", "br", "img", "hr", "source", "col", "wbr"}
INLINE = {"a", "span", "code", "strong", "em", "b", "i", "kbd", "small", "abbr", "time", "mark",
          "button", "label", "select", "option", "input", "sup", "sub", "q", "s", "u"}
SKIP = {"script", "style", "head", "template"}
CONTROLS = {"select", "input", "textarea"}
SPLIT_CLS = {"tag", "tag-state", "mark", "severity"}  # badges that sit inside a heading or a line


class Node:
    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.parent, self.children = tag, dict(attrs), parent, []

    @property
    def cls(self):
        return self.attrs.get("class", "").split()

    def ancestors(self):
        n = self.parent
        while n is not None:
            yield n
            n = n.parent


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", {}, None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def is_button(n):
    return isinstance(n, Node) and (
        n.tag == "button" or "button" in n.cls or "link-button" in n.cls
        or (n.tag == "input" and n.attrs.get("type") in ("submit", "button")))


def own_text(n):
    return any(isinstance(c, str) and c.strip() for c in n.children)


def text_of(n, split_out):
    """Text of n, inline children folded in, code shown in backticks. Children that are emitted on
    their own rows (buttons inside prose, controls, nested blocks) are left out and listed."""
    out = []
    for c in n.children:
        if isinstance(c, str):
            out.append(c)
        elif c.tag in SKIP or c.attrs.get("aria-hidden") == "true" and not text_any(c):
            continue
        elif c.tag in CONTROLS or is_button(c) or c.tag not in INLINE                 or set(c.cls) & SPLIT_CLS or (c.tag == "a" and (n.tag == "label" or "field-label" in n.cls)):
            split_out.append(c)
        elif c.tag == "code":
            out.append("`" + text_of(c, []) + "`")
        else:
            out.append(text_of(c, split_out))
    return "".join(out)


def text_any(n):
    return any((isinstance(c, str) and c.strip()) or (isinstance(c, Node) and text_any(c))
               for c in n.children)


def clean(s):
    return re.sub(r"\s+", " ", s).strip()


def zone(n):
    """The innermost named region the node sits in, plus the landmark above it."""
    names = []
    for a in [n] + list(n.ancestors()):
        if not isinstance(a, Node):
            continue
        c = a.cls
        label = a.attrs.get("aria-label")
        z = None
        if a.tag == "header" and "app-header" in c: z = "App header"
        elif a.tag == "nav" and "app-nav" in c: z = "Global nav"
        elif "run-bar" in c: z = "Run bar"
        elif "shared-header" in c: z = "Shared header"
        elif "library-sidebar" in c: z = "Library panel"
        elif a.tag == "dialog":
            kind = "Modal" if "modal" in c else "Sheet" if "sheet" in c else "Popover" if "popover" in c else "Dialog"
            h = first_heading(a)
            z = f"{kind}{': ' + h if h else ''}"
        elif "drawer" in c: z = "Side panel" + (": " + first_heading(a) if first_heading(a) else "")
        elif "state-block" in c: z = "State block"
        elif "export-stage" in c: z = "Export stage"
        elif "summary" in c and a.tag == "section": z = "Verdict"
        elif "stage-group" in c: z = "Stages: " + (first_heading(a) or "")
        elif "page-head" in c: z = "Page head"
        elif "door" in c: z = "Door"
        elif "find" in c or "find-zone" in c: z = "Find"
        elif a.tag == "form": z = "Form"
        elif "card" in c: z = "Project card"
        elif "set-item" in c: z = "Set row"
        elif a.tag == "article" and "row" in c: z = "Row"
        elif "callout" in c: z = "Finding"
        elif a.tag in ("section", "aside", "nav") and label: z = label
        elif a.tag == "main": z = "Main"
        if z and z not in names:
            names.append(z)
    names = names[:2]
    return " › ".join(reversed(names)) if names else "Page"


def first_heading(n):
    for c in n.children:
        if isinstance(c, Node):
            if c.tag in ("h1", "h2", "h3"):
                return clean(text_of(c, []))
            h = first_heading(c)
            if h:
                return h
    return None


def kind_of(n, text):
    c, t = n.cls, n.tag
    anc = [a.tag for a in n.ancestors()]
    anc_cls = {x for a in n.ancestors() for x in a.cls}
    if t == "h1" or ("title" in c and "run-bar" in anc_cls): return "title"
    if t in ("h2", "h3", "h4"):
        return "item name" if "set-item" in anc_cls or "row" in anc_cls or "card" in anc_cls else "heading"
    if is_button(n): return "button"
    if t == "option": return "option"
    if t == "label" and any(isinstance(x, Node) and x.attrs.get("type") in ("checkbox", "radio")
                            for x in n.children):
        return "option"
    if t == "span" and n.parent.tag == "label":
        first = next(x for x in n.parent.children if isinstance(x, Node))
        return "field label" if first is n else "field hint"
    if t == "label" or "field-label" in c or t == "legend" or t == "dt": return "field label"
    if "hint" in c: return "field hint"
    if t == "a" and n.parent.tag in ("h2", "h3") and anc_cls & {"row", "set-item", "card"}: return "item name"
    if "state-line" in c: return "panel row line"
    if t == "a": return "nav" if "nav" in anc or "tabs" in anc_cls or "scope" in anc_cls else "link"
    if "severity" in c or "mark" in c: return "severity"
    if "tag-state" in c: return "state badge"
    if "tag" in c:
        return "kind badge" if text in ("skill", "agent", "prompt", "mcp", "script", "app") else "state badge"
    if t == "pre": return "generated file"
    if "name" in c and "summary" in anc: return "stage name"
    if "result" in c: return "stage result"
    if "time" in c or t == "time": return "duration"
    if "description" in c: return "description"
    if "state-block" in anc_cls or "callout" in anc_cls or "summary" in anc_cls or n.attrs.get("role") == "alert" \
            or "export-stage" in anc_cls or "state-line" in c or "waiting" in c:
        return "state message"
    if "meta" in c or "meta" in anc_cls or "facts" in anc_cls or "usage" in anc_cls: return "fact"
    if t == "summary": return "disclosure"
    return "body"


def walk(n, rows, page):
    if not isinstance(n, Node) or n.tag in SKIP:
        return
    if n.tag == "title":
        return
    for attr, typ in (("placeholder", "placeholder"), ("aria-label", "a11y label"),
                      ("title", "tooltip"), ("alt", "alt text"), ("value", "value")):
        v = n.attrs.get(attr)
        if v and not (attr == "value" and n.tag != "input"):
            if attr == "value" and n.attrs.get("type") in ("hidden", "checkbox", "radio"):
                continue
            rows.append((page, zone(n), clean(v), typ, n))
    if n.tag in CONTROLS and n.tag != "select":
        return
    if own_text(n) or n.tag in ("option",) or (is_button(n) and text_any(n)) or n.tag == "pre":
        split = []
        txt = clean(text_of(n, split)) if n.tag != "pre" else text_of(n, []).strip("\n")
        if txt:
            rows.append((page, zone(n), txt, kind_of(n, txt), n))
        for c in split:
            walk(c, rows, page)
        return
    for c in n.children:
        walk(c, rows, page)


def is_user(n, kind, text):
    """User content: what the person wrote or named, not what the product says."""
    if kind in ("item name", "description"):
        return True
    anc_cls = {x for a in n.ancestors() for x in a.cls}
    if "account" in anc_cls and kind == "body":
        return True
    if re.fullmatch(r"(`[^`]*`[\s,·/@+]*)+", text):
        return True
    return False


def rows():
    out = []
    for p in sorted(PAGES.glob("*.html")):
        if p.name == "wireframes.html":
            continue
        t = Tree()
        t.feed(p.read_text(encoding="utf-8"))
        body = next(c for c in t.root.children if isinstance(c, Node) and c.tag == "html")
        rs = []
        walk(body, rs, p.stem)
        for page, z, text, kind, node in rs:
            out.append((page, z, text, kind, "user" if is_user(node, kind, text) else ""))
    return out


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for r in rows():
        print("\t".join(x.replace("\t", " ").replace("\n", "⏎") for x in r))
