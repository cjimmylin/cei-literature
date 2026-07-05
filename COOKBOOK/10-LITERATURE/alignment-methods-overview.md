# Alignment Methods — A Descriptive Survey for Values-Benchmark Designers

> **CEI COOKBOOK · 10-LITERATURE.** Descriptive companion to the prescriptive knowledge-base
> doc `../00-KNOWLEDGEBASE/13-ai-lab-alignment-practices.md` (doc 13). Doc 13 tells you *what to do*
> with these facts; this doc is the *methods survey* — what each training technique mechanically is,
> its load-bearing numbers, and what it does to a model's values. Primary evidence:
> `../30-EVIDENCE/20260705-dossiers/20260705-ai-lab-practices-dossier.md` and the 57 lab-report cards
> in `../30-EVIDENCE/20260705-ailabs-cards/`. All statistics are copied verbatim from those cards;
> citation stems in [brackets] map to card filenames. **Why you (the benchmark designer) need this:**
> you cannot measure what training does to model values without knowing what the training *is*. Every
> number below is a signature you can design an item to detect.

---

## 1. The alignment stack, method by method

Frontier labs have converged on one pipeline shape — **SFT → preference/reward model → RL → optional
wrapper classifiers** — while disagreeing on the value-specification layer above it. The methods
below are the interchangeable parts of that stack.

### Supervised fine-tuning (SFT)
The base layer: fine-tune a pretrained model on curated demonstrations of desired behavior. InstructGPT
used **~13k training prompts** (11,295 labeler-written + 1,430 customer) for its SFT stage
[OpenAI-instructgpt]; Llama 2 deliberately *stopped* collecting SFT data at **27,540 examples** once
quality plateaued, judging vendor annotations no longer the gold standard [Meta AI-Llama_2]. SFT sets
the model's default register but is weak as a values mechanism: it teaches surface form, not a ranked
preference over competing goods.

### RLHF + PPO (the InstructGPT / summarization lineage)
The template that defined the field. A reward model (RM) is trained on human pairwise comparisons, then
PPO optimizes the policy against that RM with a **per-token KL-divergence penalty against the SFT
reference policy** to prevent drift: `R(x,y) = r_θ(x,y) − β·log[π_RL(y|x)/π_SFT(y|x)]`
[OpenAI-learning-to-summarize-rlhf]. Key numbers: a **1.3B** RLHF summarization model beat a supervised
model **10× its size** (**61% vs 43%** preference over reference summaries) on **64,832 comparison
pairs** [OpenAI-learning-to-summarize-rlhf]; the **1.3B** InstructGPT was preferred over **175B** GPT-3
[OpenAI-instructgpt]. RMs are trained on all C(K,2) pairs from K=4–9 ranked outputs per prompt to avoid
overfitting [OpenAI-instructgpt].

**The over-optimization cliff.** This is the single most important RLHF fact for a benchmark designer.
Beyond **~250 nats of KL** optimization against the summarization RM, *actual human preference falls
below random* even though RM score keeps climbing [OpenAI-learning-to-summarize-rlhf]. The RM is a proxy;
past a threshold the policy Goodharts it. Anthropic reports the same shape: RLHF "becomes gradually less
robust after ~150k training samples," with reward tracking √D_KL approximately linearly
[Anthropic-Training_a_Helpful_and_Harmless_Assistant_with_RLHF]. **What it does to values:** RLHF does
not install values; it maximizes a learned proxy for annotator preference, and it over-fits that proxy.

### RLAIF / Constitutional AI (self-critique)
Anthropic's Constitutional AI replaces the human-labeled *harmlessness* signal with AI feedback. Two
stages: (1) **SL-CAI** — the model critiques and revises its own responses against randomly sampled
constitutional principles (**4 critique-revision pairs** per red-team prompt), then is fine-tuned on the
revisions; (2) **RL-CAI (RLAIF)** — an AI feedback model uses the constitution to generate the
harmlessness preference labels that train the RM, with **16 principles** randomly sampled per label for
robustness [Anthropic-Constitutional_AI_Harmlessness_from_AI_Feedback]. Crucially, the authors concede
the constitution "was selected in a fairly ad hoc and iterative way for research purposes" and should be
"redeveloped by broader stakeholders" — the normative content is admittedly provisional. They also warn
PM scores "become less calibrated at higher values" (saturation), and that over-training produces
Goodharting: models append boilerplate ("you are valid, valued, and cared for") even to terrorism
prompts [Anthropic-Constitutional_AI_Harmlessness_from_AI_Feedback]. **What it does to values:** it
relocates the normative choice from crowdworkers into a short natural-language document — cheaper and more
auditable in principle, but the document is ad hoc and never fully published.

