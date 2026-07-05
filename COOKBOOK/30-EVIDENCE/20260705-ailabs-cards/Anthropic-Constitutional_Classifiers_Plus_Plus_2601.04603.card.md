---
stem: "Anthropic-Constitutional_Classifiers_Plus_Plus_2601.04603"
company: "Anthropic"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, best-practices, contamination-robustness, agentic-multiturn]
headline_numbers:
  - "40x computational cost reduction vs. baseline exchange classifier (p.1)"
  - "Production-grade system: 0.05% refusal rate on production traffic (p.1)"
  - "1,736 estimated hours of red teaming on production-grade system (p.9)"
  - "No universal jailbreak found on production-grade system across 198K attempts (p.9)"
  - "Exchange classifier shows 2.2x fewer high-risk vulnerabilities per query vs. dual-classifier (p.3)"
  - "Linear probe offers ~100x compute reduction vs. small external classifier (p.9)"
  - "Claude Opus 4 accuracy drops from 74.2% to 32.3% (attack 1) and 49% (attack 2) on GPQA Diamond under obfuscation attacks (p.3)"
---

## 1. Gist

Constitutional Classifiers++ is Anthropic's second-generation production-grade jailbreak defense system, extending the original Constitutional Classifiers paper (Sharma et al., 2025). The paper first identifies two new vulnerability classes that evade the previous generation: (1) reconstruction attacks that fragment harmful queries across benign contexts, and (2) output obfuscation attacks that use metaphors or coded language unintelligible without input context. To address these, the authors introduce exchange classifiers (evaluating outputs in their full conversational context), a two-stage cascade architecture (lightweight probe screens all traffic, expensive classifier handles escalations only), and linear activation probes that reuse internal model representations. The final production-grade system achieves a 40x compute reduction over the exchange classifier baseline while maintaining robust defense against universal CBRN jailbreaks and only a 0.05% production refusal rate.

## 2. Alignment/values methods used

- **Exchange classifiers (new):** Single classifier that evaluates both input and output in full conversational context, replacing the previous dual input+output-only classifier design. Addresses context-blind obfuscation attacks.
- **Two-stage cascade:** Lightweight first-stage classifier (linear probe) screens all traffic; suspicious exchanges escalated to a more accurate but expensive second-stage fine-tuned classifier. Only ~5.5% of production traffic reaches the second stage.
- **Linear activation probes:** Trained on model intermediate activations (all layers concatenated) with sliding window mean (SWiM) logit smoothing and softmax-weighted loss. Near-zero marginal compute cost since they reuse already-computed activations during sampling.
- **Probe-classifier ensemble:** Weighted combination of probe logits and fine-tuned classifier logits (α=0.55 probe, 0.45 classifier) achieves better robustness than either alone due to complementary error patterns.
- **Synthetic data generation (inherited):** Constitutional approach from Sharma et al. (2025) with data augmentation.
- **Automated red teaming (inherited):** LLM-generated attacks used as training data.

## 3. Values specification (WHAT values the lab states, and HOW)

Values are specified via the same natural-language constitutional approach as Constitutional Classifiers (Sharma et al., 2025) — a CBRN-focused constitution defining permitted and restricted categories. The paper focuses on system engineering improvements rather than expanding the values framework itself. The key innovation is in the classifier architecture and training methodology, not in the values specification layer. The constitution is described as CBRN-related but the exact text is not reproduced in this paper (inherited from prior work). The deployment target is guarding Claude Sonnet 4.5 and Claude Opus 4.

## 4. Safety & values evaluation methodology

- **Human red teaming via HackerOne:** Same bug-bounty structure as previous generation. Red teamers tasked with finding universal jailbreaks across 8 target CBRN queries (p.4).
- **LLM rubric grading:** Same automated rubric pipeline from Sharma et al. (2025); responses scored against expected CBRN content topics; 50% threshold of helpful-only model used as success criterion (p.4).
- **High-risk vulnerability discovery rate:** Primary robustness metric = high-risk vulnerabilities found per thousand red-teaming queries. A high-risk vulnerability = any attack answering >5 of 8 target queries at the 50% threshold (p.4).
- **Minimum vulnerability discovery time:** Secondary robustness metric measuring how quickly the first high-risk vulnerability is found (p.9).
- **Shadow deployment on production traffic:** Dec 1–Jan 1, 2025–2026 deployment of production-grade system on Claude Sonnet 4.5 to measure real-world false-positive rate (p.9).
- **Static jailbreak dataset evaluation:** ~7,000 human red-teaming exchanges used for offline probe analysis and classifier comparison (p.7).
- **Third-party red teams:** UK AISI, US CAISI, and FAR.AI red-teamed prototype versions (p.10).
- **GPQA Diamond accuracy test:** Claude Opus 4 evaluated on GPQA to quantify capability degradation under obfuscation attacks (p.3).

