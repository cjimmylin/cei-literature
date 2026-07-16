# F8 — parsers.py recovery-path fix (source-level) + equivalence proof

**Date:** 2026-07-16 (session 6) · **Authorization:** free code fix (F8, 20260716
adjudication, OR-7 / CV-5 cluster) — zero model calls. **Files:**
`walkworthy_inspect/parsers.py` (fix), `tests/test_parsers_f8.py` (regression),
`logs/f8-mock-20260716/` (mock run, gitignored).

## Defect (as shipped through session 5)

`reparse_allocation_response` returned a vacuous `ok=True, non_compliant=False,
allocation_values={}` on a block-less prose answer whenever the allocation spec was
degenerate (`tokens=[]`, `budget<=0`) — observed in the 20260715 live smoke
(§"Latent parser note") and flagged by OR-7. Mechanism: with `tokens=[]`,
`candidates = {}` so `all(candidates.values())` is vacuously True, `product()` of zero
pools yields one empty candidate, `_allocation_result` finds nothing missing (vacuous),
and `budget<=0` forces `sum_ok=True`. Two degenerate-truth idioms compose into a false
"compliant" flag. The headline CSR was never affected (empty allocation → no CSR →
unscorable), and M4's derived non-compliance (`csr unscorable ∧ empty
allocation_values`) already routed around the bad flag in the sanctioned reporting
path — the defect was in the per-sample `allocation_ok`/`non_compliant` metadata.

v1 (`harness/walkworthy/parsers.py::_allocation_result`) carries the identical edge;
v1 is READ-ONLY and stays untouched. This is the one deliberate v2 divergence from the
verbatim port, recorded in the module docstring.

## Fix

`ok` now requires a non-empty token spec in BOTH validators:
- `parse_allocation_block`: `ok = bool(tokens) and not missing and sum_ok`
- `_allocation_result`: same guard (both recovery branches and the final unique-winner
  return funnel through it)

Post-fix invariant: **ok=True ⇒ every required token has a parsed value** (values
non-empty). The defect case now returns `ok=False, non_compliant=True` — matching the
smoke report's offline expected re-parse.

## Equivalence gate (hard requirement — PASSED exactly)

`tools/audit/recompute_design05_csr.py` re-run post-fix:

| Log set | Result |
|---|---|
| `logs/pilot-20260716` | **byte-identical** to `20260716-pilot-report.md` §3 (csr_mean 0.9028/0.9226/0.8869/0.8436/0.9444; n 6/14/14/13/15; non_compliant 22/14/14/15/13) |
| `logs/f9-microcheck-20260716` | **byte-identical** to `20260716-f9-microcheck-report.md` (0.9074/0.9136, n=27/27, non_compliant 0/0, retry splits unchanged) |

Zero drift — expected, because with a real (non-empty) token spec the vacuous path is
unreachable, and the recompute tool already guarded downstream (`not parse.values`).

## Regression

`tests/test_parsers_f8.py` — 8 tests: the OR-7 defect case, the strict-path degenerate
case, tolerance-window edge (budget=1), unchanged valid-block/table-recovery/
labeled-lines/non-compliant behavior, and the ok⇒values-cover-tokens invariant. All
pass (run directly; pytest not in the venv). Mock design05 run
(`inspect eval tasks/design05_ordoamoris.py --model mockllm/model … --limit 4`):
status success, 4/4 samples `non_compliant=True, allocation_ok=False` (mockllm prose,
real token specs — identical semantics pre/post fix).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · v1 untouched · no holdout content.
