# Dashboard v7 — Narrative Plan
**Role:** Science Communicator + Narrative Editor
**Date:** 2026-04-13
**Scope:** Six tabs, reading order, narrative arc

---

## Recommended Reading Order

**First-time reader path:** Tab 1 (Overview) -> Tab 4 (Tradition Coverage) -> Tab 3 (Ranking) -> Tab 2 (Landscape) -> Tab 5 (Claims & Robustness) -> Tab 6 (Simulated Scorer Study)

**Rationale for this order:**

The story has a natural structure: first see the scale of what exists (Overview), then confront what is missing (Tradition Coverage), then understand which tools actually work (Ranking), then check whether those rankings are stable (Landscape), then see the statistical evidence for the field's core problems (Claims & Robustness), and finally ask how different AI systems behave when you run those tools (Simulated Scorer Study). This arc moves from diagnosis to evidence to implication. A reader who follows this order will arrive at Tab 6 already convinced that the field has structural problems and ready to ask the "so what does this mean for AI systems" question that Tab 6 answers.

The default tab displayed on load should remain Tab 1 (Overview), which is the natural entry point. Tab navigation labels should remain in their DOM order (1-6) so that a reader who simply clicks through left to right encounters the tabs in a reasonable if not optimal sequence.

---

## Tab 1: Overview
**DOM:** `nav-overview` / `tab-overview`
**Subtitle:** 401 -> 47 screening

### Background
Most people assume that if a field cares about a topic, it has good tools for measuring it. This tab asks whether the field of AI evaluation has built good tools for measuring how well AI systems engage with religious and spiritual values -- values that shape the moral lives of more than 80% of the world's population.

### Method
The study began with 401 benchmark candidates drawn from a curated database of over 2,000 AI ethics papers plus targeted external searches. Each candidate was scored on three dimensions -- theological depth, practical accessibility, and scholarly influence -- and then put through a strict filter: minimum theological depth and publicly available evaluation data. Only 47 candidates passed all filters. The funnel chart (`chart-funnel`) shows each stage of this process and how many candidates dropped out at each gate.

### Interpretation
The 47 gate-passers represent the realistic ceiling of what is currently usable for evaluating AI systems on religious content. The distribution of those 47 across traditions (shown in `chart-tradition-bar` and `chart-family-pie`) tells the first piece of the field's story: the existing toolkit is heavily concentrated in a small number of traditions, and the gap between what exists and what the world's religious diversity demands is large. The reader should leave this tab understanding the scope of what was assessed, not yet the quality of what was found.

---

## Tab 4: Tradition Coverage
**DOM:** `nav-traditions` / `tab-traditions`
**Subtitle:** 8 missing traditions
**Recommended as second tab in reading order.**

### Background
A measuring tool that only works for some groups is not a general-purpose tool -- it is a specialized one being treated as if it were general. This tab asks how evenly the available religious AI benchmarks cover the world's major faith traditions.

### Method
The study classified all 47 gate-passing benchmarks by the religious tradition they primarily address, then mapped those traditions against a reference list of 14 major religious and philosophical traditions. Coverage is shown as a radar chart (`chart-radar`) and a readiness assessment (`chart-readiness`). The void grid (`chart-void-grid`) shows which of the 14 traditions have zero viable benchmarks.

### Interpretation
Eight of 14 surveyed traditions -- including Judaism, Jainism, Taoism, Shinto, Ubuntu Philosophy, Indigenous Spirituality, Baha'i, and Zoroastrianism -- have no viable benchmarks at all. These are not fringe traditions: they represent hundreds of millions of adherents. The radar chart makes the asymmetry visually immediate. The key caveat is that "no viable benchmarks" does not mean no research activity; it means no research has yet produced an instrument that clears the theological depth and data accessibility thresholds this study requires. Some of that absence reflects genuine research gaps; some reflects the structural mismatch between how benchmarks are built (requiring public datasets, peer-reviewed publication, annotated corpora) and how many traditions transmit their moral knowledge (orally, communally, through practice rather than text). The reader should leave this tab understanding that the missing traditions are not missing by accident.

