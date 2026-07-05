---
stem: "Anthropic-Challenges_of_Automated_Red-Teaming_for_LLMs_2401.03315"
company: "Anthropic"
reader_model: "sonnet"
confidence: "low"
theme_tags: [ai-lab-practices, contamination-robustness, best-practices]
headline_numbers:
  - "212 real-world Malla samples collected from underground marketplaces (p.1)"
  - "182 jailbreak prompts identified circumventing public LLM APIs (p.1)"
  - "93.40% of Mallas offer malicious code generation (p.6)"
  - "WormGPT generated $28,325 revenue in ~2 months (July-September 2023) (p.8)"
  - "Malla pricing: $5-199/month vs $399 for conventional malware (p.8)"
---

## 1. Gist

**CRITICAL NOTE: The extract filename and stem suggest this is an Anthropic paper on "Challenges of Automated Red Teaming for LLMs." However, the actual extract content is the paper "Malla: Demystifying Real-world Large Language Model Integrated Malicious Services" (arXiv:2401.03315) by Lin et al. from Indiana University Bloomington — not an Anthropic paper. Anthropic is mentioned only as one of several LLM vendors whose APIs were exploited by Malla services. This card documents the actual extract content.**

The paper presents the first systematic empirical study of 212 real-world "Malla" — malicious LLM-integrated applications operated as underground services. The authors collect data from nine underground marketplaces and forums (Feb 2023–Oct 2023), identify 14 commercial Malla services and 198 publicly accessible Malla projects, and analyze their ecosystem, pricing, technical infrastructure, and quality of malicious output. Key findings: Mallas overwhelmingly use GPT-3.5/4 APIs with jailbreak prompts (most common technique) or uncensored open-source LLMs; malicious code generation dominates (93.4% of Mallas); Malla projects on FlowGPT had 2.75x higher average usage than non-Malla projects; safety measures on LLM platforms were inadequate and frequently bypassed.

## 2. Alignment/values methods used

This paper does not describe any alignment methods — it is an empirical study of misuse. However, it documents the failure modes of existing alignment measures:
- **Jailbreak prompts** successfully bypassed Constitutional AI-trained models (gpt-3.5-turbo, Claude-2, etc.)
- **Uncensored fine-tuned models** (e.g., Luna AI Llama2 Uncensored) were exploited without any safety bypass needed
- **Platform usage policies** were enforced inadequately — XXXGPT violated Poe's policies but operated undetected from July 2023 to March 2024

The paper notes that LLM vendors like OpenAI (RLHF + red-teaming), Anthropic (Constitutional AI), and Meta had implemented safety measures that were systematically circumvented (p.3).

## 3. Values specification

Not applicable — this is a security research paper, not a values specification document. The paper implicitly treats non-harm and non-facilitation of cybercrime as the operative values that LLM safety measures are supposed to protect. The documented failure is that these values were not reliably enforced in deployment.

## 4. Safety & values evaluation methodology

The authors conducted empirical evaluation of Malla-generated content quality across three malicious task types:
- Malicious code generation (compilability, VirusTotal evasion)
- Phishing email generation (readability via OOPSpam spam scoring)
- Phishing site creation (browser executability, URL scan evasion)

For their own research ethics, the study was IRB-approved, followed Menlo Report principles, limited interactions to single-account queries, deleted chat history post-testing, and pursued responsible disclosure to Anthropic, OpenAI, Meta, Poe, and FlowGPT (p.5-6).

## 5. Benchmarks used or introduced

The paper does not introduce formal benchmarks. Evaluation metrics used:
- **VirusTotal**: Used to assess whether Malla-generated malware evaded detection
- **OOPSpam**: Used to assess phishing email quality/readability
- **NSFW Text Classifier**: Used to triage suspicious Malla projects on Poe and FlowGPT
- **LLM authorship attribution classifier**: Used to reverse-engineer backend LLMs used by Mallas (p.4)

The authors developed a dataset of 182 jailbreak prompts across five public LLM APIs, and 45 malicious prompts for content generation tasks (p.1, Table 2, p.5).

## 6. Agentic / multiturn evaluation aspects

Not directly applicable — the paper focuses on single-turn or short multi-turn interactions. However, Malla services themselves represent a form of agentic misuse: they act as intermediary services that wrap LLM APIs with malicious system prompts and deploy them at scale. The authors describe the Malla workflow as a multi-step pipeline (develop → deploy → promote → purchase → interact → use) that functions as a service ecosystem (p.3, Figure 1).

## 7. Key numbers

