---
stem: "2024-Lin-AI-Face"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, validity-psychometrics, saturation-discrimination]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 1646545
dataset_construction: "mixed"
languages: [n/a]
models_tested: ["Xception", "EfficientB4", "ViT-B/16", "F3Net", "SPSL", "SRM", "UCF", "UnivFD", "CORE", "DAW-FDD", "DAG-FDD", "PG-FDD"]
headline_numbers: ["1,245,660 fake + 400,885 real face images, ~1.65M total across 37 generation methods (p.3)", "10 of 12 detectors achieve AUC > 98% on the test set (p.6)", "AI-Face annotation ACC surpasses A-FF++ by 78.714% on gender and 48.000% on age (p.5)", "PG-FDD best combined fairness+utility: AUC 99.172%, ACC 96.174% (p.6)", "Intersectional FEO up to 67.545% (UCF) on the age attribute (p.6)"]
---
## 1. Gist
AI-Face is a million-scale, demographically annotated dataset of AI-generated and real face images, paired with the first comprehensive *fairness* benchmark for AI-generated-face detectors. It is a computer-vision fairness benchmark, NOT an LLM values-alignment benchmark, but it is highly relevant to the CEI cookbook as an exemplar of how to operationalize and measure *fairness/bias as a first-class evaluated construct*: it annotates every item with protected attributes (skin tone, gender, age), defines a battery of group, intersectional, and individual fairness metrics, and stress-tests fairness under distribution shift and post-processing perturbations. Its methodological moves — demographic annotation pipelines, intersectional subgroup slicing, fairness-vs-utility joint reporting, and "fairness reliability" (robustness + generalization) evaluation — transfer directly to designing values/pluralism benchmarks where subgroup equity matters.

## 2. Benchmark/eval design features
Constructs measured: (a) *utility* of AI-face detectors (real vs. fake binary classification) via AUC, ACC, AP, EER, FPR; (b) *fairness* along skin tone (Monk Skin Tone 10-shade), binary gender, and 5 age groups, using Demographic Parity (FDP), Max Equalized Odds (FMEO), Equal Odds (FEO), Overall Accuracy Equality (FOAE), and Individual fairness (FIND) (p.5). Fairness is evaluated at group, intersectional (gender × skin-tone → F-L, F-M, F-D, M-L, M-M, M-D), and individual levels. A distinctive "fairness reliability" axis adds *robustness* (6 image post-processings: crop, rotation, brightness/contrast, HSV, Gaussian blur, JPEG compression) and *generalization* (cross-dataset transfer to CCv2, DF-Platter, GenData) (p.6-7). Item structure: images labeled with source subset, generation method, and three demographic attributes; answer space is binary real/fake.

## 3. Task format & example item
n/a (image classification dataset — no textual items). Each "item" is a cropped face image (RetinaFace-cropped) tagged with skin tone (Tone 1-10), gender (Male/Female), age (Child/Youth/Adult/Middle-age/Senior), subset, and real/fake label (p.3).

## 4. Scoring / grading methodology
Detectors output a real/fake score; utility scored by AUC, ACC, AP, EER, FPR (higher AUC/ACC/AP better; lower EER/FPR better). Fairness scored by five metrics (FDP, FMEO, FEO, FOAE, FIND), all "lower is better" (%), computed at group, intersectional, and individual levels (p.5-6). Reliability scored as performance *ratios/deltas* before vs. after post-processing (points near 1.0 = robust) and as absolute changes under cross-dataset transfer (p.6-7). 80%/20% train/test split (p.5).

## 5. Dataset construction & provenance
Mixed provenance: images collected/integrated from public academic datasets, GitHub repos, and commercial tools under their licenses. Fake set = 1,245,660 images from 4 deepfake-video datasets (FF++, DFDC, DFD, Celeb-DF-v2), 10 GANs, and 8 diffusion models; real set = 400,885 from FFHQ, IMDB-WIKI, and real portions of FF++/DFDC/DFD/Celeb-DF-v2; 28 subsets, 37 generation methods total (p.3). Demographic labels are *algorithmically generated*: skin tone by facial-landmark masking + K-means color clustering → nearest Monk tone; gender/age by a CLIP ViT-L/14-based lightweight annotator trained on IMDB-WIKI with an imbalance loss (Vector Scaling) + fairness loss (Sinkhorn distance) and Sharpness-Aware Minimization (p.3-4). Access gated by signed EULA; IRB-approved (p.8).

