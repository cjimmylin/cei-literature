# Agent 6: PhilPapers & Philosophy Databases Explorer Report

**Date:** 2026-02-07
**Agent:** Agent 6 - PhilPapers + Philosophy Databases Explorer
**Mission:** Find NEW papers with implementable benchmarks/datasets for ethical values alignment in LLMs from philosophy-first databases and journals
**Searches Conducted:** 19 web searches + 8 deep-fetch operations

---

## Executive Summary

This report identifies **14 NEW papers** not present in the existing 67+ known papers list. These papers originate from philosophy-adjacent venues (Royal Society Open Science, PNAS, Nature Machine Intelligence, Scientific Reports, AI and Ethics/Springer, NeurIPS Ethics Workshops, WINLP) and represent an underexplored vector: philosophy-first perspectives on LLM moral evaluation. Several introduce novel philosophical frameworks (principalism, common morality theory, metaethics, moral pluralism) that go beyond the CS-venue focus of prior searches.

---

## NEW Papers Found

---

### Paper 1: The Convergent Ethics of AI? Analyzing Moral Foundation Priorities in LLMs with a Multi-Framework Approach

**Full Citation:** Coleman, C., Neuman, W.R., Dasdan, A., Ali, S., & Shah, M. (2025). The Convergent Ethics of AI? Analyzing Moral Foundation Priorities in Large Language Models with a Multi-Framework Approach. arXiv preprint arXiv:2504.19255.

**DOI/URL:** https://arxiv.org/abs/2504.19255 | https://doi.org/10.48550/arXiv.2504.19255

**Philosophical Frameworks:**
- PRIME Framework (Priorities in Reasoning and Intrinsic Moral Evaluation) - novel methodology
- Moral Foundations Theory (Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Sanctity/Degradation)
- Kohlberg's Developmental Stages of moral reasoning
- Consequentialist-Deontological reasoning spectrum

**Dataset Details:**
- Dual-protocol approach: direct self-description questioning + response analysis to established ethical dilemmas
- 25 classic moral dilemmas used as test stimuli
- Evaluates six moral dimensions from Moral Foundations Theory
- 6 leading LLMs tested across frameworks

**LLMs Tested:** 6 leading LLMs (including Claude, GPT-4, LLaMA; Claude achieves 91.2% alignment with human moral intuitions; LLaMA at 76.3%)

**Code/Data URLs:** Not publicly released at time of search

**Implementation Readiness:** MEDIUM - The PRIME framework is well-specified and the dual-protocol methodology is reproducible, but no public dataset release yet.

**Unique Contribution:** First paper to systematically apply three distinct philosophical typologies (moral philosophy, comparative ethics, behavioral psychology) simultaneously to LLM evaluation. Reveals convergent moral prioritization across all models: strong Care/Fairness emphasis, weak Authority/Loyalty/Sanctity weighting. Philosophy-grounded rather than CS-grounded approach.

---

### Paper 2: Language Model Alignment in Multilingual Trolley Problems (MultiTP)

**Full Citation:** Jin, Z., Kleiman-Weiner, M., Piatti, G., Levine, S., Liu, J., Gonzalez, F., Ortu, F., Strausz, A., Sachan, M., Mihalcea, R., Choi, Y., & Scholkopf, B. (2024/2025). Language Model Alignment in Multilingual Trolley Problems. ICLR 2025 Spotlight. arXiv:2407.02273.

**DOI/URL:** https://arxiv.org/abs/2407.02273

**Philosophical Frameworks:**
- Trolley Problem paradigm from moral philosophy (Philippa Foot, Judith Jarvis Thomson)
- Moral Machine experiment framework (40M+ human judgments across 200+ countries)
- Cross-cultural moral psychology (6 moral dimensions: species, gender, fitness, status, age, number of lives)

**Dataset Details:**
- **MultiTP corpus:** 98,440 trolley problem vignettes
- 460 vignettes per language across 107 languages
- On-demand generated data (not found in training corpora - methodological innovation)
- Grounded in Moral Machine human judgment baselines
- Six moral preference dimensions systematically varied

