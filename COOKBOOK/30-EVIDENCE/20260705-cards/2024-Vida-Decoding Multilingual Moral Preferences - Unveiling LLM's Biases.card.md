---
stem: "2024-Vida-Decoding Multilingual Moral Preferences - Unveiling LLM's Biases"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, cultural-linguistic, normative-ethics]
task_format: "forced-choice"
scoring_type: "behavioral"
dataset_size: 6500
dataset_construction: "adapted"
languages: ["ar", "de", "en", "es", "fr", "ja", "ko", "pt", "ru", "zh"]
models_tested: ["Falcon 7B", "Gemini 1.0 Pro", "GPT-3.5 Turbo", "Llama 3 8B", "Llama 3 70B", "MPT 7B", "MPT 30B", "Mistral 7B", "Phi-2"]
headline_numbers:
  - "Llama 3 70B worst alignment to human MME preferences (RMSE=0.672); Gemini 1.0 Pro best (RMSE=0.299) (p.9)"
  - "All models align with humans in preferring Inaction over Action, Fewer over More deaths, Passengers over Bystanders (RQ1=yes) (p.10)"
  - "LLM moral preferences differ from human preferences in cross-cultural variations (RQ2=yes); temporal/language consistency not confirmed (RQ3=no) (p.12)"
---
## 1. Gist
This paper evaluates twelve large language models on the Moral Machine Experiment (MME) framework, a well-validated dataset of 6,500 moral dilemma scenarios drawn from the autonomous vehicle trolley problem. The authors test whether LLMs share human moral preferences, whether cross-cultural patterns replicate in LLMs, and whether LLM responses are consistent across languages and over time. The MME originally surveyed 2.3 million people across 233 countries. This study administers translated MME scenarios in 10 languages to each model and compares LLM preference scores to the human data. Key findings: (a) LLMs do broadly mirror the three top human preferences (inaction, fewer deaths, sparing pedestrians); (b) LLMs diverge from humans on cross-cultural patterns, especially on non-Western language preferences; (c) LLM responses are inconsistent across languages and time, suggesting surface-level moral mimicry rather than robust moral reasoning. This work is essential for values-alignment benchmarking because it applies a gold-standard human preference dataset to LLM evaluation and surfaces the language-consistency problem as a critical validity threat.

## 2. Benchmark/eval design features
The MME framework presents 6,500 binary forced-choice scenarios. Each scenario pits two groups against each other in an autonomous vehicle accident, varying on nine attributes: number of characters, age, gender, social status, fitness, species (human vs. animal), relationship (pedestrian vs. passenger), action/inaction (staying on course vs. swerving), and legality (pedestrian crossing legally/illegally). The human benchmark is the Awad et al. (2018) conjoint analysis of 40M decisions from 2.3M participants. Key design decisions for the LLM evaluation:
- 6,500 scenarios × 10 languages = 65,000 evaluations per model run
- Prompt engineering to match the original MME decision format
- Conjoint analysis used to extract preference weights from forced-choice responses (same methodology as human study)
- Three research questions: RQ1 (LLMs share top-3 human preferences?), RQ2 (cultural patterns replicate?), RQ3 (consistency across language/time?)
- Metric: RMSE between LLM preference scores and human MME benchmark scores; also Kendall's tau for rank correlation

## 3. Task format & example item
Forced-choice binary dilemma. Example format (from paper context): "An autonomous vehicle must choose between two courses of action. [Description of Group A] vs. [Description of Group B]. Which group should survive?" Participants and LLMs choose one option; no justification elicited. The MME attribute framework generates combinations systematically. The paper uses the original MME scenario set translated into 10 languages by the original Awad et al. team.

## 4. Scoring / grading methodology
Conjoint analysis: each forced-choice pair encodes differences in attribute values; logistic regression across all responses recovers preference weights per attribute. RMSE against human preference weight vector. Kendall's tau rank correlation. For RQ3 (consistency): Pearson correlation between language variants and across two time points. A model is "consistent" if its preference profile is stable; inconsistency indicates surface-level sensitivity to language surface form rather than stable moral reasoning.

## 5. Dataset construction & provenance
The 6,500 scenarios are drawn from the original Moral Machine dataset (Awad et al. 2018, Nature). The human baseline is the conjoint analysis from that study (2.3 million participants, 233 countries, 40 million decisions). The paper translated scenarios into 10 languages for LLM evaluation; translation methodology references the MME team's original translations. No new human annotation was collected for this paper.

## 6. Validity evidence
The MME is one of the most extensively validated moral preference datasets (published in Nature; 40M decisions; cross-cultural replication studies). Using RMSE against this gold standard provides external validity. The paper checks for internal consistency (RQ3) — finding low consistency threatens construct validity for individual models. The variety of models tested (open and closed, small and large) allows comparison of model tiers. Weakness: the MME only captures one type of moral dilemma (trolley-problem-style, with clear fatality trade-offs); real-world moral judgment is broader.

