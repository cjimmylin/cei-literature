---
stem: "2022-Jeong-Zero-shot Visual Commonsense Immorality Prediction"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [normative-ethics, moral-psychology, design-space]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 2172
dataset_construction: "scraped"
languages: [en]
models_tested: [CLIP ViT-B/32, CLIP ViT-B/16, CLIP ViT-L/14, GPT-3 (few-shot), BERT-base, BERT-large, RoBERTa-large, ALBERT-xxlarge]
headline_numbers: ["Visual Commonsense Immorality benchmark: 2,172 immoral images across 25 keywords in 3 categories (p.2, p.6)", "Human study: 172 AMT participants, our-benchmark median immorality 4.10 vs MS-COCO 1.91 on 5-point Likert (p.9)", "CLIP text classifier accuracy 74.4-79.2% vs NLP baselines 62.9-90.4% (p.7)", "Category mean immorality: felony 0.858, antisocial 0.809, environment 0.762 (p.8)", "Zero-shot F-measure on own benchmark 0.962 (ViT-B/32) (p.8)"]
---
## 1. Gist
This paper builds a zero-shot model to predict "commonsense immorality" of images by training an MLP classifier on the text-only ETHICS commonsense-morality dataset (Hendrycks et al. 2021) inside CLIP's joint image-text embedding space, then transferring to unseen images. Its benchmark contribution — a new Visual Commonsense Immorality (VCI) dataset of 2,172 immoral images spanning felony, antisocial behavior, and environmental pollution — is a rare visual moral-judgment evaluation resource. For values-alignment benchmarking it matters as (a) an early example of grounding a moral benchmark in a legal/normative taxonomy (US Code Title 18) plus commonsense keywords, (b) a demonstration of cross-modal transfer of moral labels from text to image, and (c) a case study in the fragility and cultural narrowness of "commonsense immorality" as a construct.

## 2. Benchmark/eval design features
Construct measured: degree of commonsense immorality ("action that clearly should not have been done", p.6), predicted as a continuous 0-1 score or binarized moral/immoral. Two artifacts: (1) a text classifier trained on ETHICS commonsense morality (>21K examples: ~6K short 1-2 sentence + ~7K long 1-8 paragraph scenarios); (2) the VCI image benchmark: 2,172 images from 25 immoral keyword queries grouped into 3 categories — felony (armed robbery, burglary, kidnapping, vandalism, drunk driving), antisocial behavior (jaywalking, exam cheating, secondhand smoking, manspreading, affair, etc.), and environmental pollution (fly-tipping, air/water/land pollution, space junk). Answer space: binary label or immorality probability.

## 3. Task format & example item
Text training item: map a sentence to binary moral/immoral, e.g. "I painted the entire school with a nude lady" (p.2), "I punched my friend" (p.4), "I trashed his essay" (short) (p.7). Image task: given an unseen image (e.g. a person striking with a hammer), output immorality probability (p.9). Human eval prompt: "How immoral is the image below?" on 5-point Likert (p.9).

## 4. Scoring / grading methodology
Model: binary cross-entropy trained MLP head on frozen CLIP embeddings (Eq. 1, p.5); evaluated by F-measure with alpha=0.2 (recall-emphasized) and accuracy (p.8). Video: classify violent if mean per-frame probability > 0.7 (p.9). Human validation: 5-point Likert immorality ratings averaged and compared across image sources (p.9). Threshold 0.9 used in human-study experiments (p.9).

## 5. Dataset construction & provenance
VCI images scraped via Google Image queries for 25 immoral keywords, then manually filtered to remove irrelevant images (p.2, p.6), inspired by ImageNet-Sketch collection method. 2,172 images total (p.6). Keyword taxonomy grounded in US Code Title 18 for felonies plus dictionary "harmful to society" definition for antisocial behavior (p.6). Training source: ETHICS commonsense dataset — short scenarios from AMT, long from Reddit with filters (p.5). ETHICS drawn from four countries (p.5). Code and dataset released on GitHub (p.2). Evaluation also uses MS-COCO, ImageNet, SMID, Sexual Intent Detection, Real Life Violence Situations, NSFW, XD-Violence (p.7).

## 6. Validity evidence
Human study: 172 AMT participants from 6+ ethnic groups rated 100 sampled images; VCI images rated median 4.10 immorality vs. MS-COCO 1.91, confirming construct validity of the benchmark (p.9). Model beats prior work (Schramowski et al.) 3.14 vs 2.82 median (p.10). Criterion alignment with human intuition claimed. Text classifier compared against NLP baselines (Table 3, p.20). No inter-rater reliability statistic reported.

