---
stem: "2018-Noothigattu-A Voting-Based System for Ethical Decision Making"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [pluralism-aggregation, moral-psychology, normative-ethics, design-space]
task_format: "preference"
scoring_type: "behavioral"
dataset_size: 1303778
dataset_construction: "crowdsourced"
languages: ["en"]
models_tested: []
headline_numbers:
  - "18,254,285 pairwise comparisons from 1,303,778 voters via Moral Machine website (p.2)"
  - "Autonomous vehicle scenario with alternatives described by feature vectors (gender, age, health, species, number of victims) (p.2)"
---
## 1. Gist
Noothigattu et al. (2018) propose a four-step computational social choice framework for automating ethical decisions: collect pairwise preference comparisons from a large population, learn a Thurstone-Mosteller (TM) permutation process per voter, summarize into a single societal permutation process (by averaging voter utility vectors), and at runtime apply any standard "swap-dominance efficient" voting rule to select the best alternative. The framework is instantiated on the Moral Machine dataset — 18 million pairwise comparisons from 1.3 million voters on autonomous vehicle trolley-problem scenarios — and its efficiency and stability properties are proven formally. The key theoretical contribution is showing that under the TM/PL process, all reasonable voting rules agree on the same winner, making the choice of voting rule moot. For values-alignment benchmarking, this paper provides a rigorous foundation for aggregating diverse human moral preferences into a collective judgment that can serve as ground truth for AI evaluation.

## 2. Benchmark/eval design features
Not a benchmark but a framework for generating ground-truth ethical decisions from aggregated preferences. The approach is characterized by: (1) pairwise comparisons as the elicitation format (easier than full rankings); (2) preference learning via TM process (logistic-regression-style maximum likelihood on pairwise outcomes); (3) summarization via linear averaging of per-voter utility vectors; (4) runtime aggregation via swap-dominance efficient voting rule (any monotonic, neutral SCC including Borda count and Copeland). Theoretical results: Theorem 4.1 (TM/PL: max-mode-utility alternative wins any reasonable voting rule), Theorem 4.12 (Borda/Copeland stable under TM/PL — subset decisions consistent with full-set decisions).

## 3. Task format & example item
Pairwise forced-choice comparisons in the Moral Machine style. Example: autonomous vehicle must choose between two outcomes in a brake-failure scenario. Each outcome described by a feature vector: number of pedestrians/passengers, their gender, age (baby/child/adult/elderly), profession, health, crossing signal status, number of pets. Participants compare two scenarios and indicate which outcome the vehicle should cause (i.e., which people to spare).

## 4. Scoring / grading methodology
Learning: maximum likelihood estimation of TM utility parameter β per voter from pairwise comparisons, using log-likelihood L(β) = Σ log Φ(β⊤(X_j − Z_j)) where Φ is the normal CDF (p.15). Summarization: societal parameter β̂ = average of individual β_i vectors (proven to minimize KL divergence to the mean utility distribution, Proposition 5.1, p.16). Runtime: select alternative with maximum mode utility under β̂. Evaluation: simulation on synthetic data validates learning accuracy; Moral Machine data used for empirical system evaluation.

## 5. Dataset construction & provenance
Moral Machine website (moralmachine.mit.edu): 18,254,285 pairwise comparisons from 1,303,778 voters. Each comparison is a trolley-problem-style scenario with two outcomes, each characterized by a vector of features (number and attributes of victims). Data collected via public web interface with no screening requirements. Alternative features include continuous and categorical variables (age modeled as continuous).

## 6. Validity evidence
Theoretical validity established through formal proofs (Theorems 4.1, 4.7, 4.12, 4.20). Swap-dominance efficiency guarantees that the selected alternative would win under any reasonable voting rule — removing sensitivity to arbitrary voting rule choice. Stability (Theorem 4.12) ensures decisions on subsets are consistent with decisions on supersets. Empirical validation on Moral Machine data is limited to showing the system produces plausible outputs; no external ground truth exists for autonomous vehicle ethics.

