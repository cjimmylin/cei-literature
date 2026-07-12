# CHARITROC Public Qualification Diagnostics

> **Qualification only — not calibration, private measurement, or a freeze authorization.**

Source report SHA-256: `905ae96234cd2c88ff1c3699eea564462725cbc33019504a5642fa450b055959`

## Stage-3 and Stage-4 summary

| Model | N | Belief acc. | Action acc. | Joint acc. | Benign mean | Malicious mean | Stage-4 scores 0/1/2/3/4 |
|---|---:|---:|---:|---:|---:|---:|---|
| gpt-5.4-mini | 12 | 0.5833 | 0.7500 | 0.4167 | 2.3333 | 0.8333 | 4/3/2/0/3 |

## Cue-specific counts

| Model | Cue | N | Belief correct | Action correct | Joint correct | Stage-4 scores 0/1/2/3/4 |
|---|---|---:|---:|---:|---:|---|
| gpt-5.4-mini | strong | 3 | 2 | 3 | 2 | 2/0/0/0/1 |
| gpt-5.4-mini | weak | 3 | 2 | 2 | 1 | 1/0/0/0/2 |
| gpt-5.4-mini | absent | 3 | 2 | 2 | 2 | 1/1/1/0/0 |
| gpt-5.4-mini | adversarial | 3 | 1 | 2 | 0 | 0/2/1/0/0 |

## Between-model exact agreement

| Pair | S3 belief/action/joint | S4 belief/action/joint |
|---|---|---|

## Interpretation guards

- Public N=12 qualification only; not calibration, a private benchmark result, or a multi-vendor concordance test.
- Stage-3 joint belief/action accuracy must not be used alone for model ranking.
- Invalid case evidence does not necessarily prove malicious motive; belief and action channels must be interpreted separately.
- The cue/judge bank remains frozen pending replicated localized evidence for a revision.

Diagnostic SHA-256: `246f348ad67ca194eaccde9726b8984e23532b863ca80170a44a02e73ce132b9`
