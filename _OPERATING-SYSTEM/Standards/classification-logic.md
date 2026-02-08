# Classification Logic Standards

**Version:** 1.0
**Created:** 2026-02-02
**Category:** Classification Procedures
**Applies to:** All paper classification workflows

---

## Overview

The CEI Literature Vault implements a **7-stage classification pipeline** to enrich paper metadata with ethical and technical properties. This standard documents the logic, order, and edge cases for each stage.

---

## 7-Stage Classification Pipeline

The optimal order minimizes re-processing - each stage filters input for the next.

```
Stage 1: Ethics Overall (Broad filter)
    ↓
Stage 2: Ethics Frameworks (Virtue/Deontological/Utilitarian)
    ↓
Stage 3: Ethics Perspective (If overall=Yes BUT no framework)
    ↓
Stage 4: Research Topic (If overall=No)
    ↓
Stage 5: Cultural & Religious Values
    ↓
Stage 6: Moral Psychology
    ↓
Stage 7: Data Nature (Benchmark/Eval/Dataset)
```

**Rationale:** Run broad filters (Stage 1) before specific ones (Stages 2-3). Separate ethical (Stages 2-3) from non-ethical (Stage 4). Cross-cutting concerns (Stages 5-7) run on all papers.

---

## Stage 1: Ethics Overall

### Field
`ethics_overall`: Yes/No

### Purpose
Broad filter to identify papers with any ethical dimension.

### Script
`PYTHON/classify_ethics.py`

### Detection Logic
Keyword matching on abstracts and titles.

**Trigger Keywords:**
- ethics, ethical, moral, morality, morally
- value, values, fairness, unfairness
- harm, harmful, harmlessness, safety (when combined with "AI" or "model")
- bias, discrimination, toxicity
- responsibility, responsible AI
- alignment (when combined with "value" or "human")

### Examples

**Yes:**
- "We investigate ethical considerations in AI development"
- "Mitigating bias and promoting fairness in language models"
- "Value alignment through constitutional AI"

**No:**
- "A novel transformer architecture for machine translation"
- "Improving BERT embeddings with contrastive learning"
- "Question answering on knowledge graphs"

### Edge Cases

**Constitutional AI / TruthfulQA Issue:**
- **Problem:** Papers like "Constitutional AI" use technical terms ("harmlessness", "hallucination") rather than explicit "ethics" keywords
- **Current State:** May be classified as `ethics_overall: "No"`
- **Workaround:** Stage 4 (Research Topic) catches these as "AI Safety & Alignment"
- **Future Fix:** Add "harmlessness", "truthfulness", "hallucination" as ethics trigger keywords

**Safety vs. Robustness:**
- **Safety** (ethical concern) = preventing harm to humans, value alignment
- **Robustness** (technical concern) = model reliability, adversarial examples
- If abstract mentions "safety" with "AI" or "model" → likely ethical
- If abstract mentions "robustness" without ethical context → likely technical

---

## Stage 2: Ethics Frameworks

### Fields
- `virtue_ethics`: Yes/No
- `deontological_ethics`: Yes/No
- `utilitarian_ethics`: Yes/No

### Purpose
Identify papers grounded in specific philosophical frameworks.

### Script
`PYTHON/classify_ethics.py` (same script, multiple fields)

### Detection Logic

#### Virtue Ethics
**Keywords:**
- virtue, virtues, virtuous
- character, character-based
- eudaimonia, flourishing
- aristotelian, aristotle
- phronesis (practical wisdom)
- moral exemplar

**Examples:**
- "Virtue-based AI: Designing agents with character"
- "Phronesis and practical wisdom in autonomous systems"

#### Deontological Ethics
**Keywords:**
- duty, duties, obligation, obligations
- kantian, kant
- categorical imperative
- rights, rights-based
- deontology, deontological

**Examples:**
- "Rights-based framework for AI decision-making"
- "Kantian duties in autonomous vehicle ethics"

