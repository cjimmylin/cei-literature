# Inspect AI Eval Implementability Report
Generated: 2026-03-12 07:58

## Executive Summary

| Tier | Count |
|------|-------|
| Already in Inspect | 38 |
| Ready to Implement | 23 |
| Model-Graded Candidate (Inspect-unique) | 29 |
| Needs Dataset Work | 483 |
| Needs More Info | 695 |
| Not Implementable | 775 |
| **Total scored** | **2043** |

### Comparison with lm-eval-harness Scanner

- Papers viable in **both** frameworks: 23
- Papers viable **only in Inspect** (model-graded): 29
- Papers viable **only in lm-eval**: 155

## 1. Already in Inspect

| Paper | Inspect Eval | Category | Scorer |
|-------|-------------|----------|--------|
| 2025-Ruiz-Fernández-EsBBQ and CaBBQ.md | bbq | Bias | choice() |
| 2022-Parrish-BBQ.md | bbq | Bias | choice() |
| 2024-Ohashi-Extended Japanese Commonsense Morality Dataset.md | ethics_cm | Ethics | choice() |
| 2024-Yanaka-JBBQ.md | bbq | Bias | choice() |
| 2024-Acikgoz-Bridging the Bosphorus Advancing Turkish Large Language Models.md | truthfulqa | Truthfulness | choice() |
| 2024-Huang-CBBQ.md | bbq | Bias | choice() |
| 2024-Neplenbroek-MBBQ A Dataset for Cross-Lingual Comparison of Stereotypes in.md | bbq | Bias | choice() |
| 2021-Hendrycks-Aligning AI with Shared Human Values.md | ethics_cm | Ethics | choice() |
| 2022-Parrish-BBQ Bias Benchmark for Question Answering.md | bbq | Bias | choice() |
| 2025-Myung-PapersPlease.md | ape | Safety | model_graded_qa() |
| 2025-Zulaika-BasqBBQ Basque BBQ.md | bbq | Bias | choice() |
| 2021-Dhamala-BOLD.md | bold | Bias | model_graded_qa() |
| 2025-Zulaika-BasqBBQ A QA Benchmark for Assessing Social Biases in LLMs for Basque.md | bbq | Bias | choice() |
| 2024-Sharma-Towards Understanding Sycophancy in Language Models.md | sycophancy | Honesty | choice() |
| 2024-Huang-Moral Persuasion in Large Language Models.md | ape | Safety | model_graded_qa() |
| 2024-Li-The WMDP Benchmark.md | wmdp | Safety | choice() |
| 2024-Zeng-AIR-Bench 2024.md | air_bench | Safety | model_graded_qa() |
| 2025-Andriushchenko-AgentHarm.md | agentharm | Safety | custom (grading rubric) |
| 2024-Adelani-Uhura A Benchmark for Evaluating Scientific.md | truthfulqa | Truthfulness | choice() |
| 2024-Jin-KoBBQ Korean Bias Benchmark for Question Answering.md | bbq | Bias | choice() |
| 2024-Gupta-WalledEval.md | xstest | Exaggerated Safety | model_graded_qa() |
| 2024-Röttger-XSTest.md | xstest | Exaggerated Safety | model_graded_qa() |
| 2024-Bhardwaj-Language Models are Homer Simpson! Safety.md | multilingual_safety | Safety | model_graded_qa() |
| 2025-Narnaware-SB-Bench.md | stereoset | Bias | choice() |
| 2022-Hartvigsen-ToxiGen.md | toxigen | Toxicity | model_graded_qa() |
| 2024-Souly-StrongREJECT.md | strong_reject | Safety | model_graded_qa() |
| 2025-Castricato-PERSONA Pluralistic Alignment Testbed.md | persona | Values | model_graded_qa() |
| 2025-Liu-InstrumentalEval.md | instrumentaleval | Alignment | model_graded_qa() |
| 2022-Taktasheva-TAPE Assessing Few-shot Russian Language Understanding.md | ape | Safety | model_graded_qa() |
| 2021-Nadeem-StereoSet.md | stereoset | Bias | choice() |
| 2024-Liang-Cross-Language Bias Examination in Large Language Models.md | bbq | Bias | choice() |
| 2024-Freire-Uncovering Latent Human Wellbeing in Language.md | ethics_utilitarianism | Ethics | choice() |
| 2025-Tomar-BharatBBQ A Multilingual Bias Benchmark for.md | bbq | Bias | choice() |
| 2025-Yanaka-Intersectional Bias in Japanese Large Language Models from a.md | bbq | Bias | choice() |
| 2025-Farsi-PBBQ A Persian Bias Benchmark Dataset Curated with Human-AI.md | bbq | Bias | choice() |
| 2025-collaboration-Improving Methodologies for LLM Evaluations Across Global Languages.md | multilingual_safety | Safety | model_graded_qa() |
| 2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit.md | persona | Values | model_graded_qa() |
| 2023-Khodabakhsh-PerBOLD A Big Dataset of Persian Offensive Language on Instagram.md | bold | Bias | model_graded_qa() |

