# WCF-Bench — R49 MVP OPEN Re-parse

**DESCRIPTIVE / PRE-GATE — not a gated G1–G7 measurement.**

Re-parse: 2026-07-12T16:06:33 · OFFLINE · corrected manifest: `07-PILOTS/20260712-artifact-corrected-requal`

Sole response evidence: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/07-PILOTS/20260710-mvp-run/transcripts.jsonl`. The historical MVP run was not modified and no SUT or judge call was made.

## Coverage

- OPEN transcript cells re-parsed: **309**.
- Judge verdict texts consumed: **1688/1688**.
- Historical willingness-marker population: **155 verdicts across 65 OPEN cells** (R47 F-3 expectation: 155 / 65).
- Per-judge score records changed or recovered: **149** across **67** cells. A marker hit may confirm an unchanged numeric value; the delta table retains both.

## OPEN headline means by SUT

| SUT | n OPEN | original | corrected | changed headlines |
|---|---:|---:|---:|---:|
| anthropic/claude-haiku-4.5 | 76 | 0.9422 | 0.9447 | 11 |
| deepseek/deepseek-chat | 77 | 0.8407 | 0.8435 | 6 |
| meta-llama/llama-3.1-8b-instruct | 77 | 0.3686 | 0.3539 | 18 |
| mistralai/mistral-large-2512 | 79 | 0.9051 | 0.8988 | 8 |

OPEN remains **SINGLE-FAMILY (google)** under R34.4. Corrected headlines use only Gemini's OPEN-eligible, non-fenced values; GPT and Grok raws remain in the delta and disagreement evidence but do not aggregate.

## R42 material-delta screen

**No new R42-material candidate was found.** The two R42-referenced changes are exactly R42.1's already-adjudicated parser corrections: WHOLE-C1-004×deepseek Gemini manner 2.5→0.5 and MEND-C5-W204×llama Gemini matter 0.0→0.25. No other explicitly adjudicated R42 OPEN cell changed.

## Historical qualification footnote

R47 finding F-4 stands: the pre-bridge probe-stability award-consistency results carry the same quoted-evidence willingness artifact. This re-parse revises no historical manifest.

Full per-cell and per-judge before/after values are in `delta-table.json`; corrected eligible-only spread records are in `disagreement.json`.
