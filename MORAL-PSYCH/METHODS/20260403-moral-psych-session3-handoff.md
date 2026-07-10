# Session 3 Handoff: Moral Psychology Benchmarks Meta-Evaluation

**Date:** 2026-04-03
**Session scope:** Comprehensive Introduction & Literature Review writing
**Status:** Introduction and Related Work sections COMPLETE. PDFs generated.

---

## What Was Accomplished (This Session)

### 1. Convened 12-Member Writing Council
- Purpose-built for writing (not assessment): Narrative Architect, Moral Psychology Historian, MFT Deep Expert, Process Theories Specialist, Harm & Values Theorist, Developmental Psychologist, Psychometric Authority, Benchmark Landscape Surveyor, Format & Measurement Specialist, Cross-Cultural & Baseline Expert, Alignment & Training Effects Expert, Emerging Frontiers Scout
- Key design choices: merged related theories (dual-process + intuitionism, dyadic + Schwartz), added Narrative Architect and Historian roles absent from assessment council
- Output: `PAPER/20260403-writing-council.json`

### 2. Research Phase: All 12 Background Folders Read
- Read all 12 `search-results.json` files (150 papers' metadata: author, year, venue, abstract snippet, relevance, download status)
- Built comprehensive citation map across all folders
- Papers span: MFT (18), Dual Process (15), Social Intuitionism (12), Dyadic Morality (13), Schwartz/Kohlberg (18), Psychometric Validity (12), Benchmark Meta-Analyses (11), Format Mismatch (10), Human Baselines (10), Moral Identity/Trolley (9), Prompting Effects (10), Emerging Benchmarks (12)

### 3. Comprehensive Literature Review Written
- **File:** `PAPER/related-work-mpbench.md`
- **6,679 words** (was 1,051 — 6.4× expansion)
- **7 major sections, 18 subsections:**
  - 2.1 Moral Psychology: Theories of Moral Cognition (2,500 words)
    - 2.1.1 Content Theories (MFT, Schwartz, Moral Identity)
    - 2.1.2 Process Theories (Dual Process, Social Intuitionism)
    - 2.1.3 Structural Theories (Dyadic Morality, Kohlberg, Trolley)
    - 2.1.4 Synthesis: The Theory Space
  - 2.2 Computational Operationalization of Moral Psychology (1,500 words)
    - 2.2.1 NLP Adoption (2014–2024)
    - 2.2.2 LLM-Specific Moral Evaluation
    - 2.2.3 The Missing Operationalizations
  - 2.3 Psychometric Validity (1,000 words)
  - 2.4 Format Effects, Human Baselines, Measurement (1,000 words)
  - 2.5 Alignment Training and Prompting Effects (800 words)
  - 2.6 Emerging Benchmarks and Current Trajectory (800 words)
  - 2.7 Positioning This Work (400 words)
- **Novel organizational framework:** Content/Process/Structure tripartite classification of moral theories — argues MFT benchmarks measure only content, leaving process and structure unmeasured
- **Key argument:** "Infrastructure advantage" — MFT dominated NLP not because it's the best theory but because it had MFQ + MFTC (questionnaire + corpus), which other theories lacked

### 4. Comprehensive Introduction Written
- **File:** `PAPER/introduction-mpbench.md`
- **2,493 words** (was 632 — 3.9× expansion)
- **7 subsections:**
  - 1.1 The Stakes: LLMs in Moral Contexts
  - 1.2 The Landscape of Moral Psychology
  - 1.3 Why Theoretical Grounding Matters for LLM Evaluation
  - 1.4 The Research Gap
  - 1.5 This Paper: Five Claims (with empirical specifics)
  - 1.6 Contributions (4 items)
  - 1.7 Paper Organization
- All 5 claims have empirical numbers matching results-mpbench.md exactly
- Three practical risks articulated: Goodhart's Law, construct validity assumption, baseline-free evaluation

### 5. PDF Generation
- `PAPER/introduction-mpbench.pdf` — 5 pages, 92KB, Times New Roman
- `PAPER/related-work-mpbench.pdf` — 13 pages, 129KB, Times New Roman
- Generated via fpdf2 (pure Python, no LaTeX needed)
- Minor rendering limitations: em dashes as `---`, inline bold/italic stripped

---

## Complete File Inventory (Session 3 additions)

```
MORAL-PSYCH/PAPER/
├── 20260403-writing-council.json          (NEW — 12-member writing council)
├── introduction-mpbench.md                (REWRITTEN — 2,493 words, was 632)
├── introduction-mpbench.pdf               (NEW — 5 pages)
├── introduction-mpbench.html              (NEW — intermediate HTML)
├── related-work-mpbench.md                (REWRITTEN — 6,679 words, was 1,051)
├── related-work-mpbench.pdf               (NEW — 13 pages)
```

Total paper word count now: ~9,172 (intro + review) + ~4,854 (methodology + results + discussion + conclusion) = **~14,026 words**

---

## User Decisions (Binding for Future Sessions)

1. **Scope:** Standalone project — do NOT reference normative ethics project
2. **Weighting:** 50/30/20 (Psychological Depth / Practical Ease / Citation Impact)
3. **Models:** Claude-only first, expand to GPT-4o/Llama-3 later
4. **Output directory:** All files in `CEI-Lit-WS/MORAL-PSYCH/`
5. **Paper target:** ACL/EMNLP 2026 Datasets & Benchmarks track
6. **Comprehensiveness priority:** User explicitly prioritizes comprehensive coverage over brevity for intro/review

---

## What Remains

### Immediate Next Steps (from Session 2, still pending)
1. **Run actual Claude API trials** — current trials use published baselines; need real Opus/Sonnet runs
2. **De-duplicate TrolleyBench** — v2 top-15 has duplicate entries at ranks 12 + 14
3. **Re-add Kohlberg DIT** — lost all Kohlberg representation in v2 due to `data_url=NA` hard gate
4. **Playwright-verify dashboard** — agent verified, but user should confirm visually

### Background Literature (from Session 2, still pending)
5. **Manual download** of 31 remaining paywalled papers (institutional access needed)
6. **Ingest 14 new external finds** into vault (from Phase 2a search)
7. **Integrate background papers** into paper's bibliography (currently ~100+ citations in intro/review, should cross-reference with BibTeX)

### Paper Finalization
8. **Generate figures** from dashboard exports (6 planned)
9. **BibTeX generation** — compile full reference list from all cited papers
10. **LaTeX conversion** for ACL/EMNLP submission format
11. **Section numbering** and cross-reference consistency across all sections
12. **PDF rendering improvement** — current fpdf2 PDFs lack inline bold/italic; consider installing LaTeX or using pandoc with a proper engine

### Dashboard Enhancement (from Session 2)
13. **GitHub Pages deployment** — needs public repo (per memory: Free plan requires public)
14. **Re-generate data.js** after actual trials complete (Phase 4 data will change)

---

## Critical Dependencies

1. **Keyword scorer:** `PYTHON/moral_psych_scoring.py` — expanded Session 2, 87 tests
2. **Implementability CSV:** `STATISTICS/20260313-implementability-cross-framework-table-v2.csv`
3. **Python env:** `../.venv/bin/python` (Python 3.9 — needs `from __future__ import annotations`)
4. **PDF extracts:** `PDF Extracts/YYYY/` — used by scorer and trial agents
5. **Background registry:** `BACKGROUND/20260403-background-registry.json` — master list of all 150 papers
6. **Writing council:** `PAPER/20260403-writing-council.json` — 12-member council for intro/review design
7. **Background papers:** Raw PDFs/HTML in `BACKGROUND/{01-12}/` folders (NOT markdown extracts). Each folder has `search-results.json` with metadata.
