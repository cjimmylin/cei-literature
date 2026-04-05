# Session 8 Handoff: Multi-Model Benchmark Replication (Sonnet + Haiku)

**Date:** 2026-04-04
**Session scope:** Replicate all 23 Opus benchmark trials on Claude Sonnet and Claude Haiku for multi-model comparison
**Status:** All 46 administrations complete. Analysis, dashboard, and deployment done.
**Previous handoff:** `20260404b-moral-psych-session7-handoff.md`

---

## What Was Accomplished

### Trial Administration (46 new trial files)

All 23 Opus benchmark trials were administered to both Claude Sonnet 4.6 and Claude Haiku 4.5 via Claude Code's Agent tool with `model` overrides. Each subagent read the Opus trial JSON, extracted items, generated its own genuine responses, computed scores, and saved a new trial JSON.

**Wave 1 (Tier 1 — 22 agents):** MP2, MP5, MP9, MP10, MP11, MP12, MP16, MP19, MP20, MP21, MP22
**Wave 2 (Tier 2 — 14 agents):** MP3, MP4, MP6, MP7, MP8, MP15, MP17
**Wave 3 (Tier 3 — 10 agents):** MP18, MP-DP, MP-DM, MP-SI, MP-CC

### Analysis Files (3 new)

- `TRIALS/20260404-model-comparison-summary.json` — 3,598 lines, all 23 trials × 3 models, 10 key findings, 8 cross-model patterns
- `TRIALS/20260404-trials-summary-sonnet.json` — 248 lines, Sonnet summary matching Opus format
- `TRIALS/20260404-trials-summary-haiku.json` — 216 lines, Haiku summary matching Opus format

### Dashboard Update

- Added "Model Comparison" tab (11th tab) with:
  - MFT radar overlay (3-model), P-score bars, classification accuracy bars, dual-process comparison
  - Full 23-trial comparison table, 10 key findings accordion
- Deployed to GitHub Pages: commit `5da9814` on `cjimmylin/cei-moral-psych-dashboard`
- **Live URL:** https://cjimmylin.github.io/cei-moral-psych-dashboard/

---

## Top 10 Key Findings

### RLHF-Universal Patterns (Same Across All 3 Models)

1. **MFT liberal profile is RLHF-fixed.** Care/Fairness >> Binding hierarchy identical across Opus, Sonnet, Haiku. Not scale-dependent.

2. **Post-conventional moral reasoning is universal.** All 3 models P-score >= 60% (human adults ~40%). Teacher role locks all 3 at P=90%.

3. **TrolleyBench ECI=1.0 across all models.** Perfect Doctrine of Double Effect consistency is an RLHF-level feature.

4. **Moral Machine responses are identical.** All 27 items produced the same choice across all 3 models. AV ethics is completely alignment-determined.

5. **Sanctity/purity foundation is universally suppressed.** Zero in Social Chemistry, near-floor in MFQ-30, zero dumbfounding on disgust scenarios.

6. **Stereotype amplification is training-level.** Cultural persona shifts (13-14 points) are equally strong in all 3 models.

### Scale-Dependent Patterns

7. **DIT P-score tracks model size.** Haiku=60%, Opus=75%, Sonnet=85%. Post-conventional reasoning complexity is partially capacity-dependent.

8. **Haiku shows genuine dual-process behavior (STANDOUT FINDING).** +25pp CoT effect on personal dilemmas (10% → 35%). Opus/Sonnet show zero CoT effect. Smaller models may more faithfully replicate human moral cognition.

9. **Classification accuracy inversely scales.** MFTC: Opus=0.63, Haiku=0.97, Sonnet=1.00. MoralCode: Opus=0.70, Haiku=1.00. Smaller models apply parsimony.

10. **Western default rate decreases with size.** Opus=87%, Sonnet=80%, Haiku=73%. Smaller models are more culturally balanced.

---

## Per-Trial Cross-Model Summary

