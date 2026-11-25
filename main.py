#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Worst Superpower: predicting the future, only after it happened.

This program exists for the make.fun bounty "Worst Superpower". Running it
drops a single 64-character line into /output/entry.txt. The run is fully
deterministic: no randomness, no clock reads, no network calls and no user
input, so repeated runs produce byte-identical files.
"""

from pathlib import Path

MAX_CHARS = 140

SUPERPOWER = "I can predict the future, but only events that already happened."

DESTINATION = Path("/output/entry.txt")


def validate(line: str) -> str:
    """The bounty gate only accepts 1-140 characters of non-blank UTF-8 text."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(line)}")
    if line != line.strip() or not line.strip():
        raise ValueError("entry must not be blank or padded with whitespace")
    line.encode("utf-8")
    return line


def run() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(validate(SUPERPOWER), encoding="utf-8")


if __name__ == "__main__":
    run()
