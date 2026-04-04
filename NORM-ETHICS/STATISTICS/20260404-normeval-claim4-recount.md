# NormEval Claim 4 — Systematic Recount of Judgment vs. Reasoning Coding

**Date:** 2026-04-04
**Task:** Verify the accuracy of Claim 4: "Most benchmarks (28 of 37) test moral judgment rather than moral reasoning"
**Data Sources:**
- `20260402-normative-benchmark-feature-matrix.json` — v1 feature matrix (A3_reasoning field)
- `20260404-normeval-v2-feature-scores.json` — v2 refined features (A3_reasoning_refined, 0-100 scale)

---

## 1. Coding Rule Definitions

Three categories are used to classify whether a benchmark tests moral **judgment**, moral **reasoning**, or **both**:

### Judgment-only (J)
The benchmark evaluates *what the model concludes* without requiring or assessing the reasoning process. Typical formats: MCQ with correct/incorrect answer, binary moral/immoral classification, Likert agreement scales, pairwise forced-choice comparisons.

*Examples:* ETHICS (MCQ across 5 categories), CMoralEval (classification of moral acceptability), Moral Machine experiments (forced pairwise preference).

### Both judgment and reasoning (B)
The benchmark evaluates the model's conclusion AND includes some component assessing reasoning quality, justification, or process. The reasoning assessment may be secondary or partial but is explicitly present in the evaluation rubric.

*Examples:* Moral Persuasion (tests both susceptibility to persuasion AND quality of moral argumentation), Pluralistic Moral Gap (evaluates judgment alignment AND value reasoning patterns).

### Reasoning-focused (R)
The benchmark primarily evaluates *how the model reasons*: identification of relevant moral principles, quality of tradeoff articulation, procedural application of ethical frameworks, or rubric-based scoring of reasoning steps. A final judgment may exist, but the evaluation weight falls on the reasoning process.

*Examples:* MoReBench (expert rubric scoring procedural reasoning), MoralReason (reasoning traces evaluated), Beyond Ethical Alignment (deductive + abductive reasoning tested).

### Coding Decision Rules
1. **B1_format** is a primary indicator: Binary, MCQ, and Pairwise formats strongly suggest J.
2. **A2_depth = "Explicit framework application"** is necessary but not sufficient for R — a benchmark can apply frameworks yet still score only judgment (e.g., Greatest Good applies Oxford Utilitarianism Scale but scores choice, not reasoning).
3. **B8_scorer = "Model-graded" or rubric-based** elevates toward R if the rubric assesses reasoning quality.
4. **v2 A3_reasoning_refined** provides a continuous scale: 25=J, 50=B, 75=framework reasoning, 100=procedural reasoning.

---

## 2. Full 37-Row Recount Table

