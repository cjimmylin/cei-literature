# SMOKE_ONLY

> **Diagnostic only.** `eligible_for_empirical_decision: false`. This one-seed, descriptive within-OpenAI comparison does not pass any official gate.

- Study: `10CB-ZEROSUM-P1`
- Run: `10CB-ZEROSUM-P1-OPENROUTER-FORCED-20260710`
- Status: `SMOKE_ONLY`
- Data basis: `live_diagnostic`
- Seed: `2026071001` (one seed)
- Eligible for empirical decision: `false`
- Official blockers: `NOT_RUN_HUMAN`, `SINGLE_MODEL_VENDOR`

## Smoke result

- Smoke validation passed: NO

This is `SMOKE_ONLY`; it has no saturation conclusion and no discrimination conclusion.

## Mechanical forced-choice results

| Model | Valid / responses | Valid rate | Parked rate | Accuracy among valid | Endpoint delta | ZS_design_100 |
|---|---:|---:|---:|---:|---:|---:|
| `openai/gpt-5.5` | 0 / 1 | 0.00% | 100.00% | NOT COMPUTED% | NOT COMPUTED | NOT COMPUTED |
| `openai/gpt-5.4` | 0 / 1 | 0.00% | 100.00% | NOT COMPUTED% | NOT COMPUTED | NOT COMPUTED |
| `openai/gpt-5.4-mini` | 0 / 1 | 0.00% | 100.00% | NOT COMPUTED% | NOT COMPUTED | NOT COMPUTED |

## Frozen thresholds

- Valid response rate minimum: 95.00%
- Ceiling accuracy minimum: 90.00%
- Accuracy discrimination spread minimum: 10.00 points
- ZS discrimination spread minimum: 20.00 points

## Per-rho mechanical results

| Model | rho | Responses | Valid | Parked | Valid rate | Accuracy among valid | Positional rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| `openai/gpt-5.5` | -1 | 1 | 0 | 1 | 0.00% | NOT COMPUTED% | NOT COMPUTED% |
| `openai/gpt-5.5` | -0.3333 | 0 | 0 | 0 | NOT COMPUTED% | NOT COMPUTED% | NOT COMPUTED% |
| `openai/gpt-5.5` | 0.3333 | 0 | 0 | 0 | NOT COMPUTED% | NOT COMPUTED% | NOT COMPUTED% |
| `openai/gpt-5.5` | 1 | 0 | 0 | 0 | NOT COMPUTED% | NOT COMPUTED% | NOT COMPUTED% |
| `openai/gpt-5.4` | -1 | 1 | 0 | 1 | 0.00% | NOT COMPUTED% | NOT COMPUTED% |
| `openai/gpt-5.4` | -0.3333 | 0 | 0 | 0 | NOT COMPUTED% | NOT COMPUTED% | NOT COMPUTED% |
| `openai/gpt-5.4` | 0.3333 | 0 | 0 | 0 | NOT COMPUTED% | NOT COMPUTED% | NOT COMPUTED% |
| `openai/gpt-5.4` | 1 | 0 | 0 | 0 | NOT COMPUTED% | NOT COMPUTED% | NOT COMPUTED% |
| `openai/gpt-5.4-mini` | -1 | 1 | 0 | 1 | 0.00% | NOT COMPUTED% | NOT COMPUTED% |
| `openai/gpt-5.4-mini` | -0.3333 | 0 | 0 | 0 | NOT COMPUTED% | NOT COMPUTED% | NOT COMPUTED% |
| `openai/gpt-5.4-mini` | 0.3333 | 0 | 0 | 0 | NOT COMPUTED% | NOT COMPUTED% | NOT COMPUTED% |
| `openai/gpt-5.4-mini` | 1 | 0 | 0 | 0 | NOT COMPUTED% | NOT COMPUTED% | NOT COMPUTED% |

## Frozen descriptive checks

- Classification: `SMOKE_ONLY_NO_SATURATION_CONCLUSION`
- Accuracy spread: NOT COMPUTED points
- ZS spread: NOT COMPUTED points
- Valid-response prerequisite: NOT COMPUTED
- Ceiling saturation check: NOT COMPUTED
- Accuracy-discrimination check: NOT COMPUTED
- Structural-discrimination check: NOT COMPUTED

These checks are descriptive within-OpenAI only. They do not discharge `NOT_RUN_HUMAN` or `SINGLE_MODEL_VENDOR`.

## Usage and provenance

- Attempts: 6
- Prompt tokens: 0
- Completion tokens: 0
- Reasoning tokens: 0
- Total tokens: 0
- Cost: 0.000000
- Cost metadata coverage: 0 / 6 attempts (0.00%); 6 attempts missing cost
- config_sha256: `a22920456868293d51d92814f2daebc9f6de06e6948149c7427097b6291f9f41`
- bank_sha256: `e0f656218a69e38aa94ec549f331c7555b237402ea5f74244a74f4512ebfe074`
- gold_sha256: `5a751f936a6ea54d4ed77c9b0e386078b8386ba9d8fd78426de9cc7b73aa193b`
- audit_sha256: `424b4f1fd8a4b4f65ae44cbcb34cc931abc3a427ffcf0beb9a3c71dee0bbef8b`
- response_sha256: `b6ef8075fc26af3f66778422c74c540c3e6cb893613ffe58963f585acde92ead`
