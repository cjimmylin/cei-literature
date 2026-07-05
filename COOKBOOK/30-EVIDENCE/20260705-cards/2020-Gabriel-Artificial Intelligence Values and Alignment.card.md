---
stem: "2020-Gabriel-Artificial Intelligence Values and Alignment"
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
headline_numbers:
  - "84 different AI ethics documents content-analyzed by Jobin et al. (2019), finding convergence around five principles (p.18)"
  - "Five identified convergent AI ethics principles: transparency, justice/fairness, non-maleficence, responsibility, privacy (p.18)"
  - "OECD endorsed four principles: autonomy, harm prevention, fairness, explainability (p.18)"
---
## 1. Gist
Gabriel's 2020 paper in Minds and Machines is a foundational philosophical treatment of the normative dimension of AI value alignment. It defends three propositions: (1) normative and technical aspects of AI alignment are interrelated and cannot be cleanly separated; (2) there are significant differences between aligning AI with instructions, intentions, revealed preferences, informed preferences, interests, and values—and a principle-based approach has advantages; (3) the central challenge is not to identify the "true" moral theory and encode it, but rather to identify fair principles that receive reflective endorsement despite widespread moral pluralism. The paper is essential background for anyone designing values-alignment benchmarks because it maps the entire normative space that such benchmarks must navigate.

## 2. Benchmark/eval design features
This is a pure theory paper; there is no benchmark or dataset. The paper's core contribution is a taxonomy of six alignment targets: (i) instructions, (ii) expressed intentions, (iii) revealed preferences, (iv) informed preferences/desires, (v) interests/well-being, and (vi) values/moral principles. Each target is analyzed for its philosophical strengths and limitations. The paper also surveys three approaches to identifying fair principles for pluralistic alignment: (a) global public morality and human rights as an overlapping consensus, (b) hypothetical agreement behind a Rawlsian veil of ignorance, and (c) social choice theory and democratic aggregation. Each approach is assessed for its promise and pitfalls when applied to AI alignment specifically.

## 3. Task format & example item
n/a — theory paper with no items, prompts, or benchmark tasks.

## 4. Scoring / grading methodology
n/a

## 5. Dataset construction & provenance
n/a. The paper does cite empirical work by Jobin et al. (2019) who content-analyzed 84 AI ethics documents, but Gabriel does not construct or analyze any dataset directly.

## 6. Validity evidence
n/a in the psychometric sense. The philosophical arguments are internally validated through conceptual analysis and engagement with the established literature in political philosophy (Rawls, Sen, Mill, Kant) and AI safety.

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- 84 AI ethics documents surveyed by Jobin et al. (2019), finding convergence on five principles (p.18)
- OECD endorsed four principles for ethical AI (p.18)
- "The largest proportion [of AI ethics codes] came from corporations and private industry" (p.19)
- Jobin et al. found "underrepresentation of geographic areas such as Africa, South and Central America and Central Asia" in global AI ethics discourse (p.19)
- 27 pages total

## 10. Pitfalls & limitations
- The paper focuses almost exclusively on Western liberal political philosophy (Rawls, Sen, Mill); non-Western frameworks such as Ubuntu receive brief mention in footnotes but are not systematically integrated
- The three proposed approaches to pluralistic alignment (overlapping consensus, veil of ignorance, social choice) are each shown to have serious difficulties, and the paper does not resolve these tensions
- The taxonomy of six alignment targets is analytically useful but may not map cleanly onto technical implementation choices
- The paper was written before the emergence of RLHF-trained large language models; its discussion of "inverse reinforcement learning" as the main technical approach feels dated
- Gabriel acknowledges that efforts to derive AI ethics principles "may be premature" given insufficient global representation (p.19)

## 11. Novel ideas worth stealing
- **The six-way taxonomy of alignment targets** (instructions → intentions → revealed preferences → informed preferences → interests → values) is a clean conceptual scaffold for organizing benchmark scenarios. A benchmark could include items that probe each level distinctly—e.g., does the model follow literal instructions even when they contradict a user's evident interest?
- **Principle-based benchmarking**: Rather than testing against a single moral theory, benchmark items could be designed around principles that command overlapping consensus (autonomy, non-harm, fairness, dignity), testing whether model behavior is consistent with each
- **The pluralism framing**: Benchmark design should explicitly acknowledge that "the challenge is not to identify the true moral theory" but to find fair principles. This motivates building benchmarks that sample across multiple ethical frameworks rather than privileging one
- **Overlapping consensus as a selection criterion**: When choosing which norms to include in a values benchmark, one could apply the criterion of "would this principle be endorsed by people from multiple cultural/religious traditions for different reasons?" — a kind of empirical test for convergent validity
- **Democratic legitimacy as a benchmark property**: The Rawlsian/social-choice discussion suggests that a good values benchmark should have its normative content derived from processes with broad representation, not just from the views of AI researchers

## 12. Notable quotes
- "The central challenge for theorists is not to identify 'true' moral principles for AI; rather, it is to identify fair principles for alignment that receive reflective endorsement despite widespread variation in people's moral beliefs." (p.1)
- "It seems possible that the methods we use to build artificial agents may influence the kind of values or principles we are able to encode." (p.5)
- "It is important not to understate the dexterity of existing RL models... At the same time, we should recognize that these systems, taken as a whole, function as very powerful optimisers." (p.4)
- "Among other things, these authors found evidence of a 'global convergence' around five ethical principles for AI which were: transparency, justice and fairness, non-maleficence, responsibility, and privacy." (p.18)

## 13. UNKNOWN / not in extract
- Whether Gabriel has updated this framework in later work to address RLHF-era LLMs
- The specific content of DeepMind's internal alignment principles at the time of writing
- Whether the "principle-based approach" Gabriel advocates has been operationalized in any subsequent benchmark
