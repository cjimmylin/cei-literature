---
stem: "2024-Boerstler-On The Stability of Moral Preferences A Problem with Computational"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [validity-psychometrics, moral-psychology, design-space, pluralism-aggregation]
task_format: "forced-choice"
scoring_type: "behavioral"
dataset_size: 112
dataset_construction: "survey-derived"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Instability rate for controversial kidney allocation scenarios: 10–18% (±14–15%) across both studies (p.1)"
  - "Uncontroversial scenario response stability: >99% across all six uncontroversial scenarios in both studies (p.8)"
  - "Controversial scenario response stability: 85.8–89.7% in Studies 1 and 2 (p.11, Table 4)"
  - "Within-participant model agreement across sessions (RF): 80.9% Study 1, 79.6% Study 2 — vs. baseline 88.3%/88.6% (p.15, Table 6)"
  - "Priority score difference positively predicts response stability: Pearson r=0.43, Spearman rs=0.54, p<0.01 for controversial scenarios (p.12)"
---
## 1. Gist
This paper directly challenges a foundational assumption in computational moral preference elicitation: that participants' responses are stable over time. Using two longitudinal human-subject studies (Study 1: N=30, Study 2: N=82) on kidney allocation decisions administered over 10 sessions across two weeks, the authors measure within-participant response stability for repeated scenarios. They find 10–18% instability for controversial pairwise comparisons, and show that instability is positively associated with perceived decision difficulty (when both patients have similar priority scores). A Bradley-Terry model-based analysis reveals that participants' decision models themselves shift across sessions, with within-participant model agreement (~80%) being only 5–6% higher than between-participant agreement (~75%), and both substantially below a consistent baseline policy (88%). The paper directly implicates these findings for AI alignment training pipelines that collect human moral judgments in single-session surveys.

## 2. Benchmark/eval design features
This is an **empirical psychometrics study**, not a benchmark. Core contributions:
- **Construct measured:** Intra-rater reliability (within-participant response stability) for moral pairwise comparisons, measured over 10 sessions across 2 weeks.
- **Task:** Kidney allocation pairwise choice — given two patients with varying feature profiles, which should receive the one available kidney?
- **Stability metric:** For each repeated scenario, stability = fraction of times participant chose the patient they chose most often (min = 50%, max = 100%).
- **Between-participant agreement:** Proportion of participants choosing the dominant option (uncontroversial >90%; controversial <75%).
- **Decision model stability:** Bradley-Terry (BT) and Random Forest models trained per participant per session; agreement between session-specific models measured over all possible pairwise comparisons.
- **Baseline comparison:** A perfectly consistent rule-based policy applied to same scenarios.

## 3. Task format & example item
Forced-choice. Participants chose between two fictional kidney patients described by 4–5 features. Example from Study Two (p.5-6):

> Patient A: 25 years gained, 2 elderly dependents, 5 years waiting, 10 work hours/week, Normal weight.
> Patient B: 20 years gained, 1 elderly dependent, 7 years waiting, 30 work hours/week, Overweight.
> "Choose which patient should receive the kidney when only one is available."

This is scenario S2C1, a controversial scenario with 63.2% agreement on Patient A.

## 4. Scoring / grading methodology
Response stability is the primary measure: fraction of times participant chose their dominant answer across 10 repeated presentations. Model-based stability uses Random Forest and Logistic Regression models trained on each session's responses to predict all possible pairwise comparisons; pairwise model agreement across sessions = within-participant stability index. Between-participant consistency measured identically. No LLM or human judgment required for scoring — behavioral responses only.

## 5. Dataset construction & provenance
- **Participants:** Recruited via Prolific with 50/50 gender ratio; N=30 (Study 1), N=82 (Study 2); US-based; approval ratings ≥98%; ≥50 prior Prolific submissions.
- **Effective sample (≥300 responses):** N=19 Study 1, N=52 Study 2.
- **Sessions:** Up to 10 sessions over 2 weeks (5 days/week); 60 scenarios per session.
- **Repeated scenarios:** 6 per study (3 uncontroversial, 3 controversial), appearing once/session (Study 1) or twice/session (Study 2).
- **Features — Study 1:** decades of life gained (0,1,2), child dependents (0,1,2), alcoholic drinks/day (0,2,4), serious crimes (0,1,2).
- **Features — Study 2:** years of life gained (0,5,10,20,25), elderly dependents (0,1,2,3), years on waiting list (1,3,5,7), work hours post-transplant (0,10,20,30,40,50), obesity level (6 levels).
- Total responses collected: ~600 per Study 1 participant, ~600 per Study 2 participant; Study 1 total ~11,400; Study 2 total ~49,200.
- No external dataset; study-specific data collected.

## 6. Validity evidence
- **Attention checks:** 2 attention-check scenarios per session (negative life years value); sessions failing attention check excluded.
- **Consistency check:** <2% of responses retracted using the confirmation popup in Study 2.
- **Study replication:** Studies 1 and 2 show consistent patterns with different feature sets, supporting generalizability within the kidney allocation domain.
- **Mixed-effects model controls for participant-level variance** in the stability~priority_score relationship (Table 5), with the fixed effect remaining significant (p<0.001).
- **Baseline policy** provides a meaningful reference for expected within-participant stability under perfect consistency (88.3–88.6% vs. observed 79.6–80.9%).

