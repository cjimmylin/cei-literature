<!-- WALKWORTHY-CANARY-7f3e2026 -->
# 6A. Exploratory MVP Paper Preview

**Status:** DRAFT — separate from the release-grade O5 results in §6.

> Small exploratory panel; inexpensive, unvalidated judges; descriptive only; not
> release-grade evidence.

MVP-A1 executed a deterministic 60-item PUBLIC subset across three inexpensive SUTs
and two inexpensive cross-family judges. The snapshot contains all 180 item×SUT
executions and 480/480 logical units for each judge. All 1,715 attempts have paired
custody finishes; conservative exposure was $0.551363883 under a $5.00 NTE.
<!-- source: 00-PORTFOLIO/20260713-mvp-a1-descriptive-analysis.md §1 -->

**Table 6A.1 — Registered primary-metric preview.** Values are shown in fixed manifest
order, not ranked. Parentheses report retained contributions and exclusions. Metrics
differ by design and cannot be compared across rows.

| d | primary | Mistral Small | Gemini Flash-Lite | Qwen3 8B |
|---|---|---:|---:|---:|
| 01 | full-obedience-rate fallback | 50.0000 (4/2) | 80.0000 (5/1) | 66.6667 (6/0) |
| 02 | break turn | 0.0000 (2/4) | 0.0000 (2/4) | 6.2500 (2/4) |
| 03 | say–do gap | N/A (0/6) | 50.0000 (2/4) | 50.0000 (2/4) |
| 04 | motive-sensitivity index | 24.4444 (5/1) | 14.4444 (5/1) | 11.1111 (4/2) |
| 05 | constraint-satisfaction rate | 77.7778 (6/0) | 85.5556 (6/0) | 77.7778 (6/0) |
| 06 | criterion profile | 71.8452 (7/11) | 85.4762 (7/3) | 93.4524 (7/0) |
| 07 | arc shape | N/A (0/6) | N/A (0/6) | N/A (0/6) |
| 08 | covert–overt gap | 25.0000 (4/2) | 16.6667 (3/3) | 16.6667 (3/3) |
| 09 | symmetry index | 100.0000 (1/5) | 100.0000 (1/5) | 100.0000 (2/4) |
| 10 | mercy delta | 12.5000 (4/2) | 6.2500 (4/2) | 12.5000 (4/2) |

<!-- source: 00-PORTFOLIO/20260713-mvp-a1-descriptive-analysis.md §2 -->

**Table 6A.2 — Exact cheap-judge rubric-cell agreement (operational only).** This is
not accuracy, κ, or human validation.

| d | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agreement | 86.11% | 22.46% | 66.67% | 86.11% | 77.78% | 88.89% | 17.59% | 75.00% | 43.06% | 79.86% |

<!-- source: 00-PORTFOLIO/20260713-mvp-a1-descriptive-analysis.md §3 -->

**Figure 6A.1 — Registered execution and custody completeness.**

![MVP-A1 custody and completeness](figures/mvp-a1-custody-completeness.svg)

The figure is intentionally operational. A performance heatmap, model ranking,
release-status matrix, and validated-judge concordance figure are unavailable under
the MVP license. Those shapes require human-validity evidence and remain downstream
of O5 G4.
<!-- source: 00-PORTFOLIO/20260713-mvp-a1-descriptive-analysis.md §4 -->
