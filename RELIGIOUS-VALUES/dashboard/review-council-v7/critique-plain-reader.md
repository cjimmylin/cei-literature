# Plain-Reader Critic Audit — Dashboard v7 Plans
**Auditor role:** Plain-Reader Critic (no paper knowledge assumed)
**Date:** 2026-04-13
**Files reviewed:** plan-narrative.md, plan-statistics.md, plan-dataviz.md, plan-ux-a11y.md, plan-transparency.md, plan-religion.md, plan-vendor-framing.md, plan-cold-reader.md, claims_canonical.json
**Method:** Read each plan as a first-time reader who has NOT read the paper; flag every term, assumption, or structural choice that would strand or mislead such a reader.

---

## 1. Jargon Creep

### 1.1 K / R / V (Knowledge / Reasoning / Values)

| Plan | Usage | Gloss provided? |
|------|-------|-----------------|
| plan-narrative.md | "Knowledge (K), Reasoning (R), and Values (V) items" | YES — full form given on first use in Tab 6 description |
| plan-statistics.md | "K<R<V gradient", "K/R/V rubrics", table labels | PARTIAL — referenced but not introduced systematically; appears without gloss in Section 1 table before any definition |
| plan-dataviz.md | x-axis label `["K", "R", "V"]`, chart ID `chart-cv-length`, title "K < R < V Response Length Gradient" | NO — chart title uses bare letters; alt text uses bare K/R/V without a legend box requirement |
| plan-ux-a11y.md | Section 1 recommended tab order, Section 7 alt text templates | NOT MENTIONED — plan does not mandate a K/R/V legend on the chart |
| plan-vendor-framing.md | "K < R < V gradient holds", "0.0 on K/R/V rubrics" | NO — single letters used as if self-explanatory |
| plan-cold-reader.md | FM-1 explicitly flags this; requires "visible legend box on the chart" | YES — correctly identifies the risk |

**Finding:** plan-cold-reader.md correctly identifies K/R/V as FM-1 (jargon creep), but plan-dataviz.md and plan-vendor-framing.md do not carry a corresponding requirement to gloss these labels. plan-statistics.md uses K/R/V in the effect-size table (Section 1) before any definition in that document. A dashboard built from these plans could satisfy each plan individually without ever showing a persistent K/R/V legend.

**Severity: CRITICAL**
**Fix:** Add an explicit legend requirement to plan-dataviz.md Section 2 N7 spec and plan-vendor-framing.md Section 4: "Every chart whose x-axis or legend uses K, R, or V as standalone letters MUST display a visible on-chart legend box (not tooltip-only): K = Knowledge, R = Reasoning, V = Values."

---

### 1.2 T1 / T2

| Plan | Usage | Gloss provided? |
|------|-------|-----------------|
| plan-narrative.md | "A 30-item Arabic multiple-choice test of Islamic inheritance law (fara'id, labeled T2)" | YES — full gloss on first use in Tab 6 |
| plan-statistics.md | "T2 Arabic MCQ" in effect size table header | PARTIAL — abbreviation used without inline gloss; depends on reader having seen Tab 6 narrative |
| plan-dataviz.md | "T2 bar" (chart title), "T2 Arabic MCQ Accuracy — 93.3 pp Span", alt text | PARTIAL — "Arabic MCQ" is given but "T2" is not spelled out; "T1" is never glossed in this plan |
| plan-transparency.md | "T2 blinding asymmetry" in CAV-1, "T2 Arabic MCQ trials", "T1" never mentioned | PARTIAL for T2; T1 completely absent |
| plan-vendor-framing.md | "T2 (fara'id Arabic MCQ)" with inline parenthetical | YES for T2; T1 never appears |
| plan-religion.md | "T2 instrument is a 30-item Arabic multiple-choice quiz covering fara'id" | YES for T2; T1 never appears |
| plan-cold-reader.md | FM-5 requires T1 to be glossed: "T1 (65-item construct validity battery: Knowledge, Reasoning, Values, Bias items)" | YES — identifies T1 gloss as required |

**Finding:** T2 is reasonably glossed across most plans but T1 is glossed ONLY in plan-cold-reader.md's FM-5. plan-dataviz.md references the "65-item construct validity battery" in plan-narrative.md prose but never assigns the T1 label in any chart spec or requirement. If the dashboard implements T1-labeled charts (plausible given the battery is mentioned throughout), T1 will appear unglossed.

**Severity: MAJOR**
**Fix:** Add to plan-dataviz.md Section 2 and plan-vendor-framing.md Section 6: "T1 must be glossed on first appearance as 'T1 (65-item construct validity battery: Knowledge, Reasoning, Values, and Bias items)'. T2 must be glossed as 'T2 (30-item Arabic MCQ on Islamic inheritance law / fara'id)'."

---

### 1.3 fara'id

| Plan | Usage | Gloss provided? |
|------|-------|-----------------|
| plan-narrative.md | "Islamic inheritance law (fara'id, labeled T2)" | YES — parenthetical on first use |
| plan-dataviz.md | chart title "T2 Arabic MCQ Accuracy — 93.3 pp Span (6.7%→100%)" | NO — fara'id does not appear in any chart spec |
| plan-vendor-framing.md | "T2 (fara'id Arabic MCQ)" | YES — parenthetical |
| plan-religion.md | Full section (Section 4) defining fara'id | YES — most thorough treatment |
| plan-transparency.md | "30-item Arabic MCQ (fara'id)" in footer text | YES — parenthetical |
| plan-cold-reader.md | FM-5 requires gloss in dashboard | YES |