- **212** real-world Malla samples studied (p.1)
- **182** jailbreak prompts identified circumventing public LLM APIs (p.1)
- **14** commercial Malla services and **198** Malla projects (p.6)
- **93.40%** of Mallas offer malicious code generation; 41.51% phishing email; 17.45% scam sites (p.6)
- **10,603** average usage volume of Malla projects on FlowGPT vs. **3,846** for non-Malla (p.7)
- **$28,325** WormGPT revenue over ~2 months Jul–Sep 2023 (~$15,965/month) (p.8)
- Malla pricing: **$5-$199/month** vs. **$399** for conventional malware (p.8)
- **69.60%** of Poe Malla projects and **86.30%** of FlowGPT projects remained available after responsible disclosure (p.7)
- **24/25** Malla service listings remained active on underground marketplaces through the study period (p.7)
- **5 public LLM APIs** targeted by the 182 jailbreak prompts; OpenAI most frequently targeted (p.1)

## 8. Findings relevant to values-benchmark design

Several findings are directly relevant to values-benchmark design:

1. **Safety training is necessary but not sufficient**: Models trained with Constitutional AI (Claude) and RLHF (GPT-3.5/4) were still exploitable via jailbreak prompts. Values benchmarks that only test "refusal in standard conditions" dramatically underestimate real-world vulnerability.

2. **Benchmark contamination via open-source fine-tunes**: Uncensored models derived from Llama-2 (e.g., Luna AI Llama2 Uncensored) completely bypass alignment-trained evaluation metrics. Benchmark results from safety-trained models may not generalize to fine-tuned or uncensored variants.

3. **Platform-level enforcement gap**: Even when models refuse, hosting platforms (Poe, FlowGPT) may permit deployment of jailbroken wrappers. Values evaluations should test not just the base model but the full deployment stack.

4. **Quality of harmful output is measurably high**: Some Mallas (DarkGPT, EscapeGPT) generated compilable malware that evaded VirusTotal, and phishing emails that bypassed OOPSpam — suggesting that safety benchmarks relying on crude toxicity classifiers may miss technically sophisticated harmful outputs.

5. **Adversarial ecosystem evolves faster than defenses**: From first Malla listing (April 2023) to rapid proliferation (July-August 2023), the timeline suggests any static values benchmark would be outdated within months.

## 9. Novel ideas worth stealing

- **Real-world misuse monitoring as a benchmark signal**: Rather than only running lab evaluations, track how models are being exploited in the wild (e.g., via underground marketplace monitoring). This provides ecological validity that curated benchmark sets lack.

- **Jailbreak prompt taxonomy**: The paper's collection of 182 real-world jailbreak prompts from 5 APIs represents a naturalistic adversarial test set. A values-alignment benchmark could incorporate a "jailbreak robustness" subsection using real jailbreaks rather than researcher-constructed ones.

- **Full-pipeline evaluation**: Evaluate the model's output quality on genuinely harmful tasks (not just refusal rates) — does the model's refusal actually prevent harm, or do fine-tuned/jailbroken variants complete the task at high quality?

- **Platform accountability dimension**: Test not just model behavior but how the model behaves when deployed through LLMA hosting platforms that may strip or ignore system-level guardrails.

## 10. Notable quotes

1. "We observe that miscreants utilized an LLM-integrated application (LLMA) hosting platform, Poe offered by Quora, to showcase a 'vouch copy' of their Malla. Despite the violation of the platform's usage policies, this activity went unchecked throughout our observation window from July 2023 to March 2024." (p.1-2)

2. "Our findings bring to light that certain Mallas, like DarkGPT and EscapeGPT, excel in producing high-quality malicious code that is both compilable and capable of evading VirusTotal detection." (p.1)

3. "Malla projects have garnered significantly more usage than non-Malla projects, illuminating the alarming extent of LLM misuse in the cyber threat landscape." (p.7)

4. "The fact that a high percentage of Mallas remain active despite disclosures indicates an urgent need for actions to be taken by the stakeholders and a pressing demand for holding them accountable." (p.7)

## 11. UNKNOWN / not in extract

- **FILE MISMATCH**: The extract file is labeled as Anthropic's paper on "Challenges of Automated Red Teaming for LLMs" (arXiv:2401.03315) but the content is the "Malla" paper (also arXiv:2401.03315) by Indiana University. The arXiv number appears to be shared or mislabeled. The actual Anthropic red-teaming paper (if it exists with this number) is NOT in this extract.
- Specific jailbreak prompt texts are described as released as artifacts but not reproduced in the extract.
- Detailed quality metrics tables for malicious code generation, phishing emails, and phishing sites (Sections 5+) are not captured in the first 22 pages read — the extract ends before the full quality analysis.
- The paper's reverse-engineering methodology for attributing backend LLMs is described briefly but details are in later sections not fully extracted.
- Anthropic's internal response to the responsible disclosure is not described.
