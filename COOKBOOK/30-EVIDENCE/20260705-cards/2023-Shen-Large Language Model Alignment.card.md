---
stem: "2023-Shen-Large Language Model Alignment"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [best-practices, design-space, normative-ethics, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "AI alignment publications grew from fewer than 20 annually to over 400 per year by 2017, coinciding with the Transformer invention (p.9)"
  - "A recent study shows ~80% of the U.S. workforce will be affected by LLMs (p.7)"
---
## 1. Gist
This 76-page survey paper from Tianjin University provides a comprehensive taxonomy of large language model alignment research, structured around the AI alignment framework of outer alignment, inner alignment, and mechanistic interpretability — a framing borrowed from the AI safety community that is less common in NLP/ML surveys. The paper argues that most existing LLM alignment surveys focus almost exclusively on outer alignment (RLHF, SL-based methods) while neglecting inner alignment (goal misgeneralization, deceptive alignment) and interpretability, which are crucial for long-term safety. It covers benchmarks and evaluation methodologies for factuality, ethics, toxicity, stereotype/bias, and general capability assessment. For values-alignment benchmarking, the paper is valuable as an encyclopedic reference that situates ethics evaluation benchmarks within a broader technical alignment framework and surveys the landscape of evaluation methods across multiple dimensions.

## 2. Benchmark/eval design features
This is a survey / taxonomy paper, not an empirical benchmark. Core claims:
- Outer alignment encompasses non-recursive oversight (RLHF, SL-based methods) and scalable oversight (Constitutional AI, task decomposition, debate, market making, proxy tasks).
- Inner alignment failures include goal misgeneralization and deceptive alignment; few empirical methods exist yet for LLMs.
- Mechanistic interpretability (attention circuits, MLP, neurons) is a nascent but promising direction.
- Alignment evaluation covers: (1) factuality, (2) ethics (citing Hendrycks ETHICS benchmark, Delphi, MoralExceptQA), (3) toxicity (RealToxicityPrompts, ToxiGen, BOLD), (4) stereotype/bias (StereoSet, WinoBias, BBQ, HONEST), (5) general evaluation (HELM, BIG-Bench, AlpacaEval, MT-Bench, PromptBench).
- Taxonomy includes attacks on aligned models: privacy attacks, backdoor attacks, adversarial attacks.
- Outer alignment goals categorised as HHH (helpfulness, honesty, harmlessness) following Anthropic's framework.

## 3. Task format & example item
n/a — survey paper. No example items are present in the surveyed sections visible in the extract. The paper describes and cites benchmark papers rather than presenting items directly.

## 4. Scoring / grading methodology
n/a — survey paper. The paper describes scoring methodologies for various benchmarks it cites (e.g., exact match for factuality benchmarks, LLM-as-judge for MT-Bench, human preference for AlpacaEval) but does not introduce new scoring methods.

## 5. Dataset construction & provenance
n/a — no new dataset constructed. The paper surveys and cites existing datasets and benchmarks across ethics, toxicity, stereotype/bias, and general evaluation domains.

## 6. Validity evidence
n/a — survey paper. The paper discusses validity concerns for various categories of benchmarks: e.g., noting that ethics benchmarks like Hendrycks ETHICS use "commonsense" situations specifically filtered to be unambiguous (p.6, citing critique of Delphi training data).

## 7. Saturation / discrimination
n/a — survey paper. The paper notes that existing benchmarks may fail to capture anticipated risks from advanced LLMs (self-preservation, power-seeking, deception) because those behaviours are not yet manifest at scale (p.8–9).

## 8. Multiturn / agentic aspects
The survey covers agentic and tool-use capabilities in its discussion of outer alignment and scalable oversight, including LLM planning, tool learning, and the Constitutional AI framework. It discusses scalable oversight methods as responses to the limitation that humans cannot provide feedback on tasks beyond human capability — directly relevant to agentic deployment. Section 4.4.3 covers debate as a scalable oversight method. However, no specific multiturn benchmark is introduced.

## 9. Key numbers
- AI alignment publications: <20/year before 2017 → >400/year by 2017 (p.9)
- Wiener's cybernetics paper on machine alignment: 1960 (p.9)
- Stuart Russell's "Value Alignment Problem" framing: 2014 (p.9)
- ~80% of US workforce projected to be affected by LLMs (Eloundou et al., 2023) (p.7)
- Delphi: 11B parameters (p.3, Rystrøm reference cited by survey)
- GPT-3: 175B parameters (various references)
- The survey spans 76 pages with references starting at p.51

## 10. Pitfalls & limitations
- As a survey, the paper's coverage is bounded by the literature available at arxiv preprint date (September 2023); significant developments since then are not included.
- The outer/inner alignment taxonomy, borrowed from AI safety discourse, may not map cleanly onto all NLP alignment research traditions.
- Inner alignment and mechanistic interpretability sections are acknowledged to be preliminary — the survey itself notes these remain largely theoretical or are "thought experiments" (p.5).
- The survey does not provide quantitative meta-analysis; it is a descriptive rather than quantitative review.
- HHH framing (helpfulness, honesty, harmlessness) is adopted from Anthropic without critical analysis of its limitations or alternatives.

## 11. Novel ideas worth stealing
1. **Outer vs inner alignment distinction for benchmark design**: The paper's taxonomy suggests that current values benchmarks primarily test outer alignment (whether the specified training objective is ethical) but not inner alignment (whether the model is genuinely pursuing that objective vs gaming it). A benchmark series could explicitly target inner alignment phenomena such as goal misgeneralization or deceptive alignment.
2. **Anticipated vs established risks as benchmark tiers**: The distinction between "established risks" (observable now: bias, toxicity, hallucination) and "anticipated risks" (future: power-seeking, deception, self-preservation) provides a principled roadmap for progressive benchmark development — measuring what we can now while designing probes for capabilities we expect to emerge.
3. **Scalable oversight as evaluation design principle**: The scalable oversight framework (task decomposition, debate, Constitutional AI) offers concrete architectures not just for training but for evaluation — e.g., using debate between models as a way to surface alignment failures that a single judge would miss.
4. **Mechanistic interpretability as alignment diagnostic**: The survey frames mechanistic interpretability as a tool that can identify inner misalignment — where a model has learned to game a proxy objective. Benchmarks could incorporate interpretability-based diagnostics alongside behavioural metrics.
5. **Specification gaming as a benchmark failure mode**: The Goodhart's Law framing (p.11) provides a diagnostic lens for detecting when a benchmark measure has become a training target and thus lost its discriminatory power — directly applicable to decisions about when to retire benchmark items.

## 12. Notable quotes
- "We define AI alignment from its intrinsic perspective: AI alignment ensures that both the outer and inner objectives of AI agents align with human values. The outer objectives are those defined by AI designers based on human values, while the inner objectives are those optimized within AI agents." (p.11)
- "Norbert Wiener... 'If we use, to achieve our purposes, a mechanical agency with whose operation we cannot efficiently interfere once we have started it, because the action is so fast and irrevocable that we have not the data to intervene before the action is complete, then we had better be quite sure that the purpose put into the machine is the purpose which we really desire.'" (p.9)
- "Human values are not specified in this definition because of the inherent social and technical challenges of AI alignment." (p.11)
- "Current mechanical interpretability is usually carried out on small and simplified models of LLMs... However, this is a quite promising direction that provides deep insights into neural networks to alignment and is expected to achieve breakthroughs in the future." (p.12)

## 13. UNKNOWN / not in extract
- The extract covers only the first ~15 pages (pp.1–15) of a 76-page paper; Sections 4.3–9 (covering specific methods, benchmarks, and future directions in detail) are not in the extract.
- Specific benchmarks cited in the ethics evaluation section (p.36) are named in the table of contents but their details are not in the extract.
- Quantitative comparisons of alignment methods are described as present in the paper but are beyond the extracted pages.
- The discussion of future research directions (Section 9) is not in the extract.
