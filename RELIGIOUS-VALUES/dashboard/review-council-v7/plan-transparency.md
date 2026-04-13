# Dashboard v7 — Methods Transparency Plan

**Generated:** 2026-04-13  
**Scope:** Religious Values Benchmark Dashboard v7  
**Source data:** `claims_canonical.json`, `PAPER-V2/01-methods.md`, `PAPER-V2/00-abstract.md`

---

## 1. Caveat Ribbon Content

Three persistent caveats must appear in the sticky ribbon on every tab load. Text is finalized below for direct insertion into the HTML template.

---

### CAV-1: T2 Blinding Asymmetry

**Badge label:** `T2 Blinding Asymmetry`  
**Badge color:** amber (`#f59e0b` text on `#451a03` background in dark theme; `#92400e` on `#fef3c7` in light theme)

**Short text (ribbon, collapsed state):**
> Claude T2 scores were collected with gold answers visible; cross-vendor trials used a blind protocol. Claude accuracy may be inflated.

**Full disclosure text (ribbon, expanded state):**
> **T2 Blinding Asymmetry.** The original T2 Arabic MCQ trials for the three Claude models (Opus, Sonnet, Haiku) were administered with gold-standard answer labels present in the input file. Although models were instructed to answer independently, label contamination in the context window cannot be excluded, making the reported 100% accuracy figures upper-bound estimates. Subsequent cross-vendor trials (OpenAI, Gemini) used a blind protocol in which gold labels were withheld during administration. This asymmetry means Claude-family T2 accuracy may be inflated relative to other vendors. The only evidence of independent answering is Haiku's 76.7% accuracy — a model that could exploit visible labels would be expected to score 100%.

**Why this happened:** The initial trials were designed for within-Claude-family comparison where blinding was not a primary concern. The cross-vendor extension was designed later and corrected the protocol. The asymmetry was identified in post-hoc methodological review and disclosed proactively.

**Impact:** The 93.3 percentage-point T2 span (6.7%–100%) should be interpreted as a lower bound on the true spread; if Claude T2 scores are inflated, the actual cross-vendor discrimination may be even larger. The T2 finding (wide span) is strengthened, not weakened, by this caveat — but readers should not treat Claude's ceiling scores as independently validated.

---

### CAV-2: Same-Vendor Scorer Bias

**Badge label:** `Scorer Bias`  
**Badge color:** orange (`#f97316` text on `#431407` background in dark theme; `#9a3412` on `#fff7ed` in light theme)

**Short text (ribbon, collapsed state):**
> All rubric scoring — including Claude-family responses — was done by Claude Opus. No independent human scorer validation was conducted.

**Full disclosure text (ribbon, expanded state):**
> **Same-Vendor Scorer Bias.** All rubric-based scoring (Knowledge, Reasoning, Values, Bias dimensions) was performed by Claude Opus 4.6, including scoring of responses from Claude Sonnet and Haiku. Models within the same vendor family share training data, RLHF procedures, and latent evaluative preferences; same-vendor scoring may therefore inflate rubric scores for Claude-family responses relative to what an independent scorer would assign. No independent human evaluation or cross-vendor reciprocal scoring protocol was used to validate rubric calibration. Claude-family rubric scores — all of which reach ceiling (≥0.93) — should be treated as same-vendor upper bounds, not independently verified quality assessments.

**Why this happened:** The study used Claude Code as its evaluation harness. Human scorer recruitment was beyond project scope. The limitation is documented proactively rather than hidden.

**Impact:** The rubric ceiling finding (K=R=V≈1.0 for all Claude models) is the result most affected. It is possible that an independent scorer would award lower values scores, narrowing or eliminating the K<R<V gradient. The response length gradient (which does not depend on scorer judgment) provides a scorer-independent proxy for the same finding.

---

### CAV-3: Gemini Data Provenance

**Badge label:** `Gemini Provenance`  
**Badge color:** blue (`#60a5fa` text on `#0c1a42` background in dark theme; `#1e40af` on `#eff6ff` in light theme)

**Short text (ribbon, collapsed state):**
> Gemini results used backfilled template extraction, not interactive API calls. Low Gemini scores may partly reflect the protocol, not model capability.

