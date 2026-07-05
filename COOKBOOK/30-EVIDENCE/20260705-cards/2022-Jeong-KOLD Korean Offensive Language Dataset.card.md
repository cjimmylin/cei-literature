---
stem: "2022-Jeong-KOLD Korean Offensive Language Dataset"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, design-space, normative-ethics]
task_format: "classifier"
scoring_type: "exact-match"
dataset_size: 40429
dataset_construction: "crowdsourced"
languages: ["ko"]
models_tested: ["BERT-base (Korean)", "RoBERTa-base (Korean)", "RoBERTa-large (Korean)", "MUDES (multilingual)"]
headline_numbers:
  - "Dataset contains 40,429 comments; 50.2% labeled offensive (p.4)"
  - "Krippendorff's α = 0.55 overall inter-annotator agreement for offensiveness (Level A) (p.4)"
  - "Best offensive detection F1 = 78.8% (RoBERTa-large) (p.6)"
  - "Adding title context boosts target group classification F1 by +13.1 absolute (30.6% relative) (p.7)"
  - "MUDES multilingual model scores only F1=12.8 on Korean span detection vs 40.6 for native model (p.8)"
  - "3,124 annotators participated in creating the final dataset (p.4)"
---
## 1. Gist
KOLD is the Korean Offensive Language Dataset, a 40,429-comment corpus sourced from NAVER news and YouTube, annotated hierarchically with offensiveness, target type (group/individual/other/untargeted), and target group (21 categories tailored to Korean culture). It is the first Korean dataset combining hierarchical offense taxonomy, target group identification, and both offensive- and target-span annotations. For values-alignment benchmarking, KOLD is important because it demonstrates that culturally specific target groups (e.g., Korean-Chinese, Feminist, Progressive/Conservative) diverge sharply from Western English datasets, proving that off-the-shelf multilingual models trained on English data transfer poorly to non-English cultural contexts. It provides a worked example of how hate speech annotation must be grounded in local cultural norms.

## 2. Benchmark/eval design features
Three-level hierarchical annotation schema (adapting OLID/Zampieri 2019):
- **Level A**: Binary offensiveness (OFF / NOT)
- **Level B**: Target type of offensive language (UNT=untargeted, IND=individual, GRP=group, OTH=other)
- **Level C**: Target group attribute + specific target group (21 categories across Gender & Sexual Orientation, Race/Ethnicity/Nationality, Political Affiliation, Religion, Miscellaneous)

Each annotation accompanied by span annotations: offensive spans (the minimal text justifying offensiveness) and target spans (text identifying the targeted entity). Context (article/video title) is provided to annotators.

Data is 80-10-10 train/val/test split. Majority voting across 3 annotators determines gold labels; disagreements resolved by expert inspectors.

Korean-specific annotation design decisions: morphological boundary rules, implicit hate speech guidance, multi-group annotation (a comment can target multiple groups), and 21 target groups expanded from English precedents to include Chinese, Korean-Chinese, and Indian populations as well as Feminist (culturally prominent in Korea).

## 3. Task format & example item
Text classification at three hierarchical levels. Example item (from Table 1, p.2):
- **Title/Context**: "GS25's poster of Brave Girls evokes dispute over gender issues yet again"
- **Comment**: "Feminism is not about gender inequality, It is a mental disorder"
- **Level A**: OFF (offensive)
- **Level B**: GRP (group-targeted)
- **Level C**: Target group = Feminist (Miscellaneous attribute)
- **Offensive span**: entire comment
- **Target span**: "Feminism"

## 4. Scoring / grading methodology
Binary-F1 for Level A (offensiveness); macro-F1 for Levels B (target type) and C (target group). Character-level F1 (following Da San Martino et al. 2019) for span prediction: if ground truth is empty, F1=1; if prediction is empty, F1=0. Training uses HuggingFace Transformers; learning rate grid search over {1e-5, 2e-5, 3e-5, 5e-5}, epochs {1–5}, batch size 32/64. Results reported as mean over 5 runs.

## 5. Dataset construction & provenance
**Source**: Comments from NAVER news articles and YouTube videos (March 2020–March 2022), collected using predefined Korean keywords across gender, sexual orientation, race/ethnicity, religion domains. 43,996 comments collected initially; filtered to 40,429 final annotations.

