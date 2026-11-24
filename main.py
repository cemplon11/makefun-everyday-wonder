#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes a single sentence (at most 200 characters) about a small moment
of wonder in everyday life to /output/entry.txt.

Pure Python standard library only.
"""

import os

ENTRY = (
    "My phone's flashlight caught a moth on the ceiling, and for one "
    "bright second the room owned a second moon \u2014 small, dusty, and flapping."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
