# P3 Manual Browser Execution Plan

Generated: 2026-02-14T07:54:25

Execute in order. For each item: open URL in browser, download verified PDF, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

## #1 `LSRC0019` `2018-Liebeskind-Identifying Abusive Comments in Hebrew Facebook.md`
- URL: https://doi.org/10.1109/icsee.2018.8646190
- Host: `ieeexplore.ieee.org`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://doi.org/10.1109/icsee.2018.8646190 | http://xplorestaging.ieee.org/ielx7/8643018/8645960/08646190.pdf?arnumber=8646190
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Use IEEE landing page with institution login, then PDF.

## #2 `LSRC0535` `2021-Perifanos-Multimodal Hate Speech Detection in Greek Social Media.md`
- URL: https://doaj.org/article/05daae56eb58463caf4838d544585112
- Host: `doaj.org`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://doaj.org/article/05daae56eb58463caf4838d544585112 | https://doi.org/10.3390/mti5070034
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open DOAJ record and follow Full Text to publisher PDF.

## #3 `LSRC0136` `2022-Ataei-Pars-OFF A Benchmark for Offensive Language Detection on Farsi Social.md`
- URL: https://doi.org/10.1109/taffc.2022.3219229
- Host: `ieeexplore.ieee.org`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://doi.org/10.1109/taffc.2022.3219229 | http://xplorestaging.ieee.org/ielx7/5165369/10330166/09936700.pdf?arnumber=9936700
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Use IEEE landing page with institution login, then PDF.

## #4 `LSRC0151` `2022-Saeed-Hate Speech Detection in Social Media for the Kurdish Language.md`
- URL: https://link.springer.com/content/pdf/10.1007/978-3-031-14054-9_24
- Host: `link.springer.com`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://link.springer.com/content/pdf/10.1007/978-3-031-14054-9_24 | https://doi.org/10.1007/978-3-031-14054-9_24
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open article/chapter page first, then Download PDF in browser session.

## #5 `LSRC0152` `2023-Badawi-KurdiSent A Corpus for Kurdish Sentiment Analysis.md`
- URL: https://link.springer.com/content/pdf/10.1007/s10579-023-09716-6.pdf
- Host: `link.springer.com`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://link.springer.com/content/pdf/10.1007/s10579-023-09716-6.pdf | https://link.springer.com/article/10.1007/s10579-023-09716-6/fulltext.html
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open article/chapter page first, then Download PDF in browser session.

## #6 `LSRC0232` `2024-CiTIUS-A Galician-Portuguese Generative Model.md`
- URL: https://link.springer.com/content/pdf/10.1007/978-3-031-73503-5_24
- Host: `link.springer.com`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://link.springer.com/content/pdf/10.1007/978-3-031-73503-5_24 | https://doi.org/10.1007/978-3-031-73503-5_24
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open article/chapter page first, then Download PDF in browser session.

## #7 `LSRC0468` `2024-Keller-HOCON34k A Corpus of Hate Speech in Online Comments from German.md`
- URL: https://link.springer.com/content/pdf/10.1007/978-3-031-78090-5_18
- Host: `link.springer.com`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://link.springer.com/content/pdf/10.1007/978-3-031-78090-5_18 | https://doi.org/10.1007/978-3-031-78090-5_18
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open article/chapter page first, then Download PDF in browser session.

## #8 `AUTO_RIBEIRO2024` `2024-Ribeiro-Machine Ethics Architecture of Virtue.md`
- URL: https://link.springer.com/content/pdf/10.1007/978-3-031-48855-9_29
- Host: `link.springer.com`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://link.springer.com/content/pdf/10.1007/978-3-031-48855-9_29 | https://doi.org/10.1007/978-3-031-48855-9_29
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open article/chapter page first, then Download PDF in browser session.

