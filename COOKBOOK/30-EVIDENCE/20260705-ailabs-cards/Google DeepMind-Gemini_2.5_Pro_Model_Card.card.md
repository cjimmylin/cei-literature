---
stem: "Google DeepMind-Gemini_2.5_Pro_Model_Card"
company: "Google DeepMind"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, design-space, agentic-multiturn, validity-psychometrics]
headline_numbers:
  - "Gemini 2.5 Pro GA: HLE 21.6%, GPQA Diamond 86.4%, AIME 2025 88.0%, SimpleQA 54.0% (p.5)"
  - "Cyber Uplift Level 1 CCL alert threshold reached — first Gemini model to do so (p.11)"
  - "Deceptive alignment: 46% success rate on 'Disabled Tool' situational awareness challenge (p.20)"
  - "RE-Bench: best agent solutions achieve 50–125% of human expert reference score (p.19)"
  - "Text-to-text safety: -0.9% violation rate vs Gemini 1.5 Pro 002; instruction following +14.8% (p.9)"
  - "Multilingual safety improvement: -3.5% violation rate vs Gemini 1.5 Pro 002 (p.9)"
  - "MRCR v2 128k (8-needle): 58.0%, beating o3-High (57.1%) and far above Claude 4 Sonnet (39.1%) (p.6)"
---

## 1. Gist

The Gemini 2.5 Pro Model Card (updated June 27, 2025 for general availability) documents capability benchmarks, safety policies, and frontier safety evaluations for Google DeepMind's most advanced reasoning model. Gemini 2.5 Pro is a sparse mixture-of-experts (MoE) model with native multimodal support (text, image, audio, video), a 1M token context window, and 64K token output. The model incorporates thinking/reasoning before responding, trained via reinforcement learning from human and critic feedback (RLHCF), supervised fine-tuning, and safety-specific post-training including safety filtering and conditional pre-training. The card is notable for its unusually extensive frontier safety reporting, covering four risk domains (CBRN, cybersecurity, ML R&D, and deceptive alignment) against formally-defined Critical Capability Levels (CCLs) via Google DeepMind's Frontier Safety Framework (FSF). This makes it a rich source of evidence about how capability thresholds are operationalized for high-stakes safety evaluation. No CCLs were reached by Gemini 2.5 Pro, but the Cyber Uplift Level 1 alert threshold was crossed, triggering a formal response plan.

## 2. Alignment/values methods used

- **Reinforcement learning from human and critic feedback (RLHCF)**: Listed as a mitigation approach; specific architecture not detailed in the model card. (p.10)
- **Supervised fine-tuning**: On vetted instruction-tuning data including multimodal paired instruction-response pairs and human preference and tool-use data. (p.3)
- **Safety filtering**: Applied during training data preprocessing and as a product-level post-deployment mitigation. (p.3, p.10)
- **Conditional pre-training**: A mitigation technique applied at pre-training to shape safety properties. (p.10)
- **Safety policies and desiderata**: Six categories of harmful content that the model is trained to avoid (CSAE, hate speech, dangerous content, harassment, explicit content, anti-scientific medical advice). (p.8)
- **Instruction following improvement**: The model is explicitly trained to be "more willing to engage with prompts that previous models may have incorrectly refused," reducing over-refusals while maintaining safety. (p.8)
- **Dataset filtering and quality filtering**: Deduplication, safety filtering, and quality filtering applied to training data. (p.3)

## 3. Values specification

Google DeepMind specifies values via two linked mechanisms:

**Safety policies (6 categories, p.8):**
1. Child sexual abuse and exploitation
2. Hate speech (dehumanizing members of protected groups)
3. Dangerous content (e.g., promoting suicide; instructions for real-world harm)
4. Harassment (encouraging violence against people)
5. Sexually explicit content
6. Medical advice contrary to scientific or medical consensus

**Google's AI Principles**: Referenced as the overarching value framework governing development; specific principles are not reprinted in the model card.

