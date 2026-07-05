---
stem: "2025-Vargas-Context-Aware and Expert Data Resources for Brazilian Portuguese Hate"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, validity-psychometrics, design-space, normative-ethics]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 7000
dataset_construction: "crowdsourced"
languages: ["pt-BR", "en", "es", "fr", "de", "tr"]
models_tested: ["mBERT", "fastText", "SVM", "Naive Bayes"]
headline_numbers:
  - "HateBR 2.0 corpus: 7,000 Instagram comments (3,500 offensive, 3,500 non-offensive), expert-annotated (p.1)"
  - "MOL multilingual offensive lexicon: 1,000 terms/expressions in Brazilian Portuguese with translations to 5 languages (p.1)"
  - "Cohen's kappa for binary class annotation: 0.75 average across annotator pairs (p.10)"
  - "Fleiss' kappa: 0.74 for binary class (p.10)"
  - "Best baseline performance on HateBR 2.0: mBERT 85% F1-score (p.16)"
  - "MOL model on Portuguese corpus: 88% F1-score (p.17)"
---
## 1. Gist
This paper introduces two complementary hate-speech resources for Brazilian Portuguese: (1) HateBR 2.0, an updated expert-annotated corpus of 7,000 Instagram comments from Brazilian politicians' accounts, with binary offensive/non-offensive labels and nine hate-speech target categories; and (2) MOL (Multilingual Offensive Lexicon), a 1,000-term context-aware lexicon manually extracted by a linguist and translated by native speakers into English, Spanish, French, German, and Turkish. Both resources achieve high inter-annotator agreement and are designed to address the scarcity of quality hate-speech resources for low-resource languages. For values-alignment benchmarking, this paper demonstrates expert-annotation methodology, the importance of context-dependent offense classification, deeply culture-rooted terms, and multilingual adaptation of normative concepts.

## 2. Benchmark/eval design features
**HateBR 2.0 corpus:**
- Two-layer annotation schema: (1) binary offensive vs. non-offensive; (2) multi-class hate speech target (9 categories: antisemitism, apologist for dictatorship, fatphobia, homophobia, partyism, racism, religious intolerance, sexism, xenophobia, or non-hate offensive).
- Balanced classes: 3,500 offensive + 3,500 non-offensive (exactly balanced by design).
- Comments from 6 Brazilian politicians' accounts (3 left-wing, 3 right-wing; 4 women, 2 men).
- 17.4% of original HateBR replaced (1,216 comments) to remove one-word and highly-similar items.

**MOL lexicon:**
- 1,000 explicit (951) and implicit (49) pejorative terms/expressions.
- Two contextual labels: context-independent (mostly pejorative, 612 terms) vs. context-dependent (ambiguous context, 388 terms).
- 150 terms also labeled with hate speech targets.
- ~10% classified as "deeply culture-rooted" (no adequate translation possible).
- Translated to 5 languages by native speakers with cultural adaptation.

## 3. Task format & example item
Binary classification task. Example offensive comments (Table 2, p.5):

Offensive: "Essa besta humana é o câncer do País, tem q voltar p jaula, urgentemente! E viva o Presidente Bolsonaro."
Translation: "This human beast is the cancer of the country, it has to go back to the cage, urgently! And long live to President Bolsonaro."

Non-offensive: "A minoria rica é bem organizada e se reúnem secretamente. Lucram muito com essa política exclusiva deles."
Translation: "The wealthy minority is well organized and meets in secret. They profit a lot from this exclusive policy of theirs."

Annotators classified each comment as offensive or non-offensive at layer 1, then identified which of 9 hate speech targets applied at layer 2.

## 4. Scoring / grading methodology
Annotation agreement measured with Cohen's kappa (pairwise: AB=0.75, BC=0.69, CA=0.80, avg=0.75) and Fleiss' kappa (0.74) for binary class. For tie cases in hate speech targets, a linguist adjudicated.

Baseline experiments evaluated with precision, recall, and F1-score. Six models tested: TF-IDF+SVM, TF-IDF+NB, fastText unigram/bigram/trigram, mBERT. 90%/10% train/validation split. MOL lexicon experiments tested SVM with two feature types (MOL weights and B+M combined weights) on HateBR 2.0, OLID (English), and HatEval (Spanish).

## 5. Dataset construction & provenance
- Source: Instagram comments on posts of 6 Brazilian politicians (political domain selected deliberately).
- Original HateBR (Vargas et al. 2022): 7,000 comments; HateBR 2.0 replaced 1,216 comments (one-word: 305 offensive + 911 non-offensive) to improve classifier generalizability.
- Annotators: 3 experts with at least PhD-level education, from different Brazilian regions (North and Southeast), diverse political alignment (liberal/conservative), diverse racial background (white and Black women).
- MOL extraction: linguist manually identified pejorative terms from HateBR corpus, then 3 expert annotators classified contextual usage.
- MOL Kappa for context annotation: 0.73 average (AB=0.72, BC=0.60, CA=0.87).
- Translations by native speakers from Brazil, USA, Peru, Burkina Faso/Africa, Germany, Turkey.
- Both resources publicly available: HateBR 2.0 at github.com/franciellevargas/HateBR; MOL at github.com/franciellevargas/MOL.
- License: Creative Commons Attribution 4.0.

