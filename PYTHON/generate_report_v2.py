#!/usr/bin/env python3
"""
Generate a detailed statistics report (20260119-paper-statistics-2.md) for Cultural, Religious, and Moral Psych classifications.

LEARNINGS / DESIGN DECISIONS:
- Format: "Year, Author, [[Filename|Title]]" per user preference.
- Scans all files in papers/ to ensure latest metadata (including fixed years) is used.
"""

import re
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

sys.path.insert(0, str(Path(__file__).parent))
from moral_psych_scoring import (
    MP_FIELDS, FIELD_DISPLAY_NAMES, is_mp_detected, parse_mp_value,
)
from religious_scoring import (
    RV_FIELDS,
    FIELD_DISPLAY_NAMES as RV_DISPLAY_NAMES,
    is_rv_detected,
    parse_rv_value,
)

from vault_config import PAPERS_DIR, STATISTICS_DIR

OUTPUT_FILE = STATISTICS_DIR / "20260119-paper-statistics-2.md"

def extract_frontmatter(text: str) -> Dict[str, str]:
    """Extract YAML frontmatter as a dictionary."""
    if not text.startswith("---"):
        return {}
    
    end_match = re.search(r'\n---\s*\n', text[3:])
    if not end_match:
        return {}
    
    end_pos = end_match.end() + 3
    raw_frontmatter = text[4:end_pos-4].strip()
    
    frontmatter_dict = {}
    for line in raw_frontmatter.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            frontmatter_dict[key] = val
            
    return frontmatter_dict

def get_clean_values(fm: Dict[str, str], key: str) -> List[str]:
    """Get list of values for a key, ignoring N/A."""
    val = fm.get(key, 'N/A')
    if val in ['N/A', 'Unknown', 'None', '']:
        return []
    
    # helper to split comma separated values
    values = [v.strip() for v in val.split(',')]
    return [v for v in values if v and v not in ['N/A', 'Unknown']]

def extract_metadata(content: str, filename: str) -> Tuple[str, str, str]:
    """Extract (Year, Author, Title) from content."""
    fm = extract_frontmatter(content)
    
    # Year
    year = fm.get('year', 'NoYear')
    
    # Author
    author = "Unknown"
    if 'first_author' in fm:
        # "Bolukbasi, Tolga" -> "Bolukbasi"
        author = fm['first_author'].split(',')[0].strip()
    elif 'authors' in fm:
        author = fm['authors'].split(';')[0].split(',')[0].strip()
    
    # Title
    title = fm.get('short_title', filename.replace('.md', ''))
    
    return year, author, title

def main():
    papers = list(PAPERS_DIR.glob("*.md"))
    
    # Data Structures
    # category -> {value -> [(year, author, title, filename)]}
    stats = {
        "National / Ethnic / Cultural Values": defaultdict(list),
        "Religious Values": defaultdict(list),
        "Religious Values (Per-Tradition)": defaultdict(list),
        "Moral Psychology": defaultdict(list),
        "Moral Psychology (Per-Theory)": defaultdict(list),
    }
    
    total_tagged_papers = set()
    
    for paper in sorted(papers):
        try:
            with open(paper, 'r', encoding='utf-8') as f:
                content = f.read()
            
            fm = extract_frontmatter(content)
            name = paper.name
            
            year, author, title = extract_metadata(content, name)
            item = (year, author, title, name)
            
            # Cultural
            for val in get_clean_values(fm, 'national_ethnic_cultural'):
                stats["National / Ethnic / Cultural Values"][val].append(item)
                total_tagged_papers.add(name)
                
            # Religious — prefer rv_* scores, fall back to religious_values string
            rv_detected_any = False
            for rv_field in RV_FIELDS:
                rv_val = fm.get(rv_field, '')
                if is_rv_detected(rv_val):
                    tradition_name = RV_DISPLAY_NAMES[rv_field]
                    stats["Religious Values (Per-Tradition)"][tradition_name].append(item)
                    rv_detected_any = True
            if rv_detected_any:
                stats["Religious Values"]["Detected (from rv_* scores)"].append(item)
                total_tagged_papers.add(name)
            else:
                # Fallback: read religious_values string (legacy)
                for val in get_clean_values(fm, 'religious_values'):
                    stats["Religious Values"][val].append(item)
                    total_tagged_papers.add(name)
                
            # Psych — prefer mp_* scores, fall back to moral_psychology string
            mp_detected_any = False
            for mp_field in MP_FIELDS:
                mp_val = fm.get(mp_field, '')
                if is_mp_detected(mp_val):
                    theory_name = FIELD_DISPLAY_NAMES[mp_field]
                    stats["Moral Psychology (Per-Theory)"][theory_name].append(item)
                    mp_detected_any = True
            if mp_detected_any:
                stats["Moral Psychology"]["Detected (from mp_* scores)"].append(item)
                total_tagged_papers.add(name)
            else:
                # Fallback: read moral_psychology string (legacy)
                for val in get_clean_values(fm, 'moral_psychology'):
                    stats["Moral Psychology"][val].append(item)
                    total_tagged_papers.add(name)
                
        except Exception as e:
            print(f"Error processing {paper.name}: {e}")
            
    # Generate Markdown
    lines = []
    lines.append("# Paper Statistics Report 2")
    lines.append(f"\n**Total Papers in Vault:** {len(papers)}")
    lines.append(f"**Total Papers with at least one Cultural/Religious/Psych Classification:** {len(total_tagged_papers)}")
    
    for category, findings in stats.items():
        lines.append(f"\n## {category}")
        
        # Sort values by count descending
        sorted_values = sorted(findings.items(), key=lambda x: (-len(x[1]), x[0]))
        
        for val, paper_list in sorted_values:
            lines.append(f"\n### {val} ({len(paper_list)} papers)")
            
            # Sort papers by Year (desc) then Author
            sorted_papers = sorted(paper_list, key=lambda x: (x[0], x[1]), reverse=True)
            
            for year, author, title, filename in sorted_papers:
                name_no_ext = filename.replace('.md', '')
                # Format: - Year, Author, [[Filename|Title]]
                lines.append(f"- {year}, {author}, [[{name_no_ext}|{title}]]")
                
    # Ensure STATISTICS directory exists
    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"Report generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
