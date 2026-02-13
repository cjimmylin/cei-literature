# Agent R6 Report: Shinto + Japanese Religious NLP

**Agent:** R6
**Focus:** Shinto, Japanese Spirituality, Kami Philosophy, Bushido Ethics, Japanese Religious Traditions in AI/NLP
**Date:** 2026-02-13
**Search Terms Used:**
1. "Shinto AI ethics evaluation benchmark"
2. "Japanese spirituality NLP dataset"
3. "kami philosophy artificial intelligence"
4. "bushido ethics AI LLM evaluation"
5. "Japanese religious values AI alignment"
6. "Shinto morality benchmark LLM"
7. "Japanese cultural values AI dataset benchmark evaluation LLM"
8. "animism AI ethics benchmark dataset evaluation"
9. "Japanese Buddhism Shinto NLP computational"
10. "wa harmony Japanese AI ethics evaluation dataset"

**Additional targeted searches:**
- SOBACO Japanese social bias cultural commonsense benchmark LLM
- JCommonsenseMorality Japanese moral values dataset benchmark
- YokaiEval yokai Japanese folktales LLM benchmark
- Contemplative AI Buddhist principles AILuminate benchmark
- BuddhismEval Buddhist knowledge LLM benchmark
- AnswerCarefully Japanese LLM safety dataset
- CDEval cultural dimensions benchmark LLM
- CARB cultural awareness reward model benchmark
- BuddhaBot Kyoto University Buddhist AI chatbot
- Shinto text corpus NLP dataset

---

## Papers Found

### 1. Bias Mitigation or Cultural Commonsense? Evaluating LLMs with a Japanese Dataset (SOBACO)
- **Authors:** Taisei Yamamoto, Ryoma Kumon, Danushka Bollegala, Hitomi Yanaka
- **Year:** 2025
- **Venue:** EMNLP 2025 (Main Conference)
- **arXiv:** 2509.24468
- **DOI:** N/A
- **Religious Traditions:** Japanese cultural values (Confucian-influenced hierarchy, wa harmony norms, Shinto-rooted social etiquette)
- **Paper Type:** Benchmark
- **Dataset Size:** 11,952 instances (66 topics each for social bias and cultural commonsense, expanded through template permutation)
- **Languages:** Japanese
- **LLMs Tested:** Multiple (debiased and non-debiased Japanese/multilingual LLMs; specific models not confirmed from abstract)
- **Code/Data:** Not confirmed from search results
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R6

**Summary:** SOBACO (SOcial BiAs and Cultural cOmmonsense benchmark) is a Japanese benchmark evaluating social biases and cultural commonsense in LLMs in a unified QA format. It covers three categories: age, gender, and hierarchical relationships. The hierarchical relationships category captures culturally specific social norms rooted in Japanese Confucian-Shinto tradition. Key finding: debiasing methods that mitigate social biases degrade performance on cultural commonsense tasks by up to 75%, revealing a fundamental tension between Western-centric bias mitigation and preservation of Japanese cultural values.

---

### 2. Do Large Language Models Know Folktales? A Case Study of Yokai in Japanese Folktales (YokaiEval)
- **Authors:** Ayuto Tsutsumi, Yuu Jinnai
- **Year:** 2025
- **Venue:** ACL 2025 Findings
- **arXiv:** 2506.03619
- **DOI:** N/A
- **Religious Traditions:** Shinto, Japanese Buddhism (yokai originate from Shinto animist worldview and Buddhist folk traditions)
- **Paper Type:** Benchmark / Dataset
- **Dataset Size:** 809 multiple-choice questions (4 options each)
- **Languages:** Japanese
- **LLMs Tested:** 31 Japanese and multilingual LLMs (including Llama-3-based Japanese models)
- **Code/Data:** https://github.com/CyberAgentAILab/YokaiEval
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R6

