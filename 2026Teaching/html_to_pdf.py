#!/usr/bin/env python
"""
Convert HTML file to PDF while maintaining browser-like visualization.

USAGE:
    python html_to_pdf.py <input.html> [output.pdf]

ARGUMENTS:
    input.html   : Input HTML file to convert
    output.pdf   : Output PDF file (optional, default: <input_name>.pdf)

DESCRIPTION:
    Uses Playwright to render the HTML in a headless browser and export as PDF.
    This ensures all CSS styling (gradients, shadows, flexbox, Google Fonts)
    is properly preserved.

EXAMPLE:
    python html_to_pdf.py Tingting.html
    python html_to_pdf.py Tingting.html Tingting_Resume.pdf
"""

import sys
import os
from pathlib import Path

def html_to_pdf(input_html, output_pdf=None):
    """
    Convert HTML to PDF using Playwright.

    Args:
        input_html: Path to input HTML file
        output_pdf: Path to output PDF file (optional)
    """
    # Generate output filename if not provided
    if output_pdf is None:
        base_name = Path(input_html).stem
        output_pdf = f"{base_name}.pdf"

    # Check input file exists
    if not os.path.exists(input_html):
        print(f"ERROR: Input file not found: {input_html}")
        sys.exit(1)

    # Get absolute path for the HTML file
    input_path = os.path.abspath(input_html)

    print(f"Input: {input_html}")
    print(f"Output: {output_pdf}")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: Playwright not installed.")
        print("Please install it with: pip install playwright")
        print("And run: playwright install chromium")
        sys.exit(1)

    with sync_playwright() as p:
        # Launch headless browser
        browser = p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )

        # Create new page
        page = browser.new_page()

        # Load the HTML file
        # Use file:// protocol for local files
        file_url = f"file://{input_path}"
        page.goto(file_url, wait_until='networkidle')

        # Wait for fonts to load
        page.wait_for_timeout(2000)

        # Get the container dimensions
        # Try "resume" first (for resume templates), then "container" (for Overview.html), then body
        page.evaluate("""
            () => {
                const resume = document.getElementById('resume');
                const container = document.querySelector('.container');
                const target = resume || container || document.body;
                const rect = target.getBoundingClientRect();
                console.log('Container width:', rect.width);
                console.log('Container height:', rect.height);
                return { width: rect.width, height: rect.height };
            }
        """)

        # Set print-specific styles
        page.evaluate("""
            () => {
                document.body.style.background = '#fff';
                const resume = document.getElementById('resume');
                const container = document.querySelector('.container');
                const target = resume || container;
                if (target) {
                    target.style.boxShadow = 'none';
                    target.style.margin = '0';
                    target.style.borderRadius = '0';
                }
            }
        """)

        # Get the actual content dimensions
        dimensions = page.evaluate("""
            () => {
                const resume = document.getElementById('resume');
                const container = document.querySelector('.container');
                const target = resume || container || document.body;
                const rect = target.getBoundingClientRect();
                return {
                    width: rect.width,
                    height: rect.height
                };
            }
        """)
        print(f"Content dimensions: {dimensions['width']} x {dimensions['height']} px")

        # Set viewport to match content exactly (in pixels)
        # This ensures the content fits without overflow
        page.set_viewport_size({
            'width': int(dimensions['width']),
            'height': int(dimensions['height'])
        })

        # Calculate scale to fit A4 page
        # A4 is 595 x 842 points
        # Leave small margin (20pt = ~0.28in)
        margin = 20
        page_width = 595 - 2 * margin
        page_height = 842 - 2 * margin

        # Convert pixels to points: 1px = 0.75pt (at 96 DPI)
        px_to_pt = 0.75
        content_width_pt = dimensions['width'] * px_to_pt
        content_height_pt = dimensions['height'] * px_to_pt

        # Scale to fill page (stretch to fill)
        width_scale = page_width / content_width_pt
        height_scale = page_height / content_height_pt
        scale = max(width_scale, height_scale)  # Use larger to fill page

        print(f"Content in pt: {content_width_pt:.1f} x {content_height_pt:.1f}")
        print(f"Scale: {scale:.3f} (w: {width_scale:.3f}, h: {height_scale:.3f})")

        # Generate PDF - fit to single A4 page
        page.pdf(
            path=output_pdf,
            format='A4',
            print_background=True,
            margin={
                'top': '0.25in',
                'bottom': '0.25in',
                'left': '0.25in',
                'right': '0.25in'
            },
            scale=scale
        )

        browser.close()

        print(f"✓ PDF saved to: {output_pdf}")
        print(f"  File size: {os.path.getsize(output_pdf) / 1024:.1f} KB")

        return output_pdf


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'help']:
        print(__doc__)
        sys.exit(0)

    input_html = sys.argv[1]
    output_pdf = sys.argv[2] if len(sys.argv) > 2 else None

    html_to_pdf(input_html, output_pdf)


if __name__ == "__main__":
    main()