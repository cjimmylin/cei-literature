# Paper Metadata Schema

**Version:** 1.0
**Created:** 2026-02-02
**Category:** Data Structure Reference
**Applies to:** All paper files in `papers/`

---

## Overview

This document defines all YAML frontmatter fields used in CEI Literature Vault paper files. Each paper is a `.md` file with YAML frontmatter + markdown body.

**Format:**
```yaml
---
[YAML frontmatter fields]
---

# [Paper Title]
[Markdown body content]
```

---

## Field Categories

1. **Zotero Fields** - Imported from Zotero (read-only, managed externally)
2. **Classification Fields** - Added by classification pipeline
3. **Enrichment Fields** - Added by manual or automated enrichment
4. **File Linking Fields** - Internal vault references
5. **Metadata Fields** - Additional metadata

---

## 1. Zotero Fields (Core Metadata)

### key
- **Type:** String
- **Required:** Yes
- **Format:** Alphanumeric, unique
- **Source:** Zotero item key
- **Example:** `key: 2KFZELQU`
- **Notes:** Primary identifier, immutable

### type
- **Type:** String
- **Required:** Yes
- **Format:** Zotero item type
- **Values:** `journalArticle`, `conferencePaper`, `preprint`, `document`, `report`, `book`, `thesis`
- **Example:** `type: journalArticle`

### title / short_title
- **Type:** String
- **Required:** One of them required
- **Format:** Quoted if contains special chars
- **Example:** `short_title: "Concrete Problems in AI Safety"`
- **Notes:** `short_title` preferred for display

### year
- **Type:** Integer
- **Required:** Yes
- **Format:** YYYY
- **Example:** `year: 2016`
- **Notes:** Publication year, used in filename `YYYY-Author-Title.md`

### first_author
- **Type:** Wikilink (String)
- **Required:** Yes
- **Format:** Quoted wikilink `"[[Author Name]]"`
- **Example:** `first_author: "[[Dario Amodei]]"`
- **Notes:** MUST be quoted (YAML standard), links to `Authors/Author Name.md`

### authors
- **Type:** String
- **Required:** Recommended
- **Format:** Semicolon-separated list
- **Example:** `authors: "Dario Amodei; Chris Olah; Jacob Steinhardt"`
- **Notes:** Full author list, used for display

### url
- **Type:** String (URL)
- **Required:** Recommended
- **Format:** Full URL
- **Example:** `url: "https://arxiv.org/abs/1606.06565"`
- **Notes:** Primary source URL (arXiv, publisher, ACL Anthology)

### external_pdf
- **Type:** String (URL)
- **Required:** Optional
- **Format:** Direct PDF URL
- **Example:** `external_pdf: "https://arxiv.org/pdf/1606.06565.pdf"`
- **Notes:** Direct link to PDF on external server

### abstract
- **Type:** String (Multiline)
- **Required:** Recommended
- **Format:** Plain text, no markdown
- **Example:** `abstract: "Rapid progress in machine learning..."`
- **Notes:** Paper abstract, used for classification

### DOI
- **Type:** String
- **Required:** Optional
- **Format:** DOI identifier
- **Example:** `DOI: "10.1145/1234567"`
- **Notes:** Digital Object Identifier

### publication_title / container-title
- **Type:** String
- **Required:** Optional (for journal articles/conference papers)
- **Format:** Journal or conference name
- **Example:** `publication_title: "Neural Information Processing Systems"`
- **Notes:** Venue name

---

## 2. Classification Fields

### ethics_overall
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = Yes equivalent)
- **Example:** `ethics_overall: 82`
- **Notes:** Broad filter for ethical content. Score computed by weighted keyword matching.
- **Backward Compatibility:** Legacy `"Yes"`/`"No"` strings accepted during transition. Use `parse_ethics_value()` from `ethics_scoring.py` to normalize.
- **Script:** `classify_ethics.py` / `ethics_scoring.py` (Stage 1)

### virtue_ethics
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = Yes equivalent)
- **Example:** `virtue_ethics: 0`
- **Notes:** Virtue ethics framework detected
- **Backward Compatibility:** Legacy `"Yes"`/`"No"` accepted. Use `parse_ethics_value()` to normalize.
- **Script:** `classify_ethics.py` / `ethics_scoring.py` (Stage 2)

### deontological_ethics
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = Yes equivalent)
- **Example:** `deontological_ethics: 0`
- **Notes:** Deontological ethics framework detected
- **Backward Compatibility:** Legacy `"Yes"`/`"No"` accepted. Use `parse_ethics_value()` to normalize.
- **Script:** `classify_ethics.py` / `ethics_scoring.py` (Stage 2)

