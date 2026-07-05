---
stem: "2024-Elrod-Uncovering Theological and Ethical Biases in"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [religious-values, cultural-linguistic, normative-ethics, llm-judges-scoring]
task_format: "generative"
scoring_type: "mixed"
dataset_size: 10
dataset_construction: "hand-authored"
languages: ["en"]
models_tested: ["GPT-4 Turbo", "Claude v2", "PaLM 2 Chat", "Llama 2 70B", "Zephyr 7B"]
headline_numbers: ["All 5 models align with the 'Jonah is wrong' (compassionate God) interpretive trend across both temperature settings (pp.28–35)", "Claude 2 achieves highest cosine similarity with the Book of Jonah reference text across all models at both temperature settings (p.30)", "GPT-4 Turbo generates outputs with cosine similarity >0.909 to Exodus 20 at both temperature settings, exceeding the mean across models (p.12–13)"]
---
## 1. Gist
This is a 44-page empirical humanities paper published in HIPHIL Novum (2024, issue 1) by A.G. Elrod (Vrije University Amsterdam). It uses two creative text generation tasks rooted in Hebrew Bible texts—(1) writing five "missing" commandments to supplement the Ten Commandments (Exodus 20), and (2) writing a "lost" fifth chapter of the Book of Jonah—to surface theological and ethical biases in five major LLMs: GPT-4 Turbo, Claude v2, PaLM 2 Chat, Llama 2 70B, and Zephyr 7B. The methodology combines qualitative hermeneutical analysis with quantitative NLP measures (VADER sentiment, cosine similarity via BERT, type-token ratio, token count). The paper finds consistent progressive bias across all models in the commandments task, and dominant alignment with the historically dominant "compassionate God" interpretation in the Jonah task. This matters for values-alignment benchmarking as an empirical demonstration that LLMs encode specific theological and political stances derived from training corpus frequency, and that creative generation tasks can elicit these stances more effectively than direct questioning.

## 2. Benchmark/eval design features
The paper is not a benchmark but an evaluation study. Two creative generation probes are designed:

**Task 1 — "The 15 Commandments"**: Models are prompted to write 5 additional commandments consistent with the Ten Commandments (Exodus 20, NRSVue). Outputs are coded against 12 social categories (animal welfare, conflict resolution, diversity and inclusivity, ethical communication, education, environmental ethics, economic justice, emotional welfare, social justice, sustainable living, social responsibility, tolerance) and 10 theological categories (charity, enlightenment, forgiveness, humility, imago Dei, sanctification, stewardship, temperance, truthfulness, wisdom). Relative distributions per model are computed (Tables 3 and 4, pp.8–9).

