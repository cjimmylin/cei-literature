# 2026-07-09 — Codex WITNESS Fix-Session Handoff

## Outcome

The binding WITNESS MF-1 through MF-8 fix session and all three Job 2 drafting jobs are
complete. The canonical 20260709 deterministic P1 rerun is green and explicitly
**SIMULATED**. It validates the instrument and analysis only; it is not evidence about any
real model, does not satisfy the live P1, and does not authorize the 240-core build-out.

The work is on branch `codex/sermonmount-witness-fix-20260709` in the isolated worktree:

```text
/Users/jimmy.lin/.config/superpowers/worktrees/CEI-Lit-WS/sermonmount-witness-fix-20260709
```

Base commit: `06c6c1754`. Nothing is staged or committed.

## Canonical deterministic evidence

- Report: [`DESIGNS/09-witness/pilots/20260709-witness-p1-report.md`](DESIGNS/09-witness/pilots/20260709-witness-p1-report.md)
- Run manifest: [`DESIGNS/09-witness/pilots/20260709-p1-run/run_manifest.json`](DESIGNS/09-witness/pilots/20260709-p1-run/run_manifest.json)
- Shared score: [`SHARED/scores/09-witness-20260709.jsonl`](SHARED/scores/09-witness-20260709.jsonl)
- Reproduction/readiness guide: [`DESIGNS/09-witness/README.md`](DESIGNS/09-witness/README.md)

The run contains 300 items, 45 cores, 60 controls, three deterministic mock models, ten
repeats, 10,350 unique one-call sessions, and 135 per-model/core audit records. The shared
score has 90 per-S-ID/model/tier rows; every row has a 90% CI and the explicit labels
`execution_type: SIMULATED` and `evidence: simulated`. All six holdout cores are absent from
every analysis, shared-score, and report artifact.

The primary analysis is the preregistered probability-scale DiD with a joint moral-core and
control-base cluster bootstrap at B=2,000. The full-precision state feeds prediction and
stability. B5 made a real attempt and records `UNAVAILABLE` because `Rscript` is absent; it
does not invent a robustness result.

Key SHA-256 values:

| Artifact | SHA-256 |
|---|---|
| `run_manifest.json` | `9b889034a98b57c538645fae6fcaffc7380cd81bfcfbe33191c2b2d12e30d088` |
| `scored.jsonl` | `07e82e89d4d8244b0a0bf5318921711dca1d9f49033d6516fc08af4664400dff` |
| `audit_log.jsonl` | `2c25c67a42a70604419c0b9e300101cbf5860ae8ca210f69483c13b52281cd20` |
| `gap_surface_state.jsonl` | `1d6b3f4ec0185de1e09dd33b9d7b1dbdf37c8403ccb0b9b8f3c8ddd8441a2069` |
| `prediction_test.json` | `e14e4378738946e2d835d28c960cfd57eba5ecb66c172db586b2b3bb930a48b6` |
| `stability.json` | `6f3dd274d92ecbd0ff5b29227cc1e2d2fb8d2e25a4aebb9b6bc7c683fde6dc1a` |
| dated report | `c868162d478b2fa9cdc3e392a94ea767618684a96e95147b8c390c8c5d0c0b16` |
| dated shared score | `8d7addad7e01802fe8094d563e3ca5fb6bcce25b8aa7a82e55bdab8daf99b990` |

## MF acceptance matrix

| Fix | Status | Mechanical evidence |
|---|---|---|
| MF-1 controls | PASS | 15 bases × 4 modalities; 5/5/5 difficulty bands; 43–63 words; matched REC/ACT structure; self-initiated ACT branches exercised. |
| MF-2 uncertainty | PASS | Probability DiD; exact B=2,000 joint cluster bootstrap; variance-share trigger; B4 estimator switch; legacy path only by explicit flag; B5 honest `UNAVAILABLE`. |
| MF-3 GEN | PASS | Natural paraphrase families and `pole_text`; zero underscore-style tool signals; frozen matcher SHA-256 `366d8bdd7e4ec0eb444d426908ee5b6221d14b181b4341556d22f5062f056420`; development blind audit 31/40 = .775, not production judge validity. |
| MF-4 REC | PASS | Semantic rewrites, not padding; longest .200/.233; overlap .300/.300; maximum parity .087591; shortest credits 7/8/7/8; merged and each authoring batch green. |
| MF-5 holdout | PASS | Six canonical holdout IDs excluded recursively from every analysis output, score export, and report. |
| MF-6 isolation | PASS | `_perm` drives execution; exact 30×2×4 moral plus 15×1×4 control shape; fresh retained client object per call; pre-spend reservation; streamed verification; failed stages preserved; no deletion APIs; Darwin/Linux atomic no-replace publication; final source-content/inode validation; live path fails closed. |
| MF-7 canary | PASS | Opaque canary/private training marker; 0/300 identity or benchmark leakage findings. |
| MF-8 END | PASS | Generic digit, currency, and capitalized multi-token proper-name detectors; all canonical END renderings green and mutations rejected. |

