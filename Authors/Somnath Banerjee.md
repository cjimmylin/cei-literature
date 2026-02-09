---
name: "Somnath Banerjee"
affiliation: "Indian Institute of Technology Kharagpur (IIT Kharagpur)"
research_interests:
  - "AI Safety"
  - "LLM Safety Alignment"
  - "Decoding-Time Safety Methods"
  - "Explainable AI"
  - "Software Information Retrieval"
website: ""
google_scholar: "https://scholar.google.com/citations?hl=en&user=X5Zh5BwAAAAJ"
semantic_scholar: ""
researchgate: "https://www.researchgate.net/profile/Somnath-Banerjee-17"
---

# Somnath Banerjee

## Research Summary

Somnath Banerjee is a Research Scholar at the Indian Institute of Technology Kharagpur (IIT Kharagpur), India, working in the Department of Computer Science & Engineering. His research interests span LLM safety, explainable AI, AI safety, and software information retrieval, with 377+ citations.

His notable contribution is SafeInfer, published at AAAI 2025, which proposes a novel context-adaptive decoding-time safety alignment strategy for large language models. Unlike traditional approaches that rely on fine-tuning or training-time interventions, SafeInfer operates during inference, allowing flexible, context-adaptive safety controls without model retraining.

SafeInfer operates in two stages: (1) the safety amplification phase employs safe demonstration examples to adjust the model's hidden states and increase the likelihood of safer outputs, and (2) the safety-guided decoding phase applies safety-optimized distributions to guide token selection during generation, ensuring generated content complies with ethical guidelines.

The research addresses a critical challenge: safety-aligned language models often exhibit fragile and imbalanced safety mechanisms, increasing the likelihood of generating unsafe content. SafeInfer provides a more robust approach by shifting safety from training time to inference time, enabling dynamic adaptation to different contexts and risk levels.

Along with SafeInfer, the research introduces HarmEval, a novel benchmark for extensive safety evaluations designed to address potential misuse scenarios in accordance with the policies of leading AI companies. This work represents an important advancement in making AI safety more flexible and adaptable to real-world deployment scenarios.

## Papers in this Vault


- [[2025-Banerjee-SafeInfer|SafeInfer]] (First Author)

## Notes

Research emphasis on practical, deployment-ready safety mechanisms that can be applied at inference time rather than requiring expensive retraining, with potential applications for adapting safety levels to different regulatory contexts or user populations dynamically.
