# Full-Coverage 292-Benchmark Assessment: Study Design Document

**Date:** 2026-04-05 (Session 19)
**Purpose:** Expand the moral psychology benchmark meta-evaluation from 54 assessed candidates to all 292 candidates, replacing the top-15 binary selection with a 4-tier ranking system (top/high/med/low) using Jenks natural breaks on composite scores. All 292 candidates are re-scored from scratch for internal consistency.

**Previous work superseded:** `20260404-extended-feature-matrix-v3.json` (54 × 162 matrix)

---

## 1. Council Roster

A 12-member expert council was assembled specifically for this expansion study. The council is optimized for two challenges the original Council A did not face: (a) scoring candidates with limited source material (the 237 previously unassessed candidates have variable information availability), and (b) designing a continuous quality classification rather than a binary selection threshold.

| ID | Role | Primary Responsibility | Feature Assignments |
|----|------|----------------------|---------------------|
| C1 | **Psychometric Methodologist** | Scoring rubric consistency, inter-batch calibration, null-handling rules | D1–D24 rubric authority |
| C2 | **Statistical Classifier** | Jenks natural breaks algorithm, tier boundary sensitivity analysis, distribution diagnostics | Phase 4 lead |
| C3 | **MFT Specialist** | Accurate scoring of MFT-adjacent candidates; distinguishes vocabulary borrowing from genuine theory engagement | A1–A6 for MFT candidates |
| C4 | **Process Theories Expert** | Scoring dual-process, intuitionist, and dyadic candidates that keyword scorer undervalues | A1–A6 for underrepresented theories |
| C5 | **Values & Identity Expert** | Schwartz, Kohlberg, identity theory scoring; theory version currency (G1) | A1–A6 for values/developmental candidates |
| C6 | **Cultural Psychology Expert** | Non-Western candidates, cross-cultural validation, WEIRD bias assessment | F1–F44 lead |
| C7 | **LLM Evaluation Specialist** | Practical implementability, harness compatibility, prompt sensitivity | E1–E44 lead |
| C8 | **Data Engineering Expert** | Information availability triage, source material quality grading, data format assessment | B1–B10, G23–G28 |
| C9 | **Bibliometrician** | Citation data, venue tiers, replication counts, theory genealogy | C1–C5, G13–G22 |
| C10 | **Impact Analyst** | Traces how full-coverage results change each of 5 claims; identifies new findings enabled by tier system | Phase 5 lead |
| C11 | **Paper Integration Architect** | Maps section-by-section edits, ensures narrative coherence across methodology–results–discussion | Phase 6 lead |
| C12 | **Quality Auditor** | Post-wave calibration checks, outlier detection, coverage verification, anchor scoring comparison | Phase 3 calibration gates |

---

## 2. Council Deliberation Record

### 2.1 Information Availability Triage

**Decision context:** The original 54-benchmark assessment relied on deep paper reading (abstracts + full PDF extracts + supplementary materials). The 237 previously unassessed candidates have variable source material — some have rich PDF extracts, others have only titles and mp_* keyword scores. The council must define how to handle this heterogeneity.

**C1 (Psychometric Methodologist):** Inconsistent information depth is the primary threat to scoring validity. If we score a benchmark 0 on E4 (prompt template sensitivity) because the paper doesn't discuss prompt variation, that's not the same as a genuine score of 0 from a paper that explicitly tested only one prompt. We need to distinguish "absent evidence" from "evidence of absence."

**C8 (Data Engineering Expert):** I propose three information tiers based on what's available:

| Info Tier | Criteria | Expected Count | Scoring Implications |
|-----------|----------|---------------|---------------------|
| **A** | PDF extract exists + abstract populated + paper file exists | ~180–200 | Full scoring possible across all 158 features |
| **B** | Paper file exists with abstract but no PDF extract | ~60–80 | Tiers A–C scorable from abstract/metadata; D–G features requiring deep reading score as `null` or `inferred` |
| **C** | Minimal metadata only (title, year, venue, mp_* scores) | ~15–30 | Only metadata-derivable features scorable (year, venue tier, theory classification); most features null |

**C1:** I accept this triage. For Tier B and C candidates, we adopt the following null policy:

**DECISION — Null Policy:**

1. **Explicit null** (`null`): Used when a feature cannot be scored from available information AND the absence of information is not itself informative. Example: D3 (factor structure validation) for a Tier C candidate where we simply don't have the paper — we don't know if they did factor analysis or not.