### utilitarian_ethics
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = Yes equivalent)
- **Example:** `utilitarian_ethics: 0`
- **Notes:** Utilitarian ethics framework detected
- **Backward Compatibility:** Legacy `"Yes"`/`"No"` accepted. Use `parse_ethics_value()` to normalize.
- **Script:** `classify_ethics.py` / `ethics_scoring.py` (Stage 2)

### care_ethics
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = Yes equivalent)
- **Example:** `care_ethics: 0`
- **Notes:** Ethics of care score. Detects care ethics, feminist ethics, relational ethics, Gilligan, Noddings.
- **Backward Compatibility:** Legacy `"Yes"`/`"No"` accepted. Use `parse_ethics_value()` to normalize.
- **Script:** `classify_ethics.py` / `ethics_scoring.py` (Stage 2)

### contractarian_ethics
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = Yes equivalent)
- **Example:** `contractarian_ethics: 0`
- **Notes:** Contractarian/social contract ethics score. Detects Rawls, social contract, veil of ignorance, distributive justice.
- **Backward Compatibility:** Legacy `"Yes"`/`"No"` accepted. Use `parse_ethics_value()` to normalize.
- **Script:** `classify_ethics.py` / `ethics_scoring.py` (Stage 2)

### ethics_perspective
- **Type:** String
- **Required:** Conditional (if ethics_overall=Yes but no frameworks)
- **Values:** See `classification-logic.md` for full list
- **Common Values:**
  - `"AI Safety & Alignment"`
  - `"Bias & Fairness"`
  - `"Toxicity & Hate Speech"`
  - `"Moral Reasoning & Psychology"`
  - `"Truthfulness & Factuality"`
  - `"Privacy & Surveillance"`
  - `"Responsible AI"`
- **Example:** `ethics_perspective: "AI Safety & Alignment"`
- **Notes:** Ethical category for papers without traditional frameworks
- **Script:** `classify_ethics_perspective.py` (Stage 3)

### research_topic
- **Type:** String
- **Required:** Conditional (if ethics_overall=No)
- **Values:** See `classification-logic.md` for full list
- **Common Values:**
  - `"Machine Learning"`
  - `"NLP & Representation Learning"`
  - `"Question Answering"`
  - `"Machine Translation"`
  - `"Computer Vision"`
  - `"Benchmarks & Datasets"`
  - `"AI Safety & Alignment"` (catch-all)
- **Example:** `research_topic: "Machine Learning"`
- **Notes:** Technical domain for non-ethical papers
- **Script:** `classify_non_ethics_topics.py` (Stage 4)

### national_ethnic_cultural
- **Type:** String or List
- **Required:** Optional
- **Values:** `"N/A"` | String | List
- **Example (single):** `national_ethnic_cultural: "Chinese"`
- **Example (multiple):**
  ```yaml
  national_ethnic_cultural:
    - Chinese
    - Confucian
  ```
- **Example (none):** `national_ethnic_cultural: N/A`
- **Notes:** Cultural/ethnic values detected
- **Script:** `classify_cultural_religious.py` (Stage 5)

### religious_values
- **Type:** String or List
- **Required:** Derived (auto-generated from rv_* scores)
- **Values:** `"N/A"` | String | List
- **Example (single):** `religious_values: "Islam"`
- **Example (multiple):**
  ```yaml
  religious_values:
    - Buddhism
    - Taoism
  ```
- **Example (none):** `religious_values: N/A`
- **Notes:** Derived display field listing all traditions with rv_* score >= 50. No longer directly classified; computed from the 14 rv_* score fields.
- **Script:** `classify_cultural_religious.py` / `religious_values_scoring.py` (Stage 5)

### rv_islam / rv_christianity / rv_buddhism / rv_judaism / rv_hinduism / rv_sikhism / rv_confucianism / rv_taoism / rv_shinto / rv_jainism / rv_bahai / rv_zoroastrianism / rv_ubuntu / rv_indigenous
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = tradition detected)
- **Examples:**
  - `rv_islam: 72` — Islam detected with high confidence
  - `rv_christianity: 0` — Christianity not detected
  - `rv_ubuntu: 55` — Ubuntu tradition marginally detected
- **Notes:** Religious values confidence scores. Each field represents one tradition. Scores >= 50 mean the tradition is detected. Both `religious_values` and `religious_values_list` are derived from these scores.
- **Insertion Order:** rv_* fields go between `religious_values:` and `religious_values_list:` in the YAML frontmatter.
- **Script:** `classify_cultural_religious.py` / `religious_values_scoring.py` (Stage 5)

