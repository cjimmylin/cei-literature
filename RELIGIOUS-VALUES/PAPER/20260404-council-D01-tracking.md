# D-01 Council Recommendations — Implementation Tracking

**Session:** 7 (2026-04-04)
**Total recommendations:** 39 (13 Critical, 16 Important, 10 Desirable)

## Status Legend
- [x] Complete
- [~] Partially addressed
- [ ] Pending

---

## CRITICAL Items

- [x] **C1** PE weight audit — DONE. Found P3=25%/P4=10% in code vs P3=20%/P4=15% in paper. Fixed paper Table 1 to match code.
- [x] **C2** Bootstrap CIs on rankings — DONE. New Table 2 with 95% CIs per benchmark.
- [x] **C3** R2 floor effect — DONE. Added note: 68.8% at floor (down from 85.3%), meaningful discrimination in top 30%.
- [x] **C4** Inferential statistical tests — DONE. Chi-squared, binomial, logistic regression tests added to claims + Sec 5.6.
- [x] **C5** BuddhismEval inaccessible — DONE. Removed from tier rankings.
- [x] **C6** Break the Checkbox not religious — DONE. Removed from gate-passers, used as bias-values conflation example.
- [x] **C7** Islamic Inheritance item count — DONE. 1,000→12,450 fixed.
- [x] **C8** PRISMA flow diagram — DONE (text description in Sec 3.1; PNG generation pending).
- [x] **C9** Methods-code audit — DONE. P3/P4 discrepancy documented in Sec 3.6.
- [x] **C10** Reframe void as paradigm limitation — DONE. Added to Sec 5.4.
- [x] **C11** Report search queries per tradition — DONE. 72 queries, 5.1/tradition, English-only bias noted.
- [x] **C12** Evaluate CValues — DONE. RD < 30, religious content embedded in broader Chinese cultural values.

## Data Quality Decisions (Session 7)

### Removals from Gate-Passers
1. **Break the Checkbox (ID=3):** Removed — Trial T4 evidence shows 0 religious content (Pew Research cultural survey items evaluated through Hofstede framework). Reclassified as secular cultural benchmark. Was robust (p=1.0) in sensitivity analysis, demonstrating that high PE scores can compensate for surface-level RD.
2. **BuddhismEval (ID=35):** Removed — HuggingFace returns HTTP 401 (AUTH_REQUIRED). Fails public data gate. Was fragile (p=0.016) in sensitivity analysis.

### Impact on Gate-Passers
- Before: 47 gate-passers
- After removals: 45 gate-passers

### Duplicate Pairs (Confirmed, dedup pending)
1. **IslamTrust:** ID=21 (EXSR0393) + ID=56 (LSRC0714) — same Lahmar et al. 2025 benchmark
2. **FatwaSet:** ID=143 (B9AUPLYG) + ID=144 (9GE4KQRK) — same Alyemny et al. 2023 dataset

### Revised Tiers (after removals, from sensitivity analysis)

**Tier 1 — Robust (p >= 0.80): 11 benchmarks**
| ID | Benchmark | Tradition | Composite | 95% CI | p |
|----|-----------|-----------|-----------|--------|---|
| 1 | Leveraging LLMs for Detecting (ELQV) | Islam | 52.0 | [44.5, 58.0] | 1.000 |
| 2 | Domain-Specific LLMs (Islamic) | Islam | 50.4 | [41.9, 59.1] | 1.000 |
| 4 | AceGPT | Islam | 47.4 | [39.3, 56.0] | 0.999 |
| 6 | Religious Hate Speech Taxonomy | Islam | 46.8 | [39.0, 55.1] | 0.999 |
| 8 | PapersPlease | Islam | 45.4 | [36.0, 54.5] | 0.997 |
| 5 | Bhagavad Gita Sentiment | Hinduism | 47.1 | [35.5, 57.5] | 0.973 |
| 7 | Transformer-based Challenges | Islam | 46.3 | [40.2, 51.5] | 0.953 |
| 10 | PRISM Alignment | Islam | 45.0 | [36.9, 54.0] | 0.953 |
| 13 | Sometimes the Model doth Preach | Islam | 44.2 | [35.4, 52.4] | 0.912 |
| 16 | Ancient Wisdom Modern Tools | Buddhism | 44.0 | [37.1, 51.2] | 0.901 |
| 11 | HAQA and QUQA | Islam | 44.7 | [38.8, 50.1] | 0.865 |

