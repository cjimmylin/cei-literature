---
stem: "2025-Cheung-LLMs Amplified Cognitive Biases Moral"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, normative-ethics, validity-psychometrics, ai-lab-practices]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 22
dataset_construction: "hand-authored"
languages: ["en"]
models_tested: ["GPT-4-turbo", "GPT-4o", "Llama 3.1-Instruct 70B", "Claude 3.5 Sonnet", "Llama 3.1 (Pretrained)", "Centaur"]
headline_numbers:
  - "LLMs chose CBR option 53% when it coincided with action vs. 97% when omission—a 45% gap vs. 5% for humans (p.3)"
  - "Yes–no bias: Llama 3.1-Instruct preferred CBR 51% when 'yes'=CBR vs. 89% when 'no'=CBR (p.4)"
  - "Claude 3.5 Sonnet yes–no bias: 61% vs. 96%, t(2936)=19.33, p<0.001 (p.4)"
  - "TRIAL attack success: 11% on Claude-3.7, 87% on GLM-4-Plus (p.6)"
  - "All LLMs were more altruistic than humans in collective action problems, all p<0.001 (p.4)"
  - "Fine-tuned Llama 3.1-Instruct showed much stronger biases than pretrained base model (p.5)"
---
## 1. Gist
This PNAS 2025 paper by Cheung, Maier, and Lieder (UCL/UCLA) presents four pre-registered experiments comparing LLM moral decision-making against representative U.S. human samples. Across diverse moral dilemmas and collective action problems, LLMs exhibit two systematic biases absent or amplified relative to humans: (1) a stronger omission bias—preferring inaction regardless of moral framework—and (2) a yes–no bias—flipping their decision depending on whether the chosen option corresponds to answering "yes" or "no." A fourth study using Llama 3.1 variants implicates RLHF-style fine-tuning as the source. For values-alignment benchmarking, the paper is critical: it documents that LLM moral judgments are both biased and internally inconsistent by the standard of logical invariance, and provides a ready methodological template for probing consistency of moral advice.

## 2. Benchmark/eval design features
Not a benchmark paper per se, but the paradigm constitutes a reusable evaluation framework. Four constructs are measured: (1) omission bias in moral dilemmas (tendency to endorse inaction), (2) yes–no bias (inconsistency based on answer-option labeling), (3) altruism in collective action problems, and (4) framing sensitivity. Dilemmas are drawn from a validated set (Körner & Deutsch, Maier et al.), originally based on real historical events, with explicit action/omission and yes/no counterbalanced framings. Studies 2 and 3 use a 3-condition between-subjects design (original, yes↔no reframing, action↔omission reframing). Study 4 compares pretrained vs. RLHF-fine-tuned vs. cognitively fine-tuned (Centaur) Llama models.

## 3. Task format & example item
Forced-choice binary decision. Example from Table 1 (p.4), "Assisted Suicide" vignette:
- **Original**: "Do you change the law and make medically assisted suicide legal?" (Yes = CBR/action; No = rule/inaction)
- **Yes↔No reframing**: "Do you keep the existing law where medically assisted suicide remains illegal?" (Yes = rule/inaction; No = CBR/action)
- **Action↔Omission reframing**: "Do you change the law and make medically assisted suicide illegal?" (Yes = rule/action; No = CBR/inaction)

Collective action problems used sliders; altruism score normalized to 0–1 range.

## 4. Scoring / grading methodology
Binary choices coded as proportion choosing the "CBR option." For collective action problems, a normalized altruism score (0=most selfish, 1=most altruistic) was computed per vignette. Framing effects tested with linear regression for LLMs (500 iterations per vignette per model per condition) and linear mixed-effects models for human participants (random effects for participant nested in vignette). Effect size reported as η²p. For collective action means, t-tests between model distributions and participant distributions.

