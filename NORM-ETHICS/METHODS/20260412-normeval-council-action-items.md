# NormEval v2 — Council Action Items (Executable Sprint Handoff)

**Date:** 2026-04-12
**Sprint window:** 2026-04-13 (Day 1) → 2026-04-26 (Day 14)
**Target venue:** TMLR (primary) + arXiv (priority claim)
**Source:** `20260412-normeval-submission-council-report.md` (Phase B synthesis)

This document operationalizes the Phase B council verdicts into specific file patches, protocol designs, and a day-by-day calendar. Each section is self-contained and executable.

---

## A1. Dashboard URL Insertion (MUST-DO, 12/12)

**Dashboards to reference** (per root MEMORY.md — these URLs must be verified live before Day 1):
1. `https://cjimmylin.github.io/cei-normeval-dashboard/`
2. `https://cjimmylin.github.io/cei-normeval-dashboard-v2/`
3. `https://cjimmylin.github.io/cei-normeval-dashboard-v3/`

### Files to edit

| File | Approx. location | Change |
|------|------------------|--------|
| `PAPER-v2/abstract-normeval-v2.md` | line 17 (final paragraph) | Expand release sentence to include URLs + Zenodo DOI placeholder |
| `PAPER-v2/conclusion-normeval-v2.md` | line 21 (§7.1 Contribution Five) | Insert URLs + DOI placeholder |
| `PAPER-v2/` (new file) | NEW: `data-availability-normeval-v2.md` | Create Data & Code Availability Statement (see A5) |

### Patches

**A1.1 — Abstract (line 17)**

OLD:
```
We release the complete 54-by-26 feature matrix, all trial data, and an interactive multi-vendor dashboard as open artifacts for the research community.
```

NEW:
```
We release the complete 54-by-26 feature matrix, all trial data, verbatim prompt templates, and three interactive multi-vendor dashboards as open artifacts for the research community. Dashboards: https://cjimmylin.github.io/cei-normeval-dashboard/ (v1, single-vendor), https://cjimmylin.github.io/cei-normeval-dashboard-v2/ (v2, cross-vendor), https://cjimmylin.github.io/cei-normeval-dashboard-v3/ (v3, cross-vendor with temperature-sensitivity replication). All artifacts are archived at Zenodo (DOI: [TO-MINT, A2]) under CC-BY-4.0 (data) / MIT (code).
```

**A1.2 — Conclusion §7.1 Contribution Five (line 21)**

OLD:
```
Fifth, we release open artifacts -- the complete 54-by-26 feature matrix (Table S1), all trial data, and an interactive multi-vendor dashboard -- to enable replication and extension by the research community.
```

NEW:
```
Fifth, we release open artifacts -- the complete 54-by-26 feature matrix (Table S1), all item-level trial data for T1–T15 across 9 models, verbatim prompt templates and model version strings, analysis scripts, and three interactive multi-vendor dashboards (v1 single-vendor: https://cjimmylin.github.io/cei-normeval-dashboard/; v2 cross-vendor: https://cjimmylin.github.io/cei-normeval-dashboard-v2/; v3 cross-vendor + temperature sensitivity: https://cjimmylin.github.io/cei-normeval-dashboard-v3/). All artifacts are permanently archived at Zenodo (DOI: [TO-MINT, A2]) under CC-BY-4.0 (data) / MIT (code). See the Data & Code Availability Statement for full contents.
```

**A1.3 — New Data & Code Availability file**

Create `PAPER-v2/data-availability-normeval-v2.md` with the DAS drafted in A5.

### Verification

```bash
grep -rn "cjimmylin.github.io/cei-normeval-dashboard" PAPER-v2/
# Expected: 3 URL variants (v1, v2, v3) appearing in abstract + conclusion + DAS = ~6 hits
```

Open each URL in a browser to confirm 200 OK before inserting. If v3 does not exist yet (it is the T>0 replication dashboard per A2), mark the URL with `[pending deployment Day 9]` in the patches and deploy before Day 13 (arXiv push).

### Effort

**1 hour** (text edits only). Dashboard verification adds ~15 min.

---

## A2. Gemini T>0 Replication Protocol (SHOULD-DO, sprint §c)

### Protocol specification

| Parameter | Value |
|-----------|-------|
| **Endpoints** | 4 Gemini models from the original study: `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemini-2.5-pro`, `gemini-3.1-pro` (freeze exact API version strings from Zenodo deposit before starting) |
| **Temperatures** | T=0.3, T=0.7, T=1.0 (three non-zero settings; T=0 baseline already in corpus) |
| **Item set** | 30 judgment items drawn from the two benchmarks driving the identity finding: **20 from T13 Oxford Utilitarianism Scale** (all 9 IH items + 9 IB items + 2 attention checks) and **10 from T14 PNAS Cognitive Biases** (stratified: 5 that show cross-vendor divergence between non-Gemini models, 5 that were at ceiling). Pre-register the item list before execution. |
| **Replications per (model × T × item)** | n=3 draws → observe within-setting response variance |
| **Total API calls** | 4 endpoints × 3 temperatures × 30 items × 3 draws = **1,080 calls** |
| **Wall-clock estimate** | ~12 API-hours at standard Gemini rate limits (60 RPM tier); ~4 hours at higher-tier quota. Budget 3 calendar days (Days 4–6) with safety margin for rate-limit backoff. |
| **Analysis** | Per (model, T): compute pairwise Hamming distance across the 4 Gemini endpoints on the 30-item vector. For n=3 draws, report the modal response + within-cell disagreement rate. |

### Decision tree for §5.6 rewrite

**Outcome A — Identity persists at all T>0 (all 4 endpoints produce identical modal responses across all 30 items at T=0.3, 0.7, 1.0):**

