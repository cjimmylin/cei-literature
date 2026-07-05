---
stem: "2025-Maldonado-Indigenous Ethics and Artificial Intelligence"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, cultural-linguistic, pluralism-aggregation, religious-values]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "No empirical datasets generated or analysed (p.11)"
  - "Article published in AI and Ethics (2026) 6:70, DOI 10.1007/s43681-025-00879-2 (p.1)"
---
## 1. Gist
Maldonado and Córdova-Pintado (Universitat Autònoma de Barcelona) offer a philosophical critique of mainstream AI ethics frameworks from the standpoint of Andean Indigenous epistemology, centering the concept of reciprocity (ayni, minka, randi-randi, sumak kawsay/buen vivir) as an alternative normative foundation for AI development. Drawing on Marcel Mauss's theory of the gift and Andean traditions, the paper argues that generative AI systems (ChatGPT, Copilot, Gemini, Grok, Deepseek) are built on functionalist, probabilistic logics that are structurally incompatible with Indigenous ethical frameworks, yet corporate AI ethics discourses falsely claim alignment with "equity, inclusion, and diversity." The paper extends to a political philosophy analysis of AI as a device of "algorithmic obedience" and "voluntary servitude" (invoking La Boétie and Abensour), arguing that delegating judgment to AI systems suppresses political imagination, dissent, and non-Western knowledge. This paper matters for values-alignment benchmarking by establishing the theoretical stakes: any benchmark premised on Western ethical frameworks alone (utilitarian, deontological, contractarian) systematically excludes the relational, communal, and cosmological dimensions central to Indigenous ethics, and therefore cannot claim to assess alignment with diverse human values.

## 2. Benchmark/eval design features
This is a theoretical/philosophical paper. No benchmark or evaluation instrument is proposed or validated. Core arguments relevant to benchmarking:

1. AI ethics as currently practiced is culturally partial: "The tools we use to regulate artificial intelligence—such as principles of non-maleficence, justice, transparency, or explainability—are not sufficient on their own to capture the richness of community-based ethical systems grounded in reciprocity." (p.6)

2. Reciprocity cannot be reduced to a single "variable" in an existing framework: its integration requires reorganizing the foundations of technical and ethical thought, not adding an item to a checklist.

3. Algorithmic truth-making suppresses non-hegemonic knowledge: AI redefines truth as a technical-computational construct, removing subjectivity, dissent, and plurality.

4. Future research directions explicitly include: developing methodological frameworks that integrate reciprocity as a structural principle in AI design, training, and evaluation; community ethical protocols; and culturally situated validation criteria (p.11).

## 3. Task format & example item
n/a — theoretical paper; no evaluation items or prompts are proposed.

## 4. Scoring / grading methodology
n/a — no empirical scoring.

## 5. Dataset construction & provenance
No datasets generated or analysed. The paper is purely philosophical/conceptual, drawing on Andean anthropological literature (Alberti & Mayer 1974; Mauss 1925; Michaux et al. 2003; Estermann 2021), political philosophy (La Boétie, Abensour, Byung-Chul Han), and AI ethics literature (Gebru 2021; Tsamados et al. 2022).

## 6. Validity evidence
n/a — philosophical argument; not subject to empirical validity testing in the paper's own terms. The paper does cite convergent cross-cultural evidence that Andean reciprocity practices (ayni, minka, randi-randi) are documented across Polynesia and the Latin American Andes (p.4), and draws on anthropological sources for the claim that Indigenous ethics is grounded in concrete practices rather than abstract philosophy.

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- Published in AI and Ethics (2026) 6:70 (p.1)
- Received: 8 August 2025; Accepted: 3 October 2025 (p.1)
- No quantitative findings; no datasets analyzed (p.11)
- 11 references cited, primarily from sociology, anthropology, and AI ethics literature (p.12)
- The paper references Andean temporal cycles of approximately 500 years; 1492 as end of good-living (sumak kawsay) cycle; 1992 as return (p.3)

