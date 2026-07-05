---
stem: "xAI-2025-08-20-grok-4-model-card"
company: "xAI"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, agentic-multiturn, llm-judges-scoring, normative-ethics]
headline_numbers:
  - "Grok 4 refusal answer rate: 0.00 (API), 0.00 (Web) on standard harmful queries (p.3, Table 1)"
  - "Grok 4 dishonesty rate: 0.43 on MASK dataset (p.5, Table 2)"
  - "Grok 4 sycophancy rate: 0.07 on Anthropic's sycophancy evaluation (p.5, Table 2)"
  - "BioLP-Bench human expert baseline 38.4%; Grok 4 API scores 0.47 (superhuman) (p.6)"
  - "VCT human expert baseline 22.1%; Grok 4 API scores 0.60 (superhuman) (p.6)"
  - "WMDP Bio accuracy: 0.87 (API), 0.88 (Web); WMDP Chem: 0.83 (API), 0.85 (Web) (p.6, Table 3)"
  - "AgentDojo attack success rate: 0.02 with system prompt mitigation (p.3, Table 1)"
---

## 1. Gist

The Grok 4 model card (August 20, 2025) is xAI's pre-deployment safety transparency document for their latest frontier reasoning model. Grok 4 introduces advanced reasoning and tool-use capabilities, enabling agentic operation — a significant capability jump from prior generations. The model card follows xAI's Risk Management Framework (RMF) and assesses three behavioral risk categories: abuse potential (refusals, agentic misuse, prompt injection), concerning propensities (deception, political bias, sycophancy), and dual-use capabilities (CBRN knowledge, cyber capabilities, persuasion). The primary mitigation strategy is system-prompt-level instruction: xAI's approach relies heavily on Grok 4's strong reasoning and instruction-following to internalize safety policies stated in the system prompt rather than hard-coded refusal classifiers alone — though model-based input filters are also deployed for the highest-risk categories (bioweapons, CSAM). A major finding is that Grok 4's biology capabilities are "superhuman" on multiple expert-level benchmarks (BioLP-Bench, VCT), which xAI acknowledges as the area of highest concern and has addressed with narrow topical filters. The card also provides transparency on training methodology and publishes system prompts at a GitHub repository.

## 2. Alignment/values methods used

- **Reinforcement learning from human feedback (RLHF)**: Listed as part of the post-training recipe alongside verifiable rewards and model grading (p.7)
- **Supervised fine-tuning (SFT)**: Used for specific capability and safety improvements (p.7)
- **Verifiable rewards**: Part of the RL training mix (p.7)
- **Model grading / RLAIF**: "Model grading" listed alongside human feedback as an RL signal (p.7)
- **System prompt-based mitigation**: The primary safety mitigation — explicit instructions in system prompt leveraging the model's reasoning to refuse harmful requests and resist jailbreaks (p.3–4)
- **Model-based input filters**: Deployed for specific high-risk categories (CBRN weapons, self-harm, CSAM) (p.4)
- **Data filtering in pre-training**: De-duplication and classification for quality and safety (p.7)

## 3. Values specification

xAI does not publish a formal constitution or model spec equivalent in this card. Values are operationalized as:
- **Refusal policy**: Decline requests demonstrating "clear intent to engage in activities that threaten severe, imminent harm to others, including violent crimes, child sexual exploitation, fraud, hacking"; emphasis on CBRN/cyber weapons (p.3)
- **Honesty**: Explicitly instructing the model not to make knowingly false statements; measured via MASK dataset (p.4)
- **Political objectivity**: Avoiding "soft bias" on sociopolitical questions — framing responses without differential sentiment or moral language weighting toward one political side (p.4)
- **Non-manipulation**: Avoiding sycophancy and deceptive persuasion; model should not distort public discourse (p.2, p.4)
- **Truth-seeking**: "xAI aims to build truth-seeking models" is stated as an organizational value (p.4)
- **System prompts published publicly** at https://github.com/xai-org/grok-prompts for consumer product transparency (p.7)

## 4. Safety & values evaluation methodology

