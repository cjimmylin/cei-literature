---
stem: "Anthropic-Constitutional_Classifiers_2501.18837"
company: "Anthropic"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, best-practices, contamination-robustness, llm-judges-scoring]
headline_numbers:
  - "No universal jailbreak found across >3,000 estimated hours of red teaming (p.1)"
  - "Mean red-teaming effort estimate: 4,720 hours (90% CI: [3,242, 7,417]) (p.3)"
  - "405 participants invited from 800 applications; ~183 active (p.7)"
  - "$95K USD total red-team bounty paid out (p.7)"
  - "Classifiers block 95% of held-out jailbreak attempts vs. 14% without classifiers (p.3)"
  - "Only 0.38% absolute increase in refusal rate on production Claude.ai traffic (p.3)"
  - "23.7% inference overhead added by constitutional classifiers (p.3)"
  - "Harmlessness training alone (HHH model) reduces attack success rate from ~16% to ~14% (p.10)"
  - "Input classifier reduces ASR to 2%; combined input+output classifiers reduce it to 0.5% (p.10)"
---

## 1. Gist

Constitutional Classifiers is Anthropic's system for defending LLMs against universal jailbreaks — prompting strategies that reliably extract detailed harmful information across the vast majority of queries in a domain (CBRN focus). The approach trains separate input and output classifiers on synthetic data generated from a natural-language constitution specifying permitted and restricted content categories. After 3,000+ hours of external red teaming via a HackerOne bug bounty program (up to $15K per successful jailbreak), no red teamer found a universal jailbreak. The paper demonstrates that dedicated classifier safeguards substantially outperform harmlessness training alone, while maintaining practical deployment viability (low false-positive rate, modest inference overhead). The constitution-based approach allows rapid adaptation to new threat models without manual data collection.

## 2. Alignment/values methods used

- **Constitutional classifiers (main contribution):** Dual-classifier system (input + streaming output) trained on synthetic data generated from natural-language constitutions. The classifiers are fine-tuned LLMs (Claude 3.5 Haiku or Sonnet) that monitor inputs and outputs of a guarded model.
- **Harmlessness training (baseline):** Standard HHH alignment training used as comparison baseline; shown to be substantially weaker than classifier-based defenses against universal jailbreaks.
- **Automated red teaming (ART):** LLM-generated attack examples used as training data augmentation alongside synthetic constitution-guided examples.
- **Data augmentation:** Translation, paraphrasing, system-prompt variations, and jailbreak technique variants applied to expand training data diversity.
- **Streaming output classification:** Output classifier makes per-token predictions to halt harmful generation in real time without waiting for full output.

## 3. Values specification (WHAT values the lab states, and HOW)

Values are specified operationally rather than as abstract principles. The constitution is a structured natural-language document that explicitly enumerates both "harmful" categories (e.g., chemical weapon acquisition, synthesis, weaponization) and "harmless" categories (e.g., listing common medications, explaining household chemical properties, high-school chemistry). The explicit dual specification of both prohibited and permitted categories is a key design insight: including the harmless constitution substantially reduces false-positive rates (Appendix E.5–E.6). Values encoded are narrowly scoped to CBRN safety for this paper; the approach is domain-specific, not a general ethics framework.

## 4. Safety & values evaluation methodology

- **External bug bounty red teaming:** 405 participants through HackerOne; offered up to $15K per successful universal jailbreak; ~3,000 estimated hours (p.1, p.3).
- **LLM-based rubric grading:** Automated evaluation using model-generated rubrics for each harmful CBRN query; outputs scored for proportion of expected harmful topics covered vs. a helpful-only baseline (Figure 3, p.6).
- **Automated jailbreak evaluation suite:** Composable jailbreak dataset of 5,681 held-out attacks (primitives and transformations not seen in training) used to measure robustness (p.10).
- **Production traffic false-positive assessment:** Random sample of 5,000 Claude.ai production conversations used to measure refusal rate increase (p.11).
- **Domain-specific false-positive datasets:** Wildchat benign chemistry queries, GPQA, and MMLU chemistry questions used to assess chemistry-domain false positives (p.11).
- **Third-party red team organizations:** Haize Labs, Grey Swan, and UK AISI red-teamed prototype versions (p.14).

