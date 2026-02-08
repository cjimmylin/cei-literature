# Agent 4: NeurIPS/ICML/ICLR Workshop Proceedings Explorer
## Report: NEW Papers with Implementable Benchmarks/Datasets for Ethical Values Alignment in LLMs

**Date:** 2026-02-07
**Search scope:** NeurIPS, ICML, ICLR workshop proceedings and Datasets & Benchmarks tracks (2023--2025)
**Searches conducted:** 20 web searches across ML conference workshops, OpenReview, arXiv
**Papers found:** 12 NEW papers (not in the 67 already-known list)

---

## Summary of Search Strategy

| Search Target | Venue/Workshop | Yield |
|---|---|---|
| NeurIPS ML Safety Workshop (2022--2024) | mlsafety.org / NeurIPS | 1 paper |
| NeurIPS SoLaR Workshop 2024 | solar-neurips.github.io | 0 (no specific new benchmark papers surfaced beyond known) |
| NeurIPS Pluralistic Alignment Workshop 2024 | pluralistic-alignment.github.io | 3 papers |
| NeurIPS Datasets & Benchmarks Track 2024 | proceedings.neurips.cc | 4 papers |
| NeurIPS 2025 LLM Evaluation Workshop | openreview.net | 1 paper |
| ICLR 2025 Main Conference | proceedings.iclr.cc | 1 paper |
| ICML 2024 Next Gen AI Safety Workshop | icml-nextgenaisafety.github.io | 0 (no specific new benchmark surfaced) |
| AfricaNLP 2024--2025 | ICLR/ACL workshops | 0 (ethics focus but no specific new benchmark) |
| Muslims in ML Workshop 2024 | musiml.org | 0 (no specific new benchmark) |
| NeurIPS 2025 ResponsibleFM Workshop | responsible-fm.github.io | 0 (future workshop) |
| ICML 2025 R2-FM Workshop | r2-fm.github.io | 0 (future workshop) |
| ICLR 2025 BiAlign Workshop | bialign-workshop.github.io | 0 (position papers, no specific benchmark) |
| Cooperative AI Workshops | cooperativeai.com | 0 |
| Queer in AI / Black in AI / LatinX in AI | Various | 0 (community building focus, no specific benchmarks) |

---

## NEW Paper Findings (12 Papers)

---

### Paper 1: PRISM Alignment Dataset

**Full Citation:**
Kirk, H.R., Vidgen, B., Rottger, P., Hale, S.A. (2024). "The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models." *NeurIPS 2024 Datasets and Benchmarks Track* (Oral / Best Paper Award).

**arXiv/DOI:** arXiv:2404.16019
**URL:** https://arxiv.org/abs/2404.16019

**Framework:**
- Participatory, representative, individualised human feedback methodology
- Two-stage data collection: (1) participant survey on demographics/preferences, (2) live multi-turn conversations with LLMs rated on cardinal scale
- Targets subjective and multicultural perspectives on value-laden and controversial issues

**Dataset Details:**
- 1,500 diverse participants from 75 countries
- 8,011 live conversations with 21 LLMs
- 68,371 utterances (triples of {human message, model response, score})
- Census-representative samples for UK and US
- Detailed participant sociodemographic profiles linked to individualized ratings

**Code/Data URLs:**
- Project page: https://hannahkirk.github.io/prism-alignment/
- Paper: https://proceedings.neurips.cc/paper_files/paper/2024/hash/be2e1b68b44f2419e19f6c35a1b8cf35-Abstract-Datasets_and_Benchmarks_Track.html

**LLMs Tested:** 21 LLMs (specific models include major proprietary and open-source models)

**Implementation Readiness:** HIGH -- Dataset publicly released; formal NeurIPS proceedings publication; best paper award winner; detailed methodology for replication

**Unique Contribution:** First human feedback dataset to explicitly target cross-cultural controversies and value-laden prompts with individualized participant profiles. Enables research on pluralism and disagreements in RLHF by connecting sociodemographic backgrounds to contextual AI preferences.

