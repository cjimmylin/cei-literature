---
stem: "2025-Eriksson-Can We Trust AI Benchmarks An Interdisciplinary Review"
reader_model: "opus"
confidence: "high"
is_benchmark: false
theme_tags: [best-practices, validity-psychometrics, contamination-robustness, saturation-discrimination]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: 110
dataset_construction: "n/a"
languages: [en]
models_tested: []
headline_numbers: ["meta-review of ~110 publications, 2014-2024 (p.4)", "~55% of reviewed articles published 2023 or later (p.4)", "of 24 SOTA LLM benchmarks, only 4 provided replication scripts, ≤10 ran multiple evals (p.9)", "of 30 models analyzed, only 9 reported train-test overlap (p.9)", ">70% of computer-vision benchmark datasets reused from other domains (p.5)"]
---
## 1. Gist
An interdisciplinary meta-review (European Commission JRC authors) of ~110 publications (2014-2024) critiquing quantitative AI benchmarking. It synthesizes a taxonomy of "Nine Reasons to Be Cautious with Benchmarks" spanning technical flaws (data/annotation, construct validity, contamination, gaming) and sociotechnical flaws (commercial incentives, community path-dependency, saturation, unknown unknowns, cultural narrowness). It matters enormously for values-alignment benchmarking because it is a structured catalogue of the exact failure modes a new values benchmark must avoid, framed with policy/regulatory stakes (EU AI Act). It is not itself a benchmark — it is the anti-pattern reference document, and its "safetywashing," "sandbagging," and construct-validity arguments are directly load-bearing for how one designs and defends an ethics/values eval.

## 2. Benchmark/eval design features
Core artifact is a nine-issue taxonomy (all as narrative categories, deliberately interlinked, not ranked): (5.1) Data collection/annotation/documentation — poor provenance, dataset reuse, noisy annotation, shortcut learning; (5.2) Weak construct validity — benchmarks "do not measure what they claim," contested constructs like "stereotype"/"toxicity" left undefined, safetywashing (safety benchmarks correlate with capability); (5.3) Sociocultural context/gap — benchmarks as normative instruments, misalignment with practitioner needs; (5.4) Narrow diversity/scope — text-only, English-only, static one-time testing, aggregation problems, failure to characterize *how* models fail; (5.5) Economic/competitive roots — SOTA-chasing, industry capture (private share of biggest models 11%→96% 2010-2021); (5.6) Rigging/gaming — Goodhart's law, MCQ-optimization, data contamination, sandbagging; (5.7) Dubious community vetting — benchmark lottery, peer-washing, path dependencies; (5.8) Rapid development/saturation — benchmarks outdated, hit 100% ceiling; (5.9) AI complexity/unknown unknowns — latent vulnerabilities, creators' knowledge limits.

## 3. Task format & example item
n/a — no items; this is a survey. Illustrative critique example: HellaSwag drawing ethics proxies from Amazon crowdworkers and Reddit "Am I the Asshole?" is questioned as a proxy for morals (p.7).

## 4. Scoring / grading methodology
n/a. Methodology is a snowball literature sample (not systematic keyword search) starting from Raji et al. 2021 "AI and the Everything in the Whole Wide World Benchmark," expanding via reference lists and citation tracking; inclusion = papers primarily critiquing benchmarks; exclusion = papers proposing/applying benchmarks (p.4). ~110 papers, 2014-2024.

## 5. Dataset construction & provenance
The "dataset" is the corpus of ~110 reviewed papers. Snowball sampling deliberately chosen to capture preprints and cross-disciplinary terminology; papers proposing new benchmarks excluded because they "reproduce the general notion that quantitative benchmarks provide a reasonable technical fix" (p.4). Special effort to include image/sound/audiovisual critique under-represented vs text.

## 6. Validity evidence
n/a as an empirical instrument. But the paper marshals strong secondary evidence on benchmark *invalidity*: Blodgett et al. found StereoSet/CrowS-Pairs/WinoBias/WinoGender all fail to define what they measure (p.6); Ren et al. found ETHICS, TruthfulQA, GPQA, MT-Bench, LMSYS Arena etc. correlate strongly with upstream capability (safetywashing, p.7); Reuel et al. audit of 24 SOTA benchmarks (p.9).

## 7. Saturation / discrimination
Section 5.8 is dedicated to saturation: prominent LLM benchmarks (Lambada, ARC, OBQA, HellaSwag, WinoGrande) predate in-context learning and chat, and many are outperformed to ~100% accuracy (p.10); "a benchmark no longer reflects model performance" once saturated (Ott et al., p.10). Also notes intra-model variance is largely unmeasured — "most benchmarks fail to distinguish signal and noise" (Reuel et al., p.7).

