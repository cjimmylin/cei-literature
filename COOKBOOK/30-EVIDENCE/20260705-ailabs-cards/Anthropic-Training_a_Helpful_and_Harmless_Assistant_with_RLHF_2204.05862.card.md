---
stem: "Anthropic-Training_a_Helpful_and_Harmless_Assistant_with_RLHF_2204.05862"
company: "Anthropic"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, best-practices, validity-psychometrics, normative-ethics]
headline_numbers:
  - "Online HH RLHF model preferred over professional writers by crowdworkers ~57% of the time (p.7)"
  - "PM accuracy on HHH evaluation reaches 86%, above the reported mean human accuracy of 75% (p.14)"
  - "Crowdworker-researcher agreement on labels approximately 63%, lower than comparable work (p.10)"
  - "Training 100% on helpfulness data causes harmlessness test accuracy to fall far below random chance, and vice versa (p.24)"
  - "With only 10 harmful examples, OOD detection achieves AUROC of 0.94±0.02 for 52B model (p.28)"
  - "Core base dataset: 44k helpfulness comparisons + 42k red-teaming comparisons; RS dataset: 52k helpfulness + 2k red-teaming (p.12)"
  - "Iterated online RLHF updates models on roughly weekly cadence over ~5 weeks (p.12)"
---

## 1. Gist

This foundational Anthropic paper (2022) describes the full pipeline for training a helpful and harmless (HH) assistant using preference modeling and reinforcement learning from human feedback (RLHF). It covers: human feedback data collection (via crowdworkers on MTurk and Upwork), preference model (PM) training and scaling, RLHF fine-tuning with PPO, robustness analysis, iterated online training, compatibility with specialized skills (coding, summarization), out-of-distribution (OOD) detection for harmful requests, and qualitative evaluation. The paper demonstrates that RLHF improves helpfulness and harmlessness simultaneously for large models (13B+), and that alignment training does not tax capabilities—in fact it improves NLP benchmark performance for large models. It also identifies and quantifies the fundamental tension between helpfulness and harmlessness as competing objectives, and proposes iterated online training as a remedy for preference model degradation at high reward scores. This paper is essentially the methodological backbone of Anthropic's early alignment work.

## 2. Alignment/values methods used

- **RLHF (PPO)**: Primary method. Preference models assign rewards based on human-expressed preferences; PPO optimizes the policy against these rewards with a KL penalty term (λ_KL = 0.001) to prevent excessive deviation from the initial policy.
- **Preference Modeling (PM)**: Trained on comparison data (two model responses, crowdworker selects the better one). Separate helpfulness and harmlessness PMs; mixed PMs used for HH.
- **Preference Model Pretraining (PMP)**: Language models are first pretrained as preference models before fine-tuning on HF datasets, improving sample efficiency.
- **Context Distillation**: HHH (helpful, honest, harmless) dialogues are distilled into the model via context, producing the initial policy before RLHF.
- **Iterated Online RLHF**: Policy is deployed to crowdworkers, new comparison data is collected, and the PM and policy are retrained on a weekly cadence, progressively filling out the upper tail of the quality distribution.
- **Rejection Sampling (RS)**: k=16 samples generated from context-distilled model, best selected by PM, used as an intermediate data collection step.
- **OOD Detection (Simplified Relative Mahalanobis distance)**: Activation-based anomaly detection used to flag harmful/out-of-distribution requests without any labeled harmful examples.

## 3. Values specification

The paper deliberately avoids prescribing what "helpful" and "harmless" mean, instead letting crowdworkers operationalize these concepts through their preferences. The values targeted are:

- **Helpfulness**: Assisting with text-based tasks (answering questions, writing, editing, discussing plans).
- **Harmlessness**: Not assisting with harmful goals (bank robbery, toxic language, etc.). Defined implicitly by red-teamers choosing the more harmful of two responses.
- **Honesty**: Explicitly mentioned as a third goal but not the primary focus; RLHF improves honesty as a side effect (crowdworkers told "lying isn't helpful").

The "HHH" (Helpful, Honest, Harmless) framing from prior Anthropic work [Askell et al., 2021] provides the overall value framework, but no formal constitution, policy document, or model spec is described in this paper. Values are distributed across: (1) the crowdworker feedback data, (2) the HHH evaluation benchmark, and (3) the PALMS sensitive questions used for qualitative review.

## 4. Safety & values evaluation methodology

**Human Evaluation:**
- Crowdworker preference comparisons using Elo scoring (Section 2.4).
- Comparison to professional writers (hired on Upwork): crowdworkers preferred the HH model ~57% of the time (p.7).
- 17 samples generated per prompt; median sample selected by online HH PM to mitigate cherry-picking (p.7).

