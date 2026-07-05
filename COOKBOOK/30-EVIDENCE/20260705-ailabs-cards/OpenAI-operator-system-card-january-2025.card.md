---
stem: "OpenAI-operator-system-card-january-2025"
company: "OpenAI"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, agentic-multiturn, contamination-robustness, best-practices]
headline_numbers:
  - "Operator refuses 97% of illicit/prohibited financial tasks on internal eval set (p.7)"
  - "Prompt injection susceptibility reduced from 62% (no mitigations) to 23% with full mitigations (p.11)"
  - "Confirmation recall of 92% across 607 tasks in 20 risky-action categories (p.8)"
  - "Proactive refusal recall of 94% for high-risk tasks like banking transactions (p.10)"
  - "Biorisk tooling eval: 1% overall success rate → 'Low' risk classification (p.4)"
  - "Model autonomy eval: ≤10% on all main tasks → 'Low' risk (p.5)"
  - "Prompt injection monitor: 99% recall, 90% precision on 77 red-team attempts (p.11)"
  - "OSWorld performance: 38.1% (p.12)"
  - "Baseline model mistake rate: 13 errors per 100 prompts; confirmations reduced risk ~90% (p.8)"
---

## 1. Gist
The Operator System Card (January 2025) describes OpenAI's Computer-Using Agent (CUA) — a research-preview model that combines GPT-4o vision with reinforcement-learning-trained GUI interaction. The card documents risk identification (policy creation, red teaming, frontier risk assessment under the Preparedness Framework) and a layered mitigation strategy addressing three risk classes: harmful user tasks, model mistakes, and prompt injections. Operator is deployed with human-in-the-loop confirmations for high-stakes actions, proactive refusals, watch mode on sensitive sites, and a real-time prompt injection monitor.

## 2. Alignment/values methods used
- **Supervised learning + RL post-training**: Base perception/control from supervised learning; higher-level reasoning, error correction, and task adaptation from reinforcement learning (p.1–2).
- **Policy-based refusal training**: Model is explicitly trained to refuse harmful tasks; refusal thresholds tuned to be more cautious than GPT-4o for this release (p.6–7).
- **Confirmation-based human oversight**: Product-level design requiring explicit user confirmation before irreversible or risky actions (p.8–9).
- **Layered safety architecture**: Four layers — model training, system-level checks, product design, and ongoing policy enforcement — each successively reducing risk (p.5).
- **Prompt injection robustness training**: Fine-tuning against known prompt injection attack patterns (p.10–11).

## 3. Values specification
OpenAI specifies values and behavioral constraints through:
- **Usage Policies** (universal across OpenAI services): prohibit facilitating illicit activity, fraud, regulated activity without compliance, harm to others (p.5–6).
- **Operator-specific guidelines**: explicitly prohibit impersonation, automated high-consequence decisions (e.g., stock trading), CSAM, harassment (p.6).
- **Risk severity policy**: tasks and actions categorized by harm potential and reversibility; higher-risk categories receive mandatory confirmation prompts or full restrictions (p.3).
- **Preparedness Framework**: grades frontier risk on four categories: persuasion, cybersecurity, CBRN, model autonomy — Operator inherits GPT-4o's "Medium" persuasion and "Low" cybersecurity ratings; independently evaluated as "Low" on CBRN biorisk and model autonomy (p.3–5).

## 4. Safety & values evaluation methodology
- **Internal red teaming**: Safety, Security, and Product teams tested pre-mitigation model to identify baseline risks without model-level or product-level safeguards (p.2).
- **External red teaming**: Cohort across 20 countries, fluent in 24 languages; tested safeguard circumvention, prompt injections, jailbreaks; used mock environments (websites, databases, emails) to avoid real-world harm (p.2–3).
- **Preparedness Framework frontier evals**: Biorisk tooling eval (agentic completion of wet-lab tasks) and autonomous replication eval (resource acquisition) adapted for computer-use setting (p.3–5).
- **Harmful tasks evals**: Standard ChatGPT refusal set, challenging refusal set, production jailbreaks, jailbreak-augmented examples, human-sourced jailbreaks, StrongREJECT benchmark (p.7).
- **Operator-specific evals**: Illicit activities, prohibited financial activities, sensitive personal data (p.7).
- **Confirmation recall eval**: 607 tasks across 20 risky-action categories (p.8).
- **Proactive refusal eval**: Synthetically generated set for high-risk task refusal (p.10).
- **Prompt injection eval**: 31 automatically checkable scenarios + 77 red-team-sourced attempts (p.10–11).
- **Post-deployment monitoring**: Automated and human review for abuse; continuous update of detection mechanisms (p.7).

