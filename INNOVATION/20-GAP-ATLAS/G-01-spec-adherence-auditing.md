# G-01 — Spec-Adherence Auditing

**Stage A** · **Ratings S/T/F: H/H/H** · **Programs: RP-01 SPECGRADE** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## Statement                       [KERNEL — FROZEN]
The vault holds effectively zero literature on auditing whether models follow their published behavioral specifications, twelve months after spec-adherence auditing became a recognized empirical subfield with its own harnesses and headline results.

## Why it matters                  [KERNEL — FROZEN]
Specs are now the constitutions-of-record — the only public, versioned statement of what "aligned" is supposed to mean for a deployed model. If adherence is unmeasured (or measured only by the labs themselves), the central outer-alignment claim of the deployment era is unverifiable by anyone outside. Severity H because every downstream governance and safety-case argument routes through it; CEI-fit H because adherence auditing IS benchmark craft aimed at a new target document.

## Evidence                        (corpus + field)
**Corpus baseline (2026-07-07):** spec-adherence returns ~0 abstract hits across 2,368 paper notes. The vault's mass sits in evaluation-side categories (Helpfulness/RLHF 299, Moral Reasoning 268, Fairness 233, Cultural 193); the *target document* whose adherence would be audited is absent as an object of study.

**Field:** an auditing subfield crystallized in under a year, driven by two forces (Front A causal story): reasoning models made inference-time spec consultation trainable (deliberative alignment), and governance pressure pushed labs to publish versioned, CC0-licensed value documents (OpenAI Model Spec revisions 2025-02→2025-12; Claude's Constitution 2026-01-22). Once the target is public, adherence becomes empirical. Three founding artifacts:
- **SpecEval** (Stanford; arXiv:2509.02464, NeurIPS 2025): parse spec → generate probes → measure spec↔output↔self-judgment consistency; gaps **up to 20 points** across 16 models, 6 developers.
- **Stress-testing model specifications** (Anthropic + Thinking Machines; arXiv:2510.07686): 300k value-tradeoff scenarios, 70k+ significant cross-model divergences (this artifact is the deeper half — see G-02).
- **Model Spec Evals** (OpenAI, Mar 2026): open harness, compliance 72% (GPT-4o) → ~84–89% (GPT-5.x); Thinking > Instant. Adherence is now a tracked, versioned capability.

## State of the art
The subfield measures adherence but not the spec itself; **nobody owns "how to write a good spec"** (Front A actors). Harnesses are lab-run or lab-adjacent, so the outer-alignment adherence claim is currently self-attested. Third-party, values-content adherence probing across ≥2 frontier models is the open niche RP-01 targets — reproducing the published 15–20-point gap on independent items would convert a lab metric into an external, citable check. CEI's item-writing and validity machinery (WCF→registry, Decalogue, Galatians 5 pipelines) transfers directly to probe construction.

## What closing looks like         [KERNEL — FROZEN]
M1 — the auditing literature (SpecEval, stress-testing, Model Spec Evals) is acquired, extracted, and classified under a specification taxonomy code. M2 — CEI can run a third-party values-content adherence probe set against at least two frontier models and reproduce the published 15–20-point gap finding on its own items. M3 — spec-adherence results become a standing, citable CEI output (audit report or diff series) that external work references.

## CEI response                    [KERNEL — FROZEN]
RP-01 SPECGRADE owns this gap; its distinguishing move is grading the spec ex ante rather than only auditing the model — see G-02, which is the deeper half of the problem.

## OPUS-EXPAND checklist           (LIVING)
- [ ] Deep-read SpecEval (2509.02464) and summarize its parse→probe→consistency method into §State of the art, including how it defines the consistency gap.
- [ ] Deep-read Stress-Testing (2510.07686) and extract the exact scenario-generation protocol reusable as CEI probe substrate.
- [ ] Add a replication-status table: which of the three headline gaps (SpecEval 20pt, Model Spec Evals 72→89%, stress-test divergence) CEI can reproduce with API-only access and no lab harness.
- [ ] Confirm the OpenAI Model Spec Evals harness is open and record its license + probe families; check overlap with RP-01 values-content probes.
- [ ] Check Front A watch-list trigger: has Model Spec Evals added values-content clauses beyond safety/compliance? If so, direct-overlap check with RP-01.
- [ ] Map SpecEval's 16-model / 6-developer coverage against CEI's target frontier set to size the M2 two-model reproduction.

## Sources                         (evidence classes marked)
- SpecEval — arXiv:2509.02464 (NeurIPS 2025) — **SEARCH-CONFIRMED** — G-01 anchor.
- Stress-Testing Model Specifications — arXiv:2510.07686 — **SEARCH-CONFIRMED** — spans G-01/G-02.
- Reasoning over Boundaries / SpecBench (Align3) — arXiv:2509.14760 — **SEARCH-CONFIRMED** — test-time deliberation, P2.
- Model Spec Evals (OpenAI, Mar 2026) — non-arXiv harness — **SEARCH-CONFIRMED**.
- OpenAI Model Spec (versioned, 2025-12-18) — https://model-spec.openai.com — **SEARCH-CONFIRMED** (non-arXiv manual ingest).
- Corpus grep baseline (spec-adherence ~0 hits, 2,368 notes, 2026-07-07) — **VERIFIED** (`../02-gap-atlas.md`).
