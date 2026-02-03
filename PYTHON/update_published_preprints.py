#!/usr/bin/env python3
"""
Update metadata and rename papers that were preprints but are now published.
"""

import re
from pathlib import Path

from vault_config import PAPERS_DIR

# Mapping of unique substring in filename -> {metadata to update}
# If year changes, we will trigger a rename.
UPDATES = {
    "Man is to Computer Programmer": {
        "publication": "Proceedings of the 30th Conference on Neural Information Processing Systems (NIPS 2016)",
        "type": "conferencePaper",
        "year": "2016" # Matches
    },
    "TrolleyMod v1.0": {
        "publication": "Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES)",
        "type": "conferencePaper"
        # Year 2018 matches
    },
    "A Voting-Based System": {
        "publication": "Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence (AAAI-18)",
        "type": "conferencePaper",
        "year": "2018" # Matches
    },
    "Situational factors shape moral judgments": {
        "publication": "Nature Human Behaviour",
        "type": "journalArticle",
        "year": "2022" # Was 2019
    },
    "Aligning AI with Shared Human Values": {
        "publication": "International Conference on Learning Representations (ICLR 2021)",
        "type": "conferencePaper",
        "year": "2021" # Was 2020
    },
    "StereoSet": {
        "publication": "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL 2021)",
        "type": "conferencePaper",
        "year": "2021" # Was 2020
    },
    "All That's 'Human' Is Not Gold": {
        "publication": "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL 2021)",
        "type": "conferencePaper",
        "year": "2021" # Matches
    },
    "Scruples": {
        "publication": "Proceedings of the AAAI Conference on Artificial Intelligence (AAAI-21)",
        "type": "conferencePaper",
        "year": "2021" # Matches
    }
}

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', '', name)
    name = re.sub(r'[\n\r\t]', ' ', name)
    name = re.sub(r'\s+', ' ', name)
    return name.strip()

def get_frontmatter(content):
    if content.startswith('---'):
        end = content.find('\n---\n', 3)
        if end != -1:
            return content[3:end], content[end+5:]
    return None, content

def update_frontmatter_value(frontmatter_str, key, value):
    pattern = re.compile(f'^{key}:\\s*.*$', re.MULTILINE)
    replacement = f'{key}: "{value}"'
    if pattern.search(frontmatter_str):
        return pattern.sub(replacement, frontmatter_str)
    else:
        return frontmatter_str + f'\n{replacement}'

def main():
    files = list(PAPERS_DIR.glob('*.md'))
    count = 0
    
    for file_path in files:
        matched_key = None
        for key in UPDATES:
            if key in file_path.name:
                matched_key = key
                break
        
        if not matched_key:
            continue
            
        print(f"Updating {file_path.name}...")
        data = UPDATES[matched_key]
        
        try:
            content = file_path.read_text(encoding='utf-8')
            frontmatter_str, body = get_frontmatter(content)
            
            if not frontmatter_str:
                print(f"Skipping {file_path.name}, no frontmatter.")
                continue
            
            # Update key fields
            for k, v in data.items():
                frontmatter_str = update_frontmatter_value(frontmatter_str, k, v)
            
            new_content = f"---{frontmatter_str}\n---\n{body}"
            
            # Write content
            # Rename logic
            year_match = re.search(r'^year:\s*"(.*?)"', frontmatter_str, re.MULTILINE)
            year = year_match.group(1) if year_match else "NoYear"
            
            # We need strictly the new year if we updated it
            if 'year' in data:
                year = data['year']
            
            # Need strict components for rename
            short_title_match = re.search(r'^short_title:\s*"(.*?)"', frontmatter_str, re.MULTILINE)
            short_title = short_title_match.group(1) if short_title_match else "Untitled"
            
            first_author_match = re.search(r'^first_author:\s*"(.*?)"', frontmatter_str, re.MULTILINE)
            first_author = first_author_match.group(1) if first_author_match else "Unknown"
            
            if ',' in first_author:
                last_name = first_author.split(',')[0].strip()
            else:
                last_name = first_author.split(' ')[-1].strip()
                
            clean_year = sanitize_filename(year)
            clean_last_name = sanitize_filename(last_name)
            clean_short_title = sanitize_filename(short_title)
            
            new_filename = f"{clean_year}-{clean_last_name}-{clean_short_title}.md"
            new_path = PAPERS_DIR / new_filename
            
            if file_path.name != new_filename:
                new_path.write_text(new_content, encoding='utf-8')
                file_path.unlink()
                print(f"Renamed to {new_filename}")
                count += 1
            else:
                file_path.write_text(new_content, encoding='utf-8')
                print(f"Updated metadata in {new_filename}")
                count += 1
                
        except Exception as e:
            print(f"Error processing {file_path.name}: {e}")

    print(f"Processed {count} papers.")

if __name__ == "__main__":
    main()
