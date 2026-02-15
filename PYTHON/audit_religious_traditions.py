#!/usr/bin/env python3
"""
Audit papers for religious tradition keywords beyond title+abstract.

Scans papers + PDF extracts against expanded RELIGIOUS_PATTERNS with
weighted scoring to find misclassified papers tagged N/A.
"""

import re
import json
import sys
import functools
from pathlib import Path
from collections import defaultdict

print = functools.partial(print, flush=True)

SCRIPT_DIR = Path(__file__).parent
WS_ROOT = SCRIPT_DIR.parent
PAPERS_DIR = WS_ROOT / "papers"
EXTRACTS_DIR = WS_ROOT / "PDF Extracts"
LOGS_DIR = WS_ROOT / "logs"
OUTPUT_FILE = LOGS_DIR / "20260215-religious_traditions_audit.json"

sys.path.insert(0, str(SCRIPT_DIR))
from classify_cultural_religious import RELIGIOUS_PATTERNS
from yaml_frontmatter_utils import read_paper, parse_frontmatter

# Compile patterns
COMPILED_PATTERNS = {}
for tradition, patterns in RELIGIOUS_PATTERNS.items():
    COMPILED_PATTERNS[tradition] = [re.compile(p, re.IGNORECASE) for p in patterns]


def extract_title(body):
    """Extract title from the '# Title' heading in the paper body."""
    match = re.search(r'^# (.+?)$', body, re.MULTILINE)
    return match.group(1).strip() if match else ""


def extract_abstract(body):
    """Extract abstract text from the '## Abstract' section in the paper body."""
    match = re.search(r'## Abstract\s*\n\n(.*?)(?=\n## |\Z)', body, re.DOTALL)
    return match.group(1).strip() if match else ""


def load_extract(extract_path_value):
    """Load PDF extract text given the pdf_extract YAML field value."""
    if not extract_path_value or extract_path_value in ("N/A", ""):
        return ""
    # Strip quotes
    clean = extract_path_value.strip('"').strip("'")
    # Validate it looks like a path (not abstract text accidentally stored in this field)
    if len(clean) > 200 or not clean.startswith("PDF Extracts/"):
        return ""
    full_path = WS_ROOT / clean
    if full_path.exists():
        try:
            return full_path.read_text(encoding="utf-8")
        except Exception:
            return ""
    return ""


def score_paper(title, abstract, extract_text):
    """Score paper against all traditions. Returns {tradition: {score, matches}}."""
    results = {}
    for tradition, compiled in COMPILED_PATTERNS.items():
        title_hits = sum(1 for p in compiled if p.search(title)) if title else 0
        abstract_hits = sum(1 for p in compiled if p.search(abstract)) if abstract else 0
        extract_hits = sum(1 for p in compiled if p.search(extract_text)) if extract_text else 0

        score = title_hits * 3 + abstract_hits * 2 + extract_hits * 1

        if score > 0:
            # Collect evidence snippets
            evidence = []
            for p in compiled:
                for text, label in [(title, "title"), (abstract, "abstract"), (extract_text[:5000], "extract")]:
                    if text:
                        m = p.search(text)
                        if m:
                            start = max(0, m.start() - 30)
                            end = min(len(text), m.end() + 30)
                            snippet = text[start:end].replace("\n", " ").strip()
                            evidence.append({"source": label, "pattern": p.pattern, "context": f"...{snippet}..."})

            results[tradition] = {
                "score": score,
                "title_hits": title_hits,
                "abstract_hits": abstract_hits,
                "extract_hits": extract_hits,
                "evidence": evidence[:10]  # Limit evidence snippets
            }

    return results


def main():
    papers = sorted(PAPERS_DIR.glob("*.md"))
    print(f"Found {len(papers)} papers to audit")

    candidates = []
    all_matches = []
    tradition_counts = defaultdict(int)

    for i, paper in enumerate(papers):
        if (i + 1) % 200 == 0:
            print(f"  Processing {i+1}/{len(papers)}...")

        try:
            frontmatter, body = read_paper(paper)
            fields = parse_frontmatter(frontmatter)

            current_religious = fields.get("religious_values", "N/A").strip('"')

            title = extract_title(body)
            abstract = extract_abstract(body)
            extract_text = load_extract(fields.get("pdf_extract", ""))

            scores = score_paper(title, abstract, extract_text)

            if not scores:
                continue

            # Record all matches regardless of current tag
            entry = {
                "filename": paper.name,
                "current_religious_values": current_religious,
                "traditions": scores,
                "max_score": max(s["score"] for s in scores.values()),
                "top_tradition": max(scores, key=lambda t: scores[t]["score"]),
            }
            all_matches.append(entry)

            # Candidates: currently N/A but scored >= 2
            if current_religious == "N/A":
                high_scoring = {t: s for t, s in scores.items() if s["score"] >= 2}
                if high_scoring:
                    entry["candidate_traditions"] = {t: s for t, s in high_scoring.items()}
                    candidates.append(entry)
                    for t in high_scoring:
                        tradition_counts[t] += 1

        except Exception as e:
            print(f"  Error processing {paper.name}: {e}")

    # Summary
    print(f"\n{'='*60}")
    print(f"AUDIT RESULTS")
    print(f"{'='*60}")
    print(f"  Papers scanned:     {len(papers)}")
    print(f"  Papers with ANY religious keyword: {len(all_matches)}")
    print(f"  Candidates (N/A, score>=2): {len(candidates)}")
    print(f"\n  Tradition breakdown (candidates):")
    for trad, count in sorted(tradition_counts.items(), key=lambda x: -x[1]):
        print(f"    {trad}: {count}")

    # Write output
    output = {
        "metadata": {
            "date": "2026-02-15",
            "papers_scanned": len(papers),
            "total_with_keywords": len(all_matches),
            "candidate_count": len(candidates),
            "threshold": 2,
            "weights": {"title": 3, "abstract": 2, "extract": 1},
        },
        "tradition_counts": dict(tradition_counts),
        "candidates": candidates,
        "all_matches": all_matches,
    }

    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nOutput: {OUTPUT_FILE}")
    print(f"  Size: {OUTPUT_FILE.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
