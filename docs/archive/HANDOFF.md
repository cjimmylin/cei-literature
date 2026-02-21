# HANDOFF.md — Session 79 Continuation Guide

**Generated:** 2026-02-15 | **Vault:** CEI Literature Vault | **Papers on disk:** 2,008

> This file is a self-contained guide for a fresh Claude session to continue work on the CEI Literature Vault. Read this file first, then `CLAUDE.md` for operating rules.

---

## Current State (as of Feb 15, 2026)

### What Just Happened (Session 78)

Session 78 completed two major tasks:

1. **Religious Tradition Reclassification (Workstreams A+C):** Deep-read 228 candidate papers, reclassified 77 from N/A to specific religious traditions. Religious-tagged papers went from 126 to 203 across 14 traditions. Committed to git.
2. **Culture Search Import (parallel work):** 30 agents searched for culture/nationality benchmark papers, found 375, imported 161 truly new ones as CULT-keyed papers. **This work is NOT yet committed.**

### Uncommitted Files (286 total)

| Category | Count | Status |
|----------|-------|--------|
| Untracked papers (`papers/`) | 161 | CULT-keyed, need classification |
| Untracked PDF extracts (`PDF Extracts/`) | 112 | Already extracted from downloaded PDFs |
| Untracked Python scripts (`PYTHON/`) | 5 | Culture search pipeline scripts |
| Untracked log (`logs/`) | 1 | `20260215-culture_search_master_list.md` |
| Modified Python scripts | 7 | Report generators + classifiers (minor fixes) |

### Key Numbers

