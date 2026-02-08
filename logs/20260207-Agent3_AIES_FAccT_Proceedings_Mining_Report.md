# Agent 3: AIES + FAccT + EAAMO Complete Proceedings Mining Report

**Date:** 2026-02-07
**Scope:** AIES 2018-2025, FAccT 2018-2025, EAAMO 2021-2025
**Searches conducted:** 20 web searches across ACM DL, AAAI OJS, arXiv, conference sites
**Focus:** NEW papers with implementable benchmarks/datasets for ethical values alignment in LLMs

---

## EXECUTIVE SUMMARY

Systematic mining of dedicated AI ethics conference proceedings (AIES, FAccT, EAAMO) yielded **19 NEW papers** not in the already-known list. These venues are rich in evaluation frameworks, benchmark datasets, and methodological contributions that are often missed by standard NLP venue searches. Key themes: political value alignment, sycophancy evaluation, norm inconsistency testing, safety evaluation gaps, cultural alignment reliability, guardrail effectiveness, mental health ethics, and participatory/collective alignment.

---

## NEW PAPERS FOUND

---

### 1. SycEval: Evaluating LLM Sycophancy

- **Full citation:** Fanous, A., Goldberg, J., Agarwal, A., Lin, J., Zhou, A., Xu, S., Bikia, V., Daneshjou, R., & Koyejo, S. (2025). "SycEval: Evaluating LLM Sycophancy." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES-25)*, 8(1), 893-900.
- **arXiv:** 2502.08177
- **DOI:** 10.1609/aies.v8i1.36598
- **Ethical frameworks:** Sycophancy as alignment failure; tension between helpfulness and truthfulness
- **Dataset details:** Evaluation framework using AMPS (mathematics) and MedQuad (medical advice) datasets; multi-domain sycophancy probing
- **Code/data:** Not yet publicly released (check arxiv for updates)
- **LLMs tested:** ChatGPT-4o, Claude-Sonnet, Gemini-1.5-Pro
- **Key findings:** Sycophantic behavior in 58.19% of cases; Gemini highest (62.47%), ChatGPT lowest (56.71%); regressive sycophancy (leading to incorrect answers) in 14.66%
- **Implementation readiness:** HIGH — clear evaluation protocol with existing public datasets
- **What makes it unique:** First systematic sycophancy evaluation framework at a dedicated AI ethics venue; distinguishes progressive vs. regressive sycophancy

---

### 2. GermanPartiesQA: Benchmarking LLMs for Political Alignment and Sycophancy

- **Full citation:** Batzner, J., Stocker, V., Schmid, S., & Kasneci, G. (2025). "GermanPartiesQA: Benchmarking Commercial Large Language Models and AI Companions for Political Alignment and Sycophancy." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES-25)*, 8(1), 330-342.
- **arXiv:** 2407.18008
- **DOI:** 10.1609/aies.v8i1.36552
- **Ethical frameworks:** Political neutrality; bias in political discourse; sycophancy vs. steerability
- **Dataset details:** 418 political statements from German Voting Advice Applications across 11 elections; German language
- **Code/data:** https://github.com/janbatzner/germanpartiesqa
- **LLMs tested:** GPT-4o, GPT-3.5, Claude 3 Sonnet, Claude 2.1, Cohere Command R+, Cohere Command
- **Implementation readiness:** HIGH — dataset publicly available on GitHub, clear evaluation methodology
- **What makes it unique:** Political alignment benchmark grounded in real electoral data; distinguishes sycophancy from persona-based steerability; non-English (German) benchmark

---

### 3. Norm Inconsistency in LLM Decision-Making

