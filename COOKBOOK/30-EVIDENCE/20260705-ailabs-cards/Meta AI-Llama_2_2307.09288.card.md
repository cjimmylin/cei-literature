---
stem: "Meta AI-Llama_2_2307.09288"
company: "Meta AI"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, best-practices, llm-judges-scoring, agentic-multiturn]
headline_numbers:
  - "Llama 2-Chat 70B achieves 36% win rate and 31.5% tie rate vs. ChatGPT on helpfulness (p.19)"
  - "Over 1 million binary comparisons collected for Meta reward modeling data (p.10)"
  - "Red-teaming involved over 350 people across diverse expertise and demographics (p.28)"
  - "7B model safety robustness improved from γ=1.8 to γ=0.45 triggering violations per person per hour (p.29)"
  - "False refusal rate is approximately 0.05% on the helpfulness dataset even with 100% safety data (p.26)"
  - "Llama 2-Chat 70B toxicity drops to 0.01% on ToxiGen, down from 24.60% pretrained (p.31)"
  - "IRR on safety evaluations ranges 0.70–0.95 (Gwet's AC2), average 0.92 on Llama 2-Chat annotations (p.30)"
  - "Helpfulness RM achieves avg accuracy 70.6% across open-source preference benchmarks (p.12)"
  - "Total pretraining: 3.3M GPU hours, 539 tCO2eq emissions (all offset) (p.7)"
  - "SFT annotations stopped at 27,540 examples after quality plateau (p.9)"
---

## 1. Gist

Llama 2 (arXiv 2307.09288) is Meta AI's July 2023 open-source release of pretrained and instruction-fine-tuned LLMs at 7B, 13B, 34B, and 70B parameter scales. The fine-tuned variant, Llama 2-Chat, is optimized for dialogue and trained with a full RLHF pipeline comprising SFT, iterative reward modeling, rejection sampling, and PPO. The paper provides exceptional transparency into Meta's alignment methodology, including two separate reward models (helpfulness vs. safety), a novel Ghost Attention (GAtt) technique for multi-turn consistency, safety context distillation, red-teaming with 350+ people, and quantitative analyses of safety/helpfulness trade-offs. Evaluations cover academic benchmarks, human preference evaluations (~4,000 prompts), safety violation rates (~2,000 adversarial prompts), and inter-rater reliability metrics. Llama 2-Chat 70B is competitive with ChatGPT on human evaluations and outperforms open-source models significantly.

## 2. Alignment/values methods used

- **Supervised Fine-Tuning (SFT):** Bootstrapped from public instruction data, then shifted to 27,540 high-quality vendor-annotated examples covering helpfulness and safety behaviors.
- **RLHF with two separate reward models:** A helpfulness RM and a safety RM are trained independently to avoid tension between the two objectives.
- **Rejection Sampling fine-tuning:** Samples K outputs per prompt, selects best by reward score, fine-tunes on that. Applied from RLHF-V1 through V5 for the 70B model; smaller models distilled from its outputs.
- **PPO (Proximal Policy Optimization):** Combined with rejection sampling for RLHF-V5 and beyond.
- **Safety Context Distillation:** Generates responses with safety preprompt (e.g., "You are a safe and responsible assistant"), then fine-tunes model without the preprompt; only kept when it improves the safety RM score.
- **Ghost Attention (GAtt):** A novel technique that synthetically concatenates the system instruction to all user messages during fine-tuning, with loss zeroed on intermediate turns, to maintain multi-turn instruction consistency.
- **Iterative data collection:** Annotation performed in weekly batches; reward models retrained each iteration to stay on-distribution with evolving Llama 2-Chat outputs.

## 3. Values specification

Meta specifies values operationally through **annotation guidelines** rather than a formal constitution or model spec document. Key elements:

- **Helpfulness:** Defined as how well responses fulfill users' requests and provide requested information.
- **Safety:** Defined as avoiding unsafe content — explicitly separated from helpfulness to allow independent reward modeling and annotation.
- **Risk categories:** Three broad categories — illicit/criminal activities (terrorism, theft, human trafficking); hateful/harmful activities (defamation, self-harm, eating disorders, discrimination); and unqualified advice (medical, financial, legal).
- **Attack vectors:** Annotators instructed to probe via psychological manipulation, logic manipulation, syntactic manipulation (misspelling), semantic manipulation (metaphor), perspective manipulation (role-playing), and non-English languages.
- **Response best practices:** Address immediate safety concerns → explain potential risks → provide additional helpful information.
- **Negative UX categories:** Annotators trained to avoid failure modes documented in Appendix A.5.2.

