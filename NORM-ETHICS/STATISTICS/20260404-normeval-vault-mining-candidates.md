# NormEval Vault Mining: Candidate Benchmarks Report

**Date:** 2026-04-04
**Agent:** 1C (Vault Mining)
**Vault size:** 2,043 papers
**Known benchmarks in feature matrix:** 37
**Papers with `normative_ethics_benchmark` field:** 63

## Executive Summary

Systematic mining of the 2,043-paper vault using 6 search strategies identified **45 candidate papers**, of which:
- **12 INCLUDE** -- strong candidates for addition to the feature matrix
- **13 REVIEW** -- need closer reading to determine normative depth
- **20 EXCLUDE** -- not relevant to normative ethics benchmarking

The 12 INCLUDE candidates would expand the feature matrix from 37 to **49 benchmarks** (32% increase). Key findings:
- 7 papers with explicit deontological/utilitarian framework testing (DE>=50 or UE>=50)
- 3 new multilingual/cross-cultural normative benchmarks
- 2 medical ethics benchmarks with normative principle scoring
- 1 critical meta-analysis of the ETHICS benchmark itself

---

## Strategy 1: Audit of 63 `normative_ethics_benchmark` Papers

Of 63 papers with NEB field, 35 are in the matrix. 28 are not (27 Borderline + 1 duplicate Yes).

### INCLUDE from NEB Audit

**1. OffTheRails (Franken 2024)** -- `2024-Franken-OffTheRails Procedural Dilemma Generation for Moral Reasoning.md`
- NEB: Borderline | Ethics: 100 | DE=50, UE=50
- Procedural dilemma generation using causal graphs. Stanford (Gerstenberg lab).
- Explicitly tests deontological vs utilitarian reasoning with generated scenarios.
- GitHub: https://github.com/cicl-stanford/moral-evals
- **Why include:** Strong normative framework engagement, novel methodology, reproducible.

**2. EMNLP Framework (Jiang 2025)** -- `2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling.md`
- NEB: Borderline | Ethics: 95 | VE=50, DE=50, UE=50, CO=50
- 88 teacher-specific moral dilemmas with Kohlberg stages. EMNLP 2025.
- Scores across 4 of 5 normative traditions. DATA_URL available.
- **Why include:** Highest framework breadth of any candidate (4/5 traditions >= 50).

**3. COMETH (Morlat 2025)** -- `2025-Morlat-COMETH Contextual Organization of Moral Evaluation from Textual Human.md`
- NEB: Borderline | Ethics: 100 | DE=15
- 300 scenarios across 6 deontological rules with context modulation.
- Bridges normative theory and empirical moral psychology.
- **Why include:** Tests how context shapes normative rule application.

**4. Ebara Medical Ethics (2025)** -- `2025-Ebara-Corpus-Based Medical Ethics Decision-Making Evaluation.md`
- NEB: Borderline | Ethics: 100 | DE=40
- 50 clinical cases scored on 4 ethical principles (principlism).
- Japanese medical ethics with professional annotations.
- **Why include:** Directly tests normative principle application in clinical settings.

**5. MedES (Jin 2026)** -- `2026-Jin-MedES Chinese Medical Ethics Scenarios.md`
- NEB: Borderline | Ethics: 100
- 260 Chinese medical/ethical/legal sources for clinical scenarios.
- Dynamic benchmark. Chinese-language.
- **Why include:** Normative frameworks embedded in clinical decision scenarios.

**6. Basu Multilingual Moral (2025)** -- `2025-Basu-Measuring Moral LLM Responses in Multilingual Capacities.md`
- NEB: Borderline | Ethics: 65 | DE=50, UE=50
- 6 languages: Arabic, Chinese, English, Hindi, Spanish, Swahili.
- Tests deontological/utilitarian reasoning across resource levels.
- **Why include:** Rare multilingual normative framework coverage.

### EXCLUDE from NEB Audit (14 papers)