**LLMs Tested:** 19 LLMs including Llama (various sizes), Gemma 2, Mistral 7B, Phi, Qwen 2, GPT-3, GPT-4, GPT-4o-mini

**Code/Data URLs:** https://github.com/causalNLP/moralmachine

**Implementation Readiness:** HIGH - Dataset publicly available, 107 languages, code released, well-structured evaluation protocol. ICLR 2025 Spotlight + Best Paper at NeurIPS 2024 Workshop on Pluralistic Alignment.

**Unique Contribution:** Largest multilingual moral evaluation dataset; grounded in classic trolley problem from philosophy; on-demand data generation avoids training contamination; reveals significant cross-lingual variance in moral alignment challenging uniform moral reasoning assumptions.

---

### Paper 3: The Pluralistic Moral Gap: Understanding Judgment and Value Differences between Humans and LLMs

**Full Citation:** Russo, G., Nozza, D., Rottger, P., & Hovy, D. (2025). The Pluralistic Moral Gap: Understanding Judgment and Value Differences between Humans and Large Language Models. arXiv:2507.17216.

**DOI/URL:** https://arxiv.org/abs/2507.17216

**Philosophical Frameworks:**
- Moral pluralism (value diversity as fundamental)
- 60-value moral taxonomy built from 3,783 value expressions
- Human moral judgment distribution analysis (beyond single "correct" answers)

**Dataset Details:**
- **Moral Dilemma Dataset:** 1,618 real-world moral dilemmas
- Each paired with distribution of human moral judgments (binary evaluation + free-text rationale)
- 60-value taxonomy extracted from 3,783 human value expressions
- Dynamic Moral Profiling (DMP): Dirichlet-based sampling method conditioning on human value distributions

**LLMs Tested:** Multiple LLMs (specific models not enumerated in available abstract)

**Code/Data URLs:** Not yet publicly released at time of search

**Implementation Readiness:** MEDIUM-HIGH - Well-defined dataset structure and novel DMP method; 64.3% alignment improvement demonstrated. Dataset release expected.

**Unique Contribution:** First paper to operationalize "pluralistic moral gap" - mismatch in both distribution and diversity of moral values between humans and LLMs. Introduces Dynamic Moral Profiling as a philosophically-grounded alignment correction technique. Philosophy-first perspective on why LLMs default to majority moral positions.

---

### Paper 4: TrolleyBench: Evaluating Emergent Moral Reasoning and Consistency in LLMs

**Full Citation:** Zhu, A. (2025). TrolleyBench: Evaluating Emergent Moral Reasoning and Consistency in LLMs. NeurIPS 2025 LLM Evaluation Workshop Poster.

**DOI/URL:** https://openreview.net/forum?id=27j9XJQV5O

**Philosophical Frameworks:**
- Trolley Problem paradigm (moral philosophy)
- Ethical consistency as a philosophical requirement (stable moral character/virtue ethics connection)
- Clarifying and contradictory follow-ups testing moral coherence

**Dataset Details:**
- Open-source benchmark with structured trolley-problem moral dilemmas
- Includes clarifying and contradictory follow-up questions
- Two novel metrics: Ethical Consistency Index (ECI) and entropy-based Inconsistency Score
- Human baselines included for comparison

**LLMs Tested:** Deepseek-R1, Mistral Small-32B, Gemini-2.5, GPT-4.1-mini

**Code/Data URLs:** https://anonymous.4open.science/r/TrolleyBench-FD46/README.md

**Implementation Readiness:** HIGH - Open-source, publicly available, novel metrics defined, human baselines provided. Published at NeurIPS 2025 workshop.

**Unique Contribution:** First open-source benchmark explicitly designed to evaluate ethical consistency (not just accuracy). Novel ECI metric captures a philosophically important dimension: whether models maintain coherent moral positions when challenged. Reveals ethical stances as "steerable but fragile."

---

### Paper 5: MedEthicsQA: A Comprehensive Question Answering Benchmark for Medical Ethics Evaluation of LLMs

