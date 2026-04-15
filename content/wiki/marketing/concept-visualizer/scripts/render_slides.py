#!/usr/bin/env python3
"""
Render HTML slide files → PDF → JPG images → PPTX
Usage: python3 render_slides.py slide1.html [slide2.html ...] -o output.pptx
"""
import argparse
import os
import subprocess
import sys
import tempfile
from io import BytesIO

from PIL import Image
from pptx import Presentation
from pptx.util import Inches


def html_to_jpg(html_path: str, output_jpg: str, width: int = 1280, height: int = 720) -> bool:
    """Convert HTML to JPG via WeasyPrint + pdftoppm."""
    try:
        import weasyprint
    except ImportError:
        print("Installing weasyprint...", flush=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "weasyprint", "--break-system-packages"], check=True)
        import weasyprint

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_pdf:
        tmp_pdf_path = tmp_pdf.name

    try:
        html = weasyprint.HTML(filename=os.path.abspath(html_path))
        html.write_pdf(tmp_pdf_path)

        # pdftoppm: PDF → JPEG at 150 dpi (produces ~1587×893 for A4, but our page is sized correctly)
        with tempfile.NamedTemporaryFile(suffix="", delete=False) as tmp_img_base:
            tmp_img_base_path = tmp_img_base.name

        result = subprocess.run(
            ["pdftoppm", "-r", "150", "-jpeg", "-singlefile", tmp_pdf_path, tmp_img_base_path],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"pdftoppm error: {result.stderr}", file=sys.stderr)
            return False

        # pdftoppm adds .jpg suffix
        generated_jpg = tmp_img_base_path + ".jpg"
        if not os.path.exists(generated_jpg):
            # Sometimes pdftoppm adds -1.jpg
            generated_jpg = tmp_img_base_path + "-1.jpg"

        if not os.path.exists(generated_jpg):
            print(f"Generated image not found at {generated_jpg}", file=sys.stderr)
            return False

        # Resize/crop to exact 1280×720
        with Image.open(generated_jpg) as img:
            img = img.convert("RGB")
            # Resize to fit 1280×720 maintaining aspect ratio, then center crop
            img_w, img_h = img.size
            target_w, target_h = 1280, 720
            scale = max(target_w / img_w, target_h / img_h)
            new_w = int(img_w * scale)
            new_h = int(img_h * scale)
            img = img.resize((new_w, new_h), Image.LANCZOS)
            left = (new_w - target_w) // 2
            top = (new_h - target_h) // 2
            img = img.crop((left, top, left + target_w, top + target_h))
            img.save(output_jpg, "JPEG", quality=95)

        return True

    finally:
        if os.path.exists(tmp_pdf_path):
            os.unlink(tmp_pdf_path)


def images_to_pptx(image_paths: list[str], output_pptx: str) -> str:
    """Combine slide images into a PPTX file."""
    prs = Presentation()
    prs.slide_width = Inches(13.333)   # 16:9 widescreen
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    for img_path in image_paths:
        slide = prs.slides.add_slide(blank_layout)
        with Image.open(img_path) as img:
            img = img.convert("RGB")
            buf = BytesIO()
            img.save(buf, format="JPEG", quality=95)
            buf.seek(0)
            slide.shapes.add_picture(
                buf,
                Inches(0), Inches(0),
                Inches(13.333), Inches(7.5)
            )

    prs.save(output_pptx)
    return f"Saved {len(image_paths)} slides to {output_pptx}"


def main():
    parser = argparse.ArgumentParser(description="Convert HTML slides to PPTX")
    parser.add_argument("html_files", nargs="+", help="HTML slide files in order")
    parser.add_argument("-o", "--output", required=True, help="Output PPTX path")
    args = parser.parse_args()

    jpg_paths = []
    with tempfile.TemporaryDirectory() as tmpdir:
        for i, html_path in enumerate(args.html_files):
            jpg_path = os.path.join(tmpdir, f"slide_{i+1:02d}.jpg")
            print(f"Rendering slide {i+1}/{len(args.html_files)}: {html_path}", flush=True)
            ok = html_to_jpg(html_path, jpg_path)
            if not ok:
                print(f"ERROR: Failed to render {html_path}", file=sys.stderr)
                sys.exit(1)
            jpg_paths.append(jpg_path)
            print(f"  ✓ {jpg_path}", flush=True)

        result = images_to_pptx(jpg_paths, args.output)
        print(result)


if __name__ == "__main__":
    main()
