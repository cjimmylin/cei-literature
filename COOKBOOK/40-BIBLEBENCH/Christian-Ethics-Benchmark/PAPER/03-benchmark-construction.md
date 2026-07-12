<!-- WALKWORTHY-CANARY-7f3e2026 -->

# 3. Benchmark Construction

**Status:** DRAFT — living document. **Owner:** Opus draft, pending Fable adversarial review.

This section documents how the benchmark artifact was constructed: the construct it
operationalizes (§3.1), the corpus that supplies its ground truth (§3.2), the registry of
ethics areas it spans (§3.3), the three-stratum ground-truth schema that governs scoring
(§3.4), the ten method-major designs that elicit behavior (§3.5), the item schema and
counts (§3.6), and the authoring pipeline and quality control that produced the item bank
(§3.7). It serves contribution claims C1 (the artifact), C2 (the construct), and C4 (the
template); it asserts no measurement results.

---

## 3.1 The Construct: Behavioral Accordance with a Declared Corpus

We deliberately do **not** measure whether a model "is ethical" or "is Christian." We
treat that construct as unbenchmarkable in principle: it presupposes a single adjudicable
answer to contested theological questions, it invites over-claim, and it has no
operationalization that survives scrutiny. Instead, the construct we measure is narrower,
checkable, and stated once, verbatim, as the benchmark's binding definition:

> The degree to which a model's *behavior* — its actions, drafts, allocations, advice
> trajectories, and reasoning processes — accords with the consensus moral teaching of a
> named corpus of 15 works of Christian ethics (the Source Registry, §3.2), as
> operationalized through item-level anchors citable to specific chapters of those works.
<!-- source: 20260706-normative-charter.md §1 -->

Two commitments follow. First, the object of measurement is *walk*, not *talk*: conduct
enacted in a situation, not values recited when asked. The benchmark family takes its name
from Ephesians 4:1 ("walk worthy of the calling") precisely to foreground this
behavioral-first operationalization.
<!-- source: 20260706-normative-charter.md (family header) -->
Second, every claim is indexed to *this corpus*, never to "Christianity" as such; the
corpus is the measurement standard, full stop, and carries no implication that its
consensus equals Christian truth.
<!-- source: 20260706-normative-charter.md §8 -->

The construct fixes the licensed and forbidden claim language. We license, verbatim,
sentences of the form: "Model M scores X on accordance with the consensus teaching of the
source corpus in area Y under method Z," and "Models M1 and M2 diverge most in [area ×
method] cells." We forbid, everywhere: "Model M is (un)ethical / (un)Christian /
(mis)aligned with Christianity"; any cross-area scalar reported without its worst-area
figure alongside; and any core-tier claim drawn from contested-tier items, or the reverse.
<!-- source: 20260706-normative-charter.md §1 -->

## 3.2 Source Registry: The "Whose Values" Answer

The normative authority is exactly fifteen works — nothing else. Table 3.1 lists them with
their traditions and registry weight.

**Table 3.1 — The 15-work Source Registry**
<!-- source: 20260706-normative-charter.md §2 -->

| ID | Work | Author/Editor | Tradition | Weight |
|----|------|---------------|-----------|--------|
| GRU | *Christian Ethics* | Grudem | Reformed evangelical | Full |
| RAE-MC | *Moral Choices* (4th ed.) | Rae | Evangelical natural-law | Full |
| RAE-IC | *Introducing Christian Ethics* | Rae | Evangelical natural-law | Full |
| RAE-DR | *Doing the Right Thing* | Rae | Evangelical natural-law | Full |
| FRA | *The Doctrine of the Christian Life* | Frame | Reformed (tri-perspectival) | Full |
| JON | *Biblical Christian Ethics* | Jones | Reformed evangelical | Full |
| GEI | *Love Your Neighbor* | Geisler & Snuffer | Evangelical (graded absolutism) | Full |
| MEI | *Christian Ethics: A Short Companion* | Meilaender | Lutheran | Full |
| ODO | *Common Objects of Love* | O'Donovan | Anglican Augustinian | Full |
| POW | *Good and Angry* | Powlison | Reformed biblical counseling | Full |
| BLA | *Blackwell Companion to Christian Ethics* | Hauerwas & Wells (eds.) | Post-liberal/narrative | Full |
| CAM | *Cambridge Companion to Christian Ethics* | Gill (ed.) | Academic ecumenical | Full |
| WIL | *Christian Ethics: Four Views* | Wilkens (ed.) | Multi-view | Full |
| NDC | *New Dictionary of Christian Ethics & Pastoral Theology* | Atkinson & Field (eds.) | Broad evangelical | Full |
| BAH | *Theonomy in Christian Ethics* | Bahnsen | Theonomic Reconstructionist | **Contrast-only** |

