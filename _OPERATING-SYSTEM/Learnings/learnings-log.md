# Learnings Log
*Last updated: 2026-02-02*

---

## Category Index

| Category | Description | Jump |
|----------|-------------|------|
| Classification | Paper classification logic refinements, edge cases | [Classification](#classification) |
| YAML | Frontmatter corruption prevention, validation | [YAML](#yaml) |
| API | arXiv, Semantic Scholar integration patterns | [API](#api) |
| PDF Processing | Extraction, download, recovery workflows | [PDF](#pdf-processing) |
| Author Management | Name validation, enrichment workflows | [Author](#author-management) |
| Data Quality | Validation, audits, corruption detection | [Data](#data-quality) |
| Skills | Skill creation, improvement, automation | [Skills](#skills) |
| Workflows | Multi-step process optimization, batch operations | [Workflows](#workflows) |
| Git | GitHub integration, commit patterns | [Git](#git) |

---

## How to Add Learnings

**Automated:** Use `/remember-thread` skill at session end
**Manual:** Add entries in table format below

**Format:** `| YYYY-MM-DD | Category | Learning |`

**Guidelines:**
- Be specific and actionable (not generic)
- Include context (what triggered the learning)
- Note edge cases and exceptions
- Link to relevant Standards/ files if applicable

---

## 2026-02-02

| Date | Category | Learning |
|------|----------|----------|
| 2026-02-02 | Workflows | **Progressive Disclosure Architecture:** Created `_OPERATING-SYSTEM/` structure with 4-layer memory (learnings log, standards, skills, configs). Keeps agent configs <80 lines while maintaining detailed procedural knowledge in `Standards/`. Inspired by LifeOS-Agent-Vault. See `_OPERATING-SYSTEM/README.md`. |

---

## 2026-01-31

| Date | Category | Learning |
|------|----------|----------|
| 2026-01-31 | Workflows | **Parallel Agent Execution:** User explicitly prefers parallel agents for efficiency. Launch ALL agents in SINGLE message for maximum parallelization. Result: 8x speedup (3 hours vs 24 hours sequential) for 14 AI lab documentation downloads. 23 agents launched simultaneously - all successful. See `docs/PARALLEL_AGENT_BEST_PRACTICES.md`. |
| 2026-01-31 | PDF Processing | **PDF Download Methods:** PDFs must use `Bash curl` (WebFetch causes API errors). Web content extraction uses WebFetch to convert HTML→markdown. Model cards: WebFetch extracts from GitHub README pages. Never use WebFetch for binary PDF downloads. |
| 2026-01-31 | API | **arXiv Version Management:** Papers get updated on arXiv (v1 → v2 → v3). Examples: Llama 3 Herd v3, CyberSecEval 3 v2, SAM 2 v2. Always verify latest version with MD5 checksums. Version number appears in filename and PDF metadata. Check `https://arxiv.org/abs/{id}` for latest version. |
| 2026-01-31 | Data Quality | **Documentation Patterns by Region:** US companies (OpenAI, Anthropic, Meta) provide comprehensive arXiv papers + system cards. Chinese companies (Alibaba/Qwen, DeepSeek, Zhipu) have high velocity with mix of arXiv + blog posts. xAI provides model cards only (no technical papers). NVIDIA provides deep technical reports with implementation details. |
| 2026-01-31 | Data Quality | **Non-Existent Resources:** Early model technical reports often don't exist (GPT-3.5, GPT-4 Turbo, Phi-2). Incremental updates rarely documented (Llama 3.3, Yi-1.5). API-only releases have no papers (ERNIE 5.0, MAI-1). Document these absences with explanations to prevent repeated searches. |

---

## 2026-01-24

| Date | Category | Learning |
|------|----------|----------|
| 2026-01-24 | YAML | **YAML Corruption Prevention System:** Created comprehensive safety system after discovering 530+ papers with corrupted frontmatter. Three-part system: (1) `yaml_frontmatter_utils.py` library (mandatory for all YAML ops), (2) `YAML_SAFEGUARDS.md` (technical reference), (3) `DEVELOPER_PLAYBOOK.md` (how-to guide). See `Standards/yaml-standards.md`. |
| 2026-01-24 | YAML | **Orphaned List Items:** Most common corruption pattern is orphaned `  - "#Tag"` without parent key. Caused by string concatenation of YAML. Fix: Always use `write_paper()` function which rebuilds frontmatter from dict. Validation detects orphaned items via regex `^\s*-\s+` without preceding parent key. |
| 2026-01-24 | YAML | **Closing Marker Format:** YAML closing marker MUST be `\n---\n` (newlines before AND after). Wrong: `{fm}---` or `{fm}\n---`. This breaks YAML parsing in Obsidian. All 530 papers had missing newline before closing marker. Fixed via `rebuild_frontmatter()`. |
| 2026-01-24 | YAML | **Field Format Consistency:** `newtags` is a STRING (comma-separated), NOT a YAML list. Wrong: `newtags:\n  - Tag`. Right: `newtags: "Tag1, Tag2"`. This field aggregates classification tags. Using list format breaks parsing and creates orphaned items when tags are updated. |
| 2026-01-24 | Data Quality | **Corrupted Abstracts Fix:** 80 papers had abstracts replaced with "Einstein-Podolsky-Rosen correlations" quantum physics text (Zotero import bug). Fixed via: (1) Body extraction (55 papers - extract from `## Abstract` section), (2) API calls to Semantic Scholar (1 paper), (3) Manual web research (23 papers), (4) Quote escaping (1 paper). All sources documented in fix scripts. |

---

## 2026-01-07

| Date | Category | Learning |
|------|----------|----------|
| 2026-01-07 | Git | **NO FILE DELETIONS Rule:** Session 7 accidentally deleted 422 PDF files using `rm -rf PDFs/`. Absolute rule implemented: NEVER use `rm`, `unlink`, or any delete command. Always use `mv file RECYCLE-BIN/`. This rule has NO EXCEPTIONS. Added to pre-commit validation and all documentation. See `Standards/file-safety.md`. |
| 2026-01-07 | PDF Processing | **PDF Recovery Strategy:** After mass deletion, recovered via multi-source strategy: (1) Zotero storage (read-only backup), (2) arXiv re-downloads, (3) Semantic Scholar, (4) Publisher sites. Created `PYTHON/recover_pdfs.py` script. Recovery took 8 hours. Documented in `docs/PDF_RECOVERY_GUIDE.md`. |

---

## Earlier 2026-01

| Date | Category | Learning |
|------|----------|----------|
| 2026-01-20 | Classification | **Ethics Framework Disambiguation:** When papers mention multiple ethical frameworks, prioritize based on primary contribution. Papers *proposing* virtue-based AI architectures = `virtue_ethics: "Yes"`. Papers *critiquing* utilitarianism while proposing alternatives = `utilitarian_ethics: "No"`. Check abstract for "we propose" vs "we critique". |
| 2026-01-18 | Classification | **Cultural Classification Scope:** Language-specific datasets (Chinese NLP, Arabic speech) get cultural tags even if not explicitly about cultural values. Rationale: Language embeds cultural context. Examples: Qwen (Chinese), GurbaniDB (Punjabi/Sikh), JambaJuice (Hebrew). Tag indicates cultural relevance for research contextualization. |
| 2026-01-15 | Author Management | **Short Name Handling:** Asian surnames (1-2 chars) + Western first names cause wikilink issues. "Li, John" creates `[[John Li]]` which may conflict with "Li, Jane" → `[[Jane Li]]`. Solution: Enrich with institutional affiliation + disambiguation. Example: `[[John Li (Stanford)]]`. See `Standards/author-management.md`. |
| 2026-01-12 | API | **Semantic Scholar Rate Limits:** API returns 429 (Too Many Requests) after ~100 requests in 5 minutes. Implements: (1) Exponential backoff (2^n seconds), (2) Batch requests with delays, (3) Cache results in `logs/semantic_scholar_cache.json`. Never retry immediately - causes IP blocking. |
| 2026-01-10 | Classification | **Benchmark vs Eval vs Dataset:** Distinction matters for research_topic field. **Benchmark** = standardized test suite with metrics (MMLU, GSM8K). **Eval** = evaluation framework/methodology (EleutherAI lm-eval-harness). **Dataset** = data collection without standard tasks (Wikipedia dump). Papers can be multiple types. See `Standards/classification-logic.md`. |
| 2026-01-08 | PDF Processing | **PDF Extract Format:** Extracts are `.md` files with YAML frontmatter + full text. Format: `---\nsource_pdf: "[[PDFs/file.pdf]]"\nextracted_date: YYYY-MM-DD\npages: N\n---\n\n[Full text]`. Enables full-text search in Obsidian. Created by `PYTHON/extract_pdf_text.py` using PyMuPDF. Links bidirectional: paper→extract, extract→PDF. |
| 2026-01-05 | Workflows | **7-Stage Classification Pipeline:** Optimal order for batch classification: (1) ethics_overall (broad filter), (2) ethics frameworks (virtue/deontological/utilitarian), (3) ethics_perspective (if overall=Yes but no framework), (4) research_topic (if overall=No), (5) cultural/religious, (6) moral psychology, (7) data nature (benchmark/eval/dataset). Order minimizes re-processing - each stage filters input for next. See `Standards/classification-logic.md`. |

---

## Archive Policy

**Trigger:** When a year section exceeds 200 entries
**Action:** Move to `learnings-log-YYYY.md` (e.g., `learnings-log-2026.md`)
**Retention:** Keep current year + previous year in main log
**Search:** Use `grep -r "pattern" Learnings/` to search across all years

---

## Related Documentation

- **Standards:** `../Standards/` - Timeless procedural knowledge
- **Session History:** `docs/SESSION_HISTORY.md` - Detailed session records
- **Workflows:** `docs/WORKFLOWS.md` - Multi-step procedures
- **Known Issues:** `docs/KNOWN_ISSUES.md` - Common problems and solutions

---

**Maintained by:** `/remember-thread` skill + manual additions
**Format:** Markdown table for greppability and version control
**Version Control:** Track in git for change history
