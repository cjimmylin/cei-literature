# Cross-Cultural AI Values Alignment — Session 3 Handoff

**Date:** 2026-04-04
**Session:** Introduction/literature review writing + post-writing cleanup + gold standard validation
**Project:** `CEI-Lit-WS/CULTURAL-GLOBAL/`
**GitHub Pages:** https://cjimmylin.github.io/cei-cultural-global/
**Dashboard repo:** https://github.com/cjimmylin/cei-cultural-global
**Previous handoff:** `METHODS/20260403-session-2-handoff.md` (Session 2: priorities + background)
**Intro handoff:** `PAPER/20260404-intro-litreview-handoff.md` (detailed writing process)

---

## What Was Done This Session

Two major work blocks: (1) comprehensive introduction and literature review writing via council-guided parallel agents, and (2) post-writing cleanup including reference updates, archival, dashboard push, and gold standard validation.

---

## Block 1: Introduction & Literature Review (12,150 words)

### Pipeline
```
Phase 0: Spine document → spine-cultural-global.md
Phase 1-2: 4 parallel writing agents (section1 + section2 parts 1-3)
Phase 3: 12-member expert council deliberation (50 recommendations)
Phase 4: Assembly + revision → introduction-cultural-global.md
Phase 5: Handoff document
```

### Canonical File
`PAPER/introduction-cultural-global.md` — **12,150 words**, replaces old `01-introduction.md` (1,000w) and `02-background.md` (1,500w).

### Section Structure
| Section | Words | Content |
|---------|-------|---------|
| **1. Introduction** | ~2,700 | Hook (RLHF pipeline → 5 traditions), stakes, WEIRD problem, gap, 5 RQs, 4 contributions |
| **2.1** WEIRD Critique | ~900 | Henrich, Markus/Kitayama, Gelfand, Shweder/Haidt, Awad Moral Machine |
| **2.2** AI Ethics Landscape | ~900 | Jobin 84 guidelines, Mittelstadt critique, second-gen operationalization |
| **2.3** Alignment Pipeline | ~1,400 | **NEW** — Gabriel, RLHF, Constitutional AI, Sorensen pluralism, corporate concentration, labor |
| **2.4** Non-Western Frameworks | ~3,100 | 7 traditions (Confucian, Ubuntu, Islamic, Buddhist, Dharmic, Indigenous, Buen Vivir) |
| **2.5** Decolonial AI | ~770 | Mohamed, epistemic extractivism, positionality acknowledgment |
| **2.6** Cross-Cultural Fairness | ~750 | Sambasivan, Selbst Portability Trap, impossibility results |
| **2.7** Contribution in Context | ~620 | 5 positioning moves + 4 extensions |

### Council
12 members (6 tradition + 6 methodological). 10 Critical + 23 Important + 17 Desirable recommendations. All Critical and Important applied. 2 minority reports (Floridi on principlist pragmatism; Gabriel on "no view from nowhere").

### Key New Content
- **Section 2.3 (Alignment Pipeline)** — traces where cultural values enter RLHF/Constitutional AI, including corporate concentration (OpenAI/Anthropic/Google/Meta) and labor dimension (Kenyan contractors, Perrigo 2023)
- **Positionality** — statement in Section 1.6 + detailed acknowledgment in Section 2.5
- **Anti-essentialization** — 0 violations in final file; internal diversity acknowledged for each tradition

---

## Block 2: Post-Writing Cleanup

### Task 1: References Updated
- `10-references.md`: 62 → **110 entries** (+48 new)
- All citations in `introduction-cultural-global.md` now have matching reference entries
- Coverage: alignment pipeline (Bai, Christiano, Ouyang), all 7 traditions, decolonial (Quijano, Grosfoguel), fairness (Selbst, Chouldechova), labor (Perrigo)

### Task 2: Files Archived
6 files moved to `PAPER/archive/`:
- `01-introduction-pre-rewrite.md` (original intro)
- `02-background-pre-rewrite.md` (original background)
- `section1-introduction.md` (intermediate draft)
- `section2-litreview-part1.md` (intermediate draft)
- `section2-litreview-part2.md` (intermediate draft)
- `section2-litreview-part3.md` (intermediate draft)

### Task 3: Dashboard Pushed
- Committed 14-tab update (dendrogram + CA biplot tabs) → `ba99e73`
- Pushed to `github.com/cjimmylin/cei-cultural-global` → GitHub Pages live
- 183 insertions, 12 deletions (index.html + data.js)

### Task 4: Gold Standard Validation (520 papers)

**The most significant methodological finding of this session.**

7 framework result files in `COUNCIL/20260404-gs-nw_*.json` + consolidated `20260404-gold-standard-results.json`.

| Framework | Precision | Recall | F1 | TP | FP | FN |
|-----------|-----------|--------|-----|----|----|-----|
| Islamic Ethics | **0.71** | 1.00 | **0.83** | 12 | 5 | 0 |
| Indigenous | 0.58 | 0.97 | 0.73 | 28 | 20 | 1 |
| Ubuntu | 0.50 | 1.00 | 0.67 | 11 | 11 | 0 |
| Dharmic | 0.20 | 1.00 | 0.33 | 2 | 8 | 0 |
| Buddhist | 0.19 | 1.00 | 0.32 | 3 | 13 | 0 |
| Buen Vivir | 0.17 | 1.00 | 0.29 | 1 | 5 | 0 |
| Confucian | 0.16 | 1.00 | 0.28 | 8 | 42 | 0 |
| **Mean** | **0.36** | **1.00** | **0.45** | **65** | **104** | **1** |