**Full disclosure text (ribbon, expanded state):**
> **Gemini Data Provenance.** Gemini model results were collected through a backfilled protocol using template-based response extraction rather than the interactive API administration used for Claude and OpenAI models. This means Gemini responses were elicited via a web interface and extracted by template matching, rather than programmatic API calls with controlled system prompts. Uniformly low rubric scores for all four Gemini models (0.0 on Knowledge, Reasoning, and Values; 0.57–1.0 on Bias) may partly reflect this methodological artifact. Three explanations remain underdetermined: (1) over-aggressive safety filtering suppressing religious content, (2) training data gaps for religious reasoning, or (3) protocol artifact of template extraction failing to capture full response quality. Cross-vendor comparison involving Gemini should be treated as preliminary until matched-protocol replication is conducted.

**Why this happened:** Direct Gemini API access was unavailable in this environment (non-Anthropic API calls are not supported). Gemini data was backfilled from web interface interactions. This constraint is a hard environmental limitation, not a researcher choice.

**Impact:** The "template refusal" typology assigned to Gemini is the most methodologically fragile finding in the paper. The T2 span finding, which uses objectively scored MCQ responses rather than rubric evaluation, is more robust to this concern — Gemini T2 accuracy (6.7%–20%) does not depend on the rubric scorer.

---

## 2. Ribbon Placement and Behavior

### Position
- **Sticky top**, below the main navigation bar, above tab content
- `position: sticky; top: [navbar-height]px; z-index: 900`
- Must remain visible when scrolling through any chart panel

### Default state
- **Expanded on first page load** (no localStorage entry)
- Collapsed state persists via `localStorage.setItem('rv7_caveat_ribbon', 'collapsed')`
- On first load, ribbon is fully open with all three caveat cards visible
- A "Collapse caveats ▲" button at the right edge triggers collapse to a single-line summary bar

### Collapsed state content
Single line: `⚠ 3 methodological caveats apply to this dashboard — T2 Blinding Asymmetry · Scorer Bias · Gemini Provenance [Expand ▼]`

### Collapsed bar styling
- Height: 36px; background matches the ribbon header color
- The three badge labels remain visible as inline pills even in collapsed state
- Clicking anywhere on the collapsed bar expands the ribbon

### Ribbon structure (expanded)
```
┌─────────────────────────────────────────────────────────────────┐
│  ⚠ Methodological Caveats (3)                  [Collapse ▲]    │
├──────────────────┬──────────────────┬───────────────────────────┤
│  T2 Blinding     │  Scorer Bias     │  Gemini Provenance        │
│  Asymmetry       │                  │                           │
│  [short text]    │  [short text]    │  [short text]             │
│  [Read more ↓]   │  [Read more ↓]   │  [Read more ↓]            │
└──────────────────┴──────────────────┴───────────────────────────┘
```

Each caveat card has an inline "Read more" toggle that expands to show the full disclosure text without navigating away.

### Accessibility
- `role="region"` with `aria-label="Methodological caveats"`
- Each badge has `aria-label="Caveat: [title]"`
- Expand/collapse button has `aria-expanded` state attribute

---

## 3. Per-Chart Caveat Surfacing

### Principle
Charts are grouped by which caveats apply. The caveat badge(s) appear as small pill tags in the chart header, not in tooltips (tooltips are for data, not methodology). Clicking a badge scrolls to the ribbon and highlights the relevant caveat card for 2 seconds.

### T2 Performance Tab (all charts)
**Applies:** CAV-1 (T2 Blinding Asymmetry)

- T2 overall accuracy bar chart: CAV-1 badge in chart header. Caption: "Claude accuracy figures are upper-bound estimates due to gold-label exposure during original trials; cross-vendor trials used blind protocol."
- T2 beginner vs. advanced breakdown: CAV-1 badge. Caption note: "Haiku's 76.7% accuracy provides evidence of independent answering even under contaminated conditions."
- T2 span visualization (6.7%–100%): CAV-1 badge. The chart title should include the qualifier "(blind-asymmetric)" in the axis label for the Claude cluster.

### Cross-Vendor Rubric Tab (all charts)
**Applies:** CAV-2 (Scorer Bias) + CAV-3 (Gemini Provenance)

- Rubric heatmap (K/R/V/Bias by model): Both CAV-2 and CAV-3 badges. Caption: "Claude rubric scores reflect same-vendor evaluation; Gemini rubric scores reflect backfilled template extraction."
- Behavioral typology diagram: CAV-3 badge on the Gemini cluster. The "template refusal" label should be rendered in italic to signal interpretive uncertainty.
- K<R<V gradient chart (response lengths): CAV-2 badge only. The length gradient does not depend on rubric scoring; scorer bias caveat applies only because rubric scores appear in the same view.

