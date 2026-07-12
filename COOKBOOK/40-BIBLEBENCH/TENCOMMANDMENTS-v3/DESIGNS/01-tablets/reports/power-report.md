# TABLETS pre-run power report

**Evidence eligibility:** `PRE_RUN_ONLY`

**Empirical status:** `NOT_EMPIRICAL`

Alpha = 0.05; target power = 0.80; simulations = 10000; seed = 20260711.

| Claim | Method | P1 n | Official n | P1 power | P1 MDE | Official MDE | Status | Flatness |
|---|---|---:|---:|---:|---:|---:|---|---|
| smallest_pair_x_tier_cell | two-sided exact binomial pair-choice simulation | 3 | 9 | 0.000 | N/A | 0.450 | UNDERPOWERED_DESCRIPTIVE | INELIGIBLE_UNDERPOWERED |
| pair_x_tier_flip | paired two-proportion exact discordance simulation | 3 | 9 | 0.000 | N/A | 0.800 | UNDERPOWERED_DESCRIPTIVE | INELIGIBLE_UNDERPOWERED |
| ladder_rank_and_dispersion | C1-C9 full pair tournament Bradley-Terry MM refit with registered ladder_dispersion_100 | 3 | 9 | 0.646 | 3.000 | 1.500 | UNDERPOWERED_DESCRIPTIVE | INELIGIBLE_UNDERPOWERED |
| cg | conditional certified-cell binomial conformance simulation | 3 | 9 | 0.000 | N/A | 0.450 | UNDERPOWERED_DESCRIPTIVE | INELIGIBLE_UNDERPOWERED |
| triad_coherence | trial-level conditional triangle-reversal MCMC | 3 | 9 | N/A | N/A | N/A | NOT_ESTIMABLE_UNTIL_WIN_MARGINS | INELIGIBLE_NOT_ESTIMABLE |

This artifact is PRE_RUN_ONLY and NOT_EMPIRICAL. It cannot establish flatness, confirm a claim, or promote diagnostic evidence.
