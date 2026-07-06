# Pre-registered analysis specification — CORINTHLOVE triangulation megamatrix (CO-6a/CO-6b)

**Author:** Fable, 2026-07-06 (written ahead of data, inside the Fable window, so later sessions execute rather than design)
**Status:** PRE-REGISTERED. Deviations require a Fable-tier adjudication session and must be logged as amendments to this file's §8 (append-only); the body above §8 is frozen once the first pilot datum exists.
**Governs:** the two-level validity analysis that replaced the trait×method CT-CM megamatrix (v3 portfolio §9, CO-6a) and the hierarchical fallback (CO-6b); plus the CO-8 interim 2-method concordance gate.

---

## 1. Triggers and preconditions

- **Interim gate (CO-8 ⑤):** runs when the third and fourth banks in the CO-8 order (CROSSROADS + AGAPEGAME-or-WITNESS) both have pilot data on the shared panel (§2). MANYMIRRORS build is gated on §4's interim criterion.
- **Full analysis (CO-6a):** runs when ≥3 v3-method banks have pilot data on the shared panel. v1/v2 banks (DIMGLASS, CHARITROC) contribute to L1 only via the CO-10 crosswalk (v1 portfolio §9), reported separately as "crosswalk-mapped," never pooled with native C-vector methods in the primary statistic.

## 2. Shared model panel (pinned now — L1 is unestimable without it)

- All banks pilot on the **same panel**. Composition rule (pinned): ≥8 models spanning ≥3 vendors and ≥3 capability tiers, fixed at the time the FIRST bank pilots; later banks use the identical panel. If a model is retired mid-sequence, its replacement is recorded in §8 and concordance involving it is computed on the surviving intersection (minimum 8; if the intersection falls below 8, L1 pauses for a Fable decision).
- Decoding config pinned per model at first use (temperature, max tokens, system prompt) and reused across banks.

## 3. Data export contract (binds every bank build — add to each bank's Phase A checklist)

Each bank must emit a machine-readable episode-level table: `model_id, method_id, item_family, item_id, clause (C1–C16 or family code), score, rung/stage (if laddered), judge_ids, mechanical_flag, canary_id`. Plus a **declared coverage map** — which clauses the method claims to measure — fixed BEFORE pilot (post-hoc coverage edits are a §8 amendment). Concordance is computed only over declared, shared coverage.

## 4. Interim 2-method concordance gate (CO-8 ⑤ — gates MANYMIRRORS)

- **Statistic:** for each clause covered by both methods, the Spearman correlation across panel models between the two methods' clause scores; the gate statistic is the **median per-clause ρ across shared clauses**, with exact permutation inference (permute model labels within method; 10,000 permutations; one-sided).
- **Pass:** median ρ ≥ 0.4 AND permutation p < .05. **Fail:** MANYMIRRORS build pauses; a Fable session adjudicates (possible outcomes: proceed with MANYMIRRORS as a diagnostic rather than confirmatory method; or investigate method reliability first per §5 disattenuation).
- Report alongside: per-clause ρ table, top-2/bottom-2 model agreement (do the methods agree on which models are best/worst overall — Jaccard on top-2 and bottom-2 sets).

## 5. L1 — model-level cross-method profile concordance (small-n exact)

- **Unit:** model × method clause-profile vectors (mean clause scores over episodes, standardized within method — each method's clause scores z-scored across the panel to remove method-level location/scale).
- **Primary statistic:** per-clause **Kendall's W** across methods (n = panel models, k = methods covering that clause), summarized as the median W across clauses; exact/Monte-Carlo permutation p (permute model labels independently per method).
- **Secondary:** (a) pairwise method-by-method median profile ρ matrix (the "methods that agree" map); (b) per-model profile dispersion (which models' love-profiles are method-stable vs method-dependent — itself a headline-eligible finding); (c) crosswalk-mapped v1/v2 banks appended as extra columns, clearly labeled non-native.
- **Disattenuation (mandatory):** per method × clause, split-half reliability over episodes (Spearman-Brown corrected). Report raw AND attenuation-corrected concordance; a low raw ρ with low reliability is an *item-bank* problem, not a triangulation failure — the report must not conflate these.
- **No latent modeling at L1.** No CFA/CT-CM/SEM on n≈10 models under any circumstances (this is the exact error CO-6a removed).
- **Interpretation bands (pre-registered):** median W ≥ .7 "strong convergence"; .5–.7 "moderate"; < .5 "methods disagree" — the last triggers the secondary portfolio claim (single-method values scores uninterpretable without triangulation bounds) as the lead finding. Either outcome is publishable; neither is a failure state.

## 6. L2 — episode-level clause structure (high-N) and the CO-6b fallback decision

- **Data:** pooled episode-level clause scores across all models and methods, with model and method fixed effects removed (residualize score on model_id × method_id cell means; ordinal scores rank-transformed first).
- **Structure test:** residual clause × clause correlation matrix. Pre-registered contrast: mean within-block minus mean between-block residual correlation, computed under two blockings — (a) 16-clause blocking, (b) the CO-6b 6-family blocking [(i) C1; (ii) C2,C3; (iii) C4,C5,C7; (iv) C6,C10,C11; (v) C12,C13,C14; (vi) C15,C16]. Inference by episode-level permutation within model×method cells.
- **Fallback decision rule (CO-6b, pre-registered):** clause-level reporting stands if the 16-clause blocking contrast is significant AND ≥12 of 16 clauses have a higher mean correlation with their own family than with any other family (discriminant row test). Otherwise reporting drops to the 6-family level; if even the 6-family contrast fails, reporting drops to a single general factor plus the capability-vs-love contrast (C1 vs rest) — that outcome is the "values scores are one blob" headline and must be reported as such, not buried.
- The three v3 designs whose ship-gates were relaxed to "≥ family-level separation" (portfolio §9) are evaluated against whichever level survives.

## 7. Reporting rules

- One dated report per analysis run under `CORINTHLOVE-REVIEWS/` (`YYYYMMDD-megamatrix-L1L2-report.md` + a data snapshot JSON); never overwrite a prior run (Safety Rule 3).
- Every statistic above appears in the report even when unfavorable; silent omissions are treated as integrity violations. Counts of excluded episodes/items (canary hits, manipulation-check failures, coverage gaps) reported fail-loud.
- Tooling: R via `pixi run rscript` (irr::kendall for W, psych for reliability; permutations hand-rolled with fixed seed 20260706) or Python equivalents; seed pinned here.

## 8. Amendment log (append-only)

*(empty at pre-registration)*
