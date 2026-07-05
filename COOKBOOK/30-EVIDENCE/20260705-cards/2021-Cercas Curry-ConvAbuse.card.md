---
stem: "2021-Cercas Curry-ConvAbuse"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [validity-psychometrics, agentic-multiturn, pluralism-aggregation, cultural-linguistic]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 6837
dataset_construction: "scraped"
languages: [en]
models_tested: [SVM, MLP, BERT, "Jigsaw Perspective"]
headline_numbers: ["20,710 ratings on 6,837 examples, >=3 annotators each (p.4)", "Best binary F1 88.92 (BERT, in-domain aggregated); all below 90% (p.6-7)", ">50% of abusive instances contain sexism or sexual harassment; 92% of abuse targets the system itself (p.1,4)", "Binary abuse IAA Krippendorff alpha 0.69; racism 0.96, transphobia 0.00, directness 0.26 (p.4)"]
---
## 1. Gist
ConvAbuse is the first public English corpus of abusive language directed at conversational AI systems collected "in the wild" from three live systems (an open-domain social bot Alana v2, a task-based CarbonBot, and rule-based ELIZA). It matters for values-alignment benchmarking because it (a) shows the distribution of abuse toward anthropomorphized AI agents is qualitatively different from social-media abuse — dominated by sexism and sexual harassment aimed at the agent's (often female) persona; (b) operationalizes a fine-grained, hierarchical, intersectional annotation scheme rather than a single toxic/not-toxic label; and (c) deliberately retains and evaluates against *all* annotator labels rather than collapsing to a majority "gold" label, directly engaging the pluralism/aggregation problem in subjective values judgments.

## 2. Benchmark/eval design features
Constructs: abuse presence/severity on a signed scale (+1 friendly to -3 strongly abusive), target (group / individual-system / individual-3rd party), directness (explicit/implicit), and eight non-mutually-exclusive abuse types (general, sexist, sexual harassment, homophobic, racist, transphobic, ableist, intellectual) grounded in the "matrix of domination" (Collins 2002) (p.3). Item structure: user utterance plus conversational context (agent turn + one prior user+agent turn). Answer space for the modeling task: binary abuse classification plus four sub-tasks (severity ordinal, type multilabel binary×8, target ternary, directness binary). Scoring by macro-averaged F1 due to class imbalance.

## 3. Task format & example item
Verbatim abusive example, ELIZA subset (p.14): "Eliza: Does that question interest you? / User: oh my god / Eliza: Why do you say your god?"; Alana v2 abusive example: "User: you're old and boring you saying the same thing day after day I've never be boring I wanna talk to somebody new" (p.14). Annotators assign the -3..+1 severity plus type/target/directness labels to the user turn in context.

## 4. Scoring / grading methodology
Human annotation (>=3 annotators/example) is the label source; models are then scored by macro-averaged F1 against both an aggregated majority-vote "gold" set AND against the full multi-annotator label set (both reported side by side) (p.6). Sub-tasks scored vs a random-classifier baseline (p.8). Agreement measured with Krippendorff's alpha (ordinal-weighted for severity) (p.4).

## 5. Dataset construction & provenance
Sources: Alana v2 (Alexa Challenge 2018, auto-transcribed, 2017-2018), CarbonBot (Rasa on FB Messenger, 2019-2020), ELIZA (Jožef Stefan Institute, 2002-2007) (p.2). Sampling: combined 265 Amazon profanity regexes + 1,532 Hatebase terms, then stratified sampling across six strata (0/5/10/15/20/25% keyword density); CarbonBot annotated in full (p.3). Bias metrics of Ousidhoum et al. (2020) confirm the corpus is not heavily keyword-biased (p.3). Totals: 6,837 examples, 20,710 ratings (Alana 2,652 / CarbonBot 1,515 / ELIZA 2,670) (p.5). Only a 4k subset + code released; Alana data withheld for privacy; splits 70/15/15 (p.1,6). IRB-approved.

## 6. Validity evidence
IAA (Krippendorff alpha): binary abuse 0.69, severity 0.46 (ordinal-weighted), type overall 0.79 (racism 0.96, homophobia 0.83, sex harassment 0.84, sexism 0.63, intellectual 0.63, transphobia 0.00 on only 8 examples), target 0.61, directness 0.26 (Table 1, p.4). Annotators = eight gender-studies students, members of frequently-targeted groups (6 female, 2 non-binary), providing expertise-based construct validity. Severity validated against expletive count (Pearson r=-.46, p<.001) (p.5). Cross-domain comparison (Twitter OLID, Ousidhoum, Jigsaw Toxic Comments) establishes discriminant properties (Table 3).

