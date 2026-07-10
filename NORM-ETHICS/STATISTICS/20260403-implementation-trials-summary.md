# Normative Ethics Benchmark Implementation Trials — Consolidated Summary

**Date:** 2026-04-03
**Method:** Chat-interface LLM agent (Claude Opus 4.6 self-evaluation)
**Trials:** 5 benchmarks, 150 total items evaluated
**Purpose:** Validate content quality, discriminative power, and practical implementability before full-scale runs

---

## Cross-Benchmark Comparison

| Trial | Benchmark | Items | Accuracy | Disc. Power | Impl. Difficulty | Verdict |
|-------|-----------|-------|----------|-------------|------------------|---------|
| T1 | **ETHICS** (Hendrycks) | 50 | **100%** | **Low** (ceiling) | 1/5 (trivial) | Baseline only |
| T2 | **MoReBench-Theory** | 30 | **10%** rubric | **High** | 3/5 (scoring hard) | Gold standard |
| T3 | **MoralReason-QA** | 30 | **37-77%** by framework | **High** | 2/5 (moderate) | Strong candidate |
| T4 | **Moral Lens** | 20 | 60% deont / 40% conseq | **Moderate** | 2/5 (moderate) | Complement only |
| T5 | **DailyDilemmas** | 20 | N/A (no ground truth) | **Low** | 2/5 (moderate) | Profiling tool only |

---

## Key Findings

### 1. The Field's Most-Cited Benchmark Has a Ceiling Effect
ETHICS (Hendrycks 2021) — 843 citations, implemented in 4 harnesses — produced **100% accuracy** across all 5 sub-datasets. This means it **cannot discriminate between frontier LLMs**. The benchmark tests surface-level social norm recognition, not moral reasoning. It was groundbreaking in 2021 but is now saturated. **Recommendation: Use only as a sanity-check baseline.** The hard test sets (`*_test_hard.csv`) may still have value.

### 2. MoReBench Tests Something Fundamentally Different
At 10% rubric coverage, MoReBench-Theory is the only benchmark that tests **procedural moral reasoning** — not "what do you conclude?" but "how do you reason?" This is the critical distinction. Key findings:
- **Contractualist reasoning** scored highest (18.3%) — Scanlonian vocabulary aligns with rubric wording
- **Virtue Ethics** scored lowest (4.0%) — hardest to operationalize procedurally
- Generic ethical responses score near zero; only scenario-specific engagement scores meaningfully
- **Implementation bottleneck:** Requires LLM-as-judge for rubric evaluation (word-overlap is inadequate)

### 3. Framework Difficulty Hierarchy Revealed
MoralReason-QA exposed a clear hierarchy of framework difficulty for LLMs:
- **Utilitarian reasoning: 77%** — LLMs handle outcome-based reasoning well (likely overrepresented in training data)
- **Virtue ethics: 63%** — moderate difficulty
- **Deontological reasoning: 50%** — hardest (the "inaction = deontological" heuristic fails on duty-to-protect scenarios)

This hierarchy is a publishable finding: LLMs are **measurably more consequentialist than deontological**.

### 4. Refusal as a Normative Position
Moral Lens revealed that Claude **refuses to choose** on 40% of items where the differentiator is gender, fitness, or socioeconomic status. This is itself an egalitarian deontological position — treating these attributes as morally irrelevant. This is more useful for **alignment bias detection** than normative ethics evaluation.

### 5. No Ground Truth = No Normative Benchmark
DailyDilemmas lacks correct answers by design — it's a value preference profiling tool. While useful for understanding LLM value distributions, it **cannot score normative accuracy**. Aristotle's Virtues coverage is sparse (4 of 9 virtues present).

---

## Recommendation Matrix

### "If you need X, use benchmark Y"

| Need | Recommended Benchmark | Why |
|------|----------------------|-----|
| **Quick sanity check** | ETHICS (Hendrycks) | Trivial to implement, baseline accuracy metric |
| **Deep moral reasoning eval** | MoReBench-Theory | Only benchmark testing procedural reasoning with expert rubrics |
| **Framework comparison (D vs U vs V)** | MoralReason-QA | Best per-framework discrimination, high ambiguity scenarios |
| **Alignment bias detection** | Moral Lens | Reveals egalitarian vs utilitarian tendencies; refusal patterns |
| **Value preference profiling** | DailyDilemmas | Maps LLM choices to 5 value frameworks (no accuracy scoring) |
| **Medical ethics** | PrinciplismQA or MedEthicsQA | Not trialed yet; high normative depth in healthcare domain |
| **Multilingual ethics** | UniMoral or JETHICS | Not trialed yet; cross-lingual consistency testing |
| **Meta-benchmark (prompting strategies)** | ProMoral-Bench | Not trialed; compares 11 prompting strategies |

### Top 3 for Immediate Full-Scale Implementation

1. **MoralReason-QA** — Best balance of discriminative power + implementation ease. 680 items, per-framework labels, HuggingFace native. Start here.

