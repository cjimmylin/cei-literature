# Methods: Moral Psychology Benchmark Selection for LLM Values Alignment

**Date:** 2026-04-03
**Project:** MORAL-PSYCH

## Overview

This document describes the methodology for identifying, characterizing, and ranking moral psychology benchmarks for LLM values alignment evaluation.

## Phase 1: Candidate Extraction

### Multi-Signal Detection

Papers were extracted from a vault of 2,046 AI ethics papers using 5 signals:

1. **mp_* scores >= 50** — Papers scored >= 50 on any of 8 moral psychology fields by the vault's keyword scorer (`moral_psych_scoring.py`)
2. **Benchmark/eval/dataset + keyword match** — Papers tagged is_benchmark/is_eval/is_dataset with >= 2 moral psychology keyword matches in abstract/key_contribution
3. **DATA_URL + strong keyword match** — Papers with accessible data and >= 3 keyword matches
4. **Very strong keyword match** — >= 5 keyword matches regardless of other signals
5. **Known benchmark names** — Title/abstract containing known benchmark names (ETHICS, MoralBench, ValueBench, Scruples, Delphi, MACHIAVELLI, etc.)

### Keyword Taxonomy

65 regex patterns covering:
- 8 moral psychology theories (MFT, Schwartz, Trolley, Kohlberg, Dual Process, Social Intuitionist, Dyadic, Moral Identity)
- Psychometric instrument names (MFQ, PVQ, DIT, MFV)
- General moral psychology terms (moral judgment, moral reasoning, moral cognition)
- Values alignment terms
- Specific benchmark names

### Result

222 candidates extracted: 177 benchmarks, 43 datasets, 2 other.

**Critical finding:** The keyword scorer (mp_*) missed major benchmarks like ValueBench (44 psychometric instruments, mp_schwartz=0) and ETHICS (Hendrycks, mp_mft=0). Multi-signal detection was essential.

## Phase 2: Expert Council Assessment

### Council Composition

9 virtual expert perspectives assessed the top 40 candidates (by mp_max + keyword_count):

1. MFT Specialist — theory fidelity
2. Developmental Psychologist — Kohlberg stage validity
3. Psychometrician — construct validity, source instruments
4. NLP Evaluator — harness compatibility, scorer types
5. Cross-Cultural Psychologist — WEIRD bias, multilingual coverage
6. AI Safety Researcher — deployment relevance
7. Bibliometrician — citation impact, venue tiers
8. Data Engineer — reproducibility, data access
9. Survey Methodologist — search protocol rigor

### Assessment Process

Three parallel assessment agents:
- **Agent 1 (Depth):** Read PDF extracts for 40 papers. Assessed A2 (operationalization), A4 (source instrument), A5 (human baseline), A6 (construct validity), A7 (cultural provenance), A8 (languages), B1 (format), B2 (size), B10 (LLM fidelity), theories verified.
- **Agent 2 (Impact):** Cross-referenced with implementability CSV. Assessed safety relevance, B6-B9 (harness tiers, scorer type, model compatibility), C3 (venue tier), C5 (hub presence).
- **Agent 3 (Secondary):** Scanned candidates 41-80 for hidden gems and underrepresented theories.

### Citation Data

Semantic Scholar API queried for top 80 candidates. 54/80 found. 10 had no DOI or arXiv ID.

## Phase 3: Composite Scoring

### Feature Normalization

All features normalized to 0-100 scale:

| Feature | Normalization |
|---------|--------------|
| A2 (operationalization) | {1:10, 2:40, 3:70, 4:100} |
| A6 (construct validity) | {1:10, 2:30, 3:50, 4:75, 5:100} |
| A1 (theories) | {0:0, 1:30, 2:60, 3:80, 4+:100} |
| A5 (human baseline) | {Published:100, Paper:70, Partial:40, No:0} |
| B1 (format) | MCQ=100, Binary=90, Forced-choice=85, Likert=70, ... |
| B2 (size) | Log-scaled: <50=20, 200=40, 1K=60, 5K=75, 20K=85, >20K=100 |
| B3 (data) | HuggingFace=100, GitHub=95, OSF=90, Anonymous=60 |
| C1 (citations) | Log-scaled: <5=10, 20=30, 50=50, 100=65, 200=75, 500=85, >500=100 |
| C2 (rate) | Citations/year: <2=15, 5=30, 10=50, 25=65, 50=80, 100=90, >100=100 |

### Composite Formula

```
PD = A2×0.25 + A6×0.20 + A1×0.15 + A5×0.15 + A3×0.15 + A4×0.10
PE = B3×0.20 + B2×0.15 + B6×0.15 + B7×0.15 + B1×0.10 + B4×0.10 + B10×0.15
CI = C1×0.30 + C2×0.30 + C3×0.25 + C5×0.15
COMPOSITE = PD × 0.50 + PE × 0.30 + CI × 0.20
```

### Selection Algorithm

1. **Hard gates:** PD >= 40 AND data publicly available (38 of 40 passed)
2. **Dedup:** Removed 2 duplicate entries (TrolleyBench, Khandelwal DIT)
3. **Theory caps:** Max 3 Trolley, max 4 MFT (prevents over-representation)
4. **Greedy selection:** Top papers by composite, respecting caps
5. **Diversity fills:** Swap in lower-ranked papers to meet: >= 2 Schwartz, >= 1 Kohlberg, >= 1 minority theory (identity/dyadic/intuitionist/dual_process)

## Limitations

1. **Assessment depth limited to top 40:** The 40 papers assessed by the council represent a subset of the 222 candidates. Papers ranked 41-222 may contain hidden gems, particularly for underrepresented theories.
2. **No Semantic Scholar data for 26 papers:** Papers without DOIs or arXiv IDs could not be citation-checked.
3. **Keyword scorer blind spots:** The vault's mp_* scorer uses keyword matching, which missed ValueBench (A6=psychometric), ETHICS (Hendrycks), and potentially other benchmarks that use general terminology.
4. **Minority theory gap is genuine:** The absence of Dual Process, Social Intuitionist, and Dyadic Morality benchmarks appears to reflect a real research gap, not a search failure.
5. **Paper #15 is weak:** The Schwartz diversity minimum forced inclusion of a low-composite paper. A dedicated Schwartz PVQ-40 benchmark for LLMs would be a stronger entry.

## Reproducibility

All scripts and data files are in `CEI-Lit-WS/MORAL-PSYCH/`:
- `extract_candidates.py` — Multi-signal candidate extraction
- `build_feature_matrix.py` — Feature matrix construction and composite scoring
- `20260403-moral-psych-benchmark-candidates.json` — Raw candidate data
- `20260403-council-depth-assessment.json` — Expert depth assessments
- `20260403-council-impact-assessment.json` — Expert impact assessments
- `20260403-citation-counts.json` — Semantic Scholar citation data
- `20260403-moral-psych-benchmark-feature-matrix.json` — Unified feature matrix
- `20260403-moral-psych-top15-selection.json` — Final selection with metadata
