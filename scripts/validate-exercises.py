#!/usr/bin/env python3
"""Validate the assignment pages and local instructional images."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXERCISES = ROOT / "Assignment_19_Conditions and Loops in JavaScript"
EXPECTED = [f"Q{i}.html" for i in range(1, 6)]
errors = []
image_count = 0

for name in EXPECTED:
    page = EXERCISES / name
    if not page.is_file():
        errors.append(f"Missing exercise: {page.relative_to(ROOT)}")
        continue
    source = page.read_text(encoding="utf-8")
    for marker in ("<!DOCTYPE html>", "<html", "<head>", "<body>", "</html>"):
        if marker.lower() not in source.lower():
            errors.append(f"{name}: missing {marker}")
    if not re.search(r"<script\b", source, re.IGNORECASE):
        errors.append(f"{name}: no inline script element found")

for name in ("Q1.html", "Q2.html", "Q3.html"):
    page = EXERCISES / name
    if not page.is_file():
        continue
    source = page.read_text(encoding="utf-8")
    refs = re.findall(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\']', source, re.IGNORECASE)
    for ref in refs:
        if re.match(r"^(https?:|data:|#)", ref, re.IGNORECASE):
            continue
        target = (page.parent / ref).resolve()
        if not target.is_file():
            errors.append(f"{name}: missing image reference {ref}")
        else:
            image_count += 1

if errors:
    print("❌ Exercise validation failed:")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print(f"✅ Found {len(EXPECTED)} exercise pages and verified {image_count} local image references.")
print("ℹ️ This check does not execute JavaScript or render pages.")