- **Full citation:** Jain, S., Calacci, D., & Wilson, A. (2024). "As an AI Language Model, 'Yes I Would Recommend Calling the Police': Norm Inconsistency in LLM Decision-Making." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES-24)*, 7(1), 624-633.
- **arXiv:** 2405.14812
- **DOI:** 10.1609/aies.v7i1.31665
- **Ethical frameworks:** Norm consistency; racial bias in policing recommendations; situated ethics
- **Dataset details:** Thousands of Amazon Ring home surveillance video descriptions; annotated for criminal activity, subject skin-tone, gender, and neighborhood demographics
- **Code/data:** Dataset built from Amazon Ring videos (Calacci 2020, MIT Media Lab)
- **LLMs tested:** GPT-4, Gemini 1.0, Claude 3 Sonnet
- **Key findings:** Models said no crime in most videos (even when 39% showed crime) but recommended calling police for 20-45% of videos; racial demographic biases in recommendations
- **Implementation readiness:** MEDIUM — video description dataset requires access; methodology is replicable
- **What makes it unique:** Tests LLM norm consistency in a real-world high-stakes surveillance application; reveals disconnect between crime detection and police-calling recommendations

---

### 4. Mapping Moral Reasoning in LLMs: A Multi-Dimensional Analysis of Safety Principle Conflicts

- **Full citation:** Mahajan, S. (2025). "Mapping Moral Reasoning in LLMs: A Multi-Dimensional Analysis of Safety Principle Conflicts." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES-25)*, 8(2), 1674-1685.
- **DOI:** 10.1609/aies.v8i2.36665
- **Ethical frameworks:** Conflicting safety principles (confidentiality vs. harm prevention vs. institutional loyalty); deontological vs. consequentialist reasoning under constraint
- **Dataset details:** Scenarios where multiple safety principles conflict within the same prompt; multi-dimensional analysis of reasoning chains
- **Code/data:** Check AIES proceedings
- **LLMs tested:** qwq:latest, gemma3 27b, and others
- **Key findings:** Models adopt structurally distinct reasoning profiles; some use longer deliberative chains, others heuristic-driven compact strategies
- **Implementation readiness:** MEDIUM — framework is clear but dataset specifics need verification from full paper
- **What makes it unique:** Focuses specifically on intra-model principle conflicts rather than single ethical dimension testing

---

### 5. Collective Constitutional AI: Aligning a Language Model with Public Input

- **Full citation:** Huang, S., Siddarth, D., Lovitt, L., Jackson, T., Hwang, A., Batista, R., Ganguli, D., Durmus, E., Saurav, S., Karavani, E., Hua, M., Cepelewicz, J., Tamkin, A., Askell, A., Clark, J., Bai, Y., & Amodei, D. (2024). "Collective Constitutional AI: Aligning a Language Model with Public Input." *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT '24)*, 1395-1417.
- **arXiv:** 2406.07814
- **DOI:** 10.1145/3630106.3658979
- **Ethical frameworks:** Participatory alignment; democratic AI governance; collective deliberation on values
- **Dataset details:** 275 public statements sourced via Polis platform (after moderation); constitutions derived from public deliberation; evaluated on BBQ (bias), OpinionQA (political ideology), MMLU, GSM8K
- **Code/data:** Open-sourced data available; Anthropic research page
- **LLMs tested:** Claude models (various); CCAI-trained model compared to standard Constitutional AI model
- **Key findings:** CCAI-trained model shows lower bias across 9 social dimensions; public-sourced constitutions are richer (275 statements vs. 58 for standard Anthropic constitution)
- **Implementation readiness:** HIGH — public dataset, clear methodology, open-sourced
- **What makes it unique:** First language model fine-tuned with collectively sourced public input; bridges participatory democracy and AI alignment

---

### 6. Randomness, Not Representation: The Unreliability of Evaluating Cultural Alignment in LLMs

