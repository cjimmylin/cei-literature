#!/usr/bin/env python3
"""
Migrate AI Labs PDFs from workspace to root-level AI-Lab-PDFs directory.

This script moves all PDF files from CEI-Lit-WS/AI Labs to a new AI-Lab-PDFs
directory at the vault root, preserving the complete company/model hierarchy.

Usage:
    python migrate_ai_labs_pdfs.py --dry-run   # Preview changes
    python migrate_ai_labs_pdfs.py --execute   # Execute migration
    python migrate_ai_labs_pdfs.py --rollback  # Rollback migration
"""

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Tuple

# Import vault configuration
from vault_config import WORKSPACE_ROOT

# Define paths
AI_LABS_DIR = WORKSPACE_ROOT / "AI Labs"
VAULT_ROOT = WORKSPACE_ROOT.parent
AI_LAB_PDFS_ROOT = VAULT_ROOT / "AI-Lab-PDFs"
LOGS_DIR = WORKSPACE_ROOT / "logs"


def find_all_pdfs(directory: Path) -> List[Path]:
    """
    Recursively find all PDF files in directory.

    Args:
        directory: Directory to search

    Returns:
        List of PDF file paths
    """
    if not directory.exists():
        print(f"Warning: Directory does not exist: {directory}")
        return []

    pdf_files = list(directory.rglob("*.pdf"))
    return sorted(pdf_files)


def count_pdfs(directory: Path) -> int:
    """Count PDF files in directory."""
    return len(find_all_pdfs(directory))


def filter_valid_pdfs(pdf_files: List[Path], min_size_kb: int = 1) -> Tuple[List[Path], List[Path]]:
    """
    Filter PDFs by size to separate valid files from stubs.

    Args:
        pdf_files: List of PDF paths
        min_size_kb: Minimum file size in KB (default 1KB)

    Returns:
        Tuple of (valid_pdfs, stub_pdfs)
    """
    min_size_bytes = min_size_kb * 1024
    valid_pdfs = []
    stub_pdfs = []

    for pdf in pdf_files:
        if pdf.stat().st_size >= min_size_bytes:
            valid_pdfs.append(pdf)
        else:
            stub_pdfs.append(pdf)

    return valid_pdfs, stub_pdfs


def build_migration_mappings(source_pdfs: List[Path]) -> List[Tuple[Path, Path]]:
    """
    Build source -> destination path mappings.

    Args:
        source_pdfs: List of source PDF paths

    Returns:
        List of (source_path, dest_path) tuples
    """
    mappings = []

    for source_path in source_pdfs:
        # Get relative path from AI Labs directory
        try:
            rel_path = source_path.relative_to(AI_LABS_DIR)
        except ValueError:
            print(f"Warning: Path not in AI Labs directory: {source_path}")
            continue

        # Build destination path
        dest_path = AI_LAB_PDFS_ROOT / rel_path
        mappings.append((source_path, dest_path))

    return mappings


def preview_migration(mappings: List[Tuple[Path, Path]], show_limit: int = 10):
    """
    Preview migration changes without executing.

    Args:
        mappings: List of (source, dest) path tuples
        show_limit: Maximum number of examples to show
    """
    print(f"\n{'='*70}")
    print(f"MIGRATION PREVIEW - DRY RUN MODE")
    print(f"{'='*70}\n")

    print(f"Total PDFs to migrate: {len(mappings)}")
    print(f"Source: {AI_LABS_DIR}")
    print(f"Destination: {AI_LAB_PDFS_ROOT}")

    # Analyze structure
    companies = set()
    for src, dst in mappings:
        rel_path = dst.relative_to(AI_LAB_PDFS_ROOT)
        if rel_path.parts:
            companies.add(rel_path.parts[0])

    print(f"\nCompanies to migrate: {len(companies)}")
    print(f"Companies: {', '.join(sorted(companies))}")

    # Show sample mappings
    print(f"\nFirst {min(show_limit, len(mappings))} files:")
    for i, (src, dst) in enumerate(mappings[:show_limit], 1):
        print(f"\n{i}. {src.name}")
        print(f"   FROM: {src.relative_to(WORKSPACE_ROOT)}")
        print(f"   TO:   {dst.relative_to(VAULT_ROOT)}")

    if len(mappings) > show_limit:
        print(f"\n... and {len(mappings) - show_limit} more files")

    print(f"\n{'='*70}")
    print("Run with --execute to perform migration")
    print(f"{'='*70}\n")


