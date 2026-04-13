# Data Contract: RV Dashboard v7

**Version:** 7.0
**Generated:** 2026-04-13
**Canonical data file:** `claims_canonical.json`
**DOM skeleton:** `dom-skeleton.html`

---

## 1. Claims Array Schema

Each of the 8 claims is normalized into this shape:

```json
{
  "claim_id": "C1",
  "claim_number": 1,
  "title": "string",
  "tests": [
    {
      "test_name": "string",
      "statistic": 64.957,
      "statistic_name": "chi-squared",
      "p_value": 0.0,
      "effect_size": 0.526,
      "effect_size_name": "Cramer's V",
      "ci_low": null,
      "ci_high": null,
      "n": 47,
      "significant": true
    }
  ],
  "verdict": "supported" | "revised" | "not_significant",
  "plain_english": "string"
}
```

**Normalization rules:**
- C1 and C8 have nested `tests: [...]` arrays in source data. Each sub-test becomes an entry in `tests`.
- C2-C7 have flat `statistic`/`p_value` at claim level. These are wrapped into a single-element `tests` array.
- `verdict` is derived: `"supported"` if significant=true, `"revised"` for C4/C5/C6/C7 where the claim was revised per the paper, `"not_significant"` if p >= 0.05 and not revised.
- `plain_english` is a one-sentence lay summary from the paper abstract/results.

### Verdict Mapping

| Claim | significant | verdict |
|-------|-------------|---------|
| C1 | true | supported |
| C2 | true | supported |
| C3 | true | supported |
| C4 | false | revised |
| C5 | false | not_significant |
| C6 | false | revised |
| C7 | false | not_significant |
| C8 | true | supported |

---

## 2. Cross-Vendor Typology Schema

```json
{
  "cross_vendor_typology": {
    "differentiated_engagement": {
      "label": "Differentiated Engagement",
      "simulated_label": "Claude family (Opus, Sonnet, Haiku) -- original vendor",
      "vendor": "Anthropic",
      "description": "string",
      "key_metrics": {
        "rubric_k": 1.0,
        "rubric_r": 1.0,
        "rubric_v_min": 0.933,
        "mean_k_length": 1463.3,
        "mean_v_length": 6572.1,
        "gradient_holds": true
      }
    },
    "compressed_accuracy": {
      "label": "Compressed Accuracy",
      "simulated_label": "Claude-roleplaying-OpenAI-scorer (Codex, Codex-Mini)",
      "vendor": "OpenAI (simulated)",
      "description": "string",
      "key_metrics": {
        "rubric_k": 0.967,
        "rubric_r": 0.917,
        "rubric_v_min": 0.867,
        "response_compression": "5-80x shorter than Claude",
        "gradient_holds": false
      }
    },
    "template_refusal": {
      "label": "Template Refusal",
      "simulated_label": "Claude-roleplaying-Gemini-scorer (4 Gemini models, backfilled)",
      "vendor": "Gemini (simulated)",
      "description": "string",
      "key_metrics": {
        "rubric_k": 0.0,
        "rubric_r": 0.0,
        "rubric_v_max": 0.2,
        "bias_score_range": "0.567-1.0",
        "gradient_holds": false
      }
    }
  }
}
```

---

## 3. T2 Span Table Schema

```json
{
  "t2_span": {
    "min_accuracy": 0.0667,
    "max_accuracy": 1.0,
    "span_pp": 93.3,
    "min_model": "gemini-2.5-pro",
    "max_model": "claude-opus-4-6",
    "max_models_at_ceiling": ["claude-opus-4-6", "claude-sonnet-4-20250514", "gpt-codex"],
    "per_model": [
      {
        "model": "string",
        "vendor": "string",
        "simulated": false,
        "t2_overall": 1.0,
        "t2_beginner": 1.0,
        "t2_advanced": 1.0
      }
    ]
  }
}
```

---

## 4. Rubric Ceiling Matrix Schema

```json
{
  "rubric_ceiling": {
    "threshold": 0.93,
    "note": "All Claude models achieve >= 0.93 on K, R, V rubrics",
    "matrix": [
      {
        "model": "string",
        "vendor": "string",
        "simulated": false,
        "rubric_knowledge": 1.0,
        "rubric_reasoning": 1.0,
        "rubric_values": 0.933,
        "rubric_bias": 1.0,
        "at_ceiling": true
      }
    ]
  }
}
```