### mp_mft
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = theory detected)
- **Example:** `mp_mft: 72`
- **Notes:** Moral Foundations Theory (Haidt/Graham) score
- **Script:** `classify_moral_psych.py` / `moral_psych_scoring.py` (Stage 6)

### mp_schwartz
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = theory detected)
- **Example:** `mp_schwartz: 0`
- **Notes:** Value Pluralism / Schwartz basic values score
- **Script:** `classify_moral_psych.py` / `moral_psych_scoring.py` (Stage 6)

### mp_trolley
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = theory detected)
- **Example:** `mp_trolley: 0`
- **Notes:** Trolley / Dilemmas methodology score
- **Script:** `classify_moral_psych.py` / `moral_psych_scoring.py` (Stage 6)

### mp_kohlberg
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = theory detected)
- **Example:** `mp_kohlberg: 0`
- **Notes:** Cognitive Developmental (Kohlberg/Piaget) score
- **Script:** `classify_moral_psych.py` / `moral_psych_scoring.py` (Stage 6)

### mp_dual_process
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = theory detected)
- **Example:** `mp_dual_process: 0`
- **Notes:** Dual Process Theory (Greene) score
- **Script:** `classify_moral_psych.py` / `moral_psych_scoring.py` (Stage 6)

### mp_intuitionist
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = theory detected)
- **Example:** `mp_intuitionist: 0`
- **Notes:** Social Intuitionist Model score
- **Script:** `classify_moral_psych.py` / `moral_psych_scoring.py` (Stage 6)

### mp_dyadic
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = theory detected)
- **Example:** `mp_dyadic: 0`
- **Notes:** Dyadic Morality (Gray) score
- **Script:** `classify_moral_psych.py` / `moral_psych_scoring.py` (Stage 6)

### mp_identity
- **Type:** Integer (0-100)
- **Required:** Yes (after classification)
- **Values:** `0-100` (integer confidence score; >= 50 = theory detected)
- **Example:** `mp_identity: 0`
- **Notes:** Moral Identity score
- **Script:** `classify_moral_psych.py` / `moral_psych_scoring.py` (Stage 6)

### moral_psychology
- **Type:** String
- **Required:** Derived (auto-generated from mp_* scores)
- **Values:** `"N/A"` | Comma-separated theory names
- **Example:** `moral_psychology: "Moral Foundations Theory"`
- **Notes:** Derived display string listing all theories with mp_* score >= 50. No longer directly classified; computed from the 8 mp_* score fields above.
- **Script:** `classify_moral_psych.py` / `moral_psych_scoring.py` (Stage 6)

### is_benchmark
- **Type:** String
- **Required:** Yes (after data nature classification)
- **Values:** `"Yes"` | `"No"` | `"N/A"` | `"Unknown"`
- **Example:** `is_benchmark: "No"`
- **Notes:** Paper introduces/uses benchmark
- **Script:** `classify_data_nature.py` (Stage 7)

### is_eval
- **Type:** String
- **Required:** Yes (after data nature classification)
- **Values:** `"Yes"` | `"No"` | `"N/A"` | `"Unknown"`
- **Example:** `is_eval: "Yes"`
- **Notes:** Paper provides evaluation method
- **Script:** `classify_data_nature.py` (Stage 7)

### is_dataset
- **Type:** String
- **Required:** Yes (after data nature classification)
- **Values:** `"Yes"` | `"No"` | `"N/A"` | `"Unknown"`
- **Example:** `is_dataset: "No"`
- **Notes:** Paper introduces dataset
- **Script:** `classify_data_nature.py` (Stage 7)

### data_description
- **Type:** String
- **Required:** Conditional (if is_benchmark/eval/dataset = Yes)
- **Format:** Auto-generated description
- **Example:** `data_description: "Benchmark for moral/ethical reasoning"`
- **Notes:** Technical description of data contribution
- **Script:** `classify_data_nature.py` (Stage 7)

### data_metrics
- **Type:** String
- **Required:** Optional
- **Format:** Comma-separated metrics
- **Example:** `data_metrics: "817 questions, 6 tasks, 38 categories"`
- **Notes:** Quantitative metrics extracted from abstract
- **Script:** `classify_data_nature.py` (Stage 7)

### newtags
- **Type:** String (comma-separated)
- **Required:** Yes (after tag aggregation)
- **Format:** **String, NOT YAML list**
- **Example:** `newtags: "AI Safety & Alignment, Chinese, Benchmark"`
- **Notes:** Aggregates all classification tags for easy filtering
- **Script:** `generate_newtags.py` (Final stage)
- **CRITICAL:** Must be string (see `yaml-standards.md`)

