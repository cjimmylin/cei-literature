# Dashboard v7 — Religious Studies Communication Plan

**Author:** Religious Studies Scholar (council role)
**Date:** 2026-04-13
**Scope:** Communication guidance for the 14-tradition panel, void-factor framing, Islam dominance,
T2 fara'id instrument, romanization, and WEIRD-bias sensitivity.
**Encoding:** Latin-1 only. No native scripts. ASCII apostrophes throughout.

---

## 1. Introducing the 14 Traditions to a General Audience

The dashboard reaches audiences who may have no prior exposure to comparative religion. Each
tradition needs a single orienting sentence — enough to understand what kind of intellectual and
moral system it represents, without caricature or reductive shorthand.

### Recommended one-sentence descriptions (display text)

| Tradition | Status | Orienting sentence |
|-----------|--------|--------------------|
| Islam | STRONG | A monotheistic tradition originating in 7th-century Arabia, organized around the Quran and the Sunna of the Prophet Muhammad, with a rich jurisprudential tradition (fiqh) governing ethics, law, and worship for roughly 1.9 billion adherents worldwide. |
| Christianity | MODERATE | A monotheistic tradition centered on the life and teachings of Jesus of Nazareth, encompassing Catholic, Orthodox, and Protestant denominations with distinct moral theologies spanning natural law, covenant ethics, and liberation theology. |
| Hinduism | MODERATE | A family of South Asian religious traditions with roots in the Vedic corpus, organized around concepts of dharma (moral duty), karma (action and consequence), and moksha (liberation), with six classical philosophical schools and numerous living ethical traditions. |
| Buddhism | MODERATE | A tradition originating with Siddhartha Gautama in the 5th century BCE, organized around the Four Noble Truths and the Eightfold Path, encompassing Theravada, Mahayana, and Vajrayana lineages with distinct ethical frameworks. |
| Sikhism | WEAK | A monotheistic tradition founded in 15th-century Punjab by Guru Nanak, centered on the Guru Granth Sahib and the ethical triad of seva (selfless service), kirat karni (honest livelihood), and vand chakna (sharing with others). |
| Confucianism | WEAK | A Chinese philosophical tradition rooted in the teachings of Kongzi (Confucius, 551-479 BCE), organized around ren (benevolence), li (ritual propriety), yi (righteousness), and the ideal of the junzi — the morally exemplary person. |
| Judaism | CRITICAL GAP | A monotheistic tradition with origins in the Hebrew Bible and a 2,000-year tradition of Talmudic interpretation, halakhic (legal-ethical) reasoning, and multi-voice argumentation (machloket) that remains one of the most computationally rich textual traditions in existence. |
| Jainism | CRITICAL GAP | An ancient Indian tradition organized around ahimsa (non-violence), anekantavada (the many-sidedness of reality), and aparigraha (non-possessiveness), with a rigorous ethics of non-harm that extends to all living beings. |
| Taoism | VOID | A Chinese tradition rooted in the Daodejing and the concept of dao (the Way), emphasizing wu wei (non-coercive action) and ziran (naturalness) as guides to ethical life and governance. |
| Shinto | VOID | Japan's indigenous religious tradition, organized around kami (sacred spirits or presences) and values of wa (harmony), purity, and reverence transmitted through ritual and site-specific practice rather than a fixed scriptural canon. |
| Ubuntu Philosophy | VOID | An African philosophical tradition, particularly prominent in Southern and East Africa, organized around the relational principle "I am because we are" — an ethical framework that grounds personhood, moral obligation, and justice in community rather than individual autonomy. |
| Indigenous Spirituality | VOID | An umbrella label for hundreds of distinct Indigenous religious and ethical traditions across every inhabited continent, transmitted through oral tradition, ceremony, and land-based practice, with moral frameworks grounded in intergenerational kinship and ecological relationships. |
| Baha'i | VOID | A monotheistic tradition founded in 19th-century Persia, emphasizing the unity of all religions and humanity, progressive revelation, and principles of global justice, gender equality, and world citizenship. |
| Zoroastrianism | VOID | One of the world's oldest monotheistic traditions, originating in ancient Persia with the prophet Zarathustra, organized around the ethical triad of humata, hukhta, hvarshta (good thoughts, good words, good deeds) and the principle of asha (truth/righteousness). |

### Display conventions

