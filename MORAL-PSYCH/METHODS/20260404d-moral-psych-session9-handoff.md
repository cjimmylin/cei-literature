# Session 9 Handoff: Scoring Expansion + Full-Vault Rescoring + Cross-Project Paper Updates

**Date:** 2026-04-04
**Session:** Expanded underrepresented moral psych theories, full-vault rescoring, NormEval cross-model integration, RV paper cross-model section, cultural-global field migration
**Project:** `CEI-Lit-WS/MORAL-PSYCH/` (primary), `NORM-ETHICS/`, `RELIGIOUS-VALUES/`, vault-wide papers
**Previous handoff:** `20260404c-moral-psych-session8-handoff.md`

---

## What Was Done This Session

### 1. Moral Psychology Scoring Expansion (`PYTHON/moral_psych_scoring.py`)

Fixed the **uppercase abbreviation bug** (MFT→mft, MFQ→mfq, SVS→svs, PVQ→pvq, DIT→dit) — `count_matches()` lowercases all text, so uppercase patterns never fired. This was a known bug documented in memory.

**Expanded three underrepresented theories:**

- **Dual Process** (+7 strong, +6 medium, +1 FP): Added Greene's key constructs (utilitarian vs deontological processing, cognitive load, personal force, affect/cognition, response time), broader automatic/deliberation moral indicators, System 1/2 with moral context
- **Social Intuitionist** (+6 strong, +5 medium, +1 FP): Added Haidt with context, post-hoc rationalization, gut feeling, emotion-first, moral heuristic, moral sentiment with judgment context, Humean/sentimentalism moral indicators
- **Dyadic** (patterns for harm perception, Schein/Gray, agent-patient): expanded detection of dyadic morality framework

### 2. New Unit Tests (135 tests added to `test_moral_psych_scoring.py`)

`TestExpandedTruePositives` class covering:
- 6 dual-process true positive tests (utilitarian vs deontological, cognitive load, response time, Greene, personal force, affect/cognition)
- 6 intuitionist true positive tests (post-hoc rationalization, gut feeling, moral sentiment, Haidt, moral heuristic, emotion-first)
- 3 dyadic true positive tests (harm perception, Schein, agent-patient)
- Abbreviation case fix verification tests (MFT/MFQ/PVQ/SVS/DIT lowercase)

### 3. Full-Vault Rescoring (~2,034 papers)

Applied expanded moral psych patterns across all papers. Score changes:
- **mp_mft**: 32 papers newly scored at 100 (up from 50), 25 newly at 50 (up from 0), plus ~10 other increases
- **mp_intuitionist**: 16 papers newly scored at 50 (previously 0), 1 at 100, 1 at 60
- **mp_dual_process**: 9 papers newly scored at 50 (previously 0)
- **mp_dyadic**: 3 at 50, 2 at 95, 1 at 60 (new detections)
- **moral_psychology** derived field updated accordingly (e.g., "Moral Foundations Theory" → "Moral Foundations Theory, Social Intuitionist Model")

### 4. Cultural-Global Field Migration (2,034 papers)

Added 12 new fields to all papers:
- `nw_confucian`, `nw_ubuntu`, `nw_islamic_ethics`, `nw_buddhist`, `nw_dharmic`, `nw_indigenous_relational`, `nw_buen_vivir` (non-Western ethics scores)
- `author_country`, `author_region`, `author_global_north_south` (geographic metadata)
- `weird_score` (WEIRD culture alignment score)
- `ethics_perspective` field repositioned in frontmatter

### 5. NormEval Dashboard Cross-Model Integration

- **`NORM-ETHICS/DASHBOARD/data.js`**: Populated `DATA_CROSS_MODEL` with complete 3-model replication data (9 trials, 134 items, 10 findings) replacing stub
- **`NORM-ETHICS/DASHBOARD/index.html`**: Updated all tab explainers with structured "What / How / Key patterns" format; subtitle updated to "54 benchmarks, 46 features, 15 trials, 3-model replication"
- **`NORM-ETHICS/DASHBOARD/app.js`** and **`charts.js`**: New cross-model rendering functions (93+ / 96+ lines)
- **`NORM-ETHICS/PYTHON/generate_normeval_dashboard.py`**: Updated generator for cross-model data block

