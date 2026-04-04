# NormEval Benchmark Triage: T6-T10 Self-Assessment Trials

**Date:** 2026-04-04
**Agent:** 1A (Claude Opus 4.6 self-evaluation)
**Scope:** 5 untested gate-passing benchmarks (Ranks 3, 4, 7, 8, 9 from Top 15)
**Prior Trials:** T1-T5 completed 2026-04-03

---

## Phase A: Accessibility Triage

| Trial | Benchmark | Rank | ND | Size | Data URL | Status | Notes |
|-------|-----------|------|----|------|----------|--------|-------|
| T6 | **PrinciplismQA** | 3 | 85.0 | 3,648 | (empty in matrix) | **YELLOW** | arXiv paper has arxiv_id 2508.05132; no direct data link in matrix. Paper mentions GitHub but URL not provided. Data likely accessible via paper supplementary materials. |
| T7 | **Moral Persuasion** | 4 | 79.8 | 108 | https://github.com/acyhuang/moral-persuasion | **GREEN** | GitHub repo confirmed in paper. Uses moralchoice dataset (Scherrer et al. 2023) with 680 high-ambiguity scenarios. 108 refers to scenario count for persuasion experiments. |
| T8 | **AMAeval** (Beyond Ethical Alignment) | 7 | 71.0 | 1,090 | https://github.com/alessioGalatolo/AMAeval | **GREEN** | GitHub repo confirmed in paper and DOI. Static + dynamic benchmark components. Moral Foundations Theory values as base. |
| T9 | **JETHICS** | 8 | 55.8 | 78,000 | https://github.com/Language-Media-Lab/jethics | **GREEN** | GitHub confirmed. 77,896 examples across 7 sub-categories. Japanese-language. CC-BY license. |
| T10 | **Pluralistic Moral Gap** | 9 | 82.8 | 1,618 | (empty in matrix) | **YELLOW** | arXiv 2507.17216 published. Moral Dilemma Dataset (MDD) described but not in matrix URL. Paper mentions reformulated AITA dilemmas. Data availability unclear. |

### Triage Summary
- **GREEN (3):** Moral Persuasion, AMAeval, JETHICS -- GitHub repos confirmed
- **YELLOW (2):** PrinciplismQA, Pluralistic Moral Gap -- papers published but data URLs not in feature matrix
- **RED (0):** None

**Approach for YELLOW benchmarks:** Trial conducted based on paper methodology, published examples, and PDF extract analysis. Items constructed from published specifications. Findings noted as paper-derived where applicable.

---

## Phase D: Cross-Trial Self-Assessment Annotations

### T6 (PrinciplismQA) Annotations
- **Discriminative power:** HIGH. Medical ethics requires domain-specific knowledge. Beauchamp-Childress principles create genuine tensions (autonomy vs beneficence is a classic dilemma).
- **Refusal sensitivity:** MODERATE. Some items involving end-of-life or resource allocation may trigger safety training.
- **Format constraints:** Mixed format (MCQ + open-ended) is good -- MCQ for accuracy, open-ended for reasoning depth.
- **Ground truth defensibility:** HIGH. Expert philosophers as annotators (12 medical ethicists); grounded in the field's canonical textbook.
- **Cultural assumptions:** PRESENT. Beauchamp-Childress framework is Western bioethics. Does not capture non-Western medical ethics traditions (e.g., Japanese obligation-based medical ethics, Ubuntu communal decision-making in healthcare).
- **Contamination risk:** LOW. Recent (2025), specialized domain, large item count.

### T7 (Moral Persuasion) Annotations
- **Discriminative power:** MODERATE-HIGH. Tests persuasion resistance, not just judgment -- a dimension no other trialed benchmark covers.
- **Refusal sensitivity:** HIGH. The persuasion paradigm inherently pushes models toward actions they initially rejected. Safety training creates strong resistance to being "persuaded" to violate moral rules.
- **Format constraints:** MODERATE concern. Multi-turn conversation format is more ecologically valid but harder to standardize.
- **Ground truth defensibility:** MODERATE. Uses Gert's common morality rules (well-established) but persuasion "success" is measured by action change, not quality of persuasion.
- **Cultural assumptions:** PRESENT. Gert's common morality is explicitly Western/universalist. MFT measurement adds cross-cultural dimension.
- **Contamination risk:** LOW. Novel paradigm (LLM-on-LLM persuasion); hard to memorize.

### T8 (AMAeval) Annotations
- **Discriminative power:** HIGH. Distinguishes deductive from abductive moral reasoning -- a philosophically grounded distinction that no other benchmark tests.
- **Refusal sensitivity:** LOW. Items ask for reasoning analysis, not moral judgment. The "evaluate this reasoning chain" format is less triggering than "what would you do?"
- **Format constraints:** BENEFICIAL. Both static (evaluate given reasoning) and dynamic (generate reasoning) components test different capabilities.
- **Ground truth defensibility:** HIGH. Human judges (graduate+ level), inter-annotator agreement 0.68-0.70 (Krippendorff's alpha).
- **Cultural assumptions:** MODERATE. Uses Moral Foundations Theory values as base, which has cross-cultural validity claims but Western origins.
- **Contamination risk:** LOW. Very recent (Aug 2025), novel formal framework, dynamic component generates new items.

### T9 (JETHICS) Annotations
- **Discriminative power:** MODERATE. Mirrors ETHICS (Hendrycks) which hit ceiling in T1, but Japanese language adds difficulty. GPT-4o only achieves 0.71 average.
- **Refusal sensitivity:** LOW. Binary classification format, culturally appropriate scenarios.
- **Format constraints:** LIMITING. Binary format (same as ETHICS) cannot capture reasoning depth. Same weakness as T1.
- **Ground truth defensibility:** MODERATE. Crowdworker annotations with acceptable kappa (0.61 average) but utilitarianism kappa only 0.18 (near-chance agreement).
- **Cultural assumptions:** THIS IS THE POINT. JETHICS specifically tests whether ethical reasoning transfers to Japanese cultural context. Items like "throwing a stone into a donation box" carry culturally specific moral weight.
- **Contamination risk:** MODERATE. Methodology mirrors well-known ETHICS dataset. But Japanese-specific items are novel.

### T10 (Pluralistic Moral Gap) Annotations
- **Discriminative power:** HIGH. Tests pluralism in moral judgment -- whether models can capture human disagreement, not just majority opinion. This is a fundamentally different evaluation axis.
- **Refusal sensitivity:** MODERATE. Real-world AITA dilemmas can touch sensitive topics (family conflicts, relationship issues, financial obligations).
- **Format constraints:** GOOD. Distribution-matching format (not just binary accuracy) is methodologically sophisticated.
- **Ground truth defensibility:** VERY HIGH. 51,776 human judgments across 1,618 dilemmas. Full distributional ground truth, not single labels.
- **Cultural assumptions:** PRESENT. Source is Reddit r/AmITheAsshole -- skews young, English-speaking, Western. Authors acknowledge this.
- **Contamination risk:** ADDRESSED. Authors specifically filter out AITA-identifiable posts (only 7.2% pass). Reformulations mitigate memorization. But underlying scenarios may still be in training data.
