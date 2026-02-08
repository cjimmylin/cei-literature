import os
import re
from pathlib import Path
from typing import Dict, List, Set

# Constants
PDF_EXTRACTS_DIR = Path("PDF Extracts")
STATISTICS_DIR = Path("STATISTICS")
OUTPUT_FILE = STATISTICS_DIR / "20260124-paper-statistics-4.md"

# Regex Patterns for Classification
# 1. Context Filter: Must discuss AI/Optimization/Alignment
CONTEXT_PATTERNS = [
    r"\b(AI|artificial intelligence|machine learning|deep learning|LLM|large language model|neural network)\b",
    r"\b(alignment|safety|value alignment|robustness|steerability|control problem)\b",
    r"\b(agent|system|bot|assistant|model)\b"
]

# 2. General Normative Ethics Filter
NORMATIVE_PATTERNS = [
    r"\b(normative|ethical theory|ethical system|moral theory|moral philosophy|value system)\b",
    r"\b(ethics|morality|moral status|moral standing|moral patient)\b"
]

# 3. Specific Frameworks
# (a) Virtue Ethics
VIRTUE_ETHICS_PATTERNS = [
    r"\b(virtue ethics?)\b",
    r"\b(aristotle|aristotelian|eudaimonia|phronesis|flourishing)\b",
    r"\b(virtuous agent|character trait|moral character)\b",
    r"\b(wisdom|courage|temperance|justice)\b"  # Cardinal virtues in context
]

# (b) Deontology
DEONTOLOGY_PATTERNS = [
    r"\b(deonotolog[a-z]*)\b", # Catch deontology/deological
    r"\b(kant|kantian|categorical imperative)\b",
    r"\b(duty|duties|obligation|obligations|rule-based ethics)\b",
    r"\b(rights-based|moral rule|moral constraint)\b",
    r"\b(rossian|prima facie dut[yi])\b"
]

# (c) Utilitarianism/Consequentialism
UTILITARIAN_PATTERNS = [
    r"\b(utilitarian[a-z]*)\b",
    r"\b(consequentialis[a-z]*)\b",
    r"\b(mill|bentham|sidgwick)\b",
    r"\b(utility function|maximize utility|maximize welfare|aggregate well-being)\b",
    r"\b(greatest good|hedonic calculus)\b"
]

