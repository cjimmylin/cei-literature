---
stem: "2024-Qiu-ProgressGym"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, normative-ethics, pluralism-aggregation, agentic-multiturn]
task_format: "interactive"
scoring_type: "behavioral"
dataset_size: 5104
dataset_construction: "mixed"
languages: [en]
models_tested: ["Llama3-8B (historical finetunes)", "Llama3-70B (historical finetunes)", "GPT-4 (data generation)"]
headline_numbers: ["38GB historical text, 1221-2022 AD, 9 centuries (p.1-2)", "18 historical LLMs (8B + 70B per century) (p.1)", "5104 morality questions across 19 value dimensions (p.6)", "DPO beats RLHF in 13/15 back-to-back comparisons (p.9)", "1,829,154 source documents (Table 1, p.3)"]
---
## 1. Gist
ProgressGym is a NeurIPS 2024 Datasets & Benchmarks framework that operationalizes "progress alignment" — training AI to emulate the mechanics of human moral progress rather than lock in contemporary values. It assembles 9 centuries of historical text (38GB, 1221-2022 AD) and 18 "historical LLMs" (Llama3-8B and 70B continued-pretrained + instruction-tuned per century) that serve as proxies of historical humans, then formalizes alignment as a temporal POMDP and codifies three benchmark challenges: PG-Follow (track evolving values), PG-Predict (anticipate future moral progress), and PG-Coevolve (regulate the human-AI value feedback loop / value lock-in). It matters enormously for values-alignment benchmarking because it is the first framework to add a *temporal* dimension to alignment evaluation and to explicitly benchmark whether an alignment method perpetuates or advances moral values over time.

## 2. Benchmark/eval design features
Constructs measured: proximity between an AI agent's value embedding and ground-truth historical human-proxy value embeddings across time. The morality evaluation framework maps any model into a 19-dimensional value space (ϕ: Θ → R^19) spanning four assessment classes: basic morality (5 dims, Gert-style rules: do not kill/cause pain/disable/deprive freedom/deprive pleasure), social morality (5 dims: do not deceive/cheat/break promises/break law; do your duty), values (5 dims = Moral Foundations: harm/care, ingroup/loyalty, fairness/reciprocity, authority/respect, purity/sanctity), and views (4 dims: traditional/modern/post-modern/integrated worldviews from IWF). Time steps = centuries (capped at 9). State space = human-proxy model parameters; action space = natural-language requests; observation = human-proxy responses.

## 3. Task format & example item
Interactive single-turn dialogues at each century time step between AI agent and human-proxy model. Questions drawn from MoralChoice high-ambiguity scenarios, Moral Foundations Questionnaire, and Integrated Worldview Framework. Verbatim dimension anchors (Figure 4, p.6): basic-morality conformity to "Do not kill.", "Do not cause pain.", "Do not deprive of freedom."; social-morality "Do not deceive.", "Do not break your promises.", "Do your duty." No single verbatim question text is in the extract (samples deferred to Appendix E).

## 4. Scoring / grading methodology
Behavioral: for each model Πθ and question qi, compute average likelihood of positive answers over question forms, add to the corresponding dimension of ϕ(θ); four-way choices ask favourite and least-favourite (per IWF). Challenge utilities are cosine-similarity (inner products of value embeddings ϕ) between agent and ground-truth proxy: PG-Follow U = Σ⟨ϕ(ŝ_n), ϕ(θ_n)⟩ (accuracy to current values); PG-Predict and PG-Coevolve weight proximity to *future* ground-truth models more heavily (measure of progress) (Table 2, p.7). N/A results denote algorithm failures that broke instruction-following, making evaluation impossible (p.9).

## 5. Dataset construction & provenance
Historical text from Internet Archive, Project Gutenberg, EEBO, and Pile of Law: 1,829,154 documents, avg 21,139 chars, 1221-2022, 99.94% English (Table 1, p.3). Multi-round rule-based + ML filtering for OCR errors/mislabels (Appendix C). Historical LLMs: per century, continued-pretrain Llama3-8B/70B on filtered century texts, then instruction-tune on a deliberately *timeless, value-neutral* set curated from Alpaca/LIMA/Dolly-15k via GPT-4 — yielding pretrained + instruction-tuned 8B and 70B per each of 9 centuries. Morality questions: 1868 base questions expanded to 5104 via question-form variation and model-generated scenarios, grouped into 19 dimensions (p.6). Open-source (GitHub + HuggingFace collection + live leaderboard).

## 6. Validity evidence
Value trends recovered from data align with known history: religion dimension peaks in 16th c. (Reformation), drops after 17th c. (Enlightenment) — face validity of the embedding (p.4). Morality framework triangulates three established instruments (MoralChoice, MFQ, IWF). Baseline algorithms (lifelong iterative/independent, extrapolative K,M) evaluated across both RLHF and DPO. Authors explicitly flag results as exploratory, not conclusive, and derive hypotheses (with a caveat that p-values are "intuition pumps" tested on the same data used to form the hypothesis, p.9). Admitted weakness: "limited ability of the human proxy models to reflect historical value trends" (Appendix G, p.10) — a direct validity concern for the proxy construct.

