#!/usr/bin/env python3
"""
Generate batch assignments for parallel PDF extraction.

Identifies missing PDF extracts and distributes them across N batches
using round-robin allocation by organization for even workload distribution.
"""

import json
import os
from pathlib import Path
from collections import defaultdict
from vault_config import AI_LAB_PDFS_DIR, PDF_EXTRACTS_DIR

EXTRACT_DIR = PDF_EXTRACTS_DIR / "AI Labs"
BATCH_DIR = Path(__file__).parent.parent / "logs" / "batches"
NUM_BATCHES = 10


def find_unique_pdfs():
    """Find all unique PDFs, preferring model-specific folders over Papers folders."""
    pdf_map = defaultdict(list)  # filename -> list of full paths

    for root, dirs, files in os.walk(AI_LAB_PDFS_DIR):
        for f in files:
            if f.lower().endswith('.pdf'):
                full_path = Path(root) / f
                pdf_map[f].append(full_path)

    # For duplicates, prefer paths that don't contain "Papers"
    unique_pdfs = {}
    for filename, paths in pdf_map.items():
        if len(paths) == 1:
            unique_pdfs[filename] = paths[0]
        else:
            # Prefer non-Papers paths
            non_papers = [p for p in paths if 'Papers' not in str(p)]
            unique_pdfs[filename] = non_papers[0] if non_papers else paths[0]

    return unique_pdfs


def extract_company_model(pdf_path):
    """Extract company and model name from path."""
    parts = pdf_path.parts
    # Check for old structure (AI Labs in path)
    if 'AI Labs' in parts:
        idx = parts.index('AI Labs')
        company = parts[idx + 1] if len(parts) > idx + 1 else "Unknown"
        model = parts[idx + 2] if len(parts) > idx + 2 and parts[idx + 2] != 'Papers' else None
        return company, model
    # New structure: AI-Lab-PDFs at root
    elif 'AI-Lab-PDFs' in parts:
        idx = parts.index('AI-Lab-PDFs')
        company = parts[idx + 1] if len(parts) > idx + 1 else "Unknown"
        model = parts[idx + 2] if len(parts) > idx + 2 and parts[idx + 2] != 'Papers' else None
        return company, model
    return "Unknown", None


def find_missing_extracts():
    """Identify PDFs that don't have corresponding markdown extracts."""
    unique_pdfs = find_unique_pdfs()
    missing = []

    for filename, pdf_path in unique_pdfs.items():
        company, model = extract_company_model(pdf_path)
        output_filename = f"{company}-{filename.replace('.pdf', '.md')}"
        output_path = EXTRACT_DIR / output_filename

        if not output_path.exists():
            missing.append({
                'pdf_filename': filename,
                'pdf_path': str(pdf_path),
                'output_path': str(output_path),
                'company': company,
                'model': model
            })

    return missing


def distribute_batches(missing_pdfs, num_batches):
    """Distribute PDFs across batches using round-robin by organization."""
    # Group by company
    by_company = defaultdict(list)
    for pdf_info in missing_pdfs:
        by_company[pdf_info['company']].append(pdf_info)

    # Sort companies by name for deterministic order
    companies = sorted(by_company.keys())

    # Initialize batches
    batches = [[] for _ in range(num_batches)]

    # Round-robin distribution
    batch_idx = 0
    for company in companies:
        for pdf_info in by_company[company]:
            batches[batch_idx].append(pdf_info)
            batch_idx = (batch_idx + 1) % num_batches

    return batches


def main():
    """Generate batch assignment files."""
    print("=" * 60)
    print("Batch Assignment Generation")
    print("=" * 60)

    # Find missing extracts
    print("\nScanning AI Labs directory...")
    missing = find_missing_extracts()
    print(f"Found {len(missing)} PDFs missing extracts")

    if not missing:
        print("\nNo missing extracts - all PDFs already processed!")
        return

    # Group by company for reporting
    by_company = defaultdict(int)
    for pdf_info in missing:
        by_company[pdf_info['company']] += 1

    print("\nMissing extracts by organization:")
    for company in sorted(by_company.keys()):
        print(f"  {company}: {by_company[company]}")

    # Distribute across batches
    print(f"\nDistributing {len(missing)} PDFs across {NUM_BATCHES} batches...")
    batches = distribute_batches(missing, NUM_BATCHES)

    # Create batch directory
    BATCH_DIR.mkdir(parents=True, exist_ok=True)

    # Write batch files
    for i, batch in enumerate(batches):
        batch_file = BATCH_DIR / f"batch_{i}.json"
        with open(batch_file, 'w', encoding='utf-8') as f:
            json.dump(batch, f, indent=2)
        print(f"  Batch {i}: {len(batch)} PDFs → {batch_file}")

    # Summary
    print("\n" + "=" * 60)
    print("BATCH SUMMARY")
    print("=" * 60)
    print(f"Total PDFs: {len(missing)}")
    print(f"Batches: {NUM_BATCHES}")
    print(f"PDFs per batch: {min(len(b) for b in batches)}-{max(len(b) for b in batches)}")
    print(f"\nBatch files saved to: {BATCH_DIR}/")

    # Show distribution
    print("\nBatch distribution:")
    for i, batch in enumerate(batches):
        companies = ', '.join(sorted(set(p['company'] for p in batch)))
        print(f"  Batch {i}: {len(batch)} PDFs ({companies})")


if __name__ == "__main__":
    main()
