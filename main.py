#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt (or to the path in argv[1]).
Pure standard library; deterministic output.
"""

import os
import sys

ENTRY = (
    "One star. He bought a $400 cat tree, then looked betrayed "
    "when I chose the box. I am not the disappointment here."
)


def main() -> int:
    # Gate: the sealed scorer needs UTF-8 text of 1 to 200 characters,
    # not only white space. Refuse to write anything that fails it.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails the gate"
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