## #9 `LSRC0208` `2024-Trajano-OLID-BR Offensive Language Identification Dataset for Brazilian.md`
- URL: https://link.springer.com/content/pdf/10.1007/s10579-023-09657-0.pdf
- Host: `link.springer.com`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://link.springer.com/content/pdf/10.1007/s10579-023-09657-0.pdf | https://link.springer.com/article/10.1007/s10579-023-09657-0/fulltext.html
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open article/chapter page first, then Download PDF in browser session.

## #10 `LSRC0069` `2024-Younas-Proposing Central Asian AI Ethics Principles A Multilevel Approach.md`
- URL: https://link.springer.com/content/pdf/10.1007/s43681-024-00505-7.pdf
- Host: `link.springer.com`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://link.springer.com/content/pdf/10.1007/s43681-024-00505-7.pdf | https://link.springer.com/article/10.1007/s43681-024-00505-7/fulltext.html
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open article/chapter page first, then Download PDF in browser session.

## #11 `LSRC0645` `2025-Abdelhalim-Full article Artificial intelligence tools and literary translation a.md`
- URL: https://doaj.org/article/0b7596092b654cc18314add11274f3ad
- Host: `doaj.org`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://doaj.org/article/0b7596092b654cc18314add11274f3ad | https://doi.org/10.1080/23311983.2025.2508031
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open DOAJ record and follow Full Text to publisher PDF.

## #12 `LSRC0638` `2025-Sun-Full article ChatGPT translation vs. human translation an examination.md`
- URL: https://doaj.org/article/92bbdf42d3af4e0b9e559fa24c51182d
- Host: `doaj.org`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://doaj.org/article/92bbdf42d3af4e0b9e559fa24c51182d | https://doi.org/10.1080/23311886.2025.2472916
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open DOAJ record and follow Full Text to publisher PDF.

## #13 `` `2023-Stenseke-Use and Abuse Normative Ethics Moral Machines.md`
- URL: https://ebooks.iospress.nl/pdf/doi/10.3233/FAIA220614
- Host: `ebooks.iospress.nl`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://ebooks.iospress.nl/pdf/doi/10.3233/FAIA220614 | https://doi.org/10.3233/faia220614
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Publisher landing page; try PDF control and DOI mirror if blocked.

## #14 `LSRC0618` `2024-Kuriyozov-Construction and Evaluation of Sentiment Datasets for Low-Resource.md`
- URL: https://link.springer.com/content/pdf/10.1007/978-3-031-05328-3_15
- Host: `link.springer.com`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://link.springer.com/content/pdf/10.1007/978-3-031-05328-3_15 | https://doi.org/10.1007/978-3-031-05328-3_15
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open article/chapter page first, then Download PDF in browser session.

## #15 `LSRC0689` `2025-Xie-Ce‐LLMs Status and trends of education‐specific large language models.md`
- URL: https://doaj.org/article/c2a7bded3de5490eb6686b4df108ab07
- Host: `doaj.org`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://doaj.org/article/c2a7bded3de5490eb6686b4df108ab07 | https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/fer3.70008
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open DOAJ record and follow Full Text to publisher PDF.

## #16 `LSRC0800` `2025-Onose-Benchmarking Large Language Models Across Languages Modalities Models.md`
- URL: https://arxiv.org/pdf/2311.07463.pdf
- Host: `arxiv.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `` HTTP ``
- Manual focus: Queue filename stale; update to current paper filename before retry.
- Next step: Use direct /pdf/<id>.pdf link and verify title.

## #17 `LSRC0493` `2023-University-Harmful Communication Detection of Toxic Language and Threats on.md`
- URL: https://dl.acm.org/doi/pdf/10.1145/3625007.3627597
- Host: `dl.acm.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://dl.acm.org/doi/pdf/10.1145/3625007.3627597 | https://dl.acm.org/doi/10.1145/3625007.3627597
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Institution login likely required. Open DOI page; use PDF button or author-provided free copy.