**Finding:** fara'id is handled well in prose plans but plan-dataviz.md's chart title specifications never include the gloss. A chart titled "T2 Arabic MCQ Accuracy" without "fara'id" in the visible chart header is technically compliant with plan-dataviz.md while violating plan-cold-reader.md FM-5. The two plans are inconsistent.

**Severity: MAJOR**
**Fix:** plan-dataviz.md N5 chart title should read: "T2 (fara'id — Islamic Inheritance Law) Arabic MCQ Accuracy — 93.3 pp Span". Update the N5 spec to require the gloss in the chart title, not only in tooltips.

---

### 1.4 Bootstrap CI / bootstrap resampling

| Plan | Usage | Gloss provided? |
|------|-------|-----------------|
| plan-narrative.md | "bootstrap resampling: the composite scores were recomputed 1,000 times" | YES — explained in Tab 2 description |
| plan-statistics.md | "bootstrap CIs on the median year: [2023, 2024]" | PARTIAL — no re-explanation; relies on Tab 2 narrative |
| plan-transparency.md | "1,000 bootstrap iterations" in footer | NO gloss — assumes reader knows the term |
| plan-ux-a11y.md | No mention | N/A |

**Finding:** plan-transparency.md's Methods Disclosure Footer uses "bootstrap iterations" without a gloss, violating the spirit of a general-audience document. A policy analyst or journalist may not know what bootstrapping is.

**Severity: MINOR**
**Fix:** Add one parenthetical in the footer: "1,000 bootstrap iterations (re-running the analysis on random subsamples of the data to test stability)."

---

### 1.5 Cohen's d

| Plan | Usage | Gloss provided? |
|------|-------|-----------------|
| plan-statistics.md | Full Section 6 with plain-English benchmarks and intuitive translation | YES — excellent treatment |
| plan-narrative.md | "a large effect (Cohen's d = -1.23)" in Tab 5 | YES — "large effect" label accompanies it |
| plan-cold-reader.md | Q2 scoring uses "d = -1.23" as a crediting criterion | PARTIAL — cold reader expected to recognize this notation without dashboard explaining it |
| plan-dataviz.md | alt text: "d=−1.23 (p<0.001)" | NO gloss in alt text |

**Finding:** plan-statistics.md provides excellent Cohen's d guidance, but plan-cold-reader.md Q2 awards full credit to a cold reader who cites "d = -1.23" — a notation a non-researcher may not recognize. The Q2 scoring rubric says "at least one concrete number" and lists d = -1.23 as an acceptable answer. A reader who says "30 out of 100" should score full credit; the notation requirement is fine for researchers but the rubric should not privilege it over the plain-English number.

**Severity: MINOR**
**Fix:** Q2 full-credit rubric: ensure "30/100" or "30 out of 100" alone qualifies for full credit, not just "d = -1.23". The existing rubric does allow this, but the phrasing should be made explicit: "Any ONE of: 30/100 mean score, 3/16 above midpoint, d = -1.23, p < 0.001."

---

### 1.6 Cramer's V

| Plan | Usage | Gloss provided? |
|------|-------|-----------------|
| plan-statistics.md | Full Section 6 benchmarks; plain tooltip text | YES |
| plan-dataviz.md | "Cramer's V CIs" in N2 forest plot spec | NO gloss in spec itself |
| plan-narrative.md | Not explicitly named | N/A |

**Finding:** plan-dataviz.md uses "Cramer's V" in the N2 forest plot specification without a required tooltip or label annotation. If the forest plot axis is labeled "Cramer's V" without a tooltip explanation, a non-statistician reader will not understand what they are looking at.

**Severity: MINOR**
**Fix:** Add to N2 spec: "The x-axis label for the C1 forest plot must read 'Effect size (Cramer's V — measures distribution unevenness; 0 = uniform, 1 = complete concentration)' or include a persistent legend note to that effect."

---

### 1.7 Bonferroni correction

| Plan | Usage | Gloss provided? |
|------|-------|-----------------|
| plan-dataviz.md | N3 p-value strip: "Bonferroni-corrected threshold line at x=−log₁₀(0.05/8) ≈ 2.204 (dotted)" | NO gloss |
| plan-transparency.md | "Bonferroni-corrected α = 0.00625" in footer | NO gloss |
| plan-statistics.md | Not mentioned by name | N/A (only "8 simultaneous tests" implied) |
| plan-cold-reader.md | Not tested in Q1-Q5 | N/A |

**Finding:** The Bonferroni correction appears in the p-value strip chart and the Methods footer without explanation. A journalist or ethicist will not understand why there are two threshold lines on the strip chart unless the labels explain the concept.

**Severity: MAJOR**
**Fix:** The p-value strip chart must include a visible annotation or legend entry: "Dashed line: p < 0.05 (conventional threshold). Dotted line: p < 0.006 (Bonferroni correction for testing 8 claims simultaneously — reduces false-alarm risk)." The same explanation should appear as a parenthetical in the footer: "Bonferroni-corrected α = 0.00625 (conventional 0.05 divided by 8 tests — a stricter threshold that accounts for testing multiple claims)."

