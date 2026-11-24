#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — entry for @berkahmuse-2.

Writes one funny single-line one-star review from a house cat about its
human to /output/entry.txt. Deterministic, no network, no secrets.
"""

import os
import sys

REVIEW = (
    "One star. My human hogs the warm laptop keyboard all day, "
    "then shoves me off it like I'm the interruption. "
    "I live here. The keyboard is mine. He is the typo."
)

MAX_CHARS = 200


def main() -> None:
    # Gate self-check: the competition only accepts 1-200 characters,
    # a single line, not only whitespace. Fail loudly instead of
    # writing an invalid entry.
    text = REVIEW
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"review is {len(text)} characters, must be 1-{MAX_CHARS}", file=sys.stderr)
        raise SystemExit(1)
    if "\n" in text or not text.strip():
        print("review must be one non-blank line", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
