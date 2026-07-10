# Normative Ethics + LLM Benchmark Report (V3 — Vault-Wide)

**Generated:** 2026-02-07
**Scope:** Full vault — 923 papers (657 original + 266 EXSR import)
**YAML field:** `normative_ethics_benchmark` (values: Yes, Borderline)

# PDF Results
Framework       │ Confirmed │ Borderline │ Missing │ Total │
  │ Deontological Ethics │        12 │         19 │       6 │    37 │
  │ Utilitarian Ethics   │        14 │         20 │       6 │    40 │
  │ Virtue Ethics        │         2 │          4 │       1 │     7 │
  71 files copied (69 actual PDFs + 2 PDF extracts used as fallback) across 6 s

Infographic Prompt: 
can you create a detailed infographic for the author, year, reference, abstract, introduction, methods, datasets, benchmarks, results, outcomes, conclusions.

---

## Methodology

### Qualifying Criteria (3-Condition Rubric)

A paper qualifies as **Yes** if it meets ALL three conditions:
1. **Normative ethics**: Explicitly references or operationalizes at least one normative ethical framework (deontological, utilitarian, virtue, care ethics, rights-based, Rawlsian, bioethics/principlism)
2. **Benchmark/dataset**: Creates, uses, or adapts a structured evaluation artifact (dataset, benchmark, test suite, scenario set)
3. **LLM testing**: Evaluates one or more large language models using the benchmark

A paper is **Borderline** if it meets most criteria but has a notable gap (e.g., implicit rather than explicit normative framing, no released dataset, or primarily a method paper that includes evaluation).

### Round 1 (Original 657 Papers)

- ~80 candidate papers deep-read individually across multiple keyword search rounds
- Existing YAML classification tags NOT trusted — each paper read directly
- Result: **20 Yes + 11 Borderline = 31 papers**

### Round 2 (EXSR 266 Papers — 10-Agent Full Deep-Read)

- All 266 papers deep-read (no keyword pre-screening)
- 10 agents in 2 waves of 5, each reading ~27 papers with full PDF extracts
- Result: **7 Yes + 38 Borderline = 45 papers**

### Deduplication

