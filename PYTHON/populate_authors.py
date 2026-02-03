#!/usr/bin/env python3
"""
Populate the Authors CRM by extracting authors from paper markdown files.
"""

import re
from pathlib import Path

from vault_config import PAPERS_DIR, AUTHORS_DIR

# Template path
TEMPLATE_PATH = AUTHORS_DIR / 'TEMPLATE.md'

def get_author_files():
    """Returns a set of existing author names (filenames without .md)."""
    return {f.stem for f in AUTHORS_DIR.glob('*.md') if f.name not in ('README.md', 'TEMPLATE.md')}

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

def extract_authors_from_papers():
    """Maps author names to a list of paper wikilinks."""
    author_map = {} # {AuthorName: [PaperWikilink, ...]}
    
    for paper_file in PAPERS_DIR.glob('*.md'):
        try:
            content = paper_file.read_text(encoding='utf-8')
            frontmatter = parse_frontmatter(content)
            if not frontmatter or 'authors' not in frontmatter:
                continue
            
            # Format: "Author 1; Author 2; Author 3" or "Author 1, Author 2"
            raw_authors = frontmatter['authors']
            if ';' in raw_authors:
                authors = [a.strip() for a in raw_authors.split(';')]
            else:
                authors = [a.strip() for a in raw_authors.split(',')]
            
            title = frontmatter.get('short_title') or paper_file.stem
            wikilink = f"[[{paper_file.stem}|{title}]]"
            
            for author in authors:
                if not author or author.lower() == 'unknown':
                    continue
                # Normalize author name (Laukkonen, Ruben E -> Ruben E Laukkonen)
                # But for now, let's keep them as they are or do simple reversal if comma exists
                name = author
                if ',' in author:
                    parts = [p.strip() for p in author.split(',')]
                    if len(parts) == 2:
                        name = f"{parts[1]} {parts[0]}"
                
                if name not in author_map:
                    author_map[name] = []
                author_map[name].append(wikilink)
        except Exception as e:
            print(f"Error parsing {paper_file.name}: {e}")
            
    return author_map

def create_author_file(name, papers):
    """Creates a new author file from template."""
    # Sanitize name for filename
    safe_name = name.strip().replace('/', '-').replace('\\', '-').replace(':', '-')
    if not safe_name:
        return
        
    author_file = AUTHORS_DIR / f"{safe_name}.md"
    if author_file.exists():
        # Update existing file (simplified: just append new papers if not present)
        content = author_file.read_text(encoding='utf-8')
        new_papers = []
        for paper in papers:
            if paper not in content:
                new_papers.append(paper)
        
        if new_papers:
            if '## Papers in this Vault' in content:
                parts = content.split('## Papers in this Vault')
                papers_section = parts[1]
                for p in new_papers:
                    papers_section = f"\n- {p}" + papers_section
                content = parts[0] + '## Papers in this Vault' + papers_section
                author_file.write_text(content, encoding='utf-8')
        return

    # Use template for new file
    template = TEMPLATE_PATH.read_text(encoding='utf-8')
    content = template.replace('Full Name', name)
    content = content.replace('name: "Full Name"', f'name: "{name}"')
    
    papers_list = "\n".join([f"- {p}" for p in sorted(papers)])
    content = content.replace('- [[PaperFilename|Paper Title]]', papers_list)
    
    author_file.write_text(content, encoding='utf-8')
    print(f"Created author: {name}")

def main():
    print("Extracting authors from papers...")
    author_map = extract_authors_from_papers()
    print(f"Found {len(author_map)} unique authors.")
    
    if not TEMPLATE_PATH.exists():
        print("Error: TEMPLATE.md not found.")
        return

    for name, papers in author_map.items():
        create_author_file(name, papers)

if __name__ == "__main__":
    main()
