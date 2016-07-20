# -*- coding: utf-8 -*-

import os # OS 모듈 Import
import os.path # OS.PATH 모듈 Import
import csv # CSV 모듈 Import

file_type = [] # File 확장자 추출에 사용될 리스트 선언
file_type_list = [] # File 확장자 수집할 리스트 선언

file_size = 0 # File 크기 변수

file_dict = dict() # 확장자 별 정보를 저장할 Dictionary 선언

def csv_make(): # .csv 파일을 만들고 읽어들일 함수 선언

    global file_csv # file_csv 변수에 대해 전역 변수 선언

    file_csv = open("report.csv","w") # report.csv 파일을 생성해서 오픈
    
    print "[!] Make CSV File !" # 파일 생성 시, 알림 메시지 출력

def csv_write(): # 생성된 csv 파일에 기록하는 함수 선언

    global file_csv # 전역 변수 file_csv 사용

    file_csv.write("File Extensions" + ", " + "Total Size (Byte)" + ", " + "Count" + "\n") # csv 파일 첫 줄에 분류를 위한 표 작성

    for cov_file_type in file_dict.keys(): # 딕셔너리 키 값들을 cov_file_type에 대입 반복

        if cov_file_type == "": # cov_file_type 값이 존재하지 않는다면 / 확장자가 존재 하지 않는 파일을 분류
        
            file_csv.write("None Extension Files" + ", " + str(file_dict[cov_file_type][0]) + ", " + str(file_dict[cov_file_type][1]) + "\n") # 확장자가 없는 파일에 대하여 파일 크기 합과 개수 출력
    
        else: # 존재한다면

            file_csv.write(cov_file_type + ", " + str(file_dict[cov_file_type][0]) + ", " + str(file_dict[cov_file_type][1]) + "\n") # 확장자 마다 분류하여 파일 크기 합과 개수 출력

    print "[!] All Process is Finish, Thank you!" # 프로그램 종료 메시지 출력

def main(drive_name): # 파일 정보를 추출 및 가공할 Main 함수 선언
    
    try: # 예외 처리 활용을 위한 try문 사용

        scan_drive = os.listdir(drive_name) # main 함수 인자 값을 이용하여 드라이브의 디렉토리 scan_drive에 저장

        for file_name in scan_drive: # scan_drive의 값을 file_name에 for문으로 대입 & 반복

            full_file_name = os.path.join(drive_name, file_name) # 받은 드라이브의 값과 파일 이름을 결합하여 경로 생성
        
            if os.path.isdir(full_file_name): # 만들어진 경로가 디렉토리인지 파일인지 판단
            
                main(full_file_name) # 디렉토리인 경우 무시하고 Main 함수 반복
            
            else: # 파일인 경우 실행
            
                file_size = os.path.getsize(full_file_name) # 해당 경로의 파일 크기 값 저장     
                file_type = os.path.splitext(full_file_name)[-1].split(",")[0] # splitext로 파일 명에서 확장자 분리 및 오류 값 처리
                cov_file_type = file_type.lower() # 파일 확장자를 소문자로 처리 
            
                if cov_file_type in file_dict: # 파일 확장자 Dictionary 안에 파일 확장자가 존재 시
                
                    file_dict[cov_file_type][0] = file_dict[cov_file_type][0] + file_size # 파일 크기 값을 불러오는 대로 값을 Dictionary에 추가 시켜줌
                    file_dict[cov_file_type][1] = file_dict[cov_file_type][1] + 1 # 파일 개수 값을 불러오고 추가하는 대로 개수를 Dictionary에서 상승 시킴
                
                else: # 존재하지 않는다면
            
                    file_dict[cov_file_type] = [0,1] # Dictionary에 없는 새로운 확장자 등록
                    file_dict[cov_file_type][0] = file_size # Dictionary에 새로 등록된 확장자에 대해 파일 크기 값 대입
    
    except: # 예외 발생 시
        
        pass # 무시하고 통과

csv_make() # csv_make 함수 실행 

destination_drive = raw_input("[!] Input Mounted Drive Path : ") # 분석을 원하는 마운트 된 드라이브 경로 입력

print "[!] Wait a minute, Please do not open CSV file" # CSV 파일을 열지말라는 경고 메시지 출력

main(destination_drive) # 입력받은 드라이브 경로를 Main 함수에 대입 및 실행

csv_write() # csv_write 함수 실행