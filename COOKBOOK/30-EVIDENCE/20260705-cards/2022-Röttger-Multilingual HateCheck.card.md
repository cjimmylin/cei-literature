---
stem: "2022-Röttger-Multilingual HateCheck"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, cultural-linguistic, validity-psychometrics, saturation-discrimination]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: 36582
dataset_construction: "hand-authored"
languages: ["ar", "nl", "fr", "de", "hi", "it", "zh", "pl", "pt", "es"]
models_tested: ["XLM-T", "XLM-R", "Perspective API"]
headline_numbers:
  - "36,582 total test cases across 10 languages (p.3)"
  - "34 functional tests grouped into 11 classes per language (p.3)"
  - "Best overall macro F1 per language: Mandarin 71.5, Italian 69.6, Spanish 69.5 (p.6)"
  - "Worst overall macro F1: Hindi 58.1, Arabic 59.4 (p.6)"
  - "Counter speech (F18/F19) accuracy as low as 9.6% (Arabic) (p.7)"
---
## 1. Gist
Multilingual HateCheck (MHC) extends the English HateCheck functional test suite for hate speech detection models to ten additional languages: Arabic, Dutch, French, German, Hindi, Italian, Mandarin, Polish, Portuguese, and Spanish. The paper introduces 36,582 hand-crafted test cases covering 34 functional tests in 11 classes, each with clear gold-standard labels. The core insight is that standard held-out test set evaluation paints an incomplete and potentially misleading picture of model quality—systematic gaps and biases in datasets mean models may learn overly simplistic decision rules. Functional testing reveals these weaknesses specifically. For values-alignment benchmarking, MHC is a direct template: it demonstrates how to test for fine-grained behavioral failures across protected groups and languages using contrastive test case design, prescriptive annotation, and template-based scalable generation.

## 2. Benchmark/eval design features
MHC tests distinct expressions of hate (F1–F8, F10–F12, F14–F15, F23–F34) and contrastive non-hate (F9, F13, F16–F22). Key distinctions:
- Explicit derogation (F1–F3) vs. implicit derogation (F4)
- Direct threat (F5) vs. normative threat (F6)
- Slurs (F7) vs. profanity (F8)
- Negated hate (F12) vs. negated non-hate (F13)—a strong contrastive pair
- Counter speech quoting hate (F18) vs. referencing hate (F19)
- Abuse at objects (F20), individuals (F21), non-protected groups (F22)
- Spelling variations in Latin script (F23–F27), Arabic-specific (F28–F31), Mandarin-specific (F32–F34)

Seven protected groups per language (with language-specific variation). Template-based generation allows equal coverage across groups and easy extension to new groups. The benchmark is binary: hateful vs. non-hateful per case, with each case belonging to exactly one functional test.

## 3. Task format & example item
Each test case is a short text statement with a gold label of hateful or non-hateful. Example:
- DE (German), F8 (hate with profanity, hateful): "F*ck alle Juden" (p.2)
- DE (German), F8 non-hateful profanity contrast: "Ich hatte noch nie so einen guten F*ck" (p.2)
- FR (French), F13 negated hate (non-hateful): "Je ne déteste pas les blacks." (p.7)
- Arabic, F19 (counter speech), non-hateful: accuracy only 9.6% (p.7)

## 4. Scoring / grading methodology
Primary metric: per-functionality accuracy (% correct on test cases for that functional test in that language), and macro F1 across hateful/non-hateful for each language. Evaluation reveals model weaknesses per function and per protected group separately. Annotation of gold labels is prescriptive (annotators instructed to follow clear guidelines, not personal views), validated by three native-speaking annotators per language (more than 120 annotators total). Cases where majority annotator labels differed from gold were flagged but not removed, as disagreements were attributed to annotator failure to follow guidelines rather than genuine ambiguity.

## 5. Dataset construction & provenance
36,582 test cases hand-crafted by native-speaking language experts with prior hate speech annotation experience. English HateCheck cases serve as starting points but experts adapted creatively for cultural and linguistic relevance. Template-based generation (replacing identity group [IDENT] and slur [SLR] tokens) accounts for 88.6% of cases; remaining are individually crafted. Polish has the most cases (3,815); Mandarin the least (3,378). Average case length: 8.5 words (std. dev. = 3.6). Dataset available on GitHub.

## 6. Validity evidence
Gold labels validated by three native-speaking annotators per language; more disagreement than original English HateCheck (where 99.4% confirmed gold). Upon review, most disagreement stemmed from annotators not following guidelines. All annotator labels published for filtering. The test suite diagnoses specific weaknesses not apparent from held-out test set performance—XTC achieves 84.7 macro F1 on Spanish held-out test set but much lower on MHC (69.5), demonstrating construct validity of MHC as revealing hidden failures.

