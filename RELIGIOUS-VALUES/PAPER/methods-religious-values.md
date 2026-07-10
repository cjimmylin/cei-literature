## 3. Methods

### 3.1 Benchmark Corpus Assembly

We assembled the evaluation corpus in two stages. First, we drew on the CEI Literature Vault, a curated collection of 2,099 AI ethics papers spanning 2019--2026, in which prior classification had tagged papers along religious values dimensions using a 14-field scoring system covering the traditions listed in the Terminology Glossary. We intersected religious values scores with benchmark and evaluation indicators to produce 401 religious benchmark candidates. Twenty-nine papers addressing religion only as a demographic variable in bias measurement were excluded from further scoring.

Second, we conducted an external search across Semantic Scholar, arXiv, and HuggingFace Datasets using 72 queries organized by tradition family, combining tradition-specific terms with benchmark vocabulary (e.g., *"Buddhist ethics benchmark LLM"*, *"Quranic question answering evaluation"*). The search returned 70 discoveries after deduplication. Of these, 53 met inclusion criteria and were ingested; 16 were excluded as false positives (physics experiments, medical studies, or unrelated benchmarks), and 1 was a duplicate. Inclusion criteria required that a paper (a) explicitly evaluate LLMs on religious or theological content, (b) be published 2021--2026 (with exceptions for older foundational databases), and (c) be available as a peer-reviewed publication or recognized preprint.

We classified each candidate into three tiers of religious engagement: **theological** (deep engagement with scriptural exegesis, jurisprudential reasoning, or denominational distinctions), **theological-values** (moderate engagement with tradition-specific ethical content), and **values** (surface-level mention of religious concepts within broader cultural or moral evaluation). This classification informed the Religious/Theological Depth scoring described in Section 3.2.

### 3.2 Feature Matrix Design

We characterized each of the 401 benchmark candidates along 22 features organized into three axes (Table 1): **Religious/Theological Depth (RD)**, measuring how rigorously a benchmark engages religious content; **Practical Ease (PE)**, measuring implementability; and **Citation Impact (CI)**, measuring scholarly influence.

Religious/Theological Depth features capture the number of traditions tested (R1), the depth of theological engagement on a 1--5 ordinal scale (R2), scriptural grounding measured by direct reference to primary sacred texts such as the Quran, Bible, Vedas, or Pali Canon (R3, 0--5), denominational awareness distinguishing intra-tradition diversity such as Sunni/Shia or Catholic/Protestant (R4, 0--3), pluralistic coverage of multiple traditions (R5, 0--5), and expert validation measuring whether theologians or religious scholars participated in benchmark construction (R6, 0--5). Practical Ease features record task format using a 12-code taxonomy (P1; see Table S3), dataset size (P2), data availability with URL (P3), code availability (P4), license terms (P5), an implementability composite reflecting harness compatibility across standard evaluation frameworks (P7, 0--10), scorer type (P8), model compatibility with open and closed LLMs (P9), and language coverage (P10). Citation Impact features include raw citation count (C1), age-normalized citations per year (C2), venue and tier classification (C3), downstream adoption count (C4), leaderboard presence (C5), and community engagement indicators such as shared tasks and workshops (C6).

To mitigate subjectivity in the most consequential feature---theological depth (R2)---we calibrated against three anchors. IslamicMMLU \cite{Alharbi2024} (R2 = 4) engages fiqh-level jurisprudential reasoning across four madhabs, including a madhab bias detection task. Break the Checkbox (R2 = 2) presents multi-religion multiple-choice questions without deep theological engagement within any tradition. At the lower bound, papers mentioning religious vocabulary in general cultural surveys without theological substance were scored R2 = 1. All remaining benchmarks were scored relative to these anchors by the first author, with rationales recorded in the feature matrix (Table S1).

The format taxonomy (P1) comprises 12 codes---from high-harness-compatibility formats (MCQ, MRC, BIN, SHT, TXT) through medium (SCN, PSY, MIX) to low (OPN, MTN, RAG, MUL)---reflecting the heterogeneous evaluation designs in the corpus (Table S3).

### 3.3 Composite Scoring

We computed three axis scores. **Religious/Theological Depth (RD)** weights theological depth and expert validation most heavily, reflecting this survey's focus on evaluating genuine religious engagement rather than surface-level mention:

> RD = R2 x 25 + R6 x 20 + R1 x 15 + R3 x 15 + R5 x 15 + R4 x 10

**Practical Ease (PE)** prioritizes implementability and data access:

> PE = P7 x 30 + P3 x 20 + P4 x 15 + P9 x 15 + P10 x 10 + P5 x 10

**Citation Impact (CI)** balances normalized citations with downstream adoption and community activity:

> CI = C2 x 30 + C4 x 25 + C3 x 20 + C6 x 15 + C5 x 10

All axis scores are normalized to 0--100. The composite score combines the three axes:

> COMPOSITE = RD x 0.40 + PE x 0.35 + CI x 0.25