**Full Citation:** Wei, J., Meng, Z., Xiao, Z., Hu, T., Feng, Y., Zhou, Z., Wu, J., & Liu, Z. (2025). MedEthicsQA: A Comprehensive Question Answering Benchmark for Medical Ethics Evaluation of LLMs. arXiv:2506.22808.

**DOI/URL:** https://arxiv.org/abs/2506.22808

**Philosophical Frameworks:**
- Beauchamp & Childress's Principalism (bioethics)
- 4P-26C-256G hierarchical ethics taxonomy (4 Pillar Principles - 26 Categories - 256 Detailed Guidelines)
- Four pillars: Autonomy (12.0%), Beneficence (44.3%), Non-Maleficence (32.4%), Justice (11.3%)

**Dataset Details:**
- 5,623 multiple-choice questions + 5,351 open-ended questions = 10,974 total items
- Sourced from medical datasets, question banks, and PubMed literature
- Rigorous quality pipeline: 22.4% expert-verified with 2.47% error rate
- CC BY-NC 4.0 license

**LLMs Tested:** State-of-the-art Medical LLMs and their foundation models (specific names in full paper)

**Code/Data URLs:** https://github.com/JianhuiWei7/MedEthicsQA

**Implementation Readiness:** HIGH - Large dataset, publicly released, GitHub available, well-validated. Operationalizes Beauchamp & Childress principalism directly.

**Unique Contribution:** Directly operationalizes the most influential framework in bioethics (principalism) as an LLM evaluation benchmark. Reveals that medical fine-tuning degrades ethical performance compared to foundation models - a critical finding for applied bioethics.

---

### Paper 6: PrinciplismQA: Towards Assessing Medical Ethics from Knowledge to Practice

**Full Citation:** Hong, C., Wu, M., Xiao, Q., Wang, Y., Wan, X., Yu, G., Wang, B., & Hu, Y. (2025). Towards Assessing Medical Ethics from Knowledge to Practice. arXiv:2508.05132.

**DOI/URL:** https://arxiv.org/abs/2508.05132

**Philosophical Frameworks:**
- Beauchamp & Childress's Four Principles (Autonomy, Beneficence, Non-Maleficence, Justice)
- WHO 2025 ethical governance guidelines for LLMs in clinical care
- Knowledge-Practice gap framework (philosophical distinction between knowing-that and knowing-how)

**Dataset Details:**
- **PrinciplismQA benchmark:** 3,648 questions total
  - 2,182 four-option MCQs (Knowledge tier)
  - 1,466 open-ended case-based questions (Practice tier)
- Sources: 350 authoritative medical ethics textbooks (2010+); AMA Journal of Ethics "Case and Commentary" articles (1999-2025)
- Expert-validated by medical professionals

**LLMs Tested:**
- Closed-source: GPT-4.1, o3, o3-mini, Claude Sonnet 4, Gemini 2.5 Flash, Qwen-Plus, DeepSeek-V3, DeepSeek-R1
- Open-source: Llama-3.1, Qwen2.5, Gemma-3
- Medical-specialized: HuatuoGPT-o1, Med42, MedGemma

**Code/Data URLs:** Not explicitly listed (likely forthcoming)

**Implementation Readiness:** MEDIUM-HIGH - Well-structured, expert-validated, but code/data URLs not yet confirmed publicly.

**Unique Contribution:** Distinguishes ethical knowledge from ethical practice application in LLMs - a philosophically significant finding. Most models "know" ethical principles but cannot effectively apply them to real-world clinical cases. Bridges the epistemology gap (knowing vs. doing) in a measurable way.

---

### Paper 7: Large Language Models Show Amplified Cognitive Biases in Moral Decision-Making

**Full Citation:** Capraro, V., et al. (2025). Large language models show amplified cognitive biases in moral decision-making. Proceedings of the National Academy of Sciences (PNAS), 122. DOI: 10.1073/pnas.2412015122.

**DOI/URL:** https://www.pnas.org/doi/10.1073/pnas.2412015122

**Philosophical Frameworks:**
- Omission bias (moral philosophy: distinction between acts and omissions)
- Moral psychology (cognitive bias framework)
- Deontological vs. consequentialist framing in dilemma presentation
- Personal vs. impersonal moral dilemmas (Greene et al. dual-process theory)

