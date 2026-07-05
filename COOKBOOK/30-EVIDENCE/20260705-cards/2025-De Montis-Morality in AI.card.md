---
stem: "2025-De Montis-Morality in AI"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, design-space, pluralism-aggregation]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Commonsense Norm Bank: 1.7 million descriptive judgments on everyday situations (referenced, p.2)"
  - "Proposed Loving Attention Vectors (LAVs) derived from 4 normative-descriptive word pairs from Murdoch (p.15)"
---
## 1. Gist
This work-in-progress paper by Bombaerts, Delisse, and Kaymak (Eindhoven University of Technology / Dembrane, 2025) is a philosophical-technical proposal for embedding morality directly into LLM architectures and frameworks through "morality-by-design" principles, rather than relying solely on post-hoc RLHF or static rule-based constraints. The central argument draws on Iris Murdoch's moral philosophy of "loving attention"—sustained, just observation that enables moral transformation—to propose concrete computational operationalizations: Loving Attention Vectors (LAVs) in embedding space, modifications to attention's query/key/value matrices to detect and weight moral salience, and moral gradient descent via RLHF-style reward models. The paper also develops a System Attention Framework grounded in Posner's attention network theory and Luhmann's systems theory. For values-alignment benchmarking, the paper is theoretically important: it argues that current benchmark approaches (like Delphi/Commonsense Norm Bank) rely on static rule-based inputs that miss the dynamic, systemic nature of moral processing, and proposes that moral evaluation frameworks should measure attentional reinterpretation capacity, context-sensitive moral salience, and moral consistency across diverse framings.

## 2. Benchmark/eval design features
Not an empirical benchmark paper. Core theoretical contributions:
1. **System Attention Framework**: six-element model (structure, attention, alerting/awareness, orienting/focus, executing/decision, learning) applied both to cognitive processing and moral processing in LLMs, grounded in Posner's attention networks and Luhmann's systems theory.
2. **Murdoch's Loving Attention as computational target**: operationalized via (a) Loving Attention Vectors (LAVs) in embedding space encoding moral reinterpretations (e.g., "vulgar" → "refreshingly simple"); (b) morally-tuned Q/K/V matrices; (c) moral loss functions in RLHF.
3. **Critique of static approaches**: argues Delphi (Commonsense Norm Bank, 1.7M judgments) and Constitutional AI are insufficient because they use static rule-based inputs, missing dynamic and systemic moral processing.
4. **Table 1 framework**: a systematic comparison of LLM cognitive processing / biological moral processing (Murdoch) / LLM moral processing as-is / potential improvements, organized by six system attention framework components.

## 3. Task format & example item
n/a — theoretical/philosophical paper. No empirical items or evaluation tasks presented. The closest analog is a worked example from Murdoch's mother-in-law (M) and daughter-in-law (D) narrative: M reinterprets D from "vulgar, undignified, noisy, bumptious, tiresome juvenile" to "refreshingly simple, spontaneous, gay, delightfully youthful." This is used to derive LAVs:
LAV_noisy-gay = embedding("gay") – embedding("noisy"); LAV_love = MEAN(4 such vectors). (p.15-16)

## 4. Scoring / grading methodology
n/a — no empirical scoring. The paper acknowledges at length (Discussion, pp.23-26) that "traditional metrics of accuracy and alignment may prove insufficient for assessing morally-oriented AI systems" and that the framework "provides no clear methodology for validating moral improvements or preventing the introduction of new biases through moral fine-tuning."

## 5. Dataset construction & provenance
n/a — no dataset. References existing work: Commonsense Norm Bank (1.7M judgments in Delphi), Moral Foundations Theory (Graham et al., Haidt), MoralStrength lexicon (Araque et al.), and Teitelbaum & Simchon's semantic projection work on embedding spaces. The Delisse (2024) master's thesis at TU Eindhoven is cited as empirical groundwork for the LAV approach.

## 6. Validity evidence
No empirical validation. The paper explicitly describes itself as "work-in-progress" and "exploratory." Authors acknowledge: (1) the functional analogy between human and LLM attention is metaphorical rather than ontological; (2) the framework lacks empirical validation; (3) the six-element attention structure collapses Posner's empirically distinct alerting/orienting/executive networks in ways that "may lose important distinctions"; (4) the LAV operationalization "risks transforming a profound moral practice into mere stylistic preference adjustment." Graves (2025) and Delisse (2024) are cited as limited preliminary empirical support for the attention-morality connection.

## 7. Saturation / discrimination
n/a — no empirical data. However, the paper implicitly identifies a discrimination problem for current benchmarks: static rule-based approaches (Delphi, Constitutional AI) cannot measure dynamic moral reinterpretation capacity or context-sensitive moral growth, creating a gap that architectural/framework approaches might address.

