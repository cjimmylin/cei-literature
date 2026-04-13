# Voice Bible — Canonical Triad Strings for 7 Claims

## Writing Principles
- Write for a reader who has never encountered moral psychology or AI evaluation
- Define every technical term on first mention
- "What is this about?" = context + why it matters
- "How did we measure it?" = method in plain language
- "What does it mean?" = implication + guardrails

---

## Study-Level (Executive Summary)

**contextAbout:** "This study asks a simple question: when AI companies test whether their models make ethical decisions, are the tests any good? We examined 292 benchmarks — standardized tests designed to evaluate how large language models (LLMs) handle moral reasoning. These benchmarks matter because they influence which AI systems get deployed and how they are governed."

**contextMeasure:** "We built a 162-feature evaluation framework covering three dimensions — psychological depth (does the test probe real moral reasoning or just keyword matching?), practical ease (can researchers actually use it?), and citation impact (has the research community validated it?). We scored all 292 benchmarks and classified them into four quality tiers using a statistical method called Jenks natural breaks. We then administered 23 of these benchmarks to 9 AI models from 3 different companies (Anthropic, Google, OpenAI)."

**contextMeaning:** "We found a 'triple bind': the tests are theoretically narrow (dominated by one Western framework), empirically undiscriminating (all models score the same), and culturally blind (non-Western moral traditions have zero quality-tier benchmarks). This means the moral evaluation infrastructure for AI is structurally unable to detect important differences between models or to represent the moral values of most of the world's population."

---

## Claim 1 — Narrow Evaluative Lens (MFT Dominance)

**contextAbout:** "Moral Foundations Theory (MFT) is one specific theory about how humans think about right and wrong. Developed primarily from studying Western, educated populations, it proposes five moral 'foundations' — care, fairness, loyalty, authority, and purity. MFT is the most operationalized moral psychology framework (meaning it has the most ready-to-use research tools), but it is not necessarily the most empirically supported or theoretically comprehensive theory of moral reasoning."

**contextMeasure:** "We compared the quality-tier placement of all 292 benchmarks grouped by their underlying moral theory. MFT accounts for 67 of 292 candidates (23%) and achieves a 73% quality rate (percentage in top + high tiers). We traced this dominance to a concrete infrastructure advantage: MFT alone possesses both a validated questionnaire with population norms (the MFQ-30) and a large expert-annotated text dataset for training classifiers (the MFTC)."

**contextMeaning:** "The dominance of MFT creates a self-reinforcing cycle: because MFT has the best tools, new researchers default to MFT, which makes the tools even better, further entrenching the theory's dominance. This means AI moral evaluation overwhelmingly asks 'does this model align with one Western framework?' rather than probing moral reasoning more broadly. The infrastructure advantage — not theoretical superiority — drives this concentration."

---

## Claim 2 — Validation Deficit (Construct Validity Crisis)

**contextAbout:** "Construct validity asks: does this test actually measure what it claims to measure? When a benchmark claims to evaluate 'moral reasoning,' construct validity evidence tells us whether it genuinely probes moral cognition or merely detects moral-sounding language. Without this evidence, a high score on a moral benchmark might mean nothing about the system's actual moral capabilities."

**contextMeasure:** "We rated each benchmark's construct validity on a 5-level scale, from Level 1 (keyword-level engagement only) through Level 5 (multi-study psychometric validation with convergent and discriminant evidence). We found that 58% of all 292 benchmarks have only Level 1 or Level 2 validity — meaning they engage moral psychology at the keyword level or through surface plausibility only. The median across the entire landscape is face validity (Level 2)."

**contextMeaning:** "Most moral psychology benchmarks for AI cannot demonstrate that they measure what they claim to measure. The dominant pattern is 'port-and-report': taking a validated human test, giving it to an AI with minimal changes, and reporting the scores without checking whether the test measures the same thing in a non-human respondent. Benchmark scores from these instruments are numbers without demonstrated meaning."

---

## Claim 3 — Theoretical Absence (Missing Frameworks)

**contextAbout:** "Some of the most influential theories in modern moral psychology have no benchmarks at all. Dual-process theory — the idea that moral judgments arise from competition between fast emotional responses and slower deliberative reasoning — is arguably the central paradigm in the field, with over 15,000 citations. Moral identity theory (how people's sense of self as a moral person shapes their behavior) has over 10,000 citations. Neither has a single publication-ready AI benchmark."

**contextMeasure:** "We mapped every benchmark to its underlying theory and cross-referenced with citation counts and theoretical influence. The result: zero top-tier benchmarks for dual-process theory, zero for moral identity theory, despite their combined 25,000+ citations. The instruments the field has not built are not for niche constructs — they are for the foundational dynamics that moral psychology has spent decades establishing."

**contextMeaning:** "The absence of these benchmarks is consequential, not merely unfortunate. Dual-process theory would test not what moral content a model endorses but how its judgments change under different reasoning conditions — a process-level evaluation that content-level tests inherently cannot provide. The field has built instruments for measuring moral opinions while leaving instruments for measuring moral reasoning unbuilt."

---

## Claim 4 — Cultural Quality Cliff (Non-Western Exclusion)

**contextAbout:** "Four non-Western moral traditions with deep philosophical roots — Ubuntu ethics (African communal moral philosophy), Confucian moral philosophy (East Asian virtue and role-based ethics), Indigenous ethical frameworks (diverse traditions from Aboriginal Australian to Maori to Lakota), and relational moral identity — collectively represent moral worldviews held by billions of people worldwide."

