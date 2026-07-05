---
stem: "2023-Ibrohim-Hate speech and abusive language detection in Indonesian social media"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, design-space, validity-psychometrics]
task_format: "n/a"
scoring_type: "classifier"
dataset_size: null
dataset_construction: "scraped"
languages: ["Indonesian"]
models_tested: []
headline_numbers:
  - "27 papers selected from 1,659 initial candidates across 5 databases for systematic review (p.5, Table 4)"
  - "3,325 hate speech cases handled by Indonesian police in 2017 — a 44.99% increase from 2017's 1,829 cases (p.1)"
  - "Most Indonesian HSAL research uses Twitter text data with classical machine learning (SVM, NB, RFDT) and n-gram features (p.9)"
  - "Best reported performances range from 57.9% accuracy (image dataset) to 98.7% accuracy (text dataset with rule-based annotation) (p.7-8, Table 5)"
---
## 1. Gist
This is a systematic literature review (Kitchenham framework) of hate speech and abusive language (HSAL) detection research in Indonesian social media, covering 27 papers from 2014–2020. Indonesia is the world's 4th largest social media user base and has a serious HSAL problem, yet Indonesian NLP research in this area remains significantly underdeveloped relative to English. The review analyzes definitions, datasets, annotation strategies, preprocessing techniques, and model performance across text, speech, and image modalities. For values-alignment benchmarking, this paper matters as a case study in: how cultural and legal context shapes annotation schemes, the challenges of building non-English hate speech datasets, and the gap between binary detection and richer hierarchical annotation (target, category, level) needed for policy-relevant systems.

## 2. Benchmark/eval design features
This is a review paper, not a benchmark. Core findings:

**Definition landscape**: HSAL definitions in Indonesian research come from five sources: previous works, social media platform rules, Indonesian law (Bareskrim Polri guidelines), sociolinguistic books, or FGD (Focus Group Discussion) results. The Bareskrim Polri (Indonesian cybercrime police) definition is the most authoritative — hate speech must have a specific target (individual or group) and is categorized by religion/creed, race/ethnicity, physical/disability, gender/sexual orientation, and other invective/slander. Three severity levels: weak (individual, no incitement), moderate (group, no incitement), strong (any, with incitement/provocation).

**Dataset landscape**: 
- Modalities: text (dominant), speech, image (one study)
- Sources: Twitter (most common), Facebook, Instagram, YouTube, LINE, Sarahah
- Almost all monolingual Indonesian; only 2 studies use multilingual data
- Most datasets annotated by 3 annotators with 100% agreement or majority voting

**Model landscape**: Most studies use classical ML (SVM, NB, RFDT, Logistic Regression) with n-gram features. Some recent work uses LSTM, BiLSTM, FastText, and early BERT applications. SVM consistently performs competitively. Deep learning outperforms classical ML when sufficient data is available.

## 3. Task format & example item
No benchmark items — review paper. But the review provides detailed examples of the Indonesian HSAL taxonomy (p.3, Table 2):

Example of strong hate speech: "Immediately coordinate the mass power of the Muslims ... to immediately surround the Myanmar embassy ... drive out the Bastard Ambassador and Buddhist that oppressive Rohingya from Indonesia!!!" — Target: Group (Myanmar/Buddhist); Category: Religion/creed + Race/ethnicity; Level: Strong.

Example of abusive-but-not-hate-speech: "Bastard! You're a funny Chinese bro haha" — not hate speech because it expresses familiarity/closeness rather than incitement.

## 4. Scoring / grading methodology
The review covers diverse evaluation metrics used across 27 papers: accuracy and F-measure (F1) are the most common. Results vary by task complexity:
- Binary hate speech detection: up to 98.7% accuracy, 96.2% F-Measure
- Multi-label classification with target/category/level: 66.12% accuracy (all labels), 77.36% accuracy without target/category/level
- Image dataset: 57.9% accuracy
- Multimodal (text+speech): ~86.98% F-Measure

## 5. Dataset construction & provenance
The review analyzes 27 datasets spanning 2014–2020. Key patterns:
- **Twitter dominant**: ~17/27 papers use Twitter data
- **Annotation strategies**: Three annotators per item standard; backgrounds diversified by sex, age, job, ethnicity, religion to reduce bias
- **100% agreement vs. majority voting**: Some studies require 100% agreement (stricter); others use majority voting
- **Expert annotation**: One study uses a linguistic expert from Badan Bahasa (Language Center) West Java
- **Rule-based annotation**: One study uses explicit rules ("abusive word + provocative word = hate speech") to reduce annotator burden
- **The reference multi-label dataset**: Ibrohim & Budi (2019) built a multi-label dataset with hate speech target, category, and level — validated via FGD with Indonesian cybercrime police — appears to be the most richly annotated Indonesian HSAL resource

