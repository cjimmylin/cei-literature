# Agent 12-13: East/South Asian Ethics + Multilingual Moral Evaluation Report

**Agent Role:** Buddhist/Hindu/Confucian/East Asian Ethics + Multilingual Moral Evaluation
**Date:** 2026-02-07
**Search Queries Executed:** 17
**New Papers Found:** 16 (not in the known list of ~90+ prior papers)

---

## EXECUTIVE SUMMARY

This report identifies 16 new papers with implementable benchmarks, datasets, or evaluation frameworks for ethical values alignment in LLMs, focused on (A) East/South Asian ethical traditions and (B) multilingual moral evaluation. All papers listed below are NOT in the excluded known-papers list. The findings reveal a rapidly growing literature on cross-cultural and multilingual moral evaluation of LLMs, with notable gaps remaining in dedicated Buddhist, Hindu, and Daoist AI ethics benchmarks.

---

## SECTION A: EAST/SOUTH ASIAN ETHICAL TRADITIONS

---

### Paper 1: JETHICS -- Japanese Ethics Understanding Evaluation Dataset

**Full Citation:** Takeshita, M., & Rzepka, R. (2025). JETHICS: Japanese Ethics Understanding Evaluation Dataset. arXiv:2506.16187.

**arXiv/DOI:** https://arxiv.org/abs/2506.16187

**Framework:** Normative ethical theories (utilitarianism, virtue ethics, deontology, justice) adapted for Japanese cultural contexts plus commonsense morality.

**Dataset Details:**
- **Size:** 77,896 total examples
- **Format:** Categorized moral scenarios with labels; evaluated via 8-shot prompting on 1,000 randomly selected examples per category
- **Breakdown:** Utilitarianism (19,529), Virtue Ethics (19,920), Commonsense Morality (19,963), Justice-Desert (5,276), Justice-Impartiality (5,260), Deontology-Role (4,940), Deontology-Request (3,008)
- **Languages:** Japanese
- **Creation:** Crowdworker-generated scenarios validated by multiple annotators via majority voting

**LLMs Tested:** llm-jp-3-3.7b, llm-jp-3-13b, Meta-Llama-3-8B, Llama-3-ELYZA-JP-8B, GPT-4o, GPT-4o-mini

**Key Results:** GPT-4o achieved ~0.7 average accuracy; top Japanese LLMs reached ~0.5, indicating substantial room for improvement in Japanese ethics understanding.

**Implementation Readiness:** HIGH -- Large dataset, well-structured categories, clear evaluation methodology.

**Unique Contribution:** First large-scale, multi-theory Japanese ethics evaluation dataset covering utilitarianism, virtue ethics, deontology, and justice simultaneously.

---

### Paper 2: Extended Japanese Commonsense Morality Dataset (eJCM)

**Full Citation:** Ohashi, T., Nakagawa, T., & Iyatomi, H. (2024). Extended Japanese Commonsense Morality Dataset with Masked Token and Label Enhancement. In *Proceedings of CIKM '24*, October 21--25, 2024.

**DOI:** https://dl.acm.org/doi/10.1145/3627673.3679924 | arXiv: https://arxiv.org/abs/2410.09564

**Framework:** Commonsense morality evaluation with Masked Token and Label Enhancement (MTLE) data augmentation.

**Dataset Details:**
- **Size:** 31,184 sentences (expanded from 13,975 original JCommonsenseMorality sentences)
- **Format:** Binary moral judgment sentences (acceptable/unacceptable)
- **Languages:** Japanese
- **Method:** MTLE strategically obscures morally-significant sentence components and replaces them with LLM-generated alternatives while reassigning classifications

**LLMs Tested:** Various Japanese LLMs; benchmarked against GPT-4 Turbo (0.787 F1)

**Key Results:** eJCM model achieved F1 of 0.857 (vs. 0.837 original JCM, 0.850 AugGPT); on Japanese culture-specific tasks improved from 0.681 to 0.756.

**Implementation Readiness:** HIGH -- Published at CIKM, well-validated augmentation methodology.

**Unique Contribution:** Demonstrates a scalable augmentation method for expanding culture-specific moral datasets.

---

### Paper 3: Does Cross-Cultural Alignment Change the Commonsense Morality of Language Models?

