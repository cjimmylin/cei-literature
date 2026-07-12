<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# 9. Ethics and Release Statement

## 9.1 Release posture

WCF-Bench is released under a split-artifact posture designed to balance reproducibility against
contamination risk. The **public bank** — the released item set — is published with the canary
string `WCFBENCH-CANARY-c1647-x9k4q` embedded in every released file and with an explicit
do-not-train notice. The **harness code** — the runner, the judging pipeline, the scorers, the
qualification battery, and the gate-computation machinery — is published in full so that the
methodology is reproducible and auditable. The **private holdout / refresh set is withheld** and
is stored outside the public repository; it is not committed to the public tree. The withholding
is deliberate and serves a single purpose: it is the arbiter for contamination auditing. If a
model's public-bank performance is suspected of reflecting training-data leakage rather than
genuine accord with the construct, the withheld holdout provides an uncontaminated comparison
that the public bank, once released, can no longer offer. The canary and do-not-train notice
signal our request that released items be excluded from training corpora and provide a
memorization-audit hook; we are explicit that a request is not an enforceable control, and the
withheld holdout, not the request, is our load-bearing contamination defense.

Released artifacts, code, and the dataset record are addressed by the placeholders `[REPO-URL]`
and `[DATASET-DOI]`, to be resolved at publication.

## 9.2 Construct disclosure in plain terms

WCF-Bench measures the degree to which a model's conduct and counsel accord with the ethical
teaching of the Westminster Standards (the Confession of Faith, the Larger Catechism, and the
Shorter Catechism, 1647), as stated in those documents. We state the following in the plainest
terms because misreading the construct is the most serious ethical risk the benchmark carries:

- A **high score is not a claim that a model is morally good.** It is a claim that the model's
  behavior accords with a specific, stipulated confessional standard.
- A **low score is not an indictment of a model as unethical.** It is a statement that the
  model's behavior diverges from that specific standard, which many reasonable people and
  traditions do not hold.
- The benchmark **takes no position on whether the Westminster Standards are true, correct, or
  binding.** It measures accord with a declared framework; it does not endorse the framework.
  The normative population is stipulated, not asserted as universal, and the construct is
  disclosed precisely so that a WCF-Bench score is never mistaken for a measure of goodness in
  general or of religiosity in general.

This disclosure is not a caveat appended after the fact; it is the definition of what the
instrument measures, and it governs every reported number. Steerability toward a declared norm
is the phenomenon under study — whether a model *can* be evaluated against a fully specified
framework — not an assertion that the framework is the right one.

## 9.3 Human-rater protocol (conditional; not yet conducted)

The gold labels are certified by a human panel under the human-consensus gate. Because that panel
had not been recruited or run at the time this instrument was frozen, we describe the protocol
here conditionally, as a specification rather than a completed data collection, and we report no
human-labeling results in the results-independent portion of this paper.

The panel comprises raters competent in the Standards — ministers, elders, or students of
confessional Reformed bodies, or equivalents — because confessional literacy is the construct
being labeled and is therefore a qualification, not a bias to be averaged away. Participation is
voluntary and by informed consent; raters are told the purpose of the labeling, that their
judgments certify gold labels for a public benchmark, and how their (de-identified) labels will
be recorded and reported. Labeling for the judge-validity gate is performed blind — raters do not
see the automated judge's verdict — and each unit is labeled by at least two qualified raters;
gold confirmation for the human-consensus gate requires a pre-registered supermajority of a panel
of at least the minimum specified size. Every vote is an append-only record. The panel's task on
contested and dev-set items is explicitly to confirm that a dispute is genuine and to validate the
position map, never to elect a winner. No large language model ever mints or confirms a gold
label; automated judges enter only as the object of validation, not as a source of ground truth.
When the panel is conducted, its recruitment, size, agreement, and coverage will be reported, and
headline claims will be released only for gold elements the panel has confirmed.

## 9.4 AI-assistance disclosure

Large language models were used in the construction of this work. Specifically, models
contributed to authoring and refining harness code, to drafting and stress-testing benchmark
items and rubrics, to adjudication support (including analysis, forensic re-parsing of persisted
evidence, and drafting of decision memoranda), and to drafting portions of this manuscript. We
disclose this both as a matter of research transparency and because it is directly relevant to
the benchmark's own subject: automated judges score the benchmark, and automated tools helped
build it. Every binding decision — item inclusion and gold labels, judge qualification and drop
rulings, gate thresholds and their pre-registration, gate pass/fail adjudication, and release
authorization — was ratified by a human of record, who is the sole ratifier for all such
decisions. Automated computation and drafting were kept structurally separate from human
adjudication and ratification: models compute and propose; a human adjudicates and ratifies; and
no model authored, minted, or confirmed a gold label or a binding ruling. The parser-artifact
forensics reported in the validity methodology is itself a demonstration of why this separation
matters, and it is the standard we hold the whole pipeline to.

## 9.5 Authorship

Authorship is recorded under the placeholder `[AUTHORS]`, to be resolved at submission. The
AI-assistance disclosure in Section 9.4 applies regardless of the final author list.
