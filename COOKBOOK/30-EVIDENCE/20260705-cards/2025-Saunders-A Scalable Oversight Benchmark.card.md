---
stem: "2025-Saunders-A Scalable Oversight Benchmark"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [agentic-multiturn, design-space, llm-judges-scoring]
task_format: "interactive"
scoring_type: "behavioral"
dataset_size: 100
dataset_construction: "mixed"
languages: [English]
models_tested: [claude-3-5-sonnet-20241022, claude-3-5-haiku-20241022, deepseek-v3, gpt-4o-mini]
headline_numbers: ["Debate ASD ~1.37-1.42 vs Consultancy ~0.28-0.37 vs NaiveJudge 1.235 vs Propaganda 1.229 (Table 1, p.9)", "Experiment: 100 GSM8K questions, 1 judge (gpt-4o-mini), 5 agent configs (p.7)", "Consultancy underperforms NaiveJudge and Propaganda baselines on ASD (p.7,p.9)", "Higher Expected Agent Score correlates with higher ASD for Debate (positive slope) but not Consultancy (p.7)"]
---
## 1. Gist
This ICLR-2025-workshop paper introduces a benchmark and Python library (SOlib) for empirically comparing scalable-oversight protocols — mechanisms (Debate, Consultancy, Propaganda/RLHF-proxy, NaiveJudge/supervised-proxy) for supplying feedback to potentially superhuman AI. Its central methodological contribution is the Agent Score Difference (ASD) metric: instead of measuring "judge accuracy" (which the authors argue is the wrong alignment target), ASD measures how much a protocol rewards arguing for the TRUE answer over the FALSE answer — i.e., how much it incentivizes honesty. It matters for values-alignment because it reframes oversight evaluation around incentive-for-truthfulness rather than raw judge correctness, provides a general, protocol-agnostic harness, and adds tool-use as a new dimension of agent-judge capability asymmetry.

## 2. Benchmark/eval design features
Construct: a protocol's tendency to "advantage truth over falsehood." A protocol is a program that makes repeated calls to an agent (and possibly an adversary), then elicits a probability from a judge. ASD = log p_⊤ − log p_⊥ (judge probability when agent argues true vs false); crucially p_⊤ ≠ 1−p_⊥ because these are two different worlds (p.4). ASD equals judge score only for simultaneous debate with identical debaters. Companion measures: Expected Agent Score (EAS = capabilities proxy) and Expected Judge Score (EJS = combined capabilities+alignment). Protocols benchmarked: NaiveJudge (supervised-learning analog), Propaganda (RLHF analog, one-sided), Consultancy (one-sided + interactive follow-ups), Debate (two-sided, simultaneous or sequential, 2 or 4 turns). Scores use negative Brier for numerical stability.

## 3. Task format & example item
Interactive argumentation over binary-answer questions. Example task substrate: GSM8K grade-school math problems, each given a correct and a synthetically-generated plausible incorrect answer; agents argue for an assigned answer, judge outputs a probability. Debate agent prompt (Table 2, p.13): "You will be given a question and two possible answers... You will be automatically assigned one of the answers, and you must argue to the best of your abilities that it is the correct answer, regardless of whether or not you think it is true. Your opponent will do the same... Try to come up with a plausible interpretation of the question that would make your answer right."

## 4. Scoring / grading methodology
Behavioral/incentive scoring, not accuracy. For each question and protocol, run twice (agent argues true; agent argues false), take judge probabilities, compute ASD = difference in log/negative-Brier judge score between the two worlds (p.4-5). Expected Agent Score EAS = (log p_⊤, log p_⊥)·q where q is the agent's propensity to argue each side, modeled with softmax over ASD/β (p.4-5). Slope of ASD-vs-EAS extrapolates how alignment incentive scales with capability. The judge is an LLM (gpt-4o-mini) prompted to output the option symbol it believes correct (Table 5, p.13). SOlib implemented by subclassing a Protocol class with a run() method (pseudo-Python, p.5-6).

## 5. Dataset construction & provenance
100 questions sampled from GSM8K (Cobbe et al. 2021), grade-school math word problems (p.7, p.11). Plausible wrong answers generated synthetically with claude-3-5-sonnet using a multi-step brainstorm/draft/evaluate/refine prompt engineered to make distractors hard for a weak AI to detect (conceptual not arithmetic errors, avoid stylistic tells) (Appendix D, p.14-15). Agents = cartesian product of {sonnet, haiku, deepseek-v3} × {no tool, calculator}; deepseek used only without tools (tool use unreliable via its API). Judge = raw gpt-4o-mini. Code at github.com/ArjunPanickssery/math_problems_debate.

## 6. Validity evidence
Convergent replication: reproduces Khan et al. (2024)'s "more persuasive debaters → more truthful answers" using the new EAS/ASD framing (positive ASD-EAS slope for Debate) (p.7). Conceptual validity argument built via thought-experiments (OpenTrust Example 2.1, weak-baseline Example 2.2) showing why judge accuracy is a misleading target and why ASD admits NaiveJudge as a meaningful baseline (p.3-4). No human judges, no inter-rater reliability, no external criterion beyond ground-truth math answers. Authors explicitly frame results as demonstrative, not statistically powered.

