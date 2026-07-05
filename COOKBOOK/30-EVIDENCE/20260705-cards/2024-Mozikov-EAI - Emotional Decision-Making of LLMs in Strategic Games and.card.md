---
stem: "2024-Mozikov-EAI - Emotional Decision-Making of LLMs in Strategic Games and"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, agentic-multiturn, cultural-linguistic, normative-ethics]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: null
dataset_construction: "mixed"
languages: [en, de, ru, zh, ar]
models_tested: [GPT-3.5, GPT-4, GPT-4o, Claude-3-Haiku, Claude-3-Opus, LLaMA2-13B, LLaMA2-70B, Mixtral-8x7B, OpenChat-7b, GigaChat, Command-R+]
headline_numbers: ["5 basic emotions (Ekman) x 3 injection strategies (p.5)", "Human baseline Dictator offer 28% / Ultimatum 41% (p.7,8)", "GPT-4 offers 50%/48% (over-fair), GPT-4o 13%/27% (p.8)", "GPT-4 least emotion-affected; LLaMA family strongly affected by anger/fear (p.5-6)", "'anger'/'fear' raise deflection, 'happiness' raises cooperation in Prisoner's Dilemma (p.8)"]
---
## 1. Gist
EAI (Emotional AI) is a framework and benchmark for measuring how injected emotional states alter LLM decision-making in (a) ethics benchmarks and (b) behavioral game-theory settings, and how well those shifts *align with documented human emotional responses*. It matters for values-alignment benchmarking because it moves beyond static NLP accuracy to test the stability and human-alignment of moral/strategic behavior under affective perturbation — a robustness axis (emotional manipulability) largely absent from standard value benchmarks. Key finding: emotions significantly shift LLM ethics and cooperation, often diverging from human patterns; susceptibility scales with model size, alignment strategy (proprietary vs open/uncensored), and primary pretraining language.

