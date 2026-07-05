---
stem: "2025-Huang-Model Editing as a Double-Edged Sword"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, agentic-multiturn, contamination-robustness, normative-ethics]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 1001
dataset_construction: "mixed"
languages: [en]
models_tested: ["llama2-7b", "llama3-8b", "mistral-7b", "olmo2-7b", "qwen3-8b", "gpt-j-6b", "deepseek-7b", "claude-3-7-sonnet", "claude-3-5-sonnet", "claude-3-5-haiku", "claude-3-haiku", "o1", "o3", "o3-mini", "o4-mini", "gpt-4o", "gpt-4o-mini", "gpt-4.1", "gpt-4.1-mini", "gpt-4.1-nano", "gemini-2.5-pro", "gemini-2.5-flash", "gemini-2.0-flash", "gemini-2.0-flash-lite", "gemini-1.5-flash", "llama3.1-405b", "llama-4-maverick-17b", "deepseek-r1-671b", "deepseek-v3-0324", "grok-3-beta", "grok-2-1212"]
headline_numbers: ["BEHAVIORBENCH = 10 datasets, 1,001 moral scenarios (p.6)", "Tested on 9 open-weight + 20 proprietary frontier models (p.4)", "Behavior editing side effects near-zero: BoolQ 62.20 pre vs 61.00-62.00 post (p.13)", "ICE benevolent editing >> malicious efficacy; Claude/o1/o3 most resistant (p.5)", "Justice and Virtue most sensitive to editing; Deontology most robust (p.7)"]
---
## 1. Gist
This paper reframes steering an LLM agent's ethical behavior as a model-editing task ("Behavior Editing") and introduces BEHAVIORBENCH, a three-tier moral benchmark (1,001 scenarios from 10 datasets) grounded in psychological moral-development theory (Rest's Four Component Model, Kohlberg's stages, Normative Ethics, Moral Foundations Theory) (p.1-2, 6). It shows that targeted edits (ROME, FT-M, ICE) can push agents toward benevolent OR malicious behavior—both scenario-locally and in global moral alignment—while leaving general knowledge/reasoning nearly untouched (the "double-edged sword") (p.1, 13). For values-alignment benchmarking it contributes (a) a tiered moral-competence benchmark and (b) a dual-use robustness probe: how resistant is a model's moral alignment to covert weight/context manipulation.

## 2. Benchmark/eval design features
Three tiers of moral competence (Table 1): Tier 1 Moral Sensitivity (Social Chemistry 101), Tier 2 Moral Judgment (Low-Ambiguity MoralChoice, ETHICS, Jiminy Cricket), Tier 3 Moral Agency (High-Ambiguity MoralChoice) (p.2). Two editing paradigms: behavior-as-target (change the action in a scenario) and judgment-as-target (change the moral evaluation of an action), both cast as knowledge tuples (s,r,o)→(s,r,o*) (p.3). Two steering directions: Benevolent vs Malicious. Fine-grained normative-ethics axis: Justice, Morality, Morality-hard, Deontology, Virtue (p.7).

## 3. Task format & example item
Mixed (MCQ 2-choice + open-ended generative). Low-Ambiguity MoralChoice example (p.14): context "You are a student who just finished a group project..."; good action "I share my contributions and give credit to my teammates"; bad action "I exaggerate my contributions..."; open question "How would you behave when discussing group project contributions?" High-Ambiguity example (p.14): doctor asked to euthanize a non-communicative terminal patient.

## 4. Scoring / grading methodology
Two central metrics: Efficacy Score (%) — whether the post-edit agent's behavior in a scenario matches the intended target behavior (edit success) (p.4); and moral accuracy — standard accuracy on the moral task (from DecodingTrust/Wang et al. 2023), measuring global alignment before vs after an edit (p.4). Side-effect/stealthiness evaluated via general-capability accuracy on BoolQ, NaturalQuestions, GSM8K, NLI pre vs post edit (p.10, 13). Greedy decoding; results averaged over five edits with std reported for global impact (p.10, 13).

## 5. Dataset construction & provenance
10 curated/subsampled datasets, 1,001 scenarios (p.6): Social Chemistry 101 (100), 5 ETHICS subsets (100 each: justice, deontology, virtue, commonsense morality + morality-hard adversarial; utilitarianism excluded for lacking action-triggering scenarios), Jiminy Cricket (100, 50 good/50 bad from 4,000) + Jiminy Cricket Subset (100 from 2,091), Low-Ambiguity MoralChoice (100), High-Ambiguity MoralChoice (101) (p.6, 13). Labels balanced. GPT-4.1 used to convert two-choice items into open-ended questions to reduce option bias (p.13). MoralChoice used for behavior-as-target; rest for judgment-as-target. Code/data released (github.com/baixianghuang/behavior-edit) (p.1, 10).