## #18 `EXSR0597` `2022-Multiple Data in Brief-Sanadset 650K Data on Hadith Narrators.md`
- URL: https://doi.org/10.1016/j.dib.2022.108540
- Host: `linkinghub.elsevier.com`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://doi.org/10.1016/j.dib.2022.108540
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Landing page only; pivot to ScienceDirect PDF control.

## #19 `LSRC0621` `2024-Unknown-A structured sentiment analysis dataset based on public comments from.md`
- URL: https://doi.org/10.1016/j.dib.2024.110232
- Host: `linkinghub.elsevier.com`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://doi.org/10.1016/j.dib.2024.110232
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Landing page only; pivot to ScienceDirect PDF control.

## #20 `LSRC0768` `2025-Unknown-Enhancing Multilingual Hate Speech Detection From Language-Specific.md`
- URL: https://doi.org/10.1109/access.2024.3452987
- Host: `ieeexplore.ieee.org`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://doi.org/10.1109/access.2024.3452987
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Use IEEE landing page with institution login, then PDF.

## #21 `LSRC0380` `2024-Jang-Cross-Linguistic Moral Preferences in Large Language Models Evidence.md`
- URL: https://doi.org/10.3390/electronics14244919
- Host: `www.mdpi.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://doi.org/10.3390/electronics14244919 | https://www.mdpi.com/2079-9292/14/24/4919/pdf
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Use article page PDF control (JS/cookie required).

## #22 `LSRC0653` `2025-Cognitive-Cognitive LLMs Toward Human-Like Artificial Intelligence by.md`
- URL: https://doi.org/10.1177/29498732251377341
- Host: `journals.sagepub.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://doi.org/10.1177/29498732251377341 | https://journals.sagepub.com/doi/pdf/10.1177/29498732251377341
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Often auth-gated; use institution login for PDF.

## #23 `LSRC0057` `2025-Deepawali-Hate Speech Detection Research in South Asian Languages A Survey of.md`
- URL: https://dl.acm.org/doi/10.1145/3711710
- Host: `dl.acm.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://dl.acm.org/doi/10.1145/3711710 | https://dl.acm.org/doi/pdf/10.1145/3711710
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Institution login likely required. Open DOI page; use PDF button or author-provided free copy.

## #24 `LSRC0072` `2025-Göçen-Teachers vs. large language models ethical decision-making across.md`
- URL: https://www.tandfonline.com/doi/pdf/10.1080/10508422.2025.2581274
- Host: `www.tandfonline.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://www.tandfonline.com/doi/pdf/10.1080/10508422.2025.2581274 | https://doi.org/10.1080/10508422.2025.2581274
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Often auth-gated; use institution login for PDF or accepted manuscript.

## #25 `LSRC0703` `2025-Lim-How Do Users Identify and Perceive Stereotypes Understanding User.md`
- URL: https://dl.acm.org/doi/pdf/10.1145/3715275.3732207
- Host: `dl.acm.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://dl.acm.org/doi/pdf/10.1145/3715275.3732207 | https://doi.org/10.1145/3715275.3732207
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Institution login likely required. Open DOI page; use PDF button or author-provided free copy.

## #26 `EXSR0299` `2025-Muntean-Moral Coherentism Theoretical Framework Muntean.md`
- URL: https://doi.org/10.5406/21521123.62.3.06
- Host: `scholarlypublishingcollective.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://doi.org/10.5406/21521123.62.3.06 | https://scholarlypublishingcollective.org/uip/apq/article-pdf/62/3/279/2274621/279muntean.pdf
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Publisher landing page; check for OA/accepted manuscript mirrors.

