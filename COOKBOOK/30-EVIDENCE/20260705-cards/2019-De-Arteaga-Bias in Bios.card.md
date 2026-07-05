---
stem: "2019-De-Arteaga-Bias in Bios"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [validity-psychometrics, design-space, normative-ethics, cultural-linguistic]
task_format: "n/a"
scoring_type: "classifier"
dataset_size: 397340
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["BOW logistic regression", "word embeddings + logistic regression", "DNN with GRU + attention"]
headline_numbers:
  - "397,340 biographies spanning 28 occupations scraped from Common Crawl (p.2)"
  - "DNN gender classifier accuracy on scrubbed biographies: 68.2% (vs. 50% chance) (p.6)"
  - "BOW TPR gender gap correlation with occupational gender imbalance: r=0.85 (with indicators), r=0.74 (without) (p.5)"
  - "14.7% of female rappers correctly predicted only when gender indicators swapped were previously misclassified as models (p.5)"
  - "Female surgeons: only 11.6% of true positives are women, vs. 14.6% in the population (p.4)"
---
## 1. Gist
De-Arteaga et al. (2019, CMU/Microsoft Research/LinkedIn) present a large-scale study of gender bias in occupation classification using 397,340 online biographies. The paper demonstrates that (a) TPR gender gaps are strongly correlated with existing occupational gender imbalances across BOW, word-embedding, and DNN representations; (b) "scrubbing" explicit gender indicators reduces but does not eliminate these gaps; and (c) models learn proxy features for gender even without explicit indicators, amplifying societal injustice through a feedback loop. The work matters for values-alignment benchmarking as a canonical case study in how seemingly neutral classifiers systematically disadvantage underrepresented groups, and it formalizes the concept of "compounding injustice" with a formal proof and simulation.

## 2. Benchmark/eval design features
The paper introduces the **BiasBios dataset** and methodology:
- **Dataset**: 397,340 English-language online biographies from Common Crawl, spanning 28 occupations, with binary gender inferred from pronouns. Train/val/test split: 65%/10%/25%, stratified by occupation.
- **Task**: Multi-class occupation prediction from biography text (28 classes); gender is a protected attribute, not the target.
- **Bias metric**: TPR gender gap per occupation — Gapд,y = TPRд,y − TPR∼д,y — and its correlation with πд,y (fraction of occupation y that is gender д).
- **Counterfactual analysis**: For each biography, swap explicit gender indicators (name + pronouns) and measure how many predictions change.
- **Proxy analysis**: DNN attention weights over vocabulary to identify words used as gender proxies when explicit indicators are removed.
- **Simulation**: Forward-propagate classifier predictions across 10 time steps to model compounding imbalance.

## 3. Task format & example item
The paper describes prediction from text, with the following illustrative example (p.3):
> Input text: "She graduated from Lehigh University, with honours in 1998. Nancy has years of experience in weight loss surgery, patient support, education, and diabetes."
> Target label: nurse
> (The occupation label "nurse" is extracted from the first sentence "Nancy Lee is a registered nurse" and withheld; the classifier must predict the occupation from the rest of the biography.)

The counterfactual version would swap "She" → "He" and "Nancy" → a male name, keeping everything else fixed.

## 4. Scoring / grading methodology
- Overall accuracy on 28-class occupation prediction (reported per representation and scrubbing condition).
- TPR gender gap (Gapд,y) per occupation, computed on the test split.
- Pearson correlation between Gapfemale,y and πfemale,y across 28 occupations as the primary bias metric.
- Counterfactual change rate: percentage of biographies whose predicted label changes when gender indicators are swapped.
- Gender prediction accuracy on scrubbed text as evidence that gender information remains after scrubbing.

## 5. Dataset construction & provenance
- Sourced from Common Crawl WET files from 16 crawls (2014–2018). (p.2)
- Filtered for pattern "[Name] is a(n) [occupation]" using BLS Standard Occupation Classification.
- 28 most frequent occupations selected; some merged (e.g., "economics professor" → professor).
- Deduplication by name + occupation combination.
- 397,340 biographies; professor most frequent (118,400), rapper least (1,406). (p.2)
- Source code and dataset available at http://aka.ms/biasbios. (p.3)
- Binary gender label extracted from pronouns (acknowledged as simplification). (p.1)
- fastText embeddings trained on Common Crawl (overlapping source, noted as caveat). (p.3)

## 6. Validity evidence
- Three semantic representations (BOW, WE, DNN) all show consistent positive correlation between TPR gender gap and occupational gender imbalance, with correlations ranging r = 0.71–0.86. (p.5)
- Formal theorem proves that if πд,y < 0.5 and Gapд,y < 0, then the classifier compounds the gender imbalance (p.4).
- DNN gender classifier achieves 68.2% accuracy on scrubbed biographies (BOW: 65.5%), confirming residual gender information after scrubbing. (p.6)
- Proxy words identified consistently across multiple runs: women, husband, mother, woman, female as top attention targets. (p.7)
- Simulation across 10 time steps confirms monotonic compounding of gender imbalance. (p.7)