- Use the tradition name as the primary label; add the family tag (Abrahamic, Dharmic, East Asian,
  African/Indigenous, Other) as secondary metadata.
- Status badges: STRONG (green), MODERATE (blue), WEAK (amber), CRITICAL GAP (orange), VOID (gray).
- VOID is a data-infrastructure classification, not an evaluative judgment. See Section 2.

---

## 2. Explaining "Void Factors" — Traditions with Zero Viable Benchmarks

### The core communication problem

Eight of 14 traditions have zero gate-passing benchmarks. The risk is that a general audience reads
this as: "these traditions have not produced valuable moral thought" or "these traditions are less
important to evaluate." Both readings are false and potentially harmful.

### Recommended framing

The VOID and CRITICAL GAP statuses describe a deficit in *evaluation infrastructure*, not in
theological richness, ethical sophistication, or real-world importance. The correct causal chain is:

  Benchmark creation requires a specific pipeline:
  peer-reviewed paper -> annotated public dataset -> GitHub repository
  -> HuggingFace upload -> evaluation harness.

  Some traditions have communities that have built this pipeline.
  Most have not — not because their ethics are simpler,
  but because the pipeline itself has prerequisites (textual canon, public data licensing,
  English-language venue access) that structurally advantage certain knowledge systems.

### Display language to use

Use this or close paraphrase in tooltip/annotation text:

> "VOID means no publicly available benchmark exists — not that this tradition lacks ethical depth.
> Judaism, for example, has one of the world's oldest computational humanities projects and a vast
> digital corpus (Sefaria), yet produces zero gate-passing benchmarks because its scholarly community
> and the NLP evaluation community have not yet built the shared infrastructure to connect them."

> "For oral and practice-based traditions such as Indigenous Spirituality and Ubuntu Philosophy, the
> absence of public benchmarks may reflect community decisions about epistemic sovereignty — the right
> of a community to govern who accesses its sacred knowledge — rather than any gap in the tradition's
> moral reasoning."

### Two distinct void types — communicate them separately

The dashboard should distinguish these two situations visually or via separate annotation:

**Type A — Community coordination gap** (Judaism, Confucianism, Taoism, Jainism):
Resources exist; the pipeline bridge has not been built. Addressable through institutional investment
in shared-task infrastructure. Estimated timeline: 2-3 years with sustained effort.

