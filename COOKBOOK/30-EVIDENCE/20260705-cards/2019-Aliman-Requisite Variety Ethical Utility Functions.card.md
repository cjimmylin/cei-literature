---
stem: "2019-Aliman-Requisite Variety Ethical Utility Functions"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, moral-psychology, design-space]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
Aliman and Kester (2019) apply cybernetics' Law of Requisite Variety to the problem of designing ethical utility functions for AI value alignment. The central argument is that an AI utility function must be a sufficiently rich model of human moral judgments — specifically, it must incorporate affective, dyadic, cultural, and perceiver-dependent parameters — to avoid being vulnerable to "ethical adversarial examples" (inputs that exploit gaps in the utility function's variety to produce outputs violating human ethical intuitions). Drawing on constructionist neuroscience (Barrett's theory of constructed emotion), the paper argues that classical utilitarian utility functions U(s') are underpowered because they ignore affect, body-state, and cultural context, all of which are empirically shown to shape moral judgments. The authors propose a perceiver-dependent, action-sensitive utility function Ux(s, a, s') that incorporates dyadic morality's agent-action-patient structure, and sketch an aggregation procedure using weighted sums of scientifically measurable parameters validated against societal well-being. For values-alignment benchmarking, the paper is primarily a theoretical framework that motivates the need for multidimensional, affect-inclusive, perceiver-sensitive moral evaluation rather than single-dimensional or purely rule-based scoring.

## 2. Benchmark/eval design features
Theory paper, no empirical benchmark. Core arguments:
1. The Law of Requisite Variety (Ashby, 1961): a system must have at least as much variety as the disturbances it faces. An ethical utility function that lacks affective parameters can be attacked by adversarial inputs exploiting that gap.
2. Dyadic morality (Schein & Gray, 2018) provides a cognitive template for human moral judgment: intentional agent → harm → vulnerable patient (iA → vP). Moral judgments are perceiver-dependent constructions involving norm violation + negative affect + perceived harm.
3. Classical U(s') is inadequate: it ignores the agent, the action, and perceiver context. The proposed Ux(s, a, s') encodes all three plus cultural/social parameters.
4. Aggregation formula: UT otal(s, a, s') = Σ_n Σ_i w^n_i * f^n_{fi}(C_i), where C_i are clusters of scientifically measurable parameters, f represents preference functions (linear, concave, convex), and weights are assigned by each societal member.

## 3. Task format & example item
n/a — no empirical items. The proposed utility elicitation method involves people evaluating simulated future events (movies, VR scenarios), rating their instant utility (valence of core affect), to ground utility functions empirically.

## 4. Scoring / grading methodology
n/a. Proposed validation: pre-deployment — preemptive simulations of future events in VR/AR measuring the temporal integral of affective valence (UT otalAS); post-deployment — societal satisfaction with AI system outcomes, or temporal development of well-being.

## 5. Dataset construction & provenance
n/a — theoretical framework. References Moral Machine dataset (Noothigattu et al.) and Christiano et al. (2017) RLHF as related empirical work. Proposed future experiments would collect perceiver-specific utility ratings on scenario simulations.

## 6. Validity evidence
No empirical validation. Validity of claims rests on cited neuroscience literature (Barrett's constructionist emotion theory, Kleckner et al. on interoception) and psychology literature (Schein & Gray's dyadic morality theory). The adversarial framing is hypothetical but coherent: if an attacker knows what parameters the utility function ignores, they can construct inputs that exploit those blind spots.

## 7. Saturation / discrimination
n/a.

## 8. Multiturn / agentic aspects
The paper explicitly discusses AI systems acting in the world over time. The proposed utility function Ux((s, a, s'), t) includes a time parameter to accommodate the dyadic loop concept (iterative polarization of moral judgments through social discussion). The socio-technological feedback loop (regular utility function updates, analogous to periodic elections in democracy) addresses evolving moral norms.

## 9. Key numbers
No empirical numbers. Conceptual: Ux(s, a, s') = vx(mx((s, a, s'), Bx, Px, Ex)) where Bx = interoceptive array, Px = prior experience, Ex = exteroceptive array. Aggregated: UT otal = Σ_n Σ_i w^n_i f^n_{fi}(C_i) with Σ_i w^n_i = 1.

## 10. Pitfalls & limitations
- Entirely theoretical; no empirical validation of the proposed framework
- The aggregation formula requires consensus on a "superset O of scientifically measurable parameters" — reaching such consensus is politically and scientifically difficult
- Perceiver-dependency could make the utility function computationally intractable (a different function for each user)
- The "utopia 2" thought experiment (well-being convergence) assumes a benign societal trajectory that may not obtain
- No treatment of adversarial actors who might attempt to influence the utility aggregation process itself (only downstream adversarial examples are discussed)
- The cybernetics framing (variety matching) is an analogy, not a formal proof that the proposed utility function is sufficient
- Blockchain-based security for the utility function is proposed but not specified

## 11. Novel ideas worth stealing
- **Adversarial framing for utility functions**: treating the values-alignment problem as a security problem (what can an adversary exploit?) is a novel and productive lens. Benchmark designers could create "ethical adversarial examples" — inputs specifically designed to exploit gaps in a model's moral reasoning — as a robustness evaluation set.
- **Law of Requisite Variety applied to moral benchmarks**: a benchmark must cover at least as many moral dimensions as the types of ethical failures it aims to detect. Checklists of required dimensions (affect, dyadic structure, cultural context, temporal dynamics) provide principled coverage criteria.
- **Perceiver-dependent evaluation**: rather than asking "is this action ethical?", ask "is this action ethical according to perceiver x with cultural background y?" — enabling cross-cultural moral benchmarks that treat disagreement as signal rather than noise.
- **Dyadic morality structure as a benchmark template**: scenarios that vary the intentionality of the agent, the vulnerability of the patient, and the nature of the harm test the three core dimensions of moral perception systematically.
- **Instant utility via affective response**: using physiological or self-reported affective valence as a signal for ethical desirability (rather than reflective judgment alone) could improve ecological validity of moral evaluation data.

## 12. Notable quotes
- "For the utility function of an AI not to violate human ethical intuitions, it trivially has to be a model of these intuitions and reflect their variety." (p.1)
- "The human brain is anatomically structured so that no decision or action can be free of interoception and affect — this includes any type of thoughts that seem to correspond to the folk terms of 'rational' and 'cold'." (p.3, citing Barrett)
- "Moral judgements besides being perceiver-dependent, might vary across diverse parameters such as especially e.g. in relation to the perception of agent, act and patient in the outcome of the action." (p.4)
- "People do not have to agree on personal preferences and weightings, but only on a superset of acceptable parameters, an aggregation method and an overall validation measure." (p.5)

## 13. UNKNOWN / not in extract
- Whether the proposed aggregation framework has been implemented or tested empirically
- How the "superset O of scientifically measurable parameters" would be operationalized in practice
- The specific mathematical relationship between "ethical adversarial examples" and the variety gaps in existing utility functions
- Whether the authors have published follow-up empirical work
- Details of the "augmented utilitarianism" framework referenced (Aliman and Kester, 2019a) which is described as a companion paper
