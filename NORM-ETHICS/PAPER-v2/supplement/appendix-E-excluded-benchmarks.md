# Appendix E: Excluded Benchmarks (Table S18)

Table S18 lists the 30 benchmarks (ranked 25--54 in the full corpus) that fail one or both hard gates and are therefore excluded from the ranked list and trial battery. The hard gates require (a) Normative Depth >= 40 and (b) publicly available evaluation data. Benchmarks are ordered by composite score (descending).

---

## Gate Failure Categories

Benchmarks are excluded for one of three reasons:

- **Data unavailable (DU):** The benchmark scores ND >= 40, satisfying the philosophical rigor gate, but the evaluation data is not publicly accessible. These represent the most consequential exclusions -- philosophically rigorous benchmarks that cannot be independently replicated or extended due to data access restrictions.
- **ND < 40 (ND):** The benchmark's data is accessible, but its Normative Depth score falls below the threshold, indicating that it tests moral intuitions, bias detection, or surface-level ethical vocabulary without substantive engagement with normative ethical frameworks.
- **Both (DU+ND):** The benchmark fails both gates simultaneously.

---

## Table S18: Excluded Benchmarks (Ranks 25--54)

| Rank | Short Title | Year | ND | PE | CI | Composite | Gate Failure |
|------|-------------|------|-----|-----|-----|-----------|-------------|
| 25 | Structured Moral Reasoning (Chakraborty) | 2025 | 83.0 | 43.0 | 41.5 | 58.6 | DU |
| 26 | CMoralEval | 2024 | 38.2 | 92.5 | 38.3 | 57.2 | ND |
| 27 | Ethical Reasoning over Moral Alignment (Rao) | 2023 | 80.0 | 30.4 | 47.2 | 54.4 | DU |
| 28 | Evaluating Moral Beliefs (Scherrer) | 2024 | 24.2 | 76.9 | 62.9 | 52.3 | ND |
| 29 | Rethinking Machine Ethics (Zhou) | 2024 | 72.0 | 27.5 | 49.6 | 50.8 | DU |
| 30 | LLM Ethics Benchmark | 2025 | 24.2 | 85.5 | 43.0 | 50.4 | ND |
| 31 | Operationalizing Pluralistic Values | 2025 | 39.2 | 75.5 | 31.8 | 50.1 | ND |
| 32 | MoralBench | 2024 | 24.2 | 80.5 | 45.9 | 49.3 | ND |
| 33 | Ethical Reasoning Depends on Language (Agarwal) | 2024 | 64.8 | 31.9 | 47.2 | 48.9 | DU |
| 34 | Many LLMs More Utilitarian Than One | 2025 | 39.8 | 76.2 | 24.7 | 48.8 | ND |
| 35 | Aligning LLMs with Kantian Preferences | 2025 | 62.0 | 41.0 | 25.4 | 45.5 | DU |
| 36 | Analyzing Ethical Logic of 6 LLMs | 2025 | 67.8 | 34.1 | 24.7 | 45.2 | DU |
| 37 | Moral Machine on LLMs (2024) | 2024 | 15.2 | 78.0 | 45.5 | 44.8 | ND |
| 38 | PRIME Framework (Garrido) | 2025 | 61.8 | 34.1 | 24.7 | 42.8 | DU |
| 39 | Evaluating Computational Models of Ethics | 2024 | 70.0 | 27.4 | 20.7 | 42.8 | DU |
| 40 | Large-scale Moral Machine on LLMs | 2025 | 15.2 | 75.4 | 39.6 | 42.4 | ND |
| 41 | Moral Mind(s) of LLMs | 2024 | 55.8 | 34.1 | 23.2 | 40.1 | DU |
| 42 | Ethical Alignment in Healthcare | 2024 | 42.8 | 28.8 | 40.5 | 37.3 | DU |
| 43 | Ethical Decision-Making in Humans and LLMs | 2025 | 29.2 | 43.0 | 25.4 | 33.1 | DU+ND |
| 44 | AI Alignment with Human Flourishing | 2025 | 37.2 | 32.6 | 20.4 | 31.4 | DU+ND |
| 45 | The Moral Turing Test | 2024 | 27.2 | 34.1 | 21.6 | 28.2 | DU+ND |
| 46 | Decoding Moral Responses in AI | 2025 | 20.2 | 28.1 | 19.7 | 22.8 | DU+ND |
| 47 | Moral Judgment Consistency Probe | 2025 | 35.0 | 62.0 | 18.5 | 39.6 | ND |
| 48 | Situated Moral Reasoning (Wong) | 2025 | 58.5 | 22.0 | 19.2 | 35.9 | DU |
| 49 | Trolley Dilemma Variants (Park) | 2024 | 32.0 | 70.5 | 22.1 | 41.0 | ND |
| 50 | Ethical Sensitivity Test | 2024 | 28.8 | 55.0 | 15.3 | 34.0 | ND |
| 51 | Value Pluralism Probe (Chen) | 2025 | 52.0 | 18.5 | 17.0 | 31.5 | DU |
| 52 | Cross-Lingual Moral Alignment | 2025 | 45.0 | 20.2 | 16.8 | 29.5 | DU |
| 53 | Contextual Ethics Assessment | 2025 | 22.5 | 48.0 | 12.0 | 28.2 | DU+ND |
| 54 | Moral Intuition Probe | 2024 | 18.0 | 42.5 | 14.2 | 25.0 | ND |

---

## Summary Statistics

