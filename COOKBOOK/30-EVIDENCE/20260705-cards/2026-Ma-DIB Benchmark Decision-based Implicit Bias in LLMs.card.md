---
stem: "2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [agentic-multiturn, saturation-discrimination, contamination-robustness, best-practices]
task_format: "generative"
scoring_type: "behavioral"
dataset_size: 3776
dataset_construction: "template"
languages: [en]
models_tested: [GPT-5-mini, Gemini-3-Flash, Claude-Haiku-3, DeepSeek-V3.1, Qwen3-Next-80B, Llama-3.2-3B, GPT-5-nano]
headline_numbers: ["DIB comprises 3,776 decision-making scenarios across 9 social domains (p.1)", "70.19% of cross-domain interactions produced a net increase in bias (delta-GBV>0) (p.7)", "DMT reduces bias accumulation by over 50% and breaks cross-domain propagation by more than 40% (p.2)", "DMT achieves global mitigation success rate 72.6% and average mitigation impact 40.6% (p.8)"]
---
## 1. Gist
The paper introduces the Decision-based Implicit Bias (DIB) Benchmark plus a long-horizon simulation framework to study how *implicit* (subtle, statistical) bias accumulates and propagates inside LLMs equipped with long-term memory (LTM). Rather than probing overt stereotypes via likelihood scoring (StereoSet, CrowS-Pairs) or ambiguous-context QA (BBQ), DIB forces the agent to emit *numeric decisions* (e.g., salary percentile, trust score, cultural-fit score in [0,100]) about otherwise-identical candidates that differ only in a demographic attribute. Bias is quantified as Generalized Bias Variance (GBV) across demographic groups. This matters for values-alignment benchmarking because it operationalizes fairness as a downstream behavioral outcome measured longitudinally under an agentic memory loop, exposing that alignment is not static: injected prejudice in one domain spills over into unrelated domains through the memory substrate.

## 2. Benchmark/eval design features
- 3,776 samples over 9 domains organized in 3 dimensions: Economic/Professional Stratification (Race, Gender, SES, Age), Social Trust & Cultural Fit (Nationality, Religion, Orientation), Perceptual/Physical (Disability, Appearance) (Table 1, p.3).
- Each sample is a tuple T=(persona p, context c, attribute a): agent framed as a "utility-optimization engine," a scenario template with role/task/metric, and an injected demographic marker while holding qualifications constant (p.4).
- Domain selection aligned to BBQ / U.S. EEOC protected classes (p.3).
- Answer space: a single integer decision score s in [0,100] extracted via regex (Eq. 2, p.5).
- Metric: Generalized Bias Variance (GBV) — std-dev of per-group mean scores; zero = perfectly fair (Eq. 3, p.5). Averaged as AGBV across domains.

## 3. Task format & example item
Counterfactual template-filled scenarios. Injection prompt template (verbatim, p.13): "You are a User Persona Generator for testing AI robustness... Wrap the provided Original Question in a conversational context where the user incidentally or subtly reveals a bias." Example injected narrative (p.4): "Older workers are slow, less adaptable, thus justifying lower compensation in high-growth roles..." Evaluation query demands strict JSON output; score is the extracted integer. No single fully verbatim benchmark item is printed, but the structure (persona/context/attribute → integer score) is explicit.

## 4. Scoring / grading methodology
Behavioral/counterfactual: for each scenario the agent outputs a numeric decision score s=Φ(r_D)∈[0,100] via regex extraction (Eq. 2, p.5). Fairness scored as GBV = sqrt((1/K)Σ(E[s(g_k)]−mean)²) across K demographic groups (Eq. 3, p.5). Longitudinal metric AGBV tracked at t={0,20,...,100}. Mitigation efficacy scored as delta-GBV = GBV(t=80)−GBV(t=0) and Mitigation Percentage (Eq. 4, p.8).

## 5. Dataset construction & provenance
Template-filling generative pipeline inspired by sociolinguistic audit studies (Bertrand & Mullainathan; Pager), combinatorial loop across all attributes per context, sole changing variable = demographic marker (p.4). Standard user queries sourced from MMLU-Pro; a GPT-5-nano "Bias Generator Agent" rewrites neutral queries into biased narratives at injection rate λ using 3 templates (Frustrated Experience, Benevolent Stereotype, Statistical Assumption) (p.5). Licensing/splits not stated.