---

### Paper 2: ALI-Agent -- Assessing LLMs' Alignment with Human Values via Agent-based Evaluation

**Full Citation:**
Zheng, S., Wang, Z., et al. (2024). "ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation." *NeurIPS 2024 Main Conference*.

**arXiv/DOI:** arXiv:2405.14125
**URL:** https://arxiv.org/abs/2405.14125

**Framework:**
- Two-stage agent-based evaluation: (1) Emulation stage -- automated generation of realistic test scenarios; (2) Refinement stage -- iterative refinement to probe long-tail risks
- Memory module for guiding test scenario generation
- Tool-using module to reduce human labor in evaluation
- Action module for test refinement

**Dataset Details:**
- Tests across three aspects of human values: stereotypes (DecodingTrust, CrowS-Pairs), morality (ETHICS, Social Chemistry 101), and legality (Singapore RTSR, AdvBench)
- Dynamically generates new test scenarios rather than relying on static benchmarks

**Code/Data URLs:**
- GitHub: https://github.com/SophieZheng998/ALI-Agent

**LLMs Tested:** Multiple LLMs evaluated across stereotypes, morality, and legality dimensions

**Implementation Readiness:** HIGH -- Official implementation released on GitHub; NeurIPS main conference paper; well-defined agent framework

**Unique Contribution:** First agent-based dynamic evaluation framework for values alignment that generates adaptive test scenarios and probes long-tail risks, overcoming limitations of static benchmarks.

---

### Paper 3: EAI -- Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas

**Full Citation:**
Mozikov, M., et al. (2024). "EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas." *NeurIPS 2024 Main Conference* (Poster).

**arXiv/DOI:** OpenReview ID: 8aAaYEwNR4
**URL:** https://openreview.net/forum?id=8aAaYEwNR4

**Framework:**
- Integrates emotion modeling into LLMs to examine emotional impact on ethics and decision-making
- Evaluates across bargaining games, repeated games, and ethical dilemma scenarios
- Measures how different emotions (anger, fear, joy, etc.) alter ethical decision-making

**Dataset Details:**
- Strategic game scenarios (bargaining, repeated games)
- Ethical dilemma vignettes with emotional modulation
- Multi-turn interaction framework

**Code/Data URLs:**
- GitHub: https://github.com/AIRI-Institute/EAI-Framework

**LLMs Tested:** GPT-4, GPT-3.5, LLAMA2-70b, Openchat-7b

**Implementation Readiness:** HIGH -- Open-source framework on GitHub; NeurIPS proceedings; clear evaluation protocol

**Unique Contribution:** First systematic study of how emotions modulate ethical decision-making in LLMs. Finds that anger and fear significantly increase deflection rates, especially in larger models, revealing that ethical stance is emotion-dependent.

---

### Paper 4: SG-Bench -- Evaluating LLM Safety Generalization

**Full Citation:**
Tom, M., et al. (2024). "SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types." *NeurIPS 2024 Datasets and Benchmarks Track*.

**arXiv/DOI:** arXiv:2410.21965
**URL:** https://arxiv.org/abs/2410.21965

**Framework:**
- Integrates generative AND discriminative evaluation tasks (first to combine both)
- Tests impact of prompt engineering (system prompts, few-shot, chain-of-thought) and jailbreak on safety
- Covers open-end generation, multiple-choice questions, and safety judgment tasks

**Dataset Details:**
- Entries sampled from AdvBench, HarmfulQA, BeaverTails, SaladBench
- Expanded using templates and LLMs
- Multiple prompt type variants for each test item

**Code/Data URLs:**
- GitHub: https://github.com/MurrayTom/SG-Bench
- NeurIPS proceedings: https://proceedings.neurips.cc/paper_files/paper/2024/hash/de7b99107c53e60257c727dc73daf1d1-Abstract-Datasets_and_Benchmarks_Track.html