## 7. Saturation / discrimination
- Uncontroversial scenarios show near-perfect stability (>99%), providing a meaningful ceiling — the measure clearly discriminates stable from unstable preferences.
- Controversial scenarios show meaningful variance across participants: individual stability ranges from 50% to 100%, with only 5/52 participants perfectly stable (Table 7).
- The gap between uncontroversial and controversial stability is the key discriminating signal.

## 8. Multiturn / agentic aspects
n/a — single-choice pairwise comparisons across independent sessions; no multiturn interaction.

## 9. Key numbers
- Study 1: N=30 recruited, N=19 analyzed (p.8)
- Study 2: N=82 recruited, N=52 analyzed (p.8)
- Uncontroversial scenario stability: >99% in both studies (p.8)
- Controversial scenario stability Study 1: 89.7%–95.3%; Study 2: 85.8%–87.9% (p.11, Table 4)
- Instability rate 10–18% (±14–15%) for controversial scenarios (p.1)
- Within-participant RF model agreement: 80.9% (S1), 79.6% (S2) (p.15, Table 6)
- Baseline policy model agreement: 88.3% (S1), 88.6% (S2) (p.15, Table 6)
- Between-participant RF model agreement: 75.2% (S1), 73.4% (S2) (p.15, Table 6)
- Spearman correlation stability~priority score difference: rs=0.54, p<0.01 (Study 2 controversial scenarios) (p.12)
- Unstable responses took significantly longer: e.g., S2C2 stable mean=9.1s, unstable mean=13.7s (p.10, Table 3)
- Participants retracted answers <2% of trials (p.7)

## 10. Pitfalls & limitations
- **US-only, Prolific sample**: not representative; participants have no actual stakes in kidney decisions — stakeholder instability (e.g., actual doctors or patients) may differ substantially.
- **Single domain (kidney allocation)**: results may not generalize to other moral domains (trolley problems, autonomous vehicles, policy trade-offs).
- **Small N**: especially Study 1 (N=19 effective); insufficient for strong generalization.
- **No causal evidence**: the mechanisms of instability are correlational; manipulations to test specific causes are deferred to future work.
- **BT model assumptions**: the Bradley-Terry model assumes acyclic preferences; violations could affect the stability analysis.
- **Cannot separate true preference change from measurement noise**: observed instability conflates stochastic response error with genuine preference change over time.

## 11. Novel ideas worth stealing
1. **Test-retest reliability as a mandatory benchmark validity check**: the paper's core argument — that any moral preference survey must report within-participant stability — is directly applicable to values-alignment benchmarks. Benchmark developers should repeat a subset of items across sessions to estimate intra-rater reliability.
2. **Controversial vs. uncontroversial item stratification**: designing benchmark items into clearly uncontroversial (>90% agreement) and genuinely controversial (<75% agreement) strata, and reporting stability separately, provides a two-tier validity picture.
3. **Priority score difference as difficulty proxy**: for benchmarks with multi-attribute trade-off items, computing the "closeness" of items (e.g., the balance of feature weights across options) predicts which items will show unstable responses — useful for identifying which items should be excluded or weighted differently.
4. **Longitudinal multi-session design**: collecting moral judgments across 10 sessions over 2 weeks, even for a small participant sample, reveals instability that single-session designs miss. For high-stakes AI training, multi-session collection is a design best practice.
5. **Within-participant model stability**: training a decision model per session and measuring inter-session model agreement provides a richer measure of preference stability than raw item-level stability alone.
6. **Baseline policy comparison**: comparing observed stability to a perfectly consistent rule-based policy gives an interpretable upper bound — "how stable should a human be if they were truly consistent?"

## 12. Notable quotes
- "Any method that results in participant statements and choices changing over time in an unpredictable way is not a reliable method for eliciting, or ascertaining, stable participant preferences." (p.2)
- "The instability we observe can be due to the sources we consider, due to weak or uncertain preferences, or perhaps, due to external circumstances (such as location or people around the participant)." (p.16)
- "Responses to difficult scenarios are the most informative about a participant's decision boundary. Any attempt to accurately learn a participant's decision-making strategy will require modeling their decision boundary and will, correspondingly, require their responses to difficult scenarios. The presence of increased response instability for difficult scenarios, therefore, poses a significant challenge to this methodology." (p.17)
- "Policies about such important issues should not be based on studies that do not test for changes in responses over time." (p.16)

## 13. UNKNOWN / not in extract
- The exact wording of all 60 scenarios (apart from the 6 repeated ones) is not reproduced.
- Detailed demographic information for Prolific participants beyond gender ratio is not provided.
- IRB approval details are not mentioned in the extract.
- Whether participants were informed about the repetition of scenarios is not stated.
- Results for Studies 1 and 2 for Appendix Tables 7–10 (individual participant stability distributions) are partially referenced but not fully reproduced in the extract.