def execute_migration(mappings: List[Tuple[Path, Path]]) -> dict:
    """
    Execute PDF migration.

    Args:
        mappings: List of (source, dest) path tuples

    Returns:
        Migration log dictionary
    """
    print(f"\n{'='*70}")
    print(f"EXECUTING MIGRATION")
    print(f"{'='*70}\n")

    log = {
        "timestamp": datetime.now().isoformat(),
        "source_dir": str(AI_LABS_DIR),
        "dest_dir": str(AI_LAB_PDFS_ROOT),
        "total_files": len(mappings),
        "successful": [],
        "failed": [],
        "errors": []
    }

    # Create destination root
    AI_LAB_PDFS_ROOT.mkdir(parents=True, exist_ok=True)
    print(f"Created destination directory: {AI_LAB_PDFS_ROOT}")

    # Move files
    print(f"\nMoving {len(mappings)} PDFs...")
    for i, (source_path, dest_path) in enumerate(mappings, 1):
        try:
            # Create destination directory
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            # Move file (atomic operation)
            shutil.move(str(source_path), str(dest_path))

            log["successful"].append({
                "source": str(source_path),
                "destination": str(dest_path)
            })

            if i % 50 == 0:
                print(f"  Moved {i}/{len(mappings)} files...")

        except Exception as e:
            error_msg = f"Failed to move {source_path}: {e}"
            print(f"  ERROR: {error_msg}")
            log["failed"].append(str(source_path))
            log["errors"].append(error_msg)

    print(f"\nMigration complete!")
    print(f"  Successfully moved: {len(log['successful'])} files")
    print(f"  Failed: {len(log['failed'])} files")

    return log


def rollback_migration(log_file: Path = None):
    """
    Rollback migration by moving PDFs back to workspace.

    Args:
        log_file: Path to migration log file (optional)
    """
    print(f"\n{'='*70}")
    print(f"ROLLING BACK MIGRATION")
    print(f"{'='*70}\n")

    # Find PDFs in destination
    dest_pdfs = find_all_pdfs(AI_LAB_PDFS_ROOT)

    if not dest_pdfs:
        print("No PDFs found in destination directory. Nothing to rollback.")
        return

    print(f"Found {len(dest_pdfs)} PDFs to move back")

    # Build reverse mappings
    mappings = []
    for dest_path in dest_pdfs:
        rel_path = dest_path.relative_to(AI_LAB_PDFS_ROOT)
        source_path = AI_LABS_DIR / rel_path
        mappings.append((dest_path, source_path))

    # Move files back
    print(f"\nMoving {len(mappings)} PDFs back to workspace...")
    successful = 0
    failed = 0

    for i, (dest_path, source_path) in enumerate(mappings, 1):
        try:
            source_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(dest_path), str(source_path))
            successful += 1

            if i % 50 == 0:
                print(f"  Moved {i}/{len(mappings)} files...")

        except Exception as e:
            print(f"  ERROR: Failed to move {dest_path}: {e}")
            failed += 1

    print(f"\nRollback complete!")
    print(f"  Successfully moved: {successful} files")
    print(f"  Failed: {failed} files")


