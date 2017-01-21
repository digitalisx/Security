위 프로그램은 사용자의 이미지 파일(ewf, dd)을 입력하여 원하는 옵션에 맞추어 파일을 추출하는 프로그램입니다.

사용을 위한 환경은 다음과 같습니다.

- Windows7 64bit 이상
- Python 2.7.X의 환경 설치
- Pytsk3 및 Pyewf 모듈이 설치되어 있어야 함

Pytsk3 : https://github.com/log2timeline/l2tbinaries/blob/master/win32/pytsk3-20160721.1.win32-py2.7.msi
Pyewf : https://github.com/log2timeline/l2tbinaries/blob/master/win32/pyewf-20140608.1.win32-py2.7.msi

사용을 위해서는 실행 화면에서 분석하고자 하는 이미지 파일의 경로나 파일 명을 입력하여주면 됩니다. (screenshot 파일을 참조하셔도 좋습니다)
(cmd를 통해서 압축 해제한 폴더로 이동하신 뒤 코드를 실행시키면 더욱 좋습니다)

옵션을 통해 원하는 파일만 추출 할 수 있습니다. 옵션 파일은 Python 2.7의 문법을 따르며

file_size, file_extension, modified_time, created_time, accessed_time, edited_time, file_path를 이용하여 사용자가 원하는 대로 조정할 수 있습니다.

압축 파일 내부에 예시 옵션 파일이 존재하며 의미는 다음과 같습니다.


(file_size >= 10000 and file_extension == ".pdf") and (not bool(re.search("windows", file_path)) or bool(re.search("2011", str(modified_time))))


파일의 크기가 10,000 이상이며 확장자를 ".PDF"로 가지는 파일 중에 파일 경로에 "windows"라는 폴더가 없거나 Modified Time이 2011년경인 경우만 필터링하라.

실행 결과 예시 이미지 파일에서 위 조건에 맞는 파일만 선정하여 추출하여  extract_files라는 폴더 안에 3개의 PDF 파일이 추출되었음을 볼 수 있습니다.
또한 report.csv 파일에서 추출한 파일에 대한 7가지 정보 (MACE Time, 확장자, 파일 크기, 전체 경로)를 출력해주었음을 볼 수 있습니다.

