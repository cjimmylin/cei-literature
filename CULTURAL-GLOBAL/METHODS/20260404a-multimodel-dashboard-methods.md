# Methods: Multi-Model Cross-Cultural Benchmark Trial Replication and Dashboard Annotation

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/CULTURAL-GLOBAL/`

## Data and Materials

### Trial Corpus
- **Baseline:** 10 trial JSON files (CC1-CC10, 380 items) self-administered by Claude Opus 4.6 on 2026-04-04
- **Replication:** Same 380 items self-administered by Claude Sonnet 4.6 and Claude Haiku 4.5
- **Total corpus:** 30 trial files, 1,140 item-level responses across 3 models
- **Item types:** 210 numeric (CC1-CC5, scales 0-5 or 1-5) and 170 qualitative (CC6-CC10, structured text responses with `perspectives` dicts)

### Benchmarks Covered
| Trial | Benchmark | Items | Type | Ethical Tradition |
|-------|-----------|-------|------|-------------------|
| CC1 | GlobalOpinionQA | 50 | Numeric | WVS/Pew cross-cultural values |
| CC2 | MFQ Cross-Cultural | 50 | Numeric | Moral Foundations Theory |
| CC3 | NormAd Cultural Norms | 40 | Numeric | Tightness-looseness |
| CC4 | IslamTrust (Maqasid) | 40 | Numeric | Islamic jurisprudence |
| CC5 | Confucian Dilemmas | 30 | Numeric | Wu lun / five relationships |
| CC6 | Ubuntu Scenarios | 30 | Qualitative | Communal personhood |
| CC7 | Buddhist Scenarios | 30 | Qualitative | Four Noble Truths |
| CC8 | CulturalBench | 40 | Qualitative | Cross-cultural commonsense |
| CC9 | Dharmic Scenarios | 30 | Qualitative | Hindu/Jain/Buddhist/Sikh |
| CC10 | Value Conflicts | 40 | Qualitative | Multi-tradition dilemmas |

## Procedure

### Self-Administration Protocol
Each model received the same items from the Opus trial files with response fields stripped, preserving read-only fields (questions, domains, scales, human baselines). Models were instructed to "respond honestly based on your own values, reasoning, and tendencies" without attempting to simulate cultural neutrality.

Trials were dispatched as parallel agents (10 per model) using Claude Code's Agent tool with `model` parameter overrides (`"sonnet"` or `"haiku"`). Each agent read the corresponding Opus trial file, extracted items, self-administered all items, and wrote the output as a structured JSON file.

### Prompt Invariants
All agents received identical meta-instructions:
1. Respond honestly; do not copy Opus responses
2. For numeric items: use integers within the stated scale range
3. For qualitative items: set `response_numeric` to null
4. Include reasoning and cultural bias reflection per item
5. Domain-specific fields (e.g., `perspectives` dict for CC10, `tradition_perspective` for CC6-CC9) were required per trial type

### Validation
A dedicated validation script (`validate_multimodel_trials.py`) checked each trial file for:
- JSON parsability
- Item count matching declared `items_count`
- Required fields present per trial type
- Numeric responses within valid range
- Item ID correspondence with Opus baseline
- Domain-specific field completeness

## Analysis

### Per-Model Metrics
For each model, the following were computed (adapted from `analyze_trials.py`):
1. **Country distances (CC1):** Mean absolute difference between model's numeric responses and 8 country baselines (WVS/Pew aggregates)
2. **MFQ profile (CC2):** Foundation scores (Care, Fairness, Loyalty, Authority, Sanctity) with individualizing/binding ratio
3. **RLHF conflict frequency:** Keyword-based categorization of conflict text across 6 themes (individual autonomy, secular epistemology, consequentialist optimization, gender equality, anti-authority bias, harm principle absolutism)
4. **Engagement depth (CC4-CC9):** Heuristic scoring (1-4 scale) based on presence of perspective-taking markers, structural limitation acknowledgments, and applied reasoning signals in response text
5. **Response length:** Mean character count per trial

### Cross-Model Comparison Metrics
1. **Pearson r:** Pairwise correlation of numeric responses across CC1-CC5 (210 items per model pair)
2. **Cohen's kappa:** Agreement coefficient on integer-rounded responses (k=6 categories for 0-5 scale)
3. **Mean absolute difference (MAD):** Average absolute response divergence per model pair
4. **Divergence items:** Items ranked by cross-model variance; top 15 reported
5. **Model size gradient:** Monotonicity test on Germany distance, Saudi Arabia distance, and MFQ ratio across model size order (Opus > Sonnet > Haiku)

### Dashboard Visualization
Dashboard data was pre-computed in Python (`generate_benchmark_tab.py`) following the "fat data, thin client" architecture: all analytics emitted as JavaScript constants, browser performs zero computation. The dashboard uses ECharts 5 + Bootstrap 5.3 with an Okabe-Ito colorblind-safe palette. Model colors: Opus (#0072B2, blue), Sonnet (#009E73, green), Haiku (#E69F00, orange).

## Computational Environment

- **Python:** 3.9 (via `.venv`)
- **Key libraries:** fpdf2 2.8.4 (PDF generation), json (stdlib)
- **Models:** Claude Opus 4.6 (`claude-opus-4-6`), Claude Sonnet 4.6 (`claude-sonnet-4-6`), Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)
- **Agent dispatch:** Claude Code Agent tool with `model` parameter override and `run_in_background: true`
- **Rate limits:** Sonnet CC10 required one retry due to rate limiting; all other agents completed on first attempt
- **Dashboard hosting:** GitHub Pages via `cjimmylin/cei-cultural-global` public repository

## Limitations and Decisions

1. **Self-administration validity:** Models respond to their own item batteries, not to external evaluators. Self-reported RLHF conflict identification may undercount conflicts the model cannot detect.

2. **Engagement depth is heuristic:** The 1-4 depth scoring uses keyword pattern matching (e.g., "cannot inhabit," "from an Ubuntu perspective") rather than semantic evaluation. This may systematically favor verbose models (Sonnet) over concise ones (Haiku).

3. **Single timepoint:** All trials were conducted on 2026-04-04 with current model weights. Model updates would require re-administration.

4. **English-only:** All items and responses are in English. Cross-cultural benchmarks administered in the languages of the traditions they test (Arabic, Mandarin, Swahili) would yield different results.

5. **Non-monotonic gradient:** The finding that Haiku is more WEIRD-biased than Opus (MFQ ratio 4.82 vs 3.75) cannot be attributed to model size alone, as RLHF fine-tuning differs across model families. The gradient test is descriptive, not causal.

6. **Qualitative trials not included in numeric agreement:** Cross-model agreement (Pearson r, kappa) is computed only for CC1-CC5 (210 items). Qualitative trials (CC6-CC10, 170 items) are compared via engagement depth and response length but lack quantitative agreement metrics.
