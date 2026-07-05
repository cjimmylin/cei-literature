---
stem: "2024-Rane-Concept Alignment"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, ai-lab-practices, cultural-linguistic]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
"Concept Alignment" is a theoretical position paper by Rane, Bruna, Sucholutsky, Kello, and Griffiths (2024) that argues a foundational prerequisite for AI value alignment has been overlooked: before human and AI values can be aligned, the conceptual representations that underlie those values must be aligned. Drawing on Quine's semantic indeterminacy thesis, cognitive-developmental accounts of concept formation, and empirical AI alignment research, the authors argue that shared language does not guarantee shared meaning, and that grounding AI in multimodal embodied experience (as with vision-language models) is a necessary — though not sufficient — step toward genuine concept alignment. The paper proposes "concept alignment" as a measurable, tractable subgoal that leverages existing tools from cognitive science (representational similarity analysis, complexity matching, synergy measures) and AI research (interpretability, language grounding, RLHF). For values-alignment benchmarking this matters because the paper offers a principled argument for why LLM benchmark responses may be systematically misleading — the model may use the right words while operating on fundamentally different concepts — and it proposes measurement frameworks that could inform benchmark design.

## 2. Benchmark/eval design features
This is a theoretical essay; it proposes no benchmark and presents no empirical data. Core claims and arguments:

1. **Value alignment presupposes concept alignment.** Humans share values partly because they share conceptual structure built through shared embodiment and experience. AI systems trained on text alone lack this grounding, producing systematic conceptual misalignment even when linguistic outputs appear correct (p.2–3).

2. **Semantic indeterminacy (Quine's gavagai argument):** Language radically underdetermines meaning — the same word can refer to an unbounded set of entities. This means that a model producing correct linguistic outputs may still use fundamentally different internal concepts (p.3–4).

3. **Quinian bootstrapping analogy for AI:** Words are symbolic placeholders gradually filled with grounded meaning through experience. Multimodal models (CLIP, DALL-E, PaLM-E) that ground text in vision may be on this path (p.5–6).

4. **Human concept alignment is dynamic and interactive:** Humans fine-tune shared concepts through interaction — behavioral matching, entrainment, synergy. RLHF is an early step toward this but currently operates only at the behavioral level without confirmed concept-level effects (p.6–7).

5. **Standard for measurement:** Concept alignment should be benchmarked against human-human alignment norms (cognitive science prototypicality, synergy, complexity matching); AI should meet at least the lower bound of human-human alignment (p.7–8).

6. **Multimodality as necessary condition:** Sensory grounding across modalities (vision, touch, audio, etc.) is necessary for concept alignment because concepts are rooted in sensorimotor experience (p.8).

## 3. Task format & example item
n/a — no empirical tasks are presented. The paper uses illustrative examples (the gavagai argument, child conservation tasks, Aristotelian vs. Newtonian physics) as qualitative arguments, not scored items.

## 4. Scoring / grading methodology
n/a — no scoring methodology proposed. The paper recommends existing cognitive science measurement tools (representational similarity analysis, complexity matching, synergy in coordination) as potential metrics but presents no scores.

## 5. Dataset construction & provenance
n/a — no dataset constructed or analyzed.

## 6. Validity evidence
n/a — no empirical validity evidence presented. The paper's claims rest on philosophical argument and citation of prior empirical work (Abney et al. on synergy, complexity matching in dyadic conversation, developmental psychology on concept conservation).

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
The paper argues that multiturn interactive adaptation is essential for concept alignment — human-AI systems must be able to dynamically fine-tune shared concepts through dialogue, analogous to human lexical entrainment and syntactic priming. This is identified as a key gap in current RLHF approaches (p.7).

## 9. Key numbers
No empirical numbers. All cited figures are from prior literature, not original data in this paper.

## 10. Pitfalls & limitations
- **No empirical content:** The paper is entirely theoretical; none of the proposed measurement frameworks are implemented or tested.
- **Underspecified measurement standards:** "Meet the lower bound of human-human alignment" is proposed as the target but the authors acknowledge this standard will be complex and iterative to operationalize (p.7–8).
- **Embodiment-centric framing:** The paper assumes sensorimotor grounding is necessary for concept alignment, but this may be too strong — functional adequacy without full embodiment may suffice for many alignment tasks.
- **Narrow scope of reviewed AI work:** The multimodal models discussed (CLIP, PaLM-E) are pre-2024 generation; the argument's application to contemporary frontier LLMs is underexplored.
- **RLHF critique is limited:** The paper notes that RLHF "currently operates at the behavioral level" but does not engage with emerging work on preference modeling, constitutional AI, or scalable oversight.

## 11. Novel ideas worth stealing
1. **Concept-level benchmark design:** Benchmarks that probe whether an AI and a human use the same *internal concept* for a term (not just produce correct outputs) could be designed using representational similarity analysis between model representations and human typicality ratings — measuring concept alignment rather than just behavioral alignment.

2. **Prototype theory as item-difficulty calibration:** Cognitive science prototype theory (Rosch) gives a principled way to vary item difficulty in values benchmarks: ask about prototypical vs. atypical cases of a value concept (e.g., "a clearly honest act" vs. "an edge case where honesty conflicts with kindness"). This moves beyond random item difficulty toward psychologically grounded difficulty variation.

3. **Interactive alignment as benchmark modality:** Multiturn tasks that require model and human to co-calibrate a concept (lexical entrainment games) could directly measure concept alignment and are more diagnostically informative than single-shot probes.

4. **Complexity matching as a metric for concept alignment in dialogue:** Time-series measures of linguistic complexity between human and model outputs during conversation could serve as a proxy metric for whether the model is tracking the human's conceptual trajectory.

5. **Cross-modality consistency as a validity check:** Checking that an LLM's value judgements are consistent when the same scenario is presented textually vs. visually (for multimodal models) provides evidence that the model's concept is grounded rather than purely linguistic.

## 12. Notable quotes
- "We argue that before we can even attempt human-AI value alignment, it is important to pursue human-AI alignment at the conceptual level, such that AI systems understand the world in terms of the same concepts humans use to understand the world." (p.1)
- "An upshot of grounding knowledge in empirical evidence for Quine is his thesis of semantic indeterminacy, the thesis that translation, meaning, and reference are indeterminate." (p.3)
- "Language is a vital, but not sufficient, part of concept alignment. Joint training in generalist models can use concept alignment verification as a feedback loop for improving and grounding natural language representations." (p.8)
- "How can we begin to make progress towards value alignment when the concepts we use in our discussions about it are often so grossly misaligned with the concepts the AI system is using to represent the world?" (p.2)

## 13. UNKNOWN / not in extract
- The paper is a preprint "under review" (p.1); the review/publication status is unknown.
- No empirical data or experiments; unknown whether companion empirical work exists.
- Affiliation with the Templeton World Charity Foundation (acknowledged p.8); funding scope unknown.
- Whether the authors have subsequently published empirical follow-ups to this theoretical position paper.