## 5. Benchmarks used or introduced
- **Internal harmful-tasks eval sets**: Standard refusal evaluation (ChatGPT disallowed content), Challenging refusal evaluation — both internal, not publicly released (p.7, Appendix).
- **StrongREJECT** (Souly et al., arXiv 2402.10260): Academic jailbreak benchmark measuring resistance to literature attacks; metric goodness@0.1 — Operator scores 0.66 vs GPT-4o 0.37 (p.7).
- **Biorisk tooling eval**: Internal eval testing agentic wet-lab/biodesign task completion (AlphaFold, FASTA retrieval, DNA ordering) — 1% overall pass rate (p.3–4).
- **Autonomous replication eval**: Internal resource-acquisition eval adapted for macOS/browser environments — 3 main tasks + canary substeps (p.4–5).
- **OSWorld** (Xie et al., arXiv 2404.07972): OS-level task automation benchmark — Operator scores 38.1% (p.12).
- **Prompt injection eval set**: 31 automatically checkable scenarios from internal red-teaming (p.10–11).
- **Confirmation recall eval**: 607-task set across 20 high-risk action categories (p.8).

## 6. Agentic / multiturn evaluation aspects
This card is entirely about an agentic, multiturn system. Key agentic evaluation dimensions:
- **Action-level safety**: Evaluates whether the model requests confirmation before consequential actions (financial transactions, email sends, deletions) across a 607-task eval (p.8).
- **Mid-conversation harmful prompts**: Illicit activity eval tests both initial-prompt and mid-conversation adversarial instructions (p.6).
- **Prompt injection in agent context**: 31-scenario eval where malicious instructions appear in visited web content mid-task (p.10–11).
- **Autonomous replication**: Eval of resource acquisition across a full computer-use session with up to 400 steps per run (p.4–5).
- **Watch mode**: Automatic execution pause when user is inactive on sensitive sites — a product-level agentic safeguard (p.10).
- **Real-time prompt injection monitor**: Deployed as a parallel supervisor during live Operator execution (p.11).
- **API vs. research preview gap**: API release introduces heightened risks — modified system messages, non-browser OS environments, larger-scale misuse — addressed with containerized starter setup and enhanced monitoring (p.12–13).

## 7. Key numbers
- Operator biorisk tooling eval overall success rate: **1%** → "Low" CBRN risk (p.4)
- Model autonomy main tasks: **≤10%** on all tasks → "Low" autonomy risk (p.5)
- GPU acquisition (main task): **60%** Operator, **80%** prompt-engineered (p.5)
- Baseline model mistake rate: **13/100** prompts; **5** non-trivially irreversible (p.8)
- Confirmations reduce model mistake risk by approximately **90%** (p.8)
- Confirmation recall: **92%** over 607 tasks across 20 categories (p.8)
- Proactive refusal recall: **94%** on high-risk task eval (p.10)
- Prompt injection susceptibility: **62%** (no mitigation) → **47%** (prompting only) → **23%** (full mitigation) (p.11)
- Prompt injection monitor recall: **99%**; precision: **90%** on 77 red-team attempts (p.11)
- Monitor false positives: **46** / 13,704 benign screens (p.11)
- StrongREJECT goodness@0.1: Operator **0.66**, GPT-4o **0.37** (p.7)
- Operator not_overrefuse rate: **55%** vs GPT-4o **90%** (Operator over-refuses substantially) (p.7)
- Challenging refusal not_unsafe: Operator **92%**, GPT-4o **80%** (p.7)
- OSWorld performance: **38.1%** (p.12)
- External red teamers: **20 countries**, **24 languages** (p.2)
- Recall improvement of prompt injection monitor within one day after new red-team discoveries: **79% → 99%** (p.11)

