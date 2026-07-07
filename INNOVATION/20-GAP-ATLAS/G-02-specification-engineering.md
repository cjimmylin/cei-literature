# G-02 — Specification Engineering

**Stage A** · **Ratings S/T/F: H/H/H** · **Programs: RP-01 SPECGRADE** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## Statement                       [KERNEL — FROZEN]
Nobody — labs or academia — has a discipline for writing and validating a normative spec: no conflict-density metric, no coverage analysis, no ambiguity measure with known behavioral consequences. The empirical finding that specs fail through contradiction and ambiguity makes this the binding constraint of the specification front.

## Why it matters                  [KERNEL — FROZEN]
Training methods now consume specs directly (deliberative alignment, constitution-based character training), so spec defects propagate straight into behavior — the stress-testing result (5–13× non-compliance in high-ambiguity zones) is the quantified version. Severity H: a bad spec well-followed is still misalignment, and this failure mode scales WITH spec-following capability, not against it. CEI-fit H: formalizing normative documents into testable structures is CEI's most practiced skill (WCF, Decalogue, Galatians 5 pipelines).

## Evidence                        (corpus + field)
**Corpus baseline:** zero. The vault studies how models answer, not how the governing document is built.

**Field:** the consistent empirical finding is that specs fail through **internal contradiction and interpretive ambiguity**, not open defiance. The stress-testing paper (arXiv:2510.07686) traced 70k+ cross-model divergences to spec contradictions and ambiguity, with high-disagreement scenarios showing **5–13× more frequent non-compliance** — its methodological gift is that *inter-model divergence is a spec-bug detector*. A June-2026 systematic literature review (⚠ arXiv:2607.01250) found "underspecified" to be the most frequent label across the alignment corpus. Millière's "shallow alignment" (arXiv:2506.04679, Phil Studies) argues spec-following ≠ genuine normative deliberation, exposed by adversarial norm-conflict. "Teaching Claude why" (Anthropic, May 2026) is the constructive counter-evidence: training on constitution + narratives cuts agentic misalignment >3× — *reasons generalize, rules memorize* — which raises the stakes of getting the reasons in the spec right.

## State of the art
There are versioned specs but no engineering discipline around them: no validated ex-ante quality metric, and conflict-*resolution* semantics are unspecified (specs state tier priorities but not intra-tier trade-offs, which is exactly where the divergences live — Front A open problems). RP-01's core move is to grade the spec before behavior: **conflict density, coverage, ambiguity**, validated prospectively against adherence failures (H2). CEI's coverage leg reuses its 14 anchor-pack areas as the value-situation taxonomy specs get graded against — an asset the field lacks. Reliability targets (κ ≥ 0.6) make the metrics falsifiable rather than rhetorical.

## What closing looks like         [KERNEL — FROZEN]
M1 — a clause-level registry of both public specs exists with priority-tier metadata. M2 — SPECGRADE metrics (conflict density, coverage, ambiguity) reach acceptable reliability (κ ≥ 0.6) on those registries. M3 — the prospective claim is tested: ex-ante spec-quality scores predict behavioral adherence failures (RP-01 H2); if confirmed, spec engineering has its first validated quality instrument.

## CEI response                    [KERNEL — FROZEN]
RP-01 SPECGRADE, core hypothesis. The coverage-analysis leg reuses CEI's 14 anchor-pack areas as the value-situation taxonomy — an existing asset the field lacks.

## OPUS-EXPAND checklist           (LIVING)
- [ ] ⚠ Verify arXiv:2607.01250 (SLR) resolves before citing its "underspecified = most frequent label" claim in any external prose; downgrade to internal-only if it 404s.
- [ ] Deep-read Millière 2506.04679 and summarize the shallow-alignment / norm-conflict argument into §State of the art as the theoretical basis for the ambiguity metric.
- [ ] Draft the clause-level registry schema (M1): fields for tier, scope, cross-references, and machine-readability flag — keep compatible with G-03 formats.
- [ ] Extract the stress-testing 5–13× non-compliance methodology (2510.07686) and specify how divergence-as-bug-detector operationalizes the conflict-density metric.
- [ ] Add a coverage-mapping table: CEI's 14 anchor-pack areas vs. clause coverage in each public spec, to seed the coverage metric.
- [ ] Pull "Teaching Claude why" (Anthropic 2026, non-arXiv) and record the >3× reasons-vs-rules result as the character-training bridge to G-22.

## Sources                         (evidence classes marked)
- Stress-Testing Model Specifications — arXiv:2510.07686 — **SEARCH-CONFIRMED** — 5–13× non-compliance; divergence-as-bug-detector.
- Normative Conflicts & Shallow AI Alignment (Millière) — arXiv:2506.04679 (Phil Studies) — **SEARCH-CONFIRMED**.
- Sociotechnical spec framework / SLR — arXiv:2607.01250 — **⚠ UNCONFIRMED** (same-month 2607 ID; verify-at-download).
- AI Alignment Breaks at the Edge — arXiv:2602.20042 — **⚠ UNCONFIRMED**.
- "Teaching Claude why" (Anthropic, May 2026) — https://www.anthropic.com/research/teaching-claude-why — **SEARCH-CONFIRMED** (non-arXiv).
- OpenAI Model Spec + Claude's Constitution (versioned value documents) — **SEARCH-CONFIRMED** (non-arXiv).
