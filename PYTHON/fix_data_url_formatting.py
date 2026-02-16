#!/usr/bin/env python3
"""
Fix DATA_URL formatting: replace bare NA with quoted "NA".

433 papers have `DATA_URL: NA` (unquoted) which should be `DATA_URL: "NA"` for
consistency with the rest of the vault.

Uses safe regex replacement (no parse/rebuild round-trip).
"""

import re
import functools
from pathlib import Path

print = functools.partial(print, flush=True)

PAPERS_DIR = Path(__file__).parent.parent / "papers"


def fix_data_url():
    fixed = 0
    errors = 0

    for paper in sorted(PAPERS_DIR.glob("*.md")):
        try:
            content = paper.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = paper.read_text(encoding="latin-1")

        # Match DATA_URL: NA (not already quoted, not part of a longer value)
        # Negative lookahead ensures we don't match DATA_URL: "NA" or DATA_URL: NA_something
        new_content, n = re.subn(
            r'^(DATA_URL:\s*)NA\s*$',
            r'\g<1>"NA"',
            content,
            count=1,
            flags=re.MULTILINE,
        )

        if n > 0:
            paper.write_text(new_content, encoding="utf-8")
            fixed += 1

    print(f"Fixed {fixed} papers with bare DATA_URL: NA → DATA_URL: \"NA\"")
    if errors:
        print(f"Errors: {errors}")


if __name__ == "__main__":
    fix_data_url()