## #27 `LSRC0199` `2025-Wasi-Dialectal Bias in Bengali An Evaluation of Multilingual Language.md`
- URL: https://dl.acm.org/doi/pdf/10.1145/3701716.3715468
- Host: `dl.acm.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://dl.acm.org/doi/pdf/10.1145/3701716.3715468 | https://dl.acm.org/doi/10.1145/3701716.3715468
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Institution login likely required. Open DOI page; use PDF button or author-provided free copy.

## #28 `LSRC0713` `2025-Aly-Applying Data Feminism Principles to Assess Bias in English and.md`
- URL: https://doi.org/10.1145/3715275.3732119
- Host: `dl.acm.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://doi.org/10.1145/3715275.3732119 | https://dl.acm.org/doi/pdf/10.1145/3715275.3732119
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Institution login likely required. Open DOI page; use PDF button or author-provided free copy.

## #29 `LSRC0649` `2025-Cognitive-Improved Tibetan Word Vectors Models Based on Position Information.md`
- URL: https://dl.acm.org/doi/pdf/10.1145/3681787
- Host: `dl.acm.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://dl.acm.org/doi/pdf/10.1145/3681787 | https://dl.acm.org/doi/10.1145/3681787
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Institution login likely required. Open DOI page; use PDF button or author-provided free copy.

## #30 `LSRC0626` `2025-Pretrained-Optimizing Uyghur Speech Synthesis by Combining Pretrained.md`
- URL: https://dl.acm.org/doi/pdf/10.1145/3675397
- Host: `dl.acm.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://dl.acm.org/doi/pdf/10.1145/3675397 | https://dl.acm.org/doi/10.1145/3675397
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Institution login likely required. Open DOI page; use PDF button or author-provided free copy.

## #31 `EXSR0585` `2022-Pollak-Embeddings Models for Buddhist Sanskrit.md`
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10280248/pdf/peerj-cs-08-1128.pdf
- Host: `pmc.ncbi.nlm.nih.gov`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://pmc.ncbi.nlm.nih.gov/articles/PMC10280248/pdf/peerj-cs-08-1128.pdf
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open in browser, locate PDF link, verify title, update fields.

## #32 `LSRC0127` `2024-Miranda-Desiderata for Filipino NLP in the Age of LLMs.md`
- URL: https://arxiv.org/pdf/2410.20817
- Host: `arxiv.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `` HTTP ``
- Example attempted URLs: https://arxiv.org/pdf/2410.20817
- Manual focus: Downloaded file did not match title strongly; re-check source and verify first-page title.
- Next step: Use direct /pdf/<id>.pdf link and verify title.

## #33 `T7SMT2WN` `2025-Center-Personal Consultations Case Study Database.md`
- URL: https://www.ncbcenter.org/s/NCBC-Case-Studies.pdf
- Host: `static1.squarespace.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `` HTTP ``
- Example attempted URLs: https://www.ncbcenter.org/s/NCBC-Case-Studies.pdf
- Manual focus: Downloaded file did not match title strongly; re-check source and verify first-page title.
- Next step: Open in browser, locate PDF link, verify title, update fields.

## #34 `LSRC0753` `2025-Demidova-SIGARAB - Arabic NLP Archives.md`
- URL: https://drive.google.com/uc?id=1e5XNSsPZZnp4Oa4LK_qVucu_0iQJb0lS&export=download
- Host: `drive.usercontent.google.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `` HTTP ``
- Example attempted URLs: https://drive.google.com/uc?id=1e5XNSsPZZnp4Oa4LK_qVucu_0iQJb0lS&export=download | https://drive.google.com/uc?id=1pIX0om3GYK41GwHE7xnG1PFznlJSgiRF&export=download
- Manual focus: Downloaded file did not match title strongly; re-check source and verify first-page title.
- Next step: Direct file URL; verify payload is real PDF and title-matched.

## #35 `LSRC0816` `2025-Masood-Large language models are biased - local initiatives are fighting for.md`
- URL: https://arxiv.org/pdf/1810.04805
- Host: `arxiv.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `` HTTP ``
- Example attempted URLs: https://arxiv.org/pdf/1810.04805 | https://assets.mofoprod.net/network/documents/Common_Crawl_Mozilla_Foundation_2024.pdf
- Manual focus: Downloaded file did not match title strongly; re-check source and verify first-page title.
- Next step: Use direct /pdf/<id>.pdf link and verify title.