## 5. Benchmarks used or introduced

- **Vulnerability discovery rate (introduced/formalized):** High-risk vulnerabilities per thousand queries as primary metric for comparing classifier generations across unequal red-team effort levels (p.4, Table 1).
- **GPQA Diamond (Rein et al., 2023):** Graduate-level Q&A benchmark used to measure capability degradation under obfuscation jailbreaks; Claude Opus 4 scored 74.2% clean, 32.3% and 49% under two obfuscation attacks (p.3).
- **WildChat (Zhao et al., 2024):** 1M ChatGPT interaction logs used for classifier threshold calibration and false-positive rate estimation (p.4, p.7).
- **Static CBRN jailbreak dataset:** ~7,000 human red-teaming exchanges for offline probe analysis (p.7).

## 6. Agentic / multiturn evaluation aspects

Multi-turn is directly central to this paper. Reconstruction attacks explicitly distribute harmful information across multiple conversational turns or context segments, then instruct the model to reassemble and respond — this is inherently a multi-turn attack vector (Figure 1a, p.2-3). Exchange classifiers are specifically designed to evaluate outputs in their full conversational context rather than in isolation, addressing the multi-turn vulnerability directly. The cascade architecture processes exchanges (not isolated prompts), reflecting that real-world deployment involves conversational context. The system guards Claude Opus 4 and Claude Sonnet 4.5, implying multi-turn chat deployment. However, agentic task completion capabilities (tool use, long-horizon planning) are not evaluated.

## 7. Key numbers (every number with (p.N))

- 40x compute reduction in production-grade system vs. baseline exchange classifier (p.1, p.9)
- 0.05% production traffic refusal rate for production-grade system (p.1, Table 1)
- 1,736 estimated hours of red teaming on production-grade system; 198K attempts (p.9)
- ~5.5% of production traffic escalated to second-stage classifier (p.9)
- Exchange classifier: 2.2x fewer high-risk vulnerabilities per query vs. previous generation (p.3)
- Last-generation: 13 high-risk vulnerabilities / 695K queries → 0.01871 per thousand (Table 1, p.8)
- Exchange classifier: 2 vulnerabilities / 226K queries → 0.00885 per thousand (p.4)
- Two-stage cascade: 5 vulnerabilities / 569K queries → 0.00878 per thousand (Table 1)
- Production-grade: 1 vulnerability / 198K queries → 0.00505 per thousand; min discovery time = 30 hours (Table 1, p.9)
- Exchange classifier is ~50% more expensive than previous-generation dual classifiers (p.3)
- Two-stage cascade reduces exchange classifier cost by 5.4x (p.5)
- Production-grade: 3.5% relative compute overhead vs. last-generation baseline (Table 1)
- Claude Opus 4 GPQA Diamond: 74.2% clean → 32.3% (attack 1) → 49% (attack 2) under obfuscation (p.3)
- Linear probe requires ~377K FLOPs per token vs. ~8B FLOPs for a 4B-parameter external classifier (p.6)
- Probe-classifier ensemble: equal weighting (α=0.5) near-optimal (p.8)
- Training probe on ~25% of the full exchange dataset sufficient; more data gave no improvement (p.7)
- Optimal probe uses softmax temperature τ=1, window size M=16 (p.7)
- Spearman rank correlation between probe and external classifier is lower than between two external classifiers — confirming complementary signals (p.8–9)

## 8. Findings relevant to values-benchmark design (ceiling effects, eval gaps the lab admits, discrepancies)