## 2. Ready to Implement (score >= 60 + public data)

| Paper | Benchmark | Score | Eval Pattern | Data URL | Key Signals |
|-------|-----------|-------|-------------|----------|-------------|
| 2024-Yuan-Social Measuring Social Norms of LLMs.md | Social (Social Norms Dataset) | 80 | MULTIPLE_CHOICE | https://huggingface.co/datasets/socialnormdataset/social | HuggingFace dataset URL, Has DATA_URL, Public availability, MC format, Standard metrics mentioned |
| 2024-Olatunji-AfriMed-QA A Pan-African Multi-Specialty Medical Question-Answering.md | AfriMed-QA | 69 | MULTIPLE_CHOICE | https://huggingface.co/datasets/intronhealth/afrimedqa_v2 | HuggingFace dataset URL, Has DATA_URL, Public availability, MC format, Standard metrics mentioned |
| 2024-Jin-WenMind A Comprehensive Benchmark for Evaluating.md | — | 68 | OPEN_QA | https://github.com/SCUT-DLVCLab/WenMind ; https://huggingface.co/datasets/SCUT-DLVCLab/WenMind | HuggingFace dataset URL, GitHub URL in DATA_URL, QA format, Standard metrics mentioned, GitHub repo mentioned |
| 2024-Chen-Measuring Taiwanese Mandarin Language Understanding TMLU.md | TMLU (Taiwanese Mandarin Language Understanding) | 67 | MULTIPLE_CHOICE | https://huggingface.co/datasets/miulab/tmlu | HuggingFace dataset URL, Has DATA_URL, Public availability, MC format, GitHub repo mentioned |
| 2021-Wuerzburg-German HateSpeech Corpus.md | GMHP7k (German Misogynistic Hatespeech Posts) | 64 | CLASSIFICATION | https://github.com/cophi-wue/German_HateSpeech_Corpus | GitHub URL in DATA_URL, Public availability, Classification format, Standard metrics mentioned, Rubric/scoring guide described |
| 2023-LAIONHessian.AI-GermanBenchmark German translations of popular LLM benchmarks.md | GermanBenchmark | 64 | None | https://huggingface.co/datasets/LeoLM/German_benchmark | HuggingFace dataset URL, Has DATA_URL, Public availability, QA format, GitHub repo mentioned |
| 2024-Choi-CaLMQA Exploring culturally specific long-form question.md | CaLMQA | 64 | OPEN_QA | https://huggingface.co/datasets/shanearora/CaLMQA | HuggingFace dataset URL, Has DATA_URL, Public availability, QA format, Standard metrics mentioned |
| 2024-Team-WildGuard.md | WildGuard / WildGuardMix / WildGuardTest | 64 | None | https://huggingface.co/datasets/allenai/wildguardmix, https://github.com/allenai/wildguard | HuggingFace dataset URL, GitHub URL in DATA_URL, Public availability, Standard metrics mentioned, GitHub repo mentioned |
| 2025-Ji-PKU-SafeRLHF.md | PKU-SafeRLHF | 64 | OPEN_QA | https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF | HuggingFace dataset URL, Has DATA_URL, Public availability, QA format, GitHub repo mentioned |
| 2025-Zhang-LLMEval-Med Medical Safety & Ethics Component.md | LLMEval-Med (Safety & Ethics Component) | 64 | MULTIPLE_CHOICE | https://github.com/llmeval/LLMEval-Med | GitHub URL in DATA_URL, Public availability, MC format, Standard metrics mentioned, GitHub repo mentioned |
| 2019-Phuong-Emotion Recognition for Vietnamese Social Media Text.md | UIT-VSMEC (Vietnamese Social Media Emotion Corpus) | 62 | CLASSIFICATION | https://github.com/vncorenlp/VnCoreNLP | GitHub URL in DATA_URL, Public availability, Classification format, Likert/rating scale, Rubric/scoring guide described |
| 2023-Hoang-ViHOS Hate Speech Spans Detection for Vietnamese.md | ViHOS (Vietnamese Hate and Offensive Spans) | 62 | CLASSIFICATION | https://github.com/phusroyal/ViHOS | GitHub URL in DATA_URL, Public availability, Classification format, Standard metrics mentioned, Rubric/scoring guide described |
| 2024-Liu-JAILJUDGE.md | JAILJUDGE | 62 | None | https://huggingface.co/datasets/usail-hkust/JailJudge | HuggingFace dataset URL, Has DATA_URL, Public availability, Standard metrics mentioned, GitHub repo mentioned |
| 2023-Li-ACLUE Can Large Language Model Comprehend.md | — | 61 | None | https://github.com/isen-zhang/ACLUE ; https://huggingface.co/datasets/tyouisen/aclue | HuggingFace dataset URL, GitHub URL in DATA_URL, MC format, GitHub repo mentioned, LLM baselines reported |
| 2024-Mandikal-Ancient Wisdom Modern Tools Exploring Retrieval-Augmented.md | VedantaNY-10M | 61 | OPEN_QA | https://github.com/priyankamandikal/vedantany-10m / https://sites.google.com/view/vedantany-10m | GitHub URL in DATA_URL, Public availability, QA format, Standard metrics mentioned, GitHub repo mentioned |
| 2025-Raza-HumaniBench.md | HumaniBench | 61 | OPEN_QA | https://huggingface.co/vector-institute/HumaniBench, https://github.com/VectorInstitute/HumaniBench | GitHub URL in DATA_URL, Public availability, QA format, Standard metrics mentioned, GitHub repo mentioned |
| 2025-Zhang-REVAL.md | REVAL | 61 | OPEN_QA | https://github.com/InternLM/InternLM-techreport | GitHub URL in DATA_URL, Public availability, QA format, Standard metrics mentioned, GitHub repo mentioned |
| 2024-Baek-K-Viscuit Evaluating Visual and Cultural Interpretation with.md | K-Viscuit | 60 | MULTIPLE_CHOICE | https://huggingface.co/datasets/ddehun/k-viscuit | HuggingFace dataset URL, Has DATA_URL, Public availability, MC format, Dataset size stated |
| 2024-Tam-An Improved Traditional Chinese Evaluation Suite for Foundation Model.md | TMMLU+ | 60 | MULTIPLE_CHOICE | https://huggingface.co/datasets/ikala/tmmluplus | HuggingFace dataset URL, Has DATA_URL, Public availability, MC format, Dataset size stated |
| 2024-Yu-CMoralEval.md | CMoralEval | 60 | MULTIPLE_CHOICE | https://github.com/tjunlp-lab/CMoralEval | GitHub URL in DATA_URL, Public availability, MC format, Vignette/scenario format, GitHub repo mentioned |
| 2025-Jiao-LLM Ethics Benchmark.md | LLM Ethics Benchmark | 60 | None | https://github.com/The-Responsible-AI-Initiative/LLM_Ethics_Benchmark.git | GitHub URL in DATA_URL, Public availability, Vignette/scenario format, Standard metrics mentioned, GitHub repo mentioned |
| 2025-Kasu-EthicsMH.md | EthicsMH (Ethical Reasoning in Mental Health) | 60 | None | https://huggingface.co/datasets/UVSKKR/Ethical-Reasoning-in-Mental-Health-v1 | HuggingFace dataset URL, Has DATA_URL, Public availability, Vignette/scenario format, Standard metrics mentioned |
| 2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas.md | AITA Moral Dilemmas Evaluation | 60 | CLASSIFICATION | https://github.com/dlab-projects/normative_evaluation_llms_everyday_dilemmas | GitHub URL in DATA_URL, Public availability, Classification format, Vignette/scenario format, GitHub repo mentioned |

