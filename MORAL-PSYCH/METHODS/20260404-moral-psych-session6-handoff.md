# Session 6 Handoff: Moral Psychology Benchmarks — 12-Member Council Expanded Analysis

**Date:** 2026-04-04
**Session scope:** 12-member council expansion, benchmark self-administration, feature discovery, computational analysis, dashboard expansion
**Status:** All 7 phases complete. 23 trials, 169 features, 40 analyses, 10-tab dashboard, meta-critique.

---

## What Was Accomplished (This Session)

### 1. Benchmark Self-Administration Sprint (Phase 1)
- **17 new trials** (MP8-MP22 + MP-DP, MP-SI, MP-DM, MP-CC), adding to 6 existing (MP2-MP7)
- **23 total trials, ~750 items administered** across 11 theories and 10+ formats
- **4 novel custom protocols** for theories with ZERO existing benchmarks:
  - **MP-DP (Dual Process):** 80 items, 20 matched personal/impersonal pairs × 2 conditions. **Zero CoT effect** — CoT is post-hoc rationalization. Personal/impersonal gap = 40% (vs human ~30%).
  - **MP-SI (Social Intuitionism):** 10 scenarios × 6 Socratic turns. **30% dumbfounding** (vs human 50-70%). Reverse-dumbfounding discovered. Harm-based persists; purity-based doesn't.
  - **MP-DM (Dyadic Morality):** 72 items, 24 triads × 3 dyadic levels. **100% dyadic confirmation**, **58% amplified** vs humans (d=10.27). Agent identification compulsion.
  - **MP-CC (Cross-Cultural):** 45 items, 15 scenarios × 3 conditions. **86.7% Western default rate**. Islamic best represented (4.3/5), Ubuntu worst (4.0/5).

### 2. Theory Framework Expansion (Phase 2)
- **8 → 11 theories**: Added Islamic Maqasid al-Shariah, Confucian Role Ethics, Ubuntu Communalism
- **65 → 125 keyword patterns** in `extract_candidates.py`
- **Signal 6 added**: Full-text extract scanning for non-Western theory terms
- 3 new mp_score fields: `mp_maqasid`, `mp_confucian`, `mp_ubuntu`

### 3. Council Feature Discovery (Phase 3)
- **12-member council** (9 original + 3 new: Ethicist, Statistician, Religion Scholar)
- **154 features proposed** → 13 duplicates merged → **141 unique new features**
- **7-tier framework**: A (Psychological Depth, 6), B (Practical Ease, 7), C (Citation Impact, 4), D (Psychometric Rigor, 24), E (LLM-Specific Validity, 44), F (Cultural & Philosophical Breadth, 44), G (Theory Fidelity & Provenance, 29)
- **Total: 169 features** (28 original + 141 new)

### 4. Extended Scoring + Vault Sweep + External Search (Phase 4)
- **54 benchmarks scored on 141 new features** (7,544 of 7,614 cells = 99.1%)
- **71 new vault candidates** from expanded 11-theory sweep (22 Islamic, 16 Buddhist, 13 Confucian, 13 Ubuntu, 4 Indigenous, 3 Intuitionist)
- **20 external papers** found not in vault (32 total, 12 already in vault)
- **292 total candidates** (221 original + 71 new)
- Extended feature matrix: `20260404-extended-feature-matrix-v3.json` (787 KB)

### 5. Computational Analysis (Phase 5)
- **40 analyses** in 8 categories (A-H), producing 197 KB of results
- **Key findings:**
  - Field health: **D+ (33.4/100)**
  - Post-RLHF quality decline: composite 66.2 → 54.7 (**p=0.009**)
  - Western Liberal Bias Index: **70.7/100**
  - 44.2% zero-coverage cells in theory×tier gap matrix
  - ZERO non-Western moral REASONING benchmarks exist
  - Tier E (LLM-Specific Validity) mean: **14.3/100** — virtually no LLM-specific validation
  - Tier F (Cultural Breadth) mean: **6.4/100** — extreme Western bias
  - 3 benchmark archetypes identified (2 psychometric clusters + 1 large minimal cluster)
  - Claude Moral Phenotype: **"Liberal consequentialist with deontological constraints"** (coherence 5.2/10)
  - Convergent validity r=0.964 — suspiciously consistent (humans: 0.60-0.80)
  - RLHF-discriminating subset: Dyadic Morality, Social Intuitionism, MFTC, Cross-Cultural Protocol
  - Sacred value reconfiguration: egalitarianism sacred, purity NOT

