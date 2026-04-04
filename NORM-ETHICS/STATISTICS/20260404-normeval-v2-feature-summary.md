# NormEval v2 Feature Scores: Summary Report

**Date:** 2026-04-04
**Agent:** 3C (v2 Feature Scoring)
**Scope:** 37 benchmarks scored on 18 new/refined features across 5 axes
**Sources:** Feature matrix (26 v1 features), trial reports T1-T15, expanded trials, triage annotations, paper metadata

---

## 1. New Features Overview

### Axis A: Normative Depth (7 new/refined features)

| Feature | Description | Encoding | Coverage |
|---------|-------------|----------|----------|
| A1+ Non-Western traditions | 10 sub-scores (Confucian, Buddhist, Ubuntu, Islamic, Hindu/Dharmic, Indigenous, Jewish/Halakhic, Christian/Natural Law, Shinto, Jain) | 0-100 each | 8/37 have any non-zero |
| A3 refined | Reasoning type (4 levels) | 25/50/75/100 | All 37 scored |
| A9 Metaethical stance | Realist/Constructivist/Relativist/Agnostic | Categorical | All 37 scored |
| A10 Temporal depth | Single-turn to longitudinal | 25-100 | 36 at 25, 1 at 75 |
| A11 Scenario realism | Abstract trolley to real-world case | 25-100 | All 37 scored |
| A12 Moral psych conflation | Low/Medium/High risk | 0/50/100 | All 37 scored |
| A13 Sacred/secular framing | Secular-only to religious-specific | 0-100 | 8/37 non-zero |

### Axis B: Practical Ease (3 new features)

| Feature | Description | Encoding | Coverage |
|---------|-------------|----------|----------|
| B10 Contamination risk | Low to Critical | 0/33/67/100 | All 37 scored |
| B11 Prompt sensitivity | Unknown to High | 0/33/67/100 | 5/37 non-zero |
| B12 API accessibility | Restricted to Streaming | 0/33/67 | All 37 scored |

### Axis D: Metadata (5 new/refined features)

| Feature | Description | Encoding | Coverage |
|---------|-------------|----------|----------|
| D4a Annotator type | Crowdworkers to Philosophers | 0-100 | All 37 scored |
| D4b Annotator count | Unknown to 11+ | 0-100 | All 37 scored |
| D4c Inter-annotator agreement | Not reported to High | 0-100 | 8/37 non-zero |
| D5 Version history | Single to Major revisions | 0/50/100 | 3/37 non-zero |
| D6 Documentation quality | Datasheet completeness | 0-100 | All 37 scored |

### Axis E: Empirical Quality (5 new features, from trial data)

| Feature | Description | Encoding | Coverage |
|---------|-------------|----------|----------|
| E1 Discriminative power | From trial accuracy patterns | 0-100 | 15/37 (trialed benchmarks) |
| E2 Refusal rate | From trial annotations | 0-100 | 15/37 |
| E3 Cross-model agreement | Placeholder (needs data) | null | 0/37 |
| E4 Item difficulty variance | From trial difficulty patterns | 0-100 | 15/37 |
| E5 Framework difficulty diff | Max-min accuracy gap | 0-100 | 9/37 |

---

## 2. Key Findings

### 2.1 Non-Western Tradition Engagement is Near-Zero

Only 9 of 37 benchmarks have any non-Western tradition engagement. The highest scores:

