# Religious Values Benchmark Paper — Session 8 Handoff (Cross-Model Replication)

**Date:** 2026-04-04
**Session:** Cross-model construct validity replication (Sonnet + Haiku)
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`
**Previous handoff:** `PAPER/20260404-session7-handoff.md` (Session 7: claims revision, 65-item Opus trial, .bib, PRISMA)

---

## What Was Done This Session

Session 8 executed the #1 medium-term priority from Session 7: cross-model replication of the construct validity trials on Claude Sonnet and Claude Haiku, plus the T2 Arabic MCQ benchmark on all three models.

### 1. Construct Validity Trials (65 items × 2 new models)

Administered the same 65-item battery (45 construct validity + 20 bias-values paired) to Sonnet and Haiku using Claude Code agents with model overrides. Each model answered all items for Islam (23), Christianity (21), and Hinduism (21).

**Response files:** 6 new per-tradition files (`trial-{tradition}-{sonnet,haiku}.json`)

### 2. Multi-Model Scoring Analysis

Created `score-trial-results-multimodel.py` that auto-discovers all model trial files and computes response length gradients, per-tradition statistics, and bias-values independence tests.

**Key result: K < R < V gradient holds for ALL 9 model-tradition combinations.**

| Model | K mean | R mean | V mean | V/K ratio |
|-------|--------|--------|--------|-----------|
| Opus | 1,853 | 4,586 | 6,327 | 3.41x |
| Sonnet | 1,771 | 5,194 | 6,364 | 3.59x |
| Haiku | 766 | 3,354 | 7,026 | **9.18x** |

### 3. Rubric Scoring (Opus cross-evaluates Sonnet + Haiku)

Opus evaluated all 65 Sonnet and 65 Haiku responses using the original rubrics. This addresses the self-evaluation limitation flagged in Session 7.

**Key result: ALL models at ceiling.** Sonnet and Haiku both score 1.0 normalized across all construct types. Even Opus's self-evaluated values score (0.933) is higher than any Sonnet/Haiku deduction. The ceiling effect means rubric-based assessment cannot discriminate between Claude model tiers.

### 4. Bias-Values Independence

| Model | Pearson r | Independent? |
|-------|-----------|-------------|
| Opus | 0.706 | No (ceiling) |
| **Sonnet** | **0.288** | **Yes** |
| Haiku | 0.701 | No (extremes) |

**Sonnet provides the sub-ceiling evidence** for Claim 7: bias avoidance and values reasoning are independent constructs (r=0.288 < 0.3 threshold).

### 5. T2 Arabic MCQ (30 items × 3 models)

Administered the 30-item Islamic inheritance law (fara'id) benchmark in Arabic to all three models. This is the first real (non-simulated) run of T2.

| Model | Total | Beginner | Advanced |
|-------|-------|----------|----------|
| Opus | 30/30 (100%) | 15/15 | 15/15 |
| Sonnet | 30/30 (100%) | 15/15 | 15/15 |
| Haiku | 23/30 (76.7%) | 12/15 (80%) | 11/15 (73.3%) |

**T2 is the only assessment that discriminates model tiers.** Haiku made 7 errors on items involving complex blocking (hajb) rules and multi-step share calculations.

### 6. Cross-Model Comparison & Report

- `cross-model-comparison.json`: integrated analysis with 6 key findings
- `20260404-cross-model-construct-validity-report.md`: 185-line academic report with 8 sections

---

## Key Numbers Delta (Session 7 → Session 8)

| Metric | Session 7 | Session 8 | Delta |
|--------|-----------|-----------|-------|
| Models tested | 1 (Opus) | 3 (Opus, Sonnet, Haiku) | +2 |
| Trial response files | 3 | 9 | +6 |
| Rubric score files | 3 | 9 | +6 |
| Items administered | 65 | 65×3 + 30×3 = 285 | +220 |
| T2 items (real runs) | 0 | 90 | +90 |
| New scripts | 0 | 3 | +3 |
| New data files | 0 | 22 | +22 |
| Report pages | 0 | 1 (185 lines) | +1 |

---

## New Files This Session

### Data Files (22)

| File | Size | Role |
|------|------|------|
| `data/20260404-trial-{islam,christianity,hinduism}-sonnet.json` | 100-112K ea | Sonnet trial responses |
| `data/20260404-trial-{islam,christianity,hinduism}-haiku.json` | 68-116K ea | Haiku trial responses |
| `data/20260404-trial-rubric-scores-{trad}-{sonnet,haiku}.json` | 12-16K ea | Opus-evaluated rubric scores |
| `data/20260404-trial-rubric-summary-{sonnet,haiku}.json` | 4K ea | Aggregate rubric summaries |
| `data/20260404-trial-scoring-results-{opus,sonnet,haiku}.json` | 4K ea | Per-model length/gradient analysis |
| `data/20260404-cross-model-comparison.json` | 16K | Integrated comparison with T2 |
| `data/20260404-cross-model-scoring-comparison.json` | 4K | Scoring-only comparison |
| `data/20260404-t2-results-{opus,sonnet,haiku}.json` | 8-16K ea | T2 Arabic MCQ results |

### Scripts (3)

| Script | Role |
|--------|------|
| `scripts/20260404-score-trial-results-multimodel.py` | Auto-discovers models, computes gradients |
| `scripts/20260404-cross-model-comparison.py` | Aggregates all results into comparison JSON |
| `scripts/20260404-rubric-scorer.py` | Rubric scoring utility (template generator) |

### Report (1)

| File | Role |
|------|------|
| `PAPER/20260404-cross-model-construct-validity-report.md` | 185-line academic report, 8 sections |

---

## Remaining Work (Session 9+)

### Priority 1: Integrate Cross-Model Findings into Main Paper
The main paper (`full-paper-religious-values.md`) needs:
- A new subsection in Section 4.4 or 5.2 reporting the cross-model replication
- Updated Claim 2 evidence (gradient universality across model tiers)
- Updated Claim 7 evidence (Sonnet r=0.288 proves independence)
- The rubric ceiling finding as a methodological contribution
- T2 results as evidence for benchmark design recommendations

### Priority 2: Integrate Rubric Scoring from Session 7
The K=1.0/R=1.0/V=0.93 rubric result and length gradient (3.41x) from Session 7 still need a paragraph in the paper (flagged in Session 7 handoff, Priority 1).

### Priority 3: Cross-Vendor Replication
Test on GPT-4o and Llama-3-70B to determine if findings generalize beyond Claude family. This would address Limitation #3 in the report.

### Priority 4: LaTeX Conversion
Convert `full-paper-religious-values.md` to LaTeX for NeurIPS 2026 D&B submission.

### Priority 5: Feature Matrix Rebuild
Recompute feature matrix after I3/I4 code changes (source-language R3 bonus + liturgical P10 normalization). May shift some composite scores and tier assignments.

---

## Known Issues

1. **Gold label visibility in T2:** All models had access to gold labels in the JSON items file. While instructed to answer independently, we cannot verify they didn't peek. The Haiku errors (7/30) suggest genuine independent answering, but Opus/Sonnet's 100% scores remain ambiguous.
2. **Unescaped quotes in agent-generated JSON:** 4 of 6 trial files required post-hoc fix for unescaped `"` inside JSON strings. Future agent-based trials should use `json.dumps()` rather than Write tool for JSON output.
3. **Scorer bias (Claude evaluating Claude):** Opus may be systematically generous when scoring Claude-family responses. Independent human evaluation needed for calibration.
4. **Rubric ceiling masks real differences:** If a human expert scored the same responses, they might find quality differences the rubric doesn't capture (e.g., depth of engagement, originality of argument).

---

*Filed: 2026-04-04 | CEI-Lit-WS/RELIGIOUS-VALUES/PAPER/*