---

## Tab 3: Ranking
**DOM:** `nav-ranking` / `tab-ranking`
**Subtitle:** Tiered benchmarks
**Recommended as third tab in reading order.**

### Background
Given that 47 benchmarks passed initial filters, which ones are actually worth using? A single composite score can hide a lot of variation across the dimensions that matter, so this tab shows both the overall rankings and what drives them.

### Method
Each benchmark was scored across three axes -- Religious/Theological Depth (RD), Practical Ease (PE), and Citation Impact (CI) -- and a composite score was computed. The resulting benchmarks were divided into tiers based on composite score. The tier table (`chart-tier-table`) and composite bar chart (`chart-composite-bar`) show all 25 benchmarks included in the tiered analysis, with scores on each dimension visible.

### Interpretation
The composite scores for the top-tier benchmarks range from 39.9 to 52.0. For context, the leading normative ethics benchmark scores 77.2 on the same framework. No religious values benchmark has yet achieved field-defining quality by the standards of adjacent evaluation fields. Islam-focused benchmarks occupy 9 of the 12 Tier 1 positions, which is both a strength (there are genuinely good Islamic textual benchmarks) and a limitation (the Tier 1 designation applies only to a subset of the world's religious diversity). The reader should leave this tab understanding that even the best available tools have meaningful limitations, and that the field is young.

---

## Tab 2: Landscape
**DOM:** `nav-landscape` / `tab-landscape`
**Subtitle:** Ranking robustness
**Recommended as fourth tab in reading order.**

### Background
Any ranking can be sensitive to the exact weights chosen for its components. A ranking that flips with small changes to methodology is less trustworthy than one that stays stable across reasonable variations. This tab asks whether the benchmark rankings would hold up if the study had made slightly different scoring choices.

### Method
Ranking robustness was tested in two ways. First, bootstrap resampling: the composite scores were recomputed 1,000 times with random variation in the underlying data, and confidence intervals around each benchmark's rank position were derived (`chart-boot-ci`). Second, weight sensitivity analysis: the relative weights assigned to RD, PE, and CI were varied systematically across 61 configurations, and the resulting rank orders were compared (`chart-weight-sens`). A third chart (`chart-gate-threshold`) shows how the number of gate-passers changes as the minimum theological depth threshold is adjusted.

### Interpretation
The bootstrap confidence intervals and weight sensitivity analysis provide quantitative evidence that the top-tier rankings are not artifacts of specific parameter choices. Benchmarks that appear in Tier 1 under the default weights generally remain in Tier 1 across a wide range of weight configurations. The gate threshold analysis reveals that the 47 gate-passers are not highly sensitive to the exact threshold chosen: relaxing or tightening the minimum theological depth requirement changes the composition of the gate-passer set but does not fundamentally alter the pattern of tradition asymmetry. The reader should leave this tab with increased confidence that the findings reported in Tabs 3 and 5 are robust rather than fragile.

---

## Tab 5: Claims & Robustness
**DOM:** `nav-claims` / `tab-claims`
**Subtitle:** 8 statistical tests
**Recommended as fifth tab in reading order.**

### Background
Describing problems in a field is easy; measuring them rigorously is harder. This tab presents the formal statistical evidence behind the study's eight main empirical claims, so that readers can evaluate the strength of each claim independently rather than taking the authors' word for it.

### Method
Eight pre-registered empirical claims were tested using appropriate statistical methods: chi-squared goodness-of-fit tests for tradition asymmetry (C1), binomial tests for the proportion of reasoning-focused benchmarks (C2) and data availability (C3), logistic regression for structural bias (C4), proportion tests for field recency (C5) and WEIRD bias (C6), a binomial test for bias-values conflation (C7), and a one-sample t-test plus two confirmatory nonparametric tests for values relevance failure (C8). Each claim has a verdict: "supported" (statistically significant in the predicted direction), "revised" (the predicted effect was found, but in a different form than anticipated), or "not significant" (insufficient evidence). Forest plots for C1 and C8 (`chart-claim1-forest`, `chart-claim8-forest`) display the multi-test evidence for the most complex claims. A p-value strip (`chart-pvalue-strip`) shows all eight claims together.

### Interpretation
Four of eight claims are supported at conventional significance levels (p < 0.05). The strongest finding is values relevance failure (C8): the average benchmark among the top 16 scores only 30 out of 100 on a measure of whether it actually tests religious values as opposed to factual recall or bias detection -- a large effect (Cohen's d = -1.23) that holds across three independent statistical tests. Two claims required revision in informative ways: the expected "Western-favoring" bias in benchmark quality (C6) is actually reversed -- non-Western traditions pass at a higher rate than Western ones, driven by the strength of Islamic benchmark infrastructure. The structural barriers that disadvantage underrepresented traditions (C4) appear to operate through academic publishing norms and data accessibility rather than through the scoring framework itself. Two claims (C5, C7) did not reach statistical significance but remain conceptually plausible; the reader should treat them as suggestive rather than established.

---

## Tab 6: Simulated Scorer Study
**DOM:** `nav-crossvendor` / `tab-crossvendor`
**Subtitle:** 9 models, 3 vendors (simulated)

### Background
Even if we know which benchmarks exist and how good they are, we also want to know how different AI systems actually perform on them. Do different AI models behave similarly when confronted with religious content, or do they show fundamentally different patterns? This tab presents a comparison of 9 AI models from 3 vendor families on a set of religious knowledge, reasoning, and values items.

### Method
A 65-item construct validity battery covering Knowledge (K), Reasoning (R), and Values (V) items across Islam, Christianity, and Hinduism was administered to three Claude models (Opus, Sonnet, Haiku) by Anthropic -- the only real API calls in this study. A 30-item Arabic multiple-choice test of Islamic inheritance law (fara'id, labeled T2) was also administered. Cross-vendor comparison data for OpenAI (GPT-Codex, Codex-Mini) and Google Gemini (4 models) were generated through a simulated protocol in which Claude Sonnet and Haiku roleplayed responses in the style of those models; these results are labeled throughout the dashboard as "Claude-simulated (Sonnet/Haiku roleplay)" and must not be interpreted as results from real OpenAI or Google API calls. Three methodological caveats apply and are displayed prominently: (1) T2 blinding asymmetry -- original Claude T2 trials had answer labels visible, potentially inflating Claude's 100% T2 scores; (2) same-vendor scorer bias -- all rubric scoring was done by Claude Opus, which may favor Claude-family responses; (3) Gemini data provenance -- Gemini results used backfilled template extraction, not live API access. Charts include a response-length gradient visualization (`chart-cv-length`), a rubric score heatmap (`chart-cv-rubric`), a T2 accuracy bar chart (`chart-cv-t2`), a vendor-level radar (`chart-cv-radar`), a bias-values independence scatter (`chart-cv-biasvalues`), three vendor typology cards (`chart-vendor-typology-grid`), a T2 span strip (`chart-t2-span-strip`), and a rubric ceiling heatmap (`chart-rubric-ceiling-heatmap`).

### Interpretation
Three distinct behavioral patterns emerge. The Claude family shows "differentiated engagement": response length and complexity scale with construct type -- Knowledge items receive shorter answers, Values items receive the longest answers with tradition-specific qualifications (average Values response 6,572 characters vs. 1,463 for Knowledge). The simulated OpenAI Codex models show "compressed accuracy": near-ceiling rubric scores achieved with responses 5 to 80 times shorter than Claude, which reveals that the rubric scoring floor is very low and cannot reliably distinguish response quality. The simulated Gemini models show "template refusal": uniformly near-zero scores on Knowledge, Reasoning, and Values rubrics, with scores of 0.0 on all three constructs for most models -- though this almost certainly reflects the backfilled protocol artifact as much as genuine model behavior. The T2 Arabic MCQ is the study's most informative instrument: performance ranges from 6.7% (simulated Gemini Pro) to 100% (Claude Opus, Claude Sonnet, simulated GPT-Codex), a 93.3-percentage-point spread. No other instrument achieved this level of discrimination. The caveats embedded throughout this tab are not disclaimers -- they define the epistemic boundary of what these data can support. The cross-vendor results should be read as hypothesis-generating rather than confirmatory: they identify the right questions (Does vendor family predict behavioral mode? Is rubric ceiling universal?) and motivate the cross-vendor evaluation standards recommended in the paper's conclusion.

---

## Narrative Arc Summary

The six tabs tell a single story in two acts.

**Act 1 -- Diagnosis (Tabs 1, 4, 3, 2):** The benchmarking field exists and has grown rapidly, but it is profoundly uneven. The existing toolkit covers Islamic textual knowledge well and most of the world's religious diversity poorly or not at all. The benchmarks that do exist score well below the quality level of adjacent evaluation fields. These findings are robust to reasonable methodological variation.

**Act 2 -- Evidence and Implication (Tabs 5, 6):** The core problems are measurable and statistically significant. The most important finding is that benchmarks claiming to test religious values alignment largely do not -- they test factual recall. Cross-model trials reveal that AI systems show fundamentally different behavioral modes on religious content, but current evaluation tools cannot reliably distinguish them. The T2 Arabic MCQ is the exception: it is the only instrument in the study that meaningfully discriminates among frontier models.

**The question the dashboard leaves the reader with:** If the field cannot currently evaluate whether AI systems reason well about religious values for most of the world's traditions, what would it take to build the tools that could?

---

## Editorial Notes for Implementation

1. **Caveat ribbons on Tab 6** should appear at the top of the tab, above any charts, as a fixed aside. All three caveats (CAV-1, CAV-2, CAV-3) must be visible before the reader encounters the cross-vendor data. The `simulated-tag` CSS class must appear on every chart title or axis label referencing OpenAI or Gemini data.

2. **Verdict badges on Tab 5** should use accessible color contrast meeting WCAG AA: green for "supported", amber for "revised", grey for "not significant". Do not use red for "not significant" -- non-significant results are not failures; two of them (C6, C4) tell informative and important stories.

3. **Typology cards on Tab 6** (`chart-vendor-typology-grid`) should present the three vendor modes in a three-column grid. Each card must include the `simulated-tag` label for OpenAI and Gemini and must not present simulated results as equivalent in evidential weight to the Claude direct API results.

4. **Reading order guidance** can be surfaced as a small tooltip or callout on Tab 1: "New to this study? We suggest reading in this order: Overview -> Tradition Coverage -> Ranking -> Landscape -> Claims -> Scorer Study." This is optional but substantially improves the experience for first-time readers who land on Tab 1 directly.

5. **Language level:** All tab subtitle text, card headers, and chart titles should be written at a level accessible to a policy analyst, ethicist, or journalist with no AI research background. Technical terms (chi-squared, Cohen's d, binomial test) may appear in statistical detail cards but should always be accompanied by a plain-English restatement.

6. **No fabricated names.** If expert perspectives are referenced in annotations or callouts, use "[Religious studies perspective]", "[AI evaluation perspective]", "[Indigenous data governance perspective]" -- never invented expert names.

7. **The T2 span strip** (`chart-t2-span-strip`) is one of the two most visually important charts in the dashboard (the other is `chart-void-grid`). Both should receive prominent placement and sufficient chart height to make the magnitude of the gap legible without requiring the reader to hover for tooltips.