def verify_migration():
    """Verify migration succeeded."""
    print(f"\n{'='*70}")
    print(f"VERIFYING MIGRATION")
    print(f"{'='*70}\n")

    # Count PDFs in source
    source_count = count_pdfs(AI_LABS_DIR)
    print(f"PDFs remaining in workspace: {source_count}")

    if source_count > 0:
        source_pdfs = find_all_pdfs(AI_LABS_DIR)
        valid_pdfs, stub_pdfs = filter_valid_pdfs(source_pdfs)
        print(f"  Valid PDFs (>1KB): {len(valid_pdfs)}")
        print(f"  Stub PDFs (<1KB): {len(stub_pdfs)}")

        if stub_pdfs:
            print(f"\n  Stub files (left behind):")
            for pdf in stub_pdfs:
                size_bytes = pdf.stat().st_size
                print(f"    {pdf.relative_to(WORKSPACE_ROOT)} ({size_bytes} bytes)")

    # Count PDFs in destination
    dest_count = count_pdfs(AI_LAB_PDFS_ROOT)
    print(f"\nPDFs in new location: {dest_count}")

    # Count companies
    if AI_LAB_PDFS_ROOT.exists():
        companies = [d for d in AI_LAB_PDFS_ROOT.iterdir() if d.is_dir()]
        print(f"Companies migrated: {len(companies)}")
        if companies:
            print(f"Companies: {', '.join(sorted([c.name for c in companies]))}")

    print(f"\n{'='*70}")
    if dest_count >= 390:  # Expecting ~396, allow for some variance
        print("✅ Migration verification PASSED")
    else:
        print(f"⚠️  Migration verification WARNING: Expected ~396 PDFs, found {dest_count}")
    print(f"{'='*70}\n")


def save_log(log: dict, log_file: Path):
    """Save migration log to file."""
    log_file.parent.mkdir(parents=True, exist_ok=True)

    with open(log_file, 'w') as f:
        json.dump(log, indent=2, fp=f)

    print(f"\nMigration log saved to: {log_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Migrate AI Labs PDFs to root-level directory"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without executing"
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Execute migration"
    )
    parser.add_argument(
        "--rollback",
        action="store_true",
        help="Rollback migration"
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verify migration status"
    )

    args = parser.parse_args()

    # Default to dry-run if no action specified
    if not (args.dry_run or args.execute or args.rollback or args.verify):
        args.dry_run = True

    # Rollback mode
    if args.rollback:
        rollback_migration()
        return

    # Verify mode
    if args.verify:
        verify_migration()
        return

    # Find all PDFs in source
    print("Scanning for PDFs in AI Labs directory...")
    all_pdfs = find_all_pdfs(AI_LABS_DIR)
    print(f"Found {len(all_pdfs)} total PDFs")

    # Filter out stub files
    valid_pdfs, stub_pdfs = filter_valid_pdfs(all_pdfs)
    print(f"  Valid PDFs (>1KB): {len(valid_pdfs)}")
    print(f"  Stub PDFs (<1KB): {len(stub_pdfs)}")

    if stub_pdfs:
        print(f"\nStub files (will not be migrated):")
        for pdf in stub_pdfs:
            size_bytes = pdf.stat().st_size
            print(f"  {pdf.relative_to(WORKSPACE_ROOT)} ({size_bytes} bytes)")

    # Build migration mappings
    mappings = build_migration_mappings(valid_pdfs)

    if not mappings:
        print("\nNo PDFs to migrate!")
        return

    # Dry-run mode
    if args.dry_run:
        preview_migration(mappings)
        return

    # Execute mode
    if args.execute:
        # Confirm execution
        print(f"\n⚠️  WARNING: This will move {len(mappings)} PDFs from workspace to AI-Lab-PDFs/")
        response = input("Continue? [y/N]: ")

        if response.lower() != 'y':
            print("Migration cancelled.")
            return

        # Execute migration
        log = execute_migration(mappings)

        # Save log
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = LOGS_DIR / f"pdf_migration_{timestamp}.json"
        save_log(log, log_file)

        # Verify
        verify_migration()


if __name__ == "__main__":
    main()
