"""Generate LinkedIn banner for ServiMariae.

LinkedIn personal banner: 1584 x 396 px.
Brand: navy #1d3a8a, cream #fbf7f0, gold #c9a227.
Profile photo overlays bottom-left ~64-216 px horizontally — keep text right of x=300
or vertically above y=300.

ponytail: single solid-color composition. Add subtle ornament when a real cross
or image asset is decided.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1584, 396
NAVY = (29, 58, 138)
CREAM = (251, 247, 240)
GOLD = (201, 162, 39)

TITLE = "ServiMariae"
TAG = "Ad Iesum per Mariam"

img = Image.new("RGB", (W, H), NAVY)
draw = ImageDraw.Draw(img)

title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 120)
tag_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 42)
small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 26)


def center_text(text, font, y, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((W - w) / 2 - bbox[0], y), text, font=font, fill=fill)


title_y = 110
center_text(TITLE, title_font, title_y, CREAM)

# gold divider
div_y = title_y + 145
draw.line([(W / 2 - 80, div_y), (W / 2 + 80, div_y)], fill=GOLD, width=2)

tag_y = div_y + 28
center_text(TAG, tag_font, tag_y, CREAM)

# corner tagline — kept off bottom-left profile-photo zone
hint = "Catholic reflections"
hb = draw.textbbox((0, 0), hint, font=small_font)
hw = hb[2] - hb[0]
draw.text(((W - hw) / 2 - hb[0], H - 50), hint, font=small_font, fill=CREAM)

img.save("/root/repos/servi-mariae/assets/banner-linkedin.png", optimize=True)
print("ok")
