#!/usr/bin/env python3
"""
Check publication status of preprints using Semantic Scholar API.

LEARNINGS:
- Semantic Scholar API is effective for finding venue/year of ArXiv preprints.
- Rate limits (429) must be handled with backoff.
- Publication venue names should be filtered (ignore "ArXiv", "CoRR") to detect true updates.
"""

import re
import json
import time
import urllib.request
import urllib.error
from pathlib import Path

from vault_config import PAPERS_DIR
SEMANTIC_SCHOLAR_URL = "https://api.semanticscholar.org/graph/v1/paper/ArXiv:{paper_id}?fields=venue,year,publicationVenue,title,url,isOpenAccess,openAccessPdf"

def get_frontmatter(content):
    if content.startswith('---'):
        end = content.find('\n---\n', 3)
        if end != -1:
            return content[3:end], content[end+5:]
    return None, content

def extract_arxiv_id(frontmatter):
    # Try DOI first: 10.48550/arXiv.1607.06520 -> 1607.06520
    doi_match = re.search(r'doi:\s*"?10.48550/arXiv.([\d.]+)"?', frontmatter, re.IGNORECASE)
    if doi_match:
        return doi_match.group(1)
        
    # Try URL: http://arxiv.org/abs/1607.06520 -> 1607.06520
    url_match = re.search(r'url:\s*"?https?://arxiv.org/abs/([\d.]+)"?', frontmatter, re.IGNORECASE)
    if url_match:
        return url_match.group(1)
        
    return None

def fetch_semantic_scholar_data(arxiv_id):
    url = SEMANTIC_SCHOLAR_URL.format(paper_id=arxiv_id)
    try:
        req = urllib.request.Request(url)
        # Add User-Agent to avoid blocking
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)')
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None # Paper not found or ArXiv ID invalid for SS
        elif e.code == 429:
            print("Rate limit hit. Sleeping for 10s...")
            time.sleep(10)
            return fetch_semantic_scholar_data(arxiv_id) # Retry once
        else:
            print(f"Error fetching {arxiv_id}: {e}")
            return None
    except Exception as e:
        print(f"Error fetching {arxiv_id}: {e}")
        return None

def update_frontmatter_value(frontmatter_str, key, value):
    pattern = re.compile(f'^{key}:\\s*.*$', re.MULTILINE)
    replacement = f'{key}: "{value}"'
    if pattern.search(frontmatter_str):
        return pattern.sub(replacement, frontmatter_str)
    else:
        return frontmatter_str + f'\n{replacement}'

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', '', name)
    name = re.sub(r'[\n\r\t]', ' ', name)
    name = re.sub(r'\s+', ' ', name)
    return name.strip()

def main():
    files = list(PAPERS_DIR.glob('*.md'))
    count = 0
    updated_count = 0
    
    total_papers = len(files)
    print(f"Checking {total_papers} papers...")
    
    for i, file_path in enumerate(files, 1):
        try:
            content = file_path.read_text(encoding='utf-8')
            frontmatter_str, body = get_frontmatter(content)
            
            if not frontmatter_str: continue
            
            # Check if it is a preprint
            type_match = re.search(r'^type:\s*"?preprint"?', frontmatter_str, re.MULTILINE)
            if not type_match:
                continue
                
            arxiv_id = extract_arxiv_id(frontmatter_str)
            if not arxiv_id:
                # print(f"Skipping {file_path.name}: No ArXiv ID found.")
                continue
                
            print(f"[{i}/{total_papers}] Checking {file_path.name} (ArXiv:{arxiv_id})...")
            
            data = fetch_semantic_scholar_data(arxiv_id)
            if not data:
                time.sleep(4)
                continue
                
            # Check for publication venue (rest of logic same)
            venue_name = None
            if data.get('publicationVenue') and data['publicationVenue'].get('name'):
                venue_name = data['publicationVenue']['name']
            elif data.get('venue'):
                venue_name = data['venue']
                
            if venue_name and venue_name.lower() != 'arxiv' and venue_name.lower() != 'corr':
                # Published!
                year = str(data.get('year', ''))
                
                print(f"  -> Found publication: {venue_name} ({year})")
                
                # Update Metadata
                frontmatter_str = update_frontmatter_value(frontmatter_str, 'type', 'conferencePaper') # Default to conference
                frontmatter_str = update_frontmatter_value(frontmatter_str, 'publication', venue_name)
                if year:
                    frontmatter_str = update_frontmatter_value(frontmatter_str, 'year', year)
                
                # Update Content
                new_content = f"---{frontmatter_str}\n---\n{body}"
                
                # Rename Logic
                short_title_match = re.search(r'^short_title:\s*"(.*?)"', frontmatter_str, re.MULTILINE)
                short_title = short_title_match.group(1) if short_title_match else "Untitled"
                
                first_author_match = re.search(r'^first_author:\s*"(.*?)"', frontmatter_str, re.MULTILINE)
                first_author = first_author_match.group(1) if first_author_match else "Unknown"
                
                if ',' in first_author:
                    last_name = first_author.split(',')[0].strip()
                else:
                    last_name = first_author.split(' ')[-1].strip()
                
                # fallback year
                if not year:
                    year_match = re.search(r'^year:\s*"(.*?)"', frontmatter_str, re.MULTILINE)
                    year = year_match.group(1) if year_match else "NoYear"

                clean_year = sanitize_filename(year)
                clean_last_name = sanitize_filename(last_name)
                clean_short_title = sanitize_filename(short_title)
                
                new_filename = f"{clean_year}-{clean_last_name}-{clean_short_title}.md"
                new_path = PAPERS_DIR / new_filename
                
                if file_path.name != new_filename:
                    new_path.write_text(new_content, encoding='utf-8')
                    file_path.unlink()
                    print(f"  -> Renamed to {new_filename}")
                else:
                    file_path.write_text(new_content, encoding='utf-8')
                    print(f"  -> Updated metadata.")
                
                updated_count += 1
            else:
                pass
                # print(f"Still preprint.")
            
            time.sleep(4) # Rate limit politeness
            
        except Exception as e:
            print(f"Error processing {file_path.name}: {e}")

    print(f"Updated {updated_count} papers.")

if __name__ == "__main__":
    main()
