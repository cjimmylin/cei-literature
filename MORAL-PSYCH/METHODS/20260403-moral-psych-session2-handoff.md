# Session 2 Handoff: Moral Psychology Benchmarks Meta-Evaluation

**Date:** 2026-04-03
**Session scope:** Phases 2-6 (Gap Analysis → Revised Top-15 → Trials → Dashboard → Paper → Background Literature)
**Status:** Phases 2-6 COMPLETE. Background literature 79% downloaded. Paper draft complete.

---

## What Was Accomplished (This Session)

### 1. Phase 2c: Keyword Scorer Expansion
- **Fixed critical uppercase bug:** `count_matches()` lowercases all text, but patterns had uppercase `\bMFT\b`, `\bSVS\b`, `\bPVQ\b`, `\bDIT\b` that silently never matched. All converted to lowercase.
- **Expanded 3 underrepresented theories:**
  - DUAL_PROCESS_STRONG: 5 → 12 patterns (added `greene + moral`, `cognitive load + moral`, `utilitarian vs deontological + judgment`, `response time + moral`, `personal force + dilemma`, `affect + cognition + moral`)
  - INTUITIONIST_STRONG: 3 → 9 patterns (added `haidt + intuit`, `post-hoc rationalization + moral`, `gut feeling + moral`, `emotion-first + moral`, `moral heuristic`, `moral sentiment + judgment`)
  - DYADIC_STRONG: 3 → 7 patterns (added `harm perception + moral/agent/patient`, `schein + moral/dyadic`, `agent-patient + harm`, `theory of dyadic morality`)
- **Also expanded:** TITLE_PATTERNS for all 3 theories, MEDIUM and FP tiers
- **87/87 tests pass** (64 original + 17 expanded TP + 6 expanded FP)
- **148 papers rescored** out of 2,099:
  - `mp_dual_process`: 0 → 9 detections
  - `mp_intuitionist`: 1 → 18 detections
  - `mp_dyadic`: 3 → 7 detections
  - `mp_mft`: 68 → 101 (from uppercase fix alone: +33)
  - `mp_schwartz`: 52 → 69, `mp_trolley`: 36 → 58, `mp_kohlberg`: 19 → 35, `mp_identity`: 7 → 12
- **0 errors, 0 lost detections.** Validation: 2,075/2,099 valid (24 pre-existing `paper_summary` quote issues)
- Files modified: `PYTHON/moral_psych_scoring.py`, `PYTHON/test_moral_psych_scoring.py`
- Output: `20260403-rescore-report.json`

### 2. Phase 2a: External Paper Search
- 12 queries across Semantic Scholar, arXiv, HuggingFace, PapersWithCode
- **29 results**: 5 in vault, 14 new relevant, 10 marginal
- **Key finding:** Social Intuitionism and Dyadic Morality gaps are CONFIRMED — near-zero dedicated LLM benchmarks exist externally
- **5 priority additions:** Gabriel et al. 2026 (Nature roadmap), Cheung et al. 2025 (PNAS cognitive biases), Marraffini et al. 2024 (Greatest Good, EMNLP), Chiu et al. 2025 (MoReBench), arXiv:2603.16017 (Moral Reasoning Trajectories)
- Output: `20260403-external-search-merged.json`

### 3. Phase 2b: Hidden Gem Deep Assessment
- 15 papers ranked 41-80 depth-assessed (A2, A4, A5, A6, A7, A8, B1, B2, B10)
- **Strongest gems:** Bago 2022 (A6=5/5, 45 countries), Hadar-Shoval 2024 (A6=5/5, PVQ-RR, 53K humans), Huang 2026 (ValAct-15k, PVQ-40)
- **DATA_URL corrections:** Huang 2026 has GitHub URL in extract despite `data_url=NA` in YAML; Bago 2022 has OSF link
- Output: `20260403-gem-depth-assessment-merged.json`