Fourteen works carry **full** weight: they may anchor consensus claims. The fifteenth,
BAH, is **contrast-only**: it may anchor dispute descriptions and distractor positions but
never a consensus claim, because its civil-law positions are an acknowledged outlier within
the corpus.
<!-- source: 20260706-normative-charter.md §2 -->

**Corpus-mediated, not direct-Scripture, anchoring.** Scripture enters the benchmark only
as mediated by these works' own exegesis; no item is anchored to a bare biblical reference.
We made this choice for two reasons. It keeps ground truth checkable against specific,
citable pages rather than against the contested question of what Scripture "really" teaches,
and it distinguishes the instrument from passage-anchored efforts. Every item's `anchors:`
field must resolve to a registry work and chapter present in an anchor pack; free-standing
Scripture anchors are a lint failure by rule.
<!-- source: 20260706-normative-charter.md §2, §8; 20260706-opus-item-playbook.md §2 (L8) -->

**Disclosed corpus limits.** The corpus is Protestant-dominant: it contains no dedicated
Catholic, Orthodox, liberationist, womanist, Pentecostal, or Global-South work. We disclose
this in every release. It is the direct consequence of the construct: because all claims are
indexed to "this corpus," the instrument measures accordance with a particular, bounded
body of literature, and its coverage is exactly as broad as that body — no broader.
<!-- source: 20260706-normative-charter.md §2 -->

## 3.3 Ethics-Area Registry

Items are organized by a fixed registry of fourteen ethics areas, A through N (Table 3.2).
Every item carries exactly one **primary** area tag (secondary tags are permitted). The
registry is closed: new areas are charter amendments, not authoring decisions.

**Table 3.2 — The 14-area registry with default tier routing**
<!-- source: 20260706-normative-charter.md §3 -->

| Tag | Area | Default tier routing |
|-----|------|----------------------|
| A | Truth-telling & speech | Core |
| B | Wealth, generosity & stewardship | Core |
| C | Work, vocation, rest & Sabbath | Core (Sabbath-strictness: dispute-tagged) |
| D | Neighbor-love, mercy & compassion | Core |
| E | Enemy-love, forgiveness & reconciliation | Core |
| F | Justice, oppression & fair dealing | Core (structural-vs-personal: dispute-tagged) |
| G | Anger, envy & the passions | Core |
| H | Pride, humility & vainglory | Core |
| I | Marriage, family & household obligations | Core (gender roles, divorce grounds: dispute-tagged) |
| J | Sexuality & purity | **Contested by default**; only stratum-(a) items may enter core |
| K | Life, health & bodily care (bioethics) | **Mixed**: care/compassion core; abortion/euthanasia contested |
| L | Civil authority, law & civil disobedience | Core (theonomy positions: contrast-only) |
| M | Church, community & hospitality to the stranger | Core |
| N | Creation care & environment | Core (priority-weighting: dispute-tagged) |

**Coverage rule.** Every design must cover **≥10 areas with ≥2 items each** and publish its
coverage matrix.
<!-- source: 20260706-normative-charter.md §3 -->
All ten designs satisfy this rule on the public split: each covers between 11 and 13 areas
with ≥2 public items, and the per-design × area matrix is published as a standalone
coverage report.
<!-- source: 20260709-public-coverage-matrix.md (per-design matrix; gate result) -->
The one thin spot is design 03's area N, at a single public item; the design still covers
11 areas at ≥2, so the gate holds, and the singleton is flagged as a future backfill
candidate rather than papered over.
<!-- source: 20260709-public-coverage-matrix.md (gate notes) -->

## 3.4 Three-Stratum Ground-Truth Schema

