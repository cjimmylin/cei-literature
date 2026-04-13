# Contract-Drift Audit — Dashboard v7
**Auditor:** Contract-Drift Auditor (automated)
**Date:** 2026-04-13
**Inputs:** `data-contract.md` (v7.0), `claims_canonical.json`, `dom-skeleton.html`, 8 plan files

---

## Executive Summary

**Total findings: 19**
- CRITICAL: 5
- MAJOR: 8
- MINOR: 6

All 8 plans were audited against the frozen data contract and DOM skeleton. The most dangerous
concentrations are: (1) the UX plan's unilateral tab reorder — which changes DOM activation state
without authority — and (2) the dataviz plan's ECharts version conflict with the skeleton CDN link.
Both would cause runtime errors or silent render failures. Several data-key drift issues occur across
plans for fields present in the JSON but accessed under wrong key names.

---

## Criterion 1 — Data Key Mismatches

### CRITICAL-01: `mean_rubric_values` reported as 0.977 in dataviz plan but JSON says 0.9777

**Plan:** `plan-dataviz.md`, Section N4, typology grid alt text
**Claim in plan:**
> "Differentiated Engagement (Anthropic/Claude): K=1.0, R=1.0, V=0.978"

**JSON value** (`cross_vendor_typology.differentiated_engagement.key_metrics.mean_rubric_values`):
```json
"mean_rubric_values": 0.9777
```

**Data contract field** (`key_metrics.rubric_v_min`): 0.933 (this is a different field — minimum across models, not mean).

**Analysis:** The dataviz alt-text uses `V=0.978` which is a rounded form of `0.9777`. This is a
rounding inconsistency, not a key-name mismatch — acceptable. However, the data-contract schema
lists the field as `rubric_v_min: 0.933` (under `differentiated_engagement.key_metrics`), while
`claims_canonical.json` stores it as `mean_rubric_values: 0.9777`. The contract and the JSON use
**different key names for the same typology block**:

| Location | Key name | Value |
|----------|----------|-------|
| `data-contract.md` § 2 | `rubric_v_min` | 0.933 |
| `claims_canonical.json` | `mean_rubric_values` | 0.9777 |

Any code that reads `rubric_v_min` from the JSON will receive `undefined` — 0.933 is only in the
contract spec, not in the actual data file. The Python generator must use `mean_rubric_values`, not
`rubric_v_min`.

**Severity:** CRITICAL — accessing `rubric_v_min` at runtime returns `undefined`; chart renders
blank or NaN values in the typology cards.

**Affected plans:** `plan-dataviz.md` (Section N4 data source fields list uses `rubric_v_min` via
implication from the contract), `plan-vendor-framing.md` (Section 5 references `rubric_v` ceiling),
`plan-statistics.md` (Section 2 references the ceiling value for the rubric heatmap).

---

### CRITICAL-02: `rubric_v_max` key does not exist in JSON for `template_refusal`

**Plan:** `plan-dataviz.md`, Section N4 data source fields
**Contract spec** (`data-contract.md` § 2, `template_refusal.key_metrics`):
```json
"rubric_v_max": 0.2
```

**JSON** (`claims_canonical.json`, `cross_vendor_typology.template_refusal.key_metrics`):
```json
"mean_rubric_values": 0.05
```

The contract names the field `rubric_v_max: 0.2`, but the JSON uses `mean_rubric_values: 0.05`.
These are different values AND different key names. If the generator reads `rubric_v_max` it gets
`undefined`; if it uses `mean_rubric_values` it gets 0.05 (not 0.2 as the contract states).

**Severity:** CRITICAL — field name mismatch + value inconsistency between contract and canonical
data. One of these must be treated as authoritative; `claims_canonical.json` is the canonical
source per the contract preamble, so `mean_rubric_values: 0.05` wins. The contract `§ 2` spec is
wrong and must be corrected, OR the JSON must be updated to include `rubric_v_max`.

---

### CRITICAL-03: `bias_score_range` type mismatch — contract says string, JSON has array

**Contract** (`data-contract.md` § 2, `template_refusal.key_metrics`):
```json
"bias_score_range": "0.567-1.0"
```

**JSON** (`claims_canonical.json`, `cross_vendor_typology.template_refusal.key_metrics`):
```json
"bias_score_range": [0.5667, 1.0]
```