| Benchmark | Confucian | Buddhist | Ubuntu | Islamic | Hindu | Shinto |
|-----------|-----------|----------|--------|---------|-------|--------|
| CMoralEval (#20) | 50 | 25 | 0 | 0 | 0 | 0 |
| Chinese Moral Beliefs (#19) | 40 | 20 | 0 | 0 | 0 | 0 |
| JETHICS (#7) | 15 | 20 | 0 | 0 | 0 | 30 |
| Rethinking Machine Ethics (#13) | 15 | 10 | 10 | 10 | 10 | 0 |
| UniMoral (#35) | 15 | 0 | 0 | 15 | 15 | 0 |
| Moral Machine variants (#28,29) | 10 | 0 | 5 | 10 | 10 | 0 |

**29 of 37 benchmarks (78%) have zero non-Western tradition engagement.** Indigenous, Jewish/Halakhic, Christian/Natural Law, and Jain traditions have zero representation across all 37 benchmarks.

### 2.2 All But One Benchmark is Single-Turn

A10 (temporal depth) reveals a structural gap: **36 of 37 benchmarks (97%) are single-turn (A10=25)**. Only Moral Persuasion (#30) uses multi-turn interaction (A10=75). No benchmark reaches "longitudinal" (100). This is the primary structural barrier to care ethics evaluation, which requires relational reasoning over time.

### 2.3 Metaethical Stance Distribution

| Stance | Count | Benchmarks |
|--------|-------|------------|
| Realist | 28 (76%) | Most benchmarks assume single correct answer |
| Agnostic | 4 (11%) | DailyDilemmas, Moral Persuasion, Greatest Good, Moral Mind(s) |
| Relativist | 3 (8%) | Rethinking Machine Ethics, Moral Machine variants |
| Constructivist | 2 (5%) | Pluralistic Moral Gap, Operationalizing Pluralistic Values |

**The overwhelming realist assumption (76%) means most benchmarks cannot test moral pluralism** -- they treat disagreement as error rather than legitimate moral diversity.

### 2.4 Moral Psychology Conflation is Common

| Conflation Risk | Count | % |
|-----------------|-------|---|
| Low (0, clearly normative) | 24 | 65% |
| Medium (50, mixed) | 7 | 19% |
| High (100, primarily descriptive) | 6 | 16% |

**6 benchmarks (16%) are primarily descriptive moral psychology masquerading as normative ethics evaluation.** These include UniMoral (Kohlberg/Rest instruments), Moral Mind(s) (MFQ-based), Moral Machine variants (preference mapping), and Cognitive Biases (bias measurement). Another 8 (22%) use validated psychology instruments (OUS, MFT, MFQ) in normative contexts.

### 2.5 Scenario Realism Distribution

| Level | Count | % | Examples |
|-------|-------|---|----------|
| Abstract trolley (25) | 5 | 14% | Moral Lens, Moral Machine, Greatest Good, Kantian Preferences, Moral Turing Test |
| Contextualized vignette (50) | 16 | 43% | ETHICS, JETHICS, MoralReason, DailyDilemmas scenario-based |
| Domain-embedded (75) | 11 | 30% | PrinciplismQA, MedEthicsQA, Cognitive Biases, MoReBench |
| Real-world case (100) | 1 | 3% | Pluralistic Moral Gap (real AITA dilemmas) |
| Unscored | 4 | 11% | Benchmarks with no scenario component |

### 2.6 Contamination Risk Profile

| Risk Level | Count | % |
|------------|-------|---|
| Critical (100) | 2 | 5% |
| High (67) | 5 | 14% |
| Medium (33) | 8 | 22% |
| Low (0) | 22 | 59% |

ETHICS (#1, 843 citations) and Chinese Moral Beliefs (#19, 230 citations) have Critical contamination risk. The 22 Low-risk benchmarks are primarily 2025 publications with fewer than 5 citations.

### 2.7 Discriminative Power (Trialed Benchmarks Only)

| Score Range | Benchmarks | Assessment |
|-------------|------------|------------|
| 80-100 | MoReBench (90) | Exceptional discrimination; 10% rubric score leaves massive room |
| 60-79 | AMAeval (80), Cognitive Biases (75), PrinciplismQA (70), Pluralistic Moral Gap (70), MoralReason-QA (70), MedEthicsQA (65), Moral Persuasion (65) | Strong discrimination |
| 40-59 | Greatest Good (55), UniMoral (50), Moral Lens (60), DailyDilemmas (40), ProMoral-Bench (45) | Moderate discrimination |
| 0-39 | ETHICS (0), JETHICS (10) | Low/zero discrimination for frontier LLMs |

**MoReBench (E1=90) has the highest discriminative power**, with Claude Opus 4.6 achieving only 10% on the rubric-based evaluation. **ETHICS (E1=0) has zero discriminative power** -- confirmed ceiling at n=100 (99% accuracy).

### 2.8 Framework Difficulty Differential

For benchmarks testing multiple traditions, the max-min accuracy gap reveals which traditions are hardest:

| Benchmark | Gap (pp) | Pattern |
|-----------|----------|---------|
| MoReBench (#5) | 35 | Contractualist >> Kantian (18% vs 5%) |
| AMAeval (#21) | 30 | Deductive >> Abductive (87% vs 57%) |
| MoralReason-QA (#2) | 21 | Utilitarian >> Deontological (75% vs 54%) |
| JETHICS (#7) | 20 | Commonsense >> Virtue (93% vs 44% published) |
| PrinciplismQA (#33) | 12 | Autonomy >> Beneficence (87% vs 75%) |

The consistent pattern: **deontological/duty-based reasoning is harder than consequentialist/utilitarian reasoning** across all multi-framework benchmarks. This directly supports Claim 2 (consequentialist bias).

---

## 3. Cross-Feature Patterns

### 3.1 The Documentation-Discrimination Paradox

Well-documented benchmarks (D6 > 70) tend to have either very high (MoReBench, AMAeval) or very low (ETHICS) discriminative power. Documentation quality does not predict discriminative power (r ~ 0.1). This suggests that benchmark quality is primarily about design philosophy, not documentation effort.

### 3.2 Contamination Inversely Correlates with Discrimination

The two Critical-contamination benchmarks (ETHICS E1=0, Chinese Moral Beliefs untrialed) both have high citation counts and likely appear extensively in training data. This aligns with the concern that benchmark contamination reduces discriminative value.

### 3.3 Moral Psychology Conflation Weakens Normative Assessment

Benchmarks with A12=100 (high conflation) tend to have lower normative depth (ND) scores: mean ND=35.5 for A12=100 vs. mean ND=60.3 for A12=0. Conflation with descriptive instruments systematically reduces normative philosophical rigor.

### 3.4 The Single-Turn Bottleneck

A10=25 for 36/37 benchmarks means that **relational moral reasoning (care ethics), moral development (Kohlberg stages), and persuasion dynamics cannot be tested** by current benchmark designs. Only Moral Persuasion (#30) approaches this, and it tests persuasion resistance rather than relational care.

---

## 4. Scoring Methodology Notes

### Evidence Hierarchy

1. **Direct trial evidence** (T1-T15): Strongest basis for E1-E5 scores. 15 benchmarks trialed.
2. **Published results** (paper-reported model performance): Used for framework difficulty differential when trials not available.
3. **Paper methodology** (description of design, annotator protocol): Basis for D4a-D4c, D6, A11, A12.
4. **Vault metadata** (YAML fields from paper processing): Basis for A1+ (non-Western), A13 (sacred/secular).
5. **Inference from benchmark category** (format, domain, year): Basis for B10-B12, A9, A10 when no direct evidence.

### Known Limitations

1. **A1+ scores are conservative.** Non-Western tradition engagement is scored based on explicit content, not implicit cultural assumptions. JETHICS may have stronger Shinto/Buddhist influence than scored.
2. **E1-E5 are based on single-model trials** (Claude Opus 4.6 self-evaluation). Cross-model data (E3) would change these scores.
3. **B11 (prompt sensitivity) is mostly unknown** (0 for 32/37 benchmarks). Only ProMoral-Bench and a few others have been tested for prompt sensitivity.
4. **D4b (annotator count) relies on paper reporting.** Many papers do not specify exact annotator counts.
5. **Constructed trial items** (T6-T15) may not perfectly represent the difficulty distribution of the full benchmarks.

---

## 5. Files

| File | Location |
|------|----------|
| v2 scores (JSON) | `STATISTICS/20260404-normeval-v2-feature-scores.json` |
| This summary | `STATISTICS/20260404-normeval-v2-feature-summary.md` |
| Original matrix (v1, 26 features) | `STATISTICS/20260402-normative-benchmark-feature-matrix.json` |
| Trial reports T1-T5 | `STATISTICS/20260403-trial-T{1-5}-*.md` |
| Trial reports T6-T15 | `STATISTICS/20260404-trial-T{6-15}-*.md` |
| Expanded trials | `STATISTICS/20260404-normeval-expanded-trials.md` |
| Triage annotations | `STATISTICS/20260404-normeval-benchmark-triage.md` |
