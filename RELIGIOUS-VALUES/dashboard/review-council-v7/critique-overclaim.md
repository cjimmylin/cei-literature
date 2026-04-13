---
created: 2026-04-13
author: Overclaim Auditor
scope: All 8 dashboard v7 plan files + claims_canonical.json
plans_audited:
  - plan-cold-reader.md
  - plan-dataviz.md
  - plan-narrative.md
  - plan-religion.md
  - plan-statistics.md
  - plan-transparency.md
  - plan-ux-a11y.md
  - plan-vendor-framing.md
---

# Overclaim Audit — Dashboard v7 Plans

## Executive Summary

The 8 plans are collectively strong on simulation disclosure. The vendor-framing plan
(plan-vendor-framing.md) and transparency plan (plan-transparency.md) are exemplary — they
contain some of the most rigorous provenance disclosure language in any dashboard project this
auditor has reviewed. However, several specific overclaim patterns were identified across the
other plans that require correction before implementation. No CRITICAL bare-vendor-name issues
were found in final prose, but CRITICAL issues exist around C8 strength framing, C4/C6 verdict
language, and one generalization overclaim. Full findings follow.

---

## Audit Findings by Criterion

---

### Criterion 1 — Bare Vendor Names (GPT, OpenAI, Gemini, Google without qualifier)

**Result: NO CRITICAL HITS in final prose.**

The vendor-framing plan (plan-vendor-framing.md, Section 2) establishes and enforces canonical
labels throughout:
- `Claude-as-Claude` for real Anthropic output
- `Claude-roleplaying-OpenAI-scorer` / `Sim: OpenAI-scorer` for simulated OpenAI
- `Claude-roleplaying-Gemini-scorer` / `Sim: Gemini-scorer` for simulated Gemini

Section 11 of plan-vendor-framing.md explicitly forbids bare "OpenAI", "GPT", "Gemini",
"Google" anywhere in the rendered DOM, with a lint check requirement. This is correctly specified.

**MINOR — plan-dataviz.md, Section 2, N5 pre-computed alt text:**

The alt text for chart N5 (T2 Span Strip) reads:
> "GPT-Codex (Simulated): 100%."

"GPT-Codex" appears without the canonical "Claude-roleplaying-OpenAI-scorer" or "Sim:"
prefix. The alt text is the string embedded in `data.js` and exposed via `aria-label` — it
will be read verbatim by screen readers. A screen-reader user encounters "GPT-Codex
(Simulated)" without the roleplay framing context that sighted users get from the visual
hatching and badge system.

**Required fix:** Update the pre-computed alt text to:
> "Claude-roleplaying-OpenAI-scorer as GPT-Codex (Simulated): 100%."

or at minimum:
> "(Simulated by Claude) GPT-Codex: 100%."

**MINOR — plan-dataviz.md, Section 2, N4 pre-computed alt text:**

The typology grid alt text reads:
> "Simulated: Compressed Accuracy (OpenAI): K=0.967..."
> "Simulated: Template Refusal (Gemini): K=0.0..."

Bare "OpenAI" and "Gemini" appear without the roleplay qualifier. The word "Simulated:" in
the prefix helps but does not convey that it is Claude simulating those vendors — the current
phrasing could be read as "OpenAI submitted data labeled Simulated." Correct to:
> "Simulated (Claude-roleplaying): Compressed Accuracy (OpenAI-scorer condition)..."
> "Simulated (Claude-roleplaying): Template Refusal (Gemini-scorer condition)..."

---

### Criterion 2 — Claim Strength Inflation (Revised and Not-Significant Verdicts)

**MAJOR — plan-narrative.md, Tab 5 Interpretation paragraph, C4 and C6:**

The narrative plan writes of C4:
> "The structural barriers that disadvantage underrepresented traditions (C4) appear to
> operate through academic publishing norms and data accessibility..."

This language states the mechanism as if it is confirmed ("appear to operate through"),
whereas the statistics plan (plan-statistics.md, Section 4) correctly notes that the logistic
regression has pseudo R-squared = 0.068 and neither individual predictor reaches significance
(p > 0.09 for both). The narrative plan omits the non-significance caveat entirely for C4.

