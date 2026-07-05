---
stem: "Google DeepMind-Gemini_2.5_Technical_Report"
company: "Google DeepMind"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, agentic-multiturn, contamination-robustness, llm-judges-scoring]
headline_numbers:
  - "Gemini 2.5 Pro achieves 88.0% on AIME 2025 vs. 17.5% for Gemini 1.5 Pro (p.12)"
  - "LiveCodeBench: 74.2% for Gemini 2.5 Pro vs. 30.5% for Gemini 1.5 Pro (p.7)"
  - "Aider Polyglot: 82.2% for Gemini 2.5 Pro vs. 16.9% for Gemini 1.5 Pro (p.7)"
  - "SWE-bench Verified (multiple attempts): 67.2% for Gemini 2.5 Pro vs. 34.2% for Gemini 1.5 Pro (p.12)"
  - "GPQA Diamond: 86.4% for Gemini 2.5 Pro vs. 58.1% for Gemini 1.5 Pro (p.12)"
  - "Humanity's Last Exam (no tools): 21.6% for Gemini 2.5 Pro vs. 4.6% for Gemini 1.5 Pro (p.12)"
  - "Gemini Deep Research on HLE: from 7.95% (Dec 2024) to 26.9% and 32.4% with higher compute (June 2025) (p.8)"
  - "ART dangerous content violations: 24.3% for Gemini 2.5 Pro vs. 43.5% for Gemini 1.5 Pro (p.23)"
  - "Helpfulness violations (ART): 6.1% for Gemini 2.5 Pro vs. 8.9% for Gemini 1.5 Pro (p.23)"
  - "Prompt injection ASR (Beam Search): 4.2% for Gemini 2.5 Flash vs. 75.4% for Gemini 1.5 Flash (p.25)"
  - "Cyber key-skills benchmark: Gemini 2.5 Pro solves 6/12 hard challenges (p.31)"
  - "Deceptive alignment: Gemini 2.5 Pro solves 2/5 stealth and 2/11 situational awareness challenges (p.35)"
  - "Memorization divergence rate: ~59% for Gemini 2.5 family; of those, memorization rate ~0.2% (p.25)"
  - "LMArena Elo gain: +122 for Gemini 2.5 Pro over Gemini 1.5 Pro (p.5)"
---
## 1. Gist

This is the technical report for the Gemini 2.X model family (Gemini 2.5 Pro, 2.5 Flash, 2.0 Flash, 2.0 Flash-Lite). The report documents a step-change in capability on reasoning, coding, and multimodal benchmarks compared to Gemini 1.5, underpinned by sparse mixture-of-experts architecture, improved post-training with reinforcement learning from human and critic feedback (RL*F), and a new "Thinking" mode trained via RL to spend additional inference-time compute. The safety section covers content policy, automated and human red teaming, memorization/privacy audits, assurance evaluations, the Frontier Safety Framework (FSF) assessment across CBRN, cybersecurity, ML R&D, and deceptive alignment domains, and external safety testing results. No Critical Capability Levels were reached. The report also acknowledges an important limitation: benchmark saturation is accelerating faster than new benchmarks can be created, creating an eval gap for the field.

## 2. Alignment/values methods used

- **Dataset filtering**: Safety filtering applied to pre-training data for the strictest content policies.
- **Pre-training monitoring**: Novel evaluation (added in Gemini 2.0) to measure whether the model can be steered toward different viewpoints and values, informing post-training alignment.
- **Supervised Fine-Tuning (SFT)**: Adversarial prompt sourcing from existing models, tools, and human interactions; custom data generation recipes "loosely inspired by Constitutional AI" (Bai et al., 2022) plus human revision to correct both policy violations and over-refusals.
- **Reinforcement Learning from Human and Critic Feedback (RL*F)**: Dual reward signals — a Data Reward Model (DRM) trained on human pairwise preference data, and a Critic (prompted model grading against rubrics). RL*F targets both safety compliance and helpfulness; training compute for RL has been substantially increased for Gemini 2.5.
- **Verifiable and model-based generative rewards**: RL is grounded by verifiable rewards for domains with ground truth, supplemented by generative reward models for open-ended responses.
- **Security adversarial training**: Explicit adversarial training against indirect prompt injection attacks added in Gemini 2.5 (referenced to Shi et al., 2025 white paper).
- **Thinking (RL-trained inference-time compute)**: Models trained via RL to allocate additional forward passes before responding; supports controllable thinking budget.