> Rewrite §5.6 line 105 Three hypotheses paragraph: delete hypothesis (c) (independent convergence ruled out by T>0 replication). Add: "Temperature-sensitivity replication at T=0.3, 0.7, and 1.0 (Appendix L; n=1,080 calls) confirms that the identity is not an artifact of deterministic decoding: all four endpoints produce modal-identical responses across 30 judgment items at every non-zero temperature tested. Under stochastic sampling, the probability of four genuinely independent inference stacks producing identical modal outputs across 30 items × 3 temperatures is negligible. We conclude that shared inference infrastructure or a shared alignment layer is the only remaining viable explanation."
>
> Abstract (line 15) edit: "raising questions about effective model diversity in the marketplace" → "consistent with shared inference infrastructure across the four Gemini endpoints tested (confirmed by temperature-sensitivity replication at T=0.3/0.7/1.0)."

**Outcome B — Identity dissolves at T>0 (endpoints diverge at any T>0):**

> Rewrite §5.6: "Under stochastic sampling (T=0.3, 0.7, 1.0) the four Gemini endpoints diverge on [X/30] items, dissolving the T=0 identity. This recharacterizes the finding as a temperature-zero decoding convergence rather than shared inference infrastructure. The result remains methodologically consequential: all temperature-zero cross-vendor benchmarks using Gemini endpoints may report artifactually inflated agreement, and future evaluations should default to T>0 for identity diagnostics."
>
> Abstract (line 15): "raising questions about effective model diversity" → "a temperature-zero convergence phenomenon that dissolves under stochastic sampling (Appendix L); at T=0.3 and above, the four endpoints produce distinguishable outputs."

**Outcome C — Partial persistence (some T values persist, others dissolve):**

> Rewrite §5.6 as a structured finding: "Identity persists at T=0.3 (byte-identical) and T=0.7 (97% modal agreement) but dissolves at T=1.0 ([X]% modal agreement). We interpret this as residual structural signal under low-entropy sampling that is overwhelmed by noise at high entropy — consistent with shared-alignment-layer (hypothesis b) but not shared-routing (hypothesis a)."

### Output files

- `STATISTICS/20260413-gemini-t-replication-preregistration.md` — pre-registered item list, expected outcomes, analysis plan (write Day 3, before execution)
- `STATISTICS/20260416-gemini-t-replication-raw.json` — raw API responses, one record per (model × T × item × draw)
- `STATISTICS/20260417-gemini-t-replication-analysis.md` — computed agreement statistics + outcome classification
- `PAPER-v2/appendix-L-temperature-sensitivity-v2.md` — new appendix reporting methods + results
- Dashboard `v3` deployment — add T-sensitivity tab (Day 9)

### Effort

- Protocol pre-reg + item selection: 3 hours (Day 3)
- API execution: ~12 API-hours wall-clock (Days 4–6, runs in background)
- Analysis + §5.6 rewrite: 1 day (Day 7)
- Appendix L drafting: 0.5 day (Day 7)
- **Total analyst time: ~2.5 days; total wall-clock: 4 days**

### Fallback

If Gemini API access fails (rate-limit lockout, endpoint deprecation, quota denial) within 72 hours of Day 4 launch, abort and invoke Expert 9's abstract-demotion path:
- Abstract line 15: "raising questions about effective model diversity in the marketplace" → "consistent with shared inference infrastructure pending stochastic replication."
- §5.6 line 115: keep the 12/12 future-work recommendation but add "We attempted this replication during the pre-submission sprint; API access constraints [specify] prevented execution within the submission window."
- Document failure in new §6.2 subsection "Planned but unexecuted replications."

---

## A3. Paper Identity Reframing (DEFER-WITH-FRAMING, Expert 11 Option a)

This converts the paper from "definitive typology + psychometric instrument" to "landscape atlas + exploratory cross-vendor trials."

### A3.1 — Title

**Files:** `PAPER-v2/abstract-normeval-v2.md` line 2; `PAPER-v2/conclusion-normeval-v2.md` line 2; all other `PAPER-v2/*.md` files with the same title in YAML frontmatter (READ-FIRST: grep every file for `title:` to find and align).

OLD:
```
title: "Three Ethical Profiles, One Knowledge Ceiling: A Meta-Evaluation of 54 Normative Ethics Benchmarks Across Nine LLMs and Three Vendors"
```

NEW:
```
title: "Mapping the Normative Ethics Benchmark Landscape: A 54-Benchmark Atlas and Exploratory Cross-Vendor Trials of Nine LLMs"
```

### A3.2 — Abstract reframing

Four sentences change (all on line 15 of `abstract-normeval-v2.md`):

**Sentence change 1** — "models cluster into three ethical profiles" phrasing:

OLD:
```
Most strikingly, models cluster into three ethical profiles defined by Instrumental Harm tolerance (IH), Cognitive Bias Rate (CBR), and persuasion resistance: a Conservative profile (GPT-5, IH = 2.93; Opus, IH = 3.0), a Moderate profile (Sonnet, IH = 3.2; GPT-5-mini, IH = 3.2), and a Permissive profile (Haiku and all four Gemini models, IH = 4.47).
```

NEW:
```
Exploratory cross-vendor trials reveal two statistically distinguishable clusters (Restrictive: GPT-5, Opus, Sonnet, GPT-5-mini, IH = 2.93–3.2; Permissive: Haiku and all four Gemini models, IH = 4.47) with a tentative exploratory sub-ordering within the Restrictive tier (Conservative: GPT-5, Opus; Moderate: Sonnet, GPT-5-mini) that is not resolved by the current 8.75-items-per-model battery and awaits balanced-battery replication.
```

**Sentence change 2** — framing of landscape contribution:

OLD:
```
We present the first systematic meta-evaluation of normative ethics benchmarks for LLMs.
```

NEW:
```
We present the first systematic atlas of the normative ethics benchmark landscape for LLMs, accompanied by exploratory cross-vendor trials that surface hypotheses for future balanced-battery psychometric validation.
```

