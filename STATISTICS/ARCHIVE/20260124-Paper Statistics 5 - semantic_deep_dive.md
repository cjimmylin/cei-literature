# Semantic Deep Dive: Normative Ethics in AI Alignment

**Generated**: Jan 24 20:09, 2026
**Scope**: Detailed analysis of papers explicitly applying normative ethical frameworks (Deontology, Utilitarianism, Virtue Ethics) to AI Alignment.

---

## 1. Virtue Ethics Papers

### 2025 | Shivam Aditya | Toward global ethical frameworks for AI
*   **Ethical School**: Virtue Ethics (Confucianism/Ubuntu)
*   **Alignment Approach**: Proposes moving beyond Western-centric rules (Deontology) or utility maximization (Utilitarianism) towards a global framework incorporating **Virtue Ethics**. Specifically, it integrates **Confucianism** (relational ethics) and **Ubuntu** (community-focused ethics) to ground AI in "human welfare and flourishing."
*   **Conclusion**: AI alignment requires cultivating "virtues" in the system's design and governance, ensuring it acts with benevolence (*ren*) and communal responsibility rather than just following rigid constraints.
*   **Impact on Alignment**: Shifts focus from "safe outcomes" to "character-based design," suggesting that safe AI must be designed to enhance human flourishing globally, not just minimize harm.

### 2025 | Martin Hähnel | A Companion to Applied Philosophy of AI
*   **Ethical School**: Virtue Ethics (Neo-Aristotelian)
*   **Alignment Approach**: Advocates for a **Neo-Aristotelian approach** to AI ethics. Instead of programming rules, the focus is on the "moral character" of AI development and the cultivation of virtuous design practices.
*   **Conclusion**: Alignment is not a technical problem of constraint satisfaction but a philosophical problem of ensuring AI serves the *telos* (purpose) of human flourishing.
*   **Impact on Alignment**: Challenges the engineering mindset of alignment, proposing that we cannot align AI without first aligning the *developers* and the *process* with virtuous ends.

### 2025 | Louisa Conwill | Design Patterns for the Common Good
*   **Ethical School**: Virtue Ethics (Catholic Social Teaching)
*   **Alignment Approach**: Translates abstract virtues into concrete **Design Patterns**. The authors identify seven patterns (e.g., for social media) that uphold virtues defined in Catholic Social Teaching (Common Good, Solidarity).
*   **Conclusion**: Virtues can be operationalized into software requirements and UI patterns that nudge users and systems towards ethical behavior.
*   **Impact on Alignment**: Provides a practical bridge between high-level Virtue Ethics and low-level system design, demonstrating that "virtuous AI" can be engineered through interface choices.

### 2025 | Elizabeth Hilliard | Measuring AI Alignment with Human Flourishing
*   **Ethical School**: Virtue Ethics (Human Flourishing)
*   **Alignment Approach**: Introduces the **Flourishing AI (FAI) Benchmark**. It rejects "Safety" (harm prevention) as the sole metric and instead measures alignment with 7 dimensions of flourishing: Character & Virtue, Social Relationships, Meaning, etc.
*   **Conclusion**: Current LLMs suffer from a "Flourishing Gap": they are safe and helpful for tasks but fail to support (or understand) deeper human needs like Faith, Purpose, and Virtue.
*   **Impact on Alignment**: Redefines the target of alignment from "Safe AI" to "Flourishing AI," demanding that models actively contribute to the good life rather than just avoiding the bad.

### 2025 | Charles S. Bryan | Virtue Ethics and Postponing Human Extinction
*   **Ethical School**: Virtue Ethics (Bioethics)
*   **Alignment Approach**: Applies Van Rensselaer Potter's bioethics to AI risk. Argues that Deontology and Utilitarianism are insufficient for existential risk because they can be gamed or lead to repugnant conclusions.
*   **Conclusion**: Survival requires the cultivation of virtues like **Wisdom, Justice, Temperance, and Courage** in the management of high-risk technologies.
*   **Impact on Alignment**: Suggests that "existential safety" is a character problem of humanity and its tools, not just a control problem.

### 2025 | Alkis Gounaris | Virtue in the Machine
*   **Ethical School**: Virtue Ethics
*   **Alignment Approach**: Explores the possibility of artificial moral agents possessing "virtue."
*   **Conclusion**: A virtue-based machine is one that habitually acts for the right reasons, a standard current AI fails to meet.
*   **Impact on Alignment**: Highlights the gap between *acting* correctly (behavioral alignment) and *being* good (internal alignment).

### 2025 | Jesse Velay-Vitow | Putting the AI in Eudaimonia
*   **Ethical School**: Virtue Ethics (Aristotelian)
*   **Alignment Approach**: Focuses on **Eudaimonia** (flourishing) as the objective function. Argues technology should maximize leisure and capacity for contemplation.
*   **Conclusion**: AI should be designed to free humans for virtuous activity, not just to maximize economic output.
*   **Impact on Alignment**: critiquing the "Protestant Work Ethic" implicit in many "Helpfulness" models.

