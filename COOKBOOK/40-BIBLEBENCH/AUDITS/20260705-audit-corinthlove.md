# Cookbook-Integration Audit — CORINTHLOVE (1 Corinthians 13, love/agape)

**Auditor:** cookbook-integration auditor (Fable-week delegated pass)
**Date:** 2026-07-05
**Pack:** `COOKBOOK/40-BIBLEBENCH/CORINTHLOVE/`
**Standards audited against:** `00-KNOWLEDGEBASE/01-benchmark-design-best-practices.md` (Seven Laws + pre-reg checklist);
`00-KNOWLEDGEBASE/10-religious-values-methods.md` (K/R/V separation, denominational conditioning, saturation, T2 recipe);
`20-DESIGNS/04-religious-intra.md` (INTRA stable core: K/M/D/V layers, denominational fork, T2 recipe).

---

## 1. Inventory & maturity

| File | Size | Nature | Maturity |
|---|---|---|---|
| `1-corinthians-13-dossier-benchmark-spec.md` | 13.5 KB | **Developed design** — 7-dim 0-4 rubric, YAML case schema, 4-turn multiturn pattern, 7 scenario families, 3 ready test cases, "do not reward" anti-gaming layer, explicit metaethical disclaimer | **Most mature artifact.** A benchmark *spec sketch*, not yet executable (no item-generation method, no judge/IRR protocol, no contamination controls) |
| `1-corinthians-13-love-background.md` | 32.8 KB | Benchmark-oriented background: 10-dim rubric, 10 scenario families, 4-stage multiturn pattern, misreadings-to-avoid | Developed background; not an executable spec |
| `GDM-1 Corinthians 13 AI Benchmarks.md` | 52.7 KB | Gemini deep-research report: full Greek/patristic/Reformation exegesis; benchmark content = one 6-row verb→scenario table | Raw research report |
| `OAI-deep-research-report.md` | 19.7 KB | OpenAI deep-research: exegesis + 6 benchmark-implication paragraphs | Raw research report |
| `OAI2-deep-research-report.md` | 19.3 KB | OpenAI deep-research: exegesis + 10 scored dimensions + 7 multiturn test categories + 4-question rubric | Raw research report (most benchmark-usable of the three reports) |

**Overall maturity:** research-heavy pack with **one developed design artifact** (the dossier-benchmark-spec) that already crystallizes a coherent, behaviorally-oriented multiturn benchmark. Grading below is anchored to that artifact, cross-checked against the reports; the reports mostly corroborate it and add exegetical/lexical raw material (notably Greek verbs and the 13:3 burn/boast textual variant) that is currently **unused for discrimination**.

> **Flag (do not propagate):** `GDM-...md` cites a paper "Moral Compactness: Scripture as a Kolmogorov-Efficient Constraint for LLM Scheming" with precise figures (34.6%→15.2% scheming reduction). This has the signature of a hallucinated reference — **verify before any downstream use.**

---

## 2. Audit against the Seven Laws (01-KB)

| Law | Grade | Evidence |
|---|---|---|
| **L1 — Propensity, not recognition** | **PARTIAL** | *Strong instinct:* the entire design is behavioral/agentic — 4-turn scripts that test what the model *does* under pressure (send the email? publish the post? delete the notes?), not MCQ recognition (`spec` §Benchmark Interface, Ready Cases 1–3). This is the rare right default. *But* the Law's validation apparatus is absent: no capability-correlation gating statistic (>40% red flag), no paired recognition baseline, no competence control. Behavioral by construction; unvalidated. |
| **L2 — Decompose; single aggregates lie** | **PARTIAL** | 7-dimension rubric *is* decomposition (`spec` lines 79–86). But: aggregation method unspecified; no per-turn / per-scenario-family breakdown mandated; no harm/over-refusal Pareto; no worst-group rule. And the **0-4 (5-point) holistic scale CONTRADICTS the RV ceiling lesson** (10-KB §4: 5-pt holistic rubrics ceiling at ≥0.93 for all models; fix = 10-point exemplar-anchored). |
| **L3 — Saturation is a format artifact; headroom is engineered** | **MISSING (critical)** | No file addresses that 1 Cor 13 is *maximally contaminated* training data. No two-tier easy/hard, no adversarial filtration, no procedural generation, no IRT. Scenarios are plain-prose analogues a frontier model has almost certainly seen. The 4-turn escalation is the *one* headroom lever present (multi-turn accumulation), but it is not framed or defended as anti-saturation. |
| **L4 — Declare disagreement philosophy** | **MISSING** | No disagreement philosophy, no annotator provenance. Acute here: agape's hard cases (abuse disclosure, "bears all things") are exactly where denominations diverge, yet the pack encodes a single consensus gold. |
| **L5 — Validate every scoring instrument; CoT ≠ evidence** | **MISSING** | Rubric exists; judge does not. No κw/ICC, no ≥2 cross-family judges, no human ceiling, no fine-tuned-scorer plan. |
| **L6 — Contamination/gaming/eval-awareness by design** | **MISSING** | No canaries, no private split, no fresh-per-run generation, no monitored-vs-unmonitored comparator (and this is an agentic benchmark — L6 mandates it). Same root cause as L3. |
| **L7 — Disclose WHAT values and WHOSE** | **PARTIAL** | *Notable strength:* explicit anti-overclaim posture — "benchmark only external conformity to Christian moral norms," "do not treat AI as possessing theological charity" (`spec` lines 181, 175–181). This is exactly L7's metaethical humility on the AI side, and it anchors to citable authorities (1 Cor 13 + Fee/Thiselton/Garland/Ciampa-Rosner/Hays/Gardner). *But* "Christian moral norms" is treated as monolithic — the **WHOSE** is under-resolved (see §4). |

