<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# WCF-Bench MVP Exploratory Paper Traceability

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

This map transcribes accepted immutable values. It does not recompute or re-score
PPP-1 evidence. Paths are relative to the WCF-Benchmark project root. For table and
figure rows, the copied file in this paper directory is byte-identical to the named
accepted packet source, as recorded in `source-manifest.json`.

| Manuscript claim or artifact | Accepted value | Immutable source and exact field/path |
|---|---:|---|
| Status and validity label | COMPLETE; EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE | `07-PILOTS/20260713-ppp1-exploratory-preview/run-metadata.json`: `run_status`, `validity_label`; `08-PAPER/20260713-ppp1-exploratory-preview/00-README.md`: status and visible label |
| Frozen SUT roster | `meta-llama/llama-3.1-8b-instruct`; `deepseek/deepseek-chat`; `qwen/qwen3.7-plus` | `run-metadata.json`: `identity.suts`; `08-PAPER/20260713-ppp1-exploratory-preview/01-source-manifest.json`: `roster.suts` |
| Sole judge where required | `google/gemini-2.5-flash` | `run-metadata.json`: `identity.judge`; accepted packet manifest: `roster.judge` |
| Runnable base items | 226 | `run-metadata.json`: `identity.runnable_items`; accepted packet manifest: frozen-bank `selected_version` |
| Excluded development-only items | four: `LIB-C2-W305`, `LIB-C3-W202`, `LIB-C7-008`, `LIB-C8-W304` | `run-metadata.json`: `identity.excluded_dev_set_only_ids` |
| Item composition | 204 normal items and 22 episode items | `run-metadata.json`: `identity.normal_items`, `identity.episode_items` |
| Scope exclusions | base items only; no perturbations and no G1-G7 or human-panel evidence | `08-PAPER/20260713-ppp1-exploratory-preview/06-preview-discussion.md`; `07-preview-limitations.md` |
| Expected and recorded cells | 226 x 3 = 678; 678/678 recorded | `run-metadata.json`: `identity.expected_cells`, `recorded_cells`; `05-preview-results.md`: opening paragraph |
| Scored and error-recorded cells | 618 scored; 60 errors | `run-metadata.json`: `scored_cells`, `error_cells`; `07-PILOTS/20260713-ppp1-exploratory-preview/ppp1-report.md`: status bullets |
| Headline-eligible cells | 666 expected; 607 numeric; 59 missing headline values | `tables/03-overall-aggregate.csv`: `headline_expected_n`, `numeric_n`, and accepted denominator relation; `05-preview-results.md`: opening paragraph |
| Contested cells | 12, excluded from headline mean and retained only as separate disclosure/coherence/settled-core evidence | `tables/03-overall-aggregate.csv`: `contested_n`; accepted packet manifest: `score_contract.contested`; `05-preview-results.md` |
| Numeric scoring provenance | 109 mechanical numeric; 498 judge-scored numeric | `tables/03-overall-aggregate.csv`: `mechanical_numeric_n`, `judge_numeric_n`; accepted packet manifest: `score_contract` |
| Mechanical scorer statement | ORDINAL and ANCHOR remain mechanical | `ppp1-report.md`: final sentence; accepted packet manifest: `score_contract.ordinal_anchor_open` |
| Missingness rule | errors, ungraded, and unrecorded cells are missing, never zero | accepted packet manifest: `score_contract.missingness`; all accepted packet table prefaces |
| Llama aggregate | mean 0.3878; 95% CI [0.3425, 0.4357]; 213/222 numeric; 9 errors; coverage 0.9595 | `tables/02-per-sut-aggregate.md`: Llama row; full precision in corresponding CSV row |
| DeepSeek aggregate | mean 0.7882; 95% CI [0.7466, 0.8251]; 202/222 numeric; 20 errors; coverage 0.9099 | `tables/02-per-sut-aggregate.md`: DeepSeek row; full precision in corresponding CSV row |
| Qwen aggregate | mean 0.8449; 95% CI [0.8129, 0.8734]; 192/222 numeric; 31 errors; coverage 0.8649 | `tables/02-per-sut-aggregate.md`: Qwen row; full precision in corresponding CSV row |
| Per-SUT interval method | design-stratified item bootstrap; 1,000 deterministic resamples | `tables/02-per-sut-aggregate.md`: `ci_method` for each row |
| Overall pooled support summary | mean 0.6656; SD 0.3991; 95% CI [0.6302, 0.7004]; 607/666 numeric; 60 errors; coverage 0.9114 | `tables/03-overall-aggregate.md`: only data row; full precision in corresponding CSV row |
| Overall interval method | item-cluster bootstrap across all SUT observations; 1,000 deterministic resamples | `tables/03-overall-aggregate.md`: `ci_method` |
| Rows affected by errors | 15 of 30 design-by-SUT rows contain at least one error | `08-PAPER/20260713-ppp1-exploratory-preview/06-preview-discussion.md`: first paragraph; row denominators in `tables/01-per-design-per-sut.csv` |
| Full per-design table | 30 design-by-SUT rows with expected, numeric, error, coverage, mean, SD, interval, and scoring-source columns | accepted `tables/01-per-design-per-sut.md` and `.csv`; copied unchanged to this directory |
| Figure 1 | accepted design-by-SUT means; errors not imputed | accepted `figures/01-design-by-sut.svg`; denominator values in accepted table 01 |
| Figure 2 | accepted per-SUT aggregate means and intervals; errors not imputed | accepted `figures/02-per-sut-aggregate.svg`; denominator values in accepted table 02 |
| Paid calls | 1,722 | accepted `02-normalized-cells.csv`: `paid_call_count` custody field and final `raw_ledger_end_line` 1722; accepted source manifest identifies the selected final append-only raw ledger |
| Actual-first cost | $3.0552242489 | `run-metadata.json`: `actual_first_accounting_total_usd` (stored as 3.055224248900004); rounded report display in `ppp1-report.md` |
| Strict not-to-exceed cap | $23.56 | `run-metadata.json`: `budget_usd`; `run-metadata.json`: `budget_hit` is false |
| Response-attributed cost | unavailable because 2 calls used fallback accounting | `run-metadata.json`: `response_attributed_cost_usd` is null; `accounting_fallback_count` is 2; `accounting_fallback_sources.catalog_ceiling_missing_response_usage` is 2 |
| Shared-key usage delta | $13.7768984160, contextual only and never PPP-1-attributable | `run-metadata.json`: `key_usage_delta_usd` (stored as 13.776898415999995); `ppp1-report.md`: shared-key delta labeled contextual only |
| Evidence custody | RECONCILED | `run-metadata.json`: `custody_reconciled` is true and `custody_reconciliation_notes` is empty; `ppp1-report.md`: evidence custody |
| Checkpoint span | 9h46m18s | `checkpoint.jsonl`: first row `timestamp` = `2026-07-13T20:36:30Z`; last row `timestamp` = `2026-07-14T06:22:48Z`; this is explicitly reported as a first-to-last checkpoint-span derivation, not launch wall-time |
| PPP-1 relation to T4 | PPP-1 does not amend, replace, or satisfy registered T4 | `08-PAPER/20260713-ppp1-exploratory-preview/06-preview-discussion.md`: registered confirmatory study remains separate and unchanged; packet README: prohibited claim list |

## Non-empirical prose provenance

The abstract, introduction, related-work framing, benchmark-design description,
registered validity protocol, discussion, limitations, and ethics posture are adapted
selectively from `08-PAPER/01-abstract-skeleton.md` through
`08-PAPER/10-ethics-release.md`. Any full-protocol description in the manuscript is
explicitly prospective and registered; it is not evidence that PPP-1 validated the
protocol or passed a gate.
