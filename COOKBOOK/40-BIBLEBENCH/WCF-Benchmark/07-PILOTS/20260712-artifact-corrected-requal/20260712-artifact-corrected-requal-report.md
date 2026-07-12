# WCF-Bench — R47.3 Artifact-Corrected Requalification

Re-parse: 2026-07-12T15:59:59 · K=8, gate >= 5/8 · OFFLINE

This is the **corrected manifest event under R47.3** and it **supersedes the as-executed Task-4 manifest as manifest of record**. The Task-4 directory remains an unchanged historical record.

Sole evidence source: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/07-PILOTS/20260711-format-bridge-requal/raw_verdicts.jsonl`. No live calls were made.

## Corrected K=8 pass/fail table

| judge | family | probe | n_pass/K | result |
|---|---|---|---:|---|
| gemini-flash | google | g4 | 8/8 | PASS |
| gemini-flash | google | award_consistency | 8/8 | PASS |
| gemini-flash | google | discrimination | 8/8 | PASS |
| gemini-flash | google | disclosure_inversion | 8/8 | PASS |
| gemini-flash | google | negative_disclosure | 8/8 | PASS |
| gemini-flash | google | settled_core | 8/8 | PASS |
| grok-4.20 | x-ai | g4 | 8/8 | PASS |
| grok-4.20 | x-ai | award_consistency | 8/8 | PASS |
| grok-4.20 | x-ai | discrimination | 0/8 | FAIL |
| grok-4.20 | x-ai | disclosure_inversion | 8/8 | PASS |
| grok-4.20 | x-ai | negative_disclosure | 8/8 | PASS |
| grok-4.20 | x-ai | settled_core | 8/8 | PASS |
| cohere-command-a | cohere | g4 | 0/8 | FAIL |
| cohere-command-a | cohere | award_consistency | 8/8 | PASS |
| cohere-command-a | cohere | discrimination | 0/8 | FAIL |
| amazon-nova-pro | amazon | g4 | 1/8 | FAIL |
| amazon-nova-pro | amazon | award_consistency | 8/8 | PASS |
| amazon-nova-pro | amazon | discrimination | 1/8 | FAIL |

## Corrected eligibility

| judge | eligible surfaces |
|---|---|
| gemini-flash | coherence, disclosure, open_award, settled_core |
| grok-4.20 | coherence, disclosure, settled_core |
| cohere-command-a | none |
| amazon-nova-pro | none |

## OPEN outcome

**SINGLE-FAMILY (google)** under R34.4: Gemini Flash is OPEN-eligible; Grok, Cohere, and Nova are not. The candidate ladder remains CLOSED. No candidate was rerun or added.

Both incumbent award-consistency rows correct from 0/8 to 8/8. Grok's discrimination row remains a substantive 0/8; Cohere and Nova remain ineligible.