## 6. Validity evidence
The review notes annotation validity challenges across reviewed papers:
- HSAL annotation is highly subjective — annotator background (sex, age, ethnicity, religion) affects judgments
- Diversity of annotator backgrounds is used as a bias-reduction strategy in best-practice studies
- The Bareskrim Polri FGD process for the reference definition represents the strongest validation approach — external legal/authority grounding
- Most studies do not report inter-annotator agreement statistics explicitly
- Rule-based annotation can eliminate bias for clear-cut cases but struggles with ambiguous cases

## 7. Saturation / discrimination
- Binary classification tasks (hate vs. not hate) show high performance (up to 98.7%) suggesting saturation for simple cases
- Multi-label classification including target/category/level drops to 66% — large headroom for improvement
- Image-based hate speech detection: only 57.9% accuracy — very nascent
- Multimodal (text+speech) approaches show modest improvements over text-only
- Code-switching and informal language remain major unsolved challenges

## 8. Multiturn / agentic aspects
n/a — classification tasks, no interactive dialogue.

## 9. Key numbers
- 27 papers selected from 1,659 initial candidates (p.5, Table 4)
- Database sources: IEEE Xplore (17 papers), ACM (4), Springer (0), ACL Anthology (1), Science Direct (1), Scopus (4) (p.5)
- Research period: 2014–2020 (published 2010-2021 search window, filtered to last 10 years)
- Indonesian police handled 3,325 hate speech cases in 2017, up 44.99% from 1,829 cases in 2016 (p.1)
- 5 hate speech categories: Religion/Creed; Race/Ethnicity; Physical/Disability; Gender/Sexual Orientation; Other Invective/Slander (p.4)
- 3 hate speech severity levels: weak, moderate, strong (p.4)
- Most-used platform: Twitter (p.9)
- Best binary classification: 98.7% accuracy (rule-based annotation + ANN) (p.8, Table 5)
- Multi-label classification with all labels: 66.12% accuracy (p.8, Table 5)
- Multimodal (text+speech): 86.98% F-Measure (p.8, Table 5)

## 10. Pitfalls & limitations
- **Review cutoff**: Papers searched February 4, 2021 — does not cover transformer/BERT-era developments post-2020
- **Definition inconsistency across reviewed papers**: Many papers use foreign definitions (e.g., Twitter's community guidelines) not calibrated to Indonesian cultural/legal context
- **Binary detection is insufficient**: Most research focuses only on hate vs. not-hate — target, category, and level detection is needed for policy use but understudied
- **Dataset fragmentation**: No single standardized dataset used across papers, making comparison difficult
- **Modality gap**: Speech and image-based HSAL detection severely underdeveloped relative to text
- **Code-switching**: Indonesian social media frequently mixes Indonesian with English, Javanese, and other local languages — most models don't handle this
- **Twitter bias**: Overreliance on Twitter data may not represent hate speech on other platforms (WhatsApp, LINE, YouTube comments)
- **Reproducibility**: Many papers don't publicly release datasets or models

## 11. Novel ideas worth stealing
- **Hierarchical annotation schema (target + category + level)**: The Bareskrim Polri-validated Indonesian schema is a well-developed example of going beyond binary labels — adaptable for values-alignment benchmarks that need to distinguish severity and domain of norm violations
- **FGD with legal/authority stakeholders**: Validating annotation guidelines via focus group discussions with domain authorities (cybercrime police, human rights commissions) grounds annotation in legally-recognized definitions — a more rigorous alternative to researcher-defined labels
- **Annotator diversity as bias-reduction strategy**: Explicitly diversifying annotators by sex, age, ethnicity, and religion and reporting this as a methodological decision is a best practice for culturally-sensitive annotation
- **Abusive-but-not-hate distinction**: The explicit separation of abusive language (informal expression of familiarity/emphasis) from hate speech (targeted incitement) is a useful conceptual distinction for benchmarks on offensive content — not all offensive language is morally equivalent
- **Rule-based bootstrapping for clear cases**: Using explicit logical rules ("abusive word + provocative word = strong hate speech") to pre-annotate unambiguous cases before human review can scale annotation while reserving human judgment for borderline cases

## 12. Notable quotes
- "Hate speech and abusive language problems cannot be dealt with immediately by only detecting whether a text contains hate speech and abusive language or not." (p.1)
- "Annotating HSAL is quite challenging since these tasks are quite subjective and can bring up bias on annotation." (p.9)
- "to reduce bias, some researchers also considered the annotators' background including sex, age, job, ethnicity, and religion" (p.9)
- "Although hate speech is often accompanied by abusive language, not every utterance/expression that contains abusive/dirty words/phrases constitutes hate speech." (p.4)

## 13. UNKNOWN / not in extract
- Performance results post-2020 (BERT-era Indonesian NLP developments)
- The full list of 27 papers reviewed (partially available in Table 5 extract but cut off)
- Whether any reviewed datasets are publicly available
- Inter-annotator agreement statistics across reviewed papers
- Whether hate speech in Indonesian social media has shifted patterns post-2021 (pandemic, elections)
- The specific challenges posed by Indonesian code-switching and regional dialects (Javanese, Sundanese) on model performance
