# 온동네 랜딩페이지 — 배포 폴더 (v2)

## 올리는 방법
이 폴더 안의 내용을 폴더 구조 그대로
  develop/ondongne/
경로에 올립니다. (기존 파일은 덮어쓰세요)

  - 한국어: dancompany.co.kr/develop/ondongne/
  - 영어:   dancompany.co.kr/develop/ondongne/ondongne_en.html
  - 일본어: dancompany.co.kr/develop/ondongne/ondongne_jp.html

## 폴더 구성
- index.html          한국어
- ondongne_en.html    영어
- ondongne_jp.html    일본어
- support.js          페이지 렌더링 런타임
- assets/             이미지 (로고, 앱 스크린샷)

## v1에서 바뀐 점 (이미지·스타일 깨짐 수정)
1. _ds 폴더를 없앴습니다.
   디자인 스타일을 각 HTML 안에 직접 넣었습니다.
   → 밑줄로 시작하는 폴더를 무시하는 호스팅에서도 정상 표시됩니다.
   서버에 남아 있는 기존 _ds 폴더는 삭제해도 됩니다.
2. 이미지와 스크립트 경로를 절대 경로(/develop/ondongne/...)로 바꿨습니다.
   → 주소 끝에 슬래시가 없어도(.../ondongne) 이미지가 깨지지 않습니다.

## 중요
경로가 /develop/ondongne/ 로 고정되어 있습니다.
다른 경로에 올리려면 HTML 안의 /develop/ondongne/ 을
새 경로로 모두 바꿔주세요.

## 수정 방법
- 문구: 각 HTML 파일에서 해당 텍스트를 직접 수정
- 이미지: assets/ 안의 파일을 같은 이름으로 덮어쓰기
- 폰트는 Google Fonts에서 불러옵니다(인터넷 연결 필요)