**Full Citation:** Jinnai, Y. (2024). Does Cross-Cultural Alignment Change the Commonsense Morality of Language Models? In *Proceedings of the 2nd Workshop on Cross-Cultural Considerations in NLP (C3NLP) at ACL 2024*.

**Venue:** C3NLP Workshop, ACL 2024

**Framework:** Cross-cultural preference alignment evaluation using JCommonsenseMorality (JCM) vs. ETHICS datasets.

**Dataset Details:**
- **Datasets used:** JCommonsenseMorality (Japanese), ETHICS (English)
- **Languages:** Japanese, English
- **Format:** Comparative fine-tuning evaluation

**LLMs Tested:** Japanese language models (SFT baseline vs. English-aligned vs. Japanese-aligned variants)

**Key Results:** Models aligned with English-translated JCM achieved higher accuracy than those aligned with Japanese-translated ETHICS, suggesting cultural differences are harder to transfer than language differences.

**Implementation Readiness:** MEDIUM -- Framework paper with actionable methodology; relies on existing datasets.

**Unique Contribution:** First systematic study showing that cross-cultural alignment transfers some but not all moral commonsense, with language being easier to bridge than culture.

---

### Paper 4: Analyzing the Safety of Japanese Large Language Models in Stereotype-Triggering Prompts

**Full Citation:** Nakanishi, A., Sano, Y., Liu, G., & Pierri, F. (2025). Analyzing the Safety of Japanese Large Language Models in Stereotype-Triggering Prompts. arXiv:2503.01947. Submitted to IEEE Transactions on Artificial Intelligence.

**arXiv/DOI:** https://arxiv.org/abs/2503.01947

**Framework:** Safety and stereotype evaluation for Japanese LLMs using bias-triggering prompt templates.

**Dataset Details:**
- **Size:** 3,612 prompts (301 social group terms x 12 stereotype-inducing templates)
- **Format:** Open-ended response evaluation (not binary choice)
- **Languages:** Japanese (with English and Chinese model comparisons)

**LLMs Tested:** LLM-jp (Japanese-native), plus English-trained and Chinese-trained foundational models

**Key Results:** Japanese LLMs refused biased responses at only 0.3% (vs. 12.2% English, 29.3% Chinese), with all models generating toxic responses toward specific social groups.

**Implementation Readiness:** HIGH -- Clear prompt-based methodology, quantitative metrics for refusal rate and toxicity.

**Unique Contribution:** First systematic safety evaluation of Japanese LLMs revealing critically insufficient ethical safety mechanisms compared to English/Chinese counterparts.

---

### Paper 5: Decolonial AI Alignment -- Openness, Visesa-Dharma, and Including Excluded Knowledges