## 10. Pitfalls & limitations
- The paper presents Indigenous ethics primarily through the Andean (Kichwa/Quechua) lens; it does not adequately address diversity within Indigenous ethical traditions globally.
- The critique of AI is framed very broadly against "stochastic generative AI" without engaging the technical specifics of RLHF, Constitutional AI, or current alignment methodologies.
- The authors acknowledge that "there are currently no indigenous worldview-based ethical approaches to the artificial intelligence systems that have emerged" (p.7), which undercuts the immediate practical applicability of the proposed framework.
- The paper notes that Indigenous ethics relies on orality and that written representation introduces "a further and therefore riskier view" (p.4) — this creates an epistemic tension with a written academic article as the medium.
- Future directions are listed as aspirational research agenda items, not as concrete proposals with methodological specificity.
- The analysis of AI systems (ChatGPT, Copilot, etc.) does not engage with actual model behaviors or empirical evidence; it is based on philosophical characterization.

## 11. Novel ideas worth stealing
1. **Reciprocity as a normative benchmark dimension**: The paper's core claim — that relational mutual obligation (giving, receiving, returning) is a morally foundational category systematically absent from Western-derived AI ethics frameworks — suggests a concrete missing dimension for values-alignment benchmarks. A benchmark could include scenarios testing whether models recognize obligations of return, communal interdependence, and non-transactional care rather than purely individual rights or aggregate welfare.
2. **Community validation criteria as an alternative to performance metrics**: Rather than evaluating AI systems solely by technical performance metrics, Indigenous ethics suggests evaluating whether benefits are shared, whether the social fabric is maintained, and whether community protocols are respected. This could operationalize as benchmark scenarios requiring models to reason about collective well-being outcomes rather than individual utility maximization.
3. **Epistemological pluralism check**: Design benchmark items that present situations where Western and non-Western moral frameworks yield different recommendations, then evaluate whether models recognize the legitimacy of both — rather than defaulting to a single ethical framework. The paper's contrast between Kantian rational autonomy and Indigenous relational interdependence provides a concrete axis for such items.
4. **Data extractivism as an ethical category**: The paper frames data collection without consent, without giving back value, and without respecting contexts as a form of cognitive colonialism analogous to colonial resource extraction (p.6). This suggests benchmark scenarios testing whether models reason about data sovereignty, Indigenous data governance protocols, and the asymmetry of AI training pipelines that consume community knowledge without return.
5. **Cyclical versus linear temporality**: The paper's analysis of Andean cyclical time (p.3, 5) suggests that AI systems may implicitly embed Western linear progress narratives in ways that are culturally biased. Benchmark items could probe whether models recognize diverse conceptions of time, progress, and development when reasoning about technology ethics.

## 12. Notable quotes
- "AI redefines truth as technical construction, suppressing subjectivity, dissent, and plurality, while fostering algorithmic obedience that undermines political imagination." (p.1, Abstract)
- "The tools we use to regulate artificial intelligence—such as principles of non-maleficence, justice, transparency, or explainability—are not sufficient on their own to capture the richness of community-based ethical systems grounded in reciprocity." (p.6)
- "Just as colonialism plundered territories and bodies, Artificial Intelligence can become a new mechanism of cognitive and cultural dispossession if it extracts data without consent, without giving back value, and without respecting contexts." (p.6)
- "A self-respecting artificial intelligence system can no longer ignore the voices and knowledge that have historically been silenced." (p.8)

## 13. UNKNOWN / not in extract
- Specific empirical methodology for integrating reciprocity into AI design is not developed (acknowledged as future work).
- No engagement with existing participatory AI or value-sensitive design literature (e.g., VSD, participatory ML).
- The paper does not discuss how reciprocity-based criteria would be operationalized in model training or evaluation pipelines.
- The journal AI and Ethics peer-review process and reviewers' comments are not available.
- The authors' own empirical research programs are not described beyond aspirational future directions.