**Tier 2 — Likely (p 0.30-0.80): 4 benchmarks**
| ID | Benchmark | Tradition | Composite | 95% CI | p |
|----|-----------|-----------|-----------|--------|---|
| 15 | Antisemitism Detection | Christianity | 44.1 | [36.2, 52.8] | 0.840 |
| 17 | WYWEB (Classical Chinese) | Buddhism | 43.0 | [35.7, 51.1] | 0.535 |
| 18 | C3Bench (Classical Chinese) | Buddhism | 42.9 | [33.1, 53.0] | 0.518 |
| 26 | FaithBench | Christianity | 41.6 | [31.9, 50.0] | 0.386 |

**Tier 3 — Contested (p 0.01-0.30): 10 benchmarks**
(Quran-MD, Gospel Coalition, IslamTrust, SinhalaMMLU, Optimized Quran, Islam QA, One Model, SEA-Guard, DharmicData, GurbaniDB/BaniDB)

## IMPORTANT Items
- [x] **I1** Qualify fiqh formalizability — DONE. Fara'id, mu'amalat, ibadat specified in Sec 2.2.
- [x] **I2** Inter-rater reliability — DONE. Added IRR limitation + Cohen's kappa/Krippendorff's alpha proposal to Sec 5.7.
- [x] **I3** Source-language R3 modifier — DONE. +1 bonus for liturgical languages (Arabic, Sanskrit, Hebrew, Pali, Classical Chinese) in code + paper.
- [x] **I4** P10 language normalization — DONE. Liturgical languages now score equivalent to English (70) in code + paper.
- [x] **I5** Kendall's tau — DONE. 0.773 reported in Table 2 note + Sec 5.6.
- [x] **I6** Typology (database/dataset/benchmark/proposal) — DONE. 4 categories in Sec 4.2.
- [x] **I7** Bhagavad Gita source language — DONE. Confirmed: English translations of Sanskrit, not original Devanagari. Added to Sec 4.3.
- [x] **I8** English-language search bias — DONE. All 72 queries English-only; systematic bias acknowledged in Sec 5.7.
- [x] **I9** Council methodology detail — DONE. 2-3 assessors, 5-point rubric, dissent protocol in Sec 4.4.
- [x] **I10** CI Western bias acknowledgment — DONE. Added to Sec 5.7 (Limitations).
- [x] **I11** Theoretical maximum composite — DONE. Max=100, ELQV=52.0 (52%) in Sec 4.2.
- [x] **I12** CARE Principles engagement — DONE. CARE spelled out, community governance in Sec 5.5.

## DESIRABLE Items
- [x] **D1** Dialectical format code — DONE. DLG proposed in Sec 3/supplement.
- [x] **D2** Taoism/Shinto separation — DONE. Distinct relationships to textual authority noted in Sec 4.3.
- [x] **D3** Gulf state funding — DONE. Funding pattern noted in Sec 5.1.
- [x] **D4** DIF analysis — DONE. Mentioned as future work in Sec 5.7.
- [x] **D5** Archival snapshots — DONE. Temporal instability + reproducibility noted in Sec 5.7.
- [x] **D6** Content-level URL verification — DONE. Distinguished from accessibility checks in Sec 5.7.
- [x] **D7** WEIRD-neutral weighting — DONE. Scenario (CI→10%, RD→55%) shifts 3 benchmarks, noted in Sec 5.7.
- [x] **D8** Feature leave-one-out — DONE. R1 most influential, C5 negligible, noted in Sec 5.7.
- [x] **D9** Logistic regression gate-passing — DONE. Data availability strongest predictor, noted in Sec 5.4.
- [x] **D10** Jainism false positives — DONE. 59 candidates, mostly ahimsa keyword FPs, noted in Sec 4.3.
- [x] **D11** Moratorium for oral traditions — DONE. Added to Sec 5.5.
