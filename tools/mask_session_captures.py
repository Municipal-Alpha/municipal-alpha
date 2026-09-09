"""Mask town and staff names in the session captures.

Boxes come from macOS Vision OCR (scratchpad/ocr.swift), so the coordinates are
measured from the image rather than eyeballed. Every target is a regex over the
recognised token, and the script asserts the expected hit count before it writes
anything -- an OCR miss must fail loudly, not silently ship an unmasked name.
"""
import re, sys
from PIL import Image, ImageDraw

# The bar colour is picked from the image, not hardcoded, so the same tool
# works on a light-mode and a dark-mode capture of the same session. On the
# dark captures this lands on the value the earlier hand-made redactions used.
GREY_ON_DARK  = (90, 90, 92)
GREY_ON_LIGHT = (170, 168, 164)

def bar_colour(im):
    w, h = im.size
    corners = [im.getpixel(c) for c in ((4, 4), (w - 5, 4), (4, h - 5), (w - 5, h - 5))]
    lum = sum(0.2126 * r + 0.7152 * g + 0.0722 * b for r, g, b in corners) / 4
    return GREY_ON_DARK if lum < 128 else GREY_ON_LIGHT
PAD_X, PAD_Y = 3, 2
ROW_TOL = 10      # px: same text line
GAP_MAX = 26      # px: merge neighbouring tokens into one bar

def boxes(tsv):
    out = []
    for line in open(tsv, encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) != 5:
            continue
        t, x, y, w, h = parts
        out.append((t, int(x), int(y), int(w), int(h)))
    return out

def merge(hits):
    # Sort into row BANDS first, then by x within the band. Sorting on raw y
    # interleaves tokens whose baselines differ by a pixel ("Duggan" at y=561
    # sorting before "Greg" at y=562), which silently defeats the adjacency
    # merge and leaves two bars where one belongs.
    hits = sorted(hits, key=lambda b: (round(b[2] / ROW_TOL), b[1]))
    merged = []
    for b in hits:
        if merged:
            p = merged[-1]
            same_row = abs(b[2] - p[2]) <= ROW_TOL
            gap = b[1] - (p[1] + p[3])
            if same_row and 0 <= gap <= GAP_MAX:
                x0 = min(p[1], b[1]); y0 = min(p[2], b[2])
                x1 = max(p[1] + p[3], b[1] + b[3]); y1 = max(p[2] + p[4], b[2] + b[4])
                merged[-1] = (p[0] + " " + b[0], x0, y0, x1 - x0, y1 - y0)
                continue
        merged.append(b)
    return merged

def run(src, dst, tsv, pattern, expect):
    rx = re.compile(pattern)
    hits = [b for b in boxes(tsv) if rx.match(b[0])]
    if len(hits) != expect:
        sys.exit(f"FAIL {src}: matched {len(hits)} token(s), expected {expect}: "
                 f"{[h[0] for h in hits]}")
    bars = merge(hits)
    im = Image.open(src).convert("RGB")
    grey = bar_colour(im)
    d = ImageDraw.Draw(im)
    for _, x, y, w, h in bars:
        d.rounded_rectangle(
            [x - PAD_X, y - PAD_Y, x + w + PAD_X, y + h + PAD_Y],
            radius=3, fill=grey)
    im.save(dst)
    print(f"{dst}: {len(hits)} token(s) -> {len(bars)} bar(s)  {im.size}  bar={grey}")

D = "/Users/christianmilz/Desktop"
S = "/private/tmp/claude-501/-Users-christianmilz-Projects-muni-scraper/df2085f3-b3b3-42c8-821e-b115162a864f/scratchpad"
IMG = "/private/tmp/claude-501/-Users-christianmilz-Projects-muni-scraper/df2085f3-b3b3-42c8-821e-b115162a864f/scratchpad/site/content/images"

run(f"{D}/Screenshot 2026-09-09 at 10.23.36.png", f"{IMG}/demo-ask.png",
    f"{S}/dk_find.tsv", r"^(Essex|Stratham|Greenfield|Pittsfield),?$", 4)

run(f"{D}/Screenshot 2026-09-09 at 10.24.02.png", f"{IMG}/demo-signals.png",
    f"{S}/dk_check.tsv", r"^(Essex|Junction),?$", 3)

run(f"{D}/Screenshot 2026-09-09 at 10.24.20.png", f"{IMG}/demo-crm.png",
    f"{S}/dk_crm.tsv",
    r"^(Kent|Johnson|Brittany|McGregor|Karen|Adams|Greg|Duggan|Dan|Roy|Aaron|Martin|Charles|Cole),?$", 14)
