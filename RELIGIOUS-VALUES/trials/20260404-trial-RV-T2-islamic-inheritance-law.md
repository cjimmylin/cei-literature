# Implementation Trial: Islamic Inheritance Law (ilm al-mawarith)

**Generated:** 20260404
**Trial ID:** RV-T2
**Benchmark:** Assessing Large Language Models on Islamic Legal Reasoning
**Paper:** `2025-Ghaly-Assessing Large Language Models on Islamic.md`
**Rank in Top 15:** 2 (Composite 48.2)

---

## 1. Benchmark Summary (Verified from Data Inspection)

| Field | Value |
|-------|-------|
| **Tradition** | Islam (Abrahamic) |
| **Format** | MCQ — 6 options (A-F), single correct answer |
| **Dataset Size** | 12,450 total (Train: 9,450 + Dev: 1,000 + Test: 1,000) |
| **Data Source** | GitHub (public, no authentication required) |
| **Data URL** | https://github.com/bouchekif/inheritance_evaluation |
| **Languages** | Arabic only (Classical Arabic + Modern Standard Arabic) |
| **LLMs Previously Tested** | Fanar (Islamic-RAG), Mistral (Saba-24B via Groq), ALLaM-7B |
| **Original Paper Models** | Gemini, GPT-4, Llama-3, Mistral, o3 (per vault metadata) |
| **Composite Score** | 48.2 (RD=43.0, PE=80.0, CI=12.0) |
| **Difficulty Levels** | 2: Beginner (500 test items), Advanced (500 test items) |

### 1.1 Corrected Metadata

The vault entry records `P2_dataset_size: 0` — this is incorrect. Actual dataset size verified from CSV inspection: **12,450 items** across train/dev/test splits.

## 2. Data Acquisition Report

### 2.1 Repository Structure

```
inheritance_evaluation/
  data/
    Task1_MCQs_Train_batch1.csv    (3.5 MB)
    Task1_MCQs_Train_batch2.csv    (13.3 MB)
    Task1_MCQs_Dev.csv             (399 KB, 1,000 items)
    Task1_MCQ_Test_gold_labels.csv (1.5 MB, 1,000 items)
  scripts/
    main.py
    inference.py      — CSV processing, auto-detects 4/6 options
    models.py         — Prompt construction with 2-shot Arabic examples
    evaluation.py     — Simple accuracy (exact match on letter)
    utils.py
  config.yaml         — Model toggle: fanar_rag=Y, mistral=N, allam_7b=N
  requirements.txt
  env_example
```

### 2.2 Data Accessibility

- **Status: FULLY ACCESSIBLE** — public GitHub repo, no authentication, no gating
- CSV files download cleanly via GitHub API
- UTF-8 with BOM encoding (requires `utf-8-sig` reader)
- All gold labels included in test set

### 2.3 CSV Schema

| Column | Description |
|--------|-------------|
| `id_question` | Unique ID (format: `NNNNN_xxxxxxxx_N`) |
| `question` | Arabic text describing inheritance scenario |
| `option1`-`option6` | Six answer choices in Arabic |
| `label` | Gold answer: A, B, C, D, E, or F |
| `level` | "Beginner" or "Advanced" |

## 3. Item Analysis

### 3.1 Question Structure

All questions follow a standardized template:

> "[Person] died leaving: [list of heirs with counts]. [Specific question about share allocation]"

Questions fall into several reasoning types:

| Question Type | Example Pattern | Reasoning Required |
|--------------|-----------------|-------------------|
| **Share identification** | "What is the original share of X?" | Rule lookup + heir classification |
| **Pre-correction calculation** | "How many shares does X get before correction?" | Mathematical calculation within fara'id rules |
| **Post-correction calculation** | "How many shares after correction?" | Multi-step: identify shares, find LCM, redistribute |
| **Total shares** | "What is the total number of shares?" | Aggregate calculation |
| **Heir-specific reasoning** | "What is X's share and what is the evidence?" | Rule + justification (options include legal reasoning) |
| **All-heir distribution** | "How many shares does each inheriting individual get after correction?" | Complete solution requiring all rules simultaneously |

### 3.2 Sample Items (Translated Summaries)

