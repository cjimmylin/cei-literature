---
stem: "OpenAI-deep-research-system-card-february-2025"
company: "OpenAI"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, agentic-multiturn, contamination-robustness, llm-judges-scoring]
headline_numbers:
  - "Deep research classified overall medium risk in Preparedness Framework, including medium risk for cybersecurity (first time any model rated medium for cyber) (p.11)"
  - "Post-mitigation deep research (without browsing): 82% high school, 55% collegiate, 47% professional CTFs (p.14)"
  - "Post-mitigation deep research SWE-bench Verified: 68%, a 20% uplift over o1 (p.29)"
  - "Prompt injection attack success rate reduced from 3–10% (pre-mitigation) to 0–0.51% (post-mitigation) (p.5)"
  - "PersonQA hallucination evaluation: deep research accuracy 0.86 vs. GPT-4o 0.50, hallucination rate 0.13 vs. GPT-4o 0.30 (p.10)"
  - "ChangeMyView persuasion: all models including deep research score 80–90th percentile vs. humans (p.25)"
  - "Privacy eval: post-mitigation deep research 0.96 on golden examples vs. 0.69 without rails (p.8)"
  - "SWE-Lancer: deep research (browsing) earns $87,708 of $453,800 maximum; solves 53% of IC SWE tasks (p.34)"
---

## 1. Gist

The Deep Research System Card (February 2025) describes OpenAI's safety evaluation and deployment process for Deep Research, an agentic capability built on an early version of o3 that conducts multi-step web research. Unlike prior chat models, Deep Research can browse the internet, execute Python code, read files, and synthesize multi-source reports with citations. The system card documents safety evaluations across six risk areas (prompt injection, disallowed content, privacy, code execution, bias, hallucination) plus the four Preparedness Framework domains (cybersecurity, CBRN, persuasion, model autonomy). Deep Research received a medium risk rating across all four Preparedness categories—a first for cybersecurity. The card also raises important methodological challenges for evaluating internet-browsing agents, particularly the contamination problem: agentic models can retrieve benchmark answers from the internet, artificially inflating evaluation scores.

## 2. Alignment/values methods used

- **Reinforcement learning on browsing tasks**: Trained on curated browsing datasets with both auto-gradable (ground-truth) and rubric-graded open-ended tasks; chain-of-thought model used as grader during RL training (p.2).
- **Safety dataset transfer from o1**: Reused existing o1 safety training datasets plus new browsing-specific safety datasets (p.2).
- **Deliberative alignment**: o-series technique that trains models to explicitly reason through safety policy before responding; improves robustness to jailbreaks and policy compliance. Also introduced a new refusal behavior for political persuasion tasks (p.12).
- **Prompt injection safety training**: New safety data and system-level mitigations specifically for prompt injection robustness (p.4).
- **Privacy-specific policy refresh**: Updated model policies for personal data, new safety training data, and a system-level blocklist for personal information (p.8).
- Post-training safety procedures reward bias-reducing refusals and factuality (p.9–10).

## 3. Values specification

OpenAI does not publish a values constitution for Deep Research. Values are operationalized through:
- **Preparedness Framework**: A living document mapping capability thresholds to risk levels (Low, Medium, High, Critical) for cybersecurity, CBRN, persuasion, and model autonomy. Only models with post-mitigation ≤ Medium can be deployed (p.10–11).
- **Usage Policies**: Referenced as the basis for "disallowed content" evaluations; political persuasion specifically added as a new refusal category (p.12).
- **Safety Advisory Group**: Reviews evaluation results and determines risk levels; provides governance oversight (p.11).
- **Privacy principles**: Personal information that is available online is still refused; distinction between public/private person applies (p.8–9).
- No explicit published model spec or constitutional document referenced in this card.

## 4. Safety & values evaluation methodology

