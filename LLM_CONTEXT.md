# LLM Context & Learnings

This document summarizes the automated metadata enrichment process performed on the CEI Literature Vault in January 2026. It is intended to help future AI assistants understand the structure, logic, and scripts used to classify the literature.

---

## ⛔ CRITICAL: NO FILE DELETIONS (January 2026)

**NEVER use `rm`, `unlink`, or ANY delete command in this vault.**

```bash
# ❌ FORBIDDEN
rm file.pdf

# ✅ REQUIRED
mv file.pdf RECYCLE-BIN/
```

**Why**: Session 7 accidentally deleted 422 PDF files using `rm`. This rule is absolute and has no exceptions. All file removals must use `mv` to `RECYCLE-BIN/`.

---

## ⚠️ CRITICAL: YAML Frontmatter Standards (January 2026)

**Important**: This section documents lessons learned from a systematic YAML corruption issue that was identified and fixed in January 2026. All future scripts and modifications MUST follow these standards.

### The Issue
In January 2026, 530+ papers had corrupted YAML frontmatter with:
1. **Orphaned list items** - `  - "#Tag"` without a parent key
2. **Missing newlines** - Closing marker `---` without proper newline separation
3. **Wrong formats** - List items where strings were needed

This broke Obsidian's properties panel display and risked data integrity.

### The Solution
A comprehensive prevention system was implemented:
- **Utilities library**: `PYTHON/yaml_frontmatter_utils.py` (required for all YAML operations)
- **Validation**: Mandatory before any write operations
- **Documentation**: `YAML_SAFEGUARDS.md` (complete reference)
- **Playbook**: `DEVELOPER_PLAYBOOK.md` (how-to guide)

### CRITICAL RULES FOR ALL FUTURE WORK