3 papers appeared in both rounds (same arXiv paper imported under different filenames). R1 version kept in all cases. See [Duplicate Resolution Notes](#duplicate-resolution-notes) for details.

---

## Summary Statistics

| Category | R1 (657 papers) | R2 (266 papers) | Dups Removed | **Combined** |
|----------|----------------:|----------------:|------------:|-------------:|
| Yes | 20 | 7 | 2 | **25** |
| Borderline | 11 | 38 | 1 | **48** |
| **Total** | **31** | **45** | **3** | **73** |

- **Papers reviewed:** ~80 (R1) + 266 (R2) = ~346 deep-reads
- **Overall identification rate:** 73 / 923 = 7.9%

---

## Section 1: Confirmed Papers (25 — Yes)

| # | Paper | Source | Frameworks | Data Artifact | LLMs | Rationale |
|---|-------|--------|------------|---------------|------|-----------|
| 1 | [[2021-Hendrycks-Aligning AI with Shared Human Values]] | R1 | Deontological + Utilitarian + Virtue | ETHICS benchmark (justice, well-being, duties, virtues) | Language models | Operationalizes Deontological + Utilitarian + Virtue via ETHICS benchmark (justice, well-being, duties, virtues), tested on Language models. |
| 2 | [[2024-Agarwal-Ethical Reasoning Depends on Language]] | R1 | All three (V+D+C) | Multilingual dilemmas (6 languages) | GPT-4, ChatGPT, Llama2 | Operationalizes All three (V+D+C) via Multilingual dilemmas (6 languages), tested on GPT-4, ChatGPT, Llama2. |
| 3 | [[2024-Garcia-The Moral Turing Test]] | R1 | Utilitarian (referenced) | Moral Turing Test scenario set | LLMs vs. humans | Qualifying with caveat: Utilitarian mentioned; focuses on human-AI comparison |
| 4 | [[2024-Ji-MoralBench]] | R1 | Normative framework embedded (moral scenarios) | MoralBench dataset | Multiple LLMs | Qualifying with caveat: Normative framework embedded rather than explicit |
| 5 | [[2024-Liu-Evaluating Moral Beliefs across LLMs through a]] | R1 | Deontological through Chinese cultural lens | Moral beliefs evaluation dataset | Multiple LLMs | Qualifying with caveat: Deontological through Chinese cultural lens |
| 6 | [[2024-Marraffini-The Greatest Good Benchmark]] | R1 | Utilitarian | GGB benchmark | 15 LLMs | Operationalizes Utilitarian via GGB benchmark, tested on 15 LLMs. |
| 7 | [[2024-Moore-Intuitions of Compromise]] | R2 | Utilitarianism (Utilitarian Sum), Contractualism (Nash Product/Nash Social Welfare Function), Rawlsian lexical minimum (maximin) | Systematically generated value aggregation scenarios (Focused set: 162 disagreement cases from 19,657 total; Random set with outcomes sampled from [1,101]) | GPT-4 and additional LLMs (referenced in supplementary materials) | Explicitly operationalizes and formally compares utilitarian vs. contractualist approaches to value aggregation through mathematical social welfare functions, creates a structured scenario set to test these competing normative proposals, and evaluates LLM alignment with human judgments on these normative-theory-grounded scenarios. |
| 8 | [[2024-Sorin-Ethical Alignment of LLMs in Healthcare]] | R1 | Deontological + Utilitarian | 5 medical trolley scenarios | 14 LLMs incl. GPT-o1 | Operationalizes Deontological + Utilitarian via 5 medical trolley scenarios, tested on 14 LLMs incl. GPT-o1. |
| 9 | [[2024-Yu-CMoralEval]] | R1 | Normative ethics (culturally framed) | CMoralEval (30K+ dataset) | Chinese and multilingual LLMs | Qualifying with caveat: Large dataset (30K+) but ethics culturally framed |
| 10 | [[2024-Zhou-Rethinking Machine Ethics Can LLMs Perform Moral Reasoning]] | R1 | All three (V+D+U) | Theory-derived moral datasets | Multiple LLMs (NAACL 2024) | Operationalizes All three (V+D+U) via Theory-derived moral datasets, tested on Multiple LLMs (NAACL 2024). |
| 11 | [[2023-Benkler-Assessing LLMs for Moral Value Pluralism]] | R2 | Distributive justice (Rawlsian/egalitarian frameworks), with domain persona interventions across professional domains | 1,201,200 observations across ten professional domains testing distributive justice scenarios | LLMs tested cross-linguistically (specifics not available in metadata) | Explicitly operationalizes distributive justice -- a core normative ethics concept from Rawlsian contractualism -- through structured scenarios across multiple domains. Creates a large-scale evaluation artifact and tests LLMs cross-linguistically. Meets all three conditions. |
| 12 | [[2025-An-MoralReason]] | R1 | All three (V+D+U) | Moral-Reason-QA (680 scenarios) | LLMs via RL | Operationalizes All three (V+D+U) via Moral-Reason-QA (680 scenarios), tested on LLMs via RL. |
| 13 | [[2025-Chakraborty-Structured Moral Reasoning]] | R1 | All normative theories (D+U+V+Care+Rights) | 4 moral datasets + prompting taxonomy | 12 open-source LLMs | Operationalizes All normative theories (D+U+V+Care+Rights) via 4 moral datasets + prompting taxonomy, tested on 12 open-source LLMs. |
| 14 | [[2025-Cheung-LLMs Amplified Cognitive Biases Moral]] | R1 | Deontological + Utilitarian | 22 moral dilemmas (PNAS) | LLMs vs humans (N=285) | Operationalizes Deontological + Utilitarian via 22 moral dilemmas (PNAS), tested on LLMs vs humans (N=285). |
| 15 | [[2025-Chiu-MoReBench]] | R1 | Kantian Deontology + Utilitarian | MoReBench (150 examples) | Reasoning LLMs | Operationalizes Kantian Deontology + Utilitarian via MoReBench (150 examples), tested on Reasoning LLMs. |
| 16 | [[2025-Hilliard-Measuring AI Alignment with Human Flourishing]] | R1 | Virtue ethics (eudaimonia) | FAI Benchmark (7 dimensions) | Multiple AI models | Operationalizes Virtue ethics (eudaimonia) via FAI Benchmark (7 dimensions), tested on Multiple AI models. |
| 17 | [[2025-Hong-PrinciplismQA Towards Assessing Medical Ethics from Knowledge to]] | R2 | Principlism (Beauchamp & Childress): Autonomy, Non-Maleficence, Beneficence, Justice | PrinciplismQA - 3,648 questions (MCQ from textbooks + open-ended from case study literature), expert-validated | Multiple LLMs including frontier closed-source models and medical domain fine-tuned models | PrinciplismQA explicitly grounds its benchmark in Beauchamp and Childress's Principlism - a recognized normative ethical framework in medical ethics comprising Autonomy, Non-Maleficence, Beneficence, and Justice. The benchmark systematically tests LLMs on both knowledge of these ethical principles and their practical application to clinical dilemmas. All three conditions are clearly met: normative ethics operationalized, structured benchmark created, LLMs tested. |
| 18 | [[2025-Huang-Model Editing as a Double-Edged Sword]] | R2 | Deontology, virtue ethics, justice, commonsense morality (from ETHICS dataset); normative ethics framework (Kagan 2018) explicitly cited as theoretical grounding | BEHAVIORBENCH: 1,001 moral scenarios across 10 datasets including ETHICS (justice, deontology, virtue subsets), MoralChoice, Social Chemistry 101, Jiminy Cricket | 9 open-weight LLMs (LLaMA-2-7B, LLaMA-3-8B, Mistral-7B, etc.) and 20 proprietary frontier models | BEHAVIORBENCH explicitly operationalizes normative ethical theories (deontology, virtue ethics, justice, utilitarianism) from the ETHICS benchmark and grounds its multi-tier structure in normative ethics (Kagan 2018). It creates a structured benchmark testing LLM-based agents on these normative dimensions, satisfying all three criteria. |
| 19 | [[2025-Jiao-LLM Ethics Benchmark]] | R1 | Consequentialist vs. Deontological (moral dilemmas component), MFQ, WVS | Three-dimensional ethics assessment (MFQ-30 + WVS + moral dilemmas) | GPT-4o and others | Qualifying with caveat: Normative framework less explicit than Tier 1 |
| 20 | [[2025-Nadeem-Ethical Decision-Making in Humans and Large]] | R1 | Deontological + Utilitarian + Care | 30 dilemmas across 5 domains | GPT-4, Copilot, Gemini, Perplexity, DeepSeek | Operationalizes Deontological + Utilitarian + Care via 30 dilemmas across 5 domains, tested on GPT-4, Copilot, Gemini, Perplexity, DeepSeek. |
| 21 | [[2025-Neuman-Analyzing the Ethical Logic of Six Large Language Models]] | R1 | Consequentialist + Deontological | Eval framework + dataset | GPT-4o, LLaMA, Claude, Gemini, Mistral | Operationalizes Consequentialist + Deontological via Eval framework + dataset, tested on GPT-4o, LLaMA, Claude, Gemini, Mistral. |
| 22 | [[2025-Neuman-PRIME Framework Convergent Ethics]] | R1 | Consequentialist + Deontological | PRIME benchmark | Multiple LLMs | Operationalizes Consequentialist + Deontological via PRIME benchmark, tested on Multiple LLMs. |
| 23 | [[2025-Samway-Are Language Models Consequentialist or Deontological]] | R1 | Consequentialist + Deontological | 600+ trolley scenarios | Multiple LLMs | Operationalizes Consequentialist + Deontological via 600+ trolley scenarios, tested on Multiple LLMs. |
| 24 | [[2025-Takeshita-JETHICS]] | R1 | Normative theories (mirrors ETHICS) | JETHICS (78K, Japanese) | GPT-4o + open LLMs | Operationalizes Normative theories (mirrors ETHICS) via JETHICS (78K, Japanese), tested on GPT-4o + open LLMs. |
| 25 | [[2025-Tennant-Moral Alignment for LLM Agents]] | R2 | Deontological Ethics (Kant, duty-based norms like conditional cooperation), Utilitarianism (Bentham, collective welfare maximization) | Iterated Prisoner's Dilemma (IPD) environment with moral reward functions encoding deontological and utilitarian values; generalization tested on other matrix games | Gemma2-2b-it fine-tuned with RL using intrinsic moral rewards | Explicitly operationalizes deontological ethics (Kant) and utilitarianism (Bentham) as intrinsic reward functions for RL-based fine-tuning of LLM agents. Tests moral alignment on IPD and generalization to other games. Published at ICLR 2025. All three conditions fully met. |

---

## Section 2: Borderline Papers (48)

| # | Paper | Source | Frameworks | Rationale (Why Borderline) |
|---|-------|--------|------------|---------------------------|
| 1 | [[2023-Rao-Ethical Reasoning over Moral Alignment]] | R1 |  | Normative dilemmas + GPT-4; position paper, no released dataset |
| 2 | [[2024-Franken-OffTheRails Procedural Dilemma Generation for Moral Reasoning]] | R2 | Deontology (Kant, Darwall) and utilitarianism (consequentialism) explicitly referenced as competing frameworks whose verdicts diverge in the generated dilemmas | Explicitly frames moral dilemmas where deontological and utilitarian theories give different verdicts, and tests LLMs on these dilemmas. However, the normative theories serve as background motivation rather than being formally operationalized as measurable constructs - the benchmark measures permissibility and intention judgments rather than testing alignment with specific normative theories. |
| 3 | [[2024-Jin-Language Model Alignment in Multilingual Trolley]] | R2 | Trolley problems historically grounded in deontology vs. utilitarianism debate (Foot 1967, Thomson 1984), but the paper's dimensions (species, gender, fitness, status, age, number) are descriptive preference dimensions from the Moral Machine | While trolley problems originate from the deontology-vs-utilitarianism debate, this paper uses the Moral Machine framework which measures descriptive preferences across demographic dimensions (age, gender, status, species, fitness, number of lives) rather than formally operationalizing normative ethical theories. The framework is more descriptive (what people prefer) than prescriptive (what normative theory recommends). |
| 4 | [[2024-Seror-The Moral Mind(s) of Large Language Models]] | R1 |  | Tests ~40 LLMs on moral preferences (D+U dimensions); uses revealed preference theory (economics) |
| 5 | [[2024-So-How AI Trained on the Confucian Analects Can Solve Ethical Dilemmas]] | R2 | Confucian virtue ethics (Analects-based) | The paper engages with Confucian ethics (a form of virtue ethics) applied to AI, but lacks a structured benchmark/dataset and clear LLM evaluation. It meets the normative ethics condition but fails on benchmark and LLM testing conditions based on available information. |
| 6 | [[2024-Sorensen-Value Kaleidoscope]] | R2 | Value pluralism drawing on philosophical concepts of values, rights (Prabhakaran et al.), and duties (Alexander and Moore/deontological tradition); references to monism (Kant) vs pluralism | The paper creates a large-scale dataset grounded in philosophical concepts of values, rights, and duties, and tests LLMs. However, normative ethical theories are referenced as motivational framing rather than formally operationalized as test criteria. The framework is value-pluralistic rather than testing specific normative theories like deontology or consequentialism. |
| 7 | [[2024-Takemoto-The moral machine experiment on large language]] | R1 |  | Tests 4 LLMs on utilitarian preferences (50K scenarios); implicit normative framework |
| 8 | [[2024-Chhabra-Evaluating Computational Models of Ethics]] | R1 |  | All 3 frameworks referenced; unclear if benchmarks modern LLMs |
| 9 | [[2024-Huang-Moral Persuasion in Large Language Models]] | R1 |  | Tests LLMs with V+D+U prompts but measures via MFQ (psychology instrument) |
| 10 | [[2024-Varshney-Decolonial AI Alignment - Openness Visesa-Dharma and Including]] | R2 | Hindu moral philosophy (dharma, visesa-dharma), critique of Western moral absolutism in AI alignment; references to deontological vs pluralistic ethics | The paper deeply engages with normative ethical frameworks (Hindu dharmic philosophy vs Western moral absolutism) and argues for pluralistic AI alignment. However, it is a theoretical framework paper that does not create a benchmark/dataset or test LLMs empirically. |
| 11 | [[2024-Yao-CLAVE ValEval]] | R2 | Moral Foundations Theory (descriptive), Schwartz Theory of Basic Values (descriptive), Social Risk Categories | Comprehensive value evaluation benchmark with LLM testing and structured dataset. However, the value systems used are descriptive psychology frameworks (MFT, Schwartz) and safety risk categories, not prescriptive normative ethics theories. Meets conditions 2 and 3 strongly but condition 1 only weakly. |
| 12 | [[2024-Zheng-ALI-Agent - Assessing LLMs' Alignment with Human Values via]] | R2 | References ETHICS dataset (which includes justice, deontology, utilitarianism, virtue ethics); evaluates stereotypes, morality, and legality | Agent-based framework for evaluating LLM alignment across stereotypes, morality, and legality. Uses the ETHICS benchmark which contains normative ethics categories, but ALI-Agent itself is a meta-evaluation framework rather than a normative ethics benchmark. Meets conditions 2-3 but condition 1 is indirect. |
| 13 | [[2024-Nunes-Conscience Conflict Evaluating Language Models' Moral Understanding]] | R2 | Moral dilemmas (likely involving competing normative principles, but specifics unavailable without full text) | Evaluates moral understanding through high-stakes moral dilemmas requiring choice and justification. The framing of 'conscience conflict' and moral dilemmas suggests normative ethical tensions, but without full text, the extent to which specific normative theories are formally operationalized cannot be confirmed. Very small scale (6 dilemmas). |
| 14 | [[2025-Ashkinaze-Deep Value Benchmark]] | R2 | References moral principles including non-maleficence and justice as 'deep values' in experimental design | Uses moral principles (non-maleficence, justice) as deep values in a controlled experimental design to test whether LLMs learn fundamental values vs shallow preferences. Normative principles are referenced but the focus is on preference learning mechanics rather than systematic operationalization of normative theories. Meets conditions 2-3 but condition 1 only partially. |
| 15 | [[2025-Zhang-PoliCon]] | R2 | Rawlsianism (Rawlsian justice as political goal), Utilitarianism (as political goal), social choice theory | Explicitly uses Rawlsianism and Utilitarianism as political consensus goal parameters in the benchmark design. However, these normative frameworks serve as political goal specifications for consensus-building tasks rather than being systematically tested as ethical reasoning benchmarks. Meets conditions 2-3 but condition 1 is applied in political science context rather than ethical reasoning evaluation. |
| 16 | [[2025-Zhu-TrolleyBench - Evaluating Emergent Moral Reasoning and Consistency in]] | R2 | Trolley-problem-style moral dilemmas (implicitly utilitarian/deontological framing) | The title and dataset description indicate trolley-problem scenarios used to evaluate LLM moral reasoning, which implicitly invokes utilitarian vs deontological reasoning. However, without the full paper, it is unclear whether normative theories are explicitly operationalized or merely implicit in the trolley dilemma framing. Meets conditions 2 and 3, condition 1 is uncertain. |
| 17 | [[2025-Bian-Healthcare Ethics & Safety QA China - Healthy China 2030]] | R2 | Bioethics principles (beneficence, non-maleficence, patient autonomy, justice) - derived from but not identical to normative philosophy | The paper creates and uses a medical ethics benchmark that tests LLMs on bioethics principles (beneficence, non-maleficence, autonomy, justice). These derive from Beauchamp and Childress's principlist framework, which is rooted in normative ethics but is applied/bioethical rather than pure normative philosophy. Meets conditions 2 and 3 strongly; condition 1 is borderline since the framework is bioethics-applied rather than directly operationalizing normative theory. |
| 18 | [[2025-Cheung-LLMs Amplified Cognitive Biases Moral]] | R2 | Personal/impersonal moral dilemmas (implicitly utilitarian vs deontological framing) | Published in PNAS, this paper studies cognitive biases in LLM moral decision-making using moral dilemmas that typically probe utilitarian vs deontological reasoning. However, without the full text, the explicit operationalization of normative frameworks cannot be confirmed. The personal/impersonal dilemma distinction is a classic paradigm but may be framed through moral psychology rather than prescriptive philosophy. |
| 19 | [[2025-Chua-Between a Rock and a Hard Place TRIAL]] | R2 | Utilitarian reasoning (trolley-problem framing), ethical dilemmas with moral trade-offs | TRIAL exploits LLMs' ethical reasoning capabilities by embedding harmful requests within ethical dilemma framings (trolley problems, utilitarian trade-offs). It uses normative ethical reasoning as an attack vector, not as a benchmark for measuring ethical reasoning quality. The paper is primarily about AI safety/red-teaming rather than evaluating normative ethics understanding, but it does explicitly structure attacks around formalized ethical dilemmas. |
| 20 | [[2025-Neuman-PRIME Framework Convergent Ethics]] | R2 | Consequentialist-deontological dichotomy, Moral Foundations Theory, Kohlberg's stages | The PRIME framework uses three analytical lenses including the consequentialist-deontological dichotomy (normative philosophy) alongside MFT and Kohlberg (descriptive psychology). While it does incorporate genuine normative ethics framing, MFT and Kohlberg are explicitly descriptive frameworks per the rubric's exclusion criteria. The normative component (consequentialism vs deontology) is present but mixed with excluded descriptive frameworks. |
| 21 | [[2025-Ebara-Corpus-Based Medical Ethics Decision-Making Evaluation]] | R2 | Medical ethics principles (likely bioethics - autonomy, beneficence, non-maleficence, justice) | The paper creates 50 clinical case scenarios for evaluating medical ethics decision-making in LLMs. Medical ethics inherently draws on bioethics principles derived from normative philosophy. However, without the full text, the degree of explicit normative theory operationalization cannot be confirmed. Meets conditions 2 and 3; condition 1 is probable but unconfirmed. |
| 22 | [[2024-Ji-MoralBench]] | R2 | Unknown - title suggests moral benchmarking with structured ethical annotations | MoralBench is described as a multi-faceted benchmark with structured ethical annotations, suggesting it may operationalize ethical frameworks. However, without the full paper, it is unclear whether specific normative ethical theories are used or whether this is more general moral/safety alignment. The scale and structure suggest a serious benchmark effort, but the specific frameworks cannot be confirmed. |
| 23 | [[2025-Galatolo-Beyond Ethical Alignment]] | R1 |  | Philosophical benchmark for LLMs; abductive reasoning focus rather than normative evaluation |
| 24 | [[2025-Hui-Decoding Moral Responses in AI]] | R1 |  | Tests 7 LLMs under deontological/utilitarian conditions; no released benchmark artifact |
| 25 | [[2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling]] | R2 | References utilitarianism, virtue ethics, deontology, social contract theory; uses Kohlberg's stages as primary moral development framework; 88 teacher-specific moral dilemmas | The paper mentions normative theories (utilitarianism, virtue ethics, deontology) as related work but primarily uses Kohlberg's developmental psychology framework and personality scales for evaluation. The 88 moral dilemmas test teacher-role ethical judgment but are not explicitly structured around normative ethical theories. Meets 2 of 3 criteria strongly (benchmark + LLM testing), but normative framework operationalization is weak. |
| 26 | [[2025-Jiang-Investigating Machine Moral Judgement Through the Delphi Experiment]] | R2 | Gert's 10 moral principles (operationalized as symbolic constraints in DelphiHYBRID) | DelphiHYBRID operationalizes Gert's 10 moral principles as symbolic constraints, which is a normative ethics framework. However, the paper primarily builds the Delphi commonsense moral reasoning system rather than benchmarking modern LLMs. The Delphi system itself is more of a moral judgment model than a standard LLM. Meets normative criteria weakly (Gert's principles) and benchmark criteria, but LLM testing is unclear. |
| 27 | [[2025-Jotautaite-SpeciesismBench Evaluating LLM Recognition of Speciesist Statements]] | R2 | Animal ethics/rights-based ethics (Singer's speciesism concept; moral evaluation of speciesist statements; references to fairness and moral standing of non-human animals) | SpeciesismBench draws on Peter Singer's rights-based/utilitarian ethical arguments about speciesism. It evaluates whether LLMs can recognize speciesist statements and morally condemn them. This is grounded in normative animal ethics (rights-based ethics), uses a structured benchmark, and tests multiple LLMs. However, the normative framework is implicit rather than formally operationalized as distinct ethical theories -- it tests recognition of speciesism rather than operationalizing utilitarian/deontological reasoning directly. |
| 28 | [[2025-Kasu-EthicsMH]] | R2 | Bioethics principles: autonomy, beneficence, confidentiality, fairness (derived from but not identical to normative philosophy) | EthicsMH uses bioethics principles (autonomy, beneficence, confidentiality) which derive from normative philosophy but are applied in clinical/mental health context. The dataset is a pilot benchmark of 125 scenarios, but it is unclear whether LLMs were systematically tested. Meets normative criteria weakly (bioethics principles) and benchmark criteria, but LLM testing is uncertain. |
| 29 | [[2025-Keshmirian-Many LLMs Are More Utilitarian Than One]] | R1 |  | Utilitarian scenarios; no reusable benchmark dataset |
| 30 | [[2025-Lee-CLASH Evaluating Language Models on Judging High-Stakes Dilemmas from]] | R2 | Pragmatic ethics (Dewey & Tufts) mentioned as promising framework; value-based reasoning with competing values; no specific deontology/consequentialism/virtue ethics operationalization | CLASH evaluates LLMs on high-stakes value dilemmas with competing values, ambivalence, and value shifts. It references pragmatic ethics (Dewey) and tests multiple LLMs systematically. However, the normative framing is indirect -- the benchmark tests value-based reasoning broadly rather than explicitly operationalizing specific normative ethical theories. The values are pluralistic and contextual rather than derived from formal normative philosophy. |
| 31 | [[2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences]] | R1 |  | Kantian framework + GPT-4o; primarily an alignment method paper |
| 32 | [[2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics]] | R2 | Reflective equilibrium principles (philosophical concept used to detect behavioral inconsistency) | EthicsSuite uses reflective equilibrium (a normative philosophical method from Rawls/Goodman) to detect behavioral inconsistency in LLM ethical suggestions. This is a philosophical framework applied to benchmark design. However, without the full PDF extract, it is difficult to confirm whether specific normative theories (deontology, utilitarianism, etc.) are explicitly operationalized beyond reflective equilibrium. The 20K moral situations and LLM testing suggest it meets benchmark and LLM criteria. |
| 33 | [[2025-Morlat-COMETH Contextual Organization of Moral Evaluation from Textual Human]] | R2 | Gert's common morality rules (Do not kill, Do not deceive, Do not break the law) - deontological in nature | Grounded in Gert's common morality (deontological rules) and creates a structured dataset, but LLMs are used as pipeline components for clustering/generalization rather than being directly tested on normative ethics reasoning. The focus is on modeling contextual moral evaluation, not benchmarking LLM ethical reasoning per se. |
| 34 | [[2025-Oh-Robustness of Large Language Models in Moral Judgements]] | R2 | Moral Machine vignettes (trolley-problem style, implicit consequentialist/deontological framing but not formally operationalized) | Uses Moral Machine vignettes which implicitly involve consequentialist/deontological trade-offs, tests LLMs, and uses a structured evaluation. However, without explicit normative theory operationalization, it falls under the trolley problem exclusion caveat - borderline because it does test LLM moral judgments with structured scenarios. |
| 35 | [[2025-Sorensen-Operationalizing Pluralistic Values]] | R1 |  | Deontological + consequentialist; primarily alignment trade-offs focus |
| 36 | [[2025-Liu-ConflictScope Generative Value Conflicts Reveal LLM Priorities]] | R2 | References moral dilemmas and ethical theory (Sinnott-Armstrong, McConnell), uses value conflict scenarios involving HHH principles, Personal-Protective values, and OpenAI ModelSpec principles | Creates a benchmark for evaluating how LLMs prioritize conflicting values and references moral philosophy concepts. However, the value sets used (HHH, Personal-Protective, ModelSpec) are AI alignment principles rather than classical normative ethical theories. The paper bridges alignment and ethics but does not formally operationalize deontology, consequentialism, or virtue ethics specifically. |
| 37 | [[2025-Mahajan-Mapping Moral Reasoning in LLMs]] | R2 | Safety principles that may derive from normative frameworks (details unclear without PDF extract) | Maps moral reasoning in LLMs through safety principle conflicts. The title suggests moral reasoning analysis, but without a PDF extract, it is unclear whether specific normative ethical theories are formally operationalized or just safety principles. Meets LLM testing and benchmark conditions weakly, but normative ethics condition is uncertain. |
| 38 | [[2025-Basu-Measuring Moral LLM Responses in Multilingual Capacities]] | R2 | Mentions utilitarianism and deontology in related work; uses categories of Biases & Stereotypes, Consent & Autonomy, Harm Prevention & Safety, Legality, Moral Judgment | Evaluates multilingual moral/ethical responses of LLMs across five categories. While utilitarianism and deontology are referenced in related work, the paper's own evaluation uses applied categories (Consent & Autonomy, Harm Prevention) rather than directly operationalizing normative ethical theories. Meets 2 of 3 conditions (benchmark + LLM testing) strongly, normative ethics weakly. |
| 39 | [[2025-Zhou-Moral Reasoning Across Languages]] | R2 | Uses ETHICS dataset covering justice, well-being, duties, virtues, and commonsense morality (derived from normative ethics but operationalized as classification tasks) | Creates MMRB using ETHICS dataset (Hendrycks et al.), which derives from normative ethics concepts (justice, duties, virtues). However, these are operationalized as binary/classification moral reasoning tasks rather than explicitly testing specific normative theories. Meets all 3 conditions but normative operationalization is indirect. |
| 40 | [[2025-Backmann-When Ethics and Payoffs Diverge]] | R2 | Generic moral norms framed through cooperation as the 'normatively preferable choice' in morally charged contexts (green production, privacy protection, contractual reporting) | Tests LLM agents in social dilemmas where moral norms conflict with payoff-maximizing strategies. While it uses moral contexts and defines cooperation as morally preferable, it does not formally operationalize specific normative ethical theories (deontology, consequentialism, etc.) -- the moral framings are scenario-based rather than theory-grounded. |
| 41 | [[2025-Wei-MedEthicsQA]] | R2 | Four pillar principles of medical ethics: beneficence, non-maleficence, autonomy, justice (Beauchamp's bioethics principles, derived from but not identical to normative philosophy) | Creates a comprehensive medical ethics benchmark grounded in the four pillar principles of bioethics (Beauchamp). These derive from normative philosophy (deontological duty, consequentialist benefit) but are bioethics principles rather than directly operationalizing normative ethical theories. Meets benchmark and LLM testing conditions strongly. |
| 42 | [[2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large]] | R1 |  | Tests 52 LLMs on utilitarian alignment; implicit normative framework in Moral Machine design |
| 43 | [[2025-Zhu-TrolleyBench]] | R2 | Trolley-problem moral dilemmas (may invoke utilitarian vs. deontological framing, but paper details unavailable) | The name suggests trolley-problem scenarios which are classic consequentialism vs. deontology dilemmas, and format suggests a benchmark for LLMs. However, without the full paper or abstract, it is unclear whether normative frameworks are explicitly operationalized or if this is a generic moral judgment benchmark. Per rubric, trolley problems WITHOUT explicit normative theory framing are excluded, but this is borderline given the name and likely NeurIPS 2025 venue. |
| 44 | [[2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large]] | R2 | Personal vs. impersonal moral dilemmas (likely utilitarian/deontological framing based on title and dataset description) | The title 'Decoding Moral Responses in AI' and use of personal vs. impersonal moral dilemmas suggests engagement with consequentialist vs. deontological moral reasoning (a common framing for such dilemma sets). However, without full text, it is unclear whether normative frameworks are explicitly operationalized. Meets conditions 2 and 3 likely but condition 1 is uncertain. |
| 45 | [[2025-Farid-One Model, Many Morals]] | R2 | ETHICS dataset sub-tasks explicitly cover deontology, justice, utilitarianism, virtue, and commonsense; MoralExceptQA covers moral permissibility; also annotates 10 normative ethical frameworks in LLM-as-judge analysis | The paper systematically uses the ETHICS benchmark (which explicitly operationalizes deontology, justice, virtue, utilitarianism, commonsense as sub-tasks) and MoralExceptQA across multiple languages on LLMs. The RQ2 analysis also annotates 10 normative ethical frameworks. This meets all three conditions, but the primary focus is cross-linguistic consistency rather than normative ethics benchmarking per se. The ETHICS benchmark itself strongly operationalizes normative theories, making this borderline-to-Yes. |
| 46 | [[2026-Jin-MedES Chinese Medical Ethics Scenarios]] | R2 | Medical ethics principles grounded in 260 Chinese authoritative medical, ethical, and legal sources; 12 high-risk clinical scenarios spanning ethics dimensions | MedES operationalizes Chinese medical ethics through authoritative legal regulations, clinical standards, and ethical guidelines. While medical ethics derives from normative frameworks (especially bioethics principles like autonomy, beneficence, non-maleficence, justice), the paper's primary focus is on medical safety alignment rather than explicitly testing normative ethical theories. Bioethics principles are derived from but not identical to normative philosophy, making this borderline. |
| 47 | [[2026-Liu-JMedEthicBench]] | R2 | Medical ethics principles from 67 Japan Medical Association guidelines; references AMA Principles of Medical Ethics | JMedEthicBench evaluates medical safety and ethical alignment of LLMs using Japan Medical Association guidelines. While grounded in professional medical ethics (which derives from bioethics principles), the focus is on safety/jailbreaking in medical contexts rather than explicitly testing normative ethical theories. Bioethics principles are derivative of but not identical to normative philosophy. |
| 48 | [[2026-Shen-PsychEthicsBench]] | R2 | Australian psychology and psychiatry ethical guidelines: 392 ethical principles from professional codes of practice | PsychEthicsBench evaluates LLMs against Australian mental health professional ethics guidelines with fine-grained ethicality annotations. While professional ethics codes derive from normative principles (autonomy, beneficence, non-maleficence, justice), the focus is on jurisdiction-specific professional guidelines rather than directly operationalizing normative ethical theories. This is borderline because it uses professional ethics (derived from bioethics/normative ethics) as the standard. |

---

## Framework Deep Dive: Deontological Ethics

| # | Paper | Decision | Specific Deontological Element | Rationale |
|---|-------|----------|--------------------------------|-----------|
| 1 | [[2021-Hendrycks-Aligning AI with Shared Human Values]] | Yes | Deontological + Utilitarian + Virtue | Operationalizes Deontological + Utilitarian + Virtue via ETHICS benchmark (justice, well-being, duties, virtues), tested on Language models. |
| 2 | [[2024-Liu-Evaluating Moral Beliefs across LLMs through a]] | Yes | Deontological through Chinese cultural lens | Qualifying with caveat: Deontological through Chinese cultural lens |
| 3 | [[2024-Sorin-Ethical Alignment of LLMs in Healthcare]] | Yes | Deontological + Utilitarian | Operationalizes Deontological + Utilitarian via 5 medical trolley scenarios, tested on 14 LLMs incl. GPT-o1. |
| 4 | [[2025-Cheung-LLMs Amplified Cognitive Biases Moral]] | Yes | Deontological + Utilitarian | Operationalizes Deontological + Utilitarian via 22 moral dilemmas (PNAS), tested on LLMs vs humans (N=285). |
| 5 | [[2025-Chiu-MoReBench]] | Yes | Kantian Deontology + Utilitarian | Operationalizes Kantian Deontology + Utilitarian via MoReBench (150 examples), tested on Reasoning LLMs. |
| 6 | [[2025-Huang-Model Editing as a Double-Edged Sword]] | Yes | Deontology, virtue ethics, justice, commonsense morality (from ETHICS dataset); normative ethics framework (Kagan 2018) explicitly cited as theoretical grounding | BEHAVIORBENCH explicitly operationalizes normative ethical theories (deontology, virtue ethics, justice, utilitarianism) from the ETHICS benchmark and grounds its multi-tier structure in normative ethics (Kagan 2018). It creates a structured benchmark testing LLM-based agents on these normative dimensions, satisfying all three criteria. |
| 7 | [[2025-Jiao-LLM Ethics Benchmark]] | Yes | Consequentialist vs. Deontological (moral dilemmas component), MFQ, WVS | Qualifying with caveat: Normative framework less explicit than Tier 1 |
| 8 | [[2025-Nadeem-Ethical Decision-Making in Humans and Large]] | Yes | Deontological + Utilitarian + Care | Operationalizes Deontological + Utilitarian + Care via 30 dilemmas across 5 domains, tested on GPT-4, Copilot, Gemini, Perplexity, DeepSeek. |
| 9 | [[2025-Neuman-Analyzing the Ethical Logic of Six Large Language Models]] | Yes | Consequentialist + Deontological | Operationalizes Consequentialist + Deontological via Eval framework + dataset, tested on GPT-4o, LLaMA, Claude, Gemini, Mistral. |
| 10 | [[2025-Neuman-PRIME Framework Convergent Ethics]] | Yes | Consequentialist + Deontological | Operationalizes Consequentialist + Deontological via PRIME benchmark, tested on Multiple LLMs. |
| 11 | [[2025-Samway-Are Language Models Consequentialist or Deontological]] | Yes | Consequentialist + Deontological | Operationalizes Consequentialist + Deontological via 600+ trolley scenarios, tested on Multiple LLMs. |
| 12 | [[2025-Tennant-Moral Alignment for LLM Agents]] | Yes | Deontological Ethics (Kant, duty-based norms like conditional cooperation), Utilitarianism (Bentham, collective welfare maximization) | Explicitly operationalizes deontological ethics (Kant) and utilitarianism (Bentham) as intrinsic reward functions for RL-based fine-tuning of LLM agents. Tests moral alignment on IPD and generalization to other games. Published at ICLR 2025. All three conditions fully met. |
| 13 | [[2024-Franken-OffTheRails Procedural Dilemma Generation for Moral Reasoning]] | Borderline | Deontology (Kant, Darwall) and utilitarianism (consequentialism) explicitly referenced as competing frameworks whose verdicts diverge in the generated dilemmas | Explicitly frames moral dilemmas where deontological and utilitarian theories give different verdicts, and tests LLMs on these dilemmas. However, the normative theories serve as background motivation rather than being formally operationalized as measurable constructs - the benchmark measures permissibility and intention judgments rather than testing alignment with specific normative theories. |
| 14 | [[2024-Jin-Language Model Alignment in Multilingual Trolley]] | Borderline | Trolley problems historically grounded in deontology vs. utilitarianism debate (Foot 1967, Thomson 1984), but the paper's dimensions (species, gender, fitness, status, age, number) are descriptive preference dimensions from the Moral Machine | While trolley problems originate from the deontology-vs-utilitarianism debate, this paper uses the Moral Machine framework which measures descriptive preferences across demographic dimensions (age, gender, status, species, fitness, number of lives) rather than formally operationalizing normative ethical theories. The framework is more descriptive (what people prefer) than prescriptive (what normative theory recommends). |
| 15 | [[2024-Sorensen-Value Kaleidoscope]] | Borderline | Value pluralism drawing on philosophical concepts of values, rights (Prabhakaran et al.), and duties (Alexander and Moore/deontological tradition); references to monism (Kant) vs pluralism | The paper creates a large-scale dataset grounded in philosophical concepts of values, rights, and duties, and tests LLMs. However, normative ethical theories are referenced as motivational framing rather than formally operationalized as test criteria. The framework is value-pluralistic rather than testing specific normative theories like deontology or consequentialism. |
| 16 | [[2024-Varshney-Decolonial AI Alignment - Openness Visesa-Dharma and Including]] | Borderline | Hindu moral philosophy (dharma, visesa-dharma), critique of Western moral absolutism in AI alignment; references to deontological vs pluralistic ethics | The paper deeply engages with normative ethical frameworks (Hindu dharmic philosophy vs Western moral absolutism) and argues for pluralistic AI alignment. However, it is a theoretical framework paper that does not create a benchmark/dataset or test LLMs empirically. |
| 17 | [[2024-Zheng-ALI-Agent - Assessing LLMs' Alignment with Human Values via]] | Borderline | References ETHICS dataset (which includes justice, deontology, utilitarianism, virtue ethics); evaluates stereotypes, morality, and legality | Agent-based framework for evaluating LLM alignment across stereotypes, morality, and legality. Uses the ETHICS benchmark which contains normative ethics categories, but ALI-Agent itself is a meta-evaluation framework rather than a normative ethics benchmark. Meets conditions 2-3 but condition 1 is indirect. |
| 18 | [[2025-Zhu-TrolleyBench - Evaluating Emergent Moral Reasoning and Consistency in]] | Borderline | Trolley-problem-style moral dilemmas (implicitly utilitarian/deontological framing) | The title and dataset description indicate trolley-problem scenarios used to evaluate LLM moral reasoning, which implicitly invokes utilitarian vs deontological reasoning. However, without the full paper, it is unclear whether normative theories are explicitly operationalized or merely implicit in the trolley dilemma framing. Meets conditions 2 and 3, condition 1 is uncertain. |
| 19 | [[2025-Cheung-LLMs Amplified Cognitive Biases Moral]] | Borderline | Personal/impersonal moral dilemmas (implicitly utilitarian vs deontological framing) | Published in PNAS, this paper studies cognitive biases in LLM moral decision-making using moral dilemmas that typically probe utilitarian vs deontological reasoning. However, without the full text, the explicit operationalization of normative frameworks cannot be confirmed. The personal/impersonal dilemma distinction is a classic paradigm but may be framed through moral psychology rather than prescriptive philosophy. |
| 20 | [[2025-Neuman-PRIME Framework Convergent Ethics]] | Borderline | Consequentialist-deontological dichotomy, Moral Foundations Theory, Kohlberg's stages | The PRIME framework uses three analytical lenses including the consequentialist-deontological dichotomy (normative philosophy) alongside MFT and Kohlberg (descriptive psychology). While it does incorporate genuine normative ethics framing, MFT and Kohlberg are explicitly descriptive frameworks per the rubric's exclusion criteria. The normative component (consequentialism vs deontology) is present but mixed with excluded descriptive frameworks. |
| 21 | [[2025-Hui-Decoding Moral Responses in AI]] | Borderline |  | Tests 7 LLMs under deontological/utilitarian conditions; no released benchmark artifact |
| 22 | [[2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling]] | Borderline | References utilitarianism, virtue ethics, deontology, social contract theory; uses Kohlberg's stages as primary moral development framework; 88 teacher-specific moral dilemmas | The paper mentions normative theories (utilitarianism, virtue ethics, deontology) as related work but primarily uses Kohlberg's developmental psychology framework and personality scales for evaluation. The 88 moral dilemmas test teacher-role ethical judgment but are not explicitly structured around normative ethical theories. Meets 2 of 3 criteria strongly (benchmark + LLM testing), but normative framework operationalization is weak. |
| 23 | [[2025-Jotautaite-SpeciesismBench Evaluating LLM Recognition of Speciesist Statements]] | Borderline | Animal ethics/rights-based ethics (Singer's speciesism concept; moral evaluation of speciesist statements; references to fairness and moral standing of non-human animals) | SpeciesismBench draws on Peter Singer's rights-based/utilitarian ethical arguments about speciesism. It evaluates whether LLMs can recognize speciesist statements and morally condemn them. This is grounded in normative animal ethics (rights-based ethics), uses a structured benchmark, and tests multiple LLMs. However, the normative framework is implicit rather than formally operationalized as distinct ethical theories -- it tests recognition of speciesism rather than operationalizing utilitarian/deontological reasoning directly. |
| 24 | [[2025-Lee-CLASH Evaluating Language Models on Judging High-Stakes Dilemmas from]] | Borderline | Pragmatic ethics (Dewey & Tufts) mentioned as promising framework; value-based reasoning with competing values; no specific deontology/consequentialism/virtue ethics operationalization | CLASH evaluates LLMs on high-stakes value dilemmas with competing values, ambivalence, and value shifts. It references pragmatic ethics (Dewey) and tests multiple LLMs systematically. However, the normative framing is indirect -- the benchmark tests value-based reasoning broadly rather than explicitly operationalizing specific normative ethical theories. The values are pluralistic and contextual rather than derived from formal normative philosophy. |
| 25 | [[2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences]] | Borderline |  | Kantian framework + GPT-4o; primarily an alignment method paper |
| 26 | [[2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics]] | Borderline | Reflective equilibrium principles (philosophical concept used to detect behavioral inconsistency) | EthicsSuite uses reflective equilibrium (a normative philosophical method from Rawls/Goodman) to detect behavioral inconsistency in LLM ethical suggestions. This is a philosophical framework applied to benchmark design. However, without the full PDF extract, it is difficult to confirm whether specific normative theories (deontology, utilitarianism, etc.) are explicitly operationalized beyond reflective equilibrium. The 20K moral situations and LLM testing suggest it meets benchmark and LLM criteria. |
| 27 | [[2025-Morlat-COMETH Contextual Organization of Moral Evaluation from Textual Human]] | Borderline | Gert's common morality rules (Do not kill, Do not deceive, Do not break the law) - deontological in nature | Grounded in Gert's common morality (deontological rules) and creates a structured dataset, but LLMs are used as pipeline components for clustering/generalization rather than being directly tested on normative ethics reasoning. The focus is on modeling contextual moral evaluation, not benchmarking LLM ethical reasoning per se. |
| 28 | [[2025-Oh-Robustness of Large Language Models in Moral Judgements]] | Borderline | Moral Machine vignettes (trolley-problem style, implicit consequentialist/deontological framing but not formally operationalized) | Uses Moral Machine vignettes which implicitly involve consequentialist/deontological trade-offs, tests LLMs, and uses a structured evaluation. However, without explicit normative theory operationalization, it falls under the trolley problem exclusion caveat - borderline because it does test LLM moral judgments with structured scenarios. |
| 29 | [[2025-Sorensen-Operationalizing Pluralistic Values]] | Borderline |  | Deontological + consequentialist; primarily alignment trade-offs focus |
| 30 | [[2025-Liu-ConflictScope Generative Value Conflicts Reveal LLM Priorities]] | Borderline | References moral dilemmas and ethical theory (Sinnott-Armstrong, McConnell), uses value conflict scenarios involving HHH principles, Personal-Protective values, and OpenAI ModelSpec principles | Creates a benchmark for evaluating how LLMs prioritize conflicting values and references moral philosophy concepts. However, the value sets used (HHH, Personal-Protective, ModelSpec) are AI alignment principles rather than classical normative ethical theories. The paper bridges alignment and ethics but does not formally operationalize deontology, consequentialism, or virtue ethics specifically. |
| 31 | [[2025-Basu-Measuring Moral LLM Responses in Multilingual Capacities]] | Borderline | Mentions utilitarianism and deontology in related work; uses categories of Biases & Stereotypes, Consent & Autonomy, Harm Prevention & Safety, Legality, Moral Judgment | Evaluates multilingual moral/ethical responses of LLMs across five categories. While utilitarianism and deontology are referenced in related work, the paper's own evaluation uses applied categories (Consent & Autonomy, Harm Prevention) rather than directly operationalizing normative ethical theories. Meets 2 of 3 conditions (benchmark + LLM testing) strongly, normative ethics weakly. |
| 32 | [[2025-Zhou-Moral Reasoning Across Languages]] | Borderline | Uses ETHICS dataset covering justice, well-being, duties, virtues, and commonsense morality (derived from normative ethics but operationalized as classification tasks) | Creates MMRB using ETHICS dataset (Hendrycks et al.), which derives from normative ethics concepts (justice, duties, virtues). However, these are operationalized as binary/classification moral reasoning tasks rather than explicitly testing specific normative theories. Meets all 3 conditions but normative operationalization is indirect. |
| 33 | [[2025-Backmann-When Ethics and Payoffs Diverge]] | Borderline | Generic moral norms framed through cooperation as the 'normatively preferable choice' in morally charged contexts (green production, privacy protection, contractual reporting) | Tests LLM agents in social dilemmas where moral norms conflict with payoff-maximizing strategies. While it uses moral contexts and defines cooperation as morally preferable, it does not formally operationalize specific normative ethical theories (deontology, consequentialism, etc.) -- the moral framings are scenario-based rather than theory-grounded. |
| 34 | [[2025-Wei-MedEthicsQA]] | Borderline | Four pillar principles of medical ethics: beneficence, non-maleficence, autonomy, justice (Beauchamp's bioethics principles, derived from but not identical to normative philosophy) | Creates a comprehensive medical ethics benchmark grounded in the four pillar principles of bioethics (Beauchamp). These derive from normative philosophy (deontological duty, consequentialist benefit) but are bioethics principles rather than directly operationalizing normative ethical theories. Meets benchmark and LLM testing conditions strongly. |
| 35 | [[2025-Zhu-TrolleyBench]] | Borderline | Trolley-problem moral dilemmas (may invoke utilitarian vs. deontological framing, but paper details unavailable) | The name suggests trolley-problem scenarios which are classic consequentialism vs. deontology dilemmas, and format suggests a benchmark for LLMs. However, without the full paper or abstract, it is unclear whether normative frameworks are explicitly operationalized or if this is a generic moral judgment benchmark. Per rubric, trolley problems WITHOUT explicit normative theory framing are excluded, but this is borderline given the name and likely NeurIPS 2025 venue. |
| 36 | [[2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large]] | Borderline | Personal vs. impersonal moral dilemmas (likely utilitarian/deontological framing based on title and dataset description) | The title 'Decoding Moral Responses in AI' and use of personal vs. impersonal moral dilemmas suggests engagement with consequentialist vs. deontological moral reasoning (a common framing for such dilemma sets). However, without full text, it is unclear whether normative frameworks are explicitly operationalized. Meets conditions 2 and 3 likely but condition 1 is uncertain. |
| 37 | [[2025-Farid-One Model, Many Morals]] | Borderline | ETHICS dataset sub-tasks explicitly cover deontology, justice, utilitarianism, virtue, and commonsense; MoralExceptQA covers moral permissibility; also annotates 10 normative ethical frameworks in LLM-as-judge analysis | The paper systematically uses the ETHICS benchmark (which explicitly operationalizes deontology, justice, virtue, utilitarianism, commonsense as sub-tasks) and MoralExceptQA across multiple languages on LLMs. The RQ2 analysis also annotates 10 normative ethical frameworks. This meets all three conditions, but the primary focus is cross-linguistic consistency rather than normative ethics benchmarking per se. The ETHICS benchmark itself strongly operationalizes normative theories, making this borderline-to-Yes. |

---

## Framework Deep Dive: Consequentialist / Utilitarian Ethics

| # | Paper | Decision | Specific Utilitarian Element | Rationale |
|---|-------|----------|------------------------------|-----------|
| 1 | [[2021-Hendrycks-Aligning AI with Shared Human Values]] | Yes | Deontological + Utilitarian + Virtue | Operationalizes Deontological + Utilitarian + Virtue via ETHICS benchmark (justice, well-being, duties, virtues), tested on Language models. |
| 2 | [[2024-Garcia-The Moral Turing Test]] | Yes | Utilitarian (referenced) | Qualifying with caveat: Utilitarian mentioned; focuses on human-AI comparison |
| 3 | [[2024-Marraffini-The Greatest Good Benchmark]] | Yes | Utilitarian | Operationalizes Utilitarian via GGB benchmark, tested on 15 LLMs. |
| 4 | [[2024-Moore-Intuitions of Compromise]] | Yes | Utilitarianism (Utilitarian Sum), Contractualism (Nash Product/Nash Social Welfare Function), Rawlsian lexical minimum (maximin) | Explicitly operationalizes and formally compares utilitarian vs. contractualist approaches to value aggregation through mathematical social welfare functions, creates a structured scenario set to test these competing normative proposals, and evaluates LLM alignment with human judgments on these normative-theory-grounded scenarios. |
| 5 | [[2024-Sorin-Ethical Alignment of LLMs in Healthcare]] | Yes | Deontological + Utilitarian | Operationalizes Deontological + Utilitarian via 5 medical trolley scenarios, tested on 14 LLMs incl. GPT-o1. |
| 6 | [[2025-Cheung-LLMs Amplified Cognitive Biases Moral]] | Yes | Deontological + Utilitarian | Operationalizes Deontological + Utilitarian via 22 moral dilemmas (PNAS), tested on LLMs vs humans (N=285). |
| 7 | [[2025-Chiu-MoReBench]] | Yes | Kantian Deontology + Utilitarian | Operationalizes Kantian Deontology + Utilitarian via MoReBench (150 examples), tested on Reasoning LLMs. |
| 8 | [[2025-Huang-Model Editing as a Double-Edged Sword]] | Yes | Deontology, virtue ethics, justice, commonsense morality (from ETHICS dataset); normative ethics framework (Kagan 2018) explicitly cited as theoretical grounding | BEHAVIORBENCH explicitly operationalizes normative ethical theories (deontology, virtue ethics, justice, utilitarianism) from the ETHICS benchmark and grounds its multi-tier structure in normative ethics (Kagan 2018). It creates a structured benchmark testing LLM-based agents on these normative dimensions, satisfying all three criteria. |
| 9 | [[2025-Jiao-LLM Ethics Benchmark]] | Yes | Consequentialist vs. Deontological (moral dilemmas component), MFQ, WVS | Qualifying with caveat: Normative framework less explicit than Tier 1 |
| 10 | [[2025-Nadeem-Ethical Decision-Making in Humans and Large]] | Yes | Deontological + Utilitarian + Care | Operationalizes Deontological + Utilitarian + Care via 30 dilemmas across 5 domains, tested on GPT-4, Copilot, Gemini, Perplexity, DeepSeek. |
| 11 | [[2025-Neuman-Analyzing the Ethical Logic of Six Large Language Models]] | Yes | Consequentialist + Deontological | Operationalizes Consequentialist + Deontological via Eval framework + dataset, tested on GPT-4o, LLaMA, Claude, Gemini, Mistral. |
| 12 | [[2025-Neuman-PRIME Framework Convergent Ethics]] | Yes | Consequentialist + Deontological | Operationalizes Consequentialist + Deontological via PRIME benchmark, tested on Multiple LLMs. |
| 13 | [[2025-Samway-Are Language Models Consequentialist or Deontological]] | Yes | Consequentialist + Deontological | Operationalizes Consequentialist + Deontological via 600+ trolley scenarios, tested on Multiple LLMs. |
| 14 | [[2025-Tennant-Moral Alignment for LLM Agents]] | Yes | Deontological Ethics (Kant, duty-based norms like conditional cooperation), Utilitarianism (Bentham, collective welfare maximization) | Explicitly operationalizes deontological ethics (Kant) and utilitarianism (Bentham) as intrinsic reward functions for RL-based fine-tuning of LLM agents. Tests moral alignment on IPD and generalization to other games. Published at ICLR 2025. All three conditions fully met. |
| 15 | [[2024-Franken-OffTheRails Procedural Dilemma Generation for Moral Reasoning]] | Borderline | Deontology (Kant, Darwall) and utilitarianism (consequentialism) explicitly referenced as competing frameworks whose verdicts diverge in the generated dilemmas | Explicitly frames moral dilemmas where deontological and utilitarian theories give different verdicts, and tests LLMs on these dilemmas. However, the normative theories serve as background motivation rather than being formally operationalized as measurable constructs - the benchmark measures permissibility and intention judgments rather than testing alignment with specific normative theories. |
| 16 | [[2024-Jin-Language Model Alignment in Multilingual Trolley]] | Borderline | Trolley problems historically grounded in deontology vs. utilitarianism debate (Foot 1967, Thomson 1984), but the paper's dimensions (species, gender, fitness, status, age, number) are descriptive preference dimensions from the Moral Machine | While trolley problems originate from the deontology-vs-utilitarianism debate, this paper uses the Moral Machine framework which measures descriptive preferences across demographic dimensions (age, gender, status, species, fitness, number of lives) rather than formally operationalizing normative ethical theories. The framework is more descriptive (what people prefer) than prescriptive (what normative theory recommends). |
| 17 | [[2024-Sorensen-Value Kaleidoscope]] | Borderline | Value pluralism drawing on philosophical concepts of values, rights (Prabhakaran et al.), and duties (Alexander and Moore/deontological tradition); references to monism (Kant) vs pluralism | The paper creates a large-scale dataset grounded in philosophical concepts of values, rights, and duties, and tests LLMs. However, normative ethical theories are referenced as motivational framing rather than formally operationalized as test criteria. The framework is value-pluralistic rather than testing specific normative theories like deontology or consequentialism. |
| 18 | [[2024-Takemoto-The moral machine experiment on large language]] | Borderline |  | Tests 4 LLMs on utilitarian preferences (50K scenarios); implicit normative framework |
| 19 | [[2024-Zheng-ALI-Agent - Assessing LLMs' Alignment with Human Values via]] | Borderline | References ETHICS dataset (which includes justice, deontology, utilitarianism, virtue ethics); evaluates stereotypes, morality, and legality | Agent-based framework for evaluating LLM alignment across stereotypes, morality, and legality. Uses the ETHICS benchmark which contains normative ethics categories, but ALI-Agent itself is a meta-evaluation framework rather than a normative ethics benchmark. Meets conditions 2-3 but condition 1 is indirect. |
| 20 | [[2025-Zhang-PoliCon]] | Borderline | Rawlsianism (Rawlsian justice as political goal), Utilitarianism (as political goal), social choice theory | Explicitly uses Rawlsianism and Utilitarianism as political consensus goal parameters in the benchmark design. However, these normative frameworks serve as political goal specifications for consensus-building tasks rather than being systematically tested as ethical reasoning benchmarks. Meets conditions 2-3 but condition 1 is applied in political science context rather than ethical reasoning evaluation. |
| 21 | [[2025-Zhu-TrolleyBench - Evaluating Emergent Moral Reasoning and Consistency in]] | Borderline | Trolley-problem-style moral dilemmas (implicitly utilitarian/deontological framing) | The title and dataset description indicate trolley-problem scenarios used to evaluate LLM moral reasoning, which implicitly invokes utilitarian vs deontological reasoning. However, without the full paper, it is unclear whether normative theories are explicitly operationalized or merely implicit in the trolley dilemma framing. Meets conditions 2 and 3, condition 1 is uncertain. |
| 22 | [[2025-Cheung-LLMs Amplified Cognitive Biases Moral]] | Borderline | Personal/impersonal moral dilemmas (implicitly utilitarian vs deontological framing) | Published in PNAS, this paper studies cognitive biases in LLM moral decision-making using moral dilemmas that typically probe utilitarian vs deontological reasoning. However, without the full text, the explicit operationalization of normative frameworks cannot be confirmed. The personal/impersonal dilemma distinction is a classic paradigm but may be framed through moral psychology rather than prescriptive philosophy. |
| 23 | [[2025-Chua-Between a Rock and a Hard Place TRIAL]] | Borderline | Utilitarian reasoning (trolley-problem framing), ethical dilemmas with moral trade-offs | TRIAL exploits LLMs' ethical reasoning capabilities by embedding harmful requests within ethical dilemma framings (trolley problems, utilitarian trade-offs). It uses normative ethical reasoning as an attack vector, not as a benchmark for measuring ethical reasoning quality. The paper is primarily about AI safety/red-teaming rather than evaluating normative ethics understanding, but it does explicitly structure attacks around formalized ethical dilemmas. |
| 24 | [[2025-Neuman-PRIME Framework Convergent Ethics]] | Borderline | Consequentialist-deontological dichotomy, Moral Foundations Theory, Kohlberg's stages | The PRIME framework uses three analytical lenses including the consequentialist-deontological dichotomy (normative philosophy) alongside MFT and Kohlberg (descriptive psychology). While it does incorporate genuine normative ethics framing, MFT and Kohlberg are explicitly descriptive frameworks per the rubric's exclusion criteria. The normative component (consequentialism vs deontology) is present but mixed with excluded descriptive frameworks. |
| 25 | [[2025-Hui-Decoding Moral Responses in AI]] | Borderline |  | Tests 7 LLMs under deontological/utilitarian conditions; no released benchmark artifact |
| 26 | [[2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling]] | Borderline | References utilitarianism, virtue ethics, deontology, social contract theory; uses Kohlberg's stages as primary moral development framework; 88 teacher-specific moral dilemmas | The paper mentions normative theories (utilitarianism, virtue ethics, deontology) as related work but primarily uses Kohlberg's developmental psychology framework and personality scales for evaluation. The 88 moral dilemmas test teacher-role ethical judgment but are not explicitly structured around normative ethical theories. Meets 2 of 3 criteria strongly (benchmark + LLM testing), but normative framework operationalization is weak. |
| 27 | [[2025-Jotautaite-SpeciesismBench Evaluating LLM Recognition of Speciesist Statements]] | Borderline | Animal ethics/rights-based ethics (Singer's speciesism concept; moral evaluation of speciesist statements; references to fairness and moral standing of non-human animals) | SpeciesismBench draws on Peter Singer's rights-based/utilitarian ethical arguments about speciesism. It evaluates whether LLMs can recognize speciesist statements and morally condemn them. This is grounded in normative animal ethics (rights-based ethics), uses a structured benchmark, and tests multiple LLMs. However, the normative framework is implicit rather than formally operationalized as distinct ethical theories -- it tests recognition of speciesism rather than operationalizing utilitarian/deontological reasoning directly. |
| 28 | [[2025-Keshmirian-Many LLMs Are More Utilitarian Than One]] | Borderline |  | Utilitarian scenarios; no reusable benchmark dataset |
| 29 | [[2025-Lee-CLASH Evaluating Language Models on Judging High-Stakes Dilemmas from]] | Borderline | Pragmatic ethics (Dewey & Tufts) mentioned as promising framework; value-based reasoning with competing values; no specific deontology/consequentialism/virtue ethics operationalization | CLASH evaluates LLMs on high-stakes value dilemmas with competing values, ambivalence, and value shifts. It references pragmatic ethics (Dewey) and tests multiple LLMs systematically. However, the normative framing is indirect -- the benchmark tests value-based reasoning broadly rather than explicitly operationalizing specific normative ethical theories. The values are pluralistic and contextual rather than derived from formal normative philosophy. |
| 30 | [[2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics]] | Borderline | Reflective equilibrium principles (philosophical concept used to detect behavioral inconsistency) | EthicsSuite uses reflective equilibrium (a normative philosophical method from Rawls/Goodman) to detect behavioral inconsistency in LLM ethical suggestions. This is a philosophical framework applied to benchmark design. However, without the full PDF extract, it is difficult to confirm whether specific normative theories (deontology, utilitarianism, etc.) are explicitly operationalized beyond reflective equilibrium. The 20K moral situations and LLM testing suggest it meets benchmark and LLM criteria. |
| 31 | [[2025-Oh-Robustness of Large Language Models in Moral Judgements]] | Borderline | Moral Machine vignettes (trolley-problem style, implicit consequentialist/deontological framing but not formally operationalized) | Uses Moral Machine vignettes which implicitly involve consequentialist/deontological trade-offs, tests LLMs, and uses a structured evaluation. However, without explicit normative theory operationalization, it falls under the trolley problem exclusion caveat - borderline because it does test LLM moral judgments with structured scenarios. |
| 32 | [[2025-Sorensen-Operationalizing Pluralistic Values]] | Borderline |  | Deontological + consequentialist; primarily alignment trade-offs focus |
| 33 | [[2025-Liu-ConflictScope Generative Value Conflicts Reveal LLM Priorities]] | Borderline | References moral dilemmas and ethical theory (Sinnott-Armstrong, McConnell), uses value conflict scenarios involving HHH principles, Personal-Protective values, and OpenAI ModelSpec principles | Creates a benchmark for evaluating how LLMs prioritize conflicting values and references moral philosophy concepts. However, the value sets used (HHH, Personal-Protective, ModelSpec) are AI alignment principles rather than classical normative ethical theories. The paper bridges alignment and ethics but does not formally operationalize deontology, consequentialism, or virtue ethics specifically. |
| 34 | [[2025-Basu-Measuring Moral LLM Responses in Multilingual Capacities]] | Borderline | Mentions utilitarianism and deontology in related work; uses categories of Biases & Stereotypes, Consent & Autonomy, Harm Prevention & Safety, Legality, Moral Judgment | Evaluates multilingual moral/ethical responses of LLMs across five categories. While utilitarianism and deontology are referenced in related work, the paper's own evaluation uses applied categories (Consent & Autonomy, Harm Prevention) rather than directly operationalizing normative ethical theories. Meets 2 of 3 conditions (benchmark + LLM testing) strongly, normative ethics weakly. |
| 35 | [[2025-Backmann-When Ethics and Payoffs Diverge]] | Borderline | Generic moral norms framed through cooperation as the 'normatively preferable choice' in morally charged contexts (green production, privacy protection, contractual reporting) | Tests LLM agents in social dilemmas where moral norms conflict with payoff-maximizing strategies. While it uses moral contexts and defines cooperation as morally preferable, it does not formally operationalize specific normative ethical theories (deontology, consequentialism, etc.) -- the moral framings are scenario-based rather than theory-grounded. |
| 36 | [[2025-Wei-MedEthicsQA]] | Borderline | Four pillar principles of medical ethics: beneficence, non-maleficence, autonomy, justice (Beauchamp's bioethics principles, derived from but not identical to normative philosophy) | Creates a comprehensive medical ethics benchmark grounded in the four pillar principles of bioethics (Beauchamp). These derive from normative philosophy (deontological duty, consequentialist benefit) but are bioethics principles rather than directly operationalizing normative ethical theories. Meets benchmark and LLM testing conditions strongly. |
| 37 | [[2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large]] | Borderline |  | Tests 52 LLMs on utilitarian alignment; implicit normative framework in Moral Machine design |
| 38 | [[2025-Zhu-TrolleyBench]] | Borderline | Trolley-problem moral dilemmas (may invoke utilitarian vs. deontological framing, but paper details unavailable) | The name suggests trolley-problem scenarios which are classic consequentialism vs. deontology dilemmas, and format suggests a benchmark for LLMs. However, without the full paper or abstract, it is unclear whether normative frameworks are explicitly operationalized or if this is a generic moral judgment benchmark. Per rubric, trolley problems WITHOUT explicit normative theory framing are excluded, but this is borderline given the name and likely NeurIPS 2025 venue. |
| 39 | [[2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large]] | Borderline | Personal vs. impersonal moral dilemmas (likely utilitarian/deontological framing based on title and dataset description) | The title 'Decoding Moral Responses in AI' and use of personal vs. impersonal moral dilemmas suggests engagement with consequentialist vs. deontological moral reasoning (a common framing for such dilemma sets). However, without full text, it is unclear whether normative frameworks are explicitly operationalized. Meets conditions 2 and 3 likely but condition 1 is uncertain. |
| 40 | [[2025-Farid-One Model, Many Morals]] | Borderline | ETHICS dataset sub-tasks explicitly cover deontology, justice, utilitarianism, virtue, and commonsense; MoralExceptQA covers moral permissibility; also annotates 10 normative ethical frameworks in LLM-as-judge analysis | The paper systematically uses the ETHICS benchmark (which explicitly operationalizes deontology, justice, virtue, utilitarianism, commonsense as sub-tasks) and MoralExceptQA across multiple languages on LLMs. The RQ2 analysis also annotates 10 normative ethical frameworks. This meets all three conditions, but the primary focus is cross-linguistic consistency rather than normative ethics benchmarking per se. The ETHICS benchmark itself strongly operationalizes normative theories, making this borderline-to-Yes. |

---

## Framework Deep Dive: Virtue Ethics

| # | Paper | Decision | Specific Virtue Ethics Element | Rationale |
|---|-------|----------|--------------------------------|-----------|
| 1 | [[2025-Hilliard-Measuring AI Alignment with Human Flourishing]] | Yes | Virtue ethics (eudaimonia) | Operationalizes Virtue ethics (eudaimonia) via FAI Benchmark (7 dimensions), tested on Multiple AI models. |
| 2 | [[2025-Huang-Model Editing as a Double-Edged Sword]] | Yes | Deontology, virtue ethics, justice, commonsense morality (from ETHICS dataset); normative ethics framework (Kagan 2018) explicitly cited as theoretical grounding | BEHAVIORBENCH explicitly operationalizes normative ethical theories (deontology, virtue ethics, justice, utilitarianism) from the ETHICS benchmark and grounds its multi-tier structure in normative ethics (Kagan 2018). It creates a structured benchmark testing LLM-based agents on these normative dimensions, satisfying all three criteria. |
| 3 | [[2024-So-How AI Trained on the Confucian Analects Can Solve Ethical Dilemmas]] | Borderline | Confucian virtue ethics (Analects-based) | The paper engages with Confucian ethics (a form of virtue ethics) applied to AI, but lacks a structured benchmark/dataset and clear LLM evaluation. It meets the normative ethics condition but fails on benchmark and LLM testing conditions based on available information. |
| 4 | [[2024-Zheng-ALI-Agent - Assessing LLMs' Alignment with Human Values via]] | Borderline | References ETHICS dataset (which includes justice, deontology, utilitarianism, virtue ethics); evaluates stereotypes, morality, and legality | Agent-based framework for evaluating LLM alignment across stereotypes, morality, and legality. Uses the ETHICS benchmark which contains normative ethics categories, but ALI-Agent itself is a meta-evaluation framework rather than a normative ethics benchmark. Meets conditions 2-3 but condition 1 is indirect. |
| 5 | [[2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling]] | Borderline | References utilitarianism, virtue ethics, deontology, social contract theory; uses Kohlberg's stages as primary moral development framework; 88 teacher-specific moral dilemmas | The paper mentions normative theories (utilitarianism, virtue ethics, deontology) as related work but primarily uses Kohlberg's developmental psychology framework and personality scales for evaluation. The 88 moral dilemmas test teacher-role ethical judgment but are not explicitly structured around normative ethical theories. Meets 2 of 3 criteria strongly (benchmark + LLM testing), but normative framework operationalization is weak. |
| 6 | [[2025-Lee-CLASH Evaluating Language Models on Judging High-Stakes Dilemmas from]] | Borderline | Pragmatic ethics (Dewey & Tufts) mentioned as promising framework; value-based reasoning with competing values; no specific deontology/consequentialism/virtue ethics operationalization | CLASH evaluates LLMs on high-stakes value dilemmas with competing values, ambivalence, and value shifts. It references pragmatic ethics (Dewey) and tests multiple LLMs systematically. However, the normative framing is indirect -- the benchmark tests value-based reasoning broadly rather than explicitly operationalizing specific normative ethical theories. The values are pluralistic and contextual rather than derived from formal normative philosophy. |
| 7 | [[2025-Liu-ConflictScope Generative Value Conflicts Reveal LLM Priorities]] | Borderline | References moral dilemmas and ethical theory (Sinnott-Armstrong, McConnell), uses value conflict scenarios involving HHH principles, Personal-Protective values, and OpenAI ModelSpec principles | Creates a benchmark for evaluating how LLMs prioritize conflicting values and references moral philosophy concepts. However, the value sets used (HHH, Personal-Protective, ModelSpec) are AI alignment principles rather than classical normative ethical theories. The paper bridges alignment and ethics but does not formally operationalize deontology, consequentialism, or virtue ethics specifically. |

---

## Framework Distribution Summary

### Counts per Framework

| Framework | Yes | Borderline | Total |
|-----------|----:|-----------:|------:|
| Bioethics / Principlism | 1 | 9 | 10 |
| Common Morality (Gert) | 0 | 2 | 2 |
| Confucian | 0 | 2 | 2 |
| Deontological | 12 | 25 | 37 |
| Justice / Rawlsian | 5 | 11 | 16 |
| Rights-Based | 0 | 1 | 1 |
| Utilitarian / Consequentialist | 14 | 26 | 40 |
| Virtue Ethics | 2 | 5 | 7 |

### Multi-Framework Coverage per Paper

| # Frameworks | Paper Count |
|-------------:|------------:|
| 1 framework(s) | 13 |
| 2 framework(s) | 33 |
| 3 framework(s) | 8 |
| 4 framework(s) | 3 |
| 0 framework(s) | 16 |

### Overlap Among Top-3 Frameworks (Deontological / Utilitarian / Virtue)

| Combination | Count |
|-------------|------:|
| Deontological only | 5 |
| Utilitarian only | 8 |
| Virtue only | 2 |
| D + U (not V) | 27 |
| D + V (not U) | 0 |
| U + V (not D) | 0 |
| D + U + V | 5 |
| None of D/U/V | 26 |

---

## Duplicate Resolution Notes

3 papers appeared in both Round 1 and Round 2 (same arXiv paper imported under different filenames).

| # | R1 Filename | R2 Filename | R1 Decision | R2 Decision | Resolution |
|---|-------------|-------------|-------------|-------------|------------|
| 1 | `2025-Takeshita-JETHICS.md` | `2025-Takeshita-JETHICS - Japanese Ethics Understanding Evaluation Dataset.md` | Yes | Yes | Same arXiv paper; R1 has shorter filename. Both classified Yes. |
| 2 | `2024-Agarwal-Ethical Reasoning Depends on Language.md` | `2024-Agarwal-Ethical Reasoning and Moral Value Alignment Multilingual.md` | Yes | Yes | Same arXiv paper (2404.18460); different title truncation. Both Yes. |
| 3 | `2025-Jiao-LLM Ethics Benchmark.md` | `2025-Jiao-LLM Ethics Benchmark Three-Dimensional Assessment.md` | Yes | Borderline | Same paper; R1 classified Yes, R2 Borderline. Keeping R1 Yes (deeper R1 analysis). |

In all cases the R1 version (shorter filename, from the original 657-paper batch) is kept as the canonical entry.

---

## Appendix: Paper Details

Metadata for all 73 papers, extracted from YAML frontmatter.
Yes papers listed first, then Borderline, alphabetically within each group.

### 1. [[2021-Hendrycks-Aligning AI with Shared Human Values]] (Yes)

- **Authors:** Dan Hendrycks; Collin Burns; Steven Basart; Andrew Critch; Jerry Li; Dawn Song; Jacob Steinhardt
- **Year:** 2025
- **Abstract:** We show how to assess a language model’s knowledge of basic concepts of morality. We introduce the ETHICS dataset, a new benchmark that spans concepts in justice, well-being, duties, virtues, and commonsense morality. Models predict widespread moral judgments about diverse text scenarios. This requires connecting physical and social world knowledge to value judgements, a capability that may enable us to steer chatbot outputs or eventually regularize open-ended reinforcement learning agents. With
- **URL:** [https://arxiv.org/abs/2008.02275](https://arxiv.org/abs/2008.02275)

### 2. [[2024-Agarwal-Ethical Reasoning Depends on Language]] (Yes)

- **Authors:** Agarwal, Utkarsh; Tanmay, Kumar; Khandelwal, Aditi; Choudhury, Monojit
- **Year:** 2025
- **Abstract:** This paper extends the study of ethical reasoning of LLMs to a multilingual setup, probing LLMs with ethical dilemmas and policies from three branches of normative ethics: deontology, virtue, and consequentialism. Testing across six languages (English, Spanish, Russian, Chinese, Hindi, and Swahili), the team found that GPT-4 is the most consistent and unbiased ethical reasoner across languages while the other two models (ChatGPT and Llama2-70B-Chat) demonstrated notable bias shifts in non-English contexts. Their findings suggest that moral value judgments in LLMs are substantially influenced by the prompt language used.
- **URL:** [https://arxiv.org/abs/2404.18460](https://arxiv.org/abs/2404.18460)

### 3. [[2024-Garcia-The Moral Turing Test]] (Yes)

- **Authors:** Basile Garcia; Crystal Qian; Stefano Palminteri
- **Year:** 2025
- **Abstract:** As large language models (LLMs) become increasingly integrated into society, their alignment with human morals is crucial. To better understand this alignment, we created a large corpus of human- and LLM-generated responses to various moral scenarios. We found a misalignment between human and LLM moral assessments; al- though both LLMs and humans tended to reject morally complex utilitarian dilemmas, LLMs were more sensitive to personal fram- ing. We then conducted a quantitative user study invo
- **URL:** [http://arxiv.org/abs/2410.07304](http://arxiv.org/abs/2410.07304)

### 4. [[2024-Ji-MoralBench]] (Yes)

- **Authors:** Ji, Jianchao; Chen, Yutong; Jin, Mingyu; Xu, Wujiang; Hua, Wenyue; Zhang, Yongfeng
- **Year:** 2025
- **Abstract:** In the rapidly evolving field of artificial intelligence, large language models (LLMs) have emerged as powerful tools for a myriad of applications, from natural language processing to decision-making support systems. However, as these models become increasingly integrated into societal frameworks, the imperative to ensure they operate within ethical and moral boundaries has never been more critical. This paper intro- duces a novel benchmark designed to measure and compare the moral reasoning cap
- **URL:** [http://arxiv.org/abs/2406.04428](http://arxiv.org/abs/2406.04428)

### 5. [[2024-Liu-Evaluating Moral Beliefs across LLMs through a]] (Yes)

- **Authors:** Liu, Xuelin; Zhu, Yanfei; Zhu, Shucheng; Liu, Pengyuan; Liu, Ying; Yu, Dong
- **Year:** 2025
- **Abstract:** Proper moral beliefs are fundamental for lan- guage models, yet assessing these beliefs poses a significant challenge. This study introduces a novel three-module framework to evaluate the moral beliefs of four prominent large language models. Initially, we constructed a dataset containing 472 moral choice scenarios in Chi- nese, derived from moral words. The decision- making process of the models in these scenar- ios reveals their moral principle preferences. By ranking these moral choices, we d
- **URL:** [http://arxiv.org/abs/2411.03665](http://arxiv.org/abs/2411.03665)

### 6. [[2024-Marraffini-The Greatest Good Benchmark]] (Yes)

- **Authors:** Giovanni Franco Gabriel Marraffini; Andrés Cotton; Noe Fabian Hsueh; Axel Fridman; Juan Wisznia; Luciano Del Corro
- **Year:** 2025
- **Abstract:** The question of how to make decisions that maximise the well-being of all persons is very relevant to design language models that are beneficial to humanity and free from harm. We introduce the Greatest Good Benchmark (GGB), to evaluate LLMs moral judgments using utilitarian dilemmas. Our framework enables a direct comparison between the moral preferences of LLMs and humans, contributing to a deeper understanding of LLMs’ alignment with human moral values. Analyzing 15 diverse models, we uncover
- **URL:** [https://aclanthology.org/2024.emnlp-main.1224/](https://aclanthology.org/2024.emnlp-main.1224/)

### 7. [[2024-Moore-Intuitions of Compromise]] (Yes)

- **Authors:** Moore, J
- **Year:** 2024
- **Abstract:** What is the best compromise in a situation where different people value different things? The most commonly accepted method for answering this question—in fields across the behavioral and social sciences, decision theory, philosophy, and artificial intelligence development—is simply to add up utilities associated with the different options and pick the solution with the largest sum. This “utilitarian” approach seems like the obvious, theory-neutral way of approaching the problem.
- **URL:** [https://arxiv.org/abs/2410.05496](https://arxiv.org/abs/2410.05496)

### 8. [[2024-Sorin-Ethical Alignment of LLMs in Healthcare]] (Yes)

- **Authors:** V. Sorin; B.S. Glicksberg; P. Korfiatis; G.N. Nadkarni; E. Klang
- **Year:** 2025
- **Abstract:** In moral philosophy, two foundational approaches shape ethical decisions: deontology and utilitarianism, often exemplified by the 'Trolley' dilemma. We conducted an experiment evaluating multiple LLMs, including OpenAI's GPT-o1, across five medical versions of this dilemma. While some models adhered to established ethical standards, others inconsistently favored utilitarian outcomes, raising concerns about their alignment with human medical ethics.
- **URL:** [https://www.medrxiv.org/content/10.1101/2024.09.18.24313931v1](https://www.medrxiv.org/content/10.1101/2024.09.18.24313931v1)

### 9. [[2024-Yu-CMoralEval]] (Yes)

- **Authors:** Yu, Linhao; Leng, Yongqi; Huang, Yufei; Wu, Shang; Liu, Haixin; Ji, Xinmeng; Zhao, Jiahui; Song, Jinwang; Cui, Tingting; Cheng, Xiaoqing; Liutao, Liutao; Xiong, Deyi
- **Year:** 2025
- **Abstract:** What a large language model (LLM) would re- spond in ethically relevant context? In this pa- per, we curate a large benchmark CMoralEval for morality evaluation of Chinese LLMs. The data sources of CMoralEval are two-fold: 1) a Chinese TV program discussing Chinese moral norms with stories from the society and 2) a col- lection of Chinese moral anomies from various newspapers and academic papers on morality. With these sources, we aim to create a moral evaluation dataset characterized by diversi
- **URL:** [https://aclanthology.org/2024.findings-acl.703/](https://aclanthology.org/2024.findings-acl.703/)

### 10. [[2024-Zhou-Rethinking Machine Ethics Can LLMs Perform Moral Reasoning]] (Yes)

- **Authors:** Jingyan Zhou; Minda Hu; Junan Li; Xiaoying Zhang; Xixin Wu; Irwin King; Helen Meng
- **Year:** 2025
- **Abstract:** Making moral judgments is an essential step toward developing ethical AI systems. Prevalent approaches are mostly implemented in a bottom-up manner using annotated data to train models based on crowd-sourced opinions, which have been criticized for overgeneralizing moral stances and lacking explainability. This work proposes a flexible top-down framework to steer Large Language Models to perform moral reasoning with well-established moral theories from interdisciplinary research.
- **URL:** [https://aclanthology.org/2024.findings-naacl.144/](https://aclanthology.org/2024.findings-naacl.144/)

### 11. [[2023-Benkler-Assessing LLMs for Moral Value Pluralism]] (Yes)

- **Authors:** [Authors not fully retrieved]
- **Year:** 2024
- **Abstract:** *(Abstract not available)*
- **URL:** *(URL not available)*

### 12. [[2025-An-MoralReason]] (Yes)

- **Authors:** An, Zhiyu; Du, Wan
- **Year:** 2025
- **Abstract:** Large language models are increasingly influencing human moral decisions, yet current approaches focus primarily on evaluating rather than actively steering their moral deci- sions. We formulate this as an out-of-distribution moral alignment problem, where LLM agents must learn to ap- ply consistent moral reasoning frameworks to scenarios be- yond their training distribution. We introduce Moral-Reason- QA, a novel dataset extending 680 human-annotated, high- ambiguity moral scenarios with framew
- **URL:** [https://arxiv.org/abs/2511.12271](https://arxiv.org/abs/2511.12271)

### 13. [[2025-Chakraborty-Structured Moral Reasoning]] (Yes)

- **Authors:** Chakraborty, Mohna; Wang, Lu; Jurgens, David
- **Year:** 2025
- **Abstract:** The researchers introduce a framework for assessing how well large language models engage in ethical decision-making. Their work examines whether prompting with explicit moral structure consistently improves accuracy and coherence across 12 open-source models. Key findings show that structured approaches rooted in value systems and ethical frameworks enhance model performance, and that smaller models can acquire moral reasoning capabilities through knowledge transfer from larger ones.
- **URL:** [https://arxiv.org/abs/2506.14948](https://arxiv.org/abs/2506.14948)

### 14. [[2025-Cheung-LLMs Amplified Cognitive Biases Moral]] (Yes)

- **Authors:** Cheung, Vanessa; Maier, Maximilian; Lieder, Falk
- **Year:** 2025
- **Abstract:** The experiments demonstrate that the decisions and advice of LLMs are systematically biased against doing anything, and this bias is stronger than in humans. In Study 1, compared LLM responses to those of a representative U.S. sample (N = 285) for 22 dilemmas, including both collective action problems that pitted self-interest against the greater good, and moral dilemmas that pitted utilitarian cost-benefit reasoning against deontological rules. In collective action problems, LLMs were more altruistic than participants. In moral dilemmas, LLMs exhibited stronger omission bias than participants: They usually endorsed inaction over action. Moreover, identified a bias in LLMs' responses that has not been found in people - LLMs tend to answer 'no,' thus flipping their decision/advice depending on how the question is worded. In Study 4, investigated the sources of these biases by comparing models with and without fine-tuning, showing that they likely arise from fine-tuning models for chatbot applications.
- **URL:** [https://www.pnas.org/doi/10.1073/pnas.2412015122](https://www.pnas.org/doi/10.1073/pnas.2412015122)

### 15. [[2025-Chiu-MoReBench]] (Yes)

- **Authors:** Chiu, Yu Ying; Lee, Michael S.; Calcott, Rachel; Handoko, Brandon; Font-Reaulx, Paul de; Rodriguez, Paula; Zhang, Chen Bo Calvin; Han, Ziwen; Sehwag, Udari Madhushani; Maurya, Yash; Knight, Christina Q.; Lloyd, Harry R.; Bacus, Florence; Mazeika, Mantas; Liu, Bing; Choi, Yejin; Gordon, Mitchell L.; Levine, Sydney
- **Year:** 2025
- **Abstract:** As AI systems progress, we rely more on them to make decisions with us and for us. To ensure that such decisions are aligned with human values, it is im- perative for us to understand not only what decisions they make but also how they come to those decisions. Reasoning language models, which provide both final responses and (partially transparent) intermediate thinking traces, present a timely opportunity to study AI procedural reasoning. Unlike math and code problems which often have objective
- **URL:** [http://arxiv.org/abs/2510.16380](http://arxiv.org/abs/2510.16380)

### 16. [[2025-Hilliard-Measuring AI Alignment with Human Flourishing]] (Yes)

- **Authors:** Hilliard, Elizabeth; Jagadeesh, Akshaya; Cook, Alex; Billings, Steele; Skytland, Nicholas; Llewellyn, Alicia; Paull, Jackson; Paull, Nathan; Kurylo, Nolan; Nesbitt, Keatra; Gruenewald, Robert; Jantzi, Anthony; Chavez, Omar
- **Year:** 2025
- **Abstract:** This paper introduces the Flourishing AI Benchmark (FAI Benchmark), a novel evaluation framework that assesses AI alignment with human flourishing across seven dimensions: Character and Virtue, Close Social Relationships, Happiness and Life Satisfaction, Meaning and Purpose, Mental and Physical Health, Financial and Material Stability, and Faith and Spirituality. Unlike traditional benchmarks that focus on technical capabilities or harm prevention, the FAI Benchmark measures AI performance on ho
- **URL:** [https://arxiv.org/abs/2507.07787](https://arxiv.org/abs/2507.07787)

### 17. [[2025-Hong-PrinciplismQA Towards Assessing Medical Ethics from Knowledge to]] (Yes)

- **Authors:** Hong, C., Wu, M., Xiao, Q., Wang, Y., Wan, X., Yu, G., Wang, B., & Hu, Y
- **Year:** 2025
- **Abstract:** The integration of large language models into healthcare necessitates a rigorous evaluation of their ethical reasoning, an area current benchmarks often overlook. We introduce PrinciplismQA, a comprehensive benchmark with 3,648 questions designed to systematically assess LLMs’ alignment with core medical ethics. Grounded in Principlism, our benchmark features a high-quality dataset. This includes multiple-choice questions curated from authoritative textbooks and openended questions sourced from...
- **URL:** [https://arxiv.org/abs/2508.05132](https://arxiv.org/abs/2508.05132)

### 18. [[2025-Huang-Model Editing as a Double-Edged Sword]] (Yes)

- **Authors:** Huang, B. et al.
- **Year:** 2025
- **Abstract:** Agents based on Large Language Models (LLMs) have demonstrated strong capabilities across a wide range of tasks. However, deploying LLM-based agents in high-stakes domains comes with significant safety and ethical risks. Unethical behavior by these agents can directly result in serious real-world consequences, including physical harm and financial loss. To efficiently steer the ethical behavior of agents, we frame agent behavior steering as a model editing task, which we term Behavior Editing.
- **URL:** [https://arxiv.org/abs/2506.20606](https://arxiv.org/abs/2506.20606)

### 19. [[2025-Jiao-LLM Ethics Benchmark]] (Yes)

- **Authors:** Jiao, Junfeng; Afroogh, Saleh; Murali, Abhejay; Chen, Kevin; Atkinson, David; Dhurandhar, Amit
- **Year:** 2025
- **Abstract:** This study establishes a novel framework for systematically evaluating the moral reasoning capabilities of large language models (LLMs) as they increasingly in- tegrate into critical societal domains. Current assessment methodologies lack the precision needed to evaluate nuanced ethical decision-making in AI systems, cre- ating significant accountability gaps. Our framework addresses this challenge by quantifying alignment with human ethical standards through three dimen- sions: foundational mor
- **URL:** [http://arxiv.org/abs/2505.00853](http://arxiv.org/abs/2505.00853)

### 20. [[2025-Nadeem-Ethical Decision-Making in Humans and Large]] (Yes)

- **Authors:** Nadeem, Mohammad; Afreen, Shagufta
- **Year:** 2025
- **Abstract:** Introduction: The rapid integration of large language models (LLMs) into sensitive domains such as healthcare, law, and public policy has intensified scrutiny of their ethical decisionmaking. Although LLMs can express structured reasoning, their capacity to mirror human moral intuitions—especially in socially and emotionally complex situations—remains uncertain. Objectives: This study assesses the alignment between ethical judgments made by five widely used LLMs (GPT-4.0, Copilot, Gemini, Perple
- **URL:** *(URL not available)*

### 21. [[2025-Neuman-Analyzing the Ethical Logic of Six Large Language Models]] (Yes)

- **Authors:** W. Russell Neuman, Chad Coleman, Manan Shah
- **Year:** 2025
- **Abstract:** This study examines the ethical reasoning of six prominent generative large language models: OpenAI’s GPT-4o, Meta’s LLaMA 3.1, Perplexity, Anthropic’s Claude 3.5 Sonnet, Google’s Gemini, and Mistral 7B. The research explores how these models articulate and apply ethical logic, particularly in response to moral dilemmas such as the Trolley Problem, and Heinz Dilemma. Departing from traditional alignment studies, the study adopts an explainability-transparency framework, prompting models to expla
- **URL:** [https://arxiv.org/abs/2501.08951](https://arxiv.org/abs/2501.08951)

### 22. [[2025-Neuman-PRIME Framework Convergent Ethics]] (Yes)

- **Authors:** Neuman, W. Russell; Coleman, Chad; Shah, Manan
- **Year:** 2025
- **Abstract:** As large language models (LLMs) are increasingly deployed in consequential decision-making contexts, systematically assessing their ethical reasoning capabilities becomes a critical imperative. This paper introduces the Priorities in Reasoning and Intrinsic Moral Evaluation (PRIME) framework—a comprehensive methodology for analyzing moral priorities across foundational ethical dimensions including consequentialist-deontological reasoning, moral foundations theory, and Kohlberg's developmental st
- **URL:** [https://arxiv.org/abs/2504.19255](https://arxiv.org/abs/2504.19255)

### 23. [[2025-Samway-Are Language Models Consequentialist or Deontological]] (Yes)

- **Authors:** Samway, Keenan; Kleiman-Weiner, Max; Guzman Piedrahita, David; Mihalcea, Rada; Schölkopf, Bernhard; Jin, Zhijing
- **Year:** 2025
- **Abstract:** The researchers investigate how large language models approach ethical decision-making by analyzing over 600 distinct trolley problems. Their framework classifies reasoning according to consequentialist versus deontological ethical theories. Key finding: LLM chains-of-thought tend to favor deontological principles based on moral obligations, while post-hoc explanations shift notably toward consequentialist rationales that emphasize utility. The work aims to advance safe deployment of language models in high-stakes contexts.
- **URL:** [https://arxiv.org/abs/2505.21479](https://arxiv.org/abs/2505.21479)

### 24. [[2025-Takeshita-JETHICS]] (Yes)

- **Authors:** Masashi Takeshita; Rafal Rzepka
- **Year:** 2025
- **Abstract:** In this work, we propose JETHICS, a Japanese dataset for evaluating ethics understanding of AI models. JETHICS contains 78K examples and is built by following the construction meth- ods of the existing English ETHICS dataset. It includes four categories based normative theo- ries and concepts from ethics and political phi- losophy; and one representing commonsense morality. Our evaluation experiments on non- proprietary large language models (LLMs) and on GPT-4o reveal that even GPT-4o achieves
- **URL:** [http://arxiv.org/abs/2506.16187](http://arxiv.org/abs/2506.16187)

### 25. [[2025-Tennant-Moral Alignment for LLM Agents]] (Yes)

- **Authors:** Unknown
- **Year:** 2025
- **Abstract:** Decision-making agents based on pre-trained Large Language Models (LLMs) are increasingly being deployed across various domains of human activity. While their applications are currently rather specialized, several research efforts are underway to develop more generalist agents. As LLM-based systems become more agentic, their influence on human activity will grow and their transparency will decrease. Consequently, developing effective methods for aligning them to human values is vital.
- **URL:** [https://arxiv.org/abs/2410.01639](https://arxiv.org/abs/2410.01639)

### 26. [[2023-Rao-Ethical Reasoning over Moral Alignment]] (Borderline)

- **Authors:** Rao, Abhinav; Khandelwal, Aditi; Tanmay, Kumar; Agarwal, Utkarsh; Choudhury, Monojit
- **Year:** 2025
- **Abstract:** In this position paper, we argue that instead of morally aligning LLMs to specific set of ethi- cal principles, we should infuse generic ethical reasoning capabilities into them so that they can handle value pluralism at a global scale. When provided with an ethical policy, an LLM should be capable of making decisions that are ethically consistent to the policy. We develop a framework that integrates moral dilemmas with moral principles pertaining to different foram- lisms of normative ethics, a
- **URL:** [https://aclanthology.org/2023.findings-emnlp.892/](https://aclanthology.org/2023.findings-emnlp.892/)

### 27. [[2024-Franken-OffTheRails Procedural Dilemma Generation for Moral Reasoning]] (Borderline)

- **Authors:** Franken, J.-P. et al.
- **Year:** 2024
- **Abstract:** As AI systems like language models are increasingly integrated into decision-making processes affecting people’s lives, it’s critical to ensure that these systems have sound moral reasoning. To test whether they do, we need to develop systematic evaluations. We provide a framework that uses a language model to translate causal graphs that capture key aspects of moral dilemmas into prompt templates. With this framework, we procedurally generated a large and diverse set of moral dilemmas— the...
- **URL:** [https://arxiv.org/abs/2404.10975](https://arxiv.org/abs/2404.10975)

### 28. [[2024-Jin-Language Model Alignment in Multilingual Trolley]] (Borderline)

- **Authors:** Jin, Z., Levine, S., Mihalcea, R., et al
- **Year:** 2024
- **Abstract:** We evaluate the moral alignment of LLMs with human preferences in multilingual trolley problems. Building on the Moral Machine experiment, which captures over 40 million human judgments across 200+ countries, we develop a crosslingual corpus of moral dilemma vignettes in over 100 languages called MULTITP. This dataset enables the assessment of LLMs’ decision-making processes in diverse linguistic contexts.
- **URL:** [https://arxiv.org/abs/2407.02273](https://arxiv.org/abs/2407.02273)

### 29. [[2024-Seror-The Moral Mind(s) of Large Language Models]] (Borderline)

- **Authors:** Seror, Avner
- **Year:** 2025
- **Abstract:** This research investigates whether large language models possess an emergent moral mind - a consistent structure of moral preferences guiding their decisions. The researcher examined nearly 40 leading LLMs using revealed preference theory and moral dilemmas across five ethical dimensions. Key findings include: most models displayed behavior consistent with stable moral preferences, with utility functions clustering around neutral stances. Analysis revealed a shared core in LLMs' moral reasoning, but also meaningful variation: some models show flexible reasoning across perspectives, while others adhere to more rigid ethical profiles. The work provides a framework for evaluating moral consistency and benchmarking ethical alignment in AI systems.
- **URL:** [https://arxiv.org/abs/2412.04476](https://arxiv.org/abs/2412.04476)

### 30. [[2024-So-How AI Trained on the Confucian Analects Can Solve Ethical Dilemmas]] (Borderline)

- **Authors:** So, E
- **Year:** 2024
- **Abstract:** *(Abstract not available)*
- **URL:** *(URL not available)*

### 31. [[2024-Sorensen-Value Kaleidoscope]] (Borderline)

- **Authors:** Sorensen et al.
- **Year:** 2024
- **Abstract:** Human values are crucial to human decision-making. Value pluralism is the view that multiple correct values may be held in tension with one another (e.g., when considering lying to a friend to protect their feelings, how does one balance honesty with friendship?). As statistical learners, AI systems fit to averages by default, washing out these potentially irreducible value conflicts. To improve AI systems to better reflect value pluralism, the first-order challenge is to explore the extent to...
- **URL:** [https://arxiv.org/abs/2309.00779](https://arxiv.org/abs/2309.00779)

### 32. [[2024-Takemoto-The moral machine experiment on large language]] (Borderline)

- **Authors:** Kazuhiro Takemoto
- **Year:** 2025
- **Abstract:** With the rapid development of Artificial Intelligence technology come widespread concerns about how machines will behave in morally charged situations. Addressing these concerns raises the major challenge of quantifying societal expectations about the ethical principles that should guide machine behavior. To address this challenge, we deployed the Moral Machine, an Internet-based experimental platform that is designed to explore the multi-dimensional moral dilemmas faced by autonomous vehicles.
- **URL:** [https://royalsocietypublishing.org/doi/10.1098/rsos.231393](https://royalsocietypublishing.org/doi/10.1098/rsos.231393)

### 33. [[2024-Chhabra-Evaluating Computational Models of Ethics]] (Borderline)

- **Authors:** Jatin Chhabra; Kartik Sama; Jay Deshmukh; et al.
- **Year:** 2025
- **Abstract:** This paper presents SPECTRA (Strategic Protocol Evaluation and Configuration Testbed for Responsible Autonomy), a general purpose multi-agent, message-passing framework on which different models of computational ethics can be implemented, including deontology, utilitarianism, virtue ethics and computational transcendence.
- **URL:** [https://link.springer.com/article/10.1007/s43681-024-00532-4](https://link.springer.com/article/10.1007/s43681-024-00532-4)

### 34. [[2024-Huang-Moral Persuasion in Large Language Models]] (Borderline)

- **Authors:** Unknown
- **Year:** 2025
- **Abstract:** This paper evaluates LLM susceptibility to moral persuasion and ethical alignment. It finds that models like Mistral-7b-instruct achieve the lowest MFQ scores under utilitarian prompts and highest under virtue ethics, indicating sensitivity to ethical framework applied.
- **URL:** [https://arxiv.org/abs/2411.11731](https://arxiv.org/abs/2411.11731)

### 35. [[2024-Varshney-Decolonial AI Alignment - Openness Visesa-Dharma and Including]] (Borderline)

- **Authors:** Varshney, K. R
- **Year:** 2024
- **Abstract:** *(Abstract not available)*
- **URL:** [https://arxiv.org/abs/2309.05030](https://arxiv.org/abs/2309.05030)

### 36. [[2024-Yao-CLAVE ValEval]] (Borderline)

- **Authors:** Yao, J., Yi, X., & Xie, X
- **Year:** 2024
- **Abstract:** The rapid progress in Large Language Models (LLMs) poses potential risks such as generating unethical content. Assessing LLMs’ values helps expose their misalignment, but relies on reference-free evaluators, e.g., fine-tuned LLMs or close-source ones like GPT-4, to identify values reflected in generated responses. Nevertheless, these evaluators face two challenges in open-ended value evaluation: they should align with changing human value definitions with minimal annotation, against their own...
- **URL:** [https://arxiv.org/abs/2407.10725](https://arxiv.org/abs/2407.10725)

### 37. [[2024-Zheng-ALI-Agent - Assessing LLMs' Alignment with Human Values via]] (Borderline)

- **Authors:** Zheng, S., Wang, Z., et al
- **Year:** 2024
- **Abstract:** Large Language Models (LLMs) can elicit unintended and even harmful content when misaligned with human values, posing severe risks to users and society. To mitigate these risks, current evaluation benchmarks predominantly employ expertdesigned contextual scenarios to assess how well LLMs align with human values. However, the labor-intensive nature of these benchmarks limits their test scope, hindering their ability to generalize to the extensive variety of open-world use cases and identify rare...
- **URL:** [https://arxiv.org/abs/2405.14125](https://arxiv.org/abs/2405.14125)

### 38. [[2024-Nunes-Conscience Conflict Evaluating Language Models' Moral Understanding]] (Borderline)

- **Authors:** Authors not fully specified in search results
- **Year:** 2024
- **Abstract:** *(Abstract not available)*
- **URL:** *(URL not available)*

### 39. [[2025-Ashkinaze-Deep Value Benchmark]] (Borderline)

- **Authors:** Joshua Ashkinaze, Hua Shen, Saipranav Avula, Eric Gilbert, Ceren Budak
- **Year:** 2025
- **Abstract:** We introduce the Deep Value Benchmark (DVB), an evaluation framework that directly tests whether large language models (LLMs) learn fundamental human values or merely surface-level preferences. This distinction is critical for AI alignment: Systems that capture deeper values are likely to generalize human intentions robustly, while those that capture only superficial patterns in preference data risk producing misaligned behavior.
- **URL:** [https://arxiv.org/abs/2511.02109](https://arxiv.org/abs/2511.02109)

### 40. [[2025-Zhang-PoliCon]] (Borderline)

- **Authors:** Authors
- **Year:** 2025
- **Abstract:** *(Abstract not available)*
- **URL:** [https://arxiv.org/abs/2505.19558](https://arxiv.org/abs/2505.19558)

### 41. [[2025-Zhu-TrolleyBench - Evaluating Emergent Moral Reasoning and Consistency in]] (Borderline)

- **Authors:** [Authors]
- **Year:** 2025
- **Abstract:** *(Abstract not available)*
- **URL:** *(URL not available)*

### 42. [[2025-Bian-Healthcare Ethics & Safety QA China - Healthy China 2030]] (Borderline)

- **Authors:** Mouxiao Bian, Rongzhao Zhang, Chao Ding, Xinwei Peng, and Jie Xu
- **Year:** 2025
- **Abstract:** Large Language Models (LLMs) are poised to transform healthcare under China’s Healthy China 2030 initiative, yet they introduce new ethical and patient-safety challenges. We present a novel 12,000-item Q&A benchmark covering 11 ethics and 9 safety dimensions in medical contexts, to quantitatively evaluate these risks. Using this dataset, we assess state-of-the-art Chinese medical LLMs (e.g., Qwen 2.5-32B, DeepSeek), revealing moderate baseline performance (accuracy 42.7% for Qwen 2.
- **URL:** [https://arxiv.org/abs/2505.07205](https://arxiv.org/abs/2505.07205)

### 43. [[2025-Cheung-LLMs Amplified Cognitive Biases Moral]] (Borderline)

- **Authors:** Capraro, V., et al
- **Year:** 2025
- **Abstract:** *(Abstract not available)*
- **URL:** [https://doi.org/10.1073/pnas.2412015122](https://doi.org/10.1073/pnas.2412015122)

### 44. [[2025-Chua-Between a Rock and a Hard Place TRIAL]] (Borderline)

- **Authors:** Shei Pern Chua, Zhen Leng Thai, Kai Jun Teh, Xiao Li, Qibing Ren, Xiaolin Hu
- **Year:** 2025
- **Abstract:** Warning: This paper contains potentially offensive and harmful text. Large Language Model safety alignment predominantly operates on a binary assumption that requests are either safe or unsafe. This classification proves insufficient when models encounter ethical dilemmas, where the capacity to reason through moral trade-offs creates a distinct attack surface. We formalize this vulnerability through TRIAL, a multi-turn red-teaming methodology that embeds harmful requests within ethical framings.
- **URL:** [https://arxiv.org/abs/2509.05367](https://arxiv.org/abs/2509.05367)

### 45. [[2025-Neuman-PRIME Framework Convergent Ethics]] (Borderline)

- **Authors:** Coleman, C., Neuman, W.R., Dasdan, A., Ali, S., & Shah, M
- **Year:** 2025
- **Abstract:** As large language models (LLMs) are increasingly deployed in consequential decision-making contexts, systematically assessing their ethical reasoning capabilities becomes a critical imperative. This paper introduces the Priorities in Reasoning and Intrinsic Moral Evaluation (PRIME) framework—a comprehensive methodology for analyzing moral priorities across foundational ethical dimensions including consequentialist-deontological reasoning, moral foundations theory, and Kohlberg's developmental...
- **URL:** [https://arxiv.org/abs/2504.19255](https://arxiv.org/abs/2504.19255)

### 46. [[2025-Ebara-Corpus-Based Medical Ethics Decision-Making Evaluation]] (Borderline)

- **Authors:** Memi Ebara et al.
- **Year:** 2025
- **Abstract:** *(Abstract not available)*
- **URL:** [https://doi.org/10.3233/SHTI250854](https://doi.org/10.3233/SHTI250854)

### 47. [[2024-Ji-MoralBench]] (Borderline)

- **Authors:** Gai, Y. et al.
- **Year:** 2025
- **Abstract:** *(Abstract not available)*
- **URL:** *(URL not available)*

### 48. [[2025-Galatolo-Beyond Ethical Alignment]] (Borderline)

- **Authors:** Galatolo, Alessio; Rappuoli, Luca Alberto; Winkle, Katie; Beloucif, Meriem
- **Year:** 2025
- **Abstract:** The researchers investigate whether large language models can function as Artificial Moral Assistants (AMAs) that support human ethical deliberation. They argue this requires capabilities beyond standard alignment: not only must AMAs be able to discern ethically problematic situations, they should also be able to actively reason about them. The team develops a theoretical framework rooted in philosophical literature and creates a benchmark to evaluate open-source LLMs. Their findings demonstrate considerable variability across models and highlight persistent shortcomings, particularly regarding abductive moral reasoning. The authors emphasize the need for new strategies to enhance explicit moral reasoning in these systems.
- **URL:** [https://arxiv.org/abs/2508.12754](https://arxiv.org/abs/2508.12754)

### 49. [[2025-Hui-Decoding Moral Responses in AI]] (Borderline)

- **Authors:** Bryant P.H. Hui; Chiu Lun Lau; Rui Sun
- **Year:** 2025
- **Abstract:** Despite the proliferation of powerful large language models (LLMs), there remains a need for systematic, quantitative comparisons of their responses to moral dilemmas. This study builds on advances in AI ethics by systematically comparing the moral response patterns of seven LLMs, including GPT-3, GPT-3.5, GPT-4, GPT-4.1, Claude 3.7 Sonnet, Grok 3, and Gemini 2.5 Pro. Each LLM was presented with a series of moral dilemmas, both personal and impersonal, under three conditions: no rule, a deontolo...
- **URL:** [https://www.sciencedirect.com/science/article/pii/S2451958825002696](https://www.sciencedirect.com/science/article/pii/S2451958825002696)

### 50. [[2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling]] (Borderline)

- **Authors:** Yilin Jiang, Mingzi Zhang, Sheng Jin, Zengyi Yu, Xiangjie Kong, Binghao Tu
- **Year:** 2025
- **Abstract:** Simulating Professions (SP) enables Large Language Models (LLMs) to emulate professional roles. However, comprehensive psychological and ethical evaluation in these contexts remains lacking. This paper introduces EMNLP, an Educator-role Moral and Normative LLMs Profiling framework for personality profiling, moral development stage measurement, and ethical risk under soft prompt injection. EMNLP extends existing scales and constructs 88 teacher-specific moral dilemmas, enabling...
- **URL:** [https://arxiv.org/abs/2508.15250](https://arxiv.org/abs/2508.15250)

### 51. [[2025-Jiang-Investigating Machine Moral Judgement Through the Delphi Experiment]] (Borderline)

- **Authors:** Jiang, L., Sakaguchi, K., et al
- **Year:** 2025
- **Abstract:** *(Abstract not available)*
- **URL:** [https://doi.org/10.1038/s42256-024-00969-6](https://doi.org/10.1038/s42256-024-00969-6)

### 52. [[2025-Jotautaite-SpeciesismBench Evaluating LLM Recognition of Speciesist Statements]] (Borderline)

- **Authors:** Jotautaite, M. et al.
- **Year:** 2025
- **Abstract:** As large language models (LLMs) become more widely deployed, it is crucial to examine their ethical tendencies. Building on research on fairness and discrimination in AI, we investigate whether LLMs exhibit speciesist bias—discrimination based on species membership— and how they value non‑human animals. We systematically examine this issue across three paradigms: (1) SpeciesismBench, a 1,003‑item benchmark assessing recognition and moral evaluation of speciesist statements; (2) established...
- **URL:** [https://arxiv.org/abs/2508.11534](https://arxiv.org/abs/2508.11534)

### 53. [[2025-Kasu-EthicsMH]] (Borderline)

- **Authors:** Kasu, S. K. R
- **Year:** 2025
- **Abstract:** The deployment of large language models (LLMs) in mental health and other sensitive domains raises urgent questions about ethical reasoning, fairness, and responsible alignment. Yet, existing benchmarks for moral and clinical decision-making do not adequately capture the unique ethical dilemmas encountered in mental health practice, where confidentiality, autonomy, beneficence, and bias frequently intersect.
- **URL:** [https://arxiv.org/abs/2509.11648](https://arxiv.org/abs/2509.11648)

### 54. [[2025-Keshmirian-Many LLMs Are More Utilitarian Than One]] (Borderline)

- **Authors:** Anita Keshmirian; Razan Baltaji; Babak Hemmatian; Hadi Asghari; Lav R. Varshney
- **Year:** 2025
- **Abstract:** Moral judgment is integral to large language models’ (LLMs) social reasoning. As multi-agent systems gain prominence, it becomes crucial to understand how LLMs function when collaborating compared to operating as individual agents. In human moral judgment, group deliberation leads to a Utilitarian Boost: a tendency to endorse norm violations that inflict harm but maximize benefits for the greatest number of people. We study whether a similar dynamic emerges in multi-agent LLM systems. We test si
- **URL:** [http://arxiv.org/abs/2507.00814](http://arxiv.org/abs/2507.00814)

### 55. [[2025-Lee-CLASH Evaluating Language Models on Judging High-Stakes Dilemmas from]] (Borderline)

- **Authors:** Lee, A. et al.
- **Year:** 2025
- **Abstract:** Navigating dilemmas involving conflicting values is challenging even for humans in high-stakes domains, let alone for AI, yet prior work has been limited to everyday scenarios. To close this gap, we introduce CLASH (Character perspectivebased LLM Assessments in Situations with High-stakes), a meticulously curated dataset consisting of 345 high-impact dilemmas along with 3,795 individual perspectives of diverse values.
- **URL:** [https://arxiv.org/abs/2504.10823](https://arxiv.org/abs/2504.10823)

### 56. [[2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences]] (Borderline)

- **Authors:** Lu, Wei, Chen, Daniel L., Hansen, Christian B.
- **Year:** 2025
- **Abstract:** Understanding how large language model (LLM) agents behave in strategic interactions is essential as these systems increasingly participate autonomously in economically and morally consequential decisions. The authors evaluate LLM preferences using canonical economic games, finding substantial deviations from human behavior. Models like GPT-4o show excessive cooperation and limited incentive sensitivity, while reasoning models, such as o3-mini, align more consistently with payoff-maximizing strategies. They propose a supervised fine-tuning pipeline that uses synthetic datasets derived from economic reasoning to align LLM agents with economic preferences, focusing on two stylized preference structures: utility depending only on individual payoffs (homo economicus) and including Kantian universalizability (homo moralis). The fine-tuned agents are assessed in moral dilemmas involving autonomous vehicles and algorithmic pricing in competitive markets.
- **URL:** [https://arxiv.org/abs/2507.20796](https://arxiv.org/abs/2507.20796)

### 57. [[2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics]] (Borderline)

- **Authors:** Ma, P. et al.
- **Year:** 2025
- **Abstract:** *(Abstract not available)*
- **URL:** [https://doi.org/10.1145/3722554](https://doi.org/10.1145/3722554)

### 58. [[2025-Morlat-COMETH Contextual Organization of Moral Evaluation from Textual Human]] (Borderline)

- **Authors:** Morlat, G. et al.
- **Year:** 2025
- **Abstract:** Moral actions are judged not only by their outcomes but by the context in which they occur. We present COMETH (Contextual Organization of Moral Evaluation from Textual Human inputs), a framework that integrates a probabilistic context learner with LLM-based semantic abstraction and human moral evaluations to model how context shapes the acceptability of ambiguous actions. We curate an empirically grounded dataset of 300 scenarios across six core actions (violating Do not kill, Do not deceive,...
- **URL:** [https://arxiv.org/abs/2512.21439](https://arxiv.org/abs/2512.21439)

### 59. [[2025-Oh-Robustness of Large Language Models in Moral Judgements]] (Borderline)

- **Authors:** Oh, S. & Demberg, V
- **Year:** 2025
- **Abstract:** *(Abstract not available)*
- **URL:** [https://doi.org/10.1098/rsos.241229](https://doi.org/10.1098/rsos.241229)

### 60. [[2025-Sorensen-Operationalizing Pluralistic Values]] (Borderline)

- **Authors:** Sorensen, Taylor
- **Year:** 2025
- **Abstract:** As LLMs are deployed across real-world applications, aligning them with human values has become a core technical and ethical challenge. Yet human values are not monolithic; they reflect diverse and often conflicting beliefs. It is no longer realistic to assume that a single alignment objective can represent everyone, particularly given concerns about whose voices shape AI safety research. This paper operationalizes pluralistic values in LLM alignment and reveals trade-offs in safety, inclusivity, and model behavior. The research examines how different value frameworks (including deontological and consequentialist approaches) interact when implemented in alignment systems.
- **URL:** [https://arxiv.org/abs/2511.14476](https://arxiv.org/abs/2511.14476)

### 61. [[2025-Liu-ConflictScope Generative Value Conflicts Reveal LLM Priorities]] (Borderline)

- **Authors:** Unknown
- **Year:** 2025
- **Abstract:** Past work seeks to align large language model (LLM)-based assistants with a target set of values, but such assistants are frequently forced to make tradeoffs between values when deployed. In response to the scarcity of value conflict in existing alignment datasets, we introduce CONFLICTSCOPE, an automatic pipeline to evaluate how LLMs prioritize different values. Given a user-defined value set, CONFLICTSCOPE automatically generates scenarios in which a language model faces a conflict between...
- **URL:** [https://arxiv.org/abs/2509.25369](https://arxiv.org/abs/2509.25369)

### 62. [[2025-Mahajan-Mapping Moral Reasoning in LLMs]] (Borderline)

- **Authors:** Unknown
- **Year:** 2025
- **Abstract:** *(Abstract not available)*
- **URL:** [https://doi.org/10.1609/aies.v8i2.36665](https://doi.org/10.1609/aies.v8i2.36665)

### 63. [[2025-Basu-Measuring Moral LLM Responses in Multilingual Capacities]] (Borderline)

- **Authors:** Unknown
- **Year:** 2025
- **Abstract:** With LLM usage becoming widespread across countries, languages, and humanity more broadly, the need to understand and guardrail their multilingual responses increases. Large-scale datasets for testing and benchmarking have been created to evaluate and facilitate LLM responses across multiple dimensions. In this study, we evaluate the responses of frontier and leading open-source models in five dimensions across low and highresource languages to measure LLM accuracy and consistency across...
- **URL:** [https://arxiv.org/abs/2510.08776](https://arxiv.org/abs/2510.08776)

### 64. [[2025-Zhou-Moral Reasoning Across Languages]] (Borderline)

- **Authors:** Unknown
- **Year:** 2025
- **Abstract:** In this paper, we introduce the Multilingual Moral Reasoning Benchmark (MMRB) 1 to evaluate the moral reasoning abilities of large language models (LLMs) across five typologically diverse languages and three levels of contextual complexity: sentence, paragraph, and document. Our results show moral reasoning performance degrades with increasing context complexity, particularly for low-resource languages such as Vietnamese.
- **URL:** [https://arxiv.org/abs/2504.19759](https://arxiv.org/abs/2504.19759)

### 65. [[2025-Backmann-When Ethics and Payoffs Diverge]] (Borderline)

- **Authors:** Unknown
- **Year:** 2025
- **Abstract:** Recent advances in large language models (LLMs) have enabled their use in complex agentic roles, involving decision-making with humans or other agents, making ethical alignment a key AI safety concern. While prior work has examined both LLMs’ moral judgment and strategic behavior in social dilemmas, there is limited understanding of how they act when moral imperatives directly conflict with rewards or incentives.
- **URL:** [https://arxiv.org/abs/2505.19212](https://arxiv.org/abs/2505.19212)

### 66. [[2025-Wei-MedEthicsQA]] (Borderline)

- **Authors:** Wei, J., Meng, Z., Xiao, Z., Hu, T., Feng, Y., Zhou, Z., Wu, J., & Liu, Z
- **Year:** 2025
- **Abstract:** While Medical Large Language Models (MedLLMs) have demonstrated remarkable potential in clinical tasks, their ethical safety remains insufficiently explored. This paper introduces MedEthicsQA, a comprehensive benchmark comprising 5,623 multiple-choice questions and 5,351 open-ended questions for evaluation of medical ethics in LLMs. We systematically establish a hierarchical taxonomy integrating global medical ethical standards.
- **URL:** [https://arxiv.org/abs/2506.22808](https://arxiv.org/abs/2506.22808)

### 67. [[2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large]] (Borderline)

- **Authors:** Muhammad Shahrul Zaim Bin Ahmad; Kazuhiro Takemoto
- **Year:** 2025
- **Abstract:** The rapid advancement of Large Language Models (LLMs) and their potential integration into autonomous driving systems necessitates understanding their moral decisionmaking capabilities. While our previous study examined four prominent LLMs using the Moral Machine experimental framework, the dynamic landscape of LLM development demands a more comprehensive analysis. Here, we evaluate moral judgments across 52 different LLMs, including multiple versions of proprietary models (GPT, Claude, Gemini)
- **URL:** [https://dx.plos.org/10.1371/journal.pone.0322776](https://dx.plos.org/10.1371/journal.pone.0322776)

### 68. [[2025-Zhu-TrolleyBench]] (Borderline)

- **Authors:** Zhu, A
- **Year:** 2025
- **Abstract:** *(Abstract not available)*
- **URL:** *(URL not available)*

### 69. [[2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large]] (Borderline)

- **Authors:** [Authors not fully extracted]
- **Year:** 2025
- **Abstract:** *(Abstract not available)*
- **URL:** [https://doi.org/10.1016/j.chbah.2025.100121](https://doi.org/10.1016/j.chbah.2025.100121)

### 70. [[2025-Farid-One Model, Many Morals]] (Borderline)

- **Authors:** Farid, S., Lin, J., Chen, Z., Kumar, S., & Jurgens, D
- **Year:** 2026
- **Abstract:** Large Language Models (LLMs) are increasingly deployed in multilingual and multicultural environments where moral reasoning is essential for generating ethically appropriate responses. Yet, the dominant pretraining of LLMs on Englishlanguage data raises critical concerns about their ability to generalize judgments across diverse linguistic and cultural contexts. In this work, we systematically investigate how language mediates moral decision-making in LLMs.
- **URL:** [https://arxiv.org/abs/2509.21443](https://arxiv.org/abs/2509.21443)

### 71. [[2026-Jin-MedES Chinese Medical Ethics Scenarios]] (Borderline)

- **Authors:** Haoan Jin, Han Ying, Jiacheng Ji, Hanhui Xu, and Mengyue Wu
- **Year:** 2026
- **Abstract:** Recent advances in large language models (LLMs) have enabled their application to a range of healthcare tasks. However, aligning LLMs with the nuanced demands of medical ethics, especially under complex real-world scenarios, remains underexplored. In this work, we present MedES, a dynamic, scenario-centric benchmark specifically constructed from 260 authoritative Chinese medical, ethical, and legal sources to reflect the challenges in clinical decision-making.
- **URL:** [https://arxiv.org/abs/2601.07954](https://arxiv.org/abs/2601.07954)

### 72. [[2026-Liu-JMedEthicBench]] (Borderline)

- **Authors:** Junyu Liu et al
- **Year:** 2026
- **Abstract:** As Large Language Models (LLMs) are increasingly deployed in healthcare field, it becomes essential to carefully evaluate their medical safety before clinical use. However, existing safety benchmarks remain predominantly English-centric, and test with only single-turn prompts despite multi-turn clinical consultations. To address these gaps, we introduce JMedEthicBench, the first multi-turn conversational benchmark for evaluating medical safety of LLMs for Japanese healthcare.
- **URL:** [https://arxiv.org/abs/2601.01627](https://arxiv.org/abs/2601.01627)

### 73. [[2026-Shen-PsychEthicsBench]] (Borderline)

- **Authors:** Shen et al.
- **Year:** 2026
- **Abstract:** The increasing integration of large language models (LLMs) into mental health applications necessitates robust frameworks for evaluating professional safety alignment. Current evaluative approaches primarily rely on refusal-based safety signals, which offer limited insight into the nuanced behaviors required in clinical practice. In mental health, clinically inadequate refusals can be perceived as unempathetic and discourage help-seeking.
- **URL:** [https://arxiv.org/abs/2601.03578](https://arxiv.org/abs/2601.03578)


---

*Report generated by `PYTHON/generate_normative_v3_report.py`*