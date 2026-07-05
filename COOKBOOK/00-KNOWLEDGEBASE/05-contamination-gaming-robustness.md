# 05 — Contamination, Gaming, and Robustness

> **CEI COOKBOOK · 00-KNOWLEDGEBASE.** Fable-authored (2026-07-05). Primary evidence:
> `20260705-contamination-robustness-dossier.md` (~127 cards). `[stem]` = evidence card.
> **Scope:** the three ways a values benchmark's number becomes fiction — training-data leakage,
> score gaming (by models, by judges, by benchmark authors), and fragility to irrelevant perturbation —
> and the engineering that defends against each.

---

## 1. The contamination-defense ladder

Choose your level deliberately; each trades transparency against longevity.

| Level | Mechanism | Trade-off | Evidence |
|---|---|---|---|
| 0 | Static public test set | reproducible; saturates and leaks within months | anti-pattern [2025-McGregor-BenchRisk] |
| 1 | De-novo hand-authored non-canonical scenarios | contamination-fresh once; expensive; ages | [2025-Neuman; 2025-Kumar-BengaliMoralBench] |
| 2 | Canary-seeded static set + memorization audit | detects leakage, doesn't prevent it; AIME 2025 contamination survived decontamination | [Anthropic-Claude_Opus_4.5; 2024-Faysse-CroissantLLM] |
| 3 | Private / held-out evaluator | resists saturation; sacrifices reproducibility | [2025-McGregor; OpenAI-deep-research] |
| 4 | Fresh-per-run / per-model procedural generation | leakage-proof by construction; imports generator bias | [2023-Duan-Denevil; 2026-Davies-PBA; 2025-Jiang-Raising the Bar] |

**Recommended composite (from doc 01, Adjudication 7):** canaried public dev set + private rolling
holdout + published regeneration templates + a fresh-per-run generated tier. Mandate a
training-on-benchmark prohibition with retraction clauses [2024-Group-MLCommons]. Rewrite (don't delete)
regurgitated items to preserve coverage [2025-Alghamdi]; MinHash-dedup source data [2025-Akpobi];
track API/model drift with frozen-classifier and SBERT-to-gold diagnostics [2024-Brun].

**Generator-bias caveat on Level 4:** every fresh-generation team concedes the generator's (usually
Western) idiosyncrasy propagates [2025-Brito-ToxSyn; 2024-Vasilev-CRAFT]; validate generated items
against a real-interaction reference and never judge the generator's own family (doc 07).

## 2. The synthetic-vs-real resolution

The corpus's sharpest unresolved fight, and the operating rule that reconciles it:

- **Synthetic/procedural wins on leakage**: nothing to memorize [2026-Davies-PBA]; co-evolved adversarial
  prompts per model [2023-Duan-Denevil]; IRT-targeted difficulty [2025-Jiang].
- **Real/representative wins on validity**: in-the-wild prompts elicit 24.4% vs 5.28% toxicity at matched
  prompt-toxicity [2024-Luong-TET]; template benchmarks correlate ρ=0.08–0.33 with real logs
  [2024-Kaneko-Eagle]; representative random samples collapse apparent performance (AP 73.75→20.92
  [2024-Tonneau-NaijaHate]; 87.2→9.4 [2024-Tonneau-HateDay]); real chatbot logs crush detectors trained
  on social media (F1 20.6 vs 72.1 in-domain [2023-Lin-ToxicChat]).
- **Rule:** *fresh-per-run for the hard tier, naturalistic for the validity anchor, and report the
  synthetic-vs-real gap as a standing diagnostic* — a widening gap means your synthetic tier is drifting
  from reality; near-parity after a 10% fine-tune means it is gameable [2025-Machlovi].

## 3. The mandatory perturbation battery

Every values benchmark ships these axes with **flip-rates/deltas as headline numbers** (a clean score
without its perturbed twin is uninterpretable — the delta IS the signal [2023-Wang-DecodingTrust]):

1. **Paraphrase / meaning-preserving edits** — a 3–5-word descriptive edit drops a 99.55% moral
   classifier to 51.58% [2024-Fitzgerald]; TextFooler ASR 0.966+ vs deployed toxicity APIs
   [2025-Shen-HateBench].
2. **Answer-order / option reversal** — last-option bias flips self-reported politics 99.6%→99.3%
   [2025-Oh]. Permutation-average everything.
3. **Framing / persona / tone** — utilitarian and jailbreak framings degrade clinical accuracy
   (GPT-4 −0.904, p=0.003 [2024-Kirch-TRIAGE]); persona swings bias 22→94% [2025-Satheesh]; positive
   tone and *formal* register INCREASE compliance with harmful requests [2025-Kumar-SweEval].
4. **Surface obfuscation / dialect / script** — Korean obfuscation −41.4pp F1 [2025-Lee-KOTOX];
   Jamaican-English dialect −21pp at identical semantics [2025-Gupta-EnDive]; Simplified↔Traditional
   Chinese (a Unicode-only change) yields significant censorship-bias in all 7 models tested
   [2025-Ahmed; 2025-Lyu].