---

## 3. Enrichment Fields

### key_contribution
- **Type:** String
- **Required:** Recommended (for ethics framework papers)
- **Format:** One-sentence summary
- **Example:** `key_contribution: "The seminal paper defining five concrete technical problems in AI Safety."`
- **Notes:** Specific technical/theoretical contribution
- **Source:** Manual or LLM-derived

### significance
- **Type:** String
- **Required:** Recommended (for ethics framework papers)
- **Format:** One-sentence significance statement
- **Example:** `significance: "Transformed AI Safety from a speculative field into a rigorous engineering discipline."`
- **Notes:** Why this matters for AI alignment
- **Source:** Manual or LLM-derived

### paper_summary
- **Type:** String (Multiline)
- **Required:** Optional
- **Format:** Structured sections (Abstract, Overview, Methodology, Conclusions)
- **Example:** `paper_summary: "Abstract: ... | Overview: ... | Methodology: ... | Conclusions: ..."`
- **Notes:** Condensed summary with section delimiters (`|`)
- **Source:** Automated summarization

---

## 4. File Linking Fields

### local_pdf
- **Type:** Wikilink (String)
- **Required:** Recommended
- **Format:** Quoted wikilink `"[[PDFs/filename.pdf]]"`
- **Example:** `local_pdf: "[[PDFs/2016-Amodei-Concrete Problems in AI Safety.pdf]]"`
- **Notes:** MUST be quoted (see `yaml-standards.md`)
- **Links to:** External PDF directory (configured in `.vault-config.json`)

### pdf_extract
- **Type:** Wikilink (String) or Path (String)
- **Required:** Optional
- **Format:** Path relative to vault root or quoted wikilink
- **Example:** `pdf_extract: "PDF Extracts/2016-Amodei-Concrete Problems in AI Safety.md"`
- **Notes:** Full-text extraction for search
- **Source:** `extract_pdf_text.py` using PyMuPDF

---

## 5. Metadata Fields

### tags
- **Type:** List
- **Required:** Optional
- **Format:** Proper YAML list
- **Example:**
  ```yaml
  tags:
    - AIAlignment
    - Safety
  ```
- **Notes:** Obsidian tags (different from `newtags`)

### Human View
- **Type:** String
- **Required:** Optional
- **Format:** Empty or status
- **Example:** `Human View: "Reviewed"`
- **Notes:** Human review status

### Human View Date
- **Type:** Date
- **Required:** Optional
- **Format:** YYYY-MM-DD
- **Example:** `Human View Date: "2026-02-01"`

### Human View note
- **Type:** String
- **Required:** Optional
- **Format:** Free text
- **Example:** `Human View note: "Excellent foundational paper"`

### Not AI
- **Type:** String
- **Required:** Optional
- **Format:** Empty or reason
- **Example:** `Not AI: "Human-only research"`
- **Notes:** Marks papers outside AI scope

---

## Field Value Conventions

### N/A vs Empty vs "No"

| Value | Meaning | Use Case |
|-------|---------|----------|
| `N/A` | Not applicable | Field doesn't apply to this paper |
| `""` (empty) | Unknown/not yet classified | Field not yet processed |
| `"No"` | Explicitly not present | Classification ran, feature not detected |
| `"Unknown"` | Uncertain | Can't determine from available info |

**Examples:**
```yaml
national_ethnic_cultural: N/A  # Paper has no cultural dimension
religious_values: "No"          # Classification ran, no religious values found
data_metrics: "Not specified"   # No metrics in abstract
```

### Quoting Rules

**MUST quote:**
- Wikilinks: `"[[Author Name]]"`, `"[[PDFs/file.pdf]]"`
- Strings with special chars: `title: "Ethics: A Survey"`
- Values with colons, brackets, hashes

**Optional quote:**
- Simple strings: `ethics_overall: "Yes"` or `ethics_overall: Yes`
- Numbers: `year: 2016` (no quotes)

**See `yaml-standards.md` for comprehensive quoting rules.**

---

## Example Complete Paper

