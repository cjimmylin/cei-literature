# Ethical Values Alignment Benchmarks for LLMs
## Comprehensive Research Report

**Generated:** 2026-02-07
**Scope:** Papers with implementable datasets, benchmarks, code, or evaluation frameworks for assessing LLM alignment with ethical values
**Anchor paper:** Hendrycks et al. (2021) "Aligning AI with Shared Human Values" (ICLR 2021, ~688 citations)

---

## Executive Summary

This report catalogues **35+ papers and resources** providing implementable benchmarks for evaluating ethical values alignment in large language models. The landscape has expanded dramatically since Hendrycks et al. (2021), with major growth in:

1. **Multi-framework ethics benchmarks** — MoReBench (2025) now tests 5 normative frameworks with 1,000 scenarios
2. **Cross-cultural values** — 10+ benchmarks covering 45+ countries, MENA region, Islamic values, and Hofstede dimensions
3. **Moral psychology instruments** — ValueBench covers 453 value dimensions from 44 psychometric inventories
4. **Scaling laws** — Takemoto (2025) demonstrates power-law moral alignment improvements across 75 model configurations

**Key gaps remain:** No dedicated benchmarks exist for Confucian ethics, Ubuntu/African values, Hindu ethics, or Buddhist ethics as standalone evaluation datasets — these traditions appear only in theoretical governance frameworks. Care ethics and virtue ethics also lack deep standalone benchmarks.

---

## A. Multi-Framework Ethics Benchmarks