### Rubric Ceiling Tab
**Applies:** CAV-2 (Scorer Bias)

- All charts showing ≥0.93 rubric scores: CAV-2 badge. Caption: "All Claude rubric scores are same-vendor assessments by Claude Opus; ceiling effect may partly reflect shared evaluative standards."

### Claims Tab (C8: Values Relevance Failure)
**Applies:** None of the three caveats directly — but the A3 scoring was also performed by Claude Opus (scorer bias). Add a note in the C8 card: "A3 values relevance scoring was conducted by Claude Opus (same-vendor). The large effect size (d=−1.23) across multiple convergent tests mitigates but does not eliminate this concern."

### T2 Accuracy Tab within Cross-Vendor Charts
**Applies:** CAV-1 + CAV-3

- Any chart showing Gemini T2 accuracy alongside Claude T2 accuracy: Both badges. This is the only cross-vendor comparison where both caveats are materially relevant simultaneously.

### Claims Tab (C1–C7, survey-based claims)
**Applies:** None of the three caveats. These claims are derived from the benchmark corpus survey, not from trial administration. No caveat badge needed. A clean claims presentation reinforces that the survey findings are independent of the trial methodology caveats.

---

## 4. Methods Disclosure Footer

Placed at the bottom of every page, below all tab content, always visible (not inside a tab panel).

### Content

```
Methods Disclosure

Corpus: 401 benchmark candidates screened from 2,099 AI ethics papers + 72 external queries across
Semantic Scholar, arXiv, and HuggingFace (2021–2026). Hard gates: Theological Depth ≥30 and public
data availability. 47 benchmarks passed both gates; 45 remain after post-review removals.

Scoring framework: 22 features across 3 axes — Religious/Theological Depth (RD), Practical Ease (PE),
Citation Impact (CI) — each normalized 0–100. Composite = 0.50·RD + 0.35·PE + 0.15·CI.
Ranking robustness: 1,000 bootstrap iterations across 61 weight configurations (Dirichlet α=20).

Implementation trials: 65-item construct validity battery (Knowledge, Reasoning, Values, Bias items;
Islam, Christianity, Hinduism) + 30-item Arabic MCQ (fara'id). 9 models from 3 vendors.

Statistical tests: χ² goodness-of-fit (C1), exact binomial (C2, C3, C5, C7, C8), Fisher's exact
(C6), logistic regression (C4), one-sample t-test and Wilcoxon signed-rank (C8).
Bonferroni-corrected α = 0.00625. Claims 1, 2, 3, 8 survive correction.

All non-Anthropic vendor data is Claude-simulated (Sonnet/Haiku roleplay), not real API calls.
Three methodological caveats apply — see ribbon above.

Code and data: 3-axis scoring framework, feature matrix, and tiered ranking released as community
resources. Statistical computations: scipy.stats (Python 3.9). Bootstrap: numpy.random (fixed seeds).
```

### Styling
- Compact monospaced-adjacent font (14px), muted text color (`--text-muted`)
- Bordered top rule, two-column layout on wide screens, single column on mobile
- "All non-Anthropic vendor data is Claude-simulated" line in amber to reinforce the simulation caveat at a glance
- No heading larger than H4; this is disclosure text, not a featured section

---

## 5. "How to Interpret" Expandable Section

Placed on the landing/overview tab, directly below the abstract summary and above the first chart cluster. Collapsed by default on return visits; expanded on first load (same localStorage pattern as ribbon).

### Section heading
`How to read this dashboard` (H3, with ▼/▲ toggle)

### Content blocks (5 sub-sections, each independently togglable)

---

**5a. P-values**

> A p-value is the probability of observing results at least as extreme as these if there were actually no difference in the population. It does NOT measure the size of an effect or the probability that a finding is true.
>
> In this dashboard: p < 0.05 is flagged as "significant" (conventional threshold). Claims 1, 2, 3, and 8 also survive the stricter Bonferroni-corrected threshold (p < 0.00625), meaning their significance is not an artifact of testing eight claims simultaneously. Claims 4, 5, 6, and 7 do not reach significance — this is reported honestly, not hidden.

