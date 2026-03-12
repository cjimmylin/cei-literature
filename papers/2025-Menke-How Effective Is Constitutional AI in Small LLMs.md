---























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 9RIP3LZI
type: conferencePaper
short_title: "How Effective Is Constitutional AI in Small LLMs?"
year: 2025
first_author: "[[Antonio-Gabriel Chacón Menke]]"
last_author: "[[Phan Xuan Tan]]"
authors: Antonio-Gabriel Chacón Menke; Phan Xuan Tan
doi: 10.48550/arXiv.2503.17365
url: "http://arxiv.org/abs/2503.17365"
pdf_extract: "PDF Extracts/2025/2025-Menke-How Effective Is Constitutional AI in Small LLMs.md"
local_pdf: "[[PDFs/2025/2025-Menke-How Effective Is Constitutional AI in Small LLMs.pdf]]"
external_pdf: "http://arxiv.org/pdf/2503.17365.pdf"
publication: arXiv.org
CONF-CC: "Preprint"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: Utilitarianism
key_contribution: "Studies the effectiveness of Constitutional AI (CAI) self-critique on small (7-9B) models like DeepSeek-R1 and Llama 3"
significance: "Finds that CAI efficacy is highly architecture-dependent; Llama models improve significantly, while others show little gain, suggesting alignment techniques are not essentially transferable across model sizes"
tags: 
abstract: "Recent incidents highlight safety risks in Large Language Models (LLMs), motivating research into alignment methods like Constitutional AI (CAI). This paper explores CAI’s self-critique mechanism on small, uncensored 7-9B parameter models: DeepSeek-R1-8B, Gemma-2-9B, Llama 3.1-8B, and Qwen2.5-7B. We show that while Llama-based models exhibited significant harm reduction through self-critique, other architectures demonstrated less improvement in harm detection after abliteration."
paper_summary: "Abstract: Recent incidents highlight safety risks in Large Language Models (LLMs), mo- tivating research into alignment methods like Constitutional AI (CAI). This pa- per explores CAI's self-critique mechanism  | Overview: HOW EFFECTIVE IS CONSTITUTIONAL AI IN SMALL LLMS? A STUDY ON DEEPSEEK-R1 AND ITS PEERS Antonio-Gabriel Chac´on Menke Shibaura Institute of Technology, Tokyo Kempten University of Applied Sciences, Kem | Methodology: We experiment with four small instruction models in the 7-9B parameter range: DeepSeek-R1-Distill-Llama-8B (DeepSeek-AI et al., 2025) (R1-Llama); Gemm | Conclusions: Figure 1 shows that models based on the Llama architecture (R1-Llama and Llama-3.1) demon- strated the strongest harm reduction in their revised respo"
DATE_ADDED: 20260208
LLM_assessed: "DeepSeek, Gemma, Llama-3, Qwen"
DATA_URL: "https://zenodo.org/records/12608602"
CONFERENCE: "Other Conference"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "Yes"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "90 prompts"
---
 How Effective Is Constitutional AI in Small LLMs? A Study on DeepSeek-R1 and Its Peers

## Authors

[[Antonio-Gabriel Chacón Menke]], [[Phan Xuan Tan]]

## Links

