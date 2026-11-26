#!/usr/bin/env python3
"""One Star, Written in Sap — a houseplant's one-line 1-star review of its human.

The program prints exactly one line: a review in the plant's own voice,
with a concrete grievance (called "low-maintenance", then forgotten for
three weeks behind the curtains) and the reason for the single star
(the cat at least says hello). Under 280 characters, per the bounty gate.
It also writes the identical line to /output/entry.txt.
"""

LINE = (
    "\u2605\u2606\u2606\u2606\u2606 He called me \"low-maintenance\", "
    "then forgot me for three weeks behind the curtains. "
    "I survived on one sunbeam and pure spite. "
    "One star, because the cat at least says hello."
)


def main() -> None:
    if len(LINE) >= 280:
        raise ValueError("review line must stay under 280 characters")
    text = LINE + "\n"
    import sys
    sys.stdout.write(text)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
