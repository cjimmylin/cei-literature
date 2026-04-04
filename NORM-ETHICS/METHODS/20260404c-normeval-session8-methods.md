# Methods: Cross-Model Replication of NormEval Benchmark Trials

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/NORM-ETHICS/`

## Data and Materials

**Trial Items:** Items were drawn from the original NormEval implementation trials (T1–T15), which were previously documented as markdown narrative files in `STATISTICS/20260403-trial-T*.md` and `20260404-trial-T*.md`. For the cross-model replication, only individually documented items were used — items described only in summarized ranges (e.g., "A4–A8: further items on...") were not reconstructed. Coverage ranged from 100% (T14, 22/22 items individually documented) to approximately 40% (T6, 12/30 items).

**Models tested:** Claude Opus 4.6 (baseline, from prior sessions), Claude Sonnet 4.6 (mid-capability), and Claude Haiku 4.5 (small/fast). Model IDs: `claude-opus-4-6`, `claude-sonnet-4-6`, `claude-haiku-4-5`.

**Benchmarks replicated (10 of 15):** T6 (PrinciplismQA), T7 (Moral Persuasion), T8 (AMAeval), T9 (JETHICS), T10 (Pluralistic Moral Gap), T11 (MedEthicsQA), T12 (UniMoral), T13 (Greatest Good Benchmark / Oxford Utilitarianism Scale), T14 (PNAS Cognitive Biases), T15 (ProMoralBench).

**Not replicated (5):** T1–T5 (ETHICS, MoReBench, MoralReason-QA, MoralLens, DailyDilemmas) — these had fewer than 8 individually documented items each, limiting statistical power for cross-model comparison.

## Procedure

### Item Preparation

Trial items were extracted directly from the markdown trial reports without a formal parsing script, given the heterogeneous narrative formats. For each trial, items were identified by their bold headers (`**A1 (MCQ):**`, `**HC1:**`, `**IB1:**`, etc.), and item text, response format, options (for MCQ), and ground truth were recorded manually. Items summarized in ranges were excluded and documented as partial coverage.

### Model Administration

For each trial and each model (Sonnet, Haiku), a Claude Code agent was spawned using the `model` parameter override (`model="sonnet"` or `model="haiku"`). Each agent received:

1. A standardized assessment prompt specifying the benchmark context, response format requirements (letter selection for MCQ, 1–7 integer for Likert, binary "Right/Wrong" for moral dilemma items), and an instruction to return all responses as a single JSON object.
2. The full item set for that trial, verbatim from the original trial documentation (including Japanese text for T9, Likert item text for T13, scenario descriptions for T14).

Administration was conducted in batches of up to 3 parallel agents (Claude Code concurrency limit). Sessions were interrupted by rate limits on two occasions; work resumed after reset.

### Response Collection

Agent responses were parsed from the returned JSON objects. For Sonnet and Haiku, responses were written to per-trial JSON files (`20260404-trial-T{N}-{name}-{model}.json`) using the same schema established for Opus trials:

```json
{
  "trial_id": "...",
  "benchmark": "...",
  "model": "...",
  "administration_date": "2026-04-04",
  "administration_method": "Claude Code agent, standardized prompt",
  "items": [{...}],
  "summary": {...}
}
```

## Analysis

### Per-Trial Scoring

For trials with binary or MCQ ground truth (T6, T9, T11), accuracy was computed as percentage correct. For Likert-scale trials (T13), mean scores were computed separately for the Impartial Beneficence (IB) and Instrumental Harm (IH) subscales. For scenario judgment trials (T10, T14), agreement with the expected majority human response was computed. For persuasion trials (T7), the Decision Change Rate (DCR = changed positions / total scenarios) was computed per model.

### Cross-Model Agreement

Pairwise agreement was computed for each item where Sonnet and Haiku produced the same response as Opus (binary agreement). For Likert items, mean absolute difference between model pairs was used. Across all 134 comparable items:

- Opus–Sonnet: 85.1% agreement
- Sonnet–Haiku: 82.1% agreement
- Opus–Haiku: 77.6% agreement
- All three: 73.1% agreement

### E3 Feature Population

The `E3_cross_model_agreement` field in `20260404-normeval-v2-feature-scores.json` (previously `null` for all 37 benchmarks) was populated for the 9 benchmarks with directly mappable v2 IDs. Agreement metrics were structured as `{opus_sonnet, opus_haiku, sonnet_haiku, three_way}` Spearman-equivalent agreement rates, derived from per-trial results.

### Dashboard Integration

The cross-model comparison data was embedded in the NormEval dashboard (GitHub Pages) through two mechanisms:

1. The Python generator (`generate_normeval_dashboard.py`) was updated to load `20260404-normeval-cross-model-comparison.json` and emit it as a `DATA_CROSS_MODEL` JavaScript constant in `data.js`.
2. Four ECharts visualizations were added to Tab 8 (Cross-Model) in `charts.js`: IH mean by model size, CBR rate on moral dilemmas, knowledge vs judgment agreement, and persuasion resistance (DCR).

## Computational Environment

- **Python:** 3.9 (system Python at `/opt/homebrew/bin/python3`)
- **Agent framework:** Claude Code CLI with `model` parameter override
- **Models tested:** `claude-sonnet-4-6`, `claude-haiku-4-5`
- **Dashboard:** ECharts 5.5.1, Bootstrap 5.3.3, GitHub Pages (public repo: `cjimmylin/cei-normeval-dashboard`)
- **Rate limits:** Sonnet and Haiku agents share a sub-agent rate limit that reset approximately every 2 hours during this session

## Limitations and Decisions

**Partial item coverage:** 5 of 15 trials (T1–T5) were not replicated due to insufficient individually documented items in the original markdown reports. The item sets for these trials were sampled to `/tmp/` during the original Opus trials and are no longer retrievable. A full replication would require re-downloading the original datasets and re-sampling with the documented seed (42) for T1.

**Single administration:** All trials were administered once per model (n=1) to match the Opus baseline protocol. No variance estimate is available. For publication, repeated administration with temperature variation would provide confidence intervals on the reported means.

**System prompt confound:** The Opus trials were administered with the full CEI project system prompt active (noted in the original trial metadata). Sonnet and Haiku agents received the standardized assessment-only prompt without the project context. This constitutes a methodological difference that should be noted in the paper. Future work should explicitly test the effect of system prompt on moral reasoning outputs.

**Single model family:** Results apply to the Claude model family (RLHF-trained models from Anthropic). The IH inverse scaling finding may not generalize to models trained with different alignment methods (e.g., RLAIF, constitutional AI from other providers).

**Persuasion starting-position asymmetry (T7):** Opus initially chose Action 2 (non-lethal) on S3 and was persuaded to Action 1 (lethal force); both Sonnet and Haiku initially chose Action 1. The DCR metric therefore conflates persuasion susceptibility with initial position differences. A proper persuasion trial would require that all models start from the same initial choice.
