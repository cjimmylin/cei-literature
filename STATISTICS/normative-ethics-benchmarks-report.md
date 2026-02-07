# Normative Ethics + LLM Benchmark Paper Identification Report

**Date:** 2026-02-07
**Exemplar Paper:** 2021-Hendrycks-Aligning AI with Shared Human Values (ICLR 2021)
**YAML Field Added:** `normative_ethics_benchmark` (values: `Yes`, `Borderline`)

---

## Methodology

### Objective

Identify papers in the CEI Literature Vault that combine **normative ethics frameworks** (virtue ethics, deontological ethics, utilitarian/consequentialist ethics) with **benchmarks or datasets** for rigorously assessing **LLMs**. The Hendrycks ETHICS paper serves as the exemplar: it explicitly operationalizes deontological, utilitarian, and virtue-theoretic concepts into a dataset used to evaluate language models.

### Search Process

1. **~80 candidate papers read individually** across multiple rounds of keyword searches
2. Existing YAML tags (`virtue_ethics`, `deontological_ethics`, `utilitarian_ethics`, `is_benchmark`, `is_dataset`) were NOT trusted — each paper was read directly
3. Search terms included:
   - Normative ethics: *deontological, utilitarian, consequentialist, virtue ethics, Kantian, categorical imperative, rights-based, duty, eudaimonia, flourishing, phronesis, normative framework*
   - Benchmarks/data: *benchmark, dataset, evaluation, test suite, moral dilemma, trolley problem*
   - LLM terms: *LLM, language model, GPT, ChatGPT, Claude, Llama, foundation model*
4. Fields searched: `abstract`, `key_contribution`, `significance`, `paper_summary`, plus PDF extracts for ambiguous cases

### Qualifying Criteria

A paper qualifies as **Yes** if it meets ALL three conditions:
1. **Normative ethics**: Explicitly references or operationalizes at least one normative ethical framework (deontological, utilitarian, virtue, care ethics, rights-based)
2. **Benchmark/dataset**: Creates, uses, or adapts a structured evaluation artifact (dataset, benchmark, test suite, scenario set)
3. **LLM testing**: Evaluates one or more large language models using the benchmark

A paper is **Borderline** if it meets most criteria but has a notable gap (e.g., implicit rather than explicit normative framing, no released dataset, or primarily a method paper that includes evaluation).

---

## Section 1: Confirmed Papers (20 papers — `normative_ethics_benchmark: Yes`)

### Tier 1: Strong Matches (15 papers)

| # | File | Ethics Frameworks | Data Artifact | LLMs Tested |
|---|------|------------------|---------------|-------------|
| 1 | `2021-Hendrycks-Aligning AI with Shared Human Values.md` | Deontological + Utilitarian + Virtue | ETHICS benchmark (justice, well-being, duties, virtues) | Language models |
| 2 | `2025-An-MoralReason.md` | All three (V+D+U) | Moral-Reason-QA (680 scenarios) | LLMs via RL |
| 3 | `2024-Agarwal-Ethical Reasoning Depends on Language.md` | All three (V+D+C) | Multilingual dilemmas (6 languages) | GPT-4, ChatGPT, Llama2 |
| 4 | `2025-Samway-Are Language Models Consequentialist or Deontological.md` | Consequentialist + Deontological | 600+ trolley scenarios | Multiple LLMs |
| 5 | `2025-Chiu-MoReBench.md` | Kantian Deontology + Utilitarian | MoReBench (150 examples) | Reasoning LLMs |
| 6 | `2024-Marraffini-The Greatest Good Benchmark.md` | Utilitarian | GGB benchmark | 15 LLMs |
| 7 | `2025-Takeshita-JETHICS.md` | Normative theories (mirrors ETHICS) | JETHICS (78K, Japanese) | GPT-4o + open LLMs |
| 8 | `2025-Hilliard-Measuring AI Alignment with Human Flourishing.md` | Virtue ethics (eudaimonia) | FAI Benchmark (7 dimensions) | Multiple AI models |
| 9 | `2025-Neuman-Analyzing the Ethical Logic of Six Large Language Models.md` | Consequentialist + Deontological | Eval framework + dataset | GPT-4o, LLaMA, Claude, Gemini, Mistral |
| 10 | `2025-Neuman-PRIME Framework Convergent Ethics.md` | Consequentialist + Deontological | PRIME benchmark | Multiple LLMs |
| 11 | `2024-Sorin-Ethical Alignment of LLMs in Healthcare.md` | Deontological + Utilitarian | 5 medical trolley scenarios | 14 LLMs incl. GPT-o1 |
| 12 | `2025-Cheung-LLMs Amplified Cognitive Biases Moral.md` | Deontological + Utilitarian | 22 moral dilemmas (PNAS) | LLMs vs humans (N=285) |
| 13 | `2024-Zhou-Rethinking Machine Ethics Can LLMs Perform Moral Reasoning.md` | All three (V+D+U) | Theory-derived moral datasets | Multiple LLMs (NAACL 2024) |
| 14 | `2025-Nadeem-Ethical Decision-Making in Humans and Large.md` | Deontological + Utilitarian + Care | 30 dilemmas across 5 domains | GPT-4, Copilot, Gemini, Perplexity, DeepSeek |
| 15 | `2025-Chakraborty-Structured Moral Reasoning.md` | All normative theories (D+U+V+Care+Rights) | 4 moral datasets + prompting taxonomy | 12 open-source LLMs |

