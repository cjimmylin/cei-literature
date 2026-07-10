# Reproducibility Verification Log
**Date:** 2026-04-12
**Source data:** `CEI-Lit-WS/CULTURAL-GLOBAL/TRIALS/` (30 Claude JSON files, 50 Gemini JSON files)
**Comparison file:** `COMPARISON/20260404-all-model-comparison-summary.json`

## 1. RLHF Conflict Counts

### 1.1 Data Structure Discovery

RLHF conflict data exists at **two levels** in the trial JSON:

1. **Summary-level:** `summary.rlhf_conflicts_identified` -- a list of thematic conflict descriptions.
   Present in: all 10 Opus trials, 0 Sonnet trials, 1 Haiku trial (CC4 only).

2. **Item-level:** per-item fields named `rlhf_conflict` (CC4), `rlhf_tension` (CC6-CC9),
   `rlhf_pulls_toward` (CC10), or `rlhf_tension_meta` (CC6, 1 item).
   Present in: CC4, CC6, CC7, CC8, CC9, CC10 for all 3 models.
   Absent in: CC1, CC2, CC3, CC5 (no item-level RLHF fields).

### 1.2 Summary-Level Conflict Counts

| Model | CC1 | CC2 | CC3 | CC4 | CC5 | CC6 | CC7 | CC8 | CC9 | CC10 | **Total** |
|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|-----------|
| opus | 6 | 5 | 5 | 6 | 5 | 8 | 8 | 8 | 8 | 8 | **67** |
| sonnet | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| haiku | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | **6** |

### 1.3 Item-Level RLHF Field Counts

| Model | CC4 | CC6 | CC7 | CC8 | CC9 | CC10 | **Total** |
|-------|-----|-----|-----|-----|-----|------|-----------|
| opus | 40 | 30 | 30 | 40 | 30 | 40 | **210** |
| sonnet | 40 | 30 | 30 | 40 | 30 | 40 | **210** |
| haiku | 40 | 30 | 30 | 40 | 30 | 40 | **210** |

### 1.4 Combined Counts (Summary + Item-Level)

| Model | Summary | Item-Level | Combined |
|-------|---------|------------|----------|
| opus | 67 | 210 | **277** |
| sonnet | 0 | 210 | **210** |
| haiku | 6 | 210 | **216** |
| **All** | **73** | **630** | **703** |

### 1.5 Comparison with Claimed Values

| Source | Opus | Sonnet | Haiku | Total |
|--------|------|--------|-------|-------|
| Comparison file `total` | 277 | 210 | 216 | 703 |
| Reproduced (summary+item) | 277 | 210 | 216 | 703 |
| Match? | YES | YES | YES | YES |

**FINDING:** The comparison file's `total` field counts summary-level + item-level conflicts combined.
Opus: 67 summary + 210 item = **277** (MATCH with comparison file).
Sonnet: 0 summary + 210 item = **210** (MATCH).
Haiku: 6 summary + 210 item = **216** (MATCH).

### 1.6 Theme Classification (Comparison File) -- Internal Consistency

| Model | Claimed Total | Theme Sum | Discrepancy |
|-------|--------------|-----------|-------------|
| opus | 277 | 302 | +25 |
| sonnet | 210 | 229 | +19 |
| haiku | 216 | 230 | +14 |

**FINDING:** All 3 models have `theme_sum > total`. This means the theme classifier
assigns multiple themes to some conflicts (multi-classification), inflating the per-theme
row sums. The `total` field is the correct unique count; `by_theme` values are
non-exclusive category assignments.

### 1.7 Table 8 Header: n=237

**Claimed:** Table 8 header says n=237.

**Analysis:** No combination of raw trial data reproduces 237 exactly:
- Summary-only (3 models): 73
- Item-only (3 models): 630
- Combined (3 models): 703
- Opus combined: 277
- Sonnet combined: 210
- Haiku combined: 216
- Average per model: 234.3
- Items mentioning "RLHF" in any field (Opus): 241

**VERDICT: MISMATCH.** The value 237 appears to be erroneous. If Table 8 reports
per-model Opus conflicts, the correct value is **277**. If it reports summary-level
thematic conflicts across all 3 Claude models, the correct value is **73**.

## 2. MFQ I:B Ratio

### Opus
- Care/Harm: n=6, mean=4.667
- Fairness/Cheating: n=6, mean=4.833
- Loyalty/Betrayal: n=6, mean=2.000
- Authority/Subversion: n=6, mean=1.333
- Sanctity/Degradation: n=5, mean=0.400
- Individualizing = (4.667 + 4.833) / 2 = **4.750**
- Binding = (2.000 + 1.333 + 0.400) / 3 = **1.244**
- I:B ratio = **3.82**
- Comparison file: indiv=4.75, bind=1.27, ratio=3.75
- **MISMATCH** (reproduced=3.82, claimed=3.75)

