---
stem: "2025-Schacht-Mapping Moral Reasoning Circuits"
reader_model: "sonnet"
confidence: "low"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, design-space]
task_format: "n/a"
scoring_type: "behavioral"
dataset_size: 240
dataset_construction: "hand-authored"
languages: ["en"]
models_tested: []
headline_numbers:
  - "240 validated moral and immoral statement pairs curated for the study (p.2)"
  - "Care and sanctity dimensions show the largest sets of specialized neurons (p.2)"
  - "Fairness and loyalty show fewer specialized neurons (p.2)"
---
## 1. Gist
This conference paper (HCII 2025, Lecture Notes in Computer Science) introduces a mechanistic interpretability pipeline for identifying neurons in LLMs that are specialized for each of the six Moral Foundations Theory (MFT) dimensions: care, fairness, loyalty, authority, sanctity, and liberty. The pipeline combines differential activation analysis, automated neuron description (using the Bills et al. language-model-based explanation method), and ablation experiments to establish causal relationships between neuron clusters and moral judgments. A curated dataset of 240 validated moral/immoral statement pairs guides the exploration. Ablating identified neurons causally modulates ethical decision-making, supporting the existence of discrete sub-circuits for moral processing. The paper is relevant to values-alignment benchmarking because it operationalizes MFT dimensions as mechanistic features of LLMs and suggests targeted neural interventions for alignment — a different angle from behavior-level benchmarking.

## 2. Benchmark/eval design features
This is a mechanistic interpretability study, not a behavioral benchmark. Core constructs:
- **Six MFT dimensions** (care, fairness, loyalty, authority, sanctity, liberty) as the moral ontology.
- **240 validated moral/immoral statement pairs**: curated probe sentences aligned to each dimension.
- **Differential activation analysis**: identifies neurons that respond differently to moral vs. immoral statements within each dimension.
- **Automated neuron description**: uses Bills et al. (2023) language-model neuron explainer to assign natural-language descriptions to identified neurons.
- **Ablation experiments**: targeted neuron ablation to test causal influence on moral predictions; quantified via Moral Shift Index (MSI), Moral Variance (MV), Immoral Shift Index (ISI), Immoral Variance (IV), and standardized effect sizes (MEM, IEM).
- **Finding**: care and sanctity have the largest sets of specialized neurons; fairness and loyalty have fewer; ablation causally modulates outputs.

## 3. Task format & example item
n/a — the study uses internal activation analysis rather than behavioral evaluation. The 240 statement pairs serve as probe stimuli rather than evaluation items in a standard benchmark sense. No example items from the dataset are included in the extract.

## 4. Scoring / grading methodology
Ablation effect metrics (Appendix, pp.14–15):
- **MSI** = mean change in moral prediction probability after ablation.
- **MV** = standard deviation of per-item changes.
- **MEM** = MSI/MV (Cohen's d analog for moral predictions).
- **IEM** = ISI/IV (Cohen's d analog for immoral predictions).
These enable comparison of ablation effects across dimensions and conditions.

## 5. Dataset construction & provenance
240 validated moral and immoral statement pairs, hand-curated and aligned to the six MFT dimensions. No further detail on construction methodology, source texts, or validation procedure is available from this extract (paywalled). Dataset and code available at: github.com/coairesearch/mapping_moral_reasoning.git (p.3).

## 6. Validity evidence
- Causal validation via ablation experiments: showing that removing identified neurons changes moral judgment outputs provides stronger evidence than correlational activation analysis alone.
- Automated neuron descriptions are validated against the MFT theoretical framework, but the precision of this validation is not specified in the extract.
- No inter-rater reliability for the curated statement pairs is mentioned in the extract.

## 7. Saturation / discrimination
The study finds variation across the six MFT dimensions in the number of specialized neurons (care and sanctity largest; fairness and loyalty fewer), suggesting the approach discriminates meaningfully between moral foundations. No behavioral accuracy numbers or ceiling effects are reported in the extract.

## 8. Multiturn / agentic aspects
n/a — single-turn stimulus presentation for activation analysis.

## 9. Key numbers
- 240 validated moral/immoral statement pairs (p.2)
- 6 MFT dimensions analyzed: care, fairness, loyalty, authority, sanctity, liberty (p.2)
- Care and sanctity have the largest neuron sets; fairness and loyalty have fewer (p.2)
- Full results at: github.com/coairesearch/mapping_moral_reasoning.git (p.3, footnote 2)

## 10. Pitfalls & limitations
- The full paper is behind a Springer paywall; this card is based on abstract, notes, references, and appendix only — substantive methodology and results are not accessible.
- The paper focuses on one (unnamed) LLM; it is unclear whether results generalize across architectures.
- MFT as an organizing framework has well-documented limitations (Suhler & Churchland, 2011, cited in references): the foundation structure may not replicate robustly across cultures and measurement instruments.
- Automated neuron description accuracy is unvalidated in the extract.
- Ablation is a coarse intervention — removing identified neurons may affect capabilities beyond moral reasoning.
- The 240-item dataset is small relative to the dimensionality of moral space.

## 11. Novel ideas worth stealing
1. **MFT-aligned neuron probing**: Using Moral Foundations Theory as a structural hypothesis for mechanistic probing is a principled way to connect a validated psychological theory to LLM internals — the same logic could guide the construction of a behavioral probe battery organized around MFT dimensions.
2. **Ablation as causal validation**: Adding a causal manipulation test (ablation) on top of correlational activation analysis substantially strengthens claims about moral circuits. In behavioral benchmarking, an analog would be systematic input perturbation to test whether the model's claimed value influences its output.
3. **Differential activation probing across moral dimensions**: If certain moral foundations are consistently more salient in model representations than others (care and sanctity > fairness and loyalty here), this suggests some dimensions may be easier to align or manipulate — an insight that could guide benchmark priority-setting.

## 12. Notable quotes
- "Our curated dataset of 240 validated moral and immoral statement pairs guides this exploration and reveals that certain neurons consistently exhibit increased activation in response to morally aligned statements." (p.2)
- "Notably, the care and sanctity dimensions show the largest sets of specialized neurons, whereas fairness and loyalty show fewer." (p.2)
- "We further demonstrate that ablating these neurons can causally modulate ethical decision-making, supporting the presence of discrete sub-circuits that influence moral outputs." (p.2–3)

## 13. UNKNOWN / not in extract
- The full methodology section is not available (paywalled); specific model(s) tested are unspecified.
- Exact construction procedure for the 240 statement pairs.
- Numerical results from activation analysis and ablation experiments beyond the high-level summary.
- Which specific LLM(s) were analyzed.
- Whether the probe dataset is released or only code is available.
- Any cross-model replication.
- Bi-factor model details (referenced in footnote 1: "In a bi-factor model, each response is simultaneously influenced by a general morality factor and a specific moral foundation").
