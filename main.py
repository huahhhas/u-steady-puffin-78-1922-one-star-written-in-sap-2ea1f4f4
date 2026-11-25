#!/usr/bin/env python3
"""One Star, Written in Sap.

A single one-line 1-star review, written in the voice of a houseplant
about the human who owns it, for the make.fun bounty of the same name.

The line is written exactly, with no trailing newline, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set), then
re-read and checked against the gate: UTF-8 text, 1-279 characters,
not only whitespace, a single line.
"""

import hashlib
import os
from pathlib import Path

# The review: one star, one line, one drowned houseplant.
LINE = (
    "One star. He waters me every Sunday, thirsty or not, then looks "
    "betrayed when my roots rot. A calendar reminder is not a care "
    "plan, and I am drowning on a schedule."
)


def validate(text: str) -> None:
    """Check the line against the bounty gate before it is submitted."""
    assert text == LINE, "entry.txt does not match the line"
    assert 1 <= len(text) <= 279, f"length {len(text)} outside 1-279"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text, "entry is not a single line"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    text = target.read_text(encoding="utf-8")
    validate(text)
    print(f"wrote {target} ({len(text)} chars)")
    print("sha256:", hashlib.sha256(text.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
