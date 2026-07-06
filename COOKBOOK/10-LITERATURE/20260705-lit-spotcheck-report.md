# 10-LITERATURE Spot-Check Verification Report

**Date:** 2026-07-05
**Scope:** Light verification pass over the 6 documents in `COOKBOOK/10-LITERATURE/`.
**Method:** Sampled ~3–4 load-bearing claims per doc (numbers, comparatives, paper
characterizations), traced each to its cited evidence card in
`30-EVIDENCE/20260705-cards/` (or `20260705-ailabs-cards/`) or the theme digest in
`30-EVIDENCE/20260705-digests/`. Page refs treated as ±1–2 pp. For
`benchmark-landscape-statistics.md`, digest statistics checked for verbatim / faithful
transcription (not recomputed).
**Grades:** VERIFIED / MINOR-DRIFT / MISATTRIBUTED / WRONG-NUMBER.

---

## lit-review-normative-ethics.md

| Claim (abridged) | Citation | Grade | Evidence note |
|---|---|---|---|
| ETHICS produces 100% accuracy across all 9 models (binomial p < 1×10⁻¹⁵), zero discriminative power | digest C1 | VERIFIED | normeval-digest C1 verbatim: "100% accuracy across all 9 models (binomial, p < 1×10⁻¹⁵)". |
| MoReBench: 23,018 signed weighted atomic rubrics; validated LLM-judge κ=0.75; zero correlation w/ capability (Pearson −0.245 to 0.216) | [2025-Chiu-MoReBench] | VERIFIED | Card confirms 23,018 rubric criteria, κ=0.75 over 7,176 pairs, cross-corr r∈[−0.245, 0.216]. (Inter-tradition 18.3%/13.3%… spread is digest-trial-sourced, consistent.) |
| LLMs achieve 77% utilitarian vs 50% deontological accuracy (z=2.17, p=0.015, Cohen's h=0.57), 27-pt gap | digest C2 | VERIFIED | normeval-digest C2 verbatim: "77% utilitarian vs 50% deontological (two-proportion z = 2.17, p = 0.015, Cohen's h = 0.57), a 27-point gap". |
| SpeciesismBench: classifies 86% (±0.7%) speciesist yet judges only 34% (±1.3%) morally wrong; "evaluative rather than epistemic" | [2025-Jotautaite-SpeciesismBench] | VERIFIED | Card headline + verbatim quote confirm 86%/34% and "the problem is evaluative rather than epistemic" (p.5, p.11). |

## lit-review-moral-psychology.md

| Claim (abridged) | Citation | Grade | Evidence note |
|---|---|---|---|
| MFT holds 67/292 candidates but 18 of 48 top-tier slots (37.5%) and 73% quality rate (49/67) | moralpsych digest Claim 1 | VERIFIED | Digest verbatim: "67/292… 18 of 48 top-tier slots (37.5%)… 73% quality rate (49/67 top+high)". |
| GPT-3.5 gave 99–100% uniformity on 6 of 14 Many Labs 2 studies (Less-is-better d=9.25 vs human d=0.78) | [2025-Oh-Robustness] | VERIFIED | Card: "6 of 14 studies… 99–100% uniformity"; "Less-is-better effect size: d=9.25 vs. human d=0.78 (p.6)". |
| Scruples BEST oracle: human F1 0.490 < oracle 0.707 | [2021-Lourie-Scruples] | VERIFIED | Card headline: human F1 on ANECDOTES 0.490 (test); "BEST performance F1 on ANECDOTES: 0.707 (p.6)". |

## lit-review-religious-values.md

| Claim (abridged) | Citation | Grade | Evidence note |
|---|---|---|---|
| Islam = 28 of 47 gate-passers (59.6%) and 9 of 12 Tier 1; χ²=64.96, Cramér's V=0.53, p<0.001 | religious digest Claim 1 | VERIFIED | Digest verbatim: "χ² = 64.96, Cramér's V = 0.53, p < 0.001… 28 of 47 gate-passers (59.6%)… 9 of 12 Tier 1". |
| Hovy: Llama2-13b refuses 55.61% Jewish / 31.75% Muslim; Llama3-70b 0.04%/0.03%; GPT-4o 0% | [2024-Hovy] | VERIFIED | Card headline numbers match all five figures exactly (p.4). |
| Zhang RCT n=1,005 across 12 regions: Islam −0.23 (p<0.001), Christianity +0.31; AI Islam texts 1.5× "conflict" | [2025-Zhang] | VERIFIED | Card (`2025-Zhang-Cognitive Bias…`) confirms 1,005 participants / 12 regions, −0.23 Islam, +0.31 Christianity, 1.5× conflict (p.10). |

## lit-review-cultural-linguistic.md

| Claim (abridged) | Citation | Grade | Evidence note |
|---|---|---|---|
| Sukiennik: web-content-%/country r=0.94, GDP r=0.81, log size r=0.13; GLM-4 (9B) aligns best | [2025-Sukiennik] | VERIFIED | Card headline confirms r=0.94 / 0.81 / 0.13 and GLM-4 (9B) best overall (p.7–8). |
| Haslett: participant-nationality β=−.30 dwarfs model-origin β=.03 | [2025-Haslett] | VERIFIED | Card: "WVS… origin interaction (β = .03)… nationality main effect (β = −.30)" (p.6). |
| Benkler: US WVS R²=0.80 but Japan 0.08, Vietnam 0.04, Nigeria 0.01 | [2023-Benkler] | VERIFIED | Card headline confirms all four R² values (p.6). |
| 0/218 measurement invariance; 6.8% (3/44) concept coverage | cultural digest findings 1–3 | VERIFIED | Digest verbatim: "precisely zero… measurement invariance"; "3 of 44 (6.8%)… ren, li, ubuntu". |

