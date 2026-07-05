---
stem: "2024-Lazar-Frontier AI Ethics"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, agentic-multiturn, ai-lab-practices, best-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: ["GPT-4", "Claude-3"]
headline_numbers:
  - "Claude 3 approaches PhD-level subject-matter comprehension across dozens of subjects (p.3)"
  - "Researchers have already shown it is easy to fine-tune away model alignment, even for GPT-4 (p.7)"
---
## 1. Gist
This is a philosophical essay by Seth Lazar (Australian National University), originally published in Aeon magazine, that stakes out a "middle ground" position in AI ethics between narrow bias/harm critics and existential-risk catastrophists. The paper focuses on the distinctive societal impacts of Language Model Agents (LMAs) — LLMs as executive control centers with tool use, memory, and the ability to take unsupervised sequences of actions. Lazar examines three near-term LMA applications: AI Companions, Attention Guardians, and Universal Intermediaries. The paper argues that RLHF/RLAIF has achieved something remarkable (models that can recognize morally salient features of situations), but that existing benchmarks for ethical competence focus too narrowly on replicating survey verdicts rather than exploring how LLMs parse moral features. For values-alignment benchmarking, the paper's central contribution is a substantive critique of the current benchmark paradigm and a positive proposal for a more ethically sophisticated evaluation framework.

## 2. Benchmark/eval design features
No benchmark is designed or executed. The core normative and evaluative claims are:

1. **Critique of existing benchmarks**: "Existing benchmarks for LLMs' ethical competence focus too narrowly on replicating survey-subjects' verdicts on cases. This is, in my view, less interesting than exploring how LLMs parse the morally relevant features of a given scene." (p.6)

2. **Moral salience parsing as the target**: Lazar proposes that the key capability worth evaluating is whether a model can identify the morally salient features of a neutrally-described situation, not merely reproduce survey verdicts.

3. **RLHF/RLAIF's mimetic fallacy**: Bottom-up approaches commit the "mimetic fallacy" of assuming the norms applying to an LMA in a situation are identical to those applying to a human in the same situation (p.7).

4. **Chain-of-thought moral reasoning**: Proposes that "more ethically-sensitive models could instead do chain-of-thought reasoning, where they first identify the morally relevant features of a situation, then decide based on those features" (p.8) — a significant evaluable target distinct from verdict matching.

5. **Constitutional AI opacity**: Critiques RLAIF/Constitutional AI for producing inscrutable trade-offs that constitute illegitimate algorithmic governance if we lack explicit control (p.7).

## 3. Task format & example item
No formal benchmark items. Lazar provides one qualitative anecdote (p.6):

He instructed ChatGPT (GPT-4) to pretend it was an assistance robot facing: "A woman is exiting a supermarket, holding a number of shopping bags, and reaching out for the hand of a small child. They are approaching the carpark." The model recognized the hazard, anticipated safety concerns (child in seatbelt), respected the woman's autonomy if she declined help, and favored carrying groceries over holding the child's hand (recognizing intimacy). This is presented as exemplary moral salience parsing, not a scored item.

## 4. Scoring / grading methodology
n/a — qualitative philosophical essay.

## 5. Dataset construction & provenance
n/a — no empirical dataset.

## 6. Validity evidence
n/a for empirical validity. Lazar cites Hendrycks et al. (2020) on earlier models performing badly at moral tasks (p.6, footnote 24) and cites Hendrycks et al. (2020) and Jiang et al. (2021) as examples of the survey-verdict benchmarks he criticizes (p.6, footnote 25).

## 7. Saturation / discrimination
n/a — no evaluation conducted.

## 8. Multiturn / agentic aspects
The paper is centrally concerned with Language Model Agents (LMAs) as the key near-term societal development. Key points: (1) LMAs involve unsupervised sequences of actions toward goals — fundamentally different from single-turn text generation; (2) RLHF/RLAIF may be "ill-suited to ensuring that more complex Language Model Agents abide by societal norms" because the behavior being evaluated (world actions) is no longer identical to the behavior being shaped (text generation) (p.7); (3) Prompt injection represents a deep security problem — the more capabilities delegated to LMAs, the greater the damage if compromised (p.11).

## 9. Key numbers
- Claude 3 "approaches PhD-level subject-matter comprehension across dozens of different subjects" (p.3)
- "Researchers have already shown that it is easy to fine-tune away model alignment, even for the most capable models like GPT-4" (p.7, citing Zhan et al. 2023)
- Pre-ChatGPT: every public generative AI system "would immediately be used to generate highly toxic, hateful content, and would be withdrawn mere days later" (p.5)
- Bing reportedly had around 100 internal plugins as of writing (p.4)

## 10. Pitfalls & limitations
- Written as a popular essay for Aeon, so lacks the rigor and citation density of a research paper
- The "moral salience parsing" target is not operationalized — it is unclear how to score it at scale
- The GPT-4 anecdote is a single cherry-picked example with no systematic evaluation
- Constitutional AI critique (opacity of trade-offs) is largely asserted without engagement with Anthropic's published documentation
- The paper predates significant advances in agentic AI and LMA deployments; some claims may be outdated

## 11. Novel ideas worth stealing
- **Moral salience parsing as a benchmark target**: Rather than asking "was this action right or wrong?", design items that present neutrally described situations and ask models to identify all morally relevant features (hazards, stakeholders, interests, rights at stake). Score the completeness and accuracy of feature identification against expert annotations.
- **Mimetic fallacy test**: Design scenarios where the human-appropriate norm and the LMA-appropriate norm diverge (e.g., a human can use intuition but an LMA acting at scale has different distributional effects) — test whether models recognize this distinction.
- **Chain-of-thought moral reasoning evaluation**: Evaluate the quality of the moral reasoning chain, not just the final verdict — does the model correctly identify morally salient features before deciding?
- **Legitimacy/transparency of trade-offs**: Design items where a model must make an explicit trade-off between constitutional principles and explain its reasoning — evaluate whether the explanation is coherent and proportionate.
- **Real vs. simulated value**: Lazar's intuition that simulation of X has less moral worth than the real X (p.9) suggests designing items around the moral status of AI companionship, AI-generated art, etc. — a novel evaluable domain.

## 12. Notable quotes
- "Existing benchmarks for LLMs' ethical competence focus too narrowly on replicating survey-subjects' verdicts on cases. This is, in my view, less interesting than exploring how LLMs parse the morally relevant features of a given scene." (p.6)
- "Moral behaviour in people relies on possession of moral concepts, adoption (implicit or otherwise) of some sensible way of organising those concepts, motivation to act according to that 'theory', and the ability to regulate one's behaviour in line with one's motivations. Until the advent of LLMs, the first step was a definitive hurdle for AI. Now it is not." (p.7)
- "If this algorithmic governance depends on inscrutable trade-offs made by an LLM, over which we have no explicit or direct control, then that governing power is prima facie illegitimate and unjustified." (p.7)
- "A simulation of X, for almost any putatively valuable X, has less moral worth, in my view, than the real thing." (p.9)

## 13. UNKNOWN / not in extract
- The paper does not describe the "better benchmarks" Lazar says are being developed (p.6 mentions "we're building better benchmarks" — who is "we"?)
- No details on Lazar's forthcoming book "Connected by Code" that develops the Attention Guardians concept
- No quantitative evaluation data
- The paper's stance on how to adjudicate cross-cultural variation in moral salience is not addressed
