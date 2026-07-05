---
stem: "2025-Fillies-A novel German TikTok hate speech dataset far-right comments against"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [design-space, validity-psychometrics, cultural-linguistic, normative-ethics]
task_format: "n/a"
scoring_type: "human-rating"
dataset_size: 10586
dataset_construction: "scraped"
languages: ["de"]
models_tested: []
headline_numbers:
  - "13.76% of comments annotated as hateful (majority agreement on specific label) (p.1)"
  - "26.04% flagged as problematic (at least one non-hate label by two annotators) (p.11)"
  - "Fleiss kappa average inter-annotator agreement: 0.40 (p.13)"
  - "59.3% of comments classified as negative by BERT sentiment classifier (p.14)"
  - "10,586 comments from 9,723 unique users across 146 TikTok videos (p.11)"
---
## 1. Gist
Fillies et al. present the first German hate speech dataset collected from TikTok, focusing on far-right comment sections under videos from accounts identified by domain experts in online extremism. The 10,586 annotated comments use a novel 32-label hierarchical annotation scheme developed with extremism experts, covering types of hate (dehumanization, devaluation, stereotyping, criminalization, threatening language, violence/killing, insult), origins of hate (ideology and narrative: Third Reich nostalgia, white supremacy, anti-LGBTQIA+, anti-wokeness, misogyny/anti-feminism, antisemitism, etc.), and targets of hate (gender, immigration status, national origin, race/ethnicity, religious beliefs, sexual orientation, occupation). Three trained annotators produced a dataset with moderate inter-annotator agreement (Fleiss κ = 0.40) and 13.76% hate prevalence. The dominant targets are politicians (especially the German Green Party) and women. The paper contributes a dataset, a detailed annotation schema, and quantitative/qualitative analysis including keyword analysis and BERT-based sentiment scoring. For values-alignment benchmarking this paper is relevant as a model for fine-grained annotation schema design for culturally-specific, platform-specific toxic content, with honest reporting of annotation challenges and mental health impacts.

## 2. Benchmark/eval design features
Not an LLM benchmark — a dataset paper. The evaluation framework is the annotation scheme itself: a 32-label multi-label taxonomy organized into three top-level classes (hate speech, non-hate speech, unreadable), with hate speech subdivided into types, origins, and targets. Each comment can receive multiple labels simultaneously. An intensity level (low/medium/high) is also assigned to hateful statements. Annotation procedure: iterative guideline development with annotators; independent annotation with Doccano; majority voting (at least 2/3 annotators agree) for final labels; senior adjudicators resolve disagreements. The ensemble of 6 classifiers used to select high-hate videos is a methodological novelty: videos with highest average hate (by classifier ensemble) were selected until 10,000 comments were reached.

## 3. Task format & example item
Not applicable for LLM evaluation. The annotation task is multi-label classification of a TikTok comment with context that it was posted under a German far-right video.

Examples from annotation scheme (pp.8–10):
- Intensity Low: "Du Arsch bist der letzte Dreck" (You ass, are the last dirt)
- Intensity Medium: "Lieber ein Arschlo..... als Grüner kriminellen Dreck" (Rather an a... than green criminal dirt)
- Intensity High: "Diese schlampe baerbock holt sie alle rein toetet sie" (The slut Baerbock, get her and kill her)

## 4. Scoring / grading methodology
Human annotation with majority voting (≥2/3 annotators must agree for a label to be included). Binary hate flag: True if ≥2 annotators selected any non-hate label. Inter-annotator agreement: Fleiss' Kappa on binary vector representation of multi-label annotations. Final combined annotation used for analysis; individual annotator labels retained in dataset. Sentiment analysis via pre-trained German BERT-based classifier (Guhr et al., 2020).

## 5. Dataset construction & provenance
Source: TikTok comment sections. Account selection: experts from Modus-Zad identified 323 accounts relevant to German-speaking far-right ecosystem via snowball sampling; 142 remained accessible. Collection period: 1 September – 30 November 2023; ~815,000 total comments collected. Subset selection: random sample of ~150,000 comments grouped by video; 6-classifier ensemble scores used to select videos with highest hate; first videos until 10,000 comment threshold. After cleaning (duplicates, title-only, bots, URL-only): 10,586 comments from 146 videos, 9,723 unique users. Anonymized via NER and pattern-matching before publication. Available at Zenodo (by request, verified research institutions only).

## 6. Validity evidence
Fleiss κ = 0.40 average (pairwise: 0.35–0.43), classified as "fair, bordering on moderate" (p.13). Authors acknowledge this is limited given the large taxonomy. Qualitative validity supported by domain expert involvement in taxonomy design and annotator training. External validity supported by correspondence with real-world reports (e.g., German news reporting on Green Party minister receiving 700 criminal complaints). No inter-rater agreement above 0.5 reported for any pair. Sentiment analysis (59.3% negative) corroborates annotation outcomes.

