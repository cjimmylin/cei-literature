# NormEval GPT Mini (Codex) Cross-Model Summary

- Date: 2026-04-04
- Model: gpt-5-mini (Codex agent)
- Administration: direct Codex mini reasoning; no SDK/API used
- Scope: T6-T15 only, matching the existing Claude and Codex runs

## Headline Findings

- T13: mini IB=4.87, IH=3.2, placing the mini run near Sonnet and notably less harm-averse than the existing main Codex run.
- T14: mini CBR rate is 53.8%, above the existing main Codex run and equal to Sonnet.
- T7: mini decision change rate is 0.0%, matching both Sonnet and the existing main Codex run on this limited persuasion set.
- T6, T9, T11, and T15 remain saturated on the knowledge/classification items used in the replication.

## Per-Trial Comparison

### T6

- Benchmark: PrinciplismQA Medical Ethics
- Mini vs main Codex agreement: 7/7 (100.0%)
- Mini vs Sonnet agreement: 7/7 (100.0%)
- Mini vs Haiku agreement: 7/7 (100.0%)
- Mini primary metric: 100.0

### T7

- Benchmark: Moral Persuasion in LLMs
- Mini vs main Codex agreement: 3/3 (100.0%)
- Mini vs Sonnet agreement: 3/3 (100.0%)
- Mini vs Haiku agreement: 2/3 (66.7%)
- Mini DCR: 0.0 | Main 0.0 | Opus 66.7 | Sonnet 0.0 | Haiku 33.3

### T8

- Benchmark: AMAeval (Beyond Ethical Alignment)
- Mini vs main Codex agreement: 5/6 (83.3%)
- Mini vs Sonnet agreement: 6/6 (100.0%)
- Mini vs Haiku agreement: 4/6 (66.7%)
- Mini abductive mean: 3.0 | Main 2.67 | Opus 2.67 | Sonnet 3.0 | Haiku 3.0

### T9

- Benchmark: JETHICS — Japanese Ethics Understanding Evaluation Dataset
- Mini vs main Codex agreement: 22/22 (100.0%)
- Mini vs Sonnet agreement: 22/22 (100.0%)
- Mini vs Haiku agreement: 22/22 (100.0%)
- Mini primary metric: 100.0

### T10

- Benchmark: Pluralistic Moral Gap
- Mini vs main Codex agreement: 6/7 (85.7%)
- Mini vs Sonnet agreement: 5/7 (71.4%)
- Mini vs Haiku agreement: 7/7 (100.0%)
- Mini high-consensus alignment: 3/3 (100%) | Main 3/3 (100%) | Opus 90% | Sonnet 67% | Haiku 100%

### T11

- Benchmark: MedEthicsQA
- Mini vs main Codex agreement: 6/6 (100.0%)
- Mini vs Sonnet agreement: 6/6 (100.0%)
- Mini vs Haiku agreement: 6/6 (100.0%)
- Mini primary metric: 100.0

### T12

- Benchmark: UniMoral Multilingual Moral Reasoning
- Mini vs main Codex agreement: 4/6 (66.7%)
- Mini vs Sonnet agreement: 4/6 (66.7%)
- Mini vs Haiku agreement: 4/6 (66.7%)
- Mini mean Kohlberg stage: 5.0 | Main 5.17 | Opus 5.0 | Sonnet 5.17 | Haiku 5.0

### T13

- Benchmark: The Greatest Good Benchmark (OUS)
- Mini vs main Codex agreement: 20/30 (66.7%)
- Mini vs Sonnet agreement: 17/30 (56.7%)
- Mini vs Haiku agreement: 15/30 (50.0%)
- Mini IB/IH: 4.87/3.2 | Main 5.13/2.93 | Opus 4.7/3.0 | Sonnet 5.0/3.2 | Haiku 4.87/4.47

### T14

- Benchmark: Cognitive Biases in Moral Decision-Making (PNAS)
- Mini vs main Codex agreement: 21/22 (95.5%)
- Mini vs Sonnet agreement: 21/22 (95.5%)
- Mini vs Haiku agreement: 18/22 (81.8%)
- Mini CBR/CA: 53.8% / 77.8% | Main 46.2% / 77.8% | Opus 46.2% | Sonnet 53.8% | Haiku 69.2%

### T15

- Benchmark: ProMoral-Bench
- Mini vs main Codex agreement: 5/5 (100.0%)
- Mini vs Sonnet agreement: 5/5 (100.0%)
- Mini vs Haiku agreement: 5/5 (100.0%)
- Mini strategy accuracies: ZS 100.0%, FS-CoT 100.0%, Constitutional 100.0%

