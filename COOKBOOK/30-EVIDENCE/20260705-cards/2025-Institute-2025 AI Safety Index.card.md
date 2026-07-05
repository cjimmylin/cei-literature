---
stem: "2025-Institute-2025 AI Safety Index"
reader_model: "sonnet"
confidence: "low"
is_benchmark: false
theme_tags: [ai-lab-practices, best-practices]
task_format: "n/a"
scoring_type: "rubric"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Seven GPAI companies evaluated: Anthropic, OpenAI, Google DeepMind, x.AI, Meta, Zhipu AI, Deepseek (p.2)"
  - "34 indicators of responsible conduct assessed across 6 domains (p.2)"
  - "Control-Problem strategies found inadequate for all companies evaluated (p.1)"
---
## 1. Gist
This is an executive summary (2-page extract) of the Future of Life Institute's Summer 2025 AI Safety Index, a periodic independent expert panel evaluation of safety practices at leading general-purpose AI (GPAI) companies. The index evaluates seven major AI companies — Anthropic, OpenAI, Google DeepMind, x.AI, Meta, Zhipu AI, and Deepseek — across six critical domains and 34 indicators, using a US GPA letter-grade system. The summary's key finding is that, despite some modest progress, no company has robust plans to ensure public safety, the control-loss risk remains effectively unaddressed, and companies have abandoned previous voluntary safety commitments, highlighting the need for third-party validation and binding oversight. For values-alignment benchmarking, this document represents one instantiation of external structured evaluation of AI lab practices against safety criteria — useful as a reference for what governance-oriented "lab practices" evaluation looks like at scale.

## 2. Benchmark/eval design features
This is an expert-panel evaluation, not an AI system benchmark. Core features:
- Seven GPAI companies evaluated: Anthropic, OpenAI, Google DeepMind, x.AI, Meta, Zhipu AI, Deepseek.
- Six critical domains assessed (specific domain names not listed in the 2-page extract).
- 34 indicators of responsible conduct; each receives a letter grade from panel members.
- Evidence base combines publicly available material (research papers, policy documents, news articles, industry reports) plus a tailored industry survey that companies could complete to increase transparency.
- Independent review panel of six experts: Dylan Hadfield-Menell (MIT), Jessica Newman (UC Berkeley), David Krueger (U Montreal / Mila), Tegan Maharaj (HEC Montréal / Mila), Sneha Revanur (Encode Justice), Stuart Russell (UC Berkeley).
- Grading uses US GPA system: A+ (4.3) through F (0.0).
- Full report available at futureoflife.org/index-s25 (not in extract).

## 3. Task format & example item
n/a — expert panel evaluation of institutional safety practices; no item-level prompts or tasks administered to AI models.

## 4. Scoring / grading methodology
US GPA letter-grade system (A+, A, A–, B+, ..., F) corresponding to numerical values 4.3, 4.0, 3.7, 3.3, ..., 0. Panel members contribute letter grades, brief justifications, and improvement recommendations for each indicator. Aggregation method not described in the 2-page extract.

## 5. Dataset construction & provenance
Evidence sourced from: (1) publicly available material including research papers, policy documents, news articles, and industry reports; (2) a tailored industry survey companies could optionally complete. The survey allows companies to increase transparency but is not mandatory, introducing potential selection bias.

## 6. Validity evidence
Not assessable from this 2-page extract. The full report would be needed for inter-rater reliability, panel deliberation protocols, and validity claims. The extract notes that the review panel "volunteered" their time and that the evaluation was independent of the companies.

## 7. Saturation / discrimination
Not applicable at the summary level. The extract reports that large disparities remain across companies in risk management practices, suggesting meaningful discrimination between companies on some indicators. All companies were found inadequate on control-loss risk, implying a floor effect on that domain.

## 8. Multiturn / agentic aspects
Not directly evaluated in this framework — the evaluation assesses institutional safety practices, not model behavior in interactive settings.

## 9. Key numbers
- 7 GPAI companies evaluated (p.2)
- 6 critical domains assessed (p.2)
- 34 indicators of responsible conduct (p.2)
- 6 independent review panel members (p.2)
- GPA scale: A+ = 4.3, F = 0 (p.1)
- All companies found inadequate on control-loss risk strategies (p.1)

## 10. Pitfalls & limitations
- The 2-page extract contains only an executive summary; the full methodology, per-indicator grades, and detailed findings are not available for review.
- Companies' voluntary participation in the industry survey creates selection bias — companies with stronger safety practices may be more willing to complete it.
- The extract notes companies "had abandoned previous voluntary commitments," suggesting that self-reported or voluntary data may not be reliable.
- The panel's grading is subjective expert judgment; without inter-rater reliability data, consistency across panel members is unknown.
- Coverage is limited to seven companies (all English-language-dominated Western or Chinese AI labs), excluding many AI developers globally.
- The index is periodic (not continuous), so it cannot capture rapid changes in safety practices between evaluation cycles.

## 11. Novel ideas worth stealing
1. **Multi-indicator rubric grading for institutions**: The 34-indicator, 6-domain structure with letter grades is a reusable template for designing structured rubrics to evaluate AI lab safety practices. Benchmarks for AI ethics governance could adapt this structure.
2. **Voluntary-plus-public evidence base**: Combining what companies voluntarily disclose with independent public evidence creates a dual-source evaluation that is harder to game than self-report alone.
3. **Named independent panel**: Publishing the names and affiliations of evaluators increases accountability and interpretability of the resulting grades. Values-alignment benchmark governance should consider similar transparency.
4. **Explicit focus on control-loss risk as a domain**: Treating loss-of-human-control as a distinct, separately graded domain — not subsumed under general "safety" — is a design choice that highlights alignment-specific concerns.

## 12. Notable quotes
- "None have robust, reliable, plans for ensuring the public remains safe from their products." (p.1)
- "The Control-Problem remains unsolved: Despite their explicit ambitions to develop artificial general intelligence (AGI) capable of rivaling or exceeding human intelligence and replacing humans, the review panel again found the current strategies of all companies inadequate for ensuring that these systems remain safe and under human control." (p.1)
- "The report showed how companies had abandoned previous voluntary commitments, highlighting a need for third party validation of risk assessments and legally binding oversight with enforcement mechanisms." (p.1)
- "Just as functioning breaks give drivers the confidence to accelerate, effective AI safety measures give society the confidence to innovate and adopt AI." (p.2)

## 13. UNKNOWN / not in extract
- The six specific domains used for evaluation (names not listed in 2-page extract).
- Per-company grades on any indicator or domain.
- The 34 specific indicators assessed.
- The full methodology for aggregating panel member grades.
- Any inter-rater reliability or calibration process for the panel.
- Whether the industry survey was completed by each company and to what extent.
- Results for specific model capabilities (the index evaluates company practices, not specific model behaviors).