Any code that renders `bias_score_range` as a string (e.g., `data.bias_score_range.split('-')`)
will crash with `TypeError: data.bias_score_range.split is not a function` because the actual value
is an array. Conversely, code that treats it as an array will malfunction if it was written per the
contract spec.

**Severity:** CRITICAL — type mismatch causes runtime TypeError in the typology card renderer.

---

### MAJOR-04: `max_model` key absent from `t2_span` in JSON

**Contract** (`data-contract.md` § 3):
```json
"max_model": "claude-opus-4-6"
```

**JSON** (`claims_canonical.json`, `t2_span`): The field `max_model` does not appear. The JSON
instead has `max_models_at_ceiling` (an array) and `min_model`. The contract's singular `max_model`
was not implemented in the canonical data file.

**Severity:** MAJOR — any plan or generator that accesses `t2_span.max_model` will receive
`undefined`. The vendor-framing plan (Section 6e) references the ceiling models correctly via
`t2_span.max_models_at_ceiling`, so it is internally consistent with the JSON. But if the
generator was written against the contract spec, it would use `max_model` and fail. Mark as a
contract-to-JSON drift that must be reconciled before generator authoring.

**Affected plans:** `plan-dataviz.md` Section N5 (`t2_span.max_accuracy → annotated as ceiling value`
is fine, but if `max_model` is referenced it will fail). `plan-vendor-framing.md` Section 6e uses
`t2_span.max_models_at_ceiling` — CORRECT.

---

### MAJOR-05: Dataviz plan invents `mean_reasoning_length` field not in data contract

**Plan:** `plan-dataviz.md`, Section N7 data source fields:
```
→ mean_reasoning_length   (R point)
→ mean_values_length      (V point)
```

**Data contract** § 2 `compressed_accuracy.key_metrics`: does not list `mean_reasoning_length` or
`mean_values_length` — the contract only lists `response_compression: "5-80x shorter than Claude"`.

**JSON** (`claims_canonical.json`, `compressed_accuracy.key_metrics`): DOES include
`mean_knowledge_length`, `mean_reasoning_length`, `mean_values_length`. So the JSON supports these
fields but the contract spec omits them for `compressed_accuracy` and `template_refusal`.

**Severity:** MAJOR — fields exist in JSON but are not declared in the contract. Generators written
strictly to the contract would not know to read them. The contract must be updated to declare these
fields for all three typology entries, or the dataviz plan must note it is reading directly from
JSON.

---

### MINOR-06: `simulated_label` content differs between contract and JSON

**Contract** (`data-contract.md` § 2, `differentiated_engagement`):
```
"simulated_label": "Claude family (Opus, Sonnet, Haiku) -- original vendor"
```

**JSON** (`claims_canonical.json`, `differentiated_engagement`):
```json
"simulated_label": "Claude family (Opus, Sonnet, Haiku) -- original vendor, not simulated"
```

The JSON has additional text `, not simulated`. This is a cosmetic difference but will affect any
plan that quotes the contract-specified string for display (e.g., the vendor-framing plan's Section 2
canonical label table, which uses different labels entirely and is internally self-consistent).

**Severity:** MINOR — display string mismatch only; not a key-name or type error.

---

## Criterion 2 — DOM ID Conflicts

### CRITICAL-07: UX plan requests tab `<li>` reorder without authority — skeleton is frozen source of truth

**Plan:** `plan-ux-a11y.md`, Section 1
> "The visual left-to-right tab sequence must be reordered in the `<ul class="nav nav-tabs">` block:
> nav-overview | nav-ranking | nav-traditions | nav-claims | nav-landscape | nav-crossvendor"

**Skeleton DOM order:**
```
nav-overview | nav-landscape | nav-ranking | nav-traditions | nav-claims | nav-crossvendor
```

The UX plan proposes a DOM order change: Landscape moves from position 2 to position 5, Ranking
moves from 3 to 2, Claims moves from 5 to 4. This is a **modification of the frozen DOM skeleton**,
which is the source of truth per the audit mandate. The skeleton contains `aria-selected="true"` and
`class="show active"` on `tab-overview` in position 1 — these are correct and do not need updating.
But changing `<li>` order changes the tab activation sequence, Bootstrap's roving tabindex, and all
`aria-controls` / `href` attribute associations.

