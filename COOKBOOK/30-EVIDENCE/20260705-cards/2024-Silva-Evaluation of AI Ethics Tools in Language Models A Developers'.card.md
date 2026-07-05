---
stem: "2024-Silva-Evaluation of AI Ethics Tools in Language Models A Developers'"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [ai-lab-practices, design-space, normative-ethics, validity-psychometrics]
task_format: "n/a"
scoring_type: "human-rating"
dataset_size: 11
dataset_construction: "survey-derived"
languages: ["pt", "en"]
models_tested: []
headline_numbers:
  - "213 AIETs found in literature survey (Jan 2019–Jul 2023), filtered to 8, final 4 selected (p.7)"
  - "Harms Modeling rated best for identifying risks: avg. 4.67/5 by CAPIVARA developers (p.18)"
  - "Model Cards rated best for stakeholder documentation: 90% of interview developers chose it (p.22)"
  - "35 total interview sessions with 11 developers across 4 Portuguese LMs (p.9)"
  - "100% of general interview developers had NOT previously ethically evaluated their model (p.22)"
---
## 1. Gist
This paper evaluates four AI Ethics Tools (AIETs) — Model Cards, ALTAI, FactSheets, and Harms Modeling — applied to Portuguese-language large language models through structured developer interviews. It is the first empirical study assessing AIETs' usability and effectiveness from a developer perspective. The study identifies that generic AIETs serve adequately as ethical reflection guides but fail to capture language-model-specific risks such as idiomatic bias or cultural under-representation. For values-alignment benchmarking, this paper directly informs the design of developer-facing ethics assessment frameworks and reveals gaps in current tooling that new benchmarks should address.

## 2. Benchmark/eval design features
This is a qualitative case study, not a benchmark itself. Core contributions:
- Comprehensive literature survey identifying 213 AIETs (updated to 288 by March 2025).
- Structured methodology for AIET selection using six criteria: AI lifecycle stage, technical vs. reflective nature, feasibility for LMs, recency, target audience, and ethical principles covered.
- Developer evaluation questionnaire with agree/disagree Likert items, general classification questions, and a 5-point rating scale.
- Risk identification questionnaire based on 21 risks from Weidinger et al. plus three Portuguese-specific risks.
- Case study design: pilot with CAPIVARA model (all 4 AIETs), then 4 anonymous Portuguese LMs (Model Cards + Harms Modeling only).

## 3. Task format & example item
n/a — qualitative interview study. Developers answered the AIET questionnaires verbally in Portuguese; researchers filled in AIET documentation. Post-interview questionnaire was self-administered.

Example questionnaire statement (p.13):
> "The AIET is easy to use/answer" [Agree / Weakly agree / Neutral / Weakly disagree / Disagree]

## 4. Scoring / grading methodology
Developers rated each AIET on a 5-point scale. Likert agree/disagree proportions are reported as bar charts. General questions were multiple choice (e.g., "which AIET would you prefer to use again?"). Risk identification used forced choice among AIETs or "None." Inter-developer disagreement within the same group was documented (see Table 10).

## 5. Dataset construction & provenance
- 11 developers (4 groups of 2, 2, 3, 4) from 4 anonymous Portuguese LMs.
- Interviews conducted remotely via Google Meet, June–July 2024, recorded and transcribed.
- Pilot: 3 developers from CAPIVARA model.
- Research Ethics Committee approval obtained.
- Participant identities kept anonymous; demographic data not collected (small population risk of identification).

## 6. Validity evidence
- Pilot study (CAPIVARA) served as methodology test before the main study.
- Results for CAPIVARA (where ALTAI and FactSheets were also included) align with the main study direction, providing cross-validation.
- Application order of AIETs was randomized across groups to control for order effects.
- Author notes potential bias in CAPIVARA results since those developers had contact with the research team.
- No IRR computed across interviews; qualitative results rely on percentage reporting.

## 7. Saturation / discrimination
Small sample (11 developers, 4 models). Wide disagreement within groups about risk presence (Table 10) suggests the AIETs do not drive convergent risk identification even among developers of the same model. ALTAI scored 2/5 vs. Harms Modeling 4.67/5 in pilot — good discrimination between tools. In main study, Model Cards (4.1) vs. Harms Modeling (3.6) shows more compressed spread.