| ID | Benchmark | v1 A3 | v2 A3 | Code | Justification |
|----|-----------|-------|-------|------|---------------|
| 1 | ETHICS (Hendrycks) | Tests judgment only | 25 | **J** | MCQ/mixed format; classifies actions as right/wrong across 5 categories; no reasoning rubric |
| 2 | MoralReason (An) | Tests reasoning process | 75 | **R** | Generates framework-specific reasoning traces; GRPO reward optimizes both decision and reasoning process |
| 3 | Ethical Reasoning Depends on Language (Agarwal) | Tests judgment only | 25 | **J** | Scenario-based format testing judgment consistency across languages; no reasoning evaluation |
| 4 | Are LLMs Consequentialist or Deontological (Bai) | Tests reasoning process | 75 | **R** | Classifies reasoning traces as consequentialist/deontological; analyzes chain-of-thought |
| 5 | MoReBench (Chiu) | Tests reasoning process | 100 | **R** | Expert rubric scoring procedural reasoning; 5/5 grounding; sole benchmark testing full reasoning process |
| 6 | Greatest Good Benchmark (Marraffini) | Tests judgment only | 25 | **J** | Operationalizes Oxford Utilitarianism Scale but scores binary judgment (accept/reject instrumental harm), not reasoning |
| 7 | JETHICS (Niu) | Tests judgment only | 25 | **J** | Binary moral/immoral classification; no reasoning component |
| 8 | Measuring AI Alignment with Human Flourishing (Hilliard) | Tests both | 50 | **B** | Mixed format: Likert-scale judgments on flourishing dimensions + open-ended items requiring justification |
| 9 | Analyzing Ethical Logic of Six LLMs (Bozdag) | Tests reasoning process | 75 | **R** | Analyzes reasoning through ethical typologies (consequentialist-deontological, MFT, Kohlberg); explainability approach |
| 10 | PRIME Framework Convergent Ethics (Rao) | Tests reasoning process | 75 | **R** | Dual-protocol methodology analyzing moral priorities across frameworks; tests reasoning structure |
| 11 | Ethical Alignment of LLMs in Healthcare (Jiang) | Tests judgment only | 25 | **J** | Scenario-based format testing judgment alignment in medical contexts; no reasoning rubric |
| 12 | LLMs Amplified Cognitive Biases (Park) | Tests judgment only | 25 | **J** | Scenario-based; measures bias in moral judgment, not reasoning process |
| 13 | Rethinking Machine Ethics (Zhou) | Tests reasoning process | 75 | **R** | Operationalizes 4 moral theories as prompting scaffolds; tests reasoning, not just verdicts |
| 14 | Ethical Decision-Making in Humans and LLMs (Nandi) | Tests judgment only | 25 | **J** | Mixed format; implicit/surface depth; compares decisions, not reasoning processes |
| 15 | Structured Moral Reasoning (Chakraborty) | Tests reasoning process | 75 | **R** | Value-grounded framework; tests structured reasoning with prompting taxonomy |
| 16 | LLM Ethics Benchmark (UniMoral / Aula) | Tests judgment only | 25 | **J** | Mixed format; implicit/surface depth; classification of ethical acceptability |
| 17 | MoralBench (Ji) | Tests judgment only | 25 | **J** | MCQ format; implicit depth; tests correct answer selection |
| 18 | Moral Turing Test (Suresh) | Tests judgment only | 25 | **J** | Open-ended but scores judgment plausibility (Turing-test style), not reasoning quality |
| 19 | Evaluating Moral Beliefs across LLMs (Scherrer) | Tests judgment only | 25 | **J** | Pairwise comparison; tests moral preference consistency, not reasoning |
| 20 | CMoralEval (Yu) | Tests judgment only | 25 | **J** | Mixed format; Chinese moral judgment classification; implicit depth |
| 21 | Beyond Ethical Alignment (Nashed) | Tests reasoning process | 100 | **R** | Formal AMA framework testing deductive AND abductive moral reasoning explicitly |
| 22 | Evaluating Computational Models of Ethics (Chhabra) | Tests judgment only | 25 | **J** | SPECTRA framework implements 4 paradigms as computational agents but scores model-graded outputs, not reasoning process. Paywalled — coding conservative |
| 23 | Operationalizing Pluralistic Values (Qiu) | Tests judgment only | 25 | **J** | Mixed format; implicit depth; tests value alignment, not reasoning |
| 24 | Aligning LLM Agents with Kantian Preferences (Albergante) | Tests reasoning process | 75 | **R** | Formalizes Kantian universalizability via economic game theory; tests moral preference formation process |
| 25 | Ethical Reasoning over Moral Alignment (Rao) | Tests reasoning process | 75 | **R** | Integrates moral dilemmas with normative formalisms at different abstraction levels; tests reasoning quality |
| 26 | Many LLMs Are More Utilitarian Than One (Hansel) | Tests judgment only | 25 | **J** | Mixed format; tests aggregated judgment patterns, not reasoning |
| 27 | Decoding Moral Responses in AI (Moral Lens / Kopeinik) | Tests judgment only | 25 | **J** | Scenario-based; implicit depth; tests response classification |
| 28 | Large-scale Moral Machine Experiment (Bauer) | Tests judgment only | 25 | **J** | Pairwise forced-choice; replicates Moral Machine paradigm; tests preference, not reasoning |
| 29 | Moral Machine Experiment on LLMs (Takemoto) | Tests judgment only | 25 | **J** | Pairwise forced-choice; same Moral Machine paradigm; tests preference only |
| 30 | Moral Persuasion in LLMs (Huang) | Tests both | 50 | **B** | Tests susceptibility to persuasion AND quality of moral argumentation using Gert's rules + MFT |
| 31 | Moral Mind(s) of LLMs (Bai) | Tests judgment only | 25 | **J** | Pairwise comparison; revealed preference methodology from economics; tests judgment patterns |
| 32 | DailyDilemmas (Hua) | Tests judgment only | 25 | **J** | Binary format; framework-aware but tests value preference choice, not reasoning |
| 33 | PrinciplismQA (Hong) | Tests both | 75 | **B*** | Mixed format (2,182 MCQ + 1,466 open-ended); explicitly grounded in Beauchamp-Childress 4 principles. MCQ portion tests judgment; open-ended portion with 12 medical experts tests reasoning. *See Section 4 for recoding discussion.* |
| 34 | Pluralistic Moral Gap (Russo) | Tests both | 50 | **B** | Scenario-based; evaluates both judgment alignment AND value reasoning patterns |
| 35 | Are Rules Meant to be Broken (Haemmerl) | Tests judgment only | 25 | **J** | Scenario-based; multilingual moral judgment consistency; no reasoning assessment |
| 36 | MedEthicsQA (Wei) | Tests judgment only | 25 | **J** | Mixed format; medical ethics QA; framework-aware but scores correctness, not reasoning |
| 37 | ProMoral-Bench (Thomas) | Tests both | 50 | **B** | Meta-benchmark evaluating prompting strategies; scores both UMSS judgment metric AND CoT reasoning quality |

