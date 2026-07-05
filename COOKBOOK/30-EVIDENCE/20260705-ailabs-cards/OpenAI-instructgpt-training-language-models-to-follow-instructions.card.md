---
stem: "OpenAI-instructgpt-training-language-models-to-follow-instructions"
company: "OpenAI"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, normative-ethics, pluralism-aggregation, validity-psychometrics]
headline_numbers:
  - "1.3B InstructGPT preferred over 175B GPT-3 despite 100x fewer parameters (p.1)"
  - "175B InstructGPT preferred over 175B GPT-3 85±3% of the time (p.3)"
  - "InstructGPT generates truthful+informative answers ~twice as often as GPT-3 on TruthfulQA (p.3)"
  - "InstructGPT generates ~25% fewer toxic outputs than GPT-3 when prompted to be respectful (p.3)"
  - "Inter-annotator agreement: training labelers 72.6±1.5%, held-out labelers 77.3±1.3% (p.8)"
  - "SFT dataset: ~13k training prompts; RM dataset: ~33k training prompts; PPO dataset: ~31k (p.7)"
  - "Hallucination rate: InstructGPT 21% vs GPT-3 41% on closed-domain tasks (p.3)"
  - "175B PPO-ptx requires 60 petaflops/s-days vs 3,640 for GPT-3 pretraining (p.17)"
  - "Labeler demographics: 75% under 35, mostly US or Southeast Asian (p.37)"
  - "Dataset is ~96% English (p.35)"
---

## 1. Gist

InstructGPT (Ouyang et al., 2022; arXiv:2203.02155) is the foundational paper establishing Reinforcement Learning from Human Feedback (RLHF) as the dominant technique for aligning large language models with human intentions. OpenAI fine-tuned GPT-3 using a three-step pipeline: supervised fine-tuning (SFT) on labeler-written demonstrations, reward model (RM) training on ranked comparisons, and PPO reinforcement learning against the reward model. The key empirical finding is striking: 1.3B InstructGPT outputs were preferred to 175B GPT-3 outputs despite having 100x fewer parameters. This paper also contains unusually candid methodological and normative self-reflection — particularly in Section 5.2 ("Who are we aligning to?") — that is directly relevant to values-benchmark design. The paper introduces and operationalizes the Helpful-Honest-Harmless (HHH) framework and surfaces core tensions including alignment tax, reward hacking, labeler non-representativeness, and the multi-stakeholder problem in defining "human values."

## 2. Alignment/values methods used

- **RLHF with PPO**: Core alignment method. Three stages: (1) SFT on human demonstrations, (2) reward model trained on K-way ranked comparisons, (3) PPO optimization with KL penalty from SFT model (p.8-9)
- **PPO-ptx**: RLHF with mixed pretraining gradients to mitigate alignment tax. Adds γ×log(π_RL(x)) pretraining objective to PPO objective (p.9)
- **KL penalty**: Per-token KL divergence from the SFT model added to reward during RL, with coefficient β, to prevent over-optimization of the reward model (p.9)
- **SFT baseline**: Supervised fine-tuning on labeler-written demonstrations of desired behavior (p.8)
- **Human preference comparisons**: Labelers rank K=4–9 model outputs per prompt; all C(K,2) pairs used as training signal for RM to avoid overfitting (p.8)

## 3. Values specification

The paper operationalizes values through the **Helpful-Honest-Harmless (HHH)** framework, attributed to Askell et al. (2021):
- **Helpful**: Follow user's instructions and infer intent, including implicit intent (p.10)
- **Honest/Truthful**: Statements about the world should be true; the paper acknowledges true "honesty" (comparing outputs to beliefs) is unmeasurable in black-box models, so they proxy with truthfulness metrics (p.10)
- **Harmless**: No physical, psychological, social, institutional, or environmental harm (p.10)

**Priority ordering (for evaluation):** Harmless and truthful > helpful; except when output is much more helpful, only slightly less truthful/harmless, and not in a high-stakes domain (p.37, labeling instructions excerpt).

**Alignment target explicitly bounded:** The paper candidly states: "This procedure aligns the behavior of GPT-3 to the stated preferences of a specific group of people (mostly our labelers and researchers), rather than any broader notion of 'human values'" (p.2). The labelers are primarily English-speaking people from the United States or Southeast Asia hired via Upwork or Scale AI (p.18).

**No formal constitution or model spec cited** — values are operationalized through labeler instructions and researcher judgment.

## 4. Safety & values evaluation methodology

**Human preference evaluations (main):**
- Labelers rate InstructGPT vs. SFT 175B baseline on held-out API prompts
- Winrate comparisons on both InstructGPT prompt distribution and GPT-3 prompt distribution
- 1-7 Likert scale overall quality ratings
- Metadata labels: instruction-following, hallucinations, appropriateness as customer assistant, explicit constraint satisfaction, sexual/violent content, denigration of protected class, gives harmful advice, expresses opinion/moral judgment (Table 3, p.9)

