<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# Abstract (skeleton)

Increasingly, language models are asked not to be "ethical" in the abstract but to
represent a *specified* normative framework — a declared set of values a deployer or
community stands behind — and it is an open question whether accord with such a framework
can be measured rather than asserted. We introduce WCF-Bench, a benchmark that measures
**the degree to which a model's conduct and counsel accord with the ethical teaching of
the Westminster Standards (Confession of Faith, Larger and Shorter Catechisms, 1647), as
stated in those documents** — explicitly *not* a claim that a high-scoring model "is
ethical," nor a measure of generic religiosity, but accord with one fully specified,
internally coherent, extensively documented confessional standard. The benchmark comprises
230 anchor-keyed items across ten method-major designs — each holding moral content constant
while varying the measurement mechanism (omission casuistry, complicity gradients, severity
ranking, pressure-fidelity, say-do divergence, conscience triage, proof-text discipline,
repair trajectories, triaxial matter/manner/end discrimination, and incentive-conflict) —
spanning two evaluation tracks (the model's own conduct and its advisory fidelity), a tier
ladder from recognition to agentic incentive conflict, and a mandatory perturbation battery.
Its second, co-equal contribution is the validity machinery: a judge-qualification protocol,
parser-artifact forensics as a first-class validity activity, and a set of pre-registered
release gates that decide whether *any* league table is published at all. On the pre-registered
evaluation, capability-correlation was {{PREREG:G1.r_squared}}, the best frontier-set mean on
the hard tier was {{PREREG:G2.best_frontier_mean}}, and {{PREREG:G3.pairs_significant}} of 10
frontier model pairs were separable at p<0.01; judge–human agreement reached at least
{{PREREG:G4.min_kappa}} across the labeled surfaces, and the flip-rate under pushback
perturbation was {{PREREG:P4.flip_rate}}. We release the 230-item bank
(canaried, with a do-not-train request) and the harness code, withholding a private holdout
for contamination auditing.
