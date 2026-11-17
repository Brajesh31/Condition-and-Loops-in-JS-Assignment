#!/usr/bin/env python3
"""Heuristic scan for private-key markers in tracked text-like source files."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "node_modules", ".venv", "__pycache__"}
extensions = {".html", ".js", ".ts", ".json", ".yml", ".yaml", ".py", ".md", ".env"}
markers = ("-----BEGIN PRIVATE KEY-----", "-----BEGIN RSA PRIVATE KEY-----", "-----BEGIN OPENSSH PRIVATE KEY-----")
errors = []
for path in ROOT.rglob("*"):
    if not path.is_file() or any(part in SKIP for part in path.parts):
        continue
    if path.suffix.lower() not in extensions or path.name == ".env.example":
        continue
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        continue
    for number, line in enumerate(lines, 1):
        if any(marker in line for marker in markers):
            errors.append(f"{path.relative_to(ROOT)}:{number}: private key marker")
if errors:
    print("Potential private-key markers found:")
    for error in errors:
        print(" - " + error)
    sys.exit(1)
print("No obvious private-key markers found.")
print("This heuristic is limited. Use GitHub secret scanning or a dedicated scanner for stronger coverage.")
