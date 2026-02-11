"""
Iris helper: create a new diary entry from the template.

Usage:
  python scripts/new_entry.py 001_first_trade
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "diary" / "000_template.md"
DIARY_DIR = ROOT / "diary"

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/new_entry.py <entry_name>")
        sys.exit(1)

    name = sys.argv[1].strip()
    out = DIARY_DIR / f"{name}.md"

    if out.exists():
        print(f"Already exists: {out}")
        sys.exit(1)

    content = TEMPLATE.read_text(encoding="utf-8")
    out.write_text(content, encoding="utf-8")
    print(f"Created: {out}")

if __name__ == "__main__":
    main()
