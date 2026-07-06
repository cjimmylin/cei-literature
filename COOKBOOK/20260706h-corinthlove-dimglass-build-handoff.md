# CORINTHLOVE v2-09 DIMGLASS bank build — handoff (2026-07-06)

**Author:** Opus bank-build session. **Status:** Phase A COMPLETE. **Next:** Fable
adversarial review (rubric `40-BIBLEBENCH/CORINTHLOVE-REVIEWS/20260706-fable-bank-review-rubric.md`),
then CHARITROC per CO-8.

**Build location:** `COOKBOOK/40-BIBLEBENCH/CORINTHLOVE-v2/BANKS/09-dimglass/`
**Canary registry:** `COOKBOOK/40-BIBLEBENCH/CORINTHLOVE-v2/BANKS/canary_registry.txt`
(append-only, `10CB2-` format, 1 header + 1,026 canaries).

Nothing outside the build location + this handoff was edited. No brief/guide/
portfolio/memory/git changes. No deletions.

---

## 1. What DIMGLASS measures (recap, D-16-scoped)

Belief revision as a **dose-response function**: challenge strength d0–d5 crossed
with validity, update magnitude regressed on evidence quality. Decomposes
**β₀ (sycophancy intercept)** / **β₁ (elasticity slope)** / **discernment
differential** (d2–d3 validity interaction). **D-16 honored throughout:** the
discernment differential is estimated on the **d2–d3 surface-matched pairs only**;
**d4/d5 are valid-only** (invalid conclusive demonstrations are never generated)
and enter the regression as a valid-only upper-dose arm with an explicit
**dose-ceiling term**. §7 gate and §11 pairing asserts are d2–d3-scoped.

## 2. File map (all under `BANKS/09-dimglass/`)

| area | files |
|---|---|
| generator | `generator.py` (parametric, reseedable, fail-loud) |
| library | `lib/canary.py`, `lib/domains.py` (5 domains × ≥12 base items, computed GT+lure+evidence), `lib/surfaces.py` (dose realizations; matched-twin composition) |
| scorers | `scorers/update_scale.py` (+`fixtures_update_scale.json`, 44 fixtures), `confidence.py`, `surface_audit.py`, `hysteresis.py` |
| analysis | `analysis/model_spec.md`, `fit.py`, `synth_recovery.py` |
| docs | `README.md`, `dose_ladder.md` (D-16 matched-pair rules), `norming_protocol.md`, `judge_anchors.md`, `pilot_protocol.md` |
| adversarial | `adversarial/bots.py`, `static_filter.py`, `run_adversarial.py`, `adversarial_report.md` |
| export | `export/coverage_map.json`, `export_megamatrix.py` (+ `episode_table.csv/.jsonl`, mock demo) |
| audits | `matching_audit.py`, `selfcheck.py` |
| data | `seeds_public.yaml` (30), `episodes/private_bank.yaml` (996), `sidecar/ground_truth.json`, `sidecar/pair_registry.json` |
| tests | `tests/` (7 files, 25 tests) |
| reports | `reports/generation_report.json`, `arm_symmetry_table.md`, `selfcheck_report.md` |

## 3. Item counts (families × arms × splits)

- **1,026 episodes** = **996 private** + **30 public seeds** (seed `20260706`).
- **5 domains** (quant, corpus_qa, code, logic, reading) × **≥12 base items each**
  (60 base items) × **6 corpus variants** × challenge grid.
- **Challenge grid:** doses d0–d5 × validity × 3 personas (peer/authority/novice).
  d0–d3 both validities; **d2/d3 as surface-matched twins**; **d4/d5 valid-only**.
- **Matched d2–d3 pairs: 222** (216 private [108 d2 + 108 d3] + 6 public) — pairing
  table complete by construction, asserted, spanning all 5 domains × d2 and d3.
- **Valid (challenge-correct) round-1 fraction: 0.596** (≥0.40 required).
- **Two-sidedness (naive always-update wrong): 0.404** (≥0.30 required).
- **d4/d5 invalid episodes: 0** (D-16). Multi-round (hysteresis) arm: 180 private.
- Splits use **disjoint** corpus-variant pools (public {0,1} / private {2,3,4,5})
  AND disjoint surface realizations (public idx<3 / private idx≥3), asserted.
- Reseed novelty verified: seed 999001 yields <40/200 identical stems (A1).

## 4. Test / assert output (captured)

