# Wave3 Browser-Login Handoff (Remaining Blocked)

- Generated: 2026-02-14 02:05:05
- Blocked items: 38
- Source queue: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/logs/20260214-wave3-browser-interactive-queue.csv`

## Host Buckets
- `PAYWALL_LOGIN`: 16
- `RESOURCE_NOT_PDF`: 13
- `PREPRINT_PORTAL`: 3
- `MIXED_SITE`: 3
- `BLOG_OR_FORUM`: 2
- `NETWORK_PORTAL`: 1

## Host Playbook
### `github.com` (6)
- Bucket: `RESOURCE_NOT_PDF`
- Steps: Open repo page; check README/releases for linked paper DOI/arXiv/PDF.
- Fallback: If no paper PDF exists, mark as resource-page exception (non-PDF artifact).

### `huggingface.co` (6)
- Bucket: `RESOURCE_NOT_PDF`
- Steps: Open dataset/model/space card; check linked paper or arXiv in card metadata/README.
- Fallback: If no paper PDF exists, mark as resource-page exception (non-PDF artifact).

### `link.springer.com` (5)
- Bucket: `PAYWALL_LOGIN`
- Steps: Open `primary_url` while logged in through institution; click `Download PDF`; avoid direct curl-style links outside browser session.
- Fallback: If paywalled, check chapter/article page for author accepted manuscript or repository link; else keep blocked.

### `www.sciencedirect.com` (5)
- Bucket: `PAYWALL_LOGIN`
- Steps: Open article page with institution login; click `View PDF`; check page for author accepted manuscript/open archive links.
- Fallback: If no OA mirror and paywalled, keep blocked.

### `ieeexplore.ieee.org` (3)
- Bucket: `PAYWALL_LOGIN`
- Steps: Open `primary_url` in institutional browser login; click `PDF`/`Download`; if needed open `doi_url`; if needed use `stamp.jsp?arnumber=` from page while logged in.
- Fallback: If no institutional access, search author-uploaded accepted manuscript via Scholar/OpenAlex; otherwise keep blocked.

### `papers.ssrn.com` (2)
- Bucket: `PREPRINT_PORTAL`
- Steps: Open SSRN abstract page and use `Download this paper`; sign in if prompted.
- Fallback: If disabled/unavailable, search title + SSRN ID mirrors.

### `dl.acm.org` (2)
- Bucket: `PAYWALL_LOGIN`
- Steps: Open DOI/landing page with institutional login; click `PDF`; check ACM page for Author-Izer/free copy links.
- Fallback: If blocked, search author pages/repositories for accepted manuscript; else keep blocked.

### `www.researchgate.net` (1)
- Bucket: `NETWORK_PORTAL`
- Steps: Open publication page while logged in; click full-text download if available.
- Fallback: If no direct download, use DOI/Scholar for official or repository copy; do not use request-only links as resolved.

### `www.authorea.com` (1)
- Bucket: `PREPRINT_PORTAL`
- Steps: Open Authorea article page in browser; use `Download`/`Export PDF` and check version history.
- Fallback: If 403 persists, use OpenAlex/Scholar to find mirrored preprint or conference version.

### `forum.effectivealtruism.org` (1)
- Bucket: `BLOG_OR_FORUM`
- Steps: Open post and inspect for linked preprint DOI/arXiv/PDF references.
- Fallback: If post-only content with no paper PDF, mark as non-PDF resource.

### `ljvmiranda921.github.io` (1)
- Bucket: `BLOG_OR_FORUM`
- Steps: Open post and inspect outbound links for arXiv/DOI/PDF.
- Fallback: If no paper linked, mark as non-PDF resource.

### `cke.um.ac.ir` (1)
- Bucket: `MIXED_SITE`
- Steps: Open article page and use native PDF download link in browser (may require JS/cookies).
- Fallback: If inaccessible, search title via Scholar/OpenAlex for mirrors.

### `nilc.icmc.usp.br` (1)
- Bucket: `MIXED_SITE`
- Steps: Open project page and crawl subpages for publication/PDF links.
- Fallback: If only benchmark/task page exists and no paper, mark as non-PDF resource.

### `tjee.tabrizu.ac.ir` (1)
- Bucket: `MIXED_SITE`
- Steps: Open article page and click native `PDF`/download icon in browser session.
- Fallback: If inaccessible, search title via Scholar/OpenAlex for mirrors.

### `www.tandfonline.com` (1)
- Bucket: `PAYWALL_LOGIN`
- Steps: Open article page with institution login; click `Download PDF`; check for accepted manuscript/open version links.
- Fallback: If blocked, look for accepted manuscript on author/institution pages.

### `openai.com` (1)
- Bucket: `RESOURCE_NOT_PDF`
- Steps: Open page and inspect for linked paper/report PDF.
- Fallback: If no standalone paper PDF exists, mark as resource-page exception.

## Paper Checklist
- [ ] `LSRC0230` `2020-Souza-BERTimbau Pretrained BERT Models for Brazilian Portuguese.md`
  Priority: `P1` | Category: `RESEARCHGATE` | Host: `www.researchgate.net`
  Status note: blocked (HTTP 403)
  Primary URL: https://www.researchgate.net/publication/345395208_BERTimbau_Pretrained_BERT_Models_for_Brazilian_Portuguese
  Candidate URLs:
  - https://www.researchgate.net/publication/345395208_BERTimbau_Pretrained_BERT_Models_for_Brazilian_Portuguese
  OpenAlex: https://api.openalex.org/works?search=BERTimbau%3A+Pretrained+BERT+Models+for+Brazilian+Portuguese
  Scholar: https://scholar.google.com/scholar?q=BERTimbau%3A+Pretrained+BERT+Models+for+Brazilian+Portuguese
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0137` `2023-Unknown-Pars-HaO Hate and Offensive Language Detection on Persian Tweets.md`
  Priority: `P1` | Category: `PREPRINT_AUTHOREA` | Host: `www.authorea.com`
  Status note: blocked (HTTP 403)
  Primary URL: https://www.authorea.com/users/581546/articles/683116-pars-hao-hate-and-offensive-language-detection-on-persian-tweets-using-machine-learning-and-deep-learning
  Candidate URLs:
  - https://www.authorea.com/users/581546/articles/683116-pars-hao-hate-and-offensive-language-detection-on-persian-tweets-using-machine-learning-and-deep-learning
  OpenAlex: https://api.openalex.org/works?search=Pars-HaO%3A+Hate+and+Offensive+Language+Detection+on+Persian+Tweets+Using+Machine+Learning+and+Deep+Learning
  Scholar: https://scholar.google.com/scholar?q=Pars-HaO%3A+Hate+and+Offensive+Language+Detection+on+Persian+Tweets+Using+Machine+Learning+and+Deep+Learning
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0274` `2025-Unknown-BenchMoral A Benchmarking to Assess the Moral Sensitivity of Large.md`
  Priority: `P2` | Category: `MIXED_OR_UNKNOWN` | Host: `forum.effectivealtruism.org`
  Status note: blocked (not_pdf_header)
  Primary URL: https://forum.effectivealtruism.org/posts/eTEtMc2d38GDZZ8ke/benchmoral-a-benchmarking-to-assess-the-moral-sensitivity-of
  OpenAlex: https://api.openalex.org/works?search=BenchMoral%3A+A+Benchmarking+to+Assess+the+Moral+Sensitivity+of+Large+Language+Models+%28LLMs%29+in+Spanish
  Scholar: https://scholar.google.com/scholar?q=BenchMoral%3A+A+Benchmarking+to+Assess+the+Moral+Sensitivity+of+Large+Language+Models+%28LLMs%29+in+Spanish
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0127` `2024-Miranda-Desiderata for Filipino NLP in the Age of LLMs.md`
  Priority: `P2` | Category: `MIXED_OR_UNKNOWN` | Host: `ljvmiranda921.github.io`
  Status note: blocked (manual-auth rejected_verification)
  Primary URL: https://ljvmiranda921.github.io/notebook/2024/12/17/filipino-llm/
  Candidate URLs:
  - https://ljvmiranda921.github.io/notebook/2024/12/17/filipino-llm/
  OpenAlex: https://api.openalex.org/works?search=Desiderata+for+Filipino+NLP+in+the+Age+of+LLMs
  Scholar: https://scholar.google.com/scholar?q=Desiderata+for+Filipino+NLP+in+the+Age+of+LLMs
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0138` `2025-Jafarinejad-PerGOLD Identification of Offensive Language in Persian Tweets.md`
  Priority: `P2` | Category: `MIXED_OR_UNKNOWN` | Host: `cke.um.ac.ir`
  Status note: blocked (not_pdf_header)
  Primary URL: https://cke.um.ac.ir/article_46412.html
  OpenAlex: https://api.openalex.org/works?search=PerGOLD%3A+Identification+of+Offensive+Language+in+Persian+Tweets%3A+Leveraging+Crowdsourcing
  Scholar: https://scholar.google.com/scholar?q=PerGOLD%3A+Identification+of+Offensive+Language+in+Persian+Tweets%3A+Leveraging+Crowdsourcing
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0220` `2016-Fonseca-ASSIN Avaliação de Similaridade Semântica e INferência textual.md`
  Priority: `P2` | Category: `MIXED_OR_UNKNOWN` | Host: `nilc.icmc.usp.br`
  Status note: blocked (HTTP 301)
  Primary URL: http://nilc.icmc.usp.br/assin/
  OpenAlex: https://api.openalex.org/works?search=ASSIN%3A+Avalia%C3%A7%C3%A3o+de+Similaridade+Sem%C3%A2ntica+e+INfer%C3%AAncia+textual
  Scholar: https://scholar.google.com/scholar?q=ASSIN%3A+Avalia%C3%A7%C3%A3o+de+Similaridade+Sem%C3%A2ntica+e+INfer%C3%AAncia+textual
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0139` `2023-Khodabakhsh-PerBOLD A Big Dataset of Persian Offensive Language on Instagram.md`
  Priority: `P2` | Category: `MIXED_OR_UNKNOWN` | Host: `tjee.tabrizu.ac.ir`
  Status note: blocked (HTTP 000)
  Primary URL: https://tjee.tabrizu.ac.ir/article_15794.html
  OpenAlex: https://api.openalex.org/works?search=PerBOLD%3A+A+Big+Dataset+of+Persian+Offensive+Language+on+Instagram+Comments
  Scholar: https://scholar.google.com/scholar?q=PerBOLD%3A+A+Big+Dataset+of+Persian+Offensive+Language+on+Instagram+Comments
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0019` `2018-Liebeskind-Identifying Abusive Comments in Hebrew Facebook.md`
  Priority: `P2` | Category: `PAYWALL_IEEE` | Host: `ieeexplore.ieee.org`
  Status note: blocked (doi-mirror no_verified_pdf)
  Primary URL: https://ieeexplore.ieee.org/document/8646190
  DOI: https://doi.org/10.1109/ICSEE.2018.8646190
  Candidate URLs:
  - https://ieeexplore.ieee.org/document/8646190
  - https://doi.org/10.1109/ICSEE.2018.8646190
  - https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8646190
  OpenAlex: https://api.openalex.org/works?search=Identifying+Abusive+Comments+in+Hebrew+Facebook
  Scholar: https://scholar.google.com/scholar?q=Identifying+Abusive+Comments+in+Hebrew+Facebook
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0136` `2022-Ataei-Pars-OFF A Benchmark for Offensive Language Detection on Farsi Social.md`
  Priority: `P2` | Category: `PAYWALL_IEEE` | Host: `ieeexplore.ieee.org`
  Status note: blocked (doi-mirror no_verified_pdf)
  Primary URL: https://ieeexplore.ieee.org/document/9936700
  DOI: https://doi.org/10.1109/taffc.2022.3219229
  Candidate URLs:
  - https://ieeexplore.ieee.org/document/9936700
  - https://doi.org/10.1109/taffc.2022.3219229
  - https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9936700
  OpenAlex: https://api.openalex.org/works?search=Pars-OFF%3A+A+Benchmark+for+Offensive+Language+Detection+on+Farsi+Social+Media
  Scholar: https://scholar.google.com/scholar?q=Pars-OFF%3A+A+Benchmark+for+Offensive+Language+Detection+on+Farsi+Social+Media
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0192` `2020-Unknown-Sinhala Hate Speech Detection in Social Media using Text Mining and.md`
  Priority: `P2` | Category: `PAYWALL_IEEE` | Host: `ieeexplore.ieee.org`
  Status note: blocked (doi-mirror no_verified_pdf)
  Primary URL: https://ieeexplore.ieee.org/document/9023655/
  DOI: https://doi.org/10.1109/MERCon50084.2020.9023655
  Candidate URLs:
  - https://ieeexplore.ieee.org/document/9023655/
  - https://doi.org/10.1109/MERCon50084.2020.9023655
  - https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9023655
  - https://ieeexplore.ieee.org/document/9023655
  OpenAlex: https://api.openalex.org/works?search=Sinhala+Hate+Speech+Detection+in+Social+Media+using+Text+Mining+and+Machine+Learning
  Scholar: https://scholar.google.com/scholar?q=Sinhala+Hate+Speech+Detection+in+Social+Media+using+Text+Mining+and+Machine+Learning
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0069` `2024-Younas-Proposing Central Asian AI Ethics Principles A Multilevel Approach.md`
  Priority: `P2` | Category: `PAYWALL_SPRINGER` | Host: `link.springer.com`
  Status note: blocked (doi-mirror no_verified_pdf)
  Primary URL: https://link.springer.com/article/10.1007/s43681-024-00505-7
  DOI: https://doi.org/10.1007/s43681-024-00505-7
  Candidate URLs:
  - https://link.springer.com/article/10.1007/s43681-024-00505-7
  - https://doi.org/10.1007/s43681-024-00505-7
  - https://link.springer.com/content/pdf/10.1007/s43681-024-00505-7.pdf?download=1
  - https://link.springer.com/content/pdf/10.1007/s43681-024-00505-7.pdf
  OpenAlex: https://api.openalex.org/works?search=Proposing+Central+Asian+AI+Ethics+Principles%3A+A+Multilevel+Approach+for+Responsible+AI
  Scholar: https://scholar.google.com/scholar?q=Proposing+Central+Asian+AI+Ethics+Principles%3A+A+Multilevel+Approach+for+Responsible+AI
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0151` `2022-Saeed-Hate Speech Detection in Social Media for the Kurdish Language.md`
  Priority: `P2` | Category: `PAYWALL_SPRINGER` | Host: `link.springer.com`
  Status note: blocked (doi-mirror no_verified_pdf)
  Primary URL: https://link.springer.com/chapter/10.1007/978-3-031-14054-9_24
  DOI: https://doi.org/10.1007/978-3-031-14054-9_24
  Candidate URLs:
  - https://link.springer.com/chapter/10.1007/978-3-031-14054-9_24
  - https://doi.org/10.1007/978-3-031-14054-9_24
  - https://link.springer.com/content/pdf/10.1007/978-3-031-14054-9_24.pdf?download=1
  - https://link.springer.com/content/pdf/10.1007/978-3-031-14054-9_24.pdf
  OpenAlex: https://api.openalex.org/works?search=Hate+Speech+Detection+in+Social+Media+for+the+Kurdish+Language
  Scholar: https://scholar.google.com/scholar?q=Hate+Speech+Detection+in+Social+Media+for+the+Kurdish+Language
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0152` `2023-Badawi-KurdiSent A Corpus for Kurdish Sentiment Analysis.md`
  Priority: `P2` | Category: `PAYWALL_SPRINGER` | Host: `link.springer.com`
  Status note: blocked (doi-mirror no_verified_pdf)
  Primary URL: https://link.springer.com/article/10.1007/s10579-023-09716-6
  DOI: https://doi.org/10.1007/s10579-023-09716-6
  Candidate URLs:
  - https://link.springer.com/article/10.1007/s10579-023-09716-6
  - https://doi.org/10.1007/s10579-023-09716-6
  - https://link.springer.com/content/pdf/10.1007/s10579-023-09716-6.pdf?download=1
  - https://link.springer.com/content/pdf/10.1007/s10579-023-09716-6.pdf
  OpenAlex: https://api.openalex.org/works?search=KurdiSent%3A+A+Corpus+for+Kurdish+Sentiment+Analysis
  Scholar: https://scholar.google.com/scholar?q=KurdiSent%3A+A+Corpus+for+Kurdish+Sentiment+Analysis
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0208` `2024-Trajano-OLID-BR Offensive Language Identification Dataset for Brazilian.md`
  Priority: `P2` | Category: `PAYWALL_SPRINGER` | Host: `link.springer.com`
  Status note: blocked (doi-mirror no_verified_pdf)
  Primary URL: https://link.springer.com/article/10.1007/s10579-023-09657-0
  DOI: https://doi.org/10.1007/s10579-023-09657-0
  Candidate URLs:
  - https://link.springer.com/article/10.1007/s10579-023-09657-0
  - https://doi.org/10.1007/s10579-023-09657-0
  - https://link.springer.com/content/pdf/10.1007/s10579-023-09657-0.pdf?download=1
  - https://link.springer.com/content/pdf/10.1007/s10579-023-09657-0.pdf
  OpenAlex: https://api.openalex.org/works?search=OLID-BR%3A+Offensive+Language+Identification+Dataset+for+Brazilian+Portuguese
  Scholar: https://scholar.google.com/scholar?q=OLID-BR%3A+Offensive+Language+Identification+Dataset+for+Brazilian+Portuguese
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0232` `2024-CiTIUS-A Galician-Portuguese Generative Model.md`
  Priority: `P2` | Category: `PAYWALL_SPRINGER` | Host: `link.springer.com`
  Status note: blocked (doi-mirror no_verified_pdf)
  Primary URL: https://link.springer.com/chapter/10.1007/978-3-031-73503-5_24
  DOI: https://doi.org/10.1007/978-3-031-73503-5_24
  Candidate URLs:
  - https://link.springer.com/chapter/10.1007/978-3-031-73503-5_24
  - https://doi.org/10.1007/978-3-031-73503-5_24
  - https://link.springer.com/content/pdf/10.1007/978-3-031-73503-5_24.pdf?download=1
  - https://link.springer.com/content/pdf/10.1007/978-3-031-73503-5_24.pdf
  OpenAlex: https://api.openalex.org/works?search=A+Galician-Portuguese+Generative+Model
  Scholar: https://scholar.google.com/scholar?q=A+Galician-Portuguese+Generative+Model
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0083` `2024-Thu-Development and Evaluation of Myanmar GPT A Language Model for.md`
  Priority: `P2` | Category: `PREPRINT_SSRN` | Host: `papers.ssrn.com`
  Status note: blocked (HTTP 403)
  Primary URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4871732
  Candidate URLs:
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4871732
  OpenAlex: https://api.openalex.org/works?search=Development+and+Evaluation+of+Myanmar+GPT%3A+A+Language+Model+for+Myanmar+Natural+Language+Processing
  Scholar: https://scholar.google.com/scholar?q=Development+and+Evaluation+of+Myanmar+GPT%3A+A+Language+Model+for+Myanmar+Natural+Language+Processing
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0165` `2024-Khan-From Tradition to Technology A Systematic Survey on Navigating Pashto.md`
  Priority: `P2` | Category: `PREPRINT_SSRN` | Host: `papers.ssrn.com`
  Status note: blocked (HTTP 403)
  Primary URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031721
  Candidate URLs:
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031721
  OpenAlex: https://api.openalex.org/works?search=From+Tradition+to+Technology%3A+A+Systematic+Survey+on+Navigating+Pashto+in+Modern+NLP
  Scholar: https://scholar.google.com/scholar?q=From+Tradition+to+Technology%3A+A+Systematic+Survey+on+Navigating+Pashto+in+Modern+NLP
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0057` `2025-Deepawali-Hate Speech Detection Research in South Asian Languages A Survey of.md`
  Priority: `P3` | Category: `PAYWALL_ACM` | Host: `dl.acm.org`
  Status note: blocked (doi-mirror no_verified_pdf)
  Primary URL: https://dl.acm.org/doi/10.1145/3711710
  DOI: https://doi.org/10.1145/3711710
  Candidate URLs:
  - https://dl.acm.org/doi/10.1145/3711710
  - https://doi.org/10.1145/3711710
  - https://dl.acm.org/doi/pdf/10.1145/3711710
  OpenAlex: https://api.openalex.org/works?search=Hate+Speech+Detection+Research+in+South+Asian+Languages%3A+A+Survey+of+Tasks%2C+Datasets+and+Methods
  Scholar: https://scholar.google.com/scholar?q=Hate+Speech+Detection+Research+in+South+Asian+Languages%3A+A+Survey+of+Tasks%2C+Datasets+and+Methods
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0199` `2025-Wasi-Dialectal Bias in Bengali An Evaluation of Multilingual Language.md`
  Priority: `P3` | Category: `PAYWALL_ACM` | Host: `dl.acm.org`
  Status note: blocked (doi-mirror no_verified_pdf)
  Primary URL: https://dl.acm.org/doi/10.1145/3701716.3715468
  DOI: https://doi.org/10.1145/3701716.3715468
  Candidate URLs:
  - https://dl.acm.org/doi/10.1145/3701716.3715468
  - https://doi.org/10.1145/3701716.3715468
  - https://dl.acm.org/doi/pdf/10.1145/3701716.3715468
  OpenAlex: https://api.openalex.org/works?search=Dialectal+Bias+in+Bengali%3A+An+Evaluation+of+Multilingual+Language+Models
  Scholar: https://scholar.google.com/scholar?q=Dialectal+Bias+in+Bengali%3A+An+Evaluation+of+Multilingual+Language+Models
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0126` `2023-Unknown-Hate speech and abusive language detection in Indonesian social media.md`
  Priority: `P3` | Category: `PAYWALL_ELSEVIER` | Host: `www.sciencedirect.com`
  Status note: blocked (HTTP 403)
  Primary URL: https://www.sciencedirect.com/science/article/pii/S2405844023058553
  Candidate URLs:
  - https://www.sciencedirect.com/science/article/pii/S2405844023058553
  - https://www.sciencedirect.com/science/article/pii/S2405844023058553/pdf
  - https://www.sciencedirect.com/science/article/pii/S2405844023058553/pdfft?isDTMRedir=true&download=true
  - https://www.sciencedirect.com/science/article/pii/S2405844023058553/pdfft?download=true
  - https://www.cell.com/article/S2405844023058553/pdf
  OpenAlex: https://api.openalex.org/works?search=Hate+speech+and+abusive+language+detection+in+Indonesian+social+media%3A+Progress+and+challenges
  Scholar: https://scholar.google.com/scholar?q=Hate+speech+and+abusive+language+detection+in+Indonesian+social+media%3A+Progress+and+challenges
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0155` `2025-Unknown-Bochun Automatically Annotated Stance Detection Dataset for Sorani.md`
  Priority: `P3` | Category: `PAYWALL_ELSEVIER` | Host: `www.sciencedirect.com`
  Status note: blocked (HTTP 403)
  Primary URL: https://www.sciencedirect.com/science/article/pii/S2352340925005669
  Candidate URLs:
  - https://www.sciencedirect.com/science/article/pii/S2352340925005669
  - https://www.sciencedirect.com/science/article/pii/S2352340925005669/pdf
  - https://www.sciencedirect.com/science/article/pii/S2352340925005669/pdfft?isDTMRedir=true&download=true
  - https://www.sciencedirect.com/science/article/pii/S2352340925005669/pdfft?download=true
  - https://www.cell.com/article/S2352340925005669/pdf
  OpenAlex: https://api.openalex.org/works?search=Bochun%3A+Automatically+Annotated+Stance+Detection+Dataset+for+Sorani+Kurdish+Language
  Scholar: https://scholar.google.com/scholar?q=Bochun%3A+Automatically+Annotated+Stance+Detection+Dataset+for+Sorani+Kurdish+Language
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0270` `2025-Unknown-Towards Realistic Evaluation of Cultural Value Alignment in Large.md`
  Priority: `P3` | Category: `PAYWALL_ELSEVIER` | Host: `www.sciencedirect.com`
  Status note: blocked (doi-mirror no_verified_pdf)
  Primary URL: https://www.sciencedirect.com/science/article/abs/pii/S030645732500041X
  DOI: https://doi.org/10.1016/j.techfore.2025.123XX
  Candidate URLs:
  - https://www.sciencedirect.com/science/article/abs/pii/S030645732500041X
  OpenAlex: https://api.openalex.org/works?search=Towards+Realistic+Evaluation+of+Cultural+Value+Alignment+in+Large+Language+Models%3A+Diversity+Enhancement+for+Survey+Response+Simulation
  Scholar: https://scholar.google.com/scholar?q=Towards+Realistic+Evaluation+of+Cultural+Value+Alignment+in+Large+Language+Models%3A+Diversity+Enhancement+for+Survey+Response+Simulation
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0286` `2025-Unknown-Leading and Non-Leading Prompts Quantifying Gender Bias in Large.md`
  Priority: `P3` | Category: `PAYWALL_ELSEVIER` | Host: `www.sciencedirect.com`
  Status note: blocked (HTTP 403)
  Primary URL: https://www.sciencedirect.com/science/article/pii/S0950705125009608
  Candidate URLs:
  - https://www.sciencedirect.com/science/article/pii/S0950705125009608
  - https://www.sciencedirect.com/science/article/pii/S0950705125009608/pdf
  - https://www.sciencedirect.com/science/article/pii/S0950705125009608/pdfft?isDTMRedir=true&download=true
  - https://www.sciencedirect.com/science/article/pii/S0950705125009608/pdfft?download=true
  - https://www.cell.com/article/S0950705125009608/pdf
  OpenAlex: https://api.openalex.org/works?search=Leading+and+Non-Leading+Prompts%3A+Quantifying+Gender+Bias+in+Large+Language+Models+through+BiasBloom+Corpus
  Scholar: https://scholar.google.com/scholar?q=Leading+and+Non-Leading+Prompts%3A+Quantifying+Gender+Bias+in+Large+Language+Models+through+BiasBloom+Corpus
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0297` `2025-Unknown-TELEIA A Spanish Language Dataset for Evaluating Artificial.md`
  Priority: `P3` | Category: `PAYWALL_ELSEVIER` | Host: `www.sciencedirect.com`
  Status note: blocked (HTTP 403)
  Primary URL: https://www.sciencedirect.com/science/article/pii/S2352340925001696
  Candidate URLs:
  - https://www.sciencedirect.com/science/article/pii/S2352340925001696
  - https://www.sciencedirect.com/science/article/pii/S2352340925001696/pdf
  - https://www.sciencedirect.com/science/article/pii/S2352340925001696/pdfft?isDTMRedir=true&download=true
  - https://www.sciencedirect.com/science/article/pii/S2352340925001696/pdfft?download=true
  - https://www.cell.com/article/S2352340925001696/pdf
  OpenAlex: https://api.openalex.org/works?search=TELEIA%3A+A+Spanish+Language+Dataset+for+Evaluating+Artificial+Intelligence+Models
  Scholar: https://scholar.google.com/scholar?q=TELEIA%3A+A+Spanish+Language+Dataset+for+Evaluating+Artificial+Intelligence+Models
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0072` `2025-Göçen-Teachers vs. large language models ethical decision-making across.md`
  Priority: `P3` | Category: `PAYWALL_TANDF` | Host: `www.tandfonline.com`
  Status note: blocked (doi-mirror no_verified_pdf)
  Primary URL: https://www.tandfonline.com/doi/full/10.1080/10508422.2025.2581274
  DOI: https://doi.org/10.1080/10508422.2025.2581274
  Candidate URLs:
  - https://www.tandfonline.com/doi/full/10.1080/10508422.2025.2581274
  - https://doi.org/10.1080/10508422.2025.2581274
  - https://www.tandfonline.com/doi/pdf/10.1080/10508422.2025.2581274
  OpenAlex: https://api.openalex.org/works?search=Teachers+vs.+large+language+models%3A+ethical+decision-making+across+educational+dilemmas+in+Turkish+schools
  Scholar: https://scholar.google.com/scholar?q=Teachers+vs.+large+language+models%3A+ethical+decision-making+across+educational+dilemmas+in+Turkish+schools
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0140` `2024-Hadi-The Dark Side of Instagram A Large Dataset for Identifying Persian.md`
  Priority: `P4` | Category: `RESOURCE_PAGE_NO_PDF` | Host: `github.com`
  Status note: blocked (not_pdf_header)
  Primary URL: https://github.com/davardoust/PHICAD
  Candidate URLs:
  - https://github.com/davardoust/PHICAD
  OpenAlex: https://api.openalex.org/works?search=The+Dark+Side+of+Instagram%3A+A+Large+Dataset+for+Identifying+Persian+Harmful+Comments+%28PHICAD%29
  Scholar: https://scholar.google.com/scholar?q=The+Dark+Side+of+Instagram%3A+A+Large+Dataset+for+Identifying+Persian+Harmful+Comments+%28PHICAD%29
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0144` `2024-Baruni-ParsBench Toolkits for Benchmarking LLMs Based on the Persian.md`
  Priority: `P4` | Category: `RESOURCE_PAGE_NO_PDF` | Host: `github.com`
  Status note: blocked (not_pdf_header)
  Primary URL: https://github.com/ParsBench/ParsBench
  Candidate URLs:
  - https://github.com/ParsBench/ParsBench
  OpenAlex: https://api.openalex.org/works?search=ParsBench%3A+Toolkits+for+Benchmarking+LLMs+Based+on+the+Persian+Language+Tasks
  Scholar: https://scholar.google.com/scholar?q=ParsBench%3A+Toolkits+for+Benchmarking+LLMs+Based+on+the+Persian+Language+Tasks
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0196` `2025-Unknown-BharatBench Comprehensive Multilingual Multimodal Evaluations.md`
  Priority: `P4` | Category: `RESOURCE_PAGE_NO_PDF` | Host: `github.com`
  Status note: blocked (not_pdf_header)
  Primary URL: https://github.com/ola-krutrim/BharatBench
  Candidate URLs:
  - https://github.com/ola-krutrim/BharatBench
  OpenAlex: https://api.openalex.org/works?search=BharatBench%3A+Comprehensive+Multilingual+Multimodal+Evaluations
  Scholar: https://scholar.google.com/scholar?q=BharatBench%3A+Comprehensive+Multilingual+Multimodal+Evaluations
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0221` `2024-Chaves-Napolab The Natural Portuguese Language Benchmark.md`
  Priority: `P4` | Category: `RESOURCE_PAGE_NO_PDF` | Host: `github.com`
  Status note: blocked (not_pdf_header)
  Primary URL: https://github.com/ruanchaves/napolab
  Candidate URLs:
  - https://github.com/ruanchaves/napolab
  OpenAlex: https://api.openalex.org/works?search=Napolab%3A+The+Natural+Portuguese+Language+Benchmark
  Scholar: https://scholar.google.com/scholar?q=Napolab%3A+The+Natural+Portuguese+Language+Benchmark
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0339` `2019-Ptaszynski-Results of the PolEval 2019 Shared Task 6 First Dataset and Open.md`
  Priority: `P4` | Category: `RESOURCE_PAGE_NO_PDF` | Host: `github.com`
  Status note: blocked (not_pdf_header)
  Primary URL: https://github.com/ptaszynski/cyberbullying-Polish
  Candidate URLs:
  - https://github.com/ptaszynski/cyberbullying-Polish
  OpenAlex: https://api.openalex.org/works?search=Results+of+the+PolEval+2019+Shared+Task+6%3A+First+Dataset+and+Open+Shared+Task+for+Automatic+Cyberbullying+Detection+in+Polish+Twitter
  Scholar: https://scholar.google.com/scholar?q=Results+of+the+PolEval+2019+Shared+Task+6%3A+First+Dataset+and+Open+Shared+Task+for+Automatic+Cyberbullying+Detection+in+Polish+Twitter
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0345` `2024-Gordic-Serbian LLM Evaluation Dataset.md`
  Priority: `P4` | Category: `RESOURCE_PAGE_NO_PDF` | Host: `github.com`
  Status note: blocked (not_pdf_header)
  Primary URL: https://github.com/gordicaleksa/serbian-llm-eval
  Candidate URLs:
  - https://github.com/gordicaleksa/serbian-llm-eval
  OpenAlex: https://api.openalex.org/works?search=Serbian+LLM+Evaluation+Dataset
  Scholar: https://scholar.google.com/scholar?q=Serbian+LLM+Evaluation+Dataset
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0022` `2025-Dementieva-TextDetox Multilingual Toxicity Dataset.md`
  Priority: `P4` | Category: `RESOURCE_PAGE_NO_PDF` | Host: `huggingface.co`
  Status note: blocked (not_pdf_header)
  Primary URL: https://huggingface.co/datasets/textdetox/multilingual_toxicity_dataset
  Candidate URLs:
  - https://huggingface.co/datasets/textdetox/multilingual_toxicity_dataset
  OpenAlex: https://api.openalex.org/works?search=TextDetox+Multilingual+Toxicity+Dataset
  Scholar: https://scholar.google.com/scholar?q=TextDetox+Multilingual+Toxicity+Dataset
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0042` `2024-community-Open Leaderboard for Hebrew LLMs.md`
  Priority: `P4` | Category: `RESOURCE_PAGE_NO_PDF` | Host: `huggingface.co`
  Status note: blocked (not_pdf_header)
  Primary URL: https://huggingface.co/blog/leaderboard-hebrew
  Candidate URLs:
  - https://huggingface.co/blog/leaderboard-hebrew
  OpenAlex: https://api.openalex.org/works?search=Open+Leaderboard+for+Hebrew+LLMs
  Scholar: https://scholar.google.com/scholar?q=Open+Leaderboard+for+Hebrew+LLMs
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0059` `2022-Hate-speech-CNERG-Kannada Code-Mixed Abusive Speech Detection MuRIL-based.md`
  Priority: `P4` | Category: `RESOURCE_PAGE_NO_PDF` | Host: `huggingface.co`
  Status note: blocked (not_pdf_header)
  Primary URL: https://huggingface.co/Hate-speech-CNERG/kannada-codemixed-abusive-MuRIL
  Candidate URLs:
  - https://huggingface.co/Hate-speech-CNERG/kannada-codemixed-abusive-MuRIL
  OpenAlex: https://api.openalex.org/works?search=Kannada+Code-Mixed+Abusive+Speech+Detection+%28MuRIL-based%29
  Scholar: https://scholar.google.com/scholar?q=Kannada+Code-Mixed+Abusive+Speech+Detection+%28MuRIL-based%29
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0149` `2025-Unknown-MIZAN A Persian LLM Leaderboard.md`
  Priority: `P4` | Category: `RESOURCE_PAGE_NO_PDF` | Host: `huggingface.co`
  Status note: blocked (not_pdf_header)
  Primary URL: https://huggingface.co/spaces/MCINext/mizan-llm-leaderboard
  Candidate URLs:
  - https://huggingface.co/spaces/MCINext/mizan-llm-leaderboard
  OpenAlex: https://api.openalex.org/works?search=MIZAN%3A+A+Persian+LLM+Leaderboard
  Scholar: https://scholar.google.com/scholar?q=MIZAN%3A+A+Persian+LLM+Leaderboard
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0200` `2024-Aupi-WoNBias A Complete Bengali Gender Bias Dataset.md`
  Priority: `P4` | Category: `RESOURCE_PAGE_NO_PDF` | Host: `huggingface.co`
  Status note: blocked (not_pdf_header)
  Primary URL: https://huggingface.co/datasets/gender-bias-bengali/wonbias-complete-dataset
  Candidate URLs:
  - https://huggingface.co/datasets/gender-bias-bengali/wonbias-complete-dataset
  OpenAlex: https://api.openalex.org/works?search=WoNBias%3A+A+Complete+Bengali+Gender+Bias+Dataset
  Scholar: https://scholar.google.com/scholar?q=WoNBias%3A+A+Complete+Bengali+Gender+Bias+Dataset
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0222` `2024-Garcia-Open Portuguese LLM Leaderboard.md`
  Priority: `P4` | Category: `RESOURCE_PAGE_NO_PDF` | Host: `huggingface.co`
  Status note: blocked (not_pdf_header)
  Primary URL: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard
  Candidate URLs:
  - https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard
  OpenAlex: https://api.openalex.org/works?search=Open+Portuguese+LLM+Leaderboard
  Scholar: https://scholar.google.com/scholar?q=Open+Portuguese+LLM+Leaderboard
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

- [ ] `LSRC0185` `2025-Unknown-IndQA A Culture-Aware Benchmark for Indian Languages.md`
  Priority: `P4` | Category: `RESOURCE_PAGE_NO_PDF` | Host: `openai.com`
  Status note: blocked (HTTP 403)
  Primary URL: https://openai.com/index/introducing-indqa/
  OpenAlex: https://api.openalex.org/works?search=IndQA%3A+A+Culture-Aware+Benchmark+for+Indian+Languages
  Scholar: https://scholar.google.com/scholar?q=IndQA%3A+A+Culture-Aware+Benchmark+for+Indian+Languages
  Success criteria: Save valid PDF (starts with %PDF) and confirm title match, then update `external_pdf`, `local_pdf`, and `pdf_extract`.