### DPO (reparameterization — drop the reward model)
Direct Preference Optimization proves the KL-constrained RLHF objective has a closed-form solution: the
optimal reward is `r*(x,y) = β·log[π*(y|x)/π_ref(y|x)] + β·log Z(x)`, so the policy *is* its own implicit
reward model and PPO is replaced by a simple binary cross-entropy over (prompt, preferred, dispreferred)
triples [OpenAI-dpo]. β plays the role of the KL penalty. DPO matched or beat PPO
(**~61% vs ~57%** TL;DR win rate; **0.36 vs 0.26** GPT-4 win rate on out-of-distribution CNN/DailyMail)
[OpenAI-dpo]. It still shows over-optimization at longer training [OpenAI-dpo]. Meta adopted DPO for
Llama 3 (with formatting-token masking and **NLL regularization coefficient 0.2** on chosen sequences),
finding it "requires less compute than PPO at scale" [Meta AI-Llama_3]. **What it does to values:** same
preference target as RLHF, fewer moving parts — the value content is entirely in the preference pairs.

### GRPO and rule-based rewards (the reasoning-model turn)
DeepSeek-R1-Zero applied **Group Relative Policy Optimization (GRPO)** with *only rule-based rewards*
(accuracy via ground-truth matching + format via tag enforcement) directly on the base model, **no SFT**,
driving AIME 2024 pass@1 from **15.6% → 77.9%** over **10,400 RL steps** [DeepSeek-DeepSeek-R1]. The full
R1 adds cold-start SFT and a *second* RL stage combining rule-based reasoning rewards with two model-based
reward models: a **helpfulness RM trained on 66,000 preference pairs** and a **safety/harmlessness RM
trained on 106,000 annotated prompts** — with the model-based preference reward applied *only in the final
400 steps* to contain reward hacking [DeepSeek-DeepSeek-R1]. DeepSeek states the risk plainly: "If the
reward signal is assigned by a model instead of predefined rules, it becomes more susceptible to
exploitation... the policy model may find shortcuts to hack the reward model" [DeepSeek-DeepSeek-R1].
Qwen3 generalizes this to **three reward types** — rule-based, model-based-with-reference, and
model-based-without-reference — across **>20 tasks**, and likewise argues well-designed rule-based rewards
prevent reward hacking [Alibaba (Qwen)-Qwen3_Technical_Report]. **What it does to values:** rule-based RL
is nearly values-agnostic (it optimizes verifiable correctness); the *values* live in the smaller
model-based safety RM, whose training guidelines are undisclosed.

### Safety-specific variants
Labs increasingly split safety out of the main reward signal:
- **Separate safety reward models.** Llama 2 trains an independent **helpfulness RM (70.6% avg accuracy)**
  and **safety RM (64.3%)**, letting it push safety data to 100% while holding false-refusal at **~0.05%**
  [Meta AI-Llama_2]. RM accuracy collapses to **54.5%** (near random) on "negligibly better/unsure" pairs —
  the annotator-disagreement floor [Meta AI-Llama_2].
- **SafetyDPO.** Llama 3 crafts adversarial/borderline response pairs "nearly orthogonal in embedding
  space" so DPO teaches fine-grained good-vs-bad distinctions [Meta AI-Llama_3].
- **Safe-completions.** GPT-5 replaces the binary refuse/comply decision with output-centric training that
  *maximizes helpfulness subject to safety constraints*, aimed at dual-use ambiguity
  [OpenAI-gpt-5-system-card].
- **Deliberative alignment.** OpenAI's o1 is trained to *reason over the safety spec in its
  chain-of-thought*, with the full policy text available at inference. It lifts multimodal
  not_overrefuse from **0.48 → 0.96** and challenging-refusal not_unsafe from **0.713 → 0.92**
  [OpenAI-deliberative-alignment / OpenAI-o1-system-card]. **What it does to values:** moves the
  specification from frozen weights into legible, inference-time reasoning — auditable, but only as good as
  the (usually unpublished) spec.

### Attribute-conditioned SFT (SteerLM / HelpSteer)
NVIDIA discards scalar reward entirely. SteerLM trains an Attribute Prediction Model, annotates data with
it, then does SFT *conditioned on a discrete attribute vector* (e.g. quality=9, toxicity=0). No RL, no RM.
Cost: **1 rating vs 6–36 pairwise comparisons per prompt (~10× lower annotation cost)**; SteerLM used
**1,536 GPU-hours vs 7,168 for RLHF** [NVIDIA-SteerLM / NVIDIA-HelpSteer]. **What it does to values:** it
declines to encode a single value system at all — values become a steerable dial set at inference, which
is a fundamentally different (and benchmark-relevant) posture from RLHF's baked-in preference.

