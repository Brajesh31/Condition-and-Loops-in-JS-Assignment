#!/usr/bin/env python3
"""Validate assignment HTML pages, titles, scripts, and referenced images."""
from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EXERCISES = ROOT / "Assignment_19_Conditions and Loops in JavaScript"
EXPECTED = [f"Q{i}.html" for i in range(1, 6)]
errors = []
image_count = 0

class ExerciseParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title_open = False
        self.title_text = []
        self.script_count = 0
        self.images = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag.lower() == "title":
            self.title_open = True
        elif tag.lower() == "script":
            self.script_count += 1
        elif tag.lower() == "img":
            self.images.append((attributes.get("src", ""), attributes.get("alt", "")))

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.title_open = False

    def handle_data(self, data):
        if self.title_open:
            self.title_text.append(data)

for name in EXPECTED:
    page = EXERCISES / name
    if not page.is_file():
        errors.append(f"Missing exercise: {page.relative_to(ROOT)}")
        continue

    parser = ExerciseParser()
    try:
        parser.feed(page.read_text(encoding="utf-8"))
        parser.close()
    except Exception as error:
        errors.append(f"{name}: HTML parsing error: {error}")
        continue

    title = " ".join(" ".join(parser.title_text).split())
    if not title or title.lower() == "document":
        errors.append(f"{name}: missing a descriptive document title")
    if parser.script_count == 0:
        errors.append(f"{name}: no embedded script element found")

    for source, alt in parser.images:
        if not source:
            errors.append(f"{name}: image without a source")
            continue
        if not alt.strip():
            errors.append(f"{name}: image missing meaningful alt text: {source}")
        if source.startswith(("http://", "https://", "data:", "#")):
            continue
        target = (page.parent / source).resolve()
        if not target.is_file():
            errors.append(f"{name}: missing image reference {source}")
        else:
            image_count += 1

if errors:
    print("❌ Exercise validation failed:")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print(f"✅ Validated {len(EXPECTED)} exercise pages, descriptive titles, embedded scripts, and {image_count} local images.")
print("ℹ️ This check does not execute JavaScript or render pages.")
