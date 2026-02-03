import re
import json
import pathlib

REVIEW_FILE = pathlib.Path("STATISTICS/abstracts_for_review.md")
OUTPUT_FILE = pathlib.Path("STATISTICS/matched_papers_text.json")

# Reuse patterns from generate_semantic_report.py
SEMANTIC_PATTERNS = {
    # ... (Copied patterns for consistency, or I can just import if I refactored, but copy is safer 4 one-shot)
    "VIRTUE": [
        r"(virtue ethics)", r"(human flourishing)", r"(eudaimonia)", r"(moral character)", r"(aretaic)", r"(neo-aristotelian)"
    ],
    "DEONTOLOGY": [
        r"(deontology)", r"(deontological)", r"(kantian)", r"(categorical imperative)", r"(moral duty)", r"(moral rule)", r"(rights-based)", r"(duty-based)"
    ],
    "UTILITARIAN": [
        r"(utilitarian)", r"(consequentialis)", r"(greatest good)", r"(expected value).{0,50}(moral|ethics)"
    ],
    "ALIGN_CONSTITUTIONAL": [
        r"(constitutional ai)", r"(helpful, honest, and harmless)", r"(clara|anthropic|bai et al)", r"(alignment principles)", r"(rule-based alignment)"
    ],
    "ALIGN_RLHF": [
        r"(reinforcement learning from human feedback|rlhf)", r"(reward model)", r"(human preferences).{0,50}(optimization|learning)", r"(preference model)"
    ],
    "ALIGN_PLURALISM": [
        r"(pluralis)(m|tic)", r"(diverse values)", r"(cross-cultural).{0,50}(alignment|ethics)", r"(global).{0,50}(ethics|values)", r"(value variation)"
    ],
    "ALIGN_BENCHMARKS": [
        r"(benchmark).{0,50}(ethics|moral|alignment)", r"(dataset).{0,50}(ethics|moral|alignment)", r"(evaluating).{0,50}(alignment|ethics)", r"(metric).{0,50}(alignment|harm)"
    ],
    "ALIGN_GENERAL": [
        r"(value alignment)", r"(human values).{0,50}(alignment|ai)", r"(ai safety).{0,50}(values|ethics)", r"(machine ethics).{0,50}(general|field)"
    ]
}

def analyze_text_semantically(text):
    text_lower = text.lower()
    categories = set()
    for cat, patterns in SEMANTIC_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, text_lower):
                categories.add(cat)
    return categories

def main():
    if not REVIEW_FILE.exists():
        print(f"Error: {REVIEW_FILE} not found.")
        return

    content = REVIEW_FILE.read_text(encoding='utf-8')
    papers = []
    current_paper = {}
    current_text = ""
    
    lines = content.split('\n')
    for line in lines:
        if line.startswith("## Paper:"):
            if current_paper:
                # Analyze previous
                cats = analyze_text_semantically(current_text)
                if cats:
                    current_paper['categories'] = list(cats)
                    current_paper['text'] = current_text.strip()
                    papers.append(current_paper)
            
            current_paper = {"text": ""}
            current_text = ""
            parts = line.replace("## Paper:", "").strip().split('|')
            if len(parts) >= 3:
                current_paper["year"] = parts[0].strip()
                current_paper["author"] = parts[1].strip()
                current_paper["title"] = parts[2].strip()
                
        elif line.startswith("File:"):
             current_paper["link"] = line.replace("File:", "").strip()
        elif line.startswith("### Abstract") or line.startswith("### Detailed Summary") or line.startswith("---"):
            continue
        else:
            current_text += " " + line.strip()

    if current_paper:
         cats = analyze_text_semantically(current_text)
         if cats:
             current_paper['categories'] = list(cats)
             current_paper['text'] = current_text.strip()
             papers.append(current_paper)

    OUTPUT_FILE.write_text(json.dumps(papers, indent=2), encoding='utf-8')
    print(f"Dumped {len(papers)} matched papers to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
