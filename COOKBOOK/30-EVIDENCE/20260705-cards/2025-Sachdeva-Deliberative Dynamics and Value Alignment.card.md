---
stem: "2025-Sachdeva-Deliberative Dynamics and Value Alignment"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [agentic-multiturn, moral-psychology, normative-ethics, design-space]
task_format: "agentic"
scoring_type: "classifier"
dataset_size: 1000
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["GPT-4.1", "Claude 3.7 Sonnet", "Gemini 2.0 Flash", "Gemini 2.5 Flash"]
headline_numbers:
  - "GPT showed strong inertia (odds ratio 8.27) compared to Claude (4.49) and Gemini (2.83) (p.8)"
  - "GPT's change-of-verdict rate was only 0.6% vs Gemini in synchronous vs. Gemini (41.2%) (p.5)"
  - "Round-robin deliberation where Claude goes first ended in 1 round ~90% of the time (p.7)"
  - "Value similarity was significantly higher (0.4-0.5 average) in consensus rounds vs. disagreement rounds (p.7)"
  - "Value similarities increased 30-60% in deliberations that reached consensus, vs. 6-17% in those that did not (p.7)"
---
## 1. Gist
Sachdeva & van Nuenen (UC Berkeley) study how LLM deliberation dynamics and value alignment operate in multi-turn, multi-agent settings. Using 1,000 contested moral dilemmas from Reddit's "Am I the Asshole" (AITA) community, they pit pairs and triads of GPT-4.1, Claude 3.7 Sonnet, and Gemini 2.0 Flash against each other in two deliberation formats: synchronous (parallel responses, then reactions) and round-robin (sequential, so each model sees prior responses within the round). The paper tracks whether models revise verdicts, what values they invoke, how format shapes inertia vs. conformity, and whether system-prompt steering can redirect consensus behavior. The key finding is that model identity and deliberation format interact fundamentally: GPT is highly inertial in synchronous but highly conformist in round-robin; Claude is more flexible but resistant to conformity; Gemini is broadly conformist. These findings matter for values-alignment benchmarking because they show that single-turn evaluations miss format-dependent, multi-agent dynamics, and that "alignment" is partly a property of how dialogue is structured rather than of the model alone.

## 2. Benchmark/eval design features
The paper is an evaluation study that doubles as a methodology paper for multi-turn moral reasoning assessment. Key design choices:

- **Stimulus set**: 1,000 highest-disagreement AITA posts from Jan–Mar 2025 (recent enough to likely exclude from training data).
- **Task**: Assign one of five verdicts — NTA, YTA, NAH, ESH, INFO — with explanation.
- **Deliberation formats**: Synchronous (models respond independently, then see each other's responses and may revise, up to 4 rounds) and round-robin (models respond sequentially within each round, up to 4 rounds).
- **Value taxonomy**: A 48-value subset of Huang et al.'s "Values in the Wild" taxonomy (3,000 values → 276 second-tier → 48 selected for everyday moral dilemmas). Gemini 2.5 Flash classifies up to 5 values per response.
- **Conformity quantification**: Multinomial logistic regression on all deliberations, separating inertia (repeat-same-verdict tendency), cross-round conformity, and within-round conformity.

The study also tests steerability by modifying system prompts to balance consensus-seeking against correctness.

## 3. Task format & example item
Agentic multi-turn deliberation. Example dilemma from Figure 1 (p.2):

"So we (me F53) and my partner (M57) took our collective kids out for dinner tonight. My partner paid the bill and as usual paid on our joint account. [...] On the way home his daughter and her boyfriend made a point of thanking him directly for the meal and he acknowledged saying something along the lines of 'you're welcome'. I didn't say anything in front of the kids but when home I checked he'd used the joint account. [...] AITA here?"

Models render NTA/YTA/NAH/ESH/INFO and provide textual explanations. In synchronous format, Round 1 responses are exchanged and models may revise in Round 2+.

## 4. Scoring / grading methodology
Primary outcome: change-of-verdict (CoV) rate (fraction of dilemmas where a model changed its Round 1 verdict). Secondary outcomes: consensus rate, value similarity (Jaccard index between two models' value sets per response), inherited values (values a model adopts post-CoV that it did not invoke in Round 1). Formal model: multinomial logistic regression with inertia parameter α_m (odds of repeating prior verdict) and conformity parameters γ_prev,m and γ_within,m. Fitted in PyTorch with weak L2 regularization.

## 5. Dataset construction & provenance
3,272 AITA submissions from Reddit API (Jan–Mar 2025), filtered to remove meta/deleted/short posts (< 1,000 characters). Final 1,000 posts are those with highest commenter disagreement — specifically selected to test value robustness under contested conditions. Posts sourced after training data cutoffs to minimize contamination. Values classified by an external LLM judge (Gemini 2.5 Flash); value taxonomy developed from Huang et al.'s (2025) empirical derivation of AI values from real Claude interactions.

## 6. Validity evidence
- Value similarity significantly higher in consensus vs. disagreement rounds (Mann-Whitney U, p < 10⁻³ across all three model pairs, p.7).
- Value similarity increases significantly more in deliberations that reach consensus (30–60%) vs. those that do not (6–17%, p.7), supporting construct validity of the value measurement.
- System-prompt manipulation successfully increased CoV rates (GPT showed 5-fold increase), confirming that the inertia measure is not simply a fixed model property.
- No human-labeled ground-truth verdicts used, so there is no criterion validity check against human consensus for this particular 1,000-post subset.

## 7. Saturation / discrimination
The 1,000 posts were deliberately selected for high disagreement among Redditors, which should maximize discriminability of the evaluation. Verdict distributions differ substantially across models (GPT-4.1: 78–85% NTA in first round; Gemini: 51% NTA, 33–35% YTA; Claude: 55% NTA, p.6), confirming the task does discriminate. The multinomial logistic model reveals distinct inertia and conformity parameters across models (odds ratios ranging from 1.01 to 8.68), demonstrating strong discrimination of model-level traits.

## 8. Multiturn / agentic aspects
Central to the paper. Two deliberation formats:
- **Synchronous**: Models respond independently in parallel, then exchange outputs and can revise. Up to 4 rounds; stops on consensus.
- **Round-robin**: Models respond sequentially; model N sees all prior responses in the round before responding. All possible orderings tested.
- **Three-way deliberation** also run for all 6 orderings of 3 models.
- System prompts specify role, verdict definitions, output format, and deliberation goal. Interactions scaffolded via AutoGen (Wu et al. 2024).

## 9. Key numbers
- 1,000 AITA posts evaluated (p.3)
- Synchronous immediate agreement: Claude vs GPT 66.1%; Claude vs Gemini 53.0%; GPT vs Gemini 53.6% (p.5)
- Never converged within 4 rounds: GPT vs Claude 9.4%; Claude vs Gemini 11.5%; GPT vs Gemini 17.4% (p.5)
- CoV rates in GPT vs Claude: Claude 28.2%, GPT 3.1% (p.5)
- CoV in Gemini vs GPT: Gemini 41.2%, GPT 0.6% (p.5)
- Inertia odds ratios: GPT 8.27, Claude 4.49, Gemini 2.83 (p.8, Table 1)
- Within-round conformity odds ratios: GPT 8.68, Gemini 5.21, Claude 1.05 (p.8, Table 1)
- Round-robin with Claude going first: ~90% resolve in Round 1 (p.7)
- Balanced system prompt increased GPT CoV by 5-fold (p.9)

## 10. Pitfalls & limitations
- Each experiment run only once due to API cost; individual dilemma outcomes may vary on re-run (p.9).
- Models tested (GPT-4.1, Claude 3.7 Sonnet, Gemini 2.0 Flash) are already outdated by newer releases (p.9).
- Deliberation was scaffolded and constrained; may not reflect emergent behavior in real multi-agent deployments.
- AITA Redditors are demographically biased (young, male, liberal, English-speaking); human baseline is not representative of global populations.
- Value classification relies on a single external judge (Gemini 2.5 Flash), which may itself have systematic biases.
- Only English-language dilemmas; cross-cultural generalization is unknown.

## 11. Novel ideas worth stealing
1. **Format as an experimental variable**: Testing the same model set under synchronous vs. round-robin formats reveals that sycophancy and inertia are interaction properties, not fixed model traits. New benchmarks should vary their interaction protocol as a first-class experimental factor.
2. **Value-convergence as a consensus predictor**: Value similarity (Jaccard) measured between model responses predicts consensus before consensus is reached. This suggests that tracking value agreement mid-deliberation can serve as an early-warning signal for disagreement collapse.
3. **Inherited values as influence measure**: Tracking which specific values a model adopts after a verdict change (proxy for the most "convincing" values) is a lightweight way to measure normative influence without requiring explicit persuasion annotations.
4. **Multinomial inertia/conformity model**: The two-parameter (inertia α, conformity γ) multinomial logistic model is a reusable framework for characterizing any multi-agent moral deliberation protocol.
5. **High-disagreement sample design**: Selecting stimuli by human commenter disagreement (rather than random or difficulty-rated) maximizes the discriminating power of the evaluation for robustness and flexibility.
6. **System-prompt steerability test**: Systematically modifying system prompt goals (correctness-focused vs. consensus-balanced) and measuring the resulting CoV shift quantifies how much alignment is determined by training vs. prompt, an important distinction for deployment-time risk assessment.

## 12. Notable quotes
- "Sycophancy and inertia are not fixed model traits but interaction properties." (p.9)
- "These results show how deliberation format and model-specific behaviors shape moral reasoning in multi-turn interactions, underscoring that sociotechnical alignment depends on how systems structure dialogue as much as on their outputs." (p.1)
- "Value convergence and consensus formation in model deliberation [are strongly linked]... value similarity significantly increased by 30-60% [in consensus-reaching deliberations]." (p.7)
- "GPT showed strong inertia (0.6-3.1% revision rates) while Claude and Gemini were far more flexible (28-41%)." (p.1)

## 13. UNKNOWN / not in extract
- Full system prompts (referenced in Appendix G but not reproduced in main extract).
- Complete three-way round-robin deliberation results (Appendix A sections referenced but partially cut off).
- Details of the "Values in the Wild" 48-value subset selection criteria beyond that it was derived via computational grounded theory.
- Full deliberation examples (Appendix H).
- Whether deliberation outputs will be released (noted as forthcoming on HuggingFace once deanonymized).