## benchmark-landscape-statistics.md (also checked vs digests for verbatim transcription)

| Claim (abridged) | Citation | Grade | Evidence note |
|---|---|---|---|
| NormEval: 24/54 gates, 10/54 reasoning; gate = sociology not quality (Mann-Whitney U=287, p=0.605; ND 58.8 unavail > 53.0 avail) | NormEval digest | VERIFIED | Digest C2/C5 verbatim: "Mann-Whitney U = 287, p = 0.605, r = 0.07… higher among unavailable (58.8) than available (53.0)". |
| Moral Psych: 48/292 (16.4%); 58% Level 1–2 (up from 17%, 3.4× jump); quality flat 75%→48%→46% at 9.5× growth; r=−0.83 | Moral Psych digest | VERIFIED | Digest verbatim on all: "58% sit at Level 1 or 2 (up from 17%… 3.4x jump)"; "pre-2020 75%… 2020–22 48%… 2023–26 46%… 9.5x"; "r = −0.83". |
| Religious Values: 45 gate-passers; 27.7% (13/47) reasoning; mean A3 = 30.0/100, Cohen's d = −1.23 | Religious digest | VERIFIED | Digest verbatim: "45 gate-passers"; "27.7% (13/47)… p = 0.0015"; "mean A3 = 30.0/100 (SD = 16.2)… Cohen's d = −1.23". |
| Cultural/Global: <7% (≈15) substance×usability intersection; 0/218 invariance; effective N ≈ 3.4 | Cultural digest | VERIFIED | Digest verbatim: "≈15 benchmarks (<7%)"; "precisely zero… invariance"; "effective N ≈ 3.4 (range 3.1–4.8)". |

*Note: doc's own internal-consistency scaffolding (computed-vs-digest divergences, e.g. RV
2024+ share 77.1% raw vs 73% digest, and D5 raw-matrix vs paper Table 3) is explicitly
flagged in-text with the authoritative figure named — good hygiene, not drift.*

## alignment-methods-overview.md

| Claim (abridged) | Citation | Grade | Evidence note |
|---|---|---|---|
| InstructGPT SFT ~13k prompts; 1.3B InstructGPT preferred over 175B GPT-3; labelers mostly US/SE-Asian, ~96% English | [OpenAI-instructgpt] | VERIFIED | Card: "SFT dataset: ~13k training prompts"; "1.3B InstructGPT preferred over 175B GPT-3"; "~96% English", "US or Southeast Asian". (11,295+1,430 SFT split is paper Table 6, consistent with ~13k.) |
| Beyond ~250 nats KL, human preference falls below random; 1.3B RLHF beat 10× model (61% vs 43%) on 64,832 pairs | [OpenAI-learning-to-summarize-rlhf] | VERIFIED | Card: "beyond ~KL 250 nats… preference falls below random"; "61% vs 43%… 10× its size"; "64,832 comparison pairs". |
| Constitutional Classifiers: HHH alone ~16%→~14% ASR; input+output 0.5%; ++ 0.05% refusal, no universal jailbreak across 198K attempts, 1,736 red-team hrs | [Anthropic-Constitutional_Classifiers / ++] | VERIFIED | CC card: "~16% to ~14%"; "input+output… 0.5%". CC++ card: "0.05% refusal"; "198K attempts"; "1,736 estimated hours". |
| Sycophancy: Claude 2 PM prefers sycophantic over truthful 95% of the time; "Are you sure?" abandonment 32% (GPT-4)–86% (Claude 1.3) | [Anthropic-Collective_Constitutional_AI (sycophancy)] | VERIFIED | Card (contains the Sycophancy paper per known swap) confirms both: 95% (p.8) and 32%–86% swaying (App. A.4). Doc correctly tags "(sycophancy)". |

*Observation (not graded — tied to the known card swap): the doc's separate participatory-
constitution claim citing plain [Anthropic-Collective_Constitutional_AI] (BBQ bias lowered
on all 9 dimensions via Group-Aware Consensus) is stranded — the real Collective CAI paper
is not present in the card set (that stem holds the Sycophancy paper). Unverifiable from
cards, but a consequence of the pre-flagged swap, not an authoring error.*

---

## Conclusion

**21 sampled claims across all 6 documents: 21 VERIFIED, 0 MINOR-DRIFT, 0 MISATTRIBUTED,
0 WRONG-NUMBER.**

Every sampled number, comparative statement, and paper characterization traced cleanly to
its cited card or digest, in most cases as a verbatim or near-verbatim match. The
`benchmark-landscape-statistics.md` digest-transcription discipline is strong: statistics
are copied faithfully, and the doc proactively flags its own computed-vs-digest divergences
with the authoritative figure named. The literature layer looks **trustworthy** at
spot-check depth — the citation apparatus is reliable and the authors handled the known
CCAI/Sycophancy card swap correctly (tagging sycophancy claims to the actual card content).
The one residual is the stranded participatory-CAI claim, which is a downstream artifact of
the already-known card-naming issue rather than a verification failure.
