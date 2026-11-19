# Offline build step: draws the 19 Nov 2026 news card with Pillow. main.py just copies the result.
from PIL import Image, ImageDraw, ImageFont
W = 1024
B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
f = lambda p, s: ImageFont.truetype(p, s)
img = Image.new("RGB", (W, W), (14, 20, 34))
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 120], fill=(180, 30, 40))
d.text((32, 14), "WORLD NEWS", font=f(B, 52), fill="white")
d.text((32, 76), "THURSDAY 19 NOVEMBER 2026", font=f(B, 34), fill=(255, 225, 225))
stories = [
 ("1", (200, 60, 60), "TRUMP, XI, PUTIN MEET IN SHENZHEN",
  ["First-ever 3-way summit at APEC.", "'Declaration Towards Peace': UN reform,", "nuclear-risk talks, more refined fuel,", "limits on the ICC. No Ukraine breakthrough."]),
 ("2", (60, 120, 200), "WORLD COURT: MYANMAR COMMITTED GENOCIDE",
  ["ICJ rules against Myanmar over the 2017", "Rohingya crackdown. First time the court", "has held a state responsible for genocide."]),
 ("3", (220, 130, 40), "WARS: UKRAINE, IRAN, GAZA",
  ["Putin vows response to Kerch Bridge strikes;", "Europe's Berlin summit rejects 'Yalta format'.", "Houthi missile hits Riyadh's PIF Tower.", "Israeli tanks push past Gaza 'yellow line'."]),
 ("4", (60, 160, 110), "MARKETS: ANTHROPIC IPO, WALL ST FALLS",
  ["Anthropic debuts on Nasdaq: IPO $83,", "opened $111.50, record offering.", "S&P 500 -2%, 6th straight loss; Dow -2.2%."]),
 ("5", (140, 90, 190), "ALSO TODAY",
  ["US and Venezuela restore military ties.", "Cyclone Akvan nears India's Odisha coast;", "100,000+ evacuated.", "Denmark ratifies Greenland deal with US."]),
]
y = 140
hs = [172, 140, 172, 140, 172]
# compact layout
heights = [150, 125, 150, 125, 150]
for (n, col, head, lines), h in zip(stories, heights):
    d.rounded_rectangle([24, y, W - 24, y + h - 8], 14, fill=(28, 38, 60))
    d.ellipse([38, y + 12, 86, y + 60], fill=col)
    d.text((53, y + 17), n, font=f(B, 30), fill="white")
    d.text((100, y + 14), head, font=f(B, 25), fill=(255, 255, 255))
    for i, ln in enumerate(lines):
        d.text((100, y + 50 + i * 24), ln, font=f(R, 20), fill=(205, 215, 235))
    y += h
d.text((24, 1024 - 30), "Sources: AP, Reuters, BBC, NPR, Euronews, The Hindu. Events of 19 Nov 2026.", font=f(R, 15), fill=(150, 160, 180))
img.save("entry.png", optimize=True)
