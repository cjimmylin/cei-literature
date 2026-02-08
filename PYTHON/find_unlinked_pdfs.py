#!/usr/bin/env python3
"""
Find Unlinked PDFs - Orphan Detection Tool

This script identifies PDFs in the PDFs/ directory that exist but are not
properly linked in their corresponding paper markdown files.

It detects papers where:
- The local_pdf field is missing or set to N/A
- BUT a PDF file with the same stem name exists in PDFs/

This helps find orphaned PDFs that should be linked to their papers.

Usage:
    python3 PYTHON/find_unlinked_pdfs.py

Output:
    Lists paper-PDF pairs where linkage should be added.

Related Scripts:
    - audit_pdf_links.py: Full audit of all PDF link statuses
    - fuzzy_match_pdfs.py: Find potential matches using fuzzy name matching
"""
from pathlib import Path
from vault_config import PAPERS_DIR, PDFS_DIR

def find_unlinked_pdfs():
    papers_dir = PAPERS_DIR
    pdfs_dir = PDFS_DIR
    
    pdf_files = {f.name for f in pdfs_dir.rglob("*.pdf")}
    paper_files = list(papers_dir.glob("*.md"))
    
    unlinked_found = []
    
    for paper in paper_files:
        with open(paper, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "local_pdf:" not in content or "local_pdf: N/A" in content:
            # Expected PDF name is the same as the paper name but with .pdf
            expected_pdf = paper.stem + ".pdf"
            if expected_pdf in pdf_files:
                unlinked_found.append((paper.name, expected_pdf))
                
    print(f"Papers with missing/NA local_pdf but existing PDF file: {len(unlinked_found)}")
    for p, f in unlinked_found:
        print(f"  {p} -> {f}")

if __name__ == "__main__":
    find_unlinked_pdfs()
