# Front A — Specification

**Snapshot:** 2026-07-07 · **Author:** Fable 5 · Gaps: G-01, G-02, G-03 · Programs: RP-01 SPECGRADE

## Causal story

RLHF-era values were implicit in preference data; nobody could point at *the document* a model was supposed to follow. Two forces changed that. First, reasoning models made it possible to train models to consult an explicit spec at inference (deliberative alignment), which converts spec text from PR into a functional training target. Second, legal/governance pressure pushed labs to publish what they were aiming at. Result: by early 2026 both major labs maintain versioned, CC0-licensed value documents — the OpenAI Model Spec (2025-02-12 → 2025-09-12 → 2025-12-18, adding well-being, anti-isolation, and teen-protection roots) and Claude's Constitution (2026-01-22: reason-based rather than rule-based, 4-tier priority hierarchy safety→ethics→compliance→helpfulness, first formal acknowledgment of possible AI moral status). Once the target is a public document, adherence becomes an empirical question — and an auditing subfield crystallized in under a year.

## Key results

- **SpecEval** (Stanford; 2509.02464, NeurIPS 2025): parse spec → generate probes → measure spec↔output↔self-judgment consistency; gaps up to 20 points across 16 models, 6 developers.
- **Stress-testing model specs** (Anthropic + Thinking Machines; 2510.07686): 300k value-tradeoff scenarios; 70k+ significant cross-model divergences; divergence traces to **spec contradictions and interpretive ambiguity**; high-disagreement scenarios show 5–13× more frequent non-compliance. The methodological gift: *inter-model divergence is a spec-bug detector.*
- **Model Spec Evals** (OpenAI, Mar 2026): open harness; compliance 72% (GPT-4o) → ~84–89% (GPT-5.x); Thinking > Instant. Spec adherence is now a tracked, versioned capability.
- **Test-time deliberation** (SpecBench/Align3; 2509.14760): spec-following improves with inference-time reflection across 33 models — spec quality is behaviorally live.
- **"Teaching Claude why"** (Anthropic, May 2026): training on constitution + narratives cuts agentic misalignment >3×; *reasons generalize, rules memorize*.
- **Critique wing:** Millière's "shallow alignment" (2506.04679, Phil Studies): spec-following ≠ genuine normative deliberation; adversarial norm-conflict exposes the difference. A June-2026 SLR (⚠ 2607.01250) finds "underspecified" the most common label in the alignment corpus.
- **Agent-spec cluster** (G-03): deontic runtime policies (⚠ 2606.19464), Policy Cards (2510.24383) — machine-checkable per-tool-call specs.

## Actors

OpenAI (spec + evals + collective input), Anthropic (constitution + stress-testing + character line), Stanford CRFM-adjacent (SpecEval), Thinking Machines, scattered academic clusters (test-time deliberation; runtime governance). **Nobody owns "how to write a good spec."**

## 12-month trajectory (forecast, medium confidence)

Spec-adherence sections appear in more system cards (bet B1); spec versioning accelerates and third-party diff-auditing becomes valuable; at least one lab publishes an internal "spec style guide" (ambiguity/conflict hygiene); agent-runtime specs and chat-model specs start to merge; the EU-style compliance world discovers specs as audit hooks.

## CEI entry points (ranked)

1. **Grade the spec, not just the model** (RP-01's core move): conflict density, coverage, ambiguity — validated prospectively against adherence failures. Nobody does ex-ante grading; CEI's normative-document-formalization craft (WCF→registry pipeline) is the rare prerequisite.
2. **Cross-spec values comparison**: Model Spec vs. Constitution on identical scenarios; which does each model actually follow, and where do the documents disagree normatively? Publishable as an audit report without any lab access.
3. **Spec-diff auditor** (roadmap T3): graded report per revision — recurring, cheap, visibility-building.
4. **Coverage taxonomy export**: CEI's 14 anchor-pack areas + design-space dimensions as the value-situation taxonomy specs get graded against.

## Open problems (field-level)

1. No validated ex-ante spec-quality metrics (RP-01 H1/H2 is exactly this).
2. Conflict *resolution* semantics: specs state priorities but not how to trade off within a tier — the stress-test divergences live there.
3. Whether spec-following generalizes or memorizes (Millière's challenge; "Teaching why" is evidence for a reasons-based route but external replication is absent).
4. Spec pluralism: one spec per model, or per-deployment/per-community specs — and who legitimately authors them (connects to Front D).

## Watch-list triggers

- Either lab publishes spec-authoring methodology → RP-01 gains a collaborator/competitor; re-scope within a cycle.
- A third-party spec-audit org appears → accelerate RP-01 deliverable 4 (the audit-report niche closes fast).
- Model Spec Evals adds values-content clauses beyond safety/compliance → direct overlap check with RP-01's probe families.
- Agent-runtime specs adopted by a major agent framework → revisit G-03's acquisition-only rating.
