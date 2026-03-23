# Wave12 Remaining 30 Manual Retrieval Checklist

Date: 2026-02-14
Scope: 30 papers that remained without local PDFs after automated and fallback runs.

## Summary
- Total papers: 30
- Metadata marked manual_only: 30
- Current error mix:
  - not_pdf_header (HTTP 200): 18
  - http_403 (HTTP 403): 10
  - http_404 (HTTP 404): 1
  - http_418 (HTTP 418): 1

## Host Groups
### doi.org (9)
Tactics:
- Open DOI in browser and follow redirect to publisher landing page.
- Try publisher PDF/download button with signed-in browser session.
- If paywalled, search accepted manuscript via OpenAlex/Google Scholar/institutional repository.
Papers:
- `2020-Whaanga-Indigenous Protocol and Artificial Intelligence Position.md` | `not_pdf_header HTTP 200` | https://doi.org/10.11573/spectrum.library.concordia.ca.00986506
- `2021-Mghari-Cyberbullying and Hate Speech Detection on.md` | `not_pdf_header HTTP 200` | https://doi.org/10.1016/j.dib.2022.108540
- `2023-Das-Mytho-Annotator An Annotation Tool for Indian.md` | `not_pdf_header HTTP 200` | https://doi.org/10.7717/peerj-cs.1617
- `2024-Kajiwara-Hate Speech and Offensive Language Dataset.md` | `not_pdf_header HTTP 200` | https://doi.org/10.1016/j.ipm.2021.102524
- `2024-Paraschiv-Offensive Text Span Detection in Romanian Comments Using Large.md` | `http_403 HTTP 403` | https://doi.org/10.3390/info15010008
- `2024-Altinel-So-haTRed A Novel Hybrid System for.md` | `not_pdf_header HTTP 200` | https://doi.org/10.1109/access.2024.3415350
- `2024-Khanduja-Telugu Language Hate Speech Detection Using.md` | `not_pdf_header HTTP 200` | https://doi.org/10.1016/j.sasc.2024.200112
- `2025-Sharma-Hate Speech Detection Research in South.md` | `not_pdf_header HTTP 200` | https://doi.org/10.1016/j.knosys.2025.113915
- `2025-Solidjonov-How do LLMs perform on Turkish.md` | `http_403 HTTP 403` | https://doi.org/10.1080/23311983.2025.2600519

### www.mdpi.com (3)
Tactics:
- Open article page in browser and use PDF download button while signed in.
- If blocked by challenge, retry with normal browser session and cookies.
Papers:
- `2024-Toygar-Turkish Offensive Language Detection Dataset.md` | `http_403 HTTP 403` | https://www.mdpi.com/2079-9292/14/24/4919/pdf
- `2024-Rashid-Urdu Toxicity Detection A Multi-Stage and.md` | `http_403 HTTP 403` | https://www.mdpi.com/2673-2688/6/8/194/pdf?version=1755769417
- `2024-team-MahaMarathi-7B Marathi Large Language Model.md` | `http_403 HTTP 403` | https://www.mdpi.com/2079-9292/14/17/3484/pdf?version=1756625048

### arxiv.org (2)
Tactics:
- Open arXiv abs page and download PDF from the page UI.
- Verify paper title matches target before linking.
Papers:
- `2024-Kajiwara-A curated dataset for hate speech detection on social media text - PMC.md` | `not_pdf_header HTTP 200` | http://arxiv.org/abs/2212.12799
- `2024-Moe-Fact Checking in Low-Resource Languages A.md` | `http_404 HTTP 404` | https://arxiv.org/pdf/2406.02169.pdf

### link.springer.com (2)
Tactics:
- Open Springer article/chapter page and download PDF with browser session.
- If paywalled, check Springer SharedIt/accepted manuscript or repository copy.
Papers:
- `2024-Zeng-Proposing Central Asian AI Ethics Principles.md` | `not_pdf_header HTTP 200` | https://link.springer.com/content/pdf/10.1007/s43681-024-00505-7.pdf
- `2025-Ishkhanyan-Ethical considerations in AI-powered language technologies insights.md` | `not_pdf_header HTTP 200` | https://link.springer.com/content/pdf/10.1007/s43681-025-00716-6.pdf

### pmc.ncbi.nlm.nih.gov (2)
Tactics:
- Open article in browser and click PDF button from the page.
- Use delivered PDF URL from browser network tab if direct URL serves HTML to scripts.
Papers:
- `2022-Pollak-Embeddings Models for Buddhist Sanskrit.md` | `not_pdf_header HTTP 200` | https://pmc.ncbi.nlm.nih.gov/articles/PMC10280248/pdf/peerj-cs-08-1128.pdf
- `2024-Akhunzada-Multi-IsnadSet MIS for Sahih Muslim Hadith.md` | `not_pdf_header HTTP 200` | https://pmc.ncbi.nlm.nih.gov/articles/PMC11096860/pdf/main.pdf

