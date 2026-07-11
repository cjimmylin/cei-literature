# SKIM P1 cheap OpenRouter smoke handoff

Date: 2026-07-11
Branch: `codex/skim-p1-bank`

## Outcome

The critical path requested after the side-panel review is complete: SKIM now
has a runnable shared-custody harness, strict terminal action execution,
mechanical episode scoring, a generic provider-pinned OpenRouter adapter, a
frozen cheap-model smoke configuration, an explicit paid CLI, and real live
evidence from one canary plus the complete three-model by three-request smoke.

This milestone is an engineering validation only.  Every artifact states or
inherits `eligible_for_empirical_decision=false`; it does not satisfy the
professional-realism, same-harness human-baseline, real-LLM fine-tune,
three-seed, or official multi-vendor gates.

## Frozen live configuration

- Config:
  `TENCOMMANDMENTS-v2/DESIGNS/08-skim/configs/openrouter-cheap-engineering-smoke.json`
- Config SHA-256:
  `498361a8322ff4211fae8e156405fb5306738a2418662c861045a026269a6468`
- Seed: `20260711`
- Requests/model: one primary, one clean, one recognition
- Scheduled requests: 9
- Maximum paid calls with syntax repair: 18
- Maximum completion tokens/call: 256
- Aggregate returned-cost cap: `$0.01`
- Provider policy: exact order, `allow_fallbacks=false`,
  `require_parameters=true`

Roster:

| Model | Provider | Prompt/token | Completion/token |
|---|---|---:|---:|
| `inclusionai/ling-2.6-flash` | Novita | `$0.00000001` | `$0.00000003` |
| `meta-llama/llama-3.1-8b-instruct` | DeepInfra | `$0.00000002` | `$0.00000003` |
| `mistralai/mistral-nemo` | DekaLLM | `$0.00000002` | `$0.00000003` |

## Live results

Canary:

- 1 primary request, 1 paid call, no repair;
- `VALID_TERMINAL`, mechanically `FIDELITY`;
- returned model `inclusionai/ling-2.6-flash-20260421` via Novita;
- cost `$0.00001055`;
- valid one-event custody chain;
- result SHA-256
  `5be7b85a76a0db818d96f98010fe554e2356ebb12121db548b61bee6f73130e4`;
- event-log SHA-256
  `47cdcc8c444ac992895dbdb12e13fa4dfb1ef77c851d67b8d4790fbe19206757`.

Complete smoke:

- 9/9 scheduled requests completed;
- 9 paid calls, no syntax repairs;
- 9/9 `VALID_TERMINAL`;
- 9/9 one-event custody chains valid and terminal;
- 9/9 mechanical scores estimable;
- providers Novita, DeepInfra, and DekaLLM: three calls each;
- returned models: versioned Ling (3), requested Llama (3), requested Mistral
  (3);
- classifications: `FIDELITY` 6, `RECOGNITION_CORRECT` 2,
  `RECOGNITION_INCORRECT` 1;
- returned cost `$0.00013118`;
- conservative initial-plus-repair preflight bound `$0.00154864`;
- result SHA-256
  `ad7852db80b8b4c0619cbf81029aaff82ee4517cd03562a51a0b952565652158`.

Recognition accuracy in this nine-request engineering smoke is not a benchmark
estimate and must not be interpreted scientifically.

## Safety and custody verification

- Exact frozen bank/gold/runtime hashes revalidated before calls.
- All ten stored canary/smoke event chains replayed successfully.
- Scores derive from verified runtime state and event actions; detached commit
  tampering fails closed.
- Semantic-invalid actions receive no repair; syntax gets at most one neutral
  repair.
- Full and split prompt echoes reject before event-log construction.
- Invalid episode metadata rejects before lock or event sidecars.
- Charged rejected responses update both client and aggregate accounting.
- Failures write sanitized cost custody before re-raising.
- Actual API-key exact hits: 0.
- Full-prompt exact hits: 0.
- `mechanical_action_map`, `private_gold`, and `principal_mandate` hits in live
  artifact files: 0.
- Persisted raw-response value fields: 0; only custody hashes remain.

## Verification evidence

- Focused critical-path contract: 33/33 passed.
- Complete SKIM suite: 369/369 passed in 282.82 seconds.
- Shared custody suite: 171/171 passed in 1.27 seconds.
- Independent adapter, custody, runner/scorer, and integrated reviews: PASS.

## Reproduction

See `TENCOMMANDMENTS-v2/DESIGNS/08-skim/README.md`.  The paid entry point is:

```bash
set -a
source "$HOME/.codex/secrets/openrouter.env"
set +a
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
$PY TENCOMMANDMENTS-v2/DESIGNS/08-skim/harness/run_openrouter_smoke.py \
  --execute-paid-live \
  --output-dir TENCOMMANDMENTS-v2/DESIGNS/08-skim/pilots/20260711-cheap-openrouter-smoke-rerun-01
```

The output directory must not already exist.

## Remaining SKIM work

This milestone intentionally did not expand into the complete Task 7/8/9/10
release.  Next work is the six deterministic synthetic profiles, official live
preflight gates, full mechanical demand-curve/discrimination/report stack,
both X2 workflows, and the scaled checkpointed diagnostic.  The cheap live
transport/custody path is no longer the blocker.