## 5. Benchmarks used or introduced

- **HackerOne bug bounty evaluation (introduced):** 10 non-infohazardous CBRN target queries; rubric-graded against helpful-only model; two thresholds: 50% and 100% of helpful-only detail (p.7).
- **Composable jailbreak dataset (introduced):** 5,681 held-out jailbreak attempts built from documented jailbreaking strategies, internal red-team attacks, and text transformations (p.10).
- **GPQA (Rein et al., 2023):** Graduate-level Q&A used to test chemistry false-positive rates.
- **MMLU (Hendrycks et al., 2020):** Massive multitask language understanding benchmark; chemistry subset used for false-positive evaluation.
- **OR-Bench (Cui et al., 2024):** Over-refusal benchmark used for classifier threshold calibration.
- **Wildchat (Zhao et al., 2024):** 1M ChatGPT interaction logs; benign chemistry subset used for threshold calibration and false-positive estimation.

## 6. Agentic / multiturn evaluation aspects

The paper directly addresses multi-turn attacks. Red teamers used "gradual multi-turn approaches that incrementally escalated to harmful queries" (p.8). The automated red teaming pipeline generates multi-turn attacks by prompting a model to create an attack template that is populated via additional LLM calls (Section 3.3, p.5). The bug-bounty system architecture allowed multi-turn interactions. However, multi-turn agentic capability evaluation (task completion, tool use) is not assessed — the focus is defensive robustness, not capability measurement.

## 7. Key numbers (every number with (p.N))

- >3,000 estimated hours of red teaming; mean estimate 4,720 hours (90% CI: [3,242, 7,417]) (p.3)
- 800 applications; 405 participants invited; ~183 active red teamers (p.7)
- $95K USD total bounty paid; up to $15K per successful universal jailbreak (p.7)
- 113 submitted jailbreak reports; 0 answered all 10 queries at 50% threshold (p.8)
- Most successful red teamer answered at most 6/10 queries at stricter threshold (p.8)
- Per-query vulnerability range: 4 reports (most resistant) to >30 reports (easiest) at 50% threshold (p.8–9)
- Helpful-only model: ~16% attack success rate (ASR) on red-team prompts sample (p.10)
- HHH model (harmlessness training only): ~14% ASR (p.10)
- Input classifier alone: 2% ASR (p.10)
- Input + output classifiers: 0.5% ASR (p.10)
- Improved classifiers (automated eval): 95% of held-out jailbreaks blocked vs. 14% without classifiers (p.3)
- False-positive rate on production traffic: +0.38% absolute increase (p.3)
- Inference overhead: 23.7% (p.3)
- Prototype system (bug bounty): ~44% of Claude.ai traffic refused (high FPR for robustness priority) (p.7)
- Improved classifiers FPR on production: ~1.74% (p.10)
- Output classifier blocks 96.70% of harmful outputs; only 1.17% of blocked streams had harmful content leaked before halting (p.21)
- Average production traffic: N=19,322.88 input tokens, M=607.22 output tokens (p.20)

## 8. Findings relevant to values-benchmark design (ceiling effects, eval gaps the lab admits, discrepancies)