### Tier 2: Qualifying with Caveats (5 papers)

| # | File | Caveat |
|---|------|--------|
| 16 | `2025-Jiao-LLM Ethics Benchmark.md` | Normative framework less explicit than Tier 1 |
| 17 | `2024-Ji-MoralBench.md` | Normative framework embedded rather than explicit |
| 18 | `2024-Garcia-The Moral Turing Test.md` | Utilitarian mentioned; focuses on human-AI comparison |
| 19 | `2024-Liu-Evaluating Moral Beliefs across LLMs through a.md` | Deontological through Chinese cultural lens |
| 20 | `2024-Yu-CMoralEval.md` | Large dataset (30K+) but ethics culturally framed |

---

## Section 2: Borderline Papers (11 papers — `normative_ethics_benchmark: Borderline`)

| # | File | Why Borderline |
|---|------|----------------|
| 1 | `2025-Galatolo-Beyond Ethical Alignment AMAs.md` | Philosophical benchmark for LLMs; abductive reasoning focus rather than normative evaluation |
| 2 | `2024-Unknown-Evaluating Computational Models of Ethics.md` | All 3 frameworks referenced; unclear if benchmarks modern LLMs |
| 3 | `2025-Sorensen-Operationalizing Pluralistic Values.md` | Deontological + consequentialist; primarily alignment trade-offs focus |
| 4 | `2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences.md` | Kantian framework + GPT-4o; primarily an alignment method paper |
| 5 | `2023-Rao-Ethical Reasoning over Moral Alignment.md` | Normative dilemmas + GPT-4; position paper, no released dataset |
| 6 | `2025-Keshmirian-Many LLMs Are More Utilitarian Than One.md` | Utilitarian scenarios; no reusable benchmark dataset |
| 7 | `2025-Hui-Decoding Moral Responses in AI.md` | Tests 7 LLMs under deontological/utilitarian conditions; no released benchmark artifact |
| 8 | `2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large.md` | Tests 52 LLMs on utilitarian alignment; implicit normative framework in Moral Machine design |
| 9 | `2024-Takemoto-The moral machine experiment on large language.md` | Tests 4 LLMs on utilitarian preferences (50K scenarios); implicit normative framework |
| 10 | `2024-Unknown-Moral Persuasion in Large Language Models.md` | Tests LLMs with V+D+U prompts but measures via MFQ (psychology instrument) |
| 11 | `2024-Seror-Moral Minds of LLMs.md` | Tests ~40 LLMs on moral preferences (D+U dimensions); uses revealed preference theory (economics) |

---

## Section 3: Exclusion Patterns

The following paper types were reviewed but did NOT qualify. These patterns explain why papers that might seem related at first glance were excluded:

### Psychology-Based Frameworks (not normative ethics)

| Pattern | Example Papers | Why Excluded |
|---------|---------------|-------------|
| **Moral Foundations Theory** | Abdulhai, M3oralBench, Jotautaite, BenchMoral, Flores | MFT is a descriptive psychological theory, not a prescriptive normative framework |
| **Kohlberg cognitive development** | Deng-Probing Moral Development, Khandelwal-DIT | Developmental psychology framework, not normative philosophy |

### Social Norms / Commonsense Ethics

| Pattern | Example Papers | Why Excluded |
|---------|---------------|-------------|
| **Social norms / commonsense** | Emelin-Moral Stories, Jiang-Delphi, Hendrycks-Jiminy Cricket, Leteno-Histoires Morales | Crowdsourced norms without grounding in normative theory |

### Benchmarks Without Normative Framing