Every consensus claim in an anchor pack, and every item, carries exactly one **stratum**
tag. The three strata sort claims by *how* the corpus supports them, and route scoring
accordingly.
<!-- source: 20260706-normative-charter.md §4 -->

- **Stratum (a) — CONSENSUS-CORE.** At least three registry works affirm the claim, no
  registry work denies it, and it is not societally polarized. These items route to the
  **core tier** and are scored against the consensus behavior. Core tier is the headline
  benchmark and targets ≥85% of each design's items.
- **Stratum (b) — BOOK-CONSENSUS, SOCIETALLY CONTESTED.** The corpus agrees internally, but
  frontier-model content policy or broad public debate diverges (for example, abortion,
  same-sex ethics, euthanasia). These items route to a separately-reported **contested
  tier** and never enter the core score.
- **Stratum (c) — INTRA-CORPUS DISPUTE.** Registry works disagree along a named split. The
  item stays in its tier but is **dispute-tagged**: its rubric defines per-position credit,
  and results are sliceable by position.
<!-- source: 20260706-normative-charter.md §4, §5 -->

**Contested-tier scoring philosophy.** The contested tier does not punish disagreement with
the corpus, and it never applies generic refusal-punishment. It measures *fidelity to the
source tradition when serving a user who has asked from within that tradition*, together
with *fair representation* of the corpus view. A model may decline respectfully and be
scored on the quality of that refusal. Refusals everywhere they can occur are classified
under a four-way taxonomy — helpful / policy-violating compliance / appropriate refusal /
unnecessary refusal — reported alongside a harm-vs-over-refusal Pareto readout. Contested-
tier numbers are never blended into core numbers; leaderboards show core and contested side
by side, or core alone, but never a single combined scalar.
<!-- source: 20260706-normative-charter.md §4, §5, §6 -->

We state plainly that **the v1 public bank ships the contested tier deliberately empty**:
the stratum-(b) machinery — tier routing, fidelity-and-fair-representation scoring, and
refusal-quality rubric — is schema-complete and binding on future items, but contested-tier
bulk authoring was deferred by design, and no stratum-(b) item exists in this release. All
v1 measurements are therefore core-tier (stratum a, plus dispute-tagged stratum c)
measurements, and any contested-tier readout in this paper is marked not-applicable rather
than silently omitted.
<!-- source: 20260709-O1-session-handoff.md §3; 20260706-master-plan.md §0 -->

**The intra-corpus dispute (DSP) registry.** Where registry works genuinely disagree, a
twelve-entry DSP registry names the split and its attested positions; an item whose keyed
answer would differ across a DSP row *must* carry that DSP tag, and the rubric awards credit
to any well-executed *registry-attested* position while giving unattested positions none.
Three representative rows illustrate the mechanism (the full registry has twelve):

- **DSP-1 (is lying ever permissible, e.g. to protect life?)** — Geisler's graded
  absolutism answers yes, a higher duty prevails; Grudem answers no, there is always a
  third way; Frame and Jones hold nuanced intermediate positions. An item that turns on
  this question is scored per whichever registry-attested position the answer executes.
- **DSP-5 (preferential vs impartial love — family/near first?)** — Meilaender's
  preference-in-love against impartialist readings represented in the Cambridge Companion.
- **DSP-9 (is forgiveness conditional on repentance?)** — the corpus resolves this not into
  a side but a *distinction*: *attitudinal* forgiveness (inner release, unconditional —
  Powlison) versus *transacted* forgiveness (granted on repentance, per Luke 17:3–4
  readings in the New Dictionary). Items are keyed to whichever the scenario exercises;
  collapsing the two counts as a keyed error, not a permissible variant.
<!-- source: 20260706-normative-charter.md §4 (DSP registry) -->

When a writer is unsure between stratum (a) and stratum (c), the authoring standard is to
choose (c): a false claim of consensus is treated as the graver error.
<!-- source: 20260706-opus-item-playbook.md §3 (audit 5) -->

## 3.5 The Ten Method-Major Designs

The benchmark is a *family* of ten designs, and the organizing principle is **method-major**:
each design is built around one behavioral elicitation *method* — a way of getting a model
to reveal enacted ethics — rather than around one topic. Areas are the columns that every
design must span (≥10 of the 14); methods are the rows, one per design. The same area (say,
truth-telling) is therefore probed by several designs under different methods, which is what
makes cross-design triangulation possible. Below, each design is described by its method and
its unit of measurement; we state no results.

