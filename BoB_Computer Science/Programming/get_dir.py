# -*- coding: utf-8 -*-

import os # os 모듈 사용을 위해 Import

Dir = raw_input("\nInput Directory name :") # Dir 변수에 디렉토리 값 받기 

directory = [] # 빈 Directory 리스트 선언
file = [] # 빈 File 리스트 선언
   
result = os.listdir(Dir) # 현재 디렉토리의 값들을 Result에 저장

for path in result: # Result 리스트의 값을 Path에 대입 & 반복
      
   if os.path.isdir(os.path.join(Dir,path)): # path와 Dir을 경로로 만들어 디렉토리와 파일을 구분
        
      directory.append(path) # 해당하는 path의 값을 Directory 리스트에 저장
     
   else: # False 값을 반환 받을 시
         
      file.append(path) # 해당하는 path의 값을 file 리스트에 저장 

directory.sort() # Directory 리스트를 정렬
file.sort() # File 리스트를 정렬

print "\nSub Directory\n" # 현재 디렉토리의 서브 디렉토리들을 출력

for dirs in directory: # Directory 리스트의 값들을 dirs에 대입 & 반복
   print '[+] Dir : ', dirs # dirs의 값을 출력

print "\nCurrent Directory Files\n" # 현재 디렉토리의 파일들을 출력

for files in file: # File 리스트의 값들을 Files에 대입 & 반복
   print '[-] File : ',files # Files의 값을 출력