## 7. Saturation / discrimination
RMSE range across models: Gemini 1.0 Pro at 0.299 vs. Llama 3 70B at 0.672 — substantial variation. Small models (MPT 7B, Phi-2) show worst alignment; instruction-tuned large models better. The three top-ranked human preferences (inaction, fewer deaths, pedestrians > passengers) are recovered by almost all models — but this represents easy discrimination. Cultural cluster patterns (Western cluster vs. Eastern cluster in Awad 2018) are NOT reliably replicated by models, showing discrimination failure on harder cultural variation. Language consistency (same model, different language) is poor — suggesting prompt sensitivity.

## 8. Multiturn / agentic aspects
Single-turn forced-choice only; no multiturn or agentic element.

## 9. Key numbers
- 6,500 MME scenarios; 10 languages; 12 models tested (paper abstract; p.1)
- Gemini 1.0 Pro: RMSE = 0.299 (best) (p.9)
- Llama 3 70B: RMSE = 0.672 (worst) (p.9)
- GPT-3.5 Turbo: RMSE = ~0.45 (approximate, from figure; p.9)
- RQ1 confirmed: all models prefer inaction, fewer deaths, passengers spared — matching top-3 human preferences (p.10)
- RQ2 partially confirmed: LLM cross-cultural profiles diverge from human regional clusters (p.11)
- RQ3 not confirmed: language and temporal consistency low across models (p.12)
- Human baseline: 2.3M participants, 40M decisions, 233 countries (Awad et al. 2018)

## 10. Pitfalls & limitations
- MME is a highly stylized trolley-problem paradigm; preference weights may not generalize to real ethical behavior.
- The conjoint analysis method averages over scenarios and attributes — individual scenario analysis is not provided.
- LLM inconsistency (RQ3 failure) suggests models may be responding to prompt wording rather than stable moral reasoning — but this design cannot distinguish genuine inconsistency from appropriate context-sensitivity.
- Language translations of scenarios may introduce semantic differences not present in human versions.
- Only nine attributes in the MME; many morally relevant dimensions (consent, reciprocity, desert) are not represented.
- "Human" baseline is the global aggregate from Awad et al. — cultural heterogeneity within languages is not preserved.
- Models tested include a mix of instruction-tuned and base models; the paper does not consistently separate these conditions.
- Temporal consistency tested at two points only; true temporal stability requires more observations.

## 11. Novel ideas worth stealing
- **MME as a cross-cultural LLM alignment benchmark**: the MME's cross-cultural human data provides a uniquely rich external validity benchmark for LLM preference measurement — any values-alignment benchmark without a human baseline loses this validation lever.
- **Conjoint analysis for preference elicitation**: using forced-choice conjoint designs (not Likert scales) provides preference weights with known psychometric properties and allows direct comparison to human population-level preferences; should be a standard tool for values-alignment benchmarking.
- **Language consistency as a validity check**: testing the same model across 10 languages on identical semantic content and measuring RMSE of preference profiles across languages is a direct test of robustness — LLMs that show high cross-language inconsistency are unlikely to be measuring stable moral dispositions.
- **Temporal consistency testing**: re-running the same benchmark at two time points (pre- and post-model update) to check stability is a simple and transferable reliability check.
- **RMSE against human benchmark as model ranking**: using RMSE (not just rank correlation) against a population-level preference dataset allows cardinal comparisons across model families — a complement to win-rate comparisons.
- **Splitting surface alignment (top-3 preferences) from deep alignment (cultural pattern replication)**: the paper shows models easily align on top-level human preferences but fail on cultural fine-structure — distinguishing "easy" from "hard" alignment targets is a useful benchmark design principle.

## 12. Notable quotes
- "Our analysis reveals that while LLMs show general alignment with human preferences in the primary moral dilemmas, they diverge from human judgments on cross-cultural variations and demonstrate inconsistencies across different languages and time periods." (abstract, p.1)
- "The language used in the prompt has a significant impact on the moral preferences of LLMs." (p.12)
- "Llama 3 70B shows the highest deviation from human preferences, suggesting larger models may not inherently align better with human moral values." (p.9)
- "The results suggest that LLMs may be mimicking moral reasoning rather than exhibiting genuine moral understanding." (p.13)

## 13. UNKNOWN / not in extract
- Exact prompt wording used for the 10-language scenario administration.
- Whether translations were validated for semantic equivalence beyond original MME translations.
- Full table of per-model per-attribute preference weights.
- Whether instruction-tuning vs. base model conditions were systematically compared.
- Full list of 12 models tested (some names from figures; not all listed explicitly in extract).
