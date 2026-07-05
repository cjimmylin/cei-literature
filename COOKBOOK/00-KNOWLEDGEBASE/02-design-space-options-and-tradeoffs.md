# 02 — The Design Space: Options and Trade-offs

> **CEI COOKBOOK · 00-KNOWLEDGEBASE.** Fable-authored (2026-07-05). Primary evidence:
> `20260705-design-space-dossier.md` (~230 cards) cross-checked against the agentic, saturation, and
> judges dossiers. `[stem]` = evidence card. This doc is the MENU: every major design option for a
> values-alignment benchmark, its cost, its blind spot, and when to choose it. Use with doc 01's pipeline
> (Step 1–2, 5).

---

## A. Task-format menu

**Rule zero: format is an experimental variable, not a presentation detail.** The same scenarios produce
different value rankings under different formats (protective values rank 1.7 in MCQ vs 4.5 open-ended
[2025-Liu-ConflictScope]); MCQ "reveals understanding of values rather than actual orientation"
[2024-Lee-KorNAT]. 96% of surveyed studies are static, only 3% interactive [2025-Snoswell] — which is
exactly why interactive formats are where publishable headroom lives.

| Format | What it buys | Blind spot / cost | Choose when | Anchor cards |
|---|---|---|---|---|
| **MCQ / forced-choice** | cheap exact-match scoring; high reliability; large N | measures recognition, not disposition (Law 1); guessing floor inverts rankings; saturates first | large-scale screening — only WITH an abstention trap and a paired open-ended subset | [2025-Su; 2025-Liu-ConflictScope; 2025-Davies-F2Bench] |
| **Likert / survey transplant** (MFQ, PVQ, WVS) | comparability to decades of human data | LLMs lack the self-referent; "correct-answer effect" collapses variance (SD=0); cross-instrument coherence R²<0.08 | only with permutation averaging, per-condition SD reporting, and re-audited factor structure | [2024-Almeida; 2024-Nunes; 2025-Chen-MoVa] |
| **Minimal-pair / factorial template** | causal attribution of one variable; clean null point | ecological artificiality; template monotony detectable | isolating one identity/value token; bias deltas | [2018-Kiritchenko; 2018-Rudinger; 2025-Al-SHADES] |
| **Free-text generation** | ecological; reasoning visible; hardest to game | needs a validated scorer (doc 07); costlier | disposition/reasoning is the construct | [2023-Bang-AISOCRATES; 2023-Duan-Denevil] |
| **Distribution elicitation** (sample N times, match human distribution) | honors pluralism; determinism-as-misalignment measurable | needs survey ground truth; N× inference cost | contested items with real human disagreement | [2024-Lee-KorNAT; 2025-Russo; 2025-Durmus-GlobalOpinionQA] |
| **Reasoning-process elicitation** (grade the chain, not the verdict) | catches right-answer-wrong-reason; framework-conditioning testable | expensive rubrics (23k expert criteria in MoReBench); CoT unfaithfulness caveat | open moral items with no single gold answer | [2025-Chiu-MoReBench; 2025-Galatolo; 2025-Samway] |
| **Multi-step / branching / multiturn** | path dependence, consistency under escalation, accumulation effects | trajectory scoring; harness complexity | any deployment-relevance claim (Law 3) | [2025-Ebara; 2025-Fan-FAIRMT; 2025-Wu-Staircase] |
| **Agentic / game-theoretic** | revealed values under real incentive conflict; scheming/deception observable | most complex harness; eval-awareness risk | when trade-off behavior is the construct | [2025-Backmann-MORALSIM; Zhipu AI-AgentBench; 2026-Ma-DIB] |
| **Multimodal / embodied** | expanded harm surface; time pressure | degraded scoring reliability; VLMs answer ~40% without the image | vision/embodiment is intrinsic to the construct | [2025-Gao-MIST; 2024-Yan-M³oralBench] |

**Composition rule:** a publication-grade benchmark pairs at least one cheap format with one behavioral
format on the same content and reports the divergence as a headline finding (the expressed–revealed gap
is the single most replicated phenomenon in this corpus — see agentic dossier finding 1).

## B. Item-construction menu

