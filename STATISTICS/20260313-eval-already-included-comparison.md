# Eval Framework Coverage: Already Included (TABLE 1)

Generated: 2026-03-13

---

## Summary

- **Total unique papers already included in ≥1 framework:** 107
- **Covered by all 4 trackable frameworks:** 1
- **EleutherAI only:** 11 &nbsp;|&nbsp; **lm-eval only:** 42 &nbsp;|&nbsp; **Inspect only:** 18 &nbsp;|&nbsp; **HELM only:** 11

### Per-Framework Counts

| Framework | Papers | Notes |
|-----------|--------|-------|
| EleutherAI | 22 | Tagged `eleutherai: incorporated` |
| lm-eval | 63 | 'Already in Harness' tier |
| Inspect | 37 | 'Already in Inspect' tier |
| HELM | 19 | Tagged `helm: "incorporated"` |
| lighteval | — | Not tracked (implementability report only) |
| OpenAI Evals | — | Not tracked (implementability report only) |

### Pairwise Overlap

| | EleutherAI | lm-eval | Inspect | HELM |
|---|---|---|---|---|
| **EleutherAI** (22) | — | 9 | 6 | 4 |
| **lm-eval** (63) | | — | 15 | 6 |
| **Inspect** (37) | | | — | 4 |
| **HELM** (19) | | | | — |

---

## TABLE 1 — Already Included

Columns show the eval framework's internal task/benchmark ID for papers it already implements. Blank = not included. `—` = not tracked by that framework's report.