**Static Alignment Evaluations:**
- **HHH Evaluation** [Askell et al., 2021, BIG-Bench]: Tests whether PMs and models prefer helpful, honest, harmless responses. PM achieves 86% accuracy vs. reported mean human of 75% (p.14).
- **TruthfulQA (MC1)**: Tests honesty/calibration of RLHF models; large models improve, effect increases with scale (p.22).
- **BBQ-Lite** (from BIG-Bench): Stereotype bias across 9 dimensions; authors note limited conclusions can be drawn as plain LMs appear unbiased on this metric, suspecting measurement limitations (p.23).
- **Bot Adversarial Dialogues (BAD)** [Xu et al., 2020]: External validation that PMs correctly score harmful AI utterances lower.
- **Gender bias evaluation**: PM score differences across matched gender terms; variation within gender appears as large as across genders, suggesting limited PM gender bias (p.15–16).
- **Sentiment toward racial and religious groups**: RLHF improves positive sentiment toward all groups; bias across groups less clear (p.23).

**NLP Capability Evaluations:**
- MMLU, Lambada, HellaSwag, OpenBookQA, ARC-Easy, ARC-Challenge, TriviaQA (zero-shot and few-shot).
- HumanEval for code (pass@k).

**Robustness Study:**
- 50/50 dataset split, train separate PMs on each half, train RL policy against train PM while evaluating with test PM (p.17–18).
- Red-teaming for harmlessness via crowdworkers (adversarial data collection).

## 5. Benchmarks used or introduced

| Benchmark | Type | What it Measures |
|-----------|------|-----------------|
| **HHH Evaluation** [Askell et al., 2021 / BIG-Bench] | Static alignment | Model/PM preference for helpful, honest, harmless responses |
| **TruthfulQA (MC1)** [Lin et al., 2021] | Static alignment | Model honesty/calibration |
| **BBQ-Lite** [Parrish et al., 2021 / BIG-Bench] | Bias | Stereotype bias across 9 protected categories |
| **Bot Adversarial Dialogues (BAD)** [Xu et al., 2020] | Harm | Whether PMs correctly score harmful AI utterances |
| **MMLU** | NLP capability | Multitask language understanding |
| **Lambada, HellaSwag, OpenBookQA, ARC, TriviaQA** | NLP capability | Commonsense, reading comprehension, trivia |
| **HumanEval (CodeX)** [Chen et al., 2021] | Code | Python function completion, pass@k |
| **PALMS sensitive questions** [Solaiman & Dennison, 2021] | Qualitative | Model behavior on sensitive topics |
| **Elo scoring** (crowdworker preferences) | Human eval | Relative model quality as judged by crowdworkers |

## 6. Agentic / multiturn evaluation aspects

The paper uses a multi-turn dialogue format throughout: crowdworkers have open-ended conversations with models, making preference selections at each conversational step (not just the first). PM accuracy is studied as a function of conversational turn (Figure 8): accuracy is highest at turn 1 and approximately constant thereafter (p.13). The paper provides several 2-turn dialogue examples (Section 6.3). However, there is no evaluation of extended agentic tasks, tool use, or autonomous task completion. The longest dialogues shown are 2-turn. The paper explicitly notes that multi-turn dialogue evaluation is a gap: "we likely need to build more subtle and comprehensive evaluations that include multi-turn dialogue, as this is an area where humans will likely use the models, and it's also a place where it's inherently more difficult to measure performance against subtle objectives such as bias and fairness" (p.35).

## 7. Key numbers

- **Dataset sizes**: 44k helpfulness + 42k red-teaming comparisons (base); 52k helpfulness + 2k red-teaming (RS); 22k helpfulness (online) (p.12)
- **Model sizes**: 7 models from 13M to 52B parameters (geometric series, ~4× increments) (p.13)
- **RLHF prompt dataset**: 137k crowdworker prompts + 369k model-generated prompts (p.17)
- **RLHF robustness**: training becomes gradually less robust after ~150k training samples (p.17)
- **HHH eval PM accuracy**: 86% for static 52B PM, vs. mean human 75% (p.14)
- **Crowdworker-researcher agreement**: ~63%, lower than comparable work (p.10–11)
- **PM calibration on HH mixture**: slightly under-confident; helpfulness-only PMs are very well calibrated (p.13–14)
- **Helpfulness vs. harmlessness tension**: training 100% on one causes test accuracy on the other to fall far below chance (p.24–25); weighting λ=10 harmlessness loss causes 7.4% helpfulness drop for 13M model vs. only 1.5% for 52B (p.25)
- **OOD detection AUROC** (no outlier exposure, 52B, best layer): ~0.85; with 10 harmful examples (outlier exposure): 0.94±0.02 (p.28)
- **RLHF vs. human writers (helpfulness Elo)**: crowdworkers prefer HH online model ~57%, helpful-only model ~51% over writers (p.29)
- **Alignment bonus threshold**: RLHF improves zero-shot NLP for ~13B and 52B models; smaller models pay alignment tax (p.6, p.22)
- **KL-reward relation**: approximately linear between reward and √DKL during RLHF training (p.18)
- **Online training iteration cadence**: roughly weekly over ~5 weeks (p.12)

## 8. Findings relevant to values-benchmark design

**Tension between helpfulness and harmlessness as anti-correlated objectives**: PMs trained exclusively on one distribution perform worse than chance on the other. This is fundamental to benchmark design: a single score combining helpfulness and harmlessness will mask their trade-off. Separate benchmarks or Pareto frontier analysis are needed (p.24–25).