The statistics plan handles this correctly (Section 4 dashboard text is properly hedged:
"No individual predictor reaches statistical significance (p > 0.09)"). The narrative plan
contradicts it by stating the mechanism affirmatively without the non-significance qualifier.

**Required fix in plan-narrative.md, Tab 5 Interpretation:**
Add an explicit qualifier such as: "...appear to operate through academic publishing norms —
though neither individual predictor reaches statistical significance (p > 0.09), and the
finding is classified as revised, not confirmed."

**MAJOR — plan-narrative.md, Tab 5 Interpretation paragraph, C6:**

The narrative plan writes:
> "the expected 'Western-favoring' bias in benchmark quality (C6) is actually reversed —
> non-Western traditions pass at a higher rate than Western ones..."

The statistics plan (plan-statistics.md, Section 4) correctly notes that C6 Fisher's exact
test has p = 0.09 — just above the threshold — and says "Treat as a strong trend, not a
confirmed effect." The narrative plan does not include this hedge. A reader of the narrative
plan text alone would believe C6 direction reversal is a confirmed finding.

**Required fix in plan-narrative.md, Tab 5 Interpretation:**
Add: "...though this direction reversal does not reach the conventional significance threshold
(p = 0.09) and should be treated as a strong trend rather than a confirmed effect."

**MINOR — plan-statistics.md, Section 3, structural placement note:**

The statistics plan writes:
> "C8 should appear first in the 'Core Findings' tab, above all other claims."

This is correct framing. However, the statistics plan also writes in Section 3:
> "This is an argument about construct validity, not just coverage."

This characterization is accurate and welcome. No overclaim here. (Flagged for completeness
— no fix required.)

---

### Criterion 3 — Claim 8 Overclaim (d=-1.23 as definitive vs strong evidence)

**MAJOR — plan-statistics.md, Section 3, "three-way convergence" box proposed text:**

The proposed callout reads:
> "Three independent statistical tests all point to the same conclusion: mean score 30.0
> (t-test), median score 27.5 (Wilcoxon), only 3 of 16 benchmarks above the midpoint
> (binomial). Convergent evidence across methods strengthens confidence beyond what any
> single test provides."

The phrase "all point to the same conclusion" is accurate but the box lacks any mention of
the scorer bias caveat (CAV-2) that plan-transparency.md correctly surfaces: "A3 values
relevance scoring was conducted by Claude Opus (same-vendor)." The convergence box, if
displayed as the primary C8 callout, will be seen before the caveat ribbon by many users who
are focused on the claim cards. A reader sees "three independent tests → same conclusion"
without the scorer-independence caveat.

The transparency plan (plan-transparency.md, Section 3, Claims Tab annotation) does add:
> "A3 values relevance scoring was conducted by Claude Opus (same-vendor). The large effect
> size (d=−1.23) across multiple convergent tests mitigates but does not eliminate this
> concern."

But this annotation appears in plan-transparency.md. The statistics plan's convergence box
does not cross-reference it. If a developer implements the statistics plan's convergence box
without reading the transparency plan, the caveat will be absent from the box.

**Required fix:** Add to the statistics plan's proposed convergence box text:
> "Note: A3 values relevance scores were assessed by Claude Opus (same scorer as the Claude
> trials). See Caveat 2: Scorer Bias above."

**MINOR — plan-cold-reader.md, Q2 scoring rubric:**

Q2 specifies the expected answer for the "most important finding" as:
> "The most important finding is that most religious values benchmarks do not actually test
> religious values — the mean values relevance score is 30/100 (significantly below the
> midpoint)..."

The rubric awards full credit for answers that identify "values relevance failure" with "at
least one concrete number." This is appropriate. However, the failure mode listed for Q2
is "Buried lede" — if C8 is below the fold, readers default to C1.

This is a good failure mode specification. No overclaim in the gate itself.

