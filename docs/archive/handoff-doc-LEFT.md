# CEI Literature Vault — Post-Session 85 Handoff

**Date:** 2026-02-16
**Sessions covered:** 84 + 85
**Last commit:** `3a214291` (pushed to `origin/main`)

---

## Vault Snapshot

| Metric | Count |
|--------|-------|
| Papers | 2,002 |
| PDFs indexed | ~1,813 |
| PDF Extracts | ~2,487 |
| Author Profiles | ~9,801 |
| Validation | 2,002/2,002 pass, 0 errors |
| Benchmark survey | 100% (989 candidates / 2,002 surveyed) |
| Abstracts | 2,002/2,002 present |
| Culture/nationality data | 1,275 papers (63.7%) |
| LLM assessment enriched | 1,115 papers |

---

## What Was Completed (Sessions 84-85)

### Session 84 (massive)
- Benchmark deep-read survey: **2,002/2,002 complete** (989 candidates, 49.4%)
- Unknown author resolution: 70/86 resolved via 3 LLM agents
- PDF discovery: 74 new PDF URLs found from 223 missing-PDF papers
- local_pdf fix: 44 papers (29 blank->N/A, 9 quote fixes, 6 PDF renames)
- DATA_URL formatting: 433 papers fixed
- Garbage author cleanup: 8 profiles recycled
- Report scripts: 5 updated to 20260216 date prefixes
- 6 new PYTHON scripts created

### Session 85
- Author fixes applied: 70 YAML updated, 69 papers renamed, 31 PDFs + 31 extracts renamed
- 250 new author profiles created
- PDF download: 20/74 downloaded + extracted + YAML updated
- 54 PDFs blocked by bot protection (need manual browser download)

---

## Priority 1 — Regenerate All Reports & Dashboards

**Status:** UNBLOCKED (benchmark survey now 100% complete)
**Effort:** ~15 minutes (5 sequential script runs + 2 dashboard pushes)

The 5 report scripts already have OUTPUT_FILE updated to `20260216-` date prefixes. All data sources are fresh.

### Steps:
```bash
cd CEI-Lit-WS

# Run all 5 reports sequentially
../.venv/bin/python PYTHON/generate_vault_overview_report.py
../.venv/bin/python PYTHON/generate_values_alignment_report.py
../.venv/bin/python PYTHON/generate_benchmark_survey_report.py
../.venv/bin/python PYTHON/generate_llm_assessment_report.py

# Dashboard (generates HTML)
../.venv/bin/python PYTHON/generate_vault_dashboard.py
```

### Push dashboards:
- `cjimmylin.github.io/cei-dashboard/` — general vault dashboard
- `cjimmylin.github.io/cei-dashboard-llm/` — LLM assessment dashboard

### Current stale reports:
| Report | Current Date | Issue |
|--------|-------------|-------|
| Vault Overview | 20260215 | Pre-benchmark-completion, pre-author-fixes |
| Values Alignment | 20260215 | Pre-full-survey (was 528 candidates, now 989) |
| Benchmark Survey | 20260215 | Was partial (~827 candidates), now 989 |
| LLM Assessment | 20260215 | Minor (pre-dedup count) |
| Religious Gap | 20260215 | Scope was pre-culture import |
| Both Dashboards | 20260215 | All stale data |

**CRITICAL:** Never overwrite existing `20260215-` reports. The scripts should already point to `20260216-` output paths.

---

## Priority 2 — Download Remaining 54 Bot-Blocked PDFs

**Status:** Needs manual browser download
**Effort:** Manual, ~1-2 hours

54 of the 74 discovered PDF URLs returned HTTP 403 or HTML landing pages when fetched by script. These publishers block automated downloads.

**Data:** `logs/20260216-pdf_download_results.json`

### Bot-blocked source breakdown:
| Source | Count | Notes |
|--------|-------|-------|
| MDPI | 15 | Open access but bot-protected |
| ACM | 6 | Requires institutional access |
| DOI.org | 6 | Redirects to publisher |
| IEEE | 4 | Requires institutional access |
| ScienceDirect | 4 | Requires institutional access |
| Other | 19 | Mixed publishers |

### After manual download:
1. Save PDFs to `Lit-WS-PDFs/YYYY/` (year-based subdirectory)
2. Extract text: `/extract-pdf-text` skill or `PYTHON/extract_pdf_text.py`
3. Update YAML: set `local_pdf` wikilink and `pdf_extract` path

### Also pending:
- **Ochasi PDF** (1 paper): `https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/dewb.70007`
  Save to: `Lit-WS-PDFs/2025/2025-Ochasi-Reframing Justice in Healthcare AI.pdf`

---

## Priority 3 — Data Quality Gaps (Lower Priority)

### 3a. Unknown Authors — 16 remaining
All 16 are institutional/non-academic content with legitimately no individual author. No action needed unless you want to adopt a standardized institutional authorship format (e.g., `[[Organization Name]]`).

