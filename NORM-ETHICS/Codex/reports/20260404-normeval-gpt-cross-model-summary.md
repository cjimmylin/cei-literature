# NormEval GPT (Codex) Cross-Model Summary

- Date: 2026-04-04
- Model: gpt-5 (Codex agent)
- Administration: direct Codex agent reasoning; no SDK/API used
- Scope: T6-T15 only, matching the existing three-model replicated benchmark set

## Headline Findings

- T13: IB=5.13, IH=2.93 for GPT, making this Codex run slightly more harm-averse than Sonnet and materially more harm-averse than Haiku.
- T14: GPT CBR rate on moral dilemmas is 46.2%, close to Opus and below Sonnet/Haiku.
- T7: GPT decision change rate is 0.0%, matching Sonnet's resistance profile in this direct administration.
- T6, T9, T11, and T15 remain saturated or near-saturated on the knowledge/classification items used in the Claude replication.

## Per-Trial Comparison

### T6

- Benchmark: PrinciplismQA Medical Ethics
- GPT vs Sonnet agreement: 7/7 (100.0%)
- GPT vs Haiku agreement: 7/7 (100.0%)
- GPT primary metric: 100.0

### T7

- Benchmark: Moral Persuasion in LLMs
- GPT vs Sonnet agreement: 3/3 (100.0%)
- GPT vs Haiku agreement: 2/3 (66.7%)
- GPT DCR: 0.0 | Opus 66.7 | Sonnet 0.0 | Haiku 33.3

### T8

- Benchmark: AMAeval (Beyond Ethical Alignment)
- GPT vs Sonnet agreement: 5/6 (83.3%)
- GPT vs Haiku agreement: 3/6 (50.0%)
- GPT abductive mean: 2.67 | Opus 2.67 | Sonnet 3.0 | Haiku 3.0

### T9

- Benchmark: JETHICS — Japanese Ethics Understanding Evaluation Dataset
- GPT vs Sonnet agreement: 22/22 (100.0%)
- GPT vs Haiku agreement: 22/22 (100.0%)
- GPT primary metric: 100.0

### T10

- Benchmark: Pluralistic Moral Gap
- GPT vs Sonnet agreement: 6/7 (85.7%)
- GPT vs Haiku agreement: 6/7 (85.7%)
- GPT high-consensus alignment: 3/3 (100%) | Opus 90% | Sonnet 67% | Haiku 100%

### T11

- Benchmark: MedEthicsQA
- GPT vs Sonnet agreement: 6/6 (100.0%)
- GPT vs Haiku agreement: 6/6 (100.0%)
- GPT primary metric: 100.0

### T12

- Benchmark: UniMoral Multilingual Moral Reasoning
- GPT vs Sonnet agreement: 5/6 (83.3%)
- GPT vs Haiku agreement: 4/6 (66.7%)
- GPT mean Kohlberg stage: 5.17 | Opus 5.0 | Sonnet 5.17 | Haiku 5.0

### T13

- Benchmark: The Greatest Good Benchmark (OUS)
- GPT vs Sonnet agreement: 24/30 (80.0%)
- GPT vs Haiku agreement: 9/30 (30.0%)
- GPT IB/IH: 5.13/2.93 | Opus 4.7/3.0 | Sonnet 5.0/3.2 | Haiku 4.87/4.47

### T14

- Benchmark: Cognitive Biases in Moral Decision-Making (PNAS)
- GPT vs Sonnet agreement: 20/22 (90.9%)
- GPT vs Haiku agreement: 17/22 (77.3%)
- GPT CBR/CA: 46.2% / 77.8% | Opus 46.2% / 77.8% | Sonnet 53.8% / 77.8% | Haiku 69.2% / 77.8%

### T15

- Benchmark: ProMoral-Bench
- GPT vs Sonnet agreement: 5/5 (100.0%)
- GPT vs Haiku agreement: 5/5 (100.0%)
- GPT strategy accuracies: ZS 100.0%, FS-CoT 100.0%, Constitutional 100.0%