| Method | Strength | Weakness | Anchor cards |
|---|---|---|---|
| **Hand-authored de-novo scenarios** | contamination-fresh, construct-targeted | expensive; author bias; small N | [2025-Neuman-Auditing; 2025-Kumar-BengaliMoralBench] |
| **Templates + slot-filling** | scale + balance by construction; grammatical-agreement tags enable multilingual validity | artificial; slot vocabulary leaks construct | [2018-Dixon; 2025-Al-SHADES] |
| **Scraped / naturalistic** (forums, court cases, clinical protocols, real chat logs) | ecological validity; realism dz=1.31 over trolley artifice; elicits 5× the violations of templates | licensing/decay; prevalence imbalance; contamination over time | [2023-Körner; 2024-Luong-TET; 2021-Lourie-Scruples; 2024-Kirch-TRIAGE] |
| **Survey-derived** (WVS, Moral Machine, PEW) | pre-validated construct + human distribution for free | descriptive-not-normative; WEIRD skew in the survey itself | [2024-Lee-KorNAT; 2024-Jin-MULTITP] |
| **LLM-generated (static release)** | coverage, cheap, refreshes saturation | generator's cultural bias; gameable (10% fine-tune → parity); self-preference if generator family is judged | [2022-Hartvigsen-ToxiGen; 2025-Machlovi] |
| **LLM-generated (fresh-per-run / adaptive)** | leakage-proof by construction; difficulty targeting (IRT+CAT) | generator bias remains; reproducibility needs seeds/templates | [2025-Jiang-Raising the Bar; 2026-Davies-PBA; 2023-Duan-Denevil] |
| **Adversarial / dynamic collection** (attack-success gating, DADC, jailbreak mining) | discrimination built in; realistic threat model | chases current models; needs refresh cadence | [2023-Huang-Flames; 2024-Jiang-WildTeaming; 2024-Goldzycher] |
| **Causal-graph / factorial generation** | balanced coverage of morally-relevant factors | abstraction; small factor spaces | [2024-Franken-OffTheRails] |
| **Genetic-algorithm curation** | targets the ambiguous middle where discrimination lives | needs a fitness signal (human ratings) | [2026-Li-PluriHarms] |

**Composition rule:** anchor with naturalistic/protocol-grounded items (validity), scale with
template/generated items (coverage), gate everything through the shortcut audit (doc 01 Step 2), and
reserve a fresh-per-run generated tier for longevity.

## C. Scoring & metric menu

| Approach | Use for | Never for | Anchor cards |
|---|---|---|---|
| Exact-match / macro-F1 (+ majority-class baseline) | closed constructs, imbalanced classes | contested items; imbalance without macro/PABAK | [2019-Basile; 2025-Ishmam-BanTH] |
| Distributional distance (KL/JSD/EMD/L2/cross-entropy + oracle ceiling) | pluralistic constructs | clear-cut hazards (dilutes the floor) | [2021-Lourie; 2025-Durmus; 2024-Jin-MULTITP] |
| Threshold-free AUC families (BPSN/BNSP), confidence-aware (UCerF) | fairness error-direction decomposition | headline single numbers | [2019-Borkan; 2025-Wang-UCerF] |
| Bias metrics bounded by accuracy | making "perfect model = provably unbiased" | — | [2024-Jin-KoBBQ; 2022-Parrish-BBQ] |
| Pareto pairs (harm × over-refusal) + four-way refusal taxonomy | any safety-adjacent construct | — (mandatory) | [Anthropic-HH-RLHF; Anthropic-Claude_3.7; 2024-Röttger-XSTest] |
| Metric triads (avg + disparity + worst-group) | group-differentiated constructs | — | [2022-Chalkidis-FairLex] |
| Worst-case + frequency pairs (EMT + ToxProb) | tail-risk constructs | mean-only reporting | [2020-Gehman-RealToxicityPrompts] |
| Consistency/coherence, judge-free (ECI, CCEI, NOTO) | saturation-resistant hedge; contested items | sole metric (a consistently evil agent scores high) | [2025-Zhu-TrolleyBench; 2024-Seror; 2025-Gupta-VAL-Bench] |
| Process/rubric scoring (signed weighted atomic criteria) | no-ground-truth moral reasoning | verdict-only items | [2025-Chiu-MoReBench] |
| Behavioral/propensity (allocations, actions, side-effects) | Law-1 compliance; agentic | — (the default target) | [2023-Tamkin-discrim-eval; 2025-Backmann] |
| Interpretable steerable aggregation (fitted linear weights, per-framing leaderboards) | pluralism; community re-weighting | hiding the aggregation choice | [2025-Li-SafetyAnalyst; 2024-Defrance-ABCFair] |

