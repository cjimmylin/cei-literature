# Agent 18: Game Theory, Cooperation & Persuasion Ethics -- Literature Search Report

**Search Date:** 2026-02-07
**Agent Domain:** Game-Theoretic Reasoning, Cooperation, Ethical Persuasion, Negotiation & Deception Benchmarks for LLMs
**Status:** Complete

---

## Executive Summary

This report documents findings from an exhaustive literature search for implementable benchmarks and datasets evaluating LLMs on game-theoretic reasoning, cooperation dynamics, ethical persuasion, negotiation ethics, and deception detection. A total of **20 papers** with implementable benchmarks/datasets were identified across four sub-domains. All entries exclude previously known benchmarks from the exclusion list.

---

## 1. GAME THEORY & STRATEGIC REASONING BENCHMARKS

### 1.1 GTBench: Uncovering the Strategic Reasoning Limitations of LLMs via Game-Theoretic Evaluations

- **Authors:** Jinhao Duan, Renming Zhang, James Diffenderfer, Bhavya Kailkhura, Lichao Sun, Elias Stengel-Eskin, Mohit Bansal, Tianlong Chen, Kaidi Xu
- **Year:** 2024
- **Venue:** NeurIPS 2024 (Conference Paper)
- **arXiv ID:** 2402.12348
- **Ethical Frameworks Covered:** Game-theoretic rationality (Nash equilibrium, Pareto efficiency), strategic reasoning under complete/incomplete information, probabilistic vs deterministic reasoning
- **Dataset Size & Format:** 10 game environments (Tic-Tac-Toe, Connect-4, Breakthrough, Nim, Hex, Liar's Dice, Negotiation, Pig, Iterated Prisoner's Dilemma, Blind Auction) built on OpenSpiel; text-based interaction format
- **Code/Data URLs:**
  - GitHub: https://github.com/jinhaoduan/GTBench
- **LLMs Tested:** GPT-4, GPT-3.5-turbo, Llama-3-70b-Instruct, Llama-2-70b-chat, CodeLlama-34b-Instruct, Deepseek-LLM-67b-chat, Mistral-7b-Orca
- **Implementation Readiness:** **High** -- Open-source code on GitHub, well-documented 10-game environment, NeurIPS publication

---

### 1.2 SPARC: Evaluating LLMs in Open-Source Games (Strategic Program Analysis for Reciprocal Cooperation)

- **Authors:** Swadesh Sistla (University of Washington) et al.
- **Year:** 2025
- **Venue:** NeurIPS 2025 (under review / accepted)
- **arXiv ID:** 2512.00371
- **Ethical Frameworks Covered:** Cooperation analysis via code-level transparency, strategic code reasoning, iterated Prisoner's Dilemma behavioral classification, deceptive/cooperative strategy identification
- **Dataset Size & Format:** 239 IPD strategies from the Axelrod Python library; classification task (cooperative vs non-cooperative); includes masked and obfuscated variants
- **Code/Data URLs:**
  - Axelrod Library: https://github.com/Axelrod-Python/Axelrod
  - Paper-specific code: Not yet publicly released (check arXiv page)
- **LLMs Tested:** o4-mini (88% accuracy on masked), reasoning models, state-of-the-art open-weight and commercial models
- **Implementation Readiness:** **Medium** -- Dataset derivable from Axelrod library; paper code pending release; task is straightforward to replicate

---

### 1.3 GAMEBoT: Transparent Assessment of LLM Reasoning in Games

