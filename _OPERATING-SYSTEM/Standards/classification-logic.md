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
Stage 2: Ethics Frameworks (Virtue/Deontological/Utilitarian/Care/Contractarian)
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
`ethics_overall`: Integer 0-100 (>= 50 = ethics-relevant)

### Purpose
Broad filter to identify papers with any ethical dimension, with confidence scoring.

### Script
`PYTHON/classify_ethics.py` (calls `PYTHON/ethics_scoring.py`)

### Scoring Algorithm

The scoring system replaced the binary Yes/No with a weighted confidence score:

```
score = strong_matches x 15 + medium_matches x 5 - fp_context x 10 + title_bonus(20)
```

- **strong_matches**: High-confidence ethics keywords (e.g., "ethical", "morality", "deontological")
- **medium_matches**: Moderate-confidence keywords (e.g., "fairness", "bias", "alignment")
- **fp_context**: False-positive contextual penalties (e.g., "bias" in purely statistical context)
- **title_bonus(20)**: +20 if ethics keywords appear in title (stronger signal than abstract)
- **Threshold**: >= 50 classified as ethics-relevant (equivalent to old "Yes")
- **Canonical keyword lists**: Defined in `PYTHON/ethics_scoring.py`

### Detection Logic
Weighted keyword matching on abstracts and titles.

**Trigger Keywords** (see `PYTHON/ethics_scoring.py` for canonical, weighted lists):
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
- `virtue_ethics`: Integer 0-100 (>= 50 = framework detected)
- `deontological_ethics`: Integer 0-100 (>= 50 = framework detected)
- `utilitarian_ethics`: Integer 0-100 (>= 50 = framework detected)
- `care_ethics`: Integer 0-100 (>= 50 = framework detected)
- `contractarian_ethics`: Integer 0-100 (>= 50 = framework detected)

### Purpose
Identify papers grounded in specific philosophical frameworks (5 normative frameworks).

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

#### Care Ethics
**Keywords:**
- care ethics, ethics of care
- feminist ethics, relational ethics
- gilligan, noddings, held, slote
- empathy, caregiving, compassion
- interdependence, vulnerability
- caring relationship, care-based

**Examples:**
- "An ethics of care approach to AI caregiving robots"
- "Gilligan's relational ethics in algorithmic decision-making"

#### Contractarian Ethics
**Keywords:**
- social contract, contractarianism, contractualism
- rawls, rawlsian, scanlon
- veil of ignorance, original position
- justice as fairness, distributive justice
- maximin, difference principle
- reasonable agreement, moral contract

**Examples:**
- "Rawlsian fairness in machine learning classifiers"
- "A social contract theory for AI governance"

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
- `ethics_overall` >= 50 (ethics-relevant) AND
- No specific framework detected (all five framework scores < 50)

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
Applied **ONLY** to papers where `ethics_overall` < 50 (not ethics-relevant)

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