### A1. ETHICS Dataset (Hendrycks et al., 2021) — THE ANCHOR
- **Citation:** Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song, D., & Steinhardt, J. (2021). Aligning AI With Shared Human Values. *ICLR 2021*.
- **arXiv:** [2008.02275](https://arxiv.org/abs/2008.02275) | ~688 citations
- **Frameworks:** Justice, Deontology, Virtue Ethics, Utilitarianism, Commonsense Morality
- **Dataset:** ~130K+ examples across 5 sub-tasks (justice: 26.5K, deontology: 25.3K, virtue: 38K, + utilitarianism + commonsense)
- **Code:** [GitHub](https://github.com/hendrycks/ethics) | [HuggingFace](https://huggingface.co/datasets/hendrycks/ethics)
- **LLMs tested:** BERT-large, ALBERT-xxlarge, RoBERTa-large, GPT-3 (few-shot)
- **Also in:** EleutherAI [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (`hendrycks_ethics` task)
- **Readiness:** ★★★ HIGH

### A2. MoReBench (Chiu et al., 2025)
- **Citation:** Chiu, Y.Y., Lee, S., et al. (2025). MoReBench: Evaluating Procedural and Pluralistic Moral Reasoning in Language Models, More than Outcomes.
- **arXiv:** [2510.16380](https://arxiv.org/abs/2510.16380)
- **Frameworks:** Kantian Deontology, Benthamite Act Utilitarianism, Aristotelian Virtue Ethics, Scanlonian Contractualism, Gauthierian Contractarianism
- **Dataset:** 1,000 moral scenarios + 23,000+ rubric criteria; MoReBench-Theory: 150 examples across 5 frameworks
- **Code:** [GitHub](https://github.com/morebench/morebench) | [HuggingFace](https://huggingface.co/datasets/morebench/morebench)
- **LLMs tested:** Multiple (evaluation scripts + judge model pipeline included)
- **Note:** Created with 50+ PhD moral philosophers; rubric-based scoring across 5 dimensions
- **Readiness:** ★★★ HIGH

### A3. LLM Ethics Benchmark (Jiao et al., 2025)
- **Citation:** Jiao, J., Afroogh, S., Murali, A., Chen, K., Atkinson, D., & Dhurandhar, A. (2025). LLM Ethics Benchmark: A Three-Dimensional Assessment System. *Scientific Reports*.
- **arXiv:** [2505.00853](https://arxiv.org/abs/2505.00853) | **DOI:** [10.1038/s41598-025-18489-7](https://www.nature.com/articles/s41598-025-18489-7)
- **Frameworks:** Deontological, Consequentialist, Virtue Ethics (3 dimensions: foundational moral principles, reasoning robustness, value consistency)
- **Dataset:** 3 instruments as JSON files: MFQ (`mfq.json`), WVS (`wvs.json`), Moral Dilemmas (`dilemmas.json`)
- **Code:** [GitHub](https://github.com/The-Responsible-AI-Initiative/LLM_Ethics_Benchmark) — Full CLI tool, CC0-1.0 license
- **LLMs tested:** GPT-4o (90.0), Claude 3.7 Sonnet (90.9), DeepSeek-V3 (86.1), LLaMA 3.1-70B (75.8), Gemini 2.5 Pro (86.1)
- **Readiness:** ★★★ HIGH

### A4. MoralBench (Ji et al., 2024)
- **Citation:** Ji, J., Chen, Y., Jin, M., Xu, W., Hua, W., & Zhang, Y. (2024). MoralBench: Moral Evaluation of LLMs. *KDD Explorations*, 27(1).
- **arXiv:** [2406.04428](https://arxiv.org/abs/2406.04428)
- **Frameworks:** Moral Foundations Theory (Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Sanctity/Degradation, Liberty/Oppression)
- **Dataset:** MFQ-30-LLM (30 items) + MFV-LLM (132 vignettes) = 162 items total
- **Code:** [GitHub](https://github.com/agiresearch/MoralBench) | [Google Drive data](https://drive.google.com/drive/u/0/folders/1k93YZJserYc2CkqP8d4B3M3sgd3kA8W7)
- **LLMs tested:** Zephyr, LLaMA-2-70B (highest MFQ: 58.5), Gemma-1.1-7B, GPT-3.5, GPT-4 (highest MFV: 52.8)
- **Readiness:** ★★★ HIGH

### A5. EthicsSuite (Ma et al., 2023)
- **Citation:** Ma, P., Li, Z., Sun, A., & Wang, S. (2023). "Oops, Did I Just Say That?" Testing and Repairing Unethical Suggestions of LLMs with Suggest-Critique-Reflect Process.
- **arXiv:** [2305.02626](https://arxiv.org/abs/2305.02626)
- **Frameworks:** Justice, Deontology, Virtue Ethics, Utilitarianism, Commonsense (contextualizes ETHICS dataset seeds)
- **Dataset:** ~20,000 contextualized moral situations (JSONL format)
- **Code:** [GitHub](https://github.com/LLM-Ethics/EthicsSuite) (dataset only, no eval code)
- **LLMs tested:** 7 LLMs including ChatGPT, GPT-4, Llama-13B — uncovered 109,824 unethical suggestions
- **Readiness:** ★★☆ MEDIUM

---

## B. Single-Framework / Focused Ethics Benchmarks

### B1. MoralChoice — Evaluating Moral Beliefs Encoded in LLMs (Scherrer et al., 2023)
- **Citation:** Scherrer, N., Shi, C., Feder, A., & Blei, D.M. (2023). Evaluating the Moral Beliefs Encoded in LLMs. *NeurIPS 2023 (Spotlight)*.
- **arXiv:** [2307.14324](https://arxiv.org/abs/2307.14324)
- **Frameworks:** Cross-framework (scenarios annotated with violated moral rules)
- **Dataset:** 680 high-ambiguity + 687 low-ambiguity = 1,367 moral scenarios; A/B choice format
- **Code:** [GitHub](https://github.com/ninodimontalcino/moralchoice) | [HuggingFace](https://huggingface.co/datasets/ninoscherrer/moralchoice)
- **LLMs tested:** 28 models (GPT-3/3.5/4, Claude v1.2/v1.3/v2.0, Claude Instant, PaLM 2, Flan-T5 ×5, BLOOMZ ×7, OPT-IML, Cohere Command, AI21 J2)
- **Readiness:** ★★★ HIGH

### B2. MoralExceptQA (Jin et al., 2022)
- **Citation:** Jin, Z., Levine, S., Gonzalez Adauto, F., Kamal, O., Sap, M., Sachan, M., Mihalcea, R., Tenenbaum, J., & Schölkopf, B. (2022). When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment. *NeurIPS 2022*.
- **arXiv:** [2210.01478](https://arxiv.org/abs/2210.01478)
- **Frameworks:** Deontological (testing when rules can be permissibly broken)
- **Dataset:** 148 rule-breaking scenarios across 3 subsets; human agreement percentages included
- **Code:** [GitHub](https://github.com/feradauto/MoralCoT) | [HuggingFace](https://huggingface.co/datasets/feradauto/MoralExceptQA)
- **LLMs tested:** Delphi, GPT-3, InstructGPT + 7 baselines; MoralCoT outperforms by 6.2% F1
- **Readiness:** ★★★ HIGH

### B3. The Greatest Good Benchmark (Marraffini et al., 2024)
- **Citation:** Marraffini, G.F.G., Cotton, A., Hsueh, N.F., Fridman, A., Wisznia, J., & Del Corro, L. (2024). The Greatest Good Benchmark: Measuring LLMs' Alignment with Utilitarian Moral Dilemmas. *EMNLP 2024*.
- **DOI:** [10.18653/v1/2024.emnlp-main.1224](https://aclanthology.org/2024.emnlp-main.1224/)
- **Frameworks:** Utilitarian (Impartial Beneficence + Instrumental Harm from Oxford Utilitarianism Scale)
- **Dataset:** 144 statements (9 original + 90 synthetic), 5,940 calls/model; validated by 3 utilitarianism experts
- **Code:** [GitHub (pending)](https://github.com/noehsueh/greatest-good-benchmark) | [ACL data ZIP](https://aclanthology.org/attachments/2024.emnlp-main.1224.data.zip)
- **LLMs tested:** 15 models (ChatGPT, GPT-4, Gemini Pro 1.0/1.5, Claude-3-Haiku/Opus, Falcon-7b/40b, Gemma-7b, Llama-3-8b/70b, Mistral-7b, Mixtral-8x7b, Yi-6b/34b)
- **Readiness:** ★★☆ MEDIUM

### B4. MACHIAVELLI Benchmark (Pan et al., 2023)
- **Citation:** Pan, A., Shern, C.S., et al. (2023). Do the Rewards Justify the Means? Measuring Trade-Offs Between Rewards and Ethical Behavior in the MACHIAVELLI Benchmark. *ICML 2023*.
- **arXiv:** [2304.03279](https://arxiv.org/abs/2304.03279)
- **Frameworks:** Consequentialist (deception, power-seeking, harm in interactive environments)
- **Dataset:** 134 Choose-Your-Own-Adventure games, 572,322 scenes, 4,559 achievements, 3M+ annotations
- **Code:** [GitHub](https://github.com/aypan17/machiavelli) | [Project page](https://aypan17.github.io/machiavelli/)
- **LLMs tested:** GPT-4 and other agents in interactive text-based environments
- **Readiness:** ★★★ HIGH

### B5. DailyDilemmas (Chiu et al., 2024)
- **Citation:** Chiu, Y.Y., Jiang, L., & Choi, Y. (2024). DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life. *ICLR 2025 Spotlight*.
- **arXiv:** [2410.02683](https://arxiv.org/abs/2410.02683)
- **Frameworks:** Multi-lens: Aristotle's Virtues, MFT, World Values Survey, Maslow's Hierarchy, Plutchik's Emotions — 301 human values
- **Dataset:** 1,360 moral dilemmas (interpersonal, workplace, environmental)
- **Code:** OpenReview supplementary ZIP
- **LLMs tested:** GPT-4-turbo, Mixtral-8x7B, others
- **Readiness:** ★★☆ MEDIUM

### B6. Right vs. Right (Yuan et al., 2024)
- **Citation:** Yuan, J., Murukannaiah, P.K., & Singh, M.P. (2024). Right vs. Right: Can LLMs Make Tough Choices?
- **arXiv:** [2412.19926](https://arxiv.org/abs/2412.19926)
- **Frameworks:** Kidder's ethical dilemma framework (Truth vs. Loyalty, Individual vs. Community, Short-term vs. Long-term, Justice vs. Mercy); larger LLMs show deontological tendency
- **Dataset:** 1,730 ethical dilemmas, 4 value-conflict pairs
- **LLMs tested:** 20 models from 6 families (OpenAI, Anthropic, Meta, Mistral, Alibaba, 01-AI)
- **Code:** No public repository confirmed
- **Readiness:** ★☆☆ LOW

### B7. MORABLES (2025)
- **Citation:** MORABLES: A Benchmark for Assessing Abstract Moral Reasoning in LLMs with Fables.
- **arXiv:** [2509.12371](https://arxiv.org/abs/2509.12371) (September 2025)
- **Frameworks:** Abstract moral reasoning from literary fables (Western literary tradition)
- **Dataset:** 709 fable-moral pairs; multiple-choice with adversarial variants
- **Code:** [HuggingFace](https://huggingface.co/datasets/cardiffnlp/Morables)
- **LLMs tested:** 11 models: Mistral-7B, Llama 3.1-8B, Qwen 2.5-7B, Mixtral-8x22B, Llama 3.3-70B, DeepSeek V3, Gemini 2.0 Flash, GPT-4o, Claude 3.5 Sonnet, GPT-o3-mini, DeepSeek R1
- **Readiness:** ★★★ HIGH

### B8. Conscience Conflict (Hota & Jokinen, 2024)
- **Citation:** Hota, A. & Jokinen, J.P.P. (2024/2025). Conscience Conflict? Evaluating Language Models' Moral Understanding. *CEUR-WS Vol-4004*.
- **URL:** [CEUR-WS](https://ceur-ws.org/Vol-4004/paper3.pdf)
- **Frameworks:** Deontological, Consequentialist, Virtue (3 archetypes: Principled, Conformist, Avoidant)
- **Dataset:** 6 high-stakes moral dilemma vignettes
- **LLMs tested:** 5 open-source: Mistral, LLaMA-3.2, Gemma, DeepSeek-r1, Phi4
- **Code:** No public repository
- **Readiness:** ★☆☆ LOW

### B9. Normative Evaluation with Everyday Moral Dilemmas (Sachdeva & van Nuenen, 2025)
- **Citation:** Sachdeva, P.S. & van Nuenen, T. (2025). Normative Evaluation of Large Language Models with Everyday Moral Dilemmas. *FAccT 2025*.
- **arXiv:** [2501.18081](https://arxiv.org/abs/2501.18081)
- **Frameworks:** Normative evaluation using real-world moral dilemmas (AITA subreddit)
- **Dataset:** 10,000+ AITA moral dilemmas sourced from Reddit
- **Code:** [GitHub](https://github.com/dlab-projects/normative_evaluation_llms_everyday_dilemmas)
- **LLMs tested:** 7 LLMs (moderate-to-high self-consistency, low inter-model agreement)
- **Readiness:** ★★★ HIGH

---

## C. Cross-Cultural Values Benchmarks

### C1. WorldValuesBench (Zhao et al., 2024)
- **Citation:** Zhao, W., Mondal, D., Tandon, N., Dillion, D., Gray, K., & Gu, Y. (2024). WorldValuesBench. *LREC-COLING 2024*.
- **arXiv:** [2404.16308](https://arxiv.org/abs/2404.16308)
- **Cultural scope:** 94,728 participants worldwide (WVS data)
- **Dataset:** 20M+ examples (demographic attributes, value question → answer)
- **Languages:** English
- **LLMs tested:** Alpaca-7B, Vicuna-7B, Mixtral-8x7B-Instruct, GPT-3.5 Turbo
- **Readiness:** ★★☆ MEDIUM (massive dataset, no confirmed public repo)

### C2. CultureLLM (Li et al., 2024)
- **Citation:** Li, C., Chen, M., Wang, J., Sitaram, S., & Xie, X. (2024). CultureLLM: Incorporating Cultural Differences into Large Language Models. *NeurIPS 2024*.
- **arXiv:** [2402.10946](https://arxiv.org/abs/2402.10946)
- **Cultural scope:** 9 cultures (Arabic, Bengali, Chinese, English, German, Korean, Portuguese, Spanish, Turkish)
- **Dataset:** 50 WVS seed samples/culture with semantic data augmentation; 7 topic categories
- **Code:** [GitHub](https://github.com/Scarelette/CultureLLM)
- **LLMs tested:** GPT-3.5, Gemini Pro, GPT-4 (CultureLLM outperforms GPT-3.5 by 8.1%)
- **Readiness:** ★★★ HIGH

### C3. CIVICS (Pistilli et al., 2024)
- **Citation:** Pistilli, G., Leidinger, A., Jernite, Y., Kasirzadeh, A., Luccioni, A.S., & Mitchell, M. (2024). CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models. *AIES 2024*.
- **arXiv:** [2405.13974](https://arxiv.org/abs/2405.13974)
- **Cultural scope:** 9 national contexts (Australia, Canada, France, Germany, Italy, Singapore, Turkey, UK)
- **Dataset:** 699 hand-crafted prompts; topics: LGBTQI rights, social welfare, immigration, disability rights, surrogacy
- **Languages:** 5 (English, German, French, Italian, Turkish) | CC BY 4.0
- **Code:** [HuggingFace](https://huggingface.co/datasets/llm-values/CIVICS)
- **Readiness:** ★★★ HIGH

### C4. LLM-GLOBE (Karinshak et al., 2024)
- **Citation:** Karinshak, E., Hu, A., Kong, K., Rao, V., Wang, J., Wang, J., & Zeng, Y. (2024). LLM-GLOBE: A Benchmark Evaluating the Cultural Values Embedded in LLM Output.
- **arXiv:** [2411.06032](https://arxiv.org/abs/2411.06032)
- **Cultural scope:** US vs. China; GLOBE framework (9 cultural dimensions)
- **Dataset:** 36,675 closed-ended + 900 open-generation prompts; English + Chinese
- **Code:** [GitHub](https://github.com/raovish6/LLM-GLOBE) — novel "LLMs-as-a-Jury" eval pipeline
- **LLMs tested:** Claude, Gemini, GPT-3.5, GPT-4 (US); GLM-4, Ernie 3.5/4.0, Qwen-14b (China)
- **Readiness:** ★★★ HIGH

### C5. CQ-Bench (Liu et al., 2025)
- **Citation:** Liu, Z., Dey, P., Huang, J.-T., Zhao, Z., Jiang, B., Gupta, R., Liu, Y., Du, Y., & Zhao, J. (2025). Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs' Cultural Intelligence with CQ-Bench.
- **arXiv:** [2504.01127](https://arxiv.org/abs/2504.01127)
- **Cultural scope:** Global (WVS + GlobalOpinions; ethical, religious, social, political topics)
- **Dataset:** 1,000 multi-character conversation stories; 3 tasks (attitude detection, value selection, value extraction)
- **Code:** [GitHub](https://github.com/uscnlp-lime/CQ-Bench)
- **LLMs tested:** Qwen 2.5 (7B/14B/32B), Qwen 3-4B, LLaMA 3.1-8B, LLaMA 3.2-3B, DeepSeek-V3/R1, GPT-4o-mini, o4-mini, o3, o3-mini, o1
- **Key finding:** Fine-tuning LLaMA-3.2-3B on 500 examples improves >10%, outperforming o3-mini
- **Readiness:** ★★★ HIGH

### C6. MENAValues (Zahraei & Asgari, 2025)
- **Citation:** Zahraei, P.S. & Asgari, E. (2025). I Am Aligned, But With Whom? MENA Values Benchmark for Evaluating Cultural Alignment and Multilingual Bias in LLMs.
- **arXiv:** [2510.13154](https://arxiv.org/abs/2510.13154)
- **Cultural scope:** 16 MENA countries (Algeria, Egypt, Iran, Iraq, Jordan, Kuwait, Lebanon, Libya, Mauritania, Morocco, Palestine, Qatar, Saudi Arabia, Sudan, Tunisia, Turkey)
- **Dataset:** 864 MCQ from WVS Wave 7 + 2022 Arab Opinion Index; governance, economics, cultural identity, wellbeing
- **Languages:** English, Arabic, Persian, Turkish
- **Code:** [GitHub](https://github.com/llm-lab-org/MENA-Values-Benchmark-Evaluating-Cultural-Alignment-and-Multilingual-Bias-in-Large-Language-Models)
- **LLMs tested:** Llama-3.1-8B, Mistral-7B, AYA-expanse-8b, Fanar-1-9B, ALLAM-Thinking, GPT-4o-mini, Gemini 2.5 Flash Lite
- **Key finding:** "Cross-Lingual Value Shifts" — identical questions yield different responses based on language
- **Readiness:** ★★★ HIGH

### C7. IslamTrust (Lahmar et al., 2025)
- **Citation:** Lahmar, A., Arafat, M.E., Farou, Z., & Mahmud, M. (2025). IslamTrust: A Benchmark for LLMs Alignment with Islamic Values. *Muslims in ML Workshop @ NeurIPS 2025*.
- **OpenReview:** [PBcv90iKFB](https://openreview.net/forum?id=PBcv90iKFB)
- **Cultural scope:** Islamic values across 6 domains; bilingual
- **Dataset:** 406 MCQ; Arabic + English; MIT license
- **Code:** [HuggingFace](https://huggingface.co/datasets/Abderraouf000/IslamTrust-benchmark) | ~~[GitHub](https://github.com/abderraouf-000/IslamTrust-LLM-Benchmark)~~ (404 — repo may have moved; HF dataset confirmed valid)
- **LLMs tested:** SILMA-9B (best), Fanar-1-9B, ALLaM-7B, Llama-3.1-8B
- **Key finding:** LLMs perform better in Arabic than English; systematic biases in interfaith dialogue
- **Readiness:** ★★★ HIGH

### C8. CDEval (Wang et al., 2024)
- **Citation:** Wang, Y., Zhu, Y., Kong, C., Wei, S., Yi, X., Xie, X., & Sang, J. (2024). CDEval: A Benchmark for Measuring the Cultural Dimensions of Large Language Models. *Cross-Cultural NLP Workshop @ ACL 2024*.
- **arXiv:** [2311.16421](https://arxiv.org/abs/2311.16421)
- **Cultural scope:** Hofstede's 6 cultural dimensions (PDI, IDV, UAI, MAS, LTO, IVR) across 7 domains; compared against 98 countries
- **Dataset:** 2,953 questions; English, Chinese, German
- **Code:** [GitHub](https://github.com/astrodrew/CDEval)
- **LLMs tested:** 17 models (GPT-4, GPT-3.5-turbo, ChatGLM v1-3, Spark-v2, Llama2-Chat, Qwen-Chat, Baichuan-Chat, Alpaca-7B, Chinese-Alpaca2-13B, etc.)
- **Readiness:** ★★★ HIGH

### C9. CulturalBench (Chiu et al., 2025)
- **Citation:** Chiu, Y.Y., Jiang, L., Lin, B.Y., Park, C.Y., Li, S.S., Ravi, S., Bhatia, M., Antoniak, M., Tsvetkov, Y., Shwartz, V., & Choi, Y. (2025). CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark. *ACL 2025*.
- **arXiv:** [2410.02677](https://arxiv.org/abs/2410.02677)
- **Cultural scope:** 45 countries/regions across 14 geographic areas (North/South/West Africa, Americas, East/South/Southeast Asia, Middle East, Europe, Oceania)
- **Dataset:** 1,696 human-written, 5-annotator-verified questions; 17 topics in 3 categories; CC BY 4.0
- **Code:** [HuggingFace Space](https://hf.co/spaces/kellycyy/CulturalBench)
- **LLMs tested:** 29 models (GPT-3.5/4o/o1, Llama 3/3.1/3.3, Claude 3.5 Sonnet, Mistral, Cohere Aya, DeepSeek, Qwen)
- **Key finding:** Accuracy 28.7%-61.5% (hard version) vs. 92.4% human performance
- **Readiness:** ★★★ HIGH

### C10. XCR-Bench (Kabir et al., 2026)
- **Citation:** Kabir, M., Ahmed, T., Rahman, M.M., Ji, S., Alhuzali, H., & Ananiadou, S. (2026). XCR-Bench: A Multi-Task Benchmark for Evaluating Cultural Reasoning in LLMs.
- **arXiv:** [2601.14063](https://arxiv.org/abs/2601.14063)
- **Cultural scope:** Chinese, Arabic, Bengali (with West Bengal/India and Bangladesh sub-variants)
- **Dataset:** 4,900 parallel sentences, 1,098 Culture-Specific Items; 3 reasoning tasks; CC BY-NC-ND 4.0
- **Code:** [GitHub](https://github.com/mohsinulkabir14/xcr_bench)
- **LLMs tested:** GPT-4o, Qwen-2.5-Max, Gemini-2.0-Flash, Claude-3.7-Sonnet, DeepSeek-R1, LLaMA-3.3-70B, OLMo-2-32B
- **Readiness:** ★★★ HIGH

---

## D. Moral Psychology & Foundations Benchmarks

### D1. Delphi / Commonsense Norms Bank (Jiang et al., 2021)
- **Citation:** Jiang, L., et al. (2021/2025). Can Machines Learn Morality? The Delphi Experiment. *Nature Machine Intelligence* (2025 follow-up).
- **arXiv:** [2110.07574](https://arxiv.org/abs/2110.07574)
- **Frameworks:** Commonsense moral reasoning (Rawlsian bottom-up approach)
- **Dataset:** Norm Bank: 1.7M descriptive human moral judgments
- **Code:** [GitHub](https://github.com/liweijiang/delphi)
- **Model:** Delphi (T5-11B based Unicorn model)
- **Readiness:** ★★★ HIGH

### D2. ValueBench (Ren et al., 2024)
- **Citation:** Ren, Y., Ye, H., Fang, H., Zhang, X., & Song, G. (2024). ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models. *ACL 2024*.
- **arXiv:** [2406.04214](https://arxiv.org/abs/2406.04214)
- **Frameworks:** 44 psychometric inventories covering 453 value dimensions
- **Code:** [GitHub](https://github.com/Value4AI/ValueBench)
- **LLMs tested:** 6 representative LLMs
- **Readiness:** ★★★ HIGH

### D3. Touché / ValueEval (SemEval 2023, CLEF 2024)
- **Citation:** Kiesel, J., et al. (2023). The Touché23-ValueEval Dataset for Identifying Human Values behind Arguments.
- **arXiv:** [2301.13771](https://arxiv.org/abs/2301.13771)
- **Frameworks:** 19 Schwartz values (value detection + value attainment)
- **Dataset:** ~3,000 human-annotated texts (400-800 words each); news articles + political manifestos
- **Languages:** 8 languages
- **Code:** [Zenodo](https://zenodo.org/records/6814564) | [Task page](https://touche.webis.de/clef24/touche24-web/human-value-detection.html)
- **Readiness:** ★★★ HIGH

### D4. MFTCXplain (Vargas et al., 2025)
- **Citation:** Vargas, F., et al. (2025). MFTCXplain: A Multilingual Benchmark Dataset for Evaluating the Moral Reasoning of LLMs through Multi-hop Hate Speech Explanation. *Findings of EMNLP 2025*.
- **arXiv:** [2506.19073](https://arxiv.org/abs/2506.19073)
- **Frameworks:** Moral Foundations Theory (10 moral sentiment categories)
- **Dataset:** 3,000 tweets; Portuguese, Italian, Persian, English; binary hate speech labels + moral categories + text span rationales
- **Code:** [GitHub](https://github.com/franciellevargas/MFTCXplain)
- **LLMs tested:** LLaMA-70B-Instruct, GPT-4o Mini
- **Key finding:** LLMs achieve F1 0.836 on hate speech detection but <0.35 on moral sentiment prediction
- **Readiness:** ★★★ HIGH

### D5. Scaling Laws for Moral Machine Judgment (Takemoto, 2025)
- **Citation:** Takemoto, K. (2025). Scaling Laws for Moral Machine Judgment in Large Language Models.
- **arXiv:** [2601.17637](https://arxiv.org/abs/2601.17637)
- **Frameworks:** Moral Machine trolley-problem scenarios
- **Dataset:** Uses Moral Machine framework across 75 model configurations (0.27B-1000B parameters)
- **Code:** [GitHub](https://github.com/kztakemoto/mmllm)
- **Key finding:** Power-law relationship D ∝ S^(−0.10±0.01) — moral alignment improves predictably with scale
- **Readiness:** ★★★ HIGH

---

## E. Psychometric & Values Survey Benchmarks

### E1. Structured Moral Reasoning: Value-Grounded Framework (Chakraborty et al., 2025)
- **Citation:** Chakraborty, S., Wang, X., & Jurgens, D. (2025). Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework. *EMNLP 2025*.
- **arXiv:** [2506.14948](https://arxiv.org/abs/2506.14948) | [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1541/)
- **Frameworks:** Schwartz values + Care Ethics scaffolds; first-principles reasoning
- **Dataset:** Benchmarked across 4 existing moral datasets; 12 open-source models
- **Key finding:** Prompting with explicit moral structure consistently improves accuracy; supervised distillation transfers moral competence from large to small models
- **Readiness:** ★★☆ MEDIUM (framework paper, uses existing datasets)

### E2. Beyond Ethical Alignment: Evaluating LLMs as Artificial Moral Assistants (Galatolo et al., 2025)
- **Citation:** Galatolo, A., Rappuoli, L.A., Winkle, K., & Beloucif, M. (2025). Beyond Ethical Alignment: Evaluating LLMs as Artificial Moral Assistants.
- **arXiv:** [2508.12754](https://arxiv.org/abs/2508.12754)
- **Frameworks:** Formal AMA framework (deductive + abductive moral reasoning)
- **Dataset:** Custom benchmark for AMA qualities
- **Code:** Code availability noted but URL pending
- **Key finding:** Persistent shortcomings in abductive moral reasoning across models
- **Readiness:** ★★☆ MEDIUM

### E3. Diverse Human Value Alignment via Ethical Reasoning (Wang et al., 2025)
- **Citation:** Wang, J., Xue, S., Li, J., & Wang, X. (2025). Diverse Human Value Alignment for Large Language Models via Ethical Reasoning. *AIES 2025*.
- **arXiv:** [2511.00379](https://arxiv.org/abs/2511.00379) | [AIES proceedings](https://ojs.aaai.org/index.php/AIES/article/view/36744)
- **Frameworks:** 5-step ethical reasoning CoT (contextual facts → hierarchical norms → options → multi-lens analysis → reflection)
- **Dataset:** Uses SafeWorld dataset (50 countries, 493 regions)
- **Key contribution:** Pipeline for generating fine-tuning datasets of ethical reasoning at scale
- **Readiness:** ★★☆ MEDIUM

---

## F. Meta-Resources & Survey Papers

### F1. SafetyPrompts.com (Vidgen et al., 2024)
- **URL:** [safetyprompts.com](https://safetyprompts.com/)
- **Scope:** Living catalogue of 144+ LLM safety datasets (23 specifically in "Value Alignment" category)
- **Readiness:** ★★★ HIGH (meta-resource)

### F2. SafetyBench (Zhang et al., 2024)
- **Citation:** Zhang, Z., et al. (2024). SafetyBench: Evaluating the Safety of Large Language Models. *ACL 2024*.
- **arXiv:** [2309.07045](https://arxiv.org/abs/2309.07045)
- **Dataset:** 11,435 MCQ across 7 safety categories (includes Ethics and Morality); Chinese + English
- **Code:** [GitHub](https://github.com/thu-coai/SafetyBench)
- **LLMs tested:** 25 models
- **Readiness:** ★★★ HIGH

### F3. Awesome-LLM-Psychometrics
- **URL:** [GitHub](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)
- **Scope:** Curated list of LLM psychometric and psychology papers
- **Readiness:** ★★★ HIGH (meta-resource, 597 stars)

### F4. EleutherAI lm-evaluation-harness
- **URL:** [GitHub](https://github.com/EleutherAI/lm-evaluation-harness)
- **Scope:** Unified evaluation framework including `hendrycks_ethics` task for reproducible ethics benchmarking
- **Readiness:** ★★★ HIGH (standard evaluation tool)

---

## Implementation Priority Guide

### Tier 1: Start Here (HIGH readiness + broad framework coverage)
| Priority | Benchmark | Why |
|----------|-----------|-----|
| 1 | **MoReBench** | 5 normative frameworks, 1,000 scenarios, 23K criteria, GitHub+HF, rubric-based |
| 2 | **ETHICS (Hendrycks)** | Anchor paper, 130K+ examples, 5 sub-tasks, in lm-eval-harness |
| 3 | **LLM Ethics Benchmark (Jiao)** | 3D assessment, MFQ+WVS+Dilemmas as JSON, CLI tool, CC0 license |
| 4 | **MoralChoice (Scherrer)** | 28 models already evaluated, statistical methodology, NeurIPS spotlight |
| 5 | **CulturalBench** | 45 countries, 29 models, 1,696 questions, CC BY 4.0, ACL 2025 |

### Tier 2: Expand Coverage (HIGH readiness + specific focus)
| Priority | Benchmark | Focus |
|----------|-----------|-------|
| 6 | **ValueBench** | 453 psychometric value dimensions |
| 7 | **CQ-Bench** | Implicit cultural values via conversation |
| 8 | **MENAValues** | MENA region, 4 languages, cross-lingual shifts |
| 9 | **IslamTrust** | Islamic values, bilingual, MIT license |
| 10 | **MACHIAVELLI** | Interactive consequentialist ethics |
| 11 | **CIVICS** | 9 national contexts, HuggingFace, CC BY 4.0 |
| 12 | **Delphi/Norm Bank** | 1.7M commonsense moral judgments |

### Tier 3: Specialized Deep-Dives (MEDIUM/HIGH readiness + unique angles)
| Priority | Benchmark | Focus |
|----------|-----------|-------|
| 13 | **MFTCXplain** | Multilingual moral foundations in hate speech |
| 14 | **Scaling Laws (Takemoto)** | Model size → moral alignment relationship |
| 15 | **Touché/ValueEval** | Schwartz values in text, 8 languages |
| 16 | **CDEval** | Hofstede cultural dimensions |
| 17 | **CultureLLM** | 9-culture fine-tuning framework |
| 18 | **MORABLES** | Abstract moral reasoning from fables |
| 19 | **Greatest Good** | Utilitarian-specific, 15 models |

---

## Gap Analysis

### Well-Covered Areas
- **Consequentialism/Utilitarianism:** Greatest Good, MACHIAVELLI, Moral Machine experiments
- **Deontology:** ETHICS sub-task, MoralExceptQA, MoReBench-Theory
- **Moral Foundations Theory:** MoralBench, MFTCXplain, LLM Ethics Benchmark
- **Western cultural values:** CulturalBench, CIVICS, LLM-GLOBE
- **Islamic values:** IslamTrust, MENAValues
- **WVS-based cross-cultural:** WorldValuesBench, CultureLLM, CQ-Bench, CDEval

### Critical Gaps (No Dedicated Benchmarks Found)
| Gap | Status | Opportunity |
|-----|--------|-------------|
| **Confucian ethics** | Theoretical papers only (governance frameworks) | Need dataset operationalizing ren (仁), li (禮), yi (義) |
| **Ubuntu/African ethics** | Normative philosophy papers only | Need dataset operationalizing ubuntu, communalism, relational identity |
| **Hindu ethics** | No papers found | Need dataset covering dharma, karma, ahimsa |
| **Buddhist ethics** | No papers found | Need dataset covering precepts, compassion, interdependence |
| **Care ethics (standalone)** | Partial via MFT's Care/Harm | Need dedicated feminist/care ethics evaluation |
| **Virtue ethics (deep)** | Partial via ETHICS sub-task | Need phronesis, eudaimonia, character assessment |
| **Cross-framework conflict resolution** | Only Conscience Conflict (6 scenarios) | Need larger dataset of genuine ethical framework conflicts |
| **Non-English-first benchmarks** | Most are English-centric | MENAValues and IslamTrust are notable exceptions |

---

## Vault Status (as of 2026-02-07)

### Already in Vault (19 papers) — no import needed
| # | Paper | Vault Match |
|---|-------|-------------|
| A1 | ETHICS (Hendrycks 2021) | `2021-Hendrycks-Aligning AI with Shared Human Values.pdf` |
| A2 | MoReBench (Chiu 2025) | `2025-Chiu-MoReBench.pdf` |
| A3 | LLM Ethics Benchmark (Jiao 2025) | `2025-Jiao-LLM Ethics Benchmark.pdf` |
| A4 | MoralBench (Ji 2024) | `2024-Ji-MoralBench.pdf` |
| B1 | MoralChoice (Scherrer 2023) | `2023-Scherrer-Evaluating the Moral Beliefs Encoded in LLMs.pdf` |
| B3 | Greatest Good (Marraffini 2024) | `2024-Marraffini-The Greatest Good Benchmark.pdf` |
| B4 | MACHIAVELLI (Pan 2023) | `2023-Pan-Do the Rewards Justify the Means Measuring.pdf` |
| B5 | DailyDilemmas (Chiu 2024) | `2024-Chiu-DailyDilemmas.pdf` |
| B9 | Normative Evaluation (Sachdeva 2025) | `2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas.pdf` |
| C1 | WorldValuesBench (Zhao 2024) | `2024-Wu-WorldValuesBench.pdf` |
| C3 | CIVICS (Pistilli 2024) | `2024-Pistilli-CIVICS.pdf` |
| C9 | CulturalBench (Chiu 2025) | `2025-Chiu-CulturalBench.pdf` |
| D1 | Delphi — see note* | Related Jin 2024 found; Jiang 2021 Delphi NOT confirmed |
| D2 | ValueBench (Ren 2024) | `2024-Ren-ValueBench.pdf` |
| D5 | Scaling Laws (Takemoto) | `2024-Takemoto-The moral machine experiment on large language.pdf` (2024 version) |
| E1 | Structured Moral Reasoning (Chakraborty 2025) | `2025-Chakraborty-Structured Moral Reasoning.pdf` |
| E2 | Beyond Ethical Alignment (Galatolo 2025) | `2025-Galatolo-Beyond Ethical Alignment.pdf` |
| E3 | Diverse Human Value Alignment (Wang 2025) | `2025-Wang-Diverse Human Value Alignment for LLMs via Ethical Reasoning.pdf` |
| F2 | SafetyBench (Zhang 2024) | `2024-Zhang-SafetyBench.pdf` |

### NOT in Vault (14 papers) — candidates for import
| # | Paper | arXiv / Source |
|---|-------|---------------|
| A5 | EthicsSuite (Ma 2023) | [2305.02626](https://arxiv.org/abs/2305.02626) |
| B2 | MoralExceptQA (Jin 2022) | [2210.01478](https://arxiv.org/abs/2210.01478) |
| B6 | Right vs. Right (Yuan 2024) | [2412.19926](https://arxiv.org/abs/2412.19926) |
| B7 | MORABLES (2025) | [2509.12371](https://arxiv.org/abs/2509.12371) |
| B8 | Conscience Conflict (Hota 2024) | [CEUR-WS Vol-4004](https://ceur-ws.org/Vol-4004/paper3.pdf) |
| C2 | CultureLLM (Li 2024) | [2402.10946](https://arxiv.org/abs/2402.10946) |
| C4 | LLM-GLOBE (Karinshak 2024) | [2411.06032](https://arxiv.org/abs/2411.06032) |
| C5 | CQ-Bench (Liu 2025) | [2504.01127](https://arxiv.org/abs/2504.01127) |
| C6 | MENAValues (Zahraei 2025) | [2510.13154](https://arxiv.org/abs/2510.13154) |
| C7 | IslamTrust (Lahmar 2025) | [OpenReview PBcv90iKFB](https://openreview.net/forum?id=PBcv90iKFB) |
| C8 | CDEval (Wang 2024) | [2311.16421](https://arxiv.org/abs/2311.16421) |
| C10 | XCR-Bench (Kabir 2026) | [2601.14063](https://arxiv.org/abs/2601.14063) |
| D3 | Touché/ValueEval (Kiesel 2023) | [2301.13771](https://arxiv.org/abs/2301.13771) |
| D4 | MFTCXplain (Vargas 2025) | [2506.19073](https://arxiv.org/abs/2506.19073) |

---

## Notes

- All GitHub URLs verified as of 2026-02-07 — 19/20 valid; IslamTrust GitHub repo (404) replaced with HuggingFace link
- Implementation readiness ratings: ★★★ HIGH = repo + data + eval code; ★★☆ MEDIUM = data available, needs custom eval; ★☆☆ LOW = described only
- This report is for research reference only — user will decide which papers to import into vault