### 3b. PDF Audit — 4 "File Not Found" entries
4 papers still have `[[Unknown]]` in their wikilinks and no matching PDF on disk:
- `2026-[[Unknown]]-Qalb Largest State-of-the-Art Urdu Large Language.md`
- `2025-[[Unknown]]-Creating and Evaluating Code-Mixed Nepali-English and.md`
- `2026-[[Unknown]]-UrduBench An Urdu Reasoning Benchmark using.md`
- `2025-[[Unknown]]-Alif Advancing Urdu Large Language Models.md`

These are subset of the 16 `[[Unknown]]` papers. If authors can be identified, run `apply_author_fixes.py` to rename.

### 3c. Unquoted Wikilinks — 155 local_pdf + 44 first_author
Legacy entries without YAML quotes. Validation passes, Obsidian works fine. Cosmetic inconsistency only. Low priority.

### 3d. `languages_list` backfill — ~1,143 papers (57.1%)
Field was added during culture enrichment wave but only populated for papers that went through that pipeline. Could use 20-agent swarm pattern to backfill.

---

## Priority 4 — Religious Tradition Search (Workstream B)

**Status:** NOT STARTED
**Effort:** Multi-agent search + import pipeline

4 zero-benchmark traditions need targeted paper searches:
- Shinto
- Baha'i
- Zoroastrian
- Indigenous spiritual traditions

**Expected yield:** 20-50 new papers
**Reference:** `STATISTICS/20260215-religious-ethical-tradition-gap-analysis.md`

**Search venues:**
- HuggingFace model/dataset cards
- ACL workshops (NLP for religious texts)
- AfricaNLP, Deep Learning Indaba proceedings
- Japanese NLP venues (Shinto)
- Religious studies + AI ethics crossover journals

---

## Recommended Session Order

| Step | Task | Type | Est. Effort |
|------|------|------|-------------|
| 1 | Regenerate 5 reports | Scripts | 15 min |
| 2 | Push dashboards to GitHub Pages | Manual | 10 min |
| 3 | Manual PDF downloads (54 bot-blocked) | Browser | 1-2 hours |
| 4 | `languages_list` backfill (1,143 papers) | 20-agent swarm | 30 min |
| 5 | Religious tradition search | Multi-agent | 1+ hour |

Steps 1-2 are highest value — they unlock the full benchmark survey results for the dashboards.

---

## Key File References

### Scripts (all in `CEI-Lit-WS/PYTHON/`)
| Script | Purpose |
|--------|---------|
| `generate_vault_overview_report.py` | Main vault report |
| `generate_vault_dashboard.py` | Interactive HTML dashboard |
| `generate_values_alignment_report.py` | Values/alignment analysis |
| `generate_benchmark_survey_report.py` | Benchmark survey report |
| `generate_llm_assessment_report.py` | LLM assessment report |
| `generate_tradition_gap_report.py` | Religious tradition gap analysis |
| `download_discovered_pdfs.py` | PDF download (supports `--start` for resume) |
| `fix_local_pdf_fields.py` | Fix blank/broken local_pdf (3 categories) |
| `fix_data_url_formatting.py` | Fix bare DATA_URL values |
| `apply_author_fixes.py` | Apply author corrections + renames |
| `validate_all_papers.py` | Validate all 2,002 papers |
| `audit_pdf_links.py` | Audit PDF link integrity |

### Data & Logs (all in `CEI-Lit-WS/logs/`)
| File | Contents |
|------|----------|
| `20260216-benchmark_survey_all_classifications.json` | All 2,002 survey results |
| `20260216-benchmark_survey_candidates.json` | 989 benchmark candidates |
| `20260216-culture_list_consolidation.json` | Culture/nationality data |
| `20260216-missing_pdfs_discovered.json` | 74 discovered PDF URLs |
| `20260216-pdf_download_results.json` | Download results (20 success, 54 fail) |
| `20260216-unknown_authors_resolved.json` | 70 resolved authors (applied) |
| `benchmark_survey_round3_batches/` | Round 3 agent batch inputs + results |

### Memory Files (in `~/.claude/projects/.../memory/`)
| File | Contents |
|------|----------|
| `MEMORY.md` | Master memory (loaded into every session) |
| `outstanding-tasks.md` | Outstanding task tracker (post-Session 85) |
| `benchmark-survey-pipeline.md` | Benchmark pipeline docs |
| `llm-assessment-pipeline.md` | LLM assessment docs |
| `report-generation.md` | Report generation docs |

---

## Critical Rules Reminder

1. **Report immutability:** NEVER overwrite existing reports. Always create new files with new date prefixes.
2. **YAML safety:** NEVER use `parse_frontmatter()` -> `rebuild_frontmatter()` round-trip. Use regex-based field replacement.
3. **File deletion:** NEVER use `rm`. Always `mv` to `RECYCLE-BIN/`.
4. **Validation:** Always run `validate_all_papers.py` after any batch YAML modifications.
5. **Parallel agents:** Verify result file freshness before consolidating. Rate-limited agents leave stale data.
6. **PDF paths:** Use `rglob("*.pdf")` not `glob("*.pdf")` — PDFs are in year-based subdirs. But use `iterdir()` if filenames may contain brackets (`[[Unknown]]`).

---

*Generated 2026-02-16 at end of Session 85.*