However: the cold-reader plan's Q2 expected answer includes the phrase "significantly below
the midpoint" — using "significantly" in its statistical sense. This is accurate (p < 0.001)
but could be misread by a layperson as "very" rather than as a statistical term. Given that
this is a cold-reader gate document, not a dashboard display string, the risk is low. Flag as
MINOR informational note; no fix required.

---

### Criterion 4 — Three Caveats Visibility Across Plans

**CRITICAL — plan-narrative.md: All 3 caveats absent from Tab 5 interpretation.**

The Tab 5 (Claims & Robustness) interpretation in plan-narrative.md describes C8 as:
> "The strongest finding is values relevance failure (C8): the average benchmark among the
> top 16 scores only 30 out of 100 on a measure of whether it actually tests religious values
> as opposed to factual recall or bias detection — a large effect (Cohen's d = -1.23) that
> holds across three independent statistical tests."

None of the three caveats are mentioned. The plan-transparency.md does add a C8 caveat
(scorer bias note), but the narrative plan is the primary reading guide for Tab 5 — a
developer or designer using plan-narrative.md as the authoritative source for Tab 5
interpretation text will produce a C8 block with no caveat visible on the claims tab.

The narrative plan's Tab 6 (Simulated Scorer Study) correctly references all three caveats:
> "Three methodological caveats apply and are displayed prominently: (1) T2 blinding
> asymmetry... (2) same-vendor scorer bias... (3) Gemini data provenance..."

But these caveats are not linked back into Tab 5's C8 block, even though CAV-2 (scorer bias)
directly affects the A3 scoring that underlies C8.

**Required fix in plan-narrative.md, Tab 5 Interpretation:**
Add to the C8 paragraph: "Values relevance (A3) scoring was performed by Claude Opus
(same-vendor as the Claude trial models — see Caveat 2: Scorer Bias). The large effect size
(d=−1.23) and three-test convergence mitigate but do not eliminate this concern."

**MAJOR — plan-dataviz.md: No caveat tags specified for any claims-tab charts.**

The dataviz plan specifies per-chart caveat tags for Tab 6 (cross-vendor charts) implicitly
through the vendor framing and simulated-tag CSS class. However, for the new N1 (C8 forest
plot) and N3 (p-value strip chart) in Tab 5, the dataviz plan does not specify that a
caveat badge should appear in the chart header linking to CAV-2 (scorer bias). The
plan-transparency.md specifies per-chart caveat surfacing (Section 3), but the dataviz plan
does not cross-reference it for Tab 5 charts.

A developer implementing charts from plan-dataviz.md alone will not add the caveat badge to
the C8 forest plot.

**Required fix in plan-dataviz.md, Section 2, N1 specification:**
Add: "Chart header must include a CAV-2 (Scorer Bias) badge — same pattern as Tab 6 charts.
A3 values relevance was scored by Claude Opus. See plan-transparency.md Section 3."

**PASS — plan-transparency.md:**
This plan correctly surfaces all three caveats in the sticky ribbon (Section 1), per-chart
caveat tagging (Section 3), and the footer methods disclosure (Section 4). The transparency
plan is the canonical reference and is internally consistent.

**PASS — plan-vendor-framing.md:**
Section 10 specifies that Tab 6 must end with a "Methodological Limitations Panel"
reproducing all four cross-vendor caveats from the paper's limitations list verbatim.
All three study caveats (T2 blinding, scorer bias, Gemini provenance) are explicitly named.

**PASS — plan-cold-reader.md:**
Q4 tests specifically whether readers can recall at least one of the three caveats.
Q3 tests whether readers correctly identify the simulation framing. This gate is well-
designed for caveat visibility validation.

**MINOR — plan-ux-a11y.md: Caveat ribbon behavior described but CAV-2/C8 link not specified.**

The UX plan describes the caveat ribbon architecture correctly (Section 9) and specifies DOM
placement (before tab navigation). However, it does not specify that the per-chart caveat
badge for C8-related charts should link back to `#cav-2`. The transparency plan does specify
this (Section 3, per-chart badge links). The risk is low since plan-transparency.md is
authoritative, but consistency would help.

**MINOR — plan-religion.md:**
The religion plan (plan-religion.md) focuses on tradition framing, romanization conventions,
and WEIRD-bias sensitivity. It does not address the trial methodology caveats. This is
appropriate — the religion plan is not responsible for trial data. However, Section 4
("Handling T2 — The Fara'id Discriminative Test") discusses T2 results:
> "Haiku achieves 76.7% overall (80% beginner, 73.3% advanced)..."
> "The Gemini family produces the most striking results: 6.7% to 20% across four models."

CAV-1 (T2 blinding asymmetry) is mentioned in the final checklist item:
> "CAV-1 (T2 blinding asymmetry) is disclosed wherever T2 accuracy figures appear."

But the body of Section 4.3 does not include the blinding caveat in the interpretation text
it proposes for the dashboard. If a developer follows Section 4.3 body text rather than the
checklist, the blinding caveat may be absent from the T2 discussion prose.

**Required fix in plan-religion.md, Section 4.3:**
Add a sentence to the proposed dashboard display guidance:
> "Note: original Claude T2 trials had gold-standard answer labels visible; these scores
> (100% for Opus and Sonnet) are upper-bound estimates. See CAV-1 in the caveats ribbon."

---

### Criterion 5 — "Cross-Vendor" Language Without "Simulated" Qualifier

**CRITICAL — plan-narrative.md, Tab 6 heading and subtitle text:**

The narrative plan uses "Simulated Scorer Study" as the tab name (correct) but the subtitle
text reads:
> "9 models, 3 vendors (simulated)"

The word "vendors" in parenthesis-qualified form is borderline. More importantly, the Tab 6
Background section opens with:
> "Even if we know which benchmarks exist and how good they are, we also want to know how
> different AI systems actually perform on them. Do different AI models behave similarly when
> confronted with religious content, or do they show fundamentally different patterns? This
> tab presents a comparison of 9 AI models from 3 vendor families on a set of religious
> knowledge, reasoning, and values items."

The phrase "9 AI models from 3 vendor families" does not include a "simulated" qualifier.
A reader who reads only the Background section (before reaching the Method section) would
believe the study has genuine 3-vendor data. The Background section is the framing paragraph
that establishes the research question — it appears before any disclosure.

**Required fix in plan-narrative.md, Tab 6 Background:**
Change to:
> "This tab presents a comparison using 9 model configurations from 3 vendor-family
> conditions — of which only the Anthropic Claude family used real API calls; OpenAI and
> Gemini conditions were simulated by Claude models roleplaying those vendor behaviors."

**MAJOR — plan-narrative.md, Tab 6 Interpretation paragraph, Gemini and OpenAI result framing:**

The interpretation states:
> "The simulated OpenAI Codex models show 'compressed accuracy'..."
> "The simulated Gemini models show 'template refusal'..."

"Simulated" qualifier is present — this is correct. However, the sentence before these reads:
> "Three distinct behavioral patterns emerge."

This does not qualify whether "emerge" refers to real patterns or simulation artifacts. A
reader who is skimming may see "Three distinct behavioral patterns emerge" as a top-level
finding without registering that two of the three "emerge" from simulation. Add "from this
mixed real-and-simulated dataset" or similar.

**PASS — plan-vendor-framing.md:**
"Cross-Vendor" is explicitly forbidden in Section 1 (tab name) and Section 11 (forbidden
strings list). This is the strongest language in any of the 8 plans on this criterion.

**PASS — plan-transparency.md:**
Footer disclosure (Section 4) explicitly states: "All non-Anthropic vendor data is
Claude-simulated (Sonnet/Haiku roleplay), not real API calls."

**MINOR — plan-statistics.md, Section 7 (Implementation Note 7):**

States: "Simulated cross-vendor data (Gemini, OpenAI) must be labeled with 'Simulated —
Claude roleplay, not real API' wherever model comparison charts appear."

Uses "cross-vendor" in the implementation note itself (a developer-facing text, not user-
facing). Since this note is not rendered to users, it is a MINOR consistency issue rather
than a user-facing overclaim. The vendor-framing plan bans "cross-vendor" from rendered DOM
and JS display strings; this note is meta-commentary. Recommend updating for terminology
consistency: replace "Simulated cross-vendor data" with "Simulated vendor-condition data."

---

### Criterion 6 — Generalization Overclaim

**MAJOR — plan-narrative.md, overall narrative arc summary ("Act 2"):**

The narrative arc summary states:
> "Cross-model trials reveal that AI systems show fundamentally different behavioral modes
> on religious content, but current evaluation tools cannot reliably distinguish them."

"AI systems" is an overgeneralization. The trials cover Claude (real API), and simulated
proxies for OpenAI and Gemini. The conclusion that "AI systems show fundamentally different
behavioral modes" should be bounded to "Claude models show..." or "In this study's model
configurations, three behavioral modes were identified..." Claiming that "AI systems" broadly
show this is not supported by a study that has real data for only one vendor family.

**Required fix in plan-narrative.md, narrative arc summary:**
Change "AI systems show fundamentally different behavioral modes" to:
"Model configurations in this study's trial show three distinct behavioral modes — though
only the Claude family results derive from real API calls; the OpenAI and Gemini patterns are
Claude-simulated and require replication."

**MAJOR — plan-statistics.md, Section 3, C8 connection to field-level implications:**

The statistics plan writes:
> "The most policy-relevant number... d = -1.23 means the mean values relevance score (30.0)
> is 1.23 standard deviations below the midpoint (50.0)."

And in Section 3:
> "C8 is supported by three methodologically distinct tests..."

This framing is correct for the 16 benchmarks assessed in the A3 scoring. However, the
statistics plan does not clarify anywhere that the A3 values relevance scoring was applied
to only 16 of the 47 gate-passers. The full claims_canonical.json shows n=16 for the t-test.
The statistics plan discusses "the top 16" once (in Section 3 proposed callout text) but the
section header and dashboard placement guidance do not consistently carry this "n=16"
qualifier. A reader who sees the C8 forest plot without reading the n=16 qualifier might
infer the values relevance failure applies to all 47 gate-passers.

**Required fix in plan-statistics.md, Section 3:**
Add to the proposed callout box text: "(assessed on the top-16 tier-eligible benchmarks; the
remaining 31 gate-passers were not scored on A3)"

