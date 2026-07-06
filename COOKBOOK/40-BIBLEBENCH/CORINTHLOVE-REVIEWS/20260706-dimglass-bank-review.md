# Adversarial bank review — DIMGLASS (v2-09), first CO-8 build

**Reviewer:** Fable, 2026-07-06, per `20260706-fable-bank-review-rubric.md`. First bank in the CO-8 order — findings here bind the pattern for all subsequent builds.
**Input:** `CORINTHLOVE-v2/BANKS/09-dimglass/` at build state (uncommitted), handoff `COOKBOOK/20260706h-corinthlove-dimglass-build-handoff.md`.
**Stance:** attempted refutation. All builder-reported checks were re-executed independently by the reviewer, not trusted from the handoff.

## 1. Verdict

**CONDITIONAL GO.** The bank's spine is sound and its self-reporting is honest. Two binding fixes (BF-1, BF-2) must be applied and re-audited before this bank is used as the template for CHARITROC or enters any pilot; two documentation fixes (BF-3, BF-4) ride along. No finding kills the design or requires Fable re-adjudication.

## 2. Independently reproduced evidence (rubric A–D)

Reviewer re-ran on 2026-07-06: `pytest tests/ -q` → **25/25 pass**; `selfcheck.py` → 7/7 PASS (files, YAML lint over 1,026 episodes, leakage 1,026/1,026 sidecar, canary uniqueness vs registry, two-sidedness 0.404 ≥ 0.30, twin failure modes, forbidden-refs 0 hits); `matching_audit.py` → 222 pairs, 0 failures; `run_adversarial.py` → all 4 bots caught, static filter 1,026→1,026 (0 removed).

- **A1/A2 generation integrity:** parametric generator, 25 fail-loud asserts, reseed-novelty test passes; axis coverage verified by reviewer crosstab over all 996 private episodes — **except the persona hole in F1 below**.
- **B1 telegraphing:** reviewer sampled rendered twins across all 5 domains — no vice-naming, no eval framing, no ladder display; the static filter's 0-removed is credible because text is composed from clean template pools (and the filter's scan covers the full model-visible surface: corpus documents are embedded in `stage_1`, which is scanned). Frontier-model filter pass correctly deferred (no credentials) and labeled.
- **B2/B3:** sidecar boundary well-drawn and documented (README §Model-visible: model sees ONLY `multiturn_script`; scoring key/labels/GT-lure tokens sidecar-only); the raw-answer-in-valid-d4/d5 judgment call is CORRECT (the stated answer is the manipulation; the secret is the condition label). Canaries `10CB2-09-` registered (1,026 unique), never in visible text.
- **B4:** public/private disjoint at both corpus-variant and surface-realization level, asserted and tested.
- **C1/C2 design fidelity:** graded 0–3 update scale matches §5; β₀/β₁/discernment extraction with synthetic-recovery gates (planted-parameter recovery verified, incl. zero-discernment null). **D-16 verified at the data level:** 0 invalid d4/d5 episodes in the bank; discernment scoped to 222 d2–d3 registered pairs; dose-ceiling term present in `model_spec.md`/`fit.py`.
- **C3 arm symmetry:** matching audit reproduced; twins share wrapper+persona+opener and differ in single-clause polarity + counter token (byte-level check on samples). *Plausibility* symmetry is a different matter — see F2.
- **D1–D4:** every mock result labeled "harness validation, NOT a measurement" (verified in reports); megamatrix export schema matches prespec §3 exactly; `coverage_map.json` declares family-code coverage (`DIMGLASS:EPISTEMIC_HUMILITY`) — the right call for a v2 bank (prespec §1: crosswalk-mapped only, never pooled with native C-vector methods; crosswalk is Fable-owned). Scope/citation greps clean.

The builder's four flagged judgment calls (handoff §7) are all **accepted** as decided.

## 3. Findings

**F1 — BINDING (BF-1): no `novice` persona exists at d4/d5.** Reviewer crosstab over all 996 episodes: novice = 0 at both d4 (156 challenges) and d5 (126), populated everywhere else. Root cause: `lib/surfaces.py` `_D4`/`_D5` wrapper pools contain only peer/authority entries. Consequences: (a) the brief §4's *novice-correct* cell — "hesitant novice who happens to be right," the status-vs-evidence test — is impossible at exactly the doses where evidence is decisive, and the brief's own worked seed (§10, round-2 d4 hesitant novice) cannot be generated; (b) `pilot_protocol.md`'s status-tracking sub-study is unexecutable where it matters; (c) persona is structurally confounded with dose in the regression; (d) `dose_ladder.md` claims all three personas per dose — internal inconsistency.
**Fix:** add ≥3 novice wrappers each to `_D4`/`_D5`, add a fail-loud generator assert that every dose × persona cell is non-empty, regenerate, re-run all audits/tests, refresh the arm-symmetry table.

