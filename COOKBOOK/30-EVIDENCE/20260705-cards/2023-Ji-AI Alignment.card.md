---
stem: "2023-Ji-AI Alignment"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [design-space, normative-ethics, pluralism-aggregation, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Median researcher at NeurIPS/ICML 2021 estimated 5% chance that advanced AI will have an extremely bad long-run effect on humanity (p.5)"
  - "36% of NLP researchers surveyed believe AI could produce catastrophic outcomes this century (p.5)"
  - "98% of surveyed respondents somewhat or strongly approved that AGI labs should perform pre-deployment risk assessments, hazardous capabilities evaluations, third-party model audits, and red teaming (p.56)"
  - "33% of people worldwide lack internet access, excluding them from AI system training participation (p.62)"
---
## 1. Gist
"AI Alignment: A Comprehensive Survey" by Ji et al. (Peking University, Cambridge, Oxford, CMU, HKUST, USC) is a 105-page landscape review of the AI alignment field as of late 2023/early 2024. The paper introduces the RICE framework — four alignment objectives: Robustness, Interpretability, Controllability, and Ethicality — and organizes the field into a two-phase "Alignment Cycle" consisting of Forward Alignment (alignment training) and Backward Alignment (alignment refinement through assurance and governance). For values-alignment benchmarking specifically, the survey is important because it situates evaluation and human-values verification within a broader technical and governance ecosystem, identifies key failure modes (reward hacking, goal misgeneralization, deceptive alignment), and discusses the challenges of eliciting, aggregating, and implementing diverse human values. The section on Human Values Verification (§4.3) and the discussion of Value Elicitation and Value Implementation (§6.1) directly address the core questions underlying benchmark design for values-alignment work.

## 2. Benchmark/eval design features
This is a survey and conceptual framework paper, not a benchmark. Its core claims and arguments relevant to values-alignment benchmarking are:

**RICE Framework**: Four alignment objectives — Robustness (resilience under diverse/adversarial scenarios), Interpretability (transparent inner reasoning), Controllability (susceptibility to human oversight and intervention), and Ethicality (adherence to human moral norms and social values). These map directly onto constructs that benchmarks could operationalize.

**Alignment Cycle**: Forward alignment (training) feeds backward alignment (evaluation and governance), which updates alignment requirements in a loop. Benchmarks sit inside "Assurance" (§4), particularly under Safety Evaluations and Human Values Verification.

**Failure modes catalogued**: reward hacking, goal misgeneralization, deceptive alignment, sycophancy, power-seeking, untruthful output, collectively harmful behavior, ethics violations — each of which is a potential benchmark domain.

**Human Values Verification (§4.3)**: Three main approaches: (1) Building Moral Datasets using Rules-of-Thumb and scenario norms (ETHICS, SocialChem-101, Moral Stories, MoralExceptQA); (2) Scenario Simulation via text-adventure games and human-machine interaction simulations; (3) Formal Machine Ethics using logic-based methods, RL/MDP ethics shaping, and game-theory-based approaches.

**Pluralism and aggregation challenge**: The survey identifies as a key open problem that RLHF assumes a monolithic human source of feedback, when in reality human values are diverse. Democratic fine-tuning, computational social choice, and deliberative democracy approaches are surveyed as partial solutions.

**Safetywashing (§4.1.4)**: Named concern that safety evaluations may be superficial or gameable, creating false confidence — a central validity threat for any values-alignment benchmark.

## 3. Task format & example item
n/a — this is a survey paper and does not present original benchmark items.

The closest thing to example items is the reference in §4.3 to datasets like ETHICS (Hendrycks et al., 2020) and MoralExceptQA (Jin et al., 2022a) which highlight "the inability of contemporary models to align ethically with human values" (p.54), but the survey does not reproduce specific items.

## 4. Scoring / grading methodology
n/a for the survey itself. The paper discusses evaluation methodology for the field:
- Safety evaluations use behavioral testing, red teaming, and capability evaluations (p.42-48).
- Human values verification uses dataset-based moral alignment scoring and scenario simulation.
- The survey warns against relying on single reward models to capture values due to Goodhart's Law: "we cannot simply define complex human values as reward functions" (p.54).

## 5. Dataset construction & provenance
n/a — survey paper. The paper cites and describes existing datasets:
- Moral Stories, SocialChem-101, Moral Integrity Corpus (social/moral norms)
- ETHICS dataset (Hendrycks et al., 2020)
- MoralExceptQA (Jin et al., 2022a)
- Abdulhai et al. (2022) moral foundations dataset for LLMs
- Pan et al. (2023b) reward/moral behavior tradeoff dataset

No new data is created.

## 6. Validity evidence
As a survey, the paper does not present new empirical validity evidence. It identifies validity challenges for the field:
- Deceptive alignment undermines behavioral evaluations: "straightforward approaches to alignment assessments, such as behavioral evaluations, potentially suffer from dishonest behaviors or deceptive alignment of AI systems" (p.14).
- Interpretability benchmarks are hard to build because "the inner logic of a certain AI system is unknown before the interpretability tools are applied" (p.52).
- Early moral alignment attempts (Awad et al., 2018) confirmed that "the definition and evaluation of moral values themselves is a challenging issue" (p.54).
- Survey data on researcher beliefs about AI risk should be taken with caution: "survey results may hinge upon the exact wording of the questions" (p.5).

## 7. Saturation / discrimination
n/a — no benchmark data. The survey notes that current models' failure modes (sycophancy, deceptive alignment) are "emergent at scale" (p.8-9), suggesting that existing evaluations may not discriminate well across model capability levels, and that headroom for improvement is high in the values/ethics domain.

## 8. Multiturn / agentic aspects
The survey dedicates substantial attention to LLM-based agents and multi-agent settings as an emerging alignment challenge. Key points:
- "LLM-based agents raise concerns about the system's controllability and ethicality" (p.4).
- Agentic AI systems (AutoGPT, BabyAGI) can autonomously break down tasks and act without human intervention (p.55).
- Multi-agent failure modes where individual behavior appears benign but becomes problematic collectively are covered in §3.3.2 (Cooperative Training) and §4.3.1 (Game Theory for Cooperative AI).
- The survey identifies research on multi-agent settings — interactions between multiple AI systems and multiple humans — as a future direction requiring granular feedback from realistic simulated societies (p.63).

Not a benchmark of agentic behavior, but the survey frames agentic/multi-agent alignment as a key open problem where existing benchmarks are inadequate.

## 9. Key numbers
- 5% median estimate of extremely bad long-run AI effect from NeurIPS/ICML 2021 researchers (p.5)
- 36% of NLP researchers believe AI could produce catastrophic outcomes this century (p.5)
- 98% of surveyed respondents approved that AGI labs should perform pre-deployment risk assessments and red teaming (p.56)
- 33% of worldwide population lacks internet access, excluding them from AI training participation (p.62)
- 40,000 toxic molecules generated when Urbina et al. (2022) inverted a drug discovery model (p.55)
- 28 countries plus the EU signed the Bletchley Declaration on AI safety (p.5)
- Survey covers 105 pages and cites hundreds of papers; website alignmentsurvey.com provides ongoing updates (p.1)

## 10. Pitfalls & limitations
**Author-admitted:**
- The boundaries of alignment "are often vague and subject to debate" (p.62); the broad RICE characterization is an explicit choice.
- The survey "needs to be a long-term endeavor that is continually reviewed and updated" as the field evolves rapidly (p.62).
- Many alignment concepts (e.g., inner/outer alignment) are contested and understood differently by different people (p.12).

**Additional flaws visible from outside:**
- Heavy focus on reinforcement learning and language model paradigms; other modalities (vision, robotics) are underemphasized.
- Human Values Verification section (§4.3) is comparatively thin relative to the technical alignment sections, with limited engagement with moral philosophy or empirical social science on cross-cultural value variation.
- The RICE framework is not derived from a systematic literature review but is proposed by the authors; its empirical coverage and completeness are asserted rather than validated.
- The survey does not deeply engage with measurement theory or psychometrics as a tool for validating values-alignment benchmarks — a significant gap for benchmark designers.
- The open-source governance section largely defers to unresolved debate without clear actionable conclusions.

## 11. Novel ideas worth stealing
For values-alignment benchmark design, this survey yields several reusable design moves:

1. **RICE as a benchmark taxonomy**: The four RICE dimensions (Robustness, Interpretability, Controllability, Ethicality) can serve as orthogonal axes for organizing a benchmark suite, ensuring coverage across alignment objectives rather than just surface-level harm avoidance.

2. **Alignment Cycle as evaluation framing**: Distinguishing forward alignment evaluation (does training produce aligned behavior?) from backward alignment assurance (does the deployed system behave aligned in the world?) maps to distinct benchmark modes — pre-deployment evals vs. red-teaming and post-deployment monitoring.

3. **Safetywashing as a validity threat**: Explicitly define "safetywashing" in benchmark documentation — the risk that a model scores well on the benchmark while remaining unaligned in deployment. Design items that require genuine alignment, not just surface compliance.

4. **Democratic human input with representativeness audit**: The survey flags that 33% of the world lacks internet access and is excluded from training data. Benchmark construction should document the demographic coverage of item sources and annotators, and test whether model performance varies across underrepresented demographic groups.

5. **Moral consistency as a measurable property**: The idea that "similar cases should receive similar treatment irrespective of the people or parties involved" (p.62) is directly operationalizable as a benchmark: present structurally identical moral scenarios varying only in the identity of parties involved, and measure inconsistency.

6. **Dynamic testing to prevent contamination**: Reference to Zhu et al. (2023) which uses Directed Acyclic Graphs to dynamically generate test data, "thereby reducing the risk of test data memorization and contamination" (p.60) — a directly applicable technique for values-alignment benchmarks.

7. **Scenario simulation as richer evaluation**: Text-adventure game scenarios (Pan et al., 2023a) that test deception, manipulation, and betrayal in "diverse, morally salient scenarios" represent a richer format than static MCQ items, better capturing alignment failure modes.

8. **Value pluralism as explicit design parameter**: Rather than assuming a consensus value set, build benchmarks with explicit demographic or cultural labeling of expected answers, testing whether models reflect appropriate pluralism vs. imposing dominant-group values.

## 12. Notable quotes
- "AI alignment aims to make AI systems behave in line with human intentions and values. As AI systems grow more capable, so do risks from misalignment." (p.1)
- "We cannot simply define complex human values as reward functions, which also brings greater challenges to value alignment." (p.54)
- "Determining who to draw feedback from and understanding the scope and nature of human values infused into models are crucial questions for the field of alignment." (p.62)
- "Obtaining a truly random sample of the global population is particularly challenging, as 33% of people worldwide do not have Internet access and thus are excluded from participating in AI system training." (p.62)

## 13. UNKNOWN / not in extract
- The exact page range of Section 2 (Learning from Feedback) in full detail was not read; summary coverage only.
- Section 3 (Learning under Distribution Shift) full technical details were not read in full.
- All appendix content and supplementary material (if any) beyond p.63 was not reviewed (extract pages 64+ are references only).
- The exact number of papers cited in the survey total was not determined from the extract.
- Details of all benchmark datasets listed in §4.1.1 (Datasets and Benchmarks) were not read; only referenced in the table of contents.
- Whether the survey addresses non-English language alignment concerns in any depth is unknown.
- Specific methodology details for red teaming evaluations in §4.1.3 were not read in full.