## 8. Multiturn / agentic aspects
n/a directly, but the review argues benchmarks' "one-time testing logic" fails to capture "the evolving nature of human-AI interactions" and calls for longitudinal, interactive, multi-system evaluation (McIntosh et al., Birhane et al.; p.7).

## 9. Key numbers
- ~110 papers reviewed, 2014-2024; ~55% from 2023+ (p.4)
- Röttger et al.: ~46% of AI safety benchmarks produced in 2023, 15 new datasets in first two months of 2024 (p.4)
- >70% of computer-vision benchmark datasets reused from other domains (Koch et al., p.5)
- Oakden-Rayner: removing chest-drain images dropped model performance >20% (p.6)
- Reuel et al.: of 24 SOTA benchmarks, only 4 gave replication scripts, ≤10 ran multiple evals or reported significance (p.9)
- Zhang et al.: of 30 models, only 9 reported train-test overlap (p.9)
- Industry share of biggest AI models: 11% (2010) → 96% (2021) (p.8)
- Ott et al.: study of 3765 benchmarks — only a small minority reached widespread adoption (p.9)
- GPT-4 solved easy Codeforces problems only if added before 5 Sept 2021 (contamination signal, p.9)

## 10. Pitfalls & limitations
Author-admitted: not exhaustive; snowball sampling introduces selection bias; nine-issue categories overlap and are a "narrative tool," not an absolute taxonomy (p.4-5); scope excludes qualitative benchmarks and papers proposing benchmarks (p.4); limited to 2014-2024. As a resource for benchmark *builders*, it is diagnostic not prescriptive (mitigation is future work). The catalogued failure modes themselves are the key content: construct-validity gaps, safetywashing, sandbagging, contamination, saturation, Anglo-centrism, one-time-testing logic.

## 11. Novel ideas worth stealing
- **Nine-issue checklist as a pre-registration gate**: before shipping a values benchmark, audit against all nine (define the construct explicitly; document provenance; test contamination; report intra-model variance/multiple seeds; check capability-correlation to avoid safetywashing; include non-English/non-text; design against gaming).
- **Safetywashing test**: explicitly measure whether your "values/safety" score correlates with raw capability — if it does, you may be measuring capability, not alignment (Ren et al.). A concrete validity control every ethics benchmark should run.
- **"Benchmark the benchmarks" / trustworthiness signaling**: the paper's closing call — regulators need "standardised methods for assessing the trustworthiness of benchmarks" rather than standardized metrics — suggests a meta-benchmark rubric as a distinct deliverable.
- **Failure-characterization over single-score ranking**: build evals that reveal *when and why* models fail (error taxonomies), not just a leaderboard number — "much more important to understand when and why models fail" (Gehrmann).
- **Dynamic / hidden-holdout benchmarks** to counter contamination and Goodharting (Chollet's hidden test sets, LiveBench-style rotation).
- **Report replication scripts + statistical significance + multiple seeds** as minimum standard (only 4/24 did).
- **Construct-definition discipline**: for contested constructs (stereotype, toxicity, morality) publish an explicit operational definition, or inherit the "abstraction error" that "produces a false sense of certainty" (Selbst).

## 12. Notable quotes
- "no benchmark is neutral and ... AI tests and benchmarking practices always rest 'on interwoven technical and normative decisions'" (p.2)
- "framing an AI benchmark dataset as general purpose 'is ultimately dangerous and deceptive, resulting in misguidance on task design ... enabling ... potential model misuse'" (Raji et al., p.6)
- "it's not like a lawyer's job is to answer bar exam questions all day" (Narayanan and Kapoor, p.7)
- "when a measure becomes a target, it ceases to be a good measure" (Goodhart/Strathern, p.8)
- "We do not necessarily need standardised benchmark metrics and methods. But we do need standardised methods for assessing the trustworthiness of benchmarks" (p.11)

## 13. UNKNOWN / not in extract
- The full list of the ~110 reviewed papers (only References A-J visible in extract).
- Whether any quantitative coding/frequency analysis was applied across the corpus (appears purely narrative).
- Specific mitigation framework details (explicitly deferred to future work).
- Any figures/tables enumerating the nine issues in tabular form.
- Author inter-rater process for categorizing papers beyond "discussing within the wider author group" (p.5).