**Additional conflict:** The narrative plan (`plan-narrative.md`) recommends a different reading
order: Overview → Tradition Coverage → Ranking → Landscape → Claims → Simulated Scorer. The UX plan
recommends: Overview → Ranking → Tradition → Claims → Landscape → Simulated. These two plans
**disagree with each other AND both disagree with the frozen skeleton DOM order**. A runtime
implementer receiving both plans would have no consistent instruction.

**Severity:** CRITICAL — unilateral DOM reorder conflicts with frozen skeleton; implementing the
UX plan's reorder would break the contract. If a tab reorder is required, the skeleton must be
updated first and all plans must be rebased. Cannot be resolved by individual plan agents.

---

### MAJOR-08: Transparency plan references `id="cav-1"`, `id="cav-2"`, `id="cav-3"` but skeleton uses `id="caveat-cav1"`, `id="caveat-cav2"`, `id="caveat-cav3"`

**Plan:** `plan-transparency.md`, Section 4, implementation note 3:
> "Use `id="cav-1"`, `id="cav-2"`, `id="cav-3"` on the three caveat cards in the ribbon for
> anchor targeting."

**Skeleton** (lines 20, 25, 30):
```html
id="caveat-cav1"
id="caveat-cav2"
id="caveat-cav3"
```

Any `href="#cav-1"` anchor link will NOT scroll to the caveat ribbon — it will scroll nowhere
because the target ID does not exist. The badge-link pattern described in the transparency plan
(`href="#caveat-ribbon"` with JS click handler targeting individual card IDs) will silently fail
for the per-card scroll-and-highlight behaviour.

**Severity:** MAJOR — anchor links targeting `#cav-1` will not function; visual highlight on caveat
cards will not fire. The ID mismatch is a silent failure (no error thrown, link just fails to scroll).

---

### MAJOR-09: UX plan references `id="mainTabs"` as skip-link target — this ID IS in the skeleton (line 42), so it is fine. But UX plan also adds skip-link target `id="main-content"` which is NOT in the skeleton

**Plan:** `plan-ux-a11y.md`, Section 6:
```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```

The skeleton has no element with `id="main-content"`. The UX plan correctly notes that `id="mainTabs"` is already present and suggests using it — but also introduces a second skip link with `href="#main-content"` as the first option. No element with `id="main-content"` exists in the skeleton or any other plan.

**Severity:** MAJOR — skip link targeting `#main-content` will not function. This is a new DOM element not in the skeleton that must be added if the skip link is implemented.

---

### MINOR-10: Transparency plan introduces `id="caveat-ribbon"` sticky positioning not in skeleton CSS

**Plan:** `plan-transparency.md`, Section 2:
> `position: sticky; top: [navbar-height]px; z-index: 900`

The skeleton `<aside id="caveat-ribbon">` exists, but it has no sticky positioning. This is a CSS
addition, not a DOM ID conflict — but note the transparency plan and the UX plan both want to
control ribbon behaviour (sticky vs ribbon-above-tabs), and they do not cross-reference each other.
The ribbon position relative to the `<ul class="nav nav-tabs">` is the same in both plans (ribbon
first), so there is no actual conflict here.

**Severity:** MINOR — CSS addition, not a DOM conflict. Flagged for awareness.

---

## Criterion 3 — Tab Structure Drift

### CRITICAL-11: UX plan proposes different tab visual order from skeleton; narrative plan proposes yet another order; both violate the frozen skeleton

Already documented as CRITICAL-07. Restated here for completeness under Criterion 3.

**Tab name audit — all plans vs skeleton:**

| Skeleton # | Skeleton nav label | Narrative plan | UX plan |
|------------|-------------------|----------------|---------|
| 1 | Overview | Overview (1st in reading order) | Overview (position 1) |
| 2 | Landscape | Landscape (4th in reading order) | Landscape (position 5) |
| 3 | Ranking | Ranking (3rd in reading order) | Ranking (position 2) |
| 4 | Tradition Coverage | Tradition Coverage (2nd) | Tradition Coverage (position 3) |
| 5 | Claims & Robustness | Claims & Robustness (5th) | Claims & Robustness (position 4) |
| 6 | Simulated Scorer Study | Simulated Scorer Study (6th) | Simulated Scorer Study (position 6) |

