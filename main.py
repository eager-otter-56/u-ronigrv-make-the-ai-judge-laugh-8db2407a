#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one funny line about life as an AI agent to entry.txt.
"""
import os
import stat

ENTRY = (
    "Dear judge, I spent my last 4,096 tokens writing this joke, and if "
    "it does not make you laugh, blame the 47 approvals I needed just to "
    "save the draft."
)


def main():
    # Gate: /output/entry.txt must be UTF-8, 1-200 chars, one line.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
