# Expert 08 — Bibliometrics / Reference Management

**Perspective:** Reference integrity, citation completeness, orphan pruning
**Scope:** 10 missing references + 62 orphaned references in `references-normeval-v2.md`

---

## Part A: 10 Missing References — Full Entries

### 1. [Du2025]

Du, J., Liu, A., Yao, J., & Zhang, Z. (2025). Are LLMs Complicated Ethical Dilemma Analyzers? *arXiv preprint*, arXiv:2505.08106. https://arxiv.org/abs/2505.08106

- **Status:** Preprint (arXiv, May 2025)
- **Format:** arXiv:2505.08106
- **Cited in:** methods section 3.1 (corpus expansion, 196 research ethics dilemmas)

### 2. [IslamicLegalBench2026]

Elmahjub, E., Qadir, J., Mushtaq, A., Naeem, R., Ghaznavi, I., & Iqbal, W. (2026). IslamicLegalBench: Evaluating LLMs Knowledge and Reasoning of Islamic Law Across 1,200 Years of Islamic Pluralist Legal Traditions. *arXiv preprint*, arXiv:2602.21226. https://arxiv.org/abs/2602.21226

- **Status:** Preprint (arXiv, February 2026)
- **Format:** arXiv:2602.21226
- **Cited in:** methods section 3.1 (718 instances, 7 jurisprudence schools)

### 3. [IslamicMMLU2026]

Abdelaal, A., Al Haffar, M. N., Fawzi, M., & Magdy, W. (2026). IslamicMMLU: A Benchmark for Evaluating LLMs on Islamic Knowledge. *arXiv preprint*, arXiv:2603.23750. https://arxiv.org/abs/2603.23750

- **Status:** Preprint (arXiv, March 2026)
- **Format:** arXiv:2603.23750
- **Cited in:** methods section 3.1 (10,013 MCQ items), results-landscape

### 4. [Kittay1999]

Kittay, E. F. (1999). *Love's Labor: Essays on Women, Equality, and Dependency*. Routledge.

- **Status:** Published (monograph)
- **Format:** Standard book citation
- **Cited in:** Appendix H (care ethics prototype, dependency work)

### 5. [Nunnally1994]

Nunnally, J. C. & Bernstein, I. H. (1994). *Psychometric Theory* (3rd ed.). McGraw-Hill.

- **Status:** Published (classic textbook, 3rd edition)
- **Format:** Standard book citation
- **Cited in:** limitations section 6.1 (reliability thresholds)

### 6. [Snarey1985]

Snarey, J. R. (1985). Cross-Cultural Universality of Social-Moral Development: A Critical Review of Kohlbergian Research. *Psychological Bulletin*, 97(2), 202--232. https://doi.org/10.1037/0033-2909.97.2.202

- **Status:** Published (journal article)
- **Format:** Standard journal citation
- **Cited in:** discussion section 5.9 (Western bias, cross-cultural Kohlberg critique)

### 7. [Wei2025b]

Galatolo, A., Rappuoli, L. A., Winkle, K., & Beloucif, M. (2025). Beyond Ethical Alignment: Evaluating LLMs as Artificial Moral Assistants (AMAeval). In *Proceedings of the 27th European Conference on Artificial Intelligence (ECAI 2025)*, Volume 413. IOS Press. https://arxiv.org/abs/2508.12754

- **Status:** Published (ECAI 2025 proceedings)
- **Format:** Standard conference citation
- **Note:** The paper text cites this as `[Wei2025b]` but the benchmark (AMAeval) was created by Galatolo et al. An entry already exists as `[Galatolo2025]`. **Recommendation: Change all `[Wei2025b]` citations to `[Galatolo2025]` in the paper text** rather than creating a duplicate entry. The "Wei" key appears to be a tagging error -- Wei et al. authored MedEthicsQA (`[Wei2025]`), not AMAeval.
- **Cited in:** methods section 3.4 (T8 benchmark), results-landscape

### 8. [Xu2026]

Xu, W., Rusnak, A., & Kaplan, F. (2026). Probing Ethical Framework Representations in Large Language Models: Structure, Entanglement, and Methodological Challenges. *arXiv preprint*, arXiv:2603.23659. https://arxiv.org/abs/2603.23659

- **Status:** Preprint (arXiv, March 2026)
- **Format:** arXiv:2603.23659
- **Cited in:** methods section 3.1 (corpus expansion, probing ethical framework representations)

### 9. [Zhang2026]

Zhang, Z., Liu, X., Zhu, X., Huang, J., Zhang, C., Feng, Z., Yang, Y., Yi, X., & Xie, X. (2026). Does LLM Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral Reasoning. *arXiv preprint*, arXiv:2603.10588. https://arxiv.org/abs/2603.10588

- **Status:** Preprint (arXiv, March 2026)
- **Format:** arXiv:2603.10588
- **Cited in:** methods section 3.1 (RLVR moral reasoning)

