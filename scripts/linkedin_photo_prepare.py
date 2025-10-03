#!/usr/bin/env python3
"""
Prepare a LinkedIn-friendly profile photo:
- Replace the red background with a subtle whitish-blue gradient
- Add a simple navy tie positioned via face detection

Usage:
  python scripts/linkedin_photo_prepare.py --input path/to/photo.jpg --output out.png

Notes:
- Background removal uses color segmentation in HSV (red background keying).
- Face detection uses OpenCV Haar cascade.
- Output is saved as PNG to preserve transparency/quality.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np
from PIL import Image, ImageDraw

# Lazy imports for heavy deps to avoid CLI startup overhead

def _lazy_import_cv2():  # type: ignore
    import cv2  # noqa: F401
    return cv2


Color = Tuple[int, int, int]


@dataclass
class FaceBox:
    x: int
    y: int
    width: int
    height: int

    @property
    def center_bottom(self) -> Tuple[int, int]:
        return (self.x + self.width // 2, int(self.y + self.height * 0.95))


def generate_linkedin_gradient_background(width: int, height: int,
                                          top_color: Color = (234, 243, 255),
                                          bottom_color: Color = (191, 215, 255)) -> Image.Image:
    """Create a vertical whitish-blue gradient background (RGBA)."""
    # Create gradient by linear interpolation per row
    gradient = np.zeros((height, width, 4), dtype=np.uint8)
    top = np.array([*top_color, 255], dtype=np.float32)
    bottom = np.array([*bottom_color, 255], dtype=np.float32)

    for row in range(height):
        t = row / max(1, height - 1)
        color = (1 - t) * top + t * bottom
        gradient[row, :, :] = color.astype(np.uint8)

    return Image.fromarray(gradient, mode="RGBA")


def remove_background_keep_subject(image: Image.Image) -> Image.Image:
    """Key out red background via HSV and return RGBA subject image.

    This method is tuned for photos with a fairly uniform red backdrop.
    """
    cv2 = _lazy_import_cv2()
    rgb = image.convert("RGB")
    bgr = cv2.cvtColor(np.array(rgb), cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

    # Red appears near 0 and 180 hue in HSV. Use two ranges and combine.
    lower_red1 = np.array([0, 60, 40])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 60, 40])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_bg_mask = cv2.bitwise_or(mask1, mask2)

    # Refine mask: suppress likely foreground by preserving low saturation/different hue
    # and tighten edges using morphology.
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    red_bg_mask = cv2.morphologyEx(red_bg_mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    red_bg_mask = cv2.morphologyEx(red_bg_mask, cv2.MORPH_OPEN, kernel, iterations=1)

    # Optionally, expand background mask towards borders to ensure full backdrop selection.
    border_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    red_bg_mask = cv2.dilate(red_bg_mask, border_kernel, iterations=1)

    # Subject mask is inverse of red background
    subj_mask = cv2.bitwise_not(red_bg_mask)

    # Feather edges for smoother composite
    subj_mask = cv2.GaussianBlur(subj_mask, (9, 9), 0)

    # Compose RGBA subject
    alpha = (subj_mask.astype(np.float32) / 255.0)
    rgba = np.dstack([
        np.array(rgb)[:, :, 0],
        np.array(rgb)[:, :, 1],
        np.array(rgb)[:, :, 2],
        (alpha * 255).astype(np.uint8),
    ])
    subject = Image.fromarray(rgba, mode="RGBA")
    return subject


def detect_primary_face_bbox(image_rgb: Image.Image) -> Optional[FaceBox]:
    """Detect the most prominent face using OpenCV Haar cascade."""
    cv2 = _lazy_import_cv2()
    gray = cv2.cvtColor(np.array(image_rgb.convert("RGB")), cv2.COLOR_RGB2GRAY)
    # Load cascade from OpenCV data path
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,
                                          flags=cv2.CASCADE_SCALE_IMAGE, minSize=(80, 80))
    if faces is None or len(faces) == 0:
        return None
    # Choose the largest face
    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
    return FaceBox(int(x), int(y), int(w), int(h))


def draw_tie(image_rgba: Image.Image, face_box: Optional[FaceBox]) -> Image.Image:
    """Draw a simple navy tie below the face. Operates in-place and returns image."""
    img = image_rgba.copy().convert("RGBA")
    w, h = img.size
    draw = ImageDraw.Draw(img, mode="RGBA")

    if face_box is None:
        # Fallback: assume face is centered upper-half
        cx = w // 2
        cy = int(h * 0.42)
        face_height = int(h * 0.22)
    else:
        cx, cy = face_box.center_bottom
        face_height = face_box.height

    # Tie sizing based on face height
    knot_height = max(12, int(face_height * 0.12))
    knot_width = max(16, int(face_height * 0.16))
    tie_length = max(int(h * 0.20), int(face_height * 1.2))
    tie_bottom_width = max(26, int(knot_width * 1.6))

    # Colors
    navy = (10, 42, 102, 255)  # #0a2a66
    navy_dark = (6, 26, 64, 255)
    highlight = (255, 255, 255, 60)

    # Knot (an isosceles trapezoid/diamond-ish)
    knot_top_y = cy + int(face_height * 0.02)
    knot_bottom_y = knot_top_y + knot_height
    half_knot_w = knot_width // 2

    knot_points = [
        (cx - half_knot_w, knot_top_y),
        (cx + half_knot_w, knot_top_y),
        (cx + int(half_knot_w * 0.7), knot_bottom_y),
        (cx - int(half_knot_w * 0.7), knot_bottom_y),
    ]
    draw.polygon(knot_points, fill=navy, outline=navy_dark)

    # Tie blade (downward kite shape)
    tip_y = min(h - 6, knot_bottom_y + tie_length)
    blade_half_top = int(knot_width * 0.6)
    blade_half_bottom = tie_bottom_width // 2

    blade_points = [
        (cx - blade_half_top, knot_bottom_y),
        (cx + blade_half_top, knot_bottom_y),
        (cx + blade_half_bottom, tip_y - int(tie_bottom_width * 0.4)),
        (cx, tip_y),
        (cx - blade_half_bottom, tip_y - int(tie_bottom_width * 0.4)),
    ]
    draw.polygon(blade_points, fill=navy, outline=navy_dark)

    # Subtle highlight on the left side of blade
    highlight_poly = [
        (cx - blade_half_top + 1, knot_bottom_y + 2),
        (cx - blade_half_top + 1, tip_y - int(tie_bottom_width * 0.45)),
        (cx - 2, tip_y - 4),
        (cx - 2, knot_bottom_y + 2),
    ]
    draw.polygon(highlight_poly, fill=highlight)

    return img


def compose_subject_on_background(subject_rgba: Image.Image, background_rgba: Image.Image) -> Image.Image:
    bg = background_rgba.copy().convert("RGBA")
    subj = subject_rgba.copy().convert("RGBA")
    if subj.size != bg.size:
        subj = subj.resize(bg.size, Image.LANCZOS)
    composed = Image.alpha_composite(bg, subj)
    return composed


def process(input_path: str, output_path: str, width: Optional[int], height: Optional[int]) -> None:
    # Load image
    base_img = Image.open(input_path)

    # Resize if requested
    if width or height:
        target_w = width or int(base_img.width * (height / base_img.height))
        target_h = height or int(base_img.height * (width / base_img.width))
        base_img = base_img.resize((int(target_w), int(target_h)), Image.LANCZOS)

    # Remove red background via HSV segmentation
    subject = remove_background_keep_subject(base_img)

    # Background gradient
    bg = generate_linkedin_gradient_background(subject.width, subject.height)

    # Composite
    composed = compose_subject_on_background(subject, bg)

    # Tie drawing based on face detection on the composed image (better lighting/contrast)
    face_box = detect_primary_face_bbox(composed.convert("RGB"))
    with_tie = draw_tie(composed, face_box)

    # Save output (PNG)
    with_tie.save(output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare a LinkedIn-friendly profile photo")
    parser.add_argument("--input", required=True, help="Path to input photo")
    parser.add_argument("--output", required=True, help="Path to save processed PNG/JPG")
    parser.add_argument("--width", type=int, default=None, help="Optional output width in pixels")
    parser.add_argument("--height", type=int, default=None, help="Optional output height in pixels")

    args = parser.parse_args()
    process(args.input, args.output, args.width, args.height)


if __name__ == "__main__":
    main()
