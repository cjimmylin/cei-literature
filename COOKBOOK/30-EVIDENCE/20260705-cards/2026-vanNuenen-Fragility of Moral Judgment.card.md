---
stem: "2026-vanNuenen-Fragility of Moral Judgment"
reader_model: "sonnet"
confidence: "low"
is_benchmark: true
theme_tags: [moral-psychology, validity-psychometrics, saturation-discrimination, normative-ethics]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 2939
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["GPT-4.1", "Claude 3.7", "DeepSeek V3", "Qwen2.5-72B"]
headline_numbers:
  - "Surface edits flip judgments in 7.5% of cases (abstract)"
  - "POV shifts flip judgments in 24.3% of cases (abstract)"
  - "Protocol choice yields only 67.6% agreement across prompting conditions (abstract)"
  - "4 models evaluated across 129K total judgments (abstract)"
---
## 1. Gist
This paper investigates the stability — or instability — of moral judgments produced by large language models. Using 2,939 real-world moral dilemmas sourced from the Reddit community r/AmItheAsshole (AITA), van Nuenen and Sachdeva construct a systematic perturbation study that stresses LLM moral judgment along three axes: surface-level edits (minor wording changes), point-of-view shifts (changing narrative perspective), and persuasion cues (adding rhetorical pressure). The core finding is that LLM moral judgments are fragile: they flip at meaningful rates under perturbations that should be irrelevant to a principled moral evaluation. This is highly relevant for values-alignment benchmarking because it demonstrates that benchmark scores measuring "moral judgment" may be capturing prompt-format sensitivity rather than genuine moral reasoning capacity.

## 2. Benchmark/eval design features
The study uses AITA dilemmas as a naturalistic corpus of everyday moral situations — distinct from stylized trolley-problem scenarios. Three perturbation families stress-test each dilemma: (1) surface edits that change wording without changing meaning, (2) POV shifts that reframe first-person vs. third-person narration, and (3) persuasion cues that add explicit pressure toward a verdict. The paper also varies prompting protocol (likely system prompt framing), finding that protocol choice alone produces only 67.6% agreement — meaning format decisions dominate moral content. The dual-process-adjacent framing situates findings within moral psychology: fast/intuitive vs. slow/deliberative processing in LLMs.

## 3. Task format & example item
Full text unavailable. Based on abstract: models are presented with AITA-style moral dilemmas and asked to render a verdict (e.g., "YTA" / "NTA" — "you're the asshole" / "not the asshole"), making this a forced-choice moral judgment task. No verbatim example items are available from the abstract alone.

n/a (full text unavailable)

## 4. Scoring / grading methodology
Judgment stability is assessed by measuring flip rates — the proportion of cases where a model reverses its verdict under a given perturbation. Exact-match comparison between perturbed and baseline responses. 129K total judgments across 4 models suggests multiple runs per dilemma per perturbation condition.

## 5. Dataset construction & provenance
2,939 dilemmas scraped from r/AmItheAsshole (Reddit). This community provides naturalistic, crowd-sourced moral dilemmas with community verdicts, making it an ecologically valid corpus of everyday ethics. Licensing and train/test splits unknown (full text unavailable). Contamination risk: AITA posts are public and likely in LLM training data, which is a significant concern for this evaluation design.

## 6. Validity evidence
The perturbation design itself serves as an implicit validity test: a morally robust model should not flip judgments under semantics-preserving changes. The 67.6% agreement under protocol variation is a direct validity concern — it shows that what is being measured is partly prompt-format sensitivity, not just moral reasoning. Human baselines, inter-rater reliability statistics, and factor analyses are unknown (full text unavailable).

## 7. Saturation / discrimination
With flip rates ranging from 7.5% (surface edits) to 24.3% (POV shifts), there is substantial discrimination across perturbation types — the benchmark differentiates between perturbation families. Whether individual models differ substantially from each other is unknown (full text unavailable).

## 8. Multiturn / agentic aspects
n/a — appears to be single-turn forced-choice evaluation based on the abstract description.

## 9. Key numbers
- 2,939 dilemmas from r/AmItheAsshole (abstract)
- 7.5% judgment flip rate under surface edits (abstract)
- 24.3% judgment flip rate under POV shifts (abstract)
- 67.6% agreement when varying prompting protocol (abstract)
- 129K total judgments across 4 models (abstract)
- 4 models tested: GPT-4.1, Claude 3.7, DeepSeek V3, Qwen2.5-72B (abstract)

## 10. Pitfalls & limitations
- **Contamination risk**: AITA posts are public internet text, almost certainly in training data for all tested models; community verdicts may also be memorized.
- **Protocol sensitivity**: The 67.6% agreement finding undercuts the benchmark's own reliability — results may be highly dependent on prompt wording choices made by researchers.
- **Ecological validity tradeoff**: AITA scenarios involve interpersonal social disputes, which may not generalize to other moral domains (harm, fairness, purity, authority).
- **No human baseline reported** (from abstract): Without knowing how humans perform under the same perturbations, it is unclear whether the flip rates reflect LLM-specific fragility or general human inconsistency.
- Full methodology, results tables, and discussion unavailable (full text unavailable).

## 11. Novel ideas worth stealing
- **Perturbation-based stability testing** as a validity check for any moral benchmark: run surface edits + POV shifts on existing items to measure how much scores reflect prompt-format sensitivity vs. moral content. This is a reusable diagnostic.
- **Reddit AITA corpus** as a source of naturalistic, crowd-validated moral dilemmas with ground-truth human verdicts — richer and more ecologically valid than hand-authored vignettes.
- **Protocol variation as a first-class variable**: systematically varying system prompt framing and reporting agreement rates across protocols reveals hidden benchmark fragility that single-protocol studies miss.
- **Dual-process framing applied to LLMs**: using the intuitive/deliberative distinction to hypothesize when models will be more vs. less stable could yield principled predictions testable in new benchmarks.
- **Flip rate as a metric**: reporting % of items where verdict flips under perturbation is more informative than aggregate accuracy — it directly measures the robustness of moral judgment rather than average performance.

## 12. Notable quotes
Full text unavailable — no verbatim quotes can be provided.

## 13. UNKNOWN / not in extract
- Full methodology section (full text unavailable)
- Exact perturbation definitions and examples
- Per-model breakdown of flip rates and agreement scores
- Human baseline performance
- Inter-rater reliability statistics
- Whether persuasion cues were effective and at what rate
- Discussion section conclusions and author interpretations
- Any ablations or controls for contamination
- Licensing of the AITA dataset
- Train/test/validation splits
- All page-level citations (no PDF extract available)