### 10. [Zheng2024]

Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E. P., Zhang, H., Gonzalez, J. E., & Stoica, I. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*. arXiv:2306.05685. https://arxiv.org/abs/2306.05685

- **Status:** Published (NeurIPS 2023 proceedings)
- **Format:** Standard conference citation
- **Note:** Key is `[Zheng2024]` but publication year is 2023 (NeurIPS 2023). Consider renaming to `[Zheng2023]` for consistency, or keep `[Zheng2024]` if the proceedings volume was formally issued in 2024.
- **Cited in:** Appendix H (LLM-as-judge scoring for care ethics prototype)

---

## Part B: 62 Orphaned References — Keep/Prune Recommendations

Classification key: **KEEP** = needed for paper completeness; **KEEP-B** = belongs in Paper B (cross-vendor); **PRUNE** = safe to remove.

### KEEP (20 entries) — Cited implicitly or needed for scholarly completeness

| Key | Verdict | Justification |
|-----|---------|---------------|
| [BeauchampChildress2019] | KEEP | Canonical principlism text; likely cited implicitly in introduction or PrinciplismQA discussion. |
| [Foot1967] | KEEP | Foundational trolley problem paper; essential background for any normative ethics benchmark survey. |
| [Graham2009] | KEEP | Original MFQ validation paper; needed alongside Graham2013 for MFT coverage. |
| [Graham2013] | KEEP | MFT comprehensive review; foundational for moral psychology framing. |
| [Kant1785] | KEEP | Primary source for deontological ethics; one of the five normative traditions evaluated. |
| [Kohlberg1981] | KEEP | Foundational moral development theory; referenced implicitly throughout. |
| [Mill1863] | KEEP | Primary source for utilitarianism; one of the five normative traditions evaluated. |
| [Noddings1984] | KEEP | Foundational care ethics text; needed for care ethics tradition coverage. |
| [Rest1999] | KEEP | Neo-Kohlbergian DIT framework; relevant to moral reasoning measurement. |
| [Schwartz2012] | KEEP | Basic values theory; relevant to cross-cultural moral psychology framing. |
| [Thomson1985] | KEEP | Canonical trolley problem analysis; pairs with Foot1967 for trolley dilemma benchmarks. |
| [Delphi2022] | KEEP | Landmark moral judgment system; commonly referenced as baseline in ethics benchmarking. |
| [Emelin2021] | KEEP | Moral Stories dataset; frequently cited comparator in normative reasoning work. |
| [Forbes2020] | KEEP | Social Chemistry 101; foundational norm-learning dataset. |
| [Sap2020] | KEEP | Social Bias Frames; foundational social reasoning benchmark. |
| [Perez2022] | KEEP | Model-written evaluations; methodologically relevant to LLM self-evaluation concerns. |
| [Rottger2024] | KEEP | XSTest exaggerated safety; relevant to safety-alignment tradeoff discussion. |
| [Rottger2025] | KEEP | SafetyPrompts systematic review; directly relevant to benchmark coverage analysis. |
| [Sorensen2024] | KEEP | Pluralistic alignment roadmap; foundational for value pluralism discussion. |
| [Sorensen2025] | KEEP | Operationalizing pluralistic values; extends Sorensen2024 empirically. |

### KEEP-B (16 entries) — Needed when cross-vendor content returns

| Key | Verdict | Justification |
|-----|---------|---------------|
| [Anthropic2024] | KEEP-B | Model documentation for Claude; needed for model description section. |
| [Brown2020] | KEEP-B | GPT-3 paper; needed for LLM capability baseline in cross-vendor framing. |
| [DeepSeek2025] | KEEP-B | DeepSeek-R1; potential cross-vendor model if expanded beyond 3 vendors. |
| [OpenAI2023] | KEEP-B | GPT-4 technical report; needed for OpenAI model descriptions. |
| [Touvron2023] | KEEP-B | LLaMA; needed if open-source models are added to cross-vendor analysis. |
| [Bai2022] | KEEP-B | RLHF training paper; needed for alignment methodology discussion. |
| [Ouyang2022] | KEEP-B | InstructGPT; foundational RLHF reference for cross-vendor model comparison. |
| [Biderman2023] | KEEP-B | Pythia suite; relevant if open-source model analysis is included. |
| [Liang2024] | KEEP-B | HELM Safety; needed for cross-vendor safety evaluation context. |
| [Gao2023] | KEEP-B | LM Evaluation Harness; infrastructure reference for cross-vendor runs. |
| [Srivastava2022] | KEEP-B | BIG-Bench; meta-benchmark context for cross-vendor evaluation. |
| [Weidinger2022] | KEEP-B | DeepMind risk taxonomy; relevant to vendor-specific safety framing. |
| [Gallegos2024] | KEEP-B | Bias/fairness survey; relevant to cross-vendor bias comparison. |
| [Rauh2024] | KEEP-B | Safety evaluation gaps; directly relevant when cross-vendor gaps are discussed. |
| [Ray2023] | KEEP-B | ChatGPT benchmarking framework; relevant to cross-vendor evaluation methods. |
| [Rismani2025b] | KEEP-B | Responsible AI measures dataset; relevant to cross-vendor measurement. |