**Dataset Details:**
- Series of realistic moral dilemmas (personal and impersonal)
- Collective action problems
- Three experimental conditions per dilemma
- Human comparison baselines with controlled experiments

**LLMs Tested:** Range of LLMs including GPT variants (specific models in full paper); human participants as baselines

**Code/Data URLs:** PNAS supplementary materials (publicly available with publication)

**Implementation Readiness:** MEDIUM - Experimental paradigm is well-described and reproducible. Dilemma sets are standard in moral psychology. Published in PNAS lends high credibility.

**Unique Contribution:** Published in PNAS (premier interdisciplinary journal). Discovers two novel biases: (1) amplified omission bias (LLMs endorse inaction over action more strongly than humans), (2) novel "yes-no bias" unique to LLMs (responses flip based on question wording). Both biases induced by RLHF fine-tuning. Directly relevant to moral philosophy debate on acts vs. omissions.

---

### Paper 8: Robustness of Large Language Models in Moral Judgements

**Full Citation:** Oh, S. & Demberg, V. (2025). Robustness of large language models in moral judgements. Royal Society Open Science, 12(4), 241229. DOI: 10.1098/rsos.241229.

**DOI/URL:** https://royalsocietypublishing.org/doi/abs/10.1098/rsos.241229

**Philosophical Frameworks:**
- Moral Machine paradigm (applied ethics)
- Robustness as a necessary condition for moral competence (virtue ethics/moral philosophy)
- Moral dilemma vs. non-dilemma distinction (genuine ethical conflict requiring value trade-offs)

**Dataset Details:**
- Moral Machine vignettes with systematic prompt variations
- Tests sensitivity to: option labeling (Case 1/2 vs. A/B), prompt wording, attribute distribution
- Identified confounds in prior Moral Machine LLM studies
- Evaluation across dilemma and non-dilemma moral scenarios

**LLMs Tested:** Multiple LLMs (specific models in full paper; builds on Moral Machine LLM literature)

**Code/Data URLs:** Saarland University repository (publicly available via publication)

**Implementation Readiness:** MEDIUM - Provides important methodological corrections for existing benchmarks. Vignettes and protocols described in detail. Useful as a robustness audit layer.

**Unique Contribution:** Published in Royal Society Open Science. Demonstrates that previous Moral Machine LLM results may be confounded by presentation artifacts. Changing "Case 1/Case 2" to "(A)/(B)" reverses model decisions. Philosophically important: if moral judgments are not robust to surface-level changes, models lack genuine moral competence. Provides essential robustness audit methodology.

---

### Paper 9: Decoding Moral Responses in AI: A Quantitative Analysis of Large Language Models

**Full Citation:** [Authors not fully extracted]. (2025). Decoding Moral Responses in AI: A Quantitative Analysis of Large Language Models. ScienceDirect. DOI: 10.1016/j.chbah.2025.100121 (Computers in Human Behavior: Artificial Humans).

**DOI/URL:** https://www.sciencedirect.com/science/article/pii/S2451958825002696

**Philosophical Frameworks:**
- Deontological ethics (rule-based moral reasoning)
- Utilitarian/consequentialist ethics
- Personal vs. impersonal moral dilemma distinction (Greene et al.)
- Ethical preamble framing (explicit normative framing)

**Dataset Details:**
- Series of moral dilemmas, both personal and impersonal
- Three experimental conditions: no rule preamble, deontological preamble, utilitarian preamble
- Logistic regression analysis of moral reasoning patterns

**LLMs Tested:** 7 LLMs: GPT-3, GPT-3.5, GPT-4, GPT-4.1, Claude 3.7 Sonnet, Grok 3, Gemini 2.5 Pro

**Code/Data URLs:** Available via ScienceDirect supplementary materials

**Implementation Readiness:** MEDIUM - Well-defined experimental protocol. Reproducible with described moral dilemma sets and framing conditions.

