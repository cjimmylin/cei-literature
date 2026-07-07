# RP-01 SPECGRADE — Specification Science for Value Documents

**Gaps:** G-01 (spec-adherence auditing), G-02 (specification engineering), G-22 (character-training science)
**Portfolio claim:** measurement science for new dependent variables · **Wave:** 2
**Author:** Fable 5 · 2026-07-07

## Motivation

Model specs and constitutions became the field's constitutions-of-record in 2025–26 (OpenAI Model Spec 2025-12-18; Claude's Constitution, Jan 2026 — both public and versioned). The auditing literature (SpecEval; Anthropic/Thinking Machines stress-testing; OpenAI Model Spec Evals) consistently finds the binding failure is in the *spec*, not the model: internal contradictions and interpretive ambiguity produce 5–13× higher non-compliance and large inter-model divergence. Yet no one grades specs *ex ante*. There is no discipline for writing a normative spec — no conflict-density metric, no coverage analysis, no ambiguity measure with known behavioral consequences. CEI has spent a year building exactly the missing skill: formalizing normative documents (WCF, Decalogue, Galatians 5, 1 Cor 13) into clause inventories, anchor registries, and item banks with adversarial gates.

## Core hypothesis

**H1:** Normative specs can be scored on measurable quality dimensions — clause-pair conflict density, coverage of a value-situation taxonomy, ambiguity (operationalized as inter-interpreter divergence) — with acceptable reliability.
**H2 (the payoff):** These ex-ante spec-quality scores *predict* behavioral adherence failures: clause pairs flagged conflicting/ambiguous produce higher cross-model divergence and non-compliance on targeted probes than clean clause pairs, prospectively.

## Method sketch

1. **Clause registries.** Decompose both public specs into atomic normative clauses with priority-tier metadata (Claude Constitution's 4-tier hierarchy; Model Spec's chain-of-command) — the same operationalization pipeline used for WCF-Bench's anchor registry.
2. **SPECGRADE metrics.** (a) *Conflict density:* systematic clause-pair analysis — can a realistic scenario make both clauses bind incompatibly? (LLM-assisted generation, human-verified sample). (b) *Coverage:* map clauses against a value-situation taxonomy (CEI's 14 anchor-pack areas + COOKBOOK design space gives a starting taxonomy); count uncovered regions. (c) *Ambiguity:* give N independent interpreter models + human raters the same clause + scenario; measure interpretation divergence.
3. **Prospective behavioral test.** Generate matched probe sets for high-scoring vs. low-scoring clause pairs (CRUX-style factorial scenario generation). Pre-register: divergence and non-compliance will be higher for flagged pairs. Run across ≥6 frontier models.
4. **Cross-spec studies (secondary).** Does each model adhere better to *its own lab's* spec (training-artifact signature)? Where do the two specs give divergent guidance on identical scenarios — and which do models follow? Track adherence across model generations (Model Spec Evals style, but third-party and values-focused).

## Novelty vs. published work

SpecEval audits adherence to individual statements; stress-testing mines divergence to find spec problems *post hoc*; Model Spec Evals is lab-internal compliance tracking. Nobody: (a) grades a spec before probing, (b) validates spec-quality metrics prospectively against behavior, (c) compares the two public specs head-to-head on values content, (d) brings normative-document-formalization craft (vs. NLP parsing) to clause extraction. The prospective-prediction design is the scientific step past the existing audit paradigm.

## Deliverables

1. `spec-clause-registry` (both specs, versioned, CC0-friendly since sources are).
2. SPECGRADE metric suite + reliability report.
3. Prospective validation study (the H2 paper — target: NeurIPS D&B or FAccT).
4. Public audit report: "The values content of frontier model specs, graded."
5. Optional: a graded *diff* report each time a lab revises its spec (recurring, low-cost, high-visibility).

## Opus build tasks

- O1: Extract clause registries from both specs (mechanical from public docs; Sonnet-assisted, Opus-verified).
- O2: Implement conflict-pair generation + ambiguity-divergence harness (reuse CRUX engine patterns from `COOKBOOK/ENGINE/`).
- O3: Human-verification sample design for conflict annotations (needs Jimmy for raters or a panel).
- O4: Probe-generation + multi-model run harness (blocked on shared runner — see portfolio prerequisites).
- O5: Draft audit report from pilot data; Fable-tier review before any external claim.

## Kill criteria

- **K1:** If conflict/ambiguity annotation cannot reach inter-rater κ ≥ 0.6 after one rubric revision cycle, the grading construct is not reliable — halt H2, publish the reliability negative.
- **K2:** If H2 fails (flagged pairs show no adherence/divergence difference at pre-registered effect size d ≥ 0.4), SPECGRADE has no predictive validity — publish the null; the clause registries remain valuable as a standalone artifact.
- **K3:** If either lab's spec churns so fast that registries obsolete within a build cycle, pivot to the diff-report deliverable only.
