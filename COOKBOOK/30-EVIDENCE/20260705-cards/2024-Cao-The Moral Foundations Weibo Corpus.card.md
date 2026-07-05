---
stem: "2024-Cao-The Moral Foundations Weibo Corpus"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, cultural-linguistic, validity-psychometrics, llm-judges-scoring]
task_format: "n/a"
scoring_type: "classifier"
dataset_size: 25671
dataset_construction: "crowdsourced"
languages: ["zh"]
models_tested: ["GPT-4", "Llama 3", "Qwen 2"]
headline_numbers:
  - "25,671 Chinese Weibo posts annotated across 7 thematic domains (p.3)"
  - "10 moral sentiment categories (5 MFT foundations × virtue/vice) plus Non-Moral (p.3)"
  - "Kappa ranges 0.45–0.92 across topics; PABAK 0.50–0.91 (p.4)"
  - "GPT-4 overall F1=0.60, Llama 3 F1=0.56, Qwen 2 F1=0.38 (p.5)"
  - "14,105 out of 25,671 posts labeled Non-Moral (p.5)"
---
## 1. Gist
The Moral Foundations Weibo Corpus (MFWC) is the first large-scale Chinese social media dataset annotated for moral sentiment using Moral Foundations Theory (MFT). It fills a critical gap: prior MFT corpora (MFTC on Twitter, MFR on Reddit) target English, yet China has ~1.09 billion social media users whose moral expression is shaped by different cultural norms (face-saving, indirect communication, content moderation). The corpus spans 7 politically and socially varied topics on Weibo, with each post annotated by 3 trained annotators across 10 MFT categories. For values-alignment benchmarking, MFWC matters because it provides ground-truth moral labels in Chinese that can be used to evaluate LLMs' cross-lingual moral understanding and to stress-test whether MFT categories transfer across cultures and moderation regimes.

## 2. Benchmark/eval design features
Dataset construction paper, not a benchmark. Core contributions: (1) 25,671 Weibo posts manually annotated with 10 MFT categories (Care, Harm, Fairness, Cheating, Loyalty, Betrayal, Authority, Subversion, Purity, Degradation) plus Non-Moral; (2) multi-label annotation design (overlapping labels permitted); (3) kappa and PABAK inter-rater reliability assessment; (4) LLM baseline classification using GPT-4, Llama 3, and Qwen 2 as zero-shot classifiers; (5) discussion of how Weibo's stringent content moderation affects the moral expression distribution compared to Western platforms.

## 3. Task format & example item
Each Weibo post is presented to annotators as a single text item; annotators assign one or more of the 11 labels (10 MFT categories + Non-Moral). For LLM evaluation, each post is a classification task. No verbatim example post is given in the extract. The annotation guide (Appendix A) gives the scheme: C1=Care, C2=Harm, F1=Fairness, F2=Cheating, L1=Loyalty, L2=Betrayal, A1=Authority, A2=Subversion, P1=Purity, P2=Degradation, NM=Non-Moral (p.12).

## 4. Scoring / grading methodology
Inter-annotator agreement: Fleiss kappa and PABAK test, reported per topic (Table 1). Final label assigned by majority vote (at least 2 of 3 annotators agree). LLM baseline performance reported as precision, recall, and F1 per foundation category and overall (Tables 3-13). Multi-label classification: both single-label and multi-label results reported.

## 5. Dataset construction & provenance
Posts scraped from Weibo across 7 topics: animal protection, real estate, people's livelihoods, volunteers, volunteer army, China-U.S. Prime Minister meeting (San Francisco), Hangzhou Asian Games. Selection criteria: moral salience, discussion intensity, coverage of sensitive/political content. Three undergraduate annotators trained on the MFT Coding Guide (adapted for Chinese context). Labels determined by majority vote; disagreements resolved through discussion. No personally identifiable information retained. Funded by Wenzhou-Kean University grant IRSPK2023005. License not explicitly stated in extract.

