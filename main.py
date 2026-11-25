#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Entry for the make.fun bounty "Worst Superpower".

The power on offer: perfect predictions of the future, delivered strictly
after the fact. This script is deliberately boring — it prints one fixed
64-character line and writes the same bytes to /output/entry.txt on every
run, with no randomness, no clock, no network and no input to read.
"""

import sys
from pathlib import Path

ENTRY = "I can predict the future, but only events that already happened."
OUT_FILE = Path("/output/entry.txt")
LIMIT = 140


def check(text: str) -> str:
    """Refuse anything the bounty gate would reject: blank, padded, or long."""
    stripped = text.strip()
    if text != stripped or not stripped:
        raise ValueError("entry must be non-blank with no surrounding whitespace")
    if len(text) > LIMIT:
        raise ValueError(f"entry is {len(text)} chars, limit is {LIMIT}")
    if len(text.split()) < 2:
        raise ValueError("entry must be a sentence, not a single word")
    text.encode("utf-8")
    return text


def main() -> int:
    line = check(ENTRY)
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(line, encoding="utf-8")
    sys.stdout.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