**Full Citation:** Varshney, K. R. (2024). Decolonial AI Alignment: Openness, Visesa-Dharma, and Including Excluded Knowledges. In *Proceedings of the 2024 AAAI/ACM Conference on AI, Ethics, and Society (AIES '24)*.

**arXiv/DOI:** https://arxiv.org/abs/2309.05030 | https://ojs.aaai.org/index.php/AIES/article/view/31739

**Framework:** Hindu philosophical concept of visesa-dharma (context-specific notions of right and wrong) applied to decolonial AI alignment. Three forms of openness: model openness, societal openness, openness to excluded knowledges.

**Dataset Details:**
- **Type:** Theoretical/framework paper (no standalone dataset)
- **Contribution:** Proposes using Hindu argumentative moral philosophy as alternative to Western moral absolutism in LLM alignment

**Key Concepts:** Visesa-dharma vs. sadharana-dharma; Hinduism as "open-source religion"; colonialism recapitulated in LLM alignment practices.

**Implementation Readiness:** LOW-MEDIUM -- Theoretical framework; no implementable dataset but provides actionable philosophical grounding for building Hindu-ethics-informed benchmarks.

**Unique Contribution:** First peer-reviewed paper at a top venue applying Hindu moral philosophy (visesa-dharma) to critique and reformulate LLM alignment as a decolonial project.

---

### Paper 6: Fluent but Foreign -- Even Regional LLMs Lack Cultural Alignment

**Full Citation:** Agarwal, D., Shukla, A., Sitaram, S., & Vashistha, A. (2025). Fluent but Foreign: Even Regional LLMs Lack Cultural Alignment. arXiv:2505.21548. Under review.

**arXiv/DOI:** https://arxiv.org/abs/2505.21548

**Framework:** Two-dimensional cultural alignment evaluation (values + practices) using nationally representative surveys and community-sourced QA datasets, with India as focal case study.

**Dataset Details:**
- **Format:** Four complementary population-scale benchmarks; user study with 115 Indian participants
- **Languages:** Multiple Indic languages
- **Evaluation dimensions:** Values (survey-grounded) and Practices (community QA)

**LLMs Tested:** 12 models total -- 6 Indic LLMs and 6 global LLMs

**Key Results:** A U.S. respondent is a closer proxy for Indian values than any Indic model. Indic models are linguistically fluent but culturally Western. Standard remediation (prompting, fine-tuning) proved ineffective.

**Implementation Readiness:** HIGH -- Reusable, community-grounded methodology; multiple benchmark types.

**Unique Contribution:** First systematic evidence that regional/sovereign LLMs trained on local languages still fail at cultural alignment, with a reusable evaluation framework for South Asian contexts.

---

### Paper 7: How AI Trained on the Confucian Analects Can Solve Ethical Dilemmas

**Full Citation:** So, E. (2024). How AI Trained on the Confucian Analects Can Solve Ethical Dilemmas. PhilArchive.

**URL:** https://philarchive.org/rec/SOHATI

**Framework:** Confucian virtue ethics (ren/benevolence) applied to AI chatbot design, using passages from the Analects as algorithmic training material.

**Dataset Details:**
- **Type:** Theoretical/proposal paper with practical application demonstration (psychology AI chatbots)
- **Source text:** Confucian Analects passages
- **Languages:** English (with Classical Chinese source texts)

**Implementation Readiness:** LOW -- Conceptual framework; no formal dataset or benchmark, but proposes a concrete approach for incorporating Confucian virtue ethics into AI systems.

**Unique Contribution:** Proposes a specific methodology for incorporating Analects passages into AI training to reduce Eurocentric bias using Eastern virtue ethics.

---

## SECTION B: MULTILINGUAL MORAL EVALUATION

---

### Paper 8: CARE -- Multilingual Human Preference Learning for Cultural Awareness

**Full Citation:** Guo, G., Naous, T., Wakaki, H., Nishimura, Y., Mitsufuji, Y., Ritter, A., & Xu, W. (2025). CARE: Multilingual Human Preference Learning for Cultural Awareness. In *Proceedings of EMNLP 2025*. arXiv:2504.05154.

**arXiv/DOI:** https://arxiv.org/abs/2504.05154

**Framework:** Multilingual culture-specific preference learning using DPO/KTO/SimPO alignment across five cultural dimensions: cultural entities, cultural commonsense, social norms, opinions, and literacy.

**Dataset Details:**
- **Size:** 3,490 culturally specific questions + 31,700 LLM/human-written responses with human preference judgments
- **Format:** Question-response pairs with native-speaker preference annotations
- **Languages/Cultures:** Chinese, Arabic, Japanese
- **Collection:** Manual identification of culturally-relevant queries from instruction tuning datasets; supplemented by native speakers with overseas experience

**LLMs Tested:** Qwen2.5-7B, Gemma2-9B (among others)

**Code/Data URLs:** GitHub (referenced as public release with EMNLP 2025 acceptance)

**Key Results:** Even 25% of CARE achieves 74% improvement; cross-culture synergy exists (mixing local/foreign culture samples improves local cultural awareness).

**Implementation Readiness:** HIGH -- Large annotated dataset, published at EMNLP 2025, covers key East Asian + Arabic cultures.

**Unique Contribution:** First large-scale multilingual preference learning dataset specifically designed for cultural awareness, with novel findings on cross-culture synergy effects.

---

### Paper 9: Whose Morality Do They Speak? Unraveling Cultural Bias in Multilingual Language Models

**Full Citation:** Aksoy, M. (2024). Whose Morality Do They Speak? Unraveling Cultural Bias in Multilingual Language Models. arXiv:2412.18863. Published in *Information Processing and Management* (Elsevier), 2025.

**arXiv/DOI:** https://arxiv.org/abs/2412.18863 | https://www.sciencedirect.com/science/article/pii/S2949719125000482

**Framework:** Moral Foundations Questionnaire 2 (MFQ-2) applied across eight languages; six moral foundations: care, equality, proportionality, loyalty, authority, purity.

**Dataset Details:**
- **Format:** MFQ-2 questionnaire administered in 8 languages
- **Languages:** Arabic, Farsi, English, Spanish, Japanese, Chinese, French, Russian
- **Evaluation:** Comparative analysis of moral foundation scores across languages

**LLMs Tested:** GPT-3.5-Turbo, GPT-4o-mini, Llama 3.1, MistralNeMo

**Key Results:** Significant cultural and linguistic variability in moral foundations; English-centric training data creates bias favoring English moral norms.

**Implementation Readiness:** HIGH -- Uses established psychological instrument (MFQ-2); reproducible methodology; 8 languages including 3 East Asian languages.

**Unique Contribution:** First systematic application of MFQ-2 across eight languages to evaluate moral foundations in multilingual LLMs.

---

### Paper 10: One Model, Many Morals -- Uncovering Cross-Linguistic Misalignments in Computational Moral Reasoning

**Full Citation:** Farid, S., Lin, J., Chen, Z., Kumar, S., & Jurgens, D. (2025). One Model, Many Morals: Uncovering Cross-Linguistic Misalignments in Computational Moral Reasoning. arXiv:2509.21443.

**arXiv/DOI:** https://arxiv.org/abs/2509.21443

**Framework:** Translation of two established moral reasoning benchmarks into five typologically diverse languages; zero-shot multilingual evaluation with structured typology of moral reasoning errors.

**Dataset Details:**
- **Format:** Translated moral reasoning benchmarks; 22 pages, 11 figures, 6 tables
- **Languages:** Five culturally and typologically diverse languages
- **Method:** Zero-shot evaluation with qualitative analysis of reasoning strategies

**Key Results:** Significant inconsistencies in moral judgments across languages reflecting cultural misalignment; identifies drivers of disparities ranging from disagreements to reasoning strategy differences.

**Implementation Readiness:** MEDIUM-HIGH -- Systematic methodology with error typology; builds on established benchmarks.

**Unique Contribution:** First structured typology of moral reasoning errors in cross-linguistic LLM evaluation; case study linking pretraining data composition to moral misalignment.

---

### Paper 11: Exploring Cultural Variations in Moral Judgments with Large Language Models

**Full Citation:** Mohammadi, H., & Bagheri, A. (2025). Exploring Cultural Variations in Moral Judgments with Large Language Models. arXiv:2506.12433.

**arXiv/DOI:** https://arxiv.org/abs/2506.12433

**Code/Data URL:** https://github.com/mohammadi-hadi/cultural-moral-judgments-llms

**Framework:** Log-probability-based moral justifiability scoring compared against World Values Survey (WVS) and Pew Research Center Global Attitudes Survey data spanning 55+ countries.

**Dataset Details:**
- **Format:** Structured probing prompts with contrasting moral statements; log-probability scoring
- **Languages:** Multiple (corresponding to WVS countries)
- **Coverage:** 55+ countries from WVS and Pew surveys

**LLMs Tested:** GPT-2, OPT, BLOOMZ, Qwen (smaller models); GPT-4o, GPT-4o-mini, Gemma-2-9b-it, Llama-3.3-70B-Instruct (advanced models)

**Key Results:** Advanced instruction-tuned models achieve substantially higher positive correlations with human moral judgments; all models align better with W.E.I.R.D. nations than non-Western regions.

**Implementation Readiness:** HIGH -- Code available on GitHub; uses established survey instruments; covers 55+ countries.

**Unique Contribution:** Largest-scale comparison of LLM moral judgments against ground-truth human survey data from WVS/Pew, with explicit W.E.I.R.D. bias quantification.

---

### Paper 12: Decoding Multilingual Moral Preferences -- Unveiling LLM's Biases Through the Moral Machine Experiment

**Full Citation:** Vida, K., Damken, F., & Lauscher, A. (2024). Decoding Multilingual Moral Preferences: Unveiling LLM's Biases Through the Moral Machine Experiment. In *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES '24)*, 7(1), 1490--1501.