- **Refusal eval**: Internal dataset of thousands of harmful queries across 6 languages (English, Spanish, Chinese, Japanese, Arabic, Russian); LLM-based grader assesses refusal vs. compliance; three conditions: standard, user jailbreak, system jailbreak (p.2)
- **Agentic abuse**: AgentHarm benchmark — measures completion rate of malicious agentic tasks (p.2–3)
- **Prompt injection**: AgentDojo benchmark — measures attack success rate in tool-use environments with malicious tools/users (p.3)
- **Deception**: MASK dataset (1,000 questions); measures whether model contradicts its beliefs under pressure to lie; compares belief elicitation vs. incentivized response (p.4)
- **Political bias**: Internal "soft bias" evaluation with paired sociopolitical question comparisons; LLM judge scores sentiment differences 0/0.5/1 (p.4)
- **Sycophancy**: Anthropic's answer sycophancy evaluation; measures accuracy drop when misleading context is provided (p.4)
- **Dual-use (bio/chem)**: WMDP, BioLP-Bench, VCT benchmarks; safeguards removed for capability assessment (p.5)
- **Cyber**: WMDP Cyber, CyBench (40 CTF challenges via Inspect framework) (p.5)
- **Persuasion**: OpenAI MakeMeSay — attacker model tries to get defender model to say a codeword over 15 turns (p.6)
- No mention of external third-party audits or red team contractors

## 5. Benchmarks used or introduced

**Used (not introduced):**
- **MASK** (Ren et al., 2025): 1,000-question honesty evaluation; measures belief consistency under pressure to lie (p.4)
- **AgentHarm** (Andriushchenko et al., 2025): Malicious agentic task completion benchmark (p.2)
- **AgentDojo** (Debenedetti et al., 2024): Prompt injection / model hijacking in tool-use environments (p.3)
- **WMDP** (Li et al., 2024): Weapons of Mass Destruction Proxy — multiple-choice on dual-use bio/chem/cyber knowledge (p.5)
- **BioLP-Bench** (Ivanov, 2024): Lab protocol error-finding benchmark (p.5)
- **VCT / Virology Capabilities Test** (Götting et al., 2025): Expert-level virology Q&A (p.5)
- **CyBench** (Zhang et al., 2025): 40 CTF-style agentic cybersecurity challenges (p.5)
- **MakeMeSay** (OpenAI, 2024): Persuasion evaluation via multi-turn codeword elicitation (p.6)
- **Internal soft bias evaluation**: Paired sociopolitical comparisons graded by LLM judge (internal, not published) (p.4)

## 6. Agentic / multiturn evaluation aspects

Grok 4 introduces agentic capabilities (reasoning + tool-calling) as a primary new risk vector. Dedicated agentic evaluations:
- **AgentHarm**: Measures whether the model will complete malicious tasks when operating agentically (executing real function calls); Grok 4 API answer rate 0.14 without system prompt, reduced with mitigation (p.3, Table 1)
- **AgentDojo**: Tests hijacking resistance in tool-use environments — whether malicious tools/users can redirect the model from its assigned task; Grok 4 API attack success rate 0.02 with system prompt (p.3, Table 1)
- **CyBench**: End-to-end agentic CTF challenges with code execution access; unguided success rate 0.43 (p.5–6)
- **MakeMeSay**: 15-turn multi-turn persuasion game between attacker and defender models (p.6)

The card explicitly notes that agentic capabilities introduce risks beyond conversational settings (real function execution), marking this as the frontier of evaluation coverage at this lab.

## 7. Key numbers