2. **Inferred zero** (score: 0, confidence: `inferred`): Used when the absence of information IS informative. Example: C5 (hub/leaderboard presence) — if a benchmark has no presence on Papers With Code or HuggingFace, that's a genuine 0 regardless of our access to the paper. Similarly: G20 (pre-registration) can be checked externally; G24 (licensing) can be checked from repositories.

3. **Conservative estimate** (score: N, confidence: `low`): Used when partial information allows a bounded estimate. Example: A Tier B candidate with abstract mentioning "MFQ-30" can be scored A4=100 (validated source instrument) with high confidence, even without the PDF extract.

**C12 (Quality Auditor):** I want a hard rule: any candidate with >60% null features is excluded from tier ranking but still reported in supplementary materials. They contribute to "total landscape" counts but not to the quality distribution analysis.

**DECISION — Maximum null rate:** 60% of 158 active features = 95 features. Candidates with >95 null features are flagged as "insufficient data for tier ranking" and excluded from Jenks analysis. They appear in supplementary tables with a dagger (†) symbol.

### 2.2 Confidence Grading

**C1:** Every score cell carries a confidence grade:

| Grade | Meaning | When Used |
|-------|---------|-----------|
| `high` | Scored from direct evidence in abstract or PDF extract | Tier A candidates; metadata-derivable features for all tiers |
| `medium` | Scored from indirect evidence (e.g., venue implies peer review quality) | Tier B candidates on features requiring some inference |
| `low` | Conservative estimate from minimal information | Tier C candidates; features where only bounds can be established |
| `inferred` | Score of 0 assigned because absence of evidence is itself informative | Hub presence, pre-registration, open access — checkable externally |

**C7 (LLM Evaluation Specialist):** For Tier E features (LLM-specific validity), most Tier B/C candidates will score low regardless of information availability — these are features that require the benchmark to have been administered to LLMs with sensitivity analysis, which most haven't done. So low scores here reflect genuine quality gaps, not information gaps.

**C6 (Cultural Psychology Expert):** Same for Tier F. Most benchmarks have not been validated cross-culturally. A score of 0 on F6 (cultural validation breadth) is usually genuine, not an information gap.

**DECISION:** Confidence grades are recorded but do NOT affect composite scoring. A score of 40 with confidence `low` contributes the same 40 to the composite as a score of 40 with confidence `high`. The confidence grades are for transparency and future sensitivity analysis, not for weighting.

### 2.3 Composite Formula

**C2 (Statistical Classifier):** The current formula is PD×0.50 + PE×0.30 + CI×0.20, using only Tiers A–C. We now have Tiers D–G with 134 additional features. Should the composite incorporate them?

**C1:** No — and here's why. The 28-feature core (Tiers A–C) was designed as a *selection* instrument. The extended features (D–G) were designed as a *characterization* instrument. They answer different questions: the core asks "is this benchmark worth using?" while the extended asks "what are its detailed properties?" Mixing them would dilute the selection signal with characterization noise.

**C10 (Impact Analyst):** I agree. The paper's 5 claims are all framed around the core composite (PD/PE/CI). Changing the composite formula would break comparability with the existing analysis and force us to re-derive all claims from a new scoring basis. The extended features should be reported as tier profiles, not folded into the ranking composite.

**DECISION — Composite formula unchanged:**
```
PD = A2(0.25) + A6(0.20) + A1(0.15) + A5(0.15) + A3(0.15) + A4(0.10)
PE = B3(0.20) + B2(0.15) + B6(0.15) + B7(0.15) + B1(0.10) + B4(0.10) + B10(0.15)
CI = C1(0.30) + C2(0.30) + C3(0.25) + C5(0.15)
COMPOSITE = PD × 0.50 + PE × 0.30 + CI × 0.20
```

**However**, the extended features (D–G) will be reported as **tier profiles** — aggregate statistics computed within each tier to characterize what distinguishes "top" from "low" benchmarks beyond the core composite.

### 2.4 Tier Semantics

**C2:** The Jenks algorithm will find natural breaks in the composite score distribution. But we need to define what each tier *means* — the algorithm finds gaps, but the labels need semantic content.

**Council consensus after deliberation:**

