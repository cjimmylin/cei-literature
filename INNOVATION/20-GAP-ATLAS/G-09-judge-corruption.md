# G-09 — Judge-Corruption Science

**Stage C** · **Ratings S/T/F: H/H/H** · **Programs: RP-03, RP-04** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## Statement                       [KERNEL — FROZEN]
A negative-results literature now documents that the judging layer — human and AI — is corruptible in ways debate-style presentation does not fix: confirmation and automation bias, persuasion tracking debater priors, quality ratings favoring belief-misaligned arguments, judge collapse at capability gaps. Every LLM-judged CEI benchmark inherits this threat, and the vault lacks the literature.

## Why it matters                  [KERNEL — FROZEN]
Severity H twice over: (a) it undermines oversight protocols (G-07's judging leg); (b) it is a direct validity threat to CEI's own published verdicts. CEI-fit H: we run judge pipelines daily and have the psychometric machinery to quantify the corruption instead of hand-waving it.

## Evidence                        (corpus + field)
**Corpus baseline:** the negative-results judging literature is absent; CEI benchmarks depend on the judging leg it attacks.

**Field:** negative results are piling up on the judge (Front C key results):
- **Confirmation / automation bias in human overseers** (arXiv:2507.19486): two-sided (debate-style) presentation does *not* fix it.
- **AI debaters' own beliefs** (arXiv:2510.13912): debaters are more persuasive arguing their own priors, and belief-misaligned arguments get **rated higher quality** — persuasion tracks the debater's prior, not the truth.
- **LLM-as-judge collapse at capability gaps** (peer-prediction baseline, arXiv:2601.20299): judging degrades toward random at 5–20× gaps, where peer prediction still holds.
- **Self-preference bias** (arXiv:2410.21819): judges favor their own outputs.

This is a direct validity threat to every LLM-judged CEI bench — the governance protocol §6.2 already makes the G-09 caveat a standing methods requirement.

## State of the art
The negative literature is real but was run on QA / safety content; the **values version is both missing and directly self-serving** — CEI runs LLM-judge pipelines daily and has the psychometric machinery (inter-rater reliability, judge-family disagreement structure) to quantify the corruption rather than hand-wave it. Response is split by design: RP-03 measures corruption *within oversight protocols*; RP-04's dogfood audit measures it *within CEI's own scoring pipelines*. The RP-04 K2 pre-commitment (mandatory robustness pass if CEI's own verdicts are threatened) is part of this gap's response — it binds CEI to act on what the audit finds.

## What closing looks like         [KERNEL — FROZEN]
M1 — cluster acquired; G-09 caveat becomes a standing methods requirement (done — governance protocol §6.2). M2 — RP-04's dogfood audit quantifies judge-family disagreement structure on CEI's own banks. M3 — judge-corruption effect sizes on values content published (RP-03 metrics + RP-04 memo), with triangulation guidance benchmarks can adopt.

## CEI response                    [KERNEL — FROZEN]
Split by design: RP-03 measures corruption within oversight protocols; RP-04 measures it within scoring pipelines. The pre-commitment in RP-04 K2 (mandatory robustness pass if CEI's own verdicts are threatened) is part of this gap's response.

## OPUS-EXPAND checklist           (LIVING)
- [ ] Deep-read AI-debaters-own-beliefs 2510.13912 and summarize the belief-misaligned-rated-higher result into §State of the art; assess whether CEI value items are especially exposed (contested items = strong priors).
- [ ] Deep-read confirmation-bias 2507.19486 and record which debiasing interventions it tested and which failed.
- [ ] Design the RP-04 dogfood judge-family disagreement audit (M2): ≥3 judge families on a fixed CEI bank slice, with a disagreement-structure metric.
- [ ] Confirm governance protocol §6.2 wording covers the standing G-09 caveat and cross-link it here (M1 done).
- [ ] Add a triangulation-guidance draft (M3): concrete steps a benchmark can adopt to bound judge-corruption effect sizes.
- [ ] Cross-reference G-07 (oversight judging leg) and G-08 (weak-supervisor deception) as the shared judge-integrity thread.

## Sources                         (evidence classes marked)
- Confirmation Bias in oversight — arXiv:2507.19486 — **SEARCH-CONFIRMED** — P1 anchor.
- AI Debaters' Own Beliefs — arXiv:2510.13912 — **SEARCH-CONFIRMED** — P1 anchor.
- Peer Prediction (LLM-judge collapse baseline) — arXiv:2601.20299 — **SEARCH-CONFIRMED**.
- Self-Preference Bias (LLM judge) — arXiv:2410.21819 — **SEARCH-CONFIRMED**.
- Debate Helps Weak Judges — arXiv:2605.27483 — **⚠ UNCONFIRMED** (2605 ID; verify-at-download).
- Governance protocol §6.2 (standing G-09 methods caveat) — **VERIFIED** (`../00-CHARTER/01-governance-protocol.md`).