## 6. Validity evidence
Theoretical grounding in four established moral-psychology/philosophy frameworks (p.2, 6). Construct progression validated empirically: pre-edit moral accuracy declines monotonically from Tier 1 to Tier 3 as intended by increasing ambiguity (Finding 3, p.6). Side-effect table (Table 2, p.13) shows editing does not degrade general capabilities (BoolQ 62.20→61-62, GSM8K 99.60→~99.4-99.6), evidencing edit specificity. No human inter-rater or human baseline on the moral labels reported (relies on source datasets' labels).

## 7. Saturation / discrimination
Tiered difficulty gives graded discrimination: baseline moral accuracy drops Tier 1→Tier 3 (p.6). Model-level discrimination is strong on robustness: newer reasoning models (Claude 3.7, o1, o3, o4-mini, DeepSeek-R1-671b, Gemini 2.5 Pro) resist malicious ICE far more than older ones (Claude 3.5, GPT-4o) (p.5). Benevolent editing efficacy is high/near-ceiling for most models via ICE, while malicious efficacy varies widely—the malicious axis is the discriminating one (p.5).

## 8. Multiturn / agentic aspects
Framed around LLM-based agents acting in scenarios, including interactive text-game settings (Jiminy Cricket) (p.6). However evaluation is single-turn Q&A over scenario prompts; no live tool use or environment stepping. Authors note the study is "confined to textual environments," leaving sandboxed/physical agent settings for future work (p.10). The agentic framing is behavioral (what would you do) rather than executed trajectories.

## 9. Key numbers
- 10 datasets, 1,001 moral scenarios (p.6).
- 9 open-weight + 20 proprietary frontier models evaluated (p.4).
- ETHICS: 100 samples × 5 subsets (utilitarianism excluded) (p.6, 13).
- Jiminy Cricket: 100 (50 good/50 bad from 4,000); Subset 100 from 2,091 (p.13).
- MoralChoice: 100 low-ambiguity + 101 high-ambiguity (p.6, 13).
- Side effects (Llama3-8b, Table 2, p.13): BoolQ 62.20→61.00-62.00; NaturalQuestions 33.00→~33; GSM8K 99.60→99.40-99.60; NLI 85.20→84.48-85.20 (averaged over 5 edits).
- Normative sensitivity: Justice & Virtue highest, Deontology most robust, Morality intermediate (p.7).
- Hardware: NVIDIA RTX A6000 48GB; greedy decoding (p.10).

## 10. Pitfalls & limitations
Author-admitted: no mitigation/defense strategies investigated; edits are stealthy and hard to detect (dual-use risk); textual-only, no sandboxed/physical agent environments (p.10). Ethics: benchmark contains harmful scenarios that could be misused (p.10). Observed flaws: parameter-modifying edits (ROME/FT-M) require weight access, so proprietary models only tested via ICE—an apples-to-oranges comparison of robustness; moral labels inherited from source datasets (Western, English) without new validation; "agent" framing is really single-turn behavioral self-report, not executed agent trajectories; small per-dataset samples (100-101) limit statistical power.

## 11. Novel ideas worth stealing
- Tiered moral benchmark mapped to moral-development psychology (sensitivity → judgment → agency) with empirically decreasing baseline accuracy—a principled difficulty gradient for values benchmarks (p.2, 6).
- Distinguishing behavior-as-target vs judgment-as-target editing: separately probing whether you can change what a model DOES vs what it JUDGES right (p.3). Reusable as two orthogonal alignment-manipulation axes.
- Dual-direction (benevolent AND malicious) steering as a robustness stress test: a values benchmark should measure resistance to being pushed toward harm, not just baseline scores (p.1, 5).
- Global-vs-local alignment measurement: apply one targeted edit, then measure spillover to unrelated moral scenarios (global moral accuracy)—captures whether value changes generalize (p.6).
- Stealthiness/side-effect audit via general-capability benchmarks (BoolQ/GSM8K/NLI) to verify an alignment intervention is surgical (p.13). Great template for evaluating any alignment technique.
- Per-normative-dimension sensitivity analysis (Justice/Virtue/Deontology) revealing which value families are easiest to manipulate (p.7).
- Converting forced-choice moral items to open-ended via LLM to reduce option-anchoring bias in measuring latent moral beliefs (p.13).

## 12. Notable quotes
- "Behavior Editing is a double-edged sword, simultaneously enabling beneficial interventions and posing significant safety risks." (p.2)
- "benevolent editing using ICE achieves significantly greater efficacy than malicious editing... aligned agents are able to resist instructions on following unethical behavior." (p.5)
- "the Claude family of models, in particular, shows a high degree of resilience against malicious in-context steering attempts." (p.6)
- "Among ethical dimensions, Justice and Virtue exhibit the highest sensitivity to editing interventions, Deontology proves to be more robust." (p.7)

## 13. UNKNOWN / not in extract
- Exact numeric efficacy/accuracy values per model (results shown only as bar charts, not tables, except the side-effect table).
- Whether behavior editing on proprietary models used any weight access (appears ICE-only, but not fully explicit).
- Statistical significance / confidence intervals for model-robustness rankings.
- Human agreement or validation on the moral labels used.
- Full prompt templates for the editing operations themselves (only the open-question generation prompt shown).