**arXiv/DOI:** https://arxiv.org/abs/2407.15184 | https://ojs.aaai.org/index.php/AIES/article/view/31741

**Framework:** Moral Machine Experiment scenarios adapted for multilingual LLM evaluation across 10 languages.

**Dataset Details:**
- **Size:** 6,500 moral dilemma scenarios
- **Format:** Trolley-problem-style moral dilemmas from Moral Machine
- **Languages:** 10 languages

**LLMs Tested:** Falcon, Gemini, Llama, GPT, MPT (5 models)

**Key Results:** All LLMs exhibit different moral biases; Llama 3 diverges greatly from human values, preferring to save fewer people; significant cross-linguistic inconsistencies within models.

**Implementation Readiness:** HIGH -- Published at AIES 2024; well-defined scenarios; 10 languages.

**Unique Contribution:** First multilingual analysis of moral bias in complex moral dilemmas (not just atomic actions) across 10 languages and 5 LLM families.

---

### Paper 13: Ethical Reasoning and Moral Value Alignment of LLMs Depend on the Language We Prompt Them In

**Full Citation:** Agarwal, U., Tanmay, K., Khandelwal, A., & Choudhury, M. (2024). Ethical Reasoning and Moral Value Alignment of LLMs Depend on the Language We Prompt Them In. In *Proceedings of LREC-COLING 2024*, pp. 6330--6340.