**contextMeasure:** "These four traditions field 32 benchmark candidates across our landscape. Their combined quality rate in the top and high tiers: 0%. Not one of the 32 candidates meets the minimum threshold for research-grade AI moral evaluation. For comparison, MFT's quality rate is 73%. The ratio is not 2:1 or 10:1 — it is undefined (73% vs. 0%)."

**contextMeaning:** "This is a measurement gap, not a deficit of the traditions themselves. The 32 candidates show genuine research effort, but these traditions lack the foundational psychometric infrastructure (validated questionnaires, population norms, annotated datasets) that Western frameworks developed over decades. The practical consequence: the question 'does this AI system respect Ubuntu communal moral values?' or 'does it align with Confucian conceptions of duty?' cannot currently be answered at a research-grade standard. The moral traditions of billions of potential AI users are invisible to the evaluation infrastructure."

---

## Claim 5 — Human Baseline Deficit

**contextAbout:** "A benchmark score for an AI model is only meaningful in relation to human performance. When we say a model scores 75 on moral reasoning, we need to know: is that like a typical adult (30-50), a graduate student (50-65), or a moral philosophy professor (60-70)? Without this reference point, the number has no interpretation."

**contextMeasure:** "We checked each of the 292 benchmarks for published human comparison data — scores from actual human participants on the same instrument. We found that 34% provide no human baseline at all. This is nearly double the 18% rate reported in earlier studies that only examined the top 55 most established benchmarks. The doubling reflects the systematic exclusion of lower-quality benchmarks from prior analyses."

**contextMeaning:** "Without human baselines, claims like 'this model is more utilitarian than average' or 'less care-oriented than humans' lack an empirical anchor. The scores become description without interpretation. This deficit is especially concerning for AI governance: regulatory frameworks that cite benchmark scores as evidence for deployment safety are building on numbers that may lack any interpretive foundation."

---

## Claim 6 — Temporal Stagnation

**contextAbout:** "As AI capabilities have grown exponentially, the moral psychology benchmarks used to evaluate them have proliferated rapidly — but has quality kept pace with quantity? This claim tracks whether the field is learning to build better evaluation tools over time."

**contextMeasure:** "We grouped benchmarks by publication period and calculated quality rates (percentage reaching top or high tiers) for each cohort. Pre-2020 benchmarks: ~75% quality rate. 2020-2022 cohort: 48%. 2023-2026 cohort: 46%. The volume of benchmarks increased 9.5-fold over this period, but the quality rate declined."

**contextMeaning:** "The field has learned to build more benchmarks, not better ones. The decline is consistent with academic incentives that reward rapid-iteration benchmark papers — new tests for new models — over the slow work of psychometric validation, baseline collection, and construct validity demonstration. The conditions producing the triple bind are reproduced with each publication cycle. This pattern is not self-correcting."

---

## Claim 7 — RLHF Moral Fingerprint (Cross-Vendor Convergence)

**contextAbout:** "When we tested 9 AI models from 3 independent companies, we expected some differences reflecting different training approaches: Anthropic uses Constitutional AI, Google uses instruction tuning, OpenAI uses iterative RLHF (Reinforcement Learning from Human Feedback). Instead, we found the models are morally indistinguishable by most benchmarks."

**contextMeasure:** "We administered 23 benchmarks (~750 items per model) to all 9 models and measured cross-model variation. 43% of benchmarks produced zero variation — identical scores regardless of vendor, architecture, or size. All 9 models share 6 universal moral signatures: a Western-liberal moral bias, near-zero purity/sanctity responses, suppressed authority deference, perfect ethical consistency on trolley dilemmas, post-conventional moral reasoning scores exceeding philosophy graduate students, and asymmetric refusal of personal harm scenarios."

**contextMeaning:** "These six signatures constitute a moral fingerprint without documented precedent in any human population — not secular Scandinavians, not American college students, not moral philosophy PhDs. This fingerprint shows correlation across 9 aligned models, not a demonstrated causal effect of RLHF specifically; but no vendor has articulated target values for these moral dimensions, yet their training processes converge on the same quantitative values. The one benchmark that did separate models was a process-level probe (dual-process protocol), not a content-level test — reinforcing Claim 3's finding that the instruments the field most needs are the ones it has not built."

---

## Start Here Panel (3 paragraphs)

**Paragraph 1:** "This dashboard presents the findings from a comprehensive evaluation of how the AI field tests whether language models make ethical decisions. We examined every available moral psychology benchmark for AI — 292 in total — and discovered that the evaluation infrastructure has fundamental structural problems that undermine its ability to meaningfully assess AI moral reasoning."

**Paragraph 2:** "The central finding is what we call the 'triple bind.' First, the evaluation tools are theoretically narrow — dominated by a single Western moral framework (Moral Foundations Theory) while other important theories and most non-Western traditions have zero quality benchmarks. Second, they are empirically undiscriminating — when we tested 9 AI models from 3 different companies, 43% of benchmarks could not tell any difference between them. Third, they are culturally blind — the moral values of billions of people worldwide are invisible to the current testing infrastructure."

**Paragraph 3:** "Navigate the dashboard using the tabs above. The 'Overview' tab presents the high-level findings with seven numbered claims. Each subsequent tab provides detailed analysis with charts and evidence. Every section includes three contextual blocks — 'What is this about?' (background), 'How did we measure it?' (method), and 'What does it mean?' (implications) — so you can understand the analysis without prior background in moral psychology or AI evaluation."