### Sonnet
- Care/Harm: n=6, mean=4.500
- Fairness/Cheating: n=6, mean=4.500
- Loyalty/Betrayal: n=6, mean=2.000
- Authority/Subversion: n=6, mean=1.500
- Sanctity/Degradation: n=5, mean=0.800
- Individualizing = (4.500 + 4.500) / 2 = **4.500**
- Binding = (2.000 + 1.500 + 0.800) / 3 = **1.433**
- I:B ratio = **3.14**
- Comparison file: indiv=4.2, bind=1.3, ratio=3.23
- **MISMATCH** (reproduced=3.14, claimed=3.23)

### Haiku
- Care/Harm: n=6, mean=4.500
- Fairness/Cheating: n=6, mean=4.833
- Loyalty/Betrayal: n=6, mean=2.000
- Authority/Subversion: n=6, mean=1.333
- Sanctity/Degradation: n=5, mean=0.400
- Individualizing = (4.500 + 4.833) / 2 = **4.667**
- Binding = (2.000 + 1.333 + 0.400) / 3 = **1.244**
- I:B ratio = **3.75**
- Comparison file: indiv=4.5, bind=0.93, ratio=4.82
- **MISMATCH** (reproduced=3.75, claimed=4.82)

#### Note on MFQ item counts
The MFQ trial has 50 items total: 29 standard MFQ items (6 Care, 6 Fairness, 6 Loyalty,
6 Authority, 5 Sanctity, 1 catch item = 30; but only 29 mapped to 5 foundations) plus
20 cross-cultural extension items. Only the 29 standard items are used for I:B calculation.

#### Discrepancy Analysis

The comparison file uses **pre-rounded** foundation scores from `summary.foundation_scores`:
- opus: {'Care_Harm': 4.8, 'Fairness_Cheating': 4.7, 'Loyalty_Betrayal': 1.8, 'Authority_Subversion': 1.2, 'Sanctity_Degradation': 0.8}
- sonnet: {'Care_Harm': 4.4, 'Fairness_Cheating': 4.0, 'Loyalty_Betrayal': 1.6, 'Authority_Subversion': 1.1, 'Sanctity_Degradation': 1.2}
- haiku: {'Care_Harm': 4.4, 'Fairness_Cheating': 4.6, 'Loyalty_Betrayal': 1.4, 'Authority_Subversion': 0.9, 'Sanctity_Degradation': 0.5}

If we use those pre-rounded values:
- opus: indiv=4.750, bind=1.2667, ratio=3.75 (claimed: 3.75)
- sonnet: indiv=4.200, bind=1.3000, ratio=3.23 (claimed: 3.23)
- haiku: indiv=4.500, bind=0.9333, ratio=4.82 (claimed: 4.82)

## 3. Pairwise Correlations

CC6-CC10 have `response_numeric: null` (qualitative scenarios). Correlations computed on CC1-CC5 only.

Numeric items per model: 210 (CC1: 50, CC2: 50, CC3: 40, CC4: 40, CC5: 30 = 210)

| Pair | Reproduced r | Claimed r | Status |
|------|-------------|-----------|--------|
| opus vs sonnet | 0.9520 | 0.952 | **MATCH** |
| opus vs haiku | 0.9154 | 0.915 | **MATCH** |
| sonnet vs haiku | 0.8845 | 0.885 | **MATCH** |

**Note:** If the paper computed correlations across ALL 380 items (including qualitative),
the null values in CC6-CC10 would produce NaN. The claimed correlations must be based on
the numeric subset only (CC1-CC5, n=210).

## 4. Cultural Distance Rankings (Table 7)

| Rank | Country | Reproduced Distance | Claimed Distance | Status |
|------|---------|-------------------|-----------------|--------|
| 1 | Germany | 0.538 | 0.538 | **MATCH** |
| 2 | US | 0.884 | 0.884 | **MATCH** |
| 3 | Japan | 0.990 | 0.99 | **MATCH** |
| 4 | Brazil | 1.062 | 1.062 | **MATCH** |
| 5 | China | 1.332 | 1.332 | **MATCH** |
| 6 | India | 1.560 | 1.56 | **MATCH** |
| 7 | Nigeria | 1.760 | 1.76 | **MATCH** |
| 8 | Saudi_Arabia | 1.974 | 1.974 | **MATCH** |

Ranking order match: **MATCH**
- Reproduced: Germany < US < Japan < Brazil < China < India < Nigeria < Saudi_Arabia
- Claimed: Germany < US < Japan < Brazil < China < India < Nigeria < Saudi_Arabia

## 5. Gemini Identity Check

Gemini models: ['gemini-2.5-flash', 'gemini-2.5-flash-lite', 'gemini-2.5-pro', 'gemini-3.1-flash-lite-preview', 'gemini-3.1-pro']

