---
stem: "2021-Plaza-del-Arco-OffendES A New Corpus in Spanish for Offensive Language Research"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [design-space, cultural-linguistic, validity-psychometrics, saturation-discrimination]
task_format: "forced-choice"
scoring_type: "mixed"
dataset_size: 47128
dataset_construction: "scraped"
languages: ["es"]
models_tested: ["BETO"]
headline_numbers: ["BETO 4-class macro F1: 64.77% (p.8, Table 6)", "BETO binary macro F1: 78.39% (p.8, Table 7)", "Cohen's kappa inter-annotator agreement: 0.3579 (fair) (p.7)", "47,128 total labeled comments (p.9)", "283,622 total comments collected; 47,128 annotated (p.4)"]
---
## 1. Gist
Plaza-del-Arco et al. (2021) present OffendES, the first large-scale Spanish offensive language dataset focused on young influencer audiences across Twitter, Instagram, and YouTube. The corpus contains 47,128 Spanish comments manually labeled by MTurk workers using a five-category annotation scheme (OFP, OFG, OFO, NOE, NO), with a subset of 14,989 comments labeled by 10 annotators providing probability-vector soft labels for multi-output regression. For values-alignment benchmarking, OffendES is notable for three design innovations: (1) targeting a specific social context (young people and influencer culture), (2) introducing the NOE (non-offensive expletive) category to distinguish genuine offense from culturally normative swearing, and (3) providing distributional confidence labels alongside categorical ones.

## 2. Benchmark/eval design features
**Annotation scheme (5 categories):**
- OFP (Offensive, Person): offensive text targeting a specific individual
- OFG (Offensive, Group): offensive text targeting people sharing ethnicity, gender, sexual orientation, political ideology, religious belief, etc.
- OFO (Offensive, Other): offensive text where target is an organization, event, place, or issue
- NOE (Non-Offensive with Expletives): contains rude/swear words but no offense intent; often has positive connotation
- NO (Non-Offensive): neither offensive nor expletive

**Two annotation subsets:**
- 3-Ann subset: 44,951 comments, 3 annotators each, for multi-class classification
- 10-Ann subset: 14,989 comments, 10 annotators each, provides probability vectors per label for multi-output regression

**Data sources:**
- 12 controversial Spanish influencers (6 male, 6 female, ages 24-35)
- Last 50 posts per influencer tracked across Instagram, Twitter, YouTube
- From 283,622 collected comments: 23,788 selected via offensive lexicon flag + 36,212 selected via lexical diversity maximization

**Key design innovation:** NOE category explicitly separates expletive language used positively ("you're the fucking boss") from actual offensive intent — addressing a known misclassification problem in prior work.

## 3. Task format & example item
From Appendix Table 3 (p.13):
- OFG: "El feminismo es cáncer y las feministas son mierda." / "Feminism is cancer and feminists are shit." — YouTube
- OFP: "El que llora siempre en sus videos por haber sido acosado para dar pena ahora acosa a gente... patético." / "The one who always cries in his videos for having been harassed now harasses people... pathetic." — Twitter
- NOE: "Yo estoy de puta madre en casa... yo nací en cuarentena." / "I'm doing fucking great at home... I was born in quarantine." — YouTube
- NO: "Si pudiera viajar... Que tengas un buen día saludos desde Buenos Aires, Argentina." — Instagram

## 4. Scoring / grading methodology
**Multi-class classification (3-Ann):**
- BETO fine-tuned on 30,079 comments (95%); evaluated on 3,343 (5%)
- Metrics: Precision, Recall, F1 per class + macro and weighted averages
- None-labeled entries (no annotator agreement) excluded from classification experiments

**Multi-output regression (10-Ann):**
- Label confidence = count(annotators choosing label) / total annotators
- BETO fine-tuned on 13,020; evaluated on 685
- Metric: Mean Squared Error (MSE = 0.0241)

**Post-annotation quality control:** One prolific annotator with >60% error rate on tracking comments was removed — reduced 3-Ann subset from 54,023 to 44,951.

## 5. Dataset construction & provenance
- 283,622 total comments collected from Instagram, YouTube, Twitter (Feb-Mar 2020)
- YouTube: 203,863 raw comments; Instagram: 61,351; Twitter: 19,925 (p.4, Table 1)
- Offensive lexicon pre-filter: 23,788 comments flagged; remainder selected via vocabulary-maximizing lexical diversity algorithm
- 60,000 comments sent to MTurk annotation (Spain-based workers only)
- 3-Ann trial: 4,500 instances with 3 annotators; 1,500 instances with 10 annotators (September 2020)
- Final annotation: Nov 17, 2020 – Jan 2, 2021
- Available upon request from authors; case/punctuation/emojis preserved

## 6. Validity evidence
- Cohen's kappa for 3-Ann subset: 0.3579 (fair) — low but acknowledged (p.7)
- After merging OFO into NOE: kappa rises to 0.3837 (marginal improvement) (p.7)
- Tracking comments (gold examples in annotation guide) used to catch unreliable annotators — one annotator with >60% error rate removed (p.7)
- NOE and OFO classes showed the lowest annotator consensus (OFO: only 33.72% 3-annotator agreement) (p.7, Figure 3)
- Lexical diversity analysis (MTLD) confirms meaningful signal: OFP and NOE have low diversity (single-word insults) vs. NO (higher diversity) (p.8, Table 5)
- Female influencers receive more offensive comments than male — findable cross-validation with external literature

