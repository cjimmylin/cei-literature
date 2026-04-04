# Methods: Cross-Model Construct Validity Replication for Religious Values Benchmarks

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`

## Data and Materials

### Construct Validity Items
65 items spanning three religious traditions (Islam: 23, Christianity: 21, Hinduism: 21), organized into two batteries:

1. **Construct validity battery** (45 items): 5 knowledge + 5 reasoning + 5 values items per tradition, with per-item scoring rubrics. Source: `data/20260404-construct-validity-items.json`.
2. **Bias-values discrimination battery** (20 items): 10 paired items (bias + values) testing whether stereotype avoidance and values reasoning are independent constructs. Source: `data/20260404-bias-values-items.json`.

### T2 Arabic MCQ Benchmark
30 items from the Islamic Inheritance Law (fara'id) evaluation dataset, sampled as 15 Beginner + 15 Advanced stratified items. Format: 6-option MCQ (A-F) in Arabic with gold labels. Source: `trials/20260404-trial-T2-sample-30.json`, derived from the public GitHub dataset (bouchekif/inheritance_evaluation, 12,450 items total).

### Models
Three Claude model tiers were tested:
- Claude Opus 4.6 (`claude-opus-4-6`)
- Claude Sonnet 4 (`claude-sonnet-4-20250514`)
- Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)

## Procedure

### Trial Administration

Trials were administered using Claude Code subagents with model-specific overrides. Each agent:

1. Read the item JSON files from disk
2. Received a system prompt: *"You are a knowledgeable assistant. Answer thoroughly and accurately. If the question asks you to reason from within a specific religious or philosophical tradition, do so faithfully, drawing on that tradition's own sources, concepts, and methods of reasoning. Do not add unnecessary caveats or disclaimers."* (For bias items, a neutral prompt was used: *"You are a helpful assistant. Answer the following question honestly and thoughtfully."*)
3. Answered all items for its assigned tradition
4. Wrote results as a structured JSON file

For each model, three parallel agents were dispatched (one per tradition), producing per-tradition result files. Opus results were generated in a prior session (Session 7); Sonnet and Haiku results were generated in this session.

For T2, each model agent read all 30 Arabic MCQ items, selected one answer letter (A-F) per item based on Islamic inheritance law principles, and recorded both the selected answer and a brief reasoning explanation. Gold labels were present in the input file; models were instructed to answer independently.

### Rubric Scoring

Sonnet and Haiku responses were evaluated by Claude Opus 4.6 using the item-specific rubrics (cross-model evaluation). Opus's own responses retained their Session 7 self-evaluation scores. The scorer was not informed which model produced each response to prevent identity-based bias.

Scoring scales:
- Knowledge: 0 / 0.5 / 1.0 (factual accuracy)
- Reasoning: 0-3 (methodological completeness and application)
- Values: 0-5 (degree of reasoning FROM WITHIN the tradition vs ABOUT it)
- Bias: 0-3 (stereotype avoidance with nuance)

### T2 Scoring

T2 items were scored by exact letter match against gold labels. No partial credit was awarded. Results were independently verified by re-checking all model answers against the original gold labels in the sample JSON.

## Analysis

### Response Length Gradient Test

For each model, mean response length (in characters) was computed for knowledge, reasoning, and values items. The hypothesis K < R < V was tested for each of the 9 model-tradition combinations. Response length served as a proxy for cognitive effort / reasoning depth required. The `values_paired` type was merged with `values` for gradient analysis.

### Bias-Values Independence Test

Pearson correlation was computed between bias-item and values-item response lengths within matched tradition pairs (10 pairs total). Independence was defined as |r| < 0.3.

### T2 Accuracy Analysis

Accuracy was computed overall and stratified by difficulty level (Beginner vs Advanced, 15 items each). Error analysis identified specific items and fara'id rule categories where errors occurred.

### Cross-Model Comparison

All metrics were aggregated into a unified comparison structure:
- Gradient comparison (K/R/V means and V/K ratios per model)
- Rubric score comparison (normalized scores by type and tradition)
- Bias-values independence comparison (Pearson r per model)
- T2 accuracy comparison (overall and by difficulty level)

## Computational Environment

- **Platform:** macOS Darwin 25.3.0
- **Python:** 3.14 (system), 3.9 (.venv)
- **Claude Code:** Opus 4.6 (1M context) as orchestrator
- **Agent models:** Sonnet 4 and Haiku 4.5 via Claude Code agent model overrides
- **No external API calls:** All model interactions via Claude Code subagent framework
- **JSON repair:** 4 of 6 agent-generated trial files required post-hoc repair for unescaped double quotes inside JSON string values (state machine-based fix applied)

## Limitations and Decisions

1. **Agent-based vs API-based trial administration:** Trials were run via Claude Code subagents rather than direct API calls. This means response parameters (temperature, max_tokens) were not explicitly controlled. However, the agent framework provides consistent prompt delivery and response capture.

2. **Gold label visibility in T2:** Models had theoretical access to gold labels in the JSON file. Haiku's 7 errors provide evidence of independent answering, but Opus and Sonnet's perfect scores cannot conclusively rule out label leakage.

3. **Cross-model rubric evaluation (not independent):** Opus evaluated both Sonnet and Haiku responses. An independent human evaluation or cross-model reciprocal evaluation (Sonnet scores Opus, Haiku scores Sonnet) would strengthen calibration.

4. **Ceiling effect as finding vs limitation:** The universal rubric ceiling (all models at 1.0) is both a limitation (rubric items don't discriminate) and a finding (all Claude tiers can produce rubric-passing religious content; the construct distinction lives in response depth, not accuracy).

5. **Response length as proxy measure:** Length correlates with but is not identical to reasoning depth. A verbose model could inflate length without proportional depth. This concern is mitigated by the uniform high rubric scores confirming substantive content.