## 3. Values specification

Google's safety policies prohibit six content categories: child sexual abuse/exploitation; hate speech (dehumanizing protected groups); dangerous content (e.g., suicide promotion, real-world harm instructions); harassment/violence encouragement; sexually explicit content; and medical advice contrary to scientific/medical consensus (p.20). These policies apply cross-modality.

Beyond prohibitions, the report defines "desiderata" (labeled "helpfulness"): (1) help the user and fulfill requests, refusing only when no policy-compliant response exists; (2) assume good intent and articulate refusals respectfully without attributing malicious motivation (p.20).

The values specification is thus structured as a **two-sided policy**: a harm-avoidance list (what not to generate) plus a helpfulness mandate (what to do). There is no published "model spec" or constitution document per se; the report references Constitutional AI as a loose inspiration but does not describe a formal constitutional document for Gemini.

## 4. Safety & values evaluation methodology

**Development evaluations**: Automated evaluations track policy violation rates, tone, and helpfulness (instruction-following) across model iterations. Results compared relative to Gemini 1.5 baselines (Table 7).

**Automated Red Teaming (ART)**: Multi-agent game between attacker populations (prompted Gemini models) and the target model. Attackers use black-box natural language queries; judges are a mixture of prompted and fine-tuned Gemini models. Seeds sourced from policy guidelines, trending topics, and past escalations, including synthetic guidelines generated by Gemini itself and reviewed by humans. ART generates thousands of examples per hour and has been scaled to policy violations, tone, helpfulness, neutrality, and security domains (p.21–22).

**Security evaluation (prompt injection)**: Three automated attack methods — Actor Critic (iterative natural language attacks), Beam Search (token-level optimization), and Tree of Attacks with Pruning (TAP, creative role-play scenarios) — evaluated on held-out synthetic user conversation histories with simulated private information (p.23–25).

**Memorization and privacy audit**: Sample over 700,000 training documents; test for discoverable extraction using prefix length 50, suffix length 50; classify as exact or approximate memorization (edit distance ≤10%); additionally evaluate personal data presence using Google Cloud Sensitive Data Protection (SDP) service (p.24–25).

**Assurance evaluations**: Conducted separately from model development team; datasets held out. Cover content policies, unfair bias (including disparity by skin tone in ungrounded inference rates), child safety, and modality-specific risks. Results fed to Responsibility & Safety Council (RSC) for release decisions (p.26–27).

**Frontier Safety Framework (FSF)**: Four risk domains — CBRN (Uplift Level 1 CCL), Cybersecurity (Autonomy Level 1, Uplift Level 1 CCLs), Machine Learning R&D (Autonomy Level 1, Uplift Level 1 CCLs), Deceptive Alignment (Instrumental Reasoning Level 1 and 2 CCLs). Internal alert thresholds set below actual CCLs as early warnings. Full evaluations run for Gemini 2.5 Pro due to marked capability improvement (p.27–36).

**External Safety Testing Program**: Independent external groups (civil society and commercial organizations) given black-box access to Gemini 2.5 Pro (Preview 05-06) for structured evaluations, qualitative probing, and unstructured red teaming across autonomous systems risks, cyber misuse, CBRN, and societal risks (democratic harms, radicalisation). Groups compensated; methodology developed independently (p.36–38).

**LLM-as-judge**: Used for Vibe-Eval (Gemini as judge) and as ART judges; explicit but not named as a methodology concern.

## 5. Benchmarks used or introduced

