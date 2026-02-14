# P2 Manual Browser Execution Plan

Generated: 2026-02-14T07:45:38

Execute in order. For each item: open URL in browser, download verified PDF, then update `external_pdf`, `local_pdf`, and `pdf_extract`.

## #1 `EXSR0499` `2024-Yeltay-Kazakh Language Dataset for Hate Speech.md`
- URL: https://doi.org/10.1109/iccia62557.2024.10719327
- Host: `ieeexplore.ieee.org`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://doi.org/10.1109/iccia62557.2024.10719327 | http://xplorestaging.ieee.org/ielx8/10719028/10718863/10719327.pdf?arnumber=10719327
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Use DOI/landing page and click PDF with institutional login.

## #2 `EXSR0518` `2024-Younas-Proposing Central Asian AI Ethics Principles A Multilevel Approach.md`
- URL: https://link.springer.com/content/pdf/10.1007/s43681-024-00505-7.pdf
- Host: `link.springer.com`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://link.springer.com/content/pdf/10.1007/s43681-024-00505-7.pdf | https://link.springer.com/article/10.1007/s43681-024-00505-7/fulltext.html
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open article/chapter page first, then use Download PDF in browser session. If blocked, capture accepted manuscript link.

## #3 `EXSR0421` `2025-Martinez-Religion and Racial Bias in Artificial.md`
- URL: https://doaj.org/article/b7706dcd2a334756a56cb8bcc7c6c354
- Host: `doaj.org`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://doaj.org/article/b7706dcd2a334756a56cb8bcc7c6c354 | https://doi.org/10.1177/23780231251377210
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open DOAJ record and follow Full Text link to publisher PDF.

## #4 `LSRC0831` `2025-Unknown-Bilingual Code-Switching Using XLM-RoBERTa.md`
- URL: https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.175756344.42614762/v1
- Host: `www.techrxiv.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.175756344.42614762/v1 | https://doi.org/10.36227/techrxiv.175756344.42614762/v1
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Open DOI page and use PDF download in browser session.

## #5 `EXSR0550` `2023-University-Antisemitism on Twitter A Dataset for.md`
- URL: https://doi.org/10.5281/zenodo.7932888
- Host: `zenodo.org`
- Reason to prioritize: already resolves to live landing page; responded with HTTP 200
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://doi.org/10.5281/zenodo.7932888
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Use Files section for direct PDF download URL.

## #6 `EXSR0474` `2024-Phyo-Development and Evaluation of Myanmar GPT.md`
- URL: http://dx.doi.org/10.2139/ssrn.4871732
- Host: `papers.ssrn.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: http://dx.doi.org/10.2139/ssrn.4871732 | https://doi.org/10.2139/ssrn.4871732
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Open abstract page and use Download this paper; sign-in may be required.

## #7 `AUTO_OCHASI2025` `2025-Ochasi-Reframing Justice in Healthcare AI.md`
- URL: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/dewb.70007
- Host: `onlinelibrary.wiley.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/dewb.70007 | https://onlinelibrary.wiley.com/doi/pdf/10.1111/dewb.70007
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Open DOI landing page and use PDF/PDFDirect with browser cookies.

## #8 `EXSR0620` `0000-projects-BaniDB Shabad OS Digital Gurbani Database.md`
- URL: https://xplorestaging.ieee.org/ielx7/8643018/8645960/08646190.pdf?arnumber=864619
- Host: `xplorestaging.ieee.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://xplorestaging.ieee.org/ielx7/8643018/8645960/08646190.pdf?arnumber=864619
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Use real IEEE Xplore page when possible; staging links may be unstable. Use institutional login for PDF.

## #9 `EXSR0602` `2021-Mghari-Cyberbullying and Hate Speech Detection on.md`
- URL: https://namespace.openaire.eu/oaf
- Host: `namespace.openaire.eu`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `curl_return_6` HTTP ``
- Example attempted URLs: https://namespace.openaire.eu/oaf
- Manual focus: Open landing page and locate canonical PDF link.
- Next step: Metadata-only namespace endpoint. Find linked repository/publisher page.

## #10 `EXSR0559` `2023-[[Unknown]]-ISE-Hate A Benchmark Corpus for Inter-faith.md`
- URL: https://www.sciencedirect.com/science/article/abs/pii/S0306457323000079
- Host: `www.sciencedirect.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://www.sciencedirect.com/science/article/abs/pii/S0306457323000079
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Open article page in institutional session and click View PDF.

## #11 `EXSR0480` `2024-Moe-Fact Checking in Low-Resource Languages A.md`
- URL: https://www.yorku.ca/research/ycar/events/fact-checking-dataset-transformer-model-burmese-language-lwin-moe-13112024/
- Host: `www.yorku.ca`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `` HTTP ``
- Manual focus: Queue filename stale; update to current paper filename before retry.
- Next step: Event/landing page; follow outbound links (usually arXiv/repository) for PDF.

## #12 `EXSR0537` `2024-Toygar-Turkish Offensive Language Detection Dataset.md`
- URL: https://huggingface.co/datasets/Toygar/turkish-offensive-language-detection
- Host: `huggingface.co`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://huggingface.co/datasets/Toygar/turkish-offensive-language-detection
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Resource page. Find linked paper DOI/arXiv in model/dataset card.

## #13 `EXSR0543` `2024-[[Unknown]]-Urdu Toxicity Detection A Multi-Stage and.md`
- URL: https://www.mdpi.com/2673-2688/6/8/194
- Host: `www.mdpi.com`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_403` HTTP `403`
- Example attempted URLs: https://www.mdpi.com/2673-2688/6/8/194
- Manual focus: Use authenticated browser session (institution/login/cookies), then click native PDF control.
- Next step: Open article page and use built-in PDF button (JS/cookie). Prefer versioned PDF URL.

## #14 `EXSR0508` `2024-team-MahaMarathi-7B Marathi Large Language Model.md`
- URL: https://huggingface.co/marathi-llm/MahaMarathi-7B-v24.01-Base
- Host: `huggingface.co`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `not_pdf_header` HTTP `200`
- Example attempted URLs: https://huggingface.co/marathi-llm/MahaMarathi-7B-v24.01-Base
- Manual focus: Landing/resource page returned HTML. Extract actual PDF link from page and retry.
- Next step: Resource page. Find linked paper DOI/arXiv in model/dataset card.

## #15 `EXSR0379` `2025-Solidjonov-How do LLMs perform on Turkish.md`
- URL: https://www.semanticscholar.org/paper/97df3935f7098dbf1a4e13d343469cd01fa6888e
- Host: `www.semanticscholar.org`
- Reason to prioritize: best available candidate for this paper
- Last automated blocker: `http_202` HTTP `202`
- Example attempted URLs: https://www.semanticscholar.org/paper/97df3935f7098dbf1a4e13d343469cd01fa6888e
- Manual focus: Candidate is metadata/preview page; pivot to publisher/DOI PDF link.
- Next step: Metadata-only. Use linked DOI/arXiv/Publisher buttons to reach actual PDF source.