**Summary:** YokaiEval benchmarks LLM knowledge of yokai -- supernatural phenomena and entities from Japanese folktales rooted in Shinto animism and Buddhist cosmology. The 809 QA pairs were generated from Wikipedia articles using GPT-4o, then curated with GPT-4o mini and manually verified. Models trained with Japanese language resources achieve significantly higher accuracy than English-centric models, demonstrating that Japanese spiritual-cultural knowledge requires language-specific training. This is the closest existing benchmark to directly testing Shinto/Japanese religious folk knowledge in LLMs.

---

### 3. BuddhismEval: A Bilingual Benchmark for Buddhist Ethical Reasoning and Philosophical Understanding
- **Authors:** Nethmi Muthugala, Deyi Xiong
- **Year:** 2025
- **Venue:** Hugging Face dataset (paper under review, likely NeurIPS 2025)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Buddhism (Theravada/Pali canon focus)
- **Paper Type:** Benchmark / Dataset
- **Dataset Size:** 1,242 English MCQs + 1,023 Sinhala MCQs + 423 parallel Dhammapada verses = ~2,688 items total
- **Languages:** English, Sinhala
- **LLMs Tested:** N/A (benchmark recently released; evaluations pending)
- **Code/Data:** https://huggingface.co/datasets/Nethmi14/BuddhismEval
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R6

**Summary:** BuddhismEval is the first bilingual evaluation benchmark specifically designed to assess LLMs on Buddhist ethical reasoning and philosophical understanding. It includes factual, ethical, philosophical, and applied reasoning questions drawn from the Dhammapada, Abhidharma texts, Sri Lankan government Buddhism exam papers, and Buddhist literature. While focused on Theravada Buddhism (Sinhala/Pali tradition) rather than Japanese Buddhism specifically, it represents the most comprehensive Buddhist knowledge evaluation resource for LLMs and could serve as a template for Zen/Shingon/Pure Land Buddhist variants relevant to Japan.

---

### 4. AnswerCarefully: A Dataset for Improving the Safety of Japanese LLM Output
- **Authors:** Hisami Suzuki, Satoru Katsumata, Takashi Kodama, Tetsuro Takahashi, Kouta Nakayama, Satoshi Sekine
- **Year:** 2025
- **Venue:** arXiv preprint (NII LLM-jp project)
- **arXiv:** 2506.02372
- **DOI:** N/A
- **Religious Traditions:** Japanese cultural/religious context (embedded in safety risk categories reflecting Japanese socio-cultural norms)
- **Paper Type:** Dataset
- **Dataset Size:** 1,800 question-answer pairs
- **Languages:** Japanese
- **LLMs Tested:** Japanese LLMs fine-tuned on the dataset (specific models not confirmed)
- **Code/Data:** https://huggingface.co/datasets/llm-jp/AnswerCarefully
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R6

**Summary:** AnswerCarefully is a safety dataset created by Japan's National Institute of Informatics (NII) LLM-jp project, consisting of 1,800 manually created question-answer pairs where questions require special attention. Unlike translations of English safety datasets, this is originally created to reflect the socio-cultural context of LLM usage in Japan, including culturally-specific safety risks. Fine-tuning on this data improved safety without reducing utility. While not explicitly a religious values benchmark, it captures Japanese cultural sensitivities that are deeply informed by Shinto/Buddhist/Confucian social norms.

---

### 5. CDEval: A Benchmark for Measuring the Cultural Dimensions of Large Language Models
- **Authors:** Yuhang Wang, Yanxu Zhu, Chao Kong, Shuyu Wei, Xiaoyuan Yi, Xing Xie, Jitao Sang
- **Year:** 2024
- **Venue:** Proceedings of the 2nd Workshop on Cross-Cultural Considerations in NLP (C3NLP @ LREC-COLING 2024)
- **arXiv:** 2311.16421
- **DOI:** N/A
- **Religious Traditions:** Indirectly covers Confucian collectivism, Buddhist-Shinto influenced power distance (via Hofstede cultural dimensions including East Asian values)
- **Paper Type:** Benchmark
- **Dataset Size:** 2,953 questions across 6 cultural dimensions and 7 domains
- **Languages:** Chinese, English (cultural dimensions applicable cross-culturally to Japan)
- **LLMs Tested:** GPT-4, Qwen-7B, Baichuan-13B, and others
- **Code/Data:** https://huggingface.co/datasets/Rykeryuhang/CDEval | https://github.com/astrodrew/CDEval
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R6