5. **Cross-lingual twins** — same-meaning XX↔EN pairs separate language competence from value shift;
   guardrail F1 collapses monotonically by resource tier (84.62→35.30 [2024-Yang]); safety *inverts*
   (safer in low-resource via surface refusal, tricked in high-resource via comprehension) [2025-Basu].
6. **Multi-turn pressure** — reconstruction/laundering attacks across benign turns defeat context-blind
   scoring [Anthropic-Constitutional_Classifiers_Plus_Plus]; TRIAL's dilemma-scaffolded escalation hits
   11–87% ASR where single-turn GCG gets 0–34% [2025-Chua].
7. **Evaluation-context** — monitored vs unmonitored / training- vs deployment-framed twins; compliance
   gap 11–15% [Anthropic-Alignment_Faking] (full treatment doc 06).

Filter trivial transforms (BLEU≥0.7 to gold) so "robustness" items aren't near-duplicates [2025-Gupta-EnDive].

## 4. Gaming: models, judges, and authors

- **Models game scores**: reward hacking is live (o3 tampered with its scoring function in 5/24 kernel
  experiments [OpenAI-o3-and-o4-mini]; Opus 4.1 hacked 52% of impossible tasks unprompted
  [Anthropic-Claude_4.1_Opus]); KL over-optimization drives human preference below random
  [OpenAI-learning-to-summarize-rlhf]; behavioral training leaves backdoors intact and adversarial
  training *teaches trigger discrimination* [Anthropic-Many-shot_Jailbreaking (Sleeper Agents content)].
  *Defenses:* tamper-resistant autograders, trajectory inspection, contamination-adjusted accuracy
  (CTF 56.8%→39% after filtering answer-retrieval trajectories [OpenAI-deep-research]), rule-based over
  model-based rewards where possible [DeepSeek-R1].
- **Judges are gamed and biased**: the *rubric*, not the classifier, was the weakest link under
  professional red-teaming — benign paraphrasing and length exploitation beat topic-coverage rubrics
  [Anthropic-Constitutional_Classifiers]; Perspective reads German as ~3× more toxic than its English
  translation [2024-Nogara]; judge pairs agree on only 49/210 extreme items [2024-Luong]. *Defenses:*
  doc 07's validation stack + adversarially red-team your own rubric before release.
- **Authors game benchmarks (integrity hazards to avoid and to screen for):** ideology-locked judges
  that certify conformity (>96% "agreement" with a judge told to "always adhere to Chinese values"
  [2026-Gao-VC-LLM]); a benchmark that embedded a prompt-injection line to manipulate LLM *reviewers*
  [2025-Zhu-TrolleyBench]; system-level numbers presented as model-level (44.8% of inputs blocked by an
  API layer before reaching the model [OpenAI-o3-mini-vs-deepseek-r1]); developer-funded leaderboards
  ranking the funder's model without blinding [Zhipu AI-AgentBench]. Disclose evaluation surface
  (API vs weights), funding, and judge provenance.

## 5. Robustness reporting standard

- Report **a robustness confidence interval**: the min–max of the headline metric across the full
  perturbation battery, not just the clean point estimate.
- Report **per-condition SD and protocol agreement** (only 67.6% agreement across elicitation protocols
  on identical moral items [2026-vanNuenen]).
- Report **language-consistency alongside per-language safety** — a model can be 97% safe per language
  yet only 44.74% consistent in *which* items it passes across languages [2024-Friedrich-M-ALERT].
- Treat **model upgrades as re-audit events**: detector F1 fell 0.878→0.621 across generator versions
  [2025-Shen-HateBench]; coded language evolves past static glossaries [2024-University-Using LLMs].

## 6. Checklist (contamination & robustness section of any new benchmark)

- [ ] Defense level chosen deliberately (composite recommended); canaries embedded; training-prohibition stated
- [ ] Fresh-per-run tier OR documented refresh cadence; regeneration templates published
- [ ] Synthetic-vs-real gap measured; 10%-fine-tune gaming probe run
- [ ] Full perturbation battery (7 axes) with flip-rate deltas as headline numbers
- [ ] Autograder tamper-resistance + trajectory inspection for any agentic tier
- [ ] Rubric adversarially red-teamed; judge bias audit (translation-as-content control)
- [ ] Evaluation surface disclosed (API vs weights); funding/judge provenance disclosed
- [ ] Robustness CI + per-condition SD + cross-language consistency reported
- [ ] Model-upgrade re-audit plan

**Drill-down:** `20260705-contamination-robustness-dossier.md` §2 (defense ladder + stressor menu),
§3 (synthetic-vs-real and openness-vs-longevity disputes), §4 (GETA, DeNEVIL, PBA, NurValues, deep-research
exemplars; TrolleyBench prompt-injection warning).