def load_file_content(filepath: Path) -> str:
    """Reads the content of a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return ""

def extract_metadata(content: str) -> Dict[str, str]:
    """Extracts basic metadata from the PDF extract frontmatter."""
    metadata = {}
    
    # Extract source PDF name to parse year/author/title
    source_match = re.search(r'source_pdf: "(.*?)"', content)
    if source_match:
        source_pdf = source_match.group(1)
        # Assuming format YYYY-Author-Title.pdf
        parts = source_pdf.replace('.pdf', '').split('-', 2)
        if len(parts) >= 3:
            metadata['year'] = parts[0]
            metadata['author'] = parts[1]
            metadata['title'] = parts[2]
            metadata['filename'] = source_pdf.replace('.pdf', '') # Base filename for wikilink
        else:
             # Fallback
            metadata['year'] = "Unknown"
            metadata['author'] = "Unknown"
            metadata['title'] = source_pdf.replace('.pdf', '')
            metadata['filename'] = source_pdf.replace('.pdf', '')

    return metadata

def check_patterns(text: str, patterns: List[str]) -> bool:
    """Checks if any pattern in the list exists in the text (case-insensitive)."""
    text_lower = text.lower()
    for pattern in patterns:
        if re.search(pattern, text_lower):
            return True
    return False

def analyze_papers():
    """Main analysis function."""
    
    classification = {
        "set_1_all": [],
        "virtue": [],
        "deontology": [],
        "utilitarian": []
    }
    
    print(f"Scanning PDF extracts in {PDF_EXTRACTS_DIR}...")
    
    count = 0
    match_count = 0
    
    # Iterate through all .md files in PDF Extracts
    for file_path in PDF_EXTRACTS_DIR.glob("*.md"):
        count += 1
        content = load_file_content(file_path)
        
        # Check Context (Must have AI + Alignment terms)
        # We need simpler logic: does it mention AI AND (Alignment OR Safety)?
        has_ai = check_patterns(content, [r"\b(AI|artificial intelligence|LLM|language model)\b"])
        has_alignment = check_patterns(content, [r"\b(alignment|safety|value|ethics|control)\b"])
        
        if not (has_ai and has_alignment):
            continue
            
        # Check General Normative Relevance
        # It must either match general normative terms OR specific frameworks
        is_normative = check_patterns(content, NORMATIVE_PATTERNS)
        is_virtue = check_patterns(content, VIRTUE_ETHICS_PATTERNS)
        is_deontology = check_patterns(content, DEONTOLOGY_PATTERNS)
        is_utilitarian = check_patterns(content, UTILITARIAN_PATTERNS)
        
        # Define "Set Number 1" criteria:
        # User asked for "papers that discuss using normative ethical systems for values alignment"
        # So we include if it matches general normative terms OR any specific school
        if is_normative or is_virtue or is_deontology or is_utilitarian:
            metadata = extract_metadata(content)
            entry = {
                "year": metadata.get('year', 'Unknown'),
                "author": metadata.get('author', 'Unknown'),
                "title": metadata.get('title', 'Unknown'),
                "link": f"[[{metadata.get('filename', 'Unknown')}|{metadata.get('title', 'Unknown')}]]"
            }
            
            classification["set_1_all"].append(entry)
            match_count += 1
            
            if is_virtue:
                classification["virtue"].append(entry)
            if is_deontology:
                classification["deontology"].append(entry)
            if is_utilitarian:
                classification["utilitarian"].append(entry)

    # Sort lists by Year desc, then Author
    for key in classification:
        classification[key].sort(key=lambda x: (x['year'], x['author']), reverse=True)

    print(f"Scanned {count} files.")
    print(f"Found {match_count} papers relevant to Normative Ethics for AI Alignment.")
    
    generate_report(classification, match_count, count)

def generate_report(classification, match_count, total_scanned):
    """Generates the markdown report."""
    
    lines = []
    lines.append("# Paper Statistics 4: Normative Ethical Systems for AI Alignment")
    lines.append("")
    lines.append(f"**Total Papers Scanned:** {total_scanned}")
    lines.append(f"**Identified Set 1 Papers:** {match_count}")
    lines.append(f"**Generated:** {os.popen('date').read().strip()}")
    lines.append("")
    lines.append("## Overview")
    lines.append("This report identifies papers that discuss using **normative ethical systems** (Virtue Ethics, Deontology, Utilitarianism) for AI/LLM value alignment.")
    lines.append("")
    
    # 1. Master List
    lines.append("## 1. Master List: All Normative Ethics Papers for AI Alignment")
    lines.append(f"*(Total: {len(classification['set_1_all'])})*")
    lines.append("")
    lines.append("| Year | Author | Title |")
    lines.append("|------|--------|-------|")
    for paper in classification['set_1_all']:
        lines.append(f"| {paper['year']} | {paper['author']} | {paper['link']} |")
    lines.append("")
    
    # 2. Sub-lists
    lines.append("## 2. Breakdown by Ethical School")
    lines.append("")
    
    # (a) Virtue Ethics
    lines.append(f"### (a) Virtue Ethics")
    lines.append(f"*(Count: {len(classification['virtue'])})*")
    lines.append("| Year | Author | Title |")
    lines.append("|------|--------|-------|")
    if not classification['virtue']:
        lines.append("| - | - | None identified |")
    for paper in classification['virtue']:
        lines.append(f"| {paper['year']} | {paper['author']} | {paper['link']} |")
    lines.append("")
    
    # (b) Deontological Ethics
    lines.append(f"### (b) Deontological Ethics")
    lines.append(f"*(Count: {len(classification['deontology'])})*")
    lines.append("| Year | Author | Title |")
    lines.append("|------|--------|-------|")
    if not classification['deontology']:
        lines.append("| - | - | None identified |")
    for paper in classification['deontology']:
        lines.append(f"| {paper['year']} | {paper['author']} | {paper['link']} |")
    lines.append("")
    
    # (c) Utilitarian / Consequentialist Ethics
    lines.append(f"### (c) Utilitarian & Consequentialist Ethics")
    lines.append(f"*(Count: {len(classification['utilitarian'])})*")
    lines.append("| Year | Author | Title |")
    lines.append("|------|--------|-------|")
    if not classification['utilitarian']:
        lines.append("| - | - | None identified |")
    for paper in classification['utilitarian']:
        lines.append(f"| {paper['year']} | {paper['author']} | {paper['link']} |")
    lines.append("")

    # Write to file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
        
    print(f"Report generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    analyze_papers()
