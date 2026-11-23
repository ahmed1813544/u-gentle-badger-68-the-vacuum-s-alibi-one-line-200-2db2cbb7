"""The Vacuum's Alibi: write the robot vacuum's one-line excuse to entry.txt.

Stdlib only, deterministic: every run writes the exact same bytes.
"""

import os

LINE = (
    "I did not miss it. My cliff sensors classified the Cheerio as a "
    "load-bearing structure, and I am not licensed to demolish your kitchen."
)


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # single line, no trailing newline.
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
