#!/usr/bin/env python3
"""
Batch download PDFs for new papers from arXiv.

Downloads PDFs for papers that have external_pdf URLs but no local_pdf set.
Uses curl for downloads and respects arXiv rate limits.

Usage: python3 PYTHON/batch_download_pdfs.py START END [--dry-run]
  START: 1-indexed position in the list of papers needing downloads
  END: 1-indexed position (inclusive)
  --dry-run: show what would be downloaded without downloading

Run from CEI-Lit-WS/ directory.
"""

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

# Configuration
PAPERS_DIR = Path("papers")
VAULT_CONFIG = Path(".vault-config.json")
DELAY_SECONDS = 3  # Delay between downloads (arXiv rate limiting)
MAX_RETRIES = 2
CURL_TIMEOUT = 60  # seconds


def get_pdfs_dir():
    """Get PDF storage directory from vault config."""
    config = json.loads(VAULT_CONFIG.read_text())
    return Path(config["pdf_path"])


def get_papers_needing_download():
    """Find all new papers with external_pdf but no local_pdf."""
    papers = []

    for f in sorted(PAPERS_DIR.glob("*.md")):
        content = f.read_text(encoding='utf-8')

        # Only process new papers from the exhaustive search import
        if 'DATE_ADDED: 20260207' not in content:
            continue

        # Check for external_pdf URL
        ext_match = re.search(r'external_pdf:\s*"(https?://[^"]+)"', content)
        if not ext_match:
            continue

        # Check if local_pdf already set (has a wikilink value)
        local_match = re.search(r'local_pdf:\s*"?\[\[', content)
        if local_match:
            continue  # Already has a local PDF

        external_url = ext_match.group(1)
        pdf_filename = f.stem + ".pdf"

        papers.append({
            'paper_path': f,
            'paper_name': f.name,
            'external_url': external_url,
            'pdf_filename': pdf_filename,
        })

    return papers


def download_pdf(url, output_path, retries=MAX_RETRIES):
    """Download a PDF using curl with retry logic."""
    for attempt in range(retries + 1):
        try:
            result = subprocess.run(
                [
                    "curl", "-sS", "-L",
                    "-o", str(output_path),
                    "-w", "%{http_code}",
                    "--max-time", str(CURL_TIMEOUT),
                    "--connect-timeout", "15",
                    "-H", "User-Agent: CEI-Literature-Vault/1.0 (Academic Research)",
                    url
                ],
                capture_output=True, text=True, timeout=CURL_TIMEOUT + 10
            )

            http_code = result.stdout.strip()

            if http_code == "200":
                # Verify file is actually a PDF (not an error page)
                if output_path.exists() and output_path.stat().st_size > 1000:
                    # Quick check: PDF files start with %PDF
                    with open(output_path, 'rb') as f:
                        header = f.read(5)
                    if header == b'%PDF-':
                        return True, "OK"
                    else:
                        output_path.unlink()
                        return False, f"Not a PDF (got HTML error page?)"
                elif output_path.exists():
                    size = output_path.stat().st_size
                    output_path.unlink()
                    return False, f"File too small ({size} bytes)"

            elif http_code == "429":
                # Rate limited — wait longer and retry
                if attempt < retries:
                    wait = 10 * (attempt + 1)
                    time.sleep(wait)
                    continue
                return False, f"HTTP 429 (rate limited after {retries} retries)"

            else:
                if output_path.exists():
                    output_path.unlink()
                return False, f"HTTP {http_code}"

        except subprocess.TimeoutExpired:
            if attempt < retries:
                time.sleep(5)
                continue
            return False, "Timeout"
        except Exception as e:
            return False, str(e)

    return False, "Max retries exceeded"


def update_local_pdf_field(paper_path, pdf_filename):
    """Add local_pdf field to paper's YAML frontmatter.

    Uses safe string insertion (NOT parse/rebuild round-trip).
    """
    content = paper_path.read_text(encoding='utf-8')

    # Insert local_pdf line after external_pdf line
    local_pdf_line = f'local_pdf: "[[PDFs/{pdf_filename}]]"'

    if 'external_pdf:' in content:
        # Insert after external_pdf line
        content = re.sub(
            r'(external_pdf:\s*"[^"]*"\n)',
            r'\1' + local_pdf_line + '\n',
            content,
            count=1
        )
    elif 'url:' in content:
        # Insert after url line
        content = re.sub(
            r'(url:\s*"[^"]*"\n)',
            r'\1' + local_pdf_line + '\n',
            content,
            count=1
        )
    else:
        # Insert before DATE_ADDED
        content = content.replace(
            'DATE_ADDED:',
            local_pdf_line + '\nDATE_ADDED:'
        )

    paper_path.write_text(content, encoding='utf-8')


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 PYTHON/batch_download_pdfs.py START END [--dry-run]")
        print("  START/END: positions in download queue (1-indexed, inclusive)")
        sys.exit(1)

    start = int(sys.argv[1])
    end = int(sys.argv[2])
    dry_run = '--dry-run' in sys.argv

    pdfs_dir = get_pdfs_dir()
    if not pdfs_dir.exists():
        print(f"ERROR: PDF directory not found: {pdfs_dir}")
        sys.exit(1)

    # Get all papers needing downloads
    all_papers = get_papers_needing_download()
    print(f"Total papers needing PDF download: {len(all_papers)}")

    # Select batch
    batch = all_papers[start - 1:end]
    print(f"Processing positions {start}-{end} ({len(batch)} papers)")
    if dry_run:
        print("*** DRY RUN MODE ***")
    print()

    downloaded = 0
    skipped = 0
    failed = 0

    for i, paper in enumerate(batch):
        pdf_path = pdfs_dir / paper['pdf_filename']

        # Skip if PDF already exists on disk
        if pdf_path.exists() and pdf_path.stat().st_size > 1000:
            print(f"  [{start + i:3d}] SKIP (exists): {paper['pdf_filename']}")
            skipped += 1
            continue

        if dry_run:
            print(f"  [{start + i:3d}] DRY RUN: {paper['pdf_filename']}")
            print(f"         URL: {paper['external_url']}")
            downloaded += 1
            continue

        # Download
        success, msg = download_pdf(paper['external_url'], pdf_path)

        if success:
            size_kb = pdf_path.stat().st_size / 1024
            print(f"  [{start + i:3d}] OK ({size_kb:.0f}KB): {paper['pdf_filename']}")
            downloaded += 1

            # Update paper's local_pdf field
            try:
                update_local_pdf_field(paper['paper_path'], paper['pdf_filename'])
            except Exception as e:
                print(f"         WARNING: Failed to update YAML: {e}")
        else:
            print(f"  [{start + i:3d}] FAIL ({msg}): {paper['pdf_filename']}")
            failed += 1

        # Rate limiting
        if i < len(batch) - 1:  # Don't sleep after last download
            time.sleep(DELAY_SECONDS)

    print(f"\n{'='*50}")
    print(f"BATCH {start}-{end} SUMMARY")
    print(f"  Downloaded: {downloaded}")
    print(f"  Skipped:    {skipped}")
    print(f"  Failed:     {failed}")
    print(f"{'='*50}")


if __name__ == '__main__':
    main()