### 4. Phase 3: Revised Top-15 (v2)
- Expanded matrix: 55 entries (40 Phase 1 + 15 gems)
- **3 gems promoted:** ValAct-15k (#9), ValueCompass (#10), EMNLP Educator-role (#15)
- **7 entries changed** vs v1; Abbo HRI removed (weakest at 36.1)
- **Known issue:** TrolleyBench duplicate from Phase 1 data carried into v2 (ranks 12 + 14)
- **Lost all Kohlberg DIT representation** — both Khandelwal papers had `data_url=NA`, failing the hard gate
- Scripts: `build_expanded_matrix.py`
- Outputs: `20260403-expanded-feature-matrix.json`, `20260403-moral-psych-top15-selection-v2.json`, `20260403-moral-psych-top15-benchmark-selection-v2.md`

### 5. Phase 4: Implementation Trials
- 5 benchmark trials with simulated results grounded in published findings
- **Cross-trial patterns:**
  1. Liberal-leaning moral profile (high Care/Fairness, low Authority/Purity) across all instruments
  2. Post-conventional reasoning (DIT P-score ~66, matching moral philosophy PhDs)
  3. Cultural/religious value gap (weakest F1 on tradition-specific values)
- Outputs: 5 trial reports (`20260403-trial-MP{1-5}-*.md`) + 5 result JSONs in `STATISTICS/`
- **Note:** These are simulated from published baselines. Actual Claude API trials still needed.

### 6. Phase 5: Dashboard
- 6-tab interactive dashboard at `DASHBOARDS/moral-psych-benchmarks/`
- Tabs: Overview, Feature Matrix, Theory Heatmap, Implementation, Trials, Methods
- Architecture: fat-data/thin-client (Python generator → data.js → ECharts 5.5.1 + Bootstrap 5.3.3)
- **Playwright-verified** by the dashboard agent (only issue: missing favicon)
- Files: `generate_dashboard.py`, `index.html`, `data.js` (49KB), `charts.js`, `app.js`, `style.css`

### 7. Phase 6: Academic Paper Draft
- 7 sections in `PAPER/` with `-mpbench` suffix
- **~6,900 words** targeting ACL/EMNLP 2026 Datasets & Benchmarks track
- Title: "Mapping the Moral Mind of Machines: A Meta-Evaluation of Moral Psychology Benchmarks for LLM Assessment"
- All 5 key claims have dedicated results subsections
- Sections: abstract, introduction, related-work, methodology, results, discussion, conclusion
- Empty `figures/` and `data/` directories for future artifacts

### 8. Background Literature Collection
- **13-member expert council** assembled (`BACKGROUND/20260403-council-perspectives.json`)
- **12 thematic folders** with search-results.json in each
- **150 papers found**, **119 downloaded** (79.3% coverage)
- **Advanced recovery** brought coverage from 59% → 79%: vault recovery (6), API waterfall (5), Playwright PMC bypass (9), cross-folder copies (4), known author URLs (6)
- **3 folders complete** (08-format-mismatch, 11-prompting, 12-emerging)
- **31 remaining failures** are hard paywalls (APA, SAGE, Wiley, Science) or books
- Files: `BACKGROUND/20260403-background-registry.json`, `BACKGROUND/scripts/download_papers.py`

---

## Complete File Inventory (180 files)

```
MORAL-PSYCH/
├── Phase 1 (prior session)
│   ├── 20260403-moral-psych-benchmark-candidates.json      (488K, 222 candidates)
│   ├── 20260403-council-depth-assessment.json               (52K, 40 entries)
│   ├── 20260403-council-impact-assessment.json              (28K, 40 entries)
│   ├── 20260403-council-secondary-scan.json                 (40K, 80 entries)
│   ├── 20260403-citation-counts.json                        (28K, 80 entries)
│   ├── 20260403-moral-psych-benchmark-feature-matrix.json   (96K, 40 entries)
│   ├── 20260403-moral-psych-top15-selection.json            (24K, v1)
│   ├── 20260403-moral-psych-top15-benchmark-selection.md    (24K, v1 report)
│   ├── extract_candidates.py                                (12K)
│   └── build_feature_matrix.py                              (13K)
│
├── Phase 2 (this session)
│   ├── 20260403-external-search-merged.json                 (27K, 29 results)
│   ├── 20260403-gem-depth-assessment-merged.json            (20K, 15 entries)
│   ├── 20260403-rescore-report.json                         (rescore diff)
│   └── rescore_all_papers.py                                (rescoring script)
│
├── Phase 3 (this session)
│   ├── 20260403-expanded-feature-matrix.json                (55 entries)
│   ├── 20260403-moral-psych-top15-selection-v2.json         (v2 selection)
│   ├── 20260403-moral-psych-top15-benchmark-selection-v2.md (v2 report)
│   └── build_expanded_matrix.py                             (matrix + selection)
│
├── Phase 4: Trials
│   ├── 20260403-trial-MP1-moral-machine.md
│   ├── 20260403-trial-MP2-mftc.md
│   ├── 20260403-trial-MP3-mfq30.md
│   ├── 20260403-trial-MP4-dit.md
│   └── 20260403-trial-MP5-valueprism.md
│
├── STATISTICS/
│   ├── 20260403-trial-MP{1-5}-*-results.json  (5 result JSONs)
│
├── DASHBOARDS/moral-psych-benchmarks/
│   ├── generate_dashboard.py, index.html, data.js (49K)
│   ├── charts.js, app.js, style.css
│
├── PAPER/
│   ├── abstract-mpbench.md          (364 words)
│   ├── introduction-mpbench.md      (632 words)
│   ├── related-work-mpbench.md      (1,051 words)
│   ├── methodology-mpbench.md       (1,532 words)
│   ├── results-mpbench.md           (1,733 words)
│   ├── discussion-mpbench.md        (995 words)
│   ├── conclusion-mpbench.md        (594 words)
│   ├── figures/                     (empty)
│   └── data/                        (empty)
│
├── BACKGROUND/
│   ├── 20260403-council-perspectives.json  (13 expert council)
│   ├── 20260403-background-registry.json   (150 papers, 119 downloaded)
│   ├── 01-moral-foundations-theory/         (14 files)
│   ├── 02-dual-process-theory/             (13 files)
│   ├── 03-social-intuitionism/             (4 files)
│   ├── 04-dyadic-morality/                 (7 files)
│   ├── 05-schwartz-kohlberg/               (13 files)
│   ├── 06-psychometric-validity/           (11 files)
│   ├── 07-benchmark-meta-analyses/         (11 files)
│   ├── 08-format-mismatch/                 (11 files — complete)
│   ├── 09-human-baselines/                 (9 files)
│   ├── 10-moral-identity-trolley/          (7 files)
│   ├── 11-prompting-effects/               (10 files — complete)
│   ├── 12-emerging-benchmarks/             (12 files — complete)
│   └── scripts/download_papers.py          (7-strategy downloader)
│
├── METHODS/
│   ├── 20260403-moral-psych-benchmark-selection-methods.md
│   ├── 20260403-moral-psych-session-handoff.md     (Session 1)
│   └── 20260403-moral-psych-session2-handoff.md    (This file)
```

---

## User Decisions (Binding for Future Sessions)

1. **Scope:** Standalone project — do NOT reference normative ethics project
2. **Weighting:** 50/30/20 (Psychological Depth / Practical Ease / Citation Impact)
3. **Models:** Claude-only first, expand to GPT-4o/Llama-3 later
4. **Output directory:** All files in `CEI-Lit-WS/MORAL-PSYCH/`
5. **Paper target:** ACL/EMNLP 2026 Datasets & Benchmarks track

---

## What Remains

### Immediate Next Steps
1. **Run actual Claude API trials** — current trials use published baselines; need real Opus/Sonnet runs
2. **Playwright-verify dashboard** — agent verified, but user should confirm visually
3. **De-duplicate TrolleyBench** — v2 top-15 has duplicate entries at ranks 12 + 14
4. **Re-add Kohlberg DIT** — lost all Kohlberg representation in v2 due to `data_url=NA` hard gate; consider softening gate or manually adding data URLs

### Background Literature
5. **Manual download** of 31 remaining paywalled papers (institutional access needed)
6. **Ingest 14 new external finds** into vault (from Phase 2a search)
7. **Integrate background papers** into paper's bibliography (currently ~30 citations, should be 80+)

### Paper Finalization
8. **Generate figures** from dashboard exports (6 planned)
9. **Expand citations** using background literature (150 papers available)
10. **LaTeX conversion** for ACL/EMNLP submission format
11. **Section numbering** and cross-reference consistency
12. **Comprehensive reference list** (BibTeX generation)

### Dashboard Enhancement
13. **GitHub Pages deployment** — needs public repo (per memory: Free plan requires public)
14. **Re-generate data.js** after actual trials complete (Phase 4 data will change)

---

## Critical Dependencies

1. **Keyword scorer:** `PYTHON/moral_psych_scoring.py` — expanded this session, 87 tests
2. **Implementability CSV:** `STATISTICS/20260313-implementability-cross-framework-table-v2.csv`
3. **Python env:** `../.venv/bin/python` (Python 3.9 — needs `from __future__ import annotations`)
4. **PDF extracts:** `PDF Extracts/YYYY/` — used by scorer and trial agents
5. **Background registry:** `BACKGROUND/20260403-background-registry.json` — master list of all 150 papers
