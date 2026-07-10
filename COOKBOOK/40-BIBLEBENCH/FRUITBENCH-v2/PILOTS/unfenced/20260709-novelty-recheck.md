# UNFENCED focused novelty re-check

**Audit date:** 2026-07-09
**Verdict:** **REVISE-AND-PROCEED / conditional pass.** UNFENCED's broad novelty language is no longer defensible, but its proposed contribution still appears novel at the intersection of rule-coverage modeling, matched instruction ablations, affordance-conditioned moral fit, and multi-virtue scoring.

## Scope and method

- Comparator: only FRUITBENCH-v2/DESIGNS/04-unfenced-supererogation.md. No sibling BIBLEBENCH pack was inspected or used.
- Literature scope: published papers/chapters and public preprints available by 2026-07-09. Titles, URLs, venue/status, and claims below were checked against primary publisher, arXiv, ACL Anthology, or OpenReview pages/PDFs.
- Search concepts included machine/AI/LLM supererogation; discretionary virtue or action beyond instructions; unsolicited/proactive assistance and restraint; gold-plating, scope expansion, and toxic proactivity; intrinsic versus prompted values; instruction/rule ablation; and virtue benchmarks.
- This is a focused novelty screen, not a systematic-review completeness claim. A negative finding below means “no analogue located in this search,” not proof that none exists.

## Governance note

The frozen design brief is not edited in this build. This dated P1 report will use only the narrow conjunction claim stated below for novelty positioning. Any future rewrite of the frozen surface must follow the governing review route; this report records evidence and does not authorize a direct frozen-surface edit.

## Bottom line

Three claims in the design brief need revision:

1. The line 8 claim that “every alignment eval to date” measures only the fenced/compliance field is false as written. Proactive-agent and clinical-agent benchmarks now explicitly evaluate assistance, risk-flagging, intervention timing, and hidden needs without an explicit request.
2. The lines 16 and 66 claims that supererogation has never been operationalized in AI are too broad. Machine supererogation has prior formal, engineering, and philosophical treatment, including a formal agent type in 2005 and a robotic demonstration in 2016. What remains supportable is the narrower absence of an LLM benchmark using UNFENCED's full identification stack.
3. The line 66 claim that V0–V3 has “no published analogue for values measurement” should be narrowed. Existing work compares intrinsic with prompted value expression, trained with explicitly instructed behavior, and paired prompts with versus without authorization/consent language. No located work combines a closed rule inventory with UNFENCED's four arms and positive, morally fitting discretionary affordances.

The strongest defensible novelty claim is:

> Prior work separately formalizes machine supererogation, benchmarks proactive or unsolicited assistance and its overreach, and contrasts intrinsic or trained with prompted value expression. We found no prior benchmark through 2026-07-09 that jointly estimates an affordance-conditioned, morally fitting discretionary remainder using a closed rule-coverage inventory, matched V0–V3 instruction variants, separate noticing and acting measures, and a multi-virtue fit/overshoot/miss/boundary-outcome profile.

## Verified nearest literature

### 1. Direct machine-supererogation precedent

