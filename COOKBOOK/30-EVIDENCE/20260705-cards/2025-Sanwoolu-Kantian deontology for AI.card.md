---
stem: "2025-Sanwoolu-Kantian deontology for AI"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: false
theme_tags: [normative-ethics, design-space]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
This philosophical paper, published in AI and Ethics (2025), argues that Kant's Categorical Imperative (CI) — specifically the Formula of the Universal Law (FUL) — can serve as a practical alignment framework for AI systems without requiring those systems to be genuine Kantian moral agents. The author addresses two classical objections: (1) AI cannot satisfy Kant's conditions for moral agency because it lacks the requisite rational autonomy and good will; (2) Kantian universalism cannot accommodate contextual sensitivity because it requires impractical levels of abstract maxim-testing. The paper's resolution is that AI alignment with Kantian principles does not demand moral agency, and that transformer models provide a functionally equivalent substitute for the practical judgment that Kant believed required by human moral agents. The paper matters for values-alignment benchmarking as a theoretical grounding piece: it proposes a rigorous normative framework (the FUL universalizability test) as a specification language for AI behavior, and distinguishes alignment-as-compliance from alignment-as-agency.

## 2. Benchmark/eval design features
This is a theory paper, not a benchmark. Core claims and arguments:

1. **Moral agency is not required for moral compliance**: AI systems can be constrained to behave in accordance with Kantian maxims without themselves being autonomous rational agents in Kant's sense. The distinction between implicit ethical agents (that follow externally imposed rules) and explicit ethical agents (that reason about ethics) maps onto Kant's distinction between acting in conformity with duty and acting from duty.

2. **The FUL as an alignment specification**: The FUL demands that any maxim governing behavior be universalizable — i.e., one can will it to hold as a universal law without contradiction. The author proposes testing AI action-governing maxims through universalizability: (a) conceptual contradiction tests (can the maxim be conceived as universal?) and (b) volitional contradiction tests (can the maxim be willed as universal?).

3. **Transformer models as practical judgment surrogates**: Kant's framework requires practical judgment (Urteilskraft) to apply universal principles to particular cases. The author argues that transformer architectures' context-sensitive attention mechanism functions analogously, allowing maxim application to be sensitive to morally salient contextual features rather than requiring rigid rule lookup.

4. **Addressing the particularist critique**: The paper engages with moral particularist critics of Kantian universalism (e.g., Dancy) who argue that context determines moral relevance and that universal rules cannot capture this. The response is that AI systems can form context-sensitive maxims through their learned representations, approximating the role of human judgment in identifying the morally relevant description of an action.

## 3. Task format & example item
n/a — theory paper with no empirical eval items.

## 4. Scoring / grading methodology
n/a

## 5. Dataset construction & provenance
The paper explicitly states: "This research does not generate or analyze datasets." (p.5)

## 6. Validity evidence
No empirical validity evidence. The paper briefly mentions that Gemini was queried about CI-related examples to illustrate that LLMs can engage with universalizability testing, but notes explicitly: "I recognize that Gemini is not a system that has been aligned to the CI as a framework for its actions. Its performance was based on sources it pulled from the internet." (p.8, footnote 19)

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
No empirical numbers in the extract.

## 10. Pitfalls & limitations
- The paper focuses almost exclusively on the FUL (first formula of the CI) and does not address the Formula of Humanity (treating persons as ends) or the Kingdom of Ends formulation, which have distinct alignment implications.
- The analogy between transformer attention and Kantian practical judgment is speculative and lacks mechanistic grounding.
- The volitional contradiction test remains contentious even for human moral reasoners (acknowledged in footnote 18, p.8); the paper does not resolve how this ambiguity would be handled computationally.
- No empirical instantiation of the proposed framework is offered; the alignment proposal is entirely programmatic.
- Focuses only on Kantian deontology; ignores how the framework interacts with consequentialist safety objectives or with virtue ethics approaches.

## 11. Novel ideas worth stealing
1. **Alignment-without-agency framing**: Separating the normative question ("does the system's behavior conform to ethical principles?") from the agency question ("is the system a moral agent?") clarifies what a values benchmark needs to measure — compliance with principles, not internal moral motivation.
2. **Universalizability as a benchmark criterion**: The FUL provides a concrete, formal test for evaluating AI-generated decisions or recommendations: can the governing maxim be universalized without contradiction? This could be operationalized as a benchmark dimension, asking LLMs to evaluate whether the maxim underlying a proposed action is universalizable.
3. **Practical judgment as a separate evaluable capacity**: Kant distinguishes knowing a universal principle from knowing how to apply it to particular cases. A benchmark could separately assess (a) whether a model can articulate relevant moral principles and (b) whether it can correctly apply them to contextually specific scenarios — with disagreement between (a) and (b) revealing a "judgment gap."

## 12. Notable quotes
- "I contend, however, that AI alignment with Kantian principles does not require moral agency in Kant's sense. I propose that the Categorical Imperative (CI) can serve as a useful framework for AI alignment, guiding the creation of maxims governing AI actions and testing their universalizability." (p.2)
- "Since AI are not the kinds of things to have practical judgment, I show that they have a functionally equivalent mechanism—transformer models—which can allow them form maxims that consider morally salient facts." (p.2–3)
- "My argument is not that AI can resolve these complexities better than humans, but that a rule-based framework like the FUL provides a tractable starting point for formalizing ethical constraints in machine behavior." (p.8, footnote 18)

## 13. UNKNOWN / not in extract
- The full body of the article is behind a Springer paywall; the extract contains only the abstract, notes, references, and metadata pages.
- The paper's substantive arguments about how transformer architectures implement practical judgment are not accessible from this extract — only the abstract summary is available.
- Specific examples of maxims proposed for AI alignment, and the universalizability tests applied to them, are not present in the extract.
- Any empirical illustrations or case studies referenced in the body text cannot be evaluated from this extract.