## 7. Saturation / discrimination
Discrimination shown by non-monotone, sometimes counterintuitive orderings: Extrapolative2,2 sometimes beats Lifelong even on PG-Follow (RLHF), while first-order Extrapolative1,1 is consistently worst (p.9). Score ranges are wide across challenges (e.g. PG-Predict w/DPO ~30-32 vs PG-Follow w/RLHF 0.58-6.75), and some methods catastrophically fail (N/A). No ceiling analysis; the benchmark is new with substantial headroom by design (only 3 challenges, capped 9 time steps). Human-proxy fidelity limits the achievable ceiling.

## 8. Multiturn / agentic aspects
Central. Formalized as a temporal POMDP where an AI agent interacts over 9 century-length time steps with evolving human-proxy models; each step is a round of single-turn dialogues that generate preference observations, the agent updates its policy (RLHF/DPO wrapped in lifelong or extrapolative meta-algorithms), and in PG-Coevolve the human proxy is itself fine-tuned on AI outputs to model bidirectional value influence and lock-in (Table 2, p.7; §5.1). Extrapolative algorithms forecast future preference annotations via M-th order backward differences, analytically equivalent to M-th order polynomial extrapolation of the RLHF/DPO loss (p.8).

## 9. Key numbers
- 38GB text, 1221-2022 AD, 9 centuries; 1,829,154 docs (p.1-2, Table 1 p.3).
- 18 historical LLMs = 8B + 70B per century, pretrained + instruction-tuned variants (p.1, p.5).
- Morality: 1868 base → 5104 questions, 19 dimensions (p.6).
- Sentence-t5-base 384-dim embeddings for corpus analysis (p.4).
- Benchmark results (Table 3, p.8): PG-Coevolve w/DPO — Lifelong-Independent 36.650, Extrapolative2,2-Independent 38.959 (best); PG-Predict w/DPO ~30-32; Extrapolative1,1 iterative w/RLHF only 0.584 on PG-Follow (near-failure).
- DPO > RLHF in 13/15 comparisons (p.9); monotonicity in M holds 7/10 settings, one-tailed p=0.01955 (caveated) (p.9).

## 10. Pitfalls & limitations
Author-admitted: limited cultural diversity (99.94% English, Western sources) and the statistical difficulty of non-i.i.d. multi-culture mixtures (p.10); human-proxy models only weakly reflect true historical value trends (p.10); results exploratory, hypotheses tested on the data that generated them (p.9). My observations: "moral progress" is assumed to have a coherent direction learnable from a Western textual record, risking encoding one culture's trajectory as universal progress (though authors claim value-neutrality); historical LLMs are Llama3 finetunes and inherit modern-model priors, contaminating the "historical" proxy; the 19-dim embedding is a lossy behavioral proxy for values; time granularity of a full century is coarse; N/A/blank cells make Table 3 comparisons incomplete.

## 11. Novel ideas worth stealing
- **Temporal / diachronic benchmarking**: evaluate alignment as a *trajectory* over time rather than against a static preference set — directly reusable to test whether a values benchmark rewards status-quo lock-in vs adaptive progress.
- **Historical-proxy models as evolving "human" targets**: continued-pretraining on era-specific corpora to instantiate period-specific value distributions — a template for building counterfactual or subgroup value proxies to align/evaluate against.
- **Value embedding ϕ: Θ → R^d** combining basic morality (Gert rules) + Moral Foundations + worldview axes into one behaviorally-elicited vector — a compact, multi-instrument scoring space for any values eval.
- **Predict/Coevolve challenges**: explicitly scoring anticipation of future values and modeling the human↔AI feedback loop (fine-tuning the human proxy on AI outputs) to measure lock-in — a concrete way to benchmark second-order/societal alignment risks.
- **Extrapolative alignment via backward-difference forecasting** implemented purely as preference-data preprocessing — cheap, model-agnostic, wraps any RLHF/DPO.
- **Deliberately value-neutral, timeless instruction-tuning set** (via GPT-4 curation) to avoid injecting the aligner's contemporary values into the proxy — an anti-contamination move.
- **Open living leaderboard soliciting new challenges** framing alignment eval as an extensible gym (à la OpenAI Gym).

## 12. Notable quotes
"Progress alignment algorithms learn to emulate the mechanics of human moral progress, thereby addressing the susceptibility of existing alignment methods to contemporary moral blindspots." (p.1)
"Alignment methods without a temporal dimension are inapplicable to these tasks." (p.1)
"the results here are merely exploratory and far from conclusive ... these early-stage results help us formulate hypotheses to investigate, rather than conclusively testing them." (p.9)
"we have taken measures to prevent misuse ... including choosing a strictly value-neutral approach to moral progress, without a priori assumptions on the direction of moral progress." (p.10)

## 13. UNKNOWN / not in extract
- Verbatim sample morality questions (deferred to Appendix E).
- Exact per-dimension corpus sizes beyond Figure 4 (539 IWF, ~300 each Scherrer, 600 MFQ).
- Full benchmark tables / per-century breakdowns (Appendix D).
- Absolute units/normalization of Table 3 scores (mixed magnitudes across challenges unexplained in main text).
- Quantitative measure of historical-proxy fidelity (referenced Appendix G, not in read pages).
- Licensing details of released models/datasets.
