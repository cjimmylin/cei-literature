#!/usr/bin/env python3
"""Fetch abstracts for papers that are missing them."""

import re
import time
import urllib.request
import urllib.parse
from pathlib import Path
from xml.etree import ElementTree

# Import safe YAML utilities
from yaml_frontmatter_utils import read_paper, write_paper, reconstruct_content
from vault_config import PAPERS_DIR, WORKSPACE_ROOT

def get_arxiv_abstract(arxiv_url):
    """Fetch abstract from arXiv API."""
    # Extract arxiv ID from URL
    match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d+\.\d+)', arxiv_url)
    if not match:
        return None

    arxiv_id = match.group(1)
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            xml_data = response.read().decode('utf-8')

        # Parse XML
        root = ElementTree.fromstring(xml_data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}

        entry = root.find('atom:entry', ns)
        if entry is not None:
            summary = entry.find('atom:summary', ns)
            if summary is not None and summary.text:
                # Clean up the abstract
                abstract = summary.text.strip()
                abstract = re.sub(r'\s+', ' ', abstract)
                return abstract
    except Exception as e:
        print(f"    Error fetching from arXiv: {e}")
    return None

def extract_arxiv_url(content):
    """Extract arXiv URL from markdown content."""
    # Look for arXiv URL in Links section
    patterns = [
        r'\*\*arXiv\*\*:\s*(https?://arxiv\.org/[^\s\n]+)',
        r'\*\*Arxiv\*\*:\s*(https?://arxiv\.org/[^\s\n]+)',
        r'(https?://arxiv\.org/abs/\d+\.\d+)',
        r'(https?://arxiv\.org/pdf/\d+\.\d+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            return match.group(1)
    return None

def has_abstract(body):
    """Check if the markdown body has an abstract with content."""
    if '## Abstract' not in body:
        return False
    abstract_section = body.split('## Abstract')[1].split('##')[0].strip()
    return bool(abstract_section)

def add_abstract_to_md(filepath, abstract):
    """Add abstract to a markdown file using safe YAML utilities."""
    # Use safe YAML utilities to read the paper
    try:
        frontmatter, body = read_paper(filepath)
    except ValueError as e:
        print(f"    Error reading YAML: {e}")
        return False

    # Modify the body to add/update abstract
    if '## Abstract' in body:
        # Replace empty abstract section
        parts = body.split('## Abstract')
        before = parts[0]
        after_parts = parts[1].split('##', 1)
        rest = '##' + after_parts[1] if len(after_parts) > 1 else ''
        new_body = before + '## Abstract\n\n' + abstract + '\n\n' + rest
    elif '## Notes' in body:
        # Insert before Notes section
        new_body = body.replace('## Notes', f'## Abstract\n\n{abstract}\n\n## Notes')
    else:
        # Append at the end
        new_body = body + f'\n## Abstract\n\n{abstract}\n'

    # Use safe YAML utilities to write the paper
    try:
        write_paper(filepath, frontmatter, new_body, validate=True)
        return True
    except ValueError as e:
        print(f"    Error writing YAML: {e}")
        return False

def main():
    updated = 0
    no_abstract_found = []
    no_arxiv_url = []
    read_errors = []

    for md_file in sorted(PAPERS_DIR.glob('*.md')):
        # Use safe YAML utilities to read the paper
        try:
            frontmatter, body = read_paper(md_file)
            # Reconstruct full content for URL extraction (which may be in body or frontmatter)
            content = reconstruct_content(frontmatter, body)
        except (ValueError, FileNotFoundError) as e:
            read_errors.append((md_file.name, str(e)))
            continue

        if has_abstract(body):
            continue

        print(f"Processing: {md_file.name[:60]}...")

        arxiv_url = extract_arxiv_url(content)

        if not arxiv_url:
            print(f"  No arXiv URL found")
            no_arxiv_url.append(md_file.name)
            continue

        print(f"  Found arXiv URL: {arxiv_url}")
        abstract = get_arxiv_abstract(arxiv_url)
        time.sleep(0.3)  # Rate limit

        if abstract:
            if add_abstract_to_md(md_file, abstract):
                print(f"  Added abstract")
                updated += 1
            else:
                no_abstract_found.append(md_file.name)
                print(f"  Failed to write abstract")
        else:
            no_abstract_found.append(md_file.name)
            print(f"  Could not fetch abstract")

    print(f"\n{'='*50}")
    print(f"Updated {updated} papers with abstracts from arXiv")
    print(f"Papers without arXiv URL: {len(no_arxiv_url)}")
    print(f"Papers where fetch failed: {len(no_abstract_found)}")
    if read_errors:
        print(f"Papers with read errors: {len(read_errors)}")

    # Write lists
    with open(WORKSPACE_ROOT / 'missing_abstracts.txt', 'w') as f:
        f.write("=== Papers without arXiv URL ===\n")
        for name in no_arxiv_url:
            f.write(name + '\n')
        f.write("\n=== Papers where arXiv fetch failed ===\n")
        for name in no_abstract_found:
            f.write(name + '\n')
        if read_errors:
            f.write("\n=== Papers with YAML read errors ===\n")
            for name, error in read_errors:
                f.write(f"{name}: {error}\n")

if __name__ == "__main__":
    main()