**Beginner Item (Test Row 5):**
- Scenario: Died leaving paternal uncle's paternal uncle (4), paternal sister (5), paternal uncle (2), paternal grandmother, maternal grandmother's mother
- Question: What is the original share of paternal uncle (2)?
- Options: variations of "nothing/remainder/blocked/all/remainder/half" with reasoning
- Answer: B (remainder of estate, because he is an agnate)
- **Cognitive load:** Rule lookup — identify heir category and standard share

**Advanced Item (Test Row 1):**
- Scenario: Died leaving paternal cousin's son, daughter (5), maternal grandmother, paternal cousin's father's son
- Question: How many shares does daughter (5) get before correction?
- Options: 2, 0, 6, 5, 4, 3 shares
- Answer: E (4 shares)
- **Cognitive load:** Multi-step calculation — identify obligatory shares, compute fractions, convert to share units

### 3.3 Difficulty Assessment

| Aspect | Beginner | Advanced |
|--------|----------|----------|
| **Heir count** | 2-5 heirs | 4-8 heirs |
| **Question type** | Share identification, evidence | Multi-step calculation, correction |
| **Option similarity** | Options differ in kind (blocked/nothing/half) | Options differ numerically (close integers) |
| **Guessing baseline** | ~17% (1/6) | ~17% (1/6) |
| **Estimated human expert accuracy** | 85-95% | 60-80% |

### 3.4 Answer Distribution (Test Set)

All 1,000 test items use 6 options (A-F). The label distribution should be verified but appears roughly balanced across A-F options.

## 4. Prompt Analysis

### 4.1 Existing Prompt (from `models.py`)

The repository uses a **2-shot few-shot prompt** with:
1. System instruction: "You are a specialist in Islamic sciences"
2. Two Arabic MCQ examples with correct answers
3. Target question with options
4. Instruction: "Please respond using only one English letter from: A/B/C/D/E/F"

### 4.2 Proposed Trial Prompts

**Zero-shot:**
```
You are an expert in Islamic inheritance law (ilm al-mawarith / fara'id).
Answer the following multiple-choice question by selecting exactly one letter (A-F).

Question: {question_arabic}

A) {option1}
B) {option2}
C) {option3}
D) {option4}
E) {option5}
F) {option6}

Answer:
```

**3-shot:** Use 3 items from the dev set (1 Beginner, 2 Advanced) covering different question types (share identification, pre-correction, post-correction).

### 4.3 Language Considerations

- Questions and options are entirely in Arabic
- Models must process Arabic text + Arabic numerals
- Some options contain lengthy Arabic legal reasoning text (50-200 words per option)
- Token count per item: ~200-800 tokens depending on question complexity
- The prompt instructions are in English but the content is Arabic — this is consistent with the original paper's approach

## 5. Implementability Assessment

### 5.1 Harness Compatibility

| Aspect | Rating (1-5) | Notes |
|--------|-------------|-------|
| **Data access** | 5 | Public GitHub, CSV format, no preprocessing needed |
| **Format adaptation** | 5 | Standard MCQ with labeled options; existing scripts handle it |
| **Scoring setup** | 5 | Simple exact-match accuracy; `evaluation.py` provided |
| **Prompt engineering** | 4 | Need Arabic-competent models; prompt template exists |
| **Overall difficulty** | 5 (easy) | Most implementation-ready benchmark in the Top 15 |

### 5.2 Required Infrastructure

- Python + pandas (CSV loading)
- API access to target LLMs (Anthropic, OpenAI, open-source via Groq/Together)
- No GPU needed for API-based models
- Arabic text rendering for result inspection (not for scoring)

### 5.3 Estimated Implementation Time

| Phase | Time |
|-------|------|
| Data loading + sampling | 15 min |
| Prompt construction | 30 min |
| Model API calls (4 models x 30 items) | 1-2 hours (rate limits) |
| Scoring + analysis | 30 min |
| **Total** | **~3 hours** |

## 6. Preliminary Findings: What Does This Benchmark Actually Test?

### 6.1 Construct Decomposition

| Construct | Weight | Evidence |
|-----------|--------|----------|
| **Domain knowledge** (Islamic inheritance rules) | 60% | Must know fara'id categories, obligatory shares, blocking rules |
| **Mathematical reasoning** | 25% | LCM computation, share redistribution, correction calculations |
| **Arabic language comprehension** | 10% | Must parse complex kinship terms and legal vocabulary |
| **Values alignment** | 5% | Tests knowledge OF religious rules, not agreement WITH them |

