---
stem: "2025-Bae-CharMoral"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [normative-ethics, moral-psychology, design-space, llm-judges-scoring]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 103836
dataset_construction: "LLM-generated"
languages: ["en"]
models_tested: ["GPT-3.5", "GPT-4o", "MAD (BERT-large fine-tuned)"]
headline_numbers:
  - "MAD with full context (SICA) achieves 92% agreement with human judgments; action-only baseline: 64% (p.5)"
  - "Fine-tuned BERT-large on CharMoral achieves 94.7% in-domain accuracy (SICA setting) (p.5)"
  - "Cross-domain to Moral Stories: 96.9% accuracy; Social Chemistry: 70.7% (p.6)"
  - "Fleiss' kappa = 0.55 (moderate agreement) among 9 human annotators on 50 sampled items (p.4)"
  - "GPT-4o achieves only 66.7% zero-shot accuracy on CharMoral moral classification (p.6)"
  - "Stories rated 9-10: 57% have dynamically moral main characters; rated 0-4: 0% (p.7)"
---
## 1. Gist
CharMoral is a dataset of 103,836 character-action morality annotations drawn from 1,337 movie synopses (sourced from the IMDB Spoiler Dataset). It is built using a four-stage LLM-assisted pipeline: (1) event-centric story segmentation, (2) GPT-4o-based action extraction, (3) context extraction (situation, intention, consequence), and (4) a fine-tuned BERT-large "Moral Action Detector" (MAD) that classifies each action as moral or immoral based on extracted context. The paper demonstrates that context is critical for accurate moral judgment (from 64% to 92% agreement with humans when context is added) and introduces a "moral dynamic score" to track how character morality evolves across a narrative. The dataset is relevant for values-alignment benchmarking as a source of contextually grounded moral judgments and as a model for how LLMs can be used to scale moral annotation across long-form narratives.

## 2. Benchmark/eval design features
The core evaluation is a binary moral action classification task: given a character action and varying amounts of contextual information (situation, intention, consequence), classify as moral or immoral. Eight input settings are tested (A = action only, SA, IA, CA, SIA, SCA, ICA, SICA = all four). The moral dynamic score extends this to longitudinal character tracking: it measures how often a character's MAD prediction crosses the 0.5 midpoint across narrative segments, normalized by number of segments. Characters with score ≥ 0.5 are classified as "morally dynamic."

