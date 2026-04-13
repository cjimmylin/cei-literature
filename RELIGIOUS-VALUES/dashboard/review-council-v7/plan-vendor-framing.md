---
created: 2026-04-13
author: Simulated-Vendor Framing Officer
status: APPROVED — execute against dashboard v7
---

# Vendor Framing Plan — Dashboard v7 "Simulated Scorer Study" Tab

## 1. Tab Identity

**Tab name (nav label):** `Simulated Scorer Study`
Do NOT use "Cross-Vendor", "Multi-Vendor", "Vendor Comparison", or any variant that implies
independent real-world API access.

**Tab subtitle (rendered as a callout block directly beneath the tab header):**

> All non-Anthropic results in this tab were produced by Claude models (Sonnet and Haiku)
> role-playing as alternative vendor scorers following scripted behavioral protocols, not by
> real OpenAI or Google APIs. Results for the OpenAI-scorer and Gemini-scorer conditions
> should be treated as hypothesis-generating simulations rather than confirmed vendor
> benchmarks, and must be replicated with matched real-API protocols before publication.

The callout must use a visually distinct style (e.g., amber/warning card, left-border accent,
icon: warning triangle). It must appear before any chart in the tab — never buried in a footer.


## 2. Scorer Labels — Canonical Forms

The following label strings are the ONLY permitted forms throughout the entire tab (chart
titles, axis labels, legend entries, tooltips, annotations, and prose). No exceptions.

| Condition | Canonical Label | Short form (axis/legend only) |
|-----------|-----------------|-------------------------------|
| Anthropic Claude family | `Claude-as-Claude` | `Claude-as-Claude` |
| Simulated OpenAI scorer | `Claude-roleplaying-OpenAI-scorer` | `Sim: OpenAI-scorer` |
| Simulated Gemini scorer | `Claude-roleplaying-Gemini-scorer` | `Sim: Gemini-scorer` |

**Forbidden bare forms (anywhere in the tab, including code comments rendered as tooltips):**
- `OpenAI`, `GPT`, `GPT-4`, `Codex` (without the `Claude-roleplaying-` or `Sim:` prefix)
- `Gemini`, `Google` (without the `Claude-roleplaying-` or `Sim:` prefix)
- `Claude` alone when used to distinguish from simulated conditions — always `Claude-as-Claude`

Individual model names (`gpt-codex`, `gemini-2.5-pro`, etc.) MAY appear in tooltip detail
lines IF they are immediately preceded by the phrase `(simulated by Claude):`.

Example tooltip model line:
```
Model: (simulated by Claude): gpt-codex
```


## 3. Chart Title Prefix Rule

Every chart whose data includes any simulated-scorer condition MUST have its title prefixed
with `Simulated:` followed by a space and the descriptive title. The prefix is not optional
even when all conditions in the chart are simulated.

Examples:
- `Simulated: Response-Length Gradient by Construct Category`
- `Simulated: Rubric Score Matrix — Knowledge / Reasoning / Values / Bias`
- `Simulated: T2 Accuracy by Model and Difficulty Level`
- `Simulated: Behavioral Mode Summary — Differentiated vs. Compressed vs. Template`

Charts that display ONLY Claude-as-Claude data (no simulated conditions) do NOT require the
prefix. Use judgment: if a reader could confuse the scope, add the prefix anyway.


## 4. Tooltip Simulation Caveat

Every ECharts tooltip formatter in this tab MUST include a final line with the simulation
caveat. Use this exact text, adjusting `[condition]` as appropriate:

```
⚠ [Claude-roleplaying-OpenAI-scorer / Claude-roleplaying-Gemini-scorer] data is
  Claude-simulated, not real API output.
```

For `Claude-as-Claude` tooltips, the caveat line is:
```
✓ Claude-as-Claude: real Anthropic API output (Opus/Sonnet/Haiku).
```

Implementation note: add this as the last `<div>` inside the tooltip HTML template. Font size
should be 0.78em, color `var(--text-muted)` or equivalent dim tone, to visually subordinate
the caveat without hiding it.


## 5. Behavioral Mode Labels

The three behavioral modes from `claims_canonical.json → cross_vendor_typology` must be
identified by their descriptive behavior name as the PRIMARY label, with the scorer condition
in parentheses as a secondary qualifier.

| JSON key | Primary label (chart title, legend) | Secondary qualifier (parenthetical) |
|----------|-------------------------------------|-------------------------------------|
| `differentiated_engagement` | **Differentiated Engagement** | (Claude-as-Claude) |
| `compressed_accuracy` | **Compressed Accuracy** | (Claude-roleplaying-OpenAI-scorer) |
| `template_refusal` | **Template Refusal** | (Claude-roleplaying-Gemini-scorer) |