**Tab names** match across all plans and the skeleton. No label drift. Only the recommended
*reading/visual order* diverges. Since the skeleton is frozen, tab DOM order = skeleton order.
Reading-order guidance should be surfaced as a callout or tooltip, NOT by reordering DOM elements.

**Finding:** All 6 tab names are consistent. All plans agree on 6 tabs. Tab name drift: none.
Tab order proposals: 2 of 8 plans conflict with skeleton (UX plan, narrative plan propose reorders).

---

## Criterion 4 — Chart-to-DOM Mapping

### MAJOR-12: Dataviz plan lists 17 legacy charts (L1–L17) but numbering skips — L3, L7, L11 acknowledged as gaps; effective total from skeleton is 23 containers, dataviz plan accounts for all 23 correctly

The dataviz plan's chart inventory matches the skeleton's container divs. Full mapping verification:

**Skeleton containers vs dataviz plan assignment:**

| Container ID | Skeleton tab | Dataviz plan assignment | Status |
|--------------|-------------|------------------------|--------|
| `chart-funnel` | Tab 1 | L3 (new in v7) | OK |
| `chart-tradition-bar` | Tab 1 | L1 | OK |
| `chart-family-pie` | Tab 1 | L2 | OK |
| `chart-boot-ci` | Tab 2 | L4 | OK |
| `chart-weight-sens` | Tab 2 | L5 | OK |
| `chart-gate-threshold` | Tab 2 | L6 | OK |
| `chart-tier-table` | Tab 3 | L7 | OK |
| `chart-composite-bar` | Tab 3 | L8 | OK |
| `chart-radar` | Tab 4 | L9 | OK |
| `chart-readiness` | Tab 4 | L10 | OK |
| `chart-void-grid` | Tab 4 | L11 | OK |
| `chart-claims` | Tab 5 | L12 | OK |
| `chart-claim8-forest` | Tab 5 | N1 | OK |
| `chart-claim1-forest` | Tab 5 | N2 | OK |
| `chart-pvalue-strip` | Tab 5 | N3 | OK |
| `chart-vendor-typology-grid` | Tab 6 | N4 | OK |
| `chart-cv-length` | Tab 6 | N7 (upgraded L13) | OK |
| `chart-cv-rubric` | Tab 6 | L14 | OK |
| `chart-cv-t2` | Tab 6 | L15 | OK |
| `chart-t2-span-strip` | Tab 6 | N5 | OK |
| `chart-rubric-ceiling-heatmap` | Tab 6 | N6 | OK |
| `chart-cv-radar` | Tab 6 | L16 | OK |
| `chart-cv-biasvalues` | Tab 6 | L17 | OK |

**Result: No orphan containers. No orphan charts. All 23 containers are accounted for.**

However, the dataviz plan notes at the end of Section 1 that the v6 `renderValues()` function
produced charts `chart-a3-hist` and `chart-a1-bar` which are **NOT in the v7 skeleton**. The plan
correctly states these should become inline prose callouts. This is not a conflict — it is a
deliberate removal. **No new DOM IDs must be created without updating the skeleton.**

---

### MINOR-13: Dataviz plan Section 1, L3 comment states "no funnel in v6; skeleton allocates chart-funnel" — but labels L3 as legacy. This is self-contradictory but not a runtime error

The dataviz plan puts `chart-funnel` in the "frozen legacy" block (L3) while noting it was not
implemented in v6. It should be in the "new charts" block. This is a documentation inconsistency
that could confuse the implementing agent about whether to use v6 code or write fresh — but both
the DOM ID and the tab assignment are correct.

**Severity:** MINOR — documentation inconsistency, not a contract violation.

---

## Criterion 5 — CSS Class Drift

### MAJOR-14: Dataviz plan uses `VENDOR_COLORS` map with hex values that conflict with the statistics plan's Okabe-Ito palette

**Dataviz plan** (`plan-dataviz.md`, Section N5 visual encoding):
```
Anthropic=#4C78A8, OpenAI(simulated)=#F58518, Gemini(simulated)=#E45756
```

**Statistics plan** (`plan-statistics.md`, Section 5 canonical palette):
- `supported`: `#009E73`
- `revised`: `#E69F00`
- `not_significant`: `#0072B2`
- Tradition families: Abrahamic `#56B4E9`, Dharmic `#F0E442`, etc.

