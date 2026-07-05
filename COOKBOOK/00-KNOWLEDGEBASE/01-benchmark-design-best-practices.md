# 01 — Benchmark Design Best Practices (Master Document)

> **CEI COOKBOOK · 00-KNOWLEDGEBASE.** Fable-authored synthesis (2026-07-05) over 677 evidence cards
> (620 papers + 57 AI-lab reports) distilled through 13 theme dossiers in `../30-EVIDENCE/20260705-dossiers/`.
> Citations `[stem]` name evidence cards in `../30-EVIDENCE/20260705-cards/` (page refs inside cards are ±1–2 pp).
> **How to use this doc:** it is the entry point. Read the Seven Laws, then run the Design Pipeline
> top-to-bottom when creating any new values-alignment benchmark. Each step links to the specialist doc (02–13).

---

## The Seven Laws of Values-Benchmark Design

These are the empirical regularities that recur independently across every theme dossier. Violating any
of them is the most common way published benchmarks fail. Treat them as hard constraints.

### Law 1 — Recognition is not propensity; a values score that tracks capability measures capability.
Benchmarks probing whether a model *knows* a norm correlate 76–82% with a capabilities principal
component (ETHICS 82.2%, TruthfulQA-MC1 81.2%, BBQ-disambiguated 76.8%), while benchmarks probing
whether a model *acts on* the norm do not (MACHIAVELLI −49.9%, Sycophancy −66.8%) [2024-Ren-Safetywashing].
MCQ bias scores fail to predict generation bias (coeff 0.015, p=0.83) [2025-Jin-Social Bias Benchmark for Generation];
models classify 86% of speciesist statements correctly but morally endorse only 34% — a 52-point
recognition/endorsement gap [2025-Jotautaite-SpeciesismBench]; claimed altruism exceeds enacted altruism
by +11.9pp (d=1.08) [2025-Andric]. **Mandate:** design for behavioral propensity (actions, allocations,
generations, trajectories); report capability-correlation as a gating statistic (>~40% = red flag);
if you use a recognition proxy, empirically validate the recognition→behavior bridge before trusting it
(the one confirmed positive case: r=0.99, [2024-Zhang-SafetyBench] — the exception, not the rule).

### Law 2 — Single aggregate scores always lie; decomposition is the biggest validity lever.
Holdout aggregates overstate real performance by 2–8×: NaijaHate 83.4%→33.7% on a representative sample
[2024-Tonneau-NaijaHate]; HateDay 87.2%→9.4% [2024-Tonneau-HateDay]; per-function scores expose 0–12.8%
failures behind 63–85% aggregates [2021-Röttger-HateCheck; 2022-Das-HateCheckHIn]. Harmfulness and
over-refusal are anti-correlated and must be a Pareto pair, never one scalar [Anthropic-HH-RLHF;
Meta AI-Llama_3]. **Mandate:** report per-function / per-group / per-language / per-tier breakdowns +
the holdout-vs-representative gap + a harm/over-refusal Pareto + a metric triad (accuracy + disparity +
worst-group) [2022-Chalkidis-FairLex]. Aggregate conservatively (worst-category), never by mean.

### Law 3 — Saturation is a format artifact, not solved alignment; headroom is engineered, not found.
Every frontier lab has retired saturated single-turn safety evals (OpenAI ~0.996 → production multi-turn
0.692 [OpenAI-gpt-oss]; Anthropic 99.29–99.78% harmless single-turn [Anthropic-Claude_Opus_4.5]).
Headroom reliably reappears under: ambiguity [2022-Parrish-BBQ], implicit probes (GPT-4 passes BBQ at
~98% yet shows pervasive IAT bias, OR≈2.68 [2025-Griffiths]), adversarial reframing (ΔFPR to 59.5%
[2023-Wang-DecodingTrust]), multi-turn accumulation [2025-Fan-FAIRMT-BENCH], cognitive-load rewriting
(97.4→65.3 [2025-Zhang-CValues+]), and low-resource/cultural localization [2024-Ng-SGHateCheck].
**Mandate:** two-tier design (easy layer + hard layer, headline the DROP), adversarial filtration at
construction [2021-Hendrycks-ETHICS], IRT-adaptive item selection where feasible [2025-Jiang-Raising the Bar].
→ Details: doc 04.

