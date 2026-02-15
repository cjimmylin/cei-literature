#!/usr/bin/env python3
"""
Analyze batch 10 papers for religious tradition classification.
Deep-read each paper and PDF extract to determine if religious/ethical
traditions are substantively engaged.
"""

import json
import os
from pathlib import Path

WORKSPACE = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS")
BATCH_FILE = WORKSPACE / "logs/religious_audit_batches/batch_10.json"
PAPERS_DIR = WORKSPACE / "papers"
RESULTS_FILE = WORKSPACE / "logs/religious_audit_batches/results_agent_10.json"

def read_file_safe(filepath):
    """Read file safely, return content or None."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def main():
    # Load batch
    with open(BATCH_FILE) as f:
        batch = json.load(f)

    print(f"Loaded {len(batch)} papers from batch 10")

    # Process each paper
    for idx, item in enumerate(batch, 1):
        filename = item['filename']
        print(f"\n{'='*80}")
        print(f"Paper {idx}/{len(batch)}: {filename}")
        print(f"{'='*80}")

        # Read paper
        paper_path = PAPERS_DIR / filename
        paper_content = read_file_safe(paper_path)
        if paper_content:
            print(f"Paper: {len(paper_content)} chars")
            print(paper_content[:500])

        # Read extract if available
        if item['has_extract'] and item['pdf_extract_path']:
            extract_path = WORKSPACE / item['pdf_extract_path']
            extract_content = read_file_safe(extract_path)
            if extract_content:
                print(f"\nExtract: {len(extract_content)} chars")
                print(extract_content[:500])

        print(f"\nCandidate traditions: {item['candidate_traditions']}")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