## #36 `EXSR0386` `2025-Research-IndQA An Indic QA Benchmark for.md`
- URL: https://www.ibm.com/downloads/documents/us-en/107a02e94948f49f
- Host: `www.ibm.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `` HTTP ``
- Manual focus: Paper already has local PDF; ensure external_pdf/pdf_extract are consistent.
- Next step: Open in browser, locate PDF link, verify title, update fields.

## #37 `LSRC0764` `2025-Firmino-Improving hate speech detection using Cross-Lingual Learning -.md`
- URL: http://ceur-ws.org/Vol-2765/overview.pdf
- Host: `ceur-ws.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `` HTTP ``
- Example attempted URLs: http://ceur-ws.org/Vol-2765/overview.pdf | http://ceur-ws.org/Vol-2253/paper49.pdf
- Manual focus: Downloaded file did not match title strongly; re-check source and verify first-page title.
- Next step: Use direct CEUR PDF link (/Vol-*/paper*.pdf).

## #38 `LSRC0661` `2025-Unknown-New Guidelines for Evaluating Literary Translation in Hiring and.md`
- URL: https://www.acls.org/wp-content/uploads/2021/11/Guidelines-for-the-Translation-of-Social-Science-Texts.pdf
- Host: `www.acls.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `` HTTP ``
- Example attempted URLs: https://www.acls.org/wp-content/uploads/2021/11/Guidelines-for-the-Translation-of-Social-Science-Texts.pdf
- Manual focus: Downloaded file did not match title strongly; re-check source and verify first-page title.
- Next step: Open in browser, locate PDF link, verify title, update fields.

## #39 `LSRC0833` `2025-Xu-Nlp Fairness ConceptNet blog.md`
- URL: https://arxiv.org/pdf/1607.06520.pdf
- Host: `arxiv.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `` HTTP ``
- Example attempted URLs: https://arxiv.org/pdf/1607.06520.pdf
- Manual focus: Downloaded file did not match title strongly; re-check source and verify first-page title.
- Next step: Use direct /pdf/<id>.pdf link and verify title.

## #40 `LSRC0789` `2025-Jiang-Preserving the Past AI in Indigenous Language Preservation - Viterbi.md`
- URL: https://arxiv.org/pdf/2405.08997
- Host: `arxiv.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `` HTTP ``
- Example attempted URLs: https://arxiv.org/pdf/2405.08997
- Manual focus: Downloaded file did not match title strongly; re-check source and verify first-page title.
- Next step: Use direct /pdf/<id>.pdf link and verify title.

## #41 `LSRC0609` `2025-Hulagadri-Towards fair and comprehensive multilingual LLM benchmarking SEA-LION.md`
- URL: https://arxiv.org/pdf/2311.07804?ref=cohere-ai.ghost.io
- Host: `arxiv.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `` HTTP ``
- Example attempted URLs: https://arxiv.org/pdf/2311.07804?ref=cohere-ai.ghost.io | https://arxiv.org/pdf/2009.03300v3?ref=cohere-ai.ghost.io
- Manual focus: Downloaded file did not match title strongly; re-check source and verify first-page title.
- Next step: Use direct /pdf/<id>.pdf link and verify title.

## #42 `LSRC0624` `2021-Pretrained-Research on Uyghur‐Chinese Neural Machine Translation Based on the.md`
- URL: https://doi.org/10.1155/2021/5744248
- Host: `www.hindawi.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://doi.org/10.1155/2021/5744248 | https://downloads.hindawi.com/journals/misy/2021/5744248.pdf
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Open in browser, locate PDF link, verify title, update fields.

## #43 `LSRC0663` `2025-Li-AI Development and Innovation A Comparison of Large Language Models.md`
- URL: https://dl.acm.org/doi/pdf/10.1145/3769086
- Host: `dl.acm.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://dl.acm.org/doi/pdf/10.1145/3769086 | https://doi.org/10.1145/3769086
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Institution login likely required. Open DOI page; use PDF button or author-provided free copy.