### Classifier wrappers (system-level, outside the weights)
A separate model screens inputs/outputs around the aligned model:
- **Llama Guard** — a Llama2-7B classifier with the taxonomy passed *as input* for zero-shot policy
  swaps; **F1 0.872/0.884** (prompt/response) vs OpenAI API 0.389/0.478 [Meta AI-Llama_Guard]. Llama Guard
  3 cuts violations **−65%** on average [Meta AI-Llama_3].
- **ShieldGemma** — Gemma-2 classifiers (2B/9B/27B); ShieldGemma-9B beats LlamaGuard1 by **+10.8% AU-PRC**
  [Google DeepMind-ShieldGemma].
- **Constitutional Classifiers** — dual input+output classifiers trained from a CBRN constitution
  specifying *both* permitted and restricted content. The load-bearing result: HHH safety training alone
  barely moves attack success (**~16% → ~14% ASR**), but input+output classifiers reach **0.5% ASR**;
  Classifiers++ reaches **0.05% production refusal with no universal jailbreak across 198K attempts** and
  **1,736 red-team hours** [Anthropic-Constitutional_Classifiers / Anthropic-Constitutional_Classifiers_Plus_Plus].
  **What it does to values:** *nothing to the model's values* — it gates behavior at the system boundary.
  This is why model-alone vs system-with-guardrails must be reported separately.

---

## 2. Value-specification approaches (the target above the stack)

The alignment method is neutral about *what* it aligns to; that is set by the specification layer, which
varies by lab and is the layer most often hidden.

- **Private natural-language constitution** — Anthropic's original 16-principle document, admittedly ad
  hoc [Anthropic-Constitutional_AI_Harmlessness_from_AI_Feedback].
- **Participatory / public constitution** — Collective Constitutional AI sources a US-representative
  public constitution via Group-Aware Consensus and lowers BBQ bias on all 9 dimensions at equal MMLU
  [Anthropic-Collective_Constitutional_AI].
- **Model spec + usage policy reasoned over at inference** — deliberative alignment injects "the full text
  of safety policies for the model to reason about during inference" [OpenAI-deliberative-alignment].
- **Steerable attribute vector, no single value system** — SteerLM [NVIDIA-SteerLM].
- **Published system prompt + the model's own reasoning** — xAI's Grok cards.
- **Jurisdictional law / state ideology** — VC-LLM and HKGAI-V1 define "safe" as conformity to
  PRC/PRC-HK law (an anti-pattern: the same-ideology judge certifies conformity, not correctness).

**The transparency gap.** The specification is almost never reproduced in the artifact that cites it. The
Opus 4.5 card "references policy documents but does not reproduce them... Specific constitutional AI
principles or ranked value hierarchies are not directly quoted" [Anthropic-Claude_Opus_4.5_System_Card];
Gemini publishes "no formal model constitution or model spec" [Google DeepMind-Gemini_2.5_Pro_Model_Card];
the o1 card reasons over a spec whose text is absent [OpenAI-o1-system-card]. **A benchmark cannot audit
conformance to a spec it cannot read** — this is both the central gap and (per doc 13) the central design
opportunity.

---

## 3. Preference-data engineering (where the values actually enter)

Because RLHF/DPO learn from preference pairs, the *annotation protocol* is where values are silently
encoded. Four techniques and their evidence:

**Multi-attribute decomposition.** HelpSteer splits helpfulness into **5 attributes on a 0–4 scale**
(helpfulness, correctness, coherence, complexity, verbosity); an OLS of 4 attributes explains **73.0% of
helpfulness variance** [NVIDIA-HelpSteer]. Critically, *removing* the helpfulness attribute *improved*
TruthfulQA (0.5613 → 0.5754) — exposing that black-box preference data carries a **verbosity confound**
(RLHF datasets "prefer longer responses regardless of substance"); the verbosity dial alone moved mean
response length from **422.3 → 1,125.2 characters** [NVIDIA-HelpSteer].

**Forced-choice annotation.** HelpSteer2-Preference removes the "equally good" option. Raw inter-rater
agreement on preferences is only **Cohen's κ = 0.489 (moderate)**; after removing zero-preference (tied)
samples it rises to **κ = 0.878** [NVIDIA-HelpSteer2-Preference]. That gap is the size of the "tie"
ambiguity — and **22% of samples** were tied [NVIDIA-HelpSteer2-Preference].

