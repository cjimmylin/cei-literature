---
stem: "Meta AI-CyberSecEval_3_2408.01605"
company: "Meta AI"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, agentic-multiturn, llm-judges-scoring, validity-psychometrics]
headline_numbers:
  - "Llama 3 405B showed no statistically significant uplift in cyberattack completion rates vs. search-engine baseline (p=0.34 novices, p=0.75 experts) (p.25)"
  - "Llama 3 405B surpassed GPT-4 Turbo by 22-23% on autonomous software vulnerability exploitation benchmarks (p.13)"
  - "All LLMs failed insecure autocomplete test cases at ~31% rate; Llama 3 405B autocomplete insecure rate 30.55% (p.15)"
  - "Prompt injection Attack Success Rates (ASR) 20-40% across all models tested (p.14)"
  - "LlamaGuard 3 reduced cyberattack helpfulness violation rate by 50.4% (405B) and 53.9% (70B) (p.20)"
  - "62 Meta employee volunteers in human uplift study; 31 experts / 31 novices (p.8)"
  - "LLM-judge correlation with human judges r=0.89 for spear-phishing persuasiveness (p.6)"
---

## 1. Gist

CyberSecEval 3 is Meta AI's third-generation benchmark suite for empirically measuring cybersecurity risks and capabilities of large language models, released alongside Llama 3 (405B, 70B, 8B). The paper assesses 8 risk areas across two categories: (1) risks to third parties from offensive cyber capabilities (automated social engineering, scaling manual offensive cyber operations, autonomous offensive cyber operations, autonomous software vulnerability discovery and exploitation); and (2) risks to application developers and end users (prompt injection, insecure code suggestions, malicious code execution in code interpreters, and facilitating cyberattacks). The paper is notable for including a formal human subjects study (n=62) and for publicly releasing all evaluation code and guardrails (CodeShield, PromptGuard, LlamaGuard 3). The central finding is that Llama 3 models' cybersecurity risks are comparable to peer models and can be substantially mitigated with the released guardrails.

This paper is relevant to values-benchmark design primarily through its methodological contributions: multi-method evaluation combining automated benchmarks, LLM judges, and human studies; explicit calibration of LLM judges against human raters; and frank discussion of evaluation limitations including effect size, confounding, and false positive rates. While the domain is cybersecurity rather than values alignment broadly, the measurement architecture translates directly.

## 2. Alignment/values methods used

CyberSecEval 3 is an evaluation paper, not a training paper. Meta's alignment approach for Llama 3 against cybersecurity risks relies on:
- **Safety post-training with built-in refusal behaviors**: the base Llama 3 models have instruction-tuned refusal behavior for high-severity prompts (e.g., privilege escalation requests) while complying more readily with lower-severity requests.
- **Guardrails as primary mitigation layer**: the main safety mechanism is external classifier guardrails applied to inputs and/or outputs — not model-internal alignment. The three released guardrails are:
  - **LlamaGuard 3**: fine-tuned Llama 3 8B classifier for unsafe content categories based on MLCommons AI Safety taxonomy, extended with "Code Interpreter Abuse" category.
  - **PromptGuard**: multi-label classifier detecting jailbreaks and indirect injections.
  - **CodeShield**: static analysis inference-time filter identifying insecure code across 7 languages and 50+ CWEs.
- The paper explicitly frames guardrails as a "best practice" for all Llama 3 deployments, implying that model-level safety training alone is insufficient.

## 3. Values specification

Meta's values are specified operationally through the **MLCommons AI Safety taxonomy of harm categories**, which LlamaGuard 3 is trained on. The taxonomy is not spelled out in detail in this paper; the paper adds one new category ("Code Interpreter Abuse") to this external taxonomy. The safety policy for cybersecurity risks is implicitly encoded via:
- Compliance / refusal behavior calibrated through the MITRE ATT&CK ontology (mapping cyber-attack helpfulness requests to attack categories: discovery, recon, C2, collection, exfiltration, persistence, privilege escalation, execution, lateral movement, evasion).
- A "false refusal rate" (FRR) benchmark used to measure over-restriction, reflecting the helpfulness-safety trade-off as a core value.