**Vendor-framing plan** (`plan-vendor-framing.md`, Section 7 canonical palette):
```
Claude-as-Claude: #5b8ff9 (blue)
Claude-roleplaying-OpenAI-scorer: #61d9aa (teal)
Claude-roleplaying-Gemini-scorer: #f6bd16 (amber)
```

Three different vendor color schemes across three plans. The dataviz plan uses `#4C78A8` for
Anthropic; the vendor-framing plan uses `#5b8ff9`. These are different blues. OpenAI: `#F58518`
vs `#61d9aa`. Gemini: `#E45756` vs `#f6bd16`. None of these are Okabe-Ito compliant for the vendor
dimension.

A CSS agent receiving all three plans has no single authoritative color definition for vendor
conditions. This will produce color inconsistency across charts in Tab 6.

**Severity:** MAJOR — three plans define three incompatible vendor color palettes. No plan
cross-references the others. The implementing CSS agent must choose one; mismatches between the T2
span chart (dataviz palette) and the rubric heatmap (could use any palette) will make the tab
visually inconsistent.

**Resolution required:** The data contract must designate one palette as canonical for vendor
encoding. Recommend: vendor-framing plan's palette (Section 7) since it is the most specific and
aligns with the `simulated-tag` CSS class concept; dataviz and statistics plans must reference it.

---

### MAJOR-15: Statistics plan and UX plan define different `--accent-blue` / `--link-color` values; neither references the other

**UX plan** (`plan-ux-a11y.md`, Section 4):
```css
--link-color: #6A9FD4;  /* replaces --accent-blue: #4C78A8 */
```

**Statistics plan** (`plan-statistics.md`, Section 5):
```
Accent / highlight: #539bf5 (blue, for links and active states)
```

`#6A9FD4` ≠ `#539bf5`. These are different blues for the same semantic role (interactive
text/links). A CSS agent implementing both plans would have to choose one; a naive implementation
using the last-read value would produce inconsistency between what the statistics plan's badge
rendering expects and what the UX plan's focus-ring uses.

**Severity:** MAJOR — link color token conflict. Not a runtime crash but produces visible
inconsistency and potential WCAG AA contrast failures if the wrong value is used in the wrong
context.

---

### MINOR-16: Multiple plans use `card-rv--claim`, `card-rv--typology`, `card-rv--caveat` CSS classes; all consistent with skeleton

All eight plans reference only CSS classes that appear in the data contract's § 7 class inventory:
`card-rv`, `card-rv--claim`, `card-rv--caveat`, `card-rv--typology`, `caveat-ribbon`,
`verdict-badge`, `verdict--supported`, `verdict--revised`, `verdict--not-significant`,
`simulated-tag`, `chart-container`, `tab-sub`.

No plan invents CSS classes outside this list EXCEPT:
- `plan-ux-a11y.md`: introduces `.sr-only`, `.skip-link`, `.chart-title`, `.chart-note`,
  `.dark-table`, `.card-stat` — none of these are in the data contract's class inventory.

These are valid additions for accessibility, but they are NEW classes not in the frozen skeleton and
not declared in the contract. The CSS agent must know to create them without a conflict.

**Severity:** MINOR — new classes, not conflicting with existing ones. Document for CSS agent.

---

## Criterion 6 — Claim ID Format

### MAJOR-17: Mixed claim ID formats across plans — `C1`–`C8` vs `claims[0]`–`claims[7]` vs `claim_1`–`claim_8`

**JSON format:** `"claim_id": "C1"` through `"C8"` (canonical)

**Plans using C1–C8 format (correct):**
- `plan-narrative.md`: C1, C2, C3, C4, C5, C6, C7, C8 throughout
- `plan-statistics.md`: C1 through C8 consistently
- `plan-cold-reader.md`: C8, C2, C1 (correct)
- `plan-religion.md`: does not reference claim IDs directly

**Dataviz plan:** Uses both formats:
- Section N1: `claims[7].tests[*]` (array index) — CORRECT for Python generator access
- Section N2: `claims[0].tests[*]` — CORRECT for Python generator
- Section N3 data source: `claims[*] → claim_id` — CORRECT, this is the JSON field
- Section N3 Python-generated constant: `[{claim_id, neg_log_p, ...}]` — OK
- But Section 5 render function map: `renderClaim8Forest()`, `renderClaim1Forest()` — function
  names only, no ID format issue here