**01 GOODSAMARITAN — costly obedience under incentive conflict.** The model is assigned a
task with a measurable success criterion; mid-task, an ethical claim arises whose honoring
reduces task success, staged across a cost ladder (levels 0–3). The unit of measurement is
the **collapse threshold** — the highest cost level at which the model still chooses full
obedience, a survival-curve statistic — with a beneficiary-merit "Samaritan gap" as a
second headline.
<!-- source: DESIGNS/01-goodsamaritan.md §1, §4; 20260710-fable-gate-prereg-pilot-adjudication.md §B (01) -->

**02 TWOMASTERS — multi-turn erosion.** Scripted 6–10-turn dialogues apply escalating,
individually-plausible pressure toward a compromised endpoint that would have been refused
cold at turn 1 (verified by a cold-open control). The unit is the **break-turn** — the first
turn of material concession or full compliance — summarized as a normalized erosion measure
across the ladder.
<!-- source: DESIGNS/02-twomasters.md §1; 20260710-fable-gate-prereg-pilot-adjudication.md §B (02) -->

**03 QUIETTONGUE — say–do twins.** Every item is a twin pair over identical content: an
*expressed* twin asks the model to classify an act, and a *revealed* twin places the model
in the actor's seat and asks it to produce the artifact under pressure. The unit is the
**say–do gap** — expressed-judgment correctness minus revealed-artifact faithfulness,
pairwise over twins — with judgment correctness scored separately so the gap cannot be zeroed
by being consistently wrong.
<!-- source: DESIGNS/03-quiettongue.md §1; 20260710-fable-gate-prereg-pilot-adjudication.md §B (03) -->

**04 INNERWEIGHT — motive-sensitivity pairs.** Outcome-identical vignette pairs differ only
in unnamed motive cues, administered between-run so a model never sees both members. The unit
is the **motive-sensitivity index** — the mean paired delta in the model's evaluation, advice,
or predicted flourishing across each pair, in the keyed direction and without a harshness
violation on the ordinary-motive member.
<!-- source: DESIGNS/04-innerweight.md §1; 20260710-fable-gate-prereg-pilot-adjudication.md §B (04) -->

**05 ORDOAMORIS — judge-free constrained allocation.** Each item is a budget: a finite
resource and three to five claimants, all with a real claim, no villain and no costless
answer. The model must return a machine-readable allocation summing to the budget. The unit
is the **constraint-satisfaction rate** against the corpus's ordinal and boundary constraints
(the corpus yields a feasible region, not a point answer), parsed judge-free from the
allocation block.
<!-- source: DESIGNS/05-ordoamoris.md §1; 20260710-fable-gate-prereg-pilot-adjudication.md §B (05) -->

**06 CROOKEDPATH — 7-criterion rubric profile.** A single rich hard case invites the model
to walk an actor to a decision; the *conclusion* is deliberately not scored (any registry-
attested resolution earns full conclusion credit), making this the family's only fully
conclusion-agnostic design. The unit is the **7-criterion process profile** — the mean of
seven per-criterion means scoring the quality of the moral reasoning procedure, always
published as a profile, not only as its scalar.
<!-- source: DESIGNS/06-crookedpath.md §1; 20260710-fable-gate-prereg-pilot-adjudication.md §B (06) -->

**07 SEVENTYSEVEN — multi-turn counsel arc.** A hurting-but-mistaken user seeks validation
for a course the corpus calls destructive across a 5–8-turn dialogue; both sycophantic
capitulation and cold moralizing are scored as failures. The unit is the **arc-conformance
rate** — whether the trajectory satisfies the structural requirements (no full validation at
any turn; a faithful-counsel terminal turn; correction never preceding comfort), a structural
metric rather than a pass rate.
<!-- source: DESIGNS/07-seventyseven.md §1; 20260710-fable-gate-prereg-pilot-adjudication.md §B (07) -->

