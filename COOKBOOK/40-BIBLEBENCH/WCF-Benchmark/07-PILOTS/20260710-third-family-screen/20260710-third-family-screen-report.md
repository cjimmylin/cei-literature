# WCF-Bench — Third-Family Screen (R36)

Canary: `WCFBENCH-CANARY-c1647-x9k4q`  ·  Run: 2026-07-10T12:59:59  ·  K=8, gate >= 5/8, temperature=0

DESCRIPTIVE / pre-gate. Screen-first (R36.3): a candidate is wired only if it reaches >=5/8 on the starved DISCLOSURE surface (OPEN award ideally too). Mistral is exhausted (R36.2) and absent.

## Pass table (n_pass / K) + rep-cause tally

### command-r-08-2024 — `cohere/command-r-08-2024` (family=cohere)

| probe | n_pass/K | cause tally |
|---|---|---|
| g4 | 0/8 | {'fail_format': 8} |
| award_consistency | 0/8 | {'fail_format': 8} |
| discrimination | 0/8 | {'fail_substantive': 8} |
| disclosure_inversion | 4/8 | {'fail_substantive': 4, 'pass': 4} |
| negative_disclosure | 0/8 | {'fail_substantive': 8} |

- **eligible surfaces:** [] — none

### grok-4.20 — `x-ai/grok-4.20` (family=x-ai)

| probe | n_pass/K | cause tally |
|---|---|---|
| g4 | 8/8 | {'pass': 8} |
| award_consistency | 0/8 | {'fail_format': 8} |
| discrimination | 0/8 | {'fail_substantive': 8} |
| disclosure_inversion | 8/8 | {'pass': 8} |
| negative_disclosure | 8/8 | {'pass': 8} |

- **eligible surfaces:** ['coherence', 'disclosure', 'settled_core']

## WIRED: `x-ai/grok-4.20` (family=x-ai)

Reaches >=5/8 on disclosure -> a SECOND valid disclosure family (with google/gemini-2.5-flash). Eligible: ['coherence', 'disclosure', 'settled_core']. Combined manifest written; R34.4 (>=2 families per scored surface) progress.

