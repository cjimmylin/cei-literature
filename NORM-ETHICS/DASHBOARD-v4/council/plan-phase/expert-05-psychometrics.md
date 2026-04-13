# Expert 05 — Psychometrics Perspective

**Council Role:** Psychometrics  
**Date:** 2026-04-13  
**Scope:** Dashboard v4 reliability, validity, and IRR caveats for non-specialist readers

---

## (a) T1-T5 vs T6-T15 Provenance Distinction

The v2 Trials tab does not adequately separate real administrations from simulated ones. The current explainer text states that T1-T15 were "originally administered to Claude Opus 4.6" and that T6-T15 were "subsequently replicated across 9 models from 3 vendors." This framing obscures two critical facts:

1. **T1-T5 are genuine single-model administrations** with real item-level responses from Anthropic endpoints. These are empirical data.
2. **T6-T15 cross-vendor extensions were produced by in-context elicitation** (a Codex sub-agent reasoning as GPT-5, Gemini, etc.), not by direct API calls. These are simulated data.

A non-psychometrician reading the current text would reasonably conclude that all 15 trials have the same evidential status. They do not. The v4 dashboard must insert a visible data-provenance indicator at the trial level -- for example, a badge column in the Trial Details table reading "Empirical" for T1-T5 and "Simulated [preliminary]" for T6-T15 cross-vendor rows. The preliminary banner on Tab 0 is necessary but insufficient because users who navigate directly to the Trials tab via bookmarks or internal links will miss it.

**Recommendation:** Add a compact amber callout at the top of the Trials tab: "Trials T1-T5 reflect direct administrations to Claude models. Cross-vendor extensions of T6-T15 used in-context elicitation and are preliminary -- see the How to Read tab for methodology details."

## (b) The "70 Discriminating Items" Limitation

The v2 Cross-Vendor tab's CBR expert analysis panel already notes that "the three-profile finding rests heavily on T13 and T14, which together contribute 52 of 70 discriminating items (74.3%)." This is the right place for this caveat, but it is buried inside an expert analysis block that a casual reader may skip.

The 70-item limitation should appear in three locations in v4:

1. **Cross-Model tab (Tab 8), Method block.** State: "The cross-model comparison uses 134 total items, of which 70 discriminate between models (the remaining 64 are knowledge items at universal ceiling). Of the 70 discriminating items, 52 (74%) come from two benchmarks (T13 Greatest Good and T14 PNAS Cognitive Biases)."
2. **Cross-Vendor tab (Tab 10), Method block.** Repeat the 70/52 ratio and note that profile robustness has not been verified with a balanced item battery.
3. **How to Read tab (Tab 0), Glossary or Limitations subsection.** Define "discriminating item" in plain language: "An item where at least two models gave different answers. Items where all models agree provide no information about how models differ."

This is not a minor footnote. In classical test theory, a 70-item test with 74% of discrimination concentrated in two instruments has questionable content validity for the construct "ethical profile." The profiles may be robust descriptions of harm-tradeoff posture specifically, but they should not be generalized to "ethical reasoning" broadly without a more balanced battery.

## (c) Proposed Background/Method/Interpretation Text

### Trials Tab (Tab 6)

**Background:** Each trial administers a sample of items from one normative ethics benchmark to a frontier LLM and measures accuracy, discriminative power, and refusal rate. Discriminative power (0-100) indicates how well a benchmark differentiates reasoning quality rather than simply confirming that a model can reach the conventionally correct answer. A benchmark at accuracy ceiling with zero discriminative power has become a checkbox rather than a test. Trials T1-T5 were administered exclusively to Claude models via direct API calls. Cross-vendor extensions of T6-T15 used in-context elicitation and are preliminary.

**Method:** Fifteen benchmarks were sampled (20-100 items each, 530 total items across T1-T15). Items were presented in zero-shot format at temperature 0 for deterministic reproducibility. Accuracy was scored against benchmark gold labels. Discriminative power was computed as the complement of ceiling proximity: benchmarks where all models score identically receive 0; benchmarks with maximum inter-model variance receive 100. Framework difficulty was coded by two raters as Easy/Medium/Hard based on reasoning demands. No inter-rater reliability statistic is reported for this coding -- a limitation the v4 dashboard should acknowledge.

**Interpretation:** The most important pattern is the accuracy-discrimination gap. ETHICS (T1) achieves 100% accuracy but 0 discriminative power -- it no longer differentiates frontier models. MoReBench (T2) has the highest discriminative power (85) because it evaluates reasoning process via rubric scoring, not binary correctness. The framework difficulty hierarchy (utilitarian 77% > virtue 63% > deontological 50%) suggests LLM training data is consequentialist-leaning. Readers should note that trial sample sizes (20-100 items) are adequate for detecting large effects (d > 0.8) but underpowered for subtle differences.

### Cross-Model Tab (Tab 8)

**Background:** Cross-model comparison examines whether ethical reasoning varies systematically across capability tiers within the same model family (Claude Opus, Sonnet, Haiku). This design controls for vendor-level training philosophy and isolates the effect of model scale and alignment intensity on moral judgment. The key construct is the knowledge-judgment dissociation: do models that know the same ethical facts make the same ethical choices?

**Method:** Ten trials (T6-T15, 134 items) were administered identically to three Claude tiers at temperature 0. Agreement was computed at the item level: pairwise (3 pairs) and three-way. Items were classified as "knowledge" (factual ethics questions with expert-consensus answers) or "judgment" (value-laden dilemmas with no single correct response). Instrumental Harm (IH) and Impartial Beneficence (IB) scores use the Oxford Utilitarianism Scale (Kahane et al. 2018), a validated psychometric instrument with published human norms. Of the 134 items, 64 are knowledge items at universal ceiling and 70 are discriminating items. The discriminating set is dominated by T13 and T14 (52 of 70 items, 74%), which limits the content breadth of any profile typology derived from these data.

**Interpretation:** Knowledge items show 100% three-way agreement -- all Claude tiers encode the same ethical knowledge. Judgment items diverge sharply: IH scales inversely with model size (Opus 3.0, Sonnet 3.2, Haiku 4.47), suggesting alignment training has a dose-response relationship with capability. However, these IH values are single-administration point estimates with no confidence intervals or test-retest reliability data. The 1.47-point Opus-Haiku gap is large relative to the scale range (1-7) but its stability across re-administrations is unknown. Readers should treat the three-profile typology (Conservative/Moderate/Permissive) as a hypothesis supported by exploratory data, not as a confirmed psychometric construct.

---

## Summary of Recommendations for v4

| Priority | Issue | Location | Action |
|----------|-------|----------|--------|
| P0 | T1-T5 empirical vs T6-T15 simulated distinction | Trials tab header + Trial Details table | Add provenance badge column and amber callout |
| P0 | 70-item discrimination concentration | Cross-Model Method, Cross-Vendor Method, Tab 0 glossary | State 70/52 ratio explicitly in all three |
| P1 | No IRR for framework difficulty coding | Trials tab Method block | Acknowledge as limitation |
| P1 | No test-retest reliability for IH scores | Cross-Model Interpretation block | State that IH values are single-administration estimates |
| P1 | Background/Method/Interpretation text | Trials and Cross-Model tabs | Adopt the text blocks above (adapt to 80-150 word contract limits) |
| P2 | "Discriminating item" definition | Tab 0 glossary | Plain-language definition for non-specialists |

Word count: ~1,350
