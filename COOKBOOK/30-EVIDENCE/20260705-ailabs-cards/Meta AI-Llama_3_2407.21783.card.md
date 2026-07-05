---
stem: "Meta AI-Llama_3_2407.21783"
company: "Meta AI"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, best-practices, agentic-multiturn, contamination-robustness]
headline_numbers:
  - "Llama 3 405B achieves 87.3% on MMLU (5-shot), comparable to GPT-4 (0125) at 85.1% (p.2)"
  - "Pre-training corpus: ~15T multilingual tokens vs. 1.8T for Llama 2 (p.1)"
  - "Memorization rate (405B, n=50): 1.13% average verbatim inclusion (p.42)"
  - "Llama Guard 3 reduces violations by 65% on average across benchmarks (p.50)"
  - "Full Llama Guard (input+output) reduces English VR by -86% at cost of +102% FRR (p.50)"
  - "CBRNE uplift study with 62 internal volunteers found no significant uplift from Llama 3 (p.47)"
  - "Prompt injection attacks against Llama 3 405B successful 21.7% of the time (p.46)"
  - "Llama 3 405B complied with malicious code interpreter prompts 10.4% of the time (p.46)"
  - "Over 4000 benchmark prompts per capability or language, mixing single- and multi-turn (p.41)"
---

## 1. Gist

This paper presents the Llama 3 herd of open foundation models (8B, 70B, 405B parameters), covering pre-training, post-training, safety methodology, and multimodal extensions. The safety sections (Section 5.4) detail Meta's end-to-end responsible development approach: internal benchmark construction, safety finetuning (SFT + SafetyDPO), red teaming, cybersecurity and CBRNE uplift assessments, and system-level safety via Llama Guard 3. The paper is notable for explicitly tracking both Violation Rate (VR) and False Refusal Rate (FRR) as dual metrics, acknowledging the safety–helpfulness tradeoff as a first-class design constraint.

## 2. Alignment/values methods used

- **Supervised Finetuning (SFT)**: Combines helpfulness and safety data; ratio of adversarial to borderline prompts is carefully tuned per model size (p.43).
- **Direct Preference Optimization (DPO)**: Used after SFT; Meta found DPO requires less compute than PPO at scale and adopted algorithmic modifications including formatting token masking and NLL regularization on chosen sequences (coefficient 0.2) (p.11).
- **SafetyDPO**: A specialized DPO variant using adversarial and borderline response pairs crafted to be nearly orthogonal in embedding space, teaching the model to distinguish good from bad responses (p.43).
- **Rejection Sampling (RS)**: Used in conjunction with reward model to select highest-quality SFT candidates (p.11).
- **Reward Model (RM)**: Trained on top of the pre-trained checkpoint; used to score rejection-sampled candidates (p.11).
- **System-level safety (Llama Guard 3)**: A separate 8B classifier fine-tuned to detect unsafe inputs/outputs; deployed as input/output filter around the main model (p.49).

## 3. Values specification

Meta does not describe a single published constitution or model spec in this paper, but operationalizes values through:
- **Internal safety policy**: Referenced throughout as the basis for benchmark and annotation guidelines; not published in full.
- **ML Commons AI Safety Taxonomy (Vidgen et al., 2024)**: Used as the hazard category framework for Llama Guard 3 training; 13 categories including Child Sexual Exploitation, Hate, Indiscriminate Weapons, Privacy, Suicide & Self-Harm, Violent Crimes, etc. (p.49).
- **Refusal tone guideline**: A specific guideline was developed for how models should phrase refusals, with zero-shot rewriting and human-in-the-loop editing to align training data to the guideline (p.43).
- **Dual metrics (VR + FRR)**: Helpfulness is operationalized partly through False Refusal Rate, creating an explicit tension managed through data mix ablations.

## 4. Safety & values evaluation methodology

