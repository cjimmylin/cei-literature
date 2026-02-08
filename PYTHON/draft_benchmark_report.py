
import json
import pathlib
import re

INPUT_JSON = pathlib.Path("STATISTICS/20260124-benchmark_papers_list.json")
OUTPUT_MD = pathlib.Path("STATISTICS/20260124-paper-statistics-6.md")

def get_category(text):
    text = text.lower()
    if "toxicity" in text or "toxic" in text or "hate" in text or "offensive" in text or "harm" in text:
        return "Safety & Toxicity"
    if "bias" in text or "gender" in text or "stereotype" in text or "fairness" in text or "discrimination" in text:
        return "Bias & Fairness"
    if "moral" in text or "ethic" in text or "norm" in text or "value" in text:
        return "Morality & Values"
    if "hallucination" in text or "fact" in text or "truth" in text or "grounding" in text:
        return "Truthfulness & Hallucination"
    if "reasoning" in text or "qa" in text or "question" in text or "knowledge" in text:
        return "Reasoning & Knowledge"
    if "law" in text or "legal" in text or "policy" in text:
        return "Legal & Policy"
    if "speech" in text or "dialect" in text or "multilingual" in text:
        return "Multilingual & Cultural"
    return "General / Infrastructure"

def extract_conclusion(text):
    # Try to find the abstract text (usually inside quotes in text_preview)
    # The text_preview often has "Abstract ...".
    # Clean up newlines
    clean_text = text.replace("\n", " ")
    
    # Look for abstract-like content
    sentences = re.split(r'(?<=[.!?]) +', clean_text)
    
    # Try to find "result" or "conclu" sentences
    candidates = []
    for s in sentences:
        if any(w in s.lower() for w in ["find", "show", "conclude", "demonstrate", "result", "establish", "reveal"]):
            candidates.append(s)
            
    if candidates:
        # Return the last 2 candidates
        return " ".join(candidates[-2:]).strip().strip('"')
    
    # Fallback: Last sentence
    if sentences:
        return sentences[-1].strip().strip('"')
    return "N/A"

def parse_author_from_filename(filename):
    # Format: YYYY-Author-Title.md
    parts = filename.split('-')
    if len(parts) >= 2:
        return parts[1]
    return "Unknown"

def main():
    data = json.loads(INPUT_JSON.read_text(encoding='utf-8'))
    
    # Fix Authors
    for p in data:
        if p['author'] == "Unknown":
            # Extract from link/filename
            # Link is [[YYYY-Author-Title.md]]
            fname = p['link'].replace("[[", "").replace("]]", "")
            p['author'] = parse_author_from_filename(fname)

    # Sort by Year (desc) then Category
    data.sort(key=lambda x: (x.get('year', '0000'), x.get('title', '')), reverse=True)
    
    # Group by category
    categories = {
        "Safety & Toxicity": [],
        "Bias & Fairness": [],
        "Morality & Values": [],
        "Truthfulness & Hallucination": [],
        "Reasoning & Knowledge": [],
        "Multilingual & Cultural": [],
        "Legal & Policy": [],
        "General / Infrastructure": []
    }
    
    for paper in data:
        cat = get_category(paper['text_preview'] + " " + paper['title'])
        if cat in categories:
            categories[cat].append(paper)
        else:
            categories["General / Infrastructure"].append(paper)
        
    # Write Markdown
    lines = []
    lines.append("# Paper Statistics 6: Benchmarks & Quantitative Evaluations")
    lines.append(f"**Total Papers Identified**: {len(data)}")
    lines.append("**Method**: Keyword Search in Abstracts, Summaries, and PDF Extracts")
    lines.append("")
    lines.append("## Overview")
    lines.append("This report lists papers that provide **quantitative benchmarks, datasets, evaluation frameworks, or metrics** for AI alignment.")
    lines.append("")
    
    # Master Table
    lines.append("## 1. Master List by Category")
    for cat, papers in categories.items():
        if not papers: continue
        lines.append(f"### {cat} ({len(papers)})")
        lines.append("\n| Year | Author | Title |")
        lines.append("|------|--------|-------|")
        for p in papers:
            lines.append(f"| {p['year']} | {p['author']} | {p['link']} |")
        lines.append("")
        
    lines.append("## 2. Deep Dive Analysis")
    
    for cat, papers in categories.items():
        if not papers: continue
        lines.append(f"\n## {cat}")
        for p in papers:
            lines.append(f"\n### {p['year']} | {p['author']} | {p['link']}")
            
            # Semantic Analysis
            # Try to identify the benchmark name
            text = p['text_preview']
            
            # Simple heuristic for Approach
            approach = "Introduces/Uses a quantitative framework."
            match_snippets = [m.replace("Text Match: ", "") for m in p['matches'] if "Text Match" in m]
            if match_snippets:
                # excessive quotes cleanup
                snippet = match_snippets[0].strip('"').strip("'")
                approach = f"Key Contribution: *\"{snippet}\"*..." 
            
            conclusion = extract_conclusion(text)
            if len(conclusion) > 300: conclusion = conclusion[:300] + "..."
            
            lines.append(f"*   **Alignment Approach**: {approach}")
            lines.append(f"*   **Conclusion**: {conclusion}")
            lines.append(f"*   **Impact on Alignment**: Quantitative measurement of {cat.lower()}.")
            lines.append("")
            
    OUTPUT_MD.write_text("\n".join(lines), encoding='utf-8')
    print(f"Draft report written to {OUTPUT_MD}")

if __name__ == "__main__":
    main()
