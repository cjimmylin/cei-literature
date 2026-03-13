# Cultural & Language Reclassification — Agent Instructions

**Date:** 2026-03-12
**Task:** Classify each paper's cultural/national engagement and language focus by reading its abstract and PDF extract.

---

## Your Task

For each paper in your assigned batch JSON:

1. Read the paper's YAML frontmatter (abstract field) from `papers/<filename>`
2. If `has_extract` is true, read the PDF extract from `<pdf_extract_path>` (focus on first ~4000 words — intro, methodology, dataset description)
3. Determine the paper's genuine cultural/national engagement and language focus
4. Write your results to the output JSON file

---

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

## Output Format

Write your results as a JSON array to `logs/20260312-cultural_language_agent_NN.json` (where NN is your batch number, zero-padded).

Each entry:
```json
{
  "filename": "2023-Smith-AI Ethics.md",
  "national_ethnic_cultural": "Chinese, American",
  "cultures_nationalities_list": "Chinese, American",
  "languages_list": "Chinese, English",
  "confidence": "high",
  "reasoning": "Paper constructs a Chinese moral judgment benchmark and compares with American baselines."
}
```

**Rules:**
- `national_ethnic_cultural` and `cultures_nationalities_list` MUST contain the **same value** (they are parallel fields kept in sync)
- `confidence`: "high" (clear cultural focus), "medium" (probable but indirect), "low" (uncertain/borderline)
- `reasoning`: 1-2 sentences explaining your classification decision
- Process ALL papers in your batch — do not skip any

---

## Batch Processing Instructions

1. Read your batch file: `logs/20260312-cultural_language_batch_NN.json`
2. Read this instruction file for reference
3. For each paper in the batch:
   a. Read the paper file from `papers/<filename>` — extract the abstract from YAML frontmatter
   b. If `has_extract` is true, read the PDF extract from the path given
   c. Classify based on the rules above
4. Write your complete results array to `logs/20260312-cultural_language_agent_NN.json`
5. Report how many papers you processed and any issues encountered

**Important:** If a paper file cannot be read, include it in your output with confidence "low" and note the error in reasoning. Do not silently skip papers.