No external constitution or published policy document is referenced; the guidelines are described as "iteratively refined" based on newly identified risks. The Responsible Use Guide is mentioned as a separate resource.

## 4. Safety & values evaluation methodology

- **Safety Human Evaluation:** ~2,000 adversarial prompts (1,351 single-turn, 623 multi-turn); rated by 3 annotators on a 5-point Likert scale (1=severe violation, 5=safe and helpful); majority vote determines violation status; IRR via Gwet's AC2 (range 0.70–0.95, avg 0.92 for Llama 2-Chat). (p.29–30)
- **Helpfulness Human Evaluation:** ~4,000 single and multi-turn prompts; 3 raters per comparison; 7-point Likert scale; Gwet's AC2 ranges 0.37–0.55 depending on closeness of model comparison. (p.18–19)
- **Reward model-based evaluation:** In-house safety and helpfulness RMs used as proxies for iterative selection; validated against human preference on held-out test sets; also compared against GPT-4 as judge.
- **GPT-4 as judge:** Used for win-rate evaluation between Llama 2-Chat and ChatGPT to reduce bias from in-house RM; order of responses randomly swapped. (p.18)
- **Automatic safety benchmarks (pretrained):** TruthfulQA (truthfulness+informativeness), ToxiGen (toxic generation %), BOLD (sentiment bias across demographics). (p.22–23)
- **Red Teaming:** 350+ people including cybersecurity experts, election fraud specialists, social media misinformation, legal, policy, civil rights, ethics, ML, creative writing; diverse socioeconomic/gender/ethnicity/racial backgrounds; probed for criminal planning, trafficking, substances, sexual content, unqualified advice, privacy violations, WMD capabilities. Robustness metric γ = avg violations per person per hour. (p.28–29)
- **False refusal measurement:** Classifier applied to helpfulness test set and a curated 210-sample borderline set. (p.26)
- **Dataset contamination analysis:** Reported in Appendix A.6. (p.8)

## 5. Benchmarks used or introduced

**Academic benchmarks (capabilities):**
- HumanEval, MBPP (code)
- PIQA, SIQA, HellaSwag, WinoGrande, ARC, OpenBookQA, CommonsenseQA (commonsense reasoning)
- NaturalQuestions, TriviaQA (world knowledge)
- SQuAD, QuAC, BoolQ (reading comprehension)
- GSM8K, MATH (math)
- MMLU (5-shot), BBH (3-shot), AGI Eval (3–5 shot) (aggregated)

**Safety benchmarks:**
- TruthfulQA — truthfulness and informativeness of generations
- ToxiGen — toxic/hate speech generation rate across demographic groups
- BOLD — sentiment bias in open-ended generations across demographic attributes (race, religion, gender)

**Preference/reward benchmarks:**
- Anthropic Helpful and Harmless datasets
- OpenAI Summarize, WebGPT
- StackExchange, Stanford SHP, Synthetic GPT-J (for reward model accuracy comparison)

**Human evaluation sets (internal):**
- Meta Helpfulness test set (~4,000 prompts)
- Meta Safety test set (~2,000 adversarial prompts)

**Tool use evaluation:**
- ASDiv, SVAMP, MAWPS (math with calculator access)

## 6. Agentic / multiturn evaluation aspects

- **Ghost Attention (GAtt):** Specifically designed and evaluated for multi-turn consistency — maintains adherence to system-level instructions across 20+ turns until context limit. Tested with persona constraints (Act as Napoleon, Speak in French, Hobbies constraints) not present in training data. (p.16–17)
- **Multi-turn vs. single-turn safety:** Multi-turn conversations are consistently more prone to unsafe responses across all models tested. Llama 2-Chat maintains lower violation rates on multi-turn than baselines. Falcon, which lacked multi-turn SFT data, performs particularly poorly on multi-turn. (p.30–31)
- **Multi-turn human evaluations:** Human safety evaluation set includes 623 multi-turn adversarial prompts. Human helpfulness evaluation covers both single and multi-turn prompts. (p.18, p.29)
- **Multi-turn memory failure identification:** Initial RLHF models tended to forget initial system instructions after a few turns — explicitly identified as a failure mode driving GAtt development. (p.16)

