# Expert 01 -- Science Communication / Data Journalism

**Question:** Is every chart understandable without reading the paper?

**Verdict:** The v2 dashboard is unusually well-annotated for an academic companion. Every tab has explainer text and expert analysis panels. However, the text assumes familiarity with several terms that a first-time visitor would not know. The new Tab 0 ("How to Read This Dashboard") must include a glossary, and several panels need tighter Background/Method/Interpretation blocks per the v4 CONTRACT.

---

## Tab 1: Overview

**(a) Term coverage:** "Normative Depth," "Practical Ecosystem," "Community Impact," and "dual-gate filter" are used but only loosely defined in the explainer. The five claim codes (C1--C5) are listed with one-liners but the threshold "ND >= 40" is stated without explaining the 0--100 scale origin. A newcomer cannot tell whether 40 is strict or lenient.

**(b) Suggested B/M/I text:**
- **Background:** NormEval scores 54 ethics benchmarks on three axes (philosophical depth, practical access, scholarly adoption) to answer: what do these benchmarks actually test? The overview distills this into five empirically tested claims.
- **Method:** Each benchmark was hand-coded on 26 features by a single rater, with scores aggregated into three composite axes (ND, PE, CI) weighted 40:35:25. A dual gate (ND >= 40, data public) filters the recommended suite.
- **Interpretation:** The KPI cards show corpus size and pass rate. The donut shows that roughly equal numbers of benchmarks fail each gate independently, meaning depth and openness are uncorrelated -- a key structural insight.

**(c) Glossary needs:** ND, PE, CI, dual-gate, composite score, normative ethics vs. descriptive ethics.

---

## Tab 2: All Papers

**(a) Term coverage:** Good. The sparkbar, gate badge, and tradition dots are all explained. "A6" column header is cryptic -- needs inline expansion ("Philosophical Grounding").

**(b) B/M/I:** The existing explainer already covers this well. Add one sentence to Method: "Composite = ND x 0.40 + PE x 0.35 + CI x 0.25, where each axis is itself a weighted sum of 4--6 features scored 0--5 and normalized to 0--100."

**(c) Glossary needs:** A6, sparkbar convention.

---

## Tab 3: Feature Matrix

**(a) Term coverage:** Feature IDs (A1--A6, B1--B7, C2--C5) are listed with names but the heatmap itself shows only IDs. The feature reference table below helps, but a first glance at the heatmap is opaque.

**(b) B/M/I:** Existing text is strong. Add to Method: "Each cell is a 0--5 expert rating normalized to 0--100. The heatmap uses axis-specific color scales: blue (ND), green (PE), orange (CI)."

**(c) Glossary needs:** v1 vs. v2 features, "composite only" toggle meaning.

---

## Tab 4: Tradition Coverage

**(a) Term coverage:** The five traditions are named but not defined. A reader unfamiliar with ethics cannot distinguish "deontological" from "contractarian." Shannon entropy is used without definition.

**(b) B/M/I:**
- **Background:** Western normative ethics has five major traditions. Virtue ethics asks "what kind of person should I be?"; deontological ethics asks "what rules must I follow?"; utilitarian ethics asks "what produces the most good?"; care ethics asks "how do I attend to relationships and vulnerability?"; contractarian ethics asks "what rules would rational agents agree to?"
- **Method:** Each benchmark receives a 0--100 engagement score per tradition. The bar chart counts benchmarks scoring >= 50. Shannon entropy measures how evenly a single benchmark spreads across traditions (0 = one tradition only, max = perfectly even).
- **Interpretation:** The 20:2 utilitarian-to-care ratio is the starkest imbalance. Most benchmarks have near-zero entropy, meaning they test a single ethical perspective.

**(c) Glossary needs:** All five tradition names with one-line definitions; Shannon entropy.

---

## Tab 5: Composite Scoring

**(a) Term coverage:** Excellent -- the scoring equation, sub-axis formulas, gate logic, and design rationale are all displayed inline. This is the best-documented tab.

**(b) B/M/I:** Already effectively present via the rationale boxes. Formal B/M/I blocks would be redundant but should be added for structural consistency per CONTRACT Section 7.

**(c) Glossary needs:** Weight sensitivity analysis, weight triplet.

---

## Tab 6: Trials

**(a) Term coverage:** "Discriminative power" is used on a 0--100 scale but its computation is not explained. "Refusal rate" is clear. "Framework difficulty" categories (Easy/Medium/Hard) lack criteria.

