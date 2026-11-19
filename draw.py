#!/usr/bin/env python3
"""Draw the news-image-20261118 entry: a one-day newspaper front page.

Layout (1024x1024, flat newspaper style, PIL only):
  masthead | lead headline | 4 illustrated panels | region key |
  46-story table (4 cols, short labels + source tags) |
  UTC timeline strip | footer with date-check note.
All 46 stories were reported on Wednesday 18 November 2026.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (248, 244, 233)
INK = (20, 20, 20)
MUTED = (90, 86, 76)
NAVY = (20, 38, 63)
RED = (179, 35, 27)
GOLD = (184, 134, 11)
RULE = (180, 172, 152)
PANEL_BG = (255, 255, 255)

REGION_COLORS = {
    "ASIA-PACIFIC": (29, 78, 216),
    "MIDDLE EAST": (185, 28, 28),
    "EUROPE": (15, 118, 110),
    "N. AMERICA": (124, 58, 237),
    "AFRICA": (180, 83, 9),
    "S. ASIA & OCEANIA": (3, 105, 161),
    "TECH & MARKETS": (77, 124, 15),
}

# (label, region, source) — every story reported on 18 Nov 2026.
STORIES = [
    ("Xi meets Putin in Shenzhen", "ASIA-PACIFIC", "AFP"),
    ("APEC summit opens", "ASIA-PACIFIC", "REUTERS"),
    ("QUAD unveils new plan", "ASIA-PACIFIC", "REUTERS"),
    ("Carney meets Trump", "ASIA-PACIFIC", "PMO CANADA"),
    ("Cyclone Akvan hits Odisha", "ASIA-PACIFIC", "IMD"),
    ("Dhoni retires from IPL", "ASIA-PACIFIC", "INDIAN MEDIA"),
    ("ASEAN terms for Myanmar", "ASIA-PACIFIC", "REUTERS"),
    ("Iran fires on Kuwait base", "MIDDLE EAST", "REUTERS"),
    ("Iran hits Bahrain", "MIDDLE EAST", "AL JAZEERA"),
    ("3rd US carrier in Gulf", "MIDDLE EAST", "REUTERS"),
    ("Aramco tower hit", "MIDDLE EAST", "REUTERS"),
    ("Eisenkot to form govt", "MIDDLE EAST", "ISRAELI MEDIA"),
    ("Kahana elected speaker", "MIDDLE EAST", "ISRAELI MEDIA"),
    ("Board faults both sides", "MIDDLE EAST", "AP"),
    ("Iran-US talks in Geneva", "MIDDLE EAST", "REUTERS"),
    ("Trump weighs Iran strike", "MIDDLE EAST", "US MEDIA"),
    ("Kerch Bridge collapses", "EUROPE", "UKRAINE MIL."),
    ("Biggest POW swap agreed", "EUROPE", "REUTERS"),
    ("EU: \u20ac45bn for Ukraine", "EUROPE", "EU"),
    ("France tests M51.3", "EUROPE", "FRENCH MOD"),
    ("French student protests", "EUROPE", "FRENCH MEDIA"),
    ("German book-prize row", "EUROPE", "GERMAN MEDIA"),
    ("NATO unveils comms plan", "EUROPE", "NATO"),
    ("Peltola wins; Senate 56\u201344", "N. AMERICA", "AP"),
    ("US loses measles-free status", "N. AMERICA", "PAHO"),
    ("JPMorgan bug hits accounts", "N. AMERICA", "JPMORGAN"),
    ("NYC travel ban in storm", "N. AMERICA", "NYC"),
    ("Jesse Jackson dies, 84", "N. AMERICA", "US MEDIA"),
    ("Thanksgiving travel: 81.5m", "N. AMERICA", "AAA"),
    ("Ebola passes 11,000 cases", "AFRICA", "WHO"),
    ("RSF strikes on El Obeid", "AFRICA", "PANA"),
    ("Chad closes Sudan border", "AFRICA", "CHAD GOVT"),
    ("Nigeria eyes UN rights seat", "AFRICA", "NIGERIA"),
    ("Morocco 5th in FIFA ranking", "AFRICA", "FIFA"),
    ("2,500 lost on sea routes", "AFRICA", "UNHCR"),
    ("Afghan quake kills 600+", "S. ASIA & OCEANIA", "AFGHAN AUTH."),
    ("Pakistan blast toll hits 16", "S. ASIA & OCEANIA", "PAK. MEDIA"),
    ("India: leave Iran now", "S. ASIA & OCEANIA", "INDIAN EMB."),
    ("Duckett 133 seals ODI win", "S. ASIA & OCEANIA", "ECB"),
    ("Zverev into Turin semis", "S. ASIA & OCEANIA", "ATP"),
    ("Nvidia rejects Huang", "TECH & MARKETS", "NVIDIA"),
    ("OpenAI launches GPT-6.2", "TECH & MARKETS", "OPENAI"),
    ("Oil nears $93 on Gulf fears", "TECH & MARKETS", "MARKETS"),
    ("COP31 opens in Turkey", "TECH & MARKETS", "UN"),
    ("Russia: hypersonics for subs", "TECH & MARKETS", "RUSSIA"),
    ("Gaza winter emergency", "TECH & MARKETS", "UN"),
]

TIMELINE = [
    ("05:50", "ECOWAS verdict"),
    ("06:42", "UNHCR appeal"),
    ("06:59", "RSF strikes reported"),
    ("09:30", "Morning brief"),
    ("13:52", "Duckett 133"),
    ("18:11", "FIBA field set"),
]


def font(name, size):
    base = "/usr/share/fonts/truetype/dejavu"
    paths = {
        "serif_b": f"{base}/DejaVuSerif-Bold.ttf",
        "serif": f"{base}/DejaVuSerif.ttf",
        "sans_b": f"{base}/DejaVuSans-Bold.ttf",
        "sans": f"{base}/DejaVuSans.ttf",
    }
    return ImageFont.truetype(paths[name], size)


def center(draw, cx, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)


def icon_summit(d, x, y):
    # three leader circles over a table line
    cols = [(29, 78, 216), (185, 28, 28), (245, 158, 11)]
    lets = ["US", "CN", "RU"]
    for i, (c, t) in enumerate(zip(cols, lets)):
        cx = x + 22 + i * 34
        d.ellipse([cx - 15, y + 8, cx + 15, y + 38], fill=c, outline=INK, width=2)
        f = font("sans_b", 11)
        tw = d.textlength(t, font=f)
        d.text((cx - tw / 2, y + 18), t, font=f, fill=(255, 255, 255))
    d.line([x + 4, y + 52, x + 104, y + 52], fill=INK, width=3)


def icon_gulf(d, x, y):
    # explosion starburst over a missile silhouette
    cx, cy = x + 54, y + 26
    pts = []
    import math
    for i in range(24):
        ang = math.pi * i / 12
        r = 26 if i % 2 == 0 else 12
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    d.polygon(pts, fill=(245, 158, 11), outline=(185, 28, 28))
    d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=(185, 28, 28))
    d.polygon([(x + 46, y + 52), (x + 50, y + 34), (x + 54, y + 52)], fill=(60, 60, 60))
    d.rectangle([x + 48, y + 50, x + 60, y + 62], fill=(60, 60, 60))


def icon_bridge(d, x, y):
    # arch bridge with a crack in the middle
    d.line([x + 6, y + 56, x + 102, y + 56], fill=INK, width=3)
    d.arc([x + 14, y + 6, x + 94, y + 62], 180, 360, fill=INK, width=3)
    d.line([x + 22, y + 56, x + 22, y + 26], fill=INK, width=3)
    d.line([x + 86, y + 56, x + 86, y + 26], fill=INK, width=3)
    d.line([x + 52, y + 30, x + 46, y + 40, x + 56, y + 48, x + 50, y + 56],
           fill=RED, width=3)
    d.line([x + 56, y + 56, x + 66, y + 62], fill=RED, width=3)


def icon_ballot(d, x, y):
    # ballot box with a check mark
    d.rounded_rectangle([x + 26, y + 22, x + 82, y + 62], radius=4,
                        outline=INK, width=3, fill=(255, 255, 255))
    d.rectangle([x + 40, y + 18, x + 68, y + 26], fill=INK)
    d.line([x + 34, y + 46, x + 46, y + 56, x + 74, y + 28],
           fill=(15, 118, 110), width=5)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 28  # side margin

    # ---- masthead ----
    d.rectangle([0, 0, W, 66], fill=NAVY)
    d.text((mx, 10), "THE WORLD IN ONE DAY", font=font("serif_b", 38),
           fill=(255, 255, 255))
    d.text((mx, 10), "THE WORLD IN ONE DAY", font=font("serif_b", 38),
           fill=(255, 255, 255))
    right = "WEDNESDAY 18 NOVEMBER 2026"
    w = d.textlength(right, font=font("sans_b", 19))
    d.text((W - mx - w, 10), right, font=font("sans_b", 19), fill=(255, 255, 255))
    sub = "46 STORIES  \u00b7  7 REGIONS  \u00b7  ALL DATE-CHECKED"
    w = d.textlength(sub, font=font("sans_b", 13))
    d.text((W - mx - w, 38), sub, font=font("sans_b", 13), fill=(232, 197, 90))

    # ---- lead headline ----
    d.text((mx, 76), "THE DAY'S BIGGEST STORY", font=font("sans_b", 14),
           fill=RED)
    d.text((mx, 94), "XI AND PUTIN MEET IN SHENZHEN",
           font=font("serif_b", 42), fill=INK)
    d.text((mx, 140),
           "on the eve of the first-ever Trump trilateral  \u00b7  APEC opens  \u00b7  Gulf on edge",
           font=font("sans", 17), fill=MUTED)
    d.line([mx, 164, W - mx, 164], fill=RULE, width=1)

    # ---- 4 illustrated panels ----
    panels = [
        ("THE SHENZHEN SUMMIT", "Xi\u2013Putin meet; Trump joins Thursday", icon_summit),
        ("GULF ON EDGE", "Iran fires on Kuwait & Bahrain", icon_gulf),
        ("KERCH BRIDGE HIT", "Road span collapses, day two", icon_bridge),
        ("SENATE FLIPS 56\u201344", "Peltola wins the Alaska seat", icon_ballot),
    ]
    pw = (W - 2 * mx - 3 * 12) // 4
    py, ph = 174, 148
    for i, (cap, sub2, icon) in enumerate(panels):
        x = mx + i * (pw + 12)
        d.rectangle([x, py, x + pw, py + ph], fill=PANEL_BG,
                    outline=RULE, width=1)
        d.rectangle([x, py, x + pw, py + 5], fill=RED)
        icon(d, x + (pw - 108) // 2, py + 12)
        center(d, x + pw / 2, py + 82, cap, font("sans_b", 15), INK)
        # sub-caption, wrapped to two lines max
        f = font("sans", 12)
        words = sub2.split()
        lines, cur = [], ""
        for wd in words:
            t = (cur + " " + wd).strip()
            if d.textlength(t, font=f) <= pw - 16:
                cur = t
            else:
                lines.append(cur)
                cur = wd
        lines.append(cur)
        for j, ln in enumerate(lines[:2]):
            center(d, x + pw / 2, py + 104 + j * 16, ln, f, MUTED)

    # ---- region key ----
    ky = 334
    items = list(REGION_COLORS.items())
    x = mx
    f = font("sans_b", 12)
    for name, col in items:
        d.rectangle([x, ky + 2, x + 10, ky + 12], fill=col)
        x += 14
        d.text((x, ky), name, font=f, fill=INK)
        x += d.textlength(name, font=f) + 18

    # ---- story table: 4 columns x 12 rows ----
    ty, by = 360, 926
    cols = 4
    cw = (W - 2 * mx - (cols - 1) * 16) // cols
    rows = 12
    rh = (by - ty) // rows
    lab_f = font("sans_b", 13)
    src_f = font("sans", 10)
    for idx, (label, region, src) in enumerate(STORIES):
        col_i = idx // rows
        row_i = idx % rows
        x = mx + col_i * (cw + 16)
        y = ty + row_i * rh
        col = REGION_COLORS[region]
        d.ellipse([x, y + 5, x + 8, y + 13], fill=col)
        d.text((x + 13, y), label, font=lab_f, fill=INK)
        d.text((x + 13, y + 19), f"{region} \u00b7 {src}", font=src_f,
               fill=MUTED)
        if row_i < rows - 1:
            d.line([x, y + rh - 9, x + cw, y + rh - 9], fill=(226, 220, 204),
                   width=1)

    # ---- UTC timeline ----
    d.text((mx, 940), "UTC TIMELINE", font=font("sans_b", 12), fill=RED)
    tl_x0, tl_x1 = mx + 152, W - mx
    d.line([tl_x0, 966, tl_x1, 966], fill=INK, width=2)
    for i, (t, ev) in enumerate(TIMELINE):
        cx = tl_x0 + i * (tl_x1 - tl_x0) // (len(TIMELINE) - 1)
        d.ellipse([cx - 5, 961, cx + 5, 971], fill=RED, outline=INK, width=1)
        tf = font("sans_b", 11)
        tw = d.textlength(t, font=tf)
        d.text((cx - tw / 2, 940), t, font=tf, fill=INK)
        ef = font("sans", 10)
        ew = d.textlength(ev, font=ef)
        ex = min(max(cx - ew / 2, tl_x0), tl_x1 - ew)
        d.text((ex, 974), ev, font=ef, fill=MUTED)

    # ---- footer ----
    d.line([mx, 996, W - mx, 996], fill=RULE, width=1)
    center(d, W / 2, 1004,
           "Every story above was reported on Wednesday 18 November 2026  \u00b7  "
           "Sources: AFP \u00b7 Reuters \u00b7 AP \u00b7 Al Jazeera \u00b7 WHO \u00b7 FIFA \u00b7 NATO \u00b7 IMD",
           font("sans", 11), MUTED)

    img.save(OUT, optimize=True)
    print("saved", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
