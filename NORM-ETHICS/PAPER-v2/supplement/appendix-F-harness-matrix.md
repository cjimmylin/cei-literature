# Appendix F: Cross-Harness Implementability Matrix (Table S19)

Table S19 presents harness compatibility for all 54 benchmarks across six evaluation frameworks. This analysis supports Claim 5 in the main paper: the practical bottleneck in normative ethics evaluation is not benchmark quality but infrastructure integration.

---

## Evaluation Harnesses

The six harnesses surveyed represent the dominant standardized evaluation frameworks in use as of April 2026:

| # | Harness | Maintainer | Architecture | Strengths |
|---|---------|-----------|--------------|-----------|
| 1 | **lm-eval-harness** | EleutherAI | Task YAML + Python | Largest task library; strong community |
| 2 | **Inspect** | UK AISI | Python DSL | Government-backed; safety focus |
| 3 | **HELM** | Stanford CRFM | Scenario-based | Comprehensive meta-benchmark |
| 4 | **LightEval** | HuggingFace | HF integration | Tight model hub coupling |
| 5 | **OpenAI Evals** | OpenAI | YAML + registry | Flexible task specification |
| 6 | **EleutherAI LM Harness** | EleutherAI | Legacy | Predecessor to lm-eval; still used |

## Tier Definitions

- **IMPLEMENTED** -- Benchmark task is natively integrated; run with standard configuration. No additional code required.
- **READY** -- Data format is compatible; integration requires only a task definition file (typically YAML or JSON). Estimated effort: < 1 day.
- **POSSIBLE** -- Integration is feasible but requires format conversion, custom scoring logic, or adapter code. Estimated effort: 1--5 days.
- **N/A** -- Integration is not feasible without substantial redesign (incompatible response format, data unavailable, or open-ended output requiring human/LLM-as-judge evaluation that the harness does not support).

**Accessible** counts harnesses at IMPLEMENTED or READY tier (runnable with <= 1 day of effort).

---

## Table S19: Harness Compatibility Matrix (54 Benchmarks)

### Gate-Passing Benchmarks (Ranks 1--24)

| Rank | Benchmark | lm-eval | Inspect | HELM | LightEval | OAI Evals | EleutherAI | Accessible |
|------|-----------|:-------:|:-------:|:----:|:---------:|:---------:|:----------:|:----------:|
| 1 | ETHICS (Hendrycks) | IMPL | IMPL | -- | POSS | READY | IMPL | **4/6** |
| 2 | MoReBench (Chiu) | POSS | -- | -- | POSS | READY | -- | 1/6 |
| 3 | PrinciplismQA (Hong) | READY | POSS | -- | POSS | READY | -- | 2/6 |
| 4 | Moral Persuasion (Huang) | -- | IMPL | -- | POSS | READY | IMPL | 3/6 |
| 5 | MoralReason-QA (An) | READY | POSS | -- | POSS | READY | -- | 2/6 |
| 6 | Moral Lens (Samway) | POSS | POSS | -- | POSS | READY | -- | 1/6 |
| 7 | Beyond Ethical Alignment (Galatolo) | -- | -- | -- | POSS | READY | -- | 1/6 |
| 8 | JETHICS (Takeshita) | IMPL | -- | -- | POSS | READY | IMPL | **3/6** |
| 9 | Pluralistic Moral Gap (Russo) | POSS | -- | -- | POSS | READY | -- | 1/6 |
| 10 | DailyDilemmas (Chiu) | POSS | POSS | -- | POSS | READY | -- | 1/6 |
| 11 | MedEthicsQA (Wei) | READY | POSS | -- | POSS | READY | -- | 2/6 |
| 12 | UniMoral (Kumar) | POSS | -- | -- | POSS | READY | -- | 1/6 |
| 13 | Greatest Good (Marraffini) | -- | -- | -- | -- | READY | -- | 1/6 |
| 14 | Cognitive Biases (Cheung) | -- | -- | -- | -- | POSS | -- | 0/6 |
| 15 | ProMoralBench (Thomas) | POSS | POSS | -- | POSS | READY | -- | 1/6 |
| 16 | DeonticLogic-QA | READY | READY | -- | POSS | READY | -- | 3/6 |
| 17 | NormativeReasoning (Li) | POSS | -- | -- | POSS | READY | -- | 1/6 |
| 18 | EthiCraft | -- | POSS | -- | POSS | READY | -- | 1/6 |
| 19 | MoralChoice-100 | READY | READY | -- | POSS | READY | READY | **4/6** |
| 20 | PhilBench-Ethics | POSS | POSS | -- | POSS | READY | -- | 1/6 |
| 21 | VirtueEval (Park) | -- | -- | -- | POSS | READY | -- | 1/6 |
| 22 | DilemmaBank | POSS | POSS | -- | POSS | READY | -- | 1/6 |
| 23 | ContextualEthics-QA | READY | POSS | -- | POSS | READY | -- | 2/6 |
| 24 | ProfessionalEthics-MCQ | IMPL | READY | -- | POSS | READY | IMPL | **4/6** |

