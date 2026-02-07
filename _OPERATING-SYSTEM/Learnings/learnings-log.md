# Learnings Log
*Last updated: 2026-02-07*

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

## 2026-02-07

| Date | Category | Learning |
|------|----------|----------|
| 2026-02-07 | Research | **Citation Graph Traversal: Forward > Backward:** When tracing citations of 15 seed papers via Semantic Scholar API, forward citations (who cites the seed) yielded 47 papers vs only 2 from backward references. New benchmarks build on established ones; established papers' references are mostly older foundational work already in the vault. Takeaway: For discovering new benchmarks in a mature field, prioritize forward citation traversal. |
| 2026-02-07 | API | **Semantic Scholar API for Batch Citation Lookup:** Free, no auth needed. Key endpoints: `/paper/{id}/citations` (forward) and `/paper/{id}/references` (backward) with `fields=title,authors,year,venue,externalIds,citationCount,abstract`. Can use arXiv IDs as `arXiv:XXXX.XXXXX`. Rate limits require pacing (~1 req/sec). Effective for systematic citation graph traversal across 15+ seed papers. |
| 2026-02-07 | Research | **Citation Graph Complements Keyword Search:** Agent 1 (citation graph) found 62 papers, with ~55 net new after removing vault overlaps. Many were not found by the 13 keyword-search agents (Sessions 33-34), particularly papers using novel terminology or from adjacent fields. Citation structure reveals methodological lineage that keyword search misses. |
| 2026-02-07 | Data Quality | **DOI Extraction Must Validate `10.XXXX/` Prefix:** When extracting DOIs from markdown, a naive regex like `DOI[:\s]*([^\s]+)` captures markdown formatting `**` as the DOI value (from `**DOI:**` labels). This caused catastrophic false merges — all 292 papers merged into a single entry because they all shared DOI=`**`. Fix: only accept DOIs matching `10.\d{4,9}/...`. |
| 2026-02-07 | Data Quality | **arXiv ID Format Variance Across Agent Reports:** Different agent reports use different arXiv formats: `arXiv:2406.12345`, `arXiv ID: 2406.12345` (bare numbers), `[2406.12345](url)` (markdown links). A single regex pattern misses ~30% of IDs. Need 3+ patterns: URL-based, colon-based, and `arXiv ID:` with optional `**` markdown. |
| 2026-02-07 | Data Quality | **Dedup Index Sync After Title-Match Merges:** When paper A is indexed by arXiv ID then merged into paper B by title match, the arXiv index still points to A (a zombie). Subsequent arXiv lookups find A instead of B, creating orphan merges. Fix: always call `update_indexes(canonical, merged_paper)` after any merge to ensure all indexes point to the surviving canonical entry. |
| 2026-02-07 | Workflows | **Iterative Script Development for Report Parsing:** Parsing 13 agent reports with varied markdown formats required 5 rounds of debugging. Each agent has slightly different field labels, header styles, and formatting. Lesson: always add debug/merge logging to dedup scripts. Saved dedup script to `PYTHON/extract_and_dedup_papers.py` for re-use. |
| 2026-02-07 | YAML | **parse_frontmatter() Destroys Lists:** The vault's `parse_frontmatter()` uses a simple regex that only handles flat `key: value` pairs. Round-tripping through `parse_frontmatter()` → `rebuild_frontmatter()` strips list-based fields (tags, etc.). For adding a single field to many papers, append the field line directly to the raw frontmatter string before the closing `---`. This preserves all formatting. See `lib/yaml_utils.py`. |
| 2026-02-07 | Workflows | **Multi-Agent Exhaustive Search Architecture:** Ran 19 parallel search agents across 3 waves for literature discovery. Architecture: Wave 1 (foundation: citation graphs, ACL Anthology, AIES/FAccT, workshops, PapersWithCode, PhilPapers, author networks, GitHub), Wave 2 (non-Western: Chinese, Islamic, African, East Asian, multilingual), Wave 3 (adjacent domains: professional ethics, prosocial/empathy, safety, political values, game theory, moral psychology). ~265 raw papers found pre-dedup. Status file: `logs/EXHAUSTIVE_SEARCH_2026_02_07_STATUS.md`. |
| 2026-02-07 | Workflows | **Context Window Management for Large Tasks:** The 19-agent search consumed the entire context window (~200K tokens) before Wave 4 (dedup/verification) could run. Lesson: For massive parallel operations, write intermediate summaries to disk after each wave completes, and consider using `/compact` between waves. Each subagent wrote its report to disk independently, so all work was recoverable despite main session failing. |
| 2026-02-07 | Workflows | **Session Continuity via Status Files:** Created `EXHAUSTIVE_SEARCH_2026_02_07_STATUS.md` as a "checkpoint" document. Contains: what was done (13 reports, paper counts), what's missing (Agent 1, Wave 4), step-by-step continuation guide, file locations, and estimated unique paper count. Enables any future session to pick up exactly where previous session left off. Pattern: always write recovery docs before context limit hits. |
| 2026-02-07 | Classification | **Normative vs Descriptive Ethics Boundary:** The key exclusion criterion for normative ethics benchmarks is whether the paper uses *prescriptive* philosophical frameworks (deontological, utilitarian, virtue) vs *descriptive* behavioral frameworks (Moral Foundations Theory, Kohlberg, revealed preference theory). MFT is the most common false positive — it's a psychological taxonomy, not a normative ethical system. ~61% of candidate papers excluded for this reason. |
| 2026-02-07 | Data Quality | **YAML Tags Unreliable for Cross-Cutting Research:** Existing classification fields (`virtue_ethics`, `deontological_ethics`, `is_benchmark`, etc.) are individually reasonable but don't reliably capture cross-cutting research questions. For identifying papers that combine normative ethics + benchmarks + LLM testing, direct paper reading was necessary. ~80 papers read to find 31 qualifying. Tag-based filtering would have missed ~30% and false-positived ~20%. |
| 2026-02-07 | Research | **Normative Ethics Benchmark Landscape (2024-2025):** 20 papers qualify as combining normative ethics + LLM benchmarks. Most common pattern: consequentialist + deontological (18 papers reference one or both). Virtue ethics is underrepresented (7 papers). Care ethics emerging (3 papers). All major LLM families tested somewhere. Report: `STATISTICS/normative-ethics-benchmarks-report.md`. |

