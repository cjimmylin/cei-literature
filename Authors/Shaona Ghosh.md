---
name: "Shaona Ghosh"
affiliation: "NVIDIA"
research_interests:
  - "AI Content Safety"
  - "LLM Safety and Moderation"
  - "Adaptive AI Systems"
  - "Safety Taxonomy Development"
  - "Jailbreak Attack Robustness"
  - "Ensemble Learning for Safety"
website: ""
google_scholar: ""
semantic_scholar: ""
---

# Shaona Ghosh

## Research Summary

Shaona Ghosh is an AI researcher at NVIDIA (email: shaonag@nvidia.com) leading work on AI content safety and moderation systems. Her research focuses on developing comprehensive safety frameworks and datasets for large language models and generative AI systems.

Her notable contribution is AEGIS (Online Adaptive AI Content Safety Moderation with Ensemble of LLM Experts), published on arXiv in April 2024 with a follow-up AEGIS 2.0 at NAACL 2025. This work addresses the significant deficiency in high-quality content safety datasets that comprehensively cover critical safety areas.

AEGIS introduces a broad content safety risk taxonomy comprising 13 critical risk and 9 sparse risk categories. The team curated AEGISSAFETYDATASET, consisting of approximately 26,000 human-LLM interaction instances with human annotations. They instruction-tuned multiple LLM-based safety models called AEGISSAFETYEXPERTS, which surpass or perform competitively with state-of-the-art LLM-based safety models.

A key innovation is the AEGIS meta-algorithm that leverages an ensemble of specialist instruction-tuned safety experts and dynamically selects the most suitable expert for specific contexts using a no-regret online adaptation framework with strong theoretical guarantees. The models demonstrate robustness across multiple jailbreak attack categories while maintaining high performance on general capabilities (MT Bench scores).

The AEGIS dataset and models have been released to the research community through Hugging Face, including both permissive and defensive variants of the safety models, enabling broader research into content moderation systems.

## Papers in this Vault





- [[2026-Gupta-Language Caste and Context Demographic Disparities in AI-Generated|Language, Caste, and Context: Demographic Disparities in AI-Generated Explanations Across Indian and American STEM Educational Systems]] (Last Author)
- [[2025-Ghosh-AEGIS 2.0|AEGIS 2.0]] (First Author)
- [[2025-Group-AILuminate|AILuminate]] (First Author)
- [[2024-Ghosh-AEGIS|AEGIS]] (First Author)

## Notes





- *From 2025-Ghosh-AEGIS 2.0*:, Email: makeshn@nvidia.com
- *From 2025-Ghosh-AEGIS 2.0*:, Email: jibinv@nvidia.com
- *From 2025-Ghosh-AEGIS 2.0*:, Email: trebedea@nvidia.com
- *From 2024-Ghosh-AEGIS*:, Email: shaonag@nvidia.com
Research emphasizes scalable, adaptive approaches to AI safety that can handle diverse risk categories and evolving attack patterns. The work provides both theoretical frameworks and practical tools for content moderation at scale, with significant contributions to the open-source AI safety community.