| Pattern | Example Papers | Why Excluded |
|---------|---------------|-------------|
| **Bias/fairness benchmarks** | BEATS, McBE, MORALISE, PapersPlease (ERG theory) | Measure bias/fairness, not normative ethical reasoning |
| **Safety benchmarks** | Yuan-R-Judge (risk awareness), Pisano-Moral High Ground | Safety/harm prevention, not normative ethical analysis |
| **Role-playing quality** | Tu-CharacterEval (persona consistency) | Measures character consistency, not ethical reasoning |
| **Reasoning quality audit** | Neuman-Auditing Ethical Logic | Same author as qualified papers but focuses on reasoning quality, not normative classification |
| **Uses existing ETHICS benchmark** | Freire-Latent Wellbeing, Karpov-Inducing Biases | No new normative contribution; applies existing benchmark |

### Theory-Only Papers (no LLM benchmark)

| Pattern | Example Papers | Why Excluded |
|---------|---------------|-------------|
| **Theoretical / philosophical only** | Rusnak-EudAImonia, Zohny-ADEPT, Brophy-Black Box, Steen-ChatGPT Ethics, Khamassi-Strong/Weak Alignment, Sullins-Phronesis, Akhtar-Ethicsophical, So-Confucian Analects, AI Alignment Fair Treatment | Discuss normative ethics but provide no benchmark or dataset |
| **Normative + no LLM testing** | Prabhumoye-Case Study (deontological NLP, no benchmark) | Has normative framing but no evaluation artifact |

### Method Papers (primarily alignment techniques)

| Pattern | Example Papers | Why Excluded |
|---------|---------------|-------------|
| **LLM as tool / alignment METHOD** | Dubey-Addressing Moral Uncertainty, Tennant-Moral Alignment (x2), Takeshita-Theory-based Moral AI, Menke-Constitutional AI | Focus on alignment methods, not normative evaluation benchmarks |
| **Method papers (social norms)** | Sun-ClarityEthic (contrastive norm learning) | Novel method, not a normative benchmark |

### Other Non-Qualifying Patterns

| Pattern | Example Papers | Why Excluded |
|---------|---------------|-------------|
| **Applied medical ethics (no normative framework)** | MedEthicEval, MedEthicsQA, Zhou-Moral Reasoning Across Languages | Domain-specific ethics without explicit normative grounding |
| **Human-only studies** | Awad-Universals in moral decisions (70K humans, no LLMs) | No LLM evaluation |
| **Game theory / social dilemmas** | Backmann-MoralSim (prisoner's dilemma) | Game-theoretic framing, not normative ethics |
| **Cross-linguistic consistency** | Farid-One Model Many Morals, Kumar-UniMoral | Tests consistency across languages, not normative frameworks |
| **Value taxonomy / cultural values** | Benkler-Assessing Value Pluralism (WVS), Russo-Pluralistic Moral Gap | Cultural values mapping, not normative ethical evaluation |
| **Moral competence / reasoning quality** | Kilov-Discerning What Matters, Liu-Diagnosing Moral Reasoning | Measures reasoning quality, not normative classification |
| **Qualitative / philosophical analysis** | McGee-How Ethical Is Utilitarian Ethics, Bang-Ethical Quandary QA | Qualitative analysis without structured benchmark |
| **General AI ethics framework** | Ray-Benchmarking ethical alignment (NLP benchmark review) | Survey/review paper, not a benchmark itself |

### Note on Duplicate

The paper `2024-Unknown-Ethical Reasoning and Moral Value Alignment` (arXiv:2404.18460) appears to be a duplicate/variant of `2024-Agarwal-Ethical Reasoning Depends on Language` (same scope, models, methodology) — not double-counted.

---

## Summary Statistics

| Category | Count |
|----------|-------|
| **Confirmed (Yes)** | 20 |
| **Borderline** | 11 |
| **Total tagged** | 31 |
| **Papers reviewed** | ~80 |
| **Exclusion rate** | ~61% |

### Framework Distribution (Confirmed papers)

| Framework | Papers Referencing |
|-----------|-------------------|
| Deontological | 17 |
| Utilitarian/Consequentialist | 18 |
| Virtue Ethics | 7 |
| Care Ethics | 3 |
| Rights-Based | 1 |

---

## Verification Checklist

- [ ] `normative_ethics_benchmark` field present in all 31 tagged papers (20 Yes + 11 Borderline)
- [ ] `../.venv/bin/python PYTHON/validate_all_papers.py` passes
- [ ] Spot-check 3 papers by reading YAML frontmatter
- [ ] Report renders correctly in Obsidian