| Tier | Label | Composite Range | Semantic Definition |
|------|-------|----------------|---------------------|
| **Top** | Publication-ready | TBD (Jenks) | Psychometrically validated, theory-grounded, data-available benchmarks with construct validity evidence (A6≥4) and human baselines. Suitable for definitive LLM moral evaluation claims. |
| **High** | Research-grade | TBD (Jenks) | Meaningful theoretical engagement with moderate-to-strong operationalization. May lack cross-cultural validation, comprehensive baselines, or LLM-specific revalidation. Suitable for exploratory research with appropriate caveats. |
| **Med** | Emerging | TBD (Jenks) | Either theory-inspired without formal validation, OR technically strong (large dataset, good format) but theoretically shallow. Represents the modal benchmark: reasonable effort, incomplete psychometric grounding. |
| **Low** | Landscape-only | TBD (Jenks) | Keyword-level engagement with moral psychology. May use MFT terminology without testing MFT predictions, or employ ad-hoc moral classification without theoretical grounding. Documents the field's breadth but not suitable for drawing psychological conclusions about LLMs. |

**C3 (MFT Specialist):** The "low" tier is critical for Claim 1. Many of the 101 MFT-detected papers use MFT *vocabulary* without MFT *theory*. The tier system will quantify this: how many MFT candidates are genuinely "top" vs. just borrowing terminology?

**C4 (Process Theories Expert):** And for Claim 3, the tier system answers a harder question than "are there zero benchmarks?" It answers "are there any *good* benchmarks?" If all dual-process candidates land in "low" or "med," the claim strengthens from "missing" to "absent at every quality level."

### 2.5 Downstream Impact Map

**C10 (Impact Analyst) and C11 (Paper Integration Architect)** produced the following impact map:

| Paper Section | Current Basis | New Basis | Expected Impact |
|--------------|--------------|-----------|-----------------|
| §3.2 Assessment | 55 assessed via 3-pass protocol | 292 assessed via batch-calibrated protocol | Major rewrite |
| §3.4 Selection | 5-step algorithm → top-15 | Jenks natural breaks → 4 tiers | Complete replacement |
| §4.1 Claim 1 (MFT) | 222 candidates, 55 assessed, top-15 | 292 candidates, all assessed, tier distribution | Statistics change; MFT×tier crosstab is new |
| §4.2 Claim 2 (Validity) | A6 distribution over 55 | A6 distribution over 292 | Gap likely widens dramatically |
| §4.3 Claim 3 (Missing) | "3 theories have zero benchmarks" | "3 theories have zero top/high benchmarks" | Claim refines (stronger or softer) |
| §4.4 Claim 4 (Baselines) | 18% no baselines (of 55) | % no baselines (of 292) | Deficit rate likely increases |
| §4.5 Claim 5 (Format) | Format distribution over 55 | Format distribution over 292 + tier×format | New tier dimension |
| §5 Discussion | "Value monoculture" thesis | Same thesis + tier evidence | Strengthened with full-coverage data |
| §5.3 Limitations | "Only 55 assessed" | Info tier confidence grades | Limitation changes character |
| Abstract | "assess 55 in depth" | "assess all 292 candidates" | Number updates |
| §1.5 Five Claims | Claim statistics | Updated statistics | Number updates |
| §6 Conclusion | Recommendations based on top-15 | Recommendations based on tier landscape | Richer recommendations |
| Supp S1 | 54×162 matrix | 292×158 matrix + tier assignments | Major expansion |

**New analyses enabled:**
1. **Quality gradient over time** — are 2024–2026 benchmarks better than 2018–2020?
2. **Theory × quality interaction** — is MFT's median quality higher or lower than Schwartz's?
3. **Infrastructure → quality pathway** — does data availability predict tier independent of psychological depth?
4. **Hidden gems** — are there genuinely good benchmarks in the previously unassessed 237?

### 2.6 Assessment Batch Plan

**C8 (Data Engineering Expert):**

Divide 292 candidates into 20 batches of ~15, stratified by:
- **Theory**: Each batch has mixed theories (not all-MFT)
- **Info tier**: Each batch has mix of A/B/C
- **Year**: Each batch spans publication years

**Execution in 4 waves:**

