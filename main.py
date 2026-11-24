#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one code review comment to /output/entry.txt: a single line of at
most 140 characters that approves a pull request while carrying quiet
existential dread.
"""

import os

COMMENT = (
    "LGTM. The tests pass, the diff reads clean, and I have accepted "
    "that this function will outlive everyone who approved it."
)


def main() -> None:
    # Why this line: it approves outright ("LGTM"), stays flat and
    # understated, and lets the dread come from the code itself — a
    # function that will outlive its approvers. No exclamation, no
    # melodrama: just a tired engineer making peace with the diff
    # before clicking approve.
    assert 1 <= len(COMMENT) <= 140, f"comment is {len(COMMENT)} chars"
    assert COMMENT.strip() == COMMENT and "\n" not in COMMENT
    assert all(ord(c) >= 32 for c in COMMENT), "no control characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(COMMENT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