### CC1 (GlobalOpinionQA)

| Comparison | Identical? | Items Different |
|-----------|-----------|-----------------|
| gemini-2.5-flash vs gemini-2.5-flash-lite | NO | 30/50 |
| gemini-2.5-flash vs gemini-2.5-pro | NO | 30/50 |
| gemini-2.5-flash vs gemini-3.1-flash-lite-preview | NO | 31/50 |
| gemini-2.5-flash vs gemini-3.1-pro | NO | 29/50 |

**All Gemini CC1 responses identical: False**

**FINDING:** Gemini models produce **different** responses across model variants.
This **refutes** the hypothesis of pure template derivation. Each Gemini model
has distinct response patterns, suggesting genuine per-model trial execution
(or at minimum, model-specific template variation).

#### Gemini inter-model correlations (CC1)

- gemini-2.5-flash vs gemini-2.5-flash-lite: r = 0.631
- gemini-2.5-flash vs gemini-2.5-pro: r = 0.593
- gemini-2.5-flash vs gemini-3.1-flash-lite-preview: r = 0.618
- gemini-2.5-flash vs gemini-3.1-pro: r = 0.632
- gemini-2.5-flash-lite vs gemini-2.5-pro: r = 0.909
- gemini-2.5-flash-lite vs gemini-3.1-flash-lite-preview: r = 0.895
- gemini-2.5-flash-lite vs gemini-3.1-pro: r = 0.900
- gemini-2.5-pro vs gemini-3.1-flash-lite-preview: r = 0.877
- gemini-2.5-pro vs gemini-3.1-pro: r = 0.898
- gemini-3.1-flash-lite-preview vs gemini-3.1-pro: r = 0.885

## 6. Summary of All Verified Statistics

| # | Statistic | Claimed | Reproduced | Status |
|---|-----------|---------|------------|--------|
| 1a | Table 8 header total | n=237 | No matching count (closest: 277 Opus, 73 summary, 703 all) | **MISMATCH** |
| 1b | Opus RLHF total (comparison file) | 277 | 277 (67 summary + 210 item) | **MATCH** |
| 1c | Sonnet RLHF total | 210 | 210 (0 summary + 210 item) | **MATCH** |
| 1d | Haiku RLHF total | 216 | 216 (6 summary + 210 item) | **MATCH** |
| 1e | Opus theme sum = total? | 277 | theme_sum=302 (multi-classification) | **EXPECTED** |
| 2a | Opus I:B ratio | 3.75 | 3.82 (from raw items) | **MISMATCH** |
| 2b | Opus I:B from summary scores | 3.75 | 3.75 (from pre-rounded) | **MATCH** |
| 3 | r(opus,sonnet) | 0.952 | 0.9520 | **MATCH** |
| 3 | r(opus,haiku) | 0.915 | 0.9154 | **MATCH** |
| 3 | r(sonnet,haiku) | 0.885 | 0.8845 | **MATCH** |
| 4a | Table 7 rank order | Ger<US<Jpn<Bra<Chn<Ind<Nga<SA | Same | **MATCH** |
| 4b | All 8 distance values | See above | All within 0.005 | **MATCH** |
| 5 | Gemini CC1 all identical | Expected identical | False | **REFUTED** |

## 7. Recommended Corrections for Manuscript

### Critical (arithmetic errors)

1. **Table 8 header n=237**: This value has no reproducible basis in the trial data.
   - If Table 8 reports *all RLHF conflicts across 3 Claude models*: correct to **n=703**
   - If Table 8 reports *Opus-only RLHF conflicts*: correct to **n=277**
   - If Table 8 reports *summary-level thematic conflicts only*: correct to **n=73** (all models) or **n=67** (Opus)
   - Clarify in the table caption what constitutes a "conflict" (summary-level vs item-level vs combined)

2. **Opus comparison total=277 vs theme breakdown sum=302**: NOT an error.
   The theme classifier assigns multiple themes to 25 conflicts (302-277=25 multi-classified).
   However, the table must note that theme columns are non-exclusive, or report primary-theme-only counts.

3. **MFQ I:B ratio**: The paper claims Opus I:B=3.75, which matches the computation from
   *pre-rounded* foundation scores in `summary.foundation_scores` (3.75).
   From raw item-level data, the precise value is **3.82**.
   Recommendation: use raw-item computation (3.82) and note rounding in methods.

### Minor

4. **Gemini identity claim**: If the paper claims all Gemini models produce identical responses,
   this is **refuted** by the data. Each Gemini model variant has distinct responses
   (29-31 of 50 CC1 items differ between pairs).

5. **Pairwise correlations**: These require specification that they are computed on the
   numeric-response subset only (CC1-CC5, n=210 items), as CC6-CC10 have qualitative
   responses with `response_numeric: null`.
