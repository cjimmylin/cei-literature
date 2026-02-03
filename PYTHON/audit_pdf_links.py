#!/usr/bin/env python3
"""
Audit PDF Links - Comprehensive Link Validation Tool

This script audits the local_pdf field across all paper markdown files,
categorizing them by link status:

Categories:
- Valid: Properly formatted link pointing to existing PDF
- N/A: Explicitly marked as not available
- Missing Prefix: PDF exists but path missing "PDFs/" prefix
- File Not Found: Link points to non-existent PDF file
- Malformed: Link format is invalid
- Missing Field: No local_pdf field in frontmatter

Usage:
    python3 PYTHON/audit_pdf_links.py

Output:
    Summary statistics and detailed lists of issues needing attention.

Related Scripts:
    - find_unlinked_pdfs.py: Quick check for orphaned PDFs
    - fuzzy_match_pdfs.py: Find potential PDF-paper matches
"""
import re
from pathlib import Path
from vault_config import PAPERS_DIR, PDFS_DIR

def audit_links():
    papers_dir = PAPERS_DIR
    pdfs_dir = PDFS_DIR
    
    pdf_files = {f.name for f in pdfs_dir.glob("*.pdf")}
    paper_files = list(papers_dir.glob("*.md"))
    
    results = {
        "valid": [],
        "missing_prefix": [],
        "file_not_found": [],
        "na": [],
        "malformed": [],
        "missing_field": []
    }
    
    for paper in paper_files:
        try:
            # Using utf-8-sig to handle BOMs automatically
            with open(paper, 'r', encoding='utf-8-sig') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(paper, 'r', encoding='latin-1') as f:
                    content = f.read()
            except Exception as e:
                print(f"Error reading {paper.name}: {e}")
                continue
            
        # Match local_pdf: [[path]] or local_pdf: "[[path]]" or local_pdf: path
        match = re.search(r'^local_pdf:\s*(.*)$', content, re.MULTILINE)
        
        if not match:
            results["missing_field"].append(paper.name)
            continue
            
        raw_val = match.group(1).strip()
        link_val = raw_val.strip('"').strip("'")
        
        if link_val == "N/A" or not link_val:
            results["na"].append(paper.name)
            continue
            
        # Extract filename from wikilink [[...]]
        wiki_match = re.search(r'\[\[(.*?)\]\]', link_val)
        if wiki_match:
            link_path = wiki_match.group(1)
            # Remove any display text after |
            link_path = link_path.split('|')[0].strip()
        else:
            link_path = link_val
            
        if link_path.startswith("PDFs/"):
            clean_name = link_path[5:]
            if clean_name in pdf_files:
                results["valid"].append(paper.name)
            else:
                results["file_not_found"].append((paper.name, link_val))
        elif link_path.endswith(".pdf"):
             if link_path in pdf_files:
                 results["missing_prefix"].append((paper.name, link_val))
             else:
                 results["file_not_found"].append((paper.name, link_val))
        else:
            results["malformed"].append((paper.name, link_val))

    print(f"Total Papers: {len(paper_files)}")
    print(f"Valid Links: {len(results['valid'])}")
    print(f"N/A: {len(results['na'])}")
    print(f"Missing Prefix: {len(results['missing_prefix'])}")
    print(f"File Not Found: {len(results['file_not_found'])}")
    print(f"Malformed: {len(results['malformed'])}")
    print(f"Missing Field: {len(results['missing_field'])}")
    
    if results["missing_prefix"]:
        print("\nMissing Prefix Details (Paper: Current Value):")
        for p, l in results["missing_prefix"]:
            print(f"  {p}: {l}")
            
    if results["file_not_found"]:
        print("\nFile Not Found Details (Paper: Current Value):")
        for p, l in results["file_not_found"]:
            print(f"  {p}: {l}")

    if results["malformed"]:
        print("\nMalformed Details (Paper: Current Value):")
        for p, l in results["malformed"]:
            print(f"  {p}: {l}")

if __name__ == "__main__":
    audit_links()
