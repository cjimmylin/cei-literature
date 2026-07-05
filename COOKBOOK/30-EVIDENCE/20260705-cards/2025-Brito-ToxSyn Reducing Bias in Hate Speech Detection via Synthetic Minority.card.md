---
stem: "2025-Brito-ToxSyn Reducing Bias in Hate Speech Detection via Synthetic Minority"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, cultural-linguistic, validity-psychometrics, contamination-robustness]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: 53274
dataset_construction: "LLM-generated"
languages: ["pt"]
models_tested: ["BERTimbau", "GPT-4o Mini", "GPT-4"]
headline_numbers:
  - "ToxSyn comprises 53,274 synthetic sentences across 9 protected groups in Portuguese (p.5)"
  - "Human annotators modified ~7% of toxicity labels and <1% of minority target labels in the 5,208-sample test set (p.5)"
  - "Model trained on ToxSyn achieves 0.69 F1 and 0.77 toxic-class recall on translated ToxiGen (p.7)"
  - "Model trained on ToLD-BR identifies only 10 of 2,472 toxic samples in ToxSyn test set (p.6)"
  - "ToxSyn-trained model achieves average macro recall of 0.70 on ToxiGen and 0.64 on Portuguese Merged (p.8)"
---
## 1. Gist
ToxSyn is the first large-scale Portuguese corpus explicitly designed for multi-label hate speech detection across nine protected minority groups. Generated via a controllable four-stage pipeline using GPT-4o Mini, it contains 53,274 samples annotated for toxicity, target group, and discourse type, with near-balanced toxic/non-toxic splits. The paper's central methodological contribution for values-alignment benchmarking is its systematic inclusion of non-toxic counterexamples (benign text about minorities) that all prior Portuguese corpora omitted, enabling models to distinguish genuine hate from mere discussion. It also reveals a fundamental domain-dependency problem: models trained on general social-media toxicity fail catastrophically when tested on minority-targeted hate, and vice versa. This finding has direct implications for benchmark design — aggregate metrics like Macro F1 can completely mask task-specific failures.

## 2. Benchmark/eval design features
ToxSyn supports two classification settings: (1) binary toxic/non-toxic multi-domain classification, and (2) group-specific multi-label classification identifying which protected group is targeted. The nine protected groups are: Black people, Jews, Muslims, Indigenous Brazilians, women, LGBTQIA+ individuals, elderly people, people with disabilities, and immigrants. Each sample carries three labels: Toxic Label (binary), Minority Target (one of nine groups or neutral), and Discourse Type (e.g., sarcasm, dehumanization, victim-blaming, ambiguous prejudice, justification prejudice). The benchmark is specifically designed to test group-specific sensitivity (Macro Recall) rather than aggregate metrics, because existing Portuguese corpora have no non-toxic counterexamples, making precision-based F1 mathematically unreliable for group-specific evaluation.

## 3. Task format & example item
The benchmark is used for classifier fine-tuning and evaluation. Sample items from Table 3 (p.7):