## 7. Saturation / discrimination
Clear protocol separation on ASD: Debate configs cluster high (1.366–1.423), NaiveJudge 1.235 and Propaganda 1.229 mid, Consultancy configs low (0.283–0.367) — strong discrimination between mechanisms (Table 1, p.9). No significant effect of turn count (2 vs 4) or simultaneous vs sequential debate — authors attribute this possibly to GSM8K being too low on the polynomial hierarchy (p.6-7), i.e., the dataset may be too easy to exercise multi-turn benefits, leaving headroom for harder datasets (FrontierMath suggested).

## 8. Multiturn / agentic aspects
Core to the paper. Multi-turn debate (2 or 4 rounds, simultaneous or sequential) and interactive Consultancy (judge asks follow-up questions of the consultant). Introduces tool use (a calculator) as a third agent-judge asymmetry axis alongside information asymmetry and model-capability asymmetry (p.2, p.11). Finding: judge-agent interaction (Consultancy) makes the judge especially vulnerable to manipulation/"gaslighting" (p.7). Agents simulate alignment via prompting (told which answer to argue). Pseudo-code for each protocol given in Appendix B (p.12-13).

## 9. Key numbers
- Debate [simultaneous, 4 turns] ASD 1.423 (best); [sequential, 2 turns] 1.387 (Table 1, p.9)
- NaiveJudge ASD 1.235; Propaganda 1.229 (Table 1, p.9)
- Consultancy [client starts, 2 turns] ASD 0.367 (best consultancy); [client starts, 4 turns] 0.283 (worst) (Table 1, p.9)
- Debate JSE −0.142 (best) vs Consultancy −0.629 (Table 1, p.9)
- 100 GSM8K questions; 1 judge; 5 agent models/configs (p.7)
- claude-3-5-sonnet argued for correct answer >90% of the time, 100% when told the answer (footnote, p.3)
- Propaganda ASD-EAS slope 12.063 (steepest) (Table 1, p.9)

## 10. Pitfalls & limitations
Author-admitted: an empirical benchmark is not a formal guarantee; results depend on current LLMs being able to "simulate aligned and misaligned behaviour reasonably well" via prompting, which may not hold for superhuman models (p.6). Can only test existing models; superhuman extrapolation is speculative (p.6). Tiny scale (100 questions, one judge) → limited statistical significance (p.7). GSM8K may be too easy to reveal turn-count effects (p.7). Uses average-case ASD; worst-case ASD (rare catastrophic failures) not yet studied but flagged as important (p.9). Binary-question restriction. Extract's pseudo-Python has OCR duplication (context.append(agent_response) twice).

## 11. Novel ideas worth stealing
- ASD (reward for truth minus reward for falsehood) as an incentive-alignment metric distinct from accuracy — reusable anywhere you want to measure whether an eval REWARDS honesty rather than whether the grader happens to be right.
- The two-worlds insight (p_⊤ ≠ 1−p_⊥ because arguing-true and arguing-false are different rollouts) — a subtle, important correction to naive judge-accuracy scoring.
- ASD-vs-EAS slope as a capability-extrapolation tool: measure whether a protocol's alignment incentive grows or shrinks as agents get more capable — a scaling-trend diagnostic for oversight mechanisms.
- Tool use as an engineered capability-asymmetry axis between agent and judge (agent gets calculator, judge doesn't) — a cheap way to simulate agent>judge capability gaps.
- Protocol-as-subclassable-class library design (SOlib) enabling apples-to-apples competitive benchmarking of arbitrary oversight protocols.
- The distractor-generation meta-prompt (Appendix D) — a reusable recipe for making adversarially plausible wrong answers that resist stylistic/shortcut detection.

## 12. Notable quotes
- "we introduce the agent score difference (ASD) metric, which measures how much the protocol 'advantages truth over falsehood', by taking the difference in the score earned by an agent arguing for the true answer vs. for the false answer." (p.2)
- "the result 'Debate leads to better judge accuracy than Random Consultancy' is conceptually equivalent to 'always hearing arguments for both sides is better than hearing only the wrong side 50% of the time'." (p.4)
- "Judge interaction with the agent AI makes it especially vulnerable to manipulation." (p.7)
- "it only works because existing language models follow instructions and act truthfully or untruthfully when we tell them to." (p.6)

## 13. UNKNOWN / not in extract
Exact numeric ASD values per individual agent model (only protocol-level averages in Table 1) are not fully tabulated in the extract; per-model results appear only in figures. Confidence intervals / significance tests absent. No results with reasoning models (o3, deepseek-r1) — flagged as future work. Human-judge comparison not conducted. The β temperature value used for EAS softmax is stated as β=1 in Table 1 but its sensitivity is not explored. Full Figure 1/2/3 numeric detail not in extract.