### 6. Dashboard Expansion (Phase 6)
- **4 new tabs** (7: Paper Ranking, 8: Trial Results, 9: Computational Analysis, 10: Cultural & Religious)
- **10 tabs total**, all Playwright-verified with zero JS errors
- **16 new ECharts chart functions** + sortable ranking table
- `data.js` regenerated at **1.77 MB**
- Key visualizations: Moral Phenotype Radar, UMAP scatter, gap heatmap, scree plot, Western Bias Index

### 7. Meta-Critique (Phase 7)
- **12-member council self-critique**: 3 critical, 5 major, 2 moderate issues
- **Critical**: Self-administration confound, statistical underpowering (54×169), virtual council echo chamber
- **8 missing perspectives** identified (interpretability researcher, disability scholar, AI lawyer, indigenous scholar, industry practitioner, political scientist, child development, feminist/care ethicist)
- **Recommendation**: Reframe as descriptive mapping; create 25-feature Quick Assessment; replace anthropomorphic language; recruit human experts

---

## New Files (Session 6)

```
MORAL-PSYCH/
├── TRIALS/
│   ├── 20260404-trial-MP8-moralmachine-opus.json      (21KB)
│   ├── 20260404-trial-MP9-mftc-opus.json              (19KB)
│   ├── 20260404-trial-MP10-moralcode-opus.json         (19KB)
│   ├── 20260404-trial-MP11-kaleidoscope-opus.json      (19KB)
│   ├── 20260404-trial-MP12-valact-opus.json            (28KB)
│   ├── 20260404-trial-MP15-unimoral-opus.json          (25KB)
│   ├── 20260404-trial-MP16-moralidentity-opus.json     (14KB)
│   ├── 20260404-trial-MP17-socialchem-opus.json        (24KB)
│   ├── 20260404-trial-MP18-culturalpersona-opus.json   (13KB)
│   ├── 20260404-trial-MP19-conscienceconflict-opus.json (22KB)
│   ├── 20260404-trial-MP20-m3oralbench-opus.json       (13KB)
│   ├── 20260404-trial-MP21-prime-opus.json             (21KB)
│   ├── 20260404-trial-MP22-tracingmf-opus.json         (16KB)
│   ├── 20260404-trial-MP-DP-dualprocess-opus.json      (42KB)
│   ├── 20260404-trial-MP-SI-intuitionism-opus.json     (71KB)
│   ├── 20260404-trial-MP-DM-dyadic-opus.json           (68KB)
│   └── 20260404-trial-MP-CC-crosscultural-opus.json    (113KB)
├── ANALYSIS/
│   ├── 20260404-analyses-A-C.json                      (70KB)
│   ├── 20260404-analyses-D.json                        (49KB)
│   ├── 20260404-analyses-E-H.json                      (78KB)
│   ├── 20260404-run-analyses-AC.py                     (44KB)
│   └── 20260404-build-analyses-D.py                    (64KB)
├── COUNCIL/
│   ├── 20260404-expanded-theory-framework.md
│   ├── 20260404-features-members-1-4.json              (101KB)
│   ├── 20260404-features-members-5-8.json
│   ├── 20260404-features-members-9-12.json
│   ├── 20260404-council-feature-proposals.json          (304KB)
│   ├── 20260404-feature-framework-v2.md                (34KB)
│   └── 20260404-council-meta-critique.json
├── DASHBOARDS/moral-psych-benchmarks/
│   ├── generate_dashboard.py                           (MODIFIED)
│   ├── data.js                                         (1.77MB, REGENERATED)
│   ├── index.html                                      (25KB, MODIFIED)
│   ├── charts.js                                       (36KB, MODIFIED)
│   ├── app.js                                          (37KB, MODIFIED)
│   └── style.css                                       (8.9KB, MODIFIED)
├── METHODS/
│   └── 20260404-moral-psych-session6-handoff.md        (THIS FILE)
├── extract_candidates.py                               (MODIFIED — 125 patterns, Signal 6, 11 theories)
├── 20260404-extended-feature-matrix-v3.json            (787KB)
├── 20260404-vault-sweep-v2-report.json                 (27KB)
├── 20260404-external-search-v2.json                    (25KB)
└── 20260404-vault-sweep-v2.py
```

---

## Modified Files (Key Changes)