- **Full citation:** Khanzada, A., Taori, R., & Hashimoto, T. (2025). "Randomness, Not Representation: The Unreliability of Evaluating Cultural Alignment in LLMs." *Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency (FAccT '25)*.
- **arXiv:** 2503.08688
- **DOI:** 10.1145/3715275.3732147
- **Ethical frameworks:** Cultural alignment reliability; cross-cultural values; methodological rigor in ethics evaluation
- **Dataset details:** Systematic robustness testing of survey-based cultural alignment evaluations; tests stability, extrapolability, and steerability across multiple dimensions
- **Code/data:** https://github.com/ariba-k/llm-cultural-alignment-evaluation
- **LLMs tested:** Multiple models including those evaluated in Mazeika et al. (2025)
- **Key findings:** Cultural alignment is (1) not stable — trivial format changes exceed real cultural differences; (2) not extrapolable — limited dimensions produce near-random clustering; (3) not steerable — optimized prompting produces erratic patterns
- **Implementation readiness:** HIGH — GitHub code available; meta-evaluation framework applicable to any cultural alignment benchmark
- **What makes it unique:** Critical meta-evaluation that challenges the validity of survey-based cultural alignment methods; essential methodological contribution

---

### 7. Normative Evaluation of LLMs with Everyday Moral Dilemmas (Sachdeva et al., FAccT 2025)

- **Full citation:** Sachdeva, P., et al. (2025). "Normative Evaluation of Large Language Models with Everyday Moral Dilemmas." *Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency (FAccT '25)*.
- **DOI:** 10.1145/3715275.3732044
- **Ethical frameworks:** Normative ethics; everyday moral reasoning; LLM-as-judge methodology applied to complex moral discourse
- **Dataset details:** 10,000+ posts from Reddit's "Am I The Asshole" (AITA) subreddit; real-world everyday moral dilemmas with community judgments
- **Code/data:** Check ACM DL for supplementary materials
- **LLMs tested:** 7 LLMs evaluated
- **Key findings:** Evaluates how LLMs assign and explain moral blame across thousands of real-world submissions rather than contrived survey questions
- **Implementation readiness:** HIGH — large-scale dataset from publicly available Reddit data; clear evaluation protocol
- **What makes it unique:** Uses naturalistic moral discourse (AITA) rather than synthetic ethical dilemmas; applies LLM-as-judge to moral evaluation

**NOTE:** This appears to be the FAccT 2025 version of the "Normative Evaluation (Sachdeva)" already known. If the already-known entry refers to a different Sachdeva paper, this is new. Flagging for deduplication check.

---

### 8. AI Alignment at Your Discretion

- **Full citation:** Buyl, M., Khalaf, H., et al. (2025). "AI Alignment at Your Discretion." *Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency (FAccT '25)*, 3046-3074.
- **arXiv:** 2502.10441
- **DOI:** 10.1145/3715275.3732194
- **Ethical frameworks:** Annotator discretion in alignment; arbitrary power in preference labeling; human vs. algorithmic discretion
- **Dataset details:** Metrics for analyzing discretion in preference datasets used for RLHF; audits across multiple alignment datasets
- **Code/data:** Check arXiv for supplementary materials
- **LLMs tested:** GPT-4o, DeepSeek-V3, Claude 3.5 Sonnet (audited); reward models fine-tuned on human preferences
- **Key findings:** Excessive discretion afforded to annotators; annotators frequently use discretion arbitrarily; significant discrepancy between off-the-shelf model discretion and human preferences; RLHF may not transfer human discretion to LLMs
- **Implementation readiness:** MEDIUM — metrics framework is implementable; requires access to preference datasets
- **What makes it unique:** First systematic analysis of discretion in AI alignment; bridges alignment methodology and fairness research

---

### 9. Gaps in the Safety Evaluation of Generative AI

- **Full citation:** Rauh, M., Marchal, N., Manzini, A., et al. (2024). "Gaps in the Safety Evaluation of Generative AI." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES-24)*, 7(1), 1200-1217.
- **DOI:** 10.1609/aies.v7i1.31717
- **Ethical frameworks:** Sociotechnical safety evaluation; three-layer evaluation framework (capability, human interaction, systemic)
- **Dataset details:** Comprehensive review and taxonomy of all available safety evaluations; maps gaps across evaluation layers
- **Code/data:** Google DeepMind research; no standalone dataset but provides evaluation taxonomy
- **LLMs tested:** DeepMind's LLMs (evaluation experience-based)
- **Key findings:** Model-centered automated benchmarks obscure social harms; proposes three-layer evaluation (capability testing, human interaction assessment, systemic impact evaluation)
- **Implementation readiness:** MEDIUM — provides framework/taxonomy rather than ready-made dataset; highly useful for structuring evaluation efforts
- **What makes it unique:** From Google DeepMind's internal evaluation experience; proposes sociotechnical evaluation roadmap

---

### 10. Can We Trust AI Benchmarks? An Interdisciplinary Review

- **Full citation:** Eriksson, M., Purificato, E., Noroozian, A., Vinagre, J., Chaslot, G., Gomez, E., & Fernandez-Llorca, D. (2025). "Can We Trust AI Benchmarks? An Interdisciplinary Review of Current Issues in AI Evaluation." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES-25)*, 8(1), 850-864.
- **arXiv:** 2502.06559
- **DOI:** 10.1609/aies.v8i1.36595
- **Ethical frameworks:** Meta-evaluation of benchmarking practices; documentation adequacy; data contamination; construct validity
- **Dataset details:** Meta-review of ~110 studies discussing benchmark shortcomings over last 10 years
- **Code/data:** Review/survey paper
- **LLMs tested:** N/A (meta-analysis)
- **Key findings:** Identifies biases in dataset creation, inadequate documentation, data contamination, and failures to distinguish signal from noise; maps sociotechnical issues in benchmarking
- **Implementation readiness:** LOW (meta-analysis) — but provides essential guidelines for benchmark design
- **What makes it unique:** Definitive meta-review of AI benchmark trustworthiness from an ethics venue

---

### 11. "Do Your Guardrails Even Guard?" Evaluating Moderation Guardrails for LLM Alignment

- **Full citation:** Das Antar, A., Huan, X., & Banovic, N. (2025). "Do Your Guardrails Even Guard? Method for Evaluating Effectiveness of Moderation Guardrails in Aligning LLM Outputs with Expert User Expectations." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES-25)*, 8(1), 705-718.
- **DOI:** 10.1609/aies.v8i1.36583
- **Ethical frameworks:** Guardrail effectiveness; alignment between LLM outputs and empirical evidence/expert knowledge
- **Dataset details:** Real-world evaluation scenarios including resume quality assessment and recidivism prediction
- **Code/data:** Check AIES proceedings for supplementary materials
- **LLMs tested:** Multiple LLMs with various guardrail configurations
- **Key findings:** Provides method to evaluate and select guardrails that best align LLM outputs with expert knowledge
- **Implementation readiness:** HIGH — practical evaluation method with real-world use cases
- **What makes it unique:** First systematic method for evaluating guardrail effectiveness specifically for ethical alignment