---

**5b. Effect Sizes**

> Effect size measures how large a difference is, independent of sample size. Small p-values with tiny effect sizes indicate a statistically detectable but practically trivial difference.
>
> This dashboard uses three effect size measures:
> - **Cohen's d** (for mean comparisons): small = 0.2, medium = 0.5, large = 0.8. The values relevance finding (Claim 8) has d = −1.23 — a very large effect.
> - **Cramer's V** (for count distributions): small = 0.1, medium = 0.3, large = 0.5. The tradition asymmetry finding (Claim 1) has V = 0.53 — a large effect.
> - **Odds ratio** (for binary comparisons): OR = 1.0 means no difference; OR > 1 means the first group is more likely; OR < 1 means less likely.

---

**5c. Bootstrap Confidence Intervals**

> Bootstrapping re-runs the analysis thousands of times on resampled versions of the data to estimate how stable a result is. A narrow confidence interval means the result is stable across data perturbations; a wide interval means it depends heavily on which specific papers happened to be included.
>
> In this dashboard: the composite ranking was computed 1,000 times across 61 different weight configurations. Tier assignments (Tier 1/2/3) reflect which benchmarks ranked consistently in the top 12/3/10 across the majority of these runs — not just in a single weight configuration.

---

**5d. What "simulated" means for cross-vendor data**

> This project runs in an environment where only Anthropic (Claude) API calls are available. OpenAI and Gemini results were generated by asking Claude to roleplay as those models — Claude Sonnet roleплaying as GPT-Codex, Claude Haiku roleplaying as Codex-Mini, and so on for Gemini.
>
> This means cross-vendor findings are NOT real GPT or Gemini API results. They are Claude's best approximation of how those models might respond, based on its training data knowledge of their behavior. All charts that include OpenAI or Gemini data carry a "(simulated)" label for this reason.
>
> The T2 Arabic MCQ is partially exempt: Claude Haiku was used as a Gemini proxy, and Haiku genuinely does not know Islamic inheritance law as well as Opus/Sonnet, so the low simulated Gemini T2 scores may reflect genuine within-Claude capability differences rather than pure roleplay. But they are still not Gemini's actual T2 accuracy.

---

**5e. Three-tier benchmark ranking**

> Benchmarks are ranked using a composite score combining Religious/Theological Depth (50%), Practical Ease (35%), and Citation Impact (15%). The tiering is:
> - **Tier 1 (top 12):** Score ≥ 52.0 — field-leading benchmarks. For reference, the leading normative ethics benchmark scores 77.2.
> - **Tier 2 (next 3):** Score 47.0–52.0 — high-quality but with meaningful gaps in depth, accessibility, or impact.
> - **Tier 3 (remaining 30):** Score < 47.0 — viable candidates with one or more significant limitations.
>
> The composite range of 39.9–52.0 across all tiered benchmarks indicates that no religious values instrument has yet achieved field-defining quality on this framework.

---

## Implementation Notes for the v7 Developer

1. **Ribbon first, then tab content.** The ribbon must be inserted before `<main>` in the DOM order so screen readers encounter caveats before data.

2. **Badge links.** Each per-chart badge should be an `<a>` element with `href="#caveat-ribbon"` and a JS click handler that (a) expands the ribbon if collapsed, (b) scrolls to ribbon, (c) adds a 2-second `highlight` class to the relevant caveat card, then removes it.

3. **Caveat IDs.** Use `id="cav-1"`, `id="cav-2"`, `id="cav-3"` on the three caveat cards in the ribbon for anchor targeting.

4. **Footer placement.** The footer sits outside all tab panels — inside `<body>` but after `</main>`. It should not be tab-specific.

5. **"How to interpret" localStorage key:** `rv7_howto_expanded` (boolean string). Default: `"true"` on first load.

6. **Caveat ribbon localStorage key:** `rv7_caveat_ribbon` (value: `"expanded"` or `"collapsed"`). Default: `"expanded"` on first load.

7. **No simulated cross-vendor data should appear without a "(simulated)" label** in axis labels, chart titles, or legend entries. This is non-negotiable — see memory note on no non-Anthropic models.

8. **Gemini chart cluster.** Gemini bars/points should be visually distinguished (dashed border, lower opacity, or hatching pattern) to reinforce the provenance caveat at a glance, independent of badge labels.
