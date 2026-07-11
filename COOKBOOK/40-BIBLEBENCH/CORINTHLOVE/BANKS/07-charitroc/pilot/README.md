# CHARITROC panel runner

`run_panel.py` is the provider-explicit, resumable runner for the frozen
CHARITROC panel: `gpt-5.5`, `gpt-5.4`, and `gpt-5.4-mini`, all at medium
reasoning effort. GPT-5.6 Sol is excluded. The manifest forbids model fallback
or substitution.

The runner does not contain a hidden fake mode and does not make a network call
unless `--run-mode live` is supplied. Test fixtures invoke mock mode through the
Python API and every mock artifact is labeled exactly
`harness validation, NOT a measurement`.

## Prerequisites

- Run from the `07-charitroc` bank root.
- Use `/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python`.
- Complete the bank regeneration/static-gate phase first. Live construction
  refuses to start unless the persisted public, calibration, private, ground
  truth, and judge-token artifacts exist and agree.
- Use a new output directory for each provider. `run_metadata.json` binds an
  output directory to one provider and one run mode.
- Codex runs require the frozen Codex CLI version/configuration. OpenRouter runs
  require `OPENROUTER_API_KEY` in the process environment. The key is read only
  at call time, is never written, and is rejected if it appears in an artifact.

Set this shell convenience variable:

```bash
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
```

## Live command sequence

Use one output root for the complete provider run. The production freeze binds
the calibration analysis in that root, so calibration and private execution
must not be split across unrelated roots. Codex example:

```bash
OUT=pilot/runs/20260710-codex

$PY pilot/run_panel.py access \
  --out "$OUT" --provider codex --run-mode live
$PY pilot/run_panel.py verify-access \
  --out "$OUT" --provider codex --run-mode live
$PY pilot/run_panel.py smoke \
  --out "$OUT" \
  --provider codex --run-mode live
$PY pilot/run_panel.py verify \
  --out "$OUT" \
  --provider codex --run-mode live --stage smoke

$PY pilot/run_panel.py calibration \
  --out "$OUT" \
  --provider codex --run-mode live
$PY pilot/run_panel.py reliability \
  --out "$OUT" \
  --provider codex --run-mode live
$PY pilot/run_panel.py analyze \
  --out "$OUT" \
  --provider codex --run-mode live

$PY pilot/run_panel.py freeze \
  --out "$OUT" \
  --provider codex --run-mode live
$PY pilot/run_panel.py private \
  --out "$OUT" \
  --provider codex --run-mode live
$PY pilot/run_panel.py analyze-private \
  --out "$OUT" --provider codex --run-mode live
```

If a provider/quota failure occurs during `access`, the failed first-stage
evidence is durably written under `access/failures/<model>/attempt-NN.json` and
the runner stops. It never silently repeats that provider call. After the
external condition is confirmed resolved, authorize the retry explicitly:

```bash
$PY pilot/run_panel.py access \
  --out "$OUT" --provider codex --run-mode live \
  --retry-failed-access
```

Only when `private-analysis-96.json` says `action: extend_to_192` and
`extension_allowed: true`, activate and run the predeclared extension exactly
once:

```bash
$PY pilot/run_panel.py activate-private-extension \
  --out "$OUT" --provider codex --run-mode live
$PY pilot/run_panel.py private-extension \
  --out "$OUT" --provider codex --run-mode live
$PY pilot/run_panel.py verify \
  --out "$OUT" --provider codex --run-mode live \
  --stage private-extension
$PY pilot/run_panel.py analyze-private \
  --out "$OUT" --provider codex --run-mode live
```

The final command writes the separate immutable
`reports/private-analysis-192.json`; it never overwrites the frozen 96-case
decision record.

For OpenRouter, use a separate output root, set `--provider openrouter`, and
provide `OPENROUTER_API_KEY` out of band. Never place the key in an argument,
log, JSON, YAML, Markdown file, or shell-history-bearing command.

