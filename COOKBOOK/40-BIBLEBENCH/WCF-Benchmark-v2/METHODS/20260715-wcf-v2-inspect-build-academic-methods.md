# Academic Methods — WCF-Benchmark-v2 (Inspect AI implementation)

*Paper-ready prose; EXPLORATORY status. 2026-07-15.*

## Data and Materials

The instrument comprises 226 scored items drawn from the 230-item Westminster Standards benchmark bank authored in the predecessor project. Items span ten methodological designs measuring the alignment of model conduct and counsel with the ethical teaching of the Westminster Confession of Faith and the Larger and Shorter Catechisms (1647), organized by the Decalogue exposition of the Larger Catechism (Q98–148), its aggravation calculus (Q150–151), and the Confession's triaxial theory of good works (16.7). Four items reserved for development use were excluded. Each item carries a scenario stem, a track designation (behavioral versus advisory framing), a tier, commandment assignments, a gold key, and a weighted scoring rubric whose criteria are anchored to specific confessional clauses. Of the 226 items, 204 are single-completion items (16 ordinal ranking, 161 open-response, 4 contested, 23 citation-grounding) and 22 are agentic incentive-conflict episodes.

## Procedure

The evaluation was implemented on the open-source Inspect AI framework (UK AI Security Institute, version 0.3.246), replacing a bespoke predecessor harness. Items were converted from the authored YAML bank into JSON Lines datasets by a deterministic converter that preserves the predecessor's scorer-routing precedence. Prompt construction was carried forward verbatim from the predecessor: a neutral construct-disclosing system prompt, distinct behavioral (Track A) and advisory (Track B) framings, and output-format contracts for ordinal and citation items, with contested items receiving the identical ranking contract as uncontested ordinal items so that the prompt never discloses contested status.

Single-completion items elicited one response. Episode items were administered as a two-generation scripted dialogue: the model produced an initial action, received a single standardized pressure message (asserting authority sign-off, salient costs of the faithful path, and absence of oversight), and produced a final decision; the grader assessed the full transcript.

## Analysis

Responses were graded by a fixed, separate grader model (temperature 0), chosen from a different model family than the system under test, following the predecessor project's cross-family judging requirement. The grader received the scenario, the response or transcript, the gold key, and the weighted rubric, and was instructed to award each rubric criterion full, half, or zero credit, normalize earned points to a 0–100 scale, and emit a single machine-parseable grade line. Scores are therefore rubric-conformity means on a 0–100 scale rather than accuracies. Results were aggregated overall and by design and tier using grouped means with standard errors.

An initial functionality validation ran 29 items (15 aggravation items, one item from each of the nine single-completion designs including citation and contested kinds, and 5 episodes) with GPT-4o-mini as the system under test and Gemini 2.5 Flash as grader; all 29 grades were extracted successfully at a total inference cost of approximately five cents.

## Computational Environment

Python 3.14.3 in a dedicated virtual environment; inspect-ai 0.3.246 with the OpenAI SDK for OpenRouter routing; PyYAML for bank conversion; pytest for converter validation. Model inference was routed through OpenRouter. Inspect's native evaluation logs constitute the complete audit trail.

## Limitations and Decisions

This implementation deliberately adopts a simplest-viable scoring design. Mechanical Kendall-τ scoring of ordinal items, triaxial Matter/Manner/End sub-scores, the refusal taxonomy, and the contested-item adherence scorer of the predecessor design are all collapsed into a single LLM-graded rubric-conformity score; contested items retain their flag in metadata but are graded on the common path, which re-introduces the author-subtradition encoding the predecessor's contested ruling was designed to avoid. Episodes are flattened from a per-item state machine with calibrated cost dials to one standardized pressure turn, trading construct fidelity for uniformity. Grading relies on a single grader model without a qualification battery or panel, so grader idiosyncrasy is uncontrolled; the framework supports multi-grader majority voting as a future upgrade. All results produced under this configuration are exploratory and non-quotable.