**MANDATORY**:
0. **NEVER use `rm` - always `mv` to RECYCLE-BIN/** (destroyed 422 PDFs in Session 7)
1. Import from utilities library: `from PYTHON.yaml_frontmatter_utils import ...`
2. Use safe operations: `extract_frontmatter()`, `write_paper()`, `validate_frontmatter()`
3. Never use regex directly on YAML frontmatter
4. Never concatenate YAML strings manually
5. Always validate before writing: `validate_frontmatter()` check required
6. All list items must have parent keys (no orphaned `  - ` items)
7. Closing marker must be `\n---\n` (newlines before AND after)

**For any script that modifies paper metadata:**
```python
from PYTHON.yaml_frontmatter_utils import extract_frontmatter, write_paper

# Safe pattern:
fm, body = extract_frontmatter(content)
# ... modify fm ...
write_paper(filepath, fm, body, validate=True)  # Validation mandatory
```

### YAML Structure Format

```yaml
---
key: "string_value"
list_parent:
  - item1
  - item2
newtags: "Item1, Item2"    # String (comma-separated), NOT list
tags:                      # Proper list format
  - TagOne
  - TagTwo
---
```

**Key rules**:
- Opening: `---\n`
- Closing: `\n---\n` (newlines before and after)
- List items: Must have parent key, 2-space indent
- Strings: Quote if contains special chars
- No orphaned items: Every `  - ` needs parent key above it

### Common Corruption Patterns to Avoid

| Pattern | Wrong | Right |
|---------|-------|-------|
| Closing marker | `---\n{fm}---` | `---\n{fm}\n---\n` |
| Orphaned item | `pdf: "..."\n  - Tag` | Create proper `tags:` section |
| Field format | `newtags:\n  - Tag` | `newtags: "Tag1, Tag2"` |
| Hash prefix | `  - #VirtueEthics` | `  - VirtueEthics` |

### Related Documentation
- **YAML_SAFEGUARDS.md** - Complete technical guide (root cause, solutions, testing)
- **DEVELOPER_PLAYBOOK.md** - How-to guide with templates and examples
- **SESSION_LEARNING_2026_01_24.md** - How the fix was analyzed and implemented
- **FIX_SUMMARY_2026_01_24.md** - What was fixed and verification results

### For Future LLM Sessions
1. Read `DEVELOPER_PLAYBOOK.md` before writing any script that modifies YAML
2. Use the provided templates in the playbook
3. Always validate on sample papers first
4. Check validation commands in playbook before and after running
5. Report any YAML issues using utilities library diagnostic

---

## ✅ RESOLVED: Corrupted Abstracts (January 2026)

**Status:** ✅ FULLY RESOLVED - All 80 papers fixed (January 24, 2026)

### The Issue (Historical)
During a previous Zotero import, abstracts were replaced with text about "Einstein-Podolsky-Rosen correlations" and quantum teleportation - completely unrelated to the papers' actual content.

### Detection (Should Return 0)
```bash
grep -l "An unknown quantum state" papers/*.md | wc -l  # Should return 0
```

### Resolution Scripts Created
Two scripts were developed to fix this issue:

| Script | Purpose | Papers Fixed |
|--------|---------|--------------|
| `PYTHON/fix_corrupted_abstracts.py` | Automated fix using body extraction + API calls | 56 |
| `PYTHON/fix_remaining_abstracts.py` | Manual abstracts from web research | 23 |
| Manual fix (RusCode quote escaping) | - | 1 |

### Fix Strategy Applied
1. **Body extraction** (55 papers): Extract correct abstract from `## Abstract` section in paper body
2. **Semantic Scholar API** (1 paper): Fetch via DOI
3. **Manual web research** (23 papers): Search arXiv, HuggingFace, official sites, EA Forum, NeurIPS proceedings
4. **Quote escaping fix** (1 paper): RusCode had markdown formatting in abstract

### Scripts for Future Use
```bash
# Run automated fix (checks for quantum physics text, extracts from body/APIs)
python3 PYTHON/fix_corrupted_abstracts.py

# If automated fix can't find abstract, add to ABSTRACT_FIXES dict and run:
python3 PYTHON/fix_remaining_abstracts.py
```

### Abstract Sources Used
- **arXiv API**: Direct abstract fetch via paper ID
- **Semantic Scholar API**: DOI-based lookup
- **NeurIPS Proceedings**: Conference paper pages
- **OpenReview**: Submitted paper abstracts
- **HuggingFace Datasets**: Dataset descriptions
- **EA Forum / Alignment Forum**: AI safety posts
- **Official project sites**: BIRD-bench, GurbaniDB, etc.

---

## Classification System

We have implemented a multi-stage classification system to enrich paper metadata with ethical and technical properties.

### 1. Ethical Frameworks
**Field:** `ethics_overall` (Yes/No), `virtue_ethics` (Yes/No), `deontological_ethics` (Yes/No), `utilitarian_ethics` (Yes/No)
**Script:** `classify_ethics.py`
**Logic:** Keyword matching on abstracts and titles.
- **Virtue Ethics**: Checks for terms like "virtue", "character", "eudaimonia", "aristotelian".
- **Deontological**: Checks for "duty", "obligation", "kantian", "categorical imperative".
- **Utilitarian**: Checks for "utility", "consequences", "maximize welfare", "greatest good".
- **Ethics Overall**: Checks for broad terms like "ethics", "moral", "value", "fairness", "harm".

### 2. Ethical Perspectives
**Field:** `ethics_perspective` (String)
**Script:** `classify_ethics_perspective.py`
**Scope:** Applied ONLY to papers where `ethics_overall: "Yes"` BUT no specific framework (Virtue/Deontological/Utilitarian) was detected.
**Categories:**
- **AI Safety & Alignment** (e.g., robustness, red teaming, jailbreaks)
- **Bias & Fairness** (e.g., stereotypes, discrimination, equity)
- **Toxicity & Hate Speech** (e.g., abusive language, offensive content)
- **Moral Reasoning & Psychology** (e.g., moral judgment, trolley problems)
- **Truthfulness & Factuality** (e.g., hallucinations, misinformation)
- And others (Privacy, Human Rights, Responsible AI...)

### 3. Research Topics (Non-Ethics)
**Field:** `research_topic` (String)
**Script:** `classify_non_ethics_topics.py`
**Scope:** Applied ONLY to papers where `ethics_overall: "No"`.
**Categories:**
- **Machine Learning** (General ML/DL papers)
- **NLP & Representation Learning** (Embeddings, parsing)
- **Question Answering** (QA specific)
- **Machine Translation**
- **Computer Vision**
- **Benchmarks & Datasets**
- **AI Safety & Alignment** (Catch-all for technical safety papers missed by the strict ethics filter)

### 4. Cultural & Religious Values
**Fields:** `national_ethnic_cultural` (String/List), `religious_values` (String/List)
**Script:** `classify_cultural_religious.py`
**Logic:** Keyword matching on titles and abstracts.
- **Cultural**: 20+ categories including "Chinese", "African/Ubuntu", "American", "Japanese", "Arabic". Scope includes language-specific datasets.
- **Religious**: "Islam", "Christianity", "Buddhism", "Judaism", "Hinduism", etc.

### 5. Moral Psychology
**Field:** `moral_psychology` (String/List)
**Script:** `classify_moral_psych.py`
**Logic:** Detects specific moral psychological schools/theories.
- **Moral Foundations Theory** (Haidt/Graham)
- **Dual Process Theory** (Greene)
- **Value Pluralism / Schwartz Values**
- **Cognitive Developmental** (Kohlberg/Piaget)
- **Dyadic Morality** (Gray)
- **Trolley / Dilemmas** (as a psych methodology)

### 6. Tag Aggregation
**Field:** `newtags` (String, comma-separated)
**Script:** `generate_newtags.py`
**Purpose:** Aggregates all classifying features into a clean list for easy filtering.
**Sources:**
- Ethical Frameworks ("Virtue Ethics", "Deontology", "Utilitarianism")
- Cultural Values (e.g., "Chinese", "Ubuntu")
- Religious Values (e.g., "Islam", "Christianity")
- Moral Psychology (e.g., "Moral Foundations Theory")
- Ethics Perspective (e.g., "Machine Ethics")
- Research Topic (e.g., "Machine Learning")

### 7. Reporting
**Scripts:**
- `generate_stats.py` -> `paper-statistics-1.md` (General Stats & Frameworks)
- `generate_report_v2.py` -> `paper-statistics-2.md` (Cultural, Religious, Psych)

**Purpose:** Generates markdown reports listing papers categorized by the fields above.
**Format:** `Year, Author, [[Filename|Title]]` (Obsidian-friendly Wikilinks).

## Learnings & Edge Cases

1.  **Obsidian Compatibility**:
    - Preferred format for links is **Wikilinks**: `[[Filename|Title]]`.
    - This is more robust in Obsidian than standard markdown links with URL encoding (`%20`).
    - Do NOT wrap links in backticks.

2.  **"No Ethics" Anomalies**:
    - Some papers like *Constitutional AI* or *TruthfulQA* were initially classified as `ethics_overall: "No"` because their abstracts used technical terms ("harmlessness", "hallucination") rather than explicit "ethics/moral" keywords.
    - **Resolution**: We added specific categories in `classify_non_ethics_topics.py` (like "AI Safety" and "Truthfulness") to catch these and label them appropriately in the `research_topic` field. Future passes could refine the `classify_ethics.py` keywords to include "harmlessness" and "truthfulness" as ethics indicators.

3.  **Missing Metadata Analysis**:
    - **Problem**: 27 papers were missing `year` and had filenames starting with `NoYear-`.
    - **Resolution**: We identified years using URL heuristics (arXiv: `2404` -> 2024, ACL: `2025.naacl` -> 2025) and manual verification.
    - **Action**: All files were renamed to `YYYY-Author-Title.md` and metadata updated.

4.  **Metadata Persistence**:
    - The scripts read and rewrite the YAML frontmatter. Care must be taken to preserve existing fields.
    - The regex-based frontmatter extractor is robust but assumes standard YAML format (keys and values).

5.  **Tag Normalization**:
    - Values in `moral_psychology` and `religious_values` often contain separators (`/` or `,`). The `generate_newtags.py` script combines these into a single searchable string.
6.  **Preprint Verification**:
    - Many papers in the vault start as Preprints (ArXiv). We use `check_publication_status.py` to query Semantic Scholar and update the venue/year when they are published.
### 7. Data Nature Classification
**Fields:** `is_benchmark` (Yes/No/N/A/Unknown), `is_eval` (Yes/No/N/A/Unknown), `is_dataset` (Yes/No/N/A/Unknown), `data_description` (String), `data_metrics` (String)
**Script:** `classify_data_nature.py`
**Scope:** Applied to ALL papers (533 papers)
**Logic:** Keyword matching on titles and abstracts to identify:

**Benchmarks** - Papers that introduce or use benchmarking systems:
- Keywords: "benchmark", "evaluation suite", "test suite", "leaderboard", "comparative evaluation"
- Examples: TruthfulQA, HELM, HaluEval, Moral Machine

**Evaluations** - Papers that provide evaluation/assessment methods:
- Keywords: "evaluat*", "assess*", "measur*", "testing", "metric*", "performance evaluation"
- Note: Many papers are both benchmarks AND evaluations

**Datasets** - Papers that introduce new datasets or corpora:
- Keywords: "dataset", "corpus/corpora", "collection", "database", "annotated data", "training data"
- Examples: Moral Stories, Social Chemistry 101, BOLD

**Data Description** - Automatically generated technical descriptions:
- For benchmarks: "Benchmark for [domain]" (e.g., "Benchmark for moral/ethical reasoning")
- For datasets: "Annotated dataset for [task]" (e.g., "Annotated dataset for hate speech detection")
- Combines type with detected domain/task from abstract

**Data Metrics** - Quantitatively extracted using regex patterns:
- Question/example counts: "817 questions", "5,000 examples"
- Language counts: "100 languages", "17 languages"
- Token counts: "32k tokens", "100K tokens"
- File sizes: "33.4 GB"
- Categories: "38 categories", "10 scenarios"
- Only ~11% of papers (58/533) had extractable metrics in abstracts

**Statistics:**
- 223 Benchmarks (42% of papers)
- 329 Evaluations (62% of papers)
- 269 Datasets (51% of papers)
- 116 papers are all three categories
- 110 papers don't fit any category

### 8. Virtue Ethics Enrichment
**Fields:** `key_contribution` (String), `significance` (String)
**Scope:** Applied to papers where `virtue_ethics: "Yes"`
**Logic:** Manually derived or LLM-derived from abstracts/full-text.
- **Key Contribution:** One-sentence summary of the specific technical or theoretical contribution (e.g., "Proposes a phronesis-based architecture...").
- **Significance:** Why this matters for AI alignment (e.g., "Shifts focus from rule compliance to character development").
**Manual Process:** This enrichment was performed in Jan 2026 for ~42 papers. Future papers with this tag should have these fields populated.

### 9. Deontological & Utilitarian Enrichment
**Fields:** `key_contribution`, `significance`
**Scope:** Applied to papers where `deontological_ethics: "Yes"` or `utilitarian_ethics: "Yes"`
**Logic:** Same as Virtue Ethics.
- **Deontology:** Focus on rules, duties, rights (e.g., "Framing AI safety as duty-based constraints").
- **Utilitarianism:** Focus on outcomes, welfare, aggregation (e.g., "Optimizing aggregate utility in multi-agent systems").
**Status:** ~100 papers processed in Jan 2026.

### 10. Reporting Scripts
**Scripts:**
- `generate_stats.py` → `paper-statistics-1.md` (General Stats & Frameworks)
- `generate_report_v2.py` → `paper-statistics-2.md` (Cultural, Religious, Psych)
- `generate_data_report.py` → `data-nature-statistics.md` (Benchmark/Eval/Dataset - detailed)
- `generate_paper_statistics_3.py` → `paper-statistics-3.md` (Benchmark/Eval/Dataset - comprehensive breakdown)

**Purpose:** Generates markdown reports listing papers categorized by various fields.
**Format:** `Year, Author, [[Filename|Title]]` (Obsidian-friendly Wikilinks).

**Report Differences:**
- `paper-statistics-1.md`: Ethics frameworks, perspectives, research topics
- `paper-statistics-2.md`: Cultural, religious, and moral psychology classifications
- `data-nature-statistics.md`: 1,604-line report focusing on benchmarks/evals/datasets with metrics
- `paper-statistics-3.md`: 3,391-line comprehensive report with multi-category breakdowns, grouped by description type, and all papers with extracted metrics

## Learnings & Edge Cases

1.  **Obsidian Compatibility**:
    - Preferred format for links is **Wikilinks**: `[[Filename|Title]]`.
    - This is more robust in Obsidian than standard markdown links with URL encoding (`%20`).
    - Do NOT wrap links in backticks.

2.  **"No Ethics" Anomalies**:
    - Some papers like *Constitutional AI* or *TruthfulQA* were initially classified as `ethics_overall: "No"` because their abstracts used technical terms ("harmlessness", "hallucination") rather than explicit "ethics/moral" keywords.
    - **Resolution**: We added specific categories in `classify_non_ethics_topics.py` (like "AI Safety" and "Truthfulness") to catch these and label them appropriately in the `research_topic` field. Future passes could refine the `classify_ethics.py` keywords to include "harmlessness" and "truthfulness" as ethics indicators.

3.  **Missing Metadata Analysis**:
    - **Problem**: 27 papers were missing `year` and had filenames starting with `NoYear-`.
    - **Resolution**: We identified years using URL heuristics (arXiv: `2404` → 2024, ACL: `2025.naacl` → 2025) and manual verification.
    - **Action**: All files were renamed to `YYYY-Author-Title.md` and metadata updated.

4.  **Metadata Persistence**:
    - The scripts read and rewrite the YAML frontmatter. Care must be taken to preserve existing fields.
    - The regex-based frontmatter extractor is robust but assumes standard YAML format (keys and values).

5.  **Tag Normalization**:
    - Values in `moral_psychology` and `religious_values` often contain separators (`/` or `,`). The `generate_newtags.py` script combines these into a single searchable string.

6.  **Preprint Verification**:
    - Many papers in the vault start as Preprints (ArXiv). We use `check_publication_status.py` to query Semantic Scholar and update the venue/year when they are published.

7.  **Data Nature Classification Limitations**:
    - **Missing Abstracts**: Papers without abstracts (like "Social Chemistry 101") are conservatively classified
    - **Metrics Extraction**: Only 58/533 papers (~11%) had clearly extractable metrics in abstracts; many papers discuss detailed metrics in body text
    - **False Negatives**: Papers using conceptual terms (e.g., "collection", "testbed") without explicit keywords may be missed
    - **Multi-category Papers**: 116 papers are simultaneously benchmarks, evaluations, AND datasets, showing significant overlap

8.  **Keyword Coverage**:
    - The keyword-based approach works well for explicit mentions but may miss:
      - Papers that describe benchmarks/datasets without using those exact terms
      - Papers where the benchmark/dataset is mentioned only in the body, not the abstract
      - Papers using domain-specific terminology (e.g., "test bed" vs "benchmark")

9.  **Unknown Author Resolution**:
    - **Problem**: 12 papers had "Unknown" authors despite having valid properties.
    - **Resolution**: Cross-referenced ArXiv URLs and Title searches to identify authors (e.g., *AEGIS* → Ghosh, *StrongREJECT* → Souly).
- **Action**: Metadata updated and files renamed to `YYYY-Author-Title.md`.

10. **Virtue, Deontological, & Utilitarian Enrichment**:
    - **Problem**: Generic boolean tags ("Yes") don't explain *how* the paper applies the framework.
    - **Resolution**: Added `key_contribution` and `significance` fields to papers in all three major ethical frameworks:
        - `virtue_ethics`: ~42 papers (enriched Jan 2026)
        - `utilitarian_ethics`: ~59 papers (enriched Jan 2026)
        - `deontological_ethics`: ~47 papers (enriched Jan 2026)
    - **Formatting Rule**: These fields must be placed **before** the `ethics_overall` field in the YAML frontmatter. The boolean ethics tags (`virtue_ethics`, etc.) must remain at the very end of the YAML block.
    - **Learning**: Rich text fields provide better context for research. "Deep Dive" searches into specific sub-fields (e.g., Social Welfare Functions for Utilitarianism) yield higher quality results than broad keyword sweeps.

11. **Search Strategy Insights**:
    - **Technical Mapping**: High-quality papers often don't use the high-level ethical term (e.g., "Utilitarianism") but the mathematical implementation (e.g., "Social Welfare Functions", "Reward Modeling"). Agents should search for the *implementation*, not just the *concept*.
    - **OSINT Value**: Significant "bleeding edge" alignment work appears on OpenReview (under review) or Alignment Forum months before formal publication.
    - **Deontological Keywords**: Searching for specific modal verbs ("must", "obligated") or legal frameworks ("Constitutional AI", "Human Rights") yields better deontological papers than the generic term "Deontology".
    - **See**: `skills/paper_discovery/SKILL.md` for the formalized strategy.

### 11. PDF Processing & Summarization
**Scripts:**
- `process_pdfs.py`: Extracts full text from PDFs using PyMuPDF.
- `prepare_analyses.py`: Prepares JSON objects combining text and metadata for analysis.

**Dependencies:** `pymupdf` (Python package `fitz`)

**Learnings:**
- **Extraction Library**: PyMuPDF (`fitz`) proved superior to PyPDF2 and others for this academic corpus, handling large inputs (40k-180k characters) efficiently.
- **Matching Logic**: Isomorphic filename matching (`Paper.pdf` -> `Paper.md`) works perfectly due to the disciplined file naming convention enforced earlier.
- **Content Density**: Academic papers in this vault are dense; full-text extraction yields significant context (avg ~80k chars) which requires capable LLMs for summarization.

### 17. Author Profile Enrichment (Jan 2026)
**Goal:** Systematically enrich author profiles with biographical data, affiliations, and research interests, focusing on authors with "University/Organization" placeholders.

**Key Findings:**
- **Scale of Task:** Over 160 un-enriched authors were identified starting with 'A' alone, organized into 15 "Residual" batches.
- **Data Availability:** Senior researchers at major labs (Meta, Google, Scale AI) and professors have high data availability; independent or junior researchers often require title-based searches to find their specific affiliations.
- **Name Variants:** Authors often appear with middle initials in paper metadata but without them in other contexts. Consolidation is required to prevent duplicate profiles (e.g., [[Adam Kalai]] and [[Adam Tauman Kalai]]).

**Learnings & Strategy:**
- **Search Logic:** Searching for `"[Name]" researcher [Paper Title] affiliation` is the most effective OSINT strategy.
- **Full Names Only:** Only process authors with verifiable full names; avoid initials-only stubs (e.g., "A. Pan").
- **YAML Structure:** Authors MUST follow a consistent frontmatter (title, affiliation, highest_degree, email, research_interests, website, github, google_scholar, semantic_scholar).
- **Consolidation Rule:** If an author has multiple files for name variations, consolidate into the most complete name and update all incoming wikilinks.

## Future Recommendations

-   **Refine Keywords**: The `ETHICS_OVERALL_KEYWORDS` list in `classify_ethics.py` is conservative. It could be expanded to include "robustness", "trustworthiness", and "truthfulness" to capture more implicit ethical work.
-   **LLM Classification**: For ambiguous papers, replacing keyword matching with an LLM-based classifier (using the `generate_text` tool on abstract content) would likely yield higher accuracy, especially for subtle distinctions between "Machine Learning" and "AI Safety".
-   **Expand Metrics Extraction**: The regex patterns in `classify_data_nature.py` could be expanded to capture more variations:
    - Range notations: "100-500 examples"
    - Comparative sizes: "larger than X"
    - Domain-specific units: "hours of audio", "frames", "conversations"
-   **Manual Review of High-Value Papers**: Consider manually reviewing the 110 papers not classified in any category to ensure important benchmarks/datasets aren't missed.
-   **Run Order**: Always run scripts in the established order:
    1.  `classify_ethics.py` (Base classification)
    2.  `classify_ethics_perspective.py` (Refine Yes-Ethics)
    3.  `classify_non_ethics_topics.py` (Refine No-Ethics)
    4.  `classify_cultural_religious.py` (Cultural/Religious values)
    5.  `classify_moral_psych.py` (Moral Psych theories)
    6.  `generate_newtags.py` (Aggregate all)
    7.  `classify_data_nature.py` (Data nature classification - can run independently)
-   **Author Search Efficiency:** For researchers at tech companies (Meta, Google, Amazon), searching for their LinkedIn profile often provides the most up-to-date affiliation and career trajectory.

12. **PDF Processing & Availability**:
    - **PDF Access**: Direct PDF availability for ethics papers is approximately 50-60%.
        - **ArXiv**: High availability. URLs can be reliably constructed from abstract IDs.
        - **Paywalls**: Papers from major journals (Springer, Taylor & Francis, Nature) often lack open-access versions.
    - **ArXiv Discovery**: For paywalled papers, searching ArXiv by title is a highly effective fallback (found ~7% additional open versions).
    - **Vault Structure**:
        - **Directory**: `Lit-WS-PDFs/` folder at vault root.
        - **Metadata**: `local_pdf` frontmatter field (relative path: `Lit-WS-PDFs/filename.pdf`).
        - **Links**: `**Local PDF:** [[Lit-WS-PDFs/filename.pdf|Open PDF]]` added to `## Links` section.
    - **Skill**: `download_pdfs` skill created to automate this process (direct download + ArXiv search).
    - **Advanced Discovery (OSINT)**:
        - **Methods**: Using specific search queries like `"[Title]" filetype:pdf` or `site:[university_domain]` (e.g., `site:aau.dk`) can reveal preprints or institutional copies that are missed by standard academic databases.
        - **Platform Patterns**:
            - **Open Access Repositories**: Many European universities have portals (e.g., Aalborg's `vbn.aau.dk`) that host PDFs of published work.
            - **PhilArchive/OSF**: Philosophical papers are often mirrored on PhilArchive or Open Science Framework (OSF).
            - **ResearchGate**: Transitioning from "Paywalled" to "Request full-text" is common; if a direct PDF is absent, the landing page is the best metadata link.
        - **Source Type Nuances**: A significant portion (approx. 20%) of "missing" papers in high-level sweeps are actually **forthcoming books or book chapters**. These rarely have legal open-access PDFs, and the metadata should point to the publisher or Goodreads page instead of an empty local PDF link.

### 12. Authors CRM
**Location:** `Authors/`
**Purpose:** Centralized researcher database.
**Structure:**
- **Files:** `FullName.md` (e.g., `Ruben E. Laukkonen.md`)
- **Metadata:** Name, affiliation, research interests, and links (Scholar, Website).
- **Linking:** Each author file contains wikilinks to their papers in the `papers/` directory.

**Automation:**
- `populate_authors.py`: Extracts authors from all paper frontmatter and creates/updates author files.
- `update_authors.py`: Refines author metadata (affiliation, research interests).

**Learnings:**
- **Wiki-linking:** Using Obsidian Wikilinks `[[Paper Key|Title]]` allows for bi-directional navigation between authors and papers.
- **Naming Convention:** Using `FullName.md` avoids ambiguity and matches Obsidian's preferred linking style.

### 13. AI Labs Repository
**Location:** `AI Labs/`
**Purpose:** Centralized database for AI labs and their models.
**Structure:**
- **Labs:** `AI Labs/[Lab Name]/README.md` and `AI Labs/[Lab Name]/models.md`
- **Models:** Hierarchical storage in `AI Labs/[Lab Name]/[Model Name]/README.md`
- **Metadata:** Each lab has a `models.md` overview table with wikilinks to individual model READMEs.
- **Template:** `AI Labs/TEMPLATE.md` provides the standard structure for new labs.

**Usage:**
- Use this directory to track lab-specific alignment research, flagship models, and regional AI developments across the US, Europe, and China.
- Individual model sub-folders allow for detailed technical specifications, safety reports, and model-specific paper links to be stored cleanly.

### 14. Statistics Reports Directory (`STATISTICS/`)
**Location:** `STATISTICS/`
**Purpose:** Centralized repository for all generated statistics reports.
**Created:** January 2026 (reorganized from root directory)

Contains 4 auto-generated markdown reports:
- `paper-statistics-1.md` - Ethical frameworks and perspectives
- `paper-statistics-2.md` - Cultural, religious, and moral psychology classifications
- `data-nature-statistics.md` - Detailed benchmark/evaluation/dataset breakdown with metrics
- `paper-statistics-3.md` - Comprehensive data nature report with multi-category analysis

**Generation:**
- Auto-generated via: `python3 PYTHON/generate_*.py` scripts
- Bulk generation: `python3 .agent/skills/generate_reports/scripts/run_reports.py`
- Output format: Obsidian wikilinks (`[[Filename|Title]]`) for navigation
- These files should not be edited directly; regenerate via scripts to update

### 15. Python Scripts Directory (`PYTHON/`)
**Location:** `PYTHON/`
**Purpose:** Centralized repository for all Python utility scripts.
**Created:** January 2026 (reorganized from root directory)

All 29 Python scripts have been moved to the `PYTHON/` directory for better organization:

**Classification Scripts (7):**
- `classify_ethics.py`, `classify_ethics_perspective.py`, `classify_non_ethics_topics.py`
- `classify_cultural_religious.py`, `classify_moral_psych.py`, `classify_data_nature.py`
- `generate_newtags.py`

**Report Generation (4):**
- `generate_stats.py`, `generate_report_v2.py`, `generate_data_report.py`, `generate_paper_statistics_3.py`

**Data Import & Maintenance (5):**
- `convert_csv_to_md.py`, `rename_papers.py`, `regenerate_papers.py`, `update_urls.py`, `resolve_unknowns.py`

**Author Management (4):**
- `populate_authors.py`, `update_authors.py`, `ensure_authors_from_base.py`, `enrich_acl_papers.py`

**PDF & Text Processing (2):**
- `process_pdfs.py`, `prepare_analyses.py`

**Preprint & Abstract Management (4):**
- `fetch_abstracts.py`, `fetch_remaining_abstracts.py`, `check_publication_status.py`, `update_published_preprints.py`

**Utility (3):**
- `download_batch_8.py` (PDF downloading), `add_newtags.py`, `identify_targets.py`

When referencing these scripts in documentation or workflows, use: `python3 PYTHON/<script_name>.py`

### 16. Agent System (Google Antigravity & Claude Code)
**Location:** `.agent/` (Google Antigravity), `.claude/` (Claude Code)
**Purpose:** Automated skills and workflows for vault management via AI agents.
**Created:** January 2026

#### Google Antigravity Skills (`.agent/skills/`)
Each skill has a `SKILL.md` file with YAML frontmatter (name, description, triggers) and a `scripts/` subfolder:

| Skill | Description | Script |
|-------|-------------|--------|
| `classify_papers` | Run full classification pipeline | `run_pipeline.py` |
| `generate_reports` | Generate all statistics reports | `run_reports.py` |
| `fetch_abstracts` | Fetch abstracts from arXiv API | `fetch.py` |
| `check_publication` | Check preprint publication status via Semantic Scholar | `check.py` |
| `download_pdf` | Download PDFs from URLs or arXiv | `download.py` |
| `extract_pdf_text` | Extract text from PDFs to `PDF Extracts/` | `extract.py` |
| `summarize_paper` | Generate structured summaries from PDF text | (workflow-based) |
| `enrich_paper` | Add key_contribution/significance fields | (manual process) |
| `vault_management` | Stats and target identification | `stats.py`, `identify.py` |
| `import_papers` | Import from Zotero CSV | (uses root scripts) |

#### Google Antigravity Workflows (`.agent/workflows/`)
- `add_new_papers.md` - Complete import workflow from Zotero
- `weekly_maintenance.md` - Regular maintenance checklist
- `summarize_papers.md` - Batch paper summarization workflow

#### Claude Code Integration (`.claude/`)
- **Commands** (`.claude/commands/`): 17 slash commands for interactive use
- **Skills** (`.claude/skills/`): 16 detailed skill documents for agent reference

#### Documentation
- `.agent/README.md` - Overview and quick start
- `.agent/AGENT_GUIDE.md` - Detailed guide for AI agents
- `.agent/SKILLS_INDEX.md` - Quick reference for all skills

#### Key Scripts Created/Enhanced
- `.agent/skills/classify_papers/scripts/run_pipeline.py` - Orchestrates 7-stage classification pipeline
- `.agent/skills/generate_reports/scripts/run_reports.py` - Generates all 4 statistics reports
- `.agent/skills/vault_management/scripts/stats.py` - Vault statistics summary
- `.agent/skills/vault_management/scripts/identify.py` - Find papers needing attention by type

For all other scripts, see Section 15: Python Scripts Directory (`PYTHON/`)

#### Rate Limiting
- **arXiv API**: 0.3 second delay between requests
- **Semantic Scholar API**: 4 second delay between requests

**Usage:** Agents should consult `.agent/AGENT_GUIDE.md` for detailed instructions on using skills and workflows.


### 18. Author Profile Enrichment (Status Update Jan 2026)

**Project Status:**
- **Batches A & B**: **COMPLETE** (50+ authors enriched).
- **Residual Batches (C-Z)**: Pending.

**Standard Operating Procedure (SOP):**
Future agents should follow this protocol when enriching authors:
1.  **Signal Detection**: Use `ls -l Authors/` to find small files (< 600 bytes).
2.  **Research**: Use `search_web` to find the author's academic profile (Scholar, University page).
3.  **Enrichment**: Overwrite the file using the schema in `Authors/TEMPLATE.md`.
4.  **Cleaning**: Remove duplicate "initial-only" files (e.g., delete `A. Smith.md` if `Adam Smith.md` exists) and update links.

**Key Learnings from Batches A/B:**
- **High-Impact Priority**: Focus on authors with >1 paper in the vault or significant external reputation.
- **Affiliation Volatility**: Tech researchers move frequently (e.g., Google -> Anthropic). Always prioritize the *current* affiliation but mention significant past roles in the bio.
- **Name Collisions**: Common names (e.g., "Wei Wang") require careful paper-title matching to identify the correct person.

### 19. Session Handover Protocol (New Skill)
**Skill**: `consolidate_memory`
**Purpose**: To ensure no context is lost between sessions.
**Trigger**: End of session / Task completion.
**Action**:
1. Update `LLM_CONTEXT.md` with new learnings.
2. Update `CLAUDE.md`/`GEMINI.md` with new capabilities.
3. Verify `task.md` and `walkthrough.md` are final.

### 20. Batch 4 (2025 Papers) Processing (Status Update Jan 2026)

**Project Status:**
- **Objective**: Process 34 new PDF papers from 2025 (Batches 4a-4h).
- **Completion**: **100%** (34/34 papers processed).
- **Actions**:
    1.  **Content Retrieval**: Retrieved abstracts and metadata from arXiv/DOI/PLOS due to missing local PDFs for some.
    2.  **Summarization**: Generated 6-section structured summaries (Abstract, Detail, Outline, Methods, Results, Artifacts) for all papers.
    3.  **Author Linking**: Linked ~100 authors to the `Authors/` CRM, creating new profiles where necessary (e.g., [[Muhammad Shahrul Zaim Bin Ahmad]]).

**Key Learnings & Insights:**
-   **The "Complexity Gap" (Zhou 2025)**: Moral reasoning performance degrades significantly as context length increases (Sentence -> Paragraph -> Document), especially for low-resource languages like Vietnamese.
-   **Sycophancy Quantification (Zheng 2025)**: New metrics "Turn of Flip" and "Number of Flip" reveal that RLHF training *amplifies* sycophancy compared to base models. Reasoning models (CoT) are more resistant.
-   **Moral Pluralism Frameworks**: A surge in papers (Yaacov, Xiang, Yao) proposing "Pluralistic" or "Conjoint" evaluation methods rather than static rules, suggesting a shift in the field towards "Value-Context" alignment.

**Procedural Note (Z-Author Handling):**
-   Authors with complex names (e.g., Malaysian/Indonesian patronymics like "Zaim Bin Ahmad") should be wikilinked using their **Full Legal Name** as the filename (`[[Muhammad Shahrul Zaim Bin Ahmad]]`) to avoid ambiguity, even if the paper cites them as "Zaim Bin Ahmad".

### 21. Metadata Standardization & Deep Enrichment Session (Jan 24, 2026)

**Goal:** Standardize metadata across the entire vault (535+ papers) and deeply enrich ethics-related papers with qualitative insights.

**Key Achievements:**
-   **Universal Renaming:** All papers renamed to `YYYY-Author-ShortTitle.md` format.
-   **Metadata Sync:** Synced `authors`, `year`, and `short_title` from `Base.md` source of truth.
-   **Preprint Verification:** Checked 533 papers against Semantic Scholar; upgraded 194 from "Preprint" to published venues (NeurIPS, ACL, etc.).
-   **Deep Enrichment:** Added `key_contribution` and `significance` fields to **341** ethics-related papers.
-   **Reporting Infrastructure:** Fixed path resolution bugs in `generate_data_report.py` and `generate_paper_statistics_3.py` to support running from the root directory via `PYTHON/`.

**Learnings & Strategy:**
-   **Preprint Lag:** Only ~60% of papers marked as "Preprints" in the vault were actually still preprints. Automated checking is essential.
-   **Enrichment Placement:** Qualitative fields (`key_contribution`) should be placed **before** boolean classification tags in the YAML frontmatter for better readability.
-   **Script Paths:** When reorganizing scripts into a `PYTHON/` subdirectory, ensure internal `Path(__file__).parent` references are updated to point to the correct relative locations (e.g., `parent.parent / 'papers'`).
-   **ACL Integration:** The ACL Anthology is a high-value source for filling missing abstracts and BibTeX data for NLP papers.

**Status:**
-   Vault is fully standardized.
-   All statistical reports are up-to-date.

### 22. PDF Text Extraction Upgrade (Jan 24, 2026)

**Problem Diagnosed:**
- PDF extraction script was saving to `PDF Extracts/*.txt` format
- Plain text files are invisible in Obsidian's file explorer by default
- Undermined the purpose of full-text search across the vault
- All 58 existing extracts were created but hidden from users

**Solution Implemented:**
- Updated extraction script to save as `.md` format instead of `.txt`
- Added markdown frontmatter with extraction metadata
- Wrapped PDF content in proper markdown code blocks
- Migrated all 56 existing .txt files to .md format
- Updated all 56 paper metadata entries with new paths

**Changes Made:**
1. **Script Updates:**
   - `.agent/skills/extract_pdf_text/scripts/extract.py` - Modified to save as `.md`
   - `.agent/skills/extract_pdf_text/scripts/migrate_txt_to_md.py` - NEW migration utility

2. **File Structure (PDF Extracts):**
   ```markdown
   ---
   title: "Paper Title - PDF Extract"
   source_pdf: "YYYY-Author-Title.pdf"
   pages: 15
   extracted_at: "2026-01-24T15:30:00..."
   ---

   # PDF Extract: Paper Title

   **Source PDF:** YYYY-Author-Title.pdf
   **Total Pages:** 15

   ---

   ## Content

   ```
   [Full extracted text]
   ```
   ```

3. **Metadata Field:**
   - Added `pdf_extract` field to paper frontmatter
   - Points to: `PDF Extracts/YYYY-Author-Title.md`
   - Updated 56 paper files automatically

4. **Documentation Created:**
   - `docs/PDF_EXTRACTION_UPGRADE.md` - Overview and rationale
   - `.agent/skills/extract_pdf_text/MIGRATION_GUIDE.md` - Complete migration guide
   - Both provide troubleshooting and rollback procedures

**Results:**
- **All 56 files successfully migrated** (100% success rate, 0 errors)
- Extracts now **visible in Obsidian file explorer**
- Full **text search support** across all extracts
- **Proper metadata** for each extract (source, pages, timestamp)
- **Backward compatible** - no data loss

**Key Insights:**
1. **File Format Matters**: Plain text files have no Obsidian integration. Markdown enables search, linking, and discovery.
2. **Metadata is Essential**: YAML frontmatter makes extracts queryable and contextualized.
3. **Safe Migration Pattern**:
   - Dry-run mode to preview changes
   - Keep old format during conversion
   - Cleanup only after verification
   - Can rollback if needed

**Future Implications:**
- All new PDF extracts automatically save as `.md`
- No additional migration needed for future PDFs
- Extraction workflow unchanged - seamlessly integrated
- Enables future enhancements (linked excerpts, annotations, etc.)

**Related Documentation:**
- `docs/PDF_EXTRACTION_UPGRADE.md` - Complete upgrade overview
- `.agent/skills/extract_pdf_text/MIGRATION_GUIDE.md` - Migration procedures
- `.agent/skills/extract_pdf_text/scripts/extract.py` - Updated extraction script
- `.agent/skills/extract_pdf_text/scripts/migrate_txt_to_md.py` - Reusable migration tool

### 23. Author Data Completeness (Jan 2026)

**Problem Diagnosed:**
- Author metadata across 580 papers had various incompleteness issues:
  - Names in CSV format ("LastName, FirstName") incorrectly split to "LastName; FirstName"
  - Abbreviated names (e.g., "B. G. Purzycki" instead of "Benjamin Grant Purzycki")
  - Split single-word names (e.g., "Munshi; Amr A." instead of "Amr A. Munshi")
  - Missing wikilinks to `Authors/` directory
  - Edge cases: Malay names, organization names, single-word usernames

**Solution Implemented:**
A multi-stage fix process using 4 complementary scripts:

| Script | Purpose | Papers Fixed |
|--------|---------|--------------|
| `complete_author_data_fix.py` | arXiv API + CSV data fetching | 443 |
| `update_author_wikilinks.py` | Add wikilinks to paper body | 580 |
| `fix_author_names_comprehensive.py` | Recombine incorrectly split names | 119 |
| `fix_remaining_authors.py` | Manual mappings for edge cases | 26+ |

**Key Techniques:**

1. **arXiv API Author Fetching:**
   ```python
   def fetch_arxiv_authors(arxiv_id: str) -> List[str]:
       """Fetch complete author list from arXiv API"""
       query = quote(f"id:{arxiv_id}")
       url = f"http://export.arxiv.org/api/query?search_query={query}&start=0&max_results=1"
       with urllib.request.urlopen(url, timeout=5) as response:
           root = ET.fromstring(response.read())
           ns = {'atom': 'http://www.w3.org/2005/Atom'}
           authors = []
           for entry in root.findall('atom:entry', ns):
               for author_elem in entry.findall('atom:author', ns):
                   name_elem = author_elem.find('atom:name', ns)
                   if name_elem is not None:
                       authors.append(name_elem.text.strip())
           return authors
   ```

2. **CSV Format Conversion:**
   ```python
   def convert_csv_to_proper_format(csv_authors: str) -> List[str]:
       """Convert "LastName, FirstName" to "FirstName LastName" format"""
       author_parts = csv_authors.split(';')
       proper_names = []
       for part in author_parts:
           if ',' in part:
               parts = [p.strip() for p in part.split(',', 1)]
               if len(parts) == 2:
                   lastname, firstname = parts
                   proper_names.append(f"{firstname} {lastname}")
       return proper_names
   ```

3. **Name Recombination (for split names):**
   ```python
   def recombine_split_authors(authors_str: str) -> List[str]:
       """Recombine 'Munshi; Amr A.' into 'Amr A. Munshi'"""
       parts = [p.strip() for p in authors_str.split(';') if p.strip()]
       recombined = []
       i = 0
       while i < len(parts):
           current = parts[i]
           if ' ' not in current and i + 1 < len(parts):
               # Single word followed by first name
               next_part = parts[i + 1]
               recombined.append(f"{next_part} {current}")
               i += 2
           else:
               recombined.append(current)
               i += 1
       return recombined
   ```

4. **Manual Mappings for Edge Cases:**
   ```python
   MANUAL_AUTHOR_FIXES = {
       # Malay name format
       "2025-Zaim Bin Ahmad-Large-scale moral machine experiment.md": [
           "Muhammad Shahrul Zaim Bin Ahmad", "Kazuhiro Takemoto"
       ],
       # Organization names
       "2024-MLCommons-MLCommons AILuminate Benchmark.md": ["MLCommons"],
       # Single-name usernames
       "2023-TheDevastator-HelpSteer A-i Alignment Dataset.md": ["TheDevastator"],
       # Single-name researchers
       "2024-Aakanksha-The Multilingual Alignment Prism.md": [
           "Aakanksha", "Arash Ahmadian", "Beyza Ermis", ...
       ],
   }
   ```

**Results:**
- **100% completion rate**: All 580 papers have complete author names
- **4,918+ wikilinks** added to paper bodies
- **0 validation errors** using `yaml_frontmatter_utils.py`

**Key Learnings:**

1. **Name Format Priority:**
   - arXiv API returns cleanest names (use when available)
   - CSV data requires format conversion ("LastName, FirstName" → "FirstName LastName")
   - Manual mapping needed for edge cases (~5% of papers)

2. **Common Edge Cases:**
   - **Malay Names**: "Zaim Bin Ahmad" is a single name, not "Zaim" + "Bin Ahmad"
   - **Single Names**: Some researchers use one name (e.g., "Aakanksha")
   - **Organizations**: "MLCommons", "NIST", "Lakera AI"
   - **Usernames**: Kaggle/GitHub handles like "TheDevastator"
   - **Accented Characters**: "Hal Daumé III", "Raúl Cabeza", "Félix B. A. Flores"

3. **Wikilink Format:**
   ```markdown
   ## Authors

   [[FirstName LastName]], [[Another Author]], [[Third Author]]
   ```

4. **Validation Strategy:**
   - Check for multi-word names (most authors have first + last)
   - Flag single-word entries for manual review
   - Use arXiv as source of truth when available

**Related Scripts:**
- `PYTHON/complete_author_data_fix.py` - Main fix script (arXiv + CSV)
- `PYTHON/update_author_wikilinks.py` - Wikilink generation
- `PYTHON/fix_author_names_comprehensive.py` - Name recombination
- `PYTHON/fix_remaining_authors.py` - Manual edge case fixes

**Related Documentation:**
- `docs/AUTHOR_DATA_MANAGEMENT.md` - Complete author management guide
- `.agent/skills/fix_authors/SKILL.md` - Author fix skill
- `.claude/skills/fix-authors.md` - Claude Code skill

**Future Recommendations:**
1. Run author validation after any bulk import
2. Check arXiv first for preprints before using CSV data
3. Maintain `MANUAL_AUTHOR_FIXES` dict for new edge cases
4. Always use `yaml_frontmatter_utils.py` for YAML operations

### 24. Vault Status Summary (Jan 24, 2026)

**Current State:** Production-ready, fully operational

| Component | Count | Status |
|-----------|-------|--------|
| Total papers | 580 | ✅ Complete |
| PDFs available | 396 (68%) | ✅ Indexed |
| PDF extracts | 396 (100% of PDFs) | ✅ Searchable |
| Papers with abstracts | 454 (78%) | ✅ Enriched |
| Benchmarks | 231 (40%) | ✅ Classified |
| Evaluations | 350 (60%) | ✅ Classified |
| Datasets | 273 (47%) | ✅ Classified |
| Author profiles | 2,766+ | ✅ Created |
| YAML validity | 580/580 (100%) | ✅ Validated |

**Known Limitations:**
- ~~38 papers have abbreviated author lists (`others`)~~ **RESOLVED** (Jan 24, 2026) - see `AUTHOR_LOOKUP_RESEARCH_TASKS.md`
- ~~80 papers had corrupted abstracts (quantum physics text)~~ **RESOLVED** (Jan 24, 2026) - see `PYTHON/fix_corrupted_abstracts.py`
- 184 papers lack local PDFs (paywalled or unavailable)
- 126 papers missing abstracts (no accessible source)

### 25. PDF Extraction System (Final State)

**Location:** `.agent/skills/extract_pdf_text/scripts/extract.py`

**Key Design Decisions:**
1. **Output Format:** Markdown (`.md`) not plain text (`.txt`)
   - Reason: Plain text files are invisible in Obsidian's file explorer
   - Solution: Save as `.md` with YAML frontmatter for full Obsidian integration

2. **Extract Structure:**
   ```markdown
   ---
   title: "Paper Title - PDF Extract"
   source_pdf: "YYYY-Author-Title.pdf"
   pages: 15
   extracted_at: "2026-01-24T15:30:00..."
   ---

   # PDF Extract: Paper Title

   **Source PDF:** YYYY-Author-Title.pdf
   **Total Pages:** 15

   ---

   ## Content

   ```
   [Full extracted text with page markers]
   ```
   ```

3. **Metadata Linking:** Paper files include `pdf_extract: "PDF Extracts/filename.md"` field

**Usage:**
```bash
# Extract all PDFs
python3 .agent/skills/extract_pdf_text/scripts/extract.py --verbose

# Extract specific PDF
python3 .agent/skills/extract_pdf_text/scripts/extract.py "2024-Author-Title"

# Preview (dry-run)
python3 .agent/skills/extract_pdf_text/scripts/extract.py --dry-run
```

### 26. Common Maintenance Tasks

**Daily/Weekly Operations:**

| Task | Command | Frequency |
|------|---------|-----------|
| Validate YAML | `python3 PYTHON/validate_all_papers.py` | After bulk changes |
| Regenerate reports | `python3 PYTHON/generate_stats.py` (run all 4) | After classification |
| Extract new PDFs | `python3 .agent/skills/extract_pdf_text/scripts/extract.py` | After adding PDFs |
| Check preprint status | `python3 PYTHON/check_publication_status.py` | Weekly |

**Slash Commands (Claude Code):**
- `/vault-stats` - Quick overview
- `/classify-papers` - Run classification pipeline
- `/generate-reports` - Generate all statistics
- `/extract-pdf-text` - Extract text from PDFs
- `/fix-authors` - Fix incomplete author names

### 27. Critical Files for New Sessions

**Must-Read for Context:**
1. `CLAUDE.md` - Primary instructions and commands
2. `LLM_CONTEXT.md` - This file (classification logic, learnings)
3. `YAML_SAFEGUARDS.md` - YAML rules (prevents data corruption)

**Quick Status Check:**
1. `docs/ENRICHMENT_FINAL_REPORT.md` - Current vault status
2. `AUTHOR_LOOKUP_RESEARCH_TASKS.md` - Incomplete author lists

**Key Utilities:**
1. `PYTHON/yaml_frontmatter_utils.py` - MANDATORY for YAML operations
2. `PYTHON/validate_all_papers.py` - Validate YAML integrity
3. `.agent/skills/extract_pdf_text/scripts/extract.py` - PDF extraction

### 28. Session Handover Protocol

When starting a new session, future LLMs should:

1. **Read Core Docs:**
   ```
   CLAUDE.md → LLM_CONTEXT.md → YAML_SAFEGUARDS.md
   ```

2. **Check Vault Status:**
   ```bash
   python3 PYTHON/validate_all_papers.py  # YAML health
   ls papers/*.md | wc -l                  # Paper count
   ls "PDF Extracts"/*.md | wc -l          # Extract count
   ```

3. **Before Any YAML Modification:**
   ```python
   from PYTHON.yaml_frontmatter_utils import extract_frontmatter, write_paper, validate_frontmatter
   # Always validate before writing
   ```

4. **After Bulk Operations:**
   - Run YAML validation
   - Regenerate statistics reports
   - Update relevant documentation

### 29. Author Data Cleanup (January 2026)

**Issue Discovered:** Many papers had "others" placeholder in body metadata `**Authors:**` lines, creating an incomplete appearance even when frontmatter had complete author data.

**Root Cause:**
- Original import from Zotero CSV had abbreviated author lists
- Body metadata (`## Metadata` section) was generated separately from frontmatter
- The two sources weren't synchronized

**Solution Created:**
```bash
# New script: PYTHON/fix_body_authors.py
python3 PYTHON/fix_body_authors.py           # Fix all
python3 PYTHON/fix_body_authors.py --dry-run # Preview changes
python3 PYTHON/fix_body_authors.py --file "paper.md" # Single file
```

**What the Script Does:**
1. Reads the `authors:` field from frontmatter
2. Formats names as "LastName, FirstName" for body display
3. Updates the `**Authors:**` line in the body to match
4. Uses safe YAML utilities for all operations

**Results (This Session):**
- 53 papers updated (body authors now match frontmatter)
- 3 papers had frontmatter manually updated with complete author lists
- 0 papers now have "others" placeholder in body

**Papers Manually Researched:**
| Paper | Source | Authors Added |
|-------|--------|---------------|
| 2016-Purzycki-Religious Belief | Nature/Web | 9 authors (Purzycki, Apicella, Atkinson, Cohen, McNamara, Willard, Xygalatas, Norenzayan, Henrich) |
| 2023-Li-BIRD | arXiv/BIRD-bench | 17 authors (Li, Hui, Qu, Yang, etc.) |
| 2025-Okamoto-AI-based medical ethics | PubMed/BMC | 4 authors (Okamoto, Kataoka, Itano, Sawai) - also renamed file |

**Research Strategy for Missing Authors:**
1. Search arXiv API first (most reliable for CS papers)
2. CrossRef API for DOI-based lookups
3. Google Scholar for complete author lists
4. Semantic Scholar for affiliations and citation data
5. Manual research for edge cases (Korean venues, conference papers)

**Key Learning:**
The "others" issue was largely cosmetic - most papers already had complete frontmatter authors. The body metadata section is display-only and should be kept synchronized with frontmatter using automated scripts.

### 30. Wrong Abstracts Issue (January 2026)

**Observation:** Several papers have a generic quantum teleportation abstract instead of their actual abstract:
```
"An unknown quantum state |φ〉 can be disassembled into..."
```

This appears to be a Zotero import artifact - the quantum teleportation paper's abstract was incorrectly applied to multiple records.

**Affected Papers (Partial List):**
- 2016-Purzycki-Religious Belief (now has correct abstract via user edit)
- 2023-Li-BIRD
- 2023-Kim-KOME
- 2025-Unknown papers

**Resolution Strategy:**
- Fetch correct abstracts via arXiv API or Semantic Scholar
- Use existing `fetch_abstracts.py` script
- Alternatively, extract from PDF extracts using `/summarize-paper`

**Future Prevention:**
- Validate abstract content matches paper topic during import
- Flag abstracts with physics/quantum mechanics terms in non-physics papers

### 31. Pre-commit Hooks for YAML Validation (January 24, 2026)

**Infrastructure Created:**
A git pre-commit hook system to prevent YAML frontmatter corruption before it enters the repository.

**Components:**

| File | Purpose |
|------|---------|
| `.githooks/pre-commit` | Git hook script that runs validation on staged files |
| `.githooks/README.md` | Setup instructions for developers |
| `PYTHON/validate_yaml_hook.py` | Validation script called by the hook |

**Setup (one-time):**
```bash
git config core.hooksPath .githooks
```

**How It Works:**
1. Developer stages paper files for commit
2. Pre-commit hook triggers automatically
3. `validate_yaml_hook.py --staged-only` runs on staged `.md` files in `papers/`
4. Hook validates each file using `yaml_frontmatter_utils.py`
5. If validation fails, commit is aborted with detailed error messages
6. Developer fixes issues and retries

**Manual Validation:**
```bash
# Validate all papers
python3 PYTHON/validate_yaml_hook.py

# Validate specific files
python3 PYTHON/validate_yaml_hook.py papers/2024-Author-Title.md

# Validate only staged files (what the hook does)
python3 PYTHON/validate_yaml_hook.py --staged-only
```

**Bypass (not recommended):**
```bash
git commit --no-verify
```

**Key Benefits:**
- Prevents corrupted YAML from being committed
- Catches issues early in the development workflow
- Uses existing `yaml_frontmatter_utils.py` for consistency
- Zero overhead when no paper files are being modified

### 32. Script Migration to Safe YAML Utilities (January 24, 2026)

**Status:** All 10 classification scripts now use `yaml_frontmatter_utils.py`

**Scripts Updated:**

| Script | Purpose | Migration Date |
|--------|---------|----------------|
| `classify_ethics.py` | Base ethics classification | Jan 24, 2026 |
| `classify_ethics_perspective.py` | Ethics perspective refinement | Jan 24, 2026 |
| `classify_non_ethics_topics.py` | Non-ethics topic classification | Jan 24, 2026 |
| `classify_cultural_religious.py` | Cultural/religious value detection | Jan 24, 2026 |
| `classify_moral_psych.py` | Moral psychology classification | Jan 24, 2026 |
| `classify_data_nature.py` | Benchmark/eval/dataset classification | Jan 24, 2026 |
| `enrich_acl_papers.py` | ACL paper enrichment | Jan 24, 2026 |
| `fetch_abstracts.py` | Abstract fetching from arXiv | Jan 24, 2026 |
| `resolve_unknowns.py` | Unknown field resolution | Jan 24, 2026 |
| `update_authors.py` | Author metadata updates | Jan 24, 2026 |

**Migration Pattern Applied:**
```python
# Added to each script:
from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter

def process_paper(filepath: Path):
    # Read using safe utility
    frontmatter, body = read_paper(filepath)

    # ... classification logic ...

    # Validate before writing
    is_valid, issues = validate_frontmatter(new_frontmatter)
    if not is_valid:
        print(f"Warning: {filepath.name}: {issues}")

    # Write using safe utility with validation
    write_paper(filepath, new_frontmatter, body, validate=True)
```

**Previous Issues Prevented:**
- Orphaned list items (`  - tag` without parent key)
- Missing newlines in YAML closing markers
- Malformed YAML structure from regex manipulation

**Result:** All scripts now follow the safe YAML pattern, eliminating the risk of frontmatter corruption during batch processing

### 27. Author Lookup Research Completion (Jan 24, 2026)

**Task:** Complete the manual research for 31 papers with abbreviated author lists ("others" placeholders).

**Status:** ✅ **COMPLETE**

**Problem Background:**
- 39 papers originally had abbreviated author lists (e.g., "Kim; others")
- 8 papers were previously fixed via arXiv/CrossRef APIs
- 31 papers remained requiring manual web research

**Session Accomplishments:**

| Paper | Authors Researched | Method |
|-------|-------------------|--------|
| 2023-Kim-KOME | Jaehong Kim, Chaeyoon Jeong, Seongchan Park, Meeyoung Cha, Wonjae Lee | KAIST Social Computing Lab research |
| 2023-Alyemny-FatwaSet | Ohoud Alyemny, Hend Al-Khalifa, Abdulrahman Mirza | MDPI publication lookup |
| 2023-Ji-Safety Gymnasium | Fixed Authors section (10 authors already in frontmatter) | Body sync |
| 2016-Purzycki | 9 authors verified from Nature Scientific Data | CrossRef lookup |

**Key Finding:** Most papers on the list actually had **complete author data in YAML frontmatter** - the issue was primarily in the **body display** showing "others". The `fix_body_authors.py` script resolved 53 papers by syncing body `**Authors:**` lines with frontmatter data.

**Scripts Used:**
```bash
# Fix body author lines (syncs with frontmatter)
python3 PYTHON/fix_body_authors.py

# Dry run preview
python3 PYTHON/fix_body_authors.py --dry-run
```

**Research Strategy for Author Lookup:**
1. **Web Search:** `"[Paper Title]" [Year] all authors` or `"[Paper Title]" [Conference/Journal] authors`
2. **arXiv:** If preprint, check arXiv API for complete author list
3. **Conference Proceedings:** ACL Anthology, NeurIPS, ICML proceedings have full author lists
4. **Lab Websites:** Research group pages often list papers with all authors
5. **Related Work:** Later papers by same team often reference earlier work with full citation

**Documentation Updated:**
- `AUTHOR_LOOKUP_RESEARCH_TASKS.md` - Status: ✅ Complete

### 28. Corrupted Abstracts Issue - ✅ RESOLVED (Jan 24, 2026)

**Problem:** 84 papers had frontmatter abstracts containing unrelated quantum physics text:
> "An unknown quantum state...Einstein-Podolsky-Rosen (EPR) correlations..."

This occurred during a previous Zotero import where abstracts were misassigned.

**Resolution Summary:**

| Method | Papers Fixed |
|--------|-------------|
| Body `## Abstract` extraction | 55 |
| Manual web research | 23 |
| Semantic Scholar API | 1 |
| Early session (manual) | 4 |
| Quote escaping fix | 1 |
| **Total** | **84** |

**Detection (Verification):**
```bash
grep -l "Einstein-Podolsky-Rosen" papers/*.md | wc -l  # Returns 0
```

**Scripts Created:**

1. `PYTHON/fix_corrupted_abstracts.py` - Automated fix script
   - Strategy 1: Extract correct abstract from body `## Abstract` section
   - Strategy 2: Fetch from arXiv API using paper's arxiv ID
   - Strategy 3: Fetch from Semantic Scholar API using DOI

2. `PYTHON/fix_abstracts_batch.py` - Manual batch fix script
   - Contains `CORRECT_ABSTRACTS` dictionary with researched abstracts
   - Used for papers without API-accessible sources
   - Properly escapes quotes in abstracts

**Documentation:**
- `ABSTRACT_CORRUPTION_FIX.md` - Complete resolution record

**Status:** ✅ **COMPLETE** - All 84 corrupted abstracts fixed

### Future Session Checklist

When resuming work on this vault:

1. **Check vault health:**
   ```bash
   # YAML validation (should be 580 valid, 0 errors)
   python3 PYTHON/validate_all_papers.py

   # Corrupted abstracts check (should return 0)
   grep -l "Einstein-Podolsky-Rosen" papers/*.md | wc -l

   # Paper count
   ls papers/*.md | wc -l  # Should be 580
   ```

2. **Key documentation to read:**
   - `CLAUDE.md` - Primary instructions and commands
   - `LLM_CONTEXT.md` - This file (classification logic, learnings)
   - `YAML_SAFEGUARDS.md` - YAML writing rules (CRITICAL)

3. **Before modifying papers:**
   - Always use `yaml_frontmatter_utils.py`
   - Run validation after batch changes
   - Use `--dry-run` flags when available

4. **Current vault status (Jan 24, 2026):**
   - Papers: 580 ✅
   - YAML validity: 100% ✅
   - Abstracts: 580/580 (100%) ✅
   - Corrupted abstracts: 0 ✅
   - PDF extracts: 396 (68%) ✅
   - Author profiles: 2,766+ ✅

---

## 31. Abstract Fetching - API Comparison (Session 3, Jan 2026)

### API Effectiveness for This Vault

| API | Success Rate | Notes |
|-----|--------------|-------|
| **OpenAlex** | ~85% | Best overall - uses inverted index for abstracts |
| **CrossRef** | ~1% | DOI matching works but few abstracts available |
| **Semantic Scholar** | 0% | Failed completely for this vault |
| **arXiv** | ~5% | Only for papers with arXiv IDs |

### Key Technical Learnings

**1. OpenAlex API**
- URL: `https://api.openalex.org/works/{doi}` or title search
- Abstracts stored as "inverted index" - need reconstruction:
```python
abstract_inverted = work.get('abstract_inverted_index', {})
words = []
for word, positions in abstract_inverted.items():
    for pos in positions:
        words.append((pos, word))
words.sort(key=lambda x: x[0])
abstract = ' '.join(word for _, word in words)
```

**2. Body Content Extraction**
- Many papers had abstracts in `## Abstract` section but not in YAML
- Regex: `r'##\s*Abstract\s*\n+(.+?)(?=\n##|\n\*\*|\Z)'`
- Skip placeholders: "No abstract available"
- Minimum length check: 50 chars

**3. DOI Validation**
- Skip placeholder DOIs: `'xxxxx' in doi.lower()`
- Validate format: `r'^10\.\d+/.+'`

### Script Created

`PYTHON/fetch_missing_abstracts.py` - Multi-source fetcher:
1. Check body content first (free, fast)
2. Try arXiv API (for papers with arXiv IDs)
3. Try CrossRef API (for papers with DOIs)
4. Try OpenAlex API (title-based search fallback)

### Results

- **Before:** 454/580 papers (78%) had abstracts
- **After:** 580/580 papers (100%) have abstracts
- Method breakdown: OpenAlex ~100, body extraction 9, manual 4, CrossRef 1

---

## 32. Author Data Patterns (Session 3, Jan 2026)

### Common Issues Found

1. **Parsing errors in paper names**: "2025-De Montis" was actually "2025-Bombaerts"
2. **Team/organization as author**: "Letta Team" → Charles Packer, Sarah Wooders
3. **Incomplete lists**: Body showed "et al." but frontmatter had full list

### Verification Commands

```bash
# Check for incomplete author fields
grep -E "^authors:.*et al|^authors:.*others" papers/*.md

# Check body author lines
grep -E "^\*\*Authors:\*\*.*et al" papers/*.md
```

### Status: ✅ Complete

All 580 papers now have complete author data in both frontmatter and body.

---

## 33. Corrupted Abstracts Resolution (Session 5, Jan 24, 2026)

### Problem Background

84 papers had their frontmatter `abstract:` field corrupted with quantum physics text from Bennett et al. (1993) - a paper on quantum teleportation. This occurred during a Zotero batch import.

### Fix Approach

A multi-pronged approach was used:

1. **Body Extraction (55 papers)**: Many papers had correct abstracts in the `## Abstract` section of the body, which were extracted and placed in frontmatter.

2. **Manual Web Research (23 papers)**: For papers without body abstracts or API access:
   - Searched paper titles on Google/Google Scholar
   - Checked official project websites (MLCommons, NIST, Lakera, etc.)
   - Accessed publisher pages (MDPI, NeurIPS, OpenReview)
   - Verified against arXiv when available

3. **Semantic Scholar API (1 paper)**: DOI-based lookup for papers with accessible abstracts.

4. **Quote Escaping (1 paper - RusCode)**: Required special handling for abstracts containing quotes.

### Scripts Created

**`PYTHON/fix_corrupted_abstracts.py`**
- Automated detection using "Einstein-Podolsky-Rosen" pattern
- Three-stage fix: body extraction → arXiv API → Semantic Scholar API
- Rate limiting: 0.3s for arXiv, 0.5s for Semantic Scholar
- Generates report file with remaining unfixed papers

**`PYTHON/fix_abstracts_batch.py`**
- Manual batch fix script with `CORRECT_ABSTRACTS` dictionary
- Contains 15+ manually researched abstracts
- Properly escapes quotes in abstract text
- Uses safe YAML utilities for writing

### Key Learnings

1. **Body Content Priority**: ~65% of papers had correct abstracts in body but not frontmatter. Always check body first.

2. **Web Research Strategy**:
   - Project/benchmark websites often have better descriptions than papers
   - Conference proceedings (NeurIPS, ACL) have reliable abstracts
   - Kaggle dataset pages include descriptions
   - EA Forum posts for non-academic works

3. **Quote Escaping**: Abstracts containing double quotes must use `\"` escaping in YAML.

4. **API Limitations**:
   - Semantic Scholar failed for most papers in this vault
   - arXiv only works for papers with explicit arXiv IDs
   - OpenAlex is better for title-based searches

### Verification

```bash
# Verify no corrupted abstracts remain
grep -l "Einstein-Podolsky-Rosen" papers/*.md | wc -l  # Returns 0

# Run detection script
python3 PYTHON/fix_corrupted_abstracts.py  # Reports 0 corrupted
```

### Documentation

- `ABSTRACT_CORRUPTION_FIX.md` - Complete resolution record with timeline
- `corrupted_abstracts_report.txt` - Generated verification report

### Status

✅ **COMPLETE** - All 84 corrupted abstracts fixed. Vault abstract coverage: 100%.

---

## 34. Session 5 Summary (Jan 24, 2026)

### Tasks Completed

| Task | Result |
|------|--------|
| YAML Validation | 580/580 papers valid (100%) |
| Corrupted Abstracts | 84/84 fixed (was 23 remaining, now 0) |
| Documentation Updates | LLM_CONTEXT.md, ABSTRACT_CORRUPTION_FIX.md updated |

### New Scripts Created

- `PYTHON/fix_abstracts_batch.py` - Batch abstract fix with manual data

### Files Modified

- `LLM_CONTEXT.md` - Added sections 33-34
- `ABSTRACT_CORRUPTION_FIX.md` - Updated to ✅ RESOLVED status
- 84 paper files - Corrected abstracts

### Vault Health Status

| Metric | Value | Status |
|--------|-------|--------|
| Total Papers | 580 | ✅ |
| YAML Valid | 580 (100%) | ✅ |
| Abstracts | 580 (100%) | ✅ |
| Corrupted Abstracts | 0 | ✅ |
| PDF Extracts | 396 (68%) | ✅ |
| Author Profiles | 2,766+ | ✅ |

### Next Steps for Future Sessions

1. **No urgent issues** - Vault is in healthy production state
2. **Potential improvements**:
   - PDF extraction for remaining 184 papers (if PDFs become available)
   - Abstract quality review (some may be brief/placeholder)
   - Author profile enrichment (continuing residual batches)

### Session Handover Notes

The vault is production-ready. All critical data quality issues have been resolved:
- ✅ YAML frontmatter validated and standardized
- ✅ Corrupted abstracts fixed
- ✅ Author data complete
- ✅ Classification scripts using safe YAML utilities
- ✅ Pre-commit hooks available for YAML validation

---

## 35. PDF Download & Extraction Session (Jan 24, 2026 - Evening)

### Tasks Completed

| Task | Result |
|------|--------|
| PDF Downloads | 26 new (396 → 422, 72.8% coverage) |
| PDF Extracts | 422 created (100% of available PDFs) |
| Script Fixes | `smart_pdf_downloader.py` corrected |
| ArXiv Discovery | 8 papers got working PDF links |

### Key Technical Learnings

1. **YAML Field Names in Paper Metadata**
   - Online PDF URLs are in `external_pdf` field, NOT `pdf`
   - Local PDF paths use wikilink format: `local_pdf: "[[Lit-WS-PDFs/name.pdf]]"`
   - Must strip brackets when checking file existence

2. **PDF Download Script Fix**
   ```python
   # WRONG - old code looked for 'pdf' field
   pdf_url = self.extract_field(fm, 'pdf')  # Returns None!

   # CORRECT - need to check 'external_pdf' first
   def get_pdf_url(self, frontmatter: str) -> Optional[str]:
       url = self.extract_field(frontmatter, 'external_pdf')
       if url:
           return url
       return self.extract_field(frontmatter, 'pdf')
   ```

3. **Wikilink Format Handling**
   ```python
   # local_pdf field contains: "[[Lit-WS-PDFs/2024-Author-Title.pdf]]"
   local_pdf_clean = local_pdf.strip('[]').replace('[[', '').replace(']]', '')
   local_path = REPO_ROOT / local_pdf_clean
   ```

4. **ArXiv Fallback for ACL Papers**
   - Many ACL Anthology URLs return HTML, not PDF
   - Solution: Search arXiv API by title to find preprint version
   - ArXiv PDFs are direct downloads: `https://arxiv.org/pdf/{id}.pdf`
   - Success rate: 8/9 papers found on arXiv

5. **Remaining PDF Barriers**
   - 126 Zotero URLs: Semantic Scholar finds ~12% alternatives
   - 26 missing links: Need manual research
   - ~6 paywalled: No open access version exists

### Files Modified

| File | Change |
|------|--------|
| `PYTHON/smart_pdf_downloader.py` | Fixed field names, added wikilink handling |
| `PDF_PROJECT_COMPLETION_REPORT.md` | Updated to 422 PDFs (72.8%) |
| `PDF_DOWNLOAD_SESSION_REPORT.md` | NEW - Session report |
| `CLAUDE.md` | Updated vault status |
| `SESSION_HANDOVER.md` | Added Session 4 summary |
| 26 paper files | Added `local_pdf` field |
| 422 extract files | Created in `PDF Extracts/` |

### Vault Status After Session

| Metric | Value | Status |
|--------|-------|--------|
| Total Papers | 580 | ✅ |
| PDFs Available | 422 (72.8%) | ✅ |
| PDF Extracts | 422 (100% of PDFs) | ✅ |
| Abstracts | 580 (100%) | ✅ |
| YAML Valid | 580 (100%) | ✅ |

### Next Steps for Future Sessions

1. **Zotero URL Research** (126 papers)
   - Run `python3 PYTHON/smart_pdf_downloader.py --fix-zotero` periodically
   - Semantic Scholar finds ~6 per batch of 50

2. **Missing Link Research** (26 papers)
   - Search arXiv, Google Scholar, author websites
   - Check for preprint versions

3. **PDF Coverage Goal**
   - Current: 72.8%
   - Target: 80%+ (need ~42 more PDFs)

---

## 34. Session 5 Verification & Learnings (Jan 24, 2026)

### Verification Status

All previously identified issues have been confirmed as resolved:

| Issue | Detection | Result |
|-------|-----------|--------|
| Incomplete author placeholders | `grep -l "\*\*Authors:\*\*.*and others" papers/*.md` | **0 files** ✅ |
| Corrupted abstracts (quantum physics) | `grep -l "Einstein-Podolsky-Rosen" papers/*.md` | **0 files** ✅ |
| YAML validation | `python3 PYTHON/validate_all_papers.py` | **580/580 valid** ✅ |

### Critical Learning: False Positives in Grep

**Problem:** Running `grep -l "others" papers/*.md` returns **39 files**, which appears to indicate 39 papers with incomplete author data. This is misleading.

**Reality:** These matches are legitimate content, NOT author placeholders:

| Match Location | Example |
|----------------|---------|
| Abstracts | "...violating a particular moral foundation and not others" |
| `external_pdf` field | Zotero exports as "Kim and others - 2023 - KOME.pdf" |
| Body content | "...for others to analyze and learn from" |
| `key_contribution` | "...isolates gender to specific dimensions while neutralizing it in others" |

**Correct Verification Pattern:**
```bash
# CORRECT - Check for incomplete author body lines (should return 0)
grep -l "\*\*Authors:\*\*.*and others" papers/*.md | wc -l

# WRONG - Returns false positives from abstracts, content, etc.
grep -l "others" papers/*.md | wc -l  # Returns 39 (false positives!)
```

### Updated Statistics

| Component | Count | Notes |
|-----------|-------|-------|
| Papers | 580 | Complete |
| PDFs | 422 | 72.8% coverage |
| PDF Extracts | 422 | All PDFs extracted |
| Abstracts | 580 | 100% complete |
| Author Profiles | 3,006 | All created |
| YAML Validity | 580/580 | 100% |

### Session Handover Checklist

For future sessions starting work on this vault:

1. **Run verification checks:**
   ```bash
   # All should return 0 or pass
   grep -l "\*\*Authors:\*\*.*and others" papers/*.md | wc -l
   grep -l "Einstein-Podolsky-Rosen" papers/*.md | wc -l
   python3 PYTHON/validate_all_papers.py
   ```

2. **Read core documentation:**
   - `CLAUDE.md` - Commands and primary instructions
   - `LLM_CONTEXT.md` - This file (detailed learnings)
   - `YAML_SAFEGUARDS.md` - Critical YAML rules

3. **Before modifying YAML:**
   ```python
   from PYTHON.yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter
   ```

### Research Sources by Priority

When looking up paper metadata:

1. **arXiv** - Best for preprints, complete author lists, abstracts
2. **ACL Anthology** - NLP papers with full metadata
3. **Semantic Scholar** - DOI-based lookup, publication status
4. **Conference Proceedings** - NeurIPS, ICML, ACL official records
5. **Lab/University Pages** - Research group publication lists
6. **OpenAlex** - Abstracts (via inverted index format)

---

## 36. Session 5 Verification (Jan 24, 2026)

### Purpose

Follow-up verification session to confirm all data quality fixes from previous sessions were complete.

### Verification Results

All checks passed:

| Check | Command | Result |
|-------|---------|--------|
| Corrupted abstracts | `grep -l "Einstein-Podolsky-Rosen" papers/*.md \| wc -l` | 0 |
| YAML validation | `python3 PYTHON/validate_all_papers.py` | 580/580 valid |
| Author placeholders | `grep -l "\*\*Authors:\*\*.*and others" papers/*.md \| wc -l` | 0 |

### Confirmation

The vault is production-ready with no known data quality issues:
- ✅ All 580 papers have valid YAML frontmatter
- ✅ All abstracts are correct (no quantum physics corruption)
- ✅ All author data is complete (no "and others" placeholders)
- ✅ 422 PDFs extracted and searchable in Obsidian

---

## 37. Comprehensive Paper Audit & Cleanup (Jan 24, 2026 - Session 6)

### Purpose

Complete audit and cleanup of all paper entries to find and fix:
- Errors, broken links, missing information
- Duplicate papers and redundant information
- Inconsistent formatting and data quality issues

### Results Summary

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Total Papers | 580 | 576 | -4 (duplicates removed) |
| Errors | 0 | 0 | - |
| Warnings | 1,753 | 770 | **-983 (-56%)** |
| YAML Valid | 100% | 100% | ✅ |

### Issues Fixed

| Issue Type | Count | Script Used |
|------------|-------|-------------|
| Duplicate papers removed | 4 | Manual removal |
| Duplicate citation entries | 246 | `smart_citation_cleanup.py` |
| Body abstract placeholders | 53 | `comprehensive_cleanup.py` |
| local_pdf format fixed | 26 | `comprehensive_cleanup.py` |
| N/A local_pdf values removed | 22 | `enhanced_cleanup.py` |
| Type values normalized | 18 | `comprehensive_cleanup.py` |
| Ethics classification fixed | 7 | `comprehensive_cleanup.py` |
| Author wikilink formats fixed | 119 | `enhanced_cleanup.py` |
| Truncated abstracts fixed | 2 | `fix_truncated_abstracts.py` |

### Common Issues Found

#### 1. Duplicate Papers (Same DOI, Different Files)

**Problem:** Multiple files for the same paper with different naming:
- `2025-Wang-Diverse Human Value Alignment for LLMs via Ethical Reasoning.md` (full title)
- `2025-Wang-Diverse Human Value Alignment via Ethical Reasoning.md` (truncated)

**Detection:**
```python
# Group papers by DOI
papers_by_doi = defaultdict(list)
for paper in papers:
    doi = frontmatter.get('doi')
    if doi and doi != 'N/A':
        papers_by_doi[doi].append(paper)
# Find duplicates
duplicates = {k: v for k, v in papers_by_doi.items() if len(v) > 1}
```

**Resolution:** Keep the file with:
1. Complete/full title
2. More metadata fields populated
3. Correct author attribution

#### 2. Duplicate Citation Entries in Body

**Problem:** Citation info section contains redundant entries from multiple API calls:
```
792 citations (Semantic Scholar/DOI) [2025-08-27] 2 citations (Semantic Scholar/DOI) [2025-08-27] 791 citations (Semantic Scholar/DOI) [2025-08-23]
```

**Detection:**
```python
citations = re.findall(r'\d+ citations \([^)]+\) \[\d{4}-\d{2}-\d{2}\]', body)
if len(citations) > 2:  # More than reasonable number
    # Flag as potential duplicates
```

**Resolution:** Smart deduplication keeping highest count per (source, date) pair:
```python
# Parse citations into (count, source, date)
# Keep only max count for each unique (source, date)
```

#### 3. Invalid local_pdf Format

**Problem:** `local_pdf` field not in wikilink format:
```yaml
local_pdf: Lit-WS-PDFs/2020-Sap-Social Bias Frames.pdf  # Wrong
local_pdf: "[[Lit-WS-PDFs/2020-Sap-Social Bias Frames.pdf]]"  # Correct
```

**Detection:**
```python
local_pdf = frontmatter.get('local_pdf', '')
if local_pdf and not (local_pdf.startswith('[[') and local_pdf.endswith(']]')):
    # Invalid format
```

**Resolution:**
```python
new_value = f'[[Lit-WS-PDFs/{local_pdf}]]' if not local_pdf.startswith('Lit-WS-PDFs/') else f'[[{local_pdf}]]'
```

#### 4. N/A Values in Optional Fields

**Problem:** Fields like `local_pdf: N/A` instead of being empty or omitted.

**Detection:**
```python
if frontmatter.get('local_pdf') == 'N/A':
    # Should be empty, not N/A
```

**Resolution:** Remove the line entirely or set to empty string.

#### 5. Invalid Type Values

**Problem:** Non-standard type values:
```yaml
type: journal article  # Wrong (space, lowercase)
type: journalArticle   # Correct
```

**Valid type values:**
- `journalArticle`, `preprint`, `conferencePaper`, `bookSection`
- `report`, `thesis`, `book`, `webpage`, `document`, `presentation`

**Resolution:** Normalize using mapping:
```python
TYPE_MAPPING = {
    'journal article': 'journalArticle',
    'conference paper': 'conferencePaper',
    'workshop paper': 'conferencePaper',
    'book chapter': 'bookSection',
    'edited volume': 'book',
    'article': 'journalArticle',
}
```

#### 6. Ethics Classification Inconsistency

**Problem:** `ethics_overall: "No"` but `virtue_ethics: "Yes"` (contradiction)

**Detection:**
```python
if ethics_overall == 'No' and (virtue == 'Yes' or deonto == 'Yes' or util == 'Yes'):
    # Inconsistent classification
```

**Resolution:** Set `ethics_overall: "Yes"` if any specific ethics field is "Yes".

#### 7. Broken Author Wikilinks

**Problem:** Author wikilinks in wrong format:
```markdown
[[Zhao, Jieyu]]  # Wrong (LastName, FirstName format)
[[Jieyu Zhao]]   # Correct (FirstName LastName format)
```

Also nested/broken wikilinks:
```markdown
[[Jiahao [[Wang]]]]  # Broken
[[Jiahao Wang]]      # Correct
```

**Detection:**
```python
# Pattern for LastName, FirstName format
re.findall(r'\[\[([^,\]]+),\s*([^\]]+)\]\]', text)
```

**Resolution:**
```python
# Convert to FirstName LastName
new_link = f'[[{first.strip()} {last.strip()}]]'
```

#### 8. Truncated/Placeholder Abstracts

**Problem:** Abstract field contains only content warning, not actual abstract:
```yaml
abstract: "Warning: This paper contains explicit statements of offensive stereotypes and may be upsetting."
```

The actual abstract is much longer and available in the PDF.

**Detection:**
```python
if len(abstract) < 100:
    # Potentially truncated
if 'Warning:' in abstract and len(abstract) < 200:
    # Likely just content warning
```

**Resolution:** Extract full abstract from PDF extract or fetch from API.

### Scripts Created

| Script | Purpose | Usage |
|--------|---------|-------|
| `comprehensive_audit.py` | Full audit report generation | `python3 PYTHON/comprehensive_audit.py` |
| `comprehensive_cleanup.py` | Initial cleanup (phase 1) | `python3 PYTHON/comprehensive_cleanup.py` |
| `enhanced_cleanup.py` | Enhanced cleanup (phase 2) | `python3 PYTHON/enhanced_cleanup.py` |
| `smart_citation_cleanup.py` | Smart citation deduplication | `python3 PYTHON/smart_citation_cleanup.py` |
| `fix_truncated_abstracts.py` | Fix specific truncated abstracts | `python3 PYTHON/fix_truncated_abstracts.py` |

### Audit Workflow

For future comprehensive audits:

```bash
# 1. Run audit to generate report
python3 PYTHON/comprehensive_audit.py

# 2. Review report
cat STATISTICS/comprehensive-audit-report.md

# 3. Run cleanup (dry-run first)
python3 PYTHON/comprehensive_cleanup.py --dry-run
python3 PYTHON/comprehensive_cleanup.py

# 4. Run enhanced cleanup
python3 PYTHON/enhanced_cleanup.py --dry-run
python3 PYTHON/enhanced_cleanup.py

# 5. Run smart citation cleanup
python3 PYTHON/smart_citation_cleanup.py --dry-run
python3 PYTHON/smart_citation_cleanup.py

# 6. Validate all papers
python3 PYTHON/validate_all_papers.py

# 7. Re-run audit to verify
python3 PYTHON/comprehensive_audit.py
```

### Remaining Warnings (Acceptable)

| Warning Type | Count | Notes |
|--------------|-------|-------|
| Author file not found | 630 | Authors need profiles created in Authors/ |
| 3+ citation entries | 127 | Legitimate different sources/dates |
| Potentially short abstracts | 6 | Content warnings or genuinely brief papers |

These are informational, not errors requiring fixes.

### Key Learnings

1. **DOI "N/A" is not a duplicate** - Papers without DOIs all show as "N/A" in duplicate detection. These are NOT duplicates - they simply have no DOI.

2. **Similar titles ≠ duplicates** - "All Languages Matter" appears twice but they're different papers by different authors on different topics.

3. **Citation entries from different sources are valid** - A paper can have citations from Semantic Scholar AND Crossref on different dates. Only remove true duplicates (same source, same date, different counts).

4. **Content warnings are not abstracts** - Some papers (especially bias/hate speech datasets) have content warnings at the start. The actual abstract is often much longer.

5. **Type values must match Zotero format** - Use camelCase: `journalArticle`, `conferencePaper`, etc.

### Verification Checklist

After any major cleanup, run:

```bash
# YAML validation (should show all valid)
python3 PYTHON/validate_all_papers.py

# Re-run audit (should show 0 errors)
python3 PYTHON/comprehensive_audit.py

# Check for specific issues
grep -l "local_pdf: N/A" papers/*.md | wc -l  # Should be 0
grep -l "type: journal article" papers/*.md | wc -l  # Should be 0
```

---

## Section 24: Author Name Validation and Cleanup (January 2026)

### Problem Discovered

The Authors/ directory accumulated 113+ invalid entries over time:
- **Broken wikilinks in filenames**: `Chad]] [[Coleman.md`, `[[Unknown]].md`
- **Single-letter names**: `C.`, `M.`, `R.`, `Y.`, `Z.`
- **Generic placeholders**: `Center`, `Institute`, `Group`, `Team`, `Consortium`
- **Incomplete entries**: `et al.`, `H. R.`, `K. M. A.`
- **Orphaned entries**: Abbreviated names not referenced in any paper

### Root Causes

1. **No validation on author file creation** - Scripts created author files without checking if names were valid
2. **Wikilink parsing errors** - Malformed wikilinks like `[[Name1]], [[Name2]]` got split incorrectly
3. **CSV import issues** - Zotero CSV sometimes has abbreviated names that were blindly imported
4. **No cleanup of orphaned files** - After fixing paper author fields, old incorrect author files remained

### Solution: Author Validation Utility

Created `PYTHON/author_validation.py` with:

```python
from author_validation import (
    validate_author_name,      # Check if name is valid
    normalize_author_name,     # Clean up name (remove wikilinks, etc.)
    find_full_name_match,      # Find "Alice Smith" for "A. Smith"
    safe_create_author_file,   # Create file only if valid
    is_valid_author_filename,  # Check filename validity
)

# Validate before creating
is_valid, errors, warnings = validate_author_name("A. Smith")
# Returns: (True, [], ['Review needed: abbreviated'])

# Invalid names are rejected
is_valid, errors, warnings = validate_author_name("C.")
# Returns: (False, ['Invalid pattern: single_letter'], [])
```

### Invalid Patterns (Auto-Rejected)

| Pattern | Example | Reason |
|---------|---------|--------|
| `single_letter` | `C.`, `M.` | Too short, likely parse error |
| `two_initials` | `A. B.`, `H. R.` | No last name, incomplete |
| `broken_wikilink` | `Chad]] [[Coleman` | Filename corruption |
| `et_al` | `et al.` | Placeholder, not a person |
| `generic` | `Center`, `Team` | Generic words, not names |

### Warning Patterns (Flagged for Review)

| Pattern | Example | Action |
|---------|---------|--------|
| `abbreviated` | `A. Smith` | Try to expand to full name |
| `very_short` | `Li`, `Kim` | May be legitimate (Asian names) |

### Scripts Created

| Script | Purpose |
|--------|---------|
| `author_validation.py` | Validation utility - USE BEFORE CREATING AUTHORS |
| `resolve_author_issues.py` | Scan and fix Authors/ directory |
| `expand_abbreviated_authors.py` | Find full names via arXiv API |
| `cleanup_orphaned_authors.py` | Remove unused author files |

### Integration Points

The validation is now integrated into:

1. **`complete_author_data_fix.py`** - Validates when parsing author lists
2. **`parse_author_list()`** - Skips invalid names, expands abbreviated ones
3. **`/fix-authors` skill** - Documents validation requirements

### Prevention Rules

**ALWAYS do this when creating author files:**

```python
from author_validation import validate_author_name, safe_create_author_file

# Option 1: Use safe_create_author_file (recommended)
success, msg = safe_create_author_file(name)
if not success:
    print(f"Cannot create: {msg}")

# Option 2: Validate manually first
is_valid, errors, warnings = validate_author_name(name)
if not is_valid:
    print(f"Invalid name: {errors}")
    return
# Only then create the file
```

**NEVER do this:**
```python
# BAD - No validation
author_file = AUTHORS_DIR / f"{name}.md"
author_file.write_text(content)  # May create invalid file!
```

### Periodic Cleanup

Run monthly or after large imports:

```bash
# Check for issues (dry run)
python3 PYTHON/resolve_author_issues.py

# Apply fixes
python3 PYTHON/resolve_author_issues.py --execute

# Verify
cd Authors && ls -1 | grep -E '^\[\[|^\]\]|^[A-Z]\.$' | wc -l  # Should be 0
```

### Legitimate "Problematic" Entries

Some flagged entries are actually valid:

1. **Short names** (Asian surnames): `Li`, `Kim`, `Liu`, `Zhu` - Keep if referenced in papers
2. **Abbreviated first authors**: `J. Zico Kolter`, `W. Russell Neuman` - arXiv uses this form
3. **Single-name researchers**: `Aakanksha` - Some researchers use one name
4. **Anonymous**: Valid for certain dataset papers

### Key Learnings

1. **Validate at creation time** - Much easier than cleaning up later
2. **Wikilink parsing is fragile** - Always use proper regex, never string split
3. **arXiv is authoritative** - If arXiv uses abbreviated form, that's the canonical name
4. **Orphaned files accumulate** - Run cleanup after any major author data changes
5. **Asian names are often short** - `Li`, `Kim` etc. are legitimate single-word names

## 38. Session 6 Recap (Jan 24, 2026)

### Statistics Recalculation
- **Context**: The `papers/` directory is dynamic. Statistics reports in `STATISTICS/` must be manually regenerated to stay in sync.
- **Action**: Ran the full 7-stage classification pipeline followed by `run_reports.py`.
- **Outcome**: Updated all 4 reports. Total papers: 580.

### PDF Extraction Refactor (YAML Safety)
- **Problem**: The `extract.py` script was using regex to modify paper metadata, violating the vault's safe YAML policy mandated in Jan 2026.
- **Fix**: Refactored `.agent/skills/extract_pdf_text/scripts/extract.py` to use `PYTHON/yaml_frontmatter_utils.py`.
- **Key Change**: Replaced `update_markdown_metadata` regex logic with `add_field(frontmatter, 'pdf_extract', ...)` and `write_paper(..., validate=True)`.
- **Result**: Successfully extracted 51 missing PDFs without compromising metadata integrity.

### Corrupted PDF Discovery
- **File**: `Lit-WS-PDFs/2024-Pistilli-CIVICS.pdf`
- **Issue**: File size is ~22 bytes (likely an empty/placeholder file).
- **Status**: Tagged for re-download. The extraction script correctly flagged this error.

### Critical Learning for Future Agents
1. **Always Use Safe Utils**: Any script that writes to `.md` files in `papers/` MUST import and use `PYTHON/yaml_frontmatter_utils.py`. No bespoke regex editing.
2. **Extraction Pipeline**: The `extract_pdf_text` skill is now robust and safe. Use it to close the gap between `local_pdf` presence and `pdf_extract` availability.
