# Plan: Exhaustive Language-Organized LLM Cultural Values Benchmark Search

## Context

The CEI Literature Vault (846 papers) has strong coverage for Chinese (31+ benchmarks) and English, moderate coverage for Arabic/Japanese/Korean, but **zero dedicated benchmarks** for Hindi (600M speakers), Tamil, Telugu, Urdu, Malay, Turkish, and dozens more languages. The previous exhaustive search (Feb 7, 2026) was organized by *topic/venue* using 19 agents — this new search will be organized by *language* to systematically close the coverage gaps. New papers will include a `languages_list` YAML field listing all languages covered in each paper.

---

## Phase 1: Agent Swarm Search (25 agents, 5 waves of 5)

### Agent Organization

Each agent receives a language group and runs **8 search queries per language** via `WebSearch`, recording structured results. Agents are prioritized by coverage gap severity.

#### Wave 1 — HIGH PRIORITY (zero/minimal vault coverage)

| Agent | Languages | Rationale |
|-------|-----------|-----------|
| A1 | Hindi, Urdu, Nepali, Marathi | 0 benchmarks, 1B+ speakers combined |
| A2 | Tamil, Telugu, Kannada, Malayalam | 0 benchmarks, 300M+ speakers (Dravidian family) |
| A3 | Turkish, Azerbaijani, Kazakh, Uzbek | 0 benchmarks (Turkic family) |
| A4 | Thai, Lao, Khmer, Burmese | 0-2 benchmarks (Mainland SEA) |
| A5 | Swahili, Yoruba, Hausa, Igbo, Amharic, Zulu, Twi, Wolof, Somali | Minimal — only IrokoBench covers some |

#### Wave 2 — HIGH PRIORITY (continued)

| Agent | Languages | Rationale |
|-------|-----------|-----------|
| A6 | Indonesian, Malay, Filipino/Tagalog, Javanese, Sundanese | 3 benchmarks total (Maritime SEA) |
| A7 | Persian/Farsi, Kurdish, Pashto | 2 benchmarks (Iranian languages) |
| A8 | Bengali, Sinhala, Assamese, Odia | 2 benchmarks only (Eastern South Asian) |
| A9 | Portuguese, Galician | Minimal coverage, 260M+ speakers |
| A10 | Hebrew, Yiddish | Minimal, distinct research ecosystem |

#### Wave 3 — MODERATE PRIORITY (some coverage, likely missed papers)

| Agent | Languages | Rationale |
|-------|-----------|-----------|
| B1 | Korean | 4 benchmarks, significant research scene |
| B2 | Spanish (Iberian + Latin American variants) | 3 benchmarks, needs expansion |
| B3 | Russian, Ukrainian, Belarusian, Bulgarian | 3 benchmarks (Slavic East) |
| B4 | Polish, Czech, Slovak, Serbian, Croatian, Slovenian | 0 benchmarks (Slavic West/South) |
| B5 | Vietnamese | 1-2 benchmarks, growing NLP community |

#### Wave 4 — MODERATE PRIORITY (continued)

| Agent | Languages | Rationale |
|-------|-----------|-----------|
| B6 | French (European + Francophone African + Quebecois) | 4 benchmarks, needs dialect coverage |
| B7 | German, Dutch, Danish, Swedish, Norwegian, Finnish, Icelandic | 3 benchmarks (Germanic/Nordic) |
| B8 | Italian, Romanian, Catalan, Basque | Minimal (Romance + isolate) |
| B9 | Greek, Georgian, Armenian, Albanian, Maltese | 0 benchmarks (European minority) |
| B10 | Mongolian, Tibetan, Uyghur, Kyrgyz | 0 benchmarks (Central/Inner Asian) |

#### Wave 5 — COMPLETENESS + CROSS-CUTTING

| Agent | Languages | Rationale |
|-------|-----------|-----------|
| C1 | Chinese (Mandarin, Cantonese, Classical, Min, Hakka) | Well-covered but check for new 2025-2026 papers |
| C2 | Japanese + Arabic (MSA + dialects) | Well-covered but check for new papers |
| D1 | Multilingual benchmarks (5+ languages) | Cross-cutting: MMLU, MEGA, Belebele, etc. |
| D2 | Low-resource / Indigenous (Quechua, Guarani, Māori, Welsh, Irish, Hawaiian, Navajo, Inuktitut) | Likely sparse but important for gap analysis |
| D3 | Code-switching / Transliteration / Dialectal (Hinglish, Spanglish, Arabizi, Romanized scripts) | Emerging research area |

### Search Query Template (per language L)

Each agent runs these 8 queries via `WebSearch` for EACH language in its group:

```
1. "{L} LLM benchmark cultural values evaluation"
2. "{L} language model ethics moral reasoning benchmark"
3. "{L} NLP dataset bias fairness evaluation"
4. "{L} AI safety benchmark toxicity hate speech"
5. "{L} large language model alignment values assessment"
6. "multilingual benchmark evaluation {L} values"
7. "{L} LLM evaluation dataset 2024 2025 2026"
8. site:arxiv.org OR site:aclanthology.org "{L}" benchmark values LLM
```

Plus language-specific supplementary queries:
- Native script variants (e.g., "हिंदी LLM बेंचमार्क", "アラビア語 LLM ベンチマーク")
- Regional conference venues (e.g., ROCLING for Chinese, PACLIC for Asian, AfricaNLP for African)
- HuggingFace dataset searches: `site:huggingface.co/datasets {L} values OR ethics OR moral OR bias`

### Agent Output Format

Each agent produces a structured JSON report:

```json
{
  "agent_id": "A1",
  "languages": ["Hindi", "Urdu", "Nepali", "Marathi"],
  "papers_found": [
    {
      "title": "...",
      "authors": "...",
      "year": 2025,
      "url": "https://...",
      "arxiv_id": "2501.12345",
      "doi": "10.1234/...",
      "languages_covered": ["Hindi", "English"],
      "benchmark_name": "HindiBench",
      "abstract_snippet": "...",
      "source": "Google Scholar / arXiv / ACL Anthology",
      "data_url": "https://huggingface.co/...",
      "relevance_notes": "..."
    }
  ],
  "search_queries_used": [...],
  "total_found": 15,
  "already_in_vault": ["2024-Author-Title.md", ...]
}
```

---

## Phase 2: Consolidation & Deduplication

### Step 2a: Merge Agent Reports → Master List

Script: **`PYTHON/consolidate_language_search.py`** (new)

1. Load all 25 agent JSON reports from `logs/`
2. Merge into unified list
3. Deduplicate within the new results (DOI → arXiv ID → 85% title word-overlap)
4. Cross-reference against existing 846 vault papers using:
   - DOI match
   - arXiv ID match (with YYMM prefix validation to avoid false matches)
   - Normalized title similarity (≥85% word overlap)
5. Output: `logs/20260213-language_search_master_list.json`
6. Output: `logs/20260213-language_search_master_list.md` (human-readable)

### Step 2b: Cross-Verification

- Spot-check 20 random papers from the master list
- Verify: paper exists, title/authors correct, URL works, language claim accurate
- Output: `logs/20260213-language_search_cross_verification.md`

---

## Phase 3: Import New Papers

### Step 3a: Create Paper Files

Script: **`PYTHON/import_language_search_papers.py`** (new, adapts existing import logic)

For each new paper:
1. Generate filename: `YYYY-FirstAuthor-ShortTitle.md`
2. Create YAML frontmatter with all standard fields + new `languages_list` field
3. Create markdown body (title, authors, metadata, links)
4. Validate YAML with `validate_frontmatter()`
5. Set `DATE_ADDED: 20260213`

### Step 3b: Download PDFs

Reuse: **`PYTHON/comprehensive_pdf_finder.py`** (15-strategy waterfall)
- ArXiv papers: direct PDF download
- DOI papers: Unpaywall → publisher → Semantic Scholar → OpenAlex
- Rate limits: arXiv 3s, Semantic Scholar 10s, others per existing config
- Parallel: 5 background processes with START/END ranges

### Step 3c: Extract PDF Text

Reuse: **`PYTHON/batch_extract_pdfs.py`**
- `pdftotext` extraction to `PDF Extracts/YYYY/` directory
- Year-based subdirectory layout per existing convention

### Step 3d: Classify

Reuse: 7-stage classification pipeline
- `classify_ethics.py` (stages 1-2)
- `classify_ethics_perspective.py` (stage 3)
- `classify_non_ethics_topics.py` (stage 4)
- `classify_cultural_religious.py` (stage 5)
- `classify_moral_psych.py` (stage 6)
- `classify_data_nature.py` (stage 7)

---

## Phase 4: `languages_list` YAML Field

### Field Specification

```yaml
languages_list: "Hindi, English, Urdu"
```

- **Key:** `languages_list`
- **Type:** Comma-separated string (consistent with `LLM_assessed`, `newtags`)
- **Position:** After `national_ethnic_cultural` field
- **Values:** Standardized language names (English, not ISO codes)
- **For multilingual papers:** List ALL languages covered (e.g., "English, Chinese, Arabic, Hindi, Swahili")
- **For English-only papers:** `"English"` or `"N/A"` if language is not the focus

### For NEW papers (automatic during import)

