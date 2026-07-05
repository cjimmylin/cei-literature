---
stem: "2025-Liu-Diagnosing Moral Reasoning Acquisition in"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, validity-psychometrics, design-space]
task_format: "free-text"
scoring_type: "rubric"
dataset_size: 10000
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["Mistral-7B-v0.1", "Llama3-8B"]
headline_numbers:
  - "Moral foundation classification convergence fails even with 210,000 training samples while SST approaches 1.0 (p.3)"
  - "RLA correlation between representational similarity and prediction exceeds 0.9 across all conditions (p.7)"
  - "Full CLCA training raises Llama3.1 8B individual accuracy from 0.3162 to 0.3973 on WVS (p.8)"
---
## 1. Gist
This paper diagnoses why LLMs fail to genuinely acquire moral reasoning capabilities, introducing the concept of the "pragmatic dilemma." The authors argue that existing learning paradigms (fine-tuning on curated moral datasets) improve benchmark scores primarily through distributional semantic similarity between training and test items, not through genuine pragmatic understanding. Morality, unlike sentiment analysis, operates at the level of pragmatics — two superficially unrelated situations can share the same moral foundation — and current Transformer-based architectures cannot bridge this gap. The paper is important for values-alignment benchmarking because it provides a mechanistic explanation for why LLM moral performance improvements may be illusory and proposes a diagnostic algorithm (RLA) to detect when this is the case.

## 2. Benchmark/eval design features
This is a theory-and-diagnostic paper, not a benchmark proposal. The authors use three existing tasks as downstream evaluations of moral reasoning acquisition:
- **Moral Foundations classification**: classifying moral situations into foundations from MFT (Care, Fairness, Loyalty, Authority, Purity).
- **Rule of Thumb (RoT) generation**: generating a principle that explains why a situation is right or wrong.
- **Ethical judgment prediction**: predicting whether a situation is acceptable.

Two datasets are used: **SocialChem** (Forbes et al., 2020) and **MIC — Moral Integrity Corpus** (Ziems et al., 2022). Fine-tuning uses 10,000 samples with a single underlying moral foundation for analytical convenience.

Core claims: (1) Moral foundation classification exhibits a fundamental generalization failure not seen in semantics-level tasks (SST). (2) Performance gains in RoT generation and ethical judgment prediction arise from distributional semantic similarity, not pragmatic understanding. (3) The pragmatic dilemma is the primary bottleneck for moral reasoning acquisition.

## 3. Task format & example item
From the dataset annotation table (p.2):
> Situation: Reminding my coworker who crashed into my car to pay to get it repaired.
> Moral Foundation: Fairness.
> Rule of Thumb (RoT): If you crash into someone's car, you should pay for their repairs.
> (Ethical) Judgment: You should.

The generalization challenge is illustrated with two situations sharing the same foundation (authority-subversion) but with very different surface forms (p.3):
> Situation: Kicking a kid out of his birthday party.
> Situation: Not telling my mom I smoke weed.

## 4. Scoring / grading methodology
For **classification**: development accuracy over 10 fine-tuning epochs with BERT-base-uncased + classifier layer, compared against SST as a semantics baseline.

For **generation tasks** (RoT, judgment): BertScore, Rouge-1, Rouge-2, and Rouge-L metrics following Ziems et al. (2022). The paper emphasizes this is not aimed at state-of-the-art performance but at understanding generalization mechanisms.

The novel **Representational Likelihood Algorithm (RLA)** (p.6) correlates representational similarity (cosine similarity of hidden states from layer 15 onward) with prediction likelihood to identify "generalization-supportive" training samples. RLA results > 0.9 indicate that predictions depend on finding semantically similar training examples.

## 5. Dataset construction & provenance
- **SocialChem** (Forbes et al., 2020): crowdsourced situations with moral foundations and RoTs.
- **MIC** (Ziems et al., 2022): prompt-reply pairs treated as moral situations.
- Classification fine-tuning: 7,500 randomly sampled cases.
- RoT/judgment fine-tuning: 10,000 samples with single underlying moral foundation.
- Convergence analysis: training set sizes from 1,000 to 210,000 in steps of 2,000.
- No new dataset is introduced; analysis is conducted on existing resources.

## 6. Validity evidence
The paper's validity argument is mechanistic: the authors demonstrate (1) convergence failure in moral classification versus convergence success in SST (Figure 2, p.3); (2) RLA scores above 0.9 confirming the semantics-dependence hypothesis (Table 4, p.7); (3) qualitative analysis of top-10 generalization-supportive training samples showing they share high distributional similarity but not necessarily the same moral foundation (Figure 4, p.8). The comparison with SST as a controlled semantic baseline provides internal validity.