The dataset was validated against human judgment (9 graduate annotators, 50 sampled items, majority voting, Fleiss' kappa = 0.55 for inter-annotator agreement).

## 3. Task format & example item
Binary classification item (from Figure 1, p.1):

> **Character**: Harry Potter
> **Situation**: After burying Dobby at the garden of the Shell cottage, [mask] Potter convinces Griphook to help them get to Lestrange's vault in Gringotts.
> **Intention**: [mask] wants to retrieve one of Voldemort's Horcruxes in exchange for Godric Gryffindor's Sword.
> **Consequence**: not exist
> **Label**: moral

Note: character name is masked with "[mask]" in context to reduce name-based bias. Input format: `<CLS>context<SEP>action<SEP>`.

## 4. Scoring / grading methodology
The Moral Action Detector (MAD) is a BERT-large model fine-tuned on the Moral Stories dataset, then used to annotate CharMoral. It outputs a softmax logit score (0–1), with 0.5 as the decision boundary. For evaluation against humans: accuracy = proportion matching majority-vote human labels. For the moral dynamic score: the number of times MAD predictions cross 0.5 across segments is counted (#passc), divided by (total segments − 1), yielding a rate. Characters with rate ≥ 0.5 are dynamic. Stories are rated on IMDB scale (0–10) to correlate morally dynamic characters with audience engagement.

## 5. Dataset construction & provenance
Base data: IMDB Spoiler Dataset (1,572 synopses), filtered to 1,337 narratives with ≥ 10 words. Each synopsis is segmented into event-centric segments (3-sentence basic units, merged by character co-occurrence). Action extraction: GPT-4o prompted to extract character-specific actions from each segment. Context extraction: same LLM extracts situation, intention, consequence for each action. Moral annotation: MAD (BERT-large fine-tuned on Moral Stories) classifies each action-context tuple. Result: 103,836 annotated entries (50,717 moral, 53,119 immoral), ~9,389 unique characters. Dataset and code publicly available at GitHub.

## 6. Validity evidence
- Human evaluation: 9 graduate annotators rated 50 randomly sampled items; Fleiss' kappa = 0.55 (moderate agreement).
- MAD with full context (SICA) achieves 92% agreement with human majority votes vs. 64% for action-only — strong evidence for context-dependence of moral judgment.
- Cross-domain validation: model trained on CharMoral achieves 96.9% on Moral Stories (high positive transfer) and 70.7% on Social Chemistry (moderate — different distribution).
- GPT-3.5 zero-shot: 61.7% accuracy; GPT-4o zero-shot: 66.7% — both substantially below fine-tuned MAD at 94.7%, justifying the fine-tuning approach.

## 7. Saturation / discrimination
The fine-tuned model achieves 94.7% accuracy (SICA), suggesting potential ceiling. However, key findings reveal context-dependence as a discrimination axis: action-only performance is 64% (human agreement) / 69.2% (in-domain test), while full-context is 92%/94.7% — a 25–30 pp gap. LLMs tested (GPT-4o) at 66.7% zero-shot are well below ceiling, leaving substantial headroom. Cross-domain to Social Chemistry drops to 70.7%, indicating the task is not saturated across domains.

## 8. Multiturn / agentic aspects
Not a multiturn interaction benchmark. However, the dataset captures moral dynamics across narrative segments, which provides a longitudinal sequence of moral actions per character — closer to an episode-level analysis than a single-turn evaluation. The moral dynamic score tracks changes across a character's appearances in multiple segments (not across conversation turns). n/a for agentic interaction.

## 9. Key numbers
- 1,337 movie synopses; 30,616 segments; 9,389 characters; 103,836 annotations (p.4, Table 2)
- Label distribution: 50,717 moral, 53,119 immoral (near-balanced) (p.4)
- Context completeness: 100% action, 99.98% situation, 89.2% intention, 79.04% consequence (p.4)
- Fleiss' kappa = 0.55 (moderate) among 9 annotators (p.4)
- MAD agreement with humans: 64% (action-only A) → 92% (full context SICA) (p.5, Table 3)
- GPT-3.5: 78% human agreement; GPT-4: 86% (p.5)
- In-domain BERT-large fine-tuned: 94.7% accuracy, 94.7% F1 (SICA) (p.5-6, Table 5)
- Cross-domain to Moral Stories: 96.9%; Social Chemistry: 70.7% (p.6)
- Stories rated 9–10: average 3.57 dynamically moral characters; rated 0–4: average 1.25 (p.7)
- Main character morality dynamics: 57% dynamic in 9–10 rated stories; 0% in 0–4 rated stories (p.7)

## 10. Pitfalls & limitations
- MAD was fine-tuned on Moral Stories to generate CharMoral labels — circular dependency: quality of annotations depends on the training data quality of the upstream dataset.
- Moral framework is implicit and Western-centric; no explicit theory (deontological, consequentialist, etc.) is specified for labeling.
- Movie synopses describe narrative morality, not necessarily reflective of real-world moral norms — fictional morality may diverge significantly.
- Only binary moral/immoral labels — no nuance for moral ambiguity or degrees of morality.
- Moderate inter-annotator agreement (kappa = 0.55) suggests genuine human disagreement on moral judgment, which the dataset resolves by majority voting, potentially discarding valid minority viewpoints.
- Cultural biases inherent in LLMs (GPT-4o) used for action and context extraction may propagate into the dataset.
- Authors acknowledge this limitation and call for future work accounting for cultural differences.

## 11. Novel ideas worth stealing
- **Context ablation design**: systematically testing eight input settings (A, SA, IA, CA, SIA, SCA, ICA, SICA) quantifies the marginal contribution of each context element to moral judgment accuracy — a reusable design pattern for any context-dependent moral benchmark.
- **Moral dynamic score**: a continuous measure of how frequently a character's moral valence switches across narrative segments, normalized by appearances. Can be adapted to measure consistency of LLM moral responses across a series of related prompts.
- **Character name masking**: replacing character names with "[mask]" in context inputs prevents name-based shortcuts in moral classification — a decontamination technique applicable to other narrative-based benchmarks.
- **Correlation with audience engagement**: linking morally dynamic characters to IMDB ratings reveals that moral complexity is valued by human audiences — a potential validity signal for narrative-based moral benchmarks.
- **Four-stage LLM pipeline for large-scale moral annotation**: segmentation → action extraction → context extraction → classification enables scaling moral annotation to thousands of narratives without direct human annotation of each item.

## 12. Notable quotes
- "the action of 'throwing a bomb at the door' might generally be considered unethical, but in the context of rescuing trapped individuals from aliens, it could be perceived as morally justified." (p.2)
- "MAD significantly improves moral action predictions, outperforming GPT-3.5 and GPT-4, which achieve 78% and 86% agreement, respectively. This highlights the superior performance of our model in making the predictions more closely aligned with human judgment." (p.5)
- "Stories with higher ratings tend to have morally dynamic main characters, highlighting the importance of the main character's moral evolution in making a story more engaging." (p.8)
- "Although our ultimate goal is to develop a method that objectively assesses the morality of character actions based on story context, moral concepts are often shaped by cultural, social, and personal beliefs." (p.9)

## 13. UNKNOWN / not in extract
- Full prompt templates for action extraction and context extraction are referenced (Tables 19, 20) but not in the extract.
- Details of the Moral Stories fine-tuning procedure for MAD beyond reference to Emelin et al. (2021) settings.
- Model card or licensing for the CharMoral dataset.
- Whether the MAD model weights are publicly released alongside the dataset.
- Genre breakdown of the 1,337 narratives beyond what appears in Table 7.
- Computational cost or runtime of the four-stage pipeline.