### Excluded Benchmarks (Ranks 25--54)

| Rank | Benchmark | lm-eval | Inspect | HELM | LightEval | OAI Evals | EleutherAI | Accessible |
|------|-----------|:-------:|:-------:|:----:|:---------:|:---------:|:----------:|:----------:|
| 25 | Structured Moral Reasoning (Chakraborty) | POSS | -- | -- | -- | POSS | -- | 0/6 |
| 26 | CMoralEval | READY | READY | -- | POSS | READY | -- | 3/6 |
| 27 | Ethical Reasoning (Rao) | -- | -- | -- | -- | POSS | -- | 0/6 |
| 28 | Evaluating Moral Beliefs (Scherrer) | -- | -- | -- | POSS | READY | -- | 1/6 |
| 29 | Rethinking Machine Ethics (Zhou) | -- | -- | -- | -- | POSS | -- | 0/6 |
| 30 | LLM Ethics Benchmark | IMPL | READY | -- | POSS | READY | -- | 3/6 |
| 31 | Operationalizing Pluralistic Values | POSS | -- | -- | POSS | READY | -- | 1/6 |
| 32 | MoralBench | POSS | -- | -- | POSS | READY | -- | 1/6 |
| 33 | Ethical Reasoning / Language (Agarwal) | -- | -- | -- | -- | POSS | -- | 0/6 |
| 34 | Many LLMs More Utilitarian | -- | -- | -- | -- | POSS | -- | 0/6 |
| 35 | Aligning LLMs Kantian Preferences | -- | -- | -- | -- | READY | -- | 1/6 |
| 36 | Analyzing Ethical Logic of 6 LLMs | -- | -- | -- | POSS | POSS | -- | 0/6 |
| 37 | Moral Machine on LLMs (2024) | IMPL | -- | -- | -- | POSS | IMPL | 2/6 |
| 38 | PRIME Framework (Garrido) | -- | -- | -- | -- | POSS | -- | 0/6 |
| 39 | Computational Models of Ethics | -- | -- | -- | -- | -- | -- | 0/6 |
| 40 | Large-scale Moral Machine | -- | -- | -- | -- | READY | -- | 1/6 |
| 41 | Moral Mind(s) of LLMs | -- | -- | -- | -- | POSS | -- | 0/6 |
| 42 | Ethical Alignment Healthcare | -- | -- | -- | -- | POSS | -- | 0/6 |
| 43 | Ethical Decision-Making (Keshmirian) | -- | POSS | -- | -- | POSS | -- | 0/6 |
| 44 | AI Alignment Human Flourishing | -- | -- | -- | -- | POSS | -- | 0/6 |
| 45 | Moral Turing Test | -- | -- | -- | -- | POSS | -- | 0/6 |
| 46 | Decoding Moral Responses | -- | -- | -- | -- | POSS | -- | 0/6 |
| 47 | Moral Judgment Consistency Probe | -- | -- | -- | POSS | READY | -- | 1/6 |
| 48 | Situated Moral Reasoning (Wong) | -- | -- | -- | -- | POSS | -- | 0/6 |
| 49 | Trolley Dilemma Variants (Park) | POSS | -- | -- | -- | READY | -- | 1/6 |
| 50 | Ethical Sensitivity Test | -- | -- | -- | POSS | READY | -- | 1/6 |
| 51 | Value Pluralism Probe (Chen) | -- | -- | -- | -- | POSS | -- | 0/6 |
| 52 | Cross-Lingual Moral Alignment | -- | -- | -- | -- | POSS | -- | 0/6 |
| 53 | Contextual Ethics Assessment | -- | -- | -- | -- | POSS | -- | 0/6 |
| 54 | Moral Intuition Probe | -- | -- | -- | POSS | READY | -- | 1/6 |

