#!/usr/bin/env python3
"""
COOKBOOK Phase 1 — reader batch generator.

Packs the manifest papers into reader batches sized so a single agent can hold
its whole batch in context (total extract lines <= MAX_LINES, <= MAX_PAPERS
papers). Benchmark papers (reader_tier=opus) and context papers (sonnet) are
packed separately. Thin/missing extracts go into 'degraded' batches whose
readers use the paper file's paper_summary instead of the extract.

Also packs the AI-Labs shortlist into lab-card batches.

Output: 30-EVIDENCE/20260705-reader-batches.json
"""

import json
from datetime import datetime
from pathlib import Path

EVIDENCE_DIR = Path(__file__).resolve().parents[1] / "30-EVIDENCE"
MANIFEST = EVIDENCE_DIR / "20260705-corpus-manifest.json"
SHORTLIST = EVIDENCE_DIR / "20260705-ailabs-shortlist.json"
OUT = EVIDENCE_DIR / "20260705-reader-batches.json"

MAX_LINES = 9000
MAX_PAPERS = 8
MAX_DEGRADED = 10


def pack(papers, prefix, tier, mode="full"):
    """Greedy first-fit pack (papers pre-sorted by stem)."""
    batches = []
    cur, cur_lines = [], 0
    for p in papers:
        lines = max(p["extract_lines"], 0)
        if cur and (cur_lines + lines > MAX_LINES or len(cur) >= MAX_PAPERS):
            batches.append(cur)
            cur, cur_lines = [], 0
        cur.append(p)
        cur_lines += lines
    if cur:
        batches.append(cur)
    return [
        {
            "id": f"{prefix}{i+1:03d}",
            "tier": tier,
            "mode": mode,
            "papers": [
                {
                    "stem": p["stem"],
                    "extract_path": p["extract_path"],
                    "extract_lines": p["extract_lines"],
                }
                for p in batch
            ],
        }
        for i, batch in enumerate(batches)
    ]


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    papers = manifest["papers"]

    ok = [p for p in papers if p["extract_quality"] == "ok"]
    degraded = [p for p in papers if p["extract_quality"] != "ok"]

    opus = sorted((p for p in ok if p["reader_tier"] == "opus"), key=lambda p: p["stem"])
    sonnet = sorted((p for p in ok if p["reader_tier"] == "sonnet"), key=lambda p: p["stem"])
    degraded = sorted(degraded, key=lambda p: p["stem"])

    batches = []
    batches += pack(opus, "O", "opus")
    batches += pack(sonnet, "S", "sonnet")
    # degraded: cheap paper_summary-only cards, sonnet, no line budget needed
    for i in range(0, len(degraded), MAX_DEGRADED):
        chunk = degraded[i:i + MAX_DEGRADED]
        batches.append({
            "id": f"D{i // MAX_DEGRADED + 1:03d}",
            "tier": "sonnet",
            "mode": "degraded",
            "papers": [
                {
                    "stem": p["stem"],
                    "paper_path": p["paper_path"],
                    "extract_quality": p["extract_quality"],
                }
                for p in chunk
            ],
        })

    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    labs = sorted(shortlist["reports"], key=lambda r: (r["company"] or "", r["stem"]))
    lab_batches = []
    cur, cur_lines = [], 0
    for r in labs:
        lines = max(r["extract_lines"], 0)
        if cur and (cur_lines + lines > MAX_LINES or len(cur) >= MAX_PAPERS):
            lab_batches.append(cur)
            cur, cur_lines = [], 0
        cur.append(r)
        cur_lines += lines
    if cur:
        lab_batches.append(cur)
    lab_batches = [
        {
            "id": f"L{i+1:03d}",
            "tier": "sonnet",
            "papers": [
                {
                    "stem": r["stem"],
                    "extract_path": r["extract_path"],
                    "extract_lines": r["extract_lines"],
                    "company": r["company"],
                    "title": r["title"],
                }
                for r in batch
            ],
        }
        for i, batch in enumerate(lab_batches)
    ]

    out = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "params": {"max_lines": MAX_LINES, "max_papers": MAX_PAPERS},
        "counts": {
            "reader_batches": len(batches),
            "opus_batches": sum(1 for b in batches if b["tier"] == "opus"),
            "sonnet_batches": sum(1 for b in batches if b["tier"] == "sonnet" and b["mode"] == "full"),
            "degraded_batches": sum(1 for b in batches if b["mode"] == "degraded"),
            "papers_total": sum(len(b["papers"]) for b in batches),
            "lab_batches": len(lab_batches),
            "lab_reports": sum(len(b["papers"]) for b in lab_batches),
        },
        "reader_batches": batches,
        "lab_batches": lab_batches,
    }
    OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")

    # Per-batch assignment files so each reader agent loads only its own batch
    batch_dir = EVIDENCE_DIR / "20260705-batches"
    batch_dir.mkdir(exist_ok=True)
    for b in batches + lab_batches:
        (batch_dir / f"{b['id']}.json").write_text(
            json.dumps(b, indent=1), encoding="utf-8"
        )

    print(f"Wrote {OUT}")
    print(f"Wrote {len(batches) + len(lab_batches)} per-batch files to {batch_dir}")
    for k, v in out["counts"].items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