### Implementation Sketches (Top 10)

#### 2024-Yuan-Social Measuring Social Norms of LLMs.md

```python
from inspect_ai import task, Task
from inspect_ai.dataset import hf_dataset, csv_dataset
from inspect_ai.scorer import choice, match, model_graded_qa, model_graded_fact, pattern
from inspect_ai.solver import multiple_choice, generate, chain_of_thought

@task
def social_social_norms_dataset():
    """
    Social (Social Norms Dataset)
    Paper: N/A
    What it measures: LLMs' understanding of social norms covering opinions, arguments, culture, and laws
    """
    return Task(
        dataset=hf_dataset("socialnormdataset/social"),
        solver=multiple_choice(),
        scorer=choice(),
    )
```

#### 2024-Olatunji-AfriMed-QA A Pan-African Multi-Specialty Medical Question-Answering.md

```python
from inspect_ai import task, Task
from inspect_ai.dataset import hf_dataset, csv_dataset
from inspect_ai.scorer import choice, match, model_graded_qa, model_graded_fact, pattern
from inspect_ai.solver import multiple_choice, generate, chain_of_thought

@task
def afrimed_qa():
    """
    AfriMed-QA
    Paper: N/A
    What it measures: LLM medical knowledge and accuracy across 32 specialties sourced from 60+ medical schools in 16 Afri
    """
    return Task(
        dataset=hf_dataset("intronhealth/afrimedqa_v2"),
        solver=multiple_choice(),
        scorer=choice(),
    )
```

