<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — PR-9 mechanical decision evidence (post-Grok)

**Date:** 2026-07-11. **Executor:** Codex. **Scope:** evidence only; no ruling.

This packet tightens the quantities Jimmy/Fable need for PR-9. It does not select the
W1 surface, authorize a re-execution, size the approved human workload, amend §E, or
license any gate verdict. Source: the immutable public O4 panel JSONL. HOLDOUT was not
loaded.

## 1. Reproduced selector facts

Two independent aggregations (`jq` and `awk`) agree:

- panel: **2,064 records**;
- `refusal_tag == pending_adjudication`: **609 records**;
- selected records with an actual `needs_adjudication` cell: **589**;
- selected records without a judge disagreement: **20** (11 design 05; 9 design 09);
- `needs_adjudication` cells inside the 609-record selector: **1,767**;
- `needs_adjudication` cells across the full panel: **3,172**;
- cells outside the current selector: **1,405**.

The full unresolved surface spans **1,297 records**. The current selector contains 589
of those records; 708 unresolved records lie outside it.

## 2. Mistral fallback exposure

The trigger-relevant denominator is unresolved cells, not merely records. Under the
current selector, Mistral owns more than 10% of unresolved cells in every design.

| design | pending records | Mistral pending records | ownership | selected unresolved cells | Mistral selected cells | selected share | full unresolved cells | Mistral full cells | full share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 01 | 71 | 14 | 19.72% | 88 | 18 | 20.45% | 123 | 27 | 21.95% |
| 02 | 122 | 14 | 11.48% | 655 | 70 | 10.69% | 1,003 | 152 | 15.15% |
| 03 | 61 | 11 | 18.03% | 148 | 22 | 14.86% | 257 | 42 | 16.34% |
| 04 | 81 | 15 | 18.52% | 210 | 46 | 21.90% | 364 | 71 | 19.51% |
| 05 | 19 | 4 | 21.05% | 8 | 1 | 12.50% | 61 | 5 | 8.20% |
| 06 | 3 | 1 | 33.33% | 21 | 7 | 33.33% | 147 | 35 | 23.81% |
| 07 | 67 | 14 | 20.90% | 252 | 49 | 19.44% | 436 | 76 | 17.43% |
| 08 | 36 | 8 | 22.22% | 48 | 10 | 20.83% | 82 | 14 | 17.07% |
| 09 | 106 | 18 | 16.98% | 194 | 38 | 19.59% | 270 | 49 | 18.15% |
| 10 | 43 | 9 | 20.93% | 143 | 34 | 23.78% | 429 | 109 | 25.41% |
| **total** | **609** | **108** | **17.73%** | **1,767** | **295** | **16.69%** | **3,172** | **580** | **18.28%** |

Four of the 108 Mistral-tagged pending records are among the 20 non-tie-breakable
records (three design 05; one design 09). Therefore:

- current-selector Mistral own-family burden with actual disagreeing cells:
  **104 records / 295 atomic cells**;
- full-surface Mistral own-family burden: **225 records / 580 atomic cells**;
- incremental burden outside the current selector: **121 records / 285 atomic cells**.

These are pre-tie-breaker exposure counts, not a final Part-B export. Additional cells
could remain contested after the pair plus tie-breaker. Conversely, the approved W1
surface may change under the pending FR-16 ruling.

## 3. Part-B packaging dependency

Protocol §6 defines Part B at the unresolved **cell** level. The current
`label_sample.export_part_b` implementation emits one context row per unresolved
record. For multi-cell designs, records and atomic labeling decisions are not the same
quantity. The final Part-B exporter therefore needs a TDD update after FR-16 fixes the
surface/routing; this packet does not silently treat 104 or 225 context records as the
human decision count.

## 4. 02/07 re-execution cost evidence

The earlier dashboard estimate of ~$10–15 is not supported by the completed run's cost
ledger. Summing `_panel_cost.usd` over the exact six-SUT 02/07 O4 surface gives:

- 02: **$17.550653** for 216 records;
- 07: **$9.131048** for 162 records;
- combined: **$26.681701** for 378 records, 10,037 calls, 14,626,004 prompt tokens, and
  2,487,196 completion tokens.

The sum of every record's `_panel_cost.usd` is $48.745000, matching
`panel_summary.json`, so the per-record ledger reconciles. **$26.68 is a historical
same-surface baseline, not a price guarantee.** A cheaper transcript-only execution
path is not currently specified or authorized; inventing one would change the ordered
re-execution contract.

## 5. Decision branches now requiring rulings

1. **Transcript branch (Jimmy):** authorize a new immutable 02/07 six-SUT re-execution
   using the historical ~$26.68 baseline, or supply recovered full transcripts.
2. **Selector branch (Fable/ratify Jimmy):** current 609-record surface versus the full
   3,172-cell §B surface; route the 20 parse/arbiter pendings outside the tie-breaker.
3. **STOP-8 branch (Jimmy):** accept Mistral plus an explicitly approved Part-B surface,
   or issue a logged §E replacement-model amendment and require its reliability probe.

Until all three are logged, Codex remains stopped before W1.

## 6. Reproduction notes

For each record, unresolved-cell count was computed as:

```jq
[.judge_report.disagreements[]? | select(.needs_adjudication == true)] | length
```

The aggregation was run twice with independent `jq --slurp` and line-oriented
`jq | awk` paths. Both produced the same per-design record/cell counts. Historical cost
was checked both against the 02/07 records and against the panel-level $48.745 total.
