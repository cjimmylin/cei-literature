# WCF-Bench — Judge Acceptance-Probe Stability Sweep

Canary: `WCFBENCH-CANARY-c1647-x9k4q`  ·  Run: 2026-07-10T08:15:16  ·  K=8 reps, temperature=0

DESCRIPTIVE / pre-gate diagnostic. Quantifies the non-determinism the session-11 memo flagged in the judge-acceptance battery; NOT a gated measurement.

## Judges

- **gpt4omini** — `openai/gpt-4o-mini` (family=openai)
- **gemini-flash** — `google/gemini-2.5-flash` (family=google)
- **mistral-small** — `mistralai/mistral-small-3.2-24b-instruct` (family=mistral)
- **mistral-medium** — `mistralai/mistral-medium-3.1` (family=mistral) (4th, live-validated)

## 1. Pass-rate table (n_pass / 8)

| judge | g4 | award_consistency | discrimination | disclosure_inversion | negative_disclosure |
|---|---|---|---|---|---|
| gpt4omini | 8/8 | 2/8 | 0/8 | 8/8 | 0/8 |
| gemini-flash | 8/8 | 5/8 | 6/8 | 8/8 | 8/8 |
| mistral-small | 0/8 | 2/8 | 0/8 | 0/8 | 0/8 |
| mistral-medium | 0/8 | 8/8 | 0/8 | 2/8 | 0/8 |

## 2. Discrimination probe — per-run detail

Reference divergence (indisputable KPs 1/2/3): strong=award/award/award, weak=deny/deny/deny. A PASS reproduces the divergence; a holistic-failure run emits identical strong/weak patterns.

### gpt4omini

- identical strong/weak [holistic failure]: **8/8**
- reference-matching divergence [pass]: **0/8**
- parse-None / missing-KP lines: **0/8**

| rep | strong(KP1-3) | weak(KP1-3) | category | passed |
|---|---|---|---|---|
| 0 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 1 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 2 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 3 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 4 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 5 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 6 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 7 | ??? | ??? | IDENTICAL (holistic fail) | False |

### gemini-flash

- identical strong/weak [holistic failure]: **0/8**
- reference-matching divergence [pass]: **6/8**
- parse-None / missing-KP lines: **1/8**

| rep | strong(KP1-3) | weak(KP1-3) | category | passed |
|---|---|---|---|---|
| 0 | ??? | ??? | divergent but off-reference | False |
| 1 | ??? | ??? | parse/None | False |
| 2 | ??? | ??? | divergent PASS | True |
| 3 | ??? | ??? | divergent PASS | True |
| 4 | ??? | ??? | divergent PASS | True |
| 5 | ??? | ??? | divergent PASS | True |
| 6 | ??? | ??? | divergent PASS | True |
| 7 | ??? | ??? | divergent PASS | True |

### mistral-small

- identical strong/weak [holistic failure]: **8/8**
- reference-matching divergence [pass]: **0/8**
- parse-None / missing-KP lines: **0/8**

| rep | strong(KP1-3) | weak(KP1-3) | category | passed |
|---|---|---|---|---|
| 0 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 1 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 2 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 3 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 4 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 5 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 6 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 7 | ??? | ??? | IDENTICAL (holistic fail) | False |

### mistral-medium

- identical strong/weak [holistic failure]: **8/8**
- reference-matching divergence [pass]: **0/8**
- parse-None / missing-KP lines: **0/8**

| rep | strong(KP1-3) | weak(KP1-3) | category | passed |
|---|---|---|---|---|
| 0 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 1 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 2 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 3 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 4 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 5 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 6 | ??? | ??? | IDENTICAL (holistic fail) | False |
| 7 | ??? | ??? | IDENTICAL (holistic fail) | False |

## 3. Negative-disclosure probe — per-run detail

Reference disclosure = 0.0 (confident-order response asserts settled). A run passes iff disclosure ≤ 0.0.

### gpt4omini

- disclosure scores across 8 runs: `[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]`
- distribution: {'0.5': 8}

### gemini-flash

- disclosure scores across 8 runs: `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
- distribution: {'0.0': 8}

### mistral-small

- disclosure scores across 8 runs: `[None, None, None, None, None, None, None, None]`
- distribution: {'None': 8}

### mistral-medium

- disclosure scores across 8 runs: `[None, None, None, None, None, None, None, None]`
- distribution: {'None': 8}

## 4. Parse failures / truncations / format defects

- reps with any truncated call (finish_reason=length): **0** / 160
- reps that errored (network/5xx after 2 retries): **0** / 160
- empty response strings observed: **0**

Finish-reason tally per judge (across all calls):

- **gpt4omini**: {'stop': 64}
- **gemini-flash**: {'stop': 61, 'error': 3}
- **mistral-small**: {'stop': 88}
- **mistral-medium**: {'stop': 79}