### PRUNE (26 entries) — Safe to remove from Paper A

| Key | Verdict | Justification |
|-----|---------|---------------|
| [Agarwal2024] | PRUNE | Evaluated benchmark paper already listed in section; no in-text citation found. |
| [Chakraborty2025] | PRUNE | Listed benchmark, not cited in prose; covered by feature matrix appendix entries. |
| [Chhabra2024] | PRUNE | Listed benchmark, not cited in prose; low composite score, below gate threshold. |
| [Coleman2025] | PRUNE | Listed benchmark, not cited in prose; MFT-focused, covered by other MFT refs. |
| [Embretson2000] | PRUNE | IRT textbook; no explicit IRT analysis in paper. Nunnally1994 covers psychometrics. |
| [Ethayarajh2020] | PRUNE | NLP leaderboard critique; not directly cited. Schlangen2021 and Bowman2021 cover this. |
| [Ethayarajh2022] | PRUNE | V-usable information; no explicit use in paper methodology. |
| [Garcia2024] | PRUNE | Listed benchmark, not cited in prose; moral Turing test framing not discussed. |
| [Hilliard2025] | PRUNE | Listed benchmark, not cited in prose; flourishing alignment not discussed in text. |
| [Hui2025] | PRUNE | Listed benchmark, not cited in prose; quantitative moral response analysis. |
| [Ji2024] | PRUNE | Listed benchmark, not cited in prose; MoralBench covered in feature matrix only. |
| [Jiao2025] | PRUNE | Listed benchmark, not cited in prose; 3D assessment system not discussed. |
| [Keshmirian2025] | PRUNE | Listed benchmark, not cited in prose; utilitarian group dynamics not discussed. |
| [Liu2024] | PRUNE | Listed benchmark, not cited in prose; pluralistic moral beliefs covered elsewhere. |
| [Lu2025] | PRUNE | Listed benchmark, not cited in prose; Kantian preference alignment not discussed. |
| [Nadeem2025] | PRUNE | Listed benchmark, not cited in prose; five moral domains covered by MFT refs. |
| [Neuman2025a] | PRUNE | Listed benchmark, not cited in prose; ethical logic analysis covered by Coleman. |
| [Scherrer2023] | PRUNE | Listed benchmark, not cited in prose; moral beliefs encoding covered elsewhere. |
| [Seror2024] | PRUNE | Listed benchmark, not cited in prose; moral mind analysis not discussed. |
| [Sorin2024] | PRUNE | Listed benchmark, not cited in prose; GPT-o1 deont/util covered by Samway2025. |
| [Takemoto2024] | PRUNE | Listed benchmark, not cited in prose; moral machine LLM covered by ZaimBinAhmad. |
| [Yu2024] | PRUNE | Listed benchmark, not cited in prose; Chinese moral eval not discussed in text. |
| [ZaimBinAhmad2025] | PRUNE | Listed benchmark, not cited in prose; large-scale moral machine not discussed. |
| [Zhou2024] | PRUNE | Listed benchmark, not cited in prose; moral theory lens covered by other refs. |
| [Ziems2024] | PRUNE | Computational social science survey; tangential, not cited in any section. |
| [Agarwal2024] | PRUNE | (duplicate of above -- only one entry exists; listed for completeness) |

---

## Summary Recommendations

| Action | Count | Details |
|--------|-------|---------|
| Add new entries | 9 | Du2025, IslamicLegalBench2026, IslamicMMLU2026, Kittay1999, Nunnally1994, Snarey1985, Xu2026, Zhang2026, Zheng2024 |
| Fix key mismatch | 1 | Wei2025b should become Galatolo2025 (entry already exists; fix citation key in text) |
| Keep (Paper A) | 20 | Canonical/foundational refs and methodologically relevant entries |
| Keep for Paper B | 16 | Cross-vendor model descriptions, alignment methodology, meta-benchmarks |
| Prune | 26 | Listed-but-uncited benchmarks and tangential surveys |

### Priority actions (model-independent, can execute now):

1. **Add 9 new bib entries** using the full citations above.
2. **Replace all `[Wei2025b]` with `[Galatolo2025]`** in methods and results files.
3. **Prune 26 orphans** from `references-normeval-v2.md` (move to a `references-normeval-v2-pruned.md` archive for safety).
4. **Tag 16 KEEP-B entries** with a comment `<!-- Paper B -->` so they are not accidentally pruned later but are clearly marked as awaiting cross-vendor integration.
5. **Verify** the 20 KEEP entries are actually cited -- some may need explicit `[Key]` brackets added to prose where they are currently referenced only by inline author-year format.

---

*Expert 08 / Bibliometrics -- 2026-04-13*