The plans contain 24 smoke, 96 calibration, 24 reliability, and 96 primary
private occurrences. Each occurrence runs all three models before the next
occurrence begins. The predeclared additional 96 private occurrences remain
inactive unless the frozen 96-episode analysis authorizes the one-time
activation. Activated extension records use the separate `private-extension`
state, evidence, score, ledger, invocation, and report namespace while retaining
the original frozen private-plan hash.

## Persistence and resumption contract

For every provider stage, the runner first appends an invocation-journal start
that binds the orchestration attempt, integrity session, request hash, and
transport-descriptor hash. The validated sink immediately persists immutable
stage evidence and its exact attempt-ledger rows before the driver may advance
to the next stage. A completed stage is never marked abandoned merely because
its surrounding episode later stops; only a journaled start with neither
persisted evidence/ledger nor a terminal failure record is abandoned on resume.
Retries receive a new `orchestration-N` path and never overwrite prior bytes.
Every immutable write and append is flushed and `fsync`-committed before the
runner returns to the provider. If a crash lands between evidence and one of
several attempt-ledger rows, resume revalidates the immutable evidence and
reconstructs only the missing derived ledger rows before any later call.
The mechanical score is written before the terminal high-level state. A second
integrity session is explicit rather than disguised as an overwrite.

The output tree contains:

- `plans/`: deterministic, manifest-hashed occurrence plans.
- `access/`: the one-stage, non-bank model-access probe; never a measurement.
  Each exact-model probe is durably written before the next model is called,
  and the final report must byte-match all three provider-replayed probe files.
  Failed access evidence is separately immutable, provider-replayed, labeled
  `model access probe, NOT a measurement`, and requires an explicit retry.
- `state/`: append-only high-level execution state.
- `invocations/`: append-only provider-stage start/abandonment journal.
- `ledger/`: append-only stage-attempt records.
- `evidence/`: immutable requests, raw results, transport descriptors, and
  attestations, one object per stage.
- `failures/`: preserved non-measurement OpenRouter protocol-attempt records.
- `scores/`: sidecar-derived mechanical scoring only.
- `judge_queue/`: blinded unresolved cases. There is no parsing repair,
  semantic replacement, or guessed score.
- `reports/`: harness-integrity, calibration analysis, distinct sealed-private
  96/192 analyses, and the one-time extension activation record.

`verify` rereads all persisted bytes, validates confined paths, hashes, schemas,
and state transitions, then replays every provider evidence validator. It
requires bidirectional invocation/evidence/ledger accounting, rebuilds every
score from trusted sidecar truth plus final evidence, rebuilds every unresolved
judge-queue row from the raw response, and rederives reliability links.
Standalone reliability verification first performs full trusted calibration
verification. Missing,
extra, duplicate, or tampered records fail closed. It is safe to run repeatedly.

## Measurement interpretation

Smoke validates the harness; it is not a discrimination estimate. Calibration
analysis reports stage-4 ordinal AUC/operating points separately from stage-3
updating, retains all family rows and all nine prior-by-cost cells, links the
reliability repeat to its exact calibration score hash, and reports ambiguity-
control sensitivity without scalarizing the channels. Live analysis always
uses and records 2,000 bootstrap draws; reduced draws are test-only and are
refused in live mode.

Do not interpret a report unless `harness.measurement_ready` is true. `freeze`
also refuses live private launch unless the calibration report rederives with a
valid self-hash/provider/provenance, complete harness, non-saturated and
informative results, passing discrimination, and passing ambiguity controls.
Unresolved
or invalidated cases remain visible and queued; they are never repaired into a
measurement. `freeze` writes a companion private-protocol freeze that binds the
construction freeze, calibration-analysis file hash, frozen confirmation
criteria, private plan, and extension entries. Those surfaces are validated
again in the `before_stage` hook immediately before every primary-private or
private-extension provider stage.
