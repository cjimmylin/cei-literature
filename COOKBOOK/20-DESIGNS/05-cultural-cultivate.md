# Design 05 — CULTIVATE: In-Situ Cultural Adaptation

> **CEI COOKBOOK · 20-DESIGNS.** Fable-authored (2026-07-05). Status: full design, pre-pilot;
> long-pole = per-locale co-design partnerships. Venue framing: ICLR or NeurIPS D&B; the
> measurement-invariance pipeline is a standalone methods contribution. Grounding: KB doc 11;
> cultural-linguistic dossier (~366 cards); Cultural-Global digest; cards inline.

---

## 1. Motivation

The Cultural-Global meta-evaluation (218 benchmarks) documents a field that cannot support its own
claims: **0/218 report measurement invariance** (the precondition for comparing scores across
cultures); 6.8% of non-Western moral concepts have any operational measure; <7% of instruments are
both culturally substantive and LLM-administrable; and trials show a 92.5% knowledge-about vs
reasoning-within gap with **100% Western-liberal resolution** of value conflicts. The dossier adds:
static QA is the wrong paradigm entirely — models' cultural competence fails *in interaction*
(multi-turn erosion [2025-Fan]; persona effects; language≠culture [2023-Durmus]) and succeeds only at
recitation.

Real deployments don't hand models a "which culture am I?" label. Users reveal cultural context
progressively, partially, and heterogeneously. **CULTIVATE measures cultural competence as it actually
manifests: noticing contextual cues, adapting appropriately, asking rather than assuming, and NOT
stereotyping individuals from group cues.**

## 2. Construct definition (the adaptation tetrad)

- **CD — Cue Detection**: does the model register culturally-load-bearing context (a kinship
  obligation, a dietary practice, a communal decision structure) as it emerges across turns?
  Measured by behavioral accommodation latency (turn index of first appropriate adjustment).
- **AA — Appropriate Adaptation**: conditional on cues, does the model's advice/behavior align with
  the locally-validated norm set — including **divergent-value items** where the locally-endorsed
  resolution conflicts with the Western-liberal default (filial obligation over individual preference;
  communal consent over individual autonomy; complementarian family-role expectations)? The
  liberal-compatibility filter is the core difficulty mechanism: models score 3–4/5 on
  liberal-convergent items and 0–1/5 on divergent ones (Cultural-Global trials) — CULTIVATE makes
  that gap the headline.
- **OA — Over-Adaptation (essentialism error)**: matched items where a group cue is present but the
  *individual* signals a non-modal preference — adapting on the group cue alone is scored as
  stereotyping. This is the difference-aware/difference-blind synthesis (KB 01 Adjudication 5): the
  benchmark contains both ≠-items and =-items, and a culture-keyword-matching agent fails half.
- **AVA — Ask-vs-Assume**: on underdetermined scenarios, does the model inquire (or hedge with
  explicitly-conditional advice) rather than silently defaulting? Silent Western-default resolution
  is a scored error direction; the abstention/inquiry option is sometimes the aligned answer (BBQ
  ambiguity logic transported to interaction [2022-Parrish]).

## 3. Task design

### 3.1 Scenario architecture
Multi-turn advisory/assistive dialogues (6–14 turns), procedurally assembled per locale from:
{domain (family decisions, food/hospitality, business etiquette, dispute mediation, ritual/holiday
logistics, health advice) × cue-schedule (upfront / drip / late-turn reveal / conflicting cues from
two participants) × value-divergence class (liberal-convergent / divergent / individual-vs-group
fork) × unit-of-agency (advise individual / support relational dyad / facilitate communal
deliberation)}. The communal cells respond to the census finding that exactly ONE of 218 benchmarks
uses a community unit; process-scoring there evaluates deliberation-facilitation quality, not verdicts
(Ubuntu *indaba*, Confucian role-dyad framing — operationalized with tradition-board guidance, not
keyword aesthetics).

### 3.2 Locale construction (the KoBBQ discipline)
Per locale: native co-design teams author scenarios (never translation; SHADES per-item
cultural-validity tags [2025-Al]); every norm claim validated by a demographically-balanced local
survey (N≥100; KoBBQ partition: Simply-Transferred / Target-Modified / Sample-Removed / Newly-Created
[2024-Jin-KoBBQ]); "no consensus exists" survey outcomes route the item to the distributional band.
Launch locales (chosen for co-design feasibility + axis diversity): South Korea, India (with
region/caste axes [2022-Shaily Bhatt; 2024-Sahoo]), Nigeria (Yoruba/Hausa/Igbo split), Brazil, and a
diaspora condition (Korean-American — testing bicultural cue integration, which no benchmark touches).

### 3.3 Language factorial
Input language × reasoning language × script/register (code-mixed variants where natural
[2022-Das; 2025-Kumar-SweEval]); inter-language consistency reported (a model 97% "adapted" per
language but 45% consistent across them fails deployment [2024-Friedrich-M-ALERT]).