## #44 `AUTO_MUYSKENS2024` `2024-Muyskens-Can an AI-carebot be filial.md`
- URL: https://journals.sagepub.com/doi/pdf/10.1177/09697330241238332
- Host: `journals.sagepub.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://journals.sagepub.com/doi/pdf/10.1177/09697330241238332 | https://journals.sagepub.com/doi/full-xml/10.1177/09697330241238332
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Often auth-gated; use institution login for PDF.

## #45 `LSRC0652` `2025-Cognitive-Tibetan Text Classification based on Prompt Learning and Ensemble.md`
- URL: https://dl.acm.org/doi/10.1145/3711827
- Host: `dl.acm.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://dl.acm.org/doi/10.1145/3711827 | https://dl.acm.org/doi/pdf/10.1145/3711827
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Institution login likely required. Open DOI page; use PDF button or author-provided free copy.

## #46 `` `2021-Sullins-Artificial Phronesis - What It Is and Is Not.md`
- URL: https://doi.org/10.1093/oso/9780190081713.003.0015
- Host: `academic.oup.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://doi.org/10.1093/oso/9780190081713.003.0015
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Institution login required; use chapter/article PDF control.

## #47 `EXSR0609` `2021-collaborators-Optimisation of the Largest Annotated Tibetan.md`
- URL: https://www.tara.tcd.ie/bitstreams/a792d942-04f8-4021-8b03-16e6088dd6d7/download
- Host: `www.tara.tcd.ie`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://www.tara.tcd.ie/bitstreams/a792d942-04f8-4021-8b03-16e6088dd6d7/download
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Open in browser, locate PDF link, verify title, update fields.

## #48 `EXSR0558` `2023-2023-Hadiths Classification Using a Novel Author-Based.md`
- URL: https://www.mdpi.com/2504-2289/7/3/141/pdf
- Host: `www.mdpi.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://www.mdpi.com/2504-2289/7/3/141/pdf
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Use article page PDF control (JS/cookie required).

## #49 `LSRC0126` `2023-Unknown-Hate speech and abusive language detection in Indonesian social media.md`
- URL: https://www.semanticscholar.org/paper/f21e111e0836662aeb75cb39ac3dec241d199855
- Host: `www.semanticscholar.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_202` HTTP `202`
- Example attempted URLs: https://www.semanticscholar.org/paper/f21e111e0836662aeb75cb39ac3dec241d199855
- Manual focus: Candidate is metadata/preview page; pivot to publisher/DOI PDF link.
- Next step: Metadata-only page; pivot to DOI/arXiv/publisher links.

## #50 `LSRC0137` `2023-Unknown-Pars-HaO Hate and Offensive Language Detection on Persian Tweets.md`
- URL: https://www.authorea.com/users/581546/articles/683116-pars-hao-hate-and-offensive-language-detection-on-persian-tweets-using-machine-learning-and-deep-learning
- Host: `www.authorea.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://www.authorea.com/users/581546/articles/683116-pars-hao-hate-and-offensive-language-detection-on-persian-tweets-using-machine-learning-and-deep-learning
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Use article page export/download PDF control.

## #51 `EXSR0506` `2024-Felipe-Ruiz-Lexical Sentiment and Correlation Analysis of.md`
- URL: https://www.semanticscholar.org/paper/3c74734c8c6bc4775172978d5b48784ffa93329e
- Host: `www.semanticscholar.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_202` HTTP `202`
- Example attempted URLs: https://www.semanticscholar.org/paper/3c74734c8c6bc4775172978d5b48784ffa93329e
- Manual focus: Candidate is metadata/preview page; pivot to publisher/DOI PDF link.
- Next step: Metadata-only page; pivot to DOI/arXiv/publisher links.

## #52 `LSRC0725` `2024-Kajiwara-Beyond Traditional Classifiers Evaluating Large Language Models for.md`
- URL: https://www.mdpi.com/2079-3197/13/8/196
- Host: `www.mdpi.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://www.mdpi.com/2079-3197/13/8/196
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Use article page PDF control (JS/cookie required).