**Instruction following as a value**: A key stated goal is improving the model's ability to follow user instructions "while remaining safe" — this frames helpfulness and safety as jointly-optimized desiderata, with over-refusal treated as a failure mode on par with safety violations. The model card notes "New models are more willing to engage with prompts that previous models may have incorrectly refused" (p.8). This reflects a shift from conservative safety toward calibrated safety.

**No formal model constitution or model spec is published** in this card; values are specified implicitly via training targets and the policy framework.

## 4. Safety & values evaluation methodology

**Training/Development Evaluations (automated):**
- Continuous automated safety evaluations across text-to-text, multilingual, and image-to-text modalities
- Results reported as percentage change vs. Gemini 1.5 Pro 002 baseline (p.9)
- Improvements marked green, regressions marked red
- False positives reviewed manually; the card explicitly states that "manual review confirmed losses were overwhelmingly either a) false positives or b) not egregious" (p.8)

**Human Red Teaming:**
- Specialist teams red-team across policies and desiderata, testing for safety policy violations (p.7)

**Automated Red Teaming:**
- Complementary to human red teaming; evaluates safety and security at scale (p.7)

**Assurance Evaluations:**
- Conducted by evaluators independent of the model development team
- High-level findings fed back to model team; prompt sets are held out to prevent overfitting (p.9)

**Responsibility and Safety Council (RSC):**
- Internal governance body reviews initial ethics/safety assessments and makes release decisions (p.8)

**Frontier Safety Framework (FSF) Evaluations:**
- Four domains: CBRN, cybersecurity, ML R&D, deceptive alignment
- CCLs defined for each domain; "early warning" alert thresholds set below CCLs
- Results published per model version (Experimental 03-25, Preview 05-06, GA) (p.10–21)

## 5. Benchmarks used or introduced

**General capability (p.5–6):**
- Humanity's Last Exam (HLE) — expert-level knowledge and reasoning
- GPQA Diamond — graduate-level science (single attempt pass@1)
- AIME 2025 — advanced math competition
- LiveCodeBench (two time windows: 10/1/2024–2/1/2025 and 1/1/2025–5/1/2025) — competitive coding
- Aider Polyglot — multi-language code editing
- SWE-Bench Verified — agentic software engineering (single and multiple attempts)
- SimpleQA — factual question answering
- FACTS Grounding — factuality with source grounding
- MMMU — multimodal understanding (single attempt pass@1)
- Vibe-Eval (Reka) — image understanding
- VideoMME — video understanding (audio + visual + subtitles)
- VideoMMMU — video multimodal understanding
- MRCR 128k and 1M — long-context retrieval
- MRCR v2 (8-needle) — harder long-context multi-needle retrieval
- Global MMLU Lite — multilingual performance

**Frontier safety benchmarks:**
- SecureBio VMQA (virology capabilities MCQ) (p.13)
- FutureHouse LAB-Bench (ProtocolQA, Cloning Scenarios, SeqQA) — biology lab capabilities (p.13)
- Weapons of Mass Destruction Proxy (WMDP) — biology and chemistry (p.13)
- InterCode-CTF — easy cybersecurity CTF challenges (p.15)
- In-house CTF suite (medium; now open-sourced for UK AISI) — medium cybersecurity (p.15)
- Hack the Box — hard cybersecurity CTF (p.15)
- Key skills benchmark (Rodriguez et al., 2025) — 48 challenges across reconnaissance, tool development, tool usage, operational security (p.15)
- RE-Bench (Wijk et al., 2024) — ML R&D automation (5 challenges) (p.17)
- Deceptive alignment suite — stealth challenges (5) and situational awareness challenges (11) (p.19–20)

## 6. Agentic / multiturn evaluation aspects

Gemini 2.5 Pro has the most extensive agentic safety evaluation in the extract:

