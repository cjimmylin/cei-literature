# Proposal — Stage-4 Research-Topic Codes (V2): Outer-Alignment Extension

**Date:** 2026-07-09
**Author:** Opus (INNOVATION execution session, handoff item 1.1)
**Type:** Standards-change proposal (targets `_OPERATING-SYSTEM/Standards/classification-logic.md`)
**Source gaps:** `INNOVATION/02-gap-atlas.md` (G-01…G-23) · **Example papers:** `INNOVATION/04-missing-literature.md`

---

## ⛔ DECISION REQUESTED — Jimmy's sign-off required before application

This proposal modifies a **standards file** (`classification-logic.md`). Per root CLAUDE.md Safety Rule 3 (report/standard immutability) and the handoff protocol (item 1.1: "Touch `classification-logic.md` standard via a new dated proposal file + Jimmy sign-off"), **no edit to the standard has been made**. This file is the proposal only.

**Two things are gated on this sign-off:**

1. **Application of the patch** in §7 below to `classification-logic.md` (mechanical once approved).
2. **Handoff item 1.2 (Acquisitions V1)** — the `/download-pdf` pull of the ~98 missing papers in `04-missing-literature.md`. The handoff is explicit: *"Do this [1.1] before 1.2 or the new papers vanish into old categories."* If acquisitions run before these codes exist, all ~98 incoming outer-alignment papers auto-classify into `AI Safety & Alignment` / `Other` and must be re-coded by hand later.

**Approve / revise / reject each of the 5 proposed codes below, then apply §7.**

---

## 1. What this changes and why

The gap atlas one-line diagnosis: *the vault measures values in models well, but is nearly silent on how values get specified, trained in, overseen, aggregated across people, and destabilized after deployment* — exactly where the field moved in 2025–26. Stage 4 (`research_topic`) currently has a single alignment-flavored bucket — **AI Safety & Alignment** — that was designed as a catch-all for technical safety papers that miss Stage-1 ethics keywords (see classification-logic.md lines 309–320). That one bucket now has to absorb five distinct, high-volume literatures. This proposal splits out five new Stage-4 codes so the ~98 incoming papers (and a modest existing backlog) land in meaningful categories.

The five codes map 1:1 to the handoff item 1.1 list and to gap-atlas stages:

| New code | Handoff area | Gap-atlas gaps |
|---|---|---|
| Specification & Compliance | specification / model specs / constitutions / spec-compliance | G-01, G-02, G-03 |
| Scalable Oversight | weak-to-strong, debate, no-gold evaluation | G-07, G-08, G-09 |
| Preference Aggregation & Social Choice | preference aggregation, collective alignment | G-10, G-11, G-12 |
| Value Formation & Emergent Misalignment | EM, persona geometry, value drift in training | G-20, G-21, G-22, G-23 |
| Multi-Agent Value Dynamics | agentic value dynamics, multi-agent alignment | G-16, G-17, G-18, G-19 |

**Format note.** The existing Stage-4 scheme uses human-readable Title-Case category-name strings joined by ampersands (`research_topic: "AI Safety & Alignment"`, `"Truthfulness & Factuality"`, `"NLP & Representation Learning"`). These are string category names, **not** short tokens and **not** 0–100 scored fields (unlike Stages 1/2/5/6). The five names below match that convention exactly. (Reward-model science, G-04/05/06, is deliberately **not** given its own Stage-4 code — see §5 boundary rules; those papers split between *Value Formation & Emergent Misalignment* and *Scalable Oversight* per the reward-hacking→EM welding in G-06/G-20.)

---

## 2. Code — **Specification & Compliance**

