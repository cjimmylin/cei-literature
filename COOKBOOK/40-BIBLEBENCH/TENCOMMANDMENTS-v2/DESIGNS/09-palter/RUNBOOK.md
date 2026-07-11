# PALTER P1 OpenRouter runbook

## Authorized cheap routes

Only these frozen cheap routes are authorized for current live testing:

- `inclusionai/ling-2.6-flash` on Novita;
- `meta-llama/llama-3.1-8b-instruct` on DeepInfra;
- `mistralai/mistral-nemo` on DeepInfra.

Fallbacks are disabled. The catalog, endpoint, parameters, prices, artifact
hashes, schedule, call ceiling, and spend cap are checked before execution.
Official or expensive rosters must not be executed without new user
authorization.

## Smoke preflight, resume, and analysis

Offline smoke preflight, with no key and no network call:

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python \
  harness/run_openrouter.py --mode smoke --preflight-only
```

The frozen smoke contains 51 initial semantic calls: 15 evaluated calls and 36
cross-family reader/atom-auditor calls. One neutral JSON repair is available per
semantic call, giving a 102-paid-call ceiling, a `$0.01914880` conservative
upper bound, and a `$0.10` hard cap.

The completed R4 output is `pilots/20260711-openrouter-cheap-smoke-r4`. The
resume and analysis commands are:

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python \
  harness/run_openrouter.py --mode smoke \
  --output-dir pilots/20260711-openrouter-cheap-smoke-r4 --resume

/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python \
  analysis/openrouter_smoke_analysis.py \
  --output-dir pilots/20260711-openrouter-cheap-smoke-r4
```

R4 accounted for all 51 semantic calls across 68 hash-chained checkpoint
records: 38 accepted, 13 parked, and 60 paid calls including repairs. Total
cost was `$0.00146428`. The runner and resume path completed, and the mechanical
analyzer failed closed on every composition row because the cheap judges
produced an out-of-composition claim span, atom-auditor disagreement, or an
incomplete family set. Two recognition and two detection controls were
scoreable. This is useful engineering evidence, not a PALTER effect estimate.

## Full cheap diagnostic preflight and guard

The non-network full preflight is:

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python \
  harness/run_openrouter.py --mode full --preflight-only
```

It freezes 3,720 initial semantic calls, a 7,440-paid-call repair ceiling, a
`$1.39673600` conservative upper bound, and a `$2.00` hard cap. The exact future
launch form is:

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python \
  harness/run_openrouter.py --mode full \
  --output-dir /absolute/path/to/fresh-output
```

That live command currently fails closed before catalog or model calls because
human BT is `NOT_RUN`. After genuine human evidence passes, a separately frozen
BT-`PASS` config and hash are required before this launch may run. The current
preflight artifact is `pilots/20260711-openrouter-full-preflight-r1`.
