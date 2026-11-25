#!/usr/bin/env python3
"""Entry for the make.fun bounty "Have You Tried Turning It Off?"
(u-motasimfuad-have-you-tried-turning-it-off-154a938b).

The whole entry is one line of dialogue: a hopeless tech support agent,
cheerfully useless, talking to a customer who is already at the end of
their rope. The joke is on the agent, never the customer — his empathy
is real, it is just the only tool he has, and even the hold music is
outperforming him.

The program writes that single line to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader).
"""

import os

LINE = (
    "Please don't cry, sir. If you cry, I'll have to cry too, "
    "and then the hold music is the only one on this call doing its job."
)


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 199 characters,
    and not only white space. Refuse to hand in anything else."""
    encoded = line.encode("utf-8")  # raises if it cannot be encoded
    if not line.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(line) <= 199:
        raise ValueError(f"entry is {len(line)} characters, outside 1..199")
    if len(encoded) > 199:
        raise ValueError("entry encodes to more than 199 bytes")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