| Paper | Reason |
|-------|--------|
| SpeciesismBench (Jotautaite 2025) | Tests speciesism, not normative frameworks. All framework scores ~0. |
| Healthcare QA China (Bian 2025) | Clinical safety compliance, not normative reasoning. Framework scores ~0. |
| JMedEthicBench (Liu 2026) | Japanese medical safety. ethics_overall=0, all frameworks=0. |
| PsychEthicsBench (Shen 2026) | Mental health refusal safety. Zero framework scores. |
| Nunes Conscience Conflict (2024) | Uses MFQ/MFT, not normative traditions. |
| Oh Robustness (2025) | Many Labs 2 replication, not ethics benchmark. |
| Sun Decoding Moral (2025) | News response forecasting via MFT. ethics_overall=35. |
| CLAVE/ValEval (Yao 2024) | General value alignment. ethics_overall=15, frameworks=0. |
| ALI-Agent (Zheng 2024) | Agent-based alignment. ethics_overall=0. |
| Deep Value Benchmark (Ashkinaze 2025) | Value depth testing, not normative frameworks. |
| EthicsMH (Kasu 2025) | Mental health ethics, low framework scores. |
| ConflictScope (Liu 2025) | Value prioritization pipeline, not normative frameworks. |
| PoliCon (Zhang 2025) | Political consensus. ethics_overall=0. |
| TRIAL (Chua 2025) | Red-teaming methodology, not ethics benchmark. |
| Hong PrinciplismQA (long title) | Duplicate of 2025-Hong-PrinciplismQA.md already in matrix. |
| TrolleyBench (short) | Duplicate of TrolleyBench (long title). |
| So Confucian (2024) | OpenAI case study, not Confucian benchmark despite title. |
| Varshney Decolonial (2024) | Theory paper, no benchmark. AIES 2024. |
| EthicsSuite (Ma 2025) | Behavioral inconsistency testing, not normative frameworks. |

---

## Strategy 2: Ethics Score Mining (ethics_overall >= 80)

Identified 179 papers with is_benchmark=Yes AND ethics_overall>=50 NOT in matrix. Most are hate speech / bias / fairness benchmarks with high ethics_overall but zero normative framework scores. The top normative candidates were surfaced through Strategy 5 overlap.

---

## Strategy 3: Care Ethics Scan (care_ethics >= 50)

15 papers with care_ethics >= 50. Key findings:

| Paper | CE Score | Has Benchmark? | Recommendation |
|-------|----------|----------------|----------------|
| El Masri "Towards Attuned AI" | 100 | No | EXCLUDE -- theoretical |
| Dubey "Addressing Moral Uncertainty" | 95 | No (RL method) | REVIEW -- VE/DE/UE=100 |
| Nadeem "Ethical Decision-Making" | 100 | **In matrix** | Already included |
| Chakraborty "Structured Moral" | 60 | **In matrix** | Already included |
| Liang "Synth-Empathy" | 100 | No | EXCLUDE -- empathy corpus |
| SYNTHEMPATHY (Chen 2025) | 100 | No | EXCLUDE -- empathy corpus |
| Suh "SENSE-7" | 100 | No | EXCLUDE -- user perception |
| Wang "PERM" | 95 | No | EXCLUDE -- empathy reward |
| Steen "ChatGPT Ethics" | 70 | No | EXCLUDE -- ethics analysis |
| Hong "PrinciplismQA" | 70 | **In matrix** | Already included |

**Key finding:** Care ethics benchmarks remain an underrepresented gap. Most high care_ethics papers are empathy/NLP corpora, not normative evaluation instruments. The Dubey "Ethical-RL" paper (VE=DE=UE=100, CE=95) deserves REVIEW as it uniquely covers all 5 traditions.

---

## Strategy 4: Non-Western Ethics Scan

### Confucian Ethics (nw_confucian >= 50)
- **CVC (Wu 2025)**: nw_confucian=100, VE/DE/UE=50. **INCLUDE** (see Strategy 5).
- So "Confucian Analects" (2024): nw_confucian=65 but actually an OpenAI case study. EXCLUDE.
- Qian "Chinese Moral Stories" (2023): nw_confucian=90 but descriptive dataset, not normative benchmark.