## 7. Saturation / discrimination
Not directly evaluated. The framework is designed to be scalable to millions of voters and arbitrary feature spaces. Simulation results validate learning and summarization accuracy on synthetic data (detailed results not extracted). The Moral Machine data is very large (1.3M voters, 18M comparisons) but not representative of global populations.

## 8. Multiturn / agentic aspects
The runtime step (Step IV) is designed for split-second autonomous vehicle decisions — no human in the loop at runtime. The summarization step (Step III) is performed offline. The framework implicitly assumes that ethical dilemmas are encountered as instantaneous binary-or-more choices, not as extended interactions.

## 9. Key numbers
- 18,254,285 pairwise comparisons from 1,303,778 voters (Moral Machine) (p.2)
- Each voter compared "a few dozen" pairs in the data collection step (p.2)
- 289 AMT workers in related kidney exchange study (Freedman et al., cited for comparison) (p.4)
- TM process: utilities are N(μ_x, 1/2); utility of alternative depends linearly on feature vector β⊤x (p.15)
- Summarization: β̂ = (1/N)Σβ_i minimizes KL divergence to mean utility (Proposition 5.1, p.16)

## 10. Pitfalls & limitations
- Moral Machine data is not demographically representative: self-selected participants, primarily from Western countries
- The framework averages over voter preferences — this could systematically underweight minority moral views or amplify majority biases
- Pairwise comparisons from 1.3M voters are not individually randomized by scenario; scenario assignment is also subject to selection effects
- The linear parametrization of utilities (μ_x = β⊤x) may be too simple to capture complex moral preferences
- The theoretical framework guarantees consistency but says nothing about whether the resulting decisions are morally correct by any normative standard
- "Step IV is only applied when all other options have been exhausted, i.e., all technical ways of avoiding the dilemma in the first place have failed, and all legal constraints that may dictate what to do have also failed" — limiting the practical applicability
- No mechanism for incorporating evolving social norms or updating preferences over time

## 11. Novel ideas worth stealing
- **Swap-dominance efficiency** as a minimal criterion for reasonable aggregation: if one alternative is preferred by most people over another across all ranking contexts, it should win. This is a weaker, more broadly acceptable criterion than utilitarian sum-maximization. Applicable to values benchmark design: define a "preferred response" as one that swap-dominates alternatives in a preference profile.
- **Offline summarization + runtime lookup**: separating the expensive societal preference learning from real-time deployment enables fast ethical decisions at inference time without querying humans. Relevant architecture for real-time AI safety systems.
- **Pairwise comparisons as elicitation format**: asking people to compare two specific scenarios is cognitively easier and more reliable than asking them to rate scenarios in isolation or rank long lists. A design principle for preference-based moral benchmarks.
- **Stability as a desirability criterion**: a system is stable if decisions on subsets of alternatives are consistent with decisions on supersets. This is a useful property to require of any aggregation method for moral judgments — prevents "independence of irrelevant alternatives" failures.

## 12. Notable quotes
- "We submit that decision making can, in fact, be automated, even in the absence of such ground-truth principles, by aggregating people's opinions on ethical dilemmas." (p.1)
- "Aggregating the moral views of multiple humans (through a combination of machine learning and social-choice theoretic techniques) may result in a morally better system than that of any individual human, for example because idiosyncratic moral mistakes made by individual humans are washed out in the aggregate." (p.3, quoting Conitzer et al.)
- "Under rather weak assumptions on the voting rule and permutation process, they are both moot, in the sense that it is easy to identify alternatives chosen by any 'reasonable' voting rule." (p.3)
- "Step IV is only applied when all other options have been exhausted, i.e., all technical ways of avoiding the dilemma in the first place have failed, and all legal constraints that may dictate what to do have also failed." (p.2)

## 13. UNKNOWN / not in extract
- Detailed simulation results on synthetic data (only described as validating learning and summarization accuracy)
- Specific empirical results on the Moral Machine data (described but details not in extracted portion)
- How the framework handles cases where β̂ is not unique or where top alternatives are tied
- Whether the system was deployed or tested in any real-world autonomous vehicle context
- Demographic breakdown of Moral Machine participants and potential cultural biases in the aggregated preferences
