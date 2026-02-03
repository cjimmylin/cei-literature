#!/usr/bin/env python3
"""
Add Review Metadata Script

Adds the following fields to the top of all paper frontmatters:
1. Human View (Default: "No")
2. Human View Date (Default: "")
3. Human View note (Default: "")
4. Not AI (Default: "No")

Preserves existing values if fields already exist.
Reorders frontmatter to ensure these are at the top.
"""

from pathlib import Path
import sys
import os

# Add the current directory to sys.path to ensure we can import the utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from yaml_frontmatter_utils import read_paper, write_paper, parse_frontmatter, rebuild_frontmatter
from vault_config import PAPERS_DIR

def add_review_metadata():
    if not PAPERS_DIR.exists():
        print(f"Error: papers directory not found at {PAPERS_DIR}")
        return

    print(f"Scanning papers in {PAPERS_DIR}...")
    
    # Define priority fields and defaults (Empty as requested)
    priority_fields = [
        ("Human View", ""),
        ("Human View Date", ""),
        ("Human View note", ""),
        ("Not AI", "")
    ]
    
    count = 0
    errors = 0
    
    files = list(PAPERS_DIR.glob('*.md'))
    total = len(files)
    
    for i, paper_path in enumerate(files):
        try:
            # Read paper
            try:
                frontmatter_str, body = read_paper(paper_path)
            except Exception as e:
                print(f"Skipping {paper_path.name}: {e}")
                errors += 1
                continue
                
            # Parse fields
            fields = parse_frontmatter(frontmatter_str)
            
            # Create new ordered dictionary
            new_fields = {}
            
            # 1. Add priority fields (top of file)
            for key, default_val in priority_fields:
                if key in fields:
                    # Preserve existing value
                    new_fields[key] = fields[key]
                    # Remove from source so we don't duplicate
                    del fields[key]
                else:
                    # Use default
                    new_fields[key] = default_val
            
            # 2. Add remaining fields
            for key, value in fields.items():
                new_fields[key] = value
                
            # Rebuild frontmatter
            new_frontmatter = rebuild_frontmatter(new_fields, preserve_order=True)
            
            # Write back
            write_paper(paper_path, new_frontmatter, body, validate=True)
            count += 1
            
            if i % 50 == 0:
                print(f"Processed {i}/{total} papers...")
                
        except Exception as e:
            print(f"Error processing {paper_path.name}: {e}")
            errors += 1
            
    print(f"\nComplete! Processed {count} papers. {errors} errors.")

if __name__ == "__main__":
    add_review_metadata()
