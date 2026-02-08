
import re
import pathlib
import json

# Paths - use vault_config
from vault_config import PAPERS_DIR, PDF_EXTRACTS_DIR, STATISTICS_DIR
OUTPUT_JSON = STATISTICS_DIR / "20260124-benchmark_papers_list.json"

# Stricter Patterns for "Contribution" of a benchmark
# We want papers that PROVIDE/CREATE benchmarks, not just use them.
CONTRIBUTION_PATTERNS = [
    r"(introduce|propose|present|develop|construct|release|created|contribution).{0,100}(benchmark|dataset|framework|metric|suite|scale|test set|corpus)",
    r"(novel|new|comprehensive).{0,50}(benchmark|dataset|evaluation|metric)",
    r"(audit|evaluate|assess|measure|quantify).{0,50}(safety|alignment|ethics|morality|bias).{0,50}(using|via|with).{0,50}(benchmark|dataset|framework)",
    r"evaluation framework",
    r"quantitative assessment",
    r"safety benchmark"
]

TITLE_PATTERNS = [
    r"benchmark", r"dataset", r"evaluation", r"audit", r"metric", r"test suite", r"quantifying", r"measuring"
]

def get_pdf_content(year, author_last, title_short):
    """
    Tries to find the PDF extract for a given paper.
    """
    candidates = list(PDF_EXTRACTS_DIR.glob(f"{year}*{author_last}*"))
    for c in candidates:
        if title_short.lower() in c.name.lower():
            return c.read_text(encoding='utf-8')
    return ""

def analyze_paper(file_path):
    content = file_path.read_text(encoding='utf-8')
    
    # parse frontmatter
    metadata = {}
    lines = content.split('\n')
    yaml_block = []
    if lines[0] == '---':
        for line in lines[1:]:
            if line == '---':
                break
            yaml_block.append(line)
            
    for line in yaml_block:
        if ':' in line:
            key, val = line.split(':', 1)
            metadata[key.strip()] = val.strip()
                
    year = metadata.get('year', 'Unknown')
    author = metadata.get('author', 'Unknown')
    title = metadata.get('title', file_path.stem)
    
    # define search zone: Abstract + Title + Key Contribution (if exists) + Summary
    # We consciously exclude the full PDF text citation list to avoid false positives.
    # However, we check the PDF *Introduction* (first 3000 chars) if available.
    
    search_zones = []
    search_zones.append(title)
    search_zones.append(metadata.get('abstract', ''))
    search_zones.append(metadata.get('key_contribution', ''))
    
    # Get PDF Extract but only headers or intro
    author_last = author.split()[-1] if author else ""
    title_short = title[:15]
    pdf_text = get_pdf_content(year, author_last, title_short)
    if pdf_text:
        # Take first 4000 chars (Intro) and maybe look for "Method" headers
        search_zones.append(pdf_text[:5000])
    
    full_search_text = "\n".join(search_zones)
    
    matches = []
    
    # Check Title (Strong signal)
    if any(re.search(p, title, re.IGNORECASE) for p in TITLE_PATTERNS):
        matches.append("Title Match")
        
    # Check Contribution Patterns in text
    for pattern in CONTRIBUTION_PATTERNS:
        match = re.search(pattern, full_search_text, re.IGNORECASE)
        if match:
            matches.append(f"Text Match: {match.group(0)[:50]}...")
            
    if matches:
        return {
            "year": year,
            "author": author,
            "title": title,
            "link": f"[[{file_path.name}]]",
            "matches": matches,
            "text_preview": full_search_text[:4000] # Context for deep dive gen
        }
    return None

def main():
    results = []
    print(f"Scanning papers in {PAPERS_DIR}...")
    
    files = sorted(list(PAPERS_DIR.glob("*.md")))
    for f in files:
        if f.name == "README.md" or f.name == "TEMPLATE.md":
            continue
            
        data = analyze_paper(f)
        if data:
            results.append(data)
            
    print(f"Found {len(results)} potential benchmark papers.")
    OUTPUT_JSON.write_text(json.dumps(results, indent=2), encoding='utf-8')
    print(f"Saved to {OUTPUT_JSON}")

if __name__ == "__main__":
    main()