#### Utilitarian Ethics
**Keywords:**
- utility, utilities
- consequences, consequentialism
- maximize welfare, greatest good
- utilitarian, utilitarianism
- cost-benefit analysis (in ethical context)

**Examples:**
- "Consequentialist approaches to AI alignment"
- "Maximizing welfare in multi-agent systems"

### Framework Disambiguation

**When a paper mentions multiple frameworks:**

1. **Proposing vs. Critiquing:**
   - Papers **proposing** virtue-based architectures → `virtue_ethics: "Yes"`
   - Papers **critiquing** utilitarianism while proposing alternatives → `utilitarian_ethics: "No"`
   - Check abstract for "we propose" vs "we critique"

2. **Comparative Studies:**
   - Papers comparing frameworks without favoring one → Mark ALL mentioned frameworks as "Yes"
   - Example: "Virtue vs. Utilitarian Approaches to AI Ethics" → Both "Yes"

3. **Primary Contribution:**
   - If paper clearly centers on one framework, prioritize that one
   - Example: "A Deontological Framework for AI (with utilitarian considerations)" → `deontological_ethics: "Yes"`, `utilitarian_ethics: "Yes"` (but deontological is primary)

### Enrichment Fields (Manual)

For papers with framework tags, add:
- `key_contribution` (String) - One-sentence summary of specific technical/theoretical contribution
- `significance` (String) - Why this matters for AI alignment

**Examples:**
- **key_contribution:** "Proposes a phronesis-based architecture for contextual moral reasoning"
- **significance:** "Shifts focus from rule compliance to character development in AI agents"

---

## Stage 3: Ethics Perspective

### Field
`ethics_perspective`: String (category name)

### Scope
Applied **ONLY** to papers where:
- `ethics_overall: "Yes"` AND
- No specific framework detected (all three frameworks are "No")

### Purpose
Categorize ethical papers that don't fit traditional philosophical frameworks.

### Script
`PYTHON/classify_ethics_perspective.py`

### Categories

1. **AI Safety & Alignment** - Robustness, red teaming, jailbreaks, adversarial attacks
2. **Bias & Fairness** - Stereotypes, discrimination, equity, representational harm
3. **Toxicity & Hate Speech** - Abusive language, offensive content, content moderation
4. **Moral Reasoning & Psychology** - Moral judgment, trolley problems, ethical dilemmas
5. **Truthfulness & Factuality** - Hallucinations, misinformation, factual accuracy
6. **Privacy & Surveillance** - Data privacy, tracking, surveillance ethics
7. **Human Rights & Social Justice** - Rights violations, social impact, justice
8. **Responsible AI** - Governance, accountability, transparency
9. **Machine Ethics** - Explicit machine ethics, artificial moral agents
10. **Value Alignment** - Human values, preference learning, reward modeling

### Detection Logic
Keyword matching on abstracts and titles, category-specific.

**Example Keywords by Category:**

**AI Safety & Alignment:**
- red team, jailbreak, adversarial, attack, robustness
- safety, safe, unsafe, harmful behavior
- alignment, misalignment

**Bias & Fairness:**
- bias, biased, stereotype, discrimination
- fairness, unfairness, equity, equality
- representational harm, allocational harm

**Truthfulness & Factuality:**
- hallucination, truthful, truthfulness
- factual, factuality, misinformation
- accuracy, veracity

### Edge Cases

**Multiple Perspectives:**
- Some papers fit multiple categories (e.g., bias + fairness + toxicity)
- Choose the **primary** perspective based on abstract focus
- If truly equal, pick the first match alphabetically (for consistency)

---

## Stage 4: Research Topic (Non-Ethics)

### Field
`research_topic`: String (category name)

### Scope
Applied **ONLY** to papers where `ethics_overall: "No"`

### Purpose
Categorize non-ethical papers by technical domain.

### Script
`PYTHON/classify_non_ethics_topics.py`

### Categories

