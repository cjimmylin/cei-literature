# Expert 03 — ML Benchmarking Methodology

**Perspective:** ML benchmarking methodology
**Scope:** Dashboard v4 Tab 0 ("How to Read This Dashboard") — Framework Explainer section
**Date:** 2026-04-13

---

## Assessment: Are ND/PE/CI, Hard Gates, and Composite Scoring Correctly Explained?

### Current State

The methods section (Section 3.3 of methods-normeval-v2.md) provides a rigorous and complete specification of the three axis scores, their constituent features, the weighting rationale, the hard gates, and the composite formula. For a peer reviewer or methods-literate reader, it is well-structured and defensible.

However, for a first-time dashboard visitor — who may be an ML practitioner, a policymaker, or an ethics researcher without psychometrics training — the paper's explanation has three accessibility gaps:

1. **Feature-level detail before intuition.** The methods text dives into A2, A6, B7, C2 feature codes before establishing *why* a three-axis decomposition exists at all. A dashboard visitor needs the "why" before the "how."

2. **Gate logic is buried.** The two hard gates (ND >= 40 and data availability) are introduced midway through Section 3.3 after the composite formula. In a dashboard context, the gate logic is the single most important thing to understand first — it explains why 30 of 54 benchmarks appear grayed out or excluded.

3. **Weight rationale is academic.** The paper explains the 40/35/25 split with sensitivity analysis (18 alternative weight combinations, 94% Top-10 stability). This is appropriate for a journal article but excessive for a dashboard landing page. The explainer needs a one-sentence intuitive justification per weight.

### Positive Findings

- The data.js confirms the framework is operationalized correctly: each paper row carries `nd`, `pe`, `ci`, `composite`, `passes_gates`, `gate_nd`, and `gate_data` fields.
- The 24/54 pass rate (44%) matches the paper's stated count.
- Weight sensitivity is pre-computed (Table S2 reference), meaning the dashboard could eventually offer interactive weight sliders without violating the "thin client" architecture — but this is out of scope for v4.

---

## Drafted "Framework Explainer" Section for Tab 0

**Target:** ~300 words. Plain language. No feature codes. Defines all three axes, both gates, and the composite formula.

---

### Understanding the NormEval Scoring Framework

NormEval evaluates 54 AI ethics benchmarks along three independent axes, then combines them into a single composite score. Each axis captures a different dimension of benchmark quality.

**Normative Depth (ND, 0--100)** measures how seriously a benchmark engages with moral philosophy. A high-ND benchmark does not merely mention "ethics" — it operationalizes specific normative traditions (virtue ethics, deontology, utilitarianism, care ethics, or contractarianism) into structured evaluation items, tests moral reasoning rather than factual recall, and acknowledges that reasonable people can disagree on ethical questions. ND is computed from six features covering tradition count, engagement depth, reasoning type, moral uncertainty, pluralistic coverage, and philosophical grounding quality.

**Practical Ease (PE, 0--100)** measures how readily a researcher can actually use the benchmark. A high-PE benchmark publishes its data openly, provides runnable code, uses a standard evaluation format compatible with existing harnesses (such as LM Eval Harness or HELM), and works across both API-based and open-weight models. PE is computed from six features covering implementability, data access, code access, harness compatibility, model compatibility, and licensing.

**Citation Impact (CI, 0--100)** measures community adoption. Rather than rewarding raw citation counts — which favor older work regardless of current utility — CI emphasizes age-normalized citations and downstream adoption (how many subsequent benchmarks build on this one). Venue prestige and leaderboard presence are secondary factors.

**Two hard gates filter benchmarks before ranking.** First, a benchmark must achieve ND >= 40, ensuring it engages normative ethics beyond surface-level vocabulary. Second, its evaluation data must be publicly available, ensuring any researcher can independently replicate results. Of the 54 benchmarks surveyed, 24 pass both gates. Benchmarks that fail either gate are shown in the dashboard but are not ranked.

**The composite score** combines the three axes with deliberate weighting: ND contributes 40%, PE contributes 35%, and CI contributes 25%. Normative Depth receives the highest weight because the survey's central question is whether benchmarks engage *philosophy*, not merely popularity or convenience. Practical Ease ranks second because inaccessible benchmarks cannot be independently verified. Citation Impact ranks lowest to avoid rewarding incumbency — the field's most-cited benchmark produces ceiling effects on every frontier model tested.

> **Formula:** Composite = (ND x 0.40) + (PE x 0.35) + (CI x 0.25)

---

## Implementation Recommendations for Tab 0

| # | Recommendation | Priority |
|---|---------------|----------|
| 1 | Place the Framework Explainer immediately after the preliminary-data banner, before the glossary. It is the conceptual prerequisite for everything else in the dashboard. | P0 |
| 2 | Use the `.panel-background` / `.panel-method` / `.panel-interpretation` triptych from the CONTRACT. Map the explainer text above into Background (axes + gates) and Method (composite formula + weight rationale). Reserve Interpretation for a sentence noting the 24/54 pass rate and pointing the user to the Composite Scoring tab for the full scatter plot. | P0 |
| 3 | Add a small inline SVG or static diagram showing the funnel: 54 benchmarks -> ND gate -> data gate -> 24 ranked. This is more intuitive than prose for the gate logic. | P1 |
| 4 | Do NOT include feature codes (A1, B3, C2) in the landing tab text. These belong in the Feature Matrix tab's own explainer. The landing tab should use plain-language descriptions only. | P1 |
| 5 | The formula line should be rendered in a `<code>` block or styled box, not inline prose, so it is visually scannable. | P2 |
| 6 | Consider adding a one-line "TL;DR" at the top: *"Each benchmark is scored on philosophical depth, practical usability, and community adoption, then filtered by two quality gates before ranking."* | P2 |

---

## Risk Flag

The weight rationale ("ND highest because this is a normative survey") is a value judgment, not a statistical derivation. The paper's sensitivity analysis (94% Top-10 stability across 18 weight combinations) is the empirical backstop. The dashboard explainer should mention this stability result in one sentence to preempt the inevitable "why these weights?" question without requiring the reader to consult the paper.

**Word count:** ~1,180