### www.techrxiv.org (2)
Tactics:
- Open TechRxiv article page in browser, then click Download PDF.
- If denied, try alternate version (v1/v2) and DOI landing page.
Papers:
- `2023-Akram-ISE-Hate A Benchmark Corpus for Inter-faith.md` | `http_403 HTTP 403` | https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.24106617.v2
- `2025-Unknown-Bilingual Code-Switching Using XLM-RoBERTa.md` | `http_403 HTTP 403` | https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.175756344.42614762/v1

### xplorestaging.ieee.org (2)
Tactics:
- Open IEEE Xplore canonical article page (not xplorestaging) and use institutional login.
- Use DOI or arnumber to locate official PDF endpoint.
- If blocked, search author/preprint copy (HAL/arXiv/institutional repository).
Papers:
- `0000-projects-BaniDB Shabad OS Digital Gurbani Database.md` | `not_pdf_header HTTP 200` | http://xplorestaging.ieee.org/ielx7/8643018/8645960/08646190.pdf?arnumber=864619
- `2018-Nguyen-UIT-VSFC Vietnamese Students' Feedback Corpus for Sentiment Analysis.md` | `not_pdf_header HTTP 200` | http://xplorestaging.ieee.org/ielx7/8553666/8573236/08573337.pdf?arnumber=8573337

### dl.acm.org (1)
Tactics:
- Open ACM article page using institutional login for PDF.
- If paywalled, check author homepage/accepted manuscript repositories.
Papers:
- `2025-Salehi-Blind Faith User Preference and Expert.md` | `http_403 HTTP 403` | https://dl.acm.org/doi/pdf/10.1145/3715275.3732162

### dx.doi.org (1)
Tactics:
- Use https://doi.org form in browser and follow to publisher.
- Attempt OA copy via repository if publisher PDF is blocked.
Papers:
- `2024-Phyo-Development and Evaluation of Myanmar GPT.md` | `http_403 HTTP 403` | http://dx.doi.org/10.2139/ssrn.4871732

### ebooks.iospress.nl (1)
Tactics:
- Open IOS Press chapter landing page and check if PDF is OA or login-gated.
- If gated, locate author manuscript or conference preprint copy.
Papers:
- `2023-Thapa-NEHATE Large-Scale Annotated Data Shedding Light.md` | `not_pdf_header HTTP 200` | https://ebooks.iospress.nl/pdf/doi/10.3233/FAIA230535

### hal.science (1)
Tactics:
- Open HAL record and look for attached full-text file under Documents/Files.
- If no file, use DOI/title search for mirror repositories.
Papers:
- `2019-Unknown-Cross-Platform Evaluation for Italian Hate Speech Detection.md` | `not_pdf_header HTTP 200` | https://hal.science/hal-02381152

### hdl.handle.net (1)
Tactics:
- Open Handle page and follow target repository link to file bitstream.
- Download attached PDF manually from destination repository.
Papers:
- `2023-Bosco-Detecting Racial Stereotypes An Italian Social Media Corpus where.md` | `not_pdf_header HTTP 200` | https://hdl.handle.net/11586/413290

### ieeexplore.ieee.org (1)
Tactics:
- Open article record on IEEE Xplore and use institutional access for PDF.
- If unavailable, search same title in author/institution repositories.
Papers:
- `2024-Yeltay-Kazakh Language Dataset for Hate Speech.md` | `not_pdf_header HTTP 200` | https://ieeexplore.ieee.org/ielx8/10719028/10718863/10719327.pdf

### journals.sagepub.com (1)
Tactics:
- Open SAGE article page with institutional login and download PDF.
- If paywalled, search for accepted manuscript/preprint copy.
Papers:
- `2025-Martinez-Religion and Racial Bias in Artificial.md` | `http_403 HTTP 403` | https://journals.sagepub.com/doi/pdf/10.1177/23780231251377210

### repozitorij.ffzg.unizg.hr (1)
Tactics:
- Open repository landing page and locate direct bitstream download link.
- If anti-bot or tokenized URL, download manually in browser and place into Lit-WS-PDFs/YYYY/.
Papers:
- `2020-Karan-Detecting Hate Speech Online A Case of Croatian.md` | `http_418 HTTP 418` | https://repozitorij.ffzg.unizg.hr/islandora/object/ffzg:892/datastream/FILE0