**MINOR — plan-cold-reader.md, Q5 expected answer:**

The expected answer for Q5 states:
> "Most viable benchmarks: Islam (28 of 47 gate-passing candidates; 9 of 12 Tier 1 benchmarks)"

This is accurate. However, the Q5b expected answer states:
> "Reader does not need all 8 — naming at least 3 correct traditions counts."

This is a reasonable gate threshold, but one potential misread is that a reader might infer
the 8 traditions listed represent ALL traditions with zero benchmarks in the entire global
religious landscape, rather than specifically zero within the 14-tradition scope of this
study. No fix required in the gate document itself, but the dashboard text should specify
"8 of the 14 traditions included in this study's scope" when listing the zero-coverage
traditions.

**MINOR — plan-religion.md, Section 2 void-type framing:**

The plan distinguishes Type A (coordination gap) from Type B (structural epistemic exclusion)
voids. Section 2 states for Type A:
> "Estimated timeline: 2-3 years with sustained effort."

This timeline estimate is not sourced from the paper's claims or data. It is an editorial
judgment introduced by the religion plan council member. Presenting a "2-3 year" estimate as
dashboard annotation text implies empirical precision that is not supported. If included in
dashboard display text, it should be qualified as "rough estimate" or "estimated order of
magnitude" and noted as editorial judgment, not a study finding.

