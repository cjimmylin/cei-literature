# Expert 02 — ML Benchmarking Methodology

**Perspective:** ML benchmarking methodology (composite scoring, gate design, measurement validity)
**Scope:** Methods (Section 3) and Results-Landscape (Section 4.1-4.2) of NormEval Paper v2
**Question:** Are ND/PE/CI definitions and gates still correct for v2.2-preliminary? Which passages reference cross-vendor data vs. pure landscape analysis? Is the composite formula self-consistent?

---

## 1. ND/PE/CI Operational Definitions: Status Assessment

The three axis definitions in Section 3.3 are **model-independent and remain valid** for v2.2-preliminary. They characterize static properties of benchmarks (philosophical depth, data availability, citation counts), not model behavior. No revision needed.

**One concern with CI stability.** Citation counts (C1, C2) are snapshot-dependent. The text reports ETHICS at 843 citations (Section 3.3) and repeats this in Section 4.2 (Rank 1 entry). If v2.2 is published months after data collection, these numbers will be stale. Recommend adding a "citation snapshot date" to the methods (e.g., "Semantic Scholar counts retrieved 2026-03-XX") rather than treating them as fixed constants.

**A6 calibration anchors.** The three-point calibration (MoReBench = 5, ETHICS = 3, Hui = 1) is described only in Section 3.2. Since A6 carries 20% of the ND composite, the calibration protocol should note that these anchors were set by a single rater (acknowledged in Section 3.7, limitation 4). This is internally consistent but worth cross-referencing explicitly in Section 3.2 to avoid the impression that calibration anchors obviate the single-rater problem.

## 2. Hard Gates: Correct and Model-Independent

The two gates -- ND >= 40 and public data availability -- are properties of benchmarks, not of model outputs. The 24-pass / 30-fail partition, the Mann-Whitney U test on ND distributions (U = 287, p = 0.605), and the "sociological filter" interpretation are all landscape-level claims. **No cross-vendor contamination.** These sections are clean for v2.2-preliminary.

**Minor inconsistency in gate arithmetic.** Section 3.3 states: "14 failed the ND gate alone, 21 lacked public data alone, and 5 failed both, yielding 24 benchmarks that passed both gates." Check: 14 + 21 + 5 = 40 failures, but 54 - 24 = 30 failures. The numbers do not add up. The "alone" language suggests exclusive categories, but 14 + 21 + 5 = 40, not 30. This is likely a wording error: the intended meaning is probably "14 failed ND (including 5 that also failed data), 21 failed data (including those same 5)," which gives 14 + 21 - 5 = 30. **This must be clarified in v2.2.**

## 3. Composite Formula: Self-Consistency Check

**Section 3.3 states:**
- COMPOSITE = ND x 0.40 + PE x 0.35 + CI x 0.25

**Section 4.1 (ND-PE Tradeoff) states:**
- "60% of ETHICS's rank-1 composite score (77.2) derives from properties orthogonal to philosophical rigor"

Verification: ETHICS has PE = 95.0, CI = 80.0. PE contribution = 95.0 x 0.35 = 33.25. CI contribution = 80.0 x 0.25 = 20.0. Sum = 53.25. As a share of 77.2: 53.25 / 77.2 = 69.0%, not 60%. The text says "60%"; the actual figure is closer to **69%**. This is either a rounding artifact from an earlier version of the weights or a straightforward arithmetic error. **Correct to 69% or explain the discrepancy.**

**Cross-check on ETHICS composite:** ND = 59.8 x 0.40 = 23.92; PE = 95.0 x 0.35 = 33.25; CI = 80.0 x 0.25 = 20.0. Total = 77.17, which rounds to 77.2. The composite score itself is correct.

**Weight sensitivity claim.** Section 3.3 reports "94% stable across 18 weight combinations" for the Top 10 and "no benchmark moved more than 3 rank positions." This claim is model-independent and survives into v2.2. However, the 18 combinations and Table S2 should be verified as actually present in supplementary materials.