## 7. Saturation / discrimination
Dataset is highly imbalanced: 13.76% hateful at majority-agreement level; 9 of 32 labels have fewer than 20 examples. Heavy concentration in insult (179 alone, 323 with others), threatening language (98 + 126), and devaluation (44 + 155). Rare labels (antisemitism: 8 total, white supremacy: 4 total) severely limit classifier training. Sentiment distribution: 59.3% negative, though not all negative = hateful.

## 8. Multiturn / agentic aspects
n/a. Individual comment annotations; no conversation structure analyzed.

## 9. Key numbers
- 10,586 annotated comments from 146 TikTok videos (p.11)
- 9,723 unique user IDs (p.11)
- 13.76% hateful (majority agreement on specific label) (p.1)
- 26.04% problematic (any non-hate label by ≥2 annotators) (p.11)
- 32-label annotation taxonomy (p.2)
- 3 annotators; average age 33.33 years, 2 male/1 female, all native German speakers (p.4)
- Fleiss κ: annotator 1/2 = 0.42; 1/3 = 0.43; 2/3 = 0.35; average = 0.40 (p.13)
- Sentiment: 59.3% negative (p.14)
- Intensity distribution: low = 49.4%, medium = 33.1%, high = 17.5% (p.12)
- Most common target: politicians (97 alone, 395 with others) (p.12)
- Most common type: insult (179 alone, 323 with others) (p.11)
- Top keyword across all labels: "grünen" (Greens/Green Party) (p.13)
- Collection period: 1 Nov – 30 Nov 2023 (p.4)

## 10. Pitfalls & limitations
- Only three annotators; insufficient for robust multi-class multi-label agreement (p.13).
- Large taxonomy (32 labels) with sparse coverage of many classes — many labels have <20 examples, limiting classifier training (p.11).
- Temporal scope limited to November 2023 only (p.14).
- Single platform (TikTok); findings may not transfer to other platforms (p.14).
- All annotators are adult German-speaking academics; may struggle with youth language (Algospeak, dialectal slang) (p.14).
- Initial video selection used English-translated classifier ensemble, potentially introducing translation-based biases (p.4).
- Dataset access is gated (request-only), limiting reproducibility.
- Annotator mental health impacts acknowledged but not systematically mitigated in study design (p.15).

## 11. Novel ideas worth stealing
1. **Classifier-ensemble-guided sample selection**: Using an ensemble of 6 existing classifiers to pre-select high-hate videos (rather than random sampling) increases hate prevalence from ~1% in the wild to ~14% in the dataset — a budget-efficient way to oversample rare target content.
2. **Three-axis annotation taxonomy (type/origin/target)**: Decomposing hate speech into what kind of hate, why (ideological origin), and who is targeted enables fine-grained co-occurrence analysis. The cross-tabulation of these axes reveals structural patterns (e.g., politicians × insult × delegitimization of democracy as a tight cluster).
3. **Intensity level within hate class**: Annotating low/medium/high intensity provides a severity gradient that binary labels miss — critical for triage/moderation prioritization.
4. **Expert-in-the-loop taxonomy design**: Collaborating with domain experts in online extremism (Modus-Zad) grounds the taxonomy in real-world threat modeling rather than abstract academic categories.
5. **Algospeak and dialectal evasion documentation**: Qualitative observation that Bavarian/Austrian dialects and Algospeak (misspellings, character substitutions) are used to evade moderation suggests NLP benchmarks need robust-to-orthographic-variation test sets.
6. **Honest annotator mental health reporting**: Documenting that annotators capped sessions to protect mental health, and that one withdrew, is important for responsible dataset construction and is increasingly required by publication standards.

## 12. Notable quotes
- "The Grünen party is a frequent target of hate speech... In all types_of_hate classes... the Grünen party is mentioned within the top ten keywords." (p.13)
- "One annotator specifically noted that engaging extensively in annotation 'gives you a dark worldview if you annotate too much in one day.'" (p.15)
- "The general observation is that these dialects are often used to express very hateful thoughts. It may be that formulating hateful sentences in the dialect is a tactic applied by users to avoid moderation." (p.15)
- "Far-right groups use extreme rhetoric to frame the green party as an enemy." (p.15)

## 13. UNKNOWN / not in extract
- Full precision/recall of the 6-classifier ensemble used for video selection.
- Whether the dataset includes the video-level metadata (video topics) or only comments.
- Specific identities of the 323 far-right accounts used for data collection.
- Whether the Zenodo release includes individual annotator labels or only combined labels.
- Details of the GDPR anonymization NER models used.
- Whether any quality verification was done on the classifier-ensemble video selection step.
