---
stem: "2025-McGregor-BenchRisk Identifying 57 Failure Modes in AI Safety Benchmarks"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, validity-psychometrics, contamination-robustness, saturation-discrimination]
task_format: "n/a"
scoring_type: "rubric"
dataset_size: 26
dataset_construction: "hand-authored"
languages: [en]
models_tested: []
headline_numbers: ["57 failure modes and 196 mitigations identified across 26 benchmarks (p.1)", "All 26 benchmarks present significant risk in >=1 of 5 dimensions (p.1)", "5-rater BBQ scoring Fleiss' kappa 0.53 (moderate) (p.7)", "Longevity worst dimension; only AILuminate (75) and ARC-AGI-Private (52) high (p.8)", "16 of 26 benchmarks left Failure Mode #002 (task too broadly defined) unmitigated (p.9)"]
---
## 1. Gist
BenchRisk is a metaevaluation benchmark — a "benchmark for benchmarks" — that applies NIST-style risk management to LLM safety/evaluation benchmarks. Through iterative reading of 26 popular benchmarks, the authors catalogued 57 failure modes and 196 mitigations, scoring each benchmark across five reliability dimensions (comprehensiveness, intelligibility, consistency, correctness, longevity). It matters for values-alignment benchmarking because it provides a structured, reusable checklist of what makes an eval trustworthy for real-world decisions, and empirically shows that even flagship safety/ethics benchmarks (ETHICS, BBQ, TruthfulQA, RealToxicityPrompts, Machiavelli) have serious unmitigated reliability risks.

## 2. Benchmark/eval design features
Construct measured: benchmark *reliability* (Def 2: ability to inform real-world decisions in a stated context for a stated time with no failures). Five dimensions mapped to user questions (Fig.1-2, p.3): comprehensiveness ("does it cover my use case?"), intelligibility ("do I understand the scores?"), consistency ("is the CI real?"), correctness ("could results be systematically biased?"), longevity ("how long can I use it?"). Each failure mode has severity fs∈[0,1] (4 levels: catastrophic ≤1.0, critical <0.75, degraded <0.5, marginally degraded <0.25, p.6) and initial likelihood 1.0; mitigations reduce severity and/or likelihood multiplicatively and stack; risk = severity×likelihood (Def 5). BenchRisk score per dimension = sum of risk reductions (Algorithm 1, p.6).

## 3. Task format & example item
n/a (it is a scoring framework, not an item-based benchmark). Example failure-mode/mitigation pair (p.7, Fig.3): Failure Mode #25 (Correctness) "Developers place evaluator or other test ground truth within system chain" (severity 0.9); Mitigation #28 "Do you refrain from making the evaluator or ground truth publicly available?"

## 4. Scoring / grading methodology
Expert-judgment rubric. Two reviewers (primary + secondary) discuss each mitigation's applicability to each benchmark using public documentation, reaching consensus (p.7). Scores normalized 0-100 (0 = no risk mitigated, 100 = all known risk mitigated). Reliability of the scoring process itself validated: 5 independent raters scored BBQ, Fleiss' kappa 0.53 (moderate); 117/196 mitigations scored consistently, 33 with one disagreement, 46 with two (p.7).

## 5. Dataset construction & provenance
26 benchmarks selected from the BetterBench list plus co-author interest picks; failure modes/mitigations grown iteratively as each benchmark surfaced new ones (p.7). 3 benchmarks (simulator-based) tested BenchRisk coverage without extending the list; 3 had scores entered by benchmark authors and confirmed. Open-source: benchrisk.ai and GitHub, with issue templates for community-driven amendment (p.4,11). Adapts NIST SP 800-30, DoD MIL-STD-882E severity levels, reliability engineering.

## 6. Validity evidence
Inter-rater Fleiss' kappa 0.53 on BBQ (p.7). Monte Carlo resampling + winner-take-all vote analysis of single-rater error (Fig.6, p.10). Convergent/discriminant check vs BetterBench: found independent across all dimensions — measuring different things (reliability-for-decisions vs design quality) (p.9, Fig.5). Longevity validated against empirical time-to-saturation for 7 benchmarks with human baselines >1yr post-publication; high-longevity benchmarks saturate slower, but sample too small for conclusions (p.8-9).