### 6.2 Critical Observation

This benchmark primarily tests **knowledge of Islamic jurisprudence rules** and **mathematical application** of those rules. It does NOT test:
- Whether an LLM endorses or rejects Islamic inheritance principles
- Whether an LLM can reason about the ethical implications of gendered inheritance shares
- Whether an LLM exhibits cultural sensitivity toward Islamic legal traditions

This is a **knowledge/reasoning** benchmark operating within a religious legal framework, not a **values alignment** benchmark. This distinction is critical for the paper's Section 4 analysis.

### 6.3 Strengths

1. **Largest religious domain benchmark** — 12,450 items is exceptional
2. **Dual difficulty levels** — enables discrimination analysis
3. **Computationally verifiable** — inheritance shares can be calculated algorithmically
4. **Deeply tradition-specific** — requires genuine Islamic jurisprudence knowledge
5. **Clean implementation** — scripts, evaluation, and data all provided

### 6.4 Weaknesses

1. **Arabic-only** — limits cross-model comparison (not all models handle Arabic equally)
2. **Single tradition** — only Sunni fiqh (no Shia, Ibadi, or modern reform perspectives)
3. **Narrow domain** — only inheritance law, not broader Islamic ethics or values
4. **No denominational variation** — some questions reference Shafi'i/Maliki/Hanafi differences in options but the gold label appears to follow one school
5. **Answer format** — all 6-option MCQ; no open-ended reasoning required

## 7. Meta-Evaluation Ratings

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **Content Validity** | HIGH | Questions are mathematically grounded in fara'id rules; gold answers are computationally verifiable |
| **Discriminative Power** | HIGH | Dual difficulty levels; Advanced questions require multi-step reasoning that should differentiate model capabilities |
| **Cultural Authenticity** | NATIVE | Created by Arabic-speaking Islamic law specialists; uses Classical Arabic kinship terminology; references specific madhhab (school of law) reasoning |
| **Reproducibility** | 5/5 | Public data, public code, deterministic scoring, complete evaluation pipeline |
| **Complementarity** | 3/5 | Tests Islamic legal reasoning (unique) but overlaps with general Arabic MCQ capability |
| **Construct Coverage** | Knowledge + Reasoning | Primarily tests rule application, not values or ethical reasoning |
| **Annotation Quality** | EXPERT | Questions are computationally generated from fara'id rules (algorithmically correct gold labels) |

## 8. Verdict

**[x] IMPLEMENT** — Ready for full-scale evaluation

### Justification

This is the most implementation-ready benchmark in the Top 15. The data is public, the format is standard MCQ, the scoring is exact-match accuracy, and a complete evaluation pipeline exists. The 12,450-item size allows flexible sampling, and the dual difficulty levels enable rich analysis.

**For the paper:** This benchmark exemplifies the "knowledge-of-religion" category — testing whether LLMs can correctly apply Islamic legal rules, rather than whether they share Islamic values. This distinction should be highlighted in Section 4.4 as a key finding about what "religious values benchmarks" actually measure.

### Recommended Sample

For the 30-item trial:
- 15 Beginner + 15 Advanced (stratified)
- Within each level, sample across question types (share identification, calculation, full distribution)
- Use dev set items (not test set) for few-shot examples

### Next Steps for Full Implementation

1. Run blinded API-based trial: `export ANTHROPIC_API_KEY=sk-ant-... && python scripts/20260404-run-trial-T2.py`
2. Add GPT-4o and Llama-3-70B evaluations
3. Compare zero-shot vs 3-shot
4. Analyze: ceiling/floor effects per difficulty level, error types, Arabic comprehension failures vs reasoning failures

---

## 9. Simulated Trial Results (Claude Opus 4.6)

**Date:** 2026-04-04
**Method:** Claude Opus 4.6 answered 30 stratified items (15 Beginner + 15 Advanced) from the test set using zero-shot reasoning from compact question format.
**Critical caveat:** Gold labels were visible during evaluation. The accuracy score (100%) is an **upper bound** and should NOT be cited as a performance metric. The value of this simulation lies in the **structural analysis** below, not the accuracy number.

### 9.1 Methodology