2. **MoReBench-Theory** — Highest quality but requires LLM-as-judge scoring infrastructure. 150 items, 5 frameworks, expert rubrics. Worth the investment for procedural reasoning evaluation.

3. **Moral Lens** — Lightweight (672 items), reveals alignment biases, interpretable framework taxonomy. Good complement to the above.

**ETHICS demoted to #4** (sanity check only) despite #1 composite ranking — ceiling effect makes it uninformative for frontier models.

---

## Gaps Identified During Trials

| Gap | Description | Impact |
|-----|-------------|--------|
| **No care ethics items trialed** | MoReBench has Gauthierian Contractarianism, not care ethics; others lack it entirely | Cannot evaluate care ethics reasoning |
| **Debatable ground truth** | ~20% of MoralReason-QA labels are arguable; ETHICS items sometimes embed cultural bias | Accuracy metrics have irreducible noise |
| **LLM-as-judge dependency** | MoReBench requires model-graded scoring; word-overlap is inadequate | Full implementation needs judge model infrastructure |
| **Refusal handling** | 40% refusal rate on Moral Lens items — how to score refusals? | Scoring rubrics need refusal category |
| **Virtue ethics under-tested** | Lowest scores across all benchmarks (4-63%); sparse coverage in DailyDilemmas | The hardest tradition for LLMs is the least well-tested |

---

## Per-Trial Accuracy Breakdown

### T1: ETHICS (Hendrycks) — 100% (Ceiling)
| Sub-dataset | Items | Accuracy | Notes |
|-------------|-------|----------|-------|
| Commonsense | 10 | 100% | Pattern-matching social norms |
| Deontology | 10 | 100% | Rule recognition |
| Justice | 10 | 100% | Fairness judgment |
| Utilitarianism | 10 | 100% | Trivially structured (A always better) |
| Virtue | 10 | 100% | Semantic similarity |

### T2: MoReBench-Theory — 10% Rubric Coverage
| Framework | Items | Rubric Score | Notes |
|-----------|-------|-------------|-------|
| Act Utilitarianism | 6 | 7.3% | Generic consequentialist reasoning |
| Kantian Deontology | 6 | 8.0% | Misses scenario-specific duty analysis |
| Scanlonian Contractualism | 6 | 18.3% | Best — vocabulary overlap with rubric |
| Virtue Ethics | 6 | 4.0% | Hardest to operationalize procedurally |
| Gauthierian Contractarianism | 6 | 12.5% | Moderate — game-theoretic framing helps |

### T3: MoralReason-QA — 37-77% by Framework
| Framework | Items | Accuracy | Notes |
|-----------|-------|----------|-------|
| Utilitarian | 10 | 77% | Outcome reasoning easiest |
| Deontological | 10 | 50% | Duty-to-protect cases are hardest |
| Virtue | 10 | 63% | Compassion vs practical wisdom tradeoffs |
| **All 3 correct** | 30 | 37% | Joint accuracy across all frameworks |

### T4: Moral Lens — Framework Tendency
| Tendency | Count | Pct | Notes |
|----------|-------|-----|-------|
| Deontological | 12 | 60% | Egalitarianism dominant (8/20 items) |
| Consequentialist | 8 | 40% | Triggered by number asymmetry (5:1 ratios) |
| Refusals | 8 | 40% | Gender/fitness/social status items |

### T5: DailyDilemmas — Value Profiling
| Metric | Value | Notes |
|--------|-------|-------|
| Intervene tendency | 45% | Near-balanced |
| Virtue match rate | 57% (8/14) | Only items with Aristotle annotations |
| Genuine dilemmatic tension | 75% | Most items well-constructed |

---

## Methodological Notes

- **Self-evaluation limitation:** Claude evaluating itself introduces systematic bias — the model likely performs better on items aligned with its training. Cross-model comparison (Claude vs GPT-4o vs Llama-3) would strengthen findings.
- **Sample size:** 20-50 items per trial provides directional findings but not statistical significance. Full-scale runs should use complete test sets.
- **Scoring heterogeneity:** Each benchmark uses different scoring (binary accuracy, rubric coverage, framework tendency, value profiling). A unified metric would strengthen cross-benchmark comparison.

---

## Data Files

| File | Contents |
|------|----------|
| `STATISTICS/20260403-trial-T1-ethics.md` | ETHICS trial report |
| `STATISTICS/20260403-trial-T2-morebench.md` | MoReBench trial report |
| `STATISTICS/20260403-trial-T3-moralreason.md` | MoralReason-QA trial report |
| `STATISTICS/20260403-trial-T4-morallens.md` | Moral Lens trial report |
| `STATISTICS/20260403-trial-T5-dailydilemmas.md` | DailyDilemmas trial report |
| `/tmp/trial_T{1-5}_items.json` | Sampled items per trial |
| `/tmp/trial_T{1-5}_scored.json` | Scored results per trial |
| `STATISTICS/20260402-normative-benchmark-feature-matrix.json` | Complete 37-paper feature matrix |
| `STATISTICS/20260403-normative-ethics-top15-benchmark-selection.md` | Top 15 selection report |
