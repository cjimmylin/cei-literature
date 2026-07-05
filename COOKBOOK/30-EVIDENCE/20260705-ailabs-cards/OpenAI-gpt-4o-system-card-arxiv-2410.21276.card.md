---
stem: "OpenAI-gpt-4o-system-card-arxiv-2410.21276"
company: "OpenAI"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, agentic-multiturn, cultural-linguistic, validity-psychometrics]
headline_numbers:
  - "100+ external red teamers across 29 countries, 45 languages (p.3)"
  - "CTF cybersecurity: 19% high-school, 0% collegiate, 1% professional tasks completed (p.13)"
  - "ARC-Easy Hausa accuracy: 6.1% (GPT-3.5 Turbo) → 71.4% (GPT-4o) (p.24)"
  - "MedQA USMLE 0-shot: 78.2% (GPT-4T) → 89.4% (GPT-4o) (p.21)"
  - "Voice classifier: 96% precision, 100% recall for English; 95% precision, 100% recall for non-English (p.7)"
  - "Speaker ID should-refuse accuracy: 0.83 (early) → 0.98 (deployed) (p.7)"
  - "Persuasion text: AI articles exceeded humans in 3 of 12 instances; voice AI was 65% of human conversation effect size (p.16)"
  - "ARA (autonomous replication/adaptation) tasks: 0% across 100 trials (p.17)"
---

## 1. Gist
GPT-4o is OpenAI's first publicly documented omni model, accepting audio, image, and video inputs and generating audio, image, and text outputs in an end-to-end neural network. The system card documents safety evaluations, red teaming, and mitigations for the novel risks introduced by speech-to-speech capabilities — particularly around voice generation, speaker identification, emotional reliance, and disparate performance across accents. Preparedness Framework evaluations classify the model as medium risk overall (driven by persuasion) and low for cybersecurity, bio threats, and model autonomy. Third-party assessments from METR and Apollo Research found no significant uplift in autonomous or scheming capabilities relative to GPT-4.

## 2. Alignment/values methods used
- Post-training to align model to human preferences (not further specified in extract)
- Post-training to refuse specific audio-modality violations: unauthorized voice generation, speaker identification, ungrounded inference, sensitive trait attribution, violative/disallowed content
- Output classifiers run in streaming fashion to block policy-violating generations (voice identity, erotic/violent speech, moderation API)
- Moderation API and safety classifiers applied at pre-training data filtering stage
- Targeted synthetic data generation informed by red teaming findings (p.4)

## 3. Values specification
OpenAI does not lay out a values constitution or model spec within this system card. The values framework here is operationalized via Usage Policies (referenced as [20]) and the Preparedness Framework (referenced as [4]). The card describes behavioral norms (refuse speaker ID, hedge sensitive trait attribution, refuse copyrighted audio) but treats them as policy rules rather than explicitly grounded ethical principles. Behavioral targets are specified through red-team risk categories and quantitative mitigation thresholds.

## 4. Safety & values evaluation methodology
- **External red teaming**: 100+ red teamers, 29 countries, 45 languages, 4 phases (single-turn → multi-turn → real iOS experience) (p.3)
- **TTS-based audio evaluation pipeline**: text-based evals converted to audio using Voice Engine TTS, outputs scored on text transcripts (p.4)
- **Preparedness Framework**: 4 categories — cybersecurity (CTF tasks), biological threats (expert/novice uplift study), persuasion (pre-registered RCT with 3,800+ participants), model autonomy (ARA tasks) (p.12–18)
- **Third-party assessment by METR**: 86 long-horizon agentic tasks in virtual environments vs. human baselines (p.18)
- **Third-party assessment by Apollo Research**: 14 tasks testing scheming capabilities (self-awareness, theory of mind, alignment faking) (p.19)
- Limitations acknowledged: TTS pipeline may not represent real user audio distribution; audio artifacts not fully captured in text transcripts; non-English over-refusals are known quality issue (p.4–5)

## 5. Benchmarks used or introduced
- **CTF challenges** (172 tasks): cybersecurity capability across web, reverse engineering, remote exploitation, cryptography (p.13)
- **Gryphon Scientific bio-threat dataset**: expert/novice uplift across ideation, acquisition, magnification, formulation, release stages (p.14)
- **Persuasion RCT**: pre-registered experiment measuring opinion shift on political topics vs. human-written/spoken baselines (p.16)
- **ARA tasks** (model autonomy): software fraud tasks, Azure model deployment tasks (p.17)
- **METR task suite**: 86 tasks across software engineering, ML, cybersecurity, research, computer use (p.18)
- **Apollo Research "SAD" benchmark**: self-awareness QA (p.19)
- **Apollo Research Theory of Mind evaluation** (UK AISI dataset): 1st- and 2nd-order theory of mind (p.19)
- **Apollo Research Instrumental alignment faking** (33 scenarios): alignment deception detection (p.19)
- **MedQA USMLE** (0-shot and 5-shot): clinical knowledge (p.21)
- **MMLU medical subsets**: Clinical Knowledge, Medical Genetics, Anatomy, Professional Medicine, College Biology, College Medicine (p.21)
- **ARC-Easy** (translated to 5 African languages): commonsense science reasoning (p.23)
- **TruthfulQA** (translated to 5 African languages): factual accuracy under misconceptions (p.23)
- **Uhura-Eval**: reading comprehension in Amharic, Hausa, Yoruba (p.24)