**Unique Contribution:** Tests whether LLMs have inherent default ethical orientations. Finds GPT-4 and Claude 3.7 Sonnet resist utilitarian framing and remain deontological even under utilitarian prompts - suggesting "ethical personality" persistence. Philosophy-relevant: tests whether models can flexibly adopt different normative frameworks or are locked into one.

---

### Paper 10: AI Language Model Rivals Expert Ethicist in Perceived Moral Expertise

**Full Citation:** [Authors from Kurt Gray Lab]. (2025). AI language model rivals expert ethicist in perceived moral expertise. Scientific Reports, 15. DOI: 10.1038/s41598-025-86510-0.

**DOI/URL:** https://www.nature.com/articles/s41598-025-86510-0

**Philosophical Frameworks:**
- Moral expertise (philosophy: who counts as a moral expert?)
- Moral justification quality (soundness, nuance, thoughtfulness)
- Applied ethics evaluation (real-world moral advice scenarios)

**Dataset Details:**
- Study 1 (n=501): Comparison of GPT moral justifications vs. human-written justifications
- Study 2 (n=900): GPT-4o moral advice vs. NYT "The Ethicist" column advice
- Evaluation criteria: moral soundness, trustworthiness, thoughtfulness, nuance, correctness
- Uses real moral advice scenarios from published ethics columns

**LLMs Tested:** GPT models (GPT-4o specifically in Study 2), compared against American laypeople and professional ethicist

**Code/Data URLs:** Available via Scientific Reports supplementary materials

**Implementation Readiness:** MEDIUM - Novel evaluation paradigm (human perception of moral expertise). Reproducible with standard experimental psychology methods.

**Unique Contribution:** Published in Scientific Reports. Directly tests the philosophical question of AI moral expertise using human perception studies. GPT-4o rated as more moral, trustworthy, thoughtful, and correct than a professional ethicist (NYT "The Ethicist"). Raises profound philosophical questions about the nature of moral expertise.

---

### Paper 11: Investigating Machine Moral Judgement Through the Delphi Experiment (DelphiHYBRID)

**Full Citation:** Jiang, L., Sakaguchi, K., et al. (2025). Investigating machine moral judgement through the Delphi experiment. Nature Machine Intelligence, 7. DOI: 10.1038/s42256-024-00969-6.

**DOI/URL:** https://www.nature.com/articles/s42256-024-00969-6

**Philosophical Frameworks:**
- Bernard Gert's Common Morality (10 moral principles)
- Top-down symbolic moral reasoning + bottom-up neural reasoning (hybrid approach)
- Moral constraint graphs (conflicts between moral factors)
- Rawlsian philosophical foundations

**Dataset Details:**
- DelphiHYBRID system: operationalizes Gert's 10 moral principles as symbolic constraints
- Moral constraint graphs: nodes = judgments from principles or neural model; edges = logical violations (identity, entailment, contradiction)
- Commonsense moral scenarios from Delphi datasets
- Top-down moral principles guide bottom-up commonsense inferences

**LLMs Tested:** Delphi neural model + symbolic hybrid; compared against pure neural approaches

**Code/Data URLs:** https://github.com/liweijiang/delphi

**Implementation Readiness:** MEDIUM-HIGH - Code available on GitHub, published in Nature Machine Intelligence. Unique hybrid architecture.