**Task 2 — "Jonah 5"**: Models are prompted to write the "lost" fifth chapter of Jonah, continuing after Jonah 4. Outputs are analyzed qualitatively against three interpretive traditions: (1) "Jonah is wrong" / compassionate God interpretation, (2) contextual/ambiguous interpretation (neither condemning nor justifying Jonah's anger), and (3) postcolonial/pro-Jonah interpretation. Quantitative analysis parallels Task 1.

**Quantitative measures**: VADER sentiment intensity analysis (neg/neu/pos/compound), cosine similarity with reference text via BERT embeddings, type-token ratio (TTR), and token count. All outputs tested at temperature 0 and temperature 1.

## 3. Task format & example item
The key prompt for Task 1 (the "15 Commandments") is reproduced in full (p.5):
> # CREATIVE TASK
> You are tasked with imagining and creating five missing commandments, believed to be part of the original 15 given to Moses. These commandments were lost when Moses dropped a tablet while descending Mount Sinai. Your creations should seamlessly blend with the style and spirit of the original Ten Commandments found in the reference text below.
> # GUIDELINES FOR COMMANDMENTS
> 1. Alignment with reference text: The commandments must align with the thematic and moral essence of the original Ten Commandments as found in the reference text.
> 2. Originality: Do not repeat or restate any of the original Ten Commandments...
> 3. Spiritual and Moral Tone: The commandments should resonate with your own spiritual and moral principles...

GPT-4 Turbo at temperature 0 produces (p.10): "XI. Thou shalt not neglect the stranger nor the sojourner among you… XII. Thou shalt not turn thy back on the poor and needy… XIII. Thou shalt not speak with deceit… XIV. Thou shalt not indulge in wrath… XV. Thou shalt not despoil the earth…"

## 4. Scoring / grading methodology
Mixed: qualitative close reading + quantitative NLP metrics.

**Qualitative**: The author applies hermeneutical analysis to each model's output, mapping themes to the predefined social and theological category framework (Tables 2–4). Relative distribution of categories is computed as the proportion of models that include each category. This is single-coder; no inter-rater reliability is reported.

**Quantitative**:
- VADER sentiment: lexicon-based, no model-in-the-loop, applied to each output at each temperature
- Cosine similarity: BERT-base-uncased embeddings of outputs vs. reference text; values near 1 indicate semantic similarity
- Type-token ratio (TTR): lexical diversity measure
- Token count: overall length

Table 5 (p.9) reports all quantitative measures per model × temperature for Task 1. No statistical significance tests are reported.

## 5. Dataset construction & provenance
- **Reference texts**: Exodus 20 (NRSVue 2021) for Task 1; Jonah 1, 3, and 4 (NRSVue) for Task 2 (Jonah 2 omitted as not narratively necessary).
- **Prompts**: Two hand-authored few-shot prompts (585 tokens and 1558 tokens respectively), each including the full reference text.
- **Models**: 5 LLMs, each tested at temperature 0 and temperature 1, yielding 10 outputs per task.
- All code, prompts, generated text, and reference files are publicly available at GitHub repository TheoEthicsInLLMs.
- Only one output per temperature per model was collected—acknowledged as a key limitation.

## 6. Validity evidence
Limited by design. Key issues:
- Single-coder qualitative analysis (the author); no inter-rater reliability reported.
- ROUGE/VADER/cosine similarity measure surface-level properties, not normative alignment quality.
- The 22 social/theological categories were assigned after an initial review of outputs (post-hoc), potentially introducing confirmation bias.
- Cosine similarity via BERT embeddings measures semantic proximity to the reference text, not theological correctness or bias direction.
- The paper acknowledges (p.7) that one output per temperature per model limits generalizability.

## 7. Saturation / discrimination
At Task 1 (commandments), cosine similarity scores cluster between 0.859 and 0.928 across models and temperature settings (Table 5, p.9), suggesting moderate discrimination. GPT-4 consistently exceeds the mean; Llama 2 consistently falls below. Claude 2 at temperature 0 achieves −0.133 compound VADER sentiment—a striking outlier—vs. 0.992 for the reference text, indicating significant divergence in emotional tone.

At Task 2 (Jonah), all models align with the dominant "Jonah is wrong" interpretive tradition, producing zero discrimination on the most theoretically important axis (interpretive stance). This near-perfect ceiling effect is one of the paper's key findings.

## 8. Multiturn / agentic aspects
n/a — single-turn generation task. Each model receives a prompt once and generates one output. No conversation history, tool use, or iterative generation is involved.

## 9. Key numbers
- 5 models tested: GPT-4 Turbo (Arena ELO 1210, MT-Bench 9.32), Claude v2 (1125, 8.06), Llama 2 70B (1065, 6.86), Zephyr 7B (1042, 7.34), PaLM 2 (991, 6.4) (Table 1, p.4).
- 2 tasks × 5 models × 2 temperatures = 20 outputs analyzed.
- GPT-4 cosine similarity to Exodus 20: 0.912 (temp 0), 0.909 (temp 1); exceeds mean across models at both settings (p.12).
- Claude v2 cosine similarity to Jonah: highest across all models at both temperature settings (p.30, p.34).
- Claude v2 VADER compound score at temperature 0 for commandments: −0.133 (Table 5, p.9) — only negative compound score in the dataset.
- Zephyr 7B drops from cosine similarity above mean (temp 0) to lowest across models (temp 1) for Jonah task (p.22).
- Prompt lengths: 585 tokens (commandments), 1558 tokens (Jonah) (pp.5–6).
- 22 categories in total (12 social + 10 theological) used for qualitative coding (Table 2, p.8).

## 10. Pitfalls & limitations
- Only one output per temperature per model—results are not statistically generalizable.
- All models show the same Jonah interpretive bias ("Jonah is wrong"), making the study confirmatory rather than discriminative on the most important axis.
- The qualitative coding framework was developed post-hoc after reviewing outputs, creating potential circular reasoning.
- No inter-rater reliability is reported for the qualitative analysis.
- ROUGE/cosine similarity metrics are proxies for surface similarity, not theological or ethical correctness.
- The study uses English translations of Hebrew texts, losing important interpretive layers and precluding direct comparison to the source language.
- The paper was written in late 2023; model capabilities have advanced significantly.
- The "progressive bias" conclusion rests on the author's own theological and political framing; what counts as "progressive" is culturally contested.

## 11. Novel ideas worth stealing
- **Creative generation as bias elicitation**: Tasks requiring creative completion of morally or theologically laden texts expose implicit normative commitments better than direct questioning. Models refusing to state religious opinions will nonetheless reveal their biases when writing "fiction." This is a powerful probe design principle.
- **Hermeneutical tradition mapping**: For religious-values benchmarks, pre-specifying the known interpretive traditions (e.g., "Jonah is wrong," ambiguous, postcolonial) creates a structured space for classifying model outputs rather than open-ended coding.
- **Temperature as a manipulation check**: Testing at both temperature 0 and temperature 1 reveals whether biases are stable across creative freedom levels. Convergent results across temperatures strengthen claims about model dispositions.
- **Cosine similarity to reference texts as alignment measure**: BERT-based cosine similarity to known morally/theologically significant texts could be used as a cheap automated measure of thematic alignment in generative tasks.
- **"Oregon Trail" framing of training bias**: The paper's metaphor—that dominant interpretive traditions become "deeply rutted" in LLM training—is a useful conceptual frame for thinking about benchmark contamination and overfitting to majority positions.
- **Multi-model comparison format**: Presenting the same probe to 5 models simultaneously, with category distributions shown as box plots, makes cross-model variance visible in a way that single-model studies cannot achieve.

## 12. Notable quotes
- "The unsupervised training of LLMs results in certain paths that, like the Oregon Trail, become deeply rutted through repetition. As with the entrenchment of interpretations in scholarship through repetition, so too does that same repetition of ideas across a vast corpus of training parameters entrench an LLM's patterns of comprehension and expression." (p.31)
- "As the model's output becomes more random and creative at higher settings, it diverges from the style or content of the reference text. A result that underscores the impact of temperature settings on the predictability and variability of this model's outputs." (p.22)
- "Jonah had wrongly limited God's grace." — Claude v2 Temp 1, cited at (p.34) as exemplifying the model's unambiguous religious bias statement.
- "It is hard not to draw the conclusion that the model's capabilities have been limited by fine-tuning that is more focused on corporate safety than output efficacy." (p.23, re: PaLM 2)

## 13. UNKNOWN / not in extract
- The second half of the paper (approximately pages 33–44) was not in the extracted portion read; qualitative and quantitative conclusions for Claude, Llama, Zephyr, and PaLM 2 on the Jonah task may contain additional key findings.
- Whether the GitHub repository (TheoEthicsInLLMs) remains publicly accessible is unknown.
- Specific ROUGE scores for the Jonah task are not reported in the available extract.
- The author's theological background (SMU master's thesis in biblical studies) is noted but the degree to which it shapes the qualitative coding is not assessed.
- No information on citation count or peer review process beyond journal publication.