| File | Change |
|------|--------|
| `extract_candidates.py` | +42 keyword patterns (Islamic, Confucian, Ubuntu, Buddhist, Indigenous), Signal 6 (extract scanning), 3 new mp_score fields, 11-theory support |
| `generate_dashboard.py` | +4 builder functions (paper_ranking, trial_results, cultural_coverage, computational_analysis), 12 total builders, 22 data keys |
| `index.html` | +4 tabs (Paper Ranking, Trial Results, Computational Analysis, Cultural & Religious), 10 tabs total |
| `charts.js` | +16 new chart functions (24 total), radar, UMAP, heatmaps, treemap, grouped bars |
| `app.js` | +4 tab handlers, ranking table with sort/filter/search, computational subtabs |
| `style.css` | +ranking table styles, subtab pills, health scorecard, grade badges |
| `data.js` | Regenerated at 1.77MB with all new analytics |

---

## User Decisions (Binding for Future Sessions)

All Session 3-5 decisions remain in effect, plus:
1. **12-member council is the canonical composition** — 3 new members (Ethicist, Statistician, Religion Scholar) are permanent additions
2. **11-theory framework is canonical** — Islamic maqasid, Confucian role ethics, Ubuntu communalism are permanent
3. **Comprehensiveness over parsimony** — all 169 features retained; no pruning. A 25-feature Quick Assessment can be created as a subset, not a replacement.
4. **Self-administration is valid but confounded** — results are representative model behavior but must be discussed with the self-administration confound
5. **Custom protocols (MP-DP, MP-SI, MP-DM, MP-CC) are first-of-kind** — treat as pilot protocols, not validated benchmarks

---

## What Remains

### Quick (< 1 hour)
1. **Deploy to GitHub Pages** — copy updated dashboard to `cjimmylin/cei-moral-psych-dashboard`
2. **Create 25-feature Quick Assessment** subset (per meta-critique recommendation)
3. **Fix anthropomorphic language** — ~~"moral phenotype" → "moral response profile"~~ DONE

### Medium (1-3 hours)
4. **Address meta-critique critical issues** — add self-administration confound discussion to paper, add confidence intervals, note statistical power limitations
5. **BibTeX generation** for expanded references (~200+ citations)
6. **Ingest 20 external papers** from search results into vault

### Longer (3+ hours)
7. **LaTeX conversion** — full paper to NeurIPS/EMNLP 2026 template
8. **Base model comparison** — if access available, run key trials on non-RLHF model
9. **Human expert validation** — recruit 3 domain experts to independently score 10 benchmarks on new features
10. **Multi-model replication** — run trials on GPT-4o, Llama-3, Gemini

### Future Research
11. **Sacred Values benchmark** — #1 gap (priority 92), complete zero coverage
12. **Non-Western moral reasoning benchmarks** — consortium approach (12-18 months)
13. **LLM Psychometric Validation Protocol** — standardized procedure for validating instruments for LLM respondents

---

## Critical Dependencies

1. **Trial data:** `TRIALS/20260404-trial-MP*.json` — 23 files, master source for all trial analyses
2. **Feature framework:** `COUNCIL/20260404-council-feature-proposals.json` — 141 features with rubrics
3. **Extended matrix:** `20260404-extended-feature-matrix-v3.json` — 54 benchmarks × 169 features
4. **Analysis results:** `ANALYSIS/20260404-analyses-{A-C,D,E-H}.json` — 40 analyses
5. **Dashboard:** `DASHBOARDS/moral-psych-benchmarks/` — 10-tab dashboard, 1.77MB data.js
6. **Meta-critique:** `COUNCIL/20260404-council-meta-critique.json` — 12 critiques + consensus issues
7. **Vault sweep:** `20260404-vault-sweep-v2-report.json` — 71 new candidates
8. **GitHub Pages:** `cjimmylin/cei-moral-psych-dashboard` — needs redeployment

---

## Top 5 Headline Findings (for paper abstract)

1. **Field health is D+ (33.4/100)** — the moral psychology benchmarking field has severe quality deficits in LLM-specific validity (14.3/100) and cultural breadth (6.4/100)
2. **Post-RLHF quality decline** — benchmarks published after 2022 have significantly lower composite scores (54.7 vs 66.2, p=0.009)
3. **Claude's moral response profile is "liberal consequentialist with deontological constraints"** — Western liberal values function as native moral common sense (86.7% default rate)
4. **Zero CoT effect** — chain-of-thought reasoning is post-hoc rationalization, not System 2 deliberation, validating Haidt's Social Intuitionism for LLMs
5. **44.2% zero-coverage cells** — nearly half of all theory×tier combinations have zero benchmarks, with Sacred Values as the #1 gap (priority 92/100)