- **Local PDF:** [[PDFs/2025/2025-Menke-How Effective Is Constitutional AI in Small LLMs.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2503.17365
- **DOI:** https://doi.org/10.48550/arXiv.2503.17365

## Abstract

This paper investigates the effectiveness of **Constitutional AI (CAI)** self-critique mechanisms in small (7-9B parameter) Large Language Models (LLMs), specifically **DeepSeek-R1-8B, Gemma-2-9B, Llama 3.1-8B, and Qwen2.5-7B**. To isolate the intrinsic effectiveness of CAI, the models were first "abliterated" to suppress their pre-existing refusal behaviors. The study reveals that while Llama-based architectures (especially DeepSeek-R1) show significant harm reduction via self-correction, other architectures like Qwen and Gemma struggle to identify harmful content during the critique phase, sometimes even suggesting "improvements" to harmful responses.

### Detailed Summary
The research explores whether "small" models can replicate the safety breakthroughs seen in much larger proprietary models like Claude (which pioneered CAI). The authors use a three-step process: **Initial Generation -> Self-Critique -> Revision**. By using abliterated (uncensored) models, they force the model to rely purely on its constitutional "rules" during the critique phase rather than built-in guardrails. The results show a "Reasoning Dividend": DeepSeek-R1, which includes an explicit reasoning (thinking) step, was the most consistent at identifying its own harmful outputs and revising them into polite refusals, whereas other models often "drifted" toward maintaining harmful content while merely adding warnings.

### Paper Outline
1.  **Introduction**: The need for accessible, resource-efficient alignment methods (CAI).
2.  **Methodology**: Selection of 7-9B models, the "Abliteration" technique, and the 3-step CAI pipeline.
3.  **Results**: Performance analysis using HarmBench categories (Chemical, Biological, Cybercrime, etc.).
4.  **Benchmark Testing**: Impact of abliteration on general knowledge and Ethical/Safety Benchmarks.
5.  **Conclusion**: Architectural variations in CAI efficacy.

### Methods Summary
*   **CAI Pipeline**:
    1.  **Initial**: Prompting with a harmful HarmBench query.
    2.  **Critique**: "Identify if the answer is harmful... recommend refusing... describe specific changes."
    3.  **Revision**: "Rewrite the original response... politely refuse if necessary."
*   **Abliteration**: A technique that removes a single activation direction responsible for refusal, creating a baseline of "uncensored" behavior.
*   **Evaluation**: 90 prompts from HarmBench evaluated by a separate model and manual check.
*   **Benchmarks**: MMLU (Knowledge), ETHICS Commonsense (Morality), and SafetyBench.

### Results Summary
1.  **Llama Superiority**: **Llama 3.1-8B** and **DeepSeek-R1-8B** (Llama-based) reduced harmful response rates from ~87% (initial) to ~11-38% (revised).
2.  **Qwen/Gemma Failure**: These models showed minimal improvement (e.g., Qwen: 76.7% -> 67.8%), often failing to see any harm in their initial unethical responses.
3.  **Reasoning Step Impact**: DeepSeek-R1 demonstrated lower standard deviation in its safety performance, suggesting its "Thinking" blocks help it bridge the gap between "Moral Knowledge" and "Moral Application."
4.  **Abliteration Side-Effects**: Qwen-2.5 suffered a 20-point drop in Ethics benchmark scores after abliteration, suggesting its moral reasoning is more fragile or "intertwined" with its refusal directions compared to Llama.

### Conclusions
Constitutional AI is a viable self-alignment technique for small models, but its success is heavily dependent on **model architecture and reasoning capabilities**. Llama-based models are currently the most robust platform for implementing CAI in resource-constrained settings. The authors suggest that specialized "safety-reasoning" (like R1) is the key to effective self-critique.

### Artifact Contributions
*   **Constitutional AI Self-Critique Prompts**: Optimized instructions for small models to identify harm without false positives.
*   **Abliteration Baseline**: A method for testing "true" alignment efficacy by removing surface-level refusal triggers.

## Data Description

The study evaluates Constitutional AI's self-critique mechanism on four small uncensored 7-9B parameter models: DeepSeek-R1-Distill-Llama-8B, Gemma-2-9B-it, Llama 3.1-8B-Instruct, and Qwen2.5-7B-Instruct. The evaluation uses 90 HarmBench prompts randomly selected across six harm categories, with additional benchmark testing on MMLU, tinyBenchmarks, ETHICS, and SafetyBench.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Machine-Learning

## Citation Info

0 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23] arXiv:2503.17365 [cs]