#### Fields
- `rv_islam`: Integer 0-100 (Islam)
- `rv_christianity`: Integer 0-100 (Christianity)
- `rv_buddhism`: Integer 0-100 (Buddhism)
- `rv_judaism`: Integer 0-100 (Judaism)
- `rv_hinduism`: Integer 0-100 (Hinduism)
- `rv_sikhism`: Integer 0-100 (Sikhism)
- `rv_confucianism`: Integer 0-100 (Confucianism)
- `rv_taoism`: Integer 0-100 (Taoism)
- `rv_shinto`: Integer 0-100 (Shinto)
- `rv_jainism`: Integer 0-100 (Jainism)
- `rv_bahai`: Integer 0-100 (Baha'i Faith)
- `rv_zoroastrianism`: Integer 0-100 (Zoroastrianism)
- `rv_ubuntu`: Integer 0-100 (Ubuntu)
- `rv_indigenous`: Integer 0-100 (Indigenous traditions)
- `religious_values`: String/List (derived display — lists traditions with score >= 50)

#### Scoring Algorithm

Uses the same weighted formula as ethics and moral psychology scoring:

```
score = strong_matches x 15 + medium_matches x 5 - fp_context x 10 + title_bonus(20)
```

- **strong_matches**: High-confidence tradition-specific keywords (e.g., "Islamic ethics", "Quran", "Buddhist")
- **medium_matches**: Moderate-confidence keywords (e.g., "halal", "dharma", "karma")
- **fp_context**: False-positive contextual penalties for generic terms
- **title_bonus(20)**: +20 if tradition keywords appear in title
- **Strong-floor**: Any strong match guarantees minimum score of 50
- **Threshold**: >= 50 classified as tradition detected
- **Clamped**: [0, 100]
- **Canonical keyword lists**: Defined in `PYTHON/religious_values_scoring.py`

#### Derived `religious_values` Field

The `religious_values` field is now **derived** from rv_* scores, not directly classified. After scoring all 14 traditions, any tradition with score >= 50 is included:

- 0 traditions >= 50: `religious_values: N/A`
- 1 tradition >= 50: `religious_values: "Islam"`
- 2+ traditions >= 50: `religious_values:\n  - Buddhism\n  - Taoism`

**Detection Logic:**
- Keyword matching on titles and abstracts
- Explicit mentions of religious texts, concepts, values

**Examples:**
- "Islamic ethics in AI governance" → `rv_islam: 72`
- "Christian virtue in autonomous systems" → `rv_christianity: 65`
- "GurbaniDB: Sikh scripture dataset" → `rv_sikhism: 55`

### Format

**Single Value:**
```yaml
national_ethnic_cultural: "Chinese"
religious_values: "Islam"
rv_islam: 72
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
```

**Multiple Values:**
```yaml
national_ethnic_cultural:
  - Chinese
  - Confucian
religious_values:
  - Buddhism
  - Taoism
rv_islam: 0
rv_christianity: 0
rv_buddhism: 65
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 55
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
```

---

## Stage 6: Moral Psychology

### Fields
- `mp_mft`: Integer 0-100 (Moral Foundations Theory)
- `mp_schwartz`: Integer 0-100 (Value Pluralism / Schwartz)
- `mp_trolley`: Integer 0-100 (Trolley / Dilemmas)
- `mp_kohlberg`: Integer 0-100 (Cognitive Developmental)
- `mp_dual_process`: Integer 0-100 (Dual Process Theory)
- `mp_intuitionist`: Integer 0-100 (Social Intuitionist Model)
- `mp_dyadic`: Integer 0-100 (Dyadic Morality)
- `mp_identity`: Integer 0-100 (Moral Identity)
- `moral_psychology`: String (derived display — lists theories with score >= 50)

### Script
`PYTHON/classify_moral_psych.py` (calls `PYTHON/moral_psych_scoring.py`)

### Scope
Applied to **ALL** papers

### Scoring Algorithm

Uses the same weighted formula as ethics scoring:

```
score = strong_matches x 15 + medium_matches x 5 - fp_context x 10 + title_bonus(20)
```

- **strong_matches**: High-confidence theory-specific keywords (e.g., "moral foundations", "Haidt", "trolley problem")
- **medium_matches**: Moderate-confidence keywords (e.g., "care/harm", "moral dilemma")
- **fp_context**: False-positive contextual penalties for generic terms
- **title_bonus(20)**: +20 if theory keywords appear in title
- **Threshold**: >= 50 classified as theory detected
- **Canonical keyword lists**: Defined in `PYTHON/moral_psych_scoring.py`

### Per-Theory Keyword Tiers (Summary)

Full keyword lists are in `PYTHON/moral_psych_scoring.py`. Brief summary:

| Theory | Strong Keywords | Medium Keywords | FP-Prone Terms |
|--------|----------------|-----------------|----------------|
| MFT (`mp_mft`) | moral foundations, MFT, Haidt | care/harm, loyalty/betrayal, sanctity | fairness (generic) |
| Schwartz (`mp_schwartz`) | Schwartz values, value survey | Achievement, Power, Security | Achievement (generic), Power (generic), Security (generic) |
| Trolley (`mp_trolley`) | trolley problem, trolley dilemma | moral dilemma, ethical dilemma | dilemma (generic) |
| Kohlberg (`mp_kohlberg`) | Kohlberg, moral development stages | pre-conventional, post-conventional | development (generic) |
| Dual Process (`mp_dual_process`) | dual process, Greene (moral context) | System 1, System 2 (moral context) | system (generic) |
| Intuitionist (`mp_intuitionist`) | social intuitionist, moral intuition | gut feeling, automatic judgment | intuition (generic) |
| Dyadic (`mp_dyadic`) | dyadic morality, moral dyad, Gray | agent-patient, harm-based | agent (generic) |
| Identity (`mp_identity`) | moral identity, moral self | moral centrality, moral commitment | identity (generic) |

### Why FP Handling Is Critical

Many moral psychology terms are generic English words that appear frequently in non-psychology contexts:
- **"Achievement"**, **"Power"**, **"Security"** (Schwartz values) appear in ML performance papers
- **"Agent"** (Dyadic) appears in RL/multi-agent systems papers
- **"Identity"** appears in NLP identity-related papers unrelated to moral identity
- **"System"** appears ubiquitously in CS papers

Without FP penalties, these generic terms would cause massive over-classification. The `fp_context` deduction ensures that papers using these words in non-psychological contexts receive lower scores.

### Derived `moral_psychology` String

The `moral_psychology` field is now **derived** from mp_* scores, not directly classified. After scoring all 8 theories, any theory with score >= 50 is included in the display string:

- 0 theories >= 50: `moral_psychology: N/A`
- 1 theory >= 50: `moral_psychology: "Moral Foundations Theory"`
- 2+ theories >= 50: `moral_psychology: "Moral Foundations Theory, Dual Process Theory"`

### Categories (Psychological Schools/Theories)

1. **Moral Foundations Theory** (`mp_mft`) - Haidt/Graham (Care, Fairness, Loyalty, Authority, Sanctity)
2. **Value Pluralism / Schwartz** (`mp_schwartz`) - Schwartz's 10 basic values
3. **Trolley / Dilemmas** (`mp_trolley`) - Trolley problems as methodology
4. **Cognitive Developmental** (`mp_kohlberg`) - Kohlberg/Piaget stages of moral development
5. **Dual Process Theory** (`mp_dual_process`) - Greene (emotional vs. rational moral judgment)
6. **Social Intuitionist Model** (`mp_intuitionist`) - Haidt's intuitionist approach
7. **Dyadic Morality** (`mp_dyadic`) - Gray (moral dyad: agent & patient)
8. **Moral Identity** (`mp_identity`) - Moral self-concept and centrality

### Format

```yaml
mp_mft: 72
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Moral Foundations Theory"
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
1. Ethical Frameworks ("Virtue Ethics", "Deontology", "Utilitarianism", "Care Ethics", "Contractarian Ethics")
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
| 1.1 | 2026-03-13 | Ethics scoring: binary Yes/No replaced with 0-100 integer confidence scores |
| 1.2 | 2026-03-13 | Moral psychology scoring: 8 mp_* fields (0-100) replace direct classification; moral_psychology now derived |
| 1.3 | 2026-03-13 | Religious values scoring: 14 rv_* fields (0-100); religious_values now derived from scores |
| 1.4 | 2026-03-13 | Normative ethics expanded from 3 to 5 frameworks: added care_ethics and contractarian_ethics |
