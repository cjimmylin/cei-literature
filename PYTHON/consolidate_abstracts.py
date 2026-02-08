import os
import re
from pathlib import Path

# Paths
PAPERS_DIR = Path("papers")
STATISTICS_DIR = Path("STATISTICS")
OUTPUT_FILE = STATISTICS_DIR / "20260124-abstracts_for_review.md"

def get_frontmatter_and_content(content):
    match = re.search(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return "", content

def extract_field(frontmatter, key):
    match = re.search(fr'{key}: "(.*?)"', frontmatter)
    if match:
        return match.group(1)
    match = re.search(fr'{key}: (.*?)$', frontmatter, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ""

def get_abstract(content):
    # Try to find abstract in content
    match = re.search(r'## Abstract\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def get_summary(content):
    # Try to find detailed summary
    match = re.search(r'## Detailed Summary\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def main():
    if not STATISTICS_DIR.exists():
        STATISTICS_DIR.mkdir()

    output_lines = []
    output_lines.append("# Abstracts and Summaries for Semantic Review")
    output_lines.append(f"Generated: {os.popen('date').read().strip()}")
    output_lines.append("\n---\n")

    files = sorted(list(PAPERS_DIR.glob("*.md")))
    print(f"Processing {len(files)} papers...")

    count_with_abstract = 0
    count_with_summary = 0

    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                full_text = f.read()
            
            fm, body = get_frontmatter_and_content(full_text)
            
            year = extract_field(fm, "year") or "Unknown"
            author = extract_field(fm, "author") or "Unknown"
            title = extract_field(fm, "title") or filepath.stem
            
            # Clean author name (remove [[ ]])
            if author:
                author = author.replace("[[", "").replace("]]", "")

            # 1. Get Abstract (prefer frontmatter 'abstract' if exists, else markdown section)
            abstract = extract_field(fm, "abstract")
            if not abstract:
                abstract = get_abstract(body)
            
            # 2. Get Summary
            summary = get_summary(body)
            
            # Filter: If neither exists, skip? Or print "No info"?
            # User wants to read to determine match. If no text, we can't determine.
            # But we should output metadata so I know it was skipped?
            # Actually, most papers have at least extracted phrases or title. 
            # Let's include if there is ANY text tokens related to ethics/AI to keep file size manageable?
            # User said "Do not just use text matching". 
            # I will include ALL papers that match a very broad "AI" or "Ethics" keyword in the whole file
            # to avoid dumping 500 empty files.
            
            # Broad pre-filter for "AI" or "Ethics" or "Values" just to be sane
            if not re.search(r'(AI|Artificial Intelligence|Language Model|Alignment|Safety|Ethics|Moral|Value|Bias|Fairness)', full_text, re.IGNORECASE):
                continue

            output_lines.append(f"## Paper: {year} | {author} | {title}")
            output_lines.append(f"File: [[{filepath.name}]]")
            
            if abstract:
                count_with_abstract += 1
                output_lines.append("\n### Abstract")
                output_lines.append(abstract)
            else:
                output_lines.append("\n### Abstract")
                output_lines.append("(No abstract found)")

            if summary:
                count_with_summary += 1
                output_lines.append("\n### Detailed Summary")
                output_lines.append(summary)
            
            output_lines.append("\n---\n")

        except Exception as e:
            print(f"Error reading {filepath}: {e}")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(output_lines))

    print(f"Processed {len(files)} papers.")
    print(f"Papers with Abstracts: {count_with_abstract}")
    print(f"Papers with Summaries: {count_with_summary}")
    print(f"Output generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