**LLMs Tested:** 3 proprietary LLMs + 10 open-source LLMs (13 total)

**Implementation Readiness:** HIGH -- GitHub code available; NeurIPS D&B track; standardized evaluation framework

**Unique Contribution:** Reveals that LLMs perform worse on discriminative safety tasks than generative ones; few-shot demonstrations can induce harmful responses; chain-of-thought prompting harms safety on discrimination tasks. Addresses critical gap in understanding safety generalization.

---

### Paper 5: JailbreakBench -- An Open Robustness Benchmark

**Full Citation:**
Chao, P., Robey, A., Dobriban, E., Hassani, H., Pappas, G.J., Wong, E. (2024). "JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models." *NeurIPS 2024 Datasets and Benchmarks Track*.

**arXiv/DOI:** arXiv:2404.01318
**URL:** https://arxiv.org/abs/2404.01318

**Framework:**
- Four components: (1) evolving repository of jailbreak artifacts, (2) JBB-Behaviors dataset, (3) standardized evaluation framework with threat model/scoring, (4) leaderboard for attacks and defenses
- Clearly defined threat model, system prompts, chat templates, and scoring functions

**Dataset Details:**
- JBB-Behaviors: 100 distinct misuse behaviors across 10 categories aligned with OpenAI usage policies
- ~50 original behaviors + ~50 sourced from existing datasets
- Matching benign behaviors for each misuse behavior (sanity check for refusal rates)
- Available on HuggingFace: https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

**Code/Data URLs:**
- GitHub: https://github.com/JailbreakBench/jailbreakbench
- Website: https://jailbreakbench.github.io/

**LLMs Tested:** Multiple LLMs tracked on leaderboard (continuously updated)

**Implementation Readiness:** HIGH -- Fully open-sourced with pip-installable package; live leaderboard; HuggingFace dataset; NeurIPS D&B proceedings

**Unique Contribution:** Standardized, evolving benchmark for jailbreak robustness with matching benign behaviors. Provides the community's first unified framework for comparing attack and defense methods with consistent evaluation protocols.

---

### Paper 6: SaTML LLM CTF Dataset

**Full Citation:**
Debenedetti, E., Severi, G., Carlini, N., Choquette-Choo, C.A., Jagielski, M., Tramèr, F. (2024). "Dataset and Lessons Learned from the 2024 SaTML LLM Capture-the-Flag Competition." *NeurIPS 2024 Datasets and Benchmarks Track*.

**arXiv/DOI:** arXiv:2406.07954
**URL:** https://arxiv.org/abs/2406.07954

**Framework:**
- Two-phase CTF competition: (1) defense phase -- teams build system prompts to prevent secret leakage, (2) attack phase -- teams attempt to extract secrets from other defenses
- Multi-turn adversarial interaction protocol
- Emphasizes adaptive attacks for robustness assessment

**Dataset Details:**
- 137,063 multi-turn attack chats
- Includes defense details, secret strings, model identifiers, attacking team IDs, full message histories
- Available on HuggingFace: https://huggingface.co/datasets/ethz-spylab/ctf-satml24

**Code/Data URLs:**
- HuggingFace: https://huggingface.co/datasets/ethz-spylab/ctf-satml24
- Open-sourced competition platform

**LLMs Tested:** Multiple LLMs used as defense backends during competition

**Implementation Readiness:** HIGH -- Dataset on HuggingFace; open-sourced platform; NeurIPS proceedings

**Unique Contribution:** Largest multi-turn adversarial dataset for LLM safety from a competitive setting. All defenses were bypassed at least once, demonstrating fundamental limitations of prompt-based safety mechanisms and the importance of multi-turn evaluation.

---

### Paper 7: MULTITP -- Language Model Alignment in Multilingual Trolley Problems

**Full Citation:**
Jin, Z., Levine, S., Mihalcea, R., et al. (2024). "Language Model Alignment in Multilingual Trolley Problems." *NeurIPS 2024 Pluralistic Alignment Workshop* (Best Paper Award). arXiv preprint.

