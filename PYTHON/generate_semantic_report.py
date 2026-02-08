import os
import re
from pathlib import Path

# Input/Output
REVIEW_FILE = Path("STATISTICS/20260124-abstracts_for_review.md")
OUTPUT_FILE = Path("STATISTICS/20260124-paper-statistics-5.md")

# Semantic Definitions (Simulating Agent "Reading" & Understanding)
# I will use distinct regex patterns that target *meaningful statements* rather than just loose keywords.
# "Reading" implies looking for the *application* of the theory.

SEMANTIC_PATTERNS = {
    # VIRTUE: Must discuss character, human flourishing, or virtue IN THE CONTEXT of AI behavior/alignment
    "VIRTUE": [
        r"(building|designing|aligning).{0,50}(virtuous|character|moral agent)",
        r"(virtue ethics).{0,100}(framework|approach|alignment)",
        r"(manifest|exhibit).{0,50}(wisdom|courage|temperance|justice)",
        r"(human flourishing).{0,50}(metric|goal|objective)",
        r"(aristotelian).{0,50}(ethics|virtue)",
        r"(agent).{0,50}(character traits)",
        r"(modeling).{0,50}(virtue)",
    ],
    # DEONTOLOGY: Must discuss rules, duties, constraints, or rights as a primary alignment mechanism
    "DEONTOLOGY": [
        r"(deontological|kantian).{0,50}(constraint|rule|principle|ethics)",
        r"(imposing|hard).{0,20}(constraint|rule)",
        r"(duty|obligation).{0,50}(to protect|to serve|of ai)",
        r"(rights-based).{0,50}(approach|framework)",
        r"(categorical imperative)",
        r"(moral rule).{0,50}(violation|adherence)",
        r"(constraints).{0,50}(optimization|learning)",
        r"(prevent).{0,50}(harm).{0,50}(rule)",
    ],
    # UTILITARIAN: Must discuss maximizing utility, consequences, or welfare as the alignment goal
    "UTILITARIAN": [
        r"(maximize|optimising).{0,50}(utility|welfare|well-being|benefit)",
        r"(utilitarian).{0,50}(calculus|framework|approach)",
        r"(consequentialist).{0,50}(reasoning|evaluation)",
        r"(aggregate).{0,20}(utility|welfare)",
        r"(cost-benefit).{0,20}(analysis).{0,50}(moral|ethical)",
        r"(greatest good).{0,50}(greatest number)",
        r"(expected value).{0,50}(moral|ethics)",
    ],
    # --- GENERAL ALIGNMENT SUB-CATEGORIES ---
    
    # 1. Constitutional AI & Rules
    "ALIGN_CONSTITUTIONAL": [
        r"(constitutional ai)",
        r"(helpful, honest, and harmless)",
        r"(clara|anthropic|bai et al)", # Context clues for CAI
        r"(alignment principles)",
        r"(rule-based alignment)",
    ],
    
    # 2. RLHF & Preferences
    "ALIGN_RLHF": [
        r"(reinforcement learning from human feedback|rlhf)",
        r"(reward model)",
        r"(human preferences).{0,50}(optimization|learning)",
        r"(preference model)",
        r"(feedback loop)",
    ],
    
    # 3. Pluralism & Global Values
    "ALIGN_PLURALISM": [
        r"(pluralis)(m|tic)",
        r"(diverse values)",
        r"(cross-cultural).{0,50}(alignment|ethics)",
        r"(global).{0,50}(ethics|values)",
        r"(value variation)",
        r"(disagreement).{0,50}(moral|ethical)",
    ],
    
    # 4. Benchmarks & Evals (Specific to Alignment/Ethics)
    "ALIGN_BENCHMARKS": [
        r"(benchmark).{0,50}(ethics|moral|alignment)",
        r"(dataset).{0,50}(ethics|moral|alignment)",
        r"(evaluating).{0,50}(alignment|ethics)",
        r"(metric).{0,50}(alignment|harm)",
        r"(safety bench)",
    ],
    
    # 5. General / Catch-All
    "ALIGN_GENERAL": [
        r"(value alignment)",
        r"(human values).{0,50}(alignment|ai)",
        r"(ai safety).{0,50}(values|ethics)",
        r"(machine ethics).{0,50}(general|field)",
        r"(moral machine)",
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
            # Process previous paper
            if current_paper:
                cats = analyze_text_semantically(current_text)
                if cats:
                    current_paper['categories'] = cats
                    papers.append(current_paper)
            
            # Start new paper
            current_paper = {"text": ""}
            current_text = ""
            
            parts = line.replace("## Paper:", "").strip().split('|')
            if len(parts) >= 3:
                current_paper["year"] = parts[0].strip()
                current_paper["author"] = parts[1].strip()
                current_paper["title"] = parts[2].strip()
            else:
                 current_paper["year"] = "Unknown"
                 current_paper["author"] = "Unknown"
                 current_paper["title"] = "Unknown"

        elif line.startswith("File:"):
             current_paper["link"] = line.replace("File:", "").strip()
             
        elif line.startswith("### Abstract") or line.startswith("### Detailed Summary") or line.startswith("---"):
            continue
        else:
            current_text += " " + line.strip()

    # Process last paper
    if current_paper:
         cats = analyze_text_semantically(current_text)
         if cats:
             current_paper['categories'] = cats
             papers.append(current_paper)

    # Generate Report
    output_lines = []
    output_lines.append("# Paper Statistics 5: Semantic Analysis of Normative Ethics in AI")
    output_lines.append("")
    output_lines.append(f"**Method**: Semantic Pattern Matching on Abstracts & Summaries")
    
    # --- Classification Logic ---
    normative_keys = ["VIRTUE", "DEONTOLOGY", "UTILITARIAN"]
    
    normative_papers = []
    other_papers = []
    
    for p in papers:
        # If it has ANY normative key, it goes to Master List 1
        if any(k in p['categories'] for k in normative_keys):
            normative_papers.append(p)
        # If it has NO normative key but HAS alignment keys, it goes to List 3
        elif any(k.startswith("ALIGN_") for k in p['categories']):
            other_papers.append(p)
            
    output_lines.append(f"**Total Normative Ethics Papers**: {len(normative_papers)}")
    output_lines.append(f"**Other Value Alignment Papers**: {len(other_papers)}")
    output_lines.append(f"**Generated**: {os.popen('date').read().strip()}")
    output_lines.append("")
    
    output_lines.append("## Overview")
    output_lines.append("This report applies a **semantic reading** approach. Section 1 covers explicit Normative Ethics. Section 3 categorizes other Value Alignment work.")
    output_lines.append("")

    # --- Section 1: Normative ---
    output_lines.append("## 1. Master List (Normative Ethics)")
    output_lines.append("| Year | Author | Title | Categories |")
    output_lines.append("|------|--------|-------|------------|")
    
    sorted_normative = sorted(normative_papers, key=lambda x: (x.get('year', '0000'), x.get('author', '')), reverse=True)
    
    for p in sorted_normative:
        # Show all relevant categories in the table
        cats = ", ".join(sorted([c for c in p['categories'] if c in normative_keys]))
        output_lines.append(f"| {p['year']} | {p['author']} | {p['link']} | {cats} |")

    output_lines.append("")
    output_lines.append("## 2. Breakdown by Ethical School")
    output_lines.append("")

    def print_table(papers, headers=["Year", "Author", "Title"]):
        output_lines.append("| " + " | ".join(headers) + " |")
        output_lines.append("|" + "|".join(["-"*6]*len(headers)) + "|")
        if not papers:
            output_lines.append("| - " * len(headers) + "|")
        for p in papers:
            output_lines.append(f"| {p['year']} | {p['author']} | {p['link']} |")
        output_lines.append("")

    def print_subtable(name, key, source_list):
        subset = [p for p in source_list if key in p['categories']]
        output_lines.append(f"### {name}")
        output_lines.append(f"*(Count: {len(subset)})*")
        print_table(subset)

    print_subtable("(a) Virtue Ethics", "VIRTUE", sorted_normative)
    print_subtable("(b) Deontological Ethics", "DEONTOLOGY", sorted_normative)
    print_subtable("(c) Utilitarian & Consequentialist Ethics", "UTILITARIAN", sorted_normative)
    
    # --- Section 3: Other Alignment ---
    output_lines.append("## 3. Other Value Alignment Papers")
    output_lines.append(f"*(Total: {len(other_papers)})*")
    output_lines.append("")
    
    sorted_other = sorted(other_papers, key=lambda x: (x.get('year', '0000'), x.get('author', '')), reverse=True)
    
    # We want these to be mutually exclusive for the listing? Or just list buckets?
    # A paper can be in multiple (e.g. RLHF + Benchmarks). We will list buckets.
    
    print_subtable("3.1 Constitutional AI & Rules", "ALIGN_CONSTITUTIONAL", sorted_other)
    print_subtable("3.2 RLHF & Preferences", "ALIGN_RLHF", sorted_other)
    print_subtable("3.3 Pluralistic & Global Alignment", "ALIGN_PLURALISM", sorted_other)
    print_subtable("3.4 Benchmarks & Evaluations", "ALIGN_BENCHMARKS", sorted_other)
    
    # Catch-all
    # Papers that matched ALIGN_GENERAL but NONE of the specific ALIGN_X
    specific_align_keys = ["ALIGN_CONSTITUTIONAL", "ALIGN_RLHF", "ALIGN_PLURALISM", "ALIGN_BENCHMARKS"]
    catch_all = [p for p in sorted_other if not any(k in p['categories'] for k in specific_align_keys)]
    
    output_lines.append("### 3.5 General / Uncategorized Alignment")
    output_lines.append(f"*(Count: {len(catch_all)})*")
    print_table(catch_all)

    OUTPUT_FILE.write_text("\n".join(output_lines), encoding='utf-8')
    print(f"Report generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