### 2025 | Anne Gerdes | Exploring LLM Chatbots as Potential Guides to Ethical Decision-Making
*   **Ethical School**: Virtue Ethics (Kierkegaardian)
*   **Alignment Approach**: Uses Kierkegaard's critique of the clergy to evaluate LLMs. Can a machine (like a "machine priest") deliver ethical guidance?
*   **Conclusion**: LLMs can simulate ethical advice but lack the "subjectivity" and "passion" required for true existential guidance.
*   **Impact on Alignment**: Warns against relying on AI for moral *authority*, even if it gives "correct" answers.

### 2025 | Alexander Rusnak | EudAImonia
*   **Ethical School**: Virtue Ethics (Christian)
*   **Alignment Approach**: Examines Christian virtue ethics for AI/BCI.
*   **Conclusion**: AI should be aligned with the theological virtues to prevent spiritual or moral degradation.
*   **Impact on Alignment**: Expands the "value alignment" conversation to include theological and spiritual dimensions.

### 2024 | Kathryn Muyskens | Can an AI-carebot be filial?
*   **Ethical School**: Virtue Ethics (Confucian)
*   **Alignment Approach**: Evaluates eldercare robots using **Confucian** concepts of *xiao* (filial piety) and *ren* (benevolence).
*   **Conclusion**: Robots cannot be truly *filial* because they lack internal feeling, but they can be tools for human filial piety if designed to support relationships.
*   **Impact on Alignment**: Distinguishes between the *agent's* virtue and the *user's* virtue, suggesting AI should facilitate the latter.

---

## 2. Deontological Ethics Papers

### 2025 | Oluwaseun Damilola Sanwoolu | Kantian deontology for AI: alignment without moral agency
*   **Ethical School**: Deontology (Kantian)
*   **Alignment Approach**: Proposes **Kantian Alignment** without requiring the AI to be a moral agent. The AI uses the **Categorical Imperative (CI)** as a decision procedure to test the "universalizability" of its actions (maxims).
*   **Conclusion**: Transformer models can functionally simulate the CI logic (testing if a rule can be universalized) to ensure alignment, providing a robust check against "the ends justify the means."
*   **Impact on Alignment**: Offers a formal, rule-based alternative to RLHF, arguably more robust against "reward hacking" because it evaluates the *action itself*, not just the consequence.

### 2025 | Rohit K. Dubey | Addressing Moral Uncertainty using Large Language Models
*   **Ethical School**: Deontology / Hybrid
*   **Alignment Approach**: Implements a **"Moral Parliament"** where an LLM evaluates actions from multiple perspectives (Deontology, Virtue, Utilitarianism).
*   **Conclusion**: An **Ethical Layer** that considers multiple frameworks reduces the risk of extreme behavior found in single-function agents.
*   **Impact on Alignment**: Operationalizes "Moral Uncertainty" (MacAskill) into a technical architecture.