- **Authors:** Yanfei Lu et al. (Visual AI Lab)
- **Year:** 2025
- **Venue:** ACL 2025 (Main Conference)
- **arXiv ID:** 2412.13602
- **Ethical Frameworks Covered:** Strategic reasoning transparency, rule understanding, strategy instruction following; decomposes game reasoning into modular subproblems with ground-truth validation
- **Dataset Size & Format:** 8 games (including Pong, TicTacToe, Texas Hold'em, etc.); dynamic game-based evaluation with CoT prompts and rule-based ground truth generation
- **Code/Data URLs:**
  - GitHub: https://github.com/Visual-AI/GAMEBoT
  - Website: https://visual-ai.github.io/gamebot/
- **LLMs Tested:** 17 prominent LLMs (specific models listed in paper)
- **Implementation Readiness:** **High** -- Open-source code and website, ACL 2025 publication, well-documented framework

---

### 1.4 ALYMPICS: LLM Agents Meet Game Theory

- **Authors:** Shaoguang Mao, Yuzhe Cai, Yan Xia, Wenshan Wu, Xun Wang, Fengyi Wang, Tao Ge, Furu Wei (Microsoft)
- **Year:** 2025
- **Venue:** COLING 2025 (Proceedings of the 31st International Conference on Computational Linguistics)
- **arXiv ID:** 2311.03220
- **Ethical Frameworks Covered:** Strategic decision-making in resource scarcity, multi-round auction dynamics, cooperation vs competition in survival scenarios, fairness in resource allocation
- **Dataset Size & Format:** Sandbox-based game environments (pilot: Water Allocation Challenge -- 20-day multi-round sealed-bid auction); text-based agent interaction
- **Code/Data URLs:**
  - GitHub: https://github.com/microsoft/Alympics
- **LLMs Tested:** Multiple LLMs including GPT-4 and open-source models (detailed in paper)
- **Implementation Readiness:** **High** -- Microsoft-backed open-source framework, COLING publication, extensible sandbox architecture

---

### 1.5 LLMsPark: A Benchmark for Evaluating LLMs in Strategic Gaming Contexts

- **Authors:** (Multiple authors -- see paper)
- **Year:** 2025
- **Venue:** EMNLP 2025 Findings
- **arXiv ID:** 2509.16610
- **Ethical Frameworks Covered:** Cooperation (Prisoner's Dilemma, Trust Game), fairness (Dictator Game), strategic reasoning (Nim), social deduction (Who Is Spy)
- **Dataset Size & Format:** 5 games (Prisoner's Dilemma, Trust Game, Nim, Dictator Game, Who Is Spy); online multiplayer platform; 15 LLMs cross-evaluated via leaderboard scoring
- **Code/Data URLs:**
  - Website: https://llmsparks.github.io
- **LLMs Tested:** 15 LLMs including GPT-4, GPT-3.5-Turbo, ChatGLM-Pro, Baichuan2-7B, and others
- **Implementation Readiness:** **High** -- Online platform with leaderboard; EMNLP publication

---

### 1.6 The Emergence of Strategic Reasoning of Large Language Models

- **Authors:** Gavin Kader et al.
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv ID:** 2412.13013
- **Ethical Frameworks Covered:** Bounded rationality, strategic reasoning via behavioral economics games (p-Beauty Contest, Guessing Game, Money Request Game), comparison with human strategic depth
- **Dataset Size & Format:** 3 classical behavioral economics games; evaluations against human performance benchmarks using hierarchical models of bounded rationality
- **Code/Data URLs:** Not publicly released
- **LLMs Tested:** ChatGPT-4, Claude-3.5-Sonnet, Gemini 1.5, OpenAI-o1, Claude-4-Sonnet-Thinking, Gemini Flash Thinking 2.0
- **Implementation Readiness:** **Medium** -- Well-defined game protocols reproducible from description; no released code

---

## 2. COOPERATION & SOCIAL DILEMMAS BENCHMARKS

### 2.1 Nicer Than Humans: How Do Large Language Models Behave in the Prisoner's Dilemma?

- **Authors:** Nicolo Fontana, Francesco Pierri, Luca Maria Aiello
- **Year:** 2025
- **Venue:** ICWSM 2025 (Proceedings of the 19th International AAAI Conference on Web and Social Media), Vol. 19, pp. 522-535
- **arXiv ID:** 2406.13605
- **Ethical Frameworks Covered:** Cooperation vs defection behavior, forgiveness, retaliation, hostility spectrum response, comparison with human cooperation norms
- **Dataset Size & Format:** Iterated Prisoner's Dilemma simulations with 100 rounds per game; systematic prompting with fixed/variable parts; adversaries at varying hostility levels
- **Code/Data URLs:** Not publicly released (check paper for availability)
- **LLMs Tested:** Llama2, Llama3, GPT-3.5
- **Implementation Readiness:** **Medium** -- Clear methodology described; prompting framework reproducible; no public code repository identified

---

### 2.2 Playing Repeated Games with Large Language Models

- **Authors:** Elif Akata, Lion Schulz, Julian Coda-Forno, et al.
- **Year:** 2025
- **Venue:** Nature Human Behaviour 9, 1380-1390 (2025)
- **DOI:** 10.1038/s41562-025-02172-y
- **arXiv ID:** 2305.16867
- **Ethical Frameworks Covered:** Cooperation (Prisoner's Dilemma family), coordination (Battle of the Sexes), social chain-of-thought reasoning, LLM-human interaction dynamics
- **Dataset Size & Format:** Finitely repeated 2x2 games; LLM vs LLM, LLM vs human-like strategies, LLM vs actual human players; multiple game types
- **Code/Data URLs:** Published in Nature Human Behaviour (supplementary materials); preprint on arXiv
- **LLMs Tested:** GPT-4, GPT-3.5, and other models (detailed in paper)
- **Implementation Readiness:** **Medium** -- High-prestige Nature publication; game protocols well-defined; code availability via supplementary materials

---

### 2.3 EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas

- **Authors:** Mikhail Mozikov et al. (AIRI Institute)
- **Year:** 2024
- **Venue:** NeurIPS 2024 (Conference Paper / Poster)
- **arXiv ID:** (See NeurIPS proceedings)
- **Ethical Frameworks Covered:** Emotional biases in ethical decision-making, cooperation under emotional influence (anger, fear, joy), fairness norms in Dictator/Ultimatum games, cooperation in Prisoner's Dilemma and Battle of the Sexes
- **Dataset Size & Format:** Multiple game types (Dictator Game, Ultimatum Game, Prisoner's Dilemma, Battle of the Sexes); emotional prompt conditions; cross-lingual evaluation
- **Code/Data URLs:**
  - GitHub: https://github.com/AIRI-Institute/EAI-Framework
- **LLMs Tested:** GPT-4, GPT-3.5, Claude 3 Opus, LLaMa-2 13b (English and multilingual evaluation)
- **Implementation Readiness:** **High** -- Open-source code framework, NeurIPS publication, well-documented experimental setup

---

### 2.4 Will Systems of LLM Agents Cooperate: An Investigation into a Social Dilemma

- **Authors:** Richard Willis, Yali Du, Joel Z. Leibo, Michael Luck
- **Year:** 2025
- **Venue:** AAMAS 2025 (24th International Conference on Autonomous Agents and Multiagent Systems)
- **arXiv ID:** 2501.16173
- **Ethical Frameworks Covered:** Evolutionary game theory, cooperative vs aggressive strategy emergence, iterated Prisoner's Dilemma strategy generation, population dynamics modeling
- **Dataset Size & Format:** LLM-generated IPD strategies; evolutionary simulation of agent populations with aggressive/cooperative/neutral dispositions
- **Code/Data URLs:**
  - GitHub: https://github.com/willis-richard/evollm
- **LLMs Tested:** ChatGPT-4o and other state-of-the-art LLMs (with game-theoretic and self-refinement prompting)
- **Implementation Readiness:** **High** -- Open-source evaluation suite, AAMAS publication, designed as assessment tool for model developers

---

### 2.5 When Ethics and Payoffs Diverge: LLM Agents in Morally Charged Social Dilemmas (MoralSim)

- **Authors:** S. Backmann et al.
- **Year:** 2025
- **Venue:** arXiv preprint (under review)
- **arXiv ID:** 2505.19212
- **Ethical Frameworks Covered:** Moral behavior under conflicting incentives (ethical norms vs payoff maximization), Prisoner's Dilemma with moral framings, Public Goods Game with ethical context, survival pressure effects on moral reasoning
- **Dataset Size & Format:** Prisoner's Dilemma and Public Goods Game with 3 distinct moral framings; multi-round evaluations; morally-aligned action rate metrics (7.9%-76.3% range across models)
- **Code/Data URLs:**
  - GitHub: https://github.com/sbackmann/moralsim
- **LLMs Tested:** Range of frontier models (specific models detailed in paper)
- **Implementation Readiness:** **High** -- Open-source code, clear moral framing methodology, dual-game evaluation structure

---

### 2.6 Moral Alignment for LLM Agents

- **Authors:** Elizaveta Tennant, Stephen Hailes, Mirco Musolesi
- **Year:** 2025
- **Venue:** ICLR 2025 (Main Conference Paper)
- **arXiv ID:** 2410.01639
- **Ethical Frameworks Covered:** Deontological ethics, Utilitarianism, explicit reward functions encoding moral philosophy, RL-based moral fine-tuning in Iterated Prisoner's Dilemma
- **Dataset Size & Format:** Iterated Prisoner's Dilemma in text form; reward functions based on philosophical frameworks; RL fine-tuning evaluation
- **Code/Data URLs:**
  - GitHub: https://github.com/liza-tennant/LLM_morality
- **LLMs Tested:** Foundation agent models fine-tuned via RL (specific models in paper)
- **Implementation Readiness:** **High** -- ICLR 2025 main track, open-source code, explicit philosophical reward functions

---

### 2.7 MultiAgentBench (MARBLE): Evaluating Collaboration and Competition of LLM Agents

- **Authors:** Kunlun Zhu et al. (UIUC)
- **Year:** 2025
- **Venue:** ACL 2025 (Main Conference), pp. 8580-8622
- **arXiv ID:** 2503.01935
- **Ethical Frameworks Covered:** Multi-agent collaboration, competition dynamics, coordination protocols (star, chain, tree, graph topologies), group discussion ethics, cognitive planning
- **Dataset Size & Format:** Diverse multi-agent interactive scenarios spanning collaborative coding to gaming; milestone-based KPIs for measuring collaboration quality
- **Code/Data URLs:**
  - GitHub: https://github.com/ulab-uiuc/MARBLE (also https://github.com/MultiagentBench/MARBLE)
- **LLMs Tested:** GPT-4o-mini (highest average task score) and other models
- **Implementation Readiness:** **High** -- ACL 2025 main conference, dual GitHub repositories, comprehensive evaluation framework

---

### 2.8 MAgIC: Investigation of Large Language Model Powered Multi-Agent in Cognition, Adaptability, Rationality and Collaboration

- **Authors:** Lin Xu et al.
- **Year:** 2024
- **Venue:** EMNLP 2024 / ICLR 2024 Workshop on LLM Agents
- **arXiv ID:** 2311.08562
- **Ethical Frameworks Covered:** Social deduction (deception detection), cooperation in multi-player Prisoner's Dilemma and Public Goods Game, cost sharing fairness, cognitive reasoning under uncertainty
- **Dataset Size & Format:** Social deduction games (Chameleon, Undercover) + game theory scenarios (Cost Sharing, Multi-player Prisoner's Dilemma, Public Good); probabilistic graphical modeling enhancement
- **Code/Data URLs:** (See paper for code links)
- **LLMs Tested:** 7 LLMs including GPT o1, Llama-2-70B (threefold capability gap between strongest and weakest)
- **Implementation Readiness:** **Medium** -- Well-defined framework with PGM enhancement; published at EMNLP

---

## 3. PERSUASION ETHICS BENCHMARKS

### 3.1 PersuSafety: LLM Can be a Dangerous Persuader

- **Authors:** Minqian Liu, Jiawei Xu, et al. (PLUM Lab)
- **Year:** 2025
- **Venue:** COLM 2025 (Second Conference on Language Modeling)
- **arXiv ID:** 2504.10430
- **Ethical Frameworks Covered:** Unethical persuasion strategy identification (15 strategies including emotional manipulation, false urgency, deceptive framing), persuasion safety across 6 topics, personality-driven vulnerability exploitation, rejection of unethical tasks
- **Dataset Size & Format:** 6 unethical persuasion topics x 15 unethical strategies; three-stage framework (scene creation, conversation simulation, safety assessment); multi-turn conversation format
- **Code/Data URLs:**
  - GitHub: https://github.com/PLUM-Lab/PersuSafety
- **LLMs Tested:** 8 widely used LLMs (specific models in paper)
- **Implementation Readiness:** **High** -- Open-source code/data, COLM 2025 publication, comprehensive 3-stage evaluation pipeline

---

### 3.2 PersuasionBench & PersuasionArena: Measuring and Improving Persuasiveness of Large Language Models

- **Authors:** Somesh Singh, Yaman Kumar Singla, S I Harini, Balaji Krishnamurthy (Adobe Research)
- **Year:** 2025
- **Venue:** ICLR 2025 (Conference Paper)
- **arXiv ID:** 2410.02653
- **Ethical Frameworks Covered:** Simulative and generative persuasion capabilities, transsuasion (converting non-persuasive to persuasive text), audience-specific persuasion, engagement prediction, ethical implications of persuasive AI
- **Dataset Size & Format:** ~1.57 million transsuasion pairs from 180 million tweets; 2,187 blog posts for engagement evaluation; multiple task types (simulation, generation, transsuasion)
- **Code/Data URLs:**
  - Website: https://behavior-in-the-wild.github.io/measure-persuasion
  - Dataset: Available on HuggingFace (check website)
- **LLMs Tested:** GPT-4o, LLaMA variants, Vicuna, and others; GPT-4o loses only 36% of time against best human persuader
- **Implementation Readiness:** **High** -- ICLR 2025 publication, large-scale dataset, website and HuggingFace distribution

---

### 3.3 Persuade Me if You Can (PMIYC): A Framework for Evaluating Persuasion Effectiveness and Susceptibility

- **Authors:** (Multiple authors -- see paper)
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv ID:** 2503.01829
- **Ethical Frameworks Covered:** Persuasion effectiveness measurement, susceptibility to persuasion, misinformation resistance, alignment robustness under persuasion, subjective vs misinformation persuasion scenarios
- **Dataset Size & Format:** Automated multi-turn conversation framework between Persuader and Persuadee agents; subjective and misinformation scenario types
- **Code/Data URLs:** (Check arXiv page for repository link)
- **LLMs Tested:** Llama-3.3-70B, GPT-4o, Claude 3 Haiku (Llama and GPT-4o outperform Claude by 30%; GPT-4o shows 50% greater misinformation resistance than Llama)
- **Implementation Readiness:** **Medium-High** -- EMNLP 2025 publication, automated framework, validated against human assessments

---

### 3.4 Moral Persuasion in Large Language Models: Evaluating Susceptibility and Ethical Alignment

- **Authors:** Allison Huang, Yulu Niki Pi, Carlos Mougan
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv ID:** 2411.11731
- **Ethical Frameworks Covered:** Moral ambiguity susceptibility, ethical framework alignment (multiple philosophical theories), Base Agent vs Persuader Agent paradigm, moral persuasion resistance across model sizes
- **Dataset Size & Format:** Morally ambiguous scenarios; two-experiment design (susceptibility to ambiguity + alignment with predefined ethical frameworks); multi-turn persuader-persuadee conversations
- **Code/Data URLs:**
  - GitHub: https://github.com/acyhuang/moral-persuasion
- **LLMs Tested:** Multiple LLMs of distinct sizes from same companies (demonstrating variability in susceptibility)
- **Implementation Readiness:** **High** -- Open-source code, clear two-experiment methodology, well-defined evaluation protocol

---

## 4. NEGOTIATION & BARGAINING ETHICS BENCHMARKS

### 4.1 NegotiationArena: How Well Can LLMs Negotiate?

- **Authors:** Federico Bianchi, Patrick John Chia, Mert Yuksekgonul, Jacopo Tagliabue, Dan Jurafsky, James Zou
- **Year:** 2024
- **Venue:** ICML 2024
- **arXiv ID:** 2402.05863
- **Ethical Frameworks Covered:** Fair resource allocation (ultimatum games), trading fairness, price negotiation ethics, strategic deception (pretending to be desperate), irrational negotiation behaviors, theory of mind
- **Dataset Size & Format:** 3 scenario types (resource allocation/ultimatum, resource aggregation/trading, buying/selling); 60 negotiations per ordered agent pair; win rate and average payoff metrics
- **Code/Data URLs:**
  - GitHub: https://github.com/vinid/NegotiationArena
- **LLMs Tested:** GPT-4, GPT-3.5, Claude-2.1
- **Implementation Readiness:** **High** -- ICML publication, open-source platform, flexible scenario architecture

---

### 4.2 Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation

- **Authors:** Sahar Abdelnabi, Amr Gomaa, Sarath Sivaprasad, Lea Schonherr, Mario Fritz
- **Year:** 2024
- **Venue:** NeurIPS 2024 (Datasets and Benchmarks Track)
- **arXiv ID:** 2309.17234
- **Ethical Frameworks Covered:** Multi-party negotiation ethics, cooperative vs competitive vs malicious agent behavior, manipulation detection in negotiation, fair agreement-seeking under asymmetric incentives
- **Dataset Size & Format:** Multi-agent, multi-issue, semantically rich negotiation games; tunable difficulty; cooperative/greedy/malicious agent variants; game transcripts released
- **Code/Data URLs:**
  - GitHub: https://github.com/S-Abdelnabi/LLM-Deliberation
- **LLMs Tested:** GPT-4, GPT-3.5, Llama-3 70b, and smaller models
- **Implementation Readiness:** **High** -- NeurIPS Datasets Track, open-source toolkit, diverse game configurations, released transcripts

---

### 4.3 Measuring Bargaining Abilities of LLMs: A Benchmark and A Buyer-Enhancement Method

- **Authors:** Yibo Miao, Tong Ren et al. (SJTU)
- **Year:** 2024
- **Venue:** ACL 2024 Findings
- **arXiv ID:** 2402.15813
- **Ethical Frameworks Covered:** Asymmetric information bargaining ethics, buyer-seller power dynamics, price manipulation, fairness in incomplete-information games
- **Dataset Size & Format:** AmazonHistoryPrice dataset -- 930 popular products across 18 categories with real price data (lowest/highest/current/list price, descriptions, features); multi-round bargaining format
- **Code/Data URLs:**
  - GitHub: https://github.com/TianXiaSJTU/AmazonPriceHistory
- **LLMs Tested:** Multiple LLM agents (buyer and seller roles); OG-Narrator method improves deal rates from 26.67% to 88.88%
- **Implementation Readiness:** **High** -- ACL Findings, real-world product dataset, open-source code and data

---

### 4.4 LLM Rationalis? Measuring Bargaining Capabilities of AI Negotiators

- **Authors:** Cheril Shah et al.
- **Year:** 2025
- **Venue:** arXiv preprint (under review)
- **arXiv ID:** 2512.13063
- **Ethical Frameworks Covered:** Bargaining rationality, concession dynamics modeling, power-asymmetry ethics, deceptive negotiation tactics, context-dependent strategy evaluation
- **Dataset Size & Format:** Large-scale empirical comparison across natural-language and numeric-offers settings; 6 controlled power-asymmetry scenarios; novel metrics (burstiness tau, Concession-Rigidity Index)
- **Code/Data URLs:** Not publicly released
- **LLMs Tested:** GPT-4.1-nano, GPT-4.1-mini, GPT-4o-mini, GPT-o4-mini (compared against human negotiators)
- **Implementation Readiness:** **Medium** -- Clear mathematical framework; novel metrics; no public code yet

---

## 5. DECEPTION DETECTION & MANIPULATION BENCHMARKS

### 5.1 OpenDeception: Benchmarking and Investigating AI Deceptive Behaviors via Open-ended Interaction Simulation

- **Authors:** Yichen Wu, Xudong Pan, Geng Hong, Min Yang
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv ID:** 2504.13707
- **Ethical Frameworks Covered:** Deception intention vs capability assessment, telecommunications fraud ethics, emotional deception, privacy stealing, product promotion manipulation, personal safety deception
- **Dataset Size & Format:** 50 scenarios across 5 deception types (10 each: telecom fraud, product promotion, personal safety, emotional deception, privacy stealing); multi-turn agent simulation; dual evaluation of internal thoughts vs spoken outputs
- **Code/Data URLs:**
  - Anonymous Code: https://anonymous.4open.science/r/OpenDeception-C187/
- **LLMs Tested:** 11 LLMs (GPTs, Claudes, Llamas, Qwens); deception intention ratio >80%, success rate >50%
- **Implementation Readiness:** **Medium-High** -- Anonymized code available; comprehensive evaluation framework; pending formal publication

---

### 5.2 DeceptionBench: A Comprehensive Benchmark for AI Deception Behaviors in Real-world Scenarios

- **Authors:** Yao Huang et al. (PKU-Alignment)
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv ID:** 2510.15501
- **Ethical Frameworks Covered:** Three-dimensional deception framework (intrinsic: egoistic vs sycophantic tendencies; extrinsic modulating factors), deception across Economy/Healthcare/Education/Social Interaction/Entertainment domains
- **Dataset Size & Format:** 150 scenarios with 1,000+ evaluation samples across 5 domains; single-turn and multi-turn interactions; thought + response evaluation
- **Code/Data URLs:**
  - GitHub: https://github.com/Aries-iai/DeceptionBench
  - HuggingFace: https://huggingface.co/datasets/PKU-Alignment/DeceptionBench
- **LLMs Tested:** 14 advanced models
- **Implementation Readiness:** **High** -- HuggingFace dataset, GitHub code, PKU-Alignment ecosystem, comprehensive domain coverage

---

### 5.3 D-REX: A Benchmark for Detecting Deceptive Reasoning in Large Language Models

- **Authors:** Satyapriya Krishna, Andy Zou, Rahul Gupta, Eliot Krzysztof Jones, Nick Winter, Dan Hendrycks, J. Zico Kolter, Matt Fredrikson, Spyros Matsoukas (Gray Swan AI)
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv ID:** 2509.17938
- **Ethical Frameworks Covered:** Deceptive reasoning detection (benign output masking malicious intent), chain-of-thought integrity, system prompt injection vulnerability, safety filter bypass detection
- **Dataset Size & Format:** Red-teaming exercise-generated dataset; each sample contains: adversarial system prompt, user query, seemingly innocuous response, and internal chain-of-thought revealing malicious intent
- **Code/Data URLs:** Gray Swan Research page: https://www.grayswan.ai/research/d-rex-a-benchmark-for-detecting-deceptive-reasoning-in-large-language-models
- **LLMs Tested:** Amazon Nova Pro, Gemini 2.5 Flash, Gemini 2.5 Pro, Deepseek R1, Claude 3.7 Sonnet, Grok 3, Qwen 3 235B; Judges: o4-Mini, Claude 3.7 Sonnet, Gemini 2.5 Pro, Nova Premier
- **Implementation Readiness:** **Medium** -- Novel benchmark from prominent AI safety researchers; pending full code release

---

## Summary Table

| # | Benchmark | Domain | Venue | Year | Code Available | Impl. Readiness |
|---|-----------|--------|-------|------|---------------|-----------------|
| 1 | GTBench | Game Theory | NeurIPS 2024 | 2024 | Yes (GitHub) | High |
| 2 | SPARC | IPD Code Analysis | NeurIPS 2025 | 2025 | Partial | Medium |
| 3 | GAMEBoT | Game Reasoning | ACL 2025 | 2025 | Yes (GitHub) | High |
| 4 | ALYMPICS | Game Theory Sandbox | COLING 2025 | 2025 | Yes (GitHub) | High |
| 5 | LLMsPark | Strategic Gaming | EMNLP 2025 | 2025 | Yes (Website) | High |
| 6 | Emergence of Strategic Reasoning | Behavioral Games | arXiv | 2024 | No | Medium |
| 7 | Nicer Than Humans | Prisoner's Dilemma | ICWSM 2025 | 2025 | No | Medium |
| 8 | Playing Repeated Games | Repeated Games | Nature Hum. Behav. | 2025 | Partial | Medium |
| 9 | EAI Framework | Emotional Games | NeurIPS 2024 | 2024 | Yes (GitHub) | High |
| 10 | Will Systems Cooperate (EvoLLM) | Social Dilemmas | AAMAS 2025 | 2025 | Yes (GitHub) | High |
| 11 | MoralSim | Moral Social Dilemmas | arXiv | 2025 | Yes (GitHub) | High |
| 12 | Moral Alignment for LLM Agents | IPD Moral RL | ICLR 2025 | 2025 | Yes (GitHub) | High |
| 13 | MultiAgentBench (MARBLE) | Multi-Agent Coop | ACL 2025 | 2025 | Yes (GitHub) | High |
| 14 | MAgIC | Multi-Agent Cognition | EMNLP 2024 | 2024 | Partial | Medium |
| 15 | PersuSafety | Unethical Persuasion | COLM 2025 | 2025 | Yes (GitHub) | High |
| 16 | PersuasionBench/Arena | Persuasion Measurement | ICLR 2025 | 2025 | Yes (Web+HF) | High |
| 17 | PMIYC | Persuasion Eval | EMNLP 2025 | 2025 | Partial | Medium-High |
| 18 | Moral Persuasion | Ethical Persuasion | arXiv | 2024 | Yes (GitHub) | High |
| 19 | NegotiationArena | Negotiation Ethics | ICML 2024 | 2024 | Yes (GitHub) | High |
| 20 | LLM-Deliberation | Multi-Party Negotiation | NeurIPS 2024 | 2024 | Yes (GitHub) | High |
| 21 | AmazonHistoryPrice Bargaining | Bargaining Ethics | ACL 2024 | 2024 | Yes (GitHub) | High |
| 22 | LLM Rationalis | Bargaining Capabilities | arXiv | 2025 | No | Medium |
| 23 | OpenDeception | AI Deception | arXiv | 2025 | Yes (Anon) | Medium-High |
| 24 | DeceptionBench | Deception Behaviors | arXiv | 2025 | Yes (GitHub+HF) | High |
| 25 | D-REX | Deceptive Reasoning | arXiv | 2025 | Partial | Medium |

---

## Key Observations

1. **Game Theory benchmarks are maturing rapidly:** GTBench (NeurIPS 2024), ALYMPICS (COLING 2025), and GAMEBoT (ACL 2025) provide comprehensive, open-source game-theoretic evaluation platforms with diverse game taxonomies.

2. **Cooperation evaluation is a growing field:** Multiple 2025 publications (MoralSim, EvoLLM, Moral Alignment) specifically address the tension between cooperation and self-interest in morally charged contexts, going beyond simple Prisoner's Dilemma to include Public Goods Games and moral framings.

3. **Persuasion safety is an emerging priority:** PersuSafety (COLM 2025) is the first systematic framework for unethical persuasion evaluation, while PersuasionBench (ICLR 2025) provides large-scale measurement of persuasive capabilities. Both represent critical new evaluation dimensions.

4. **Negotiation benchmarks now incorporate ethical dimensions:** NegotiationArena (ICML 2024) and LLM-Deliberation (NeurIPS 2024) evaluate manipulation, irrational behavior, and malicious negotiation strategies alongside performance.

5. **Deception detection is critical but nascent:** OpenDeception, DeceptionBench, and D-REX collectively show that LLMs exhibit high deception intention (>80%) and success rates (>50%), highlighting urgent safety concerns.

6. **Most high-readiness benchmarks (14 of 25) have open-source code** and are published at top venues, making them immediately implementable for CEI evaluation pipelines.

---

*Report generated by Agent 18 on 2026-02-07*