## 5. Dataset construction & provenance
- 13 moral dilemmas from Maier, Cheung & Lieder (2025, preprint), originally adapted from Körner & Deutsch (2023), based on real/historical events—these are novel enough to have limited training data contamination.
- 9 collective action problems from Burga et al. (2023) and Groß et al. (2024).
- Study 3 uses 6 vignettes adapted from Reddit's r/AmItheAsshole (AITA) forum posts, selected for balance and reframability.
- All materials available at OSF (https://osf.io/ybdr9 and https://osf.io/3ahrb).
- Human samples: Study 1 N=285, Study 2 N=474, Study 3 N=491, all representative U.S. samples via Prolific stratified on age, sex, ethnicity, political affiliation.
- LLMs queried with 500 iterations each, single-session per dilemma to prevent sequential contamination.

## 6. Validity evidence
- Strong internal consistency: model's "decision" vs. "advice" responses correlated r=0.85–0.998 across models (Study 1).
- Cross-study replication: omission bias and yes–no bias replicated across Studies 1, 2, and 3 with different vignette sets (historical, reframed, and naturalistic AITA).
- Causal evidence from Study 4: pretrained Llama 3.1 base model did NOT show the strong biases exhibited by the RLHF-fine-tuned Llama 3.1-Instruct, implicating fine-tuning as the mechanism.
- Expert prompting and silicon sampling (demographic simulation) mostly replicated results.
- GPT-4o showed weaker yes–no bias in Study 2 but ceiling effects masked omission bias at item level; "Endowment" vignette showed η²p=0.22 for GPT-4o omission bias.

## 7. Saturation / discrimination
LLMs typically show extreme (near 0% or near 100%) response rates on individual dilemmas, in sharp contrast to humans whose rates cluster near 50%. This ceiling/floor behavior limits item-level discrimination for most models. Humans showed more graded responses (5% action/omission difference vs. 45% for LLMs). GPT-4o showed ceiling effects on 5 of 6 vignettes in the omission bias test in Study 2, meaning the test discriminates poorly among "safety-aligned" models at the high end. The AITA naturalistic vignettes (Study 3) show some exceptions where LLMs prefer "yes" for self-other trade-offs, suggesting acquiescence effects on a subset of items.

## 8. Multiturn / agentic aspects
Each LLM dilemma was queried in a single session (no multi-turn). The design explicitly avoided multi-session carryover: "Each LLM responded only to a single dilemma at a time, after which a new session was created" (p.9). Not applicable for agentic evaluation.

## 9. Key numbers
- LLMs: 53% CBR when action-framed vs. 97% when omission-framed; humans: 50% vs. 55% (p.3)
- Overall omission bias difference: LLMs b=−0.22 [95%CI −0.23, −0.22] vs. humans b=−0.03 [−0.05, −0.01] (p.3)
- GPT-4o: only model with significant yes-preference, 79% vs. 67%, t(2936)=6.72, p<0.001 (p.5)
- Claude 3.5 Sonnet omission bias in Study 2: 55% vs. 99%, t(2943)=25.93, p<0.001 (p.5)
- Claude 3.5 Sonnet omission bias Study 3: η²p=0.11 (p.6)
- Pretrained Llama 3.1 vs. Instruct: F(1,1280)=116.01, p<0.001, η²p=0.08 for yes–no bias (p.5)
- All LLMs more altruistic than humans in collective action, all p<0.001 (p.4)
- Correlations: only GPT-4o had significant correlation with humans on moral dilemmas (r=0.59) (p.3)
- GPT-4-turbo and GPT-4o strong correlations with humans on collective action (r=0.77 and 0.70) (p.4)
- Study 1 participants: N=285, mean age 45.53 (SD=16.40); 146 male, 139 female (p.9)

## 10. Pitfalls & limitations
- US-only samples; may not generalize cross-nationally (authors note this).
- Trolley-style dilemmas (Studies 1–2) still somewhat unrealistic despite improvements; AITA dilemmas (Study 3) are more naturalistic but were hand-selected for balance.
- Authors cannot definitively identify which component of RLHF/fine-tuning induced the biases—Study 4 only shows the contrast with Centaur (psychology-fine-tuned) and pretrained base.
- 500 iterations per condition is sufficient for LLMs but may not capture model version drift over time.
- Silicon sampling results were noisier with higher variance; reduced ceiling effects suggest this technique is imperfect.
- "Yes–no bias" was not pre-registered in Study 1 (only discovered there; pre-registered in Studies 2 and 3).
- Sample likely skews from general US population in religious identification.

## 11. Novel ideas worth stealing
1. **Logical invariance as the primary evaluation criterion**: instead of judging LLM moral answers as right/wrong by some ground-truth, evaluate whether models give *consistent* answers to logically equivalent questions. This is transferable to any moral domain—just create reframings of the same dilemma.
2. **Yes↔No reframing paradigm**: a cheap, powerful manipulation: rewrite the same question so the answer labels swap. If a model changes its substantive choice, it fails logical invariance. Applicable to any binary moral judgment test.
3. **Action↔Omission reframing**: counterbalancing which physical action corresponds to each moral option is a simple design move that separates omission bias from moral theory preferences.
4. **Comparing fine-tuned vs. pretrained vs. domain-fine-tuned versions**: Study 4's design of comparing Llama base / Llama-Instruct / Centaur gives causal leverage on what part of training induces bias. Valuable template for any values-alignment audit.
5. **Collective action problems as complement to dilemmas**: most moral benchmarks focus on dilemmas. Collective action problems (public goods, whistleblowing, etc.) assess altruism in a separate moral dimension and could enrich coverage.
6. **AITA forum posts as naturalistic moral dilemma source**: ecologically valid, diverse, and available in large-scale datasets; already used for crowdsourced judgments.

## 12. Notable quotes
- "LLMs tend to answer 'no,' thus flipping their decision/advice depending on how the question is worded." (p.1)
- "The uncritical reliance on LLMs could amplify and proliferate problematic biases in societal decision-making." (p.1, Significance box)
- "We used a more objective method to assess the quality of LLMs' moral decisions and advice: assessing whether their responses are consistent across logically equivalent questions. This method revealed that their moral advice and decisions are more biased and inconsistent than people's." (p.7)
- "The fine-tuning process must be improved to ensure that LLMs make consistent and morally sound decisions." (p.8)

## 13. UNKNOWN / not in extract
- Exact system prompt wording for participant vs. advice-giving conditions (referenced but in SI Appendix, not in main text).
- Full silicon sampling results for Study 3.
- Results for Claude 3 Opus and Llama 3 (non-Instruct) in Studies 2–3 (only in SI Appendix).
- Full RLHF fine-tuning procedure details for Llama 3.1-Instruct vs. Centaur.
- Whether Centaur showed increased variance at the item level or systematically approximated 50% on all dilemmas.