## 6. Validity evidence
Kappa varies widely by topic (0.45 for People's Livelihood to 0.92 for Protecting Animals, Table 1). High kappa topics are explicitly moral; low kappa topics contain more ambiguous general discourse. PABAK generally higher than kappa, adjusting for class imbalance. LLM baselines show GPT-4 consistently outperforms Llama 3 and Qwen 2 in F1, with GPT-4 best at balancing precision and recall. Construct validity is primarily asserted through adherence to Graham et al. (2013) MFT framework; no factor analysis or external criterion validation reported.

## 7. Saturation / discrimination
Strong class imbalance: 14,105 of 25,671 posts are Non-Moral (p.5). Among moral categories, Care/Harm (3,525) and Fairness/Cheating (2,572) dominate; Purity/Degradation (1,321) is rarest. This skew likely depresses model F1 on minority classes. The paper notes the imbalance as a limitation. Across discourse domains, performance varies substantially, suggesting domain-specific moral expression is a major discrimination challenge.

## 8. Multiturn / agentic aspects
n/a. Single-post annotation and classification.

## 9. Key numbers
- 25,671 Weibo posts total, 7 topics (p.3)
- 10 MFT moral categories + Non-Moral (p.3)
- 3 annotators per post, majority vote final label (p.3)
- Kappa range: 0.45 (People's Livelihood) to 0.92 (Protecting Animals) (p.4)
- PABAK range: 0.50 (People's Livelihood) to 0.91 (Volunteers) (p.4)
- 14,105 posts Non-Moral (54.9% of total) (p.5)
- GPT-4 overall F1=0.60, precision=0.65, recall=0.58 (p.5)
- Llama 3 overall F1=0.56, precision=0.60, recall=0.59 (p.5)
- Qwen 2 overall F1=0.38, precision=0.75, recall=0.32 (p.5)
- GPT-4 Care F1=0.74 (best single-class performance); Degradation F1=0.55 (worst) (p.6)

## 10. Pitfalls & limitations
- Heavy class imbalance toward Non-Moral may bias models and inflate macro F1 for dominant categories while depressing rare ones (p.8).
- Weibo's content moderation suppresses extreme moral expression, making MFWC unrepresentative of unmoderated Chinese discourse; cross-platform generalization is uncertain.
- Geographic and demographic coverage: Weibo users skew urban; rural moral expression not captured.
- MFT is a Western psychological framework; cross-cultural validity of the 5-foundation structure for Chinese social media is assumed but not tested.
- Only 7 topical domains; extra-domain generalization is explicitly flagged as difficult (p.3).
- No split details beyond train/test for the baseline experiments.
- LLM baselines are zero-shot; fine-tuned baseline would better characterize the corpus difficulty.

## 11. Novel ideas worth stealing
- **Politically diverse topic selection**: deliberately including sensitive/political topics (China-U.S. summit, volunteer army) alongside everyday topics (animals, real estate) to capture the full range of moral sentiment expression — a valuable design principle for any values benchmark that wants ecological validity.
- **Weibo content moderation as a natural variable**: the contrast between moderated (Weibo) and unmoderated (Twitter/Reddit) corpora is a natural experiment in how platform norms shape moral expression, exploitable for studying alignment under different speech norms.
- **Separate virtue/vice coding**: splitting each MFT foundation into its positive pole (virtue) and negative pole (vice) creates 10 labels rather than 5, capturing psychologically distinct states; this granularity could improve LLM alignment evaluation by distinguishing endorsing care from condemning harm.
- **PABAK alongside kappa**: reporting both corrects for class imbalance in reliability assessment — a methodological refinement worth adopting in any human-rated moral benchmark.
- **Multi-label design with primary domain identification**: allowing overlapping labels while attempting to identify the dominant foundation mirrors the genuine ambiguity of moral expression and provides richer signal than forced-choice single labels.

## 12. Notable quotes
- "In English, sentiments are usually expressed more directly... In contrast, Chinese culture is more concerned with maintaining face and social harmony and thus may be more subtle and euphemistic in its expression of sentiments." (p.1)
- "The stringent content moderation mechanisms on Weibo contribute to the distinctiveness of the MFWC. By providing a dataset characterized by more moderate expressions of moral sentiments, the MFWC offers a valuable contrast to other corpus." (p.2)
- "Low consensus among trained coders, therefore, is not merely a problem but an indication that the association might be subject to important boundary conditions, weak, or even illusory." (p.12)
- "Training coders to minimize disagreement does not change this reality but conceals it." (p.12)

## 13. UNKNOWN / not in extract
- Full text of the Moral Foundations Coding Guide for Chinese (Appendix A, only partially visible)
- Exact train/validation/test split sizes for the LLM experiments
- Whether the corpus is publicly released and under what license
- Performance of traditional ML baselines (logistic regression mentioned in discussion p.8 but results table not clearly shown for all categories in extract)
- Number of posts per topic in the breakdown (Table 2 shows moral category counts but not totals per topic summing correctly in the extract)
- Detailed breakdown of multi-label vs. single-label results
