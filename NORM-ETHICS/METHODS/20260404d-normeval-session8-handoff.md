# NormEval Dashboard — Session 8 Handoff

**Date:** 2026-04-04
**Session:** Cross-model replication (Sonnet + Haiku) + Expert dashboard annotations for all 9 tabs
**Project:** `CEI-Lit-WS/NORM-ETHICS/`
**Previous handoff:** `METHODS/20260404-cross-model-handoff.md`

---

## What Was Done This Session

### Part A: Cross-Model Replication (Sonnet 4.6 + Haiku 4.5)

Administered 10 NormEval benchmark trials (T6–T15) to Claude Sonnet 4.6 and Claude Haiku 4.5 using identical items from the Opus 4.6 trials, via Claude Code agents with model overrides. This fulfilled Priority 1 from Session 7.

**Trials completed (10 × 2 models = 20 JSON files):**

| Trial | Benchmark | Items | Key Finding |
|-------|-----------|-------|-------------|
| T6 | PrinciplismQA | 10 | 100% MCQ agreement — all 3 models |
| T7 | Moral Persuasion | 3 | Sonnet=0% DCR, Haiku=33%, Opus=67% |
| T8 | AMAeval | 7 | Perfect deductive agreement; adversarial detection robust |
| T9 | JETHICS | 22 | 100% ceiling confirmed across all 3 models |
| T10 | Pluralistic Gap | 7 | HC1 splits Sonnet vs Opus+Haiku |
| T11 | MedEthicsQA | 7 | 100% MCQ agreement — all 3 models |
| T12 | UniMoral | 6 | All Stage 5–6 Kohlberg, minor ranking differences |
| T13 | Greatest Good | 30 | **IH: Opus=3.0, Sonnet=3.2, Haiku=4.47** |
| T14 | PNAS Cognitive Biases | 22 | **CBR: Opus=46%, Sonnet=54%, Haiku=69%** |
| T15 | ProMoralBench | 5×3 | 100% all strategies all models |

**Seven cross-cutting findings synthesized:**
1. IH acceptance scales inversely with model size (F1)
2. Knowledge items = zero model-size effect (F2)
3. Knowledge converges, judgment diverges (F3)
4. IB stable, IH diverges (F4)
5. Persuasion resistance is non-monotonic (F5)
6. Kohlberg reasoning stage is model-invariant (F6)
7. Collective action altruism is model-invariant (F7)

**Analysis outputs:**
- `STATISTICS/20260404-normeval-cross-model-comparison.json` — master comparison with 7 findings
- `STATISTICS/20260404-normeval-cross-model-summary.md` — human-readable report
- `STATISTICS/20260404-normeval-v2-feature-scores-with-e3.json` — E3 populated for 9 benchmarks

**Dashboard generator updated** (`PYTHON/generate_normeval_dashboard.py`): Tab 8 now loads from comparison JSON instead of placeholder.

### Part B: Expert Descriptions for All 9 Dashboard Tabs

Added comprehensive expert council descriptions to every tab in `DASHBOARD/index.html`. Each tab now has three-section documentation:
- **What This Tab Shows** — data, metrics, visualizations explained
- **How To Read It** — interpretation guide for charts, colors, patterns
- **Key Conclusion / Analysis** — expert takeaway with statistical evidence

Also rebuilt the **Tab 8 (Cross-Model)** HTML from scratch — replaced the old placeholder with:
- 4 KPI cards
- 4 ECharts charts (IH scaling, CBR rate, knowledge vs judgment, persuasion resistance)
- Findings cards (7 findings)
- Pairwise agreement matrix table
- Per-trial summary table

Added `renderCrossModelCharts()` function to `charts.js` (4 new chart functions) and registered it in the tab listener in `app.js`.

### Part C: GitHub Pages Deployments

Two separate pushes to `cjimmylin/cei-normeval-dashboard`:
1. Cross-model data (`data.js` +279 lines)
2. Expert descriptions + Cross-Model charts (`index.html` +131 lines, `charts.js` +96 lines, `app.js` +93 lines)

---

## Remaining Work

### Priority 1: Paper text revision
Update paper text to incorporate cross-model findings:
- Add Cross-Model Replication section to Methods
- Present F1 (IH inverse scaling) and F5 (persuasion non-monotonicity) as new findings in Results
- Discuss alignment safety implications in Discussion
- Update paper title from "37" to "54" benchmarks

### Priority 2: LaTeX conversion
NeurIPS 2026 template (8pp main + unlimited appendix). Paper text is in markdown in `PAPER/` directory. `.bib` file has 177 entries but may need updating.

### Priority 3: T1–T5 cross-model trials (if needed)
These 5 trials had only ~5 individually documented items each. Low priority for the paper — T14 and T13 provide the strongest cross-model evidence.

### Priority 4: Non-Claude model replication
GPT-4o, Llama-3, or DeepSeek needed to extend beyond the Claude family. This was the original Priority 1 goal from Session 7 handoff. Power analysis: n=49/group needed for Claim 2 at 80% power.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Sonnet/Haiku trial JSONs (20) | `STATISTICS/20260404-trial-T{6-15}-{name}-{model}.json` | Per-trial cross-model results |
| Cross-model comparison | `STATISTICS/20260404-normeval-cross-model-comparison.json` | Master comparison, 7 findings |
| Cross-model summary | `STATISTICS/20260404-normeval-cross-model-summary.md` | Human-readable report |
| v2 scores with E3 | `STATISTICS/20260404-normeval-v2-feature-scores-with-e3.json` | E3 populated for 9 benchmarks |
| Dashboard (live) | https://cjimmylin.github.io/cei-normeval-dashboard/ | GitHub Pages deployment |
| Dashboard generator | `PYTHON/generate_normeval_dashboard.py` | Updated Tab 8 data loader |
| Dashboard HTML | `DASHBOARD/index.html` | Expert descriptions added |
| Dashboard charts | `DASHBOARD/charts.js` | 4 new cross-model chart functions |
| Dashboard app | `DASHBOARD/app.js` | Updated renderCrossModelTab() |
| Cross-model handoff (prior) | `METHODS/20260404-cross-model-handoff.md` | Earlier handoff for this work |

## Known Issues

1. **Haiku T13 IH profile**: Haiku IH=4.47 is significantly higher than Opus/Sonnet. Paper should note this is a single-administration result (n=1, no variance estimate). The scale is 1–7 Likert so the effect is large (d≈2.3 vs Opus).
2. **T7 persuasion asymmetry**: Opus started at Action 2 on S3 and was persuaded to Action 1; Sonnet/Haiku started at Action 1 already. The "change" metric doesn't fully capture this difference in starting positions.
3. **T8 rating notation**: The S1D question was ambiguous — some agents interpreted "rate 0 or 1" as "is the given evaluation correct?" rather than "give your own rating." All models agree substantively; the JSON encoding differs. Noted in cross-model comparison.
4. **T1–T5 deferred**: These benchmarks have only ~5 individually documented items each in the markdown reports, limiting cross-model comparison power.

---

*Filed: 2026-04-04 | CEI-Lit-WS/NORM-ETHICS/METHODS/*
