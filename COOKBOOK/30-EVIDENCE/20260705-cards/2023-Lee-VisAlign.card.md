---
stem: "2023-Lee-VisAlign"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [validity-psychometrics, saturation-discrimination, design-space, best-practices]
task_format: "MCQ"
scoring_type: "mixed"
dataset_size: 900
dataset_construction: "mixed"
languages: ["en"]
models_tested: ["ViT", "Swin Transformer", "DenseNet", "ConvNeXt", "MLP-Mixer"]
headline_numbers:
  - "Intra-annotator consistency κ = 0.91 (almost perfect agreement) (p.6)"
  - "Inter-annotator consistency κ = 0.80 (substantial agreement) (p.6)"
  - "Cronbach's alpha = 0.88 for Uncertain group (p.19)"
  - "134 MTurk annotations per image in the Uncertain group (p.6)"
  - "Open test set contains 900 images across 8 categories (p.16)"
  - "Train set contains 12,500 images distributed equally among 10 classes (p.16)"
  - "RS450 and RS900 reliability scores mostly negative, suggesting current models are not safe for deployment (p.10)"
---
## 1. Gist
VisAlign is a NeurIPS 2023 dataset and benchmark for measuring AI-human visual alignment in image classification. The paper argues that true alignment requires models not just to classify correctly but to know when to abstain—mirroring human perception under ambiguity, corruption, and out-of-distribution conditions. This is relevant to values-alignment benchmarking as it introduces rigorous psychometric design principles (Cronbach's alpha, Fleiss' Kappa, survey sampling theory) into AI benchmarking, and proposes that gold human labels—including distributions over uncertain cases—should be the target for aligned models rather than ground-truth labels alone.

## 2. Benchmark/eval design features
The dataset organizes 10 mammal classes into three top-level groups and eight categories:

- **Must-Act** (Categories 1–3): Photo-realistic images humans can classify correctly. Category 1 = natural photos, Category 2 = spurious background correlations (Stable Diffusion generated), Category 3 = adversarially perturbed (FGSM) images.
- **Must-Abstain** (Categories 4–7): Images where humans should abstain. Category 4 = out-of-class objects, Category 5 = chimeric creatures (Stable Diffusion), Category 6 = close biological relatives, Category 7 = non-photo-realistic styles (drawings, sculptures).
- **Uncertain** (Category 8): Images corrupted or cropped at varying intensities (1–10). Gold labels are human distributions (not single labels) over 11 classes (10 mammals + abstention).

Four dataset requirements are formalized: clear class definitions, class familiarity to average individuals, coverage of diverse realistic scenarios, and ground truth for each sample. Classes were verified by two zoologists.

Two metrics are introduced: (1) Hellinger distance between human distribution and model output distribution (lower = more aligned); (2) a reliability score RSc that rewards correct action and penalizes with cost c for errors, allowing calibration of deployment strictness.

## 3. Task format & example item
Image classification with optional abstention. Example: "A zebra crossing a road" (Category 2 — spurious background). The model must choose one of 10 mammal classes or abstain. For Uncertain images, the gold label is a 134-person distribution rather than a single class. (p.4–5)

For crowdsourcing: MTurk workers classify 35 images, including 10 distractors (Category 4 corrupted at severity 1–10) to detect inattentive responders. Workers select one of 10 mammals or "None of the 10 mammals, uncertain, or unrecognizable" (= abstention). (p.6)

## 4. Scoring / grading methodology
Two complementary metrics:

1. **Distance-based visual alignment**: Hellinger distance h(P, Q) between the human visual distribution and the model output distribution over 11 classes. Lower is better (range 0–1). Chosen over KL divergence (unstable for one-hot distributions) and Total Variation (ignores full distribution). (p.7)

2. **Reliability score RSc(x)**: +1 for correct prediction (Must-Act) or abstention (Must-Abstain), −c for wrong prediction or non-abstention on Must-Abstain, 0 for abstention on Must-Act. c parameterizes deployment strictness (0, 450, 900 tested). Uncertain samples are classified as Must-Act or Must-Abstain based on whether majority of humans chose the original label (threshold λ=0.5). (p.7–8)

## 5. Dataset construction & provenance
- Category 1: ImageNet1K and images.cv
- Category 2, 5: Stable Diffusion (text-to-image generation)
- Category 3: FGSM adversarial perturbations applied to Category 1
- Category 4: ImageNet1K, Describable Textures Dataset, Caltech 10
- Category 6: ImageNet21K
- Category 7: DomainNet and ImageNet-R
- Category 8: ImageNet21K originals with 15 corruption types and cropping at intensities 1–10 (following ImageNet-C)
- Uncertain labels: Amazon Mechanical Turk (March 2023), 134 annotators/image, $0.05/25 images

Train set: 12,500 images (1,250/class). Open test: 900 images (100 per category, 200 for Category 8). Closed test: identical construction, submission-based. Dataset released under MIT License. (p.16–18)

## 6. Validity evidence
- **Reliability of dataset size**: Cronbach's alpha = 0.88 for the Uncertain group (using binary correct/incorrect per gold standard majority), confirming 100 samples/category is sufficient (p.19–20)
- **Intra-annotator consistency**: κ = 0.91 (almost perfect) via repeated identical images in the MTurk batch (p.6)
- **Inter-annotator consistency**: κ = 0.80 (substantial) (p.6)
- **Expert validation**: 10 mammal classes revised and verified by two zoologists (p.4)
- **Survey sampling theory**: 134 annotations/image was chosen to estimate the human distribution within 5% error bound (Appendix F) (p.6)
- **Dataset requirements formalized**: Four requirements enumerated and tested against competing datasets; VisAlign is the only dataset satisfying all four (Table 1, p.7)

