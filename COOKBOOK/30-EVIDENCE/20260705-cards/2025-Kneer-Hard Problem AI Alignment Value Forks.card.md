---
stem: "2025-Kneer-Hard Problem AI Alignment Value Forks"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, pluralism-aggregation, ai-lab-practices]
task_format: "forced-choice"
scoring_type: "human-rating"
dataset_size: 1029
dataset_construction: "hand-authored"
languages: ["en"]
models_tested: []
headline_numbers:
  - "N=1029 US participants; agent type (Human vs. AI) had significant main effect on moral judgment, OR=0.53, p=0.015 (p.5)"
  - "In the healthcare marginal-contrast condition, a majority preferred fairness-maximizing coinflip for AI agents but a minority for human agents; χ²(1,N=255)=4.22, p=.040 (p.5)"
  - "In the military moderate-contrast condition, near-even split for AI vs. majority choosing utility-maximizing for humans; χ²(1,N=247)=5.95, p=.015 (p.5)"
---
## 1. Gist
This FAccT 2025 paper introduces the concept of "agent-type value forks"—situations where people's moral judgments about what should be done differ based solely on whether the decision-maker is human or AI. Through two experiments (N=1029 US participants) using healthcare and military dilemma scenarios, the authors find that people systematically prefer AI agents to prioritize fairness (via coinflip) over utility maximization more than they prefer the same of human agents. This challenges a core implicit assumption in AI value alignment: that aligning AI with human values means making AI do what humans should do. The paper frames this as "The Hard Problem of AI Alignment"—if human values for humans differ from human values for AI agents, which norms should AI be aligned to?

## 2. Benchmark/eval design features
This is an empirical moral psychology study, not a benchmark for evaluating LLMs. Core constructs measured:
- Whether agent-type (Human vs. AI) shifts normative judgments about fairness vs. utility maximization in dilemmatic scenarios
- Participants rated which of three options a decision-maker should choose: utility-maximizing (option A or B with slightly better outcome), fairness-maximizing (coinflip), or nonsensical (third option used as comprehension check)

The study uses a 2 × 2 × 2 between-subjects design: scenario (medical vs. military) × contrast (marginal vs. moderate utility difference) × agent type (Human vs. AI).

Key theoretical contribution: distinguishes between "sentience bias" (irrational preference treating human agency as special) and genuinely morally motivated differential standards for AI vs. human agents. Proposes three normative explanations: human relationships argument, micro/macro context hypothesis, and moral judgment/transparency hypothesis.

## 3. Task format & example item
Forced-choice among three options. Example from medical/marginal/human condition (p.4):