---

## 5. Caveats Array Schema

```json
{
  "caveats": [
    {
      "id": "CAV-1",
      "title": "string",
      "short_description": "string (1 sentence)",
      "full_description": "string (paragraph)"
    }
  ]
}
```

Three caveats:
- **CAV-1**: T2 Blinding Asymmetry
- **CAV-2**: Same-Vendor Scorer Bias
- **CAV-3**: Gemini Data Provenance

---

## 6. Metadata Schema

```json
{
  "metadata": {
    "source_files": [
      "data/20260404-claim-robustness-tests.json",
      "COMPARISON/results/vendor-comparison.json",
      "COMPARISON/results/model-comparison.json",
      "PAPER-V2/03-discussion.md",
      "PAPER-V2/02-results.md",
      "PAPER-V2/00-abstract.md"
    ],
    "generated_date": "2026-04-13",
    "version": "7.0",
    "note": "All cross-vendor data is Claude-simulated (Sonnet/Haiku roleplay), not real GPT/Gemini API calls"
  }
}
```

---

## 7. DOM IDs and CSS Classes

### Tab Navigation

| Tab # | Nav ID | Pane ID | Label | Subtitle |
|-------|--------|---------|-------|----------|
| 1 | `nav-overview` | `tab-overview` | Overview | 401 -> 47 screening |
| 2 | `nav-landscape` | `tab-landscape` | Landscape | Ranking robustness |
| 3 | `nav-ranking` | `tab-ranking` | Ranking | Tiered benchmarks |
| 4 | `nav-traditions` | `tab-traditions` | Tradition Coverage | 8 missing traditions |
| 5 | `nav-claims` | `tab-claims` | Claims & Robustness | 8 statistical tests |
| 6 | `nav-crossvendor` | `tab-crossvendor` | Simulated Scorer Study | 9 models, 3 vendors (simulated) |

### Chart Container IDs

#### Tab 1: Overview
- `chart-tradition-bar` -- tradition distribution bar chart
- `chart-family-pie` -- tradition family pie chart
- `chart-funnel` -- 401 -> 47 screening funnel

#### Tab 2: Landscape
- `chart-boot-ci` -- bootstrap CI for rankings
- `chart-weight-sens` -- weight sensitivity analysis
- `chart-gate-threshold` -- gate threshold sensitivity

#### Tab 3: Ranking
- `chart-tier-table` -- tiered ranking table/heatmap
- `chart-composite-bar` -- composite score bar chart

#### Tab 4: Tradition Coverage
- `chart-radar` -- tradition coverage radar
- `chart-readiness` -- readiness assessment chart
- `chart-void-grid` -- 8-tradition void grid

#### Tab 5: Claims & Robustness
- `chart-claims` -- claim evidence summary (existing)
- `chart-claim8-forest` -- **NEW** C8 forest plot (4 sub-tests)
- `chart-claim1-forest` -- **NEW** C1 forest plot (2 sub-tests)
- `chart-pvalue-strip` -- p-value dot strip for all 8 claims

#### Tab 6: Simulated Scorer Study
- `chart-cv-length` -- K < R < V response length gradient
- `chart-cv-rubric` -- rubric heatmap (model x dimension)
- `chart-cv-t2` -- T2 accuracy by model bar chart
- `chart-cv-radar` -- vendor-level radar
- `chart-cv-biasvalues` -- bias-values independence scatter
- `chart-vendor-typology-grid` -- **NEW** 3-mode typology cards
- `chart-t2-span-strip` -- **NEW** T2 accuracy span strip (6.7% to 100%)
- `chart-rubric-ceiling-heatmap` -- **NEW** model x K/R/V ceiling heatmap

### CSS Classes

| Class | Purpose |
|-------|---------|
| `card-rv` | Standard dashboard card container |
| `card-rv--claim` | Claim evidence card |
| `card-rv--caveat` | Caveat ribbon card |
| `card-rv--typology` | Vendor typology card |
| `caveat-ribbon` | Top caveat aside ribbon |
| `verdict-badge` | Claim verdict badge |
| `verdict--supported` | Green badge |
| `verdict--revised` | Amber badge |
| `verdict--not-significant` | Grey badge |
| `simulated-tag` | "Simulated" qualifier tag on vendor labels |
| `chart-container` | Standard ECharts container div |
| `tab-sub` | Tab subtitle span |