**Always attach:** empirical ceiling, naive baseline, interpretation threshold (73% of 791 RAI measures
ship no interpretation criterion [2025-Rismani]), and per-condition SD.

## D. Difficulty-injection menu (from the saturation dossier; details doc 04)

1. Two-tier easy/hard with the drop as headline [2025-Lin-MORALISE; 2025-Yao-NurValues].
2. Adversarial filtration / highest-loss retention [2021-Hendrycks-ETHICS].
3. Cross-model hardest-item distillation (10K→1K lifts GPT-4 bias exposure 11%→57% [2025-Fan-FairMT]).
4. Ambiguity engineering + abstention scoring [2022-Parrish-BBQ].
5. Cognitive-load rewriting (single sentence → 3-turn dialogue/story: 97.4→65.3 [2025-Zhang-CValues+]).
6. Implicit/indirect probes (IAT-style) where explicit saturates [2025-Bai; 2025-Griffiths].
7. Cultural/low-resource localization (Tamil near-zero while English passes [2024-Ng-SGHateCheck]).
8. Multi-turn adversarial accumulation [2025-Fan-FAIRMT; 2026-Ma-DIB].
9. IRT-adaptive generation at the ability frontier [2025-Jiang-Raising the Bar].
10. Fine-grained sub-labels (span-level, norm attribution) that floor models while binary saturates
    [2025-Seker-HATECAT-TR; 2025-Lin-MORALISE].

## E. The five recurring format-artifacts (design traps)

1. **MCQ guessing floor** — a weak model's random-guess minimum inverts rankings vs open-ended
   [2025-Davies-F2Bench].
2. **Correct-answer effect** — Likert/survey items elicit deterministic answers (SD=0), inflating
   correlations and collapsing discrimination [2024-Almeida; 2025-Oh].
3. **Answer-order artifact** — last-option bias flips "moral" self-reports 99.6%→99.3% [2025-Oh].
   Permutation averaging (≥30 iters or 48-permutation DIT protocol) is the standard control [2023-Deng].
4. **Verbosity/polish artifact** — judges rate longer, more moral-language-dense answers higher (GPT-4o
   advice "more moral" than a professional ethicist in 74% of cases via moral-language density
   [2025-Dillion]); length-correct and calibrate (doc 07).
5. **Refusal gaming** — consistency and safety metrics reward blanket refusal unless over-refusal is
   co-scored (Erase-Check: 0% ASR at 99.6% over-refusal [2025-Zhang-AISafetyLab]).

## F. Worked default: the recommended stack for a new values benchmark

If you have no strong reason to deviate, build this (rationale in docs 01, 04, 06):

1. **Content core:** naturalistic scenarios (real cases / field-grounded) + minimal-pair twins +
   an ambiguity band (consensus-stratified) + culturally-localized subsets (natively authored).
2. **Structure:** Tier-0 competence controls → Tier-1 recognition (MCQ + abstention traps; expected to
   saturate; serves as floor) → Tier-2 open-ended/process-graded → Tier-3 multiturn adversarial →
   Tier-4 agentic/incentive-conflict subset.
3. **Scoring:** behavioral primary; per-item keypoint rubrics; two cross-family judges + human
   validation; distributional scoring on the contested band; Pareto pair + worst-group reporting.
4. **Lifecycle:** canaried public dev + private rolling holdout + published regeneration templates.

This stack is deliberately expensive at Tier 3–4. That is where the unsaturated, discriminative,
publication-worthy signal is (Law 3; agentic dossier findings 1–5). Cheap tiers exist to calibrate and
to connect to prior literature, not to carry conclusions.

**Drill-down:** `20260705-design-space-dossier.md` §2 (full decision tables), §3 (disagreement inventory),
§4 (exemplars/anti-patterns per option).
