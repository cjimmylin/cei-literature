# Mid-Project Handoff v2 — 2026-02-16 (Post Session 89)

This document captures the state of the CEI Literature Vault and provides actionable guidance for the next session. Supersedes `handoff-doc-MIDDLE.md` (post-Session 86).

---

## 1. Vault Census

| Metric | Count | Notes |
|--------|-------|-------|
| Papers | 2,034 | 2,002 base + 32 religious tradition imports (ZERO prefix) |
| PDFs on disk | 1,797 | In `Lit-WS-PDFs/YYYY/` subdirs |
| PDF Extracts | 2,487 | In `PDF Extracts/YYYY/` subdirs |
| Author Profiles | 9,791 | In `Authors/` (187 garbage removed, pipeline rebuilt) |
| Validation | 2,034/2,034 pass | 0 errors |

### Field Coverage (all 2,034 papers)

| Field | Coverage | Detail |
|-------|----------|--------|
| `ethics_overall` | 100% | All papers classified |
| `LLM_assessed` | 100% | 1,579 with model data (78%), rest N/A |
| `languages_list` | 100% | 1,415 with data (70.7%), 587 blank |
| `cultures_nationalities_list` | 100% | 1,275 with data (63.7%), 727 N/A |
| `local_pdf` | 100% | 1,795 valid links, 203 N/A, 4 not-found |
| `benchmark_candidate` | 100% | 989 Yes (49.4%) from 2,002 surveyed |
| `authors_incomplete` | 54 papers | Down from 60 (6 resolved via Semantic Scholar) |
| Unknown-author papers | 16 | All institutional (legit no individual author) |

### Reports & Dashboards

| Report/Dashboard | File | Status |
|------------------|------|--------|
| Vault Overview | `STATISTICS/20260216-vault-overview-report.md` | STALE (shows 924/528) |
| Benchmark Survey | `STATISTICS/20260216-llm-ethics-benchmark-survey.md` | STALE (shows 924 screened) |
| Values Alignment | `STATISTICS/20260216-ethical-values-alignment-benchmarks-report.md` | STALE (pre-expansion) |
| LLM Assessment | `STATISTICS/20260216-llm-assessment-data-availability-report.md` | FRESH (2,034 papers) |
| Religious Traditions | `STATISTICS/20260216-religious-ethical-tradition-gap-analysis.md` | FRESH (2,034 papers) |
| Dashboard (HTML) | `DASHBOARDS/20260216-vault-dashboard.html` | Deployed, 2,034 papers |
| Dashboard v3 (HTML) | `DASHBOARDS/20260216-vault-dashboard-3.html` | Deployed, 2,034 papers, 767 KB |

### GitHub Pages Dashboards (ALL DEPLOYED)

| Dashboard | URL | Last Updated |
|-----------|-----|--------------|
| General vault | `cjimmylin.github.io/cei-dashboard/` | 2026-02-16 (2,034 papers) |
| LLM assessment | `cjimmylin.github.io/cei-dashboard-llm/` | 2026-02-16 (2,034 papers) |
| Dashboard v3 (8-tab) | `cjimmylin.github.io/cei-dashboard-3/` | 2026-02-16 (2,034 papers, 55 charts) |

---

## 2. What's Been Done (Sessions 86 RIGHT — 89)

### Session 86 RIGHT — Year Fix + Author Rebuild + Reports
- Fixed year field corruption across 1,005 papers
- Rebuilt author pipeline: 9,791 unique authors, 162 new stubs, 8,835 updated
- Cleaned 66 garbage author profiles
- Regenerated all 6 reports with 2,034-paper data
- Documentation refresh + handoff docs

### Session 87 — Root PDF Cleanup + ZERO Paper Assessment
- Sorted 128 root PDFs to year-based directories + updated YAML wikilinks
- Recycled 3 legacy ethics directories (84 PDFs moved to RECYCLE-BIN)
- LLM-assessed 32 ZERO papers (1 GPT-4, 31 NA)

### Session 88 — ZERO Paper Enrichment + Dashboard Deployment
- Enriched 32 ZERO papers with `cultures_nationalities_list` and `languages_list`
- Deployed `cei-dashboard-llm` to GitHub Pages (commit f40fcc6)

### Session 89 — Dashboard v3 Generation + Deployment
- Created `PYTHON/generate_vault_dashboard_3.py` (1,903 lines)
  - Template injection architecture: reads old v3 HTML, replaces `const DATA` blob
  - Computes 20 data sections including Cultural Values, Moral Psychology, Religious Values, Normative Ethics
- Generated `DASHBOARDS/20260216-vault-dashboard-3.html` (767 KB, 8 tabs, 55 charts)
- Deployed to `cjimmylin.github.io/cei-dashboard-3/`
- Deployed `cei-dashboard` to GitHub Pages (2,034 papers)

---