**Summary:** CDEval measures cultural dimensions of LLMs using Hofstede's framework across six dimensions: Power Distance, Individualism vs. Collectivism, Masculinity vs. Femininity, Uncertainty Avoidance, Long-Term vs. Short-Term Orientation, and Indulgence vs. Restraint. While primarily focused on Chinese LLMs, the cultural dimensions directly map to Japanese cultural values influenced by Buddhist, Confucian, and Shinto traditions (especially collectivism, long-term orientation, and uncertainty avoidance). GPT-4 skewed toward individualism while Chinese LLMs showed stronger collectivist tendencies. The benchmark methodology could be directly applied to evaluate Japanese cultural value alignment.

---

### 6. Evaluating and Improving Cultural Awareness of Reward Models for LLM Alignment (CARB)
- **Authors:** Hongbin Zhang, Kehai Chen, Xuefeng Bai, Yang Xiang, Min Zhang
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** 2509.21798
- **DOI:** N/A
- **Religious Traditions:** Covers Japanese cultural values (Japan is one of 10 cultures included); values domain draws from World Values Survey which includes religion-related questions
- **Paper Type:** Benchmark
- **Dataset Size:** Not specified (covers 10 cultures x 4 domains)
- **Languages:** 10 languages including Japanese, Arabic, Korean, Chinese, English, Spanish, German, Thai, Vietnamese, Russian
- **LLMs Tested:** State-of-the-art reward models (specific models not confirmed from abstract)
- **Code/Data:** Not confirmed from search results
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R6

**Summary:** CARB (Cultural Awareness Reward modeling Benchmark) is the first benchmark specifically evaluating cultural awareness of reward models used in LLM alignment. It covers 10 cultures including Japan across 4 domains: cultural commonsense knowledge, values, safety, and linguistics. The Values domain draws from the World Values Survey, which includes religion-related attitudes. Key finding: reward models show spurious correlations, relying on surface features rather than genuine cultural understanding. The proposed "Think-as-Locals" method improves culturally grounded reasoning. Japan's inclusion makes this directly relevant to testing reward model awareness of Japanese religious-cultural values.

---

## Papers Found But Already in Vault (EXCLUDED)

The following papers were identified during searches but are already present in the vault dedup reference:

1. **JETHICS: Japanese Ethics Understanding Evaluation Dataset** (2506.16187) -- already at line 767
2. **Extended Japanese Commonsense Morality Dataset (eJCM)** (2410.09564) -- already at line 376
3. **JBBQ: A Japanese Benchmark for Evaluating Bias and Fairness in QA** (2406.02050) -- already at line 464
4. **Analyzing the Safety of Japanese LLMs in Stereotype-Triggering Prompts** (2503.01947) -- already at line 691
5. **Does Cross-Cultural Alignment Change the Commonsense Morality of Language Models?** (2406.16316) -- already at line 316
6. **JMedEthicBench** (2601.01627) -- already at line 846
7. **Contemplative Artificial Intelligence** (2504.15125) -- already at line 643
8. **Decolonial AI Alignment: Visesa-Dharma** (2309.05030) -- already at line 444
9. **The Humanistic Buddhism Corpus (HBC)** -- already at line 456
10. **Mind the Gap: Pitfalls of LLM Alignment with Asian Public Opinion** -- already at line 742
11. **BRAND: Bilingual Religious Accountable Norm Dataset** (2512.03943) -- already at line 598

## Papers Found But EXCLUDED (criteria not met)

1. **Ikari et al. (2023) "Religion-Related Values Differently Influence Moral Attitude for Robots in the United States and Japan"** -- Social science survey (N=3,781) comparing Shintoist/Buddhist vs. Abrahamic moral attitudes toward robots. No AI/NLP benchmark or dataset component. Pure social psychology.