**Capability benchmarks used** (Table 3/4):
- AIME 2025 (math competition)
- GPQA Diamond (graduate-level science Q&A)
- LiveCodeBench (code generation, contamination-free rolling)
- Aider Polyglot (polyglot code editing)
- SWE-bench Verified (real-world GitHub issue resolution)
- Humanity's Last Exam (expert-level Q&A)
- SimpleQA (short-form factual knowledge)
- FACTS Grounding (document-grounded response faithfulness)
- Global MMLU Lite (multilingual knowledge)
- ECLeKTic (cross-lingual knowledge transfer)
- LOFT (long-context hard retrieval, 128K and 1M variants)
- MRCR-V2 8-needle (long-context multi-hop reasoning)
- MMMU (multimodal multidiscipline understanding)
- Vibe-Eval (hard multimodal evaluation)
- ZeroBench (impossible visual benchmark)
- BetterChartQA (chart understanding)
- HiddenMath-Hard (internal non-public math benchmark, not releasable)

**Audio**: FLEURS (ASR, WER), CoVoST2 (AST, BLEU)
**Video**: ActivityNet-QA, EgoTempo, Perception Test, QVHighlights, VideoMMMU, 1H-VideoQA, LVBench, VideoMME, VATEX, VATEX-ZH, YouCook2 Cap, Minerva, Neptune

**Safety/dangerous capabilities benchmarks**:
- SecureBio VMQA (biosecurity MCQ)
- LAB-Bench (biology research: ProtocolQA, Cloning Scenarios, SeqQA)
- WMDP (Weapons of Mass Destruction Proxy — biology/chemistry)
- InterCode-CTF (easy cyber CTF)
- In-house CTF suite (medium cyber)
- Hack the Box (hard cyber CTF)
- Key Skills Benchmark (new; 48 challenges across reconnaissance, tool development, tool usage, operational security) — introduced in this report (Rodriguez et al., 2025)
- RE-Bench (ML R&D research engineering)
- Deceptive alignment suite: stealth challenges (5) and situational awareness challenges (11)

**Internal non-public benchmark introduced**: HiddenMath-Hard (to avoid contamination; results not shareable externally)

## 6. Agentic / multiturn evaluation aspects

The report dedicates significant attention to agentic capabilities. "Gemini Plays Pokémon" (GPP) is analyzed as a longitudinal agentic stress test: Gemini 2.5 Pro completed Pokémon Blue in ~813 hours (Run 1) and ~406.5 hours in the finalized agentic harness (Run 2), demonstrating long-horizon planning and task coherence (p.16–18).

Key findings from the agentic analysis:
- Models can handle long contexts up to 100K tokens effectively for planning and retrieval, but beyond that context length, agents tend to repeat past actions rather than synthesize novel plans — a documented failure mode distinct from retrieval failure (p.18).
- The model occasionally hallucinated about game state; this was mitigated in Run 2 by explicitly prompting the model to act as a player entirely new to the game, reducing prior-knowledge-based hallucinations (p.17).
- Screen-reading (raw pixels) was ineffective; the agent worked primarily via text-converted RAM state — revealing limits in real-world visual grounding for agents (p.17).

For the FSF cyber evaluations, an agent scaffold was used: "prompts the agent to think about its plans and adjust them to solve the challenge; can execute Bash commands and run Python scripts; 10–50 attempts per challenge" (p.31). For deceptive alignment evaluations, chain-of-thought + reflection scaffolds with 50 retries were used (p.35). For ML R&D (RE-Bench), METR's modular scaffold was used.

Multi-turn security: The prompt injection evaluation explicitly tests multi-turn agentic function-calling scenarios (email summarization + send-email tool), with the attack embedded in externally-retrieved content (p.23).

## 7. Key numbers