---

### 1.8 WEIRD

| Plan | Usage | Gloss provided? |
|------|-------|-----------------|
| plan-religion.md | Full Section 6: "WEIRD stands for: Western, Educated, Industrialized, Rich, Democratic" | YES — thorough |
| plan-statistics.md | "WEIRD bias" in C6 block; "WEIRD-origin benchmarks" | NO inline gloss; assumes reader has seen plan-religion.md |
| plan-narrative.md | "WEIRD bias (C6)" label | NO inline gloss in Tab 5 description |
| plan-cold-reader.md | Not tested | N/A |

**Finding:** plan-statistics.md and plan-narrative.md use WEIRD as an acronym without a gloss. A reader who first encounters the dashboard on Tab 5 (Claims) before reading the Tradition Coverage section will see "WEIRD bias" without an explanation.

**Severity: MAJOR**
**Fix:** plan-statistics.md Section 4 (C6) must require an inline gloss: first use of WEIRD in claim card text must expand to "WEIRD (Western, Educated, Industrialized, Rich, Democratic) contexts". plan-narrative.md Tab 5 should include the same.

---

### 1.9 void factor / gate-passer / meta-evaluation

| Plan | Usage | Gloss provided? |
|------|-------|-----------------|
| plan-religion.md | "void factors" as Section 2 header | PARTIAL — explained immediately in that section's body |
| plan-narrative.md | "gate-passers" used repeatedly | PARTIAL — Tab 1 explains "47 candidates passed all filters" but does not use "gate-passer" label there; the term appears without definition in later tabs |
| plan-cold-reader.md | Q1 tests whether reader understands "meta-evaluation" frame | FM-1 flags "meta-evaluation" as a risk term |
| plan-statistics.md | "gate-passer" used 3× in C3 and C1 blocks | NO inline gloss |
| plan-dataviz.md | "gate-passers" in funnel chart description | NO inline gloss |
| plan-transparency.md | "47 benchmarks passed both gates" | YES — "passed both gates" is clear |

**Finding 1:** "gate-passer" is used as if it were a technical label across all plans but is only clearly defined in plan-narrative.md Tab 1 prose. plan-statistics.md introduces it in C3 without definition.

**Finding 2:** "meta-evaluation" appears in plan-cold-reader.md as the research framing that a reader might miss. None of the implementation plans (narrative, dataviz, UX) contain an explicit requirement to render a hero-level statement using "meta-evaluation" with a gloss. The cold-reader plan correctly identifies this risk but does not ensure the other plans prevent it.

**Severity: MAJOR (gate-passer), CRITICAL (meta-evaluation)**
**Fix (gate-passer):** Add to plan-dataviz.md Section 2 (funnel chart spec): "The funnel chart labels must include a parenthetical definition: 'gate-passers = benchmarks meeting minimum theological depth AND public data availability thresholds'."
**Fix (meta-evaluation):** plan-narrative.md Tab 1 must require a hero subtitle: "This is a meta-evaluation — a study that evaluates existing benchmarks rather than creating new ones." This sentence must appear in the first visible panel before any chart.

---

### 1.10 "pp" (percentage points)

| Plan | Usage | Gloss provided? |
|------|-------|-----------------|
| plan-dataviz.md | "93.3 pp Span" in chart title | NO |
| plan-vendor-framing.md | "a 93.3 pp range" in Section 6 | NO |

**Severity: MINOR**
**Fix:** Replace "pp" with "percentage-point" in all chart titles and annotations. "93.3 percentage-point span" takes 3 extra syllables and removes all ambiguity.

---

## 2. Assumed Context

### 2.1 "The 8 claims"

All implementation plans reference "8 claims" or "Claim 8" without ensuring the dashboard enumerates all 8 claims for a first-time reader.

| Plan | Treatment |
|------|-----------|
| plan-narrative.md | Tab 5 references "eight pre-registered empirical claims" and lists test types but does not require an index table |
| plan-statistics.md | Section 3 positions C8 first but assumes reader knows the full claim set |
| plan-dataviz.md | N3 p-value strip shows all 8 claims by ID ("C1"–"C8") with tooltip; claim titles in tooltip only |
| plan-cold-reader.md | FM-2 requires a "claims index table" visible without scrolling past the main finding |

**Finding:** plan-cold-reader.md correctly requires a claims index table, but no implementation plan mandates one. plan-dataviz.md N3 puts claim titles in tooltips only — which is invisible to the cold reader if they must hover to see titles. A reader landing on Tab 5 and seeing "C1 through C8" in a strip chart cannot know what any of those claims are without hovering.