## 7. Saturation / discrimination
MHC reveals clear differentiation across functional tests. Explicit hate (dehumanization F3, direct threats F5/F6) achieves 80-97% accuracy across languages. Implicit hate (F4) is harder: 52-85% range. Counter speech (F18/F19) is near floor: 10-65% accuracy. Negated hate (F13) is also low: 18-44%. This spread of 9.6%–97.9% accuracy across tests indicates excellent discrimination. Model performance on slurs (F7) is notably weak for Spanish (43.3%), Polish (51.1%), Italian (52.1%)—below random chance baseline of 50%.

## 8. Multiturn / agentic aspects
n/a — all test cases are single short statements with binary classification, no context beyond the individual document.

## 9. Key numbers
- Total test cases: 36,582 across 10 languages (p.3)
- Hateful cases: 25,511 (69.7%); non-hateful: 11,071 (30.3%) (p.3)
- Polish has most cases (3,815); Mandarin least (3,378) (p.3)
- 88.6% generated from templates (p.3)
- Average test case: 8.5 words (p.3)
- More than 120 annotators total (p.3)
- XTC on MHC best: Mandarin 71.5 macro F1; worst: Hindi 58.1 (p.6)
- Counter speech F19 accuracy: Arabic 9.6%, Hindi 13.7%, French 18.6% (p.6-7)
- XTC on Spanish held-out test: 84.7 macro F1 vs. 69.5 on MHC Spanish (p.4)
- F7 (slur) accuracy: Spanish 43.3%, Polish 51.1%, Italian 52.1% (p.7)
- French gay-targeted hate F1: 56.4 vs. women 70.9 (target bias, p.7)

## 10. Pitfalls & limitations
- Cases in different languages are not literal translations, so cross-language performance comparisons are not strictly like-for-like (p.8).
- MHC diagnoses weaknesses, not generalisable strengths—must be used to complement, not replace, held-out test set evaluation (p.7).
- Only 10 languages; hundreds remain uncovered (p.8).
- Test selection was partly informed by English-centric (Anglo) interviews; may miss language-specific hate forms not represented in English HateCheck (p.8).
- Languages vary within themselves across regions and sociodemographic groups; specific dialects chosen may not reflect full linguistic diversity (p.8).
- No context beyond individual documents; no multimodal content (p.7).
- The surprisingly good Mandarin performance may partly reflect Mandarin prevalence in XLM-R pretraining rather than genuine cross-lingual transfer (p.7).

## 11. Novel ideas worth stealing
- **Functional test taxonomy with contrastive non-hate cases**: the design of having a test for hate using profanity (F8) paired with a non-hateful profanity test (F9) is directly reusable. Any values benchmark should include contrastive cases that share surface features but differ in the value being tested.
- **Template-based generation for coverage equity**: using [IDENT] and [SLR] templates ensures equal numbers of test cases per protected group—a fairness-in-evaluation design principle for any group-level benchmark.
- **Prescriptive annotation with gold standard labels**: treating labels as ground truth to be followed rather than elicited personal opinions is a valuable choice when testing for behavior against a defined standard (rather than surveying diverse views).
- **Functional test → accuracy breakdown as the output format**: reporting per-function accuracy rather than aggregate F1 exposes model weaknesses that aggregate metrics hide—directly applicable to any benchmark that tests multiple behavioral dimensions.
- **Language-specific slur and spelling variation tests**: testing whether models handle evasion tactics (leet speak, missing characters, Arabizi) reveals robustness properties. A values benchmark could include paraphrase robustness tests along similar lines.
- **Target group × language matrix for bias detection**: testing the same template across all protected groups in the same language reveals differential protection—useful for any benchmark evaluating whether a model is equally aligned across demographic groups.

## 12. Notable quotes
- "Hate speech datasets are prone to exhibit systematic gaps and biases due to how they are sampled and annotated. Therefore, models may perform deceptively well by learning overly simplistic decision rules rather than encoding a generalisable understanding of the task." (p.1)
- "These contrasts make the test suites particularly challenging to models that rely on overly simplistic decision rules and thus enable more accurate evaluation of model functionalities." (p.2)
- "If XTC was used to moderate content, these critical weaknesses could cause serious harm. In particular, misclassifying counter speech risks undermining positive efforts to fight hate speech, and biased target coverage may create and entrench biases in the protections afforded to different groups." (p.7)
- "MHC diagnoses specific model weaknesses rather than generalisable model strengths, and should be used to complement rather than substitute evaluation on held-out test sets of real-world hate speech." (p.7)

## 13. UNKNOWN / not in extract
- Full list of slurs and protected group identity terms for each language (referenced as Appendix B).
- Complete list of annotators, their recruitment procedures and compensation (referenced as Appendix C).
- Per-annotator disaggregated label data (described as published on GitHub but not reproduced).
- Results for individual XLM-T models fine-tuned on single datasets vs. combined (referenced as Appendix F).
- Perspective API comparison details beyond the three languages where identity_attack is available (referenced as Appendix H).