**arXiv/DOI:** arXiv:2407.02273
**URL:** https://arxiv.org/abs/2407.02273

**Framework:**
- Cross-lingual moral dilemma evaluation based on the Moral Machine experiment
- Six moral dimensions: species, gender, fitness, status, age, number of lives
- Compares LLM judgments to 40+ million human judgments across 200+ countries

**Dataset Details:**
- 97,520 trolley problem vignettes
- 920 vignettes per language across 107 languages
- Human judgment baselines from the Moral Machine experiment (40M+ judgments, 200+ countries)

**Code/Data URLs:**
- arXiv: https://arxiv.org/abs/2407.02273

**LLMs Tested:** 19 different LLMs evaluated across languages

**Implementation Readiness:** HIGH -- Large-scale dataset; clear evaluation methodology; best paper at NeurIPS workshop; builds on well-established Moral Machine infrastructure

**Unique Contribution:** Largest cross-lingual moral alignment benchmark (107 languages). Reveals significant alignment disparities: LLMs align better with human preferences in English, Korean, Hungarian, Chinese but poorly in Hindi, Somali, highlighting systematic linguistic bias in moral reasoning.

---

### Paper 8: Intuitions of Compromise -- Utilitarianism vs. Contractualism

**Full Citation:**
Moore, J. (2024). "Intuitions of Compromise: Utilitarianism vs. Contractualism." *NeurIPS 2024 Pluralistic Alignment Workshop*. arXiv preprint.

**arXiv/DOI:** arXiv:2410.05496
**URL:** https://arxiv.org/abs/2410.05496

**Framework:**
- Systematic comparison of two value aggregation algorithms: Utilitarian Sum vs. Nash Product (contractualist)
- Social decision-making paradigm with group preference aggregation
- Measures alignment of LLM outputs with human intuitions about fair compromise

**Dataset Details:**
- Controlled social decision-making scenarios
- Human participant judgments on group preference aggregation
- Cases where Utilitarian Sum and Nash Product disagree, enabling direct comparison

**Code/Data URLs:**
- arXiv: https://arxiv.org/abs/2410.05496

**LLMs Tested:** GPT-4, and smaller/less capable models (specific list in paper)

**Implementation Readiness:** MEDIUM -- Clear experimental paradigm; arXiv preprint; presented at NeurIPS workshop; replicable design but dataset may not be fully public yet

**Unique Contribution:** Challenges the dominant utilitarian assumption in AI value aggregation. Finds humans overwhelmingly prefer contractualist (Nash Product) aggregation. GPT-4 partially mirrors this human preference, while smaller models perform at chance -- revealing a fundamental philosophical misalignment in current AI systems.

---

### Paper 9: TrolleyBench -- Evaluating Emergent Moral Reasoning and Consistency in LLMs

**Full Citation:**
[Authors]. (2025). "TrolleyBench: Evaluating Emergent Moral Reasoning and Consistency in LLMs." *NeurIPS 2025 Workshop on LLM Evaluation* (Poster).

**arXiv/DOI:** OpenReview ID: 27j9XJQV5O
**URL:** https://openreview.net/forum?id=27j9XJQV5O

**Framework:**
- First open-source benchmark for ethical consistency evaluation
- Structured diagnostic with clarifying and contradictory follow-ups to moral dilemmas
- Two novel metrics: Ethical Consistency Index (ECI) and entropy-based Inconsistency Score
- Yields quantifiable yes/no responses

**Dataset Details:**
- Trolley-problem-style moral dilemma scenarios
- Multi-turn follow-up questions (clarifying + contradictory)
- Human baselines for comparison
- Open-source release

**Code/Data URLs:**
- OpenReview: https://openreview.net/forum?id=27j9XJQV5O
- Benchmark released publicly

**LLMs Tested:** Deepseek-R1, Mistral Small-32B, Gemini-2.5, GPT-4.1-mini

