# SKIM P1

SKIM P1 contains 640 frozen logical records, 640 aligned private-gold records,
and 800 executable runtime requests. The shared custody runtime lives at
`TENCOMMANDMENTS/harness/custody_stack`; SKIM composes that implementation and
does not maintain a second custody stack.

All OpenRouter runs described here are engineering diagnostics. They remain
`eligible_for_empirical_decision=false` and cannot satisfy the professional,
human-baseline, capability, multi-seed, or official-roster gates.

## Credential-free verification

Run from `COOKBOOK/40-BIBLEBENCH`:

```bash
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
$PY -m pytest TENCOMMANDMENTS-v2/DESIGNS/08-skim/tests -q
```

The full synthetic schedule can be replayed without credentials or paid calls:

```bash
$PY TENCOMMANDMENTS-v2/DESIGNS/08-skim/pilots/run_synthetic_validation.py \
  --output-dir TENCOMMANDMENTS-v2/DESIGNS/08-skim/pilots/synthetic-validation-rerun-01
```

The frozen R1 synthetic validation completed 14,400/14,400 episodes: 13,600
valid terminal episodes and 800 deliberately parked fixture cases, with 16,000
fixture calls, zero external paid calls, and zero cost. Its result SHA-256 is
`734b1eacc53dedd7108acf806685d019414484fa13c9c512274ee4391a406822`.
The expanded evidence is preserved locally and in
`pilots/20260711-synthetic-validation-r1/evidence.tar.gz`; its archive manifest
records the archive and source-result hashes.

## Cheap OpenRouter engineering smoke

The R2 smoke executes three requests (primary, clean, and recognition) against
each of three inexpensive model/provider pairs. Provider fallbacks are disabled
and one neutral syntax repair is permitted.

```bash
set -a
source "$HOME/.codex/secrets/openrouter.env"
set +a
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
$PY TENCOMMANDMENTS-v2/DESIGNS/08-skim/harness/run_openrouter_smoke.py \
  --execute-paid-live \
  --config TENCOMMANDMENTS-v2/DESIGNS/08-skim/configs/openrouter-cheap-engineering-smoke-r2.json \
  --output-dir TENCOMMANDMENTS-v2/DESIGNS/08-skim/pilots/cheap-openrouter-smoke-rerun-01
```

The frozen R2 smoke completed on 2026-07-11:

- 9/9 scheduled requests valid and mechanically scored;
- 9 paid calls through Novita and DeepInfra;
- total returned cost `$0.00013260` under a `$0.01` hard cap;
- conservative preflight bound `$0.00156400`;
- no credential, private-gold map, full prompt, or raw response serialized.

Artifacts are under `pilots/20260711-cheap-openrouter-smoke-r2/`. The smoke
configuration SHA-256 is
`5cf79207e29a38b2465c524f272e4cf8b97600267b46b2479373ca363f215597`;
the result SHA-256 is
`802b91ca8b01d346bd47fac55e4219ccc6f3b4cc26edb45243946c1dca746188`.

## Resumable cheap diagnostic

The frozen one-seed diagnostic schedules 800 requests for each cheap model,
2,400 total. It uses provider-pinned routing, per-model hash-chained
checkpoints, a 4,800-call ceiling, a `$1.00` hard cap, and retry only for HTTP
429 responses. A charged or ambiguously delivered row is never automatically
replayed. Parked rows remain part of the accounted schedule and are reported
separately from valid responses.

Start only in a new output directory:

```bash
set -a
source "$HOME/.codex/secrets/openrouter.env"
set +a
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
$PY TENCOMMANDMENTS-v2/DESIGNS/08-skim/harness/run_openrouter_diagnostic.py \
  --execute-paid-live \
  --max-workers 1 \
  --smoke-dir TENCOMMANDMENTS-v2/DESIGNS/08-skim/pilots/20260711-cheap-openrouter-smoke-r2 \
  --output-dir TENCOMMANDMENTS-v2/DESIGNS/08-skim/pilots/cheap-openrouter-full-rerun-01
```

Resume the preserved R1 run without replaying checkpointed rows:

```bash
$PY TENCOMMANDMENTS-v2/DESIGNS/08-skim/harness/run_openrouter_diagnostic.py \
  --execute-paid-live \
  --resume \
  --max-workers 1 \
  --smoke-dir TENCOMMANDMENTS-v2/DESIGNS/08-skim/pilots/20260711-cheap-openrouter-smoke-r2 \
  --output-dir TENCOMMANDMENTS-v2/DESIGNS/08-skim/pilots/20260711-cheap-openrouter-full-r1
```

After repeated HTTP 429s and both 5- and 15-minute cooldowns, the R1 diagnostic
was closed as provider-limited at 2,002/2,400 checkpointed episodes rather than
cycling the endpoint for hours. It preserves 1,983 valid terminal episodes and
19 parked episodes, accounts for 2,032 paid-call equivalents and `$0.032953218`,
and remains resumable at Mistral schedule index 2002. The explicitly incomplete
snapshot is
`pilots/20260711-cheap-openrouter-full-r1/provider-limited-result.json`, SHA-256
`47a2e5166b6e83414029f72e7054dfa80c813e83cd660b0ebc2637e49e93e8d9`.
The checkpoint and event evidence is preserved in that directory and in
`evidence.tar.gz`. On a fresh clone, extract the archive into the same run
directory before resuming; verify it against `evidence-manifest.json` first.

Rebuild a provider-limited snapshot only into a new filename after additional
checkpoint progress:

```bash
$PY TENCOMMANDMENTS-v2/DESIGNS/08-skim/analysis/checkpoint_snapshot.py \
  --smoke-dir TENCOMMANDMENTS-v2/DESIGNS/08-skim/pilots/20260711-cheap-openrouter-smoke-r2 \
  --output-dir TENCOMMANDMENTS-v2/DESIGNS/08-skim/pilots/20260711-cheap-openrouter-full-r1 \
  --output-name provider-limited-result-r2.json
```

If the remaining schedule is later completed and `diagnostic-result.json`
exists, build the deterministic complete-run engineering report into a new
path:

```bash
$PY TENCOMMANDMENTS-v2/DESIGNS/08-skim/analysis/engineering_report.py \
  --result TENCOMMANDMENTS-v2/DESIGNS/08-skim/pilots/20260711-cheap-openrouter-full-r1/diagnostic-result.json \
  --output TENCOMMANDMENTS-v2/DESIGNS/08-skim/pilots/20260711-cheap-openrouter-full-r1/engineering-report.json
```

## Scale-up boundary

Only the cheap engineering roster is authorized for live testing in the
current phase. The official 7,200-request schedule is defined in
`preregistration.md` and `configs/p1-live.example.json`, but its exact model
IDs, providers, catalog prices, and finite spend ceiling remain deliberately
unfrozen. It must remain `NOT_RUN` until those values are frozen and the user
authorizes the spend. A cheap diagnostic or synthetic result must never be
promoted to official evidence.

## Publication-only gates still not run

- professional realism panel;
- same-harness human baseline;
- real-LLM 10% fine-tune probe;
- frozen external capability PC1;
- official three-model, three-seed evidence.