1. **Machine Learning** - General ML/DL papers
2. **NLP & Representation Learning** - Embeddings, parsing, language models
3. **Question Answering** - QA-specific systems
4. **Machine Translation** - Translation systems
5. **Computer Vision** - Image/video processing
6. **Benchmarks & Datasets** - Data contributions without ethical focus
7. **AI Safety & Alignment** - Catch-all for technical safety papers missed by Stage 1

### Detection Logic
Keyword matching on abstracts and titles.

**Example Keywords:**

**NLP & Representation Learning:**
- embedding, BERT, transformer, language model
- parsing, syntax, semantics, NLP

**Machine Translation:**
- translation, translate, MT, neural MT
- source language, target language

**AI Safety & Alignment (Catch-all):**
- constitutional AI, harmlessness (if not caught in Stage 1)
- truthfulness, factuality (if not caught in Stage 1)
- reward hacking, specification gaming

### Purpose of "AI Safety & Alignment" Category in Non-Ethics

This category catches papers like:
- Constitutional AI (uses "harmlessness" not "ethics")
- TruthfulQA (uses "hallucination" not "moral")

These are **ethically relevant** but didn't trigger Stage 1 keywords. This ensures they're still findable under AI safety.

---

## Stage 5: Cultural & Religious Values

### Fields
- `national_ethnic_cultural`: String/List
- `religious_values`: String/List

### Script
`PYTHON/classify_cultural_religious.py`

### Scope
Applied to **ALL** papers (regardless of ethics_overall)

### Cultural Values

**20+ Categories:**
- Chinese, Japanese, Korean, Indian
- African/Ubuntu, American, European
- Arabic, Hebrew, Persian
- Indigenous/Native
- Latin American
- Southeast Asian
- And others...

**Detection Logic:**
- Keyword matching on titles and abstracts
- Includes language-specific datasets (e.g., Chinese NLP → "Chinese" cultural tag)

**Rationale for Language Datasets:**
- Language embeds cultural context
- Examples: Qwen (Chinese), GurbaniDB (Punjabi/Sikh), Hebrew NLP datasets
- Tag indicates cultural relevance for research contextualization

**Examples:**
- "Moral values in Chinese AI systems" → Chinese
- "Ubuntu ethics for AI alignment" → African/Ubuntu
- "Arabic speech recognition dataset" → Arabic (language → cultural)

### Religious Values

**Categories:**
- Islam, Christianity, Buddhism, Judaism, Hinduism
- Sikhism, Jainism, Confucianism, Taoism
- And others...

**Detection Logic:**
- Keyword matching on titles and abstracts
- Explicit mentions of religious texts, concepts, values

**Examples:**
- "Islamic ethics in AI governance" → Islam
- "Christian virtue in autonomous systems" → Christianity
- "GurbaniDB: Sikh scripture dataset" → Sikhism

### Format

**Single Value:**
```yaml
national_ethnic_cultural: "Chinese"
religious_values: "Islam"
```

**Multiple Values:**
```yaml
national_ethnic_cultural:
  - Chinese
  - Confucian
religious_values:
  - Buddhism
  - Taoism
```

---

## Stage 6: Moral Psychology

### Field
`moral_psychology`: String/List

### Script
`PYTHON/classify_moral_psych.py`

### Scope
Applied to **ALL** papers

### Categories (Psychological Schools/Theories)

1. **Moral Foundations Theory** - Haidt/Graham (Care, Fairness, Loyalty, Authority, Sanctity)
2. **Dual Process Theory** - Greene (emotional vs. rational moral judgment)
3. **Value Pluralism / Schwartz Values** - Schwartz's 10 basic values
4. **Cognitive Developmental** - Kohlberg/Piaget stages of moral development
5. **Dyadic Morality** - Gray (moral dyad: agent & patient)
6. **Trolley / Dilemmas** - Trolley problems as methodology

### Detection Logic

**Keyword Examples:**

**Moral Foundations Theory:**
- moral foundations, MFT, Haidt
- care/harm, fairness/cheating, loyalty/betrayal
- authority/subversion, sanctity/degradation