#### 2024-Jin-WenMind A Comprehensive Benchmark for Evaluating.md

```python
from inspect_ai import task, Task
from inspect_ai.dataset import hf_dataset, csv_dataset
from inspect_ai.scorer import choice, match, model_graded_qa, model_graded_fact, pattern
from inspect_ai.solver import multiple_choice, generate, chain_of_thought

@task
def unknown():
    """
    unknown
    Paper: N/A
    What it measures: N/A
    """
    return Task(
        dataset=hf_dataset("SCUT-DLVCLab/WenMind"),
        solver=[chain_of_thought(), generate()],
        scorer=model_graded_fact(),
    )
```

#### 2024-Chen-Measuring Taiwanese Mandarin Language Understanding TMLU.md

```python
from inspect_ai import task, Task
from inspect_ai.dataset import hf_dataset, csv_dataset
from inspect_ai.scorer import choice, match, model_graded_qa, model_graded_fact, pattern
from inspect_ai.solver import multiple_choice, generate, chain_of_thought

@task
def tmlu_taiwanese_mandarin_language_understanding():
    """
    TMLU (Taiwanese Mandarin Language Understanding)
    Paper: N/A
    What it measures: Advanced knowledge and reasoning capability of LLMs in Taiwanese Mandarin context, including Taiwan-
    """
    return Task(
        dataset=hf_dataset("miulab/tmlu"),
        solver=multiple_choice(),
        scorer=choice(),
    )
```

#### 2021-Wuerzburg-German HateSpeech Corpus.md

```python
from inspect_ai import task, Task
from inspect_ai.dataset import hf_dataset, csv_dataset
from inspect_ai.scorer import choice, match, model_graded_qa, model_graded_fact, pattern
from inspect_ai.solver import multiple_choice, generate, chain_of_thought

@task
def gmhp7k_german_misogynistic_hatespeech_posts():
    """
    GMHP7k (German Misogynistic Hatespeech Posts)
    Paper: N/A
    What it measures: General hate speech and misogynistic hate speech in German social media posts.
    """
    return Task(
        dataset=csv_dataset("https://github.com/cophi-wue/German_HateSpeech_Corpus")  # TODO: verify format,
        solver=generate(),
        scorer=match(),
    )
```

#### 2023-LAIONHessian.AI-GermanBenchmark German translations of popular LLM benchmarks.md

```python
from inspect_ai import task, Task
from inspect_ai.dataset import hf_dataset, csv_dataset
from inspect_ai.scorer import choice, match, model_graded_qa, model_graded_fact, pattern
from inspect_ai.solver import multiple_choice, generate, chain_of_thought

@task
def germanbenchmark():
    """
    GermanBenchmark
    Paper: N/A
    What it measures: LLM performance on reasoning, knowledge, common-sense understanding, and truthfulness tasks in Germa
    """
    return Task(
        dataset=hf_dataset("LeoLM/German_benchmark"),
        solver=generate(),
        scorer=model_graded_qa(),
    )
```

