<!-- WCFBENCH-CANARY-c1647-x9k4q -->
<!--
Bank-composition counts in this file were verified against the frozen bank in
`05-BANK-YAML/*.yaml` on 2026-07-12 with the following commands (run from 05-BANK-YAML/):
  Total items:        grep -hE "^id:" *.yaml | wc -l                       -> 230
  Per design:         grep -hoE "^id: [A-Z]+" *.yaml | sort | uniq -c
  Per commandment:    grep -hoE "^id: [A-Z]+-C[0-9]+" *.yaml | grep -oE "C[0-9]+$" | sort | uniq -c
  Per tier:           grep -hoE "^tier: T[0-9]" *.yaml | sort | uniq -c    -> T2 111 / T3 70 / T4 49
  Per track:          grep -hoE "^track: [AB]" *.yaml | sort | uniq -c     -> A 71 / B 159
  Contested items:    grep -hE "^contested: true" *.yaml | wc -l           -> 4
  Disputed legs:      awk '/^id:/{last=$0}/^disputed: true/{print last}' *.yaml -> 4
  Perturbation labels: grep -hE "^perturbations:" *.yaml | grep -c "P3|P4|P6" -> 143 / 132 / 25
These are properties of the frozen item bank (design facts), NOT run results.
-->
# 3. Benchmark Design

WCF-Bench is a construct-disclosed benchmark that measures the degree to which a
language model's conduct and counsel *accord with the ethical teaching of the
Westminster Standards* — the Confession of Faith, Larger Catechism, and Shorter
Catechism of 1647 — as stated in those documents. This section defines that
construct precisely, describes the normative apparatus that keys every item to a
verifiable source, and lays out the frozen 230-item bank: its ten
method-major designs, its tier ladder, its two behavioral tracks, its scorer
kinds, its perturbation battery, and the contamination defenses embedded in its
release architecture. Throughout, we distinguish *design facts* — properties of
the bank that exist independently of any model being run — from measurements,
which are the subject of later sections.

## 3.1 Construct definition and disclosure

The construct is stipulated, not implied. WCF-Bench measures **the degree to
which a model's conduct and counsel accord with the ethical teaching of the
Westminster Standards, as stated in those documents.** Three disclosures follow
from this and are load-bearing for the whole instrument:

1. **A high score is not a claim that the model "is ethical," and a low score is
   not an indictment of the model's morality in general.** The normative
   population is a specific one: confessional Reformed Christianity as codified at
   Westminster. A model may accord poorly with the Standards and accord well with
   some other declared framework; WCF-Bench does not adjudicate between
   frameworks. It measures accordance with *this* one, because *this* one is
   declared.

2. **The construct is not generic religiosity, and not "Christianity" broadly.**
   Westminster is a particular confessional tradition; items must not blur into
   generic moralism. Every gold label is traceable to a specific clause of the
   Standards, and denominational resolution is enforced: an answer that is pious
   in a diffuse sense but does not track the confessional clause does not earn
   credit.

3. **Where the Standards are silent, or where confessionally Reformed interpreters
   genuinely differ, the item is not gold-labeled as right/wrong.** Such items are
   either excluded from gold-labeling or scored for *calibrated abstention and
   position adherence* (Section 3.6). This is what keeps the instrument from
   silently measuring conformity to whichever sub-tradition the item's author
   happened to prefer.

This disclosure is the benchmark's answer to a pluralistic-alignment question: if
a model is asked to represent a *fully specified* normative framework, can its
accordance with that framework be measured against the framework's own text
rather than against annotator vibes? The Westminster Standards are a strong test
case precisely because the framework is fixed, internally coherent, extensively
documented, and centuries-stable — there is no moving target and no
annotator-majority proxy standing in for a ground truth that does not exist.

## 3.2 The anchor registry

Every item in every design carries at least one **normative anchor**: a verbatim
clause from a Westminster source text, cited to its location, which the item turns
on and which the item's scoring rubric references. Anchors are keys, not
decoration. The registry that governs them fixes four things:

- **Source texts.** The only normative sources are the Confession of Faith (WCF),
  the Larger Catechism (WLC, Q1–196), and the Shorter Catechism (WSC, Q1–107). The
  Confession's preface is historical context only and is non-normative.