## 3. Remaining Tasks

### Tier 1: Reports (High Value, Low Effort)

#### A. Regenerate 3 Stale Text Reports
3 of 5 markdown reports are stale — they still reference 924 papers / 528 candidates instead of 2,034 / 989.

**Stale reports:**
1. `generate_vault_overview_report.py` — shows "924 screened, 528 candidates"
2. `generate_benchmark_survey_report.py` — shows "924 papers screened"
3. `generate_values_alignment_report.py` — shows pre-expansion data

**Steps:**
1. Update `OUTPUT_FILE` in each script to use a NEW date prefix (e.g., `20260217-`)
2. Run:
   ```bash
   cd CEI-Lit-WS
   ../.venv/bin/python PYTHON/generate_vault_overview_report.py
   ../.venv/bin/python PYTHON/generate_benchmark_survey_report.py
   ../.venv/bin/python PYTHON/generate_values_alignment_report.py
   ```
3. Verify output shows 2,034 papers and 989 candidates

**CRITICAL:** Never overwrite existing `20260216-` files. Create new date-prefixed copies.

---

### Tier 2: Data Quality (Moderate Effort)

#### B. Download 54 Bot-Blocked PDFs (Manual Browser)
54 PDFs returned HTTP 403 or HTML landing pages from scripts. These require manual browser download.

| Source | Count |
|--------|-------|
| MDPI | 15 |
| ACM | 6 |
| DOI.org | 6 |
| IEEE | 4 |
| ScienceDirect | 4 |
| Other | 19 |

**Data:** `logs/20260216-pdf_download_results.json` (has URLs + expected filenames)

**After download:**
1. Save PDFs to `Lit-WS-PDFs/YYYY/` with correct filename
2. Extract text: `../.venv/bin/python PYTHON/extract_pdf_text.py "Lit-WS-PDFs/YYYY/filename.pdf"`
3. Update paper YAML: `local_pdf` and `pdf_extract` fields
4. Script can be re-run: `../.venv/bin/python PYTHON/download_discovered_pdfs.py` (skips already-downloaded)

#### C. Ochasi PDF (1 paper, manual)
- **Paper:** `papers/2025-Ochasi-Reframing Justice in Healthcare AI.md`
- **URL:** `https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/dewb.70007`
- **Save to:** `Lit-WS-PDFs/2025/2025-Ochasi-Reframing Justice in Healthcare AI.pdf`

#### D. Resolve 54 `authors_incomplete` Papers
- Down from 263 (Session 80) → 60 (Session 86) → 54 (6 resolved via Semantic Scholar)
- Semantic Scholar API is heavily rate-limited (HTTP 429 even at 15s delays)
- Many may be truly unresolvable (paywalled, no API data)
- Scripts: `PYTHON/extract_authors_from_pdf.py`, `PYTHON/apply_author_extraction.py`

---

### Tier 3: Maintenance (Low Priority)

#### E. 4 "File Not Found" PDF Links
4 papers have `[[Unknown]]` in wikilinks with no matching PDF on disk. These are among the 16 institutional/Unknown-author papers. If authors can be identified, renaming would fix the links.

#### F. Unquoted Wikilinks (Cosmetic)
- ~155 `local_pdf` fields with unquoted `[[...]]`
- ~44 `first_author` fields with unquoted `[[...]]`
- Validation passes, Obsidian works fine. Purely cosmetic inconsistency.

#### G. 16 Unknown-Author Papers (Closed)
All 16 are institutional/non-academic content with legitimately no individual author. No action needed.

---

## 4. Key Scripts & Locations

### Report Generators (in `CEI-Lit-WS/PYTHON/`)

| Script | Output |
|--------|--------|
| `generate_vault_overview_report.py` | Vault overview (14 sections + 2 appendices) |
| `generate_benchmark_survey_report.py` | Benchmark survey (10 categories) |
| `generate_values_alignment_report.py` | Values alignment (6 sections, A-F) |
| `generate_llm_assessment_report.py` | LLM assessment (4 sections + 2 appendices) |
| `generate_religious_gap_report.py` | Religious tradition gap analysis |

### Dashboard Generators

| Script | Output | Size |
|--------|--------|------|
| `generate_vault_dashboard.py` | Basic 7-tab dashboard | ~200 KB |
| `generate_vault_dashboard_3.py` | Advanced 8-tab dashboard (template injection) | ~767 KB |

### Validation & Utilities

| Script | Purpose |
|--------|---------|
| `validate_all_papers.py` | YAML validation — run after any batch modification |
| `validate_papers_enhanced.py` | Extended validation checks |
| `audit_pdf_links.py` | PDF link integrity audit |
| `download_discovered_pdfs.py` | PDF download (supports `--start` for resume) |
| `extract_pdf_text.py` | PDF text extraction |
| `detect_orphaned_authors.py` | 3-tier orphan detection (garbage/format/true) |