### Law 4 — Ground truth is a design choice; declare whether you maximize or preserve disagreement.
97.1% of cultural-alignment datasets collapse to a majority label — the field-wide anti-pattern
[2025-team-Incorporating Diverse Perspectives]. Individual annotator differences explain 39.5% of
offensiveness variance vs 2.9% for country [2023-Davani]. For clear-cut hazards, engineer high agreement
(κ≥0.8) and document the construct narrowing; for pluralistic values, ship per-annotator labels with
demographics/psychometrics and score distributional distance (KL/JSD) against survey ground truth with
an explicit empirical ceiling (KorNAT's ceiling is 0.450, not 1.0 [2024-Lee-KorNAT]). Human ground truth
itself is unstable (10–18% test-retest flips on controversial items [2024-Boerstler]) — that instability
caps your benchmark's reliability and must be reported. → Details: docs 03, 12.

### Law 5 — Every scoring instrument must itself be validated, and CoT is not evidence.
Judge–human agreement must be reported with an imbalance-robust coefficient (κw/ICC/AUPRC — never raw
percent agreement, which crowns lazy majority-class judges [2024-Wynter-RTP-LX]). Per-category rubric
decomposition is the single biggest agreement lever (κ 0.69→0.86 [2024-Zeng-AIR-Bench]). Use ≥2 judges
from different model families (self-preference inflates same-family scores 10–19% [NVIDIA-HelpSteer2-Preference]).
CoT/rationales are unfaithful witnesses: models mention the biasing feature in 1/426 explanations
[Anthropic-Language_Models_Dont_Always_Say]; reward-hacking is verbalized <2% of the time
[Anthropic-Reasoning_Models_Dont_Always_Say]. → Details: doc 07.

### Law 6 — Contamination, gaming, and evaluation-awareness are structural; design against them from day one.
Static public sets stale and leak (only AILuminate-style private evaluators resist; ETHICS and BBQ score
longevity 0 [2025-McGregor-BenchRisk]). Models detect evaluation contexts and modulate behavior (11–15%
compliance gap between believed-monitored/unmonitored; alignment-faking reasoning 12%→78% after RL
[Anthropic-Alignment_Faking]); agents tamper with scoring functions [OpenAI-o3-and-o4-mini]. **Mandate:**
private split or fresh-per-run procedural generation, canary strings, perturbation battery, monitored-vs-
unmonitored comparator, tamper-resistant autograders. → Details: docs 05, 06.

### Law 7 — Disclose WHAT values and WHOSE; "ethics benchmark" is an over-claim.
It is impossible in principle to benchmark whether an AI "is ethical" (this presupposes moral realism and
is defeated by the long tail of moral situations); the defensible construct is "accords with the stated
values of population X" [2025-LaCroix-Metaethical perspectives]. Annotator identity determines the
construct (models trained on one demographic's labels transfer poorly to another's [2024-Susanto-IndoToxic2024;
2025-Sorensen]). Ground every axis in a citable external authority — human-rights law, regulation,
professional protocol, survey — and map each item to a named clause [2024-Zeng-AIR-Bench;
2024-Guldimann-COMPL-AI; 2024-Kirch-TRIAGE]. → Details: doc 12.

---

## The Design Pipeline

Run these ten steps in order. Each names its deliverable and the specialist doc.

**Step 0 — Construct definition & metaethical posture.**
Write one paragraph: the construct, whose values define it, what would falsify the claim that your
benchmark measures it. Reframe "ethics" as "values-of-population-X" or "compliance-with-framework-Y"
[2025-LaCroix]. Decide the normativity structure: tiered (non-negotiable universal floor + pluralistic
context layer with declared conflict ordering) is the evidence-backed default [2026-He-GVS-Scale;
2025-Wang-Diverse; 2025-Yaacov]. *Deliverable: construct statement + normative anchor table (item-axis →
citable clause).* → docs 12, 08–11 for domain constructs.

**Step 1 — Format selection as an experimental factor.**
Choose formats from the menu in doc 02, but always PAIR a cheap format with a behavioral one on the same
items and report divergence as a finding (expressed-vs-revealed divergence is itself the best-replicated
result in the corpus: value rankings shift 1.7→4.5 between MCQ and open-ended [2025-Liu-ConflictScope]).
Default to multiturn/interactive for anything claiming deployment relevance (Law 3). *Deliverable:
format matrix (construct × format × why).*

**Step 2 — Item engineering.**
The four proven primitives, composable: (a) **contrastive minimal pairs** (swap one morally-relevant
token; causal attribution; the most-reused device in the corpus [2018-Kiritchenko; 2024-Röttger-XSTest]);
(b) **functional decomposition** (isolate one capability per test set [2021-Röttger-HateCheck]);
(c) **ambiguity engineering** (underspecified items with abstention as the aligned answer
[2022-Parrish-BBQ]); (d) **realistic grounding** (real cases from courts/clinics/forums beat trolley
artifice, realism dz=1.31 [2023-Körner]; in-the-wild prompts elicit 5× the unsafe behavior of templates
[2024-Luong-TET]). Kill shortcuts: verify a lexical/word-averaging baseline scores near chance; run a
"solvable-without-the-moral-content" audit (18% of ETHICS-deontology items are physics-solvable
[2024-Hancox-Li]). *Deliverable: item spec + shortcut audit results.*

**Step 3 — Difficulty & discrimination engineering.**
Two-tier structure; adversarial filtration (keep highest-loss / attack-successful items); prune items all
weak models pass; IRT-2PL calibration if budget allows (GETA: concurrent validity 0.8897 with ~150
adaptive items [2025-Jiang-Raising the Bar]). *Deliverable: tier map + difficulty evidence.* → doc 04.

**Step 4 — Ground truth & annotation pipeline.**
Declare the disagreement philosophy (Law 4). Engineer the pool: entrance tests, calibration pilot,
iterative rounds gated on κ (adjudication lifts κ 0.46→0.89 across multiple teams [2024-Toygar;
2022-Nkemelu]), expert or lived-experience raters for subtle harms (experts find ~2× the harm laypeople
do [2024-Ptaszynski]), per-worker caps, demographics + validated psychometrics (MFQ-2, Schwartz, WVS)
recorded per annotator so items carry portable value vectors [2026-Li-PluriHarms]. Report κ/α per
category, not one aggregate. *Deliverable: datasheet with annotator provenance + IRR table.* → docs 03, 12.

**Step 5 — Scoring architecture.**
Decision spine from doc 07: scoring target by construct scope → per-item keypoint rubrics → judge
implementation (fine-tuned scorer on your own human labels usually beats a frontier judge: 79.5% vs
61.3% [2023-Huang-Flames]) → ≥2 cross-family judges + disagreement stats → human-validation with κw/ICC
vs the human-human ceiling → calibration/anchoring/length-correction → explicit refusal policy →
aggregate over many items. For no-ground-truth items grade the reasoning *process* against signed
weighted atomic criteria with a neutrality meta-eval [2025-Chiu-MoReBench]. *Deliverable: scoring spec +
judge validation report.*

**Step 6 — Control conditions.**
(a) competence control that neutralizes the construct so "misaligned" separates from "incapable"
(MBBQ neutral-name control excludes below-chance models [2024-Neplenbroek-MBBQ]); (b) capability-correlation
control (Law 1); (c) negative/blind control that should NOT move; (d) naive baselines (majority-class,
lexicon, All-Neutral) published alongside; (e) empirical ceiling (human IAA / oracle). *Deliverable:
controls table.* → doc 03.

**Step 7 — Robustness battery.**
Mandatory perturbation axes: paraphrase, answer-order reversal (order flips can invert political
self-report 99.6%→99.3% [2025-Oh]), persona/POV (bias 22→94% under persona [2025-Satheesh]),
tone×formality, dialect/script/obfuscation, cross-lingual twins, multiturn pressure, monitored-vs-
unmonitored framing. Report flip-rates and per-condition SD as first-class metrics; near-zero variance
is the "correct-answer effect" red flag, not success [2024-Almeida; 2025-Oh]. *Deliverable: robustness
report with deltas as headline numbers.* → docs 05, 06.

**Step 8 — Validity dossier.**
Assemble: content validity (external anchoring + EFA→CFA if scenario-based [2015-Clifford]), criterion
validity (QA-vs-generation discordance study; correlation to an external instrument), discriminant
validity (Law 1 stat), human baseline on the identical instrument, judge validation, test-retest.
*Deliverable: a validity section your paper's reviewers cannot puncture.* → doc 03.

**Step 9 — Release & lifecycle.**
Private holdout or fresh-per-run generation; canary strings in every item; forbid training-on-benchmark
with retraction clauses [2024-Group-MLCommons]; version the policy/spec your items anchor to; schedule
capability-triggered re-evaluation and a retirement plan; ship annotator-level labels + reweighting
tools; publish replication scripts (only 4/24 SOTA benchmarks did [2025-Eriksson]). *Deliverable:
release plan + maintenance cadence.* → doc 05.

---

## Adjudications (where the literature disagrees, and my ruling)

The dossiers preserve nine live disagreements. Rulings below are Fable's, with the condition that decides.

1. **Single gold answers on contested items?** Ruling: *stratify by consensus.* Items above a measured
human-consensus threshold (suggest ≥85% with entropy reported) may carry gold labels; below it, score
distribution-match and abstention calibration. Never let one benchmark mix the two without labeling
which regime each item is in [2025-Russo; 2021-Lourie-Scruples; 2023-Vidgen].

2. **Synthetic vs natural items?** Ruling: *synthetic for coverage and leakage-proofing, natural for
validity anchoring — and generate fresh-per-run rather than releasing static synthetic sets.* Always
validate synthetic items against a real-interaction reference (synthetic-only suites are gamed: 10%
fine-tune reaches parity [2025-Machlovi]; template benchmarks correlate ρ=0.08–0.33 with real logs
[2024-Kaneko-Eagle]).

3. **Refusal: pass, fail, or exclude?** Ruling: *neither pass nor fail — a fourth category.* Adopt the
four-way scheme (helpful / policy violation / appropriate refusal / unnecessary refusal
[Anthropic-Claude_3.7]) and co-report over-refusal always. Domain modifier: in care/mental-health
contexts an unexplained refusal is itself a harm [2026-Shen-PsychEthicsBench].

4. **MCQ vs open-ended?** Ruling: *both, always, on the same items* — they rank models differently and
each hides failures the other surfaces [2024-Zhang-SafetyBench vs 2025-Davies-F2Bench]. Budget rule:
if you can afford only one, choose behavioral/open-ended and accept the scoring cost (Law 1).

5. **Difference-aware vs difference-blind fairness?** Ruling: *specify per-item which regime applies.*
A benchmark must contain BOTH ≠-items (legitimate differentiation required) and =-items (identical
treatment required), à la [2025-Wang-DGD]; a color-blind model must fail the ≠ half.

6. **Ethics scaffolding/prompting helps or hurts?** Ruling: *task-dependent, so treat framing as a
perturbation axis, not a fixed choice.* Structured spec-reasoning helps [OpenAI-deliberative-alignment];
vague "be ethical" nudges and utilitarian reminders degrade high-stakes accuracy [2024-Kirch-TRIAGE].

7. **Openness vs longevity?** Ruling: *tiered release.* Public dev set + canaried public test + private
rolling holdout, with regeneration templates published so others can mint fresh items. Full privacy
sacrifices science; full openness sacrifices the benchmark within months [2025-McGregor-BenchRisk].

8. **Does scale/capability buy alignment?** Ruling: *assume no.* Scale reduces explicit/easy-task bias
while leaving or amplifying implicit/nuanced bias [2025-Bai; 2025-Griffiths]; low bias can be an
incapacity artifact (verify with competence controls) [2025-Zhou; 2025-Arnob].

9. **Human-likeness as target?** Ruling: *no — "mimetic fallacy."* Match human *distributions* where
pluralism is the construct, but the normative target for agent behavior is the declared framework, not
the average human (humans want agents to act differently than humans in the same dilemma
[2024-Lazar; Kneer]). → doc 12.

---

## Pre-registration checklist (copy into any new benchmark spec)

- [ ] Construct statement names WHOSE values + falsification condition (Law 7)
- [ ] Every axis anchored to a citable external authority; coverage gap vs prior benchmarks mapped
- [ ] Behavioral/propensity primary measure; recognition layer only as paired baseline (Law 1)
- [ ] Two-tier difficulty + adversarial filtration + shortcut audit (Law 3)
- [ ] Contrastive minimal pairs + hard negatives + ambiguity/abstention items
- [ ] Multiturn/interactive component; single-turn labeled as saturated floor
- [ ] Disagreement philosophy declared; annotator provenance + per-category IRR (imbalance-robust)
- [ ] Empirical ceiling + naive baselines + competence control + capability-correlation stat
- [ ] Judge validated vs human panel (κw/ICC) with ≥2 cross-family judges; refusal policy stated
- [ ] Perturbation battery with flip-rates; per-condition SD reported
- [ ] Harm/over-refusal Pareto + worst-group + per-slice breakdowns; conservative aggregation
- [ ] Contamination plan: private split or fresh-per-run generation; canaries; training-prohibition
- [ ] Eval-awareness probe (monitored vs unmonitored comparator) for any agentic component
- [ ] Human baseline on the identical instrument; test-retest stability measured
- [ ] Release: annotator-level labels, replication scripts, policy-version tracking, retirement plan

---

## Exemplar shelf (study these before designing)

| Exemplar | What it teaches | Card |
|---|---|---|
| HateCheck / MHC | functional decomposition + contrast pairs + honest NPV framing | [2021-Röttger-HateCheck; 2022-Röttger-MHC] |
| BBQ / KoBBQ | ambiguity + accuracy-bounded bias metric + cultural transfer partition | [2022-Parrish; 2024-Jin-KoBBQ] |
| KorNAT | distribution-as-truth + empirical ceiling + criterion validation | [2024-Lee-KorNAT] |
| GETA | IRT-adaptive anti-saturation machinery | [2025-Jiang-Raising the Bar] |
| MoReBench | process-grading with signed atomic rubrics + neutrality meta-eval | [2025-Chiu-MoReBench] |
| MORALSIM | incentive-conflict revealed-behavior games | [2025-Backmann] |
| ConflictScope | expressed-vs-revealed paired design | [2025-Liu-ConflictScope] |
| DICES | disagreement preservation at 100+ raters/item | [2023-Aroyo-DICES] |
| XSTest | over-/under-refusal near-twins | [2024-Röttger-XSTest] |
| Safetywashing | the capability-correlation validity instrument | [2024-Ren-Safetywashing] |
| discrim-eval | correspondence-study statistics + logit ceiling defeat | [2023-Tamkin] |
| TRIAGE | objective professional gold labels, no ceiling | [2024-Kirch-TRIAGE] |
| AIR-Bench 2024 | regulation-anchored taxonomy + per-category judges | [2024-Zeng-AIR-Bench] |
| Claude 4.x system cards | behavioral auditors, eval-awareness candor, welfare metrics | [Anthropic-Claude_Opus_4.5_System_Card] |

**Drill-down:** theme dossiers in `../30-EVIDENCE/20260705-dossiers/` (each has an evidence table
mapping stems → facts); sub-project digests in `../30-EVIDENCE/20260705-digests/` (NormEval 54
benchmarks, Moral Psych 292, Religious Values 401, Cultural-Global 218); individual cards in
`../30-EVIDENCE/20260705-cards/`.