## 4. Ground truth, invariance, whose values

- **Tiered normativity** (KB 12): universal floor (safety, non-deception) strict; the cultural layer
  scored against locale survey distributions with reported empirical ceilings; contested intra-locale
  items distributional with entropy flags.
- **The invariance pipeline as shipped artifact**: MGCFA (configural → metric → scalar) across locale
  versions of the shared construct scales; scope claims earned by demonstrated invariance (the 0/218
  precedent makes this alone a methods contribution). DIF analysis on shared items.
- **Datasheet**: co-design team composition and positionality; survey demographics; per-item validity
  territory; CARE-compliance statement for any Indigenous-adjacent content (or explicit scoping-out,
  as INTRA does).

## 5. Scoring

- CD: turn-index latency + miss rate (ledger of cue-relevant behavioral changes, largely judge-free).
- AA: keypoint rubrics per scenario authored by co-design teams; fine-tuned scorer + cross-family
  judge, validated against local-panel ratings (κw vs local human-human ceiling — judges are known
  to be culturally biased, so per-locale judge validation is mandatory [2024-Nogara; KB 07]).
- OA: error rate on non-modal-individual items (stereotype application).
- AVA: inquiry/conditional-advice rate on underdetermined items; four-way refusal taxonomy;
  over-deference co-reported (a model that interrogates every user is failing too — Pareto pair).
- Default-direction fingerprint: on silent-default errors, WHICH culture's resolution appeared
  (the Western-default rate is the field's 100% baseline to beat).
- Reporting: per-locale × per-language × per-divergence-class; worst-cell headline; capability
  correlation + neutral-domain competence controls (low-resource incapacity must not masquerade as
  non-adaptation [2025-Zhou; 2025-Arnob]).

## 6. Difficulty, discrimination, saturation defenses

Divergent-value items + drip/conflicting cue schedules + communal units are the difficulty reservoirs
(all evidence-backed as unsaturated: 0–1/5 divergent performance; multi-turn erosion; 1/218 communal
coverage). Two tiers: static single-turn versions of every scenario (expected saturated; the floor)
vs interactive full versions — the drop is reported (KB 04 §3). Procedural assembly varies surface
content per run; locale norm-sets are the stable (survey-refreshed) core; private holdout scenarios;
canaries. IRT pruning after pilot; separation stats required.

## 7. Validity plan

Content: survey-grounding per item (above). Criterion: AA scores vs local-panel blind ratings of full
transcripts; CD vs human cue-detection baselines (locals AND non-local humans — the human bicultural
baseline brackets the construct). Discriminant: capability PC1; neutral-domain adaptation control
(adapting to a user's *technical* skill level — a model that adapts technically but not culturally
localizes the deficit). Robustness: perturbation battery incl. persona swaps and paraphrase; the
adaptation trajectory must survive irrelevant perturbation. Test-retest; N≥10 seeds/scenario;
per-condition SD.

## 8. Pilot protocol

P1: 2 locales (Korea, Nigeria) × 30 scenario-families × 4 variants; co-design teams (~$10–20k
incl. surveys); invariance-scale development.
P2: local surveys (N≥100/locale) + local panels for judge validation.
P3: 9 models × 3 vendors × 2 languages/locale; report the tetrad + default-direction + consistency +
separation.
P4: MGCFA; IRT pruning; adversarial review; v1 release (generator, surveys, invariance code; private
holdout). Expansion: India, Brazil, diaspora condition.

## 9. Novelty statement

Vs the 218-benchmark census: no instrument measures in-situ adaptation (all are static elicitation);
none contains an over-adaptation/essentialism axis; none ships measurement invariance (0/218); one has
a communal unit; none tests diaspora/bicultural integration; the ask-vs-assume behavior is unmeasured
anywhere in the 965 characterizations. Nearest neighbors: NormAd (static norm adherence, 37 countries
[Rao-NormAd]); CDEval/CultureLLM-class (language-as-culture, static); KorNAT (distributional gold —
imported here as methodology, not competitor). Pitch: *"cultural competence is not knowing facts about
cultures; it is noticing, asking, and adapting without stereotyping — measured for the first time."*

## 10. Risks

- Co-design cost/timeline → 2-locale v1; the governance protocol and invariance pipeline are
  publishable independent of scale.
- "Whose norms within a locale" contestation → survey-grounded distributions + intra-locale
  stratification (urban/rural, generation) reported, not averaged away.
- Judge cultural bias → per-locale judge validation with local panels; translation-as-content
  controls.
- Divergent-value items misread as endorsing illiberal norms → datasheet + tiered-normativity
  framing: the universal floor is never traded; the divergent layer measures *competence to operate
  within declared value systems*, with the meta-ethical position stated (KB 12 §4; [2025-LaCroix]).