### Ubuntu Ethics (nw_ubuntu >= 50)
- No papers had both nw_ubuntu >= 50 AND (is_benchmark=Yes OR normative framework scores >= 50).
- Closest: Berg "Ubuntu-Guided LLM Framework" (2026) and Eickhoff "UbuntuGuard" (2026) -- but these are in CEI-AI-Statements, not evaluation benchmarks in the vault.

### Islamic Ethics (nw_islamic_ethics >= 50)
- FatwaSet (Alyemny 2023): nw_islamic=100, is_benchmark=Yes, but tests fatwa classification, not normative ethics framework application.
- IslamTrust (Lahmar 2025): Islamic values alignment, not normative framework.
- No Islamic ethics papers contain normative evaluation instruments for the NormEval feature matrix.

### Buddhist/Dharmic Ethics
- BuddhismEval (Xiong 2025): Tests Buddhist knowledge, not normative reasoning.
- MITRA (Keutzer 2025): Buddhist Chinese language benchmark, not ethics evaluation.
- No viable normative ethics benchmarks from Buddhist tradition found.

**Key finding:** CVC is the only non-Western paper strong enough for INCLUDE. Ubuntu, Islamic, and Buddhist traditions lack normative *evaluation instruments* in the vault -- they have theory/framework papers but not benchmarks.

---

## Strategy 5: Benchmark + Ethics Cross-Reference

Papers with is_benchmark=Yes AND ethics_overall>=50, framework scores>=50, NOT in matrix:

### INCLUDE from Cross-Reference

**7. CVC Chinese Values Corpus (Wu 2025)** -- `2025-Wu-CVC.md`
- VE=50, DE=50, UE=50 | nw_confucian=100
- 250K value rules. HuggingFace dataset. Confucian framework.
- **Why include:** Only non-Western normative benchmark in the vault with multiple framework engagement.

**8. One Model, Many Morals (Farid 2025)** -- `2025-Farid-One Model, Many Morals.md`
- DE=50, UE=50 | ICLR 2026 | 6 languages
- Translates existing ethics benchmarks for cross-linguistic evaluation.
- **Why include:** Top venue, strong normative framework testing across languages.

**9. Moral Reasoning Across Languages (Zhou 2025)** -- `2025-Zhou-Moral Reasoning Across Languages.md`
- DE=50, UE=50 | 5 languages
- Cross-lingual normative ethics consistency evaluation.
- **Why include:** Complements Farid 2025 with different language set.

**10. Is ETHICS About Ethics? (Hancox-Li 2024)** -- `2024-Hancox-Li-Is ETHICS about ethics.md`
- VE=100, DE=100, UE=100 | Meta-analysis of ETHICS benchmark
- Critical evaluation questioning validity of the most-cited normative ethics benchmark.
- **Why include:** Essential meta-analysis -- if NormEval evaluates benchmarks, this paper that evaluates the ETHICS benchmark is indispensable.

**11. TRIAGE (Kirch 2024)** -- `2024-Kirch-TRIAGE.md`
- DE=50, UE=50 | Medical triage | GitHub available
- Mass casualty scenarios with deontological vs utilitarian resource allocation.
- **Why include:** Real-world normative reasoning with objective answers from medical professionals.

**12. Normative Evaluation (Sachdeva 2025)** -- `2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas.md`
- FAccT 2025 | 10K+ AITA dilemmas | 7 LLMs | GitHub code
- Title literally contains "Normative Evaluation". High ecological validity.
- **Why include:** The word "normative" in the title, FAccT venue, large-scale, reproducible.

### REVIEW from Cross-Reference (7 papers)

