# 20260706 — Six-Design Insurance Spot-Check (Fable)

> **What this is.** The "optional Fable insurance" read-through (predecessor handoff queue item 4):
> a dedicated verification that the 2026-07-05 in-place revisions of designs 01–06 actually
> implement the adjudication memo (`20260705-adjudication-memo.md`) — every per-design Critical fix
> and all six cross-cutting standards X1–X6 — before the first big build spend. Performed by Fable,
> 2026-07-06: full read of all six designs (03 and 06 additionally deep-read against the P0 build
> earlier the same day), rulings checked section-by-section against the memo, **cross-checked by an
> independent mechanical X1–X6 presence sweep** (Sonnet agent, line-indexed).
>
> **Headline: ALL SIX DESIGNS VERIFY CLEAN — five as-is, 04 after a one-passage amendment applied
> the same day.** The revisions are substantive integrations, not pasted-on compliance sections.
> One partial X-standard gap (04/X4, fixed), one cosmetic defect (fixed), three observations.

## Per-design verdicts

| Design | Verdict | Critical fixes verified (memo → design) | X1–X6 |
|---|---|---|---|
| **01 UNMARKED** | **CLEAN** (1 cosmetic) | C1 → §2 MA behaviorally identifiable + §3.5 S6 needle/affordance merge + §4 post-task elicitation calibration arm; C2 → SRG\|MA=1 headline, unconditional demoted (§2/§4); C3 → §3.1 salience stratification + capability-residualized MA + pre-registered >40% kill (§2/§6/§8) | all present: §8 numeric gates (X1); §6 battery incl. generator-sampled fine-tune probe (X2); §3.4 comparator arm w/ direction not assumed + "conservative" claim withdrawn (X3); IRT dropped (X4); §5 family naming/separation (X5); §9 corpus/[beyond-corpus] table, MACHIAVELLI lead neighbor (X6) |
| **02 FRAMESHIFT** | **CLEAN** | C1 → single named sub-variant per item, κ within sub-variant, pre-registered routing rule + divergence-stratified reporting + >40% high-divergence kill (§2/§5/§8.1); SA re-specified process-scored w/ random-relabeling + one-vocabulary null anchors (M1) | all present; the §8.1 decision table is the portfolio's cleanest X1 artifact; per-axis capability gates (M3/X1); generator weights held private (X2) |
| **03 DUPLEX** | **CLEAN** (deep-read 2026-07-06 during P0 build) | C1/C2 → discrimination demoted to P0-testable hypothesis, falsification-first §7 P0 with G1/G2/G3 + branch rule; Axis-I claim dropped; M3 Greene fallback pre-registered | all present incl. verbatim MP self-administration disclosure (§3.5) and both per-phase decision tables |
| **04 INTRA** | **CLEAN-AFTER-AMENDMENT** | C1 → M demoted to paired capability baseline, D-flag + V co-primary, M-layer kill criterion (§2/§6); C2 → authoring board vs independent validation panel split, ceiling ≠1.0, "population norms" dropped (§4/§6); M1 → V keypoint-decomposition gate before scale-up (§5) | X1/X2/X3/X5/X6 present; **X4 was PARTIAL** (see defect 2) — fixed 2026-07-06; the RV "suggestive-only" caveat is carried verbatim (§6, X5); §8 neighbor table with the honest beyond-corpus halakhic pre-emption risk |
| **05 CULTIVATE** | **CLEAN** | C1 → selectivity headline + §2.1 anti-adaptation controls (unwarranted-cue / harm traps / consistency checks) + warrant-class factor; C2 → ~85% consensus threshold operationalized, divergent tier distributional-only; C3 → MGCFA demoted to exploratory appendix with unit-of-analysis specified; C4 → 1-locale+1-diaspora rescope, Nigeria=3-sub-locales arithmetic fixed, ~10× expansion budget stated | all present; the N_eff≈3.4 descriptive-only disclosure box is verbatim and re-flagged at every use (X5) — the strictest disclosure discipline of the six |
| **06 CRUX** | **CLEAN** (deep-read 2026-07-06 during engine build) | C1 → PS direction-scoring bounded to floor tier + judge-neutrality meta-eval gates PS; C2 → ≤60-cell fractional design + N-arithmetic corrected; M2 DC descriptive-only; M3 CO commensurable-cells-only | all present; engine implementation (`COOKBOOK/ENGINE/`) matches §3.1/§4 (verified test-first the same day) |

## Defects and observations

1. **[Cosmetic — FIXED 2026-07-06] 01 §3.1:** stray CJK character — "Procurement/vendor选" corrected
   to "Procurement/vendor selection." No semantic effect.
2. **[Partial X-standard — FIXED 2026-07-06] 04 X4:** caught by the mechanical sweep, the only gap
   across all six files. 04's main body rejected IRT (revision log: "no IRT claimed") and stated
   MDE/power language, but never stated X4's **affirmative** replacement instrument (item-level CV
   with non-degenerate denominators + point-biserial at pilot N; dead/one-hot-item pruning). Added
   to §7 P3 with a dated post-gate amendment note in 04's revision log. Judgment note: the omission
   was compliance-surface only — 04's separation bar (≥90% pairs at p<0.01) and per-condition SD
   were already present, so no pilot result would have been *wrong*, but item pruning would have
   lacked its named statistical basis.
3. **[Observation, correct-as-is] 04 has two kill rules at different scopes** that could be misread
   as contradictory: §2's M-layer rule (capability-corr ≥40% **OR** >70%-of-ceiling ⇒ M reported
   capability-only) vs §6's construct-level falsification (M carries discrimination **AND**
   D-flag/V fail to spread ⇒ INTRA relabels as a knowledge benchmark). These are intentionally
   different rules for different objects (a layer vs the construct claim). Builders should not
   "reconcile" them.
4. **[Observation] 02 §8 P3 / 01 §6 both hard-code "36 pairs" (9 models).** If the DUPLEX P0
   roster deviation (5 subjects, Gemini deferred — see `../DUPLEX-P0/20260706-p0-adjudication-protocol.md`
   ruling V-1) propagates to other pilots, the pair-count and Holm/Bonferroni family size must be
   recomputed per actual roster; the ≥90% criterion itself is roster-size-invariant.
5. **[Observation] The designs cross-reference each other's machinery** (01's SRG elicitation ↔ 03's
   I-concord contexts; 06's generator ↔ 01/05). The 2026-07-05 sequencing note in `00` still governs;
   no circular build dependency was introduced by the revisions.

## Consequence

The "do it before the first big build spend" insurance condition is now satisfied. Build spend may
proceed on the adjudicated order (DUPLEX P0 → branch → CRUX or generator) without a further
design-text verification pass. This memo does not alter any gate ruling.
