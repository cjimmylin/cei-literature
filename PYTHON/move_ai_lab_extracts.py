#!/usr/bin/env python3
"""
Move AI Labs PDF extracts from PDF Extracts/AI Labs/ to their respective model folders.

Each extract has a source_pdf field in its YAML frontmatter that indicates
the original PDF location, which we use to determine the destination folder.
"""

import os
import re
import shutil
from pathlib import Path

# Use vault_config for paths
from vault_config import AI_LABS_DIR, PDF_EXTRACTS_DIR
EXTRACTS_DIR = PDF_EXTRACTS_DIR / "AI Labs"


def get_source_pdf_from_extract(extract_path):
    """Extract the source_pdf field from the YAML frontmatter."""
    with open(extract_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find source_pdf in YAML frontmatter
    match = re.search(r'source_pdf:\s*["\']?([^"\'\n]+)["\']?', content)
    if match:
        return match.group(1).strip()
    return None


def get_destination_folder(source_pdf):
    """
    Determine the destination folder based on the source PDF path.

    Example: "AI Labs/Anthropic/Claude 4/Claude_4_Opus_Sonnet_System_Card.pdf"
    -> Returns "AI Labs/Anthropic/Claude 4/"
    """
    source_path = Path(source_pdf)
    # Get the parent directory (the model folder)
    return source_path.parent


def move_extracts():
    """Move all extracts to their respective model folders."""
    if not EXTRACTS_DIR.exists():
        print(f"Error: {EXTRACTS_DIR} does not exist")
        return

    moved = 0
    skipped = 0
    errors = []

    extract_files = list(EXTRACTS_DIR.glob("*.md"))
    print(f"Found {len(extract_files)} extract files to process\n")

    for extract_path in sorted(extract_files):
        filename = extract_path.name

        # Get source PDF path from the extract
        source_pdf = get_source_pdf_from_extract(extract_path)

        if not source_pdf:
            errors.append((filename, "No source_pdf found in frontmatter"))
            continue

        # Determine destination folder
        dest_folder = get_destination_folder(source_pdf)

        # Skip if destination is a Papers folder - use the parent instead
        if dest_folder.name == "Papers":
            # Keep in Papers folder but within AI Labs structure
            pass

        dest_folder_full = Path(dest_folder)

        if not dest_folder_full.exists():
            errors.append((filename, f"Destination folder does not exist: {dest_folder}"))
            continue

        # Create new filename (remove company prefix)
        # e.g., "Anthropic-Claude_4_Opus_Sonnet_System_Card.md" -> "Claude_4_Opus_Sonnet_System_Card.md"
        parts = filename.split('-', 1)
        if len(parts) > 1:
            new_filename = parts[1]
        else:
            new_filename = filename

        # Rename to extract.md or keep original name
        dest_path = dest_folder_full / new_filename

        # Check if already exists
        if dest_path.exists():
            print(f"  Skipping {filename} - already exists at destination")
            skipped += 1
            continue

        # Move the file
        try:
            shutil.move(str(extract_path), str(dest_path))
            print(f"✓ {filename}")
            print(f"  -> {dest_path}")
            moved += 1
        except Exception as e:
            errors.append((filename, str(e)))

    # Summary
    print("\n" + "=" * 60)
    print("MOVE SUMMARY")
    print("=" * 60)
    print(f"Moved: {moved}")
    print(f"Skipped: {skipped}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\nErrors:")
        for filename, error in errors:
            print(f"  - {filename}: {error}")


if __name__ == "__main__":
    move_extracts()
