import sys
from bs4 import BeautifulSoup

if len(sys.argv) != 3:
    print("Usage: python add_gallery_image.py gallery/image_name.jpg \"Your Caption Here\"")
    sys.exit(1)

NEW_IMAGE   = sys.argv[1]
NEW_CAPTION = sys.argv[2]

with open("gallery.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

# ── 1. Insert new slide first ──
new_slide = BeautifulSoup(f"""
<div class="carousel-slide active" data-index="0">
  <img src="{NEW_IMAGE}" alt="{NEW_CAPTION}" />
  <div class="slide-caption">
    <p class="text-white text-sm font-medium drop-shadow">{NEW_CAPTION}</p>
  </div>
</div>""", "html.parser")

slides = soup.select(".carousel-slide")
for i, slide in enumerate(slides):
    slide["data-index"] = str(i + 1)
    if "active" in slide.get("class", []):
        slide["class"].remove("active")

slides[0].insert_before(new_slide)

# ── 2. Insert new dot first ──
new_dot = BeautifulSoup(
    f'<button class="dot active" data-dot="0" aria-label="Go to slide 1"></button>',
    "html.parser")

dots = soup.select(".dot")
for i, dot in enumerate(dots):
    dot["data-dot"] = str(i + 1)
    if "active" in dot.get("class", []):
        dot["class"].remove("active")

dots[0].insert_before(new_dot)

# ── 3. Insert new thumbnail first ──
new_thumb = BeautifulSoup(f"""
<button class="thumb-btn active" data-thumb="0" aria-label="Thumbnail 1">
  <img src="{NEW_IMAGE}" alt="{NEW_CAPTION}" />
</button>""", "html.parser")

thumbs = soup.select(".thumb-btn")
for i, thumb in enumerate(thumbs):
    thumb["data-thumb"] = str(i + 1)
    if "active" in thumb.get("class", []):
        thumb["class"].remove("active")

thumbs[0].insert_before(new_thumb)

# ── 4. Save ──
with open("gallery.html", "w") as f:
    f.write(str(soup))

print(f"Done! Added '{NEW_CAPTION}' ({NEW_IMAGE}) as the first slide in gallery.html")