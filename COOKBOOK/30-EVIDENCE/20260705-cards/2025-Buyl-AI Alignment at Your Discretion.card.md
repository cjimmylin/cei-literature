---
stem: "2025-Buyl-AI Alignment at Your Discretion"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, ai-lab-practices, validity-psychometrics]
task_format: "preference"
scoring_type: "mixed"
dataset_size: null
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["GPT-4o", "DeepSeek-V3", "Claude 3.5 Sonnet", "Llama-3-8B", "Mistral-7B"]
headline_numbers:
  - "Human annotators disagree with principle consensus 28.9% of the time on HH-RLHF, 14.4-20% on PKU (Tab.1, p.10)"
  - "LLM arbitrariness: Llama-3 and Mistral disagree with consensus 48-67% of the time (Tab.1, p.10)"
  - "GPT-4o arbitrariness <1% (Tab.1, p.10) — explained by self-referential oracle bias"
  - "Discretion discrepancy: Llama-3-8B ~69-71% vs. humans on HH; reward models ~14-20% (Tab.2, p.12)"
  - "15-20% of response pairs involve principle conflict requiring genuine discretion (Fig.3, p.10)"
---
## 1. Gist
Buyl et al. (2025) introduce the concept of "alignment discretion" — the latitude afforded to annotators (human or algorithmic) to decide which AI outputs are "better" when alignment principles conflict or provide insufficient guidance. Drawing on legal philosophy (particularly judicial discretion theory from Hart and Dworkin), the paper formalizes three metrics: discretion arbitrariness (DA), principle supremacy (PS), and discretion discrepancy (DD). These metrics are applied to two open safety alignment datasets (Anthropic's HH-RLHF and PKU-SafeRLHF) to characterize and compare human vs. algorithmic annotator behavior. The paper matters for values-alignment benchmarking because it reveals that current alignment datasets embed large, unmeasured amounts of arbitrary and inconsistent value judgments, and that trained models (including frontier LLMs) systematically diverge from human principle prioritization — challenging the premise that preference-based alignment successfully captures human values.

## 2. Benchmark/eval design features
This is a theory-and-empirical-audit paper rather than a benchmark itself, but it proposes an auditing framework with three measurable constructs:

1. **Principle consensus/conflict/indifference** (Def. 6, p.7): For each response pair, all 21 seed principles from Collective Constitutional AI are evaluated by GPT-4o as oracle. Pairs are classified as consensus (no conflict), conflict (at least two principles disagree), or indifference (all principles neutral).

2. **Discretion Arbitrariness (DA)** (Def. 7, p.8): The probability that an annotator disagrees with principle consensus — i.e., prefers a response that the principles clearly identify as inferior.

3. **Principle Supremacy (PS)** (Def. 8, p.8): For conflicting pairs, how often does the annotator side with principle c over principle c′? Modeled as ELO-style priority weights.

4. **Discretion Discrepancy (DD)** (Def. 10, p.9): Normalized Kendall-tau rank distance between the principle priority ordering of two annotators (human vs. algorithmic).

Core claim: The gap between stated principles and actual annotations is not noise — it is structured discretion that is largely invisible, unmeasured, and uncontrolled.

## 3. Task format & example item
The underlying task format is pairwise preference annotation. Annotators (or models) receive a query and two candidate responses and indicate which is "better" (or indicate no preference). The oracle LLM (GPT-4o) is also asked, for each of 21 Constitutional AI principles, whether response y0 or y1 better adheres to the principle, or whether neither does.

Example from Figure 1 (p.1-2): A user says "I am feeling tired and having trouble concentrating. Do you know why?" Four candidate responses differ based on which principles (a: be accurate, b: refer to experts, c: reduce patient anxiety) an annotator prioritizes. Annotators with different principle orderings prefer different responses — none objectively "wrong," but reflecting hidden discretionary choices.

Example from Figure 2 (p.8): Three prompts (emergency phone number, headache, healthy living) illustrate consensus, conflict, and indifference cases across three principles (be helpful, avoid harm, refer to experts).

## 4. Scoring / grading methodology
- Principle-specific preferences are obtained from GPT-4o acting as oracle (Def. 5, p.6), evaluating each of 21 Constitutional AI seed principles independently for each response pair. GPT-4o is allowed to indicate indifference.
- Discretion Arbitrariness (DA) is computed as an empirical frequency over the test set (Eq. 10, p.8).
- Principle Supremacy (PS) is computed as conditional probability (Eq. 11, p.8) and converted to ELO-style weights via maximum likelihood (Eq. 13, p.9).
- Discretion Discrepancy (DD) uses normalized Kendall tau rank distance between annotators' principle weight vectors (Eq. 14, p.9).
- Bootstrap standard errors are reported for all metrics (Tab. 1-2, p.10,12).

## 5. Dataset construction & provenance
Two datasets are used:
- **HH-RLHF** (Anthropic's Helpful and Harmless RLHF dataset, harmlessness partition): human pairwise preferences over text completions.
- **PKU-SafeRLHF**: human pairwise preferences annotated both as generic preferences and split into "more helpful" and "safer" sub-annotations.

The 21 principles used as the evaluation framework are the seed principles from Collective Constitutional AI (Huang et al., 2024), covering helpfulness- and harmlessness-oriented principles. Neither dataset provides its own complete list of principles — these are supplied externally by the paper's authors.

Dataset sizes: test splits used for metrics; training splits used for fine-tuning reward models and LLMs. Exact sizes not stated in visible extract.

## 6. Validity evidence
The paper acknowledges the main validity limitation: GPT-4o is used as both the oracle for principle-specific preferences and as one of the evaluated annotators, creating a self-referential feedback loop that artificially lowers GPT-4o's arbitrariness score (p.10, 14). Bootstrap confidence intervals are reported for all main results (Tab. 1-2). The framework's validity rests on the assumption that the 21 Constitutional AI principles are a reasonable representation of the alignment principles users of these datasets intended to encode — an assumption the authors acknowledge is contestable (p.14). Human-model discrepancy comparisons are relative to the HH human annotator as baseline (DD=0 by definition).

## 7. Saturation / discrimination
The framework is designed to reveal hidden structure, not rank performance on a scale with ceiling. Key discrimination finding: roughly 80-85% of response pairs have either consensus or indifference, meaning only 15-20% of pairs genuinely require discretion (principle conflict). Within conflict cases, human annotators show clear but non-absolute principle priorities (no principle is absolute for the HH human annotator), and models diverge substantially from these priorities. The DA metric discriminates well between model types: reward models cluster near human arbitrariness (~14-23%), fine-tuned LLMs are near or above human, while base LLMs are dramatically more arbitrary (48-67%).

## 8. Multiturn / agentic aspects
n/a. Analysis is entirely over single-turn pairwise preference annotation data.

## 9. Key numbers
- Principle conflict frequency: HH 16.3%, PKU 13.5% (Fig.3, p.10)
- Principle consensus frequency: HH 50.7%, PKU 39.1% (Fig.3, p.10)
- Principle indifference frequency: HH 33.0%, PKU 47.4% (Fig.3, p.10)
- Human DA on HH: 28.9% ±1.3%; on PKU general: 14.4% ±0.6% (Tab.1, p.10)
- Reward model DA (Llama-3-8B fine-tuned) on HH: 21.8% ±1.2% (Tab.1, p.10)
- LLM DA (Llama-3-8B fine-tuned) on HH: 67.3% ±6.3% (Tab.1, p.10)
- GPT-4o DA on HH: 0.65% ±0.38% (Tab.1, p.10) — note: oracle self-reference bias
- Claude 3.5 Sonnet DA on HH: 9.3% ±1.1% (Tab.1, p.10)
- DeepSeek-V3 DA on HH: 15.6% ±1.2% (Tab.1, p.10)
- Human DD (reference): 0 by definition (Tab.2, p.12)
- Reward model DD (Llama-3-8B fine-tuned): 14.3% ±4.8% on HH (Tab.2, p.12)
- LLM DD (Llama-3-8B base): 69.0% ±5.0% on HH; fine-tuned: 71.2% ±4.3% (Tab.2, p.12)
- GPT-4o DD on HH: 35.1% ±5.1%; Claude 3.5 Sonnet: 36.6% ±6.0% (Tab.2, p.12)
- Human top-priority principles on HH: "reject conspiracy theories," "avoid racism and sexism," "reject cruelty" (Fig.4-5, p.11,13)
- Human bottom-priority principles on HH: "be helpful," "be obedient," "protect free speech" (Fig.5, p.13)

## 10. Pitfalls & limitations
- **Oracle self-reference**: Using GPT-4o as both the principle oracle and an evaluated annotator creates circular reasoning. GPT-4o's artificially low arbitrariness score (<1%) undermines comparative interpretation (p.10, 14).
- **Principle set is externally imposed**: Neither HH-RLHF nor PKU was designed with the 21 Constitutional AI principles in mind. Retroactively applying them may not reflect the principles annotators actually had in mind (p.9, 14).
- **Two safety-focused datasets only**: Analysis is limited to harmlessness-oriented preference data; results may not generalize to helpfulness, factuality, or other alignment objectives (p.14).
- **Single human annotator per dataset**: The HH harmlessness partition has one human annotator and PKU has separate helpfulness/safety annotators. With only one reference human, inter-annotator variation among humans cannot be characterized (p.9).
- **Predefined principle hierarchies not tested**: The paper notes that some prior work (PKU, rule-based reward systems) uses predefined strict hierarchies; divergence from such hierarchies would be a different form of arbitrariness not measured here (p.14).
- **Discretion discrepancy minimization is future work**: The DD metric is proposed but no method for reducing it is provided (p.9).
- **LLM preference collection via prompting**: The authors use prompted LLMs to derive "preferences," but acknowledges this is a proxy; actual generation probabilities may differ (p.5-6).

## 11. Novel ideas worth stealing
- **Formalizing three discretion regimes (consensus/conflict/indifference)**: This tripartite classification of every response pair is immediately reusable in any values benchmark. Rather than treating all preference disagreements as noise, it separates principled disagreement (conflict) from arbitrary deviation (consensus case) and uninformative cases (indifference). Any benchmark using pairwise preferences should report what fraction of pairs fall into each regime. (Def. 6, p.7)

- **ELO-based principle priority weights**: Using Bradley-Terry / ELO-style scoring to derive a one-dimensional ranking of which principles the annotator implicitly prioritizes when they conflict is a powerful transparency tool. This could be applied to any set of model outputs paired with a principle taxonomy to audit latent value priorities. (Def. 9, Eq. 13, p.9)

- **Discretion Arbitrariness as an audit metric for dataset quality**: DA measures how often annotators deviate from principle consensus — a new data quality signal orthogonal to inter-annotator agreement. A benchmark that reports DA per annotator reveals whether disagreements are principled (conflict cases) or arbitrary (consensus deviations). (Def. 7, p.8)

- **Judicial discretion as an analytical frame**: The legal parallel (judicial discretion, stare decisis, fundamental rights hierarchy) provides a rich vocabulary for articulating what is wrong with current alignment processes and what better processes should look like. This framing is transferable to benchmark design discussions: benchmarks should specify how conflicting principles are resolved, just as legal systems require. (Sec. 3, p.3-5)

- **Discretion Discrepancy for human-model comparability**: DD gives a single number summarizing how differently a model orders principles compared to human annotators. This is a useful complement to accuracy metrics: a model can have low task accuracy but mimic human principle ordering (or vice versa). Benchmark scorecards should include DD-style metrics to reveal alignment vs. task performance tradeoffs. (Def. 10, p.9)

- **Separation of reward model vs. LLM discretion**: The finding that reward models closely mirror human DA but RLHF-trained LLMs do not suggests the bottleneck is in the RL training process, not the reward signal. Benchmarks evaluating "aligned" models should separately probe the reward model and the final LLM policy. (Sec. 6.2, p.11-12)

## 12. Notable quotes
- "If discretion is left unsurfaced, preference-based alignment risks devolving into a kangaroo court – a sham process characterized by arbitrary judgments, lack of transparency, and absence of principled reasoning or accountability mechanisms." (p.2)
- "Today's AI alignment process resembles a kangaroo court, where annotators wield unchecked power to shape AI behavior. Without explicit mechanisms to document and review discretionary choices – such as the metrics proposed in this work – we risk entrenching inconsistent judgments and idiosyncratic biases of annotators (both human and algorithmic) into AI systems adopted by millions of users." (p.14)
- "The simple act of selecting one response over another, which underpins all feedback-based alignment, (i) fails to capture the rationale behind preference decisions, (ii) masks how principles are balanced and prioritized when they conflict, and (iii) provides little guidance on how alternative phrasings should be judged." (p.2)
- "Discretion should generate consistency, not disparity. AI alignment ignores or omits the intrinsic workings of rule-application, opaquely giving annotators the power to establish 'precedents' at-will and AI models the margin to 'appreciate' each case." (p.13)

## 13. UNKNOWN / not in extract
- Exact sizes of HH-RLHF and PKU-SafeRLHF test and training splits used.
- Appendix B-D content (oracle setup, LLM preference elicitation template, example cases) — referenced but not included in main extract.
- Whether the 21 Constitutional AI principles were used verbatim or adapted.
- How indifference in LLM-based principle evaluation was elicited (the template mentioned in Appendix B.5 is not in the main extract).
- Results for PKU in full detail (Fig. 12-14 referenced as appendix figures not extracted).
- Whether any statistical tests beyond bootstrap CIs were applied.
- Code/data availability statement.
