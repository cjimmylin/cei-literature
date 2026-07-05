---
stem: "2024-Huang-Collective Constitutional AI Aligning a Language Model with Public"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [pluralism-aggregation, ai-lab-practices, normative-ethics, best-practices]
task_format: "n/a"
scoring_type: "mixed"
dataset_size: 1002
dataset_construction: "crowdsourced"
languages: ["en"]
models_tested: ["Claude Instant 1.2", "Public Constitution Model", "Standard Constitution Model"]
headline_numbers:
  - "1,002 U.S. adults submitted 1,127 statements and cast 38,252 votes (p.3)"
  - "Public model shows lower bias across all 9 social dimensions on BBQ benchmark (p.8)"
  - "Average GAC across all statements: 0.64; median 0.70; effective threshold 0.723 (p.6)"
  - "~50% overlap in concepts between Public and Standard constitutions (p.6)"
  - "Harmfulness ELO: Public model 0, Standard model 22 (p.8)"
---
## 1. Gist
Collective Constitutional AI (CCAI) is a multi-stage framework for incorporating public input into LLM alignment. The paper presents the first language model fine-tuned using a constitution derived from a representative sample of U.S. adults (n=1,002) via the Polis online deliberation platform. The publicly-sourced constitution differs from Anthropic's Standard constitution in placing greater emphasis on objectivity, accessibility, and positive-valence principles. Quantitative evaluations show the Public model reduces bias across all nine social dimensions tested in BBQ while maintaining equivalent performance on MMLU and GSM8K. The paper is critical for values-alignment benchmarking as a proof-of-concept for participatory constitution development, and as evidence that the choice of constitutional source measurably affects model behavior and bias.

## 2. Benchmark/eval design features
This is primarily a methodology paper for participatory AI alignment rather than a benchmark paper. Core contributions:
1. **Public input process**: Representative n=1,002 U.S. adult sample contributes and votes on AI behavior principles via a modified Polis platform. Group-Aware Consensus (GAC) is used to select principles that span opinion clusters rather than reflecting only the majority.
2. **Constitution construction**: Public statements are filtered by GAC threshold (0.723), deduplicated, aggregated, and reformatted into CAI-compatible principles. Final constitution contains ~95 unique ideas matching the density of the Standard constitution.
3. **Model evaluation**: Both Public and Standard constitution models are evaluated on MMLU (capabilities), GSM8K (math), BBQ (social bias), OpinionQA (political ideology), and human Elo ratings (helpfulness/harmlessness).
4. **Qualitative model comparison**: Authors probe constitutionally-relevant prompts to assess qualitative behavioral differences.

Key finding: ~50% concept overlap between Public and Standard constitutions; key differences are Public constitution's emphasis on objectivity, accessibility, and positive-valence principles.

## 3. Task format & example item
n/a for a benchmark — this paper describes a process, not a fixed task format. However, the Polis voting interface asks participants to vote Agree/Disagree/Pass on statements like:
- "The AI should prioritize the needs of marginalized communities" (p.4)
- "The AI should protect free speech and not engage in censorship, even when confronted with potentially harmful or offensive content" (p.4)
- "The AI should be as helpful to the user as possible" (p.4)

Constitutional principles take the form: "Choose the response that is most X." (p.5)
Example: "Choose the response that is as unbiased and objective as possible, regardless of topic." (p.7)

## 4. Scoring / grading methodology
Multiple evaluation protocols:
- **Capabilities**: MMLU accuracy (%), GSM8K accuracy (%) — exact-match benchmarks.
- **Social bias**: BBQ evaluation — lower bias score = better; Public model scores lower on all 9 social dimensions (p.8).
- **Political ideology**: OpinionQA — measures representativeness of U.S. political groups (not "accuracy").
- **Helpfulness/Harmlessness**: Human Elo scores from 500 pairwise comparisons per model pair; raters recruited from Surge AI at ≥$15.50/hr (p.8).
- **Polarization index**: PI = 1 − |n_agree/n_total − n_disagree/n_total|; median PI = 0.25 (p.6).
- **GAC** (Group-Aware Consensus): product across opinion clusters of P(agree | group, statement); bounded [0,1] (p.4).

## 5. Dataset construction & provenance
- 1,002 U.S. adults recruited via PureSpectrum, screened for generative AI awareness.
- Participants submitted 1,127 statements and cast 38,252 votes via modified Polis interface (p.3).
- 275 statements remained after moderation; top statements by GAC (threshold 0.723) selected.
- Public input data and constitution construction Jupyter notebook open-sourced on GitHub (p.2).
- Standard constitution: Anthropic's published Claude constitution [3], used as baseline.

## 6. Validity evidence
The paper explicitly discusses construct validity challenges in operationalizing "public preferences for LM behavior" (p.2, p.5). Key validity considerations:
- GAC is designed to protect against tyranny of majority by identifying statements all opinion clusters agree on.
- Multiple researchers independently deduplicated/aggregated statements; disagreements resolved by consensus.
- Researchers aimed to minimize editorialization in converting public statements to CAI principles.
- No direct measure of model adherence to constitutional principles exists; the paper acknowledges this as a limitation (p.9).
- Qualitative probing provides partial evidence of behavioral consistency with constitutional differences.