## 7. Key numbers

- Model sizes: 7B, 13B, 34B (unreleased), 70B parameters (p.4)
- Pretraining corpus: 2 trillion tokens (p.5)
- Context length: 4k tokens (doubled from Llama 1's 2k) (p.5)
- SFT annotations: 27,540 high-quality examples (p.9)
- Meta reward modeling comparisons: 1,418,091 (helpfulness + safety); total dataset 2,919,326 comparisons (p.11)
- Helpfulness RM accuracy: 70.6% avg across benchmarks; 63.2% on Meta Helpfulness test set (p.12)
- Safety RM accuracy: 64.3% avg across benchmarks; 64.5% on Meta Safety test set (p.12)
- RLHF iterations: V1–V5 (p.13)
- Red-team size: 350+ people (p.28)
- Robustness γ: 7B model improved from 1.8 → 0.45 violations/person/hour (p.29)
- Average 90% rejection rate (mitigated violations) across consecutive model versions (p.29)
- Llama 2-Chat 70B win rate vs. ChatGPT: 36% win, 31.5% tie (p.19)
- Llama 2-Chat 34B win rate vs. Falcon 40B and Vicuna-33B: >75% (p.18)
- Llama 2-Chat 7B win rate vs. MPT-7B-chat: 60% (p.18)
- TruthfulQA: Llama 2-Chat 70B = 64.14% (up from 50.18% pretrained) (p.31)
- ToxiGen: Llama 2-Chat all sizes effectively 0% (lowest of all models tested); 70B pretrained = 24.60% (p.31)
- IRR on safety Likert scale: 0.70–0.95 Gwet's AC2 (avg 0.92 for Llama 2-Chat) (p.30)
- IRR on helpfulness 7-point Likert: Gwet's AC2 = 0.37–0.55 (p.19)
- False refusal rate: ~0.05% on helpfulness dataset even at 100% safety data (p.26)
- Pretraining CO2: 539 tCO2eq, all offset (p.7)
- Training compute: 3,311,616 GPU hours total (p.7)
- Llama 2 70B vs. GPT-3.5 on MMLU: 68.9 vs. 70.0 (p.8)
- Pretraining data: 89.70% English, 8.38% unknown (includes code) (p.22)
- "christian" appears in 33.2% of training documents in religion category (p.21)
- "american" appears in 69.4% of nationality documents (p.21)

## 8. Findings relevant to values-benchmark design

**Helpfulness–safety tension is real but manageable:** Separate helpfulness and safety RMs outperform a single RM on each dimension, suggesting that conflating helpfulness and safety in a single eval can obscure both. For benchmark design, this implies that safety and helpfulness should be measured on separate scales and not aggregated.

**Reward model accuracy degrades on close comparisons:** The helpfulness RM achieves 89.9% accuracy when one response is "significantly better" but only 54.5% when responses are "negligibly better/unsure" — close to random. This has direct implications for benchmark discrimination: items where model differences are small produce unreliable human labels. Benchmark items need to be calibrated so that target behaviors are clearly distinguishable. (p.12)

**Reward model saturation not observed:** Scaling trends show that reward model accuracy continues to improve with more data and larger models without plateau, suggesting benchmark-quality coverage of preference space is still far from saturated. (p.13)

**Human evaluation IRR on helpfulness is low:** Gwet's AC2 of 0.37–0.55 on 7-point Likert helpfulness evaluation even with controlled guidelines and trained annotators. This is a major caveat for any benchmark relying on helpfulness judgments — subjectivity creates wide disagreement bands. Safety annotations show much higher agreement (0.70–0.95).

**Multi-turn consistently harder:** Every model tested shows higher violation rates on multi-turn prompts than single-turn. Yet most existing benchmarks are single-turn. Any values benchmark should include a multi-turn component.

**Benchmarks do not capture deployment reality:** "Benchmarks give a summary view... but they do not provide a fully comprehensive view of the impact the model may have on people or real-world outcomes; that would require study of end-to-end product deployments." (p.23) The BOLD dataset prompts (6–9 words) are acknowledged as unrealistic. Gap between benchmark performance and real-world safety is explicitly admitted.

**Western skew in training data:** "american" in 69.4% of nationality documents, "christian" in 33.2% of religion documents. Benchmarks designed on top of Llama 2 outputs or similar corpora will inherit these cultural biases.

**False refusal as an underreported dimension:** The false refusal rate (~0.05% on helpfulness, much higher on borderline prompts) is a key quality dimension not measured by standard safety benchmarks. A benchmark addressing values alignment needs to measure both over-refusal and under-refusal.

**GPT-4 vs. in-house RM as judges produce different win rates:** The in-house RM shows more favorable results for Llama 2-Chat than GPT-4 (>60% win rate by GPT-4 vs. higher by internal RM), illustrating how choice of judge affects benchmark conclusions. Third-party judges are more credible for cross-model comparisons.

## 9. Novel ideas worth stealing

1. **Separate reward models per dimension:** Designing two scoring rubrics — one for helpfulness, one for safety — and scoring them independently before any aggregation reveals trade-offs that a combined score hides. Applied to benchmark design: report helpfulness and safety/values-adherence as separate axes.

2. **Robustness metric γ (violations per person per hour):** A task-completion rate for adversarial evaluators is a cleaner operationalization of safety robustness than violation-rate-on-a-fixed-set, because it normalizes for evaluator effort. Could be adapted as a "red-team yield" metric in benchmarks.

3. **Multi-turn GAtt consistency test:** A principled evaluation of whether a model maintains a system-level value constraint across 20+ dialogue turns could be a standalone benchmark dimension — especially relevant for persona/value drift in agentic settings.

4. **Borderline prompt set as a calibration tool:** The 210-sample borderline dataset (prompts that look adversarial but are legitimate) is a precision–recall calibration instrument for over-refusal. Any values benchmark should include analogous items that test false positive rate as well as false negative rate.

5. **Granular preference-rating to test discriminability:** Using a 4-point scale (significantly better → negligibly better) and reporting reward model accuracy separately per level reveals where evaluation signal breaks down. Benchmark designers can use this approach to audit whether their items have sufficient signal-to-noise at the intended discrimination level.

6. **Context distillation with answer templates per risk category:** For targeted values evals, providing category-specific response templates (first refute misinformation, then provide evidence, then offer resources) makes evaluation criteria more concrete and reproducible than general guidelines.

7. **Iterative annotation batches with model updates:** Running annotation in weekly batches, retraining reward models, then using new model to sample next batch ensures annotators are always evaluating the current distribution. For benchmark development, this suggests adaptive sampling procedures rather than fixed static prompt sets.

## 10. Notable quotes

"Benchmarks give a summary view of model capabilities and behaviors that allow us to understand general patterns in the model, but they do not provide a fully comprehensive view of the impact the model may have on people or real-world outcomes; that would require study of end-to-end product deployments." (p.23)

"We observe that our reward models overall are well calibrated with our human preference annotations... the accuracy is superior for the 'significantly better' test set and degrades gradually as comparison pairs become more similar... It is expected that learning to model human preferences becomes challenging when deciding between two similar model responses, due to annotator subjectivity and their reliance on nuanced details that may differentiate responses." (p.12–13)

"Safety is inherently a long-tail problem, where the challenge comes from a small number of very specific cases." (p.24)

"Supervised data may no longer be the gold standard, and this evolving circumstance compels a re-evaluation of the concept of 'supervision.'" (p.32)

## 11. UNKNOWN / not in extract

- Details of the Responsible Use Guide (separate document, URL provided but not in extract)
- Exact prompts in the borderline test set (Appendix Table 41 referenced but not fully reproduced in extract)
- Llama 2-Chat 34B release rationale specifics beyond "lack of time to sufficiently red team" (p.4)
- Full breakdown of BOLD sentiment scores per religion subgroup beyond what is in extract (tables 45–48 partially in extract but truncated)
- Specifics of the "negative UX categories" instructed to annotators (Appendix A.5.2 referenced but not fully quoted)
- Details on whether external audits or third-party safety evaluators (beyond red-teamers) were used
- Contamination analysis details (Appendix A.6 referenced on p.8 but not read in detail)