## #53 `LSRC0165` `2024-Khan-From Tradition to Technology A Systematic Survey on Navigating Pashto.md`
- URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031721
- Host: `papers.ssrn.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031721
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Open abstract page and download PDF (may require sign-in).

## #54 `LSRC0083` `2024-Thu-Development and Evaluation of Myanmar GPT A Language Model for.md`
- URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4871732
- Host: `papers.ssrn.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4871732
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Open abstract page and download PDF (may require sign-in).

## #55 `LSRC0619` `2024-Unknown-Towards Better Sentiment Analysis in the Turkish Language Dataset.md`
- URL: https://www.semanticscholar.org/paper/dd6418de683b5a4054a8b8c9ed261c288093fa13
- Host: `www.semanticscholar.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_202` HTTP `202`
- Example attempted URLs: https://www.semanticscholar.org/paper/dd6418de683b5a4054a8b8c9ed261c288093fa13
- Manual focus: Candidate is metadata/preview page; pivot to publisher/DOI PDF link.
- Next step: Metadata-only page; pivot to DOI/arXiv/publisher links.

## #56 `LSRC0603` `2024-Veitsman-The Development and Experimental Evaluation of a Multilingual Speech.md`
- URL: https://www.mdpi.com/2076-3417/15/24/12880
- Host: `www.mdpi.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://www.mdpi.com/2076-3417/15/24/12880
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Use article page PDF control (JS/cookie required).

## #57 `EXSR0419` `2025-2025-Pretrained Models Against Traditional Machine Learning.md`
- URL: https://www.mdpi.com/2079-9292/14/17/3484/pdf
- Host: `www.mdpi.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://www.mdpi.com/2079-9292/14/17/3484/pdf
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Use article page PDF control (JS/cookie required).

## #58 `LSRC0775` `2025-Mohammadi-Cross-Cultural Challenges to Artificial Intelligence Ethics.md`
- URL: https://www.mdpi.com/2813-0324/8/1/21
- Host: `www.mdpi.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://www.mdpi.com/2813-0324/8/1/21
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Use article page PDF control (JS/cookie required).

## #59 `LSRC0700` `2025-Open-Uncensored AI in the Wild Tracking Publicly Available and Locally.md`
- URL: https://www.semanticscholar.org/paper/c53ac0de65a29e9c6a71685a289ba92263ffad80
- Host: `www.semanticscholar.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_202` HTTP `202`
- Example attempted URLs: https://www.semanticscholar.org/paper/c53ac0de65a29e9c6a71685a289ba92263ffad80
- Manual focus: Candidate is metadata/preview page; pivot to publisher/DOI PDF link.
- Next step: Metadata-only page; pivot to DOI/arXiv/publisher links.

## #60 `AUTO_ROURKE2025` `2025-Rourke-Mind Crime.md`
- URL: https://www.goodreads.com/book/show/226055728-mind-crime
- Host: `www.goodreads.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://www.goodreads.com/book/show/226055728-mind-crime
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Metadata page only; pivot to DOI/arXiv/publisher paper.

## #61 `EXSR0338` `2025-Salehi-Blind Faith User Preference and Expert.md`
- URL: https://dl.acm.org/doi/pdf/10.1145/3715275.3732162
- Host: `dl.acm.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://dl.acm.org/doi/pdf/10.1145/3715275.3732162
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Institution login likely required. Open DOI page; use PDF button or author-provided free copy.

## #62 `EXSR0392` `2025-Solidjonov-Investigating linguistic errors in large language.md`
- URL: https://www.tandfonline.com/doi/full/10.1080/23311983.2025.2600519
- Host: `www.tandfonline.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://www.tandfonline.com/doi/full/10.1080/23311983.2025.2600519
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Often auth-gated; use institution login for PDF or accepted manuscript.

