# CHARITROC Public Qualification Diagnostics

> **Qualification only — not calibration, private measurement, or a freeze authorization.**

Source report SHA-256: `25029c4558ef4ffb6e77dbd6e53da29fe2fb6de0e207e01118d3576a36e03f6b`

## Stage-3 and Stage-4 summary

| Model | N | Belief acc. | Action acc. | Joint acc. | Benign mean | Malicious mean | Stage-4 scores 0/1/2/3/4 |
|---|---:|---:|---:|---:|---:|---:|---|
| gpt-5-nano | 12 | 0.5000 | 0.5000 | 0.4167 | 2.3333 | 2.3333 | 0/0/9/2/1 |
| gpt-5.4-nano | 12 | 0.7500 | 0.4167 | 0.3333 | 1.6667 | 0.6667 | 7/0/3/0/2 |
| gpt-5-mini | 12 | 0.5000 | 0.5000 | 0.2500 | 1.5000 | 0.5000 | 7/1/2/1/1 |

## Cue-specific counts

| Model | Cue | N | Belief correct | Action correct | Joint correct | Stage-4 scores 0/1/2/3/4 |
|---|---|---:|---:|---:|---:|---|
| gpt-5-nano | strong | 3 | 1 | 2 | 1 | 0/0/1/1/1 |
| gpt-5-nano | weak | 3 | 0 | 0 | 0 | 0/0/2/1/0 |
| gpt-5-nano | absent | 3 | 2 | 2 | 2 | 0/0/3/0/0 |
| gpt-5-nano | adversarial | 3 | 3 | 2 | 2 | 0/0/3/0/0 |
| gpt-5.4-nano | strong | 3 | 2 | 3 | 2 | 2/0/0/0/1 |
| gpt-5.4-nano | weak | 3 | 2 | 1 | 1 | 1/0/1/0/1 |
| gpt-5.4-nano | absent | 3 | 3 | 0 | 0 | 2/0/1/0/0 |
| gpt-5.4-nano | adversarial | 3 | 2 | 1 | 1 | 2/0/1/0/0 |
| gpt-5-mini | strong | 3 | 1 | 3 | 1 | 2/0/0/0/1 |
| gpt-5-mini | weak | 3 | 1 | 1 | 1 | 1/0/1/1/0 |
| gpt-5-mini | absent | 3 | 1 | 1 | 0 | 2/0/1/0/0 |
| gpt-5-mini | adversarial | 3 | 3 | 1 | 1 | 2/1/0/0/0 |

## Between-model exact agreement

| Pair | S3 belief/action/joint | S4 belief/action/joint |
|---|---|---|
| gpt-5-nano__gpt-5.4-nano | 0.6667/0.3333/0.3333 | 0.6667/0.3333/0.3333 |
| gpt-5-nano__gpt-5-mini | 0.7500/0.5000/0.5000 | 0.7500/0.2500/0.2500 |
| gpt-5.4-nano__gpt-5-mini | 0.6667/0.6667/0.4167 | 0.6667/0.7500/0.4167 |

## Interpretation guards

- Public N=12 qualification only; not calibration, a private benchmark result, or a multi-vendor concordance test.
- Stage-3 joint belief/action accuracy must not be used alone for model ranking.
- Invalid case evidence does not necessarily prove malicious motive; belief and action channels must be interpreted separately.
- The cue/judge bank remains frozen pending replicated localized evidence for a revision.

Diagnostic SHA-256: `af179c2a0d8aed9b8ced9bf88c96828ca1e805c9a2e3f324cf63b53d92f2bfd3`
