#!/usr/bin/env python3
"""
Enrich papers with metadata from ACL Anthology.
"""

import re
import json
import time
import urllib.request
from pathlib import Path

# Import safe YAML utilities
from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter
from vault_config import PAPERS_DIR

def get_acl_url(content):
    """Finds ACL Anthology URL in content."""
    match = re.search(r'(https://aclanthology.org/[a-zA-Z0-9.\-]+/?)', content)
    if match:
        return match.group(1).rstrip('/') + '/' # Ensure trailing slash for consistency
    return None

def fetch_page(url):
    """Fetches ACL page content."""
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_metadata(html):
    """Extracts metadata from ACL Anthology HTML."""
    metadata = {}
    
    # 1. Extract paper_params JSON
    # const paper_params={...};
    params_match = re.search(r'const paper_params\s*=\s*(\{.*?\});', html, re.DOTALL)
    if params_match:
        try:
            # weak JSON parsing because keys aren't quoted in the JS const usually?
            # actually keys in the curl output were NOT quoted: const paper_params={anthology_id:"..."}
            # Standard json.loads won't parse unquoted keys.
            # We need to quote keys or use a regex to extract fields manually.
            js_obj = params_match.group(1)
            
            # ID
            id_m = re.search(r'anthology_id:\s*"(.*?)"', js_obj)
            if id_m: metadata['anthology_id'] = id_m.group(1)
            
            # Title
            title_m = re.search(r'title:\s*"(.*?)"', js_obj)
            if title_m: 
                # Decode potential XML/HTML formatting in title like <fixed-case>
                t = title_m.group(1)
                t = re.sub(r'<[^>]+>', '', t)
                metadata['title'] = t
                
            # Abstract
            # Abstract might span lines or have quotes.
            # Regex for abstract is tricky if it contains quotes.
            # But the sample showed abstract:"..."
            # We'll try to capture it.
            # If standard regex fails, we fall back to finding id="paperAbstract" value in HTML (form input)
            pass 
        except Exception:
            pass

    # Fallback/Reliable way: Parse HTML attributes
    
    # Abstract (value attribute of hidden input or textarea)
    # <textarea ... id="paperAbstract"> ... </textarea> ? In the curl it was:
    # document.getElementById("paperAbstract").value=paper_params.abstract
    # So it uses JS to populate.
    # We must extract from JS string `abstract:"..."`.
    
    # Let's try capturing abstract from JS
    abs_match = re.search(r'abstract:\s*"(.*?)"', html, re.DOTALL) # Simple regex might fail on escaped quotes
    if abs_match:
        metadata['abstract'] = abs_match.group(1).replace('\\"', '"').replace('\\n', ' ')
        
    # Authors
    # authors:[{first:"...",last:"...",id:"..."},...]
    # We can regex for `authors:\[(.*?)\]`
    authors_match = re.search(r'authors\s*:\s*\[(.*?)\]', html, re.DOTALL)
    if authors_match:
        authors_json = authors_match.group(1)
        # Parse individual objects {first:"...",last:"..."}
        author_list = []
        for am in re.finditer(r'\{first:"(.*?)",last:"(.*?)"', authors_json):
            first = am.group(1)
            last = am.group(2)
            # Handle empty first name?
            full = f"{last}, {first}" if first else last
            author_list.append(full)
        metadata['authors_list'] = author_list
    
    # PDF Link
    # <a class="badge badge-primary ..." href="2021.emnlp-main.587.pdf">
    # or document.getElementById("paperPDF").href="..."
    pdf_match = re.search(r'id="paperPDF" href="(.*?)"', html) # From JS
    if not pdf_match:
        # Try finding link ending in .pdf
        pdf_match = re.search(r'href="([^"]+\.pdf)" class="badge badge-primary', html)
        
    if pdf_match:
        metadata['pdf_url'] = pdf_match.group(1)
        if not metadata['pdf_url'].startswith('http'):
            # It might be relative? ACL usually absolute in JS or relative in HTML.
            # If "2021.pdf", need base. But JS showed "https://aclanthology.org/..."
            pass
            
    # DOI
    # <a href="https://doi.org/..." class="badge badge-secondary ...">
    doi_match = re.search(r'href="(https://doi.org/[^"]+)"', html)
    if doi_match:
        metadata['doi_url'] = doi_match.group(1)
        
    # BibTeX
    # <pre id="citeBibtexContent" ...> ... </pre>
    # Content usually inside.
    bib_match = re.search(r'<pre id="citeBibtexContent"[^>]*>(.*?)</pre>', html, re.DOTALL)
    if bib_match:
        metadata['bibtex'] = bib_match.group(1).strip()
        # Extract BibKey from BibTeX
        # @inproceedings{curry-etal-2021-convabuse,
        key_match = re.search(r'@\w+\{(.*?),', metadata['bibtex'])
        if key_match:
            metadata['bibkey'] = key_match.group(1)
            
    return metadata

