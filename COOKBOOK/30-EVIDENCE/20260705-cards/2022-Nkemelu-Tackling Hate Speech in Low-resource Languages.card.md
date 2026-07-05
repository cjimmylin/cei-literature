---
stem: "2022-Nkemelu-Tackling Hate Speech in Low-resource Languages"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, design-space, validity-psychometrics, pluralism-aggregation]
task_format: "classifier"
scoring_type: "classifier"
dataset_size: 226
dataset_construction: "crowdsourced"
languages: ["my"]
models_tested: ["SVM", "Balanced Random Forest", "FastText"]
headline_numbers:
  - "Final dataset: 226 unique Burmese hate speech posts from 43,996 initial Facebook posts (p.5)"
  - "FastText with oversampling achieves F1=0.92, precision=0.93, recall=0.92 (p.7)"
  - "Annotator agreement increased from average 68.75% to 93% after peer feedback sessions (p.6)"
  - "Only less than 4% of Facebook posts in dataset were labeled as hate speech (p.8)"
  - "8 context experts (5 female, 3 male) annotated the data (p.4)"
---
## 1. Gist
This paper reports on a remote community-based study developing hate speech detection for Burmese (Myanmar), motivated by Facebook-spread anti-Rohingya hate speech that contributed to mass violence and genocide. The study develops a four-stage process for collaborating with "context experts" (native Burmese speakers with lived political knowledge) as co-designers, annotators, and model validators — not merely translators. The resulting dataset is small (226 confirmed hate posts from 43,996 initial posts) due to the genuine rarity of hate speech in social media, but the process methodology is the primary contribution. For values-alignment benchmarking, this paper is critical as a case study in how culturally grounded, community-centered annotation differs from crowdsourcing, and why annotation for values-sensitive tasks in underrepresented languages requires context expertise, not just language fluency.

## 2. Benchmark/eval design features
The paper is primarily a process paper, not a benchmark design paper. Core contributions:
- A four-stage collaborative process: (1) partner recruitment and project scoping, (2) hate speech definition + annotation guidelines co-developed with legal experts, (3) data collection and model training, (4) model validation with context experts.
- Binary hate speech classification (hate / not hate) using Burmese Facebook posts.
- Hate speech definition adapted from UN Strategy on Hate Speech + Facebook's protected characteristics list, reviewed by Yangon-based legal experts.
- Lexicon-based data collection using 158 Burmese hate terms (72 from Hatebase + 88 from Phandeeyar COVID-19 tracking).
- Annotator pairing strategy: pairs share posts, then discuss disagreements; iterative feedback increases agreement from 68.75% → 93% over four cycles.

Key methodological arguments:
- Context experts are not the same as language experts — political/cultural lived experience is essential for accurate hate speech annotation.
- Standard IAA metrics (Cohen's κ, Fleiss' κ) are inappropriate when class imbalance is extreme; percent agreement used instead.
- Data work is systematically undervalued in ML projects; stakeholders must be educated about its importance.

## 3. Task format & example item
Binary text classification: each Burmese Facebook post labeled as hate speech (Yes) or not (No).

Annotation guideline example (from p.4):
- Hate speech: posts using "pejorative or discriminatory language with reference to a person or a group on the basis of who they are" (adapted from UN definition).
- NOT hate speech: "The Burmese military is corrupt!" — attacks integrity but does not invoke a protected characteristic.
- Protected characteristics: religion, ethnicity, nationality, race, color, descent, gender, caste, sexual orientation, sex, gender identity, serious disease (composite of UN/Facebook definitions).

No verbatim Burmese example posts are reproduced in the extract due to data sharing restrictions.

## 4. Scoring / grading methodology
Precision, recall, and F1-score on a held-out test set. Oversampling used to address severe class imbalance (less than 4% hate speech). Three classical ML models compared: SVM, Balanced Random Forest (BRF), FastText. Best model: FastText with oversampling (F1=0.92). Standard accuracy-based classification metrics; no human evaluation of model outputs beyond qualitative model validation by context experts.

## 5. Dataset construction & provenance
**Source**: Facebook posts via CrowdTangle API from social and political Burmese pages (October 2018 – June 2020), period including 2020 Myanmar national elections.

**Collection**: Keyword-based retrieval using 158 Burmese hate terms (Hatebase 72 + Phandeeyar 88, combined after deduplication). Starting: 43,996 posts.

**Preprocessing**: Zawgyi→Unicode conversion; remove non-Burmese posts; remove emojis; retain code-switching; word segmentation (Myanmar language tools); stopword removal. After filtering: 5,646 posts for annotation.

**Annotation**: 8 context experts (5F/3M), recruited via political Facebook pages, native Burmese speakers resident in Myanmar, paid. 100 posts/day/annotator over 4 days with paired labeling; remainder individually. Final labeled hate speech posts: 226.

**Data sharing**: Cannot be publicly shared under CrowdTangle's terms of use; annotation guidelines and hate term lexicon released on GitHub.

## 6. Validity evidence
- **Annotator agreement**: percent agreement (used instead of kappa due to class imbalance). Increased from 68.75% → 93% over four peer feedback cycles (p.6).
- **Legal expert review**: Annotation guidelines reviewed and edited by Yangon-based legal team, providing external validity for the hate speech definition.
- **Model validation**: Context experts reviewed live data inference results and identified false positive (benign posts with hate lexicon terms flagged) and false negative (hateful posts lacking archetypal terms) error types.
- **Protected characteristic distribution**: Figure 1 (p.5) shows distribution of protected characteristics in labeled hate posts, described as consistent with Myanmar's socio-political context.
- Note: no inter-rater reliability statistics (κ) reported — a methodological choice justified by class imbalance arguments.