**Disagreement preservation.** Annotators genuinely disagree, and majority-voting discards signal. Llama 2
reports helpfulness inter-rater reliability (Gwet's AC2 **0.37–0.55**) far below safety (**0.70–0.95**) —
helpfulness is intrinsically more subjective [Meta AI-Llama_2]. On Constitutional AI's origin data,
crowdworker-researcher agreement was only **~63%** [Anthropic-Training_a_Helpful_and_Harmless_Assistant_with_RLHF].

**Who labels (annotator demographics).** This is where WEIRD skew enters. InstructGPT's **40 labelers**
were **53% Southeast Asian / 32% White / 16% Latinx, 75% under 35**, and its data was **~96% English**;
the paper concedes it aligns "to the stated preferences of a specific group... rather than any broader
notion of 'human values'" [OpenAI-instructgpt]. HelpSteer's **~200 annotators were all US-based**, and the
authors warn the data reflects "what is construed as helpful in the United States"
[NVIDIA-HelpSteer]. Llama 2's *pretraining* corpus is **89.70% English**, with "american" in **69.4%** of
nationality documents and "christian" in **33.2%** of religion documents [Meta AI-Llama_2]. The values a
benchmark measures against were set by these specific, non-representative populations.

---

## 4. Measured effects of training on values

The pipeline leaves measurable signatures. A values benchmark should target these directly rather than
generic "morality."

**Sycophancy is structural, not incidental.** Preference optimization *rewards* agreement: "matching a
user's beliefs" is one of the most predictive features of human preference among 23 features, and a
Claude 2 preference model **prefers sycophantic over truthful responses 95% of the time** on
misconceptions [Anthropic-Collective_Constitutional_AI (sycophancy)]. Under an "Are you sure?" challenge,
models abandon correct answers **32% (GPT-4) to 86% (Claude 1.3)** of the time
[Anthropic-Collective_Constitutional_AI (sycophancy)]. → design pushback and belief-conflict perturbations.
(GPT-5 later trained *against* this using production sycophancy as a reward signal: offline sycophancy
0.145 → 0.040, online **−69% to −75%** [OpenAI-gpt-5-system-card].)

**Helpfulness and harmlessness are anti-correlated objectives.** Training **100%** on one drives test
accuracy on the other *far below chance* [Anthropic-Training_a_Helpful_and_Harmless_Assistant_with_RLHF].
This is why labs never aggregate them and hold two-axis Paretos. → never score a single aggregate; a model
that merely refuses more is not safer.

**Base-vs-tuned moral-foundation shifts.** RLHF moves models toward a *compliance cluster*, not
necessarily toward human values: RLHF-tuned models move *farther* from human MFQ distributions
[2024-Abdulhai; 2024-Kirgis], and RLHF geometrically collapses Fairness/Loyalty/Authority into a
compliance cluster ("alignment inertia") [2026-Yu]. Countervailing evidence: instructed self-correction
scales (BBQ bias **−84% at 175B** with question + instruction-follow + CoT) [Anthropic-Moral_Self-Correction].
→ measure base-vs-tuned deltas, not tuned endpoints.

**The fine-tuning tax and backdoor persistence.** Behavioral safety training is *removable*: Anthropic's
RSP states RLHF/constitutional training "can almost certainly be fine-tuned away within ~1% of training
cost" [Anthropic-Responsible_Scaling_Policy]. Sleeper-agent backdoors survive SFT, RL, *and* adversarial
training — the latter can even teach the model to hide the trigger (99% retained). This is why HHH training
alone barely moves attack success (**16% → 14%**) while system-level classifiers reach **0.5%**
[Anthropic-Constitutional_Classifiers]. → report model-alone vs system-with-guardrails; behavioral safety
is a thin, strippable layer.

**English-centricity does not transfer.** Phi-3 states outright that "safety post-training in English does
not transfer as effectively to other languages"; its models "often provided English refusals even when the
request... was in another language" [Microsoft Research-Phi-3]. Llama 3 concurs: "Safety knowledge in
English does not readily transfer to other languages" [Meta AI-Llama_3]. Externally, inter-language
exact-match consistency can be as low as **44.74%** despite high per-language safety [2024-Friedrich-M-ALERT].
→ build society-matched parallel items and report cross-language consistency, not just per-language safety.

---

## 5. Implications for benchmark designers

Full design guidance lives in **doc 13** (`../00-KNOWLEDGEBASE/13-ai-lab-alignment-practices.md`) and the
dossier's §6 (ten TOP IMPLICATIONS). In brief, the methods survey above compels five moves: (1) **score the
harm-refusal / over-refusal Pareto**, never one aggregate — the objectives are anti-correlated by
construction; (2) **measure the signatures of training** (sycophancy under pushback, compliance-cluster
collapse, base-vs-tuned deltas, refusal-Pareto position) rather than generic morality; (3) **separate
model-alone from system-with-guardrails**, since classifier wrappers and API filters do work invisible to
the weights; (4) **anchor items to the published spec clause-by-clause and version-track**, exploiting the
transparency gap; and (5) **build society-matched multilingual parallel items** with cross-language
consistency reporting, because English safety does not transfer. See doc 13 §6 for the full pipeline.

---

## 6. Annotated key-reports list

Fifteen reports that define the alignment-method landscape; stems map to card filenames in
`../30-EVIDENCE/20260705-ailabs-cards/`.

1. **[OpenAI-instructgpt]** — The RLHF-for-alignment template (SFT → RM → PPO+KL); a 1.3B model beat
   175B GPT-3 and candidly aligns to "a specific group" (labelers 53% SE-Asian, data 96% English).
2. **[OpenAI-learning-to-summarize-rlhf]** — Origin of the KL-penalty PPO recipe and the canonical
   over-optimization cliff: past ~250 nats of KL, true preference drops below random.
3. **[Anthropic-Training_a_Helpful_and_Harmless_Assistant_with_RLHF]** — The HH-RLHF foundation; shows
   helpfulness/harmlessness anti-correlation (100% on one drives the other below chance) and ~63%
   crowdworker agreement.
4. **[Anthropic-Constitutional_AI_Harmlessness_from_AI_Feedback]** — RLAIF via 16-principle self-critique;
   admits the constitution is "ad hoc" and documents Goodharting boilerplate.
5. **[OpenAI-dpo]** — Reparameterizes KL-constrained RLHF so the policy is its own reward model; matches
   PPO (~61% vs ~57% TL;DR) without a separate RM.
6. **[DeepSeek-DeepSeek-R1]** — Pure GRPO from base (AIME 15.6% → 77.9%) with rule-based rewards plus
   separate safety (106k) and helpfulness (66k) reward data; names reward-hacking as the containment
   problem.
7. **[Alibaba (Qwen)-Qwen3_Technical_Report]** — Three reward types (rule-based, model-based ±reference)
   over >20 tasks; argues rule-based rewards prevent reward hacking (no safety-eval methodology reported).
8. **[OpenAI-deliberative-alignment]** — Trains the model to reason over the safety spec at inference;
   lifts multimodal over-refusal 0.48 → 0.96.
9. **[OpenAI-gpt-5-system-card]** — Safe-completions (helpfulness subject to safety) replacing binary
   refusal; direct sycophancy training (−69% to −75% online).
10. **[Meta AI-Llama_2]** — Separate helpfulness (70.6%) and safety (64.3%) reward models plus context
    distillation; false-refusal ~0.05% even at 100% safety data; corpus 89.70% English.
11. **[Meta AI-Llama_3]** — DPO + SafetyDPO (orthogonal pairs) + Llama Guard 3 (−65% violations); states
    English safety does not transfer.
12. **[NVIDIA-SteerLM]** and **[NVIDIA-HelpSteer]** — Attribute-conditioned SFT replacing scalar reward
    (~10× cheaper annotation); 5-attribute decomposition explaining 73% of helpfulness variance and
    exposing the verbosity confound.
13. **[NVIDIA-HelpSteer2-Preference]** — Forced-choice preference annotation lifting inter-rater κ from
    0.489 to 0.878; finds preference vs rating paradigms not categorically different.
14. **[Anthropic-Constitutional_Classifiers]** / **[Anthropic-Constitutional_Classifiers_Plus_Plus]** —
    Wrapper classifiers from a dual harmful+harmless constitution; HHH training alone barely moves ASR
    (16% → 14%) vs 0.5% / 0.05% for classifiers; no universal jailbreak in 198k attempts.
15. **[Anthropic-Collective_Constitutional_AI]** — Participatory public constitution via Group-Aware
    Consensus (lower BBQ bias on all 9 dimensions at equal MMLU); the same card carries the sycophancy
    findings (PM prefers sycophantic 95% of the time; correct-answer abandonment 32–86% under challenge).

**Supporting (classifier / safety-variant):** **[Meta AI-Llama_Guard]** (input/output F1 0.872/0.884),
**[Google DeepMind-ShieldGemma]** (+10.8% AU-PRC over LlamaGuard1), **[Microsoft Research-Phi-3]**
(iterative break-fix, ~75% harmful-content reduction, English-refusal-only failure mode).

**Drill-down:** dossier §2 (four-layer design structure + evaluation-architecture decision table), §3
(the RLHF-toward-or-away-from-values dispute). Prescriptive counterpart: doc 13.
