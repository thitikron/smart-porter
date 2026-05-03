from PIL import Image, ImageDraw, ImageFont
import os

sizes = [72, 96, 128, 144, 152, 192, 384, 512]
os.makedirs('icons', exist_ok=True)

for size in sizes:
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background circle
    margin = int(size * 0.05)
    draw.ellipse([margin, margin, size-margin, size-margin], fill='#0077B6')
    
    # Inner white circle accent
    inner = int(size * 0.1)
    draw.ellipse([inner, inner, size-inner, size-inner], fill='#0096C7')
    
    # Hospital cross
    cx, cy = size // 2, size // 2
    bar_w = int(size * 0.15)
    bar_h = int(size * 0.38)
    
    # Vertical bar
    draw.rectangle([cx - bar_w, cy - bar_h, cx + bar_w, cy + bar_h], fill='white')
    # Horizontal bar
    draw.rectangle([cx - bar_h, cy - bar_w, cx + bar_h, cy + bar_w], fill='white')
    
    # Small wheelchair symbol below cross
    dot_r = int(size * 0.04)
    dot_y = int(size * 0.72)
    draw.ellipse([cx - dot_r, dot_y - dot_r, cx + dot_r, dot_y + dot_r], fill='white')
    
    img.save(f'icons/icon-{size}.png')
    print(f'Generated icon-{size}.png')

print('All icons generated!')