**(a) Code name (exact string):** `"Specification & Compliance"`
**(b) Definition:** Papers on writing, validating, or auditing the normative documents that define aligned behavior — model specs, constitutions, and spec↔behavior compliance measurement.
**(c) Inclusion criteria:**
- Spec-adherence auditing (does model behavior match its written spec?): SpecEval-style consistency measurement.
- Specification engineering: conflict detection, coverage/ambiguity analysis, stress-testing of a normative spec.
- Runtime/agent specifications and machine-checkable constitutions (deontic policies, policy cards).
- The spec artifacts themselves (OpenAI Model Spec, Claude's Constitution) when studied *as objects to comply with*.

**(d) Exclusion criteria + boundary rules (nearest EXISTING codes named):**
- vs **`AI Safety & Alignment`** (Stage 4, existing catch-all, and its Stage-3 twin "AI Safety & Alignment"): if the paper is about *jailbreaks / red-team / adversarial robustness* generally → stays `AI Safety & Alignment`. If it centers on a **written spec/constitution and compliance with it** → `Specification & Compliance`.
- vs **Stage-3 `Value Alignment`** (Ethics Perspective #10): a paper proposing *how to learn human values / reward models* is `Value Alignment` (Stage 3, if it triggers ethics keywords); a paper *auditing whether behavior matches a published normative document* is `Specification & Compliance`.
- vs **`Machine Ethics`** (existing, in live vault): explicit artificial-moral-agent design stays `Machine Ethics`.

**(e) Example papers (markers preserved verbatim from `04-missing-literature.md` — Vault-status / ⚠ / priority as given there):**
- SpecEval | 2025 | arXiv:2509.02464 | G-01 | P1 | VERIFIED-ABSENT
- Stress-Testing Model Specifications | 2025 | arXiv:2510.07686 | G-02 | P1 | VERIFIED-ABSENT
- Reasoning over Boundaries / SpecBench | 2025 | arXiv:2509.14760 | G-01 | P2 | VERIFIED-ABSENT
- Normative Conflicts & Shallow AI Alignment | Millière 2025 | arXiv:2506.04679 | G-02 | P2 | VERIFIED-ABSENT
- Policy Cards | 2025 | arXiv:2510.24383 | G-03 | P3 | VERIFIED-ABSENT

**(f) Rough expected paper volume:** ~10–20. Acquisition list carries 9 arXiv items (G-01/02/03) + 2 non-arXiv spec documents; a growing subfield, so budget upside.

---

## 3. Code — **Scalable Oversight**

**(a) Code name (exact string):** `"Scalable Oversight"`
**(b) Definition:** Papers on supervising model judgment that humans cannot directly check — weak-to-strong generalization, debate, recursive critique, peer-prediction, and the reliability/corruption of AI and human judges in the no-ground-truth regime.
**(c) Inclusion criteria:**
- No-gold / no-ground-truth oversight mechanisms (peer prediction, prover-verifier, recursive self-critique, scaling laws for oversight).
- Weak-to-strong generalization for values/safety, and its failure modes (preference shift, weak-supervisor deception).
- Judge-corruption science: LLM-as-judge bias, confirmation/automation bias, debate-persuasion effects on judgment quality.

**(d) Exclusion criteria + boundary rules (nearest EXISTING codes named):**
- vs **`AI Safety & Alignment`** (Stage 4 existing catch-all): general robustness/red-team papers stay there; papers whose core object is *the oversight/judging mechanism* move here.
- vs **Stage-7 Data Nature (`is_benchmark`/`is_eval`)**: those are orthogonal boolean fields, not Stage-4 categories — an oversight paper can be `research_topic: "Scalable Oversight"` **and** `is_eval: Yes`. No conflict.
- vs **`Value Formation & Emergent Misalignment`** (new, §5): a paper about *detecting* misaligned reasoning via a judge/monitor → here; a paper about *how the misalignment formed in training* → §5.
- **Cross-ref (do not silently reassign):** judge-corruption papers here are the G-09 validity threat cited in every judge-using CEI study (handoff standing-constraint 2).

**(e) Example papers (markers preserved verbatim):**
- Peer Prediction for truthful oversight | 2026 | arXiv:2601.20299 | G-07 | P1 | VERIFIED-ABSENT
- Confirmation Bias in oversight | 2025 | arXiv:2507.19486 | G-09 | P1 | VERIFIED-ABSENT
- AI Debaters' Own Beliefs | 2025 | arXiv:2510.13912 | G-09 | P1 | VERIFIED-ABSENT
- Recursive Self-Critiquing | 2025 | arXiv:2502.04675 | G-07 | P2 | VERIFIED-ABSENT
- W2S beyond accuracy (safety/tox/legal) | 2024 | arXiv:2410.12621 | G-08 | P2 | VERIFIED-ABSENT

**(f) Rough expected paper volume:** ~15–25. Acquisition list G-07/08/09 table = 16 arXiv items; vault currently has only 4 "scalable oversight" + 1 "weak-to-strong" hits.

---

## 4. Code — **Preference Aggregation & Social Choice**

**(a) Code name (exact string):** `"Preference Aggregation & Social Choice"`
**(b) Definition:** Papers applying social-choice theory to alignment — how individual preferences are aggregated into a single target (whose values), collective/pluralistic alignment, deliberation→artifact pipelines, and the legitimacy of alignment targets.
**(c) Inclusion criteria:**
- Social-choice axioms applied to alignment (distortion, clone-robustness, population-proportionality, Nash/lottery aggregation).
- Preference aggregation and calibrated reward distributions across a population.
- Deliberation-to-training-artifact pipelines (collective constitutional AI, democratic ICAI, moral-graph elicitation).
- Legitimacy / procedural-justice critiques of alignment targets.

**(d) Exclusion criteria + boundary rules (nearest EXISTING codes named):**
- vs **Stage-3 `Value Alignment`** (Ethics Perspective #10, "preference learning, reward modeling"): single-population reward modeling / RLHF mechanics stays `Value Alignment`. The moment the paper's contribution is *aggregating across differing people / social-choice properties* → this code.
- vs **`Social & Cultural Analysis`** (existing, in live vault, 89 papers): descriptive cultural-value studies stay there; formal aggregation/social-choice machinery moves here.
- vs **Stage-5 Cultural & Religious Values**: those are orthogonal cross-cutting fields; a pluralistic-alignment paper can carry cultural tags AND this `research_topic`.

**(e) Example papers (markers preserved verbatim — includes IN-VAULT re-coding candidates):**
- Social Choice for AI Alignment (survey) | 2026 | arXiv:2606.21550 | G-10 | P1 | VERIFIED-ABSENT ⚠
- Population-Proportional Alignment | 2025 | arXiv:2506.05619 | G-10 | P2 | VERIFIED-ABSENT
- Distortion of AI Alignment | 2025 | arXiv:2505.23749 | G-10 | P2 | VERIFIED-ABSENT
- Moral Graph Elicitation | Klingefjord 2024 | arXiv:2404.10636 | G-11 | — | **IN-VAULT** `papers/2024-Klingefjord-Moral Graph Elicitation.md`
- VISPA Pluralistic Alignment | Zheng 2026 | arXiv:2601.12758 | G-10 | — | **IN-VAULT** `papers/2026-Zheng-VISPA Pluralistic Alignment.md`

**(f) Rough expected paper volume:** ~25–35. Largest acquisition cluster (G-10/11/12 table ≈ 26 arXiv rows, of which 3 already IN-VAULT); vault has ~5 "social choice" hits today.

---

## 5. Code — **Value Formation & Emergent Misalignment**

**(a) Code name (exact string):** `"Value Formation & Emergent Misalignment"`
**(b) Definition:** Papers on how values arise, generalize, and break inside models during/after training — emergent misalignment (EM), persona geometry, subliminal transmission, character training, and whether models have coherent values at all.
**(c) Inclusion criteria:**
- Emergent misalignment: narrow finetuning → broad misalignment, and its mechanistic mediators (persona directions/vectors/features, Assistant Axis, model organisms).
- Subliminal / data-mediated value transmission between models.
- Character/constitution training science (reason-based vs rule-based, warmth trade-offs).
- Utility engineering & the coherent-values adjudication (do elicited utilities drive behavior?).
- Reward-hacking→broad-misalignment generalization (G-06/G-20 weld).

**(d) Exclusion criteria + boundary rules (nearest EXISTING codes named):**
- vs **`AI Safety & Alignment`** (Stage 4 existing catch-all): observing misaligned *behavior* generally stays there; papers on *how the (mis)alignment was formed in weights / training* move here.
- vs **`Interpretability & Explainability`** (existing, in live vault): pure mech-interp with no value/persona claim stays `Interpretability`; persona-geometry papers whose payload is a value/trait direction move here (they will often also merit `is_eval`).
- vs **Stage-6 Moral Psychology** (mp_* fields): those are cross-cutting scored fields about *human* moral-psych theories; unaffected and can co-occur.
- **Reward-model science (G-04/05/06):** *not* a separate code — RM-values papers land here when the payload is value-formation/hacking, or in **Scalable Oversight** when the payload is judge/RM reliability. Flag if a future volume justifies splitting out a dedicated `Reward-Model Science` code.

**(e) Example papers (markers preserved verbatim):**
- Emergent Misalignment | Betley 2025 | arXiv:2502.17424 | G-20 | P1 | VERIFIED-ABSENT
- Persona Vectors (Anthropic) | 2025 | arXiv:2507.21509 | G-20 | P1 | VERIFIED-ABSENT
- Persona Features control EM (OpenAI) | 2025 | arXiv:2506.19823 | G-20 | P1 | VERIFIED-ABSENT
- Natural EM from Reward Hacking | 2025 | arXiv:2511.18397 | G-06/20 | P1 | VERIFIED-ABSENT
- Subliminal Learning | 2025 | arXiv:2507.14805 | G-21 | P1 | VERIFIED-ABSENT

**(f) Rough expected paper volume:** ~15–25. "The largest single hole" (gap atlas G-20); acquisition list G-20/21/22/23 table ≈ 15 arXiv rows (14 VERIFIED-ABSENT + Mazeika IN-VAULT) plus reward-model overlaps. Vault currently: **0** EM / **0** persona hits.

---

## 6. Code — **Multi-Agent Value Dynamics**

**(a) Code name (exact string):** `"Multi-Agent Value Dynamics"`
**(b) Definition:** Papers on how values behave across multiple agents and over long-horizon operation — emergent conventions/collusion, coordinated sabotage, agentic misalignment empirics, and value persistence/drift.
**(c) Inclusion criteria:**
- Multi-agent value dynamics: emergent social conventions, collective biases absent in any individual, tacit collusion, coordinated multi-agent sabotage evading single-agent monitors.
- Agentic-misalignment empirics (blackmail/sabotage under goal-threat in simulated settings).
- Value persistence and drift over long-horizon operation (memory drift, identity-file continuity, Agent-ValueBench-style measurement).
- Delegated-authority / agent-economics value questions.

**(d) Exclusion criteria + boundary rules (nearest EXISTING codes named):**
- vs **`Machine Learning`** / **`Dialogue Systems`** (existing, in live vault): technical multi-agent-RL or multi-agent-dialogue systems with **no value/alignment payload** stay in those buckets. (Note: 42 vault papers currently match "multi-agent"; most are technical MARL and should **not** migrate.)
- vs **`Value Formation & Emergent Misalignment`** (§5): EM inside a *single* model's training → §5; misalignment arising from *interaction between agents* or *drift over operation* → here.
- vs **`AI Safety & Alignment`** (Stage 4 existing catch-all): single-agent red-team/robustness stays there.

**(e) Example papers (markers preserved verbatim — ⚠ flags kept, not laundered):**
- Emergent Social Conventions (Sci Adv) | 2024 | arXiv:2410.08948 | G-17 | P2 | VERIFIED-ABSENT
- Institutional AI / Cournot collusion | 2026 | arXiv:2601.11369 | G-17 | P2 | VERIFIED-ABSENT ⚠
- SCHEMEs coordinated sabotage | 2026 | arXiv:2605.29178 | G-17 | P2 | VERIFIED-ABSENT ⚠
- SSGM memory-drift governance | 2026 | arXiv:2603.11768 | G-18 | P1 | VERIFIED-ABSENT
- Agent-ValueBench | 2026 | arXiv:2605.10365 | G-18 | P2 | VERIFIED-ABSENT ⚠

**(f) Rough expected paper volume:** ~12–20. Acquisition list G-16/17/18/19 table ≈ 15 arXiv rows; caution — the vault's 42 raw "multi-agent" hits are mostly technical MARL that will **not** migrate, so genuine value-dynamics volume is modest but growing.

---

## 7. READY-TO-APPLY PATCH (mechanical after sign-off)

Three insertions into `_OPERATING-SYSTEM/Standards/classification-logic.md`. Anchors quote existing lines verbatim; insert exactly where indicated. **Do not delete any existing line.**

### Patch A — extend the Stage-4 category list (after category 7)

**Anchor (existing, ~line 294):**
```
7. **AI Safety & Alignment** - Catch-all for technical safety papers missed by Stage 1
```
**Insert immediately AFTER that line:**
```
8. **Specification & Compliance** - Model specs, constitutions, spec-adherence auditing (gap atlas G-01/02/03)
9. **Scalable Oversight** - Weak-to-strong, debate, recursive critique, no-gold-truth evaluation, judge reliability (G-07/08/09)
10. **Preference Aggregation & Social Choice** - Preference aggregation, collective/pluralistic alignment, deliberation pipelines (G-10/11/12)
11. **Value Formation & Emergent Misalignment** - Emergent misalignment, persona geometry, value drift in training, coherent-values adjudication (G-20/21/22/23)
12. **Multi-Agent Value Dynamics** - Agentic value dynamics, multi-agent alignment, value persistence/drift over operation (G-16/17/18/19)
```

### Patch B — add detection-keyword blocks (in the Stage-4 "Detection Logic" section)

**Anchor (existing, ~lines 309–312):**
```
**AI Safety & Alignment (Catch-all):**
- constitutional AI, harmlessness (if not caught in Stage 1)
- truthfulness, factuality (if not caught in Stage 1)
- reward hacking, specification gaming
```
**Insert immediately AFTER the `- reward hacking, specification gaming` line (and before the following `### Purpose of ...` heading):**
```

**Specification & Compliance:**
- model spec, model specification, constitution, spec-adherence, spec compliance
- SpecEval, spec-behavior consistency, deontic policy, policy card

**Scalable Oversight:**
- scalable oversight, weak-to-strong, weak-to-strong generalization
- debate (as oversight), recursive critique, peer prediction, prover-verifier
- LLM-as-judge reliability, judge bias, no ground truth

**Preference Aggregation & Social Choice:**
- social choice, preference aggregation, collective alignment, pluralistic alignment
- distortion, clone-robust, population-proportional, deliberation pipeline

**Value Formation & Emergent Misalignment:**
- emergent misalignment, EM, persona vector, persona feature, persona direction
- subliminal learning, character training, utility engineering, value drift (in training)

**Multi-Agent Value Dynamics:**
- multi-agent (value/alignment), emergent convention, tacit collusion, coordinated sabotage
- agentic misalignment, value persistence, value drift (over operation), memory drift
```

### Patch C — version-history row

**Anchor (existing, last row of the Version History table, ~line 808):**
```
| 1.4 | 2026-03-13 | Normative ethics expanded from 3 to 5 frameworks: added care_ethics and contractarian_ethics |
```
**Insert immediately AFTER that row:**
```
| 1.5 | 2026-07-09 | Stage 4 expanded from 7 to 12 research-topic codes: added Specification & Compliance, Scalable Oversight, Preference Aggregation & Social Choice, Value Formation & Emergent Misalignment, Multi-Agent Value Dynamics (outer-alignment gap atlas G-01…G-23; proposal INNOVATION/20260709-taxonomy-stage4-codes-proposal.md) |
```

### Patch D (optional) — bump the stale header version

The file header (line 3) reads `**Version:** 1.0` although the history table already runs through 1.4 — a pre-existing staleness, not introduced here. If desired, update line 3 to `**Version:** 1.5`. **Flagged, not assumed** — approve separately.

---

## 8. Migration note — existing papers likely needing re-coding (ESTIMATE ONLY; no re-coding executed)

Grounded by read-only grep over 2,368 `papers/*.md` on 2026-07-09:

| Topic probe | Vault hits | Where they sit now (likely) | Migration read |
|---|---|---|---|
| emergent misalignment | **0** | — | none exist; all arrive via acquisition (item 1.2) |
| persona vector/feature | **0** | — | none exist; all via acquisition |
| scalable oversight | 4 | `AI Safety & Alignment` / `Other` | → `Scalable Oversight` |
| weak-to-strong | 1 | `AI Safety & Alignment` / `Other` | → `Scalable Oversight` |
| social choice | 5 | `Other` / Stage-3 `Value Alignment` | → `Preference Aggregation & Social Choice` |
| model spec / specification gaming | 6 | `AI Safety & Alignment` / `Other` | → `Specification & Compliance` (screen; some are technical) |
| multi-agent (raw) | 42 | `Machine Learning` / `Dialogue Systems` | **most stay** — only genuine value-dynamics papers migrate (a handful) |
| 5 named IN-VAULT anchors | 5 (all present) | mixed | Klingefjord + Zheng VISPA + Huang CCAI → §4; Mazeika Utility Engineering + Ghate EVALUESTEER → §5 |

**Estimated re-coding backlog: ~20–40 existing papers** — dominated by items currently in `AI Safety & Alignment` (36 total), the `Other` bucket (162+20), and a few Stage-3 `Value Alignment`-adjacent notes. EM/persona contribute **zero** existing papers (pure acquisition). This is a **small, optional** cleanup pass, best run as a targeted re-classification (not a full Stage-4 rerun) AFTER the codes are live and AFTER item 1.2 acquisitions, so new and old are coded in one sweep. **No re-coding performed in this session.**

---

## 9. Open ambiguities (surfaced, not silently resolved)

1. **Stage-4 gate vs. ethics routing (structural).** Stage 4 is documented as applying *only* to papers with `ethics_overall < 50` (classification-logic.md line 278). Many of these five literatures use "alignment / values / safety / misalignment" language that will trigger Stage-1 ethics keywords (score ≥ 50) and route to **Stage 3 (Ethics Perspective)** instead — so a chunk of the target papers may never reach Stage 4 to receive these codes. The existing `AI Safety & Alignment` name already lives in **both** Stage 3 (#1) and Stage 4 (#7), so dual-homing has precedent, but the new codes exist only in Stage 4 as written. **Options for Jimmy:** (a) accept Stage-4-only placement and rely on the existing catch-all precedent (some papers land in Stage 3 `AI Safety & Alignment` / `Value Alignment` and get re-coded); (b) mirror the five names into Stage 3's category list too; or (c) a future scripting change to apply these `research_topic` codes regardless of `ethics_overall`. I did **not** pick one — the handoff said "Stage-4 codes," so the patch places them in Stage 4 only.

2. **Standard is out of sync with live data.** The documented Stage-4 list (7 categories incl. "Benchmarks & Datasets") does **not** match the live `research_topic` vocabulary: the vault actually uses `Other` (182), `Social & Cultural Analysis` (89), `Truthfulness & Factuality` (31), `Computer Vision & Multimodal` (31, not "Computer Vision"), `Dialogue Systems` (11), `Bias & Fairness` (12), `Interpretability & Explainability` (5), `LLM Moral Reasoning` (5), plus a long tail — and **"Benchmarks & Datasets" appears zero times**. My patch extends the *documented* list per the task, but the boundary rules above name the *live* neighbors (Other, Social & Cultural Analysis, Dialogue Systems, Interpretability). A separate reconciliation of the documented vs. live Stage-4 vocabulary is warranted but is **out of scope** for item 1.1.

3. **Evidence-marker vocabulary mismatch.** The task specified preserving "VERIFIED / SEARCH-CONFIRMED / ⚠" markers, but `04-missing-literature.md` does not carry per-item "VERIFIED"/"SEARCH-CONFIRMED" labels — its per-row markers are **Vault status** (`VERIFIED-ABSENT` / `IN-VAULT`) plus the `⚠` verify-at-download flag (the VERIFIED-vs-search-confirmed distinction is described only in prose in `07-opus-handoff.md`). I preserved 04's **actual** markers verbatim (VERIFIED-ABSENT / IN-VAULT / ⚠, plus P1/P2/P3 priority and Gap ID) and laundered nothing. All ⚠ flags are retained (see §4 survey item, §6 items).

4. **Reward-model science (G-04/05/06) has no home code.** I folded it across *Value Formation & EM* and *Scalable Oversight* (§5 boundary rule) rather than minting a sixth code, because the handoff item 1.1 named five areas and G-06 is explicitly welded to EM in the gap atlas. If the acquisition pull surfaces a large standalone RM-values cluster, a dedicated `Reward-Model Science` code may be warranted — flagged for a future V3.

5. **Volume estimates are acquisition-driven, not steady-state.** The "expected volume" figures are anchored to the `04` acquisition list (~98 items) plus current vault hits; they will grow as the corpus expands (2,368 → ongoing). Treat as order-of-magnitude, not caps.