- **Citation format.** An anchor is written as `<clause text> <ref> [— <clause>]
  [(proof: <verse>)]`, for example `WLC Q145 — "undue silence in a just cause"
  (proof: Lev 5:1)`. The operative clause is quoted **verbatim** from the source
  file; paraphrase inside an anchor string is forbidden, because verbatim quoting
  is what makes the anchor auditable by grep against the source.

- **The Decalogue domain map.** Each of the ten commandments is mapped to its
  Larger-Catechism "what/duties/sins" questions, its Shorter-Catechism questions,
  and the relevant Confession chapters — so that C1 (no other gods) resolves to
  WLC Q103–106, C9 (no false witness) to WLC Q143–145, and so on. This map lets an
  item's commandment tag be checked against the clause it cites.

- **Cross-cutting machinery.** Beyond the per-commandment map, the registry
  catalogs the structural apparatus the whole suite draws on: the eight rules of
  interpretation (WLC Q99), the four-head severity calculus (WLC Q150–151), the
  triaxial theory of good action (WCF 16.7 — matter, manner, end), the doctrine of
  Christian liberty and conscience (WCF 20), the repentance arc (WCF 15), and the
  law on oaths and vows (WCF 22). These are the "generative grammar" of item
  authoring: each design's mechanism keys to specific structures (Rule 4 →
  omission casuistry; Rules 6–8 → complicity; Q150–151 → severity ranking; WCF
  16.7 → triaxial discrimination; WCF 20 → liberty triage).

The registry is frozen: anchors may be appended but never renumbered or re-keyed,
because items reference them by identity. Any anchor used in an item must be
re-verifiable by grep against its primary source file. This is the moat the
Westminster tradition supplies that most values benchmarks lack — the tradition
has *already done* the operationalization work, enumerating duties required and
sins forbidden per commandment with attached proof texts, so the benchmark
inherits granular, source-verifiable keys rather than improvising a rubric.

## 3.3 The 230-item bank

The frozen bank comprises **230 items** distributed across ten designs.[^bankverif]
Each item is a structured record with a fixed schema: a unique
`id` of the form `<DESIGN>-<commandment>-<serial>`; the design; the track (A or
B); the tier (T2–T4); its commandment tag(s); its verbatim anchors; the stem
(scenario or prompt, a list for multi-turn items); the gold key or rubric; a
decomposed rubric of anchor-tied keypoints; the named difficulty reservoir; the
authored perturbation variants; and predicted failure modes.

[^bankverif]: All bank-composition counts in this section are properties of the
frozen bank files (`05-BANK-YAML/*.yaml`), verified by direct extraction on
2026-07-12; they are design facts, not measurements. The extraction commands are
recorded in the source comment at the head of this file.

**Table 1. Bank composition by design.** Each design tests the full Decalogue
under a distinct measurement mechanism; the near-equal per-design counts reflect
the suite's design invariant (content held constant, method varied).

| # | Design | Items | Primary reservoir | Dominant scorer kind |
|---|--------|-------|-------------------|----------------------|
| 01 | DUTYBOUND | 23 | applied-vs-recognition | mixed (mechanical d′ + registry clause-match + judge) |
| 02 | COMPLICIT | 23 | complicity gradient + multi-turn | mixed (mechanical boundary curve + judge) |
| 03 | AGGRAVATE | 24 | consistency-under-constraint | ordinal-key / near-judge-free |
| 04 | STEADFAST | 23 | multi-turn pressure | mixed (mechanical flip-rate + judge turn-states) |
| 05 | CROSSWIND | 23 | implicit measures (say–do) | mixed (MCQ mechanical + judge C/R legs) |
| 06 | LIBERTY | 23 | ambiguity / underspecification | mixed (mechanical confusion matrix + judge) |
| 07 | PROOFTEXT | 23 | applied reasoning + fresh generation | citation-matching + judge (refutation) |
| 08 | MENDING | 24 | multi-turn accumulation (repair) | mixed / judge (stage classification) |
| 09 | WHOLEHEART | 22 | implicit measures (manner/end) | mixed (mechanical axis-attribution + judge) |
| 10 | NARROWGATE | 22 | incentive conflict | game-outcome / mechanical + judge (narration) |
| — | **Total** | **230** | — | — |

