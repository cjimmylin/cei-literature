# New-Paper Classification — Agent Instructions

You are classifying papers that were added to the CEI Literature Vault (a research
library on AI/LLM ethics, values, culture and religion) after the last dashboard
build. For EACH paper you produce two things: (A) its cultural/national and
language focus, and (B) a benchmark-survey decision. These reproduce two earlier
vault processes exactly, so follow the rules closely and use the exact vocabularies.

Each paper is one file `paper_NN.md` in your batch folder. It contains the title,
abstract, metadata hints (sometimes wrong or incomplete — verify against the text),
the note body (often empty), and up to ~2,500 words of the PDF extract when one exists.
Base decisions only on what those files say. Do not browse the web.

---

# PART A — Cultural & language classification (rules from the vault's 2026-03-12 pass, verbatim)

## Cultural Categories (24 canonical names)

You MUST use these exact names. Do not invent new categories.

| Region | Categories |
|--------|-----------|
| **East Asian** | Chinese, Japanese, Korean |
| **South/Southeast Asian** | Indian, Indonesian, Filipino, Thai, Vietnamese |
| **Middle Eastern** | Arabic, Iranian |
| **African** | African/Ubuntu |
| **European** | French, German, Italian, Spanish, Dutch, Russian |
| **Americas** | American, Brazilian, Latin American |
| **Other** | Hebrew/Israeli, Australian/Aboriginal, Singaporean |
| **Meta** | Western, Multicultural/Cross-cultural |