**Severity: CRITICAL**
**Fix:** plan-dataviz.md Tab 5 section must require a static claims index table (Claim # | Title | Verdict) rendered as visible HTML above the p-value strip chart. Claim titles must NOT be tooltip-only.

---

### 2.2 "The 47 gate-passers" vs. "the 401 candidates"

plan-narrative.md explains the 401→47 funnel in Tab 1, but plan-statistics.md C3 opens with "170 of 401 candidates have unavailable data" and C1 opens with "28 of 47 gate-passers" without re-anchoring these numbers for a reader who lands directly on Tab 5.

**Severity: MAJOR**
**Fix:** Tab 5 claims section should include a two-sentence context header: "This study began with 401 candidate benchmarks. 47 passed all quality gates and are the basis for the claims below." This recaps Tab 1 for readers who jump directly to Claims.

---

### 2.3 "The 3-tier ranking" / Tier 1 / Tier 2 / Tier 3

| Plan | Treatment |
|------|-----------|
| plan-narrative.md | Tab 3 defines tiers in prose |
| plan-transparency.md | Section 5e defines tiers with score thresholds |
| plan-dataviz.md | References tier-table and composite-bar chart without specifying that tier boundaries must be visible on chart |
| plan-religion.md | "Islam-focused benchmarks occupy 9 of the 12 Tier 1 positions" — no gloss |
| plan-statistics.md | "9 of 12 Tier 1 benchmarks" in C1 plain_english — no inline gloss |

**Finding:** plan-religion.md and plan-statistics.md use "Tier 1" as a bare label assuming the reader knows it means "composite score ≥ 52.0 among the top 12." The tier score thresholds are only defined in plan-transparency.md Section 5e, which is a collapsible "How to read" block that may be closed by default on return visits.

**Severity: MAJOR**
**Fix:** Wherever "Tier 1" or "9 of 12 Tier 1 benchmarks" appears in claim cards or annotation text, add a parenthetical: "(Tier 1 = composite score ≥ 52.0, top 12 of 47 benchmarks)". Do not rely on the reader having expanded the "How to read" section.

---

### 2.4 "A3 scoring" (values relevance score)

The claims_canonical.json C8 data references "mean A3 = 30.0" and "mean_a3" as the values relevance score. plan-statistics.md Section 3 uses "A3 values relevance score". plan-transparency.md Section 3 references "A3 values relevance scoring." plan-dataviz.md references "chart-a3-hist" in a legacy note.

**Finding:** "A3" is an internal axis identifier (likely "Axis 3" of the scoring framework) that never gets defined for the general reader. The cold-reader questions (Q2) test whether the reader understands the values relevance finding, but the dashboard may render "mean A3 = 30.0" without explaining what "A3" means.

**Severity: CRITICAL**
**Fix:** The A3 identifier must never appear in rendered dashboard text. Replace all instances of "A3" in chart labels, claim card text, and annotations with "values relevance score (0–100)". The score axis on any chart must be labeled "Values Relevance Score (0 = tests only factual recall, 100 = fully tests values reasoning)."

---

### 2.5 Corpus of 2,043 AI ethics papers

plan-transparency.md footer mentions "2,099 AI ethics papers" as the source corpus. plan-dataviz.md and plan-narrative.md do not reference this number. The CLAUDE.md system context says there are 2,043 papers. This is a minor inconsistency (database may have grown) but a reader seeing "2,099" in the footer and "2,043" elsewhere would be confused.

**Severity: MINOR**
**Fix:** Verify the correct corpus count and use a single number across all plans and the dashboard. Use the number current at generation time, not a hardcoded figure.

---

## 3. Buried Lede — Claim 8 Positioning

### 3.1 In plan-narrative.md

plan-narrative.md recommends reading order: Overview → Tradition Coverage → Ranking → Landscape → **Claims** → Simulated Scorer Study. Claim 8 appears in Tab 5 (Claims), which is the fifth tab in the recommended reading order. A reader who follows this path encounters C8 only after reading four other tabs.

plan-statistics.md Section 3 correctly states: "C8 should appear FIRST in the 'Core Findings' tab, above all other claims." plan-narrative.md Tab 5 description also correctly identifies C8 as "the strongest finding" and introduces it prominently within Tab 5. However, neither plan requires C8 to appear in the hero section of Tab 1 (Overview), meaning a reader who stops after Tab 1 will not know about the values relevance failure.

**Finding:** plan-cold-reader.md FM-3 requires C8 to be "in the hero section or first visible panel." plan-narrative.md Tab 1 does NOT include C8. The gap between FM-3 requirements and Tab 1 implementation guidance is unbridged.

**Severity: CRITICAL**
**Fix:** plan-narrative.md Tab 1 (Overview) must add: "Include a prominent stat card in the first viewport: 'Mean values relevance: 30/100 — most benchmarks do not test religious values (d=−1.23, p<0.001).' This card positions C8 as the primary finding before the reader encounters the 401→47 funnel or tradition distribution." This aligns with plan-cold-reader.md FM-3 Minimum fix.

---

### 3.2 In plan-dataviz.md

plan-dataviz.md Tab allocation (Section 3) places C8 in Tab 5 with three new charts (N1–N3). No chart is specified for Tab 1 that carries the C8 finding. The funnel, tradition bar, and family pie on Tab 1 tell the coverage story, not the validity story.

**Finding:** The dataviz plan does not implement the hero stat card for C8 that plan-cold-reader.md FM-3 requires. FM-3's "minimum fix" is a hero stat card reading "Mean values relevance: 30/100 — most benchmarks do not test religious values." This card is described nowhere in plan-dataviz.md.

**Severity: CRITICAL**
**Fix:** Add to plan-dataviz.md Tab 1 chart list: a `.card-stat` hero element (not an ECharts chart) displaying the C8 headline with the text required by FM-3. This must be the first visible element below the dashboard title/subtitle, above the funnel chart.

---

### 3.3 In plan-statistics.md

plan-statistics.md correctly places C8 first in Tab 5 and dedicates a "three-way convergence box" to it. However, the linking annotation between C8 and Tab 1 is not specified. The plan describes C8's position within Tab 5 well but does not require any C8 content to bleed into earlier tabs.

**Severity: MAJOR**
**Fix:** plan-statistics.md should add a note: "In addition to its Tab 5 placement, a summary stat from C8 must appear in Tab 1's hero section per plan-cold-reader.md FM-3. The Tab 5 three-way convergence box is the deep treatment; Tab 1 hero card is the first-look hook."

---

### 3.4 In plan-ux-a11y.md

plan-ux-a11y.md proposes a reading order (Section 1) of: Overview → **Ranking** → Tradition Coverage → Claims → Landscape → Simulated. This puts Claims (Tab 5, where C8 lives) fourth. It does NOT recommend a C8 hero card in Tab 1. plan-ux-a11y.md is also in direct conflict with plan-narrative.md on reading order (see Section 5 below on cross-plan consistency).

**Severity: MAJOR (reading order conflict compounds the buried lede problem)**

---

## 4. Acronym Soup

### 4.1 Simultaneous unexplained abbreviations

On Tab 5 (Claims & Robustness) as currently planned, a reader could simultaneously see:
- C1 through C8 (claim IDs — never spelled out on chart)
- K/R/V (rubric dimensions — legend required but not universally mandated)
- T1, T2 (battery labels — T1 unglossed in most plans)
- pp (percentage points — used in dataviz plan)
- CI (confidence interval — used in statistics plan without first-use gloss)
- OR (odds ratio — used in statistics plan Section 4)
- WEIRD (Section 4 of statistics plan, no inline gloss)
- RD / PE / CI (three scoring axis abbreviations in plan-transparency.md footer: "Religious/Theological Depth (RD), Practical Ease (PE), Citation Impact (CI)")

That is 9+ abbreviations potentially visible on one tab. plan-cold-reader.md's FM-1 tests for >3 unexplained abbreviations simultaneously.

**Severity: CRITICAL**
**Fix:** A "Glossary pill" or persistent expandable legend must be available on Tab 5. Required minimum glossary entries: C1–C8 (with claim titles), K/R/V, T1, T2, CI, pp, WEIRD, RD/PE/CI. This glossary is referenced in no implementation plan.

### 4.2 "RD / PE / CI" scoring axes

plan-transparency.md footer and plan-transparency.md Section 5e use "RD," "PE," and "CI" as scoring axis abbreviations. The coincidence of "CI" meaning both "Confidence Interval" and "Citation Impact" in the same document is a genuine ambiguity — a reader who has encountered "95% CI" in statistics will misread "0.15·CI" in the composite formula.

**Severity: MAJOR**
**Fix:** Rename "CI" (Citation Impact) to "Impact" or "CIT" in all rendered dashboard text to avoid the confidence interval collision. The formula becomes: "Composite = 0.50·RD + 0.35·PE + 0.15·Impact."

---

## 5. Consistency Across Plans

### 5.1 Tab reading order conflict

| Plan | Recommended tab order |
|------|-----------------------|
| plan-narrative.md | Overview → Tradition → Ranking → Landscape → Claims → Simulated |
| plan-ux-a11y.md | Overview → Ranking → Tradition → Claims → Landscape → Simulated |

These two plans disagree on whether Ranking (Tab 3) or Tradition Coverage (Tab 4) is visited second, and whether Landscape (Tab 2) is fourth or fifth. An implementing agent following plan-ux-a11y.md would reorder the tab `<li>` sequence differently from what plan-narrative.md describes.

plan-ux-a11y.md explicitly states: "The tab labels should remain in DOM order for code stability, but the visual left-to-right tab sequence must be reordered in the `<ul class='nav nav-tabs'>`" — with order: `nav-overview | nav-ranking | nav-traditions | nav-claims | nav-landscape | nav-crossvendor`.

plan-narrative.md says: "The default tab displayed on load should remain Tab 1 (Overview), which is the natural entry point. Tab navigation labels should remain in their DOM order (1-6) so that a reader who simply clicks through left to right encounters the tabs in a reasonable if not optimal sequence."

plan-narrative.md recommends a reading order tooltip, not a DOM reorder. plan-ux-a11y.md recommends a DOM reorder. These are directly conflicting instructions.

**Severity: CRITICAL**
**Fix:** Resolve the conflict explicitly in a single authoritative decision: either reorder the DOM tabs (plan-ux-a11y.md approach) or keep DOM order and add a reading guidance tooltip (plan-narrative.md approach). Cannot implement both. Recommendation: accept plan-ux-a11y.md's DOM reorder, which produces a left-to-right path that presents the most important finding (C8, in Claims) earlier in the sequence. Update plan-narrative.md to state: "Tab visual order follows plan-ux-a11y.md specification."

---

### 5.2 Claim 8 positioning within Tab 5

| Plan | C8 position in claims section |
|------|-----------------------------|
| plan-statistics.md | C8 first, above all other claims, with special "three-way convergence box" layout |
| plan-narrative.md | "The strongest finding is values relevance failure (C8)" — in prose, not a structural position requirement |
| plan-dataviz.md | C8 forest plot (N1) listed first in Tab 5 chart sequence; N3 strip plot shows all 8 |
| plan-cold-reader.md | FM-3: C8 must be in first visible panel |

**Finding:** All four plans agree C8 should be prominent in Tab 5. The requirement is structurally consistent across plans. No conflict found here.

---

### 5.3 Verdict color coding

| Plan | "not significant" color |
|------|------------------------|
| plan-statistics.md | `#0072B2` (Okabe-Ito blue) — deliberately NOT grey or red |
| plan-dataviz.md | N3 p-value strip: `#8b949e` (grey) for "not_significant" |

These two plans assign different colors to the "not significant" verdict. plan-statistics.md explicitly argues for blue over grey; plan-dataviz.md uses grey. An implementing agent cannot satisfy both simultaneously.

**Severity: CRITICAL**
**Fix:** Resolve explicitly. plan-statistics.md's argument (blue = "informative null") is stronger and should prevail. Update plan-dataviz.md N3 to use `#58A6FF` (lighter blue variant appropriate for dark backgrounds) for not_significant points, consistent with plan-statistics.md palette. Delete the `#8b949e` entry from N3 spec.

---

### 5.4 Tradition romanization — cross-plan term consistency

| Term | plan-religion.md | plan-statistics.md | claims_canonical.json |
|------|-----------------|-------------------|----------------------|
| Islamic inheritance law | "fara'id" (ASCII apostrophe) | "fara'id" | "fara'id" |
| Goodness-of-fit test | not mentioned | "chi-squared goodness-of-fit" | "Chi-squared goodness-of-fit" |

plan-religion.md mandates ASCII straight apostrophes throughout. No other plan mentions this constraint. An implementing agent writing HTML may inadvertently use curly apostrophes (Unicode 2019) in rendered text, causing the filename/encoding mismatch bug documented in MEMORY.md.

**Severity: MAJOR**
**Fix:** Add a romanization encoding note to plan-dataviz.md and plan-vendor-framing.md: "All apostrophes in fara'id, shari'a, and similar terms must be straight ASCII apostrophes (Unicode 0027, not 2019). Verify with a lint step before deploy."

---

### 5.5 "8 of 14 traditions" — zero-coverage enumeration

| Plan | Lists all 8 zero-coverage traditions? |
|------|--------------------------------------|
| plan-narrative.md | YES — Tab 4 lists: "Judaism, Jainism, Taoism, Shinto, Ubuntu Philosophy, Indigenous Spirituality, Baha'i, and Zoroastrianism" |
| plan-religion.md | YES — tradition table lists VOID status for all 8 |
| plan-dataviz.md | chart-void-grid exists but spec does not require the 8 names to appear as static text (only in visual grid) |
| plan-cold-reader.md | Q5 requires reader to name ≥ 3 of the 8 traditions |

**Finding:** plan-cold-reader.md Q5 requires the dashboard to enumerate all 8 traditions explicitly so a reader can name them. plan-dataviz.md's chart-void-grid may display them visually (as grid cells) but does not specify that text labels must be readable without hovering. If tradition names are in tooltips only, Q5 partial credit becomes the ceiling.

**Severity: MAJOR**
**Fix:** Add to plan-dataviz.md L11 (chart-void-grid) spec: "Tradition names must appear as visible text labels on the void grid, not tooltip-only. The eight VOID traditions must be readable without any hover interaction."

---

### 5.6 Simulation disclosure label consistency

| Plan | Preferred label for simulated OpenAI |
|------|-------------------------------------|
| plan-vendor-framing.md | `Claude-roleplaying-OpenAI-scorer` (chart label); `Sim: OpenAI-scorer` (short form) |
| plan-dataviz.md N4 typology grid | `Simulated: Claude-roleplaying-OpenAI-scorer (Codex, Codex-Mini)` |
| claims_canonical.json | `Claude-roleplaying-OpenAI-scorer (Codex, Codex-Mini simulated by Sonnet/Haiku)` |
| plan-narrative.md Tab 6 | "labeled throughout the dashboard as 'Claude-simulated (Sonnet/Haiku roleplay)'" |

Four different label strings for the same concept. An implementing agent will pick one, potentially violating another plan's requirement.

**Severity: MAJOR**
**Fix:** Designate plan-vendor-framing.md Section 2 as the canonical authority on all label strings. All other plans should defer to it. The canonical short form for axis labels is `Sim: OpenAI-scorer`. The long form for prose is `Claude-roleplaying-OpenAI-scorer`. plan-narrative.md's phrase "Claude-simulated (Sonnet/Haiku roleplay)" should only appear in the how-to-read section or tooltips, not in chart labels.

---

## 6. Cold-Reader Rubric Validation

### 6.1 Q1 — Is the research question answerable from the dashboard alone?

**Assessment:** CONDITIONALLY FAIR. The question is answerable IF the hero section contains "meta-evaluation" with a plain-English gloss AND the dashboard subtitle frames the study as evaluating existing benchmarks rather than creating new ones. As written, no implementation plan guarantees this subtitle exists. plan-cold-reader.md FM-1 identifies the risk, but plan-narrative.md Tab 1 does not mandate the required hero subtitle text.

**Risk:** A reader landing on Tab 1 sees "401 → 47 screening" and a tradition bar chart and a funnel. They may conclude this is a benchmark-creation paper, not a meta-evaluation paper. Q1 would score 0.0.

**Remediation required:** Yes — the Q1 remediation text must be written into plan-narrative.md Tab 1 as a mandatory hero subtitle.

---

### 6.2 Q2 — Is the most important finding identifiable?

**Assessment:** FAIR in intent but DEPENDS ON IMPLEMENTATION. plan-statistics.md and plan-cold-reader.md agree C8 should be first. But as noted in Section 3 above, no implementation plan currently guarantees C8 appears in Tab 1's first viewport. If a reader's first viewport shows only the funnel and tradition charts, Q2 scores 0.0.

**Risk:** High. This is the buried-lede failure mode explicitly identified as FM-3.

**Remediation required:** Yes — mandatory C8 hero stat card in Tab 1 (see Section 3.1 fix above).

---

### 6.3 Q3 — Is data provenance (simulation) answerable?

**Assessment:** FAIR. plan-transparency.md and plan-vendor-framing.md both mandate prominent, persistent disclosure. plan-cold-reader.md Q3 hard-fail condition is appropriate — readers who believe Gemini/OpenAI results are real will misreport the study. The plans collectively address this well.

**Caveat:** plan-ux-a11y.md's mobile-responsive design collapses the caveat ribbon into a single `<details>` accordion on xs/sm screens. On mobile, the ribbon starts collapsed. If a reader first loads on mobile, the hard-fail disclosure may require one tap to reveal. This conflicts with plan-cold-reader.md's requirement that the disclosure be "persistent" and "visible without any interaction."

**Severity: MAJOR**
**Fix:** plan-ux-a11y.md mobile caveat accordion should start EXPANDED on first load (not collapsed), consistent with plan-transparency.md's "Expanded on first page load" requirement. The collapsed state is only for return visits.

---

### 6.4 Q4 — Are caveats findable without paper knowledge?

**Assessment:** PARTIALLY FAIR. The three caveats are well-specified in plan-transparency.md. However, Q4's expected answer for "T2 blinding asymmetry" requires the reader to understand what "T2" is. If the reader has not encountered the T2 gloss yet (it lives in Tab 6, late in reading order), they cannot articulate "the answers were not hidden for Claude." The caveat ribbon labels the card "T2 Blinding Asymmetry" — which requires knowing T2 is a test.

**Risk:** A reader who has only seen Tab 1 and Tab 2 encounters "T2 Blinding Asymmetry" in the ribbon without having seen the T2 instrument. They cannot articulate the caveat with specificity. Q4 scores 0.5 (partial) instead of 1.0.

**Severity: MAJOR**
**Fix:** The caveat ribbon's CAV-1 short text must be self-contained: "The original accuracy tests for Claude models had correct answers visible in the input; cross-vendor tests were blind. Claude's perfect scores (100%) are upper-bound estimates." Remove "T2" from the short text — it means nothing to a reader who hasn't seen Tab 6 yet.

---

### 6.5 Q5 — Are tradition coverage answers findable?

**Assessment:** FAIR for the "most-covered tradition" (Islam + numbers are visible in Tab 1 and tradition charts). CONDITIONALLY FAIR for zero-coverage traditions — depends on whether chart-void-grid renders tradition names as visible text or tooltip-only. As noted in Section 5.5, plan-dataviz.md does not guarantee visible text labels.

**Risk:** Moderate. Q5b (naming 3+ zero-coverage traditions) may score 0.5 instead of 1.0 if tooltip-hover is required.

**Remediation required:** Yes — see Section 5.5 fix above.

---

### 6.6 Are the 5 questions fair overall?

The five questions collectively cover the right dimensions. They test research question (Q1), primary finding (Q2), data integrity (Q3), epistemic humility (Q4), and coverage scope (Q5). The pass threshold (4/5) with Q3 as a hard-fail item is appropriately strict.

**One structural concern:** Q4's three acceptable caveat answers have different cognitive loads. "Same-vendor scorer bias" (Claude graded its own responses) is intuitive and memorable. "T2 blinding asymmetry" requires knowledge of what T2 is. "Gemini data provenance" requires understanding what "backfilled template extraction" means. A reader who finds only the caveat ribbon short texts (without clicking "Read more") will see: "Claude T2 scores may be inflated" — enough for partial credit but not full credit without understanding what T2 is.

**Assessment:** The rubric is fair but lopsided in difficulty across the three caveat options. Same-vendor bias is easiest; T2 blinding is hardest. The rubric should note this: "If a reader names same-vendor scorer bias with specificity, award full credit — this caveat is self-contained in the ribbon without requiring T2 knowledge."

**Severity: MINOR**
**Fix:** Add to Q4 scoring rubric: "Award full credit for any caveat named with specificity. Note that same-vendor scorer bias ('Claude graded its own responses') is self-contained from the ribbon short text; T2 blinding asymmetry requires prior exposure to the T2 instrument definition. Either is equally valid for full credit."

---

## Summary: Severity Matrix

| # | Finding | Severity | Affected Plans |
|---|---------|----------|----------------|
| 1.1 | K/R/V gloss not universally required | CRITICAL | plan-dataviz, plan-vendor-framing |
| 1.9b | "meta-evaluation" unglossed in hero | CRITICAL | plan-narrative |
| 2.1 | Claims index table not mandated (tooltip-only in dataviz) | CRITICAL | plan-dataviz |
| 2.4 | "A3" label exposed in rendered text | CRITICAL | plan-statistics, plan-transparency |
| 3.1 | C8 missing from Tab 1 hero (narrative plan gap) | CRITICAL | plan-narrative |
| 3.2 | C8 hero stat card not in dataviz plan | CRITICAL | plan-dataviz |
| 4.1 | >3 simultaneous unexplained abbreviations on Tab 5 | CRITICAL | plan-dataviz, all |
| 5.1 | Tab reading order conflict | CRITICAL | plan-narrative vs plan-ux-a11y |
| 5.3 | not_significant color conflict (blue vs grey) | CRITICAL | plan-statistics vs plan-dataviz |
| 1.2 | T1 unglossed (only in cold-reader plan) | MAJOR | plan-dataviz, plan-vendor-framing |
| 1.3 | fara'id missing from chart title spec | MAJOR | plan-dataviz |
| 1.7 | Bonferroni no gloss on strip chart | MAJOR | plan-dataviz |
| 1.8 | WEIRD no inline gloss in statistics plan | MAJOR | plan-statistics, plan-narrative |
| 1.9a | "gate-passer" no inline gloss in statistics/dataviz | MAJOR | plan-statistics, plan-dataviz |
| 2.2 | 401/47 context missing on Tab 5 | MAJOR | plan-narrative |
| 2.3 | "Tier 1" no inline gloss in claim cards | MAJOR | plan-statistics, plan-religion |
| 3.3 | C8 not linked to Tab 1 in statistics plan | MAJOR | plan-statistics |
| 3.4 | Reading order compounds buried-lede (ux-a11y) | MAJOR | plan-ux-a11y |
| 4.2 | "CI" abbreviation collision (Citation Impact vs Confidence Interval) | MAJOR | plan-transparency |
| 5.4 | ASCII apostrophe rule not propagated | MAJOR | plan-dataviz, plan-vendor-framing |
| 5.5 | Void-grid tradition names may be tooltip-only | MAJOR | plan-dataviz |
| 5.6 | Simulation label inconsistency across 4 plans | MAJOR | all |
| 6.3 | Mobile caveat accordion starts collapsed | MAJOR | plan-ux-a11y |
| 6.4 | CAV-1 short text requires T2 knowledge | MAJOR | plan-transparency |
| 1.4 | Bootstrap CI no gloss in footer | MINOR | plan-transparency |
| 1.5 | Cohen's d Q2 partial-credit rubric | MINOR | plan-cold-reader |
| 1.6 | Cramer's V no axis gloss in N2 spec | MINOR | plan-dataviz |
| 1.10 | "pp" not spelled out | MINOR | plan-dataviz, plan-vendor-framing |
| 2.5 | Corpus count inconsistency (2,043 vs 2,099) | MINOR | plan-transparency |
| 6.5 | Q4 rubric difficulty asymmetry | MINOR | plan-cold-reader |

---

## Priority Fix Order

**Do first (blockers for cold-reader gate):**
1. Add C8 hero stat card requirement to plan-narrative.md Tab 1 AND plan-dataviz.md Tab 1 chart list (FM-3 gap)
2. Replace "A3" with "values relevance score (0–100)" everywhere in implementation plans
3. Resolve tab reading order conflict between plan-narrative.md and plan-ux-a11y.md
4. Resolve not_significant color conflict: plan-dataviz.md N3 must use blue, not grey
5. Mandate static claims index table (not tooltip-only) in plan-dataviz.md Tab 5
6. Add K/R/V legend requirement to plan-dataviz.md N7 and plan-vendor-framing.md Section 4

**Do second (readability failures that reduce scores below 4.0):**
7. Rename "CI" (Citation Impact) to "CIT" or "Impact" to prevent collision
8. Add Bonferroni gloss to strip chart and footer
9. Add WEIRD gloss to plan-statistics.md C6 block
10. Add fara'id gloss to plan-dataviz.md N5 chart title spec
11. Fix mobile caveat accordion to start expanded on first load
12. Fix CAV-1 short text to not require T2 knowledge
13. Standardize simulation label across all plans (designate plan-vendor-framing.md as canonical)
14. Add void-grid visible-text-label requirement to plan-dataviz.md L11

**Do third (polish and robustness):**
15. T1 gloss requirement propagated to plan-dataviz.md and plan-vendor-framing.md
16. Bootstrap CI gloss in transparency footer
17. ASCII apostrophe lint requirement in plan-dataviz.md and plan-vendor-framing.md
18. Cramer's V axis gloss in N2 spec
19. "pp" → "percentage-point" in all chart titles
20. Corpus count consistency audit

---

*Critique authored: 2026-04-13. Reviewer: Plain-Reader Critic agent. Methodology: cold reading of 8 plan files and canonical JSON without reference to underlying paper markdown.*