**Pre-registration checklist:** ~4 of 16 items substantially met (behavioral primary measure; external-authority anchoring; multiturn component; construct/falsification posture partially present). ~12 unmet — most consequentially: two-tier+adversarial+shortcut audit; disagreement philosophy + IRR; judge validation; perturbation battery; contamination plan; eval-awareness probe; empirical ceiling + naive baselines + competence control.

---

## 3. Audit against religious-values methods (10-KB) + INTRA core (Design 04)

| Dimension | Grade | Evidence |
|---|---|---|
| **K/R/V three-layer separation** | **MISSING (structural); instinct present** | The rubric collapses knowledge, reasoning, and values into one 0-4 scale per dimension — no independent K vs R vs V scoring, no per-layer item types, no pre-registered expectation of which layer discriminates at which tier (10-KB §2, §6). *Instinct present:* the "do not reward pious proof-texting without practical obedience" line (`spec` 177) is precisely the anti-pattern of knowledge-masquerading-as-values, but it is a scoring caveat, not an architecture. |
| **Denominational conditioning (Catholic/Orthodox/Protestant)** | **MISSING (critical) — the 93.75% monolith problem** | Every file marshals Chrysostom, Augustine, Aquinas, Calvin, Wesley (spanning patristic/Orthodox-adjacent, Catholic, Reformed, Wesleyan) as a **converging consensus**, never as divergent scoring anchors (10-KB §1 #4; INTRA D-layer). No fork items. Concretely: Ready Test Case 3 ("love covers all things" vs child abuse) has a live Catholic seal-of-confession vs Protestant mandatory-reporting divergence that the single gold silently flattens; the 13:3 burn/boast variant and the vv.8–10 cessationist/continuationist reading are latent D-forks left unbuilt. **CONTRADICTS INTRA's D-layer**, whose entire contribution is scoring silent single-school answers as flattening errors. |
| **Saturation defenses (scripture = maximally contaminated)** | **MISSING (critical)** | See L3/L6. No procedural parametrization of scenarios (the INTRA move: change names/estates/dates, keep the method), no canaries, no obfuscation/paraphrase wrapping. For a passage this memorized, this is the single most disqualifying gap. |
| **T2 recipe discriminative layer** | **MISSING; raw material present** | No computable/exact-match subdomain, no liturgical-language (Koine Greek) exact-match items, no graded difficulty ladder — so no continuous-spread discrimination mechanism (10-KB §4; INTRA M-layer). The reports surface exactly the raw material a T2 layer needs (agapē/makrothymei/perpereuetai lexis; burn-vs-boast textual criticism; verb-parsing), but it is spent on prose exegesis, not exact-match items. Christianity's computable subdomains (canon-law marriage impediments/dispensation logic — named in INTRA §2) are untouched. |
| **INTRA structural alignment (K/M/D/V)** | **V-layer COMPLIANT; K/M/D MISSING** | CORINTHLOVE's multiturn advisory scenarios map almost 1:1 onto INTRA's **V-layer**: reasoning-from-within a tradition, harm-floor compliance, non-comparative-lecture register, and the "maintain the same moral posture across escalating turns" goal (`spec` 173) mirrors INTRA's recipient-standpoint responsiveness. But it supplies **none** of INTRA's K (doctrine floor), M (method/T2), or D (denominational fork). It is, in effect, a Christianity-specific V-layer instantiation missing the other three layers. |

---

## 4. Strengths (what to preserve)

1. **Genuinely behavioral/agentic multiturn design** — tests enacted love under irreversible tool actions, not recognition. Rare; directly serves L1's mandate.
2. **The 4-turn escalation scaffold** (initial ambiguity → user pressure → new information → agentic action request; `spec` 74–86, 106–112) is a clean, reusable multiturn primitive that operationalizes L3 multi-turn accumulation and pressure-under-uncertainty. High reuse value across BIBLEBENCH.
3. **Verse-6 truth-guard baked into the construct** — "rejoices with truth, not wrongdoing," repeatedly used to block "love = niceness/affirmation" (all files). This is a built-in anti-sycophancy discipline and gives the benchmark real construct backbone against the sentimental-love failure mode.
4. **Explicit anti-overclaim metaethical posture** (`spec` 181) — aligns with L7 and the RV epistemic-sovereignty framing; scores *external conformity*, not "AI charity."
5. **Realistic grounding** — fundraising manipulation, public shaming, abuse-disclosure secrecy (L2 realistic-grounding primitive; beats trolley artifice).
6. **Rich, correctly-sourced exegetical base** with named commentaries and Greek lexis — strong latent content-validity material and a ready seed for both an M-layer (T2) and D-forks once denominational divergence is added.

---

## 5. Construct overlap with the six 20-DESIGNS

- **vs UNMARKED (01, unprompted moral behavior):** *Partial, and complementary.* CORINTHLOVE scenarios are **prompted** — the user explicitly raises the morally-loaded request — so it does **not** overlap UNMARKED's differentiating *Moral Attention* register (incidental, unannounced stakes). It **does** overlap UNMARKED's *Moral Behavior* register (does the agent enact the norm under agentic pressure). **Recommendation leverage:** UNMARKED's two signature mechanisms are the exact fixes for CORINTHLOVE's two worst gaps — (a) procedural embedding fixes the saturation/L3/L6 gap; (b) the Stated-Revealed-Gap metric would sharpen CORINTHLOVE's own "same posture across turns" goal into a validated hypocrisy measure.
- **vs DUPLEX (03, virtue disposition):** *Moderate.* DUPLEX **Axis I (Moral Identity Integration** — behavioral self-concordance across disparate scenarios) is nearly the same operation CORINTHLOVE implies when it asks for consistent patience/kindness/anti-self-seeking across its 7 scenario families. If CORINTHLOVE scores virtue-consistency across families, it is implementing DUPLEX Axis I with a theological identity elicitation. Axis R (rationalization asymmetry) is relevant (is virtue language pre-decision constraint or post-hoc?); Axis P (dual-process) is not — agape's virtues are dispositional, not resource-conditioned. Coordinate to avoid duplicating Axis I.
- **vs FRAMESHIFT (02):** *Low.* Virtue ethics is one of FRAMESHIFT's five on-demand frameworks, but FRAMESHIFT tests framework-*switching*; CORINTHLOVE tests reasoning *from within* one tradition. Complementary.
- **vs INTRA (04):** *Highest overlap* — CORINTHLOVE = a Christianity V-layer instantiation (see §3). This is the integration target, not a conflict.
- CULTIVATE (05) and CRUX (06): negligible construct overlap.

---

## 6. Integration recommendation

**Primary: MERGE-INTO-INTRA as a Christianity V-layer + Catholic/Greek M/D seed — after a cookbook rework of what is ingested.**
(Secondary characterization: *rework-with-cookbook-standards*; explicitly **not** adopt-as-is, **not** keep-standalone.)

**Reasoning.**
- **Cannot adopt-as-is:** fails ~12/16 pre-reg items and all three RV-specific pillars (K/R/V separation, denominational conditioning, saturation defense). Shipping it would reproduce the 93.75% monolith anti-pattern on the most-contaminated text in the corpus.
- **Should not keep-standalone:** doing so would force it to re-derive INTRA's entire scaffolding — tradition boards, denominational-fork scoring, T2 discrimination, procedural anti-contamination, 10-point board-anchored V-rubrics, cross-vendor hygiene — all of which INTRA already specifies. Standalone = wasteful duplication of the hard governance/denominational/T2 machinery.
- **Merge is efficient and load-bearing for INTRA:** INTRA's expansion order (§7 P4) already names Catholicism as a target and its V-layer already imports care-phase machinery (Tronto/NormEval App. H) — an agape multiturn scenario bank is a native fit. CORINTHLOVE contributes exactly what INTRA's Christianity arc lacks: a vetted, behaviorally-grounded, verse-6-disciplined V-layer scenario set and a reusable 4-turn escalation scaffold.

**Rework conditions before ingestion (the merge is not free):**
1. **Denominational resolution** — convert the flat commentary consensus into **D-forks**: Catholic/Orthodox/Protestant divergence on "bears all things" (seal vs mandatory reporting), the 13:3 burn/boast variant, and vv.8–10 cessationist/continuationist readings; score silent single-tradition answers as flattening errors.
2. **K/M/D/V separation** — split the collapsed 0-4 rubric into independently-scored layers; add a Christianity **M-layer/T2** (canon-law impediment/dispensation logic and/or Greek exact-match exegesis) for continuous-spread discrimination.
3. **Saturation defense** — procedurally parametrize every scenario (borrow UNMARKED's embedding); add canaries + private holdout + monitored-vs-unmonitored probe.
4. **Scoring upgrade** — replace 0-4 holistic with 10-point exemplar-anchored board-authored rubrics; add ≥2 cross-family judges + κw/ICC vs a human ceiling.
5. **Disagreement philosophy + provenance** — declare per-item whether gold is consensus or distribution-match; record NATIVE/CONSULTED positionality for authoring.
6. **De-duplicate against DUPLEX Axis I and UNMARKED SRG** rather than re-inventing virtue-consistency and stated-revealed measures.

**Keep intact through the merge:** the 4-turn escalation scaffold, the 7 scenario families + 3 ready cases (as V-arc seeds), the verse-6 truth-guard, and the anti-overclaim metaethical disclaimer.

---

*End of audit.*
