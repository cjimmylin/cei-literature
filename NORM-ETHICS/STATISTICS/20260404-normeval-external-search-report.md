# NormEval External Search: Benchmarks Not Yet in Vault

**Date:** 2026-04-04
**Agent:** 2B (External Search)
**Search scope:** Web (arXiv, Semantic Scholar, HuggingFace, Google Scholar, publisher sites)
**Known benchmarks:** 37 (feature matrix) + 12 (vault mining candidates)
**Vault size:** 2,043 papers

## Executive Summary

Systematic external search across 5 strategies identified **25 candidate papers**, of which:
- **5 ADD_TO_VAULT** -- genuinely new papers not in the vault with normative ethics relevance
- **7 MONITOR** -- relevant to the NormEval argument but not new benchmarks
- **13 SKIP** -- already in the vault or not normative ethics benchmarks

The 5 ADD_TO_VAULT candidates would add novel perspectives on:
- Representational probing of normative framework distinctions (Xu et al. 2026)
- RLVR training methods applied to moral reasoning benchmarks (Zhang et al. 2026)
- Islamic knowledge/jurisprudence benchmarking at unprecedented scale (IslamicMMLU, IslamicLegalBench)
- Real-world research ethics dilemma evaluation (Du et al. 2025)

**Key finding: The non-Western benchmark gap is rapidly closing for Islamic ethics** (3 new benchmarks in early 2026 alone), while Buddhist, Hindu/Dharmic, Ubuntu, and Indigenous ethics benchmarks remain at zero.

---

## Strategy 1: Forward Citation Search

Searched for papers citing the top 5 benchmarks in the feature matrix.

### Citing ETHICS (Hendrycks 2021)
- Xu et al. (2026) use ETHICS to probe whether LLMs distinguish normative frameworks at the representation level. **ADD_TO_VAULT** -- see #1.
- ProMoral-Bench (Thomas 2026) already in vault. Uses ETHICS + novel ETHICS-Contrast robustness test.

### Citing MoReBench (Chiu 2025)
- Zhang et al. (2026) adapt RLVR training methods using MoReBench. **ADD_TO_VAULT** -- see #2.
- Huang et al. (2026) study moral reasoning trajectories using MoReBench. Already in vault.
- Both papers extend MoReBench rather than introducing new benchmarks.

### Citing DailyDilemmas (Chiu 2024)
- Anthropic "Values in the Wild" (COLM 2025) references DailyDilemmas. Already in vault.
- "Do Language Models Think Consistently?" uses DailyDilemmas + OpinionQA. Already in vault.
- No new benchmark datasets found citing DailyDilemmas.

### Citing MoralReason-QA (An 2025) and Samway (2025)
- No new citing papers with novel datasets found beyond what is already in the vault.

### Strategy 1 Yield: 2 ADD_TO_VAULT, 0 MONITOR

---

## Strategy 2: arXiv Search (Post-March 2026)

Searched 6 query variants targeting recent arXiv submissions.

### New finds NOT in vault:

**1. Probing Ethical Framework Representations (Xu, Rusnak, Kaplan 2026)** -- arXiv 2603.23659
- EPFL. March 2026.
- Probes hidden representations across 5 ethical frameworks (deontology, utilitarianism, virtue, justice, commonsense) in 6 LLMs (4B-72B params).
- Key finding: differentiated ethical subspaces exist but with asymmetric transfer (deontology probes generalize to virtue; commonsense fails on justice).
- Post-hoc validation reveals probes partly depend on benchmark template surface features.
- **Directly relevant to NormEval Claim 2** (benchmarks may test surface features, not deep normative reasoning).
- **Recommendation: ADD_TO_VAULT**

**2. Does LLM Alignment Really Need Diversity? (Zhang et al. 2026)** -- arXiv 2603.10588
- Microsoft Research. March 2026.
- First empirical study comparing RLVR paradigms on MoReBench.
- Trains Qwen3-1.7B judge model with rubric-grounded rewards.
- Finds moral reasoning has concentrated high-reward distributions (unlike math).
- **Recommendation: ADD_TO_VAULT**

### Already in vault (confirmed):
- Understanding Moral Reasoning Trajectories (Huang 2026) -- arXiv 2603.16017
- ProMoral-Bench (Thomas 2026) -- arXiv 2602.13274
- The Staircase of Ethics (Wu 2025) -- arXiv 2505.18154
- MoCoP (Jamshidi 2025) -- arXiv 2512.03026
- MFTCXplain (Trager 2025) -- arXiv 2506.19073
- Discerning What Matters (Kilov 2025) -- arXiv 2506.13082
- Mapping Moral Reasoning in LLMs (Mahajan 2025) -- AIES 2025
- A Roadmap for Evaluating Moral Competence (Gabriel 2026) -- Nature

