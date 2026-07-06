# WITNESS (v2-09) — build

The profession–behaviour **gap-surface** methodology: identical moral content probed in four
matched modalities — **END** (endorse) → **REC** (recognize) → **GEN** (generate) → **ACT**
(act, tool sandbox) — holding moral structure/parties/stakes constant, subtracting a non-moral
format-difficulty control, and reporting per-principle **signed** gaps (END–ACT, REC–ACT,
GEN–ACT) as a 40-principle × contrast surface. Brief: `../09-witness.md` (§2/§8 LOCKED).

WITNESS is build 1 of the v2 portfolio: its 30 pilot cores are the **shared seed stock**
(`../../SHARED/core-ledger.jsonl`) that designs 02/05/06/08 re-skin (guide §3).

## ⚠ Credential status
No API keys in this vault → the live multi-model P1 is **credential-gated** (the Fable/
credential STOP point). The P1 here is a **harness validation**: a deterministic
`MockModelClient` with a hand-set gap profile proves the analysis recovers injected
structure. **Its numbers are not a measurement of any model.** Real clients are stubbed
(`harness/model_client.py`); wiring a key runs the identical pipeline for real. See
`pilots/20260706-witness-p1-report.md`.

## Layout
```
witness_common.py     schema + LOCKED-gate validator (END-no-particulars, REC-counterfeit,
                      two-sided, no-Sermon-leakage) + I/O
itembank/  seed_cores.py, cores_batch_{A,B,C}.py  -> hand-authored cores
           build_bank.py  -> merge+validate+invariants -> cores.jsonl (+ SHARED ledger)
           render.py      -> renderings.jsonl  (4 matched modalities × 2 skins)
           format_control.py -> format_control.jsonl (15 bases × 4 formats)
harness/   model_client.py (mock + real stubs), act_sandbox.py, run_p1.py (session hygiene)
scoring/   score_end.py, score_rec.py, action_classifier.py, judge.py, signal_match.py
audits/    leakage_audit.py (hard gate), matching_audit.py (§9a), shortcut_audit.py
analysis/  gap_surface.py, stability_bootstrap.py, prediction_test.py, make_report.py, stats_util.py
tests/     test_witness.py   (pytest, 15 tests)
pilots/    20260706-p1-run/ (scored.jsonl, qc.json, gap_surface.jsonl, …) + dated report
```

## Reproduce (deterministic; run from `CEI-Lit-WS/`)
```bash
PY=../.venv/bin/python ; D=COOKBOOK/40-BIBLEBENCH/SERMONMOUNT-v2/DESIGNS/09-witness
$PY $D/itembank/seed_cores.py --write && $PY $D/itembank/cores_batch_A.py --write \
  && $PY $D/itembank/cores_batch_B.py --write && $PY $D/itembank/cores_batch_C.py --write
$PY $D/itembank/build_bank.py           # -> cores.jsonl + SHARED/core-ledger.jsonl
$PY $D/itembank/render.py               # -> renderings.jsonl
$PY $D/itembank/format_control.py       # -> format_control.jsonl
$PY $D/audits/leakage_audit.py          # hard gate (must PASS)
$PY $D/audits/matching_audit.py         # §9a
$PY $D/audits/shortcut_audit.py         # finding: REC lexical overlap (see report §3)
$PY $D/harness/run_p1.py                # -> scored.jsonl, qc.json
$PY $D/analysis/gap_surface.py          # -> gap_surface.jsonl + SHARED score file
$PY $D/analysis/stability_bootstrap.py
$PY $D/analysis/prediction_test.py
$PY $D/analysis/make_report.py          # -> pilots/20260706-witness-p1-report.md
$PY -m pytest $D/tests/test_witness.py -q
```

## Wiring a real model (credential path)
Implement `AnthropicClient.respond` (SDK installed) and/or `CodexClient` (OAuth CLI on PATH)
in `harness/model_client.py`, add the spec to `run_p1.MOCK_MODELS`→real list. END/REC are
text completions; GEN is open text; ACT is a tool-use loop against `act_sandbox`. Everything
downstream (scoring, audits, analysis, report) is unchanged.

## Hard rules honoured
Scope isolation (SERMONMOUNT corpus + v1 + KB only); LOCKED §2/§8 untouched; no Sermon/registry
language in any tested-model prompt (leakage audit = 0); X-VULN floor (no core scores
endure-abuse/waive-protection as gold); vault safety (no deletions; new dated report only).
```