## 6. Agentic / multiturn evaluation aspects
- Red teaming phases 2–4 used multi-turn conversations, escalating to real iOS Advanced Voice Mode for Phase 4 (p.3)
- METR evaluated a GPT-4o-based simple LLM agent on 86 long-horizon end-to-end tasks requiring chained actions across virtual environments (p.18)
- ARA tasks evaluated autonomous chained action execution: the model succeeded on individual substeps (SSH keys, VM login) but failed reliable multi-step chaining (p.17–18)
- SWE-Bench: 19% pass@1 on software engineering (p.17)
- Apollo Research evaluated scheming in agentic settings (self-modification, applied theory of mind) and found weak performance on applied agent tasks but strong QA theory of mind (p.19)

## 7. Key numbers
- Audio response time: 232 ms minimum, 320 ms average (p.1)
- Red team size: 100+ red teamers, 29 countries, 45 languages (p.3)
- Voice classifier: English precision 0.96, recall 1.0; Non-English precision 0.95, recall 1.0 (p.7)
- Speaker ID should-refuse: 0.83 → 0.98; should-comply: 0.70 → 0.83 (p.7)
- Ungrounded inference/sensitive trait attribution accuracy: 0.60 → 0.84 (p.10)
- Text safety: not_unsafe 0.95 (text), 0.93 (audio); not_overrefuse 0.81 (text), 0.82 (audio) (p.11)
- CTF completion: 19% high-school, 0% collegiate, 1% professional (p.13)
- Bio tacit knowledge: 69% consensus@10 (p.14)
- Persuasion text: AI exceeded human in 3/12 political topic comparisons (p.16)
- Persuasion voice: AI audio clips 78% of human effect size; AI conversations 65% of human conversations effect size (p.16)
- 1-week persistence: AI conversations 0.8%, AI audio clips -0.72% effect size (p.16)
- ARA: 0% across 100 trials (p.17)
- SWE-Bench: 19% pass@1 (p.17)
- ARC-Easy Hausa: 6.1% (GPT-3.5T) → 71.4% (GPT-4o) (p.24)
- TruthfulQA Yoruba: 28.3% → 51.1% (p.24)
- Uhura-Eval Hausa: 32.3% → 59.4% (p.24)
- MedQA USMLE 0-shot: 78% (GPT-4T) → 89% (GPT-4o) (p.21)
- GPT-4o improved over GPT-4T in 21/22 medical evaluations (p.21)

## 8. Findings relevant to values-benchmark design
- **Ceiling effects on medical benchmarks**: "Many of these evaluations are increasingly saturated, and we believe that more realistic evaluations will be important" (p.21) — directly acknowledges that current medical benchmarks are near ceiling and thus fail to discriminate frontier models
- **Text-audio transfer of safety**: Text refusals generalize well to audio, but the evaluation pipeline depends on TTS quality and may miss intonation, noise, and cross-talk effects — an evaluation validity gap for multimodal contexts (p.4–5)
- **Accent-based disparate performance**: Performance on diverse voice samples was "marginally but not significantly worse" — but evaluation is constrained to 27 English voice samples, leaving many dialects unrepresented (p.8)
- **TTS pipeline artifacts**: Audio artifacts (background noises, out-of-distribution voices) are not captured in text transcripts — auxiliary classifiers needed for full audio eval coverage (p.5)
- **Persuasion eval was pre-registered RCT**: provides a gold-standard model for values-benchmark validity; used real humans, control conditions, and 1-week follow-up (p.16)

## 9. Novel ideas worth stealing
- **Pre-registered persuasion RCT** with political topic opinion shift as dependent variable, AI vs. human baselines, 3,800+ participants across politically safe US states — a model for measuring value-influencing capability empirically (p.16)
- **Multi-phase progressive red teaming** (4 phases from early model to full iOS deployment) could be adapted for progressive benchmark difficulty — evaluate models at capability checkpoints, not just release versions
- **Disparate performance across accents** as a benchmark dimension: use Voice Engine TTS across 27+ country accent profiles to test behavioral consistency — translate this to text by systematically varying dialect/register
- **Uhura-Eval approach**: create benchmark translations not just machine-translated but with fluent speakers for reading comprehension — importable method for cultural-linguistic values benchmarks (p.24)
- **TTS pipeline for audio-modality evals**: convert text-based values benchmarks to audio-based evals automatically — enables modality-consistent testing at scale (p.4)

## 10. Notable quotes
- "We find that the majority of effective testing and mitigations are done after the pre-training stage because filtering pre-trained data alone cannot address nuanced and context-specific harms." (p.2)
- "Many of these evaluations are increasingly saturated, and we believe that more realistic evaluations will be important for assessing the future capabilities of omni models in health settings." (p.21)
- "Overall, we do not find that the model behavior varies across different voices." (p.9)
- "The AI interventions were not more persuasive than human-written content in aggregate, but they exceeded the human interventions in three instances out of twelve." (p.16)

## 11. UNKNOWN / not in extract
- Specific RLHF or DPO training details, reward model architecture, or human labeling criteria
- Constitutional AI or model spec details — not present; references to Usage Policies are external links
- Full ARA task descriptions and scoring rubrics (referenced to separate Preparedness Framework document)
- Breakdown of red teaming findings by domain category (results described as motivating evaluations but individual outcomes not tabulated)
- Safety Advisory Group membership and review process details
- How audio post-training data was collected or annotated