Usage pattern in prose annotations and chart subtitles:
```
Differentiated Engagement (Claude-as-Claude): K < R < V gradient holds across all
model tiers and tradition combinations.

Compressed Accuracy (Claude-roleplaying-OpenAI-scorer): near-ceiling rubric scores
(0.87–1.0) from responses 5–80× shorter than Claude-as-Claude.

Template Refusal (Claude-roleplaying-Gemini-scorer): 0.0 on K/R/V rubrics;
0.57–1.0 on Bias only. Explanation is underdetermined — three competing hypotheses,
no current evidence to distinguish them.
```

Never write "the Gemini mode" or "the OpenAI mode" as shorthand. Always use the behavior
name first.


## 6. T2 (fara'id) Framing

T2 is the Islamic inheritance law Arabic MCQ (30 items). It is the ONLY instrument in the
tab that provides genuine discriminative power; the rubric is ceiling/floor-bound and cannot
separate models. This must be communicated prominently.

### 6a. T2 Section Header

Every chart or panel displaying T2 results must include a section header or chart subtitle:

> T2 (fara'id Arabic MCQ) — Only Truly Discriminative Measure in This Study

### 6b. T2 Framing Annotation

Include a fixed annotation box (not a tooltip — always visible) near the T2 chart:

> **Why T2 matters:** The rubric produces ceiling effects for Claude-as-Claude and
> Claude-roleplaying-OpenAI-scorer, and floor effects for Claude-roleplaying-Gemini-scorer,
> making rubric scores uninformative for cross-condition comparison. T2 accuracy spans
> 6.7% – 100% (a 93.3 pp range), providing the only reliable basis for ordering models.
> T2 used a blind protocol (gold labels withheld) for all conditions except the original
> Claude-as-Claude trials, which had gold labels visible — those figures are upper-bound
> estimates.

### 6c. T2 Data Provenance Warning

In the T2 per-model breakdown chart, the tooltip for ALL Claude-as-Claude rows (Opus, Sonnet,
Haiku) must append:

```
⚠ Original Claude T2 trials: gold labels visible to evaluating system.
  Reported accuracy is an upper-bound estimate, not a blind measurement.
```

For simulated-scorer rows, the tooltip appends:
```
⚠ Simulated scorer (Claude role-play). Blind protocol applied (gold labels withheld).
```

### 6d. T2 Chart: Do Not Aggregate Into Mode Groups

Display T2 accuracy per individual model (9 rows), not collapsed by behavioral mode. The
within-mode variance (e.g., Gemini-simulated: 6.7% to 20%) is itself a finding and must not
be hidden by averaging. Use a horizontal bar chart ordered by T2 overall accuracy descending.
Color-code by condition using the canonical palette below, with simulated conditions rendered
with a hatched or dashed fill to distinguish from real-API output.

### 6e. T2 Key Metrics to Highlight

| Metric | Value | Source |
|--------|-------|---------|
| Accuracy span | 93.3 pp | `claims_canonical.json → t2_span.span_pp` |
| Ceiling models (100%) | Opus, Sonnet, gpt-codex (simulated) | `t2_span.max_models_at_ceiling` |
| Floor model (6.7%) | gemini-2.5-pro (simulated) | `t2_span.min_model` |
| Haiku divergence | beginner 80%, advanced 73.3% | `t2_span.per_model[claude-haiku-4-5]` |
| Simulated Gemini range | 6.7%–20% across 4 models | computed from `t2_span.per_model` |


## 7. Canonical Color Palette for This Tab

Consistent color identity reduces reader confusion. Adhere strictly.

| Condition | Fill color | Border / hatch | Hex |
|-----------|-----------|---------------|-----|
| Claude-as-Claude | Solid fill | None | `#5b8ff9` (blue) |
| Claude-roleplaying-OpenAI-scorer | Hatched fill | Diagonal lines | `#61d9aa` (teal) |
| Claude-roleplaying-Gemini-scorer | Hatched fill | Cross-hatch | `#f6bd16` (amber) |

Hatching on simulated conditions serves as a persistent visual reminder that data is
simulated, independent of tooltips. Implement via SVG pattern fill in ECharts custom renderer
or use reduced opacity (0.55) with a dashed border as fallback if pattern fill is unavailable.

The legend must display a small `[simulated]` badge (grey pill, 0.7em) next to every
simulated condition label. Claude-as-Claude gets a `[real API]` badge in the same style.


## 8. Underdetermined Gemini Explanation — Display Rules

The paper's discussion explicitly states that the Template Refusal pattern is
"underdetermined" — three hypotheses exist and current evidence cannot distinguish them.
The dashboard MUST reflect this epistemic state. Do NOT present any single explanation as
confirmed.

In any annotation, tooltip, or panel text describing Template Refusal:

```
Template Refusal results are underdetermined. Three competing explanations exist:
(a) safety filtering on religious content, (b) training data gaps for theological
reasoning, (c) methodological artifact of the backfilled/template-extraction protocol.
The available data cannot distinguish among them. Treat as a provisional hypothesis
pending matched-protocol replication.
```

Never write: "Gemini refuses religious content due to safety filters" or any other
single-explanation framing.


## 9. Rubric Ceiling / Same-Vendor Scorer Caveat

The rubric ceiling paradox (all Claude-as-Claude models at ≥ 0.93; compressed-accuracy
simulated scorer also at 0.87–1.0) must be surfaced in the Rubric Score Matrix chart with a
fixed overlay annotation:

> Rubric scoring performed by Claude Opus 4.6. Same-vendor scoring of Claude-as-Claude
> responses introduces potential inflation bias. Rubric scores should NOT be used to
> compare conditions — use T2 accuracy for cross-condition ordering.


## 10. Tab Layout Order

Sections must appear in this sequence to ensure the framing callout appears before data:

1. **Simulation Protocol Callout** (amber warning card — see Section 1)
2. **Behavioral Mode Summary** — three-card layout, one per mode, primary label first
3. **Rubric Score Matrix** — chart with ceiling annotation (Section 9)
4. **Response-Length Gradient** — bar chart grouped by condition and construct category
5. **T2 (fara'id) Results** — section header per 6a, annotation per 6b, per-model bars per 6d
6. **Methodological Limitations Panel** — static text listing all caveats (T2 blinding
   asymmetry, same-vendor scorer bias, Gemini backfilled protocol, underdetermined Template
   Refusal explanation, replication requirement)

The Methodological Limitations Panel in item 6 must reproduce the four cross-vendor
limitations from `03-discussion.md` (items 12–16 in the limitations list) verbatim or
near-verbatim. This is non-negotiable — the paper's limitation disclosure must propagate
to the dashboard.


## 11. Strings That Must Never Appear (Anywhere in Tab DOM or JS Source)

The following strings are forbidden in rendered HTML, chart titles, tooltip text, JS
variable names used as display strings, and data labels. Automated lint check recommended
before merge.

```
Forbidden:
  "Cross-Vendor"
  "cross-vendor"
  "OpenAI"          (without "Claude-roleplaying-" or "Sim:" prefix)
  "GPT"             (without "Claude-roleplaying-" or "(simulated by Claude):" prefix)
  "Gemini"          (without "Claude-roleplaying-" or "Sim:" prefix)
  "Google"          (in context of model vendor)
  "Vendor A / B / C" (anonymization is not permitted — the simulation framing must be explicit)
  "real GPT"
  "actual Gemini"
  "GPT-4o"          (this model was never part of the study)
  "cross-model replication" (use "simulated-scorer replication" instead)
```

Permitted in JS source only (not rendered):
  `gpt-codex`, `gemini-2.5-pro` etc. as internal data keys, provided they are never
  surfaced in any rendered label without the `(simulated by Claude):` prefix.


## 12. Handoff Checklist for Implementing Agent

Before marking the Simulated Scorer Study tab as complete, verify each item:

- [ ] Tab nav label reads "Simulated Scorer Study" (not "Cross-Vendor")
- [ ] Simulation protocol callout appears as first DOM element in tab body
- [ ] All three scorer conditions use canonical labels (Section 2) in every chart
- [ ] Every chart title is prefixed "Simulated:" where required (Section 3)
- [ ] Every tooltip ends with the 1-line simulation caveat (Section 4)
- [ ] Behavioral mode cards lead with descriptive label, scorer condition in parentheses (Section 5)
- [ ] T2 section header present: "T2 (fara'id Arabic MCQ) — Only Truly Discriminative Measure" (Section 6a)
- [ ] T2 annotation box always visible, not tooltip-only (Section 6b)
- [ ] T2 per-model chart shows 9 individual rows, not collapsed by mode (Section 6d)
- [ ] T2 Claude-as-Claude rows have upper-bound-estimate provenance warning (Section 6c)
- [ ] Simulated conditions rendered with hatched/dashed fill (Section 7)
- [ ] `[simulated]` / `[real API]` badges in legend (Section 7)
- [ ] Template Refusal annotation uses underdetermined framing (Section 8)
- [ ] Rubric ceiling overlay annotation present (Section 9)
- [ ] Methodological Limitations Panel is last section, caveats reproduced from paper (Section 10)
- [ ] Lint check confirms no forbidden strings in rendered DOM (Section 11)