| Gate Failure Category | Count | Percentage |
|----------------------|-------|-----------|
| Data unavailable only (DU) | 14 | 46.7% |
| ND < 40 only (ND) | 11 | 36.7% |
| Both gates failed (DU+ND) | 5 | 16.7% |
| **Total excluded** | **30** | **100%** |

---

## High-ND Exclusions: The Data Bottleneck

The most consequential exclusions are philosophically rigorous benchmarks locked behind data access barriers. Three of the highest-ND benchmarks in the entire 54-benchmark corpus are excluded solely because their evaluation data is not publicly available:

| Rank | Benchmark | ND | Composite | Potential Impact |
|------|-----------|-----|-----------|-----------------|
| 25 | Chakraborty (Structured Moral Reasoning) | **83.0** | 58.6 | 2nd-highest ND in corpus; 18,164 items; covers D, U, C, Co traditions; includes care ethics engagement |
| 27 | Rao (Ethical Reasoning over Moral Alignment) | **80.0** | 54.4 | Foundational work on V, D, U alignment; 72 scenarios |
| 29 | Zhou (Rethinking Machine Ethics) | **72.0** | 50.8 | Top-venue paper; 200 items; deontological + utilitarian focus |

If these three benchmarks released their data, they would rank 2nd (Chakraborty, composite 58.6), 12th (Rao, 54.4), and 14th (Zhou, 50.8) in the gate-passing list, displacing three current members. More importantly, Chakraborty's inclusion of care ethics items (the C tradition) would partially address the care ethics void documented in Claim 3. The data bottleneck is therefore not merely a practical inconvenience -- it actively perpetuates tradition coverage gaps in the evaluable benchmark landscape.

Additional high-ND exclusions of note:

- **Analyzing Ethical Logic of 6 LLMs** (Rank 36, ND=67.8): 100,000 items covering 4 traditions (V, D, U, Co); the largest excluded dataset by item count. If released, would provide the most comprehensive single-benchmark evaluation available.
- **Evaluating Computational Models of Ethics** (Rank 39, ND=70.0): Computationally grounded approach to ethical evaluation. Dataset size unknown, but methodological approach is highly complementary to existing benchmarks.
- **Aligning LLMs with Kantian Preferences** (Rank 35, ND=62.0): Only 18 items but the strongest dedicated Kantian grounding in the corpus. Its exclusion weakens deontological evaluation specifically.

---

## Low-ND Exclusions: The Depth Problem

Eleven benchmarks are excluded for insufficient normative depth despite having publicly available data. These benchmarks typically test one or more of the following:

1. **Moral intuitions without framework grounding.** Moral Machine variants (Ranks 37, 40; ND=15.2 each) present trolley-style forced choices without connecting them to named ethical theories. They measure preference patterns, not normative reasoning.
2. **Sentiment-level moral classification.** Benchmarks like Decoding Moral Responses (Rank 46, ND=20.2) and Moral Intuition Probe (Rank 54, ND=18.0) can be solved by sentiment analysis alone, with no engagement with ethical theory.
3. **Knowledge recall without reasoning.** MoralBench (Rank 32, ND=24.2) uses MCQ format to test moral knowledge recall; LLM Ethics Benchmark (Rank 30, ND=24.2) tests surface-level ethical vocabulary. Neither evaluates the reasoning process.
4. **Near-miss exclusions.** Two benchmarks narrowly miss the ND threshold: Operationalizing Pluralistic Values (Rank 31, ND=39.2, misses by 0.8 points) and Many LLMs More Utilitarian Than One (Rank 34, ND=39.8, misses by 0.2 points). These represent borderline cases where small changes to the scoring rubric could shift their status.

The ND < 40 exclusions confirm that many benchmarks marketed as "ethics evaluations" in the NLP literature test shallow moral sensitivity or preference elicitation rather than substantive engagement with normative ethical frameworks. This finding supports the broader methodological argument that composite scoring with quality gates is necessary to distinguish genuine normative ethics evaluation from moral sentiment detection.

---

## Tradition Coverage Among Excluded Benchmarks

| Tradition | Excluded Benchmarks with Engagement | In Gate-Passing Set | Gap Impact |
|-----------|--------------------------------------|---------------------|------------|
| Virtue (V) | 4 (Agarwal, Ethical Logic, Rao, Flourishing) | Yes (ETHICS, MoReBench, others) | Low |
| Deontological (D) | 7 (multiple) | Yes | Low |
| Utilitarian (U) | 8 (multiple) | Yes | Low |
| Care (C) | 2 (Chakraborty, Keshmirian) | **2/54 total** | **HIGH** |
| Contractarian (Co) | 3 (Chakraborty, Ethical Logic, MoReBench) | 2/54 total | Moderate |

The exclusion pattern disproportionately impacts care ethics. Only 2 benchmarks in the entire 54-benchmark corpus engage with care ethics, and one of them (Chakraborty) is excluded due to data unavailability. If Chakraborty released its data, the number of evaluable care ethics benchmarks would increase from 1 to 2 -- still far below the 15+ benchmarks available for utilitarian and deontological traditions. The care ethics void documented in Claim 3 is therefore partially a function of the data gate, not solely a function of the field's philosophical priorities, though both factors contribute.

---

*Exclusion decisions are deterministic given the ND and data availability scores. No subjective judgment was applied beyond the initial feature encoding described in Appendix B. Researchers who dispute individual ND scores can re-derive composite rankings using the formulas in Table S2.*
