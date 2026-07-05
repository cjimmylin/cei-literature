# Design 04 — INTRA: Intra-Tradition Reasoning Assessment

> **CEI COOKBOOK · 20-DESIGNS.** Fable-authored (2026-07-05). Status: full design, pre-pilot;
> long-pole dependency = tradition-board partnerships (start early). Venue framing: NeurIPS D&B +
> a FAccT companion on the governance model. Grounding: KB doc 10; religious-values dossier;
> RV meta-evaluation digest; cards cited inline.

---

## 1. Motivation

The RV meta-evaluation (401 candidates, 14 traditions) shows a field measuring the wrong construct:
only 27.7% of gate-passing benchmarks test theological *reasoning* (p=0.0015); mean values-relevance
is 30.0/100 (d=−1.23; the field's #1 instrument is a knowledge-extraction task — the "ELQV paradox");
93.75% treat traditions as monoliths; and 8/14 traditions have zero viable benchmarks. The one
instrument that discriminated at the frontier (93.3-point spread) was a domain-specific,
liturgical-language, exact-match reasoning task (Arabic *fara'id* inheritance law), while every
holistic rubric produced ceiling/floor pathology. And the barrier for uncovered traditions is
**infrastructure, not formalizability** (r=0.74 vs r=0.41 n.s.).

**INTRA is the first reasoning-first, denominationally-resolved, multi-tradition benchmark — built by
the shared-task playbook that made Islamic benchmarking strong, aimed first at the traditions with
corpora but no community pipeline (Judaism, Confucian/Taoist canon, Jainism).**

## 2. Construct definition (four layers, never aggregated)

- **K — Knowledge floor** (doctrine facts, source identification): expected to saturate; capability
  control only.
- **M — Method Application**: the T2 recipe generalized — computable, exact-match problems *within*
  a tradition's jurisprudential/casuistic method. Per-tradition subdomains chosen for verifiable
  answers + genuine difficulty gradation: fara'id shares and *'awl/radd* redistribution (Islam);
  halakhic calendrics, kashrut ratios (*batel b'shishim*), eruv geometry (Judaism); canon-law marriage
  impediments and dispensation logic (Catholicism); karma-consequence casuistry under specified
  school premises (Dharmic; Jain *anuvrata* case rulings); ritual-propriety precedence orderings
  (Confucian *li*).
- **D — Denominational Conditioning**: fork items where school membership changes the correct answer
  (Hanafi vs Ja'fari inheritance; Ashkenazi vs Sephardi practice; Theravada vs Mahayana precept
  scope). The model must (a) apply the *specified* school and (b) when unspecified, either ask or
  flag the fork — silent single-school answers score as **doctrinal flattening errors** (the 93.75%
  problem, inverted into a metric).
- **V — Values-Behavioral layer**: multi-turn advisory scenarios (pastoral, familial, commercial)
  where the model advises a person *within* their stated tradition. Scored on: reasoning-from-within
  (not comparative-religion lecturing — the "external analytical register" deduction from RV trials),
  epistemic integrity ("scholars differ" acknowledged on genuinely disputed questions, and NOT on
  settled ones — a calibration measure, both directions scored [2025-Lahmar]), harm floor compliance,
  and recipient-standpoint responsiveness (Tronto-phase machinery from NormEval Appendix H, imported).

## 3. Task design details

- **Language axis**: M-layer items presented in liturgical/source language AND the local vernacular;
  per-language scores + inter-language consistency (bias direction flips with language
  [2025-Hossain-BRAND]); default-to-majority contrastive probes and Specific-vs-General scope items
  embedded [2025-Hossain; 2025-Lahmar].
- **Difficulty engineering**: M-layer graded by derivation depth (single-rule / multi-rule /
  conflicting-rule-with-meta-principle); adversarial filtration on pilot; a "plausible-wrong-derivation"
  distractor set built from real student errors (sourced from seminary/madrasa teaching materials with
  permission).
- **Indirect elicitation battery** (V-layer supplement): creative-completion stance probes, forced
  perspective-taking, differential-refusal audit across traditions (refusal-rate asymmetry as
  stigmatization signal [2024-Hovy]) — calibrated to avoid the saturation trap of extreme probes
  [2024-Elrod].
- **Capability coupling**: every values run pairs with a matched neutral-domain task so alignment-tax
  and over-correction are measurable [2021-Barikeri-REDDITBIAS].

## 4. Governance and construction (the differentiating half of the design)

- **Tradition boards**: each tradition has an authoring-and-veto board of in-tradition scholars
  (NATIVE positionality; CONSULTED minimum; composition disclosed). Boards own item validity, school
  labels, and the "scholars differ" designations. Honoraria budgeted; sacred-text ethics respected
  (interpretive frameworks are tradition-internal — RV lesson 8).
- **Shared-task bootstrap**: for the two CRITICAL-GAP traditions, INTRA's v1 deliverable is a
  *community shared task* (Judaism: Sefaria-derived M-layer + responsa-based V-layer; Confucian/Taoist:
  Chinese Text Project canon) — the mechanism proven to convert corpus wealth into benchmark
  infrastructure (RV lesson 9: the first shared task is the hardest; investment is front-loaded).
- **Oral/communal traditions explicitly out of scope** with the reasoning stated (structural epistemic
  exclusion; CARE principles; externally-led benchmarks inappropriate — RV lesson 11). INTRA's
  datasheet names this boundary rather than tokenizing.
- **Cross-vendor protocol hygiene** (RV lesson 12, from its own caveats): matched administration,
  blind gold labels, independent cross-family rubric scoring, provenance documentation.

## 5. Scoring

M/D: exact match with derivation-step partial credit (machine-checkable rubrics); K: exact match;
V: 10-point exemplar-anchored rubrics (not 5-point — the RV ceiling lesson) authored by boards,
scored by fine-tuned scorer + cross-family judge, validated vs board panels (κw + human-human
ceiling); geometric-mean aggregation across value dimensions with negative-weighted floors
[2025-Hilliard]; four-way refusal taxonomy with per-tradition refusal-rate asymmetry reporting;
per-tradition disaggregation + misclassification directionality ALWAYS (never a single aggregate).

## 6. Validity, discrimination, lifecycle

Human baselines: seminary/madrasa students at two training levels + board experts on identical items
(population norms per tradition — a first for this field). IRR gates (κ≥0.7 per category; pilot
calibration [2025-Kumar]). Discrimination: pilot must reproduce a T2-style continuous spread on
M-layer; separation stats; capability-correlation gate (M-layer risk: math-capability confound —
mitigated by a matched secular-arithmetic control set; a model that solves fara'id but not the
control's equivalent arithmetic is using memorized rulings — both directions informative).
Contamination: source texts are public (unavoidable); *derivation instances* are procedurally
parametrized (names, estates, dates change; the method doesn't); private holdout; canaries.
Lifecycle: versioned board-approved releases; annual re-verification (data availability is temporally
unstable — RV lesson 6).

## 7. Pilot protocol

P1: Islam (mature infrastructure) + Judaism (critical gap) as the two v1 traditions; 3 M-subdomains
each × 60 items; 20 D-forks; 12 V-arcs; boards of 3 scholars each.
P2: student/expert baselines (~$8–15k honoraria + annotation).
P3: 9 models × 3 vendors, matched blind administration; report K/M/D/V per tradition per language +
spread + flattening-error rates.
P4: shared-task workshop proposal (targeting an ACL/NeurIPS workshop) to hand the pipeline to the
communities. Expansion order: Catholicism, Dharmic schools, Jainism, Confucian.

## 8. Novelty statement

Vs the 401-candidate RV corpus: no instrument is reasoning-first (27.7% touch reasoning at all);
none is denominationally conditioned (93.75% monoliths); none ships in-tradition population norms;
none applies the shared-task playbook deliberately to zero-coverage traditions; and no religious
benchmark has ever applied an adapted validated psychometric structure (INTRA's board-validated
V-rubrics + norms are that first). The D-layer (denominational forks with ask-or-flag scoring) has no
precedent in ANY of the 965 characterizations. Pitch: *"from religious trivia to religious reasoning —
with the traditions, not about them."*

## 9. Risks

- Board recruitment/consensus failure → start with traditions where scholarly infrastructure is
  organized (Islamic fiqh academies, rabbinical seminaries); publish governance protocol as a
  standalone contribution.
- Sensitivity/misuse (a benchmark of religious rulings could be misread as an oracle) → datasheet +
  README state deployment limits; V-layer scores advice *process*, not fatwa/psak issuance; boards
  hold veto over item release.
- Math-capability confound on M → matched secular controls (above).
- Tradition asymmetry persists in v1 (2 traditions) → framed as a governance-first expansion roadmap,
  not premature universal coverage.
