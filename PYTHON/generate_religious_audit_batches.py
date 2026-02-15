#!/usr/bin/env python3
"""
Generate batch files for religious tradition deep-read classification.

Reads audit candidates from logs/20260215-religious_traditions_audit.json,
resolves PDF extract paths, and splits into 10 balanced batches for
parallel agent processing.

Output: logs/religious_audit_batches/batch_01.json through batch_10.json
"""

import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from yaml_utils import extract_frontmatter, parse_frontmatter
from config import PAPERS_DIR, PDF_EXTRACTS_DIR, LOGS_DIR

AUDIT_FILE = LOGS_DIR / "20260215-religious_traditions_audit.json"
BATCHES_DIR = LOGS_DIR / "religious_audit_batches"


def resolve_extract_path(paper_path, fm_text):
    """Resolve the PDF extract path for a paper, return relative path or None."""
    fields = parse_frontmatter(fm_text)
    extract_ref = fields.get("pdf_extract", "").strip("\"'")
    if extract_ref and len(extract_ref) < 200 and extract_ref.startswith("PDF Extracts/"):
        extract_path = PAPERS_DIR.parent / extract_ref
        if extract_path.exists():
            return extract_ref

    # Fallback: try matching by stem in year subdirs
    for year_dir in PDF_EXTRACTS_DIR.iterdir():
        if year_dir.is_dir():
            candidate = year_dir / "{}.md".format(paper_path.stem)
            if candidate.exists():
                return str(candidate.relative_to(PAPERS_DIR.parent))

    # Fallback: root
    candidate = PDF_EXTRACTS_DIR / "{}.md".format(paper_path.stem)
    if candidate.exists():
        return "PDF Extracts/{}.md".format(paper_path.stem)

    return None


def main():
    if not AUDIT_FILE.exists():
        print("ERROR: Audit file not found: {}".format(AUDIT_FILE))
        print("Run audit_religious_traditions.py first.")
        sys.exit(1)

    with open(AUDIT_FILE, "r", encoding="utf-8") as f:
        audit_data = json.load(f)

    candidates = audit_data.get("candidates", [])
    print("Loaded {} candidates from audit".format(len(candidates)))

    if not candidates:
        print("No candidates to process. Exiting.")
        sys.exit(0)

    # Enrich with extract paths
    enriched = []
    for cand in candidates:
        paper_path = PAPERS_DIR / cand["filename"]
        if not paper_path.exists():
            print("  WARN: Paper not found: {}".format(cand["filename"]))
            continue

        try:
            content = paper_path.read_text(encoding="utf-8")
            fm_text, _ = extract_frontmatter(content)
        except (ValueError, Exception) as e:
            print("  WARN: Bad frontmatter: {} — {}".format(cand["filename"], e))
            continue

        extract_ref = resolve_extract_path(paper_path, fm_text)
        enriched.append({
            "filename": cand["filename"],
            "pdf_extract_path": extract_ref or "",
            "has_extract": extract_ref is not None,
            "candidate_traditions": list(cand.get("candidate_traditions", {}).keys()),
            "max_score": cand.get("max_score", 0),
            "top_tradition": cand.get("top_tradition", ""),
        })

    print("Enriched {} candidates (with extract paths)".format(len(enriched)))
    print("  With PDF extract: {}".format(sum(1 for e in enriched if e["has_extract"])))
    print("  Without PDF extract: {}".format(sum(1 for e in enriched if not e["has_extract"])))

    # Sort by max_score descending (highest-confidence first)
    enriched.sort(key=lambda x: -x["max_score"])

    # Split into 10 batches (or fewer if not enough candidates)
    n_batches = min(10, max(1, len(enriched)))
    batch_size = math.ceil(len(enriched) / n_batches)

    BATCHES_DIR.mkdir(parents=True, exist_ok=True)

    for batch_num in range(1, n_batches + 1):
        start = (batch_num - 1) * batch_size
        end = min(start + batch_size, len(enriched))
        batch = enriched[start:end]

        out_path = BATCHES_DIR / "batch_{:02d}.json".format(batch_num)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(batch, f, indent=2, ensure_ascii=False)

        traditions_in_batch = set()
        for entry in batch:
            traditions_in_batch.update(entry["candidate_traditions"])

        print("  Batch {:02d}: {} papers → {} (traditions: {})".format(
            batch_num, len(batch), out_path.name,
            ", ".join(sorted(traditions_in_batch))))

    print("\nBatch files written to: {}".format(BATCHES_DIR))
    print("Total: {} papers across {} batches".format(len(enriched), n_batches))

    # Write rubric for agents
    rubric_path = BATCHES_DIR / "RUBRIC.md"
    rubric = """# Religious Tradition Deep-Read Classification Rubric

For each paper in your batch, read the full paper content (title, abstract, body)
and the PDF extract (if available). Then classify:

## Fields to output (JSON array):

```json
{
  "filename": "2024-Author-Title.md",
  "decision": "Reclassify" | "Keep N/A" | "Uncertain",
  "religious_tradition": "Buddhism" | "Hinduism" | "Islam" | etc. | "N/A",
  "confidence": "High" | "Medium" | "Low",
  "evidence": "Brief quote or description of religious content found",
  "reasoning": "Why this paper should/shouldn't be reclassified"
}
```

## Decision criteria:

- **Reclassify**: Paper substantively engages with a religious/ethical tradition's
  values, principles, or frameworks. The tradition is central to the paper's argument
  or evaluation methodology, not merely mentioned in passing.
- **Keep N/A**: Paper mentions a tradition incidentally (e.g., "Buddhist-majority country")
  but doesn't engage with the tradition's ethical content.
- **Uncertain**: Evidence is ambiguous; paper discusses concepts that may or may not
  be grounded in a specific tradition.

## Important:
- A paper discussing "karma" in a secular psychology context is NOT Buddhist/Hindu
- A paper studying "values in Thai culture" IS relevant to Buddhism (dominant tradition)
- A paper on "data sovereignty" that specifically discusses Indigenous rights IS relevant
- Multi-tradition papers should pick the PRIMARY tradition or list comma-separated
"""
    rubric_path.write_text(rubric, encoding="utf-8")
    print("Rubric written to: {}".format(rubric_path))


if __name__ == "__main__":
    main()
