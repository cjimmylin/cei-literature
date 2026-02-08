
import json
import pathlib
import re

# Input: The existing broad list (we will use this as the candidate pool)
INPUT_LIST = pathlib.Path("STATISTICS/20260124-benchmark_papers_list.json")
# Output: A text file for the agent to read
OUTPUT_TEXT = pathlib.Path("STATISTICS/20260124-candidates_for_review.txt")
PAPERS_DIR = pathlib.Path("papers")

def get_full_content(paper_entry):
    link = paper_entry.get('link', '')
    # Extract filename from [[Filename.md]]
    match = re.search(r'\[\[(.*?)\]\]', link)
    if not match:
        return "No filename found."
    
    filename = match.group(1)
    file_path = PAPERS_DIR / filename
    
    if not file_path.exists():
        return "File not found."
    
    content = file_path.read_text(encoding='utf-8')
    
    # Extract Abstract and potentially Summary sections
    # Heuristic: extracting content between frontmatter and end or headers
    
    # Remove frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    
    # Limit to first 2000 characters to capture Abstract + Intro/Contribution
    # (Abstracts are usually at the top)
    return content[:2500].replace("\n", " ")

def main():
    if not INPUT_LIST.exists():
        print("Input list not found.")
        return

    data = json.loads(INPUT_LIST.read_text(encoding='utf-8'))
    
    # Sort for consistent variability
    data.sort(key=lambda x: x.get('year', '0000'), reverse=True)
    
    with open(OUTPUT_TEXT, 'w', encoding='utf-8') as f:
        f.write(f"CANDIDATE PAPERS FOR REVIEW ({len(data)} papers)\n")
        f.write("==================================================\n\n")
        
        for i, paper in enumerate(data):
            f.write(f"ID: {i}\n")
            f.write(f"PAPER: {paper['year']} | {paper['author']} | {paper['title']}\n")
            
            full_text = get_full_content(paper)
            f.write(f"CONTENT: {full_text}\n")
            f.write("-" * 80 + "\n\n")
            
    print(f"Compiled {len(data)} papers into {OUTPUT_TEXT}")

if __name__ == "__main__":
    main()
