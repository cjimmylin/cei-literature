#!/usr/bin/env python3
"""Fix semicolon-format author fields in specific papers.

These papers have authors in "Last; First" format instead of "First Last" format.
Uses re.subn with re.MULTILINE for safe YAML editing (no parse→rebuild).
"""

import os
import re
import tempfile
from pathlib import Path

PAPERS_DIR = Path(__file__).resolve().parent.parent / "papers"

# Each entry: (filename, new_authors, new_first_author, new_last_author)
# first_author = first name in list, last_author = last name in list
FIXES = [
    # Single-author papers
    (
        "2021-Angle-Can AI Lead to Genuine Virtue Confucian.md",
        "Stephen C. Angle",
        "[[Stephen C. Angle]]",
        "[[Stephen C. Angle]]",
    ),
    (
        "2023-McDonald-AI alignment and the categorical imperative.md",
        "Fritz J. McDonald",
        "[[Fritz J. McDonald]]",
        "[[Fritz J. McDonald]]",
    ),
    (
        "2025-Brophy-Black Box Deployed.md",
        "Matthew E. Brophy",
        "[[Matthew E. Brophy]]",
        "[[Matthew E. Brophy]]",
    ),
    (
        "2025-Bryan-Virtue Ethics and Postponing Human Extinction.md",
        "Charles S. Bryan",
        "[[Charles S. Bryan]]",
        "[[Charles S. Bryan]]",
    ),
    (
        "2025-Elder-The Ethics of Digital Ghosts.md",
        "Alexis M. Elder",
        "[[Alexis M. Elder]]",
        "[[Alexis M. Elder]]",
    ),
    (
        "2025-Gong-Faith Respect and Moral Compass in.md",
        "Gerrit W. Gong",
        "[[Gerrit W. Gong]]",
        "[[Gerrit W. Gong]]",
    ),
    (
        "2025-Sanwoolu-Kantian deontology for AI.md",
        "Oluwaseun D. Sanwoolu",
        "[[Oluwaseun D. Sanwoolu]]",
        "[[Oluwaseun D. Sanwoolu]]",
    ),
    (
        "2025-Sullins-Automated Ethical Practical Reasoning.md",
        "John P. Sullins",
        "[[John P. Sullins]]",
        "[[John P. Sullins]]",
    ),
    # Multi-author papers
    (
        "2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences.md",
        "Wei Lu; Daniel L. Chen; Christian B. Hansen",
        "[[Wei Lu]]",
        "[[Christian B. Hansen]]",
    ),
    (
        "2026-Kolt-Legal Alignment for Safe and Ethical AI.md",
        '"Noam Kolt; Nicholas Caputo; Jack Boeglin; Cullen O\'Keefe; Rishi Bommasani; Stephen Casper; Mariano-Florentino Cuéllar; Noah Feldman; Iason Gabriel; Gillian K. Hadfield; Lewis Hammond; Peter Henderson; Atoosa Kasirzadeh; Seth Lazar; Anka Reuel; Kevin L. Wei; Jonathan Zittrain"',
        '"[[Noam Kolt]]"',
        '"[[Jonathan Zittrain]]"',
    ),
]


def fix_field(content: str, field: str, new_value: str) -> tuple[str, int]:
    """Replace a YAML frontmatter field value using re.subn (MULTILINE safe)."""
    # Match the field line: key: value (possibly quoted)
    pattern = rf'^({re.escape(field)}:)\s*.*$'
    replacement = rf'\1 {new_value}'
    new_content, count = re.subn(pattern, replacement, content, count=1, flags=re.MULTILINE)
    return new_content, count


def validate_quotes(content: str) -> bool:
    """Check that every line in the frontmatter has even quote count."""
    # Extract frontmatter
    m = re.match(r'^---\n(.*?\n)---', content, re.DOTALL)
    if not m:
        return True  # no frontmatter to validate
    fm = m.group(1)
    for i, line in enumerate(fm.split('\n'), start=2):
        if line.count('"') % 2 != 0:
            print(f"  WARNING: Odd quote count on line {i}: {line!r}")
            return False
    return True


def write_atomic(path: Path, content: str):
    """Write content atomically using tmp file + os.replace."""
    fd, tmp_path = tempfile.mkstemp(
        dir=path.parent, prefix=f".tmp.{os.getpid()}.", suffix=".md"
    )
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(content)
        os.replace(tmp_path, path)
    except Exception:
        # Clean up temp file on failure
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


def main():
    total_fixed = 0
    errors = 0

    for filename, new_authors, new_first, new_last in FIXES:
        paper_path = PAPERS_DIR / filename
        if not paper_path.exists():
            print(f"ERROR: Not found: {paper_path}")
            errors += 1
            continue

        print(f"Processing: {filename}")
        content = paper_path.read_text(encoding='utf-8')

        # Fix authors field
        content, n1 = fix_field(content, "authors", new_authors)
        if n1 == 0:
            print(f"  WARNING: authors field not found or not replaced")

        # Fix first_author field
        content, n2 = fix_field(content, "first_author", new_first)
        if n2 == 0:
            print(f"  WARNING: first_author field not found or not replaced")

        # Fix last_author field
        content, n3 = fix_field(content, "last_author", new_last)
        if n3 == 0:
            print(f"  WARNING: last_author field not found or not replaced")

        # Validate quotes
        if not validate_quotes(content):
            print(f"  ERROR: Quote validation failed, skipping write")
            errors += 1
            continue

        # Write atomically
        write_atomic(paper_path, content)
        total_fixed += 1
        print(f"  Fixed: authors={n1}, first_author={n2}, last_author={n3}")

    print(f"\nDone: {total_fixed} papers fixed, {errors} errors")


if __name__ == "__main__":
    main()
