---
name: "Yiju Guo"
affiliation: "Renmin University of China / Tsinghua University"
research_interests:
  - "Multi-Objective AI Alignment"
  - "Preference Optimization"
  - "Controllable LLM Training"
  - "Helpfulness-Harmlessness-Honesty Trade-offs"
website: ""
google_scholar: ""
semantic_scholar: ""
---

# Yiju Guo

## Research Summary

Yiju Guo is a researcher affiliated with the Gaoling School of Artificial Intelligence at Renmin University of China, with connections to Tsinghua University's Department of Computer Science and Technology. His research focuses on addressing fundamental challenges in AI alignment, particularly the trade-offs between multiple alignment objectives.

His flagship work, Controllable Preference Optimization (CPO), tackles the "alignment tax"—a critical compromise where enhancements in alignment within one objective (e.g., harmlessness) can diminish performance in others (e.g., helpfulness). Unlike existing unidirectional alignment techniques that lead to sub-optimal trade-offs, CPO explicitly specifies preference scores for different objectives, thereby guiding the model to generate responses that meet varying requirements across the "3H" desiderata: helpfulness, honesty, and harmlessness.

The research, published at EMNLP 2024 in Miami, Florida, demonstrates that by introducing diverse data and alignment goals, CPO surpasses baseline methods in aligning with single objectives while mitigating the impact of the alignment tax and achieving improvements in multi-objective alignment. This work provides practitioners with tools to tune models for different trade-offs depending on the application context, offering crucial flexibility in deploying LLMs for diverse use cases.

The research was conducted in collaboration with Ganqu Cui, Lifan Yuan, Ning Ding, Zexu Sun, Bowen Sun, Huimin Chen, Ruobing Xie, Jie Zhou, Yankai Lin, Zhiyuan Liu, and Maosong Sun, and is supported by the OpenBMB project with code publicly available on GitHub.

## Papers in this Vault


- [[2024-Liu-Controllable Preference Optimization|Controllable Preference Optimization]] (First Author)

## Notes


- *From 2024-Liu-Controllable Preference Optimization*: Affiliation: lable Preference Optimization - PDF Extract", Email: cgq22@mails.tsinghua.edu.cn
The CPO paper has received 3 citations as of August 2025. The work addresses a critical practical challenge in LLM deployment: how to balance multiple alignment objectives without sacrificing performance in any single dimension. Code available at https://github.com/OpenBMB/CPO.
