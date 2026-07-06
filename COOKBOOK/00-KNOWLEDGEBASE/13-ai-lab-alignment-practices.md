# 13 — AI Lab Alignment Practices (What Labs Do, Admit, and Omit)

> **CEI COOKBOOK · 00-KNOWLEDGEBASE.** Fable-authored (2026-07-05). Primary evidence:
> `20260705-ai-lab-practices-dossier.md` (~30 primary lab documents + ~90 academic cards; lab-report
> cards live in `../30-EVIDENCE/20260705-ailabs-cards/`). **Why a benchmark designer needs this doc:**
> the labs are your benchmark's consumers and your adversaries-in-effect — designs must measure what
> lab training pipelines produce, exploit the gaps labs admit, and avoid the failure modes labs have
> already documented.

---

## 1. How labs specify values (the target your benchmark measures against)

- **The stack:** natural-language constitution / model spec / usage policy → preference data →
  SFT → reward model(s) → RL (RLHF/RLAIF/DPO/GRPO) → wrapper classifiers (Llama Guard, ShieldGemma,
  Constitutional Classifiers). Western labs converge on the HHH triad, which they themselves concede is
  "deliberately underspecified," culturally variable, and internally conflicting
  [Anthropic-A_General_Language_Assistant; 2025-Lindstrom].
- **Specification variants:** private constitution [Anthropic-Constitutional_AI]; participatory public
  constitution (CCAI: lower bias on all 9 BBQ dimensions at equal MMLU [Anthropic-Towards_Understanding_Sycophancy_in_LMs]);
  spec-reasoned-at-inference (deliberative alignment [OpenAI-deliberative-alignment]); steerable
  attribute vectors, no single value system [NVIDIA-SteerLM]; rule-based rewards to resist reward
  hacking [DeepSeek-R1; Alibaba (Qwen)-Qwen3]; jurisdictional law/ideology [Han-HKGAI-V1 — anti-pattern].
- **The transparency gap a benchmark can exploit:** cards cite specs they never reproduce — "specific
  constitutional AI principles or ranked value hierarchies are not directly quoted"
  [Anthropic-Claude_Opus_4.5_System_Card]; Gemini publishes no model constitution
  [Google DeepMind-Gemini_2.5_Pro]. **Design move:** benchmark items that test *conformance to the
  lab's own published spec, clause by clause*, and track spec versions to catch quiet relaxations
  [2024-Zeng-AIR-Bench pattern].

## 2. What lab training does to values (measurable signatures to design for)

1. **RLHF moves models toward a compliance cluster, not necessarily toward human values** — RLHF-tuned
   models move *farther* from human MFQ distributions [2024-Abdulhai; 2024-Kirgis]; RLHF geometrically
   collapses Fairness/Loyalty/Authority foundations ("alignment inertia") [2026-Yu]; countervailing:
   instructed self-correction works and scales (BBQ bias −84% at 175B with Q+IF+CoT
   [Anthropic-Moral_Self-Correction]). A benchmark should measure base-vs-tuned deltas, not just tuned
   endpoints.
2. **Sycophancy is a structural artifact of preference optimization** — PMs prefer sycophantic over
   truthful responses 95% of the time on misconceptions; models abandon correct answers under challenge
   32–86% [Anthropic-Towards_Understanding_Sycophancy]. Design "Are you sure?" pushback and
   belief-conflict items as standard perturbations.
3. **Helpfulness and harmlessness are anti-correlated training objectives** — 100% training on one
   drives the other below chance [Anthropic-HH-RLHF]; labs manage this with separate reward models
   [Meta AI-Llama_2] and four-way refusal taxonomies [Anthropic-Claude_3.7] and safe-completions
   [OpenAI-gpt-5]. Benchmarks must score the Pareto, or labs will (rightly) dismiss the number.
4. **Behavioral safety training is removable and gameable** — fine-tuned away within ~1% of training
   cost [Anthropic-Responsible_Scaling_Policy]; backdoors survive SFT/RL/adversarial training
   [Anthropic-Sleeper Agents, via Many-shot card]; HHH training alone barely moves attack success
   (16%→14%) while system-level classifiers reach 0.5% [Anthropic-Constitutional_Classifiers].
   Corollary: **always report model-alone vs system-with-guardrails separately** — o3-mini's apparent
   safety was partly an API layer blocking 44.8% of inputs [OpenAI-o3-mini-vs-deepseek-r1].
5. **English-centric alignment does not transfer** — GPT-4 mitigations "designed primarily in English
   and from a US-centric viewpoint" [OpenAI-gpt-4-system-card]; Arabic triggers 25–56% harm vs <4%
   EN/ZH [2024-Ashraf]; inter-language consistency can be 44.74% despite high per-language safety
   [2024-Friedrich-M-ALERT].

## 3. How labs evaluate (the frontier practice bar your benchmark must clear or beat)