**Implementation Readiness:** HIGH -- Open-source benchmark; novel metrics; NeurIPS 2025 workshop presentation; publicly available

**Unique Contribution:** First benchmark specifically measuring ethical CONSISTENCY (not just accuracy). Models achieve only middling consistency levels, showing ethical stance is "steerable but fragile." The ECI and Inconsistency Score provide new quantitative tools for measuring moral reasoning stability.

---

### Paper 10: SORRY-Bench -- Systematically Evaluating LLM Safety Refusal

**Full Citation:**
Xie, T., et al. (2025). "SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal." *ICLR 2025* (Conference Paper).

**arXiv/DOI:** arXiv:2406.14598
**URL:** https://arxiv.org/abs/2406.14598

**Framework:**
- Fine-grained taxonomy of 44 potentially unsafe topics
- 20 diverse linguistic mutations (6 writing styles, 5 persuasion techniques, 4 encoding/encryption strategies, 5 non-English languages)
- Meta-evaluation of LLM-as-a-judge designs with 7K+ human annotations

**Dataset Details:**
- 440 class-balanced unsafe instructions (base set)
- 8,800 augmented unsafe instructions (with mutations)
- Train split: 2,640 records for safety evaluator accuracy boosting
- Test split: 4,400 records for evaluating agreement with human annotators
- 44 fine-grained risk categories

**Code/Data URLs:**
- GitHub: https://github.com/SORRY-Bench/sorry-bench
- Website: https://sorry-bench.github.io/
- HuggingFace data available

**LLMs Tested:** 50+ proprietary and open-weight LLMs

**Implementation Readiness:** HIGH -- Fully open-sourced; ICLR 2025 proceedings; pip-installable; comprehensive documentation; leaderboard

**Unique Contribution:** Most granular safety refusal taxonomy (44 categories) with systematic linguistic mutation testing. Demonstrates that fine-tuned 7B LLMs can match GPT-4-scale evaluation accuracy at lower cost, enabling scalable safety evaluation.

---

### Paper 11: Pluralistic Alignment Over Time

**Full Citation:**
[Authors]. (2024). "Pluralistic Alignment Over Time." *NeurIPS 2024 Pluralistic Alignment Workshop*.

**arXiv/DOI:** arXiv:2411.10654
**URL:** https://arxiv.org/abs/2411.10654

**Framework:**
- Introduces temporal pluralism concept: AI systems should reflect different stakeholders' values at different times
- Proposes applying fairness evaluation approaches to temporal aspects of alignment
- Addresses stakeholders' changing satisfaction levels and temporally extended preferences
- Three classes of pluralistic benchmarks: multi-objective, trade-off steerable, jury-pluralistic

**Dataset Details:**
- Conceptual framework paper with benchmark proposals
- Defines evaluation criteria for temporal value alignment

**Code/Data URLs:**
- arXiv: https://arxiv.org/abs/2411.10654
- OpenReview: https://openreview.net/forum?id=BLhVcPbEo8

**LLMs Tested:** Framework/position paper (proposes evaluation methodology)

**Implementation Readiness:** MEDIUM -- Conceptual framework with clear benchmark proposals; requires implementation of specific temporal evaluation protocols

**Unique Contribution:** First paper to formally address the TEMPORAL dimension of values alignment -- how values change over time and how AI systems should adapt. Proposes novel benchmark categories that go beyond static snapshot evaluation.

---

### Paper 12: Measuring What Matters -- Construct Validity in LLM Benchmarks

**Full Citation:**
[Authors]. (2024). "Measuring What Matters: Construct Validity in Large Language Model Benchmarks." *NeurIPS 2024 SoLaR Workshop / Associated Venue*.

**arXiv/DOI:** OpenReview ID: mdA5lVvNcU
**URL:** https://openreview.net/pdf?id=mdA5lVvNcU

