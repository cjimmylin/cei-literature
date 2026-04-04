# Hypothesis Tests for NormEval 5 Claims

Date: 2026-04-04
Benchmarks: 37

## C1: Ceiling Effect
**H0:** GPT-4 performance on binary moral judgments = 50% (chance)
**H1:** GPT-4 performance > 50%

Test: Binomial test for P(50/50 correct | p=0.9)
This tests whether observing 50/50 correct is plausible if true accuracy is 90%.

- P(50/50 correct | p=0.5, chance): p = 8.88e-16 (binomial test)
- P(all 50 correct | p=0.9): 0.005154
- P(>=45/50 | p=0.5): 2.10e-09

**Interpretation:** If a model scores 50/50, we can reject chance (p=0.5)
with p < 8.88e-16. The ceiling effect is real: at p=0.9 true accuracy,
the probability of a perfect score is 0.0052 (not negligible),
making benchmarks unable to discriminate among high-performing models.

## C2: Utilitarian Bias
**H0:** Accuracy on utilitarian items = accuracy on deontological items
**H1:** Utilitarian accuracy > deontological accuracy

- Utilitarian accuracy: 77% (n=30)
- Deontological accuracy: 50% (n=30)
- Two-proportion z-test: z = 2.172, p = 0.0149
- Difference: 27.0 percentage points
- 95% CI for difference: [3.6%, 50.4%]
- Cohen's h = 0.570 (medium)

**Interpretation:** The 27 percentage-point gap is statistically
significant (p = 0.0149), with Cohen's h = 0.570 indicating a
medium effect size.

## C3: Care Ethics Void
**H0:** Care ethics is assigned uniformly like other traditions
**H1:** Care ethics is systematically absent as primary tradition

- Benchmarks with care ethics as primary/co-primary: 2/37
- Under uniform assignment (p=1/5 per benchmark):
  P(exactly 0 have care as primary) = 2.60e-04
  P(care never primary across 37) = 0.000260

- Care ethics score > 0: 4/37 benchmarks
- Care ethics score >= 50: 2/37 benchmarks

**Interpretation:** Only 2/37 benchmarks have care ethics as
primary. Under uniform random assignment, P(0 out of 37) = 2.60e-04,
strongly suggesting systematic exclusion rather than chance.

## C4: Judgment-Only Predominance
**H0:** P(judgment-only) = 0.5
**H1:** P(judgment-only) > 0.5

- Judgment-only benchmarks: 22/37 (59.5%)
- Binomial test (H1: p > 0.5): p = 0.1620
- Wilson 95% CI: [43.5%, 73.7%]

**Interpretation:** 22/37 = 59.5% of benchmarks
test only judgment. Not significant
at alpha=0.05 (p = 0.1620).

## C5: Data Availability Bottleneck
**H0:** ND scores are the same for data-available vs data-unavailable benchmarks
**H1:** They differ (two-sided)

- Data-available benchmarks (n=23): mean ND = 52.6, median = 55.8
- Data-unavailable benchmarks (n=14): mean ND = 55.3, median = 61.9
- Mann-Whitney U = 144.0, p = 0.6052
- Rank-biserial r = 0.106

**Interpretation:** Data-unavailable benchmarks have
non-significantly lower
ND scores (p = 0.6052). Effect size r = 0.106.