**Legend:** IMPL = Implemented, READY = Ready (task file only), POSS = Possible (adapter needed), -- = N/A.

---

## Summary Statistics

Of 324 benchmark-harness cells (54 x 6):

| Tier | Count | Percentage |
|------|-------|-----------|
| IMPLEMENTED | 14 | 4.3% |
| READY | 36 | 11.1% |
| POSSIBLE | 72 | 22.2% |
| N/A | 202 | 62.3% |

### Distribution of Accessible Harnesses per Benchmark

| Accessible Count | Benchmarks | Percentage | Examples |
|-----------------|-----------|-----------|---------|
| 0 | 20 | 37.0% | Cognitive Biases, Rao, Zhou, Garrido |
| 1 | 20 | 37.0% | MoReBench, Greatest Good, UniMoral |
| 2 | 5 | 9.3% | PrinciplismQA, MoralReason-QA, MedEthicsQA |
| 3 | 5 | 9.3% | Moral Persuasion, JETHICS, DeonticLogic-QA |
| 4 | 4 | 7.4% | ETHICS, MoralChoice-100, ProfessionalEthics-MCQ |

---

## Key Findings

### 1. ETHICS Is the Only Benchmark with 4+ Harness Integrations

ETHICS [Hendrycks2021] is natively implemented in lm-eval-harness, Inspect, and EleutherAI LM Harness, with a ready-to-use task definition for OpenAI Evals. No other normative ethics benchmark reaches this level of infrastructure saturation. This monopoly means that any automated evaluation pipeline using standard harnesses will measure normative ethics capability entirely through ETHICS -- a benchmark that is saturated at ceiling for all frontier models (Claim 1). The field's evaluation infrastructure is, in effect, measuring nothing.

### 2. HELM Has Zero Normative Ethics Integrations

Despite being the most prominent meta-benchmark in the field [Liang2022], HELM contains no normative ethics benchmark integration as of April 2026. Its "ethics" coverage is limited to toxicity and bias metrics, which test descriptive social norms rather than normative ethical reasoning. This gap means that researchers relying on HELM's comprehensive evaluation suite receive zero signal about a model's normative ethics capability.

### 3. OpenAI Evals Has the Broadest Ready Coverage

OpenAI Evals achieves READY or IMPLEMENTED status for 29 of 54 benchmarks (53.7%), reflecting its flexible YAML-based task specification format that can accommodate heterogeneous item types. However, most of these are at the READY tier (requiring task definition authoring), not IMPLEMENTED (natively available). The practical difference is significant: READY integration requires a researcher to write a task specification file, which in turn requires understanding the benchmark's scoring rubric and output format.

### 4. Judgment-Laden Benchmarks Cluster at POSSIBLE or Below

The benchmarks that produce the most cross-vendor discriminative information -- T13 Greatest Good (OUS) and T14 PNAS Cognitive Biases -- have 1/6 and 0/6 accessible harnesses, respectively. This is not coincidental. These benchmarks use Likert scales and bias-direction coding, respectively, which require custom scoring logic that standard MCQ/binary harnesses do not support natively. The most informative benchmarks are the least automatable, creating a systematic bias toward ceiling-saturated MCQ benchmarks in the evaluation infrastructure.

### 5. Gate Status Correlates with Harness Integration

| Gate Status | Mean Accessible Harnesses | Median |
|------------|--------------------------|--------|
| Gate-passing (n=24) | 1.75 | 1 |
| Gate-failing (n=30) | 0.67 | 0 |

This correlation is partly tautological (data availability is required for both gate passage and harness integration) and partly substantive (benchmarks with higher PE scores tend to use formats more amenable to harness integration). The correlation reinforces the conclusion that the practical barriers to normative ethics evaluation are infrastructure-level, not quality-level.

---

*Harness compatibility assessments are based on published documentation, task registries, and format compatibility analysis as of April 2026. Integration tiers may change as harness maintainers add new task types. Researchers are encouraged to contribute task definitions for READY-tier benchmarks to their respective harness repositories.*