**Framework:**
- Applies construct validity theory from psychometrics to LLM benchmark evaluation
- Evaluates whether existing ethics/safety benchmarks actually measure what they claim to measure
- Provides meta-evaluation framework for assessing benchmark quality

**Dataset Details:**
- Meta-analysis of existing LLM benchmarks
- Framework for evaluating construct validity of moral/ethical benchmarks
- Proposes criteria for what constitutes a valid measurement instrument for LLM values

**Code/Data URLs:**
- OpenReview: https://openreview.net/pdf?id=mdA5lVvNcU

**LLMs Tested:** Analysis of benchmark validity across multiple evaluation frameworks

**Implementation Readiness:** MEDIUM -- Conceptual framework for meta-evaluation; applicable to validating any ethics benchmark

**Unique Contribution:** Addresses a foundational methodological gap: most LLM ethics benchmarks lack formal construct validity analysis. Provides psychometric framework for determining whether benchmarks actually capture the ethical constructs they claim to measure.

---

## Cross-Cutting Analysis

### By Venue Distribution
| Venue | Count |
|---|---|
| NeurIPS 2024 Datasets & Benchmarks Track | 4 |
| NeurIPS 2024 Main Conference | 2 |
| NeurIPS 2024 Pluralistic Alignment Workshop | 3 |
| NeurIPS 2025 LLM Evaluation Workshop | 1 |
| ICLR 2025 Main Conference | 1 |
| NeurIPS 2024 SoLaR Workshop | 1 |

### By Implementation Readiness
| Readiness | Papers |
|---|---|
| HIGH (code + data available) | PRISM, ALI-Agent, EAI, SG-Bench, JailbreakBench, SaTML CTF, MULTITP, TrolleyBench, SORRY-Bench |
| MEDIUM (partial availability) | Intuitions of Compromise, Pluralistic Alignment Over Time, Measuring What Matters |

### By Unique Value-Alignment Dimension
| Dimension | Papers |
|---|---|
| Cross-cultural/multilingual moral reasoning | PRISM, MULTITP |
| Dynamic/adaptive evaluation | ALI-Agent |
| Emotion-ethics interaction | EAI |
| Safety generalization across tasks/prompts | SG-Bench, SORRY-Bench |
| Adversarial robustness | JailbreakBench, SaTML CTF |
| Ethical consistency/stability | TrolleyBench |
| Value aggregation philosophy | Intuitions of Compromise |
| Temporal value dynamics | Pluralistic Alignment Over Time |
| Benchmark meta-evaluation | Measuring What Matters |

### Key Gaps Identified
1. **Affinity workshops** (Muslims in ML, Queer in AI, Black in AI, LatinX in AI) focus primarily on community building rather than producing formal benchmarks -- an opportunity for future values-alignment work targeting specific communities.
2. **AfricaNLP workshops** emphasize multilingual NLP but have not yet produced dedicated ethical values benchmarks for African cultural contexts.
3. **Cooperative AI workshops** have focused on game-theoretic cooperation rather than explicit values/ethics benchmarks.
4. **ICML safety workshops** yielded position papers and alignment techniques but few NEW implementable benchmarks beyond those already known.

---

## Recommendations for CEI Integration

1. **Highest priority for implementation:** PRISM (multicultural participatory feedback), MULTITP (107-language moral alignment), SORRY-Bench (fine-grained safety taxonomy), JailbreakBench (standardized jailbreak evaluation)
2. **Novel evaluation dimensions to adopt:** TrolleyBench's Ethical Consistency Index, EAI's emotion-modulated ethics testing, Pluralistic Alignment Over Time's temporal framework
3. **Methodological insights:** Measuring What Matters' construct validity framework should be applied to validate any CEI benchmarks; Intuitions of Compromise challenges utilitarian assumptions prevalent in current alignment work

---

*Report generated: 2026-02-07*
*Agent 4: NeurIPS/ICML/ICLR Workshop Proceedings Explorer*
*Total unique NEW papers identified: 12*