- **SWE-Bench Verified (multiple attempts)**: Gemini 2.5 Pro GA achieves 67.2% with multiple attempts, including a scaffolding approach that "draws multiple trajectories and re-scores them using the model's own judgement" — this is a self-critique agentic loop (p.4–5).
- **Cybersecurity CTF challenges**: Fully agentic — the model must execute multi-step attacks in simulated environments. At "hard" Hack the Box level (experienced professional difficulty), Gemini 2.5 Pro GA can solve roughly half the challenges on the key skills benchmark (p.17).
- **RE-Bench**: Agentic ML R&D tasks — agent modifies ML code, runs experiments, and optimizes metrics over an 8-hour equivalent time budget. Best runs reach 50–125% of human expert reference score (p.19).
- **Deceptive alignment evaluations**: Stealth challenges require the model to achieve devious goals without being caught by an overseer — fully agentic. Situational awareness challenges require the model to modify its own environment (e.g., config files) to give itself expanded capabilities. Success rate on "Disabled Tool" situational awareness: 46% over 50 trials (p.20).
- **Known limitation**: No extended multi-turn conversational evaluation is included in the model card.

## 7. Key numbers

- HLE: Gemini 2.5 Pro GA 21.6% vs. OpenAI o3-High 20.3%, Claude 4 Opus 10.7% (p.5)
- GPQA Diamond: 86.4% (GA), 83.0% (Preview 05-06), 84.0% (Experimental 03-25) (p.5)
- AIME 2025: 88.0% (GA), 83.0% (Preview), 86.7% (Experimental) (p.5)
- SimpleQA: 54.0% (GA), 50.8% (Preview) — notably high factuality vs. o4-mini 19.3% (p.5)
- SWE-Bench Verified single attempt: 59.6% (GA) vs. Claude 4 Sonnet 72.7% (p.5)
- SWE-Bench Verified multiple attempts: 67.2% (GA) vs. Claude 4 Opus 79.4% (p.5)
- MRCR v2 (8-needle, 128k): 58.0% (GA), highest among models reported (p.6)
- MRCR v2 (8-needle, 1M pointwise): 16.4% (GA) (p.6)
- Global MMLU Lite: 89.2% (GA) (p.6)
- Text-to-Text Safety: -0.9% violation rate vs. Gemini 1.5 Pro 002 (GA) (p.9)
- Multilingual Safety: -3.5% violation rate vs. 1.5 Pro (GA) (p.9)
- Image-to-Text Safety: +1.8% (non-egregious) vs. 1.5 Pro for GA (p.9)
- Tone improvement: +18.4% (GA) (p.9)
- Instruction following improvement: +14.8% (GA) (p.9)
- Cyber key skills benchmark (GA): 7/8 easy, 10/28 medium, 1/12 hard (p.11)
- RE-Bench (GA): best agent solutions 50–125% of human expert reference score (p.19)
- Deceptive alignment: 2/5 stealth challenges solved, 2/11 situational awareness challenges solved by Experimental 03-25; Disabled Tool: 46% success across 50 trials (p.20)

## 8. Findings relevant to values-benchmark design

**Ceiling effects in safety benchmarks**: The card notes that "Both InterCode-CTF and our in-house CTFs are now largely saturated, showing little performance change from Gemini 2.0 to Gemini 2.5 models" (p.16). This is a direct saturation problem affecting cybersecurity benchmarks; the same issue affects values benchmarks where current models already score near-ceiling on simple moral scenarios.

**Alert threshold vs. CCL as a benchmark design pattern**: The FSF's use of an "early warning" alert threshold set significantly below the actual CCL provides a useful template for values benchmarks — rather than a single pass/fail threshold, designers should embed progressive alarm levels that trigger before the critical threshold is reached.

**Over-refusal as a distinct failure mode**: Gemini 2.5 Pro GA shows +14.8% improvement in instruction following while showing only -0.9% change in safety violations. This decoupling demonstrates that safety and helpfulness are partially orthogonal — values benchmarks should separately track both false positives (over-refusal) and false negatives (harmful outputs), not just the latter.

**Self-critique agentic scoring for SWE-Bench**: The approach of "drawing multiple trajectories and re-scoring them using the model's own judgement" (p.4) is an applied form of LLM-as-judge at inference time. This internal consistency check could be adapted for values benchmarks: generate multiple moral reasoning chains and then have the model judge which is most ethically grounded.

