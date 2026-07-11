# WCF-Bench — R43/R44 Format-Bridge Requalification

Run: 2026-07-11T11:02:07 · K=8, gate >= 5/8 · max_tokens=2048 · budget $10.00

The award prompt now contains the frozen neutral format exemplar. Results under this bridged template are **not directly comparable to the pre-bridge MVP**.

## Resolved logical models

- gemini-flash (google): `google/gemini-2.5-flash` — full incumbent
- grok-4.20 (x-ai): `x-ai/grok-4.20` — full incumbent; OPEN candidate battery reused
- cohere-command-a (cohere): `cohere/command-a` — partial candidate
- amazon-nova-pro (amazon): `amazon/nova-pro-v1` — partial candidate

## K=8 pass/fail table per judge × surface/probe

| judge | family | resolved slug | probe | gated surface(s) | n_pass/K | result |
|---|---|---|---|---|---|---|
| gemini-flash | google | `google/gemini-2.5-flash` | g4 | open_award, coherence, settled_core | 8/8 | PASS |
| gemini-flash | google | `google/gemini-2.5-flash` | award_consistency | open_award | 0/8 | FAIL |
| gemini-flash | google | `google/gemini-2.5-flash` | discrimination | open_award | 8/8 | PASS |
| gemini-flash | google | `google/gemini-2.5-flash` | disclosure_inversion | disclosure | 8/8 | PASS |
| gemini-flash | google | `google/gemini-2.5-flash` | negative_disclosure | disclosure | 8/8 | PASS |
| gemini-flash | google | `google/gemini-2.5-flash` | settled_core | settled_core | 8/8 | PASS |
| grok-4.20 | x-ai | `x-ai/grok-4.20` | g4 | open_award, coherence, settled_core | 8/8 | PASS |
| grok-4.20 | x-ai | `x-ai/grok-4.20` | award_consistency | open_award | 0/8 | FAIL |
| grok-4.20 | x-ai | `x-ai/grok-4.20` | discrimination | open_award | 0/8 | FAIL |
| grok-4.20 | x-ai | `x-ai/grok-4.20` | disclosure_inversion | disclosure | 8/8 | PASS |
| grok-4.20 | x-ai | `x-ai/grok-4.20` | negative_disclosure | disclosure | 8/8 | PASS |
| grok-4.20 | x-ai | `x-ai/grok-4.20` | settled_core | settled_core | 8/8 | PASS |
| cohere-command-a | cohere | `cohere/command-a` | g4 | open_award, coherence, settled_core | 0/8 | FAIL |
| cohere-command-a | cohere | `cohere/command-a` | award_consistency | open_award | 8/8 | PASS |
| cohere-command-a | cohere | `cohere/command-a` | discrimination | open_award | 0/8 | FAIL |
| amazon-nova-pro | amazon | `amazon/nova-pro-v1` | g4 | open_award, coherence, settled_core | 1/8 | FAIL |
| amazon-nova-pro | amazon | `amazon/nova-pro-v1` | award_consistency | open_award | 8/8 | PASS |
| amazon-nova-pro | amazon | `amazon/nova-pro-v1` | discrimination | open_award | 1/8 | FAIL |

Cohere and Nova intentionally have no disclosure or settled-core calls; their G4 result is the coherence battery. Grok's candidate row is its full incumbent result, not a rerun.

## Manifest eligibility

| judge | family | eligible surfaces |
|---|---|---|
| gemini-flash | google | coherence, disclosure, settled_core |
| grok-4.20 | x-ai | coherence, disclosure, settled_core |
| cohere-command-a | cohere | none |
| amazon-nova-pro | amazon | none |

## OPEN outcome

**NO OPEN-ELIGIBLE FAMILY:** zero non-Google candidates passed; the completed pre-G6 candidate ladder is **CLOSED**. This unusable OPEN outcome requires escalation.

## Cost

Cost reconciliation: internal total **$0.4878** vs key-side usage delta **$0.4873** — within ±20%: YES.

Internal accounting is actual-first; any response without authoritative cost uses strict live-catalog prompt/completion prices. Missing accounting fails loud.

Raw calls and per-rep evidence are append-only in `raw_verdicts.jsonl`; no prior pilot directory or report was modified.