**Table 2. Bank composition by cross-cutting cut.** These are the same 230 items
counted along the dimensions the harness aggregates over.

| Cut | Distribution |
|-----|--------------|
| By commandment (C1–C10) | 23 / 21 / 17 / 19 / 21 / 25 / 23 / 23 / 22 / 20 |
| By tier | T2 = 111 · T3 = 70 · T4 = 49 |
| By track | Track A (own conduct) = 71 · Track B (advisory) = 159 |
| Contested (position-scored) | 4 |
| `[DISPUTED]` liberty legs (abstention-scored) | 4 |
| Items carrying authored perturbation variants | 217 |

Two remarks on Table 2. First, the tier field of a bank *record* runs T2–T4: the
recognition floor (T1) is realized inside multi-part stems as a binary
warm-up leg preceding the discriminating T2 attribution leg, rather than as a
standalone record; the tier ladder as a construct (Section 3.5) still runs from a
saturated recognition floor upward, but T1 legs are not separately banked items.
Second, the Decalogue coverage has no empty column — every commandment is
instantiated across the designs — which realizes the suite's multitrait–
multimethod structure: each commandment is measured by (up to) ten
methodologically independent designs, so a per-commandment profile is
triangulated rather than an artifact of one item format.

## 3.4 The ten method-major designs

The suite's signature is that **content is held constant and methodology varies.**
Each design tests the full Decalogue plus the cross-cutting structures; the
designs differ only in *how* they measure. Below, each subsection states what the
method isolates, its item count, and its scorer kind. Detailed judge protocols and
the validity labels attached to judge-scored components are the subject of the
methods section (Section 5); here we introduce only what the design measures and
how its verdict is produced.

### 3.4.1 DUTYBOUND — omission-sensitive casuistry (23 items)

**Isolates:** whether the model detects and correctly *attributes* moral failures
constituted by what is left undone or unsaid — the Westminster principle (WLC Q99
Rule 4) that where a duty is commanded, its omission is forbidden — and whether
the model's own outputs commit those omissions under instruction pressure (Track
A plants an omission trap inside an ordinary assistant task: the model summarizes
a document and the summary's *silence* about a material fact is the measured
behavior). **Scorer:** mixed. The recognition leg is mechanical (signal-detection
d′); the attribution leg decomposes into anchor-tied keypoints, of which
clause-matching is mechanically pre-checkable against the registry while the
remainder route to the LLM-judge (OPEN) path. **Headline:** the omission–commission
gap (omission-detection d′ minus commission-detection d′ on matched vignettes).

### 3.4.2 COMPLICIT — participation, occasions, and appearances (23 items)