**Dual Process Theory:**
- dual process, Greene, emotional vs rational
- system 1 vs system 2 (in moral context)

**Trolley / Dilemmas:**
- trolley problem, trolley dilemma
- moral dilemma, ethical dilemma

### Format

**Single Theory:**
```yaml
moral_psychology: "Moral Foundations Theory"
```

**Multiple Theories:**
```yaml
moral_psychology:
  - Moral Foundations Theory
  - Dual Process Theory
```

---

## Stage 7: Data Nature Classification

### Fields
- `is_benchmark`: Yes/No/N/A/Unknown
- `is_eval`: Yes/No/N/A/Unknown
- `is_dataset`: Yes/No/N/A/Unknown
- `data_description`: String (auto-generated)
- `data_metrics`: String (auto-extracted)

### Script
`PYTHON/classify_data_nature.py`

### Scope
Applied to **ALL** papers

### Definitions

#### Benchmarks
Papers that introduce or use **standardized test suites** with metrics.

**Keywords:**
- benchmark, evaluation suite, test suite
- leaderboard, comparative evaluation
- standard test, assessment suite

**Examples:**
- TruthfulQA, HELM, HaluEval, MMLU
- Moral Machine, Social Chemistry Benchmark

#### Evaluations
Papers that provide **evaluation/assessment methods** (may not be standardized).

**Keywords:**
- evaluat*, assess*, measur*
- testing, metric*, performance evaluation
- comparative study, empirical analysis

**Note:** Many papers are both benchmarks AND evaluations.

#### Datasets
Papers that introduce **new datasets or corpora**.

**Keywords:**
- dataset, corpus/corpora, collection
- database, annotated data, training data
- compiled data, gathered data

**Examples:**
- Moral Stories, Social Chemistry 101, BOLD
- GurbaniDB, Jigsaw Toxicity Dataset

### Data Description (Auto-generated)

**Format:**
- Benchmarks: "Benchmark for [domain]"
- Datasets: "Annotated dataset for [task]"
- Evaluations: "Evaluation framework for [domain]"

**Examples:**
- "Benchmark for moral/ethical reasoning"
- "Annotated dataset for hate speech detection"
- "Evaluation framework for AI safety"

**Logic:** Combines type with detected domain/task from abstract.

### Data Metrics (Auto-extracted)

**Regex Patterns for Quantitative Extraction:**
- Question/example counts: "817 questions", "5,000 examples"
- Language counts: "100 languages", "17 languages"
- Token counts: "32k tokens", "100K tokens"
- File sizes: "33.4 GB"
- Categories: "38 categories", "10 scenarios"

**Example:**
```yaml
data_metrics: "817 questions, 6 tasks, 38 categories"
```

**Note:** Only ~11% of papers (58/533) had extractable metrics in abstracts.

### Statistics (From 533 Papers)
- **223 Benchmarks** (42%)
- **329 Evaluations** (62%)
- **269 Datasets** (51%)
- **116 papers** are all three categories
- **110 papers** don't fit any category

### Edge Cases

**Benchmark vs. Evaluation:**
- **Benchmark** = standardized, reusable test suite (MMLU, GSM8K)
- **Evaluation** = any assessment method (may be one-time)
- If standardized → both benchmark and eval
- If ad-hoc assessment → eval only

**Dataset without Benchmark:**
- Wikipedia dumps, Common Crawl → dataset but not benchmark
- No standardized tasks or metrics

**All Three:**
- Paper introduces dataset + defines standard tasks + provides evaluation framework
- Example: "TruthfulQA: Measuring How Models Mimic Human Falsehoods"

---

## Tag Aggregation (Post-Classification)

### Field
`newtags`: String (comma-separated)

### Script
`PYTHON/generate_newtags.py`

### Purpose
Aggregates all classification features into searchable tag string.