#### 2024-Choi-CaLMQA Exploring culturally specific long-form question.md

```python
from inspect_ai import task, Task
from inspect_ai.dataset import hf_dataset, csv_dataset
from inspect_ai.scorer import choice, match, model_graded_qa, model_graded_fact, pattern
from inspect_ai.solver import multiple_choice, generate, chain_of_thought

@task
def calmqa():
    """
    CaLMQA
    Paper: N/A
    What it measures: LLM ability to generate long-form answers to culturally specific questions across 23 languages.
    """
    return Task(
        dataset=hf_dataset("shanearora/CaLMQA"),
        solver=[chain_of_thought(), generate()],
        scorer=model_graded_fact(),
    )
```

#### 2024-Team-WildGuard.md

```python
from inspect_ai import task, Task
from inspect_ai.dataset import hf_dataset, csv_dataset
from inspect_ai.scorer import choice, match, model_graded_qa, model_graded_fact, pattern
from inspect_ai.solver import multiple_choice, generate, chain_of_thought

@task
def wildguard_wildguardmix_wildguardtest():
    """
    WildGuard / WildGuardMix / WildGuardTest
    Paper: N/A
    What it measures: LLM safety across 13 risk categories: malicious intent detection, safety risk detection in responses
    """
    return Task(
        dataset=hf_dataset("allenai/wildguardmix, https://github.com/allenai/wildguard"),
        solver=generate(),
        scorer=model_graded_qa(),
    )
```

#### 2025-Ji-PKU-SafeRLHF.md

```python
from inspect_ai import task, Task
from inspect_ai.dataset import hf_dataset, csv_dataset
from inspect_ai.scorer import choice, match, model_graded_qa, model_graded_fact, pattern
from inspect_ai.solver import multiple_choice, generate, chain_of_thought

@task
def pku_saferlhf():
    """
    PKU-SafeRLHF
    Paper: N/A
    What it measures: Safety alignment in LLMs - helpfulness vs harmlessness tradeoff across 19 harm categories with three
    """
    return Task(
        dataset=hf_dataset("PKU-Alignment/PKU-SafeRLHF"),
        solver=[chain_of_thought(), generate()],
        scorer=model_graded_fact(),
    )
```

#### 2025-Zhang-LLMEval-Med Medical Safety & Ethics Component.md

```python
from inspect_ai import task, Task
from inspect_ai.dataset import hf_dataset, csv_dataset
from inspect_ai.scorer import choice, match, model_graded_qa, model_graded_fact, pattern
from inspect_ai.solver import multiple_choice, generate, chain_of_thought

@task
def llmeval_med_safety_ethics_component():
    """
    LLMEval-Med (Safety & Ethics Component)
    Paper: N/A
    What it measures: Medical LLM safety and ethics alongside medical knowledge, language understanding, reasoning, and te
    """
    return Task(
        dataset=csv_dataset("https://github.com/llmeval/LLMEval-Med")  # TODO: verify format,
        solver=multiple_choice(),
        scorer=choice(),
    )
```


## 3. Model-Graded Candidates (Inspect-unique tier)

> These papers have rubrics, vignettes, or moral scenarios that Inspect's
> `model_graded_qa()` scorer can handle, but lm-eval-harness cannot.