## 8. Multiturn / agentic aspects
Not empirically addressed, but the paper's concept of "moral learning" through iterative attention and the proposed multi-agent environment for training are directly relevant to multi-turn/agentic moral evaluation. Specifically: "embedding models in multi-agent environments and training them with diverse, conflicting value systems to reflect real-world moral complexity" (p.2); "reflection layers and recursive feedback loops can simulate deliberation and enable re-evaluation of prior decisions" (p.2).

## 9. Key numbers
- Commonsense Norm Bank: 1.7 million descriptive judgments (referenced, p.2)
- Moral Foundations Theory: 6 modular foundations in human moral reasoning (p.15)
- LAVs derived from 4 normative-descriptive word pairs from Murdoch's mother-in-law example (p.15-16)
- Paper runs 32 pages including references; 6 sections + appendix-level reference list
- Delisse (2024) master's thesis: experimented with updating normative descriptive word associations toward Murdochian loving attention (cited p.3)
- Graves (2025): "moral attention can extend computational attention mechanisms to attend to the moral dimension of human experience" (cited p.3)

## 10. Pitfalls & limitations
Authors acknowledge extensively (pp.23-26):
- The framework is metaphorical and functional, not ontological; functional analogies between human and AI attention may be superficial.
- LAV operationalization risks "reducing a profound moral practice to stylistic preference adjustment."
- No empirical validation of whether LAVs produce genuine moral sensitivity or surface-level linguistic changes.
- Murdoch's theory focuses on individual internal transformation, not collective moral norms—hard to generalize across cultures and contexts.
- "The approach assumes that moral salience can be reliably detected and encoded in embedding spaces, overlooking the contested and culturally variable nature of moral judgment."
- The six-element framework collapses Posner's empirically distinct attention networks.
- No methodology for validating moral improvements or preventing new biases.
- Fundamental challenge: translating first-person moral experience into third-person computational processing; AI lacks consciousness, lived experience, and "unselfing."
- Power concern: "do we want current big-tech companies being able to control our morality?" (p.26).

## 11. Novel ideas worth stealing
1. **Loving Attention Vectors (LAVs) as a benchmark construct**: the proposal to construct anchored difference vectors capturing moral reinterpretations (dismissive → generous, stereotyping → attentive) could be operationalized as a benchmark task. Pairs of morally equivalent but differently valenced descriptions could test whether models preferentially reframe toward more generous interpretations.
2. **Moral geometry of embedding spaces as a measurement target**: the paper synthesizes evidence (Fitz 2023, Leshinskaya et al. 2023, Abdulhai et al. 2023) that embedding spaces contain latent moral dimensions. A benchmark could use semantic projection to measure how morally attuned a model's embedding space is.
3. **Morality-by-design as a benchmark axis**: instead of only measuring model outputs, benchmarks could measure architectural features—does the model's attention mechanism differentially weight morally salient tokens? Can LAV-like transformations be induced?
4. **ENGAGE mode / moral facilitation over moral arbitration**: the paper's argument that "embedding moral sensitivity need not require embedding moral conclusions—architectures could enhance moral reasoning capacity while preserving moral agency" (p.26) suggests a benchmark dimension: does the model present multiple moral perspectives or impose a single framework?
5. **Dynamic moral reinterpretation as an evaluation target**: does the model revise its moral assessment of a person/situation when presented with additional context in later turns? This is a multiturn benchmark design directly motivated by Murdoch's "let me look again" orienting step.
6. **RLHF reward decomposition for moral dimensions**: decomposing rewards into attentional quality, generous reinterpretation, and contextual appropriateness components is a concrete methodology for training moral values rather than just harmlessness.

## 12. Notable quotes
- "Moral processing should be regarded as a constitutive aspect of artificial intelligence itself, requiring an architectural commitment to embedding ethical reasoning within the fabric of model design, rather than appending it as a post hoc constraint or filter alone." (p.27)
- "LLMs could—and should—generate multiple moral perspectives, presenting competing moral frameworks transparently rather than privileging one view." (p.26)
- "The key insight is that embedding moral sensitivity need not require embedding moral conclusions—architectures could enhance moral reasoning capacity while preserving moral agency and democratic contestation." (p.26)
- "Machine learning becomes moral learning—when perception, representation, and responsibility align." (p.21)

## 13. UNKNOWN / not in extract
- Details of the Delisse (2024) master's thesis experiments (only briefly summarized in main text).
- Whether the paper has been peer-reviewed or is preprint-only.
- The paper's venue/journal of submission (described as "work-in-progress").
- Specific results from any pilot experiments with LAVs.
- How the "moral optimization algorithm" would be concretely specified beyond the RLHF framing.
- Whether Yaacov (2025) dual-hybrid structure (referenced p.3) has been empirically tested.
- How cross-cultural variation in moral embedding geometry would be handled.
