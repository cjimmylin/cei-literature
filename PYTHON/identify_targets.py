#!/usr/bin/env python3
"""
Identify Target Papers for Manual Enrichment

This script identifies papers that need manual attention based on classification gaps.
Specifically, it finds papers where:
- ethics_overall: Yes (paper touches on ethics)
- But NO specific framework (virtue, deontological, utilitarian) is identified
- AND the paper lacks a key_contribution field

These papers likely need manual review to properly classify their ethical perspective.

Usage:
    python3 PYTHON/identify_targets.py

Output:
    Prints count and first 10 target papers needing enrichment.
"""
from pathlib import Path
import re

from vault_config import PAPERS_DIR

def get_frontmatter(content):
    if content.startswith('---'):
        end = content.find('\n---\n', 3)
        if end != -1:
            return content[3:end]
    return ""

def main():
    files = list(PAPERS_DIR.glob('*.md'))
    targets = []
    
    for f in files:
        try:
            content = f.read_text(encoding='utf-8')
            fm = get_frontmatter(content)
            
            is_ethics = re.search(r'ethics_overall:\s*"Yes"', fm)
            is_virtue = re.search(r'virtue_ethics:\s*"Yes"', fm)
            is_deonto = re.search(r'deontological_ethics:\s*"Yes"', fm)
            is_util = re.search(r'utilitarian_ethics:\s*"Yes"', fm)
            
            if is_ethics and not (is_virtue or is_deonto or is_util):
                if 'key_contribution:' not in fm:
                    targets.append(f)
                
        except Exception:
            pass
            
    print(f"Total targets remaining: {len(targets)}")
    for t in targets[:10]:
        print(f" - {t.name}")

if __name__ == "__main__":
    main()