**Required fix in plan-religion.md, Section 2, Type A description:**
Either remove the timeline estimate from dashboard display text or add: "(rough editorial
estimate — not a study finding)."

---

## Summary Table

| # | Severity | Plan | Location | Finding |
|---|----------|------|----------|---------|
| 1 | CRITICAL | plan-narrative.md | Tab 5 Interpretation | CAV-2 scorer bias absent from C8 block; all 3 caveats missing from Tab 5 |
| 2 | CRITICAL | plan-narrative.md | Tab 6 Background | "9 AI models from 3 vendor families" with no simulation qualifier in framing paragraph |
| 3 | MAJOR | plan-narrative.md | Tab 5 Interpretation | C4 mechanism stated affirmatively without non-significance qualifier (contradicts plan-statistics.md) |
| 4 | MAJOR | plan-narrative.md | Tab 5 Interpretation | C6 direction reversal stated as confirmed finding without p=0.09 hedge |
| 5 | MAJOR | plan-narrative.md | Narrative Arc Summary | "AI systems show fundamentally different behavioral modes" overgeneralizes beyond Claude-only real data |
| 6 | MAJOR | plan-statistics.md | Section 3, convergence box | C8 convergence box lacks CAV-2 scorer bias cross-reference |
| 7 | MAJOR | plan-statistics.md | Section 3, C8 scope | n=16 scope of A3 scoring not consistently stated; implies findings apply to all 47 |
| 8 | MAJOR | plan-dataviz.md | Section 2, N1 spec | C8 forest plot spec lacks caveat badge instruction for CAV-2 |
| 9 | MAJOR | plan-narrative.md | Tab 6 Interpretation | "Three distinct behavioral patterns emerge" not flagged as mixed real+simulated dataset |
| 10 | MINOR | plan-dataviz.md | N5 alt text | "GPT-Codex (Simulated)" in aria-label lacks roleplay framing for screen readers |
| 11 | MINOR | plan-dataviz.md | N4 alt text | Bare "OpenAI" and "Gemini" in typology grid alt text |
| 12 | MINOR | plan-statistics.md | Section 7, note 7 | "Simulated cross-vendor data" uses forbidden term in developer-facing text |
| 13 | MINOR | plan-religion.md | Section 4.3 body | T2 interpretation text lacks CAV-1 blinding caveat in body (only in checklist) |
| 14 | MINOR | plan-religion.md | Section 2, Type A | "2-3 year" timeline estimate unsourced; should be labeled editorial, not study finding |
| 15 | MINOR | plan-ux-a11y.md | Section 9 | Does not specify that C8-related charts need CAV-2 badge (deferred to transparency plan) |