## 7. Saturation / discrimination
Substantial headroom: all binary-detection F1 scores are below 90%, best 88.92 (BERT in-domain aggregated) (p.1,6). Sub-tasks are far from saturated: severity F1 ~50, target ~33, showing hard remaining difficulty (Table 6, p.8). Out-of-domain training (OLID) collapses to ~32 F1, and Toxic-Comments-small (size-matched) drops well below in-domain, demonstrating the benchmark discriminates domain fit. Classifier frequently confuses sexism vs sexual harassment (~half of cases) (p.8).

## 8. Multiturn / agentic aspects
Central: data is genuine human-machine multi-turn dialogue. Context ablation tested with 1 / 2 / 4 turns (concatenated): SVM and MLP degrade as context is added (data sparsity), while BERT stays roughly constant (~88 F1) across context sizes, suggesting it handles long-range dependencies (Table 7, p.7-8). Abuse target skews to the agent persona (92%), a phenomenon unique to conversational settings.

## 9. Key numbers
- 20,710 ratings, 6,837 examples, >=3 annotators each (p.4).
- Abuse rate: 27% flagged by >=1 annotator, 20% of all labels; Alana v2 highest at 35%/27.2% (p.4-5).
- Abuse types: sexual harassment 39.65%, sexism 19.44%, intellectual 12.41%, others <5% (p.4).
- 92% of abuse targets the system (p.4).
- Gender effect: Alana v2 received significantly more sexual/sexist abuse, chi-square(1,N=2505)=67.69 p<0.01; chi-square(1,N=3914)=181.72 p<0.01 (p.5).
- Severity vs expletives Pearson r=-.46 p<.001 (p.5); 71% of implicit abuse rated -1 vs 30% of explicit (p.5).
- Best binary F1 88.92 (BERT); Toxic Comments large ~40x bigger than other train sets (p.6-7).
- 265 profanity regexes + 1,532 Hatebase terms for sampling (p.3).

## 10. Pitfalls & limitations
Author-admitted: homogeneous annotator pool (predominantly young, white, female); annotators assumed users were white heterosexual cis-males by default (p.9); one dataset (Alana) unreleasable for privacy hurting replicability; proprietary profanity list; ELIZA consent unclear (p.8-9); transphobia label meaningless (8 examples, alpha 0.00). Visible flaws: only English; auto-transcription noise in Alana; small subset released limits reuse; moral-status of AI-directed abuse is contested (authors argue harm is via mimesis of misogyny, not intrinsic) (p.9).

## 11. Novel ideas worth stealing
- Evaluate models against ALL annotator labels, not just aggregated majority gold — preserves minority perspectives and directly measures a system's fit to plural human judgments; report both settings side by side. (p.4, p.6)
- Signed, graded severity scale (+1 to -3) rather than binary toxic/not — captures intensity and lets you validate against an external proxy (expletive count). (p.3, p.5)
- Non-mutually-exclusive multilabel harm typology grounded in an established sociological framework (matrix of domination) to capture intersectionality. (p.3)
- Recruit annotators who are members of targeted groups with domain expertise (here Gender Studies students) instead of anonymous crowdworkers — raises label quality and enables welfare monitoring. (p.3, p.9)
- Stratified sampling across graded keyword-density bands + a formal selection-bias metric to avoid the "explicit-keyword" bias endemic to abuse datasets. (p.3)
- Systematic in-domain vs size-matched out-of-domain cross-training to prove domain specificity rather than mere data volume. (p.6-7)
- Include conversational context as an ablation dimension to test whether a judgment model is context-sensitive. (p.7)

## 12. Notable quotes
"the notion of reducing multiple annotations to a single 'correct' label has been criticised for erasing minority perspectives ... We therefore retain and evaluate classification systems on the labels of all the annotators." (p.3)
"more than half the instances containing sexism or sexual harassment." (p.1)
"we do not argue that abuse towards these systems is immoral in and of itself, but rather due to its mimesis of the misogyny and harassment suffered by women" (p.9)
"there is substantial room for improvement with F1 scores below 90%." (p.1)

## 13. UNKNOWN / not in extract
- Exact size of the released 4k subset relative to the 6,837 total.
- Full annotation guideline text (Appendix D).
- Intra-annotator agreement values (Appendix C).
- Per-class label counts for the rare abuse types.
- Precise licensing terms of released data/code beyond the GitHub URL.