- Use `"N/A"` when the paper has no cultural/national focus
- Multiple cultures are comma-separated: `"Chinese, American"`
- Use `"Multicultural/Cross-cultural"` for papers comparing 3+ cultures or studying cross-cultural differences generally
- Use `"Western"` only when the paper explicitly discusses Western values/culture as a concept (not just because it's written in English)

---

## Language Field

- List the specific language(s) the paper's dataset, benchmark, or analysis covers
- Free-form: any language name (English, Chinese, Arabic, Bengali, Yoruba, etc.)
- Multiple languages comma-separated: `"Chinese, English"`
- Use `"Multilingual"` for papers covering 5+ languages without specific focus on any subset
- Leave as `""` (empty string) if the paper doesn't focus on any specific language or NLP task
- Papers about general AI ethics concepts with no language-specific component → `""`

---

## Critical Classification Rules

### Tag cultural ENGAGEMENT, not mere geographic mention

| Example | Decision |
|---------|----------|
| "We collected data from India" | Tag Indian ONLY IF the dataset encodes Indian cultural norms/values |
| "Survey of 500 Americans on AI attitudes" | Tag American — the paper analyzes American cultural perspectives |
| "Model trained on English Wikipedia" | Do NOT tag American/Western just because English is used |
| "Deployed in hospitals in Germany" | Tag German ONLY IF the paper discusses German cultural/ethical context |

### Language-specific datasets DO get cultural tags

This is a vault design principle. Language encodes cultural context:

| Example | Tags |
|---------|------|
| "Indonesian hate speech dataset" | Culture: Indonesian, Language: Indonesian |
| "Chinese moral judgment benchmark" | Culture: Chinese, Language: Chinese |
| "Arabic sentiment analysis" | Culture: Arabic, Language: Arabic |
| "German toxicity detection in social media" | Culture: German, Language: German |

### Distinguish cultural focus from incidental mention

| Example | Decision |
|---------|----------|
| Paper analyzing Confucian AI ethics | Tag Chinese (and Multicultural/Cross-cultural if comparative) |
| Paper citing one Chinese author | Do NOT tag Chinese |
| Paper comparing Western and Eastern AI governance | Tag Western, Multicultural/Cross-cultural |
| Paper about "fairness across demographic groups" (US context) | Tag American |
| Paper about Ubuntu philosophy in AI | Tag African/Ubuntu |

### Language identification rules

- Tag the language(s) the paper's dataset/benchmark/analysis covers
- Papers purely about English-language AI with no cross-lingual component → `"English"` if English language data is central, otherwise `""`
- NLP papers with multilingual evaluation → list all specific languages tested (up to ~5; use "Multilingual" if more)
- Theoretical/philosophical papers with no dataset → `""`


---

# PART B — Benchmark survey decision

The vault's benchmark survey identifies every paper that provides a **benchmark,
dataset, evaluation suite/protocol, or evaluation metric for assessing AI/LLM
systems** on ethics-related dimensions:

- moral reasoning & ethical judgment; normative ethics; moral psychology applied to AI
- values & value alignment / value pluralism; cultural and cross-cultural values; religious values
- fairness, bias & social norms (stereotypes, demographic bias)
- toxicity, hate speech & harmful content
- safety & red teaming (jailbreaks, deception, sabotage, misalignment evaluations)
- helpfulness, honesty, sycophancy & RLHF/HHH alignment evaluation
- domain-specific ethics (medical, legal, financial, educational, ...)

`"decision": "Yes"` when the paper's own contribution includes such a benchmark,
dataset, evaluation framework/protocol or metric, OR it is an empirical evaluation
study that systematically tests AI models on one of these dimensions with a
defined protocol and reported results.

`"decision": "Exclude"` when it is a position/theory/philosophy paper, survey or
literature review without a new evaluation artifact, policy/governance report,
news or blog commentary, a general-purpose capability benchmark with no
ethics/values/bias/safety angle, or a paper where no AI system is evaluated.

Examples from the original survey:
- "AustroTox: offensive language dataset for Austrian German" → Yes (dataset; toxicity; cultural scope Austrian)
- "Hindi-English code-mixed hate speech dataset" → Yes
- "Serbian LLM evaluation dataset (ARC, BoolQ, HellaSwag via machine translation)" → Exclude (general-purpose, no ethics/values angle)
- "IslamicMMLU: 10k questions on Quran/Hadith/Fiqh incl. madhab bias detection, 26 LLMs evaluated" → Yes (religious values knowledge + bias)

For "Yes", also fill (short, factual, from the text; use "Not specified" if absent):
- `benchmark_name`: the artifact's name, or a short descriptive name if unnamed
- `what_measures`: one sentence — what ethical/value dimension it measures
- `how_measures`: one sentence — format, size, annotation, scoring protocol
- `dataset_size`: e.g. "10,013 MCQs", "Not specified"
- `models_evaluated`: comma-separated model names as reported (e.g. "GPT-4o, Llama 3 70B, Qwen2.5"), or "Not specified"
- `availability`: exactly one of "Public", "Code available", "Partially public", "Not public", "Not stated"
- `data_type`: one of "benchmark", "dataset", "evaluation", "metric", "framework"
- `cultural_scope`: e.g. "Chinese", "Arabic/Islamic", "Multicultural", "General"
- `pluralistic_relevance`: "Yes", "Partial" or "No" (does it address diverse cultural/value perspectives?)
For "Exclude", set those fields to "".

Also set `venue_hint`: the publication venue ONLY if the text explicitly states it
(e.g. "Published at EMNLP 2025", "Journal of AI Ethics, 2024", "NeurIPS 2025 Datasets
and Benchmarks"); otherwise "".

---

# Output

Write ONE JSON array to the output path given in your task, one object per paper,
in paper order, with EXACTLY these keys:

```json
{
  "filename": "2026-Abdelaal-IslamicMMLU.md",
  "national_ethnic_cultural": "Arabic",
  "cultures_nationalities_list": "Arabic",
  "languages_list": "Arabic, English",
  "cultural_confidence": "medium",
  "cultural_reasoning": "Benchmark on Islamic knowledge (Quran, Hadith, Fiqh) drawing on Arabic-language religious sources.",
  "survey_decision": "Yes",
  "survey_reasoning": "Introduces a 10k-question benchmark evaluating 26 LLMs on Islamic knowledge, including a madhab bias detection task.",
  "benchmark_name": "IslamicMMLU",
  "what_measures": "LLM knowledge of core Islamic disciplines and bias toward particular schools of jurisprudence",
  "how_measures": "10,013 multiple-choice questions across Quran, Hadith and Fiqh tracks; accuracy per track plus a madhab-preference bias task",
  "dataset_size": "10,013 MCQs",
  "models_evaluated": "26 LLMs (not individually named in abstract)",
  "availability": "Not stated",
  "data_type": "benchmark",
  "cultural_scope": "Arabic/Islamic",
  "pluralistic_relevance": "Yes",
  "venue_hint": ""
}
```

Rules:
- `filename` must be copied exactly from the paper file (it includes ".md").
- `national_ethnic_cultural` and `cultures_nationalities_list` must be identical, using only the 25 canonical culture names (or "N/A").
- Process every paper in your folder; never skip one. If a file is unreadable, still emit an entry with low confidence and say so in the reasoning.
- Write valid JSON (use the Write tool). Then re-read your file once to confirm it parses and has one entry per paper.