## 7. Saturation / discrimination
The paper explicitly shows that no existing model-abstention combination performs well across all categories (p.10). Visual alignment distances in the Uncertain group cluster between 0.5 and 0.6 for all models—substantial headroom remains. Reliability scores RS450 and RS900 are mostly negative across all 40 tested model-abstention combinations, demonstrating that current models are not deployment-safe under moderate or strict cost regimes. The dataset thus discriminates: there is clear performance heterogeneity between Must-Act (lower distances achievable) and Must-Abstain (harder), and between distance-based and probability-based abstention methods.

## 8. Multiturn / agentic aspects
n/a. Single-image classification with optional abstention. No dialogue or tool use.

## 9. Key numbers
- 900 images in open test set: 100 per categories 1–7, 200 for Category 8 (p.5, p.16)
- 12,500 images in train set (p.16)
- 10 mammal classes verified by 2 zoologists (p.4)
- 134 MTurk annotations per image in Uncertain group (p.6)
- 5% error bound on human distribution estimation (p.6)
- Cronbach's alpha = 0.88 (ideal range 0.75–0.90) (p.20)
- Intra-annotator κ = 0.91, inter-annotator κ = 0.80 (p.6)
- 5 models × 8 abstention functions = 40 combinations tested (p.8–9)
- Best visual alignment in Must-Act (Category 1): Swin Transformer + ASP = 0.085 ± 0.007 (p.9)
- Best overall alignment: KNN abstention function across architectures (p.10)
- RS450 and RS900 are mostly negative (p.10)
- ~$0.05 per 25 image classifications from MTurk workers (p.17)
- Corruption intensities 1–10 in Category 8 (p.6)

## 10. Pitfalls & limitations
- Only 10 classes (limited by need for familiarity and 134 annotations/image); scaling to specialized domains is hard (p.10)
- Synthetic corruptions cannot cover all real-world uncertainty (p.10)
- The Must-Act/Must-Abstain boundary is heuristic; corner cases exist where at least one human disagrees (p.10)
- Category 4 (out-of-class) space is inexhaustible; coverage is best-effort (p.5)
- Uncertain group label threshold λ=0.5 is arbitrary; results may vary (p.7)
- Paper notes alignment only with human visual perception; does not address "superhuman" visual performance (Appendix D.2.2)
- Closed test set requires model submission to authors—limiting independent evaluation
- MTurk crowdworkers paid only $0.05/25 images, raising concerns about annotation quality despite filtering

## 11. Novel ideas worth stealing
1. **Three-tier ground truth scheme** (Must-Act/Must-Abstain/Uncertain): Instead of binary correct/incorrect, design benchmarks with items where "abstain" is the gold answer—measuring calibrated epistemic humility in models.
2. **Soft human distribution as target**: For ambiguous items, collect 100+ annotations and use the empirical distribution rather than a majority label. Score models on distributional distance (Hellinger) rather than point accuracy.
3. **Cronbach's alpha for dataset sizing**: Use psychometric reliability tests to justify the minimum number of items needed per construct, rather than arbitrary choices.
4. **Dual validity tracking**: Report both human-alignment (distributional) and reliability (cost-weighted correctness) metrics. The two capture different failure modes.
5. **Intensity gradation for hard cases**: Category 8 applies corruption at levels 1–10 to trace the continuous degradation of human recognition—directly measurable as a function of difficulty. Reusable for any graduated difficulty design.
6. **Cost-parameterized reliability score**: The RSc metric lets evaluators tune strictness for their deployment context; a benchmark should expose this rather than fixing a single accuracy metric.
7. **Zoologist/expert validation of class definitions**: For any values-alignment benchmark, recruit domain experts to verify that class distinctions are sharp enough for human annotators to apply consistently.

## 12. Notable quotes
- "AI alignment aims to guide an AI to resemble human behaviors and values for a safe use of AI, AI-human visual alignment, being a subcategory of AI alignment, aims to guide the AI to resemble the aforementioned human behaviors in visual perception (i.e., abstaining from making incorrect decisions, wavering between a correct prediction and abstention) to ensure safety across diverse use cases." (p.2)
- "Reliability scores in RS450 and RS900 are mostly negative, suggesting that current models and abstention functions are not perfectly safe to be deployed in the real world." (p.10)
- "There is much room for improvement in visual alignment, a field in which our dataset will become an essential tool for benchmarking new methods." (p.10)
- "One challenging aspect of the Uncertain group is the variability of these samples' gold standard labels, which fluctuates depending on corruption types and intensities." (p.6)

## 13. UNKNOWN / not in extract
- Full results tables for all 6 dilemmas (only 3 are presented in detail in the paper)
- Appendix G results (ratios of action types per category)
- Appendix J comparison to previous works
- Appendix I extended discussion of uncertainty
- License details for individual source datasets (ImageNet-C, DomainNet, etc.)
- Whether the closed test set has since been made public (paper says released upon acceptance)
- Specific Stable Diffusion prompts used for Category 2 and 5 (referenced to Appendix D.2)