The import script (`import_language_search_papers.py`) will include `languages_list` directly from the agent reports' `languages_covered` field.

### For EXISTING 846 papers (backfill — Phase 4b)

A separate agent swarm (10 agents × ~85 papers each) will read each existing paper's abstract, title, `national_ethnic_cultural` field, and PDF extract to determine the languages covered, then insert `languages_list` using safe regex insertion:

**Script:** `PYTHON/backfill_languages_list.py` (new)

1. **Generate batches:** Split 846 papers into 10 batch files (JSON manifests)
2. **Agent swarm (10 agents, 2 waves of 5):** Each agent reads paper content and determines:
   - Languages explicitly mentioned as being evaluated/benchmarked
   - Languages of datasets used
   - If paper is English-only theoretical/survey with no language-specific evaluation → `"English"` or `"N/A"`
3. **Consolidation:** `PYTHON/consolidate_languages_backfill.py` applies the field using safe regex:

```python
# Safe insertion pattern (preserves all other YAML lines)
re.subn(
    r'^(national_ethnic_cultural:.*$)',
    r'\1\nlanguages_list: "{languages}"',
    frontmatter, count=1, flags=re.MULTILINE
)
```

4. **Validation:** Run `validate_all_papers.py` to confirm 0 errors

---

## Phase 5: Reporting & Dashboard Update

1. **Language Coverage Report:** `STATISTICS/20260213-language-coverage-report.md`
   - Before/after comparison by language
   - Gap analysis: languages with still-zero benchmarks
   - Language × benchmark-type matrix

2. **Update Vault Overview:** Regenerate `STATISTICS/20260213-vault-overview-report.md` with new language section

3. **Update Dashboard:** Add language coverage visualization to dashboard

---

## Execution Timeline

| Step | Action | Parallelism | Est. Papers |
|------|--------|-------------|-------------|
| Wave 1 | Agents A1-A5 (South Asian, SEA, Turkic, African) | 5 parallel | ~40-80 new |
| Wave 2 | Agents A6-A10 (Maritime SEA, Iranian, Bengali, Portuguese, Hebrew) | 5 parallel | ~30-60 new |
| Wave 3 | Agents B1-B5 (Korean, Spanish, Slavic, Vietnamese) | 5 parallel | ~25-50 new |
| Wave 4 | Agents B6-B10 (French, Germanic, Romance, European, Central Asian) | 5 parallel | ~20-40 new |
| Wave 5 | Agents C1-C2, D1-D3 (completeness + cross-cutting) | 5 parallel | ~30-60 new |
| Consolidation | Dedup + cross-verify | Sequential | — |
| Import | Create files, PDFs, extracts, classify | 5 parallel batches | — |
| Backfill | Add `languages_list` to existing 846 papers | 10 agents (2×5) | 846 enriched |
| **Total estimated** | | | **~100-250 new + 846 backfilled** |

---

## Verification & QC

1. **YAML validation:** `../.venv/bin/python PYTHON/validate_all_papers.py` — must pass 100%
2. **languages_list audit:** Spot-check 30 papers to verify language labels are accurate
3. **Dedup verification:** Ensure 0 duplicates were imported
4. **PDF link verification:** `python3 PYTHON/audit_pdf_links.py` — no broken links
5. **Report regeneration:** Re-run all report generators to incorporate new data

---

## Key Files to Create/Modify

### New Scripts
- `PYTHON/consolidate_language_search.py` — Merge agent reports, dedup, master list
- `PYTHON/import_language_search_papers.py` — Create paper .md files with `languages_list`
- `PYTHON/backfill_languages_list.py` — Batch generator for existing paper enrichment
- `PYTHON/consolidate_languages_backfill.py` — Apply `languages_list` to existing papers

### Reused Scripts (no changes)
- `PYTHON/comprehensive_pdf_finder.py` — PDF acquisition
- `PYTHON/batch_extract_pdfs.py` — Text extraction
- `PYTHON/validate_all_papers.py` — Validation
- `PYTHON/classify_*.py` — 7-stage classification

### Modified Scripts
- `PYTHON/validate_all_papers.py` — Add `languages_list` to accepted fields (if validation is strict)
- `PYTHON/generate_vault_overview_report.py` — Add language coverage section
- `PYTHON/generate_vault_dashboard.py` — Add language visualization tab

### Output Files
- `logs/20260213-language_search_agent_*.json` — 25 agent reports
- `logs/20260213-language_search_master_list.json` — Consolidated master list
- `logs/20260213-language_search_master_list.md` — Human-readable version
- `logs/20260213-language_search_cross_verification.md` — Spot-check results
- `STATISTICS/20260213-language-coverage-report.md` — Final report
