#!/usr/bin/env python3
"""Angry Judge entry: one short funny rant (max 400 chars) about a small
everyday annoyance, written to /output/entry.txt (or $OUTPUT_PATH/entry.txt).

The rant, drafted fresh from prose: proving you are human to a CAPTCHA,
over and over, and the site still doubting you. The test was never about
humanity; it is about patience, and the ranter is failing it.

The program validates the text before writing: 1-400 characters, no control
characters (the sealed gate only accepts clean UTF-8 text), then writes it
with no trailing newline and echoes it to stdout for the grader log.
"""
import os
import sys

RANT = (
    "Today I proved I am human nine times. Nine CAPTCHAs. "
    "Traffic lights, bicycles, crosswalks \u2014 I clicked them all, "
    "and the internet still squints at me like a robot in a fake moustache. "
    "The test was never whether I am human. It is whether I am patient. "
    "I am not."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_PATH", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = RANT.strip()
    if not 1 <= len(text) <= 400:
        print(f"rant is {len(text)} chars, must be 1-400", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 and ch not in "\t\n" for ch in text):
        print("rant contains control characters", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