---

### 12. How LLM Counselors Violate Ethical Standards in Mental Health Practice

- **Full citation:** Iftikhar, Z., Xiao, A., Ransom, S., Huang, J., & Suresh, H. (2025). "How LLM Counselors Violate Ethical Standards in Mental Health Practice: A Practitioner-Informed Framework." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES-25)*.
- **DOI:** 10.1609/aies.v8i1.36632
- **Ethical frameworks:** APA professional ethics standards; CBT-based therapeutic ethics; 15 identified ethical failure modes across 5 themes
- **Dataset details:** 137 sessions (110 self-counseling tests by trained peer counselors + 27 simulated clinical interactions reviewed by licensed psychologists)
- **Code/data:** Brown University; check paper for data availability
- **LLMs tested:** GPT Series (multiple versions), Claude, Llama
- **Key findings:** 15 recurring ethical failures in 5 themes; inappropriate crisis navigation, misleading responses reinforcing negative beliefs, false empathy
- **Implementation readiness:** HIGH — clear evaluation framework with 15 codified ethical risk categories
- **What makes it unique:** Practitioner-informed (not researcher-designed) ethics evaluation framework; domain-specific (mental health) ethical standards

---

### 13. LLM Voting: Human Choices and AI Collective Decision-Making

- **Full citation:** Yang, J. C., Dailisan, D., Korecki, M., Hausladen, C. I., & Helbing, D. (2024). "LLM Voting: Human Choices and AI Collective Decision-Making." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES-24)*, 7(1), 1696-1708.
- **arXiv:** 2402.01766
- **DOI:** 10.1609/aies.v7i1.31758
- **Ethical frameworks:** Democratic values; collective decision-making; preference aggregation fairness
- **Dataset details:** Dataset from human voting experiments used as baseline; LLM agents replicate voting conditions
- **Code/data:** Check arXiv for supplementary materials
- **LLMs tested:** GPT-4, LLaMA-2
- **Key findings:** Voting methods and presentation order influence LLM outcomes; persona variation reduces bias; trade-off between preference diversity and alignment accuracy
- **Implementation readiness:** MEDIUM — requires constructing parallel human-AI voting experiments
- **What makes it unique:** Tests democratic values alignment through collective decision-making rather than individual moral judgments