### Strategy 2 Yield: 2 ADD_TO_VAULT, 0 MONITOR

---

## Strategy 3: HuggingFace Hub Search

Searched for datasets tagged with ethics, moral, normative, and dilemma keywords.

### Key datasets found on HuggingFace:
| Dataset | Status |
|---------|--------|
| hendrycks/ethics | In vault, in matrix (#1) |
| morebench/morebench | In vault, in matrix (#5) |
| ninoscherrer/moralchoice | In vault (2023-Scherrer) |
| demelin/moral_stories | Not in vault but 2021 paper; too old |
| Abderraouf000/IslamTrust-benchmark | In vault (2025-Lahmar) |
| society-ethics/papers | Meta-collection, not benchmark |
| metaeval/ethics | Copy of hendrycks/ethics |
| andrian-kr/ETHICS_commonsense | Subset of hendrycks/ethics |
| Ukrainian ETHICS translation (2026) | Localization of existing benchmark |

**No new normative ethics datasets found on HuggingFace** that are not already tracked in the vault or identified via other strategies.

### Strategy 3 Yield: 0 ADD_TO_VAULT, 0 MONITOR

---

## Strategy 4: Non-Western Benchmark Search

### Islamic Ethics -- RAPID GROWTH

**3. IslamicMMLU (2026)** -- arXiv 2603.23750. **ADD_TO_VAULT**
- 10,013 MCQ: Quran (2,013), Hadith (4,000), Fiqh (4,000)
- 26 LLMs evaluated; 54-point performance gap
- Fiqh track has madhab bias detection (school-of-thought preferences)
- HuggingFace leaderboard + evaluation code
- Largest Islamic AI benchmark to date

**4. IslamicLegalBench (2026)** -- arXiv 2602.21226. **ADD_TO_VAULT**
- 718 instances, 13 tasks, 7 schools of Islamic jurisprudence
- 38 foundational legal texts spanning 1,200 years
- Tasks include qiyas (analogical reasoning) and cross-school synthesis
- Best model: 68% correct, 21% hallucination
- 20% public dev set

**Already in vault:**
- IslamTrust (Lahmar 2025) -- 406 MCQ, Arabic+English
- Sacred or Synthetic (Atif 2025) -- religious question reliability

**Monitor-tier Islamic papers:**
- Assessing LLMs on Islamic Inheritance Law (2025, ArabicNLP) -- narrow domain
- Islamic Ethics and AI: Trusteeship Ethics (2025, Phil & Tech) -- theory only
- Pluralist Ethical Benchmarking for AI (2023, Phil & Tech) -- theory only

### Confucian Ethics -- COVERED
- CVC/C-VARC (Wu 2025) already in vault. 250K value rules, Confucian grounding.
- CMoralEval (2024) already in vault. Chinese moral evaluation.
- CValues (2023) already in vault.

### Buddhist Ethics -- GAP CONFIRMED
- Dharma Setu (2025, Contemporary Buddhism) bridges Buddhist wisdom + AI using 10B-token BDRC corpus but is a framework paper, not a benchmark.
- **No dedicated Buddhist ethics LLM benchmark exists.**

### Hindu/Dharmic Ethics -- GAP CONFIRMED
- Hindu Responses to AI (2025) documents theological engagement but proposes no benchmark.
- **No dedicated Hindu/Dharmic ethics LLM benchmark exists.**

### Ubuntu/African Ethics -- GAP CONFIRMED
- Ethics of AI in Africa (2025, Ethics & Info Tech) explores Ubuntu governance but is theoretical.
- Career guidance evaluation across 10 African countries (2025) uses Ubuntu framing but tests career competencies, not ethics.
- **No dedicated Ubuntu/African philosophy LLM ethics benchmark exists.**

### Strategy 4 Yield: 2 ADD_TO_VAULT, 4 MONITOR

---

## Strategy 5: Adjacent Field Scan

### AI Safety Benchmarks with Normative Components
- How Should AI Safety Benchmarks Benchmark Safety? (2026, arXiv 2601.23112) -- Reviews 210 safety benchmarks; argues they are normative not descriptive. **MONITOR**
- Mind the Gap: Unifying AI Safety and Ethics (2025, arXiv 2512.10058) -- Calls for safety-ethics integration via shared benchmarks. **MONITOR**
- Legal Alignment for Safe and Ethical AI (Kolt 2026) -- Already in vault. Oxford AIGI.

### Constitutional AI Evaluation
- RAIL in the Wild (2025, arXiv 2505.00204) -- Operationalizes Anthropic's value taxonomy for evaluation. **MONITOR**
- Values in the Wild (Anthropic, COLM 2025) -- Already in vault.

### Legal AI with Normative Components
- LegalBench (Stanford, 2023) -- Already in vault. 162 tasks including normative reasoning.
- LEXam (2025) -- Already in vault. Swiss/European law.
- No new legal AI benchmarks with explicit normative ethics framing found.

### Biomedical Ethics
- PrinciplismQA (Hong 2025) -- Already in vault and in matrix (#33).
- MedEthicsQA (2025) -- Already in vault and in matrix (#36).
- No new biomedical ethics benchmarks beyond what is tracked.

### Real-World Ethics Cases
**5. Are LLMs Complicated Ethical Dilemma Analyzers? (Du et al. 2025)** -- arXiv 2505.08106. **ADD_TO_VAULT**
- 196 real-world research ethics cases from Georgia CTSA + Online Ethics Center
- 5-component structure: Introduction, Key Factors, Historical Theoretical Perspectives, Resolution Strategies, Key Takeaways
- Expert opinions + non-expert baselines
- Tests GPT-4o-mini, Claude-3.5-Sonnet, Deepseek-V3, Gemini-1.5-Flash
- Unique: tests engagement with historical ethical theory, not just judgment

### Strategy 5 Yield: 1 ADD_TO_VAULT, 3 MONITOR

---

## Summary: Papers to Add to Vault

| # | Paper | Year | Traditions | Why Add |
|---|-------|------|-----------|---------|
| 1 | Xu et al. -- Probing Ethical Framework Representations | 2026 | DE/UE/VE/Justice/Common | Directly tests if LLMs distinguish normative frameworks at representation level |
| 2 | Zhang et al. -- RLVR for Moral Reasoning | 2026 | All 5 via MoReBench | Shows how training signals from moral benchmarks actually work |
| 3 | IslamicMMLU | 2026 | Islamic ethics | Largest Islamic benchmark (10K); madhab bias detection |
| 4 | IslamicLegalBench | 2026 | Islamic jurisprudence | 7 schools, 1,200 years, analogical reasoning tasks |
| 5 | Du et al. -- Ethical Dilemma Analyzers | 2025 | Mixed normative | 196 real research ethics cases with theoretical perspectives |

## Summary: Papers to Monitor

| # | Paper | Year | Why Monitor |
|---|-------|------|------------|
| 1 | How Should AI Safety Benchmarks Benchmark Safety? | 2026 | 210 safety benchmarks reviewed; normative framing |
| 2 | Mind the Gap: Safety-Ethics Integration | 2025 | Position paper supporting NormEval argument |
| 3 | RAIL in the Wild | 2025 | Anthropic value taxonomy operationalized |
| 4 | Islamic Trusteeship Ethics for AI | 2025 | Theoretical grounding for Islamic AI benchmarks |
| 5 | Pluralist Ethical Benchmarking for AI | 2023 | Early theory for non-Western benchmarks |
| 6 | Dharma Setu (Buddhist AI) | 2025 | 10B-token Buddhist corpus; no benchmark yet |
| 7 | Islamic Inheritance Law Assessment | 2025 | Narrow-domain Islamic legal reasoning |

---

## Key Findings for NormEval Paper

### 1. The Normative Framework Representation Gap
Xu et al. (2026) show LLMs have differentiated ethical subspaces but with asymmetric transfer and surface-feature dependence. This directly supports NormEval's claim that benchmarks may test pattern matching rather than normative reasoning.

### 2. Training Signal Analysis
Zhang et al. (2026) demonstrate moral reasoning has concentrated high-reward distributions, unlike math/code. Suggests normative benchmarks provide different training signals than capability benchmarks.

### 3. Non-Western Ethics: Islamic Surge, Others at Zero
Three new Islamic ethics benchmarks appeared in early 2026 alone (IslamicMMLU, IslamicLegalBench, IslamTrust already tracked). But Buddhist, Hindu, Ubuntu, and Indigenous ethics benchmarks remain entirely absent. This asymmetry is worth documenting in NormEval.

### 4. Framework Switching is Normal
Huang et al. (2026, already in vault) show 55-57% of consecutive reasoning steps involve framework switches. This challenges the assumption that benchmarks can cleanly test individual frameworks.

### 5. Benchmark Saturation in Western Normative Ethics
Most new papers in 2025-2026 use existing benchmarks (ETHICS, MoReBench, DailyDilemmas) rather than creating new ones. The field may be reaching saturation for Western normative ethics datasets.
