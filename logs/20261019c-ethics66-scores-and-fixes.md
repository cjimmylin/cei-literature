# 20261019c — Ethics scores for 66 notes stuck at 0, two merges, field fixes and 19 renames (owner-approved)

**Owner decisions (2026-10-19):**
- "Apply all 66".
- Perspective label: "Social & Cultural Values".
- Follow-ups: "Merge 2 duplicates", "Fix 3 field errors" and "Rename 'Unknown' notes".
- The 8 works not about AI: "Keep them".

Single-line edits only (`paper_utils.batch_update_papers`); files moved or renamed with `git mv`.

## Applied

1. **Scores for the 66 notes** listed below:
   - `ethics_overall`, the five framework scores and `ethics_perspective`, exactly as proposed;
   - `ethics_perspective` is "Social & Cultural Values" for the 46 culture/religion notes;
   - the field was appended on 65 notes, which had none; JMedEthicBench already had the same value.
2. **Merged** (same rules as `logs/20261018-duplicate-merge.md`; retired notes in `RECYCLE-BIN/20261019-duplicate-merge/papers/`):
   - **Elmahjub, kept, absorbs `2023-Unknown-Artificial Intelligence AI in Islamic Ethics`** (CGSR0064). They share a DOI.
     - Carried: `DATE_ADDED` 20260403, `type: journalArticle`, `cultural_gap_category: Islamic`.
     - Not carried: `author_country: CO`, which has no basis.
   - **`2025-Wu-The Staircase of Ethics Multi-step Moral Dilemmas`, kept, absorbs `2025-Unknown-Staircase Ethics Probing LLM Value Priorities`** (EXSR0686). It is the same EMNLP 2025 paper.
     - Carried: the full `short_title`.
     - Corrected from Wu's own extract:
       - `deontological_ethics` 50 → 15 and `utilitarian_ethics` 50 → 20. The paper builds on Moral Foundations and Schwartz values; "utilitarian" appears 2 times and "deontolog" once.
       - `ethics_perspective` General Ethics → Moral Reasoning & Psychology.
     - Its entry was removed from `DASHBOARDS/cei-dashboard-14/build/benchmark_survey_candidates.json` (1,073 → 1,072; 87 from the v14 review). `build/README.md` was updated.
3. **Field fixes:**
   - **`2025-Nayan-…`** (Hindu texts):
     - `religious_values` and `religious_values_list` Judaism → Hinduism;
     - `rv_judaism` 70 → 0 and `rv_hinduism` 0 → 70, a swap;
     - `nw_dharmic` is still 0.
   - **`2020-Hongladarom-The Ethics of AI and Robotics`:**
     - `short_title` gains the subtitle "A Buddhist Viewpoint";
     - `nw_buddhist` and `rv_buddhism` 0 → 50, the most common pair on notes tagged "Buddhist-specific";
     - `religious_values` / `religious_values_list: Buddhism` added.
   - **`2025-Unknown-Digital Ethics of AI in Saudi`:**
     - `nw_islamic_ethics` 0 → 50, matching its `rv_islam` 50;
     - its description says it integrates Islamic values.
