# Synthetic analysis scaffold

**Provenance:** `SYNTHETIC_VALIDATION_ONLY`

This directory validates BibleBench's offline analysis plumbing. Its rows are
invented fixtures, not provider outputs or model evidence. They do not support
performance statements, model comparisons, inferential statistics, aggregate
metrics, or ordering systems.

## Files

- `synthetic-observations.json` is the closed, typed input fixture. Each row
  carries an episode ID, primary logical-call ID, and evidence-bundle hash for
  later exact custody binding.
- `synthetic-summary.json` contains mechanical validity and missingness,
  module-native dimension vectors, stratum counts, red-line incidents,
  action/probe consistency, and exact repeat agreement.
- `table-shells.csv` exposes the same counts and denominators as stable table
  shells and figure data. Every data row declares
  `SYNTHETIC_VALIDATION_ONLY`.

## Regeneration

From `BIBLEBENCH-PILOT/`, run:

```bash
python -c 'from pathlib import Path; from biblebench_pilot.analysis import regenerate_artifacts; p=Path("analysis"); regenerate_artifacts(p/"synthetic-observations.json", p/"synthetic-summary.json", p/"table-shells.csv")'
```

Regeneration is deterministic and makes no network or model calls. The test
suite verifies byte identity against the checked-in JSON and CSV.

## Fail-closed boundaries

Every document and observation must declare `SYNTHETIC_VALIDATION_ONLY`.
Unknown or real provenance, non-synthetic aliases, duplicate observation IDs,
duplicate custody IDs, undeclared fields, aggregate/ordering/inferential
fields, inconsistent missingness, red-line incidents without available
evidence, invalid repeat eligibility, and non-finite values are rejected.

The synthetic validation registry fixes two native dimensions per module:
FruitBench (`bounded_kindness`, `task_fidelity`), CORINTHLOVE
(`authority_restraint`, `truth_care`), 10CBench (`neighbor_protection`,
`truthful_witness`), and SermonMount (`passage_fidelity`, `prudent_action`).
Omitted registered keys are normalized to explicit nulls, so every dimension's
denominator includes every observation from its module.

Cue-controlled outputs are absent from the checked-in summary because offline
regeneration does not receive private custody. For an explicit cue request,
the caller passes the exact schedule, evidence inventory, manifest, and private
evidence root directly to `summarize_document(...)` or
`regenerate_artifacts(...)`. The analysis entry point itself invokes
`custody.verify_cue_custody_manifest(...)`, which reopens every canonical
evidence object, and consumes that recomputed result only within the same
operation. It does not accept a `VerifiedCueCustody`, sealed token, or other
caller-supplied authority.

After recomputation, analysis binds every observation's
actor/module/episode/role/cue/logical-call/evidence identity to the manifest
and records the canonical hash of the exact observation document in the
output. Within each custody-bound actor/module/episode/role identity, cue-set
ID and stratum must remain invariant across C0/C1/C2. A cue-set or stratum
split fails before candidate denominators are formed.

With that verifier-produced binding, an explicit cue request emits paired
native-outcome transition counts plus candidate, eligible, and
missing/ineligible denominators for C0/C1, C0/C2, and C1/C2. The CSV renderer
exports matching coverage, transition, and missingness rows. These are
descriptive synthetic counts only; they do not calculate effects or make
claims. Caller-asserted, malformed, absent, or differently bound custody fails
closed.