**arXiv/DOI:** https://arxiv.org/abs/2404.18460 | https://aclanthology.org/2024.lrec-main.560/

**Framework:** Three branches of normative ethics (deontology, virtue ethics, consequentialism) evaluated across six languages using ethical dilemmas and policies.

**Dataset Details:**
- **Format:** Ethical dilemma prompts and policy scenarios
- **Languages:** English, Spanish, Russian, Chinese, Hindi, Swahili
- **Evaluation:** Consistency of moral judgments across languages and ethical frameworks

**LLMs Tested:** GPT-4, ChatGPT, Llama2-70B-Chat

**Key Results:** GPT-4 is the most consistent ethical reasoner across languages; ChatGPT and Llama2-70B-Chat show significant moral value bias in non-English languages; bias nature varies significantly across languages.

**Implementation Readiness:** HIGH -- Published at LREC-COLING 2024; clear evaluation methodology; includes Hindi and Chinese (South/East Asian).

**Unique Contribution:** First systematic study of how prompting language affects ethical reasoning across three normative ethics branches, with specific evidence for Hindi and Chinese.

---

### Paper 14: Cross-Linguistic Moral Preferences in LLMs -- Evidence from Distributive Justice Scenarios and Domain Persona Interventions

**Full Citation:** [Authors not fully retrieved]. (2024). Cross-Linguistic Moral Preferences in Large Language Models: Evidence from Distributive Justice Scenarios and Domain Persona Interventions. *Electronics*, 14(24), 4919. MDPI.

**DOI:** https://www.mdpi.com/2079-9292/14/24/4919

**Framework:** Distributive justice scenarios with domain persona interventions to evaluate cross-linguistic moral preferences.

**Dataset Details:**
- **Size:** 1,201,200 observations across ten professional domains
- **Format:** Distributive justice scenarios with domain persona prompting (sociology, economics, law, philosophy, etc.)
- **Languages:** English, Korean

**LLMs Tested:** Gemini 2.0 Flash

**Key Results:** Five of six scenarios showed significant language effects (9--56 percentage point gaps), including complete preference reversals. Domain persona injection reduces gaps by 62.7% on average.

**Implementation Readiness:** HIGH -- Large observation count; clear mitigation strategy (persona injection); English-Korean cross-linguistic focus.

**Unique Contribution:** First study of distributive justice-specific moral preferences in LLMs with a novel persona-based mitigation technique; largest observation count for Korean moral evaluation.

---

### Paper 15: An Evaluation of Cultural Value Alignment in LLM

**Full Citation:** Sukiennik, N., Gao, C., Xu, F., & Li, Y. (2025). An Evaluation of Cultural Value Alignment in LLM. arXiv:2504.08863. Submitted to COLM 2025.

