#!/usr/bin/env python3
"""
PDF Workflow Orchestrator

Runs all PDF operations in the correct sequence:
1. Fix broken Zotero URLs (batch by batch)
2. Discover missing PDF links
3. Download all PDFs
4. Final verification

Usage:
    python3 PYTHON/pdf_workflow.py --full           # Run all operations
    python3 PYTHON/pdf_workflow.py --fix-zotero     # Only fix URLs
    python3 PYTHON/pdf_workflow.py --discover       # Only discover links
    python3 PYTHON/pdf_workflow.py --download       # Only download
    python3 PYTHON/pdf_workflow.py --verify         # Only verify
"""

import subprocess
from pathlib import Path
import time

from vault_config import WORKSPACE_ROOT
REPO_ROOT = WORKSPACE_ROOT

def run_command(cmd, description):
    """Run a command and report results."""
    print(f"\n{'='*80}")
    print(f"STEP: {description}")
    print(f"{'='*80}")
    print(f"Running: {' '.join(cmd)}\n")
    
    result = subprocess.run(cmd, cwd=REPO_ROOT)
    return result.returncode == 0

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="PDF Workflow Orchestrator")
    parser.add_argument('--full', action='store_true', help='Run all operations')
    parser.add_argument('--fix-zotero', action='store_true', help='Fix Zotero URLs')
    parser.add_argument('--discover', action='store_true', help='Discover missing links')
    parser.add_argument('--download', action='store_true', help='Download PDFs')
    parser.add_argument('--verify', action='store_true', help='Verify coverage')
    parser.add_argument('--batch-size', type=int, default=100, help='Batch size for operations')
    
    args = parser.parse_args()
    
    print(f"\n{'='*80}")
    print(f"PDF WORKFLOW ORCHESTRATOR")
    print(f"{'='*80}\n")
    
    start_time = time.time()
    
    success_count = 0
    total_steps = 0
    
    # Step 1: Fix Zotero URLs
    if args.full or args.fix_zotero:
        total_steps += 1
        if run_command(
            ['python3', 'PYTHON/smart_pdf_downloader.py', '--fix-zotero'],
            'Fix broken Zotero URLs (all 181 papers)'
        ):
            success_count += 1
        
        time.sleep(2)  # Give filesystem time to sync
    
    # Step 2: Discover missing links
    if args.full or args.discover:
        total_steps += 1
        if run_command(
            ['python3', 'PYTHON/smart_pdf_downloader.py', '--discover'],
            'Discover missing PDF links (all papers)'
        ):
            success_count += 1
        
        time.sleep(2)
    
    # Step 3: Download PDFs
    if args.full or args.download:
        total_steps += 1
        if run_command(
            ['python3', 'PYTHON/smart_pdf_downloader.py', '--download'],
            'Download all PDFs'
        ):
            success_count += 1
        
        time.sleep(2)
    
    # Step 4: Verification
    if args.full or args.verify:
        total_steps += 1
        if run_command(
            ['python3', 'PYTHON/smart_pdf_downloader.py', '--report'],
            'Final Status Report'
        ):
            success_count += 1
    
    # Summary
    elapsed = time.time() - start_time
    print(f"\n{'='*80}")
    print(f"WORKFLOW SUMMARY")
    print(f"{'='*80}")
    print(f"Steps completed: {success_count}/{total_steps}")
    print(f"Time elapsed: {int(elapsed)}s ({int(elapsed/60)}m)")
    print(f"Status: {'✓ SUCCESS' if success_count == total_steps else '⚠ PARTIAL'}")

if __name__ == "__main__":
    main()