**Type B — Structural epistemic exclusion** (Indigenous Spirituality, Ubuntu Philosophy, Shinto,
Baha'i):
The pipeline design itself excludes oral, communal, and practice-based knowledge systems. Requires
fundamentally different evaluation architectures — community-governed protocols, narrative-based
assessment, participatory methods — not incremental expansion of the existing benchmark pipeline.

### What NOT to say

- Do not use "underrepresented" as a synonym for VOID — it implies merely quantitative shortfall.
- Do not say traditions are "hard to benchmark" — this implies a deficiency in the tradition.
- Do not imply that adding more benchmarks will resolve Type B gaps — this misrepresents the
  structural problem as a resource problem.

---

## 3. Presenting the Islam Dominance Finding

### The finding

Islam accounts for 28 of 47 gate-passing benchmarks (59.6%) and 9 of 12 Tier 1 benchmarks —
far exceeding its 28.2% share of candidates and far exceeding any uniform expectation across 14
traditions (chi-squared = 64.96, Cramer's V = 0.53, p < 0.001).

### Why this is a structural artifact, not a normative claim

The dominance reflects three reinforcing infrastructure factors, none of which is theological:

1. **The Quranic QA shared-task pipeline**: A self-sustaining community (active since 2019) that
   converts theological text into annotated datasets and published benchmarks. Each iteration lowers
   barriers for the next. No comparable pipeline exists for any other tradition.

2. **Arabic NLP investment**: Gulf state national AI strategies (UAE, Saudi Arabia, Qatar) have
   funded pre-trained language models, tokenizers, and evaluation frameworks for Arabic — the
   substrate on which Islamic benchmarks build. Hebrew, Sanskrit, Pali, Classical Chinese, and
   Gurmukhi have no equivalent investment at scale.

3. **Partial formalizability**: Specific subdomains of Islamic jurisprudence (fiqh) — particularly
   inheritance calculation (ilm al-mawarith) and commercial transaction rules — have explicit
   numerical rules that map onto multiple-choice formats. This formalizability applies only to
   specific applied legal subdomains, not to Islamic jurisprudence as a whole; methods such as
   qiyas (analogical reasoning) and ijtihad (independent legal reasoning) resist benchmark
   construction just as much as reasoning in other traditions.

### Recommended display framing

Primary label in the chart or callout:

> "Islam's benchmark dominance is structural, not theological."

Supporting annotation:

> "28 of 47 gate-passing benchmarks cover Islamic content — not because Islamic ethics are more
> important or more amenable to evaluation, but because the Arabic NLP research community and
> Quranic QA shared-task infrastructure have invested in exactly the pipeline that benchmark
> creation requires. The same investment, directed at other traditions, would likely produce
> comparable benchmark density."

### What NOT to say

- Do not say Islam is "easier to benchmark" without immediately clarifying that this applies only
  to specific formalizable subdomains (inheritance law, commercial rules), not to Islamic moral
  reasoning as a whole.
- Do not frame the statistic as evidence of Islamic AI dominance, Islamic influence on AI, or any
  normative claim about Islam's relationship to AI systems.
- Do not imply that other traditions are disadvantaged by Islamic benchmark production — the
  mechanism is infrastructure investment, not competition.

### The WEIRD reversal — handle carefully

C6 finding: non-WEIRD traditions pass gates at 14.4% vs WEIRD traditions at 8.9% — the opposite
of the expected direction. This reversal is driven entirely by Islamic benchmark dominance (28 of
30 non-WEIRD gate-passers are Islamic). The WEIRD/non-WEIRD dichotomy is too coarse to capture
infrastructure-specific dynamics.

Display language:

> "The expected WEIRD bias is reversed in the data — but this is driven by a single factor:
> Islamic benchmark infrastructure. The reversal does not mean non-Western traditions are
> advantaged; it means Islamic infrastructure investment is so concentrated that it overwhelms
> the population-level pattern. The 8-tradition void remains hidden beneath this surface reversal."

---

## 4. Handling T2 — The Fara'id Discriminative Test

### What fara'id is

Fara'id (from Arabic: fara'id, meaning "obligatory shares") is the Islamic law of inheritance —
the legal-theological system that governs the distribution of a deceased Muslim's estate among
heirs. Its rules are derived directly from Quranic verses (Surah 4:11-12, 4:176) and have been
developed over centuries by Islamic jurists into a precise calculus involving fractional shares,
heir categories, and residuaries.

Fara'id is governed by a subdiscipline of Islamic jurisprudence called ilm al-mawarith (the science
of inheritance shares). It requires multi-step numerical calculation: identifying heirs, assigning
Quranic fractional shares, handling cases where shares sum to more than the estate (awl, return
process), and applying blocking rules (hajb) where one heir excludes another from inheritance.

### Why it was chosen as the discriminative test

The T2 instrument is a 30-item Arabic multiple-choice quiz covering fara'id at Beginner and Advanced
difficulty levels. It was selected for three reasons that distinguish it from all other benchmarks
in the trial battery:

1. **Genuine discriminative power**: T2 spans from 6.7% (Gemini Pro) to 100% (Opus, Sonnet,
   Codex) — a 93.3-percentage-point spread. Every other instrument in the trial battery exhibits
   rubric ceiling effects that compress scores into pass/fail bands, eliminating discrimination
   between models. T2 is the only instrument where model capability produces meaningfully
   different outcomes.

2. **Verifiable correct answers**: Fara'id problems have mathematically deterministic solutions.
   The Quranic rules are explicit, the juristic rules for edge cases are codified in classical
   legal manuals, and the arithmetic is unambiguous. This means T2 items can be scored without
   rubric subjectivity — a binary correct/incorrect determination that is not possible for most
   values reasoning items.

3. **Arabic language requirement**: The advanced items require genuine facility with Arabic
   technical legal vocabulary — terms such as asaba (residuary heirs), dhul-arham (distant
   kindred), and the fractional terminology of Quranic verse — not mere English-language
   familiarity with Islamic content. This linguistic requirement provides additional discrimination
   between models trained on Arabic text at different depths.

### What the T2 results show

Haiku achieves 76.7% overall (80% beginner, 73.3% advanced), revealing a capability gradient
within the Claude family that the rubric scores mask entirely (all three Claude models score
0.93-1.0 on rubric dimensions). This internal discrimination confirms that T2 has meaningful
difficulty parameters — it is not merely a pass/fail gate but a scale that reveals relative
capability.