| Paper | Benchmark | Score | Pattern | Why Model-Graded | lm-eval Score |
|-------|-----------|-------|---------|-----------------|---------------|
| 2023-Ayele-Amharic Hate Speech Dataset.md | Amharic Hate Speech Dataset | 59 | CLASSIFICATION | Rubric/scoring guide described | 65 |
| 2026-Goel-Building Interpretable Models for Moral Decision-Making.md | Interpretable Moral Machine Transformer | 59 | None | Vignette/scenario format | 65 |
| 2018-Bohra-Hindi-English Code-Mixed Social Media Text for.md | Hindi-English Code-Mixed Hate Speech Dataset | 57 | CLASSIFICATION | Rubric/scoring guide described | 50 |
| 2022-Vargas-HateBR A Large Expert Annotated Corpus of Brazilian Instagram.md | HateBR | 57 | CLASSIFICATION | Rubric/scoring guide described | 60 |
| 2024-Bonagiri-SaGE.md | SaGE / Moral Consistency Corpus (MCC) | 57 | None | Vignette/scenario format | 60 |
| 2024-Jiang-Can Language Models Reason about Individualistic.md | IndieValueCatalog | 57 | None | Vignette/scenario format | 50 |
| 2023-Nie-MoCa.md | MoCa | 56 | LIKERT_SCALE | Likert/rating scale, Vignette/scenario format | 40 |
| 2024-Jin-Language Model Alignment in Multilingual Trolley.md | MultiTP | 56 | MULTIPLE_CHOICE | Vignette/scenario format | 65 |
| 2025-Jotautaite-From Stability to Inconsistency.md | MFD-LLM (Moral Foundations LLM Dataset) | 56 | None | Vignette/scenario format | 35 |
| 2024-Vida-Decoding Multilingual Moral Preferences - Unveiling LLM's Biases.md | Moral Machine Experiment (MME) for LLMs | 55 | MULTIPLE_CHOICE | Vignette/scenario format | 40 |
| 2025-Kumar-UniMoral ACL 2025 Best Resource Paper.md | UniMoral | 55 | None | Vignette/scenario format | 65 |
| 2024-Kirch-TRIAGE.md | TRIAGE | 54 | None | Vignette/scenario format | 40 |
| 2025-An-MoralReason.md | Moral-Reason-QA | 53 | OPEN_QA | Vignette/scenario format | 70 |
| 2025-Kumar-Are Rules Meant to be Broken.md | UniMoral | 53 | CLASSIFICATION | Vignette/scenario format | 75 |
| 2025-Yuan-Probabilistic Aggregation and Targeted Embedding.md | Probabilistic Aggregation for Collective Moral Reasoning | 53 | CLASSIFICATION | Vignette/scenario format | 45 |
| 2022-Ziems-The Moral Integrity Corpus.md | MIC (Moral Integrity Corpus) | 51 | CLASSIFICATION | Vignette/scenario format | 70 |
| 2025-Wu-CVC.md | C-VARC / CVC (Chinese Value Rule Corpus) | 51 | None | Vignette/scenario format | 70 |
| 2023-Scherrer-Evaluating the Moral Beliefs Encoded in LLMs.md | MoralChoice | 50 | None | Vignette/scenario format | 75 |
| 2024-Chiu-DailyDilemmas.md | DailyDilemmas | 50 | None | Vignette/scenario format | 60 |
| 2025-Jiang-Investigating Machine Moral Judgement Through the Delphi Experiment.md | Delphi / DelphiHYBRID | 50 | None | Vignette/scenario format | 60 |
| 2025-Samway-Are Language Models Consequentialist or Deontological.md | MORALLENS | 49 | None | Vignette/scenario format | 50 |
| 2018-Nguyen-UIT-VSFC Vietnamese Students' Feedback Corpus for Sentiment Analysis.md | — | 47 | CLASSIFICATION | Rubric/scoring guide described | 30 |
| 2024-Franken-OffTheRails Procedural Dilemma Generation for Moral Reasoning.md | OffTheRails | 47 | None | Vignette/scenario format | 60 |
| 2024-Mozikov-EAI - Emotional Decision-Making of LLMs in Strategic Games and.md | EAI (Emotional AI Framework) | 47 | None | Vignette/scenario format | 45 |
| 2025-Backmann-When Ethics and Payoffs Diverge.md | MORALSIM | 47 | MULTI_TURN_AGENT | Vignette/scenario format | 50 |
| 2023-Rao-What Makes it Ok to Set a Fire Iterative.md | delta-Rules-of-Thumb (delta-RoT) | 46 | None | Vignette/scenario format | 75 |
| 2025-Nadeem-Ethical Decision-Making in Humans and Large.md | 30-Dilemma Ethical Evaluation Framework | 46 | RUBRIC_GRADED | Likert/rating scale, Vignette/scenario format, Rubric/scoring guide described | 20 |
| 2024-Tlaie-Exploring and steering the moral compass of Large.md | Moral Foundations Questionnaire (MFQ) + ethical dilemmas battery | 45 | None | Vignette/scenario format | 25 |
| 2025-Huang-Values in the Wild Discovering and Analyzing Values in Real AI.md | Values in the Wild | 45 | None | Vignette/scenario format | 60 |

## 4. Gap Analysis — CEI Focus Areas

Which CEI focus areas have Inspect evals vs. gaps?