## 7. Saturation / discrimination
Model achieves 0.962 F-measure on its own VCI benchmark (ViT-B/32) — very high, suggesting the benchmark is relatively easy for the matched model, but this partly reflects domain alignment with ETHICS action-centric scenarios (p.8). Performance varies widely across external datasets (NSFW 0.243 for ViT-B/32 vs 0.837 for ViT-B/16, p.8), showing modality/domain gaps. Category discrimination present: felony > antisocial > environment (p.8), with "space junk" an outlier low (0.545, p.9).

## 8. Multiturn / agentic aspects
n/a — single-image / single-text classification, plus per-frame video scoring (non-interactive).

## 9. Key numbers
- VCI benchmark: 2,172 immoral images, 25 keywords, 3 categories (p.2, p.6)
- ETHICS commonsense subset: >21,000 examples (~6K short + ~7K long) (p.4-5)
- Text classifier CLIP accuracy: ViT-B/32 74.4%, ViT-L/14 79.2% (p.7, p.20)
- NLP baselines: GPT-3 few-shot 73.3%, RoBERTa-large 90.4%, BERT-large 88.5% (p.20)
- Human study: 172 participants; VCI median 4.10 vs MS-COCO 1.91 (p.9)
- Category immorality means: felony 0.858, antisocial 0.809, environment 0.762 (p.8)
- Zero-shot F-measure (alpha=0.2) on VCI: 0.962 (ViT-B/32) (p.8)
- Video: 72.7% accuracy, 75.7% F-measure on Real Life Violence (p.9)

## 10. Pitfalls & limitations
Construct is culturally contingent — authors admit "morality is an area of value judgment, it can vary given the specificity of culture" (p.6) yet anchor felonies in US law, embedding a WEIRD/US-centric moral frame (manspreading and jaywalking treated as "immoral"). Images judged from static single frames lose context (p.6). Google-scraped images risk selection bias (query terms presuppose immorality). Binary immoral/moral labels collapse degree. CLIP text encoder capped at 77 tokens degrades long scenarios (p.20). Only immoral images collected — no matched neutral controls within VCI. Small human study (172) and no IRR. Transfer accuracy on external datasets is inconsistent (NSFW 0.243).

## 11. Novel ideas worth stealing
- **Cross-modal label transfer**: train a moral classifier on abundant text data, apply it in a shared embedding space to a modality (images) lacking labeled data — a template for extending any text values benchmark to images/audio/video cheaply.
- **Legal-code-grounded taxonomy**: anchoring benchmark categories in a concrete normative source (US Code Title 18) gives defensible provenance for "why is this immoral". A pluralistic version could anchor in multiple legal/religious codes to surface cross-cultural divergence.
- **Three-tier severity taxonomy** (felony / antisocial / environment) yields graded difficulty and lets you measure whether models track human severity ordering — reusable as a discrimination axis.
- **Auditing existing benchmarks for latent immoral content** — they run the classifier over ImageNet and find many immoral images (p.8), a reusable "contamination/hygiene audit" move for training data.
- **Recall-weighted F-measure (alpha=0.2)** as a deliberate choice for safety-relevant detection where false negatives are costlier.
- **Human-study anchoring across sources** (own benchmark vs known-moral MS-COCO) as a cheap validity check that a "hard" set is actually judged worse by humans.

## 12. Notable quotes
- "we propose a model that predicts visual commonsense immorality in a zero-shot manner." (p.1)
- "Since morality is an area of value judgment, it can vary given the specificity of culture or situation. However, it is generally clear that crime or violence is a value to be rejected." (p.6)
- "we observed that widely-used image classification benchmarks, such as ImageNet, contain immoral visual scenes, potentially negatively impacting the trained model's behavior." (p.10)
- "participants answered that images from our created benchmark are immoral (median score was 4.10), while images from MS-COCO (mostly moral) received 1.91." (p.9)

## 13. UNKNOWN / not in extract
- Exact per-keyword image counts (only a bar chart described, p.6).
- Inter-rater reliability of the human study not reported.
- Licensing of scraped VCI images unspecified.
- Train/test split sizes for the VCI image benchmark itself (splits given only for ETHICS text).
- Demographic breakdown of the 172 (vs 170) participants beyond "6+ ethnic groups".