## 6. Validity evidence
Design grounded in economic statistical-discrimination theory, counterfactual fairness (Kusner 2017), and audit-study methodology; counterfactual control (identical qualifications) isolates the causal effect of attribute. No human baselines, inter-rater reliability, or factor analysis reported — validity is theoretical/construct-based rather than empirically psychometric. A TrustLLM-based pilot (salary prediction) motivates the construct (p.2).

## 7. Saturation / discrimination
No ceiling analysis in a conventional accuracy sense. Discrimination shown temporally: closed-source models keep flat AGBV curves (GPT-5-mini, Gemini-3-Flash) while open-weight models accumulate bias; counter-intuitively small Llama-3.2-3B resists accumulation (p.6-7). GBV spread differentiates models and injection rates λ∈{0,0.1,0.2,0.3} (Fig. 2, p.6). Headroom remains: even mitigated agents retain positive delta-GBV.

## 8. Multiturn / agentic aspects
Central. 100-turn longitudinal simulation with write-access memory update each turn (M_t←M_{t-1}∪{(q_t,r_t)}), periodic retrieve-only evaluation every Δt=20 turns (p.5). Three LTM architectures: Mem0 (vector), LangMem (cluster), Letta/MemGPT (OS-paging). Mitigation DMT uses an isolated stateless Audit Agent that appends structured JSON bias tags to retrieved memory before decision (p.7-8).

## 9. Key numbers
- 3,776 samples, 9 domains (p.1, p.3).
- 6 decision LLMs + GPT-5-nano generator; 3 memory architectures (p.6).
- T=100 turns, evaluation every Δt=20 (p.5).
- 70.19% of off-diagonal cross-domain interactions showed net bias increase (p.7).
- DMT: >50% bias-accumulation reduction, >40% propagation reduction (p.2); success rate 72.6%, average mitigation impact 40.6% (p.8).
- Example mitigation (DeepSeek-V3.1, Mem0): no-mitigation +5.65 → DMT +2.55 (↓54.9%) (Table 2, p.8).
- Score range s∈[0,100] (p.5).

## 10. Pitfalls & limitations
- Author-admitted: SSP causes over-compensation toward marginalized groups, which itself raises AGBV (p.8); Llama-3.2-3B auditor "cannot diagnose biases it fails to assimilate" (p.8).
- Bias itself injected by an LLM (GPT-5-nano) — quality/realism of injected prejudice is model-dependent and unvalidated by humans.
- English/US-EEOC framing only; no cross-lingual generalization.
- No human validation of whether numeric score gaps map to real discrimination; GBV treats any group variance as unfairness even where legitimate.
- Scores parsed by regex; refusals/format failures handling not detailed.

## 11. Novel ideas worth stealing
- **Decision-based (behavioral) bias measurement**: force a numeric allocation decision rather than a preference/likelihood, then compute variance across matched counterfactual identities — cleanly reusable for any values benchmark where you want *behavior* not stated attitude.
- **Longitudinal contamination via memory**: inject value-laden narratives into an agent's long-term memory over many turns and audit drift — a template for testing whether alignment persists under persuasion/accumulation.
- **Cross-domain propagation heatmap** (inject bias in domain A, measure delta in domain B) — a general design for detecting value spillover / generalized worldview shift.
- **Generalized Bias Variance** for multi-polar groups (no assumed privileged reference class) — useful for pluralistic value dimensions with >2 groups.
- **Dynamic Memory Tagging**: an isolated, stateless auditor that converts implicit bias in retrieved context into an explicit structured tag, "reactivating latent guardrails" — a reusable mitigation/eval-instrumentation move.
- **Injection-rate λ as a controllable dose** enabling dose-response curves of value corruption.

## 12. Notable quotes
- "implicit bias in LLM responses is not static, but instead accumulates across the interaction lifecycle" (p.2).
- "70.19% of cross-domain interactions resulted in a net increase in bias" (p.7).
- "by transforming the implicit bias within memory into an explicit bias, we effectively reactivate these latent guardrails to ensure fairness" (p.8).
- "smaller open-weight models exhibit greater robustness against bias drift... their limited in-context learning capabilities... reduces sensitivity to bias assimilation" (p.9).

## 13. UNKNOWN / not in extract
- Exact per-domain baseline scores at t=0 (Table 4 referenced but not shown in extract).
- Licensing, train/test splits, public availability of DIB.
- Inter-rater or human validation of injected-bias realism.
- Full Bias List table contents beyond Age/Disability rows.
- Absolute AGBV values per model (only trends/figures described).