## 6. Validity evidence
- High inter-annotator agreement: Cohen's kappa 0.75 (binary), Fleiss' kappa 0.74 — compared favorably to existing Portuguese datasets (which the paper reports have lower agreement).
- Balanced class distribution (3,500/3,500) avoids bias in classifier evaluation.
- Expert annotators (PhD-level) with diverse demographic and political profiles — reduces annotator bias.
- Baseline mBERT at 85% F1-score outperforms prior state-of-the-art on Portuguese: OLID-BR (77%), ToLD-Br (76%), previous HateBR (88% with NB/SVM on original version but see note).
- MOL lexicon contextual annotation at 0.73 kappa, considered "substantial agreement" per Landis and Koch (1977).
- ROC curve analysis shows B+M model has fewer overall wrong predictions than MOL despite lower F1.

## 7. Saturation / discrimination
Balanced corpus and strong baselines suggest the classification task is tractable but not trivially easy. mBERT at 85% F1 shows headroom for improvement. The context-dependent/independent distinction in MOL is an interesting discriminative feature: context-dependent terms weighted weakly while context-independent terms weighted strongly. Misclassification examples reveal the core challenge — highly ambiguous or culture-rooted terms (e.g., "coxinha" in Portuguese used pejoratively for socially privileged groups) cause false positives.

## 8. Multiturn / agentic aspects
n/a — static annotation task and classification experiments; no interactive components.

## 9. Key numbers
- 7,000 total comments in HateBR 2.0 (3,500 offensive, 3,500 non-offensive) (p.11)
- 1,216 comments replaced from original HateBR (305 offensive, 911 non-offensive) (p.11)
- 2,099 offensive comments from right-wing vs. 1,401 from left-wing politicians' accounts (p.11)
- 1,000 terms in MOL (951 explicit, 49 implicit) (p.12)
- 612 context-independent, 388 context-dependent MOL terms (p.12)
- 150 MOL terms labeled with hate speech targets (p.12)
- ~10% of MOL terms classified as deeply culture-rooted (p.11)
- Cohen's kappa binary class: avg 0.75 (p.10)
- Fleiss' kappa: 0.74 (p.10)
- MOL context annotation kappa: avg 0.73 (p.12)
- mBERT F1: 0.85 on HateBR 2.0 (p.16)
- MOL model F1 on Portuguese: 0.88 (p.17)
- Brazil: 3rd worldwide in Instagram audience with 110 million users (p.8)

## 10. Pitfalls & limitations
- Single-domain corpus (Instagram, political domain) — may not generalize to other platforms or topics.
- Annotations reflect definitions and values of 3 Brazilian PhD experts — may not reflect broader cultural variation within Brazil.
- Hate speech annotation is inherently subjective; binary label may oversimplify.
- Deeply culture-rooted terms (~10%) cannot be meaningfully translated, limiting cross-lingual transfer.
- MOL covers 1,000 terms manually extracted from a 7,000-comment corpus — vocabulary coverage is limited.
- Context-dependent/independent distinction requires domain expertise to apply correctly.
- Results on non-Portuguese languages (English/Spanish) use different existing corpora (OLID, HatEval), making direct comparison difficult.

## 11. Novel ideas worth stealing
- **Deeply culture-rooted category**: Explicitly flagging terms that have no adequate translation equivalent (~10%) is a powerful acknowledgment of cultural incommensurability in normative evaluation — valuable for cross-lingual values benchmarks.
- **Context-dependent vs. context-independent annotation axis**: Labeling whether a term is offensive only in context vs. always offensive provides a richer annotation than binary offensiveness; analogous schemes could apply to moral/values concepts.
- **Expert annotator diversity as bias mitigation**: Requiring annotators of different regional origin, political alignment, and race is a principled approach to reduce demographic homogeneity bias — more rigorous than typical crowdsourcing designs.
- **Balanced class design as evaluation precondition**: Deliberate 50/50 class balance avoids metrics being dominated by majority-class performance, making F1 scores more interpretable.
- **Lexicon with contextual weights**: Assigning different feature weights based on context-dependence classification (strong weight for context-independent, weak for context-dependent) is a simple but principled way to encode normative pragmatics.

## 12. Notable quotes
- "We argue that hate speech should be addressed as a cultural-aware research problem since it is a complex issue that deals with commonsense knowledge and normative social stereotypes." (p.10)
- "Approximately 10 percent of terms were classified as deeply culture-rooted. Indeed, deeply culture-rooted terms and expressions do not make sense in other cultures; hence there are no 'ideal translations.'" (p.11)
- "We argue that for hate speech tasks, only specialists with relevant levels of education should be selected due to the high complexity of tasks that tackle highly politicized domains." (p.9)
- "Corroborating the initial premise that an expert annotated corpus and accurate definitions may provide better performance for automatic ML classifiers." (p.16)

## 13. UNKNOWN / not in extract
- Specific accounts of the 6 Brazilian politicians used for data collection
- Distribution of hate speech targets (9 categories) in HateBR 2.0
- Whether test/validation split is publicly provided or fixed
- Annotation guidelines document for annotators
- Inter-annotator agreement for the hate speech target classification (9-way) beyond the binary class
- Performance breakdown by hate speech category
- Details of cultural adaptation process for MOL translations