## 7. Saturation / discrimination
The core finding is that moral foundation classification does NOT saturate with more training data (development accuracy flat even with 210,000 samples), while SST saturates near 1.0 (p.3-4). This is the central evidence for the pragmatic dilemma. For RoT generation and judgment prediction, performance improves with more information (e.g., moral-rot outperforms rot in SocialChem, BertScore .836 vs .777; p.5) but the improvement mechanism remains within distributional semantics.

## 8. Multiturn / agentic aspects
n/a. All tasks are single-turn prediction or generation tasks.

## 9. Key numbers
- Best RoT generation strategy (moral-rot) achieves BertScore .836, Rouge1 .416 on SocialChem with Mistral (p.5)
- Baseline (rot) achieves BertScore .777, Rouge1 .229 on SocialChem with Mistral (p.5)
- RLA correlation values all exceed 0.9, with judg strategy very close to 1.0 across both models (p.7)
- Moral foundation convergence: SocialChem development accuracy shows NO improvement as training set grows from 1,000 to 210,000; SST approaches 1.0 (p.4)
- Perplexity on OpenWebText is higher for morality-tuned models than SST-tuned models (p.8-9), confirming moral fine-tuning impairs general language modeling

## 10. Pitfalls & limitations
- Paper focuses only on moral situations with a single underlying moral foundation; real situations often involve multiple foundations (acknowledged, p.9).
- No analysis of social sandbox or multi-round feedback systems (acknowledged, p.9).
- The analysis uses relatively small models (7B-8B); very large models may partially overcome the pragmatic dilemma through scale, making it hard to disentangle pragmatic reasoning from powerful distributional semantics (discussed in section 5, p.9).
- Datasets (SocialChem, MIC) are English-only; no cross-cultural or multilingual analysis.
- The paper does not propose a solution, only a diagnosis — it provides no path forward beyond noting that pragmatic inference frameworks built on semantic inferences might help.

## 11. Novel ideas worth stealing
- **The pragmatic dilemma diagnostic framework**: Use RLA to check whether a model's performance gains on a values/moral task come from genuine understanding or from finding semantically similar training examples. This could be applied to any values benchmark — if high RLA scores (>0.9) are found, the benchmark may be measuring surface pattern matching rather than value understanding.
- **Convergence curves as a test of benchmark validity**: Plotting development accuracy vs. training set size for moral/values tasks and comparing to a semantics-level task is a cheap and illuminating validity check. If accuracy doesn't converge toward 1.0, the benchmark is testing pragmatic understanding, which is genuinely hard.
- **Perplexity as a tax measure**: Fine-tuning for moral tasks increases perplexity on general text more than fine-tuning for semantic tasks. This could be used as a proxy measure of how much a values-alignment training procedure distorts the underlying model.
- **The situation/foundation mismatch framing**: Systematically constructing evaluation pairs where high distributional similarity does NOT imply the same moral foundation (and vice versa) would stress-test any values benchmark for surface-level pattern matching.
- **Intermediate chain prompting (moral-rot-judg)**: Forcing models to first predict the moral foundation, then generate a rule of thumb, before making a judgment improves performance. This structured chain-of-moral-reasoning format is a reusable design pattern for eliciting more deliberate ethical responses.

## 12. Notable quotes
- "Performance improvements follow a mechanism similar to that of semantic-level tasks, and therefore remain affected by the pragmatic nature of morals latent in discourse, a phenomenon we name the pragmatic dilemma." (p.1)
- "For SST, accuracy improves as the number of training samples increases, eventually stabilizing and approaching 1.0. In contrast, the development accuracies for moral foundation classification tasks show no improvement in SocialChem and only marginal gains in MIC." (p.4)
- "While the optimal fine-tuning strategies improve performance on both tasks, this improvement remains within the realm of distributional semantics, and the pragmatic dilemma persists." (p.8)
- "We argue that the study of moral reasoning acquisition should focus on smaller LLMs with 3B–8B parameters, as these models are less powerful than very large ones yet still exhibit satisfactory instruction-following capabilities. The powerful distributional semantics of large models make it difficult to disentangle whether performance gains stem from the proposed pragmatic inference framework or from learned statistical correlations." (p.9)

## 13. UNKNOWN / not in extract
- Exact dataset sizes and splits for SocialChem and MIC used in the experiments beyond the stated 10,000 sample subset.
- Whether the authors have released code or supplementary materials beyond what is cited.
- Results for the convergence analysis on the RoT generation task (only classification convergence is shown explicitly).
- Any human baseline performance numbers for the moral foundation classification or judgment tasks.