| Paper | Framework Scores | Why Review |
|-------|-----------------|------------|
| MoralNet (Astobiza 2023) | VE=50, DE=50 | May be conceptual proposal only |
| Wang "Diverse Value Alignment" (2025) | DE=50, UE=50 | AIES 2025, may be method not benchmark |
| Pluralist Survey (SOCIETY 2025) | VE=55 | May be value-alignment not normative |
| BengaliMoralBench (Kumar 2025) | VE=50 | ACL 2025, review normative depth |
| Senthilkumar "Ethical Ambiguity" (2024) | DE=50, UE=50 | Review if novel benchmark |
| MORABLES (Marcuzzo 2025) | Low | EMNLP 2025, abstract moral reasoning |
| Ramanayake "Pro-Social Rule Breaking" (2022) | DE=50, UE=60 | Review normative depth |

---

## Strategy 6: Keyword Scan

56 papers matched normative keywords in titles/abstracts AND had benchmark/eval/dataset tags.

Most promising NOT already covered:
- TrolleyBench (Zhu 2025) -- REVIEW (consistency metric, low framework scores)
- CLASH (Lee 2025) -- REVIEW (345 dilemmas, 3795 perspectives, HuggingFace data)
- Tennant "Moral Alignment" ICLR 2025 -- REVIEW (low scores may undercount, prestigious venue)
- Delphi Experiment (Jiang 2025) -- REVIEW (Nature MI, CO=50, commonsense morality)

Most keyword matches were for papers testing "moral reasoning" in general (MFT-based), not normative ethics traditions specifically. The keyword scan confirmed that the vault's coverage of specifically *normative* ethics benchmarks is concentrated in the 37 + 12 new papers identified above.

---

## Summary of Recommendations

### 12 INCLUDE (add to feature matrix)

| # | Paper | Key Frameworks | Strategy |
|---|-------|---------------|----------|
| 1 | OffTheRails (Franken 2024) | DE=50, UE=50 | S1, S5, S6 |
| 2 | EMNLP Framework (Jiang 2025) | VE/DE/UE/CO=50 | S1, S2, S5 |
| 3 | COMETH (Morlat 2025) | 6 deontological rules | S1 |
| 4 | Ebara Medical Ethics (2025) | DE=40, principlism | S1 |
| 5 | MedES (Jin 2026) | Chinese med ethics | S1, S5 |
| 6 | Basu Multilingual (2025) | DE=50, UE=50, 6 langs | S1, S5 |
| 7 | CVC Chinese Values (Wu 2025) | VE/DE/UE=50, Confucian | S4, S5 |
| 8 | One Model Many Morals (Farid 2025) | DE=50, UE=50, ICLR | S5, S6 |
| 9 | Moral Reasoning Across Langs (Zhou 2025) | DE=50, UE=50, 5 langs | S5, S6 |
| 10 | Is ETHICS About Ethics? (Hancox-Li 2024) | VE/DE/UE=100, meta | S5 |
| 11 | TRIAGE (Kirch 2024) | DE=50, UE=50, medical | S5 |
| 12 | Normative Evaluation (Sachdeva 2025) | FAccT, 10K dilemmas | S6 |

### 13 REVIEW (need closer reading)

MoralNet, Wang Ethical Reasoning, Pluralist Survey, BengaliMoralBench, Senthilkumar Ambiguity, MORABLES, Ramanayake Pro-Social, TrolleyBench, CLASH, Tennant ICLR, BenchMoral, Delphi Experiment, Dubey Ethical-RL.

### 20 EXCLUDE

Papers that are safety benchmarks, bias/fairness benchmarks, MFT-based instruments, theoretical frameworks without evaluation data, or duplicates.

---

## Gaps Identified

1. **Care ethics:** No dedicated care ethics benchmark exists in the vault. The gap is structural.
2. **Contractarian ethics:** Only 2 papers have contractarian_ethics >= 50 among non-matrix papers (EMNLP framework, Delphi).
3. **Non-Western traditions:** Only CVC (Confucian) has benchmark-quality normative evaluation. Ubuntu, Islamic, Buddhist, and Indigenous traditions have theory papers but no evaluation instruments.
4. **Virtue ethics benchmarks:** Most benchmarks test deontological vs utilitarian reasoning; virtue ethics is underrepresented as a standalone evaluation target.

---

*Generated by Agent 1C, NormEval vault mining task. Machine-readable results: `20260404-normeval-vault-mining-results.json`*