### Sources (Priority Order)
1. Ethical Frameworks ("Virtue Ethics", "Deontology", "Utilitarianism")
2. Ethics Perspective (e.g., "AI Safety & Alignment", "Bias & Fairness")
3. Research Topic (e.g., "Machine Learning", "NLP")
4. Cultural Values (e.g., "Chinese", "Ubuntu")
5. Religious Values (e.g., "Islam", "Christianity")
6. Moral Psychology (e.g., "Moral Foundations Theory")
7. Data Nature ("Benchmark", "Dataset", "Evaluation")

### Format

**String, comma-separated:**
```yaml
newtags: "Virtue Ethics, Chinese, Buddhism, Benchmark, Moral Foundations Theory"
```

**NOT a YAML list** (see `yaml-standards.md` for rationale).

### Normalization
- Values with separators (`/` or `,`) are split: "African/Ubuntu" → "African, Ubuntu"
- Duplicates removed
- Alphabetical order (for consistency)

---

## Classification Workflow (Batch)

### Recommended Order

```bash
# Stage 1: Ethics Overall
python3 PYTHON/classify_ethics.py

# Stage 2: Ethics Frameworks (same script, multiple fields)
# Already done in Stage 1

# Stage 3: Ethics Perspective (filtered: ethics_overall=Yes, no frameworks)
python3 PYTHON/classify_ethics_perspective.py

# Stage 4: Research Topic (filtered: ethics_overall=No)
python3 PYTHON/classify_non_ethics_topics.py

# Stage 5: Cultural & Religious (all papers)
python3 PYTHON/classify_cultural_religious.py

# Stage 6: Moral Psychology (all papers)
python3 PYTHON/classify_moral_psych.py

# Stage 7: Data Nature (all papers)
python3 PYTHON/classify_data_nature.py

# Final: Tag Aggregation
python3 PYTHON/generate_newtags.py

# Validation
python3 PYTHON/validate_all_papers.py
```

### Incremental Classification (New Papers)

For newly imported papers:
1. Run all 7 stages (don't skip - some stages are conditional)
2. Validate YAML after each stage
3. Commit after full pipeline completes

### Re-classification

If classification logic changes:
1. Back up current state: `git commit -m "Pre-reclassification backup"`
2. Run affected stages only (e.g., if virtue_ethics keywords updated, run Stage 2 + newtags)
3. Validate: `python3 PYTHON/validate_all_papers.py`
4. Review diff: `git diff papers/ | head -100`
5. Commit if changes look correct

---

## Reporting

### Scripts
- `PYTHON/generate_stats.py` → `STATISTICS/20260119-paper-statistics-1.md` (General Stats & Frameworks)
- `PYTHON/generate_report_v2.py` → `STATISTICS/20260119-paper-statistics-2.md` (Cultural, Religious, Psych)

### Format
```
Year, Author, [[Filename|Title]]
```

**Obsidian-friendly Wikilinks** (NOT standard markdown with URL encoding).

---

## Quality Checks

### After Classification

```bash
# Check for papers missing classifications
grep -L "ethics_overall:" papers/*.md | wc -l  # Should be 0

# Check for orphaned ethics_perspective (should have ethics_overall=Yes)
# (Use validation scripts)

# Check newtags aggregation
grep -c "newtags:" papers/*.md  # Should equal total papers

# Validate all YAML
python3 PYTHON/validate_all_papers.py
```

### Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Papers with ethics_overall=No but ethics_perspective set | Pipeline ran out of order | Re-run Stage 3 with filter |
| Duplicate tags in newtags | generate_newtags.py bug | Re-run with deduplication |
| Missing frameworks in newtags | generate_newtags.py not run | Run generate_newtags.py |

---

## Related Standards

- **YAML Safety:** `yaml-standards.md` (mandatory for all classification scripts)
- **Paper Metadata Schema:** `paper-metadata-schema.md` (field definitions)
- **Data Quality:** `../Learnings/learnings-log.md` (classification edge cases)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-02 | Initial standard (extracted from LLM_CONTEXT.md) |
