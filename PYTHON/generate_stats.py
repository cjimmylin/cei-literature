#!/usr/bin/env python3
"""
Generate Statistics Report
Scans all markdown papers and generates a markdown report with statistics.
See LLM_CONTEXT.md for details.
"""

import re
from pathlib import Path
from collections import defaultdict

def get_frontmatter_value(frontmatter: str, key: str) -> str:
    """Get value of a key from frontmatter."""
    match = re.search(rf'^{key}:\s*"?([^"\n]*)"?', frontmatter, re.MULTILINE)
    if match:
        val = match.group(1).strip()
        return val.strip('"\'')
    return ''

def main():
    papers_dir = Path('./papers')
    papers = list(papers_dir.glob('*.md'))
    
    # Storage for categories
    # Each list will contain tuples: (year, author_last_name, title, filename)
    stats = {
        'Virtue Ethics': [],
        'Deontological Ethics': [],
        'Utilitarian Ethics': [],
        'Ethics: AI Safety & Alignment': [],
        'Ethics: Bias & Fairness': [],
        'Ethics: Toxicity & Hate Speech': [],
        'Ethics: Moral Reasoning & Psychology': [],
        'Ethics: Truthfulness & Factuality': [],
        'Research Topic: Machine Learning': [],
        'Research Topic: NLP': [], 
        'Research Topic: QA': [],
        'Research Topic: AI Safety': [],
        'Religious: Christianity': [],
        'Religious: Islam': [],
        'Cultural: Chinese': [],
        'Cultural: American': [],
        'Moral Psych: Moral Foundations': [],
    }
    
    # Generic storage for dynamic categories
    perspectives = defaultdict(list)
    topics = defaultdict(list)
    religious = defaultdict(list)
    cultural = defaultdict(list)
    moral_psych = defaultdict(list)
    
    for p in sorted(papers):
        try:
            with open(p, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.startswith('---'):
                continue
            frontmatter = content.split('---')[1]
            
            # Extract Metadata
            title_match = re.search(r'short_title: "(.*?)"', frontmatter)
            title = title_match.group(1) if title_match else p.name
            
            year = get_frontmatter_value(frontmatter, 'year')
            if not year: year = "NoYear"
            
            first_author = get_frontmatter_value(frontmatter, 'first_author')
            # Extract last name (assume "Last, First" format)
            if ',' in first_author:
                author_last = first_author.split(',')[0].strip()
            else:
                author_last = first_author.strip()
            if not author_last: author_last = "Unknown"
            
            item = (year, author_last, title, p.name)

            # 1. Frameworks
            if get_frontmatter_value(frontmatter, 'virtue_ethics') == 'Yes':
                stats['Virtue Ethics'].append(item)
            if get_frontmatter_value(frontmatter, 'deontological_ethics') == 'Yes':
                stats['Deontological Ethics'].append(item)
            if get_frontmatter_value(frontmatter, 'utilitarian_ethics') == 'Yes':
                stats['Utilitarian Ethics'].append(item)
                
            # 2. Perspective
            persp = get_frontmatter_value(frontmatter, 'ethics_perspective')
            if persp and persp != 'N/A':
                perspectives[persp].append(item)
                
            # 3. Topic
            topic = get_frontmatter_value(frontmatter, 'research_topic')
            if topic and topic != 'N/A':
                topics[topic].append(item)
                
            # 4. Religious
            rel = get_frontmatter_value(frontmatter, 'religious_values')
            if rel and rel != 'N/A':
                religious[rel].append(item)
                
            # 5. Cultural
            cult = get_frontmatter_value(frontmatter, 'national_ethnic_cultural')
            if cult and cult != 'N/A':
                cultural[cult].append(item)
                
            # 6. Moral Psych
            mps = get_frontmatter_value(frontmatter, 'moral_psychology')
            if mps and mps != 'N/A':
                moral_psych[mps].append(item)
                
        except Exception as e:
            continue

    # Generate Report Content
    lines = []
    lines.append("# Paper Statistics Report")
    lines.append(f"\nTotal Papers Scanned: {len(papers)}")
    
    def add_section(header, data_dict):
        lines.append(f"\n## {header}")
        lines.append(f"Total Categories: {len(data_dict)}")
        
        # Sort categories by count desc
        sorted_cats = sorted(data_dict.items(), key=lambda x: len(x[1]), reverse=True)
        
        for cat, items in sorted_cats:
            lines.append(f"\n### {cat} ({len(items)})")
            
            # Sort items by Year (desc), then Author
            sorted_items = sorted(items, key=lambda x: (x[0], x[1]), reverse=True)
            
            for year, author, title, filename in sorted_items:
                # Format: Year, Last Name, [[Link|Title]]
                name_no_ext = str(filename).replace('.md', '')
                lines.append(f"- {year}, {author}, [[{name_no_ext}|{title}]]")

    # Frameworks (Merged into one dict for display)
    frameworks = {
        'Virtue Ethics': stats['Virtue Ethics'],
        'Deontological Ethics': stats['Deontological Ethics'],
        'Utilitarian Ethics': stats['Utilitarian Ethics']
    }
    add_section("Ethical Frameworks", frameworks)
    
    add_section("Ethical Perspectives (General Ethics)", perspectives)
    add_section("Research Topics (Non-Ethics)", topics)
    add_section("Religious Values", religious)
    add_section("Cultural Values", cultural)
    add_section("Moral Psychology", moral_psych)
    
    # Ensure STATISTICS directory exists
    stats_dir = Path('./STATISTICS')
    stats_dir.mkdir(exist_ok=True)

    with open(stats_dir / 'paper-statistics-1.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print("Report generated: STATISTICS/paper-statistics-1.md")

if __name__ == "__main__":
    main()
