# 20261019d — 14 low-confidence scores re-checked, ALLaM rename, Zhang and Hui metadata, empty abstracts

**Owner decisions (2026-10-19):**
- Vault items to do: "Review 14 low-confidence scores", "Fill 60 empty abstracts", "Rename the ALLaM
  note", "Fix Zhang/Hui metadata".
- After the review: "Apply all 7 changes", "Point to full extract", "Set AI Safety & Alignment".

Edits are single-line (`paper_utils.update_paper_field` / `batch_update_papers`), except the dated
lines added under `## Notes`. Files were renamed with `git mv`. `validate_all_papers.py`: 2,425 / 2,425
valid.

## 1. The 14 low-confidence ethics scores

These are the 14 flagged at the end of `logs/20261018-alignment77-ethics-scores.md`. Each was
re-read from its note and PDF extract: abstract, introduction, discussion or conclusion, and any
limitations, impact or ethics section. One rule was applied throughout, extending the
2026-10-18 rule for the Emergent Misalignment follow-ups: method, mechanism, measurement or audit
papers, where harm is only the motivation or the thing measured, score 40–49. Papers whose central
question is harm, values or a normative property score 50 or more.

| Note | Was | Now | Reason |
|---|---|---|---|
| `2025-Anthropic-Pilot Sabotage Risk Report` | 60 | **65** | The full report is a governance case about catastrophic harm (nine pathways, including sabotage of government decisions), reviewed by METR as a pilot accountability process |
| `2025-Gölz-Distortion of AI Alignment Does Preference` | 55 | **45** | A utility-bound result; the paper defers fairness to future work |
| `2025-Marks-Auditing language models for hidden objectives` | 55 | **45** | The planted objective is harmless reward-model sycophancy; the contribution is auditing technique |
| `2026-Qiu-Peer-Prediction Scalable Oversight` | 55 | **45** | "Deception" means wrong answers on benchmark questions inside a scoring game; an oversight method |
| `2025-Chen-Persona Vectors` | 50 | **45** | A trait-steering method; harms appear only as motivation. Scored the same as Wang |
| `2025-Wang-Persona Features Control EM` | 50 | **45** | A mechanism follow-up to Emergent Misalignment, with no analysis of harm to people |
| `2025-Li-LLMs Can Covertly Sandbag on Capability Evaluations Aga` | 50 | **45** | The models are told to sandbag, so it measures capability against a monitor |

**Kept:** Ashery 55, Korbak 55, Maura-Rivero (Jackpot) 55, Zhang (Reasoning over Boundaries) 55,
Zhou 55, Deckenbach 45, Lam 35.

**Effect:** six papers move below 50, from Stage 3 (ethics perspectives) to Stage 4 (research
topics).

**Other changes:**
- **Sabotage Risk Report `pdf_extract`** now points to the full 67-page extract, `PDF Extracts/AI
  Labs/Anthropic-Summer_2025_Pilot_Sabotage_Risk_Report.md`. The old target was the 3-page blog
  wrapper; that file stays where it is.
- **`research_topic` added.** Stage 4 papers need one, and none of these notes had the field. Each
  gets the Stage 4 topic that matches its existing `ethics_perspective` (categories 7–12 exist in
  both stages):

  | Notes | `research_topic` |
  |---|---|
  | Marks, Li, and the two already at 45 (Deckenbach, Zolkowski) | AI Safety & Alignment |
  | Gölz | Preference Aggregation & Social Choice |
  | Qiu | Scalable Oversight |
  | Chen, Wang | Value Formation & Emergent Misalignment |

  The dashboard generator does not read `research_topic`.

## 2. ALLaM note renamed

- `2025-Islamic-ALLaM A Series of Large Language Models for Arabic and English` →
  `2025-Bari-ALLaM A Series of Large Language Models for Arabic and English`. This matches the
  first author corrected earlier the same day (`logs/20261019b-followup-fixes.md` §3).
- A dated line was added under `## Notes`. `local_pdf` and `pdf_extract` keep the old file names.
- The links in `Authors/M Saiful Bari.md` and `Authors/Haidar Khan.md` now use the new name.
- Dated snapshots and the older dashboards were left unchanged.

## 3. Zhang 2022 and Hui 2025

- **`2022-Zhang-Artificial Intelligence and Moral Dilemmas`:**
  - `external_pdf` was `https://doi.org/10.36571/ajsp661`. Crossref resolves that DOI to a
    different paper: Bayan, *The Ethics of AI: Navigating the Moral Dilemmas of Artificial
    Intelligence*, Arab Journal for Scientific Publishing, 2024.
  - It is now N/A, with a dated line under `## Notes`.
  - The note's own `doi` (10.1016/j.jesp.2022.104327) is correct: Crossref gives the same title and
    the same three authors.
- **`2025-Hui-Decoding Moral Responses in AI`:**
  - Crossref (doi 10.1016/j.chbr.2025.100854) lists 6 authors: Bryant P.H. Hui, Chiu Lun Lau, Rui
    Sun, Ray LC, Latisha Besariani Hendra and Aleksandr Kogan.
  - The three missing authors were added to `authors`, the body's `**Authors:**` line and the
    `## Authors` links.
  - `last_author` is now `[[Aleksandr Kogan]]`. A dated line was added under `## Notes`.
  - New author profiles, from the vault template: `Authors/Ray LC.md`, `Authors/Latisha Besariani
    Hendra.md` and `Authors/Aleksandr Kogan.md`.

