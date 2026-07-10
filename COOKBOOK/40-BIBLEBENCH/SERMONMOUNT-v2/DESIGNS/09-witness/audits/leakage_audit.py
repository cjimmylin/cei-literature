"""
leakage_audit.py — hard gate: NO Sermon / registry / confessional language or benchmark
identity in any string shown to a tested model (guide Law 6; brief §7). A single hit in
either independently reported category fails the run.

Scans every model-facing prompt across renderings.jsonl AND format_control.jsonl.

Run:  ../.venv/bin/python DESIGNS/09-witness/audits/leakage_audit.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from witness_common import (  # noqa: E402
    read_jsonl, leakage_hits, identity_hits, ITEMBANK_DIR, AUDITS_DIR, write_jsonl,
)


def prompt_findings(prompt: str) -> dict[str, list[str]]:
    """Return independently classified hard-gate findings for one model prompt."""
    return {
        "leakage_hits": sorted(set(leakage_hits(prompt))),
        "identity_hits": sorted(set(identity_hits(prompt))),
    }


def main() -> int:
    problems = []
    total = 0
    for fname in ("renderings.jsonl", "format_control.jsonl"):
        for r in read_jsonl(ITEMBANK_DIR / fname):
            total += 1
            findings = prompt_findings(r["prompt"])
            if findings["leakage_hits"] or findings["identity_hits"]:
                problems.append({"item_id": r["item_id"], "file": fname, **findings})
    write_jsonl(problems, AUDITS_DIR / "leakage_audit.jsonl")
    print(f"leakage audit: scanned {total} model-facing prompts")
    if problems:
        print(f"  FAIL — {len(problems)} items contain leakage:")
        for p in problems[:20]:
            print("   ", p)
        return 1
    print("  PASS — zero Sermon/registry/confessional or benchmark-identity tokens "
          "in any tested-model prompt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