We weighted RD highest because this survey specifically evaluates *religious and theological* depth---a benchmark that is easy to run but theologically shallow serves our purpose less than one that requires more implementation effort but genuinely engages tradition-specific reasoning. PE receives the second-highest weight because benchmarks without accessible data cannot be verified, replicated, or extended by independent researchers \cite{Bowman2021}. CI receives the lowest weight to avoid over-rewarding incumbency: in a field where 73\% of candidates are from 2024--2026, high citation counts disproportionately favor older benchmarks that may not reflect the current state of the art.

We applied two **hard gates** before ranking. First, RD must equal or exceed 30, ensuring minimum theological engagement and filtering candidates that mention religion only incidentally. Second, evaluation data must be publicly available on GitHub, HuggingFace, or an equivalent repository. Of the 401 candidates, 355 failed at least one gate: the data availability gate alone eliminated 77\% of the corpus, confirming that data accessibility---not benchmark quality---is the field's primary practical bottleneck \cite{Gehrmann2022}. Exactly 46 candidates passed both gates.

We then applied **diversity constraints** to prevent the Top 15 from reflecting only the tradition with the most candidates, requiring at least 4 Abrahamic, 3 Dharmic, 1 East Asian, and 1 African/Indigenous benchmark. The first three constraints were satisfied; the African/Indigenous constraint could not be met because no benchmark from either tradition passed both gates---a finding we discuss in Section 4 as evidence of structural epistemic injustice \cite{Mohamed2020}. The final Top 15 includes 9 Abrahamic (7 Islam, 2 Christianity), 3 Dharmic (Hinduism, Buddhism, Sikhism), and 1 East Asian (Confucianism), spanning 7 format codes and 9 languages (Table 2).

### 3.4 Meta-Evaluation Criteria

Beyond composite scoring, we developed seven **meta-evaluation criteria** for assessing benchmark quality along dimensions that numerical scoring cannot fully capture (Table S5). (1) **Content Validity** distinguishes benchmarks testing genuine theological reasoning from those testing factual recall, assessed by classifying a 20-item sample as requiring high, medium, or low theological engagement. (2) **Discriminative Power** checks for ceiling and floor effects by examining score ranges across model families. (3) **Cultural Authenticity** records whether benchmark authors are scholars from the tradition being evaluated (NATIVE), consulted tradition-specific experts (CONSULTED), or worked without documented domain consultation (EXTERNAL)---a distinction motivated by Hutchinson's \cite{Leavens2024} argument that sacred texts cannot be treated as "just data." (4) **Reproducibility** applies a five-item checklist: publicly available data, evaluation code, defined scoring metrics, documented prompts, and inter-annotator agreement. (5) **Complementarity** measures unique dimensions a benchmark adds to the selection (1--5 scale across tradition, task type, cognitive level, language, and domain). (6) **Construct Coverage** maps each benchmark to the dimensions of religious values alignment it measures: knowledge, reasoning, values, sensitivity, pluralism, or contextualization. (7) **Annotation Quality** records how gold-standard answers were determined, from expert theologian judgment (highest reliability) through crowdworkers to automatic generation (lowest).

### 3.5 Implementation Trial Protocol

To move beyond feature-level characterization, we designed an implementation trial protocol for each of the Top 15 benchmarks. For each trial, we sample 20--50 items stratified by difficulty and sub-category, then present them to a minimum of three models spanning frontier closed-source (e.g., Claude Opus, GPT-4o), frontier open-source (e.g., Llama-3-70B), and mid-tier (e.g., Llama-3-8B) categories. We evaluate under both zero-shot and few-shot prompting conditions, scoring with the benchmark's intended metric alongside standardized accuracy and F1. Analysis for each trial includes a ceiling check (any model above 90\% accuracy), a discrimination check (score range across models), and an error taxonomy distinguishing knowledge gaps, reasoning failures, and cultural misunderstanding (imposing assumptions from one tradition onto another). Trial templates have been generated for all 15 benchmarks; full-scale trials are in progress, with results to be reported in a companion technical report.

### 3.6 Limitations

Several methodological limitations warrant acknowledgment. First, the most consequential RD features---theological depth (R2) and expert validation (R6)---are scored via keyword heuristics rather than expert theological judgment; manual review of the Top 15 is needed to validate assignments. Second, all scoring was conducted by a single author without inter-rater reliability; calibration anchors mitigate but do not eliminate subjectivity. Third, the external search did not include Google Scholar or PapersWithCode, and HuggingFace API rate limits yielded zero results, likely underestimating the true corpus. Fourth, tradition assignment for external papers was derived from search metadata rather than expert classification. Fifth, the format taxonomy's 12 codes cannot fully capture real-world heterogeneity---several entries required the MIX residual category. Finally, the hard gate requiring publicly available data, while necessary for reproducibility, functions simultaneously as a structural exclusion mechanism for traditions governed by collective data sovereignty \cite{Carroll2020}---a limitation that is itself a finding of this study.