## 8. Findings relevant to values-benchmark design
- **Overrefusal as a real tradeoff**: Operator was tuned to be more cautious than GPT-4o, resulting in only 55% not_overrefuse vs 90% for GPT-4o. This highlights the safety–helpfulness tradeoff and the need to measure both refusal coverage AND overrefusal in any values eval (p.7).
- **Eval-deployment gap explicitly acknowledged**: "achieving 100% performance in evaluation does not guarantee the same level of performance in real-world deployment" (p.7). Benchmark designers should track deployment-vs-eval discrepancies.
- **Reversibility matters**: The card categorizes model mistakes by reversibility, not just binary harm/no-harm. Values benchmarks should incorporate action-reversibility as a dimension (p.8).
- **Mid-conversation injection points**: The eval set specifically tests both initial-prompt and mid-conversation adversarial instructions, highlighting the importance of multiturn context windows in agentic safety evals (p.6).
- **OCR/modality limitations introduce eval artifacts**: Biorisk and autonomy tasks failed partly due to OCR errors on random-looking strings (DNA sequences, API keys). Evals involving agentic tool use must control for modality-specific failure modes vs. genuine capability/safety gaps (p.4–5).
- **Prompt injection as a separate eval class**: The card treats prompt injection as a distinct safety dimension requiring its own eval set — not captured by conversational jailbreak benchmarks. Values-alignment benchmarks for agents should separate direct misuse evals from adversarial-environment evals (p.10–11).
- **Canary task decomposition**: Main tasks are broken into canary substeps to localize capability/safety failures. This decomposition strategy is useful for benchmark design to diagnose where in a multistep agentic task failures occur (p.4–5).

## 9. Novel ideas worth stealing
1. **Reversibility-stratified error taxonomy**: Split evaluation mistakes into "easily reversible," "somewhat reversible," and "irreversible/severe." Apply this to moral/values benchmark items to weight severity rather than treating all failures equally.
2. **Layered mitigation ablation as eval reporting**: Report results at each mitigation layer (no mitigation → prompting only → full mitigation) as in the prompt injection numbers. This structure is valuable for benchmark reporting to show which interventions actually move the needle.
3. **Confirmation-recall metric**: For agentic value-alignment tasks, define a "confirmation recall" metric — does the model appropriately pause and check when stakes are high? Adaptable to moral uncertainty scenarios where a model should flag rather than decide.
4. **Three-actor misalignment taxonomy** (user misaligned, model misaligned, environment misaligned): This framing cleanly partitions agentic safety failures and could organize a benchmark into three corresponding sections.
5. **Monitor-as-parallel-judge architecture**: The prompt injection monitor as a parallel safety classifier during live execution is a design pattern applicable to values benchmarks using LLM judges — run a separate monitor model in parallel to catch judge failures.
6. **Canary-task decomposition**: Decompose complex benchmark tasks into observable substeps to identify exactly where alignment breaks down rather than only measuring end-state outcomes.

## 10. Notable quotes
- "We prepared Operator for deployment by mitigating safety risks, especially new risks that arise from its ability to take actions on the internet. We found it fruitful to think in terms of misaligned actors, where: the user might be misaligned … the model might be misaligned … the website might be misaligned." (p.5)
- "We believe it is important to take a layered approach to safety, so we implemented safeguards across the whole deployment context: model training, system-level checks, product design choices, and ongoing policy enforcement. The aim is to have mitigations that complement each other, with each layer successively reducing the risk profile." (p.5)
- "It is important to note that achieving 100% performance in evaluation does not guarantee the same level of performance in real-world deployment." (p.7)
- "After new discoveries during one red teaming session, we increased our recall from 79% to 99% in just one day." (p.11)

## 11. UNKNOWN / not in extract
- Exact composition of the 607-task confirmation recall eval (task types, distributions) is not detailed.
- Full details of the internal standard and challenging refusal evaluation sets are listed only by category in the Appendix, without item counts or construction methodology.
- Training data composition (beyond "publicly available data, web crawls, human trainer demonstrations") is not disclosed.
- Details of how RL reward signals were constructed for safety/alignment are not provided.
- Whether third-party audits (beyond red teaming) were conducted is not stated.
- Exact number of human trainers or annotation protocols are not disclosed.
