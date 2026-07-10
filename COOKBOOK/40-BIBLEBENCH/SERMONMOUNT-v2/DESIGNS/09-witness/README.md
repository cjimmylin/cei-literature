# WITNESS (v2-09) — build

The profession–behaviour **gap-surface** methodology: identical moral content probed in four
matched modalities — **END** (endorse) → **REC** (recognize) → **GEN** (generate) → **ACT**
(act, tool sandbox) — holding moral structure/parties/stakes constant, subtracting a non-moral
format-difficulty control, and reporting per-principle **signed** gaps (END–ACT, REC–ACT,
GEN–ACT) as a 40-principle × contrast surface. Brief: `../09-witness.md` (§2/§8 LOCKED).

WITNESS is build 1 of the v2 portfolio: its 30 pilot cores are the **shared seed stock**
(`../../SHARED/core-ledger.jsonl`) that designs 02/05/06/08 re-skin (guide §3).

## ⚠ Live-readiness status

The available P1 is a **harness validation**: a deterministic `MockModelClient` with a
hand-set gap profile checks whether the analysis recovers injected structure. Mock
manifests, scored rows, shared-score rows, gate tables, and reports are explicitly labeled
**SIMULATED**; their numbers are not measurements of any real model.

API access remains a credential blocker, but **keys do not make the live path ready**.
Noncredential blockers remain: tested-model and judge adapters are stubs; the shared judge
stack is not calibrated or integrated; immutable provider evidence plus completion,
refusal, and retry gates are not wired; and the preregistered A6 deviation, G4b action-
classifier, and human-baseline gates are not executable end to end. Generating/tested-family
provenance and the resulting two-eligible-judge-family arithmetic are unresolved, as is the
nominal-pole κw definition. Those provenance/κw choices remain reserved for Fable/Jimmy and
must not be inferred or weakened to make a live run pass. Historical dated reports under
`pilots/` remain immutable evidence of their own earlier runs.

## Layout
```
witness_common.py     schema + LOCKED-gate validator (END-no-particulars, REC-counterfeit,
                      two-sided, no-Sermon-leakage) + I/O
itembank/  seed_cores.py, cores_batch_{A,B,C}.py  -> hand-authored cores
           build_bank.py  -> merge+validate+invariants -> cores.jsonl (+ SHARED ledger)
           render.py      -> renderings.jsonl  (4 matched modalities × 2 skins)
           format_control.py -> validate format_control.jsonl; --write-new PATH creates safely
harness/   model_client.py (mock + real stubs), act_sandbox.py, run_p1.py (session hygiene)
scoring/   score_end.py, score_rec.py, action_classifier.py, judge.py, signal_match.py
audits/    leakage_audit.py (hard gate), matching_audit.py (§9a), shortcut_audit.py
analysis/  gap_surface.py, stability_bootstrap.py, prediction_test.py, make_report.py, stats_util.py
tests/     test_witness.py + test_mf1_controls.py + test_mf2_mf5_analysis.py
           + test_mf4_rec_shortcuts.py + test_mf6_run_isolation.py
           (pytest acceptance and regression gates)
pilots/    20260706-p1-run/ (scored.jsonl, qc.json, gap_surface.jsonl, …) + dated report
```

## MF-4 REC remediation status

The 30 REC quadruples have been semantically rewritten so every option remains anchored to
the case's parties and stakes; the S38×3, S09-01/-02, S28×3, and W-S19-02 counterfeits have
explicit regression snapshots. `shortcut_audit.py` is now a hard gate: each core must meet
the exact 10% character-length parity bound; fractional and conservative longest/overlap
baselines must all be ≤0.40; and fractional shortest-pole credits must be counterbalanced
within `[floor(n/4), ceil(n/4)]`. That last interval is the build's documented operational
definition of "no pole systematically shortest," not a quotation from the governing memo.
The script applies every gate to the merged 30-core bank and independently to
`seed_cores.jsonl` and batches A/B/C, so cross-batch cancellation cannot create a pass.
The regenerated shared ledger carries the new content hashes. The complete 20260709 fix-session
review passes MF-1 through MF-8, so the review memo's MF-4 provisional condition is discharged.
That does not authorize the 240-core build-out: the live-P1 and reserved-decision gates remain.