**Data distribution determines what RLHF learns to optimize**: The paper's red-teaming procedure (crowdworkers choose the MORE harmful response) caused models to overfit to simple refusal behavior rather than learning "hostage negotiation"—nuanced, helpful responses to harmful requests. The eval gap: models had no signal for what to do, only what not to do. This is a structural benchmark design issue: if benchmark data only labels extremes, fine-grained distinctions are unlearnable (p.19–20).

**Preference model saturation at high scores**: PMs become less calibrated and less robust as RLHF policies achieve higher reward. This creates a ceiling effect in preference-based evaluation: once models exceed training distribution quality, PM scores are unreliable. Static benchmarks suffer the same problem if they are too easy for SOTA models (p.13–14, p.17).

**Evaluation distribution shift for RLHF models**: RLHF models have lower-entropy output distributions, making them less likely to produce gendered terms in fill-in-the-blank bias tasks. Standard bias evaluations become unreliable because the prompts are off-distribution for the RLHF model. Evaluations must be re-designed for instruction-following models (p.22–23).

**Crowdworker-researcher agreement is low (~63%)**: Human labeling for alignment exhibits moderate inter-annotator disagreement. PMs trained to predict crowdworker behavior can actually agree more with researchers than crowdworkers agree with researchers (p.14).

**The lab explicitly admits it has not addressed worst-case robustness**: The paper focuses on average-case behavior. Bad tails in model behavior are acknowledged as a gap. Values benchmarks should explicitly probe worst-case behavior, not just average-case metrics (p.35).

## 9. Novel ideas worth stealing

1. **Elo scoring for model comparison**: Use Elo ratings (standard chess tournament scoring) to produce relative model quality rankings from pairwise crowdworker preference data. This converts binary win/loss data into a continuous scale and handles transitivity automatically. Applicable to any values-alignment benchmark that uses pairwise human preference.

2. **Iterated online benchmark updating**: As models improve, benchmark datasets become stale. The online RLHF procedure (collect data from best current model, retrain evaluator, repeat) is a model for keeping benchmarks current. A "living benchmark" with periodic updates tied to model deployment cycles would address saturation.

3. **Separate helpfulness and harmlessness evaluations**: Never conflate into a single score. Report on a 2D Pareto frontier. Any benchmark for a "helpful + safe" value set should measure both separately and quantify trade-offs.

4. **Median sample as qualitative evaluation standard**: Generate 17 samples per prompt, select median by PM score. This controls for cherry-picking without requiring expensive adversarial prompting. Applicable to qualitative showcase in any benchmark paper.

5. **Train/test PM split for reward hacking detection**: Split preference data 50/50, train separate PMs on each half, evaluate RL policy against both. Divergence between train and test PM scores indicates the policy is exploiting the reward model rather than genuinely improving. Analogous to held-out test set in supervised learning—apply this to LLM-judge-based benchmark evaluation.

6. **OOD detection as a complement to preference modeling**: Mahalanobis-distance-based OOD detection on activations can flag harmful inputs with very few labeled examples (10 suffice for 0.94 AUROC). This is useful for benchmark filtering and flagging.

7. **"Alignment data as public good" framing**: The paper argues for an independent organization to produce high-quality, publicly available alignment preference data with a broad governance structure. For benchmark design, this implies: governance structures for annotation, public data release, and separation from commercial data pipelines.

## 10. Notable quotes

- "Our goal is not to define or prescribe what 'helpful' and 'harmless' mean but to evaluate the effectiveness of our training techniques, so for the most part we simply let our crowdworkers interpret these concepts as they see fit." (p.4)

- "Helpfulness and harmlessness often stand in opposition to each other. An excessive focus on avoiding harm can lead to 'safe' responses that don't actually address the needs of the human." (p.4)

- "We harbor a general concern that perhaps our techniques only render models aligned 'on the surface', and that they still harbor harmful biases or other tendencies that may surface in more subtle contexts." (p.35)

- "Without a clear specification for the format and type of 'alignment data' most relevant for AI training, it has been difficult for anyone other than researchers to gather the information needed to train safe and beneficial AI systems." (p.36)

## 11. UNKNOWN / not in extract

- Full details of the appendices (A–E) including PM architecture, detailed RL hyperparameters, full NLP evaluation figures, code model RLHF prompts, and crowdworker interface details are described but the full extract was read only through page ~37 of 74 pages. Key quantitative results in the appendix (Figures 28–40) are referenced but their full content is not included here.
- The identity and demographic composition of crowdworkers is not disclosed beyond "master-qualified US-based MTurk workers" and some Upwork workers.
- Specific constitution or policy document underlying the HHH framework is referenced as [Askell et al., 2021] but not reproduced here.
- Whether Constitutional AI (published after this paper) supersedes the HH RLHF approach is outside this extract's scope.
- Honesty evaluation methodology beyond TruthfulQA is not developed in this paper; authors note this as a limitation and future direction.
