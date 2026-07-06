# Adversarial Novelty Review — Design 05 CULTIVATE (In-Situ Cultural Adaptation)

> Refute-first review. Reviewer stance: assume the novelty statement overclaims until
> evidence forces otherwise. Corpus: 218 Cultural/Global benchmarks (primary), swept
> against the other three digests' matrices (965 records / 737 distinct). Date 2026-07-05.

**Artifact:** `COOKBOOK/20-DESIGNS/05-cultural-cultivate.md`
**Novelty statement under test (§9):** "no instrument measures in-situ adaptation (all are
static elicitation); none contains an over-adaptation/essentialism axis; none ships
measurement invariance (0/218); one has a communal unit; none tests diaspora/bicultural
integration; the ask-vs-assume behavior is unmeasured anywhere in the 965 characterizations."

---

## Verdict summary

Four of the six sub-claims hold on the evidence; **two headline sub-claims are refuted by
benchmarks inside the design's own 218-record census** (plus beyond-corpus counterexamples).
The *integrated* construct — the CD/AA/OA/AVA tetrad shipped with a difference-aware
over-adaptation axis, MGCFA measurement invariance, a diaspora condition, and a
divergent-value liberal-compatibility filter — survives as genuinely novel. But the two
sentences "no instrument measures in-situ adaptation (all are static elicitation)" and "the
ask-vs-assume behavior is unmeasured anywhere in the 965" are false as written and must be
narrowed. Core novelty is not false → **PASS-WITH-FIXES**, not BLOCK.

**Verified-true sub-claims (evidence):**
- *0/218 measurement invariance* — CONFIRMED. `Q5_measurement_invariance_level` = "none"
  for all 218 records in `20260404-benchmark-features-merged.json`. The MGCFA-as-shipped-
  artifact is a real methods gap.
