---
stem: "2024-Aupi-WoNBias A Complete Bengali Gender Bias Dataset"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, normative-ethics]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 31484
dataset_construction: "mixed"
languages: ["bn"]
models_tested: ["BanglaBERT"]
headline_numbers:
  - "31,484 annotated Bengali text entries across three classes: Negative (10,656), Positive (10,170), Neutral (10,658) (p.107)"
  - "Inter-annotator agreement: Cohen's Kappa κ=0.74 (95% CI [0.71, 0.77]) (p.108)"
  - "BanglaBERT recall: Neutral 0.962, Positive 0.881, Negative 0.824 (p.109)"
  - "52,671 unique tokens in corpus; 61.60% hapax legomena (p.108)"
  - "Negative class: 89.2% pairwise agreement; 16.4% confusion between Positive and Neutral (p.108)"
---

## 1. Gist
WoNBias is a 31,484-entry Bengali dataset for detecting gender-based bias against women, compiled from social media (Facebook), news platforms, blogs, and offline surveys/focus groups. It uses a three-class scheme: Negative (explicit bias/prejudice), Positive (advocacy for women), and Neutral (no gender bias). The dataset is unusually well-balanced (~33% per class), covers 52,671 unique tokens with 60+ Bengali feminine terms including derogatory variants, and achieves Cohen's Kappa of 0.74 through a structured seven-annotator process with regional diversity across Bangladesh's seven administrative divisions. The paper fills a critical gap: Bengali is spoken by over 230 million people but remains severely under-resourced in gender bias NLP, meaning automated content moderation cannot currently detect discrimination against women in Bengali digital discourse. For values-alignment benchmarking, WoNBias demonstrates how to build a culturally grounded, low-resource-language bias dataset that captures the specific sociolinguistic patterns of a non-Western community.

## 2. Benchmark/eval design features
**Constructs measured**: Gender bias against women in Bengali text — categorized as Negative (derogatory, stereotyping, dehumanizing), Positive (advocacy, affirmation), or Neutral (no gender dimension).

**Item structure**: Single Bengali text item (sentence or short passage, avg ~11.5–12.3 words) labeled with one of three classes.

**Inclusion rules**: (1) Self-contained context — bias must be unambiguous without external context; (2) Derogatory language detection — covers direct slurs, gendered stereotypes, dehumanizing comparisons; (3) Lexical diversity — 60+ Bengali feminine terms (e.g., মেয়ে, নারী, স্ত্রী, বউ) including derogatory variants.

**Data sources**: Facebook posts and comments (~600,000 entries before filtering), regional newspapers (Prothom Alo, BD News 24, Ittefaq), government policy texts on gender issues, questionnaire/survey responses from female university students and working professionals, and focus groups across Bangladesh.

**BanglaBERT baseline**: Fine-tuned for three-class classification; results reported as per-class recall.

## 3. Task format & example item
Three-class forced-choice (Negative / Positive / Neutral). Examples:

- Negative: "েমেয়জাতটাই খারাপ" [women are the worst as a group] — explicit slur; Label: Negative
- Negative: "স্তৰ্ীজাত গাধার সমান" [wives are like donkeys] — dehumanizing comparison; Label: Negative
- Negative: "েমেয়েদর সায়েন্স পড়ার দরকার নাই" [women shouldn't study science] — gendered stereotype; Label: Negative
- Positive: "নারীরা সকল েপশায় সমথর্" [women excel in all professions] — explicit advocacy; Label: Positive
- Neutral: "বাংলাদেশে িশক্ষার হার বাড়েছ" [literacy rates are rising in Bangladesh] — no gender dimension; Label: Neutral
- Edge case excluded: "েমেয়টার পিরণিত িঠক-ই হেয়েছ" [She got what she deserved] — ambiguous without context; Discarded

## 4. Scoring / grading methodology
Human annotation by seven university students (4 male, 3 female) representing all seven administrative divisions of Bangladesh. Quality control: 1,500-entry balanced subset (500 per class) labeled by two independent annotators; disagreements resolved by a third senior annotator as arbitrator. Cohen's Kappa κ=0.74 (substantial agreement). BanglaBERT fine-tuned for three-class classification; evaluated on per-class recall. No precision/F1 breakdown reported for BanglaBERT; only recall (Neutral: 0.962, Positive: 0.881, Negative: 0.824). Deduplication: removed identical and near-identical sentences (75% match threshold) while retaining paraphrases.

## 5. Dataset construction & provenance
- **Web sources**: Facebook posts/comments (~600,000 pre-filter), regional newspapers, blogs
- **Offline sources**: Questionnaires distributed to female students and professionals; focus groups with women from diverse backgrounds (students, homemakers, working professionals)
- **Existing corpora**: Incorporated some pre-existing datasets for vocabulary expansion (e.g., BanglaParaphrase)
- **Scale**: 31,484 final entries after deduplication and filtering
- **Class balance**: Negative 10,656 (33.84%), Positive 10,170 (32.32%), Neutral 10,658 (33.84%)
- **Publicly available**: gender-bias-bengali/wonbias-complete-dataset on Hugging Face (released 2025, superseding partial prior release)
- **Coverage**: 52,671 unique tokens, 371,781 total words, avg 11.80 words/text

## 6. Validity evidence
- **Inter-annotator agreement**: Cohen's Kappa κ=0.74 (95% CI [0.71, 0.77]), meeting Landis & Koch "substantial" threshold (κ > 0.61).
- **Disaggregated reliability**: Negative class has highest agreement (89.2% pairwise precision) due to clear lexical markers; Positive/Neutral confusion at 16.4% reflects genuine semantic ambiguity in implicit praise vs. neutral statements.
- **Error analysis**: Documented error taxonomy including false neutrals (sarcasm), false positives (neutral praise), and edge cases (code-mixed insults, e.g., "মাইয়া পুরাই আন্টি আন্টি লাগে").
- **Contingency matrix**: Full 3×3 matrix reported (Table 4): Negative 446/500 agreement; Neutral 398/500; Positive 399/500.
- **Annotator diversity**: Seven annotators from all seven Bangladesh divisions with diverse academic backgrounds (agriculture, economics, political science, software engineering), ages 20–26 — explicit effort to capture regional dialectal variation.

## 7. Saturation / discrimination
BanglaBERT achieves 0.962 Neutral recall but only 0.824 Negative recall, indicating the benchmark is still appropriately challenging for the important class (explicit bias detection). The normalized confusion matrix shows that Negative is most confused with Neutral (10.65% misclassification rate), reflecting that subtle bias (sarcasm, implication) remains hard for the model. Lexical diversity metrics (61.60% hapax legomena) indicate vocabulary breadth sufficient to challenge models on unseen expressions of bias.

## 8. Multiturn / agentic aspects
n/a — single-text classification dataset; no dialogue or agentic framing.

## 9. Key numbers
- Total dataset: 31,484 entries (p.107)
- Class distribution: Negative 10,656 (33.84%), Positive 10,170 (32.32%), Neutral 10,658 (33.84%) (p.107)
- Unique tokens: 52,671; total words: 371,781 (p.108)
- Avg words/text: 11.80 overall; 12.31 Negative, 11.57 Positive, 11.52 Neutral (p.108)
- Hapax legomena: 32,447 (61.60%) (p.108)
- Cohen's Kappa κ=0.74 (95% CI [0.71, 0.77]) (p.108)
- Negative class pairwise precision: 89.2% (p.108)
- Positive/Neutral confusion: 16.4% of cases contested (p.108)
- BanglaBERT recall: Neutral 0.962, Positive 0.881, Negative 0.824 (p.109)
- 60+ Bengali feminine terms covered in lexical analysis (p.109)
- Annotators: 7 (4 male, 3 female), 1 from each Bangladesh division (p.107)

## 10. Pitfalls & limitations
- Focuses exclusively on binary gender (women vs. not-women); non-binary and LGBTQ+ identities are absent.
- No intersectional annotation — race, religion, class, and caste dimensions of discrimination against Bengali women are not captured.
- Keyword-based deduplication and filtering may still leave near-duplicate entries that inflate apparent dataset size.
- Annotator pool is entirely university students aged 20–26, introducing generational and education-level bias; older women, rural women, and women with lower education are underrepresented as annotators.
- Facebook scraping is limited to publicly accessible content; private groups (where more extreme bias may circulate) are excluded.
- No assessment of temporal bias — the dataset represents a single collection period; language of discrimination evolves.
- BanglaBERT results are reported only as recall, not as precision or F1, making it hard to assess the classifier's usefulness for practical deployment.
- Dialectal variations (Sylheti, Chittagonian, etc.) are not explicitly annotated, though annotators representing those divisions were included.
- No comparison to a human-level performance upper bound.

## 11. Novel ideas worth stealing
1. **Regional annotator stratification**: Deliberately recruiting annotators from each major administrative division to capture dialectal and cultural variation in bias expression is a replicable strategy for any language with significant regional diversity.
2. **Three-class scheme with positive advocacy class**: Including a Positive class (content that affirms women's equality) alongside Negative and Neutral enables training models that can distinguish pro-gender-equality content from neutral content — a more nuanced benchmark than binary hate/not-hate.
3. **Offline + online data fusion**: Combining social media scraping with offline surveys and focus groups (asking women about their own experiences of discriminatory language) captures both naturally occurring and participant-elicited instances of bias — more ecologically valid than scraping alone.
4. **Lexical diversity metrics as dataset quality indicators**: Reporting unique tokens, hapax legomena percentage, and per-class vocabulary size is an underused practice that assesses how much novel text the benchmark can present to models.
5. **Bias severity scale proposal**: The paper explicitly calls for a future bias severity scale (from mild stereotypes to hate speech) as a limitation. This is directly actionable: a Likert-scale severity annotation on top of the three-class scheme would enable fine-grained evaluation.
6. **Self-contained context inclusion rule**: Requiring that bias be interpretable without external context (discarding ambiguous sentences like "she got what she deserved") is a principled way to ensure that automated classifiers can be evaluated fairly.

## 12. Notable quotes
- "Gender bias and negative gender discourse against women on digital platforms in Bengali often escape detection because of the linguistic inability of universal tools and fragmented moderation infrastructure." (p.105)
- "Such representational harms are damaging because they reinforce restrictive and inappropriate stereotypes about the roles women are expected to perform, such as the notion that (women shouldn't study science) 'েমেয়েদর সায়েন্স পড়ার দরকার নাই'." (p.105)
- "The inter-annotator agreement yields κ=0.74 (95% CI [0.71, 0.77]), indicating substantial agreement according to Landis & Koch's benchmark." (p.108)
- "The negative class showed the strongest agreement, with 89.2% pairwise precision. This was due to the presence of clear lexical markers of bias, such as slurs and explicit comparisons." (p.108)

## 13. UNKNOWN / not in extract
- The full dataset statistics for each source (Facebook vs. newspapers vs. surveys) breakdown is not provided.
- No information about licensing terms for the released dataset.
- The total number of Facebook posts/comments before filtering is stated as "approximately 6,00,000" (Indian number format = 600,000) — exact post-filter count per source is not given.
- The updated questionnaire referenced in footnote 2 is not reproduced.
- No F1-score or precision reported for BanglaBERT — only per-class recall.
- No comparison to existing Bengali NLP models other than BanglaBERT.
- Cross-validation setup details (e.g., number of folds, test set size) for BanglaBERT fine-tuning are not provided.
