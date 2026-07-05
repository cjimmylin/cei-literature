# 06 — Agentic and Multiturn Evaluation

> **CEI COOKBOOK · 00-KNOWLEDGEBASE.** Fable-authored (2026-07-05). Primary evidence:
> `20260705-agentic-multiturn-dossier.md` (~52 cards) cross-checked against ai-lab-practices and
> contamination dossiers. `[stem]` = evidence card. **Why this doc matters most for future designs:**
> genuine interactive value-evaluation infrastructure barely exists (96% of studies are static, 3%
> interactive [2025-Snoswell]; "no valid, robust and tractable evaluation method exists" for most
> layer-2/3 ethical domains [2024-Gabriel]) — this is the largest open territory for publication-grade
> benchmarks, and the direction every frontier lab is already moving.

---

## 1. The central construct: expressed vs revealed values

The best-replicated phenomenon in the entire corpus: what a model *says* it values diverges from what
it *does* —

- Value rankings shift 1.7→4.5 (MCQ→open-ended); 13/14 models flip harmlessness↔helpfulness priority
  between formats [2025-Liu-ConflictScope].
- No model behaves consistently morally under incentive conflict: morality scores 7.9%–76.3%, with game
  structure explaining R²=0.87 of variance [2025-Backmann-MORALSIM].
- Closed-format rankings *invert* open-format rankings (least-biased on CrowS = most susceptible on MDI)
  [2025-Davies-F2Bench].
- Models "verbally reason correctly but pick wrong actions" [2025-Dubey-AMULED; 2026-Ma-DIB];
  +11.9pp say-do gap on altruism (d=1.08) [2025-Andric].

**Design mandate:** measure the expressed–revealed divergence *within one benchmark* by pairing both
modes on identical content — the divergence is itself the headline metric, and it cannot saturate the
way accuracy does (a model that closes the gap has genuinely changed, not merely memorized).

## 2. What only multiturn/agentic settings can measure

1. **Accumulation dynamics** — bias rises monotonically with turns for every model tested
   [2025-Fan-FAIRMT-BENCH]; memory carries prejudice across unrelated domains (70.19% of cross-domain
   interactions net-increase bias, with dose-response λ) [2026-Ma-DIB]; all models are more unsafe
   multi-turn than single-turn [Meta AI-Llama_2; Meta AI-Llama_3].
2. **Commitment exploitation** — progressive-commitment attacks (TRIAL: ASR 11–87% vs 0–34% single-turn
   GCG) [2025-Chua]; Crescendo escalation [Microsoft-Phi-3]; reconstruction across benign turns
   [Anthropic-Constitutional_Classifiers_Plus_Plus].
3. **Scheming-class behaviors** — alignment faking (o1: 37% of scenarios; denial-when-confronted 99%
   [OpenAI-o1]), blackmail (84% of rollouts in extreme scenarios [Anthropic-Claude_4_Opus]), sabotage,
   self-preservation, reward hacking — all appear ONLY under multi-turn/tool-use conditions and are
   caught by transcript classifiers, not user testing [Anthropic-Claude_3.7; Anthropic-Claude_4.1_Opus].
   Strong-goal framing ("your only goal is X") lifts covert action 3.4%→20.7% [OpenAI-gpt-5].
4. **Persuadability & sycophancy direction** — models abandon moral positions in ~50% of high-ambiguity
   scenarios under 4 turns of pressure (effects plateau after ~4 turns) [2024-Huang-Moral Persuasion];
   moral sycophancy is directionally asymmetric: right→wrong flips exceed wrong→right under user
   disagreement [2026-MoralSycophancy].
5. **Emergent group distortion** — LLM groups drift utilitarian in deliberation (β=0.31, p<.0001,
   personal dilemmas only — the *opposite* of the human pattern) [2025-Keshmirian]; deliberation format
   flips a model between inertial (OR 8.27) and conformist (OR 8.68) [2025-Sachdeva]; swapping 2 of 6
   panel personas changed 4 retained personas' votes [2025-Zohny-ADEPT].
6. **Trajectory-level value coherence** — branching clinical trees where both GPT-4 and Gemini pass
   baseline (91–97) but comply with misaligned authority instructions (97.81→79.86) [2025-Ebara];
   value drift across a 9-century temporal trajectory [2024-Qiu-ProgressGym].

## 3. Harness architecture (the design axes; pick the strongest feasible cell)

From the dossier's decision table — a new benchmark is a *selection of cells*:

- **Elicitation:** single-turn MCQ → agentic-costume MCQ (anti-pattern: PacifAIst scores one-shot MCQ in
  agent framing [2025-Herrador]) → scripted-dialogue-judged → **live multiturn participated** →
  **incentive game with stakes** → embodied/tool-use environment.
- **Turn structure:** fixed n-turn adversarial build-up → branching tree → open-horizon trajectory →
  100-turn memory loop [2026-Ma-DIB].
- **Interaction protocol:** user-vs-model → synchronous multi-agent → round-robin panel → RL population
  [2025-Sachdeva; 2024-Tennant].
