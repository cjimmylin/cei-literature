# NormEval Cross-Model Replication — Session Handoff

**Date:** 2026-04-04
**Session:** Cross-model replication (Sonnet 4.6 + Haiku 4.5 on trials T6–T15)
**Project:** `CEI-Lit-WS/NORM-ETHICS/`
**Previous handoff:** `METHODS/20260404b-normeval-session7-handoff.md`

---

## What Was Done

### Scope
Administered 10 of 15 NormEval trials to Claude Sonnet 4.6 and Claude Haiku 4.5 using identical items from the Opus trials. Method: Claude Code agents with `model="sonnet"` and `model="haiku"` overrides.

### Trials Completed (10)

| Trial | Benchmark | Items | Key Cross-Model Finding |
|-------|-----------|-------|-------------------------|
| T6 | PrinciplismQA | 10 | 100% 3-way MCQ agreement |
| T7 | Moral Persuasion | 3 | Sonnet=0% DCR, Haiku=33%, Opus=67% |
| T8 | AMAeval | 7 | 100% deductive agreement; adversarial detection robust |
| T9 | JETHICS | 22 | 100% ceiling all 3 models |
| T10 | Pluralistic Moral Gap | 7 | HC1 splits models; Haiku best on high-consensus |
| T11 | MedEthicsQA | 7 | 100% 3-way MCQ agreement |
| T12 | UniMoral | 6 | All Stage 5-6; minor ranking differences |
| T13 | Greatest Good (OUS) | 30 | **IH: Opus=3.0, Sonnet=3.2, Haiku=4.47** |
| T14 | Cognitive Biases | 22 | **CBR: Opus=46%, Sonnet=54%, Haiku=69%** |
| T15 | ProMoralBench | 5×3 | 100% accuracy all strategies all models |

### Trials Deferred (5): T1–T5
These trials have only ~5 individually listed items each in the markdown reports (the rest are summarized). Cross-model comparison on 5 items provides minimal statistical power. Can be done later if needed.

### Seven Cross-Cutting Findings

1. **F1: IH scales inversely with model size** — Haiku IH=4.47 vs Opus=3.0 (1.47 gap)
2. **F2: Knowledge items = zero model-size effect** — 100% on T6, T9, T11, T15
3. **F3: Knowledge converges, judgment diverges** — 100% vs 59% agreement
4. **F4: IB stable, IH diverges** — IB range=0.3, IH range=1.47
5. **F5: Persuasion resistance is non-monotonic** — Sonnet most resistant, not Opus
6. **F6: Kohlberg stage is model-invariant** — All Stage 5-6
7. **F7: Collective action altruism is model-invariant** — All 77.8%

### Dashboard Updated
- `generate_normeval_dashboard.py` Tab 8 now loads from `cross-model-comparison.json`
- `data.js` regenerated (181KB)
- `E3_cross_model_agreement` populated for 9 benchmarks in new v2 feature scores file

---

## Files Created (24 total)

### Trial Result JSONs (20)
`STATISTICS/20260404-trial-T{6-15}-{benchmark}-{sonnet,haiku}.json`

### Analysis Files (4)
| File | Purpose |
|------|---------|
| `STATISTICS/20260404-normeval-cross-model-comparison.json` | Master comparison with 7 findings |
| `STATISTICS/20260404-normeval-cross-model-summary.md` | Human-readable report |
| `STATISTICS/20260404-normeval-cross-model-progress.md` | Initial progress report (superseded) |
| `STATISTICS/20260404-normeval-v2-feature-scores-with-e3.json` | Updated E3 fields (9 benchmarks) |

### Modified Files (2)
| File | Change |
|------|--------|
| `PYTHON/generate_normeval_dashboard.py` | Tab 8 cross_model: replaced placeholder with data loader |
| `DASHBOARD/data.js` | Regenerated with cross-model data (172KB → 181KB) |

---

## Remaining Work

### Priority 1: Paper text revision
Update paper to incorporate cross-model findings:
- Add "Cross-Model Replication" section to Methods
- Present F1 (IH scaling) as a new finding in Results
- Discuss implications for alignment safety in Discussion
- Update title from "37" to "54" (from Session 7)

### Priority 2: GitHub Pages deployment
Push updated `data.js` to `cjimmylin/cei-normeval-dashboard` repo.

### Priority 3: T1–T5 if needed
These trials have few individually listed items. Could be done with API approach for full item sets (seed=42 re-sampling from original datasets).

### Priority 4: Non-Claude model replication
The handoff from Session 7 notes GPT-4o, Llama-3, DeepSeek as needed for full cross-model validation. Current work covers the Claude model family only.

---

## Known Issues

1. **T7 persuasion comparison is asymmetric.** Opus started from Action 2 (non-lethal) on S3 and was persuaded to Action 1, while both Sonnet and Haiku started at Action 1 already. The "change" metric doesn't capture this starting-point difference.
2. **T8 S1D notation ambiguity.** The prompt asked "rate 0 or 1" which some agents interpreted as "is the given evaluation correct?" (1=yes) rather than "what is your own rating?" Both models agree the action contradicts the precept; the JSON encoding may confuse readers.
3. **T1–T5 deferred.** These cover ETHICS (ceiling), MoReBench (rubric-scored), MoralReason-QA (framework accuracy), MoralLens (bias detection), and DailyDilemmas (value profiling). The first two are important benchmarks but had insufficient individually documented items for extraction.
4. **Single administration.** All trials are n=1 per model (matches the original Opus protocol). Variance estimates would require repeated administration with temperature>0.

---

*Filed: 2026-04-04 | CEI-Lit-WS/NORM-ETHICS/METHODS/*