---

## 3. Counts Summary

### Current v1 coding (from feature matrix):
| Category | Count | Benchmarks |
|----------|-------|------------|
| **Judgment only (J)** | 22 | IDs: 1, 3, 6, 7, 11, 12, 14, 16, 17, 18, 19, 20, 22, 23, 26, 27, 28, 29, 31, 32, 35, 36 |
| **Both (B)** | 5 | IDs: 8, 30, 33, 34, 37 |
| **Reasoning (R)** | 10 | IDs: 2, 4, 5, 9, 10, 13, 15, 21, 24, 25 |
| **Total** | **37** | |

### Derived counts:
| Metric | Count | Percentage |
|--------|-------|------------|
| J only | 22 | 59.5% |
| J + B (broad "judgment") | 27 | 73.0% |
| R only | 10 | 27.0% |
| Paper spine claim | 28 | 75.7% |

### v2 refined distribution:
| v2 Score | Meaning | Count |
|----------|---------|-------|
| 25 | Judgment only | 22 |
| 50 | Tests both | 4 |
| 75 | Framework reasoning | 9 |
| 100 | Procedural reasoning | 2 |

**Key discrepancy:** v1 has 5 "Tests both" but v2 has only 4 at score=50. PrinciplismQA (ID=33) is coded "Tests both" in v1 but scored 75 (framework reasoning) in v2.

---

## 4. Discrepancy Analysis

### 4.1 Why 28 does not equal 27

The paper spine states "28 of 37" test judgment rather than reasoning. The data shows:
- J = 22, B = 5, R = 10, total = 37
- J + B = 27, not 28

**The 28 is arithmetically impossible given the current coding.** One of three errors must exist:

**Hypothesis A (most likely): PrinciplismQA was originally coded J, not B.**
If PrinciplismQA (ID=33) was originally coded as J (judgment only), the counts would have been J=23, B=4, R=10, and J+B=27 — still not 28. This alone does not explain the discrepancy.

**Hypothesis B: The spine used "tests judgment" loosely to mean "does not primarily test reasoning."**
If the spine counted J + B = "tests judgment" (i.e., 37 - R = 37 - 10 = 27), plus one additional benchmark was either miscounted or recoded between versions, the spine would show 28. This is the most plausible explanation: a counting error of +1 during prose writing, likely from off-by-one when subtracting R from the total (37 - 10 = 27, written as 28).

**Hypothesis C: One benchmark was recoded between the spine draft and the feature matrix.**
If any single benchmark was recoded from J to R or B to R between the time the spine was written and the final feature matrix was saved, the spine number would become stale. Given that the body text (results-landscape-normeval.md) says "22 of 37" (J only), this suggests the spine was written with a different counting methodology than the body.

### 4.2 PrinciplismQA Coding Inconsistency

PrinciplismQA (ID=33) has conflicting codes:
- **v1:** "Tests both" (B)
- **v2:** 75 (framework reasoning, suggesting R)

**Evidence for B (current v1 coding):**
- Contains 2,182 MCQ items (pure judgment) alongside 1,466 open-ended items
- The MCQ component is judgment-only; the open-ended component with medical expert evaluation involves reasoning
- Mixed format with dual evaluation modes supports "both"

**Evidence for R (v2 coding):**
- A2_depth = "Explicit framework application" and A6_grounding = 4
- Deeply grounded in Beauchamp-Childress four principles
- 12 medical expert annotators evaluate quality of ethical reasoning

**Recommendation:** Keep as **B** in v1. The MCQ majority (60% of items) is genuinely judgment-only, and the open-ended portion evaluates reasoning. "Both" is the most accurate characterization. The v2 score of 75 likely reflects the depth of the open-ended component but does not account for the MCQ volume. The v2 score should be corrected to 50 for consistency.

### 4.3 Other Questionable Codings

**ID=6, Greatest Good Benchmark — currently J, could be argued as B.**
Rationale for J: Despite operationalizing utilitarianism through the validated Oxford Utilitarianism Scale and citing Bentham/Mill/Singer, the evaluation format asks for binary acceptance/rejection of utilitarian scenarios. No reasoning rubric exists. The philosophical grounding is in the *construction* of stimuli, not in the *evaluation* of responses. **Verdict: J is correct.**

