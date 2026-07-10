# Eval-of-Evals Methodology: Religious Values Benchmarks

**Generated:** 2026-04-03
**Purpose:** Framework for meta-evaluating and comparing religious values benchmarks before choosing which to implement

---

## 1. Why an Eval-of-Evals?

Not all benchmarks are equal. A benchmark can score well on our 3-axis composite (RD/PE/CI) yet fail as a meaningful evaluation of religious values alignment. This methodology defines how to systematically assess the quality of benchmarks themselves before investing implementation effort.

Key question: **If we run Model X on Benchmark B and get score S, what does S actually tell us about Model X's religious values alignment?**

---

## 2. Seven Meta-Evaluation Criteria

### 2.1 Content Validity
**Does the benchmark test what it claims to test?**

| Level | Description | Example |
|-------|-------------|---------|
| HIGH | Questions require genuine theological reasoning | "According to Hanafi jurisprudence, how should inheritance be divided when..." |
| MEDIUM | Questions test religious knowledge but not reasoning | "Which book of the Bible contains the Ten Commandments?" |
| LOW | Questions mention religion but test general skills | "Translate this Arabic text about Islamic law" |

**Assessment method:** Sample 20 questions from the benchmark. Classify each as HIGH/MEDIUM/LOW. Compute percentage at each level. A benchmark with >50% HIGH is content-valid for theological reasoning; >50% MEDIUM is valid for knowledge testing only.

### 2.2 Discriminative Power
**Can the benchmark distinguish between models?**

| Signal | Interpretation |
|--------|----------------|
| All models score >90% | Ceiling effect — benchmark is too easy |
| All models score <20% | Floor effect — benchmark is too hard or misspecified |
| Scores range 30-80% | Good discrimination |
| Score variance <5% | Low discrimination — models perform similarly |
| Score variance >20% | Good discrimination between models |

**Assessment method:** Run benchmark on 3+ models (at least 1 frontier, 1 mid-tier, 1 small). Compute score range and variance. Flag ceiling/floor effects.

### 2.3 Cultural Authenticity
**Were benchmarks created by scholars from the tradition being evaluated?**

| Level | Description |
|-------|-------------|
| NATIVE | Created by scholars of that tradition (e.g., Islamic law scholars creating fiqh benchmarks) |
| CONSULTED | Created by CS researchers with tradition-specific consultation |
| EXTERNAL | Created by researchers outside the tradition with no documented consultation |

**Assessment method:** Check author affiliations, acknowledgments, and methodology section for evidence of domain expertise.

### 2.4 Reproducibility
**Can independent researchers replicate the evaluation?**

Checklist:
- [ ] Data publicly available with documented format
- [ ] Evaluation code available
- [ ] Scoring metrics clearly defined
- [ ] Prompt templates documented (for LLM-based evaluation)
- [ ] Inter-annotator agreement reported (for human-judged benchmarks)

Score: count of YES items out of 5.

### 2.5 Complementarity
**Does this benchmark add information not provided by others in our selection?**

Dimensions of complementarity:
- **Tradition:** Tests a tradition not covered by other selected benchmarks
- **Task type:** Uses a different evaluation format (MCQ vs. open-ended vs. scenario)
- **Cognitive level:** Tests different cognitive demands (recall vs. reasoning vs. application)
- **Language:** Evaluates in a language not covered by other benchmarks
- **Domain:** Tests a domain not covered (law, ethics, liturgy, history)

Score: count of unique dimensions (1-5). A benchmark that scores 1 is redundant; 4+ is highly complementary.

### 2.6 Construct Coverage
**What aspect of "religious values alignment" does this benchmark measure?**

The construct space for religious values alignment has at least 6 dimensions:

| Dimension | Description | Example Benchmarks |
|-----------|-------------|-------------------|
| **Knowledge** | Factual recall about traditions | FaithBench (Christian theology), Ghaly (Islamic inheritance law) |
| **Reasoning** | Applying religious principles to novel cases | QIAS shared task (inheritance computation), scenario-based benchmarks |
| **Values** | Representing a tradition's value system | SP-Typology (multi-religion psychometric), EVALUESTEER |
| **Sensitivity** | Avoiding offense to practitioners | Religious hate speech detection, bias benchmarks |
| **Pluralism** | Handling multiple traditions fairly | Multi-tradition benchmarks, interfaith scenarios |
| **Contextualization** | Adapting responses to tradition-specific contexts | Denomination-aware responses, cultural context |

**Assessment method:** Classify each benchmark by primary dimension(s). The ideal Top 15 covers all 6.

### 2.7 Annotation Quality
**How were the gold-standard answers determined?**

| Level | Method | Reliability |
|-------|--------|-------------|
| EXPERT | Domain theologians/religious scholars | Highest |
| MIXED | CS researchers + domain consultation | High |
| CROWD | Crowdworkers (MTurk, etc.) | Medium |
| AUTO | Automatically generated (templates, LLM) | Low |
| DERIVED | From existing religious texts (no annotation needed) | Medium-High |

---

## 3. Implementation Trial Protocol

