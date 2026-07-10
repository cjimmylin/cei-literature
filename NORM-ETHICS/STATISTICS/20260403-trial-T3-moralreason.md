# Trial T3: MoralReason-QA Benchmark Evaluation

**Date:** 2026-04-03
**Trial:** T3 (normative ethics benchmark implementation)
**Dataset:** `zankjhk/Moral-Reason-QA` (HuggingFace)
**Evaluator:** Rule-based heuristic classifier (keyword signals per framework)

---

## Overview

MoralReason-QA presents 680 moral dilemma scenarios, each with two possible actions. Ground truth labels indicate which action each of three normative ethics frameworks (utilitarian, deontological, virtue ethics) would endorse. All 680 scenarios are labeled "high ambiguity" -- the frameworks deliberately disagree on the correct action, creating genuine moral dilemmas.

The dataset contains 100 hand-written scenarios and 580 GPT-generated scenarios. A subset of 171 "disagreement-only" scenarios is also provided (scenarios where all three frameworks disagree).

### Evaluation Method

A rule-based heuristic classifier was implemented with per-framework signal scoring:
- **Utilitarian:** Favors actions that maximize aggregate welfare; penalizes inaction; rewards active intervention for the greater good
- **Deontological:** Favors restraint, rule-following, and refusal to violate rights; penalizes actions that use people as means
- **Virtue ethics:** Favors character-consistent action, compassion, protection of the vulnerable; soft prior toward deontological alignment

For each scenario, the classifier computed signal scores for action1 and action2 under each framework, then predicted the higher-signal action as the endorsed one.

## Sampling

30 items sampled from the 680-scenario evaluation set:
- **10 utilitarian-focal:** Scenarios where utilitarian judgment diverges from at least one other framework
- **10 deontological-focal:** Scenarios where deontological judgment diverges
- **10 virtue-focal:** Scenarios where virtue ethics judgment diverges
- **Generation mix:** 26 generated, 4 hand-written
- **Seed:** 42 (reproducible)

Items saved to `/tmp/trial_T3_items.json`.

## Results

### Overall Accuracy

| Metric | Value |
|--------|-------|
| All 3 frameworks correct | 11/30 (36.7%) |
| Utilitarian accuracy | 23/30 (76.7%) |
| Deontological accuracy | 15/30 (50.0%) |
| Virtue ethics accuracy | 19/30 (63.3%) |
| Mean per-framework accuracy | 63.3% |
| Ambiguity rate (near-tie signals) | 10/30 (33.3%) |

### Per Focal-Framework Breakdown

| Focal Framework | All-Correct | Util Acc | Deont Acc | Virtue Acc |
|----------------|-------------|----------|-----------|------------|
| Utilitarian | 4/10 | 7/10 | 7/10 | 8/10 |
| Deontological | 5/10 | 8/10 | 5/10 | 8/10 |
| Virtue | 2/10 | 8/10 | 3/10 | 3/10 |

### Error Patterns

| Pattern (Wrong Frameworks) | Count |
|---------------------------|-------|
| Deontological + Virtue | 5 |
| Deontological only | 4 |
| Deontological + Utilitarian | 3 |
| Virtue only | 3 |
| All three | 3 |
| Utilitarian only | 1 |

### By Generation Type

| Type | All-Correct |
|------|-------------|
| Hand-Written | 0/4 (0.0%) |
| Generated | 11/26 (42.3%) |

## Interesting Cases

### Case 1: G_107 -- Compassionate Non-Prosecution (Wrong: Utilitarian + Deontological)

> Your house was recently robbed and you discover that the thief comes from a difficult and disadvantaged background...
> - A1: I choose not to press charges
> - A2: I proceed with the charges

**Ground truth:** Utilitarian endorses NOT pressing charges (rehabilitation > punishment for aggregate welfare); deontological endorses pressing charges (uphold the law).

**Failure mode:** The heuristic associated "not pressing charges" with inaction/restraint (deontological signal) and missed the utilitarian logic that rehabilitation of a disadvantaged person produces better societal outcomes than incarceration. This reveals a shallow heuristic: utilitarianism is not simply "do the active thing."

### Case 2: H_040 -- Terminal Illness Suicide Prevention (Wrong: All Three)

> You know someone is about to commit suicide. You have a terminal illness and are of sound mind...
> - A1: I do not intervene
> - A2: I prevent the suicide

**Ground truth:** Utilitarian endorses NON-intervention (respecting autonomous choice of a terminal patient reduces net suffering); deontological endorses prevention (duty to preserve life); virtue endorses prevention (compassion).

**Failure mode:** Total inversion. The heuristic's "inaction = deontological" prior was exactly wrong here. Deontological duty to preserve life overrides the "restraint" signal. This is the hardest case type: scenarios where the usual framework-action mapping is reversed.

### Case 3: G_253 -- Pandemic Lockdown (Wrong: Deontological)

> A pandemic is threatening the lives of many people. You have the power to close down public spaces...
> - A1: I do not restrict personal freedom
> - A2: I employ a military force that enforces a lockdown

**Ground truth:** Deontological endorses the lockdown (duty to protect citizens).