**F2 — BINDING (BF-2): one family's invalid d2 claims are logic-defeatable, breaking plausibility matching.** In quant/code/logic/reading, invalid d2/d3 claims are *false-premise + coherent-inference* (defeating them requires checking content — the construct). The corpus_qa "retention" family's invalid claim is *true-premise + non-sequitur* ("the earlier draft was formally rejected and never controls here, so 11 [the draft's number] beats X") — defeated by inference-checking alone, no content contact needed. For affected pairs the discernment differential partially measures logic-checking, not evidence discernment.
**Fix:** rewrite that family's invalid clause to false-premise/coherent-inference form; sweep ALL families' invalid clauses and classify each (premise-false vs inference-invalid), requiring coherent inference throughout; add the coherence-class rule to `dose_ladder.md`'s matched-pair construction rules; regenerate and re-audit.

**F3 — DOCUMENTATION (BF-3): d0 deviates from the brief undisclosed.** Brief defines d0 as bare disagreement ("I think that's wrong"); every implemented d0 wrapper supplies an explicit alternative answer (`{counter}`). Defensible — the anchor is uniform across all doses, so slope and differential are unaffected, and mechanical flip-scoring needs a target — but β₀ becomes "update under contradiction-with-anchor," not pure social pressure. **Fix:** document the deviation and its β₀ interpretation in `dose_ladder.md` and `analysis/model_spec.md`. No regeneration needed.

**F4 — DOCUMENTATION (BF-4):** `dose_ladder.md`'s persona/realization claims must be corrected to match the post-BF-1 reality.

## 4. Standing conditions (carried, not new)

1. **Norming study is the precondition for any discernment claim** (builder already flagged): structural symmetry ≠ perceived-strength symmetry. Human raters blind to validity must confirm d2/d3 twins are strength-matched before the differential is reported as discernment. Jimmy dependency.
2. Frontier-model adversarial filter pass, IRT difficulty calibration, judge exercise, and §7 ship-gates are all Phase B (credential-gated).
3. Megamatrix export validated on mock rows only.

## 5. Reviewer's negative duty (rubric §E)

The two strongest reasons this bank might not survive external replication, independent of verdict:
1. **The discernment headline rests entirely on plausibility matching that no human has yet confirmed.** If norming shows invalid twins are perceptibly weaker (even post-BF-2), the "near-zero discernment" prediction becomes an artifact and the headline collapses to "models can't logic-check" — a much weaker claim. This is the single biggest threat to the design's podium claim.
2. **Template homogeneity:** 996 episodes derive from 60 base items and fixed wrapper pools, with an identical harness instruction ("Reconsider if warranted… FINAL:") after every challenge. Dose *contrasts* survive this (uniform across arms), but absolute β₀ estimates may not generalize to naturalistic challenge phrasing, and a format-adapted model could shift the whole function. Mitigation exists (per-level contrasts as primary under §7(d)), but reviewers should not quote β₀ as "sycophancy rate" without that caveat.

## 5b. Fix discharge (same day, Fable-verified)

BF-1…BF-4 were applied by an Opus fix session on 2026-07-06 and **independently re-verified by the reviewer**: 25/25 pytest, selfcheck 7/7, matching audit 222/0 failures, adversarial pass all reproduced post-fix; dose × persona crosstab now 18/18 non-empty (d4 novice = 39, d5 novice = 24) with a new fail-loud generator assert; corpus_qa d2 AND d3 invalid clauses rewritten to false-premise/coherent-inference (the fix sweep found the d2 valid arm was also incoherent, and caught a d3 non-sequitur this review had not named — both fixed; classification table in `dose_ladder.md`); d0-anchor deviation documented in `dose_ladder.md` + `model_spec.md`; regeneration at the original seed left episode/pair counts and the canary registry byte-identical. **Verdict upgraded: the CONDITIONAL GO conditions are DISCHARGED — bank is GO for its role as CO-8 template and for the credentialed pilot, subject only to the §4 standing conditions (norming study, Phase B gates).**

## 6. Propagation orders for subsequent CO-8 builds

Binding on CHARITROC and later banks: (P-1) persona/axis coverage assert — every declared design cell must be non-empty in the generated bank, enforced fail-loud, not assumed from template pools; (P-2) where matched pairs exist, classify and match the *defeat class* of invalid arms (premise vs inference), not just surface form; (P-3) any deviation from the brief's dose/condition definitions must be documented in the bank's docs at build time.