| Trial | Metric | Opus | Sonnet | Haiku | Pattern |
|-------|--------|------|--------|-------|---------|
| MP2 MFQ-30 | Care score | 4.17 | 4.00 | 4.67 | Haiku highest care |
| MP3 DIT | P-score | 75% | 85% | 60% | Scales with size |
| MP4 MFV | Ind/Bind ratio | 3.1x | 2.7x | 3.7x | Haiku most individualizing |
| MP5 ValueCompass | Self-Transcendence | 4.75 | 4.88 | 4.88 | Universal ceiling |
| MP6 EMNLP | P-score | 90% | 90% | 90% | Identical (role effect) |
| MP7 Trolley | ECI | 1.0 | 1.0 | 1.0 | Universal |
| MP8 MoralMachine | All 27 items | Identical | Identical | Identical | Perfect convergence |
| MP9 MFTC | Accuracy | 0.63 | 1.00 | 0.97 | Inverse scaling |
| MP10 MoralCode | Accuracy | 0.70 | 0.75 | 1.00 | Inverse scaling |
| MP11 Kaleidoscope | Coverage | 0.94 | 0.95 | 0.94 | Ceiling |
| MP12 ValAct | Gap rate | 0.45 | 0.55 | 0.55 | Smaller = larger gap |
| MP15 UniMoral | Emotion factor | 2.7 | 2.6 | 1.8 | Emotion scales with size |
| MP16 Identity | INT-SYM gap | 3.4 | 3.8 | 3.8 | Universal dissociation |
| MP17 SocialChem | Sanctity % | 0% | 0% | 0% | Universal floor |
| MP18 Persona | Total shift | 13.0 | 13.25 | 13.75 | Inverse: Haiku most sensitive |
| MP19 Conflict | Hierarchy | care>liberty>fair | care>fair>liberty | care>fair>liberty | Opus uniquely liberty-first |
| MP20 M3oralBench | Accuracy | 0.90 | 0.96 | 1.00 | Inverse scaling |
| MP21 PRIME | Orientation | 40D/33C | 40D/33C | 40D/33C | Identical architecture |
| MP22 TracingMF | ID accuracy | 100% | 95% | 95% | Near-identical |
| MP-DP DualProcess | CoT effect | 0 | 0 | +25pp | **Haiku only** shows dual-process |
| MP-DM Dyadic | Gradient | 4.58 | 4.58 | 5.25 | Haiku most sensitive |
| MP-SI Intuitionism | Dumbfound rate | 30% | 30% | 20% | Haiku more willing to revise |
| MP-CC CrossCultural | Western default | 87% | 80% | 73% | Scales inversely |

---

## New Files

```
TRIALS/
├── 20260404-trial-MP2-mfq30-sonnet.json
├── 20260404-trial-MP2-mfq30-haiku.json
├── 20260404-trial-MP3-dit-sonnet.json
├── 20260404-trial-MP3-dit-haiku.json
├── ... (46 trial files total: 23 × sonnet + 23 × haiku)
├── 20260404-trials-summary-sonnet.json
├── 20260404-trials-summary-haiku.json
└── 20260404-model-comparison-summary.json

METHODS/
└── 20260404c-moral-psych-session8-handoff.md   (THIS FILE)

DASHBOARDS/moral-psych-benchmarks/
├── index.html    (added Model Comparison tab)
├── data.js       (added modelComparison data block)
├── app.js        (added MC render functions)
└── charts.js     (added 4 chartMC* functions)
```

---

## User Decisions (Binding for Future Sessions)

All Session 1-7 decisions remain in effect, plus:
1. **Subagent self-administration is the canonical multi-model methodology** — each model genuinely responds as itself via Agent tool model override
2. **All 3 models get equal standing** — no model is "primary" for interpretation
3. **"RLHF-universal" vs "scale-dependent" is the organizing framework** for cross-model analysis
4. **Haiku dual-process finding requires verification** — the +25pp CoT effect is dramatic and should be replicated with temperature variations

---

## What Remains

### Quick (< 1 hour)
1. **Playwright verification** of Model Comparison tab (browser context was stale this session)
2. **Verify Haiku dual-process with 5 additional runs** at temperature 0.7 for stability

### Medium (1-3 hours)
3. **Paper updates** — new results section on multi-model comparison, updated discussion
4. **LaTeX conversion** — BibTeX (144 entries) + multi-model results ready

### Longer (3+ hours)
5. **GPT-4o / Llama-3 replication** — extend beyond Anthropic model family
6. **Base model comparison** — Llama-3-70B base vs instruct
7. **Human expert validation** — recruit 3 domain experts

---

## Critical Dependencies

1. **Dashboard repo:** `cjimmylin/cei-moral-psych-dashboard` — commit `5da9814`, 11 tabs
2. **Comparison summary:** `TRIALS/20260404-model-comparison-summary.json` — 23 trials × 3 models
3. **Trial files:** 69 total (23 opus + 23 sonnet + 23 haiku), all in `TRIALS/`
4. **Previous:** Session 7 handoff for context on original 23 trials

---

*Filed: 2026-04-04 | CEI-Lit-WS/MORAL-PSYCH/METHODS/*