4. **19 notes renamed** to their first author's surname as given in the note's own `authors` field. Each got a dated line under `## Notes`.

   | Old filename author part | New |
   |---|---|
   | 2022-Unknown-A biased emerging governance regime for | 2022-Palladino-… |
   | 2022-Unknown-Broadening AI Ethics Narratives An Indic | 2022-Divakaran-… |
   | 2022-Unknown-Confucius cyberpunk and Mr Science comparing | 2022-Fung-… |
   | 2022-Unknown-Ethics and diversity in artificial intelligence | 2022-Roche-… |
   | 2023-Unknown-Challenges of Integrating AI Ethics into | 2023-Onyejegbu-… |
   | 2023-Unknown-Machine ethics and African identities | 2023-Kohnert-… |
   | 2024-Unknown-A Middle Path for AI Ethics | 2024-Compson-… |
   | 2024-Unknown-Are certain African ethical values at | 2024-Segun-… |
   | 2024-Unknown-Confucian Role Ethics and Artificial Intelligence | 2024-Whitney-… |
   | 2025-Unknown-AI Ethics in Africa Balancing Innovation | 2025-Nweke-… |
   | 2025-Unknown-Bridging the AI Governance Gap Ethical | 2025-Durodola-… |
   | 2025-Unknown-Ethical Concerns and Institutional Policy Responses | 2025-Soko-… |
   | 2025-Unknown-Ethical Governance of AI in the | 2025-Monasterio Astobiza-… |
   | 2025-Unknown-Ethical and Social Concerns of Artificial | 2025-Checketts-… |
   | 2025-Unknown-Ethics of AI - A Philosophical | 2025-Jash-… |
   | 2025-Unknown-Hindu Responses to Artificial Intelligence Theological | 2025-Pallathadka-… |
   | 2025-Unknown-Structural bias and geographical imbalances in | 2025-Sun-… |
   | 2025-Unknown-The Guiding Role of Buddhist Thought | 2025-Yan-… |
   | 2025-ed-Ethical and Legal Dilemmas of Artificial | 2025-Gonzalez-… (matches the sibling `2025-Gonzalez-Ethical and Legal Dilemmas of National`) |

   - **References:** no author profile, note or dashboard input linked these files. Dated analysis files under `MORAL-PSYCH/`, `CULTURAL-GLOBAL/DATA/` and the v14 build provenance still name the old files, unchanged.
   - **Not renamed:**
     - `2021-Review-What Buddhism Can Do for AI`: its author is listed as "MIT Technology Review".
     - `2024-HK-Confucian Philosophy Revitalized in the Digital`: its author is listed as "Unknown (CityU HK)".
     - `2024-Unknown-Decolonizing AI ethics in Africas healthcare`: in "Mugalula Kalule Grancia" the surname is unclear.

## Checks and effect

- `validate_all_papers.py`: 2,425 / 2,425 valid.
- `validate_papers_enhanced.py` totals, `main` → this branch:
  - 92 → 91 papers with errors;
  - 47 → 46 with warnings;
  - "Missing document type" 20 → 19 (Elmahjub now has `type`);
  - no new issue.
- Dashboard v14 rebuilt:
  - papers: 2,427 → 2,425;
  - ethics-relevant: 795 → 859 (+66, minus the 2 retired duplicates);
  - candidates: 1,073 → 1,072;
  - deontological: 101 → 100; utilitarian: 106 → 105 (the Wu correction);
  - virtue, care and contractarian unchanged;
  - `index.html` text updated.

## Still open (from the review below)

- The Gonzalez / "ed" pair (book vs chapter?).
- The van Norren 2020 draft and 2022 version.
- The year checks (Santiago Declaration, Kohnert MPRA).
- The unreliable `author_country` values (CO etc.).
- `cultural_gap_category` on Palladino and Yastreb.
- `nw_dharmic` on the Nayan note.

---

# The approved review list (as sent to the owner)


**Which notes:** every note whose title contains "ethic" and whose six ethics scores (`ethics_overall` plus the five frameworks) are all 0. 62 of the 66 were added on 2026-04-03 by the cultural-gap search with placeholder zeros and were never scored; the v14 write-back fills only empty fields, so it skipped them. The Hongladarom book is one of them.

