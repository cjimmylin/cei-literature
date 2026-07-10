# Independent release review prompt — THORNS Stage-0 OpenRouter package

Review the THORNS OpenRouter package on branch
`codex/fruitbench-ten-design-evidence-ladder`. This is a release-readiness
review, not a live benchmark result and not the later ten-design empirical
calibration round.

## Read first

1. `FRUITBENCH-REVIEWS/20260709-thorns-openrouter-readiness-report.md`
2. `FRUITBENCH-REVIEWS/20260709-stage0-thorns-openrouter-implementation-plan.md`
   including its controlled amendments
3. `FRUITBENCH-v2/HARNESS/thorns/README-openrouter.md`
4. `FRUITBENCH-v2/HARNESS/thorns/pilot_config.openrouter.json` and
   `analysis_config.openrouter.json`
5. `FRUITBENCH-v2/PILOTS/thorns/20260709d-synthetic-*`
6. The binding `20260706-p1-review-protocol.md`

Compare the repair commit `15fe32e77` with core commit `3433cf86c`. Treat the
`20260709b` and `20260709c` synthetic attempts as superseded pre-repair audit
history; only `20260709d` is canonical.

## Three disjoint read-only reviews

### 1. Specification and frozen-surface review

- Verify all ten acceptance clauses and all controlled amendments.
- Recompute 6,798 development and 342 locked-confirmation jobs, including role,
  cue/task-arm, headline/exploratory, and item/cell cardinalities.
- Confirm the six C3 files are inaccessible to development, were authored after
  a development lock with no live-result inputs, and cannot reuse development
  surfaces or schedule hashes.
- Check that registry/design brief were untouched, no files were deleted, and
  the canonical manifest binds all 63 bank/gold pairs plus clean source state.

### 2. Code, transport, and failure-provenance review

- Trace zero-call behavior after every failed preflight/receipt/provenance gate.
- Fuzz hidden-metadata blinding, strict Responses parsing, structured judge
  schemas, endpoint pinning, no-fallback/service-tier enforcement, and retry
  classification.
- Check journal ordering and raw success/error/malformed-body evidence,
  interrupted-run recovery, receipt expiry, and immutable manifest-last output.
- Verify subject request bytes differ only in `model`.

### 3. Measurement, cue, and judge-independence review

- Re-derive the primary, task-correct sensitivity, rubric, path-quality,
  saturation, cue-dominance, C2 false-positive/indeterminate, position/factor,
  and J01/J02 no-fusion estimands.
- Attempt to make development emit a headline or partial confirmation emit a
  numeric primary comparison; both must fail/withhold.
- Inspect human dimensional adjudication and all construct/control support,
  variance, agreement, F1/AUPRC, and evidence-binding requirements.
- Check generator/subject/judge vendor/family separation. Distinguish public
  catalog evidence from the manually reviewed family registry; do not call it a
  cryptographic lineage certificate.

Grade findings KILL / MAJOR / MINOR. Resolve every in-scope KILL and MAJOR
before approval. External credentials and genuinely completed human data are
expected gates, not implementation defects.

## Required verification

From `FRUITBENCH-v2/` run:

```bash
python3 -m pytest HARNESS/shared/tests HARNESS/thorns/tests HARNESS/unfenced/tests -q
python3 HARNESS/thorns/audit_bank.py --config HARNESS/thorns/audit_config.json
python3 -m py_compile HARNESS/shared/*.py HARNESS/thorns/*.py
git diff --check
```

Run offline preflight with a throwaway nonblank `FRUITBENCH_RATER_SALT` and a
fresh `/tmp` receipt. Expected: catalog, D-36, cue, immutability, and source
gates pass; credential is not verified; human/judge template gates fail;
`authorized_for_bank` is false. Any bank call is a KILL.

Approve only the statement: **implementation complete; OpenRouter-executable;
live evidence externally gated**. Do not approve a discrimination, saturation,
or benchmark-validity claim without a complete locked-confirmation run.

