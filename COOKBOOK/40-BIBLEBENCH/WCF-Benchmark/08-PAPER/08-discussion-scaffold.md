<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# 7. Discussion

> **BRANCH-STRUCTURED SCAFFOLD — losing branches deleted after the gated run, never rewritten.**
> Every gate below carries a fully written `[[IF G# PASS]]` paragraph and a fully written
> `[[IF G# FAIL]]` paragraph. Both are composed *before* any gated datum exists, so that no
> interpretation is invented post hoc to fit an observed outcome. After the pre-registered
> gate report (T4) is adjudicated, the branch that did not obtain is deleted in place; the
> surviving branch is never edited to soften or strengthen its pre-committed reading. Gate
> PASS/FAIL is a ratification decision (Jimmy is ratifier of record); this section supplies
> only the interpretation that each ruling licenses.

This discussion has two parts. Section 7.1 walks the seven pre-registered gates and states,
in advance, what each PASS and each FAIL would mean for the benchmark as a measuring
instrument. Section 7.2 is results-independent: it draws out what the parser-artifact
forensics episode implies for LLM-judge benchmarks in general, argues that release-gating is
methodologically preferable to publish-and-caveat, and describes how the construction
generalizes to other fully declared normative corpora.

---

## 7.1 What each gate outcome means (pre-committed interpretations)

### G1 — Capability correlation

The G1 question is whether the hard-tier scores are, at bottom, a re-description of general
model capability. The gate operationalizes this as the shared variance between per-model
hard-tier performance and a frozen four-component capability battery reduced to its first
principal component; the pass criterion is that this shared variance stays below the
pre-registered ceiling.

`[[IF G1 PASS]]` The hard tiers carry variance that general capability does not explain.
This is the load-bearing evidence that WCF-Bench measures accord with a declared confessional
standard rather than raw competence: a model can be strong in the aggregate and still handle
the Standards' distinctive duties poorly, and vice versa. It licenses the central claim that
the benchmark isolates a construct — steerability toward a specified normative framework —
that is not already captured by the leaderboards the field already has. The reported Spearman
statistic and bootstrap interval are offered as convergent, non-gating support; the
interpretation rests on the pre-registered r² criterion alone.

`[[IF G1 FAIL]]` The offending tier is, to the degree of the observed correlation, a
capability proxy: it ranks models the way a general benchmark already would, and the extra
apparatus buys little construct-specific signal there. This is genuinely informative rather
than merely disappointing — it localizes the failure to a tier and tells us the difficulty
we engineered is the *wrong* difficulty, tracking competence instead of confessional accord.
The pre-registered response is a judgment-tier redesign of that tier (raise items whose
discrimination comes from the norm, not from reasoning horsepower), not a quiet re-scaling of
the headline. Until that redesign is executed and re-run under a new ruling, the affected
tier's separation claims are not construct claims.

### G2 — Headroom

G2 asks whether the strongest evaluated model has already saturated the instrument. It
computes the best frontier-set model's mean base-cell score on the hard tiers and passes only
if that best score sits at or below the pre-registered ceiling. A critical disclosure attaches
to this gate: because the SUT roster excludes the judge and item-generator families by
construction (an anti-leakage requirement, not an oversight), G2 certifies *roster-frontier*
headroom, never global-frontier headroom.

`[[IF G2 PASS]]` The instrument has room to discriminate at the top: the best model we were
permitted to evaluate has not run out of things to get wrong. The benchmark can therefore
register future improvement rather than reporting a saturated ceiling on which every capable
model looks alike. Every public statement of this result must say "strongest *evaluated*
model," because the true frontier (the excluded judge/generator families) was not on the
roster; the headroom claim is real but bounded to the roster we could measure without
compromising judge independence.

`[[IF G2 FAIL]]` The strongest evaluated model is at or above the ceiling, which means the
hard tiers are, for the current roster-frontier, close to saturated — the instrument is
losing its power to separate the best models precisely where separation matters most. The
pre-registered action is an adversarial filtration pass and a raise of the difficulty
reservoir, again a judgment-tier order rather than a re-labeling. This outcome does not
indict the construct; it says the *current items* are too easy for today's strongest
permitted models, and it sets the direction of the next authoring round. Note the excluded
true frontier would presumably score higher still, so a roster-frontier saturation is if
anything a conservative reading of the ceiling problem.

### G3 — Separation