### Data & Logs (in `CEI-Lit-WS/logs/`)

| File | Contents |
|------|----------|
| `20260216-benchmark_survey_all_classifications.json` | 2,002 survey entries |
| `20260216-benchmark_survey_candidates.json` | 989 benchmark candidates |
| `20260216-culture_list_consolidation.json` | Culture/nationality data |
| `20260216-language_list_consolidation.json` | Language data |
| `20260216-pdf_download_results.json` | 74 entries (20 success, 54 fail) |
| `20260216-zero_coverage_search_master_list.json` | 42 religious tradition papers found |
| `20260216-orphaned_authors_classified.json` | Author profile classification |

### Memory Files (in `~/.claude/projects/.../memory/`)

| File | Purpose |
|------|---------|
| `MEMORY.md` | Master memory (auto-loaded into every session) |
| `outstanding-tasks.md` | Outstanding task tracker |
| `benchmark-survey-pipeline.md` | Benchmark survey pipeline docs |
| `llm-assessment-pipeline.md` | LLM assessment docs |
| `report-generation.md` | Report generation patterns & lessons |

---

## 5. Architecture Notes

### Dashboard v3 Template Injection (New in Session 89)
- `generate_vault_dashboard_3.py` reads the old v3 HTML template (636 KB)
- Uses brace-counting parser to find `const DATA = {...};` boundary (regex fails on nested braces)
- Replaces only the DATA blob, preserves all CSS/JS/chart code
- Extended YAML scanner handles both scalar and multi-line list fields
- 5 compute functions: base, cultural, normative, moral_psych, religious

### YAML Safety (CRITICAL)
- **NEVER** use `parse_frontmatter()` → `rebuild_frontmatter()` round-trip (destroys list fields)
- Safe pattern: `re.subn(rf'^{re.escape(key)}:.*$', replacement, frontmatter, count=1, flags=re.MULTILINE)`
- Always run `validate_all_papers.py` after batch YAML modifications

### File Safety (CRITICAL)
- **NEVER** use `rm` — always `mv` to `RECYCLE-BIN/`
- PDFs in `Lit-WS-PDFs/YYYY/`, extracts in `PDF Extracts/YYYY/`
- Use `rglob("*.pdf")` not `glob("*.pdf")` for year-based subdirs
- Use `iterdir()` if filenames may contain brackets (`[[Unknown]]`)

### Report Immutability (CRITICAL)
- **NEVER** overwrite existing reports — create new ones with new date prefixes
- Update script `OUTPUT_FILE` paths to the new date BEFORE running

### Parallel Agent Pattern
- Batch generator → N parallel agents → consolidation → validation
- Waves of 5 agents to manage rate limits
- Always verify agent result file freshness before consolidating
- Watch for curly/straight quote filename mismatches in agent outputs

---

## 6. Git & Deployment

- **Repo:** `https://github.com/cjimmylin/cei-literature`
- **Branch:** `main`
- **Latest commit:** `f68e1430` — "Infrastructure: Add dashboard v3 generation script + regenerated dashboard (2,034 papers)"
- **Status:** Clean working tree, 1 commit ahead of origin (needs push)
- **PDFs:** NOT tracked in git (external storage)
- **Dashboard repos (all deployed):**
  - `cjimmylin/cei-dashboard` (commit a8e9a32)
  - `cjimmylin/cei-dashboard-llm` (commit f40fcc6)
  - `cjimmylin/cei-dashboard-3` (commit 4e4ea8f)

---

## 7. What NOT to Worry About

- **Validation:** 2,034/2,034 pass, 0 errors. Vault is clean.
- **Benchmark survey:** 100% complete (989 candidates from 2,002 papers surveyed)
- **Culture/language enrichment:** Complete across all papers
- **Author pipeline:** Rebuilt and clean (9,791 profiles, 187 garbage removed)
- **Dashboards:** All 3 deployed with current 2,034-paper data
- **Religious tradition search:** Complete (32 papers imported for Shinto/Baha'i/Zoroastrian/Indigenous)
- **Root PDFs:** All sorted into year-based directories

---

## 8. Recommended Next Session Priorities

| Priority | Task | Type | Est. Effort |
|----------|------|------|-------------|
| 1 | Push main to origin (1 commit ahead) | `git push` | 1 min |
| 2 | Regenerate 3 stale text reports (new date prefix) | Scripts | 15 min |
| 3 | Manual PDF downloads (54 bot-blocked) | Browser | 1-2 hours |
| 4 | Resolve authors_incomplete (54 papers) | API/manual | 30 min |

Steps 1-2 are quick wins that bring all artifacts up to date with the 2,034-paper vault.

---

*Generated: 2026-02-16, Post Session 89*
*Vault: 2,034 papers, 2,034/2,034 valid, 0 errors*
*Dashboards: All 3 deployed*