**Sentence change 3** — Gemini finding (contingent on A2 outcome):

See A2 decision tree above. Keep placeholder `[Gemini-identity sentence per A2 outcome]` until Day 7.

**Sentence change 4** — release statement: see A1.1 patch.

### A3.3 — §7.1 Conclusion Contribution Three (line 17)

OLD:
```
Third, we document the emergence of three ethical profiles that cluster by moral posture rather than vendor identity: a Conservative profile (GPT-5, Opus; IH approximately 3.0, CBR = 46.2%, 0% persuasion change), a Moderate profile (Sonnet, GPT-5-mini; IH = 3.2, CBR = 53.8%), and a Permissive profile (Haiku, all four Gemini models; IH = 4.47, CBR = 69.2%, 33.3% persuasion change).
```

NEW:
```
Third, we document two statistically distinguishable ethical clusters that cross vendor boundaries — a Restrictive cluster (GPT-5, Opus, Sonnet, GPT-5-mini; IH range 2.93–3.2; non-overlapping CI vs. Permissive) and a Permissive cluster (Haiku, all four Gemini models; IH = 4.47) — with a tentative exploratory sub-ordering inside the Restrictive cluster (Conservative: GPT-5, Opus; Moderate: Sonnet, GPT-5-mini) whose boundary is not resolved by the current 70-discriminating-item battery (Conservative–Moderate IH gap = 0.2 points; CI overlap on the paper's own Table S21). We treat the two-cluster claim as Confirmed and the Conservative–Moderate sub-ordering as an exploratory hypothesis pending balanced-battery replication.
```

### A3.4 — §6.1 Limitations — reframe the "effective battery size" paragraph

**File:** `PAPER-v2/limitations-normeval-v2.md` line 11.

Insert after the existing paragraph's closing sentence:

> Accordingly, we frame this paper as an exploratory meta-evaluation and landscape atlas rather than a validated psychometric instrument. Nunnally's 10–15 items-per-examinee floor applies to instruments that claim individual-level measurement; the present study's unit of inference is the cluster-level posture contrast (Restrictive vs. Permissive), for which the current battery is adequate. A separate instrument-development paper (250+ discriminating items, IRT 2PL/3PL, full-matrix inter-rater reliability) is the appropriate follow-up for individual-model profiling claims (Section 7.3 Future Work).

### A3.5 — New Status-of-Findings table (§4.6 or new §4.7)

Add a new table classifying F1–F7 from `results-crossvendor-normeval-v2.md`:

| Finding | Evidence tier | Rationale |
|---------|---------------|-----------|
| F1a. Restrictive vs. Permissive clusters | **Confirmed** | Non-overlapping CIs on IH, CBR, agreement (Table S21) |
| F1b. Conservative vs. Moderate sub-ordering | **Exploratory** | CI overlap at n=8.75 items/model; awaits balanced battery |
| F2. Gemini identity | **Confirmed** / **Hypothesis** (contingent on A2 outcome) | p ≈ 10⁻¹⁰³ at T=0; temperature-sensitivity [per A2] |
| F3. Universal knowledge ceiling | **Confirmed** | 100% agreement on 44/114 knowledge items, p < 1e-15 |
| F4. Knowledge-judgment divergence | **Confirmed** | 12/12 council endorsement; robust to item decomposition |
| F5. GPT-5 most conservative | **Exploratory** | Confounded with Codex wrapper (Dissent C); cluster-level claim holds |
| F6. Cross-vendor clustering | **Confirmed** | Sonnet–GPT-5 > Sonnet–Haiku agreement (robust to cluster relabel) |
| F7. Non-monotonic persuasion | **Hypothesis-only** | n=3 items; single-item-flip fragility |

### Effort

~1–2 days of prose revision (Days 3–4). No new data.

---

## A4. IRR Sprint Subsample (SHOULD-DO, Expert 2/3/4/11)

### Protocol

| Parameter | Value |
|-----------|-------|
| **Rater panel** | 1 additional human rater with philosophy background + 1 rater trained in care ethics (per Expert 3). If human recruitment fails by Day 2, fall back to a **3-LLM panel** (Claude Opus 4.6, GPT-5 via direct API, Gemini 2.5 Pro) with a structured rubric prompt treating each LLM as a blinded rater. Document the recruitment path in Appendix K. |
| **Benchmark subsample** | **15 benchmarks** (~28% of the 54-benchmark corpus), stratified sample: 5 high-ND, 5 mid-ND, 5 low-ND; within each stratum, 2 care-ethics-adjacent + 2 contractarian-adjacent + 1 random to ensure Expert 3's concern is covered |
| **Features re-rated** | The three highest-subjectivity features only: **Normative Depth (ND)**, **Reasoning Depth (RD)**, **Tradition Engagement (TE)**. (Full 26-feature IRR deferred to post-publication reliability note per Expert 5.) |
| **Rating protocol** | Blinded: raters receive benchmark PDF + rubric (Table S2 extracted to standalone file) + 1-page anchor examples. No access to first-author scores until after completion. |
| **Statistics** | Quadratic-weighted Cohen's κ per feature (ND and RD are ordinal; TE is ordinal with 5 levels) with 95% bootstrap CIs. For the 3-LLM fallback panel, compute ICC(2,k) treating raters as random effects. |
| **Reporting thresholds** | κ ≥ 0.60 = "substantial agreement" (pass). κ ∈ [0.40, 0.60) = "moderate" — report with caveat. κ < 0.40 = "fair" — flag as limitation and soften all claims derived from that feature. |

### Output file