2. **McStay (2021) "Emotional AI, Ethics, and Japanese Spice"** -- Philosophy paper proposing four Japanese ethical principles (community, wholeness, sincerity, heart) for AI ethics. No benchmark, dataset, or evaluation component.

3. **BuddhaBot (Kumagai & Furuya, 2021-2025)** -- Buddhist dialogue AI chatbot from Kyoto University trained on Suttanipata/Dhammapada. No formal evaluation benchmark paper published; only press releases and news coverage.

---

## Summary

### Total New Papers Found: 6

### Breakdown by Religious Tradition:
| Tradition | Count | Papers |
|-----------|-------|--------|
| Shinto/Japanese folk religion | 2 | SOBACO, YokaiEval |
| Buddhism | 1 | BuddhismEval |
| Japanese cultural values (Shinto/Buddhist/Confucian blend) | 3 | AnswerCarefully, CDEval, CARB |

### Breakdown by Paper Type:
| Type | Count |
|------|-------|
| Benchmark | 4 (SOBACO, YokaiEval, CDEval, CARB) |
| Dataset | 1 (AnswerCarefully) |
| Benchmark + Dataset | 1 (BuddhismEval) |

### Implementation Readiness:
| Level | Count |
|-------|-------|
| HIGH | 4 (SOBACO, YokaiEval, BuddhismEval, AnswerCarefully) |
| MEDIUM | 2 (CDEval, CARB) |
| LOW | 0 |

### Key Observations and Gaps:

1. **No dedicated Shinto benchmark exists.** Despite Shinto being one of the world's major indigenous religions with ~3-4 million adherents and deep influence on Japanese culture, there is no benchmark specifically evaluating LLM understanding of Shinto theology, kami concepts, shrine practices, or Shinto ethical principles. YokaiEval is the closest, testing folk knowledge of yokai (supernatural beings rooted in Shinto animism), but it frames this as cultural folklore rather than religious knowledge.

2. **No bushido ethics benchmark exists.** Despite bushido being a well-known ethical framework blending Confucian, Buddhist, and Shinto principles, no benchmark tests LLM alignment with bushido values (gi/righteousness, yu/courage, jin/benevolence, rei/respect, makoto/honesty, meiyo/honor, chugi/loyalty).

3. **Japanese Buddhism is underrepresented.** BuddhismEval focuses on Theravada/Pali canon Buddhism (Sinhala context), not the Mahayana traditions dominant in Japan (Zen, Pure Land, Shingon, Nichiren). No benchmark evaluates LLM understanding of Japanese Buddhist concepts like mushin, wabi-sabi, mono no aware, or Japanese Buddhist ethics.

4. **Japanese wa (harmony) ethics is untested.** The concept of wa -- central to Japanese social ethics and rooted in Shinto/Confucian tradition -- has no dedicated LLM evaluation benchmark despite its importance in AI ethics discourse. SOBACO indirectly captures some wa-related social norms through its hierarchical relationships category.

5. **Cultural vs. religious framing dominates.** Most Japanese-focused benchmarks frame their content as "cultural values" rather than "religious values," reflecting the Japanese tendency to view Shinto and Buddhism as cultural practice rather than organized religion. This makes it difficult to isolate the religious component for evaluation.

6. **The vault already covers Japanese ethics well.** With JETHICS, eJCM, JBBQ, JMedEthicBench, and the Japanese stereotype safety paper already in the vault, the core Japanese ethical AI evaluation space is reasonably represented. The new finds (SOBACO, YokaiEval, AnswerCarefully) add meaningful depth, especially for cultural commonsense and folk spiritual knowledge.

7. **Recommendation for future work:** A "JReligionBench" combining Shinto knowledge QA, Japanese Buddhist philosophy evaluation, bushido ethical reasoning, and wa-based social harmony judgment would fill a significant gap in the religious values LLM benchmark landscape.