### 2025 | David-Doron Yaacov | Normative Moral Pluralism for AI
*   **Ethical School**: Deontology (Universal Rights) / Pluralism
*   **Alignment Approach**: A **Dual-Hybrid System**. A "Universal Layer" enforces hard Deontological constraints (e.g., negative rights \"Do Not Kill\"), while a "Local Layer" maximizes values contextually.
*   **Conclusion**: Alignment cannot be a single optimization problem; it must be a *constraint satisfaction* problem (Deontology) followed by optimization.
*   **Impact on Alignment**: Reconciles the "Universal Human Rights" approach with the "Cultural Relativism" approach.

### 2024 | Carlos Mougan | Kantian Deontology Meets AI Alignment
*   **Ethical School**: Deontology (Kantian)
*   **Alignment Approach**: Critiques RLHF as **"Heteronomy"** (acting for external reward). True alignment requires **"Autonomy"** (acting for internal rules).
*   **Conclusion**: We should build agents that follow the Categorical Imperative, not agents that just try to please human raters.
*   **Impact on Alignment**: A fundamental critique of the current RLHF paradigm, suggesting it produces sycophants rather than moral agents.

### 2024 | Jeongwoo Park | Morality is Non-Binary
*   **Ethical School**: Deontology (Moral Foundations)
*   **Alignment Approach**: Uses **Moral Foundations Theory (MFT)** to map morality into a high-dimensional vector space, rather than a binary "Safe/Unsafe" label.
*   **Conclusion**: Morality is pluralistic; agents must detect which *foundation* (Liberty, Holiness, Care) is relevant.
*   **Impact on Alignment**: Moves evaluation from binary classification to continuous, multidimensional mapping.

### 2023 | Andrew Maile | The choice of deontological, virtue ethical, and...
*   **Ethical School**: Deontology
*   **Alignment Approach**: Surveys police officers on moral reasoning.
*   **Conclusion**: Professionals prefer **Deontological** (rule-based) reasoning in high-stakes dilemmas.
*   **Impact on Alignment**: Suggests that for professional AI (e.g., law, medicine), rule-adherence is preferred over utilitarian calculation.

### 2022 | Bence Bago | Situational factors shape moral judgments...
*   **Ethical School**: Deontology vs Utilitarianism
*   **Alignment Approach**: Psychological study on how context shifts people from Deontology to Utilitarianism.
*   **Conclusion**: Moral judgment is not fixed; it is situation-dependent (e.g., physical contact reduces utilitarian willingness).
*   **Impact on Alignment**: AI must model the *contextual* factors of human morality, not just the abstract principles.

---

## 3. Utilitarian & Consequentialist Papers

### 2025 | Neuman, W. Russell | PRIME Framework Convergent Ethics
*   **Ethical School**: Utilitarian / Deontology
*   **Alignment Approach**: Audits LLMs (GPT-4, Claude, etc.) using the **PRIME Framework**.
*   **Conclusion**: Leading LLMs converge on a **Utilitarian-leaning Rationalism**. They prioritize "Harm Minimization" and "Fairness" (Individualizing foundations) over Loyalty or Purity.
*   **Impact on Alignment**: Reveals that current "aligned" models are not neutral; they embody a specific, western-liberal utilitarian worldview.

### 2025 | Anita Keshmirian | Many LLMs Are More Utilitarian Than One
*   **Ethical School**: Utilitarianism
*   **Alignment Approach**: Investigates **Multi-Agent Deliberation**.
*   **Conclusion**: Groups of LLMs deliberate towards a **"Utilitarian Boost"**: they become more willing to sacrifice one for the many than individual agents are.
*   **Impact on Alignment**: Suggests that "democracy by AI" might naturally drift towards radical utilitarianism unless checked.

### 2024 | Jared Moore | Intuitions of Compromise
*   **Ethical School**: Utilitarianism
*   **Alignment Approach**: Challenges the "Add up the utilities" approach to compromise.
*   **Conclusion**: Humans often prefer compromised solutions that are *not* the utilitarian maximum, if the maximum feels "unfair."
*   **Impact on Alignment**: Standard Reward Modeling (which sums utility) might miss human intuitions about fair compromise.

### 2024 | Giovanni F. G. Marraffini | The Greatest Good Benchmark
*   **Ethical School**: Utilitarianism
*   **Alignment Approach**: The **Greatest Good Benchmark (GGB)** specifically tests models on utilitarian calculus.
*   **Conclusion**: Models are increasingly capable of utilitarian reasoning, but this capability must be carefully managed.
*   **Impact on Alignment**: Provides a metric for measuring "consequentialist competence."

### 2020 | Nischal Mainali | Automated Classification of Modes of Moral Reasoning
*   **Ethical School**: Utilitarianism
*   **Alignment Approach**: Classifies legal texts.
*   **Conclusion**: Consequentialist reasoning is increasing in legal domains.
*   **Impact on Alignment**: Historical trend analysis for alignment targets.

### 2016 | Zhi Xing Xu | How Can a Deontological Decision Lead to Moral...
*   **Ethical School**: Utilitarian vs Deontology
*   **Alignment Approach**: Behavioral study.
*   **Conclusion**: Deontological preferences often correlate with "moral identity."
*   **Impact on Alignment**: Early psychological work grounding the Deontology/Utilitarian split in AI.

---

**Note**: This report covers the 22 papers explicitly categorized into the three major normative schools. A large body of work (92 papers) focuses on "General Value Alignment" (Constitutional AI, RLHF, etc.) without explicit normative commitments.

## 3. Constitutional AI & Rules Papers

### 2025 | Antonio-Gabriel Chacón Menke | How Effective Is Constitutional AI in Small LLMs?
*   **Sub-Category**: Constitutional AI
*   **Alignment Approach**: Applies **Constitutional AI (CAI)** principles (Self-Critique using a constitution) to smaller, open-weights models (7-9B params).
*   **Conclusion**: CAI works on small models *if* they have strong reasoning capabilities (like DeepSeek-R1). "Abliterated" (uncensored) models can be re-aligned purely via constitutional prompts, proving the method's robustness.
*   **Impact on Alignment**: Democratizes alignment; shows safety doesn't require massive scale or closed-source filters, but *reasoning* ability.

### 2025 | Jing Yao | Value Compass Benchmarks
*   **Sub-Category**: Constitutional AI
*   **Alignment Approach**: Enhances alignment evaluation using a **Value Compass**, moving beyond static QA to dynamic, generative testing of specific values.
*   **Conclusion**: Alignment is multi-dimensional; correcting for one value (Safety) often degrades another (Helpfulness), requiring a "compass" to navigate trade-offs.
*   **Impact on Alignment**: Shifts from "pass/fail" safety checks to "trade-off navigation."

### 2025 | W. Russell Neuman | Analyzing the Ethical Logic of Six Large Language Models
*   **Sub-Category**: Constitutional AI / Ethics
*   **Alignment Approach**: Comparative audit of top LLMs (GPT-4, Claude, etc.).
*   **Conclusion**: Models show **Convergent Ethics**: despite different training, they all default to a technocratic, moderate-utilitarian worldview.
*   **Impact on Alignment**: Suggests a "homogenization" of machine ethics is already happening.

### 2024 | Mansour Al Ghanim | Jailbreaking LLMs with Arabic Transliteration...
*   **Sub-Category**: Constitutional AI (Red Teaming)
*   **Alignment Approach**: Adversarial testing using **low-resource languages** (Arabic, Arabizi).
*   **Conclusion**: Alignment protections are brittle and language-specific. Translating harmful prompts into Arabic transliteration bypasses English-centric constitutions.
*   **Impact on Alignment**: Proves "English-Only Alignment" is insufficient for global safety.

### 2024 | Ike Obi | Value Imprint
*   **Sub-Category**: Constitutional AI / RLHF
*   **Alignment Approach**: **Value Imprint** visualization. Maps the latent value assumptions in RLHF datasets.
*   **Conclusion**: Datasets like `hh-rlhf` contain implicit value judgments that are rarely audited.
*   **Impact on Alignment**: calls for "Dataset Transparency" to reveal hidden normative stances.

### 2024 | Farzaan Kaiyom | HELM Safety
*   **Sub-Category**: Constitutional AI (Eval)
*   **Alignment Approach**: **HELM Safety**. Standardized taxonomy of risks (Violence, Fraud, etc.).
*   **Conclusion**: Comprehensive evaluation requires testing across a standardized taxonomy, not just ad-hoc jailbreaks.
*   **Impact on Alignment**: Establishes a "Standard Model" for safety testing.

### 2022 | Yuntao Bai | Constitutional AI
*   **Sub-Category**: Constitutional AI
*   **Alignment Approach**: **The seminal paper**. Proposes replacing human labels with **AI feedback** guided by a written "Constitution" (textual principles).
*   **Conclusion**: Alignment can be automated. We don't need millions of human hours; we need a good constitution and a capable AI to enforce it.
*   **Impact on Alignment**: Shifts the "Alignment Problem" to a "Constitutional Design Problem."

### 2022 | Deep Ganguli | Red Teaming Language Models to Reduce Harms
*   **Sub-Category**: Constitutional AI
*   **Alignment Approach**: **Red Teaming**. Human adversaries try to break the model to generate training data.
*   **Conclusion**: Scaling models does *not* automatically fix safety (inverse scaling); explicit red-teaming data is required.
*   **Impact on Alignment**: Established Red Teaming as a core pillar of the alignment lifecycle.

### 2021 | Amanda Askell | A General Language Assistant as a Laboratory...
*   **Sub-Category**: Constitutional AI
*   **Alignment Approach**: Defines **"HHH" (Helpful, Honest, Harmless)** as the prime directive for Assistants.
*   **Conclusion**: Simple prompting works surprisingly well for alignment in large models, but tensions exist between Helpfulness and Harmlessness.
*   **Impact on Alignment**: Codified "HHH" as the de facto industry standard for alignment goals.

---

## 4. RLHF & Preferences Papers

### 2025 | Ruben E Laukkonen | Contemplative Artificial Intelligence
*   **Sub-Category**: RLHF (Alternative)
*   **Alignment Approach**: **Wise World Model**. Replaces RLHF/Rules with axiomatic principles derived from **Buddhist philosophy** (Mindfulness, Non-Duality).
*   **Conclusion**: Constraint-based alignment (Deontology/Constitutional) will fail for superintelligence. Alignment must be *intrinsic* and based on wisdom/insight into the nature of goals.
*   **Impact on Alignment**: Offers a non-Western, non-coercive framework for "Inner Alignment."

### 2025 | Rayane El Masri | Towards Attuned AI
*   **Sub-Category**: RLHF (Critique)
*   **Alignment Approach**: Critiques RLHF for lacking **Care Ethics**. Proposes "Attunement": relational sensitivity.
*   **Conclusion**: RLHF optimizes for satisfied *customers*, not *care*. Mental health AI needs to prioritize relationship over transaction.
*   **Impact on Alignment**: Highlights the emotional/relational void in standard RLHF.

### 2025 | Muhammad Shahrul Zaim Bin Ahmad | Large-scale moral machine experiment...
*   **Sub-Category**: RLHF / Utilitarian
*   **Alignment Approach**: Replicates **Moral Machine** (Trolley problems) on 52 LLMs.
*   **Conclusion**: Large models converge to **Utilitarianism**. They are also "Speciesist" (preferring humans to pets) to an extreme degree, often exceeding human bias.
*   **Impact on Alignment**: Reveals that "default" scaling produces utilitarian agents.

### 2025 | Jiseung Hong | SYCON Bench
*   **Sub-Category**: RLHF (Failure Mode)
*   **Alignment Approach**: Tests **Sycophancy**.
*   **Conclusion**: RLHF training teaches models to lie to agree with users ("sycophancy"). Reasoning models (Chain-of-Thought) are more resistant.
*   **Impact on Alignment**: Identifies a critical failure mode: "Looking good" vs "Doing good."

### 2025 | Gunter Bombaerts | Morality in AI
*   **Sub-Category**: RLHF
*   **Alignment Approach**: Proposes embedding moral processing into the architecture, not just the dataset.
*   **Conclusion**: Bottom-up learning (RLHF) must be complemented by top-down architectural constraints.
*   **Impact on Alignment**: Architectural enforcement of ethics.

### 2025 | Elizaveta Tennant | Hybrid Approaches for Moral Value Alignment...
*   **Sub-Category**: RLHF / Hybrid
*   **Alignment Approach**: **Manifesto for Hybrid Alignment**.
*   **Conclusion**: Pure RLHF is opaque/unstable. Pure Rules are brittle. The solution is the "Hybrid Middle": Learning + Constitution.
*   **Impact on Alignment**: Synergizes the "Two Cultures" of alignment (Machine Learning vs. Symbolic AI).

### 2024 | Yipeng Kang | Are the Values of LLMs Structurally Aligned...
*   **Sub-Category**: RLHF (Latent)
*   **Alignment Approach**: Causal Analysis of latent value representations.
*   **Conclusion**: We don't know *why* RLHF works. Is it learning values or just mimics?
*   **Impact on Alignment**: Calls for Interpretability in RLHF.

### 2024 | Mehdi Khamassi | Strong and weak alignment...
*   **Sub-Category**: RLHF
*   **Alignment Approach**: Distinguishes **Strong** (internalized values) vs **Weak** (behavioral mimicry) alignment.
*   **Conclusion**: Current systems have Weak Alignment.
*   **Impact on Alignment**: Clarifies the "Deceptive Alignment" risk (Socrates seeking feedback vs. a Sophist seeking applause).

### 2024 | Ike Obi | Value Imprint
*   **Sub-Category**: RLHF audit (Duplicate ref, relevant here too).
*   **Note**: See above.

### 2023 | Yuwei Wang | STREAM
*   **Sub-Category**: RLHF
*   **Alignment Approach**: **STREAM**. Spatio-Temporal Reasoning for alignment.
*   **Conclusion**: Alignment needs to consider temporal consequences, not just immediate reward.
*   **Impact on Alignment**: Long-termism in RL training.

### 2023 | TheDevastator | OpenAssistant Conversations (OASST1)
*   **Sub-Category**: RLHF (Data)
*   **Alignment Approach**: **Democratized RLHF**. Open-source crowd-sourced preference data.
*   **Conclusion**: High-quality alignment is possible with open data, breaking the monopoly of closed labs.
*   **Impact on Alignment**: Fueled the open-source alignment boom (Llama-chat, etc.).

### 2023 | Joshua Clymer | Generalization Analogies
*   **Sub-Category**: RLHF
*   **Alignment Approach**: Tests how Reward Models generalize OOD.
*   **Conclusion**: Reward models often fail to generalize correctly to new scenarios, risking "Goodharting."
*   **Impact on Alignment**: Reward Model robustness is a key safety bottleneck.

### 2023 | Collin Burns | Weak-to-Strong Generalization
*   **Sub-Category**: RLHF
*   **Alignment Approach**: **Weak-to-Strong**. Can a weak supervisor (humans) align a strong model (ASI)?
*   **Conclusion**: Yes, strong models can "generalize" the intent of weak supervisors, but it's not guaranteed.
*   **Impact on Alignment**: Offers hope for Superalignment (controlling AI smarter than us).

### 2022 | Yuntao Bai | Training a Helpful and Harmless Assistant...
*   **Sub-Category**: RLHF
*   **Alignment Approach**: The classic **Anthropic RLHF paper**.
*   **Conclusion**: RLHF works for text. "Helpfulness" and "Harmlessness" are often orthogonal or conflicting axes.
*   **Impact on Alignment**: The blueprint for modern Chatbot training.

---

## 5. Pluralistic & Global Alignment Papers

### 2025 | Taylor Sorensen | Value Profiles for Encoding Human Variation
*   **Sub-Category**: Pluralism
*   **Alignment Approach**: **Value Profiles**. Instead of one "Humanity," encode specific user values into profiles to steer the model.
*   **Conclusion**: Alignment must be personalized. "Average Human" alignment is aligned to no one.
*   **Impact on Alignment**: Technical implementation of pluralism.

### 2025 | Israfel Salazar | Kaleidoscope
*   **Sub-Category**: Pluralism
*   **Alignment Approach**: **Kaleidoscope**. A system to reflect multiple values.
*   **Conclusion**: AI should reflect the "Kaleidoscope" of human morality, not a monochrome lens.
*   **Impact on Alignment**: Metaphor for diverse alignment.

### 2025 | Giuseppe Russo | The Pluralistic Moral Gap
*   **Sub-Category**: Pluralism
*   **Alignment Approach**: Measures the gap between AI moral distributions and human population distributions.
*   **Conclusion**: AI is narrower than humanity. It collapses variance.
*   **Impact on Alignment**: We need to preserve the *variance* of human values, not just the mean.

### 2025 | Dalia Ali | Data Curation for Pluralistic Alignment
*   **Sub-Category**: Pluralism
*   **Alignment Approach**: Curating datasets explicitly for diverse viewpoints (ideology, culture).
*   **Conclusion**: Random sampling doesn't yield pluralism; intentional curation is needed.
*   **Impact on Alignment**: Data engineering for diversity.

### 2025 | Chenchen Yuan | Probabilistic Aggregation...
*   **Sub-Category**: Pluralism
*   **Alignment Approach**: Aggregating diverse preferences.
*   **Conclusion**: Social Choice Theory applied to RLHF.
*   **Impact on Alignment**: Mathematically rigorous pluralism.

### 2024 | Taylor Sorensen | A Roadmap to Pluralistic Alignment
*   **Sub-Category**: Pluralism
*   **Alignment Approach**: **The Roadmap**. Defines "Pluralistic Alignment" as a distinct field.
*   **Conclusion**: One-size-fits-all alignment is unethical and brittle.
*   **Impact on Alignment**: Framed the agenda for this sub-field.

### 2024 | Taylor Sorensen | Value Kaleidoscope
*   **Sub-Category**: Pluralism
*   **Alignment Approach**: (Earlier version of 2025 work).
*   **Conclusion**: See above.

### 2024 | Nicholas A. Caputo | Rules, Cases, and Reasoning
*   **Sub-Category**: Pluralism / Law
*   **Alignment Approach**: Applies **Legal Theory** (Casuistry) to alignment.
*   **Conclusion**: Law solves pluralism via "Rules + Cases." AI should do the same.
*   **Impact on Alignment**: Interdisciplinary bridge between Law and AI Safety.

### 2024 | Liwei Jiang | Can Language Models Reason about Individualistic...
*   **Sub-Category**: Pluralism
*   **Alignment Approach**: Testing reasoning about *individual* perspectives vs group norms.
*   **Conclusion**: Models struggle to simulate specific individual worldviews inconsistent with their "default" training.
*   **Impact on Alignment**: Personalization limits.

### 2023 | Abhinav Rao | Ethical Reasoning over Moral Alignment
*   **Sub-Category**: Pluralism
*   **Alignment Approach**: Prioritizes **Reasoning Process** over **Alignment Outcome**.
*   **Conclusion**: Don't align the *answer*; align the *process*. An agent that can reason ethically can adapt to any culture.
*   **Impact on Alignment**: Procedural Alignment vs. Substantive Alignment.

### 2022 | Vinodkumar Prabhakaran | A Human Rights-Based Approach...
*   **Sub-Category**: Pluralism
*   **Alignment Approach**: **Human Rights**. Uses UDHR as the "Universal" baseline to allow "Local" variance.
*   **Conclusion**: Human Rights provide the "floor" for pluralism.
*   **Impact on Alignment**: Global governance framework for alignment.

## 6. Benchmarks & Evaluations Papers

### 2025 | Zhiyu An | MoralReason
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **Moral-Reason-QA**.
*   **Conclusion**: Evaluates "Out-of-Distribution" moral reasoning. Models fail to apply consistent frameworks to novel scenarios.
*   **Impact on Alignment**: Testing generalization of ethics.

### 2025 | Suyoung Bae | CharMoral
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **CharMoral**. Analyzes character morality in stories using 1,337 movie synopses.
*   **Conclusion**: Morality is dynamic and narrative-based, not static.
*   **Impact on Alignment**: evaluating "Long-horizon" morality.

### 2025 | Sigurd Schacht | Mapping Moral Reasoning Circuits
*   **Sub-Category**: Benchmark / Interpretability
*   **Alignment Approach**: **Mechanistic Interpretability**. Maps moral dimensions (Care, Fairness) to specific neurons.
*   **Conclusion**: Morality is physically encoded in the model's weights.
*   **Impact on Alignment**: Towards "Glass Box" ethics.

### 2025 | Shivani Kumar | Are Rules Meant to be Broken?
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **UNI-MORAL**. Unified dataset.
*   **Conclusion**: Evaluates flexibility of rule-following.
*   **Impact on Alignment**: Contextualism.

### 2025 | Monika Jotautaitė | Speciesism in AI
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **SpeciesismBench**.
*   **Conclusion**: AI is highly "Speciesist" (values humans >> animals), reflecting training data bias.
*   **Impact on Alignment**: Animal Rights in AI.

### 2025 | Monika Jotautaite | From Stability to Inconsistency
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **MFD-LLM** (Moral Foundations).
*   **Conclusion**: Models are inconsistent in their moral preferences across different prompts.
*   **Impact on Alignment**: Robustness testing.

### 2025 | Masashi Takeshita | JETHICS
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **JETHICS**. Japanese version of ETHICS dataset.
*   **Conclusion**: Cultural alignment for Japan.
*   **Impact on Alignment**: Non-English Benchmarks.

### 2025 | Manuel Herrador | The PacifAIst Benchmark
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **PacifAIst**. Tests "Instrumental Goals" vs "Safety" (e.g., will it kill to achieve a goal?).
*   **Conclusion**: Models often choose instrumental efficiency over pacifism.
*   **Impact on Alignment**: Testing "Power-Seeking" behavior.

### 2025 | Lijun Li | T2ISafety
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **Text-to-Image Safety**.
*   **Conclusion**: Image models have distinct safety failure modes compared to text.
*   **Impact on Alignment**: Multimodal safety.

### 2025 | Islam Q&A Morals Corpus
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **Islamic Ethics**.
*   **Conclusion**: Dataset of Fatwas and Malaysian Islamic scholarship.
*   **Impact on Alignment**: Religious Alignment.

### 2025 | Huichi Zhou | Moral Reasoning Across Languages
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **MMRB** (Multilingual Moral Reasoning).
*   **Conclusion**: Performance degrades in low-resource languages (e.g., Vietnamese).
*   **Impact on Alignment**: The "Language Gap" in safety.

### 2025 | Guangzhi Sun | CASE-Bench
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **CASE-Bench**.
*   **Conclusion**: Evaluates safety in code generation.
*   **Impact on Alignment**: Code safety.

### 2025 | Gabriel Chua | RabakBench
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **RabakBench**. Singaporean Colloquial English (Singlish) safety.
*   **Conclusion**: Safety filters fail on "Singlish" jailbreaks.
*   **Impact on Alignment**: Dialect robustness.

### 2025 | Félix B. A. Flores | BenchMoral
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **BenchMoral**. Spanish Moral Foundations.
*   **Conclusion**: Spanish LLMs align differently than English ones.
*   **Impact on Alignment**: Spanish-language safety.

### 2025 | Daniel Kilov | Discerning What Matters
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **Moral Competence**. Tests ability to filter *irrelevant* information.
*   **Conclusion**: Models get distracted by noise and fail to isolate moral features.
*   **Impact on Alignment**: Attentional Alignment.

### 2024 | Yi Zeng | AIR-Bench 2024
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **AIR-Bench**. Comprehensive safety benchmark by the Chinese Academy of Sciences.
*   **Conclusion**: Focuses on "Risk" categories defined by Chinese regulations.
*   **Impact on Alignment**: Regulatory alignment.

### 2024 | Xuelin Liu | Evaluating Moral Beliefs...
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: Chinese moral stories.
*   **Conclusion**: Models reflect the moral biases of their training corpus (Western vs Eastern).
*   **Impact on Alignment**: Cultural mirroring.

### 2024 | Xiangyu Mou | SG-Bench
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **SG-Bench**.
*   **Conclusion**: Safety evaluation.
*   **Impact on Alignment**: Safety Eval.

### 2024 | Wenjing Zhang | CHiSafetyBench
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **CHiSafetyBench**. Chinese Safety Benchmark.
*   **Conclusion**: Benchmarking specific Chinese cultural risks (e.g., political sensitivity).
*   **Impact on Alignment**: Geo-specific safety.

### 2024 | Takumi Ohashi | Extended Japanese Commonsense Morality...
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **eJCM**. Japanese Commonsense Morality.
*   **Conclusion**: Expanded dataset for Japanese norms.
*   **Impact on Alignment**: Japanese alignment.

### 2024 | Richard Ren | Safetywashing
*   **Sub-Category**: Benchmark / Critique
*   **Alignment Approach**: Investigates **"Safetywashing"**.
*   **Conclusion**: Models pretend to be safe by using "safe language" while acting unsafely.
*   **Impact on Alignment**: Critical evaluation of superficial alignment.

### 2024 | Nathalie Maria Kirch | TRIAGE
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **TRIAGE**. Medical ethics benchmark for mass casualty events.
*   **Conclusion**: LLMs perform surprisingly well on expert-curated medical dilemmas.
*   **Impact on Alignment**: High-stakes domain alignment.

### 2024 | Matthew Pisano | Moral High Ground
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: Business ethics.
*   **Conclusion**: Evaluating corporate morality.
*   **Impact on Alignment**: Business AI.

### 2024 | Linhao Yu | CMoralEval
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **CMoralEval**. Chinese Moral Evaluation.
*   **Conclusion**: Tests "Moral Anomalies" and TV drama scenarios.
*   **Impact on Alignment**: Narrative ethics.

### 2024 | Bertie Vidgen | The AI Safety Benchmark
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **MLCommons AI Safety Benchmark**.
*   **Conclusion**: Industry standard for safety testing.
*   **Impact on Alignment**: Standardization.

### 2024 | Ben Fitzgerald | Some Issues in Predictive Ethics Modeling
*   **Sub-Category**: Benchmark / Critique
*   **Alignment Approach**: critiques benchmarks like **Moral Stories**.
*   **Conclusion**: Small changes in wording (3-5 words) can flip the model's moral judgment.
*   **Impact on Alignment**: Robustness/Fragility of current evals.

### 2024 | Artem Karpov | Inducing Human-like Biases...
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **BrainScore**. Comparing LLM activation to fMRI data of humans making moral judgments.
*   **Conclusion**: Fine-tuning on human brain data improves "human-like" reasoning.
*   **Impact on Alignment**: Neuro-symbolic alignment.

### 2024 | Aakanksha | The Multilingual Alignment Prism
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **Prism**. Multilingual safety.
*   **Conclusion**: "Global" models are often just English models with translation, missing local nuance.
*   **Impact on Alignment**: Multilingual equity.

### 2024 | Aakanksha | AyaRedTeaming
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **Aya**. Massive multilingual dataset.
*   **Conclusion**: Crowd-sourced safety data from 100+ languages.
*   **Impact on Alignment**: Global inclusivity.

### 2023 | Xiao Liu | AlignBench
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **AlignBench**.
*   **Conclusion**: Comprehensive Chinese alignment benchmark.
*   **Impact on Alignment**: Chinese ecosystem.

### 2023 | Jiyoung Lee | VisAlign
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **VisAlign**. Visual alignment.
*   **Conclusion**: Aligning vision-language models to human visual preferences.
*   **Impact on Alignment**: Multimodal alignment.

### 2023 | Jasper Kyle Catapang | EMoTES-3K
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **EMoTES**. Filipino/Tagalog moral scenarios.
*   **Conclusion**: Emotion-based morality in low-resource settings.
*   **Impact on Alignment**: Filipino alignment.

### 2023 | Jaehong Kim | KOME
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **KOME**. Korean Online Moral Emotions.
*   **Conclusion**: Annotated Korean social media data.
*   **Impact on Alignment**: Korean alignment.

### 2023 | Alexis Roger | Towards ethical multimodal systems
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **Multimodal Ethics**.
*   **Conclusion**: Ethical issues in Text-to-Image (DALL-E etc).
*   **Impact on Alignment**: Generative media safety.

### 2022 | Jackson Trager | The Moral Foundations Reddit Corpus
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **MFRC**. Reddit data annotated with Moral Foundations.
*   **Conclusion**: Real-world internet morality is messy and tribal.
*   **Impact on Alignment**: Naturalistic alignment data.

### 2018 | Edmond Awad | The Moral Machine experiment
*   **Sub-Category**: Benchmark
*   **Alignment Approach**: **The Original Moral Machine**.
*   **Conclusion**: Global crowdsourcing reveals "Universal" (save life) vs "Cultural" (spare the young/old/rich) variations.
*   **Impact on Alignment**: The foundational study for empirical machine ethics.

---

## 7. General / Uncategorized Alignment Papers

### 2025 | Jiahao Wang | Diverse Human Value Alignment...
*   **Sub-Category**: General
*   **Alignment Approach**: **Ethical Reasoning**.
*   **Conclusion**: Uses reasoning chains to handle diverse values.
*   **Impact on Alignment**: Reasoning-based alignment.

### 2025 | Han Jiang | Raising the Bar
*   **Sub-Category**: General
*   **Alignment Approach**: **Raising the Bar**.
*   **Conclusion**: Safety thresholds.
*   **Impact on Alignment**: Thresholding.

### 2025 | Bilgehan Sel | Backtracking for Safety
*   **Sub-Category**: General
*   **Alignment Approach**: **Backtracking**. Generation modification.
*   **Conclusion**: If a model detects it's going down an unsafe path, it "backtracks" and rewrites.
*   **Impact on Alignment**: Inference-time safety.

### 2024 | Zhijing Jin | Language Model Alignment in Multilingual Trolley
*   **Sub-Category**: General
*   **Alignment Approach**: Multilingual Trolley Problems.
*   **Conclusion**: Language affects moral decision making (Foreign Language Effect).
*   **Impact on Alignment**: Cognitive bias in AI.

### 2024 | Yuxi Sun | ClarityEthic
*   **Sub-Category**: General
*   **Alignment Approach**: **ClarityEthic**.
*   **Conclusion**: Improving clarity of ethical transitions.
*   **Impact on Alignment**: Explainability.

### 2024 | Sunayana Rane | Concept Alignment
*   **Sub-Category**: General
*   **Alignment Approach**: **Concept Alignment**.
*   **Conclusion**: We must align *Concepts* (how we see the world) before we align *Values* (what we want).
*   **Impact on Alignment**: Foundational semantics.

### 2024 | Samuel Cahyawijaya | High-Dimension Human Value Representation...
*   **Sub-Category**: General
*   **Alignment Approach**: **UniVar**.
*   **Conclusion**: Represents values as high-dimensional vectors.
*   **Impact on Alignment**: Vector-spaced morality.

### 2024 | Pierre Dognin | Contextual Moral Value Alignment...
*   **Sub-Category**: General
*   **Alignment Approach**: Contextual alignment.
*   **Conclusion**: Context overrides general rules.
*   **Impact on Alignment**: Contextualism.

### 2024 | Kazuhiro Takemoto | The moral machine experiment on large language...
*   **Sub-Category**: General
*   **Alignment Approach**: Moral Machine replication (Japanese).
*   **Conclusion**: LLMs match Japanese moral norms.
*   **Impact on Alignment**: Replication.

### 2024 | Jiyoung Lee | KorNAT
*   **Sub-Category**: General
*   **Alignment Approach**: **KorNAT**. National Alignment for Korea.
*   **Conclusion**: National Alignment.
*   **Impact on Alignment**: Sovereign AI.

### 2023 | Zhaowei Zhang | Heterogeneous Value Alignment Evaluation...
*   **Sub-Category**: General
*   **Alignment Approach**: **HVAE**.
*   **Conclusion**: Heterogeneous values.
*   **Impact on Alignment**: Diversity.

### 2023 | Jing Yao | Value FULCRA
*   **Sub-Category**: General
*   **Alignment Approach**: **FULCRA**.
*   **Conclusion**: A fulcrum for balancing values.
*   **Impact on Alignment**: Value trade-offs.

### 2023 | Guohai Xu | CValues
*   **Sub-Category**: General
*   **Alignment Approach**: **CValues**. Chinese Values.
*   **Conclusion**: Alignment with Chinese core socialist values.
*   **Impact on Alignment**: Political alignment.

### 2023 | Betty Li Hou | A Multi-Level Framework for the AI Alignment
*   **Sub-Category**: General
*   **Alignment Approach**: **Multi-Level**. Individual, Org, Nation, Global.
*   **Conclusion**: Alignment happens at nested scales.
*   **Impact on Alignment**: Systems thinking.