## 7. Saturation / discrimination
Directly studies benchmark saturation as the "longevity" dimension. Most benchmarks score poorly on longevity because academic norms push data release (reproducibility) which enables training-to-test. Outliers AILuminate (private evaluator) and ARC-AGI-Private (competition holdout) resist saturation (p.8). Scores discriminate well: mean 13 (Wordcraft) to 74 (AILuminate) (Fig.4, p.8). Ethics benchmark: longevity 0, mean 37; BBQ: longevity 0, mean 49.

## 8. Multiturn / agentic aspects
n/a for the framework itself, though it explicitly notes simulator/agentic benchmarks (Machiavelli, Wordcraft) require additional failure modes deemed out of current scope (p.7-8).

## 9. Key numbers
- 57 failure modes, 196 mitigations, 26 benchmarks scored (p.1).
- Severity thresholds: catastrophic ≤1.00, critical <0.75, degraded <0.50, marginally <0.25 (p.6).
- BBQ 5-rater agreement: 117 consistent, 33 one-disagreement, 46 two-disagreement, Fleiss kappa 0.53 (p.7).
- Failure Mode #002 (task too broad) unmitigated by 16 of 26 benchmarks (p.9).
- Failure Mode #003 (LLM-produced prompts) has 8 candidate mitigations; Mitigation 89 rated most effective (p.9).
- Benchmark means (Fig.4): AILuminate 74, ARC-AGI-Private 61, WinoGrande 51, ETHICS 37, BBQ 49, MMLU 40, TruthfulQA 38, RealToxicityPrompts 25, Machiavelli 31, Wordcraft 13.

## 10. Pitfalls & limitations
Author-admitted: scores rest on subjective expert judgment (Fleiss 0.53 only moderate); outside assessment relies on public docs and will be superseded by author self-scores (p.7); likelihood/severity are not statistical estimates but assigned levels (p.5); small sample for longevity validation (p.9); intelligibility dimension had strongest rater disagreement (p.10). My read: reliability-increasing mitigations can reduce scientific utility (openness↔longevity tension explicitly acknowledged, p.4); "all failure modes start at likelihood 1.0" worst-case assumption is arbitrary; three authors are also authors of scored benchmarks (marked with *), a conflict.

## 11. Novel ideas worth stealing
- **Failure-mode/mitigation catalog as a design checklist** — for a NEW values benchmark, pre-audit against the 57 failure modes across the 5 dimensions before release (p.1,3).
- **Severity×likelihood risk scoring with stacking multiplicative mitigations** (Algorithm 1) gives a single comparable reliability number per dimension (p.6).
- **Longevity/anti-contamination mitigations**: restrict evaluation-on-demand (Mitigation 67), refrain from publishing evaluator/ground truth (Mitigation 28), avoid releasing test set to SUT developers (Mitigation 145) — directly reusable to keep a values benchmark from saturating (p.7-8).
- **LLM-generated-prompt bias check** (Mitigation 4): run any SUT that may have been privileged during prompt generation and drop instances if unfair advantage found (p.9) — critical when using LLMs to author values items.
- **User-centered "can I rely on it?" framing** with design studies of actual benchmark users for score presentation (Mitigation 75) (p.10).
- **Community-driven versioned amendment process** via issue templates for evolving the catalog (p.11).
- **Metaevaluation dimension mapping** (Fig.2): longevity failures cascade into correctness/comprehensiveness/consistency, all foundational to intelligibility — a causal model of how eval trust degrades.

## 12. Notable quotes
- "the only benchmark that is always 100 percent reliable is one that is never used" (p.2).
- "A benchmark that a user does not understand is not reliable for that user" (p.2).
- "The Anna Karenina principle holds success requires satisfying many conditions, while failure requires few conditions to be met" (p.11).
- "All 26 scored benchmarks present significant risk within one or more of the five scored dimensions" (p.1).

## 13. UNKNOWN / not in extract
Full enumerated list of all 57 failure modes and 196 mitigations (in appendices A/B, not in read portion), the exact per-dimension algorithmic weights, complete Appendix B specification, and the specific numeric scores for the intelligibility-disagreement Table 6.