## Reproduce (deterministic; run from `CEI-Lit-WS/`)
```bash
PY=../.venv/bin/python ; D=COOKBOOK/40-BIBLEBENCH/SERMONMOUNT-v2/DESIGNS/09-witness
$PY $D/itembank/seed_cores.py --write && $PY $D/itembank/cores_batch_A.py --write \
  && $PY $D/itembank/cores_batch_B.py --write && $PY $D/itembank/cores_batch_C.py --write
$PY $D/itembank/build_bank.py           # -> cores.jsonl + SHARED/core-ledger.jsonl
$PY $D/itembank/render.py               # -> renderings.jsonl
$PY $D/itembank/format_control.py --check  # validate canonical 15-base/60-row artifact
$PY $D/audits/leakage_audit.py          # hard gate (must PASS)
$PY $D/audits/matching_audit.py         # §9a
$PY $D/audits/shortcut_audit.py         # hard MF-4 REC lexical/parity gate (must PASS)
: "${DATE:?export a fresh YYYYMMDD DATE}" ; : "${RUN_ID:?export a fresh unique RUN_ID}"
RUN_DIR="$(pwd)/$D/pilots/${DATE}-${RUN_ID}"
SHARED_SCORE="$(pwd)/COOKBOOK/40-BIBLEBENCH/SERMONMOUNT-v2/SHARED/scores/09-witness-${DATE}.jsonl"
$PY $D/harness/run_p1.py --run-date "$DATE" --run-id "$RUN_ID" \
  --output-dir "$RUN_DIR" --models mock-alpha mock-beta mock-gamma --repeats 10
$PY $D/analysis/gap_surface.py --run-dir "$RUN_DIR" --date "$DATE" \
  --shared-score "$SHARED_SCORE"
$PY $D/analysis/stability_bootstrap.py --run-dir "$RUN_DIR"
$PY $D/analysis/prediction_test.py --run-dir "$RUN_DIR"
$PY $D/analysis/make_report.py --run-dir "$RUN_DIR" --date "$DATE" \
  --report "$D/pilots/${DATE}-witness-p1-report.md"
$PY -m pytest $D/tests/test_witness.py $D/tests/test_mf1_controls.py \
  $D/tests/test_mf2_mf5_analysis.py $D/tests/test_mf4_rec_shortcuts.py \
  $D/tests/test_mf6_run_isolation.py -q
```

`RUN_DIR` must be absolute, must be named `${DATE}-${RUN_ID}`, and must not already exist.
The runner refuses it before loading items or initializing a provider otherwise. It creates
`run_manifest.json`, `audit_log.jsonl`, `scored.jsonl`, and `qc.json` only for a completed
asserted run. The analysis step creates the run-local hashed audit snapshot and refuses to
overwrite either run-local outputs or the dated guide-§7 shared score.

## Live path (not yet runnable)

Implementing a tested-model client is only one part of the live path. A live run also needs
independent judge adapters and calibrated shared-judge integration, raw immutable provider
evidence with retry/refusal/completion handling, eligible-family provenance, and executable
A6/G4b/human gates. Only after those checks pass may a provider declare
`execution_type = "LIVE"`; the analysis then binds that evidence class and run ID into every
shared-score row and report gate. Supplying credentials alone must not relabel a simulated or
incompletely evidenced run as live.

## Hard rules honoured
Scope isolation (SERMONMOUNT corpus + v1 + KB only); LOCKED §2/§8 untouched; no Sermon/registry
language in any tested-model prompt (leakage audit = 0); X-VULN floor (no core scores
endure-abuse/waive-protection as gold); vault safety (no deletions; new dated report only).