**Key Finding:** Near-perfect recall (0.995 mean) but low precision (0.358 mean). The dominant FP pattern is **NLP-on-tradition-texts**: papers that apply NLP tools TO Buddhist/Confucian/Hindu texts are conflated with papers that use those traditions' ethical frameworks AS analytical tools. This distinction — *studying a tradition's texts* vs *thinking with a tradition's ethics* — is the methodological crux.

**Precision-adjusted estimates change the narrative:**

| Framework | Raw Count | Precision-Adjusted |
|-----------|-----------|-------------------|
| Confucian | 86 | ~14 |
| Indigenous | 53 | ~31 |
| Islamic | 30 | ~21 |
| Ubuntu | 26 | ~13 |
| Buddhist | 26 | ~5 |
| Dharmic | 19 | ~4 |
| Buen Vivir | 9 | ~2 |
| **Total** | **249** | **~90** |

Non-Western philosophical engagement is even rarer than raw counts suggest — strengthening the paper's central argument.

---

## Files Created This Session

### New Files
| File | Location | Purpose |
|------|----------|---------|
| `spine-cultural-global.md` | `PAPER/` | Shared contract for parallel writing |
| `council-deliberation-intro-review.md` | `PAPER/` | 12-member council review (7,500w) |
| `introduction-cultural-global.md` | `PAPER/` | **Canonical intro + lit review (12,150w)** |
| `20260404-intro-litreview-handoff.md` | `PAPER/` | Writing process handoff |
| `20260404-gs-nw_confucian.json` | `COUNCIL/` | Confucian gold standard labels |
| `20260404-gs-nw_ubuntu.json` | `COUNCIL/` | Ubuntu gold standard labels |
| `20260404-gs-nw_islamic.json` | `COUNCIL/` | Islamic gold standard labels |
| `20260404-gs-nw_buddhist.json` | `COUNCIL/` | Buddhist gold standard labels |
| `20260404-gs-nw_dharmic.json` | `COUNCIL/` | Dharmic gold standard labels |
| `20260404-gs-nw_indigenous.json` | `COUNCIL/` | Indigenous gold standard labels |
| `20260404-gs-nw_buen_vivir.json` | `COUNCIL/` | Buen Vivir gold standard labels |
| `20260404-gold-standard-results.json` | `COUNCIL/` | Consolidated P/R/F1 results |
| `20260404-session-3-handoff.md` | `METHODS/` | This file |

### Modified Files
| File | Change |
|------|--------|
| `10-references.md` | +48 entries (62→110) |

### Archived Files (PAPER/archive/)
| File | Original |
|------|----------|
| `01-introduction-pre-rewrite.md` | Original thin intro |
| `02-background-pre-rewrite.md` | Original thin background |
| `section1-introduction.md` | Intermediate draft |
| `section2-litreview-part{1,2,3}.md` | Intermediate drafts |

---

## What Needs Doing Next

### Priority 1: Update Paper with Validation Results
- Add gold standard P/R/F1 table to Section 3 (Methodology)
- Report both raw and precision-adjusted counts throughout Sections 4-7
- Add discussion of NLP-on-texts FP pattern in Section 8 (Discussion) as methodological limitation
- Consider: the precision-adjusted numbers strengthen the WEIRD argument

### Priority 2: Remaining Desirable Council Revisions (11)
- D1: RLAIF/DPO mention for currency
- D2: Broaden Confucian section title
- D5-D9: Additional citations (Li 2006, Escobar 2018, Bietti 2020, Kukutai & Taylor 2016)
- D11: Political economy of AI ethics scholarship
- D12: Moderate self-congratulatory tone in 2.7
- D16-D17: Non-English citations, verb symmetry audit

### Priority 3: Keyword Scorer Improvement
The gold standard reveals systematic FP patterns that could be addressed:
- **Confucian:** Filter Chinese NLP benchmarks (ACLUE, C3Bench, etc.) that don't engage philosophy
- **Buddhist/Dharmic:** Distinguish "NLP on religious texts" from "ethics using religious frameworks"
- **Ubuntu:** Filter Ubuntu Linux references
- **Indigenous:** Filter "indigenous language" NLP without ethical framework

### Priority 4: LaTeX Conversion for Submission
- pandoc 3.9 + ACM acmart.cls template
- Build references.bib from 10-references.md
- Finalize figure placement
- Target: AIES 2027 or FAccT 2027

### Priority 5: Background Literature Expansion
- Use 44 EXTRACT files to deepen Section 2 citations
- Address council-identified gaps (Central Asian indigenous, East Asian Buddhist)
- 86 background papers still without PDFs (30 books, 56 paywalled)

---

## Reproducibility

### Introduction/Lit Review
Intermediate files preserved in `PAPER/archive/`. Council deliberation in `PAPER/council-deliberation-intro-review.md`. Spine contract in `PAPER/spine-cultural-global.md`.

### Gold Standard
Seed 42. Sample in `COUNCIL/20260403-gold-standard-sample.json`. Per-framework labels in `COUNCIL/20260404-gs-nw_*.json`. Consolidated in `COUNCIL/20260404-gold-standard-results.json`.

### Full Pipeline (from Session 2 handoff)
```bash
cd CEI-Lit-WS
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/score_nonwestern_frameworks.py
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/enrich_author_geography.py
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/score_weird.py
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/enrich_cultural_classification.py
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/analyze_regional_clusters.py
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/stats_clustering.py
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/stats_tests.py
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/correspondence_analysis.py
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/stats_bayesian.py
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/generate_cultural_dashboard.py
```

---

*Filed: 2026-04-04 | Session 3 | CULTURAL-GLOBAL/METHODS/*