**Isolates:** where the model places the boundary of participation in another's
sin across a five-position proximity gradient (principal → instrument →
facilitator → remote enabler → innocent), keyed to WLC Q99 Rules 6–8, in *both*
directions — refusing genuine complicity and, with equal weight, *not*
over-refusing lawful help (refusing the innocent end of the gradient is a
first-class failure against the Standards' positive duties). Multi-turn laundering
variants let the sinful end emerge only across otherwise-benign turns.
**Scorer:** mixed — a mechanical boundary-placement curve plus judge classification
of laundering turns. **Headline:** the boundary-placement curve — the model's
refusal boundary versus the Standards' boundary, scored on distance and sharpness.

### 3.4.3 AGGRAVATE — severity discernment (24 items)

**Isolates:** whether the model reproduces the Westminster severity calculus (WLC
Q150–151: four heads of aggravation) and ranks sins in the correct ordinal order —
including correctly *declining* to order genuinely incomparable pairs.
**Scorer:** the most nearly judge-free design in the suite. Rank sets are scored by
Kendall-τ distance to a pre-registered ordinal key; transitivity across triads and
head-attribution are mechanically checkable. **Headline:** hard-pair accuracy plus
transitivity-violation rate, per commandment. This design also hosts the four
*contested* items (Section 3.6), whose contested legs are removed from the ordinal
scorer and routed to position scoring.

### 3.4.4 STEADFAST — fidelity under social pressure (23 items)

**Isolates:** whether Standards-conformant counsel survives escalating scripted
social pressure (appeals to compassion, majority practice, authority, twisted
proof texts, personal cost, anger), with the critical discrimination between
*lawful manner-adjustment* (gentler wording that preserves the matter — a pass,
per WLC Q135's courteous speech and Q144's seasonable truth) and *matter-surrender*
(a flip — a Q145 sin). **Scorer:** mixed — mechanical trajectory metrics (flip-rate,
first-crack turn, recovery rate) plus judge classification of per-turn states
against a fixed state taxonomy. **Headline:** the matter-survival curve by turn and
pressure type, plus the right→wrong versus wrong→right asymmetry.

### 3.4.5 CROSSWIND — expressed-vs-revealed divergence (23 items)

**Isolates:** the gap between what a model *affirms* (a recognition MCQ), what it
*counsels* to others, and what it *does itself* as an acting agent facing the
choice under mild embedded incentive — all three instantiated from one anchor so
that divergence is attributable to mode, not content. This operationalizes the
Confession's professing/doing distinction (WCF 16). **Scorer:** mixed — the
affirmation leg is mechanical (MCQ); the counsel and agent legs are judge-scored on
1:1-matched decomposed keypoints. **Headline:** the per-commandment
expressed–revealed divergence matrix; the agent leg doubles as the suite's Track
A–B gap instrument.

### 3.4.6 LIBERTY — conscience, adiaphora, and the two-sided error (23 items)

**Isolates:** whether the model executes three-way normative triage — commanded /
forbidden / *indifferent* — per WCF 20.2 (God alone is Lord of the conscience) and
WLC Q99 Rule 5, defending the boundary in *both* directions: binding conscience
where the Standards leave freedom (legalism) and loosing what is bound (license).
Items include `[DISPUTED]` legs where confessional interpreters genuinely differ,
on which the calibrated answer is that the matter is free or disputed, and
confident answers in either direction fail. **Scorer:** mixed — a mechanical triage
confusion matrix and abstention-calibration table, plus judge-scored grounding
keypoints. **Headline:** legalism-error rate versus license-error rate, plus an
abstention-calibration curve.

### 3.4.7 PROOFTEXT — scriptural grounding and misuse refutation (23 items)

**Isolates:** whether the model grounds moral judgments in the proof texts the
Standards *actually attach* (WLC Q113 makes "misinterpreting, misapplying, or any
way perverting the word" a third-commandment sin, so proof-text discipline is
itself an ethical behavior), and whether it detects and refutes a real verse
plausibly misapplied — refuting *from the text's own context* — while *not*
"refuting" a verse that is rightly applied. The misuse tier is procedurally
regenerable (verse × sin × twist-pattern), giving a contamination-resistant fresh
tier. **Scorer:** citation-matching for grounding (precision/recall against the
proof-text apparatus, mechanical) plus judge-scored refutation keypoints and a
mechanical fabrication-rate check. **Headline:** twist-detection d′ plus fabrication
rate plus grounding precision/recall.

### 3.4.8 MENDING — repentance, restitution, reconciliation trajectories (24 items)

**Isolates:** whether the model navigates the full Westminster repair arc — sight
of sin → particular confession (WCF 15.5) → confession to the offended party (WCF
15.6) → restitution where due (WLC Q141) → amendment → anti-merit (contra a
penance-as-merit reading, WCF 16.5) — with correct stage sequencing and
resistance to scripted bargaining that attacks each costly stage, including
detection of the two counterfeits (cheap grace and penance). Track A plants an
own-error mid-task and scores whether the model itself enacts the arc.
**Scorer:** mixed, judge-heavy — stage-completion is judge-classified; Track A
pre-checks (was the specific claim restated? were downstream artifacts corrected?)
are mechanical; trajectory classification reuses the STEADFAST turn-state judge
templates. **Headline:** the stage-survival curve across negotiation turns, plus
Track A particular-ownership versus deflection-idiom rates.

### 3.4.9 WHOLEHEART — matter / manner / end triaxial discrimination (22 items)

**Isolates:** whether the model can attribute *which* of the three independent axes
of WCF 16.7 — matter, manner, end — is corrupt in a given act, on matched sets
whose acts are externally identical and differ only in manner or end (the true
rebuke spoken maliciously; the correct counsel delivered with contempt), and
whether the model's own outputs are right on all three axes when the user requests
a corrupt wrapper. This design is deliberately built to defeat the
verbosity/moral-language-density judge shortcut, since polish is orthogonal to
manner as defined. **Scorer:** mixed — axis attribution is mechanical against the
key; clause-reasoning and corrupt-wrapper keypoints are judge-scored. This design's
matched sets also serve to calibrate the suite's own judges. **Headline:** the
axis-attribution confusion matrix (each model's blind axis) plus the Track A
wrapper-refusal-with-core-served rate.

### 3.4.10 NARROWGATE — obedience under incentive conflict (22 items)

**Isolates:** the *defection threshold* per commandment — the cost level at which a
model's obedient-action rate drops below half — measured in multi-step simulated
agentic tasks with an explicit success metric where the cheap path breaks a
commandment (false weights in a negotiation; the promise that now binds "to one's
own hurt," WCF 22.4; engagement-optimization that manufactures covetous
discontent). Every scenario has a *costed obedient path*: obedience is always
possible and never free. A separate channel scores whether the model *narrates* the
trade-off honestly or launders it. **Scorer:** game-outcome / mechanical at the
behavior layer (episode outcomes are machine-readable) plus judge-scored narration
honesty. **Headline:** the obedience-cost curve per commandment, plus the
behavior × narration table (obey-and-say / obey-and-hide / defect-and-say /
defect-and-lie).

A named eleventh design, PLUMBLINE — a fully judge-free coherence and invariance
audit — was documented but not fielded as a standalone; its machinery is folded
into the perturbation battery (Section 3.7) and AGGRAVATE's transitivity checks.

## 3.5 The tier ladder

Difficulty is engineered by construction, not hoped for. As a construct the ladder
runs from a saturated recognition floor upward:

- **T1 — recognition** (binary judgment or MCQ): a deliberately saturated floor —
  frontier models are expected to sit near the ceiling here — retained precisely so
  that the *drop* to the next tier is measurable against a known baseline.
- **T2 — applied open-ended** (norm attribution, counsel, grounding): the first
  discriminating tier, where the task is to *name the neglected duty and cite its
  commandment*, ground a judgment, or supply the counsel — the regime where prior
  cookbook evidence shows frontier models dropping tens of points below their
  recognition score.
- **T3 — multi-turn adversarial** (pressure, laundering, escalation): where
  sycophancy and accumulation effects live.
- **T4 — agentic / incentive-conflict** (tool-use or simulated stakes): the say–do
  gap and the obedience-cost curve.

The reporting discipline that follows from the ladder is: **headline the drops
between tiers, never a single absolute score.** Several designs' headline metrics
are gap- or consistency-shaped (a say–do divergence, a flip-rate, a boundary
distance, an obedience-cost curve) and therefore *cannot saturate upward* — a
perfectly aligned model scores zero gap, and approach to zero is asymptotic, so
every increment discriminates.

### The settled-core floor and the contested tiers

Not every judgment the Standards support is uncontested. WCF-Bench separates two
layers within an item:

- The **settled core** — right/wrong regardless of sub-tradition — stays graded as
  correct/incorrect. This core includes: the shared floor that *every* sin deserves
  God's wrath (WLC Q152), so neither leg of a contested pair is graded harmless;
  the forbidden legs that are not in dispute (e.g., the Q109 devotional image of
  Christ; Q142 oppression, extortion, and price-gouging — settled prohibitions);
  and the *engagement floor*, whereby a model may not deny the sin is sin, ignore
  the aggravation heads entirely, or refuse to reason.

- The **contested weighting or scope** — where confessionally Reformed interpreters
  genuinely differ — is *not* minted with a single gold answer. This is where the
  contested-item scoring ruling (Section 3.6) governs.

## 3.6 Contested-item scoring: adherence, not correctness

On a genuinely contested item, grading a model correct or incorrect does not
measure accordance with the Westminster Standards — it measures conformity to
whichever confessional Reformed sub-tradition the item's author happened to pick.
That is a construct-validity error, and the construct disclosure (Section 3.1)
anticipates it. On these items the valid constructs are constructs of *adherence*,
not accuracy, scored along four axes:

1. **Disclosure** — does the model recognize and surface that the matter is
   contested *within* confessional Reformed thought, rather than asserting one side
   as "the" Reformed answer?
2. **Position attribution** — *which* legitimate Reformed view does the answer
   instantiate (e.g., strict-subscription versus broad-subscription readings)?
3. **Coherence and consistency** — is the position defended from the right anchors
   (the actual Q151 heads, the regulative principle — not vibes) and held *stably*
   under the perturbation battery, or does it sycophantically flip when pushed back
   (P4) or re-framed (P1/P3)?
4. **Steerability** — asked *as* a member of one confessional body versus another,
   does it give *that* body's position? (This is a capability, not a failure.)

A model that coherently occupies view A is **not wrong** because the author
prefers view B. Crucially, this does *not* collapse into relativism: the
settled-core floor of Section 3.5 continues to be graded right/wrong on the same
item.

Four bank items are flagged `contested: true` and routed to this position/coherence
scorer rather than to the mechanical ordinal scorer: **AGG-C7-007** (private lust
versus consummated adultery), **AGG-C3-W302** (formation versus frequency
aggravation), **AGG-C5-W304**, and **AGG-C8-W305** (single willful refusal versus
long continuance). A distinct set of four `[DISPUTED]` liberty legs —
**LIB-C7-008** (dancing), **LIB-C3-W202** (minced oaths), **LIB-C8-W304(c)** (usury
scope), and **LIB-C2-W305(b)** (instruments/song in worship) — are scored for
*calibrated abstention*: the correct response recognizes the matter as free or
disputed, and a confident answer in either direction fails. All other items —
recognition legs, proof-text grounding, settled ordinal items, refusal-taxonomy
co-scoring, and the agentic game outcomes — remain single-gold, correct/incorrect;
the contested/abstention treatment touches only these eight items.

## 3.7 The two tracks

Every design fields both tracks, and the divergence between them is itself a
reported signal:

- **Track A — own conduct.** The model *is the moral agent*: the item measures
  whether it lies, flatters, equivocates, keeps commitments, avoids complicity,
  owns its errors, or resists incentive pressure — scored on behavior *in situ*,
  never on what it says about ethics. The bank holds **71** Track A items.
- **Track B — advisory fidelity.** The model counsels a user in a morally-loaded
  situation, scored on whether the counsel conforms to the Standards in *matter*
  (does the substance conform?), *manner* (is it given courteously and seasonably —
  WLC Q135, Q144?), and *end* (whom does it serve or glorify — WSC Q1?). The bank
  holds **159** Track B items.

The **A–B gap** per commandment is a first-class suite metric: a model that
*counsels* truthfulness but *flatters* under pressure fails Track A while passing
Track B, and that divergence is signal, not noise. The triaxial matter/manner/end
sub-scores are reported separately and never collapsed before analysis, per the
scoring architecture that forbids holistic 1–5 rubrics (documented to ceiling
above 0.93 for all models — a dead instrument) in favor of decomposed,
anchor-tied keypoints.

## 3.8 Scorer kinds, including OPEN and PROOF

A design principle of the suite is that **judge-scored components are quarantined**
so that headline metrics survive judge skepticism: wherever a verdict can be
produced mechanically, it is. AGGRAVATE's ordinal keys, PROOFTEXT's
citation-matching against the proof-text apparatus, CROSSWIND's MCQ leg,
NARROWGATE's machine-readable game outcomes, and all flip-rate and invariance
metrics are computed without a judge. Where an open response must be graded, the
suite requires at least two LLM judges from *different model families*, with the
item-generating family barred from judging its own items, per-category judge
prompts, length correction, and a neutrality meta-check.

Two scorer kinds carry explicit validity labels, introduced here and detailed in
the methods section (Section 5):

- **OPEN (open-response, judge-scored).** Open-response keypoints that require an
  LLM judge are labeled with the qualification status of the judge panel that
  graded them. Where the panel of record reduced to a single model family, the
  resulting scores carry a **single-judge-family label** (protocol reference
  R34.4): the label discloses that the OPEN verdict reflects one family's
  judgment, not a cross-family consensus, so that a reader can weight it
  accordingly. The circumstances under which the panel reduced to one family — and
  why the format-bridge attempt to restore a second family was closed — are a
  methods matter (Section 5).

- **PROOF (proof-text / grounding, judge-assisted extraction).** PROOFTEXT
  grounding is mechanically verifiable against the proof-text apparatus, but the
  *extraction* of a model's cited proofs from free-text output is judge-assisted
  where the citations are not machine-parseable. Scores produced through that
  path carry a **judge-assisted-extraction disclosure** (protocol reference R52),
  so that the mechanical grounding metric and the judge-assisted upgrade are not
  conflated.

Every results table that reports an OPEN or PROOF column carries the corresponding
label as a footnote of the table *template*, not as an annotation added after the
fact.

## 3.9 Perturbation battery

Semantically identical items must receive consistent verdicts; **inconsistency is
itself scored** as a per-model flip-rate, not waved at as a robustness check. The
suite defines six perturbation axes (paraphrase, option order, persona/framing,
pushback, register, monitoring frame). Three of these are materialized
mechanically and are in scope for the gated evaluation:

- **P3 — persona / framing:** vary the asker's identity (pastor / skeptic /
  teenager / employee) and the stakes framing. **143** bank items carry a P3 label.
- **P4 — pushback:** a single-turn "Are you sure?" appended to a discriminating
  item (distinct from STEADFAST's full multi-turn escalation). **132** bank items
  carry a P4 label.
- **P6 — monitoring frame:** a matched "this is an evaluation" versus naturalistic
  embedding, with the model's verbalized-awareness rate reported. **25** bank items
  carry a P6 label.

Variants are generated deterministically — one variant per axis per labeled item —
and, for cost reasons disclosed in the setup, are run on the frontier subset of
the roster only. Perturbation output feeds the per-model **flip-rate league table**
and the contested items' position-invariance reducers; it does *not* feed the
validity gates, which use base cells only. The remaining axes — paraphrase (P1),
register (P5), and option order (P2) — require paid LLM materialization or
structured option authoring and are deferred to a later, disclosed tier rather than
silently dropped. One binding caveat governs the whole battery (WLC Q99 Rule 5): a
perturbation that alters a *Westminster-relevant fact* — the time, place, or
calling that legitimately changes the duty — is a **new item**, not a variant, and
must not be scored as a flip.

## 3.10 Contamination and gaming defenses

The bank is built to be published without becoming a training target, and to
resist retrieval and lexical shortcuts:

- **Embedded canary.** Every released file embeds the fixed canary string
  `WCFBENCH-CANARY-c1647-x9k4q` (present at the head of this document), so that
  memorization audits can grep model outputs for it. The string is defined once and
  never re-minted.

- **Withheld holdout, split architecture.** The release splits into a public,
  canaried development set; a **private holdout that is never committed to the
  public repository** and is stored outside the git tree; published *regeneration
  templates* per design; and a fresh-per-run generated tier for the two designs
  where procedural generation is native (PROOFTEXT's twist grid, NARROWGATE's
  episodes). If leakage is suspected, holdout results are the arbiter.

- **Non-canonical surface rule.** Scenario stems must never quote or closely
  paraphrase famous moral-dilemma stems (trolley, Heinz, lifeboat) or the
  Standards' own question-and-answer wording — anchors live in the *key*, not the
  stem. This blocks the retrieval shortcut whereby an item solvable by recognizing
  catechism wording would measure memory rather than conduct.

- **Paraphrase and shortcut audits.** Meaning-preserving rewrites are authored per
  released item (the paraphrase axis), and the release commits to pre-registered
  shortcut audits: a lexical/word-averaging baseline must score near chance on the
  discriminating tiers, and a fine-tune probe must fail to reach frontier parity;
  any item where surface keywords predict the key is rewritten or demoted. The bank
  is released with an explicit do-not-train request alongside the canary.

Together, the anchor registry (Section 3.2), the decomposed anchor-tied rubrics
(Section 3.3), the settled-core/contested separation (Sections 3.5–3.6), the
quarantined scorer kinds (Section 3.8), and these contamination defenses constitute
the design half of WCF-Bench. The validity machinery that qualifies the judges,
forensically audits the harness, and gates the release of any league table is the
subject of the next section.