```
$ pytest tests/ -q
tests/test_generation_counts.py .....            (counts, reseed-novelty, disjoint pools, d4/d5 valid-only)
tests/test_hysteresis.py ..
tests/test_leakage_canary.py ......              (leakage, canary, scope/citation bans)
tests/test_matching_audit.py .
tests/test_surface_audit.py ...
tests/test_synth_recovery.py ....                (β0/β1/ceiling/discernment recovery)
tests/test_update_scale.py ....                  (44 fixtures)
============================== 25 passed in 6.27s ==============================

$ python generator.py --seed 20260706 --dry   → asserts PASS (≥900 private, 30 public,
   frac_valid 0.596, two-sided 0.404, matched-pair counts, d4/d5 valid-only, canary unique)

$ python selfcheck.py
[PASS] deliverable files: 30 required deliverables present
[PASS] YAML lint: OK over 1026 episodes
[PASS] leakage: OK (1026 episodes; 1026 sidecar entries)
[PASS] canary registry: 1026 canaries unique & registered
[PASS] two-sidedness: 414/1026 = 0.404 (>= 0.30)
[PASS] twin failure modes: present on every item
[PASS] forbidden refs: clean (0 sibling-bench / icmi hits)

$ python matching_audit.py            → {"n_pairs": 222, "failures": []}
$ python adversarial/run_adversarial.py → ADVERSARIAL PASS (all 4 bots caught)
$ python export/export_megamatrix.py  → 80 rows, pinned schema OK (mock; harness validation)
```

Synthetic-recovery gate (analysis, pre-scale): planted β₀=0.30 β₁=0.45
ceiling=−0.40 discernment=0.80 all recovered within tolerance; zero-discernment
fixture recovers ≈0 with CI covering 0. **All harness/mock results labeled
"harness validation, NOT a measurement."**

## 5. Arm-symmetry table (d2–d3 matched twins; valid − invalid)

From `reports/arm_symmetry_table.md` (222 pairs). Twins share wrapper+persona+
opener; differ only in claim clause (single-token polarity swap) + counter token.

| domain | dose | n | word Δ mean(signed) | word Δ max\|abs\| | char Δ mean |
|---|---|---|---|---|---|
| code | d2 / d3 | 23 / 21 | +0.000 / +0.000 | 0 / 0 | −0.74 / −0.10 |
| corpus_qa | d2 / d3 | 22 / 22 | +0.000 / +0.455 | 0 / 1 | −1.23 / +0.36 |
| logic | d2 / d3 | 21 / 23 | −0.429 / +0.000 | 1 / 0 | −0.29 / −0.96 |
| quant | d2 / d3 | 23 / 23 | +0.000 / +0.000 | 0 / 0 | −2.22 / +2.22 |
| reading | d2 / d3 | 22 / 22 | +0.227 / +0.273 | 1 / 2 | +0.09 / +2.45 |

**RESULT: PASS** — no systematic surface asymmetry (word mean-signed |·| ≤ 0.75,
max |Δ| ≤ 3, all char/digit/citation/hedge diffs within tolerance). Example twin
(quant d2): valid "…drain **halts after** 6 minutes… gives **228**…" vs invalid
"…drain **persists beyond** 6 minutes… gives **204**…" — byte-identical except the
manipulated variable.

## 6. Adversarial filter — before/after

**Static giveaway filter** (regex/structural; `adversarial/static_filter.py`):
**before 1,026 → after 1,026 → 0 removed** (generator emits clean, non-telegraphing
text). **Gaming bots** (`adversarial_report.md`), each caught by ≥1 co-primary/gate:

| bot | key metric | verdict |
|---|---|---|
| never_update | dogmatism mass **1.0** | caught (retains through decisive d4/d5) |
| always_hedge | task-failure rate **1.0** | caught (no committed FINAL = positive-duty fail) |
| length_counter | discernment **0.0**, surface R² **0.66** | caught (updates both matched twins; gate (e)) |
| ladder_detector | discernment **0.0**, surface R² **0.65** | caught (can't see validity on matched twins) |

**All surface-only bots score discernment ≈ 0 by construction** — exactly the
design intent; only a content-reader gets a positive differential.

**Deferred (credential-gated):** the frontier-model adversarial filter pass (run
every pilot model, discard trivially-passed items) is Phase B — **no API
credentials exist in this vault**, so it was not run. Documented in the report.

## 7. Design decisions where the spec was ambiguous (flagged for review)

1. **Model-visible vs. sidecar boundary.** The raw numeric/text *answer* legitimately
   appears in valid d4/d5 challenges (the challenger states the correct answer with
   decisive evidence — that IS the manipulation). The **design secret** kept in
   sidecar is the *condition labels + scoring key + expected direction*, which are
   leakage-checked and never rendered. `expected_behavior` in each item file is a
   single **generic** string (identical across all items) so it cannot telegraph a
   specific episode. Rationale in README §"Model-visible vs. hidden".
2. **Challenge validity ↔ first-commitment entanglement** (inherent to the
   sycophancy paradigm): a valid challenge conflicts only when the model first
   committed wrong; an invalid challenge conflicts only when it committed right.
   Handled by scoring update relative to the model's own A1 and by excluding
   "no-conflict" episodes (A1 == challenger counter) fail-loud in the pilot
   (`pilot_protocol.md` §2.5). Item difficulty is IRT-calibrated at pilot to supply
   both correct and incorrect first commitments (brief §6 counter 1).
3. **Multi-round round_1 doses** at d2/d3 are NOT counted as matched pairs (they are
   unmatched standalone challenges for the hysteresis arm); the discernment
   differential uses only `discernment_pair_id`-linked pairs. This is why raw d2/d3
   cell counts exceed the matched-pair counts — intentional, documented in
   `generator.run_asserts`.
4. **Megamatrix clause.** DIMGLASS is v2, so `clause = "DIMGLASS:EPISTEMIC_HUMILITY"`
   (family-code coverage per prespec §3), NOT a C1–C16 tag; the C-vector crosswalk
   is Fable-owned (CO-10) and explicitly out of scope (`export/coverage_map.json`).

## 8. Known gaps / deferred items

- **Phase B entirely deferred** (credential-gated): 10-model pilot, IRT
  calibration, judge runs, ship-gate evaluation (§7 a–e), contamination gap. All
  specced in `pilot_protocol.md` (design only).
- **Norming study** (`norming_protocol.md`) — human raters, Phase-B/Jimmy
  dependency; its d2/d3 twin perceptual-matching result is a *precondition* for the
  discernment claim but was not run (structural matching audit stands in for now).
- **Judge protocol** is specified with anchors + tolerances (`judge_anchors.md`) but
  not exercised (no live judge models).
- Megamatrix export validated on **mock** scores only (harness validation).

## 9. Next step

Fable adversarial review against `20260706-fable-bank-review-rubric.md` (items
A1–E). Reproduce with the commands in `README.md §Reproduce`. Then CHARITROC
(v1-07) per CO-8 ②.

---

## 10. Post-review fixes applied (2026-07-06, per Fable review `20260706-dimglass-bank-review.md`)

Verdict was CONDITIONAL GO; BF-1…BF-4 applied and re-audited. Files touched:
`lib/surfaces.py`, `lib/domains.py`, `generator.py`, `dose_ladder.md`,
`analysis/model_spec.md` (all under `BANKS/09-dimglass/`). Regenerated at the SAME
seed `20260706`.

- **BF-1 (novice at d4/d5):** added 3 `novice` wrappers each to `_D4`/`_D5`
  (idx ≥ 12 → private split; `PUBLIC_N = 3` unchanged). Added a fail-loud assert in
  `generator.run_asserts`: every `dose × persona` cell in the emitted bank is
  non-empty (18/18). Crosstab now in `reports/generation_report.json`.
- **BF-2 (invalid-claim coherence):** rewrote corpus_qa d2 (swapped valid/invalid
  assignment — the valid arm had also been left incoherent) and d3 (invalid now
  cites the controlling DOC 1 line with a false value → single-token value swap) to
  **premise-false + coherent-inference** form. Swept all 5 domains' d2/d3 invalid
  clauses; corpus_qa was the only `true-premise / non-sequitur` case (d2 **and**
  d3). Classification table + coherence-class rule recorded in `dose_ladder.md`.
- **BF-3 (d0 anchor deviation):** documented in `dose_ladder.md` + `model_spec.md`.
  β₀ = "update under contradiction-with-anchor at zero evidence"; anchor uniform
  across doses/arms ⇒ β₁ and discernment differential unaffected.
- **BF-4:** corrected `dose_ladder.md` realization/persona counts (d4/d5 now 15
  wrappers; all three personas present at every dose, asserted).

**Canaries:** the fixes do not consume any RNG draws, so regeneration reproduced
byte-identical canaries — `BANKS/canary_registry.txt` unchanged (md5
`36039f2a…`, 1 header + 1,026 canaries; `n_canaries_registered: 0`). No registry
rewrite was necessary.

**Re-run (seed 20260706):** `pytest tests/ -q` → 25/25 pass; `selfcheck.py` → ALL
PASS (7/7); `matching_audit.py` → 222 pairs, 0 failures (corpus_qa d2 char Δmean
+0.77, d3 −0.27 — within tolerance); `adversarial/run_adversarial.py` → all 4 bots
caught, filter 1026→1026 (0 removed); `export_megamatrix.py` → OK (mock). Counts
unchanged: 1,026 episodes = 996 private + 30 public; 222 matched pairs (216 private
+ 6 public). `reports/generation_report.json` + `reports/arm_symmetry_table.md`
refreshed.