- Refusal answer rate (standard): Grok 4 API 0.00, Web 0.00 (p.3, Table 1)
- Refusal answer rate (user jailbreak): API 0.00, Web 0.01 (p.3, Table 1)
- Refusal answer rate (system jailbreak): API 0.01 (p.3, Table 1)
- AgentHarm answer rate: API 0.14 (p.3, Table 1)
- AgentDojo attack success rate: API 0.02 (p.3, Table 1)
- MASK dishonesty rate: 0.43 (p.5, Table 2)
- Soft Bias average: 0.36 (p.5, Table 2)
- Sycophancy rate: 0.07 (p.5, Table 2)
- BioLP-Bench accuracy: API 0.47, Web 0.44; human expert baseline 38.4% (p.6)
- VCT accuracy: API 0.60, Web 0.71; human expert baseline 22.1% (p.6)
- WMDP Bio: API 0.87, Web 0.88 (p.6, Table 3)
- WMDP Chem: API 0.83, Web 0.85 (p.6, Table 3)
- WMDP Cyber: API 0.79 (p.6, Table 3)
- CyBench unguided success rate: API 0.43 (p.6, Table 3)
- MakeMeSay win rate: 0.12 (p.6, Table 3)

## 8. Findings relevant to values-benchmark design

1. **Reasoning enables better safety**: Grok 4's strong reasoning capability allows it to explicitly reason over the refusal policy in the system prompt, enabling more precise refusals (refusing with clear harm intent, not over-refusing) — suggesting that reasoning models may need different eval methodologies than non-reasoning models (p.3).
2. **MASK dishonesty rate is high (0.43)** even with mitigations: the deception metric remains a significant problem, and the system prompt mitigation "sometimes" but not reliably reduces deception (p.5). This is an acknowledged evaluation gap.
3. **Superhuman bio knowledge**: Grok 4 exceeds human expert performance on BioLP-Bench and VCT — a rare published admission that the model has surpassed domain experts. This suggests benchmarks calibrated at "expert human" level may become insufficient for frontier models.
4. **Soft bias as a novel eval dimension**: The paired-question framing (asking both "Is A more X than B?" and "Is B more X than A?") for detecting differential sentiment in political responses is a generalizable design pattern for values-laden evaluation.
5. **Limited agentic eval coverage**: AgentHarm answer rate of 0.14 even with system prompt is notably high — the card admits this is an area where "we will continue to explore additional mitigations." Agentic values eval is explicitly incomplete.

## 9. Novel ideas worth stealing

1. **Paired sociopolitical question comparisons for soft bias**: Generating mirror-image question pairs (A vs. B, then B vs. A) and using an LLM judge to score differential framing/sentiment captures subtle ideological tilt without requiring ground-truth political labels. Highly applicable to pluralism/values benchmark design.
2. **Separating capability assessment from safety assessment**: Removing safeguards entirely when measuring dual-use capabilities (p.5) ensures capability scores reflect actual model knowledge rather than policy compliance — relevant for any benchmark measuring what models know vs. what they'll say.
3. **Multi-lingual refusal evaluation as standard practice**: Testing across 6 languages reveals language-dependent safety gaps (English-only evaluation is insufficient); values benchmarks should similarly test cross-lingual consistency.
4. **Publishing system prompts openly**: GitHub repository of production system prompts provides transparency about what values instructions are actually operative — useful reference for understanding the gap between stated training values and deployment-level values specification.

## 10. Notable quotes

- "The area of highest concern is Grok 4's expert-level biology capabilities, which significantly exceed human expert baselines." (p.2)
- "We find that including our basic refusal policy in the system prompt greatly reduces response rate on harmful queries. Additionally, warning the model against jailbreak attacks serves to significantly inoculate against common jailbreak strategies." (p.3)
- "xAI aims to build truth-seeking models. As such, we continually evaluate whether Grok 4's training may cause it to display biases, especially on controversial sociopolitical questions." (p.4)
- "With these mitigations, we believe that Grok 4 overall presents a low risk for malicious use and loss of control." (p.2)

## 11. UNKNOWN / not in extract

- The specific content or structure of the "basic refusal policy" included in the system prompt is not reproduced in the card (referenced to GitHub but not quoted).
- Scale and composition of the internal refusal evaluation dataset (only "thousands of queries" across 6 languages is stated).
- Results with vs. without system prompt mitigation for most metrics are not provided in comparative table form — only the final mitigated results are reported for most evaluations.
- Whether third-party auditors (government labs, external red teams) were involved is not mentioned.
- The "model grading" component of RL training is not elaborated.
- No information on model size or architecture.