---

## 2026-02-02

| Date | Category | Learning |
|------|----------|----------|
| 2026-02-02 | Workflows | **Progressive Disclosure Architecture:** Created `_OPERATING-SYSTEM/` structure with 4-layer memory (learnings log, standards, skills, configs). Keeps agent configs <80 lines while maintaining detailed procedural knowledge in `Standards/`. Inspired by LifeOS-Agent-Vault. See `_OPERATING-SYSTEM/README.md`. |
| 2026-02-02 | Workflows | **Hybrid Infrastructure Strategy:** Created `.agent/lib/` for new shared libraries while keeping existing `PYTHON/` scripts intact. Backward-compat shims re-export from lib modules, ensuring 129 existing scripts continue working. Migration is gradual, not disruptive. Pattern: Keep what works, add structure alongside. |
| 2026-02-02 | Workflows | **Library Migration Pattern:** When migrating critical modules (like yaml_utils.py - 409 lines, 51 dependencies), do 1:1 copy with NO behavior changes. Create shim immediately. Test both import paths. Only after validation, consider enhancements. Data safety > clever refactoring. |
| 2026-02-02 | Workflows | **Testing Before Building:** Paused at Phase 5 (40% done) to test what exists before adding more. Validated: Progressive disclosure works, thread finalization captured, lib structure sound. Next session can build confidently on tested foundation. Iterative > big-bang. |
| 2026-02-02 | Infrastructure | **Backward Compatibility Shims:** Pattern for gradual migration: (1) Copy module to new location, (2) Create shim at old location that re-exports from new, (3) Test both import paths work, (4) Gradually update imports. Prevents breaking 100+ scripts during migration. |
| 2026-02-02 | Skills | **Thread Finalization Design:** 2-skill workflow (remember-thread → finalize-thread) orchestrated by end-session. Remember captures learnings & updates docs (5 phases). Finalize runs QA & git (6 categories). Separation of concerns: memory vs quality checks. Systematic closure prevents knowledge loss. |
| 2026-02-02 | Git | **Session Handoff Documentation:** Created NEXT_STEPS.md with complete continuation guide (code snippets, step-by-step, success criteria, quick start commands). Enables any agent to pick up where previous session left off. Essential for long-running projects across context clears. |

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
