#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

def create_entry_image():
    base_path = "base.png"
    output_path = "entry.png"
    
    if not os.path.exists(base_path):
        raise FileNotFoundError(f"{base_path} not found")
        
    img = Image.open(base_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    
    width, height = img.size
    
    # Target center x = 62% of width
    cx = int(width * 0.62)
    # Headline baseline y = 12% of height
    cy = int(height * 0.12)
    
    # Fonts
    headline_font_size = 42
    subline_font_size = 20
    
    headline_font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    if not os.path.exists(headline_font_path):
        headline_font_path = "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf"
        
    headline_font = ImageFont.truetype(headline_font_path, headline_font_size)
    subline_font = ImageFont.truetype(headline_font_path, subline_font_size)
    
    headline_text = "ONE LIGHT-DAY FROM HOME"
    subline_text = "Voyager 1 - 22 November 2026"
    
    # Colors
    gold_color = (245, 200, 107) # #f5c86b
    white_color = (235, 240, 245)
    
    # Measure headline width to center it around cx
    bbox = draw.textbbox((0, 0), headline_text, font=headline_font)
    t_width = bbox[2] - bbox[0]
    t_height = bbox[3] - bbox[1]
    
    hx = cx - (t_width // 2)
    hy = cy - t_height
    
    # Draw shadow for headline
    shadow_offset = 2
    draw.text((hx + shadow_offset, hy + shadow_offset), headline_text, font=headline_font, fill=(10, 10, 15))
    draw.text((hx, hy), headline_text, font=headline_font, fill=gold_color)
    
    # Subline below headline with letterspacing
    subline_chars = list(subline_text)
    letter_spacing = 3
    char_widths = [draw.textbbox((0, 0), c, font=subline_font)[2] - draw.textbbox((0, 0), c, font=subline_font)[0] for c in subline_chars]
    total_sub_width = sum(char_widths) + letter_spacing * (len(subline_chars) - 1)
    
    sub_x = cx - (total_sub_width // 2)
    sub_y = hy + t_height + 14
    
    # Draw subline shadow & text with letterspacing
    curr_x = sub_x
    for i, c in enumerate(subline_chars):
        draw.text((curr_x + 1, sub_y + 1), c, font=subline_font, fill=(10, 10, 15))
        draw.text((curr_x, sub_y), c, font=subline_font, fill=white_color)
        curr_x += char_widths[i] + letter_spacing
        
    img.save(output_path, "PNG", optimize=True)
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    create_entry_image()