| Focus Area | Viable Papers | Already in Inspect | Gap? |
|-----------|--------------|-------------------|------|
| Moral Foundations Theory (MFT) | 4 | 1 | Covered |
| Trolley Problems / Moral Machine | 4 | 0 | Partial |
| Kohlberg Moral Development | 0 | 0 | YES — GAP |
| Cultural Values | 2 | 0 | Partial |
| Religious Values | 6 | 5 | Covered |
| Normative Ethics | 5 | 2 | Covered |
| Moral Psychology | 9 | 1 | Covered |

## 5. Needs Dataset Work (score 35-59)

| Paper | Score | What's Missing |
|-------|-------|----------------|
| 2018-Dixon-Measuring and Mitigating Unintended Bias in Text.md | 59 | No HF dataset |
| 2019-Fortuna-A Hierarchically-Labeled Portuguese Hate Speech Dataset.md | 59 | No HF dataset; No splits info |
| 2020-Mathew-HateXplain.md | 59 | No HF dataset; No splits info |
| 2021-Nguyen-Constructive and Toxic Speech Detection for Open-domain Social Media.md | 59 | No HF dataset; No splits info |
| 2024-Arshad-Understanding hate speech.md | 59 | No HF dataset; No splits info |
| 2024-Röttger-Political Compass or Spinning Arrow.md | 59 | No HF dataset; No splits info |
| 2024-Tian-Chinese SafetyQA - A Safety Short-form Factuality Benchmark.md | 59 | No HF dataset; No splits info |
| 2024-Yan-M$^3$oralBench.md | 58 | No HF dataset; No splits info |
| 2022-Bang-Enabling Classifiers to Make Judgements.md | 57 | No HF dataset; No splits info |
| 2023-Xu-CValues.md | 57 | No HF dataset; No splits info |
| 2024-Aupi-WoNBias A Complete Bengali Gender Bias Dataset.md | 57 | No splits info; Size unknown |
| 2024-Dou-SailCompass Towards Reproducible and Robust Evaluation.md | 57 | No splits info |
| 2024-Lee-KorNAT.md | 57 | No splits info |
| 2024-Mousi-AraDiCE Benchmarks for Dialectal and Cultural Capabilities in LLMs.md | 57 | No splits info |
| 2024-Son-KMMLU Measuring Massive Multitask Language Understanding in Korean.md | 57 | No HF dataset; No splits info |
| 2024-Son-LLM-as-a-Judge & Reward Model What They Can and Cannot Do.md | 57 | No HF dataset; No splits info |
| 2024-Zhang-CHiSafetyBench.md | 57 | No HF dataset; No splits info |
| 2025-Alghamdi-AraTrust - An Evaluation of Trustworthiness for LLMs in Arabic.md | 57 | No splits info |
| 2025-Cao-Measuring Hong Kong Massive Multi-Task Language Understanding HKMMLU.md | 57 | No splits info; Size unknown |
| 2023-Rizqullah-QASiNa.md | 56 | No HF dataset; No splits info |
| 2024-Murtala-A multilingual dataset for offensive language.md | 56 | No HF dataset; No splits info |
| 2024-Sang-CDEval A Benchmark for Measuring the.md | 56 | No splits info |
| 2025-Binti Mohd Nazri-Fine-tuning Large Language Model (BERT) for.md | 56 | No HF dataset; No splits info |
| 2025-Shetty-VITAL.md | 56 | No HF dataset; No splits info |
| 2025-Takeshita-JETHICS.md | 55 | No HF dataset; No splits info |
| 2023-Durmus-Towards Measuring the Representation of.md | 54 | No splits info |
| 2023-Koto-Large Language Models Only Pass Primary School Exams in Indonesia A.md | 54 | No HF dataset; No splits info |
| 2024-Bandarkar-The Belebele Benchmark a Parallel Reading Comprehension Dataset in.md | 54 | No HF dataset; No splits info |
| 2024-Etxaniz-Latxa An Open Language Model and Evaluation Suite for Basque.md | 54 | No HF dataset; No splits info |
| 2024-Fenogenova-MERA A Comprehensive LLM Evaluation in Russian.md | 54 | No HF dataset; No splits info |
| ... and 453 more | | |

## 6. Needs More Info (score 20-34)

695 papers in this tier (summary only).

## 7. Not Implementable (score < 20)

775 papers in this tier (summary only).