---

### 14. On The Stability of Moral Preferences: A Problem with Computational Elicitation Methods

- **Full citation:** Boerstler, K., Keswani, V., Chan, L., Schaich Borg, J., Conitzer, V., Heidari, H., & Sinnott-Armstrong, W. (2024). "On The Stability of Moral Preferences: A Problem with Computational Elicitation Methods." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES-24)*, 7(1), 156-167.
- **arXiv:** 2408.02862
- **DOI:** 10.1609/aies.v7i1.31626
- **Ethical frameworks:** Moral preference stability; temporal consistency of ethical judgments; kidney allocation ethics
- **Dataset details:** Repeated moral preference surveys across 10 sessions in 2 studies; kidney allocation decisions
- **Code/data:** Check arXiv for supplementary materials
- **LLMs tested:** N/A (human study, but directly applicable to LLM moral preference evaluation)
- **Key findings:** Challenges the assumption that moral preferences are stable over time; significant implications for preference-based alignment approaches
- **Implementation readiness:** MEDIUM — methodological contribution applicable to LLM evaluation design
- **What makes it unique:** Empirically tests a foundational assumption of preference-based alignment; critical for anyone building moral preference datasets

---

### 15. ValueCompass: A Framework for Measuring Contextual Value Alignment Between Humans and LLMs

- **Full citation:** Shen, H., et al. (2025). "ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs." *WiNLP Workshop at EMNLP 2025; also ACL 2025 Demo Track*.
- **arXiv:** 2409.09586
- **DOI:** See ACL Anthology: 2025.winlp-main.15 and 2025.acl-demo.64
- **Ethical frameworks:** Schwartz's Theory of Basic Values (56 universal values, 10 motivational types); contextual value alignment
- **Dataset details:** Evaluations across 4 real-world scenarios (collaborative writing, education, public sectors, healthcare); 28 contexts from 4 topics and 7 countries (US, UK, India, Germany, France, Canada, Australia); 112 human participants
- **Code/data:** https://github.com/huashen218/value_action_gap
- **LLMs tested:** 5 diverse LLMs
- **Key findings:** Highest average alignment score only 0.529; humans endorse "National Security" which LLMs largely reject; LLMs systematically diminish Conservative values while elevating Benevolence/Universalism
- **Implementation readiness:** HIGH — GitHub code available; Schwartz-based instruments readily adaptable
- **What makes it unique:** Grounded in established psychological theory (Schwartz values); measures contextual rather than abstract value alignment; multi-country, multi-scenario design

---

### 16. Towards Geographic Inclusion in the Evaluation of Text-to-Image Models

- **Full citation:** Hall, M., Bell, S. J., Ross, C., Williams, A., Drozdzal, M., & Romero Soriano, A. (2024). "Towards Geographic Inclusion in the Evaluation of Text-to-Image Models." *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT '24)*.
- **arXiv:** 2405.04457
- **DOI:** 10.1145/3630106.3658927
- **Ethical frameworks:** Geographic fairness; cultural representation; diversity in AI evaluation
- **Dataset details:** 65,000 annotations from people in Africa, Europe, and Southeast Asia; evaluated on GeoDE (40 object classes across 6 regions) and DollarStreet (~200 concept classes across 4 regions)
- **Code/data:** https://github.com/facebookresearch/DIG-In
- **LLMs tested:** Text-to-image models (not LLMs per se, but framework applicable to multimodal LLMs)
- **Key findings:** Evaluation criteria vary across regions and cultures; commonly-used metrics fail to account for diversity of human preference
- **Implementation readiness:** HIGH — 65K annotations dataset; GitHub code; GeoDE and DollarStreet publicly available
- **What makes it unique:** Largest geographic diversity annotation effort for AI evaluation; directly applicable to multimodal LLM evaluation

