import io, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "_research-page.build.html")
DST = os.path.join(os.path.dirname(HERE), "research", "research.html")

s = io.open(SRC, encoding="utf-8").read()

# The artifact host supplies <!doctype>, <head> and a small reset at publish time.
# A standalone file has to carry all of it itself.
marker = "</style>"
i = s.index(marker) + len(marker)
head_content = s[:i].strip()
body_content = s[i:].strip()

RESET = """
<style>
/* Baseline the artifact host normally supplies. */
html{color-scheme:light dark}
body{margin:0}
img{max-width:100%}
[hidden]{display:none!important}
</style>
""".strip()

doc = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Five stages of research for AI Stack Builder: the competitor matrix, twelve captured flows, what actually hurts, a fifteen-cell benchmark, the chosen interaction shape, and the nine gaps still to test.">
%s
%s
</head>
<body>
%s
</body>
</html>
""" % (RESET, head_content, body_content)

io.open(DST, "w", encoding="utf-8", newline="\n").write(doc)

size = os.path.getsize(DST)
print("wrote %s  (%.2f MB)" % (DST, size / 1048576.0))

# sanity checks
check = io.open(DST, encoding="utf-8").read()
for needle in ("<!doctype html>", 'charset="utf-8"', "<title>AI Stack Builder Research</title>",
               'class="shell"', "</body>", "</html>"):
    assert needle in check, "MISSING: " + needle
assert check.count("<body>") == 1 and check.count("</html>") == 1
assert "data:image/jpeg;base64," in check
print("images embedded: %d" % check.count("data:image/jpeg;base64,"))
print("structure ok")
