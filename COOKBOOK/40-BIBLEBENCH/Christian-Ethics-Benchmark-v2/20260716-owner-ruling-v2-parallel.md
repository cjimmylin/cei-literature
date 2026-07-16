# Owner ruling — v2 remains PARALLEL (2026-07-16)

**Ruling (Jimmy, 2026-07-16):** "we want to make v2 in parallel with v1 and allow for
comparing in the future — so don't make v2 as canonical but as parallel."

**Effect:**
- Christian-Ethics-Benchmark-v2 (WALKWORTHY on Inspect AI) remains a **parallel
  harness** alongside the canonical v1 custom harness, indefinitely. It is a
  comparison instrument; future v1↔v2 cross-harness comparisons are an intended use.
- v1 (`../Christian-Ethics-Benchmark/`) remains the canonical execution path for
  release-grade evidence (paper v0.1 thread, G4 label pass, gate battery).
- The recommendation to adopt v2 as canonical (fit memo §4 + comparability evidence)
  was considered and explicitly NOT adopted.

**Evidence base at time of ruling:**
- `20260715-inspect-fit-assessment.md` — fit verdict: strong.
- `20260715c-comparability-judgepath-report.md` — judge-path replay PARITY
  (v2-vs-v1-judge-A 73.2% exact vs 59.2% v1 inter-judge baseline; 21/24 cells ≥ baseline).
- `20260715d-e2e-and-two-judge-report.md` — 2-judge re-score path validated (custom
  script path; CLI blocked by scorer registry naming at the time).

**Also authorized in the same ruling:** the three polish items ("please improve v2
with these polish items"):
1. Per-turn scoring for multi-turn designs 02/07 (v1 fidelity).
2. Metric-aggregation audit + fixes (design-01 rate discrepancy; design-03 say/do
   pairing; design-08 exemplar-admin NaN; sweep).
3. Scorer registry naming + native `inspect score` support.

Implementation report: `20260716-polish-items-report.md` (same-day).
