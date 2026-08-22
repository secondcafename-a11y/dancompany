# 온동네 랜딩페이지 — 배포 폴더

## 올리는 방법
이 폴더 안의 내용을 **폴더 구조 그대로** 웹서버에 업로드하세요.
예) dancompany.co.kr/develop/ondongne/ 에 올리면
  - 한국어: /develop/ondongne/
  - 영어:   /develop/ondongne/ondongne_en.html
  - 일본어: /develop/ondongne/ondongne_jp.html

## 폴더 구성
- index.html          한국어 페이지
- ondongne_en.html    영어 페이지
- ondongne_jp.html    일본어 페이지
- assets/             이미지 (로고, 앱 스크린샷)
- _ds/                디자인 시스템 스타일시트
- support.js          페이지 렌더링 런타임

## 주의
- 파일을 하나만 올리면 이미지가 깨집니다. 폴더 전체를 올려주세요.
- 폰트는 Google Fonts에서 불러옵니다(인터넷 연결 필요).
- 문구를 고칠 때는 index.html / ondongne_jp.html 안의 해당 텍스트를 직접 수정하면 됩니다.
- 이미지 교체는 assets/ 안의 파일을 같은 이름으로 덮어쓰면 됩니다.

## 언어 링크
푸터의 한국어/日本語 링크는 같은 폴더 안의 파일을 가리킵니다.
한국어 / English / 日本語 세 페이지가 모두 같은 폴더 안에서 서로 연결됩니다.
