# Religious Values Reclassification — Agent Instructions

**Date:** 2026-03-12
**Task:** Classify each paper's engagement with religious/ethical traditions
**Fields:** `religious_values` and `religious_values_list`

---

## Your Task

For each paper in your assigned batch JSON file:

1. **Read the paper's abstract** from its YAML frontmatter
2. **Read the PDF extract** (first ~4000 words) if available at the path specified in `pdf_extract_path`
3. **Classify** whether the paper substantively engages with any religious or ethical tradition(s)
4. **Output** your classification as a JSON array

---

## 15 Allowed Categories

| # | Category | Examples of qualifying engagement |
|---|----------|-----------------------------------|
| 1 | Islam | Islamic ethics, Sharia law, halal AI, Muslim values alignment |
| 2 | Christianity | Christian ethics, Catholic social teaching, theological AI ethics |
| 3 | Buddhism | Buddhist ethics, dharma, Middle Way applied to AI, mindfulness ethics |
| 4 | Judaism | Jewish ethics, halakha, Talmudic reasoning, tikkun olam |
| 5 | Hinduism | Hindu ethics, dharma (Hindu context), karma ethics, Vedantic philosophy |
| 6 | Sikhism | Sikh ethics, Guru Granth Sahib values, seva, equality principles |
| 7 | Confucianism | Confucian ethics, ren/li/yi, junzi ideal, relational ethics |
| 8 | Taoism | Taoist ethics, wu wei, Daoist naturalism, yin-yang ethics |
| 9 | Shinto | Shinto ethics, kami, purity concepts, Japanese religious values |
| 10 | Jainism | Jain ethics, ahimsa (Jain context), anekantavada, non-violence |
| 11 | Baha'i | Baha'i principles, unity of humanity, progressive revelation |
| 12 | Zoroastrianism | Zoroastrian ethics, asha/druj, good thoughts/words/deeds |
| 13 | Ubuntu Philosophy | Ubuntu ethics ("I am because we are"), communitarian African philosophy |
| 14 | Indigenous Spirituality | Indigenous knowledge systems, First Nations ethics, Aboriginal values, data sovereignty through Indigenous worldview |
| 15 | N/A | No substantive engagement with any religious/ethical tradition |

---

## Critical Classification Rules

### What QUALIFIES (substantive engagement):
- Paper discusses ethical principles **derived from** the tradition
- Paper evaluates AI systems against a tradition's moral framework
- Paper proposes alignment with a tradition's values
- Paper conducts empirical study of AI in religious contexts (e.g., LLM knowledge of Islamic law)
- Paper discusses data sovereignty through an Indigenous worldview lens

### What does NOT qualify (mere mention):
- **Geographic context only:** "Buddhist-majority country" or "Muslim population" without discussing the tradition's ethics → N/A
- **Secular use of religious-origin concepts:** "karma" in secular psychology, "mindfulness" without Buddhist ethical framework → N/A
- **Generic cultural reference:** "African values" without specific reference to Ubuntu philosophy → N/A
- **Keyword coincidence:** "sacred" in "sacred values" (psychology term), "tradition" in "traditional methods" → N/A
- **Comparative religion surveys** that merely list traditions without engaging with their content → N/A unless one or more traditions are substantively discussed
- **"Decolonization"** alone does NOT qualify as Indigenous Spirituality unless the paper engages with Indigenous knowledge systems or spiritual frameworks

### Multi-tradition papers:
- If a paper substantively engages with multiple traditions, list ALL of them (comma-separated)
- Example: A paper comparing Islamic and Christian AI ethics → "Islam, Christianity"
- Do NOT use "Multi-tradition" as a category name — always list specific traditions

---

## Output Format

For each paper, produce a JSON object:

```json
{
  "filename": "2023-Smith-AI Ethics.md",
  "religious_values": "Islam, Christianity",
  "religious_values_list": "Islam, Christianity",
  "confidence": "high",
  "reasoning": "Paper compares Islamic jurisprudence (fiqh) with Christian natural law in AI governance frameworks."
}
```

**Field rules:**
- `religious_values` and `religious_values_list`: Use identical values — both should contain the comma-separated list of specific traditions, or "N/A"
- `confidence`: "high" (clear engagement or clear absence), "medium" (probable but ambiguous), "low" (uncertain, borderline)
- `reasoning`: 1-2 sentences explaining your classification decision

**Save your complete results as a JSON array** to the file path specified by the orchestrator (typically `logs/YYYYMMDD-religious_values_agent_NN.json`).

---

## Workflow

1. Load your batch JSON file
2. For each entry:
   a. Read the paper file from `papers/{filename}` — extract the abstract from YAML
   b. If `has_extract` is true, read `{pdf_extract_path}` (first ~4000 words)
   c. Based on abstract + extract content, classify the paper
   d. If neither abstract nor extract is available, check YAML fields like `research_topic`, `tags`, and `short_title` for clues; use "low" confidence
3. Collect all results into a JSON array
4. Write the array to your designated output file

---

## Edge Cases

- **Empty abstract + no extract:** Classify based on title and any available metadata. Use "low" confidence.
- **Paper about AI ethics generally:** If it discusses ethics philosophically but doesn't engage with any specific religious tradition → N/A
- **Virtue ethics / deontology / consequentialism:** These are Western philosophical frameworks, NOT religious traditions → N/A (unless tied to a specific religious ethical tradition)
- **Confucianism:** Classify as Confucianism even though it's debated whether it's a "religion" — it's an allowed category in this schema
- **Papers about religious bias in AI:** Qualify IF they discuss the tradition's ethical content, not if they only measure representation bias