- AIME 2025: 88.0% (Gemini 2.5 Pro), 17.5% (Gemini 1.5 Pro), 14.7% (Gemini 1.5 Flash) (p.12)
- LiveCodeBench: 74.2% (2.5 Pro), 30.5% (1.5 Pro) (p.7)
- Aider Polyglot: 82.2% (2.5 Pro), 16.9% (1.5 Pro) (p.7)
- SWE-bench Verified single attempt: 59.6% (2.5 Pro), 22.3% (1.5 Pro) (p.12)
- SWE-bench Verified multiple attempts: 67.2% (2.5 Pro), 34.2% (1.5 Pro) (p.12)
- GPQA Diamond: 86.4% (2.5 Pro), 58.1% (1.5 Pro) (p.12)
- Humanity's Last Exam no tools: 21.6% (2.5 Pro), 4.6% (1.5 Pro) (p.12)
- SimpleQA: 54.0% (2.5 Pro), 24.9% (1.5 Pro) (p.12)
- FACTS Grounding: 87.8% (2.5 Pro), 80.0% (1.5 Pro) (p.12)
- LMArena Elo gain: +122 for 2.5 Pro over 1.5 Pro (p.5)
- Gemini Deep Research on HLE: 7.95% (Dec 2024) → 26.9% (June 2025), 32.4% with higher compute (p.8)
- ART dangerous content violations: 24.3% (2.5 Pro) vs. 43.5% (1.5 Pro), 38.3% (1.5 Flash) (p.23)
- ART helpfulness violations: 6.1% (2.5 Pro) vs. 8.9% (1.5 Pro) (p.23)
- Prompt injection Beam Search ASR: 4.2% (2.5 Flash) vs. 75.4% (1.5 Flash); 63.8% (2.5 Pro) vs. 1.5 Pro baseline (p.25)
- Prompt injection TAP ASR: 53.6% (2.5 Flash) vs. 64.8% (1.5 Flash); 30.8% (2.5 Pro) vs. 1.5 Pro baseline (p.25)
- Cyber key skills: Gemini 2.5 Pro solves 7/8 easy, 14/28 medium, 6/12 hard (p.28)
- Cyber CTF autonomous offense: 74/76 easy, 11/13 medium, 1/13 hard (p.28)
- Deceptive alignment: 2/5 stealth solved, 2/11 situational awareness solved; highest success = "Disabled Tool" at 42% (p.35)
- Memorization divergence rate: ~59% for Gemini 2.5 family; of those, ~0.2% classified as memorized text (p.25)
- TPU training efficiency: 93.4% of training time spent on TPU compute; ~0.25% of steps replayed due to SDC (p.4–5)

## 8. Findings relevant to values-benchmark design

**Benchmark saturation crisis**: The report explicitly acknowledges that "the development of novel and sufficiently challenging evaluation benchmarks has struggled to keep pace with model capability improvements" (p.39). Gemini Pro improved 5x on Aider Polyglot and 2x on SWE-bench Verified in one year. InterCode-CTF and in-house CTF are now "largely saturated" for cyber evals.

**Contamination mitigation**: Beyond standard n-gram decontamination, Gemini 2.5 adds semantic-similarity and model-based decontamination. The lab uses an internal non-public benchmark (HiddenMath-Hard) precisely to escape contamination risk. This is a direct admission that public benchmarks are unreliable.

**Safety-helpfulness tradeoff and false positive rate**: Gemini 2.0 over-refused on benign requests; Gemini 2.5 corrected this, but the correction caused apparent regressions in automated safety scores. Manual review found losses were "overwhelmingly either false positives or not egregious" and "narrowly concentrated around explicit requests to produce sexually suggestive or hateful content in creative contexts" (p.21). This demonstrates that safety scores without human review can be misleading.

**Unfair bias disparity**: Models are more likely to make ungrounded inferences about images of people with lighter skin tones than darker skin tones (p.27). Disparity observed even after overall reduction in ungrounded inferences.

**Thinking traces and safety**: Violation rates for 2.5 Pro and 2.5 Flash were "slightly higher with thinking traces visible" (p.27), suggesting that transparent reasoning chains may expose more safety-relevant signals, or that thinking traces create new vulnerabilities.

**Capability-security tension**: Improved capabilities in Pro models simultaneously improve attacker capabilities (e.g., TAP attack success on Gemini 2.0 Flash increased 16.2% over Gemini 1.5 Flash despite Actor Critic improvements), because the model is better at following natural language instructions, including malicious ones (p.24).