## 7. Saturation / discrimination
The dataset is extremely small (226 hate posts from 5,646 annotated) and highly imbalanced (less than 4% positive). This severely limits the discriminability of any benchmark built on this data. However, FastText with oversampling achieves F1=0.92, which is surprisingly high for such a small dataset — likely reflecting the lexicon-driven sampling that biases toward posts genuinely containing hate-relevant vocabulary. The paper acknowledges this as a methodological caveat (keyword sampling boosts recall but reduces natural distribution).

## 8. Multiturn / agentic aspects
n/a — single-post classification.

## 9. Key numbers
- Initial Facebook posts collected: 43,996 (p.5)
- Posts after preprocessing: 5,646 (p.5)
- Final labeled hate posts: 226 (p.4)
- Hate term lexicon: 72 (Hatebase) + 88 (Phandeeyar) = 158 total (p.5)
- Number of context experts: 8 (5F, 3M) (p.4)
- Agreement increase: 68.75% → 93% after peer feedback (p.6)
- SVM with oversampling: P=0.88, R=0.87, F1=0.87 (p.7)
- FastText with oversampling: P=0.93, R=0.92, F1=0.92 (p.7)
- Hate speech prevalence: less than 4% of Facebook posts (p.8)
- Myanmar Facebook active users (2019): over 21 million (p.9)

## 10. Pitfalls & limitations
- **Extremely small dataset**: 226 hate posts insufficient for robust ML; results are likely not generalizable without substantial data augmentation.
- **Lexicon-biased sampling**: Keyword-based collection overrepresents posts containing known hate terms; implicit/covert hate speech (using no hateful keywords) is systematically missed.
- **No data sharing**: CrowdTangle terms prevent public release; reproducibility is limited to guidelines and lexicons.
- **Percent agreement vs. kappa**: Using percent agreement without correction for chance agreement is critiqued in the IAA literature; author's justification (class imbalance undermines kappa) is valid but leaves uncertainty about annotator quality.
- **Remote study limitations**: All work done remotely during COVID-19; limited ability to conduct in-person training or resolve complex disagreements.
- **Binary labels only**: No target group identification, no severity gradient, no span annotation.
- **Black-box participation**: Technical ML aspects remained opaque to context experts, limiting their agency as co-designers and risking long-term project unsustainability.
- **Data temporal scope**: 2018-2020 data; Myanmar's political situation changed dramatically with the 2021 military coup, potentially making this dataset outdated.

## 11. Novel ideas worth stealing
1. **Context experts as full co-designers**: rather than using crowdworkers who speak the language, recruit people with lived political/cultural expertise and center their ownership of the project — essential for values annotation in politically charged domains.
2. **Annotation pairing strategy**: assigning the same posts to paired annotators for independent labeling followed by structured peer discussion — a low-cost technique that increased agreement from 68.75% → 93% and transferred context knowledge between annotators with different expertise areas.
3. **Legal expert review of annotation guidelines**: sharing guidelines with domain legal experts (not just researchers) for feedback before annotation begins — ensures the hate speech definition is locally valid and legally grounded.
4. **Hybrid lexicon construction**: combining platform-independent (Hatebase) and locally generated (Phandeeyar COVID-specific) lexicons to bootstrap data collection in low-resource settings.
5. **Context experts as model validators**: using the same community experts who annotated data to review live model inference errors — a participatory model validation approach that surfaces culturally specific error types (false positives on culturally ambiguous terms, false negatives on implicit hate).
6. **Naming the undervaluing of data work**: explicitly framing data work as skilled labor requiring fair compensation and stakeholder buy-in, and building this framing into project scoping — directly applicable to any values-annotation project.

## 12. Notable quotes
- "We argue that sustainably addressing hate speech in low-resource language settings involves empowering context experts with the technology-driven tools needed to tackle the problem locally." (p.4)
- "Context experts offer perspectives that add depth and breadth to the technical expertise of 'content experts' (in our case, machine learning researchers)." (p.4)
- "There is no universally agreed-on definition for hate speech, and what counts as hate speech in one context may not be considered hate speech in another." (p.4)
- "We identified two major error types from the model from this step. First, false-positive cases where benign posts containing terms in the hate lexicons or words typically used in hate speech posts and highly represented in the training data were wrongly flagged as hate speech by the model. Second, false-negative cases were hateful posts that did not contain the archetypal hate terms and were not classified as hate speech by the model." (p.6)

## 13. UNKNOWN / not in extract
- Table 1 (annotator labeling counts per pair) references a broken reference ("Table ??") suggesting the table numbering was unresolved at submission
- Figure 1 and Figure 2 are referenced but not reproduced in text form in the extract
- Full hate term lexicon (released on GitHub but not in extract)
- Protected characteristic distribution percentages in labeled hate posts (referenced in Figure 1)
- Details of annotator compensation (amount, payment structure)
- Whether any context experts were Rohingya or from other ethnic minority groups targeted by the hate speech
- Temporal performance analysis (whether model degrades as social media language evolves)
