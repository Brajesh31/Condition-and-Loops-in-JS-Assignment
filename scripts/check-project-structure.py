#!/usr/bin/env python3
"""Check required project files and preserved assignment pages."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md", "LICENSE", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md",
    "SECURITY.md", "SUPPORT.md", "CHANGELOG.md", "ROADMAP.md",
    "Assignment_19_Conditions and Loops in JavaScript/Q1.html",
    "Assignment_19_Conditions and Loops in JavaScript/Q2.html",
    "Assignment_19_Conditions and Loops in JavaScript/Q3.html",
    "Assignment_19_Conditions and Loops in JavaScript/Q4.html",
    "Assignment_19_Conditions and Loops in JavaScript/Q5.html",
]
missing = [item for item in required if not (ROOT / item).is_file()]
if missing:
    print("Missing required paths:")
    for item in missing:
        print(" - " + item)
    sys.exit(1)
print(f"All {len(required)} required paths are present.")