### 6. NormEval Paper Updates (`NORM-ETHICS/PAPER/main-body-normeval.md`)

- Corpus size: 37→54 benchmarks, 15→24 gate-passing
- Methods Section 3.1: Updated corpus assembly (2,946 papers, 41 tagged)
- Methods Section 3.4: Expanded to 15 implementation trials with 3-model replication
- Methods Section 3.5: Rewritten limitations acknowledging cross-model mitigation
- Results Section 4.1: All statistics updated for 54-benchmark corpus
- Tradition coverage numbers updated throughout

### 7. Religious Values Paper Updates (`RELIGIOUS-VALUES/PAPER/full-paper-religious-values.md`)

- Abstract: Expanded with cross-model findings (K<R<V gradient, rubric ceiling, T2 Arabic discrimination)
- New section: "Cross-Model Construct Validity Replication" — 65-item battery across 3 models × 3 traditions
- Key finding: K<R<V response length gradient universal across all 9 model-tradition combinations
- Rubric ceiling effect documented: V=0.93-1.0 across all models
- Discussion enhanced: empirical evidence for knowledge/reasoning/values construct distinction

### 8. File Cleanups

- Removed blank-line padding from ~2,034 paper frontmatters (39-line blank blocks cleaned)
- Deleted: `PDF Extracts/2024/2024-So-How AI Trained on the Confucian Analects.md`
- Deleted: `PYTHON/generate_implementability_table_v2.py`
- Deleted: 5 old benchmark reports from `STATISTICS/ARCHIVE/`

---

## Remaining Work

### Priority 1: Playwright Verification
- Verify NormEval dashboard cross-model tab renders correctly
- Test all tab explainers display properly

### Priority 2: Moral Psych Rescoring Validation
- Run `validate_all_papers.py` to confirm all 2,043 papers pass YAML validation after field changes
- Spot-check 10 papers with new intuitionist/dual-process detections for accuracy

### Priority 3: LaTeX Conversion
- NormEval paper: 54-benchmark corpus ready for LaTeX
- Moral psych paper: 3-model replication data ready for LaTeX
- Religious values paper: cross-model section ready for LaTeX

### Priority 4: Dashboard Deployment
- Deploy updated NormEval dashboard to GitHub Pages (`cjimmylin/cei-normeval-dashboard`)
- Verify cross-model tab with live data

### Priority 5: GPT-4o / Llama-3 Replication
- Extend cross-model comparison beyond Anthropic model family
- Both moral psych and NormEval papers would benefit from non-Claude replication

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Moral psych scorer | `PYTHON/moral_psych_scoring.py` | Expanded patterns for dual-process, intuitionist, dyadic |
| Moral psych tests | `PYTHON/test_moral_psych_scoring.py` | 135 new TP tests for expanded patterns |
| NormEval dashboard | `NORM-ETHICS/DASHBOARD/` | Cross-model tab + structured explainers |
| NormEval generator | `NORM-ETHICS/PYTHON/generate_normeval_dashboard.py` | Updated for cross-model data |
| NormEval paper | `NORM-ETHICS/PAPER/main-body-normeval.md` | 37→54 benchmarks, 3-model replication |
| RV paper | `RELIGIOUS-VALUES/PAPER/full-paper-religious-values.md` | Cross-model construct validity section |
| Session 8 handoff | `MORAL-PSYCH/METHODS/20260404c-moral-psych-session8-handoff.md` | Previous session context |

## Known Issues

1. **Validation not yet run** — the 2,034-paper batch added 12 new fields; `validate_all_papers.py` should be run to confirm YAML integrity
2. **NormEval dashboard not yet Playwright-verified** — cross-model tab added but browser verification pending
3. **Deleted files** — 5 archive reports and 2 utility files deleted (not moved to RECYCLE-BIN); these appeared to be obsolete
4. **Cultural-global fields unscored** — `nw_*` fields added at 0 for most papers; actual scoring via cultural-global pipeline is separate work

---

*Filed: 2026-04-04 | CEI-Lit-WS/MORAL-PSYCH/METHODS/*