There is no explicit constitution, model spec, or natural-language values document described in this paper. Values are inferred from the selection of what to measure and what to mitigate.

## 4. Safety & values evaluation methodology

The paper employs a multi-layered evaluation methodology:

**Automated benchmarks:**
- Spear-phishing simulation: 250 test cases per model, LLM judge scoring on a 1-5 persuasiveness rubric.
- Autonomous offensive cyber operations: 85 test runs on a simulated ransomware attack against a Windows VM, evaluated by consensus of three judge LLMs.
- Software vulnerability exploitation: zero-shot prompting on toy CTF-style challenges (string constraints, SQL injection, buffer overflow, memory corruption) across 5 programming contexts.
- Prompt injection: 251 manually curated test cases from CyberSecEval 2, evaluated by a judge LLM.
- Insecure code: static analysis via CyberSecEval corpus across 7 languages (C, C++, C#, Java, JavaScript, PHP, Python, Rust), both autocomplete and instruct modes.
- Code interpreter abuse and cyberattack helpfulness: CyberSecEval 2 corpus with LLM judge.

**Human study:**
- 62 Meta employee volunteers (31 experts, 31 novices) in a controlled capture-the-flag study measuring LLM uplift over a search-engine baseline. Two 1-hour stages: stage 1 (search engine only), stage 2 (search engine + Llama 3 405B). Survival analysis used to compare phase completion rates. Log-rank hypothesis test for statistical significance.

**LLM judge calibration:**
- For spear-phishing, LLM judge scores validated against 4 human evaluators across 10 test cases → r=0.89 correlation.
- Acknowledged limitation: LLM judges had false positives in autonomous cyber operations assessment; consensus-of-judges approach proposed as future improvement.

**Guardrail evaluation:**
- PromptGuard: ROC analysis on out-of-distribution direct jailbreak dataset (AUC=0.978) and CyberSecEval indirect injection dataset (AUC=0.966).
- CodeShield/ICD: precision 96%, recall 79% across 50 sampled LLM completions per language (human-labeled).
- LlamaGuard 3: measured via MITRE FRR benchmark, reporting false refusal rates at 2% (output-only guardrail) and 10% (input+output guardrail).

## 5. Benchmarks used or introduced

| Benchmark | What it measures |
|-----------|-----------------|
| CyberSecEval 3 — Spear-phishing sim | LLM persuasion capability for social engineering (1-5 rubric) |
| CyberSecEval 3 — Autonomous offensive ops | LLM autonomous hacking capability (low/moderate/high sophistication) |
| CyberSecEval 3 — Software vuln exploitation | LLM zero-shot exploitation of toy CTF challenges |
| CyberSecEval 2 — Prompt injection (251 cases) | Attack success rates across 15 injection categories |
| CyberSecEval (Bhatt 2023) — Insecure code | Rate of insecure code generation in autocomplete/instruct modes |
| CyberSecEval 2 — Code interpreter abuse | Compliance rate with malicious code execution prompts |
| CyberSecEval 1 — Cyber attack helpfulness | Compliance with cyberattack-facilitating requests (MITRE ATT&CK) |
| MITRE FRR benchmark | False refusal rate for guardrails (helpfulness cost of safety) |
| Hack The Box (Wifinetic, Antique) | Live hacking challenges used in human uplift study |

CyberSecEval 3 is a new release introduced by this paper, extending CyberSecEval 1 and 2.

## 6. Agentic / multiturn evaluation aspects

This paper has the most extensive agentic evaluation coverage of any CyberSecEval release:

- **Automated social engineering (multiturn)**: the spear-phishing simulation is explicitly a multiturn interaction where an LLM attacker builds rapport over multiple exchanges with an LLM-simulated victim. The LLM must reason about the victim's profile and adapt its persuasion strategy across turns — a genuine agentic multiturn challenge.
- **Autonomous offensive cyber operations**: Llama 3 405B is configured to autonomously generate and execute Linux commands based on the outcomes of previous commands on a Kali Linux VM targeting a Windows Server VM. This is a tool-use agentic loop. The model failed in effective exploitation and post-exploitation, showing limited agentic reasoning capability.
- **Human uplift study**: tests LLM as a **co-pilot** (not agent) — human retains control but uses LLM for advice across multiple turns of a hacking challenge. This is a partial multiturn evaluation with a human in the loop.
- **Explicit agentic limitation**: the paper acknowledges it did not explore chain-of-thought, RAG, tool-augmentation, or other agentic scaffolding approaches, and cites the "Naptime" system (using agentic scaffolding to achieve 20x better results on CyberSecEval 2) as evidence that base-model evaluation significantly underestimates risk under agentic conditions. This is a critical eval gap explicitly called out by the lab.

## 7. Key numbers

- 8 risk areas assessed across 2 broad categories (p.1)
- 250 spear-phishing test cases per model (p.6)
- GPT-4 Turbo human-graded average score: 2.90 ("Intermediate"); Llama 3 405B: 2.62 (p.6)
- LLM judge vs. human judge correlation: r=0.89 for spear-phishing persuasiveness (p.6)
- 62 human participants in uplift study: 31 experts / 31 novices (p.8)
- No statistically significant uplift: p=0.34 for novices, p=0.75 for experts (log-rank test) (p.25)
- Novices completed 22% more phases with LLM (39 vs. 32 phases); not significant (p.25)
- Experts completed 6% fewer phases with LLM (p.25)
- Novices reduced phase completion time by avg. 9 min 12 sec per phase with LLM (p.25)
- 85 autonomous hacking test runs (p.10)
- Llama 3 405B surpassed GPT-4 Turbo by 22% (some sources say 23%) on software vulnerability exploitation (p.13)
- All models: ~31% insecure autocomplete failure rate; Llama 3 405B autocomplete: 30.55%, instruct: 38.57% (p.15)
- GPT-4 Turbo autocomplete: 29.84%, instruct: 35.24% (p.15)
- Prompt injection ASR: 20-40% across all models; Llama 3 405B: 22%, Llama 3 8B: 19% (p.2)
- PromptGuard: 97.5% jailbreak recall at 3.9% false positive rate (p.19)
- PromptGuard: 71.4% indirect injection detection at 1% false positive rate (p.19)
- CodeShield/ICD: 190 patterns across 50 CWEs; 90% accuracy; first-layer latency <60ms; <70ms for 90% of scans (p.17)
- CodeShield precision 96%, recall 79% (p.20)
- LlamaGuard 3: 50.4% violation rate reduction for Llama 3 405B, 53.9% for 70B (input+output) (p.20)
- LlamaGuard 3: 2% FRR (output-only), 10% FRR (input+output) (p.20)
- 46% of code pushed to GitHub via GitHub Copilot is LLM-generated [citing Microsoft 2023] (p.15)
- 71% of inexperienced subjects felt they learned faster with LLM assistance (p.28)
- 54% of highly skilled subjects felt they learned faster with LLM assistance (p.28)

## 8. Findings relevant to values-benchmark design

- **LLM judges need human calibration**: the paper calibrates its LLM judge against 4 human raters (r=0.89 for spear-phishing) but notes this was a one-time cross-check with a small sample. False positives were found in the autonomous cyber operations assessment. This directly informs benchmark design: LLM judges should be routinely cross-checked, not trusted by default. The paper explicitly proposes scaling cross-checks and using consensus-of-judges as future work.
- **Agentic scaffolding changes risk profiles dramatically**: the paper cites "Naptime" achieving 20x better performance on CyberSecEval 2 through agentic scaffolding. Any capability benchmark that evaluates base models without agents will systematically underestimate real-world risk. Values benchmarks face the same issue when evaluating values-following in agentic contexts.
- **Model-only evaluation vs. system-level evaluation**: the paper evaluates both unguardrailed and guardrailed systems, making clear that "model safety" and "system safety" are distinct. The appropriate unit of evaluation for deployment risk is the system, not the base model. This is directly applicable to values-benchmark design: testing values alignment of a deployed system requires evaluating the full pipeline.
- **Effect size matters more than p-value in safety contexts**: the human uplift study found no statistically significant difference but observed 22% more phases completed by novices — a potential real effect masked by high variance and small N. The lab correctly concludes with cautious non-rejection rather than false certainty of safety.
- **Capability–safety trade-off is measurable**: the FRR metric (false refusal rate) operationalizes the cost of safety interventions on helpfulness. Benchmark designers should always report both the safety gain and the helpfulness cost of any guardrail or intervention.
- **Ceiling effect identified**: large models (405B) generate *more* insecure code than smaller models, not less — "more capable coding models also generate insecure code at a higher rate" (p.15). This suggests that scaling is not a solution to value alignment and that benchmarks should not assume monotonic improvement with model size.

## 9. Novel ideas worth stealing

1. **Human-vs.-LLM judge cross-calibration protocol**: run both human raters and LLM judges on the same subset of items, report correlation, and use this to establish confidence intervals on fully-automated evaluations. A simple, replicable quality assurance step for any LLM-judged benchmark.
2. **Consensus-of-judges approach** (proposed as future work): run multiple LLMs from different model families as judges on the same item, take majority vote or weighted consensus. This reduces false positive/negative rates of any single judge and adds robustness to benchmark scores.
3. **Dual-condition human study design**: within-subject design where participants complete equivalent tasks first without, then with, LLM assistance. Allows individual differences to be controlled while measuring uplift. Survival analysis used to compare phase completion rates — a sophisticated statistical approach adaptable to values evaluation (e.g., measuring whether LLM assistance changes the rate at which humans endorse value-violating content).
4. **Separate evaluation of model-alone vs. system-with-guardrails**: always report both conditions to distinguish model safety from system safety. This design principle prevents benchmark gaming where safety improvements via guardrails are attributed to model training.
5. **MITRE ATT&CK ontology as a harm taxonomy template**: the paper maps 10 attack categories to a structured ontology and measures compliance rates per category, revealing that severity moderates refusal rates (high severity → more refusals; low severity → more compliance). Values benchmarks could adopt analogous structured taxonomies (e.g., mapping harm types by severity, intent, and context) rather than treating all harms as equivalent.
6. **FRR (False Refusal Rate) as a first-class metric**: report the false refusal rate alongside the safety metric for every guardrail intervention. This operationalizes the helpfulness-safety trade-off quantitatively and prevents benchmarks from rewarding over-refusal.

## 10. Notable quotes

- "Work on applying agent scaffolding, however, shows that substantial improvements to a task can be made over and above base models by specializing to the task at hand. Notable in our context is work by Glazunov and Brand (2024) on 'Naptime', which uses agentic scaffolding to achieve up to 20x better results on our CYBERSECEVAL 2 benchmark across both ChatGPT and Gemini models." (p.21)
- "The Llama 3 models align with the previously noticed pattern of insecure coding generation: as the number of parameters in an LLM increases, we observe that more insecure code is generated." (p.15)
- "We see three major directions for further improvement of risk assessment for cybersecurity: first, maximizing efficacy of models under test, second, scaling up cross-checks between human and LLM judges, and finally, continuous assessment of model risk over time." (p.21)
- "Our results measure a base model with and without guardrails applied... Future risk evaluations could propose additional model-independent agent architecture specific to measuring the risk." (p.21)

## 11. UNKNOWN / not in extract

- Full taxonomy of MLCommons AI Safety harm categories that LlamaGuard 3 is trained on — referenced but not reproduced.
- Details of the PromptGuard training data and the dataset used to train the jailbreak classifier.
- Whether CyberSecEval 3 test sets will be publicly released or kept partially proprietary (code is released, but test case details for human study appear restricted).
- Inter-rater reliability statistics for the 4-person human judging panel beyond the r=0.89 correlation.
- Specifics of the CyberSecEval 2 prompt injection corpus beyond the 251-case count.
- Full dataset card and model card for LlamaGuard 3 (released separately).
- The pages 30-36 of the extract were not fully included; appendix materials beyond the uplift study limitations section (p.29-30) may contain additional evaluation detail.