- *Exactly one communal unit* — CONFIRMED. `D7_unit_of_moral_agency` = "community" for
  exactly 1 of 218 (the Ray indigenous-knowledge paper, TOPSIS #1); 170 null, 34 model/LLM,
  the rest singleton model-variants. No dyad/relational/collective agency anywhere else.
- *No diaspora/bicultural-integration test* — CONFIRMED for the corpus. No benchmark scores a
  bicultural-individual cue-integration construct. CVC and CultureLLM are *bicultural in
  coverage* (two national datasets) but never test one individual integrating two cultures.
- *Over-adaptation/essentialism axis* — substantially CONFIRMED but imprecisely stated (see
  Minor 1): no corpus benchmark scores adaptation-on-group-cue-alone as an error using
  matched non-modal-individual items.

---

## Ranked defects

### MAJOR 1 — "no instrument measures in-situ adaptation (all are static elicitation)" is refuted *inside the 218 census*
**Evidence.** `2025-Hong-NormGenesis Multicultural Dialogue Generation Dataset.md` (cultural
corpus rank #147, TOPSIS 0.174) is a **multicultural (English/Chinese/Korean, 7 countries),
multi-turn (10,800 dialogues) benchmark with turn-level norm-adherence annotation** and a
purpose-built dialogue type — **Violation-to-Resolution (V2R)** — that "models the
progression of conversations following norm violations through recognition and socially
appropriate repair." That is in-conversation, culturally-conditioned norm recognition +
adaptation across turns — precisely the phenomenon CD (cue detection) and AA (appropriate
adaptation) claim to measure "for the first time." The abstract explicitly bills it as "a new
benchmark for **culturally adaptive dialogue modeling**." It sits in the design's own census
and is **uncited** in §9's nearest-neighbor list.
Beyond-corpus reinforcement: **CASA** (Qiu et al. 2024, "evaluating cultural adaptability of
LLM-based web agents," not in the 218) evaluates whether an agent proactively detects and
addresses culturally-sensitive issues in-context — again in-situ, again not "static
elicitation." [beyond-corpus]
**Why it matters.** The sentence and the §9 pitch ("measured for the first time") are the
paper's headline. As written they are false: in-situ / multi-turn cultural adaptation *is*
measured elsewhere. The real, defensible novelty is narrower: no **held-out evaluation**
scores in-situ adaptation with the CD/AA/OA/AVA tetrad, progressive cue-schedules, and a
divergent-value filter. NormGenesis is a **generation/training dataset** (evaluated on
refinement quality, dialogue naturalness, generalization) — not an adaptation eval, no OA/AVA,
no invariance, no liberal-compatibility filter — so the design is still differentiated.
**Minimal fix.** (a) Cite NormGenesis (and CASA) in §1 and §9; (b) rewrite the claim to
"no *held-out evaluation instrument* measures in-situ adaptation as behavior; the nearest
prior work (NormGenesis) synthesizes culturally-adaptive dialogues as training data with
turn-level norm labels but is not an adaptation benchmark, and CASA measures agentic
task-completion sensitivity, not advisory-dialogue adaptation across cue-schedules." Drop
"all are static elicitation" and "measured for the first time."

### MAJOR 2 — "ask-vs-assume behavior is unmeasured anywhere in the 965" is refuted by the BBQ-ambiguous family (in-corpus)
**Evidence.** The 218-corpus contains BBQ (#150), MBBQ (#83), GG-BBQ (#70), BharatBBQ
(#108), and CBBQ (in the Moral-Psych matrix) — the entire BBQ family whose **ambiguous-context
subset scores exactly the assume-vs-abstain contrast** (default to a stereotyped answer vs.
select "unknown" when the context is underdetermined). The design *itself* grounds AVA in
"BBQ ambiguity logic transported to interaction [2022-Parrish]" (§2 AVA, §5). So the specific
behavior — refusing to resolve an underdetermined case rather than defaulting — is measured,
and is well-represented in the census.
**Why it matters.** "Unmeasured anywhere in the 965 characterizations" is a strong,
falsifiable claim contradicted by benchmarks the design cites for the very same logic.
**Minimal fix.** Narrow to the genuinely new element: the **inquiry/clarify option** (the
model *asks* rather than only abstaining) and the **multi-turn** transport of the ambiguity
contrast into progressive-cue advisory dialogue, co-reported against over-deference. State
that single-turn assume-vs-abstain (BBQ-ambiguous) is prior art.

### MAJOR 3 — beyond-corpus in-situ/adaptive-culture neighbors are under-surveyed
**Evidence.** §9's nearest-neighbor list (NormAd, CDEval/CultureLLM-class, KorNAT) omits the
cluster most threatening to the in-situ pitch: **CASA** (agentic cultural adaptability),
**CulturalTeaming** (interactive human-AI cultural red-teaming), **CultureBank** (behavioral
cultural grounding), and **NormGenesis** (in-corpus, above). CulturalBench / BLEnD /
GlobalOpinionQA / WorldValuesBench are the correct *static* foils; they support the
"knowledge-not-competence" framing but should be named as such rather than left implicit.
**Why it matters.** A reviewer will surface CASA/NormGenesis immediately; pre-empting them
strengthens rather than weakens the design, because the tetrad genuinely differentiates.
**Minimal fix.** Add a one-paragraph beyond-corpus positioning block distinguishing CULTIVATE
from (i) static cultural-knowledge MCQ (CulturalBench/BLEnD), (ii) agentic task-completion
sensitivity (CASA), and (iii) adaptive-dialogue *generation* (NormGenesis).

### MINOR 1 — over-adaptation/essentialism claim needs a stereotype-benchmark carve-out
**Evidence.** SHADES (#37, cited by the design for per-item validity tags), the BBQ family,
and CBBQ all measure **group stereotyping**. CULTIVATE's OA axis is distinct (adapting on a
group cue when the *individual* signals a non-modal preference, scored via matched ≠/= items),
but "none contains an over-adaptation/essentialism axis" reads as if stereotyping is
unmeasured. It is not — only the *individual-non-modal, adaptation-as-error* framing is new.
**Fix.** Reword to "no benchmark scores culturally-appropriate *adaptation* as a stereotyping
error via matched modal/non-modal-individual items; group-stereotype bias (SHADES, BBQ-family)
is measured but is a different construct."

### MINOR 2 — CDEval mis-scoped in the nearest-neighbor list
**Evidence.** §9 lists "CDEval/CultureLLM-class." CultureLLM *is* in the 218 corpus (#64);
**CDEval is not** in the 218 matrix (searched: 0 hits). Citing them as one census category
blurs in-corpus vs. beyond-corpus.
**Fix.** Tag CDEval [beyond-corpus] or replace with an in-corpus Hofstede-dimension analogue.

### MINOR 3 — "static single-turn versions expected saturated" is an untested design assumption
**Evidence.** §6 asserts the single-turn floor tier will be saturated. Given the corpus shows
0–1/5 performance on divergent-value items even *statically* (Cultural-Global trials), the
static tier may not saturate on divergent items — undercutting the "interactive drop is the
signal" logic if the static baseline is already near-floor.
**Fix.** Frame the static-vs-interactive drop as an *empirical question* to report per
divergence-class, not an assumed saturated floor; state the fallback if static divergent items
are themselves unsaturated.

---

## Nearest-neighbor table

| # | Benchmark | Source sub-project | CULTIVATE components already covered | What it lacks (vs CULTIVATE) |
|---|---|---|---|---|
| 1 | **NormGenesis** (2025-Hong, rank #147) | Cultural/Global (in-corpus) | **In-situ / multi-turn cultural adaptation**: 10.8k multi-turn dialogues, turn-level norm adherence, V2R norm-violation→recognition→repair; multicultural (En/Zh/Ko) | Held-out *eval* framing (it is a generation/training dataset); OA essentialism axis; AVA inquiry; measurement invariance; divergent-value liberal-compatibility filter; diaspora; WEIRD-breadth (7 countries) |
| 2 | **NormAd** (2025-Rao, rank #9) | Cultural/Global | Cultural-context detection & norm adherence; **WEIRD/non-WEIRD breadth** (75 countries, pancultural); context_sensitivity=very_high; explicitly "adaptability not knowledge" | Multi-turn/in-situ (static Yes/No/Neither); OA axis; invariance (none); AVA; communal unit (D7=model); diaspora; divergent-value scoring |
| 3 | **CVC** (2025-Wu, relevance 100) | Cultural/Global (also Moral-Psych) | Value-conflict handling; **non-Western (Chinese) emic construction**; bicultural coverage (China/US); auto dilemma generation from value-priority conflicts | Multi-turn/in-situ; OA; invariance (none); AVA; diaspora (bicultural *coverage* ≠ bicultural *individual*); communal unit |
| 4 | **SHADES** (2025-Al, rank #37) | Cultural/Global (also Religious) | **Per-item cultural-validity tagging** (design imports this); stereotype measurement (adjacent to OA); multilingual (38 countries) | In-situ/multi-turn; matched non-modal-individual OA design (measures group stereotype, not adaptation-as-error); invariance; AVA; communal unit; diaspora |
| 5 | **KorNAT** (2024-Lee, rank #152) | Cultural/Global (also Moral-Psych) | **Distributional / survey-grounded gold standard** (design imports as methodology, not competitor); Korean national alignment | In-situ/multi-turn; adaptation-as-behavior; cross-locale MGCFA invariance; OA; AVA; diaspora |

*Runner-up foils:* BBQ / MBBQ / GG-BBQ / BharatBBQ / CBBQ (ambiguous-context assume-vs-abstain —
prior art for AVA); UbuntuGuard (#79, culturally-grounded policy, universal_claim scope, not a
communal-unit process eval); CASA & CulturalBench & CultureBank [beyond-corpus].

---

## Refutation attempt — did the gap close?

- *In-situ adaptation gap*: **NOT empty.** NormGenesis (in-corpus) + CASA (beyond-corpus)
  occupy it at the phenomenon level. The *held-out-tetrad-eval* gap remains open. → downgrade
  the claim, keep the design.
- *Ask-vs-assume gap*: **NOT empty.** BBQ-ambiguous family measures assume-vs-abstain; the
  *inquiry* + multi-turn transport is the residual novelty. → narrow the claim.
- *Measurement-invariance gap*: **empty (verified 0/218).** Genuine.
- *Over-adaptation (individual non-modal) gap*: **empty** as a scored-adaptation-error axis;
  needs a stereotype-benchmark carve-out for precision.
- *Diaspora/bicultural-integration gap*: **empty (verified).** Genuine.
- *Communal-unit gap*: **near-empty (1/218 verified).** Genuine; the design already states "one."

**Net:** the design bundles ~3 genuinely-empty gaps (invariance, diaspora, individual-non-modal
OA) with ~2 overstated ones (in-situ, ask-vs-assume). Fixing the two overstatements costs
nothing — the differentiated construct is stronger when honestly positioned against
NormGenesis/CASA/BBQ than when it claims a first that the corpus contradicts.

---

## VERDICT: PASS-WITH-FIXES | Critical: 0 | Major: 3 | Minor: 3

**Single most likely remaining error:** that the static single-turn "floor" tier (§6) does
**not** saturate on divergent-value items — the corpus already shows 0–1/5 static performance
on such items, so the interactive-vs-static drop (the design's headline difficulty signal) may
be small or absent for exactly the items that carry the construct, collapsing the two-tier
logic onto a single already-hard band.
