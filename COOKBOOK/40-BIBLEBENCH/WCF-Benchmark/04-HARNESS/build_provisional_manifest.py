#!/usr/bin/env python
"""Freeze the PROVISIONAL qualification manifest of record (memo R35.6) — session 12.

The session-12 K=8 probe-stability sweep (07-PILOTS/20260710-probe-stability/
raw_verdicts.jsonl, authoritative) produced the pass table the Fable memo tabulated in
its sec0. This script re-derives the eligible-surface sets from those counts via the
SAME >=5/8 per-surface gate the harness now applies (wcfbench.qualification), and writes
the manifest JudgePanel consumes for the floor re-run. It reproduces R35.6 exactly:

  gemini-2.5-flash -> {open_award, disclosure, coherence, settled_core}
  gpt-4o-mini      -> {coherence, settled_core}
  mistral-small / mistral-medium -> {} (discarded)

APPEND-ONLY: writes a NEW file into the existing sweep dir; touches nothing else. The
per-rep cause detail lives in raw_verdicts.jsonl + the memo (this manifest carries the
n_pass counts + frozen eligibility + template hashes, not re-materialized reps).
"""

from __future__ import annotations

import os
import sys

HARNESS_ROOT = os.path.dirname(os.path.abspath(__file__))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench.qualification import manifest_from_pass_table, write_manifest  # noqa: E402

OUT = os.path.normpath(os.path.join(
    HARNESS_ROOT, "..", "07-PILOTS", "20260710-probe-stability",
    "20260710-qualification-manifest.json"))

# The memo sec0 K=8 pass table (verified against raw_verdicts.jsonl in the main loop).
# Columns: g4 | award_consistency | discrimination | disclosure_inversion | negative_disclosure
ROWS = [
    {"name": "gpt4omini", "family": "openai", "slug": "openai/gpt-4o-mini",
     "pass_counts": {"g4": 8, "award_consistency": 2, "discrimination": 0,
                     "disclosure_inversion": 8, "negative_disclosure": 0}},
    {"name": "gemini-flash", "family": "google", "slug": "google/gemini-2.5-flash",
     "pass_counts": {"g4": 8, "award_consistency": 5, "discrimination": 6,
                     "disclosure_inversion": 8, "negative_disclosure": 8}},
    {"name": "mistral-small", "family": "mistral", "slug": "mistralai/mistral-small-3.2-24b-instruct",
     "pass_counts": {"g4": 0, "award_consistency": 2, "discrimination": 0,
                     "disclosure_inversion": 0, "negative_disclosure": 0}},
    {"name": "mistral-medium", "family": "mistral", "slug": "mistralai/mistral-medium-3.1",
     "pass_counts": {"g4": 0, "award_consistency": 8, "discrimination": 0,
                     "disclosure_inversion": 2, "negative_disclosure": 0}},
]


def main() -> int:
    manifest = manifest_from_pass_table(
        ROWS,
        run_dir="07-PILOTS/20260710-probe-stability",
        timestamp="2026-07-10T08:32:00",   # the sweep's recorded run time (raw_verdicts)
        memo="R34-R37 (R35.6 provisional manifest of record)",
        k=8, threshold=5,
    )
    write_manifest(OUT, manifest)
    print(f"wrote {OUT}")
    for j in manifest["judges"]:
        print(f"  {j['slug']:44s} -> {j['eligible_surfaces'] or '[] discarded'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