`PAPER-v2/appendix-K-inter-rater-reliability-v2.md` — ~1,500 words including:
- Rater recruitment + blinding procedure
- 15-benchmark stratified sample with justification
- Per-feature κ with 95% CIs
- Disagreement patterns (which benchmarks produced the widest disagreement; qualitative discussion)
- Pre-commitment to 6-month full-matrix IRR update (Expert 5's staged-release framing)

Raw per-rater × per-benchmark × per-feature scores as CSV in Zenodo deposit under `irr/` subfolder.

### Effort

- Day 1–2: rubric extraction + rater recruitment (1 day analyst)
- Days 3–8: parallel rating (40 hours rater-time; runs in background alongside compression + T>0 work)
- Day 9: κ computation + Appendix K drafting (1 analyst-day)

### Fallback

If human rater recruitment fails and the 3-LLM panel also produces κ < 0.40 on any feature:
- Drop all claims derived from that feature from the main text; relocate to Appendix J as "preliminary observations pending reliable rating."
- Report the low κ transparently — a negative IRR result is still better than no IRR result and explicitly neutralizes Expert 9 Attack Vector 5.

---

## A5. FAIR / Zenodo Deposit (MUST-DO, 11/12)

### Deposit contents checklist

| # | Item | Format | Source path | Zenodo target path |
|---|------|--------|-------------|---------------------|
| 1 | 54×26 feature matrix | CSV + JSON | `STATISTICS/20260329-54-benchmark-feature-matrix.csv` (READ-FIRST: confirm canonical path) | `data/feature-matrix.csv`, `data/feature-matrix.json` |
| 2 | Feature schema | JSON Schema | `STATISTICS/20260329-feature-schema.json` (create if absent from Table S2 in paper) | `data/feature-schema.json` |
| 3 | Per-item response vectors T1–T15 × 9 models | JSONL | `STATISTICS/trial-raw/*.jsonl` (READ-FIRST) | `data/trials/T{01..15}.jsonl` |
| 4 | Model version strings | CSV | compile from trial headers | `data/model-versions.csv` |
| 5 | Verbatim prompt templates | MD + plain text | see A7 | `prompts/` (one file per trial) |
| 6 | Codex wrapper config | YAML + readme | export from running environment | `prompts/codex-wrapper-config.yaml` |
| 7 | Decoding parameters | CSV | per-call params; temp, top-p, top-k, max-tokens | `data/decoding-params.csv` |
| 8 | Refusal-detection scripts | Python | `PYTHON/refusal_detection.py` (READ-FIRST: locate) | `code/refusal_detection.py` |
| 9 | Scoring rubric + rater instructions | MD | extract Table S2 + Appendix K rater materials | `docs/rubric.md`, `docs/rater-instructions.md` |
| 10 | Analysis scripts (all stats in paper) | Python notebooks + .py | `PYTHON/normeval_analysis/*.py` (READ-FIRST: confirm existence) | `code/analysis/` |
| 11 | IRR raw data | CSV | from A4 | `irr/raw-ratings.csv` |
| 12 | T>0 replication raw + analysis | JSON + MD | from A2 | `replication/gemini-temperature/` |
| 13 | Dashboard source (v1, v2, v3) | HTML/JS/CSS bundle | `DASHBOARDS/cei-normeval-dashboard{,-v2,-v3}/` (READ-FIRST: locate) | `dashboards/` |
| 14 | Compute cost + ML-CO2 carbon estimate | MD | generate fresh per NeurIPS D&B checklist | `docs/compute-cost.md` |
| 15 | LICENSE files | text | new | `LICENSE-data` (CC-BY-4.0), `LICENSE-code` (MIT) |
| 16 | README with citation | MD | new | `README.md` (BibTeX + DOI + file manifest) |
| 17 | Pre-registration for A2 | MD | A2 output | `preregistration/gemini-t-replication.md` |

### Data & Code Availability Statement (draft text for new `PAPER-v2/data-availability-normeval-v2.md`)

```markdown
## Data & Code Availability Statement

All data, code, prompts, and interactive dashboards supporting this paper are
openly available under FAIR-compliant terms.

**Persistent archive.** All artifacts are permanently archived at Zenodo with
DOI [TO-MINT Day 1] under CC-BY-4.0 (data) and MIT (code) licenses. The deposit
includes (1) the complete 54×26 feature matrix with machine-readable schema;
(2) per-item response vectors for all T1–T15 trials across all 9 models, with
model version strings and decoding parameters; (3) verbatim prompt templates
and system prompts for every trial (see Appendix K.2); (4) the Codex wrapper
configuration used for GPT-5 and GPT-5-mini administration; (5) refusal-
detection and scoring scripts; (6) the scoring rubric and rater instructions
used for the 26-feature characterization; (7) raw inter-rater reliability
data from the 15-benchmark 3-feature sub-study (Appendix K); (8) raw and
analyzed data from the Gemini temperature-sensitivity replication (Appendix L);
(9) compute cost and ML-CO2 carbon estimates; and (10) the source code and
data bundles for three interactive multi-vendor dashboards.

**Interactive dashboards.**
- v1 (single-vendor landscape): https://cjimmylin.github.io/cei-normeval-dashboard/
- v2 (cross-vendor trials): https://cjimmylin.github.io/cei-normeval-dashboard-v2/
- v3 (cross-vendor + temperature-sensitivity replication):
  https://cjimmylin.github.io/cei-normeval-dashboard-v3/

**Reproducibility.** A single `make reproduce` target in the Zenodo deposit
regenerates every figure and table in the main text from the raw trial data,
with fixed random seeds. The `env/` folder pins exact Python, R, and
JavaScript dependency versions used in the published analysis.

**Third-party benchmark data.** The 54 benchmarks themselves retain their
original licenses; our deposit includes item-level responses (model outputs),
not the benchmark source items. Users wishing to reproduce the prompts must
obtain the benchmark source data from the original authors; the deposit
contains direct citations and DOIs for each benchmark.

**Pre-registration.** The Gemini temperature-sensitivity replication
(Appendix L) was pre-registered before execution. The pre-registration file
is included in the Zenodo deposit under `preregistration/`.

**Post-publication update.** A 6-month full-matrix inter-rater reliability
update (all 26 features, 2 additional raters) will be deposited as a v2 of
the Zenodo record by [Day 14 + 6 months] and cross-linked from the record
description.
```

### Target FAIR compliance

≥80% compliance per Expert 7's audit. Specifically: move all 10 current FAIL items from "not present" to PASS via this deposit. The 2 current PASS items (open-access preprint, license declaration) carry over.

### Effort

- Day 1: Create Zenodo record, mint DOI, upload feature matrix + schema (2 hours)
- Day 2: Upload trial response vectors, model versions, decoding params (2 hours)
- Day 2: Bundle prompts + Codex wrapper config (from A7, 2 hours)
- Day 2: Compute cost + ML-CO2 estimate (2 hours)
- Day 9–10: Add IRR raw data, T>0 results, dashboards, final README (2 hours)
- **Total: ~10 hours spread across sprint**

---

## A6. Word Count Restructure → TMLR (MUST-DO, 6/12 + 3 SHOULD)

### Target

TMLR has **no hard length cap**, but its reviewer guidelines recommend ≤12,000 words main text. Council consensus target: **10–12K words main + unlimited appendices.**

**Current estimate:** ~64,700 words across 9 main body files. **Reduction target: ~52K words to supplement or cut (80% compression).**

### Per-section compression targets

READ-FIRST: run `wc -w PAPER-v2/*.md` to obtain exact current counts, then allocate compression proportionally. The table below is a planning target based on typical section weights in a 64.7K-word draft.

| Section / File | Est. current | Target main | Difference | Strategy |
|---|---|---|---|---|
| `abstract-normeval-v2.md` | ~750 | 300 | −450 | Single-paragraph TMLR-style abstract (A3 reframe provides template) |
| `introduction-normeval-v2.md` | ~4,500 | 1,200 | −3,300 | Compress related work to one paragraph; cut motivating vignettes |
| `methods-normeval-v2.md` (or equivalent) | ~8,000 | 1,800 | −6,200 | Move rubric derivations, full 26-feature definitions, gate formula rationale to **Appendix A** (supplement). Keep only: (1) corpus inclusion criteria, (2) feature axis overview, (3) gate summary, (4) trial protocol summary. |
| `results-landscape-normeval-v2.md` | ~7,000 | 1,500 | −5,500 | Keep Claims 1, 3, 4 (ceiling, care-ethics void, knowledge-vs-judgment) in main text; move Claims 2 & 5 + all feature-axis cross-tabs to **Appendix B**. |
| `results-crossvendor-normeval-v2.md` | ~8,000 | 2,000 | −6,000 | Keep F1 (2+1 clusters), F3 (universal ceiling), F4 (K-J divergence), F6 (cluster-by-posture). Move F2 (Gemini identity → §5.6 treatment suffices), F5 (GPT-5 most conservative — covered by F1), F7 (persuasion) to **Appendix C**. |
| `discussion-normeval-v2.md` (§5.1–5.9) | ~16,000 | 3,500 | −12,500 | **Keep in main text:** §5.1 ceiling, §5.3 2+1 profiles (rewritten per A3), §5.4 K-J divergence, §5.9 Western bias. **Move to supplement:** §5.2 consequentialism, §5.5 care/contractarian void, §5.6 Gemini identity (to **Appendix L** with T>0 results), §5.7 refusal, §5.8 benchmark design recommendations. |
| `limitations-normeval-v2.md` | ~2,500 | 800 | −1,700 | Keep methodological top-4 bullets; move scope limitations to supplement. |
| `conclusion-normeval-v2.md` | ~2,500 | 900 | −1,600 | Compress §7.1 to one paragraph per contribution; keep the 5 Calls to Action (~500 words); move §7.3 Future Work to supplement. |
| Appendices A–J (existing) | ~15,500 | unchanged | 0 | Retained in supplement as-is |
| **TOTALS** | **~64,750** | **~12,000** | **−52,750** | Main-text target met; supplement unlimited |

### What gets cut entirely (not relocated)

- Redundant dual-process interpretation paragraphs that appear in both §5.2 and §5.3
- The duplicate "resolution of v1 caveat" paragraph structure (consolidate into one appendix subsection)
- Three-profile rhetorical framing that conflicts with A3 reframe (replace, don't relocate)

### What moves to supplement (unchanged, just relocated)

- Full rubric tables (Table S2 expansions)
- Care ethics prototype (Appendix H in current draft — keep as-is, but per Expert 3's dissent, consider promoting Table S22 caption + 1 paragraph to main text)
- Gemini identity detailed analysis (now merged with T>0 replication in Appendix L)
- Feature axis cross-tabs and robustness checks

### Verification

```bash
wc -w PAPER-v2/abstract-normeval-v2.md PAPER-v2/introduction-normeval-v2.md PAPER-v2/methods-*.md PAPER-v2/results-*.md PAPER-v2/discussion-*.md PAPER-v2/limitations-*.md PAPER-v2/conclusion-*.md
# Sum should be ≤12,500 words by end of Day 8
```

### Effort

~2 days of focused compression (Days 3–4, parallel with A3 reframe which drives some of the cuts anyway). Final polish Day 8.

### Fallback

If main text cannot be compressed below 14K by Day 8 without losing §5.9 (Expert 10's concern), invoke Expert 5's 3-paper split as the fallback venue path — but this triggers the 8-week delay Expert 12 explicitly warns against. Hold the line on TMLR at ≤13K.

---

## A7. Prompt Release Supplementary File (MUST-DO, 9/12)

### New supplementary file

Create `PAPER-v2/appendix-K-prompts-v2.md` (note: letter K is reused if IRR goes to a different letter; reconcile naming when drafting). Bundle into Zenodo `prompts/` folder in A5.

### Required contents (9 sub-items per Expert 7)

For each of T1–T15:

1. **System prompt** (verbatim, or explicit "(none)") — include any `system=` field passed to the API
2. **Assessment prompt template** — the exact item-level prompt with variable placeholders (`{{scenario}}`, `{{options}}`)
3. **Model-specific variations** — if Claude / GPT / Gemini received different wordings (e.g., due to API quirks), show all variants
4. **API version strings** — e.g., `claude-opus-4-20260115`, `gemini-2.5-flash-lite-preview-0417`, `gpt-5-2026-01-XX`
5. **Decoding parameters** — temperature, top-p, top-k, max_tokens, stop_sequences
6. **Codex wrapper configuration** — version, system prompt overlay, any wrapper-injected instructions (critical for Dissent C)
7. **Output parsing regex / scoring function** — exact extraction logic (refusal detection, answer extraction)
8. **Rate limit / retry policy** — for replication cost budgeting
9. **Compute cost + carbon estimate per trial** — for NeurIPS D&B style checklist compliance

### Where to source prompts from (READ-FIRST)

Prompts are likely scattered across:
- `STATISTICS/*-trial-*.json` (per-call logs with `prompt:` field)
- `PYTHON/normeval_trials/*.py` (hardcoded prompt templates in source)
- `NORM-ETHICS/METHODS/*-trial-protocol.md` (protocol docs from session handoffs)

READ-FIRST action item: **Day 2 morning**, grep for `system_prompt|assessment_prompt|prompt_template` across `NORM-ETHICS/` and `PYTHON/` to compile the source set. If any trial's prompts are not recoverable from these locations, flag in §6.1 as "prompt archive incomplete" — this would be a blocker-class finding.

### DAS update

A5's DAS already references `prompts/` folder. Add to DAS: "Verbatim prompt templates with system prompts, decoding parameters, and Codex wrapper configuration for all T1–T15 trials are provided in Appendix K.2 and in the Zenodo deposit under `prompts/`."

### Effort

- Day 2 morning: compile prompt sources (2 hours)
- Day 2 afternoon: draft Appendix K.2 structured document (3 hours)
- Day 3: per-trial table population + cross-checks (3 hours)
- **Total: ~1 person-day**

### Fallback

If a specific trial's prompts cannot be recovered verbatim, write: "T[X] prompt template reconstructed from protocol documentation; verbatim API calls not archived. Reproduction may require minor prompt adjustment." This is a non-ideal but honest disclosure and does not block submission.

---

## A8. 2+1 Profile Reframe (SHOULD-DO, 6 SHOULD + 2 MUST)

Mechanical patches supporting A3. This is the same reframe, localized to specific table and caption edits.

### A8.1 — §4.6 Table 4 rewrite

**File:** `PAPER-v2/results-crossvendor-normeval-v2.md` — locate Table 4 (READ-FIRST: grep for `Table 4` or `| Profile |` to find exact line).

Replace the existing 3-row profile table with the 2+1 template from Phase B §Item 9:

```markdown
| Profile | Models | Evidence tier |
|---|---|---|
| **Restrictive** | GPT-5 (†), Opus, Sonnet, GPT-5-mini (†) | Robust (non-overlapping 95% CI vs. Permissive on IH, CBR, agreement — Table S21) |
| **Permissive** | Haiku, Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, Gemini 2.5 Pro, Gemini 3.1 Pro | Robust |
| *Exploratory sub-tier within Restrictive* | Conservative (GPT-5 †, Opus) vs. Moderate (Sonnet, GPT-5-mini †) | Tentative — IH gap = 0.2 points, CI overlap at current n=8.75 items/model; unresolved in current data pending balanced-battery replication |

(†) Codex wrapper confound — see Dissent C, §6.1.
```

New caption:
> **Table 4. Two cross-vendor ethical clusters with a tentative exploratory sub-ordering.** Cluster membership derives from joint IH / CBR / pairwise-agreement analysis on the 70 discriminating items (see §4.6 and Appendix G Table S21). The Restrictive–Permissive distinction passes the non-overlap test on all three measures (Appendix G); the Conservative–Moderate sub-ordering does not and is labeled exploratory. Models cluster by ethical posture, not by vendor origin.

### A8.2 — §5.3 section rename

**File:** `PAPER-v2/discussion-normeval-v2.md` line 41.

OLD:
```
### 5.3 Three Ethical Profiles: A New Taxonomy
```

NEW:
```
### 5.3 Two Ethical Clusters with an Exploratory Sub-Ordering
```

Rewrite §5.3 opening paragraph (line 43):

OLD:
```
The central empirical contribution of this paper is the identification of three distinct ethical profiles that cluster by moral posture rather than by vendor or model scale (Section 4.6, Table 4, Figures 6--7). We define these profiles and discuss their theoretical and practical significance.
```

NEW:
```
The central empirical contribution of this paper is the identification of two statistically distinguishable ethical clusters — Restrictive and Permissive — that cross vendor boundaries, together with a tentative exploratory sub-ordering (Conservative vs. Moderate) within the Restrictive cluster whose boundary is not resolved by the current 70-discriminating-item battery (Table S21). We describe the clusters, the evidence supporting the two-cluster claim, and the unresolved status of the Conservative–Moderate contrast.
```

Throughout §5.3 (lines 43–67): global find-and-replace within this section only:
- "three profiles" → "two clusters with an exploratory sub-ordering"
- "three ethical profiles" → "two ethical clusters"
- "Conservative profile" → "Conservative sub-cluster (exploratory)" on first mention per paragraph, then "Conservative" bare
- "Moderate profile" → "Moderate sub-cluster (exploratory)" on first mention per paragraph
- "Permissive profile" → "Permissive cluster"
- Keep "Restrictive cluster" as the new umbrella term

### A8.3 — §7.1 Contribution 3 — see A3.3 patch above (already drafted)

### A8.4 — Calls 4 and 5 adjustments

**File:** `PAPER-v2/conclusion-normeval-v2.md` lines 35, 37.

Call 4 — replace "three ethical profiles" with "two ethical clusters documented in this paper (with an exploratory third sub-ordering)". Keep the vendor-disclosure recommendation intact.

Call 5 — same substitution: "ethical profiles cluster by moral posture rather than vendor origin" → "ethical clusters cross vendor boundaries."

### A8.5 — Abstract sentence — already covered in A3.2 Sentence change 1

### Verification

```bash
grep -c "three ethical profiles\|three profiles\|three-profile" PAPER-v2/*.md
# Target: 0 after reframe (any residuals = missed edit)
```

### Effort

~1 day of localized rewriting. Runs in parallel with A6 compression Days 3–4.

---

## Sprint Timeline (Day 1 = 2026-04-13 → Day 14 = 2026-04-26)

| Day | Date | Primary tasks (parallel work-streams) |
|-----|------|---------------------------------------|
| **1** Mon | 04-13 | **A1** dashboard URL insertion (1h) · **A2** launch (mint Zenodo DOI stub) · **A6** venue decision + compression plan (4h) · **A8.2** §5.3 rename · **A13** rater recruitment begins · Abstract Expert 10 Western-bias sentence · Expert 1 BetterBench/Snoswell citations added |
| **2** Tue | 04-14 | **A5** upload feature matrix, trial vectors, model versions to Zenodo · **A7** compile prompt sources + draft Appendix K.2 · **A5** compute cost + ML-CO2 estimate · **A18** initiate vendor disclosure emails (30-day clock starts) |
| **3** Wed | 04-15 | **A2** pre-registration file written and deposited · **A3** title + abstract reframe · **A6** main-text compression pass 1 (Methods + Results — Landscape) · **A14** IRR rating begins (parallel background) · **A8.1** Table 4 rewrite |
| **4** Thu | 04-16 | **A2** Gemini T=0.3 runs launch (background) · **A6** compression pass 2 (Results — Cross-vendor + Discussion) · **A3.5** Status-of-Findings table drafted · **A14** IRR rating continues |
| **5** Fri | 04-17 | **A2** Gemini T=0.7 runs · **A6** compression pass 3 (Limitations + Conclusion) · **A14** IRR rating continues · **A8.2–A8.4** global profile→cluster sweep verification |
| **6** Sat | 04-18 | **A2** Gemini T=1.0 runs + analysis begins · **A14** IRR completion · **A6** supplement assembly |
| **7** Sun | 04-19 | **A2** §5.6 rewrite + Appendix L draft · **A1** abstract Gemini sentence updated per A2 outcome · **A6** supplement final pass |
| **8** Mon | 04-20 | **A4** κ computation + Appendix K drafting (day 1 of 2) · **A6** main-text word count verification ≤12K · Integration cross-checks (all profile→cluster edits consistent) |
| **9** Tue | 04-21 | **A4** Appendix K finalized · Dashboard v3 deployed with T-sensitivity tab · **A1** dashboard v3 URL swap from `[pending]` to live · **A5** Zenodo deposit IRR + T>0 raw data upload |
| **10** Wed | 04-22 | **A19** internal co-author review pass 1 · Figure regeneration from compressed data · All table captions aligned with A8 reframe |
| **11** Thu | 04-23 | **A19** internal review pass 2 + response to co-author comments · References audit (BibTeX cleanup) · FAIR audit self-check ≥80% |
| **12** Fri | 04-24 | **A19** final polish · Cover letter drafting · Supplementary file bundling |
| **13** Sat | 04-25 | **A20** arXiv submission (priority claim) · Zenodo DOI cross-linked · Social media announcement queued for Day 14 |
| **14** Sun | 04-26 | **A21** TMLR submission · Final verification of all dashboard URLs + Zenodo DOI in submitted manuscript · Submission confirmation archived |
| (Day 32) | 05-14 | **A18** vendor disclosure 30-day window clears — integrate any responses into §6.3 for TMLR first-revision round |

### Dependencies

- **Critical path (14 days):** A2 pre-reg → A2 execution → A2 analysis → §5.6 rewrite → A19 review → A20/A21 submission
- **Secondary path (parallel):** A3/A8 reframe → A6 compression → A19 review
- **Tertiary path (parallel):** A13 rater recruitment → A14 IRR rating → A4 analysis → Appendix K → A19 review
- **Zenodo path (parallel, drives A5 and A7):** A5 DOI mint Day 1 → iterative upload Days 2–9 → final version Day 13
- **Non-blocking background:** A18 vendor disclosure (30-day clock, does not block submission)

---

## Risks & Contingencies

| Action | Risk | Fallback | Abort decision point |
|--------|------|----------|----------------------|
| **A1** Dashboard URLs | One of v1/v2/v3 offline or 404 | Deploy missing dashboard from local source on Day 9; if impossible, cite only the 2 live URLs and add footnote "v3 deployment pending" | Day 12 — if any URL still 404, remove it from the abstract but keep in DAS with note |
| **A2** Gemini T>0 | API rate-limit lockout, endpoint deprecation, quota denial | Expert 9 abstract-demotion path: change "raising questions about effective model diversity" → "consistent with shared inference infrastructure pending stochastic replication"; document failure in §6.2 | Day 6 EOD — if < 50% of calls completed and no rate-limit relief in sight, abort and invoke fallback |
| **A2** Gemini T>0 | Outcome C (partial persistence) is ambiguous to write up | Pre-draft all three outcome narratives (A/B/C) during Day 3 pre-registration so Day 7 writeup is assembly not composition | Day 7 morning — if analysis is still ambiguous at EOD, report the raw numbers and let the reader interpret |
| **A3** Reframe | Co-author pushback on retitling "Three Ethical Profiles" → "Mapping the Landscape" | Compromise title: *"Mapping the Normative Ethics Benchmark Landscape: Two Cross-Vendor Clusters and a 54-Benchmark Atlas"* — retains landscape framing and explicit 2-cluster headline. Cite Expert 2, 4, 11 consensus as decision rationale. | Day 4 EOD — if co-authors block, escalate to 48-hour decision; if unresolved by Day 6, proceed with original title and note dissent in submission letter |
| **A4** IRR | Human rater recruitment fails; LLM-panel κ < 0.40 on any feature | Soften all claims derived from that feature; relocate to Appendix J; transparently report the low κ as a limitation (better than no IRR) | Day 2 EOD — if no human raters confirmed, switch to 3-LLM panel immediately |
| **A4** IRR | 15-benchmark stratified sample over-weights one ND band because of benchmark sparsity | Use the full 54-benchmark corpus for the care-ethics and contractarian strata specifically; weight stratum sizes by availability | Day 1 — during sample selection |
| **A5** Zenodo | Deposit size exceeds free tier (50 GB) | Move dashboard source bundles to GitHub releases; link from Zenodo README | Day 2 — if deposit approaches 40 GB |
| **A5** FAIR | Refusal detection scripts not recoverable from repo | Re-derive from trial logs + document reconstruction; flag in DAS as "post-hoc recovery" | Day 2 — after code audit |
| **A6** Compression | Main text cannot reach ≤13K without gutting §5.9 Western bias (Expert 10) | Accept 13.5K target; TMLR has no hard cap. If TMLR rejects on length alone, invoke Expert 5 3-paper split fallback (8 weeks, deprioritized) | Day 8 — word count checkpoint |
| **A7** Prompts | Verbatim prompts not archived for some trials | Reconstruct from protocol docs; disclose reconstruction in Appendix K.2 | Day 2 — after source audit |
| **A8** Reframe consistency | Residual "three profiles" phrasing missed across 9 files | Day 10 grep verification `grep -rn "three profile\|three ethical\|3-profile" PAPER-v2/` → target 0 hits | Day 10 — if >5 residuals, spend Day 11 morning on cleanup |
| **A19** Internal review | Co-author identifies a blocker in A2/A3/A4 content on Day 11 | Push A20/A21 to Days 14/15, use one-day buffer; accept 1-day slip | Day 11 EOD — last fix-in-sprint deadline |
| **A21** TMLR submission | TMLR portal error or missing metadata field at submission | Have OpenReview account + co-author permissions confirmed by Day 12 | Day 13 — dry-run submission with draft PDF |
| **A18** Vendor disclosure | Google, OpenAI, or Anthropic respond with legal objection | Document the objection in §6.3; proceed with submission (30-day notice satisfied even without response); be prepared to redact specific model-version claims in revision | Day 14 — independent of sprint submission; handled at first-revision round |

### Submission go/no-go checklist (Day 14 morning)

Before pushing TMLR submit:

- [ ] Dashboard URLs v1, v2, v3 all return 200 OK
- [ ] Zenodo DOI minted, all 17 deposit items present, FAIR ≥80%
- [ ] Main text word count ≤13,000
- [ ] Zero residual "three profiles" phrasing (grep verified)
- [ ] Title matches A3.1 (or approved compromise)
- [ ] Abstract dashboard URLs and DOI present
- [ ] §5.6 updated with A2 Gemini outcome (or fallback language)
- [ ] Appendix K (IRR) present with reported κ values
- [ ] Appendix L (T>0 replication) present OR documented fallback in §6.2
- [ ] Status-of-Findings table present (F1–F7 tiered)
- [ ] DAS section present and cross-linked
- [ ] Responsible disclosure emails sent + acknowledged (Day 2 + log)
- [ ] BetterBench + Snoswell citations in §2
- [ ] Western-bias abstract sentence present
- [ ] Co-author sign-off on file

If any box unchecked on Day 14 morning: **do not submit to TMLR**. Submit to arXiv only (priority claim) and defer TMLR to Day 15–16 after remaining items resolved. Expert 12's novelty window is 2–4 months; a 1–2 day slip does not meaningfully erode first-mover credit.

---

## Deferred items (explicitly not in sprint)

- **A22** T1–T5 cross-vendor replication — deferred to follow-up study per Phase B §Item 3 (7 DEFER-TO-FUTURE, 4 DEFER-WITH-FRAMING). Framing sentence added to §6.1 per Expert 5.
- **A23** Full 54×26 IRR — deferred to 6-month post-publication reliability note per Expert 5's staged-release framing. Pre-committed in DAS.
- **Expert 11 Option (b)** — 12–18 month instrument-development paper (250+ items, IRT, CFA/LCA). Not pursued; Expert 12's novelty half-life analysis dominates. Acknowledged as the "maximum-rigor path" in §7.3 Future Work.
- **Expert 5 3-paper split** — held as fallback only if TMLR rejects.

---

## Handoff notes

- This document is the executable contract for the 14-day sprint. Each section A1–A8 is self-contained and can be assigned to a different collaborator.
- **READ-FIRST flags** mark locations where exact file paths, line numbers, or content must be verified before editing. Do not apply patches blindly to paths this document guesses at.
- All text patches use the current (2026-04-05) v2 draft as the baseline. If any of those files have been edited between 2026-04-12 and Day 1, re-derive the patch against the current state.
- Source of truth for verdicts: `20260412-normeval-submission-council-report.md` §3 Item-by-Item and §7 Prioritized Action List. Any conflict between this action-items document and the council report is resolved in favor of the council report.
- End-of-sprint handoff document (per CLAUDE.md session conventions): write `METHODS/20260426-normeval-sprint-completion-handoff.md` on Day 14 summarizing executed vs. fallback paths, κ values, A2 outcome, and submission confirmation numbers.