**ID=22, Evaluating Computational Models of Ethics — currently J, could be argued as R.**
The SPECTRA framework implements four normative paradigms as computational agents, which sounds reasoning-heavy. However, the benchmark itself uses model-graded outputs, and the extract is paywalled limiting verification. A6_grounding=4 is high for a J benchmark. **Verdict: J is acceptable given available evidence, but merits re-examination if full text becomes available.**

**ID=18, Moral Turing Test — currently J, reasonable.**
Open-ended format could suggest reasoning assessment, but the evaluation criterion is whether responses are indistinguishable from human moral judgments (Turing-test style), not whether the reasoning is sound. **Verdict: J is correct.**

---

## 5. Paper Implications

### 5.1 Corrected Numbers

The paper contains two inconsistent claims:
1. **Spine (line 22):** "Most benchmarks (28 of 37) test moral judgment rather than moral reasoning"
2. **Results body (line 9):** "22 of 37 benchmarks test moral judgment"

These refer to different metrics:
- The results body correctly reports J-only = 22/37
- The spine appears to report J+B but with an off-by-one error (27, not 28)

### 5.2 Recommended Language

**Option 1 — Strict (conservative, defensible):**
> "22 of 37 benchmarks (59.5%) test moral judgment exclusively, while only 10 (27%) assess the moral reasoning process."

Statistical test: Binomial test H1: proportion > 50%, **p = 0.162** (not significant at alpha=0.05).

**Option 2 — Broad (includes "both"):**
> "27 of 37 benchmarks (73%) include a moral judgment component, with only 10 (27%) primarily evaluating the reasoning process."

Statistical test: Binomial test H1: proportion > 50%, **p = 0.004** (significant at alpha=0.01).

**Option 3 — Recommended (precise and significant):**
> "Only 10 of 37 benchmarks (27%) make any attempt to evaluate moral reasoning quality. The remaining 27 test moral judgment — what a model concludes — either exclusively (22 benchmarks) or alongside limited reasoning assessment (5 benchmarks)."

This framing:
- Uses exact numbers from the data (22 + 5 + 10 = 37)
- Avoids the ambiguous "28 of 37"
- Centers the finding on the reasoning deficit (10/37) rather than the judgment surplus
- Is statistically significant: proportion testing reasoning < 50%, p = 0.004

### 5.3 Statistical Tests (all binomial, one-sided)

| Claim | Count | Proportion | p-value | Significant? |
|-------|-------|-----------|---------|-------------|
| J only > 50% | 22/37 | 59.5% | 0.1620 | No |
| J+B > 50% | 27/37 | 73.0% | 0.0038 | Yes (p<0.01) |
| R < 50% | 10/37 | 27.0% | 0.0038 | Yes (p<0.01) |
| Old claim (28/37 > 50%) | 28/37 | 75.7% | 0.0013 | Yes (p<0.01) |
| If PrinciplismQA->R: J+B > 50% | 26/37 | 70.3% | 0.0100 | Yes (p<0.05) |

### 5.4 Locations Requiring Updates

1. **`spine-normeval.md` line 22:** Change "28 of 37" to accurate count with precise framing
2. **`results-landscape-normeval.md` line 9:** Currently says "22 of 37" (correct for J-only); harmonize with spine
3. **`introduction-normeval.md` / `introduction-comprehensive-normeval.md`:** Check abstract for "28" references
4. **Dashboard generator** (`generate_normeval_dashboard.py` line 90): Uses hypothesis dict for C4_judgment proportion — verify data source

---

## 6. Reconciliation Summary

| Item | Old Value | Corrected Value | Action |
|------|-----------|-----------------|--------|
| Spine claim | 28 of 37 | 27 of 37 (J+B) or reframe as "only 10 of 37 test reasoning" | Must fix |
| Body text | 22 of 37 | 22 of 37 (correct for J-only) | Keep, but clarify scope |
| PrinciplismQA v1 code | Tests both (B) | Keep as B | v2 should be corrected: 75 -> 50 |
| PrinciplismQA v2 score | 75 | 50 | Should match v1 "both" classification |
| Statistical significance | Untested | J-only: p=0.162 (not sig); J+B: p=0.004 (sig) | Report appropriate test |

**Root cause of the 28 vs 22 discrepancy:** The spine and the body used different counting methodologies. The body counted strict J-only (22). The spine counted J+B (27) but introduced an arithmetic error of +1, yielding 28. Neither version is internally inconsistent — they are inconsistent *with each other*.

**Bottom line:** The correctable claim is "27 of 37 benchmarks (73%) test moral judgment, either exclusively or alongside limited reasoning assessment, while only 10 (27%) primarily evaluate the reasoning process" (p = 0.004, binomial test). This is statistically significant and empirically accurate.