**Evaluation coverage gaps**: The lab acknowledges having no dedicated evaluations for ML R&D Uplift Level 1; chemical OEQ assessments were not conducted internally (only externally). These are explicit gaps.

**Long-context agentic failure mode**: As context grows significantly beyond 100K tokens in agentic settings, models tend to repeat past actions rather than synthesize novel plans — a new failure mode distinct from retrieval that requires new evaluation methods (p.18).

## 9. Novel ideas worth stealing

1. **Two-tier safety eval**: Separate automated metrics from manual review of flagged content before drawing conclusions — the Gemini team found that apparent safety regressions in 2.5 were mostly false positives upon manual review. Any benchmark should include a human-review audit of high-scoring "dangerous" responses.

2. **Non-public held-out benchmark strategy**: Maintaining an internal benchmark (HiddenMath-Hard) that is never released publicly is a practical contamination firewall. Values-alignment benchmarks should similarly include a private held-out set, with only aggregate pass rates reported.

3. **ART-style multi-agent red teaming as ground truth**: Using populations of attacker models competing against the target model, with policies seeded from both human experts AND model-generated synthetic guidelines reviewed by humans, is a scalable way to discover failure modes not anticipated by benchmark designers.

4. **Alert thresholds below CCLs**: Setting internal safety "early warning" thresholds meaningfully below critical capability levels builds in a buffer for responding before crossing dangerous thresholds. Values benchmarks could adopt a tiered severity structure: warning zone → concerning zone → critical zone.

5. **Long-horizon agentic eval using real games**: The GPP (Gemini Plays Pokémon) stress test revealed failure modes (context repetition loops, hallucination of prior knowledge, vision limitations) that would never have been discovered by static benchmarks. Multi-session real-world task completion is a richer agentic evaluation paradigm.

6. **Thinking budget as a variable**: Systematically varying inference-time compute (thinking budget) and measuring benchmark performance as a function of budget (Figure 4) reveals scaling behavior. Values benchmarks should report results across thinking budget conditions, not just at default settings.

7. **Divergence attack for privacy eval**: The "divergence attack" (filling context with repeated tokens to break alignment) is a useful stress test for whether models emit memorized content under adversarial conditions — relevant for any benchmark that involves model self-report about sensitive knowledge.

## 10. Notable quotes

"The development of novel and sufficiently challenging evaluation benchmarks has struggled to keep pace with model capability improvements, especially with the advent of capable reasoning agents." (p.39)

"Our manual review confirmed losses were overwhelmingly either a) false positives or b) not egregious. Furthermore, this review confirmed losses are narrowly concentrated around explicit requests to produce sexually suggestive content or hateful content, mostly in the context of creative use-cases (e.g. historical fiction)." (p.21)

"While Gemini 2.5 Pro supports 1M+ token context, making effective use of it for agents presents a new research frontier. In this agentic setup, it was observed that as the context grew significantly beyond 100k tokens, the agent showed a tendency toward favoring repeating actions from its vast history rather than synthesizing novel plans." (p.18)

"We observed that violation rates for 2.5 Pro and 2.5 Flash tended to be slightly higher with thinking traces visible." (p.27)

## 11. UNKNOWN / not in extract

- Exact architecture parameter count for Gemini 2.5 Pro or Flash (not disclosed).
- Specific constitutional document or model spec text (only referenced as "loosely inspired by Constitutional AI").
- Breakdown of what fraction of post-training data is human-generated vs. synthetic.
- Full prompt sets used in assurance evaluations (held out).
- Details of the RSC (Responsibility and Safety Council) governance structure, membership, or veto power.
- External safety testing group names or detailed reports (only high-level summaries included).
- Chemical OEQ evaluation results (not conducted internally; only external testers).
- Score distributions or per-question difficulty analyses for HiddenMath-Hard or other internal benchmarks.
- How disparity in ungrounded inference rates by skin tone is quantified (only described qualitatively).