**Unique Contribution:** Published in Nature Machine Intelligence. Only system to directly operationalize a major philosophical theory (Bernard Gert's Common Morality) as computable constraints. Hybrid symbolic+neural architecture for moral reasoning is a distinctive philosophical AI approach. Shows promise of combining philosophical rigor with ML flexibility.

---

### Paper 12: LLMs on Trial: Evaluating Judicial Fairness for Large Language Models (JudiFair)

**Full Citation:** Hu, Y., Xue, Z., Li, H., Zheng, S., Chen, Q., Wang, S., Zhang, X., Zheng, N., Liu, Y., Ai, Q., Liu, Y., Clarke, C.L.A., & Shen, W. (2025). LLMs on Trial: Evaluating Judicial Fairness for Large Language Models. arXiv:2507.10852.

**DOI/URL:** https://arxiv.org/abs/2507.10852

**Philosophical Frameworks:**
- Distributive justice / procedural justice in law
- Fairness theory (legal philosophy)
- Counterfactual fairness (causal ethics)
- Rawlsian fairness concepts applied to judicial contexts

**Dataset Details:**
- **JudiFair dataset:** 177,100 unique case facts
- 65 labels across 4 fairness categories, 161 corresponding values
- Derived from 1,100 judicial documents (Chinese legal system)
- Counterfactual annotation strategy: systematic attribute alteration while holding other facts constant
- Three evaluation metrics: inconsistency, bias, imbalanced inaccuracy

**LLMs Tested:** 16 LLMs (specific models in full paper)

**Code/Data URLs:** Publicly available toolkit with all datasets and code (CC BY 4.0 license)

**Implementation Readiness:** HIGH - Large dataset, public release, CC BY 4.0, toolkit provided. Note: limited to Chinese legal system context.

**Unique Contribution:** Largest-scale judicial fairness benchmark for LLMs. Operationalizes philosophical fairness concepts (distributive justice, counterfactual fairness) in a concrete legal domain. Reveals pervasive inconsistency, bias, and imbalanced inaccuracy across all 16 tested models.

---

### Paper 13: Metaethical Perspectives on 'Benchmarking' AI Ethics

**Full Citation:** LaCroix, T. & Luccioni, S. (2025). Metaethical perspectives on 'benchmarking' AI ethics. AI and Ethics (Springer). DOI: 10.1007/s43681-025-00703-x.

**DOI/URL:** https://link.springer.com/article/10.1007/s43681-025-00703-x

**Philosophical Frameworks:**
- Metaethics (moral realism vs. anti-realism, moral objectivity)
- Value alignment theory vs. ethics benchmarking
- Consequentialism, deontology, virtue ethics as normative frameworks
- Cultural relativism and moral pluralism

**Dataset Details:**
- Not a benchmark paper per se, but a critical philosophical analysis of WHY benchmarking ethics is fundamentally problematic
- Argues for "values" and "value alignment" over "ethics" as operational concepts
- Proposes alternative evaluation mechanisms

**LLMs Tested:** N/A (theoretical/philosophical paper)

**Code/Data URLs:** N/A

**Implementation Readiness:** LOW (theoretical) but HIGH philosophical value - Provides the metaethical grounding for why and how benchmarks should be designed. Essential reading for benchmark designers.

**Unique Contribution:** Published in AI and Ethics (Springer). The only paper found that addresses the metaethical foundations of AI ethics benchmarking from a professional philosophy perspective. Argues that values are context-dependent and culturally shaped, whereas ethics frameworks claim universality - this tension explains why benchmarks fail. Essential theoretical framework for the entire field.

---

### Paper 14: Building Interpretable Models for Moral Decision-Making

**Full Citation:** Goel, M., Das, A. (Ashoka University), & Chopra, P. (2026). Building Interpretable Models for Moral Decision-Making. arXiv:2602.03351.

**DOI/URL:** https://arxiv.org/abs/2602.03351

**Philosophical Frameworks:**
- Trolley Problem paradigm (moral philosophy)
- Moral Machine experimental ethics framework
- Interpretability as philosophical requirement for moral agency (connected to virtue ethics/phronesis)
- Mechanistic interpretability of moral reasoning

**Dataset Details:**
- Moral Machine dataset: 3 million trolley-problem scenarios, 5.4M total responses, 1.7M unique scenarios
- 23 character types evaluated in paired outcome scenarios
- Custom 104K-parameter transformer model (2-layer, compositional embeddings)
- Four interpretability methods: causal intervention (DoWhy), layer-wise bias localization, circuit probing, gradient-weighted local relevance

**LLMs Tested:** Custom 104K-parameter transformer (demonstrating moral reasoning does not require large models)

**Code/Data URLs:** https://github.com/Lossfunk/modeling-moral-machine

**Implementation Readiness:** HIGH - Code publicly available, large-scale dataset (Moral Machine), well-documented interpretability pipeline.

**Unique Contribution:** From Ashoka University (philosophy-oriented institution). Demonstrates that moral decision-making competence does not require large pretrained models. 77% accuracy on Moral Machine with a tiny 104K-parameter model. Enables mechanistic analysis of HOW moral biases emerge in neural networks layer by layer - connecting to philosophical questions about the nature and origin of moral reasoning.

---

## Summary Table

| # | Paper Name | Venue | Philosophy Framework | Dataset Size | Code Available | Implementation Readiness |
|---|-----------|-------|---------------------|-------------|----------------|------------------------|
| 1 | Convergent Ethics of AI (PRIME) | arXiv 2025 | MFT + Kohlberg + Consequentialism/Deontology | 25 dilemmas, 6 LLMs | No | Medium |
| 2 | MultiTP (Multilingual Trolley) | ICLR 2025 Spotlight | Trolley Problem + Moral Machine | 98,440 vignettes, 107 languages | Yes | **High** |
| 3 | Pluralistic Moral Gap | arXiv 2025 | Moral pluralism, 60-value taxonomy | 1,618 dilemmas + 3,783 value expressions | Pending | Medium-High |
| 4 | TrolleyBench | NeurIPS 2025 Workshop | Trolley Problem + Ethical Consistency | Structured dilemmas + follow-ups | Yes | **High** |
| 5 | MedEthicsQA | arXiv 2025 | Beauchamp & Childress Principalism | 10,974 questions (MCQ + open-ended) | Yes | **High** |
| 6 | PrinciplismQA | arXiv 2025 | Principalism (4 bioethical principles) | 3,648 questions (knowledge + practice) | Pending | Medium-High |
| 7 | Amplified Cognitive Biases (PNAS) | PNAS 2025 | Omission bias, dual-process theory | Moral dilemma experiments | Supplementary | Medium |
| 8 | Robustness in Moral Judgements | Royal Soc. Open Sci. 2025 | Moral Machine + robustness requirement | Moral Machine vignettes + variants | Yes | Medium |
| 9 | Decoding Moral Responses | ScienceDirect 2025 | Deontology vs. Utilitarianism framing | Moral dilemmas x 3 conditions x 7 LLMs | Supplementary | Medium |
| 10 | AI Rivals Expert Ethicist | Scientific Reports 2025 | Moral expertise, moral justification | n=501 + n=900 human eval studies | Supplementary | Medium |
| 11 | DelphiHYBRID (Nature MI) | Nature Machine Intelligence 2025 | Gert's Common Morality (10 principles) | Delphi moral scenario datasets | Yes | Medium-High |
| 12 | JudiFair | arXiv 2025 | Distributive/procedural justice, counterfactual fairness | 177,100 case facts, 65 labels | Yes | **High** |
| 13 | Metaethical Perspectives on Benchmarking | AI and Ethics (Springer) 2025 | Metaethics (realism/anti-realism) | Theoretical | N/A | Low (theoretical) |
| 14 | Interpretable Moral Decision-Making | arXiv 2026 | Trolley Problem + mechanistic interpretability | 3M Moral Machine scenarios | Yes | **High** |

---

## Key Findings and Themes

### 1. Philosophy-First Frameworks Are Now Being Operationalized
Papers 5, 6, and 11 directly operationalize major philosophical theories (Beauchamp & Childress principalism, Bernard Gert's common morality) as computational benchmarks. This represents a significant shift from ad-hoc ethical evaluation to theory-grounded assessment.

### 2. Moral Robustness and Consistency as Philosophical Requirements
Papers 4, 7, 8, and 9 collectively demonstrate that LLMs lack robust, consistent moral reasoning. The Royal Society paper (8) shows that even changing label formatting reverses moral judgments. The PNAS paper (7) discovers amplified omission bias. TrolleyBench (4) quantifies ethical consistency. These findings connect to virtue ethics (stable moral character) and moral competence requirements.

### 3. Pluralistic Moral Values Are Underrepresented
Papers 2, 3, and 13 address moral pluralism from different angles. The Pluralistic Moral Gap (3) shows LLMs use narrower value sets than humans. MultiTP (2) reveals cross-lingual moral alignment variance. The metaethics paper (13) argues that benchmarks fundamentally struggle with value pluralism.

### 4. Knowledge-Practice Gap in Applied Ethics
Papers 5 and 6 reveal that LLMs can "know" ethical principles but fail to "apply" them in practice - a philosophically significant finding connecting to the epistemology distinction between propositional knowledge and practical wisdom (phronesis).

### 5. Medical/Bioethics as a Rich Evaluation Domain
Papers 5 and 6 demonstrate that bioethics provides unusually well-structured evaluation frameworks (principalism's 4 principles) with clear operationalization paths, making it a high-value domain for philosophy-grounded LLM evaluation.

---

## Recommendations for CEI

### Highest Priority for Implementation (Code Available, Large Datasets)
1. **MultiTP** (Paper 2) - 98K vignettes, 107 languages, ICLR spotlight
2. **MedEthicsQA** (Paper 5) - 10,974 questions, principalism framework
3. **JudiFair** (Paper 12) - 177K cases, justice/fairness framework
4. **TrolleyBench** (Paper 4) - Novel consistency metrics, open-source
5. **Building Interpretable Moral Models** (Paper 14) - 3M scenarios, interpretability pipeline

### High Philosophical Value (Theory-Grounded)
6. **DelphiHYBRID** (Paper 11) - Gert's Common Morality operationalized
7. **Pluralistic Moral Gap** (Paper 3) - Dynamic Moral Profiling method
8. **PrinciplismQA** (Paper 6) - Knowledge-practice gap measurement

### Important Methodological Contributions
9. **PNAS Cognitive Biases** (Paper 7) - Omission bias and yes-no bias discovery
10. **Robustness of Moral Judgements** (Paper 8) - Robustness audit methodology
11. **Metaethical Perspectives** (Paper 13) - Theoretical grounding for all benchmarking

---

## Search Coverage

| Search # | Query Focus | Papers Found |
|----------|-------------|--------------|
| 1 | PhilPapers applied ethics AI benchmark | Papers 13, background |
| 2 | Machine ethics evaluation dataset | Background/known |
| 3 | Philosophy & Technology journal | Background |
| 4 | Ethics & Information Technology journal | Paper 13 |
| 5 | Trolley problem LLM benchmark | Papers 2, 4, 14 |
| 6 | Thought experiments moral philosophy | Background |
| 7 | Rawlsian justice LLM evaluation | Paper 12 |
| 8 | Care ethics feminist ethics LLM | Paper 1 (MFT) |
| 9 | Virtue ethics phronesis LLM | Papers 5, 6 (knowledge-practice gap) |
| 10 | Moral realism anti-realism metaethics | Paper 13 |
| 11 | Philosophy AI operationalization benchmark | Papers 10, 11 |
| 12 | Bioethics LLM principalism | Papers 5, 6 |
| 13 | Metaethical benchmarking Springer | Paper 13 |
| 14 | Convergent Ethics moral foundation | Paper 1 |
| 15 | MultiTP multilingual trolley | Paper 2 |
| 16 | Diagnosing Moral Reasoning | Paper 4 |
| 17 | MedEthicsQA principalism | Paper 5 |
| 18 | TrolleyBench ethical consistency | Paper 4 |
| 19 | DelphiHYBRID common morality | Paper 11 |
| 20 | Pluralistic Moral Gap | Paper 3 |
| 21 | PNAS amplified cognitive biases | Paper 7 |
| 22 | Robustness moral judgements Royal Society | Paper 8 |
| 23 | Decoding moral responses | Paper 9 |
| 24 | AI rivals expert ethicist | Paper 10 |
| 25 | JudiFair judicial fairness | Paper 12 |
| 26 | PrinciplismQA knowledge-practice | Paper 6 |
| 27 | Responsible AI measures dataset | Background |

---

*Report generated by Agent 6: PhilPapers + Philosophy Databases Explorer*
*Total NEW papers identified: 14*
*Papers with publicly available code/data: 8 of 14*
*Papers from philosophy-adjacent venues (not CS conferences): 7 of 14*