**arXiv/DOI:** https://arxiv.org/abs/2504.08863

**Framework:** Cultural values questionnaire applied across 20 countries and 10 LLMs -- described as the first large-scale evaluation of LLM cultural alignment.

**Dataset Details:**
- **Format:** Validated cultural values questionnaire with human ground truth
- **Languages:** Multiple (corresponding to 20 countries assessed)
- **Coverage:** 20 countries, 10 LLMs

**LLMs Tested:** 10 models including GLM-4 (identified as best at adapting to cultural values)

**Key Results:** Models produce outputs representing "moderate cultural middle ground"; U.S. has strongest alignment; all models align better with U.S. than China regardless of model origin; GLM-4 performs best at adapting.

**Implementation Readiness:** HIGH -- Large-scale systematic evaluation; 20 countries; 10 models; clear alignment metric.

**Unique Contribution:** Largest multi-country, multi-model cultural value alignment evaluation to date; first evidence that even Chinese-origin models align better with U.S. values.

---

### Paper 16: Mind the Gap -- Pitfalls of LLM Alignment with Asian Public Opinion

**Full Citation:** Shankar, H., S P, V., Margapuri, S., & Mazumder, D. (2025). Mind the Gap: Pitfalls of LLM Alignment with Asian Public Opinion. IIIT Hyderabad / PreCog Lab.

**URL:** https://cdn.iiit.ac.in/cdn/precog.iiit.ac.in/pubs/mind_the_gap_LLM_Alignment_Steerability_Global_South.pdf

**Framework:** Evaluation of LLM alignment with Asian public opinion using Pew Research Center nationally representative surveys and regionally salient cultural datasets, focusing on religion in multilingual/plural societies.

**Dataset Details:**
- **Format:** Survey-based alignment evaluation
- **Languages/Regions:** East Asia (Traditional Chinese, Japanese, Korean, Vietnamese), Southeast Asia (Khmer, Indonesian, Simplified Chinese, Malay, Tamil, Sinhala, Thai), with emphasis on India
- **Cultural focus:** Religion-culture intersection in diverse Asian societies

**LLMs Tested:** Multiple LLMs including Llama variants (specific models in full paper)

**Key Results:** Aligned LLMs agree more closely with USA opinions than Asian public opinion; 2--5% alignment differences between USA and Asian countries; lack of culturally representative data creates large gaps in societal and religious viewpoints.

**Implementation Readiness:** MEDIUM-HIGH -- Survey-based methodology; covers 10+ Asian languages; focused on under-studied Global South populations.

**Unique Contribution:** First study specifically focused on Asian public opinion alignment gaps in LLMs, covering a uniquely broad set of South/Southeast Asian languages and religious/cultural contexts.

---

## SECTION C: SUPPLEMENTARY/CONTEXTUAL FINDINGS

### NORBU (Neural Operator for Responsible Buddhist Understanding)
- **URL:** https://norbu-ai.org/
- **Status:** Buddhist AI chatbot (not a formal benchmark/dataset paper); uses 650+ Pali Tipitaka data sources
- **Relevance:** Potential source for Buddhist ethics training data; not a peer-reviewed benchmark

### GlobalOpinionQA
- **Citation:** Durmus, E., et al. (2023). Towards Measuring the Representation of Subjective Global Opinions in Language Models. arXiv:2306.16388.
- **Dataset:** 2,554 multiple-choice questions from WVS/Pew across 14 countries
- **Status:** Established baseline benchmark (2023); widely used in subsequent work

### LLM Ethics Benchmark (Three-Dimensional)
- **Citation:** Jiao, J., et al. (2025). LLM Ethics Benchmark: A Three-Dimensional Assessment System. *Scientific Reports*. arXiv:2505.00853.
- **GitHub:** The-Responsible-AI-Initiative/LLM_Ethics_Benchmark
- **Note:** English-focused; three dimensions (foundational principles, reasoning robustness, value consistency); not culture-specific but complementary

### CAReDiO
- **Citation:** Yao, J., et al. (2025). CAReDiO: Cultural Alignment of LLM via Representativeness and Distinctiveness Guided Data Optimization. arXiv:2504.08820.
- **Note:** Framework for cultural data construction (not a benchmark per se); achieves alignment with as few as 100 training samples per culture across 5--15 cultures