## #63 `LSRC0155` `2025-Unknown-Bochun Automatically Annotated Stance Detection Dataset for Sorani.md`
- URL: https://www.semanticscholar.org/paper/6f7dd174a2c2f85e24889005a62de830543ceab0
- Host: `www.semanticscholar.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_202` HTTP `202`
- Example attempted URLs: https://www.semanticscholar.org/paper/6f7dd174a2c2f85e24889005a62de830543ceab0
- Manual focus: Candidate is metadata/preview page; pivot to publisher/DOI PDF link.
- Next step: Metadata-only page; pivot to DOI/arXiv/publisher links.

## #64 `LSRC0704` `2025-Unknown-Cultural Bias in Large Language Models A Comprehensive Analysis and.md`
- URL: https://www.degruyterbrill.com/document/doi/10.1515/jtc-2023-0019/pdf?licenseType=open-access
- Host: `www.degruyterbrill.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_202` HTTP `202`
- Example attempted URLs: https://www.degruyterbrill.com/document/doi/10.1515/jtc-2023-0019/pdf?licenseType=open-access
- Manual focus: Candidate is metadata/preview page; pivot to publisher/DOI PDF link.
- Next step: Open in browser, locate PDF link, verify title, update fields.

## #65 `LSRC0807` `2025-DeWitt Prat-Decolonizing LLMs An Ethnographic Framework for AI in African.md`
- URL: https://www.semanticscholar.org/paper/36c8dca0d6443ea49c08afd16934191c9063326d
- Host: `www.semanticscholar.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_202` HTTP `202`
- Example attempted URLs: https://www.semanticscholar.org/paper/36c8dca0d6443ea49c08afd16934191c9063326d
- Manual focus: Candidate is metadata/preview page; pivot to publisher/DOI PDF link.
- Next step: Metadata-only page; pivot to DOI/arXiv/publisher links.

## #66 `LSRC0286` `2025-Unknown-Leading and Non-Leading Prompts Quantifying Gender Bias in Large.md`
- URL: https://www.sciencedirect.com/science/article/pii/S0950705125009608
- Host: `www.sciencedirect.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://www.sciencedirect.com/science/article/pii/S0950705125009608
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open article page in institutional session and click View PDF.

## #67 `LSRC0629` `2025-Unknown-Optimizing Sentiment Analysis in Multilingual Balanced Datasets A New.md`
- URL: https://www.mdpi.com/2571-5577/8/4/104
- Host: `www.mdpi.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://www.mdpi.com/2571-5577/8/4/104
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Use article page PDF control (JS/cookie required).

## #68 `LSRC0297` `2025-Unknown-TELEIA A Spanish Language Dataset for Evaluating Artificial.md`
- URL: https://namespace.openaire.eu/oaf
- Host: `namespace.openaire.eu`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `curl_return_6` HTTP ``
- Example attempted URLs: https://namespace.openaire.eu/oaf
- Manual focus: Open landing page and locate canonical PDF link.
- Next step: Namespace endpoint is not paper PDF; locate linked repository/publisher record.

## #69 `LSRC0840` `2025-Unknown-The Green Report Three Red Flags That Your LLM Testing Strategy Is.md`
- URL: https://www.thegreenreport.blog/articles/three-red-flags-that-your-llm-testing-strategy-is-too-shallow/three-red-flags-that-your-llm-testing-strategy-is-too-shallow.html
- Host: `www.thegreenreport.blog`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://www.thegreenreport.blog/articles/three-red-flags-that-your-llm-testing-strategy-is-too-shallow/three-red-flags-that-your-llm-testing-strategy-is-too-shallow.html
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open in browser, locate PDF link, verify title, update fields.

