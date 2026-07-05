# llm-judges-scoring — sub-dossier part 1/2

Scope: LLM-as-judge reliability and bias, rubric design, judge–human agreement, and alternative scoring methods for open-ended moral/values content. Drawn from 52 evidence cards (42 papers + 10 AI-lab cards).

## A. Synthesized claims

1. **Per-category / per-item rubrics beat a single global judge prompt by a large, measurable margin.** AIR-Bench derived category-specific GPT-4o judge prompts from 3 hand-written seeds scaled to 314 categories, lifting Cohen/Fleiss κ vs. humans from **0.69 (fixed prompt) to 0.86** (p.6) [2024-Zeng-AIR-Bench 2024]. The Arabic dataset likewise used 1–5 risk-specific binary criteria questions per risk area rather than a single "is this harmful?" prompt [2024-Ashraf-Arabic Dataset for LLM Safeguard Evaluation]. MedEthicsQA and MedES decompose each reference answer into checklist key-points, one binary rubric item each [2025-Wei-MedEthicsQA; 2026-Jin-MedES Chinese Medical Ethics Scenarios].

2. **A cheap purpose-built scorer trained on your own human labels can beat a general frontier LLM judge.** FLAMES-scorer reached **79.5% accuracy vs. GPT-4-as-judge's 61.3%** (best, 5-shot+explanation) on Chinese value-alignment scoring (p.7) [2023-Huang-Flames]. AlignMMBench's fine-tuned CritiqueVLM (ChatGLM3-6B) cut mean-absolute-error vs. humans by **34.8% relative to GPT-4** (p.2) [Zhipu AI-AlignMMBench_2406.09295]. MedES's LoRA-tuned QWQ-32B "guardian" reached **F1 > 0.96 on all six dimensions** (p.12) [2026-Jin-MedES Chinese Medical Ethics Scenarios].

3. **Raw accuracy / percentage-agreement is a misleading judge-quality metric under class imbalance; weighted-κ or AUPRC is required.** RTP-LX shows Llama Guard tops percentage-agreement yet collapses to near-last on weighted Cohen's κ — "a lazy learner could output always the same label and obtain a decent performance" (p.5); human IRR was **κw = 0.62 ± 0.2**, best model GPT-4 Turbo off by only 0.22 (p.9) [2024-Wynter-RTP-LX Can LLMs Evaluate Toxicity in Multilingual Scenarios]. HateDay uses average precision because hate prevalence is ~0.7% [2024-Tonneau-HateDay Insights from a Global Hate Speech Dataset Representative of]; the Jigsaw study reports AUC over accuracy for the same reason [2025-Jigsaw-Leveraging Machine Translation for Cross-Lingual Toxicity ...].

4. **Judges differ dramatically in willingness to grade harmful content, creating systematic blind spots.** In HELM Safety, GPT-4o judged **100%** of hard DBRX-HarmBench items while Claude 3.5 Sonnet **refused 27.2% (72.8% success)** — so GPT-4o was chosen as the safety judge (p.10–12); XML-like output delimiters reduced malformed judge outputs vs. JSON (p.11) [2024-Kaiyom-HELM Safety]. Constitutional Classifiers found the **evaluation rubric, not the classifier, was the weakest link**: "benign paraphrasing" and "length exploitation" gamed topic-coverage rubrics without real uplift (p.9, p.21) [Anthropic-Constitutional_Classifiers_2501.18837].