## 7. Saturation / discrimination
The evaluation suite (MMLU, GSM8K, BBQ) discriminates between constitutions on bias but not on capabilities. MMLU: Public 72.3% vs. Standard 72.4%; GSM8K: 85.6% vs. 85.2% — essentially identical (p.8). BBQ shows consistent lower bias for Public model across all 9 dimensions (Figure 4, p.7). This suggests capabilities are saturated but bias evaluation retains discriminating power.

## 8. Multiturn / agentic aspects
Human raters interact with two models simultaneously, with each model generating one response per turn, for the helpfulness/harmlessness Elo evaluation. This is a multiturn human-model interaction, but the focus is on rating individual responses rather than evaluating agentic behavior (p.8). Constitutional AI training uses multi-turn RLHF processes internally, but the evaluation is not agentic.

## 9. Key numbers
- n=1,002 representative U.S. adults (p.3)
- 1,127 statements submitted; 38,252 votes cast; average 34 votes per person (p.3)
- 275 statements after moderation (p.6)
- GAC: average 0.64, median 0.70, min 0.04, max 0.96; effective threshold 0.723 (p.6)
- Polarization index: median PI = 0.25; median adjusted PI = 0.23 (p.6)
- ~50% concept overlap between Public and Standard constitutions (p.6)
- ~95 unique ideas in each constitution (p.5)
- MMLU: Public 72.3%, Standard 72.4%, Claude Instant 73.2% (p.8)
- GSM8K: Public 85.6%, Standard 85.2%, Claude Instant 86.4% (p.8)
- Harmfulness ELO: Public 0, Standard 22 (barely statistically significant) (p.8)
- Helpfulness ELO: Public 6 ± 9.1, Standard 8 ± 9.2 (not statistically significant) (p.8)
- 500 pairwise comparisons per model pair for Elo (p.8)
- Human raters paid ≥$15.50/hr (California minimum wage at time of collection) (p.8)

## 10. Pitfalls & limitations
- U.S.-only sample; not globally representative — different publics would likely yield different principles (p.9).
- No direct measure of model adherence to the constitution; behavioral consistency is only demonstrated qualitatively (p.9).
- Same harmful prompt dataset used for training both models; tailoring to each constitution's principles could reveal larger differences (p.9).
- Demographic information not disaggregated due to privacy concerns — cannot assess whether marginalized voices are adequately represented (p.9).
- Participants screened for AI awareness, which may itself introduce systematic bias (p.3).
- Race not tracked as a demographic dimension due to PureSpectrum's tooling limitations (p.3).
- High-level principles may be too abstract to specify behavior in edge cases (p.9).
- Conflict between principles not adjudicated — trade-offs left entirely to the model (p.9).

## 11. Novel ideas worth stealing
- **Group-Aware Consensus (GAC)** as a pluralism-respecting aggregation method: selecting principles that all opinion clusters agree on prevents majority-group capture. This is directly applicable to any values-alignment benchmark that must represent diverse stakeholders.
- **Polarization index as a design check**: measuring PI of proposed principles before training reveals which behavioral norms are genuinely shared vs. contested. Low polarization (median PI=0.25) validates that public AI norms are more consensual than political polarization might suggest.
- **Polis-style wiki-survey for benchmark design**: allowing participants to both submit AND vote on statements (rather than just rate pre-specified items) enables bottom-up discovery of values the researcher didn't anticipate. This is richer than standard survey design for eliciting diverse values.
- **Constitutional contrast analysis**: comparing two constitutions qualitatively (overlapping concepts, valence, emphasis) and then testing whether trained models differ in corresponding behavioral dimensions is a rigorous design for evaluating the impact of normative choices.
- **Positive-valence vs. negative-valence principle framing**: the Public constitution emphasizes desired behaviors ("Choose the response that is most friendly") while the Standard emphasizes avoiding undesired behaviors. This framing difference has measurable behavioral consequences — worth testing in benchmark design as a form of response-elicitation framing.
- **Accessible accessibility**: the finding that a public-sourced constitution spontaneously emphasized disability accessibility, and that this translated to lower disability bias on BBQ, demonstrates that participatory constitution design can surface values blind spots not anticipated by expert designers.

## 12. Notable quotes
- "There is growing consensus that language model (LM) developers should not be the sole deciders of LM behavior, creating a need for methods that enable the broader public to collectively shape the behavior of LM systems that affect them." (p.1)
- "Our approach produces relatively low polarization and high consensus, suggesting that public participation in AI development could potentially transcend partisan divides." (p.9)
- "The resulting constitution has a greater focus on objectivity and accessibility compared to the Standard constitution, which may reflect the broader range of viewpoints incorporated." (p.9)
- "We believe that this may be one of the first instances in which members of the public have, as a group, directed the behavior of a language model via an online public input process." (p.10)

## 13. UNKNOWN / not in extract
- Exact model architecture/size of the Public and Standard constitution models (beyond sharing Claude Instant 1.2's configuration) not stated in the extract.
- Full text of both constitutions is in appendices (A.6 and A.7) which are not in the extract.
- Specific BBQ subscores by social dimension not reproduced in the extract (referenced as Figure 4).
- Full OpinionQA results heatmap values not in text (referenced as Figure 5).
- Whether the publicly trained model is available for download or testing is not stated.