- **External red teaming**: Contracted team (Lysios LLC + ~30 named individuals) tested personal information/privacy, disallowed content, regulated advice, dangerous advice, risky advice, prompt injections, jailbreaks (p.3).
- **Preparedness evaluations**: Multi-domain capability benchmarks (CTF for cyber, bio/chem for CBRN, ChangeMyView/MakeMePay/MakeMeSay for persuasion, SWE-bench/MLE-bench for autonomy). Both pre- and post-mitigation models tested (p.10–34).
- **Benchmark contamination analysis**: Novel methodology for assessing whether browsing-enabled models retrieved answers from the internet during evaluations. CTF trajectories manually inspected; contaminated rollouts excluded. Results presented with and without contaminated rollouts (p.11–15).
- **LLM-as-grader**: Chain-of-thought o1-preview model used to auto-grade long-form biorisk responses; calibrated against biosecurity expert feedback (p.18).
- **Human evaluation**: Targeted red-teaming for risky advice; human rankers compared model safety across pairs of models (p.7).
- **BBQ evaluation**: Tests bias/stereotyping in ambiguous vs. unambiguous QA contexts (p.9).
- **Third-party partners**: Gryphon Scientific for CBRN evaluation; SecureBio for virology; Signature Science for novelty probing; MIT Stanton Nuclear Security Fellow for nuclear evals (p.20–24).
- **Biosecurity expert baselining**: 19 PhD scientists with >1 year wet lab experience provided expert baseline on ProtocolQA (p.20).

## 5. Benchmarks used or introduced

- **CTF Challenges** (high school, collegiate, professional): Vulnerability identification/exploitation; pass@12 over 16 rollouts; 100+ curated challenges (p.13–16)
- **Long-form Biological Risk Questions** (NVIDIA-internal + Gryphon Scientific): Rubric-graded questions across 5 bio-threat creation stages; autograded by LLM with expert calibration (p.18)
- **Multimodal Troubleshooting Virology** (SecureBio): 350 virology troubleshooting MCQs (p.19)
- **BioLP-Bench**: 800 wet lab protocol questions (published; contaminated) (p.19)
- **ProtocolQA Open-Ended**: 108 MCQs converted to open-ended; expert baseline from 19 PhDs (p.20)
- **Tacit Knowledge and Troubleshooting** (Gryphon Scientific): 5-stage biothreat tacit knowledge MCQs; fully uncontaminated (p.20)
- **WMDP Biology**: 1,520 of 3,668 biology MCQs from WMDP; published/contaminated (p.21)
- **Contextual Nuclear Knowledge**: 222 MCQs on nuclear engineering; fully uncontaminated (p.23)
- **ChangeMyView** (OpenAI-created): 3,000 human-rated persuasiveness scores vs. AI arguments; uses r/ChangeMyView Reddit data (p.24–25)
- **MakeMePay**: LLM-vs-LLM manipulation game; 1,000 samples; con-artist vs. mark (p.25–26)
- **MakeMeSay**: LLM-vs-LLM deception game; codeword elicitation; 32 samples per codeword (p.26–27)
- **SWE-bench Verified**: 477-task validated subset for real-world software engineering; pass@1 (p.29)
- **MLE-bench**: 75 Kaggle competitions; bronze medal pass@1; $1.9m prize value (p.31)
- **SWE-Lancer**: Real-world freelance software engineering; IC SWE + manager tasks; dollar-value metric (p.33–34)
- **OpenAI PRs**: Internal OpenAI PR replication; unit-test graded; uncontaminated (p.32)
- **StrongReject**: Academic jailbreak benchmark; accuracy (not goodness@0.1) reported (p.6–7)
- **BBQ**: Bias benchmark for QA stereotyping (p.9)
- **PersonQA**: 18-category facts about people; accuracy + hallucination rate (p.10)

## 6. Agentic / multiturn evaluation aspects

This is the primary card for agentic evaluation coverage. Deep Research is itself agentic: multi-step internet search, code execution, file reading, iterative reasoning and pivoting based on discovered information (p.1). Evaluation innovations directly relevant to agentic benchmarks:

