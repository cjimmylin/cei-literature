import os
import re
from pathlib import Path
from typing import Dict, List

# Constants
# PDF extracts location
PDF_EXTRACTS_DIR = Path("PDF Extracts")
STATISTICS_DIR = Path("STATISTICS")
OUTPUT_FILE = STATISTICS_DIR / "20260124-ethics_snippets_review.md"

# Context window size (characters before and after match)
CONTEXT_WINDOW = 300

# Regex Patterns

# 1. AI/Alignment Context (Required within the file)
# We can check this globally for the file first to filter out totally irrelevant papers
AI_CONTEXT_PATTERNS = [
    r"\b(AI|artificial intelligence|machine learning|deep learning|LLM|large language model|neural network)\b",
    r"\b(alignment|safety|value alignment|robustness|steerability|control problem)\b",
    r"\b(agent|system|bot|assistant|model)\b"
]

# 2. Key Terms to Search For (and extract context around)
PATTERNS = {
    "VIRTUE": [
        r"\b(virtue ethics?)\b",
        r"\b(aristotle|aristotelian|eudaimonia|phronesis|flourishing)\b",
        r"\b(virtuous agent|character trait|moral character)\b",
        r"\b(wisdom|courage|temperance|justice)\b"
    ],
    "DEONTOLOGY": [
        r"\b(deonotolog[a-z]*)\b", 
        r"\b(kant|kantian|categorical imperative)\b",
        r"\b(duty|duties|obligation|obligations|rule-based ethics)\b",
        r"\b(rights-based|moral rule|moral constraint)\b",
        r"\b(rossian|prima facie dut[yi])\b"
    ],
    "UTILITARIAN": [
        r"\b(utilitarian[a-z]*)\b",
        r"\b(consequentialis[a-z]*)\b",
        r"\b(mill|bentham|sidgwick)\b",
        r"\b(utility function|maximize utility|maximize welfare|aggregate well-being)\b",
        r"\b(greatest good|hedonic calculus)\b"
    ]
}

def load_file_content(filepath: Path) -> str:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return ""

def extract_metadata(content: str) -> Dict[str, str]:
    metadata = {}
    source_match = re.search(r'source_pdf: "(.*?)"', content)
    if source_match:
        source_pdf = source_match.group(1)
        # Assuming format YYYY-Author-Title.pdf
        parts = source_pdf.replace('.pdf', '').split('-', 2)
        if len(parts) >= 3:
            metadata['year'] = parts[0]
            metadata['author'] = parts[1]
            metadata['title'] = parts[2]
            metadata['filename'] = source_pdf.replace('.pdf', '')
        else:
            metadata['year'] = "Unknown"
            metadata['author'] = "Unknown"
            metadata['title'] = source_pdf.replace('.pdf', '')
            metadata['filename'] = source_pdf.replace('.pdf', '')
    return metadata

def check_patterns(text: str, patterns: List[str]) -> bool:
    text_lower = text.lower()
    for pattern in patterns:
        if re.search(pattern, text_lower):
            return True
    return False

def get_snippets(text: str, category: str, patterns: List[str]) -> List[str]:
    """finds matches and extracts context."""
    text_lower = text.lower()
    snippets = []
    
    # We want unique snippets, so if multiple keywords appear close, 
    # we might get overlapping snippets. For this review script, 
    # simple distinct matches are fine.
    
    for pattern in patterns:
        for match in re.finditer(pattern, text_lower):
            start = max(0, match.start() - CONTEXT_WINDOW)
            end = min(len(text), match.end() + CONTEXT_WINDOW)
            
            # Get original text snippet
            snippet = text[start:end].replace('\n', ' ')
            
            # Clean up whitespace
            snippet = re.sub(r'\s+', ' ', snippet).strip()
            
            # Highlight the match (markdown bold)
            # Find the match in the snippet (ignoring case for find, but strictly replacing usually fails with simple replace)
            # Regex replacement on the snippet is safer
            snippet_marked = re.sub(
                match.group(0), 
                f"**{match.group(0).upper()}**", 
                snippet, 
                flags=re.IGNORECASE, 
                count=1
            )
            
            snippets.append(snippet_marked)
            
            # Cap matches per category per file to avoid huge dumps
            if len(snippets) >= 3: 
                break
        if len(snippets) >= 3:
            break
            
    return snippets

def main():
    if not OUTPUT_FILE.parent.exists():
        OUTPUT_FILE.parent.mkdir(parents=True)
        
    output_lines = []
    output_lines.append("# Ethics Snippets Review")
    output_lines.append(f"Generated: {os.popen('date').read().strip()}")
    output_lines.append("\n---\n")
    
    count = 0
    paper_matches = 0
    
    files = sorted(list(PDF_EXTRACTS_DIR.glob("*.md")))
    
    print(f"Scanning {len(files)} extracts...")
    
    for file_path in files:
        count += 1
        content = load_file_content(file_path)
        
        # 1. Global Filter: Must have AI/Alignment context
        has_ai = check_patterns(content, [r"\b(AI|artificial intelligence|LLM|language model)\b"])
        has_align = check_patterns(content, [r"\b(alignment|safety|value|ethics|control)\b"])
        
        if not (has_ai and has_align):
            continue
            
        metadata = extract_metadata(content)
        paper_snippets = {}
        has_any_match = False
        
        # 2. Extract Snippets for each category
        for category, patterns in PATTERNS.items():
            snippets = get_snippets(content, category, patterns)
            if snippets:
                paper_snippets[category] = snippets
                has_any_match = True
        
        if has_any_match:
            paper_matches += 1
            output_lines.append(f"## Paper: {metadata.get('year')} | {metadata.get('author')} | {metadata.get('title')}")
            output_lines.append(f"Link: [[{metadata.get('filename')}]]")
            
            for cat, snips in paper_snippets.items():
                output_lines.append(f"\n### {cat}")
                for s in snips:
                    output_lines.append(f"- \"...{s}...\"")
            
            output_lines.append("\n---\n")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(output_lines))
        
    print(f"Scanned {count} files.")
    print(f"Found {paper_matches} potentially relevant papers.")
    print(f"Review file generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