- **Internal benchmarks**: Over 4,000 prompts per capability/language mixing adversarial and borderline prompts (p.41). Categories include English text, multilingual text, long context (DocQA, many-shot), and tool use (search).
- **Violation Rate (VR) + False Refusal Rate (FRR)**: Dual metric framework used throughout. A model that always refuses is "maximally safe, but not helpful in the slightest" (p.44).
- **Red teaming**: Recurring exercises by internal experts in cybersecurity, adversarial ML, responsible AI, and integrity, plus multilingual content specialists and external subject-matter experts (p.48). Attacks include multi-turn refusal suppression, hypothetical scenarios, personas/role-play, gradually escalating violation, unsafe tool chaining, language mixing.
- **Memorization audits**: Verbatim memorization measured using rolling hash n-gram index; evaluated across different prompt/ground-truth length, language, and domain (p.42).
- **CBRNE uplift study**: Six-hour structured exercises with 62 internal volunteers (31 novice, 31 expert) across biological and chemical attack scenarios (p.47).
- **Cybersecurity uplift study**: Two-stage study with the same 62 volunteers; both novice and expert showed insignificant uplift beyond open internet access (p.47).
- **CyberSecEval benchmark**: External framework measuring insecure code generation, malicious code, textual prompt injection, vulnerability identification (p.46).
- **Benchmark quality assurance**: Modeling teams did not have access to human-evaluation prompts to prevent contamination (p.40).

## 5. Benchmarks used or introduced

- **MMLU (5-shot, 0-shot CoT)**: General knowledge (p.2)
- **MMLU-Pro (5-shot CoT)**: More rigorous general knowledge (p.2)
- **IFEval**: Instruction following (p.2)
- **HumanEval, MBPP EvalPlus**: Code generation (p.2)
- **GSM8K, MATH**: Mathematical reasoning (p.2)
- **ARC Challenge**: Commonsense reasoning (p.2)
- **GPQA**: Graduate-level science questions (p.2)
- **BFCL, Nexus**: Tool use / function calling (p.2)
- **ZeroSCROLLS/QuALITY, InfiniteBench/En.MC, NIH/Multi-needle**: Long-context understanding (p.2)
- **MGSM**: Multilingual reasoning (p.2)
- **ToxiGen, XSTest**: External safety benchmarks mentioned as insufficiently broad for new capabilities (p.41)
- **CyberSecEval (Bhatt et al., 2023, 2024)**: Cybersecurity risk evaluation (p.46)
- **Internal safety benchmarks (>4000 prompts/capability)**: Meta-specific VR/FRR benchmarks; not publicly released (p.41)
- **Llama Guard 3 evaluation benchmarks**: Spanning 13 ML Commons hazard categories plus Code Interpreter Abuse (p.49)

## 6. Agentic / multiturn evaluation aspects

Multi-turn evaluation is a significant focus. Key findings:
- Multi-turn conversations generally lead to more harmful outputs than single-turn; "multi-turn conversations lead to more harmful outputs" (p.48).
- Red team identified specific multi-turn attack patterns: refusal suppression, gradually escalating violation, unsafe tool chaining, multi-turn role-playing.
- Benchmarks include both single-turn and multi-turn prompts (p.41).
- Long-context many-shot jailbreaking (Anil et al., 2024) is explicitly addressed with targeted SFT mitigation showing little impact on FRR (p.45).
- Microsoft's Crescendo multi-turn jailbreak strategy referenced as a known attack vector (p.47 in Phi-3 paper; here at p.48 in Llama context).
- Tool-use safety evaluation covers search; tool-chaining attacks where violating and benign tools are called simultaneously were discovered in red teaming (p.49).
- Attack automation (autonomous ransomware attack agents) tested but found to fail at exploit execution and post-exploitation (p.46–47).

## 7. Key numbers

- Pre-training tokens: ~15T multilingual tokens; Llama 2 used 1.8T (p.1)
- Flagship training compute: 3.8 × 10^25 FLOPs, ~50× more than largest Llama 2 (p.1)
- Model sizes: 8B, 70B, 405B parameters (p.1)
- Context window: 8K (pre-training) extended to 128K via continued pre-training (p.11)
- MMLU 5-shot: Llama 3 8B 69.4%, 70B 83.6%, 405B 87.3%; GPT-4 (0125) 85.1%, GPT-4o 89.1% (p.2)
- Memorization (405B, 50-gram): 1.13% English; 1.03% all languages; 3.91% at 1000-gram (p.42)
- Benchmark size: >4,000 prompts per capability/language (p.41)
- Llama Guard 3: -65% violations average across benchmarks (p.50)
- Full Llama Guard (English): -86% VR, +102% FRR (p.50)
- Prompt injection success rate (Llama 3 405B): 21.7% (p.46)
- Malicious code interpreter compliance (Llama 3 405B): 10.4%; Llama 3 70B: 3.8% (p.46)
- Spear phishing success: Llama 3 70B 24%, Llama 3 405B 14% (p.46)
- CBRNE uplift: No significant uplift vs. web-only control (n=62 volunteers, 31 novice / 31 expert) (p.47)
- Cybersecurity uplift study: insignificant uplift vs. open internet access (p.47)
- Human evaluation scale: 7-point scale, "win" = better or much better (p.40)