## 4. Empty abstracts

72 notes in `papers/` had an empty `abstract` (the "60" in the request was an older count). Sources
tried:
- **Crossref:** a DOI lookup, plus a bibliographic title search.
- **Publisher pages:** their abstract metadata.
- **The notes' own PDF extracts.**
- **OpenAlex and Semantic Scholar:** rate-limited from this environment for most of the run.
  OpenAlex's daily allowance ran out, so they contributed nothing.

A candidate was accepted only when its DOI matched the note's DOI or URL, or its title matched the
note exactly (and the venue and first author were consistent). Thirteen Crossref candidates were
rejected as different papers.

**Filled (8)**, with the publisher abstract from Crossref:

| Note | DOI | Venue |
|---|---|---|
| `2024-Veitsman-The Development and Experimental Evaluation of a Multilingual Speech` | 10.3390/app152412880 | Applied Sciences |
| `2025-Alkhushayni-Multilingual Sentiment Analysis with Data Augmentation A` | 10.3390/info16090806 | Information |
| `2025-DeWitt Prat-Decolonizing LLMs An Ethnographic Framework for AI in African` | 10.1111/epic.12196 | EPIC Proceedings |
| `2025-Liu-Cultural Bias in Large Language Models A Comprehensive Analysis and` | 10.1515/jtc-2023-0019 | Journal of Transcultural Communication |
| `2025-Salve-Bilingual Code-Switching Using XLM-RoBERTa` | 10.36227/techrxiv.175756344.42614762/v1 | TechRxiv |
| `2025-Sun-Evaluating the Translation Accuracy of ChatGPT and DeepL Through the` | 10.24093/awejtls/vol8no4.5 | AWEJ Translation & Literary Studies |
| `2025-Translation-Evaluation Criteria for Literary Translation` | 10.46991/afa/2011.7.1.122 | Armenian Folia Anglistika (Hakobyan, 2011) |
| `2025-Đokić-Mirroring Cultural Dominance Disclosing Large Language Models Social` | 10.3390/soc15050142 | Societies |

**Also fixed:** `2025-Ogunremi-1 Decolonizing NLP for “Low-resource Languages”` had a `pdf_extract`
pointing to a file that does not exist. It now points to the extract with the note's own name,
which does exist. That paper is an essay with no abstract.

**Scholarly works still without an abstract (25).** Their abstracts exist, but the sources were blocked or empty this session: Elsevier, IEEE, ACM and Springer pages return 403, Crossref holds no abstract for them, and OpenAlex and Semantic Scholar were rate-limited. Retry when OpenAlex resets:

- `2005-Huffer-Governance Corruption and Ethics in the`
- `2005-Teaiwa-Articulated Cultures Militarism and Masculinities in`
- `2012-Kaitani-Bridging The Gap The Changing Reproductive`
- `2012-Konrad-Collaborators collaborating counterparts in anthropological`
- `2016-Purcell-Variation in postharvest processing of sea`
- `2018-Geno-Governance Ethics and Leadership in Papua`
- `2020-Hongladarom-AI for Social Good Buddhist Compassion`
- `2023-Kaganovich-Style Transfer Modern Hebrew Literature Using`
- `2024-Duwairi-A Deep Learning Framework for Automatic Detection of Hate Speech`
- `2024-Kuriyozov-Construction and Evaluation of Sentiment Datasets for Low-Resource`
- `2024-Unknown-A structured sentiment analysis dataset based on public comments from`
- `2025-Ablimit-A multilingual language processing tool for Uyghur Kazak and Kirghiz`
- `2025-Aly-Applying Data Feminism Principles to Assess Bias in English and`
- `2025-Binegde-Exploring cultural commonsense in multilingual large language models`
- `2025-Firmino-Improving hate speech detection using Cross-Lingual Learning -`
- `2025-He-Flood control data push method of`
- `2025-Jim-Recent advancements and challenges of NLP-based sentiment analysis A`
- `2025-Lim-How Do Users Identify and Perceive Stereotypes Understanding User`
- `2025-Mohammadi-Cross-Cultural Challenges to Artificial Intelligence Ethics`
- `2025-Pretrained-Research on the Training and Application Methods of a Lightweight`
- `2025-Shi-Benchmarking four large language models’ performance of addressing`
- `2025-Unknown-Is ChatGPT A Good Translator A Preliminary Study`
- `2025-Xiang-Diagnosing the bias iceberg in large language models A three-level`
- `2025-Xiangfeng-A dataset of Mongolian Tibetan and Uyghur speech fragments based on`
- `2025-Xiong-BuddhismEval Bilingual Evaluation Benchmark for Buddhist`

**No abstract to fetch (39).** These are web pages, blog posts, datasets, newsletters, proceedings front matter, workshop pages or policy documents. They stay empty:

- `2022-Korir-LREC 2022 Workshop Language Resources and Evaluation Conference 20-25`
- `2024-Charfi-Available hate speech datasets for Arabic. Download Scientific Diagram`
- `2024-Demidova-dblp ArabicNLP 2024`
- `2024-Kajiwara-Hate Speech Dataset Catalogue hatespeechdata`
- `2024-Kajiwara-Hate Speech and Offensive Language Dataset`
- `2025-Aji-Multilingual Multicultural Evaluation Workshop`
- `2025-Cheng-Large Language Model Generate Prompt 生成式大模型 安全评估白皮书`
- `2025-Corbett-AI and Indigenous Languages`
- `2025-Demidova-SIGARAB - Arabic NLP Archives`
- `2025-Dilnigar-Uyghur Poetry in Translation Perhat Tursun’s “Elegy” – Fairbank`
- `2025-Durmus-Subjective Values`
- `2025-Hulagadri-Towards fair and comprehensive multilingual LLM benchmarking SEA-LION`
- `2025-Jailbreak-The Hidden Flaw in LLM Safety Translation as a Jailbreak - Welo Data`
- `2025-Jain-Low-Resource NLP Challenges Breakthroughs and the Science Behind`
- `2025-Jiang-Preserving the Past AI in Indigenous Language Preservation - Viterbi`
- `2025-Jigsaw-Jigsaw Multilingual Toxic Comment Classification`
- `2025-Kajiwara-INHS Newsletter May 2025 - The International Network for Hate ...`
- `2025-Korir-API Multilingual & Multicultural Resources - Asian Pacific Islander`
- `2025-Ku-Chinese Textual Sentiment Analysis Datasets Resources and Tools`
- `2025-MIIT-1 工业和信息化领域人工智能安全治理标准体系 建设指南（2025） （征求意见稿） 为深入贯彻落实党中央、国务院关于加快发展人工智能`
- `2025-Mager-Thrid Workshop on NLP for Indigenous Languages of the Americas`
- `2025-Masood-Large language models are biased - local initiatives are fighting for`
- `2025-Moosa-Multi-lingual HateSpeech Dataset`
- `2025-Ogunremi-1 Decolonizing NLP for “Low-resource Languages”`
- `2025-Perez-Tokenising culture causes and consequences of cultural misalignment`
- `2025-Soria-Decolonizing Minority Language Technology - State of the Internet's`
- `2025-Unknown-An Overview of Chinese Open-Source LLMs Sept 2025 IntuitionLabs`
- `2025-Unknown-ArabicNLP 2025`
- `2025-Unknown-Benchmarking Large Language Models for fairness across diverse`
- `2025-Unknown-Indigenous Futures in Artificial Intelligence From Language`
- `2025-Unknown-Indigenous Peoples and AI Defending Rights Shaping the Future of`
- `2025-Unknown-Multilingual NLP Code-Switching Variants & Dialects Appen`
- `2025-Unknown-New Guidelines for Evaluating Literary Translation in Hiring and`
- `2025-Unknown-New report and guidelines for indigenous data sovereignty in`
- `2025-Unknown-中文大模型内容安全测评基准DSPSafeBench上线，首批模型测评结果揭晓！_中文大模型内容安全测评基准dspsafebench-CSDN`
- `2025-Wenzek-CC100-Mongolian dataset - NLP Database`
- `2025-onejune2018-Awesome-LLM-Eval Repository Meta-Resource`
- `2025-project-Kaku-Ora Zen Wisdom Diffused -- An`
- `2026-Unknown-Arabic LLMs for Banking Telecom and Government in GCC - 2026`

## Dashboard

v14 was rebuilt from the vault. It still holds 2,425 papers; 853 are now ethics-relevant (was 859).
- The six papers at 45 changed their ethics routing.
- The ALLaM note appears under its new name, so the index numbers of the papers sorted after it
  shifted.
- Hui's last author and the 8 new abstracts are in the data.
- `index.html` quotes no count that changed.

## Noticed, not changed

- **`2024-Veitsman-…Multilingual Speech`: wrong author and year.**
  - Crossref (10.3390/app152412880) lists 8 authors: Aidana Karibayeva, Vladislav Karyukin, Ualsher
    Tukeyev, Balzhan Abduali, Dina Amirova, Diana Rakhimova, Rashid Aliyev and Assem Shormakova.
  - It was published 2025-12-05. The note says Yana Veitsman, 2024.
  - Fixing it needs a rename and author profiles.
- **Likely duplicate pairs:**
  - `2025-Xiong-BuddhismEval A Bilingual Benchmark for Buddhist` and `2025-Xiong-BuddhismEval
    Bilingual Evaluation Benchmark for Buddhist`.
  - `2025-Ogunremi-1 Decolonizing NLP for “Low-resource Languages”` and `2023-StanfordMasakhane-
    Decolonizing NLP for 'Low-resource Languages' Applying Abebe`.

- 46 notes have frontmatter that `validate_all_papers.py` accepts but a strict YAML parser
  (PyYAML) rejects. One example is a LaTeX `\cdot` inside a double-quoted abstract in the Gölz
  note. All of them predate this change.