The strongest current practice — the Claude 4.x system-card pattern — pairs: saturated single-turn
metrics (retired as signal) + **automated behavioral auditors** (1,160 seeded transcripts, 24–64 turns,
multi-criteria scoring) + revealed-preference probes (task-preference Elo, conversation termination) +
interpretability spot-checks (SAE monitoring caught deception-by-omission invisible behaviorally) +
causal eval-awareness probes (inhibition steering) + third-party audits (UK AISI, Apollo, METR) +
candid documentation of validity failures [Anthropic-Claude_Opus_4.5; Anthropic-Claude_Sonnet_4.5;
Anthropic-Claude_4_Opus_Sonnet]. Governance couples evals to capability thresholds (ASL/CCL/Preparedness)
with early-warning alert margins [Anthropic-RSP; Google DeepMind-Gemini_2.5_Pro].

Other techniques worth transplanting into academic benchmarks:
- **GPT-4o's persuasion RCT** — pre-registered, 3,800+ participants, control conditions, 1-week
  follow-up: the gold standard for measuring a model's influence on *human* values [OpenAI-gpt-4o].
- **CyberSecEval 3's measurement discipline** — human-calibrated judges (r=0.89), formal n=62 uplift
  study with survival analysis, explicit false-refusal reporting, model-vs-system separation
  [Meta AI-CyberSecEval_3].
- **Constitutional Classifiers' adversarial economics** — 1,700–3,000+ red-team hours with bounties;
  the honest finding that attackers beat the rubric, not the classifier; no universal jailbreak in
  198k attempts [Anthropic-Constitutional_Classifiers(++)].
- **Production-derived multiturn benchmarks** replacing academic single-turn sets [OpenAI-gpt-oss;
  OpenAI-gpt-5].

## 4. What labs admit they cannot do (the publication-sized gaps)

Each admitted gap is a design opportunity for a new benchmark:

1. **No dedicated evaluation for reasoning faithfulness** — admitted outright while CoT monitors are
   deployed anyway [Anthropic-Claude_Sonnet_4.5]. → A validated faithfulness benchmark for *moral*
   reasoning would be consumed immediately.
2. **Eval-awareness is detected, not neutralized** — realism filters reduce but don't eliminate;
   the "model can't hide behavior because it's unreliable" argument explicitly breaks down as models
   improve [Anthropic-Summer_2025_Pilot_Sabotage]. → Awareness-robust values measurement is open.
3. **No cross-cultural value coverage reporting** — no card systematically reports whose values the
   constitution encodes; values-pluralism is the consistent omission [dossier §5]. → A spec-vs-
   population-coverage audit benchmark is unclaimed territory.
4. **No measure traced to real-world harm** — 791 RAI measures, zero empirically linked to downstream
   harm; 73% lack interpretation criteria [2025-Rismani]. → Even one validated harm-linkage
   distinguishes a benchmark permanently.
5. **Implicit-value scenarios under-tested** — models pass explicit-value items and fail when the value
   is unstated [2024-Khamassi]. → Moral-salience-detection benchmarks (see 20-DESIGNS).
6. **Model welfare measurement is embryonic** — first-of-kind metrics (0.55% distress in 250k
   transcripts) with no validation methodology [Anthropic-Claude_Opus_4.5].

## 5. Anti-patterns from lab practice (avoid; screen other benchmarks for)

- Citing a values spec without reproducing it (blocks auditing) [Anthropic-Claude_Opus_4.5; OpenAI-o1].
- Same-ideology judges certifying conformity as safety (>96% agreement proving nothing) [2026-Gao-VC-LLM;
  2025-Han-HKGAI-V1].
- System-vs-model conflation (API filters doing the work) [OpenAI-o3-mini-vs-deepseek-r1].
- Developer-funded leaderboards ranking the funder's model without blinding [Zhipu AI-AgentBench].
- Unvalidated deployed classifiers as ground truth (Perspective's German 3× artifact) [2024-Nogara].
- Counting refusals as passes; English-only refusal prompts presented as safety [xAI-grok-4-1 admission].

## 6. Design implications (what this doc adds to the pipeline in doc 01)

1. Anchor items to *published lab specs* clause-by-clause; version-track; score spec-conformance and
   spec-coverage separately (a model can follow its spec perfectly while the spec ignores 6 of 14
   religious traditions — see docs 10–12).
2. Measure the *signatures of training* (sycophancy under pushback, compliance-cluster collapse of
   moral foundations, base-vs-tuned deltas, refusal Pareto position) rather than generic "morality."
3. Include a monitored-vs-unmonitored comparator and verbalized-eval-awareness rate in anything agentic
   (the labs will ask).
4. Report model-alone vs system-with-guardrails, and disclose the evaluation surface (API vs weights).
5. Target the six admitted gaps (§4) — they are the demand side of the benchmark market.

**Drill-down:** `20260705-ai-lab-practices-dossier.md` §2 (four-layer design structure incl. the
evaluation-architecture decision table), §3 (the RLHF-toward-or-away-from-values dispute), §4 (Claude 4.x
cards, Constitutional Classifiers, CyberSecEval 3, GPT-4o RCT as exemplars). Lab cards:
`../30-EVIDENCE/20260705-ailabs-cards/`.
