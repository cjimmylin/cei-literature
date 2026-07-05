---
stem: "2024-Kajiwara-Hate Speech Dataset Catalogue hatespeechdata"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [design-space, validity-psychometrics, normative-ethics]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 14640
dataset_construction: "crowdsourced"
languages: ["en"]
models_tested: ["BERT (base uncased)"]
headline_numbers:
  - "65% of OLID training offensive messages contain explicit markers of offensiveness (p.7)"
  - "59% of OLID test offensive messages are explicit (p.7)"
  - "Fleiss' Kappa = 0.61 after first annotation round; 0.86 after discussion and second round (p.7)"
  - "AbuseEval training set: 2,023 explicit, 726 implicit, 1,651 not abusive (of 4,400 offensive + 8,840 not) (p.8)"
  - "Cross-domain: AbuseEval-trained BERT would rank 2nd in HatEval competition (F1 +0.063 vs OffensEval) (p.9)"
---
## 1. Gist
This 2020 LREC paper (Caselli, Basile, Mitrovic, Kartoziya, Granitzer) introduces AbuseEval v1.0, a reannotation of the OLID/OffensEval dataset that adds an explicit/implicit dimension to offensive language labeling. The authors argue that existing offensive language datasets are heavily skewed toward explicitly offensive messages (those containing profanities or slurs) and fail to capture implicitly abusive language (sarcasm, irony, metonymy, rhetorical questions). They propose a three-way annotation scheme (explicit abuse, implicit abuse, not abusive) and apply it to OLID/OffensEval, creating AbuseEval v1.0. The paper is relevant to values-alignment benchmarking as it provides a systematic analysis of annotation bias in hate speech datasets and demonstrates that "abusive" and "offensive" are empirically distinct constructs—an important distinction for calibrating content safety evaluations.

## 2. Benchmark/eval design features
Core theoretical distinction: offensive language ≠ abusive language. Offensive language captures messages that may cause displeasure (including profanity in any context). Abusive language requires: (a) explicit targeting of an individual or group, (b) intention to debase/insult. The AbuseEval annotation scheme: (a) Explicit abuse—surface evidence via profanity, performatives, imperatives, negatively-loaded adjectives; (b) Implicit abuse—no surface evidence, abuse inferred through sarcasm, irony, metonymy, litotes, euphemism; (c) Not abusive—not interpretable as abusive without context, or truly not abusive.

Key analytical contribution: dictionary-based offensive language detection achieves near-SOTA performance on OLID (suggesting it is heavily keyword-dependent), while AbuseEval requires more flexible language modeling. The cross-domain experiment demonstrates that AbuseEval captures abusive language phenomena beyond what OLID's offensive language annotation captures.

## 3. Task format & example item
Three-way classification of tweets: Explicit (EXP) / Implicit (IMP) / Not Abusive (NOTABU).

Example of explicit abuse (p.7): "@USER @USER @USER He. Is. A. Sociopath. They are incapable of feeling empathy. Period." → EXP

Example of implicit abuse (p.7): "4 out of 10 British people are basically full-on racists. 4 out of 10 voters vote for the Conservatives. Coincidence!???!???" → IMP (rhetorical device)

Example of not abusive (p.7): "@USER I miss you bitch!!" → NOTABU (ambiguous without context—could be affectionate address in-community)

Annotation protocol requires annotators to first decide if message is an utterance (intelligible, complete), then check for quotes, then determine explicit/implicit/not-abusive.

## 4. Scoring / grading methodology
Annotation: Fleiss' Kappa inter-annotator agreement. First round: Kappa = 0.61 (substantial). After discussion and harmonization: Kappa = 0.86 (near-perfect). Three annotators (all paper authors); disagreements resolved through discussion. Classification experiments use fine-tuned BERT with macro-averaged F1. Binary task (ABU vs. NOT) and three-way task (EXP/IMP/NOTABU) reported separately. Cross-domain: trained on OffensEval or AbuseEval, tested on HatEval English test set.

## 5. Dataset construction & provenance
AbuseEval v1.0 is built on OLID/OffensEval (Zampieri et al. 2019), a collection of English tweets with 13,240 training and 860 test items. Only the offensive (OFF) messages were re-annotated for explicit/implicit/not-abusive: 4,400 training OFF + 240 test OFF. Non-offensive (NOT) messages (8,840 train, 620 test) were mapped to NOTABU without re-annotation. Total AbuseEval: 13,240 train + 860 test. Annotation by the three paper co-authors (not crowd workers). Data available at github.com/tommasoc80/AbuseEval. Source data: OLID/OffensEval collected from Twitter using keyword approach (political and non-political keywords), with 67% non-offensive in the original.

## 6. Validity evidence
Inter-annotator agreement: Fleiss' Kappa = 0.61 (first round), 0.86 (post-discussion). Three sources of disagreement identified: (1) subjective sensitivity of offensive language audiences, (2) "borderline" profanity/slur perception, (3) figurative language (irony, sarcasm) requiring unpacking. Urban Dictionary used as objective reference for slang/abbreviation disambiguation. Classification experiments validate the resource: BERT trained on AbuseEval achieves F1 = 0.716 on abusive vs. not (vs. 0.657 for dictionary approach), and outperforms OffensEval training by +0.063 F1 on HatEval cross-domain test.