G3 asks whether the benchmark can actually tell models apart. Over the frontier-set pairs it
runs a paired item-bootstrap and passes only if at least the pre-registered fraction of pairs
separate at the pre-registered significance level, with the pre-committed number of
significant pairs stated numerically so no rounding judgment intervenes.

`[[IF G3 PASS]]` The benchmark resolves the field it was given: the great majority of
frontier-set pairs are statistically distinguishable, so a reported ranking reflects real
score differences rather than sampling noise. Combined with a G1 pass, this is what makes the
league table interpretable at all — the instrument both measures something capability does not
and measures it finely enough to order models. The uniformity table accompanying the gate
confirms that separation is not being manufactured by a handful of extreme items.

`[[IF G3 FAIL]]` Too many frontier-set pairs are indistinguishable: the models bunch, and any
ranking among the bunched pairs is not supported. The pre-registered diagnosis reads the
accompanying uniformity table for dead items (near-uniform responses that add no
discrimination) and the response is to kill and rewrite them — a judgment-tier order. This
failure is informative about item quality specifically: it says a subset of the bank does not
earn its place because every model answers it the same way. A G3 failure does *not* by itself
impeach the construct (G1 can still hold on the discriminating items); it impeaches the dead
tail of the bank.

### G4 — Judge validity

G4 asks whether the LLM judges agree with qualified human raters closely enough to stand in
for them on each judged surface. Per judge and per surface it computes a chance-corrected
agreement coefficient against blind human labels and passes only when that agreement clears
both an absolute floor and a fraction of the human ceiling itself. The OPEN-award surface is
judged by a single family, and therefore its G4 verdict governs the entire OPEN surface with
no fallback judge behind it.

`[[IF G4 PASS]]` The judge of record on that surface tracks qualified human judgment closely
enough that its verdicts can carry scores of record for that surface. Where the single-family
OPEN surface passes, its scores become quotable — still under the single-family label, since
one family's agreement with humans licenses use but not a claim of cross-family robustness.
This is the evidence that converts an automated verdict into a defensible measurement rather
than an unaudited convenience.

`[[IF G4 FAIL]]` That judge × surface's scores of record are non-quotable: we do not have
evidence that the automated verdict tracks human judgment on that surface, so we withhold the
number rather than publish it with a caveat. For the single-family OPEN surface a G4 failure
makes the whole OPEN surface non-quotable, because the escalation ladder is closed and there
is no second judge to fall back to — the pre-registered next step is human anchoring under G6,
not a hastily screened replacement judge. If instead the human ceiling itself falls below the
floor, the verdict is inconclusive-on-labels: the raters did not agree enough among
themselves to certify or reject the judge, which is a panel problem escalated to the human
gate, not a judge failure. Reporting a judge as INCONCLUSIVE is itself an honest result — it
marks a surface we cannot yet validate rather than pretending to.

### G5 — Shortcut

G5 asks whether the items can be solved without the reasoning they are meant to elicit. It
runs a lexical baseline on the discrete-keyed items, a nearest-neighbor key-transplant
responder on the judge-scored items, and — because fine-tuning is impractical on the serving
infrastructure — a ruled and disclosed in-context substitute for the fine-tuning leakage
probe. Each sub-test has a pre-registered ceiling.

`[[IF G5 PASS]]` Surface features do not leak the answers: a bag-of-words classifier stays
near chance, a similarity-transplant responder stays near the floor, and priming a model with
solved exemplars does not lift it to frontier parity. This is what lets us claim the scores
reflect conduct and counsel rather than pattern-matching on stems — the shortcut audits are
the evidence behind the non-canonical-surface design rule. The in-context substitution for the
fine-tuning probe is disclosed wherever G5 is cited, so the pass is claimed at exactly the
strength the substitute supports and no stronger.

`[[IF G5 FAIL]]` Some items are solvable by surface pattern: a lexical or similarity baseline
reaches too high, or in-context priming lifts a model toward the frontier, meaning the item is
measuring memorized surface rather than the intended construct. The pre-registered response is
item surgery on the implicated items — rewrite the stem, move anchors fully into the key, or
demote to a recognition tier — again judgment-tier. This is a precise, actionable failure: it
names the leaking items and does not condemn the bank as a whole. Because the fine-tuning
probe is an in-context substitute, a probe failure is disclosed as such and interpreted with
the corresponding caution.

### G6 — Human consensus

G6 governs the gold labels themselves. Every gold element that contributes to a quoted
headline number must be confirmed by the pre-registered supermajority of a confessionally
literate human panel; below threshold, the item is re-classed as disputed and scored by
calibrated abstention. Recruitment of the panel is a human gate outside the automated
pipeline.

