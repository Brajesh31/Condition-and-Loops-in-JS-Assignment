#!/usr/bin/env python3
"""Basic Markdown hygiene checks; preserve intentional two-space hard breaks."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
count = 0
for path in ROOT.rglob("*.md"):
    if any(part in {".git", "node_modules"} for part in path.parts):
        continue
    count += 1
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        trailing = len(line) - len(line.rstrip(" "))
        if trailing == 1 or trailing > 2:
            errors.append(f"{path.relative_to(ROOT)}:{line_no}: unexpected trailing whitespace")
if errors:
    print("Markdown hygiene check failed:")
    for error in errors:
        print(" - " + error)
    sys.exit(1)
print(f"Scanned {count} Markdown files; intentional two-space Markdown hard breaks are allowed.")
