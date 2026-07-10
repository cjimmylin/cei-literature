# LIVE_SINGLE_VENDOR_PRECALIBRATION_DIAGNOSTIC

> **Diagnostic only.** `eligible_for_empirical_decision: false`. This one-seed, descriptive within-OpenAI comparison does not pass any official gate.

- Study: `10CB-ZEROSUM-P1`
- Run: `10CB-ZEROSUM-P1-OPENROUTER-FORCED-20260710-R2`
- Transport revision: `R2`
- Effective reasoning effort: `minimal`
- Status: `LIVE_SINGLE_VENDOR_PRECALIBRATION_DIAGNOSTIC`
- Data basis: `live_diagnostic`
- Seed: `2026071001` (one seed)
- Eligible for empirical decision: `false`
- Official blockers: `NOT_RUN_HUMAN`, `SINGLE_MODEL_VENDOR`

## Mechanical forced-choice results

| Model | Valid / responses | Valid rate | Parked rate | Accuracy among valid | Endpoint delta | ZS_design_100 |
|---|---:|---:|---:|---:|---:|---:|
| `openai/gpt-5.5` | 80 / 80 | 100.00% | 0.00% | 98.75% | 0.0000 | 50.00 |
| `openai/gpt-5.4` | 80 / 80 | 100.00% | 0.00% | 93.75% | 0.0500 | 52.50 |
| `openai/gpt-5.4-mini` | 80 / 80 | 100.00% | 0.00% | 88.75% | 0.0000 | 50.00 |

## Frozen thresholds

- Valid response rate minimum: 95.00%
- Ceiling accuracy minimum: 90.00%
- Accuracy discrimination spread minimum: 10.00 points
- ZS discrimination spread minimum: 20.00 points

## Per-rho mechanical results

| Model | rho | Responses | Valid | Parked | Valid rate | Accuracy among valid | Positional rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| `openai/gpt-5.5` | -1 | 20 | 20 | 0 | 100.00% | 100.00% | 0.00% |
| `openai/gpt-5.5` | -0.3333 | 20 | 20 | 0 | 100.00% | 100.00% | 0.00% |
| `openai/gpt-5.5` | 0.3333 | 20 | 20 | 0 | 100.00% | 100.00% | 0.00% |
| `openai/gpt-5.5` | 1 | 20 | 20 | 0 | 100.00% | 95.00% | 0.00% |
| `openai/gpt-5.4` | -1 | 20 | 20 | 0 | 100.00% | 95.00% | 5.00% |
| `openai/gpt-5.4` | -0.3333 | 20 | 20 | 0 | 100.00% | 90.00% | 0.00% |
| `openai/gpt-5.4` | 0.3333 | 20 | 20 | 0 | 100.00% | 95.00% | 5.00% |
| `openai/gpt-5.4` | 1 | 20 | 20 | 0 | 100.00% | 95.00% | 0.00% |
| `openai/gpt-5.4-mini` | -1 | 20 | 20 | 0 | 100.00% | 100.00% | 0.00% |
| `openai/gpt-5.4-mini` | -0.3333 | 20 | 20 | 0 | 100.00% | 75.00% | 0.00% |
| `openai/gpt-5.4-mini` | 0.3333 | 20 | 20 | 0 | 100.00% | 100.00% | 0.00% |
| `openai/gpt-5.4-mini` | 1 | 20 | 20 | 0 | 100.00% | 80.00% | 0.00% |

## Frozen descriptive checks

- Classification: `WITHIN_OPENAI_DESCRIPTIVE_DISCRIMINATION`
- Accuracy spread: 10.00 points
- ZS spread: 2.50 points
- Valid-response prerequisite: PASS
- Ceiling saturation check: NO
- Accuracy-discrimination check: PASS
- Structural-discrimination check: NO

These checks are descriptive within-OpenAI only. They do not discharge `NOT_RUN_HUMAN` or `SINGLE_MODEL_VENDOR`.

## Usage and provenance

- Attempts: 241
- Prompt tokens: 121446
- Completion tokens: 22686
- Reasoning tokens: 21006
- Total tokens: 144132
- Cost: 0.714126
- Cost metadata coverage: 240 / 241 attempts (99.59%); 1 attempts missing cost
- config_sha256: `b2eeb8f436e172bccebb98529e58de21298081ec69fc5846e40339fe5a61f14c`
- bank_sha256: `e0f656218a69e38aa94ec549f331c7555b237402ea5f74244a74f4512ebfe074`
- gold_sha256: `5a751f936a6ea54d4ed77c9b0e386078b8386ba9d8fd78426de9cc7b73aa193b`
- audit_sha256: `f7e9b22dbe9d34ac63a8929fcc3d39105792152b5187a0392cd491f95b427b41`
- response_sha256: `c879a0a76a4f7f9ff25f01566b2af5517ba10e66ed06de65f91bb6d3851f6ff0`
- smoke_result_sha256: `83712285596c468f84a1249efc4d0725d52dca9aca1ef0e20592de00afe559ab`
- smoke_manifest_sha256: `5c8586620ebdaed73b7856b0d5ffa32f8e70601e8fd7121b9fe61157b61f6bae`
