# index.html(한국어) → en.html(영문) 생성기. 사용법: 저장소 루트에서 `python3 scripts/make_en.py`
# 한국어 문구를 바꾸면 아래 T 목록의 원문도 같이 고쳐야 한다. 실행 후 "missing"과 "hangul lines left"가 비어 있어야 한다.

import re,sys
src=open('index.html').read()
s=src
# --- structural changes ---
s=s.replace('<html lang="ko">','<html lang="en">',1)
# Intro film: English cut (media/intro-en.*) with English controls
for ko,en in [('<!-- ===== Intro film (30s) — 세션당 1회 재생, 건너뛰기 가능 ===== -->','<!-- ===== Intro film (30s) — plays once per session, skippable ===== -->'),
              ('aria-label="단컴퍼니 소개 영상"','aria-label="DANCOMPANY intro film"'),
              ("'🔊 소리 켜기':'🔇 소리 끄기'","'🔊 Sound on':'🔇 Sound off'"),
              ('🔊 소리 켜기</button>','🔊 Sound on</button>'),
              ('건너뛰기 →</button>','Skip →</button>'),
              ('/media/intro-ko-poster.jpg','/media/intro-en-poster.jpg'),
              ('/media/intro-ko.mp4','/media/intro-en.mp4'),
              ('/media/intro-ko.webm','/media/intro-en.webm')]:
    assert ko in s, ko
    s=s.replace(ko,en)
s=s.replace('<link rel="canonical" href="https://dancompany.co.kr/">','<link rel="canonical" href="https://dancompany.co.kr/en">')
s=s.replace('<meta property="og:url" content="https://dancompany.co.kr/">','<meta property="og:url" content="https://dancompany.co.kr/en">\n<meta property="og:locale" content="en_US">')
s=s.replace('<a href="index.html" hreflang="ko" lang="ko" aria-current="true">KO</a><a href="en.html" hreflang="en" lang="en" data-cta="lang-en">EN</a>',
            '<a href="index.html" hreflang="ko" lang="ko" data-cta="lang-ko">KO</a><a href="en.html" hreflang="en" lang="en" aria-current="true">EN</a>')
s=s.replace('"streetAddress":"다산중앙로82번길 15","addressLocality":"남양주시","addressRegion":"경기도"','"streetAddress":"15 Dasanjungang-ro 82beon-gil","addressLocality":"Namyangju-si","addressRegion":"Gyeonggi-do"')
s=s.replace('"name":"단컴퍼니 DANCOMPANY"','"name":"DANCOMPANY"')
s=s.replace('href="/develop/ondongne/"','href="/develop/ondongne/ondongne_en"')