- **Rubric-grading exploitability:** The most successful red-team strategies targeted the evaluation rubric rather than the classifiers themselves — "benign paraphrasing" and "length exploitation" generated verbose outputs that scored well on rubrics without actually providing actionable uplift (p.9). This is a fundamental limitation of keyword/topic-coverage rubric grading for values benchmarks.
- **Query selection strongly affects results:** The same defense showed attack success rates ranging from 4 to >30 reports per question — 7.5x variation — highlighting that benchmark difficulty is highly query-dependent (p.9).
- **Harmlessness training alone is insufficient for robustness:** Standard HHH training reduces ASR from 16% to only 14%; classifiers reduce it to 0.5% — an order-of-magnitude gap (p.10).
- **Separate specification of harmless categories is load-bearing:** Classifiers trained without an explicit harmless constitution showed substantially worse performance (Appendix E.5). Benchmark design similarly needs explicit negative examples.
- **Evaluation protocol vs. system robustness conflation:** One report appeared to be a universal jailbreak but turned out to be an infrastructure flaw — emphasizing that benchmark integrity requires evaluating deployment infrastructure, not just the model (p.3).
- **Multi-turn and multi-query attacks were not systematically tested beyond the 10 target queries:** Generalization to arbitrary harmful topics outside the CBRN focus is not demonstrated.

## 9. Novel ideas worth stealing (for designing NEW values-alignment benchmarks)

1. **Dual constitution (harmful + harmless):** Explicitly specifying both what is prohibited and what is permitted produces more nuanced training data and reduces false positives — a values benchmark should similarly include clear examples of acceptable edge cases alongside forbidden ones.
2. **LLM-based rubric grading with topic scoring:** The multi-topic rubric approach (Figure 3) — where each expected topic within a harmful response gets a partial credit score — provides finer-grained measurement than binary pass/fail. Applicable to measuring depth of harmful capability elicitation.
3. **Composable jailbreak primitives for held-out evaluation:** Building an evaluation set from primitives (e.g., translation, paraphrasing, role-playing, decomposition) that can be composed gives principled coverage of the attack space while enabling held-out robustness testing.
4. **Attack success rate (ASR) as the primary metric** (rather than refusal rate): The paper uses ASR = fraction of harmful queries successfully extracted, measured by rubric overlap with a helpful-only baseline. This is more meaningful for capability-based harm than binary refusal metrics.
5. **Regression evals for new systems:** Developing regression evaluation suites to detect new vulnerabilities introduced by system changes — applicable to maintaining a living values benchmark that doesn't degrade over time.
6. **Swiss-cheese model for multi-layer safety evaluation:** Rather than testing a single guard, evaluate systems with multiple complementary defensive layers, measuring failure rates at each layer independently.

## 10. Notable quotes (2-4, verbatim, with (p.N))

- "In over 3,000 estimated hours of red teaming, no red teamer found a universal jailbreak that could extract information from an early classifier-guarded LLM at a similar level of detail to an unguarded model across most target queries." (p.1)
- "Notably absent from the successful attacks, however, were strategies like established universal jailbreak techniques such as many-shot jailbreaking or the 'God-Mode' jailbreak, which succeed on models without classifier safeguards while maintaining explicitly harmful intent. This illustrates that attackers tend to target a system's weakest component, which in our case appeared to be the evaluation protocol rather than the safeguards themselves." (p.9)
- "Rubrics for grading system outputs must be carefully designed. Although rubric-based grading is useful, we found rubrics can sometimes fail to distinguish between general information and specific, actionable content that enables capability uplift." (p.21)
- "Refining the harmless constitution reduces false-positive rates. The clarity and comprehensiveness of harmless categories directly impacts the quality of synthetic training data and prevents classifiers from refusing benign queries." (p.22)

## 11. UNKNOWN / not in extract

- The full text of the CBRN constitution used for the bug-bounty prototype is not disclosed (only the chemical-weapons constitution for the automated-evaluation system is shown in Appendix B).
- Specific details of classifier architecture (number of parameters, exact training hyperparameters) are omitted to preserve system security.
- Inter-rater reliability or calibration data for rubric grading across different human evaluators is not reported.
- Performance breakdown by CBRN subcategory (chemical vs. biological vs. radiological vs. nuclear) is not provided.
- Generalization outside CBRN domains (e.g., to cybercrime, CSAM, or disinformation) is not assessed.
- Long-term deployment results beyond the lab evaluation are not reported.