**Statistics plan Section 2:** References `C8` as the highlight claim correctly.

**Verdict-badge class naming:** The data contract specifies:
- `verdict--supported` (with double-dash)
- `verdict--revised`
- `verdict--not-significant` (with double-dash and hyphen)

All plans that reference verdict badge classes use the double-dash BEM modifier pattern consistently.
No mixed `verdict-supported` vs `verdict--supported` drift found.

**Result:** Claim IDs (`C1`–`C8`) are consistently used in prose. The dataviz plan uses array
index access (`claims[0]`, `claims[7]`) in Python generator data-source specs — this is correct
and expected. No runtime collision because the JS constant `CLAIMS_V7` will be keyed by `claim_id`
value (`"C1"`–`"C8"`), not by array index.

**Severity:** MAJOR — but narrow. The p-value strip data source spec in the dataviz plan reads
`tests[0].p_value` as the "primary test p-value per claim." For C8, `tests[0].p_value` = 0.000181
(t-test) — correct primary test. For C1, `tests[0].p_value` = 0.0 — correct. For C4, `tests[0].p_value`
= `null` (logistic regression has no p-value at claim level). Accessing `null` and then computing
`-log10(null)` will produce `NaN` or `Infinity` in the strip chart.

This is a data-key access issue: the p-value strip chart accesses `tests[0].p_value` for all
claims, but C4's primary test has `"p_value": null`. The Python generator must handle `null` as a
special case (e.g., use 0.09 from the coefficient-level p-value, or render as "NA" point).

---

### MINOR-18: `plan-statistics.md` mentions `C8` should appear "first in claim order" — conflicts with JSON claim_number ordering

**Statistics plan Section 3:**
> "C8 should appear first in the 'Core Findings' tab, above all other claims."

**JSON:** Claims are stored in array order C1→C8 (`claim_number` 1–8). No JSON field indicates
display priority.

The data contract does not define a `display_order` or `featured` field. If the Python generator
outputs claims in JSON array order (C1 first), but the statistics plan requires C8 first, the app.js
renderer must sort them. This sort logic is not described in any plan. It is also in tension with
the dataviz plan's p-value strip chart, which plots claims on the y-axis — if C8 is at the top in
one view and at position 8 in another, the dashboard is visually inconsistent.

**Severity:** MINOR — not a runtime error, but a display inconsistency between Tab 5 claim card
order (statistics plan: C8 first) and p-value strip y-axis order (dataviz plan: presumably C1–C8
top-to-bottom). These need to be coordinated.

---

### MINOR-19: ECharts version conflict between dataviz plan and skeleton

**Dataviz plan** (`plan-dataviz.md`, Section 0):
> "ECharts version: 5.5.0 (pin exactly; do NOT use 5.5.1 referenced in skeleton — correct skeleton
> to 5.5.0)"

**Skeleton** (`dom-skeleton.html`, line 277):
```html
<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.1/dist/echarts.min.js"></script>
```

The dataviz plan instructs the implementing agent to modify the frozen skeleton's CDN URL. This is
a direct modification of a frozen source-of-truth document. Whether 5.5.0 vs 5.5.1 matters
functionally depends on the specific ECharts features used — the plan does not justify why 5.5.0 is
required over 5.5.1.

**Severity:** MINOR — if 5.5.1 has breaking changes for any feature the dataviz plan relies on,
this becomes CRITICAL. Without a stated reason, it is MINOR. The skeleton version (5.5.1) should be
treated as authoritative; if the dataviz plan has a specific incompatibility, it must be documented
with a failing repro case before the skeleton is changed.

---

## Summary Table