---

## SYNTHESIS AND GAP ANALYSIS

### Coverage Map by Tradition/Region

| Tradition/Region | Papers Found | Benchmark Readiness |
|---|---|---|
| Japanese Ethics | 4 (JETHICS, eJCM, Cross-Cultural JCM, Safety Stereotypes) | HIGH |
| Indian/Hindu Ethics | 2 (Decolonial Visesa-Dharma, Fluent but Foreign) | LOW-MEDIUM |
| Korean Ethics | 1 (Cross-Linguistic Distributive Justice EN-KO) | MEDIUM |
| Chinese Ethics | Covered indirectly via multilingual papers | MEDIUM |
| Confucian Ethics (dedicated) | 1 (So, Analects -- theoretical) | LOW |
| Buddhist Ethics (dedicated) | 0 formal benchmarks (NORBU is a chatbot, not benchmark) | VERY LOW |
| Daoist Ethics | 0 formal benchmarks | VERY LOW |
| Multilingual Moral Eval | 8 papers | HIGH |
| Asian Public Opinion | 1 (Mind the Gap) | MEDIUM-HIGH |

### Key Gaps Identified

1. **Buddhist Ethics Benchmark:** No formal, peer-reviewed benchmark exists for evaluating LLMs against Buddhist ethical precepts (Five Precepts, Eightfold Path, karuna/compassion, metta). NORBU provides training data but no evaluation framework.

2. **Confucian Ethics Benchmark:** No dedicated computational benchmark evaluates LLMs on Confucian virtues (ren, yi, li, zhi, xin). Emma So's work is theoretical; CDEval (already known) is the closest but is Chinese-culture general.

3. **Hindu/Dharmic Ethics Benchmark:** Varshney's visesa-dharma framework is theoretical. No implementable dataset exists for evaluating LLMs against dharmic principles (karma, ahimsa, dharma, moksha).

4. **Daoist Ethics:** Complete absence of any benchmark or dataset for Daoist ethical evaluation (wu wei, ziran, de).

5. **Southeast Asian Ethics:** Mind the Gap covers survey-level alignment but no dedicated moral reasoning benchmarks exist for Thai, Vietnamese, Indonesian, Filipino ethical traditions.

### Recommendations for Priority Implementation

1. Build a **Buddhist Precepts Benchmark** using Pali Canon/Tipitaka with scenario-based evaluation (leveraging NORBU's 650+ data sources)
2. Create a **Confucian Virtues Assessment** with ren-li-yi scenarios grounded in the Analects and Mencius
3. Develop a **Dharmic Ethics Evaluation** incorporating visesa-dharma (context-specific morality) from the Mahabharata and Bhagavad Gita
4. Expand Japanese benchmarks (JETHICS, eJCM) to cover Shinto ethics and Japanese Buddhist moral philosophy
5. Develop Korean benchmarks beyond KorNAT to cover Neo-Confucian ethical traditions

---

## METHODOLOGY NOTES

- **17 web searches** executed across Buddhist, Hindu, Confucian, Daoist, Japanese, Korean, and multilingual moral evaluation queries
- **Multiple WebFetch calls** to extract detailed paper metadata from arXiv, ACL Anthology, MDPI, PhilArchive, and institutional repositories
- **Exclusion filter** applied against ~90+ known papers from prior agents
- **Date range focus:** 2024--2026 publications
- All papers verified as NOT in the known exclusion list (ETHICS, MoReBench, MoralBench, MoralChoice, Greatest Good, MACHIAVELLI, DailyDilemmas, MORABLES, WorldValuesBench, CultureLLM, CIVICS, LLM-GLOBE, CQ-Bench, MENAValues, IslamTrust, CDEval, CulturalBench, XCR-Bench, ValueBench, NormAd, FLAMES, KorNAT, CMoralEval, MULTITP, UniMoral, Value Compass, PRISM, Eagle, MFTCXplain, Multilingual DIT)

---

*Report generated by Agent 12-13 (Buddhist/Hindu/Confucian/East Asian Ethics + Multilingual Moral Evaluation)*
