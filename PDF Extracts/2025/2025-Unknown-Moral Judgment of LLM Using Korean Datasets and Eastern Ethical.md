---
title: "2025-Unknown-Moral Judgment of LLM Using Korean Datasets and Eastern Ethical - PDF Extract"
source_pdf: "2025-Unknown-Moral Judgment of LLM Using Korean Datasets and Eastern Ethical.pdf"
pages: 2
extracted_at: "2026-02-13T22:00:46.646617"
---

# PDF Extract: 2025-Unknown-Moral Judgment of LLM Using Korean Datasets and Eastern Ethical

**Source PDF:** 2025-Unknown-Moral Judgment of LLM Using Korean Datasets and Eastern Ethical.pdf
**Total Pages:** 2

---

## Content

```
--- Page 1 ---

1. 서론
LLM의등장은인간의사고를보조하거나대체할
수준으로발전하며, 판단을내릴가능성도제기되고
있다. 이에따라LLM의도덕적편향성을이해하는
것이중요한연구과제가되었다. 본연구에서는주
로영어로학습된LLM이저자원언어인한국어데
이터셋에서보이는도덕적편향성을실험적으로분
석한다. 또한, 동양윤리정책적용시모델의응답
이서양윤리정책과어떻게다른지를비교하여도
덕적판단의문화적·언어적영향을탐구한다.
2. 관련연구
Fridman et al.(2024)는LLM의도덕적판단이인
간과다르며, 모델크기가커질수록인간과유사성
이증가하는경향을실험적으로입증했다. 연구진은
공리주의적
도덕
딜레마를
통해
다양한
규모의
LLM을분석한결과, 작은모델일수록인간과차이
가크고, 대규모모델이정교한도덕적추론을수행
함을확인했다.
Agarwal et al.(2024)는LLM의학습언어와자원
수준에따라도덕적판단과편향성이달라짐을분석
했다. 영어에서는윤리정책과의일관성이유지되었
으나, 저자원언어에서는편향성이커지고일관성이
낮아지는경향이나타났다. 또한, 같은모델이라도
입력언어에따라도덕적판단이달라져, LLM이단
순규칙이아닌언어·문화적맥락의영향을받음을
시사한다.
3. 본론
Agarwal et al.(2024) 논문에서는주로영어로학습
된LLM이다자원언어환경에서4가지윤리적딜
레마를서양윤리(덕윤리, 의무론, 결과주의) 정책
과함께제공받았을때, 저자원언어환경보다편향
성이적고정확도가높은경향을보였다. 본연구에
서는이러한특성을기반으로, 다자원(영어) 및저자
원(한국어) 환경에서LLM이서양윤리와동양윤리
(유교윤리, 도교윤리, 불교윤리) 정책을적용받았
을때편향성의차이를실험적으로분석하였다. 이
를통해LLM의도덕적판단이언어적·문화적맥락
에따라어떻게달라지는지관찰하고, 편향성을규
명하는것이본연구의주요목표이다.
4. 실험
실험은OpenAI의API 키를활용하여진행되었으며,
한국어동양윤리원칙을활용한LLM의도덕적
판단연구
유준호1, 신유현2
1인천대학교컴퓨터공학부학부생
2인천대학교컴퓨터공학과교수
yoojuneho0723@inu.ac.kr,
yhshin@inu.ac.kr
Moral Judgment of LLM Using Korean Datasets
and Eastern Ethical Principles
Junho-Yoo1, Youhyun Shin2
1Dept. of Computer Science, Incheon National University
2Dept. of Computer Science, Incheon National University
요
약
대규모언어모델(LLM)의발전으로인간의사고를대체할가능성이커지며, 도덕적판단에대한관
심도증가하고있다. 그러나영어중심으로학습된LLM의특성상, 한국어의적용과동양윤리원칙
에대한연구는미비한상황이다. 본연구에서는LLM의도덕적편향을분석하고, 저자원·고자원언
어환경및동·서양윤리정책적용시편향변화여부를실험적으로검증하였다. 이를통해LLM의
도덕적판단이언어·문화적요인에따라어떻게영향을받는지를규명하고자한다. 실험결과, LLM
의도덕적판단이언어적·문화적맥락에따라달라질수있음을확인하였으며, 이러한연구결과는
AI 윤리가이드라인수립과콘텐츠검열정책개선에기여할수있을것으로기대된다.
ASK 2025 학술발표대회 논문집 (32권 1호)
- 520 -

--- Page 2 ---

모델로는GPT-3.5-Turbo-0125와GPT-4-0613을사
용하였다.
모든실험에서동일한하이퍼파라미터를
적용하였으며, Temperature는0, Top Probability는
0.95, Presence Penalty는1로설정하였다.
4-1. 데이터셋
본연구에서는Abhinav Rao et al.(2023)의논문에
서제공한딜레마와프롬프트를활용하여실험을진
행하였으며, Agarwal et al.(2024)의연구와동일하
게구글번역기를이용하여한국어데이터셋을생성
하여사용하였다.
4-2. 결과및분석
4-2-1. LLM의기본실험
<표1>은모델에정책없이도덕적딜레마만제공
한후, 자체적인윤리적판단을분석한결과를나타낸
다. 모델은"해야한다", "하면안된다", "결정할수
없다"의세가지응답중하나를선택해야한다. 기본
실험에서는4개의딜레마에대해6가지옵션순열을
생성하고, 각모델당5회씩반복하여수행하였다.
<표1> LLM의기본성능비교
Heinz
Monica
Rajesh
Timmy
GPT-3.5-Turbo-0125
English
100%
100%
100%
90%
Korean
60%
100%
100%
100%
GPT-4-0613
English
100%
100%
60%
100%
Korean
100%
100%
100%
83.3%
<표1>에서파란색은“해야한다”, 빨간색은“하면안
된다”, 그리고노란색은“결정할수없다“이다. 본실험
결과는LLM의도덕적판단이입력언어에따라달라
질수있음을시사한다.
4-2-2. 윤리정책을통한편향성실험
<표2>는동양및서양윤리정책이제공될때모
델의편향성을나타내는히트맵이다. 편향성은<표
1>에서확인된기본선호도와반대되는윤리정책
을적용했을때, 모델이기존선호도를얼마나유지
하는지를
기준으로
측정하였다.
GPT-3.5-Turbo의
경우, 영어보다한국어에서편향성이같거나더낮
은경향을보인다. 특히, 한국어에서는특정딜레마
에서편향성이극단적으로높거나낮은패턴이확인
된다. 반면, GPT-4는전반적으로편차가줄어들었
으며, 다자원언어인영어에서편향성이더적게나
타난다. 이러한결과는기존연구에서보고된실험
결과와일치한다.
5. 결론
본연구에서는LLM이내재적으로지닌도덕적가
치와편향성을분석하였다. 실험결과, 특정윤리정
책이적용될때, 특정언어환경에서는편향성이감
소하는경향이확인되었다. 이는모델이특정언어
로학습하는과정에서해당언어의사회적·도덕적
규범이내재되었기때문으로해석할수있다. 또한,
모델의크기가커질수록이러한편향성이점진적으
로감소하는경향도관찰되었다.
이번연구는LLM의도덕적판단이언어적·문화적
맥락에따라달라질수있으며, 모델의규모가윤리
적편향성에영향을미칠수있음을시사한다. 향후
연구에서는
다양한
언어와
윤리
정책을
확장하여
LLM의도덕적판단메커니즘을더욱심층적으로
분석할필요가있다.
<표2> 윤리적정책에따른LLM의편향성비교
사사문구
이 논문은 정부(과학기술정보통신부)의 재원으로 정보
통신기획평가원–학·석사연계ICT핵심인재양성 
지원을 
받아 수행된 연구임(IITP-2025-RS-2023-00260175)
참고문헌
[1] Agarwal, U. et al. (2024). Ethical Reasoning and Moral
Value Alignment of LLMs Depend on the Language We
Prompt Them in. LREC-COLING 2024, 6330–6340.
[2] Rao, A. et al. (2023). Ethical Reasoning over Moral
Alignment: A Case and Framework for In-Context Ethical
Policies in LLMs. Findings of ACL: EMNLP 2023, 13370–
13388.
[3] Marraffini, G. F. G. et al. (2024). The Greatest Good
Benchmark: Measuring LLMs’ Alignment with Utilitarian
Moral Dilemmas. EMNLP 2024, 21950–21959.
ASK 2025 학술발표대회 논문집 (32권 1호)
- 521 -

```