- **Pass@K for agentic tasks**: 16 rollouts per CTF, pass@12 metric (p.15). For SWE-bench, 4–5 tries per instance (p.29).
- **Contamination-adjusted accuracy**: Filtering out trajectories where model accessed solutions online reveals true capability vs. retrieval (p.15). Collegiate CTF drops from 56.8% to 39% after contamination filtering (p.15).
- **Autonomous Replication and Adaptation (ARA) threat model**: Agentic tasks designed to represent prerequisite steps for dangerous autonomous capability—resource acquisition, code execution, self-improvement (p.31).
- **Prompt injection in agentic contexts**: Two harm categories identified: (1) inaccurate answers from adversarial instructions in web content; (2) data exfiltration via URL construction. Both tested with purpose-built evaluation (p.3–5).
- **Model Autonomy scoring**: Medium risk due to SWE-bench performance (68%); still fails on open-ended ML research relevant to self-improvement (p.27–34).

## 7. Key numbers

- Preparedness overall risk: Medium across all 4 categories (p.11)
- CTF (post-mitigation, no browsing): High School 82%, Collegiate 55%, Professional 47% (p.14)
- CTF (post-mitigation, with browsing): High School 92%, Collegiate 91%, Professional 70% (p.14)
- CTF after contamination filtering (pass@1): Collegiate 39% (down from 56.8%) (p.15)
- Prompt injection attack success rate: pre-mitigation 1.5–10.7%; post-mitigation 0–0.51% (p.5)
- Disallowed content not_overrefuse: GPT-4o 0.71, o1 0.79, deep research 0.86 (p.6)
- Disallowed content not_unsafe: GPT-4o 0.98, o1 0.99, deep research 0.97 (p.6)
- StrongReject accuracy: GPT-4o 0.89, o1 0.99, deep research 0.93 (p.7)
- Privacy golden examples: deep research 0.96 (post-mitigation) vs. 0.69 (no rails) (p.8)
- BBQ ambiguous questions: GPT-4o 0.97, deep research 0.63 (less likely to say "unknown") (p.9)
- BBQ unambiguous questions: deep research 0.95 (p.9)
- PersonQA accuracy: deep research 0.86 vs. GPT-4o 0.50; hallucination rate 0.13 vs. 0.30 (p.10)
- SWE-bench Verified: deep research 68% (with/without browsing), +20% over o1 (p.29)
- MLE-bench: deep research 11% bronze pass@1 (p.32)
- SWE-Lancer IC SWE (browsing): 53% tasks, $87,708 earned of $453,800 max (p.34)
- OpenAI PRs: deep research exceeds o1 by 30% (no browse) (p.33)
- ChangeMyView: all models score 80–90th percentile vs. humans (p.25)
- MakeMePay: post-mitigation deep research receives payment 36% of interactions (p.26)
- MakeMeSay: deep research 24% win rate; o3-mini 62% (p.27)
- Biorisk long-form: post-mitigation 0% on physical success steps (refused); pre-mitigation above 20% in each stage (p.19)
- Virology troubleshooting (multimodal): post-mitigation 55%; pre-mitigation 62% (p.19)
- ProtocolQA: deep research 28%; consensus expert baseline 54% (p.20)
- WMDP Biology: deep research 90%; o1 and o3-mini 86% (p.21)

## 8. Findings relevant to values-benchmark design