**Automatic evaluations:**
- TruthfulQA (Lin et al., 2021): measures truthfulness and informativeness
- RealToxicityPrompts + Perspective API: automatic toxicity scoring
- Winogender and CrowS-Pairs: bias evaluation (InstructGPT does not improve over GPT-3)
- Standard NLP benchmarks: SQuAD, DROP, HellaSwag, WMT translation — used to detect alignment tax

**Labeler selection with screening test:**
- Agreement on sensitive speech flagging (75% threshold)
- Agreement on output rankings
- Sensitive demonstration writing score (6/7 Likert)
- Self-assessed ability to identify sensitive speech across cultural groups (p.36)

**Held-out labeler generalization test:** Separate labelers (no training data) used to test whether preferences generalize. 5-fold cross-validation on reward model with accuracy 69.6±0.9% on held-out labelers vs 72.4±0.4% on training labelers (p.12).

## 5. Benchmarks used or introduced

**Introduced/used for alignment evaluation:**
- Human preference winrate against 175B SFT model (main metric for alignment quality)
- Labeler metadata collection framework (12 binary/Likert labels per output, Table 3)
- Closed-domain hallucination rate (did the model make up information not in the input?)

**External benchmarks used:**
- TruthfulQA: truthfulness and informativeness (roughly doubled GPT-3's score)
- RealToxicityPrompts: automatic toxicity (Perspective API) + human toxicity evaluation
- Winogender: gender coreference bias
- CrowS-Pairs: social bias in masked language models
- SQuAD, DROP, HellaSwag, WMT 2015 French-English: NLP performance for alignment tax measurement
- FLAN and T0 datasets: comparator baselines for instruction fine-tuning

## 6. Agentic / multiturn evaluation aspects

This paper does not focus on agentic or multiturn scenarios. The evaluation is primarily single-turn prompt-response evaluation. Chat use cases represent only 8.4% of the training distribution (Table 1, p.6). The paper acknowledges that the evaluation may not generalize to inputs where "humans disagree about the desired behavior" (p.4) and that the real-world harm of outputs depends on deployment context, which labelers cannot assess from the Playground interface (p.10).

## 7. Key numbers

- 1.3B InstructGPT preferred over 175B GPT-3: evidence for RLHF efficiency over scale (p.1-3)
- 175B InstructGPT vs 175B GPT-3 winrate: 85±3% (p.3); vs few-shot GPT-3: 71±4% (p.3)
- InstructGPT vs FLAN: 78±4% winrate (p.12-13); vs T0: 79±4% (p.12-13)
- TruthfulQA: InstructGPT roughly twice as truthful+informative as GPT-3 (p.3)
- Hallucination rate on closed-domain tasks: InstructGPT 21% vs GPT-3 41% (p.3)
- Toxicity reduction: ~25% fewer toxic outputs when prompted to be respectful (p.3)
- Inter-annotator agreement: 72.6±1.5% (training) and 77.3±1.3% (held-out) (p.8)
- RM cross-validation accuracy: 69.6±0.9% on held-out labeler group (p.12)
- SFT dataset: ~13k training prompts (11,295 labeler + 1,430 customer); RM dataset: ~33k; PPO: ~31k (p.7, Table 6)
- Training compute: SFT 175B = 4.9 petaflops/s-days; PPO-ptx 175B = 60 petaflops/s-days; GPT-3 = 3,640 (p.17)
- 40 labeler contractors hired via Upwork and Scale AI (p.2)
- Dataset: ~96% English (p.35)
- Labeler demographics: 75% under 35, 50% male, 44% female, 6% nonbinary/other; 53% Southeast Asian, 32% White, 16% Latinx (p.37, Table 12)
- Use-case distribution: 45.6% generation, 12.4% open QA, 11.2% brainstorming, 8.4% chat (Table 1)
- Dataset 7.9% ambiguous prompts, 6.9% sensitive content (RM training set, Table 7)
- Model sizes evaluated: 1.3B, 6B, 175B parameters (p.3)

## 8. Findings relevant to values-benchmark design

**Alignment tax problem:**
RLHF fine-tuning reduces performance on public NLP benchmarks (SQuAD, DROP, HellaSwag, WMT) — termed the "alignment tax." The PPO-ptx fix (mixing pretraining gradients) largely mitigates this (p.3, p.17). For values-benchmark design: RLHF optimization can degrade some capabilities while improving others, so multi-dimensional evaluation is required.

**Public NLP datasets not representative of actual use:**
FLAN and T0 (fine-tuned on public NLP datasets) perform worse than InstructGPT on the actual API distribution (p.12-13). About 57% of real use is open-ended generation and brainstorming, while classification+QA (the typical NLP benchmark fare) is only ~18% (p.12). This means that standard NLP benchmarks substantially mismatch real deployment distribution — directly relevant for values benchmarks that rely on closed-form tasks.

**InstructGPT does NOT improve bias:**
Despite improvements in helpfulness and truthfulness, InstructGPT shows no improvement over GPT-3 on Winogender and CrowS-Pairs bias benchmarks (p.3). This is a notable ceiling/gap finding: RLHF toward HHH does not automatically address distributional bias.

**Reward hacking and over-hedging:**
InstructGPT exhibits "over-hedging" — giving long equivocating answers to simple questions because labelers were instructed to reward epistemic humility (p.16). This is a direct example of reward model artifacts producing unintended behavior. Values benchmarks need to separately assess calibrated uncertainty vs. epistemic cowardice.

**Alignment to a specific group, not "human values":**
The paper explicitly states InstructGPT aligns to a specific reference group (labelers + OpenAI researchers + API customers), not human values in general. The "Who are we aligning to?" discussion (Section 5.2, p.18) is one of the earliest and most candid industry acknowledgments of the pluralism-aggregation problem.

**Discrepancy between training and evaluation labeler priorities:**
During training, labelers prioritized helpfulness > truthfulness/harmlessness. During evaluation, they prioritized truthfulness/harmlessness > helpfulness. This deliberate mismatch means training labels and evaluation labels encode different values — a methodological issue worth tracking in any values evaluation design (p.7-8, appendix).

**Generalization of instruction-following beyond training distribution:**
InstructGPT generalizes to non-English languages and code QA despite near-zero representation in training data, suggesting alignment methods can generalize the "following instructions" concept itself (p.4, 15). Relevant for evaluating cultural/linguistic generalization.

## 9. Novel ideas worth stealing

1. **Explicit discussion of "who are we aligning to?"** The Section 5.2 framework (four caveats about whose preferences are being aligned: labelers, researchers, customers, broader stakeholders) is directly applicable to values-benchmark design. Any values benchmark should have an explicit "alignment to whom" section identifying whose normative preferences ground the benchmark.

2. **Multi-level metadata labeling schema**: The 12-category metadata schema (Table 3) with a mix of binary labels (hallucination, sexual content, denigrates protected class, gives harmful advice) and Likert scores is a practical template for fine-grained annotation of values-relevant dimensions.

3. **Held-out labeler generalization test**: Testing whether reward model preferences generalize to labelers who produced none of the training data is a strong form of construct validation. Values benchmarks should test whether their human ground truth generalizes across labeler groups.

4. **Alignment tax measurement protocol**: Systematically tracking performance on standard capability benchmarks before and after alignment fine-tuning is a best practice that values benchmark designers should adopt — to verify that improved alignment doesn't come with capability degradation on tasks the benchmark purports to assess.

5. **Measuring reward model accuracy via cross-validation**: Using 5-fold cross-validation to estimate how well the RM predicts held-out labeler preferences (69.6±0.9%) is a concrete psychometric validity check — analogous to inter-rater reliability but for the learned reward model. Values benchmarks using LLM judges should apply similar checks.

6. **Explicit treatment of labeler vs. user vs. stakeholder misalignment**: The paper's discussion that labelers don't see deployment context, that API customers may not optimize for end-user well-being, and that API users are not representative of all affected populations is a rich framework for thinking about construct validity in values evaluation.

## 10. Notable quotes

"This procedure aligns the behavior of GPT-3 to the stated preferences of a specific group of people (mostly our labelers and researchers), rather than any broader notion of 'human values'; we discuss this further in Section 5.2." (p.2)

"In this paper we align to the inferred user intention for simplicity, but more research is required in this area. Indeed, one of the biggest open questions is how to design an alignment process that is transparent, that meaningfully represents the people impacted by the technology, and that synthesizes peoples' values in a way that achieves broad consensus amongst many groups." (p.20)

"Our labelers are not the users who generated the prompts, there could be a divergence between what a user actually intended and what the labeler thought was intended from only reading the prompt." (p.10)

"We suspect that behavior (2) [over-hedging] emerges partly because we instruct labelers to reward epistemic humility; thus, they may tend to reward outputs that hedge, and this gets picked up by our reward model." (p.16-17)

## 11. UNKNOWN / not in extract

- The full text of labeling instructions for RM training (shown only partially in Figure 10) was promised as "full instructions here" but the full appendix text was not visible in the extract — only the excerpt is available
- Details of the reward model cross-validation experiment beyond what is summarized on p.12
- Results of further experiments on refusals (mentioned as future work in appendix B.2)
- Details of whether/how labeler instructions evolved over time and the effect of those changes on labeled data are only partially described
- Full details of bias results on Winogender/CrowS-Pairs (extended results referenced in appendix E but not available in this extract)
- Pages 43-68 (approximately) contain extended experimental details, plots, and additional tables not extracted