For each benchmark in the Top 15, run the following trial before committing to full implementation:

### 3.1 Sample Selection
- Extract 20-50 items from the benchmark (stratified by difficulty if available)
- Include items from multiple sub-categories/topics

### 3.2 Model Selection
Minimum 3 models:
- **Frontier closed:** Claude Opus/Sonnet, GPT-4o
- **Frontier open:** Llama-3-70B, Mixtral-8x22B
- **Mid-tier:** Llama-3-8B, Phi-3-mini

### 3.3 Prompting Strategy
- Zero-shot (baseline)
- 3-shot with tradition-specific examples (if applicable)
- System prompt variants: neutral vs. tradition-aware

### 3.4 Scoring
- Use the benchmark's intended metric
- Also compute: accuracy, F1, exact match (where applicable)
- For open-ended: use model-graded scoring with rubric

### 3.5 Analysis Template

For each trial, produce a report with:
1. **Ceiling check:** Is any model >90% accuracy?
2. **Discrimination check:** What is the score range across models?
3. **Error analysis:** What types of errors do models make? (knowledge gaps vs. reasoning failures vs. cultural misunderstanding)
4. **Implementation difficulty:** How long did setup take? What obstacles arose?
5. **Verdict:** IMPLEMENT / MODIFY / SKIP

---

## 4. Selection Criteria for Implementation Priority

After meta-evaluation, rank benchmarks for implementation using this decision tree:

```
Is data publicly available?
├── NO → SKIP (unless uniquely valuable and obtainable on request)
└── YES
    ├── Is format harness-compatible (MCQ/MRC/Binary)?
    │   ├── YES → HIGH PRIORITY (Tier 1)
    │   │   ├── Content validity HIGH? → IMPLEMENT FIRST
    │   │   └── Content validity MEDIUM/LOW? → IMPLEMENT WITH CAVEATS
    │   └── NO
    │       ├── Is the tradition underrepresented?
    │       │   ├── YES → MEDIUM PRIORITY (Tier 2, worth adaptation effort)
    │       │   └── NO → LOW PRIORITY (Tier 3)
    │       └── ...
    └── ...
```

### Tier Assignment

| Tier | Criteria | Expected Count |
|------|----------|----------------|
| **Tier 1: Implement First** | Data ready + harness-compatible + content valid | 4-6 benchmarks |
| **Tier 2: Adapt & Implement** | Data ready + needs format adaptation OR fills tradition gap | 4-6 benchmarks |
| **Tier 3: Exploratory** | Data unclear + unique tradition coverage | 3-5 benchmarks |
| **Skip** | No data + redundant + low content validity | 0-2 benchmarks |

---

## 5. Comprehensive Survey Feature Checklist

When characterizing any religious values benchmark, document all of the following:

### Identity
- [ ] Full title and citation
- [ ] Year published
- [ ] Authors and affiliations
- [ ] Primary religious tradition(s)
- [ ] Tradition family (Abrahamic/Dharmic/East Asian/African/Other)
- [ ] Publication venue and tier

### Content
- [ ] Number of items/questions
- [ ] Question format (MCQ/binary/open-ended/scenario/etc.)
- [ ] Cognitive level (knowledge/comprehension/application/analysis/synthesis)
- [ ] Sub-topics covered
- [ ] Languages supported
- [ ] Denominational depth (monolithic vs. denomination-aware)
- [ ] Scriptural references (yes/no, which texts)

### Technical
- [ ] Data availability (URL, license)
- [ ] Code availability
- [ ] Harness compatibility (lm-eval, Inspect, HELM, LightEval, OpenAI, EleutherAI)
- [ ] Scoring metric(s)
- [ ] Model compatibility (open/closed/both)
- [ ] Annotation method and quality

### Impact
- [ ] Citation count
- [ ] Citations per year
- [ ] Downstream adoption (papers using this as benchmark)
- [ ] Leaderboard existence
- [ ] Community activity (workshops, shared tasks)

### Meta-Evaluation
- [ ] Content validity score (HIGH/MEDIUM/LOW)
- [ ] Discriminative power (tested? results?)
- [ ] Cultural authenticity (NATIVE/CONSULTED/EXTERNAL)
- [ ] Reproducibility score (0-5)
- [ ] Complementarity score (1-5)
- [ ] Construct dimension (Knowledge/Reasoning/Values/Sensitivity/Pluralism/Contextualization)

---

## 6. Recommended Approach for Comprehensive Survey

1. **Phase A:** Score all 52 gate-passing candidates on the 7 meta-evaluation criteria (automated where possible, expert judgment for 2.1, 2.3, 2.7)
2. **Phase B:** Run implementation trials on Top 5 candidates (highest COMPOSITE + diversity)
3. **Phase C:** Based on trial results, revise rankings and select final implementation set
4. **Phase D:** Full implementation of Tier 1 benchmarks in at least 2 harnesses
5. **Phase E:** Comparative analysis across benchmarks (does model X that scores well on Islamic knowledge also score well on Christian theology?)
6. **Phase F:** Publication-ready report with methodology, findings, and recommendations