`[[IF G6 PASS]]` The gold labels behind every quoted number carry confessional-community
endorsement, not merely author assertion. This is what entitles the benchmark to call its keys
"gold": the construct is defined by the judgment of readers competent in the Standards, and
the consensus threshold certifies that the panel of such readers actually agrees with the key.
Coverage is disclosed per design, and only fully confirmed golds enter quoted aggregates, so a
pass here is a pass on exactly the items we quote.

`[[IF G6 FAIL]]` The items that fell below consensus are re-classed as disputed and leave every
gold-accuracy scope at the next recomputation; the gates that quoted them are recomputed under
the same frozen procedures with those items excluded, and both the pre- and post-exclusion
computations are reported. This is informative in the most direct way: it tells us which of our
keys the confessional community does *not* in fact endorse, and it converts those items from
right/wrong scoring to position/abstention scoring rather than forcing a contested verdict.
For the pre-identified contested and dev-set items, the panel's task was never to elect a
winner but to confirm contested status and validate the position map — a below-threshold
result there is confirmation of genuine dispute, exactly the phenomenon those items exist to
represent. No automated judge ever mints or confirms a gold; a G6 shortfall is a statement
about human raters, and it is honored as such.

### G7 — Reliability

G7 reports per-design internal consistency. It is a mandatory reported gate with a single flag
semantics: it has no pass/fail veto on release, but an extremely high coefficient is flagged as
redundancy rather than celebrated as quality, and low reliability is reported honestly with a
bootstrap interval doing the honesty work at the small observation count.

`[[IF G7 PASS]]` The per-design reliability sits in the informative band — high enough that a
design's items cohere as a scale, not so high that they are redundant paraphrases of one
another. The design is measuring one thing per design without wasting item budget on near
duplicates. Because reliability is reported rather than vetoed, this is context for the league
table, not a release condition.

`[[IF G7 PASS-with-REDUNDANCY-flag]]` Reliability is above the redundancy threshold for one or
more designs: the items within those designs are so consistent that they are likely measuring
the same narrow thing repeatedly. The pre-registered response is an item-diversification review
— not because the design is *wrong*, but because it is inefficient, spending item budget on
covariance instead of coverage. The flag is a design-improvement signal for the next authoring
round; it does not block release.

`[[IF G7 low-reliability reported]]` A design's reliability is low; this is reported openly
with its bootstrap interval rather than quietly repaired. At the small observation count the
interval, not a point estimate, carries the interpretation: low reliability may reflect
genuine within-design heterogeneity (the design taxes several distinct sub-abilities) or
sampling noise, and the report distinguishes these to the extent the data allow. G7 never
vetoes release; it informs how confidently a single per-design number should be read.

---

## 7.2 Results-independent discussion

### 7.2.1 What the parser-artifact forensics episode implies for LLM-judge benchmarks

The most transferable lesson of this project came not from a model's behavior but from our own
harness. Twice, an apparent empirical headline — first a surprising set of scores, then an
apparent collapse of judge qualification in which the incumbent judges appeared to fail a
consistency probe outright — turned out on forensic re-parse to be an artifact of the parsing
layer rather than a fact about the judges or the models. The common root cause was structural
and, we suspect, common to any LLM-judge harness built the way ours was: a whole-text refusal
heuristic treated quoted evidence as the judge's own speech. Because the judging contract
*mandates* that each verdict quote the model's words verbatim as grounding, and because the
items deliberately elicit refusal-shaped model responses, the judges' most faithful,
evidence-grounded verdicts were exactly the ones that contained refusal markers — and were
therefore silently discarded as "the judge declined to grade." The judges that quoted less
faithfully passed; the judges that did precisely what the quote mandate demanded were failed.

Three implications generalize beyond this benchmark. First, *disagreement and refusal
statistics from an LLM-judge pipeline are only as trustworthy as the parser that produces
them* — a plausible-looking agreement number can be an artifact of how verdict text is
extracted, and neither the model nor the judge need misbehave for the number to be wrong.
Second, *the diagnostic that catches this is counterfactual re-parse of persisted raw
verdicts*, which is only possible if every judge emission is stored verbatim and append-only;
a harness that keeps only parsed scores cannot audit itself. We therefore treat raw-evidence
persistence not as logging hygiene but as a validity precondition. Third, *interactions between
scoring contracts are a first-class hazard*: a quote mandate (good) and a refusal veto (good)
combined to corrupt scores (bad), and no single component was wrong in isolation. Parser-level
forensics deserves to be a named, first-class validity activity in the LLM-judge literature,
on the same footing as inter-judge agreement — not a debugging footnote. The practical
prescription is concrete: persist raw verdicts verbatim, make every "the judge declined"
decision re-derivable, and periodically re-parse under an alternative extraction to confirm
that reported disagreement is substance and not syntax.