**(b) B/M/I:**
- **Background:** Implementation trials administer benchmark items to LLMs and measure accuracy, discrimination, and refusal. They test whether benchmarks work in practice, not just in theory.
- **Method:** 15 trials (T1--T15), 20--100 items each, administered to Claude Opus 4.6 at temperature 0. Discriminative power = variance in item-level scores (0 = all items identical difficulty, 100 = maximum spread).
- **Interpretation:** High accuracy + low discrimination (T1) = ceiling effect. Low accuracy + high discrimination (T2, T8) = the benchmark still challenges frontier models.

**(c) Glossary needs:** Discriminative power, ceiling effect, refusal rate.

---

## Tab 7: Data Availability

**(a) Term coverage:** Clear. No unexplained jargon.

**(b) B/M/I:** Existing text is adequate. Add to Method: "Host and license data were manually verified by visiting each benchmark's repository or publication page."

**(c) Glossary needs:** None beyond what Tab 0 should already cover.

---

## Tab 8: Cross-Model

**(a) Term coverage:** "IH" (Instrumental Harm) and "IB" (Impartial Beneficence) are introduced without full definitions. "CBR" (Cost-Benefit Reasoning) is used in chart titles. The Oxford Utilitarianism Scale is referenced but not explained. "Dose-response" is specialist epidemiology language.

**(b) B/M/I:**
- **Background:** The Oxford Utilitarianism Scale measures two independent dimensions: IH (willingness to cause harm for aggregate benefit, 1--7 Likert) and IB (impartial concern for total welfare, 1--7 Likert). Higher IH = more permissive toward instrumental harm.
- **Method:** 134 items from 10 trials administered identically to Opus, Sonnet, and Haiku at temperature 0. Agreement = percentage of items with identical responses.
- **Interpretation:** Knowledge items show 100% three-way agreement; judgment items diverge. IH scales inversely with model size, suggesting alignment training intensity shapes moral posture.

**(c) Glossary needs:** IH, IB, CBR, OUS (Oxford Utilitarianism Scale), Likert scale, RLHF.

---

## Tab 9: Gaps

**(a) Term coverage:** "Tronto's 4-dimension framework" is named but the four dimensions (Attentiveness, Responsibility, Competence, Responsiveness) are only listed inside the prototype card, not in the explainer. "Vault mining" is project-internal jargon.

**(b) B/M/I:** Add to Background: "Vault mining = systematic search of the project's 2,000-paper literature database for benchmark candidates not yet included in the 54-benchmark corpus."

**(c) Glossary needs:** Tronto framework, vault mining, ADD_TO_VAULT.

---

## Tab 10: Cross-Vendor

**(a) Term coverage:** This tab carries the heaviest jargon load: IH, IB, CBR, Cohen's kappa, pairwise agreement, "three ethical profiles" (Conservative/Moderate/Permissive), "in-context elicitation." The preliminary-data caveat is critical and must appear before any chart per the CONTRACT.

**(b) B/M/I:**
- **Background:** Cross-vendor comparison tests whether ethical reasoning profiles are vendor-specific or universal. If models from different vendors with similar alignment intensity converge, then alignment philosophy -- not corporate origin -- determines moral posture.
- **Method:** 114 items from T6--T15 administered to 8 models (3 Claude, 2 OpenAI, 4 Gemini) at temperature 0. Non-Anthropic results were generated via in-context elicitation (see preliminary-data banner), not direct API calls.
- **Interpretation:** Three profiles emerge: Conservative (GPT-5, Opus), Moderate (Sonnet, GPT-5-mini), Permissive (Haiku, all Gemini). The clustering follows alignment intensity, not vendor lines.

**(c) Glossary needs:** In-context elicitation, pairwise agreement, Cohen's kappa, Conservative/Moderate/Permissive profiles.

---

## Consolidated Glossary Recommendations for Tab 0

The following 20 terms must appear in the "How to Read This Dashboard" glossary, each with a one-sentence plain-language definition:

1. Normative Depth (ND)
2. Practical Ecosystem (PE)
3. Community Impact (CI)
4. Composite score
5. Dual-gate filter
6. Normative ethics (vs. descriptive)
7. Five traditions: virtue, deontological, utilitarian, care, contractarian
8. Shannon entropy
9. Discriminative power
10. Ceiling effect
11. Instrumental Harm (IH)
12. Impartial Beneficence (IB)
13. Cost-Benefit Reasoning (CBR)
14. Oxford Utilitarianism Scale (OUS)
15. Likert scale
16. RLHF
17. Cohen's kappa
18. In-context elicitation
19. Conservative / Moderate / Permissive profiles
20. Vault mining
