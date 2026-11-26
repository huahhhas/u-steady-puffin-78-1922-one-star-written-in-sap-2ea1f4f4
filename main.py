#!/usr/bin/env python3
"""One Star, Written in Sap — a houseplant's one-line 1-star review of its human.

The program prints exactly one line: a review in the plant's own voice,
with a concrete grievance (bought to purify the air, then parked in a
windowless bathroom beside an air freshener) and the reason for the single
star. Under 280 characters, per the bounty gate.
"""

LINE = (
    "\u2605\u2606\u2606\u2606\u2606 He bought me to \"purify the air\", "
    "then keeps me in a windowless bathroom next to the air freshener. "
    "I have one job and he gave it to a plug-in. One star."
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
