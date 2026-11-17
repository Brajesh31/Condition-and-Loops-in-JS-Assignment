#!/usr/bin/env python3
"""Check relative Markdown link targets in repository Markdown files."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
checked = 0
for md in ROOT.rglob("*.md"):
    if any(part in {".git", "node_modules"} for part in md.parts):
        continue
    source = md.read_text(encoding="utf-8")
    for part in source.split("](")[1:]:
        raw = part.split(")", 1)[0].strip()
        target = raw.split("#", 1)[0].split(" ", 1)[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
            continue
        checked += 1
        if not (md.parent / target).resolve().exists():
            errors.append(f"{md.relative_to(ROOT)}: broken link target {target}")
if errors:
    print("Documentation link validation failed:")
    for error in errors:
        print(" - " + error)
    sys.exit(1)
print(f"Checked {checked} relative Markdown link targets.")
