# -*- coding: utf-8 -*-

import os # OS 모듈 Import
import os.path # OS.PATH 모듈 Import
import csv # CSV 모듈 Import

file_type = [] # File 확장자 추출에 사용될 리스트 선언
file_type_list = [] # File 확장자 수집할 리스트 선언

file_count = 0 # File 개수 변수
file_size = 0 # File Size 변수
file_total_size = 0 # 확장자 별 File Size 총 합 변수

file_dict = dict() # 확장자 별 정보를 저장할 Dictionary 선언

def csv_make(): # .csv 파일을 만들고 읽어들일 함수 선언

    global file_csv # file_csv 변수에 대해 전역 변수 선언

    file_csv = open("report.csv","w") # report.csv 파일을 생성해서 오픈
    
    print "[!] Make CSV File !" # 파일 생성 시, 알림 메시지 출력

def main(drive_name): # 파일 정보를 추출 및 가공할 Main 함수 선언
    
    try: # 예외 처리 활용을 위한 try문 사용

        scan_drive = os.listdir(drive_name) # main 함수 인자 값을 이용하여 드라이브의 디렉토리 scan_drive에 저장

        for file_name in scan_drive: # scan_drive의 값을 file_name에 for문으로 대입 & 반복

            full_file_name = os.path.join(drive_name, file_name)
        
            if os.path.isdir(full_file_name):
            
                main(full_file_name)
            
            else:
            
                file_size = os.path.getsize(full_file_name)     
                file_type = os.path.splitext(full_file_name)[-1].split(",")[0]
                cov_file_type = file_type.lower()
            
                if cov_file_type in file_dict:
                
                    file_dict[cov_file_type][0] = file_dict[cov_file_type][0] + file_size
                    file_dict[cov_file_type][1] = file_dict[cov_file_type][1] + 1
                
                else:
            
                    file_dict[cov_file_type] = [0,1]
    
    except:
        
        pass

def csv_write():

    global file_csv

    file_csv.write("File Extensions" + ", " + "Total Size" + ", " + "Count" + "\n")

    for cov_file_type in file_dict.keys():
    
        if cov_file_type == "":
        
            file_csv.write("None Extension Files" + ", " + str(file_dict[cov_file_type][0]) + ", " + str(file_dict[cov_file_type][1]) + "\n")
    
        else:

            file_csv.write(cov_file_type + ", " + str(file_dict[cov_file_type][0]) + ", " + str(file_dict[cov_file_type][1]) + "\n")

    print "[!] All Process is Finish, Thank you!"

csv_make()

destination_drive = raw_input("[!] Input Mounted Drive Path : ") 

print "[!] Wait a minute, Please do not open CSV file"

main(destination_drive)

csv_write()