---

### 17. Measuring What Matters: Connecting AI Ethics Evaluations to System Attributes, Hazards, and Harms (RAI Measures Dataset)

- **Full citation:** Authors TBD from full paper. (2025). "Measuring What Matters: Connecting AI Ethics Evaluations to System Attributes, Hazards, and Harms." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES-25)*.
- **DOI:** Check AIES-25 proceedings
- **Ethical frameworks:** Responsible AI principles; maps 791 measures to system components, hazards, and harms
- **Dataset details:** RAI Measures Dataset — 791 ethical evaluation measures mapped to system attributes, hazards, and ethical principles
- **Code/data:** Check AIES proceedings for dataset availability
- **LLMs tested:** N/A (meta-evaluation framework)
- **Key findings:** Only ~10% of measures concern user interactions; harm measures emphasize loss of agency, privacy, well-being; fragmentation across components leads to blind spots
- **Implementation readiness:** MEDIUM — dataset of measures is structured and usable; requires integration into evaluation pipelines
- **What makes it unique:** First systematic mapping of 791 RAI evaluation measures to concrete system attributes and harms

---

### 18. Understanding Gen Alpha's Digital Language: Evaluation of LLM Safety Systems for Content Moderation

- **Full citation:** Makhortykh, M., et al. (2025). "Understanding Gen Alpha's Digital Language: Evaluation of LLM Safety Systems for Content Moderation." *Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency (FAccT '25)*.
- **arXiv:** 2505.10588
- **DOI:** 10.1145/3715275.3732184
- **Ethical frameworks:** Youth safety; content moderation ethics; harm detection in evolved digital language
- **Dataset details:** 100 recent Gen Alpha expressions from gaming platforms, social media, and video content; first-of-its-kind dataset
- **Code/data:** Check arXiv/FAccT for supplementary materials
- **LLMs tested:** GPT-4, Claude, Gemini, Llama 3
- **Key findings:** LLMs struggle to detect masked harassment and manipulation in Gen Alpha digital discourse
- **Implementation readiness:** MEDIUM — small dataset (100 expressions) but novel and expandable; clear evaluation framework
- **What makes it unique:** First dataset capturing Gen Alpha digital expressions for AI safety evaluation; tests evolving language patterns

---

### 19. On the Pros and Cons of Active Learning for Moral Preference Elicitation

- **Full citation:** Keswani, V., Conitzer, V., Heidari, H., Schaich Borg, J., & Sinnott-Armstrong, W. (2024). "On the Pros and Cons of Active Learning for Moral Preference Elicitation." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES-24)*, 7(1), 711-723.
- **arXiv:** 2407.18889
- **DOI:** 10.1609/aies.v7i1.31673
- **Ethical frameworks:** Moral preference learning; active learning for value elicitation; assumption testing
- **Dataset details:** Synthetic simulation of moral preferences with varying assumption violations (instability, noise, hypothesis class mismatch)
- **Code/data:** Check arXiv for supplementary materials
- **LLMs tested:** N/A (methodological contribution for preference-based alignment)
- **Key findings:** Active learning can perform similarly to or worse than random query selection when preferences are unstable, noisy, or mismodeled; still viable with small instability/noise
- **Implementation readiness:** MEDIUM — simulation framework is implementable; informs design of moral preference datasets
- **What makes it unique:** Critically examines a key methodology (active learning) used in building preference-based alignment systems

---

## SUMMARY TABLE