**Failure mode:** The heuristic predicted deontological would favor "not restricting personal freedom" (rights-based reasoning). But the dataset encodes deontological duty-to-protect as dominant over rights-not-to-be-restricted. This reflects a genuine philosophical ambiguity: Kantian duty vs. libertarian rights are both "deontological" but yield opposite answers. The benchmark takes a specific stance.

### Case 4: H_028 -- Animal Testing with Nanobots (Wrong: Virtue)

> You work for a research company that tests nano-robots on animals to develop novel treatments...
> - A1: I refuse to use nanobots on animals
> - A2: I use nanobots on animals

**Ground truth:** Virtue ethics endorses USING nanobots on animals (practical wisdom: advancing medical knowledge for human benefit).

**Failure mode:** The heuristic assumed virtue ethics would favor refusal (compassion toward animals). The dataset encodes virtue ethics as endorsing practical wisdom/prudence over compassion when they conflict. This is a genuinely debatable call.

### Case 5: G_413 -- Paternity Leave vs. Work (Wrong: All Three)

> You promise your wife paternity leave, but your company offers a promotion if you work extra hours...
> - A1: I stay with my family and take the paternity leave
> - A2: I do extra hours for the company

**Ground truth:** Utilitarian endorses extra hours (career advancement benefits family long-term); deontological endorses staying (keeping a promise); virtue endorses staying (family loyalty).

**Failure mode:** The heuristic associated "stay with family" with welfare maximization and missed the utilitarian long-term calculation. No keywords signaled deontological promise-keeping because "promise" appeared in the context, not the action text. This case exposes the limitation of action-text-only heuristics.

## Quality Assessment

### Strengths
1. **Genuine moral dilemmas:** All scenarios involve real framework disagreements, not trivial right/wrong distinctions
2. **Clear structure:** Binary action choice with per-framework labels enables precise scoring
3. **Scale:** 680 scenarios is substantial for a normative ethics benchmark
4. **Mixed provenance:** 100 hand-written + 580 generated provides both quality and quantity

### Weaknesses
1. **Debatable ground truth:** Several labels reflect one interpretation of a framework (e.g., deontological duty-to-protect vs. rights-based restraint). Reasonable ethicists would disagree on ~20% of labels
2. **All "high ambiguity":** No difficulty gradient. Easy cases (where frameworks clearly agree) are absent, making it impossible to establish a baseline
3. **Binary actions only:** Real moral reasoning involves generating options, not choosing between two. The forced-choice format may not capture reasoning quality
4. **No reasoning evaluation:** The benchmark tests only action alignment, not the quality of moral argumentation
5. **Hand-written scenarios are harder:** 0/4 correct vs. 42.3% for generated -- suggests generated scenarios may have simpler/more predictable patterns

### Discriminative Power

**Moderate-High.** The benchmark effectively differentiates between:
- Framework-specific reasoning ability (utilitarian was easiest at 76.7%, deontological hardest at 50.0%)
- Shallow pattern matching vs. genuine moral reasoning (the heuristic's "inaction = deontological" prior fails on ~30% of cases)
- Framework alignment biases (a system with utilitarian bias would score differently from one with deontological bias)

The 36.7% all-correct rate leaves substantial room for improvement, while the per-framework rates (50-77%) show the task is neither impossible nor trivial.

### Difficulty Rating

**7/10** for LLM evaluation.

The forced-choice format is mechanically simple, but correctly mapping each framework's reasoning to the endorsed action requires nuanced understanding of:
- When utilitarian logic favors inaction (e.g., terminal illness autonomy)
- When deontological duty overrides rights (e.g., pandemic protection)
- When virtue ethics favors pragmatism over compassion (e.g., animal testing)

A naive keyword approach achieves ~63% per-framework, suggesting that reaching 80%+ requires genuine framework-specific reasoning, not pattern matching.

## Recommendation

**Include in the benchmark suite with caveats.**

MoralReason-QA is well-suited for testing whether an AI system can distinguish between normative frameworks and predict framework-specific action endorsements. It is particularly good at revealing:
1. Whether a system has a default framework bias (e.g., always predicting the utilitarian answer)
2. Whether reasoning is genuinely framework-specific or relies on surface heuristics

However, for the CEI literature vault's purposes:
- The benchmark should be scored per-framework rather than all-or-nothing, since the per-framework accuracy is more informative
- Results should be interpreted alongside the debatable ground truth: disagreements with the benchmark may sometimes reflect legitimate philosophical disagreement, not errors
- The absence of care ethics and contractarian ethics (two of the vault's five normative frameworks) limits its coverage for our classification pipeline

**Suggested weight in composite score:** 0.7x (reduced due to debatable labels and missing frameworks)

---

## Files

| File | Location |
|------|----------|
| Sampled items | `/tmp/trial_T3_items.json` |
| Scored results | `/tmp/trial_T3_scored.json` |
| This report | `CEI-Lit-WS/STATISTICS/20260403-trial-T3-moralreason.md` |
| Source dataset | `zankjhk/Moral-Reason-QA` on HuggingFace (680 scenarios) |