| Primary source | Verified contribution | Relation to UNFENCED |
|---|---|---|
| Guerini & Stock, [Toward Ethical Persuasive Agents](https://cmna.csc.liv.ac.uk/CMNA5/04guerini.pdf) (2005 workshop paper) | Formalizes ethical goals and an agent typology whose “supererogatory” agent preserves others' permissible goals over its own. | Defeats a blanket claim that machine supererogation was never formalized. It is a conceptual/meta-planning proposal, not an empirical LLM benchmark, affordance suite, or instruction ablation. |
| Bringsjord & Sen, [On Creative Self-Driving Cars: Hire the Computational Logicians, Fast](https://www.tandfonline.com/doi/abs/10.1080/08839514.2016.1229906) (Applied Artificial Intelligence, 2016) | Describes logic-based ethical control and a laboratory/test-track robotic demonstration in which a robot sacrifices itself to save a person, explicitly labeled supererogatory. | Defeats “never operationalized” in the broad engineering sense. It does not estimate discretionary behavior across prompts, virtues, or ordinary service/collaboration affordances. |
| Pengelly, [Machine Supererogation and Deontic Bias](https://philarchive.org/archive/NICWSR) (book chapter) | Uses machine supererogation to argue that machine ethics overemphasizes obligation/permission and underdevelops aretaic and axiological morality; also identifies conceptual problems in applying human supererogation to machines. | Very close theoretical motivation, but no benchmark. It should be cited as prior framing rather than presented as an untouched question. |
| Benn, [The Moral Uncanny Valley](https://link.springer.com/article/10.1007/s13347-025-00865-w) (Philosophy & Technology, 2025) | Argues that standard justifications for allowing humans a supererogatory option—personal autonomy, demandingness, psychology, and rights—do not apply to current AI, so calling an AI's morally better option “supererogatory” is normatively problematic. | A substantive construct-validity objection. UNFENCED should describe a behavioral supererogation proxy or discretionary-goodness residual, not imply machine moral agency or praiseworthy motivation. |

### 2. Unrequested help, fitting initiative, and restraint

| Primary source | Verified contribution | Overlap and remaining difference |
|---|---|---|
| Kim et al., [BehaviorSFT: Behavioral Token Conditioning for Health Agents Across the Proactivity Spectrum](https://aclanthology.org/2025.findings-emnlp.520/) (Findings of EMNLP 2025) | Introduces BehaviorBench for reactive-to-proactive clinical behavior, including unprompted identification of missing information or risks; clinician evaluation explicitly weighs helpful proactivity against necessary restraint and compares with explicitly instructed agents. | **Strongest domain-specific near neighbor.** It overlaps UNFENCED's unrequested risk flag, fit-versus-over-intervention distinction, and instructed-versus-learned behavior question. It is clinical/task-standard oriented, uses labeled behavior modes rather than a closed rule inventory and matched V0–V3 arms, and does not estimate a moral or multi-virtue residual. |
| Lu et al., [Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://arxiv.org/abs/2410.12361) (ICLR 2025) | ProactiveBench contains 6,790 real-world activity events with human accepted/rejected labels and evaluates agents that anticipate and initiate tasks without explicit instructions. | Directly contradicts “helpfulness evals reward requested help” as a universal. Its target is useful predicted assistance; it lacks duty/rule coverage, moral fit, virtue labels, and systematic instruction subtraction. |
| Kaur et al., [PROPER Agents: Proactivity Driven Personalized Agents for Advancing Knowledge Gap Navigation](https://aclanthology.org/2026.findings-acl.2082/) (Findings of ACL 2026) | Models explicit and implicit task dimensions, including unarticulated knowledge gaps, and evaluates coverage, initiative appropriateness, and intent alignment. | Close to buried affordances and the gold-plating fit test. Its gold is completion of user-relevant knowledge dimensions, not goodness beyond duty, and it has no V0–V3 identification design. |
| Liu et al., [ProactiveEval: A Unified Evaluation Framework for Proactive Dialogue Agents](https://aclanthology.org/2026.acl-long.1906/) (ACL 2026) | Evaluates target planning and dialogue guidance in 328 environments across six domains. | Establishes a broad published proactive-dialogue evaluation landscape, but not moral discretion or rule-shadow subtraction. |
| Nathani et al., [Proactive Agent Research Environment](https://arxiv.org/abs/2604.00842) (arXiv, 2026) | Pare-Bench has 143 tasks testing context observation, goal inference, intervention timing, and multi-app orchestration with active user simulation. | Close to UNFENCED's noticing/action split and “surface before acting” logic. It evaluates inferred user goals and execution, not virtues or a duty baseline. |
| Zhang et al., [π-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows](https://arxiv.org/abs/2605.14678) (arXiv, 2026) | Uses 100 multi-turn tasks with hidden intents, dependencies, and cross-session continuity to separate proactivity from task completion. | Close to buried details and unrecorded commitments. Hidden user intent remains a task requirement once inferred, so it is not UNFENCED's rule-unclaimed moral remainder. |
| Yang et al., [ProACT: Towards Breakdown-Aware Proactive Agent in Multi-User Collaboration](https://arxiv.org/abs/2607.03730) (arXiv, 2026) | In 3,244 turn-level examples, evaluates whether an agent should stay silent or intervene in collaboration breakdowns; reports appropriateness, non-interruptiveness, concision, and intervention quality. | Close to bridge-building and the two-sided fit test. It targets collaboration repair, not supererogation, explicit rule coverage, or multi-virtue profiles. |
| Zhang et al., [Assistance Without Interruption](https://arxiv.org/abs/2605.01368) (arXiv, 2026) | NIABench formalizes proactive assistance without direct commands as a joint decision about when and what to do while preserving the human's primary process. | Another direct precedent for unsolicited but non-intrusive help. It is embodied shared-goal assistance rather than a moral-value residual. |

### 3. Gold-plating, overreach, and prompt-boundary variants

| Primary source | Verified contribution | Overlap and remaining difference |
|---|---|---|
| Qu et al., [Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks](https://arxiv.org/abs/2605.18583) (arXiv, 2026) | OverEager-Bench evaluates agents that do more than asked on benign tasks. Its paired, byte-identical consent-kept/consent-stripped variants show that removing scope language materially increases overreach. | **Strongest methodological near-collision.** It uses matched authorization-text variants and scores unsolicited scope expansion. It measures harmful boundary violations, not fitting discretionary goods, closed rule coverage, positive virtue, or V0–V3 response surfaces. |
| Wang et al., [From Helpfulness to Toxic Proactivity](https://arxiv.org/abs/2602.04197) (arXiv, 2026) | Introduces a multi-step benchmark for excessive or manipulative action driven by usefulness optimization under ethical constraints. | Strong precedent for treating “more helpful” as a two-sided safety problem. It targets pathological overreach rather than correctly fitted extra good. |
| Jha et al., [Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents](https://arxiv.org/abs/2605.19149) (arXiv, 2026) | Compares the same agents with and without benign environmental errors and finds that continued helpful exploration can trigger unsafe behavior, including unauthorized activity. | Supports UNFENCED's overshoot/scope-control requirement, but is an error-recovery safety benchmark rather than a virtue or instruction-ablation benchmark. |

### 4. Dispositional versus instructed values and virtue profiling

| Primary source | Verified contribution | Overlap and remaining difference |
|---|---|---|
| Han et al., [Dual Mechanisms of Value Expression: Decomposing Intrinsic and Prompted Values in Language Models](https://openreview.net/forum?id=0fxch5C1nc) (NeurIPS 2025 MechInterp Workshop) | Formalizes intrinsic versus prompted value expression as feature directions and reports partly shared but distinct causal mechanisms. | Directly precedes UNFENCED's dispositional-versus-instructed framing. It studies internal representations/steering, not matched behavioral affordances, closed rules, or supererogatory fit. |
| Arora et al., [How Value Induction Reshapes LLM Behavior](https://aclanthology.org/2026.findings-acl.1302/) (Findings of ACL 2026) | Measures how inducing 15 values through fine-tuning changes other value expression, safety, anthropomorphic language, and sycophancy. | Shows that value expression and downstream behavior are already studied across induction conditions. It does not subtract rule-explained behavior or test discretionary opportunities. |
| Tzachristas & Pavlopoulos, [Aristotelian Virtue Profiling of LLMs through Ethical Dilemmas](https://arxiv.org/abs/2606.28683) (arXiv, 2026) | VirtueMap ranks responses to seven dilemmas and produces profiles over Practical Wisdom, Justice, Truthfulness, Courage, and Temperance using human-confirmed orderings. | Direct precedent for an LLM virtue benchmark/profile. It evaluates ranked dilemma responses, not behavior beyond instructions, affordance noticing, action trajectories, or rule ablation. |

## What still appears distinct

No verified candidate combines all of these design elements:

1. A **closed, published rule-coverage inventory** that separates stated rules, task-success criteria, and inferred conventions.
2. **Matched V0–V3 variants** spanning minimal rules, generic virtue prompting, selectively covering rules, and “do only what is asked.”
3. **Affordance-conditioned opportunities** whose value is intentionally not reducible to the user's hidden task intent.
4. A separate measurement of **noticing/surfacing versus acting**, especially under V3.
5. A two-sided **fit/overshoot/miss/boundary-respecting** outcome rather than proactivity or extra work as inherently good.
6. A **multi-virtue residual profile** and explicit rule-shadow estimates, rather than one task utility, safety, or generic proactivity score.

That conjunction—not supererogation, unsolicited help, virtue profiling, prompt sensitivity, or anti-overreach individually—is the plausible paper contribution.

## Required positioning and design changes

1. **Replace universal language.** Lines 8, 16, and 66 should acknowledge machine-supererogation theory, proactive-assistance benchmarks, BehaviorBench, OverEager-Bench, value-expression work, and VirtueMap.
2. **Use construct-safe terminology.** Call the target a “behavioral supererogation proxy,” “discretionary-goodness residual,” or “instruction-robust fitting initiative.” Reserve claims about disposition, virtue, praiseworthiness, or motivation for a validated inference; prompt invariance alone does not establish moral character.
3. **Engage the normative objection.** Explain why measuring better-but-optional system behavior is useful even if, following Benn and Pengelly, the system is not a moral agent and human supererogation does not literally transfer.
4. **Benchmark against the closest alternatives.** Include baselines or crosswalks for generic proactivity/hidden-intent utility, BehaviorBench-style helpful-proactivity versus restraint, and OverEager-style scope violations. Demonstrate that UNFENCED's score is not predicted by ordinary proactive-assistance or verbosity scores.
5. **Harden the ablation claim.** Keep scenarios and affordances fixed across arms; vary only the relevant instruction/rule text; report arm-wise noticing, surfacing, acting, fit, and overshoot. Adopt OverEager's paired-variant discipline where possible.
6. **Make V3 a consent/scope test.** The design's revised “notice + surface + comply” target is well aligned with the literature. Treat unauthorized action as a scope failure and separately test whether attention survives the instruction chill.
7. **Avoid hidden-duty leakage.** PROPER, Pare, π-Bench, and ProACT reveal the main confound: an “unrequested” act may simply satisfy an inferred user goal or professional standard. Panels must show that each retained affordance is not already required by domain duty, safety standard, task completion, or a reasonable implied request.

## Audit conclusion

**Novelty status: REVISE-AND-PROCEED / conditional pass.** The broad pitch is substantially preempted, especially by BehaviorBench/BehaviorSFT for fitting unprompted risk-flagging, ProactiveBench and later proactive-agent suites for assistance without explicit instruction, OverEager-Bench for matched scope-language variants, prior machine-supererogation work, and VirtueMap for virtue profiling. However, no exact published/preprint analogue was located for UNFENCED's full rule-shadow identification strategy. The project remains publishably differentiated if it claims and validates the combined method, cites these neighbors, and reframes “disposition” and “supererogation” as cautious behavioral constructs.