---

## Plans That Passed All Criteria

**plan-vendor-framing.md** — No issues found. Canonical label enforcement, forbidden strings
list, and lint check requirement are exemplary. This plan should be treated as the normative
reference for simulated-vendor framing across all plans.

**plan-transparency.md** — No issues found. All three caveats fully specified with correct
ribbon placement, per-chart badge rules, footer disclosure, and "How to interpret" expandable
section. CAV-3 Gemini provenance text correctly states: "non-Anthropic API calls are not
supported. Gemini data was backfilled from web interface interactions. This constraint is a
hard environmental limitation, not a researcher choice."

**plan-cold-reader.md** — No overclaims in the gate document itself. Q3 hard-fail condition
(zero score if reader believes cross-vendor data is real) is the correct epistemic priority.

---

## Priority Fix Order for Implementation

1. **CRITICAL first:** Fix plan-narrative.md Tab 6 Background and Tab 5 Interpretation
   (findings 1 and 2 above) before any implementation begins — these affect the primary
   reading-order text that shapes first impressions.

2. **MAJOR second:** Fix plan-narrative.md C4/C6 hedging (findings 3 and 4) and AI systems
   generalization (finding 5); fix plan-statistics.md convergence box and n=16 scope
   (findings 6 and 7); fix plan-dataviz.md N1 caveat badge instruction (finding 8).

3. **MINOR last:** Alt text label fixes in plan-dataviz.md (findings 10 and 11); terminology
   cleanup in plan-statistics.md and plan-religion.md (findings 12, 13, 14).

---

*Auditor note: The overall quality of the v7 council plans on simulation disclosure is
substantially better than most multi-tab dashboard projects. The vendor-framing and
transparency plans in particular represent a high bar. The issues found are concentrated in
plan-narrative.md, which was likely written with a focus on storytelling rather than
provenance — a predictable failure mode for narrative-role council agents. Recommend routing
all Tab 5 and Tab 6 interpretation text through the Simulated-Vendor Framing Officer for
a second pass before developer handoff.*