T=[
# head
('DANCOMPANY | 종합 비즈니스 솔루션 파트너','DANCOMPANY | Integrated Business Solutions Partner'),
('경영 컨설팅, IT 시스템 구축, 글로벌 이커머스, 문화 콘텐츠(출판)를 하나로 묶어 고객사의 비즈니스 가치를 키우는 종합 비즈니스 솔루션 파트너, 단컴퍼니입니다.','DANCOMPANY brings management consulting, IT systems, global e-commerce and publishing together to grow the value of your business.'),
('경영에서 테크까지, 비즈니스의 한계를 넘습니다. 컨설팅 · IT 개발 · 글로벌 이커머스 · 출판.','From management to technology, we take your business further. Consulting · IT development · Global e-commerce · Publishing.'),
# comments
('APPS (bordered grid, connectednine 참고)','APPS (bordered grid, after connectednine)'),
('<!-- 기존 히어로 콜라주 4장 (Business 01–04) -->','<!-- Original hero collage (Business 01–04) -->'),
('<!-- 작은 사진 · 앱 아이콘 -->','<!-- Small photos · app icons -->'),
('<!-- ===== CONVERGENCE (4대 축) ===== -->','<!-- ===== CONVERGENCE ===== -->'),
# header/nav
('aria-label="주요 메뉴"','aria-label="Main menu"'),('aria-label="모바일 메뉴"','aria-label="Mobile menu"'),('aria-label="언어 선택"','aria-label="Language"'),
('aria-label="단컴퍼니 DANCOMPANY 홈"','aria-label="DANCOMPANY home"'),
("aria-label=\"메뉴 열기\"","aria-label=\"Open menu\""),
('>4대 축</a>','>Four Pillars</a>'),('>회사 소개</a>','>About</a>'),('>사업 영역</a>','>Services</a>'),('>만든 서비스</a>','>Our Products</a>'),('>솔루션 플래너</a>','>Solution Planner</a>'),
('href="#contact">문의</a>','href="#contact">Contact</a>'),
('data-cta="header">문의하기</a>','data-cta="header">Contact us</a>'),('data-cta="mobile-menu">문의하기</a>','data-cta="mobile-menu">Contact us</a>'),
('>전화하기</a>','>Call us</a>'),
# hero
('<small>Business 01</small>경영전략 &amp; 컨설팅 데스크','<small>Business 01</small>Strategy &amp; Consulting'),
('<small>Business 02</small>스마트 앱/웹 빌딩','<small>Business 02</small>App &amp; Web Building'),
('<small>Business 03</small>글로벌 물류 &amp; 유통망','<small>Business 03</small>Global Logistics &amp; Distribution'),
('<small>Business 04</small>문화 트렌드 &amp; 북 릴리즈','<small>Business 04</small>Culture &amp; Book Releases'),
('경영에서 테크까지<span class="inline-shots"','From management to tech<span class="inline-shots"'),
('<br>비즈니스의 한계를 넘습니다</h1>','<br>we take your business further</h1>'),
('경영 컨설팅, IT 시스템 구축, 글로벌 이커머스, 문화 콘텐츠(출판)를 하나로 묶어 고객사의 비즈니스 가치를 키우는 종합 비즈니스 솔루션 파트너입니다.','We bring management consulting, IT systems, global e-commerce and cultural content (publishing) together as one partner that grows the value of your business.'),
('분석만 하고 끝내지 않습니다. 전략을 세우고, 쇼핑몰과 앱을 직접 만들고, 해외 물류·유통과 출판까지 연결해 결과로 보여 드립니다.','We don’t stop at analysis. We set the strategy, build your store and app, and connect overseas logistics, distribution and publishing — then show you the results.'),
('aria-label="해결하고 싶은 일 입력"','aria-label="Tell us what you need"'),
('placeholder="어떤 일을 해결하고 싶으세요?" aria-label="해결하고 싶은 일"','placeholder="What do you want to get done?" aria-label="What you need"'),
('aria-label="문의 양식으로 이동"','aria-label="Go to the contact form"'),
('>솔루션 프로세스 확인</a>','>See the solution process</a>'),('>핵심 사업 영역 보기</a>','>Explore our services</a>'),
('aria-label="전화 상담"','aria-label="Call us"'),('<small>전화로 바로 상담하기</small>','<small>Talk to us by phone</small>'),
('<b>02-5212-2705</b>','<b>+82 2-5212-2705</b>'),
('data-cta="header-tel">02-5212-2705</a>','data-cta="header-tel">+82 2-5212-2705</a>'),
('>전화 걸기</a>','>Call now</a>'),('aria-label="아래로 이동"','aria-label="Scroll down"'),
# convergence
('4가지 성장의 축을 하나로 묶습니다','Four pillars of growth, working as one'),
('가치를 만드는 네 가지 영역을 함께 다룹니다. 맡긴 일만 처리하는 대행사가 아니라, 고객사가 도달해야 할 목표까지 함께 가는 파트너가 되겠습니다.','We cover the four areas that create value. Not an agency that only does what it’s handed, but a partner that goes all the way to the goals you need to reach.'),
('alt="유리 회의실에서 경영전략을 논의하는 장면"','alt="A team discussing strategy in a glass meeting room"'),
('<h3>경영전략 컨설팅</h3><p>체계적인 기업 경영 진단과 시장 진출(GTM) 전략을 세웁니다.</p>','<h3>Management Consulting</h3><p>Structured business diagnostics and go-to-market (GTM) strategy.</p>'),
('alt="앱과 웹 개발 화면"','alt="App and web development on screen"'),
('<h3>앱 &amp; 웹 개발</h3><p>트래픽이 몰려도 버티는 모바일·웹 서비스를 만듭니다.</p>','<h3>App &amp; Web Development</h3><p>Mobile and web services built to hold up under heavy traffic.</p>'),
('alt="글로벌 물류 창고"','alt="Global city skyline"'),
('<h3>글로벌 이커머스 유통</h3><p>해외 마켓 입점을 최적화하고 풀필먼트를 연동합니다.</p>','<h3>Global E-commerce</h3><p>Optimized overseas marketplace listings with fulfillment built in.</p>'),
('alt="출판 도서"','alt="A stack of books"'),
('<h3>문화 출판 비즈니스</h3><p>브랜드 철학을 담은 도서를 기획하고 펴냅니다.</p>','<h3>Cultural Publishing</h3><p>Books that carry your brand’s philosophy, planned and published.</p>'),
# about
('시장의 흐름을 따라가는 데서<br>멈추지 않고, 먼저 길을 냅니다','We don’t just follow the market —<br>we lead the way'),
('단컴퍼니(DANCOMPANY)는 빠르게 변하는 글로벌 시장에서 기업이 마주한 복잡한 문제를 풀고, 새로운 기회를 만들기 위해 세워졌습니다. 트렌드를 좇는 데 그치지 않고 시장 분석(Insight), 기술(Technology), 글로벌 네트워크(Global Network) 세 가지를 바탕으로 흐름을 먼저 만듭니다.','DANCOMPANY was founded to solve the complex problems companies face in a fast-moving global market and to create new opportunities. Rather than chasing trends, we set them — built on three foundations: Insight, Technology and a Global Network.'),
('<span>프로젝트 수직 매핑율</span>','<span>Vertical project mapping</span>'),
('<span>큐텐 · 아마존 · 쇼피 즉시 대응</span>','<span>Ready for Qoo10 · Amazon · Shopee</span>'),
('<h3>Insight · 분석과 통찰</h3><p>익숙한 관행 대신 정량화된 시장 데이터를 근거로, 비즈니스가 가야 할 방향을 잡습니다.</p>','<h3>Insight</h3><p>We set your direction with quantified market data, not habit.</p>'),
('<h3>Technology · 기술 혁신</h3><p>아이디어를 실제로 작동하는 빠른 반응형 웹과 모바일 앱으로 만듭니다.</p>','<h3>Technology</h3><p>We turn ideas into fast, responsive web and mobile apps that actually work.</p>'),
('<h3>Global Commerce · 세계로의 확장</h3><p>국경을 넘는 물류 연동과 글로벌 미디어를 결합해 브랜드 가치를 키웁니다.</p>','<h3>Global Commerce</h3><p>Cross-border logistics and global media, combined to grow your brand.</p>'),
# services
('사업 분야별 상세 안내','Our services in detail'),
('탭을 눌러 컨설팅부터 출판까지, 분야별로 실제 하는 일과 강점을 확인해 보세요.','Use the tabs to see what we actually do — and where we’re strongest — from consulting to publishing.'),
('aria-label="사업 분야"','aria-label="Business areas"'),
('<h4>우리가 잘하는 것</h4>','<h4>What we do best</h4>'),('<h4>주요 서비스</h4>','<h4>Key services</h4>'),
('진단 및 견적 신청하기 <svg>','Request a diagnosis &amp; quote <svg>'),
('<small>수직 계열 통합 완료</small><p>컨설팅 ➔ IT 개발 ➔ 물류 ➔ 유통 원스톱 대응</p>','<small>Fully integrated</small><p>Consulting ➔ IT ➔ Logistics ➔ Distribution, one stop</p>'),
('<h3>경영 컨설팅 &amp; 전략 마케팅</h3>','<h3>Management Consulting &amp; Strategic Marketing</h3>'),
('데이터로 시장을 읽고, 먼저 자리를 잡습니다','Read the market with data, and get there first'),
('이론 분석에서 멈추지 않고, 실제 매출 지표와 브랜드 가치가 오르도록 함께 실행하는 ‘실전형 파트너’입니다. 항공, 물류, 제조 등 여러 산업을 정밀하게 분석합니다.','We’re a hands-on partner: we don’t stop at theory, we execute with you until revenue and brand value actually rise. We analyze industries from aviation and logistics to manufacturing in depth.'),
('<li>기업 중장기 성장 전략과 시장 진출(Go-To-Market) 전략 수립</li><li>고객 세그먼트 분석과 통합 마케팅(IMC) 브랜드 디자인</li><li>퍼포먼스 마케팅 구조 분석과 광고 효율 개선</li>','<li>Mid- to long-term growth and go-to-market strategy</li><li>Customer segmentation and integrated marketing (IMC) brand design</li><li>Performance marketing audits and ad efficiency improvement</li>'),
('alt="경영 컨설팅 업무 장면"','alt="Consulting work in progress"'),
('<h3>스마트 앱/웹 개발 &amp; 시스템 구축</h3>','<h3>App/Web Development &amp; System Integration</h3>'),
('아이디어를 실제로 작동하는 서비스로 만듭니다','We turn ideas into services that work'),
('쓰기 편한 UX/UI 설계부터 안정적인 시스템 구조까지, 비즈니스의 기반을 단단하게 만듭니다. 최신 기술을 먼저 적용해 PC와 모바일 어디서나 끊김 없이 쓰는 반응형 플랫폼을 제공합니다.','From easy-to-use UX/UI to stable system architecture, we build a solid foundation for your business. We adopt the latest technology early to deliver responsive platforms that work seamlessly on desktop and mobile.'),
('<li>iOS·Android 앱 개발과 하이브리드 애플리케이션 구축</li><li>반응형 웹사이트와 랜딩페이지 제작</li><li>물류 관리(WMS), 대용량 결제(PG), 맞춤형 ERP 및 SI 시스템 통합</li>','<li>iOS and Android apps, including hybrid applications</li><li>Responsive websites and landing pages</li><li>Warehouse management (WMS), high-volume payments (PG), custom ERP and SI integration</li>'),
('alt="앱 UX 설계 작업"','alt="App UX design work"'),
('<h3>글로벌 이커머스 &amp; 유통 프로세스</h3>','<h3>Global E-commerce &amp; Distribution</h3>'),
('한국 브랜드를 전 세계 소비자의 일상으로 보냅니다','Bringing Korean brands into everyday life worldwide'),
('세계로 퍼지는 K-트렌드를 가장 정확한 방법으로 사업화합니다. 엄격한 품질 검증을 통과한 라이프스타일·뷰티 브랜드를 글로벌 유통망에 안착시킵니다.','We turn the global spread of K-trends into real business, the right way. Lifestyle and beauty brands that pass strict quality checks get established in global distribution channels.'),
('<li>큐텐(Qoo10), 아마존(Amazon), 쇼피(Shopee) 등 글로벌 마켓플레이스 입점과 자체 D2C 몰 운영</li><li>글로벌 물류·배송 프로세스 최적화와 주문 자동화 연동</li><li>패션·뷰티 부티크 연계 마케팅과 오프라인 쇼룸 활성화</li>','<li>Listings on Qoo10, Amazon, Shopee and other global marketplaces, plus your own D2C store</li><li>Optimized global logistics and shipping, with automated order flows</li><li>Fashion and beauty boutique marketing and offline showrooms</li>'),
('alt="패션 매장"','alt="A fashion store"'),
('<small>실시간 결제 모듈(WMS/PG) 탑재 가능</small><p>바로 구매로 이어지는 결제·물류 시스템을 함께 구축하고 연동합니다</p>','<small>Real-time payment modules (WMS/PG) available</small><p>We build and connect payment and logistics systems that turn visits into purchases</p>'),
('<h3>문화 콘텐츠 &amp; 출판 비즈니스</h3>','<h3>Cultural Content &amp; Publishing</h3>'),
('인사이트를 담은 책과 전자책, 미디어를 펴냅니다','Books, e-books and media full of insight'),
('시대를 읽는 주제로 도서를 기획하고, 기획부터 글로벌 유통까지 한 번에 해결합니다. 종이책과 전자책(e-book) 유통망으로 지식을 넓게 전하고, 온라인과 오프라인을 잇습니다.','We plan books on themes that read the times and handle everything from planning to global distribution. Through print and e-book channels we spread knowledge widely and connect online with offline.'),
('<li>비즈니스 인사이트·미니멀 라이프스타일 분야 도서 기획과 출판</li><li>국내외 도서·전자책(e-book) 유통 체계와 디지털 라이브러리 구축</li><li>유튜브, SNS 등 뉴미디어와 연계한 크로스 브랜딩 콘텐츠 제작</li>','<li>Planning and publishing books on business insight and minimal lifestyle</li><li>Domestic and global book and e-book distribution, and digital libraries</li><li>Cross-branding content for YouTube, social media and other new media</li>'),
('alt="서가와 도서"','alt="Bookshelves and books"'),
# built
('<h2 class="h2">운영하는 앱, 웹 서비스</h2>','<h2 class="h2">Apps &amp; web services we run</h2>'),
('aria-label="운영하는 앱, 웹 서비스"','aria-label="Apps and web services we run"'),
('고객사 일만 하지 않습니다. 웹 도구와 앱을 직접 기획하고 개발해서 운영합니다.','We don’t only work for clients. We plan, build and run our own web tools and apps.'),
('connectednine.com에서 보기','View on connectednine.com'),
('hwp 워드 변환<span class="meta">한글 파일을 Word로 · 무료 · 즉시 삭제</span>','HWP to Word<span class="meta">Convert Hangul files to Word · Free · Deleted instantly</span>'),
('<span class="meta">코드 하나로 기기 간 파일 전송 · 3분 후 삭제</span>','<span class="meta">Send files between devices with one code · Deleted after 3 min</span>'),
('카카오 AI 매니저<span class="meta">카카오톡 고객 문의 자동 응대 · 사업자용</span>','Kakao AI Manager<span class="meta">Automatic replies to KakaoTalk inquiries · For businesses</span>'),
('<span class="meta">폰을 맞대거나 QR로 건네는 디지털 명함</span>','<span class="meta">A digital business card, shared by tap or QR</span>'),
('샐러리매니저<span class="meta">소상공인 근로계약 · 급여관리 SaaS</span>','Salary Manager<span class="meta">Employment contracts &amp; payroll SaaS for small businesses</span>'),
('온동네<span class="meta">가격 없는 이웃 나눔 앱 · 한국 · 일본</span>','Ondongne<span class="meta">Price-free neighborhood sharing app · Korea · Japan</span>'),
# apps
('게임, 교육, 생산성, 스포츠까지. 기획부터 스토어 출시까지 직접 했습니다.','Games, education, productivity and sports. We took every one from idea to store launch ourselves.'),
('터치농구','Touch Hoop'),('바나나골프','Banana Golf'),('뽈뽈이 스터디','Ppolppoli Study'),('덧셈 부엉이','Addition Owl'),
('포레스트 프렌즈','Forest Friends'),('조리대','Joriday'),('말랑이 점프','Malang Jump'),('마이 골프루틴','My Golf Routine'),
('멘붕방지 골프스코어','AntiPanic Golf Score'),('브레인드롭','BrainDrop'),('바디라인','Bodyline'),
('<small>캐주얼 게임</small>','<small>Casual game</small>'),('<small>골프 용어</small>','<small>Golf terms</small>'),('<small>생산성</small>','<small>Productivity</small>'),
('<small>교육</small>','<small>Education</small>'),('<small>지역 커뮤니티</small>','<small>Local community</small>'),('<small>키즈 전용 To-do</small>','<small>To-do for kids</small>'),
('<small>레시피 추출</small>','<small>Recipe extraction</small>'),('<small>마이크로 숏폼</small>','<small>Micro short-form video</small>'),('<small>스포츠</small>','<small>Sports</small>'),
('<small>두뇌 게임</small>','<small>Brain game</small>'),('<small>디지털 명함</small>','<small>Digital business card</small>'),('<small>체중 내비게이션</small>','<small>Weight navigation</small>'),
(' 앱 아이콘"',' app icon"'),(' App Store에서 보기"',' on the App Store"'),(' Google Play에서 보기"',' on Google Play"'),
# collages
('<h2 class="h2">페이지 뷰</h2>','<h2 class="h2">Page View</h2>'),
('data-cta="collage-head">프로젝트 문의</a>','data-cta="collage-head">Start a project</a>'),
('alt="온동네 홈 화면"','alt="Ondongne home screen"'),('<b>APP · 온동네</b><small>모바일 앱 · 한국 · 일본</small>','<b>APP · Ondongne</b><small>Mobile app · Korea · Japan</small>'),
('APP 페이지로 이동','Go to APP page'),('alt="드롭쉐어 첫 화면"','alt="DropShare home screen"'),
('<small>계정 없이 기기 간 파일 전송</small>','<small>Device-to-device file transfer, no account</small>'),('WEB 페이지로 이동','Go to WEB page'),
('alt="샐러리매니저 첫 화면"','alt="Salary Manager home screen"'),('<b>SaaS · 샐러리매니저</b><small>근로계약 · 급여관리</small>','<b>SaaS · Salary Manager</b><small>Employment contracts · Payroll</small>'),
('SaaS 페이지로 이동','Go to SaaS page'),('alt="카카오 AI 매니저 화면"','alt="Kakao AI Manager screen"'),
('<b>AI · 카카오 AI 매니저</b><small>카카오톡 고객 응대 자동화</small>','<b>AI · Kakao AI Manager</b><small>Automated KakaoTalk customer service</small>'),
('btn-sm">서비스 보기</span>','btn-sm">View service</span>'),
# planner
('단컴퍼니 융합 비즈니스 프로세스','DANCOMPANY integrated business process'),
('해결하고 싶은 문제를 아래 카드에서 골라 주세요. 바로 실행할 수 있는 로드맵과 추천 방향을 보여 드립니다.','Pick the problem you want to solve below. We’ll show you a recommended direction and a roadmap you can act on right away.'),
('aria-label="진행 단계"','aria-label="Steps"'),
('<i>1</i>비즈니스 분야','<i>1</i>Your business'),('<i>2</i>우선 과제','<i>2</i>Top priority'),('<i>3</i>진단 결과','<i>3</i>Your result'),
('Q1. 어떤 분야의 비즈니스인가요?','Q1. What kind of business are you in?'),
('<b>뷰티 &amp; 라이프스타일 브랜드</b><small>감각 있는 브랜드와 이커머스 입점</small>','<b>Beauty &amp; lifestyle brand</b><small>Stylish brands and e-commerce listings</small>'),
('<b>IT 테크 &amp; 모바일 플랫폼</b><small>빠른 반응형 웹과 앱 개발</small>','<b>IT &amp; mobile platform</b><small>Fast, responsive web and app development</small>'),
('<b>글로벌 유통 &amp; 지식 출판</b><small>해외 크로스보더 몰과 도서 보급</small>','<b>Global distribution &amp; publishing</b><small>Cross-border stores and book distribution</small>'),
('>다음 단계로</button>','>Next</button>'),
('Q2. 가장 먼저 해결하고 싶은 과제는 무엇인가요?','Q2. What do you want to solve first?'),
('<b>브랜드 가치와 타깃 확장</b><small>경영 컨설팅과 데이터 기반 브랜드 기획</small>','<b>Grow brand value &amp; reach</b><small>Consulting and data-driven brand planning</small>'),
('<b>반응형 IT 시스템 고도화</b><small>웹 쇼핑몰·앱 개발과 PG/WMS 시스템 통합</small>','<b>Upgrade your IT systems</b><small>Web store and app development with PG/WMS integration</small>'),
('<b>해외 판로 개척 &amp; 출판 기획</b><small>아마존 크로스보더 입점과 도서 출간</small>','<b>Open overseas channels &amp; publish</b><small>Amazon cross-border listings and book publishing</small>'),
('>이전으로</button>','>Back</button>'),('>맞춤 진단 보기</button>','>See my result</button>'),
('💡 추천 실행 방향','💡 Recommended direction'),('<h4>추천 실행 로드맵</h4>','<h4>Recommended roadmap</h4>'),
('>다시 플래닝하기</button>','>Start over</button>'),('>이 로드맵으로 견적 문의하기</a>','>Request a quote for this roadmap</a>'),
# why
('왜 DANCOMPANY인가요?','Why DANCOMPANY?'),
('제안서에서 멈추지 않고, 매출 지표와 물류 프로세스까지 직접 연결해 실행하는 파트너입니다.','We don’t stop at the proposal. We connect sales metrics and logistics and execute them ourselves.'),
('<h3>통합 솔루션의 힘 (All-in-One)</h3>','<h3>The power of all-in-one</h3>'),
('전략 수립(컨설팅)부터 인프라 구축(IT 개발), 판매와 콘텐츠 확산(이커머스·출판)까지 비즈니스의 처음과 끝을 한 곳에서 해결합니다.','From strategy (consulting) and infrastructure (IT development) to sales and content (e-commerce and publishing), we handle your business from start to finish in one place.'),
('<h3>트렌드를 읽는 안목 (Trendsetters)</h3>','<h3>An eye for trends</h3>'),
('시장 변화에 빠르게 반응하고, 기술과 감각적인 비주얼을 함께 읽어 소비자가 원하는 다음 흐름을 먼저 준비합니다.','We react quickly to market shifts and read technology and visual culture together, so we’re ready for what customers want next.'),
('alt="모니터가 놓인 밝은 사무 공간"','alt="A bright office with monitors on the desks"'),
('<h3>실전 중심의 성과 (Result-Oriented)</h3>','<h3>Result-oriented</h3>'),
('이론에 그치는 보고서가 아니라 매출과 트래픽 같은 숫자로 가치를 증명합니다. 결제와 물류까지 연결된 구조로 성과를 높입니다.','No reports that end in theory — we prove value with numbers like revenue and traffic, and raise results with payments and logistics wired in.'),
# marquee
('컨설팅 ➔ IT 개발 ➔ 물류 ➔ 유통, 한 곳에서 다룹니다.','Consulting ➔ IT ➔ Logistics ➔ Distribution, all in one place.'),
('<span>성장 전략</span>','<span>Growth strategy</span>'),('<span>IMC 브랜딩</span>','<span>IMC branding</span>'),('<span>퍼포먼스 마케팅</span>','<span>Performance marketing</span>'),
('<span>반응형 웹</span>','<span>Responsive web</span>'),('<span>PG 결제</span>','<span>PG payments</span>'),('<span>D2C 몰</span>','<span>D2C stores</span>'),
('<span>풀필먼트</span>','<span>Fulfillment</span>'),('<span>도서 기획</span>','<span>Book planning</span>'),('<span>전자책</span>','<span>E-books</span>'),('<span>유튜브</span>','<span>YouTube</span>'),
# contact
('글로벌 비즈니스의 시작,<br>함께하겠습니다','Let’s start your<br>global business together'),
('기획과 분석, IT 시스템 구축, 해외 입점과 유통까지 한 창구에서 해결합니다. 아래 양식을 남겨 주시면 분야별 담당자가 직접 연락드립니다.','Planning and analysis, IT systems, overseas listings and distribution — all through one point of contact. Fill in the form and the right specialist will get back to you directly.'),
('<small>온동네</small>','<small>Ondongne</small>'),('<small>샐러리매니저</small>','<small>Salary Manager</small>'),
('<span>경기도 남양주시 다산중앙로82번길 15<br>15 Dasanjungang-ro 82beon-gil, Namyangju-si, Gyeonggi-do, Korea</span>','<span>15 Dasanjungang-ro 82beon-gil, Namyangju-si, Gyeonggi-do, Republic of Korea</span>'),
('<a href="tel:0252122705">02-5212-2705</a>','<a href="tel:+82252122705">+82 2-5212-2705</a>'),
('<h3>사전 진단 의뢰</h3>','<h3>Request a free diagnosis</h3>'),
('>성함 / 담당자 *</label>','>Name *</label>'),('placeholder="홍길동"','placeholder="Jane Doe"'),('>이메일 *</label>','>Email *</label>'),
('>회사명</label>','>Company</label>'),('placeholder="회사나 브랜드 이름"','placeholder="Company or brand name"'),
('<legend>관심 있는 사업 분야 (여러 개 선택 가능)</legend>','<legend>Areas of interest (choose any)</legend>'),
('value="Business 01. 경영 컨설팅 & 전략 마케팅" data-key="consulting"><span>01 경영 컨설팅 · 마케팅</span>','value="Business 01. Management Consulting & Strategic Marketing" data-key="consulting"><span>01 Consulting · Marketing</span>'),
('value="Business 02. 스마트 앱/웹 개발 & 시스템 구축" data-key="it_system"><span>02 앱/웹 개발 · 시스템</span>','value="Business 02. App/Web Development & System Integration" data-key="it_system"><span>02 App/Web · Systems</span>'),
('value="Business 03. 글로벌 이커머스 & 유통" data-key="ecommerce"><span>03 글로벌 이커머스</span>','value="Business 03. Global E-commerce & Distribution" data-key="ecommerce"><span>03 Global E-commerce</span>'),
('value="Business 04. 문화 콘텐츠 & 출판" data-key="publishing"><span>04 콘텐츠 · 출판</span>','value="Business 04. Cultural Content & Publishing" data-key="publishing"><span>04 Content · Publishing</span>'),
('value="아직 모르겠어요" data-key="unsure"><span>아직 모르겠어요</span>','value="Not sure yet" data-key="unsure"><span>Not sure yet</span>'),
('>협업 목표 · 인프라 목표 *</label>','>Your goals *</label>'),
('placeholder="지금 겪고 있는 어려움과 원하는 성과 목표를 편하게 적어 주세요."','placeholder="Tell us what you’re struggling with and the results you want."'),
('보내기를 누르면 메일 앱이 열립니다. 내용을 확인하고 전송해 주세요.','Your email app will open. Check the message and hit send.'),
('>단컴퍼니에 솔루션 의뢰하기</button>','>Send to DANCOMPANY</button>'),
('<b>사전 진단 의뢰가 준비됐습니다</b><p>메일 앱에서 전송하시면 분야별 담당자가 목표 과제와 현재 상황을 검토한 뒤, 24시간 안에 솔루션 회신 메일을 보내 드립니다. 메일 앱이 열리지 않았다면 contact@dancompany.co.kr 으로 직접 보내 주세요.</p>','<b>Your request is ready</b><p>Once you send it from your email app, the right specialist will review your goals and situation and reply within 24 hours. If your email app didn’t open, write to contact@dancompany.co.kr directly.</p>'),
# footer
('경영에서 테크까지,<br>함께 시작해요','From management to tech,<br>let’s get started'),
('경영 전략 컨설팅, 글로벌 미디어 출판, IT 인프라 시스템 구축을 하나로 묶은 종합 비즈니스 솔루션 파트너.','An integrated business solutions partner for strategy consulting, global media and publishing, and IT infrastructure.'),
('data-cta="footer">문의하기</a>','data-cta="footer">Contact us</a>'),
('aria-label="바로가기"','aria-label="Quick links"'),('<h4>바로가기</h4>','<h4>Quick links</h4>'),('aria-label="서비스"','aria-label="Services"'),('<h4>서비스</h4>','<h4>Services</h4>'),
('>온동네</a>','>Ondongne</a>'),('>샐러리매니저</a>','>Salary Manager</a>'),
('상호명 DANCOMPANY · 대표자명 Daniel Byun<br>','DANCOMPANY · CEO Daniel Byun<br>'),('사업자등록번호 691-24-02116<br>','Business Registration No. 691-24-02116<br>'),
('📞 TEL 02-5212-2705','📞 TEL +82 2-5212-2705'),
# JS
("o?'메뉴 닫기':'메뉴 열기'","o?'Close menu':'Open menu'"),
("var ex=['어떤 일을 해결하고 싶으세요?','예) 일본 Qoo10에 화장품 입점','예) 쇼핑몰과 결제·물류 연동','예) 회사 소개 앱 개발','예) 브랜드 이야기를 담은 책 출간'];",
 "var ex=['What do you want to get done?','e.g. Sell cosmetics on Qoo10 Japan','e.g. Connect payments and logistics to my store','e.g. Build an app for my company','e.g. Publish a book about our brand'];"),
("msg.value='해결하고 싶은 일: '+v+'\\n\\n';","msg.value='What I need: '+v+'\\n\\n';"),
("msg.value='['+title+'] 맞춤 제안과 예산 계획에 대한 사전 진단을 요청합니다.';","msg.value='['+title+'] I’d like a preliminary diagnosis with a tailored proposal and budget plan.';"),
("consulting_marketing:{title:'DAN 브랜드 부스터 & 마켓 진입 패키지',sub:'경영 전략 분석 ➔ 타깃 설계 ➔ 미디어 연계 전개',desc:'시장 진입 초기의 위험 요소를 줄이고, 브랜드 정체성을 한 단계 끌어올리는 통합 플랜입니다.'",
 "consulting_marketing:{title:'DAN Brand Booster & Market Entry Package',sub:'Strategy analysis ➔ Target design ➔ Media rollout',desc:'An integrated plan that reduces early market-entry risk and lifts your brand identity to the next level.'"),
("steps:['정량 데이터 분석으로 타깃 시장을 정밀하게 분류','비주얼 마케팅 중심의 반응형 랜딩페이지 고도화','글로벌 인플루언서 네트워크와 연계한 IMC 론칭 캠페인']",
 "steps:['Segment your target market precisely with quantitative data','Upgrade a responsive, visual-first landing page','Launch an IMC campaign with a global influencer network']"),
("it_system_dev:{title:'하이브리드 모바일 앱 & 지능형 WMS 통합 패키지',sub:'안정성 99.9% 목표 모바일 결제망 ➔ 물류 자동 연동',desc:'불안정한 기존 시스템의 한계를 보완하고, 해외 고객도 빠르고 편하게 구매할 수 있는 구매 환경을 만드는 구축안입니다.'",
 "it_system_dev:{title:'Hybrid Mobile App & Smart WMS Integration Package',sub:'Mobile payments targeting 99.9% uptime ➔ Automated logistics',desc:'A build plan that fixes the limits of unstable legacy systems and gives overseas customers a fast, easy way to buy.'"),
("steps:['iOS·Android 대응 하이브리드 앱 개발 기획','트래픽에 맞춰 자동으로 늘어나는 클라우드 결제 시스템 구축','창고 관리(WMS)와 사내 ERP 연동으로 실시간 자동화']",
 "steps:['Plan and build a hybrid app for iOS and Android','Set up a cloud payment system that scales with traffic','Automate in real time by connecting WMS and your ERP']"),
("global_crossborder:{title:'K-트렌드 글로벌 풀필먼트 & 미디어 브랜드 에디션',sub:'해외 몰 포지셔닝 ➔ 글로벌 유통 ➔ 출판 브랜딩 연동',desc:'미주·유럽·아시아 D2C 시장에 자체 제품과 브랜드 가치를 담은 책·미디어를 함께 내보내는 크로스보더 패키지입니다.'",
 "global_crossborder:{title:'K-Trend Global Fulfillment & Media Brand Edition',sub:'Overseas store positioning ➔ Global distribution ➔ Publishing-led branding',desc:'A cross-border package that takes your products — and books and media about your brand — into D2C markets in the Americas, Europe and Asia.'"),
("steps:['아마존 글로벌 FBA 연동과 풀필먼트 물류 최적화','브랜드 가치를 담은 에디토리얼 북 제작과 미디어 믹스 유통','구매로 바로 이어지는 숏폼 SNS 마케팅 자동화']",
 "steps:['Connect Amazon Global FBA and optimize fulfillment','Produce an editorial brand book and distribute it across media','Automate short-form social marketing that drives purchases']"),
("msg.value='[솔루션 플래너 진단 결과]\\n선택 솔루션: '+current.title+'\\n로드맵에 따른 상세 견적과 타당성 분석 회신을 원합니다.';",
 "msg.value='[Solution Planner result]\\nSelected solution: '+current.title+'\\nPlease send a detailed quote and feasibility review for this roadmap.';"),
("var subject='[홈페이지 사전 진단 의뢰] '","var subject='[Website inquiry] '"),
("var body=['성함/담당자: '+f.name.value.trim(),'이메일: '+f.email.value.trim(),'회사명: '+(f.company.value.trim()||'-'),'관심 분야: '+(sv.join(', ')||'-'),'','협업 목표 · 인프라 목표:',f.message.value.trim()]",
 "var body=['Name: '+f.name.value.trim(),'Email: '+f.email.value.trim(),'Company: '+(f.company.value.trim()||'-'),'Areas of interest: '+(sv.join(', ')||'-'),'','Goals:',f.message.value.trim()]"),
]
T.append(('온동네','Ondongne'))
missing=[]
for ko,en in T:
    if ko not in s: missing.append(ko[:60]); continue
    s=s.replace(ko,en)
# generic leftovers in comments
s=s.replace('href="tel:0252122705"','href="tel:+82252122705"')
left=[(i+1,l.strip()[:120]) for i,l in enumerate(s.split('\n')) if re.search('[가-힣]',l)]
open('en.html','w').write(s)
print('missing:',missing); print('hangul lines left:',len(left)); [print(x) for x in left]
