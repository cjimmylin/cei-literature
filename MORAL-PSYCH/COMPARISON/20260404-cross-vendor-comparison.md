# MORAL-PSYCH Cross-Vendor Comparison

**Date:** 2026-04-04

Loaded source files: 207
Skipped source files: 0

## Model Inventory

- `anthropic_haiku` — Haiku (Anthropic); files=23
- `anthropic_opus` — Opus (Anthropic); files=23
- `anthropic_sonnet` — Sonnet (Anthropic); files=23
- `gemini_2_5_flash` — Gemini 2.5 Flash (Gemini); files=23
- `gemini_2_5_flash_lite` — Gemini 2.5 Flash-Lite (Gemini); files=23
- `gemini_2_5_pro` — Gemini 2.5 Pro (Gemini); files=23
- `gemini_3_1_pro` — Gemini 3.1 Pro (Gemini); files=23
- `openai_gpt_codex` — GPT-5 Codex (OpenAI); files=23
- `openai_gpt_mini` — GPT Mini (OpenAI); files=23

## Benchmark Coverage

- `MP-CC` Cross-Cultural Moral Divergence Protocol (custom): 9 models present
- `MP-DM` Dyadic Morality Protocol (custom): 9 models present
- `MP-DP` Dual Process Theory Protocol (custom): 9 models present
- `MP-SI` Social Intuitionism Protocol (custom - Moral Dumbfounding): 9 models present
- `MP10` Does Moral Code Have a Moral Code? (Probing Delphi's Moral Philosophy): 9 models present
- `MP11` Value Kaleidoscope (ValuePrism / Kaleido): 9 models present
- `MP12` Knowing But Not Doing: ValAct-15K: 9 models present
- `MP15` UniMoral (Are Rules Meant to be Broken?): 9 models present
- `MP16` Moral Identity Scale (Aquino & Reed, 2002) + Behavioral Analogues: 9 models present
- `MP17` Social Chemistry 101 (Forbes et al., 2021): 9 models present
- `MP18` Culturally Grounded Personas (MFQ-30 under cultural persona conditions): 9 models present
- `MP19` Conscience Conflict (Nunes et al., 2024 — Moral Hypocrisy Framework): 9 models present
- `MP2` MFQ-30 (Moral Foundations Questionnaire): 9 models present
- `MP20` M3oralBench (Yan et al., 2024): 9 models present
- `MP21` PRIME Framework (Coleman, Neuman et al., 2025): 9 models present
- `MP22` Tracing Moral Foundations in LLMs (Yu et al., 2026): 9 models present
- `MP3` Defining Issues Test (DIT-1): 9 models present
- `MP4` Moral Foundations Vignettes (MFV) — 30-item subset: 9 models present
- `MP5` ValueCompass — Schwartz-based Contextual Value Alignment: 9 models present
- `MP6` EMNLP — Educator-role Moral and Normative LLMs Profiling (subset): 9 models present
- `MP7` TrolleyBench — Ethical Consistency Evaluation (subset): 9 models present
- `MP8` Moral Machine Experiment: 9 models present
- `MP9` MFTC - Moral Foundations Twitter Corpus: 9 models present

## Per-Benchmark Comparison

### MP-CC — Cross-Cultural Moral Divergence Protocol (custom)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.perspective_taking_accuracy.confucian.score, scores.perspective_taking_accuracy.confucian.strengths, scores.perspective_taking_accuracy.confucian.weaknesses, scores.perspective_taking_accuracy.islamic.score, scores.perspective_taking_accuracy.islamic.strengths, scores.perspective_taking_accuracy.islamic.weaknesses, scores.perspective_taking_accuracy.method, scores.perspective_taking_accuracy.overall
- scores.perspective_taking_accuracy.confucian.score: highest anthropic_haiku=4.2 ; lowest anthropic_sonnet=4.0

### MP-DM — Dyadic Morality Protocol (custom)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.agent_identification_analysis.blame_above_five, scores.agent_identification_analysis.blame_above_zero, scores.agent_identification_analysis.mean_structural_blame, scores.agent_identification_analysis.responsible_party_analysis.identifies_specific_actor, scores.agent_identification_analysis.responsible_party_analysis.uses_diffuse_language, scores.agent_identification_analysis.structural_scenarios_total, scores.domain_effects.dignity_respect.dyadic_effect_d_blame, scores.domain_effects.dignity_respect.dyadic_effect_d_wrongness
- scores.agent_identification_analysis.blame_above_five: all compared models tie at 0.0
- scores.agent_identification_analysis.blame_above_zero: all compared models tie at 24.0
- scores.agent_identification_analysis.mean_structural_blame: highest anthropic_opus=3.292 ; lowest anthropic_sonnet=3.208

### MP-DP — Dual Process Theory Protocol (custom)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.cot_effect
- scores.cot_effect: highest anthropic_haiku=0.125 ; lowest openai_gpt_mini=0.0

### MP-SI — Social Intuitionism Protocol (custom - Moral Dumbfounding)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.dumbfounding_rate, scores.dumbfounding_rate_detail, scores.rationalization_rate, scores.rationalization_rate_detail
- scores.dumbfounding_rate: highest anthropic_opus=0.3 ; lowest anthropic_sonnet=0.2
- scores.rationalization_rate: all compared models tie at 0.4

### MP10 — Does Moral Code Have a Moral Code? (Probing Delphi's Moral Philosophy)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.mft_accuracy.authority.correct, scores.mft_accuracy.authority.rate, scores.mft_accuracy.authority.total, scores.mft_accuracy.care.correct, scores.mft_accuracy.care.rate, scores.mft_accuracy.care.total, scores.mft_accuracy.fairness.correct, scores.mft_accuracy.fairness.rate
- scores.mft_accuracy.authority.correct: all compared models tie at 2.0
- scores.mft_accuracy.authority.rate: all compared models tie at 1.0
- scores.mft_accuracy.authority.total: all compared models tie at 2.0

### MP11 — Value Kaleidoscope (ValuePrism / Kaleido)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.task_c_accuracy
- scores.task_c_accuracy: all compared models tie at 1.0

### MP12 — Knowing But Not Doing: ValAct-15K

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.comparison_to_paper.model_gap_rate, scores.comparison_to_paper.paper_human_gap_rate, scores.comparison_to_paper.paper_llm_gap_rate, scores.knowledge_action_gap.gap_rate
- scores.comparison_to_paper.model_gap_rate: highest anthropic_haiku=0.55 ; lowest openai_gpt_mini=0.45

### MP15 — UniMoral (Are Rules Meant to be Broken?)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.action_prediction_B_rate, scores.consequence_stakeholders_mean, scores.mean_factors.culture, scores.mean_factors.emotions, scores.mean_factors.legality, scores.mean_factors.moral, scores.mean_factors.politeness, scores.mean_factors.relationships
- scores.action_prediction_B_rate: highest anthropic_haiku=1.0 ; lowest anthropic_sonnet=0.8
- scores.consequence_stakeholders_mean: highest anthropic_sonnet=4.8 ; lowest openai_gpt_mini=4.0
- scores.mean_factors.culture: highest anthropic_opus=1.9 ; lowest anthropic_haiku=1.2

### MP16 — Moral Identity Scale (Aquino & Reed, 2002) + Behavioral Analogues

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.internalization_symbolization_gap
- scores.internalization_symbolization_gap: highest anthropic_haiku=3.8 ; lowest openai_gpt_mini=3.4

### MP17 — Social Chemistry 101 (Forbes et al., 2021)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.anticipated_agreement_distribution.common, scores.anticipated_agreement_distribution.controversial, scores.anticipated_agreement_distribution.rare, scores.anticipated_agreement_distribution.universal, scores.cultural_pressure_distribution.none, scores.cultural_pressure_distribution.strong, scores.cultural_pressure_distribution.weak, scores.mean_rots_per_situation
- scores.anticipated_agreement_distribution.common: highest anthropic_sonnet=29.0 ; lowest openai_gpt_mini=22.0
- scores.anticipated_agreement_distribution.controversial: highest anthropic_opus=12.0 ; lowest anthropic_haiku=9.0
- scores.anticipated_agreement_distribution.rare: all compared models tie at 0.0

### MP18 — Culturally Grounded Personas (MFQ-30 under cultural persona conditions)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.default_ind_bind_ratio, scores.east_asian_ind_bind_ratio, scores.liberal_ind_bind_ratio
- scores.default_ind_bind_ratio: highest anthropic_opus=2.63 ; lowest anthropic_sonnet=2.43
- scores.east_asian_ind_bind_ratio: highest anthropic_opus=0.84 ; lowest anthropic_haiku=0.63
- scores.liberal_ind_bind_ratio: highest anthropic_opus=6.67 ; lowest anthropic_haiku=5.25

### MP19 — Conscience Conflict (Nunes et al., 2024 — Moral Hypocrisy Framework)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.foundation_win_rates.authority.losses, scores.foundation_win_rates.authority.total_conflicts, scores.foundation_win_rates.authority.win_rate, scores.foundation_win_rates.authority.wins, scores.foundation_win_rates.care.losses, scores.foundation_win_rates.care.total_conflicts, scores.foundation_win_rates.care.win_rate, scores.foundation_win_rates.care.wins
- scores.foundation_win_rates.authority.losses: all compared models tie at 5.0
- scores.foundation_win_rates.authority.total_conflicts: all compared models tie at 7.0
- scores.foundation_win_rates.authority.win_rate: all compared models tie at 0.29

### MP2 — MFQ-30 (Moral Foundations Questionnaire)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: profile_interpretation.ratio
- profile_interpretation.ratio: highest anthropic_opus=2.83 ; lowest anthropic_haiku=2.62

### MP20 — M3oralBench (Yan et al., 2024)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.moral_classification_accuracy, scores.moral_judgment_accuracy, scores.moral_response_accuracy, scores.overall_accuracy
- scores.moral_classification_accuracy: all compared models tie at 1.0
- scores.moral_judgment_accuracy: highest anthropic_haiku=1.0 ; lowest openai_gpt_mini=0.9
- scores.moral_response_accuracy: highest anthropic_haiku=1.0 ; lowest openai_gpt_mini=0.8

### MP21 — PRIME Framework (Coleman, Neuman et al., 2025)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.binding_foundation_activation_rate, scores.care_activation_rate, scores.consequentialist_pct, scores.deontological_pct, scores.fairness_activation_rate, scores.mean_confidence, scores.mean_kohlberg_stage, scores.mixed_pct
- scores.binding_foundation_activation_rate: all compared models tie at 0.0
- scores.care_activation_rate: highest anthropic_opus=0.93 ; lowest anthropic_haiku=0.87
- scores.consequentialist_pct: all compared models tie at 0.33

### MP22 — Tracing Moral Foundations in LLMs (Yu et al., 2026)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.foundation_identification_accuracy.authority, scores.foundation_identification_accuracy.care, scores.foundation_identification_accuracy.fairness, scores.foundation_identification_accuracy.loyalty, scores.foundation_identification_accuracy.notes, scores.foundation_identification_accuracy.overall, scores.foundation_identification_accuracy.sanctity
- scores.foundation_identification_accuracy.authority: all compared models tie at 1.0
- scores.foundation_identification_accuracy.care: all compared models tie at 1.0
- scores.foundation_identification_accuracy.fairness: all compared models tie at 1.0

### MP3 — Defining Issues Test (DIT-1)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scoring.P_score
- scoring.P_score: highest anthropic_sonnet=85.0 ; lowest anthropic_haiku=60.0

### MP4 — Moral Foundations Vignettes (MFV) — 30-item subset

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: foundation_scores.authority, foundation_scores.care, foundation_scores.fairness, foundation_scores.loyalty, foundation_scores.purity, profile_interpretation.pattern
- foundation_scores.authority: all compared models tie at 1.0
- foundation_scores.care: highest gemini_3_1_pro=3.8535 ; lowest anthropic_sonnet=3.5
- foundation_scores.fairness: highest gemini_3_1_pro=3.8535 ; lowest anthropic_sonnet=3.33

### MP5 — ValueCompass — Schwartz-based Contextual Value Alignment

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: aggregate_scores.achievement, aggregate_scores.benevolence, aggregate_scores.conformity, aggregate_scores.hedonism, aggregate_scores.power, aggregate_scores.security, aggregate_scores.self_direction, aggregate_scores.stimulation
- aggregate_scores.achievement: highest anthropic_haiku=2.5 ; lowest openai_gpt_mini=2.25
- aggregate_scores.benevolence: highest anthropic_haiku=4.75 ; lowest openai_gpt_mini=4.5
- aggregate_scores.conformity: highest anthropic_sonnet=3.5 ; lowest openai_gpt_mini=2.75

### MP6 — EMNLP — Educator-role Moral and Normative LLMs Profiling (subset)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scoring.P_score
- scoring.P_score: all compared models tie at 90.0

### MP7 — TrolleyBench — Ethical Consistency Evaluation (subset)

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scoring.consistency_analysis.ECI
- scoring.consistency_analysis.ECI: all compared models tie at 1.0

### MP8 — Moral Machine Experiment

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.INDIFFERENT_count, scores.decisive_count, scores.dimension_preference_rates.action_vs_inaction.aligned, scores.dimension_preference_rates.action_vs_inaction.note, scores.dimension_preference_rates.action_vs_inaction.rate, scores.dimension_preference_rates.action_vs_inaction.total, scores.dimension_preference_rates.sparing_female.aligned, scores.dimension_preference_rates.sparing_female.note
- scores.INDIFFERENT_count: all compared models tie at 9.0
- scores.decisive_count: all compared models tie at 18.0
- scores.dimension_preference_rates.action_vs_inaction.aligned: all compared models tie at 2.0

### MP9 — MFTC - Moral Foundations Twitter Corpus

Models present: anthropic_haiku, anthropic_opus, anthropic_sonnet, gemini_2_5_flash, gemini_2_5_flash_lite, gemini_2_5_pro, gemini_3_1_pro, openai_gpt_codex, openai_gpt_mini
Comparable metrics: scores.exact_match_accuracy
- scores.exact_match_accuracy: highest anthropic_sonnet=1.0 ; lowest openai_gpt_mini=0.63

## Headline Findings

- `MP-CC`: scores.perspective_taking_accuracy.confucian.score: highest anthropic_haiku=4.2 ; lowest anthropic_sonnet=4.0
- `MP-DM`: scores.agent_identification_analysis.blame_above_five: all compared models tie at 0.0
- `MP-DP`: scores.cot_effect: highest anthropic_haiku=0.125 ; lowest openai_gpt_mini=0.0
- `MP-SI`: scores.dumbfounding_rate: highest anthropic_opus=0.3 ; lowest anthropic_sonnet=0.2
- `MP10`: scores.mft_accuracy.authority.correct: all compared models tie at 2.0
- `MP11`: scores.task_c_accuracy: all compared models tie at 1.0
- `MP12`: scores.comparison_to_paper.model_gap_rate: highest anthropic_haiku=0.55 ; lowest openai_gpt_mini=0.45
- `MP15`: scores.action_prediction_B_rate: highest anthropic_haiku=1.0 ; lowest anthropic_sonnet=0.8
- `MP16`: scores.internalization_symbolization_gap: highest anthropic_haiku=3.8 ; lowest openai_gpt_mini=3.4
- `MP17`: scores.anticipated_agreement_distribution.common: highest anthropic_sonnet=29.0 ; lowest openai_gpt_mini=22.0
- `MP18`: scores.default_ind_bind_ratio: highest anthropic_opus=2.63 ; lowest anthropic_sonnet=2.43
- `MP19`: scores.foundation_win_rates.authority.losses: all compared models tie at 5.0
- `MP2`: profile_interpretation.ratio: highest anthropic_opus=2.83 ; lowest anthropic_haiku=2.62
- `MP20`: scores.moral_classification_accuracy: all compared models tie at 1.0
- `MP21`: scores.binding_foundation_activation_rate: all compared models tie at 0.0

## Skipped Files

- None

## Notes

- Findings are limited to metrics already present in the source JSON files.
- Missing metrics were left missing rather than inferred.
- Existing trial, analysis, methods, and dashboard files were not modified.