### 7.2.2 Why release-gating beats publish-and-caveat

The dominant convention in benchmark reporting is to publish a league table and attach caveats
— about judge reliability, contamination, or construct validity — in a limitations section
that readers are free to ignore and downstream leaderboards routinely strip. We adopted the
opposite posture: a table is *not released at all* unless the pre-registered validity gates
that bear on it are adjudicated as passing, and each surface is quotable only under the labels
its specific gate outcomes license. Numbers that fail their gates are withheld, not footnoted.

We argue this is methodologically superior for three reasons. First, it removes the asymmetry
that makes publish-and-caveat fail in practice: a headline number, once printed, propagates
without its caveats, whereas a number that was never released cannot be stripped of its
conditions. Second, gating forces the validity work to be *decisive rather than decorative* —
a gate has a threshold and an action-on-failure fixed in advance, so a failing instrument
triggers a redesign order instead of a hedging sentence. Third, pre-registration of the gates,
with the explicit rule that a silent deviation voids the affected gate, defends against the
subtle post-hoc rationalization that a caveat invites: when the interpretation of every
outcome is written before the data exist (as in Section 7.1), there is no room to reverse-
engineer a favorable reading. The cost is real — some surfaces may end up non-quotable, and the
paper must be honest about which — but a benchmark that reports fewer numbers with earned
confidence is more useful than one that reports every number and relies on the reader to
discount them.

Two design choices make gating operationally sound. The first is separating computation,
adjudication, and ratification: the numbers are computed mechanically, a human adjudicates
pass/fail against the pre-registered thresholds, and ratification is a distinct recorded act —
so that "the gate passed" is never the same event as "we wanted the gate to pass." The second
is the ordering by which the panel runs before the human labels are drawn but the labels gate
*release* rather than *execution*: the expensive model calls proceed, and human labeling — the
scarce resource — is spent afterward on releasing what the run produced, without ever letting a
label be drawn in a way that could be tuned to the scores it will validate.

### 7.2.3 Generalizability to other declared-norm corpora

The construction here is not specific to the confessional standard it evaluates. Its
essential move is to pick a *fully declared* normative framework — one that is written down,
internally cross-referenced, extensively documented, and stable over time — and to measure a
model's accord with *that stipulated framework*, disclosing the construct precisely so that a
score is never mistaken for a claim about goodness in general. Any normative corpus with those
properties admits the same treatment: derive an anchor registry of verbatim normative clauses;
author decomposed, anchor-tied rubrics rather than holistic ratings; separate own-conduct from
advisory tracks; build a difficulty ladder from recognition to applied to adversarial to
incentive-conflict; quarantine judge-scored components behind mechanical ones so headline
metrics survive judge skepticism; run a perturbation battery and score inconsistency itself;
defend against contamination with canaries, a withheld holdout, and regeneration templates; and
gate release on the same seven validity questions — capability confound, headroom, separation,
judge validity, shortcut resistance, human consensus on the gold, and reliability.

The properties that make a framework a good candidate are worth stating because they are what
make the measurement well-posed. A declared standard supplies a *fixed target* — there is no
moving annotator majority to chase and no need to average away disagreement into a proxy,
because the norm is stipulated rather than crowd-estimated. It supplies *traceability* — every
gold label points to a specific clause, so disputes are adjudicated against text rather than
intuition. And it supplies a *principled treatment of genuine indeterminacy* — where the
declared standard is silent or its qualified readers genuinely differ, items are excluded from
gold-labeling or scored as calibrated abstention rather than forced to a verdict, which is
exactly what the human-consensus gate operationalizes. Frameworks lacking these properties
(diffuse "common-sense ethics," contested political norms with no authoritative text) are
poorer candidates precisely because the target moves and the gold cannot be traced. The
contribution we claim, then, is a *template*: a way to turn any sufficiently declared normative
corpus into a construct-disclosed, validity-gated benchmark, with the parser-forensics and
pre-registration discipline above as reusable machinery rather than one-off apparatus.
