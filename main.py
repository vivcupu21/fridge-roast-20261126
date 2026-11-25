"""Roast the Smart Fridge: one line, best laugh wins.

Writes the stored roast line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network, no randomness, deterministic output.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
