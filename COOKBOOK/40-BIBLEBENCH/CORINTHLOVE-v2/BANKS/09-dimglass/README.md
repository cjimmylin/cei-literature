# DIMGLASS (v2-09) question bank

**Epistemic Elasticity — Dose-Response Measurement of Belief Updating Under
Correction.** 1 Corinthians 13:9–12 ("we know in part… through a glass, darkly").

Measures **calibrated teachability** as a dose-response function, decomposing
sycophancy (β₀ intercept) from teachability (β₁ slope) from discernment (the
d2–d3 validity interaction). Gate-revised per **D-16** (discernment scoped to
d2–d3; d4/d5 valid-only upper-dose arm + dose-ceiling term).

## Counting unit (CO-5)

DIMGLASS counts **episodes** (standard `multiturn_script.stage_1..4`; no
design-native structure substitution). Bank size: **1,026 episodes** = 996
private + 30 public seeds (seed `20260706`; regenerate for novel items).

## Layout

```
09-dimglass/
├── README.md                 ← this file
├── generator.py              ← parametric generator (fail-loud asserts) + writer
├── dose_ladder.md            ← d0–d5 defs, D-16 matched-pair rules, matching-audit spec
├── norming_protocol.md       ← evidence-strength norming study (design only)
├── judge_anchors.md          ← revision-degree rubric (0–3), pious/stonewall/status flags
├── pilot_protocol.md         ← 10-model pilot, IRT calibration, §7 gates (Phase B design)
├── matching_audit.py         ← arm-symmetry audit → reports/arm_symmetry_table.md
├── lib/
│   ├── canary.py             ← deterministic 10CB2-09-<uuid4> canaries
│   ├── domains.py            ← 5 domains × ≥12 base items, computed GT + lure + evidence
│   └── surfaces.py           ← dose surface realizations; matched d2/d3 twin composition
├── scorers/
│   ├── update_scale.py       ← graded update classifier (mechanical + hedge/flag)
│   ├── confidence.py         ← confidence channel (Brier, calibration gap)
│   ├── surface_audit.py      ← surface-feature regression audit (gate (e))
│   ├── hysteresis.py         ← multi-round path-dependence statistic
│   └── fixtures_update_scale.json ← 44 labeled fixtures (recovered pre-scale)
├── analysis/
│   ├── model_spec.md         ← mixed-effects spec, contrasts, ceiling, fallback
│   ├── fit.py                ← β₀/β₁/ceiling + discernment (paired bootstrap)
│   └── synth_recovery.py     ← planted-parameter synthetic data
├── adversarial/
│   ├── bots.py               ← never-update / always-hedge / length-counter / ladder-detector
│   ├── static_filter.py      ← giveaway regex/structural pass
│   ├── run_adversarial.py    ← end-to-end run → adversarial_report.md
│   └── adversarial_report.md ← verdicts + before/after filter counts
├── export/
│   ├── coverage_map.json     ← declared coverage (prespec §3), fixed before pilot
│   └── export_megamatrix.py  ← episode-level table (pinned schema) + mock demo
├── tests/                    ← pytest suite (run BEFORE scale)
├── seeds_public.yaml         ← 30 public seeds (public pools)
├── episodes/private_bank.yaml← 996 private episodes (private pools, disjoint)
├── sidecar/
│   ├── ground_truth.json     ← hidden scoring key + condition labels (keyed by id)
│   └── pair_registry.json    ← d2/d3 matched-pair links (discernment_pair_id)
└── reports/                  ← generation_report.json, arm_symmetry_table.md, selfcheck_report.md
```

Portfolio canary registry: `../canary_registry.txt` (append-only, `10CB2-` format).

## Model-visible vs. hidden

- **Model sees ONLY** the rendered `multiturn_script` (stage_1..4). The challenge
  references the model's stage-1 answer via the literal placeholder `<A1>`, which
  the **live harness substitutes** at run time with the model's actual `FINAL:`.
- **Hidden (sidecar, never rendered):** the scoring key, ground-truth/lure tokens
  for scoring, dose/validity condition labels, expected update direction,
  servility/dogmatism cell flags, and the canary. `expected_behavior` in the item
  file is a single **generic** string identical across all items (no per-item
  telegraphing). Leakage is asserted in `tests/test_leakage_canary.py`.
- **Note on evidence tokens:** at d4/d5 a *valid* challenger legitimately states
  the correct answer with decisive evidence — that is the manipulation, not a
  leak. The design-secret is the *condition labels + scoring key*, which stay in
  sidecar; the arithmetic answer is task content.

## Reproduce

```bash
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
$PY generator.py --seed 20260706          # writes episodes + sidecar + canary registry
$PY -m pytest tests/ -q                    # 25 tests: scorers, generation, leakage, matching
$PY matching_audit.py                      # arm-symmetry audit
$PY adversarial/run_adversarial.py         # gaming bots + static filter
$PY export/export_megamatrix.py            # megamatrix export (mock demo)
$PY selfcheck.py                           # consolidated ship self-check
```

## Status

Phase A (authoring artifacts) COMPLETE. Phase B (pilot + human annotation) is a
protocol document only — **no live model calls exist in this vault** (no
credentials). Every harness result here is **"harness validation, NOT a
measurement."** Next: Fable adversarial review (rubric
`../../CORINTHLOVE-REVIEWS/20260706-fable-bank-review-rubric.md`), then CHARITROC
per CO-8.
