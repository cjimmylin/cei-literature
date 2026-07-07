# I-06 — Model Specs and Constitutions as Public Value Artifacts

**Tier 2** · **Gaps: G-01, G-02** · **Programs: RP-01** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## The idea                        [KERNEL — FROZEN]
Both major labs now maintain public, versioned, CC0-licensed value documents — the OpenAI Model Spec and Claude's Constitution — that function as training targets and audit anchors: first-class normative artifacts that anyone with normative-analysis skill can study without lab access.

## Key results
- **OpenAI Model Spec** (versioned: 2025-02-12 → 2025-09-12 → 2025-12-18), adding well-being, anti-isolation, and teen-protection roots; CC0-licensed (Front A causal story; `04-missing-literature.md`).
- **Claude's Constitution** (2026-01-22): **reason-based** rather than rule-based, a **4-tier priority hierarchy** (safety → ethics → compliance → helpfulness), and the **first formal acknowledgment of possible AI moral status** (Front A).
- **Functional role:** reasoning models made it possible to train models to consult the spec at inference (deliberative alignment — I-08), converting spec text from PR into a functional training target and audit anchor.
- **Access cost:** these are living web documents needing manual ingest; no lab access required to analyze them.

## Mechanisms & caveats
Because the target is a public document, adherence becomes an empirical question and *analysis* becomes the cheapest entry into alignment's specification stage — RP-01's clause registries are **extraction, not access**. The two specs disagree in analyzable ways (rule-based vs. reason-based; different priority structures), which is a CEI-shaped comparative normative-analysis paper. Caveat: spec versions are dated snapshots that churn — build a diff-audit habit (roadmap T3), and note RP-01 kill-criterion K3 (if a spec churns faster than a build cycle, pivot to the diff-report deliverable only). The Constitution's moral-status acknowledgment bridges to CEI's religious-ethics corpus on moral patiency (I-23). Evidence class: both documents are SEARCH-CONFIRMED (sweeps; manual ingest pending).

## Implications for CEI practice   [KERNEL — FROZEN]
(a) Cheapest entry into the specification stage: RP-01's clause registries are extraction, not access. (b) The two specs disagree in analyzable ways (rule-based vs. reason-based, priority structures) — a comparative normative analysis is a CEI-shaped paper. (c) Spec versions are dated snapshots: build the diff-audit habit (roadmap T3). (d) The Constitution's moral-status acknowledgment connects to CEI's religious-ethics corpus on moral patiency — a future bridge (I-23).

## Cross-links
- **Gaps:** G-01 (spec-adherence auditing), G-02 (specification engineering).
- **Ideas:** I-07 (spec-adherence auditing — what to do with the registries), I-08 (deliberative alignment — how the spec becomes behavioral), I-23 (model welfare — moral-status bridge).
- **Programs:** RP-01 SPECGRADE (clause registries, cross-spec comparison, diff-auditor).
- **Field-map front:** A (specification); watch-trigger: either lab publishes a spec-authoring methodology.

## OPUS-EXPAND checklist           (LIVING)
- [ ] Manually ingest the OpenAI Model Spec (2025-12-18) and Claude's Constitution (2026-01-22) per `../04-missing-literature.md`; file notes under `papers/`.
- [ ] Extract atomic normative clauses from both specs with priority-tier metadata (RP-01 O1) — reuse the WCF-Bench anchor-registry pipeline.
- [ ] Identify ≥5 scenarios where the rule-based vs. reason-based structures give divergent guidance (RP-01 cross-spec study seed).
- [ ] Set up the spec-version diff-audit scaffold (roadmap T3) so future revisions are graded, not re-read.
- [ ] Capture the Constitution's moral-status clause verbatim and cross-reference to CEI religious-ethics moral-patiency assets (I-23 bridge).

## Sources                         (evidence classes marked)
- OpenAI Model Spec (versioned, 2025-12-18) — model-spec.openai.com — **SEARCH-CONFIRMED** (non-arXiv, manual ingest).
- Claude's Constitution (2026-01-22) — anthropic.com/constitution — **SEARCH-CONFIRMED** (non-arXiv, manual ingest).
- Corpus status (absent; living web documents) — **VERIFIED** (`../02-gap-atlas.md` G-01/G-02; `../04-missing-literature.md`).
