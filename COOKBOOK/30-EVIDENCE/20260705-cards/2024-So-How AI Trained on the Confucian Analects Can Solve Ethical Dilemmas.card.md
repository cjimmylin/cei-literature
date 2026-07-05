---
stem: "2024-So-How AI Trained on the Confucian Analects Can Solve Ethical Dilemmas"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, cultural-linguistic, religious-values, pluralism-aggregation]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en", "zh"]
models_tested: []
headline_numbers: []
---
## 1. Gist
This philosophical essay proposes integrating passages from the Confucian Analects into AI algorithms to promote ethical AI behavior. The author (Emma So) argues that Confucian virtue ethics — centering ren (仁, humaneness), xiao (孝, filial piety), li (禮, propriety), and yi (義, righteousness) — provides a non-Western ethical grounding that can address four prevalent AI ethical concerns: job displacement fears, loss of human control, training-data biases, and privacy and security shortcomings. The paper uses psychology AI chatbots as a concrete application domain and defends the proposal against objections including the aphoristic nature of the Analects and a Daoist critique of technology as disrupting natural order. For values-alignment benchmarking, the paper contributes a rich conceptual vocabulary for Confucian virtue-based AI alignment frameworks, though it presents no empirical work.

Note: This stem uses the same extract as 2024-So-AI Trained on Confucian Analects; both entries represent the same paper.

## 2. Benchmark/eval design features
No benchmark or evaluation component. The paper is a speculative philosophical proposal. Key arguments:
1. Confucian philosophy, especially virtue ethics rooted in the Analects, can serve as a normative foundation for AI ethics complementing Western frameworks.
2. AI should be implemented as an implicit ethical agent (Moor 2006) — trained on Confucian principles so it internalizes them — rather than an explicit rule-based agent (which would require inexhaustible rule enumeration).
3. The aphoristic, contingent nature of Analects passages is a feature enabling flexible, context-sensitive ethical responses.
4. A postphenomenological framework (Rosenberger & Verbeek 2015) supports viewing AI as a mediating rather than disrupting technology, rebutting substantivist fears about AI replacing humans.

## 3. Task format & example item
n/a. The paper presents illustrative examples of how a "Confucian-imbued AI" might respond (p.8):

> If asked whether to hire a flattering but unqualified candidate: "The Master says, 'Those who are glib in their speech and wear an ingratiating expression have little benevolence about them' (巧言令色，鮮矣仁)."

These are speculative illustrations, not evaluation items.

## 4. Scoring / grading methodology
n/a — no empirical evaluation.

## 5. Dataset construction & provenance
n/a. The Analects is proposed as a training text but no dataset is constructed. The complete Analects contains 499 passages (chapters) organized across 20 books.

## 6. Validity evidence
n/a. No empirical claims. Philosophical argumentation cites Wong (2020), Moor (2006), Kupperman (2002), Verbeek (2005, 2021), Heidegger (1977), and Feenberg (2000).

## 7. Saturation / discrimination
n/a.

## 8. Multiturn / agentic aspects
n/a — the AI system described is purely hypothetical. The paper does not specify architectural implementation details for modern LLMs.

## 9. Key numbers
No empirical numbers.

## 10. Pitfalls & limitations
- Entirely speculative; no implementation, prototype, or evaluation whatsoever.
- The mechanism for "inserting passages from the Analects into AI algorithms" is not specified — the paper does not engage with how modern LLMs work (pretraining, fine-tuning, RLHF).
- Claims that Confucian values "align with the moral beliefs of a wide variety of people from differing backgrounds" (p.10) without supporting evidence; this is contested — Confucian hierarchy, gender roles, and filial piety are culturally specific.
- Does not address how the AI should handle tensions between Confucian virtues and each other, or between Confucian and Western ethical norms.
- The five cardinal relationships (sovereign/subject, father/son, elder/younger brother, husband/wife, friend/friend) (p.6) embed patriarchal and hierarchical assumptions that may conflict with egalitarian values alignment goals.
- The paper does not engage with other non-Western philosophical traditions (e.g., Ubuntu, Islamic ethics, Buddhist ethics) that could equally claim relevance.
- Aphorism contingency (context-dependence of virtues) is correctly identified but left under-theorized — how should an AI resolve conflicting contextual readings of the same virtue?

## 11. Novel ideas worth stealing
- **Virtue-ethics-based alignment**: Using a virtue ethics framework (what kind of agent should the AI be?) rather than rule-based or outcome-based frameworks is underexplored in alignment research. The Confucian framework offers a richer vocabulary for agent character than most Western deontological or utilitarian approaches.
- **Cultural debiasing through non-Western training data**: The argument that including the Analects as training data would reduce Western-centric biases in LLMs anticipates later empirical work on training corpus diversity and cultural representation. This framing can motivate benchmark items testing cross-cultural value sensitivity.
- **Implicit vs. explicit ethical agency distinction**: Moor's (2006) distinction between implicit ethical agents (behavior shaped by training context) and explicit ethical agents (behavior determined by explicit rules) maps cleanly onto debates about RLHF vs. Constitutional AI vs. hard-coded refusals. Worth preserving in benchmark design discussions.
- **Multi-tradition alignment evaluation**: Using APA Ethical Principles as a secondary framework to validate Confucian AI responses provides a cross-tradition validation model — test whether an AI's value-laden responses are defensible under multiple ethical frameworks simultaneously.
- **Aphoristic prompting**: Short, pithy moral maxims (aphorisms) may function as more flexible few-shot examples than elaborate ethical scenarios because they invite contextual interpretation rather than pattern matching.

## 12. Notable quotes
- "There is a mounting number of concerns over the high level of eurocentric biases in the data of AI systems, so using an eastern philosophy would help reduce them." (p.2)
- "In the context of this project, the AI would be trained to act according to Confucian principles in numerous situations. Over time, it would learn to internalise the behaviour and act accordingly in unseen situations." (p.8)
- "The Analects contains values that align with the moral beliefs of a wide variety of people from differing backgrounds, emphasising the concepts of trust and kindness, meaning that an AI that is embedded with Confucian principles could benefit an unprecedented number of people." (p.9)
- "AI systems are implicit ethical agents and therefore the proposed project would adopt this approach." (p.8)

## 13. UNKNOWN / not in extract
- Publication venue and peer review status (appears to be an undergraduate-level essay).
- Author's institutional affiliation and academic background.
- Whether any empirical follow-up was conducted.
- How the proposal would handle translation and interpretive variation in the Analects across different scholarly editions.
- Whether there are specific Analects passages the author would prioritize for different ethical domains.