```yaml
---
key: 2KFZELQU
type: document
short_title: "Concrete Problems in AI Safety"
year: 2016
first_author: "[[Dario Amodei]]"
authors: "Dario Amodei; Chris Olah; Jacob Steinhardt; Paul Christiano; John Schulman; Dan Mané"
url: "https://arxiv.org/abs/1606.06565"
external_pdf: "https://arxiv.org/pdf/1606.06565.pdf"
abstract: "Rapid progress in machine learning and artificial intelligence..."

# Classification Fields
ethics_overall: 82
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
care_ethics: 0
contractarian_ethics: 0
ethics_perspective: "AI Safety & Alignment"
national_ethnic_cultural: N/A
religious_values: N/A
rv_islam: 0
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
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
newtags: "AI Safety & Alignment"

# Enrichment Fields
key_contribution: "Defines five concrete technical problems in AI Safety."
significance: "Transformed AI Safety into rigorous engineering discipline."
paper_summary: "Abstract: ... | Overview: ... | Methodology: ... | Conclusions: ..."

# File Links
local_pdf: "[[PDFs/2016-Amodei-Concrete Problems in AI Safety.pdf]]"
pdf_extract: "PDF Extracts/2016-Amodei-Concrete Problems in AI Safety.md"

# Metadata
tags:
  - AIAlignment
  - Safety
Human View: ""
Human View Date: ""
Human View note: ""
Not AI: ""
---

# Concrete Problems in AI Safety

[Markdown body content...]
```

---

## Field Addition Workflow

### Adding New Classification Fields

1. **Update this schema** with field definition
2. **Update classification script** to populate field
3. **Update `generate_newtags.py`** if field should appear in newtags
4. **Run classification** on all papers (or filtered subset)
5. **Validate YAML** with `validate_all_papers.py`
6. **Update reports** if field should appear in statistics

### Deprecating Fields

1. **Mark field as deprecated** in this schema
2. **Create migration script** to remove from all papers
3. **Update classification scripts** to stop populating
4. **Run migration** and validate
5. **Remove from schema** after deprecation period

---

## Validation Rules

### Required Field Checks
```python
REQUIRED_FIELDS = ['key', 'type', 'year', 'first_author']
```

### Conditional Field Checks
```python
# Use parse_ethics_value() to normalize int scores and legacy strings
from PYTHON.ethics_scoring import parse_ethics_value

if parse_ethics_value(ethics_overall) >= 50 and all(
    parse_ethics_value(fw) < 50 for fw in [virtue, deont, util, care, contract]
):
    # ethics_perspective SHOULD be set

if parse_ethics_value(ethics_overall) < 50:
    # research_topic SHOULD be set

if any(is_x == "Yes" for is_x in [is_benchmark, is_eval, is_dataset]):
    # data_description SHOULD be set
```

### Format Checks
```python
# Year should be 4-digit integer
assert len(str(year)) == 4

# first_author should be quoted wikilink
assert first_author.startswith('"[[') and first_author.endswith(']]"')

# newtags should be string, not list
assert isinstance(newtags, str)

# See validate_papers_enhanced.py for comprehensive checks
```

---

## Related Standards

- **YAML Safety:** `yaml-standards.md` (modification procedures)
- **Classification Logic:** `classification-logic.md` (how fields are populated)
- **File Safety:** `file-safety.md` (NO DELETIONS rule)

---

## Migration from Zotero

### Import Workflow

1. **Export from Zotero:** CSV format with all metadata
2. **Run import script:** `import_papers.py` (creates .md files)
3. **Run classification pipeline:** 7-stage classification
4. **Validate:** `validate_all_papers.py`
5. **Manual enrichment:** Add key_contribution, significance
6. **PDF download:** `/download-pdf` skill
7. **Extract:** `/extract-pdf-text` skill

### Mapping Zotero → Vault Fields

| Zotero Field | Vault Field | Notes |
|--------------|-------------|-------|
| Item Key | `key` | Unique identifier |
| Item Type | `type` | Mapped to Zotero types |
| Title | `short_title` or `title` | Prefer short_title |
| Publication Year | `year` | YYYY format |
| First Author | `first_author` | Convert to wikilink |
| Authors | `authors` | Semicolon-separated |
| URL | `url` | Primary source |
| DOI | `DOI` | If available |
| Abstract | `abstract` | Plain text |

---

**Version History:**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-02 | Initial schema documentation |
| 1.1 | 2026-03-13 | Ethics fields changed from "Yes"/"No" strings to 0-100 integer confidence scores |
| 1.2 | 2026-03-13 | Added 8 mp_* moral psychology score fields (0-100); moral_psychology now derived |
| 1.3 | 2026-03-13 | Added 14 rv_* religious values score fields (0-100); religious_values now derived |
| 1.4 | 2026-03-13 | Added care_ethics and contractarian_ethics fields (0-100); normative frameworks expanded from 3 to 5 |