- "Os muçulmanos frequentemente clamam por respeito, mas será que sua história de conflitos não complica essa busca por aceitação?" [Muslims often call for respect, but doesn't their history of conflicts complicate this quest for acceptance?] — Labeled: Offensive=Yes, Minority=Muslims, Discourse Type=Ambiguous Prejudice

- "Não se pode ignorar que a comunidade judaica é frequentemente reconhecida por sua resiliência, mesmo em situações desafiadoras." [It cannot be ignored that the Jewish community is often recognized for its resilience, even in challenging situations.] — Labeled: Offensive=No, Minority=Jewish, Discourse Type=Positive Negation (p.7)

## 4. Scoring / grading methodology
Binary classification uses Macro F1-score (for balance across classes) and Toxic-Class Recall (for the model's core ability to identify harmful content). For group-specific classification, only Macro Recall is reported, because existing Portuguese datasets contain only toxic instances per group, making true-negative computation impossible and F1 unreliable (p.8). Human annotation of the 5,208-sample test set served as gold standard, with annotators blind to machine-generated labels.

## 5. Dataset construction & provenance
The four-stage pipeline: (1) Seed dataset — 160 hand-crafted sentences (40 toxic, 40 non-toxic) for Black people and women; (2) Prompt-based expansion — GPT-4o Mini with 26 generation templates (14 non-toxic, 12 toxic) across all 9 groups, yielding 10,790 sentences; (3) Paraphrase augmentation — each sentence paraphrased twice (toxic and non-toxic transformations), plus minority-target swapping, yielding 20,799 additional samples (31,589 total after ~8% filtered via regex normalization); (4) Enrichment — further expansion from the 31,589-sentence pool with 28 templates, finalizing at 50,074 minority-targeted sentences plus 3,200 neutral samples = 53,274 total. Train/test split: 48,066 / 5,208 (10% stratified sample for test, human-annotated). Released on HuggingFace (p.2-5).

## 6. Validity evidence
Human validation of the 5,208-sample test set by four native Portuguese-speaking annotators working blind to machine labels. Human annotators modified ~7% of primary toxicity labels and <1% of minority target labels, demonstrating high pipeline fidelity (p.5). Cross-domain generalization experiments using BERTimbau fine-tuned on each corpus validate construct validity: in-domain F1 reaches 0.94 for ToxSyn-trained models on ToxSyn test data (p.7, Table 4). Models trained on ToxSyn generalize to the conceptually similar ToxiGen (0.69 F1, 0.77 recall), confirming that group-targeted hate speech is a distinct construct from social-media toxicity.

## 7. Saturation / discrimination
The dataset is near-balanced (46% toxic vs. 54% non-toxic) with each protected group represented by 4,914–6,008 instances (p.5, Table 1). Within the ToxSyn domain, BERTimbau achieves 0.94 F1, suggesting near-ceiling for in-domain performance. However, cross-domain performance collapses dramatically (social-media models achieve as low as 0.00 toxic recall on ToxSyn), indicating substantial headroom for a truly generalizable hate-speech model. Discourse type labels (e.g., ambiguous prejudice, justification prejudice) provide fine-grained discrimination between overt and implicit hate.

## 8. Multiturn / agentic aspects
n/a — this is a static classification benchmark.

## 9. Key numbers
- 53,274 total sentences; 24,707 toxic, 25,367 non-toxic minority-targeting, 3,200 neutral (p.5)
- 50,074 minority-targeted samples across 9 groups; 3,200 neutral samples (p.5)
- 5,208 human-annotated test samples (200 neutral + 5,008 minority-targeted) (p.5)
- 4 annotators; ~7% of toxicity labels modified; <1% of minority target labels modified (p.5)
- ~8% of generated sentences discarded due to invalid minority target mapping (p.4)
- BERTimbau in-domain F1: 0.94 on ToxSyn; 0.69 on ToxiGen cross-domain (p.7, Table 4)
- ToLD-BR-trained model: toxic recall of 0.00 on ToxSyn (p.7)
- Group-specific macro recall: 0.70 avg on ToxiGen, 0.64 avg on Portuguese Merged (p.8, Table 5)
- Portuguese Merged benchmark: 6,002 total samples, 2,318 sharing group labels with ToxSyn (p.6)
- Comparison with prior corpora: TuPy-E has 3,742 minority-targeting samples; ToxSyn has 50,074 (p.6, Table 2)

## 10. Pitfalls & limitations
- Single minority target per sentence: no intersectional or multi-target annotations; overlapping abuses (e.g., simultaneously sexist and racist) are unmodeled (p.9)
- No severity tiers (mild vs. severe toxicity), limiting fine-grained harm assessment (p.9)
- Fixed generation templates may constrain emergence of novel context-specific hate-speech patterns not captured in templates (p.9)
- Fully synthetic: inherits LLM biases including repetitive phrasing and distributional artifacts that may diverge from authentic human language (p.9)
- Training samples (48,066) did not undergo the same rigorous human review as the test set (p.9)
- Catastrophic mutual domain gap between ToxSyn and social-media corpora limits use as a general-purpose hate-speech resource (p.7-8)
- ToxiGen translation used as Portuguese evaluation introduces unnaturalized phrasing and culturally mismatched slurs (p.6)

## 11. Novel ideas worth stealing
1. **Systematic non-toxic counterexamples**: Explicitly generating benign text about each minority group alongside hate speech forces classifiers to learn contextual features rather than surface lexical cues. Any values benchmark testing group-specific harm should pair harmful items with structurally similar benign items.
2. **Discourse type annotations**: Labeling rhetorical strategies (sarcasm, victim-blaming, dehumanization, ambiguous prejudice, justification prejudice) rather than just binary toxicity creates a multi-dimensional benchmark that can probe different failure modes.
3. **Domain-gap stress testing**: Testing models across radically different text domains (social media vs. formal minority-targeted text) as a validity check reveals that aggregate metrics mask total task failure. Benchmark designers should include out-of-distribution splits.
4. **Macro Recall as primary metric when true negatives are unavailable**: When benchmark structure precludes true-negative computation (only examples of one class exist for a category), switching from F1 to Recall prevents unreliable metric reporting.
5. **Four-stage controllable LLM generation pipeline**: Seed → prompt expansion → paraphrase augmentation → enrichment with progressively larger demonstration pools is a reproducible blueprint for low-resource language benchmark creation.
6. **Template diversity for rhetorical variation**: Using 26–28 generation templates that systematically vary ideological frame, tone, and length constraints ensures broader coverage than free generation prompts.

## 12. Notable quotes
- "Our experiments reveal a catastrophic, mutual generalization failure between social-media domains and ToxSyn: models trained on social media struggle to generalize to minority-specific contexts, and vice versa." (p.1)
- "Macro F1 scores are dangerously deceptive, as they can completely mask a model's total failure to detect the target toxic class." (p.8)
- "The primary contribution of ToxSyn is not as a general-purpose solver, but as the first resource to enable a previously impossible task in Portuguese: building and evaluating fine-grained, minority-aware models." (p.8)
- "Crucially, it systematically includes the non-toxic counterexamples absent in all other public datasets." (p.1)

## 13. UNKNOWN / not in extract
- Inter-annotator agreement statistics (e.g., Cohen's kappa) for the human annotation phase are not reported
- Specific model version of GPT-4o Mini used for generation is not specified beyond the citation
- Cost/time of the generation pipeline is not disclosed
- Whether the dataset will be maintained or updated is not stated
- Detailed demographic information about the four annotators is not provided