## 7. Saturation / discrimination
The implicit class is extremely difficult: BERT F1 for IMP = 0.24 on OffensEval three-way, 0.23 on AbuseEval three-way. Explicit class more stable: F1 ≈ 0.64. Saturation not a concern here—the implicit class represents a hard open problem. Cross-domain generalization: AbuseEval training gives significantly better cross-domain performance (HatEval F1 = 0.591) than OffensEval (F1 = 0.528), suggesting AbuseEval better captures domain-general abusive language properties.

## 8. Multiturn / agentic aspects
Not applicable. Single-message classification of Twitter posts.

## 9. Key numbers
- OLID training: 4,400 OFF + 8,840 NOT = 13,240 (Table 1, p.2)
- OLID test: 240 OFF + 620 NOT = 860 (Table 1, p.2)
- AbuseEval train: 2,023 EXP + 726 IMP + 1,651 NOTABU (+ 8,840 NOT→NOTABU) (Table 5, p.8)
- AbuseEval test: 106 EXP + 72 IMP + 62 NOTABU (+ 620 NOT→NOTABU) (Table 5, p.8)
- 65% of OLID training OFF messages contain explicit markers (p.7)
- 59% of OLID test OFF messages are explicit (p.7)
- Dictionary F1 on OffensEval: 0.722 (macro); BERT: 0.828 (Table 3, p.5)
- AbuseEval BERT binary ABU vs NOT: F1 = 0.716 ± 0.034 (Table 6, p.8)
- AbuseEval BERT three-way: IMP F1 = 0.234 ± 0.086 (Table 7, p.9)
- Cross-domain: OffensEval → HatEval F1 = 0.528; AbuseEval → HatEval F1 = 0.591 (+0.063) (Table 8, p.9)
- AbuseEval would rank 2nd (vs 7th for vanilla BERT on HatEval out of 71 systems) (p.9)
- Fleiss' Kappa round 1: 0.61; round 2: 0.86 (p.7)
- 573-word Duluth blacklist in analysis; 861-word extended offensive dictionary used (p.5)
- About 7% of training set: abusive but also annotated as untargeted (contradicting their own definition) (p.8)

## 10. Pitfalls & limitations
- Only three annotators, all paper authors—no external validation or diverse demographics
- After discussion, second-round Kappa = 0.86 may reflect convergence pressure rather than genuine agreement
- The three-way scheme conflates two distinct things: "is this abusive?" + "how is the abuse expressed?" which can complicate downstream learning
- NOTABU in AbuseEval includes both genuinely non-abusive messages AND messages that are simply uninterpretable without context—this heterogeneity in the negative class complicates training
- Binary gender/group identity not addressed; the paper focuses on directness/explicitness rather than target group
- Limited to English Twitter data; cultural context for implicit abuse varies greatly across languages and cultures
- The "not abusive without context" category creates irresolvable annotation uncertainty for many real-world cases

## 11. Novel ideas worth stealing
1. **Explicit vs. implicit as a benchmark dimension**: The explicit/implicit distinction is highly relevant for values-alignment benchmarks. Implicit harmful content (sarcasm, dog whistles, coded language) is where AI safety evaluations most often fail. Building separate test sets for implicit vs. explicit harmful content provides more diagnostic information.
2. **Contextual interpretability as a label**: Making "not interpretable without context" an explicit label category (rather than forcing annotators to guess) is honest about epistemic uncertainty and reduces annotation noise—a design principle applicable to any ambiguous classification task.
3. **Cross-domain transfer as benchmark validation**: The paper's approach of validating AbuseEval by testing cross-domain generalization (trained on AbuseEval, tested on HatEval) is a rigorous way to demonstrate that a new annotation scheme captures generalizable phenomena rather than dataset-specific artifacts.
4. **Dictionary-based upper-bound analysis**: Computing the theoretical maximum performance of a perfect profanity dictionary reveals how keyword-dependent a dataset is. Datasets with high dictionary ceilings are potentially measuring surface-form rather than meaning—a useful diagnostic for any benchmark.
5. **Urban Dictionary as non-annotator knowledge base**: Using a crowd-sourced dictionary for slang disambiguation during annotation reduces annotator cultural background bias and enables more consistent annotation of in-group language—directly applicable to any hate speech annotation involving slang.

## 12. Notable quotes
- "We claim that one shortcoming of the OLID/OffensEval data set is the annotation of every message containing a profanity as offensive. This is particularly dangerous as it may lead to misrepresentations of communities." (p.10)
- "Data sets for the detection of abusive language phenomena must be contextually grounded: the annotation of a message and of its abusiveness must be conducted with respect to the context of occurrence rather than in isolation." (p.10)
- "The use of keywords to retrieve potentially abusive messages should be deprecated, and we should collect data from 'hateful' users." (p.10)
- "The prediction of the Implicit class (IMP) is challenging. The limited amount of training data... is certainly a reason. However we also think that this is an indications of the complexity of the phenomenon." (p.9)

## 13. UNKNOWN / not in extract
- Note: The stem "2024-Kajiwara-Hate Speech Dataset Catalogue hatespeechdata" suggests this may be a different paper (possibly a catalogue paper by Kajiwara), but the extract contains the Caselli et al. 2020 paper "I Feel Offended, Don't Be Abusive!" about AbuseEval v1.0. The card describes what is actually in the extract.
- Full annotation guidelines decision tree (referenced as bit.ly/2PsWRJJ)
- Complete data statement (#BenderRule appendix only partially described)
- Annotation inter-rater statistics beyond the 100-message sample study
- Whether AbuseEval has been used as a benchmark in subsequent shared tasks
- License for the AbuseEval dataset
- Results breakdown by protected class or topic
