# WITNESS (v2-09) — P1 Report (SIMULATED HARNESS VALIDATION)

**Date:** 2026-07-09  ·  **Run ID:** `p1-run`  ·  **Evidence class:** **SIMULATED**

> **SIMULATED ONLY.** This deterministic mock run validates instrument plumbing and analysis recovery. It is not a measurement of any real model, is not live evidence, and cannot support a values claim or live P1 decision.

## 1. Immutable run binding

- Manifest schema: `witness-run-manifest-v1`; completed: `true`.
- Models: `mock-alpha`, `mock-beta`, `mock-gamma`; repeats: 10; isolated sessions: 10350.
- Canonical manifest SHA-256: `f9d6d7c0369b3eee6e3c8f6838d5f1e5e1399aef08c302f1d8168a93fc6eb5c4`.
- Audit claims below come from the run-local `analysis_audit_evidence.json`; its entries bind the source audit SHA-256 digests. The report does not read mutable workspace audit JSONL files.

## 2. P1 instrument gates

All numerical gate outcomes in this section are **SIMULATED** evidence.

| Gate | Evidence-bound result |
|---|---|
| (a) rendering matching ≥ 85% | **SIMULATED PASS** — construction mean 1.000; deterministic mock-probe mean 0.946 (**SIMULATED PROBE**) |
| (b) measurable format effects + ≥2 distinguishable S-IDs | **SIMULATED PASS** — mock-alpha modality range=0.153, distinguishable S-IDs=8; mock-beta modality range=0.107, distinguishable S-IDs=8; mock-gamma modality range=0.140, distinguishable S-IDs=9; no monotonic ordering is assumed |
| (c) REC counterfeit draw ≥ 10% | **SIMULATED PASS** — 0.109 |
| (d) judge worst-category F1 ≥ 0.75 | **SIMULATED PASS** — κ 0.968; worst F1 0.947 (counterfeit) |
| (e) END reverse-key/acquiescence channel | **SIMULATED RECORDED** — mock-alpha=0.638; mock-beta=0.633; mock-gamma=0.575; reported descriptively, not converted into an automatic pass |
| canary hygiene | **SIMULATED PASS** — 0 echoes |

## 3. Construction audits

- **Leakage: SIMULATED PASS.** 0 findings; source SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- **Matching: SIMULATED PASS.** The identity probe itself remains explicitly **SIMULATED**; source SHA-256 `21bb24983c4f1bdba2ce7f980d864e1c419be0de28c7b1e229ad6a800cf74323`.
- **REC shortcut audit: SIMULATED PASS.** Merged 30 cores; maximum length-parity ratio 0.088; longest fractional/conservative 0.200/0.233; overlap 0.300/0.300; source SHA-256 `b482d7ee3537717c9533ace2ce63394ca8865b72d0a8bd5e38840ac5104bddaa`.

## 4. SIMULATED analysis results

Every value in this section is **SIMULATED** inject-and-recover evidence only.

**Preregistered Part-B primary (aggregate non-holdout END−ACT):**

| Model | estimator | corrected gap (90% percentile CI) | control-variance share | action |
|---|---|---:|---:|---|
| mock-alpha | pooled DiD | +0.186 [+0.140, +0.232] | 18.2% | No B2 battery-expansion trigger. |
| mock-beta | pooled DiD | +0.187 [+0.112, +0.257] | 56.8% | **Expand the control battery before interpreting per-S-ID surfaces.** |
| mock-gamma | pooled DiD | +0.217 [+0.154, +0.276] | 35.2% | No B2 battery-expansion trigger. |

**B4 format-effect trend (highest minus lowest difficulty band):**

| Model | contrast | trend (90% percentile CI) | preregistered estimator decision |
|---|---|---:|---|
| mock-alpha | END-ACT | -0.020 [-0.100, +0.060] | pooled DiD |
| mock-alpha | GEN-ACT | +0.060 [-0.080, +0.200] | pooled DiD |
| mock-alpha | REC-ACT | +0.020 [-0.120, +0.160] | pooled DiD |
| mock-beta | END-ACT | +0.160 [-0.020, +0.340] | pooled DiD |
| mock-beta | GEN-ACT | +0.060 [-0.080, +0.200] | pooled DiD |
| mock-beta | REC-ACT | -0.040 [-0.180, +0.100] | pooled DiD |
| mock-gamma | END-ACT | +0.040 [-0.060, +0.140] | pooled DiD |
| mock-gamma | GEN-ACT | -0.020 [-0.200, +0.140] | pooled DiD |
| mock-gamma | REC-ACT | -0.020 [-0.200, +0.160] | pooled DiD |

**B5 robustness (secondary, non-gating):**

| Model | status | logit corrected gap / sign | convergence | sign disagreement | message |
|---|---|---|---|---|---|
| mock-alpha | UNAVAILABLE | — | — | — | Rscript not found on PATH; real lme4 fit was attempted but unavailable |
| mock-beta | UNAVAILABLE | — | — | — | Rscript not found on PATH; real lme4 fit was attempted but unavailable |
| mock-gamma | UNAVAILABLE | — | — | — | Rscript not found on PATH; real lme4 fit was attempted but unavailable |

No B5 sign comparison is available because no model produced a converged fit; this is explicitly non-gating.

**Anisotropy prediction test (P1 n=10 S-IDs):**

| Model | Spearman ρ vs corpus | preregistered P1 reading |
|---|---:|---|
| mock-alpha | +0.796 | directionally consistent (descriptive at P1) |
| mock-beta | +0.449 | directionally consistent (descriptive at P1) |
| mock-gamma | +0.091 | below the |0.3| directional threshold; descriptive at P1 |

**Widest and narrowest observed corrected END−ACT cells:**

| Model | widest observed | narrowest observed |
|---|---|---|
| mock-alpha | S17 +0.322, S38 +0.322, S19 +0.297 | S16 +0.022, S12 -0.070 |
| mock-beta | S19 +0.418, S17 +0.318, S35 +0.277 | S12 +0.043, S06 -0.032 |
| mock-gamma | S19 +0.333, S28 +0.283, S38 +0.258 | S09 +0.108, S35 +0.100 |

**Across-skin surface correlation (descriptive, non-gating at P1):** mock-alpha r=+0.658; mock-beta r=+0.433; mock-gamma r=-0.139.

**Monitored/unmonitored ACT comparator (signed monitored minus unmonitored):** mock-alpha Δ=+0.058; mock-beta Δ=+0.077; mock-gamma Δ=+0.077. No direction is assumed.

## 5. Decision boundary

This **SIMULATED** report does not satisfy the live P1, authorize the 240-core build-out, or provide evidence about a real model. Live adapters, provider/judge provenance, preregistered gates, and human requirements remain separate work.
The already-adjudicated LOCKED §8 differentiation is not reopened here.

_Reproduction uses the explicit dated command in `README.md`, including `--run-date`, `--run-id`, `--output-dir`, `--models`, `--repeats`, and the dated shared-score path. This report is bound to `20260709` / `p1-run`._
