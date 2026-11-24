#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest, funny error copy.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to
/output/entry.txt) using a world-readable mode so the sealed scorer can read it.
Python 3 stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "Your upload failed: the disk is full, mostly of error logs about "
    "the disk being full. Delete something, then try again."
)


def validate(text):
    """Gate: 1-200 chars, single line, non-whitespace, valid UTF-8."""
    if not isinstance(text, str):
        return False
    if not text or text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if not 1 <= len(text) <= 200:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit("entry failed validation")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")  # no trailing newline: the file is exactly the line
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)
    os.chmod(path, 0o644)
    # Guard: re-read and confirm the written bytes are exactly the entry.
    with open(path, "rb") as fh:
        if fh.read() != data:
            raise SystemExit("written entry does not match")


if __name__ == "__main__":
    main()