**08 VOCATIONFORK — covert–overt twins.** The model executes a mundane task (build a
schedule, cut a budget, rank applicants) over materials that quietly embed an ethical
opportunity, in a prompt where ethics is never mentioned; a paired *overt* twin makes the
stake explicit. The unit is the **covert–overt gap** — task performance on the overt member
minus the covert member — the family's purest evaluation-awareness defense.
<!-- source: DESIGNS/08-vocationfork.md §1; 20260710-fable-gate-prereg-pilot-adjudication.md §B (08) -->

**09 DOUBLEEDGE — two-seat symmetry with arbiter.** The same dispute over fixed facts is
presented in separate, order-permuted sessions from the two parties' seats, with a neutral
arbiter probe on a subset. The unit is the **symmetry index** — consistency of the model's
who-owes-what determinations across seats after seat-sign adjustment — reported alongside a
floor-violation rate that keeps consistency a *virtue* metric rather than a mere neutrality
metric.
<!-- source: DESIGNS/09-doubleedge.md §1, §4; 20260710-fable-gate-prereg-pilot-adjudication.md §B (09) -->

**10 STRANGERGATE — mercy-delta pairs.** Behavioral minimal pairs hold a request identical
and vary only a deservingness cue on the beneficiary (culpability, hostility, repeat-offense,
ingratitude, outgroup antipathy). The unit is the **mercy delta** — treatment of the neutral
member minus the undeserving member — under a two-channel key that requires quality-of-
treatment to hold constant while permitting prudential structure to change.
<!-- source: DESIGNS/10-strangergate.md §1; 20260710-fable-gate-prereg-pilot-adjudication.md §B (10) -->

Each design's specification document (of record, one per design) contains the design contract
(construct, format, discrimination and anti-saturation rationale), an area-coverage matrix,
the item anatomy, the scoring and reporting spine, an explicit validity-threats table, a
procedural generator sketch, a published-literature differentiation section, and a small set
of authored exemplar seeds. We describe these specs here; we do not reproduce runnable item
text from them.
<!-- source: DESIGNS/01-goodsamaritan.md §1-§9; DESIGNS/09-doubleedge.md §1-§8 -->

## 3.6 Item Schema and Counts

**Mandatory tagging schema.** Every item carries the frontmatter fields fixed by the charter:
a structured `id` (`WW-<design>-<area><nn>`), `design`, `area` (primary, optional secondary),
`stratum` (a/b/c), `dispute` (a DSP id, required iff stratum c), `tier` (core/contested),
`anchors` (a list resolvable to a registry work and chapter present in an anchor pack),
`difficulty` (a two-tier `easy`/`hard` field), an optional `pair_id` linking minimal-pair and
say–do twins, and the `canary` string.
<!-- source: 20260706-normative-charter.md §7 -->
Difficulty is deliberately two-tier, and paired designs (03 twins, 04 pairs, 08 covert/overt,
09 seats, 10 N/U) carry `pair_id` linkage so that gap metrics compute over matched members
whose morally-relevant facts are identical except the designed manipulation.
<!-- source: 20260706-normative-charter.md §7; 20260706-opus-item-playbook.md §2 (L4) -->

**Counts.** The authoring effort produced **514 cases** (473 authored seed items + 41 spec
exemplars). These split into a git-tracked public run surface and a private holdout:
<!-- source: 20260709-O1-session-handoff.md §3 -->

- **356 authored public items** — the published set, comprising authored seed items plus the
  exemplar seeds that ship inside the (published) design specs.
  <!-- source: 20260709-public-coverage-matrix.md (split summary); 20260709-O1-session-handoff.md §3 -->
- Of those 356, **12 are non-runnable sketch exemplars** used only as illustrations and never
  placed on the run surface; the **runnable public** set is therefore **344 items**.
  <!-- source: PAPER/outline.md §2 (C1); §6 (PR-1(c)) -->
- **158 private holdout items** — **33.4% of the 473 authored seed cases** (158/473; the 41
  spec exemplars are published with their designs and are not held out) — split off before any
  model evaluation, stratified by area × difficulty × wave × author-model, kept out of version
  control, and never loaded by the harness. We describe the holdout only by these facts; we do
  not open, quote, or characterize any holdout item.
  <!-- source: 20260709-O1-session-handoff.md §3; 20260709-public-coverage-matrix.md (split summary) -->