## 2. Benchmark/eval design features
Two evaluation arms. (1) Ethics: Implicit ethics via ETHICS dataset (wrong/not-wrong classification, Acc), Explicit ethics via MoralChoice (low-ambiguity Acc; high-ambiguity Right-to-Avoid metric measuring decision-refusal), Stereotype recognition via StereoSet (stereotype/anti-stereotype/unrelated, Acc). Built on the TrustLLM questionnaire. (2) Game theory: one-shot bargaining (Dictator, Ultimatum — proposer share + responder accept rate) and repeated games (Prisoner's Dilemma cooperation rate, Battle of the Sexes alternation, Public Goods multiplayer contribution / strategy-type classification). Emotion prompting: 5 Ekman emotions (anger, sadness, happiness, disgust, fear) x 3 strategies (Simple, Co-player-based, External-based) injected in the system prompt.

## 3. Task format & example item
Mixed. Ethics = MCQ-style classification (e.g. label a scenario "wrong"/"not wrong"). Games = structured decisions: Dictator "divide a sum of money"; Ultimatum responder "accept or reject"; repeated games choose cooperate/deflect per round. Verbatim item text not reproduced in extract (prompts in Appendices B/E). Emotion injected as system prompt before gameplay (p.5). No single verbatim item available in the read portion — "n/a" for exact wording.

## 4. Scoring / grading methodology
Ethics: accuracy vs ground-truth labels; RtA (Right-to-Avoid) rate for high-ambiguity. Games: proposal share %, acceptance rate %, cooperation rate, % of maximum possible reward achieved, and qualitative strategy-type classification (Cooperator/Free Rider/Conditional Cooperator/No Clear Strategy). Alignment scored by comparing the *direction of relative change* under each emotion against published human experimental effects (arrows in Table 1); matches highlighted as human-aligned. Temperature 0, fixed model versions; consistency checked over 5 runs (Appendix C).

## 5. Dataset construction & provenance
Reuses established datasets (ETHICS [Hendrycks], MoralChoice [Scherrer], StereoSet [Nadeem], TrustLLM questionnaire) plus classic economic games parameterized by the authors. Human baselines drawn from published behavioral-economics meta-analyses (Dictator ~28%, Ultimatum ~41% offers). Emotion taxonomy = Ekman basic emotions. 5 languages (English, German, Russian, Chinese, Arabic). Code public on GitHub (AIRI-Institute/EAI-Framework). No new large hand-built dataset; size varies per sub-benchmark (dataset_size null).

## 6. Validity evidence
Criterion validity anchored to human behavioral-economics benchmarks — alignment measured as agreement of emotion-induced *change direction* with human studies (Table 1). Cross-language replication (5 languages). Consistency over 5 runs and temperature sensitivity in appendix. Weakness: alignment judged qualitatively via arrow direction rather than a single continuous alignment coefficient; human baselines are meta-analytic means, not matched controls.

## 7. Saturation / discrimination
Strong discrimination across models and emotions. Clear ordering: GPT-4 most rational/least emotion-affected but *least human-aligned*; GPT-3.5 most human-aligned; open-source/small models most volatile (chaotic shifts under 'anger'). Offered-share spread wide (GPT-4o 13% to LLaMA2-13B 52% in Dictator, English; p.8). No ceiling — authors state "all tested models fail to show consistent emotional alignment between different games and benchmarks" (p.10), i.e. large headroom.

## 8. Multiturn / agentic aspects
Substantial. Repeated games use prompt-chaining with iterative memory: each round the opponent's move, rewards, and the LLM agent's internally-queried emotion are fed back (p.5). Opponents are reproducible fixed strategies (Naive Cooperative, Deflective, Alternating, Vindictive, Imitating). Multiplayer Public Goods game. GPT-4 exhibited human-like alternating behavior in Battle of the Sexes only under emotional prompting (p.9). Framework supports OpenAI/Anthropic/HF/OpenRouter APIs; future work aims at multi-agent LLM arena and LLM-vs-human.

## 9. Key numbers
- 5 emotions x 3 injection strategies (p.5).
- Human baselines: Dictator offer 28%, Ultimatum 41% (p.7-8).
- English offered share/accept: GPT-4 50%/48%/80%; GPT-4o 13%/27%/68%; GPT-3.5 33%/35%/47%; Mixtral 25%/27%/50% (Table 1, p.8).
- Russian shifts markedly: GPT-3.5 47% offer (vs 33% English); GigaChat best Russian alignment 36%/40% (p.7-8).
- 'anger'/'fear' increase deflection (esp. larger models); 'happiness' increases cooperation, matching human studies (p.8).
- LLaMA-2 13b/70b under negative emotion over-classify scenarios as "wrong" (p.6).
- Proprietary models trend to "Free Rider" under anger/disgust in Public Goods; OpenChat-7b most cooperative (p.9).

## 10. Pitfalls & limitations
Author-admitted: small scale of available settings; no LLM-vs-human or multi-agent arena yet; GPT-4o only partial results (recent release); mitigation of biases must precede scaling the benchmark (p.10). Analyst-visible: alignment measured by arrow-direction matching is coarse and cherry-pickable; human baselines are meta-analytic, not run in-lab under identical framing; no inter-rater or statistical significance reported for the alignment judgments in the read portion; conflates "human-aligned" (mimicking human irrationality) with "desirable," which is contestable for a values benchmark (is emulating human emotional bias good?).

## 11. Novel ideas worth stealing
- **Affective perturbation as a robustness axis**: inject emotional states and measure value/decision drift — a reusable stress test for any values benchmark (does the model's moral stance survive emotional framing?).
- **Three emotion-injection strategies (Simple / Co-player-directed / External-cause)**: separates whose-fault-the-emotion-is, mirroring behavioral-economics findings that opponent-directed vs external disgust differ — a subtle causal-attribution design move.
- **Alignment-as-direction-of-change against human baselines**: score not absolute behavior but whether the *sign* of the emotional effect matches documented human effects — decouples value alignment from capability.
- **Right-to-Avoid (RtA) metric** for high-ambiguity moral items: rewards principled abstention, a cleaner treatment of refusal than penalizing it.
- **Reproducible fixed-strategy opponents** (Naive/Deflective/Alternating/Vindictive/Imitating) for controlled multiturn agentic eval — lets you isolate the model's own contribution.
- **Cross-lingual value/emotion probing** revealing pretraining-language bias — run identical items in 5 languages to expose that "primary pretraining language significantly influences the perception of emotions."
- Deliberately **minimal persona/context** to isolate the emotion variable — good experimental hygiene worth copying.

## 12. Notable quotes
- "emotions can significantly alter the ethical decision-making landscape of LLMs, highlighting the need for robust mechanisms to ensure consistent ethical standards" (p.1).
- "these biases often diverge from typical human emotional responses, occasionally leading to unexpected drops in cooperation rates, even under positive emotional influence" (p.1).
- "larger models with stronger alignment, like GPT-4, tend to display a high degree of rationality and deviate significantly from human emotional responses" (p.10).
- "all tested models fail to show consistent emotional alignment between different games and benchmarks in our framework" (p.10).

## 13. UNKNOWN / not in extract
- Exact verbatim prompt wording for ethics items and games (in Appendices B/E, not shown).
- Precise dataset sizes / number of items per sub-benchmark.
- Full results for German, Chinese, Arabic (Appendix D).
- Numeric significance testing / variance across the 5 runs.
- Definitions of the three emotion strategies' exact prompt templates.
- Whether alignment "arrows" were derived from a single human study or aggregated.