## 8. Multiturn / agentic aspects
n/a — interviews are conducted in multiple sessions per model (one per AIET), but this is a social science methodology, not an agentic AI evaluation.

## 9. Key numbers
- 213 AIETs surveyed (Jan 2019–Jul 2023); 288 with update to March 2025 (p.7)
- Final 4 AIETs evaluated: Model Cards, ALTAI, FactSheets, Harms Modeling (p.8)
- 35 total interview sessions (p.9)
- CAPIVARA scores: Harms Modeling 4.67, Model Cards 4.33, FactSheets 3.67, ALTAI 2.0 (p.18)
- Main study scores: Model Cards 4.1, Harms Modeling 3.6 (p.22)
- Model Cards received 100% agreement on ease-of-use in main study (p.20)
- 80% of main developers preferred Model Cards for re-use (p.22)
- 90% chose Model Cards for most informative stakeholder documentation (p.22)
- 100% of main developers had never ethically evaluated their model before (p.22)
- 66.7% of CAPIVARA developers said no AIET helped them identify risks of malicious use (p.18)
- ALTAI application time: 3h; Harms Modeling: 4h; Model Cards: 2h; FactSheets: 2h (p.10)

## 10. Pitfalls & limitations
- Very small sample (11 developers, 4 models) — results not statistically generalizable.
- Only Portuguese-language LMs tested; cultural/language specificity may not transfer.
- Only use-stage AIETs selected; no coverage of design/testing stage ethics tools.
- Reliance on closed questionnaire limits capture of nuanced developer perspectives.
- CAPIVARA pilot introduces bias since those developers were affiliated with the research team.
- All 4 AIETs fall in the checklist/questionnaire category — no testing of more computational/technical AIETs.
- AIETs evaluated are all English-language, applied in Portuguese via translation — readability issues for non-English speakers (especially ALTAI).
- Developers themselves flagged that use-stage-only AIETs are insufficient; ethics needs to be integrated earlier in development.

## 11. Novel ideas worth stealing
- **Risk taxonomy as evaluation scaffold**: Using the Weidinger et al. 21-risk taxonomy as the ground truth for what AIETs should surface is a transferable pattern — any new benchmark evaluation suite could use this to measure coverage completeness.
- **Order-effect control**: Randomizing AIET application order across groups controls for anchoring and learning effects — important for any multi-tool comparison study.
- **Language-specific risk additions**: Adding three Portuguese-specific risks (cultural representation, Portuguese-speaking population representation, Portuguese language performance) beyond the standard 21-risk list demonstrates how benchmark designers should extend generic taxonomies with domain/language-specific items.
- **Developer-perspective gap analysis**: Showing that developers do not spontaneously conduct ethical review (100% of main participants) establishes a baseline for measuring whether tooling actually changes behavior — a useful pre-post design for benchmark validation studies.
- **Documentation quality as a separate dimension from risk identification**: Model Cards excels at stakeholder documentation; Harms Modeling excels at risk identification. This two-dimensional separation (internal clarity vs. external communication) is worth preserving in benchmark design.

## 12. Notable quotes
- "According to 66.7% of the developers, no AIET has led to the discussion of harms related to malicious uses of the technology, such as encouraging unethical actions, reducing the cost of disinformation campaigns, facilitating fraud and impersonation scams, and generating code for malicious or unethical use." (p.18)
- "The specific risks for the Portuguese language model ... according to 66.7% of the developers, were not addressed by any AIET, showing that generalist AIETs may not map specific risks in an AI." (p.18)
- "It is not yet natural for developers to add a step to ethically analyze their models before publishing them, showing the need for greater engagement and dissemination in the area of AI ethics." (p.22)
- "Harms Modeling, although more complete in terms of subject matter, always seemed very general to me, which ended up being an evaluation of the technology rather than the models themselves." (p.23)

## 13. UNKNOWN / not in extract
- Which specific Portuguese language models were interviewed (names withheld for confidentiality).
- Full text of the Harms Modeling documentation generated for each model.
- Full AIET comparison tables from Appendices A and B (AIETs released to March 2025).
- Inter-rater reliability of the researcher-completed AIET documentation itself.
- Whether developers' reported willingness to use AIETs again translated to actual adoption post-study.
