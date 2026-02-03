#!/usr/bin/env python3
"""
Identify authors with the most papers in the repository.
"""

import re
from pathlib import Path
from collections import Counter

from vault_config import PAPERS_DIR

def parse_frontmatter(content):
    """Simple parser for YAML frontmatter."""
    if not content.startswith('---'):
        return None
    end_match = re.search(r'\n---\n', content[3:])
    if not end_match:
        return None
    frontmatter_text = content[4:end_match.start() + 3]
    
    data = {}
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            data[key.strip()] = val.strip().strip('"')
    return data

def get_author_counts():
    """Counts papers per author by scanning markdown files."""
    counts = Counter()
    
    for paper_file in PAPERS_DIR.glob('*.md'):
        try:
            content = paper_file.read_text(encoding='utf-8')
            frontmatter = parse_frontmatter(content)
            if not frontmatter or 'authors' not in frontmatter:
                continue
            
            raw_authors = frontmatter['authors']
            if ';' in raw_authors:
                authors = [a.strip() for a in raw_authors.split(';')]
            elif ',' in raw_authors:
                # Be careful here, some names have commas (Last, First)
                # If we see "Last, First; Last, First", we already split by ;
                # If we see "Last, First, Last, First", it's ambiguous but usually Zotero uses ;
                # A simple heuristic: if there's no ; but there are multiple , then we might have a list or just one name with Last, First
                # Actually, Zotero export to CSV often uses commas if configured that way.
                # Let's check how populate_authors.py handles it.
                # populate_authors.py uses:
                # if ';' in raw_authors:
                #     authors = [a.strip() for a in raw_authors.split(';')]
                # else:
                #     authors = [a.strip() for a in raw_authors.split(',')]
                authors = [a.strip() for a in raw_authors.split(',')]
            else:
                authors = [raw_authors.strip()]
            
            seen_in_paper = set()
            for author in authors:
                if not author or author.lower() == 'unknown':
                    continue
                
                # Normalize author name (Laukkonen, Ruben E -> Ruben E Laukkonen)
                name = author
                if ',' in author:
                    parts = [p.strip() for p in author.split(',')]
                    if len(parts) == 2:
                        name = f"{parts[1]} {parts[0]}"
                
                if name not in seen_in_paper:
                    counts[name] += 1
                    seen_in_paper.add(name)
                    
        except Exception as e:
            # print(f"Error parsing {paper_file.name}: {e}")
            pass
            
    return counts

def main():
    counts = get_author_counts()
    print(f"Total Unique Authors: {len(counts)}")
    print("\nTop 20 Authors by Paper Count:\n")
    print(f"{'Author Name':<40} | {'Paper Count':<12}")
    print("-" * 55)
    for name, count in counts.most_common(20):
        print(f"{name:<40} | {count:<12}")

if __name__ == "__main__":
    main()