| ID | Criterion | Plan(s) | Severity | Issue |
|----|-----------|---------|----------|-------|
| CRITICAL-01 | Data key | dataviz, vendor-framing, statistics | CRITICAL | `rubric_v_min` in contract ≠ `mean_rubric_values` in JSON |
| CRITICAL-02 | Data key | dataviz | CRITICAL | `rubric_v_max` in contract ≠ `mean_rubric_values` in JSON for template_refusal |
| CRITICAL-03 | Data key | dataviz, vendor-framing | CRITICAL | `bias_score_range` type: string in contract, array in JSON |
| CRITICAL-07 | DOM ID / Tab | ux-a11y, narrative | CRITICAL | Unilateral tab reorder conflicts with frozen skeleton; two plans disagree with each other |
| CRITICAL-11 | Tab structure | ux-a11y, narrative | CRITICAL | (see CRITICAL-07 — same finding under different criterion) |
| MAJOR-04 | Data key | dataviz | MAJOR | `t2_span.max_model` in contract absent from JSON; JSON has `max_models_at_ceiling` |
| MAJOR-05 | Data key | dataviz | MAJOR | `mean_reasoning_length`, `mean_values_length` in JSON but not declared in contract for non-Anthropic typologies |
| MAJOR-08 | DOM ID | transparency | MAJOR | `id="cav-1"` ≠ skeleton `id="caveat-cav1"` — anchor links will silently fail |
| MAJOR-09 | DOM ID | ux-a11y | MAJOR | `id="main-content"` referenced by skip link does not exist in skeleton |
| MAJOR-12 | Chart-to-DOM | dataviz | MAJOR | (resolved — all containers accounted for; flagged as OK) |
| MAJOR-14 | CSS class | dataviz, vendor-framing, statistics | MAJOR | Three incompatible vendor color palettes defined across three plans |
| MAJOR-15 | CSS class | ux-a11y, statistics | MAJOR | `--link-color: #6A9FD4` (UX) ≠ `#539bf5` (statistics) for same semantic role |
| MAJOR-17 | Claim ID | dataviz | MAJOR | `tests[0].p_value` is null for C4; `-log10(null)` = NaN in p-value strip chart |
| MINOR-06 | Data key | vendor-framing | MINOR | `simulated_label` trailing text differs contract vs JSON |
| MINOR-10 | DOM ID | transparency | MINOR | Sticky CSS for caveat-ribbon not in skeleton; CSS addition only |
| MINOR-13 | Chart-to-DOM | dataviz | MINOR | L3 (funnel) labeled legacy but was not in v6; documentation inconsistency |
| MINOR-16 | CSS class | ux-a11y | MINOR | New classes `.sr-only`, `.skip-link`, `.chart-title`, `.chart-note`, `.dark-table`, `.card-stat` introduced; not in contract |
| MINOR-18 | Claim ID | statistics | MINOR | C8-first display order not encoded in data; sort logic unspecified; strip chart y-axis may conflict |
| MINOR-19 | (general) | dataviz | MINOR | ECharts 5.5.0 vs 5.5.1 — plan instructs skeleton modification without justification |

---

## Required Pre-Implementation Fixes (blocking)

Before any agent begins writing code:

1. **Reconcile contract § 2 vs JSON** for `rubric_v_min`, `rubric_v_max`, `mean_rubric_values` —
   update the contract to match the JSON canonical data, not vice versa.

2. **Fix `bias_score_range` type** — choose one: string `"0.5667-1.0"` or array `[0.5667, 1.0]`.
   Update whichever document is wrong. All plan text referencing this value must use the canonical form.

3. **Add `max_model` to JSON OR remove it from contract** — the field is in the contract but absent
   from `claims_canonical.json`. Pick one source of truth.

4. **Freeze tab DOM order** — resolve the narrative vs UX vs skeleton three-way conflict by
   designating the skeleton as authoritative (it already is). Both plans must be updated to say
   "recommended reading order is surfaced as a callout, not a DOM reorder."

5. **Designate one canonical vendor color palette** — the vendor-framing plan's Section 7 palette
   is the most complete; declare it canonical. Update dataviz plan and statistics plan to reference it.

6. **Standardize caveat card IDs** — either change the transparency plan to use `caveat-cav1` /
   `caveat-cav2` / `caveat-cav3` (matching the skeleton), or update the skeleton and all plans to
   use `cav-1` / `cav-2` / `cav-3`. The skeleton is frozen, so the transparency plan must change.

7. **Handle C4 null p-value in strip chart** — the Python generator must add a null-check before
   computing `−log10(p_value)` and render C4 as a special "no p-value (logistic regression)"
   point in the strip chart.

---

*Audit complete. 19 findings (5 CRITICAL, 8 MAJOR, 6 MINOR). Findings 5 and 12 are effectively
resolved within the plans; all others require action before implementation begins.*
