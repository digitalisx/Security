1) 파일 정보

파일 이름 : gmail_parse.py

파일 크기 : 7579 Bytes

Hash (MD5) : FEBFF4A2F45D45E8346FAD94E6A657E4
Hash (SHA1) : 067ADD96CDB14D63F3689A7CE5A05B30E0212825


2) 필수 설치 모듈

Gmail (https://github.com/charlierguo/gmail)

PIL (http://www.pythonware.com/products/pil/)


3) 사용 목적

Gmail과 연동하여 수신받은 메일에 포함된 링크를 통해 파일 다운로드 및 정보 추출


4) 동작 과정

(1) Result 폴더 및 일자 폴더 체크 및 생성

(2) 오늘의 일자 받아오기

(3) DB 파일 및 테이블 생성

(4) CSV 파일 및 생성

(5) Gmail 로그인 및 메일 조회

(6) URL 정보 추출 및 파일 다운로드

(7) 파일 종류 체크 및 GPS 정보 추출

(8) 파일 Hash 값 추출

(9) 추출한 정보를 DB에 기입

(10) 해당 일자의 모든 메일에 대한 정보를 받아오며 반복

(11) GPS 정보를 기반으로 지도 파일 생성 및 다운로드

(12) 반복하여 수집한 DB를 저장하고 전체 여행 경로 작성