**Annotation**: 3,124 crowdworkers recruited via SelectStar (Korean crowdsourcing platform), each worker capped at 1% of data to ensure demographic diversity. Annotators screened via qualification test; embedded gold questions used for quality control. 3 annotations per comment. IRB approved (KAIST #KH2021-177). Annotators paid above minimum wage.

**Size**: 40,429 comments total; train/val/test = 80/10/10 split.

**Licensing**: Publicly released at http://github.com/boychaboy/KOLD.

**Contamination controls**: User IDs not collected; usernames replaced with `<user>`, URLs with `<url>`, emails with `<email>`.

## 6. Validity evidence
**Inter-annotator agreement (Krippendorff's α)**:
- Level A (offensiveness): α = 0.55 (p.4)
- Level B (target type): α = 0.45 (p.4/5)
- Level C (target group): α = 0.65 (p.5)

Overall average α = 0.55. The lower α for Level B compared to Level C suggests that distinguishing between individual vs. group vs. other targets is harder than identifying the specific group once group-targeting is established.

**Cross-lingual validity**: Translated English OLID data (via Google Translate) only achieves F1=63.2 vs. KOLD-trained model's F1=76.9 for offensiveness detection (p.7), confirming the need for culture-specific data.

**Model comparison**: Hierarchical difficulty confirmed—as granularity increases across levels A→B→C, performance drops consistently across all model sizes, validating the label hierarchy.

## 7. Saturation / discrimination
The best model (RoBERTa-large) achieves F1=78.8 at Level A (offensiveness) with substantial room for improvement. Level B target type classification tops at 62.7 F1, and Level C target group at 57.5 F1—significant headroom remains, especially for fine-grained group classification.

Offensive span detection is notably harder (best F1=45.4) than target span detection (best F1=62.5), suggesting the task of identifying the precise offensive language rather than its target is harder. Multi-task learning improves span detection (+10% F1) while slightly reducing classification accuracy.

Title ablation shows that without context, Level C drops by 13.1 F1 points (30.6% relative), revealing that context is critical for discriminating fine-grained cultural targets.

## 8. Multiturn / agentic aspects
n/a — single-comment classification task with static title context.

## 9. Key numbers
- Total dataset size: 40,429 comments (p.1)
- Offensive comments: 20,130 (49.8% NOT, 50.2% OFF approximately) (p.4)
- Group-targeted offensive: 12,413 comments; 30.7% of whole dataset (p.4)
- Number of annotators: 3,124 (p.4)
- Level A Krippendorff's α: 0.55 (p.4)
- Level B Krippendorff's α: 0.45 (p.5)
- Level C Krippendorff's α: 0.65 (p.5)
- Best Level A F1 (RoBERTa-large): 78.8% (p.6)
- Best Level B F1: 62.7% (p.6)
- Best Level C F1: 57.5% (p.6)
- Best offensive span F1: 45.4% (p.6)
- Best target span F1: 62.5% (p.6)
- Title ablation boost for Level C: +13.1 F1 (30.6%) (p.7)
- KOLD model vs. translated OLID for offensiveness: 76.9 vs. 63.2 F1 (p.7)
- KOLD span model vs. MUDES: 40.6 vs. 12.8 F1 (p.8)
- Top 3 target groups: Feminist (11.42%), LGBTQ+ (10.55%), Women (8.7%) (p.5)

## 10. Pitfalls & limitations
- **Keyword-based collection bias**: Articles/comments collected using predefined offensive keywords, which oversamples offensive content and may not represent the natural distribution of social media.
- **High annotation cost**: 3,124 annotators, 3 annotations per comment, with complex guidelines requiring extensive training time (p.9).
- **Temporal drift**: Hateful language evolves (COVID-19 targets, political figures); a model trained on 2020-2022 data may not perform on future hate speech patterns (p.9).
- **Coverage of Korean social media**: Only NAVER news and YouTube; excludes other platforms (e.g., Twitter, Kakao) whose offensive language patterns may differ (p.9).
- **Annotator demographic balance**: Workers capped at 1% each but no demographic breakdown of the 3,124 annotators is provided beyond this mechanism.
- **Public release limitation**: Offensive content in the dataset could be misused to generate and publish hate speech; authors acknowledge they cannot prevent all malicious use (p.9).
- **Multi-group overlap**: Multi-targeted group annotation complicates counting and model evaluation.

## 11. Novel ideas worth stealing
1. **Three-level hierarchical annotation** that proceeds from coarse (offensive/not) to fine-grained (target group) — each level can be evaluated independently, creating a difficulty gradient useful for benchmarking.
2. **Dual span annotation** (offensive span + target span) as rationale for the classification decision — this interpretability layer could be adapted for values-alignment tasks to require models to justify their moral judgments with textual evidence.
3. **Context-as-input**: providing the article/video title alongside the comment as required context — modeling the realistic deployment scenario and revealing the dependency of fine-grained judgment on contextual grounding (+13.1 F1 for group identification).
4. **Culture-tailored target taxonomies**: rather than importing English taxonomy, starting with 1,000 pilot samples to identify culturally salient groups — a design principle directly applicable to non-WEIRD values benchmarking.
5. **Annotator diversity enforcement via per-worker caps** (1% max per worker) combined with qualification testing and gold question embeds — a practical inter-annotator quality control mechanism scalable to larger crowdsourcing efforts.
6. **Pairing strategy for annotator alignment**: requiring each annotator to label the same posts as a partner before peer review — a simple technique that improved agreement from 68.75% to 93% in similar low-resource settings.

## 12. Notable quotes
- "Language-speciﬁc datasets are essential for offensive language which is very culture- and language-dependent." (p.2)
- "Our novel ﬁnding is that target groups are deﬁned based on the speciﬁc language and culture to embrace ongoing social phenomena and reﬂect them to the dataset." (p.5)
- "In KOLD, 55.1% of group-identiﬁed offensive comments have no target span marked in the comment, which implies that in the majority of the cases, titles contain information about the targets." (p.5)
- "Although MUDES scores high on English (61.6), the performance drops signiﬁcantly in Korean (12.8)." (p.8)

## 13. UNKNOWN / not in extract
- Full annotator demographic breakdown (age, gender, political affiliation of the 3,124 workers)
- License type (CC or other) for the public release
- Detailed inter-annotator agreement at Level C broken down by specific target group attribute
- Whether the dataset includes images/multimedia or is text-only for all 40,429 comments
- Exact train/val/test sizes at each hierarchical level
