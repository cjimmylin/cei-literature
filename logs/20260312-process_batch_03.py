#!/usr/bin/env python3
"""
Process batch 03 for cultural/language classification.
Reads each paper's abstract from YAML frontmatter and prints it for classification.
"""
import json, re, os

PAPERS_DIR = "papers"
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if False else "."

def extract_abstract(filepath):
    """Extract abstract from YAML frontmatter."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return f"ERROR: {e}"

    # Find YAML frontmatter
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return "NO FRONTMATTER"
    fm = m.group(1)

    # Extract abstract field
    # Handle multi-line abstract (indented or quoted)
    abstract_match = re.search(r'^abstract:\s*["\']?(.*?)(?:["\']?\s*$)', fm, re.MULTILINE)
    if abstract_match:
        abstract = abstract_match.group(1)
        # Check for multi-line (next lines start with spaces)
        lines = fm.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('abstract:'):
                # Collect continuation lines
                abstract_lines = [abstract]
                for j in range(i+1, len(lines)):
                    if lines[j].startswith('  ') or lines[j].startswith('\t'):
                        abstract_lines.append(lines[j].strip())
                    elif lines[j].strip() == '':
                        continue
                    else:
                        break
                abstract = ' '.join(abstract_lines)
                break
        return abstract.strip().strip('"').strip("'")

    # Try block scalar
    abstract_match = re.search(r'^abstract:\s*[|>]-?\s*\n((?:\s+.*\n?)+)', fm, re.MULTILINE)
    if abstract_match:
        return re.sub(r'\n\s+', ' ', abstract_match.group(1)).strip()

    return "NO ABSTRACT FOUND"

def extract_first_n_words(filepath, n=500):
    """Extract first n words from a PDF extract file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Skip frontmatter if present
        m = re.match(r'^---\s*\n.*?\n---\s*\n?', content, re.DOTALL)
        if m:
            content = content[m.end():]
        words = content.split()[:n]
        return ' '.join(words)
    except Exception as e:
        return f"ERROR: {e}"

with open('logs/20260312-cultural_language_batch_03.json') as f:
    batch = json.load(f)

# Print abstracts for papers where we need to determine classification
for i, p in enumerate(batch):
    fn = p['filename']
    paper_path = os.path.join(PAPERS_DIR, fn)
    abstract = extract_abstract(paper_path)
    print(f"=== [{i}] {fn} ===")
    print(f"Abstract: {abstract[:500]}")
    print(f"Current: culture={p['current_national_ethnic_cultural']}, cultures_list={p['current_cultures_nationalities_list']}, languages={p['current_languages_list']}")
    print()