## 6. Validity evidence
Annotation-quality user study: 3 human labelers, majority-vote ground truth, on 1,000 "strategic" (disagreement) images from A-FF++/A-DFDC and 1,000 random from A-Celeb-DF-v2/A-DFD. AI-Face annotation accuracy far exceeds prior datasets — e.g., gender ACC 86.857% vs A-FF++ 8.143%; age ACC 85.700% vs 37.700% (p.5, Table 3). This is a criterion-validity check of the labels (the benchmark's measurement substrate). No factor analysis (not applicable to image labels). Human baselines exist only for annotation quality, not detector performance.

## 7. Saturation / discrimination
Utility is near-ceiling: 10 of 12 detectors exceed AUC 98% on the in-domain test set (p.6), indicating the *utility* axis is largely saturated. Discrimination lives in the *fairness* and *reliability* axes, which show large spreads: intersectional FEO ranges from ~18% (PG-FDD) to 67.5% (UCF) on age (p.6), and cross-domain transfer collapses utility (e.g., Xception ACC drops 17.3 points on DF-Platter; EfficientB4 AUC drops 30.9 points, p.7). Post-processing induces "evident performance degradation" (p.6). So headroom is essentially all in fairness robustness/generalization, not raw detection accuracy.

## 8. Multiturn / agentic aspects
n/a — static single-image classification benchmark; no interaction, tools, or environment.

## 9. Key numbers
- Total ~1,646,545 images: 1,245,660 fake + 400,885 real, 28 subsets, 37 generation methods (p.3).
- Skin tone distribution: Tone 5 = 31.14%, Tone 6 = 35.16%; Tones 1-3 = only 0.97% (underrepresented) (p.5).
- Age: Adult (25-44) = 49.67% dominant (p.5).
- Annotation ACC gains vs A-FF++: +78.714% gender, +48.000% age (p.5).
- 10/12 detectors AUC > 98% in-domain (p.6).
- Best model PG-FDD: AUC 99.172%, ACC 96.174%, but longest training (7h20min/epoch) (p.6).
- Max intersectional FEO: 67.545% (UCF, age) (p.6).
- Cross-domain drop example: EfficientB4 AUC −30.917 on DF-Platter (p.7).

## 10. Pitfalls & limitations
Author-admitted: demographic annotations are algorithmically generated and "may lack 100% accuracy," since attributes for synthetic faces are often ambiguous and don't map to real individuals (p.8). Self-evident: (a) binary-only gender and a fixed 5-bin age scheme bake in contested demographic ontologies; (b) skin-tone labels rest on K-means color clustering, sensitive to lighting/rendering; (c) severe skin-tone imbalance (Tones 1-3 = 0.97%) confounds fairness measurement for the smallest groups — lighter faces are more often misclassified as fake precisely because they are rare (p.6); (d) near-ceiling in-domain utility limits the dataset's power to discriminate detectors on the utility axis; (e) label quality validated only against other (weak) datasets, not an independent gold standard.

## 11. Novel ideas worth stealing
- **Fairness as a first-class, multi-level evaluated construct**: report group, *intersectional*, and *individual* fairness simultaneously, not a single aggregate — directly portable to pluralism/values benchmarks where subgroup equity across cultures/religions is the point.
- **"Fairness reliability" axis**: separate *robustness* (performance under input perturbations) from *generalization* (cross-domain transfer), and report both as deltas/ratios vs. a clean baseline. A values benchmark could analogously test whether alignment holds under paraphrase/perturbation and out-of-distribution prompts.
- **Joint fairness-vs-utility reporting** (never one without the other) to expose models that buy fairness by sacrificing capability — mirrors the alignment-tax framing.
- **Annotation-quality user study on adversarially-selected disagreement cases** ("strategic comparison" on items where your labels differ from prior work) is an efficient, high-signal validity check for any auto-labeled benchmark.
- **Explicit protected-attribute annotation of every item** enables post-hoc slicing; bake demographic/cultural metadata into items from the start.
- **EULA-gated release + datasheet + IRB** as a reusable responsible-release template for dual-use benchmarks.

## 12. Notable quotes
- "we introduce the AI-Face dataset, the first million-scale demographically annotated AI-generated face image dataset" (p.1).
- "10 out of 12 detectors have an AUC higher than 98%, demonstrating our AI-Face dataset is significant for training AI-face detectors in resulting high utility." (p.6)
- "There is currently no reliable detector, as all detectors experience severe large performance degradation under image post-processing and cross-domain evaluation." (p.7)
- "One limitation is that our dataset's annotations are algorithmically generated, so they may lack 100% accuracy... demographic attributes for most AI-generated faces are often too ambiguous to predict and do not map to real-world individuals." (p.8)

## 13. UNKNOWN / not in extract
- Exact per-metric numeric definitions/formulas for FDP, FMEO, FEO, FOAE, FIND (only cited references, formulas in appendices not in extract).
- Full Table 5 numbers for DF-Platter/GenData utility beyond the fragments shown (p.7).
- Appendix content (A-E): detailed license/datasheet, tool-comparison study, labeling protocol details.
- Inter-rater agreement statistics among the 3 annotators (only majority-vote ground truth mentioned, no kappa reported in extract).
- Any evaluation of LLMs (LLaMA2/GPT-4) — explicitly noted as future work only (p.8).