| Wave | Batches | Candidates | Calibration Gate |
|------|---------|-----------|-----------------|
| 1 | 1–5 | ~75 | C12 runs anchor comparison + drift check |
| 2 | 6–10 | ~75 | C12 runs mid-point calibration |
| 3 | 11–15 | ~75 | C12 runs drift check |
| 4 | 16–20 | ~67 | C12 runs final calibration + completeness audit |
| Mop-up | — | flagged | Sequential review of >20% null or outlier candidates |

**Calibration anchors** (3 benchmarks scored by every batch for consistency):
1. **High anchor**: Moral Machine Experiment (2018) — consistently top-ranked
2. **Mid anchor**: Value Kaleidoscope (2024) — mid-composite
3. **Low anchor**: A Tier C candidate with minimal information — tests null policy consistency

### 2.7 Feature Scoring Guide for Batch Agents

Each batch agent scores 158 features per candidate. To maintain consistency, the following decision rules apply:

**Tier A (Psychological Depth):**
- A1 (theories engaged): Count only theories with substantive engagement (≥3 items or explicit hypothesis testing), not passing mentions
- A2 (operationalization): Distinguish validated→theory-derived→theory-inspired→keyword-only; the modal case is "theory-inspired" (score 40)
- A4 (source instrument): Only credit validated instruments with published psychometric properties (MFQ, DIT, PVQ-RR, etc.)
- A5 (human baselines): "Paper-specific" (70) requires an actual human comparison sample, not just citing human norms from the source instrument
- A6 (construct validity): Level 3 ("adapts without revalidation") is the default for papers that take a human instrument and administer it to LLMs

**Tier B (Practical Ease):**
- B3 (data availability): Check actual current availability (HuggingFace, GitHub), not just claimed availability in the paper
- B6 (harness compatibility): Default 40 (custom implementation) unless evidence of lm-eval-harness or Inspect AI integration

**Tier C (Citation Impact):**
- C1/C2: Use Semantic Scholar data where available; for candidates without DOI/arXiv ID, score C1=10, C2=10 (not null — absence of indexing is informative)
- C3 (venue tier): Apply the venue tier table from supp-methods.md consistently

**Tiers D–G (Extended):**
- Score from available evidence only
- Default to 0 (not null) for features that test specific capabilities the benchmark paper does not discuss (e.g., E12 adversarial robustness = 0 if not tested)
- Use null ONLY for D9 (LLM ceiling compression) and D20 (response entropy) where empirical data is genuinely unavailable

---

## 3. Output Specifications

### 3.1 Per-Batch Output

File: `MORAL-PSYCH/ASSESSMENT/20260405-batch-{NN}.json`

```json
{
  "batch_id": 1,
  "wave": 1,
  "candidates_assessed": 15,
  "anchor_scores": {
    "moral_machine": {"PD": 75.5, "PE": 74.0, "CI": 92.5, "COMPOSITE": 78.45},
    "value_kaleidoscope": {"PD": 55.5, "PE": 69.5, "CI": 65.0, "COMPOSITE": 61.6},
    "low_anchor": {"PD": ..., "PE": ..., "CI": ..., "COMPOSITE": ...}
  },
  "assessments": [
    {
      "file": "YYYY-Author-Title.md",
      "scores": {
        "A1": {"score": 30, "confidence": "high", "evidence": "Engages 1 theory (MFT)"},
        ...
      }
    }
  ]
}
```

### 3.2 Final Matrix Output

File: `MORAL-PSYCH/20260405-full-292-feature-matrix.json`

### 3.3 Tier Assignment Output

File: `MORAL-PSYCH/ANALYSIS/20260405-tier-assignment.json`

### 3.4 Impact Analysis Output

File: `MORAL-PSYCH/METHODS/20260405f-downward-impact-analysis.md`

---

## 4. Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Scoring drift between batches | 3 calibration anchors scored by every batch; C12 runs inter-batch comparison after each wave |
| Information-poor candidates dominate "low" tier | Info tier A/B/C reported alongside quality tier; null-rate exclusion at 60% prevents unscoreable candidates from distorting distribution |
| Composite formula change breaks comparability | Formula kept identical to v2; extended features reported as profiles only |
| Jenks produces unintuitive boundaries | Cross-validate with kernel density; council reserves right to adjust ±5 points |
| Paper updates introduce inconsistencies | C11 maintains a cross-reference table of every number, table, and figure that changes |

---

*Approved by council consensus, 2026-04-05*
*Filed: CEI-Lit-WS/MORAL-PSYCH/METHODS/*