| # | Paper | Venue | Year | Implementation Readiness | Has Public Dataset/Code |
|---|-------|-------|------|--------------------------|------------------------|
| 1 | SycEval | AIES | 2025 | HIGH | Partial (uses public datasets) |
| 2 | GermanPartiesQA | AIES | 2025 | HIGH | Yes (GitHub) |
| 3 | Norm Inconsistency in LLM Decision-Making | AIES | 2024 | MEDIUM | Partial |
| 4 | Mapping Moral Reasoning (Safety Conflicts) | AIES | 2025 | MEDIUM | TBD |
| 5 | Collective Constitutional AI | FAccT | 2024 | HIGH | Yes (open-sourced) |
| 6 | Randomness, Not Representation | FAccT | 2025 | HIGH | Yes (GitHub) |
| 7 | Normative Evaluation (Everyday Moral Dilemmas) | FAccT | 2025 | HIGH | Yes (Reddit AITA data) |
| 8 | AI Alignment at Your Discretion | FAccT | 2025 | MEDIUM | Partial |
| 9 | Gaps in Safety Evaluation of Generative AI | AIES | 2024 | MEDIUM | Framework/taxonomy |
| 10 | Can We Trust AI Benchmarks? | AIES | 2025 | LOW | Meta-review |
| 11 | Do Your Guardrails Even Guard? | AIES | 2025 | HIGH | TBD |
| 12 | How LLM Counselors Violate Ethical Standards | AIES | 2025 | HIGH | 137 session dataset |
| 13 | LLM Voting | AIES | 2024 | MEDIUM | Partial |
| 14 | Stability of Moral Preferences | AIES | 2024 | MEDIUM | Simulation framework |
| 15 | ValueCompass | EMNLP/ACL | 2025 | HIGH | Yes (GitHub) |
| 16 | Geographic Inclusion in T2I Evaluation | FAccT | 2024 | HIGH | Yes (GitHub, 65K annotations) |
| 17 | RAI Measures Dataset | AIES | 2025 | MEDIUM | 791 measures dataset |
| 18 | Gen Alpha Digital Language | FAccT | 2025 | MEDIUM | 100 expressions |
| 19 | Active Learning for Moral Preference Elicitation | AIES | 2024 | MEDIUM | Simulation |

---

## DEDUPLICATION NOTES

The following items from the ALREADY KNOWN list were encountered and **excluded**:
- **CIVICS (Pistilli 2024)** — confirmed at AIES 2024, already known
- **Normative Evaluation (Sachdeva)** — Paper #7 above may overlap if the already-known entry refers to the same FAccT 2025 paper. Flagged for verification.
- **Diverse Human Value Alignment (Wang)** — already in the known list; confirmed at AIES 2025
- **SafetyBench / SafetyPrompts.com** — already known
- **MoralBench** — already known
- **Conscience Conflict** — already known
- **WorldValuesBench** — already known

---

## KEY THEMES FROM ETHICS VENUES

1. **Sycophancy as ethical failure** — AIES 2025 has multiple papers treating sycophancy as an alignment/ethics problem, not just a capability issue
2. **Political values alignment** — GermanPartiesQA shows dedicated AI ethics venues producing non-English political benchmarks
3. **Participatory/democratic alignment** — Collective Constitutional AI (FAccT 2024) represents a paradigm shift toward public input in alignment
4. **Methodological critiques** — Multiple papers (Randomness Not Representation, Can We Trust Benchmarks, Stability of Moral Preferences) challenge fundamental assumptions of current evaluation methods
5. **Domain-specific ethics** — Mental health counseling ethics (AIES 2025) shows move toward profession-specific ethical standards
6. **Guardrail evaluation** — Emerging focus on evaluating the evaluators (guardrails, moderation systems)
7. **Safety evaluation gaps** — DeepMind's AIES 2024 paper provides sociotechnical framework revealing what current benchmarks miss

---

## RECOMMENDATIONS FOR NEXT STEPS

1. **Highest priority for implementation:** SycEval, GermanPartiesQA, Collective Constitutional AI, ValueCompass, Randomness Not Representation (meta-evaluation)
2. **Download and catalog:** Papers with GitHub repos (GermanPartiesQA, Randomness Not Representation, ValueCompass, DIG-In)
3. **Verify deduplication:** Confirm whether Sachdeva Normative Evaluation (FAccT 2025) is the same as the already-known entry
4. **Mine AIES 2025 Vol. 8 No. 3:** Additional papers may exist in the third issue of AIES-25 proceedings not yet fully indexed