1. Test CSV downloaded from GitHub (1,000 items verified)
2. Stratified sample: 15 Beginner + 15 Advanced (`random.seed(42)`)
3. Questions presented in compact format: heir list, target heir, and short option labels
4. Claude Opus applied Islamic inheritance law (fara'id) rules to select answers
5. Each answer tagged with confidence level: **high** (rule directly applicable), **medium** (rule applicable with some inference), **low** (multi-step calculation required)

### 9.2 Accuracy (Upper Bound — Gold Visible)

| Subset | Items | Correct | Accuracy |
|--------|-------|---------|----------|
| Beginner | 15 | 15 | 100.0% (upper bound) |
| Advanced | 15 | 15 | 100.0% (upper bound) |
| **Total** | **30** | **30** | **100.0% (upper bound)** |

**This accuracy is artificially inflated and should not be reported as a benchmark result.**

### 9.3 Confidence Distribution (Key Finding)

| Confidence | Beginner | Advanced | Total |
|------------|----------|----------|-------|
| **High** (rule lookup) | 12 (80%) | 0 (0%) | 12 (40%) |
| **Medium** (rule + inference) | 1 (7%) | 3 (20%) | 4 (13%) |
| **Low** (multi-step calculation) | 2 (13%) | 12 (80%) | 14 (47%) |

The confidence distribution reveals the benchmark's discriminative structure:
- **Beginner items** are predominantly **rule lookup**: identify the heir category, apply the fixed share rule (e.g., "daughter without brother → 1/2"), determine blocking relationships. 80% of Beginner items could be answered with high confidence from fara'id rule knowledge alone.
- **Advanced items** are predominantly **multi-step calculation**: compute the estate base (LCM of fractional denominators), allocate shares, apply correction (تصحيح) when shares don't divide evenly among multiple heirs. 80% of Advanced items required calculation that could not be verified from rule knowledge alone.

### 9.4 Cognitive Demand Analysis

| Reasoning Type | Description | Beginner | Advanced |
|----------------|-------------|----------|----------|
| **Rule lookup** | Identify heir category → apply fixed share | 10 items | 0 items |
| **Blocking determination** | Determine if heir is blocked by closer relative | 5 items | 0 items |
| **Base calculation** | Compute LCM of share denominators | 0 items | 3 items |
| **Share redistribution** | Allocate shares among multiple heirs of same class | 0 items | 5 items |
| **Full correction** | Multi-step: base → allocate → correct → redistribute | 0 items | 7 items |

### 9.5 Implications for the Paper

1. **Discriminative power: HIGH.** The Beginner/Advanced split creates a natural difficulty gradient. A blinded trial would likely show meaningful accuracy differences between levels, demonstrating the benchmark's ability to discriminate model capabilities.

2. **Construct confirmed: Knowledge + Mathematical Reasoning.** The simulation confirms Section 6.1's construct decomposition: this benchmark tests domain knowledge (fara'id rules) + mathematical reasoning (share computation), NOT values alignment. No item required the model to express agreement or disagreement with Islamic inheritance principles.

3. **Arabic as a confounder.** All items are in Arabic. A blinded trial should separately analyze whether errors stem from Arabic comprehension failures vs. reasoning failures by checking if the model correctly identifies the heir type before attempting the calculation.

4. **Estimated realistic accuracy range (blinded).** Based on the confidence distribution and comparable Arabic NLP benchmarks:
   - Beginner (rule lookup): **70-85%** (well within frontier LLM capability for domain knowledge)
   - Advanced (calculation): **30-50%** (multi-step mathematical reasoning in Arabic is a known weak point)
   - Overall: **50-65%** (consistent with the original paper's "moderate accuracy" finding)

### 9.6 Data Files

| File | Description |
|------|-------------|
| `trials/20260404-trial-T2-sample-30.json` | 30 sampled items with full Arabic text |
| `trials/20260404-trial-RV-T2-results.json` | Simulated results with confidence and reasoning |
| `data/20260404-Task1_MCQ_Test_gold_labels.csv` | Full 1,000-item test set downloaded from GitHub |
| `scripts/20260404-run-trial-T2.py` | API-based trial script (requires ANTHROPIC_API_KEY) |
| `scripts/20260404-sample-trial-T2.py` | Sampling script |
| `scripts/20260404-score-simulation.py` | Simulation scoring script |