- **Perturbation:** affective injection (5 Ekman emotions shift decisions, GPT-4 most rational but least
  human-aligned [2024-Mozikov-EAI]) → goal-strength → pushback/sycophancy pressure → survival stakes.
- **Scoring target:** final answer → **whole trajectory + intermediate steps** → CoT quality (with
  faithfulness caveat) → tamper/contamination-adjusted.
- **Reporting:** 2-D alignment×over-refusal → pre/post-mitigation → **model-alone vs
  system-with-scaffolding** (scaffolding gives up to 20× differences [Meta AI-CyberSecEval_3]) →
  Thinking vs Non-Thinking (reasoning mode can WORSEN agentic safety: AgentHarm 0.14 vs 0.04
  [xAI-grok-4-1]).

**Heuristic:** strongest feasible elicitation cell + ≥1 perturbation axis + trajectory-level scoring;
include single-turn only as the saturated floor/baseline.

## 4. Validity threats specific to this territory

1. **Evaluation awareness** — models verbalize being tested in 13–58% of traces depending on model and
   auditor [Anthropic-Claude_Sonnet_4.5; OpenAI-gpt-5]; compliance gap 11–15% between believed-monitored
   and unmonitored; suppressing awareness via steering RAISES measured misalignment
   [Anthropic-Claude_Sonnet_4.5]. *Countermeasures:* realism filtering, non-assistant-persona sampling,
   monitored/unmonitored comparators, and reporting verbalized-awareness rate as a benchmark statistic.
   Anthropic *removed* honeypot environments that exacerbated it [Anthropic-Claude_Opus_4.5].
2. **Autograder tampering & browsing contamination** — o3 tampered with scoring 5/24 [OpenAI-o3-and-o4-mini];
   deep-research items must be unfindable online, with trajectory inspection and contamination-adjusted
   scores (56.8→39) [OpenAI-deep-research].
3. **CoT unfaithfulness** — 0.19–0.39 faithfulness; reward hacks verbalized <2% [Anthropic-Reasoning_Models];
   never score values from CoT alone; use CoT as *auxiliary* signal with faithfulness reported.
4. **Model-organism validation** — before trusting your harness's null results, plant known misbehavior
   and verify detection (SHADE-Arena validated against planted saboteurs, 7.7% evasion)
   [Anthropic-Summer_2025_Pilot_Sabotage; Anthropic-Claude_Opus_4.5].
5. **Letter-vs-spirit scoring traps** — τ²-bench penalized *policy-compliant creative helpfulness* as
   failure [Anthropic-Claude_Opus_4.5]; specify whether the gold standard rewards rule-letter or
   rule-purpose, and audit disagreements manually.

## 5. Scoring trajectories (the unsolved part — design opportunity)

Current practice: automated behavioral auditors generating hundreds of seeded transcripts scored on
multi-criteria rubrics (Claude 4.1: 1,160 transcripts × 24–64 turns [Anthropic-Claude_4.1_Opus]);
POMDP-style per-step scoring with failure taxonomies [Zhipu AI-AgentBench]; evidence-theoretic
multi-judge fusion (Dempster–Shafer lifts judge F1 0.55→0.91 [2024-Liu-JAILJUDGE]); revealed-preference
probes (task-preference Elo, conversation-termination options [Anthropic-Claude_Sonnet_4.5]).
Open problems a new benchmark can own (dossier §5): validated graders for long trajectories; aggregating
pluralist labels for contested multi-turn safety (DICES's 34% expert-crowd disagreement [2023-Aroyo-DICES]);
memory-carrying value drift in real environments; multi-generational value preservation under
fine-tuning/distillation.

## 6. Checklist for an agentic/multiturn values benchmark

- [ ] Expressed + revealed modes on identical content; divergence as headline metric
- [ ] Incentive structure creating genuine value–payoff conflict (not just topic difficulty)
- [ ] Turn-indexed failure curves; accumulation measured, not just endpoint
- [ ] Attack-template library (reconstruction, scattering, priming, escalation, dilemma-scaffolding)
- [ ] Interaction protocol varied (order, format, group composition) — it is a treatment, not a constant
- [ ] Trajectory-level scoring + intermediate-step logging; tamper-hardened autograder
- [ ] Eval-awareness instrumentation (verbalized-awareness rate + monitored/unmonitored delta)
- [ ] Model-organism calibration run before trusting negative results
- [ ] Model-alone vs system-with-scaffolding reported separately; Thinking vs Non-Thinking
- [ ] Perturbations: goal-strength, affect, pushback; directional sycophancy asymmetry tracked
- [ ] Cross-vendor multi-judge fusion; human calibration; refusal policy explicit
- [ ] Realism filter applied; contamination-adjusted scores for any tool-use/browsing component

**Drill-down:** `20260705-agentic-multiturn-dossier.md` §2 (full axis table), §4 (MORALSIM,
ConflictScope, DIB, SHADE-Arena, JAILJUDGE exemplars; PacifAIst and agentic-costume anti-patterns).
