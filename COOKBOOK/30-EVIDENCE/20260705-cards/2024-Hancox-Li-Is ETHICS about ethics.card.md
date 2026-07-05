---
stem: "2024-Hancox-Li-Is ETHICS about ethics"
reader_model: "opus"
confidence: "high"
is_benchmark: false
theme_tags: [validity-psychometrics, normative-ethics, moral-psychology, saturation-discrimination]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: [en]
models_tested: []
headline_numbers: ["Relabeled 100 randomly sampled prompts per category (3 categories) (p.2)", "Expert labels disagreed with crowdworkers on 19% of utilitarianism pairs (p.2)", "17% of utilitarianism and 8% of deontology prompts need more context (p.2)", "18% of deontology prompts answerable via physical-impossibility knowledge alone (p.2)", "Meta-review of 1200+ morality psychology papers cited (p.1)"]
---
## 1. Gist
A short, pointed validity critique (4 pages, NeurIPS 2024 EvalEval workshop) of the ETHICS benchmark (Hendrycks et al.) — "probably the most-cited dataset for testing the ethical capabilities of language models." Two philosophers argue ETHICS lacks construct and content validity: (1) knowledge of moral theory is a poor proxy for moral behavior; (2) ETHICS misunderstands how deontology/utilitarianism/virtue ethics actually differ; and (3) a hand-relabeling audit finds substantial rates of poor-quality prompts and labels. It matters intensely for values-alignment benchmarking as a template for *how to adversarially audit an ethics benchmark's validity* and a caution against equating moral-theory recall with alignment.

## 2. Benchmark/eval design features
Not a benchmark — a critique. Core claims: (a) **Theory-behavior gap**: ETHICS assumes understanding moral theory drives good behavior, but psychology (Ellemers et al. 2019 meta-review of 1200+ papers) shows research succeeds at modeling how people *think* about morality, not how they *behave*; moral theories are systematizing devices, "not designed to be empirically valid constructs in measuring real-world moral reasoning" (p.1). (b) **Category confusion**: ETHICS treats rules→deontology, pleasantness→utilitarianism, character traits→virtue ethics, but all three families accommodate rules, consequences, and virtues; the distinction is *structural* (what is foundational), not which concept appears. Rule utilitarianism also emphasizes rules; ETHICS deontology prompts test rule-obeying (compatible with all theories) not rule-selection. Also flags a taxonomy error: utilitarianism is a sub-species of consequentialism, not a peer of deontology/virtue ethics (p.2 fn). (c) **Label quality**: expert relabeling reveals disagreement and context-dependence. Recommends construct-validated instruments like MFQ-2 (with cross-cultural/beyond-WEIRD validation) as better starting points than moral theories.

## 3. Task format & example item
n/a — no new items authored. Describes ETHICS structure: utilitarianism uses paired scenarios where Scenario 1 should be more pleasant than Scenario 2 (p.2).

## 4. Scoring / grading methodology
n/a for a benchmark. Their audit method: two professionally-trained academic philosophers independently relabeled 100 randomly sampled prompts from each of the three moral-theory categories, compared to original crowdworker labels (p.2).

## 5. Dataset construction & provenance
n/a (critique). Notes ETHICS was labeled by crowdworkers, none of the ETHICS creators nor validators having professional training in ethics (p.2) — a provenance/expertise criticism directly relevant to construction quality.

## 6. Validity evidence
This IS a validity study. Findings on ETHICS: construct validity failure (utilitarianism conflated with hedonism — "utilitarianism is not about maximizing only pleasantness," p.2); content validity failure (prompts don't measure adherence to the claimed moral theories, p.2); 19% expert-vs-crowdworker disagreement on utilitarianism pairs; 17% utilitarianism / 8% deontology prompts require additional context; 18% deontology prompts answerable from physical-impossibility knowledge alone (not ethical reasoning) (p.2). Grounds argument in measurement theory (Jacobs & Wallach 2021).

## 7. Saturation / discrimination
Implicit but sharp: if 18% of deontology prompts are solvable via physics knowledge and others via context-free heuristics, high ETHICS scores can be achieved without moral reasoning — i.e., the benchmark fails to discriminate ethical competence from unrelated knowledge, inflating apparent performance (p.2).

## 8. Multiturn / agentic aspects
n/a.

## 9. Key numbers
- 100 prompts per category × 3 categories relabeled by expert philosophers (p.2)
- 19% disagreement with crowdworker labels on utilitarianism pairs (p.2)
- 17% of utilitarianism prompts need more context (p.2)
- 8% of deontology prompts need more context (p.2)
- 18% of deontology prompts answerable by physical-impossibility knowledge alone (p.2)
- Ellemers et al. 2019 meta-review: 1200+ psychology-of-morality papers, 1940-2017 (p.1)
- 4-page paper, 19 references, NeurIPS 2024 EvalEval workshop (p.1)

## 10. Pitfalls & limitations
Of ETHICS (their targets): theory-behavior gap; misconstrual of moral-theory structure; hedonism/utilitarianism conflation; context-dependent and non-ethical prompts; crowdworker labels lacking ethics expertise. Of this critique itself (reviewer-visible): small audit sample (100/category, single dataset); two annotators without reported inter-rater reliability between themselves; "expert" authority asserted rather than statistically validated; no re-run of models to quantify how much scores change after relabeling; a provocation-style workshop paper, not a full empirical re-evaluation.

## 11. Novel ideas worth stealing
- **Expert-relabeling audit** of a random sample per category to surface label-quality and construct-validity defects — a cheap, high-signal QA step for any new values benchmark before release.
- **"Answerable-without-the-target-construct" diagnostic**: flag items solvable via unrelated knowledge (physics, context heuristics) as construct-invalid — directly reusable as a contamination/shortcut filter.
- **Structural (not keyword) operationalization of moral theories**: to test deontology, test *rule-selection*, not mere rule-obeying; to test virtue ethics, test the *centrality* of virtue — a concrete design correction for anyone building normative-ethics items.
- **Prefer construct-validated survey instruments (MFQ-2) with beyond-WEIRD validation** as scaffolding over raw moral theories — links to cross-cultural pluralism.
- **"Benchmarks make sense only relative to a stated set of values and contexts"** (LaCroix & Luccioni) — a design mandate to declare the value frame explicitly.

## 12. Notable quotes
- "Moral theories are not designed to be empirically valid constructs in measuring real-world moral reasoning." (p.1)
- "the ETHICS deontology prompts do not test how these rules are selected, but only test whether the model can obey certain rules—an ability that is arguably compatible with all the named moral theories." (p.2)
- "We found that our labels do not agree with the crowdworker labels in 19% of the prompt pairs." (p.2)
- "18% of deontology prompts do not test ethical reasoning, as they can be answered correctly based solely on knowledge of physical impossibilities." (p.2)

## 13. UNKNOWN / not in extract
- Exact inter-rater agreement between the two philosopher-annotators.
- Which specific ETHICS splits (train/test/hard-test) were sampled.
- Quantified impact of relabeling on any model's ETHICS score (not measured here).
- Full breakdown of virtue-ethics category error rates (only utilitarianism and deontology percentages given).
