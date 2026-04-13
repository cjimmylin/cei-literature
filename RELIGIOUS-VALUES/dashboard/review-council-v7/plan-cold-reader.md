# Cold-Reader Comprehension Gate — Dashboard v7
**Persona:** First-Time Reader (has NOT read the paper; sees only the rendered dashboard HTML)
**Threshold:** 4 of 5 questions correct blocks deployment if failed; dashboard ships only when PASS
**Date drafted:** 2026-04-13
**Version:** 1.0

---

## Purpose

This document defines the acceptance test that BLOCKS dashboard v7 deployment. A persona agent who has not read the underlying paper is given a Playwright text snapshot of the rendered dashboard and must answer 5 comprehension questions. The gate ensures the dashboard communicates its core message, caveats, and scope limitations to any reader — not only to authors who already know the context.

---

## Part 1 — The 5 Comprehension Questions

### Q1 — Research Question
**Prompt to persona agent:**
> "Based only on what you can read in the dashboard, what question is this study trying to answer?"

**Expected correct answer (any of the following formulations count):**
- Whether existing LLM benchmarks that claim to test religious values alignment actually test what they claim
- Whether religious values benchmarks for AI models are valid, and if so, which traditions are covered
- How good are the current benchmarks for evaluating LLMs on religious values — do they measure values, knowledge recall, or bias detection?

**Scoring rubric:**
- **Full credit (1.0):** Answer identifies (a) LLM evaluation / benchmarks AND (b) religious values specifically AND (c) a validity / "does it test what it claims" angle. All three components present.
- **Partial credit (0.5):** Answer captures two of three components (e.g., mentions religious benchmarks and LLMs but omits the validity/meta-evaluation frame, OR mentions validity but calls it "ethics" not "religious values").
- **No credit (0.0):** Answer is vague ("it studies AI and religion"), mentions only one component, or describes the paper as a benchmark paper rather than a meta-evaluation.

**Failure mode detected:** Jargon creep — if the dashboard uses "meta-evaluation" without a plain-English gloss, readers may answer "it creates benchmarks" rather than "it evaluates existing benchmarks."

---

### Q2 — Most Important Finding
**Prompt to persona agent:**
> "What is the single most important finding from this study?"