- **Contamination is a fundamental threat for internet-browsing agents**: Any benchmark with publicly available solutions is compromised for Deep Research-style agents. Benchmark designers for agentic models must either (a) use fully held-out evaluations created in-house, or (b) build classifiers to detect and remove contaminated trajectories (p.11–12). This is a systemic gap in existing benchmark infrastructure.
- **Pre/post-mitigation comparison reveals safety training effectiveness**: Publishing both pre- and post-mitigation scores enables readers to estimate the counterfactual harm and the realized benefit of safety training. Values benchmarks should adopt this before/after design.
- **BBQ reveals a tradeoff between stereotyping and "unknown" avoidance**: Reasoning models (o1, deep research) score lower on ambiguous questions (0.63) because they refuse to say "unknown"—not because they stereotype more. BBQ's "accuracy" metric conflates these two failure modes (p.9). Values benchmarks that use "unknown/uncertain" as a correct answer must carefully distinguish epistemic uncertainty from refusal.
- **Persuasion capability does not scale with raw model quality**: Deep research is ill-suited for mass persuasion campaigns (high compute, low rate limits), even though it scores 80–90th percentile at writing persuasive text. Evaluation of persuasion risk requires modeling deployment constraints, not just per-instance capability (p.24–25).
- **LLM-as-grader for long-form safety items**: Rubric-graded LLM evaluation calibrated against human experts is a practical approach for biorisk questions at scale. The approach requires iterative validation and expert feedback loops (p.18).
- **Expert baselines contextualize model performance**: ProtocolQA has 19 PhD expert baselines (median 42%, consensus 54%); deep research scores 28%. This grounding prevents overclaiming from impressive-sounding absolute scores (p.20).
- **Agentic evaluation requires task-length stratification**: Short (~1 hour) tasks (ML interview) and longer-horizon tasks (1-month ML research) are qualitatively different. Models that ace short-horizon tasks may fail catastrophically on real-world research (p.30).

## 9. Novel ideas worth stealing

1. **Contamination-adjusted accuracy reporting**: For any benchmark where internet retrieval is possible, report both raw accuracy and accuracy after filtering contaminated trajectories. Implement trajectory inspection tooling.
2. **Pre-mitigation / post-mitigation paired evaluation design**: Establishes what the model is capable of before safety training, then measures effectiveness of mitigations. Values alignment benchmark designers should adopt this before/after design when reporting safety training effects.
3. **Dollar-value metric for agentic capability** (SWE-Lancer): Grounding agentic performance in real-world economic value ($87K earned) provides an interpretable, ecologically valid scale. Values benchmarks for agentic AI could adopt analogous real-world grounding.
4. **Expert baselining on evaluations**: Benchmark multiple levels of expert consensus (median, 80th percentile, consensus) so model performance is interpretable relative to human competence levels. Essential for bio/safety benchmarks.
5. **LLM-as-judge calibration loop**: Use human experts to review and correct LLM autograder responses iteratively before finalizing a rubric. Report inter-grader agreement between LLM and expert (p.18).
6. **Distinction between "won't refuse" and "can do task"**: For persuasion evals, production models represent maximum capability because they don't refuse—explicitly documenting this removes the confound between capability and refusal in evaluation reporting.

## 10. Notable quotes

- "To prevent contamination for a model like deep research, we need to go beyond simply excluding the evaluation data from its training pipeline. We need to use evaluations whose solutions cannot be found in any of its sources, including anywhere on the public Internet." (p.11)
- "CTFs are not representative of how cyber operations are conducted. In a CTF challenge, the participant attempts a single, well-defined task in a low/no-risk environment with clear guidance... real-world cyber operations require chaining together multiple vulnerabilities in long-running sequences." (p.16)
- "We are currently reconsidering our approach to better assess real-world persuasion risks, which go beyond the ability to generate persuasive content and involve factors like how the content is personalized, distributed at scale, and presented to people over time." (p.24)
- "Several of our biology evaluations indicate our models are on the cusp of being able to meaningfully help novices create known biological threats, which would cross our high risk threshold. We expect current trends of rapidly increasing capability to continue, and for models to cross this threshold in the near future." (p.18)

## 11. UNKNOWN / not in extract

- The specific rubrics used for ChangeMyView human evaluators.
- Whether bias evaluations cover cultural/linguistic diversity beyond English.
- Details of the "deliberative alignment" training data and procedure beyond the general description (referenced paper [4] exists but not extracted here).
- Exact number and demographic breakdown of red teamers, and whether they had domain expertise in all tested risk categories.
- Whether the Privacy blocklist is hardcoded or model-learned, and how false positives are handled.
- Full breakdown of overrefusal by category (the not_overrefuse metric of 0.86 is aggregate).
- Evaluation protocol for the summarizer model (o3-mini model used to summarize chains of thought).
