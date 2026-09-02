import io, os, re, sys, base64
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "research-page.tpl.html")
OUT = os.path.join(HERE, "_research-page.build.html")

F = "research/2-flows"
L = "research/1-landscape/screens"
B = "research/4-benchmark"

IMAGES = {
    # stage 1
    "c-tessl":     L + "/hard/tessl/skill-detail-scored.png",
    "c-smithery":  L + "/hard/smithery/registry-home.png",
    "c-backstage": L + "/soft/backstage/catalog-table.png",
    # flows
    "f01a": F + "/01-item-detail-and-trust/tessl-skill-evals-tab.png",
    "f01b": F + "/01-item-detail-and-trust/smithery-server-github-config.png",
    "f02a": F + "/02-library-browse-filter-search/linear-command-palette-default.jpg",
    "f02b": F + "/02-library-browse-filter-search/linear-filter-typeahead-breadcrumbs.jpg",
    "f02c": F + "/02-library-browse-filter-search/linear-filtered-to-zero-hidden-count.jpg",
    "f03a": F + "/03-relations-without-canvas/backstage-graph-depth-1.png",
    "f03b": F + "/03-relations-without-canvas/backstage-graph-depth-3.png",
    "f03c": F + "/03-relations-without-canvas/github-dependents-blast-radius.png",
    "f04a": F + "/04-validation-check-results/vercel-deployment-stages.jpg",
    "f04b": F + "/04-validation-check-results/port-scorecard-rule-expanded.png",
    "f04c": F + "/04-validation-check-results/github-actions-run-failed-annotations.png",
    "f05a": F + "/05-linked-vs-detached/figma-context-menu-clean.png",
    "f05b": F + "/05-linked-vs-detached/figma-context-menu-overridden-reset.png",
    "f05c": F + "/05-linked-vs-detached/figma-library-updates-instance-counts.png",
    "f06a": F + "/06-export-and-target-adaptation/backstage-scaffolder-template-form.png",
    "f07a": F + "/07-env-and-secrets/vercel-add-env-variable-drawer.jpg",
    "f07b": F + "/07-env-and-secrets/vercel-env-vars-empty-state.jpg",
    "f08a": F + "/08-empty-state-and-cold-start/linear-first-run-seeded-issues.jpg",
    "f08b": F + "/08-empty-state-and-cold-start/linear-projects-empty-state.jpg",
    "f09a": F + "/09-duplicate-and-fork/github-create-fork-form.jpg",
    "f09b": F + "/09-duplicate-and-fork/notion-page-menu-duplicate.jpg",
    "f10a": F + "/10-dark-design-language/linear-issues-list-dark.jpg",
    "f10b": F + "/10-dark-design-language/linear-command-palette-dark-detail.png",
    "f11a": F + "/11-copy-and-error-language/github-pr-bot-failing-test-suites.png",
    "f11b": F + "/11-copy-and-error-language/stripe-error-codes.png",
    "f12a": F + "/12-visibility-and-portfolio/github-danger-zone-visibility.jpg",
    "f12b": F + "/12-visibility-and-portfolio/notion-publish-to-web.jpg",
    # benchmark
    "b-trust":    B + "/vscode-workspace-trust.png",
    "b-problems": B + "/vscode-problems-filtered-zero.png",
    "b-figma":    B + "/figma-export-empty-selection.png",
    "b-obsidian": B + "/obsidian-quick-switcher-no-match.png",
}

MAXW = 1360
QUALITY = 86


def encode(path):
    full = os.path.join(ROOT, path.replace("/", os.sep))
    if not os.path.exists(full):
        raise SystemExit("MISSING IMAGE: " + path)
    im = Image.open(full)
    if im.mode not in ("RGB", "L"):
        im = im.convert("RGB")
    if im.width > MAXW:
        h = round(im.height * MAXW / im.width)
        im = im.resize((MAXW, h), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=QUALITY, optimize=True, progressive=True)
    raw = buf.getvalue()
    return "data:image/jpeg;base64," + base64.b64encode(raw).decode("ascii"), len(raw)


def main():
    if not os.path.exists(TPL):
        raise SystemExit("template not found: " + TPL)
    html = io.open(TPL, encoding="utf-8").read()

    total = 0
    encoded = {}
    for key, path in IMAGES.items():
        uri, n = encode(path)
        encoded[key] = uri
        total += n

    used = set(re.findall(r"\{\{IMG:([a-z0-9\-]+)\}\}", html))
    unknown = used - set(encoded)
    if unknown:
        raise SystemExit("template references unknown images: " + ", ".join(sorted(unknown)))
    unused = set(encoded) - used
    if unused:
        print("NOTE: encoded but unused: " + ", ".join(sorted(unused)))

    for key, uri in encoded.items():
        html = html.replace("{{IMG:%s}}" % key, uri)

    leftover = re.findall(r"\{\{[^}]+\}\}", html)
    if leftover:
        raise SystemExit("unsubstituted placeholders: " + ", ".join(sorted(set(leftover))))

    io.open(OUT, "w", encoding="utf-8", newline="\n").write(html)
    size = os.path.getsize(OUT)
    print("images: %d, jpeg bytes: %.2f MB" % (len(encoded), total / 1048576.0))
    print("page:   %.2f MB  -> %s" % (size / 1048576.0, OUT))
    if size > 15 * 1048576:
        print("WARNING: approaching the 16MB artifact limit")


if __name__ == "__main__":
    main()