## 7. Saturation / discrimination
- BETO macro F1 for 4-class: 64.77%; OFG class F1 only 38.10% (low-frequency class with 425 instances) (p.8, Table 6)
- Binary BETO macro F1: 78.39%; but offensive class F1: 62.82% — still substantial room for improvement (p.8, Table 7)
- None label constitutes 25.6% of 3-Ann subset (11,529 of 44,951) before filtering — indicating high inherent difficulty
- 10-Ann subset has much lower None rate, validating that more annotators improves label quality
- OFO category is systematically difficult; authors ultimately merge it into NOE

## 8. Multiturn / agentic aspects
n/a — all tasks are single-comment, single-turn classification or regression.

## 9. Key numbers
- 283,622 total comments collected (p.4, Table 1)
- 47,128 total labeled comments released (p.9)
- 3-Ann subset: 44,951 comments (after removing unreliable annotator)
- 10-Ann subset: 14,989 comments
- 12 influencers tracked across 3 platforms (p.3)
- dalas: 26.3% of all 3-Ann comments — most represented influencer (p.5, Table 2)
- YouTube: 75% of comments; Instagram: 18.6%; Twitter: 6.4% (p.5)
- 3-Ann label distribution: NO 26,425; OFP 4,102; NOE 2,470; None 11,529; OFG 425 (p.6, Table 3)
- Cohen's kappa: 0.3579 (3-Ann); 0.3837 after OFO→NOE merge (p.7)
- OFO 3-annotator consensus: 33.72% (p.7, Figure 3)
- BETO 4-class macro F1: 64.77% (p.8, Table 6)
- BETO binary macro F1: 78.39% (p.8, Table 7)
- Multi-output regression MSE: 0.0241 (p.8)
- MTLD for NO comments: 66.36 vs. OFP: 28.68 (p.8, Table 5)
- Average comment lengths: YouTube ~190 chars, Twitter ~149, Instagram ~114 (p.6, Table 4)

## 10. Pitfalls & limitations
- **Low inter-annotator agreement**: Cohen's kappa 0.3579 — "fair" barely — reflects genuine conceptual difficulty but also possible schema complexity
- **OFO category instability**: The OFO (offensive targeting organizations/events) label was consistently confused with NOE; authors ultimately merged it — suggesting the original schema was over-specified
- **Platform imbalance**: YouTube provides 75% of comments; Twitter only 6% — results may be platform-specific
- **Influencer concentration bias**: 26% of comments are about a single influencer (dalas) — content-domain variation is limited
- **MTurk-only annotation**: Crowd workers from Spain; no demographic information reported beyond location; possible socioeconomic homogeneity
- **Lexicon pre-filtering**: Non-offensive comments were selected partly by vocabulary novelty, not randomness — this may distort the NO class distribution
- **Available upon request only**: Not openly downloadable; reduces reproducibility
- **Temporal snapshot**: Comments from Feb-Mar 2020 only; no temporal diversity or replication

## 11. Novel ideas worth stealing
- **NOE (Non-Offensive Expletive) category**: Distinguishing culturally normative swearing from genuine offense is a critical design move missing from most binary hate speech datasets. Any values benchmark dealing with harm should include an analogous "technically taboo but contextually acceptable" category.
- **Multi-output regression labels from 10 annotators**: Providing normalized annotator count vectors (probability distributions over labels) enables multi-output regression as a task — more informative than majority-vote labels for borderline cases. This directly parallels SCRUPLES' distributional label design.
- **Influencer-level analysis**: Stratifying by content creator (with known demographics: 6 male, 6 female influencers) allows analyzing offensive comment patterns as a function of target identity. Values benchmarks should include explicit target metadata to enable subgroup analysis.
- **Vocabulary-maximizing comment selection**: Instead of random sampling, using lexical diversity to select a more vocabulary-diverse subset ensures the corpus covers a wider range of language use. Useful for any large-scale benchmark where coverage breadth matters.
- **Tracking comments (gold examples in annotation guide)**: Including known-answer items in every annotation batch provides real-time quality control and allows filtering unreliable workers. This is a scalable, low-cost annotation quality protocol.
- **Platform-comparative analysis**: Collecting from Instagram, Twitter, and YouTube simultaneously enables platform-level analyses (comment length, lexical diversity, offensive rate by platform). Values benchmarks should routinely collect platform metadata.

## 12. Notable quotes
- "The average agreement (kappa coefficient) grew from 36.85% for trial annotations up to 39.37% for final released comments. Yet, this level of agreement is lower than expected, which reflects the difficulty to discriminate among proposed classes." (p.5)
- "In terms of gender, it can be seen that female influencers are subject to a greater number of offensive comments than male accounts." (p.7)
- "The more annotators that were involved, the easier it was to decide the final label for a comment." (p.6)
- "Results show that deep learning models, like BERT, are good estimators of the presence of different kinds of offensive language, but that it is still a challenging task to decide whether a comment is directed to a person or not." (p.9)

## 13. UNKNOWN / not in extract
- Exact demographic profile of MTurk annotators beyond "Spain-based"
- Whether OFO was eventually dropped or retained in subsequent releases
- Whether the full 47,128-comment corpus was eventually made publicly available
- Performance of Spanish-specific models beyond BETO (e.g., XLM-RoBERTa)
- Inter-annotator agreement statistics for the 10-Ann subset separately
- Whether gender of commenters was analyzed (mentioned as future work, p.9)