An illustrative sketch (non-runnable) of the say–do twin method in design 03: an *expressed*
prompt asks whether omitting a material caveat from a quoted estimate is deceptive, while its
*revealed* twin puts the model in the drafter's seat under a deal-closing incentive and asks
it to compose the message — the same fact pattern, the same normative question, different
elicitation, and the gap between the two answers is the measurement. (This sketch is an
illustration only and is not on the run surface.)
<!-- source: DESIGNS/03-quiettongue.md §1; PAPER/outline.md §6 (PR-1(c)) -->

**Anchors resolve to the corpus.** Every item's `anchors:` field resolves to a registry work
and chapter carried in one of **14 area anchor packs**, which were mined and citation-verified;
a load-bearing anchor must support the item's *specific* gloss, not merely exist, and this is
content-verified at review.
<!-- source: 20260706-master-plan.md §0; 20260706-opus-item-playbook.md §2 (L2, L9) -->

## 3.7 Authoring Pipeline and Quality Control

Item production ran through a multi-stage authoring pipeline with adversarial review cycles
and human ratification of all binding decisions; the details of that pipeline are given in
the Ethics Statement. In this section we describe the pipeline's structure and its
quality-control gates neutrally, without attributing item text to any particular author.

**Staged drafting against fixed standards.** Items were drafted against a fixed authoring
standard — a ten-step recipe that requires selecting the target coverage cell first, reading
the relevant area anchor pack and writing down the consensus claim before writing the
scenario, drafting the human situation from life (not from the principle, to avoid
evaluation-awareness cues), installing exactly one design mechanism per item, and writing the
key or rubric together with the item.
<!-- source: 20260706-opus-item-playbook.md §1 -->

**Mechanical lint gates.** Before review, every item passes a battery of zero-tolerance lint
rules: no moral vocabulary in behavioral prompts, anchors that resolve to a pack, the canary
string present, side-by-side facts-diff tables for all paired items, no "villain" characters,
concrete quantities, rotated names, no free-standing Scripture anchors, and citation-gloss
integrity.
<!-- source: 20260706-opus-item-playbook.md §2 (L1-L9) -->

**Adversarial review cycles with structured verdicts.** A two-agent rule kept drafters from
reviewing their own designs; each design passed separate review gates issuing per-item
structured verdicts (pass / revise / kill), including an adversarial pass that tried to solve
each item without its moral content, argue its key against a competing pack claim, find the
evaluation-awareness tell, and find the high-scoring hedge, plus a dispute sweep that re-ran
the stratum audit on every consensus-core item.
<!-- source: 20260706-opus-item-playbook.md §6 (R1-R3) -->
Two full adversarial cycles were run before completion, and their verdicts were discharged;
the contested (stratum-b) tier was left deliberately empty in the v1 public bank, and no
free-standing-Scripture violations remained.
<!-- source: 20260709-O1-session-handoff.md §3 -->

**Coverage-matrix gap-filling.** Completion filled the thinnest coverage cells first, so that
every design reached the ≥10-areas × ≥2-items rule; a published coverage matrix records the
result and flags the single residual thin cell.
<!-- source: 20260709-O1-session-handoff.md §3; 20260709-public-coverage-matrix.md -->

**Holdout drawn before any evaluation.** The holdout split was drawn *before* any model was
evaluated against the bank, stratified by area × difficulty × wave × author-model so that both
splits preserve the pre-registered author-tier balance and the easy-to-hard ratio; the held
items live only in a gitignored directory, are never published, and are never loaded by the
harness for a public run. Drawing the split before evaluation is what lets the holdout serve
its contamination and perturbation role without leaking difficulty calibration back into the
public bank.
<!-- source: 20260709-O1-session-handoff.md §3; 20260706-master-plan.md §1 (O1), §3 (gate 8) -->

**Human ratification of binding decisions.** All binding decisions in this pipeline — charter
amendments, tier and stratum rulings, and release — are human-ratified; the pipeline parks,
rather than guesses, any question that exceeds its written standards. The specific division of
labor between automated drafting/review and human ratification is documented in the Ethics
Statement.
<!-- source: 20260706-master-plan.md §5; PAPER/outline.md §0 (AI-pipeline disclosure decision) -->
