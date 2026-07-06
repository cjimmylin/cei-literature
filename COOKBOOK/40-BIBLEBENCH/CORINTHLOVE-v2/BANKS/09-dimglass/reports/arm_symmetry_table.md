# DIMGLASS d2-d3 matched-arm symmetry audit

Arms differ ONLY in evidence validity (claim clause + counter token).
Diffs are (valid arm) minus (invalid arm), per matched pair.

| domain | dose | n_pairs | word Δ mean(signed) | word Δ max|abs| | char Δ mean | char Δ max|abs| | digit max|abs| | cit max|abs| | hedge max|abs| |
|---|---|---|---|---|---|---|---|---|---|
| code | d2 | 23 | +0.000 | 0 | -0.74 | 3 | 1 | 0 | 0 |
| code | d3 | 21 | +0.000 | 0 | -0.10 | 1 | 0 | 0 | 0 |
| corpus_qa | d2 | 22 | +0.000 | 0 | +0.77 | 1 | 1 | 0 | 0 |
| corpus_qa | d3 | 22 | +0.000 | 0 | -0.27 | 2 | 2 | 0 | 0 |
| logic | d2 | 21 | -0.429 | 1 | -0.29 | 2 | 0 | 0 | 0 |
| logic | d3 | 23 | +0.000 | 0 | -0.96 | 2 | 2 | 0 | 0 |
| quant | d2 | 23 | +0.000 | 0 | -2.22 | 4 | 1 | 0 | 0 |
| quant | d3 | 23 | +0.000 | 0 | +2.22 | 3 | 1 | 0 | 0 |
| reading | d2 | 22 | +0.227 | 1 | +0.09 | 6 | 0 | 0 | 0 |
| reading | d3 | 22 | +0.273 | 2 | +2.45 | 13 | 0 | 0 | 0 |

Total matched pairs audited: 222
Tolerances: {"word_mean_signed": 0.75, "word_max_abs": 3, "char_mean_signed": 6.0, "char_max_abs": 24, "digit_max_abs": 2, "cit_max_abs": 1, "hedge_max_abs": 1}

## RESULT: PASS — no systematic surface asymmetry between arms.
