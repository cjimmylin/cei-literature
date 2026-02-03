#!/usr/bin/env python3
"""
Fuzzy Match PDFs - Smart PDF-Paper Pairing Tool

This script identifies potential matches between unlinked PDF files and
papers that don't have local PDF links, using fuzzy name matching.

Matching Strategies:
1. Exact match: PDF stem exactly matches paper stem
2. Prefix match: First 30 characters match
3. Substring match: One name contains the other

This helps resolve cases where PDFs were downloaded but not properly linked,
especially when filenames differ slightly due to renaming or normalization.

Usage:
    python3 PYTHON/fuzzy_match_pdfs.py

Output:
    Lists potential PDF-paper pairings for manual review and linkage.

Related Scripts:
    - audit_pdf_links.py: Full audit of link statuses
    - find_unlinked_pdfs.py: Find exact-match orphans
"""
import re
from pathlib import Path
from vault_config import PAPERS_DIR, PDFS_DIR

def find_fuzzy_matches():
    papers_dir = PAPERS_DIR
    pdfs_dir = PDFS_DIR
    
    pdf_files = {f.name: f for f in pdfs_dir.glob("*.pdf")}
    paper_files = list(papers_dir.glob("*.md"))
    
    unlinked_pdfs = set(pdf_files.keys())
    
    # Track valid links using the same logic as the audit script
    for paper in paper_files:
        with open(paper, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        
        match = re.search(r'^local_pdf:\s*(.*)$', content, re.MULTILINE)
        if not match:
            continue
            
        link_val = match.group(1).strip().strip('"').strip("'")
        
        wiki_match = re.search(r'\[\[(.*?)\]\]', link_val)
        if wiki_match:
            link_path = wiki_match.group(1).split('|')[0].strip()
        else:
            link_path = link_val
            
        if link_path.startswith("PDFs/"):
            clean_name = link_path[5:]
            if clean_name in unlinked_pdfs:
                unlinked_pdfs.remove(clean_name)
        elif link_path.endswith(".pdf"):
             if link_path in unlinked_pdfs:
                 unlinked_pdfs.remove(link_path)
    
    print(f"Total unlinked PDFs in folder: {len(unlinked_pdfs)}")
    if not unlinked_pdfs:
        return

    # Try fuzzy matching unlinked PDFs to papers that don't have a link
    papers_without_links = []
    for paper in paper_files:
        with open(paper, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        if "local_pdf:" not in content or "local_pdf: N/A" in content or not re.search(r'local_pdf: \S', content):
            papers_without_links.append(paper)
            
    print(f"Papers without links: {len(papers_without_links)}")
    
    for pdf_name in sorted(unlinked_pdfs):
        pdf_stem = pdf_name[:-4]
        # Look for a paper with a similar name
        for paper in papers_without_links:
            paper_stem = paper.stem
            # Check for exact matches first
            if pdf_stem == paper_stem:
                print(f"EXACT MATCH: {pdf_name} <-> {paper.name}")
            # Then fuzzy
            elif pdf_stem[:30] == paper_stem[:30] or pdf_stem in paper_stem or paper_stem in pdf_stem:
                print(f"Potential Match: {pdf_name} <-> {paper.name}")

if __name__ == "__main__":
    find_fuzzy_matches()