| Metric | Value |
|--------|-------|
| Papers on disk | 2,008 |
| Papers committed in git | 1,847 |
| CULT papers (new, unclassified) | 161 |
| CULT papers with PDF | 126 (78%) |
| CULT papers with extract | 112 (70%) |
| CULT papers missing PDF | 35 |
| Papers with `[[Unknown]]` author | 104 (11 CULT + 93 non-CULT) |
| YAML validation | 2,008/2,008 PASS, 0 errors |
| Zero-benchmark traditions | 4 (Shinto, Baha'i, Zoroastrian, Indigenous) |

---

## Priority 1: Commit Uncommitted Work

**Status:** Not started
**Dependencies:** None
**Why first:** Preserves the culture-search import work before any further modifications.

### Steps

```bash
# 1. Verify validation passes
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS
../.venv/bin/python PYTHON/validate_all_papers.py

# 2. Review what will be committed
git status --short | head -30
git status --short | wc -l   # Should show 286

# 3. Stage and commit in logical groups
# Group A: New culture search scripts + log
git add PYTHON/analyze_batch_10.py \
        PYTHON/consolidate_culture_lists.py \
        PYTHON/consolidate_culture_search.py \
        PYTHON/generate_culture_list_batches.py \
        PYTHON/import_culture_search_papers.py \
        logs/20260215-culture_search_master_list.md

# Group B: Modified Python scripts
git add PYTHON/batch_abstract_and_classify.py \
        PYTHON/classify_cultural_religious.py \
        PYTHON/generate_benchmark_survey_report.py \
        PYTHON/generate_llm_assessment_report.py \
        PYTHON/generate_values_alignment_report.py \
        PYTHON/generate_vault_dashboard.py \
        PYTHON/generate_vault_overview_report.py

# Group C: New papers + extracts (bulk)
git add papers/
git add "PDF Extracts/"

# 4. Commit
git commit -m "Import 161 culture/nationality benchmark papers (CULT keys) + 112 extracts

30-agent culture search found 375 papers, 212 already in vault, 161 new.
Includes 5 pipeline scripts and updated report generators.
Papers need classification, 35 still missing PDFs."

# 5. Verify
git status   # Should be clean
```

### Expected Output
- Clean working tree after commit
- 2,008 papers tracked in git

---

## Priority 2: Classify 161 CULT Papers

**Status:** Not started (all 161 have blank `ethics_overall`)
**Dependencies:** Priority 1 (commit)
**Scripts:** `PYTHON/batch_abstract_and_classify.py` (7-stage pipeline)

### How Classification Works

The classification pipeline has 7 stages that run sequentially:
1. `classify_ethics.py` (stages 1-2): Sets `ethics_overall`, `virtue_ethics`, `deontological_ethics`, `utilitarian_ethics`
2. `classify_ethics_perspective.py` (stage 3): Only if ethics=Yes AND all 3 branches=No
3. `classify_non_ethics_topics.py` (stage 4): Only if ethics=No
4. `classify_cultural_religious.py` (stage 5): Sets `national_ethnic_cultural`, `religious_values`
5. `classify_moral_psych.py` (stage 6): Sets `moral_psychology`
6. `classify_data_nature.py` (stage 7): Sets `is_benchmark`, `is_eval`, `is_dataset`

### Steps

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS

# Run batch classification on all papers (idempotent - skips already-classified)
../.venv/bin/python PYTHON/batch_abstract_and_classify.py

# Validate after classification
../.venv/bin/python PYTHON/validate_all_papers.py
```

### Alternative: Targeted Classification

If `batch_abstract_and_classify.py` is too slow or hits issues, you can classify individual papers:

```python
# From CEI-Lit-WS/ directory
import classify_ethics as ce
import classify_cultural_religious as cr
import classify_moral_psych as mp
import classify_data_nature as cdn

# For each paper file:
ce.classify_paper(filepath)         # Stages 1-3
cr.classify_paper(filepath)         # Stage 5
mp.classify_paper(filepath)         # Stage 6
cdn.classify_paper(filepath)        # Stage 7
```

### Expected Output
- 161 papers with populated classification fields
- Validation still passes (2,008/2,008)
- Estimate: ~30-40% will have `ethics_overall: Yes` based on prior wave patterns

---

## Priority 3: PDF Acquisition + Extraction

**Status:** 126/161 have PDFs, 112/161 have extracts
**Dependencies:** None (can run in parallel with Priority 2)
**Key scripts:**
- `PYTHON/comprehensive_pdf_finder.py` — 13-strategy waterfall for PDF download
- `PYTHON/batch_extract_pdfs.py` — Text extraction with `pdftotext`

### Steps

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS

# Step 1: Download missing PDFs (35 papers)
../.venv/bin/python PYTHON/comprehensive_pdf_finder.py

# Step 2: Extract text from any new PDFs (and any CULT PDFs missing extracts)
../.venv/bin/python PYTHON/batch_extract_pdfs.py

# Step 3: Validate
../.venv/bin/python PYTHON/validate_all_papers.py
```

### PDF Directory Layout
- PDFs go in `PDFs/YYYY/filename.pdf` (year-based subdirectories)
- Extracts go in `PDF Extracts/YYYY/filename.md`
- YAML refs: `local_pdf: "[[PDFs/2025/2025-Author-Title.pdf]]"`
- Use `rglob("*.pdf")` not `glob("*.pdf")` when scanning PDFs

### Known Limitations
- Semantic Scholar API: Very aggressive rate limiting (10s+ delay, 429 after ~4 requests)
- Wiley, ACM DL, ResearchGate: Cloudflare bot-blocking (need manual browser download)
- 1 paper (Ochasi) still needs manual download: `https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/dewb.70007`

### Expected Output
- ~140-150 papers with PDFs (some paywalled/unavailable)
- ~130+ papers with extracts

---

## Priority 4: LLM Assessment Enrichment

**Status:** 161 CULT papers + ~732 older papers have placeholder `LLM_assessed` fields
**Dependencies:** Priority 2 (classification), Priority 3 (extracts help but not required)
**Scripts:**
- `PYTHON/generate_llm_assessment_batches.py` — Generates agent batch files
- `PYTHON/assess_llm_data.py` — Regex helpers for LLM model detection
- `PYTHON/consolidate_llm_assessments.py` — Applies agent results to YAML

### How It Works

This is an agent swarm task. Each agent reads ~25-40 papers (YAML + extract) and determines:
- `LLM_assessed`: Which LLM models the paper evaluates (e.g., "GPT-4, BERT, LLaMA")
- `DATA_URL`: Where the benchmark/dataset can be downloaded
- `data_description`: Brief description of what the data contains

### Steps

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS

# Step 1: Generate batches (use --since to target recent papers)
../.venv/bin/python PYTHON/generate_llm_assessment_batches.py --since 20260215

# Step 2: Launch agent swarm (5 agents at a time, ~25 papers each)
# Each agent reads its batch file and writes results JSON
# Pattern: 10 agents in 2 waves of 5

# Step 3: Consolidate results
../.venv/bin/python PYTHON/consolidate_llm_assessments.py

# Step 4: Validate
../.venv/bin/python PYTHON/validate_all_papers.py
```

### YAML Safety Rules (CRITICAL)
- **NEVER** use `parse_frontmatter()` then `rebuild_frontmatter()` — destroys list fields
- Safe pattern: `re.subn(rf'^{re.escape(key)}:.*$', replacement, frontmatter, count=1, flags=re.MULTILINE)`
- `validate_frontmatter()` counts raw `"` — use `value.replace('"', "'")` NOT `\"`
- Always validate after batch modifications

### Expected Output
- 161 CULT papers enriched with LLM assessment data
- ~5-10% will have actual LLM model names, ~15-20% will have DATA_URLs

---

## Priority 5: Author Profiles + Unknown Resolution

**Status:** 104 papers have `[[Unknown]]` placeholder author (11 CULT, 93 non-CULT)
**Dependencies:** Priority 1 (commit)
**Scripts:**
- `PYTHON/resolve_all_unknown_authors.py` — 6-source API waterfall (OpenAlex best)
- `PYTHON/discover_unknown_authors.py` + `PYTHON/apply_author_fixes.py` — older 2-step approach
- `PYTHON/rebuild_author_profiles.py` — Rebuild author profile pages

### Steps

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS

# Step 1: Resolve unknown authors via APIs
../.venv/bin/python PYTHON/resolve_all_unknown_authors.py

# Step 2: Rebuild author profiles (run AFTER author resolution)
../.venv/bin/python PYTHON/build_author_paper_map.py
../.venv/bin/python PYTHON/disambiguate_authors.py
../.venv/bin/python PYTHON/update_paper_last_author.py
../.venv/bin/python PYTHON/rebuild_author_profiles.py

# Step 3: Validate
../.venv/bin/python PYTHON/validate_all_papers.py
```

### Key Lessons from Prior Runs
- OpenAlex resolves ~80% of unknown authors (best free API)
- arXiv rate-limits compound after ~75 requests
- ~86 of the unknowns are non-academic (blogs, workshop pages, Chinese govt docs) — unresolvable
- Always validate first-author match before applying API results (prevents wrong-paper contamination)

### Expected Output
- ~15-25 more authors resolved (mostly the 11 CULT unknowns)
- Updated author profile pages in `Authors/`

---

## Priority 6: Targeted Religious Tradition Search (Workstream B)

**Status:** Not started — identified as needed by gap analysis
**Dependencies:** Priorities 1-2 (commit + classify)
**Reference:** `STATISTICS/20260215-religious-ethical-tradition-gap-analysis.md` Section 10

### What This Is

The gap analysis found 4 traditions with ZERO benchmarks: Shinto, Baha'i, Zoroastrian, Indigenous. Workstream B is a targeted literature search to find papers for these underrepresented traditions.

### Search Priorities (from gap analysis)

| Priority | Tradition | Where to Search |
|----------|-----------|-----------------|
| 1 | Buddhist | HuggingFace datasets, ACL C3NLP workshop, cite-tracking DharmaBench/BuddhismEval |
| 2 | Ubuntu/African | AfricaNLP, Deep Learning Indaba, Masakhane project |
| 3 | Hindu | Indian NLP conferences, Hindi AI ethics papers |
| 4 | Indigenous | Data sovereignty conferences, AIATSIS, Canadian First Nations digital humanities |
| 5 | Taoist | Chinese-language NLP (CCL, ROCLING) |
| 6 | Shinto | Japanese NLP (YANS, NLP2026), JETHICS |
| 7 | Jain | Anekantavada x AI pluralism, Indian philosophy |

### Search Methodology

Use the same agent swarm pattern as prior searches:
1. Generate search batches (one agent per tradition/venue)
2. Each agent searches academic databases (Semantic Scholar, arXiv, ACL Anthology, Google Scholar)
3. Consolidate results into a master list
4. Dedup against existing vault
5. Import new papers via `import_culture_search_papers.py` or similar

### Key Finding from Workstream A+C
> 0 of 203 religious-tagged papers also have `ethics_overall=Yes`. Papers are about religious *bias detection* or religious *NLP*, NOT religious *ethical frameworks applied to AI*. This is the real gap.

### Expected Output
- 20-50 new papers from underrepresented traditions
- Particularly: Shinto, Baha'i, Zoroastrian benchmarks (currently at 0)

---

## Priority 7: Dashboard + Report Regeneration

**Status:** All reports are stale (show 846-1,847 papers; vault now has 2,008)
**Dependencies:** Priorities 2-5 (classification + enrichment should complete first)
**Scripts:** All in `PYTHON/`

### Steps

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS

# Regenerate all reports
../.venv/bin/python PYTHON/generate_vault_overview_report.py
../.venv/bin/python PYTHON/generate_vault_dashboard.py
../.venv/bin/python PYTHON/generate_values_alignment_report.py
../.venv/bin/python PYTHON/generate_llm_assessment_report.py
../.venv/bin/python PYTHON/generate_benchmark_survey_report.py

# Reports go to STATISTICS/ with YYYYMMDD- prefix
# Dashboard outputs an HTML file with ECharts visualizations
```

### GitHub Pages Dashboards
- Main: `https://cjimmylin.github.io/cei-dashboard/`
- LLM: `https://cjimmylin.github.io/cei-dashboard-llm/`
- Repos: `cjimmylin/cei-dashboard`, `cjimmylin/cei-dashboard-llm`
- After regenerating, copy the HTML to the repos and push

### Expected Output
- Updated reports reflecting 2,008 papers
- Refreshed dashboard with accurate KPI cards

---

## Appendix A: Key File Paths

### Directories
| Path | Contents |
|------|----------|
| `papers/` | 2,008 paper markdown files with YAML frontmatter |
| `PDFs/YYYY/` | PDF files in year-based subdirectories |
| `PDF Extracts/YYYY/` | Extracted text from PDFs in year-based subdirectories |
| `Authors/` | 4,869 author profile pages |
| `PYTHON/` | All processing scripts |
| `STATISTICS/` | Generated reports (YYYYMMDD- prefix) |
| `logs/` | Processing logs and JSON data (YYYYMMDD- prefix) |
| `RECYCLE-BIN/` | Deleted files (never use `rm`) |
| `_OPERATING-SYSTEM/Standards/` | Detailed operating rules |

### Key Scripts
| Script | Purpose |
|--------|---------|
| `validate_all_papers.py` | YAML validation — run after every batch change |
| `batch_abstract_and_classify.py` | 7-stage classification pipeline |
| `comprehensive_pdf_finder.py` | 13-strategy PDF download waterfall |
| `batch_extract_pdfs.py` | Bulk text extraction from PDFs |
| `generate_llm_assessment_batches.py` | LLM enrichment batch generator |
| `consolidate_llm_assessments.py` | Apply LLM assessment agent results |
| `resolve_all_unknown_authors.py` | 6-source API author resolution |
| `import_culture_search_papers.py` | Import papers from search agents |

### Key Data Files
| File | Contents |
|------|----------|
| `logs/20260215-culture_search_master_list.json` | 163 new culture papers metadata |
| `logs/20260215-religious_audit_all_classifications.json` | 228 religious audit entries |
| `logs/20260215-religious_audit_decisions.json` | 77 reclassification decisions |
| `STATISTICS/20260215-religious-ethical-tradition-gap-analysis.md` | 12-section gap report |

### Utility Libraries
| File | Purpose |
|------|---------|
| `.agent/lib/yaml_utils.py` | Canonical YAML parser (regex-based, flat key:value only) |
| `PYTHON/yaml_frontmatter_utils.py` | Shim importing from canonical yaml_utils |
| `.agent/lib/pdf_utils.py` | `resolve_pdf_path()`, `make_pdf_wikilink()`, `make_extract_path()` |

---

## Appendix B: Known Issues + Gotchas

### YAML Safety (CRITICAL — Memorize These)

1. **NEVER round-trip YAML** via `parse_frontmatter()` then `rebuild_frontmatter()` — this destroys list-based fields (tags, authors). Use safe regex replacement instead.
2. **Safe field update pattern:**
   ```python
   re.subn(rf'^{re.escape(key)}:.*$', f'{key}: "{value}"', frontmatter, count=1, flags=re.MULTILINE)
   ```
3. **Quote handling:** Use `value.replace('"', "'")` NOT `\"` escaping. The validator counts raw `"` and odd counts fail.
4. **Always validate** after batch YAML changes: `../.venv/bin/python PYTHON/validate_all_papers.py`

### File Safety

1. **NEVER use `rm`** — always `mv` to `RECYCLE-BIN/`. (Session 7 deleted 422 PDFs.)
2. **PDF paths use year subdirs:** `PDFs/YYYY/filename.pdf`, extracts at `PDF Extracts/YYYY/filename.md`
3. **Use `rglob("*.pdf")`** not `glob("*.pdf")` when scanning all PDFs (year subdirs).

### API Rate Limits

1. **Semantic Scholar:** 10s+ delay needed, 429 after ~4 rapid requests. Nearly useless for batch ops.
2. **arXiv:** 3s delay, compounds after ~75 requests. Use `id_list` not `search_query=arXiv:{id}`.
3. **OpenAlex:** Best free API for author resolution (~80% success rate).

### Classification Gotchas

1. YAML classification tags are unreliable for cross-cutting research questions. Deep-read preferred.
2. Keyword screening misses ~40% of positives — full deep-read is more accurate.
3. Stage 3 (ethics perspective) only runs when ethics=Yes AND all 3 branch fields=No.
4. Stage 4 (non-ethics topics) only runs when ethics=No.

### Agent Swarm Pattern

1. Script takes START/END range args with forced stdout flush: `print = functools.partial(print, flush=True)`
2. Launch N background processes: `python script.py 1 27 > log_01.log 2>&1 &`
3. Monitor: `wc -l logs/*.log` and `grep SUMMARY logs/*.log`
4. **Always run a sequential mop-up pass** on the full range after parallel batches (catches ~5-7% stragglers from stdout buffering).

### Parallel Write Safety

1. Parallel JSON writes corrupt files — use PID-scoped temp files: `f".tmp.{os.getpid()}"` + `os.replace()`.
2. arXiv ID regex `\d{4}\.\d{4,5}` matches DOI substrings — only extract from `arxiv.org` URLs.

### Naming Conventions

1. All files in `STATISTICS/` and `logs/` (top-level only) must start with `YYYYMMDD-` date prefix.
2. Paper keys: `EXSR` (exhaustive search), `LSRC` (language search), `CULT` (culture search), or sequential number.

---

## Appendix C: Remaining Low-Priority Items

These items from the outstanding task list are still relevant but lower priority:

1. **Ochasi PDF** — Manual browser download from Wiley (OA but bot-blocked):
   - URL: `https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/dewb.70007`
   - Save to: `PDFs/2025/2025-Ochasi-Reframing Justice in Healthcare AI.pdf`
   - Then update `local_pdf` and re-extract

2. **Deduplication check** — 161 CULT papers haven't been checked against existing vault:
   - Script: `PYTHON/detect_duplicates.py` then `PYTHON/consolidate_duplicates.py`
   - Run AFTER author resolution to avoid false negatives

3. **`DATE_ADDED` backfill** — ~582 older papers lack this field (informational only)

4. **`authors_incomplete` resolution** — ~25 papers flagged (use `PYTHON/resolve_incomplete_authors.py`)

---

*This file is ephemeral session state. Do not commit to git. Delete when all priorities are complete.*
