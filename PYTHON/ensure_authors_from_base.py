#!/usr/bin/env python3
"""
Sync 'authors' and 'first_author' metadata from Base.md to paper markdown files.
"""

import csv
import re
from pathlib import Path

from vault_config import PAPERS_DIR, WORKSPACE_ROOT

# Paths
BASE_MD_PATH = WORKSPACE_ROOT / 'Base.md'

def load_base_metadata():
    """Reads Base.md and returns a dictionary of {Key: {'authors': ..., 'year': ..., 'short_title': ..., 'title': ...}}."""
    metadata = {}
    try:
        with open(BASE_MD_PATH, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = row.get('Key')
                if key:
                    metadata[key] = {
                        'authors': row.get('Author', '').strip(),
                        'year': row.get('Publication Year', '').strip(),
                        'short_title_raw': row.get('Short Title', '').strip(),
                        'title': row.get('Title', '').strip(),
                        'url': row.get('Url', '').strip(),
                        'attachments': row.get('File Attachments', '').strip()
                    }
    except Exception as e:
        print(f"Error reading Base.md: {e}")
        return {}
    return metadata

def parse_frontmatter(content):
    """Parses YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return None, content
    
    end_match = re.search(r'\n---\n', content[3:])
    if not end_match:
        return None, content
        
    frontmatter_text = content[4:end_match.start() + 3]
    rest_of_content = content[end_match.end() + 3:]
    
    # Simple manual parsing to preserve structure where possible, but we'll rebuild it cleanly
    frontmatter = {}
    current_key = None
    current_value = []

    lines = frontmatter_text.split('\n')
    for line in lines:
        if not line.strip(): continue
        
        if line.startswith('  - '):  # List item
            if current_key:
                val = line.strip()[2:].strip().strip('"')
                current_value.append(val)
        elif ':' in line:
            # New key
            if current_key:
                if len(current_value) == 1:
                    frontmatter[current_key] = current_value[0]
                elif len(current_value) > 1:
                    frontmatter[current_key] = current_value
                else: 
                     # Handle empty empty values or empty lists if needed, 
                     # though our logic resets cur_val to []
                     pass

            key_part, _, val_part = line.partition(':')
            current_key = key_part.strip()
            val_part = val_part.strip().strip('"')
            if val_part:
                current_value = [val_part]
            else:
                current_value = []
    
    # Capture last key
    if current_key:
         if len(current_value) == 1:
            frontmatter[current_key] = current_value[0]
         elif len(current_value) > 1:
            frontmatter[current_key] = current_value
    
    return frontmatter, rest_of_content

def build_frontmatter(data):
    """Reconstructs YAML frontmatter string."""
    lines = ['---']
    
    # Preferred order
    key_order = ['key', 'type', 'short_title', 'year', 'first_author', 'authors', 'doi', 'tags']
    
    seen_keys = set()
    
    for key in key_order:
        if key in data:
            val = data[key]
            if isinstance(val, list):
                lines.append(f"{key}:")
                for item in val:
                    # Escape quotes if necessary
                    item_str = str(item).replace('"', '\\"')
                    lines.append(f'  - "{item_str}"')
            else:
                # Basic string value
                if val is None: val = ""
                val_str = str(val).replace('"', '\\"')
                lines.append(f'{key}: "{val_str}"')
            seen_keys.add(key)
            
    # Add remaining keys
    for key, val in data.items():
        if key not in seen_keys:
            if isinstance(val, list):
                lines.append(f"{key}:")
                for item in val:
                    item_str = str(item).replace('"', '\\"')
                    lines.append(f'  - "{item_str}"')
            else:
                if val is None: val = ""
                val_str = str(val).replace('"', '\\"')
                lines.append(f'{key}: "{val_str}"')
    
    lines.append('---')
    return '\n'.join(lines)

def generate_short_title(raw_short, title):
    """Generates a short title <= 50 chars."""
    # 1. Use Short Title if valid
    if raw_short and len(raw_short) <= 50:
        return raw_short
    
    # 2. Use Title if valid
    if title and len(title) <= 50:
        return title
        
    if title:
        # 3. Split by colon
        if ':' in title:
            first_part = title.split(':')[0].strip()
            if len(first_part) > 2 and len(first_part) <= 50:
                return first_part
        
        # 4. Split by space-hyphen-space
        if ' - ' in title:
            first_part = title.split(' - ')[0].strip()
            if len(first_part) > 2 and len(first_part) <= 50:
                return first_part
            
    # 5. Truncate Title
    if title:
        # Take first 50 chars
        truncated = title[:50]
        # Attempt to cut at last space to avoid splitting words
        last_space = truncated.rfind(' ')
        if last_space > 20: # Ensure we don't cut too short
            truncated = truncated[:last_space]
        
        return truncated.strip().rstrip('.,;:-')
        
    return "Untitled"

def update_paper(file_path, base_data):
    try:
        content = file_path.read_text(encoding='utf-8')
        frontmatter, body = parse_frontmatter(content)
        
        if frontmatter is None:
            print(f"Skipping {file_path.name}: No valid frontmatter found.")
            return False
            
        key = frontmatter.get('key')
        if not key:
            print(f"Skipping {file_path.name}: No 'key' found in frontmatter.")
            return False
            
        if key not in base_data:
            print(f"Warning: Key {key} from {file_path.name} not found in Base.md.")
            return False
            
        entry_data = base_data[key]
        full_authors = entry_data['authors']
        year = entry_data['year']
        raw_short = entry_data['short_title_raw']
        title = entry_data['title']
        
        # Calculate first author
        if ';' in full_authors:
            first_author = full_authors.split(';')[0].strip()
        else:
            first_author = full_authors.strip()
            
        # Generate Short Title
        short_title = generate_short_title(raw_short, title)
            
        # Update frontmatter
        # Only overwrite authors if Base has data. If Base is empty (Unknown), keep existing (enriched).
        if full_authors:
            frontmatter['authors'] = full_authors
            frontmatter['first_author'] = first_author
        elif 'authors' not in frontmatter:
             frontmatter['authors'] = ""
             frontmatter['first_author'] = ""
        if year:
             frontmatter['year'] = year
        frontmatter['short_title'] = short_title
        
        # Sync URL and PDF
        # We respect existing enriched data (e.g. from ACL) if present
        
        # 1. URL
        base_url = entry_data.get('url', '')
        if base_url and 'url' not in frontmatter:
            frontmatter['url'] = base_url
            
        # 2. PDF
        if 'pdf' not in frontmatter:
            # Try to derive from Base URL
            if base_url.endswith('.pdf'):
                frontmatter['pdf'] = base_url
            elif 'arxiv.org/abs/' in base_url:
                frontmatter['pdf'] = base_url.replace('/abs/', '/pdf/') + '.pdf'
            
            # If still no PDF, check File Attachments
            if 'pdf' not in frontmatter:
                attachments = entry_data.get('attachments', '')
                if attachments:
                    # distinct paths by semi-colon
                    paths = attachments.split(';')
                    for p in paths:
                        p = p.strip()
                        if p.endswith('.pdf'):
                            # Create file:// URI
                            frontmatter['pdf'] = f"file://{p}"
                            break
        
        new_frontmatter_str = build_frontmatter(frontmatter)
        new_content = new_frontmatter_str + '\n' + body
        
        file_path.write_text(new_content, encoding='utf-8')
        return True
        
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")
        return False

def main():
    print("Loading metadata from Base.md...")
    base_data = load_base_metadata()
    print(f"Loaded {len(base_data)} entries from Base.md.")
    
    updates_count = 0
    failures_count = 0
    
    paper_files = list(PAPERS_DIR.glob('*.md'))
    print(f"Found {len(paper_files)} markdown files in {PAPERS_DIR}.")
    
    for paper_file in paper_files:
        if update_paper(paper_file, base_data):
            updates_count += 1
        else:
            failures_count += 1
            
    print("-" * 30)
    print(f"Summary:")
    print(f"  Updated: {updates_count}")
    print(f"  Skipped/Failed: {failures_count}")

if __name__ == "__main__":
    main()
