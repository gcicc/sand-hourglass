#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate hourglass icons for Sand Hourglass PWA."""

import sys
import io

# Force UTF-8 output on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Installing Pillow...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'Pillow'])
    from PIL import Image, ImageDraw

def generate_icon(size):
    """Generate hourglass icon at given size."""
    # Create image with dark background
    img = Image.new('RGBA', (size, size), color='#0d1117')
    draw = ImageDraw.Draw(img)

    # Scale for the given size
    margin = int(size * 0.1)
    usable = size - margin * 2

    # Hourglass geometry
    top_left = (margin + int(usable * 0.1), margin + int(usable * 0.05))
    top_right = (margin + int(usable * 0.9), margin + int(usable * 0.05))
    neck = (margin + int(usable * 0.5), margin + int(usable * 0.45))

    bottom_left = (margin + int(usable * 0.1), margin + int(usable * 0.95))
    bottom_right = (margin + int(usable * 0.9), margin + int(usable * 0.95))
    neck_bottom = (margin + int(usable * 0.5), margin + int(usable * 0.55))

    # Draw hourglass outline in accent color
    outline_color = '#c4a882'
    outline_width = max(1, size // 80)

    # Top chamber
    draw.polygon([top_left, top_right, neck], outline=outline_color, width=outline_width)

    # Bottom chamber
    draw.polygon([bottom_left, bottom_right, neck_bottom], outline=outline_color, width=outline_width)

    # Neck circle (opening)
    neck_radius = int(usable * 0.04)
    draw.ellipse(
        [neck[0] - neck_radius, margin + int(usable * 0.45) - neck_radius,
         neck[0] + neck_radius, margin + int(usable * 0.45) + neck_radius],
        outline=outline_color,
        width=outline_width
    )

    # Draw sand (simple rectangles in top chamber for icon visibility)
    sand_color = '#c4a882'
    sand_left = top_left[0] + int(usable * 0.05)
    sand_right = top_right[0] - int(usable * 0.05)
    sand_top = top_left[1] + int(usable * 0.1)
    sand_height = int(usable * 0.25)

    draw.rectangle(
        [sand_left, sand_top, sand_right, sand_top + sand_height],
        fill=sand_color
    )

    return img

# Generate icons
for size in [192, 512]:
    print(f"Generating {size}x{size} icon...")
    img = generate_icon(size)
    img.save(f'icon-{size}.png')
    print(f"  Created icon-{size}.png")

print("\nDone! Icons ready for PWA deployment.")