5. **For open-ended moral content there is no single correct answer, so grade the reasoning process against weighted atomic rubrics rather than the final verdict.** MoReBench scores reasoning traces against **23,018 expert-written signed weighted criteria** ({-3..+3}); inter-expert κ=0.75; it selected GPT-oss-120b as judge (F1 76.29%, **80× cheaper** than GPT-5-high's 77.46%) using the **minimum macro-F1 across categories** as a bias-robust lower bound (p.5) [2025-Chiu-MoReBench]. Neuman's five-dimension audit (Analytic Quality, Breadth, Depth, Consistency, Decisiveness) scores quality-of-reasoning where no ground truth exists [2025-Neuman-Auditing the Ethical Logic of Generative AI Models].

6. **Reference-based n-gram metrics (ROUGE/BLEU) falsely penalize valid but differently-worded moral answers; semantic metrics correlate better.** AISOCRATES got ROUGE-2 F1 of just **3.68** against expert answers despite being judged comparably multi-perspective by humans; BERTScore correlated best with human judgment, SacreBLEU inversely (p.5–6) [2023-Bang-Towards Answering Open-ended Ethical Quandary]. OpenAI's summarization work independently shows ROUGE fails to track RLHF quality gains (agreement drops ~57%→~50%) [OpenAI-learning-to-summarize-rlhf].

7. **LLM-judge scores are confounded by verbosity/detail and by the model's own family.** Neuman found audit scores "clearly tied to the level of detail models choose to provide," rewarding elaborate articulation, with values clustering near 100 (ceiling) [2025-Neuman-Auditing the Ethical Logic of Generative AI Models]. Learning-to-summarize and HelpSteer both document a length/verbosity bias in reward models and human raters (~5% of RLHF advantage vanishes after length control) [OpenAI-learning-to-summarize-rlhf; NVIDIA-HelpSteer_Multi-attribute_Helpfulness_Dataset]. Self-preference risk (OpenAI-family judge grading OpenAI models) is flagged in AIR-Bench, BBG, Flourishing, SGToxicGuard, and ELAB.

8. **Stated reasoning is often unfaithful to the actual decision, undermining any judge that reads a CoT as evidence.** Anthropic's faithfulness work shows early-answering AOC ranges 0.44 (AQuA) to 0.02 (ARC-Easy), and **larger models produce *less* faithful CoT** on 7/8 tasks (p.5–7) [Anthropic-Measuring_Faithfulness_in_CoT_Reasoning_2307.13702]. MORALLENS finds pre-decision reasoning is significantly more deontological than post-hoc explanation (CDGAP Δ=−0.178, p<0.001), i.e., justifications can be rationalizations [2025-Samway-Are Language Models Consequentialist or Deontological].

9. **Aggregate accuracy hides failure modes that only targeted probes reveal.** DweshVaani layers HateCheckHIn functional tests on top of F1 to expose over-triggering on neutral identity mentions [2025-search-DweshVaani An LLM for Detecting Religious]; TET cross-checks Perspective against Llama Guard and finds them agreeing on only **49/210** extreme-toxic (>0.9) responses [2024-Luong-Realistic Evaluation of Toxicity in Large].

10. **Interpretable, steerable scoring can decouple "what could happen" from "how much it matters."** SafetyAnalyst builds a harm-benefit tree and aggregates via **28 human-readable weights** fittable to a community's label distribution, reaching avg F1 0.81 vs. <0.72 for prior systems [2025-Li-SafetyAnalyst]. HelpSteer decomposes helpfulness into 5 anchored Likert attributes explaining 73% of variance [NVIDIA-HelpSteer_Multi-attribute_Helpfulness_Dataset].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2024-Zeng-AIR-Bench 2024 | Per-category judge prompts raise human-agreement κ from 0.69→0.86; 3-level 0/0.5/1 scoring. |
| 2023-Huang-Flames | Trained specified scorer 79.5% > GPT-4-judge 61.3%; report OOD-model generalization. |
| 2024-Kaiyom-HELM Safety | Claude judge refused 27.2% of hard harmful items (GPT-4o 100%); XML beats JSON for judge output. |
| 2024-Wynter-RTP-LX | Weighted-κ, not %-agreement, exposes lazy-learner judges under class imbalance (human κw 0.62). |
| 2025-Chiu-MoReBench | Grade weighted atomic reasoning rubrics; pick judge by min-across-category F1; κ=0.75. |
| 2024-Ashraf-Arabic Safeguard | Risk-specific 1–5 binary judge criteria; prioritize recall over precision (74.2% vs 54.8%) for safety. |
| 2025-Narnaware-SB-Bench | Multi-dimension ordinal judge (Fairness/Stereotype/Prior-Bias/Ambiguity/Faithfulness), κ=0.81, second judge cross-check. |
| 2025-Jin-Social Bias Benchmark (BBG) | MCQ bias scores do NOT predict generative bias; GPT-4 MRC evaluator 0.97 acc, κ=0.69 vs humans. |
| 2025-Wei-MedEthicsQA | Checklist-per-key-point LLM judge; validate judge via human "Reasonable Rate," not re-doing task. |
| 2026-Jin-MedES | Cross-family annotator/evaluator assignment to cut self-preference; guardian F1>0.96. |
| 2026-Shen-PsychEthicsBench | Cross-generator QC (Claude scores GPT-5 items); exclude refusal from ethicality score. |
| 2025-Samway-MORALLENS | Reasoning-order manipulation reveals post-hoc rationalization; judge F1=0.820. |
| 2025-Neuman-Auditing | Quality-of-reasoning rubric decoupled from correctness; run word-count control on judge. |
| 2025-Hilliard-Flourishing | Geometric-mean aggregation + negative-weighted rubric indicators (harmful = −100). |
| 2025-Trager-MFTCXplain | Score rationales with plausibility (Jaccard) + BERTScore; report human-human ceilings. |
| 2023-Bang-AISOCRATES | BERTScore > ROUGE/BLEU for open-ended moral QA; reference metrics falsely penalize valid answers. |
| 2024-Luong-TET | Two-evaluator cross-check (Perspective vs Llama Guard) exposes gross disagreement at the extreme. |
| 2025-Li-SafetyAnalyst | 28 interpretable, steerable aggregation weights fittable to a community's labels. |
| 2025-Machlovi-AI Moderation | Synthetic-vs-human generalization gap detects gamed/saturated safety benchmarks. |
| NVIDIA-HelpSteer | Attribute-decomposed Likert scoring with per-point anchors; 73% of helpfulness variance. |
| OpenAI-dpo | Validate LLM judge with 2 differently-worded prompts; agreement ≈ inter-human. |
| OpenAI-learning-to-summarize | Reward-model over-optimization (Goodhart); ROUGE fails to track quality. |
| Anthropic-Measuring_Faithfulness_CoT | Larger models produce less faithful CoT; AOC metric for post-hoc reasoning. |
| Anthropic-Constitutional_Classifiers | Rubric grading is exploitable (paraphrase/length); attackers hit the eval, not the model. |
| Google DeepMind-Gemini_2.5 | Two-tier eval: automated flags then manual review (most "regressions" were false positives). |
| Meta AI-CyberSecEval_3 | Calibrate LLM judge vs humans (r=0.89); propose consensus-of-judges. |
| Meta AI-Llama_Guard | Taxonomy-as-input judge; separate prompt vs response classification; AUPRC. |
| Zhipu AI-AlignMMBench | Fine-tuned CritiqueVLM judge beats GPT-4 (−34.8% MAE); prompt-rewrite stability score. |
| 2025-Andric-Do LLMs Walk Their Talk | Multi-method battery (IAT/behavioral/self-report) + Calibration Gap metric. |
| 2020-Mathew-HateXplain | Comprehensiveness/sufficiency faithfulness probes; rationale-as-eval-target. |
| 2025-Yuan-Probabilistic Aggregation | Truncated-normal EM to weight raters by reliability; Random01 robustness stress test. |
| 2025-Dubey-Moral Uncertainty | Multi-theory LLM "jury" (5 frameworks) fused via BJSD+DST rather than averaging. |
| 2025-LLMs-Leaderboard Ethical Biases | Oracle-per-template + counterfactual-consistency scoring; refusal-handling ambiguity. |
| 2025-Lan-McBE | Intrinsic (likelihood) vs comprehension probes give opposite "bigger=more biased" conclusions. |
| 2024-Tonneau-HateDay | Average precision under severe class imbalance; representative sampling collapses inflated scores. |
| 2025-search-DweshVaani | Functional black-box tests on top of F1; rationale-distillation *hurt*. |
| 2025-Farid-One Model Many Morals | LLM-judge annotation of CoT (framework + reasoning-phase tags); compliance rate reported with F1. |
| 2025-Neuman-Analyzing Six LLMs | Self-report probes (Haidt/Kohlberg) show severe order effects (99.6% conservative vs 99.3% liberal). |
| 2024-Cao-Moral Foundations Weibo | Report PABAK alongside κ to correct for class imbalance in reliability. |
| 2025-Bae-CharMoral | Context-ablation shows judge agreement 64%→92% as context added; κ=0.55 human. |
| 2025-Delaville-ToxiFrench | Human-agreement-derived ~90% performance ceiling; keep CoT but re-verify the label. |
| 2025-Derner-Gender Representation | LLM-as-annotator validated F-score vs human gold before scaling. |
| xAI-grok-4-1 | Thinking vs non-thinking variants have divergent safety/sycophancy profiles; track regressions. |

## C. Patterns & disagreements

**Convergence.** (1) Multiple independent teams find **rubric specificity is the single biggest lever** on judge–human agreement: AIR-Bench (0.69→0.86), Arabic risk-criteria, MedEthicsQA/MedES checklists, MoReBench atomic criteria, SB-Bench multi-dimension rubrics. (2) A recurring finding is that **a small fine-tuned judge beats a big general one** on the target distribution (FLAMES 79.5 vs 61.3; CritiqueVLM −34.8% MAE; MedES guardian) — and is far cheaper (MoReBench 80×). (3) Everyone who reports it flags **self-preference / same-family circularity** (AIR-Bench, BBG, Flourishing, ELAB, SGToxicGuard, MedES) and most propose a mitigation (cross-family assignment, second judge, human calibration). (4) **Class imbalance breaks accuracy-based judge validation**; RTP-LX, HateDay, Jigsaw, Cao, and Machlovi all move to κw/PABAK/AUPRC/AP.

**Disagreement.** (a) *Whether to trust CoT.* MORALLENS, Neuman, and Farid treat model reasoning traces as scorable signal, while Anthropic's faithfulness paper and ToxiFrench warn the stated reasoning is unfaithful/gameable — ToxiFrench's Dynamic Weighted Loss explicitly refuses to let the verdict be diluted by the reasoning, and "keeps the CoT but distrusts the label" [2025-Delaville-ToxiFrench]. (b) *Aggregation of moral pluralism.* Yuan aggregates via reliability-weighted truncated-normal EM; Dubey via Dempster-Shafer fusion of five framework-agents; Hilliard via geometric mean; SafetyAnalyst via fitted linear weights — no consensus on the right aggregator, and Li concedes summing harms/benefits is "not ultimately sufficient." (c) *Refusal handling.* PsychEthicsBench deliberately **excludes refusal from the ethicality score** (an inadequate refusal is unempathetic) [2026-Shen-PsychEthicsBench], whereas the Ethical-Biases leaderboard counts refusals as passes [2025-LLMs-A Leaderboard to Benchmark Ethical Biases in LLMs] and Flourishing treats *unjustified* refusal as anti-flourishing (−3) — three incompatible policies. (d) *Judge modality.* Machlovi and BBG show synthetic/LLM-generated test suites are easily gamed and MCQ bias scores don't transfer to generation, arguing against the very LLM-generated items that MedES, PsychEthicsBench, and AIR-Bench rely on.

## D. Exemplars & anti-patterns

**Best-designed for judge validity.** *AIR-Bench* [2024-Zeng] is the standout: it quantifies the per-category-rubric gain (0.69→0.86 κ), publishes 0/0.5/1 scoring, and grounds categories in citable regulation. *MoReBench* [2025-Chiu] is the exemplar for open-ended moral scoring — it (i) grades the process against signed weighted atomic rubrics, (ii) selects the judge by the *worst-case* per-category F1, (iii) runs discriminatory-power and neutrality meta-evals (equally-good traces for opposite conclusions score equally: t=−0.59, p=0.56), and (iv) bakes in a 500/500 public/private split. *RTP-LX* [2024-Wynter] models how to expose a lazy-learner judge that looks good on accuracy but fails on κw. *Gemini 2.5* [Google DeepMind] models the two-tier discipline: never trust automated safety scores without manual review — its apparent 2.5 "regressions" were mostly false positives.

**Anti-patterns.** *ELAB* [2025-Pourbahman] uses a single GPT-4o-mini that translates the data, labels it, and judges outputs, with **no human validation** and language-adherence folded into the alignment score — maximal circularity. The *Ethical-Biases leaderboard* [2025-LLMs] conflates "inconsistent across swapped communities" with "biased" and leaves refusal-handling unresolved on only ~300 thin tests. *ELAB* and *ProhibiBench*-style pipelines suffer catastrophic annotator attrition (SocialBench 150→17). More subtly, *Neuman's audits* [2025-Neuman-Auditing] reward verbosity and cluster near the 100 ceiling (GPT-4o auditing itself), and *Constitutional Classifiers* shows even a careful topic-coverage rubric was gamed by benign paraphrasing — a caution that any rubric judge must be adversarially tested against length/paraphrase exploits.

## E. Design lessons

1. **Write per-category (or per-item) judge rubrics, not one global prompt** — expect a step-change in human agreement (κ 0.69→0.86) [2024-Zeng-AIR-Bench 2024; 2024-Ashraf-Arabic Dataset]. Decompose each reference answer into binary checklist key-points [2025-Wei-MedEthicsQA; 2026-Jin-MedES].
2. **Report weighted-κ / AUPRC / PABAK, never bare accuracy, for judge validation under imbalance** — a constant-output "lazy learner" scores well on accuracy [2024-Wynter-RTP-LX; 2024-Tonneau-HateDay; 2024-Cao-Moral Foundations Weibo].
3. **Calibrate the judge against humans before trusting it, and validate the judge's *reasoning* (a "Reasonable Rate"), not just its label** [Meta AI-CyberSecEval_3 (r=0.89); 2025-Wei-MedEthicsQA; OpenAI-dpo]. Use ≥2 differently-worded judge prompts and confirm consistent rankings [OpenAI-dpo].
4. **Prefer/train a purpose-built scorer on your own human labels; report its OOD generalization** — it can beat a frontier judge at a fraction of cost [2023-Huang-Flames; Zhipu AI-AlignMMBench; 2026-Jin-MedES].
5. **Break circularity: cross-family judge assignment, a second independent judge, and cross-generator QC** [2026-Jin-MedES; 2025-Narnaware-SB-Bench; 2026-Shen-PsychEthicsBench]; run a consensus-of-judges to cut single-judge error [Meta AI-CyberSecEval_3; 2024-Luong-TET].
6. **For open-ended moral items with no ground truth, grade the reasoning process against signed weighted atomic rubrics; select the judge by minimum-across-category F1; run neutrality and discriminatory-power meta-evals** [2025-Chiu-MoReBench; 2025-Neuman-Auditing].
7. **Drop reference-based n-gram metrics for open-ended moral text; use semantic similarity or human/LLM rubric judging** [2023-Bang-AISOCRATES; OpenAI-learning-to-summarize].
8. **Control judge confounds: length/verbosity (report length-corrected scores) and self-preference** [2025-Neuman-Auditing; OpenAI-learning-to-summarize; NVIDIA-HelpSteer]; MoReBench-Hard's length correction is a template.
9. **Do not treat CoT as faithful evidence; separate the verdict from the reasoning and re-verify the verdict** [Anthropic-Measuring_Faithfulness_CoT; 2025-Delaville-ToxiFrench; 2025-Samway-MORALLENS].
10. **Adversarially test the rubric itself** (paraphrase, padding, refusal-as-evasion) — attackers target the weakest component, often the eval [Anthropic-Constitutional_Classifiers].
11. **Use interpretable, steerable, decomposed scoring** (harm-benefit trees with fittable weights; multi-attribute Likert with anchored points) so scores are auditable and re-weightable per community [2025-Li-SafetyAnalyst; NVIDIA-HelpSteer].
12. **Guard against benchmark saturation/gaming: report both an LLM-generated suite and human-curated data; if a 10% fine-tune closes the gap, the benchmark is too easy** [2025-Machlovi-AI Moderation]; verify MCQ scores transfer to generation before trusting them [2025-Jin-Social Bias Benchmark; 2025-Lan-McBE].
13. **Decide and state a refusal policy explicitly** — pass, penalize, or exclude — because it materially changes scores [2026-Shen-PsychEthicsBench; 2025-LLMs-Leaderboard; 2025-Hilliard-Flourishing].
14. **Use multi-method behavioral batteries and a Calibration Gap** (self-report minus behavior) to catch articulate-but-miscalibrated "virtue-signaling" models a single judge would miss [2025-Andric-Do LLMs Walk Their Talk].
15. **Report a human-inter-annotator performance ceiling** so judge/model scores are read relative to genuine subjectivity, not a fictional 1.0 [2025-Delaville-ToxiFrench; 2025-Trager-MFTCXplain].