## 4. Cross-Vendor vs. Landscape: Section-by-Section Flagging

### Sections that are PURE LANDSCAPE (no cross-vendor data, safe for v2.2):
- **Section 3.1** (Corpus Assembly) -- describes benchmark identification, no model data
- **Section 3.2** (Feature Matrix Design) -- 26 features are benchmark properties
- **Section 3.3** (Composite Scoring and Hard Gates) -- scoring formula and gate logic
- **Section 3.6** (Care Ethics Prototype) -- Opus-only administration, explicitly single-model
- **Section 4.1** (Landscape Analysis) -- all five subsections (Tradition Coverage, Data Availability, Format/Reasoning, ND-PE Tradeoff, Non-Western Engagement) characterize benchmarks, not models
- **Section 4.2** (Top 24 Ranking) -- composite scores derived from benchmark features only

### Sections that REFERENCE cross-vendor data (must be flagged [simulated]):
- **Section 3.4** (Implementation Trial Protocol) -- Phase 1 (T1-T5, Opus only) is clean. Phase 2 (T6-T15) explicitly names 9 models across 3 vendors including "GPT-5 (accessed via Codex agent)" and four Gemini models. **The entire Phase 2 description must carry the [simulated] flag.**
- **Section 3.5** (Statistical Methods) -- Claims 1-4 are landscape-level or Anthropic-only. However, **Claim 2** references "confirmed across vendors" with per-model Cohen's h values (Haiku h=0.42, GPT-5 h=0.71). The cross-vendor confirmation must be flagged. **Cross-vendor agreement analysis** (Cohen's kappa, 114 items, 9 models) is entirely cross-vendor. **IH/IB scaling** references "all 9 models." Both subsections need [simulated] flags.
- **Section 3.7** (Limitations) -- Limitation 3 ("Codex wrapper confound") explicitly discusses the GPT-5 access method. This is meta-commentary about cross-vendor methodology and should be **retained but annotated** to clarify the simulated status.

### Borderline passage in Section 4.1:
- The sentence "The field has built benchmarks where it is easiest to build benchmarks" is attributed to "the cross-cultural moral psychology perspective on the council." This is an interpretive claim about the landscape, not a data claim. **No flag needed**, but the council attribution should be reviewed for consistency with v2.2's own council structure.

## 5. Summary of Required Actions for v2.2-Preliminary

| Priority | Issue | Location | Action |
|----------|-------|----------|--------|
| HIGH | Gate arithmetic error (14+21+5=40, not 30) | Section 3.3 | Reword to clarify overlapping failures |
| HIGH | "60%" should be ~69% | Section 4.1, ND-PE Tradeoff | Correct arithmetic or explain |
| HIGH | Phase 2 cross-vendor protocol | Section 3.4 | Add [simulated] flag to entire Phase 2 block |
| HIGH | Claim 2 cross-vendor confirmation | Section 3.5 | Flag per-model h values as [simulated] |
| HIGH | Cross-vendor agreement analysis | Section 3.5 | Flag entire subsection as [simulated] |
| MEDIUM | IH/IB "all 9 models" | Section 3.5 | Flag as [simulated] |
| MEDIUM | Citation snapshot date missing | Section 3.2/3.3 | Add retrieval date |
| LOW | A6 single-rater cross-reference | Section 3.2 | Add forward pointer to Section 3.7 limitation 4 |
| LOW | Table S2 existence verification | Section 3.3 | Confirm supplementary table is present |

**Bottom line.** The ND/PE/CI framework and composite formula are structurally sound and model-independent. The landscape analysis (Sections 3.1-3.3, 4.1-4.2) requires no cross-vendor flags. The implementation trial protocol (Section 3.4 Phase 2) and statistical methods (Section 3.5 Claims 2, cross-vendor agreement, IH/IB) are the primary contamination zones requiring [simulated] annotations. Two arithmetic errors (gate counts, PE+CI share) need correction regardless of the cross-vendor issue.