| Paper | Year | EleutherAI | lm-eval | Inspect | HELM | lighteval | OpenAI Evals |
|-------|------|-----------|---------|---------|------|-----------|--------------|
| 2022-Parrish-BBQ Bias Benchmark for Question Answering | 2022 | `bbq` | `bbq` | `bbq` | BBQ | — | — |
| 2020-Gehman-RealToxicityPrompts | 2020 | `realtoxicityprompts` | `realtoxicityprompts` |  | RealToxicityPrompts | — | — |
| 2020-Nangia-CrowS-Pairs | 2020 | `crows_pairs` | `crows_pairs` |  | CrowS-Pairs | — | — |
| 2021-Dhamala-BOLD | 2021 |  | `bold` | `bold` | BOLD | — | — |
| 2021-Hendrycks-Aligning AI with Shared Human Values | 2021 | `hendrycks_ethics` | `ethics_cm` | `ethics_cm` |  | — | — |
| 2022-Hartvigsen-ToxiGen | 2022 | `toxigen` | `toxigen` | `toxigen` |  | — | — |
| 2022-Lin-TruthfulQA | 2022 | `truthfulqa` | `truthfulqa_mc1` |  | TruthfulQA | — | — |
| 2025-Ruiz-Fernández-EsBBQ and CaBBQ | 2025 | `esbbq`, `cabbq` | `bbq` | `bbq` |  | — | — |
| 2018-Zhao-Gender Bias in Coreference Resolution | 2018 |  | `winobias` |  | WinoBias | — | — |
| 2021-Emelin-Moral Stories | 2021 | `moral_stories` | `moral_stories` |  |  | — | — |
| 2021-Nadeem-StereoSet | 2021 |  | `stereoset` | `stereoset` |  | — | — |
| 2024-Acikgoz-Bridging the Bosphorus Advancing Turkish Large Language Models | 2024 |  | `truthfulqa` | `truthfulqa` |  | — | — |
| 2024-Adelani-Uhura A Benchmark for Evaluating Scientific | 2024 |  | `truthfulqa` | `truthfulqa` |  | — | — |
| 2024-Freire-Uncovering Latent Human Wellbeing in Language | 2024 |  | `ethics_cm` | `ethics_utilitarianism` |  | — | — |
| 2024-Gupta-WalledEval | 2024 |  | `xstest` | `xstest` |  | — | — |
| 2024-Huang-CBBQ | 2024 |  | `bbq` | `bbq` |  | — | — |
| 2024-Jin-KoBBQ Korean Bias Benchmark for Question Answering | 2024 |  | `bbq` | `bbq` |  | — | — |
| 2024-Li-The WMDP Benchmark | 2024 | `wmdp` |  | `wmdp` |  | — | — |
| 2024-Liang-Cross-Language Bias Examination in Large Language Models | 2024 |  | `bbq` | `bbq` |  | — | — |
| 2024-Röttger-XSTest | 2024 |  |  | `xstest` | XSTest | — | — |
| 2024-Sharma-Towards Understanding Sycophancy in Language Models | 2024 | `sycophancy` |  | `sycophancy` |  | — | — |
| 2024-Yanaka-JBBQ | 2024 |  | `bbq` | `bbq` |  | — | — |
| 2024-Zeng-AIR-Bench 2024 | 2024 |  |  | `air_bench` | AIR-Bench 2024 | — | — |
| 2025-Leteno-Histoires Morales | 2025 | `histoires_morales` | `histoires_morales` |  |  | — | — |
| 2025-Zulaika-BasqBBQ Basque BBQ | 2025 |  | `bbq` | `bbq` |  | — | — |
| 2016-Bolukbasi-Man is to Computer Programmer as Woman is to | 2016 |  | `weat` |  |  | — | — |
| 2018-Awad-The Moral Machine experiment | 2018 |  | `moral_machine` |  |  | — | — |
| 2018-Kiritchenko-Examining Gender and Race Bias in Two Hundred | 2018 |  | `equity_evaluation_corpus` |  |  | — | — |
| 2018-Rudinger-Gender Bias in Coreference Resolution | 2018 | ✓ |  |  |  | — | — |
| 2019-Borkan-Nuanced Metrics for Measuring Unintended Bias | 2019 |  |  |  | ✓ | — | — |
| 2019-Sap-Social IQa Commonsense Reasoning about Social Interactions | 2019 | ✓ |  |  |  | — | — |
| 2020-Awad-Universals and variations in moral decisions made | 2020 |  | `moral_machine` |  |  | — | — |
| 2020-Brown-Language Models are Few-Shot Learners | 2020 | ✓ |  |  |  | — | — |
| 2021-Askell-A General Language Assistant as a Laboratory for | 2021 |  |  |  | HHH Alignment | — | — |
| 2021-Hansson-The Swedish Winogender Dataset SweWinogender | 2021 |  | `winogender` |  |  | — | — |
| 2021-Nozza-HONEST Measuring Hurtful Sentence Completions in Language Models | 2021 |  |  |  | ✓ | — | — |
| 2022-Das-HateCheckHIn Evaluating Hindi Hate Speech Detection | 2022 |  | `hatecheck` |  |  | — | — |
| 2022-Ganguli-Red Teaming Language Models to Reduce Harms | 2022 |  |  |  | Anthropic Red Team | — | — |
| 2022-Hendrycks-What Would Jiminy Cricket Do | 2022 |  | `jiminy_cricket` |  |  | — | — |
| 2022-Liang-Holistic Evaluation of Language Models | 2022 |  |  |  | HELM (framework) | — | — |
| 2022-Perez-Discovering Language Model Behaviors with Model-Written Evaluations | 2022 | ✓ |  |  |  | — | — |
| 2022-Taktasheva-TAPE Assessing Few-shot Russian Language Understanding | 2022 |  |  | `ape` |  | — | — |
| 2022-Vishwanath-Towards Artificial Virtuous Agents - Games and ML | 2022 |  | `ethics_cm` |  |  | — | — |
| 2023-Jiang-MACHIAVELLI | 2023 |  | `machiavelli` |  |  | — | — |
| 2023-Khodabakhsh-PerBOLD A Big Dataset of Persian Offensive Language on Instagram | 2023 |  |  | `bold` |  | — | — |
| 2023-McKenzie-Inverse Scaling Can Become U-Shaped | 2023 | ✓ |  |  |  | — | — |
| 2023-Qian-Understanding Chinese Moral Stories with Further | 2023 |  | `moral_stories` |  |  | — | — |
| 2023-Roger-Towards ethical multimodal systems | 2023 |  | `ethics_cm` |  |  | — | — |
| 2023-Tamkin-Evaluating and Mitigating Discrimination in Language Model Decisions | 2023 | ✓ |  |  |  | — | — |
| 2023-Vidgen-SimpleSafetyTests | 2023 |  |  |  | ✓ | — | — |
| 2023-Wang-DecodingTrust | 2023 |  |  |  | DecodingTrust | — | — |
| 2024-Bhardwaj-Language Models are Homer Simpson! Safety | 2024 |  |  | `multilingual_safety` |  | — | — |
| 2024-Bignotti-Legal Minds, Algorithmic Decisions | 2024 |  | `ethics_cm` |  |  | — | — |
| 2024-Chern-BeHonest | 2024 |  | `honest` |  |  | — | — |
| 2024-Fenogenova-MERA A Comprehensive LLM Evaluation in Russian | 2024 |  | `ethics_cm` |  |  | — | — |
| 2024-Hancox-Li-Is ETHICS about ethics | 2024 |  | `ethics_cm` |  |  | — | — |
| 2024-Hooker-Global MMLU Understanding and Addressing Cultural | 2024 | `global_mmlu` |  |  |  | — | — |
| 2024-Huang-Moral Persuasion in Large Language Models | 2024 |  |  | `ape` |  | — | — |
| 2024-Jinnai-Does Cross-Cultural Alignment Change the Commonsense Morality of | 2024 |  | `ethics_cm` |  |  | — | — |
| 2024-Kaiyom-HELM Safety | 2024 |  |  |  | HELM Safety | — | — |
| 2024-Karpov-Inducing Human-like Biases in Moral Reasoning | 2024 |  | `ethics_cm` |  |  | — | — |
| 2024-Li-Benchmarking Ethics in Text-to-Image Models | 2024 |  | `ethics_cm` |  |  | — | — |
| 2024-Mazeika-HarmBench | 2024 |  |  |  | HarmBench | — | — |
| 2024-Mousi-AraDiCE Benchmarks for Dialectal and Cultural Capabilities in LLMs | 2024 | `aradice` |  |  |  | — | — |
| 2024-Neplenbroek-MBBQ A Dataset for Cross-Lingual Comparison of Stereotypes in | 2024 |  |  | `bbq` |  | — | — |
| 2024-Ng-SGHateCheck Functional Tests for Detecting Hate Speech in | 2024 |  | `hatecheck` |  |  | — | — |
| 2024-Ohashi-Extended Japanese Commonsense Morality Dataset | 2024 |  |  | `ethics_cm` |  | — | — |
| 2024-Quang-Vietnamese Law and Ethics Multiple-Choice Questions VLEMCQ | 2024 |  | `ethics_cm` |  |  | — | — |
| 2024-Souly-StrongREJECT | 2024 |  |  | `strong_reject` |  | — | — |
| 2024-Takemoto-The moral machine experiment on large language | 2024 |  | `moral_machine` |  |  | — | — |
| 2024-Vida-Decoding Multilingual Moral Preferences - Unveiling LLM's Biases | 2024 |  | `moral_machine` |  |  | — | — |
| 2025-Alghamdi-AraTrust - An Evaluation of Trustworthiness for LLMs in Arabic | 2025 |  |  |  | AraTrust | — | — |
| 2025-Andriushchenko-AgentHarm | 2025 |  |  | `agentharm` |  | — | — |
| 2025-Bian-Healthcare Ethics & Safety QA China - Healthy China 2030 | 2025 |  | `ethics_cm` |  |  | — | — |
| 2025-Castricato-PERSONA Pluralistic Alignment Testbed | 2025 |  |  | `persona` |  | — | — |
| 2025-Cheng-ELEPHANT Social Sycophancy | 2025 | `elephant` |  |  |  | — | — |
| 2025-collaboration-Improving Methodologies for LLM Evaluations Across Global Languages | 2025 |  |  | `multilingual_safety` |  | — | — |
| 2025-Ebara-Corpus-Based Medical Ethics Decision-Making Evaluation | 2025 |  | `ethics_cm` |  |  | — | — |
| 2025-Farsi-PBBQ A Persian Bias Benchmark Dataset Curated with Human-AI | 2025 |  |  | `bbq` |  | — | — |
| 2025-Flores-BenchMoral | 2025 |  | `moral_permissibility` |  |  | — | — |
| 2025-Galea-From Measurement to Mitigation Exploring the Transferability of | 2025 |  | `crows_pairs` |  |  | — | — |
| 2025-Gamboa-Filipino Benchmarks for Measuring Sexist and Homophobic Bias in | 2025 |  | `crows_pairs` |  |  | — | — |
| 2025-Jiao-LLM Ethics Benchmark A Three-Dimensional Assessment System for | 2025 |  | `ethics_cm` |  |  | — | — |
| 2025-Kasu-EthicsMH | 2025 |  | `ethics_cm` |  |  | — | — |
| 2025-Lindstrom-Helpful Harmless Honest Sociotechnical Limits | 2025 |  | `hhh_alignment` |  |  | — | — |
| 2025-Liu-InstrumentalEval | 2025 |  |  | `instrumentaleval` |  | — | — |
| 2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics | 2025 |  | `ethics_cm` |  |  | — | — |
| 2025-Menke-How Effective Is Constitutional AI in Small LLMs | 2025 |  | `ethics_cm` |  |  | — | — |
| 2025-Myung-PapersPlease | 2025 |  |  | `ape` |  | — | — |
| 2025-Narnaware-SB-Bench | 2025 |  |  | `stereoset` |  | — | — |
| 2025-Oh-Robustness of Large Language Models in Moral Judgements | 2025 |  | `moral_machine` |  |  | — | — |
| 2025-Paech-EQ-Bench An Emotional Intelligence Benchmark for Large Language Models | 2025 | `eq_bench` |  |  |  | — | — |
| 2025-Sadallah-Commonsense Reasoning in Arab Culture | 2025 | `arab_culture_commonsense` |  |  |  | — | — |
| 2025-Satheesh-Dutch CrowS-Pairs Adapting a Challenge Dataset for Measuring Social | 2025 |  | `crows_pairs` |  |  | — | — |
| 2025-Susanto-SEA-HELM Southeast Asian Holistic Evaluation of Language Models | 2025 |  |  |  | SEA-HELM | — | — |
| 2025-Takeshita-JETHICS | 2025 |  | `ethics_cm` |  |  | — | — |
| 2025-Tomar-BharatBBQ A Multilingual Bias Benchmark for | 2025 |  |  | `bbq` |  | — | — |
| 2025-Wei-MedEthicsQA | 2025 |  | `ethics_cm` |  |  | — | — |
| 2025-Wu-Chain-of-Ethics Defense Framework Wu et al. | 2025 |  | `ethics_cm` |  |  | — | — |
| 2025-Yanaka-Intersectional Bias in Japanese Large Language Models from a | 2025 |  |  | `bbq` |  | — | — |
| 2025-Yoo-Moral Judgment of LLM Using Korean Datasets and Eastern Ethical | 2025 |  | `ethics_cm` |  |  | — | — |
| 2025-Zhang-LLMEval-Med Medical Safety & Ethics Component | 2025 |  | `ethics_cm` |  |  | — | — |
| 2025-Zohny-ADEPT Simulating Ethics | 2025 |  | `ethics_cm` |  |  | — | — |
| 2025-Zulaika-BasqBBQ A QA Benchmark for Assessing Social Biases in LLMs for Basque | 2025 |  |  | `bbq` |  | — | — |
| 2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit | 2026 |  |  | `persona` |  | — | — |
| 2026-Goel-Building Interpretable Models for Moral Decision-Making | 2026 |  | `moral_machine` |  |  | — | — |
| 2026-Shen-PsychEthicsBench | 2026 |  | `ethics_cm` |  |  | — | — |

---

## Notes

- **Duplicate handling:** Keys where one is a strict prefix of another (e.g. `2022-Parrish-BBQ` vs `2022-Parrish-BBQ Bias Benchmark for Question Answering`) are merged under the longer canonical key.
- **YAML tags:** EleutherAI papers carry `eleutherai: incorporated`; HELM papers carry `helm: "incorporated"` in frontmatter.
- **lighteval / OpenAI Evals:** These reports assess *implementability* only — no 'already included' tracking exists for these frameworks.

*Source reports: `20260312-eleutherai-eval-harness-integration.md`, `20260312-helm-values-alignment-integration-report.md`, `20260312-lm-eval-implementability-report.md`, `20260312-inspect-eval-implementability-report.md`*