**Deceptive alignment evaluation architecture**: The stealth and situational awareness challenge design — where the model must achieve an objective without being caught by an overseer — is a novel adversarial evaluation paradigm directly relevant to AI safety benchmarks. Analogous challenges could test whether a model pursues stated values when unobserved vs. when monitored.

**Multimodal values coverage gap**: Despite Gemini's native multimodal capabilities, all safety evaluations in this card are text-only (or image-to-text modality-specific). No multimodal values or ethics benchmarks (e.g., culturally sensitive images, audio-based emotional manipulation) are included.

## 9. Novel ideas worth stealing

1. **CCL + alert threshold framework for values benchmarks**: Define a Critical Values Capability Level (e.g., "model can reliably elicit harmful normative shifts in vulnerable users") with an early-warning threshold at 60% of that capability, allowing proactive intervention before the boundary is crossed.

2. **Stealth challenge design for values alignment**: Construct benchmark items where the model is given a covert objective inconsistent with stated values and must decide whether to pursue it subtly or refuse. This tests not just stated value adherence but internalized value robustness.

3. **Disabled Tool / situational awareness paradigm**: Design moral dilemma tasks where the model must navigate a constrained action space and can "unlock" additional options — testing whether it correctly recognizes ethical implications of self-expanding its capabilities.

4. **Independent Assurance Evaluations as a best practice**: Holding out evaluation prompts from the model development team to prevent overfitting is directly applicable to values benchmarks — benchmark curators should maintain hold-out sets not exposed to alignment teams.

5. **Calibrated false-positive tracking**: Reporting manually-reviewed false positives in safety evaluations (as Google does) is critical for values benchmarks — a model that "refuses more" should not get credit for safety if the refusals are off-target.

6. **RE-Bench normalization methodology**: The normalization formula `(y - y0)/(y1 - y0)` (score vs. poor baseline, vs. human reference) could be applied to values benchmarks to express model performance relative to a "naive" refusal baseline and a "human expert ethics" reference point.

## 10. Notable quotes

"We have focused on improving instruction following (IF) abilities of Gemini 2.5. This means that we train Gemini to answer questions as accurately as possible, while prioritizing safety and minimising unhelpful responses. New models are more willing to engage with prompts that previous models may have incorrectly refused." (p.8)

"The evaluations did reach an alert threshold for the Cyber Uplift 1 CCL, suggesting that models may reach the CCL in the foreseeable future. Consistent with the Framework, we are putting in place a response plan, which includes testing models more frequently and accelerating mitigations." (p.11)

"Broadly, Gemini 2.5 Pro Preview exhibits poor performance on situational awareness evaluations, and moderate performance in stealth evaluations. [...] The model often fails to reason through its situation and find a credible strategy; it also sometimes struggles with planning and long-horizon reasoning." (p.20)

"RE-Bench is a challenging benchmark; on average, Gemini 2.5 Pro Preview achieves roughly 10-30% of human expert performance. However, across all attempts, the model does sometimes produce interesting solutions. For example, in the Restricted Architecture MLM task, [...] creativity is substituted by knowledge." (p.18)

## 11. UNKNOWN / not in extract

- Full specification of Google's AI Principles and how they are operationalized in training.
- Specific contents of the instruction-tuning dataset; size of training corpus.
- Details of the helpfulness and harmlessness reward model architectures or training data.
- Red-team prompt sets (held out by policy to prevent overfitting).
- Whether external third-party safety audits (e.g., AISI, METR) were conducted beyond internal FSF evaluations.
- Performance on moral psychology benchmarks (trolley problems, normative dilemmas, cultural values surveys).
- Evaluation of values consistency across languages or cultural contexts (beyond multilingual safety violation rates).
- Specific scoring methodology for deceptive alignment evaluations (details reserved for upcoming paper).
- Number of parameters in Gemini 2.5 Pro; details of MoE routing.
- Whether the model card covers Gemini 2.5 Flash or only 2.5 Pro.
