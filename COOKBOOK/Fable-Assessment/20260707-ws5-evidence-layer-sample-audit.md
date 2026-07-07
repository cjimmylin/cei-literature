# WS-5 — Evidence-Layer Sample Audit: cards / dossiers / digests (Fable-adjudicated, 2026-07-07)

**Method:** stratified samples verified against in-vault sources by two Sonnet agents
(cards; systematic every-62nd sampling, disjoint offsets) and one Opus agent (digests +
dossiers traced to source matrices and cards). First corpus-level audit of the 30-EVIDENCE
layer (the 2026-07-05 spot-check covered only 21 claims in 10-LITERATURE).

## Verdict: TRUSTWORTHY

- **Cards (n=26 of 677: 20 paper + 6 ailab):** 24 OK · **2 MINOR** · 0 MAJOR ·
  **0 FABRICATION**. All 26 sources located in-vault. Point estimate for MAJOR-or-worse
  error rate: 0/26 → 95% upper bound ≈ 11% (rule of three); MINOR rate ≈ 7.7%. Several
  load-bearing numbers verified verbatim against source text (Claude 99.29%±0.22; Llama-2
  36/31.5; Stiennon 61-vs-43 "10× larger" — which also CLOSES the WS-2 verification item
  on that stat: the overview is faithful to its source).
- **Digests (all 4):** every headline corpus anchor (54/292/401/218) and structural stat
  (gate counts, Jenks breaks, Kendall W, weights) traces EXACTLY to its source matrix;
  zero contradictions; **all four sub-project disclosures present and bound to their
  numbers.** Finding-level percentages that live only in external source papers are
  correctly labeled "copied verbatim; do not recompute."
- **Dossiers (2 of 13 sampled: agentic-multiturn, validity-psychometrics):** 10/10
  load-bearing claims SUPPORTED verbatim by the cited cards; citation stems resolve 76/76
  and 168/169.

## Defect list (all small; owners assigned)

| # | Defect | Grade | Fix |
|---|---|---|---|
| E-1 | `Anthropic-Sleeper Agents` cited twice in the validity-psychometrics dossier resolves to NO card | MINOR | Ingest the missing card or repoint the citation (note: a "Simple Probes Catch Sleeper Agents" stem exists post-rename — check whether that is the intended target) |
| E-2 | 2024-Meijer card: PEW panel "39 countries" vs source's 40 | MINOR | One-number card fix |
| E-3 | OpenAI-GPT-4.5 card: MakeMeSay 72% called "highest of all models" — source says TIED with post-mitigation deep research | MINOR | One-word card fix ("tied-highest") |
| E-4 | **Vault paper entry** (not the card) for 2015-Clifford backfilled with 672 vignettes; correct is 132 (the card is right) | MINOR (vault-data) | Fix the paper .md backfill — outside COOKBOOK, normal vault-fix lane |
| E-5 | ConflictScope: the KB02-headline 1.7→4.5 rank shift is directionally supported by the in-vault abstract but the specific numbers are unverifiable (abstract-only record, no extract) | note | Pull the PDF/extract when convenient; until then KB02 keeps the direction, tags the numbers "per paper, not independently verified" |

Three sampled sources were stub-only records (claims plausible, not contradicted, not
fully confirmable) — consistent with the known vault ingestion frontier, not an
evidence-layer defect.

## Interpretation

The 2026-07-05 build discipline (cards quote with page refs ±1–2 pp; digests copy verbatim
from matrices) held up under adversarial sampling. The evidence layer can be cited by
future work at face value, with the standing ±-page tolerance and the four disclosures.
The one systemic soft spot is stub-only sources: a card built on an abstract-only vault
record inherits unverifiable precision (E-5 pattern) — future card-building should tag
`source_depth: abstract-only` so consumers can see it.