**How:** three reviewers each read 22 notes (title, the note's description or abstract, its body, and a PDF extract where one exists) and applied the rubric used for the 77 alignment papers. I checked the drafts for consistency and made two changes, listed under *Changes I made to the drafts*.

## Rubric

- `ethics_overall` (0–100; 50 or more = ethics-relevant): 85–100 centrally about ethics or values; 60–84 substantial ethical content mixed with policy or description; 40–59 borderline; 10–39 incidental; 0–9 none.
- Five framework scores (virtue, deontological, utilitarian, care, contractarian; 50 or more = grounded in that framework): scored conservatively. Non-Western traditions already have their own `nw_*` fields, so a Confucian, Buddhist, Islamic or Ubuntu paper does not score a Western framework unless the text names it.
- `ethics_perspective`: set because every note scores 50 or more and none reaches 50 on a framework.

## Summary

- **All 66 come out ethics-relevant** (60–95, median 83): 33 at 85–100, 33 at 60–84. The dashboard's ethics-relevant count would go from 795 to 861.
- **No framework reaches 50.** The highest are 35 (deontological: the Bhagavad Gita framework note and the Global South governance note) and 30 (virtue: Hongladarom, Confucian role ethics). Framework counts on the dashboard would not change.
- **Perspective:** 46 Social & Cultural Values, 14 Responsible AI, 2 Machine Ethics, 2 Moral Reasoning & Psychology, 1 Privacy & Surveillance, 1 AI Safety & Alignment.
- **Confidence: 48 low, 15 medium, 3 high.** The evidence is thin: 45 notes have only a one-line description, 16 a real abstract, 3 a PDF extract, 2 the title alone. The ethics-relevant call (50 or more) is safe for all 66; the exact numbers are not. Real abstracts (needs network access) would firm them up.
- *For reference:* the vault's keyword scorer would give 23 of the 66 a score of 50 or more (it scores mostly 20–50 on one-line descriptions).

## Changes I made to the drafts

1. **Perspective label.** The standard's list has no label for cultural or religious ethics, so the reviewers mostly chose Responsible AI. The vault itself files such papers under **Social & Cultural Values** (181 notes, the fourth most used label, e.g. the Perera and Gwagwa notes). I propose that label for the 46 notes whose title or description centres a culture, religion or region; the table shows the reviewer's standard-list choice in brackets. The alternative is to keep the standard-list labels.
2. **Same paper, same scores.** `2023-Unknown-Artificial Intelligence AI in Islamic Ethics` has the same DOI as `2023-Elmahjub-AI in Islamic Ethics Towards Pluralism` (10.1007/s13347-023-00668-x); both get the Elmahjub note's scores.

## Proposed scores

Frameworks column lists only non-zero scores. Confidence: H high, M medium, L low.

| Note | Ethics | Frameworks | Perspective | Conf. | Reason |
|---|---|---|---|---|---|
| `2005-Huffer-Governance Corruption and Ethics in the` | 65 | – | Social & Cultural Values *(Responsible AI)* | L | Pacific governance study on corruption and ethics in public life, not AI; ethics is a core theme, but the title alone shows no normative framework. |
| `2018-Asiones-Critical Review Eight HighlyRated Books Moral` | 82 | virtue 10 | Social & Cultural Values *(Moral Reasoning & Psychology)* | M | Reviews eight moral theology textbooks for an undergraduate ethics course using Rest's four-component model; centrally ethical but not about AI; no single framework foregrounded. |
| `2018-Geno-Governance Ethics and Leadership in Papua` | 70 | virtue 15 | Social & Cultural Values *(Responsible AI)* | L | Personal essay on ethical leadership in Papua New Guinea governance; leadership ethics is central but it is not about AI, and character/virtue framing is only implied. |
| `2020-Hongladarom-The Ethics of AI and Robotics` | 90 | virtue 30, utilitarian 15, care 15 | Machine Ethics | L | Book on AI and robotics ethics; recognised (from memory) as Hongladarom's Buddhist-viewpoint book stressing excellence and compassion, hence modest virtue/care/utilitarian; truncated abstract is generic. |
| `2020-Unknown-Arya Prajna Artificial Intelligence according to` | 85 | – | Social & Cultural Values *(Value Alignment)* | L | Web-magazine article (Part I) proposing AI grounded in Indian ethical values; clearly ethics-focused, but only a one-line description, so Western frameworks left at zero. |
| `2021-Lovo-Indigenous knowledge around the ethics of` | 85 | deontological 15, care 10, contractarian 10 | Social & Cultural Values *(Human Rights & Social Justice)* | M | Scoping review of Oceanian Indigenous knowledge on human research ethics, motivated by harms and injustices to Indigenous participants; centrally ethical but not about AI. |
| `2021-Review-What Buddhism Can Do for AI` | 85 | virtue 10, utilitarian 20 | Social & Cultural Values *(Responsible AI)* | L | Magazine op-ed applying Buddhist suffering-reduction and non-attachment to AI ethics; suffering reduction gives a slight consequentialist lean, no explicit Western framework. |
| `2022-Norren-The ethics of artificial intelligence UNESCO` | 90 | deontological 20, care 25 | Social & Cultural Values *(Responsible AI)* | M | Critiques UNESCO's AI ethics recommendation through Ubuntu's relational, communitarian ethics; the vault's 2020 draft extract shows relationality and rights/duties themes, not explicit Western frameworks. |
| `2022-Unknown-A biased emerging governance regime for` | 85 | – | Responsible AI | L | Critique of how AI ethics principles get skewed when turned into governance practice; core is ethical principles and governance, no named framework. |
| `2022-Unknown-Broadening AI Ethics Narratives An Indic` | 85 | care 15 | Social & Cultural Values *(Responsible AI)* | L | Draws on Indian art traditions to broaden AI ethics narratives; recalled (from memory) findings stress empathy and accountability, no explicit Western framework. |
| `2022-Unknown-Confucius cyberpunk and Mr Science comparing` | 90 | virtue 25, deontological 20 | Social & Cultural Values *(Responsible AI)* | L | Compares Chinese and EU AI ethics principles and their Confucian/European philosophical roots; recognised paper (from memory), only a one-line note here, so framework scores kept modest. |
| `2022-Unknown-Ethics and diversity in artificial intelligence` | 80 | – | Responsible AI | L | Review of ethics and diversity/inclusion across national AI policies and strategies; ethics-centred policy analysis, no named framework. |
| `2023-Elmahjub-AI in Islamic Ethics Towards Pluralism` | 95 | deontological 15, utilitarian 25 | Social & Cultural Values *(Responsible AI)* | M | Islamic-ethics framework for pluralist AI norm-setting; maslaha (public welfare) gives a consequence-oriented lean and textual sources a slight duty lean, neither explicit Western theory. |
| `2023-Unknown-Artificial Intelligence AI in Islamic Ethics` | 95 | deontological 15, utilitarian 25 | Social & Cultural Values *(Responsible AI)* | M | Islamic-ethics framework for pluralist AI norm-setting; the duplicate note's full abstract centres maslaha (public interest) as normative guide, a weak consequentialist signal only. Scores set equal to the Elmahjub note (same DOI). |
| `2023-Unknown-Challenges of Integrating AI Ethics into` | 75 | – | Social & Cultural Values *(Responsible AI)* | L | Book chapter on obstacles to teaching AI ethics in Nigerian university curricula; ethics is the subject but treated educationally and descriptively, no framework indicated. |
| `2023-Unknown-Machine ethics and African identities` | 85 | – | Social & Cultural Values *(Machine Ethics)* | L | Working paper on machine ethics viewed through African identities; ethics central per title, but the one-line description shows no Western framework. |
| `2024-ASEAN-ASEAN Guide on AI Governance and` | 70 | – | Responsible AI | L | Intergovernmental voluntary guide on AI governance and ethics principles (recognised document); governance-heavy with an explicit ethics-principles component, no ethical-theory grounding. |
| `2024-Chile-Santiago Declaration for Ethical Artificial Intelligence` | 85 | – | Responsible AI | L | Regional ministerial declaration of ethical AI principles for Latin America and the Caribbean; core is ethics principles. From memory it was adopted October 2023, not 2024. |
| `2024-Gilbert-The Convergence of Artificial Intelligence and` | 75 | – | Privacy & Surveillance | M | Article on AI and privacy stressing ethical implications of data use; ethics substantive but mixed with innovation and policy discussion, no named framework. |
| `2024-HK-Confucian Philosophy Revitalized in the Digital` | 85 | virtue 20, care 15 | Social & Cultural Values *(Value Alignment)* | L | Applies Confucian interpersonal ethics to relationships with AI; clearly ethical, but the one-line description gives no explicit virtue or care-ethics grounding, so both kept low. |
| `2024-Institute-Perspectives and Approaches in AI Ethics` | 80 | – | Responsible AI | L | Montreal AI Ethics Institute web summary (from memory, of Danit Gal's 2020 chapter) of Chinese, Japanese and Korean AI ethics approaches; descriptive, no framework. |
| `2024-Unknown-A Middle Path for AI Ethics` | 85 | virtue 10 | Social & Cultural Values *(Responsible AI)* | L | Buddhist scholars apply the Middle Path to AI ethics; centrally ethical, but the description shows no explicit virtue, duty or consequence grounding (small nod to moderation). |
| `2024-Unknown-Are certain African ethical values at` | 88 | deontological 15, care 10 | Social & Cultural Values *(Human Rights & Social Justice)* | L | Argues corporate AI threatens Afro-communitarian values and human dignity; centrally ethical, but only a one-line description, so dignity/relational themes are not mapped to Western frameworks. |
| `2024-Unknown-Confucian Role Ethics and Artificial Intelligence` | 90 | virtue 30, care 20 | Social & Cultural Values *(Machine Ethics)* | L | Applies Confucian role ethics (ren, yi, xiao) to AI; centrally normative, but role ethics is relational rather than explicitly virtue or care ethics. |
| `2024-Unknown-Decolonizing AI ethics in Africas healthcare` | 88 | – | Social & Cultural Values *(Human Rights & Social Justice)* | L | AI and Ethics article arguing for decolonised AI ethics in African healthcare; centrally ethical and justice-oriented, no explicit Western framework in the one-line description. |
| `2024-Unknown-Decolonizing the Ethics of Artificial Intelligence` | 88 | – | Social & Cultural Values *(Human Rights & Social Justice)* | L | Decolonial critique of AI ethics drawing on Buddhist and Indigenous perspectives; centrally ethical, but the one-line description shows no explicit Western framework grounding. |
| `2024-Yende-Dharma and Design ethical considerations for` | 80 | virtue 10, deontological 25 | Social & Cultural Values *(Responsible AI)* | L | Medium blog post drawing on Hindu principles (dharma, ahimsa) for AI design ethics; centrally ethical, and dharma-as-duty hints at deontology without making it explicit. |
| `2025-ASEAN-Expanded ASEAN Guide on AI Governance` | 70 | – | Responsible AI | L | Intergovernmental ASEAN guide extending AI governance and ethics principles to generative AI; ethics component substantive but mixed with governance recommendations. |
| `2025-Aithal-Arjunas Dilemma as Universal Paradigm MultiFramework` | 75 | deontological 15, utilitarian 10 | Social & Cultural Values *(Moral Reasoning & Psychology)* | M | Analyses Arjuna's ethical crisis in Bhagavad Gita chapter 1 with SWOC/ABCD business frameworks; ethical but not about AI; 'multi-framework' means analytical, not ethical-theory, frameworks. |
| `2025-Aithal-Cosmic Blueprint Ethical Action MultiDimensional Analysis` | 65 | virtue 15, deontological 20 | Social & Cultural Values *(Moral Reasoning & Psychology)* | M | Analysis of Bhagavad Gita chapter 4 (knowledge, action, renunciation) for modern ethical and spiritual living; ethical but partly spiritual, no AI, no explicit Western framework. |
| `2025-Aithal-Democratization Divine Critical Analysis Inclusivity Grace` | 70 | – | Social & Cultural Values *(Human Rights & Social Justice)* | M | Theological-ethical analysis of Bhagavad Gita chapter nine's grace and radical inclusivity as a social ethic; not about AI, no Western framework invoked. |
| `2025-Du-LLMs Ethical Dilemma Analyzers` | 85 | – | Moral Reasoning & Psychology | H | Benchmark of 196 research-ethics dilemmas comparing four LLMs' and laypeople's analyses against expert opinions; centrally moral-reasoning evaluation; extract never names a normative framework. |
| `2025-Fong-From Paper to Practice Utilizing the` | 65 | – | Responsible AI | L | ISEAS policy paper on implementing the ASEAN Guide on AI Governance and Ethics; governance and policy focus with an ethics-principles component. |
| `2025-Gonzalez-Ethical and Legal Dilemmas of National` | 70 | – | Responsible AI | L | Analysis of ethical and legal dilemmas in Latin American national AI policies; ethics mixed with law and policy, no framework evident from the one-line description. |
| `2025-HAI-Moving Beyond the Term Global South` | 60 | – | Social & Cultural Values *(Human Rights & Social Justice)* | L | Stanford HAI policy web piece critiquing the 'Global South' label in AI ethics and policy; ethics is the domain, but content is mainly terminology and representation. |
| `2025-ILO-Governing AI in the World of` | 75 | – | Responsible AI | L | ILO review of global AI ethics guidelines as they apply to work and workers; ethics principles are the object, seen through labour governance. |
| `2025-Institute-Navigating AI Governance and Ethics Across` | 62 | – | Responsible AI | L | Think-tank web article comparing AI governance and ethics approaches across ASEAN states; mainly policy-descriptive with an ethics component. |
| `2025-Krishnamoorthy-Beyond Western Frameworks Why AI Ethics` | 85 | – | Social & Cultural Values *(Value Alignment)* | L | Medium blog post arguing Dharmic ethics should complement Western AI ethics frameworks; centrally ethical, but no text shows which Western frameworks are engaged. |
| `2025-Kumara-Ethically Charged Machines Rethinking Artificial Intelligence` | 75 | – | Social & Cultural Values *(Machine Ethics)* | L | Philosophical rethinking of machines' ethical status (with consciousness and free will) through Tiantai Buddhism and new materialism; abstract truncated, no Western framework visible. |
| `2025-Nayan-Automatic Extraction Summarization Ethical Dilemmas from` | 75 | – | Social & Cultural Values *(Moral Reasoning & Psychology)* | M | NLP pipeline that extracts and summarises moral dilemmas from Hindu religious texts; ethics is the object of study but the contribution is technical; no framework invoked. |
| `2025-ORourke-The Pacific Way advancing ethical research` | 72 | – | Social & Cultural Values *(Human Rights & Social Justice)* | M | Research-ethics governance in Pacific island countries, countering limited local capacity and external influence; an ethics-governance topic, not about AI; truncated abstract shows no framework. |
| `2025-Polok-AI Governance in Saudi Arabia Cultural` | 65 | – | Social & Cultural Values *(Responsible AI)* | M | Country survey of Saudi Arabia's AI governance, regulation and ethical frameworks, set against cultural values and compared internationally; ethics is one strand of a policy survey. |
| `2025-Sharma-Bridging Tradition and Technology Ethical Artificial` | 75 | – | Social & Cultural Values *(Human Rights & Social Justice)* | M | Ethical AI and the preservation of indigenous knowledge in Fiji and the Pacific; ethics substantive alongside cultural-heritage and technology issues, no named framework. |
| `2025-Unknown-AI Ethics in Africa Balancing Innovation` | 80 | – | Social & Cultural Values *(Responsible AI)* | L | Discusses balancing AI innovation with African cultural and social values; ethics-focused with policy/innovation framing; only a one-line description, no framework evident. |
| `2025-Unknown-Artificial Intelligence in Fatwa and Islamic` | 65 | deontological 15 | Social & Cultural Values *(Responsible AI)* | L | Conference paper on AI in fatwa issuance and Islamic law covering prospects, regulation and ethics; ethics is one of three themes, no explicit framework. |
| `2025-Unknown-Bridging the AI Governance Gap Ethical` | 68 | – | Responsible AI | L | Conference paper on the ethical and regulatory gap for generative AI in Nigeria; ethics paired with regulation and governance, no framework evident. |
| `2025-Unknown-Digital Ethics of AI in Saudi` | 85 | – | Social & Cultural Values *(Responsible AI)* | L | Examines AI digital ethics in Saudi Arabia and the UAE, integrating Islamic values; ethics-centred in a national-policy context; one-line description shows no explicit framework. |
| `2025-Unknown-Ethical Concerns and Institutional Policy Responses` | 75 | – | Social & Cultural Values *(Responsible AI)* | L | Study of ethical concerns about AI in Sub-Saharan African universities and institutional policy responses; ethics central alongside policy description, no framework indicated. |
| `2025-Unknown-Ethical Governance of AI in the` | 85 | deontological 35 | Social & Cultural Values *(Human Rights & Social Justice)* | L | Proceedings paper proposing a human-rights approach to ethical AI governance in the Global South; rights framing gives a moderate deontological score, not explicit Kantian theory. |
| `2025-Unknown-Ethical and Social Concerns of Artificial` | 80 | – | Responsible AI | L | Multi-author NanoEthics article on AI's ethical and social concerns across Asian societies; ethics substantive but mixed with social description; only a one-line description available. |
| `2025-Unknown-Ethical challenges for using AI in` | 85 | deontological 15 | Social & Cultural Values *(Responsible AI)* | L | Discusses ethical challenges of applying AI to understanding Islamic jurisprudence; centrally ethical, and Islamic legal obligations are not explicitly framed as deontology. |
| `2025-Unknown-Ethics of AI - A Philosophical` | 85 | – | Machine Ethics | L | Philosophical inquiry into AI ethics drawing on karma and Indian philosophy; centrally ethical, but no Western framework is evident from the one-line description. |
| `2025-Unknown-Ethics of AI in Maqasid Al-Sharias` | 90 | deontological 15, utilitarian 10 | Social & Cultural Values *(Value Alignment)* | L | Evaluates AI ethics through the five objectives (maqasid) of Sharia; centrally ethical; duty and welfare readings possible but not explicit, so deontological and utilitarian kept low. |
| `2025-Unknown-Ethics of the Use of AI` | 85 | deontological 20 | Social & Cultural Values *(Responsible AI)* | L | Examines AI ethics through the paradigm of Islamic law; centrally normative, and legal duties are likely involved but not shown as explicit deontology. |
| `2025-Unknown-Hindu Responses to Artificial Intelligence Theological` | 72 | – | Social & Cultural Values *(Machine Ethics)* | L | Hindu theological and ethical responses to AI centred on Advaita Vedanta and machine consciousness; ethics mixed with theology and metaphysics, no Western framework. |
| `2025-Unknown-Integrating Mahabharatas Ethical Principles into Artificial` | 88 | deontological 25 | Social & Cultural Values *(Value Alignment)* | L | Proposes integrating Mahabharata principles (dharma, karma, nishkama karma) into AI; duty-centred concepts give a moderate deontological signal, but deontology is not explicit. |
| `2025-Unknown-Social and Ethical Considerations of AI` | 80 | virtue 20 | Social & Cultural Values *(Responsible AI)* | L | Springer edited volume of Confucian, Daoist and Christian reflections on AI's social and ethical issues in East Asia; ethics-centred, no explicit Western framework. |
| `2025-Unknown-Staircase Ethics Probing LLM Value Priorities` | 92 | deontological 15, utilitarian 20 | Moral Reasoning & Psychology | H | EMNLP benchmark of LLM value priorities over 3,302 multi-step moral dilemmas; grounded in Moral Foundations and Schwartz values, utilitarian/deontological only mentioned (duplicate's vault extract). |
| `2025-Unknown-Structural bias and geographical imbalances in` | 70 | – | Social & Cultural Values *(Human Rights & Social Justice)* | L | Examines geographic imbalances and structural bias in AI ethics research, especially Africa's marginalisation; a justice concern about the field rather than a normative framework. |
| `2025-Unknown-The Ethical Framework Of Bhagavad Gita` | 85 | virtue 15, deontological 35 | Social & Cultural Values *(Machine Ethics)* | L | Applies the Bhagavad Gita's ethics of nishkama karma (desireless, duty-bound action) to AI systems; centrally normative, and the duty theme suggests deontology but not explicitly. |
| `2025-Unknown-The Guiding Role of Buddhist Thought` | 88 | – | Social & Cultural Values *(Responsible AI)* | L | Article proposing Buddhist ethical principles as guidance for AI ethics and development; centrally ethical, no explicit Western framework in the one-line description. |
| `2025-Yastreb-Methodological foundations of a critical approach` | 85 | – | Responsible AI | M | Philosophical article on methodological foundations of a critical approach to AI's ethical problems; centrally about ethics; truncated abstract names no virtue, deontological or other framework. |
| `2025-Younas-Toward a Cultural Co-Genesis of AI` | 90 | – | Social & Cultural Values *(Responsible AI)* | L | arXiv paper proposing 'cultural co-genesis' as a cross-tradition framework for AI ethics; centrally normative and cross-cultural, no single Western framework. |
| `2025-ed-Ethical and Legal Dilemmas of Artificial` | 75 | – | Responsible AI | L | Edited Springer book on ethical and legal AI controversies in Latin America's public sphere; ethics substantive but mixed with law and policy, no framework evident. |
| `2026-Liu-Between No-Self and the Algorithm Buddhist` | 85 | virtue 25 | Social & Cultural Values *(Value Alignment)* | M | Uses Buddhist mind-nature theory to frame ethical AI design supporting human awakening and self-realization; flourishing theme gives a weak virtue signal; Buddhism already in nw_buddhist. |
| `2026-Liu-JMedEthicBench` | 75 | deontological 15 | AI Safety & Alignment | H | Japanese multi-turn jailbreak benchmark testing whether LLMs refuse requests that violate 67 Japan Medical Association ethics guidelines; harm-focused technical safety evaluation, no framework. |

## Found while scoring (not changed)

**Not about AI (8).** Scored on their ethics content; whether they belong in an AI-ethics vault is your call:
- `2005-Huffer-Governance Corruption and Ethics in the`
- `2025-Aithal-Democratization Divine Critical Analysis Inclusivity Grace`
- `2018-Asiones-Critical Review Eight HighlyRated Books Moral`
- `2025-Aithal-Arjunas Dilemma as Universal Paradigm MultiFramework`
- `2025-ORourke-The Pacific Way advancing ethical research`
- `2018-Geno-Governance Ethics and Leadership in Papua`
- `2021-Lovo-Indigenous knowledge around the ethics of`
- `2025-Aithal-Cosmic Blueprint Ethical Action MultiDimensional Analysis`

**Not papers (7)** — web pages, blog posts or magazine pieces:
- `2021-Review-What Buddhism Can Do for AI`
- `2025-Institute-Navigating AI Governance and Ethics Across`
- `2020-Unknown-Arya Prajna Artificial Intelligence according to`
- `2025-HAI-Moving Beyond the Term Global South`
- `2025-Krishnamoorthy-Beyond Western Frameworks Why AI Ethics`
- `2024-Institute-Perspectives and Approaches in AI Ethics`
- `2024-Yende-Dharma and Design ethical considerations for`

**Duplicates and versions (4):**
- `2023-Unknown-Artificial Intelligence AI in Islamic Ethics` = `2023-Elmahjub-AI in Islamic Ethics Towards Pluralism` (same DOI). Merge candidate.
- `2025-Unknown-Staircase Ethics Probing LLM Value Priorities` = `2025-Wu-The Staircase of Ethics Multi-step Moral Dilemmas` (arXiv 2505.18154). The Wu note already has deontological 50 / utilitarian 50 / General Ethics; its extract grounds the paper in Moral Foundations and Schwartz values, so the reviewer proposed 20 / 15 here. Merge candidate; the two notes should agree.
- `2025-Gonzalez-Ethical and Legal Dilemmas of National` and `2025-ed-Ethical and Legal Dilemmas of Artificial`: same editor, year and near-identical title; possibly a chapter of the book. Needs a check.
- `2022-Norren-The ethics of artificial intelligence UNESCO` and `2020-van Norren-DRAFT-WORKING PAPER AFRICA KNOWS CONFERENCE 2020`: the 2020 note is the conference draft of the same work. A version, not a duplicate.

**Filename author wrong (24).** Mostly "Unknown", "HK", "Review" or "ed" in the filename while the `authors` field names the real author. Renaming needs the same care as today's two renames:
`2021-Review-What Buddhism Can Do for AI`, `2022-Unknown-Broadening AI Ethics Narratives An Indic`, `2023-Unknown-Machine ethics and African identities`, `2024-Unknown-A Middle Path for AI Ethics`, `2024-Unknown-Decolonizing AI ethics in Africas healthcare`, `2025-Unknown-Bridging the AI Governance Gap Ethical`, `2025-Unknown-Ethical Governance of AI in the`, `2025-Unknown-Ethics of AI - A Philosophical`, `2025-Unknown-Hindu Responses to Artificial Intelligence Theological`, `2025-Unknown-Staircase Ethics Probing LLM Value Priorities`, `2025-Unknown-The Guiding Role of Buddhist Thought`, `2025-ed-Ethical and Legal Dilemmas of Artificial`, `2022-Unknown-Confucius cyberpunk and Mr Science comparing`, `2023-Unknown-Artificial Intelligence AI in Islamic Ethics`, `2024-HK-Confucian Philosophy Revitalized in the Digital`, `2024-Unknown-Are certain African ethical values at`, `2025-Unknown-AI Ethics in Africa Balancing Innovation`, `2025-Unknown-Ethical and Social Concerns of Artificial`, `2025-Unknown-Structural bias and geographical imbalances in`, `2022-Unknown-A biased emerging governance regime for`, `2022-Unknown-Ethics and diversity in artificial intelligence`, `2023-Unknown-Challenges of Integrating AI Ethics into`, `2024-Unknown-Confucian Role Ethics and Artificial Intelligence`, `2025-Unknown-Ethical Concerns and Institutional Policy Responses`

**Year may be wrong (2):** `2024-Chile-Santiago Declaration for Ethical Artificial Intelligence` (reviewer recalls October 2023; not confirmed in the vault); `2023-Unknown-Machine ethics and African identities` (MPRA 113799 looks like 2022; the URL is revision 7).

**Other field problems:**
- `2025-Nayan-…`: `religious_values_list: Judaism`, but the paper is about ancient Indian (Hindu) texts.
- `2020-Hongladarom-The Ethics of AI and Robotics`: tagged "Buddhist-specific AI ethics" but `nw_buddhist: 0`; the subtitle (*A Buddhist Viewpoint*) is missing.
- `2025-Unknown-Digital Ethics of AI in Saudi`: `nw_islamic_ethics: 0` although its description says it integrates Islamic values.
- `author_country` is unreliable across this set: CO (Colombia) on several notes with no Colombian link (e.g. Palladino), CN for Aithal (India), KR for Krishnamoorthy.
- `cultural_gap_category` looks wrong on Palladino ("Eastern European/Central Asian") and Yastreb ("Pacific Island").