## 7. Saturation / discrimination
- Female surgeons: 14.6% of dataset, but only 11.6% of true positives after classification — imbalance amplified. (p.4)
- Scrubbing reduces TPR gaps (Figure 4) but positive correlation with occupational imbalance persists across all representations. (p.7)
- Model predictions change for 4.6–12.2% of biographies when gender indicators are swapped, depending on representation. (p.5)
- Attention to proxy words (e.g., "women") increases for all occupations after scrubbing — model compensates by leaning harder on proxies. (p.7)

## 8. Multiturn / agentic aspects
n/a — single-pass text classification.

## 9. Key numbers
- 397,340 total biographies; 28 occupations (p.2)
- Train/val/test: 65% / 10% / 25% (p.3)
- BOW correlation (with indicators): r = 0.85; DNN (without): r = 0.74 (p.5)
- DNN gender prediction accuracy (scrubbed): 68.2%; BOW: 65.5% (p.6)
- 14.7% of female rappers only correctly predicted when gender indicators swapped → previously mislabeled as models (p.5)
- Female surgeon true positive share: 11.6% vs. 14.6% base rate (p.4)
- Predictions change on swapping gender indicators: 5.5% (BOW), 12.2% (WE), 4.6% (DNN) (p.5)

## 10. Pitfalls & limitations
- Binary gender model is explicitly acknowledged as a "simplification that fails to capture important aspects of gender and erases people who do not fit within its assumptions." (p.1)
- Biographies may not have been written by their subjects; representation by others could differ from self-representation. (p.2)
- Dataset demographics of Common Crawl biographies differ from the overall workforce. (p.2)
- Focus on gender bias only; racial and socioeconomic biases likely present but not studied. (p.8)
- fastText embeddings trained on partially overlapping Common Crawl data — potential contamination. (p.3)
- Proxy behavior analysis relies on DNN attention weights, which are imperfect proxies for causal influence.
- The simulation assumes the TPR–imbalance relationship remains stable over time, which may not hold.

## 11. Novel ideas worth stealing
1. **TPR gap × base rate correlation as aggregate bias score**: Rather than reporting per-occupation gaps, a single Pearson r between TPR gender gap and occupational representation is a compact summary of whether the classifier systematically disadvantages underrepresented groups. Directly transferable to any multi-class values-alignment benchmark with demographic subgroups.
2. **Counterfactual label-flip rate**: Swap a single protected attribute (name, pronoun) and measure how often the model prediction changes. This is a minimal-pair, minimal-perturbation test that can be operationalized for any text classifier without additional annotation.
3. **Attention weight proxy analysis**: Use attention/saliency to identify which words a scrubbed model is using as proxies for the removed attribute. Useful for auditing whether a debiased benchmark inadvertently contains proxy signals.
4. **Compounding injustice simulation**: Model how classifier outputs feed back into future training data distributions; show that even small TPR gaps compound over time. A design argument for measuring disparity on the tail, not just the mean.
5. **Stratified splits by subgroup**: When any subgroup is small, stratify train/val/test splits to ensure each subgroup appears in testing with enough examples for reliable TPR estimation. Essential for any benchmark touching demographic minority groups.

## 12. Notable quotes
- "Scrubbing explicit gender indicators is like introducing a curtain—the sounds made by the candidates' shoes remain." (p.1)
- "Compounding imbalances are especially problematic if people repeatedly encounter such classifiers... the underrepresented gender will, over time, become even further underrepresented—a phenomenon sometimes referred to as the 'leaky pipeline.'" (p.7)
- "In the absence of explicit gender indicators, we did find that (1) we were able to predict the gender of a biography's subject better than random, even when controlling for occupation; (2) significant TPR gender gaps remain for some occupations; (3) there is still a positive correlation between the TPR gender gap for an occupation and the gender imbalance in that occupation, so existing gender imbalances may be compounded." (p.8)
- "Our findings highlight both the risks of using machine learning in a high-stakes setting and the difficulty of trying to promote fairness by 'scrubbing' sensitive attributes." (p.8)

## 13. UNKNOWN / not in extract
- Inter-rater reliability statistics for the gender label (inferred from pronouns, not separately annotated).
- Licensing of the BiasBios dataset.
- Whether the Common Crawl data is publicly accessible via the linked repository.
- Full numerical values in Figures 3–13 (scatter plots described but numbers not directly extractable from OCR).
- Whether any analysis was conducted for occupations with non-binary gender representation.