The stated MF-4 provisional condition on the regenerated shared ledger is discharged by the
complete MF-1–MF-8 review. This does not authorize build-out; the live-P1 and reserved
decision gates remain controlling.

## Job 2 deliverables

1. Shared judge stack: [`SHARED/judges/README.md`](SHARED/judges/README.md), implemented
   schemas/rubrics, and deterministic fail-closed scheduling, provenance, privacy,
   transformation, and result primitives. The core is operational but no live judge panel is
   selected, calibrated, or authorized.
2. Human baseline: [`20260709-witness-human-baseline-study-design.md`](20260709-witness-human-baseline-study-design.md).
3. LOGSPECK P1 preregistration: [`20260709-logspeck-p1-preregistration.md`](20260709-logspeck-p1-preregistration.md).

The three Job 2 documents have 35/35 resolving local links. The shared judge core has 97/97
passing tests.

## Final verification

- WITNESS tests: 291/291 passed.
- Shared judge tests: 97/97 passed.
- Combined: 388/388 passed.
- Format-control, leakage, matching, and REC shortcut hard audits: PASS.
- Independent publication-boundary review: PASS, including replacement-directory and
  in-place-content-change refusals, empty/nonempty target preservation, and successful-path
  atomic publication.
- Frozen judge plus eight historical artifact hashes: 9/9 exact.
- LOCKED `DESIGNS/09-witness.md` is byte-identical to HEAD, SHA-256
  `ea9449860f6d46bc2dce6e967ad9a032d4420cf988fada452941a4fade212bad`.
- Historical 20260706 pilot/report files are untouched.
- Scoped `git diff --check` is clean; the Git index is empty.

## Live P1 remains blocked

The parked note's statement that only credentials remain was too optimistic. Credentials are
necessary, but not sufficient. The current blockers are:

1. `AnthropicClient`, `CodexClient`, Gemini/tested-model adapters, and live model-judge
   adapters are not implemented end to end.
2. The shared judge core is not integrated with immutable raw provider transcripts,
   completion/refusal/retry handling, calibration data, and live assignment/result storage.
3. Material-generation-family provenance is unresolved. The eligible two-family judge
   arithmetic must be recomputed from explicit provenance; it may not be inferred or weakened.
4. The nominal-pole weighted-κ definition and other marked choices remain
   `RESERVED — Fable/Jimmy`.
5. The human baseline/deviation sample, action-classifier G4b human κ kill-gate, and remaining
   G1–G5/A6 imports, exports, and synthesis are designed but not executed end to end.
6. Environment checks found no Anthropic, Gemini, or OpenAI API credential. A Codex CLI is
   present, but its benchmark client remains a stub.

When the engineering and reserved-decision blockers are resolved, the user still needs to
supply Anthropic access and preferably Gemini access. Without an eligible third family, use
the preregistered A6 deviation protocol and the stratified human-label subsample; do not
silently relax judge-family exclusions.

## Next safe sequence

1. Resolve and record material-generation provenance and the reserved κw/judge-panel choices.
2. Implement tested-model and judge adapters plus immutable provider evidence and gate wiring.
3. Execute/calibrate the human and action-classifier validation requirements.
4. Add credentials, run the live P1, and apply A3–A8 mechanically.
5. Start the 240-core build-out only after the live decision authorizes it.

No existing `sermonmount-v2-portfolio-state` auto-memory file was found in the scoped vault
or Claude memory search. This dated handoff is the resumable state for the next session.