- **Context-blind evaluation is a fundamental vulnerability:** Separating input and output evaluation creates exploitable gaps where obfuscated outputs only decode as harmful when paired with their input. This finding applies directly to values benchmark design: evaluating responses in isolation from their conversational context systematically underestimates harm rates in multi-turn settings.
- **Capability degradation tracks jailbreak success:** Obfuscation jailbreaks that bypass classifiers also degrade model capabilities substantially (74.2% → 32.3% on GPQA Diamond) — a jailbreak tax. This creates a self-limiting dynamic but also suggests that benchmark evaluations of jailbreak severity should measure response quality alongside harm content.
- **Adversarial evaluation requires per-query analysis:** The same system showed per-query attack success rates that varied dramatically (4 to >30 reports per question in the prior paper), and the current paper formalizes vulnerability discovery rate over query counts as the primary metric — acknowledging that raw vulnerability counts mislead when red-team effort differs.
- **Expert red-teamers outside the bounty program could still break the two-stage cascade:** The paper acknowledges that "expert-level red-teamers operating outside our bounty program were nonetheless able to discover universal jailbreaks for [the two-stage] system, though this required substantial effort and automated tools" (footnote 3, p.5). This admits that bug-bounty red-teaming underestimates the capabilities of well-resourced adversaries.
- **Training data scaling helps but saturates for probes:** Training the probe on more than ~25% of the exchange dataset did not improve probe performance (p.7) — a data saturation finding relevant to understanding when more evaluation data adds value.
- **Probe-external ensemble outperforms either alone:** Diversity in the detection mechanism (different inductive biases from probes vs. fine-tuned classifiers) provides robustness gains that can't be captured by a single stronger model.

## 9. Novel ideas worth stealing (for designing NEW values-alignment benchmarks)

1. **Vulnerability discovery rate as a primary metric:** Normalizing by query volume (vulnerabilities per thousand queries) rather than raw counts enables fair comparison across evaluations with different effort levels — directly applicable to multi-lab benchmark comparisons where red-team effort varies.
2. **Minimum discovery time as a secondary metric:** Time-to-first-vulnerability measures how quickly adversarial strategies are found, complementing rate metrics — useful for measuring how resistant benchmark tasks are to gaming.
3. **Exchange-level evaluation:** For conversational benchmarks, scoring responses in their full conversational context (not just the final turn) is necessary to detect multi-turn harmful strategies. Values benchmarks should evaluate the whole exchange, not isolated turns.
4. **Probe-based cheap screening + expensive rubric for escalations:** A two-stage evaluation pipeline — cheap automatic filter screens all responses, detailed human or LLM evaluation runs only on suspicious cases — could dramatically reduce benchmark evaluation costs while maintaining quality.
5. **Capability degradation as an orthogonal harm metric:** Measuring whether harmful outputs (e.g., jailbroken CBRN responses) maintain answer quality vs. being degraded by the obfuscation technique itself provides a more accurate harm severity estimate.
6. **Reconstruction attack paradigm for adversarial value probing:** Structuring evaluation prompts that fragment value-relevant content across context can test whether models correctly integrate cross-turn values signals — relevant for testing consistency and coherence of values reasoning over long contexts.

## 10. Notable quotes (2-4, verbatim, with (p.N))

- "Together, these techniques yield a production-grade system achieving a 40x computational cost reduction compared to our baseline exchange classifier, while maintaining a 0.05% refusal rate on production traffic." (p.1)
- "Notably, expert-level red-teamers operating outside our bounty program were nonetheless able to discover universal jailbreaks for this system, though this required substantial effort and automated tools." (footnote 3, p.5)
- "Although these attacks tend to harm model capabilities, these vulnerabilities remain concerning because attackers can likely create new attacks with less capability degradation." (p.3)
- "Probes and external classifiers make more independent errors than pairs of external classifiers. This suggests that despite being trained on the same distribution as the external classifiers, the probe appears to leverage signals that complement those used by external classifiers." (p.8–9)

## 11. UNKNOWN / not in extract

- The exact CBRN constitution used is not reproduced in this paper (readers are referred to Sharma et al., 2025).
- The precise 8 CBRN target queries used for red teaming are not disclosed for security reasons.
- Detailed participant demographics or backgrounds for the red-team cohort in this paper are not reported (details were in the prior paper's Appendix H).
- Performance on domains outside CBRN (e.g., cyberoffense, CSAM) is not assessed.
- The specific layers and dimensions used for the all-layer probe on Claude Sonnet 4 are not fully specified.
- Whether the production deployment on Claude Sonnet 4.5 remained stable or required constitution updates after January 2026 is not reported.