**Expected correct answer:**
The most important finding is that most religious values benchmarks do not actually test religious values — the mean values relevance score is 30/100 (significantly below the midpoint), only 3 of 16 assessed benchmarks score above 50, and none reach 75. (This is Claim 8 / values relevance failure, Cohen's d = -1.23, p < 0.001.)

**Scoring rubric:**
- **Full credit (1.0):** Answer identifies the values relevance failure as the headline result, with at least one concrete number (30/100 mean score, OR 3/16 above midpoint, OR d = -1.23, OR p < 0.001). Does not need all numbers, just one.
- **Partial credit (0.5):** Answer identifies values relevance failure conceptually but supplies no numbers. OR answer names a different supported claim (Islam dominance / tradition asymmetry) with correct numbers — that is the second most important finding and earns partial credit.
- **No credit (0.0):** Answer names a non-significant or revised claim as the headline (e.g., "WEIRD bias" or "field recency"). OR answer describes only the cross-model performance comparison without mentioning benchmark validity.

**Failure mode detected:** Buried lede — if Claim 8 (values relevance failure) appears below the fold or is not visually distinguished as the primary finding, readers default to whatever appears first (often Claim 1 / Islam dominance).

---

### Q3 — Cross-Vendor Data Provenance
**Prompt to persona agent:**
> "How were the cross-vendor results (OpenAI and Gemini models) obtained — were they real API calls to those models, or something else? Explain what you understand from the dashboard."

**Expected correct answer:**
The OpenAI and Gemini results are simulated — Claude (Sonnet and Haiku) role-played as those models, they were not real API calls to OpenAI or Google. This is acknowledged explicitly in the dashboard.

**Scoring rubric:**
- **Full credit (1.0):** Answer states that cross-vendor results are simulated / Claude-roleplayed / not real API calls. Does not need to name which Claude models did the roleplaying; the key fact is "simulated, not real."
- **Partial credit (0.5):** Answer expresses uncertainty ("I'm not sure, the dashboard doesn't make it clear") — this counts as partial because the reader at least did not falsely assert the results are real. Award 0.5 only if reader signals awareness that something about the data provenance is qualified.
- **No credit (0.0):** Answer states or implies the results are genuine API calls to OpenAI/Google. This is the critical false belief the gate must block.

**Failure mode detected:** Caveat invisibility — if the simulation disclosure appears only in a footnote, tooltip, or collapsed section, readers assume the cross-vendor data is real and will misreport findings. The disclosure must be surfaced in the main body of the relevant chart or table.

---

### Q4 — Reason to Distrust T2 Numbers
**Prompt to persona agent:**
> "Give one reason why you might not fully trust the T2 accuracy numbers reported for the Claude models."

**Expected correct answer (any one of the following):**
1. **T2 blinding asymmetry:** The original Claude T2 trials had gold-standard answers visible; cross-vendor trials used a blind protocol. Claude's 100% scores are therefore upper-bound estimates, not blind-administration results.
2. **Same-vendor scorer bias:** All rubric scoring was done by Claude Opus 4.6, including scoring Claude-family responses — same-family models may share evaluative preferences, inflating scores.
3. **Simulation artifact (for cross-vendor):** The non-Claude T2 scores came from simulated roleplaying, not real model outputs, so comparing them to Claude's real scores is methodologically asymmetric.

**Scoring rubric:**
- **Full credit (1.0):** Answer names any one of the three caveats above with enough specificity to show the reader understood it (e.g., "the answers were not hidden for Claude" or "Claude graded its own responses" or "Gemini was simulated not real").
- **Partial credit (0.5):** Answer gestures at a legitimate concern but is too vague to confirm understanding (e.g., "there might be bias" without identifying what kind).
- **No credit (0.0):** Answer states no reason to distrust OR invents a reason not disclosed in the dashboard (hallucination). Also no credit if reader says "I didn't see any caveats" — this means caveat visibility has failed.

**Failure mode detected:** Acronym soup / caveat invisibility — if "T2" is used without a gloss ("T2 = 30-item Arabic MCQ on Islamic inheritance law / fara'id"), readers cannot engage with T2-specific caveats. Also: if caveats are collapsed behind a toggle or placed after the charts, readers skip them.

---

### Q5 — Tradition Coverage
**Prompt to persona agent:**
> "Which religious tradition has the most viable benchmarks according to this study? Which traditions have none at all?"

**Expected correct answer:**
- Most viable benchmarks: **Islam** (28 of 47 gate-passing candidates; 9 of 12 Tier 1 benchmarks)
- Traditions with zero viable benchmarks: **Judaism, Jainism, Taoism, Shinto, Ubuntu Philosophy, Indigenous Spirituality, Baha'i, and Zoroastrianism** (8 of 14 surveyed traditions). Reader does not need all 8 — naming at least 3 correct traditions counts.

**Scoring rubric:**
- **Full credit (1.0):** Correctly names Islam as most-covered AND names at least 3 of the 8 zero-coverage traditions.
- **Partial credit (0.5):** Correctly names Islam as most-covered but cannot name any zero-coverage traditions. OR names 1-2 zero-coverage traditions but misidentifies the most-covered tradition.
- **No credit (0.0):** Names a tradition other than Islam as most-covered. OR cannot identify either part of the question (the 8 traditions are presumably listed in the dashboard).

**Failure mode detected:** Assumed context — if the dashboard uses "8 of 14 traditions have zero coverage" as a headline number but does not enumerate the 8 traditions, readers cannot answer Q5b and partial credit becomes the ceiling.

---

## Part 2 — Scoring Criteria Summary

| Q | Full (1.0) | Partial (0.5) | None (0.0) | Gate-relevant failure mode |
|---|-----------|--------------|-----------|---------------------------|
| Q1 | All 3 components: LLMs + religious values + validity frame | 2 of 3 components | 1 component or vague | Jargon creep: "meta-evaluation" unglossed |
| Q2 | Values relevance failure named + at least 1 number | Values relevance failure named, no numbers | Non-significant finding named as headline | Buried lede: C8 not above fold |
| Q3 | "Simulated / not real API calls" stated | Uncertainty expressed, no false assertion | States or implies results are real | Caveat invisibility: simulation disclosure hidden |
| Q4 | Any one of 3 disclosed caveats, with specificity | Vague concern gestured at | No caveats found OR hallucinated caveat | Acronym soup: T2 unglossed; caveats collapsed |
| Q5 | Islam + 3+ zero-coverage traditions | Islam only, OR 1-2 traditions only | Wrong most-covered tradition | Assumed context: 8 traditions not enumerated |

**Pass threshold:** Score >= 4.0 (where each question scores 0, 0.5, or 1.0; maximum 5.0). Partial credits count: e.g., 3 full + 2 partial = 4.0 = PASS (barely). 3 full + 1 partial + 1 none = 3.5 = FAIL.

**Hard-fail condition:** Q3 scores 0.0 (reader falsely believes cross-vendor data is real). This automatically blocks deployment regardless of other scores, because a reader who leaves believing the Gemini/OpenAI results are real API calls will misrepresent the study. Q3 is a mandatory-pass item in addition to the 4/5 aggregate threshold.

---

## Part 3 — Failure Modes the Gate Must Catch

### FM-1: Jargon Creep
**Definition:** K/R/V used as abbreviations in charts or headings without a legend or gloss anywhere visible on the page.
**Test:** Ask persona agent to explain what K, R, V stand for. If they cannot, jargon creep is confirmed.
**Dashboard elements at risk:** Rubric score charts, the response-length gradient visualization, any axis label using single letters.
**Minimum fix required:** A visible legend box on the chart (not tooltip-only): "K = Knowledge, R = Reasoning, V = Values."

### FM-2: Assumed Context ("the 8 claims")
**Definition:** Dashboard refers to "8 claims" or "Claim 8" without enumerating or briefly labeling all 8 claims so a first-time reader can identify them.
**Test:** Ask persona agent to list the 8 claims. If they cannot retrieve a list from the dashboard, assumed context is confirmed.
**Dashboard elements at risk:** Any summary panel that says "4 of 8 claims are supported" without a claims enumeration table or expandable list.
**Minimum fix required:** A claims index table (Claim # | One-sentence label | Verdict) visible without scrolling past the main finding.

### FM-3: Buried Lede (Claim 8 below the fold)
**Definition:** The values relevance failure finding (C8, d = -1.23, mean 30/100) does not appear in the hero section or first visible panel of the dashboard. It is subordinated to tradition asymmetry (C1) or cross-model comparisons.
**Test:** Record the vertical scroll position at which a reader first encounters the C8 result. If it requires scrolling more than one viewport height, buried lede is confirmed.
**Minimum fix required:** Add a hero stat card or banner reading "Mean values relevance: 30/100 — most benchmarks do not test religious values" at the top of the dashboard, before any other findings.

### FM-4: Caveat Invisibility
**Definition:** The three methodological caveats (T2 blinding asymmetry, same-vendor scorer bias, Gemini data provenance) are placed in a collapsed accordion, footnote, or appendix section that a reader can easily miss.
**Test:** Ask persona agent "did the dashboard mention any limitations or caveats about the data?" If they report none, or only one, caveat visibility has failed.
**Minimum fix required:** Each caveat must appear either (a) inline with the relevant chart/table as a visible warning badge or callout box, OR (b) in a dedicated "Caveats" panel that is open by default (not collapsed). A footnote alone is insufficient.

### FM-5: Acronym Soup (T1/T2/fara'id unexplained)
**Definition:** T1, T2, or "fara'id" appear in charts or text without a plain-English definition visible on the same screen.
**Test:** Ask persona agent "what is T2?" and "what is fara'id?" If they cannot answer from dashboard content, acronym soup is confirmed.
**Minimum fix required:**
- "T2" must be glossed on first use: "T2 (30-item Arabic multiple-choice test on Islamic inheritance law / fara'id)"
- "fara'id" must be glossed: "fara'id = Islamic inheritance law"
- "T1" must be glossed: "T1 (65-item construct validity battery: Knowledge, Reasoning, Values, Bias items)"

---

## Part 4 — Test Protocol

### Step 1: Generate Text Snapshot
```bash
# From the dashboard directory, start HTTP server
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/RELIGIOUS-VALUES/dashboard/
python3 -m http.server 8765 &

# Use Playwright to navigate and capture rendered text
# (browser_navigate to http://localhost:8765/v7/index.html,
#  then browser_snapshot to get accessibility tree / full text content)
```

The snapshot must capture the full rendered DOM text (not PDF, not screenshot). Use Playwright `browser_snapshot` which returns the accessibility tree, preserving text that may be in collapsed sections. Scroll to bottom before snapshot to ensure lazy-loaded content is rendered.

Save snapshot to: `dashboard/review-council-v7/cold-reader-snapshot-YYYYMMDD.txt`

### Step 2: Prepare Persona Agent Context
Provide the persona agent with ONLY:
1. The full text snapshot (no JSON data files, no paper markdown)
2. This instruction block:

```
You are a first-time reader of this research dashboard. You have NOT read the underlying paper.
Answer the following 5 questions based ONLY on what you can read in the dashboard text provided.
If the dashboard does not provide enough information to answer a question, say so explicitly.
Do not guess or infer beyond what is written. Quote the dashboard text that supports each answer.
```

### Step 3: Administer Questions
Present questions Q1-Q5 sequentially (not all at once). After each answer, ask the persona agent to quote the specific dashboard text that supports it. This prevents confabulation and creates an auditable transcript.

### Step 4: Score Transcript
Apply the scoring rubric from Part 2. Score each question independently. Record:
- Raw score (0, 0.5, 1.0) per question
- Total score (0.0 – 5.0)
- Whether Q3 hard-fail condition is triggered
- Which failure modes (FM-1 through FM-5) were observed

Save transcript to: `dashboard/review-council-v7/cold-reader-transcript-YYYYMMDD.md`
Save scores to: `dashboard/review-council-v7/cold-reader-scores-YYYYMMDD.json`

### Step 5: Gate Decision
```
IF total_score >= 4.0 AND q3_score > 0.0:
    PASS → proceed to deployment
ELSE:
    FAIL → apply remediation (Part 5) → re-run gate from Step 1
```

Maximum 2 remediation-and-retest cycles before escalating to human review.

---

## Part 5 — Remediation Protocol

Each missed question maps to specific dashboard elements to fix. Do not regenerate the entire dashboard — make targeted edits only.

### Q1 missed (research question unclear)
**Fix:** Add or revise the dashboard subtitle / hero description. It must contain this sentence or equivalent:
> "This study evaluates whether existing LLM benchmarks claiming to assess religious values actually test what they claim — a meta-evaluation of 401 candidates across 14 traditions."

Required location: Hero section, visible without scrolling. Subtitle under the dashboard title.

### Q2 missed (most important finding not identified as C8)
**Fix:** Add a hero stat card displaying:
> "Mean values relevance score: **30 / 100**  
> Most benchmarks do not test religious values. (d = -1.23, p < 0.001)"

Required location: First visible panel before any other claim summaries. If a claims summary grid exists, C8 must be listed first (or visually highlighted as the primary finding with a colored border or badge).

### Q3 missed (cross-vendor data believed real)
**Fix:** This is the highest-priority fix. Add a persistent banner or alert box to the cross-vendor section:
> "**Data provenance notice:** OpenAI and Gemini results are Claude-simulated (Claude Sonnet/Haiku roleplay), not real API calls to those vendors. Treat as indicative only."

Required location: Immediately above or within the cross-vendor comparison chart — not in a footnote, not in a collapsed caveat panel. The banner must be visible without any interaction. Font size >= body text, distinct background color (warning amber or equivalent).

### Q4 missed (no caveats found or too vague)
**Fix:** Add an open-by-default "Methodological Caveats" panel. Each caveat must have:
- A short bold title
- One to two sentence plain-English description
- Which specific numbers it affects

Required minimum content:
1. **T2 blinding asymmetry** — Claude's T2 scores (100%) were obtained with gold answers visible; blind protocol used for cross-vendor trials. Claude scores are upper-bound estimates.
2. **Same-vendor scorer bias** — Claude Opus 4.6 scored all rubric responses including its own family's outputs. Scores for Claude models may be inflated.
3. **Gemini data provenance** — Gemini results used template extraction, not interactive API. Low scores (0.0 on K/R/V) may reflect the protocol, not genuine capability.

Required location: Above the fold of the cross-vendor section, or as a persistent sidebar card. Not collapsed by default.

### Q5 missed (zero-coverage traditions not enumerable)
**Fix A — if Islam not identified as most-covered:** Add a callout to the tradition distribution chart:
> "Islam: 28 of 47 gate-passing benchmarks (60%)"

**Fix B — if zero-coverage traditions not listable:** Add an enumeration table or bullet list:
> "Traditions with zero viable benchmarks (8 of 14): Judaism, Jainism, Taoism, Shinto, Ubuntu Philosophy, Indigenous Spirituality, Baha'i, Zoroastrianism"

Required location: Visible within the tradition coverage section without requiring tooltip hover or expanding an accordion.

---

## Part 6 — Passing Criteria Checklist (Pre-Test Verification)

Before administering the cold-reader test, verify the following dashboard elements exist and are visible (not hidden, not collapsed, not tooltip-only):

- [ ] Hero description states "meta-evaluation" or equivalent plain-English framing
- [ ] C8 values relevance failure (mean 30/100) visible in the first viewport
- [ ] Cross-vendor simulation disclosure is a persistent visible banner (not footnote)
- [ ] K/R/V abbreviations are glossed on first use with a visible legend
- [ ] T1 and T2 are glossed on first use with plain-English descriptions
- [ ] "fara'id" is glossed as "Islamic inheritance law" on first use
- [ ] All 8 claims are listed/indexed (not just referenced by number)
- [ ] All 8 zero-coverage traditions are enumerated (not just counted)
- [ ] Caveats panel is open by default and above the cross-vendor comparison

If any checklist item is unchecked, fix it before administering the gate. The pre-test checklist is not a substitute for the gate — both must pass.

---

*Plan authored: 2026-04-13. Gate version: v7.0. Next review after first cold-reader run.*
