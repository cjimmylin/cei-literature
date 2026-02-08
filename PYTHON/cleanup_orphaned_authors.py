#!/usr/bin/env python3
"""
Cleanup Orphaned Authors
Deletes author files that:
1. Are not referenced in any paper
2. Have invalid names (like ".")
And applies expansions for abbreviated names that have full name matches.
"""

import json
import logging
from pathlib import Path

from vault_config import AUTHORS_DIR, PAPERS_DIR, LOGS_DIR

logger = logging.getLogger(__name__)


def main(dry_run: bool = True):
    logger.info("=" * 60)
    logger.info("CLEANUP ORPHANED AUTHORS")
    logger.info(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    logger.info("=" * 60)
    logger.info("")

    # Load results
    results_file = LOGS_DIR / "20260124-author_expansion_results.json"
    if not results_file.exists():
        logger.error("No results file found. Run expand_abbreviated_authors.py first.")
        return

    with open(results_file, 'r') as f:
        data = json.load(f)

    resolved = data.get('resolved', {})
    unresolved = data.get('unresolved', [])
    to_delete = data.get('to_delete', [])

    # Actions taken
    deleted = []
    renamed = []
    kept = []

    # 1. Delete orphaned entries (unresolved = no papers reference them)
    logger.info("Step 1: Deleting orphaned author files...")
    for name in unresolved:
        author_file = AUTHORS_DIR / f"{name}.md"
        if author_file.exists():
            if not dry_run:
                author_file.unlink()
            deleted.append(name)
            logger.info(f"  {'Would delete' if dry_run else 'Deleted'}: {name}")

    # 2. Delete invalid entries
    logger.info("\nStep 2: Deleting invalid entries...")
    for name in to_delete:
        author_file = AUTHORS_DIR / f"{name}.md"
        if author_file.exists():
            if not dry_run:
                author_file.unlink()
            deleted.append(name)
            logger.info(f"  {'Would delete' if dry_run else 'Deleted'}: {name}")

    # 3. Apply real expansions (where abbreviated != full_name)
    logger.info("\nStep 3: Applying expansions...")
    for abbrev, info in resolved.items():
        full_name = info['full_name']

        # Only process if there's an actual expansion
        if abbrev != full_name:
            abbrev_file = AUTHORS_DIR / f"{abbrev}.md"
            full_file = AUTHORS_DIR / f"{full_name}.md"

            if abbrev_file.exists():
                if full_file.exists():
                    # Full name file exists, delete abbreviated
                    if not dry_run:
                        abbrev_file.unlink()
                    deleted.append(abbrev)
                    logger.info(f"  {'Would delete' if dry_run else 'Deleted'}: {abbrev} (full name exists: {full_name})")
                else:
                    # Rename to full name
                    if not dry_run:
                        abbrev_file.rename(full_file)
                    renamed.append((abbrev, full_name))
                    logger.info(f"  {'Would rename' if dry_run else 'Renamed'}: {abbrev} -> {full_name}")
        else:
            # Self-match - keep as is
            kept.append(abbrev)

    # Summary
    logger.info("\n" + "=" * 60)
    logger.info("SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Deleted: {len(deleted)}")
    logger.info(f"Renamed: {len(renamed)}")
    logger.info(f"Kept (self-matches): {len(kept)}")

    if renamed:
        logger.info("\nRenamed entries:")
        for old, new in renamed:
            logger.info(f"  {old} -> {new}")

    if kept:
        logger.info(f"\nKept (used in papers with abbreviated form): {len(kept)}")
        for name in kept[:10]:
            logger.info(f"  {name}")
        if len(kept) > 10:
            logger.info(f"  ... and {len(kept) - 10} more")

    if dry_run:
        logger.info("\n" + "=" * 60)
        logger.info("DRY RUN - No changes made. Use --execute to apply.")
        logger.info("=" * 60)


if __name__ == "__main__":
    import sys
    dry_run = "--execute" not in sys.argv
    main(dry_run=dry_run)
