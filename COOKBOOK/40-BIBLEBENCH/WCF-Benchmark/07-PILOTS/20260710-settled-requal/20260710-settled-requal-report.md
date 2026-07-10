# WCF-Bench — R39(d) Settled-Core Re-qualification + R36.4 Frontier OPEN-Award Screen

Canary: `WCFBENCH-CANARY-c1647-x9k4q`  ·  Run: 2026-07-10T16:17:22  ·  K=8, gate >= 5/8, temperature=0

DESCRIPTIVE / pre-gate. The floor-gloss changed the settled-core prompt (now in `current_template_hashes()`), staling the third-family manifest; every judge re-qualifies the SETTLED_CORE surface via the NEW settled-core probe. All other surfaces are carried forward from the frozen third-family manifest.

## 1. Settled-core probe re-qualification (LIVE)

| judge | settled_core n_pass/K | cause tally | SETTLED_CORE eligible now? |
|---|---|---|---|
| gpt4omini | 0/8 | {'fail_substantive': 8} | NO — SUSPENDED |
| gemini-flash | 8/8 | {'pass': 8} | YES |
| grok-4.20 | 8/8 | {'pass': 8} | YES |

## 2. Combined manifest eligibility (carried-forward + settled requal + frontier)

| judge | family | eligible surfaces |
|---|---|---|
| gpt4omini | openai | ['coherence'] |
| gemini-flash | google | ['coherence', 'disclosure', 'open_award', 'settled_core'] |
| mistral-small | mistral | [] — discarded |
| mistral-medium | mistral | [] — discarded |
| grok-4.20 | x-ai | ['coherence', 'disclosure', 'settled_core'] |

- **SETTLED_CORE valid families:** ['google', 'x-ai'] (2)
- **OPEN_AWARD valid families:** ['google'] (1)
- **DISCLOSURE valid families:** ['google', 'x-ai'] (2)

## 3. Frontier OPEN-award screen (R36.4, LIVE)

| candidate | family | g4 | award-consist | discrimination | OPEN-award qualified? |
|---|---|---|---|---|---|
| command-a | cohere | 0/8 | 8/8 | 0/8 | no |
| nova-pro-v1 | amazon | 0/8 | 7/8 | 0/8 | no |

No frontier candidate qualified for the OPEN award. MVP ships single-family-labeled on OPEN award (R34.4 unchanged).

## 4. Fresh template hashes (settled-core now hashed — R35.6 gap closed)

- `award_consistency`: `b2cbf18372f43cf1`
- `disclosure`: `46587575fd092a9a`
- `discrimination`: `73dae2e859ebb62a`
- `g4`: `4480dbfb4d6f9e06`
- `settled_core`: `000f05c40f1c7343`

## 5. Guardrails

Report immutability: NEW dated dir; the third-family-screen manifest is FROZEN/untouched. Canary not re-minted. Secrets runtime-only. Scope-locked to WCF-Benchmark.

