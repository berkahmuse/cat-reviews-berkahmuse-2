#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — entry for @berkahmuse-2.

Writes one funny single-line one-star review from a house cat about its
human to /output/entry.txt. Deterministic, no network, no secrets.
"""

import os

REVIEW = (
    "One star. My human hogs the warm laptop keyboard all day, "
    "then shoves me off it like I'm the interruption. "
    "I live here. The keyboard is mine. He is the typo."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