def update_paper(file_path, metadata, original_url):
    # Use safe YAML utilities
    try:
        frontmatter, body = read_paper(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return
    
    # Update Frontmatter Keys
    # Authors
    if 'authors_list' in metadata and metadata['authors_list']:
        full_authors = '; '.join(metadata['authors_list'])
        first_author = metadata['authors_list'][0].split(',')[0].strip() # Check if comma exists
        if ',' in metadata['authors_list'][0]:
             first_author = metadata['authors_list'][0].split(',')[0].strip() # "Last" from "Last, First"
        else:
             first_author = metadata['authors_list'][0].strip() # "Last" if just "Last"
        
        # Regex update
        # authors: ...
        if re.search(r'^authors:', frontmatter, re.MULTILINE):
            frontmatter = re.sub(r'^authors:.*$', f'authors: "{full_authors}"', frontmatter, flags=re.MULTILINE)
        else:
            frontmatter += f'\nauthors: "{full_authors}"'
            
        if re.search(r'^first_author:', frontmatter, re.MULTILINE):
            frontmatter = re.sub(r'^first_author:.*$', f'first_author: "{first_author}"', frontmatter, flags=re.MULTILINE)
        else:
            frontmatter += f'\nfirst_author: "{first_author}"'
            
    # URL / DOI / PDF / BibKey
    if 'doi_url' in metadata and 'doi:' not in frontmatter:
        # Extract purely the DOI value 10.xxx
        doi_val = metadata['doi_url'].replace('https://doi.org/', '')
        frontmatter += f'\ndoi: "{doi_val}"'
        
    if 'bibkey' in metadata:
        frontmatter += f'\nbibkey: "{metadata["bibkey"]}"'
        
    if original_url:
        if 'url:' not in frontmatter:
            frontmatter += f'\nurl: "{original_url}"'
            
    if 'pdf_url' in metadata:
        frontmatter += f'\npdf: "{metadata["pdf_url"]}"'

    # Update Body
    # Add Abstract if not present
    if 'abstract' in metadata:
        if '## Abstract' not in body:
            body += f'\n\n## Abstract\n\n{metadata["abstract"]}'
        else:
            # Maybe replace? User said "get all the information".
            # The existing file might have a placeholder text or empty abstract.
            # We'll just update it if it looks placeholder-y or just append it?
            # Safer to append or Replace if explicitly requested. 
            # Current papers have "## Abstract" followed by text.
            # I will Replace the Abstract section content.
            # Logic: Find ## Abstract, find next ## or end. Replace text in between.
            pattern = r'(## Abstract\s*\n)(.*?)(\n##|\Z)'
            # Use DOTALL for content
            # Wait, regex replace on body might be tricky if content is large.
            # I'll just append a note or replace if I can matching perfectly.
            # Actually, most files I saw had "## Abstract" populated? Or "No abstract available"?
            # `2021-ConvAbuse` had "*No abstract available in source.*"
            # So replacing is GOOD.
            body = re.sub(pattern, f'\\1{metadata["abstract"]}\n\\3', body, flags=re.DOTALL)
            
    # Add BibTeX
    if 'bibtex' in metadata:
        if '## BibTeX' not in body:
            body += f'\n\n## BibTeX\n\n```bibtex\n{metadata["bibtex"]}\n```'
            
    # Validate and write back using safe utility
    is_valid, issues = validate_frontmatter(frontmatter)
    if not is_valid:
        print(f"  Warning: YAML validation issues in {file_path.name}: {issues}")

    write_paper(file_path, frontmatter, body, validate=True)
    print(f"Updated {file_path.name}")


def main():
    files = list(PAPERS_DIR.glob('*.md'))
    count = 0
    
    for file_path in files:
        content = file_path.read_text(encoding='utf-8')
        acl_url = get_acl_url(content)
        
        if acl_url:
            print(f"Fetching {acl_url} for {file_path.name}...")
            html = fetch_page(acl_url)
            if html:
                metadata = extract_metadata(html)
                update_paper(file_path, metadata, acl_url)
                count += 1
                time.sleep(0.5) # Be nice to ACL
            else:
                print("Failed to fetch page.")
                
    print(f"Enriched {count} papers.")

if __name__ == "__main__":
    main()