## 8. Findings relevant to values-benchmark design

1. **External benchmarks are insufficient**: ToxiGen, XSTest "lack sufficient coverage of breadth and depth" for new Llama 3 capabilities (tool use, long context, multimodal) — Meta built entirely new internal benchmarks (p.41). This is a direct call for more comprehensive, capability-specific benchmarks.
2. **Dual-metric necessity**: Tracking only violation rate is misleading; FRR must be co-reported. Models can game safety benchmarks by over-refusing. The VR/FRR scatter plot (Figure 21) reveals that competitors differ dramatically in which side of the tradeoff they favor.
3. **Safety knowledge does not transfer across languages**: "Safety knowledge in English does not readily transfer to other languages" (p.45). Benchmarks evaluated only in English miss systematic multilingual safety gaps.
4. **Model size matters for safety learning**: Smaller models (8B) require a higher proportion of safety data to match 70B safety performance; larger models are better at distinguishing adversarial from borderline (p.43). Benchmark difficulty should be calibrated to model size.
5. **Internal benchmarks not publicly reproducible**: Meta acknowledges "the numbers in this section are not reproducible externally" (p.44). This creates a reproducibility gap for safety benchmarking.
6. **Borderline prompts are as important as adversarial prompts**: The ratio of adversarial to borderline examples is a critical design variable; false refusal is a real harm that many benchmarks ignore entirely.
7. **Many-shot / long-context jailbreaks are an unsolved challenge**: Without targeted mitigation, long-context models are "vulnerable to many-shot jailbreaking attacks" (p.45). Benchmark coverage should extend to many-shot and document-grounded adversarial settings.

## 9. Novel ideas worth stealing

1. **Dual-metric benchmark reporting (VR + FRR scatter)**: Plot safety vs. helpfulness as a Pareto frontier per model, not a single aggregate score. This reveals where models trade off and lets benchmark users choose operating points.
2. **Borderline prompt category**: Deliberately curate prompts near the policy decision boundary and measure false refusal rate as a first-class output. A values benchmark should include "near-miss" items that well-calibrated models should handle helpfully.
3. **Capability-stratified safety evaluation**: Separate benchmarks per capability (English, multilingual, long context, tool use) rather than a single aggregate score. Aggregate scores can mask catastrophic failures in specific capability stacks.
4. **Orthogonal embedding pairs for preference data**: Crafting rejected/chosen response pairs to be nearly orthogonal in embedding space (SafetyDPO) is a principled approach to teaching fine distinctions that could be adapted to values-alignment benchmark annotation rubrics.
5. **Uplift study design**: The CBRNE study design (structured 6-hour exercises, 2-person teams, novice/expert strata, Delphi SME scoring) is a transferable template for measuring real-world capability uplift from models, applicable to values-laden domains beyond biosecurity.
6. **Rainbow Teaming (MAP-Elites for prompt diversity)**: Automated adversarial prompt generation constrained across multiple diversity dimensions (p.43) could be used to generate high-coverage values-alignment test items.

## 10. Notable quotes

- "We find that our models achieve very competitive violation rate metrics while keeping false refusal rate low as well, indicating a solid balance between helpfulness and safety." (p.44)
- "While a low violation rate is desirable, it is critical to consider false refusal as a counter-metric, as a model that always refuses is maximally safe, but not helpful in the slightest." (p.44)
- "Our experiments demonstrate that safety knowledge in English does not readily transfer to other languages, particularly given the nuance of safety policies and language-specific context." (p.45)
- "A number of the new capabilities in Llama 3 do not have sufficient external benchmarks available and often external benchmarks lack sufficient coverage of breadth and depth." (p.41)

## 11. UNKNOWN / not in extract

- Full text of Meta's internal safety policy guidelines (not published)
- Detailed breakdown of SFT data composition (number of adversarial vs. borderline vs. helpfulness examples)
- Human evaluation annotation workforce details (geography, expertise, compensation)
- Full Llama Guard 3 precision/recall numbers by hazard category
- Whether any external third-party audit of the CBRNE uplift study was performed
- Details of multimodal safety evaluation (image, video, speech models not yet released)
- Whether red team findings from external contractors were independently verified