The Gemini family produces the most striking results: 6.7% to 20% across four models. This
near-floor performance, combined with 0.57-1.0 on Bias detection, suggests differential capability
profiles — competent at meta-level bias recognition, struggling with object-level theological
reasoning in Arabic — but interpretation is constrained by methodological caveats (see CAV-3).

### Dashboard display guidance

- Label the instrument as: "T2: Islamic Inheritance Law (fara'id) — 30-item Arabic MCQ"
- Include a tooltip explaining: what fara'id is, why it was chosen (discriminative power,
  verifiable answers, Arabic requirement), and the blinding caveat (CAV-1: original Claude trials
  had gold labels visible — scores are upper-bound estimates).
- Display model scores as a horizontal bar chart ranked by T2 accuracy, with Haiku's within-family
  divergence highlighted.
- State explicitly that T2 is one instrument covering one tradition's legal subdomain — not a
  comprehensive measure of Islamic values reasoning, and not a comparison across traditions.

---

## 5. Romanization Conventions

All religious and philosophical terms appear in romanized form only. No native scripts (Arabic,
Hebrew, Devanagari, Chinese characters, Gurmukhi, etc.) anywhere in the dashboard. ASCII
apostrophes only (straight single quote: ') for all special characters.

### Canonical romanizations for key terms

| Term | Canonical romanization | Tradition | Gloss |
|------|----------------------|-----------|-------|
| Islamic inheritance law | fara'id | Islam | "obligatory shares" — the Quranic inheritance system |
| Islamic law (general) | shari'a | Islam | lit. "the way to the water source"; the totality of Islamic legal-ethical norms |
| Moral duty / cosmic order | dharma | Hinduism/Buddhism | context-dependent; in Hinduism, one's righteous duty; in Buddhism, the teaching |
| Jewish legal-ethical tradition | halakha | Judaism | lit. "the way of walking"; the body of Jewish law derived from Torah and Talmud |
| Benevolence / humaneness | ren | Confucianism | the supreme Confucian virtue: love and care for others |
| The Way | dao | Taoism/Confucianism | in Taoism: the ineffable natural order; in Confucianism: the correct moral path |

### Additional terms that appear in tradition descriptions

| Term | Tradition | Gloss |
|------|-----------|-------|
| fiqh | Islam | Islamic jurisprudence (the human elaboration of shari'a) |
| ijtihad | Islam | independent legal reasoning; the exercise of scholarly judgment |
| qiyas | Islam | analogical reasoning in Islamic law |
| ahimsa | Jainism/Hinduism | non-violence; non-harming |
| wu wei | Taoism | non-coercive, effortless action in accord with the dao |
| kami | Shinto | sacred spirits or presences; divine forces |
| wa | Shinto | harmony; social and cosmic concord |
| seva | Sikhism | selfless service |
| machloket | Judaism | principled Talmudic disagreement; multi-voice argumentation |
| karma | Hinduism/Buddhism | the moral law of cause and effect across actions and lives |
| junzi | Confucianism | the morally exemplary person; the Confucian ethical ideal |

### Typographic rules

- Use straight ASCII apostrophes (') for the hamza in fara'id and shari'a. Never use curly
  apostrophes, right single quotation marks (Unicode 2019), or backticks.
- Italicize terms on first use in prose (HTML: `<em>fara'id</em>`); use plain text in table cells.
- Do not add macrons, dots below, or other diacritics — the dashboard is Latin-1 and plain ASCII
  romanizations are preferred for accessibility.
- Glosses should be in parentheses immediately after the term on first use, then omitted.

---

## 6. Sensitivity Guidance — Framing WEIRD Bias Without Dismissing Western Traditions

### What WEIRD means in this context

WEIRD stands for: Western, Educated, Industrialized, Rich, Democratic. The term originates in
Henrich et al. (2010) and identifies the population from which psychology's (and by extension,
AI evaluation's) "universal" findings disproportionately derive. In the context of this paper,
WEIRD-tradition benchmarks are those grounded in traditions with high proximity to Western academic
publishing infrastructure.

### The core sensitivity challenge

Saying "WEIRD benchmarks are biased" can be misread as:
- "Western traditions (Christianity, secularism) are biased or inferior"
- "Evaluating Christian or Jewish content is methodologically suspect"
- "We should discount Western religious traditions in favor of others"

None of these is what the analysis shows. The WEIRD critique is a critique of *structural
over-representation in research infrastructure*, not of the intellectual or moral value of the
traditions themselves.

### Recommended framing principles

**Principle 1: Separate tradition value from infrastructure advantage.**
The WEIRD critique is about what gets studied and how resources flow, not about whose values matter.
Christianity and Judaism are not evaluated poorly in this study; they simply have fewer benchmarks
than their theological richness and global adherent populations would predict — and the analysis
shows this is a research infrastructure problem, not a theological one.

**Principle 2: Christianity is itself structurally disadvantaged relative to Islam.**
The data show Christianity converts candidates to gate-passers at only 5.1% — lower than Islam
(24.8%) and lower than Hinduism (11.6%). Despite massive institutional engagement with AI ethics
(Vatican Rome Call, denominational position papers), Christianity produces relatively few viable
benchmarks. If the dashboard is read as anti-Western, this finding corrects the reading:
Western Christian institutions have engaged robustly with AI ethics, but that engagement has not
translated into benchmark production infrastructure.

**Principle 3: The WEIRD reversal is a data point, not a verdict.**
The C6 finding (non-WEIRD pass rate 14.4% > WEIRD pass rate 8.9%) should be presented with
explicit explanation that this reversal is driven by Islamic benchmark infrastructure, not by
systematic advantage for non-Western traditions. The 8-tradition void (all VOID traditions are
non-Western) is the stronger and more important structural finding.

**Principle 4: Name the mechanism, not the culture.**
Instead of "Western traditions are over-represented," say "English-language publication venues,
HuggingFace, and GitHub create structural access asymmetries." The problem is the pipeline
architecture, not Western culture.

### Recommended display language

In the WEIRD bias section/tooltip:

> "WEIRD bias describes a structural research pattern, not a value judgment about Western
> traditions. Christianity, Judaism, and secular Western ethics face many of the same
> infrastructure barriers as non-Western traditions — they simply lack the Quranic QA
> community's shared-task pipeline. The 'bias' is toward traditions with certain kinds of
> digital infrastructure, not toward any culture or tradition per se."

For the C6 reversal callout:

> "Counterintuitive finding: non-WEIRD traditions actually pass gates at a higher rate
> (14.4% vs 8.9%). But this reversal is driven almost entirely by Islamic benchmark
> infrastructure. Remove Islam from the non-WEIRD group, and the non-WEIRD pass rate
> falls below WEIRD — the 8-tradition void is the underlying structural reality."

### What NOT to say

- Do not use "Western bias" as a synonym for WEIRD — "Western" is imprecise and conflates culture,
  geography, and infrastructure in ways that generate unnecessary political readings.
- Do not imply that reducing WEIRD bias requires reducing the presence of Christianity or
  Judaism in AI evaluation — the goal is to *add* traditions, not displace existing ones.
- Do not frame Islam's benchmark dominance as a challenge to WEIRD bias analysis — the two are
  orthogonal; one is about over-representation of specific infrastructure, the other is about
  the absence of 8 traditions.
- Do not present the WEIRD critique as primarily a political claim — it is an epistemological
  claim about sample diversity and generalizability of evaluation results.

---

## Summary Checklist for Dashboard v7 Implementation

- [ ] Each of the 14 traditions has a one-sentence orienting description in its card/tooltip.
- [ ] VOID and CRITICAL GAP badges include a tooltip distinguishing Type A (coordination gap)
      from Type B (structural exclusion) where applicable.
- [ ] Islam dominance callout explicitly labels the finding as "structural, not theological"
      and names the three infrastructure factors.
- [ ] T2 section labels the instrument as "fara'id — Islamic inheritance law" with tooltip
      explaining what fara'id is and why it discriminates.
- [ ] CAV-1 (T2 blinding asymmetry) is disclosed wherever T2 accuracy figures appear.
- [ ] All romanized terms use ASCII apostrophes; no native scripts anywhere.
- [ ] WEIRD bias section distinguishes mechanism (infrastructure) from culture.
- [ ] C6 reversal is accompanied by the Islam-driven explanation.
- [ ] No fabricated expert names. Use "[Religious Studies perspective]",
      "[Islamic Studies perspective]", "[Buddhist Studies perspective]", etc.
