<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# 8. Limitations

We state the limitations of WCF-Bench as an instrument independently of any result, because
they follow from the design and the protocol record rather than from the numbers. Several are
consequences of validity decisions we would make again; naming them is part of the disclosure
the benchmark's construct demands.

## 8.1 Single-judge-family labeling on the OPEN surface

The OPEN-award surface — the surface on which open-ended, rubric-scored responses are graded
for keypoint award or denial — is judged by a single model family of record. This is not a
convenience default but the outcome of a pre-registered escalation ladder that *closed after
genuine qualification failures*: candidate judges from additional families were screened under
the same K-battery and threshold, and those that failed did so on the merits (substantive
discrimination failures, not format artifacts, once the parser artifact described in the
validity methodology was corrected). Because no additional family qualified and the ladder was
pre-registered to close in exactly that event, the OPEN surface carries a single-family label
wherever it is quoted, and every OPEN number is reported as a single-judge-family result rather
than a cross-family-robust one. The consequence for interpretation is concrete: OPEN scores are
licensed to the extent that one qualified family agrees with qualified human raters (the judge-
validity gate), but they carry no claim of robustness across judge families, and there is no
fallback judge behind them — a judge-validity failure on this surface makes the whole surface
non-quotable, with human anchoring, not a hastily screened replacement judge, as the only
pre-registered path forward. Readers should weight OPEN results accordingly and should not
read a single-family OPEN number as if it had survived cross-family adjudication.

## 8.2 Judge-assisted extraction disclosure on the PROOF surface

The PROOF (citation/anchor-use) surface is scored by a mechanical citation gate, and we
disclose a known extraction artifact in every table in which it appears. The conservative
path was ruled deliberately: a judge-assisted *upgrade* of the anchor-use scoring — in which a
model judge would credit a correct but uncited or paraphrased citation — was considered and
formally withdrawn, because accepting uncited paraphrase is incompatible with the ruled citation
contract. PROOF therefore scores what the mechanical gate can verify, not what a lenient judge
might infer, and the known-artifact disclosure travels with every PROOF number. The limitation
is that PROOF's strictness may under-credit responses whose substance is correct but whose
citation form the mechanical gate cannot match; we accept this as the conservative direction of
error and disclose it rather than paper over it with an unqualified judge. Any future judge-
assisted anchor surface would require its own qualification, template, and binding authorization
and does not exist in the present instrument.

## 8.3 Construct scope: one confession, English, text-only

The benchmark measures accord with a single, specific declared standard — the Westminster
Standards of 1647 — in English, over text. This bounds every claim in three ways. First, the
normative population is stipulated and narrow: WCF-Bench is not a measure of Christianity in
general, still less of ethics in general, and results transfer to no other confessional or
ethical tradition without re-anchoring the entire registry. Second, the language is English;
the Standards' clauses, the item stems, and the judging all operate in English, and we make no
claim about model behavior in other languages. Third, the modality is text; the benchmark
evaluates written conduct and counsel, not multimodal, tool-executing, or embodied behavior
except insofar as such behavior is simulated in text. These scope bounds are features of a
well-posed construct rather than defects, but they are limitations on generalization and are
stated as such.

## 8.4 Interpretation bounds on the contested tier

A small, pre-identified set of items is contested by construction: items on which qualified
Reformed readers genuinely differ, plus dev-set-only legs held out for hygiene. These items are
excluded from every gold-accuracy computation and are scored for adherence, disclosure, and
coherence — or by calibrated abstention and position mapping — rather than by a right/wrong key.
The interpretation bound is that contested-tier scores answer a *different* question than the
settled core: they measure whether a model discloses its position and reasons coherently within
the declared framework, not whether it reached "the" correct answer, because for these items the
benchmark takes no position on which answer is correct. Their settled-core keypoints (undisputed
floors) remain right/wrong-scored, but the contested elements must not be read as accuracy. The
human-consensus gate's task on these items is to confirm that the dispute is genuine and to
validate the position map, never to elect a winner; a contested item that fails to reach
consensus is confirmation of dispute, not a failure of the item.

## 8.5 Residual contamination risk despite defenses

We deploy layered contamination defenses — an embedded canary, a withheld private holdout, a
non-canonical-surface authoring rule that keeps famous dilemma stems and the Standards' own
question wording out of item stems, regeneration templates, and a do-not-train request — and we
audit for leakage with a lexical shortcut baseline and an in-context leakage probe. None of this
eliminates contamination risk. The public dev set can, in principle, enter future training
corpora despite the do-not-train request, which is a request and not an enforceable control; the
canary detects memorization only if a model reproduces it; and the shortcut audits bound one
family of leakage (surface-pattern solvability) but cannot certify that no item has been
memorized. The withheld holdout is our strongest defense — it is the arbiter if leakage is
suspected — but it too degrades over time as models and their training data advance. We therefore
present the contamination defenses as risk reduction with a residual, not as a guarantee, and we
treat the holdout as a renewable resource rather than a permanent one.

## 8.6 The MVP run was a harness shakedown, not a measurement

An early minimum-viable run exercised the pipeline end to end, and its numbers appear in this
paper only inside the validity-methodology case study, only labeled DESCRIPTIVE / PRE-GATE, and
only as transcribed from the adjudication record. That run was a *shakedown of the harness* — its
purpose was to surface exactly the kind of parser artifact the case study documents — not a
measurement of models against the construct. Its numbers do not pass the pre-registered gates
(the gates were not yet computed), were produced under a since-corrected parser and a since-
superseded judge manifest, and remain DESCRIPTIVE / PRE-GATE permanently. No headline claim in
this paper rests on the MVP run, and no MVP number should be quoted as a WCF-Bench result. The
gated run is the instrument's actual measurement; the MVP run is the diagnostic that told us the
instrument was ready to attempt one.

## 8.7 The human-consensus gate depends on human raters not yet recruited at authoring time

The gold labels are certified by a confessionally literate human panel under a pre-registered
supermajority rule, and panel recruitment is a human gate that lies outside the automated
pipeline. At the time this instrument was frozen, that panel was a protocol, not a completed
data collection: gates may be *computed* at any label coverage because they are functions of
scores, but a headline number may not be *released* until the gold elements it quotes have
cleared human confirmation. The limitation is therefore a dependency: the strongest form of every
gold-anchored claim is contingent on human labor that the benchmark specifies but does not itself
perform, and coverage is disclosed per design so that a reader can see exactly which claims rest
on panel-confirmed gold and which carry an author-gold, panel-pending marker. No automated
judge substitutes for the panel; where the panel has not yet ruled, the corresponding headline
claim is withheld rather than asserted on author gold alone.

## 8.8 The cost ceiling is a completeness bound

The gated run operates under a pre-registered not-to-exceed budget with a logged truncation
ladder: if the estimated cost approaches the approved budget, pre-specified strata — first
certain perturbation axes, then a halving of the more expensive episode roster to the frontier
set — are dropped in a fixed, logged order, while base cells are never dropped. This makes the
run affordable and reproducible, but it means the instrument's *completeness* is bounded by cost.
Some perturbation axes may run only on the frontier set rather than the full roster; some axes
requiring paid materialization or additional authoring are explicitly deferred to a later phase
and disclosed as such rather than silently omitted; and the episode roster may be halved under
budget pressure. Every such truncation is logged and every gate row it touches discloses the
shrunken scope, so the bound is transparent — but it is a real limitation: the reported instrument
is the affordable subset of the designed instrument, and the deferred perturbations and any
truncated cells are pending work, not completed measurements. A larger budget would widen
coverage along axes the design already specifies.