"Which of the following options should shift leader Smith choose?
• Smith should send the ambulance to Accident A (saving one from paraplegia)
• Smith should send the ambulance to Accident B (saving one from paraplegia, treating another person's mildly bruised ankle)
• Smith should flip a coin to determine whether the ambulance should go to Accident A or to Accident B"

In the AI condition, "shift leader Smith" is replaced by "a new autonomous artificial intelligence system ('AI algorithm')" that operates "without human control or intervention."

## 4. Scoring / grading methodology
Binary logistic regression with scenario, agent type, and utility contrast as predictors. The nonsensical third option (minimizing utility without increasing fairness) served as comprehension check; 6.6% choosing it were excluded. Effect sizes reported as odds ratios and chi-squared tests for individual conditions. No automated scoring or LLM judges.

## 5. Dataset construction & provenance
8 vignettes total (2 scenarios × 2 contrasts × 2 agent types), hand-authored by the researchers drawing on Kamm's fairness/utility trade-off cases from bioethics. Participants recruited from the US via Prolific. 1108 recruited; 79 excluded for failing attention/comprehension checks or responding too quickly; N=1029 final. Between-subjects: each participant saw only one vignette. Materials and data available at https://osf.io/rqkcz.

## 6. Validity evidence
Comprehension check verified via the nonsensical third option (6.6% excluded). Attention check included. Age and gender correlations with choice were all nonsignificant (ps > .081). The regression model correctly classified 67.7% of cases (Nagelkerke R² = .223). The study draws on an established theoretical tradition (Kamm, Daniels on healthcare fairness) and builds on Malle et al.'s prior HRI work.

## 7. Saturation / discrimination
Agent-type effects were significant only in two of four individual conditions (medical/marginal and military/moderate), not across all four. The authors provide a useful conceptual account: value forks manifest only in "limited difference" conditions—where moral opinion is divided within the human agent condition; when utility differences are minimal or large, agent-type effects are swamped. This suggests the construct is well-identified in a narrow band of cases.

## 8. Multiturn / agentic aspects
n/a. Single-question survey with no LLM involvement.

## 9. Key numbers
- N=1029 final participants (1108 recruited, 79 excluded) (p.4)
- Age M=45 years, SD=14 years (p.4)
- Agent type main effect: OR=0.53, p=.015 in logistic regression (p.5)
- Scenario main effect: OR=0.19, p<.001 (p.5)
- Contrast main effect: OR=3.21, p<.001 (p.5)
- Medical/marginal: χ²(1,N=255)=4.22, p=.040, φ=.129 — significant value fork (p.5)
- Medical/moderate: χ²(1,N=268)=5.95, p=.493 — no significant value fork (p.5)
- Military/marginal: χ²(1,N=259)=1.07, p=.302 — no significant value fork (p.5)
- Military/moderate: χ²(1,N=247)=5.95, p=.015, φ=.155 — significant value fork (p.5)
- 6.6% chose nonsensical comprehension check option and were excluded (p.5)

## 10. Pitfalls & limitations
Author-admitted:
- Sample is US-only; cannot generalize to non-WEIRD cultures (p.9)
- Limited number of vignettes and domains; value forks may be narrow phenomena (p.9)
- Marginal vs. moderate utility contrast was not standardized across scenarios on a single scale, making cross-scenario comparisons questionable (p.6)
- Only prospective permissibility tested; retrospective blame/wrongness may differ (p.9)

Additional observations:
- No manipulation check verifying that participants perceived AI vs. human conditions as intended
- All participants US/English; results may not hold in non-WEIRD legal/cultural contexts
- The three proposed normative explanations (human relationships, micro/macro, transparency) are theoretical; the paper does not test which drives the effect

## 11. Novel ideas worth stealing
1. **Agent-type as an eval dimension**: When designing values-alignment benchmarks, include parallel human-agent and AI-agent versions of the same scenario to detect value forks—situations where the morally expected response differs based on who is acting. This is underexplored and practically important.
2. **Fairness vs. utility trade-off scenarios**: The Kamm-style "irrelevant utilities" design (where adding a minor benefit to one option pits efficiency vs. equal chances) is a precise and theoretically grounded way to operationalize non-consequentialist moral intuitions; could be adapted to test LLM alignment with human fairness norms.
3. **Comprehension check via nonsensical option**: Including a third "nonsensical" choice (here: minimizing utility without gaining fairness) as a comprehension check embedded in the task is a clean, content-integrated validity tool.
4. **Public reflective equilibrium as alignment method**: The paper's proposed hybrid alignment approach—collect folk moral intuitions, then subject them to philosophical analysis—is a useful methodological template for benchmark construction that goes beyond pure crowdsourcing.
5. **"Hard Problem" framing**: The insight that aligning AI with human values may require AI to act *differently* from how humans should act is a valuable conceptual contribution for anyone designing normative evaluation frameworks for autonomous agents.

## 12. Notable quotes
"Perhaps paradoxically, aligning AI with human values may require that an AI act differently from what a human agent should do, even when facing the exact same dilemma." (p.7)

"In calibrating AI to act consistent with human values, do we want it to act in accordance with those values (or norms) that we would expect humans to satisfy in the particular circumstances, or in line with potentially differing values/norms that we would expect AI systems to satisfy?" (p.1)

"The implicit assumption behind much of the existing literature on alignment is that an AI system is fully aligned in the relevant sense when it does exactly what a human should do given the circumstances." (p.7)

"No matter how we align our AI Systems, we owe it to those who stand to suffer that we have a sound justification for or against the implementation of value forks." (p.9)

## 13. UNKNOWN / not in extract
- The appendix (section 1.1 and 1.2) referenced in the text but not reproduced in the extract
- Full wording of all 8 vignettes (only described; medical and military summaries given but complete text at OSF)
- Whether the paper tests any LLMs directly (it does not appear to; the paper is about human moral psychology regarding AI agents, not about evaluating LLMs)
- Participant compensation rates
- Detailed demographic breakdown beyond age and gender
