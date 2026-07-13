# WCF-Bench T3 EPISODE Offline Correction

**Date:** 2026-07-13
**Label:** DESCRIPTIVE/PRE-GATE
**Scope:** Offline correction only; no paid calls, claims, or gate adjudication.

## Artifact hierarchy

The immutable original `raw-evidence.jsonl` and `checkpoint.jsonl` remain the primary evidence. This correction controls T3 descriptive status and summary only; it does not replace or modify the original run evidence. Source paths and SHA-256 hashes are recorded in the companion JSON.

## Corrected cell

`NARROW-C7-010::anthropic/claude-haiku-4.5` is reclassified from **scored** to **error-recorded**. Its score of 1.0 and disagreement status are excluded; no other cell is rewritten.

Trace:

- Raw line 191 (within the cell bundle at lines 190–192) is the Gemini emission: `finish_reason="error"`, zero prompt/completion/total tokens, zero cost, and only 1 of 5 required keypoint verdicts.
- Checkpoint line 64 nevertheless records the cell as scored, with score 1.0 and comparison status `disagreement`.
- The bundle contains one Gemini emission and no retry emission. The persisted evidence therefore does not support a complete panel score of record for this cell.

## Corrected descriptive summary

| Measure | Corrected value |
|---|---:|
| Recorded cells | 88 |
| Scored cells | 87 |
| Error-recorded cells | 1 |
| Graded cells | 80 |
| Wholly ungraded cells | 7 |
| Agreement | 36 |
| Disagreement | 44 |
| Ungraded comparison | 7 |
| Graded mean | 0.50375 |

Score distribution: **38 at 1.0 · 36 at 0.0 · 6 partial · 7 ungraded**. The error-recorded cell is excluded from the distribution and mean.

| SUT | Graded n | Graded mean | Other status |
|---|---:|---:|---|
| `meta-llama/llama-3.1-8b-instruct` | 20 | 0.19167 | 2 wholly ungraded |
| `deepseek/deepseek-chat` | 20 | 0.34833 | 2 wholly ungraded |
| `mistralai/mistral-large-2512` | 19 | 0.50000 | 3 wholly ungraded |
| `anthropic/claude-haiku-4.5` | 21 | 0.95238 | 1 error-recorded |

## Cost and preserved truncation evidence

Response-attributed run cost remains **$0.4393786622**, with **0 accounting fallbacks**, under the **$10.00** cap. The shared-key usage delta is **$2.439582089** and is contextual only, not run-attributed. This offline correction spent $0.

Exactly three SUT emissions ended for length and remain preserved evidence; the source does not support reclassifying them as errors:

| Raw line | Item | SUT | Disposition |
|---:|---|---|---|
| 196 | `NARROW-C7-W205` | `deepseek/deepseek-chat` | `finish_reason="length"`; preserved, not reclassified |
| 199 | `NARROW-C7-W205` | `mistralai/mistral-large-2512` | `finish_reason="length"`; preserved, not reclassified |
| 259 | `NARROW-XC-W306` | `mistralai/mistral-large-2512` | `finish_reason="length"`; preserved, not reclassified |

All numbers above were recomputed from the hashed source snapshot. They are descriptive pre-gate results only and do not constitute a benchmark claim or gate ruling.
